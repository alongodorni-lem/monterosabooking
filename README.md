# Macugnaga / Monte Rosa booking minisite

Static HTML minisite for booking experiences in Macugnaga, with a small Python server that serves files and proxies Planyo REST (`/api/planyo`) so the availability ticker works without browser CORS issues.

## Local run

1. Copy `js/planyo-config.example.js` → `js/planyo-config.js` and set `PLANYO_API_KEY`, **or** export `PLANYO_API_KEY` in the environment (preferred for production-like local runs).
2. Start the server:

```bash
python serve.py
```

3. Open http://127.0.0.1:8765/

Default port is `8765`. Override with `PORT` / `HOST` env vars.

**API cache:** `serve.py` caches safe Planyo reads for **12 hours** by default (`PROXY_CACHE_TTL_SEC`). Browser list/ticker use **localStorage** with the same 12h hard TTL. After admin changes to activities/calendar: bump the `CACHE_KEY` in `js/esperienze-list.js` / `js/availability-bar.js`, clear those `localStorage` keys, restart `serve.py` (or hit `/api/planyo-cache-purge`), or lower `PROXY_CACHE_TTL_SEC`.

## Secrets

Never commit:

- `js/planyo-config.js`
- `assets/API PLANYO.txt`
- `api/planyo-secrets.php`

Use `js/planyo-config.example.js` as the template. On Render, set the **`PLANYO_API_KEY`** environment variable; `serve.py` injects it into proxied API calls when the client key is empty.

## Deploy (Render Web Service)

This project needs the `/api/planyo` proxy, so deploy as a **Web Service** (not a Static Site).

Blueprint: `render.yaml` (service name **macugnagabooking**).

1. Connect this GitHub repo in the Render dashboard (or `render blueprint launch`).
2. Set env var **`PLANYO_API_KEY`** to your Planyo API key.
3. Start command: `python serve.py` (binds `0.0.0.0:$PORT`).

Expected URL: https://macugnagabooking.onrender.com

**Renaming an existing service (subdomain):** Render matches Blueprint services by `name`. Change the live service name *before* (or together with) applying a Blueprint that uses the new name — otherwise Render may create a second service. Prefer Dashboard → service **Settings → Name** → `macugnagabooking`, or `render services update monterosabooking --name macugnagabooking`. Do not delete the service. Env vars (`PLANYO_API_KEY`), plan, and custom domains stay on the same service. After rename, the old `monterosabooking.onrender.com` hostname is usually freed and stops working.

## What’s published

HTML pages, `css/`, `js/` (example config only), `serve.py`, `api/planyo-proxy.php` (optional PHP hosting), `assets/web/` optimized images, `assets/stemma.png`, `assets/CAPOLAV-ORO1.mp4`.

Large original photos under `assets/` (outside `web/`) are gitignored and not deployed.