/* Early language preference + browser-locale redirect (load in <head>). */
(function (global) {
  "use strict";

  var SUPPORTED = ["it", "en", "fr", "de"];
  var STORAGE_KEY = "site_lang";

  function detectPageLang() {
    try {
      var parts = (location.pathname || "").split("/").filter(Boolean);
      if (parts.length && SUPPORTED.indexOf(parts[0]) >= 0 && parts[0] !== "it") {
        return parts[0];
      }
    } catch (e) {
      /* ignore */
    }
    var htmlLang = (
      (document.documentElement && document.documentElement.lang) ||
      "it"
    )
      .slice(0, 2)
      .toLowerCase();
    if (SUPPORTED.indexOf(htmlLang) >= 0) return htmlLang;
    return "it";
  }

  function currentPageFile() {
    var parts = (location.pathname || "").split("/").filter(Boolean);
    if (parts.length && SUPPORTED.indexOf(parts[0]) >= 0 && parts[0] !== "it") {
      parts = parts.slice(1);
    }
    var file = (parts.pop() || "index.html").toLowerCase();
    if (!file || file.indexOf(".") === -1) file = "index.html";
    return file;
  }

  /** Relative href to the same page in another language (mirrors MB_I18N.localHref). */
  function localHref(lang, file) {
    var f = file || currentPageFile();
    var cur = detectPageLang();
    if (lang === cur) {
      return f === "index.html" ? (cur === "it" ? "index.html" : "./") : f;
    }
    if (lang === "it") {
      return f === "index.html" ? "../" : "../" + f;
    }
    if (cur === "it") {
      return f === "index.html" ? lang + "/" : lang + "/" + f;
    }
    return f === "index.html" ? "../" + lang + "/" : "../" + lang + "/" + f;
  }

  function getPreferredLang() {
    try {
      var v = (localStorage.getItem(STORAGE_KEY) || "").slice(0, 2).toLowerCase();
      if (SUPPORTED.indexOf(v) >= 0) return v;
    } catch (e) {
      /* ignore */
    }
    return null;
  }

  function setPreferredLang(lang) {
    var code = String(lang || "")
      .slice(0, 2)
      .toLowerCase();
    if (SUPPORTED.indexOf(code) < 0) return;
    try {
      localStorage.setItem(STORAGE_KEY, code);
    } catch (e) {
      /* ignore */
    }
  }

  function detectBrowserLang() {
    var list = [];
    try {
      if (navigator.languages && navigator.languages.length) {
        list = Array.prototype.slice.call(navigator.languages);
      } else if (navigator.language) {
        list = [navigator.language];
      }
    } catch (e) {
      /* ignore */
    }
    for (var i = 0; i < list.length; i++) {
      var code = String(list[i] || "")
        .slice(0, 2)
        .toLowerCase();
      if (SUPPORTED.indexOf(code) >= 0) return code;
    }
    return "it";
  }

  function queryLang() {
    try {
      var m = /[?&]lang=([a-zA-Z]{2})/.exec(location.search || "");
      if (!m) return null;
      var code = m[1].toLowerCase();
      return SUPPORTED.indexOf(code) >= 0 ? code : null;
    } catch (e) {
      return null;
    }
  }

  function stripLangQuery(url) {
    try {
      var u = new URL(url, location.href);
      u.searchParams.delete("lang");
      var q = u.searchParams.toString();
      return u.pathname + (q ? "?" + q : "") + u.hash;
    } catch (e) {
      return url;
    }
  }

  function redirectTo(lang) {
    var href = localHref(lang, currentPageFile());
    href = stripLangQuery(href);
    if (!href) return;
    location.replace(href);
  }

  function maybeApplyLangRedirect() {
    var cur = detectPageLang();
    var fromQuery = queryLang();

    /* ?lang= always wins: save preference and jump if needed */
    if (fromQuery) {
      setPreferredLang(fromQuery);
      if (fromQuery !== cur) {
        redirectTo(fromQuery);
        return;
      }
      /* Same language: drop ?lang= from the address bar */
      try {
        var clean = stripLangQuery(location.pathname + location.search + location.hash);
        if (clean !== location.pathname + location.search + location.hash) {
          history.replaceState(null, "", clean);
        }
      } catch (e) {
        /* ignore */
      }
      return;
    }

    /*
     * Saved preference: honor by skipping browser auto-detect (no redirect).
     * Manual switch already navigated the user; preference blocks future locale pushes.
     */
    if (getPreferredLang()) return;

    var browser = detectBrowserLang();
    if (browser !== cur) {
      redirectTo(browser);
    }
  }

  global.MB_LANG_PREF = {
    STORAGE_KEY: STORAGE_KEY,
    SUPPORTED: SUPPORTED,
    getPreferredLang: getPreferredLang,
    setPreferredLang: setPreferredLang,
    detectBrowserLang: detectBrowserLang,
    detectPageLang: detectPageLang,
    localHref: localHref,
    maybeApplyLangRedirect: maybeApplyLangRedirect,
  };

  maybeApplyLangRedirect();
})(typeof window !== "undefined" ? window : this);
