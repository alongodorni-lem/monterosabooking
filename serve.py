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
"""

from __future__ import annotations

import json
import os
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
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=UTF-8")
                self.send_header("Cache-Control", "private, max-age=0")
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
    print(f"Serving on http://{HOST}:{PORT}/  (API proxy: /api/planyo)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()