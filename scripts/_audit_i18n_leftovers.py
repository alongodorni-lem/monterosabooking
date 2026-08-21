# -*- coding: utf-8 -*-
"""Audit EN/FR/DE HTML for likely Italian leftovers.

Focuses on strong Italian phrases (FAQ/schema/meta) and skips common false
positives from Italian filenames in href/canonical URLs (esperienze.html, etc.).
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Strong Italian markers (avoid common proper nouns where possible)
MARKERS = re.compile(
    r"(?:"
    r"\be dal\b|\banche\b|\bsul\b|\bsulla\b|\bsulle\b|\bsui\b|"
    r"\bdella\b|\bdelle\b|\bdello\b|\bdegli\b|\bdei\b|"
    r"\bnella\b|\bnelle\b|\bnel\b|\bnei\b|"
    r"\bCome prenot|\bCome organizz|\bQuali\b|\bSì\b|\bÈ\b|"
    r"\bportale di prenotazione\b|\bPortale di prenotazione\b|"
    r"\bprenotare\b|\bprenotazione\b|\bprenota online\b|"
    r"\bVedi le\b|\bScopri\b|\bIdeale per\b|\bSoggiorni\b|"
    r"\bEscursione\b|\bPasseggiate\b|\bgite\b|"
    r"\ba contatto\b|\bmontagna vera\b|\bcuore delle\b|"
    r"\bTraduzione automatica\b|"
    r"\braggiungibil|\bda Torino\b|"
    r"\bPerché\b|\bPuoi prenotare\b|"
    r"\bL’estate\b|\bAlba e tramonto\b|"
    r"\bOrganizza una gita\b|\bCosa prenotare\b|\bCosa si\b|\bCosa portare\b|"
    r"\bBenessere in montagna\b|"
    r"\bQuanto dura\b|\bNei pressi\b|\bNella stagione\b|\bNella frazione\b|"
    r"\bfiloni auriferi\b|\bgallerie illuminate\b|\bvisita guidata\b|"
    r"\bprenotabile online\b|\bospitato nella\b|\bcasa parrocchiale\b|"
    r"\bRaccoglie e preserva\b|\bmestieri tradizionali\b|"
    r"\bStampe e mostre\b|\bfocolare-cucina\b|\bColoni alemanni\b|"
    r"\bGarantisci l\b|\bSì, previo\b|\bAlloggio a\b|"
    r"\bUscite soft\b|\bNatura e gioco\b|\bInfo pratiche\b|"
    r"\bper le famiglie\b|\bcon passeggino\b|\bricerca dell.oro\b|"
    r"\binLanguage\":\s*\"it-IT\""
    r")",
    re.I,
)

# Allowed Italian proper-noun / fixed phrases in non-IT pages
ALLOW = re.compile(
    r"Madonna della Neve|Lago delle Locce|Lago delle Fate|"
    r"Unione Montana|Valle Anzasca|Casa Museo Walser|"
    r"Via del Pane|Pianura Padana|Touring Club Italiano|"
    r"Alts Walserhüüs|Dorf|Borca|Staffa|Pecetto|"
    r"href=\"[^\"]*prenota\.html|"
    r"href=\"[^\"]*esperienze|"
    r"id=\"prenota|"
    r"planyo_lang|"
    r"Bandiera Arancione|"
    r"Miniera della Guia|"
    r"come-funziona\.html|"
    r"scopri-macugnaga\.html",
    re.I,
)

# Filename / URL false positives (Italian path segments without Italian prose)
URLISH = re.compile(
    r"https?://[^\s\"']+|href=\"[^\"]+\"|canonical|hreflang|og:url|twitter:url",
    re.I,
)


def audit_lang(lang: str, *, strong_only: bool = False) -> list[tuple[str, int, str]]:
    root = ROOT / lang
    findings: list[tuple[str, int, str]] = []
    for path in sorted(root.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if not MARKERS.search(line):
                continue
            cleaned = ALLOW.sub("", line)
            cleaned = URLISH.sub("", cleaned)
            if not MARKERS.search(cleaned):
                continue
            # Drop bare "esperienze" in English "Experiences" nav when only from filename leftovers
            if strong_only and not re.search(
                r"Come prenot|Puoi prenotare|Quanto dura|Cosa |Nei pressi|Nella |"
                r"prenotabile|visita guidata|gallerie illuminate|filoni |"
                r"ospitato|casa parrocchiale|Raccoglie|mestieri tradizionali|"
                r"Stampe e mostre|focolare|Coloni alemanni|Garantisci|"
                r"Sì, previo|Alloggio a|Uscite soft|Natura e gioco|Info pratiche|"
                r"per le famiglie|con passeggino|ricerca dell|Vedi le|"
                r"portale di prenotazione|Perché|inLanguage\":\s*\"it-IT\"|"
                r"Macugnaga è |percorsi facili|villaggio|passeggiate in paese",
                cleaned,
                re.I,
            ):
                continue
            findings.append((str(path.relative_to(ROOT)), i, line.strip()[:160]))
    return findings


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--strong",
        action="store_true",
        help="Only report high-confidence Italian prose leftovers",
    )
    args = ap.parse_args()
    for lang in ("en", "fr", "de"):
        hits = audit_lang(lang, strong_only=args.strong)
        mode = "strong" if args.strong else "all"
        print(f"\n=== {lang.upper()} ({mode}): {len(hits)} suspect lines ===")
        by_file: dict[str, int] = {}
        for f, _, _ in hits:
            by_file[f] = by_file.get(f, 0) + 1
        for f, n in sorted(by_file.items(), key=lambda x: -x[1]):
            print(f"  {n:3d}  {f}")
        for f, i, line in hits[:50]:
            print(f"    {f}:{i}: {line}")
        if len(hits) > 50:
            print(f"    ... +{len(hits) - 50} more")


if __name__ == "__main__":
    main()
