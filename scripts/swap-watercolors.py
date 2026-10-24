#!/usr/bin/env python3
"""Swap retired SVG/photo blocks for the approved watercolor sets.

Each entry replaces one image+caption block with a watercolor sequence.
Alt text comes from uploads/manifest.md; captions are the manifest's,
adjusted per the review notes (hip sockets, scallop-like shell, pale
final fossil, DS-2026-04 + north arrow, graphic-content note).
Run:  python3 scripts/swap-watercolors.py  (idempotent)
"""

from __future__ import annotations

import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(REPO, "content", "lessons")

IMG = "images/lessons/"
TAG = "(Watercolor made for Dig School.)"

# (lesson file, old image file, [(watercolor file, alt, caption), ...])
SWAPS: list[tuple[str, str, list[tuple[str, str, str]]]] = [
    ("digging-01-detective-work.md", "digging-01-hasty-vs-careful.svg", [
        ("digging-01-hasty-vs-careful-1.jpg",
         "A messy hole in desert ground with a shovel stuck in the dirt pile and broken bones and clay pots tossed aside.",
         f"**Hasty digging:** a deep hole dug with a big shovel mixes up the soil layers, and broken bone and pottery pieces get tossed on the dirt pile, so their story is lost. {TAG}"),
        ("digging-01-hasty-vs-careful-2.jpg",
         "A paleontologist kneels by a neat string-marked pit, using a trowel and brush around a bone, with a camera, notebook, and ruler nearby.",
         f"**Careful excavation:** a level square marked with string, a small trowel and soft brush, and a ruler, camera, and field notebook record the bone right where it lies in its layer. {TAG}"),
    ]),
    ("digging-02-archaeology-and-paleontology.md", "digging-02-archaeology-vs-paleontology.svg", [
        ("digging-02-archaeology-vs-paleontology-1.jpg",
         "A painted pottery shard, a chipped stone arrowhead, and an overhead view of a stone room foundation with a round hearth.",
         f"**Archaeology studies things people made and left behind:** a decorated pottery shard, a flaked flint arrowhead, and the stone foundation of a room with its hearth. {TAG}"),
        ("digging-02-archaeology-vs-paleontology-2.jpg",
         "A ribbed fossil shell, a curved serrated dinosaur tooth, and a sandstone slab holding a complete small dinosaur skeleton.",
         f"**Paleontology studies ancient life:** a ribbed fossil shell, a serrated *Tyrannosaurus* tooth, and an articulated skeleton in sandstone. {TAG}"),
    ]),
    ("digging-03-context-and-records.md", "digging-03-context-vs-no-context.svg", [
        ("digging-03-context-vs-no-context-1.jpg",
         "A toothed fossil jaw in a tan rock layer with small shells and leaf prints, a string grid, scale bar, north arrow, and blank tag.",
         f"**In context:** the jawbone still sits in its sandstone layer with fossil river shells and leaf impressions, recorded with a string grid, scale bar, north arrow, and site tag. {TAG}"),
        ("digging-03-context-vs-no-context-2.jpg",
         "The same toothed fossil jaw lying alone in an empty, plain cardboard box on a wooden table.",
         f"**No context:** the same jawbone in a cardboard box. We can't tell where it was found, what rock it came from, or what lived alongside it. {TAG}"),
    ]),
    ("fossils-02-how-fossils-form.md", "photo-green-river-fish.jpg", [
        ("fossils-02-burial-mineralization-1.jpg",
         "Underwater view of a fish skeleton lying on a muddy lake bottom as fine particles drift down through sunlit water.",
         f"**1. Burial:** a dead fish sinks to the lake bottom, and fine mud and silt begin settling over it. {TAG}"),
        ("fossils-02-burial-mineralization-2.jpg",
         "Cutaway of a lake floor showing a fish skeleton buried beneath several stacked bands of brown and gray sediment.",
         f"**2. More layers:** sediment piles up overhead, the soft parts decay, and only the bones remain. {TAG}"),
        ("fossils-02-burial-mineralization-3.jpg",
         "Magnifying-lens view inside porous bone, with blue groundwater flowing in and depositing tiny sparkling mineral crystals.",
         f"**3. Mineralization (magnified):** groundwater carries dissolved minerals into the tiny pores of the bone, where crystals slowly fill the spaces. {TAG}"),
        ("fossils-02-burial-mineralization-4.jpg",
         "A fossil fish skeleton weathering out of tilted, layered tan rock on an eroded hillside under a blue sky.",
         f"**4. Exposure:** much later, erosion wears away the hillside and exposes the mineralized fish fossil at the surface. {TAG}"),
    ]),
    ("fossils-03-why-fossils-are-rare.md", "fossils-03-two-paths.svg", [
        ("fossils-03-two-paths-1.jpg",
         "Vultures, a coyote, beetles, and flies scavenge a deer-like carcass on an open grassy plain, with scattered bones nearby.",
         f"**The common path:** an animal that dies in the open is torn apart by scavengers like vultures, coyotes, and beetles. (Note: this painting shows some red flesh on the carcass.) {TAG}"),
        ("fossils-03-two-paths-2.jpg",
         "Bleached, crumbling bones scattered across a grassy plain with moss and small mushrooms growing among them.",
         f"**…and what's left weathers away:** sun, rain, fungi, and plants break the scattered bones down into soil, leaving no fossil. {TAG}"),
        ("fossils-03-two-paths-3.jpg",
         "Brown floodwater rushes past a riverbank where a dead antlered deer lies half-covered in mud, as a vulture watches from above.",
         f"**The rare path:** a flood quickly buries the animal in river mud and sand, hiding it from scavengers. {TAG}"),
        ("fossils-03-two-paths-4.jpg",
         "Cutaway of layered rock under a grassy plain, with a complete animal skeleton lying fossilized inside one layer.",
         f"**…and becomes a fossil:** protected underground, the pale bones turn to stone inside layers of sedimentary rock. {TAG}"),
    ]),
    ("fieldwork-03-plaster-jackets-and-transport.md", "fieldwork-03-plaster-jacket-steps.svg", [
        ("fieldwork-03-plaster-jacket-steps-1.jpg",
         "A large fossil bone resting on top of a square pillar of rock left standing in the middle of a dug-out trench.",
         f"**1. Pedestal:** dig around and under the fossil, leaving it perched on a pillar of rock. {TAG}"),
        ("fieldwork-03-plaster-jacket-steps-2.jpg",
         "The fossil bone on its rock pedestal draped with white paper towels, with a paper towel roll and rock hammer in front.",
         f"**2. Separator layer:** cover the bone with damp paper towels or foil so the plaster won't stick to it. {TAG}"),
        ("fieldwork-03-plaster-jacket-steps-3.jpg",
         "The bone and pedestal wrapped in white plaster-soaked burlap, with a plaster bucket, paper towel roll, and rock hammer nearby.",
         f"**3. Burlap and plaster:** lay strips of plaster-soaked burlap over the block to build a hard shell. {TAG}"),
        ("fieldwork-03-plaster-jacket-steps-4.jpg",
         "A flipped plaster jacket showing its rough rock underside on top, with a leftover rock stump, plaster bucket, and tools.",
         f"**4. Undercut and flip:** once the plaster hardens, cut through the pedestal and carefully flip the jacket over. {TAG}"),
        ("fieldwork-03-plaster-jacket-steps-5.jpg",
         "A fully sealed white plaster jacket with a black arrow drawn on top and a black marker beside it, next to a bucket and tools.",
         f"**5. Seal and label:** plaster the open bottom shut and mark the jacket with its field number (e.g., DS-2026-04) and a north arrow. {TAG}"),
    ]),
    ("lab-01-preparation-and-cataloging.md", "photo-museum-cabinets-nps.jpg", [
        ("lab-01-catalog-specimen-record-1.jpg",
         "A fossil jaw in a custom white foam cradle in a wooden museum drawer, beside a label card, two field photos, and a quarry map.",
         f"**A cataloged specimen:** the jawbone rests in a custom padded cradle in a museum drawer. Its painted catalog number links it to the label card, field photos, and quarry map that record where it came from. {TAG}"),
    ]),
    ("lab-02-clues-in-bones-teeth-and-stone.md", "photo-trex-tooth-usda.jpg", [
        ("lab-02-tooth-shapes-diets-1.jpg",
         "A curved, blade-like brown fossil dinosaur tooth with fine serrated edges, shown on a plain cream background.",
         f"**Meat-eater (theropod):** a curved, blade-like tooth with saw-edge serrations for slicing flesh. {TAG}"),
        ("lab-02-tooth-shapes-diets-2.jpg",
         "A slender, smooth, dark brown cone-shaped fossil tooth with a sharp point and no serrations, on a plain cream background.",
         f"**Fish-eater (marine reptile):** a tall, slender cone with a sharp point for gripping slippery prey. {TAG}"),
        ("lab-02-tooth-shapes-diets-3.jpg",
         "A long, straight, pencil-shaped brown fossil tooth with a blunt worn tip, on a plain cream background.",
         f"**Plant-stripper (sauropod):** a peg- or pencil-shaped tooth worn flat at the tip from raking leaves off branches. {TAG}"),
        ("lab-02-tooth-shapes-diets-4.jpg",
         "A fossil jaw section whose broad surface is packed with rows of small diamond-shaped teeth, forming a grinding pad.",
         f"**Plant-grinder (hadrosaur):** a dental battery of hundreds of tightly packed teeth that forms a wide, ridged grinding surface. {TAG}"),
    ]),
    ("time-01-layers-and-relative-order.md", "time-01-correlating-layers.svg", [
        ("time-01-correlating-layers-1.jpg",
         "Two rock walls across a desert valley showing the same gray, red, tan, and gravel layers, linked by dashed lines.",
         f"**Matching layers across a valley:** both canyon walls show the same order from bottom to top — gray limestone, red shale, tan sandstone, then gravel and silt — with dashed lines marking the matching layers. {TAG}"),
    ]),
    ("windows-02-dinosaurs-on-land.md", "windows-02-sprawling-vs-upright.svg", [
        ("windows-02-sprawling-vs-upright-1.jpg",
         "Head-on view of a crocodile with its leg bones drawn in, showing upper legs sticking out sideways and feet planted wide.",
         f"**Sprawling (crocodile):** the upper limb bones stick out sideways and the elbows bend down, so the feet sit far out to the sides. {TAG}"),
        ("windows-02-sprawling-vs-upright-2.jpg",
         "Head-on view of a small two-legged dinosaur with its leg bones drawn in, showing legs straight down under the body.",
         f"**Upright (dinosaur):** the legs run straight down from the hip sockets and hold the body high, like pillars. {TAG}"),
    ]),
    ("active-03-surprises-and-ongoing-discovery.md", "active-03-soft-tissue-micro.svg", [
        ("active-03-soft-tissue-micro-1.jpg",
         "A large fossil leg bone on a wooden table with its broken end facing the viewer, showing a dense outer wall and spongy core.",
         f"**A fossil *T. rex* thigh bone, broken open:** the dense outer wall surrounds a spongy center. Scientists dissolved the minerals out of pieces like this. {TAG}"),
        ("active-03-soft-tissue-micro-2.jpg",
         "Microscope view of clear, branching, flexible tubes containing tiny reddish-brown round dots.",
         f"**Under the microscope:** flexible, branching, see-through vessel-like tubes, with tiny dark reddish round structures inside. {TAG}"),
        ("active-03-soft-tissue-micro-3.jpg",
         "Microscope view of a single reddish oval bone cell with many fine filaments branching outward like tree roots.",
         f"**High magnification:** a bone-cell-like structure (osteocyte) with fine branching filaments. {TAG}"),
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
    for fname, old, photos in SWAPS:
        path = os.path.join(LESSONS, fname)
        text = open(path, encoding="utf-8").read()
        if all(f"{IMG}{p[0]}" in text for p in photos) and f"{IMG}{old}" not in text:
            print(f"{fname}: already swapped, skipping")
            continue
        lines = text.split("\n")
        idx = next((i for i, l in enumerate(lines) if f"]({IMG}{old})" in l), None)
        if idx is None:
            print(f"{fname}: {old} not found, skipping")
            continue
        end = block_end(lines, idx)
        new = [b for p in photos for b in (photo_block(*p).split("\n") + [""])]
        if end < len(lines) and lines[end].strip() == "":
            lines[idx:end] = new
        else:
            lines[idx:end] = new + [""]
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        print(f"{fname}: swapped {old} for {len(photos)} watercolor(s)")


if __name__ == "__main__":
    main()
