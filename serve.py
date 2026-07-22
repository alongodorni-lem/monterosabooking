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

Short in-memory cache (PROXY_CACHE_TTL_SEC, default 90s) for repeated
list_resources / get_event_times / resource_search GETs.
"""

from __future__ import annotations

import json
import os
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

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
PROXY_CACHE_TTL_SEC = int(os.environ.get("PROXY_CACHE_TTL_SEC", "90"))
PROXY_CACHE_MAX_ENTRIES = int(os.environ.get("PROXY_CACHE_MAX_ENTRIES", "256"))

_cache_lock = threading.Lock()
_cache: dict[str, tuple[float, bytes]] = {}


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


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ("/api/planyo", "/api/planyo-proxy.php"):
            self.proxy_planyo(parsed.query)
            return
        super().do_GET()

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
                self.send_header(
                    "Cache-Control",
                    f"private, max-age={max(0, PROXY_CACHE_TTL_SEC)}",
                )
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
                self.send_header(
                    "Cache-Control",
                    f"private, max-age={max(0, PROXY_CACHE_TTL_SEC) if use_cache else 0}",
                )
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
    print(
        f"Serving on http://{HOST}:{PORT}/  (API proxy: /api/planyo, "
        f"cache TTL={PROXY_CACHE_TTL_SEC}s)"
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
