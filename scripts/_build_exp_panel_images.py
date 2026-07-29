"""Build optimized web images for homepage experience panels."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "assets" / "web"
CURSOR = Path(
    r"C:\Users\along\.cursor\projects"
    r"\c-Users-along-Documents-attivit-2026-macugnaga-macugnaga-booking-cursor"
    r"\assets"
)


def find_cursor(substr: str) -> Path:
    matches = [p for p in CURSOR.glob("*.png") if substr.lower() in p.name.lower()]
    if not matches:
        raise SystemExit(f"Missing cursor asset: {substr}")
    return matches[0]


def cover_crop(im: Image.Image, ratio_w: float, ratio_h: float) -> Image.Image:
    im = im.convert("RGB")
    w, h = im.size
    target = ratio_w / ratio_h
    cur = w / h
    if cur > target:
        nw = int(h * target)
        left = (w - nw) // 2
        return im.crop((left, 0, left + nw, h))
    nh = int(w / target)
    top = (h - nh) // 2
    return im.crop((0, top, w, top + nh))


def save_variants(im: Image.Image, stem: str, widths: tuple[int, ...] = (800, 1200)) -> None:
    im = im.convert("RGB")
    full_w = max(widths)
    base = im.copy()
    if base.width != full_w:
        nh = max(1, int(base.height * full_w / base.width))
        base = base.resize((full_w, nh), Image.Resampling.LANCZOS)

    jpg = WEB / f"{stem}.jpg"
    webp = WEB / f"{stem}.webp"
    base.save(jpg, "JPEG", quality=82, optimize=True, progressive=True)
    base.save(webp, "WEBP", quality=78, method=6)
    print(f"{stem}.jpg/.webp {base.size} {jpg.stat().st_size // 1024}KB")

    for w in widths:
        nh = max(1, int(base.height * w / base.width))
        variant = base.resize((w, nh), Image.Resampling.LANCZOS)
        jp = WEB / f"{stem}-{w}.jpg"
        wp = WEB / f"{stem}-{w}.webp"
        variant.save(jp, "JPEG", quality=82, optimize=True, progressive=True)
        variant.save(wp, "WEBP", quality=78, method=6)
        print(f"  {stem}-{w} {variant.size} {jp.stat().st_size // 1024}KB")


def main() -> None:
    WEB.mkdir(parents=True, exist_ok=True)

    # 1) Benessere nei boschi — Monte Rosa forest bathing promo, 4:3 card crop
    forest_src = ROOT / "assets" / "forest bathing.png"
    save_variants(cover_crop(Image.open(forest_src), 4, 3), "exp-benessere-boschi")

    # 2) Miniera — interior guided visit
    mine = cover_crop(Image.open(WEB / "miniera-interno-visita-guidata.png"), 4, 3)
    save_variants(mine, "exp-miniera-visita")

    # 3) Escursioni — Via del Pane hikers from collage (inset inward to drop white frames)
    via = Image.open(find_cursor("viaadelpane-cebbb6dd")).convert("RGB")
    vw, vh = via.size
    hikers = via.crop((int(vw * 0.32), int(vh * 0.14), int(vw * 0.66), int(vh * 0.72)))
    save_variants(cover_crop(hikers, 4, 3), "exp-escursioni-via-del-pane")

    # 4) Ricerca oro — high-res promo
    gold = cover_crop(Image.open(ROOT / "assets" / "ricerca oro val quarazza.png"), 4, 3)
    save_variants(gold, "exp-ricerca-oro")

    print("DONE")


if __name__ == "__main__":
    main()
