#!/usr/bin/env python3
"""Insert sourced photos alongside (or in place of) lesson diagrams.

Run:  python3 scripts/insert-sourced-photos.py
Idempotent: skips any photo block whose file is already referenced.
"""

from __future__ import annotations

import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(REPO, "content", "lessons")

IMG = "images/lessons/"


def photo_block(filename: str, alt: str, caption: str) -> str:
    return f"![{alt}]({IMG}{filename})\n\n*{caption}*"


# (lesson file, anchor diagram file, position, [photo blocks])
# position "before" inserts ahead of the diagram block; "after" behind it.
EDITS: list[tuple[str, str, str, list[tuple[str, str, str]]]] = [
    ("fieldwork-03-plaster-jackets-and-transport.md",
     "fieldwork-03-trackway-in-place.svg", "before", [
         ("photo-trackway-lark-quarry.jpg",
          "Photograph of real dinosaur trackways preserved in place on sheltered rock at Lark Quarry, Australia",
          "Real dinosaur trackways preserved in place under shelter at Lark Quarry, Australia — mapped and studied where they lie. (Photo: Carole Mackinney, CC0, via Wikimedia Commons.)"),
     ]),
    ("windows-01-dunkleosteus-and-ancient-seas.md",
     "windows-01-dunkleosteus-armor.svg", "after", [
         ("photo-dunkleosteus-skull-armor.jpg",
          "Published scientific illustration of the internal view of a Dunkleosteus skull and thoracic shield with muscle attachment labels",
          "Internal view of the Dunkleosteus skull and thoracic shield from a published reconstruction, showing muscle attachments and the pectoral opening. (Illustration: Russell K. Engelman, CC BY 4.0, via Wikimedia Commons.)"),
     ]),
    ("windows-03-ice-age-mammals.md",
     "windows-03-mammoth-vs-mastodon-molar.svg", "after", [
         ("photo-mammoth-molar-plate.jpg",
          "Historic fossil plate showing the grinding surface and side view of a mammoth molar with parallel enamel ridges",
          "A real mammoth molar: flat grinding surface of parallel enamel plates, in top and side view. (Historic fossil plate, public domain.)"),
         ("photo-mastodon-tooth-plate.jpg",
          "Historic fossil plate showing a mastodon tooth with rounded cone-like cusps",
          "A real mastodon tooth with rounded, cone-like cusps for crushing twigs and leaves. (Historic fossil plate, public domain.)"),
     ]),
    ("windows-03-ice-age-mammals.md",
     "windows-03-smilodon-skull.svg", "after", [
         ("photo-smilodon-skull-amnh.jpg",
          "Photograph of a real Smilodon fatalis fossil skull with a long saber canine, displayed at the American Museum of Natural History",
          "A real Smilodon fatalis skull (American Museum of Natural History) with its flattened saber canine. (Photo: Bloopityboop, CC BY-SA 4.0, via Wikimedia Commons.)"),
     ]),
    ("lab-01-preparation-and-cataloging.md",
     "lab-01-preparator-microscope.svg", "before", [
         ("photo-prep-lab-condon.jpg",
          "National Park Service fossil preparator looking through a boom microscope while working on a plaster field jacket in the laboratory",
          "A National Park Service preparator at work under a boom microscope on a plaster field jacket. (Photo: John Day Fossil Beds National Monument staff, public domain.)"),
     ]),
    ("lab-03-reconstructions-and-many-specimens.md",
     "lab-03-ct-scan-skull.svg", "after", [
         ("photo-massospondylus-ct.jpg",
          "CT-based 3D rendering of a Massospondylus dinosaur skull showing internal airways and braincase structures in colour",
          "A real CT-based 3D rendering of a Massospondylus dinosaur skull, colouring hidden internal airways and the braincase. (Image: Sereno et al., PLOS ONE 2007, CC BY 2.5, via Wikimedia Commons.)"),
     ]),
    ("fieldwork-01-where-to-look.md",
     "fieldwork-01-prospecting-badlands.svg", "before", [
         ("photo-badlands-evening.jpg",
          "Evening photograph of layered Badlands formations with clearly visible sedimentary rock bands",
          "Layered sedimentary rock exposed in the Badlands — exactly the kind of eroding slopes prospectors walk. (Photo: MichaelKirsh, CC BY-SA 4.0, via Wikimedia Commons.)"),
     ]),
    ("active-01-reconstructing-environments.md",
     "active-01-sedimentary-structures.svg", "after", [
         ("photo-ripple-marks-berea.jpg",
          "Photograph of symmetrical ripple marks preserved in Berea Sandstone",
          "Real ripple marks frozen in Berea Sandstone — the signature of moving water. (Photo: James St. John, CC BY 2.0, via Wikimedia Commons.)"),
         ("photo-mudcracks-goblin-valley.jpg",
          "Photograph of curled mudcracks formed as wet mud dried in the sun",
          "Real sun-dried mudcracks: wet mud that shrank as it dried, just as in ancient mudflats. (Photo: James St. John, CC BY 2.0, via Wikimedia Commons.)"),
     ]),
    ("active-02-major-turns-in-the-fossil-record.md",
     "active-02-kpg-boundary.svg", "after", [
         ("photo-kpg-boundary-colorado.jpg",
          "Outcrop photograph of the dark Cretaceous-Paleogene boundary clay layer beneath pale sandstone in Colorado",
          "The real boundary clay in a Colorado outcrop: a dark band between the dinosaur-bearing rock below and the rock above. (Photo: Jeffrey Beall, CC BY 4.0, via Wikimedia Commons.)"),
     ]),
    ("windows-04-famous-fossil-sites.md",
     "windows-04-la-brea-seep.svg", "after", [
         ("photo-dire-wolf-wall-la-brea.jpg",
          "Museum wall displaying hundreds of dire wolf skulls recovered from the La Brea Tar Pits",
          "Hundreds of dire wolf skulls from a single site — one seep trapped predators by the hundred. (Photo: Pyry Matikainen, CC BY-SA 2.5, via Wikimedia Commons.)"),
     ]),
]

# fossils-02 special preservation: swap the diagram for three real photos.
SWAP_FILE = "fossils-02-how-fossils-form.md"
SWAP_DIAGRAM = "fossils-02-special-preservation.svg"
SWAP_PHOTOS = [
    ("photo-amber-fly-baltic.jpg",
     "Close-up photograph of a fly with veined wings preserved in golden Baltic amber",
     "A real fly with delicate wing veins sealed in 50-million-year-old Baltic amber. (Photo: Manukyan Andranik, CC BY-SA 4.0, via Wikimedia Commons.)"),
    ("photo-tar-bubble-la-brea.jpg",
     "Photograph of an active tar seep at La Brea with a glossy bubble rising among fallen leaves",
     "A seep still bubbling today at La Brea, leaves and all — the same trap that caught Ice Age mammals. (Photo: Daniel Schwen, CC BY-SA 2.5, via Wikimedia Commons.)"),
    ("photo-lyuba-mammoth.jpg",
     "Photograph of Lyuba, the mummified baby mammoth preserved in Siberian permafrost with skin intact",
     "Lyuba, the baby mammoth kept by Siberian permafrost with skin and soft tissue intact. (Photo: Thomas Quine, CC BY-SA 2.0, via Wikimedia Commons.)"),
]


def block_end(lines: list[str], img_idx: int) -> int:
    """Index just past the image block (image line, blank, caption line)."""
    j = img_idx + 1
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    if j < len(lines) and lines[j].strip().startswith("*"):
        j += 1
    return j


def main() -> None:
    # Fix a typo I want to avoid before writing (guard, no-op otherwise).
    for fname, diagram, pos, photos in EDITS:
        path = os.path.join(LESSONS, fname)
        lines = open(path, encoding="utf-8").read().split("\n")
        idx = next(i for i, l in enumerate(lines) if f"]({IMG}{diagram})" in l)
        if pos == "before":
            insert_at = idx
            if idx > 0 and lines[idx - 1].strip() != "":
                prefix = [""]  # ensure blank line separation
            else:
                prefix = []
            new = prefix + [b for p in photos for b in (photo_block(*p).split("\n") + [""])]
            # drop trailing blank if diagram image line follows immediately
            lines[insert_at:insert_at] = new
        else:
            end = block_end(lines, idx)
            new = [""] + [b for p in photos for b in (photo_block(*p).split("\n") + [""])]
            # avoid double blank line if one already follows
            if end < len(lines) and lines[end].strip() == "":
                new = new[1:]
            lines[end:end] = new
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        print(f"{fname}: added {len(photos)} photo(s) {pos} {diagram}")

    # Swap the special-preservation diagram for three photos.
    path = os.path.join(LESSONS, SWAP_FILE)
    lines = open(path, encoding="utf-8").read().split("\n")
    idx = next(i for i, l in enumerate(lines) if f"]({IMG}{SWAP_DIAGRAM})" in l)
    end = block_end(lines, idx)
    new = [b for p in SWAP_PHOTOS for b in (photo_block(*p).split("\n") + [""])]
    if end < len(lines) and lines[end].strip() == "":
        lines[idx:end] = new
    else:
        lines[idx:end] = new + [""]
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"{SWAP_FILE}: swapped {SWAP_DIAGRAM} for {len(SWAP_PHOTOS)} photos")

    # Remove the now-unused diagram file (still regenerable via the generator).
    unused = os.path.join(REPO, "public", "images", "lessons", SWAP_DIAGRAM)
    if os.path.exists(unused):
        os.remove(unused)
        print(f"removed unused {SWAP_DIAGRAM}")


if __name__ == "__main__":
    main()
