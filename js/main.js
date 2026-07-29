/* Menu, GDPR cookie banner, reveal animations, hero ready, Analytics */
(function () {
  "use strict";

  var COOKIE_KEY = "mem_macugnaga_cookie_consent";
  var GA_ID = "G-E5SCQ7QC8L";

  function loadGoogleAnalytics() {
    if (window.__mbGtagLoaded) return;
    window.__mbGtagLoaded = true;

    window.dataLayer = window.dataLayer || [];
    function gtag() {
      window.dataLayer.push(arguments);
    }
    window.gtag = gtag;
    gtag("js", new Date());
    gtag("config", GA_ID);

    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
    document.head.appendChild(s);
  }

  function consentAllowsAnalytics() {
    try {
      return localStorage.getItem(COOKIE_KEY) === "all";
    } catch (e) {
      return false;
    }
  }

  function initCookieBanner() {
    var banner = document.getElementById("cookie-banner");
    if (!banner) {
      if (consentAllowsAnalytics()) loadGoogleAnalytics();
      return;
    }

    try {
      var existing = localStorage.getItem(COOKIE_KEY);
      if (existing) {
        if (existing === "all") loadGoogleAnalytics();
        return;
      }
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
      if (value === "all") loadGoogleAnalytics();
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
