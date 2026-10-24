#!/usr/bin/env python3
"""Search Wikimedia Commons for freely licensed images and print candidates.

Usage: python3 scripts/search-commons.py "dinosaur trackway" [--limit 15]

Only surfaces files whose license metadata indicates reuse is allowed
(public domain, CC0, CC BY, CC BY-SA). Prints title, license, author,
dimensions, file page and direct URL for each candidate.
"""

from __future__ import annotations

import html
import json
import re
import sys
import urllib.parse
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"

ACCEPT = ("public domain", "cc0", "cc by", "cc by-sa", "cc-by", "cc-by-sa", "pd")
REJECT = ("nc", "nd", "fair use", "copyrighted", "no known copyright")


def clean(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s or "")
    return html.unescape(s).strip()[:160]


def lic_ok(short: str) -> bool:
    low = short.lower()
    if any(r in low for r in REJECT):
        return False
    return any(a in low for a in ACCEPT)


def search(query: str, limit: int = 15):
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": f"{query} filetype:bitmap",
        "gsrnamespace": 6,
        "gsrlimit": limit,
        "prop": "imageinfo",
        "iiprop": "url|size|extmetadata",
        "iiextmetadatafilter": "LicenseShortName|Artist|Credit",
    }
    req = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": "DigSchoolLessonImages/1.0 (school project)"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    pages = (data.get("query") or {}).get("pages") or {}
    out = []
    for p in pages.values():
        info = (p.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata") or {}
        lic = clean((meta.get("LicenseShortName") or {}).get("value", ""))
        if not lic_ok(lic):
            continue
        out.append(
            {
                "title": p.get("title", "").replace("File:", ""),
                "license": lic,
                "author": clean((meta.get("Artist") or {}).get("value", ""))
                or clean((meta.get("Credit") or {}).get("value", "")),
                "width": info.get("width"),
                "height": info.get("height"),
                "page": f"https://commons.wikimedia.org/wiki/{urllib.parse.quote('File:' + p.get('title', '').replace('File:', ''))}",
                "url": info.get("url"),
            }
        )
    return out


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: search-commons.py \"query\" [--limit N]")
    query = sys.argv[1]
    limit = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[2] == "--limit" else 15
    results = search(query, limit)
    print(f"# {len(results)} reusable candidates for {query!r}\n")
    for i, r in enumerate(results, 1):
        print(f"## {i}. {r['title']}")
        print(f"   license: {r['license']}")
        print(f"   author:  {r['author'] or '(unknown)'}")
        print(f"   size:    {r['width']}x{r['height']}")
        print(f"   page:    {r['page']}")
        print(f"   file:    {r['url']}\n")


if __name__ == "__main__":
    main()
