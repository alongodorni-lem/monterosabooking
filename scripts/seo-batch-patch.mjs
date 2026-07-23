/**
 * One-shot SEO batch patch: Twitter/OG site_name, crawlable nav fallback,
 * hero picture/srcset, brand string updates, css cache-bust.
 */
import fs from "fs";
import path from "path";

const ROOT = process.cwd();
const BRAND = "Macugnaga Booking – Esperienze ai piedi del Monte Rosa";
const SITE = "https://www.macugnagabooking.it";

const NAV_LINKS = [
  ["index.html", "Home"],
  ["esperienze.html", "Esperienze"],
  ["casa-museo-walser.html", "Casa Walser"],
  ["miniera-oro.html", "Miniera d’oro"],
  ["funivia-seggiovia.html", "Impianti"],
  ["mappa.html", "Mappa"],
  ["weekend.html", "Weekend"],
  ["scopri-macugnaga.html", "Scopri Macugnaga"],
  ["chi-siamo.html", "Chi siamo"],
  ["come-funziona.html", "Come funziona"],
  ["faq.html", "FAQ"],
];

const HERO_MAP = {
  "hero-dorf.jpg": { w: 1920, h: 1080 },
  "proposte-montagna.jpg": { w: 1600, h: 900 },
  "drone-monterosa.jpg": { w: 1600, h: 900 },
  "trekking-salute.jpg": { w: 1600, h: 900 },
  "miniera-hero.jpg": { w: 1600, h: 900 },
  "casa-museo-hero.jpg": { w: 1600, h: 900 },
  "funivia-hero.jpg": { w: 1600, h: 739 },
  "famiglie.jpg": { w: 1600, h: 900 },
  "ossola-macugnaga.jpg": { w: 1600, h: 900 },
  "vecchio-dorf.jpg": { w: 800, h: 600 },
  "forest-bathing.jpg": { w: 800, h: 600 },
};

function navFallback() {
  const links = NAV_LINKS.map(([h, l]) => `<a href="${h}">${l}</a>`).join("\n        ");
  return `<div id="site-header">
  <nav class="seo-nav-fallback" aria-label="Navigazione principale">
        ${links}
        <a class="nav-cta" href="esperienze.html">Prenota online</a>
  </nav>
</div>`;
}

function twitterBlock(title, description, image, url) {
  const lines = [
    `  <meta property="og:site_name" content="${BRAND}">`,
    `  <meta name="twitter:card" content="summary_large_image">`,
    `  <meta name="twitter:title" content="${esc(title)}">`,
    `  <meta name="twitter:description" content="${esc(description)}">`,
  ];
  if (image) lines.push(`  <meta name="twitter:image" content="${image}">`);
  if (url) lines.push(`  <meta name="twitter:url" content="${url}">`);
  return lines.join("\n");
}

function esc(s) {
  return String(s || "")
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;");
}

function metaContent(html, nameOrProp) {
  const re = new RegExp(
    `<meta\\s+(?:name|property)=["']${nameOrProp}["']\\s+content=["']([^"']*)["']`,
    "i"
  );
  const m = html.match(re);
  return m ? m[1] : "";
}

function titleOf(html) {
  const m = html.match(/<title>([^<]*)<\/title>/i);
  return m ? m[1].trim() : BRAND;
}

function pictureFromImg(imgTag) {
  const srcM = imgTag.match(/\bsrc=["']([^"']+)["']/i);
  if (!srcM) return imgTag;
  const src = srcM[1];
  const file = path.basename(src);
  if (!HERO_MAP[file]) return imgTag;
  const base = file.replace(/\.jpe?g$/i, "");
  const dir = src.includes("/") ? src.slice(0, src.lastIndexOf("/") + 1) : "";
  const altM = imgTag.match(/\balt=["']([^"']*)["']/i);
  const alt = altM ? altM[1] : "";
  const wM = imgTag.match(/\bwidth=["'](\d+)["']/i);
  const hM = imgTag.match(/\bheight=["'](\d+)["']/i);
  const dims = HERO_MAP[file];
  const w = wM ? wM[1] : String(dims.w);
  const h = hM ? hM[1] : String(dims.h);
  const fp = /fetchpriority=["']high["']/i.test(imgTag);
  const lazy = /loading=["']lazy["']/i.test(imgTag);
  const attrs = [
    `src="${dir}${file}"`,
    `srcset="${dir}${base}-800.jpg 800w, ${dir}${base}-1200.jpg 1200w, ${dir}${file} ${dims.w}w"`,
    `sizes="100vw"`,
    `alt="${alt}"`,
    `width="${w}"`,
    `height="${h}"`,
  ];
  if (fp) attrs.push(`fetchpriority="high"`);
  if (lazy) attrs.push(`loading="lazy"`);
  else if (!fp) attrs.push(`loading="lazy"`);
  attrs.push(`decoding="async"`);
  return `<picture>
          <source type="image/webp" srcset="${dir}${base}-800.webp 800w, ${dir}${base}-1200.webp 1200w, ${dir}${base}.webp ${dims.w}w" sizes="100vw">
          <img ${attrs.join(" ")}>
        </picture>`;
}

function patchHeroes(html) {
  // Only enhance heroes / page-hero / first split media — match img tags that reference known heroes
  return html.replace(/<img\b[^>]*>/gi, (tag) => {
    const srcM = tag.match(/\bsrc=["']([^"']+)["']/i);
    if (!srcM) return tag;
    const file = path.basename(srcM[1]);
    if (!HERO_MAP[file]) return tag;
    // skip if already inside picture (rough)
    return pictureFromImg(tag);
  });
}

function patchFile(file) {
  let html = fs.readFileSync(file, "utf8");
  const orig = html;

  // Brand string replacements in titles/footers visible copy (careful)
  html = html.replace(/Mountain Experience Monterosa Macugnaga/g, BRAND);
  html = html.replace(/Mountain Experience Portale di prenotazione/g, BRAND);

  // css cache bust
  html = html.replace(/css\/style\.css\?v=\d+/g, "css/style.css?v=6");
  html = html.replace(/js\/partials\.js\?v=\d+/g, "js/partials.js?v=6");

  // og:site_name + twitter (idempotent)
  if (!/property=["']og:site_name["']/.test(html)) {
    const title = titleOf(html);
    const desc =
      metaContent(html, "og:description") ||
      metaContent(html, "description") ||
      "";
    const image = metaContent(html, "og:image");
    const url = metaContent(html, "og:url") || "";
    const block = twitterBlock(title, desc, image, url);
    if (/property=["']og:locale["'][^>]*>/.test(html)) {
      html = html.replace(
        /(<meta property=["']og:locale["'][^>]*>)/i,
        `$1\n${block}`
      );
    } else if (/property=["']og:url["'][^>]*>/.test(html)) {
      html = html.replace(
        /(<meta property=["']og:url["'][^>]*>)/i,
        `$1\n${block}`
      );
    } else {
      html = html.replace(
        /(<link rel=["']canonical["'][^>]*>)/i,
        `$1\n${block}`
      );
    }
  }

  // skip link
  if (!/class=["']skip-link["']/.test(html)) {
    html = html.replace(
      /<body>/i,
      `<body>\n  <a class="skip-link" href="#main">Vai al contenuto</a>`
    );
  }

  // main id for skip link
  if (/<main>/.test(html) && !/<main\b[^>]*\bid=/.test(html)) {
    html = html.replace(/<main>/, '<main id="main">');
  }

  // crawlable nav fallback
  if (/<div id=["']site-header["']>\s*<\/div>/.test(html)) {
    html = html.replace(
      /<div id=["']site-header["']>\s*<\/div>/,
      navFallback()
    );
  } else if (
    /<div id=["']site-header["']><\/div>/.test(html) &&
    !/seo-nav-fallback/.test(html)
  ) {
    html = html.replace(/<div id=["']site-header["']><\/div>/, navFallback());
  }

  // hero picture/srcset (avoid double-wrapping)
  if (!/<picture>/.test(html)) {
    html = patchHeroes(html);
  }

  if (html !== orig) {
    fs.writeFileSync(file, html, "utf8");
    return true;
  }
  return false;
}

const files = fs
  .readdirSync(ROOT)
  .filter((f) => f.endsWith(".html"))
  .map((f) => path.join(ROOT, f));

let n = 0;
for (const f of files) {
  if (patchFile(f)) {
    console.log("patched", path.basename(f));
    n++;
  } else {
    console.log("unchanged", path.basename(f));
  }
}
console.log("done", n);
