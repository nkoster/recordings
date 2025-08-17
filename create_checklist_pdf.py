#!/usr/bin/env python3
"""
mk_checklist_pdf.py

Gebruik:
  python mk_checklist_pdf.py /pad/naar/handleiding.md [/pad/naar/output.pdf]

Leest een Markdown-bestand, zoekt de sectie 'Ultrakorte Checklist' en zet
de subsections (###) met hun bullets om naar een PDF met standaard ronde bullets.
"""
import sys
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem

def parse_checklist(md_text: str):
    lines = md_text.splitlines()
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("##") and "Ultrakorte Checklist" in line:
            start_idx = i + 1
            break
    if start_idx is None:
        raise ValueError("Kon de sectie 'Ultrakorte Checklist' niet vinden in het Markdown-bestand.")

    sections = {}
    cur_section = None
    items = []

    def commit_section(title, items):
        title = (title or "").strip()
        cleaned = []
        for it in items:
            s = it.strip()
            if not s:
                continue
            if s.startswith("- "):
                s = s[2:].strip()
            if s.startswith("* "):
                s = s[2:].strip()
            cleaned.append(s)
        if title and cleaned:
            sections[title] = cleaned

    i = start_idx
    while i < len(lines):
        line = lines[i].rstrip()

        if line.startswith("## ") and "Ultrakorte Checklist" not in line:
            if cur_section is not None:
                commit_section(cur_section, items)
            break

        if line.startswith("### "):
            if cur_section is not None:
                commit_section(cur_section, items)
            cur_section = line[4:]
            items = []
            i += 1
            continue

        stripped = line.lstrip()
        if stripped.startswith("- ") or stripped.startswith("* "):
            items.append(stripped)

        i += 1

    if cur_section is not None:
        commit_section(cur_section, items)

    if not sections:
        raise ValueError("Geen checklist-items gevonden onder de 'Ultrakorte Checklist' sectie.")
    return sections

def build_pdf(sections, output_path: Path):
    styles = getSampleStyleSheet()
    styleH = styles["Heading1"]
    styleH2 = styles["Heading2"]
    styleN = styles["Normal"]

    doc = SimpleDocTemplate(str(output_path), pagesize=A4)
    story = []

    story.append(Paragraph("Audio-opname Setup – Checklist", styleH))
    story.append(Spacer(1, 12))

    for title, items in sections.items():
        story.append(Paragraph(title, styleH2))
        bullet_list = ListFlowable(
            [ListItem(Paragraph(item, styleN)) for item in items],
            bulletType="bullet",
            start=None,
        )
        story.append(bullet_list)
        story.append(Spacer(1, 12))

    doc.build(story)

def main():
    if len(sys.argv) < 2:
        print("Gebruik: python mk_checklist_pdf.py /pad/naar/handleiding.md [output.pdf]")
        sys.exit(1)
    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"Bestand niet gevonden: {md_path}")
        sys.exit(1)
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else md_path.with_suffix(".checklist.pdf")

    md_text = md_path.read_text(encoding="utf-8")
    sections = parse_checklist(md_text)
    build_pdf(sections, output_path)
    print(f"Gereed: {output_path}")

if __name__ == "__main__":
    main()
