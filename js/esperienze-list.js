/* Custom experiences list: sorted by next available day via /api/planyo */
(function () {
  "use strict";

  var SITE_ID = 70864;
  /* Hard TTL in localStorage. Force refresh after Planyo admin changes: bump
     CACHE_KEY (e.g. v14), or clear localStorage key mem_esperienze_list_*. */
  var CACHE_KEY_BASE = "mem_esperienze_list_v28";
  /* Bust /api/img + browser cache when Planyo replaces a photo at the same URL. */
  var PHOTO_CACHE_BUST = "21";
  var CACHE_MS = 24 * 60 * 60 * 1000;
  var EVENT_TIMES_CONCURRENCY = 6;
  var MAX_DATE_LABELS = 5;
  var DESC_MAX = 220;
  var CARD_IMG_WIDTH = 640;
  var CARD_IMG_HEIGHT = 360; /* 16:9 — matches .esperienze-card__media */
  /* No eager card photos — LCP is the page hero; hydrate after text paint. */
  var EAGER_PHOTO_COUNT = 0;
  var REST_URL = "https://www.planyo.com/rest/";
  /* Daily lifts pinned first (seggiovia Belvedere, then funivia Alpe Bill). */
  var PINNED_RESOURCE_IDS = ["253658", "253679"];
  var CONCLUDED_ORDER = [
    "252703" /* Capolav-ORO */,
    "253656" /* Alpigiano per un giorno */,
    "253657" /* Trekking a Villa Aprilia */,
    "254067" /* Camminata dei Lanternit */,
    "252702" /* Macugnaga nel ’900 */,
    "252698" /* Pane, camino e folletti */,
  ];
  var CONCLUDED_RESOURCE_IDS = {};
  CONCLUDED_ORDER.forEach(function (id) {
    CONCLUDED_RESOURCE_IDS[id] = true;
  });
  var CONTACT_MAIL = "macugnagabooking@gmail.com";
  var COMING_SOON_IDS = {
    "252699": true /* Trekking del Benessere */,
    "253421": true /* La via del pane */,
  };
  var ON_REQUEST_IDS = {
    "253477": true /* Passeggiata con guida walser */,
  };
  var ON_REQUEST_PHONE = "349 8515207";
  var ON_REQUEST_TEL = "+393498515207";
  var SPECIAL_RESOURCE_IDS = {
    "253398": true /* Casa Museo Walser */,
    "252705": true /* Miniera d'Oro della Guia */,
    "253658": true /* Seggiovia Pecetto–Burki–Belvedere */,
    "253679": true /* Funivie Macugnaga Staffa–Alpe Bill */,
  };
  /* Booking deadline notice under available dates (id → i18n key). */
  var DEADLINE_NOTICES = {
    "253421": {
      key: "viaDelPaneDeadline",
      fallback: "Prenotazioni entro il 17 agosto",
    },
    "253656": {
      key: "alpigianoDeadline",
      fallback: "Prenotazione obbligatoria entro il 23 agosto",
    },
  };
  /* Local fallbacks only when Planyo HTTPS photo fails (onerror). Prefer API. */
  var PHOTO_FALLBACKS = {
    "252382": "assets/web/forest-bathing.jpg",
    "253390": "assets/web/forest-bathing.jpg",
    "252705": "assets/web/miniera-hero.jpg",
    "253398": "assets/web/casa-museo-hero.jpg",
    "252697": "assets/web/folletti-museo.jpg",
    "252699": "assets/web/trekking-salute.jpg",
    "253399": "assets/web/ricerca-oro.jpg",
    "253421": "assets/web/casa-museo-pane.jpg",
    "253658": "assets/web/funivia-belvedere.jpg",
    "253679": "assets/web/funivia-alpe-bill.jpg",
    "254066": "assets/web/favole-walser-quota.jpg",
    "254067": "assets/web/camminata-lanternit.jpg",
  };

  function siteLang() {
    return window.MB_I18N ? window.MB_I18N.detectLang() : "it";
  }

  function planyoLangCode() {
    return window.MB_I18N ? window.MB_I18N.planyoLang(siteLang()) : "IT";
  }

  function assetPrefix() {
    return window.MB_I18N ? window.MB_I18N.assetPrefix(siteLang()) : "";
  }

  function ui() {
    return window.MB_I18N ? window.MB_I18N.t(siteLang()) : {};
  }

  /* Optional date window via #esperienze-list data-date-from/to or MB_ESPERIENZE_RANGE.
     data-date-from="today" (or empty when data-date-to is set) resolves to Europe/Rome today. */
  function resolveRangeBound(token, allowTodayFallback) {
    var raw = String(token || "").trim();
    var lower = raw.toLowerCase();
    if (!raw || lower === "today") {
      return allowTodayFallback ? romeYmd(0) : "";
    }
    if (/^\d{4}-\d{2}-\d{2}$/.test(raw)) return raw;
    return "";
  }

  function getDateRange() {
    var from = "";
    var to = "";
    var cfg = window.MB_ESPERIENZE_RANGE;
    if (cfg && typeof cfg === "object") {
      from = String(cfg.from || cfg.start || "").trim();
      to = String(cfg.to || cfg.end || "").trim();
    }
    var el = mountEl();
    if (el) {
      if (!from) from = String(el.getAttribute("data-date-from") || "").trim();
      if (!to) to = String(el.getAttribute("data-date-to") || "").trim();
    }
    to = resolveRangeBound(to, false);
    /* Dynamic start: "today", or missing from when an end date is set. */
    from = resolveRangeBound(from, !!to);
    if (
      /^\d{4}-\d{2}-\d{2}$/.test(from) &&
      /^\d{4}-\d{2}-\d{2}$/.test(to) &&
      from <= to
    ) {
      return { from: from, to: to };
    }
    return null;
  }

  function formatDayMonth(ymd) {
    var d = new Date(ymd + "T12:00:00");
    return d.toLocaleDateString(localeForDates(), {
      day: "numeric",
      month: "long",
    });
  }

  function rangeSpecialLabel(range) {
    var L = ui();
    var fromLbl = formatDayMonth(range.from);
    var toLbl = formatDayMonth(range.to);
    if (L.rangeFromTo) {
      return String(L.rangeFromTo)
        .replace(/\{from\}/g, fromLbl)
        .replace(/\{to\}/g, toLbl);
    }
    return "Available from " + fromLbl + " to " + toLbl;
  }

  function filterDaysByRange(days, range, todayYmd) {
    if (!days || !days.length) return [];
    var lower = todayYmd || romeYmd(0);
    var upper = null;
    if (range) {
      if (range.from > lower) lower = range.from;
      upper = range.to;
    }
    return days.filter(function (ymd) {
      if (ymd < lower) return false;
      if (upper && ymd > upper) return false;
      return true;
    });
  }

  function cacheKey() {
    var key = CACHE_KEY_BASE + "_" + siteLang();
    var range = getDateRange();
    if (range) key += "_" + range.from + "_" + range.to;
    if (showConcludedBox()) key += "_conc";
    return key;
  }

  function showConcludedBox() {
    var el = mountEl();
    return !!(el && el.getAttribute("data-show-concluded") === "true");
  }

  function isConcludedResource(resourceId) {
    return !!CONCLUDED_RESOURCE_IDS[String(resourceId || "")];
  }

  function isComingSoonResource(resourceId) {
    return !!COMING_SOON_IDS[String(resourceId || "")];
  }

  function isOnRequestResource(resourceId) {
    return !!ON_REQUEST_IDS[String(resourceId || "")];
  }

  function markOnRequest(item) {
    var L = ui();
    if (!item) return item;
    item.onRequest = true;
    item.upcoming = false;
    item.datesPending = false;
    item.specialAugust = false;
    item.comingSoon = false;
    item.sortKey = "9999-12-29";
    item.dateLabels = [];
    item.onRequestText =
      L.guidaWalserOnRequest ||
      "Su prenotazione al {phone} nel fine settimana con minimo 3 persone.";
    return item;
  }

  function onRequestNoticeHtml(item) {
    if (!item || !item.onRequest) return "";
    var raw =
      item.onRequestText ||
      "Su prenotazione al {phone} nel fine settimana con minimo 3 persone.";
    var phoneLink =
      '<a href="tel:' +
      ON_REQUEST_TEL +
      '">' +
      escapeHtml(ON_REQUEST_PHONE) +
      "</a>";
    var html =
      raw.indexOf("{phone}") >= 0
        ? raw.split("{phone}").map(escapeHtml).join(phoneLink)
        : escapeHtml(raw);
    return '<p class="esperienze-card__on-request">' + html + "</p>";
  }

  function markComingSoon(item) {
    var L = ui();
    if (!item) return item;
    item.comingSoon = true;
    item.upcoming = false;
    item.datesPending = false;
    item.specialAugust = false;
    item.sortKey = "9999-12-31";
    item.dateLabels = [L.soon || "Prossimamente"];
    return item;
  }

  function concludedRank(resourceId) {
    var idx = CONCLUDED_ORDER.indexOf(String(resourceId || ""));
    return idx === -1 ? 999 : idx;
  }

  function markConcluded(item) {
    var L = ui();
    if (!item) return item;
    item.concluded = true;
    item.upcoming = false;
    item.datesPending = false;
    item.specialAugust = false;
    item.dateLabels = [L.concludedSeason || "Stagione conclusa"];
    return item;
  }

  function sortConcluded(items) {
    return items.slice().sort(function (a, b) {
      var ra = concludedRank(a.resourceId);
      var rb = concludedRank(b.resourceId);
      if (ra !== rb) return ra - rb;
      return String(a.name).localeCompare(String(b.name), localeForDates());
    });
  }

  function localeForDates() {
    var map = { it: "it-IT", en: "en-GB", fr: "fr-FR", de: "de-DE" };
    return map[siteLang()] || "it-IT";
  }

  function photoFallback(id) {
    var rel = PHOTO_FALLBACKS[String(id)];
    return rel ? assetPrefix() + rel : "";
  }

  function getApiKey() {
    var key = window.PLANYO_API_KEY || window.planyoApiKey || "";
    return typeof key === "string" ? key.trim() : "";
  }

  function getSiteId() {
    var id = window.PLANYO_SITE_ID || window.planyoSiteId || SITE_ID;
    return String(id || SITE_ID);
  }

  function getEndpointCandidates() {
    var configured =
      typeof window.PLANYO_API_ENDPOINT === "string"
        ? window.PLANYO_API_ENDPOINT.trim()
        : "";
    var list = [];
    if (configured) list.push(configured);
    ["/api/planyo", "api/planyo-proxy.php", REST_URL].forEach(function (u) {
      if (list.indexOf(u) === -1) list.push(u);
    });
    return list;
  }

  var resolvedEndpoint = null;
  var endpointDiscovery = null;

  function mountEl() {
    return document.getElementById("esperienze-list");
  }

  function asList(results) {
    if (!results) return [];
    if (Array.isArray(results)) return results;
    return Object.keys(results).map(function (k) {
      return results[k];
    });
  }

  function romeYmd(offsetDays) {
    var now = new Date();
    var fmt = new Intl.DateTimeFormat("en-CA", {
      timeZone: "Europe/Rome",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    });
    var base = fmt.format(now);
    var d = new Date(base + "T12:00:00");
    d.setDate(d.getDate() + (offsetDays || 0));
    var y = d.getFullYear();
    var m = String(d.getMonth() + 1).padStart(2, "0");
    var day = String(d.getDate()).padStart(2, "0");
    return y + "-" + m + "-" + day;
  }

  function augustEndYmd() {
    return romeYmd(0).slice(0, 4) + "-08-31";
  }

  function isThroughAugustPeriod() {
    return romeYmd(0) <= augustEndYmd();
  }

  function formatItDay(ymd) {
    var d = new Date(ymd + "T12:00:00");
    var s = d.toLocaleDateString(localeForDates(), {
      weekday: "long",
      day: "numeric",
      month: "long",
    });
    return s.charAt(0).toUpperCase() + s.slice(1);
  }

  function isSpecialResource(resourceId, name) {
    if (SPECIAL_RESOURCE_IDS[String(resourceId)]) return true;
    var n = String(name || "").toLowerCase();
    if (n.indexOf("casa museo walser") >= 0) return true;
    if (n.indexOf("miniera") >= 0 && n.indexOf("guia") >= 0) return true;
    if (n.indexOf("miniera d'oro") >= 0 || n.indexOf("miniera d’oro") >= 0) {
      return true;
    }
    if (n.indexOf("seggiovia") >= 0 && n.indexOf("belvedere") >= 0) return true;
    if (n.indexOf("funivie") >= 0 && n.indexOf("alpe bill") >= 0) return true;
    if (n.indexOf("funivia") >= 0 && n.indexOf("alpe bill") >= 0) return true;
    return false;
  }

  function pinRank(resourceId) {
    var idx = PINNED_RESOURCE_IDS.indexOf(String(resourceId || ""));
    return idx === -1 ? 999 : idx;
  }

  function deadlineNoticeFor(resourceId, name) {
    var id = String(resourceId || "");
    if (DEADLINE_NOTICES[id]) return DEADLINE_NOTICES[id];
    var n = String(name || "")
      .toLowerCase()
      .replace(/\s+/g, " ");
    if (n.indexOf("via del pane") >= 0) return DEADLINE_NOTICES["253421"];
    if (
      n.indexOf("alpigiano") >= 0 ||
      n.indexOf("alpagiste") >= 0 ||
      n.indexOf("alpine farmer") >= 0 ||
      n.indexOf("älpler") >= 0 ||
      n.indexOf("alpler") >= 0
    ) {
      return DEADLINE_NOTICES["253656"];
    }
    return null;
  }

  function deadlineNoticeHtml(item) {
    if (!item) return "";
    var cfg = deadlineNoticeFor(item.resourceId, item.name);
    if (!cfg) return "";
    var L = ui();
    var text = (L && L[cfg.key]) || cfg.fallback;
    return (
      '<p class="esperienze-card__deadline">' + escapeHtml(text) + "</p>"
    );
  }

  /* Keep deadline after date patches / full re-renders (progressive load). */
  function syncDeadlineNotice(card, item) {
    if (!card) return;
    var datesEl = card.querySelector(".esperienze-card__dates");
    var existingDeadline = card.querySelector(".esperienze-card__deadline");
    var notice = deadlineNoticeHtml(item);
    if (notice) {
      if (existingDeadline) {
        existingDeadline.outerHTML = notice;
      } else if (datesEl) {
        datesEl.insertAdjacentHTML("afterend", notice);
      }
    } else if (existingDeadline) {
      existingDeadline.remove();
    }
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  /* Regex strip — avoids creating a DOM node per card description. */
  function stripHtml(html) {
    return String(html || "")
      .replace(/<script[\s\S]*?<\/script>/gi, " ")
      .replace(/<style[\s\S]*?<\/style>/gi, " ")
      .replace(/<[^>]+>/g, " ")
      .replace(/&nbsp;/gi, " ")
      .replace(/&#160;/gi, " ")
      .replace(/&amp;/g, "&")
      .replace(/&lt;/g, "<")
      .replace(/&gt;/g, ">")
      .replace(/&quot;/g, '"')
      .replace(/&#39;/g, "'")
      .replace(/\u00a0/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function truncateText(text, max) {
    var t = String(text || "").trim();
    if (t.length <= max) return t;
    var cut = t.slice(0, max - 1);
    var lastSpace = cut.lastIndexOf(" ");
    if (lastSpace > Math.floor(max * 0.6)) cut = cut.slice(0, lastSpace);
    return cut.replace(/[.,;:\s]+$/, "") + "…";
  }

  function readCache() {
    try {
      var raw = localStorage.getItem(cacheKey());
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      if (!parsed || !parsed.ts || !Array.isArray(parsed.items)) return null;
      if (Date.now() - parsed.ts > CACHE_MS) return null;
      return {
        items: parsed.items,
        concluded: Array.isArray(parsed.concluded) ? parsed.concluded : [],
      };
    } catch (e) {
      return null;
    }
  }

  function writeCache(items, concluded) {
    try {
      localStorage.setItem(
        cacheKey(),
        JSON.stringify({
          ts: Date.now(),
          items: items,
          concluded: concluded || [],
        })
      );
    } catch (e) {
      /* ignore quota */
    }
  }

  function buildUrl(base, params) {
    var q = [];
    Object.keys(params).forEach(function (k) {
      if (params[k] === undefined || params[k] === null || params[k] === "") return;
      q.push(encodeURIComponent(k) + "=" + encodeURIComponent(params[k]));
    });
    var sep = base.indexOf("?") >= 0 ? "&" : "?";
    return base + sep + q.join("&");
  }

  function fetchJson(url) {
    /* no-store: proxies may send max-age=12h; stale empty get_event_times
       would stick as "Prossimamente" after Planyo dates are added. */
    return fetch(url, {
      method: "GET",
      credentials: "omit",
      cache: "no-store",
    }).then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    });
  }

  function apiCall(params) {
    if (resolvedEndpoint) {
      return fetchJson(buildUrl(resolvedEndpoint, params));
    }

    /* Share one endpoint discovery so parallel callers don't each walk candidates. */
    if (endpointDiscovery) {
      return endpointDiscovery.then(function (base) {
        return fetchJson(buildUrl(base, params));
      });
    }

    var candidates = getEndpointCandidates();
    var discover = (function tryNext(i) {
      if (i >= candidates.length) {
        return Promise.reject(new Error("No API endpoint available"));
      }
      var base = candidates[i];
      return fetchJson(buildUrl(base, params)).then(
        function (json) {
          resolvedEndpoint = base;
          return { base: base, json: json };
        },
        function () {
          return tryNext(i + 1);
        }
      );
    })(0);

    endpointDiscovery = discover
      .then(function (found) {
        return found.base;
      })
      .catch(function (err) {
        endpointDiscovery = null;
        throw err;
      });

    return discover.then(function (found) {
      return found.json;
    });
  }

  function mapPool(items, concurrency, worker) {
    var results = new Array(items.length);
    var next = 0;
    var active = 0;

    return new Promise(function (resolve, reject) {
      var kick = function () {
        if (next >= items.length && active === 0) {
          resolve(results);
          return;
        }
        while (active < concurrency && next < items.length) {
          (function (index) {
            active++;
            Promise.resolve()
              .then(function () {
                return worker(items[index], index);
              })
              .then(function (value) {
                results[index] = value;
                active--;
                kick();
              })
              .catch(reject);
          })(next++);
        }
      };
      if (!items.length) {
        resolve(results);
        return;
      }
      kick();
    });
  }

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      if (document.querySelector('script[src="' + src + '"]')) {
        resolve();
        return;
      }
      var s = document.createElement("script");
      s.src = src;
      s.async = false;
      s.onload = function () {
        resolve();
      };
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  function ensureConfig() {
    if (window.PLANYO_API_ENDPOINT || window.PLANYO_API_KEY) {
      return Promise.resolve();
    }
    return loadScript(assetPrefix() + "js/planyo-config.js").catch(function () {
      /* optional */
    });
  }

  function absoluteMediaUrl(raw) {
    var u = String(raw || "").trim();
    if (!u || u === "null" || u === "undefined") return "";
    if (/^\/\//.test(u)) u = "https:" + u;
    if (/^https?:\/\//i.test(u)) {
      return u.replace(/^http:\/\//i, "https://");
    }
    if (u.charAt(0) === "/") {
      return "https://www.planyo.com" + u;
    }
    /* Bare Planyo/S3 object key or relative media path */
    if (/^\d+_/.test(u) || /\.(jpe?g|png|webp|gif)(\?|$)/i.test(u)) {
      if (u.indexOf("/") === -1) {
        return "https://planyo-ch.s3.eu-central-2.amazonaws.com/" + u;
      }
      return "https://www.planyo.com/" + u.replace(/^\.\//, "");
    }
    return "";
  }

  function photoCandidateUrl(entry) {
    if (!entry) return "";
    if (typeof entry === "string") return absoluteMediaUrl(entry);
    if (typeof entry !== "object") return "";
    return absoluteMediaUrl(
      entry.path ||
        entry.url ||
        entry.src ||
        entry.image ||
        entry.photo ||
        entry.filename ||
        ""
    );
  }

  function isRemotePlanyoPhoto(url) {
    var u = String(url || "");
    if (!/^https:\/\//i.test(u)) return false;
    return (
      /planyo-ch\.s3[\w.-]*\.amazonaws\.com/i.test(u) ||
      /(?:^|\.)planyo\.com\//i.test(u)
    );
  }

  /* Same-origin resize/compress proxy (serve.py /api/img) — avoids 3–4MB PNGs. */
  function optimizePhotoUrl(url) {
    var u = String(url || "").trim();
    if (!u) return "";
    if (u.indexOf("/api/img") === 0) return u;
    if (!isRemotePlanyoPhoto(u)) {
      /* Local fallbacks / static assets: query bust when PHOTO_CACHE_BUST changes. */
      var sep = u.indexOf("?") >= 0 ? "&" : "?";
      return u + sep + "v=" + encodeURIComponent(PHOTO_CACHE_BUST);
    }
    return (
      "/api/img?u=" +
      encodeURIComponent(u) +
      "&w=" +
      CARD_IMG_WIDTH +
      "&q=72&f=webp&cb=" +
      encodeURIComponent(PHOTO_CACHE_BUST)
    );
  }

  function firstPhotoUrl(resource, resourceId) {
    var photos = resource && resource.photos;
    var list = asList(photos);
    var i;
    for (i = 0; i < list.length; i++) {
      var url = photoCandidateUrl(list[i]);
      if (url) return url;
    }
    var props = (resource && resource.properties) || {};
    var fromProps = absoluteMediaUrl(
      props.image ||
        props.Image ||
        props.photo ||
        props.Photo ||
        props.picture ||
        props.main_image ||
        ""
    );
    if (fromProps) return fromProps;
    /* API empty/broken — local fallback as last resort before paint. */
    var id = String(
      resourceId || (resource && (resource.id || resource.resource_id)) || ""
    );
    return id ? photoFallback(id) : "";
  }

  function bookingPageUrl(resourceId, mode, refcode) {
    var q =
      "resource_id=" +
      encodeURIComponent(resourceId) +
      "&mode=" +
      encodeURIComponent(mode || "reserve") +
      "&ppp_refcode=" +
      encodeURIComponent(refcode || "landing") +
      "&planyo_lang=" +
      encodeURIComponent(planyoLangCode());
    return assetPrefix() + "prenota.html?" + q;
  }

  function resourceDescUrl(resourceId) {
    return bookingPageUrl(resourceId, "resource_desc", "landing");
  }

  function resourceDescription(resource) {
    var props = (resource && resource.properties) || {};
    var raw =
      props.description ||
      props.Description ||
      props.desc ||
      props.short_description ||
      "";
    return truncateText(stripHtml(raw), DESC_MAX);
  }

  function horizonYmd(range) {
    if (range && range.to) return range.to;
    return romeYmd(180);
  }

  /* Accept YYYY-MM-DD, DD.MM.YYYY, DD-MM-YYYY (Planyo event_times / event_dates). */
  function ymdFromDayToken(token) {
    var raw = String(token || "").trim();
    if (!raw) return null;
    var iso = raw.match(/(\d{4})-(\d{2})-(\d{2})/);
    if (iso) return iso[1] + "-" + iso[2] + "-" + iso[3];
    var dmy = raw.match(/(\d{1,2})[.\-/](\d{1,2})[.\-/](\d{4})/);
    if (dmy) {
      var day = dmy[1].length === 1 ? "0" + dmy[1] : dmy[1];
      var month = dmy[2].length === 1 ? "0" + dmy[2] : dmy[2];
      return dmy[3] + "-" + month + "-" + day;
    }
    var months = {
      gennaio: "01",
      january: "01",
      febbraio: "02",
      february: "02",
      marzo: "03",
      march: "03",
      aprile: "04",
      april: "04",
      maggio: "05",
      may: "05",
      giugno: "06",
      june: "06",
      luglio: "07",
      july: "07",
      agosto: "08",
      august: "08",
      settembre: "09",
      september: "09",
      ottobre: "10",
      october: "10",
      novembre: "11",
      november: "11",
      dicembre: "12",
      december: "12",
    };
    var named = raw.toLowerCase().match(/(\d{1,2})\s+([a-zàèé]+)\s+(\d{4})/i);
    if (named && months[named[2]]) {
      var nd = named[1].length === 1 ? "0" + named[1] : named[1];
      return named[3] + "-" + months[named[2]] + "-" + nd;
    }
    return null;
  }

  function ymdFromTimestamp(ts) {
    var n = Number(ts);
    if (!n || !isFinite(n)) return null;
    if (n < 1e12) n *= 1000;
    var d = new Date(n);
    if (isNaN(d.getTime())) return null;
    var fmt = new Intl.DateTimeFormat("en-CA", {
      timeZone: "Europe/Rome",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    });
    return fmt.format(d);
  }

  function eventItemYmd(item) {
    if (item == null) return null;
    if (typeof item === "string" || typeof item === "number") {
      return ymdFromDayToken(item) || ymdFromTimestamp(item);
    }
    if (typeof item !== "object") return null;
    var fromTs = ymdFromTimestamp(
      item.timestamp || item.start_timestamp || item.unix_timestamp
    );
    if (fromTs) return fromTs;
    var keys = [
      "date",
      "start_date",
      "event_date",
      "day",
      "text",
      "start_time",
      "unit",
    ];
    var i;
    for (i = 0; i < keys.length; i++) {
      var ymd = ymdFromDayToken(item[keys[i]]);
      if (ymd) return ymd;
    }
    return null;
  }

  /* get_resource_info.event_dates: "01-08-2026 8:30am, 01-08-2026 6pm, ..." */
  function daysFromEventDatesString(raw, todayYmd, range) {
    var days = [];
    var seen = {};
    String(raw || "")
      .split(",")
      .forEach(function (chunk) {
        var ymd = ymdFromDayToken(chunk);
        if (!ymd) return;
        if (seen[ymd]) return;
        seen[ymd] = true;
        days.push(ymd);
      });
    days.sort();
    days = filterDaysByRange(days, range, todayYmd);
    var maxLabels = range ? 8 : MAX_DATE_LABELS;
    return days.slice(0, maxLabels);
  }

  function uniqueUpcomingDays(eventTimes, todayYmd, range) {
    var days = [];
    var seen = {};
    asList(eventTimes).forEach(function (item) {
      var ymd = eventItemYmd(item);
      if (!ymd) return;
      if (seen[ymd]) return;
      seen[ymd] = true;
      days.push(ymd);
    });
    days.sort();
    days = filterDaysByRange(days, range, todayYmd);
    var maxLabels = range ? 8 : MAX_DATE_LABELS;
    return days.slice(0, maxLabels);
  }

  function reserveUrl(resourceId) {
    return bookingPageUrl(resourceId, "reserve", "landing");
  }

  function listFallbackUrl() {
    return (
      assetPrefix() +
      "prenota.html?mode=resource_list&ppp_refcode=landing&planyo_lang=" +
      encodeURIComponent(planyoLangCode())
    );
  }

  function listResources(apiKey, siteId) {
    return apiCall({
      method: "list_resources",
      api_key: apiKey,
      site_id: siteId,
      detail_level: "15",
      list_published_only: "true",
      list_reservable_only: "true",
      language: planyoLangCode(),
      page_size: "100",
    }).then(function (json) {
      if (!json || Number(json.response_code) !== 0) {
        throw new Error(
          (json && json.response_message) || "list_resources failed"
        );
      }
      return asList(json.data && json.data.resources);
    });
  }

  function getEventTimes(apiKey, resourceId, todayYmd, range) {
    return apiCall({
      method: "get_event_times",
      api_key: apiKey,
      resource_id: resourceId,
      start_date: todayYmd,
      end_date: horizonYmd(range),
      future_only: "true",
      format: "array",
      language: planyoLangCode(),
    })
      .then(function (json) {
        if (!json || Number(json.response_code) !== 0) return [];
        return asList(json.data && json.data.event_times);
      })
      .catch(function () {
        return [];
      });
  }

  /* Fallback when get_event_times is empty/stale but resource_info lists dates. */
  function getResourceEventDateDays(apiKey, resourceId, todayYmd, range) {
    return apiCall({
      method: "get_resource_info",
      api_key: apiKey,
      resource_id: resourceId,
      language: planyoLangCode(),
    })
      .then(function (json) {
        if (!json || Number(json.response_code) !== 0) return [];
        var data = json.data || {};
        var props = data.properties || {};
        return mergeYmdLists(
          daysFromEventDatesString(data.event_dates, todayYmd, range),
          daysFromEventDatesString(data.specified_dates, todayYmd, range),
          daysFromEventDatesString(props.event_dates, todayYmd, range),
          daysFromEventDatesString(props.specified_dates, todayYmd, range)
        );
      })
      .catch(function () {
        return [];
      });
  }

  function getResourceInfo(apiKey, resourceId) {
    return apiCall({
      method: "get_resource_info",
      api_key: apiKey,
      resource_id: resourceId,
      language: planyoLangCode(),
    })
      .then(function (json) {
        if (!json || Number(json.response_code) !== 0) return null;
        var data = json.data || null;
        if (!data) return null;
        if (!data.id && !data.resource_id) data.id = resourceId;
        return data;
      })
      .catch(function () {
        return null;
      });
  }

  function loadMissingOnRequest(apiKey, existingIds, today, augustMode, range) {
    var missing = Object.keys(ON_REQUEST_IDS).filter(function (id) {
      return existingIds.indexOf(id) === -1;
    });
    if (!missing.length) return Promise.resolve([]);
    return mapPool(missing, 3, function (id) {
      return getResourceInfo(apiKey, id).then(function (r) {
        if (!r) return null;
        return markOnRequest(stubFromResource(r, today, augustMode, range));
      });
    }).then(function (rows) {
      return rows.filter(Boolean);
    });
  }

  function loadMissingComingSoon(apiKey, existingIds, today, augustMode, range) {
    var missing = Object.keys(COMING_SOON_IDS).filter(function (id) {
      return existingIds.indexOf(id) === -1;
    });
    if (!missing.length) return Promise.resolve([]);
    return mapPool(missing, 3, function (id) {
      return getResourceInfo(apiKey, id).then(function (r) {
        if (!r) return null;
        return markComingSoon(stubFromResource(r, today, augustMode, range));
      });
    }).then(function (rows) {
      return rows.filter(Boolean);
    });
  }

  function loadMissingConcluded(apiKey, existingIds, today, augustMode, range) {
    var missing = CONCLUDED_ORDER.filter(function (id) {
      return existingIds.indexOf(id) === -1;
    });
    if (!missing.length) return Promise.resolve([]);
    return mapPool(missing, 3, function (id) {
      return getResourceInfo(apiKey, id).then(function (r) {
        if (!r) return null;
        return markConcluded(stubFromResource(r, today, augustMode, range));
      });
    }).then(function (rows) {
      return rows.filter(Boolean);
    });
  }

  function mergeYmdLists() {
    var seen = {};
    var out = [];
    Array.prototype.forEach.call(arguments, function (arr) {
      (arr || []).forEach(function (ymd) {
        if (!ymd || seen[ymd]) return;
        seen[ymd] = true;
        out.push(ymd);
      });
    });
    out.sort();
    return out;
  }

  function daysFromResourcePayload(resource, todayYmd, range) {
    if (!resource) return [];
    var raw =
      resource.event_dates ||
      resource.specified_dates ||
      (resource.properties &&
        (resource.properties.event_dates || resource.properties.specified_dates)) ||
      "";
    return daysFromEventDatesString(raw, todayYmd, range);
  }

  function loadUpcomingDays(apiKey, resourceId, todayYmd, range, seedDays) {
    return Promise.all([
      getEventTimes(apiKey, resourceId, todayYmd, range),
      getResourceEventDateDays(apiKey, resourceId, todayYmd, range),
    ]).then(function (parts) {
      var days = mergeYmdLists(
        seedDays,
        uniqueUpcomingDays(parts[0], todayYmd, range),
        parts[1]
      );
      days = filterDaysByRange(days, range, todayYmd);
      var maxLabels = range ? 8 : MAX_DATE_LABELS;
      return days.slice(0, maxLabels);
    });
  }

  function sortItems(items) {
    var loc = localeForDates();
    return items.slice().sort(function (a, b) {
      var pa = pinRank(a.resourceId);
      var pb = pinRank(b.resourceId);
      if (pa !== pb) return pa - pb;
      if (a.sortKey < b.sortKey) return -1;
      if (a.sortKey > b.sortKey) return 1;
      return String(a.name).localeCompare(String(b.name), loc);
    });
  }

  /* Prefer Planyo language-specific title; `name` stays in the site default language. */
  function resourceDisplayName(r) {
    var translated = String((r && r.translated_name) || "").trim();
    if (translated) return translated;
    return String((r && r.name) || "").trim();
  }

  function stubFromResource(r, today, augustMode, range) {
    var id = String(r.id || r.resource_id || "");
    var name = resourceDisplayName(r);
    if (!id || !name) return null;
    var L = ui();

    var photo = firstPhotoUrl(r, id);
    var seedDays = daysFromResourcePayload(r, today, range);
    if (isOnRequestResource(id)) {
      return markOnRequest({
        resourceId: id,
        name: name,
        description: resourceDescription(r),
        photo: photo,
        seedDays: seedDays,
      });
    }
    var special =
      (augustMode || !!range) && isSpecialResource(id, name);
    if (special) {
      return {
        resourceId: id,
        name: name,
        description: resourceDescription(r),
        photo: photo,
        sortKey: range ? range.from : today,
        dateLabels: range
          ? [rangeSpecialLabel(range)]
          : [L.augustLabel || "Tutto Agosto"],
        upcoming: true,
        specialAugust: true,
        datesPending: false,
        seedDays: seedDays,
      };
    }

    var item = {
      resourceId: id,
      name: name,
      description: resourceDescription(r),
      photo: photo,
      sortKey: "9999-12-30",
      dateLabels: [L.datesLoading || "Loading dates…"],
      upcoming: true,
      specialAugust: false,
      datesPending: true,
      seedDays: seedDays,
    };
    if (isComingSoonResource(id)) {
      return markComingSoon(item);
    }
    if (seedDays.length) {
      applyUpcomingDays(item, seedDays);
      item.datesPending = true;
    }
    return item;
  }

  function applyUpcomingDays(item, days) {
    if (item && (item.onRequest || isOnRequestResource(item.resourceId))) {
      return markOnRequest(item);
    }
    var L = ui();
    if (!days || !days.length) {
      item.sortKey = "9999-12-31";
      item.dateLabels = [L.soon || "Coming soon"];
      item.upcoming = false;
    } else {
      item.sortKey = days[0];
      item.dateLabels = days.map(formatItDay);
      item.upcoming = true;
    }
    item.datesPending = false;
    return item;
  }

  function patchCardDates(item) {
    var el = mountEl();
    if (!el) return;
    var L = ui();
    var card = el.querySelector(
      '.esperienze-card[data-resource-id="' + item.resourceId + '"]'
    );
    if (!card) return;
    if (item && (item.onRequest || isOnRequestResource(item.resourceId))) {
      markOnRequest(item);
      var datesEl = card.querySelector(".esperienze-card__dates");
      var noticeEl = card.querySelector(".esperienze-card__on-request");
      var html = onRequestNoticeHtml(item);
      if (noticeEl) {
        noticeEl.outerHTML = html;
      } else if (datesEl) {
        datesEl.outerHTML = html;
      }
      card.classList.remove("esperienze-card--soon");
      return;
    }
    var datesEl = card.querySelector(".esperienze-card__dates");
    if (!datesEl) return;
    datesEl.className =
      "esperienze-card__dates" +
      (item.upcoming ? "" : " esperienze-card__dates--soon") +
      (item.datesPending ? " esperienze-card__dates--loading" : "");
    datesEl.innerHTML =
      '<span class="esperienze-card__dates-label">' +
      (L.nextDates || "Upcoming dates:") +
      "</span> " +
      escapeHtml(item.dateLabels.join(" · "));
    syncDeadlineNotice(card, item);
    if (item.upcoming) {
      card.classList.remove("esperienze-card--soon");
    } else {
      card.classList.add("esperienze-card--soon");
    }
  }

  function enrichPendingDates(items, apiKey) {
    var today = romeYmd(0);
    var range = getDateRange();
    var pending = items.filter(function (item) {
      return item && item.datesPending;
    });
    if (!pending.length) return Promise.resolve(items);

    return mapPool(pending, EVENT_TIMES_CONCURRENCY, function (item) {
      return loadUpcomingDays(
        apiKey,
        item.resourceId,
        today,
        range,
        item.seedDays
      ).then(function (days) {
        applyUpcomingDays(item, days);
        patchCardDates(item);
        return item;
      });
    }).then(function () {
      return items;
    });
  }

  function renderLoading() {
    var el = mountEl();
    if (!el) return;
    var L = ui();
    el.innerHTML =
      '<p class="esperienze-list__status">' +
      (L.listLoading || "Loading experiences…") +
      "</p>";
  }

  function renderError() {
    var el = mountEl();
    if (!el) return;
    var L = ui();
    var fallback = listFallbackUrl();
    el.innerHTML =
      '<div class="esperienze-list__fallback" role="alert">' +
      "<p>" +
      (L.listError ||
        "Non è stato possibile caricare l’elenco delle esperienze al momento.") +
      "</p>" +
      '<div class="btn-row">' +
      '<button type="button" class="btn btn--primary" data-esperienze-retry>' +
      (L.listRetry || "Riprova") +
      "</button>" +
      '<a class="btn btn--outline" href="' +
      escapeHtml(fallback) +
      '">' +
      (L.listOpenFallback || "Open booking list") +
      "</a>" +
      "</div></div>";
    var btn = el.querySelector("[data-esperienze-retry]");
    if (btn) {
      btn.addEventListener("click", function () {
        boot(true);
      });
    }
  }

  function renderItem(item, index, withImages) {
    var L = ui();
    var reserve = reserveUrl(item.resourceId);
    var detail = resourceDescUrl(item.resourceId);
    var rawPhoto = item.photo || photoFallback(item.resourceId) || "";
    var photoSrc = optimizePhotoUrl(rawPhoto);
    var img;
    if (!withImages) {
      /* Text-first: reserve media box; hydrate /api/img after first paint. */
      img =
        '<div class="esperienze-card__media esperienze-card__media--pending' +
        (rawPhoto ? "" : " esperienze-card__media--empty") +
        '" aria-hidden="true"' +
        (rawPhoto
          ? ' data-pending-photo="' +
            escapeHtml(rawPhoto) +
            '" data-photo-index="' +
            (typeof index === "number" ? index : 99) +
            '"'
          : "") +
        "></div>";
    } else {
      var eager = typeof index === "number" && index < EAGER_PHOTO_COUNT;
      var loadingAttrs = eager
        ? 'loading="eager" fetchpriority="low"'
        : 'loading="lazy"';
      img = photoSrc
        ? '<div class="esperienze-card__media"><img src="' +
          escapeHtml(photoSrc) +
          '" alt="" width="' +
          CARD_IMG_WIDTH +
          '" height="' +
          CARD_IMG_HEIGHT +
          '" sizes="(max-width: 720px) 100vw, 640px" ' +
          loadingAttrs +
          ' decoding="async" data-photo-fallback="1" data-photo-orig="' +
          escapeHtml(rawPhoto) +
          '"></div>'
        : '<div class="esperienze-card__media esperienze-card__media--empty" aria-hidden="true"></div>';
    }

    var datesClass =
      "esperienze-card__dates" +
      (item.concluded
        ? " esperienze-card__dates--concluded"
        : item.upcoming
          ? ""
          : " esperienze-card__dates--soon") +
      (item.datesPending ? " esperienze-card__dates--loading" : "");
    var datesHtml = item.concluded
      ? '<p class="' +
        datesClass +
        '">' +
        escapeHtml(
          (item.dateLabels && item.dateLabels[0]) ||
            L.concludedSeason ||
            "Stagione conclusa"
        ) +
        "</p>"
      : item.onRequest
        ? onRequestNoticeHtml(item)
        : '<p class="' +
          datesClass +
          '"><span class="esperienze-card__dates-label">' +
          (L.nextDates || "Upcoming dates:") +
          "</span> " +
          escapeHtml(item.dateLabels.join(" · ")) +
          "</p>" +
          (item.comingSoon ? "" : deadlineNoticeHtml(item));

    var detailBtn =
      '<a role="button" class="btn btn--outline" href="' +
      escapeHtml(detail) +
      '" data-resource-id="' +
      escapeHtml(item.resourceId) +
      '" data-action="detail">' +
      (L.details || "Dettagli") +
      "</a>";

    var bookBtn = item.concluded
      ? '<a role="button" class="btn btn--primary" href="mailto:' +
        CONTACT_MAIL +
        '">' +
        (L.contactUs || "Contattaci") +
        "</a>"
      : '<a role="button" class="btn btn-primary btn--primary" href="' +
        escapeHtml(reserve) +
        '" data-resource-id="' +
        escapeHtml(item.resourceId) +
        '" data-action="reserve">' +
        (L.bookNow || "Book now") +
        "</a>";

    return (
      '<article class="esperienze-card' +
      (item.concluded
        ? " esperienze-card--concluded"
        : item.upcoming || item.onRequest
          ? ""
          : " esperienze-card--soon") +
      '" data-resource-id="' +
      escapeHtml(item.resourceId) +
      '">' +
      img +
      '<div class="esperienze-card__body">' +
      "<h3>" +
      escapeHtml(item.name) +
      "</h3>" +
      (item.description
        ? '<p class="esperienze-card__desc">' +
          escapeHtml(item.description) +
          "</p>"
        : "") +
      datesHtml +
      '<div class="btn-row esperienze-card__actions">' +
      bookBtn +
      detailBtn +
      "</div></div></article>"
    );
  }

  function bindListInteractions(el) {
    /* Reserve / detail are plain links to prenota.html (inline Planyo). */
    bindPhotoFallbacks(el);
  }

  function bindPhotoFallbacks(el) {
    el.querySelectorAll("img[data-photo-fallback]").forEach(function (imgEl) {
      if (imgEl.dataset.fallbackBound === "1") return;
      imgEl.dataset.fallbackBound = "1";
      imgEl.addEventListener("error", function onPhotoError() {
        var src = imgEl.getAttribute("src") || "";
        var orig = imgEl.getAttribute("data-photo-orig") || "";
        /* Proxy failed → try original HTTPS once. */
        if (
          src.indexOf("/api/img") === 0 &&
          orig &&
          orig !== src &&
          imgEl.getAttribute("data-tried-orig") !== "1"
        ) {
          imgEl.setAttribute("data-tried-orig", "1");
          imgEl.src = orig;
          return;
        }
        var card = imgEl.closest("[data-resource-id]");
        var rid = card ? card.getAttribute("data-resource-id") : "";
        var fb = rid ? photoFallback(rid) : "";
        if (fb && src !== fb && orig !== fb) {
          imgEl.removeAttribute("data-photo-orig");
          imgEl.src = fb;
          return;
        }
        var media = imgEl.parentNode;
        if (media) {
          media.classList.add("esperienze-card__media--empty");
          imgEl.remove();
        }
      });
    });
  }

  /* After text paint: inject /api/img (or local) into pending media boxes. */
  function hydratePhotos(el) {
    if (!el) return;
    var pending = el.querySelectorAll("[data-pending-photo]");
    if (!pending.length) return;

    pending.forEach(function (media) {
      var rawPhoto = media.getAttribute("data-pending-photo") || "";
      var index = parseInt(media.getAttribute("data-photo-index") || "99", 10);
      var photoSrc = optimizePhotoUrl(rawPhoto);
      if (!photoSrc) {
        media.classList.add("esperienze-card__media--empty");
        media.removeAttribute("data-pending-photo");
        return;
      }
      var eager = index < EAGER_PHOTO_COUNT;
      var imgEl = document.createElement("img");
      imgEl.src = photoSrc;
      imgEl.alt = "";
      imgEl.width = CARD_IMG_WIDTH;
      imgEl.height = CARD_IMG_HEIGHT;
      imgEl.decoding = "async";
      imgEl.sizes = "(max-width: 720px) 100vw, 640px";
      imgEl.loading = eager ? "eager" : "lazy";
      if (eager) imgEl.fetchPriority = "low";
      imgEl.setAttribute("data-photo-fallback", "1");
      imgEl.setAttribute("data-photo-orig", rawPhoto);
      media.classList.remove("esperienze-card__media--pending");
      media.classList.remove("esperienze-card__media--empty");
      media.removeAttribute("data-pending-photo");
      media.removeAttribute("data-photo-index");
      media.appendChild(imgEl);
    });

    bindPhotoFallbacks(el);
  }

  function schedulePhotoHydration(el) {
    var run = function () {
      hydratePhotos(el);
    };
    /* Two rAFs ≈ after first paint of text cards. */
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        if (typeof requestIdleCallback === "function") {
          requestIdleCallback(run, { timeout: 800 });
        } else {
          setTimeout(run, 50);
        }
      });
    });
  }

  function renderGrid(items, showImages, startIndex) {
    var offset = typeof startIndex === "number" ? startIndex : 0;
    return (
      '<div class="esperienze-list__grid" role="list">' +
      items
        .map(function (item, index) {
          return (
            '<div role="listitem">' +
            renderItem(item, offset + index, showImages) +
            "</div>"
          );
        })
        .join("") +
      "</div>"
    );
  }

  function concludedLeadHtml() {
    var L = ui();
    var raw =
      L.concludedLead ||
      "Se sei interessato a queste esperienze torna a visitarci la prossima stagione. Se sei un gruppo oppure un operatore {contact}.";
    var label = L.contactUs || "contattaci";
    var link =
      '<a href="mailto:' + CONTACT_MAIL + '">' + escapeHtml(label) + "</a>";
    if (raw.indexOf("{contact}") >= 0) {
      return raw.split("{contact}").map(escapeHtml).join(link);
    }
    return escapeHtml(raw) + " " + link;
  }

  function render(items, withImages, concluded) {
    var el = mountEl();
    if (!el) return;
    var L = ui();
    var showImages = withImages === true;
    var active = (items || []).map(function (item) {
      return isOnRequestResource(item && item.resourceId)
        ? markOnRequest(item)
        : item;
    });
    var closed = concluded || [];
    if (!active.length && !closed.length) {
      var emptyMsg = getDateRange()
        ? L.listEmptyRange ||
          L.listEmpty ||
          "No bookable experiences in these dates."
        : L.listEmpty || "No experiences available at the moment.";
      el.innerHTML =
        '<p class="esperienze-list__status">' + emptyMsg + "</p>";
      return;
    }
    var html = "";
    if (active.length) {
      html += renderGrid(active, showImages, 0);
    }
    if (closed.length) {
      html +=
        '<section class="esperienze-concluded" aria-labelledby="esperienze-concluded-title">' +
        '<h2 id="esperienze-concluded-title" class="esperienze-concluded__title">' +
        escapeHtml(L.concludedTitle || "Esperienze concluse") +
        "</h2>" +
        '<p class="esperienze-concluded__lead">' +
        concludedLeadHtml() +
        "</p>" +
        renderGrid(closed, showImages, active.length) +
        "</section>";
    }
    el.innerHTML = html;

    active.concat(closed).forEach(function (item) {
      if (!item || item.concluded) return;
      var card = el.querySelector(
        '.esperienze-card[data-resource-id="' + item.resourceId + '"]'
      );
      syncDeadlineNotice(card, item);
    });

    bindListInteractions(el);
    if (!showImages) {
      schedulePhotoHydration(el);
    }
  }

  function fetchAndRender() {
    var apiKey = getApiKey();
    var today = romeYmd(0);
    var augustMode = isThroughAugustPeriod();
    var loc = localeForDates();
    var wanted = planyoLangCode();

    function listWithFallback() {
      return listResources(apiKey, getSiteId()).then(function (resources) {
        if (wanted === "IT") return resources;
        var missing = resources.filter(function (r) {
          return !(r && resourceDisplayName(r));
        });
        if (!missing.length) return resources;
        /* Fallback IT names/descriptions when target language is empty */
        return apiCall({
          method: "list_resources",
          api_key: apiKey,
          site_id: getSiteId(),
          detail_level: "15",
          list_published_only: "true",
          list_reservable_only: "true",
          language: "IT",
          page_size: "100",
        }).then(function (json) {
          if (!json || Number(json.response_code) !== 0) return resources;
          var itMap = {};
          asList(json.data && json.data.resources).forEach(function (r) {
            var id = String(r.id || r.resource_id || "");
            if (id) itMap[id] = r;
          });
          return resources.map(function (r) {
            var id = String(r.id || r.resource_id || "");
            var it = itMap[id];
            if (!it) return r;
            if (!resourceDisplayName(r)) {
              r.translated_name = "";
              r.name = it.translated_name || it.name || "";
            }
            var props = r.properties || {};
            var itProps = it.properties || {};
            if (
              !String(
                props.description ||
                  props.Description ||
                  props.desc ||
                  props.short_description ||
                  ""
              ).trim()
            ) {
              r.properties = r.properties || {};
              r.properties.description =
                itProps.description ||
                itProps.Description ||
                itProps.desc ||
                itProps.short_description ||
                "";
            }
            return r;
          });
        });
      });
    }

    return listWithFallback().then(function (resources) {
      var range = getDateRange();
      var wantConcluded = showConcludedBox();
      var stubs = resources
        .map(function (r) {
          return stubFromResource(r, today, augustMode, range);
        })
        .filter(Boolean);

      var concluded = [];
      var activeStubs = stubs.filter(function (item) {
        if (wantConcluded && isConcludedResource(item.resourceId)) {
          concluded.push(markConcluded(item));
          return false;
        }
        return true;
      });

      activeStubs.sort(function (a, b) {
        var pa = pinRank(a.resourceId);
        var pb = pinRank(b.resourceId);
        if (pa !== pb) return pa - pb;
        return String(a.name).localeCompare(String(b.name), loc);
      });

      function finish(activeItems, concludedItems) {
        var kept = activeItems.map(function (item) {
          return isOnRequestResource(item && item.resourceId)
            ? markOnRequest(item)
            : item;
        });
        if (range) {
          kept = kept.filter(function (item) {
            return (
              item &&
              (item.specialAugust ||
                item.upcoming ||
                item.comingSoon ||
                item.onRequest)
            );
          });
        }
        var sorted = sortItems(kept).map(serializeCard);
        var closed = sortConcluded(concludedItems).map(serializeCard);
        writeCache(sorted, closed);
        render(sorted, false, closed);
      }

      function serializeCard(item) {
        return {
          resourceId: item.resourceId,
          name: item.name,
          description: item.description,
          photo: item.photo,
          sortKey: item.sortKey,
          dateLabels: item.dateLabels,
          upcoming: item.upcoming,
          specialAugust: item.specialAugust,
          concluded: !!item.concluded,
          comingSoon: !!item.comingSoon,
          onRequest: !!item.onRequest,
          onRequestText: item.onRequestText || "",
        };
      }

      var seenIds = stubs.map(function (item) {
        return item.resourceId;
      });

      /* Full catalog: text-first paint, then date patches. Windowed pages wait
         until dates are filtered so the list doesn't flash unrelated cards. */
      if (!range) {
        render(activeStubs, false, sortConcluded(concluded));
      }

      var missingPromise = wantConcluded
        ? loadMissingConcluded(apiKey, seenIds, today, augustMode, range)
        : Promise.resolve([]);
      var missingSoonPromise = loadMissingComingSoon(
        apiKey,
        seenIds,
        today,
        augustMode,
        range
      );
      var missingOnRequestPromise = loadMissingOnRequest(
        apiKey,
        seenIds,
        today,
        augustMode,
        range
      );

      return Promise.all([
        enrichPendingDates(activeStubs, apiKey),
        missingPromise,
        missingSoonPromise,
        missingOnRequestPromise,
      ]).then(function (parts) {
        finish(
          parts[0].concat(parts[2], parts[3]),
          concluded.concat(parts[1])
        );
      });
    });
  }

  function boot(forceRefresh) {
    var el = mountEl();
    if (!el) return;

    ensureConfig()
      .then(function () {
        if (!forceRefresh) {
          var cached = readCache();
          if (cached) {
            render(cached.items, false, cached.concluded);
            return;
          }
        }
        renderLoading();
        return fetchAndRender();
      })
      .catch(function () {
        renderError();
      });
  }

  function scheduleBoot(forceRefresh) {
    var run = function () {
      boot(forceRefresh);
    };
    /* Let hero/copy paint before Planyo list work (still soon). */
    if (forceRefresh) {
      run();
      return;
    }
    if (typeof requestIdleCallback === "function") {
      requestIdleCallback(run, { timeout: 1200 });
    } else {
      setTimeout(run, 0);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      scheduleBoot(false);
    });
  } else {
    scheduleBoot(false);
  }
})();
