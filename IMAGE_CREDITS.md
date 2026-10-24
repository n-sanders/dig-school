# Image Credits — Dig School Lesson Diagrams

All 33 lesson images were **created for Dig School** with the generator script
`scripts/make-lesson-images.py` (run: `python3 scripts/make-lesson-images.py`).
They are original, hand-built SVG diagrams tailored to each placeholder's
Type/Description note. No third-party photos, hotlinks, or copyrighted images
are used anywhere in the lesson content.

- **Author:** Dig School contributors (generated diagrams)
- **License:** CC0 1.0 Universal (public domain dedication) — free to reuse
  for any purpose without attribution.
- **Source URL:** not applicable (created locally, not sourced); the generator
  script in this repo is the source.
- **Location:** `public/images/lessons/*.svg`, referenced from lesson bodies
  as `images/lessons/<file>.svg` (the project's local-asset format).
- **Total size:** 33 files, ~146 KB combined.

## Inventory

| # | Lesson | File | What it shows |
|---|--------|------|---------------|
| 1 | digging-01-detective-work | digging-01-hasty-vs-careful.svg | Rushed messy dig vs. neat gridded scientific dig |
| 2 | digging-01-detective-work | digging-01-layers-stack-up.svg | Hillside cutaway: topsoil, clay hearth, fossil sandstone, shell limestone |
| 3 | digging-02-archaeology-and-paleontology | digging-02-archaeology-vs-paleontology.svg | 3-row comparison: pottery/shell, arrowhead/tooth, foundation/skeleton |
| 4 | digging-03-context-and-records | digging-03-context-vs-no-context.svg | Jawbone mapped in place vs. same bone isolated in a box |
| 5 | digging-03-context-and-records | digging-03-field-notebook-grid.svg | Grid square with numbered bones + open field notebook page |
| 6 | fossils-01-body-and-trace | fossils-01-body-vs-trace.svg | 4 body fossils vs. 4 trace fossils gallery |
| 7 | fossils-02-how-fossils-form | fossils-02-burial-mineralization.svg | 4-step burial and mineralization sequence |
| 8 | fossils-02-how-fossils-form | fossils-02-mold-and-cast.svg | 3-step mold and natural-cast formation |
| 9 | fossils-02-how-fossils-form | fossils-02-special-preservation.svg | Amber insect, tar-seep bones, permafrost mammoth calf |
| 10 | fossils-03-why-fossils-are-rare | fossils-03-two-paths.svg | Branching flowchart: common decay path vs. rare fossilization path |
| 11 | fieldwork-01-where-to-look | fieldwork-01-prospecting-badlands.svg | Badlands slope with in-situ femur and float trail traced uphill |
| 12 | fieldwork-02-excavating-and-recording | fieldwork-02-tool-progression.svg | Heavy tools for overburden vs. fine tools for the fossil zone |
| 13 | fieldwork-02-excavating-and-recording | fieldwork-02-quarry-grid-map.svg | Overhead 2 m grid map of a bone bed, finds F-101–F-108 |
| 14 | fieldwork-03-plaster-jackets-and-transport | fieldwork-03-plaster-jacket-steps.svg | 5-step plaster jacketing sequence |
| 15 | fieldwork-03-plaster-jackets-and-transport | fieldwork-03-trackway-in-place.svg | Dinosaur trackway recorded in place with tape and tripod camera |
| 16 | lab-01-preparation-and-cataloging | lab-01-preparator-microscope.svg | Prep-lab bench: opened jacket, air scribe, microscope, matrix dish |
| 17 | lab-01-preparation-and-cataloging | lab-01-catalog-specimen-record.svg | Numbered jawbone in cradle linked to label, field, and rock records |
| 18 | lab-02-clues-in-bones-teeth-and-stone | lab-02-tooth-shapes-diets.svg | 4 fossil tooth shapes (slicer, gripper, stripper, grinder) |
| 19 | lab-02-clues-in-bones-teeth-and-stone | lab-02-trackway-posture.svg | Trackway measurements + hind-limb skeleton fit |
| 20 | lab-03-reconstructions-and-many-specimens | lab-03-bone-map.svg | Skeletal bone map: original vs. mirrored/filled vs. missing |
| 21 | lab-03-reconstructions-and-many-specimens | lab-03-ct-scan-skull.svg | Skull exterior vs. CT slice with braincase and hidden teeth |
| 22 | time-01-layers-and-relative-order | time-01-correlating-layers.svg | Two canyon walls linked by dashed correlation lines |
| 23 | time-02-the-geologic-timescale | time-02-geologic-column.svg | 4-tier geologic column with representative fossils |
| 24 | time-03-measuring-and-interpreting-ages | time-03-bracketing-ash-beds.svg | Fossil layer bracketed by two ash beds + zircon zoom-in |
| 25 | windows-01-dunkleosteus-and-ancient-seas | windows-01-dunkleosteus-armor.svg | Annotated Dunkleosteus skull and shoulder shield |
| 26 | windows-02-dinosaurs-on-land | windows-02-sprawling-vs-upright.svg | Sprawling vs. upright pelvis posture comparison |
| 27 | windows-02-dinosaurs-on-land | windows-02-skull-tooth-comparison.svg | Theropod vs. hadrosaur vs. sauropod skulls and teeth |
| 28 | windows-03-ice-age-mammals | windows-03-mammoth-vs-mastodon-molar.svg | Washboard mammoth molar vs. cone-cusped mastodon molar |
| 29 | windows-03-ice-age-mammals | windows-03-smilodon-skull.svg | Smilodon skull with sabers + stocky vs. lean forelimbs |
| 30 | windows-04-famous-fossil-sites | windows-04-la-brea-seep.svg | La Brea style asphalt-seep ecosystem cutaway |
| 31 | active-01-reconstructing-environments | active-01-sedimentary-structures.svg | 4 rock slabs paired with river, lakeshore, sea, swamp |
| 32 | active-02-major-turns-in-the-fossil-record | active-02-kpg-boundary.svg | Column across the end-Cretaceous boundary clay |
| 33 | active-03-surprises-and-ongoing-discovery | active-03-soft-tissue-micro.svg | Bone chip, dissolved vessel-like tubes, zoomed bone cell |

## Judgment calls

- Every placeholder's own Type/Description note asked for an **illustrated
  diagram** (comparisons, sequences, cross-sections, annotated fossil
  sketches), so purpose-built diagrams serve the lessons better than stock
  photos — e.g. no single photograph shows a mammoth molar and a mastodon
  molar side by side with grazing/browsing icons, or the exact five plaster-
  jacketing steps with the lesson's field number.
- Creating all images in-house avoids license verification risk entirely: no
  hotlinks, no uncertain CC attributions, and nothing to re-check when
  `npm run validate` runs its remote-image checks.
- SVG was chosen over PNG for crispness at any screen size and tiny file
  sizes (2–8 KB each). Each file carries its own `<title>`/`<desc>` and every
  Markdown reference has descriptive alt text plus an italic caption.
