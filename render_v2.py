#!/usr/bin/env python3
"""Render the v2 news-image entry for 24 November 2026 (1024x1024 PNG).

Draws a newspaper front page with PIL: masthead, one lead story with a
small chip illustration, then 33 further dated stories in three columns.
All 34 headlines are real events first reported on 24 November 2026,
verified against news sources on 25 November 2026.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (17, 17, 17)
GREY = (110, 108, 100)
RULE = (60, 58, 52)
LIGHT_RULE = (200, 194, 182)

DJ = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = DJ + "DejaVuSerif-Bold.ttf"
SANS_B = DJ + "DejaVuSans-Bold.ttf"
SANS_R = DJ + "DejaVuSans.ttf"

REGION_COLORS = {
    "NORTH AMERICA": (139, 26, 26),
    "EUROPE": (31, 58, 110),
    "ASIA": (15, 92, 70),
    "MIDDLE EAST": (122, 74, 18),
    "AFRICA": (91, 45, 142),
    "LATIN AMERICA": (14, 107, 122),
    "PACIFIC": (39, 78, 19),
    "SPORT": (138, 26, 75),
    "CULTURE": (68, 68, 68),
}

LEAD = ("HUANG BACK AT NVIDIA",
        "Board reinstates Jensen Huang as president and CEO, days after "
        "his resignation amid allegations a major customer smuggled "
        "advanced chips to China.")

# (region, headline) - 33 items, 3 columns of 11.
STORIES = [
    ("NORTH AMERICA", "Huawei convicted in New York"),
    ("NORTH AMERICA", "Trump orders faster federal executions"),
    ("NORTH AMERICA", "CIA hit by cyberattack"),
    ("NORTH AMERICA", "Justice Dept. charges 800 in scam sweep"),
    ("EUROPE", "NATO jet cleared to fire on Russian missile"),
    ("EUROPE", "Russian drone enters Polish airspace"),
    ("EUROPE", "Zelensky: Ukraine needs EUR 115bn in 2027"),
    ("EUROPE", "COP31 ends with no fossil-fuel deal"),
    ("EUROPE", "EU budget plan rejected"),
    ("EUROPE", "UK energy bills to rise 26%"),
    ("EUROPE", "Sarkozy and Bruni to stand trial"),
    ("EUROPE", "Turkish helicopter crash kills five"),
    ("ASIA", "Russian jets enter Korean defence zone"),
    ("ASIA", "Shenzhou-24 lifts off with first foreign astronaut"),
    ("ASIA", "Seoul offers $375,000 for AI-cheating tips"),
    ("ASIA", "China probes Shanghai party chief"),
    ("ASIA", "Australia inflation hits 4.9%"),
    ("ASIA", "Fiji declares disaster over drought"),
    ("ASIA", "24 killed in Indonesia factory fire"),
    ("MIDDLE EAST", "Israel kills Hamas security chief in Gaza"),
    ("MIDDLE EAST", "Iran vows to break US naval blockade"),
    ("MIDDLE EAST", "Houthi strike on Riyadh tower injures 11"),
    ("MIDDLE EAST", "Houthis close in on Aden"),
    ("MIDDLE EAST", "Baghdad moves to seize Kurdish oilfields"),
    ("AFRICA", "Ukraine says it sank Russian corvette off Libya"),
    ("AFRICA", "Fighting traps Ebola teams in Congo"),
    ("AFRICA", "Senegal reinstated as AFCON champions"),
    ("LATIN AMERICA", "Argentina enters technical recession"),
    ("LATIN AMERICA", "Mexico GDP grows 3.3%"),
    ("LATIN AMERICA", "Car bomb injures 12 in Colombia"),
    ("PACIFIC", "Australia signs Solomons security pact"),
    ("SPORT", "Dancing with the Stars crowns winners"),
    ("CULTURE", "Great British Bake Off crowns Odeniran"),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap by pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 26  # side margin

    # outer frame
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=2)

    # ---- masthead ----
    f_mast = font(SERIF_B, 62)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=f_mast)
    d.text(((W - tw) / 2, 30), title, font=f_mast, fill=INK)
    f_date = font(SANS_B, 20)
    dateline = "TUESDAY, 24 NOVEMBER 2026  -  34 STORIES FROM 9 REGIONS"
    tw = d.textlength(dateline, font=f_date)
    d.text(((W - tw) / 2, 104), dateline, font=f_date, fill=INK)
    d.line([(mx, 134), (W - mx, 134)], fill=RULE, width=3)
    d.line([(mx, 139), (W - mx, 139)], fill=RULE, width=1)

    # ---- lead story ----
    f_kick = font(SANS_B, 13)
    d.text((mx, 152), "LEAD  -  NORTH AMERICA  -  24 NOV 2026",
           font=f_kick, fill=(139, 26, 26))
    f_lead = font(SERIF_B, 46)
    d.text((mx, 172), LEAD[0], font=f_lead, fill=INK)
    f_dek = font(SANS_R, 16)
    for i, line in enumerate(wrap(d, LEAD[1], f_dek, 690)):
        d.text((mx, 232 + i * 22), line, font=f_dek, fill=(40, 38, 34))

    # small chip illustration (Nvidia) on the right of the lead
    cx0, cy0, cx1, cy1 = 762, 152, 998, 292
    d.rounded_rectangle([cx0, cy0, cx1, cy1], radius=10,
                        fill=(24, 28, 24), outline=(180, 150, 60), width=2)
    # pins
    for i in range(5):
        x = cx0 + 28 + i * 40
        d.line([(x, cy0 - 8), (x, cy0)], fill=(180, 150, 60), width=3)
        d.line([(x, cy1), (x, cy1 + 8)], fill=(180, 150, 60), width=3)
    for j in range(3):
        y = cy0 + 32 + j * 38
        d.line([(cx0 - 8, y), (cx0, y)], fill=(180, 150, 60), width=3)
        d.line([(cx1, y), (cx1 + 8, y)], fill=(180, 150, 60), width=3)
    f_chip = font(SANS_B, 34)
    label = "NVDA"
    tw = d.textlength(label, font=f_chip)
    d.text(((cx0 + cx1 - tw) / 2, cy0 + 34), label, font=f_chip,
           fill=(220, 190, 90))
    f_chip2 = font(SANS_B, 13)
    sub = "BACK AT THE TOP"
    tw = d.textlength(sub, font=f_chip2)
    d.text(((cx0 + cx1 - tw) / 2, cy0 + 84), sub, font=f_chip2,
           fill=(200, 200, 190))

    # ---- section strip ----
    d.line([(mx, 312), (W - mx, 312)], fill=RULE, width=2)
    f_sec = font(SANS_B, 15)
    d.text((mx, 322), "THE DAY IN BRIEF", font=f_sec, fill=INK)
    f_sec2 = font(SANS_R, 11)
    note = "ALL STORIES FIRST REPORTED 24 NOV 2026"
    tw = d.textlength(note, font=f_sec2)
    d.text((W - mx - tw, 325), note, font=f_sec2, fill=GREY)

    # ---- story grid: 3 columns x 11 rows ----
    grid_top = 352
    grid_bottom = 984
    row_h = (grid_bottom - grid_top) // 11
    col_x = [26, 356, 686]
    col_w = 312
    f_tag = font(SANS_B, 11)
    f_head = font(SANS_B, 13)

    for i, (region, headline) in enumerate(STORIES):
        col = i // 11
        row = i % 11
        x = col_x[col]
        y = grid_top + row * row_h
        d.text((x, y), region + "  -  24 NOV", font=f_tag,
               fill=REGION_COLORS[region])
        lines = wrap(d, headline, f_head, col_w)[:2]
        for j, line in enumerate(lines):
            d.text((x, y + 15 + j * 17), line, font=f_head, fill=INK)

    # column dividers
    for x in (344, 674):
        d.line([(x, grid_top), (x, grid_bottom)], fill=LIGHT_RULE, width=1)

    # ---- footer ----
    d.line([(mx, 990), (W - mx, 990)], fill=RULE, width=1)
    f_foot = font(SANS_R, 11)
    foot = ("Sources: AP, Reuters, BBC, FT, CBS, France 24, Guardian, CNN, "
            "UN News, USA Today")
    d.text((mx, 996), foot, font=f_foot, fill=GREY)
    f_foot2 = font(SANS_B, 11)
    tw = d.textlength("THE WORLD  -  24 NOV 2026", font=f_foot2)
    d.text((W - mx - tw, 996), "THE WORLD  -  24 NOV 2026",
           font=f_foot2, fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
