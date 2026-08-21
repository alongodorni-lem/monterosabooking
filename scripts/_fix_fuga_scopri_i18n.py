# -*- coding: utf-8 -*-
"""Fix fuga-citta + scopri-macugnaga FAQ leftovers for FR/DE (and EN scopri)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EN_SCOPRI_FAQ = '''        <div class="faq-list" style="margin-top:1.25rem">
          <details class="faq-item reveal">
            <summary>Is Macugnaga suitable as a family mountain destination with children?</summary>
            <p class="faq-a">Yes: easy routes, a welcoming village and guided experiences without technical mountaineering. Ideal among the <strong>family mountains</strong> of Monte Rosa. See <a href="famiglie.html">Families</a> and the activities on the <a href="esperienze.html">booking portal</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is it a mountain destination for couples and groups of friends?</summary>
            <p class="faq-a">Yes: silence, Monte Rosa panoramas and nature experiences for a romantic weekend or a getaway with friends. Discover <a href="coppie.html">Couples</a> and <a href="weekend.html">Weekend</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is Macugnaga ideal for senior travellers?</summary>
            <p class="faq-a">Yes: soft pace, accessible trails, woodland wellness and cultural visits (Walser House Museum, gold mine). Learn more about <a href="senior.html">Seniors</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Are there hikes and walks in Macugnaga?</summary>
            <p class="faq-a">From the Dorf to the woods and trails under Monte Rosa: soft walks and easy hikes from the village. Book outdoor experiences on <a href="esperienze.html">Experiences</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is Macugnaga still real mountain country, with characterful places and historic chalets?</summary>
            <p class="faq-a">Yes: traditional architecture, historic chalets, fine landscape and Monte Rosa panoramas — an authentic alpine village, among the most beautiful towns in the Alps (Touring Club Italiano Orange Flag).</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is it suitable for a real-mountain weekend close to Milan, Novara, Varese and the cities of the plain?</summary>
            <p class="faq-a">Yes: about 2 h from Milan and 1.5 h from Novara and Varese; also Lake Maggiore, Turin, the Po Plain and Switzerland. See <a href="weekend.html">Weekend</a> and <a href="fuga-citta.html">City escape</a>.</p>
          </details>
        </div>'''

FR_SCOPRI_FAQ = '''        <div class="faq-list" style="margin-top:1.25rem">
          <details class="faq-item reveal">
            <summary>Macugnaga convient-elle comme montagne pour familles et montagne avec les enfants ?</summary>
            <p class="faq-a">Oui : parcours faciles, village accueillant et expériences guidées sans alpinisme technique. Idéale parmi les <strong>montagnes pour familles</strong> du Monte Rosa. Voir <a href="famiglie.html">Familles</a> et les activités du <a href="esperienze.html">portail de réservation</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Est-ce une destination de montagne pour couples et groupes d’amis ?</summary>
            <p class="faq-a">Oui : silence, panoramas sur le Monte Rosa et expériences nature pour un week-end romantique ou une escapade entre amis. Découvrez <a href="coppie.html">Couples</a> et <a href="weekend.html">Week-end</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Macugnaga est-elle idéale pour les touristes seniors ?</summary>
            <p class="faq-a">Oui : rythme doux, sentiers accessibles, bien-être en forêt et visites culturelles (Maison-musée Walser, mine d’or). En savoir plus sur <a href="senior.html">Seniors</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Y a-t-il des randonnées et promenades à Macugnaga ?</summary>
            <p class="faq-a">Du Dorf aux bois et aux sentiers sous le Monte Rosa : promenades et randonnées douces depuis le village. Réservez le plein air sur <a href="esperienze.html">Expériences</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Macugnaga est-elle encore une vraie montagne, avec des lieux typiques et d’anciens chalets ?</summary>
            <p class="faq-a">Oui : architecture traditionnelle, anciens chalets, beau paysage et panoramas sur le Monte Rosa — un village alpin authentique, parmi les plus beaux villages des Alpes (Drapeau Orange du Touring Club Italiano).</p>
          </details>
          <details class="faq-item reveal">
            <summary>Convient-elle pour un week-end de vraie montagne près de Milan, Novara, Varese et des villes de la plaine ?</summary>
            <p class="faq-a">Oui : environ 2 h depuis Milan et 1,5 h depuis Novara et Varese ; aussi Lac Majeur, Turin, plaine du Pô et Suisse. Voir <a href="weekend.html">Week-end</a> et <a href="fuga-citta.html">Échapper à la ville</a>.</p>
          </details>
        </div>'''

DE_SCOPRI_FAQ = '''        <div class="faq-list" style="margin-top:1.25rem">
          <details class="faq-item reveal">
            <summary>Eignet sich Macugnaga als Familienberg und Bergziel mit Kindern?</summary>
            <p class="faq-a">Ja: leichte Wege, einladendes Dorf und geführte Erlebnisse ohne technischen Alpinismus. Ideal unter den <strong>Familienbergen</strong> des Monte Rosa. Siehe <a href="famiglie.html">Familien</a> und die Aktivitäten im <a href="esperienze.html">Buchungsportal</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Ist es ein Bergziel für Paare und Freundesgruppen?</summary>
            <p class="faq-a">Ja: Stille, Monte-Rosa-Panoramen und Naturerlebnisse für ein romantisches Wochenende oder einen Ausflug mit Freunden. Entdecken Sie <a href="coppie.html">Paare</a> und <a href="weekend.html">Wochenende</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Ist Macugnaga ideal für Senioren?</summary>
            <p class="faq-a">Ja: sanftes Tempo, zugängliche Wege, Wald-Wellness und Kulturbesuche (Walser-Hausmuseum, Goldmine). Mehr erfahren auf <a href="senior.html">Senioren</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Gibt es Wanderungen und Spaziergänge in Macugnaga?</summary>
            <p class="faq-a">Vom Dorf zu Wäldern und Wegen unter dem Monte Rosa: Spaziergänge und sanfte Wanderungen vom Dorf aus. Outdoor auf <a href="esperienze.html">Erlebnisse</a> buchen.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Ist Macugnaga noch echte Bergwelt, mit charakteristischen Orten und alten Chalets?</summary>
            <p class="faq-a">Ja: traditionelle Architektur, historische Chalets, schöne Landschaft und Monte-Rosa-Panoramen — ein authentisches Alpendorf, unter den schönsten Alpenorten (Orange Flag des Touring Club Italiano).</p>
          </details>
          <details class="faq-item reveal">
            <summary>Eignet es sich für ein Wochenende echter Berge nahe Mailand, Novara, Varese und den Städten der Ebene?</summary>
            <p class="faq-a">Ja: etwa 2 h von Mailand und 1,5 h von Novara und Varese; auch Lago Maggiore, Turin, Po-Ebene und Schweiz. Siehe <a href="weekend.html">Wochenende</a> und <a href="fuga-citta.html">Stadtflucht</a>.</p>
          </details>
        </div>'''

FR_FUGA_BODY = [
    (
        'alt="Macugnaga, rifugio alpino dalla città"',
        'alt="Macugnaga, refuge alpin loin de la ville"',
    ),
    (
        "<p>Macugnaga, la vraie montagne, près de Milan, al Lac Majeur, Novara, Varese e città della pianura — et Torino, Genova e la Svizzera: gite, weekend e soggiorni lunghi in un villaggio alpino autentico.</p>",
        "<p>Macugnaga, la vraie montagne près de Milan, du Lac Majeur, Novara, Varese et des villes de la plaine — et Turin, Gênes et la Suisse : sorties, week-ends et longs séjours dans un village alpin authentique.</p>",
    ),
    ('<p class="section__eyebrow">Centralità</p>', '<p class="section__eyebrow">Centralité</p>'),
    ("<h2>Lontano dal rumore, a portata di strada</h2>", "<h2>Loin du bruit, à portée de route</h2>"),
    (
        "<p>Macugnaga è il punto d’incontro ideale tra Pianura Padana e Alpi: facilement accessible depuis <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> et le <strong>Lac Majeur</strong> (y compris Orta et Mergozzo), et aussi depuis <strong>Turin</strong>, <strong>Gênes</strong>, le canton du <strong>Valais</strong> et le <strong>Tessin</strong>.</p>",
        "<p>Macugnaga est le point de rencontre idéal entre la plaine du Pô et les Alpes : facilement accessible depuis <strong>Milan</strong>, <strong>Varese</strong>, <strong>Novara</strong> et le <strong>Lac Majeur</strong> (y compris Orta et Mergozzo), et aussi depuis <strong>Turin</strong>, <strong>Gênes</strong>, le canton du <strong>Valais</strong> et le <strong>Tessin</strong>.</p>",
    ),
    (
        "<p>Idéal pour <strong>gite in montagna</strong>, idee weekend fuori città e per ritrovare se stessi e i propri affetti — oppure per settimane rigeneranti e soggiorni lunghi, y compris per nomadi digitali e chi cerca quiete per studiare o lavorare. Se soggiorni in hotel o campeggio sui laghi, Macugnaga è una meta in montagna raggiungibile per una giornata: <a href=\"esperienze.html\">prenota online</a>.</p>",
        "<p>Idéal pour des <strong>sorties en montagne</strong>, des idées week-end hors de la ville et pour se retrouver — ou pour des semaines régénérantes et de longs séjours, y compris pour nomades numériques et quiconque cherche le calme pour étudier ou travailler. Si vous séjournez à l’hôtel ou au camping sur les lacs, Macugnaga est une destination de montagne accessible pour une journée : <a href=\"esperienze.html\">réserver en ligne</a>.</p>",
    ),
    ('href="weekend.html">Pianifica il weekend</a>', 'href="weekend.html">Planifier le week-end</a>'),
    ('aria-label="Distanze indicative da Macugnaga"', 'aria-label="Distances indicatives depuis Macugnaga"'),
    (
        'alt="Expériences a contatto con la natura nei boschi di Macugnaga"',
        'alt="Expériences nature dans les bois de Macugnaga"',
    ),
    ("<h2>Week-end, settimane, vita lenta</h2>", "<h2>Week-end, semaines, vie lente</h2>"),
    (
        "<li><strong>Week-end</strong> — fuga breve con pernottamento ed esperienze a contatto con la natura</li>",
        "<li><strong>Week-end</strong> — courte escapade avec nuitée et expériences nature</li>",
    ),
    (
        "<li><strong>Settimane</strong> — ritmo lento, escursioni soft, cultura e benessere</li>",
        "<li><strong>Semaines</strong> — rythme lent, randonnées douces, culture et bien-être</li>",
    ),
    (
        "<li><strong>Longs séjours</strong> — base tranquilla per lavoro remoto e studio</li>",
        "<li><strong>Longs séjours</strong> — base calme pour télétravail et études</li>",
    ),
    ('href="esperienze.html">Prenota esperienze</a>', 'href="esperienze.html">Réserver des expériences</a>'),
    (">Alloggi</a>", ">Hébergements</a>"),
    (
        "<h2 class=\"reveal\">Questions fréquentes sulla fuga dalla città</h2>",
        '<h2 class="reveal">Questions fréquentes sur l’échappée urbaine</h2>',
    ),
    (
        """          <details class="faq-item reveal">
            <summary>Macugnaga è la vraie montagne, près de Milan, Novara, Varese e città della pianura?</summary>
            <p class="faq-a">Sì: circa <strong>2 ore</strong> depuis Milan, <strong>1,5 ore</strong> depuis Novara e Varese; également accessible depuis le Lac Majeur, depuis Turin, Genova e depuis la Suisse. Idéal pour gite in montagna e weekend Macugnaga Monte Rosa.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Che tipo di gita in montagna si può fare?</summary>
            <p class="faq-a">Expériences a contatto con la natura, passeggiate, benessere, <a href="casa-museo-walser.html">Maison Walser</a> e <a href="miniera-oro.html">mine d’or</a> — montagna accessibile, senza alpinismo tecnico. <a href="esperienze.html">Réserver en ligne</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Meglio un weekend o un soggiorno più lungo?</summary>
            <p class="faq-a">Entrambi: il weekend basta per natura e relax; settimane e soggiorni lunghi sono perfetti per quiete, studio e lavoro remoto. Voir aussi <a href="weekend.html">Idées week-end</a>.</p>
          </details>""",
        """          <details class="faq-item reveal">
            <summary>Macugnaga est-elle la vraie montagne, près de Milan, Novara, Varese et des villes de la plaine ?</summary>
            <p class="faq-a">Oui : environ <strong>2 heures</strong> depuis Milan, <strong>1,5 heure</strong> depuis Novara et Varese ; également accessible depuis le Lac Majeur, Turin, Gênes et la Suisse. Idéale pour sorties en montagne et week-ends Macugnaga Monte Rosa.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Quel type de sortie en montagne peut-on faire ?</summary>
            <p class="faq-a">Expériences nature, promenades, bien-être, <a href="casa-museo-walser.html">Maison Walser</a> et <a href="miniera-oro.html">mine d’or</a> — montagne accessible, sans alpinisme technique. <a href="esperienze.html">Réserver en ligne</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Mieux vaut un week-end ou un séjour plus long ?</summary>
            <p class="faq-a">Les deux : le week-end suffit pour nature et détente ; semaines et longs séjours sont parfaits pour le calme, les études et le télétravail. Voir aussi <a href="weekend.html">Idées week-end</a>.</p>
          </details>""",
    ),
]

DE_FUGA_BODY = [
    (
        'alt="Macugnaga, rifugio alpino dalla città"',
        'alt="Macugnaga, alpine Zuflucht vor der Stadt"',
    ),
    (
        "<p>Macugnaga, echte Berge, nahe Mailand, al Lago Maggiore, Novara, Varese e città della pianura — und Torino, Genova e la Svizzera: gite, weekend e soggiorni lunghi in un villaggio alpino autentico.</p>",
        "<p>Macugnaga, echte Berge nahe Mailand, Lago Maggiore, Novara, Varese und den Städten der Ebene — und Turin, Genua und die Schweiz: Ausflüge, Wochenenden und längere Aufenthalte in einem authentischen Alpendorf.</p>",
    ),
    ('<p class="section__eyebrow">Centralità</p>', '<p class="section__eyebrow">Zentrale Lage</p>'),
    ("<h2>Lontano dal rumore, a portata di strada</h2>", "<h2>Fern vom Lärm, gut erreichbar</h2>"),
    (
        "<p>Macugnaga è il punto d’incontro ideale tra Pianura Padana e Alpi: leicht erreichbar von <strong>Mailand</strong>, <strong>Varese</strong>, <strong>Novara</strong> und dem <strong>Lago Maggiore</strong> (einschließlich Orta und Mergozzo), und auch von <strong>Turin</strong>, <strong>Genua</strong>, dem Kanton <strong>Wallis</strong> und dem <strong>Tessin</strong>.</p>",
        "<p>Macugnaga ist der ideale Treffpunkt zwischen Po-Ebene und Alpen: leicht erreichbar von <strong>Mailand</strong>, <strong>Varese</strong>, <strong>Novara</strong> und dem <strong>Lago Maggiore</strong> (einschließlich Orta und Mergozzo), und auch von <strong>Turin</strong>, <strong>Genua</strong>, dem Kanton <strong>Wallis</strong> und dem <strong>Tessin</strong>.</p>",
    ),
    (
        "<p>Ideal für <strong>gite in montagna</strong>, idee weekend fuori città e per ritrovare se stessi e i propri affetti — oppure per settimane rigeneranti e soggiorni lunghi, einschließlich per nomadi digitali e chi cerca quiete per studiare o lavorare. Se soggiorni in hotel o campeggio sui laghi, Macugnaga è una meta in montagna raggiungibile per una giornata: <a href=\"esperienze.html\">prenota online</a>.</p>",
        "<p>Ideal für <strong>Bergausflüge</strong>, Wochenendideen außerhalb der Stadt und um sich und die eigenen Lieben wiederzufinden — oder für erholsame Wochen und längere Aufenthalte, auch für digitale Nomaden und alle, die Ruhe zum Lernen oder Arbeiten suchen. Wenn Sie in Hotel oder Camping an den Seen übernachten, ist Macugnaga ein Bergziel für einen Tag: <a href=\"esperienze.html\">online buchen</a>.</p>",
    ),
    ('href="weekend.html">Pianifica il weekend</a>', 'href="weekend.html">Wochenende planen</a>'),
    ('aria-label="Distanze indicative da Macugnaga"', 'aria-label="Ungefähre Entfernungen von Macugnaga"'),
    ("<h2>Wochenende, settimane, vita lenta</h2>", "<h2>Wochenenden, Wochen, langsames Leben</h2>"),
    (
        "<li><strong>Wochenende</strong> — fuga breve con pernottamento ed esperienze a contatto con la natura</li>",
        "<li><strong>Wochenende</strong> — kurze Flucht mit Übernachtung und Naturerlebnissen</li>",
    ),
    (
        "<li><strong>Settimane</strong> — ritmo lento, escursioni soft, cultura e benessere</li>",
        "<li><strong>Wochen</strong> — langsames Tempo, sanfte Wanderungen, Kultur und Wellness</li>",
    ),
    (
        "<li><strong>Lange Aufenthalte</strong> — base tranquilla per lavoro remoto e studio</li>",
        "<li><strong>Lange Aufenthalte</strong> — ruhige Basis für Remote-Arbeit und Studium</li>",
    ),
    ('href="esperienze.html">Prenota esperienze</a>', 'href="esperienze.html">Erlebnisse buchen</a>'),
    (">Alloggi</a>", ">Unterkünfte</a>"),
]


def replace_faq_div(html: str, new_block: str) -> str:
    import re

    return re.sub(
        r'<div class="faq-list"[^>]*>.*?</div>\s*<div class="btn-row',
        new_block + '\n        <div class="btn-row',
        html,
        count=1,
        flags=re.S,
    )


def apply_pairs(path: Path, pairs: list[tuple[str, str]]) -> int:
    text = path.read_text(encoding="utf-8")
    n = 0
    for old, new in pairs:
        if old in text:
            c = text.count(old)
            text = text.replace(old, new)
            n += c
    if n:
        path.write_text(text, encoding="utf-8", newline="\n")
    return n


def main() -> None:
    # scopri FAQ
    for lang, block in (
        ("en", EN_SCOPRI_FAQ),
        ("fr", FR_SCOPRI_FAQ),
        ("de", DE_SCOPRI_FAQ),
    ):
        path = ROOT / lang / "scopri-macugnaga.html"
        html = path.read_text(encoding="utf-8")
        new = replace_faq_div(html, block)
        if new != html:
            path.write_text(new, encoding="utf-8", newline="\n")
            print(f"scopri FAQ {lang}: ok")
        else:
            print(f"scopri FAQ {lang}: FAILED pattern")

    n = apply_pairs(ROOT / "fr" / "fuga-citta.html", FR_FUGA_BODY)
    print(f"fr fuga: {n}")
    # DE fuga - read current hero text first may differ
    de_path = ROOT / "de" / "fuga-citta.html"
    de_text = de_path.read_text(encoding="utf-8")
    # broader DE replacements
    de_extra = [
        (
            "Macugnaga, la montagna vera, vicina a Milano, al Lago Maggiore, Novara, Varese e città della pianura — e a Torino, Genova e la Svizzera: gite, weekend e soggiorni lunghi in un villaggio alpino autentico.",
            "Macugnaga, echte Berge nahe Mailand, Lago Maggiore, Novara, Varese und den Städten der Ebene — und Turin, Genua und die Schweiz: Ausflüge, Wochenenden und längere Aufenthalte in einem authentischen Alpendorf.",
        ),
        ("Stadtflucht, Herz der Alpen", "Stadtflucht, Herz der Alpen"),
        ("<h1>Stadtflucht, cuore delle Alpi</h1>", "<h1>Stadtflucht, Herz der Alpen</h1>"),
        ("<h1>Stadtflucht, Herz der Alpen</h1>", "<h1>Stadtflucht, Herz der Alpen</h1>"),
    ]
    n2 = apply_pairs(de_path, DE_FUGA_BODY + de_extra)
    # FAQ block DE
    de_text = de_path.read_text(encoding="utf-8")
    old_faq = """          <details class="faq-item reveal">
            <summary>Macugnaga è la montagna vera, vicina a Milano, Novara, Varese e città della pianura?</summary>
            <p class="faq-a">Sì: circa <strong>2 ore</strong> von Mailand, <strong>1,5 ore</strong> von Novara e Varese; auch erreichbar vom Lago Maggiore, von Turin, Genova e aus der Schweiz. Ideal für gite in montagna e weekend Macugnaga Monte Rosa.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Che tipo di gita in montagna si può fare?</summary>
            <p class="faq-a">Erlebnisse a contatto con la natura, passeggiate, benessere, <a href="casa-museo-walser.html">Walser-Haus</a> e <a href="miniera-oro.html">Goldmine</a> — montagna accessibile, senza alpinismo tecnico. <a href="esperienze.html">Online buchen</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Meglio un weekend o un soggiorno più lungo?</summary>
            <p class="faq-a">Entrambi: il weekend basta per natura e relax; settimane e soggiorni lunghi sono perfetti per quiete, studio e lavoro remoto. Siehe auch <a href="weekend.html">Wochenend-Ideen</a>.</p>
          </details>"""
    new_faq = """          <details class="faq-item reveal">
            <summary>Sind es echte Berge, nahe Mailand, Novara, Varese und den Städten der Ebene?</summary>
            <p class="faq-a">Ja: etwa <strong>2 Stunden</strong> von Mailand, <strong>1,5 Stunden</strong> von Novara und Varese; auch erreichbar vom Lago Maggiore, Turin, Genua und der Schweiz. Ideal für Bergausflüge und Wochenenden Macugnaga Monte Rosa.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Welche Art von Bergausflug ist möglich?</summary>
            <p class="faq-a">Naturerlebnisse, Spaziergänge, Wellness, <a href="casa-museo-walser.html">Walser-Haus</a> und <a href="miniera-oro.html">Goldmine</a> — zugängliche Berge, ohne technischen Alpinismus. <a href="esperienze.html">Online buchen</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Besser ein Wochenende oder ein längerer Aufenthalt?</summary>
            <p class="faq-a">Beides: das Wochenende reicht für Natur und Entspannung; Wochen und längere Aufenthalte sind ideal für Ruhe, Studium und Remote-Arbeit. Siehe auch <a href="weekend.html">Wochenend-Ideen</a>.</p>
          </details>"""
    if old_faq in de_text:
        de_text = de_text.replace(old_faq, new_faq)
        de_path.write_text(de_text, encoding="utf-8", newline="\n")
        print("de fuga FAQ: ok")
    else:
        print("de fuga FAQ: pattern miss — trying softer")
        # softer: replace summary lines
        for a, b in [
            ("Macugnaga è la montagna vera, vicina a Milano, Novara, Varese e città della pianura?",
             "Sind es echte Berge, nahe Mailand, Novara, Varese und den Städten der Ebene?"),
            ("Che tipo di gita in montagna si può fare?", "Welche Art von Bergausflug ist möglich?"),
            ("Meglio un weekend o un soggiorno più lungo?", "Besser ein Wochenende oder ein längerer Aufenthalt?"),
            ("Frequently asked questions on the fuga dalla città", "Häufige Fragen zur Stadtflucht"),
            ("Häufig gestellte Fragen zur fuga dalla città", "Häufige Fragen zur Stadtflucht"),
            ("Fragen zur fuga dalla città", "Fragen zur Stadtflucht"),
        ]:
            if a in de_text:
                de_text = de_text.replace(a, b)
        de_path.write_text(de_text, encoding="utf-8", newline="\n")
    print(f"de fuga pairs: {n2}")


if __name__ == "__main__":
    main()
