import fs from "fs";

const files = fs.readdirSync(".").filter((f) => f.endsWith(".html"));
const texts = new Set();
for (const f of files) {
  const html = fs.readFileSync(f, "utf8");
  const main = (html.match(/<main[\s\S]*?<\/main>/i) || [""])[0];
  const title = (html.match(/<title>([^<]*)<\/title>/) || [])[1];
  const desc = (html.match(/name="description" content="([^"]*)"/) || [])[1];
  if (title) texts.add(title);
  if (desc) texts.add(desc);
  main.replace(/>([^<]{8,})</g, (_, t) => {
    const s = t.replace(/\s+/g, " ").trim();
    if (s && !/^[\d\s.,;:!?%€\-–—]+$/.test(s)) texts.add(s);
  });
}
const list = [...texts].sort((a, b) => b.length - a.length);
fs.mkdirSync("scripts", { recursive: true });
fs.writeFileSync("scripts/_extract-strings.json", JSON.stringify(list, null, 2));
console.log("unique strings", list.length);
