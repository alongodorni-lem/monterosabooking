#!/usr/bin/env python3
"""Shared Mailchimp newsletter footer constants + HTML snippet.

Standard (do not invent alternatives unless explicitly asked):
- LEM logo → https://raccontidigitali.it/chi-siamo.html
- CTA «Scopri i nostri eventi per tutta la famiglia» → https://www.grottadibabbonatale.it/
- Keep credit line, raccontidigitali bar, segreteria hours lun–ven 8:30–12:30
- No «ferie» line unless asked
"""
from __future__ import annotations

SITE = "https://www.macugnagabooking.it"
LEM_LOGO_URL = f"{SITE}/assets/web/logo-lem-eventi.png"
LEM_LOGO_HREF = "https://raccontidigitali.it/chi-siamo.html"
GROTTA_HOME_URL = "https://www.grottadibabbonatale.it/"
GROTTA_CTA_TEXT = "Scopri i nostri eventi per tutta la famiglia"
RACCONTI_URL = "https://www.raccontidigitali.it/"
SEGRETERIA_EMAIL = "info@grottadibabbonatale.it"
SEGRETERIA_PHONE = "0323 497349"
SEGRETERIA_HOURS = "tutti i giorni da lunedì a venerdì 8:30–12:30"

CREDIT_LINE = (
    "Grotta di Babbo Natale è un marchio di Lem s.r.l. di Verbania, "
    "grandi eventi per bambini e famiglie in tutto il Nord Italia."
)

RACCONTI_BAR = (
    f'Scopri <a href="{RACCONTI_URL}" target="_blank" '
    'style="color:#ffffff;font-weight:bold;text-decoration:underline;">'
    "WWW.RACCONTIDIGITALI.IT</a> il digital lab di LEM Comunicazione: "
    "uno spazio dedicato alla progettazione di eventi, esperienze phygital, "
    "esperienze digitali, Intelligenza artificiale e web app per enti ed operatori. "
    "Comunicazione, sviluppo, animazioni, spettacoli e noleggi."
)


def footer_lem_block(*, green: str = "#4a6b3e", include_project_credit: bool = True) -> str:
    """Return the standard LEM / Grotta / segreteria / unsubscribe footer rows."""
    project = ""
    if include_project_credit:
        project = (
            f' · progetto Unione Montana Valli dell\'Ossola / Grotta di Babbo Natale (Lem s.r.l.)'
        )
    return f"""          <!-- Footer LEM / Grotta -->
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:24px 20px 16px 20px;border-top:1px solid #e8e8e8;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td width="180" valign="middle" align="left" style="padding:0 12px 0 0;">
                    <a href="{LEM_LOGO_HREF}" target="_blank" rel="noopener noreferrer" style="text-decoration:none;">
                      <img src="{LEM_LOGO_URL}" width="160" alt="LEM Eventi e comunicazione" style="display:block;border:0;width:160px;max-width:100%;height:auto;" />
                    </a>
                  </td>
                  <td valign="middle" align="left" style="padding:0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.45;color:#202020;">
                    <em style="font-style:italic;">{CREDIT_LINE}</em><br />
                    <a href="{GROTTA_HOME_URL}" target="_blank" rel="noopener noreferrer" style="color:#0066cc;font-weight:normal;text-decoration:underline;">{GROTTA_CTA_TEXT}</a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td bgcolor="#404040" style="background:#404040;padding:16px 20px;">
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;color:#ffffff;text-align:center;">
                {RACCONTI_BAR}
              </p>
            </td>
          </tr>
          <tr>
            <td bgcolor="#ffffff" style="background:#ffffff;padding:18px 20px 10px 20px;">
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;color:#202020;text-align:left;">
                <strong>PUOI CONTATTARE LA NOSTRA SEGRETERIA ALL'EMAIL</strong><br />
                <a href="mailto:{SEGRETERIA_EMAIL}" style="color:#D12027;font-weight:bold;text-decoration:none;">INFO@GROTTADIBABBONATALE.IT</a>
                <span style="color:#202020;"> – La segreteria per le informazioni a mezzo telefono <strong>{SEGRETERIA_PHONE}</strong>, {SEGRETERIA_HOURS}</span>
              </p>
            </td>
          </tr>
          <tr>
            <td bgcolor="#f0eeea" style="background:#f0eeea;padding:16px 20px;border-radius:0 0 6px 6px;">
              <p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:1.45;color:#666666;text-align:center;">
                Prenotazioni esperienze: <a href="{SITE}/" target="_blank" style="color:{green};text-decoration:underline;">www.macugnagabooking.it</a>{project}
              </p>
              <p style="margin:0 0 6px 0;font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:1.45;color:#666666;text-align:center;">
                Non vuoi più ricevere queste email? <a href="*|UNSUB|*" style="color:#333333;text-decoration:underline;">Annulla iscrizione</a>
              </p>
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:1.45;color:#888888;text-align:center;">
                *|HTML:LIST_ADDRESS_HTML|*
              </p>
            </td>
          </tr>"""


def footer_cta_plain() -> str:
    """Plain-text CTA line for .txt companions."""
    return f"{GROTTA_CTA_TEXT}: {GROTTA_HOME_URL}"
