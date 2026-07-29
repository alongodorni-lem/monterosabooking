"""Photorealistic 16:9 editorial collage from Macugnaga real photos. No text."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "promo-sources"
OUT_MAIL = ROOT / "assets" / "mailchimp" / "macugnaga-booking-social-16x9.png"
OUT_WEB = ROOT / "assets" / "web" / "macugnaga-booking-social-16x9.png"

W, H = 1920, 1080
GAP = 10
PAD = 14
SHADOW_BLUR = 12
SHADOW_OFFSET = (4, 5)
SHADOW_ALPHA = 88
BORDER = 3


def cover_crop(im: Image.Image, tw: int, th: int, focus=(0.5, 0.4)) -> Image.Image:
    im = im.convert("RGB")
    sw, sh = im.size
    scale = max(tw / sw, th / sh)
    nw, nh = max(1, int(round(sw * scale))), max(1, int(round(sh * scale)))
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    fx, fy = focus
    left = int(round(fx * nw - tw / 2))
    top = int(round(fy * nh - th / 2))
    left = max(0, min(left, nw - tw))
    top = max(0, min(top, nh - th))
    return im.crop((left, top, left + tw, top + th))


def soft_upscale(im: Image.Image, tw: int, th: int, focus=(0.5, 0.45)) -> Image.Image:
    out = cover_crop(im, tw, th, focus)
    sw, sh = im.size
    ratio = max(tw / sw, th / sh)
    if ratio > 2.2:
        out = out.filter(ImageFilter.GaussianBlur(0.45))
        out = out.filter(ImageFilter.UnsharpMask(radius=1.3, percent=90, threshold=2))
    elif ratio > 1.4:
        out = out.filter(ImageFilter.UnsharpMask(radius=1.0, percent=75, threshold=3))
    return out


def harmonize(im: Image.Image, brightness=1.0, contrast=1.05, color=1.06) -> Image.Image:
    im = ImageEnhance.Brightness(im).enhance(brightness)
    im = ImageEnhance.Contrast(im).enhance(contrast)
    im = ImageEnhance.Color(im).enhance(color)
    return im


def panel_with_shadow(canvas: Image.Image, panel: Image.Image, xy: tuple[int, int]) -> None:
    x, y = xy
    pw, ph = panel.size
    shadow = Image.new("RGBA", (pw + SHADOW_BLUR * 4, ph + SHADOW_BLUR * 4), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    ox = SHADOW_BLUR * 2 + SHADOW_OFFSET[0]
    oy = SHADOW_BLUR * 2 + SHADOW_OFFSET[1]
    sd.rectangle([ox, oy, ox + pw - 1, oy + ph - 1], fill=(0, 0, 0, SHADOW_ALPHA))
    shadow = shadow.filter(ImageFilter.GaussianBlur(SHADOW_BLUR))
    canvas.alpha_composite(shadow, (x - SHADOW_BLUR * 2, y - SHADOW_BLUR * 2))

    framed = Image.new("RGBA", (pw, ph), (255, 255, 255, 255))
    framed.paste(panel.convert("RGBA"), (0, 0))
    draw = ImageDraw.Draw(framed)
    draw.rectangle([0, 0, pw - 1, ph - 1], outline=(255, 255, 255, 230), width=BORDER)
    canvas.alpha_composite(framed, (x, y))


def main() -> None:
    # Bottom strip experiences (real photos only)
    trek = harmonize(Image.open(SRC / "02-dorf.png"), 1.03, 1.08, 1.05)  # Via del Pane / escursioni
    gold = harmonize(Image.open(SRC / "07-gold.png"), 1.04, 1.06, 1.08)  # ricerca oro
    mine = harmonize(Image.open(SRC / "03-mine.png"), 1.08, 1.06, 0.98)
    forest = harmonize(Image.open(SRC / "04-forest.png"), 1.03, 1.04, 1.04)
    monte = harmonize(Image.open(SRC / "05-monte-rosa.png"), 1.04, 1.12, 1.06)
    lago = harmonize(Image.open(SRC / "06-lago-fate.png"), 1.02, 1.09, 1.09)

    canvas = Image.new("RGBA", (W, H), (14, 24, 32, 255))

    # Dual hero band — Monte Rosa summer LEFT (protagonist), Lago RIGHT (also Rosa)
    # Keep #5 panel moderate width so upscale stays ~3x, not ~7x.
    hero_h = 700
    hero_y = PAD
    inner_w = W - 2 * PAD
    monte_w = int(inner_w * 0.46)  # protagonist, left
    lago_w = inner_w - monte_w - GAP

    hero_monte = soft_upscale(monte, monte_w, hero_h, focus=(0.52, 0.4))
    hero_lago = soft_upscale(lago, lago_w, hero_h, focus=(0.48, 0.36))

    panel_with_shadow(canvas, hero_monte, (PAD, hero_y))
    panel_with_shadow(canvas, hero_lago, (PAD + monte_w + GAP, hero_y))

    # Bottom experience strip
    strip_top = hero_y + hero_h + GAP + 2
    strip_h = H - strip_top - PAD
    strip_w = W - 2 * PAD
    n = 4
    panel_w = (strip_w - GAP * (n - 1)) // n

    # Bottom: trekking/Via del Pane | ricerca oro | mine | forest bathing
    bottom = [
        soft_upscale(trek, panel_w, strip_h, focus=(0.5, 0.42)),
        soft_upscale(gold, panel_w, strip_h, focus=(0.5, 0.42)),
        soft_upscale(mine, panel_w, strip_h, focus=(0.5, 0.42)),
        soft_upscale(forest, panel_w, strip_h, focus=(0.58, 0.48)),
    ]
    x = PAD
    for p in bottom:
        panel_with_shadow(canvas, p, (x, strip_top))
        x += panel_w + GAP

    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    for i, a in enumerate((24, 14, 8, 0)):
        m = i * 16
        vd.rectangle([m, m, W - 1 - m, H - 1 - m], outline=(0, 0, 0, a), width=16)
    vignette = vignette.filter(ImageFilter.GaussianBlur(22))
    canvas = Image.alpha_composite(canvas, vignette)

    out = canvas.convert("RGB")
    OUT_MAIL.parent.mkdir(parents=True, exist_ok=True)
    OUT_WEB.parent.mkdir(parents=True, exist_ok=True)
    out.save(OUT_MAIL, "PNG", optimize=True)
    out.save(OUT_WEB, "PNG", optimize=True)
    print(f"Saved {OUT_MAIL} ({out.size[0]}x{out.size[1]})")
    print(f"Copied {OUT_WEB}")


if __name__ == "__main__":
    main()
