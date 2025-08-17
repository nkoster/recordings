# Recorders Setup Handleiding & Checklist Generator

Dit project bevat een handleiding voor het opnemen van audio tijdens evenementen met behulp van de **ZOOM H1** en **ZOOM H4 (Essential of Pro)** recorders.  
Daarnaast bevat de repository een script waarmee automatisch een **printbare PDF-checklist** kan worden gegenereerd uit de handleiding.

## Inhoud
- `handleiding.md` – de volledige handleiding inclusief setup-instructies en een ultrakorte checklist
- `create_checklist_pdf.py` – Python script dat de checklist uit `handleiding.md` leest en omzet naar een PDF

## Genereren Checklist

Het is mogelijk om op basis van `handleiding.md` een checklist-PDF te genereren. Dit is handig om te doen na aanpassingen.

### Voorwaarden
- Python 3
- [ReportLab](https://pypi.org/project/reportlab/) library

Installatie van ReportLab:
```bash
pip install reportlab
```

### Checklist PDF maken
Voer het script uit met het pad naar de handleiding als argument:

```bash
python create_checklist_pdf.py handleiding.md
```

De output is standaard een bestand `handleiding.checklist.pdf` in dezelfde map.  
Je kunt ook een eigen bestandsnaam meegeven:

```bash
python create_checklist_pdf.py handleiding.md mijn_checklist.pdf
```

## Voorbeeld
De gegenereerde PDF bevat de sectie **Ultrakorte Checklist** uit de handleiding, overzichtelijk met ronde bullets per recorder.

## Licentie
Dit project is copyright (c) 2025 Patterns Studio. Verspreiding is niet toegestaan zonder toestemming.
