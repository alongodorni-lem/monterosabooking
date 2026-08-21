# -*- coding: utf-8 -*-
"""Funivia JSON-LD translations (EN/FR/DE)."""
from __future__ import annotations

FUNIVIA = {
"en": r'''<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "TouristAttraction",
        "name": "Macugnaga ski lifts — Belvedere and Monte Moro",
        "alternateName": ["Belvedere Burki chairlift", "Passo Moro cableway", "Monte Moro cableway Macugnaga"],
        "description": "Belvedere areas (Pecetto–Burki–Belvedere chairlifts) and Monte Moro (Staffa–Alpe Bill–Passo Moro cableways) in Macugnaga, Anzasca Valley. Views of Monte Rosa’s east face, alpine pastures and starting points for high walks. Opening hours: official lifts website.",
        "url": "https://www.macugnagabooking.it/en/funivia-seggiovia.html",
        "sameAs": [
          "https://macugnagamonterosaski.com/",
          "https://macugnagamonterosaski.com/impianti/",
          "https://macugnaga-monterosa.it/"
        ],
        "image": "https://www.macugnagabooking.it/assets/web/funivia-hero.jpg",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Macugnaga",
          "addressRegion": "VB",
          "postalCode": "28876",
          "addressCountry": "IT"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": 45.9667,
          "longitude": 7.9667
        },
        "touristType": ["families", "hikers", "Monte Rosa weekend", "summer and winter visitors"]
      },
      {
        "@type": "Service",
        "name": "Macugnaga ski lifts information",
        "serviceType": "Tourist information",
        "description": "Information page on Belvedere/Burki chairlifts and Monte Moro cableway in Macugnaga. Tickets and hours are managed by the lift company; here you find context and ideas to combine with portal experiences.",
        "url": "https://www.macugnagabooking.it/en/funivia-seggiovia.html",
        "provider": {
          "@type": "Organization",
          "name": "Macugnaga Booking – Experiences at the foot of Monte Rosa",
          "url": "https://www.macugnagabooking.it/en/"
        },
        "areaServed": {
          "@type": "Place",
          "name": "Macugnaga, Monte Rosa"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://macugnagamonterosaski.com/",
          "description": "Online booking of Belvedere chairlift and Alpe Bill cableway tickets on Macugnaga Booking; openings also on the official lifts website",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.macugnagabooking.it/en/"},
          {"@type": "ListItem", "position": 2, "name": "Macugnaga", "item": "https://www.macugnagabooking.it/en/scopri-macugnaga.html"},
          {"@type": "ListItem", "position": 3, "name": "Cableway and chairlift", "item": "https://www.macugnagabooking.it/en/funivia-seggiovia.html"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Which ski lifts are there in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Two main areas: the Belvedere chairlifts (Pecetto–Burki and Burki–Belvedere, with Alpe Burki as mid station) and the Monte Moro cableways (Staffa–Alpe Bill and Alpe Bill–Passo Moro)."
            }
          },
          {
            "@type": "Question",
            "name": "What can you do at altitude with chairlift and cableway?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Views of Monte Rosa’s east face from Belvedere (about 1914 m), a stop at Alpe Burki, starting points for walks toward refuges and the Belvedere glacier; on the Monte Moro side you climb toward Alpe Bill and, when the second section is running, toward Passo Moro (about 2870 m) with a 360° Alpine view."
            }
          },
          {
            "@type": "Question",
            "name": "Are the lifts open in summer?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Summer and winter openings vary and are published on the official lifts website. Always check lift status, hours and tickets on macugnagamonterosaski.com before you leave: individual sections may be open or closed for maintenance."
            }
          },
          {
            "@type": "Question",
            "name": "Can you book cableway tickets on the booking portal?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: on the Macugnaga Booking portal you can book online tickets for the Pecetto–Burki–Belvedere chairlift and the Staffa–Alpe Bill cableway (pay on site). Opening times and lift status are also updated on the official lift company website."
            }
          },
          {
            "@type": "Question",
            "name": "How to combine lifts and a weekend in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When the lifts are running, a half-day at altitude pairs well with village walks, the Walser House Museum and the gold mine. Plan weekend ideas and book activities on the booking portal."
            }
          }
        ]
      }
    ]
  }
  </script>''',
"fr": r'''<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "TouristAttraction",
        "name": "Remontées mécaniques Macugnaga — Belvedere et Monte Moro",
        "alternateName": ["Télésiège Belvedere Burki", "Téléphérique Passo Moro", "Téléphérique Monte Moro Macugnaga"],
        "description": "Domaines Belvedere (télésièges Pecetto–Burki–Belvedere) et Monte Moro (téléphériques Staffa–Alpe Bill–Passo Moro) à Macugnaga, Valle Anzasca. Panoramas sur la face Est du Monte Rosa, alpages et départs pour promenades en altitude. Horaires et ouvertures : site officiel des remontées.",
        "url": "https://www.macugnagabooking.it/fr/funivia-seggiovia.html",
        "sameAs": [
          "https://macugnagamonterosaski.com/",
          "https://macugnagamonterosaski.com/impianti/",
          "https://macugnaga-monterosa.it/"
        ],
        "image": "https://www.macugnagabooking.it/assets/web/funivia-hero.jpg",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Macugnaga",
          "addressRegion": "VB",
          "postalCode": "28876",
          "addressCountry": "IT"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": 45.9667,
          "longitude": 7.9667
        },
        "touristType": ["familles", "randonneurs", "week-end Monte Rosa", "visiteurs été et hiver"]
      },
      {
        "@type": "Service",
        "name": "Informations remontées Macugnaga",
        "serviceType": "Tourist information",
        "description": "Page d’information sur les télésièges Belvedere/Burki et le téléphérique Monte Moro à Macugnaga. Billets et horaires sont gérés par la société des remontées ; ici vous trouvez le contexte et des idées à combiner avec les expériences du portail.",
        "url": "https://www.macugnagabooking.it/fr/funivia-seggiovia.html",
        "provider": {
          "@type": "Organization",
          "name": "Macugnaga Booking – Expériences au pied du Monte Rosa",
          "url": "https://www.macugnagabooking.it/fr/"
        },
        "areaServed": {
          "@type": "Place",
          "name": "Macugnaga, Monte Rosa"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://macugnagamonterosaski.com/",
          "description": "Réservation en ligne des billets télésiège Belvedere et téléphérique Alpe Bill sur Macugnaga Booking ; ouvertures aussi sur le site officiel des remontées",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://www.macugnagabooking.it/fr/"},
          {"@type": "ListItem", "position": 2, "name": "Macugnaga", "item": "https://www.macugnagabooking.it/fr/scopri-macugnaga.html"},
          {"@type": "ListItem", "position": 3, "name": "Téléphérique et télésiège", "item": "https://www.macugnagabooking.it/fr/funivia-seggiovia.html"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Quelles remontées y a-t-il à Macugnaga ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Deux zones principales : les télésièges du Belvedere (Pecetto–Burki et Burki–Belvedere, avec Alpe Burki comme station intermédiaire) et les téléphériques du Monte Moro (Staffa–Alpe Bill et Alpe Bill–Passo Moro)."
            }
          },
          {
            "@type": "Question",
            "name": "Que faire en altitude avec télésiège et téléphérique ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Panoramas sur la face Est du Monte Rosa depuis le Belvedere (environ 1914 m), halte à l’Alpe Burki, départs pour promenades vers refuges et glacier du Belvedere ; sur le versant Monte Moro on monte vers Alpe Bill et, quand le second tronçon est en service, vers le Passo Moro (environ 2870 m) avec vue à 360° sur les Alpes."
            }
          },
          {
            "@type": "Question",
            "name": "Les remontées sont-elles ouvertes en été ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Les ouvertures estivales et hivernales varient et sont publiées sur le site officiel des remontées. Vérifiez toujours l’état des installations, horaires et billets sur macugnagamonterosaski.com avant de partir : des tronçons peuvent être ouverts ou fermés pour maintenance."
            }
          },
          {
            "@type": "Question",
            "name": "Peut-on réserver les billets téléphérique sur le portail de réservation ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : sur le portail Macugnaga Booking vous pouvez réserver en ligne les billets du télésiège Pecetto–Burki–Belvedere et du téléphérique Staffa–Alpe Bill (paiement sur place). Horaires et état des remontées restent aussi à jour sur le site officiel de la société."
            }
          },
          {
            "@type": "Question",
            "name": "Comment combiner remontées et week-end à Macugnaga ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Quand les remontées fonctionnent, une demi-journée en altitude se combine bien avec promenades au village, Maison-musée Walser et mine d’or. Organisez des idées week-end et réservez les activités sur le portail de réservation."
            }
          }
        ]
      }
    ]
  }
  </script>''',
"de": r'''<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "TouristAttraction",
        "name": "Bergbahnen Macugnaga — Belvedere und Monte Moro",
        "alternateName": ["Sesselbahn Belvedere Burki", "Seilbahn Passo Moro", "Seilbahn Monte Moro Macugnaga"],
        "description": "Gebiete Belvedere (Sesselbahnen Pecetto–Burki–Belvedere) und Monte Moro (Seilbahnen Staffa–Alpe Bill–Passo Moro) in Macugnaga, Valle Anzasca. Panoramen auf die Ostwand des Monte Rosa, Almen und Ausgangspunkte für Höhenwanderungen. Öffnungszeiten: offizielle Bergbahn-Website.",
        "url": "https://www.macugnagabooking.it/de/funivia-seggiovia.html",
        "sameAs": [
          "https://macugnagamonterosaski.com/",
          "https://macugnagamonterosaski.com/impianti/",
          "https://macugnaga-monterosa.it/"
        ],
        "image": "https://www.macugnagabooking.it/assets/web/funivia-hero.jpg",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Macugnaga",
          "addressRegion": "VB",
          "postalCode": "28876",
          "addressCountry": "IT"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": 45.9667,
          "longitude": 7.9667
        },
        "touristType": ["Familien", "Wanderer", "Monte-Rosa-Wochenende", "Sommer- und Wintergäste"]
      },
      {
        "@type": "Service",
        "name": "Informationen Bergbahnen Macugnaga",
        "serviceType": "Tourist information",
        "description": "Infoseite zu Sesselbahnen Belvedere/Burki und Seilbahn Monte Moro in Macugnaga. Tickets und Zeiten werden von der Bahngesellschaft verwaltet; hier finden Sie Kontext und Ideen zur Kombination mit Portal-Erlebnissen.",
        "url": "https://www.macugnagabooking.it/de/funivia-seggiovia.html",
        "provider": {
          "@type": "Organization",
          "name": "Macugnaga Booking – Erlebnisse am Fuße des Monte Rosa",
          "url": "https://www.macugnagabooking.it/de/"
        },
        "areaServed": {
          "@type": "Place",
          "name": "Macugnaga, Monte Rosa"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://macugnagamonterosaski.com/",
          "description": "Online-Buchung von Tickets für Sesselbahn Belvedere und Seilbahn Alpe Bill auf Macugnaga Booking; Öffnungen auch auf der offiziellen Bergbahn-Website",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Start", "item": "https://www.macugnagabooking.it/de/"},
          {"@type": "ListItem", "position": 2, "name": "Macugnaga", "item": "https://www.macugnagabooking.it/de/scopri-macugnaga.html"},
          {"@type": "ListItem", "position": 3, "name": "Seilbahn und Sesselbahn", "item": "https://www.macugnagabooking.it/de/funivia-seggiovia.html"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Welche Bergbahnen gibt es in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Zwei Hauptgebiete: die Belvedere-Sesselbahnen (Pecetto–Burki und Burki–Belvedere, mit Alpe Burki als Zwischenstation) und die Monte-Moro-Seilbahnen (Staffa–Alpe Bill und Alpe Bill–Passo Moro)."
            }
          },
          {
            "@type": "Question",
            "name": "Was kann man in der Höhe mit Sesselbahn und Seilbahn unternehmen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Panoramen auf die Ostwand des Monte Rosa vom Belvedere (ca. 1914 m), Pause an der Alpe Burki, Ausgangspunkte für Wanderungen zu Hütten und zum Belvedere-Gletscher; auf der Monte-Moro-Seite steigt man zur Alpe Bill und, wenn der zweite Abschnitt in Betrieb ist, zum Passo Moro (ca. 2870 m) mit 360°-Alpenblick."
            }
          },
          {
            "@type": "Question",
            "name": "Sind die Bahnen im Sommer geöffnet?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Sommer- und Winteröffnungen variieren und werden auf der offiziellen Bergbahn-Website veröffentlicht. Prüfen Sie vor der Abreise immer Status, Zeiten und Tickets auf macugnagamonterosaski.com: einzelne Abschnitte können wegen Wartung geöffnet oder geschlossen sein."
            }
          },
          {
            "@type": "Question",
            "name": "Kann man Seilbahn-Tickets auf dem Buchungsportal buchen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: auf dem Portal Macugnaga Booking können Sie online Tickets für die Sesselbahn Pecetto–Burki–Belvedere und die Seilbahn Staffa–Alpe Bill buchen (Zahlung vor Ort). Öffnungszeiten und Bahnstatus werden auch auf der offiziellen Website der Bahngesellschaft aktualisiert."
            }
          },
          {
            "@type": "Question",
            "name": "Wie kombiniert man Bahnen und ein Wochenende in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Wenn die Bahnen in Betrieb sind, lässt sich ein halber Tag in der Höhe gut mit Dorfspaziergängen, Walser-Hausmuseum und Goldmine kombinieren. Planen Sie Wochenend-Ideen und buchen Sie Aktivitäten auf dem Buchungsportal."
            }
          }
        ]
      }
    ]
  }
  </script>''',
}
