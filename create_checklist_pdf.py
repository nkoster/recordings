from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem

# Output PDF path
pdf_path = "/tmp/audio_setup_checklist_standard_bullets.pdf"

# Document setup
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
styleH = styles["Heading1"]
styleH2 = styles["Heading2"]
styleN = styles["Normal"]

story = []

# Title
story.append(Paragraph("Audio-opname Setup – Checklist", styleH))
story.append(Spacer(1, 12))

# Function to add a checklist section with standard bullets
def add_section(title, items):
    story.append(Paragraph(title, styleH2))
    bullet_list = ListFlowable(
        [ListItem(Paragraph(item, styleN)) for item in items],
        bulletType="bullet",  # standard round bullets
        start=None,
    )
    story.append(bullet_list)
    story.append(Spacer(1, 12))

# Sections
add_section("ZOOM H1 (FOH)", [
    "SD-kaart formatteren",
    "FOH uitgang (pre-fader) → H1 via XLR",
    "Check netspanning actief",
    "Check batterijen",
    "Input LINE, 32-bit float, 48kHz",
    "Rode knop → HOLD",
    "Na afloop: HOLD uit → stop → uit",
])

add_section("ZOOM H4 Essential (DJ Booth)", [
    "SD-kaart formatteren",
    "DJ REC OUT → H4 Essential via XLR",
    "Check netspanning actief",
    "Check batterijen",
    "32-bit float, 48kHz",
    "Rode knop → HOLD",
    "Na afloop: HOLD uit → STOP → uit",
])

add_section("ZOOM H4 Pro (DJ Booth)", [
    "SD-kaart formatteren",
    "DJ REC OUT → H4 Pro via XLR",
    "Check netspanning actief",
    "Check batterijen",
    "Mode: 4CH, 48kHz/24-bit",
    "Rode lampjes checken → niet laten clippen",
    "Rode knop → HOLD",
    "Na afloop: HOLD uit → STOP → uit",
])

# Build PDF
doc.build(story)
pdf_path
