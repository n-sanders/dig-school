#!/usr/bin/env python3
"""Swap diagram references for sourced photos in the remaining lessons.

Each entry replaces one diagram image+caption block with one or more photo
blocks. The retired SVG files stay on disk for the future illustration pass.
Run:  python3 scripts/swap-diagrams-for-photos.py  (idempotent)
"""

from __future__ import annotations

import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(REPO, "content", "lessons")

IMG = "images/lessons/"

# (lesson file, diagram file, [(photo file, alt, caption), ...])
SWAPS: list[tuple[str, str, list[tuple[str, str, str]]]] = [
    ("digging-01-detective-work.md", "digging-01-layers-stack-up.svg", [
        ("photo-grand-canyon-layers.jpg",
         "Photograph of Grand Canyon walls showing many distinct horizontal rock layers stacked from river to rim",
         "Real layered rock on a grand scale: the Grand Canyon's stacked formations, each laid down in its own chapter. (Photo: Mx. Granger, CC0, via Wikimedia Commons.)"),
    ]),
    ("digging-03-context-and-records.md", "digging-03-field-notebook-grid.svg", [
        ("photo-geological-notebook.jpg",
         "Photograph of an open geologist's field notebook with dated notes and hand-colored sketches of rock layers",
         "A real field notebook: dated notes and hand-colored sketches recording each rock layer. (Photo: PePeEfe, CC BY-SA 3.0, via Wikimedia Commons.)"),
    ]),
    ("fossils-01-body-and-trace.md", "fossils-01-body-vs-trace.svg", [
        ("photo-ammonite-pavement.jpg",
         "Photograph of a rocky shore paved with countless ammonite shell cross-sections preserved in the stone",
         "A shore paved with real ammonites — body fossils by the hundred, still in their rock layer. (Photo: RealGatba, CC0, via Wikimedia Commons.)"),
        ("photo-eubrontes-cast.jpg",
         "Photograph of a cast of a three-toed Eubrontes dinosaur footprint",
         "A real three-toed dinosaur footprint (a cast of an Eubrontes track): a trace fossil of a living animal's steps. (Track cast prepared by Paul Olsen; photo: Z22, CC BY 3.0, via Wikimedia Commons.)"),
    ]),
    ("fossils-02-how-fossils-form.md", "fossils-02-burial-mineralization.svg", [
        ("photo-green-river-fish.jpg",
         "Photograph of a complete fossil fish preserved in fine Green River Formation shale",
         "Quick burial at work: a whole fossil fish kept in exquisite detail by fine lake muds. (Photo: James St. John, CC BY 2.0, via Wikimedia Commons.)"),
    ]),
    ("fossils-02-how-fossils-form.md", "fossils-02-mold-and-cast.svg", [
        ("photo-steinkern-meretrix.jpg",
         "Photograph of steinkerns, natural internal stone casts of clam shells",
         "Nature's casts: steinkerns, solid stone copies formed inside clam shells. (Photo: H. Zell, CC BY-SA 3.0, via Wikimedia Commons.)"),
    ]),
    ("fieldwork-02-excavating-and-recording.md", "fieldwork-02-tool-progression.svg", [
        ("photo-brushing-trench-nps.jpg",
         "National Park Service researcher brushing sediment from fossils on two trench layers",
         "Slow work in the field: a researcher brushes sediment from fossils layer by layer. (Photo: U.S. National Park Service, public domain.)"),
    ]),
    ("fieldwork-02-excavating-and-recording.md", "fieldwork-02-quarry-grid-map.svg", [
        ("photo-cleveland-lloyd-quarry.jpg",
         "Excavated dinosaur bone bed under shelter at the Cleveland-Lloyd Dinosaur Quarry in Utah",
         "A real mapped bone bed: excavated dinosaur bones under shelter at Cleveland-Lloyd Quarry, Utah. (Photo: National Park Service, public domain.)"),
    ]),
    ("lab-01-preparation-and-cataloging.md", "lab-01-catalog-specimen-record.svg", [
        ("photo-museum-cabinets-nps.jpg",
         "Rows of tall museum collection cabinets housing cataloged fossils",
         "Where catalog numbers live: rows of museum cabinets keeping every specimen findable for a century. (Photo: U.S. National Park Service, public domain.)"),
    ]),
    ("lab-02-clues-in-bones-teeth-and-stone.md", "lab-02-tooth-shapes-diets.svg", [
        ("photo-trex-tooth-usda.jpg",
         "Photograph of a Tyrannosaurus rex tooth held in a hand, found in the Hell Creek Formation",
         "A real Tyrannosaurus tooth from the Hell Creek Formation, built for piercing and slicing meat. (Photo: U.S. Department of Agriculture, public domain.)"),
    ]),
    ("lab-02-clues-in-bones-teeth-and-stone.md", "lab-02-trackway-posture.svg", [
        ("photo-eubrontes-cast.jpg",
         "Photograph of a cast of a three-toed Eubrontes dinosaur footprint",
         "A real three-toed track (Eubrontes cast): footprint length, stride, and stance can all be measured from fossils like this. (Track cast prepared by Paul Olsen; photo: Z22, CC BY 3.0, via Wikimedia Commons.)"),
    ]),
    ("lab-03-reconstructions-and-many-specimens.md", "lab-03-bone-map.svg", [
        ("photo-dino-hall-mount.jpg",
         "Museum hall with reconstructed dinosaur skeleton mounts including Stegosaurus and Tyrannosaurus",
         "Reconstructions on display: museum mounts built bone by bone from many specimens. (Photo: Gary Todd, CC0, via Wikimedia Commons.)"),
    ]),
    ("time-02-the-geologic-timescale.md", "time-02-geologic-column.svg", [
        ("photo-usgs-time-scale.jpg",
         "The U.S. Geological Survey geologic time scale chart from Precambrian to the present",
         "The official U.S. Geological Survey time scale: the standard map of Earth's chapters. (Image: U.S. Geological Survey, public domain.)"),
    ]),
    ("time-03-measuring-and-interpreting-ages.md", "time-03-bracketing-ash-beds.svg", [
        ("photo-ashfall-rhino-tuff.jpg",
         "Fossil barrel-bodied rhino preserved in volcanic tuff at Ashfall Fossil Beds, Nebraska",
         "Ash as preserver and clock: a rhino entombed in volcanic tuff at Ashfall Fossil Beds. (Photo: James St. John, CC BY 2.0, via Wikimedia Commons.)"),
    ]),
    ("windows-02-dinosaurs-on-land.md", "windows-02-skull-tooth-comparison.svg", [
        ("photo-trex-skull-mor.jpg",
         "Adult Tyrannosaurus rex skull with deep jaws on display at the Museum of the Rockies",
         "A real Tyrannosaurus skull with deep bone-crushing jaws (Museum of the Rockies). (Photo: Tim Evanson, CC BY-SA 2.0, via Wikimedia Commons.)"),
        ("photo-edmontosaurus-skull.jpg",
         "Side-view scientific figure of an Edmontosaurus duck-billed dinosaur skull",
         "A duck-billed dinosaur skull (Edmontosaurus), built for cropping and grinding plants. (Figure: Xing, Mallon and Currie, CC BY 4.0, via Wikimedia Commons.)"),
        ("photo-diplodocus-skull.jpg",
         "Adult Diplodocus skull with peg-like front teeth",
         "A Diplodocus skull with rake-like peg teeth for stripping leaves. (Photo: Gary Todd, CC0, via Wikimedia Commons.)"),
    ]),
]


def photo_block(filename: str, alt: str, caption: str) -> str:
    return f"![{alt}]({IMG}{filename})\n\n*{caption}*"


def block_end(lines: list[str], img_idx: int) -> int:
    j = img_idx + 1
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    if j < len(lines) and lines[j].strip().startswith("*"):
        j += 1
    return j


def main() -> None:
    for fname, diagram, photos in SWAPS:
        path = os.path.join(LESSONS, fname)
        text = open(path, encoding="utf-8").read()
        # Already swapped?
        if all(f"{IMG}{p[0]}" in text for p in photos) and f"{IMG}{diagram}" not in text:
            print(f"{fname}: already swapped, skipping")
            continue
        lines = text.split("\n")
        idx = next((i for i, l in enumerate(lines) if f"]({IMG}{diagram})" in l), None)
        if idx is None:
            print(f"{fname}: diagram {diagram} not found, skipping")
            continue
        end = block_end(lines, idx)
        new = [b for p in photos for b in (photo_block(*p).split("\n") + [""])]
        if end < len(lines) and lines[end].strip() == "":
            lines[idx:end] = new
        else:
            lines[idx:end] = new + [""]
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        print(f"{fname}: swapped {diagram} for {len(photos)} photo(s)")


if __name__ == "__main__":
    main()
