/* Operator embed tools: direct link + HTML widget — client-side only */
(function () {
  "use strict";

  var REFCODE_MAX = 30;
  var BOOKING_BASE =
    "https://www.planyo.com/booking.php?calendar=70864&custom-language=LANG&attribute_string=%26mode%3Dresource_list%26lang%3DLANG%26sort%3Dname";

  var MSG = {
    it: {
      empty: "Inserisci il tuo sito internet (es. www.miosito.it).",
      invalid: "Usa lettere, numeri, punto, trattino o underscore (senza spazi).",
      loadError: "Impossibile caricare il template del widget. Riprova più tardi.",
      copiedCode: "Codice copiato negli appunti.",
      copiedLink: "Link copiato negli appunti.",
      copyFail: "Impossibile copiare automaticamente. Seleziona il testo e copialo manualmente.",
    },
    en: {
      empty: "Enter your website (e.g. www.mysite.com).",
      invalid: "Use letters, numbers, dots, hyphen or underscore (no spaces).",
      loadError: "Could not load the widget template. Please try again later.",
      copiedCode: "Code copied to clipboard.",
      copiedLink: "Link copied to clipboard.",
      copyFail: "Could not copy automatically. Select the text and copy it manually.",
    },
    fr: {
      empty: "Saisissez votre site internet (ex. www.monsite.fr).",
      invalid: "Utilisez lettres, chiffres, point, tiret ou underscore (sans espaces).",
      loadError: "Impossible de charger le modèle du widget. Réessayez plus tard.",
      copiedCode: "Code copié dans le presse-papiers.",
      copiedLink: "Lien copié dans le presse-papiers.",
      copyFail: "Copie automatique impossible. Sélectionnez le texte et copiez-le manuellement.",
    },
    de: {
      empty: "Geben Sie Ihre Website ein (z. B. www.meinerseite.de).",
      invalid: "Nur Buchstaben, Zahlen, Punkt, Bindestrich oder Unterstrich (ohne Leerzeichen).",
      loadError: "Widget-Vorlage konnte nicht geladen werden. Bitte später erneut versuchen.",
      copiedCode: "Code in die Zwischenablage kopiert.",
      copiedLink: "Link in die Zwischenablage kopiert.",
      copyFail: "Automatisches Kopieren fehlgeschlagen. Text markieren und manuell kopieren.",
    },
  };

  /* Fallback if assets/widget_per_altri_siti.txt is unavailable (404 / offline). */
  var FALLBACK_TEMPLATE =
    "<script type=\"text/javascript\">\n" +
    "/* change the following values to match your settings */\n" +
    "var planyo_site_id='70864'; /* ID of your planyo site */\n" +
    "var planyo_default_mode='resource_list'; /* one of: 'resource_list' (displays list of resources with photos, descriptions etc.), 'search' (displays the search box), 'empty' (will not display anything by default but will require you to either pass the resource ID as parameter in the URL (resource_id) or add an external search box or calendar preview), 'upcoming_availability' (displays a quick list of all upcoming availability) */\n" +
    "var extra_search_fields=''; /* comma-separated extra fields in the search box, e.g. 'Number of persons'. You first need to define them in settings/custom resource properties */\n" +
    "var sort_fields=''; /* comma-separated sort fields for the search box -- a single field will hide the sort dropdown box */\n" +
    "var planyo_resource_ordering='name'; /* optional sort criterium for resource list */\n" +
    "var planyo_include_js_library=true; /* set this to true if jQuery (required) should be included by this plugin, or false if your website already includes jQuery */\n" +
    "var planyo_attribs=''; /* optionally you can insert the attribute string here */\n" +
    "var planyo_resource_id=''; /* optional: ID of the resource being reserved */\n" +
    "var planyo_language='IT'; /* you can optionally change the language here, e.g. 'FR' or 'ES' or pass the languge in the 'lang' parameter. 'AUTO' means the language is detected automatically */\n" +
    "var ulap_script=\"jsonp\"; /* leave this as \"jsonp\" for a plain-javascript implementation --OR-- if using a php/asp.net/java implementation, one of the ULAP scripts: \"ulap.php\", \"ulap.aspx\", \"ulap.jsp\", in such case you must download the advanced integration Planyo files from http://www.planyo.com/Plugins/PlanyoFiles/planyo-files.zip */\n" +
    "var planyo_use_https=true;\n" +
    "var planyo_files_location='https://www.planyo.com/Plugins/PlanyoFiles'; /* relative or absolute directory where the planyo files are kept (leave unchanged for plain-javascript implementation, otherwise e.g. '/planyo-files' when using the ULAP scripts) */\n" +
    "var empty_mode=false; /* should be always set to false */\n" +
    "</script>\n" +
    "\n" +
    "<script type=\"text/javascript\">\n" +
    "function get_param (name) {name = name.replace(/[\\[]/,\"\\\\\\[\").replace(/[\\]]/,\"\\\\\\]\");var regexS = \"[\\\\?&]\"+name+\"=([^&#]*)\";var regex = new RegExp (regexS);var results = regex.exec (window.location.href);if (results == null) return null;else  return results[1];}\n" +
    "if (get_param('mode'))planyo_embed_mode = get_param('mode');\n" +
    "function get_full_planyo_file_path(name) {if(planyo_files_location.length==0||planyo_files_location.lastIndexOf('/')==planyo_files_location.length-1)return planyo_files_location+name; else return planyo_files_location+'/'+name;}\n" +
    "</script>\n" +
    "<link rel='stylesheet' href='https://www.planyo.com/schemes/?calendar=70864&detect_mobile=auto&sel=scheme_css' type='text/css' />\n" +
    "<div id='planyo_content' class='planyo'><img src='https://www.planyo.com/images/hourglass.gif' align='middle' /></div>\n" +
    "<script type='text/javascript' src='https://www.planyo.com/Plugins/PlanyoFiles/jquery-3.6.4.min.js'></script>\n" +
    "<script src='https://www.planyo.com/Plugins/PlanyoFiles/booking-utils.js' type='text/javascript'></script>\n" +
    "<noscript><a href='https://www.planyo.com/about-calendar.php?calendar=70864'>Make a reservation</a><br/><br/><a href='https://www.planyo.com/'>Reservation system powered by Planyo</a></noscript>\n";

  var templateCache = null;
  var templatePromise = null;

  function lang() {
    if (window.MB_I18N) return window.MB_I18N.detectLang();
    return "it";
  }

  function bookingLang() {
    var l = lang();
    if (l === "en" || l === "fr" || l === "de") return l.toUpperCase();
    return "IT";
  }

  function t() {
    return MSG[lang()] || MSG.it;
  }

  function assetPrefix() {
    if (window.MB_I18N) return window.MB_I18N.assetPrefix(lang());
    var path = window.location.pathname || "";
    if (/\/(en|fr|de)(\/|$)/.test(path)) return "../";
    return "";
  }

  function setAlert(el, msg) {
    if (!el) return;
    el.textContent = msg || "";
    el.hidden = !msg;
  }

  /**
   * Build a Planyo-safe refcode from a typed website name.
   * Strips protocol/path/spaces; keeps letters, digits, dot, hyphen, underscore.
   */
  function sanitizeRefcode(raw) {
    var s = String(raw || "").trim();
    s = s.replace(/^https?:\/\//i, "");
    s = s.replace(/^www\./i, "www.");
    s = s.split(/[/?#]/)[0];
    s = s.replace(/\s+/g, "");
    s = s.replace(/[^a-zA-Z0-9._-]/g, "");
    if (s.length > REFCODE_MAX) s = s.slice(0, REFCODE_MAX);
    return s;
  }

  function parseSiteInput(inputEl) {
    var raw = String((inputEl && inputEl.value) || "");
    if (!raw.trim()) {
      return { ok: false, error: t().empty };
    }
    var refcode = sanitizeRefcode(raw);
    if (!refcode) {
      return { ok: false, error: t().invalid };
    }
    return { ok: true, refcode: refcode };
  }

  function buildDirectLink(refcode) {
    var L = bookingLang();
    var url = BOOKING_BASE.replace(/LANG/g, L);
    return url + "&ppp_refcode=" + encodeURIComponent(refcode);
  }

  function injectRefcode(template, refcode) {
    var attribs = "ppp_refcode=" + refcode;
    var next = template.replace(
      /var\s+planyo_attribs\s*=\s*'[^']*'\s*;/,
      "var planyo_attribs='" + attribs + "';"
    );
    if (next === template) {
      next = template.replace(
        /var\s+planyo_attribs\s*=\s*""\s*;/,
        'var planyo_attribs="' + attribs + '";'
      );
    }
    return next;
  }

  function loadTemplate() {
    if (templateCache) return Promise.resolve(templateCache);
    if (templatePromise) return templatePromise;
    var url = assetPrefix() + "assets/widget_per_altri_siti.txt";
    templatePromise = fetch(url, { credentials: "same-origin" })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.text();
      })
      .then(function (text) {
        if (!text || text.indexOf("planyo_site_id") === -1) {
          throw new Error("Invalid template");
        }
        templateCache = text;
        return text;
      })
      .catch(function () {
        templateCache = FALLBACK_TEMPLATE;
        templatePromise = null;
        return templateCache;
      });
    return templatePromise;
  }

  function copyText(text, selectEl) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      if (!selectEl) {
        reject(new Error("no select target"));
        return;
      }
      selectEl.focus();
      if (selectEl.select) selectEl.select();
      try {
        var ok = document.execCommand("copy");
        if (ok) resolve();
        else reject(new Error("execCommand failed"));
      } catch (e) {
        reject(e);
      }
    });
  }

  /* ——— Method 1: direct link ——— */
  var linkForm = document.getElementById("embed-link-form");
  if (linkForm) {
    var linkInput = document.getElementById("embed-link-site");
    var linkError = document.getElementById("embed-link-error");
    var linkResult = document.getElementById("embed-link-result");
    var linkUrlEl = document.getElementById("embed-link-url");
    var linkCopyBtn = document.getElementById("embed-link-copy-btn");
    var linkFeedback = document.getElementById("embed-link-feedback");

    linkForm.addEventListener("submit", function (e) {
      e.preventDefault();
      setAlert(linkError, "");
      setAlert(linkFeedback, "");

      var parsed = parseSiteInput(linkInput);
      if (!parsed.ok) {
        setAlert(linkError, parsed.error);
        if (linkResult) linkResult.hidden = true;
        if (linkInput) linkInput.focus();
        return;
      }

      var url = buildDirectLink(parsed.refcode);
      if (linkUrlEl) {
        linkUrlEl.value = url;
      }
      if (linkResult) linkResult.hidden = false;
      if (linkUrlEl) {
        linkUrlEl.focus();
        linkUrlEl.select();
      }
    });

    if (linkCopyBtn) {
      linkCopyBtn.addEventListener("click", function () {
        var text = (linkUrlEl && linkUrlEl.value) || "";
        if (!text) return;
        copyText(text, linkUrlEl)
          .then(function () {
            setAlert(linkFeedback, t().copiedLink);
          })
          .catch(function () {
            setAlert(linkFeedback, t().copyFail);
            if (linkUrlEl) {
              linkUrlEl.focus();
              linkUrlEl.select();
            }
          });
      });
    }
  }

  /* ——— Method 2: HTML embed ——— */
  var form = document.getElementById("embed-widget-form");
  if (!form) return;

  var nameInput = document.getElementById("embed-site-name");
  var errorEl = document.getElementById("embed-widget-error");
  var resultEl = document.getElementById("embed-widget-result");
  var refEl = document.getElementById("embed-refcode");
  var codeEl = document.getElementById("embed-widget-code");
  var copyBtn = document.getElementById("embed-copy-btn");
  var feedbackEl = document.getElementById("embed-copy-feedback");

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    setAlert(errorEl, "");
    setAlert(feedbackEl, "");

    var parsed = parseSiteInput(nameInput);
    if (!parsed.ok) {
      setAlert(errorEl, parsed.error);
      if (resultEl) resultEl.hidden = true;
      if (nameInput) nameInput.focus();
      return;
    }

    loadTemplate()
      .then(function (tpl) {
        var html = injectRefcode(tpl, parsed.refcode);
        if (refEl) refEl.textContent = parsed.refcode;
        if (codeEl) codeEl.value = html;
        if (resultEl) resultEl.hidden = false;
        if (codeEl) {
          codeEl.focus();
          codeEl.select();
        }
      })
      .catch(function () {
        setAlert(errorEl, t().loadError);
        if (resultEl) resultEl.hidden = true;
      });
  });

  if (copyBtn) {
    copyBtn.addEventListener("click", function () {
      var text = (codeEl && codeEl.value) || "";
      if (!text) return;
      copyText(text, codeEl)
        .then(function () {
          setAlert(feedbackEl, t().copiedCode);
        })
        .catch(function () {
          setAlert(feedbackEl, t().copyFail);
          if (codeEl) {
            codeEl.focus();
            codeEl.select();
          }
        });
    });
  }
})();
