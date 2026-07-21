/**
 * Copy this file to js/planyo-config.js for local browser key (optional).
 * planyo-config.js is gitignored — do not commit the real key.
 *
 * Preferred for production: leave PLANYO_API_KEY empty here and set the
 * PLANYO_API_KEY environment variable on the host (Render). serve.py injects it.
 *
 * Get the key from the booking admin panel (API settings).
 * Restrict the key to methods: list_resources, resource_search, get_event_times
 * (and optionally limit by IP) for safer use.
 *
 * Browser calls to the REST API are usually CORS-blocked. Use the same-origin
 * proxy: run `python serve.py` (local/Render) or deploy api/planyo-proxy.php (PHP).
 */
window.PLANYO_API_KEY = "";
window.PLANYO_SITE_ID = 70864;
/**
 * Same-origin proxy (REST is CORS-blocked in browsers):
 * - Local / Render: python serve.py  →  "/api/planyo"
 * - PHP hosting: "api/planyo-proxy.php"
 */
window.PLANYO_API_ENDPOINT = "/api/planyo";