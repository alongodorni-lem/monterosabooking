# -*- coding: utf-8 -*-
"""Fix Italian leftovers in EN/FR/DE attraction + related JSON-LD / visible labels."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LD_RE = re.compile(
    r'<script type="application/ld\+json">\s*\{.*?\}\s*</script>',
    re.S,
)


def replace_ld(path: Path, new_ld: str) -> None:
    text = path.read_text(encoding="utf-8")
    m = LD_RE.search(text)
    if not m:
        raise SystemExit(f"No JSON-LD in {path}")
    # Prefer FAQPage-bearing graph if multiple scripts (replace first graph block only when single)
    scripts = list(LD_RE.finditer(text))
    # Replace the largest / first attraction graph (first script for these pages)
    target = scripts[0]
    path.write_text(text[: target.start()] + new_ld.strip() + text[target.end() :], encoding="utf-8")


def replace_all_ld_or_named(path: Path, new_blocks: list[str]) -> None:
    """Replace every application/ld+json script in order with new_blocks."""
    text = path.read_text(encoding="utf-8")
    scripts = list(LD_RE.finditer(text))
    if len(scripts) != len(new_blocks):
        raise SystemExit(f"{path}: expected {len(new_blocks)} ld scripts, found {len(scripts)}")
    out = []
    last = 0
    for m, block in zip(scripts, new_blocks):
        out.append(text[last : m.start()])
        out.append(block.strip())
        last = m.end()
    out.append(text[last:])
    path.write_text("".join(out), encoding="utf-8")


def patch_strings(path: Path, pairs: list[tuple[str, str]]) -> int:
    text = path.read_text(encoding="utf-8")
    n = 0
    for old, new in pairs:
        if old in text:
            c = text.count(old)
            text = text.replace(old, new)
            n += c
    path.write_text(text, encoding="utf-8")
    return n


# ── Miniera ──────────────────────────────────────────────────────────────────

MINIERA_EN = r'''<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "TouristAttraction",
        "name": "Guia Gold Mine Museum",
        "alternateName": ["Gold mine Macugnaga", "Miniera della Guia", "Guia gold mine"],
        "description": "Italy’s first underground gold mine open to visitors, in Macugnaga (Anzasca Valley, Monte Rosa). Guided visit of about 45 minutes in lit, level tunnels — also accessible for visitors with disabilities and pushchairs. Route about 1.5 km round trip.",
        "url": "https://www.macugnagabooking.it/en/miniera-oro.html",
        "sameAs": ["https://www.minieradoro.it/"],
        "image": "https://www.macugnagabooking.it/assets/web/miniera-hero.jpg",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Fornarelli / Guia",
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
        "touristType": ["families", "schools", "mining history enthusiasts", "Monte Rosa visitors"]
      },
      {
        "@type": "Museum",
        "name": "Guia Gold Mine Museum",
        "description": "Mine-museum in Macugnaga: gold veins, over 300 years of mining history and lit tunnels open with a guide.",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Macugnaga",
          "addressRegion": "Piedmont",
          "addressCountry": "IT"
        }
      },
      {
        "@type": ["Product", "Service"],
        "name": "Guided visit Guia gold mine",
        "description": "Guided visit of about 45 minutes in the lit tunnels of Italy’s first underground gold mine open to visitors. Level route about 1.5 km.",
        "image": "https://www.macugnagabooking.it/assets/web/miniera-hero.jpg",
        "brand": {
          "@type": "Brand",
          "name": "Macugnaga Booking – Experiences at the foot of Monte Rosa"
        },
        "category": "TouristAttraction",
        "areaServed": {
          "@type": "Place",
          "name": "Macugnaga, Valle Anzasca"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://www.macugnagabooking.it/en/miniera-oro.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR",
          "category": "Online booking guided visit"
        }
      },
      {
        "@type": "Event",
        "name": "Guided visit Guia gold mine",
        "description": "Bookable online: guided visit of about 45 minutes in the tunnels of the Guia gold mine in Macugnaga.",
        "image": "https://www.macugnagabooking.it/assets/web/miniera-hero.jpg",
        "url": "https://www.macugnagabooking.it/en/miniera-oro.html",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "location": {
          "@type": "Place",
          "name": "Guia gold mine",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Fornarelli / Guia",
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
          "url": "https://www.macugnagabooking.it/en/miniera-oro.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.macugnagabooking.it/en/"},
          {"@type": "ListItem", "position": 2, "name": "Experiences", "item": "https://www.macugnagabooking.it/en/esperienze.html"},
          {"@type": "ListItem", "position": 3, "name": "Gold mine", "item": "https://www.macugnagabooking.it/en/miniera-oro.html"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How do I book a visit to the gold mine?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "You can book online directly from this page with the Book now button. Complete the online booking form, pay securely and immediately receive confirmation by email."
            }
          },
          {
            "@type": "Question",
            "name": "Where is the Guia gold mine?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Near Fornarelli in Macugnaga (VB), Anzasca Valley, at the foot of Monte Rosa. Reach it from Pieve Vergonte or Piedimulera following signs for Macugnaga."
            }
          },
          {
            "@type": "Question",
            "name": "How long does the visit last and how long is the route?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The guided visit lasts about 45 minutes. The visitable route is about 1.5 km round trip, entirely level and lit."
            }
          },
          {
            "@type": "Question",
            "name": "Is the mine accessible for people with disabilities and pushchairs?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. The visit takes place on a single level, also accessible to people with disabilities and children in pushchairs."
            }
          },
          {
            "@type": "Question",
            "name": "What should I bring and what temperature is it inside?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Inside, the temperature is about 9 °C with high humidity (about 97%): a jacket is recommended. Animals are not allowed."
            }
          },
          {
            "@type": "Question",
            "name": "When is the gold mine open?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In the summer season typically from early June to mid-September, with online booking. Check dates and availability when you book online."
            }
          },
          {
            "@type": "Question",
            "name": "Why is it worth visiting in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "It is the first underground gold mine open to visitors in Italy: a journey into Monte Rosa mining history, complementary to walks, Walser House and lifts."
            }
          },
          {
            "@type": "Question",
            "name": "Why book online?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Booking is online. Booking online secures your place and time slot, you pay by card or PayPal and receive immediate confirmation with useful visit information."
            }
          },
          {
            "@type": "Question",
            "name": "Is the gold mine suitable for families and a day trip from Milan?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: a level route, also accessible with a pushchair, lasting about 45 minutes. It pairs with Walser House and walks — ideal on a Macugnaga Monte Rosa weekend or a mountain day trip from Milan, Varese or Novara."
            }
          }
        ]
      }
    ]
  }
  </script>'''

MINIERA_FR = r'''<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "TouristAttraction",
        "name": "Musée de la mine d’or de la Guia",
        "alternateName": ["Mine d’or Macugnaga", "Miniera della Guia", "Mine d’or de la Guia"],
        "description": "Première mine d’or souterraine visitable en Italie, à Macugnaga (Valle Anzasca, Monte Rosa). Visite guidée d’environ 45 minutes dans des galeries éclairées et de plain-pied, accessibles aussi aux personnes en situation de handicap et aux poussettes. Parcours d’environ 1,5 km aller-retour.",
        "url": "https://www.macugnagabooking.it/fr/miniera-oro.html",
        "sameAs": ["https://www.minieradoro.it/"],
        "image": "https://www.macugnagabooking.it/assets/web/miniera-hero.jpg",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Fornarelli / Guia",
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
        "touristType": ["familles", "écoles", "passionnés d’histoire minière", "visiteurs du Monte Rosa"]
      },
      {
        "@type": "Museum",
        "name": "Musée de la mine d’or de la Guia",
        "description": "Mine-musée à Macugnaga : filons aurifères, plus de 300 ans d’histoire extractive et galeries éclairées visitables avec guide.",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Macugnaga",
          "addressRegion": "Piémont",
          "addressCountry": "IT"
        }
      },
      {
        "@type": ["Product", "Service"],
        "name": "Visite guidée Mine d’or de la Guia",
        "description": "Visite guidée d’environ 45 minutes dans les galeries éclairées de la première mine d’or souterraine visitable en Italie. Parcours de plain-pied d’environ 1,5 km.",
        "image": "https://www.macugnagabooking.it/assets/web/miniera-hero.jpg",
        "brand": {
          "@type": "Brand",
          "name": "Macugnaga Booking – Expériences au pied du Monte Rosa"
        },
        "category": "TouristAttraction",
        "areaServed": {
          "@type": "Place",
          "name": "Macugnaga, Valle Anzasca"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://www.macugnagabooking.it/fr/miniera-oro.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR",
          "category": "Réservation en ligne visite guidée"
        }
      },
      {
        "@type": "Event",
        "name": "Visite guidée Mine d’or de la Guia",
        "description": "Expérience réservable en ligne : visite guidée d’environ 45 minutes dans les galeries de la Mine d’or de la Guia à Macugnaga.",
        "image": "https://www.macugnagabooking.it/assets/web/miniera-hero.jpg",
        "url": "https://www.macugnagabooking.it/fr/miniera-oro.html",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "location": {
          "@type": "Place",
          "name": "Mine d’or de la Guia",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Fornarelli / Guia",
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
          "url": "https://www.macugnagabooking.it/fr/miniera-oro.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://www.macugnagabooking.it/fr/"},
          {"@type": "ListItem", "position": 2, "name": "Expériences", "item": "https://www.macugnagabooking.it/fr/esperienze.html"},
          {"@type": "ListItem", "position": 3, "name": "Mine d’or", "item": "https://www.macugnagabooking.it/fr/miniera-oro.html"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Comment réserver la visite de la Mine d’or ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Vous pouvez réserver en ligne directement depuis cette page avec le bouton Réserver. Remplissez le formulaire de réservation en ligne, payez en toute sécurité et recevez immédiatement la confirmation par e-mail."
            }
          },
          {
            "@type": "Question",
            "name": "Où se trouve la Mine d’or de la Guia ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Près de Fornarelli à Macugnaga (VB), Valle Anzasca, au pied du Monte Rosa. On y accède depuis Pieve Vergonte ou Piedimulera en suivant les indications pour Macugnaga."
            }
          },
          {
            "@type": "Question",
            "name": "Combien dure la visite et quelle est la longueur du parcours ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "La visite guidée dure environ 45 minutes. Le parcours visitable mesure environ 1,5 km aller-retour, entièrement de plain-pied et éclairé."
            }
          },
          {
            "@type": "Question",
            "name": "La mine est-elle accessible aux personnes en situation de handicap et aux poussettes ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui. La visite se déroule sur un seul niveau, accessible aussi aux personnes en situation de handicap et aux enfants en poussette."
            }
          },
          {
            "@type": "Question",
            "name": "Que faut-il apporter et quelle température y a-t-il à l’intérieur ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "À l’intérieur, la température est d’environ 9 °C avec une humidité élevée (environ 97 %) : une veste est conseillée. Les animaux ne sont pas admis."
            }
          },
          {
            "@type": "Question",
            "name": "Quand la Mine d’or est-elle ouverte ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "En saison estivale typiquement de début juin à mi-septembre, avec réservation en ligne. Vérifiez les dates et disponibilités au moment de la réservation."
            }
          },
          {
            "@type": "Question",
            "name": "Pourquoi vaut-il la peine de la visiter à Macugnaga ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "C’est la première mine d’or souterraine visitable en Italie : un voyage dans l’histoire minière du Monte Rosa, complémentaire aux promenades, à la Maison Walser et aux remontées."
            }
          },
          {
            "@type": "Question",
            "name": "Pourquoi réserver en ligne ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "La réservation se fait en ligne. En réservant en ligne vous assurez place et horaire, payez par carte ou PayPal et recevez une confirmation immédiate avec les informations utiles pour la visite."
            }
          },
          {
            "@type": "Question",
            "name": "La Mine d’or convient-elle aux familles et à une excursion depuis Milan ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : parcours de plain-pied, accessible aussi avec poussette, durée d’environ 45 minutes. Elle se combine avec la Maison Walser et les promenades — idéale pour un week-end Macugnaga Monte Rosa ou une sortie en montagne depuis Milan, Varese ou Novara."
            }
          }
        ]
      }
    ]
  }
  </script>'''

MINIERA_DE = r'''<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "TouristAttraction",
        "name": "Goldminen-Museum Guia",
        "alternateName": ["Goldmine Macugnaga", "Miniera della Guia", "Goldmine Guia"],
        "description": "Italiens erste unterirdische Goldmine, die besichtigt werden kann, in Macugnaga (Valle Anzasca, Monte Rosa). Geführter Besuch von ca. 45 Minuten in beleuchteten, ebenen Stollen — auch zugänglich für Menschen mit Behinderung und Kinderwagen. Strecke ca. 1,5 km hin und zurück.",
        "url": "https://www.macugnagabooking.it/de/miniera-oro.html",
        "sameAs": ["https://www.minieradoro.it/"],
        "image": "https://www.macugnagabooking.it/assets/web/miniera-hero.jpg",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Fornarelli / Guia",
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
        "touristType": ["Familien", "Schulen", "Interessierte an Bergbaugeschichte", "Monte-Rosa-Besucher"]
      },
      {
        "@type": "Museum",
        "name": "Goldminen-Museum Guia",
        "description": "Minenmuseum in Macugnaga: Goldadern, über 300 Jahre Bergbaugeschichte und beleuchtete Stollen mit Führung.",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Macugnaga",
          "addressRegion": "Piemont",
          "addressCountry": "IT"
        }
      },
      {
        "@type": ["Product", "Service"],
        "name": "Geführter Besuch Goldmine Guia",
        "description": "Geführter Besuch von ca. 45 Minuten in den beleuchteten Stollen der ersten unterirdischen Goldmine Italiens, die besichtigt werden kann. Ebene Strecke ca. 1,5 km.",
        "image": "https://www.macugnagabooking.it/assets/web/miniera-hero.jpg",
        "brand": {
          "@type": "Brand",
          "name": "Macugnaga Booking – Erlebnisse am Fuße des Monte Rosa"
        },
        "category": "TouristAttraction",
        "areaServed": {
          "@type": "Place",
          "name": "Macugnaga, Valle Anzasca"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://www.macugnagabooking.it/de/miniera-oro.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR",
          "category": "Online-Buchung geführter Besuch"
        }
      },
      {
        "@type": "Event",
        "name": "Geführter Besuch Goldmine Guia",
        "description": "Online buchbar: geführter Besuch von ca. 45 Minuten in den Stollen der Goldmine Guia in Macugnaga.",
        "image": "https://www.macugnagabooking.it/assets/web/miniera-hero.jpg",
        "url": "https://www.macugnagabooking.it/de/miniera-oro.html",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "location": {
          "@type": "Place",
          "name": "Goldmine Guia",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Fornarelli / Guia",
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
          "url": "https://www.macugnagabooking.it/de/miniera-oro.html",
          "availability": "https://schema.org/InStock",
          "priceCurrency": "EUR"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Start", "item": "https://www.macugnagabooking.it/de/"},
          {"@type": "ListItem", "position": 2, "name": "Erlebnisse", "item": "https://www.macugnagabooking.it/de/esperienze.html"},
          {"@type": "ListItem", "position": 3, "name": "Goldmine", "item": "https://www.macugnagabooking.it/de/miniera-oro.html"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Wie buche ich den Besuch der Goldmine?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Sie können online direkt von dieser Seite mit dem Button Jetzt buchen reservieren. Füllen Sie das Online-Buchungsformular aus, zahlen Sie sicher und erhalten Sie sofort die Bestätigung per E-Mail."
            }
          },
          {
            "@type": "Question",
            "name": "Wo liegt die Goldmine Guia?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In der Nähe von Fornarelli in Macugnaga (VB), Valle Anzasca, am Fuße des Monte Rosa. Erreichbar von Pieve Vergonte oder Piedimulera den Schildern nach Macugnaga folgend."
            }
          },
          {
            "@type": "Question",
            "name": "Wie lange dauert der Besuch und wie lang ist die Strecke?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Der geführte Besuch dauert ca. 45 Minuten. Die begehbare Strecke misst ca. 1,5 km hin und zurück, durchgehend eben und beleuchtet."
            }
          },
          {
            "@type": "Question",
            "name": "Ist die Mine für Menschen mit Behinderung und Kinderwagen zugänglich?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja. Der Besuch findet auf einer einzigen Ebene statt, auch zugänglich für Menschen mit Behinderung und Kinder im Kinderwagen."
            }
          },
          {
            "@type": "Question",
            "name": "Was sollte ich mitbringen und welche Temperatur herrscht innen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Innen beträgt die Temperatur ca. 9 °C bei hoher Luftfeuchtigkeit (ca. 97 %): eine Jacke wird empfohlen. Tiere sind nicht erlaubt."
            }
          },
          {
            "@type": "Question",
            "name": "Wann ist die Goldmine geöffnet?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In der Sommersaison typischerweise von Anfang Juni bis Mitte September, mit Online-Buchung. Prüfen Sie Daten und Verfügbarkeit bei der Buchung."
            }
          },
          {
            "@type": "Question",
            "name": "Warum lohnt sich der Besuch in Macugnaga?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Es ist Italiens erste unterirdische Goldmine, die besichtigt werden kann: eine Reise in die Bergbaugeschichte des Monte Rosa, ergänzend zu Spaziergängen, Walser-Haus und Bahnen."
            }
          },
          {
            "@type": "Question",
            "name": "Warum online buchen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Die Buchung erfolgt online. Mit Online-Buchung sichern Sie Platz und Uhrzeit, zahlen mit Karte oder PayPal und erhalten sofort eine Bestätigung mit nützlichen Infos zum Besuch."
            }
          },
          {
            "@type": "Question",
            "name": "Eignet sich die Goldmine für Familien und einen Ausflug ab Mailand?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: ebene Strecke, auch mit Kinderwagen zugänglich, Dauer ca. 45 Minuten. Sie lässt sich mit Walser-Haus und Spaziergängen kombinieren — ideal für ein Macugnaga-Monte-Rosa-Wochenende oder einen Bergausflug ab Mailand, Varese oder Novara."
            }
          }
        ]
      }
    ]
  }
  </script>'''

from _fix_attraction_schema_i18n_casa import CASA
from _fix_attraction_schema_i18n_funivia import FUNIVIA

MINIERA = {"en": MINIERA_EN, "fr": MINIERA_FR, "de": MINIERA_DE}

# Visible / meta leftovers shared across attraction pages
VISIBLE = {
    "en": [
        ('<meta name="keywords" content="Gold mine Macugnaga, Miniera della Guia, prenota miniera oro, museo miniera Valle Anzasca, visita gallerie oro Monte Rosa">',
         '<meta name="keywords" content="Gold mine Macugnaga, Miniera della Guia, book gold mine, mine museum Anzasca Valley, gold tunnels Monte Rosa">'),
        ('<meta name="keywords" content="Walser House Museum, Macugnaga, visita museo Borca, prenota museo Walser, storia Walser Monte Rosa, Alts Walserhüüs">',
         '<meta name="keywords" content="Walser House Museum, Macugnaga, Borca museum visit, book Walser museum, Walser history Monte Rosa, Alts Walserhüüs">'),
        ("alt=\"Visita guidata nelle gallerie della Guia gold mine a Macugnaga\"",
         "alt=\"Guided visit in the tunnels of the Guia gold mine in Macugnaga\""),
        ("alt=\"Visita guidata nelle gallerie della Guia gold mine\"",
         "alt=\"Guided visit in the tunnels of the Guia gold mine\""),
        ("alt=\"Gallerie illuminate della Guia gold mine\"",
         "alt=\"Lit tunnels of the Guia gold mine\""),
        ("alt=\"Tunnel rocciosi della Gold mine on Monte Rosa\"",
         "alt=\"Rock tunnels of the gold mine on Monte Rosa\""),
        ("alt=\"Ingresso e cascata presso la Guia gold mine\"",
         "alt=\"Entrance and waterfall at the Guia gold mine\""),
        ("alt=\"Visita guidata all’esterno della Guia gold mine\"",
         "alt=\"Guided visit outside the Guia gold mine\""),
        ("<p class=\"section__eyebrow reveal\">Info pratiche</p>",
         "<p class=\"section__eyebrow reveal\">Practical info</p>"),
        ("<div><dt>Durata</dt>", "<div><dt>Duration</dt>"),
        ("<div><dt>Dove</dt>", "<div><dt>Where</dt>"),
        ("            <strong>Dove</strong>", "            <strong>Where</strong>"),
        ("            <strong>Durata</strong>", "            <strong>Duration</strong>"),
        ("alt=\"Esterno della Walser House Museum in Borca a Macugnaga, tipica architettura alpina\"",
         "alt=\"Exterior of the Walser House Museum in Borca, Macugnaga, typical alpine architecture\""),
        ("alt=\"Facciata della Casa Museo a Borca di Macugnaga con insegna e balcone fiorito\"",
         "alt=\"Facade of the House Museum in Borca di Macugnaga with sign and flower balcony\""),
        ("alt=\"Focolare e cucina storica della Walser House Museum\"",
         "alt=\"Hearth and historic kitchen of the Walser House Museum\""),
        ("alt=\"Sala dei mestieri tradizionali con attrezzi e calzature\"",
         "alt=\"Traditional crafts room with tools and footwear\""),
        ("alt=\"Sala della lavorazione e conservazione del pane\"",
         "alt=\"Bread-making and storage room\""),
        ("alt=\"Walser House Museum in Borca: architettura in legno e pietra ai piedi del Monte Rosa\"",
         "alt=\"Walser House Museum in Borca: wood and stone architecture at the foot of Monte Rosa\""),
        ("<div><dt>Context</dt><dd>Casa parrocchiale del XVII secolo (Alts Walserhüüs Van Zer Burfuggu)</dd></div>",
         "<div><dt>Context</dt><dd>17th-century parish house (Alts Walserhüüs Van Zer Burfuggu)</dd></div>"),
        ("<div><dt>For whom</dt><dd>Families, scuole, appassionati di storia alpina</dd></div>",
         "<div><dt>For whom</dt><dd>Families, schools, alpine history enthusiasts</dd></div>"),
        ("<div><dt>Dove</dt><dd>Frazione Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</dd></div>",
         "<div><dt>Where</dt><dd>Borca hamlet, Macugnaga (VB) — Anzasca Valley, Monte Rosa</dd></div>"),
        ("            <strong>Dove</strong>\n            <span>Frazione Borca, Macugnaga (VB) — Valle Anzasca, Monte Rosa</span>",
         "            <strong>Where</strong>\n            <span>Borca hamlet, Macugnaga (VB) — Anzasca Valley, Monte Rosa</span>"),
        ("destinazione <a href=\"https://macugnaga-monterosa.it/\"",
         "destination <a href=\"https://macugnaga-monterosa.it/\""),
        ("            <strong>Destinazione</strong>", "            <strong>Destination</strong>"),
        ("Cableway and chairlift in quota", "Cableway and chairlift at altitude"),
        ("alt=\"Dorf di Macugnaga, case alpine tradizionali\"",
         "alt=\"Dorf of Macugnaga, traditional alpine houses\""),
        ("alt=\"Antiche case del Dorf di Macugnaga\"",
         "alt=\"Historic houses of the Dorf of Macugnaga\""),
        ("alt=\"Storia e paesaggio di Macugnaga\"",
         "alt=\"History and landscape of Macugnaga\""),
        ("alt=\"Gold mine sotterranea\"", "alt=\"Underground gold mine\""),
        ("alt=\"Benessere tra gli alberi\"", "alt=\"Wellness among the trees\""),
        ("\"description\": \"The project del booking portal esperienze a Macugnaga Monte Rosa: catalogo, booking online e widget condivisibile.\"",
         "\"description\": \"The Macugnaga Monte Rosa booking portal project: catalogue, online booking and embeddable widget.\""),
        ("<p class=\"lead\" style=\"color:rgba(255,255,255,.9)\">Per informazioni on progetto, on widget o on the esperienze in catalogo.</p>",
         "<p class=\"lead\" style=\"color:rgba(255,255,255,.9)\">For information on the project, the widget or experiences in the catalogue.</p>"),
        ("            <div><dt>Dove</dt><dd>Macugnaga (VB), Valle Anzasca — Monte Rosa</dd></div>",
         "            <div><dt>Where</dt><dd>Macugnaga (VB), Anzasca Valley — Monte Rosa</dd></div>"),
    ],
    "fr": [
        ('<meta name="keywords" content="Mine d’or Macugnaga, Miniera della Guia, prenota miniera oro, museo miniera Valle Anzasca, visita gallerie oro Monte Rosa">',
         '<meta name="keywords" content="Mine d’or Macugnaga, Miniera della Guia, réserver mine d’or, musée mine Valle Anzasca, galeries or Monte Rosa">'),
        ("alt=\"Visita guidata nelle gallerie della Mine d’or de la Guia a Macugnaga\"",
         "alt=\"Visite guidée dans les galeries de la Mine d’or de la Guia à Macugnaga\""),
        ("alt=\"Visita guidata nelle gallerie della Mine d’or de la Guia\"",
         "alt=\"Visite guidée dans les galeries de la Mine d’or de la Guia\""),
        ("alt=\"Gallerie illuminate della Mine d’or de la Guia\"",
         "alt=\"Galeries éclairées de la Mine d’or de la Guia\""),
        ("alt=\"Tunnel rocciosi della Mine d’or on Monte Rosa\"",
         "alt=\"Tunnels rocheux de la Mine d’or sur le Monte Rosa\""),
        ("alt=\"Ingresso e cascata presso la Mine d’or de la Guia\"",
         "alt=\"Entrée et cascade près de la Mine d’or de la Guia\""),
        ("alt=\"Visita guidata all’esterno della Mine d’or de la Guia\"",
         "alt=\"Visite guidée à l’extérieur de la Mine d’or de la Guia\""),
        ("<p class=\"section__eyebrow reveal\">Info pratiche</p>",
         "<p class=\"section__eyebrow reveal\">Infos pratiques</p>"),
        ("<div><dt>Durata</dt>", "<div><dt>Durée</dt>"),
        ("<div><dt>Dove</dt>", "<div><dt>Où</dt>"),
        ("            <strong>Dove</strong>", "            <strong>Où</strong>"),
        ("            <strong>Durata</strong>", "            <strong>Durée</strong>"),
        ("alt=\"Esterno della Maison-musée Walser de Borca a Macugnaga, tipica architettura alpina\"",
         "alt=\"Extérieur de la Maison-musée Walser de Borca à Macugnaga, architecture alpine typique\""),
        ("alt=\"Facciata della Casa Museo a Borca di Macugnaga con insegna e balcone fiorito\"",
         "alt=\"Façade de la Maison-musée à Borca di Macugnaga avec enseigne et balcon fleuri\""),
        ("alt=\"Focolare e cucina storica della Maison-musée Walser\"",
         "alt=\"Foyer et cuisine historique de la Maison-musée Walser\""),
        ("alt=\"Sala dei mestieri tradizionali con attrezzi e calzature\"",
         "alt=\"Salle des métiers traditionnels avec outils et chaussures\""),
        ("alt=\"Sala della lavorazione e conservazione del pane\"",
         "alt=\"Salle de fabrication et conservation du pain\""),
        ("            <strong>Destinazione</strong>", "            <strong>Destination</strong>"),
        ("\"description\": \"Le projet del portail de réservation esperienze a Macugnaga Monte Rosa: catalogo, booking online e widget condivisibile.\"",
         "\"description\": \"Le projet du portail de réservation d’expériences à Macugnaga Monte Rosa : catalogue, réservation en ligne et widget intégrable.\""),
        ("<p class=\"lead\" style=\"color:rgba(255,255,255,.9)\">Per informazioni sur progetto, sur widget o sulle esperienze in catalogo.</p>",
         "<p class=\"lead\" style=\"color:rgba(255,255,255,.9)\">Pour toute information sur le projet, le widget ou les expériences du catalogue.</p>"),
        (">Vedi le esperienze</a>", ">Voir les expériences</a>"),
        ("            <div><dt>Dove</dt><dd>Macugnaga (VB), Valle Anzasca — Monte Rosa</dd></div>",
         "            <div><dt>Où</dt><dd>Macugnaga (VB), Valle Anzasca — Monte Rosa</dd></div>"),
    ],
    "de": [
        ('<meta name="keywords" content="Goldmine Macugnaga, Miniera della Guia, prenota miniera oro, museo miniera Valle Anzasca, visita gallerie oro Monte Rosa">',
         '<meta name="keywords" content="Goldmine Macugnaga, Miniera della Guia, Goldmine buchen, Minenmuseum Valle Anzasca, Goldstollen Monte Rosa">'),
        ("alt=\"Visita guidata nelle gallerie della Goldmine Guia a Macugnaga\"",
         "alt=\"Geführter Besuch in den Stollen der Goldmine Guia in Macugnaga\""),
        ("alt=\"Visita guidata nelle gallerie della Goldmine Guia\"",
         "alt=\"Geführter Besuch in den Stollen der Goldmine Guia\""),
        ("alt=\"Gallerie illuminate della Goldmine Guia\"",
         "alt=\"Beleuchtete Stollen der Goldmine Guia\""),
        ("alt=\"Tunnel rocciosi della Goldmine on Monte Rosa\"",
         "alt=\"Felsstollen der Goldmine am Monte Rosa\""),
        ("alt=\"Ingresso e cascata presso la Goldmine Guia\"",
         "alt=\"Eingang und Wasserfall bei der Goldmine Guia\""),
        ("alt=\"Visita guidata all’esterno della Goldmine Guia\"",
         "alt=\"Geführter Besuch außerhalb der Goldmine Guia\""),
        ("<p class=\"section__eyebrow reveal\">Info pratiche</p>",
         "<p class=\"section__eyebrow reveal\">Praktische Infos</p>"),
        ("<div><dt>Durata</dt>", "<div><dt>Dauer</dt>"),
        ("<div><dt>Dove</dt>", "<div><dt>Wo</dt>"),
        ("            <strong>Dove</strong>", "            <strong>Wo</strong>"),
        ("            <strong>Durata</strong>", "            <strong>Dauer</strong>"),
        ("alt=\"Esterno della Walser-Hausmuseum in Borca a Macugnaga, tipica architettura alpina\"",
         "alt=\"Außenansicht des Walser-Hausmuseums in Borca, Macugnaga, typische alpine Architektur\""),
        ("alt=\"Facciata della Casa Museo a Borca di Macugnaga con insegna e balcone fiorito\"",
         "alt=\"Fassade des Hausmuseums in Borca di Macugnaga mit Schild und Blumenbalkon\""),
        ("alt=\"Focolare e cucina storica della Walser-Hausmuseum\"",
         "alt=\"Herd und historische Küche des Walser-Hausmuseums\""),
        ("alt=\"Sala dei mestieri tradizionali con attrezzi e calzature\"",
         "alt=\"Raum der traditionellen Handwerke mit Werkzeugen und Schuhen\""),
        ("alt=\"Sala della lavorazione e conservazione del pane\"",
         "alt=\"Raum für Brotverarbeitung und -lagerung\""),
        ("            <strong>Destinazione</strong>", "            <strong>Destination</strong>"),
        ("\"description\": \"Das Projekt del Buchungsportal esperienze a Macugnaga Monte Rosa: catalogo, booking online e widget condivisibile.\"",
         "\"description\": \"Das Projekt des Buchungsportals für Erlebnisse in Macugnaga Monte Rosa: Katalog, Online-Buchung und einbettbares Widget.\""),
        ("<p class=\"lead\" style=\"color:rgba(255,255,255,.9)\">Per informazioni am progetto, am widget o sulle esperienze in catalogo.</p>",
         "<p class=\"lead\" style=\"color:rgba(255,255,255,.9)\">Für Informationen zum Projekt, zum Widget oder zu den Erlebnissen im Katalog.</p>"),
        (">Vedi le esperienze</a>", ">Erlebnisse anzeigen</a>"),
        ("            <div><dt>Dove</dt><dd>Macugnaga (VB), Valle Anzasca — Monte Rosa</dd></div>",
         "            <div><dt>Wo</dt><dd>Macugnaga (VB), Valle Anzasca — Monte Rosa</dd></div>"),
    ],
}

SCOPRI_FAQ_LD = {
"en": '''          {
            "@type": "Question",
            "name": "Is Macugnaga suitable as a mountain destination for families and mountains with children?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. Macugnaga is a family-scale mountain destination: easy routes, a welcoming village and guided experiences without technical mountaineering. See the Families page and the booking portal activities."
            }
          },
          {
            "@type": "Question",
            "name": "Is Macugnaga a mountain destination for couples and groups of friends?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: mountain silence, Monte Rosa views, walks and nature experiences make it ideal for a romantic couple’s weekend or a getaway with friends. See the Couples and Weekend pages on the booking portal."
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
              "text": "Yes: from the Dorf to the woods and trails under Monte Rosa you find walks and soft hikes, ideal for families and anyone who wants to live the mountains from the village. Book outdoor experiences on the Experiences page of the booking portal."
            }
          },
          {
            "@type": "Question",
            "name": "Is Macugnaga still real mountain country, with characterful places and historic chalets?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. The village has kept traditional architecture, historic chalets, fine landscape and Monte Rosa panoramas: an authentic alpine village, among the most beautiful in the Alps (Touring Club Italiano Orange Flag), to be enjoyed from the centre and the trails."
            }
          },
          {
            "@type": "Question",
            "name": "Is Macugnaga suitable for a real mountain weekend, close to Milan, Novara, Varese and the cities of the plain?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes: about 2 hours from Milan and about 1.5 hours from Novara and Varese, also reachable from Lake Maggiore, Turin, the Po Plain and Switzerland. Ideal for day trips and weekends away from the city. See Weekend and City escape."
            }
          }''',
"fr": '''          {
            "@type": "Question",
            "name": "Macugnaga convient-elle comme montagne pour familles et montagne avec enfants ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui. Macugnaga est une station de montagne à dimension familiale : parcours faciles, village accueillant et expériences guidées sans alpinisme technique. Consultez la page Familles et les activités du portail de réservation."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga est-elle une destination de montagne pour couples et groupes d’amis ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : silences de montagne, panoramas sur le Monte Rosa, promenades et expériences au contact de la nature la rendent idéale pour un week-end romantique en couple ou une escapade entre amis. Voir les pages Couples et Week-end du portail."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga est-elle idéale pour les voyageurs seniors ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui. Rythme doux, sentiers accessibles, bien-être en forêt et visites culturelles (Maison-musée Walser, mine d’or) conviennent à qui cherche la vraie montagne sans efforts extrêmes. Découvrez la page Seniors."
            }
          },
          {
            "@type": "Question",
            "name": "Y a-t-il des randonnées et promenades à Macugnaga ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : du Dorf aux bois et sentiers sous le Monte Rosa vous trouvez promenades et randonnées douces, idéales pour familles et pour vivre la montagne depuis le village. Réservez des expériences outdoor sur la page Expériences du portail."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga est-elle encore une vraie montagne, avec lieux caractéristiques et anciens chalets ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui. Le village a conservé architecture traditionnelle, anciens chalets, beau paysage et panoramas sur le Monte Rosa : un village alpin authentique, parmi les plus beaux des Alpes (Bandiera Arancione du Touring Club Italiano), à vivre depuis le centre et les sentiers."
            }
          },
          {
            "@type": "Question",
            "name": "Macugnaga convient-elle pour un week-end de vraie montagne, proche de Milan, Novara, Varese et des villes de la plaine ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Oui : environ 2 heures depuis Milan et environ 1,5 heure depuis Novara et Varese, aussi accessible depuis le lac Majeur, Turin, la plaine du Pô et la Suisse. Idéale pour sorties et week-ends hors ville. Voir Week-end et Fuite de la ville."
            }
          }''',
"de": '''          {
            "@type": "Question",
            "name": "Eignet sich Macugnaga als Familienberg und Berg mit Kindern?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja. Macugnaga ist ein familienfreundlicher Bergort: leichte Wege, ein einladendes Dorf und geführte Erlebnisse ohne technischen Alpinismus. Siehe die Seite Familien und die Aktivitäten des Buchungsportals."
            }
          },
          {
            "@type": "Question",
            "name": "Ist Macugnaga ein Bergziel für Paare und Freundesgruppen?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: Bergstille, Monte-Rosa-Panoramen, Spaziergänge und Naturerlebnisse machen es ideal für ein romantisches Paarwochenende oder eine Auszeit mit Freunden. Siehe die Seiten Paare und Wochenende auf dem Portal."
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
              "text": "Ja: vom Dorf zu Wäldern und Wegen unter dem Monte Rosa finden Sie Spaziergänge und sanfte Wanderungen, ideal für Familien und alle, die die Berge vom Ort aus erleben wollen. Buchen Sie Outdoor-Erlebnisse auf der Seite Erlebnisse des Portals."
            }
          },
          {
            "@type": "Question",
            "name": "Ist Macugnaga noch echter Berg, mit charaktervollen Orten und alten Chalets?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja. Der Ort hat traditionelle Architektur, alte Chalets, schöne Landschaft und Monte-Rosa-Panoramen bewahrt: ein authentisches Alpendorf, unter den schönsten der Alpen (Bandiera Arancione des Touring Club Italiano), erlebbar vom Zentrum und den Wegen aus."
            }
          },
          {
            "@type": "Question",
            "name": "Eignet sich Macugnaga für ein echtes Bergwochenende, nah an Mailand, Novara, Varese und den Städten der Ebene?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja: etwa 2 Stunden ab Mailand und etwa 1,5 Stunden ab Novara und Varese, auch erreichbar vom Lago Maggiore, Turin, der Po-Ebene und der Schweiz. Ideal für Ausflüge und Wochenenden außerhalb der Stadt. Siehe Wochenende und Stadtflucht."
            }
          }''',
}

FAMIGLIE_FAQ = {
"en": '''  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Is Macugnaga suitable as a mountain destination with children?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes: Macugnaga is among the most accessible family mountains of Monte Rosa — easy routes, a child-friendly village, guided experiences and qualified operators. Ideal also for day trips or weekends from Milan, Lake Maggiore, Varese and Novara."
        }
      },
      {
        "@type": "Question",
        "name": "Which family experiences can you book?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Soft nature outings, a visit to the Walser House Museum, the gold mine (level route, including with a pushchair), gold panning and other booking-portal activities. Check age and difficulty on each experience sheet."
        }
      },
      {
        "@type": "Question",
        "name": "How do you organise a mountain weekend with children?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Choose accommodation in Macugnaga, book online one or two experiences suited to little ones and combine village walks, nature and, if you like, ski lifts. See the Families and Weekend pages on the booking portal."
        }
      }
    ]
  }''',
"fr": '''  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Macugnaga convient-elle comme destination de montagne avec enfants ?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Oui : Macugnaga compte parmi les montagnes familiales les plus accessibles du Monte Rosa — parcours faciles, village adapté aux enfants, expériences guidées et opérateurs qualifiés. Idéale aussi pour sorties ou week-ends depuis Milan, le lac Majeur, Varese et Novara."
        }
      },
      {
        "@type": "Question",
        "name": "Quelles expériences familiales peut-on réserver ?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sorties nature douces, visite de la Maison-musée Walser, mine d’or (parcours de plain-pied, y compris avec poussette), recherche de l’or et autres activités du portail. Vérifiez âge et difficulté sur la fiche de chaque expérience."
        }
      },
      {
        "@type": "Question",
        "name": "Comment organiser un week-end en montagne avec enfants ?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Choisissez un hébergement à Macugnaga, réservez en ligne une ou deux expériences adaptées aux petits et combinez promenades au village, nature et, si vous voulez, remontées. Consultez les pages Familles et Week-end du portail."
        }
      }
    ]
  }''',
"de": '''  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Eignet sich Macugnaga als Bergziel mit Kindern?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Ja: Macugnaga zählt zu den zugänglichsten Familienbergen des Monte Rosa — leichte Wege, kinderfreundliches Dorf, geführte Erlebnisse und qualifizierte Anbieter. Ideal auch für Tagesausflüge oder Wochenenden ab Mailand, Lago Maggiore, Varese und Novara."
        }
      },
      {
        "@type": "Question",
        "name": "Welche Familienerlebnisse kann man buchen?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sanfte Naturausflüge, Besuch des Walser-Hausmuseums, Goldmine (ebene Strecke, auch mit Kinderwagen), Goldwaschen und weitere Portal-Aktivitäten. Prüfen Sie Alter und Schwierigkeit auf dem Blatt jedes Erlebnisses."
        }
      },
      {
        "@type": "Question",
        "name": "Wie organisiert man ein Bergwochenende mit Kindern?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Wählen Sie eine Unterkunft in Macugnaga, buchen Sie online ein oder zwei für Kleine geeignete Erlebnisse und kombinieren Sie Dorfspaziergänge, Natur und bei Bedarf Bergbahnen. Siehe die Seiten Familien und Wochenende auf dem Buchungsportal."
        }
      }
    ]
  }''',
}


def replace_first_ld(path: Path, new_ld: str) -> None:
    text = path.read_text(encoding="utf-8")
    m = LD_RE.search(text)
    if not m:
        raise SystemExit(f"No JSON-LD in {path}")
    path.write_text(text[: m.start()] + new_ld.strip() + text[m.end() :], encoding="utf-8")


def replace_faqpage_mainentity(path: Path, new_entity: str) -> None:
    text = path.read_text(encoding="utf-8")
    pat = re.compile(
        r'("@type":\s*"FAQPage",\s*"mainEntity":\s*\[)(.*?)(\]\s*\}\s*\]\s*\}\s*</script>)',
        re.S,
    )
    m = pat.search(text)
    if not m:
        raise SystemExit(f"FAQPage mainEntity not found in {path}")
    path.write_text(text[: m.start(2)] + "\n" + new_entity + "\n        " + text[m.start(3) :], encoding="utf-8")


def replace_standalone_faq(path: Path, new_json: str) -> None:
    text = path.read_text(encoding="utf-8")
    # last or FAQ-only script
    scripts = list(LD_RE.finditer(text))
    target = None
    for m in scripts:
        if '"FAQPage"' in m.group(0) and '"@graph"' not in m.group(0):
            target = m
            break
    if not target:
        raise SystemExit(f"Standalone FAQPage not found in {path}")
    block = f'<script type="application/ld+json">\n{new_json.strip()}\n  </script>'
    path.write_text(text[: target.start()] + block + text[target.end() :], encoding="utf-8")


def main() -> None:
    for lang in ("en", "fr", "de"):
        replace_first_ld(ROOT / lang / "miniera-oro.html", MINIERA[lang])
        print(f"miniera ld {lang}: ok")
        replace_first_ld(ROOT / lang / "casa-museo-walser.html", CASA[lang])
        print(f"casa ld {lang}: ok")
        replace_first_ld(ROOT / lang / "funivia-seggiovia.html", FUNIVIA[lang])
        print(f"funivia ld {lang}: ok")
        n = patch_strings(ROOT / lang / "miniera-oro.html", VISIBLE.get(lang, []))
        n += patch_strings(ROOT / lang / "casa-museo-walser.html", VISIBLE.get(lang, []))
        n += patch_strings(ROOT / lang / "funivia-seggiovia.html", VISIBLE.get(lang, []))
        n += patch_strings(ROOT / lang / "chi-siamo.html", VISIBLE.get(lang, []))
        n += patch_strings(ROOT / lang / "scopri-macugnaga.html", VISIBLE.get(lang, []))
        print(f"visible patches {lang}: {n}")
        replace_faqpage_mainentity(ROOT / lang / "scopri-macugnaga.html", SCOPRI_FAQ_LD[lang])
        print(f"scopri FAQ ld {lang}: ok")
        replace_standalone_faq(ROOT / lang / "famiglie.html", FAMIGLIE_FAQ[lang])
        print(f"famiglie FAQ ld {lang}: ok")


if __name__ == "__main__":
    main()
