#!/usr/bin/env python3
"""Collect Planyo experiences with availability 2026-08-09..2026-08-30."""
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
START = "2026-08-09"
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
        return re.sub(r"^http://", "https://", u, flags=re.I)
    if u.startswith("/"):
        return "https://www.planyo.com" + u
    if re.match(r"^\d+_", u) or re.search(r"\.(jpe?g|png|webp|gif)(\?|$)", u, re.I):
        if "/" not in u:
            return "https://planyo-ch.s3.eu-central-2.amazonaws.com/" + u
        return "https://www.planyo.com/" + u.lstrip("./")
    return ""


def first_photo(r: dict, rid: str) -> str:
    for entry in as_list(r.get("photos")):
        if isinstance(entry, str):
            url = absolute_media(entry)
        elif isinstance(entry, dict):
            url = absolute_media(
                entry.get("path")
                or entry.get("url")
                or entry.get("src")
                or entry.get("image")
                or ""
            )
        else:
            url = ""
        if url:
            return url
    props = r.get("properties") or {}
    if isinstance(props, dict):
        url = absolute_media(
            props.get("image")
            or props.get("Image")
            or props.get("photo")
            or props.get("picture")
            or ""
        )
        if url:
            return url
    return PHOTO_FALLBACKS.get(str(rid), "")


def parse_ymd_token(s: str) -> str | None:
    s = str(s or "").strip()
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", s)
    if m:
        d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return f"{y:04d}-{mo:02d}-{d:02d}"
    return None


def ymd_from_event(ev) -> str | None:
    if isinstance(ev, str):
        return parse_ymd_token(ev)
    if not isinstance(ev, dict):
        return None
    for k in ("start_time", "start", "start_date", "date", "begin", "end_time"):
        v = ev.get(k)
        if v is None or v == "":
            continue
        s = str(v)
        ymd = parse_ymd_token(s)
        if ymd:
            return ymd
        try:
            ts = int(float(s))
            if ts > 1e9:
                return datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")
        except (TypeError, ValueError):
            pass
    return None


def days_from_event_dates(s: str) -> list[str]:
    if not s:
        return []
    days = []
    for part in str(s).split(","):
        ymd = parse_ymd_token(part)
        if ymd:
            days.append(ymd)
    return days


def format_it(ymd: str) -> str:
    d = datetime.strptime(ymd, "%Y-%m-%d")
    label = f"{WD[d.weekday()]} {d.day} {MO[d.month]}"
    return label[0].upper() + label[1:]


def in_window(ymd: str) -> bool:
    return START <= ymd <= END


def window_day_count() -> int:
    a = datetime.strptime(START, "%Y-%m-%d")
    b = datetime.strptime(END, "%Y-%m-%d")
    return (b - a).days + 1


def is_special(rid: str, name: str) -> bool:
    if str(rid) in SPECIAL_IDS:
        return True
    n = (name or "").lower()
    if "casa museo walser" in n:
        return True
    if "miniera" in n and "guia" in n:
        return True
    if "miniera d'oro" in n or "miniera d’oro" in n:
        return True
    return False


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
    """Return compact label if dense schedule; else None to list dates."""
    if not days:
        return None
    n = window_day_count()
    if len(days) >= n - 1:
        return "Tutti i giorni · 9–30 agosto"
    if len(days) >= max(10, int(n * 0.65)):
        return "Quasi tutti i giorni · 9–30 agosto"
    return None


def date_labels_for(rid: str, name: str, days: list[str], special: bool, pinned: bool) -> list[str]:
    if pinned:
        return ["Tutti i giorni · 9–30 agosto"]
    if special and not days:
        return ["Tutti i giorni · 9–30 agosto"]
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
        # Exclude zero availability (unless special/pinned daily)
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
        # Pin lifts near top among daily items
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
    out = Path(__file__).resolve().parent / "_fuggite_newsletter_data.json"
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
