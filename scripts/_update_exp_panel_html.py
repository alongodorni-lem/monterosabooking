"""Point EN/FR/DE homepage experience panels at new exp-* images."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = [
    (
        'srcset="../assets/web/forest-bathing-800.webp 800w, ../assets/web/forest-bathing-1200.webp 1200w, ../assets/web/forest-bathing.webp 800w" sizes="100vw">\n'
        '          <img src="../assets/web/forest-bathing.jpg" srcset="../assets/web/forest-bathing-800.jpg 800w, ../assets/web/forest-bathing-1200.jpg 1200w, ../assets/web/forest-bathing.jpg 800w" sizes="100vw"',
        'srcset="../assets/web/exp-benessere-boschi-800.webp 800w, ../assets/web/exp-benessere-boschi-1200.webp 1200w, ../assets/web/exp-benessere-boschi.webp 1200w" sizes="(max-width:720px) 100vw, 33vw">\n'
        '          <img src="../assets/web/exp-benessere-boschi.jpg" srcset="../assets/web/exp-benessere-boschi-800.jpg 800w, ../assets/web/exp-benessere-boschi-1200.jpg 1200w, ../assets/web/exp-benessere-boschi.jpg 1200w" sizes="(max-width:720px) 100vw, 33vw"',
    ),
    (
        'srcset="../assets/web/trekking-salute-800.webp 800w, ../assets/web/trekking-salute-1200.webp 1200w, ../assets/web/trekking-salute.webp 1600w" sizes="100vw">\n'
        '          <img src="../assets/web/trekking-salute.jpg" srcset="../assets/web/trekking-salute-800.jpg 800w, ../assets/web/trekking-salute-1200.jpg 1200w, ../assets/web/trekking-salute.jpg 1600w" sizes="100vw" alt="Trekking salutista sui sentieri di Macugnaga"',
        'srcset="../assets/web/exp-escursioni-via-del-pane-800.webp 800w, ../assets/web/exp-escursioni-via-del-pane-1200.webp 1200w, ../assets/web/exp-escursioni-via-del-pane.webp 1200w" sizes="(max-width:720px) 100vw, 33vw">\n'
        '          <img src="../assets/web/exp-escursioni-via-del-pane.jpg" srcset="../assets/web/exp-escursioni-via-del-pane-800.jpg 800w, ../assets/web/exp-escursioni-via-del-pane-1200.jpg 1200w, ../assets/web/exp-escursioni-via-del-pane.jpg 1200w" sizes="(max-width:720px) 100vw, 33vw" alt="Escursione Via del Pane a Macugnaga"',
    ),
]

MINE_ALTS = {
    "en": "Gold mine visitabile a Macugnaga",
    "fr": "Mine d’or visitabile a Macugnaga",
    "de": "Goldmine visitabile a Macugnaga",
}
GOLD_ALTS = {
    "en": "Families che cercano oro al torrente con Monte Rosa",
    "fr": "Familles che cercano oro al torrente con Monte Rosa",
    "de": "Familien che cercano oro al torrente con Monte Rosa",
}


def picture_block(stem: str, alt: str) -> str:
    return (
        '<div class="exp-card__img"><picture>\n'
        f'          <source type="image/webp" srcset="../assets/web/{stem}-800.webp 800w, ../assets/web/{stem}-1200.webp 1200w, ../assets/web/{stem}.webp 1200w" sizes="(max-width:720px) 100vw, 33vw">\n'
        f'          <img src="../assets/web/{stem}.jpg" srcset="../assets/web/{stem}-800.jpg 800w, ../assets/web/{stem}-1200.jpg 1200w, ../assets/web/{stem}.jpg 1200w" sizes="(max-width:720px) 100vw, 33vw" alt="{alt}" width="600" height="450" loading="lazy" decoding="async">\n'
        "        </picture></div>"
    )


def main() -> None:
    for lang in ("en", "fr", "de"):
        path = ROOT / lang / "index.html"
        text = path.read_text(encoding="utf-8")
        for old, new in REPLACEMENTS:
            if old not in text:
                raise SystemExit(f"Missing block in {path}")
            text = text.replace(old, new, 1)

        old_mine = (
            f'<div class="exp-card__img"><img src="../assets/web/miniera-foto-11.jpg" '
            f'alt="{MINE_ALTS[lang]}" width="600" height="450" loading="lazy"></div>'
        )
        if old_mine not in text:
            raise SystemExit(f"Missing mine img in {path}")
        text = text.replace(old_mine, picture_block("exp-miniera-visita", MINE_ALTS[lang]), 1)

        old_gold = (
            f'<div class="exp-card__img"><img src="../assets/web/ricerca-oro.jpg" '
            f'alt="{GOLD_ALTS[lang]}" width="600" height="450" loading="lazy"></div>'
        )
        if old_gold not in text:
            raise SystemExit(f"Missing gold img in {path}")
        text = text.replace(old_gold, picture_block("exp-ricerca-oro", GOLD_ALTS[lang]), 1)

        path.write_text(text, encoding="utf-8")
        print(f"updated {path}")


if __name__ == "__main__":
    main()
