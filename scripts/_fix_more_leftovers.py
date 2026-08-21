# -*- coding: utf-8 -*-
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    # EN famiglie body
    en_fam = ROOT / "en" / "famiglie.html"
    t = en_fam.read_text(encoding="utf-8")
    m = re.search(
        r"<p>Macugnaga [èe] la <strong>montagna a misura di famiglia</strong>.*?</p>",
        t,
    )
    if m:
        t = t.replace(
            m.group(0),
            "<p>Macugnaga is the <strong>family-friendly mountain</strong>: walks in the Dorf, trails suitable also for the little ones, visits to the Walser House and the gold mine, outdoor activities in nature in the fresh alpine summer climate.</p>",
        )
        en_fam.write_text(t, encoding="utf-8", newline="\n")
        print("en famiglie body ok")
    else:
        print("en famiglie body miss")

    # funivia ticket questions
    for lang, newq, quali in [
        (
            "en",
            '"name": "Can you book cableway tickets on the booking portal?"',
            (
                '"name": "Quali ski lifts ci sono a Macugnaga?"',
                '"name": "Which ski lifts are there in Macugnaga?"',
            ),
        ),
        (
            "fr",
            '"name": "Peut-on réserver les billets de téléphérique sur le portail de réservation ?"',
            (
                '"name": "Quali remontées mécaniques ci sono a Macugnaga?"',
                '"name": "Quelles remontées mécaniques y a-t-il à Macugnaga ?"',
            ),
        ),
        (
            "de",
            '"name": "Kann man Seilbahntickets im Buchungsportal buchen?"',
            (
                '"name": "Quali Bergbahnen ci sono a Macugnaga?"',
                '"name": "Welche Bergbahnen gibt es in Macugnaga?"',
            ),
        ),
    ]:
        p = ROOT / lang / "funivia-seggiovia.html"
        tt = p.read_text(encoding="utf-8")
        tt2 = re.sub(
            r'"name": "Si prenotano i biglietti funivia[^"]*"', newq, tt, count=1
        )
        tt2 = tt2.replace(quali[0], quali[1])
        if tt2 != tt:
            p.write_text(tt2, encoding="utf-8", newline="\n")
            print("funivia", lang, "ok")
        else:
            print("funivia", lang, "unchanged")

    # famiglie FR/DE Quali
    for lang, a, b, a2, b2 in [
        (
            "fr",
            '"name": "Quali esperienze in famiglia si possono prenotare?"',
            '"name": "Quelles expériences en famille peut-on réserver ?"',
            "<summary>Quali esperienze in famiglia si possono prenotare?</summary>",
            "<summary>Quelles expériences en famille peut-on réserver ?</summary>",
        ),
        (
            "de",
            '"name": "Quali esperienze in famiglia si possono prenotare?"',
            '"name": "Welche Familien-Erlebnisse kann man buchen?"',
            "<summary>Quali esperienze in famiglia si possono prenotare?</summary>",
            "<summary>Welche Familien-Erlebnisse kann man buchen?</summary>",
        ),
    ]:
        p = ROOT / lang / "famiglie.html"
        tt = p.read_text(encoding="utf-8")
        tt = tt.replace(a, b).replace(a2, b2)
        p.write_text(tt, encoding="utf-8", newline="\n")
        print("famiglie", lang, "ok")

    # gita body FR/DE
    for lang, newp in [
        (
            "fr",
            "<p>Depuis Milan (et depuis Varese, Novara ou le Lac Majeur) Macugnaga est une destination concrète pour une journée ou une nuitée : village alpin Drapeau Orange, mine d’or, Maison Walser et remontées quand elles sont ouvertes.</p>",
        ),
        (
            "de",
            "<p>Von Mailand (und von Varese, Novara oder dem Lago Maggiore) ist Macugnaga ein konkretes Ziel für einen Tag oder eine Übernachtung: Orange-Flag-Alpendorf, Goldmine, Walser-Haus und Bahnen wenn geöffnet.</p>",
        ),
    ]:
        p = ROOT / lang / "gita-milano-macugnaga.html"
        tt = p.read_text(encoding="utf-8")
        tt2 = re.sub(r"<p>Da Milano \(e .*?</p>", newp, tt, count=1)
        if tt2 != tt:
            p.write_text(tt2, encoding="utf-8", newline="\n")
            print("gita", lang, "ok")
        else:
            print("gita", lang, "miss")

    # escursioni
    for lang, newp in [
        (
            "en",
            "<p>Level routes, guided visits and activities designed also for the youngest: Macugnaga is authentic family-friendly mountain country, within easy reach of the Lombardy–Piedmont plain.</p>",
        ),
        (
            "fr",
            "<p>Parcours plats, visites guidées et activités pensées aussi pour les plus petits : Macugnaga est une montagne authentique à mesure de famille, à portée de route depuis la plaine lombardo-piémontaise.</p>",
        ),
        (
            "de",
            "<p>Ebenerdige Wege, Führungen und Aktivitäten auch für die Kleinsten: Macugnaga ist authentische familienfreundliche Bergwelt, gut erreichbar aus der lombardisch-piemontesischen Ebene.</p>",
        ),
    ]:
        p = ROOT / lang / "escursioni-famiglie-macugnaga.html"
        tt = p.read_text(encoding="utf-8")
        tt2 = re.sub(r"<p>Percorsi in piano,.*?</p>", newp, tt, count=1)
        if tt2 != tt:
            p.write_text(tt2, encoding="utf-8", newline="\n")
            print("escursioni", lang, "ok")
        else:
            print("escursioni", lang, "miss")

    # weekend JSON leftover EN/FR/DE
    for lang, newtxt in [
        (
            "en",
            "Two nights are enough to enjoy nature, the village and a cultural visit. Macugnaga is reachable in about 1.5–2.5 hours from Milan, Varese, Novara and Turin — and also from hotels and campsites on Lake Maggiore, Lake Orta and Lake Mergozzo.",
        ),
        (
            "fr",
            "Deux nuits suffisent pour vivre nature, village et une visite culturelle. Macugnaga est accessible en environ 1,5–2,5 heures depuis Milan, Varese, Novara et Turin — et aussi depuis hôtels et campings sur le Lac Majeur, le Lac d’Orta et le Lac de Mergozzo.",
        ),
        (
            "de",
            "Zwei Nächte reichen für Natur, Dorf und einen Kulturbesuch. Macugnaga ist in etwa 1,5–2,5 Stunden von Mailand, Varese, Novara und Turin erreichbar — und auch von Hotels und Campingplätzen am Lago Maggiore, Ortasee und Mergozzo-See.",
        ),
    ]:
        p = ROOT / lang / "weekend.html"
        tt = p.read_text(encoding="utf-8")
        tt2 = re.sub(
            r'"text": "Due notti bastano[^"]*"',
            f'"text": "{newtxt}"',
            tt,
            count=1,
        )
        if tt2 != tt:
            p.write_text(tt2, encoding="utf-8", newline="\n")
            print("weekend", lang, "ok")
        else:
            print("weekend", lang, "miss")


if __name__ == "__main__":
    main()
