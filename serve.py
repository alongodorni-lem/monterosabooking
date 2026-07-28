#!/usr/bin/env python3
"""Static file server with same-origin proxy for the booking REST API.

Usage:
  python serve.py
  # then open http://127.0.0.1:8765/

  Production (Render): set PORT and PLANYO_API_KEY env vars.

Proxies GET /api/planyo?...  ->  https://www.planyo.com/rest/?...
Also accepts /api/planyo-proxy.php?... for parity with PHP hosting.
Injects PLANYO_API_KEY from the environment when the client omits api_key
(so the key need not be committed to the repo).

Image resize proxy: GET /api/img?u=<https-url>&w=640&q=72
Fetches allowlisted Planyo/S3 images, resizes/compresses to WebP (JPEG
fallback), and caches on disk under .cache/img/. Cuts multi‑MB PNGs down
to ~30–80KB card thumbnails.

Long-lived in-memory cache (PROXY_CACHE_TTL_SEC, default 12h) for safe
read methods: list_resources / get_event_times / get_resource_info /
resource_search. api_test is never cached. Cache key = method + sorted
query params (api_key excluded). Cleared on process restart, or via
GET /api/planyo-cache-purge. After Planyo admin changes: bump client
cache keys, clear localStorage, restart serve, or POST/GET the purge URL.
"""

from __future__ import annotations

import hashlib
import io
import json
import os
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:  # pragma: no cover - optional until pip install
    Image = None  # type: ignore[assignment]
    ImageOps = None  # type: ignore[assignment]

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8765"))
UPSTREAM = "https://www.planyo.com/rest/"
ALLOWED_METHODS = {
    "resource_search",
    "list_resources",
    "get_event_times",
    "get_resource_info",
    "api_test",
}
CACHEABLE_METHODS = {
    "resource_search",
    "list_resources",
    "get_event_times",
    "get_resource_info",
}
# Experiences/calendar change rarely — default 12 hours (set PROXY_CACHE_TTL_SEC to override).
PROXY_CACHE_TTL_SEC = int(os.environ.get("PROXY_CACHE_TTL_SEC", str(12 * 60 * 60)))
PROXY_CACHE_MAX_ENTRIES = int(os.environ.get("PROXY_CACHE_MAX_ENTRIES", "256"))

ALLOWED_IMG_HOSTS = {
    "planyo-ch.s3.eu-central-2.amazonaws.com",
    "planyo.com",
    "www.planyo.com",
}
IMG_MAX_UPSTREAM_BYTES = int(os.environ.get("IMG_MAX_UPSTREAM_BYTES", str(12 * 1024 * 1024)))
IMG_DEFAULT_WIDTH = 640
IMG_MAX_WIDTH = 1200
IMG_DEFAULT_QUALITY = 72
IMG_CACHE_DIR = Path(os.environ.get("IMG_CACHE_DIR", ".cache/img"))
IMG_CACHE_CONTROL = "public, max-age=604800, stale-while-revalidate=86400"

_cache_lock = threading.Lock()
_cache: dict[str, tuple[float, bytes]] = {}
_img_lock = threading.Lock()


def _cache_key(flat: dict[str, str]) -> str:
    parts = {k: v for k, v in flat.items() if k != "api_key"}
    return urllib.parse.urlencode(sorted(parts.items()))


def _cache_get(key: str) -> bytes | None:
    if PROXY_CACHE_TTL_SEC <= 0:
        return None
    now = time.time()
    with _cache_lock:
        entry = _cache.get(key)
        if not entry:
            return None
        ts, body = entry
        if now - ts > PROXY_CACHE_TTL_SEC:
            del _cache[key]
            return None
        return body


def _cache_set(key: str, body: bytes) -> None:
    if PROXY_CACHE_TTL_SEC <= 0:
        return
    now = time.time()
    with _cache_lock:
        if len(_cache) >= PROXY_CACHE_MAX_ENTRIES:
            # Drop expired + oldest entries
            expired = [k for k, (ts, _) in _cache.items() if now - ts > PROXY_CACHE_TTL_SEC]
            for k in expired:
                del _cache[k]
            if len(_cache) >= PROXY_CACHE_MAX_ENTRIES:
                oldest = sorted(_cache.items(), key=lambda kv: kv[1][0])[
                    : max(1, PROXY_CACHE_MAX_ENTRIES // 4)
                ]
                for k, _ in oldest:
                    del _cache[k]
        _cache[key] = (now, body)


def _cache_purge() -> int:
    with _cache_lock:
        n = len(_cache)
        _cache.clear()
        return n


def _parse_int(raw: str | None, default: int, lo: int, hi: int) -> int:
    try:
        n = int(raw) if raw is not None and str(raw).strip() != "" else default
    except (TypeError, ValueError):
        n = default
    return max(lo, min(hi, n))


def _img_cache_path(url: str, width: int, quality: int, fmt: str) -> Path:
    digest = hashlib.sha256(f"{url}|{width}|{quality}|{fmt}".encode("utf-8")).hexdigest()[:40]
    return IMG_CACHE_DIR / f"{digest}.{fmt}"


def _fetch_upstream_image(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "image/*,*/*;q=0.8",
            "User-Agent": "macugnaga-booking-img/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        # Bound download size without relying on Content-Length.
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = resp.read(64 * 1024)
            if not chunk:
                break
            total += len(chunk)
            if total > IMG_MAX_UPSTREAM_BYTES:
                raise ValueError("Upstream image too large")
            chunks.append(chunk)
        return b"".join(chunks)


def _encode_card_image(raw: bytes, width: int, quality: int, prefer_webp: bool) -> tuple[bytes, str]:
    if Image is None or ImageOps is None:
        raise RuntimeError("Pillow not installed")
    with Image.open(io.BytesIO(raw)) as im:
        im = ImageOps.exif_transpose(im)
        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")
        elif im.mode == "L":
            im = im.convert("RGB")
        w, h = im.size
        if w > width and w > 0:
            new_h = max(1, round(h * (width / float(w))))
            im = im.resize((width, new_h), Image.Resampling.LANCZOS)

        if prefer_webp:
            buf = io.BytesIO()
            im.save(buf, format="WEBP", quality=quality, method=4)
            return buf.getvalue(), "image/webp"

        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=quality, optimize=True, progressive=True)
        return buf.getvalue(), "image/jpeg"


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ("/api/planyo-cache-purge", "/api/planyo-cache-purge/"):
            cleared = _cache_purge()
            self.send_json(200, {"ok": True, "cleared": cleared})
            return
        if parsed.path in ("/api/planyo", "/api/planyo-proxy.php"):
            self.proxy_planyo(parsed.query)
            return
        if parsed.path in ("/api/img", "/api/img/"):
            self.proxy_image(parsed.query)
            return
        super().do_GET()

    def proxy_image(self, query: str) -> None:
        params = urllib.parse.parse_qs(query, keep_blank_values=True)
        raw_url = (params.get("u") or params.get("url") or [""])[-1].strip()
        if not raw_url:
            self.send_json(400, {"ok": False, "error": "Missing u"})
            return

        try:
            parsed = urllib.parse.urlparse(raw_url)
        except Exception:
            self.send_json(400, {"ok": False, "error": "Invalid url"})
            return

        if parsed.scheme != "https" or not parsed.netloc:
            self.send_json(400, {"ok": False, "error": "Only https URLs allowed"})
            return
        host = parsed.netloc.lower().split("@")[-1]
        if host not in ALLOWED_IMG_HOSTS:
            self.send_json(403, {"ok": False, "error": "Host not allowed"})
            return

        width = _parse_int(
            (params.get("w") or [""])[-1],
            IMG_DEFAULT_WIDTH,
            120,
            IMG_MAX_WIDTH,
        )
        quality = _parse_int(
            (params.get("q") or [""])[-1],
            IMG_DEFAULT_QUALITY,
            40,
            90,
        )
        accept = (self.headers.get("Accept") or "").lower()
        fmt_param = ((params.get("f") or params.get("format") or [""])[-1] or "").lower()
        prefer_webp = fmt_param in ("", "auto", "webp") and (
            "image/webp" in accept or fmt_param == "webp" or fmt_param in ("", "auto")
        )
        # Default to webp when client does not send Accept (e.g. <img src>).
        if fmt_param in ("", "auto") and "image/" not in accept:
            prefer_webp = True
        if fmt_param == "jpeg" or fmt_param == "jpg":
            prefer_webp = False

        if Image is None:
            # Soft-degrade: redirect to original so cards still render.
            self.send_response(302)
            self.send_header("Location", raw_url)
            self.send_header("Cache-Control", "private, max-age=60")
            self.end_headers()
            return

        fmt = "webp" if prefer_webp else "jpg"
        cache_path = _img_cache_path(raw_url, width, quality, fmt)
        try:
            if cache_path.is_file() and cache_path.stat().st_size > 0:
                body = cache_path.read_bytes()
                self._send_image(body, "image/webp" if fmt == "webp" else "image/jpeg", "HIT")
                return
        except OSError:
            pass

        with _img_lock:
            try:
                if cache_path.is_file() and cache_path.stat().st_size > 0:
                    body = cache_path.read_bytes()
                    self._send_image(
                        body, "image/webp" if fmt == "webp" else "image/jpeg", "HIT"
                    )
                    return
            except OSError:
                pass

            try:
                upstream = _fetch_upstream_image(raw_url)
                body, content_type = _encode_card_image(
                    upstream, width, quality, prefer_webp
                )
                try:
                    IMG_CACHE_DIR.mkdir(parents=True, exist_ok=True)
                    tmp = cache_path.with_suffix(cache_path.suffix + ".tmp")
                    tmp.write_bytes(body)
                    tmp.replace(cache_path)
                except OSError:
                    pass
                self._send_image(body, content_type, "MISS")
            except urllib.error.HTTPError as exc:
                self.send_json(
                    502,
                    {
                        "ok": False,
                        "error": "Upstream HTTP error",
                        "status": int(exc.code),
                    },
                )
            except Exception:
                self.send_json(502, {"ok": False, "error": "Image proxy failed"})

    def _send_image(self, body: bytes, content_type: str, cache_state: str) -> None:
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", IMG_CACHE_CONTROL)
        self.send_header("X-Image-Cache", cache_state)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError):
            return

    def proxy_planyo(self, query: str) -> None:
        params = urllib.parse.parse_qs(query, keep_blank_values=True)
        flat = {k: v[-1] if v else "" for k, v in params.items()}
        method = flat.get("method", "")
        if method not in ALLOWED_METHODS:
            self.send_json(400, {"response_code": 3, "response_message": "Method not allowed via proxy"})
            return
        env_key = (os.environ.get("PLANYO_API_KEY") or "").strip()
        if env_key and not (flat.get("api_key") or "").strip():
            flat["api_key"] = env_key
        if not (flat.get("api_key") or "").strip():
            self.send_json(
                500,
                {
                    "response_code": 6,
                    "response_message": "PLANYO_API_KEY not configured on server",
                },
            )
            return

        use_cache = method in CACHEABLE_METHODS
        ckey = _cache_key(flat) if use_cache else ""
        if use_cache:
            cached = _cache_get(ckey)
            if cached is not None:
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=UTF-8")
                # no-store: avoid browser HTTP cache of stale empty event times
                self.send_header("Cache-Control", "private, no-store")
                self.send_header("X-Proxy-Cache", "HIT")
                self.send_header("Content-Length", str(len(cached)))
                self.end_headers()
                try:
                    self.wfile.write(cached)
                except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError):
                    return
                return

        url = UPSTREAM + "?" + urllib.parse.urlencode(flat)
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "Accept": "application/json",
                    "User-Agent": "macugnaga-booking-proxy/1.0",
                },
            )
            with urllib.request.urlopen(req, timeout=25) as resp:
                body = resp.read()
                if use_cache:
                    _cache_set(ckey, body)
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=UTF-8")
                self.send_header("Cache-Control", "private, no-store")
                self.send_header("X-Proxy-Cache", "MISS")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                try:
                    self.wfile.write(body)
                except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError):
                    return
        except urllib.error.HTTPError as exc:
            body = exc.read() if exc.fp else b'{"response_code":6,"response_message":"Upstream HTTP error"}'
            try:
                self.send_response(502)
                self.send_header("Content-Type", "application/json; charset=UTF-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError):
                return
        except Exception:
            try:
                self.send_json(502, {"response_code": 6, "response_message": "Upstream request failed"})
            except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError):
                return

    def send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=UTF-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args) -> None:
        if args and str(args[0]).startswith("/api/"):
            super().log_message(fmt, *args)


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    img = "on" if Image is not None else "off (pip install Pillow)"
    print(
        f"Serving on http://{HOST}:{PORT}/  (API proxy: /api/planyo, "
        f"/api/img={img}, cache TTL={PROXY_CACHE_TTL_SEC}s)"
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
