# Image Credits — Dig School Lesson Images

> **Use note:** this course is built for personal, non-commercial homeschool
> education. Open-licensed images (public domain, CC0, CC BY, CC BY-SA) are
> preferred and used wherever they fit — see each entry below. Where no open
> image fits, a high-quality image from a museum, university, government, or
> educational site may be used instead, with full credit (title, creator or
> institution, source URL, and rights status) recorded here and in the
> caption. All images are stored locally in `public/images/lessons/` — the
> site never hotlinks. (Every image currently in use is open-licensed; no
> non-open images have been needed so far.)

Lesson bodies currently use **49 images**: **31 sourced photographs** and
**18 created SVG diagrams**. The 14 diagrams that photos replaced are no
longer referenced by lessons but their files stay in the repo for the future
illustration pass (regenerable anytime with
`scripts/make-lesson-images.py`). Every image has descriptive alt text and an
italic caption carrying its credit.

- **Location:** `public/images/lessons/*.svg` and `photo-*.jpg`, referenced
  from lesson bodies as `images/lessons/<file>` (the project's local-asset
  format).
- **Total size:** ~142 KB of SVGs + ~5 MB of JPEGs (max 1280px, q80).

## Sourced photographs (31)

Downloaded from Wikimedia Commons with `scripts/download-sourced-images.py`,
which re-checks each file's live license metadata — only public domain, CC0,
CC BY, and CC BY-SA files were accepted. Every photo was visually inspected
before use; three candidates were rejected on inspection (a BLM lab-prep
photo mis-titled as field jackets, an NPS "bake off" cookie photo, and a BLM
rock-face photo with no visible fossil) and are not used.

### First pass (15)

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

### Second pass (16)

| Local file | Source (Wikimedia Commons file page) | Author | License | Used in |
|------------|--------------------------------------|--------|---------|---------|
| `photo-grand-canyon-layers.jpg` | [Grand Canyon layers.jpg](https://commons.wikimedia.org/wiki/File%3AGrand%20Canyon%20layers.jpg) | Mx. Granger | CC0 1.0 | digging-01 (rock layers) |
| `photo-geological-notebook.jpg` | [Geological notebook.jpg](https://commons.wikimedia.org/wiki/File%3AGeological%20notebook.jpg) | PePeEfe | CC BY-SA 3.0 | digging-03 (field notebook) |
| `photo-ammonite-pavement.jpg` | [Ammonite Pavement.jpg](https://commons.wikimedia.org/wiki/File%3AAmmonite%20Pavement.jpg) | RealGatba | CC0 1.0 | fossils-01 (body fossils) |
| `photo-eubrontes-cast.jpg` | [Cast of Eubrontes Gigantis track by Paul Olsen.jpg](https://commons.wikimedia.org/wiki/File%3ACast%20of%20Eubrontes%20Gigantis%20track%20by%20Paul%20Olsen.jpg) | Z22 (track cast prepared by Paul Olsen) | CC BY 3.0 | fossils-01 (trace fossil) + lab-02 (trackway posture) |
| `photo-green-river-fish.jpg` | [Fossil fish, Green River Formation, Ulrich's Quarry, Wyoming, 4.jpg](https://commons.wikimedia.org/wiki/File%3AFossil%20fish%20%28Fossil%20Butte%20Member%2C%20Green%20River%20Formation%2C%20Lower%20Eocene%3B%20Ulrich%27s%20Fossil%20Quarry%2C%20west%20of%20Kemmerer%2C%20Wyoming%2C%20USA%29%204.jpg) | James St. John | CC BY 2.0 | fossils-02 (burial) |
| `photo-steinkern-meretrix.jpg` | [Meretrix intercalaris 01.jpg](https://commons.wikimedia.org/wiki/File%3AMeretrix%20intercalaris%2001.jpg) | H. Zell | CC BY-SA 3.0 | fossils-02 (mold and cast) |
| `photo-brushing-trench-nps.jpg` | [NPS researcher brushing sediment from fossils in a trench.jpg](https://commons.wikimedia.org/wiki/File%3AA%20researcher%20brushes%20away%20sediment%20from%20fossils%20on%20two%20different%20layers%20in%20the%20trench.%20The%20fossils%20on%20each%20step%20are%20from%20%28c86fc8e3-afc9-41c4-83f1-8a5f1b154ad0%29.JPG) | U.S. National Park Service | Public domain | fieldwork-02 (field tools) |
| `photo-cleveland-lloyd-quarry.jpg` | [Cleveland-Lloyd Dinosaur Quarry, Utah (35392587376).jpg](https://commons.wikimedia.org/wiki/File%3ACleveland-Lloyd%20Dinosaur%20Quarry%2C%20Utah%20%2835392587376%29.jpg) | National Park Service | Public domain | fieldwork-02 (quarry bone bed) |
| `photo-museum-cabinets-nps.jpg` | [NPS curatorial cabinets for delicate fossils.jpg](https://commons.wikimedia.org/wiki/File%3ACuratorial%20cabinets%20help%20to%20safely%20house%20the%20most%20sensitive%20objects%20in%20the%20park%27s%20museum%20collections%2C%20such%20as%20delicate%20fossils%20%28666d9bae-f01c-4b55-a679-52c59fbbbcdd%29.JPG) | U.S. National Park Service | Public domain | lab-01 (catalog archive) |
| `photo-trex-tooth-usda.jpg` | [T. rex tooth from the Hell Creek Formation (Passport in Time dig).jpg](https://commons.wikimedia.org/wiki/File%3AA%20Tyrannosaurus%20Rex%20tooth%20found%20by%20Barb%20Beasley%20during%20a%202012%20Passport%20in%20Time%20excavation%20in%20the%20Late%20Cretaceous%20Hell%20Creek%20Formation%20on%20the%20Custer%20National%20Forest%20in%20South%20Dakota%20on%20June%2022%2C%202012.jpg) | U.S. Department of Agriculture | Public domain | lab-02 (tooth and diet) |
| `photo-dino-hall-mount.jpg` | [Dinosaur Hall (10436523194).jpg](https://commons.wikimedia.org/wiki/File%3ADinosaur%20Hall%20%2810436523194%29.jpg) | Gary Todd | CC0 1.0 | lab-03 (reconstructions) |
| `photo-usgs-time-scale.jpg` | [Geologic time scale.jpg](https://commons.wikimedia.org/wiki/File%3AGeologic%20time%20scale.jpg) | United States Geological Survey | Public domain | time-02 (geologic column) |
| `photo-ashfall-rhino-tuff.jpg` | [Teleoceras in volcanic tuff, Ashfall Fossil Beds, Nebraska, 16.jpg](https://commons.wikimedia.org/wiki/File%3ATeleoceras%20major%20%28fossil%20barrel-bodied%20rhino%29%20in%20fossiliferous%20volcanic%20tuff%20%28Ash%20Hollow%20Formation%2C%20Miocene%2C%2011.83%20Ma%3B%20Ashfall%20Fossil%20Beds%2C%20Nebraska%2C%20USA%29%2016.jpg) | James St. John | CC BY 2.0 | time-03 (ash and dating) |
| `photo-trex-skull-mor.jpg` | [Large adult T Rex skull - Custer rex - Museum of the Rockies.jpg](https://commons.wikimedia.org/wiki/File%3ALarge%20adult%20T%20Rex%20skull%20-%20Custer%20rex%20-%20Museum%20of%20the%20Rockies.jpg) | Tim Evanson | CC BY-SA 2.0 | windows-02 (theropod skull) |
| `photo-edmontosaurus-skull.jpg` | [Edmontosaurus regalis skull CMN 2288.png](https://commons.wikimedia.org/wiki/File%3AEdmontosaurus%20regalis%20skull%20CMN%202288.png) | Hai Xing, Jordan C. Mallon and Margaret L. Currie | CC BY 4.0 | windows-02 (hadrosaur skull) |
| `photo-diplodocus-skull.jpg` | [Skull of Adult Diplodocus (36447135976).jpg](https://commons.wikimedia.org/wiki/File%3ASkull%20of%20Adult%20Diplodocus%20%2836447135976%29.jpg) | Gary Todd | CC0 1.0 | windows-02 (sauropod skull) |

## Created diagrams still in lessons (18)

Original hand-built SVGs from `scripts/make-lesson-images.py` (CC0 1.0,
Dig School contributors). Still referenced: `digging-01-hasty-vs-careful`,
`digging-02-archaeology-vs-paleontology`,
`digging-03-context-vs-no-context`, `fossils-03-two-paths`,
`fieldwork-01-prospecting-badlands`,
`fieldwork-03-plaster-jacket-steps`,
`fieldwork-03-trackway-in-place`, `lab-01-preparator-microscope`,
`lab-03-ct-scan-skull`, `time-01-correlating-layers`,
`windows-01-dunkleosteus-armor`, `windows-02-sprawling-vs-upright`,
`windows-03-mammoth-vs-mastodon-molar`, `windows-03-smilodon-skull`,
`windows-04-la-brea-seep`, `active-01-sedimentary-structures`,
`active-02-kpg-boundary`, `active-03-soft-tissue-micro`.
The 14 retired SVG files remain on disk for the future illustration pass (a 15th, special-preservation, was deleted earlier).

## Placeholder status (all 33)

| # | Placeholder (lesson) | Current image(s) | Source / rights |
|---|----------------------|------------------|-----------------|
| 1 | Hasty vs. careful dig (digging-01) | SVG diagram | Created, CC0 — needs generated illustration |
| 2 | Layers stack up (digging-01) | Grand Canyon layers photo | Mx. Granger, CC0 |
| 3 | Arch vs. paleo (digging-02) | SVG diagram | Created, CC0 — needs generated illustration |
| 4 | Context vs. no context (digging-03) | SVG diagram | Created, CC0 — needs generated illustration |
| 5 | Notebook + grid map (digging-03) | Field notebook photo | PePeEfe, CC BY-SA 3.0 |
| 6 | Body vs. trace gallery (fossils-01) | Ammonite pavement (CC0) + Eubrontes cast (CC BY 3.0) photos | RealGatba; Z22 |
| 7 | Burial + mineralization (fossils-02) | Green River fossil fish photo | James St. John, CC BY 2.0 |
| 8 | Mold and cast (fossils-02) | Clam steinkern photo | H. Zell, CC BY-SA 3.0 |
| 9 | Special preservation (fossils-02) | Amber fly + tar bubble + Lyuba photos | CC BY-SA 4.0 / 2.5 / 2.0 |
| 10 | Two paths (fossils-03) | SVG diagram | Created, CC0 — needs generated illustration |
| 11 | Prospecting badlands (fieldwork-01) | Badlands photo + SVG diagram | MichaelKirsh, CC BY-SA 4.0 + created CC0 |
| 12 | Tool progression (fieldwork-02) | NPS brushing photo | U.S. National Park Service, public domain |
| 13 | Quarry grid map (fieldwork-02) | Cleveland-Lloyd bone bed photo | National Park Service, public domain |
| 14 | Plaster jacket steps (fieldwork-03) | SVG diagram | Created, CC0 — needs generated illustration |
| 15 | Trackway in place (fieldwork-03) | Lark Quarry photo + SVG diagram | Carole Mackinney, CC0 + created CC0 |
| 16 | Preparator + microscope (lab-01) | NPS prep-lab photo + SVG diagram | NPS, public domain + created CC0 |
| 17 | Catalog specimen + record (lab-01) | Museum cabinets photo | U.S. National Park Service, public domain |
| 18 | Tooth shapes + diets (lab-02) | T. rex tooth photo | U.S. Dept. of Agriculture, public domain |
| 19 | Trackway + posture (lab-02) | Eubrontes cast photo | Z22, CC BY 3.0 |
| 20 | Bone map (lab-03) | Dinosaur hall mounts photo | Gary Todd, CC0 |
| 21 | CT scan skull (lab-03) | Massospondylus CT + SVG diagram | PLOS ONE CC BY 2.5 + created CC0 |
| 22 | Correlating layers (time-01) | SVG diagram | Created, CC0 — needs generated illustration |
| 23 | Geologic column (time-02) | USGS time scale | U.S. Geological Survey, public domain |
| 24 | Bracketing ash beds (time-03) | Ashfall rhino in tuff photo | James St. John, CC BY 2.0 |
| 25 | Dunkleosteus armor (windows-01) | Engelman reconstruction + SVG diagram | CC BY 4.0 + created CC0 |
| 26 | Sprawling vs. upright (windows-02) | SVG diagram | Created, CC0 — needs generated illustration |
| 27 | Skull/tooth comparison (windows-02) | T. rex + Edmontosaurus + Diplodocus skull photos | CC BY-SA 2.0 / CC BY 4.0 / CC0 |
| 28 | Mammoth vs. mastodon molars (windows-03) | 2 PD plates + SVG diagram | Public domain + created CC0 |
| 29 | Smilodon skull (windows-03) | AMNH skull photo + SVG diagram | CC BY-SA 4.0 + created CC0 |
| 30 | La Brea seep (windows-04) | Dire-wolf wall photo + SVG diagram | CC BY-SA 2.5 + created CC0 |
| 31 | Sedimentary structures (active-01) | Ripple + mudcrack photos + SVG diagram | CC BY 2.0 each + created CC0 |
| 32 | K-Pg boundary (active-02) | Colorado outcrop photo + SVG diagram | CC BY 4.0 + created CC0 |
| 33 | Soft-tissue microscopy (active-03) | SVG diagram | Created, CC0 — needs generated illustration |

## Still needs a generated illustration (8)

1. Hasty vs. careful dig — conceptual contrast; no single photo shows both.
2. Archaeology vs. paleontology — three-row comparison chart.
3. Context vs. no context — paired in-place/mapped vs. boxed contrast (the one candidate photo showed no clear fossil).
4. Two paths after death — branching flowchart.
5. Plaster jacket steps — five-step field sequence (no reusable field photo found after four queries and two visual rejections).
6. Sprawling vs. upright posture — hip-structure contrast.
7. Correlating layers across two canyon walls — two-wall matching diagram.
8. Soft-tissue microscopy — T. rex vessel/osteocyte views (key figures sit in non-open journal papers; CC BY bone-histology figures found show other taxa).
