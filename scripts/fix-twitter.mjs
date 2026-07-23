import fs from "fs";

const BRAND = "Macugnaga Booking – Esperienze ai piedi del Monte Rosa";

function getMeta(html, prop) {
  const re = new RegExp(
    `<meta\\s+(?:name|property)=["']${prop}["']\\s+content=(["'])([\\s\\S]*?)\\1`,
    "i"
  );
  const m = html.match(re);
  return m ? m[2] : "";
}

function titleOf(html) {
  const m = html.match(/<title>([^<]*)<\/title>/i);
  return m ? m[1].trim() : BRAND;
}

function escAttr(s) {
  return String(s).replace(/&/g, "&amp;").replace(/"/g, "&quot;");
}

for (const f of fs.readdirSync(".").filter((x) => x.endsWith(".html"))) {
  let html = fs.readFileSync(f, "utf8");
  const title = titleOf(html);
  const desc = getMeta(html, "og:description") || getMeta(html, "description");
  const image = getMeta(html, "og:image");
  const url = getMeta(html, "og:url");
  if (!desc) {
    console.log("no desc", f);
    continue;
  }
  html = html.replace(/\s*<meta name="twitter:title"[^>]*>/gi, "");
  html = html.replace(/\s*<meta name="twitter:description"[^>]*>/gi, "");
  html = html.replace(/\s*<meta name="twitter:image"[^>]*>/gi, "");
  html = html.replace(/\s*<meta name="twitter:url"[^>]*>/gi, "");
  const block = [
    `  <meta name="twitter:title" content="${escAttr(title)}">`,
    `  <meta name="twitter:description" content="${escAttr(desc)}">`,
    image ? `  <meta name="twitter:image" content="${escAttr(image)}">` : "",
    url ? `  <meta name="twitter:url" content="${escAttr(url)}">` : "",
  ]
    .filter(Boolean)
    .join("\n");
  if (!/name="twitter:card"/.test(html)) {
    console.log("no twitter card", f);
    continue;
  }
  html = html.replace(/(<meta name="twitter:card"[^>]*>)/i, `$1\n${block}`);
  fs.writeFileSync(f, html);
  console.log("fixed", f);
}
