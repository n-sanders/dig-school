#!/usr/bin/env python3
"""Download the sourced lesson photos from Wikimedia Commons and optimize them.

Every entry records the exact Commons file, the expected reusable license,
and the local filename. The script re-checks the live license metadata and
refuses to download anything that is not public domain, CC0, CC BY or CC BY-SA.

Run:  python3 scripts/download-sourced-images.py
Output: public/images/lessons/photo-*.jpg  (max 1280px, JPEG q80)
"""

from __future__ import annotations

import html
import io
import json
import os
import re
import urllib.parse
import urllib.request

from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(REPO, "public", "images", "lessons")
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "DigSchoolLessonImages/1.0 (school project)"}

ACCEPT = ("public domain", "cc0", "cc by", "cc by-sa", "cc-by", "cc-by-sa", "pd")
REJECT = ("nc", "nd", "fair use", "copyrighted", "no known copyright")

# (commons File: title, local filename, credit author, credit license label)
PHOTOS = [
    ("Lark Quarry Dinosaur Trackways footprints.jpg",
     "photo-trackway-lark-quarry.jpg", "Carole Mackinney", "CC0 1.0"),
    ("Dunkleosteus terrelli skull and thoracic armour internal view.jpg",
     "photo-dunkleosteus-skull-armor.jpg", "Russell K. Engelman", "CC BY 4.0"),
    ("AMNH Smilodon fatalis skull, Pleistocene California.jpg",
     "photo-smilodon-skull-amnh.jpg", "Bloopityboop", "CC BY-SA 4.0"),
    ("FMIB 39502 Molar tooth of mammoth (Elephas primigenius)- a, grinding surface; b, side view.jpeg",
     "photo-mammoth-molar-plate.jpg", "George Frederick Wright", "Public domain"),
    ("FMIB 39517 Tooth of Mastodon Americanus.jpeg",
     "photo-mastodon-tooth-plate.jpg", "George Frederick Wright", "Public domain"),
    ("Fossil preparation at the Condon Center lab.jpg",
     "photo-prep-lab-condon.jpg", "John Day Fossil Beds National Monument staff (U.S. National Park Service)", "Public domain"),
    ("Massospondylus CT scans.jpg",
     "photo-massospondylus-ct.jpg", "Sereno et al., PLOS ONE (2007)", "CC BY 2.5"),
    ("Evening at the Badlands.jpg",
     "photo-badlands-evening.jpg", "MichaelKirsh", "CC BY-SA 4.0"),
    ("Symmetrical ripple marks (Berea Sandstone, Upper Devonian or Lower Mississippian; Sunbury, Ohio, USA).jpg",
     "photo-ripple-marks-berea.jpg", "James St. John", "CC BY 2.0"),
    ("Curled mudcracks (Goblin Valley, Utah, USA) 4.jpg",
     "photo-mudcracks-goblin-valley.jpg", "James St. John", "CC BY 2.0"),
    ("Cretaceous\u2013Paleogene boundary in Colorado 1.JPG",
     "photo-kpg-boundary-colorado.jpg", "Jeffrey Beall", "CC BY 4.0"),
    ("Dire Wolf Skulls La Brea 2005-08-01.JPG",
     "photo-dire-wolf-wall-la-brea.jpg", "Pyry Matikainen", "CC BY-SA 2.5"),
    ("Fossil insect (Diptera, Nematocera in Baltic amber. Age 50 Mill. years (the Lower Eocene).jpg",
     "photo-amber-fly-baltic.jpg", "Manukyan Andranik", "CC BY-SA 4.0"),
    ("USA tar bubble la brea CA.jpg",
     "photo-tar-bubble-la-brea.jpg", "Daniel Schwen", "CC BY-SA 2.5"),
    ("Baby Mammoth Lyuba.jpg",
     "photo-lyuba-mammoth.jpg", "Thomas Quine", "CC BY-SA 2.0"),
]


def clean(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def api(params: dict):
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def fetch(title: str):
    data = api({
        "action": "query", "format": "json", "titles": f"File:{title}",
        "prop": "imageinfo", "iiprop": "url|size|extmetadata",
        "iiextmetadatafilter": "LicenseShortName|Artist",
    })
    pages = (data.get("query") or {}).get("pages") or {}
    page = next(iter(pages.values()))
    info = (page.get("imageinfo") or [{}])[0]
    meta = info.get("extmetadata") or {}
    lic = clean((meta.get("LicenseShortName") or {}).get("value", ""))
    low = lic.lower()
    if any(r in low for r in REJECT) or not any(a in low for a in ACCEPT):
        raise SystemExit(f"REFUSED {title}: license {lic!r} is not reusable")
    if not info.get("url"):
        raise SystemExit(f"REFUSED {title}: no file URL returned")
    return info["url"], lic, clean((meta.get("Artist") or {}).get("value", ""))


def download(url: str) -> bytes:
    import time

    last = None
    for attempt in range(5):
        try:
            req = urllib.request.Request(url.split("?")[0], headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001 - retry on transient HTTP errors
            last = e
            time.sleep(4 * (attempt + 1))
    raise last  # noqa: B904


def optimize(raw: bytes, dest: str, max_dim: int = 1280) -> tuple[int, int, int]:
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    if max(img.size) > max_dim:
        img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    img.save(dest, "JPEG", quality=80, progressive=True, optimize=True)
    return img.size[0], img.size[1], os.path.getsize(dest)


def main() -> None:
    os.makedirs(TARGET, exist_ok=True)
    total = 0
    import time

    for title, local, author, license_label in PHOTOS:
        url, live_lic, live_artist = fetch(title)
        time.sleep(2)  # be polite to upload.wikimedia.org
        dest = os.path.join(TARGET, local)
        w, h, size = optimize(download(url), dest)
        total += size
        print(f"OK {local} ({w}x{h}, {size / 1024:.0f} KB) [{live_lic}]")
        if live_artist and author.split(",")[0].split("(")[0].strip().lower() not in live_artist.lower():
            print(f"   note: live artist metadata reads {live_artist[:100]!r}")
    print(f"\n{len(PHOTOS)} photos, {total / 1024:.0f} KB total")


if __name__ == "__main__":
    main()
