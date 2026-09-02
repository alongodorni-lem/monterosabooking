#!/usr/bin/env python3
"""Build ritorno-a-scuola landing pages (IT/EN/FR/DE) + Mailchimp newsletter."""
from __future__ import annotations

import html
import zipfile
from pathlib import Path

from _mailchimp_footer import GROTTA_HOME_URL, footer_lem_block

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.macugnagabooking.it"
SLUG = "vivi-la-montagna-prima-del-ritorno-a-scuola.html"
DATE_TO = "2026-09-14"
LASTMOD = "2026-09-02"
CSS_V = "25"
I18N_V = "13"
PARTIALS_V = "24"
MAIN_V = "3"
LIST_V = "23"

GREEN = "#4a6b3e"
GREEN_DARK = "#2f4522"
CREAM = "#f7f5f0"
MUTED = "#5c5c5c"
ACCENT_BTN = "#72872B"

MAIL = ROOT / "assets" / "mailchimp"
NL_BASE = "newsletter-ritorno-a-scuola-settembre-2026-codice-personalizzato"

COPY = {
    "it": {
        "lang": "it",
        "dir": "",
        "prefix": "",
        "og_locale": "it_IT",
        "title": "Vivi la montagna prima del ritorno a scuola — Esperienze fino al 14 settembre | Macugnaga Booking",
        "meta_desc": "Vivi la montagna prima del ritorno a scuola a Macugnaga Monte Rosa: esperienze per tutta la famiglia prenotabili online da oggi fino al 14 settembre 2026. Giornata, weekend o ultima vacanza prima della riapertura delle scuole.",
        "og_title": "Vivi la montagna prima del ritorno a scuola | Macugnaga Monte Rosa",
        "og_desc": "Esperienze ai piedi del Monte Rosa per tutta la famiglia, da oggi fino al 14 settembre 2026 — prenota online su Macugnaga Booking.",
        "tw_title": "Vivi la montagna prima del ritorno a scuola — Fino al 14 settembre | Macugnaga",
        "crumb_label": "Ritorno a scuola",
        "h1": "Vivi la montagna prima del ritorno a scuola",
        "hero_lead": "Esperienze ai piedi del Monte Rosa per tutta la famiglia. Per una giornata, un weekend o per l’ultima vacanza prima della riapertura delle scuole.",
        "eyebrow1": "Prima della scuola",
        "h2_1": "Aria di montagna, esperienze per tutti",
        "p1a": "Prima della riapertura delle scuole, Macugnaga offre <strong>clima alpino</strong>, sentieri tra i larici e proposte pensate per famiglie, adulti e bambini ai piedi del Monte Rosa.",
        "p1b": "Fino al <strong>14 settembre</strong> il portale di prenotazione raccoglie le esperienze disponibili online: natura, cultura, ricerca dell’oro, favole Walser, miniera e attività soft.",
        "li1": "Operatori autorizzati e guide qualificate",
        "li2": "Prenotazione online con conferma immediata",
        "li3": "Idee per giornata, weekend o ultima vacanza",
        "eyebrow2": "Vicino alle città e ai laghi",
        "h2_2": "La montagna vera, a portata di strada",
        "p2a": "Macugnaga è raggiungibile in circa 1,5–2,5 ore da <strong>Milano</strong>, <strong>Varese</strong>, <strong>Novara</strong> e dal <strong>Lago Maggiore</strong> — e anche da <strong>Orta</strong>, <strong>Mergozzo</strong> e Torino.",
        "p2b": "Perfetta come <a href=\"fuga-citta.html\">fuga dalla città</a> o come giornata in montagna se soggiorni in hotel o campeggio sui laghi: aria fresca, paese alpino e panorami sul Monte Rosa senza lunghi trasferimenti.",
        "btn_fuga": "Fuga dalla città",
        "btn_fam": "Montagna con i bambini",
        "eyebrow3": "Soggiorno con pernottamento",
        "h2_3": "Dormire e risvegliarsi ai piedi del Rosa…",
        "p3a": "Fino al 14 settembre un <strong>soggiorno con pernottamento</strong> rende l’ultima vacanza più completa: alba e tramonto sul Monte Rosa, una o due esperienze prenotate online, passeggiate in paese e cucina locale.",
        "p3b": "Scegli hotel, B&amp;B o casa vacanza, poi prenota le attività qui sotto. Guida pratica su <a href=\"weekend.html\">Idee weekend</a>.",
        "btn_week": "Organizza soggiorno",
        "btn_sleep": "Dove dormire",
        "eyebrow4": "Prenota online",
        "h2_4": "Esperienze prenotabili fino al 14 settembre",
        "p4": "Elenco aggiornato delle attività con disponibilità da <strong>oggi</strong> fino al <strong>14 settembre 2026</strong>. Scegli data e posti, paga online e ricevi subito conferma con i contatti delle guide. Per il catalogo completo vedi <a href=\"esperienze.html\">tutte le esperienze</a>.",
        "list_aria": "Esperienze prenotabili fino al 14 settembre",
        "list_loading": "Caricamento esperienze…",
        "ns_mine": "Miniera d’oro della Guia",
        "ns_walser": "Casa Museo Walser di Borca",
        "ns_all": "Tutte le esperienze prenotabili",
        "ns_week": "Idee weekend a Macugnaga",
        "ns_fam": "Montagna con i bambini",
        "faq_h2": "Domande frequenti sul ritorno a scuola a Macugnaga",
        "faq1_q": "Quali esperienze posso prenotare fino al 14 settembre a Macugnaga?",
        "faq1_a": "L’elenco in questa pagina mostra le esperienze del portale di prenotazione con disponibilità da oggi fino al 14 settembre 2026: boschi e natura, <a href=\"casa-museo-walser.html\">Casa Museo Walser</a>, <a href=\"miniera-oro.html\">miniera d’oro</a>, ricerca dell’oro, favole Walser e attività per famiglie ai piedi del Monte Rosa.",
        "faq2_q": "Macugnaga è adatta per l’ultima vacanza o un weekend prima della scuola?",
        "faq2_a": "Sì: clima fresco alpino a poca distanza da Milano, Varese, Novara e dai laghi Maggiore, d’Orta e di Mergozzo. Ideale per una giornata, un weekend o l’ultima vacanza prima della riapertura delle scuole. Vedi anche <a href=\"fuga-citta.html\">Fuga dalla città</a>.",
        "faq3_q": "Come organizzare un weekend con pernottamento?",
        "faq3_a": "Alloggio a Macugnaga, una o due esperienze prenotate online e passeggiate in paese. Guida su <a href=\"weekend.html\">Weekend</a> e elenco <a href=\"https://macugnaga-monterosa.it/contenuti/306635/dove-dormire\" target=\"_blank\" rel=\"noopener\">dove dormire</a>.",
        "note": "Informazioni, prezzi e disponibilità del portale di prenotazione sono indicati dai gestori. Dopo la prenotazione riceverai i contatti degli organizzatori. <a href=\"https://www.raccontidigitali.it\" target=\"_blank\" rel=\"noopener\">Lem s.r.l.</a> non è responsabile della gestione delle attività. <a href=\"credits.html\">Maggiori informazioni</a>",
        "skip": "Vai al contenuto",
        "nav": [
            ("index.html", "Home"),
            ("esperienze.html", "Esperienze"),
            ("casa-museo-walser.html", "Casa Walser"),
            ("miniera-oro.html", "Miniera d’oro"),
            ("funivia-seggiovia.html", "Impianti"),
            ("mappa.html", "Mappa"),
            ("weekend.html", "Weekend"),
            ("scopri-macugnaga.html", "Macugnaga"),
            ("come-funziona.html", "Come funziona"),
            ("faq.html", "FAQ"),
        ],
        "nav_cta": "Prenota online",
        "nav_aria": "Navigazione principale",
        "crumb_home": "Home",
        "crumb_exp": "Esperienze",
        "cookie_aria": "Informativa cookie",
        "cookie_text": "Questo sito utilizza cookie tecnici necessari al funzionamento e servizi di terze parti per la prenotazione online e i font. <a href=\"privacy.html\">Privacy e cookie</a>",
        "cookie_ok": "Accetta",
        "cookie_ess": "Solo essenziali",
        "img_alt_hero": "Veduta del Dorf di Macugnaga con case walser e Monte Rosa",
        "img_alt_drone": "Macugnaga e Monte Rosa visti dall’alto",
        "img_alt_ossola": "Paesaggio di Macugnaga in Valle Anzasca",
        "bc_home": "Home",
        "bc_exp": "Esperienze",
        "bc_page": "Vivi la montagna prima del ritorno a scuola",
        "web_name": "Vivi la montagna prima del ritorno a scuola — Esperienze fino al 14 settembre a Macugnaga",
        "web_desc": "Esperienze prenotabili online a Macugnaga Monte Rosa da oggi fino al 14 settembre 2026, per tutta la famiglia ai piedi del Monte Rosa.",
        "list_name": "Esperienze prenotabili a Macugnaga fino al 14 settembre",
        "list_desc": "Attività in montagna prenotabili online a Macugnaga Monte Rosa fino al 14 settembre 2026.",
        "translation_note": False,
        "in_language": "it",
    },
    "en": {
        "lang": "en",
        "dir": "en/",
        "prefix": "../",
        "og_locale": "en_GB",
        "title": "Live the mountains before back to school — Experiences through 14 September | Macugnaga Booking",
        "meta_desc": "Live the mountains before back to school in Macugnaga Monte Rosa: family experiences bookable online from today through 14 September 2026. A day, a weekend, or the last holiday before school reopens.",
        "og_title": "Live the mountains before back to school | Macugnaga Monte Rosa",
        "og_desc": "Family experiences at the foot of Monte Rosa, from today through 14 September 2026 — book online on Macugnaga Booking.",
        "tw_title": "Live the mountains before back to school — Through 14 September | Macugnaga",
        "crumb_label": "Back to school",
        "h1": "Live the mountains before back to school",
        "hero_lead": "Experiences at the foot of Monte Rosa for the whole family. For a day, a weekend, or the last holiday before school reopens.",
        "eyebrow1": "Before school starts",
        "h2_1": "Mountain air, experiences for everyone",
        "p1a": "Before school reopens, Macugnaga offers an <strong>alpine climate</strong>, trails among larches and ideas for families, adults and children at the foot of Monte Rosa.",
        "p1b": "Through <strong>14 September</strong> the booking portal gathers the experiences available online: nature, culture, gold panning, Walser tales, the gold mine and gentle activities.",
        "li1": "Authorised operators and qualified guides",
        "li2": "Online booking with instant confirmation",
        "li3": "Ideas for a day, a weekend or a last holiday",
        "eyebrow2": "Close to cities and lakes",
        "h2_2": "Real mountains, within easy reach",
        "p2a": "Macugnaga is about 1.5–2.5 hours from <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> and <strong>Lake Maggiore</strong> — and also from <strong>Orta</strong>, <strong>Mergozzo</strong> and Turin.",
        "p2b": "Perfect as a <a href=\"fuga-citta.html\">city escape</a> or a mountain day if you stay in a hotel or campsite by the lakes: fresh air, alpine village and Monte Rosa views without long transfers.",
        "btn_fuga": "City escape",
        "btn_fam": "Mountains with children",
        "eyebrow3": "Stay overnight",
        "h2_3": "Sleep and wake up at the foot of the Rosa…",
        "p3a": "Through 14 September an <strong>overnight stay</strong> makes the last holiday more complete: sunrise and sunset on Monte Rosa, one or two experiences booked online, village walks and local food.",
        "p3b": "Choose a hotel, B&amp;B or holiday home, then book the activities below. Practical guide on <a href=\"weekend.html\">Weekend ideas</a>.",
        "btn_week": "Plan your stay",
        "btn_sleep": "Where to stay",
        "eyebrow4": "Book online",
        "h2_4": "Bookable experiences through 14 September",
        "p4": "Updated list of activities with availability from <strong>today</strong> through <strong>14 September 2026</strong>. Choose date and places, pay online and receive instant confirmation with guide contacts. For the full catalogue see <a href=\"esperienze.html\">all experiences</a>.",
        "list_aria": "Bookable experiences through 14 September",
        "list_loading": "Loading experiences…",
        "ns_mine": "Guia gold mine",
        "ns_walser": "Walser House Museum in Borca",
        "ns_all": "All bookable experiences",
        "ns_week": "Weekend ideas in Macugnaga",
        "ns_fam": "Mountains with children",
        "faq_h2": "Frequently asked questions about Macugnaga before back to school",
        "faq1_q": "Which experiences can I book through 14 September in Macugnaga?",
        "faq1_a": "The list on this page shows booking-portal experiences with availability from today through 14 September 2026: woods and nature, <a href=\"casa-museo-walser.html\">Walser House Museum</a>, <a href=\"miniera-oro.html\">gold mine</a>, gold panning, Walser tales and family activities at the foot of Monte Rosa.",
        "faq2_q": "Is Macugnaga good for a last holiday or weekend before school?",
        "faq2_a": "Yes: cool alpine climate a short trip from Milan, Varese, Novara and Lakes Maggiore, Orta and Mergozzo. Ideal for a day, a weekend or the last holiday before school reopens. See also <a href=\"fuga-citta.html\">City escape</a>.",
        "faq3_q": "How to plan a weekend with overnight stay?",
        "faq3_a": "Stay in Macugnaga, book one or two experiences online and enjoy village walks. Guide on <a href=\"weekend.html\">Weekend</a> and list of <a href=\"https://macugnaga-monterosa.it/contenuti/306635/dove-dormire\" target=\"_blank\" rel=\"noopener\">where to stay</a>.",
        "note": "Information, prices and availability on the booking portal are provided by the operators. After booking you will receive the organisers’ contacts. <a href=\"https://www.raccontidigitali.it\" target=\"_blank\" rel=\"noopener\">Lem s.r.l.</a> is not responsible for running the activities. <a href=\"credits.html\">More information</a>",
        "skip": "Skip to content",
        "nav": [
            ("index.html", "Home"),
            ("esperienze.html", "Experiences"),
            ("casa-museo-walser.html", "Walser House"),
            ("miniera-oro.html", "Gold mine"),
            ("funivia-seggiovia.html", "Lifts"),
            ("mappa.html", "Map"),
            ("weekend.html", "Weekend"),
            ("scopri-macugnaga.html", "Macugnaga"),
            ("come-funziona.html", "How it works"),
            ("faq.html", "FAQ"),
        ],
        "nav_cta": "Book online",
        "nav_aria": "Main navigation",
        "crumb_home": "Home",
        "crumb_exp": "Experiences",
        "cookie_aria": "Cookie notice",
        "cookie_text": "This site uses technical cookies required for operation and third-party services for online booking and fonts. <a href=\"privacy.html\">Privacy and cookies</a>",
        "cookie_ok": "Accept",
        "cookie_ess": "Essential only",
        "img_alt_hero": "View of Macugnaga Dorf with Walser houses and Monte Rosa",
        "img_alt_drone": "Macugnaga and Monte Rosa from above",
        "img_alt_ossola": "Macugnaga landscape in the Anzasca Valley",
        "bc_home": "Home",
        "bc_exp": "Experiences",
        "bc_page": "Live the mountains before back to school",
        "web_name": "Live the mountains before back to school — Experiences through 14 September in Macugnaga",
        "web_desc": "Bookable online experiences in Macugnaga Monte Rosa from today through 14 September 2026, for the whole family at the foot of Monte Rosa.",
        "list_name": "Bookable experiences in Macugnaga through 14 September",
        "list_desc": "Mountain activities bookable online in Macugnaga Monte Rosa through 14 September 2026.",
        "translation_note": True,
        "in_language": "en",
    },
    "fr": {
        "lang": "fr",
        "dir": "fr/",
        "prefix": "../",
        "og_locale": "fr_FR",
        "title": "Vivez la montagne avant la rentrée — Expériences jusqu’au 14 septembre | Macugnaga Booking",
        "meta_desc": "Vivez la montagne avant la rentrée à Macugnaga Mont Rose : expériences pour toute la famille réservables en ligne d’aujourd’hui au 14 septembre 2026. Une journée, un week-end ou les dernières vacances avant la rentrée scolaire.",
        "og_title": "Vivez la montagne avant la rentrée | Macugnaga Mont Rose",
        "og_desc": "Expériences au pied du Mont Rose pour toute la famille, d’aujourd’hui au 14 septembre 2026 — réservez en ligne sur Macugnaga Booking.",
        "tw_title": "Vivez la montagne avant la rentrée — Jusqu’au 14 septembre | Macugnaga",
        "crumb_label": "Avant la rentrée",
        "h1": "Vivez la montagne avant la rentrée",
        "hero_lead": "Expériences au pied du Mont Rose pour toute la famille. Pour une journée, un week-end ou les dernières vacances avant la rentrée scolaire.",
        "eyebrow1": "Avant l’école",
        "h2_1": "Air de montagne, expériences pour tous",
        "p1a": "Avant la rentrée scolaire, Macugnaga offre un <strong>climat alpin</strong>, des sentiers parmi les mélèzes et des propositions pour familles, adultes et enfants au pied du Mont Rose.",
        "p1b": "Jusqu’au <strong>14 septembre</strong>, le portail de réservation rassemble les expériences disponibles en ligne : nature, culture, recherche de l’or, contes walser, mine d’or et activités douces.",
        "li1": "Opérateurs autorisés et guides qualifiés",
        "li2": "Réservation en ligne avec confirmation immédiate",
        "li3": "Idées pour une journée, un week-end ou de dernières vacances",
        "eyebrow2": "Près des villes et des lacs",
        "h2_2": "La vraie montagne, à portée de route",
        "p2a": "Macugnaga est accessible en environ 1,5–2,5 heures depuis <strong>Milan</strong>, <strong>Varèse</strong>, <strong>Novare</strong> et le <strong>Lac Majeur</strong> — et aussi depuis <strong>Orta</strong>, <strong>Mergozzo</strong> et Turin.",
        "p2b": "Parfaite comme <a href=\"fuga-citta.html\">échappée de la ville</a> ou journée en montagne si vous séjournez à l’hôtel ou au camping au bord des lacs : air frais, village alpin et panoramas sur le Mont Rose sans longs trajets.",
        "btn_fuga": "Échappée de la ville",
        "btn_fam": "Montagne avec les enfants",
        "eyebrow3": "Séjour avec nuitée",
        "h2_3": "Dormir et se réveiller au pied du Rosa…",
        "p3a": "Jusqu’au 14 septembre, un <strong>séjour avec nuitée</strong> rend les dernières vacances plus complètes : lever et coucher de soleil sur le Mont Rose, une ou deux expériences réservées en ligne, promenades au village et cuisine locale.",
        "p3b": "Choisissez hôtel, B&amp;B ou maison de vacances, puis réservez les activités ci-dessous. Guide pratique sur <a href=\"weekend.html\">Idées week-end</a>.",
        "btn_week": "Organiser le séjour",
        "btn_sleep": "Où dormir",
        "eyebrow4": "Réservez en ligne",
        "h2_4": "Expériences réservables jusqu’au 14 septembre",
        "p4": "Liste à jour des activités disponibles d’<strong>aujourd’hui</strong> au <strong>14 septembre 2026</strong>. Choisissez date et places, payez en ligne et recevez aussitôt la confirmation avec les contacts des guides. Pour le catalogue complet, voir <a href=\"esperienze.html\">toutes les expériences</a>.",
        "list_aria": "Expériences réservables jusqu’au 14 septembre",
        "list_loading": "Chargement des expériences…",
        "ns_mine": "Mine d’or de la Guia",
        "ns_walser": "Maison Musée Walser de Borca",
        "ns_all": "Toutes les expériences réservables",
        "ns_week": "Idées week-end à Macugnaga",
        "ns_fam": "Montagne avec les enfants",
        "faq_h2": "Questions fréquentes sur Macugnaga avant la rentrée",
        "faq1_q": "Quelles expériences puis-je réserver jusqu’au 14 septembre à Macugnaga ?",
        "faq1_a": "La liste de cette page montre les expériences du portail de réservation disponibles d’aujourd’hui au 14 septembre 2026 : forêts et nature, <a href=\"casa-museo-walser.html\">Maison Musée Walser</a>, <a href=\"miniera-oro.html\">mine d’or</a>, recherche de l’or, contes walser et activités familles au pied du Mont Rose.",
        "faq2_q": "Macugnaga convient-elle pour de dernières vacances ou un week-end avant l’école ?",
        "faq2_a": "Oui : climat alpin frais à peu de distance de Milan, Varèse, Novare et des lacs Majeur, d’Orta et de Mergozzo. Idéal pour une journée, un week-end ou les dernières vacances avant la rentrée. Voir aussi <a href=\"fuga-citta.html\">Échappée de la ville</a>.",
        "faq3_q": "Comment organiser un week-end avec nuitée ?",
        "faq3_a": "Hébergement à Macugnaga, une ou deux expériences réservées en ligne et promenades au village. Guide sur <a href=\"weekend.html\">Week-end</a> et liste <a href=\"https://macugnaga-monterosa.it/contenuti/306635/dove-dormire\" target=\"_blank\" rel=\"noopener\">où dormir</a>.",
        "note": "Informations, prix et disponibilités du portail de réservation sont indiqués par les gestionnaires. Après la réservation vous recevrez les contacts des organisateurs. <a href=\"https://www.raccontidigitali.it\" target=\"_blank\" rel=\"noopener\">Lem s.r.l.</a> n’est pas responsable de la gestion des activités. <a href=\"credits.html\">Plus d’informations</a>",
        "skip": "Aller au contenu",
        "nav": [
            ("index.html", "Accueil"),
            ("esperienze.html", "Expériences"),
            ("casa-museo-walser.html", "Maison Walser"),
            ("miniera-oro.html", "Mine d’or"),
            ("funivia-seggiovia.html", "Remontées"),
            ("mappa.html", "Carte"),
            ("weekend.html", "Week-end"),
            ("scopri-macugnaga.html", "Macugnaga"),
            ("come-funziona.html", "Comment ça marche"),
            ("faq.html", "FAQ"),
        ],
        "nav_cta": "Réserver en ligne",
        "nav_aria": "Navigation principale",
        "crumb_home": "Accueil",
        "crumb_exp": "Expériences",
        "cookie_aria": "Information cookies",
        "cookie_text": "Ce site utilise des cookies techniques nécessaires au fonctionnement et des services tiers pour la réservation en ligne et les polices. <a href=\"privacy.html\">Confidentialité et cookies</a>",
        "cookie_ok": "Accepter",
        "cookie_ess": "Essentiels seulement",
        "img_alt_hero": "Vue du Dorf de Macugnaga avec maisons walser et Mont Rose",
        "img_alt_drone": "Macugnaga et le Mont Rose vus du ciel",
        "img_alt_ossola": "Paysage de Macugnaga dans le Val Anzasca",
        "bc_home": "Accueil",
        "bc_exp": "Expériences",
        "bc_page": "Vivez la montagne avant la rentrée",
        "web_name": "Vivez la montagne avant la rentrée — Expériences jusqu’au 14 septembre à Macugnaga",
        "web_desc": "Expériences réservables en ligne à Macugnaga Mont Rose d’aujourd’hui au 14 septembre 2026, pour toute la famille au pied du Mont Rose.",
        "list_name": "Expériences réservables à Macugnaga jusqu’au 14 septembre",
        "list_desc": "Activités de montagne réservables en ligne à Macugnaga Mont Rose jusqu’au 14 septembre 2026.",
        "translation_note": True,
        "in_language": "fr",
    },
    "de": {
        "lang": "de",
        "dir": "de/",
        "prefix": "../",
        "og_locale": "de_DE",
        "title": "Erlebe die Berge vor dem Schulstart — Erlebnisse bis 14. September | Macugnaga Booking",
        "meta_desc": "Erlebe die Berge vor dem Schulstart in Macugnaga Monte Rosa: Familienerlebnisse online buchbar von heute bis 14. September 2026. Für einen Tag, ein Wochenende oder den letzten Urlaub vor Schulbeginn.",
        "og_title": "Erlebe die Berge vor dem Schulstart | Macugnaga Monte Rosa",
        "og_desc": "Erlebnisse am Fuß des Monte Rosa für die ganze Familie, von heute bis 14. September 2026 — online buchen auf Macugnaga Booking.",
        "tw_title": "Erlebe die Berge vor dem Schulstart — Bis 14. September | Macugnaga",
        "crumb_label": "Vor dem Schulstart",
        "h1": "Erlebe die Berge vor dem Schulstart",
        "hero_lead": "Erlebnisse am Fuß des Monte Rosa für die ganze Familie. Für einen Tag, ein Wochenende oder den letzten Urlaub vor der Schulöffnung.",
        "eyebrow1": "Vor der Schule",
        "h2_1": "Bergluft, Erlebnisse für alle",
        "p1a": "Vor dem Schulbeginn bietet Macugnaga <strong>alpines Klima</strong>, Wege zwischen Lärchen und Angebote für Familien, Erwachsene und Kinder am Fuß des Monte Rosa.",
        "p1b": "Bis zum <strong>14. September</strong> bündelt das Buchungsportal die online verfügbaren Erlebnisse: Natur, Kultur, Goldwaschen, Walser-Märchen, Goldbergwerk und sanfte Aktivitäten.",
        "li1": "Autorisierte Anbieter und qualifizierte Guides",
        "li2": "Online-Buchung mit sofortiger Bestätigung",
        "li3": "Ideen für Tag, Wochenende oder letzten Urlaub",
        "eyebrow2": "Nah an Städten und Seen",
        "h2_2": "Echte Berge, gut erreichbar",
        "p2a": "Macugnaga ist in etwa 1,5–2,5 Stunden von <strong>Mailand</strong>, <strong>Varese</strong>, <strong>Novara</strong> und dem <strong>Lago Maggiore</strong> erreichbar — und auch von <strong>Orta</strong>, <strong>Mergozzo</strong> und Turin.",
        "p2b": "Perfekt als <a href=\"fuga-citta.html\">Stadtflucht</a> oder Bergtag, wenn Sie in Hotel oder Camping an den Seen übernachten: frische Luft, Alpendorf und Monte-Rosa-Panoramen ohne lange Anreise.",
        "btn_fuga": "Stadtflucht",
        "btn_fam": "Berge mit Kindern",
        "eyebrow3": "Übernachtung",
        "h2_3": "Schlafen und erwachen am Fuß des Rosa…",
        "p3a": "Bis zum 14. September macht eine <strong>Übernachtung</strong> den letzten Urlaub vollständiger: Sonnenauf- und -untergang am Monte Rosa, ein oder zwei online gebuchte Erlebnisse, Dorfspaziergänge und lokale Küche.",
        "p3b": "Wählen Sie Hotel, B&amp;B oder Ferienhaus und buchen Sie dann die Aktivitäten unten. Praktischer Leitfaden unter <a href=\"weekend.html\">Wochenend-Ideen</a>.",
        "btn_week": "Aufenthalt planen",
        "btn_sleep": "Unterkunft",
        "eyebrow4": "Online buchen",
        "h2_4": "Buchbare Erlebnisse bis 14. September",
        "p4": "Aktuelle Liste der Aktivitäten mit Verfügbarkeit von <strong>heute</strong> bis zum <strong>14. September 2026</strong>. Datum und Plätze wählen, online bezahlen und sofort Bestätigung mit Guide-Kontakten erhalten. Für den vollständigen Katalog siehe <a href=\"esperienze.html\">alle Erlebnisse</a>.",
        "list_aria": "Buchbare Erlebnisse bis 14. September",
        "list_loading": "Erlebnisse werden geladen…",
        "ns_mine": "Goldmine Guia",
        "ns_walser": "Walser-Hausmuseum in Borca",
        "ns_all": "Alle buchbaren Erlebnisse",
        "ns_week": "Wochenend-Ideen in Macugnaga",
        "ns_fam": "Berge mit Kindern",
        "faq_h2": "Häufige Fragen zu Macugnaga vor dem Schulstart",
        "faq1_q": "Welche Erlebnisse kann ich bis 14. September in Macugnaga buchen?",
        "faq1_a": "Die Liste auf dieser Seite zeigt Erlebnisse des Buchungsportals mit Verfügbarkeit von heute bis 14. September 2026: Wälder und Natur, <a href=\"casa-museo-walser.html\">Walser-Hausmuseum</a>, <a href=\"miniera-oro.html\">Goldmine</a>, Goldwaschen, Walser-Märchen und Familienaktivitäten am Fuß des Monte Rosa.",
        "faq2_q": "Eignet sich Macugnaga für den letzten Urlaub oder ein Wochenende vor der Schule?",
        "faq2_a": "Ja: kühles Alpenklima nahe Mailand, Varese, Novara und den Seen Maggiore, Orta und Mergozzo. Ideal für einen Tag, ein Wochenende oder den letzten Urlaub vor Schulbeginn. Siehe auch <a href=\"fuga-citta.html\">Stadtflucht</a>.",
        "faq3_q": "Wie plane ich ein Wochenende mit Übernachtung?",
        "faq3_a": "Unterkunft in Macugnaga, ein oder zwei online gebuchte Erlebnisse und Dorfspaziergänge. Leitfaden unter <a href=\"weekend.html\">Wochenende</a> und Liste <a href=\"https://macugnaga-monterosa.it/contenuti/306635/dove-dormire\" target=\"_blank\" rel=\"noopener\">Unterkünfte</a>.",
        "note": "Informationen, Preise und Verfügbarkeit des Buchungsportals werden von den Anbietern angegeben. Nach der Buchung erhalten Sie die Kontakte der Organisatoren. <a href=\"https://www.raccontidigitali.it\" target=\"_blank\" rel=\"noopener\">Lem s.r.l.</a> ist nicht für die Durchführung der Aktivitäten verantwortlich. <a href=\"credits.html\">Weitere Informationen</a>",
        "skip": "Zum Inhalt springen",
        "nav": [
            ("index.html", "Home"),
            ("esperienze.html", "Erlebnisse"),
            ("casa-museo-walser.html", "Walser-Haus"),
            ("miniera-oro.html", "Goldmine"),
            ("funivia-seggiovia.html", "Bahnen"),
            ("mappa.html", "Karte"),
            ("weekend.html", "Wochenende"),
            ("scopri-macugnaga.html", "Macugnaga"),
            ("come-funziona.html", "So funktioniert’s"),
            ("faq.html", "FAQ"),
        ],
        "nav_cta": "Online buchen",
        "nav_aria": "Hauptnavigation",
        "crumb_home": "Home",
        "crumb_exp": "Erlebnisse",
        "cookie_aria": "Cookie-Hinweis",
        "cookie_text": "Diese Website verwendet technisch notwendige Cookies und Drittanbieter-Dienste für Online-Buchung und Schriftarten. <a href=\"privacy.html\">Datenschutz und Cookies</a>",
        "cookie_ok": "Akzeptieren",
        "cookie_ess": "Nur Essenzielle",
        "img_alt_hero": "Blick auf das Dorf Macugnaga mit Walser-Häusern und Monte Rosa",
        "img_alt_drone": "Macugnaga und Monte Rosa von oben",
        "img_alt_ossola": "Landschaft von Macugnaga im Anzascatal",
        "bc_home": "Home",
        "bc_exp": "Erlebnisse",
        "bc_page": "Erlebe die Berge vor dem Schulstart",
        "web_name": "Erlebe die Berge vor dem Schulstart — Erlebnisse bis 14. September in Macugnaga",
        "web_desc": "Online buchbare Erlebnisse in Macugnaga Monte Rosa von heute bis 14. September 2026, für die ganze Familie am Fuß des Monte Rosa.",
        "list_name": "Buchbare Erlebnisse in Macugnaga bis 14. September",
        "list_desc": "Bergaktivitäten online buchbar in Macugnaga Monte Rosa bis 14. September 2026.",
        "translation_note": True,
        "in_language": "de",
    },
}


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def abs_url(lang: str) -> str:
    d = COPY[lang]["dir"]
    return f"{SITE}/{d}{SLUG}"


def nav_html(c: dict) -> str:
    links = "".join(f'\n        <a href="{href}">{label}</a>' for href, label in c["nav"])
    links += f'\n        <a class="nav-cta" href="esperienze.html">{c["nav_cta"]}</a>'
    return links


def landing_html(lang: str) -> str:
    c = COPY[lang]
    p = c["prefix"]
    url = abs_url(lang)
    home_item = f"{SITE}/{c['dir']}" if c["dir"] else f"{SITE}/"
    exp_item = f"{SITE}/{c['dir']}esperienze.html"
    note_block = (
        '  <p class="footer-translation-note container" hidden>Automatic translation from the official Italian version</p>\n'
        if c["translation_note"]
        else ""
    )
    return f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
  <meta charset="utf-8">
  <script src="{p}js/lang-pref.js?v=2"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{c['title']}</title>
  <meta name="description" content="{esc(c['meta_desc'])}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="it" href="{abs_url('it')}">
  <link rel="alternate" hreflang="en" href="{abs_url('en')}">
  <link rel="alternate" hreflang="fr" href="{abs_url('fr')}">
  <link rel="alternate" hreflang="de" href="{abs_url('de')}">
  <link rel="alternate" hreflang="x-default" href="{abs_url('it')}">
  <meta property="og:title" content="{esc(c['og_title'])}">
  <meta property="og:description" content="{esc(c['og_desc'])}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="{c['og_locale']}">
  <meta property="og:site_name" content="Macugnaga Booking – Esperienze ai piedi del Monte Rosa">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(c['tw_title'])}">
  <meta name="twitter:description" content="{esc(c['og_desc'])}">
  <meta name="twitter:image" content="{SITE}/assets/web/landing-agosto-aria-fresca.jpg">
  <meta name="twitter:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/web/landing-agosto-aria-fresca.jpg">
  <meta name="geo.region" content="IT-VB">
  <meta name="geo.placename" content="Macugnaga">
  <meta name="geo.position" content="45.9667;7.9667">
  <meta name="ICBM" content="45.9667, 7.9667">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Open+Sans:wght@400;600;700&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet"></noscript>
  <link rel="preload" href="{p}css/style.css?v={CSS_V}" as="style">
  <link rel="stylesheet" href="{p}css/style.css?v={CSS_V}">
<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "{esc(c['bc_home'])}", "item": "{home_item}"}},
      {{"@type": "ListItem", "position": 2, "name": "{esc(c['bc_exp'])}", "item": "{exp_item}"}},
      {{"@type": "ListItem", "position": 3, "name": "{esc(c['bc_page'])}", "item": "{url}"}}
    ]
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{esc(c['web_name'])}",
    "description": "{esc(c['web_desc'])}",
    "url": "{url}",
    "inLanguage": "{c['in_language']}",
    "isPartOf": {{
      "@type": "WebSite",
      "name": "Macugnaga Booking",
      "url": "{SITE}/"
    }},
    "about": {{
      "@type": "TouristDestination",
      "name": "Macugnaga",
      "description": "Villaggio alpino ai piedi della parete Est del Monte Rosa, Valle Anzasca (VB), Piemonte.",
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": 45.9667,
        "longitude": 7.9667
      }}
    }},
    "temporalCoverage": "2026-09-02/2026-09-14"
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "{esc(c['list_name'])}",
    "description": "{esc(c['list_desc'])}",
    "url": "{url}",
    "numberOfItems": 4,
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Miniera d’oro della Guia",
        "url": "{SITE}/{c['dir']}miniera-oro.html"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Casa Museo Walser di Borca",
        "url": "{SITE}/{c['dir']}casa-museo-walser.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "Weekend a Macugnaga",
        "url": "{SITE}/{c['dir']}weekend.html"
      }},
      {{
        "@type": "ListItem",
        "position": 4,
        "name": "Montagna con i bambini",
        "url": "{SITE}/{c['dir']}famiglie.html"
      }}
    ]
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "{esc(c['faq1_q'])}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{esc(html.unescape(c['faq1_a'].replace('<a href=\"casa-museo-walser.html\">', '').replace('<a href=\"miniera-oro.html\">', '').replace('</a>', '')))}"
        }}
      }},
      {{
        "@type": "Question",
        "name": "{esc(c['faq2_q'])}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{esc(html.unescape(c['faq2_a'].replace('<a href=\"fuga-citta.html\">', '').replace('</a>', '')))}"
        }}
      }},
      {{
        "@type": "Question",
        "name": "{esc(c['faq3_q'])}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{esc('Alloggio a Macugnaga, esperienze online e passeggiate in paese.' if lang == 'it' else c['faq3_a'].replace('<a href=\"weekend.html\">', '').replace('</a>', '').replace('<a href=\"https://macugnaga-monterosa.it/contenuti/306635/dove-dormire\" target=\"_blank\" rel=\"noopener\">', '').replace('</a>', ''))}"
        }}
      }}
    ]
  }}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">{c['skip']}</a>
  <div id="site-header">
  <nav class="seo-nav-fallback" aria-label="{c['nav_aria']}">{nav_html(c)}
  </nav>
</div>
  <div id="site-search"></div>

  <main id="main">
    <header class="page-hero">
      <div class="page-hero__media">
        <picture>
          <source type="image/webp" srcset="{p}assets/web/landing-agosto-aria-fresca-800.webp 800w, {p}assets/web/landing-agosto-aria-fresca-1200.webp 1200w, {p}assets/web/landing-agosto-aria-fresca.webp 1600w" sizes="100vw">
          <img src="{p}assets/web/landing-agosto-aria-fresca.jpg" srcset="{p}assets/web/landing-agosto-aria-fresca-800.jpg 800w, {p}assets/web/landing-agosto-aria-fresca-1200.jpg 1200w, {p}assets/web/landing-agosto-aria-fresca.jpg 1600w" sizes="100vw" alt="{esc(c['img_alt_hero'])}" width="1600" height="842" fetchpriority="high" decoding="async">
        </picture>
      </div>
      <div class="page-hero__scrim" aria-hidden="true"></div>
      <div class="page-hero__content">
        <p class="breadcrumb"><a href="index.html">{c['crumb_home']}</a> · <a href="esperienze.html">{c['crumb_exp']}</a> · {c['crumb_label']}</p>
        <h1>{c['h1']}</h1>
        <p>{c['hero_lead']}</p>
      </div>
    </header>

    <section class="section section--white">
      <div class="container split">
        <div class="reveal prose">
          <p class="section__eyebrow">{c['eyebrow1']}</p>
          <h2>{c['h2_1']}</h2>
          <p>{c['p1a']}</p>
          <p>{c['p1b']}</p>
          <ul>
            <li>{c['li1']}</li>
            <li>{c['li2']}</li>
            <li>{c['li3']}</li>
          </ul>
        </div>
        <div class="split__media reveal">
          <picture>
            <source type="image/webp" srcset="{p}assets/web/landing-agosto-aria-fresca-800.webp 800w, {p}assets/web/landing-agosto-aria-fresca-1200.webp 1200w, {p}assets/web/landing-agosto-aria-fresca.webp 1600w" sizes="(max-width:720px) 100vw, 50vw">
            <img src="{p}assets/web/landing-agosto-aria-fresca.jpg" srcset="{p}assets/web/landing-agosto-aria-fresca-800.jpg 800w, {p}assets/web/landing-agosto-aria-fresca-1200.jpg 1200w, {p}assets/web/landing-agosto-aria-fresca.jpg 1600w" sizes="(max-width:720px) 100vw, 50vw" alt="{esc(c['img_alt_hero'])}" width="800" height="421" loading="lazy" decoding="async">
          </picture>
        </div>
      </div>
    </section>

    <section class="section section--cream">
      <div class="container split split--rev">
        <div class="split__media reveal">
          <picture>
            <source type="image/webp" srcset="{p}assets/web/drone-monterosa-800.webp 800w, {p}assets/web/drone-monterosa-1200.webp 1200w, {p}assets/web/drone-monterosa.webp 1600w" sizes="(max-width:720px) 100vw, 50vw">
            <img src="{p}assets/web/drone-monterosa.jpg" srcset="{p}assets/web/drone-monterosa-800.jpg 800w, {p}assets/web/drone-monterosa-1200.jpg 1200w, {p}assets/web/drone-monterosa.jpg 1600w" sizes="(max-width:720px) 100vw, 50vw" alt="{esc(c['img_alt_drone'])}" width="800" height="600" loading="lazy" decoding="async">
          </picture>
        </div>
        <div class="reveal prose">
          <p class="section__eyebrow">{c['eyebrow2']}</p>
          <h2>{c['h2_2']}</h2>
          <p>{c['p2a']}</p>
          <p>{c['p2b']}</p>
          <div class="btn-row">
            <a class="btn btn--outline" href="fuga-citta.html">{c['btn_fuga']}</a>
            <a class="btn btn--outline" href="famiglie.html">{c['btn_fam']}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container split">
        <div class="reveal prose">
          <p class="section__eyebrow">{c['eyebrow3']}</p>
          <h2>{c['h2_3']}</h2>
          <p>{c['p3a']}</p>
          <p>{c['p3b']}</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="weekend.html">{c['btn_week']}</a>
            <a class="btn btn--outline" href="https://macugnaga-monterosa.it/contenuti/306635/dove-dormire" target="_blank" rel="noopener">{c['btn_sleep']}</a>
          </div>
        </div>
        <div class="split__media reveal">
          <picture>
            <source type="image/webp" srcset="{p}assets/web/ossola-macugnaga-800.webp 800w, {p}assets/web/ossola-macugnaga-1200.webp 1200w, {p}assets/web/ossola-macugnaga.webp 1600w" sizes="(max-width:720px) 100vw, 50vw">
            <img src="{p}assets/web/ossola-macugnaga.jpg" srcset="{p}assets/web/ossola-macugnaga-800.jpg 800w, {p}assets/web/ossola-macugnaga-1200.jpg 1200w, {p}assets/web/ossola-macugnaga.jpg 1600w" sizes="(max-width:720px) 100vw, 50vw" alt="{esc(c['img_alt_ossola'])}" width="800" height="600" loading="lazy" decoding="async">
          </picture>
        </div>
      </div>
    </section>

    <section class="section section--cream" style="padding-bottom:1rem" id="prenota">
      <div class="container prose reveal">
        <p class="section__eyebrow">{c['eyebrow4']}</p>
        <h2>{c['h2_4']}</h2>
        <p>{c['p4']}</p>
      </div>
    </section>

    <section class="planyo-wrap esperienze-list-wrap" aria-label="{esc(c['list_aria'])}">
      <div class="container">
        <div id="esperienze-list" class="esperienze-list" data-date-from="today" data-date-to="{DATE_TO}" aria-live="polite">
          <p class="esperienze-list__status">{c['list_loading']}</p>
        </div>
        <noscript>
          <ul class="esperienze-static">
            <li><a href="miniera-oro.html">{c['ns_mine']}</a></li>
            <li><a href="casa-museo-walser.html">{c['ns_walser']}</a></li>
            <li><a href="esperienze.html">{c['ns_all']}</a></li>
            <li><a href="weekend.html">{c['ns_week']}</a></li>
            <li><a href="famiglie.html">{c['ns_fam']}</a></li>
          </ul>
        </noscript>
      </div>
    </section>

    <section class="section section--white" id="faq">
      <div class="container">
        <p class="section__eyebrow reveal">FAQ</p>
        <h2 class="reveal">{c['faq_h2']}</h2>
        <div class="faq-list" style="margin-top:1.25rem">
          <details class="faq-item reveal">
            <summary>{c['faq1_q']}</summary>
            <p class="faq-a">{c['faq1_a']}</p>
          </details>
          <details class="faq-item reveal">
            <summary>{c['faq2_q']}</summary>
            <p class="faq-a">{c['faq2_a']}</p>
          </details>
          <details class="faq-item reveal">
            <summary>{c['faq3_q']}</summary>
            <p class="faq-a">{c['faq3_a']}</p>
          </details>
        </div>
        <p class="note" style="margin-top:1.75rem;max-width:48rem">{c['note']}</p>
      </div>
    </section>
  </main>

{note_block}  <div id="site-footer"></div>
  <div id="cookie-banner" class="cookie-banner" role="dialog" aria-label="{esc(c['cookie_aria'])}">
    <p>{c['cookie_text']}</p>
    <div class="cookie-banner__actions">
      <button type="button" class="btn btn--primary" data-cookie-accept>{c['cookie_ok']}</button>
      <button type="button" class="btn btn--outline" data-cookie-essential>{c['cookie_ess']}</button>
    </div>
  </div>
<script src="{p}js/i18n.js?v={I18N_V}" defer></script>
  <script src="{p}js/partials.js?v={PARTIALS_V}" defer></script>
  <script src="{p}js/main.js?v={MAIN_V}" defer></script>
  <script src="{p}js/esperienze-list.js?v={LIST_V}" defer></script>
</body>
</html>
"""


def prenota(rid: str, mode: str) -> str:
    return (
        f"{SITE}/prenota.html?resource_id={rid}"
        f"&amp;mode={mode}&amp;ppp_refcode=grotta&amp;planyo_lang=IT"
    )


def featured_block(
    *,
    rid: str,
    title: str,
    date_label: str,
    price_label: str,
    desc: str,
    photo: str,
    photo_alt: str,
) -> str:
    detail = prenota(rid, "resource_desc")
    reserve = prenota(rid, "reserve")
    return f"""          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:24px 0 8px 0;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#ffffff;border:1px solid #e2e6de;border-radius:6px;">
                <tr>
                  <td style="padding:0;">
                    <a href="{detail}" target="_blank" style="text-decoration:none;">
                      <img src="{photo}" width="600" alt="{esc(photo_alt)}" style="display:block;width:100%;max-width:600px;height:auto;border:0;border-radius:6px 6px 0 0;" />
                    </a>
                  </td>
                </tr>
                <tr>
                  <td style="padding:20px 24px 22px 24px;">
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td style="font-family:Georgia,'Times New Roman',serif;font-size:22px;line-height:1.3;color:{GREEN_DARK};font-weight:bold;padding:0 0 8px 0;">
                          {esc(title)}
                        </td>
                      </tr>
                      <tr>
                        <td style="font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.4;color:{GREEN};font-weight:bold;padding:0 0 12px 0;">
                          {esc(date_label)}
                        </td>
                      </tr>
                      <tr>
                        <td bgcolor="#e8f0e4" style="background:#e8f0e4;border-left:4px solid {GREEN};padding:12px 14px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.45;color:{GREEN_DARK};font-weight:bold;">
                          {esc(price_label)}
                        </td>
                      </tr>
                      <tr>
                        <td style="font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.55;color:{MUTED};padding:14px 0 16px 0;">
                          {esc(desc)}
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                            <tr>
                              <td bgcolor="{GREEN}" style="border-radius:4px;">
                                <a href="{detail}" target="_blank" style="display:inline-block;padding:12px 20px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;background:{GREEN};">
                                  Scopri
                                </a>
                              </td>
                              <td width="10" style="font-size:0;line-height:0;">&nbsp;</td>
                              <td bgcolor="{ACCENT_BTN}" style="border-radius:4px;">
                                <a href="{reserve}" target="_blank" style="display:inline-block;padding:12px 20px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;background:{ACCENT_BTN};">
                                  Prenota
                                </a>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>"""


def list_row(rid: str, title: str, date_label: str) -> str:
    href = prenota(rid, "resource_desc")
    return f"""                      <tr>
                        <td style="padding:0 0 12px 0;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.45;color:#202020;">
                          <a href="{href}" target="_blank" style="color:{GREEN_DARK};font-weight:bold;text-decoration:underline;">{esc(title)}</a>
                          <span style="color:{MUTED};"> — {esc(date_label)}</span>
                        </td>
                      </tr>"""


def highlight_title(text: str) -> str:
    return f"""          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:20px 24px 0 24px;">
              <p style="margin:0;font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:1.4;color:{GREEN_DARK};font-weight:bold;text-align:left;">
                {esc(text)}
              </p>
            </td>
          </tr>"""


def villaggio_zucche_block() -> str:
    href = GROTTA_HOME_URL
    huntrix = f"{SITE}/assets/web/villaggio-zucche-huntrix.jpg"
    mercoledi = f"{SITE}/assets/web/villaggio-zucche-mercoledi.jpg"
    title = (
        "Prenota il biglietto anteprima per il nostro Villaggio delle Zucche al Parco Le Cicogne "
        "di Buronzo (Novara) - Per te l'accesso alla nuova esperienza prima degli spettacoli: "
        "prova le coreografie come le Huntrix e Mercoledì"
    )
    return f"""          <!-- Promo: Villaggio delle Zucche anteprima -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:8px 0 8px 0;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#ffffff;border:1px solid #e2e6de;border-radius:6px;">
                <tr>
                  <td style="padding:0;">
                    <a href="{href}" target="_blank" rel="noopener noreferrer" style="text-decoration:none;">
                      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                          <td width="50%" valign="top" style="width:50%;padding:0;">
                            <img src="{huntrix}" width="300" alt="Prova le coreografie come le Huntrix — Villaggio delle Zucche" style="display:block;width:100%;max-width:300px;height:auto;border:0;border-radius:6px 0 0 0;" />
                          </td>
                          <td width="50%" valign="top" style="width:50%;padding:0;">
                            <img src="{mercoledi}" width="300" alt="Prova le coreografie come Mercoledì — Villaggio delle Zucche" style="display:block;width:100%;max-width:300px;height:auto;border:0;border-radius:0 6px 0 0;" />
                          </td>
                        </tr>
                      </table>
                    </a>
                  </td>
                </tr>
                <tr>
                  <td style="padding:18px 24px 10px 24px;">
                    <p style="margin:0;font-family:Georgia,'Times New Roman',serif;font-size:18px;line-height:1.4;color:{GREEN_DARK};font-weight:bold;text-align:left;">
                      {esc(title)}
                    </p>
                  </td>
                </tr>
                <tr>
                  <td style="padding:0 24px 22px 24px;" align="left">
                    <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td bgcolor="{GREEN}" style="border-radius:4px;">
                          <a href="{href}" target="_blank" rel="noopener noreferrer" style="display:inline-block;padding:12px 22px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;background:{GREEN};">
                            Scopri e prenota
                          </a>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>"""


def build_newsletter() -> str:
    landing = abs_url("it")
    oro = featured_block(
        rid="253399",
        title="Alla ricerca dell’oro in Val Quarazza",
        date_label="Sabato 5 settembre",
        price_label="€ 19,90 a persona",
        desc=(
            "Escursione per famiglie tra natura, torrenti e antiche tracce dei cercatori d’oro. "
            "Anche voi cercherete l’oro con la batea, accompagnati da una guida locale in Val Quarazza."
        ),
        photo=f"{SITE}/assets/web/ricerca-oro.jpg",
        photo_alt="Alla ricerca dell’oro in Val Quarazza",
    )
    favole = featured_block(
        rid="254066",
        title="Favole Walser in quota",
        date_label="Sabato 5 settembre",
        price_label="€ 15 a persona — con funivia e merenda",
        desc=(
            "Un pomeriggio speciale tra favole, natura e tradizioni Walser: i bambini salgono in quota "
            "con funivia e merenda, tra racconti e magia alpina."
        ),
        photo=f"{SITE}/assets/web/favole-walser-quota.jpg",
        photo_alt="Favole Walser in quota, con funivia e merenda",
    )
    lanternit_intro = highlight_title(
        "E dopo le esperienze in giornata vivi un'emozione unica: la Camminata dei Lanternit"
    )
    lanternit = featured_block(
        rid="254067",
        title="Camminata dei Lanternit",
        date_label="Sabato 5 settembre · ore 19:00",
        price_label="€ 40 a persona",
        desc=(
            "Passeggiata serale con i tradizionali lanternit tra natura, storie e sapori locali: "
            "partenza dall’Azienda Agricola Salvavegia, tappe suggestive e degustazione finale — "
            "un’esperienza per tutta la famiglia."
        ),
        photo=f"{SITE}/assets/web/camminata-lanternit.jpg",
        photo_alt="Camminata dei Lanternit",
    )
    others = "\n".join(
        [
            list_row("252697", "Piccoli Folletti al Museo Walser", "Sabato 5 settembre"),
            list_row("252705", "Miniera d’Oro della Guia", "Weekend 5–6 settembre"),
            list_row("253679", "Funivia Staffa–Alpe Bill", "Sabato–domenica 5–6 settembre"),
            list_row("253658", "Seggiovia Pecetto–Belvedere", "Sabato–domenica 5–6 settembre"),
        ]
    )
    intro = (
        "Vivi la montagna prima del ritorno a scuola. Esperienze ai piedi del Monte Rosa per tutta la famiglia. "
        "Per una giornata, un weekend o per l’ultima vacanza prima della riapertura delle scuole."
    )
    preview = (
        "Prima del ritorno a scuola: ricerca dell’oro, Favole Walser, Camminata dei Lanternit "
        "e weekend 5–6 settembre a Macugnaga. Prenota con Grotta di Babbo Natale."
    )
    return f"""<!DOCTYPE html>
<html lang="it" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="light" />
  <title>Ritorno a scuola · Settembre 2026 · Macugnaga · Grotta di Babbo Natale</title>
  <!--
    Mailchimp «Codice personalizzato» / Code your own.
    Import: Campaign → Email → Code your own → Import HTML (this single file),
    or paste the full document into the custom HTML editor.
    Subject: set in Mailchimp UI (optional merge tag *|MC:SUBJECT|*).
    Merge tags in footer: *|UNSUB|*  *|HTML:LIST_ADDRESS_HTML|*
    Images: absolute https:// only · Layout: tables + inline CSS · Width ~600px
    Refcode: grotta
  -->
</head>
<body style="margin:0;padding:0;background-color:{CREAM};-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;">
  <div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">
    {esc(preview)}
  </div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{CREAM};">
    <tr>
      <td align="center" style="padding:24px 12px;">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;">

          <!-- Header: Grotta di Babbo Natale -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:20px 24px 12px 24px;border-radius:6px 6px 0 0;text-align:center;">
              <a href="{GROTTA_HOME_URL}" target="_blank" style="text-decoration:none;">
                <img src="{SITE}/assets/web/logo-grotta-babbo-natale.png?v=2" width="180" height="180" alt="La Grotta di Babbo Natale – Tutto l'anno" style="display:block;margin:0 auto;border:0;width:180px;max-width:50%;height:auto;" />
              </a>
            </td>
          </tr>
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:22px 24px 10px 24px;">
              <p style="margin:0 0 14px 0;font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:1.4;color:#1a1a1a;text-align:center;font-weight:bold;">
                {esc(intro)}
              </p>
              <p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.45;color:{MUTED};text-align:center;">
                <a href="{SITE}/" target="_blank" style="color:{GREEN};text-decoration:underline;">www.macugnagabooking.it</a> è un progetto dell'Unione Montana Valli dell'Ossola sviluppato da Grotta di Babbo Natale (Lem s.r.l.)
              </p>
            </td>
          </tr>
          <tr>
            <td bgcolor="{GREEN}" style="background:{GREEN};padding:14px 24px;">
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.4;color:#ffffff;font-weight:bold;text-align:center;">
                Prima del ritorno a scuola · fino al 14 settembre 2026
              </p>
            </td>
          </tr>

{oro}

{favole}

{lanternit_intro}

{lanternit}

          <!-- Other weekend 5–6 settembre titles -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:20px 24px 8px 24px;">
              <p style="margin:0 0 10px 0;font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:1.35;color:{GREEN_DARK};font-weight:bold;text-align:left;">
                Anche questo weekend (5–6 settembre)
              </p>
              <p style="margin:0 0 16px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.55;color:#333333;text-align:left;">
                Altre esperienze in programma per il weekend: sabato 5 settembre e domenica 6 settembre — aria di montagna, paese e impianti. Scegli e prenota online.
              </p>
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
{others}
              </table>
            </td>
          </tr>

          <!-- CTA all experiences -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:8px 24px 28px 24px;" align="center">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td bgcolor="{GREEN}" style="border-radius:4px;">
                    <a href="{landing}" target="_blank" style="display:inline-block;padding:14px 28px;font-family:Arial,Helvetica,sans-serif;font-size:15px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;background:{GREEN};">
                      Vedi tutte le esperienze
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

{villaggio_zucche_block()}

{footer_lem_block(green=GREEN)}

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""


def write_landings() -> None:
    for lang in ("it", "en", "fr", "de"):
        c = COPY[lang]
        path = ROOT / c["dir"] / SLUG if c["dir"] else ROOT / SLUG
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(landing_html(lang), encoding="utf-8")
        print("wrote", path)


def write_newsletter() -> None:
    html_doc = build_newsletter()
    out_html = MAIL / f"{NL_BASE}.html"
    out_folder = MAIL / NL_BASE
    out_folder.mkdir(parents=True, exist_ok=True)
    out_folder_html = out_folder / f"{NL_BASE}.html"
    out_zip = MAIL / f"{NL_BASE}.zip"
    out_html.write_text(html_doc, encoding="utf-8")
    out_folder_html.write_text(html_doc, encoding="utf-8")
    with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(f"{NL_BASE}.html", html_doc.encode("utf-8"))
    print("wrote", out_html)
    print("wrote", out_zip)


def main() -> None:
    write_landings()
    write_newsletter()


if __name__ == "__main__":
    main()
