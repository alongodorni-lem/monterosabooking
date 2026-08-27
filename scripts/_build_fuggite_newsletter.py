#!/usr/bin/env python3
"""Build Mailchimp HTML + plain-text + ZIP for 9–30 agosto 2026 newsletter.

For the LEM/Grotta «codice personalizzato» footer (logo + CTA), use
scripts/_mailchimp_footer.py — see .cursor/rules/mailchimp-newsletter-footer.mdc.
"""
from __future__ import annotations

import html
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).resolve().parent / "_fuggite_newsletter_data.json"
OUT_DIR = ROOT / "assets" / "mailchimp" / "newsletter-fuggite-dal-caldo-9-30-agosto-2026"
OUT_HTML = OUT_DIR / "newsletter-fuggite-dal-caldo-9-30-agosto-2026.html"
OUT_TXT = OUT_DIR / "newsletter-fuggite-dal-caldo-9-30-agosto-2026.txt"
OUT_ZIP = ROOT / "assets" / "mailchimp" / "newsletter-fuggite-dal-caldo-9-30-agosto-2026.zip"

SITE = "https://www.macugnagabooking.it"
ESPERIENZE = f"{SITE}/esperienze.html"
LOGO = f"{SITE}/assets/web/logo-mountain-experience.png"
HERO = f"{SITE}/assets/web/landing-agosto-aria-fresca-800.jpg"
REFCODE = "grotta"

PHOTO_SITE = {
    "252382": f"{SITE}/assets/web/forest-bathing-800.jpg",
    "253390": f"{SITE}/assets/web/forest-bathing-800.jpg",
    "252705": f"{SITE}/assets/web/miniera-hero-800.jpg",
    "253398": f"{SITE}/assets/web/casa-museo-hero-800.jpg",
    "252697": f"{SITE}/assets/web/folletti-museo.jpg",
    "253399": f"{SITE}/assets/web/exp-ricerca-oro-800.jpg",
    "252702": f"{SITE}/assets/web/vecchio-dorf-800.jpg",
    "253477": f"{SITE}/assets/web/casa-museo-hero-800.jpg",
    "252700": f"{SITE}/assets/web/proposte-montagna-800.jpg",
    "252699": f"{SITE}/assets/web/trekking-salute-800.jpg",
    "253421": f"{SITE}/assets/web/exp-escursioni-via-del-pane-800.jpg",
    "252698": f"{SITE}/assets/web/casa-museo-pane.jpg",
    "253658": f"{SITE}/assets/web/funivia-belvedere.jpg",
    "253679": f"{SITE}/assets/web/funivia-alpe-bill.jpg",
    "253656": f"{SITE}/assets/web/exp-montagna-per-tutti-800.jpg",
    "253657": f"{SITE}/assets/web/trekking-salute-800.jpg",
}

GREEN = "#4a6b3e"
GREEN_DARK = "#2f4522"
GREEN_MID = "#3d5834"
CREAM = "#f7f5f0"
TEXT = "#2a2a2a"
MUTED = "#5c5c5c"
ACCENT_BTN = "#72872B"

INTRO = (
    "Fuggite dal caldo: Grotta di Babbo Natale ha selezionato per voi le più belle "
    "esperienze ai piedi del Monte Rosa. Per tutta la famiglia. Posti limitati prenota subito online"
)


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def short_name(name: str) -> str:
    n = (name or "").strip()
    replacements = {
        "MacugnYOGA ... Mente, corpo e anima al centro del cuore del Monte Rosa!": "MacugnYOGA",
        "Miniera d’Oro della Guia - visita alla miniera nel cuore della montagna": "Miniera d’Oro della Guia",
        "Visita Casa Museo Walser di Macugnaga - la vita di una volta": "Casa Museo Walser",
        "Passeggiata con vera guida walser,  tra storia e tradizione walser": "Passeggiata con guida Walser",
        "Macugnaga nel ’900: viaggio nella perla del Monte Rosa": "Macugnaga nel ’900",
        "Alla ricerca dell’oro in Val Quarazza Lago delle Fate": "Alla ricerca dell’oro – Val Quarazza",
        "La via del pane, tra borghi, storia e sapori di montagna": "La via del pane",
        "Nel cuore dei Walser: pane, camino e folletti di Macugnaga": "Nel cuore dei Walser",
        "Respira il bosco: Forest Bathing (PER ADULTI DA 12 ANNI)": "Forest Bathing (adulti da 12 anni)",
        "Respira il bosco: Forest Bathing (PER TUTTI)": "Forest Bathing (per tutti)",
        "Trekking del Benessere sul Sentiero della Salute": "Trekking del Benessere",
        "Seggiovia Pecetto - Burki - Belvedere": "Seggiovia Pecetto–Belvedere",
        "Funivie Macugnaga Staffa  - Alpe Bill": "Funivia Staffa–Alpe Bill",
        "Alpigiano per un giorno": "Alpigiano per un giorno",
        "Trekking a Villa Aprilia": "Trekking a Villa Aprilia",
    }
    return replacements.get(n, n)


def experience_block(it: dict) -> str:
    rid = str(it["resourceId"])
    name = short_name(it["name"])
    desc = it.get("description") or ""
    dates = " · ".join(it.get("dateLabels") or [])
    photo = PHOTO_SITE.get(rid) or it.get("photo") or ""
    detail = it.get("detailUrl") or it.get("cta") or ESPERIENZE
    reserve = it.get("reserveUrl") or detail
    note = it.get("deadlineNote") or ""

    img_row = ""
    if photo:
        img_row = f"""
              <tr>
                <td style="padding:0 0 14px 0;">
                  <a href="{esc(detail)}" target="_blank" style="text-decoration:none;">
                    <img src="{esc(photo)}" width="536" alt="{esc(name)}" style="display:block;width:100%;max-width:536px;height:auto;border:0;border-radius:4px;" />
                  </a>
                </td>
              </tr>"""

    note_row = ""
    if note:
        note_row = f"""
                      <tr>
                        <td style="font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.4;color:#8a4b1a;font-weight:bold;padding:0 0 10px 0;">
                          {esc(note)}
                        </td>
                      </tr>"""

    return f"""
          <tr>
            <td style="padding:0 0 28px 0;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#ffffff;border:1px solid #e2e6de;border-radius:6px;">
                <tr>
                  <td style="padding:20px 22px 22px 22px;">
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
{img_row}
                      <tr>
                        <td style="font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:1.3;color:{GREEN_DARK};font-weight:bold;padding:0 0 8px 0;">
                          {esc(name)}
                        </td>
                      </tr>
                      <tr>
                        <td style="font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.4;color:{GREEN};font-weight:bold;padding:0 0 10px 0;">
                          {esc(dates)}
                        </td>
                      </tr>
{note_row}
                      <tr>
                        <td style="font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.55;color:{MUTED};padding:0 0 16px 0;">
                          {esc(desc)}
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                            <tr>
                              <td bgcolor="{GREEN}" style="border-radius:4px;">
                                <a href="{esc(detail)}" target="_blank" style="display:inline-block;padding:12px 20px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;background:{GREEN};">
                                  Scopri
                                </a>
                              </td>
                              <td width="10" style="font-size:0;line-height:0;">&nbsp;</td>
                              <td bgcolor="{ACCENT_BTN}" style="border-radius:4px;">
                                <a href="{esc(reserve)}" target="_blank" style="display:inline-block;padding:12px 20px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;background:{ACCENT_BTN};">
                                  Prenota
                                </a>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>"""


def build_html(items: list[dict]) -> str:
    blocks = "\n".join(experience_block(it) for it in items)
    return f"""<!DOCTYPE html>
<html lang="it" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="light" />
  <title>Fuggite dal caldo · Macugnaga 9–30 agosto 2026</title>
  <!--
    Mailchimp-ready template. Paste into Campaign → Code your own / Import HTML.
    Merge tags: *|UNSUB|*  *|HTML:LIST_ADDRESS_HTML|*  *|MC:SUBJECT|*
    Refcode: {REFCODE}
  -->
</head>
<body style="margin:0;padding:0;background-color:{CREAM};-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;">
  <div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">
    {esc(INTRO)}
  </div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{CREAM};">
    <tr>
      <td align="center" style="padding:24px 12px;">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;">

          <!-- Brand bar -->
          <tr>
            <td bgcolor="{GREEN_DARK}" style="background:{GREEN_DARK};padding:22px 24px;border-radius:6px 6px 0 0;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td align="left" valign="middle" style="padding:0;">
                    <a href="{SITE}/" target="_blank" style="text-decoration:none;">
                      <img src="{LOGO}" width="72" height="72" alt="Mountain Experience Monterosa" style="display:block;border:0;width:72px;height:auto;" />
                    </a>
                  </td>
                  <td align="left" valign="middle" style="padding:0 0 0 14px;font-family:Georgia,'Times New Roman',serif;">
                    <div style="font-size:20px;line-height:1.25;color:#ffffff;font-weight:bold;">Macugnaga Booking</div>
                    <div style="font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.35;color:#d7e2d0;padding-top:4px;">Mountain Experience Monterosa</div>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Date range -->
          <tr>
            <td bgcolor="{GREEN}" style="background:{GREEN};padding:14px 24px;">
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.4;color:#ffffff;font-weight:bold;text-align:center;">
                Esperienze prenotabili · 9–30 agosto 2026
              </p>
            </td>
          </tr>

          <!-- Hero -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:0;">
              <a href="{ESPERIENZE}" target="_blank" style="text-decoration:none;">
                <img src="{HERO}" width="600" alt="Macugnaga ai piedi del Monte Rosa" style="display:block;width:100%;max-width:600px;height:auto;border:0;" />
              </a>
            </td>
          </tr>

          <!-- Intro -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:26px 24px 8px 24px;">
              <p style="margin:0 0 12px 0;font-family:Georgia,'Times New Roman',serif;font-size:22px;line-height:1.3;color:{GREEN_DARK};">
                Fuggite dal caldo
              </p>
              <p style="margin:0 0 20px 0;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.55;color:{TEXT};">
                {esc(INTRO)}
              </p>
            </td>
          </tr>

          <!-- Experiences -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:0 24px 8px 24px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
{blocks}
              </table>
            </td>
          </tr>

          <!-- Global CTA -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:8px 24px 28px 24px;text-align:center;">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center">
                <tr>
                  <td bgcolor="{GREEN_DARK}" style="border-radius:4px;">
                    <a href="{ESPERIENZE}" target="_blank" style="display:inline-block;padding:14px 28px;font-family:Arial,Helvetica,sans-serif;font-size:15px;font-weight:bold;color:#ffffff;text-decoration:none;background:{GREEN_DARK};border-radius:4px;">
                      Vedi tutte le esperienze
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td bgcolor="{GREEN_MID}" style="background:{GREEN_MID};padding:22px 24px;border-radius:0 0 6px 6px;">
              <p style="margin:0 0 10px 0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;color:#ffffff;text-align:center;">
                <a href="{SITE}/" target="_blank" style="color:#ffffff;text-decoration:underline;">www.macugnagabooking.it</a>
                &nbsp;·&nbsp;
                <a href="{ESPERIENZE}" target="_blank" style="color:#ffffff;text-decoration:underline;">Esperienze</a>
              </p>
              <p style="margin:0 0 10px 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.45;color:#dce5d6;text-align:center;">
                Macugnaga Booking – Mountain Experience Monterosa<br />
                Portale di prenotazione esperienze a Macugnaga, ai piedi del Monte Rosa.
              </p>
              <p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:1.45;color:#c5d1bc;text-align:center;">
                Non vuoi più ricevere queste email? <a href="*|UNSUB|*" style="color:#ffffff;text-decoration:underline;">Annulla iscrizione</a>
              </p>
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:1.45;color:#c5d1bc;text-align:center;">
                *|HTML:LIST_ADDRESS_HTML|*
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""


def build_txt(items: list[dict]) -> str:
    lines = [
        "MACUGNAGA BOOKING – Mountain Experience Monterosa",
        "Fuggite dal caldo · Esperienze 9–30 agosto 2026",
        "",
        INTRO,
        "",
        f"Tutte le esperienze: {ESPERIENZE}",
        "",
        "—" * 40,
        "",
    ]
    for it in items:
        name = short_name(it["name"])
        dates = ", ".join(it.get("dateLabels") or [])
        desc = it.get("description") or ""
        detail = it.get("detailUrl") or ESPERIENZE
        reserve = it.get("reserveUrl") or detail
        note = it.get("deadlineNote") or ""
        lines.extend(
            [
                name,
                f"Date: {dates}",
            ]
        )
        if note:
            lines.append(note)
        if desc:
            lines.append(desc)
        lines.extend(
            [
                f"Scopri: {detail}",
                f"Prenota: {reserve}",
                "",
                "—" * 40,
                "",
            ]
        )
    lines.extend(
        [
            f"Tutte le esperienze: {ESPERIENZE}",
            f"Sito: {SITE}/",
            "",
            "Annulla iscrizione: *|UNSUB|*",
            "*|HTML:LIST_ADDRESS_HTML|*",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    items = json.loads(DATA.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    html_doc = build_html(items)
    txt_doc = build_txt(items)
    OUT_HTML.write_text(html_doc, encoding="utf-8")
    OUT_TXT.write_text(txt_doc, encoding="utf-8")

    with zipfile.ZipFile(OUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(OUT_HTML, OUT_HTML.name)
        zf.write(OUT_TXT, OUT_TXT.name)

    print(f"Wrote {OUT_HTML}")
    print(f"Wrote {OUT_TXT}")
    print(f"Wrote {OUT_ZIP}")
    print(f"Experiences: {len(items)}")
    print(f"Refcode: {REFCODE}")
    for it in items:
        print(f"  - [{it['resourceId']}] {short_name(it['name'])}: {', '.join(it['dateLabels'])}")


if __name__ == "__main__":
    main()
