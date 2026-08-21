# -*- coding: utf-8 -*-
"""
Repair Italian leftovers in EN/FR/DE Macugnaga Booking pages.
Applies shared phrase fixes + full FAQ body/JSON replacements.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Shared phrase repairs (order matters: longer / more specific first)
# ---------------------------------------------------------------------------

SHARED_EN = [
    (
        "Within easy reach from <strong>Milano</strong>, <strong>Varese</strong>, <strong>Novara</strong> e dal <strong>Lake Maggiore</strong> (anche Orta e Mergozzo), and also from <strong>Torino</strong>, <strong>Genova</strong>, Canton <strong>Vallese</strong> e <strong>Ticino</strong>.",
        "Within easy reach from <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> and <strong>Lake Maggiore</strong> (including Orta and Mergozzo), and also from <strong>Turin</strong>, <strong>Genoa</strong>, Canton <strong>Valais</strong> and <strong>Ticino</strong>.",
    ),
    (
        "If you are staying in a hotel or campsite on <strong>Lake Maggiore</strong>, sul <strong>Lake Orta</strong> or on <strong>Lake Mergozzo</strong>",
        "If you are staying in a hotel or campsite on <strong>Lake Maggiore</strong>, on <strong>Lake Orta</strong> or on <strong>Lake Mergozzo</strong>",
    ),
    (
        "facilmente raggiungibile da <strong>Milano</strong>, <strong>Varese</strong>, <strong>Novara</strong> e dal <strong>Lake Maggiore</strong> (anche Orta e Mergozzo), and also from <strong>Torino</strong>, <strong>Genova</strong>, Canton <strong>Vallese</strong> e <strong>Ticino</strong>",
        "within easy reach of <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> and <strong>Lake Maggiore</strong> (including Orta and Mergozzo), and also from <strong>Turin</strong>, <strong>Genoa</strong>, Canton <strong>Valais</strong> and <strong>Ticino</strong>",
    ),
    (
        "raggiungibiland also froml Lake Maggiore",
        "also reachable from Lake Maggiore",
    ),
    (
        "and also froml Lake Maggiore",
        "and also from Lake Maggiore",
    ),
    (
        "Portale di prenotazione",
        "Booking portal",
    ),
    (
        "portale di prenotazione",
        "booking portal",
    ),
    (
        "Traduzione automatica dalla versione ufficiale in lingua italiana",
        "Automatic translation from the official Italian version.",
    ),
    (
        '"inLanguage": "it-IT"',
        '"inLanguage": "en-GB"',
    ),
    (
        "Online booking di esperienze in montagna a Macugnaga Monte Rosa: gite, weekend, escursioni, benessere, Walser House e miniera d'oro — vicino a Milano e al Lake Maggiore.",
        "Online booking of mountain experiences in Macugnaga Monte Rosa: day trips, weekends, hikes, wellness, Walser House and gold mine — near Milan and Lake Maggiore.",
    ),
    (
        "Book online gite ed esperienze a Macugnaga Monte Rosa: escursioni, benessere e natura vicino a Milano, al Lake Maggiore, Varese e Novara.",
        "Book online day trips and experiences in Macugnaga Monte Rosa: hikes, wellness and nature near Milan, Lake Maggiore, Varese and Novara.",
    ),
    (
        "Villaggio alpino tra i paesi più belli delle Alpi (Bandiera Arancione del Touring Club Italiano), ai piedi della parete Est del Monte Rosa. Ideale per gite in montagna, esperienze a contatto con la natura e weekend vicino a Milano, al Lake Maggiore, Varese e Novara.",
        "Alpine village among the most beautiful towns in the Alps (Touring Club Italiano Orange Flag), at the foot of the east face of Monte Rosa. Ideal for mountain day trips, nature experiences and weekends near Milan, Lake Maggiore, Varese and Novara.",
    ),
    (
        '"touristType": ["famiglie", "coppie", "senior", "weekend", "gite dalla pianura", "ospiti dei laghi"]',
        '"touristType": ["families", "couples", "seniors", "weekend", "day trips from the plain", "lake guests"]',
    ),
    (
        '"areaServed": ["Milano", "Varese", "Novara", "Lake Maggiore", "Lago d\'Orta", "Lake Mergozzo", "Torino", "Genova", "Pianura Padana", "Svizzera", "Canton Vallese", "Ticino"]',
        '"areaServed": ["Milan", "Varese", "Novara", "Lake Maggiore", "Lake Orta", "Lake Mergozzo", "Turin", "Genoa", "Po Plain", "Switzerland", "Canton Valais", "Ticino"]',
    ),
    (
        '{ "@type": "TouristAttraction", "name": "Lifts Belvedere e Monte Moro", "url": "https://www.macugnagabooking.it/en/funivia-seggiovia.html" }',
        '{ "@type": "TouristAttraction", "name": "Belvedere and Monte Moro lifts", "url": "https://www.macugnagabooking.it/en/funivia-seggiovia.html" }',
    ),
    (
        'alt="Il Dorf di Macugnaga con le antiche case alpine, Archivio Distretto Turistico dei Laghi, ph Giancarlo Parazzoli"',
        'alt="The Dorf of Macugnaga with historic alpine houses, Lakes Tourist District Archive, photo Giancarlo Parazzoli"',
    ),
    (
        'alt="Forest bathing tra gli alberi a Macugnaga"',
        'alt="Forest bathing among the trees in Macugnaga"',
    ),
    (
        'alt="Gold mine visitabile a Macugnaga"',
        'alt="Visitable gold mine in Macugnaga"',
    ),
    (
        'alt="Escursione Via del Pane a Macugnaga"',
        'alt="Via del Pane hike in Macugnaga"',
    ),
    (
        'alt="Panorama dal Belvedere verso il Monte Rosa"',
        'alt="View from Belvedere toward Monte Rosa"',
    ),
    (
        'alt="Macugnaga e Monte Rosa dall’alto"',
        'alt="Macugnaga and Monte Rosa from above"',
    ),
    (
        "Lifts Belvedere e Monte Moro",
        "Belvedere and Monte Moro lifts",
    ),
]

SHARED_FR = [
    (
        "À portée de route depuis <strong>Milano</strong>, <strong>Varese</strong>, <strong>Novara</strong> e dal <strong>Lac Majeur</strong> (anche Orta e Mergozzo), et aussi depuis <strong>Torino</strong>, <strong>Genova</strong>, Canton <strong>Vallese</strong> e <strong>Ticino</strong>.",
        "À portée de route depuis <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> et le <strong>Lac Majeur</strong> (y compris Orta et Mergozzo), et aussi depuis <strong>Turin</strong>, <strong>Gênes</strong>, le canton du <strong>Valais</strong> et le <strong>Tessin</strong>.",
    ),
    (
        "Si vous séjournez à l’hôtel ou au camping sur <strong>Lac Majeur</strong>, sul <strong>Lac d’Orta</strong> ou sur <strong>Lac de Mergozzo</strong>",
        "Si vous séjournez à l’hôtel ou au camping sur le <strong>Lac Majeur</strong>, sur le <strong>Lac d’Orta</strong> ou sur le <strong>Lac de Mergozzo</strong>",
    ),
    (
        "facilmente raggiungibile da <strong>Milano</strong>, <strong>Varese</strong>, <strong>Novara</strong> e dal <strong>Lac Majeur</strong> (anche Orta e Mergozzo), et aussi depuis <strong>Torino</strong>, <strong>Genova</strong>, Canton <strong>Vallese</strong> e <strong>Ticino</strong>",
        "facilement accessible depuis <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> et le <strong>Lac Majeur</strong> (y compris Orta et Mergozzo), et aussi depuis <strong>Turin</strong>, <strong>Gênes</strong>, le canton du <strong>Valais</strong> et le <strong>Tessin</strong>",
    ),
    (
        "raggiungibilet aussi depuisl Lac Majeur",
        "également accessible depuis le Lac Majeur",
    ),
    (
        "et aussi depuisl Lac Majeur",
        "et aussi depuis le Lac Majeur",
    ),
    (
        "Portale di prenotazione",
        "Portail de réservation",
    ),
    (
        "portale di prenotazione",
        "portail de réservation",
    ),
    (
        "Traduzione automatica dalla versione ufficiale in lingua italiana",
        "Traduction automatique à partir de la version officielle en italien.",
    ),
    (
        '"inLanguage": "it-IT"',
        '"inLanguage": "fr-FR"',
    ),
]

SHARED_DE = [
    (
        "Gut erreichbar von <strong>Milano</strong>, <strong>Varese</strong>, <strong>Novara</strong> e dal <strong>Lago Maggiore</strong> (anche Orta e Mergozzo), und auch von <strong>Torino</strong>, <strong>Genova</strong>, Canton <strong>Vallese</strong> e <strong>Ticino</strong>.",
        "Gut erreichbar von <strong>Mailand</strong>, <strong>Varese</strong>, <strong>Novara</strong> und dem <strong>Lago Maggiore</strong> (einschließlich Orta und Mergozzo), und auch von <strong>Turin</strong>, <strong>Genua</strong>, dem Kanton <strong>Wallis</strong> und dem <strong>Tessin</strong>.",
    ),
    (
        "Wenn Sie in einem Hotel oder Campingplatz am <strong>Lago Maggiore</strong>, sul <strong>Ortasee</strong> oder am <strong>Mergozzo-See</strong>",
        "Wenn Sie in einem Hotel oder Campingplatz am <strong>Lago Maggiore</strong>, am <strong>Ortasee</strong> oder am <strong>Mergozzo-See</strong>",
    ),
    (
        "facilmente raggiungibile da <strong>Milano</strong>, <strong>Varese</strong>, <strong>Novara</strong> e dal <strong>Lago Maggiore</strong> (anche Orta e Mergozzo), und auch von <strong>Torino</strong>, <strong>Genova</strong>, Canton <strong>Vallese</strong> e <strong>Ticino</strong>",
        "leicht erreichbar von <strong>Mailand</strong>, <strong>Varese</strong>, <strong>Novara</strong> und dem <strong>Lago Maggiore</strong> (einschließlich Orta und Mergozzo), und auch von <strong>Turin</strong>, <strong>Genua</strong>, dem Kanton <strong>Wallis</strong> und dem <strong>Tessin</strong>",
    ),
    (
        "raggiungibilund auch vonl Lago Maggiore",
        "auch erreichbar vom Lago Maggiore",
    ),
    (
        "und auch vonl Lago Maggiore",
        "und auch vom Lago Maggiore",
    ),
    (
        "und auch vongli hotel e campeggi sul Lago Maggiore",
        "und auch von Hotels und Campingplätzen am Lago Maggiore",
    ),
    (
        "Portale di prenotazione",
        "Buchungsportal",
    ),
    (
        "portale di prenotazione",
        "Buchungsportal",
    ),
    (
        "Traduzione automatica dalla versione ufficiale in lingua italiana",
        "Automatische Übersetzung aus der offiziellen italienischen Fassung.",
    ),
    (
        '"inLanguage": "it-IT"',
        '"inLanguage": "de-DE"',
    ),
]

# Generic leftover connectors / words still appearing in EN/FR/DE
GENERIC = {
    "en": [
        (" e dal ", " and "),
        (" e da ", " and from "),
        (" e a ", " and "),
        (" (anche ", " (including "),
        (", anche ", ", including "),
        (" anche ", " also "),
        (", sul ", ", on "),
        (" sul ", " on "),
        (" sulla ", " on the "),
        (" sulle ", " on the "),
        (" sui ", " on the "),
        (" da Torino", " from Turin"),
        (" da Milano", " from Milan"),
        (" da Novara", " from Novara"),
        (" da Varese", " from Varese"),
        (" dalla Svizzera", " from Switzerland"),
        (" dalla Pianura Padana", " from the Po Plain"),
        (" Vedi ", " See "),
        (" Vedi anche ", " See also "),
        (" Scopri di più su ", " Learn more about "),
        (" Scopri le esperienze", " Discover the experiences"),
        (" Scopri il paese", " Discover the village"),
        (" Learn more su ", " Learn more about "),
        (" Prenota</a>", " Book</a>"),
        (" prenotare le esperienze online", " book experiences online"),
        (" prenota online", " book online"),
        ("Prenota online", "Book online"),
        ("Lago d'Orta", "Lake Orta"),
        ("Lago d’Orta", "Lake Orta"),
        ("Seniorss", "Seniors"),
        ("Secure payment online con credit card e PayPal.", "Secure payment online with credit card and PayPal."),
        ("Gite in montagna, famiglie, coppie, senior, weekend Macugnaga Monte Rosa e arrivo da Milano, dal Lake Maggiore, Varese e Novara.",
         "Mountain day trips, families, couples, seniors, Macugnaga Monte Rosa weekends and arrivals from Milan, Lake Maggiore, Varese and Novara."),
    ],
    "fr": [
        (" e dal ", " et le "),
        (" e da ", " et depuis "),
        (" e a ", " et "),
        (" (anche ", " (y compris "),
        (", anche ", ", y compris "),
        (" anche ", " aussi "),
        (", sul ", ", sur "),
        (" sul ", " sur "),
        (" da Torino", " depuis Turin"),
        (" da Milano", " depuis Milan"),
        (" da Novara", " depuis Novara"),
        (" da Varese", " depuis Varese"),
        (" dalla Svizzera", " depuis la Suisse"),
        (" dalla Pianura Padana", " depuis la plaine du Pô"),
        (" Vedi ", " Voir "),
        (" Vedi anche ", " Voir aussi "),
        (" Scopri di più su ", " En savoir plus sur "),
        (" Scopri le esperienze", " Découvrir les expériences"),
        (" Scopri il paese", " Découvrir le village"),
        (" Prenota</a>", " Réserver</a>"),
        (" prenotare le esperienze online", " réserver les expériences en ligne"),
        (" prenota online", " réserver en ligne"),
        ("Lago d'Orta", "Lac d’Orta"),
        ("Lago d’Orta", "Lac d’Orta"),
        ("cuore delle Alpi", "cœur des Alpes"),
        ("la montagna vera, vicina a Milano", "la vraie montagne, près de Milan"),
        ("Come restare", "Comment séjourner"),
        ("Soggiorni lunghi", "Longs séjours"),
        ("Cosa prenotare", "Que réserver"),
        ("Ideale per ", "Idéal pour "),
    ],
    "de": [
        (" e dal ", " und dem "),
        (" e da ", " und von "),
        (" e a ", " und "),
        (" (anche ", " (einschließlich "),
        (", anche ", ", einschließlich "),
        (" anche ", " auch "),
        (", sul ", ", am "),
        (" sul ", " am "),
        (" da Torino", " von Turin"),
        (" da Milano", " von Mailand"),
        (" da Novara", " von Novara"),
        (" da Varese", " von Varese"),
        (" dalla Svizzera", " aus der Schweiz"),
        (" dalla Pianura Padana", " aus der Po-Ebene"),
        (" Vedi ", " Siehe "),
        (" Vedi anche ", " Siehe auch "),
        (" Scopri di più su ", " Mehr erfahren über "),
        (" Scopri le esperienze", " Erlebnisse entdecken"),
        (" Scopri il paese", " Das Dorf entdecken"),
        (" Prenota</a>", " Buchen</a>"),
        (" prenotare le esperienze online", " Erlebnisse online buchen"),
        (" prenota online", " online buchen"),
        ("Lago d'Orta", "Ortasee"),
        ("Lago d’Orta", "Ortasee"),
        ("cuore delle Alpi", "Herz der Alpen"),
        ("la montagna vera, vicina a Milano", "echte Berge, nahe Mailand"),
        ("Come restare", "Wie bleiben"),
        ("Soggiorni lunghi", "Lange Aufenthalte"),
        ("Cosa prenotare", "Was buchen"),
        ("Ideale per ", "Ideal für "),
        ("Kontakt portale di prenotazione", "Kontakt Buchungsportal"),
    ],
}


def apply_pairs(text: str, pairs: list[tuple[str, str]]) -> tuple[str, int]:
    n = 0
    for old, new in pairs:
        if old in text:
            c = text.count(old)
            text = text.replace(old, new)
            n += c
    return text, n


def bump_script_versions(text: str) -> str:
    text = re.sub(r"i18n\.js\?v=\d+", "i18n.js?v=12", text)
    text = re.sub(r"partials\.js\?v=\d+", "partials.js?v=24", text)
    text = re.sub(r"esperienze-list\.js\?v=\d+", "esperienze-list.js?v=20", text)
    text = re.sub(r"availability-bar\.js\?v=\d+", "availability-bar.js?v=8", text)
    text = re.sub(r"promo-popup\.js\?v=\d+", "promo-popup.js?v=4", text)
    return text


def process_lang(lang: str, shared: list[tuple[str, str]]) -> int:
    total = 0
    root = ROOT / lang
    for path in sorted(root.rglob("*.html")):
        original = path.read_text(encoding="utf-8")
        text = original
        text, n1 = apply_pairs(text, shared)
        text, n2 = apply_pairs(text, GENERIC[lang])
        text = bump_script_versions(text)
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            changed = n1 + n2
            total += changed
            print(f"  {path.relative_to(ROOT)}: {changed} replacements")
    return total


def main() -> None:
    print("=== EN ===")
    process_lang("en", SHARED_EN)
    print("=== FR ===")
    process_lang("fr", SHARED_FR)
    print("=== DE ===")
    process_lang("de", SHARED_DE)
    # Also bump versions on IT root pages that load shared JS (optional — skip IT content)
    for path in ROOT.glob("*.html"):
        original = path.read_text(encoding="utf-8")
        text = bump_script_versions(original)
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            print(f"  bumped scripts: {path.name}")


if __name__ == "__main__":
    main()
