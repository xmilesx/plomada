---
name: material-takeoff
description: Quick material takeoff from uploaded construction plans. Triggers when user uploads architectural/structural drawings and requests takeoff, estimate, quantities, or scope breakdown. Outputs structured scope packages for subs (MEP bid packages), framing estimates (wood/metal stud counts, plates, headers), drywall sheet counts by type/thickness, and rough pricing. Works with split PDF sheets or compressed plans. NOT for detailed Bluebeam-level takeoffs — this is rapid scope identification and ballpark quantities.
---

# Material Takeoff Skill

## Trigger

**User uploads:** Plan sheets (PDF) — floor plans, elevations, sections, structural
**User says:** "Takeoff" / "Material quantities" / "Scope breakdown" / "What do I need for subs"

## Workflow

### 1. Initial Assessment

Review uploaded sheets and identify:
- Project type (residential, commercial, reno, new construction)
- Scale (verify if noted, ask if unclear)
- Scope present (structural, architectural, MEP, finishes)
- Drawing quality (full set vs partial, dimensioned vs sketch)

State what sheets are present and what's missing for a complete takeoff.

### 2. Sheet-by-Sheet Extraction

For each sheet type, extract:

**Floor Plans:**
- Room count, dimensions, SF per room
- Wall LF by type (exterior, interior, demising, rated)
- Door/window schedule or counts
- Ceiling heights (if noted)

**Structural:**
- Framing system (wood vs metal vs hybrid)
- Beam sizes, spans, counts
- Point loads, headers, posts
- Foundation type (if shown)

**Sections/Details:**
- Wall assemblies
- Floor/ceiling assemblies
- Special conditions (wet walls, rated assemblies, soundproofing)

**Elevations:**
- Exterior finish types
- Window/door rough openings
- Height dimensions

### 3. Generate Takeoff Output

Output a structured takeoff with these sections:

---

## TAKEOFF OUTPUT FORMAT

### PROJECT SUMMARY
- Address/Project Name:
- Approx SF:
- Stories:
- Construction Type:
- Sheets Reviewed:

### FRAMING SCOPE

**System:** [Wood / Metal Stud / Hybrid]

| Item | Qty | Size | Notes |
|------|-----|------|-------|
| Studs | X | 2x4/2x6/3-5/8" | @16" OC |
| Plates (top/bottom) | X LF | Match stud | Double top |
| Headers | X | Size | Over openings |
| Beams | X | Size x Length | Locations |
| Posts | X | Size | Load-bearing |
| Joists | X | Size @spacing | Floor/ceiling |

**Assumptions:** [State any assumptions made]

### DRYWALL SCOPE

| Area | Sheets | Type | Thickness | Notes |
|------|--------|------|-----------|-------|
| Walls - standard | X | Regular | 1/2" | |
| Walls - rated | X | Type X | 5/8" | 1-hr assembly |
| Walls - wet | X | Moisture resistant | 1/2" | Bath/kitchen |
| Ceilings | X | Regular/Type X | 1/2" or 5/8" | |

**Sheet calc:** Wall SF ÷ 32 × 1.10 waste factor
**Total sheets:** X

### MEP SCOPE PACKAGE (for sub bidding)

**Plumbing:**
- Fixture count: X toilets, X lavs, X tubs/showers, X kitchen sinks
- Rough-in locations: [by room]
- Water heater: [if shown]
- Special: [floor drains, cleanouts, gas, etc.]

**Electrical:**
- Panel size: [if shown]
- Device count estimate: X outlets, X switches, X fixtures
- Special circuits: [HVAC, range, dryer, etc.]
- Low voltage: [data, security, AV]

**HVAC:**
- System type: [if shown — split, package, mini-split]
- Zones: X
- Ductwork: [rough LF or "see plans"]

### ROUGH PRICING REFERENCE

| Scope | Unit | Rate Range | Estimated |
|-------|------|------------|-----------|
| Framing - wood | SF | $8-15/SF | $ |
| Framing - metal | SF | $10-18/SF | $ |
| Drywall (hang/finish) | SF | $3-5/SF | $ |
| Plumbing rough | fixture | $800-1,500 | $ |
| Electrical rough | SF | $8-15/SF | $ |
| HVAC | ton | $2,500-4,000 | $ |

*Pricing is DC metro ballpark — adjust for project complexity, access, timeline*

### MISSING / VERIFY

- [ ] Items not shown on plans
- [ ] Assumptions that need confirmation
- [ ] Sheets needed for complete takeoff

---

## Pricing References

Use these as sanity-check ranges (DC metro, 2024-2025):

**Framing:**
- Wood framing (labor + material): $8-15/SF depending on complexity
- Metal stud (labor + material): $10-18/SF
- Headers/beams: $15-25/LF installed
- Underpinning/structural: Premium — price separately

**Drywall:**
- Hang + finish Level 4: $3.00-4.50/SF
- Type X / rated assemblies: Add $0.50-1.00/SF
- High ceilings (>9'): Add 15-25%

**MEP (rough-in only):**
- Plumbing: $800-1,500 per fixture (residential)
- Electrical: $8-15/SF (residential), $12-20/SF (commercial)
- HVAC: $2,500-4,000/ton installed

**Waste Factors:**
- Lumber: 10-15%
- Drywall: 10%
- Complex layouts: 15-20%

## Notes

- This is rapid scope identification, not detailed estimating
- Always verify dimensions from scaled drawings
- For complex structural, get engineer to verify loads
- MEP counts are for sub bidding — they'll do their own detailed takeoff
- Pricing is starting point — adjust for current market, project specifics
