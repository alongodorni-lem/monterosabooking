/* Home promo popup — delay, dismiss, a11y */
(function () {
  "use strict";

  var STORAGE_KEY = "mb_promo_popup_aug26";
  var DELAY_MS = 3000;
  var script =
    document.currentScript ||
    document.querySelector('script[src*="promo-popup.js"]');

  function cfg(name, fallback) {
    if (!script) return fallback;
    return script.getAttribute("data-" + name) || fallback;
  }

  function alreadySeen() {
    try {
      return sessionStorage.getItem(STORAGE_KEY) === "1";
    } catch (e) {
      return false;
    }
  }

  function markSeen() {
    try {
      sessionStorage.setItem(STORAGE_KEY, "1");
    } catch (e) {
      /* ignore */
    }
  }

  function build() {
    var title = cfg("title", "Natura, relax e montagna.");
    var text = cfg("text", "Il programma dall'1 all'8 agosto.");
    var cta = cfg("cta", "VEDI ATTIVITÀ");
    var href = cfg("href", "esperienze-1-8-agosto-macugnaga.html");
    var img = cfg("img", "assets/web/promo-popup-agosto.jpg");
    var closeLabel = cfg("close", "Chiudi");

    var root = document.createElement("div");
    root.id = "promo-popup";
    root.className = "promo-popup";
    root.setAttribute("hidden", "");
    root.innerHTML =
      '<button type="button" class="promo-popup__backdrop" tabindex="-1" aria-label="' +
      closeLabel +
      '"></button>' +
      '<div class="promo-popup__dialog" role="dialog" aria-modal="true" aria-labelledby="promo-popup-title" aria-describedby="promo-popup-text">' +
      '<button type="button" class="promo-popup__close" aria-label="' +
      closeLabel +
      '">&times;</button>' +
      '<div class="promo-popup__media">' +
      '<img src="' +
      img +
      '" alt="" width="1200" height="675" decoding="async">' +
      "</div>" +
      '<div class="promo-popup__body">' +
      '<p class="promo-popup__title" id="promo-popup-title">' +
      title +
      "</p>" +
      '<p class="promo-popup__text" id="promo-popup-text">' +
      text +
      "</p>" +
      '<a class="promo-popup__cta" href="' +
      href +
      '">' +
      cta +
      "</a>" +
      "</div></div>";

    document.body.appendChild(root);
    return root;
  }

  function init() {
    if (alreadySeen()) return;

    var root = build();
    var dialog = root.querySelector(".promo-popup__dialog");
    var closeBtn = root.querySelector(".promo-popup__close");
    var backdrop = root.querySelector(".promo-popup__backdrop");
    var ctaLink = root.querySelector(".promo-popup__cta");
    var lastFocus = null;
    var opened = false;

    function getFocusable() {
      return dialog.querySelectorAll(
        'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])'
      );
    }

    function open() {
      if (opened || alreadySeen()) return;
      opened = true;
      lastFocus = document.activeElement;
      root.removeAttribute("hidden");
      requestAnimationFrame(function () {
        root.classList.add("is-open");
        closeBtn.focus();
      });
      document.documentElement.style.overflow = "hidden";
    }

    function close() {
      if (!opened) return;
      opened = false;
      markSeen();
      root.classList.remove("is-open");
      document.documentElement.style.overflow = "";
      window.setTimeout(function () {
        root.setAttribute("hidden", "");
      }, 350);
      if (lastFocus && typeof lastFocus.focus === "function") {
        lastFocus.focus();
      }
    }

    closeBtn.addEventListener("click", close);
    backdrop.addEventListener("click", close);
    ctaLink.addEventListener("click", markSeen);

    document.addEventListener("keydown", function (e) {
      if (!opened) return;
      if (e.key === "Escape") {
        e.preventDefault();
        close();
        return;
      }
      if (e.key !== "Tab") return;
      var nodes = getFocusable();
      if (!nodes.length) return;
      var first = nodes[0];
      var last = nodes[nodes.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });

    window.setTimeout(open, DELAY_MS);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
