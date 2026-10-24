#!/usr/bin/env python3
"""Replace every `> **[Image Placeholder: ...]**` block in content/lessons/
with an inline Markdown image pointing at a locally stored SVG diagram.

Run:  python3 scripts/fill-image-placeholders.py
Idempotent: after the first run no placeholder blocks remain, so re-runs
report 0 replacements.
"""

from __future__ import annotations

import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(REPO, "content", "lessons")

# title -> (svg file, alt text, caption)
MAP = {
    "Hasty Digging vs. Careful Excavation": (
        "digging-01-hasty-vs-careful.svg",
        "Comparison of a messy rushed dig with broken finds tossed aside versus a neat gridded excavation where a scientist uses small tools and records everything",
        "Rushing destroys fragile finds and their clues; slow, recorded digging preserves the evidence.",
    ),
    "How Layers Stack Up in the Ground": (
        "digging-01-layers-stack-up.svg",
        "Hillside cutaway showing topsoil with grass and a coin on top, then a clay hearth layer, then sandstone with a fossil bone, then shell-bearing limestone at the base, with younger upward and older downward",
        "Deeper layers were laid down first, so they are usually older than the layers above them.",
    ),
    "Archaeology vs. Paleontology Side-by-Side Comparison": (
        "digging-02-archaeology-vs-paleontology.svg",
        "Three-row comparison of human-made pottery, arrowhead, and room foundation against fossil shell, dinosaur tooth, and articulated skeleton",
        "Archaeology studies things people made; paleontology studies fossils of ancient life.",
    ),
    "Find With Context vs. Find Without Context": (
        "digging-03-context-vs-no-context.svg",
        "A fossil jawbone mapped in its sandstone layer with shells, scale bar, and site tag beside the same bone alone in a box with its location, layer, and neighbours unknown",
        "The same find tells a rich story in context and almost none without it.",
    ),
    "Field Notebook Page and Grid Map": (
        "digging-03-field-notebook-grid.svg",
        "Excavation grid square with numbered bones, compass direction, and scale beside an open field notebook page with a sketch, depths, and rock-layer notes",
        "Grid maps and notebooks let any scientist rebuild the site long after the dig.",
    ),
    "Body Fossils vs. Trace Fossils Gallery": (
        "fossils-01-body-vs-trace.svg",
        "Gallery of body fossils including an ammonite shell, dinosaur tooth, fern frond, and petrified wood beside trace fossils including a trackway, burrows, bite marks, and a coprolite",
        "Body fossils are parts of organisms; trace fossils are signs of what they did.",
    ),
    "Four-Step Burial and Mineralization Sequence": (
        "fossils-02-burial-mineralization.svg",
        "Four panels showing quick burial of a fish, deepening sediment layers, mineral-rich groundwater filling bone pores, and erosion exposing the fossil",
        "Burial, protection, mineral seepage, and later exposure turn remains into stone.",
    ),
    "How a Fossil Mold and Natural Cast Form": (
        "fossils-02-mold-and-cast.svg",
        "Three steps showing a buried clam shell, the hollow mold left after it dissolves, and minerals filling the mold into a solid stone cast",
        "A mold is the hollow impression; a cast is the stone copy that fills it.",
    ),
    # NOTE: this diagram was retired after the first run — three real photos
    # (amber fly, tar bubble, Lyuba; see scripts/insert-sourced-photos.py)
    # now cover its panels, so the file no longer exists. Kept here as a
    # record of the original placeholder mapping.
    "Special Preservation Examples": (
        "fossils-02-special-preservation.svg (retired; see insert-sourced-photos.py)",
        "An insect with veined wings in golden amber, bones in a dark tar seep, and a woolly mammoth calf in icy permafrost",
        "Amber, tar, and ice can preserve details that ordinary rock rarely keeps.",
    ),
    "Two Paths After Death — Recycling vs. Fossilization": (
        "fossils-03-two-paths.svg",
        "Flowchart from death splitting into the common path of scavengers, decay, and recycling with no fossil, and the rare path of rapid burial and mineralization ending in a fossil",
        "Almost everything is recycled; fossilization needs fast burial and the right chemistry.",
    ),
    "Prospecting a Badlands Hillside": (
        "fieldwork-01-prospecting-badlands.svg",
        "Badlands slope with a fossil femur still in its mudstone layer and a trail of bone scraps leading a prospector with a notebook uphill to the source",
        "Follow loose fragments uphill: the rest of the fossil is often still in the layer.",
    ),
    "Field Tool Progression — Overburden to Bone Surface": (
        "fieldwork-02-tool-progression.svg",
        "Rock-wall cross-section with hammers, chisels, and shovels assigned to barren overburden and trowel, pick, brush, consolidant, and calipers assigned to the fossil zone",
        "Heavy tools clear empty rock; only small tools work near the bone.",
    ),
    "Overhead Quarry Grid Map of a Bone Bed": (
        "fieldwork-02-quarry-grid-map.svg",
        "Two-metre string grid over ribs, pelvis, femur, and jaw labelled F-101 to F-108 with a north arrow, scale bar, and ancient river-flow direction",
        "Every bone is numbered, mapped, and photographed before anything moves.",
    ),
    "Five-Step Diagram of Plaster Jacketing a Fossil": (
        "fieldwork-03-plaster-jacket-steps.svg",
        "Five steps from carving a rock pedestal around a femur to paper separator, plaster-soaked burlap, undercutting and flipping, and a sealed jacket labelled DS-2026-04",
        "The jacket cradles fossil and rock together for the trip to the lab.",
    ),
    "Dinosaur Trackway Left in Place for Study": (
        "fieldwork-03-trackway-in-place.svg",
        "Three-toed footprint trail across a rock ledge recorded with a measuring tape, tripod camera, and notebook while the rock stays untouched",
        "Some finds teach most where they lie, so crews map and scan them in place.",
    ),
    "Fossil Preparator Working Under a Microscope": (
        "lab-01-preparator-microscope.svg",
        "Prep-lab bench with an opened plaster jacket holding a skull, an air scribe, a boom microscope, a dish of saved matrix, and archival adhesive",
        "Preparation removes rock grain by grain under magnification and saves every crumb.",
    ),
    "Cataloged Fossil Specimen and Archive Record": (
        "lab-01-catalog-specimen-record.svg",
        "Numbered fossil jawbone resting in a padded cradle, linked by its catalog number to a label card, field photos and quarry map, and the rock-layer record",
        "One catalog number ties the specimen to its hillside, layer, and neighbours forever.",
    ),
    "Four Fossil Tooth Shapes and Their Diets": (
        "lab-02-tooth-shapes-diets.svg",
        "Four fossil teeth with magnified biting surfaces: a serrated theropod slicer, a conical fish-gripper, a peg-like leaf-stripper, and a ridged grinding battery",
        "Tooth shape records diet: slice meat, grip fish, strip leaves, or grind plants.",
    ),
    "Reading a Fossil Trackway and Limb Posture": (
        "lab-02-trackway-posture.svg",
        "Footprint trail marked for foot length, stride, and narrow width beside a hind-limb skeleton showing how hip height and joint angles are measured",
        "Trackways show how animals actually moved; skeletons show what was possible.",
    ),
    "Skeletal Reconstruction Bone Map — Original vs. Reconstructed": (
        "lab-03-bone-map.svg",
        "Side-view dinosaur skeleton shaded dark brown for original fossil bone, tan for mirrored or second-specimen bone, and white outline for still-missing bones",
        "Bone maps show exactly which parts are original evidence and which are filled in.",
    ),
    "CT Scan Revealing Hidden Structures Inside a Fossil Skull": (
        "lab-03-ct-scan-skull.svg",
        "Fossil skull exterior in rock beside a translucent CT rendering of the same skull exposing the braincase cavity and hidden replacement teeth",
        "Scanners see inside the stone without touching the fossil.",
    ),
    "Matching Rock Layers and Fossils Across Two Canyon Walls": (
        "time-01-correlating-layers.svg",
        "Two canyon walls with four matching layers each, from trilobite limestone to mammoth gravel, linked by dashed correlation lines across the valley",
        "Matching rock type, order, and fossils links separate outcrops into one timeline.",
    ),
    "The Geologic Column — Rock Divisions and Representative Fossils": (
        "time-02-geologic-column.svg",
        "Vertical rock column from Precambrian stromatolites at the base through Paleozoic trilobites and armored fish and Mesozoic dinosaurs to Cenozoic mammoths at the top",
        "The column orders the rock and fossil record from lowest and oldest to highest and youngest.",
    ),
    "Bracketing a Fossil Layer Between Volcanic Ash Beds": (
        "time-03-bracketing-ash-beds.svg",
        "Outcrop with a dinosaur sandstone between lower and upper volcanic ash beds, with a zoomed zircon crystal showing parent and daughter atoms",
        "The fossil layer is younger than the ash below it and older than the ash above it.",
    ),
    "Annotated Skull and Thoracic Armor of Dunkleosteus": (
        "windows-01-dunkleosteus-armor.svg",
        "Side view of the Dunkleosteus head and shoulder shield labelling armor plates, the bony eye ring, self-sharpening jaw blades, and the neck hinge",
        "Only the armored front third fossilizes well; the cartilage rear rarely survives.",
    ),
    "Sprawling Reptile Posture vs. Upright Dinosaur Posture": (
        "windows-02-sprawling-vs-upright.svg",
        "Front-view pelvis comparison of a sprawling lizard with sideways legs and a wide trail against a dinosaur with pillar legs under its body and a narrow trail",
        "Open hip sockets tucked dinosaur legs straight under the body.",
    ),
    "Dinosaur Skull and Tooth Comparison — Theropod vs. Hadrosaur vs. Sauropod": (
        "windows-02-skull-tooth-comparison.svg",
        "Theropod skull with curved serrated teeth, hadrosaur skull with beak and grinding dental battery, and sauropod skull with rake-like peg teeth",
        "Skulls and teeth show who sliced meat, who ground plants, and who raked leaves.",
    ),
    "Mammoth Molar vs. Mastodon Molar Side-by-Side Comparison": (
        "windows-03-mammoth-vs-mastodon-molar.svg",
        "Flat washboard mammoth molar with steppe grasses beside cone-cusped mastodon molar with spruce twigs",
        "Mammoth molars ground grass; mastodon molars crushed twigs and leaves.",
    ),
    "Saber-Toothed Cat (Smilodon) Skull and Forelimb Build": (
        "windows-03-smilodon-skull.svg",
        "Side view of a Smilodon skull with a wide-gaping jaw and long serrated sabers beside stocky Smilodon and leaner lion forelimbs",
        "Smilodon pinned prey with bear-thick forelimbs before the neck bite.",
    ),
    "How an Asphalt Seep Captures an Entire Ecosystem (La Brea)": (
        "windows-04-la-brea-seep.svg",
        "Cutaway of a La Brea style seep with a trapped mammoth, dire wolves, and Smilodon at the surface and bones, cones, seeds, and shells packed below",
        "One sticky trap preserved predators, prey, plants, and insects together.",
    ),
    "Sedimentary Structures and the Environments They Indicate": (
        "active-01-sedimentary-structures.svg",
        "Four rock slabs paired with their settings: rippled sandstone with a river, cracked mudstone with a lakeshore, shelly limestone with a shallow sea, and coal with a swamp forest",
        "Each rock texture matches a process still visible in living environments today.",
    ),
    "Stratigraphic Diagram Across the End-Cretaceous (K-Pg) Boundary": (
        "active-02-kpg-boundary.svg",
        "Rock column split by a dark boundary clay with dinosaurs, ammonites, and mosasaurs below and diversifying mammals, birds, and flowering plants above",
        "Many groups vanish at the boundary clay; different groups dominate above it.",
    ),
    "Microscopic View of Dinosaur Bone Soft Tissue and Vessel Structures": (
        "active-03-soft-tissue-micro.svg",
        "Dense T. rex bone chip, then flexible branching vessel-like tubes with cell-like dots after dissolving the mineral, then a zoomed branching bone cell",
        "Dissolving the mineral left stretchy vessel-like structures that snapped back when pulled.",
    ),
}


def replacement(title: str) -> str:
    svg, alt, caption = MAP[title]
    return f"![{alt}](images/lessons/{svg})\n\n*{caption}*"


def main() -> None:
    pattern = re.compile(
        r"> \*\*\[Image Placeholder: (?P<title>[^\]]+)\]\*\*\n(?P<detail>(?:>.*\n?)+)"
    )
    total = 0
    files_touched = 0
    for fname in sorted(os.listdir(LESSONS)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(LESSONS, fname)

        def sub(m: re.Match, fname=fname) -> str:
            title = m.group("title")
            if title not in MAP:
                raise SystemExit(f"ERROR: no image mapped for placeholder {title!r} in {fname}")
            svg, _, _ = MAP[title]
            img_path = os.path.join(REPO, "public", "images", "lessons", svg)
            if not os.path.exists(img_path):
                raise SystemExit(f"ERROR: missing image file {img_path} for {fname}")
            return replacement(title)

        with open(path, encoding="utf-8") as f:
            before = f.read()
        after, n = pattern.subn(sub, before)
        if n:
            with open(path, "w", encoding="utf-8") as f:
                f.write(after)
            print(f"{fname}: replaced {n} placeholder(s)")
            total += n
            files_touched += 1
    # Fail loudly if any placeholder survived.
    leftovers = 0
    for fname in sorted(os.listdir(LESSONS)):
        if not fname.endswith(".md"):
            continue
        with open(os.path.join(LESSONS, fname), encoding="utf-8") as f:
            leftovers += f.read().count("[Image Placeholder:")
    print(f"\nReplaced {total} placeholder(s) across {files_touched} lesson file(s).")
    print(f"Remaining placeholders: {leftovers}")
    if leftovers:
        raise SystemExit("ERROR: some placeholders were not replaced")


if __name__ == "__main__":
    main()
