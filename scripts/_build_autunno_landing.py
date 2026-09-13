#!/usr/bin/env python3
"""Build autumn landing pages (IT/EN/FR/DE) through 31 October 2026."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.macugnagabooking.it"
SLUG = "autunno-ai-piedi-del-monte-rosa.html"
DATE_TO = "2026-10-31"
LASTMOD = "2026-09-13"
CSS_V = "25"
I18N_V = "13"
PARTIALS_V = "24"
MAIN_V = "3"
LIST_V = "25"

NAV = {
    "it": [
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
    "en": [
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
    "fr": [
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
    "de": [
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
}

COPY = {
    "it": {
        "lang": "it",
        "dir": "",
        "prefix": "",
        "og_locale": "it_IT",
        "in_language": "it",
        "translation_note": False,
        "title": "Con l’autunno che si avvicina la montagna è ancora più bella | Macugnaga Booking",
        "meta_desc": "Con l’autunno che si avvicina la montagna è ancora più bella. Ecco cosa puoi fare ai piedi del Monte Rosa: esperienze prenotabili online a Macugnaga da oggi fino al 31 ottobre 2026.",
        "og_title": "Autunno ai piedi del Monte Rosa | Macugnaga Booking",
        "og_desc": "Con l’autunno che si avvicina la montagna è ancora più bella. Esperienze prenotabili fino al 31 ottobre 2026 a Macugnaga.",
        "tw_title": "Autunno ai piedi del Monte Rosa — fino al 31 ottobre | Macugnaga",
        "crumb_label": "Autunno",
        "h1": "Con l’autunno che si avvicina la montagna è ancora più bella",
        "hero_lead": "Ecco cosa puoi fare ai piedi del Monte Rosa: esperienze prenotabili da oggi fino al 31 ottobre.",
        "eyebrow1": "Stagione autunnale",
        "h2_1": "Colori, aria tersa e passi lenti",
        "p1a": "A settembre e ottobre Macugnaga mostra i larici che virano all’oro, il cielo più nitido e sentieri meno affollati. È il momento giusto per <strong>forest bathing</strong>, yoga, cultura Walser e una giornata alla ricerca dell’oro.",
        "p1b": "Fino al <strong>31 ottobre</strong> il portale di prenotazione raccoglie le esperienze con date in calendario: natura, benessere, miniera, Casa Museo Walser e proposte per tutta la famiglia.",
        "li1": "Operatori autorizzati e guide qualificate",
        "li2": "Prenotazione online con conferma immediata",
        "li3": "Idee per una giornata o un weekend in quota",
        "eyebrow2": "Vicino alle città e ai laghi",
        "h2_2": "La montagna vera, a portata di strada",
        "p2a": "Macugnaga è raggiungibile in circa 1,5–2,5 ore da <strong>Milano</strong>, <strong>Varese</strong>, <strong>Novara</strong> e dal <strong>Lago Maggiore</strong> — e anche da <strong>Orta</strong>, <strong>Mergozzo</strong> e Torino.",
        "p2b": "Perfetta come <a href=\"fuga-citta.html\">fuga dalla città</a> o come giornata in montagna se soggiorni sui laghi: aria fresca, paese alpino e panorami sul Monte Rosa.",
        "btn_fuga": "Fuga dalla città",
        "btn_fam": "Montagna con i bambini",
        "eyebrow3": "Soggiorno con pernottamento",
        "h2_3": "Dormire e risvegliarsi ai piedi del Rosa…",
        "p3a": "Un <strong>soggiorno con pernottamento</strong> rende l’autunno più completo: alba e tramonto sul Monte Rosa, una o due esperienze prenotate online, passeggiate in paese e cucina locale.",
        "p3b": "Scegli hotel, B&amp;B o casa vacanza, poi prenota le attività qui sotto. Guida pratica su <a href=\"weekend.html\">Idee weekend</a>.",
        "btn_week": "Organizza soggiorno",
        "btn_sleep": "Dove dormire",
        "eyebrow4": "Prenota online",
        "h2_4": "Esperienze prenotabili fino al 31 ottobre",
        "p4": "Elenco aggiornato delle attività con disponibilità da <strong>oggi</strong> fino al <strong>31 ottobre 2026</strong>. Scegli data e posti, paga online e ricevi subito conferma con i contatti delle guide. Per il catalogo completo vedi <a href=\"esperienze.html\">tutte le esperienze</a>.",
        "list_aria": "Esperienze prenotabili fino al 31 ottobre",
        "list_loading": "Caricamento esperienze…",
        "ns_mine": "Miniera d’oro della Guia",
        "ns_walser": "Casa Museo Walser di Borca",
        "ns_all": "Tutte le esperienze prenotabili",
        "ns_week": "Idee weekend a Macugnaga",
        "ns_fam": "Montagna con i bambini",
        "faq_h2": "Domande frequenti sull’autunno a Macugnaga",
        "faq1_q": "Quali esperienze posso prenotare fino al 31 ottobre a Macugnaga?",
        "faq1_a": "L’elenco in questa pagina mostra le esperienze del portale di prenotazione con disponibilità da oggi fino al 31 ottobre 2026: boschi e natura, Casa Museo Walser, miniera d’oro, yoga, ricerca dell’oro e attività per famiglie ai piedi del Monte Rosa.",
        "faq2_q": "Perché venire a Macugnaga in autunno?",
        "faq2_a": "L’autunno porta colori, clima fresco e sentieri più tranquilli, a poca distanza da Milano, Varese, Novara e dai laghi Maggiore, d’Orta e di Mergozzo. Ideale per una giornata o un weekend.",
        "faq3_q": "Come organizzare un weekend con pernottamento?",
        "faq3_a": "Alloggio a Macugnaga, una o due esperienze prenotate online e passeggiate in paese. Guida su Weekend e elenco dove dormire sul sito Macugnaga Monterosa.",
        "note": "Informazioni, prezzi e disponibilità del portale di prenotazione sono indicati dai gestori. Dopo la prenotazione riceverai i contatti degli organizzatori. <a href=\"https://www.raccontidigitali.it\" target=\"_blank\" rel=\"noopener\">Lem s.r.l.</a> non è responsabile della gestione delle attività. <a href=\"credits.html\">Maggiori informazioni</a>",
        "skip": "Vai al contenuto",
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
        "bc_page": "Autunno ai piedi del Monte Rosa",
        "web_name": "Con l’autunno che si avvicina la montagna è ancora più bella — Esperienze fino al 31 ottobre a Macugnaga",
        "web_desc": "Esperienze prenotabili online a Macugnaga Monte Rosa da oggi fino al 31 ottobre 2026, ai piedi del Monte Rosa.",
        "list_name": "Esperienze prenotabili a Macugnaga fino al 31 ottobre",
        "list_desc": "Attività in montagna prenotabili online a Macugnaga Monte Rosa fino al 31 ottobre 2026.",
    },
    "en": {
        "lang": "en",
        "dir": "en/",
        "prefix": "../",
        "og_locale": "en_GB",
        "in_language": "en",
        "translation_note": True,
        "title": "As autumn approaches, the mountains are even more beautiful | Macugnaga Booking",
        "meta_desc": "As autumn approaches, the mountains are even more beautiful. Here’s what you can do at the foot of Monte Rosa: experiences bookable online in Macugnaga through 31 October 2026.",
        "og_title": "Autumn at the foot of Monte Rosa | Macugnaga Booking",
        "og_desc": "As autumn approaches, the mountains are even more beautiful. Bookable experiences in Macugnaga through 31 October 2026.",
        "tw_title": "Autumn at the foot of Monte Rosa — through 31 October | Macugnaga",
        "crumb_label": "Autumn",
        "h1": "As autumn approaches, the mountains are even more beautiful",
        "hero_lead": "Here’s what you can do at the foot of Monte Rosa: experiences bookable from today through 31 October.",
        "eyebrow1": "Autumn season",
        "h2_1": "Colours, clear air and a slower pace",
        "p1a": "In September and October Macugnaga shows larches turning gold, clearer skies and quieter trails. The right time for <strong>forest bathing</strong>, yoga, Walser culture and a day gold-panning.",
        "p1b": "Through <strong>31 October</strong> the booking portal lists experiences with dates on the calendar: nature, wellness, the gold mine, the Walser House Museum and family ideas.",
        "li1": "Authorised operators and qualified guides",
        "li2": "Online booking with instant confirmation",
        "li3": "Ideas for a day trip or a weekend up high",
        "eyebrow2": "Close to cities and lakes",
        "h2_2": "Real mountains, an easy drive away",
        "p2a": "Macugnaga is about 1.5–2.5 hours from <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> and <strong>Lake Maggiore</strong> — and also from <strong>Orta</strong>, <strong>Mergozzo</strong> and Turin.",
        "p2b": "Perfect as a <a href=\"fuga-citta.html\">city escape</a> or a mountain day if you are staying by the lakes: fresh air, an alpine village and Monte Rosa views.",
        "btn_fuga": "City escape",
        "btn_fam": "Mountains with children",
        "eyebrow3": "Stay overnight",
        "h2_3": "Sleep and wake at the foot of Monte Rosa…",
        "p3a": "An <strong>overnight stay</strong> makes autumn fuller: sunrise and sunset on Monte Rosa, one or two experiences booked online, village walks and local food.",
        "p3b": "Choose a hotel, B&amp;B or holiday home, then book the activities below. Practical guide: <a href=\"weekend.html\">Weekend ideas</a>.",
        "btn_week": "Plan a stay",
        "btn_sleep": "Where to stay",
        "eyebrow4": "Book online",
        "h2_4": "Experiences bookable through 31 October",
        "p4": "Updated list of activities available from <strong>today</strong> through <strong>31 October 2026</strong>. Choose date and places, pay online and get instant confirmation with guide contacts. For the full catalogue see <a href=\"esperienze.html\">all experiences</a>.",
        "list_aria": "Experiences bookable through 31 October",
        "list_loading": "Loading experiences…",
        "ns_mine": "Guia gold mine",
        "ns_walser": "Walser House Museum in Borca",
        "ns_all": "All bookable experiences",
        "ns_week": "Weekend ideas in Macugnaga",
        "ns_fam": "Mountains with children",
        "faq_h2": "Frequently asked questions about autumn in Macugnaga",
        "faq1_q": "Which experiences can I book through 31 October in Macugnaga?",
        "faq1_a": "This page lists booking-portal experiences with availability from today through 31 October 2026: woods and nature, the Walser House Museum, the gold mine, yoga, gold panning and family activities at the foot of Monte Rosa.",
        "faq2_q": "Why visit Macugnaga in autumn?",
        "faq2_a": "Autumn brings colours, cool air and quieter trails, a short drive from Milan, Varese, Novara and Lakes Maggiore, Orta and Mergozzo. Ideal for a day or a weekend.",
        "faq3_q": "How do I plan a weekend with an overnight stay?",
        "faq3_a": "Stay in Macugnaga, book one or two experiences online and walk the village. See the Weekend page and the where-to-stay list on the Macugnaga Monterosa site.",
        "note": "Information, prices and availability on the booking portal are provided by the operators. After booking you will receive the organisers’ contacts. <a href=\"https://www.raccontidigitali.it\" target=\"_blank\" rel=\"noopener\">Lem s.r.l.</a> is not responsible for running the activities. <a href=\"credits.html\">More information</a>",
        "skip": "Skip to content",
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
        "bc_page": "Autumn at the foot of Monte Rosa",
        "web_name": "As autumn approaches, the mountains are even more beautiful — Experiences through 31 October in Macugnaga",
        "web_desc": "Experiences bookable online in Macugnaga Monte Rosa from today through 31 October 2026, at the foot of Monte Rosa.",
        "list_name": "Experiences bookable in Macugnaga through 31 October",
        "list_desc": "Mountain activities bookable online in Macugnaga Monte Rosa through 31 October 2026.",
    },
    "fr": {
        "lang": "fr",
        "dir": "fr/",
        "prefix": "../",
        "og_locale": "fr_FR",
        "in_language": "fr",
        "translation_note": True,
        "title": "Avec l’automne qui approche, la montagne est encore plus belle | Macugnaga Booking",
        "meta_desc": "Avec l’automne qui approche, la montagne est encore plus belle. Voici ce que vous pouvez faire au pied du Mont Rose : expériences réservables en ligne à Macugnaga jusqu’au 31 octobre 2026.",
        "og_title": "Automne au pied du Mont Rose | Macugnaga Booking",
        "og_desc": "Avec l’automne qui approche, la montagne est encore plus belle. Expériences réservables à Macugnaga jusqu’au 31 octobre 2026.",
        "tw_title": "Automne au pied du Mont Rose — jusqu’au 31 octobre | Macugnaga",
        "crumb_label": "Automne",
        "h1": "Avec l’automne qui approche, la montagne est encore plus belle",
        "hero_lead": "Voici ce que vous pouvez faire au pied du Mont Rose : expériences réservables d’aujourd’hui au 31 octobre.",
        "eyebrow1": "Saison d’automne",
        "h2_1": "Couleurs, air vif et pas lents",
        "p1a": "En septembre et octobre, Macugnaga montre les mélèzes dorés, un ciel plus net et des sentiers plus calmes. Le bon moment pour le <strong>bain de forêt</strong>, le yoga, la culture walser et une journée à la recherche de l’or.",
        "p1b": "Jusqu’au <strong>31 octobre</strong>, le portail de réservation rassemble les expériences avec des dates au calendrier : nature, bien-être, mine d’or, Maison-musée walser et idées pour toute la famille.",
        "li1": "Opérateurs autorisés et guides qualifiés",
        "li2": "Réservation en ligne avec confirmation immédiate",
        "li3": "Idées pour une journée ou un week-end en altitude",
        "eyebrow2": "Près des villes et des lacs",
        "h2_2": "La vraie montagne, à portée de route",
        "p2a": "Macugnaga est à environ 1,5–2,5 h de <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novare</strong> et du <strong>lac Majeur</strong> — et aussi d’<strong>Orta</strong>, <strong>Mergozzo</strong> et Turin.",
        "p2b": "Parfaite comme <a href=\"fuga-citta.html\">évasion de la ville</a> ou journée à la montagne si vous séjournez au bord des lacs : air frais, village alpin et vues sur le Mont Rose.",
        "btn_fuga": "Évasion de la ville",
        "btn_fam": "Montagne avec les enfants",
        "eyebrow3": "Séjour avec nuitée",
        "h2_3": "Dormir et se réveiller au pied du Rose…",
        "p3a": "Un <strong>séjour avec nuitée</strong> rend l’automne plus complet : aube et coucher de soleil sur le Mont Rose, une ou deux expériences réservées en ligne, promenades au village et cuisine locale.",
        "p3b": "Choisissez hôtel, B&amp;B ou maison de vacances, puis réservez les activités ci-dessous. Guide pratique : <a href=\"weekend.html\">Idées week-end</a>.",
        "btn_week": "Organiser un séjour",
        "btn_sleep": "Où dormir",
        "eyebrow4": "Réserver en ligne",
        "h2_4": "Expériences réservables jusqu’au 31 octobre",
        "p4": "Liste à jour des activités disponibles d’<strong>aujourd’hui</strong> au <strong>31 octobre 2026</strong>. Choisissez date et places, payez en ligne et recevez tout de suite la confirmation avec les contacts des guides. Pour le catalogue complet, voir <a href=\"esperienze.html\">toutes les expériences</a>.",
        "list_aria": "Expériences réservables jusqu’au 31 octobre",
        "list_loading": "Chargement des expériences…",
        "ns_mine": "Mine d’or de la Guia",
        "ns_walser": "Maison-musée walser de Borca",
        "ns_all": "Toutes les expériences réservables",
        "ns_week": "Idées week-end à Macugnaga",
        "ns_fam": "Montagne avec les enfants",
        "faq_h2": "Questions fréquentes sur l’automne à Macugnaga",
        "faq1_q": "Quelles expériences puis-je réserver jusqu’au 31 octobre à Macugnaga ?",
        "faq1_a": "Cette page liste les expériences du portail de réservation disponibles d’aujourd’hui au 31 octobre 2026 : bois et nature, Maison-musée walser, mine d’or, yoga, recherche de l’or et activités familiales au pied du Mont Rose.",
        "faq2_q": "Pourquoi venir à Macugnaga en automne ?",
        "faq2_a": "L’automne apporte couleurs, air frais et sentiers plus calmes, à peu de distance de Milan, Varese, Novare et des lacs Majeur, d’Orta et de Mergozzo. Idéal pour une journée ou un week-end.",
        "faq3_q": "Comment organiser un week-end avec nuitée ?",
        "faq3_a": "Hébergement à Macugnaga, une ou deux expériences réservées en ligne et promenades au village. Voir la page Week-end et la liste où dormir sur le site Macugnaga Monterosa.",
        "note": "Informations, prix et disponibilités du portail de réservation sont indiqués par les gestionnaires. Après la réservation, vous recevrez les contacts des organisateurs. <a href=\"https://www.raccontidigitali.it\" target=\"_blank\" rel=\"noopener\">Lem s.r.l.</a> n’est pas responsable de la gestion des activités. <a href=\"credits.html\">Plus d’informations</a>",
        "skip": "Aller au contenu",
        "nav_cta": "Réserver en ligne",
        "nav_aria": "Navigation principale",
        "crumb_home": "Accueil",
        "crumb_exp": "Expériences",
        "cookie_aria": "Information cookies",
        "cookie_text": "Ce site utilise des cookies techniques nécessaires au fonctionnement et des services tiers pour la réservation en ligne et les polices. <a href=\"privacy.html\">Confidentialité et cookies</a>",
        "cookie_ok": "Accepter",
        "cookie_ess": "Essentiels uniquement",
        "img_alt_hero": "Vue du Dorf de Macugnaga avec maisons walser et Mont Rose",
        "img_alt_drone": "Macugnaga et le Mont Rose vus du ciel",
        "img_alt_ossola": "Paysage de Macugnaga dans le val Anzasca",
        "bc_home": "Accueil",
        "bc_exp": "Expériences",
        "bc_page": "Automne au pied du Mont Rose",
        "web_name": "Avec l’automne qui approche, la montagne est encore plus belle — Expériences jusqu’au 31 octobre à Macugnaga",
        "web_desc": "Expériences réservables en ligne à Macugnaga Mont Rose d’aujourd’hui au 31 octobre 2026, au pied du Mont Rose.",
        "list_name": "Expériences réservables à Macugnaga jusqu’au 31 octobre",
        "list_desc": "Activités de montagne réservables en ligne à Macugnaga Mont Rose jusqu’au 31 octobre 2026.",
    },
    "de": {
        "lang": "de",
        "dir": "de/",
        "prefix": "../",
        "og_locale": "de_DE",
        "in_language": "de",
        "translation_note": True,
        "title": "Der Herbst rückt näher — und die Berge sind noch schöner | Macugnaga Booking",
        "meta_desc": "Der Herbst rückt näher — und die Berge sind noch schöner. Das kannst du am Fuß des Monte Rosa erleben: online buchbare Erlebnisse in Macugnaga bis 31. Oktober 2026.",
        "og_title": "Herbst am Fuß des Monte Rosa | Macugnaga Booking",
        "og_desc": "Der Herbst rückt näher — und die Berge sind noch schöner. Buchbare Erlebnisse in Macugnaga bis 31. Oktober 2026.",
        "tw_title": "Herbst am Fuß des Monte Rosa — bis 31. Oktober | Macugnaga",
        "crumb_label": "Herbst",
        "h1": "Der Herbst rückt näher — und die Berge sind noch schöner",
        "hero_lead": "Das kannst du am Fuß des Monte Rosa erleben: buchbare Erlebnisse von heute bis 31. Oktober.",
        "eyebrow1": "Herbstzeit",
        "h2_1": "Farben, klare Luft und ruhige Schritte",
        "p1a": "Im September und Oktober zeigt Macugnaga goldene Lärchen, klareren Himmel und ruhigere Wege. Die richtige Zeit für <strong>Waldbaden</strong>, Yoga, Walser-Kultur und einen Tag Goldwaschen.",
        "p1b": "Bis zum <strong>31. Oktober</strong> sammelt das Buchungsportal Erlebnisse mit Terminen im Kalender: Natur, Wellness, Goldmine, Walser-Hausmuseum und Ideen für die ganze Familie.",
        "li1": "Zugelassene Anbieter und qualifizierte Guides",
        "li2": "Online-Buchung mit sofortiger Bestätigung",
        "li3": "Ideen für einen Tag oder ein Wochenende in der Höhe",
        "eyebrow2": "Nah an Städten und Seen",
        "h2_2": "Echte Berge, gut erreichbar",
        "p2a": "Macugnaga ist in etwa 1,5–2,5 Stunden von <strong>Mailand</strong>, <strong>Varese</strong>, <strong>Novara</strong> und dem <strong>Lago Maggiore</strong> erreichbar — und auch von <strong>Orta</strong>, <strong>Mergozzo</strong> und Turin.",
        "p2b": "Perfekt als <a href=\"fuga-citta.html\">Flucht aus der Stadt</a> oder als Bergtag, wenn du an den Seen wohnst: frische Luft, Alpendorf und Monte-Rosa-Panorama.",
        "btn_fuga": "Flucht aus der Stadt",
        "btn_fam": "Berge mit Kindern",
        "eyebrow3": "Übernachtung",
        "h2_3": "Schlafen und erwachen am Fuß des Rosa…",
        "p3a": "Ein <strong>Aufenthalt mit Übernachtung</strong> macht den Herbst voller: Sonnenauf- und -untergang am Monte Rosa, ein oder zwei online gebuchte Erlebnisse, Dorfspaziergänge und lokale Küche.",
        "p3b": "Wähle Hotel, B&amp;B oder Ferienhaus und buche dann die Aktivitäten unten. Praktischer Guide: <a href=\"weekend.html\">Wochenend-Ideen</a>.",
        "btn_week": "Aufenthalt planen",
        "btn_sleep": "Übernachten",
        "eyebrow4": "Online buchen",
        "h2_4": "Buchbare Erlebnisse bis 31. Oktober",
        "p4": "Aktuelle Liste der Aktivitäten mit Verfügbarkeit von <strong>heute</strong> bis zum <strong>31. Oktober 2026</strong>. Datum und Plätze wählen, online zahlen und sofort die Bestätigung mit Guide-Kontakten erhalten. Der vollständige Katalog: <a href=\"esperienze.html\">alle Erlebnisse</a>.",
        "list_aria": "Buchbare Erlebnisse bis 31. Oktober",
        "list_loading": "Erlebnisse werden geladen…",
        "ns_mine": "Goldmine della Guia",
        "ns_walser": "Walser-Hausmuseum in Borca",
        "ns_all": "Alle buchbaren Erlebnisse",
        "ns_week": "Wochenend-Ideen in Macugnaga",
        "ns_fam": "Berge mit Kindern",
        "faq_h2": "Häufige Fragen zum Herbst in Macugnaga",
        "faq1_q": "Welche Erlebnisse kann ich bis 31. Oktober in Macugnaga buchen?",
        "faq1_a": "Diese Seite zeigt Erlebnisse des Buchungsportals mit Verfügbarkeit von heute bis 31. Oktober 2026: Wälder und Natur, Walser-Hausmuseum, Goldmine, Yoga, Goldwaschen und Familienaktivitäten am Fuß des Monte Rosa.",
        "faq2_q": "Warum im Herbst nach Macugnaga kommen?",
        "faq2_a": "Der Herbst bringt Farben, kühle Luft und ruhigere Wege, nur eine kurze Fahrt von Mailand, Varese, Novara und den Seen Maggiore, Orta und Mergozzo. Ideal für einen Tag oder ein Wochenende.",
        "faq3_q": "Wie plane ich ein Wochenende mit Übernachtung?",
        "faq3_a": "Unterkunft in Macugnaga, ein oder zwei online gebuchte Erlebnisse und Dorfspaziergänge. Siehe die Wochenend-Seite und die Unterkunftsliste auf der Website Macugnaga Monterosa.",
        "note": "Informationen, Preise und Verfügbarkeit des Buchungsportals werden von den Betreibern angegeben. Nach der Buchung erhältst du die Kontakte der Organisatoren. <a href=\"https://www.raccontidigitali.it\" target=\"_blank\" rel=\"noopener\">Lem s.r.l.</a> ist nicht für die Durchführung der Aktivitäten verantwortlich. <a href=\"credits.html\">Weitere Informationen</a>",
        "skip": "Zum Inhalt",
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
        "bc_page": "Herbst am Fuß des Monte Rosa",
        "web_name": "Der Herbst rückt näher — und die Berge sind noch schöner — Erlebnisse bis 31. Oktober in Macugnaga",
        "web_desc": "Online buchbare Erlebnisse in Macugnaga Monte Rosa von heute bis 31. Oktober 2026, am Fuß des Monte Rosa.",
        "list_name": "Buchbare Erlebnisse in Macugnaga bis 31. Oktober",
        "list_desc": "Bergaktivitäten online buchbar in Macugnaga Monte Rosa bis 31. Oktober 2026.",
    },
}


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def abs_url(lang: str) -> str:
    return f"{SITE}/{COPY[lang]['dir']}{SLUG}"


def nav_html(lang: str, c: dict) -> str:
    links = "".join(f'\n        <a href="{href}">{label}</a>' for href, label in NAV[lang])
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
    "temporalCoverage": "2026-09-13/2026-10-31"
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
          "text": "{esc(c['faq1_a'])}"
        }}
      }},
      {{
        "@type": "Question",
        "name": "{esc(c['faq2_q'])}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{esc(c['faq2_a'])}"
        }}
      }},
      {{
        "@type": "Question",
        "name": "{esc(c['faq3_q'])}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{esc(c['faq3_a'])}"
        }}
      }}
    ]
  }}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">{c['skip']}</a>
  <div id="site-header">
  <nav class="seo-nav-fallback" aria-label="{c['nav_aria']}">{nav_html(lang, c)}
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


def main() -> None:
    for lang, c in COPY.items():
        dest = ROOT / c["dir"] / SLUG if c["dir"] else ROOT / SLUG
        dest.write_text(landing_html(lang), encoding="utf-8")
        print(f"wrote {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
