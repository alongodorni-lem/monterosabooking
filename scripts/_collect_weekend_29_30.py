#!/usr/bin/env python3
"""Collect Planyo experiences with availability 2026-08-29..2026-08-30."""
from __future__ import annotations

import html as html_mod
import json
import re
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from pathlib import Path

BASE = "http://127.0.0.1:8765/api/planyo"
LIVE = "https://www.macugnagabooking.it/api/planyo"
SITE = "70864"
START = "2026-08-29"
END = "2026-08-30"
REFCODE = "grotta"
SITE_URL = "https://www.macugnagabooking.it"

# Always-bookable / daily ticket style
SPECIAL_IDS = {"253398", "252705"}  # Casa Walser, Miniera
PINNED_DAILY_IDS = {"253658", "253679"}  # Seggiovia Belvedere, Funivia Alpe Bill
DEADLINE_IDS = {"253421"}
PHOTO_FALLBACKS = {
    "252382": f"{SITE_URL}/assets/web/forest-bathing.jpg",
    "253390": f"{SITE_URL}/assets/web/forest-bathing.jpg",
    "252705": f"{SITE_URL}/assets/web/miniera-hero.jpg",
    "253398": f"{SITE_URL}/assets/web/casa-museo-hero.jpg",
    "252697": f"{SITE_URL}/assets/web/folletti-museo.jpg",
    "252699": f"{SITE_URL}/assets/web/trekking-salute.jpg",
    "253399": f"{SITE_URL}/assets/web/ricerca-oro.jpg",
    "253421": f"{SITE_URL}/assets/web/casa-museo-pane.jpg",
    "253658": f"{SITE_URL}/assets/web/funivia-belvedere.jpg",
    "253679": f"{SITE_URL}/assets/web/funivia-alpe-bill.jpg",
    "252702": f"{SITE_URL}/assets/web/vecchio-dorf.jpg",
    "253477": f"{SITE_URL}/assets/web/casa-walser.jpg",
    "252700": f"{SITE_URL}/assets/web/proposte-montagna.jpg",
}
WD = [
    "lunedì",
    "martedì",
    "mercoledì",
    "giovedì",
    "venerdì",
    "sabato",
    "domenica",
]
MO = [
    "",
    "gennaio",
    "febbraio",
    "marzo",
    "aprile",
    "maggio",
    "giugno",
    "luglio",
    "agosto",
    "settembre",
    "ottobre",
    "novembre",
    "dicembre",
]


def pick_base() -> str:
    for b in (LIVE, BASE):
        try:
            api(b, {"method": "api_test"})
            return b
        except Exception as exc:  # noqa: BLE001
            print("base fail", b, exc, file=sys.stderr)
    raise SystemExit("No Planyo API reachable")


def api(base: str, params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(base + "?" + q, headers={"User-Agent": "macugnaga-newsletter/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def as_list(results):
    if not results:
        return []
    if isinstance(results, list):
        return results
    if isinstance(results, dict):
        return list(results.values())
    return []


def strip_html(s: str) -> str:
    s = re.sub(r"<script[\s\S]*?</script>", " ", s or "", flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html_mod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def truncate(t: str, maxn: int = 180) -> str:
    t = (t or "").strip()
    if len(t) <= maxn:
        return t
    cut = t[: maxn - 1]
    sp = cut.rfind(" ")
    if sp > int(maxn * 0.6):
        cut = cut[:sp]
    return cut.rstrip(".,;: ") + "…"


def absolute_media(raw: str) -> str:
    u = (raw or "").strip()
    if not u or u in ("null", "undefined"):
        return ""
    if u.startswith("//"):
        u = "https:" + u
    if re.match(r"^https?://", u, re.I):
        return u
    if u.startswith("/"):
        return SITE_URL + u
    return u


def first_photo(r: dict, rid: str) -> str:
    for k in ("image", "image_path", "photos", "images"):
        v = r.get(k)
        if isinstance(v, str) and v.strip():
            return absolute_media(v)
        if isinstance(v, list) and v:
            item = v[0]
            if isinstance(item, str):
                return absolute_media(item)
            if isinstance(item, dict):
                for kk in ("url", "path", "image", "src"):
                    if item.get(kk):
                        return absolute_media(str(item[kk]))
    props = r.get("properties") or {}
    if isinstance(props, dict):
        for k in ("image", "photo", "immagine"):
            if props.get(k):
                return absolute_media(str(props[k]))
    return PHOTO_FALLBACKS.get(str(rid), f"{SITE_URL}/assets/web/landing-agosto-aria-fresca-800.jpg")


def parse_ymd(s: str) -> str | None:
    s = (s or "").strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.match(r"^(\d{2})-(\d{2})-(\d{4})", s)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    m = re.match(r"^(\d{2})/(\d{2})/(\d{4})", s)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    return None


def in_window(ymd: str) -> bool:
    return START <= ymd <= END


def window_day_count() -> int:
    a = datetime.strptime(START, "%Y-%m-%d").date()
    b = datetime.strptime(END, "%Y-%m-%d").date()
    return (b - a).days + 1


def format_it(ymd: str) -> str:
    d = datetime.strptime(ymd, "%Y-%m-%d").date()
    return f"{WD[d.weekday()]} {d.day} {MO[d.month]}".capitalize()


def days_from_event_dates(raw: str) -> list[str]:
    days = []
    for part in re.split(r"[,;\s]+", raw or ""):
        ymd = parse_ymd(part)
        if ymd:
            days.append(ymd)
    return days


def ymd_from_event(ev) -> str | None:
    if isinstance(ev, str):
        return parse_ymd(ev)
    if isinstance(ev, dict):
        for k in ("start_time", "start", "date", "day", "event_date"):
            if ev.get(k):
                ymd = parse_ymd(str(ev[k]))
                if ymd:
                    return ymd
    return None


def is_special(rid: str, name: str) -> bool:
    if str(rid) in SPECIAL_IDS:
        return True
    n = re.sub(r"\s+", " ", (name or "").lower())
    return "miniera" in n or "casa museo walser" in n or "visita casa museo" in n


def is_pinned_daily(rid: str) -> bool:
    return str(rid) in PINNED_DAILY_IDS


def has_deadline(rid: str, name: str) -> bool:
    if str(rid) in DEADLINE_IDS:
        return True
    return "via del pane" in re.sub(r"\s+", " ", (name or "").lower())


def resource_name(r: dict) -> str:
    return (r.get("translated_name") or r.get("name") or "").strip()


def resource_desc(r: dict) -> str:
    for k in (
        "translated_description",
        "description",
        "short_description",
        "translated_short_description",
    ):
        v = r.get(k)
        if v:
            return truncate(strip_html(str(v)))
    props = r.get("properties") or {}
    if isinstance(props, dict):
        for k in ("description", "Descrizione", "short_description"):
            v = props.get(k)
            if v:
                return truncate(strip_html(str(v)))
    return ""


def days_from_resource(r: dict) -> list[str]:
    days = []
    for ymd in days_from_event_dates(str(r.get("event_dates") or "")):
        if in_window(ymd):
            days.append(ymd)
    return sorted(set(days))


def load_days_api(base: str, rid: str) -> list[str]:
    days: list[str] = []
    try:
        je = api(
            base,
            {
                "method": "get_event_times",
                "resource_id": rid,
                "future_only": "true",
                "format": "array",
                "language": "IT",
            },
        )
        for ev in as_list((je.get("data") or {}).get("event_times")):
            ymd = ymd_from_event(ev)
            if ymd and in_window(ymd):
                days.append(ymd)
    except Exception as exc:  # noqa: BLE001
        print("event_times fail", rid, exc, file=sys.stderr)
    return sorted(set(days))


def looks_daily(days: list[str]) -> str | None:
    if not days:
        return None
    n = window_day_count()
    if len(days) >= n:
        return "Sabato 29 e domenica 30 agosto"
    return None


def date_labels_for(rid: str, name: str, days: list[str], special: bool, pinned: bool) -> list[str]:
    if pinned:
        return ["Sabato 29 e domenica 30 agosto"]
    if special and not days:
        return ["Sabato 29 e domenica 30 agosto"]
    dense = looks_daily(days)
    if dense:
        return [dense]
    if days:
        return [format_it(d) for d in days]
    return []


def prenota_url(rid: str, mode: str) -> str:
    q = urllib.parse.urlencode(
        {
            "resource_id": rid,
            "mode": mode,
            "ppp_refcode": REFCODE,
            "planyo_lang": "IT",
        }
    )
    return f"{SITE_URL}/prenota.html?{q}"


def main() -> None:
    base = pick_base()
    print("Using API", base, file=sys.stderr)
    jr = api(
        base,
        {
            "method": "list_resources",
            "site_id": SITE,
            "detail_level": "15",
            "list_published_only": "true",
            "list_reservable_only": "true",
            "language": "IT",
            "page_size": "100",
        },
    )
    code = jr.get("response_code")
    try:
        code_i = int(code)
    except (TypeError, ValueError):
        code_i = -1
    if code_i != 0:
        raise SystemExit(f"list_resources failed: {jr}")
    resources = as_list((jr.get("data") or {}).get("resources"))
    print("resources", len(resources), file=sys.stderr)

    items = []
    need_api = []
    stubs = []
    for r in resources:
        rid = str(r.get("id") or r.get("resource_id") or "")
        name = resource_name(r)
        if not rid or not name:
            continue
        days = days_from_resource(r)
        special = is_special(rid, name)
        pinned = is_pinned_daily(rid)
        stubs.append((r, rid, name, days, special, pinned))
        if not days and not special and not pinned:
            need_api.append(rid)

    api_days: dict[str, list[str]] = {}
    if need_api:
        with ThreadPoolExecutor(max_workers=6) as ex:
            futs = {ex.submit(load_days_api, base, rid): rid for rid in need_api}
            for fut in as_completed(futs):
                rid = futs[fut]
                api_days[rid] = fut.result()

    for r, rid, name, days, special, pinned in stubs:
        if not days and rid in api_days:
            days = api_days[rid]
        if not days and not special and not pinned:
            continue
        labels = date_labels_for(rid, name, days, special, pinned)
        if not labels:
            continue
        photo = first_photo(r, rid)
        if photo.startswith("/") and not photo.startswith("//"):
            photo = SITE_URL + photo
        detail = prenota_url(rid, "resource_desc")
        reserve = prenota_url(rid, "reserve")
        sort_key = days[0] if days else ("0" + START if pinned else START)
        if pinned:
            sort_key = "0" + START + rid
        items.append(
            {
                "resourceId": rid,
                "name": name,
                "description": resource_desc(r),
                "photo": photo,
                "days": days,
                "dateLabels": labels,
                "specialAugust": bool(special and not days),
                "pinnedDaily": pinned,
                "deadlineNote": (
                    "Prenotazioni entro il 17 agosto"
                    if has_deadline(rid, name)
                    else ""
                ),
                "detailUrl": detail,
                "reserveUrl": reserve,
                "cta": detail,
                "sortKey": sort_key,
            }
        )

    items.sort(key=lambda x: (x["sortKey"], x["name"].lower()))
    out = Path(__file__).resolve().parent / "_weekend_29_30_newsletter_data.json"
    out.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"count": len(items), "refcode": REFCODE, "out": str(out)}, ensure_ascii=False))
    for it in items:
        print(
            f"- [{it['resourceId']}] {it['name']} | {', '.join(it['dateLabels'])}"
            + (f" | NOTE: {it['deadlineNote']}" if it["deadlineNote"] else ""),
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
