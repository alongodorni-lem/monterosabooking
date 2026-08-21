# -*- coding: utf-8 -*-
"""Casa Museo Walser JSON-LD translations (EN/FR/DE)."""
from __future__ import annotations

CASA = {
"en": r'''<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Museum",
        "name": "Ancient Walser House Museum of Borca — Alts Walserhüüs Van Zer Burfuggu",
        "alternateName": ["Walser House Museum Macugnaga", "Walser Museum Borca"],
        "description": "Ethnographic museum housed in the 17th-century parish house in Borca di Macugnaga. It collects and preserves everyday objects of the Walser people. Guided visit of about one hour, bookable online.",
        "url": "https://www.macugnagabooking.it/en/casa-museo-walser.html",
        "sameAs": ["http://www.museowalser.com/"],
        "telephone": "+39-347-9842329",
        "email": "museowalser@libero.it",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Via Monterosa / Frazione Borca",
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
        "isAccessibleForFree": false,
        "touristType": ["families", "schools", "alpine history enthusiasts", "Monte Rosa visitors"]
      },
      {
        "@type": "TouristAttraction",
        "name": "Walser House Museum in Borca",
        "description": "Walser house museum in Macugnaga Monte Rosa: stube, traditional crafts, bread collection and mining documents.",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Macugnaga",
          "addressRegion": "Piedmont",
          "addressCountry": "IT"
        }
      },
      {
        "@type": ["Product", "Service"],
        "name": "Visit Walser House Museum in Borca",
        "description": "Guided visit of about one hour in the 17th-century parish house in Borca di Macugnaga: stube, crafts, bread and Walser memory.",
        "image": "https://www.macugnagabooking.it/assets/web/casa-museo-hero.jpg",
        "brand": {
          "@type": "Brand",
          "name": "Macugnaga Booking – Experiences at the foot of Monte Rosa"
        },
        "category": "Museum",
        "areaServed": {
          "@type": "Place",
          "name": "Macugnaga, Valle Anzasca"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://www.macugnagabooking.it/en/casa-museo-walser.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR",
          "category": "Online booking museum entry"
        }
      },
      {
        "@type": "Event",
        "name": "Visit Walser House Museum in Borca",
        "description": "Bookable online: guided visit of about one hour to the Walser House Museum in Borca, Macugnaga.",
        "image": "https://www.macugnagabooking.it/assets/web/casa-museo-hero.jpg",
        "url": "https://www.macugnagabooking.it/en/casa-museo-walser.html",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "location": {
          "@type": "Place",
          "name": "Walser House Museum in Borca",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Via Monterosa / Frazione Borca",
            "addressLocality": "Macugnaga",
            "addressRegion": "VB",
            "postalCode": "28876",
            "addressCountry": "IT"
          }
        },
        "organizer": {
          "@type": "Organization",
          "name": "Macugnaga Booking – Experiences at the foot of Monte Rosa",
          "url": "https://www.macugnagabooking.it/en/"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://www.macugnagabooking.it/en/casa-museo-walser.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.macugnagabooking.it/en/"},
          {"@type": "ListItem", "position": 2, "name": "Experiences", "item": "https://www.macugnagabooking.it/en/esperienze.html"},
          {"@type": "ListItem", "position": 3, "name": "Walser House Museum", "item": "https://www.macugnagabooking.it/en/casa-museo-walser.html"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How do I book a visit to the Walser House Museum?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "You can book entry online directly from this page with the Book now button. You pay securely and immediately receive confirmation by email."
            }
          },
          {
            "@type": "Question",
            "name": "Where is the Walser House Museum?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In the Borca hamlet of Macugnaga (VB), Anzasca Valley, at the foot of Monte Rosa. It is housed in the 17th-century parish house."
            }
          },
          {
            "@type": "Question",
            "name": "How long does the visit last?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The guided route lasts about one hour and unfolds over several levels of the historic house."
            }
          },
          {
            "@type": "Question",
            "name": "What can you see in the museum?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Prints and exhibitions in the basement; hearth-kitchen, entrance and stube on the ground floor; ancient crafts, bread-making and Mining Society documents on the upper floor."
            }
          },
          {
            "@type": "Question",
            "name": "Is the visit suitable for families and schools?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. It is designed for alpine history enthusiasts, families and schools: a living comparison between past and present life."
            }
          },
          {
            "@type": "Question",
            "name": "Can you visit outside opening hours?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, by appointment. Booking online secures your place and time slot; for special needs you can contact the museum."
            }
          },
          {
            "@type": "Question",
            "name": "Who were the Walser?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Alemannic settlers who spread across the Alps from Valais. Macugnaga was born from crossing the Monte Moro Pass: here the House Museum preserves objects and memory of that community."
            }
          },
          {
            "@type": "Question",
            "name": "Why book online?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "You guarantee entry, avoid queues, pay by card or PayPal and receive immediate confirmation with all useful visit information."
            }
          },
          {
            "@type": "Question",
            "name": "Is the Walser House Museum worth it on a weekend or a day trip from Milan?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: in about an hour you discover the Walser soul of Macugnaga. It pairs well with walks, the gold mine and lifts — perfect on a Monte Rosa weekend or a mountain day trip from Milan, Varese or Novara."
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
        "@type": "Museum",
        "name": "Musée Ancienne Maison Walser de Borca — Alts Walserhüüs Van Zer Burfuggu",
        "alternateName": ["Maison-musée Walser Macugnaga", "Musée Walser Borca"],
        "description": "Musée ethnographique hébergé dans la maison paroissiale du XVIIe siècle à Borca di Macugnaga. Il recueille et préserve les objets de la vie quotidienne du peuple walser. Visite guidée d’environ une heure, réservable en ligne.",
        "url": "https://www.macugnagabooking.it/fr/casa-museo-walser.html",
        "sameAs": ["http://www.museowalser.com/"],
        "telephone": "+39-347-9842329",
        "email": "museowalser@libero.it",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Via Monterosa / Frazione Borca",
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
        "isAccessibleForFree": false,
        "touristType": ["familles", "écoles", "passionnés d’histoire alpine", "visiteurs du Monte Rosa"]
      },
      {
        "@type": "TouristAttraction",
        "name": "Maison-musée Walser de Borca",
        "description": "Maison-musée walser à Macugnaga Monte Rosa : stube, métiers traditionnels, collection du pain et documents miniers.",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Macugnaga",
          "addressRegion": "Piémont",
          "addressCountry": "IT"
        }
      },
      {
        "@type": ["Product", "Service"],
        "name": "Visite Maison-musée Walser de Borca",
        "description": "Visite guidée d’environ une heure dans la maison paroissiale du XVIIe siècle à Borca di Macugnaga : stube, métiers, pain et mémoire walser.",
        "image": "https://www.macugnagabooking.it/assets/web/casa-museo-hero.jpg",
        "brand": {
          "@type": "Brand",
          "name": "Macugnaga Booking – Expériences au pied du Monte Rosa"
        },
        "category": "Museum",
        "areaServed": {
          "@type": "Place",
          "name": "Macugnaga, Valle Anzasca"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://www.macugnagabooking.it/fr/casa-museo-walser.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR",
          "category": "Réservation en ligne entrée musée"
        }
      },
      {
        "@type": "Event",
        "name": "Visite Maison-musée Walser de Borca",
        "description": "Expérience réservable en ligne : visite guidée d’environ une heure à la Maison-musée Walser de Borca à Macugnaga.",
        "image": "https://www.macugnagabooking.it/assets/web/casa-museo-hero.jpg",
        "url": "https://www.macugnagabooking.it/fr/casa-museo-walser.html",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "location": {
          "@type": "Place",
          "name": "Maison-musée Walser de Borca",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Via Monterosa / Frazione Borca",
            "addressLocality": "Macugnaga",
            "addressRegion": "VB",
            "postalCode": "28876",
            "addressCountry": "IT"
          }
        },
        "organizer": {
          "@type": "Organization",
          "name": "Macugnaga Booking – Expériences au pied du Monte Rosa",
          "url": "https://www.macugnagabooking.it/fr/"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://www.macugnagabooking.it/fr/casa-museo-walser.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://www.macugnagabooking.it/fr/"},
          {"@type": "ListItem", "position": 2, "name": "Expériences", "item": "https://www.macugnagabooking.it/fr/esperienze.html"},
          {"@type": "ListItem", "position": 3, "name": "Maison-musée Walser", "item": "https://www.macugnagabooking.it/fr/casa-museo-walser.html"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Comment réserver la visite de la Maison-musée Walser ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Vous pouvez réserver l’entrée en ligne directement depuis cette page avec le bouton Réserver. Vous payez en toute sécurité et recevez immédiatement la confirmation par e-mail."
            }
          },
          {
            "@type": "Question",
            "name": "Où se trouve la Maison-musée Walser ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Dans le hameau de Borca à Macugnaga (VB), Valle Anzasca, au pied du Monte Rosa. Elle est hébergée dans la maison paroissiale du XVIIe siècle."
            }
          },
          {
            "@type": "Question",
            "name": "Combien dure la visite ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Le parcours guidé dure environ une heure et se développe sur plusieurs niveaux de la maison historique."
            }
          },
          {
            "@type": "Question",
            "name": "Que voit-on dans le musée ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Estampes et expositions au sous-sol ; foyer-cuisine, entrée et stube au rez-de-chaussée ; anciens métiers, travail du pain et documents de la Società Mineraria à l’étage."
            }
          },
          {
            "@type": "Question",
            "name": "La visite convient-elle aux familles et aux écoles ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui. Elle est conçue pour les passionnés d’histoire alpine, les familles et les écoles : une comparaison vivante entre la vie d’autrefois et celle d’aujourd’hui."
            }
          },
          {
            "@type": "Question",
            "name": "Peut-on visiter hors des horaires d’ouverture ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui, sur rendez-vous. En réservant en ligne vous assurez place et horaire ; pour des besoins particuliers vous pouvez contacter le musée."
            }
          },
          {
            "@type": "Question",
            "name": "Qui étaient les Walser ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Des colons alémaniques qui se répandirent sur les Alpes depuis le Valais. Macugnaga est née du franchissement du Passo del Monte Moro : ici la Maison-musée conserve objets et mémoire de cette communauté."
            }
          },
          {
            "@type": "Question",
            "name": "Pourquoi réserver en ligne ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Vous garantissez l’entrée, évitez les attentes, payez par carte ou PayPal et recevez une confirmation immédiate avec toutes les informations utiles pour la visite."
            }
          },
          {
            "@type": "Question",
            "name": "La Maison-musée Walser vaut-elle la peine pour un week-end ou une excursion depuis Milan ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : en environ une heure vous découvrez l’âme walser de Macugnaga. Elle se combine avec promenades, mine d’or et remontées — parfaite pour un week-end Monte Rosa ou une sortie en montagne depuis Milan, Varese ou Novara."
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
        "@type": "Museum",
        "name": "Museum Antikes Walserhaus Borca — Alts Walserhüüs Van Zer Burfuggu",
        "alternateName": ["Walser-Hausmuseum Macugnaga", "Walser-Museum Borca"],
        "description": "Ethnografisches Museum im Pfarrhaus aus dem 17. Jahrhundert in Borca di Macugnaga. Es sammelt und bewahrt Alltagsgegenstände des Walser-Volkes. Geführter Besuch von etwa einer Stunde, online buchbar.",
        "url": "https://www.macugnagabooking.it/de/casa-museo-walser.html",
        "sameAs": ["http://www.museowalser.com/"],
        "telephone": "+39-347-9842329",
        "email": "museowalser@libero.it",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Via Monterosa / Frazione Borca",
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
        "isAccessibleForFree": false,
        "touristType": ["Familien", "Schulen", "Interessierte an alpiner Geschichte", "Monte-Rosa-Besucher"]
      },
      {
        "@type": "TouristAttraction",
        "name": "Walser-Hausmuseum in Borca",
        "description": "Walser-Hausmuseum in Macugnaga Monte Rosa: Stube, traditionelle Handwerke, Brotsammlung und Bergbaudokumente.",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Macugnaga",
          "addressRegion": "Piemont",
          "addressCountry": "IT"
        }
      },
      {
        "@type": ["Product", "Service"],
        "name": "Besuch Walser-Hausmuseum in Borca",
        "description": "Geführter Besuch von etwa einer Stunde im Pfarrhaus aus dem 17. Jahrhundert in Borca di Macugnaga: Stube, Handwerke, Brot und Walser-Erinnerung.",
        "image": "https://www.macugnagabooking.it/assets/web/casa-museo-hero.jpg",
        "brand": {
          "@type": "Brand",
          "name": "Macugnaga Booking – Erlebnisse am Fuße des Monte Rosa"
        },
        "category": "Museum",
        "areaServed": {
          "@type": "Place",
          "name": "Macugnaga, Valle Anzasca"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://www.macugnagabooking.it/de/casa-museo-walser.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR",
          "category": "Online-Buchung Museumseintritt"
        }
      },
      {
        "@type": "Event",
        "name": "Besuch Walser-Hausmuseum in Borca",
        "description": "Online buchbar: geführter Besuch von etwa einer Stunde im Walser-Hausmuseum in Borca, Macugnaga.",
        "image": "https://www.macugnagabooking.it/assets/web/casa-museo-hero.jpg",
        "url": "https://www.macugnagabooking.it/de/casa-museo-walser.html",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "location": {
          "@type": "Place",
          "name": "Walser-Hausmuseum in Borca",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Via Monterosa / Frazione Borca",
            "addressLocality": "Macugnaga",
            "addressRegion": "VB",
            "postalCode": "28876",
            "addressCountry": "IT"
          }
        },
        "organizer": {
          "@type": "Organization",
          "name": "Macugnaga Booking – Erlebnisse am Fuße des Monte Rosa",
          "url": "https://www.macugnagabooking.it/de/"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://www.macugnagabooking.it/de/casa-museo-walser.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Start", "item": "https://www.macugnagabooking.it/de/"},
          {"@type": "ListItem", "position": 2, "name": "Erlebnisse", "item": "https://www.macugnagabooking.it/de/esperienze.html"},
          {"@type": "ListItem", "position": 3, "name": "Walser-Hausmuseum", "item": "https://www.macugnagabooking.it/de/casa-museo-walser.html"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Wie buche ich den Besuch des Walser-Hausmuseums?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Sie können den Eintritt online direkt von dieser Seite mit dem Button Jetzt buchen reservieren. Sie zahlen sicher und erhalten sofort die Bestätigung per E-Mail."
            }
          },
          {
            "@type": "Question",
            "name": "Wo liegt das Walser-Hausmuseum?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Im Weiler Borca von Macugnaga (VB), Valle Anzasca, am Fuße des Monte Rosa. Es ist im Pfarrhaus aus dem 17. Jahrhundert untergebracht."
            }
          },
          {
            "@type": "Question",
            "name": "Wie lange dauert der Besuch?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Die geführte Route dauert etwa eine Stunde und führt über mehrere Ebenen des historischen Hauses."
            }
          },
          {
            "@type": "Question",
            "name": "Was sieht man im Museum?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Drucke und Ausstellungen im Untergeschoss; Herd-Küche, Eingang und Stube im Erdgeschoss; alte Handwerke, Brotverarbeitung und Dokumente der Società Mineraria im Obergeschoss."
            }
          },
          {
            "@type": "Question",
            "name": "Eignet sich der Besuch für Familien und Schulen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja. Er ist für Interessierte an alpiner Geschichte, Familien und Schulen gedacht: ein lebendiger Vergleich zwischen dem Leben früher und heute."
            }
          },
          {
            "@type": "Question",
            "name": "Kann man außerhalb der Öffnungszeiten besuchen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja, nach Terminvereinbarung. Mit Online-Buchung sichern Sie Platz und Uhrzeit; für besondere Bedürfnisse können Sie das Museum kontaktieren."
            }
          },
          {
            "@type": "Question",
            "name": "Wer waren die Walser?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Alemannische Siedler, die sich vom Wallis über die Alpen ausbreiteten. Macugnaga entstand durch die Überquerung des Monte-Moro-Passes: hier bewahrt das Hausmuseum Gegenstände und Erinnerung jener Gemeinschaft."
            }
          },
          {
            "@type": "Question",
            "name": "Warum online buchen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Sie garantieren den Eintritt, vermeiden Wartezeiten, zahlen mit Karte oder PayPal und erhalten sofort eine Bestätigung mit allen nützlichen Infos zum Besuch."
            }
          },
          {
            "@type": "Question",
            "name": "Lohnt sich das Walser-Hausmuseum für ein Wochenende oder einen Ausflug ab Mailand?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: in etwa einer Stunde entdecken Sie die Walser-Seele Macugnagas. Es lässt sich mit Spaziergängen, Goldmine und Bahnen kombinieren — perfekt für ein Monte-Rosa-Wochenende oder einen Bergausflug ab Mailand, Varese oder Novara."
            }
          }
        ]
      }
    ]
  }
  </script>''',
}
