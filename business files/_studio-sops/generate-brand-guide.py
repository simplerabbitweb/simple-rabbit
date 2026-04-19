#!/usr/bin/env python3
"""
Simple Rabbit Studio — Client Brand Guide Generator

Fill in the CLIENT dict below, then run:
  python generate-brand-guide.py

Output: [client-slug]-brand-guide.pdf (saved to this folder)
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Flowable,
)
from reportlab.lib.colors import HexColor, black
import os

# ── CLIENT CONFIG ─────────────────────────────────────────────────────────────
# Fill in all values before running. Every [bracket] is a placeholder.

CLIENT = {
    "name":         "[Client Business Name]",
    "slug":         "client-name",       # used for the output filename
    "tagline":      "[One sentence: what they do, for whom, and why it matters.]",
    "ideal_client": "[Who they serve — 1–2 sentences about the person on the other side of their website.]",
    "brand_vibe":   ["[Word 1]", "[Word 2]", "[Word 3]"],
    "cta":          "[Primary CTA →]",
    "website":      "[yourwebsite.com]",
    "email":        "[hello@yourwebsite.com]",
    "phone":        "[(000) 000-0000]",
    "location":     "[City, State]",

    # ── Colors ──
    # List all colors in the client's palette. Each entry renders as a swatch row.
    "colors": [
        {"name": "Primary",       "hex": "#0872CC", "use": "CTAs, links, overlines, active states"},
        {"name": "Primary Dark",  "hex": "#0660AB", "use": "Hover states on primary elements"},
        {"name": "Primary Tint",  "hex": "#E8F1FB", "use": "Tinted backgrounds, bordered accents"},
        {"name": "Black",         "hex": "#000000", "use": "Headings, high-contrast text"},
        {"name": "Dark",          "hex": "#4C4C4B", "use": "Body copy, secondary text"},
        {"name": "Mid",           "hex": "#949698", "use": "Labels, meta text, placeholders"},
        {"name": "Off-White",     "hex": "#F7F7F8", "use": "Section backgrounds, card fills"},
    ],

    # ── Typography ──
    "font_display":        "[Heading Font Name]",
    "font_display_source": "[Google Fonts / System font / Custom]",
    "font_display_use":    "All headings (H1–H4)",

    "font_body":           "[Body Font Name]",
    "font_body_source":    "[Google Fonts / System font / Custom]",
    "font_body_use":       "Body copy, buttons, navigation, inputs",

    "font_mono":           "DM Mono",
    "font_mono_source":    "Google Fonts",
    "font_mono_use":       "Overline labels, tags, metadata",

    # ── Voice & Tone ──
    "voice_do": [
        "Write in second person — address your reader as 'you'",
        "End every CTA with →",
        "Be specific — use real results, timelines, and outcomes",
        "Keep paragraphs to 2–4 sentences",
        "Use active voice in headlines",
    ],
    "voice_dont": [
        "Em-dashes anywhere",
        "Exclamation points on CTAs, buttons, or headlines",
        "Vague claims without proof ('we deliver results')",
        "Filler words: 'game-changing', 'innovative', 'seamless', 'synergy'",
        "Long, dense paragraph blocks",
    ],

    # ── Logo ──
    "logo_rules": [
        "Always use the SVG file — never stretch, recolor, or add effects",
        "Minimum size: 32px tall on screen",
        "On dark backgrounds: use the white/reversed version",
        "On light backgrounds: use the primary/dark version",
        "Maintain clear space equal to the logo height on all sides",
        "Never place the logo over a busy photo without a solid color overlay",
    ],
}

# ── SETUP ─────────────────────────────────────────────────────────────────────
W, H    = letter
MARGIN  = 0.75 * inch
ACCENT  = HexColor(CLIENT["colors"][0]["hex"])
OUTPUT  = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    f"{CLIENT['slug']}-brand-guide.pdf"
)

# ── STYLES ────────────────────────────────────────────────────────────────────
def make_styles():
    mid  = HexColor("#949698")
    dark = HexColor("#4C4C4B")
    return {
        "cover_name": ParagraphStyle(
            "cover_name", fontName="Helvetica-Bold", fontSize=38,
            leading=44, textColor=black, alignment=TA_LEFT,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub", fontName="Helvetica", fontSize=13,
            leading=20, textColor=mid, alignment=TA_LEFT,
        ),
        "cover_tagline": ParagraphStyle(
            "cover_tagline", fontName="Helvetica-Oblique", fontSize=12,
            leading=20, textColor=dark,
        ),
        "section_label": ParagraphStyle(
            "section_label", fontName="Helvetica", fontSize=9,
            leading=14, textColor=ACCENT, spaceBefore=6, spaceAfter=4,
        ),
        "section_heading": ParagraphStyle(
            "section_heading", fontName="Helvetica-Bold", fontSize=22,
            leading=28, textColor=black, spaceAfter=12,
        ),
        "body": ParagraphStyle(
            "body", fontName="Helvetica", fontSize=10,
            leading=17, textColor=dark, spaceAfter=6,
        ),
        "small_bold": ParagraphStyle(
            "small_bold", fontName="Helvetica-Bold", fontSize=9,
            leading=14, textColor=black, spaceAfter=4,
        ),
        "label": ParagraphStyle(
            "label", fontName="Helvetica", fontSize=8,
            leading=12, textColor=mid,
        ),
        "vibe_word": ParagraphStyle(
            "vibe_word", fontName="Helvetica-Bold", fontSize=15,
            leading=22, textColor=ACCENT,
        ),
        "font_name": ParagraphStyle(
            "font_name", fontName="Helvetica-Bold", fontSize=17,
            leading=22, textColor=black, spaceAfter=2,
        ),
        "font_detail": ParagraphStyle(
            "font_detail", fontName="Helvetica", fontSize=9,
            leading=14, textColor=mid, spaceAfter=6,
        ),
        "do_item": ParagraphStyle(
            "do_item", fontName="Helvetica", fontSize=9,
            leading=15, textColor=HexColor("#1A7A4A"),
        ),
        "dont_item": ParagraphStyle(
            "dont_item", fontName="Helvetica", fontSize=9,
            leading=15, textColor=HexColor("#B22222"),
        ),
        "col_header": ParagraphStyle(
            "col_header", fontName="Helvetica-Bold", fontSize=9,
            leading=14, textColor=black, spaceAfter=6,
        ),
        "footer": ParagraphStyle(
            "footer", fontName="Helvetica", fontSize=8,
            leading=12, textColor=mid, alignment=TA_CENTER,
        ),
        "credit": ParagraphStyle(
            "credit", fontName="Helvetica", fontSize=8,
            leading=12, textColor=mid, alignment=TA_CENTER,
        ),
        "cta_display": ParagraphStyle(
            "cta_display", fontName="Helvetica-Bold", fontSize=16,
            leading=22, textColor=ACCENT,
        ),
        "ref_label": ParagraphStyle(
            "ref_label", fontName="Helvetica-Bold", fontSize=9,
            leading=14, textColor=mid,
        ),
        "ref_value": ParagraphStyle(
            "ref_value", fontName="Helvetica", fontSize=9,
            leading=14, textColor=black,
        ),
    }

# ── CUSTOM FLOWABLES ──────────────────────────────────────────────────────────
class AccentRule(Flowable):
    def __init__(self, width, thickness=2):
        super().__init__()
        self.rule_width = width
        self.thickness  = thickness
        self.width      = width
        self.height     = thickness + 10

    def draw(self):
        self.canv.setFillColor(ACCENT)
        self.canv.rect(0, 4, self.rule_width, self.thickness, fill=1, stroke=0)

class LightRule(Flowable):
    def __init__(self, width):
        super().__init__()
        self.width  = width
        self.height = 1

    def draw(self):
        self.canv.setFillColor(HexColor("#DFE0E1"))
        self.canv.rect(0, 0, self.width, 0.5, fill=1, stroke=0)

class ColorSwatch(Flowable):
    def __init__(self, hex_color, size=40):
        super().__init__()
        self.hex_color = hex_color
        self.width     = size
        self.height    = size

    def draw(self):
        self.canv.setFillColor(HexColor(self.hex_color))
        self.canv.setStrokeColor(HexColor("#DFE0E1"))
        self.canv.setLineWidth(0.5)
        self.canv.roundRect(0, 0, self.width, self.height, 3, fill=1, stroke=1)

# ── PAGE CALLBACKS ────────────────────────────────────────────────────────────
def footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(HexColor("#949698"))
    canvas_obj.drawString(MARGIN, 0.45 * inch, CLIENT["name"])
    canvas_obj.drawRightString(W - MARGIN, 0.45 * inch,
                                f"Brand Guide  ·  {CLIENT['website']}")
    canvas_obj.restoreState()

def no_footer(canvas_obj, doc):
    pass

# ── SECTIONS ─────────────────────────────────────────────────────────────────
def cover(story, S):
    content_w = W - 2 * MARGIN
    story.append(Spacer(1, 0.5 * inch))
    story.append(AccentRule(content_w, thickness=3))
    story.append(Spacer(1, 1.3 * inch))
    story.append(Paragraph(CLIENT["name"], S["cover_name"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("Brand Guide", S["cover_sub"]))
    story.append(Spacer(1, 0.45 * inch))
    story.append(Paragraph(f"\u201c{CLIENT['tagline']}\u201d", S["cover_tagline"]))
    story.append(Spacer(1, 2.6 * inch))

    meta = [[CLIENT["location"], CLIENT["website"]],
            [CLIENT["phone"],    CLIENT["email"]]]
    meta_t = Table(meta, colWidths=[content_w / 2] * 2)
    meta_t.setStyle(TableStyle([
        ("FONTNAME",      (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("TEXTCOLOR",     (0, 0), (-1, -1), HexColor("#949698")),
        ("ALIGN",         (1, 0), (1, -1),  "RIGHT"),
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
    ]))
    story.append(meta_t)
    story.append(PageBreak())


def foundation(story, S):
    cw = W - 2 * MARGIN
    story.append(Paragraph("01", S["section_label"]))
    story.append(Paragraph("Brand Foundation", S["section_heading"]))
    story.append(LightRule(cw))
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Guiding Statement", S["small_bold"]))
    story.append(Spacer(1, 5))
    story.append(Paragraph(
        f"\u201c{CLIENT['tagline']}\u201d",
        ParagraphStyle("qs", fontName="Helvetica-Oblique", fontSize=12,
                       leading=20, textColor=HexColor("#4C4C4B"), spaceAfter=4)
    ))
    story.append(Spacer(1, 0.18 * inch))

    story.append(Paragraph("Ideal Client", S["small_bold"]))
    story.append(Spacer(1, 5))
    story.append(Paragraph(CLIENT["ideal_client"], S["body"]))
    story.append(Spacer(1, 0.25 * inch))

    story.append(Paragraph("Brand Vibe", S["small_bold"]))
    story.append(Spacer(1, 8))
    vibe_row = [[Paragraph(w, S["vibe_word"]) for w in CLIENT["brand_vibe"]]]
    vibe_t = Table(vibe_row, colWidths=[cw / 3] * 3)
    vibe_t.setStyle(TableStyle([
        ("ALIGN",         (0, 0), (-1, -1), "LEFT"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(vibe_t)
    story.append(Spacer(1, 0.25 * inch))

    story.append(Paragraph("Primary CTA", S["small_bold"]))
    story.append(Spacer(1, 5))
    story.append(Paragraph(CLIENT["cta"], S["cta_display"]))
    story.append(PageBreak())


def colors(story, S):
    cw = W - 2 * MARGIN
    story.append(Paragraph("02", S["section_label"]))
    story.append(Paragraph("Color Palette", S["section_heading"]))
    story.append(LightRule(cw))
    story.append(Spacer(1, 0.2 * inch))

    for color in CLIENT["colors"]:
        swatch = ColorSwatch(color["hex"], size=42)
        name_p = Paragraph(
            f'<b>{color["name"]}</b><br/>'
            f'<font color="#949698" size="9">{color["hex"]}</font>',
            ParagraphStyle("cn", fontName="Helvetica", fontSize=11,
                           leading=16, textColor=black)
        )
        use_p = Paragraph(color["use"], S["body"])
        row = [[swatch, name_p, use_p]]
        t = Table(row, colWidths=[54, 150, cw - 54 - 150 - 16])
        t.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING",   (0, 0), (0,  0),  0),
            ("LEFTPADDING",   (1, 0), (1,  0),  12),
            ("LEFTPADDING",   (2, 0), (2,  0),  16),
            ("TOPPADDING",    (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LINEBELOW",     (0, 0), (-1,  0), 0.5, HexColor("#DFE0E1")),
        ]))
        story.append(t)

    story.append(PageBreak())


def typography(story, S):
    cw = W - 2 * MARGIN
    story.append(Paragraph("03", S["section_label"]))
    story.append(Paragraph("Typography", S["section_heading"]))
    story.append(LightRule(cw))
    story.append(Spacer(1, 0.2 * inch))

    fonts = [
        {
            "label": "Display — Headings",
            "name":  CLIENT["font_display"],
            "src":   CLIENT["font_display_source"],
            "use":   CLIENT["font_display_use"],
            "sample": "heading that speaks for itself",
            "size":  26,
            "bold":  True,
        },
        {
            "label": "Body — Copy & UI",
            "name":  CLIENT["font_body"],
            "src":   CLIENT["font_body_source"],
            "use":   CLIENT["font_body_use"],
            "sample": "Body copy is warm, specific, and direct. Short paragraphs. Real specifics.",
            "size":  13,
            "bold":  False,
        },
        {
            "label": "Mono — Labels & Tags",
            "name":  CLIENT["font_mono"],
            "src":   CLIENT["font_mono_source"],
            "use":   CLIENT["font_mono_use"],
            "sample": "OVERLINE LABEL  ·  METADATA  ·  TAG",
            "size":  10,
            "bold":  False,
        },
    ]

    for f in fonts:
        story.append(Paragraph(f["label"].upper(), S["section_label"]))
        story.append(Paragraph(f["name"], S["font_name"]))
        story.append(Paragraph(f'{f["src"]}  ·  {f["use"]}', S["font_detail"]))
        sample_fn = "Helvetica-Bold" if f["bold"] else "Helvetica"
        sample_s = ParagraphStyle(
            "fs", fontName=sample_fn,
            fontSize=f["size"], leading=f["size"] * 1.45,
            textColor=HexColor("#4C4C4B"), spaceAfter=4,
        )
        story.append(Paragraph(f["sample"], sample_s))
        story.append(Spacer(1, 0.12 * inch))
        story.append(LightRule(cw))
        story.append(Spacer(1, 0.12 * inch))

    story.append(PageBreak())


def voice(story, S):
    cw   = W - 2 * MARGIN
    col  = (cw - 24) / 2

    story.append(Paragraph("04", S["section_label"]))
    story.append(Paragraph("Voice & Tone", S["section_heading"]))
    story.append(LightRule(cw))
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph(
        "Brand voice: " + "  ·  ".join(CLIENT["brand_vibe"]),
        ParagraphStyle("vr", fontName="Helvetica-Bold", fontSize=11,
                       leading=18, textColor=ACCENT, spaceAfter=14)
    ))

    do_rows   = [[Paragraph("ALWAYS", S["col_header"])]] + \
                [[Paragraph(f"\u2713  {i}", S["do_item"])]   for i in CLIENT["voice_do"]]
    dont_rows = [[Paragraph("NEVER",  S["col_header"])]] + \
                [[Paragraph(f"\u2717  {i}", S["dont_item"])] for i in CLIENT["voice_dont"]]

    max_r = max(len(do_rows), len(dont_rows))
    while len(do_rows)   < max_r: do_rows.append([Spacer(1, 1)])
    while len(dont_rows) < max_r: dont_rows.append([Spacer(1, 1)])

    rows = [[do_rows[i][0], dont_rows[i][0]] for i in range(max_r)]
    two_col = Table(rows, colWidths=[col, col])
    two_col.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (0,  -1), 16),
        ("LINEAFTER",     (0, 0), (0,  -1), 0.5, HexColor("#DFE0E1")),
        ("LEFTPADDING",   (1, 0), (1,  -1), 16),
    ]))
    story.append(two_col)
    story.append(PageBreak())


def logo_usage(story, S):
    cw = W - 2 * MARGIN
    story.append(Paragraph("05", S["section_label"]))
    story.append(Paragraph("Logo Usage", S["section_heading"]))
    story.append(LightRule(cw))
    story.append(Spacer(1, 0.2 * inch))
    for rule in CLIENT["logo_rules"]:
        story.append(Paragraph(f"\u2014  {rule}", S["body"]))
    story.append(PageBreak())


def quick_reference(story, S):
    cw = W - 2 * MARGIN
    story.append(Paragraph("06", S["section_label"]))
    story.append(Paragraph("Quick Reference", S["section_heading"]))
    story.append(LightRule(cw))
    story.append(Spacer(1, 0.2 * inch))

    rows = [
        ("Business",      CLIENT["name"]),
        ("Location",      CLIENT["location"]),
        ("Website",       CLIENT["website"]),
        ("Email",         CLIENT["email"]),
        ("Phone",         CLIENT["phone"]),
        ("Primary CTA",   CLIENT["cta"]),
        ("Brand Vibe",    "  ·  ".join(CLIENT["brand_vibe"])),
        ("Primary Color", f'{CLIENT["colors"][0]["name"]}  —  {CLIENT["colors"][0]["hex"]}'),
        ("Display Font",  f'{CLIENT["font_display"]} ({CLIENT["font_display_source"]})'),
        ("Body Font",     f'{CLIENT["font_body"]} ({CLIENT["font_body_source"]})'),
        ("Mono Font",     f'{CLIENT["font_mono"]} ({CLIENT["font_mono_source"]})'),
    ]

    table_data = [
        [Paragraph(r[0], S["ref_label"]), Paragraph(r[1], S["ref_value"])]
        for r in rows
    ]
    ref_t = Table(table_data, colWidths=[120, cw - 120])
    ref_t.setStyle(TableStyle([
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW",     (0, 0), (-1, -2), 0.5, HexColor("#DFE0E1")),
    ]))
    story.append(ref_t)
    story.append(Spacer(1, 0.55 * inch))
    story.append(Paragraph(
        "Designed by Simple Rabbit Studio  ·  simplerabbit.studio",
        S["credit"]
    ))


# ── BUILD ─────────────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN,  bottomMargin=0.85 * inch,
        title=f"{CLIENT['name']} — Brand Guide",
        author="Simple Rabbit Studio",
    )
    S     = make_styles()
    story = []

    cover(story, S)
    foundation(story, S)
    colors(story, S)
    typography(story, S)
    voice(story, S)
    logo_usage(story, S)
    quick_reference(story, S)

    doc.build(story, onFirstPage=no_footer, onLaterPages=footer)
    print(f"✓  Saved: {OUTPUT}")


if __name__ == "__main__":
    build()
