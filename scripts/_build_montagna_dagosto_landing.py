# -*- coding: utf-8 -*-
"""Generate montagna-dagosto-8-20-agosto landing pages (IT/EN/FR/DE)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://www.macugnagabooking.it"
SLUG = "montagna-dagosto-8-20-agosto.html"
URLS = {
    "it": f"{BASE}/{SLUG}",
    "en": f"{BASE}/en/{SLUG}",
    "fr": f"{BASE}/fr/{SLUG}",
    "de": f"{BASE}/de/{SLUG}",
}

ITEMLIST = {
    "it": [
        ("Miniera d’oro della Guia", "miniera-oro.html"),
        ("Casa Museo Walser di Borca", "casa-museo-walser.html"),
        ("Weekend a Macugnaga", "weekend.html"),
        ("Montagna con i bambini", "famiglie.html"),
    ],
    "en": [
        ("Guia gold mine", "miniera-oro.html"),
        ("Walser House Museum in Borca", "casa-museo-walser.html"),
        ("Weekend in Macugnaga", "weekend.html"),
        ("Mountains with children", "famiglie.html"),
    ],
    "fr": [
        ("Mine d’or de la Guia", "miniera-oro.html"),
        ("Maison-musée Walser de Borca", "casa-museo-walser.html"),
        ("Week-end à Macugnaga", "weekend.html"),
        ("Montagne avec les enfants", "famiglie.html"),
    ],
    "de": [
        ("Goldmine Guia", "miniera-oro.html"),
        ("Walser-Hausmuseum in Borca", "casa-museo-walser.html"),
        ("Wochenende in Macugnaga", "weekend.html"),
        ("Berg mit Kindern", "famiglie.html"),
    ],
}


def j(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


PAGES = {
    "it": {
        "lang": "it",
        "dir": "",
        "prefix": "",
        "locale": "it_IT",
        "title": "Montagna d’agosto — Esperienze dall’8 al 20 agosto ai piedi del Monte Rosa | Macugnaga Booking",
        "description": "Montagna d’agosto a Macugnaga Monte Rosa: tutte le esperienze prenotabili online dall’8 al 20 agosto 2026. Boschi, miniera d’oro, Casa Walser, trekking e natura — portale di prenotazione dell’Unione Montana.",
        "og_title": "Montagna d’agosto 8–20 agosto | Macugnaga Monte Rosa",
        "og_desc": "Ecco tutte le esperienze che puoi vivere ai piedi del Monte Rosa dall’8 al 20 agosto: prenota online su Macugnaga Booking.",
        "tw_title": "Montagna d’agosto — Esperienze 8–20 agosto | Macugnaga",
        "h1": "Montagna d’agosto — Ecco tutte le esperienze che puoi vivere ai piedi del Monte Rosa dall’8 al 20 agosto",
        "hero_p": "Dall’8 al 20 agosto 2026, il portale di prenotazione raccoglie le attività disponibili ai piedi del Monte Rosa: natura, cultura e montagna per tutti.",
        "crumb": "8–20 agosto",
        "breadcrumb_home": "Home",
        "breadcrumb_exp": "Esperienze",
        "skip": "Vai al contenuto",
        "nav_label": "Navigazione principale",
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
        "eyebrow1": "Estate in quota",
        "h2_1": "Aria di montagna, esperienze autentiche",
        "p1a": "Quando l’estate chiede natura e freschezza, Macugnaga offre <strong>clima alpino</strong>, sentieri tra i larici e proposte a contatto con la montagna pensate per famiglie, adulti e appassionati.",
        "p1b": "Dall’<strong>8 al 20 agosto</strong> il portale di prenotazione raccoglie le esperienze disponibili online: benessere in bosco, visite culturali, miniera d’oro, trekking e attività soft.",
        "li": [
            "Operatori autorizzati e guide qualificate",
            "Prenotazione online con conferma immediata",
            "Idee per giornata o weekend con pernottamento",
        ],
        "img1_alt": "Veduta del Dorf di Macugnaga con case walser e Monte Rosa",
        "eyebrow2": "Vicino alle città e ai laghi",
        "h2_2": "La montagna vera, a portata di strada",
        "p2a": "Macugnaga è raggiungibile in circa 1,5–2,5 ore da <strong>Milano</strong>, <strong>Varese</strong>, <strong>Novara</strong> e dal <strong>Lago Maggiore</strong> — e anche da <strong>Orta</strong>, <strong>Mergozzo</strong> e Torino.",
        "p2b": 'Perfetta come <a href="fuga-citta.html">fuga dalla città</a> o come giornata in montagna se soggiorni in hotel o campeggio sui laghi: aria fresca, paese alpino e panorami sul Monte Rosa senza lunghi trasferimenti.',
        "btn_fuga": "Fuga dalla città",
        "btn_fam": "Montagna con i bambini",
        "img2_alt": "Macugnaga e Monte Rosa visti dall’alto",
        "eyebrow3": "Soggiorno con pernottamento",
        "h2_3": "Dormire e risvegliarsi ai piedi del Rosa…",
        "p3a": "Tra l’8 e il 20 agosto un <strong>soggiorno con pernottamento</strong> rende l’estate in montagna più completa: alba e tramonto sul Monte Rosa, una o due esperienze prenotate online, passeggiate in paese e cucina locale.",
        "p3b": 'Scegli hotel, B&amp;B o casa vacanza, poi prenota le attività qui sotto. Guida pratica su <a href="weekend.html">Idee weekend</a>.',
        "btn_week": "Organizza soggiorno",
        "btn_sleep": "Dove dormire",
        "img3_alt": "Paesaggio di Macugnaga in Valle Anzasca",
        "eyebrow4": "Prenota online",
        "h2_4": "Esperienze prenotabili dall’8 al 20 agosto",
        "p4": 'Elenco aggiornato delle attività con disponibilità tra l’<strong>8</strong> e il <strong>20 agosto 2026</strong>. Scegli data e posti, paga online e ricevi subito conferma con i contatti delle guide. Per il catalogo completo vedi <a href="esperienze.html">tutte le esperienze</a>.',
        "aria_list": "Esperienze prenotabili 8–20 agosto",
        "loading": "Caricamento esperienze…",
        "faq_eyebrow": "FAQ",
        "faq_h2": "Domande frequenti su Montagna d’agosto (8–20 agosto)",
        "faq": [
            (
                "Quali esperienze posso prenotare dall’8 al 20 agosto a Macugnaga?",
                'L’elenco in questa pagina mostra tutte le esperienze del portale di prenotazione con disponibilità tra l’8 e il 20 agosto 2026: boschi e natura, <a href="casa-museo-walser.html">Casa Museo Walser</a>, <a href="miniera-oro.html">miniera d’oro</a>, trekking e attività soft ai piedi del Monte Rosa.',
            ),
            (
                "Macugnaga è adatta per una fuga dal caldo vicino a Milano e ai laghi?",
                'Sì: clima fresco alpino a poca distanza da Milano, Varese, Novara e dai laghi Maggiore, d’Orta e di Mergozzo. Vedi anche <a href="fuga-citta.html">Fuga dalla città</a>.',
            ),
            (
                "Come organizzare un weekend con pernottamento?",
                'Alloggio a Macugnaga, una o due esperienze prenotate online e passeggiate in paese. Guida su <a href="weekend.html">Weekend</a> e elenco <a href="https://macugnaga-monterosa.it/contenuti/306635/dove-dormire" target="_blank" rel="noopener">dove dormire</a>.',
            ),
        ],
        "note": 'Informazioni, prezzi e disponibilità del portale di prenotazione sono indicati dai gestori. Dopo la prenotazione riceverai i contatti degli organizzatori. <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> non è responsabile della gestione delle attività. <a href="credits.html">Maggiori informazioni</a>',
        "cookie_label": "Informativa cookie",
        "cookie_p": 'Questo sito utilizza cookie tecnici necessari al funzionamento e servizi di terze parti per la prenotazione online e i font. <a href="privacy.html">Privacy e cookie</a>',
        "cookie_ok": "Accetta",
        "cookie_ess": "Solo essenziali",
        "web_name": "Montagna d’agosto — Esperienze dall’8 al 20 agosto a Macugnaga",
        "web_desc": "Tutte le esperienze prenotabili online a Macugnaga Monte Rosa tra l’8 e il 20 agosto 2026, ai piedi del Monte Rosa.",
        "list_name": "Esperienze prenotabili a Macugnaga dall’8 al 20 agosto",
        "list_desc": "Attività in montagna prenotabili online a Macugnaga Monte Rosa tra l’8 e il 20 agosto 2026.",
        "bc_name": "8–20 agosto",
        "site_name": "Macugnaga Booking – Esperienze ai piedi del Monte Rosa",
        "faq_schema": [
            (
                "Quali esperienze posso prenotare dall’8 al 20 agosto a Macugnaga?",
                "Tra l’8 e il 20 agosto 2026 puoi prenotare online esperienze a contatto con boschi e natura, visite alla Casa Museo Walser e alla miniera d’oro, trekking e attività soft ai piedi del Monte Rosa.",
            ),
            (
                "Macugnaga è adatta per una fuga dal caldo vicino a Milano e ai laghi?",
                "Sì: Macugnaga offre aria fresca alpina a poca distanza da Milano, Varese, Novara e dai laghi Maggiore, d’Orta e di Mergozzo. Ideale per una giornata o un weekend con pernottamento fuori città.",
            ),
            (
                "Come organizzare un weekend con pernottamento dall’8 al 20 agosto?",
                "Scegli un hotel, B&B o casa vacanza a Macugnaga, prenota online una o due esperienze del periodo 8–20 agosto e combina passeggiate in paese, boschi e, se aperti, gli impianti di risalita.",
            ),
        ],
        "noscript": [
            ("miniera-oro.html", "Miniera d’oro della Guia"),
            ("casa-museo-walser.html", "Casa Museo Walser di Borca"),
            ("esperienze.html", "Tutte le esperienze prenotabili"),
            ("weekend.html", "Idee weekend a Macugnaga"),
            ("famiglie.html", "Montagna con i bambini"),
        ],
        "footer_note": None,
    },
    "en": {
        "lang": "en",
        "dir": "en/",
        "prefix": "../",
        "locale": "en_GB",
        "title": "August in the mountains — Experiences 8–20 August at the foot of Monte Rosa | Macugnaga Booking",
        "description": "August in the mountains in Macugnaga Monte Rosa: all bookable online experiences from 8 to 20 August 2026. Woods, gold mine, Walser House, trekking and nature — Unione Montana booking portal.",
        "og_title": "August in the mountains 8–20 August | Macugnaga Monte Rosa",
        "og_desc": "All the experiences you can enjoy at the foot of Monte Rosa from 8 to 20 August — book online on Macugnaga Booking.",
        "tw_title": "August in the mountains — Experiences 8–20 August | Macugnaga",
        "h1": "August in the mountains — All the experiences you can enjoy at the foot of Monte Rosa from 8 to 20 August",
        "hero_p": "From 8 to 20 August 2026, the booking portal gathers the activities available at the foot of Monte Rosa: nature, culture and mountains for everyone.",
        "crumb": "8–20 August",
        "breadcrumb_home": "Home",
        "breadcrumb_exp": "Experiences",
        "skip": "Skip to content",
        "nav_label": "Main navigation",
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
        "eyebrow1": "Summer in the mountains",
        "h2_1": "Mountain air, authentic experiences",
        "p1a": "When summer calls for nature and cool air, Macugnaga offers <strong>alpine climate</strong>, trails among larches and mountain experiences for families, adults and enthusiasts.",
        "p1b": "From <strong>8 to 20 August</strong> the booking portal gathers the experiences available online: forest wellness, cultural visits, gold mine, trekking and gentle activities.",
        "li": [
            "Authorised operators and qualified guides",
            "Online booking with instant confirmation",
            "Ideas for a day trip or a weekend with overnight stay",
        ],
        "img1_alt": "View of Macugnaga Dorf with Walser houses and Monte Rosa",
        "eyebrow2": "Close to cities and lakes",
        "h2_2": "Real mountains, within easy reach",
        "p2a": "Macugnaga is about 1.5–2.5 hours from <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> and <strong>Lake Maggiore</strong> — and also from <strong>Orta</strong>, <strong>Mergozzo</strong> and Turin.",
        "p2b": 'Perfect as a <a href="fuga-citta.html">city escape</a> or a mountain day if you stay in a hotel or campsite by the lakes: fresh air, alpine village and Monte Rosa views without long transfers.',
        "btn_fuga": "City escape",
        "btn_fam": "Mountains with children",
        "img2_alt": "Macugnaga and Monte Rosa from above",
        "eyebrow3": "Stay overnight",
        "h2_3": "Sleep and wake up at the foot of the Rosa…",
        "p3a": "Between 8 and 20 August an <strong>overnight stay</strong> makes summer in the mountains more complete: sunrise and sunset on Monte Rosa, one or two experiences booked online, village walks and local food.",
        "p3b": 'Choose a hotel, B&amp;B or holiday home, then book the activities below. Practical guide on <a href="weekend.html">Weekend ideas</a>.',
        "btn_week": "Plan your stay",
        "btn_sleep": "Where to stay",
        "img3_alt": "Macugnaga landscape in the Anzasca Valley",
        "eyebrow4": "Book online",
        "h2_4": "Bookable experiences from 8 to 20 August",
        "p4": 'Updated list of activities with availability between <strong>8</strong> and <strong>20 August 2026</strong>. Choose date and places, pay online and receive instant confirmation with guide contacts. For the full catalogue see <a href="esperienze.html">all experiences</a>.',
        "aria_list": "Bookable experiences 8–20 August",
        "loading": "Loading experiences…",
        "faq_eyebrow": "FAQ",
        "faq_h2": "Frequently asked questions about August in the mountains (8–20 August)",
        "faq": [
            (
                "Which experiences can I book from 8 to 20 August in Macugnaga?",
                'The list on this page shows all booking-portal experiences with availability between 8 and 20 August 2026: woods and nature, <a href="casa-museo-walser.html">Walser House Museum</a>, <a href="miniera-oro.html">gold mine</a>, trekking and gentle activities at the foot of Monte Rosa.',
            ),
            (
                "Is Macugnaga a good heat escape near Milan and the lakes?",
                'Yes: cool alpine climate a short trip from Milan, Varese, Novara and Lakes Maggiore, Orta and Mergozzo. See also <a href="fuga-citta.html">City escape</a>.',
            ),
            (
                "How to plan a weekend with overnight stay?",
                'Stay in Macugnaga, book one or two experiences online and enjoy village walks. Guide on <a href="weekend.html">Weekend</a> and list of <a href="https://macugnaga-monterosa.it/contenuti/306635/dove-dormire" target="_blank" rel="noopener">where to stay</a>.',
            ),
        ],
        "note": 'Information, prices and availability on the booking portal are provided by the operators. After booking you will receive the organisers’ contacts. <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> is not responsible for running the activities. <a href="credits.html">More information</a>',
        "cookie_label": "Cookie notice",
        "cookie_p": 'This site uses technical cookies required for operation and third-party services for online booking and fonts. <a href="privacy.html">Privacy and cookies</a>',
        "cookie_ok": "Accept",
        "cookie_ess": "Essential only",
        "web_name": "August in the mountains — Experiences from 8 to 20 August in Macugnaga",
        "web_desc": "All bookable online experiences in Macugnaga Monte Rosa from 8 to 20 August 2026, at the foot of Monte Rosa.",
        "list_name": "Bookable experiences in Macugnaga from 8 to 20 August",
        "list_desc": "Mountain activities bookable online in Macugnaga Monte Rosa from 8 to 20 August 2026.",
        "bc_name": "8–20 August",
        "site_name": "Macugnaga Booking – Experiences at the foot of Monte Rosa",
        "faq_schema": [
            (
                "Which experiences can I book from 8 to 20 August in Macugnaga?",
                "Between 8 and 20 August 2026 you can book online experiences among woods and nature, visits to the Walser House Museum and the gold mine, trekking and gentle activities at the foot of Monte Rosa.",
            ),
            (
                "Is Macugnaga a good heat escape near Milan and the lakes?",
                "Yes: Macugnaga offers cool alpine air a short trip from Milan, Varese, Novara and Lakes Maggiore, Orta and Mergozzo. Ideal for a day trip or a weekend with overnight stay away from the city.",
            ),
            (
                "How to plan a weekend with overnight stay from 8 to 20 August?",
                "Choose a hotel, B&B or holiday home in Macugnaga, book online one or two experiences for 8–20 August and combine village walks, woods and, if open, the ski lifts.",
            ),
        ],
        "noscript": [
            ("miniera-oro.html", "Guia gold mine"),
            ("casa-museo-walser.html", "Walser House Museum in Borca"),
            ("esperienze.html", "All bookable experiences"),
            ("weekend.html", "Weekend ideas in Macugnaga"),
            ("famiglie.html", "Mountains with children"),
        ],
        "footer_note": "Automatic translation from the official Italian version",
    },
    "fr": {
        "lang": "fr",
        "dir": "fr/",
        "prefix": "../",
        "locale": "fr_FR",
        "title": "Montagne d’août — Expériences du 8 au 20 août au pied du Mont Rose | Macugnaga Booking",
        "description": "Montagne d’août à Macugnaga Monte Rosa : toutes les expériences réservables en ligne du 8 au 20 août 2026. Forêts, mine d’or, Maison Walser, randonnées et nature — portail de réservation de l’Unione Montana.",
        "og_title": "Montagne d’août 8–20 août | Macugnaga Monte Rosa",
        "og_desc": "Voici toutes les expériences à vivre au pied du Mont Rose du 8 au 20 août — réservez en ligne sur Macugnaga Booking.",
        "tw_title": "Montagne d’août — Expériences 8–20 août | Macugnaga",
        "h1": "Montagne d’août — Voici toutes les expériences que vous pouvez vivre au pied du Mont Rose du 8 au 20 août",
        "hero_p": "Du 8 au 20 août 2026, le portail de réservation regroupe les activités disponibles au pied du Mont Rose : nature, culture et montagne pour tous.",
        "crumb": "8–20 août",
        "breadcrumb_home": "Accueil",
        "breadcrumb_exp": "Expériences",
        "skip": "Aller au contenu",
        "nav_label": "Navigation principale",
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
        "eyebrow1": "Été en altitude",
        "h2_1": "Air de montagne, expériences authentiques",
        "p1a": "Quand l’été appelle nature et fraîcheur, Macugnaga offre un <strong>climat alpin</strong>, des sentiers parmi les mélèzes et des propositions montagne pour familles, adultes et passionnés.",
        "p1b": "Du <strong>8 au 20 août</strong>, le portail de réservation regroupe les expériences disponibles en ligne : bien-être en forêt, visites culturelles, mine d’or, randonnées et activités douces.",
        "li": [
            "Opérateurs autorisés et guides qualifiés",
            "Réservation en ligne avec confirmation immédiate",
            "Idées pour une journée ou un week-end avec nuitée",
        ],
        "img1_alt": "Vue du Dorf de Macugnaga avec maisons walser et Monte Rosa",
        "eyebrow2": "Près des villes et des lacs",
        "h2_2": "La vraie montagne, à portée de route",
        "p2a": "Macugnaga est accessible en environ 1 h 30–2 h 30 depuis <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novare</strong> et le <strong>lac Majeur</strong> — et aussi depuis <strong>Orta</strong>, <strong>Mergozzo</strong> et Turin.",
        "p2b": 'Parfaite comme <a href="fuga-citta.html">échappée hors de la ville</a> ou comme journée en montagne si vous séjournez à l’hôtel ou au camping près des lacs : air frais, village alpin et panoramas sur le Mont Rose sans longs trajets.',
        "btn_fuga": "Échapper à la ville",
        "btn_fam": "Montagne avec les enfants",
        "img2_alt": "Macugnaga et le Monte Rosa vus du ciel",
        "eyebrow3": "Séjour avec nuitée",
        "h2_3": "Dormir et se réveiller au pied du Rosa…",
        "p3a": "Entre le 8 et le 20 août, un <strong>séjour avec nuitée</strong> rend l’été en montagne plus complet : aube et coucher de soleil sur le Mont Rose, une ou deux expériences réservées en ligne, balades au village et cuisine locale.",
        "p3b": 'Choisissez un hôtel, un B&amp;B ou une maison de vacances, puis réservez les activités ci-dessous. Guide pratique sur <a href="weekend.html">Idées week-end</a>.',
        "btn_week": "Organiser le séjour",
        "btn_sleep": "Où dormir",
        "img3_alt": "Paysage de Macugnaga dans le Val Anzasca",
        "eyebrow4": "Réserver en ligne",
        "h2_4": "Expériences réservables du 8 au 20 août",
        "p4": 'Liste à jour des activités disponibles entre le <strong>8</strong> et le <strong>20 août 2026</strong>. Choisissez date et places, payez en ligne et recevez aussitôt la confirmation avec les contacts des guides. Pour le catalogue complet, voir <a href="esperienze.html">toutes les expériences</a>.',
        "aria_list": "Expériences réservables 8–20 août",
        "loading": "Chargement des expériences…",
        "faq_eyebrow": "FAQ",
        "faq_h2": "Questions fréquentes sur Montagne d’août (8–20 août)",
        "faq": [
            (
                "Quelles expériences puis-je réserver du 8 au 20 août à Macugnaga ?",
                'La liste de cette page montre toutes les expériences du portail de réservation disponibles entre le 8 et le 20 août 2026 : forêts et nature, <a href="casa-museo-walser.html">Maison-musée Walser</a>, <a href="miniera-oro.html">mine d’or</a>, randonnées et activités douces au pied du Mont Rose.',
            ),
            (
                "Macugnaga convient-elle pour échapper à la chaleur près de Milan et des lacs ?",
                'Oui : un climat alpin frais à peu de distance de Milan, Varese, Novare et des lacs Majeur, d’Orta et de Mergozzo. Voir aussi <a href="fuga-citta.html">Échappée hors de la ville</a>.',
            ),
            (
                "Comment organiser un week-end avec nuitée ?",
                'Hébergement à Macugnaga, une ou deux expériences réservées en ligne et balades au village. Guide sur <a href="weekend.html">Week-end</a> et liste <a href="https://macugnaga-monterosa.it/contenuti/306635/dove-dormire" target="_blank" rel="noopener">où dormir</a>.',
            ),
        ],
        "note": 'Informations, prix et disponibilités du portail de réservation sont indiqués par les gestionnaires. Après la réservation vous recevrez les contacts des organisateurs. <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> n’est pas responsable de la gestion des activités. <a href="credits.html">Plus d’informations</a>',
        "cookie_label": "Information cookies",
        "cookie_p": 'Ce site utilise des cookies techniques nécessaires au fonctionnement et des services tiers pour la réservation en ligne et les polices. <a href="privacy.html">Confidentialité et cookies</a>',
        "cookie_ok": "Accepter",
        "cookie_ess": "Essentiels uniquement",
        "web_name": "Montagne d’août — Expériences du 8 au 20 août à Macugnaga",
        "web_desc": "Toutes les expériences réservables en ligne à Macugnaga Monte Rosa entre le 8 et le 20 août 2026, au pied du Mont Rose.",
        "list_name": "Expériences réservables à Macugnaga du 8 au 20 août",
        "list_desc": "Activités de montagne réservables en ligne à Macugnaga Monte Rosa du 8 au 20 août 2026.",
        "bc_name": "8–20 août",
        "site_name": "Macugnaga Booking – Expériences au pied du Mont Rose",
        "faq_schema": [
            (
                "Quelles expériences puis-je réserver du 8 au 20 août à Macugnaga ?",
                "Entre le 8 et le 20 août 2026, vous pouvez réserver en ligne des expériences entre forêts et nature, des visites de la Maison-musée Walser et de la mine d’or, des randonnées et des activités douces au pied du Mont Rose.",
            ),
            (
                "Macugnaga convient-elle pour échapper à la chaleur près de Milan et des lacs ?",
                "Oui : Macugnaga offre un air alpin frais à peu de distance de Milan, Varese, Novare et des lacs Majeur, d’Orta et de Mergozzo. Idéale pour une journée ou un week-end avec nuitée hors de la ville.",
            ),
            (
                "Comment organiser un week-end avec nuitée du 8 au 20 août ?",
                "Choisissez un hôtel, un B&B ou une maison de vacances à Macugnaga, réservez en ligne une ou deux expériences du 8–20 août et combinez balades au village, forêts et, s’ils sont ouverts, les remontées mécaniques.",
            ),
        ],
        "noscript": [
            ("miniera-oro.html", "Mine d’or de la Guia"),
            ("casa-museo-walser.html", "Maison-musée Walser de Borca"),
            ("esperienze.html", "Toutes les expériences réservables"),
            ("weekend.html", "Idées week-end à Macugnaga"),
            ("famiglie.html", "Montagne avec les enfants"),
        ],
        "footer_note": "Traduzione automatica dalla versione ufficiale in lingua italiana",
    },
    "de": {
        "lang": "de",
        "dir": "de/",
        "prefix": "../",
        "locale": "de_DE",
        "title": "Berge im August — Erlebnisse vom 8. bis 20. August am Fuß des Monte Rosa | Macugnaga Booking",
        "description": "Berge im August in Macugnaga Monte Rosa: alle online buchbaren Erlebnisse vom 8. bis 20. August 2026. Wälder, Goldmine, Walser-Haus, Trekking und Natur — Buchungsportal der Unione Montana.",
        "og_title": "Berge im August 8.–20. August | Macugnaga Monte Rosa",
        "og_desc": "Alle Erlebnisse am Fuß des Monte Rosa vom 8. bis 20. August — online buchen auf Macugnaga Booking.",
        "tw_title": "Berge im August — Erlebnisse 8.–20. August | Macugnaga",
        "h1": "Berge im August — Alle Erlebnisse, die Sie vom 8. bis 20. August am Fuß des Monte Rosa erleben können",
        "hero_p": "Vom 8. bis 20. August 2026 bündelt das Buchungsportal die verfügbaren Aktivitäten am Fuß des Monte Rosa: Natur, Kultur und Berge für alle.",
        "crumb": "8.–20. August",
        "breadcrumb_home": "Start",
        "breadcrumb_exp": "Erlebnisse",
        "skip": "Zum Inhalt springen",
        "nav_label": "Hauptnavigation",
        "nav": [
            ("index.html", "Start"),
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
        "eyebrow1": "Sommer in der Höhe",
        "h2_1": "Bergluft, authentische Erlebnisse",
        "p1a": "Wenn der Sommer nach Natur und Frische ruft, bietet Macugnaga <strong>Alpenklima</strong>, Wege zwischen Lärchen und Bergangebote für Familien, Erwachsene und Begeisterte.",
        "p1b": "Vom <strong>8. bis 20. August</strong> bündelt das Buchungsportal die online verfügbaren Erlebnisse: Wald-Wellness, Kulturbesuche, Goldmine, Trekking und sanfte Aktivitäten.",
        "li": [
            "Autorisierte Anbieter und qualifizierte Guides",
            "Online-Buchung mit sofortiger Bestätigung",
            "Ideen für einen Tagesausflug oder ein Wochenende mit Übernachtung",
        ],
        "img1_alt": "Blick auf das Dorf Macugnaga mit Walser-Häusern und Monte Rosa",
        "eyebrow2": "Nah bei den Städten und Seen",
        "h2_2": "Echte Berge, gut erreichbar",
        "p2a": "Macugnaga ist in etwa 1,5–2,5 Stunden von <strong>Mailand</strong>, <strong>Varese</strong>, <strong>Novara</strong> und dem <strong>Lago Maggiore</strong> erreichbar — und auch von <strong>Orta</strong>, <strong>Mergozzo</strong> und Turin.",
        "p2b": 'Perfekt als <a href="fuga-citta.html">Stadtflucht</a> oder Bergtag, wenn Sie in einem Hotel oder Campingplatz an den Seen übernachten: frische Luft, Alpendorf und Monte-Rosa-Panorama ohne lange Anreise.',
        "btn_fuga": "Stadtflucht",
        "btn_fam": "Berg mit Kindern",
        "img2_alt": "Macugnaga und Monte Rosa von oben",
        "eyebrow3": "Aufenthalt mit Übernachtung",
        "h2_3": "Schlafen und aufwachen am Fuß des Rosa…",
        "p3a": "Zwischen dem 8. und 20. August macht ein <strong>Aufenthalt mit Übernachtung</strong> den Bergsommer vollständiger: Sonnenauf- und -untergang am Monte Rosa, ein oder zwei online gebuchte Erlebnisse, Dorfspaziergänge und lokale Küche.",
        "p3b": 'Wählen Sie Hotel, B&amp;B oder Ferienhaus und buchen Sie dann die Aktivitäten unten. Praktischer Leitfaden unter <a href="weekend.html">Wochenend-Ideen</a>.',
        "btn_week": "Aufenthalt planen",
        "btn_sleep": "Unterkunft",
        "img3_alt": "Landschaft von Macugnaga im Valle Anzasca",
        "eyebrow4": "Online buchen",
        "h2_4": "Buchbare Erlebnisse vom 8. bis 20. August",
        "p4": 'Aktuelle Liste der Aktivitäten mit Verfügbarkeit zwischen dem <strong>8.</strong> und <strong>20. August 2026</strong>. Datum und Plätze wählen, online zahlen und sofort Bestätigung mit Kontakten der Guides erhalten. Für den vollständigen Katalog siehe <a href="esperienze.html">alle Erlebnisse</a>.',
        "aria_list": "Buchbare Erlebnisse 8.–20. August",
        "loading": "Erlebnisse werden geladen…",
        "faq_eyebrow": "FAQ",
        "faq_h2": "Häufige Fragen zu Bergen im August (8.–20. August)",
        "faq": [
            (
                "Welche Erlebnisse kann ich vom 8. bis 20. August in Macugnaga buchen?",
                'Die Liste auf dieser Seite zeigt alle Erlebnisse des Buchungsportals mit Verfügbarkeit zwischen dem 8. und 20. August 2026: Wälder und Natur, <a href="casa-museo-walser.html">Walser-Hausmuseum</a>, <a href="miniera-oro.html">Goldmine</a>, Trekking und sanfte Aktivitäten am Fuß des Monte Rosa.',
            ),
            (
                "Eignet sich Macugnaga als Hitzeflucht nahe Mailand und den Seen?",
                'Ja: kühles Alpenklima nah bei Mailand, Varese, Novara und den Seen Maggiore, Orta und Mergozzo. Siehe auch <a href="fuga-citta.html">Stadtflucht</a>.',
            ),
            (
                "Wie plane ich ein Wochenende mit Übernachtung?",
                'Unterkunft in Macugnaga, ein oder zwei online gebuchte Erlebnisse und Dorfspaziergänge. Leitfaden unter <a href="weekend.html">Wochenende</a> und Liste <a href="https://macugnaga-monterosa.it/contenuti/306635/dove-dormire" target="_blank" rel="noopener">Unterkunft</a>.',
            ),
        ],
        "note": 'Informationen, Preise und Verfügbarkeit des Buchungsportals werden von den Anbietern angegeben. Nach der Buchung erhalten Sie die Kontakte der Organisatoren. <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> ist nicht für die Durchführung der Aktivitäten verantwortlich. <a href="credits.html">Weitere Informationen</a>',
        "cookie_label": "Cookie-Hinweis",
        "cookie_p": 'Diese Website verwendet technisch notwendige Cookies sowie Dienste Dritter für die Online-Buchung und Schriftarten. <a href="privacy.html">Datenschutz und Cookies</a>',
        "cookie_ok": "Akzeptieren",
        "cookie_ess": "Nur Essenzielle",
        "web_name": "Berge im August — Erlebnisse vom 8. bis 20. August in Macugnaga",
        "web_desc": "Alle online buchbaren Erlebnisse in Macugnaga Monte Rosa vom 8. bis 20. August 2026, am Fuß des Monte Rosa.",
        "list_name": "Buchbare Erlebnisse in Macugnaga vom 8. bis 20. August",
        "list_desc": "Bergaktivitäten online buchbar in Macugnaga Monte Rosa vom 8. bis 20. August 2026.",
        "bc_name": "8.–20. August",
        "site_name": "Macugnaga Booking – Erlebnisse am Fuß des Monte Rosa",
        "faq_schema": [
            (
                "Welche Erlebnisse kann ich vom 8. bis 20. August in Macugnaga buchen?",
                "Zwischen dem 8. und 20. August 2026 können Sie online Erlebnisse in Wäldern und Natur, Besuche im Walser-Hausmuseum und in der Goldmine, Trekking und sanfte Aktivitäten am Fuß des Monte Rosa buchen.",
            ),
            (
                "Eignet sich Macugnaga als Hitzeflucht nahe Mailand und den Seen?",
                "Ja: Macugnaga bietet kühle Bergluft nah bei Mailand, Varese, Novara und den Seen Maggiore, Orta und Mergozzo. Ideal für einen Tagesausflug oder ein Wochenende mit Übernachtung außerhalb der Stadt.",
            ),
            (
                "Wie plane ich ein Wochenende mit Übernachtung vom 8. bis 20. August?",
                "Wählen Sie Hotel, B&B oder Ferienhaus in Macugnaga, buchen Sie online ein oder zwei Erlebnisse für den 8.–20. August und kombinieren Sie Dorfspaziergänge, Wälder und, sofern geöffnet, die Bergbahnen.",
            ),
        ],
        "noscript": [
            ("miniera-oro.html", "Goldmine Guia"),
            ("casa-museo-walser.html", "Walser-Hausmuseum in Borca"),
            ("esperienze.html", "Alle buchbaren Erlebnisse"),
            ("weekend.html", "Wochenend-Ideen in Macugnaga"),
            ("famiglie.html", "Berg mit Kindern"),
        ],
        "footer_note": "Automatische Übersetzung aus der offiziellen italienischen Fassung",
    },
}


def itemlist_json(lang: str, p: dict) -> str:
    parts = []
    for i, (name, href) in enumerate(ITEMLIST[lang], 1):
        url = f"{BASE}/{p['dir']}{href}"
        parts.append(
            f"""      {{
        "@type": "ListItem",
        "position": {i},
        "name": {j(name)},
        "url": {j(url)}
      }}"""
        )
    return ",\n".join(parts)


def faq_schema_json(p: dict) -> str:
    parts = []
    for q, a in p["faq_schema"]:
        parts.append(
            f"""      {{
        "@type": "Question",
        "name": {j(q)},
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": {j(a)}
        }}
      }}"""
        )
    return ",\n".join(parts)


def nav_html(p: dict) -> str:
    links = "\n".join(f'        <a href="{h}">{t}</a>' for h, t in p["nav"])
    return f"""  <nav class="seo-nav-fallback" aria-label="{p['nav_label']}">
{links}
        <a class="nav-cta" href="esperienze.html">{p['nav_cta']}</a>
  </nav>"""


def build(lang: str, p: dict) -> Path:
    pref = p["prefix"]
    canon = URLS[lang]
    items = itemlist_json(lang, p)
    faqs = faq_schema_json(p)
    home_url = f"{BASE}/" if lang == "it" else f"{BASE}/{lang}/"
    exp_url = f"{BASE}/{p['dir']}esperienze.html"
    img = f"{BASE}/assets/web/landing-agosto-aria-fresca.jpg"
    li = "\n".join(f"            <li>{x}</li>" for x in p["li"])
    faq_html = "\n".join(
        f"""          <details class="faq-item reveal">
            <summary>{q}</summary>
            <p class="faq-a">{a}</p>
          </details>"""
        for q, a in p["faq"]
    )
    noscript = "\n".join(
        f'            <li><a href="{h}">{t}</a></li>' for h, t in p["noscript"]
    )
    footer_note = ""
    if p.get("footer_note"):
        footer_note = (
            f'\n  <p class="footer-translation-note container" hidden>'
            f'{p["footer_note"]}</p>'
        )

    html = f"""<!DOCTYPE html>
<html lang="{p['lang']}">
<head>
  <meta charset="utf-8">
  <script src="{pref}js/lang-pref.js?v=1"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{p['title']}</title>
  <meta name="description" content="{p['description']}">
  <link rel="canonical" href="{canon}">
  <link rel="alternate" hreflang="it" href="{URLS['it']}">
  <link rel="alternate" hreflang="en" href="{URLS['en']}">
  <link rel="alternate" hreflang="fr" href="{URLS['fr']}">
  <link rel="alternate" hreflang="de" href="{URLS['de']}">
  <link rel="alternate" hreflang="x-default" href="{URLS['it']}">
  <meta property="og:title" content="{p['og_title']}">
  <meta property="og:description" content="{p['og_desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canon}">
  <meta property="og:locale" content="{p['locale']}">
  <meta property="og:site_name" content="{p['site_name']}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{p['tw_title']}">
  <meta name="twitter:description" content="{p['og_desc']}">
  <meta name="twitter:image" content="{img}">
  <meta name="twitter:url" content="{canon}">
  <meta property="og:image" content="{img}">
  <meta name="geo.region" content="IT-VB">
  <meta name="geo.placename" content="Macugnaga">
  <meta name="geo.position" content="45.9667;7.9667">
  <meta name="ICBM" content="45.9667, 7.9667">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Open+Sans:wght@400;600;700&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet"></noscript>
  <link rel="preload" href="{pref}css/style.css?v=22" as="style">
  <link rel="stylesheet" href="{pref}css/style.css?v=22">
  <link rel="stylesheet" href="https://www.planyo.com/li.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": {j(p['breadcrumb_home'])}, "item": {j(home_url)}}},
      {{"@type": "ListItem", "position": 2, "name": {j(p['breadcrumb_exp'])}, "item": {j(exp_url)}}},
      {{"@type": "ListItem", "position": 3, "name": {j(p['bc_name'])}, "item": {j(canon)}}}
    ]
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": {j(p['web_name'])},
    "description": {j(p['web_desc'])},
    "url": {j(canon)},
    "inLanguage": {j(p['lang'])},
    "isPartOf": {{
      "@type": "WebSite",
      "name": "Macugnaga Booking",
      "url": {j(home_url)}
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
    "temporalCoverage": "2026-08-08/2026-08-20"
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": {j(p['list_name'])},
    "description": {j(p['list_desc'])},
    "url": {j(canon)},
    "numberOfItems": 4,
    "itemListElement": [
{items}
    ]
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{faqs}
    ]
  }}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">{p['skip']}</a>
  <div id="site-header">
{nav_html(p)}
</div>
  <div id="site-search"></div>

  <main id="main">
    <header class="page-hero">
      <div class="page-hero__media">
        <picture>
          <source type="image/webp" srcset="{pref}assets/web/landing-agosto-aria-fresca-800.webp 800w, {pref}assets/web/landing-agosto-aria-fresca-1200.webp 1200w, {pref}assets/web/landing-agosto-aria-fresca.webp 1600w" sizes="100vw">
          <img src="{pref}assets/web/landing-agosto-aria-fresca.jpg" srcset="{pref}assets/web/landing-agosto-aria-fresca-800.jpg 800w, {pref}assets/web/landing-agosto-aria-fresca-1200.jpg 1200w, {pref}assets/web/landing-agosto-aria-fresca.jpg 1600w" sizes="100vw" alt="{p['img1_alt']}" width="1600" height="842" fetchpriority="high" decoding="async">
        </picture>
      </div>
      <div class="page-hero__scrim" aria-hidden="true"></div>
      <div class="page-hero__content">
        <p class="breadcrumb"><a href="index.html">{p['breadcrumb_home']}</a> · <a href="esperienze.html">{p['breadcrumb_exp']}</a> · {p['crumb']}</p>
        <h1>{p['h1']}</h1>
        <p>{p['hero_p']}</p>
      </div>
    </header>

    <section class="section section--white">
      <div class="container split">
        <div class="reveal prose">
          <p class="section__eyebrow">{p['eyebrow1']}</p>
          <h2>{p['h2_1']}</h2>
          <p>{p['p1a']}</p>
          <p>{p['p1b']}</p>
          <ul>
{li}
          </ul>
        </div>
        <div class="split__media reveal">
          <picture>
            <source type="image/webp" srcset="{pref}assets/web/landing-agosto-aria-fresca-800.webp 800w, {pref}assets/web/landing-agosto-aria-fresca-1200.webp 1200w, {pref}assets/web/landing-agosto-aria-fresca.webp 1600w" sizes="(max-width:720px) 100vw, 50vw">
            <img src="{pref}assets/web/landing-agosto-aria-fresca.jpg" srcset="{pref}assets/web/landing-agosto-aria-fresca-800.jpg 800w, {pref}assets/web/landing-agosto-aria-fresca-1200.jpg 1200w, {pref}assets/web/landing-agosto-aria-fresca.jpg 1600w" sizes="(max-width:720px) 100vw, 50vw" alt="{p['img1_alt']}" width="800" height="421" loading="lazy" decoding="async">
          </picture>
        </div>
      </div>
    </section>

    <section class="section section--cream">
      <div class="container split split--rev">
        <div class="split__media reveal">
          <picture>
            <source type="image/webp" srcset="{pref}assets/web/drone-monterosa-800.webp 800w, {pref}assets/web/drone-monterosa-1200.webp 1200w, {pref}assets/web/drone-monterosa.webp 1600w" sizes="(max-width:720px) 100vw, 50vw">
            <img src="{pref}assets/web/drone-monterosa.jpg" srcset="{pref}assets/web/drone-monterosa-800.jpg 800w, {pref}assets/web/drone-monterosa-1200.jpg 1200w, {pref}assets/web/drone-monterosa.jpg 1600w" sizes="(max-width:720px) 100vw, 50vw" alt="{p['img2_alt']}" width="800" height="600" loading="lazy" decoding="async">
          </picture>
        </div>
        <div class="reveal prose">
          <p class="section__eyebrow">{p['eyebrow2']}</p>
          <h2>{p['h2_2']}</h2>
          <p>{p['p2a']}</p>
          <p>{p['p2b']}</p>
          <div class="btn-row">
            <a class="btn btn--outline" href="fuga-citta.html">{p['btn_fuga']}</a>
            <a class="btn btn--outline" href="famiglie.html">{p['btn_fam']}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container split">
        <div class="reveal prose">
          <p class="section__eyebrow">{p['eyebrow3']}</p>
          <h2>{p['h2_3']}</h2>
          <p>{p['p3a']}</p>
          <p>{p['p3b']}</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="weekend.html">{p['btn_week']}</a>
            <a class="btn btn--outline" href="https://macugnaga-monterosa.it/contenuti/306635/dove-dormire" target="_blank" rel="noopener">{p['btn_sleep']}</a>
          </div>
        </div>
        <div class="split__media reveal">
          <picture>
            <source type="image/webp" srcset="{pref}assets/web/ossola-macugnaga-800.webp 800w, {pref}assets/web/ossola-macugnaga-1200.webp 1200w, {pref}assets/web/ossola-macugnaga.webp 1600w" sizes="(max-width:720px) 100vw, 50vw">
            <img src="{pref}assets/web/ossola-macugnaga.jpg" srcset="{pref}assets/web/ossola-macugnaga-800.jpg 800w, {pref}assets/web/ossola-macugnaga-1200.jpg 1200w, {pref}assets/web/ossola-macugnaga.jpg 1600w" sizes="(max-width:720px) 100vw, 50vw" alt="{p['img3_alt']}" width="800" height="600" loading="lazy" decoding="async">
          </picture>
        </div>
      </div>
    </section>

    <section class="section section--cream" style="padding-bottom:1rem" id="prenota">
      <div class="container prose reveal">
        <p class="section__eyebrow">{p['eyebrow4']}</p>
        <h2>{p['h2_4']}</h2>
        <p>{p['p4']}</p>
      </div>
    </section>

    <section class="planyo-wrap esperienze-list-wrap" aria-label="{p['aria_list']}">
      <div class="container">
        <div id="esperienze-list" class="esperienze-list" data-date-from="2026-08-08" data-date-to="2026-08-20" aria-live="polite">
          <p class="esperienze-list__status">{p['loading']}</p>
        </div>
        <noscript>
          <ul class="esperienze-static">
{noscript}
          </ul>
        </noscript>
      </div>
    </section>

    <section class="section section--white" id="faq">
      <div class="container">
        <p class="section__eyebrow reveal">{p['faq_eyebrow']}</p>
        <h2 class="reveal">{p['faq_h2']}</h2>
        <div class="faq-list" style="margin-top:1.25rem">
{faq_html}
        </div>
        <p class="note" style="margin-top:1.75rem;max-width:48rem">{p['note']}</p>
      </div>
    </section>
  </main>
{footer_note}
  <div id="site-footer"></div>
  <div id="cookie-banner" class="cookie-banner" role="dialog" aria-label="{p['cookie_label']}">
    <p>{p['cookie_p']}</p>
    <div class="cookie-banner__actions">
      <button type="button" class="btn btn--primary" data-cookie-accept>{p['cookie_ok']}</button>
      <button type="button" class="btn btn--outline" data-cookie-essential>{p['cookie_ess']}</button>
    </div>
  </div>
  <script type="text/javascript" src="https://www.planyo.com/li.js?v=3"></script>
  <script src="{pref}js/i18n.js?v=10" defer></script>
  <script src="{pref}js/partials.js?v=18" defer></script>
  <script src="{pref}js/main.js?v=3" defer></script>
  <script src="{pref}js/esperienze-list.js?v=15" defer></script>
</body>
</html>
"""
    out = ROOT / p["dir"] / SLUG if p["dir"] else ROOT / SLUG
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


def main() -> None:
    for lang, p in PAGES.items():
        out = build(lang, p)
        print("wrote", out.relative_to(ROOT), out.stat().st_size)


if __name__ == "__main__":
    main()
