/* Custom experiences list: sorted by next available day via /api/planyo */
(function () {
  "use strict";

  var SITE_ID = 70864;
  var CACHE_KEY = "mem_esperienze_list_v3";
  var CACHE_MS = 20 * 60 * 1000;
  var MAX_DATE_LABELS = 5;
  var DESC_MAX = 220;
  var AUGUST_LABEL = "Tutto Agosto";
  var REST_URL = "https://www.planyo.com/rest/";
  var SPECIAL_RESOURCE_IDS = {
    "253398": true /* Casa Museo Walser */,
    "252705": true /* Miniera d'Oro della Guia */,
  };
  /* Reliable local images when Planyo photo is missing/broken (e.g. huge S3 PNGs). */
  var PHOTO_FALLBACKS = {
    "252382": "assets/web/forest-bathing.jpg",
    "253390": "assets/web/forest-bathing.jpg",
  };

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
    var s = d.toLocaleDateString("it-IT", {
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
    return false;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function stripHtml(html) {
    var tmp = document.createElement("div");
    tmp.innerHTML = String(html || "");
    var text = (tmp.textContent || tmp.innerText || "")
      .replace(/\u00a0/g, " ")
      .replace(/\s+/g, " ")
      .trim();
    return text;
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
      var raw = sessionStorage.getItem(CACHE_KEY);
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      if (!parsed || !parsed.ts || !Array.isArray(parsed.items)) return null;
      if (Date.now() - parsed.ts > CACHE_MS) return null;
      return parsed.items;
    } catch (e) {
      return null;
    }
  }

  function writeCache(items) {
    try {
      sessionStorage.setItem(
        CACHE_KEY,
        JSON.stringify({ ts: Date.now(), items: items })
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
    var candidates = getEndpointCandidates();
    var tryNext = function (i) {
      if (i >= candidates.length) {
        return Promise.reject(new Error("No API endpoint available"));
      }
      var base = candidates[i];
      return fetchJson(buildUrl(base, params)).then(
        function (json) {
          resolvedEndpoint = base;
          return json;
        },
        function () {
          return tryNext(i + 1);
        }
      );
    };
    return tryNext(0);
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
    return loadScript("js/planyo-config.js").catch(function () {
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

  function firstPhotoUrl(resource, resourceId) {
    var id = String(
      resourceId || (resource && (resource.id || resource.resource_id)) || ""
    );
    /* Known local overrides first (reliable card thumbnails). */
    if (id && PHOTO_FALLBACKS[id]) return PHOTO_FALLBACKS[id];

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
    return "";
  }

  function resourceDescUrl(resourceId) {
    return (
      "https://www.planyo.com/booking.php?calendar=" +
      encodeURIComponent(getSiteId()) +
      "&mode=resource_desc&resource_id=" +
      encodeURIComponent(resourceId) +
      "&presentation_mode=1&planyo_lang=IT"
    );
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

  function ymdFromDmy(dmy) {
    var m = String(dmy || "").match(/^(\d{1,2})\.(\d{1,2})\.(\d{4})$/);
    if (!m) return null;
    var day = m[1].padStart(2, "0");
    var month = m[2].padStart(2, "0");
    return m[3] + "-" + month + "-" + day;
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
    if (typeof item === "string") {
      var part = item.trim().split(/\s+/)[0];
      if (/^\d{4}-\d{2}-\d{2}$/.test(part)) return part;
      return ymdFromDmy(part);
    }
    if (typeof item !== "object") return null;
    if (item.available === 0 || item.available === "0" || item.available === false) {
      /* still list the day if it's a scheduled event slot */
    }
    var fromTs = ymdFromTimestamp(item.timestamp);
    if (fromTs) return fromTs;
    var text = String(item.text || item.start_time || item.date || "").trim();
    if (!text) return null;
    var dayPart = text.split(/\s+/)[0];
    if (/^\d{4}-\d{2}-\d{2}$/.test(dayPart)) return dayPart;
    return ymdFromDmy(dayPart);
  }

  function uniqueUpcomingDays(eventTimes, todayYmd) {
    var days = [];
    var seen = {};
    asList(eventTimes).forEach(function (item) {
      var ymd = eventItemYmd(item);
      if (!ymd || ymd < todayYmd) return;
      if (seen[ymd]) return;
      seen[ymd] = true;
      days.push(ymd);
    });
    days.sort();
    return days.slice(0, MAX_DATE_LABELS);
  }

  function reserveUrl(resourceId) {
    return (
      "https://www.planyo.com/booking.php?mode=reserve&calendar=" +
      encodeURIComponent(getSiteId()) +
      "&resource_id=" +
      encodeURIComponent(resourceId) +
      "&ppp_refcode=landing"
    );
  }

  /* On-site Planyo plugin overlay (X to close). Never leave the portal. */
  function openInLightbox(url, evt) {
    if (evt) {
      evt.preventDefault();
      if (evt.stopPropagation) evt.stopPropagation();
    }
    if (!url) return;
    if (typeof window.planyo_show_plugin_lightbox === "function") {
      window.planyo_show_plugin_lightbox(url);
      return;
    }
    /* li.js not ready — create overlay DOM if helpers exist */
    if (typeof window.planyo_li_create === "function") {
      window.planyo_li_create(url);
      var liWindow = document.getElementById("planyo_li_window");
      var liBg = document.getElementById("planyo_li_bg_hider");
      if (liWindow) liWindow.style.display = "block";
      if (liBg) liBg.style.display = "block";
    }
  }

  function openReserve(resourceId, evt) {
    openInLightbox(reserveUrl(resourceId), evt);
  }

  function openDetail(resourceId, evt) {
    openInLightbox(resourceDescUrl(resourceId), evt);
  }

  function listResources(apiKey, siteId) {
    return apiCall({
      method: "list_resources",
      api_key: apiKey,
      site_id: siteId,
      detail_level: "15",
      list_published_only: "true",
      list_reservable_only: "true",
      language: "IT",
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

  function getEventTimes(apiKey, resourceId) {
    return apiCall({
      method: "get_event_times",
      api_key: apiKey,
      resource_id: resourceId,
      future_only: "true",
      format: "array",
      language: "IT",
    })
      .then(function (json) {
        if (!json || Number(json.response_code) !== 0) return [];
        return asList(json.data && json.data.event_times);
      })
      .catch(function () {
        return [];
      });
  }

  function buildItems(resources, apiKey) {
    var today = romeYmd(0);
    var augustMode = isThroughAugustPeriod();

    var jobs = resources.map(function (r) {
      var id = String(r.id || r.resource_id || "");
      var name = String(r.name || "");
      if (!id || !name) return Promise.resolve(null);

      var photo = firstPhotoUrl(r, id);
      var special = augustMode && isSpecialResource(id, name);
      if (special) {
        return Promise.resolve({
          resourceId: id,
          name: name,
          description: resourceDescription(r),
          photo: photo,
          sortKey: today,
          dateLabels: [AUGUST_LABEL],
          upcoming: true,
          specialAugust: true,
        });
      }

      return getEventTimes(apiKey, id).then(function (times) {
        var days = uniqueUpcomingDays(times, today);
        if (!days.length) {
          return {
            resourceId: id,
            name: name,
            description: resourceDescription(r),
            photo: photo,
            sortKey: "9999-12-31",
            dateLabels: ["Prossimamente"],
            upcoming: false,
            specialAugust: false,
          };
        }
        return {
          resourceId: id,
          name: name,
          description: resourceDescription(r),
          photo: photo,
          sortKey: days[0],
          dateLabels: days.map(formatItDay),
          upcoming: true,
          specialAugust: false,
        };
      });
    });

    return Promise.all(jobs).then(function (items) {
      return items
        .filter(Boolean)
        .sort(function (a, b) {
          if (a.sortKey < b.sortKey) return -1;
          if (a.sortKey > b.sortKey) return 1;
          return String(a.name).localeCompare(String(b.name), "it");
        });
    });
  }

  function renderLoading() {
    var el = mountEl();
    if (!el) return;
    el.innerHTML =
      '<p class="esperienze-list__status">Caricamento esperienze…</p>';
  }

  function renderError() {
    var el = mountEl();
    if (!el) return;
    var fallback =
      "https://www.planyo.com/booking.php?calendar=" +
      encodeURIComponent(getSiteId()) +
      "&mode=resource_list&ppp_refcode=landing";
    el.innerHTML =
      '<div class="esperienze-list__fallback" role="alert">' +
      "<p>Non è stato possibile caricare l’elenco delle esperienze al momento.</p>" +
      '<div class="btn-row">' +
      '<button type="button" class="btn btn--primary" data-esperienze-retry>Riprova</button>' +
      '<a class="btn btn--outline" href="' +
      escapeHtml(fallback) +
      '" data-action="lightbox-fallback">Apri elenco prenotazioni</a>' +
      "</div></div>";
    var btn = el.querySelector("[data-esperienze-retry]");
    if (btn) {
      btn.addEventListener("click", function () {
        boot(true);
      });
    }
    var fallbackLink = el.querySelector('[data-action="lightbox-fallback"]');
    if (fallbackLink) {
      fallbackLink.addEventListener("click", function (evt) {
        openInLightbox(fallback, evt);
      });
    }
  }

  function renderItem(item) {
    var reserve = reserveUrl(item.resourceId);
    var detail = resourceDescUrl(item.resourceId);
    var photoSrc = item.photo || PHOTO_FALLBACKS[String(item.resourceId)] || "";
    var img = photoSrc
      ? '<div class="esperienze-card__media"><img src="' +
        escapeHtml(photoSrc) +
        '" alt="" width="640" height="400" loading="lazy" data-photo-fallback="1"></div>'
      : '<div class="esperienze-card__media esperienze-card__media--empty" aria-hidden="true"></div>';

    var datesClass =
      "esperienze-card__dates" +
      (item.upcoming ? "" : " esperienze-card__dates--soon");
    var datesHtml =
      '<p class="' +
      datesClass +
      '"><span class="esperienze-card__dates-label">Prossime date:</span> ' +
      escapeHtml(item.dateLabels.join(" · ")) +
      "</p>";

    var detailBtn =
      '<a role="button" class="btn btn--outline" href="' +
      escapeHtml(detail) +
      '" data-resource-id="' +
      escapeHtml(item.resourceId) +
      '" data-action="detail">Dettagli</a>';

    var bookBtn =
      '<a role="button" class="btn btn-primary btn--primary" href="' +
      escapeHtml(reserve) +
      '" data-resource-id="' +
      escapeHtml(item.resourceId) +
      '" data-action="reserve">Effettua prenotazione</a>';

    return (
      '<article class="esperienze-card' +
      (item.upcoming ? "" : " esperienze-card--soon") +
      '" data-resource-id="' +
      escapeHtml(item.resourceId) +
      '">' +
      img +
      '<div class="esperienze-card__body">' +
      "<h3>" +
      escapeHtml(item.name) +
      "</h3>" +
      (item.description
        ? "<p class=\"esperienze-card__desc\">" +
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

  function render(items) {
    var el = mountEl();
    if (!el) return;
    if (!items || !items.length) {
      el.innerHTML =
        '<p class="esperienze-list__status">Nessuna esperienza disponibile al momento.</p>';
      return;
    }
    el.innerHTML =
      '<div class="esperienze-list__grid" role="list">' +
      items
        .map(function (item) {
          return (
            '<div role="listitem">' + renderItem(item) + "</div>"
          );
        })
        .join("") +
      "</div>";

    el.querySelectorAll('[data-action="reserve"]').forEach(function (a) {
      a.addEventListener("click", function (evt) {
        openReserve(a.getAttribute("data-resource-id"), evt);
      });
    });

    el.querySelectorAll('[data-action="detail"]').forEach(function (a) {
      a.addEventListener("click", function (evt) {
        openDetail(a.getAttribute("data-resource-id"), evt);
      });
    });

    el.querySelectorAll("img[data-photo-fallback]").forEach(function (imgEl) {
      imgEl.addEventListener("error", function () {
        var card = imgEl.closest("[data-resource-id]");
        var rid = card ? card.getAttribute("data-resource-id") : "";
        var fb = rid ? PHOTO_FALLBACKS[String(rid)] : "";
        if (fb && imgEl.getAttribute("src") !== fb) {
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

  function fetchAndRender() {
    var apiKey = getApiKey();
    return listResources(apiKey, getSiteId())
      .then(function (resources) {
        return buildItems(resources, apiKey);
      })
      .then(function (items) {
        writeCache(items);
        render(items);
      });
  }

  function boot(forceRefresh) {
    var el = mountEl();
    if (!el) return;

    renderLoading();

    ensureConfig()
      .then(function () {
        if (!forceRefresh) {
          var cached = readCache();
          if (cached) {
            render(cached);
            return;
          }
        }
        return fetchAndRender();
      })
      .catch(function () {
        renderError();
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      boot(false);
    });
  } else {
    boot(false);
  }
})();
