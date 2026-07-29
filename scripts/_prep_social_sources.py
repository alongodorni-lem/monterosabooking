"""Crop card text / extract panels into assets/promo-sources for the social collage."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CURSOR_ASSETS = Path(
    r"C:\Users\along\.cursor\projects"
    r"\c-Users-along-Documents-attivit-2026-macugnaga-macugnaga-booking-cursor"
    r"\assets"
)
DEST = ROOT / "assets" / "promo-sources"


def crop_card_photo(im: Image.Image) -> Image.Image:
    """Remove white footer text area from experience cards."""
    rgb = im.convert("RGB")
    arr = np.asarray(rgb)
    h, w = arr.shape[:2]
    cut = h
    for y in range(int(h * 0.45), h):
        row = arr[y]
        white = (row.min(axis=1) > 225) & (row.mean(axis=1) > 240)
        if float(white.mean()) > 0.72:
            cut = y
            break
    cut = max(int(h * 0.35), cut - 2)
    left, right = 0, w
    for x in range(w // 4):
        col = arr[:cut, x]
        if float((col.min(axis=1) > 225).mean()) > 0.9:
            left = x + 1
        else:
            break
    for x in range(w - 1, w * 3 // 4, -1):
        col = arr[:cut, x]
        if float((col.min(axis=1) > 225).mean()) > 0.9:
            right = x
        else:
            break
    top = 0
    for y in range(min(40, cut // 8)):
        if float((arr[y].min(axis=1) > 225).mean()) > 0.85:
            top = y + 1
        else:
            break
    return rgb.crop((left, top, right, cut))


def save(im: Image.Image, name: str) -> None:
    path = DEST / name
    im.convert("RGB").save(path, "PNG", optimize=True)
    print(f"{name}: {im.size}")


def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    g = {
        "gold_card": CURSOR_ASSETS
        / "c__Users_along_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images__D4D22F64-0163-498A-946D-9A5E26428BFC_-e7b9b568-8d31-4756-b839-d1f7892c8b0d.png",
        "gold_collage": CURSOR_ASSETS
        / "c__Users_along_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images_ricerca_oro_valquarazza_macugnagabooking-18cd5ef6-6086-424d-b375-d4fedd273fc5.png",
        "forest_wide": CURSOR_ASSETS
        / "c__Users_along_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images_fabrizio_cutro_rallenta_respira-ad5bd86c-cb04-48bf-ac26-b4a5097b9248.png",
        "forest_card": CURSOR_ASSETS
        / "c__Users_along_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images__DBD17B77-812B-40CD-9309-5674AEF61AA7_-d813fbe4-e4de-4230-ac64-b90cfe6d3e47.png",
        "trek_card": CURSOR_ASSETS
        / "c__Users_along_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images__8F8ABB8C-7794-48CE-8CE4-57C4AD792FC6_-130ffe06-6e34-4de7-b44c-93f4fe1f7b30.png",
        "via_pane": CURSOR_ASSETS
        / "c__Users_along_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images_viaadelpane-cebbb6dd-164a-4225-81bd-97fbdb92f97f.png",
    }
    for k, p in g.items():
        if not p.exists():
            raise SystemExit(f"Missing source {k}: {p}")

    # Ricerca oro: family panning (text cropped). Keep wool as separate file.
    gold = crop_card_photo(Image.open(g["gold_card"]))
    save(gold, "07-gold.png")
    gc = Image.open(g["gold_collage"]).convert("RGB")
    gw, gh = gc.size
    # Center gold-pan circle inset from Val Quarazza collage
    pan = gc.crop((int(gw * 0.30), int(gh * 0.22), int(gw * 0.70), int(gh * 0.82)))
    save(pan, "07-gold-pan.png")

    # Forest bathing: wide landscape primary
    save(Image.open(g["forest_wide"]).convert("RGB"), "04-forest.png")
    save(crop_card_photo(Image.open(g["forest_card"])), "04-forest-alt.png")

    # Escursioni / Via del Pane: central hikers only (exclude collage insets)
    vp = Image.open(g["via_pane"]).convert("RGB")
    vw, vh = vp.size
    hikers = vp.crop((int(vw * 0.30), int(vh * 0.10), int(vw * 0.68), int(vh * 0.72)))
    save(hikers, "02-dorf.png")  # trekking slot (replaces prior dorf path)
    save(crop_card_photo(Image.open(g["trek_card"])), "02-trekking-card.png")

    print("Done prep.")


if __name__ == "__main__":
    main()
