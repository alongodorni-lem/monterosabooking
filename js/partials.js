/* Shared header, footer, Planyo search mount — multilingual */
(function () {
  "use strict";

  function i18n() {
    return window.MB_I18N || null;
  }

  function lang() {
    return i18n() ? i18n().detectLang() : "it";
  }

  function ui() {
    return i18n() ? i18n().t(lang()) : {};
  }

  function prefix() {
    return i18n() ? i18n().assetPrefix(lang()) : "";
  }

  function href(file) {
    return file;
  }

  function currentPage() {
    if (i18n()) return i18n().currentPageFile();
    var path = (location.pathname.split("/").pop() || "index.html").toLowerCase();
    if (!path || path === "") path = "index.html";
    return path;
  }

  function navLink(file, label, page) {
    var cur = page === file ? ' aria-current="page"' : "";
    return '<a href="' + href(file) + '"' + cur + ">" + label + "</a>";
  }

  function languageSwitcher() {
    var L = ui();
    var cur = lang();
    var page = currentPage();
    var codes = [
      { code: "it", label: "IT" },
      { code: "en", label: "EN" },
      { code: "fr", label: "FR" },
      { code: "de", label: "DE" },
    ];
    var options = codes
      .map(function (item) {
        var url = i18n() ? i18n().localHref(item.code, page) : item.code + "/";
        return (
          '<option value="' +
          url +
          '"' +
          (item.code === cur ? " selected" : "") +
          " lang=\"" +
          item.code +
          '">' +
          item.label +
          "</option>"
        );
      })
      .join("");
    return (
      '<div class="lang-switcher">' +
      '<label class="lang-switcher__label" for="lang-switcher-select">' +
      (L.langLabel || "Language") +
      "</label>" +
      '<select id="lang-switcher-select" class="lang-switcher__select" aria-label="' +
      (L.langLabel || "Language") +
      '">' +
      options +
      "</select></div>"
    );
  }

  function renderHeader() {
    var page = currentPage();
    var el = document.getElementById("site-header");
    if (!el) return;
    var L = ui();

    el.innerHTML =
      '<div class="site-header">' +
      '<div class="site-header__top">' +
      '<button type="button" class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="' +
      (L.openMenu || "Open menu") +
      '">' +
      '<span class="nav-toggle__bars" aria-hidden="true">' +
      "<span></span><span></span><span></span>" +
      "</span></button>" +
      languageSwitcher() +
      '<nav class="site-nav" id="site-nav" aria-label="' +
      (L.navLabel || "Main") +
      '">' +
      navLink("index.html", L.home || "Home", page) +
      navLink("esperienze.html", L.experiences || "Experiences", page) +
      navLink("casa-museo-walser.html", L.walser || "Walser", page) +
      navLink("miniera-oro.html", L.mine || "Mine", page) +
      navLink("funivia-seggiovia.html", L.lifts || "Lifts", page) +
      navLink("mappa.html", L.map || "Map", page) +
      navLink("weekend.html", L.weekend || "Weekend", page) +
      navLink("scopri-macugnaga.html", L.discover || "Discover", page) +
      navLink("come-funziona.html", L.howItWorks || "How it works", page) +
      navLink("faq.html", L.faq || "FAQ", page) +
      '<a class="nav-cta" href="esperienze.html">' +
      (L.bookOnline || "Book online") +
      "</a>" +
      "</nav></div></div>";

    initMobileNav();
    initLanguageSwitcher();
  }

  function initLanguageSwitcher() {
    var sel = document.getElementById("lang-switcher-select");
    if (!sel || sel.dataset.langBound === "1") return;
    sel.dataset.langBound = "1";
    sel.addEventListener("change", function () {
      var opt = sel.options[sel.selectedIndex];
      var code = opt && opt.getAttribute("lang");
      if (code) {
        if (window.MB_LANG_PREF && window.MB_LANG_PREF.setPreferredLang) {
          window.MB_LANG_PREF.setPreferredLang(code);
        } else {
          try {
            localStorage.setItem("site_lang", code);
          } catch (e) {
            /* ignore */
          }
        }
      }
      var url = sel.value;
      if (url) location.href = url;
    });
  }

  function initMobileNav() {
    var toggle = document.querySelector(".nav-toggle");
    var nav = document.getElementById("site-nav");
    var L = ui();
    if (!toggle || !nav || toggle.dataset.navBound === "1") return;
    toggle.dataset.navBound = "1";

    function setOpen(open) {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute(
        "aria-label",
        open ? L.closeMenu || "Close menu" : L.openMenu || "Open menu"
      );
    }

    toggle.addEventListener("click", function () {
      setOpen(!nav.classList.contains("is-open"));
    });

    nav.addEventListener("click", function (e) {
      if (e.target && e.target.closest("a")) setOpen(false);
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  function renderTranslationNote() {
    var L = ui();
    if (!L.translationNote || lang() === "it") return;
    var existing = document.querySelector(".translation-note");
    if (existing) existing.remove();
    var wrap = document.createElement("div");
    wrap.className = "translation-note";
    wrap.setAttribute("role", "note");
    wrap.innerHTML =
      '<div class="container"><p>' + L.translationNote + "</p></div>";
    var main = document.getElementById("main") || document.querySelector("main");
    if (main) {
      main.appendChild(wrap);
      return;
    }
    var footerHost = document.getElementById("site-footer");
    if (footerHost && footerHost.parentNode) {
      footerHost.parentNode.insertBefore(wrap, footerHost);
    }
  }

  function renderFooter() {
    var el = document.getElementById("site-footer");
    if (!el) return;
    var L = ui();
    var p = prefix();

    el.innerHTML =
      '<footer class="site-footer">' +
      '<div class="container footer-grid">' +
      '<div class="footer-brand">' +
      '<img class="stemma-mark" src="' +
      p +
      'assets/stemma.png" width="72" height="72" alt="' +
      (L.brandLine || "") +
      '" loading="lazy">' +
      "<div><strong>" +
      (L.brandLine || "") +
      "</strong>" +
      "<p>" +
      (L.fosmit || "") +
      "</p>" +
      "<p>" +
      (L.engineBy || "") +
      '<a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a>' +
      (L.engineFor || "") +
      "</p>" +
      "</div></div>" +
      "<div><h3>" +
      (L.contacts || "Contacts") +
      "</h3><ul>" +
      '<li><a href="mailto:macugnagabooking@gmail.com">macugnagabooking@gmail.com</a></li>' +
      "</ul></div>" +
      "<div><h3>" +
      (L.bookingPortal || "") +
      "</h3><ul>" +
      '<li><a href="esperienze.html">' +
      (L.bookExperiences || "") +
      "</a></li>" +
      '<li><a href="casa-museo-walser.html">' +
      (L.walserFull || "") +
      "</a></li>" +
      '<li><a href="miniera-oro.html">' +
      (L.mine || "") +
      "</a></li>" +
      '<li><a href="funivia-seggiovia.html">' +
      (L.lifts || "") +
      "</a></li>" +
      '<li><a href="mappa.html">' +
      (L.mapExperiences || "") +
      "</a></li>" +
      '<li><a href="come-funziona.html">' +
      (L.howItWorks || "") +
      "</a></li>" +
      "</ul></div>" +
      "<div><h3>" +
      (L.infoPortals || "") +
      "</h3><ul>" +
      '<li><a href="https://macugnaga-monterosa.com/home" target="_blank" rel="noopener">' +
      (L.proloco || "") +
      "</a></li>" +
      '<li><a href="https://macugnagamonterosaski.com/" target="_blank" rel="noopener">' +
      (L.skiLiftsExt || "") +
      "</a></li>" +
      '<li><a href="https://www.comune.macugnaga.vb.it/it-it/home" target="_blank" rel="noopener">' +
      (L.comune || "") +
      "</a></li>" +
      "</ul></div></div>" +
      '<div class="container footer-disclaimer">' +
      "<p>" +
      (L.footerDisclaimer || "") +
      '<a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a>' +
      (L.lemNotResponsible || "") +
      '<a href="credits.html">' +
      (L.credits || "Credits") +
      "</a> · <a href=\"privacy.html\">" +
      (L.privacy || "Privacy") +
      "</a></p>" +
      "</div>" +
      '<div class="container footer-bottom">' +
      "<span>" +
      (L.copyright || "") +
      "</span>" +
      '<span class="footer-bottom__links"><a href="chi-siamo.html">' +
      (L.project || "") +
      '</a> · <a href="privacy.html">' +
      (L.privacy || "") +
      '</a> · <a href="credits.html">' +
      (L.credits || "") +
      "</a></span>" +
      "</div></footer>";
  }

  function renderCookieBanner() {
    var el = document.getElementById("cookie-banner");
    if (!el) return;
    var L = ui();
    el.setAttribute("aria-label", L.cookieAria || "Cookie notice");
    el.innerHTML =
      "<p>" +
      (L.cookieText || "") +
      '<a href="privacy.html">' +
      (L.cookiePrivacy || "Privacy") +
      "</a></p>" +
      '<div class="cookie-banner__actions">' +
      '<button type="button" class="btn btn--primary" data-cookie-accept>' +
      (L.cookieAccept || "Accept") +
      "</button>" +
      '<button type="button" class="btn btn--outline" data-cookie-essential>' +
      (L.cookieEssential || "Essential only") +
      "</button>" +
      "</div>";
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

  function ensureStylesheet(href) {
    if (document.querySelector('link[href="' + href + '"]')) return;
    var link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = href;
    document.head.appendChild(link);
  }

  function applyCalendarStrings(L) {
    document.new_scheme = 1;
    document.first_weekday = 1;
    document.s_prev = L.calPrev;
    document.s_next = L.calNext;
    document.s_today = L.calToday;
    document.s_day = L.calDay;
    document.s_days = L.calDays;
    document.s_week = L.calWeek;
    document.s_weeks = L.calWeeks;
    document.s_weekday = L.calWeekday;
    document.s_month = L.calMonth;
    document.s_single_res = "single resource";
    document.s_weekdays_short = L.weekdaysShort;
    document.s_weekdays_med = L.weekdaysMed;
    document.s_weekdays_long = L.weekdaysLong;
    document.s_months_short = L.monthsShort;
    document.s_months_long = L.monthsLong;
    document.s_all = L.sAll;
    document.s_showall = L.sShowall;
    document.s_areav = L.sAreav;
    document.s_clickres = L.sClickres;
    document.s_partav = L.sPartav;
    document.s_outof = L.sOutof;
    document.s_unav = L.sUnav;
    document.s_noav = L.sNoav;
    document.s_show_more = L.sShowMore;
    document.s_av = L.sAv;
    document.s_vacation = L.sVacation;
    document.s_allday = L.sAllday;
    document.s_day_view = L.sDayView;
    document.s_month_view = L.sMonthView;
    document.s_more = L.sMore;
    if (!document.date_format) document.date_format = "d.m.Y";
  }

  function mountSearchWidget() {
    var mount = document.getElementById("site-search");
    if (!mount) return Promise.resolve();
    var L = ui();
    var pl = i18n() ? i18n().planyoLang(lang()) : "IT";

    ensureStylesheet(
      "https://www.planyo.com/Plugins/PlanyoFiles/bootstrap-planyo.min.css"
    );
    ensureStylesheet(
      "https://www.planyo.com/schemes/?calendar=70864&detect_mobile=auto&sel=scheme_css"
    );
    ensureStylesheet("https://www.planyo.com/li.css");

    return loadScript("https://www.planyo.com/utils.js")
      .then(function () {
        return loadScript("https://www.planyo.com/wrappers.js");
      })
      .then(function () {
        if (typeof planyo_mobile_check === "function" && planyo_mobile_check()) {
          document.is_mobile = 1;
        }
        return loadScript("https://www.planyo.com/li.js?v=3");
      })
      .then(function () {
        mount.innerHTML =
          '<aside class="site-search" aria-label="' +
          (L.searchAria || "Search") +
          '">' +
          '<div class="container">' +
          "<div id='planyo_search_widget' class='planyo horizontal-widget'>" +
          "<style type='text/css'>" +
          ".horizontal-widget .planyo-form-item-group {margin-right:30px;}" +
          ".horizontal-widget .planyo-form-item-group label {margin-right:10px;}" +
          ".horizontal-widget #res_form_buttons {display:inline-block;}" +
          "#search_form label {display:block;float:none;width:100%}" +
          "form#search_form li.planyo_static_help {margin-left:0px;}" +
          "</style>" +
          "<form id='box_search_form' name='search_form' class=' title_above form-inline' action='https://www.planyo.com/booking.php' role='form' target='planyo_li_iframe' onsubmit=\"return planyo_li_on_submit_form()\" method='get'>" +
          "<input type='hidden' value='70864' id='calendar' name='calendar' />" +
          "<input type='hidden' value='flx2' id='range_search' name='range_search' />" +
          "<div style='position:absolute;visibility:hidden;z-index:5000;' class='picker_dropdown ' id='box_start_datecal' onmousedown='var e=arguments[0] || window.event;e.stopPropagation();' onclick='var e=arguments[0] || window.event;e.stopPropagation();'></div>" +
          "<div class='form-group planyo-form-item-group datefld single-col' id='row_box_start_date'>" +
          "<label class='control-label' for='box_start_date'>" +
          (L.startDate || "Start date") +
          "<em>*</em></label>" +
          "<div class='input-group '>" +
          "<input class='with-status-border form-control' type='text' id='box_start_date' name='box_start_date' autocomplete='off' value='' " +
          "onfocus=\"planyo_close_calendar();planyo_show_calendar('box_start_date',null);\" " +
          "onmousedown='var e=arguments[0] || window.event;e.stopPropagation();' " +
          "onclick='var e=arguments[0] || window.event;e.stopPropagation();' />" +
          "<span class='input-group-addon input-group-append' onclick=\"planyo_close_calendar();planyo_show_calendar('box_start_date',null);\">" +
          "<span class='input-group-text'><a class='planyo-cal-icon' href='#' target='_self' onclick=\"planyo_show_calendar('box_start_date',null); return false;\" id='box_start_datecalref'>&#160;</a></span></span>" +
          "</div></div>" +
          "<div style='position:absolute;visibility:hidden;z-index:5000;' class='picker_dropdown ' id='box_end_datecal' onmousedown='var e=arguments[0] || window.event;e.stopPropagation();' onclick='var e=arguments[0] || window.event;e.stopPropagation();'></div>" +
          "<div class='form-group planyo-form-item-group datefld single-col' id='row_box_end_date'>" +
          "<label class='control-label' for='box_end_date'>" +
          (L.endDate || "End date") +
          "<em>*</em></label>" +
          "<div class='input-group '>" +
          "<input class='with-status-border form-control' type='text' id='box_end_date' name='box_end_date' autocomplete='off' value='' " +
          "onfocus=\"planyo_close_calendar();planyo_show_calendar('box_end_date',null);\" " +
          "onmousedown='var e=arguments[0] || window.event;e.stopPropagation();' " +
          "onclick='var e=arguments[0] || window.event;e.stopPropagation();' />" +
          "<span class='input-group-addon input-group-append' onclick=\"planyo_close_calendar();planyo_show_calendar('box_end_date',null);\">" +
          "<span class='input-group-text'><a class='planyo-cal-icon' href='#' target='_self' onclick=\"planyo_show_calendar('box_end_date',null); return false;\" id='box_end_datecalref'>&#160;</a></span></span>" +
          "</div></div>" +
          "<input type='hidden' value='name' id='sort_fields' name='sort_fields' />" +
          "<input type='hidden' value='name' id='sort' name='sort' />" +
          "<input type='hidden' value='15' id='granulation' name='granulation' />" +
          "<input type='hidden' value='search' id='mode' name='mode' />" +
          "<input type='hidden' value='landing' id='ppp_refcode' name='ppp_refcode' />" +
          "<input type='hidden' value='" +
          pl +
          "' id='custom-language' name='custom-language' />" +
          "<input type='hidden' value='1' id='lightbox' name='lightbox' />" +
          "<div id='res_form_buttons'><label for='box_submit_button'>&nbsp;</label>" +
          "<input class='btn btn-primary btn-lg' id='box_submit_button' name='submit_button' type='submit' value='" +
          (L.search || "Search") +
          "' /></div>" +
          "<input type='hidden' value='true' id='submitted_field' name='submitted' />" +
          "</form></div></div></aside>";

        applyCalendarStrings(L);

        if (typeof planyo_set_event === "function") {
          planyo_set_event(
            document.getElementById("box_start_datecal"),
            "click",
            "planyo_dummy",
            false
          );
          planyo_set_event(
            document.getElementById("box_end_datecal"),
            "click",
            "planyo_dummy",
            false
          );
          planyo_set_event(document, "mousedown", "planyo_close_calendar", false);
        }

        window.verify_search_fields =
          "box_start_date:" +
          (L.startDate || "Start date") +
          ",box_end_date:" +
          (L.endDate || "End date");
        window.s_cnbe = L.verifyEmpty || " Cannot be empty";
        return loadScript("https://www.planyo.com/verify-search-fields.js");
      })
      .catch(function (err) {
        console.warn("Planyo search widget:", err);
        mount.innerHTML =
          '<aside class="site-search"><div class="container" style="text-align:center;padding:0.5rem">' +
          '<a class="btn btn--primary" href="esperienze.html">' +
          (L.searchFallback || "Search experiences") +
          "</a></div></aside>";
      });
  }

  function mountAvailabilityBar() {
    var search = document.getElementById("site-search");
    if (!search) return Promise.resolve();
    var p = prefix();

    var existing = document.getElementById("availability-bar");
    if (!existing) {
      var bar = document.createElement("div");
      bar.id = "availability-bar";
      bar.className = "availability-bar";
      bar.hidden = true;
      bar.setAttribute("aria-live", "polite");
      search.insertAdjacentElement("afterend", bar);
    }

    return loadScript(p + "js/planyo-config.js")
      .catch(function () {
        /* missing config: bar stays hidden */
      })
      .then(function () {
        return loadScript(p + "js/availability-bar.js?v=9");
      })
      .catch(function () {
        /* quiet fail */
      });
  }

  function localizeSkipLink() {
    var skip = document.querySelector("a.skip-link");
    if (skip) skip.textContent = ui().skip || skip.textContent;
  }

  localizeSkipLink();
  renderHeader();
  renderTranslationNote();
  renderFooter();
  renderCookieBanner();
  mountSearchWidget().then(function () {
    return mountAvailabilityBar();
  });
})();
