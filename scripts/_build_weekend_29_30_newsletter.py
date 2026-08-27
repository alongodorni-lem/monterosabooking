#!/usr/bin/env python3
"""Build Mailchimp «codice personalizzato» for weekend 29–30 agosto 2026."""
from __future__ import annotations

import html
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).resolve().parent / "_weekend_29_30_newsletter_data.json"
MAIL = ROOT / "assets" / "mailchimp"
BASENAME = "newsletter-weekend-29-30-agosto-2026-codice-personalizzato"
OUT_HTML = MAIL / f"{BASENAME}.html"
OUT_FOLDER = MAIL / BASENAME
OUT_FOLDER_HTML = OUT_FOLDER / f"{BASENAME}.html"
OUT_ZIP = MAIL / f"{BASENAME}.zip"

SITE = "https://www.macugnagabooking.it"
HOSPITALITY_URL = "https://macugnaga-monterosa.it/contenuti/306635/dove-dormire"
FOLLETTI_PHOTO = f"{SITE}/assets/web/folletti-museo-walser-collage.jpg"
HOSP_PHOTO = f"{SITE}/assets/web/ossola-macugnaga-800.jpg"
GROTTA_LOGO = f"{SITE}/assets/web/logo-grotta-babbo-natale.png?v=2"
LEM_LOGO = f"{SITE}/assets/web/logo-lem-eventi.png"
FEATURED_ID = "252697"

GREEN = "#4a6b3e"
GREEN_DARK = "#2f4522"
CREAM = "#f7f5f0"
MUTED = "#5c5c5c"
ACCENT_BTN = "#72872B"

SHORT = {
    "MacugnYOGA ... Mente, corpo e anima al centro del cuore del Monte Rosa!": "MacugnYOGA",
    "Miniera d’Oro della Guia - visita alla miniera nel cuore della montagna": "Miniera d’Oro della Guia",
    "Visita Casa Museo Walser di Macugnaga - la vita di una volta": "Casa Museo Walser",
    "Passeggiata con vera guida walser,  tra storia e tradizione walser": "Passeggiata con guida Walser",
    "Piccoli folletti al Museo Walser": "Piccoli Folletti al Museo Walser",
    "Seggiovia Pecetto - Burki - Belvedere": "Seggiovia Pecetto–Belvedere",
    "Funivie Macugnaga Staffa  - Alpe Bill": "Funivia Staffa–Alpe Bill",
    "Trekking a Villa Aprilia": "Trekking a Villa Aprilia",
}


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def short_name(name: str) -> str:
    return SHORT.get((name or "").strip(), (name or "").strip())


def prenota(rid: str, mode: str) -> str:
    return (
        f"{SITE}/prenota.html?resource_id={rid}"
        f"&amp;mode={mode}&amp;ppp_refcode=grotta&amp;planyo_lang=IT"
    )


def list_row(it: dict) -> str:
    rid = str(it["resourceId"])
    name = short_name(it["name"])
    href = prenota(rid, "resource_desc")
    return f"""                      <tr>
                        <td style="padding:0 0 12px 0;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.45;color:#202020;">
                          <a href="{href}" target="_blank" style="color:{GREEN_DARK};font-weight:bold;text-decoration:underline;">{esc(name)}</a>
                        </td>
                      </tr>"""


def build_html(items: list[dict]) -> str:
    featured = next((i for i in items if str(i["resourceId"]) == FEATURED_ID), None)
    if not featured:
        raise SystemExit(f"Featured resource {FEATURED_ID} missing from data")

    list_items = items  # all weekend titles, including featured
    list_rows = "\n".join(list_row(it) for it in list_items)

    feat_detail = prenota(FEATURED_ID, "resource_desc")
    feat_reserve = prenota(FEATURED_ID, "reserve")
    feat_dates = " · ".join(featured.get("dateLabels") or ["Sabato 29 agosto"])

    title = "Sabato 29 e domenica 30 agosto, goditi la montagna (19-22 gradi!)"
    preview = (
        "Sabato 29 e domenica 30 agosto a Macugnaga: Piccoli Folletti al Museo Walser, "
        "esperienze e aria fresca (19-22 gradi). Prenota con Grotta di Babbo Natale."
    )

    return f"""<!DOCTYPE html>
<html lang="it" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="light" />
  <title>Weekend 29–30 agosto · Macugnaga · Grotta di Babbo Natale</title>
  <!--
    Mailchimp «Codice personalizzato» / Code your own.
    Import: Campaign → Email → Code your own → Import HTML (this single file),
    or paste the full document into the custom HTML editor.
    Subject: set in Mailchimp UI (optional merge tag *|MC:SUBJECT|*).
    Merge tags in footer: *|UNSUB|*  *|HTML:LIST_ADDRESS_HTML|*
    Images: absolute https:// only · Layout: tables + inline CSS · Width ~600px
    Refcode: grotta
  -->
</head>
<body style="margin:0;padding:0;background-color:{CREAM};-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;">
  <div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">
    {esc(preview)}
  </div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{CREAM};">
    <tr>
      <td align="center" style="padding:24px 12px;">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;">

          <!-- Header: Grotta di Babbo Natale -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:20px 24px 12px 24px;border-radius:6px 6px 0 0;text-align:center;">
              <a href="https://www.grottadibabbonatale.it/" target="_blank" style="text-decoration:none;">
                <img src="{GROTTA_LOGO}" width="180" height="180" alt="La Grotta di Babbo Natale – Tutto l'anno" style="display:block;margin:0 auto;border:0;width:180px;max-width:50%;height:auto;" />
              </a>
            </td>
          </tr>
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:22px 24px 10px 24px;">
              <p style="margin:0 0 14px 0;font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:1.4;color:#1a1a1a;text-align:center;font-weight:bold;">
                {esc(title)}
              </p>
              <p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.45;color:{MUTED};text-align:center;">
                <a href="{SITE}/" target="_blank" style="color:{GREEN};text-decoration:underline;">www.macugnagabooking.it</a> è un progetto dell'Unione Montana Valli dell'Ossola sviluppato da Grotta di Babbo Natale (Lem s.r.l.)
              </p>
            </td>
          </tr>
          <tr>
            <td bgcolor="{GREEN}" style="background:{GREEN};padding:14px 24px;">
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.4;color:#ffffff;font-weight:bold;text-align:center;">
                Weekend a Macugnaga · 29–30 agosto 2026
              </p>
            </td>
          </tr>

          <!-- Block 1: Featured Folletti -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:24px 0 8px 0;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#ffffff;border:1px solid #e2e6de;border-radius:6px;">
                <tr>
                  <td style="padding:0;">
                    <a href="{feat_detail}" target="_blank" style="text-decoration:none;">
                      <img src="{FOLLETTI_PHOTO}" width="600" alt="Piccoli Folletti al Museo Walser – collage Casa Museo" style="display:block;width:100%;max-width:600px;height:auto;border:0;border-radius:6px 6px 0 0;" />
                    </a>
                  </td>
                </tr>
                <tr>
                  <td style="padding:20px 24px 22px 24px;">
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td style="font-family:Georgia,'Times New Roman',serif;font-size:22px;line-height:1.3;color:{GREEN_DARK};font-weight:bold;padding:0 0 8px 0;">
                          Piccoli Folletti al Museo Walser
                        </td>
                      </tr>
                      <tr>
                        <td style="font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.4;color:{GREEN};font-weight:bold;padding:0 0 12px 0;">
                          {esc(feat_dates)}
                        </td>
                      </tr>
                      <tr>
                        <td bgcolor="#e8f0e4" style="background:#e8f0e4;border-left:4px solid {GREEN};padding:12px 14px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.45;color:{GREEN_DARK};font-weight:bold;">
                          Laboratorio per i bambini SOLO 10 euro — Adulti ingresso e visita Casa Museo euro 4,50
                        </td>
                      </tr>
                      <tr>
                        <td style="font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.55;color:{MUTED};padding:14px 0 16px 0;">
                          Una bella iniziativa per tutta la famiglia: laboratorio creativo per bambini al Museo Walser di Borca, tra leggende, costumi e magia alpina. Un pomeriggio speciale da vivere insieme, nel cuore di Macugnaga.
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                            <tr>
                              <td bgcolor="{GREEN}" style="border-radius:4px;">
                                <a href="{feat_detail}" target="_blank" style="display:inline-block;padding:12px 20px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;background:{GREEN};">
                                  Scopri
                                </a>
                              </td>
                              <td width="10" style="font-size:0;line-height:0;">&nbsp;</td>
                              <td bgcolor="{ACCENT_BTN}" style="border-radius:4px;">
                                <a href="{feat_reserve}" target="_blank" style="display:inline-block;padding:12px 20px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;background:{ACCENT_BTN};">
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
          </tr>

          <!-- Block 2: weekend titles -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:20px 24px 8px 24px;">
              <p style="margin:0 0 10px 0;font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:1.35;color:{GREEN_DARK};font-weight:bold;text-align:left;">
                Un week end ricco di attività a Macugnaga
              </p>
              <p style="margin:0 0 16px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.55;color:#333333;text-align:left;">
                Non solo Casa Walser e Antica Miniera d’oro… non immagini quante attività puoi fare nello stesso weekend. Ecco le attività disponibili: scegli quella che preferisci o semplicemente vieni a rilassarti ai piedi del Monte Rosa. La montagna vera è vicina.
              </p>
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
{list_rows}
              </table>
            </td>
          </tr>

          <!-- Block 3: hospitality -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:20px 24px 28px 24px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#ffffff;border:1px solid #e2e6de;border-radius:6px;">
                <tr>
                  <td style="padding:20px 22px 22px 22px;">
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td style="padding:0 0 14px 0;">
                          <a href="{esc(HOSPITALITY_URL)}" target="_blank" style="text-decoration:none;">
                            <img src="{HOSP_PHOTO}" width="536" alt="Dove dormire a Macugnaga" style="display:block;width:100%;max-width:536px;height:auto;border:0;border-radius:4px;" />
                          </a>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:1.3;color:{GREEN_DARK};font-weight:bold;padding:0 0 10px 0;">
                          In giornata oppure per uno splendido week end: qui tutte le info
                        </td>
                      </tr>
                      <tr>
                        <td style="font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.55;color:{MUTED};padding:0 0 16px 0;">
                          Hotel, B&amp;B e case vacanza a Macugnaga: consulta l’elenco aggiornato sul portale ufficiale Macugnaga-Monterosa e organizza la tua giornata o il tuo weekend ai piedi del Monte Rosa.
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                            <tr>
                              <td bgcolor="{GREEN}" style="border-radius:4px;">
                                <a href="{esc(HOSPITALITY_URL)}" target="_blank" style="display:inline-block;padding:12px 20px;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:4px;background:{GREEN};">
                                  Dove dormire
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
          </tr>

          <!-- Footer LEM / Grotta -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:24px 20px 16px 20px;border-top:1px solid #e8e8e8;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td width="180" valign="middle" align="left" style="padding:0 12px 0 0;">
                    <a href="https://www.grottadibabbonatale.it/organizzazione-eventi-per-famiglie" target="_blank" style="text-decoration:none;">
                      <img src="{LEM_LOGO}" width="160" alt="LEM Eventi e comunicazione" style="display:block;border:0;width:160px;max-width:100%;height:auto;" />
                    </a>
                  </td>
                  <td valign="middle" align="left" style="padding:0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.45;color:#202020;">
                    <em style="font-style:italic;">Grotta di Babbo Natale è un marchio di Lem s.r.l. di Verbania, grandi eventi per bambini e famiglie in tutto il Nord Italia.</em><br />
                    <a href="https://www.grottadibabbonatale.it/organizzazione-eventi-per-famiglie" target="_blank" style="color:#0066cc;font-weight:normal;text-decoration:underline;">Clicca qui per conoscerci meglio</a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td bgcolor="#404040" style="background:#404040;padding:16px 20px;">
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;color:#ffffff;text-align:center;">
                Scopri <a href="https://www.raccontidigitali.it/" target="_blank" style="color:#ffffff;font-weight:bold;text-decoration:underline;">WWW.RACCONTIDIGITALI.IT</a> il digital lab di LEM Comunicazione: uno spazio dedicato alla progettazione di eventi, esperienze phygital, esperienze digitali, Intelligenza artificiale e web app per enti ed operatori. Comunicazione, sviluppo, animazioni, spettacoli e noleggi.
              </p>
            </td>
          </tr>
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:18px 20px 10px 20px;">
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;color:#202020;text-align:left;">
                <strong>PUOI CONTATTARE LA NOSTRA SEGRETERIA ALL'EMAIL</strong><br />
                <a href="mailto:info@grottadibabbonatale.it" style="color:#D12027;font-weight:bold;text-decoration:none;">INFO@GROTTADIBABBONATALE.IT</a>
                <span style="color:#202020;"> – La segreteria per le informazioni a mezzo telefono <strong>0323 497349</strong>, tutti i giorni da lunedì a venerdì 8:30–12:30</span>
              </p>
            </td>
          </tr>
          <tr>
            <td bgcolor="#f0eeea" style="background:#f0eeea;padding:16px 20px;border-radius:0 0 6px 6px;">
              <p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:1.45;color:#666666;text-align:center;">
                Prenotazioni esperienze: <a href="{SITE}/" target="_blank" style="color:{GREEN};text-decoration:underline;">www.macugnagabooking.it</a> · progetto Unione Montana Valli dell'Ossola / Grotta di Babbo Natale (Lem s.r.l.)
              </p>
              <p style="margin:0 0 6px 0;font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:1.45;color:#666666;text-align:center;">
                Non vuoi più ricevere queste email? <a href="*|UNSUB|*" style="color:#333333;text-decoration:underline;">Annulla iscrizione</a>
              </p>
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:1.45;color:#888888;text-align:center;">
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


def main() -> None:
    items = json.loads(DATA.read_text(encoding="utf-8"))
    html_doc = build_html(items)
    MAIL.mkdir(parents=True, exist_ok=True)
    OUT_FOLDER.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(html_doc, encoding="utf-8")
    OUT_FOLDER_HTML.write_text(html_doc, encoding="utf-8")
    with zipfile.ZipFile(OUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(f"{BASENAME}.html", html_doc.encode("utf-8"))
    print(
        json.dumps(
            {
                "html": str(OUT_HTML),
                "folder": str(OUT_FOLDER_HTML),
                "zip": str(OUT_ZIP),
                "count": len(items),
                "featured": FEATURED_ID,
                "hospitality": HOSPITALITY_URL,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
