# -*- coding: utf-8 -*-
"""Second-pass localization for remaining Italian leftovers on EN/FR/DE pages."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (lang, relative path) -> list of (old, new)
FIXES: dict[tuple[str, str], list[tuple[str, str]]] = {}


def add(lang: str, rel: str, pairs: list[tuple[str, str]]) -> None:
    FIXES.setdefault((lang, rel), []).extend(pairs)


# ---- EN fuga-citta ----
add(
    "en",
    "fuga-citta.html",
    [
        (
            '''      {
        "@type": "Question",
        "name": "Macugnaga è la montagna vera, vicina a Milano, Novara, Varese e città della pianura?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sì: Macugnaga (Valle Anzasca, VB) ai piedi del Monte Rosa è raggiungibile in circa 2 ore from Milan, circa 1,5 ore from Novara e Varese, and also from Lake Maggiore, from Turin, Genova e from Switzerland (Vallese e Ticino). Ideale per gite in montagna e weekend fuori città."
        }
      },
      {
        "@type": "Question",
        "name": "Che tipo di gita in montagna si può fare a Macugnaga?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Experiences a contatto con la natura (passeggiate, forest bathing, escursioni soft), visite alla Walser House Museum e alla miniera d'oro, benessere e vita di paese — senza alpinismo tecnico. Online booking on booking portal."
        }
      },
      {
        "@type": "Question",
        "name": "Meglio un weekend o un soggiorno più lungo?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Entrambi funzionano: un weekend Macugnaga Monte Rosa basta per natura, cultura e relax; settimane e soggiorni lunghi sono ideali per chi cerca quiete, lavoro remoto o studio lontano dal rumore della città."
        }
      }''',
            '''      {
        "@type": "Question",
        "name": "Is Macugnaga real mountains, close to Milan, Novara, Varese and the cities of the plain?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes: Macugnaga (Anzasca Valley, VB) at the foot of Monte Rosa is reachable in about 2 hours from Milan, about 1.5 hours from Novara and Varese, and also from Lake Maggiore, Turin, Genoa and Switzerland (Valais and Ticino). Ideal for mountain day trips and weekends out of town."
        }
      },
      {
        "@type": "Question",
        "name": "What kind of mountain day trip can you do in Macugnaga?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Nature experiences (walks, forest bathing, soft hikes), visits to the Walser House Museum and the gold mine, wellness and village life — without technical mountaineering. Online booking on the booking portal."
        }
      },
      {
        "@type": "Question",
        "name": "Is a weekend or a longer stay better?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Both work: a Macugnaga Monte Rosa weekend is enough for nature, culture and relaxation; weeks and longer stays are ideal for quiet, remote work or study away from city noise."
        }
      }''',
        ),
        ('alt="Macugnaga, rifugio alpino dalla città"', 'alt="Macugnaga, an alpine refuge from the city"'),
        ("<h1>City escape, cuore delle Alpi</h1>", "<h1>City escape, heart of the Alps</h1>"),
        (
            "<p>Macugnaga, la montagna vera, vicina a Milano, al Lake Maggiore, Novara, Varese e città della pianura — and Torino, Genova e la Svizzera: gite, weekend e soggiorni lunghi in un villaggio alpino autentico.</p>",
            "<p>Macugnaga, real mountains close to Milan, Lake Maggiore, Novara, Varese and the cities of the plain — and Turin, Genoa and Switzerland: day trips, weekends and longer stays in an authentic alpine village.</p>",
        ),
        ("<p class=\"section__eyebrow\">Centralità</p>", '<p class="section__eyebrow">Centrality</p>'),
        ("<h2>Lontano dal rumore, a portata di strada</h2>", "<h2>Far from the noise, within easy reach</h2>"),
        (
            "<p>Macugnaga è il punto d’incontro ideale tra Pianura Padana e Alpi: within easy reach of <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> and <strong>Lake Maggiore</strong> (including Orta and Mergozzo), and also from <strong>Turin</strong>, <strong>Genoa</strong>, Canton <strong>Valais</strong> and <strong>Ticino</strong>.</p>",
            "<p>Macugnaga is the ideal meeting point between the Po Plain and the Alps: within easy reach of <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> and <strong>Lake Maggiore</strong> (including Orta and Mergozzo), and also from <strong>Turin</strong>, <strong>Genoa</strong>, Canton <strong>Valais</strong> and <strong>Ticino</strong>.</p>",
        ),
        (
            "<p>Ideale per <strong>gite in montagna</strong>, idee weekend fuori città e per ritrovare se stessi e i propri affetti — oppure per settimane rigeneranti e soggiorni lunghi, including per nomadi digitali e chi cerca quiete per studiare o lavorare. Se soggiorni in hotel o campeggio on the laghi, Macugnaga è una meta in montagna raggiungibile per una giornata: <a href=\"esperienze.html\">prenota online</a>.</p>",
            "<p>Ideal for <strong>mountain day trips</strong>, weekend ideas out of town and reconnecting with yourself and loved ones — or for restorative weeks and longer stays, including for digital nomads and anyone seeking quiet to study or work. If you stay in a hotel or campsite on the lakes, Macugnaga is a mountain destination reachable for a day: <a href=\"esperienze.html\">book online</a>.</p>",
        ),
        ('href="weekend.html">Pianifica il weekend</a>', 'href="weekend.html">Plan the weekend</a>'),
        ('aria-label="Distanze indicative da Macugnaga"', 'aria-label="Indicative distances from Macugnaga"'),
        (
            'alt="Experiences a contatto con la natura nei boschi di Macugnaga"',
            'alt="Nature experiences in the woods of Macugnaga"',
        ),
        ('<p class="section__eyebrow">Come restare</p>', '<p class="section__eyebrow">How to stay</p>'),
        ("<h2>Weekend, settimane, vita lenta</h2>", "<h2>Weekends, weeks, slow living</h2>"),
        (
            "<li><strong>Weekend</strong> — fuga breve con pernottamento ed esperienze a contatto con la natura</li>",
            "<li><strong>Weekend</strong> — a short escape with overnight stay and nature experiences</li>",
        ),
        (
            "<li><strong>Settimane</strong> — ritmo lento, escursioni soft, cultura e benessere</li>",
            "<li><strong>Weeks</strong> — slow pace, soft hikes, culture and wellness</li>",
        ),
        (
            "<li><strong>Soggiorni lunghi</strong> — base tranquilla per lavoro remoto e studio</li>",
            "<li><strong>Longer stays</strong> — a quiet base for remote work and study</li>",
        ),
        ('href="esperienze.html">Prenota esperienze</a>', 'href="esperienze.html">Book experiences</a>'),
        (">Alloggi</a>", ">Where to stay</a>"),
        (
            "<h2 class=\"reveal\">Frequently asked questions on the fuga dalla città</h2>",
            '<h2 class="reveal">Frequently asked questions about the city escape</h2>',
        ),
        (
            """          <details class="faq-item reveal">
            <summary>Macugnaga è la montagna vera, vicina a Milano, Novara, Varese e città della pianura?</summary>
            <p class="faq-a">Sì: circa <strong>2 ore</strong> from Milan, <strong>1,5 ore</strong> from Novara e Varese; also reachable from Lake Maggiore, from Turin, Genova e from Switzerland. Ideale per gite in montagna e weekend Macugnaga Monte Rosa.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Che tipo di gita in montagna si può fare?</summary>
            <p class="faq-a">Experiences a contatto con la natura, passeggiate, benessere, <a href="casa-museo-walser.html">Walser House</a> e <a href="miniera-oro.html">gold mine</a> — montagna accessibile, senza alpinismo tecnico. <a href="esperienze.html">Book online</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Meglio un weekend o un soggiorno più lungo?</summary>
            <p class="faq-a">Entrambi: il weekend basta per natura e relax; settimane e soggiorni lunghi sono perfetti per quiete, studio e lavoro remoto. See also <a href="weekend.html">Weekend ideas</a>.</p>
          </details>""",
            """          <details class="faq-item reveal">
            <summary>Is Macugnaga real mountains, close to Milan, Novara, Varese and the cities of the plain?</summary>
            <p class="faq-a">Yes: about <strong>2 hours</strong> from Milan, <strong>1.5 hours</strong> from Novara and Varese; also reachable from Lake Maggiore, Turin, Genoa and Switzerland. Ideal for mountain day trips and Macugnaga Monte Rosa weekends.</p>
          </details>
          <details class="faq-item reveal">
            <summary>What kind of mountain day trip can you do?</summary>
            <p class="faq-a">Nature experiences, walks, wellness, <a href="casa-museo-walser.html">Walser House</a> and <a href="miniera-oro.html">gold mine</a> — accessible mountains, without technical mountaineering. <a href="esperienze.html">Book online</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is a weekend or a longer stay better?</summary>
            <p class="faq-a">Both: a weekend is enough for nature and relaxation; weeks and longer stays are perfect for quiet, study and remote work. See also <a href="weekend.html">Weekend ideas</a>.</p>
          </details>""",
        ),
    ],
)

# ---- EN short landings ----
add(
    "en",
    "benessere-montagna-macugnaga.html",
    [
        (
            '{"@type":"ListItem","position":2,"name":"Benessere in montagna a Macugnaga","item":"https://www.macugnagabooking.it/en/benessere-montagna-macugnaga.html"}',
            '{"@type":"ListItem","position":2,"name":"Mountain wellness in Macugnaga","item":"https://www.macugnagabooking.it/en/benessere-montagna-macugnaga.html"}',
        ),
        (
            '"name":"Benessere in montagna a Macugnaga","url":"https://www.macugnagabooking.it/en/benessere-montagna-macugnaga.html","description":"Benessere in montagna a Macugnaga Monte Rosa: aria alpina, boschi, ritmo soft e esperienze prenotabili online per staccare dalla città."',
            '"name":"Mountain wellness in Macugnaga","url":"https://www.macugnagabooking.it/en/benessere-montagna-macugnaga.html","description":"Mountain wellness in Macugnaga Monte Rosa: alpine air, woods, a soft pace and experiences you can book online to switch off from the city."',
        ),
        (
            '<p class="breadcrumb"><a href="index.html">Home</a> · Benessere in montagna a Macugnaga</p>\n        <h1>Benessere in montagna a Macugnaga</h1>\n        <p>Benessere in montagna a Macugnaga Monte Rosa: aria alpina, boschi, ritmo soft e esperienze prenotabili online per staccare dalla città.</p>',
            '<p class="breadcrumb"><a href="index.html">Home</a> · Mountain wellness in Macugnaga</p>\n        <h1>Mountain wellness in Macugnaga</h1>\n        <p>Mountain wellness in Macugnaga Monte Rosa: alpine air, woods, a soft pace and experiences you can book online to switch off from the city.</p>',
        ),
        (
            "<p>Clima estivo fresco, silenzi e paesaggio del Monte Rosa: Macugnaga è ideale per un soggiorno di benessere. Abbina passeggiate, proposte di forest bathing e visite culturali senza fretta.</p>",
            "<p>Fresh summer climate, silence and the Monte Rosa landscape: Macugnaga is ideal for a wellness stay. Combine walks, forest bathing and cultural visits at an easy pace.</p>",
        ),
        (">Ritmo soft per senior</a>", ">Soft pace for seniors</a>"),
        (">Relax per due</a>", ">Relax for two</a>"),
        (">Prenota</a>", ">Book</a>"),
    ],
)

add(
    "en",
    "gita-milano-macugnaga.html",
    [
        (
            '"name":"Gita from Milan a Macugnaga Monte Rosa"',
            '"name":"Day trip from Milan to Macugnaga Monte Rosa"',
        ),
        (
            '"description":"Organizza una gita from Milan a Macugnaga: montagna autentica a circa due ore, including raggiungibile dal Lake Maggiore. Experiences per famiglie e weekend. Book online."',
            '"description":"Plan a day trip from Milan to Macugnaga: authentic mountains about two hours away, also reachable from Lake Maggiore. Experiences for families and weekends. Book online."',
        ),
        (
            '<p class="breadcrumb"><a href="index.html">Home</a> · Gita from Milan a Macugnaga Monte Rosa</p>\n        <h1>Gita from Milan a Macugnaga Monte Rosa</h1>\n        <p>Organizza una gita from Milan a Macugnaga: montagna autentica a circa due ore, including raggiungibile dal Lake Maggiore. Experiences per famiglie e weekend. Book online.</p>',
            '<p class="breadcrumb"><a href="index.html">Home</a> · Day trip from Milan to Macugnaga Monte Rosa</p>\n        <h1>Day trip from Milan to Macugnaga Monte Rosa</h1>\n        <p>Plan a day trip from Milan to Macugnaga: authentic mountains about two hours away, also reachable from Lake Maggiore. Experiences for families and weekends. Book online.</p>',
        ),
        (
            "<p>Da Milano (e from Varese, Novara o dal Lake Maggiore) Macugnaga è una destinazione concreta per una giornata o un pernottamento: villaggio alpino Bandiera Arancione, gold mine, Walser House e impianti quando aperti.</p>",
            "<p>From Milan (and from Varese, Novara or Lake Maggiore) Macugnaga is a concrete destination for a day or an overnight stay: Orange Flag alpine village, gold mine, Walser House and lifts when open.</p>",
        ),
        (
            "<p>Anche se soggiorni in hotel o campeggio on Lake Maggiore, on Lake Orta or on Lake Mergozzo, puoi organizzare una giornata in montagna a Macugnaga / Monterosa e <a href=\"esperienze.html\">prenotare le esperienze online</a>.</p>",
            "<p>Even if you stay in a hotel or campsite on Lake Maggiore, on Lake Orta or on Lake Mergozzo, you can plan a mountain day in Macugnaga / Monterosa and <a href=\"esperienze.html\">book experiences online</a>.</p>",
        ),
        (">Weekend completo</a>", ">Full weekend</a>"),
        (">Cosa prenotare</a>", ">What to book</a>"),
    ],
)

add(
    "en",
    "senior.html",
    [
        ("<h1>Montagna per senior</h1>", "<h1>Mountains for seniors</h1>"),
        (
            "<p>Clima benefico, percorsi accessibili, cultura e silenzio: Macugnaga accoglie chi cerca benessere senza fretta.</p>",
            "<p>Beneficial climate, accessible routes, culture and silence: Macugnaga welcomes anyone seeking wellness without hurry.</p>",
        ),
        ('<p class="section__eyebrow">Benessere alpino</p>', '<p class="section__eyebrow">Alpine wellness</p>'),
        ("<h2>Un ritmo soft, tra paese e natura</h2>", "<h2>A soft pace, between village and nature</h2>"),
        (
            "<p>L’estate a Macugnaga regala respiro also nei giorni più caldi della pianura. Passeggiate leggere, visite culturali, forest bathing e momenti di quiete nel Dorf: esperienze a contatto con la natura, con naturalezza e sicurezza, accompagnati da operatori qualificati.</p>",
            "<p>Summer in Macugnaga brings breath even on the hottest days of the plain. Light walks, cultural visits, forest bathing and quiet moments in the Dorf: nature experiences, with ease and safety, accompanied by qualified operators.</p>",
        ),
        (
            "<li>Escursioni e passeggiate a difficoltà contenuta</li>",
            "<li>Hikes and walks of moderate difficulty</li>",
        ),
        (
            "<li>Weekend o soggiorni lunghi in hotel e B&amp;B</li>",
            "<li>Weekends or longer stays in hotels and B&amp;Bs</li>",
        ),
        (">Scopri le esperienze</a>", ">Discover the experiences</a>"),
        ('alt="Forest bathing tra gli alberi"', 'alt="Forest bathing among the trees"'),
        ("<h2>Cultura e paesaggio</h2>", "<h2>Culture and landscape</h2>"),
        (
            "<p class=\"lead\">Conoscere la storia walser, ammirare le case antiche, salire in seggiovia verso Burki e Belvedere (quando aperti): Macugnaga offre scoperte senza stress.</p>",
            '<p class="lead">Discover Walser history, admire historic houses, ride the chairlift toward Burki and Belvedere (when open): Macugnaga offers discoveries without stress.</p>',
        ),
        (">Scopri il paese</a>", ">Discover the village</a>"),
    ],
)

add(
    "en",
    "coppie.html",
    [
        ("<h1>Montagna per coppie</h1>", "<h1>Mountains for couples</h1>"),
        (
            "<p>Alba e tramonto on Rosa, silenzi di villaggio, sapori locali e esperienze da vivere in due.</p>",
            "<p>Sunrise and sunset on the Rosa, village silence, local flavours and experiences to share as a couple.</p>",
        ),
        ('<p class="section__eyebrow">Weekend a due</p>', '<p class="section__eyebrow">Weekend for two</p>'),
        ("<h2>Ritrovarsi ai piedi del Monte Rosa</h2>", "<h2>Reconnect at the foot of Monte Rosa</h2>"),
        (
            "<p>Concedetevi una fuga breve ma intensa: pernottamento in hotel o B&amp;B, aperitivo in centro, cena tipica, una passeggiata al tramonto e un’esperienza a contatto con la natura — dalla miniera al benessere nei boschi.</p>",
            "<p>Treat yourselves to a short but intense escape: overnight stay in a hotel or B&amp;B, aperitivo in the centre, typical dinner, a sunset walk and a nature experience — from the mine to woodland wellness.</p>",
        ),
        (
            "<li>Paesaggio imponente e atmosfera intima di villaggio</li>",
            "<li>Imposing landscape and intimate village atmosphere</li>",
        ),
        (
            "<li>Alloggi accoglienti e ristoranti di qualità</li>",
            "<li>Welcoming lodging and quality restaurants</li>",
        ),
        (
            "<li>Attività prenotabili online in pochi click</li>",
            "<li>Activities you can book online in a few clicks</li>",
        ),
        ('alt="Paesaggio romantico di Macugnaga"', 'alt="Romantic landscape of Macugnaga"'),
    ],
)

add(
    "en",
    "forest-bathing-macugnaga.html",
    [
        (
            "<p>Tra i boschi della Valle Anzasca, pratiche di immersione nella natura e passeggiate lente aiutano a staccare dalla città. Scopri le proposte benessere prenotabili online e abbina una visita culturale in paese.</p>",
            "<p>Among the woods of the Anzasca Valley, nature immersion practices and slow walks help you switch off from the city. Discover wellness offers you can book online and combine with a cultural visit in the village.</p>",
        ),
    ],
)

add(
    "en",
    "come-funziona.html",
    [
        (
            '"name": "Come prenotare un\'esperienza a Macugnaga"',
            '"name": "How to book an experience in Macugnaga"',
        ),
        (
            '{"@type": "HowToStep", "name": "Scegli l\'esperienza", "text": "Cerca per date o sfoglia l\'elenco delle attività disponibili su Experiences."}',
            '{"@type": "HowToStep", "name": "Choose the experience", "text": "Search by dates or browse the list of available activities on Experiences."}',
        ),
        (
            '{"@type": "HowToStep", "name": "Paga in sicurezza", "text": "Completa il pagamento con credit card o PayPal tramite il modulo di prenotazione online."}',
            '{"@type": "HowToStep", "name": "Pay securely", "text": "Complete payment with credit card or PayPal via the online booking form."}',
        ),
        (
            '{"@type": "HowToStep", "name": "Ricevi conferma", "text": "Ottieni subito l\'email con informazioni e contatti delle guide."}',
            '{"@type": "HowToStep", "name": "Receive confirmation", "text": "Get the email immediately with information and guide contacts."}',
        ),
    ],
)

add(
    "en",
    "chi-siamo.html",
    [
        (">Vedi le esperienze</a>", ">See the experiences</a>"),
    ],
)

add(
    "en",
    "famiglie.html",
    [
        (
            '"name": "Quali esperienze in famiglia si possono prenotare?"',
            '"name": "Which family experiences can you book?"',
        ),
        (
            '"name": "Come organizzare un weekend in montagna con i bambini?"',
            '"name": "How do you organise a mountain weekend with children?"',
        ),
        (
            '"text": "Sì: Macugnaga è tra le montagne per famiglie più accessibili del Monte Rosa — percorsi facili, villaggio a misura di bambino, esperienze guidate e operatori qualificati. Ideale also per gite in giornata o weekend from Milan, dal Lake Maggiore, Varese e Novara."',
            '"text": "Yes: Macugnaga is among the most accessible family mountains of Monte Rosa — easy routes, a child-friendly village, guided experiences and qualified operators. Ideal also for day trips or weekends from Milan, Lake Maggiore, Varese and Novara."',
        ),
        (
            "<summary>Quali esperienze in famiglia si possono prenotare?</summary>",
            "<summary>Which family experiences can you book?</summary>",
        ),
        (
            "<summary>Come organizzare un weekend in montagna con i bambini?</summary>",
            "<summary>How do you organise a mountain weekend with children?</summary>",
        ),
        (
            '<p class="faq-a">Sì: percorsi facili, villaggio accogliente ed esperienze guidate. Ideale tra le <strong>montagne per famiglie</strong> del Monte Rosa, including per gite from Milan, dal Lake Maggiore, Varese e Novara.</p>',
            '<p class="faq-a">Yes: easy routes, a welcoming village and guided experiences. Ideal among the <strong>family mountains</strong> of Monte Rosa, including for day trips from Milan, Lake Maggiore, Varese and Novara.</p>',
        ),
    ],
)


def apply_fr_de_mirrors() -> None:
    """Add FR/DE equivalents for short landings and key phrases."""
    # benessere FR
    add(
        "fr",
        "benessere-montagna-macugnaga.html",
        [
            (
                '{"@type":"ListItem","position":2,"name":"Benessere in montagna a Macugnaga","item":"https://www.macugnagabooking.it/fr/benessere-montagna-macugnaga.html"}',
                '{"@type":"ListItem","position":2,"name":"Bien-être en montagne à Macugnaga","item":"https://www.macugnagabooking.it/fr/benessere-montagna-macugnaga.html"}',
            ),
            (
                '"name":"Benessere in montagna a Macugnaga","url":"https://www.macugnagabooking.it/fr/benessere-montagna-macugnaga.html","description":"Benessere in montagna a Macugnaga Monte Rosa: aria alpina, boschi, ritmo soft e esperienze prenotabili online per staccare dalla città."',
                '"name":"Bien-être en montagne à Macugnaga","url":"https://www.macugnagabooking.it/fr/benessere-montagna-macugnaga.html","description":"Bien-être en montagne à Macugnaga Monte Rosa : air alpin, forêts, rythme doux et expériences réservables en ligne pour décrocher de la ville."',
            ),
            (
                '<p class="breadcrumb"><a href="index.html">Accueil</a> · Benessere in montagna a Macugnaga</p>\n        <h1>Benessere in montagna a Macugnaga</h1>\n        <p>Benessere in montagna a Macugnaga Monte Rosa: aria alpina, boschi, ritmo soft e esperienze prenotabili online per staccare dalla città.</p>',
                '<p class="breadcrumb"><a href="index.html">Accueil</a> · Bien-être en montagne à Macugnaga</p>\n        <h1>Bien-être en montagne à Macugnaga</h1>\n        <p>Bien-être en montagne à Macugnaga Monte Rosa : air alpin, forêts, rythme doux et expériences réservables en ligne pour décrocher de la ville.</p>',
            ),
            (
                "<p>Clima estivo fresco, silenzi e paesaggio del Monte Rosa: Macugnaga è ideale per un soggiorno di benessere. Abbina passeggiate, proposte di forest bathing e visite culturali senza fretta.</p>",
                "<p>Climat estival frais, silences et paysage du Monte Rosa : Macugnaga est idéale pour un séjour bien-être. Associez promenades, forest bathing et visites culturelles sans précipitation.</p>",
            ),
            (">Ritmo soft per senior</a>", ">Rythme doux pour seniors</a>"),
            (">Relax per due</a>", ">Détente à deux</a>"),
            (">Prenota</a>", ">Réserver</a>"),
        ],
    )
    add(
        "de",
        "benessere-montagna-macugnaga.html",
        [
            (
                '{"@type":"ListItem","position":2,"name":"Benessere in montagna a Macugnaga","item":"https://www.macugnagabooking.it/de/benessere-montagna-macugnaga.html"}',
                '{"@type":"ListItem","position":2,"name":"Berg-Wellness in Macugnaga","item":"https://www.macugnagabooking.it/de/benessere-montagna-macugnaga.html"}',
            ),
            (
                '"name":"Benessere in montagna a Macugnaga","url":"https://www.macugnagabooking.it/de/benessere-montagna-macugnaga.html","description":"Benessere in montagna a Macugnaga Monte Rosa: aria alpina, boschi, ritmo soft e esperienze prenotabili online per staccare dalla città."',
                '"name":"Berg-Wellness in Macugnaga","url":"https://www.macugnagabooking.it/de/benessere-montagna-macugnaga.html","description":"Berg-Wellness in Macugnaga Monte Rosa: Alpenluft, Wälder, sanftes Tempo und online buchbare Erlebnisse zum Abschalten von der Stadt."',
            ),
            (
                '<p class="breadcrumb"><a href="index.html">Start</a> · Benessere in montagna a Macugnaga</p>\n        <h1>Benessere in montagna a Macugnaga</h1>\n        <p>Benessere in montagna a Macugnaga Monte Rosa: aria alpina, boschi, ritmo soft e esperienze prenotabili online per staccare dalla città.</p>',
                '<p class="breadcrumb"><a href="index.html">Start</a> · Berg-Wellness in Macugnaga</p>\n        <h1>Berg-Wellness in Macugnaga</h1>\n        <p>Berg-Wellness in Macugnaga Monte Rosa: Alpenluft, Wälder, sanftes Tempo und online buchbare Erlebnisse zum Abschalten von der Stadt.</p>',
            ),
            (
                "<p>Clima estivo fresco, silenzi e paesaggio del Monte Rosa: Macugnaga è ideale per un soggiorno di benessere. Abbina passeggiate, proposte di forest bathing e visite culturali senza fretta.</p>",
                "<p>Frisches Sommerklima, Stille und Monte-Rosa-Landschaft: Macugnaga ist ideal für einen Wellness-Aufenthalt. Kombinieren Sie Spaziergänge, Forest Bathing und Kulturbesuche ohne Hetze.</p>",
            ),
            (">Ritmo soft per senior</a>", ">Sanftes Tempo für Senioren</a>"),
            (">Relax per due</a>", ">Entspannung zu zweit</a>"),
            (">Prenota</a>", ">Buchen</a>"),
        ],
    )

    # gita FR/DE
    add(
        "fr",
        "gita-milano-macugnaga.html",
        [
            (
                '"name":"Gita depuis Milan a Macugnaga Monte Rosa"',
                '"name":"Sortie depuis Milan vers Macugnaga Monte Rosa"',
            ),
            (
                '"description":"Organizza una gita depuis Milan a Macugnaga: montagna autentica a circa due ore, y compris raggiungibile dal Lac Majeur. Expériences per famiglie e weekend. Réserver en ligne."',
                '"description":"Organisez une sortie depuis Milan vers Macugnaga : montagne authentique à environ deux heures, aussi accessible depuis le Lac Majeur. Expériences pour familles et week-ends. Réserver en ligne."',
            ),
            (
                '<p class="breadcrumb"><a href="index.html">Accueil</a> · Gita depuis Milan a Macugnaga Monte Rosa</p>\n        <h1>Gita depuis Milan a Macugnaga Monte Rosa</h1>\n        <p>Organizza una gita depuis Milan a Macugnaga: montagna autentica a circa due ore, y compris raggiungibile dal Lac Majeur. Expériences per famiglie e weekend. Réserver en ligne.</p>',
                '<p class="breadcrumb"><a href="index.html">Accueil</a> · Sortie depuis Milan vers Macugnaga Monte Rosa</p>\n        <h1>Sortie depuis Milan vers Macugnaga Monte Rosa</h1>\n        <p>Organisez une sortie depuis Milan vers Macugnaga : montagne authentique à environ deux heures, aussi accessible depuis le Lac Majeur. Expériences pour familles et week-ends. Réserver en ligne.</p>',
            ),
            (
                "<p>Anche se soggiorni in hotel o campeggio sur Lac Majeur, sur Lac d’Orta ou sur Lac de Mergozzo, puoi organizzare una giornata in montagna a Macugnaga / Monterosa e <a href=\"esperienze.html\">prenotare le esperienze online</a>.</p>",
                "<p>Même si vous séjournez à l’hôtel ou au camping sur le Lac Majeur, sur le Lac d’Orta ou sur le Lac de Mergozzo, vous pouvez organiser une journée en montagne à Macugnaga / Monterosa et <a href=\"esperienze.html\">réserver les expériences en ligne</a>.</p>",
            ),
            (">Cosa prenotare</a>", ">Que réserver</a>"),
            (">Weekend completo</a>", ">Week-end complet</a>"),
        ],
    )
    add(
        "de",
        "gita-milano-macugnaga.html",
        [
            (
                '"name":"Gita von Mailand a Macugnaga Monte Rosa"',
                '"name":"Tagesausflug von Mailand nach Macugnaga Monte Rosa"',
            ),
            (
                '"description":"Organizza una gita von Mailand a Macugnaga: montagna autentica a circa due ore, einschließlich raggiungibile dal Lago Maggiore. Erlebnisse per famiglie e weekend. Online buchen."',
                '"description":"Planen Sie einen Tagesausflug von Mailand nach Macugnaga: authentische Berge in etwa zwei Stunden, auch erreichbar vom Lago Maggiore. Erlebnisse für Familien und Wochenenden. Online buchen."',
            ),
            (
                '<p class="breadcrumb"><a href="index.html">Start</a> · Gita von Mailand a Macugnaga Monte Rosa</p>\n        <h1>Gita von Mailand a Macugnaga Monte Rosa</h1>\n        <p>Organizza una gita von Mailand a Macugnaga: montagna autentica a circa due ore, einschließlich raggiungibile dal Lago Maggiore. Erlebnisse per famiglie e weekend. Online buchen.</p>',
                '<p class="breadcrumb"><a href="index.html">Start</a> · Tagesausflug von Mailand nach Macugnaga Monte Rosa</p>\n        <h1>Tagesausflug von Mailand nach Macugnaga Monte Rosa</h1>\n        <p>Planen Sie einen Tagesausflug von Mailand nach Macugnaga: authentische Berge in etwa zwei Stunden, auch erreichbar vom Lago Maggiore. Erlebnisse für Familien und Wochenenden. Online buchen.</p>',
            ),
            (
                "<p>Anche se soggiorni in hotel o campeggio am Lago Maggiore, am Ortasee oder am Mergozzo-See, puoi organizzare una giornata in montagna a Macugnaga / Monterosa e <a href=\"esperienze.html\">prenotare le esperienze online</a>.</p>",
                "<p>Auch wenn Sie in Hotel oder Camping am Lago Maggiore, am Ortasee oder am Mergozzo-See übernachten, können Sie einen Bergtag in Macugnaga / Monterosa organisieren und <a href=\"esperienze.html\">Erlebnisse online buchen</a>.</p>",
            ),
            (">Cosa prenotare</a>", ">Was buchen</a>"),
            (">Weekend completo</a>", ">Volles Wochenende</a>"),
        ],
    )

    # senior / coppie FR DE
    for lang, pairs in {
        "fr": [
            ("<h1>Montagna per senior</h1>", "<h1>Montagne pour seniors</h1>"),
            (
                "<p>L’estate a Macugnaga regala respiro aussi nei giorni più caldi della pianura. Passeggiate leggere, visite culturali, forest bathing e momenti di quiete nel Dorf: esperienze a contatto con la natura, con naturalezza e sicurezza, accompagnati da operatori qualificati.</p>",
                "<p>L’été à Macugnaga offre du souffle même les jours les plus chauds de la plaine. Promenades légères, visites culturelles, forest bathing et moments de calme dans le Dorf : expériences nature, avec naturel et sécurité, accompagnés d’opérateurs qualifiés.</p>",
            ),
            (">Scopri le esperienze</a>", ">Découvrir les expériences</a>"),
            (">Scopri il paese</a>", ">Découvrir le village</a>"),
            ("<h1>Montagna per coppie</h1>", "<h1>Montagne pour couples</h1>"),
            (
                "<p>Alba e tramonto sur Rosa, silenzi di villaggio, sapori locali e esperienze da vivere in due.</p>",
                "<p>Aube et crépuscule sur le Rosa, silences de village, saveurs locales et expériences à vivre à deux.</p>",
            ),
            (
                "<li>Attività prenotabili online in pochi click</li>",
                "<li>Activités réservables en ligne en quelques clics</li>",
            ),
        ],
        "de": [
            ("<h1>Montagna per senior</h1>", "<h1>Berge für Senioren</h1>"),
            (
                "<p>L’estate a Macugnaga regala respiro auch nei giorni più caldi della pianura. Passeggiate leggere, visite culturali, forest bathing e momenti di quiete nel Dorf: esperienze a contatto con la natura, con naturalezza e sicurezza, accompagnati da operatori qualificati.</p>",
                "<p>Der Sommer in Macugnaga schenkt Atem auch an den heißesten Tagen der Ebene. Leichte Spaziergänge, Kulturbesuche, Forest Bathing und stille Momente im Dorf: Naturerlebnisse, mit Leichtigkeit und Sicherheit, begleitet von qualifizierten Anbietern.</p>",
            ),
            (">Scopri le esperienze</a>", ">Erlebnisse entdecken</a>"),
            (">Scopri il paese</a>", ">Das Dorf entdecken</a>"),
            ("<h1>Montagna per coppie</h1>", "<h1>Berge für Paare</h1>"),
            (
                "<p>Alba e tramonto am Rosa, silenzi di villaggio, sapori locali e esperienze da vivere in due.</p>",
                "<p>Sonnenaufgang und -untergang am Rosa, Dorfstille, lokale Aromen und Erlebnisse zu zweit.</p>",
            ),
            (
                "<li>Attività prenotabili online in pochi click</li>",
                "<li>Online buchbare Aktivitäten in wenigen Klicks</li>",
            ),
        ],
    }.items():
        add(lang, "senior.html", [p for p in pairs if "senior" in p[0].lower() or "Scopri" in p[0] or "estate" in p[0]])
        add(lang, "coppie.html", [p for p in pairs if "coppie" in p[0].lower() or "Alba" in p[0] or "Attività" in p[0]])

    # FR/DE come-funziona schema
    add(
        "fr",
        "come-funziona.html",
        [
            (
                '"name": "Come prenotare un\'esperienza a Macugnaga"',
                '"name": "Comment réserver une expérience à Macugnaga"',
            ),
            (
                '{"@type": "HowToStep", "name": "Scegli l\'esperienza", "text": "Cerca per date o sfoglia l\'elenco delle attività disponibili su Expériences."}',
                '{"@type": "HowToStep", "name": "Choisissez l\'expérience", "text": "Cherchez par dates ou parcourez la liste des activités disponibles sur Expériences."}',
            ),
            (
                '{"@type": "HowToStep", "name": "Paga in sicurezza", "text": "Completa il pagamento con carte de crédit o PayPal tramite il modulo di prenotazione online."}',
                '{"@type": "HowToStep", "name": "Payez en sécurité", "text": "Finalisez le paiement par carte de crédit ou PayPal via le formulaire de réservation en ligne."}',
            ),
            (
                '{"@type": "HowToStep", "name": "Ricevi conferma", "text": "Ottieni subito l\'email con informazioni e contatti delle guide."}',
                '{"@type": "HowToStep", "name": "Recevez la confirmation", "text": "Recevez immédiatement l\'e-mail avec informations et contacts des guides."}',
            ),
        ],
    )
    add(
        "de",
        "come-funziona.html",
        [
            (
                '"name": "Come prenotare un\'esperienza a Macugnaga"',
                '"name": "So buchen Sie ein Erlebnis in Macugnaga"',
            ),
            (
                '{"@type": "HowToStep", "name": "Scegli l\'esperienza", "text": "Cerca per date o sfoglia l\'elenco delle attività disponibili su Erlebnisse."}',
                '{"@type": "HowToStep", "name": "Erlebnis wählen", "text": "Suchen Sie nach Daten oder durchsuchen Sie die Liste der verfügbaren Aktivitäten unter Erlebnisse."}',
            ),
            (
                '{"@type": "HowToStep", "name": "Paga in sicurezza", "text": "Completa il pagamento con Kreditkarte o PayPal tramite il modulo di prenotazione online."}',
                '{"@type": "HowToStep", "name": "Sicher bezahlen", "text": "Schließen Sie die Zahlung mit Kreditkarte oder PayPal über das Online-Buchungsformular ab."}',
            ),
            (
                '{"@type": "HowToStep", "name": "Ricevi conferma", "text": "Ottieni subito l\'email con informazioni e contatti delle guide."}',
                '{"@type": "HowToStep", "name": "Bestätigung erhalten", "text": "Erhalten Sie sofort die E-Mail mit Informationen und Kontakten der Guides."}',
            ),
        ],
    )

    # FR/DE forest bathing
    add(
        "fr",
        "forest-bathing-macugnaga.html",
        [
            (
                "<p>Tra i boschi della Valle Anzasca, pratiche di immersione nella natura e passeggiate lente aiutano a staccare dalla città. Scopri le proposte benessere prenotabili online e abbina una visita culturale in paese.</p>",
                "<p>Parmi les bois du Val Anzasca, pratiques d’immersion dans la nature et promenades lentes aident à décrocher de la ville. Découvrez les propositions bien-être réservables en ligne et associez une visite culturelle au village.</p>",
            ),
        ],
    )
    add(
        "de",
        "forest-bathing-macugnaga.html",
        [
            (
                "<p>Tra i boschi della Valle Anzasca, pratiche di immersione nella natura e passeggiate lente aiutano a staccare dalla città. Scopri le proposte benessere prenotabili online e abbina una visita culturale in paese.</p>",
                "<p>Unter den Wäldern des Anzasca-Tals helfen Naturimmersionspraktiken und langsame Spaziergänge, von der Stadt abzuschalten. Entdecken Sie online buchbare Wellness-Angebote und verbinden Sie sie mit einem Kulturbesuch im Dorf.</p>",
            ),
        ],
    )


def fix_faq_blocks_attraction_pages() -> None:
    """Translate remaining Italian FAQ Q/A openers on attraction pages."""
    en_casa = [
        ('"name": "Come prenoto la visita alla Walser House Museum?"', '"name": "How do I book a visit to the Walser House Museum?"'),
        (
            '"text": "Puoi prenotare online l\'ingresso direttamente da questa pagina con il pulsante Book now. Paghi in sicurezza e ricevi subito la conferma via email."',
            '"text": "You can book entry online directly from this page with the Book now button. You pay securely and immediately receive confirmation by email."',
        ),
        (
            '"text": "Nella frazione Borca di Macugnaga (VB), Valle Anzasca, ai piedi del Monte Rosa. È ospitata nella casa parrocchiale del XVII secolo."',
            '"text": "In the Borca hamlet of Macugnaga (VB), Anzasca Valley, at the foot of Monte Rosa. It is housed in the 17th-century parish house."',
        ),
        ('"name": "Cosa si vede nel museo?"', '"name": "What can you see in the museum?"'),
        ('"name": "Si può visitare also fuori dagli orari di apertura?"', '"name": "Can you visit outside opening hours?"'),
        ('"name": "Perché prenotare online?"', '"name": "Why book online?"'),
        (
            '"text": "Sì. È pensata per appassionati di storia alpina, famiglie e scuole: un confronto vivo tra la vita di un tempo e quella attuale."',
            '"text": "Yes. It is designed for alpine history enthusiasts, families and schools: a living comparison between past and present life."',
        ),
        (
            '"text": "Sì: in circa un\'ora conosci l\'anima walser di Macugnaga. Si abbina a passeggiate, miniera d\'oro e impianti — perfetta in un weekend Monte Rosa o in una gita in montagna from Milan, Varese o Novara."',
            '"text": "Yes: in about an hour you discover the Walser soul of Macugnaga. It pairs well with walks, the gold mine and lifts — perfect on a Monte Rosa weekend or a mountain day trip from Milan, Varese or Novara."',
        ),
    ]
    add("en", "casa-museo-walser.html", en_casa)

    en_miniera = [
        ('"name": "Come prenoto la visita alla Gold mine?"', '"name": "How do I book a visit to the gold mine?"'),
        (
            '"text": "Puoi prenotare online direttamente da questa pagina con il pulsante Book now. Completi il modulo di prenotazione online, paghi in sicurezza e ricevi subito la conferma via email."',
            '"text": "You can book online directly from this page with the Book now button. Complete the online booking form, pay securely and immediately receive confirmation by email."',
        ),
        (
            '"text": "Sì. The visit si svolge su un unico piano, accessibile also a diversamente abili e bambini in passeggino."',
            '"text": "Yes. The visit takes place on a single level, also accessible to people with disabilities and children in pushchairs."',
        ),
        ('"name": "Perché prenotare online?"', '"name": "Why book online?"'),
        (
            '"text": "È la prima gold mine sotterranea visitabile in Italia: un viaggio nella storia mineraria del Monte Rosa, complementare a passeggiate, Walser House e impianti."',
            '"text": "It is the first underground gold mine open to visitors in Italy: a journey into Monte Rosa mining history, complementary to walks, Walser House and lifts."',
        ),
        (
            '"text": "Sì: percorso in piano, accessibile also con passeggino, durata di circa 45 minuti. Si abbina a Walser House e passeggiate — ideale in un weekend Macugnaga Monte Rosa o in una gita in montagna from Milan, Varese o Novara."',
            '"text": "Yes: a level route, also accessible with a pushchair, lasting about 45 minutes. It pairs with Walser House and walks — ideal on a Macugnaga Monte Rosa weekend or a mountain day trip from Milan, Varese or Novara."',
        ),
    ]
    add("en", "miniera-oro.html", en_miniera)

    add(
        "en",
        "funivia-seggiovia.html",
        [
            ('"name": "Quali ski lifts ci sono a Macugnaga?"', '"name": "Which ski lifts are there in Macugnaga?"'),
            (
                '"name": "Come abbinare impianti e weekend a Macugnaga?"',
                '"name": "How to combine lifts and a weekend in Macugnaga?"',
            ),
            (
                '"text": "Sì: on portale Macugnaga Booking puoi prenotare online i biglietti della seggiovia Pecetto–Burki–Belvedere e della funivia Staffa–Alpe Bill (pagamento on posto). Orari e stato impianti restano aggiornati also on sito ufficiale della società funivie."',
                '"text": "Yes: on the Macugnaga Booking portal you can book online tickets for the Pecetto–Burki–Belvedere chairlift and the Staffa–Alpe Bill cableway (pay on site). Opening times and lift status are also updated on the official lift company website."',
            ),
            ('>Portale di prenotazione</p>', '>Booking portal</p>'),
            ('>Booking portal</p>', '>Booking portal</p>'),  # noop if already fixed
        ],
    )


def main() -> None:
    apply_fr_de_mirrors()
    fix_faq_blocks_attraction_pages()
    total = 0
    for (lang, rel), pairs in sorted(FIXES.items()):
        path = ROOT / lang / rel
        if not path.exists():
            print(f"MISSING {path}")
            continue
        text = path.read_text(encoding="utf-8")
        original = text
        n = 0
        for old, new in pairs:
            if old in text:
                c = text.count(old)
                text = text.replace(old, new)
                n += c
            elif old != new:
                # try softer match hint
                pass
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            print(f"{lang}/{rel}: {n} replacements")
            total += n
        else:
            print(f"{lang}/{rel}: no change ({len(pairs)} attempted)")
    print(f"TOTAL replacements: {total}")


if __name__ == "__main__":
    main()
