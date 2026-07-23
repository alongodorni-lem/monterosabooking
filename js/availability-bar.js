/* Site-wide bookable activities highlight bar (15 soonest date slots) */
(function () {
  "use strict";

  var SITE_ID = 70864;
  /* Hard TTL in localStorage. Force refresh after Planyo admin changes: bump
     CACHE_KEY (e.g. v8), or clear localStorage key mem_avail_bar_*. */
  var CACHE_KEY_BASE = "mem_avail_bar_v9_ticker15";
  var CACHE_MS = 12 * 60 * 60 * 1000;
  var MAX_ITEMS = 15;
  var MIN_DAYS = 7;
  var MAX_DAYS = 14;
  var REST_URL = "https://www.planyo.com/rest/";
  var SPECIAL_RESOURCE_IDS = {
    "253398": true, /* Casa Museo Walser */
    "252705": true, /* Miniera d'Oro della Guia */
  };

  function siteLang() {
    return window.MB_I18N ? window.MB_I18N.detectLang() : "it";
  }

  function planyoLangCode() {
    return window.MB_I18N ? window.MB_I18N.planyoLang(siteLang()) : "IT";
  }

  function ui() {
    return window.MB_I18N ? window.MB_I18N.t(siteLang()) : {};
  }

  function cacheKey() {
    return CACHE_KEY_BASE + "_" + siteLang();
  }

  function localeForDates() {
    var map = { it: "it-IT", en: "en-GB", fr: "fr-FR", de: "de-DE" };
    return map[siteLang()] || "it-IT";
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

  function mountEl() {
    return document.getElementById("availability-bar");
  }

  function hideBar() {
    var el = mountEl();
    if (!el) return;
    el.hidden = true;
    el.innerHTML = "";
    el.classList.remove("is-visible");
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
    var base = fmt.format(now); // YYYY-MM-DD
    var d = new Date(base + "T12:00:00");
    d.setDate(d.getDate() + (offsetDays || 0));
    var y = d.getFullYear();
    var m = String(d.getMonth() + 1).padStart(2, "0");
    var day = String(d.getDate()).padStart(2, "0");
    return y + "-" + m + "-" + day;
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

  function augustEndYmd() {
    return romeYmd(0).slice(0, 4) + "-08-31";
  }

  function isThroughAugustPeriod() {
    return romeYmd(0) <= augustEndYmd();
  }

  function daysInclusiveThrough(ymdEnd) {
    var start = romeYmd(0);
    if (start > ymdEnd) return 0;
    var a = new Date(start + "T12:00:00");
    var b = new Date(ymdEnd + "T12:00:00");
    return Math.round((b - a) / 86400000) + 1;
  }

  function getSearchHorizonDays() {
    var horizon = MAX_DAYS;
    if (isThroughAugustPeriod()) {
      var throughAug = daysInclusiveThrough(augustEndYmd());
      if (throughAug > horizon) horizon = throughAug;
    }
    return horizon;
  }

  function isSpecialResource(resourceId, name) {
    if (SPECIAL_RESOURCE_IDS[String(resourceId)]) return true;
    var n = String(name || "").toLowerCase();
    /* Prefer precise titles so sibling activities (e.g. "Piccoli folletti… Walser") stay normal. */
    if (n.indexOf("casa museo walser") >= 0) return true;
    if (n.indexOf("miniera") >= 0 && n.indexOf("guia") >= 0) return true;
    if (n.indexOf("miniera d'oro") >= 0 || n.indexOf("miniera d’oro") >= 0) return true;
    return false;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function readCache() {
    try {
      var raw = localStorage.getItem(cacheKey());
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
      localStorage.setItem(
        cacheKey(),
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

  function searchDay(ymd, apiKey, siteId) {
    return apiCall({
      method: "resource_search",
      api_key: apiKey,
      site_id: siteId,
      start_time: ymd + " 00:00",
      end_time: ymd + " 23:59",
      quantity: 1,
      range_search: "1",
      language: planyoLangCode(),
      skip_reason_not_listed: "true",
      skip_pricing_log: "true",
    })
      .then(function (json) {
        var items = [];
        if (!json || Number(json.response_code) !== 0) return items;
        var results = asList(json.data && json.data.results);
        results.forEach(function (r) {
          if (!r || r.is_unavailable) return;
          var id = r.id || r.resource_id;
          var name = String(r.translated_name || r.name || "").trim();
          if (!id || !name) return;
          items.push({
            resourceId: String(id),
            name: name,
            date: ymd,
            dateLabel: formatItDay(ymd),
          });
        });
        return items;
      })
      .catch(function () {
        return [];
      });
  }

  function fetchItems(apiKey, siteId) {
    var flat = [];
    var seen = {};
    var specialSeen = {};
    var augustMode = isThroughAugustPeriod();
    var horizonDays = getSearchHorizonDays();
    var daysThroughAug = augustMode ? daysInclusiveThrough(augustEndYmd()) : 0;

    function absorb(dayItems, specialsOnly) {
      var L = ui();
      var augustDaily = L.augustDaily || "Agosto tutti i giorni";
      dayItems.forEach(function (item) {
        var special = augustMode && isSpecialResource(item.resourceId, item.name);
        if (specialsOnly && !special) return;

        if (special) {
          if (specialSeen[item.resourceId]) return;
          specialSeen[item.resourceId] = true;
          seen["special|" + item.resourceId] = true;
          flat.push({
            date: item.date,
            dateLabel: augustDaily,
            resourceId: item.resourceId,
            name: item.name,
          });
          return;
        }

        var key = item.date + "|" + item.resourceId;
        if (seen[key]) return;
        seen[key] = true;
        flat.push({
          date: item.date,
          dateLabel: item.dateLabel,
          resourceId: item.resourceId,
          name: item.name,
        });
      });
    }

    function knownSpecialsFound() {
      return (
        specialSeen["253398"] &&
        specialSeen["252705"]
      );
    }

    function shouldStop(offset) {
      var daysSearched = offset + 1;
      if (daysSearched >= horizonDays) return true;

      var hasEnough =
        flat.length >= MAX_ITEMS && daysSearched >= MIN_DAYS;
      if (!hasEnough) return false;

      /* Keep scanning through Aug 31 until both specials appear (or horizon). */
      if (
        augustMode &&
        !knownSpecialsFound() &&
        daysSearched < daysThroughAug
      ) {
        return false;
      }
      return true;
    }

    function nextDay(offset) {
      var ymd = romeYmd(offset);
      var specialsOnly =
        augustMode &&
        flat.length >= MAX_ITEMS &&
        offset + 1 > MIN_DAYS &&
        !knownSpecialsFound();

      return searchDay(ymd, apiKey, siteId).then(function (dayItems) {
        absorb(dayItems, specialsOnly);
        if (shouldStop(offset)) {
          return finalizeItems(flat);
        }
        return nextDay(offset + 1);
      });
    }

    return nextDay(0);
  }

  function byDateThenName(a, b) {
    if (a.date < b.date) return -1;
    if (a.date > b.date) return 1;
    return String(a.name).localeCompare(String(b.name), localeForDates());
  }

  /* Prefer including August daily specials when found; fill the rest soonest-first. */
  function finalizeItems(flat) {
    var L = ui();
    var augustDaily = L.augustDaily || "Agosto tutti i giorni";
    var specials = [];
    var regulars = [];
    flat.forEach(function (item) {
      if (item.dateLabel === augustDaily) specials.push(item);
      else regulars.push(item);
    });
    specials.sort(byDateThenName);
    regulars.sort(byDateThenName);
    var room = Math.max(0, MAX_ITEMS - specials.length);
    return regulars
      .slice(0, room)
      .concat(specials)
      .sort(byDateThenName)
      .slice(0, MAX_ITEMS);
  }

  function reserveUrl(resourceId) {
    return (
      "https://www.planyo.com/booking.php?mode=reserve&calendar=" +
      encodeURIComponent(getSiteId()) +
      "&resource_id=" +
      encodeURIComponent(resourceId) +
      "&ppp_refcode=landing&planyo_lang=" +
      encodeURIComponent(planyoLangCode())
    );
  }

  function openReserve(resourceId, evt) {
    if (evt) {
      evt.preventDefault();
    }
    var url = reserveUrl(resourceId);
    if (typeof window.planyo_show_plugin_lightbox === "function") {
      window.planyo_show_plugin_lightbox(url);
      return;
    }
    window.location.href = "esperienze.html";
  }

  function renderItem(item) {
    return (
      '<li class="availability-bar__item">' +
      '<span class="availability-bar__date">' +
      escapeHtml(item.dateLabel) +
      "</span>" +
      '<span class="availability-bar__sep" aria-hidden="true"> — </span>' +
      '<a class="availability-bar__link" href="' +
      escapeHtml(reserveUrl(item.resourceId)) +
      '" data-resource-id="' +
      escapeHtml(item.resourceId) +
      '">' +
      escapeHtml(item.name) +
      "</a>" +
      "</li>"
    );
  }

  function render(items) {
    var el = mountEl();
    if (!el) return;
    if (!items || !items.length) {
      hideBar();
      return;
    }

    var L = ui();
    var slots = items.slice(0, MAX_ITEMS);
    var row = slots.map(renderItem).join("");
    /* Duplicate for seamless infinite scroll when content is short */
    var loop = row + row;

    el.hidden = false;
    el.classList.add("is-visible");
    el.innerHTML =
      '<div class="availability-bar__inner container">' +
      '<div class="availability-bar__viewport" aria-label="' +
      (L.availAria || "Prossime disponibilità") +
      '">' +
      '<ul class="availability-bar__track" role="list">' +
      loop +
      "</ul>" +
      "</div>" +
      '<a class="availability-bar__all" href="esperienze.html">' +
      (L.seeAll || "Vedi tutto") +
      "</a>" +
      "</div>";

    el.querySelectorAll("[data-resource-id]").forEach(function (a) {
      a.addEventListener("click", function (evt) {
        openReserve(a.getAttribute("data-resource-id"), evt);
      });
    });

    /* Touch: pause while interacting so a tap can land on a moving link */
    var viewport = el.querySelector(".availability-bar__viewport");
    var resumeTimer = null;
    function pauseForTouch() {
      if (resumeTimer) {
        clearTimeout(resumeTimer);
        resumeTimer = null;
      }
      el.classList.add("is-interacting");
    }
    function scheduleResume() {
      if (resumeTimer) clearTimeout(resumeTimer);
      resumeTimer = setTimeout(function () {
        el.classList.remove("is-interacting");
        resumeTimer = null;
      }, 900);
    }
    if (viewport) {
      viewport.addEventListener("touchstart", pauseForTouch, { passive: true });
      viewport.addEventListener("touchend", scheduleResume, { passive: true });
      viewport.addEventListener("touchcancel", scheduleResume, { passive: true });
    }
  }

  function boot() {
    var el = mountEl();
    if (!el) return;

    var apiKey = getApiKey();
    /* Empty key OK: serve.py injects PLANYO_API_KEY on /api/planyo. */

    var cached = readCache();
    if (cached) {
      render(cached);
      return;
    }

    fetchItems(apiKey, getSiteId())
      .then(function (items) {
        writeCache(items);
        render(items);
      })
      .catch(function () {
        hideBar();
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
