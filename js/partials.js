/* Shared header, footer, Planyo search mount */
(function () {
  "use strict";

  function currentPage() {
    var path = (location.pathname.split("/").pop() || "index.html").toLowerCase();
    if (!path || path === "") path = "index.html";
    return path;
  }

  function navLink(href, label, page) {
    var cur = page === href ? ' aria-current="page"' : "";
    return '<a href="' + href + '"' + cur + ">" + label + "</a>";
  }

  function renderHeader() {
    var page = currentPage();
    var el = document.getElementById("site-header");
    if (!el) return;

    el.innerHTML =
      '<div class="site-header">' +
      '<div class="site-header__top">' +
      '<button type="button" class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Apri menu">' +
      '<span class="nav-toggle__bars" aria-hidden="true">' +
      "<span></span><span></span><span></span>" +
      "</span></button>" +
      '<nav class="site-nav" id="site-nav" aria-label="Principale">' +
      navLink("index.html", "Home", page) +
      navLink("esperienze.html", "Esperienze", page) +
      navLink("casa-museo-walser.html", "Casa Walser", page) +
      navLink("miniera-oro.html", "Miniera d’oro", page) +
      navLink("funivia-seggiovia.html", "Impianti", page) +
      navLink("mappa.html", "Mappa", page) +
      navLink("weekend.html", "Weekend", page) +
      navLink("scopri-macugnaga.html", "Scopri Macugnaga", page) +
      navLink("come-funziona.html", "Come funziona", page) +
      navLink("faq.html", "FAQ", page) +
      '<a class="nav-cta" href="esperienze.html">Prenota online</a>' +
      "</nav></div></div>";

    initMobileNav();
  }

  function initMobileNav() {
    var toggle = document.querySelector(".nav-toggle");
    var nav = document.getElementById("site-nav");
    if (!toggle || !nav || toggle.dataset.navBound === "1") return;
    toggle.dataset.navBound = "1";

    function setOpen(open) {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Chiudi menu" : "Apri menu");
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

  function renderFooter() {
    var el = document.getElementById("site-footer");
    if (!el) return;

    el.innerHTML =
      '<footer class="site-footer">' +
      '<div class="container footer-grid">' +
      '<div class="footer-brand">' +
      '<img src="assets/stemma.png" width="64" height="64" alt="Stemma Unione Montana Valli dell\'Ossola">' +
      "<div><strong>Unione Montana Valli dell'Ossola</strong>" +
      "<p>FOSMIT · Fondo Sviluppo Montagne Italiane — Regione Piemonte</p>" +
      '<p>Booking engine sviluppato da <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> per Unione Montana Valli dell\'Ossola e operatori locali.</p>' +
      "</div></div>" +
      "<div><h3>Contatti</h3><ul>" +
      '<li><a href="mailto:macugnagabooking@gmail.com">macugnagabooking@gmail.com</a></li>' +
      "<li>P.I. IT02380720033</li>" +
      "</ul></div>" +
      "<div><h3>Portale di prenotazione</h3><ul>" +
      '<li><a href="esperienze.html">Prenota esperienze</a></li>' +
      '<li><a href="casa-museo-walser.html">Casa Museo Walser</a></li>' +
      '<li><a href="miniera-oro.html">Miniera d’oro</a></li>' +
      '<li><a href="funivia-seggiovia.html">Impianti</a></li>' +
      '<li><a href="mappa.html">Mappa esperienze</a></li>' +
      '<li><a href="come-funziona.html">Come funziona</a></li>' +
      "</ul></div>" +
      "<div><h3>Portali di informazione</h3><ul>" +
      '<li><a href="https://macugnaga-monterosa.com/home" target="_blank" rel="noopener">Associazione Turistica Pro Loco Macugnaga (info, eventi e ricettività)</a></li>' +
      '<li><a href="https://macugnagamonterosaski.com/" target="_blank" rel="noopener">Impianti di risalita</a></li>' +
      '<li><a href="https://www.comune.macugnaga.vb.it/it-it/home" target="_blank" rel="noopener">Comune di Macugnaga</a></li>' +
      "</ul></div></div>" +
      '<div class="container footer-disclaimer">' +
      "<p>Informazioni, prezzi e disponibilità riportati dal portale di prenotazione sono indicati dai gestori delle esperienze. Con la prenotazione online riceverai i contatti diretti degli organizzatori, da contattare per ogni ulteriore informazione. " +
      '<a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> non è in alcun modo responsabile della gestione delle attività. ' +
      '<a href="credits.html">Credits</a> · <a href="privacy.html">Privacy</a></p>' +
      "</div>" +
      '<div class="container footer-bottom">' +
      "<span>© Mountain Experience Monterosa Macugnaga</span>" +
      '<span><a href="privacy.html">Privacy</a> · <a href="credits.html">Credits</a></span>' +
      "</div></footer>";
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

  function mountSearchWidget() {
    var mount = document.getElementById("site-search");
    if (!mount) return Promise.resolve();

    ensureStylesheet("https://www.planyo.com/Plugins/PlanyoFiles/bootstrap-planyo.min.css");
    ensureStylesheet("https://www.planyo.com/schemes/?calendar=70864&detect_mobile=auto&sel=scheme_css");
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
          '<aside class="site-search" aria-label="Cerca esperienze">' +
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
          "<label class='control-label' for='box_start_date'>Data di inizio<em>*</em></label>" +
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
          "<label class='control-label' for='box_end_date'>Data di fine<em>*</em></label>" +
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
          "<input type='hidden' value='IT' id='custom-language' name='custom-language' />" +
          "<input type='hidden' value='1' id='lightbox' name='lightbox' />" +
          "<div id='res_form_buttons'><label for='box_submit_button'>&nbsp;</label>" +
          "<input class='btn btn-primary btn-lg' id='box_submit_button' name='submit_button' type='submit' value='Cerca' /></div>" +
          "<input type='hidden' value='true' id='submitted_field' name='submitted' />" +
          "</form></div></div></aside>";

        document.new_scheme = 1;
        document.first_weekday = 1;
        document.s_prev = "precedente";
        document.s_next = "successivo";
        document.s_today = "oggi";
        document.s_day = "giorno";
        document.s_days = "giorni";
        document.s_week = "settimana";
        document.s_weeks = "settimane";
        document.s_weekday = "giorno della settimana";
        document.s_month = "mese";
        document.s_single_res = "single resource";
        document.s_weekdays_short = ["L", "M", "M", "G", "V", "S", "D"];
        document.s_weekdays_med = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"];
        document.s_weekdays_long = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"];
        document.s_months_short = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"];
        document.s_months_long = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"];
        document.s_all = "Tutti";
        document.s_showall = "Mostra tutto";
        document.s_areav = "sono disponibili.";
        document.s_clickres = "Clicca qui per prenotare.";
        document.s_partav = "Disponibile solo per parte del giorno. Clicca sulla data per i dettagli.";
        document.s_outof = "su";
        document.s_unav = "Non disponibile";
        document.s_noav = "Non disponibile";
        document.s_show_more = "mostrare di più";
        document.s_av = "Disponibile";
        document.s_vacation = "Ferie";
        document.s_allday = "Giorno intero";
        document.s_day_view = "giorno";
        document.s_month_view = "mese";
        document.s_more = "più";
        if (!document.date_format) document.date_format = "d.m.Y";

        if (typeof planyo_set_event === "function") {
          planyo_set_event(document.getElementById("box_start_datecal"), "click", "planyo_dummy", false);
          planyo_set_event(document.getElementById("box_end_datecal"), "click", "planyo_dummy", false);
          planyo_set_event(document, "mousedown", "planyo_close_calendar", false);
        }

        window.verify_search_fields = "box_start_date:Data di inizio,box_end_date:Data di fine";
        window.s_cnbe = " Non può essere vuoto";
        return loadScript("https://www.planyo.com/verify-search-fields.js");
      })
      .catch(function (err) {
        console.warn("Planyo search widget:", err);
        mount.innerHTML =
          '<aside class="site-search"><div class="container" style="text-align:center;padding:0.5rem">' +
          '<a class="btn btn--primary" href="esperienze.html">Cerca e prenota esperienze</a></div></aside>';
      });
  }

  function mountAvailabilityBar() {
    var search = document.getElementById("site-search");
    if (!search) return Promise.resolve();

    var existing = document.getElementById("availability-bar");
    if (!existing) {
      var bar = document.createElement("div");
      bar.id = "availability-bar";
      bar.className = "availability-bar";
      bar.hidden = true;
      bar.setAttribute("aria-live", "polite");
      search.insertAdjacentElement("afterend", bar);
    }

    return loadScript("js/planyo-config.js")
      .catch(function () {
        /* missing config: bar stays hidden */
      })
      .then(function () {
        return loadScript("js/availability-bar.js");
      })
      .catch(function () {
        /* quiet fail */
      });
  }

  renderHeader();
  renderFooter();
  mountSearchWidget().then(function () {
    return mountAvailabilityBar();
  });
})();
