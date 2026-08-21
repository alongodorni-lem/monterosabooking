# -*- coding: utf-8 -*-
"""Patch remaining famiglie / casa visible leftovers."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATCHES = {
    "en/famiglie.html": [
        ("<h2 class=\"reveal\">Idee per una giornata in famiglia</h2>",
         "<h2 class=\"reveal\">Ideas for a family day</h2>"),
        ("<p class=\"lead reveal\">Tre spunti per vivere la montagna con i bambini: gioco, cultura e piccola avventura.</p>",
         "<p class=\"lead reveal\">Three ideas for mountains with children: play, culture and a little adventure.</p>"),
        ("alt=\"Bambini in attività outdoor\"",
         "alt=\"Children in outdoor activities\""),
        ("<div class=\"exp-card__body\"><h3>Natura e gioco</h3><p>Uscite soft tra boschi e prati: esperienze a contatto con la natura, al ritmo dei bambini.</p></div>",
         "<div class=\"exp-card__body\"><h3>Nature and play</h3><p>Soft outings in woods and meadows: nature experiences at a child’s pace.</p></div>"),
        ("<div class=\"exp-card__body\"><h3>Casa Museo</h3><p>Book online: storie walser da raccontare ai più piccoli.</p></div>",
         "<div class=\"exp-card__body\"><h3>House Museum</h3><p>Book online: Walser stories to tell the little ones.</p></div>"),
        ("alt=\"Families che cercano oro al torrente con Monte Rosa\"",
         "alt=\"Families panning for gold by the stream with Monte Rosa\""),
        ("<div class=\"exp-card__body\"><h3>Alla ricerca dell’oro</h3><p>Un’avventura che resta impressa nella memoria.</p></div>",
         "<div class=\"exp-card__body\"><h3>Gold panning</h3><p>An adventure that stays in the memory.</p></div>"),
        ("<h2 class=\"reveal\">Frequently asked questions per le famiglie</h2>",
         "<h2 class=\"reveal\">Frequently asked questions for families</h2>"),
        ("<p class=\"faq-a\">Natura e gioco, <a href=\"casa-museo-walser.html\">Walser House Museum</a>, <a href=\"miniera-oro.html\">gold mine</a> (including con passeggino), ricerca dell’oro e altre attività. See <a href=\"esperienze.html\">Experiences</a>.</p>",
         "<p class=\"faq-a\">Nature and play, <a href=\"casa-museo-walser.html\">Walser House Museum</a>, <a href=\"miniera-oro.html\">gold mine</a> (including with a pushchair), gold panning and other activities. See <a href=\"esperienze.html\">Experiences</a>.</p>"),
        ("<p class=\"faq-a\">Alloggio a Macugnaga, una o due esperienze prenotate online e passeggiate in paese. Guida pratica su <a href=\"weekend.html\">Weekend</a>.</p>",
         "<p class=\"faq-a\">Stay in Macugnaga, book one or two experiences online and combine with village walks. Practical guide on <a href=\"weekend.html\">Weekend</a>.</p>"),
    ],
    "fr/famiglie.html": [
        ("<h2 class=\"reveal\">Idee per una giornata in famiglia</h2>",
         "<h2 class=\"reveal\">Idées pour une journée en famille</h2>"),
        ("<p class=\"lead reveal\">Tre spunti per vivere la montagna con i bambini: gioco, cultura e piccola avventura.</p>",
         "<p class=\"lead reveal\">Trois idées pour vivre la montagne avec les enfants : jeu, culture et petite aventure.</p>"),
        ("alt=\"Bambini in attività outdoor\"",
         "alt=\"Enfants en activités outdoor\""),
        ("<div class=\"exp-card__body\"><h3>Natura e gioco</h3><p>Uscite soft tra boschi e prati: esperienze a contatto con la natura, al ritmo dei bambini.</p></div>",
         "<div class=\"exp-card__body\"><h3>Nature et jeu</h3><p>Sorties douces entre bois et prairies : expériences au contact de la nature, au rythme des enfants.</p></div>"),
        ("<div class=\"exp-card__body\"><h3>Casa Museo</h3><p>Réserver en ligne: storie walser da raccontare ai più piccoli.</p></div>",
         "<div class=\"exp-card__body\"><h3>Maison-musée</h3><p>Réservez en ligne : histoires walser à raconter aux plus petits.</p></div>"),
        ("alt=\"Familles che cercano oro al torrente con Monte Rosa\"",
         "alt=\"Familles cherchant de l’or au torrent avec le Monte Rosa\""),
        ("alt=\"Visita Maison-musée Walser per famiglie\"",
         "alt=\"Visite Maison-musée Walser pour familles\""),
        ("<div class=\"exp-card__body\"><h3>Alla ricerca dell’oro</h3><p>Un’avventura che resta impressa nella memoria.</p></div>",
         "<div class=\"exp-card__body\"><h3>À la recherche de l’or</h3><p>Une aventure qui reste gravée dans la mémoire.</p></div>"),
        ("<h2 class=\"reveal\">Questions fréquentes per le famiglie</h2>",
         "<h2 class=\"reveal\">Questions fréquentes pour les familles</h2>"),
        ("<p class=\"faq-a\">Sì: percorsi facili, villaggio accogliente ed esperienze guidate. Ideale tra le <strong>montagne per famiglie</strong> del Monte Rosa, y compris per gite depuis Milan, dal Lac Majeur, Varese e Novara.</p>",
         "<p class=\"faq-a\">Oui : parcours faciles, village accueillant et expériences guidées. Idéale parmi les <strong>montagnes pour familles</strong> du Monte Rosa, y compris pour des sorties depuis Milan, le lac Majeur, Varese et Novara.</p>"),
        ("<p class=\"faq-a\">Natura e gioco, <a href=\"casa-museo-walser.html\">Maison-musée Walser</a>, <a href=\"miniera-oro.html\">mine d’or</a> (y compris con passeggino), ricerca dell’oro e altre attività. Voir <a href=\"esperienze.html\">Expériences</a>.</p>",
         "<p class=\"faq-a\">Nature et jeu, <a href=\"casa-museo-walser.html\">Maison-musée Walser</a>, <a href=\"miniera-oro.html\">mine d’or</a> (y compris avec poussette), recherche de l’or et autres activités. Voir <a href=\"esperienze.html\">Expériences</a>.</p>"),
        ("<summary>Come organizzare un weekend in montagna con i bambini?</summary>",
         "<summary>Comment organiser un week-end en montagne avec les enfants ?</summary>"),
        ("<p class=\"faq-a\">Alloggio a Macugnaga, una o due esperienze prenotate online e passeggiate in paese. Guida pratica su <a href=\"weekend.html\">Week-end</a>.</p>",
         "<p class=\"faq-a\">Hébergement à Macugnaga, une ou deux expériences réservées en ligne et promenades au village. Guide pratique sur <a href=\"weekend.html\">Week-end</a>.</p>"),
    ],
    "de/famiglie.html": [
        ("<h2 class=\"reveal\">Idee per una giornata in famiglia</h2>",
         "<h2 class=\"reveal\">Ideen für einen Familientag</h2>"),
        ("<p class=\"lead reveal\">Tre spunti per vivere la montagna con i bambini: gioco, cultura e piccola avventura.</p>",
         "<p class=\"lead reveal\">Drei Ideen für Berge mit Kindern: Spiel, Kultur und ein kleines Abenteuer.</p>"),
        ("alt=\"Bambini in attività outdoor\"",
         "alt=\"Kinder bei Outdoor-Aktivitäten\""),
        ("<div class=\"exp-card__body\"><h3>Natura e gioco</h3><p>Uscite soft tra boschi e prati: esperienze a contatto con la natura, al ritmo dei bambini.</p></div>",
         "<div class=\"exp-card__body\"><h3>Natur und Spiel</h3><p>Sanfte Ausflüge in Wäldern und Wiesen: Naturerlebnisse im Tempo der Kinder.</p></div>"),
        ("<div class=\"exp-card__body\"><h3>Casa Museo</h3><p>Online buchen: storie walser da raccontare ai più piccoli.</p></div>",
         "<div class=\"exp-card__body\"><h3>Hausmuseum</h3><p>Online buchen: Walser-Geschichten für die Kleinen.</p></div>"),
        ("alt=\"Familien che cercano oro al torrente con Monte Rosa\"",
         "alt=\"Familien beim Goldwaschen am Bach mit Monte Rosa\""),
        ("alt=\"Visita Walser-Hausmuseum per famiglie\"",
         "alt=\"Besuch Walser-Hausmuseum für Familien\""),
        ("<div class=\"exp-card__body\"><h3>Alla ricerca dell’oro</h3><p>Un’avventura che resta impressa nella memoria.</p></div>",
         "<div class=\"exp-card__body\"><h3>Goldwaschen</h3><p>Ein Abenteuer, das in Erinnerung bleibt.</p></div>"),
        ("<h2 class=\"reveal\">Häufig gestellte Fragen per le famiglie</h2>",
         "<h2 class=\"reveal\">Häufig gestellte Fragen für Familien</h2>"),
        ("<p class=\"faq-a\">Sì: percorsi facili, villaggio accogliente ed esperienze guidate. Ideale tra le <strong>montagne per famiglie</strong> del Monte Rosa, einschließlich per gite von Mailand, dal Lago Maggiore, Varese e Novara.</p>",
         "<p class=\"faq-a\">Ja: leichte Wege, einladendes Dorf und geführte Erlebnisse. Ideal unter den <strong>Familienbergen</strong> des Monte Rosa, auch für Ausflüge ab Mailand, Lago Maggiore, Varese und Novara.</p>"),
        ("<p class=\"faq-a\">Natura e gioco, <a href=\"casa-museo-walser.html\">Walser-Hausmuseum</a>, <a href=\"miniera-oro.html\">Goldmine</a> (einschließlich con passeggino), ricerca dell’oro e altre attività. Siehe <a href=\"esperienze.html\">Erlebnisse</a>.</p>",
         "<p class=\"faq-a\">Natur und Spiel, <a href=\"casa-museo-walser.html\">Walser-Hausmuseum</a>, <a href=\"miniera-oro.html\">Goldmine</a> (auch mit Kinderwagen), Goldwaschen und andere Aktivitäten. Siehe <a href=\"esperienze.html\">Erlebnisse</a>.</p>"),
        ("<summary>Come organizzare un weekend in montagna con i bambini?</summary>",
         "<summary>Wie organisiert man ein Bergwochenende mit Kindern?</summary>"),
        ("<p class=\"faq-a\">Alloggio a Macugnaga, una o due esperienze prenotate online e passeggiate in paese. Guida pratica su <a href=\"weekend.html\">Wochenende</a>.</p>",
         "<p class=\"faq-a\">Unterkunft in Macugnaga, ein oder zwei online gebuchte Erlebnisse und Dorfspaziergänge. Praktischer Leitfaden auf <a href=\"weekend.html\">Wochenende</a>.</p>"),
    ],
    "fr/casa-museo-walser.html": [
        ('<meta name="keywords" content="Maison-musée Walser, Macugnaga, visita museo Borca, prenota museo Walser, storia Walser Monte Rosa, Alts Walserhüüs">',
         '<meta name="keywords" content="Maison-musée Walser, Macugnaga, visite musée Borca, réserver musée Walser, histoire Walser Monte Rosa, Alts Walserhüüs">'),
        ("<div><dt>Contexte</dt><dd>Casa parrocchiale del XVII secolo (Alts Walserhüüs Van Zer Burfuggu)</dd></div>",
         "<div><dt>Contexte</dt><dd>Maison paroissiale du XVIIe siècle (Alts Walserhüüs Van Zer Burfuggu)</dd></div>"),
        ("<div><dt>Pour qui</dt><dd>Familles, scuole, appassionati di storia alpina</dd></div>",
         "<div><dt>Pour qui</dt><dd>Familles, écoles, passionnés d’histoire alpine</dd></div>"),
        ("<dd>Frazione Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</dd>",
         "<dd>Hameau de Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</dd>"),
        ("<span>Frazione Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</span>",
         "<span>Hameau de Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</span>"),
    ],
    "de/casa-museo-walser.html": [
        ('<meta name="keywords" content="Walser-Hausmuseum, Macugnaga, visita museo Borca, prenota museo Walser, storia Walser Monte Rosa, Alts Walserhüüs">',
         '<meta name="keywords" content="Walser-Hausmuseum, Macugnaga, Museumsbesuch Borca, Walser-Museum buchen, Walser-Geschichte Monte Rosa, Alts Walserhüüs">'),
        ("<div><dt>Kontext</dt><dd>Casa parrocchiale del XVII secolo (Alts Walserhüüs Van Zer Burfuggu)</dd></div>",
         "<div><dt>Kontext</dt><dd>Pfarrhaus aus dem 17. Jahrhundert (Alts Walserhüüs Van Zer Burfuggu)</dd></div>"),
        ("<div><dt>Für wen</dt><dd>Familien, scuole, appassionati di storia alpina</dd></div>",
         "<div><dt>Für wen</dt><dd>Familien, Schulen, Interessierte an alpiner Geschichte</dd></div>"),
        ("<dd>Frazione Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</dd>",
         "<dd>Weiler Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</dd>"),
        ("<span>Frazione Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</span>",
         "<span>Weiler Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</span>"),
    ],
    "en/casa-museo-walser.html": [
        ("<dd>Frazione Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</dd>",
         "<dd>Borca hamlet, Macugnaga (VB) — Anzasca Valley, Monte Rosa</dd>"),
        ("<span>Frazione Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</span>",
         "<span>Borca hamlet, Macugnaga (VB) — Anzasca Valley, Monte Rosa</span>"),
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
                print(f"MISS {rel}: {old[:60]!r}")
        path.write_text(text, encoding="utf-8")
        print(f"{rel}: {n} applied")


if __name__ == "__main__":
    main()
