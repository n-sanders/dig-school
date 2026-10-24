# Image Credits — Dig School Lesson Images

Lesson bodies use 47 images: **32 created diagrams** (original SVGs built
with `scripts/make-lesson-images.py`, CC0) and **15 sourced photographs**
(downloaded from Wikimedia Commons with `scripts/download-sourced-images.py`,
stored locally — no hotlinks). Every image has descriptive alt text and an
italic caption; CC BY / CC BY-SA photos also carry their credit in the
caption, as their licenses require.

- **Location:** `public/images/lessons/*.svg` and `photo-*.jpg`, referenced
  from lesson bodies as `images/lessons/<file>` (the project's local-asset
  format).
- **Total size:** 32 SVGs (~142 KB) + 15 JPEGs (~2.2 MB, max 1280px, q80).

## Sourced photographs (15)

Downloaded via the Commons API, which re-checks each file's live license
metadata — only public domain, CC0, CC BY, and CC BY-SA files were accepted.
Each photo below was visually inspected before use; two candidates were
rejected on inspection (a BLM photo of lab prep mis-titled as field jackets,
and an NPS "bake off" cookie photo) and are not used.

| Local file | Source (Wikimedia Commons file page) | Author | License | Used in |
|------------|--------------------------------------|--------|---------|---------|
| `photo-trackway-lark-quarry.jpg` | [Lark Quarry Dinosaur Trackways footprints.jpg](https://commons.wikimedia.org/wiki/File%3ALark%20Quarry%20Dinosaur%20Trackways%20footprints.jpg) | Carole Mackinney | CC0 1.0 | fieldwork-03 (trackway in place) |
| `photo-dunkleosteus-skull-armor.jpg` | [Dunkleosteus terrelli skull and thoracic armour internal view.jpg](https://commons.wikimedia.org/wiki/File%3ADunkleosteus%20terrelli%20skull%20and%20thoracic%20armour%20internal%20view.jpg) | Russell K. Engelman | CC BY 4.0 | windows-01 (Dunkleosteus armor) |
| `photo-smilodon-skull-amnh.jpg` | [AMNH Smilodon fatalis skull, Pleistocene California.jpg](https://commons.wikimedia.org/wiki/File%3AAMNH%20Smilodon%20fatalis%20skull%2C%20Pleistocene%20California.jpg) | Bloopityboop | CC BY-SA 4.0 | windows-03 (Smilodon skull) |
| `photo-mammoth-molar-plate.jpg` | [FMIB 39502 Molar tooth of mammoth (Elephas primigenius)](https://commons.wikimedia.org/wiki/File%3AFMIB%2039502%20Molar%20tooth%20of%20mammoth%20%28Elephas%20primigenius%29-%20a%2C%20grinding%20surface%3B%20b%2C%20side%20view.jpeg) | George Frederick Wright | Public domain | windows-03 (mammoth molar) |
| `photo-mastodon-tooth-plate.jpg` | [FMIB 39517 Tooth of Mastodon Americanus.jpeg](https://commons.wikimedia.org/wiki/File%3AFMIB%2039517%20Tooth%20of%20Mastodon%20Americanus.jpeg) | George Frederick Wright | Public domain | windows-03 (mastodon molar) |
| `photo-prep-lab-condon.jpg` | [Fossil preparation at the Condon Center lab.jpg](https://commons.wikimedia.org/wiki/File%3AFossil%20preparation%20at%20the%20Condon%20Center%20lab.jpg) | John Day Fossil Beds National Monument staff (U.S. National Park Service) | Public domain | lab-01 (preparator at microscope) |
| `photo-massospondylus-ct.jpg` | [Massospondylus CT scans.jpg](https://commons.wikimedia.org/wiki/File%3AMassospondylus%20CT%20scans.jpg) | Sereno et al., PLOS ONE (2007), via the paper's CC BY figure | CC BY 2.5 | lab-03 (CT scan of skull) |
| `photo-badlands-evening.jpg` | [Evening at the Badlands.jpg](https://commons.wikimedia.org/wiki/File%3AEvening%20at%20the%20Badlands.jpg) | MichaelKirsh | CC BY-SA 4.0 | fieldwork-01 (badlands prospecting) |
| `photo-ripple-marks-berea.jpg` | [Symmetrical ripple marks (Berea Sandstone, Ohio, USA).jpg](https://commons.wikimedia.org/wiki/File%3ASymmetrical%20ripple%20marks%20%28Berea%20Sandstone%2C%20Upper%20Devonian%20or%20Lower%20Mississippian%3B%20Sunbury%2C%20Ohio%2C%20USA%29.jpg) | James St. John | CC BY 2.0 | active-01 (sedimentary structures) |
| `photo-mudcracks-goblin-valley.jpg` | [Curled mudcracks (Goblin Valley, Utah, USA) 4.jpg](https://commons.wikimedia.org/wiki/File%3ACurled%20mudcracks%20%28Goblin%20Valley%2C%20Utah%2C%20USA%29%204.jpg) | James St. John | CC BY 2.0 | active-01 (sedimentary structures) |
| `photo-kpg-boundary-colorado.jpg` | [Cretaceous–Paleogene boundary in Colorado 1.JPG](https://commons.wikimedia.org/wiki/File%3ACretaceous%E2%80%93Paleogene%20boundary%20in%20Colorado%201.JPG) | Jeffrey Beall | CC BY 4.0 | active-02 (K-Pg boundary) |
| `photo-dire-wolf-wall-la-brea.jpg` | [Dire Wolf Skulls La Brea 2005-08-01.JPG](https://commons.wikimedia.org/wiki/File%3ADire%20Wolf%20Skulls%20La%20Brea%202005-08-01.JPG) | Pyry Matikainen | CC BY-SA 2.5 | windows-04 (La Brea seep) |
| `photo-amber-fly-baltic.jpg` | [Fossil fly in Baltic amber (50 Ma, Lower Eocene).jpg](https://commons.wikimedia.org/wiki/File%3AFossil%20insect%20%28Diptera%2C%20Nematocera%20in%20Baltic%20amber.%20Age%2050%20Mill.%20years%20%28the%20Lower%20Eocene%29.jpg) | Manukyan Andranik | CC BY-SA 4.0 | fossils-02 (amber preservation) |
| `photo-tar-bubble-la-brea.jpg` | [USA tar bubble la brea CA.jpg](https://commons.wikimedia.org/wiki/File%3AUSA%20tar%20bubble%20la%20brea%20CA.jpg) | Daniel Schwen | CC BY-SA 2.5 | fossils-02 (tar preservation) |
| `photo-lyuba-mammoth.jpg` | [Baby Mammoth Lyuba.jpg](https://commons.wikimedia.org/wiki/File%3ABaby%20Mammoth%20Lyuba.jpg) | Thomas Quine | CC BY-SA 2.0 | fossils-02 (permafrost preservation) |

## Created diagrams (32)

Original hand-built SVGs from `scripts/make-lesson-images.py`
(run: `python3 scripts/make-lesson-images.py`).

- **Author:** Dig School contributors (generated diagrams)
- **License:** CC0 1.0 Universal (public domain dedication).

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
| 9 | fossils-03-why-fossils-are-rare | fossils-03-two-paths.svg | Branching flowchart: common decay path vs. rare fossilization path |
| 10 | fieldwork-01-where-to-look | fieldwork-01-prospecting-badlands.svg | Badlands slope with in-situ femur and float trail traced uphill |
| 11 | fieldwork-02-excavating-and-recording | fieldwork-02-tool-progression.svg | Heavy tools for overburden vs. fine tools for the fossil zone |
| 12 | fieldwork-02-excavating-and-recording | fieldwork-02-quarry-grid-map.svg | Overhead 2 m grid map of a bone bed, finds F-101–F-108 |
| 13 | fieldwork-03-plaster-jackets-and-transport | fieldwork-03-plaster-jacket-steps.svg | 5-step plaster jacketing sequence |
| 14 | fieldwork-03-plaster-jackets-and-transport | fieldwork-03-trackway-in-place.svg | Dinosaur trackway recorded in place with tape and tripod camera |
| 15 | lab-01-preparation-and-cataloging | lab-01-preparator-microscope.svg | Prep-lab bench: opened jacket, air scribe, microscope, matrix dish |
| 16 | lab-01-preparation-and-cataloging | lab-01-catalog-specimen-record.svg | Numbered jawbone in cradle linked to label, field, and rock records |
| 17 | lab-02-clues-in-bones-teeth-and-stone | lab-02-tooth-shapes-diets.svg | 4 fossil tooth shapes (slicer, gripper, stripper, grinder) |
| 18 | lab-02-clues-in-bones-teeth-and-stone | lab-02-trackway-posture.svg | Trackway measurements + hind-limb skeleton fit |
| 19 | lab-03-reconstructions-and-many-specimens | lab-03-bone-map.svg | Skeletal bone map: original vs. mirrored/filled vs. missing |
| 20 | lab-03-reconstructions-and-many-specimens | lab-03-ct-scan-skull.svg | Skull exterior vs. CT slice with braincase and hidden teeth |
| 21 | time-01-layers-and-relative-order | time-01-correlating-layers.svg | Two canyon walls linked by dashed correlation lines |
| 22 | time-02-the-geologic-timescale | time-02-geologic-column.svg | 4-tier geologic column with representative fossils |
| 23 | time-03-measuring-and-interpreting-ages | time-03-bracketing-ash-beds.svg | Fossil layer bracketed by two ash beds + zircon zoom-in |
| 24 | windows-01-dunkleosteus-and-ancient-seas | windows-01-dunkleosteus-armor.svg | Annotated Dunkleosteus skull and shoulder shield |
| 25 | windows-02-dinosaurs-on-land | windows-02-sprawling-vs-upright.svg | Sprawling vs. upright pelvis posture comparison |
| 26 | windows-02-dinosaurs-on-land | windows-02-skull-tooth-comparison.svg | Theropod vs. hadrosaur vs. sauropod skulls and teeth |
| 27 | windows-03-ice-age-mammals | windows-03-mammoth-vs-mastodon-molar.svg | Washboard mammoth molar vs. cone-cusped mastodon molar |
| 28 | windows-03-ice-age-mammals | windows-03-smilodon-skull.svg | Smilodon skull with sabers + stocky vs. lean forelimbs |
| 29 | windows-04-famous-fossil-sites | windows-04-la-brea-seep.svg | La Brea style asphalt-seep ecosystem cutaway |
| 30 | active-01-reconstructing-environments | active-01-sedimentary-structures.svg | 4 rock slabs paired with river, lakeshore, sea, swamp |
| 31 | active-02-major-turns-in-the-fossil-record | active-02-kpg-boundary.svg | Column across the end-Cretaceous boundary clay |
| 32 | active-03-surprises-and-ongoing-discovery | active-03-soft-tissue-micro.svg | Bone chip, dissolved vessel-like tubes, zoomed bone cell |

(The former `fossils-02-special-preservation.svg` was retired: three real
photos now cover its amber/tar/permafrost panels better. It can be
regenerated with `scripts/make-lesson-images.py` if ever needed.)

## Judgment calls

- **Photo + diagram kept together (10 placeholders):** where the photo shows
  the real thing and the diagram explains the process, both earn their place
  — e.g. the Lark Quarry trackway photo plus the documentation diagram, the
  Colorado K-Pg outcrop plus the annotated boundary column, the NPS prep-lab
  photo plus the labelled bench diagram.
- **Photos replaced the diagram (1 placeholder):** fossils-02 special
  preservation — real amber fly, bubbling tar, and Lyuba cover all three
  panels better than the illustration did.
- **Diagram kept, no photo (21 placeholders):** process/comparison diagrams
  that no single photo can show (burial sequence, mold-and-cast, two-paths
  flowchart, quarry grid map, bone map, geologic column, bracketing, layered
  hillside, context comparison, notebook page, tool zones, jacket steps,
  tooth/posture/skull comparisons, correlation, K-Pg column, soft-tissue
  micro-steps) — plus the body-vs-trace gallery, where eight matched photos
  would bloat the page for little gain.
- **Searched but nothing usable:** dinosaur soft-tissue microscopy (no
  reusably licensed T. rex vessel images on Commons; the key figures sit in
  non-CC journal papers, so the diagram stands) and field plaster jacketing
  (two candidates failed visual inspection, noted above).
- SVG was chosen over PNG for diagrams: crisp at any screen size, 2–8 KB
  each, each with `<title>`/`<desc>`.
