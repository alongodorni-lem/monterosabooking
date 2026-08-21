# -*- coding: utf-8 -*-
"""Fix remaining strong Italian leftovers (famiglie, scopri, index, landings)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATCHES: dict[str, list[tuple[str, str]]] = {
    "en/famiglie.html": [
        (
            '<p>Montagne per famiglie ai piedi del Monte Rosa: percorsi facili, esperienze guidate e un villaggio dove i piccoli scoprono natura e storia in sicurezza.</p>',
            '<p>Family mountains at the foot of Monte Rosa: easy routes, guided experiences and a village where little ones discover nature and history safely.</p>',
        ),
        ('<p class="section__eyebrow">Per le famiglie</p>', '<p class="section__eyebrow">For families</p>'),
        (
            '<h2>Facilità e sicurezza, senza rinunciare alla meraviglia</h2>',
            '<h2>Ease and safety, without giving up wonder</h2>',
        ),
        (
            '<p>Perfetta per <strong>gite in montagna</strong> e weekend from Milan, dal Lake Maggiore, Varese e Novara — senza stress e senza alpinismo tecnico.</p>',
            '<p>Perfect for <strong>mountain day trips</strong> and weekends from Milan, Lake Maggiore, Varese and Novara — without stress and without technical mountaineering.</p>',
        ),
        ('<li>Proposte chiare per età e difficoltà</li>', '<li>Clear options by age and difficulty</li>'),
        (
            '>Book an experience in famiglia</a>',
            '>Book a family experience</a>',
        ),
        (
            'alt="Famiglia in montagna a Macugnaga"',
            'alt="Family in the mountains in Macugnaga"',
        ),
        (
            'alt="Attività per bambini a Macugnaga"',
            'alt="Activities for children in Macugnaga"',
        ),
    ],
    "fr/famiglie.html": [
        (
            '<p>Montagne per famiglie ai piedi del Monte Rosa: percorsi facili, esperienze guidate e un villaggio dove i piccoli scoprono natura e storia in sicurezza.</p>',
            '<p>Montagne pour familles au pied du Monte Rosa : parcours faciles, expériences guidées et un village où les petits découvrent nature et histoire en sécurité.</p>',
        ),
        ('<p class="section__eyebrow">Per le famiglie</p>', '<p class="section__eyebrow">Pour les familles</p>'),
        (
            '<h2>Facilità e sicurezza, senza rinunciare alla meraviglia</h2>',
            '<h2>Facilité et sécurité, sans renoncer à l’émerveillement</h2>',
        ),
        (
            '<p>Macugnaga è la <strong>montagna a misura di famiglia</strong>: passeggiate nel Dorf, sentieri adatti aussi ai più piccoli, visite alla Casa Museo e alla mine d’or, attività outdoor in natura nel fresco clima estivo alpino.</p>',
            '<p>Macugnaga est la <strong>montagne à dimension familiale</strong> : promenades dans le Dorf, sentiers adaptés aussi aux plus petits, visites à la Maison-musée et à la mine d’or, activités outdoor dans la nature au frais climat estival alpin.</p>',
        ),
        (
            '<p>Perfetta per <strong>gite in montagna</strong> e week-end depuis Milan, dal Lac Majeur, Varese e Novara — senza stress e senza alpinismo tecnico.</p>',
            '<p>Parfaite pour des <strong>sorties en montagne</strong> et week-ends depuis Milan, le lac Majeur, Varese et Novara — sans stress et sans alpinisme technique.</p>',
        ),
        ('<li>Proposte chiare per età e difficoltà</li>', '<li>Propositions claires par âge et difficulté</li>'),
        ('>Réserver une expérience in famiglia</a>', '>Réserver une expérience en famille</a>'),
        ('alt="Famiglia in montagna a Macugnaga"', 'alt="Famille en montagne à Macugnaga"'),
        ('alt="Attività per bambini a Macugnaga"', 'alt="Activités pour enfants à Macugnaga"'),
    ],
    "de/famiglie.html": [
        (
            '<p>Montagne per famiglie ai piedi del Monte Rosa: percorsi facili, esperienze guidate e un villaggio dove i piccoli scoprono natura e storia in sicurezza.</p>',
            '<p>Familienberge am Fuße des Monte Rosa: leichte Wege, geführte Erlebnisse und ein Dorf, in dem die Kleinen Natur und Geschichte sicher entdecken.</p>',
        ),
        ('<p class="section__eyebrow">Per le famiglie</p>', '<p class="section__eyebrow">Für Familien</p>'),
        (
            '<h2>Facilità e sicurezza, senza rinunciare alla meraviglia</h2>',
            '<h2>Leichtigkeit und Sicherheit, ohne auf Staunen zu verzichten</h2>',
        ),
        (
            '<p>Macugnaga è la <strong>montagna a misura di famiglia</strong>: passeggiate nel Dorf, sentieri adatti auch ai più piccoli, visite alla Casa Museo e alla Goldmine, attività outdoor in natura nel fresco clima estivo alpino.</p>',
            '<p>Macugnaga ist der <strong>familienfreundliche Berg</strong>: Spaziergänge im Dorf, Wege auch für die Kleinen, Besuche im Hausmuseum und in der Goldmine, Outdoor-Aktivitäten in der Natur im frischen alpinen Sommerklima.</p>',
        ),
        (
            '<p>Perfetta per <strong>gite in montagna</strong> e Wochenenden von Mailand, dal Lago Maggiore, Varese e Novara — senza stress e senza alpinismo tecnico.</p>',
            '<p>Perfekt für <strong>Bergausflüge</strong> und Wochenenden ab Mailand, Lago Maggiore, Varese und Novara — ohne Stress und ohne technischen Alpinismus.</p>',
        ),
        ('<li>Proposte chiare per età e difficoltà</li>', '<li>Klare Angebote nach Alter und Schwierigkeit</li>'),
        ('>Erlebnis in famiglia buchen</a>', '>Familienerlebnis buchen</a>'),
        ('alt="Famiglia in montagna a Macugnaga"', 'alt="Familie in den Bergen in Macugnaga"'),
        ('alt="Attività per bambini a Macugnaga"', 'alt="Aktivitäten für Kinder in Macugnaga"'),
    ],
    "en/scopri-macugnaga.html": [
        (
            '"description": "Località di montagna vera ai piedi del Monte Rosa: villaggio alpino con architettura tradizionale, boschi, benessere ed esperienze accessibili. Ideale per famiglie, montagna con i bambini, coppie, senior e weekend from the Po Plain, dal Lake Maggiore e from Switzerland."',
            '"description": "Real mountain destination at the foot of Monte Rosa: alpine village with traditional architecture, woods, wellness and accessible experiences. Ideal for families, mountains with children, couples, seniors and weekends from the Po Plain, Lake Maggiore and Switzerland."',
        ),
    ],
    "fr/scopri-macugnaga.html": [
        (
            '"description": "Località di montagna vera ai piedi del Monte Rosa: villaggio alpino con architettura tradizionale, boschi, benessere ed esperienze accessibili. Idéal pour famiglie, montagna con i bambini, coppie, senior e weekend depuis la plaine du Pô, dal Lac Majeur e depuis la Suisse."',
            '"description": "Vraie destination de montagne au pied du Monte Rosa : village alpin à l’architecture traditionnelle, forêts, bien-être et expériences accessibles. Idéale pour familles, montagne avec enfants, couples, seniors et week-ends depuis la plaine du Pô, le lac Majeur et la Suisse."',
        ),
    ],
    "de/scopri-macugnaga.html": [
        (
            '"description": "Località di montagna vera ai piedi del Monte Rosa: villaggio alpino con architettura tradizionale, boschi, benessere ed esperienze accessibili. Ideal für famiglie, montagna con i bambini, coppie, senior e weekend von der Po-Ebene, dal Lago Maggiore e aus der Schweiz."',
            '"description": "Echtes Bergziel am Fuße des Monte Rosa: Alpendorf mit traditioneller Architektur, Wäldern, Wellness und zugänglichen Erlebnissen. Ideal für Familien, Berge mit Kindern, Paare, Senioren und Wochenenden von der Po-Ebene, vom Lago Maggiore und aus der Schweiz."',
        ),
    ],
    "en/montagna-dagosto-8-20-agosto.html": [
        (
            '"description": "Villaggio alpino ai piedi della parete Est del Monte Rosa, Valle Anzasca (VB), Piemonte."',
            '"description": "Alpine village at the foot of the east face of Monte Rosa, Anzasca Valley (VB), Piedmont."',
        ),
    ],
    "fr/montagna-dagosto-8-20-agosto.html": [
        (
            '"description": "Villaggio alpino ai piedi della parete Est del Monte Rosa, Valle Anzasca (VB), Piemonte."',
            '"description": "Village alpin au pied de la face Est du Monte Rosa, Valle Anzasca (VB), Piémont."',
        ),
    ],
    "de/montagna-dagosto-8-20-agosto.html": [
        (
            '"description": "Villaggio alpino ai piedi della parete Est del Monte Rosa, Valle Anzasca (VB), Piemonte."',
            '"description": "Alpendorf am Fuße der Ostwand des Monte Rosa, Valle Anzasca (VB), Piemont."',
        ),
    ],
    "fr/index.html": [
        (
            '"description": "Réserver en ligne gite ed esperienze a Macugnaga Monte Rosa: escursioni, benessere e natura vicino a Milano, al Lac Majeur, Varese e Novara."',
            '"description": "Réservez en ligne sorties et expériences à Macugnaga Monte Rosa : randonnées, bien-être et nature près de Milan, du lac Majeur, Varese et Novara."',
        ),
        (
            '"description": "Villaggio alpino tra i paesi più belli delle Alpi (Bandiera Arancione del Touring Club Italiano), ai piedi della parete Est del Monte Rosa. Idéal pour gite in montagna, esperienze a contatto con la natura e weekend vicino a Milano, al Lac Majeur, Varese e Novara."',
            '"description": "Village alpin parmi les plus beaux des Alpes (Bandiera Arancione du Touring Club Italiano), au pied de la face Est du Monte Rosa. Idéal pour sorties en montagne, expériences au contact de la nature et week-ends près de Milan, du lac Majeur, Varese et Novara."',
        ),
        (
            '"touristType": ["famiglie", "coppie", "senior", "weekend", "gite dalla pianura", "ospiti dei laghi"]',
            '"touristType": ["familles", "couples", "seniors", "week-end", "sorties depuis la plaine", "hôtes des lacs"]',
        ),
    ],
    "de/index.html": [
        (
            '"description": "Villaggio alpino tra i paesi più belli delle Alpi (Bandiera Arancione del Touring Club Italiano), ai piedi della parete Est del Monte Rosa. Ideal für gite in montagna, esperienze a contatto con la natura e weekend nahe Mailand, Lago Maggiore, Varese und Novara."',
            '"description": "Alpendorf unter den schönsten der Alpen (Bandiera Arancione des Touring Club Italiano), am Fuße der Ostwand des Monte Rosa. Ideal für Bergausflüge, Naturerlebnisse und Wochenenden nahe Mailand, Lago Maggiore, Varese und Novara."',
        ),
    ],
    "en/escursioni-famiglie-macugnaga.html": [
        (
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.macugnagabooking.it/en/"},{"@type":"ListItem","position":2,"name":"Escursioni per famiglie a Macugnaga","item":"https://www.macugnagabooking.it/en/escursioni-famiglie-macugnaga.html"}]}',
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.macugnagabooking.it/en/"},{"@type":"ListItem","position":2,"name":"Family hikes in Macugnaga","item":"https://www.macugnagabooking.it/en/escursioni-famiglie-macugnaga.html"}]}',
        ),
        (
            '{"@context":"https://schema.org","@type":"WebPage","name":"Escursioni per famiglie a Macugnaga","url":"https://www.macugnagabooking.it/en/escursioni-famiglie-macugnaga.html","description":"Escursioni e attività per famiglie a Macugnaga Monte Rosa: percorsi facili, miniera accessibile, Walser House. Book online.","isPartOf":{"@type":"WebSite","name":"Macugnaga Booking – Experiences at the foot of Monte Rosa","url":"https://www.macugnagabooking.it/en/"}}',
            '{"@context":"https://schema.org","@type":"WebPage","name":"Family hikes in Macugnaga","url":"https://www.macugnagabooking.it/en/escursioni-famiglie-macugnaga.html","description":"Family hikes and activities in Macugnaga Monte Rosa: easy routes, accessible mine, Walser House. Book online.","isPartOf":{"@type":"WebSite","name":"Macugnaga Booking – Experiences at the foot of Monte Rosa","url":"https://www.macugnagabooking.it/en/"}}',
        ),
        (
            '<p class="breadcrumb"><a href="index.html">Home</a> · Escursioni per famiglie a Macugnaga</p>',
            '<p class="breadcrumb"><a href="index.html">Home</a> · Family hikes in Macugnaga</p>',
        ),
        (
            '<h1>Escursioni per famiglie a Macugnaga</h1>',
            '<h1>Family hikes in Macugnaga</h1>',
        ),
        (
            '<p>Escursioni e attività per famiglie a Macugnaga Monte Rosa: percorsi facili, miniera accessibile, Walser House. Book online.</p>',
            '<p>Family hikes and activities in Macugnaga Monte Rosa: easy routes, accessible mine, Walser House. Book online.</p>',
        ),
    ],
    "fr/escursioni-famiglie-macugnaga.html": [
        (
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://www.macugnagabooking.it/fr/"},{"@type":"ListItem","position":2,"name":"Escursioni per famiglie a Macugnaga","item":"https://www.macugnagabooking.it/fr/escursioni-famiglie-macugnaga.html"}]}',
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://www.macugnagabooking.it/fr/"},{"@type":"ListItem","position":2,"name":"Randonnées en famille à Macugnaga","item":"https://www.macugnagabooking.it/fr/escursioni-famiglie-macugnaga.html"}]}',
        ),
        (
            '{"@context":"https://schema.org","@type":"WebPage","name":"Escursioni per famiglie a Macugnaga","url":"https://www.macugnagabooking.it/fr/escursioni-famiglie-macugnaga.html","description":"Escursioni e attività per famiglie a Macugnaga Monte Rosa: percorsi facili, miniera accessibile, Maison Walser. Réserver en ligne.","isPartOf":{"@type":"WebSite","name":"Macugnaga Booking – Expériences au pied du Monte Rosa","url":"https://www.macugnagabooking.it/fr/"}}',
            '{"@context":"https://schema.org","@type":"WebPage","name":"Randonnées en famille à Macugnaga","url":"https://www.macugnagabooking.it/fr/escursioni-famiglie-macugnaga.html","description":"Randonnées et activités en famille à Macugnaga Monte Rosa : parcours faciles, mine accessible, Maison Walser. Réservez en ligne.","isPartOf":{"@type":"WebSite","name":"Macugnaga Booking – Expériences au pied du Monte Rosa","url":"https://www.macugnagabooking.it/fr/"}}',
        ),
        (
            '<p class="breadcrumb"><a href="index.html">Accueil</a> · Escursioni per famiglie a Macugnaga</p>',
            '<p class="breadcrumb"><a href="index.html">Accueil</a> · Randonnées en famille à Macugnaga</p>',
        ),
        (
            '<h1>Escursioni per famiglie a Macugnaga</h1>',
            '<h1>Randonnées en famille à Macugnaga</h1>',
        ),
        (
            '<p>Escursioni e attività per famiglie a Macugnaga Monte Rosa: percorsi facili, miniera accessibile, Maison Walser. Réserver en ligne.</p>',
            '<p>Randonnées et activités en famille à Macugnaga Monte Rosa : parcours faciles, mine accessible, Maison Walser. Réservez en ligne.</p>',
        ),
    ],
    "de/escursioni-famiglie-macugnaga.html": [
        (
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Start","item":"https://www.macugnagabooking.it/de/"},{"@type":"ListItem","position":2,"name":"Escursioni per famiglie a Macugnaga","item":"https://www.macugnagabooking.it/de/escursioni-famiglie-macugnaga.html"}]}',
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Start","item":"https://www.macugnagabooking.it/de/"},{"@type":"ListItem","position":2,"name":"Familienwanderungen in Macugnaga","item":"https://www.macugnagabooking.it/de/escursioni-famiglie-macugnaga.html"}]}',
        ),
        (
            '{"@context":"https://schema.org","@type":"WebPage","name":"Escursioni per famiglie a Macugnaga","url":"https://www.macugnagabooking.it/de/escursioni-famiglie-macugnaga.html","description":"Escursioni e attività per famiglie a Macugnaga Monte Rosa: percorsi facili, miniera accessibile, Walser-Haus. Online buchen.","isPartOf":{"@type":"WebSite","name":"Macugnaga Booking – Erlebnisse am Fuße des Monte Rosa","url":"https://www.macugnagabooking.it/de/"}}',
            '{"@context":"https://schema.org","@type":"WebPage","name":"Familienwanderungen in Macugnaga","url":"https://www.macugnagabooking.it/de/escursioni-famiglie-macugnaga.html","description":"Familienwanderungen und Aktivitäten in Macugnaga Monte Rosa: leichte Wege, zugängliche Mine, Walser-Haus. Online buchen.","isPartOf":{"@type":"WebSite","name":"Macugnaga Booking – Erlebnisse am Fuße des Monte Rosa","url":"https://www.macugnagabooking.it/de/"}}',
        ),
        (
            '<p class="breadcrumb"><a href="index.html">Start</a> · Escursioni per famiglie a Macugnaga</p>',
            '<p class="breadcrumb"><a href="index.html">Start</a> · Familienwanderungen in Macugnaga</p>',
        ),
        (
            '<h1>Escursioni per famiglie a Macugnaga</h1>',
            '<h1>Familienwanderungen in Macugnaga</h1>',
        ),
        (
            '<p>Escursioni e attività per famiglie a Macugnaga Monte Rosa: percorsi facili, miniera accessibile, Walser-Haus. Online buchen.</p>',
            '<p>Familienwanderungen und Aktivitäten in Macugnaga Monte Rosa: leichte Wege, zugängliche Mine, Walser-Haus. Online buchen.</p>',
        ),
    ],
}


def main() -> None:
    for rel, pairs in PATCHES.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        n = 0
        for old, new in pairs:
            if old in text:
                text = text.replace(old, new)
                n += 1
            else:
                print(f"MISS {rel}: {old[:80]!r}")
        path.write_text(text, encoding="utf-8")
        print(f"{rel}: {n}/{len(pairs)}")


if __name__ == "__main__":
    main()
