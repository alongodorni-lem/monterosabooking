# -*- coding: utf-8 -*-
"""Replace FAQ visible list + FAQPage JSON-LD for en/fr/de with full translations."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FAQ_VISIBLE = {
    "en": r'''        <div class="faq-list">
          <details class="faq-item reveal">
            <summary>How do I book an experience?</summary>
            <p class="faq-a">Use the date search bar at the top of every page or go to <a href="esperienze.html">Experiences</a>, choose the activity and complete payment. You will immediately receive a confirmation email with information and guide contacts.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Which payment methods are accepted?</summary>
            <p class="faq-a">Secure payment online with credit card and PayPal.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is Macugnaga suitable as a mountain destination with children?</summary>
            <p class="faq-a">Yes: it is among the most accessible <strong>family mountains</strong> of Monte Rosa. See <a href="famiglie.html">Families</a> and the activity sheets on the booking portal.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is it a mountain destination for couples and groups of friends?</summary>
            <p class="faq-a">Yes: silence, Monte Rosa views and nature experiences for a romantic weekend or a getaway with friends. See <a href="coppie.html">Couples</a> and <a href="weekend.html">Weekend</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is Macugnaga ideal for senior travellers?</summary>
            <p class="faq-a">Yes: soft pace, accessible trails, woodland wellness and cultural visits. Learn more on <a href="senior.html">Seniors</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Are there hikes and walks in Macugnaga?</summary>
            <p class="faq-a">From the Dorf to the woods and trails under Monte Rosa: soft walks and easy hikes. Book outdoor experiences on <a href="esperienze.html">Experiences</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is Macugnaga still real mountain country, with characterful places and historic chalets?</summary>
            <p class="faq-a">Yes: traditional architecture, historic chalets, fine landscape and Monte Rosa panoramas. Learn more on <a href="scopri-macugnaga.html">Macugnaga</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is Macugnaga real mountains, close to Milan, Novara, Varese and the cities of the plain?</summary>
            <p class="faq-a">Yes: about 2 h from Milan, 1.5 h from Novara and Varese; also Lake Maggiore, Turin, the Po Plain and Switzerland. Details on <a href="fuga-citta.html">City escape</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Staying in a hotel or campsite on Lake Maggiore, Lake Orta or Lake Mergozzo and looking for a mountain destination?</summary>
            <p class="faq-a">Yes: Macugnaga / Monterosa is a natural mountain destination if you stay on <strong>Lake Maggiore</strong>, on <strong>Lake Orta</strong> or on <strong>Lake Mergozzo</strong>. From the lake you can plan a day at the foot of Monte Rosa — village, trails, Walser House, mine and, when open, lifts — and <a href="esperienze.html">book experiences online</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>What mountain weekend ideas do you offer?</summary>
            <p class="faq-a">Overnight stay, local cuisine, nature experiences, Walser House and gold mine. Guide on <a href="weekend.html">Weekend Macugnaga Monte Rosa</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>What nature experiences are available?</summary>
            <p class="faq-a">Walks, forest bathing, soft hikes and woodland wellness — real mountains, without technical mountaineering. <a href="esperienze.html">Book online</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>What is the best season?</summary>
            <p class="faq-a">All of them: cool summer and wellness, colourful autumn, magical winter. Check the booking calendar for availability.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Where can I stay?</summary>
            <p class="faq-a">Hotels, B&amp;Bs and holiday homes on the <a href="https://macugnaga-monterosa.it/contenuti/306635/dove-dormire" target="_blank" rel="noopener">Macugnaga-Monterosa · Where to stay</a> portal. This booking portal focuses on experiences.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Can I take the chairlift or cableway?</summary>
            <p class="faq-a">Yes, when the lifts are running: Belvedere/Burki chairlifts and the cableway toward Alpe Bill and Passo Moro (~2870&nbsp;m). Details and openings on <a href="funivia-seggiovia.html">Cableway and chairlift</a>; live status on <a href="https://macugnagamonterosaski.com/impianti/" target="_blank" rel="noopener">macugnagamonterosaski.com</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Who runs the experiences?</summary>
            <p class="faq-a">Authorised local operators. Online booking system developed by <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> for Unione Montana Valli dell’Ossola. See <a href="come-funziona.html">How it works</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Who is responsible for the booked activities?</summary>
            <p class="faq-a">Information, prices and availability on the booking portal are provided by the experience operators. After booking online you will receive the organisers’ direct contacts for any further information. <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> is in no way responsible for the management of the activities. See also <a href="credits.html">Credits</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is this site for technical mountaineering?</summary>
            <p class="faq-a">No: the booking portal is dedicated to accessible experiences for everyone. Dedicated mountaineering portals exist elsewhere.</p>
          </details>
          <details class="faq-item reveal">
            <summary>How can I contact you?</summary>
            <p class="faq-a"><a href="mailto:macugnagabooking@gmail.com">macugnagabooking@gmail.com</a> — after booking you will also receive the guides’ direct contacts.</p>
          </details>
          <details class="faq-item reveal">
            <summary>What else is there to visit beyond the activities?</summary>
            <p class="faq-a">Walser House Museum, <a href="miniera-oro.html">gold mine</a>, village events, refuges and lifts. Learn more on <a href="scopri-macugnaga.html">Macugnaga</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Is it suitable for longer stays or remote work?</summary>
            <p class="faq-a">Yes: weekends, weeks and longer stays in a quiet setting near the Po Plain and Switzerland. See <a href="fuga-citta.html">City escape</a>.</p>
          </details>
        </div>''',
    "fr": r'''        <div class="faq-list">
          <details class="faq-item reveal">
            <summary>Comment réserver une expérience ?</summary>
            <p class="faq-a">Utilisez la barre de recherche par dates en haut de chaque page ou allez sur <a href="esperienze.html">Expériences</a>, choisissez l’activité et finalisez le paiement. Vous recevrez immédiatement un e-mail de confirmation avec les informations et les contacts des guides.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Quels moyens de paiement sont acceptés ?</summary>
            <p class="faq-a">Paiement sécurisé en ligne par carte de crédit et PayPal.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Macugnaga convient-elle comme montagne avec les enfants ?</summary>
            <p class="faq-a">Oui : parmi les <strong>montagnes pour familles</strong> les plus accessibles du Monte Rosa. Voir <a href="famiglie.html">Familles</a> et les fiches d’activités du portail de réservation.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Est-ce une destination de montagne pour couples et groupes d’amis ?</summary>
            <p class="faq-a">Oui : silence, panoramas sur le Monte Rosa et expériences nature pour un week-end romantique ou une escapade entre amis. Voir <a href="coppie.html">Couples</a> et <a href="weekend.html">Week-end</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Macugnaga est-elle idéale pour les touristes seniors ?</summary>
            <p class="faq-a">Oui : rythme doux, sentiers accessibles, bien-être en forêt et visites culturelles. En savoir plus sur <a href="senior.html">Seniors</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Y a-t-il des randonnées et promenades à Macugnaga ?</summary>
            <p class="faq-a">Du Dorf aux bois et aux sentiers sous le Monte Rosa : promenades et randonnées douces. Réservez le plein air sur <a href="esperienze.html">Expériences</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Macugnaga est-elle encore une vraie montagne, avec des lieux typiques et d’anciens chalets ?</summary>
            <p class="faq-a">Oui : architecture traditionnelle, anciens chalets, beau paysage et panoramas sur le Monte Rosa. En savoir plus sur <a href="scopri-macugnaga.html">Macugnaga</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Est-ce la vraie montagne, près de Milan, Novara, Varese et des villes de la plaine ?</summary>
            <p class="faq-a">Oui : environ 2 h depuis Milan, 1,5 h depuis Novara et Varese ; aussi Lac Majeur, Turin, plaine du Pô et Suisse. Détails sur <a href="fuga-citta.html">Échapper à la ville</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Vous séjournez à l’hôtel ou au camping sur le Lac Majeur, le Lac d’Orta ou le Lac de Mergozzo et cherchez une destination de montagne ?</summary>
            <p class="faq-a">Oui : Macugnaga / Monterosa est une destination de montagne naturelle si vous séjournez sur le <strong>Lac Majeur</strong>, sur le <strong>Lac d’Orta</strong> ou sur le <strong>Lac de Mergozzo</strong>. Depuis le lac, organisez une journée au pied du Monte Rosa — village, sentiers, Maison Walser, mine et, quand elles sont ouvertes, remontées — et <a href="esperienze.html">réservez les expériences en ligne</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Quelles idées de week-end en montagne proposez-vous ?</summary>
            <p class="faq-a">Hébergement, cuisine locale, expériences nature, Maison Walser et mine d’or. Guide sur <a href="weekend.html">Week-end Macugnaga Monte Rosa</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Quelles expériences nature trouve-t-on ?</summary>
            <p class="faq-a">Promenades, forest bathing, randonnées douces et bien-être en forêt — vraie montagne, sans alpinisme technique. <a href="esperienze.html">Réserver en ligne</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Quelle est la meilleure saison ?</summary>
            <p class="faq-a">Toutes : été frais et bien-être, automne coloré, hiver magique. Consultez le calendrier de réservation pour les disponibilités.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Où puis-je dormir ?</summary>
            <p class="faq-a">Hôtels, B&amp;B et maisons de vacances sur le portail <a href="https://macugnaga-monterosa.it/contenuti/306635/dove-dormire" target="_blank" rel="noopener">Macugnaga-Monterosa · Où dormir</a>. Ce portail de réservation se consacre aux expériences.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Puis-je monter en télésiège ou téléphérique ?</summary>
            <p class="faq-a">Oui, lorsque les remontées sont en service : télésièges Belvedere/Burki et téléphérique vers Alpe Bill et Passo Moro (~2870&nbsp;m). Détails et ouvertures sur <a href="funivia-seggiovia.html">Téléphérique et télésiège</a> ; état en direct sur <a href="https://macugnagamonterosaski.com/impianti/" target="_blank" rel="noopener">macugnagamonterosaski.com</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Qui gère les expériences ?</summary>
            <p class="faq-a">Opérateurs locaux autorisés. Système de réservation en ligne développé par <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> pour Unione Montana Valli dell’Ossola. Voir <a href="come-funziona.html">Comment ça marche</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Qui est responsable des activités réservées ?</summary>
            <p class="faq-a">Les informations, prix et disponibilités du portail de réservation sont indiqués par les organisateurs des expériences. Après une réservation en ligne, vous recevrez leurs contacts directs pour toute information complémentaire. <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> n’est en aucun cas responsable de la gestion des activités. Voir aussi <a href="credits.html">Crédits</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Ce site est-il destiné à l’alpinisme technique ?</summary>
            <p class="faq-a">Non : le portail de réservation est dédié aux expériences accessibles à tous. Des portails spécialisés existent pour l’alpinisme technique.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Comment vous contacter ?</summary>
            <p class="faq-a"><a href="mailto:macugnagabooking@gmail.com">macugnagabooking@gmail.com</a> — après la réservation vous recevrez aussi les contacts directs des guides.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Que visiter en plus des activités ?</summary>
            <p class="faq-a">Maison-musée Walser, <a href="miniera-oro.html">mine d’or</a>, événements du village, refuges et remontées. En savoir plus sur <a href="scopri-macugnaga.html">Macugnaga</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Convient-elle aux longs séjours ou au télétravail ?</summary>
            <p class="faq-a">Oui : week-ends, semaines et longs séjours dans un cadre calme près de la plaine du Pô et de la Suisse. Voir <a href="fuga-citta.html">Échapper à la ville</a>.</p>
          </details>
        </div>''',
    "de": r'''        <div class="faq-list">
          <details class="faq-item reveal">
            <summary>Wie buche ich ein Erlebnis?</summary>
            <p class="faq-a">Nutzen Sie die Datumssuche oben auf jeder Seite oder gehen Sie zu <a href="esperienze.html">Erlebnisse</a>, wählen Sie die Aktivität und schließen Sie die Zahlung ab. Sie erhalten sofort eine Bestätigungs-E-Mail mit Infos und Kontakten der Guides.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Welche Zahlungsmethoden werden akzeptiert?</summary>
            <p class="faq-a">Sichere Online-Zahlung mit Kreditkarte und PayPal.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Eignet sich Macugnaga als Bergziel mit Kindern?</summary>
            <p class="faq-a">Ja: unter den zugänglichsten <strong>Familienbergen</strong> des Monte Rosa. Siehe <a href="famiglie.html">Familien</a> und die Aktivitätsseiten im Buchungsportal.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Ist es ein Bergziel für Paare und Freundesgruppen?</summary>
            <p class="faq-a">Ja: Stille, Monte-Rosa-Panoramen und Naturerlebnisse für ein romantisches Wochenende oder einen Ausflug mit Freunden. Siehe <a href="coppie.html">Paare</a> und <a href="weekend.html">Wochenende</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Ist Macugnaga ideal für Senioren?</summary>
            <p class="faq-a">Ja: sanftes Tempo, zugängliche Wege, Wald-Wellness und Kulturbesuche. Mehr erfahren auf <a href="senior.html">Senioren</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Gibt es Wanderungen und Spaziergänge in Macugnaga?</summary>
            <p class="faq-a">Vom Dorf zu Wäldern und Wegen unter dem Monte Rosa: Spaziergänge und leichte Wanderungen. Outdoor auf <a href="esperienze.html">Erlebnisse</a> buchen.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Ist Macugnaga noch echte Bergwelt, mit charakteristischen Orten und alten Chalets?</summary>
            <p class="faq-a">Ja: traditionelle Architektur, historische Chalets, schöne Landschaft und Monte-Rosa-Panoramen. Mehr erfahren auf <a href="scopri-macugnaga.html">Macugnaga</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Sind es echte Berge, nahe Mailand, Novara, Varese und den Städten der Ebene?</summary>
            <p class="faq-a">Ja: etwa 2 h von Mailand, 1,5 h von Novara und Varese; auch Lago Maggiore, Turin, Po-Ebene und Schweiz. Details auf <a href="fuga-citta.html">Stadtflucht</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Sie übernachten in Hotel oder Camping am Lago Maggiore, Ortasee oder Mergozzo-See und suchen ein Bergziel?</summary>
            <p class="faq-a">Ja: Macugnaga / Monterosa ist ein natürliches Bergziel, wenn Sie am <strong>Lago Maggiore</strong>, am <strong>Ortasee</strong> oder am <strong>Mergozzo-See</strong> übernachten. Vom See aus planen Sie einen Tag am Fuße des Monte Rosa — Dorf, Wege, Walser-Haus, Mine und, wenn geöffnet, Bahnen — und <a href="esperienze.html">buchen Erlebnisse online</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Welche Bergwochenend-Ideen bieten Sie?</summary>
            <p class="faq-a">Übernachtung, lokale Küche, Naturerlebnisse, Walser-Haus und Goldmine. Guide auf <a href="weekend.html">Wochenende Macugnaga Monte Rosa</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Welche Naturerlebnisse gibt es?</summary>
            <p class="faq-a">Spaziergänge, Forest Bathing, sanfte Wanderungen und Wald-Wellness — echte Berge, ohne technischen Alpinismus. <a href="esperienze.html">Online buchen</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Welche Jahreszeit ist am besten?</summary>
            <p class="faq-a">Alle: kühler Sommer und Wellness, bunter Herbst, magischer Winter. Prüfen Sie den Buchungskalender für Verfügbarkeiten.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Wo kann ich übernachten?</summary>
            <p class="faq-a">Hotels, B&amp;Bs und Ferienhäuser auf dem Portal <a href="https://macugnaga-monterosa.it/contenuti/306635/dove-dormire" target="_blank" rel="noopener">Macugnaga-Monterosa · Übernachten</a>. Dieses Buchungsportal widmet sich den Erlebnissen.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Kann ich Sessellift oder Seilbahn nutzen?</summary>
            <p class="faq-a">Ja, wenn die Bahnen in Betrieb sind: Sessellifte Belvedere/Burki und Seilbahn Richtung Alpe Bill und Passo Moro (~2870&nbsp;m). Details und Öffnungen auf <a href="funivia-seggiovia.html">Seilbahn und Sessellift</a>; Live-Status auf <a href="https://macugnagamonterosaski.com/impianti/" target="_blank" rel="noopener">macugnagamonterosaski.com</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Wer führt die Erlebnisse durch?</summary>
            <p class="faq-a">Autorisierte lokale Anbieter. Online-Buchungssystem entwickelt von <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> für Unione Montana Valli dell’Ossola. Siehe <a href="come-funziona.html">So funktioniert’s</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Wer ist für die gebuchten Aktivitäten verantwortlich?</summary>
            <p class="faq-a">Informationen, Preise und Verfügbarkeiten im Buchungsportal werden von den Anbietern der Erlebnisse angegeben. Nach der Online-Buchung erhalten Sie die direkten Kontakte der Organisatoren für weitere Auskünfte. <a href="https://www.raccontidigitali.it" target="_blank" rel="noopener">Lem s.r.l.</a> ist in keiner Weise für die Durchführung der Aktivitäten verantwortlich. Siehe auch <a href="credits.html">Credits</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Ist diese Website für technischen Alpinismus?</summary>
            <p class="faq-a">Nein: das Buchungsportal ist für zugängliche Erlebnisse für alle gedacht. Für technischen Alpinismus gibt es spezielle Portale.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Wie kann ich Sie kontaktieren?</summary>
            <p class="faq-a"><a href="mailto:macugnagabooking@gmail.com">macugnagabooking@gmail.com</a> — nach der Buchung erhalten Sie auch die direkten Kontakte der Guides.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Was gibt es außer den Aktivitäten zu besuchen?</summary>
            <p class="faq-a">Walser-Hausmuseum, <a href="miniera-oro.html">Goldmine</a>, Dorfveranstaltungen, Hütten und Bahnen. Mehr erfahren auf <a href="scopri-macugnaga.html">Macugnaga</a>.</p>
          </details>
          <details class="faq-item reveal">
            <summary>Eignet es sich für längere Aufenthalte oder Remote-Arbeit?</summary>
            <p class="faq-a">Ja: Wochenenden, Wochen und längere Aufenthalte in ruhiger Umgebung nahe der Po-Ebene und der Schweiz. Siehe <a href="fuga-citta.html">Stadtflucht</a>.</p>
          </details>
        </div>''',
}

FAQ_JSON = {
    "en": '''          {
            "@type": "Question",
            "name": "How do I book an experience?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Use the date search bar at the top of every page or go to Experiences, choose the activity, complete your details and pay online. You will immediately receive a confirmation email with information and guide contacts."
            }
          },
          {
            "@type": "Question",
            "name": "Which payment methods are accepted?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Payment is secure online with credit card and PayPal."
            }
          },
          {
            "@type": "Question",
            "name": "Is Macugnaga suitable as a mountain destination with children?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: it is among the most accessible family mountains of Monte Rosa. Many offers are designed for easy routes and mountain day trips with children. See the Families page and the activity sheets on the booking portal."
            }
          },
          {
            "@type": "Question",
            "name": "Is Macugnaga a mountain destination for couples and groups of friends?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: mountain silence, Monte Rosa views and nature experiences make it ideal for a romantic couple’s weekend or a getaway with friends. See the Couples and Weekend pages on the booking portal."
            }
          },
          {
            "@type": "Question",
            "name": "Is Macugnaga ideal for senior travellers?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. Soft pace, accessible trails, woodland wellness and cultural visits (Walser House Museum, gold mine) suit those seeking real mountains without extreme effort. See the Seniors page."
            }
          },
          {
            "@type": "Question",
            "name": "Are there hikes and walks in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: from the Dorf to the woods and trails under Monte Rosa you find soft walks and hikes. Book outdoor experiences on the Experiences page of the booking portal."
            }
          },
          {
            "@type": "Question",
            "name": "Is Macugnaga still real mountain country, with characterful places and historic chalets?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. The village has preserved traditional architecture, historic chalets, fine landscape and Monte Rosa panoramas: an authentic alpine village to experience from the centre and the trails. Learn more about Macugnaga."
            }
          },
          {
            "@type": "Question",
            "name": "Is Macugnaga real mountains, close to Milan, Novara, Varese and the cities of the plain?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. Macugnaga is in the Anzasca Valley (VB), Piedmont, at the foot of Monte Rosa. Typical times: about 2 hours from Milan, about 1.5 hours from Novara and Varese; also reachable from Lake Maggiore, Turin, the Po Plain and Switzerland (Valais and Ticino)."
            }
          },
          {
            "@type": "Question",
            "name": "Staying in a hotel or campsite on Lake Maggiore, Lake Orta or Lake Mergozzo and looking for a mountain destination?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: Macugnaga / Monterosa is a natural mountain destination if you stay on Lake Maggiore, on Lake Orta or on Lake Mergozzo. From the lake you can organise a day at the foot of Monte Rosa — village, trails, Walser House, gold mine and, when open, lifts — and book experiences online on the Experiences page of the booking portal."
            }
          },
          {
            "@type": "Question",
            "name": "What mountain weekend ideas do you offer in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A Macugnaga Monte Rosa weekend can include overnight stay, local cuisine, nature experiences, Walser House Museum, gold mine and, when open, ski lifts. See the Weekend page of the booking portal."
            }
          },
          {
            "@type": "Question",
            "name": "What kind of nature experiences are available?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Walks, forest bathing, soft hikes, woodland wellness and outdoor proposals guided by local operators. Ideal for those seeking real mountains without technical mountaineering."
            }
          },
          {
            "@type": "Question",
            "name": "What is the best season?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Macugnaga is an alpine village for all seasons: cool summer and wellness, autumn colours and silence, winter snow and village atmosphere. Available experiences vary: check the booking calendar."
            }
          },
          {
            "@type": "Question",
            "name": "Where can I stay?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Hotels, B&Bs and holiday homes are listed on the official Macugnaga-Monterosa portal in the Where to stay section. This booking portal focuses on experiences and activities."
            }
          },
          {
            "@type": "Question",
            "name": "Can I take the chairlift or cableway?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, when the lifts are running: Belvedere/Burki chairlifts and the cableway toward Alpe Bill and Passo Moro (about 2870 m). Details on the Cableway and chairlift page of the portal; live status and tickets on macugnagamonterosaski.com."
            }
          },
          {
            "@type": "Question",
            "name": "Who runs the experiences?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Authorised and qualified local operators. The online booking system is developed by Lem s.r.l. (https://www.raccontidigitali.it) for Unione Montana Valli dell'Ossola and local operators."
            }
          },
          {
            "@type": "Question",
            "name": "Who is responsible for the booked activities?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Information, prices and availability on the booking portal are provided by the experience operators. After booking online you will receive the organisers’ direct contacts for any further information. Lem s.r.l. is in no way responsible for the management of the activities."
            }
          },
          {
            "@type": "Question",
            "name": "Is this site also suitable for expert mountaineers?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The booking portal is dedicated to accessible experiences for everyone (families, adults, young people, groups). Dedicated portals exist for technical mountaineering; here we value the mountains lived from the village, with ease and safety."
            }
          },
          {
            "@type": "Question",
            "name": "How can I contact you?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Write to macugnagabooking@gmail.com. After booking you will also receive the guides’ direct contacts in the confirmation email."
            }
          },
          {
            "@type": "Question",
            "name": "What else is there to visit beyond the booking portal activities?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Walser House Museum, underground gold mine (the first visitable in Italy), village centre, local events, alpine refuges and the ski lifts."
            }
          },
          {
            "@type": "Question",
            "name": "Is Macugnaga suitable for a longer stay or remote work?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: beyond the weekend, many choose restorative weeks or longer stays for peace, study and work in an alpine setting near the cities of the Po Plain and Switzerland."
            }
          }''',
    "fr": '''          {
            "@type": "Question",
            "name": "Comment réserver une expérience ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Utilisez la barre de recherche par dates en haut de chaque page ou allez sur Expériences, choisissez l’activité, complétez vos données et payez en ligne. Vous recevrez immédiatement un e-mail de confirmation avec les informations et les contacts des guides."
            }
          },
          {
            "@type": "Question",
            "name": "Quels moyens de paiement sont acceptés ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Le paiement est sécurisé en ligne par carte de crédit et PayPal."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga convient-elle comme montagne avec les enfants ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : parmi les montagnes pour familles les plus accessibles du Monte Rosa. Beaucoup d’offres sont pensées pour des parcours faciles et des sorties en montagne avec enfants. Consultez la page Familles et les fiches d’activités du portail de réservation."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga est-elle une destination de montagne pour couples et groupes d’amis ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : silences de montagne, panoramas sur le Monte Rosa et expériences nature en font une destination idéale pour un week-end romantique ou une escapade entre amis. Voir les pages Couples et Week-end du portail de réservation."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga est-elle idéale pour les touristes seniors ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui. Rythme doux, sentiers accessibles, bien-être en forêt et visites culturelles (Maison-musée Walser, mine d’or) conviennent à qui cherche une vraie montagne sans effort extrême. Découvrez la page Seniors."
            }
          },
          {
            "@type": "Question",
            "name": "Y a-t-il des randonnées et promenades à Macugnaga ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : du Dorf aux bois et aux sentiers sous le Monte Rosa vous trouvez promenades et randonnées douces. Réservez des expériences outdoor sur la page Expériences du portail de réservation."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga est-elle encore une vraie montagne, avec des lieux typiques et d’anciens chalets ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui. Le village a préservé architecture traditionnelle, anciens chalets, beau paysage et panoramas sur le Monte Rosa : un village alpin authentique à vivre depuis le centre et les sentiers. En savoir plus sur Macugnaga."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga est-elle la vraie montagne, près de Milan, Novara, Varese et des villes de la plaine ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui. Macugnaga se trouve dans le Val Anzasca (VB), Piémont, au pied du Monte Rosa. Temps typiques : environ 2 heures depuis Milan, environ 1,5 heure depuis Novara et Varese ; également accessible depuis le Lac Majeur, Turin, la plaine du Pô et la Suisse (Valais et Tessin)."
            }
          },
          {
            "@type": "Question",
            "name": "Vous séjournez à l’hôtel ou au camping sur le Lac Majeur, le Lac d’Orta ou le Lac de Mergozzo et cherchez une destination de montagne ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : Macugnaga / Monterosa est une destination de montagne naturelle si vous séjournez sur le Lac Majeur, sur le Lac d’Orta ou sur le Lac de Mergozzo. Depuis le lac, organisez une journée au pied du Monte Rosa — village, sentiers, Maison Walser, mine d’or et, quand elles sont ouvertes, remontées — et réservez les expériences en ligne sur la page Expériences du portail."
            }
          },
          {
            "@type": "Question",
            "name": "Quelles idées de week-end en montagne proposez-vous à Macugnaga ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Un week-end Macugnaga Monte Rosa peut inclure hébergement, cuisine locale, expériences nature, Maison-musée Walser, mine d’or et, si ouvertes, remontées mécaniques. Voir la page Week-end du portail de réservation."
            }
          },
          {
            "@type": "Question",
            "name": "Quel type d’expériences nature trouve-t-on ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Promenades, forest bathing, randonnées douces, bien-être en forêt et propositions outdoor guidées par des opérateurs locaux. Idéales pour qui cherche la vraie montagne sans alpinisme technique."
            }
          },
          {
            "@type": "Question",
            "name": "Quelle est la meilleure saison ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Macugnaga est un village alpin pour toutes les saisons : été frais et bien-être, automne avec couleurs et silences, hiver avec neige et atmosphère de village. Les expériences disponibles varient : consultez le calendrier de réservation."
            }
          },
          {
            "@type": "Question",
            "name": "Où puis-je dormir ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Hôtels, B&B et maisons de vacances sont listés sur le portail officiel Macugnaga-Monterosa dans la section Où dormir. Ce portail de réservation se consacre aux expériences et activités."
            }
          },
          {
            "@type": "Question",
            "name": "Puis-je monter en télésiège ou téléphérique ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui, lorsque les remontées sont en service : télésièges Belvedere/Burki et téléphérique vers Alpe Bill et Passo Moro (environ 2870 m). Détails sur la page Téléphérique et télésiège du portail ; état en direct et billets sur macugnagamonterosaski.com."
            }
          },
          {
            "@type": "Question",
            "name": "Qui gère les expériences ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Opérateurs locaux autorisés et qualifiés. Le système de réservation en ligne est développé par Lem s.r.l. (https://www.raccontidigitali.it) pour Unione Montana Valli dell'Ossola et les opérateurs du territoire."
            }
          },
          {
            "@type": "Question",
            "name": "Qui est responsable des activités réservées ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Les informations, prix et disponibilités du portail de réservation sont indiqués par les organisateurs des expériences. Après une réservation en ligne, vous recevrez leurs contacts directs pour toute information complémentaire. Lem s.r.l. n’est en aucun cas responsable de la gestion des activités."
            }
          },
          {
            "@type": "Question",
            "name": "Ce site convient-il aussi aux alpinistes experts ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Le portail de réservation est dédié aux expériences accessibles à tous (familles, adultes, jeunes, groupes). Des portails spécialisés existent pour l’alpinisme technique ; ici nous valorisons la montagne vécue depuis le village, avec facilité et sécurité."
            }
          },
          {
            "@type": "Question",
            "name": "Comment vous contacter ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Écrivez à macugnagabooking@gmail.com. Après la réservation vous recevrez aussi les contacts directs des guides dans l’e-mail de confirmation."
            }
          },
          {
            "@type": "Question",
            "name": "Que visiter en plus des activités du portail de réservation ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Maison-musée Walser, mine d’or souterraine (première visitable en Italie), centre du village, événements locaux, refuges alpins et les remontées mécaniques."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga convient-elle à un long séjour ou au télétravail ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : au-delà du week-end, beaucoup choisissent des semaines régénérantes ou de longs séjours pour la tranquillité, l’étude et le travail dans un cadre alpin près des villes de la plaine du Pô et de la Suisse."
            }
          }''',
    "de": '''          {
            "@type": "Question",
            "name": "Wie buche ich ein Erlebnis?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Nutzen Sie die Datumssuche oben auf jeder Seite oder gehen Sie zu Erlebnisse, wählen Sie die Aktivität, ergänzen Sie Ihre Daten und zahlen Sie online. Sie erhalten sofort eine Bestätigungs-E-Mail mit Informationen und Kontakten der Guides."
            }
          },
          {
            "@type": "Question",
            "name": "Welche Zahlungsmethoden werden akzeptiert?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Die Zahlung ist sicher online mit Kreditkarte und PayPal."
            }
          },
          {
            "@type": "Question",
            "name": "Eignet sich Macugnaga als Bergziel mit Kindern?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: unter den zugänglichsten Familienbergen des Monte Rosa. Viele Angebote sind für leichte Wege und Bergausflüge mit Kindern gedacht. Siehe die Seite Familien und die Aktivitätsseiten im Buchungsportal."
            }
          },
          {
            "@type": "Question",
            "name": "Ist Macugnaga ein Bergziel für Paare und Freundesgruppen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: Bergstille, Monte-Rosa-Panoramen und Naturerlebnisse machen es ideal für ein romantisches Wochenende oder einen Ausflug mit Freunden. Siehe die Seiten Paare und Wochenende im Buchungsportal."
            }
          },
          {
            "@type": "Question",
            "name": "Ist Macugnaga ideal für Senioren?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja. Sanftes Tempo, zugängliche Wege, Wald-Wellness und Kulturbesuche (Walser-Hausmuseum, Goldmine) passen zu allen, die echte Berge ohne extreme Anstrengung suchen. Entdecken Sie die Seite Senioren."
            }
          },
          {
            "@type": "Question",
            "name": "Gibt es Wanderungen und Spaziergänge in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: vom Dorf zu Wäldern und Wegen unter dem Monte Rosa finden Sie Spaziergänge und sanfte Wanderungen. Buchen Sie Outdoor-Erlebnisse auf der Seite Erlebnisse des Buchungsportals."
            }
          },
          {
            "@type": "Question",
            "name": "Ist Macugnaga noch echte Bergwelt, mit charakteristischen Orten und alten Chalets?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja. Das Dorf hat traditionelle Architektur, historische Chalets, schöne Landschaft und Monte-Rosa-Panoramen bewahrt: ein authentisches Alpendorf, erlebbar vom Zentrum und den Wegen. Mehr erfahren über Macugnaga."
            }
          },
          {
            "@type": "Question",
            "name": "Sind es echte Berge, nahe Mailand, Novara, Varese und den Städten der Ebene?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja. Macugnaga liegt im Anzasca-Tal (VB), Piemont, am Fuße des Monte Rosa. Typische Fahrzeiten: etwa 2 Stunden von Mailand, etwa 1,5 Stunden von Novara und Varese; auch erreichbar vom Lago Maggiore, Turin, der Po-Ebene und der Schweiz (Wallis und Tessin)."
            }
          },
          {
            "@type": "Question",
            "name": "Sie übernachten in Hotel oder Camping am Lago Maggiore, Ortasee oder Mergozzo-See und suchen ein Bergziel?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: Macugnaga / Monterosa ist ein natürliches Bergziel, wenn Sie am Lago Maggiore, am Ortasee oder am Mergozzo-See übernachten. Vom See aus können Sie einen Tag am Fuße des Monte Rosa organisieren — Dorf, Wege, Walser-Haus, Goldmine und, wenn geöffnet, Bahnen — und Erlebnisse online auf der Seite Erlebnisse des Portals buchen."
            }
          },
          {
            "@type": "Question",
            "name": "Welche Bergwochenend-Ideen bieten Sie in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ein Wochenende Macugnaga Monte Rosa kann Übernachtung, lokale Küche, Naturerlebnisse, Walser-Hausmuseum, Goldmine und, wenn geöffnet, Bergbahnen umfassen. Siehe die Seite Wochenende des Buchungsportals."
            }
          },
          {
            "@type": "Question",
            "name": "Welche Art von Naturerlebnissen gibt es?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Spaziergänge, Forest Bathing, sanfte Wanderungen, Wald-Wellness und Outdoor-Angebote mit lokalen Anbietern. Ideal für alle, die echte Berge ohne technischen Alpinismus suchen."
            }
          },
          {
            "@type": "Question",
            "name": "Welche Jahreszeit ist am besten?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Macugnaga ist ein Alpendorf für alle Jahreszeiten: kühler Sommer und Wellness, Herbst mit Farben und Stille, Winter mit Schnee und Dorfatmosphäre. Verfügbare Erlebnisse variieren: prüfen Sie den Buchungskalender."
            }
          },
          {
            "@type": "Question",
            "name": "Wo kann ich übernachten?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Hotels, B&Bs und Ferienhäuser sind auf dem offiziellen Portal Macugnaga-Monterosa im Bereich Übernachten gelistet. Dieses Buchungsportal widmet sich Erlebnissen und Aktivitäten."
            }
          },
          {
            "@type": "Question",
            "name": "Kann ich Sessellift oder Seilbahn nutzen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja, wenn die Bahnen in Betrieb sind: Sessellifte Belvedere/Burki und Seilbahn Richtung Alpe Bill und Passo Moro (etwa 2870 m). Details auf der Seite Seilbahn und Sessellift des Portals; Live-Status und Tickets auf macugnagamonterosaski.com."
            }
          },
          {
            "@type": "Question",
            "name": "Wer führt die Erlebnisse durch?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Autorisierte und qualifizierte lokale Anbieter. Das Online-Buchungssystem wird von Lem s.r.l. (https://www.raccontidigitali.it) für Unione Montana Valli dell'Ossola und lokale Anbieter entwickelt."
            }
          },
          {
            "@type": "Question",
            "name": "Wer ist für die gebuchten Aktivitäten verantwortlich?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Informationen, Preise und Verfügbarkeiten im Buchungsportal werden von den Anbietern der Erlebnisse angegeben. Nach der Online-Buchung erhalten Sie die direkten Kontakte der Organisatoren für weitere Auskünfte. Lem s.r.l. ist in keiner Weise für die Durchführung der Aktivitäten verantwortlich."
            }
          },
          {
            "@type": "Question",
            "name": "Ist diese Website auch für erfahrene Alpinisten geeignet?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Das Buchungsportal ist für zugängliche Erlebnisse für alle gedacht (Familien, Erwachsene, Jugendliche, Gruppen). Für technischen Alpinismus gibt es spezielle Portale; hier schätzen wir die Berge vom Dorf aus, mit Leichtigkeit und Sicherheit."
            }
          },
          {
            "@type": "Question",
            "name": "Wie kann ich Sie kontaktieren?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Schreiben Sie an macugnagabooking@gmail.com. Nach der Buchung erhalten Sie auch die direkten Kontakte der Guides in der Bestätigungs-E-Mail."
            }
          },
          {
            "@type": "Question",
            "name": "Was gibt es außer den Aktivitäten des Buchungsportals zu besuchen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Walser-Hausmuseum, unterirdische Goldmine (die erste besuchbare in Italien), Dorfzentrum, lokale Veranstaltungen, Alpenhütten und die Bergbahnen."
            }
          },
          {
            "@type": "Question",
            "name": "Eignet sich Macugnaga für einen längeren Aufenthalt oder Remote-Arbeit?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: neben dem Wochenende wählen viele erholsame Wochen oder längere Aufenthalte für Ruhe, Studium und Arbeit in alpiner Umgebung nahe den Städten der Po-Ebene und der Schweiz."
            }
          }''',
}

HERO = {
    "en": "Mountain day trips, families, couples, seniors, Macugnaga Monte Rosa weekends and arrivals from Milan, Lake Maggiore, Varese and Novara.",
    "fr": "Sorties en montagne, familles, couples, seniors, week-ends Macugnaga Monte Rosa et arrivée depuis Milan, le Lac Majeur, Varese et Novara.",
    "de": "Bergausflüge, Familien, Paare, Senioren, Wochenenden Macugnaga Monte Rosa und Anreise von Mailand, Lago Maggiore, Varese und Novara.",
}

ATTRACTION_DESC = {
    "en": "Real mountain destination at the foot of Monte Rosa, ideal for families, couples, seniors, hikes and weekends from the Po Plain, Lake Maggiore and Switzerland.",
    "fr": "Destination de vraie montagne au pied du Monte Rosa, idéale pour familles, couples, seniors, randonnées et week-ends depuis la plaine du Pô, le Lac Majeur et la Suisse.",
    "de": "Echtes Bergziel am Fuße des Monte Rosa, ideal für Familien, Paare, Senioren, Wanderungen und Wochenenden aus der Po-Ebene, vom Lago Maggiore und aus der Schweiz.",
}

AREA = {
    "en": '["Milan", "Varese", "Novara", "Lake Maggiore", "Lake Orta", "Lake Mergozzo", "Turin", "Po Plain", "Switzerland"]',
    "fr": '["Milan", "Varese", "Novara", "Lac Majeur", "Lac d\'Orta", "Lac de Mergozzo", "Turin", "Plaine du Pô", "Suisse"]',
    "de": '["Mailand", "Varese", "Novara", "Lago Maggiore", "Ortasee", "Mergozzo-See", "Turin", "Po-Ebene", "Schweiz"]',
}


def replace_faq_list(html: str, block: str) -> str:
    return re.sub(
        r'<div class="faq-list">.*?</div>\s*</div>\s*</section>',
        block + "\n      </div>\n    </section>",
        html,
        count=1,
        flags=re.S,
    )


def replace_main_entity(html: str, block: str) -> str:
    return re.sub(
        r'("@type":\s*"FAQPage",\s*"mainEntity":\s*\[)(.*?)(\]\s*\})',
        lambda m: m.group(1) + "\n" + block + "\n        " + m.group(3),
        html,
        count=1,
        flags=re.S,
    )


def fix_faq(lang: str) -> None:
    path = ROOT / lang / "faq.html"
    html = path.read_text(encoding="utf-8")
    html = replace_faq_list(html, FAQ_VISIBLE[lang])
    html = replace_main_entity(html, FAQ_JSON[lang])
    # Hero intro under h1
    html = re.sub(
        r'(<h1>[^<]+</h1>\s*<p>)(.*?)(</p>)',
        lambda m: m.group(1) + HERO[lang] + m.group(3),
        html,
        count=1,
    )
    # TouristAttraction description
    html = re.sub(
        r'("@type":\s*"TouristAttraction",\s*"name":\s*"Macugnaga Monte Rosa",\s*"description":\s*")(.*?)(")',
        lambda m: m.group(1) + ATTRACTION_DESC[lang].replace("\\", "\\\\") + m.group(3),
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'"areaServed":\s*\[[^\]]*\]',
        '"areaServed": ' + AREA[lang],
        html,
        count=1,
    )
    path.write_text(html, encoding="utf-8", newline="\n")
    print(f"Updated {path.relative_to(ROOT)}")


def main() -> None:
    for lang in ("en", "fr", "de"):
        fix_faq(lang)


if __name__ == "__main__":
    main()
