/* Operator embed widget generator — client-side only */
(function () {
  "use strict";

  var form = document.getElementById("embed-widget-form");
  if (!form) return;

  var nameInput = document.getElementById("embed-site-name");
  var errorEl = document.getElementById("embed-widget-error");
  var resultEl = document.getElementById("embed-widget-result");
  var refEl = document.getElementById("embed-refcode");
  var codeEl = document.getElementById("embed-widget-code");
  var copyBtn = document.getElementById("embed-copy-btn");
  var feedbackEl = document.getElementById("embed-copy-feedback");

  var MSG = {
    it: {
      empty: "Inserisci il nome del sito o della struttura (max 15 caratteri).",
      invalid: "Usa solo lettere, numeri, trattino o underscore (senza spazi).",
      loadError: "Impossibile caricare il template del widget. Riprova più tardi.",
      copied: "Codice copiato negli appunti.",
      copyFail: "Impossibile copiare automaticamente. Seleziona il codice e copialo manualmente.",
    },
    en: {
      empty: "Enter the site or property name (max 15 characters).",
      invalid: "Use only letters, numbers, hyphen or underscore (no spaces).",
      loadError: "Could not load the widget template. Please try again later.",
      copied: "Code copied to clipboard.",
      copyFail: "Could not copy automatically. Select the code and copy it manually.",
    },
    fr: {
      empty: "Saisissez le nom du site ou de la structure (max 15 caractères).",
      invalid: "Utilisez uniquement lettres, chiffres, tiret ou underscore (sans espaces).",
      loadError: "Impossible de charger le modèle du widget. Réessayez plus tard.",
      copied: "Code copié dans le presse-papiers.",
      copyFail: "Copie automatique impossible. Sélectionnez le code et copiez-le manuellement.",
    },
    de: {
      empty: "Geben Sie den Namen der Website oder Unterkunft ein (max. 15 Zeichen).",
      invalid: "Nur Buchstaben, Zahlen, Bindestrich oder Unterstrich (ohne Leerzeichen).",
      loadError: "Widget-Vorlage konnte nicht geladen werden. Bitte später erneut versuchen.",
      copied: "Code in die Zwischenablage kopiert.",
      copyFail: "Automatisches Kopieren fehlgeschlagen. Code markieren und manuell kopieren.",
    },
  };

  var templateCache = null;
  var templatePromise = null;

  function lang() {
    if (window.MB_I18N) return window.MB_I18N.detectLang();
    return "it";
  }

  function t() {
    return MSG[lang()] || MSG.it;
  }

  function assetPrefix() {
    if (window.MB_I18N) return window.MB_I18N.assetPrefix(lang());
    return "";
  }

  function showError(msg) {
    if (!errorEl) return;
    errorEl.textContent = msg || "";
    errorEl.hidden = !msg;
  }

  function showFeedback(msg) {
    if (!feedbackEl) return;
    feedbackEl.textContent = msg || "";
    feedbackEl.hidden = !msg;
  }

  /** Spaces removed, then keep safe URL/refcode chars only. */
  function sanitizeRefcode(raw) {
    var noSpaces = String(raw || "").replace(/\s+/g, "");
    return noSpaces.replace(/[^a-zA-Z0-9_-]/g, "");
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
        templateCache = text;
        return text;
      })
      .catch(function (err) {
        templatePromise = null;
        throw err;
      });
    return templatePromise;
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      codeEl.focus();
      codeEl.select();
      try {
        var ok = document.execCommand("copy");
        if (ok) resolve();
        else reject(new Error("execCommand failed"));
      } catch (e) {
        reject(e);
      }
    });
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    showError("");
    showFeedback("");

    var refcode = sanitizeRefcode(nameInput.value);
    if (!String(nameInput.value || "").trim()) {
      showError(t().empty);
      resultEl.hidden = true;
      nameInput.focus();
      return;
    }
    if (!refcode) {
      showError(t().invalid);
      resultEl.hidden = true;
      nameInput.focus();
      return;
    }
    if (refcode.length > 15) {
      refcode = refcode.slice(0, 15);
    }

    loadTemplate()
      .then(function (tpl) {
        var html = injectRefcode(tpl, refcode);
        refEl.textContent = refcode;
        codeEl.value = html;
        resultEl.hidden = false;
        codeEl.focus();
        codeEl.select();
      })
      .catch(function () {
        showError(t().loadError);
        resultEl.hidden = true;
      });
  });

  if (copyBtn) {
    copyBtn.addEventListener("click", function () {
      var text = codeEl.value || "";
      if (!text) return;
      copyText(text)
        .then(function () {
          showFeedback(t().copied);
        })
        .catch(function () {
          showFeedback(t().copyFail);
          codeEl.focus();
          codeEl.select();
        });
    });
  }
})();
