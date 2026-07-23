import fs from "fs";

const files = fs.readdirSync(".").filter((f) => f.endsWith(".html"));
let ok = true;
for (const f of files) {
  const html = fs.readFileSync(f, "utf8");
  const h1s = [...html.matchAll(/<h1\b[^>]*>([\s\S]*?)<\/h1>/gi)].map((m) =>
    m[1].replace(/<[^>]+>/g, "").trim()
  );
  if (h1s.length !== 1) {
    console.log("H1 count", h1s.length, f, h1s);
    ok = false;
  }
  const blocks = [
    ...html.matchAll(
      /<script type="application\/ld\+json">([\s\S]*?)<\/script>/gi
    ),
  ];
  for (const [, raw] of blocks) {
    try {
      JSON.parse(raw);
    } catch (e) {
      console.log("JSON-LD fail", f, e.message);
      ok = false;
    }
  }
  if (/SearchAction/.test(html)) {
    console.log("SearchAction still in", f);
    ok = false;
  }
  if (/onrender\.com/.test(html)) {
    console.log("onrender in", f);
    ok = false;
  }
  if (!/rel="canonical"/.test(html)) {
    console.log("missing canonical", f);
    ok = false;
  }
  if (!/twitter:card/.test(html)) {
    console.log("missing twitter", f);
    ok = false;
  }
  if (!/seo-nav-fallback/.test(html)) {
    console.log("missing nav fallback", f);
    ok = false;
  }
}
console.log(ok ? "VERIFY_OK" : "VERIFY_FAIL");
