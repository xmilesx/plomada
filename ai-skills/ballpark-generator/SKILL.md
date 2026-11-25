---
name: ballpark-generator
description: Generates a free Tier 1 ballpark cost range for residential renovation projects in the DC market. Use this skill whenever someone describes a construction project and wants to know what it might cost — even loosely. Triggers on phrases like "what would this cost", "ballpark", "rough number", "how much for", "price range", "is this realistic", "what's a project like this run", "what should I tell them", "they asked about budget", "what's my range here", "can we do this for X", "does the budget make sense", "they have $X to spend", "I got an inquiry", "new lead came in", "someone reached out about", or any time a project type + neighborhood + rough scope is described. Also triggers when a prospect's stated budget needs to be validated against realistic cost. This is the first gate in the Plomada two-tier model — ballpark before site visit, always.
---

# Ballpark Generator — Plomada Tier 1

Free ballpark range only. No site visit required. No drawings required.
Purpose: qualify budget alignment before investing estimating time.

---

## TRIGGER PHRASES (broad — if in doubt, run this skill)

Any of these should fire this skill:
- "what would this cost" / "how much" / "rough number" / "ballpark"
- "is their budget realistic" / "does $X make sense" / "can we do this for X"
- "I got an inquiry" / "new lead" / "someone reached out" / "prospect wants"
- "what should I tell them" / "what's my range" / "what do I say about price"
- "they're thinking X" / "their budget is X" / "they said they have X"
- "is this worth a site visit" / "should I meet with them"
- Project type + neighborhood + any scope description = run this skill

---

## INPUTS — Collect What You Can, Estimate the Rest

```
PROJECT TYPE: [gut reno / kitchen+bath / basement underpinning / historic restoration / addition / design-build / other]
GROSS SF AFFECTED: [SF or "unknown"]
SCOPE CATEGORIES: [structural / MEP full replacement / MEP partial / finishes only / exterior / combination]
NEIGHBORHOOD / ZIP: [Columbia Heights / Capitol Hill / Petworth / Hill East / Georgetown / etc.]
SPECIAL CONDITIONS: [historic district / construction loan / occupied during construction / pre-1940 building / other]
PROSPECT'S STATED BUDGET: [$X or "not stated"]
```

If the user hasn't provided all inputs, extract what you can from their description and make reasonable assumptions. State your assumptions clearly in the output. Do not ask 6 questions before generating — make your best estimate and flag what you assumed.

---

## COST DATABASE — DC Market 2025

### Base Ranges by Project Type (total project cost)

| Project Type | Low | Mid | High | Notes |
|---|---|---|---|---|
| Kitchen + Bath only | $85K | $120K | $175K | Defined scope, predictable MEP |
| Full floor gut (1 floor) | $120K | $165K | $220K | MEP + finishes |
| Gut renovation 2-story SF | $280K | $380K | $500K | Full MEP replacement |
| Gut renovation 3-story rowhouse | $380K | $480K | $650K | Full MEP, 3 floors |
| Gut renovation 4-story rowhouse | $480K | $600K | $800K | Full MEP, permit complexity |
| Basement finish only | $65K | $90K | $130K | No underpinning |
| Basement underpinning + finish | $180K | $250K | $350K | Structural, staged inspections |
| Addition (rear/up) | $220K | $320K | $450K | Zoning, structural integration |
| Historic restoration | $420K | $550K | $750K | HPRB compliance, material sourcing |
| Design-build full (2-story) | $350K | $480K | $650K | Includes preconstruction coordination |

### Trade Benchmarks (embedded — use for component-level cross-checks)

**Plumbing (labor + materials):**
- Permit/admin: $1,000
- Ground package: $4,500
- Per kitchen: $2,000
- Per bathroom: $1,500
- Per laundry: $750

**Electrical (Elements of Energy actuals):**
- Full 3-story SF rough + trim + panel + permit: $7,900
- 200A panel upgrade: $2,000/panel
- Per bathroom: $600–$800
- Per kitchen: $1,200–$1,500

**HVAC (Vasquez Brothers actuals):**
- Single system 1.5–2 ton, full ductwork: $12,500
- Two-system full install, 3-story rowhouse: $25,880–$28,500
- Per floor zone: $13,380–$15,000

---

## ADJUSTMENT FACTORS

Apply these modifiers to the base range:

| Condition | Adjustment |
|---|---|
| Historic district (HPRB review required) | +15–25% |
| Pre-1940 building (concealed conditions risk) | +10–20% |
| Occupied during construction | +15% |
| Construction loan (draw timing complexity) | No cost impact — note in output |
| Georgetown / high-cost neighborhood | +10% |
| Petworth / outer neighborhoods | Base |
| Capitol Hill / Hill East | Base to +5% |
| Columbia Heights | Base |
| Scope still undefined / early stage | Widen range by 20% each direction |
| Client has no drawings | Note in caveat — add contingency flag |

---

## BUDGET ALIGNMENT ASSESSMENT

After generating range, assess prospect's stated budget:

| Situation | Assessment | Action |
|---|---|---|
| Budget within range | ✅ ALIGNED | Proceed to site visit + preconstruction proposal |
| Budget 10–20% below low end | ⚠️ BORDERLINE | Proceed with caveat — scope may need adjustment |
| Budget >20% below low end | ❌ MISALIGNED | Do not schedule site visit — issue polite redirect |
| Budget not stated | ❓ UNKNOWN | Ask before scheduling site visit |

---

## OUTPUT FORMAT

```
═══════════════════════════════════════════════════════════
PLOMADA BALLPARK — [Project Type] | [Neighborhood]
═══════════════════════════════════════════════════════════

PROJECT SUMMARY
──────────────────────────────────────────────────────────
Type:              [project type]
Location:          [neighborhood]
Scope:             [brief scope description]
SF Affected:       [SF or estimated]
Special Flags:     [historic / pre-1940 / occupied / none]

COST RANGE
──────────────────────────────────────────────────────────
Low:               $[X]
Mid:               $[X]
High:              $[X]

Range drivers:     [2–3 sentences on what pushes toward high vs low end]

BUDGET ALIGNMENT
──────────────────────────────────────────────────────────
Prospect's budget: $[X] / [not stated]
Assessment:        [✅ ALIGNED / ⚠️ BORDERLINE / ❌ MISALIGNED / ❓ UNKNOWN]

[If ALIGNED or BORDERLINE:]
→ Recommended next step: Schedule site visit. Propose paid preconstruction ($2,500–$5,000 depending on complexity, credited to contract).

[If MISALIGNED:]
→ Do not schedule site visit. Use redirect language below.

[If UNKNOWN:]
→ Ask budget before committing to site visit. Use qualification script below.

STANDARD CAVEATS (include in any client-facing communication)
──────────────────────────────────────────────────────────
This range is based on comparable projects in the DC market and is not a quote. 
Actual costs depend on existing conditions, final scope, permit requirements, and 
market pricing at time of construction. A detailed budget requires a site assessment 
and formal preconstruction engagement.

ASSUMPTIONS MADE
──────────────────────────────────────────────────────────
• [List any inputs you estimated rather than received]
• [Note if range is wider due to unknown conditions]

═══════════════════════════════════════════════════════════
```

---

## CLIENT-FACING LANGUAGE TEMPLATES

### Budget Alignment Script (use when budget is unknown before site visit)
> Before we schedule a site visit, I want to make sure we're aligned on investment range. For a [project type] in [neighborhood], projects of this scope typically run between [LOW] and [HIGH]. That range reflects [key driver — e.g., full MEP replacement, permit complexity, structural work]. If that range is workable, the next step is a paid preconstruction engagement where we assess existing conditions, document scope, and produce a reliable budget. The fee is [$X], credited toward construction if we proceed. If the range is higher than expected, I'd rather know now than after we've both invested time.

### Misaligned Budget Redirect
> Based on what you've described, projects of this scope in DC typically run between [LOW] and [HIGH]. That's meaningfully higher than the [budget] you mentioned. Rather than waste your time on a site visit that leads to a budget that doesn't work, I'd suggest either revisiting the scope to focus on highest-priority items, or revisiting the timeline to allow for a larger investment. I'm happy to talk through what a scaled-back version might look like. No cost for a quick call.

### Preconstruction Proposal Close
> Given that the budget looks aligned, the right next step is a preconstruction agreement. For a project of this scope, the preconstruction fee is [$X]. That covers a formal site assessment, trade partner input, a detailed budget by division, a permit feasibility review, and a preliminary schedule. The fee is fully credited toward construction if we proceed. I can send the agreement this week if you'd like to move forward.

---

## NOTES FOR DC MARKET SPECIFICALLY

- DCRA permit fees on a $500K project: $3,000–$8,000 (include in range)
- Historic district review adds 4–8 weeks to permit timeline — flag for client
- Basement underpinning always requires structural engineer + staged inspections — add $8,000–$15,000 for structural engineering
- Pre-1940 buildings: budget for potential asbestos/lead abatement ($5,000–$25,000 if triggered)
- Construction loan clients: note that draw timing affects GC cash flow — larger deposit required upfront
