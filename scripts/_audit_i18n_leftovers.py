# -*- coding: utf-8 -*-
"""Audit EN/FR/DE HTML for likely Italian leftovers."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Strong Italian markers (avoid common proper nouns where possible)
MARKERS = re.compile(
    r"(?:"
    r"\be dal\b|\banche\b|\bsul\b|\bsulla\b|\bsulle\b|\bsui\b|"
    r"\bdella\b|\bdelle\b|\bdello\b|\bdegli\b|\bdei\b|"
    r"\bnella\b|\bnelle\b|\bnel\b|\bnei\b|"
    r"\bCome\b|\bQuali\b|\bSì\b|\bÈ\b|"
    r"\bportale di prenotazione\b|\bPortale di prenotazione\b|"
    r"\bprenotare\b|\bprenotazione\b|\bprenota online\b|"
    r"\bVedi\b|\bScopri\b|\bIdeale per\b|\bSoggiorni\b|"
    r"\bEscursione\b|\bPasseggiate\b|\bgite\b|"
    r"\ba contatto\b|\bmontagna vera\b|\bcuore delle\b|"
    r"\bTraduzione automatica\b|"
    r"\braggiungibil|\bda Torino\b|"
    r"\bPerché\b|\bPuoi prenotare\b|"
    r"\besperienze\b|\besperienza\b|"
    r"\bL’estate\b|\bAlba e tramonto\b|"
    r"\bOrganizza una gita\b|\bCosa prenotare\b|"
    r"\bBenessere in montagna\b|"
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
    r"id=\"prenota|"
    r"planyo_lang|"
    r"Bandiera Arancione",
    re.I,
)


def audit_lang(lang: str) -> list[tuple[str, int, str]]:
    root = ROOT / lang
    findings: list[tuple[str, int, str]] = []
    for path in sorted(root.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if not MARKERS.search(line):
                continue
            # strip allowed tokens then re-check
            cleaned = ALLOW.sub("", line)
            if MARKERS.search(cleaned):
                findings.append((str(path.relative_to(ROOT)), i, line.strip()[:160]))
    return findings


def main() -> None:
    for lang in ("en", "fr", "de"):
        hits = audit_lang(lang)
        print(f"\n=== {lang.upper()}: {len(hits)} suspect lines ===")
        by_file: dict[str, int] = {}
        for f, _, _ in hits:
            by_file[f] = by_file.get(f, 0) + 1
        for f, n in sorted(by_file.items(), key=lambda x: -x[1]):
            print(f"  {n:3d}  {f}")
        for f, i, line in hits[:40]:
            print(f"    {f}:{i}: {line}")
        if len(hits) > 40:
            print(f"    ... +{len(hits) - 40} more")


if __name__ == "__main__":
    main()
