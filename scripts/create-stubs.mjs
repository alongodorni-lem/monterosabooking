import fs from "fs";

const BRAND = "Macugnaga Booking – Esperienze ai piedi del Monte Rosa";
const NAV = `  <div id="site-header">
  <nav class="seo-nav-fallback" aria-label="Navigazione principale">
        <a href="index.html">Home</a>
        <a href="esperienze.html">Esperienze</a>
        <a href="casa-museo-walser.html">Casa Walser</a>
        <a href="miniera-oro.html">Miniera d’oro</a>
        <a href="funivia-seggiovia.html">Impianti</a>
        <a href="mappa.html">Mappa</a>
        <a href="weekend.html">Weekend</a>
        <a href="scopri-macugnaga.html">Scopri Macugnaga</a>
        <a href="chi-siamo.html">Chi siamo</a>
        <a href="come-funziona.html">Come funziona</a>
        <a href="faq.html">FAQ</a>
        <a class="nav-cta" href="esperienze.html">Prenota online</a>
  </nav>
</div>`;

const stubs = [
  {
    file: "trekking-macugnaga.html",
    slug: "trekking-macugnaga.html",
    title: "Trekking a Macugnaga Monte Rosa | Sentieri e escursioni",
    h1: "Trekking e sentieri a Macugnaga",
    desc: "Idee di trekking e escursioni a Macugnaga Monte Rosa: sentieri per tutti i livelli, passeggiate in famiglia e gite dalla pianura. Prenota esperienze online.",
    image: "trekking-salute.jpg",
    related: [
      ["esperienze.html", "Prenota un’escursione"],
      ["famiglie.html", "Montagna con i bambini"],
      ["weekend.html", "Idee weekend"],
    ],
    body: "Macugnaga offre sentieri dal paese ai boschi e, quando gli impianti sono aperti, punti di partenza in quota verso Belvedere e alpeggi. Su questo portale trovi esperienze guidate e benessere da abbinare alla tua giornata outdoor.",
  },
  {
    file: "forest-bathing-macugnaga.html",
    slug: "forest-bathing-macugnaga.html",
    title: "Forest bathing a Macugnaga | Benessere nei boschi",
    h1: "Forest bathing e benessere nei boschi",
    desc: "Forest bathing e passeggiate benessere a Macugnaga Monte Rosa: ritrova respiro tra gli alberi ai piedi del Monte Rosa. Prenota online.",
    image: "forest-bathing.jpg",
    related: [
      ["esperienze.html", "Prenota benessere"],
      ["senior.html", "Montagna per senior"],
      ["coppie.html", "Idee per coppie"],
    ],
    body: "Tra i boschi della Valle Anzasca, pratiche di immersione nella natura e passeggiate lente aiutano a staccare dalla città. Scopri le proposte benessere prenotabili online e abbina una visita culturale in paese.",
  },
  {
    file: "gita-milano-macugnaga.html",
    slug: "gita-milano-macugnaga.html",
    title: "Gita da Milano a Macugnaga | Monte Rosa in giornata o weekend",
    h1: "Gita da Milano a Macugnaga Monte Rosa",
    desc: "Organizza una gita da Milano a Macugnaga: montagna autentica a circa due ore, esperienze per famiglie e weekend. Prenota online.",
    image: "hero-dorf.jpg",
    related: [
      ["fuga-citta.html", "Fuga dalla città"],
      ["weekend.html", "Weekend completo"],
      ["esperienze.html", "Cosa prenotare"],
    ],
    body: "Da Milano (e da Varese o Novara) Macugnaga è una destinazione concreta per una giornata o un pernottamento: villaggio alpino Bandiera Arancione, miniera d’oro, Casa Walser e impianti quando aperti.",
  },
  {
    file: "benessere-montagna-macugnaga.html",
    slug: "benessere-montagna-macugnaga.html",
    title: "Benessere in montagna a Macugnaga | Natura e relax",
    h1: "Benessere in montagna a Macugnaga",
    desc: "Benessere in montagna a Macugnaga Monte Rosa: aria alpina, boschi, ritmo soft e esperienze prenotabili online per staccare dalla città.",
    image: "forest-bathing.jpg",
    related: [
      ["senior.html", "Ritmo soft per senior"],
      ["coppie.html", "Relax per due"],
      ["esperienze.html", "Prenota"],
    ],
    body: "Clima estivo fresco, silenzi e paesaggio del Monte Rosa: Macugnaga è ideale per un soggiorno di benessere. Abbina passeggiate, proposte di forest bathing e visite culturali senza fretta.",
  },
  {
    file: "escursioni-famiglie-macugnaga.html",
    slug: "escursioni-famiglie-macugnaga.html",
    title: "Escursioni per famiglie a Macugnaga | Montagna con i bambini",
    h1: "Escursioni per famiglie a Macugnaga",
    desc: "Escursioni e attività per famiglie a Macugnaga Monte Rosa: percorsi facili, miniera accessibile, Casa Walser. Prenota online.",
    image: "famiglie.jpg",
    related: [
      ["famiglie.html", "Guida famiglie"],
      ["miniera-oro.html", "Miniera d’oro"],
      ["casa-museo-walser.html", "Casa Walser"],
    ],
    body: "Percorsi in piano, visite guidate e attività pensate anche per i più piccoli: Macugnaga è montagna autentica a misura di famiglia, a portata di strada dalla pianura lombardo-piemontese.",
  },
];

function dims(img) {
  if (img === "hero-dorf.jpg") return [1920, 1080];
  if (img === "famiglie.jpg") return [1600, 900];
  if (img === "trekking-salute.jpg") return [1600, 900];
  return [800, 600];
}

for (const s of stubs) {
  const base = s.image.replace(/\.jpe?g$/i, "");
  const [w, h] = dims(s.image);
  const hasWebp = fs.existsSync(`assets/web/${base}.webp`);
  const media = hasWebp
    ? `<picture>
          <source type="image/webp" srcset="assets/web/${base}-800.webp 800w, assets/web/${base}-1200.webp 1200w, assets/web/${base}.webp ${w}w" sizes="100vw">
          <img src="assets/web/${s.image}" srcset="assets/web/${base}-800.jpg 800w, assets/web/${base}-1200.jpg 1200w, assets/web/${s.image} ${w}w" sizes="100vw" alt="" width="${w}" height="${h}" fetchpriority="high" decoding="async">
        </picture>`
    : `<img src="assets/web/${s.image}" alt="" width="${w}" height="${h}" fetchpriority="high" decoding="async">`;

  const links = s.related
    .map(([href, label]) => `<a class="btn btn--outline" href="${href}">${label}</a>`)
    .join("\n            ");

  const html = `<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${s.title}</title>
  <meta name="description" content="${s.desc}">
  <link rel="canonical" href="https://www.macugnagabooking.it/${s.slug}">
  <meta property="og:title" content="${s.h1}">
  <meta property="og:description" content="${s.desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.macugnagabooking.it/${s.slug}">
  <meta property="og:locale" content="it_IT">
  <meta property="og:site_name" content="${BRAND}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${s.title}">
  <meta name="twitter:description" content="${s.desc}">
  <meta name="twitter:image" content="https://www.macugnagabooking.it/assets/web/${s.image}">
  <meta name="twitter:url" content="https://www.macugnagabooking.it/${s.slug}">
  <meta property="og:image" content="https://www.macugnagabooking.it/assets/web/${s.image}">
  <meta name="robots" content="index,follow">
  <meta name="geo.region" content="IT-VB">
  <meta name="geo.placename" content="Macugnaga">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v=6">
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.macugnagabooking.it/"},{"@type":"ListItem","position":2,"name":"${s.h1}","item":"https://www.macugnagabooking.it/${s.slug}"}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"WebPage","name":"${s.h1}","url":"https://www.macugnagabooking.it/${s.slug}","description":"${s.desc}","isPartOf":{"@type":"WebSite","name":"${BRAND}","url":"https://www.macugnagabooking.it/"}}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Vai al contenuto</a>
${NAV}
  <div id="site-search"></div>
  <main id="main">
    <header class="page-hero">
      <div class="page-hero__media">${media}</div>
      <div class="page-hero__scrim" aria-hidden="true"></div>
      <div class="page-hero__content">
        <p class="breadcrumb"><a href="index.html">Home</a> · ${s.h1}</p>
        <h1>${s.h1}</h1>
        <p>${s.desc}</p>
      </div>
    </header>
    <section class="section section--white">
      <div class="container prose reveal">
        <p class="section__eyebrow">In arrivo / approfondimento</p>
        <h2>Cosa puoi fare già oggi</h2>
        <p>${s.body}</p>
        <p class="note">Questa pagina è una landing in evoluzione: i contenuti dettagliati cresceranno nel tempo. Nel frattempo prenota le esperienze attive sul portale.</p>
        <div class="btn-row" style="margin-top:1.5rem">
            <a class="btn btn--primary" href="esperienze.html">Vedi tutte le esperienze</a>
            ${links}
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer"></div>
  <div id="cookie-banner" class="cookie-banner" role="dialog" aria-label="Informativa cookie">
    <p>Questo sito utilizza cookie tecnici necessari al funzionamento e servizi di terze parti per la prenotazione online e i font. <a href="privacy.html">Privacy e cookie</a></p>
    <div class="cookie-banner__actions">
      <button type="button" class="btn btn--primary" data-cookie-accept>Accetta</button>
      <button type="button" class="btn btn--outline" data-cookie-essential>Solo essenziali</button>
    </div>
  </div>
  <script src="js/partials.js?v=6"></script>
  <script src="js/main.js"></script>
</body>
</html>
`;
  fs.writeFileSync(s.file, html, "utf8");
  console.log("wrote", s.file);
}
