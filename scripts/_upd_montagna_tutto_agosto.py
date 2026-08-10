# -*- coding: utf-8 -*-
"""Update Montagna d'agosto landings + home promo to Attività per tutto agosto."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def apply(path: Path, repls: list[tuple[str, str]]) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in repls:
        if old not in text:
            raise SystemExit(f"MISSING in {path.relative_to(ROOT)}:\n{old[:120]}")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
    print("updated", path.relative_to(ROOT))


LANDING_IT = [
    (
        "<title>Montagna d’agosto — Esperienze dall’8 al 20 agosto ai piedi del Monte Rosa | Macugnaga Booking</title>",
        "<title>Attività per tutto agosto — Esperienze fino al 30 agosto ai piedi del Monte Rosa | Macugnaga Booking</title>",
    ),
    (
        'content="Montagna d’agosto a Macugnaga Monte Rosa: tutte le esperienze prenotabili online dall’8 al 20 agosto 2026. Boschi, miniera d’oro, Casa Walser, trekking e natura — portale di prenotazione dell’Unione Montana."',
        'content="Attività per tutto agosto a Macugnaga Monte Rosa: esperienze prenotabili online da oggi fino al 30 agosto 2026. Boschi, miniera d’oro, Casa Walser, trekking e natura — portale di prenotazione dell’Unione Montana."',
    ),
    (
        'content="Montagna d’agosto 8–20 agosto | Macugnaga Monte Rosa"',
        'content="Attività per tutto agosto | Macugnaga Monte Rosa"',
    ),
    (
        'content="Ecco tutte le esperienze che puoi vivere ai piedi del Monte Rosa dall’8 al 20 agosto: prenota online su Macugnaga Booking."',
        'content="Esperienze in programma da oggi fino al 30 agosto ai piedi del Monte Rosa: prenota online su Macugnaga Booking."',
    ),
    (
        'content="Montagna d’agosto — Esperienze 8–20 agosto | Macugnaga"',
        'content="Attività per tutto agosto — Fino al 30 agosto | Macugnaga"',
    ),
    ('"name": "8–20 agosto"', '"name": "Attività per tutto agosto"'),
    (
        '"name": "Montagna d’agosto — Esperienze dall’8 al 20 agosto a Macugnaga"',
        '"name": "Attività per tutto agosto — Esperienze fino al 30 agosto a Macugnaga"',
    ),
    (
        '"description": "Tutte le esperienze prenotabili online a Macugnaga Monte Rosa tra l’8 e il 20 agosto 2026, ai piedi del Monte Rosa."',
        '"description": "Esperienze prenotabili online a Macugnaga Monte Rosa da oggi fino al 30 agosto 2026, ai piedi del Monte Rosa."',
    ),
    (
        '"temporalCoverage": "2026-08-08/2026-08-20"',
        '"temporalCoverage": "2026-08-10/2026-08-30"',
    ),
    (
        '"name": "Esperienze prenotabili a Macugnaga dall’8 al 20 agosto"',
        '"name": "Esperienze prenotabili a Macugnaga fino al 30 agosto"',
    ),
    (
        '"description": "Attività in montagna prenotabili online a Macugnaga Monte Rosa tra l’8 e il 20 agosto 2026."',
        '"description": "Attività in montagna prenotabili online a Macugnaga Monte Rosa fino al 30 agosto 2026."',
    ),
    (
        '"name": "Quali esperienze posso prenotare dall’8 al 20 agosto a Macugnaga?"',
        '"name": "Quali esperienze posso prenotare fino al 30 agosto a Macugnaga?"',
    ),
    (
        '"text": "Tra l’8 e il 20 agosto 2026 puoi prenotare online esperienze a contatto con boschi e natura, visite alla Casa Museo Walser e alla miniera d’oro, trekking e attività soft ai piedi del Monte Rosa."',
        '"text": "Fino al 30 agosto 2026 puoi prenotare online esperienze a contatto con boschi e natura, visite alla Casa Museo Walser e alla miniera d’oro, trekking e attività soft ai piedi del Monte Rosa."',
    ),
    (
        '"name": "Come organizzare un weekend con pernottamento dall’8 al 20 agosto?"',
        '"name": "Come organizzare un weekend con pernottamento fino al 30 agosto?"',
    ),
    (
        '"text": "Scegli un hotel, B&B o casa vacanza a Macugnaga, prenota online una o due esperienze del periodo 8–20 agosto e combina passeggiate in paese, boschi e, se aperti, gli impianti di risalita."',
        '"text": "Scegli un hotel, B&B o casa vacanza a Macugnaga, prenota online una o due esperienze fino al 30 agosto e combina passeggiate in paese, boschi e, se aperti, gli impianti di risalita."',
    ),
    ("· 8–20 agosto</p>", "· Tutto agosto</p>"),
    (
        "<h1>Montagna d’agosto — Ecco tutte le esperienze che puoi vivere ai piedi del Monte Rosa dall’8 al 20 agosto</h1>",
        "<h1>Attività per tutto agosto</h1>",
    ),
    (
        "<p>Dall’8 al 20 agosto 2026, il portale di prenotazione raccoglie le attività disponibili ai piedi del Monte Rosa: natura, cultura e montagna per tutti.</p>",
        "<p>Esperienze in programma da oggi fino al 30 agosto ai piedi del Monte Rosa: natura, cultura e montagna per tutti sul portale di prenotazione.</p>",
    ),
    (
        "Dall’<strong>8 al 20 agosto</strong> il portale di prenotazione raccoglie le esperienze disponibili online: benessere in bosco, visite culturali, miniera d’oro, trekking e attività soft.",
        "Fino al <strong>30 agosto</strong> il portale di prenotazione raccoglie le esperienze disponibili online: benessere in bosco, visite culturali, miniera d’oro, trekking e attività soft.",
    ),
    (
        "Tra l’8 e il 20 agosto un <strong>soggiorno con pernottamento</strong>",
        "Fino al 30 agosto un <strong>soggiorno con pernottamento</strong>",
    ),
    (
        "<h2>Esperienze prenotabili dall’8 al 20 agosto</h2>",
        "<h2>Esperienze prenotabili fino al 30 agosto</h2>",
    ),
    (
        "Elenco aggiornato delle attività con disponibilità tra l’<strong>8</strong> e il <strong>20 agosto 2026</strong>.",
        "Elenco aggiornato delle attività con disponibilità da <strong>oggi</strong> fino al <strong>30 agosto 2026</strong>.",
    ),
    (
        'aria-label="Esperienze prenotabili 8–20 agosto"',
        'aria-label="Esperienze prenotabili fino al 30 agosto"',
    ),
    (
        'data-date-from="2026-08-08" data-date-to="2026-08-20"',
        'data-date-from="today" data-date-to="2026-08-30"',
    ),
    (
        '<h2 class="reveal">Domande frequenti su Montagna d’agosto (8–20 agosto)</h2>',
        '<h2 class="reveal">Domande frequenti su Attività per tutto agosto</h2>',
    ),
    (
        "<summary>Quali esperienze posso prenotare dall’8 al 20 agosto a Macugnaga?</summary>",
        "<summary>Quali esperienze posso prenotare fino al 30 agosto a Macugnaga?</summary>",
    ),
    (
        "con disponibilità tra l’8 e il 20 agosto 2026:",
        "con disponibilità da oggi fino al 30 agosto 2026:",
    ),
    ("esperienze-list.js?v=19", "esperienze-list.js?v=20"),
]

LANDING_EN = [
    (
        "<title>August in the mountains — Experiences 8–20 August at the foot of Monte Rosa | Macugnaga Booking</title>",
        "<title>Activities throughout August — Experiences through 30 August at the foot of Monte Rosa | Macugnaga Booking</title>",
    ),
    (
        'content="August in the mountains in Macugnaga Monte Rosa: all bookable online experiences from 8 to 20 August 2026. Woods, gold mine, Walser House, trekking and nature — Unione Montana booking portal."',
        'content="Activities throughout August in Macugnaga Monte Rosa: bookable online experiences from today through 30 August 2026. Woods, gold mine, Walser House, trekking and nature — Unione Montana booking portal."',
    ),
    (
        'content="August in the mountains 8–20 August | Macugnaga Monte Rosa"',
        'content="Activities throughout August | Macugnaga Monte Rosa"',
    ),
    (
        'content="All the experiences you can enjoy at the foot of Monte Rosa from 8 to 20 August — book online on Macugnaga Booking."',
        'content="Experiences scheduled from today through 30 August at the foot of Monte Rosa — book online on Macugnaga Booking."',
    ),
    (
        'content="August in the mountains — Experiences 8–20 August | Macugnaga"',
        'content="Activities throughout August — Through 30 August | Macugnaga"',
    ),
    ('"name": "8–20 August"', '"name": "Activities throughout August"'),
    (
        '"name": "August in the mountains — Experiences from 8 to 20 August in Macugnaga"',
        '"name": "Activities throughout August — Experiences through 30 August in Macugnaga"',
    ),
    (
        '"description": "All bookable online experiences in Macugnaga Monte Rosa from 8 to 20 August 2026, at the foot of Monte Rosa."',
        '"description": "Bookable online experiences in Macugnaga Monte Rosa from today through 30 August 2026, at the foot of Monte Rosa."',
    ),
    (
        '"temporalCoverage": "2026-08-08/2026-08-20"',
        '"temporalCoverage": "2026-08-10/2026-08-30"',
    ),
    (
        '"name": "Bookable experiences in Macugnaga from 8 to 20 August"',
        '"name": "Bookable experiences in Macugnaga through 30 August"',
    ),
    (
        '"description": "Mountain activities bookable online in Macugnaga Monte Rosa from 8 to 20 August 2026."',
        '"description": "Mountain activities bookable online in Macugnaga Monte Rosa through 30 August 2026."',
    ),
    (
        '"name": "Which experiences can I book from 8 to 20 August in Macugnaga?"',
        '"name": "Which experiences can I book through 30 August in Macugnaga?"',
    ),
    (
        '"text": "Between 8 and 20 August 2026 you can book online experiences among woods and nature, visits to the Walser House Museum and the gold mine, trekking and gentle activities at the foot of Monte Rosa."',
        '"text": "Through 30 August 2026 you can book online experiences among woods and nature, visits to the Walser House Museum and the gold mine, trekking and gentle activities at the foot of Monte Rosa."',
    ),
    (
        '"name": "How to plan a weekend with overnight stay from 8 to 20 August?"',
        '"name": "How to plan a weekend with overnight stay through 30 August?"',
    ),
    (
        '"text": "Choose a hotel, B&B or holiday home in Macugnaga, book online one or two experiences for 8–20 August and combine village walks, woods and, if open, the ski lifts."',
        '"text": "Choose a hotel, B&B or holiday home in Macugnaga, book online one or two experiences through 30 August and combine village walks, woods and, if open, the ski lifts."',
    ),
    ("· 8–20 August</p>", "· All August</p>"),
    (
        "<h1>August in the mountains — All the experiences you can enjoy at the foot of Monte Rosa from 8 to 20 August</h1>",
        "<h1>Activities throughout August</h1>",
    ),
    (
        "<p>From 8 to 20 August 2026, the booking portal gathers the activities available at the foot of Monte Rosa: nature, culture and mountains for everyone.</p>",
        "<p>Experiences scheduled from today through 30 August at the foot of Monte Rosa: nature, culture and mountains for everyone on the booking portal.</p>",
    ),
    (
        "From <strong>8 to 20 August</strong> the booking portal gathers the experiences available online: forest wellness, cultural visits, gold mine, trekking and gentle activities.",
        "Through <strong>30 August</strong> the booking portal gathers the experiences available online: forest wellness, cultural visits, gold mine, trekking and gentle activities.",
    ),
    (
        "Between 8 and 20 August an <strong>overnight stay</strong>",
        "Through 30 August an <strong>overnight stay</strong>",
    ),
    (
        "<h2>Bookable experiences from 8 to 20 August</h2>",
        "<h2>Bookable experiences through 30 August</h2>",
    ),
    (
        "Updated list of activities with availability between <strong>8</strong> and <strong>20 August 2026</strong>.",
        "Updated list of activities with availability from <strong>today</strong> through <strong>30 August 2026</strong>.",
    ),
    (
        'aria-label="Bookable experiences 8–20 August"',
        'aria-label="Bookable experiences through 30 August"',
    ),
    (
        'data-date-from="2026-08-08" data-date-to="2026-08-20"',
        'data-date-from="today" data-date-to="2026-08-30"',
    ),
    (
        '<h2 class="reveal">Frequently asked questions about August in the mountains (8–20 August)</h2>',
        '<h2 class="reveal">Frequently asked questions about activities throughout August</h2>',
    ),
    (
        "<summary>Which experiences can I book from 8 to 20 August in Macugnaga?</summary>",
        "<summary>Which experiences can I book through 30 August in Macugnaga?</summary>",
    ),
    (
        "with availability between 8 and 20 August 2026:",
        "with availability from today through 30 August 2026:",
    ),
    ("esperienze-list.js?v=19", "esperienze-list.js?v=20"),
]

LANDING_FR = [
    (
        "<title>Montagne d’août — Expériences du 8 au 20 août au pied du Mont Rose | Macugnaga Booking</title>",
        "<title>Activités pour tout le mois d’août — Expériences jusqu’au 30 août au pied du Mont Rose | Macugnaga Booking</title>",
    ),
    (
        'content="Montagne d’août à Macugnaga Monte Rosa : toutes les expériences réservables en ligne du 8 au 20 août 2026. Forêts, mine d’or, Maison Walser, randonnées et nature — portail de réservation de l’Unione Montana."',
        'content="Activités pour tout le mois d’août à Macugnaga Monte Rosa : expériences réservables en ligne d’aujourd’hui au 30 août 2026. Forêts, mine d’or, Maison Walser, randonnées et nature — portail de réservation de l’Unione Montana."',
    ),
    (
        'content="Montagne d’août 8–20 août | Macugnaga Monte Rosa"',
        'content="Activités pour tout le mois d’août | Macugnaga Monte Rosa"',
    ),
    (
        'content="Voici toutes les expériences à vivre au pied du Mont Rose du 8 au 20 août — réservez en ligne sur Macugnaga Booking."',
        'content="Expériences prévues d’aujourd’hui au 30 août au pied du Mont Rose — réservez en ligne sur Macugnaga Booking."',
    ),
    (
        'content="Montagne d’août — Expériences 8–20 août | Macugnaga"',
        'content="Activités pour tout le mois d’août — Jusqu’au 30 août | Macugnaga"',
    ),
    ('"name": "8–20 août"', '"name": "Activités pour tout le mois d’août"'),
    (
        '"name": "Montagne d’août — Expériences du 8 au 20 août à Macugnaga"',
        '"name": "Activités pour tout le mois d’août — Expériences jusqu’au 30 août à Macugnaga"',
    ),
    (
        '"description": "Toutes les expériences réservables en ligne à Macugnaga Monte Rosa entre le 8 et le 20 août 2026, au pied du Mont Rose."',
        '"description": "Expériences réservables en ligne à Macugnaga Monte Rosa d’aujourd’hui au 30 août 2026, au pied du Mont Rose."',
    ),
    (
        '"temporalCoverage": "2026-08-08/2026-08-20"',
        '"temporalCoverage": "2026-08-10/2026-08-30"',
    ),
    (
        '"name": "Expériences réservables à Macugnaga du 8 au 20 août"',
        '"name": "Expériences réservables à Macugnaga jusqu’au 30 août"',
    ),
    (
        '"description": "Activités de montagne réservables en ligne à Macugnaga Monte Rosa du 8 au 20 août 2026."',
        '"description": "Activités de montagne réservables en ligne à Macugnaga Monte Rosa jusqu’au 30 août 2026."',
    ),
    (
        '"name": "Quelles expériences puis-je réserver du 8 au 20 août à Macugnaga ?"',
        '"name": "Quelles expériences puis-je réserver jusqu’au 30 août à Macugnaga ?"',
    ),
    (
        '"text": "Entre le 8 et le 20 août 2026, vous pouvez réserver en ligne des expériences entre forêts et nature, des visites de la Maison-musée Walser et de la mine d’or, des randonnées et des activités douces au pied du Mont Rose."',
        '"text": "Jusqu’au 30 août 2026, vous pouvez réserver en ligne des expériences entre forêts et nature, des visites de la Maison-musée Walser et de la mine d’or, des randonnées et des activités douces au pied du Mont Rose."',
    ),
    (
        '"name": "Comment organiser un week-end avec nuitée du 8 au 20 août ?"',
        '"name": "Comment organiser un week-end avec nuitée jusqu’au 30 août ?"',
    ),
    (
        '"text": "Choisissez un hôtel, un B&B ou une maison de vacances à Macugnaga, réservez en ligne une ou deux expériences du 8–20 août et combinez balades au village, forêts et, s’ils sont ouverts, les remontées mécaniques."',
        '"text": "Choisissez un hôtel, un B&B ou une maison de vacances à Macugnaga, réservez en ligne une ou deux expériences jusqu’au 30 août et combinez balades au village, forêts et, s’ils sont ouverts, les remontées mécaniques."',
    ),
    ("· 8–20 août</p>", "· Tout le mois d’août</p>"),
    (
        "<h1>Montagne d’août — Voici toutes les expériences que vous pouvez vivre au pied du Mont Rose du 8 au 20 août</h1>",
        "<h1>Activités pour tout le mois d’août</h1>",
    ),
    (
        "<p>Du 8 au 20 août 2026, le portail de réservation regroupe les activités disponibles au pied du Mont Rose : nature, culture et montagne pour tous.</p>",
        "<p>Expériences prévues d’aujourd’hui au 30 août au pied du Mont Rose : nature, culture et montagne pour tous sur le portail de réservation.</p>",
    ),
    (
        "Du <strong>8 au 20 août</strong>, le portail de réservation regroupe les expériences disponibles en ligne : bien-être en forêt, visites culturelles, mine d’or, randonnées et activités douces.",
        "Jusqu’au <strong>30 août</strong>, le portail de réservation regroupe les expériences disponibles en ligne : bien-être en forêt, visites culturelles, mine d’or, randonnées et activités douces.",
    ),
    (
        "Entre le 8 et le 20 août, un <strong>séjour avec nuitée</strong>",
        "Jusqu’au 30 août, un <strong>séjour avec nuitée</strong>",
    ),
    (
        "<h2>Expériences réservables du 8 au 20 août</h2>",
        "<h2>Expériences réservables jusqu’au 30 août</h2>",
    ),
    (
        "Liste à jour des activités disponibles entre le <strong>8</strong> et le <strong>20 août 2026</strong>.",
        "Liste à jour des activités disponibles d’<strong>aujourd’hui</strong> au <strong>30 août 2026</strong>.",
    ),
    (
        'aria-label="Expériences réservables 8–20 août"',
        'aria-label="Expériences réservables jusqu’au 30 août"',
    ),
    (
        'data-date-from="2026-08-08" data-date-to="2026-08-20"',
        'data-date-from="today" data-date-to="2026-08-30"',
    ),
    (
        '<h2 class="reveal">Questions fréquentes sur Montagne d’août (8–20 août)</h2>',
        '<h2 class="reveal">Questions fréquentes sur les activités pour tout le mois d’août</h2>',
    ),
    (
        "<summary>Quelles expériences puis-je réserver du 8 au 20 août à Macugnaga ?</summary>",
        "<summary>Quelles expériences puis-je réserver jusqu’au 30 août à Macugnaga ?</summary>",
    ),
    (
        "disponibles entre le 8 et le 20 août 2026 :",
        "disponibles d’aujourd’hui au 30 août 2026 :",
    ),
    ("esperienze-list.js?v=19", "esperienze-list.js?v=20"),
]

LANDING_DE = [
    (
        "<title>Berge im August — Erlebnisse vom 8. bis 20. August am Fuß des Monte Rosa | Macugnaga Booking</title>",
        "<title>Aktivitäten für den ganzen August — Erlebnisse bis 30. August am Fuß des Monte Rosa | Macugnaga Booking</title>",
    ),
    (
        'content="Berge im August in Macugnaga Monte Rosa: alle online buchbaren Erlebnisse vom 8. bis 20. August 2026. Wälder, Goldmine, Walser-Haus, Trekking und Natur — Buchungsportal der Unione Montana."',
        'content="Aktivitäten für den ganzen August in Macugnaga Monte Rosa: online buchbare Erlebnisse von heute bis 30. August 2026. Wälder, Goldmine, Walser-Haus, Trekking und Natur — Buchungsportal der Unione Montana."',
    ),
    (
        'content="Berge im August 8.–20. August | Macugnaga Monte Rosa"',
        'content="Aktivitäten für den ganzen August | Macugnaga Monte Rosa"',
    ),
    (
        'content="Alle Erlebnisse am Fuß des Monte Rosa vom 8. bis 20. August — online buchen auf Macugnaga Booking."',
        'content="Erlebnisse von heute bis zum 30. August am Fuß des Monte Rosa — online buchen auf Macugnaga Booking."',
    ),
    (
        'content="Berge im August — Erlebnisse 8.–20. August | Macugnaga"',
        'content="Aktivitäten für den ganzen August — Bis 30. August | Macugnaga"',
    ),
    ('"name": "8.–20. August"', '"name": "Aktivitäten für den ganzen August"'),
    (
        '"name": "Berge im August — Erlebnisse vom 8. bis 20. August in Macugnaga"',
        '"name": "Aktivitäten für den ganzen August — Erlebnisse bis 30. August in Macugnaga"',
    ),
    (
        '"description": "Alle online buchbaren Erlebnisse in Macugnaga Monte Rosa vom 8. bis 20. August 2026, am Fuß des Monte Rosa."',
        '"description": "Online buchbare Erlebnisse in Macugnaga Monte Rosa von heute bis 30. August 2026, am Fuß des Monte Rosa."',
    ),
    (
        '"temporalCoverage": "2026-08-08/2026-08-20"',
        '"temporalCoverage": "2026-08-10/2026-08-30"',
    ),
    (
        '"name": "Buchbare Erlebnisse in Macugnaga vom 8. bis 20. August"',
        '"name": "Buchbare Erlebnisse in Macugnaga bis 30. August"',
    ),
    (
        '"description": "Bergaktivitäten online buchbar in Macugnaga Monte Rosa vom 8. bis 20. August 2026."',
        '"description": "Bergaktivitäten online buchbar in Macugnaga Monte Rosa bis 30. August 2026."',
    ),
    (
        '"name": "Welche Erlebnisse kann ich vom 8. bis 20. August in Macugnaga buchen?"',
        '"name": "Welche Erlebnisse kann ich bis 30. August in Macugnaga buchen?"',
    ),
    (
        '"text": "Zwischen dem 8. und 20. August 2026 können Sie online Erlebnisse in Wäldern und Natur, Besuche im Walser-Hausmuseum und in der Goldmine, Trekking und sanfte Aktivitäten am Fuß des Monte Rosa buchen."',
        '"text": "Bis 30. August 2026 können Sie online Erlebnisse in Wäldern und Natur, Besuche im Walser-Hausmuseum und in der Goldmine, Trekking und sanfte Aktivitäten am Fuß des Monte Rosa buchen."',
    ),
    (
        '"name": "Wie plane ich ein Wochenende mit Übernachtung vom 8. bis 20. August?"',
        '"name": "Wie plane ich ein Wochenende mit Übernachtung bis 30. August?"',
    ),
    (
        '"text": "Wählen Sie Hotel, B&B oder Ferienhaus in Macugnaga, buchen Sie online ein oder zwei Erlebnisse für den 8.–20. August und kombinieren Sie Dorfspaziergänge, Wälder und, sofern geöffnet, die Bergbahnen."',
        '"text": "Wählen Sie Hotel, B&B oder Ferienhaus in Macugnaga, buchen Sie online ein oder zwei Erlebnisse bis 30. August und kombinieren Sie Dorfspaziergänge, Wälder und, sofern geöffnet, die Bergbahnen."',
    ),
    ("· 8.–20. August</p>", "· Ganzer August</p>"),
    (
        "<h1>Berge im August — Alle Erlebnisse, die Sie vom 8. bis 20. August am Fuß des Monte Rosa erleben können</h1>",
        "<h1>Aktivitäten für den ganzen August</h1>",
    ),
    (
        "<p>Vom 8. bis 20. August 2026 bündelt das Buchungsportal die verfügbaren Aktivitäten am Fuß des Monte Rosa: Natur, Kultur und Berge für alle.</p>",
        "<p>Erlebnisse von heute bis zum 30. August am Fuß des Monte Rosa: Natur, Kultur und Berge für alle auf dem Buchungsportal.</p>",
    ),
    (
        "Vom <strong>8. bis 20. August</strong> bündelt das Buchungsportal die online verfügbaren Erlebnisse: Wald-Wellness, Kulturbesuche, Goldmine, Trekking und sanfte Aktivitäten.",
        "Bis <strong>30. August</strong> bündelt das Buchungsportal die online verfügbaren Erlebnisse: Wald-Wellness, Kulturbesuche, Goldmine, Trekking und sanfte Aktivitäten.",
    ),
    (
        "Zwischen dem 8. und 20. August macht ein <strong>Aufenthalt mit Übernachtung</strong>",
        "Bis 30. August macht ein <strong>Aufenthalt mit Übernachtung</strong>",
    ),
    (
        "<h2>Buchbare Erlebnisse vom 8. bis 20. August</h2>",
        "<h2>Buchbare Erlebnisse bis 30. August</h2>",
    ),
    (
        "Aktuelle Liste der Aktivitäten mit Verfügbarkeit zwischen dem <strong>8.</strong> und <strong>20. August 2026</strong>.",
        "Aktuelle Liste der Aktivitäten mit Verfügbarkeit von <strong>heute</strong> bis <strong>30. August 2026</strong>.",
    ),
    (
        'aria-label="Buchbare Erlebnisse 8.–20. August"',
        'aria-label="Buchbare Erlebnisse bis 30. August"',
    ),
    (
        'data-date-from="2026-08-08" data-date-to="2026-08-20"',
        'data-date-from="today" data-date-to="2026-08-30"',
    ),
    (
        '<h2 class="reveal">Häufige Fragen zu Bergen im August (8.–20. August)</h2>',
        '<h2 class="reveal">Häufige Fragen zu Aktivitäten für den ganzen August</h2>',
    ),
    (
        "<summary>Welche Erlebnisse kann ich vom 8. bis 20. August in Macugnaga buchen?</summary>",
        "<summary>Welche Erlebnisse kann ich bis 30. August in Macugnaga buchen?</summary>",
    ),
    (
        "mit Verfügbarkeit zwischen dem 8. und 20. August 2026:",
        "mit Verfügbarkeit von heute bis 30. August 2026:",
    ),
    ("esperienze-list.js?v=19", "esperienze-list.js?v=20"),
]

INDEX = {
    "it": [
        (
            'aria-label="Montagna d’agosto 8–20 agosto"',
            'aria-label="Attività per tutto agosto"',
        ),
        (
            '<p class="home-promo__eyebrow">8–20 agosto 2026</p>',
            '<p class="home-promo__eyebrow">Fino al 30 agosto 2026</p>',
        ),
        (
            '<p class="home-promo__title">Montagna d’agosto</p>',
            '<p class="home-promo__title">Attività per tutto agosto</p>',
        ),
        (
            '<p class="home-promo__text">Ecco tutte le esperienze che puoi vivere ai piedi del Monte Rosa — prenota online.</p>',
            '<p class="home-promo__text">Esperienze in programma da oggi fino al 30 agosto ai piedi del Monte Rosa — prenota online.</p>',
        ),
        (
            ">Montagna d’agosto 8–20</a>",
            ">Attività per tutto agosto</a>",
        ),
        ("promo-popup.js?v=2", "promo-popup.js?v=3"),
        (
            'data-title="Montagna d’agosto"',
            'data-title="Attività per tutto agosto"',
        ),
        (
            'data-text="Tutte le esperienze prenotabili dall’8 al 20 agosto ai piedi del Monte Rosa."',
            'data-text="Esperienze in programma da oggi fino al 30 agosto ai piedi del Monte Rosa."',
        ),
        (
            'data-storage-key="mb_promo_popup_aug8_20_26"',
            'data-storage-key="mb_promo_popup_aug_tutto_30_26"',
        ),
    ],
    "en": [
        (
            'aria-label="August in the mountains 8–20 August"',
            'aria-label="Activities throughout August"',
        ),
        (
            '<p class="home-promo__eyebrow">8–20 August 2026</p>',
            '<p class="home-promo__eyebrow">Through 30 August 2026</p>',
        ),
        (
            '<p class="home-promo__title">August in the mountains</p>',
            '<p class="home-promo__title">Activities throughout August</p>',
        ),
        (
            '<p class="home-promo__text">All the experiences you can enjoy at the foot of Monte Rosa — book online.</p>',
            '<p class="home-promo__text">Experiences scheduled from today through 30 August at the foot of Monte Rosa — book online.</p>',
        ),
        (
            ">August in the mountains 8–20</a>",
            ">Activities throughout August</a>",
        ),
        ("promo-popup.js?v=2", "promo-popup.js?v=3"),
        (
            'data-title="August in the mountains"',
            'data-title="Activities throughout August"',
        ),
        (
            'data-text="All bookable experiences from 8 to 20 August at the foot of Monte Rosa."',
            'data-text="Experiences scheduled from today through 30 August at the foot of Monte Rosa."',
        ),
        (
            'data-storage-key="mb_promo_popup_aug8_20_26"',
            'data-storage-key="mb_promo_popup_aug_tutto_30_26"',
        ),
    ],
    "fr": [
        (
            'aria-label="Montagne d’août 8–20 août"',
            'aria-label="Activités pour tout le mois d’août"',
        ),
        (
            '<p class="home-promo__eyebrow">8–20 août 2026</p>',
            '<p class="home-promo__eyebrow">Jusqu’au 30 août 2026</p>',
        ),
        (
            '<p class="home-promo__title">Montagne d’août</p>',
            '<p class="home-promo__title">Activités pour tout le mois d’août</p>',
        ),
        (
            '<p class="home-promo__text">Voici toutes les expériences à vivre au pied du Mont Rose — réservez en ligne.</p>',
            '<p class="home-promo__text">Expériences prévues d’aujourd’hui au 30 août au pied du Mont Rose — réservez en ligne.</p>',
        ),
        (
            ">Montagne d’août 8–20</a>",
            ">Activités pour tout le mois d’août</a>",
        ),
        ("promo-popup.js?v=2", "promo-popup.js?v=3"),
        (
            'data-title="Montagne d’août"',
            'data-title="Activités pour tout le mois d’août"',
        ),
        (
            'data-text="Toutes les expériences réservables du 8 au 20 août au pied du Mont Rose."',
            'data-text="Expériences prévues d’aujourd’hui au 30 août au pied du Mont Rose."',
        ),
        (
            'data-storage-key="mb_promo_popup_aug8_20_26"',
            'data-storage-key="mb_promo_popup_aug_tutto_30_26"',
        ),
    ],
    "de": [
        (
            'aria-label="Berge im August 8.–20. August"',
            'aria-label="Aktivitäten für den ganzen August"',
        ),
        (
            '<p class="home-promo__eyebrow">8.–20. August 2026</p>',
            '<p class="home-promo__eyebrow">Bis 30. August 2026</p>',
        ),
        (
            '<p class="home-promo__title">Berge im August</p>',
            '<p class="home-promo__title">Aktivitäten für den ganzen August</p>',
        ),
        (
            '<p class="home-promo__text">Alle Erlebnisse am Fuß des Monte Rosa — online buchen.</p>',
            '<p class="home-promo__text">Erlebnisse von heute bis zum 30. August am Fuß des Monte Rosa — online buchen.</p>',
        ),
        (
            ">Berge im August 8.–20.</a>",
            ">Aktivitäten für den ganzen August</a>",
        ),
        ("promo-popup.js?v=2", "promo-popup.js?v=3"),
        (
            'data-title="Berge im August"',
            'data-title="Aktivitäten für den ganzen August"',
        ),
        (
            'data-text="Alle buchbaren Erlebnisse vom 8. bis 20. August am Fuß des Monte Rosa."',
            'data-text="Erlebnisse von heute bis zum 30. August am Fuß des Monte Rosa."',
        ),
        (
            'data-storage-key="mb_promo_popup_aug8_20_26"',
            'data-storage-key="mb_promo_popup_aug_tutto_30_26"',
        ),
    ],
}

LINKS = {
    ROOT / "esperienze.html": [
        (
            'Per <a href="montagna-dagosto-8-20-agosto.html">Montagna d’agosto (8–20 agosto)</a> vedi l’elenco filtrato',
            'Per <a href="montagna-dagosto-8-20-agosto.html">Attività per tutto agosto</a> vedi l’elenco filtrato',
        )
    ],
    ROOT / "en" / "esperienze.html": [
        (
            'For <a href="montagna-dagosto-8-20-agosto.html">August in the mountains (8–20 August)</a> see the filtered list',
            'For <a href="montagna-dagosto-8-20-agosto.html">Activities throughout August</a> see the filtered list',
        )
    ],
    ROOT / "fr" / "esperienze.html": [
        (
            'Pour <a href="montagna-dagosto-8-20-agosto.html">Montagne d’août (8–20 août)</a>, voir la liste filtrée',
            'Pour <a href="montagna-dagosto-8-20-agosto.html">Activités pour tout le mois d’août</a>, voir la liste filtrée',
        )
    ],
    ROOT / "de" / "esperienze.html": [
        (
            'Für <a href="montagna-dagosto-8-20-agosto.html">Berge im August (8.–20. August)</a> siehe die gefilterte Liste',
            'Für <a href="montagna-dagosto-8-20-agosto.html">Aktivitäten für den ganzen August</a> siehe die gefilterte Liste',
        )
    ],
    ROOT / "weekend.html": [
        (
            'Per <a href="montagna-dagosto-8-20-agosto.html">Montagna d’agosto (8–20 agosto)</a> trovi esperienze prenotabili filtrate per data.',
            'Per <a href="montagna-dagosto-8-20-agosto.html">Attività per tutto agosto</a> trovi esperienze prenotabili filtrate per data.',
        )
    ],
    ROOT / "en" / "weekend.html": [
        (
            'For <a href="montagna-dagosto-8-20-agosto.html">August in the mountains (8–20 August)</a> you will find bookable experiences filtered by date.',
            'For <a href="montagna-dagosto-8-20-agosto.html">Activities throughout August</a> you will find bookable experiences filtered by date.',
        )
    ],
    ROOT / "fr" / "weekend.html": [
        (
            'Pour <a href="montagna-dagosto-8-20-agosto.html">Montagne d’août (8–20 août)</a>, vous trouverez des expériences réservables filtrées par date.',
            'Pour <a href="montagna-dagosto-8-20-agosto.html">Activités pour tout le mois d’août</a>, vous trouverez des expériences réservables filtrées par date.',
        )
    ],
    ROOT / "de" / "weekend.html": [
        (
            'Für <a href="montagna-dagosto-8-20-agosto.html">Berge im August (8.–20. August)</a> finden Sie buchbare Erlebnisse nach Datum gefiltert.',
            'Für <a href="montagna-dagosto-8-20-agosto.html">Aktivitäten für den ganzen August</a> finden Sie buchbare Erlebnisse nach Datum gefiltert.',
        )
    ],
    ROOT / "famiglie.html": [
        (
            ">Montagna d’agosto 8–20</a>",
            ">Attività per tutto agosto</a>",
        )
    ],
    ROOT / "en" / "famiglie.html": [
        (
            ">August in the mountains 8–20</a>",
            ">Activities throughout August</a>",
        )
    ],
    ROOT / "fr" / "famiglie.html": [
        (
            ">Montagne d’août 8–20</a>",
            ">Activités pour tout le mois d’août</a>",
        )
    ],
    ROOT / "de" / "famiglie.html": [
        (
            ">Berge im August 8.–20.</a>",
            ">Aktivitäten für den ganzen August</a>",
        )
    ],
}


def patch_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    # bump lastmod for montagna landing entries
    old = (
        "montagna-dagosto-8-20-agosto.html</loc>\n"
        "    <xhtml:link rel=\"alternate\" hreflang=\"it\" href=\"https://www.macugnagabooking.it/montagna-dagosto-8-20-agosto.html\"/>\n"
        "    <xhtml:link rel=\"alternate\" hreflang=\"en\" href=\"https://www.macugnagabooking.it/en/montagna-dagosto-8-20-agosto.html\"/>\n"
        "    <xhtml:link rel=\"alternate\" hreflang=\"fr\" href=\"https://www.macugnagabooking.it/fr/montagna-dagosto-8-20-agosto.html\"/>\n"
        "    <xhtml:link rel=\"alternate\" hreflang=\"de\" href=\"https://www.macugnagabooking.it/de/montagna-dagosto-8-20-agosto.html\"/>\n"
        "    <xhtml:link rel=\"alternate\" hreflang=\"x-default\" href=\"https://www.macugnagabooking.it/montagna-dagosto-8-20-agosto.html\"/>\n"
        "    <lastmod>2026-08-07</lastmod>"
    )
    new = old.replace("<lastmod>2026-08-07</lastmod>", "<lastmod>2026-08-10</lastmod>")
    if old not in text:
        raise SystemExit("sitemap IT block not found")
    text = text.replace(old, new)
    for lang in ("en", "fr", "de"):
        needle = (
            f"<url><loc>https://www.macugnagabooking.it/{lang}/montagna-dagosto-8-20-agosto.html</loc>"
            f"<lastmod>2026-08-07</lastmod>"
        )
        repl = needle.replace("2026-08-07", "2026-08-10")
        if needle not in text:
            raise SystemExit(f"sitemap {lang} entry not found")
        text = text.replace(needle, repl)
    path.write_text(text, encoding="utf-8")
    print("updated sitemap.xml")


def main() -> None:
    apply(ROOT / "montagna-dagosto-8-20-agosto.html", LANDING_IT)
    apply(ROOT / "en" / "montagna-dagosto-8-20-agosto.html", LANDING_EN)
    apply(ROOT / "fr" / "montagna-dagosto-8-20-agosto.html", LANDING_FR)
    apply(ROOT / "de" / "montagna-dagosto-8-20-agosto.html", LANDING_DE)

    apply(ROOT / "index.html", INDEX["it"])
    apply(ROOT / "en" / "index.html", INDEX["en"])
    apply(ROOT / "fr" / "index.html", INDEX["fr"])
    apply(ROOT / "de" / "index.html", INDEX["de"])

    for path, repls in LINKS.items():
        apply(path, repls)

    patch_sitemap()
    print("done")


if __name__ == "__main__":
    main()
