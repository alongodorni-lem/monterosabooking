/* Menu, GDPR cookie banner, reveal animations, hero ready */
(function () {
  "use strict";

  var COOKIE_KEY = "mem_macugnaga_cookie_consent";

  function initCookieBanner() {
    var banner = document.getElementById("cookie-banner");
    if (!banner) return;

    try {
      if (localStorage.getItem(COOKIE_KEY)) return;
    } catch (e) {
      /* ignore */
    }

    banner.classList.add("is-visible");

    var accept = banner.querySelector("[data-cookie-accept]");
    var essential = banner.querySelector("[data-cookie-essential]");

    function save(value) {
      try {
        localStorage.setItem(COOKIE_KEY, value);
      } catch (e) {
        /* ignore */
      }
      banner.classList.remove("is-visible");
    }

    if (accept) accept.addEventListener("click", function () { save("all"); });
    if (essential) essential.addEventListener("click", function () { save("essential"); });
  }

  function initReveal() {
    var nodes = document.querySelectorAll(".reveal");
    if (!nodes.length) return;

    if (!("IntersectionObserver" in window)) {
      nodes.forEach(function (n) { n.classList.add("is-in"); });
      return;
    }

    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    nodes.forEach(function (n) { io.observe(n); });
  }

  function initHero() {
    var hero = document.querySelector(".hero");
    if (!hero) return;
    requestAnimationFrame(function () {
      hero.classList.add("is-ready");
    });
  }

  function boot() {
    initCookieBanner();
    initReveal();
    initHero();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      setTimeout(boot, 0);
    });
  } else {
    setTimeout(boot, 0);
  }
})();
