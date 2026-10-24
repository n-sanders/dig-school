#!/usr/bin/env python3
"""Generate the 33 lesson diagrams for Dig School as clean, hand-built SVGs.

Every image placeholder in content/lessons/ describes an *illustrated diagram*
(process sequences, comparisons, cross-sections, annotated fossil sketches), so
each one is created here with code rather than sourced as a photo: a diagram
teaches the concept better and keeps a consistent visual style.

Run:  python3 scripts/make-lesson-images.py
Output: public/images/lessons/<name>.svg  (small, web-friendly SVGs)

Style notes: cream page background matching the site, warm rock tones, one
sans-serif stack, large readable labels. No embedded fonts or bitmaps.
"""

from __future__ import annotations

import os
import xml.etree.ElementTree as ET

OUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    ".." if False else "",
)
# Resolve relative to this script: <repo>/scripts/make-lesson-images.py -> <repo>
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(REPO, "public", "images", "lessons")

BG = "#fbf8f3"
INK = "#2a2522"
MUTED = "#6b625b"
BORDER = "#8a7a68"
ACCENT = "#b4561f"
ACCENT_DARK = "#8c3f13"
CARD = "#ffffff"
SAND = "#e8d5ae"
SAND_D = "#d9c39a"
MUD = "#c9a87c"
SHALE = "#b9c2c7"
LIME = "#cfd8c9"
COAL = "#4a4440"
ASH = "#d8cfc4"
GRASS = "#a3b18a"
WATER = "#a9c8d8"
BONE_C = "#efe6d4"
FOSSIL = "#7a5c3e"

FONT = "font-family='system-ui, -apple-system, \"Segoe UI\", Roboto, sans-serif'"


def esc(s: str) -> str:
    return (
        s.replace("&", " and ")
        .replace("<", "(")
        .replace(">", ")")
    )


def T(x, y, s, size=15, anchor="middle", fill=INK, weight="normal", style=""):
    st = f"text-anchor='{anchor}' font-size='{size}' fill='{fill}'"
    if weight != "normal":
        st += f" font-weight='{weight}'"
    if style:
        st += f" font-style='{style}'"
    return f"<text x='{x}' y='{y}' {st} {FONT}>{esc(s)}</text>"


def R(x, y, w, h, fill, stroke=BORDER, rx=8, sw=1.5, extra=""):
    return (
        f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='{rx}' "
        f"fill='{fill}' stroke='{stroke}' stroke-width='{sw}' {extra}/>"
    )


def panel(x, y, w, h, heading, sub=""):
    s = R(x, y, w, h, CARD)
    s += T(x + w / 2, y + 28, heading, 19, weight="bold", fill=ACCENT_DARK)
    if sub:
        s += T(x + w / 2, y + 48, sub, 13, fill=MUTED, style="italic")
    return s


def arrow(x1, y1, x2, y2, color=ACCENT, w=3.5):
    import math

    ang = math.atan2(y2 - y1, x2 - x1)
    L = 12
    p1 = (x2 - L * math.cos(ang - 0.42), y2 - L * math.sin(ang - 0.42))
    p2 = (x2 - L * math.cos(ang + 0.42), y2 - L * math.sin(ang + 0.42))
    return (
        f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' "
        f"stroke-width='{w}' stroke-linecap='round'/>"
        f"<polygon points='{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' fill='{color}'/>"
    )


def bone(x, y, length=90, thick=16, color=BONE_C):
    """Simple long-bone glyph pointing right."""
    h = thick
    return (
        f"<rect x='{x}' y='{y - h / 2}' width='{length}' height='{h}' rx='{h / 2}' "
        f"fill='{color}' stroke='{FOSSIL}' stroke-width='2'/>"
        f"<circle cx='{x + 4}' cy='{y - h / 3}' r='{h / 2.4}' fill='{color}' stroke='{FOSSIL}' stroke-width='2'/>"
        f"<circle cx='{x + 4}' cy='{y + h / 3}' r='{h / 2.4}' fill='{color}' stroke='{FOSSIL}' stroke-width='2'/>"
        f"<circle cx='{x + length - 4}' cy='{y - h / 3}' r='{h / 2.4}' fill='{color}' stroke='{FOSSIL}' stroke-width='2'/>"
        f"<circle cx='{x + length - 4}' cy='{y + h / 3}' r='{h / 2.4}' fill='{color}' stroke='{FOSSIL}' stroke-width='2'/>"
    )


def shell_spiral(cx, cy, r, color=FOSSIL):
    rings = "".join(
        f"<circle cx='{cx}' cy='{cy}' r='{r * f:.1f}' fill='none' stroke='{color}' stroke-width='2'/>"
        for f in (1.0, 0.72, 0.46, 0.24)
    )
    return rings


def footprint(cx, cy, s=1.0, color=FOSSIL):
    toes = "".join(
        f"<ellipse cx='{cx + dx * s:.1f}' cy='{cy - 26 * s:.1f}' rx='{9 * s:.1f}' ry='{13 * s:.1f}' "
        f"fill='{BONE_C}' stroke='{color}' stroke-width='2'/>"
        for dx in (-22, 0, 22)
    )
    pad = (
        f"<ellipse cx='{cx}' cy='{cy}' rx='{20 * s:.1f}' ry='{16 * s:.1f}' "
        f"fill='{BONE_C}' stroke='{color}' stroke-width='2'/>"
    )
    return toes + pad


def fern(cx, cy, h=90, color="#4e7a45"):
    s = f"<line x1='{cx}' y1='{cy}' x2='{cx}' y2='{cy - h}' stroke='{color}' stroke-width='3'/>"
    for i in range(1, 6):
        y = cy - i * h / 6
        w = 26 * (1 - i / 8)
        s += f"<line x1='{cx}' y1='{y}' x2='{cx - w}' y2='{y - 12}' stroke='{color}' stroke-width='2.5'/>"
        s += f"<line x1='{cx}' y1='{y}' x2='{cx + w}' y2='{y - 12}' stroke='{color}' stroke-width='2.5'/>"
    return s


def doc(w, h, title, desc, body):
    return (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' role='img'>"
        f"<title>{esc(title)}</title><desc>{esc(desc)}</desc>"
        f"<rect x='0' y='0' width='{w}' height='{h}' fill='{BG}'/>"
        f"{body}</svg>"
    )


def write(name, w, h, title, desc, body):
    os.makedirs(TARGET, exist_ok=True)
    path = os.path.join(TARGET, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc(w, h, title, desc, body))
    # Validate well-formed XML.
    ET.parse(path)
    return path


# ---------------------------------------------------------------- builders ---

def b_digging_hasty_vs_careful():
    left = panel(20, 20, 370, 440, "Rushing it", "treasure-hunt style")
    left += R(50, 110, 310, 130, "#9a7b55")  # messy hole
    left += "<ellipse cx='205' cy='150' rx='120' ry='45' fill='#5f4630'/>"
    left += "<ellipse cx='205' cy='150' rx='80' ry='28' fill='#3c2c1e'/>"
    # shovel
    left += "<line x1='320' y1='90' x2='250' y2='170' stroke='#6b5233' stroke-width='8' stroke-linecap='round'/>"
    left += "<polygon points='250,170 232,158 244,188' fill='#8a8f96'/>"
    # broken bits
    left += "<polygon points='90,270 120,262 112,286' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
    left += "<polygon points='150,278 178,270 168,292' fill='#d98f8f' stroke='#7a3e3e' stroke-width='2'/>"
    left += T(205, 300, "mixed-up layers", 14, fill="#5f4630", style="italic")
    left += T(205, 340, "cracked bone + pottery", 15)
    left += T(205, 362, "tossed on a dirt pile", 15)
    left += T(205, 410, "clues destroyed", 17, weight="bold", fill="#b3261e")
    left += "<text x='205' y='440' text-anchor='middle' font-size='26' fill='#b3261e' " + FONT + ">✕</text>"

    right = panel(410, 20, 370, 440, "Detective work", "slow scientific dig")
    right += R(440, 110, 310, 130, SAND)
    right += "<rect x='470' y='130' width='250' height='90' fill='none' stroke='#fff' stroke-width='3' stroke-dasharray='8 5'/>"
    right += bone(520, 175, 120, 18)
    # kneeling scientist: head + body + arm with trowel
    right += "<circle cx='640' cy='140' r='14' fill='#e8b98a' stroke='#7a5c3e' stroke-width='2'/>"
    right += "<rect x='622' y='156' width='36' height='50' rx='10' fill='#7a9cc6' stroke='#3e5a7a' stroke-width='2'/>"
    right += "<line x1='628' y1='175' x2='600' y2='185' stroke='#e8b98a' stroke-width='8' stroke-linecap='round'/>"
    right += "<polygon points='600,185 588,182 594,194' fill='#8a8f96'/>"
    right += R(690, 250, 46, 30, CARD)  # notebook
    right += "<line x1='690' y1='260' x2='736' y2='260' stroke='#6b625b' stroke-width='2'/>"
    right += "<line x1='690' y1='268' x2='736' y2='268' stroke='#6b625b' stroke-width='2'/>"
    right += T(595, 300, "string grid + level square", 14, fill=MUTED, style="italic")
    right += T(595, 340, "trowel, brush, ruler,", 15)
    right += T(595, 362, "camera, field notebook", 15)
    right += T(595, 410, "context preserved", 17, weight="bold", fill="#2f7d4a")
    right += "<text x='595' y='440' text-anchor='middle' font-size='26' fill='#2f7d4a' " + FONT + ">✓</text>"
    return 800, 480, left + right


def b_digging_layers():
    b = panel(20, 20, 620, 440, "A hillside cutaway: younger on top, older below")
    layers = [
        (70, 150, 520, 60, "#8a9a5b", "Topsoil: grass roots, modern coin"),
        (70, 210, 520, 80, MUD, "Clay: stone hearth, cooking-pot pieces"),
        (70, 290, 520, 90, SAND_D, "Sandstone: large fossil reptile bone"),
        (70, 380, 520, 60, LIME, "Limestone: ancient seashells"),
    ]
    for x, y, w, h, fill, lab in layers:
        b += R(x, y, w, h, fill)
    b += T(330, 185, "Topsoil: grass roots + a modern coin", 14)
    b += "<circle cx='520' cy='172' r='9' fill='#c9a227' stroke='#7a5c00' stroke-width='2'/>"
    b += "<path d='M120 150 q6 -18 0 -30 M140 150 q-6 -18 0 -30' stroke='#4e7a45' stroke-width='3' fill='none'/>"
    b += T(330, 255, "Clay: stone hearth + cooking-pot pieces", 14)
    b += "<rect x='150' y='232' width='70' height='16' rx='4' fill='#8a8f96' stroke='#555' stroke-width='2'/>"
    b += "<polygon points='480,250 510,244 502,264' fill='#c96f4a' stroke='#7a3e2a' stroke-width='2'/>"
    b += bone(300, 335, 130, 20)
    b += T(330, 348, "Sandstone: fossil reptile bone", 14, fill="#5f4630")
    b += shell_spiral(200, 412, 16) + shell_spiral(420, 412, 13)
    b += T(330, 428, "Limestone: ancient seashells", 14)
    b += arrow(665, 400, 665, 160)
    b += T(700, 240, "deposited", 13, fill=MUTED)
    b += T(700, 258, "later", 13, weight="bold", fill=MUTED)
    b += T(700, 276, "(younger)", 13, fill=MUTED)
    b += T(700, 330, "deposited", 13, fill=MUTED)
    b += T(700, 348, "earlier", 13, weight="bold", fill=MUTED)
    b += T(700, 366, "(older)", 13, fill=MUTED)
    return 800, 480, b


def b_arch_vs_paleo():
    rows = [
        ("Pottery shard", "Brachiopod shell", "flat decorated shard", "ribbed shell"),
        ("Flint arrowhead", "T. rex tooth", "flaked point", "serrated tooth"),
        ("Room foundation", "Skeleton in rock", "walls + hearth (plan)", "articulated bones"),
    ]
    b = T(400, 45, "Same ground, different evidence", 22, weight="bold", fill=ACCENT_DARK)
    b += T(215, 78, "ARCHAEOLOGY: things people made", 16, weight="bold")
    b += T(585, 78, "PALEONTOLOGY: fossils of ancient life", 16, weight="bold")
    y = 100
    for a, c, _, _ in rows:
        b += R(20, y, 370, 108, CARD)
        b += R(410, y, 370, 108, CARD)
        b += T(205, y + 62, a, 16, weight="bold")
        b += T(595, y + 62, c, 16, weight="bold")
        y += 118
    # glyphs row 1
    b += "<polygon points='150,150 260,150 245,185 165,185' fill='#c96f4a' stroke='#7a3e2a' stroke-width='2'/>"
    b += "<circle cx='205' cy='167' r='12' fill='none' stroke='#7a3e2a' stroke-width='2'/>"
    b += shell_spiral(595, 168, 24)
    # row 2
    b += "<polygon points='205,268 178,310 232,310' fill='#9aa0a8' stroke='#555' stroke-width='2'/>"
    b += "<line x1='192' y1='290' x2='218' y2='290' stroke='#555' stroke-width='1.5'/>"
    b += "<polygon points='595,262 575,312 615,312' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
    b += "<line x1='583' y1='280' x2='607' y2='280' stroke='#7a5c3e' stroke-width='1.5'/>"
    b += "<line x1='585' y1='290' x2='605' y2='290' stroke='#7a5c3e' stroke-width='1.5'/>"
    # row 3
    b += R(90, 386, 230, 44, "#d8cfc4")
    b += R(150, 386, 110, 44, "none", stroke="#6b5233")
    b += "<circle cx='205' cy='408' r='10' fill='#b4561f'/>"
    b += bone(500, 400, 110, 14) + bone(520, 420, 80, 12)
    b += R(480, 382, 230, 52, SAND, stroke=BORDER)
    return 800, 470, b


def b_context():
    b = T(400, 45, "Context turns a find into evidence", 22, weight="bold", fill=ACCENT_DARK)
    b += panel(20, 65, 370, 375, "In context: in place")
    b += R(50, 150, 310, 150, SAND_D)
    b += "<line x1='50' y1='200' x2='360' y2='200' stroke='#8a7a68' stroke-width='2' stroke-dasharray='6 4'/>"
    b += bone(130, 225, 130, 20)
    b += shell_spiral(300, 190, 12)
    b += fern(90, 290, 60)
    b += R(300, 120, 44, 22, CARD)  # tag
    b += T(322, 136, "F-14", 13, weight="bold")
    b += T(205, 330, "sandstone = river channel", 14)
    b += T(205, 352, "shells + leaves recorded", 14)
    b += T(205, 374, "depth + orientation mapped", 14)
    b += T(205, 416, "story preserved  ✓", 16, weight="bold", fill="#2f7d4a")
    b += panel(410, 65, 370, 375, "Out of context: no records")
    b += R(460, 170, 270, 130, "#d8cfc4")
    b += bone(520, 235, 130, 20)
    b += T(595, 150, "Location?", 17, weight="bold", fill="#b3261e")
    b += T(595, 330, "Rock layer?", 17, weight="bold", fill="#b3261e")
    b += T(595, 356, "Nearby fossils?", 17, weight="bold", fill="#b3261e")
    b += T(595, 416, "story lost  ✕", 16, weight="bold", fill="#b3261e")
    return 800, 460, b


def b_notebook_grid():
    b = panel(20, 20, 380, 440, "Quarry grid square")
    # grid
    for i in range(5):
        b += f"<line x1='{60 + i * 70}' y1='90' x2='{60 + i * 70}' y2='370' stroke='#6b5233' stroke-width='2'/>"
        b += f"<line x1='60' y1='{90 + i * 70}' x2='340' y2='{90 + i * 70}' stroke='#6b5233' stroke-width='2'/>"
    b += bone(90, 150, 90, 14) + bone(200, 260, 100, 14)
    b += shell_spiral(280, 150, 14)
    b += T(120, 200, "#14 femur", 13, weight="bold")
    b += T(250, 310, "#15 rib", 13, weight="bold")
    b += T(290, 195, "#16 tooth", 13, weight="bold")
    b += T(360, 105, "N ↑", 15, weight="bold")
    b += R(60, 380, 160, 26, CARD) + T(140, 398, "scale: 0-50 cm", 13)
    b += panel(420, 20, 360, 440, "Field notebook page")
    b += R(450, 90, 300, 300, "#fffdf5")
    b += T(600, 120, "Square B-4  ·  June 12", 14, weight="bold")
    b += "<line x1='470' y1='140' x2='730' y2='140' stroke='#b9c2c7' stroke-width='2'/>"
    notes = [
        "sketch of bones #14-16,",
        "compass N, depths in cm,",
        "green-gray mudstone layer,",
        "snail shells + plant bits.",
    ]
    y = 170
    for n in notes:
        b += T(470, y, n, 14, anchor="start")
        y += 30
    b += "<rect x='480' y='300' width='240' height='70' fill='none' stroke='#6b625b' stroke-width='1.5' stroke-dasharray='5 4'/>"
    b += bone(510, 335, 90, 12)
    b += T(600, 420, "everything linked by number", 14, fill=MUTED, style="italic")
    return 800, 480, b


def b_body_vs_trace():
    b = T(400, 45, "Two kinds of fossils", 22, weight="bold", fill=ACCENT_DARK)
    b += T(215, 78, "BODY: parts of the organism", 16, weight="bold")
    b += T(585, 78, "TRACE: signs of activity", 16, weight="bold")
    left_items = ["coiled ammonite shell", "serrated dinosaur tooth", "fern frond in shale", "petrified wood rings"]
    right_items = ["3-toed trackway", "branching burrows", "tooth-scored rib", "coprolite with scales"]
    y = 95
    for i in range(4):
        b += R(20, y, 370, 88, CARD) + T(205, y + 68, left_items[i], 14)
        b += R(410, y, 370, 88, CARD) + T(595, y + 68, right_items[i], 14)
        y += 96
    b += shell_spiral(205, 128, 20)
    b += "<polygon points='205,222 190,258 220,258' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
    b += fern(205, 348, 45)
    b += "<ellipse cx='205' cy='432' rx='30' ry='12' fill='none' stroke='#7a5c3e' stroke-width='2'/>"
    b += "<ellipse cx='205' cy='432' rx='20' ry='7' fill='none' stroke='#7a5c3e' stroke-width='1.5'/>"
    b += footprint(595, 130, 0.8)
    b += "<path d='M555 235 q20 -25 40 0 q20 25 40 0' stroke='#7a5c3e' stroke-width='3' fill='none'/>"
    b += "<path d='M560 250 q18 -20 35 0 q18 20 35 0' stroke='#7a5c3e' stroke-width='3' fill='none'/>"
    b += bone(540, 325, 110, 14)
    b += "<line x1='560' y1='318' x2='575' y2='332' stroke='#555' stroke-width='2'/>"
    b += "<line x1='575' y1='318' x2='590' y2='332' stroke='#555' stroke-width='2'/>"
    b += "<ellipse cx='595' cy='425' rx='26' ry='16' fill='#a98a5f' stroke='#5f4630' stroke-width='2'/>"
    b += "<circle cx='588' cy='422' r='3' fill='#efe6d4'/><circle cx='602' cy='428' r='3' fill='#efe6d4'/>"
    return 800, 500, b


def b_burial_sequence():
    steps = [
        ("1. Quick burial", "fish rests on lake floor;", "mud covers it"),
        ("2. Deep layers", "sediment piles up;", "soft parts decay"),
        ("3. Minerals seep", "groundwater fills", "pores with minerals"),
        ("4. Exposure", "erosion reveals", "the fossil again"),
    ]
    b = ""
    x = 15
    for i, (h, l1, l2) in enumerate(steps):
        b += panel(x, 20, 185, 380, h)
        b += R(x + 12, 110, 161, 150, SAND_D if i < 3 else SHALE)
        if i == 0:
            b += "<ellipse cx='" + str(x + 92) + "' cy='200' rx='45' ry='14' fill='#8fa8b8' stroke='#3e5a6e' stroke-width='2'/>"
            b += "<circle cx='" + str(x + 60) + "' cy='196' r='3' fill='#2a2522'/>"
            b += T(x + 92, 245, "settling mud", 12, fill=MUTED, style="italic")
        elif i == 1:
            for yy, ww in ((130, 161), (155, 161), (180, 161)):
                b += f"<line x1='{x + 12}' y1='{yy}' x2='{x + 173}' y2='{yy}' stroke='#8a7a68' stroke-width='2'/>"
            b += bone(x + 40, 225, 100, 14)
        elif i == 2:
            b += bone(x + 40, 200, 100, 16)
            for dx, dy in ((30, -20), (70, -30), (110, -18), (50, 25), (95, 30)):
                b += f"<circle cx='{x + 40 + dx}' cy='{200 + dy}' r='5' fill='#6fa8c9' stroke='#3e6e8e' stroke-width='1.5'/>"
                b += arrow(x + 40 + dx, 200 + dy + 22, x + 40 + dx, 200 + dy + 6, color="#3e6e8e", w=2)
            b += T(x + 92, 285, "magnified pores fill", 12, fill=MUTED, style="italic")
        else:
            b += "<polygon points='" + str(x + 12) + ",260 " + str(x + 70) + ",110 " + str(x + 130) + ",260' fill='#9a7b55'/>"
            b += bone(x + 55, 215, 80, 14)
        b += T(x + 92, 320, l1, 14)
        b += T(x + 92, 342, l2, 14)
        if i < 3:
            b += arrow(x + 185, 210, x + 213, 210)
        x += 198
    b += T(400, 440, "Soft parts decay; hard bones remain and turn to stone.", 15, fill=MUTED, style="italic")
    return 800, 460, b


def b_mold_cast():
    b = ""
    steps = [
        ("Step 1: shell buried", "ribbed clam in mud that hardens"),
        ("Step 2: mold", "shell dissolves; hollow impression stays"),
        ("Step 3: cast", "minerals fill the mold; stone copy"),
    ]
    x = 20
    for i, (h, sub) in enumerate(steps):
        b += panel(x, 20, 240, 400, h)
        b += R(x + 20, 110, 200, 150, SAND_D)
        if i == 0:
            b += shell_spiral(x + 120, 185, 30, color="#4a6b8a")
        elif i == 1:
            b += "<ellipse cx='" + str(x + 120) + "' cy='185' rx='42' ry='30' fill='#5f4630'/>"
            for r in (34, 24, 14):
                b += f"<ellipse cx='{x + 120}' cy='185' rx='{r}' ry='{r * 0.7:.0f}' fill='none' stroke='#d9c39a' stroke-width='2'/>"
        else:
            b += shell_spiral(x + 120, 185, 30, color=FOSSIL)
            b += T(x + 120, 245, "solid stone copy", 13, fill=MUTED, style="italic")
        b += T(x + 120, 310, sub.split(";")[0], 14)
        if ";" in sub:
            b += T(x + 120, 332, sub.split(";")[1], 14)
        if i < 2:
            b += arrow(x + 240, 185, x + 268, 185)
        x += 260
    return 800, 440, b


def b_special_preservation():
    b = panel(20, 20, 250, 400, "A. Amber")
    b += "<polygon points='60,150 240,150 220,330 80,330' fill='#e8b93c' stroke='#8a6a00' stroke-width='3'/>"
    b += "<ellipse cx='150' cy='245' rx='26' ry='10' fill='#5f4630'/>"
    b += "<circle cx='150' cy='238' r='9' fill='#3c2c1e'/>"
    b += "<ellipse cx='128' cy='232' rx='14' ry='5' fill='#cfd8dc' opacity='0.8'/>"
    b += "<ellipse cx='172' cy='232' rx='14' ry='5' fill='#cfd8dc' opacity='0.8'/>"
    b += T(145, 360, "insect sealed in", 14) + T(145, 382, "tree resin", 14)
    b += panel(280, 20, 250, 400, "B. Tar seep")
    b += R(300, 180, 210, 120, "#3a332e")
    b += "<ellipse cx='405' cy='180' rx='105' ry='16' fill='#241f1c'/>"
    b += bone(350, 230, 110, 16)
    b += T(405, 330, "bones sealed in", 14) + T(405, 352, "sticky asphalt", 14)
    b += T(405, 382, "La Brea style", 13, fill=MUTED, style="italic")
    b += panel(540, 20, 240, 400, "C. Permafrost")
    b += R(560, 150, 200, 120, "#cfe0e8")
    b += "<line x1='560' y1='190' x2='760' y2='190' stroke='#fff' stroke-width='3'/>"
    b += "<ellipse cx='660' cy='235' rx='60' ry='26' fill='#8a6f52' stroke='#5f4630' stroke-width='2'/>"
    b += "<path d='M600 235 q-14 26 -6 44 M620 240 q-10 24 -4 42' stroke='#4a3a28' stroke-width='4' fill='none'/>"
    b += "<circle cx='705' cy='228' r='4' fill='#2a2522'/>"
    b += T(660, 320, "mammoth calf frozen", 14) + T(660, 342, "hair + skin kept", 14)
    b += T(660, 382, "Siberia + Alaska", 13, fill=MUTED, style="italic")
    return 800, 440, b


def b_two_paths():
    b = T(400, 40, "Two paths after death", 22, weight="bold", fill=ACCENT_DARK)
    b += R(300, 65, 200, 50, CARD) + T(400, 96, "An organism dies", 16, weight="bold")
    b += arrow(400, 115, 140, 150)
    b += arrow(400, 115, 660, 150)
    b += R(20, 150, 240, 60, "#fbe6e4", stroke="#b3261e") + T(140, 172, "COMMON PATH", 15, weight="bold", fill="#b3261e")
    b += T(140, 194, "almost all organisms", 13, fill=MUTED, style="italic")
    b += R(540, 150, 240, 60, "#e4f4e9", stroke="#2f7d4a") + T(660, 172, "RARE PATH", 15, weight="bold", fill="#2f7d4a")
    b += T(660, 194, "needs the right conditions", 13, fill=MUTED, style="italic")
    left_steps = ["Scavengers scatter it", "Bacteria + fungi rot it", "Sun + weather wear it", "Recycled into soil: NO FOSSIL"]
    y = 230
    for s in left_steps:
        fill = "#fbe6e4" if "NO FOSSIL" in s else CARD
        b += R(20, y, 240, 44, fill, stroke="#b3261e" if "NO FOSSIL" in s else BORDER)
        b += T(140, y + 28, s, 14, weight="bold" if "NO FOSSIL" in s else "normal")
        if y < 230 + 3 * 56:
            b += arrow(140, y + 44, 140, y + 56, color="#b3261e", w=2.5)
        y += 56
    right_steps = ["Rapid burial in mud/sand", "Hidden from air + scavengers", "Minerals harden it in rock", "Preserved FOSSIL specimen"]
    y = 230
    for s in right_steps:
        fill = "#e4f4e9" if "FOSSIL" in s else CARD
        b += R(540, y, 240, 44, fill, stroke="#2f7d4a" if "FOSSIL" in s else BORDER)
        b += T(660, y + 28, s, 14, weight="bold" if "FOSSIL" in s else "normal")
        if y < 230 + 3 * 56:
            b += arrow(660, y + 44, 660, y + 56, color="#2f7d4a", w=2.5)
        y += 56
    return 800, 480, b


def b_prospecting():
    b = panel(20, 20, 760, 420, "Follow the float uphill to the source layer")
    # hillside bands
    b += "<polygon points='60,360 60,140 740,100 740,360' fill='" + SAND + "'/>"
    b += "<polygon points='60,300 740,262 740,300 60,338' fill='" + MUD + "'/>"
    b += "<polygon points='60,230 740,192 740,226 60,264' fill='" + SHALE + "'/>"
    b += T(150, 170, "sandstone", 13, fill=MUTED) + T(150, 250, "mudstone layer", 13, fill=MUTED)
    # in-situ femur
    b += bone(430, 248, 90, 16)
    b += T(475, 225, "fossil still in the layer!", 14, weight="bold", fill=ACCENT_DARK)
    # float trail
    for i, (fx, fy, s) in enumerate([(400, 300, 7), (340, 322, 6), (285, 336, 5), (235, 348, 4)]):
        b += f"<rect x='{fx}' y='{fy}' width='{s * 2}' height='{s}' rx='2' fill='{BONE_C}' stroke='{FOSSIL}' stroke-width='1.5'/>"
    b += T(300, 388, "trail of weathered bone scraps (float) washing downhill", 14, fill=MUTED, style="italic")
    # prospector
    b += "<circle cx='620' cy='300' r='13' fill='#e8b98a' stroke='#7a5c3e' stroke-width='2'/>"
    b += "<rect x='604' y='315' width='32' height='46' rx='9' fill='#7a9cc6' stroke='#3e5a6e' stroke-width='2'/>"
    b += "<line x1='620' y1='361' x2='612' y2='392' stroke='#3e5a6e' stroke-width='7' stroke-linecap='round'/>"
    b += "<line x1='620' y1='361' x2='630' y2='392' stroke='#3e5a6e' stroke-width='7' stroke-linecap='round'/>"
    b += R(636, 322, 26, 34, "#a3552f")  # pack
    b += arrow(560, 330, 480, 285, color=ACCENT_DARK)
    b += T(640, 260, "walk uphill,", 14, weight="bold")
    b += T(640, 280, "eyes on ground", 14, weight="bold")
    return 800, 460, b


def b_tool_progression():
    b = panel(20, 20, 440, 440, "Two zones, two tool kits")
    b += R(60, 110, 360, 140, "#9a7b55")
    b += T(240, 135, "BARREN OVERBURDEN", 15, weight="bold", fill="#fff")
    b += T(240, 156, "30+ cm above the fossil", 13, fill="#fff")
    # heavy tools
    b += "<line x1='120' y1='180' x2='90' y2='225' stroke='#6b5233' stroke-width='9' stroke-linecap='round'/>"
    b += "<rect x='70' y='222' width='44' height='14' rx='4' fill='#8a8f96' stroke='#555' stroke-width='2'/>"
    b += T(110, 255, "rock hammer", 12)
    b += "<polygon points='220,180 200,225 240,225' fill='#8a8f96' stroke='#555' stroke-width='2'/>"
    b += "<line x1='220' y1='180' x2='220' y2='160' stroke='#6b5233' stroke-width='8'/>"
    b += T(220, 255, "chisel", 12)
    b += "<line x1='330' y1='175' x2='300' y2='220' stroke='#6b5233' stroke-width='7' stroke-linecap='round'/>"
    b += "<polygon points='300,220 285,212 296,232' fill='#8a8f96'/>"
    b += T(322, 255, "shovel", 12)
    b += R(60, 250, 360, 160, SAND_D)
    b += T(240, 272, "FOSSIL ZONE", 15, weight="bold", fill="#5f4630")
    b += T(240, 292, "within centimetres: small tools only", 13, fill="#5f4630")
    b += bone(130, 345, 120, 16)
    b += "<line x1='300' y1='320' x2='285' y2='345' stroke='#c0c6cc' stroke-width='6' stroke-linecap='round'/>"
    b += T(305, 375, "trowel", 12)
    b += "<line x1='350' y1='318' x2='350' y2='348' stroke='#8a6f52' stroke-width='5'/>"
    b += "<ellipse cx='350' cy='356' rx='12' ry='7' fill='#d9c39a' stroke='#8a6f52' stroke-width='2'/>"
    b += T(350, 388, "brush", 12)
    b += panel(480, 20, 300, 440, "Fine kit")
    items = ["mason's trowel", "dental pick", "soft brush", "consolidant dropper", "calipers + scale bar"]
    y = 120
    for it in items:
        b += R(505, y, 250, 44, CARD) + T(630, y + 28, it, 14)
        y += 56
    b += T(630, 425, "heavy tools never", 14, weight="bold", fill="#b3261e")
    b += T(630, 445, "touch the bone", 14, weight="bold", fill="#b3261e")
    return 800, 480, b


def b_quarry_grid():
    b = panel(20, 20, 560, 440, "Overhead quarry map: 2 m x 2 m bone bed")
    for i in range(5):
        b += f"<line x1='{70 + i * 120}' y1='90' x2='{70 + i * 120}' y2='390' stroke='#6b5233' stroke-width='2'/>"
        b += f"<line x1='70' y1='{90 + i * 75}' x2='550' y2='{90 + i * 75}' stroke='#6b5233' stroke-width='2'/>"
    b += bone(100, 150, 110, 16) + T(155, 185, "F-101 rib", 13, weight="bold")
    b += "<ellipse cx='330' cy='150' rx='34' ry='20' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
    b += T(330, 185, "F-102 pelvis", 13, weight="bold")
    b += bone(430, 250, 95, 15) + T(475, 282, "F-104 femur", 13, weight="bold")
    b += bone(120, 310, 90, 14) + T(165, 342, "F-105 rib", 13, weight="bold")
    b += "<rect x='300' y='300' width='70' height='40' rx='6' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
    b += T(335, 348, "F-106 jaw", 13, weight="bold")
    b += "<ellipse cx='470' cy='340' rx='16' ry='26' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
    b += T(470, 382, "F-108 vert", 13, weight="bold")
    b += T(560, 105, "N ↑", 15, weight="bold")
    b += R(70, 400, 200, 26, CARD) + T(170, 418, "scale bar: 0-50 cm", 13)
    b += arrow(430, 130, 520, 130, color="#3e6e8e")
    b += T(475, 118, "river flow", 12, fill="#3e6e8e", style="italic")
    b += panel(600, 20, 180, 440, "Records")
    recs = ["field nos.", "depths", "orientation", "photos +", "north arrow"]
    y = 130
    for r in recs:
        b += T(690, y, r, 14)
        y += 34
    b += T(690, 340, "map before", 14, weight="bold")
    b += T(690, 362, "anything", 14, weight="bold")
    b += T(690, 384, "moves!", 14, weight="bold")
    return 800, 480, b


def b_plaster_steps():
    steps = [
        ("1. Pedestal", "trench around;", "bone on rock pillar"),
        ("2. Separator", "damp paper over", "the bone surface"),
        ("3. Plaster", "burlap strips in", "plaster, overlapped"),
        ("4. Flip", "undercut base;", "turn block over"),
        ("5. Seal + label", "plaster shut;", "no. + north arrow"),
    ]
    b = ""
    x = 12
    for i, (h, l1, l2) in enumerate(steps):
        b += panel(x, 20, 150, 400, h)
        b += R(x + 15, 120, 120, 130, SAND_D)
        if i == 0:
            b += bone(x + 35, 150, 80, 12)
            b += "<line x1='" + str(x + 15) + "' y1='180' x2='" + str(x + 135) + "' y2='180' stroke='#5f4630' stroke-width='2'/>"
        elif i == 1:
            b += bone(x + 35, 150, 80, 12)
            b += R(x + 30, 138, 90, 26, "#fff", stroke="#8a8f96")
        elif i == 2:
            b += R(x + 25, 130, 100, 60, "#fff", stroke="#8a8f96")
            for yy in (145, 160, 175):
                b += f"<line x1='{x + 25}' y1='{yy}' x2='{x + 125}' y2='{yy}' stroke='#b9c2c7' stroke-width='3'/>"
        elif i == 3:
            b += R(x + 25, 150, 100, 60, "#fff", stroke="#8a8f96")
            b += arrow(x + 40, 130, x + 110, 130)
            b += T(x + 75, 235, "chisels cut base", 11, fill=MUTED)
        else:
            b += R(x + 25, 140, 100, 70, "#fff", stroke="#8a8f96")
            b += T(x + 75, 168, "DS-2026-04", 12, weight="bold")
            b += T(x + 75, 188, "N ↑", 12, weight="bold")
        b += T(x + 75, 300, l1, 13)
        b += T(x + 75, 320, l2, 13)
        x += 156
    b += T(400, 452, "The jacket holds fossil + rock together for the bumpy ride.", 15, fill=MUTED, style="italic")
    return 800, 470, b


def b_trackway_in_place():
    b = panel(20, 20, 760, 400, "A trackway is worth more where it lies: map it, do not move it")
    b += R(50, 110, 700, 220, "#d8cfc4")
    for i, (fx, fy) in enumerate([(200, 180), (300, 230), (400, 180), (500, 230), (600, 180)]):
        b += footprint(fx, fy, 0.9)
    b += "<line x1='120' y1='300' x2='680' y2='300' stroke='#b4561f' stroke-width='3' stroke-dasharray='10 6'/>"
    b += T(400, 325, "measuring tape along the trail", 13, fill=MUTED, style="italic")
    # kneeling scientist + tripod
    b += "<circle cx='150' cy='200' r='12' fill='#e8b98a' stroke='#7a5c3e' stroke-width='2'/>"
    b += "<rect x='136' y='214' width='30' height='40' rx='8' fill='#7a9cc6' stroke='#3e5a6e' stroke-width='2'/>"
    b += R(620, 120, 90, 60, CARD) + T(665, 148, "camera on", 12) + T(665, 164, "tripod", 12)
    b += "<line x1='640' y1='180' x2='630' y2='230' stroke='#555' stroke-width='4'/>"
    b += "<line x1='665' y1='180' x2='665' y2='230' stroke='#555' stroke-width='4'/>"
    b += "<line x1='690' y1='180' x2='700' y2='230' stroke='#555' stroke-width='4'/>"
    b += T(400, 380, "photos + molds + 3-D scans; the rock ledge stays put", 15)
    return 800, 440, b


def b_prep_lab():
    b = panel(20, 20, 760, 420, "Inside the prep lab: rock off, bone kept")
    b += R(60, 120, 680, 200, "#e9e2d6")  # bench
    # microscope on boom
    b += "<rect x='560' y='150' width='20' height='120' fill='#555'/>"
    b += "<line x1='570' y1='160' x2='430' y2='160' stroke='#555' stroke-width='10'/>"
    b += "<rect x='400' y='160' width='60' height='40' rx='8' fill='#3e5a6e'/>"
    b += "<circle cx='430' cy='205' r='8' fill='#9fc3d8'/>"
    # field jacket with skull
    b += R(90, 200, 260, 90, "#fff", stroke="#8a8f96")
    b += "<ellipse cx='220' cy='245' rx='70' ry='26' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
    b += "<circle cx='170' cy='240' r='8' fill='none' stroke='#7a5c3e' stroke-width='2'/>"
    # air scribe + hand
    b += "<line x1='400' y1='230' x2='330' y2='242' stroke='#3e5a6e' stroke-width='9' stroke-linecap='round'/>"
    b += "<circle cx='410' cy='228' r='12' fill='#e8b98a' stroke='#7a5c3e' stroke-width='2'/>"
    # dish + bottle
    b += "<ellipse cx='470' cy='280' rx='45' ry='12' fill='#fff' stroke='#8a8f96' stroke-width='2'/>"
    b += T(470, 305, "matrix + micro-fossils", 12, fill=MUTED, style="italic")
    b += "<rect x='620' y='230' width='30' height='50' rx='6' fill='#9fc3d8' stroke='#3e6e8e' stroke-width='2'/>"
    b += T(635, 300, "adhesive", 12, fill=MUTED, style="italic")
    # callouts
    b += T(220, 140, "plaster jacket, cut open", 14, weight="bold")
    b += T(430, 140, "stereo microscope", 14, weight="bold")
    b += T(400, 380, "air scribe  ·  needle + brush  ·  save every crumb of matrix", 15)
    return 800, 460, b


def b_catalog_record():
    b = panel(20, 20, 360, 400, "Cataloged jawbone")
    b += R(50, 130, 300, 120, "#e9e2d6")  # cradle
    b += "<ellipse cx='200' cy='170' rx='100' ry='26' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
    for tx in (150, 175, 200, 225):
        b += f"<line x1='{tx}' y1='150' x2='{tx}' y2='190' stroke='#7a5c3e' stroke-width='2'/>"
    b += "<circle cx='200' cy='170' r='20' fill='none' stroke='#b4561f' stroke-width='2.5'/>"
    b += T(200, 176, "2026-118", 12, weight="bold", fill=ACCENT_DARK)
    b += T(200, 300, "number painted on bone", 14)
    b += T(200, 322, "padded cradle in drawer", 14)
    b += T(200, 380, "one number links it all", 15, weight="bold", fill=ACCENT_DARK)
    for i, (box, l1, l2) in enumerate([
        ("label card", "species, site,", "collector, date"),
        ("field records", "quarry map,", "photos in place"),
        ("rock record", "layer name,", "neighbour finds"),
    ]):
        y = 60 + i * 120
        b += R(420, y, 340, 100, CARD)
        b += T(590, y + 30, box, 16, weight="bold")
        b += T(590, y + 56, l1, 14)
        b += T(590, y + 78, l2, 14)
        b += arrow(380, 210, 420, y + 50)
    return 800, 440, b


def b_teeth():
    teeth = [
        ("Slicer", "theropod: curved,", "serrated, cuts meat"),
        ("Gripper", "sea reptile: tall cone,", "holds slippery fish"),
        ("Stripper", "sauropod: peg teeth,", "rake leaves off twigs"),
        ("Grinder", "duckbill: dental battery,", "mills tough plants"),
    ]
    b = ""
    x = 12
    for i, (h, l1, l2) in enumerate(teeth):
        b += panel(x, 20, 188, 400, h)
        cx = x + 94
        if i == 0:
            b += "<path d='M" + str(cx) + ",130 q40,60 4,120 q-30,-55 -30,-90 q0,-25 26,-30' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
            b += "<line x1='" + str(cx + 12) + "' y1='170' x2='" + str(cx + 26) + "' y2='170' stroke='#7a5c3e' stroke-width='1.5'/>"
            b += "<line x1='" + str(cx + 12) + "' y1='185' x2='" + str(cx + 22) + "' y2='185' stroke='#7a5c3e' stroke-width='1.5'/>"
        elif i == 1:
            b += "<polygon points='" + str(cx) + ",125 " + str(cx - 20) + ",250 " + str(cx + 20) + ",250' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
        elif i == 2:
            b += "<rect x='" + str(cx - 14) + "' y='130' width='28' height='115' rx='12' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
        else:
            b += "<rect x='" + str(cx - 45) + "' y='150' width='90' height='80' rx='10' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
            for xx in (cx - 22, cx, cx + 22):
                b += f"<line x1='{xx}' y1='150' x2='{xx}' y2='230' stroke='#7a5c3e' stroke-width='2'/>"
            for yy in (170, 190, 210):
                b += f"<line x1='{cx - 45}' y1='{yy}' x2='{cx + 45}' y2='{yy}' stroke='#b49b72' stroke-width='1.5'/>"
        b += T(cx, 300, l1, 13)
        b += T(cx, 322, l2, 13)
        b += T(cx, 368, "see: biting surface", 12, fill=MUTED, style="italic")
        x += 196
    return 800, 440, b


def b_trackway_posture():
    b = panel(20, 20, 400, 420, "The footprints: measurements")
    for i, (fx, fy) in enumerate([(120, 150), (220, 200), (320, 150)]):
        b += footprint(fx, fy, 0.95)
    b += arrow(120, 260, 220, 260, color="#3e6e8e", w=2.5)
    b += T(170, 285, "stride length", 13, fill="#3e6e8e")
    b += arrow(320, 235, 320, 300, color="#3e6e8e", w=2.5)
    b += T(360, 275, "foot length", 12, fill="#3e6e8e")
    b += T(220, 340, "narrow trail, feet under", 14, weight="bold")
    b += T(220, 362, "the body, no tail drag", 14, weight="bold")
    b += T(220, 410, "upright walker", 15, fill="#2f7d4a", weight="bold")
    b += panel(440, 20, 340, 420, "The leg bone: fit")
    b += "<rect x='590' y='110' width='40' height='150' rx='18' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += "<circle cx='610' cy='105' r='22' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += "<ellipse cx='610' cy='275' rx='30' ry='14' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += arrow(590, 180, 540, 180, color="#3e6e8e", w=2.5)
    b += T(520, 160, "hip height", 12, fill="#3e6e8e")
    b += T(610, 330, "hip + knee angles", 14)
    b += T(610, 352, "allow only certain", 14)
    b += T(610, 374, "stances", 14)
    b += T(610, 410, "skeleton shows", 15, fill="#2f7d4a", weight="bold")
    b += T(610, 428, "what was possible", 13, fill=MUTED, style="italic")
    return 800, 460, b


def b_bone_map():
    b = panel(20, 20, 760, 400, "Bone map: dark = real fossil, tan = mirrored/filled, white = missing")
    # simple sauropod-ish silhouette from shapes
    b += "<ellipse cx='400' cy='250' rx='150' ry='55' fill='#d9c39a' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += "<ellipse cx='590' cy='200' rx='55' ry='35' fill='#7a5c3e' stroke='#4a3a28' stroke-width='2.5'/>"
    b += "<rect x='620' y='180' width='90' height='28' rx='12' fill='#7a5c3e' stroke='#4a3a28' stroke-width='2'/>"
    b += "<rect x='250' y='230' width='110' height='26' rx='12' fill='#fff' stroke='#7a5c3e' stroke-width='2' stroke-dasharray='7 5'/>"
    for lx in (300, 350, 450, 500):
        b += f"<rect x='{lx}' y='290' width='22' height='70' rx='10' fill='#d9c39a' stroke='#7a5c3e' stroke-width='2'/>"
    b += "<rect x='520' y='290' width='22' height='70' rx='10' fill='#fff' stroke='#7a5c3e' stroke-width='2' stroke-dasharray='7 5'/>"
    b += T(400, 150, "skull + neck (original)", 14, weight="bold")
    b += T(300, 330, "legs mirrored", 13, fill=MUTED, style="italic")
    b += T(400, 340, "from other side", 13, fill=MUTED, style="italic")
    # legend
    b += R(60, 350, 240, 52, "#7a5c3e") + T(180, 383, "original fossil bone", 13, fill="#fff")
    b += R(310, 350, 230, 52, "#d9c39a") + T(425, 383, "mirrored / second specimen", 13)
    b += R(550, 350, 190, 52, "#fff") + T(645, 383, "still missing", 13)
    return 800, 440, b


def b_ct_skull():
    b = panel(20, 20, 370, 400, "Outside: skull in rock")
    b += R(50, 120, 310, 170, SAND_D)
    b += "<ellipse cx='205' cy='200' rx='110' ry='55' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += "<circle cx='150' cy='190' r='14' fill='none' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += "<polygon points='280,190 310,200 280,212' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
    b += T(205, 330, "what eyes + hands see", 14, fill=MUTED, style="italic")
    b += panel(410, 20, 370, 400, "CT slice: inside the stone")
    b += R(440, 120, 310, 170, "#2e3a44")
    b += "<ellipse cx='595' cy='200' rx='110' ry='55' fill='none' stroke='#9fc3d8' stroke-width='2.5'/>"
    b += "<ellipse cx='595' cy='200' rx='60' ry='28' fill='none' stroke='#9fc3d8' stroke-width='1.5' stroke-dasharray='6 4'/>"
    b += T(595, 205, "braincase cavity", 13, fill="#9fc3d8")
    for tx in (640, 660, 680):
        b += f"<polygon points='{tx},225 {tx - 8},248 {tx + 8},248' fill='#e8d93c' stroke='#8a7a00' stroke-width='1.5'/>"
    b += T(595, 268, "hidden replacement teeth", 13, fill="#e8d93c")
    b += T(595, 330, "what the scanner reveals", 14, fill=MUTED, style="italic")
    b += arrow(390, 220, 410, 220)
    return 800, 440, b


def b_correlation():
    b = panel(20, 20, 350, 400, "West canyon wall")
    west = [(110, 120, 290, 60, "#cfd8c9"), (110, 180, 290, 70, "#c96f4a"), (110, 250, 290, 80, SAND_D), (110, 330, 290, 60, "#d8cfc4")]
    for x, y, w, h, fill in west:
        b += R(x, y, w, h, fill)
    b += T(255, 155, "4: gravel + mammoth molar", 12)
    b += T(255, 220, "3: sandstone + dinosaur bones", 12)
    b += T(255, 292, "2: red shale + fern + tracks", 12)
    b += T(255, 362, "1: limestone + trilobites", 12)
    b += panel(430, 20, 350, 400, "East canyon wall")
    east = [(460, 170, 290, 60, "#cfd8c9"), (460, 230, 290, 80, SAND_D), (460, 310, 290, 70, "#c96f4a"), (460, 380, 290, 40, "#8a9a8b")]
    for x, y, w, h, fill in east:
        b += R(x, y, w, h, fill)
    b += T(605, 205, "4: gravel + mammoth molar", 12)
    b += T(605, 272, "3: sandstone + dinosaur bones", 12)
    b += T(605, 348, "2: red shale + fern + tracks", 12)
    for (x1, y1, x2, y2) in [(400, 150, 460, 200), (400, 215, 460, 270), (400, 290, 460, 345)]:
        b += f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='#b4561f' stroke-width='2.5' stroke-dasharray='9 6'/>"
    b += T(430, 452, "Match rock type + order + fossils to link the two walls into one timeline.", 15, fill=MUTED, style="italic")
    return 800, 470, b


def b_geologic_column():
    tiers = [
        ("CENOZOIC (top)", "mammoth molar · saber-cat skull · oak leaves", "#cfd8c9", 90),
        ("MESOZOIC", "ammonite · Stegosaurus · cycad leaf", "#e8d5ae", 190),
        ("PALEOZOIC", "trilobite · Dunkleosteus · fern frond", "#d8b98a", 290),
        ("PRECAMBRIAN (base)", "stromatolites · Ediacaran fronds", "#b9c2c7", 390),
    ]
    b = panel(150, 20, 400, 430, "The rock column, bottom to top")
    for name, fossils, fill, y in tiers:
        b += R(180, y, 340, 80, fill)
        b += T(350, y + 30, name, 15, weight="bold")
        b += T(350, y + 55, fossils, 12)
    b += T(620, 130, "youngest", 14, fill=MUTED, style="italic")
    b += arrow(620, 150, 620, 400)
    b += T(620, 432, "oldest", 14, fill=MUTED, style="italic")
    b += T(400, 478, "Order = observed layer sequence. Age numbers are the standard scientific framework.", 13, fill=MUTED, style="italic")
    return 800, 495, b


def b_bracketing():
    b = panel(20, 20, 500, 420, "Ash beds bracket the fossil layer")
    layers = [
        ("5. Upper shale", SHALE, 130),
        ("4. ASH BED B (upper)", ASH, 180),
        ("3. Sandstone + dinosaur skeleton", SAND_D, 250),
        ("2. ASH BED A (lower)", ASH, 330),
        ("1. Lower mudstone", MUD, 390),
    ]
    for name, fill, y in layers:
        h = 48 if "ASH" not in name else 42
        b += R(60, y, 380, h, fill, stroke="#b4561f" if "ASH" in name else BORDER, sw=3 if "ASH" in name else 1.5)
        b += T(250, y + 28, name, 14, weight="bold" if "ASH" in name else "normal")
    b += bone(140, 274, 110, 14)
    b += T(400, 250, "younger than A,", 13, fill=ACCENT_DARK, weight="bold")
    b += T(400, 268, "older than B", 13, fill=ACCENT_DARK, weight="bold")
    b += panel(540, 20, 240, 420, "Zircon zoom-in")
    b += "<polygon points='660,140 690,200 660,260 630,200' fill='#c9a0dc' stroke='#5e3a8a' stroke-width='2.5'/>"
    b += T(660, 300, "parent atoms", 13) + T(660, 322, "become daughter", 13) + T(660, 344, "atoms over time", 13)
    b += T(660, 390, "lab measures", 14, weight="bold")
    b += T(660, 412, "each ash bed", 14, weight="bold")
    return 800, 460, b


def b_dunkleosteus():
    b = panel(20, 20, 760, 380, "Dunkleosteus skull + shoulder shield (front third only)")
    # head shield
    b += "<ellipse cx='330' cy='220' rx='170' ry='90' fill='#a8927a' stroke='#4a3a28' stroke-width='3'/>"
    # jaw blades
    b += "<polygon points='430,220 520,205 520,235' fill='#efe6d4' stroke='#4a3a28' stroke-width='2.5'/>"
    b += "<polygon points='430,250 510,250 510,262' fill='#efe6d4' stroke='#4a3a28' stroke-width='2.5'/>"
    b += "<polygon points='520,205 535,198 532,220' fill='#efe6d4' stroke='#4a3a28' stroke-width='2'/>"
    # sclerotic ring
    b += "<circle cx='330' cy='195' r='24' fill='none' stroke='#2e3a44' stroke-width='5'/>"
    b += "<circle cx='330' cy='195' r='10' fill='#2e3a44'/>"
    # hinge
    b += "<line x1='210' y1='150' x2='210' y2='290' stroke='#4a3a28' stroke-width='3' stroke-dasharray='8 5'/>"
    b += T(210, 320, "head-shield hinge", 13, weight="bold")
    b += T(330, 120, "interlocking armor plates", 14, weight="bold")
    b += T(560, 170, "self-sharpening", 13, weight="bold")
    b += T(560, 190, "bony jaw blades", 13, weight="bold")
    b += T(330, 320, "bony eye ring", 13, weight="bold")
    b += T(640, 300, "soft cartilage body", 13, fill=MUTED, style="italic")
    b += T(640, 322, "rarely fossilizes", 13, fill=MUTED, style="italic")
    b += arrow(560, 200, 525, 215, w=2.5)
    b += T(400, 372, "About the length of an adult head and chest - not a 20-foot shark body.", 14, fill=MUTED, style="italic")
    return 800, 420, b


def b_posture():
    b = panel(20, 20, 370, 400, "Sprawling: lizard / crocodile")
    b += "<ellipse cx='205' cy='180' rx='60' ry='30' fill='#8a9a5b' stroke='#3e4a2e' stroke-width='2.5'/>"
    for sx in (-1, 1):
        b += f"<line x1='{205 + sx * 40}' y1='190' x2='{205 + sx * 110}' y2='250' stroke='#3e4a2e' stroke-width='12' stroke-linecap='round'/>"
        b += f"<line x1='{205 + sx * 110}' y1='250' x2='{205 + sx * 110}' y2='300' stroke='#3e4a2e' stroke-width='10' stroke-linecap='round'/>"
    b += T(205, 340, "legs out to the sides,", 14)
    b += T(205, 362, "wide trackway", 14, weight="bold")
    b += panel(410, 20, 370, 400, "Upright: dinosaur")
    b += "<ellipse cx='595' cy='170' rx='55' ry='28' fill='#c9a87c' stroke='#5f4630' stroke-width='2.5'/>"
    b += "<circle cx='560' cy='170' r='12' fill='none' stroke='#b4561f' stroke-width='3'/>"
    b += "<circle cx='630' cy='170' r='12' fill='none' stroke='#b4561f' stroke-width='3'/>"
    for sx in (-1, 1):
        b += f"<line x1='{595 + sx * 25}' y1='190' x2='{595 + sx * 25}' y2='300' stroke='#5f4630' stroke-width='12' stroke-linecap='round'/>"
    b += T(595, 340, "legs straight under body,", 14)
    b += T(595, 362, "narrow straight trail", 14, weight="bold")
    b += T(400, 452, "Open hip socket + inward-angled femur = pillar legs under the body.", 15, fill=MUTED, style="italic")
    return 800, 470, b


def b_skull_compare():
    b = ""
    skulls = [
        ("Theropod", "deep jaws, curved", "serrated slicers"),
        ("Hadrosaur", "beak + dental battery", "grinding mill inside"),
        ("Sauropod", "peg teeth at front,", "a garden rake"),
    ]
    x = 15
    for i, (h, l1, l2) in enumerate(skulls):
        b += panel(x, 20, 255, 400, h)
        cx = x + 127
        if i == 0:
            b += "<ellipse cx='" + str(cx) + "' cy='200' rx='85' ry='50' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
            for tx in (cx + 10, cx + 30, cx + 50):
                b += f"<polygon points='{tx},225 {tx - 9},252 {tx + 9},252' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2'/>"
        elif i == 1:
            b += "<ellipse cx='" + str(cx) + "' cy='200' rx='85' ry='50' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
            b += "<polygon points='" + str(cx + 55) + ",190 " + str(cx + 95) + ",200 " + str(cx + 55) + ",212' fill='#d9c39a' stroke='#7a5c3e' stroke-width='2'/>"
            b += "<rect x='" + str(cx - 40) + "' y='205' width='80' height='30' rx='6' fill='#d9c39a' stroke='#7a5c3e' stroke-width='2'/>"
            for xx in (cx - 20, cx, cx + 20):
                b += f"<line x1='{xx}' y1='205' x2='{xx}' y2='235' stroke='#7a5c3e' stroke-width='2'/>"
        else:
            b += "<ellipse cx='" + str(cx) + "' cy='190' rx='70' ry='42' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
            for k in range(5):
                tx = cx + 30 + k * 12
                b += f"<rect x='{tx}' y='218' width='8' height='30' rx='3' fill='#efe6d4' stroke='#7a5c3e' stroke-width='1.5'/>"
        b += T(cx, 310, l1, 14)
        b += T(cx, 332, l2, 14)
        x += 262
    return 800, 440, b


def b_molar_compare():
    b = panel(20, 20, 375, 400, "Mammoth molar: grazing")
    b += "<ellipse cx='207' cy='170' rx='120' ry='45' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
    for i in range(7):
        px = 107 + i * 30
        b += f"<line x1='{px}' y1='132' x2='{px}' y2='208' stroke='#7a5c3e' stroke-width='4'/>"
    b += T(207, 260, "flat washboard of", 14, weight="bold")
    b += T(207, 282, "parallel enamel plates", 14, weight="bold")
    b += T(207, 320, "grinds gritty steppe grasses", 14)
    b += T(207, 360, "+ grass icon: tufted stalks", 13, fill=MUTED, style="italic")
    b += "<path d='M150 390 q4 -22 0 -34 M170 390 q-4 -22 0 -34 M190 390 q4 -22 0 -34' stroke='#4e7a45' stroke-width='3' fill='none'/>"
    b += panel(405, 20, 375, 400, "Mastodon molar: browsing")
    b += "<ellipse cx='592' cy='170' rx='120' ry='45' fill='#e2cfa8' stroke='#7a5c3e' stroke-width='2.5'/>"
    for i in range(4):
        px = 512 + i * 52
        b += f"<circle cx='{px}' cy='168' r='17' fill='#c9a87c' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += T(592, 260, "rounded cone-like cusps", 14, weight="bold")
    b += T(592, 282, "in pairs, like a nutcracker", 14, weight="bold")
    b += T(592, 320, "crushes twigs, leaves, cones", 14)
    b += fern(592, 392, 40)
    return 800, 440, b


def b_smilodon():
    b = panel(20, 20, 480, 400, "Smilodon skull: built for a deep, precise bite")
    b += "<ellipse cx='260' cy='210' rx='130' ry='70' fill='#efe6d4' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += "<circle cx='200' cy='195' r='16' fill='none' stroke='#7a5c3e' stroke-width='2.5'/>"
    # sabers
    b += "<polygon points='300,250 288,330 312,330' fill='#fff' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += "<polygon points='340,250 330,315 352,315' fill='#fff' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += "<line x1='300' y1='270' x2='300' y2='315' stroke='#b9c2c7' stroke-width='1.5'/>"
    # open jaw
    b += "<line x1='150' y1='260' x2='260' y2='330' stroke='#7a5c3e' stroke-width='10' stroke-linecap='round'/>"
    b += T(260, 300, "jaw opens ~120 deg", 13, fill=MUTED, style="italic")
    b += T(260, 150, "7-inch flattened", 14, weight="bold")
    b += T(260, 172, "serrated canines", 14, weight="bold")
    b += panel(520, 20, 260, 400, "Stocky forelimbs")
    b += "<rect x='580' y='140' width='34' height='130' rx='15' fill='#c9a87c' stroke='#5f4630' stroke-width='2.5'/>"
    b += "<rect x='660' y='140' width='22' height='130' rx='10' fill='#d8cfc4' stroke='#6b625b' stroke-width='2'/>"
    b += T(597, 310, "Smilodon:", 14, weight="bold")
    b += T(597, 332, "bear-thick", 14)
    b += T(671, 310, "lion:", 14, weight="bold")
    b += T(671, 332, "leaner", 14)
    b += T(650, 380, "pin prey first,", 13, fill=MUTED, style="italic")
    b += T(650, 398, "then bite the neck", 13, fill=MUTED, style="italic")
    return 800, 440, b


def b_labrea():
    b = panel(20, 20, 760, 400, "One sticky trap, a whole ecosystem")
    b += R(60, 150, 680, 60, "#a9c8d8")  # water film
    b += T(400, 175, "thin water + fallen leaves hide the asphalt", 14, fill="#2e4a5a", style="italic")
    b += R(60, 210, 680, 170, "#3a332e")
    # trapped mammoth
    b += "<ellipse cx='280' cy='230' rx='70' ry='34' fill='#8a6f52' stroke='#241f1c' stroke-width='2.5'/>"
    b += "<path d='M340 225 q30 10 20 45' stroke='#e8e0cc' stroke-width='9' fill='none'/>"
    # dire wolves + smilodon at edge
    b += "<ellipse cx='500' cy='222' rx='42' ry='20' fill='#6b5a48' stroke='#241f1c' stroke-width='2'/>"
    b += "<ellipse cx='620' cy='222' rx='46' ry='22' fill='#75644f' stroke='#241f1c' stroke-width='2'/>"
    b += "<polygon points='640,232 634,252 648,252' fill='#fff' stroke='#555' stroke-width='1.5'/>"
    b += T(280, 130, "trapped mammoth", 13, weight="bold")
    b += T(540, 130, "dire wolves + Smilodon step in", 13, weight="bold")
    # below surface labels
    b += T(180, 300, "bones pile up", 13, fill="#e8e0cc")
    b += T(400, 320, "pine cones · seeds · beetle shells", 13, fill="#e8e0cc")
    b += T(620, 300, "snails · bird bones", 13, fill="#e8e0cc")
    b += "<circle cx='400' cy='290' r='6' fill='#4e7a45'/><circle cx='430' cy='295' r='4' fill='#c9a227'/>"
    b += T(400, 380, "cool moist woodland + meadow, Ice Age Los Angeles", 14, fill=MUTED, style="italic")
    return 800, 440, b


def b_sediment_structures():
    cells = [
        ("Ripples + pebbles", "river channel", SAND, "wavy current ripples"),
        ("Mud cracks + tracks", "dried lakeshore", MUD, "polygonal cracks"),
        ("Coral + shells", "warm shallow sea", LIME, "packed shells"),
        ("Coal + fern roots", "swamp forest", COAL, "dark plant carbon"),
    ]
    b = ""
    x = 12
    for h, env, fill, note in cells:
        tcol = "#fff" if fill == COAL else INK
        b += R(x, 20, 188, 400, CARD)
        b += T(x + 94, 52, h, 14, weight="bold")
        b += R(x + 14, 75, 160, 180, fill)
        if "Ripples" in h:
            for yy in (120, 145, 170, 195):
                b += f"<path d='M{x + 20} {yy} q15 -12 30 0 q15 12 30 0 q15 -12 30 0 q15 12 30 0' stroke='#8a7a68' stroke-width='2.5' fill='none'/>"
            b += f"<ellipse cx='{x + 94}' cy='235' rx='26' ry='13' fill='#b9c2c7' stroke='#555' stroke-width='2'/>"
        elif "Mud" in h:
            b += f"<polygon points='{x + 40},110 {x + 90},130 {x + 70},180' fill='none' stroke='#5f4630' stroke-width='2.5'/>"
            b += f"<polygon points='{x + 90},130 {x + 140},120 {x + 130},175 {x + 70},180' fill='none' stroke='#5f4630' stroke-width='2.5'/>"
            b += footprint(x + 94, 225, 0.55)
        elif "Coral" in h:
            b += shell_spiral(x + 60, 150, 20) + shell_spiral(x + 125, 180, 16)
            b += f"<path d='M{x + 40} 220 v-40 M{x + 60} 220 v-50 M{x + 80} 220 v-40 M{x + 100} 220 v-50 M{x + 120} 220 v-40' stroke='#7a5c3e' stroke-width='5'/>"
        else:
            b += fern(x + 94, 230, 90, color="#7ab87a")
            b += f"<line x1='{x + 60}' y1='240' x2='{x + 130}' y2='240' stroke='#2a2522' stroke-width='3'/>"
        b += T(x + 94, 290, "= " + env, 14, weight="bold", fill=ACCENT_DARK)
        b += T(x + 94, 320, note, 12, fill=MUTED, style="italic")
        b += T(x + 94, 360, "rock texture", 13)
        b += T(x + 94, 382, "matches living", 13)
        b += T(x + 94, 404, "process today", 13)
        x += 196
    return 800, 440, b


def b_kpg():
    b = panel(150, 20, 500, 420, "Across the end-Cretaceous boundary")
    b += R(200, 90, 400, 100, "#cfd8c9")
    b += T(400, 118, "CENOZOIC layers above", 15, weight="bold", fill="#2f7d4a")
    b += T(400, 142, "mammals diversify · birds · flowering plants", 13)
    b += "<ellipse cx='300' cy='165' rx='30' ry='14' fill='#8a6f52' stroke='#4a3a28' stroke-width='2'/>"
    b += fern(500, 175, 40)
    b += R(200, 190, 400, 26, "#3a332e")
    b += T(400, 208, "boundary clay: iridium · shocked quartz · fern spike", 13, fill="#fff")
    b += R(200, 216, 400, 180, SAND_D)
    b += T(400, 244, "UPPER CRETACEOUS (Mesozoic) below", 15, weight="bold", fill="#5f4630")
    b += "<ellipse cx='260' cy='300' rx='42' ry='24' fill='#6b8a6b' stroke='#2e4a2e' stroke-width='2'/>"
    b += "<polygon points='260,276 246,250 274,250' fill='#6b8a6b' stroke='#2e4a2e' stroke-width='2'/>"
    b += T(260, 340, "T. rex + Triceratops", 12)
    b += shell_spiral(420, 300, 24)
    b += T(420, 340, "ammonite", 12)
    b += "<ellipse cx='540' cy='300' rx='40' ry='14' fill='#5f7a8a' stroke='#2e4a5a' stroke-width='2'/>"
    b += T(540, 340, "mosasaur", 12)
    b += T(400, 380, "below: present · above: gone", 13, weight="bold", fill="#b3261e")
    b += T(75, 200, "mammals", 12, fill=MUTED) + T(75, 300, "dinosaurs", 12, fill=MUTED)
    b += T(725, 200, "grow varied", 12, fill=MUTED) + T(725, 300, "stop here", 12, fill=MUTED)
    return 800, 460, b


def b_soft_tissue():
    b = panel(20, 20, 250, 400, "1. Dense bone chip")
    b += "<polygon points='60,150 240,150 220,300 80,300' fill='#d9cbb2' stroke='#7a5c3e' stroke-width='2.5'/>"
    b += "<circle cx='150' cy='220' r='26' fill='none' stroke='#7a5c3e' stroke-width='2'/>"
    b += T(150, 340, "T. rex femur", 14) + T(150, 362, "(MOR 1125)", 13, fill=MUTED)
    b += panel(280, 20, 250, 400, "2. Mineral dissolved")
    b += R(300, 150, 210, 150, "#eef3f6")
    b += "<path d='M330 260 q20 -60 60 -80 q40 -20 60 -60' stroke='#c96f6f' stroke-width='5' fill='none'/>"
    b += "<path d='M350 270 q30 -40 70 -55' stroke='#c96f6f' stroke-width='4' fill='none'/>"
    for cx, cy in ((380, 210), (395, 200), (410, 192)):
        b += f"<circle cx='{cx}' cy='{cy}' r='6' fill='#8a2e2e'/>"
    b += T(405, 330, "stretchy vessel-like", 14, weight="bold")
    b += T(405, 352, "tubes + cell-like dots", 14)
    b += panel(540, 20, 240, 400, "3. Bone cell zoom")
    b += "<circle cx='660' cy='210' r='30' fill='#e8b9b9' stroke='#8a2e2e' stroke-width='2.5'/>"
    for dx, dy in ((-45, -20), (45, -25), (-40, 25), (42, 22), (0, -48)):
        b += f"<line x1='660' y1='210' x2='{660 + dx}' y2='{210 + dy}' stroke='#8a2e2e' stroke-width='2.5'/>"
    b += T(660, 300, "osteocyte with", 14)
    b += T(660, 322, "branching filaments", 14)
    b += T(660, 362, "snaps back when", 13, fill=MUTED, style="italic")
    b += T(660, 382, "pulled: still flexible", 13, fill=MUTED, style="italic")
    b += arrow(270, 225, 280, 225)
    b += arrow(530, 225, 540, 225)
    return 800, 440, b


BUILDERS = [
    ("digging-01-hasty-vs-careful.svg", "Hasty digging versus careful excavation",
     "Left: messy rushed hole with broken finds. Right: neat gridded square with small tools and records.",
     b_digging_hasty_vs_careful),
    ("digging-01-layers-stack-up.svg", "How rock and soil layers stack up",
     "Hillside cutaway with topsoil, clay hearth layer, fossil sandstone, and shell limestone, youngest on top.",
     b_digging_layers),
    ("digging-02-archaeology-vs-paleontology.svg", "Archaeology versus paleontology comparison",
     "Three rows comparing pottery with shells, arrowhead with tooth, and room foundation with skeleton.",
     b_arch_vs_paleo),
    ("digging-03-context-vs-no-context.svg", "A find with context versus without",
     "Jawbone mapped in its sandstone layer beside the same bone isolated in a box with unknowns.",
     b_context),
    ("digging-03-field-notebook-grid.svg", "Excavation grid square and field notebook page",
     "Numbered bones plotted on a meter grid beside an open notebook with sketch, depths, and layer notes.",
     b_notebook_grid),
    ("fossils-01-body-vs-trace.svg", "Body fossils versus trace fossils gallery",
     "Four body fossils (ammonite, tooth, fern, petrified wood) beside four trace fossils (tracks, burrows, bite marks, coprolite).",
     b_body_vs_trace),
    ("fossils-02-burial-mineralization.svg", "Four-step burial and mineralization sequence",
     "Quick burial, deepening layers, mineral seepage into bone pores, and final exposure by erosion.",
     b_burial_sequence),
    ("fossils-02-mold-and-cast.svg", "How a fossil mold and natural cast form",
     "Buried clam shell, dissolved shell leaving a hollow mold, and minerals filling it into a stone cast.",
     b_mold_cast),
    ("fossils-02-special-preservation.svg", "Special preservation: amber, tar, and ice",
     "Insect in golden amber, bones in a dark tar seep, and a woolly mammoth calf in permafrost.",
     b_special_preservation),
    ("fossils-03-two-paths.svg", "Two paths after death: recycling versus fossilization",
     "Branching flowchart from death to decay and recycling on one side and rare burial and fossilization on the other.",
     b_two_paths),
    ("fieldwork-01-prospecting-badlands.svg", "Prospecting a badlands hillside",
     "Layered slope with a fossil in place and a trail of bone scraps leading a prospector uphill to the source.",
     b_prospecting),
    ("fieldwork-02-tool-progression.svg", "Field tool progression from overburden to bone",
     "Heavy hammers and shovels for barren rock above, fine trowels and brushes within centimetres of the fossil.",
     b_tool_progression),
    ("fieldwork-02-quarry-grid-map.svg", "Overhead quarry grid map of a bone bed",
     "Two-metre string grid over ribs, pelvis, femur, and jaw, each with a field number, north arrow, and river-flow direction.",
     b_quarry_grid),
    ("fieldwork-03-plaster-jacket-steps.svg", "Five steps of plaster jacketing a fossil",
     "Pedestal, separator layer, burlap and plaster, undercut and flip, then seal and label.",
     b_plaster_steps),
    ("fieldwork-03-trackway-in-place.svg", "Dinosaur trackway left in place for study",
     "Footprint trail across a rock ledge recorded with tape, tripod camera, and notes instead of being cut out.",
     b_trackway_in_place),
    ("lab-01-preparator-microscope.svg", "Fossil preparator working under a microscope",
     "Workbench scene with an opened plaster jacket, air scribe, microscope, matrix dish, and adhesive.",
     b_prep_lab),
    ("lab-01-catalog-specimen-record.svg", "Cataloged specimen and its linked archive records",
     "Numbered jawbone in a padded cradle linked to its label card, field records, and rock-layer record.",
     b_catalog_record),
    ("lab-02-tooth-shapes-diets.svg", "Four fossil tooth shapes and their diets",
     "Serrated slicer, conical gripper, peg-like stripper, and ridged grinding battery with magnified biting surfaces.",
     b_teeth),
    ("lab-02-trackway-posture.svg", "Reading a fossil trackway and limb posture",
     "Footprint measurements for stride and stance beside a hind-limb skeleton showing hip height and joint angles.",
     b_trackway_posture),
    ("lab-03-bone-map.svg", "Skeletal reconstruction bone map",
     "Side-view dinosaur skeleton shaded by evidence: original bone, mirrored or second-specimen bone, and missing bone.",
     b_bone_map),
    ("lab-03-ct-scan-skull.svg", "CT scan revealing hidden structures inside a fossil skull",
     "Skull exterior in rock beside a translucent scan showing the braincase cavity and hidden replacement teeth.",
     b_ct_skull),
    ("time-01-correlating-layers.svg", "Matching rock layers and fossils across two canyon walls",
     "Two canyon outcrops with four matching layers each, linked by dashed correlation lines across the valley.",
     b_correlation),
    ("time-02-geologic-column.svg", "The geologic column with representative fossils",
     "Four stacked divisions from Precambrian stromatolites to Cenozoic mammoths, oldest at the base.",
     b_geologic_column),
    ("time-03-bracketing-ash-beds.svg", "Bracketing a fossil layer between volcanic ash beds",
     "Five-layer outcrop with a dinosaur sandstone between two dated ash beds, plus a zircon crystal zoom-in.",
     b_bracketing),
    ("windows-01-dunkleosteus-armor.svg", "Annotated skull and thoracic armor of Dunkleosteus",
     "Armored head shield with eye ring, jaw blades, and neck hinge; soft rear body noted as rarely preserved.",
     b_dunkleosteus),
    ("windows-02-sprawling-vs-upright.svg", "Sprawling reptile posture versus upright dinosaur posture",
     "Front-view pelvis comparison: sideways sprawling legs with a wide trail against pillar legs with a narrow trail.",
     b_posture),
    ("windows-02-skull-tooth-comparison.svg", "Dinosaur skull and tooth comparison",
     "Theropod slicing skull, hadrosaur beak with grinding battery, and sauropod rake-like peg teeth.",
     b_skull_compare),
    ("windows-03-mammoth-vs-mastodon-molar.svg", "Mammoth molar versus mastodon molar",
     "Flat washboard grazing molar with grasses beside cone-cusped browsing molar with twigs.",
     b_molar_compare),
    ("windows-03-smilodon-skull.svg", "Saber-toothed cat skull and forelimb build",
     "Wide-gaping skull with serrated saber canines beside stocky Smilodon and leaner lion forelimbs.",
     b_smilodon),
    ("windows-04-la-brea-seep.svg", "How an asphalt seep captures an entire ecosystem",
     "Cutaway of a La Brea style seep trapping a mammoth while predators gather, with tiny fossils preserved below.",
     b_labrea),
    ("active-01-sedimentary-structures.svg", "Sedimentary structures and the environments they indicate",
     "Four rock slabs paired with their settings: river ripples, cracked mudflat, shell sea, and coal swamp.",
     b_sediment_structures),
    ("active-02-kpg-boundary.svg", "Stratigraphic diagram across the end-Cretaceous boundary",
     "Rock column split by a dark boundary clay: dinosaurs, ammonites, and mosasaurs below; mammals above.",
     b_kpg),
    ("active-03-soft-tissue-micro.svg", "Microscopic view of dinosaur bone soft tissue",
     "Bone chip before and after dissolving the mineral, plus a zoomed branching bone cell.",
     b_soft_tissue),
]


def main():
    total = 0
    for name, title, desc, fn in BUILDERS:
        w, h, body = fn()
        path = write(name, w, h, title, desc, body)
        size = os.path.getsize(path)
        total += size
        print(f"wrote {name} ({w}x{h}, {size / 1024:.1f} KB)")
    print(f"\n{len(BUILDERS)} images, {total / 1024:.0f} KB total in {TARGET}")


if __name__ == "__main__":
    main()
