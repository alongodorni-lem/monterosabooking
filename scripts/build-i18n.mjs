/**
 * Build EN/FR/DE mirrors of Italian HTML pages + patch IT hreflang.
 * Usage: node scripts/build-i18n.mjs
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { PHRASES, PAGE_META, NAV_SEO } from "./i18n-dict.mjs";
import { PHRASES_MORE } from "./i18n-dict-more.mjs";
import { PHRASES_BODIES } from "./i18n-dict-bodies.mjs";
import { PHRASES_BODIES_2 } from "./i18n-dict-bodies2.mjs";

const ALL_PHRASES = Object.assign({}, PHRASES, PHRASES_MORE, PHRASES_BODIES, PHRASES_BODIES_2);

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const SITE = "https://www.macugnagabooking.it";
const LANGS = ["en", "fr", "de"];
const OG_LOCALE = { en: "en_GB", fr: "fr_FR", de: "de_DE", it: "it_IT" };
const TRANSLATION_NOTE = {
  en: "Traduzione automatica dalla versione ufficiale in lingua italiana",
  fr: "Traduzione automatica dalla versione ufficiale in lingua italiana",
  de: "Traduzione automatica dalla versione ufficiale in lingua italiana",
};

const PAGES = fs
  .readdirSync(ROOT)
  .filter((f) => f.endsWith(".html"))
  .sort();

function absUrl(lang, file) {
  if (file === "index.html") {
    return lang === "it" ? `${SITE}/` : `${SITE}/${lang}/`;
  }
  return lang === "it" ? `${SITE}/${file}` : `${SITE}/${lang}/${file}`;
}

function hreflangBlock(file) {
  const lines = [
    `<link rel="alternate" hreflang="it" href="${absUrl("it", file)}">`,
    `<link rel="alternate" hreflang="en" href="${absUrl("en", file)}">`,
    `<link rel="alternate" hreflang="fr" href="${absUrl("fr", file)}">`,
    `<link rel="alternate" hreflang="de" href="${absUrl("de", file)}">`,
    `<link rel="alternate" hreflang="x-default" href="${absUrl("it", file)}">`,
  ];
  return lines.join("\n  ");
}

function fixRelativePaths(html) {
  return html
    .replace(/(href|src)=(")(?!https?:|mailto:|#|\/\/)(assets\/|css\/|js\/)/g, "$1=$2../$3")
    .replace(
      /(srcset=["'])([^"']+)/g,
      (_, attr, value) =>
        attr +
        value.replace(/(^|,\s*)(assets\/)/g, (_, sep) => `${sep}../assets/`)
    );
}

function applyPhrases(html, lang) {
  const pairs = Object.keys(ALL_PHRASES)
    .map((it) => ({ it, to: ALL_PHRASES[it][lang] }))
    .filter((p) => p.to && p.to !== p.it)
    .sort((a, b) => b.it.length - a.it.length);

  let out = html;
  for (const { it, to } of pairs) {
    if (!it) continue;
    out = out.split(it).join(to);
  }
  return out;
}

function seoNav(lang) {
  const n = NAV_SEO[lang];
  return `  <nav class="seo-nav-fallback" aria-label="${n.aria}">
        <a href="index.html">${n.home}</a>
        <a href="esperienze.html">${n.experiences}</a>
        <a href="casa-museo-walser.html">${n.walser}</a>
        <a href="miniera-oro.html">${n.mine}</a>
        <a href="funivia-seggiovia.html">${n.lifts}</a>
        <a href="mappa.html">${n.map}</a>
        <a href="weekend.html">${n.weekend}</a>
        <a href="scopri-macugnaga.html">${n.discover}</a>
        <a href="come-funziona.html">${n.how}</a>
        <a href="faq.html">${n.faq}</a>
        <a class="nav-cta" href="esperienze.html">${n.cta}</a>
  </nav>`;
}

function injectScripts(html, lang) {
  const prefix = lang === "it" ? "" : "../";
  let out = html;
  out = out.replace(
    /<script src="(\.\.\/)?js\/i18n\.js\?v=\d+"><\/script>\s*/g,
    ""
  );
  out = out.replace(
    /<script src="(\.\.\/)?js\/partials\.js\?v=\d+"><\/script>/g,
    `<script src="${prefix}js/i18n.js?v=2"></script>\n  <script src="${prefix}js/partials.js?v=9"></script>`
  );
  out = out.replace(
    /(\.\.\/)?js\/esperienze-list\.js\?v=\d+/g,
    `${prefix}js/esperienze-list.js?v=9`
  );
  out = out.replace(/(\.\.\/)?js\/main\.js/g, `${prefix}js/main.js`);
  out = out.replace(/(\.\.\/)?css\/style\.css\?v=\d+/g, `${prefix}css/style.css?v=10`);
  return out;
}

function setMeta(html, lang, file) {
  const meta = (PAGE_META[file] && PAGE_META[file][lang]) || null;
  let out = html;
  out = out.replace(/<html lang="it">/, `<html lang="${lang}">`);
  out = out.replace(
    /<link rel="canonical" href="[^"]*">/,
    `<link rel="canonical" href="${absUrl(lang, file)}">`
  );
  out = out.replace(
    /property="og:url" content="[^"]*"/,
    `property="og:url" content="${absUrl(lang, file)}"`
  );
  out = out.replace(
    /property="og:locale" content="[^"]*"/,
    `property="og:locale" content="${OG_LOCALE[lang]}"`
  );
  out = out.replace(
    /name="twitter:url" content="[^"]*"/,
    `name="twitter:url" content="${absUrl(lang, file)}"`
  );

  if (meta) {
    if (meta.title) {
      out = out.replace(/<title>[^<]*<\/title>/, `<title>${meta.title}</title>`);
      out = out.replace(
        /property="og:title" content="[^"]*"/,
        `property="og:title" content="${meta.ogTitle || meta.title}"`
      );
      out = out.replace(
        /name="twitter:title" content="[^"]*"/,
        `name="twitter:title" content="${meta.title}"`
      );
    }
    if (meta.description) {
      out = out.replace(
        /name="description" content="[^"]*"/,
        `name="description" content="${meta.description}"`
      );
      out = out.replace(
        /property="og:description" content="[^"]*"/,
        `property="og:description" content="${meta.ogDescription || meta.description}"`
      );
      out = out.replace(
        /name="twitter:description" content="[^"]*"/,
        `name="twitter:description" content="${meta.ogDescription || meta.description}"`
      );
    }
  }

  /* Rewrite absolute IT URLs only inside JSON-LD blocks (not hreflang/canonical) */
  out = out.replace(
    /(<script type="application\/ld\+json">)([\s\S]*?)(<\/script>)/gi,
    (_, open, body, close) => {
      let b = body.replace(
        new RegExp(
          `${SITE.replace(/\./g, "\\.")}/(?!en/|fr/|de/)([a-z0-9.-]+\\.html)`,
          "g"
        ),
        (_, page) => absUrl(lang, page)
      );
      b = b.replace(
        new RegExp(`${SITE.replace(/\./g, "\\.")}/(?=["#])`, "g"),
        absUrl(lang, "index.html")
      );
      /* also bare trailing slash URLs in JSON */
      b = b.replace(
        new RegExp(`"${SITE.replace(/\./g, "\\.")}/"`, "g"),
        `"${absUrl(lang, "index.html")}"`
      );
      return open + b + close;
    }
  );

  /* Map iframe lang */
  out = out.replace(
    /embed-map\.php\?([^"']*?)lang=IT/g,
    `embed-map.php?$1lang=${lang.toUpperCase()}`
  );

  /* hreflang last so URL rewrites never touch them */
  out = out.replace(/\n?\s*<link rel="alternate" hreflang="[^"]+" href="[^"]*">/g, "");
  out = out.replace(
    /(<link rel="canonical"[^>]*>)/,
    `$1\n  ${hreflangBlock(file)}`
  );

  return out;
}

function replaceSeoNav(html, lang) {
  return html.replace(
    /<nav class="seo-nav-fallback"[\s\S]*?<\/nav>/,
    seoNav(lang)
  );
}

function addTranslationNotePlaceholder(html, lang) {
  /* Footer note is rendered by partials.js; keep a noscript fallback before footer mount */
  const note = TRANSLATION_NOTE[lang];
  if (!note) return html;
  if (html.includes("footer-translation-note")) {
    return html.replace(
      /<p class="footer-translation-note container"[^>]*>[\s\S]*?<\/p>/,
      `<p class="footer-translation-note container" hidden>${note}</p>`
    );
  }
  return html.replace(
    /<div id="site-footer"><\/div>/,
    `<p class="footer-translation-note container" hidden>${note}</p>\n  <div id="site-footer"></div>`
  );
}

function skipLink(lang) {
  const map = {
    en: "Skip to content",
    fr: "Aller au contenu",
    de: "Zum Inhalt springen",
  };
  return map[lang] || "Vai al contenuto";
}

function buildLangPage(srcHtml, lang, file) {
  let html = srcHtml;
  html = fixRelativePaths(html);
  html = setMeta(html, lang, file);
  html = replaceSeoNav(html, lang);
  html = injectScripts(html, lang);
  html = html.replace(
    /<a class="skip-link" href="#main">[^<]*<\/a>/,
    `<a class="skip-link" href="#main">${skipLink(lang)}</a>`
  );
  html = applyPhrases(html, lang);
  html = addTranslationNotePlaceholder(html, lang);
  /* Re-apply path fixes after phrase pass (phrases shouldn't touch paths) */
  return html;
}

function patchItalian(srcHtml, file) {
  let html = srcHtml;
  if (!html.includes('hreflang="x-default"')) {
    html = html.replace(
      /(<link rel="canonical"[^>]*>)/,
      `$1\n  ${hreflangBlock(file)}`
    );
  }
  if (!html.includes("js/i18n.js")) {
    html = html.replace(
      /<script src="js\/partials\.js\?v=\d+"><\/script>/g,
      '<script src="js/i18n.js?v=2"></script>\n  <script src="js/partials.js?v=9"></script>'
    );
  } else {
    html = html.replace(/js\/i18n\.js\?v=\d+/g, "js/i18n.js?v=2");
    html = html.replace(/js\/partials\.js\?v=\d+/g, "js/partials.js?v=9");
  }
  html = html.replace(/js\/esperienze-list\.js\?v=\d+/g, "js/esperienze-list.js?v=9");
  html = html.replace(/css\/style\.css\?v=\d+/g, "css/style.css?v=10");
  /* Shorter nav label in static seo fallback */
  html = html.replace(
    /(<nav class="seo-nav-fallback"[\s\S]*?>)([\s\S]*?)(<\/nav>)/,
    (_, open, body, close) =>
      open + body.replace(/>Scopri Macugnaga</g, ">Macugnaga<") + close
  );
  return html;
}

function writeFile(rel, content) {
  const full = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, content, "utf8");
}

function main() {
  let count = 0;
  for (const file of PAGES) {
    const src = fs.readFileSync(path.join(ROOT, file), "utf8");
    const patchedIt = patchItalian(src, file);
    if (patchedIt !== src) {
      fs.writeFileSync(path.join(ROOT, file), patchedIt, "utf8");
    }
    for (const lang of LANGS) {
      const out = buildLangPage(patchedIt, lang, file);
      const dest = file === "index.html" ? `${lang}/index.html` : `${lang}/${file}`;
      writeFile(dest, out);
      count++;
    }
  }
  console.log(`Built ${count} translated pages for ${PAGES.length} sources.`);
}

main();
