---
name: dc-feasibility
description: Generate DC property feasibility report. Trigger with "generate feasibility study for [address]". Searches PropertyQuest and Redfin, applies zoning rules, outputs professional PDF.
---

# DC Property Feasibility Report Generator

## Trigger

**User says:** "Generate feasibility study for [ADDRESS]"

**Claude does:**
1. Web search `[address] washington dc propertyquest` → get zone, lot SF, SSL, owner, assessment, ANC/SMD
2. Web search `[address] washington dc redfin` → get year built, living SF, basement SF, stories, bed/bath
3. Apply correct zoning rules (RF-1, RF-2, etc.)
4. Calculate max buildable (lot SF × lot occupancy × stories)
5. Create generator file with all data
6. Run generator → output PDF
7. Present PDF to user

**No user input required beyond the address.**

---

## Data Sources (in order)

| Source | Data | URL |
|--------|------|-----|
| PropertyQuest | Zone, lot SF, SSL, owner, assessment, neighborhood, ANC/SMD | https://propertyquest.dc.gov |
| Redfin | Year built, living SF, basement SF, stories, bed/bath | https://redfin.com |

Flag for user verification (don't block report):
- Ownership → OTR (mytax.dc.gov)
- Permits → Scout DC (scout.dcra.dc.gov)  
- Historic → DC HPO (planning.dc.gov)

---

## File Structure

```
dc-feasibility-skill/
├── SKILL.md                 # This file
├── generate_report.py       # PDF engine (WeasyPrint)
├── report_template.html     # Jinja2 template
└── generate_report.py       # Report builder with a fictional sample
```

---

## RF-1 Zoning Rules (Most Common)

| Standard | MOR | BZA SE |
|----------|-----|--------|
| Height | 35' / 3 stories (§ 303.1) | 40' (§ 303.3) |
| Lot Occupancy | 60% (§ 304.1) | 70% |
| Units | 2 (§ 302.1) | >2 if pre-1958 (§ 302.2) |
| Rear Yard | 20' min (§ 306.1) | — |
| Parking | 1 per 2 units (Subtitle C § 701.5) | — |

**Pre-1958:** Buildings before May 12, 1958 may exceed 2 units via BZA SE (Subtitle U § 320.2). Not automatic.

---

## Max Buildable Calculation

```
Max Buildable = Lot SF × 60% × 3 stories
```

RF-1 uses lot occupancy, not FAR. Example: 1,500 SF lot → 900 SF footprint → 2,700 SF above grade (theoretical max).

---

## Template Data Fields

See the sample data in `generate_report.py` for the complete field list. Key fields:

**From PropertyQuest:** zone, lot_sf, ssl, owner, owner_address, assessment, neighborhood, ward, anc, smd

**From Redfin:** year_built, year_built_year (integer), living_sf, basement_sf, current_stories, bed_bath

**Calculated:** max_footprint_sf, max_buildable_sf, lot_width (est), lot_depth (est)

**Code-based:** All zoning standards from ZR16 Subtitle E

---

## Output

Professional PDF including:
- Key metrics with hyperlinked code citations
- Zoning analysis with pre-1958 provisions (if applicable)
- Development potential (vertical, horizontal, underpinning)
- Fire protection requirements (IBC R-2/R-3 distinction)
- Regulatory pathway (MOR vs BZA)
- Next steps with agency links and research tools
- Full disclaimers and data verification statement

---

## Dependencies

Pre-installed: Python 3, WeasyPrint, Jinja2
