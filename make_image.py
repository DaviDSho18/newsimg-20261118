#!/usr/bin/env python3
"""Generate entry.png: a one-image summary of 18 November 2026 world news.

Design: a clean newspaper front page at 1024x1024, tuned to stay legible at
~300px. A masthead names the day ("THE WORLD - WEDNESDAY 18 NOVEMBER 2026"),
then a lead story with a pictogram and five more stories in a grid, each with
a short label, a bold headline and a small vector icon so a viewer who missed
the day can tell what happened from the image alone. Everything is drawn with
PIL primitives (no external images), so the file is small, crisp and legible.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
SS = 2                      # supersample factor for smooth edges
w, h = W * SS, H * SS

INK = (24, 22, 20)
PAPER = (247, 244, 236)
RULE = (60, 56, 52)
RED = (170, 34, 34)
BLUE = (30, 62, 120)
GOLD = (150, 112, 24)
GREEN = (34, 96, 60)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size * SS)


img = Image.new("RGB", (w, h), PAPER)
d = ImageDraw.Draw(img)


def text_c(x, y, s, f, fill=INK):
    d.text((x * SS, y * SS), s, font=f, fill=fill, anchor="mm")


def text_l(x, y, s, f, fill=INK):
    d.text((x * SS, y * SS), s, font=f, fill=fill, anchor="lm")


def wrap(s, f, max_w):
    words, lines, cur = s.split(), [], ""
    for word in words:
        t = (cur + " " + word).strip()
        if d.textlength(t, font=f) <= max_w * SS:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(x, y, s, f, max_w, lh, fill=INK):
    for ln in wrap(s, f, max_w):
        text_l(x, y, ln, f, fill)
        y += lh
    return y


def rule(x0, y, x1, wd=2, fill=RULE):
    d.rectangle([x0 * SS, y * SS, x1 * SS, (y + wd) * SS], fill=fill)


# ---- masthead -------------------------------------------------------------
text_c(W // 2, 48, "THE WORLD", font(SERIF_B, 66), INK)
text_c(W // 2, 100, "WEDNESDAY 18 NOVEMBER 2026", font(SANS_B, 24), RED)
rule(28, 124, W - 28, 4, INK)
rule(28, 131, W - 28, 1, INK)

# ---- lead story (left column) --------------------------------------------
LX, LW = 34, 466
y = 158
text_l(LX, y, "LEAD", font(SANS_B, 17), RED); y += 26
y = para(LX, y, "Trump meets Xi and Putin in Beijing", font(SERIF_B, 44), LW, 48)
y += 8
# pictogram: globe + three flags
d.rectangle([LX * SS, y * SS, (LX + LW) * SS, (y + 150) * SS], outline=RULE, width=2 * SS)
cx, cy, r = (LX + 92) * SS, (y + 75) * SS, 56 * SS
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLUE, width=3 * SS)
d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=BLUE, width=2 * SS)
d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=BLUE, width=2 * SS)
d.line([cx - r, cy, cx + r, cy], fill=BLUE, width=2 * SS)
for i, col in enumerate([RED, GOLD, BLUE]):
    px = (LX + 214 + i * 78) * SS
    d.line([px, (y + 32) * SS, px, (y + 124) * SS], fill=INK, width=3 * SS)
    d.rectangle([px, (y + 32) * SS, px + 50 * SS, (y + 64) * SS], fill=col)
y += 164
y = para(LX, y, "A trilateral summit at APEC: Xi says Russia and China should lead a multipolar world.", font(SERIF, 23), LW, 30)

# ---- five stories (right column) -----------------------------------------
RX, RW = 530, 460
ry = 158
stories = [
    ("EUROPE / WAR", "Ukraine strikes the Kerch Bridge", "A symbolic blow to Putin.", RED),
    ("MIDDLE EAST", "Iran hits Bahrain and Kuwait", "Strikes resume; a ship is hit in Hormuz.", GOLD),
    ("MARKETS", "Nvidia's blockbuster earnings", "Beats forecasts; keeps Jensen Huang out.", BLUE),
    ("US POLITICS", "Democrats flip Alaska", "Peltola wins; the Senate is 56-44.", RED),
    ("RUSSIA", "19 die in a Siberia plane crash", "A military transport goes down.", INK),
]
for tag, head, body, col in stories:
    text_l(RX, ry, tag, font(SANS_B, 16), col); ry += 24
    ry = para(RX, ry, head, font(SERIF_B, 29), RW, 33)
    ry = para(RX, ry, body, font(SERIF, 20), RW, 25)
    ry += 10
    rule(RX, ry, RX + RW, 1, RULE); ry += 14

# ---- bottom strip: science + health --------------------------------------
by = 862
rule(28, by - 16, W - 28, 3, INK)
text_l(34, by + 12, "SPACE", font(SANS_B, 16), GREEN)
text_l(120, by + 12, "Voyager 1 is now one light-day from Earth.", font(SERIF_B, 22), INK)
text_l(34, by + 50, "HEALTH", font(SANS_B, 16), GREEN)
text_l(120, by + 50, "The US loses its measles elimination status.", font(SERIF_B, 22), INK)

# footer rule + date repeat (legibility at small size)
rule(28, 988, W - 28, 2, INK)
text_c(W // 2, 1006, "18 NOVEMBER 2026", font(SANS_B, 20), INK)

img = img.resize((W, H), Image.LANCZOS)
img.save("entry.png", "PNG", optimize=True)
print("wrote entry.png", img.size)
