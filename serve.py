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

Open Graph for /prenota.html?resource_id=… (and /en|/fr|/de variants):
server-side rewrite of og:/twitter: meta so Facebook/WhatsApp/LinkedIn
crawlers see the resource photo/title without running client JS.

Long-lived in-memory cache (PROXY_CACHE_TTL_SEC, default 24h) for safe
read methods: list_resources / get_event_times / get_resource_info /
resource_search. api_test is never cached. Cache key = method + sorted
query params (api_key excluded). Cleared on process restart, or via
GET /api/planyo-cache-purge. After Planyo admin changes: bump client
cache keys, clear localStorage, restart serve, or POST/GET the purge URL.

Static assets (css/js/images/fonts) get Cache-Control via end_headers;
HTML stays short-lived. /api/img responses use IMG_CACHE_CONTROL (30d).
"""

from __future__ import annotations

import hashlib
import html as html_lib
import io
import json
import os
import re
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
# Experiences/calendar change rarely — default 24 hours (set PROXY_CACHE_TTL_SEC to override).
PROXY_CACHE_TTL_SEC = int(os.environ.get("PROXY_CACHE_TTL_SEC", str(24 * 60 * 60)))
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
# Proxied card thumbs: 30 days (+ SWR). Bump client ?v= / cache keys when needed.
IMG_CACHE_CONTROL = "public, max-age=2592000, stale-while-revalidate=86400"

STATIC_LONG_CACHE_EXTS = {
    ".css",
    ".js",
    ".mjs",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".svg",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".otf",
    ".map",
    ".pdf",
}
STATIC_ASSET_CACHE_CONTROL = "public, max-age=604800, stale-while-revalidate=86400"
HTML_CACHE_CONTROL = "public, max-age=300, must-revalidate"
# Resource share pages: short public cache (URL is unique per resource_id).
PRENOTA_OG_CACHE_CONTROL = "public, max-age=300, must-revalidate"

PUBLIC_ORIGIN = (
    os.environ.get("PUBLIC_ORIGIN") or "https://www.macugnagabooking.it"
).rstrip("/")
PLANYO_SITE_ID = (os.environ.get("PLANYO_SITE_ID") or "70864").strip()
DEFAULT_OG_IMAGE = f"{PUBLIC_ORIGIN}/assets/web/macugnaga-booking-social-16x9.jpg"
PRENOTA_PATHS = {
    "/prenota.html",
    "/en/prenota.html",
    "/fr/prenota.html",
    "/de/prenota.html",
}
DESC_MAX_CHARS = 220

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


def _as_list(results) -> list:
    if not results:
        return []
    if isinstance(results, list):
        return results
    if isinstance(results, dict):
        return list(results.values())
    return []


def _strip_html(raw: str) -> str:
    s = re.sub(r"<script[\s\S]*?</script>", " ", raw or "", flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html_lib.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def _truncate(text: str, max_chars: int = DESC_MAX_CHARS) -> str:
    t = (text or "").strip()
    if len(t) <= max_chars:
        return t
    cut = t[: max_chars - 1].rsplit(" ", 1)[0]
    return (cut or t[: max_chars - 1]).rstrip(".,;:") + "…"


def _absolute_media_url(raw: str) -> str:
    u = (raw or "").strip()
    if not u or u in ("null", "undefined"):
        return ""
    if u.startswith("//"):
        u = "https:" + u
    if re.match(r"^https?://", u, re.I):
        return re.sub(r"^http://", "https://", u, flags=re.I)
    if u.startswith("/"):
        return "https://www.planyo.com" + u
    if re.match(r"^\d+_", u) or re.search(r"\.(jpe?g|png|webp|gif)(\?|$)", u, re.I):
        if "/" not in u:
            return "https://planyo-ch.s3.eu-central-2.amazonaws.com/" + u
        return "https://www.planyo.com/" + u.lstrip("./")
    return ""


def _first_photo_url(resource: dict) -> str:
    for entry in _as_list(resource.get("photos")):
        if isinstance(entry, str):
            url = _absolute_media_url(entry)
        elif isinstance(entry, dict):
            url = _absolute_media_url(
                str(
                    entry.get("path")
                    or entry.get("url")
                    or entry.get("src")
                    or entry.get("image")
                    or entry.get("photo")
                    or entry.get("filename")
                    or ""
                )
            )
        else:
            url = ""
        if url:
            return url
    props = resource.get("properties") or {}
    if isinstance(props, dict):
        url = _absolute_media_url(
            str(
                props.get("image")
                or props.get("Image")
                or props.get("photo")
                or props.get("Photo")
                or props.get("picture")
                or props.get("main_image")
                or ""
            )
        )
        if url:
            return url
    return ""


def _resource_description(resource: dict) -> str:
    for key in (
        "translated_description",
        "description",
        "short_description",
        "translated_short_description",
    ):
        raw = resource.get(key)
        if raw:
            return _truncate(_strip_html(str(raw)))
    props = resource.get("properties") or {}
    if isinstance(props, dict):
        for key in (
            "description",
            "Description",
            "Descrizione",
            "short_description",
            "desc",
        ):
            raw = props.get(key)
            if raw:
                return _truncate(_strip_html(str(raw)))
    return ""


def _prenota_lang(path: str, query_lang: str) -> str:
    ql = (query_lang or "").strip().upper()
    if ql in ("IT", "EN", "FR", "DE"):
        return ql
    if path.startswith("/en/"):
        return "EN"
    if path.startswith("/fr/"):
        return "FR"
    if path.startswith("/de/"):
        return "DE"
    return "IT"


def _planyo_api_key() -> str:
    return (os.environ.get("PLANYO_API_KEY") or "").strip()


def _planyo_fetch(flat: dict[str, str]) -> dict | None:
    """Call Planyo REST; reuse PROXY cache for cacheable methods. Never log api_key."""
    method = flat.get("method", "")
    if method not in ALLOWED_METHODS:
        return None
    params = dict(flat)
    env_key = _planyo_api_key()
    if env_key and not (params.get("api_key") or "").strip():
        params["api_key"] = env_key
    if not (params.get("api_key") or "").strip():
        return None

    use_cache = method in CACHEABLE_METHODS
    ckey = _cache_key(params) if use_cache else ""
    if use_cache:
        cached = _cache_get(ckey)
        if cached is not None:
            try:
                return json.loads(cached.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                pass

    url = UPSTREAM + "?" + urllib.parse.urlencode(params)
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
            return json.loads(body.decode("utf-8"))
    except Exception:
        return None


def _fetch_resource_og(resource_id: str, language: str) -> dict[str, str] | None:
    if not re.fullmatch(r"\d{1,12}", resource_id or ""):
        return None
    payload = _planyo_fetch(
        {
            "method": "get_resource_info",
            "resource_id": resource_id,
            "language": language,
            "site_id": PLANYO_SITE_ID,
        }
    )
    if not payload:
        return None
    try:
        code = int(payload.get("response_code"))
    except (TypeError, ValueError):
        code = -1
    if code != 0:
        return None
    data = payload.get("data") or {}
    if not isinstance(data, dict):
        return None
    name = str(data.get("translated_name") or data.get("name") or "").strip()
    if not name:
        return None
    image = _first_photo_url(data) or DEFAULT_OG_IMAGE
    desc = _resource_description(data)
    if not desc:
        desc = f"{name} — Macugnaga Booking"
    return {"name": name, "description": desc, "image": image}


def _upsert_meta_property(html: str, prop: str, content: str) -> str:
    esc = html_lib.escape(content, quote=True)
    pat = re.compile(
        rf'<meta\s+property=["\']{re.escape(prop)}["\']\s+content=["\'][^"\']*["\']\s*/?>',
        re.I,
    )
    tag = f'<meta property="{prop}" content="{esc}">'
    if pat.search(html):
        return pat.sub(tag, html, count=1)
    return re.sub(r"(</head>)", f"  {tag}\n\\1", html, count=1, flags=re.I)


def _upsert_meta_name(html: str, name: str, content: str) -> str:
    esc = html_lib.escape(content, quote=True)
    pat = re.compile(
        rf'<meta\s+name=["\']{re.escape(name)}["\']\s+content=["\'][^"\']*["\']\s*/?>',
        re.I,
    )
    tag = f'<meta name="{name}" content="{esc}">'
    if pat.search(html):
        return pat.sub(tag, html, count=1)
    return re.sub(r"(</head>)", f"  {tag}\n\\1", html, count=1, flags=re.I)


def _set_title(html: str, title: str) -> str:
    esc = html_lib.escape(title, quote=False)
    if re.search(r"<title>[^<]*</title>", html, flags=re.I):
        return re.sub(r"<title>[^<]*</title>", f"<title>{esc}</title>", html, count=1, flags=re.I)
    return re.sub(r"(</head>)", f"  <title>{esc}</title>\n\\1", html, count=1, flags=re.I)


def _inject_resource_og(
    html: str,
    *,
    title: str,
    description: str,
    image: str,
    page_url: str,
) -> str:
    html = _set_title(html, title)
    html = _upsert_meta_name(html, "description", description)
    html = _upsert_meta_property(html, "og:title", title)
    html = _upsert_meta_property(html, "og:description", description)
    html = _upsert_meta_property(html, "og:image", image)
    html = _upsert_meta_property(html, "og:image:secure_url", image)
    html = _upsert_meta_property(html, "og:url", page_url)
    html = _upsert_meta_property(html, "og:type", "website")
    html = _upsert_meta_name(html, "twitter:card", "summary_large_image")
    html = _upsert_meta_name(html, "twitter:title", title)
    html = _upsert_meta_name(html, "twitter:description", description)
    html = _upsert_meta_name(html, "twitter:image", image)
    return html


def _parse_int(raw: str | None, default: int, lo: int, hi: int) -> int:
    try:
        n = int(raw) if raw is not None and str(raw).strip() != "" else default
    except (TypeError, ValueError):
        n = default
    return max(lo, min(hi, n))


def _img_cache_path(
    url: str, width: int, quality: int, fmt: str, bust: str = ""
) -> Path:
    # Include optional client bust token so in-place Planyo photo replaces invalidate disk cache.
    digest = hashlib.sha256(
        f"{url}|{width}|{quality}|{fmt}|{bust}".encode("utf-8")
    ).hexdigest()[:40]
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
    def end_headers(self) -> None:  # noqa: D401
        """Attach Cache-Control for static files (not /api/*)."""
        parsed = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(parsed.path or "/")
        if not path.startswith("/api/"):
            ext = Path(path).suffix.lower()
            if ext in STATIC_LONG_CACHE_EXTS:
                self.send_header("Cache-Control", STATIC_ASSET_CACHE_CONTROL)
            elif ext in (".html", ".htm") or path.endswith("/") or ext == "":
                self.send_header("Cache-Control", HTML_CACHE_CONTROL)
        super().end_headers()

    def do_GET(self):  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(parsed.path or "/")
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
        if path in PRENOTA_PATHS:
            qs = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
            resource_id = (qs.get("resource_id") or [""])[-1].strip()
            if resource_id:
                self.serve_prenota_with_og(path, parsed.query, resource_id)
                return
        super().do_GET()

    def serve_prenota_with_og(self, path: str, query: str, resource_id: str) -> None:
        """Serve prenota.html with resource-specific OG/Twitter meta (SSR)."""
        file_path = Path(self.translate_path(path))
        try:
            html = file_path.read_text(encoding="utf-8")
        except OSError:
            self.send_error(404, "File not found")
            return

        qs = urllib.parse.parse_qs(query, keep_blank_values=True)
        lang = _prenota_lang(
            path, (qs.get("planyo_lang") or qs.get("lang") or [""])[-1]
        )
        meta = _fetch_resource_og(resource_id, lang)
        if meta:
            title = f"{meta['name']} | Macugnaga Booking"
            page_url = f"{PUBLIC_ORIGIN}{path}"
            if query:
                page_url = f"{page_url}?{query}"
            html = _inject_resource_og(
                html,
                title=title,
                description=meta["description"],
                image=meta["image"],
                page_url=page_url,
            )

        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", PRENOTA_OG_CACHE_CONTROL)
        self.send_header("Content-Length", str(len(body)))
        # Avoid duplicate Cache-Control from end_headers for this synthetic response.
        self.path = "/api/prenota-og"
        try:
            self.end_headers()
            self.wfile.write(body)
        except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError):
            return

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

        bust = ((params.get("cb") or params.get("v") or [""])[-1] or "").strip()

        if Image is None:
            # Soft-degrade: redirect to original so cards still render.
            self.send_response(302)
            self.send_header("Location", raw_url)
            self.send_header("Cache-Control", "private, max-age=60")
            self.end_headers()
            return

        fmt = "webp" if prefer_webp else "jpg"
        cache_path = _img_cache_path(raw_url, width, quality, fmt, bust)
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
    key = "set" if _planyo_api_key() else "missing"
    print(
        f"Serving on http://{HOST}:{PORT}/  (API proxy: /api/planyo, "
        f"/api/img={img}, OG prenota=on, PLANYO_API_KEY={key}, "
        f"cache TTL={PROXY_CACHE_TTL_SEC}s)"
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
