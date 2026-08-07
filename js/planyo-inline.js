/* Configure Planyo advanced plugin for in-page (non-lightbox) embed.
   Reads resource_id / mode / lang / ppp_refcode from the URL. */
(function () {
  "use strict";

  function getParam(name) {
    var re = new RegExp("[\\?&]" + name.replace(/[\\[]/g, "\\[").replace(/[\\]]/g, "\\]") + "=([^&#]*)");
    var m = re.exec(window.location.href);
    return m ? decodeURIComponent(m[1].replace(/\+/g, " ")) : null;
  }

  function detectPlanyoLang() {
    var fromUrl =
      getParam("planyo_lang") ||
      getParam("lang") ||
      getParam("custom-language");
    if (fromUrl) {
      var u = String(fromUrl).toUpperCase();
      if (u === "IT" || u === "EN" || u === "FR" || u === "DE") return u;
    }
    if (window.MB_I18N) return window.MB_I18N.planyoLang(window.MB_I18N.detectLang());
    var htmlLang = (document.documentElement.lang || "it").slice(0, 2).toLowerCase();
    var map = { it: "IT", en: "EN", fr: "FR", de: "DE" };
    return map[htmlLang] || "IT";
  }

  var resourceId = getParam("resource_id") || "";
  var mode = getParam("mode") || "";
  if (!mode) {
    mode = resourceId ? "reserve" : "resource_list";
  }
  var allowed = {
    reserve: 1,
    resource_desc: 1,
    resource_list: 1,
    search: 1,
    upcoming_availability: 1,
    empty: 1,
    show_cart: 1,
  };
  if (!allowed[mode]) mode = resourceId ? "reserve" : "resource_list";

  var refcode = getParam("ppp_refcode") || "landing";
  var attribParts = ["ppp_refcode=" + refcode];

  /* Preserve search dates when arriving from the site search bar. */
  ["start_date", "end_date", "one_date", "start_time", "end_time", "range_search", "sort"].forEach(
    function (key) {
      var v = getParam(key);
      if (v) attribParts.push(key + "=" + v);
    }
  );

  window.planyo_site_id = "70864";
  window.planyo_default_mode = mode;
  window.planyo_resource_id = resourceId;
  window.planyo_language = detectPlanyoLang();
  window.planyo_attribs = attribParts.join("&");
  window.planyo_resource_ordering = "name";
  window.planyo_include_js_library = true;
  window.ulap_script = "jsonp";
  window.planyo_use_https = true;
  window.planyo_files_location = "https://www.planyo.com/Plugins/PlanyoFiles";
  window.empty_mode = false;
  window.extra_search_fields = "";
  window.sort_fields = "";

  /* booking-utils also checks planyo_embed_mode from URL mode= */
  window.planyo_embed_mode = mode;

  window.get_full_planyo_file_path = function (name) {
    var loc = window.planyo_files_location || "";
    if (!loc.length || loc.charAt(loc.length - 1) === "/") return loc + name;
    return loc + "/" + name;
  };
})();
