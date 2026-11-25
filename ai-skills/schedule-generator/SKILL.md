---
name: schedule-generator
description: >
  Generates a preliminary construction schedule for residential renovation projects in the DC market. Use this skill whenever a project timeline is needed — even roughly. Triggers on phrases like "how long will this take", "build me a schedule", "when can we finish", "what's the timeline", "project schedule", "how long does a gut reno take", "when should we start", "can we finish by X", "I need a schedule for the preconstruction package", "what's the permit timeline", "how do I phase this", "can we be done before the holidays", "what order do things happen", "sequence of work", "construction phases", "rough schedule", "is X months realistic", or any time a project type plus a target start or end date is mentioned. Also triggers automatically when running a preconstruction workflow — a preliminary schedule is a standard preconstruction deliverable. DC-specific permit and inspection milestones are built in.
---

# Schedule Generator — Plomada

Preliminary construction schedule with DC permit timelines, trade sequencing, and inspection milestones.
Output is a preconstruction-grade deliverable — good enough for client communication and lender packages.

---

## TRIGGER PHRASES (broad — if timeline is being discussed, run this)

- "how long will this take" / "what's the timeline" / "build a schedule"
- "when can we start" / "when can we finish" / "can we be done by X"
- "what's the permit timeline" / "how long does permitting take in DC"
- "I need a schedule for the preconstruction package"
- "how do I phase this" / "what order does work happen"
- "is X months realistic" / "rough schedule" / "sequence of work"
- Project type + start date or end date mentioned = run this skill
- Preconstruction deliverable being assembled = always include schedule

---

## INPUTS — Collect What You Can, Estimate the Rest

```
PROJECT TYPE: [gut reno / kitchen+bath / basement underpinning / historic restoration / addition / design-build]
SCOPE: [brief description — floors affected, trades, structural work]
GROSS SF: [SF or "unknown"]
START DATE TARGET: [specific date / month / "ASAP" / "after permit"]
END DATE TARGET: [specific date / "flexible" / event-driven deadline]
PERMIT STATUS: [not started / pre-application submitted / permit in hand]
HISTORIC DISTRICT: [yes / no / unknown]
OCCUPIED DURING CONSTRUCTION: [yes / no]
CONSTRUCTION LOAN: [yes / no / unknown]
```

If inputs are incomplete, make reasonable assumptions and state them clearly. Do not ask 6 questions — generate the schedule and flag what you assumed.

---

## DC PERMIT TIMELINE DATABASE

This is the single biggest variable in DC residential schedules. Always call this out explicitly.

| Permit Type | Typical Timeline | Notes |
|---|---|---|
| Standard residential permit (DCRA) | 8–12 weeks | From complete application submission |
| Complex structural / underpinning | 10–16 weeks | Structural review adds time |
| Historic district (HPRB review required) | 14–22 weeks | HPRB meets monthly — one missed cycle = 4–6 weeks added |
| Addition / zoning review | 12–18 weeks | BZA hearing if variance needed adds 8–12 weeks |
| Expedited review (fee-based) | 4–6 weeks | Available for some permit types — confirm with DCRA |
| Over-the-counter (simple scope) | 1–2 weeks | Rare for BBCDC project types |

**DCRA Inspection Milestones (add to every schedule):**
- Rough framing inspection
- Rough electrical inspection
- Rough plumbing inspection
- Rough HVAC / mechanical inspection
- Insulation inspection
- Fire blocking / fire caulk inspection (if applicable)
- Final electrical
- Final plumbing
- Final mechanical
- Final building inspection / Certificate of Occupancy

**Inspection scheduling lag (DC):** 3–7 business days from request to inspection. Failed inspection = restart the clock. Budget 1–2 weeks per inspection phase for scheduling + potential re-inspection.

---

## PHASE DURATIONS BY PROJECT TYPE

### Gut Renovation — 2-Story Rowhouse (2,000–2,800 SF)

| Phase | Duration | Notes |
|---|---|---|
| Preconstruction (paid) | 3–5 weeks | Scope, budget, permit docs |
| Permit period | 8–14 weeks | Runs concurrently with preconstruction completion |
| Demolition | 1–2 weeks | Full gut — MEP, finishes, non-structural |
| Structural work | 1–3 weeks | If beam work, lintels, wall removal |
| Rough framing | 1–2 weeks | New partitions, blocking, backing |
| Rough MEP (electrical + plumbing + HVAC) | 3–5 weeks | All trades concurrent |
| MEP inspections | 1–2 weeks | Scheduling lag + potential re-inspection |
| Insulation + air sealing | 1 week | |
| Insulation inspection | 1 week | |
| Drywall hang + finish | 2–3 weeks | |
| Paint prime + first coat | 1 week | |
| Tile + flooring rough | 2–3 weeks | Concurrent where possible |
| Cabinets + millwork | 1–2 weeks | |
| Finish MEP trim | 1–2 weeks | Fixtures, devices, trim out |
| Paint finish | 1 week | |
| Finish flooring | 1 week | |
| Punch list + inspections | 2–3 weeks | Final inspections, CO |
| **TOTAL** | **~7–9 months** | From permit submission to CO |

### Gut Renovation — 3-Story Rowhouse (2,800–4,000 SF)

| Phase | Duration | Notes |
|---|---|---|
| Preconstruction | 4–6 weeks | |
| Permit period | 10–16 weeks | |
| Demolition | 2 weeks | |
| Structural | 2–4 weeks | |
| Rough framing | 2 weeks | |
| Rough MEP | 4–6 weeks | |
| MEP inspections | 1–2 weeks | |
| Insulation + inspection | 2 weeks | |
| Drywall | 3–4 weeks | |
| Tile + flooring rough | 2–3 weeks | |
| Cabinets + millwork | 2 weeks | |
| Finish MEP trim | 2 weeks | |
| Paint | 2 weeks | |
| Finish flooring + punch | 2–3 weeks | |
| Final inspections + CO | 2–3 weeks | |
| **TOTAL** | **~9–12 months** | |

### Kitchen + Bath Only

| Phase | Duration | Notes |
|---|---|---|
| Preconstruction | 2–3 weeks | |
| Permit period | 4–8 weeks | Simpler scope |
| Demo + rough work | 1–2 weeks | |
| Rough MEP | 2–3 weeks | |
| Inspections | 1 week | |
| Tile + drywall | 2 weeks | |
| Cabinets + finish | 2 weeks | |
| Punch + final | 1 week | |
| **TOTAL** | **~4–5 months** | |

### Basement Underpinning + Finish

| Phase | Duration | Notes |
|---|---|---|
| Preconstruction + structural engineering | 6–8 weeks | SE drawings required for permit |
| Permit period | 12–18 weeks | Structural review, staged approval |
| Excavation + underpinning (staged) | 4–8 weeks | Typically 3–5 staged pours, inspected each |
| Slab + waterproofing | 2 weeks | |
| Rough framing | 1–2 weeks | |
| Rough MEP | 3–4 weeks | |
| Inspections | 2 weeks | Multiple staged inspections |
| Insulation + drywall | 2 weeks | |
| Finish work | 2–3 weeks | |
| Final inspections | 1–2 weeks | |
| **TOTAL** | **~9–12 months** | |

### Historic Restoration

| Phase | Duration | Notes |
|---|---|---|
| Preconstruction + HPRB prep | 6–10 weeks | Design compliance docs, material specs |
| HPRB review + permit | 16–24 weeks | HPRB monthly meeting cadence |
| Construction (scope-dependent) | Per gut reno above + 20% | Slower — material sourcing, compliance |
| **TOTAL** | **~12–18 months** | |

---

## CRITICAL PATH ITEMS — ALWAYS FLAG THESE

These are the items that blow up schedules when not managed. Highlight in every output:

1. **Permit timeline** — longest lead item on every DC project. Start permit prep before preconstruction is complete.
2. **Structural engineer** — required for underpinning, beam work, wall removal. SE has 4–6 week lead time. Order early.
3. **HVAC equipment lead time** — Daikin/Carrier equipment can run 4–8 weeks in supply-constrained periods. Order at rough framing stage.
4. **Custom cabinets / millwork** — 8–14 week lead time typical. Order at permit submission, not at cabinet install phase.
5. **Tile and flooring materials** — if client-selected, decision deadline must be set at preconstruction. Delays here push finish trades by weeks.
6. **HPRB meeting cycle** — if historic, HPRB meets monthly. Missing one meeting = 4–6 week slip automatically.
7. **Construction loan draw schedule** — lender inspection triggers draw. Coordinate milestone completion with draw timing to avoid cash flow gap.

---

## OCCUPIED DURING CONSTRUCTION ADJUSTMENTS

If client will live in the property during construction:
- Add 20–30% to all phase durations
- Sequence work to maintain habitable zone at all times
- Add 2 weeks for zone transitions and protection work
- Note: BBCDC charges premium for occupied renovations — flag this in budget

---

## OUTPUT FORMAT

```
═══════════════════════════════════════════════════════════
PLOMADA PRELIMINARY SCHEDULE — [Project Type] | [Address/Neighborhood]
Generated: [date] | Status: Preconstruction Estimate
═══════════════════════════════════════════════════════════

PROJECT PARAMETERS
──────────────────────────────────────────────────────────
Type:              [project type]
Scope:             [brief description]
SF:                [SF or estimated]
Historic district: [yes / no]
Occupied:          [yes / no]
Permit status:     [not started / in progress / in hand]
Target start:      [date]
Target completion: [date]

PERMIT TIMELINE (DC — CRITICAL PATH)
──────────────────────────────────────────────────────────
Permit prep start:     [date]
Estimated submission:  [date]
Estimated approval:    [date]
Permit type:           [standard / structural / historic / expedited]
Notes:                 [any flags — HPRB cycle, zoning review, etc.]

PHASE SCHEDULE
──────────────────────────────────────────────────────────
Phase                          Start        End          Duration
─────────────────────────────────────────────────────────
Preconstruction                [date]       [date]       [X weeks]
Permit period (concurrent)     [date]       [date]       [X weeks]
Mobilization + demo            [date]       [date]       [X weeks]
Structural work                [date]       [date]       [X weeks]
Rough framing                  [date]       [date]       [X weeks]
Rough MEP (elec/plmb/HVAC)    [date]       [date]       [X weeks]
MEP inspections                [date]       [date]       [X weeks]
Insulation + inspection        [date]       [date]       [X weeks]
Drywall + plaster              [date]       [date]       [X weeks]
Tile + flooring rough          [date]       [date]       [X weeks]
Cabinets + millwork            [date]       [date]       [X weeks]
Finish MEP trim                [date]       [date]       [X weeks]
Paint finish                   [date]       [date]       [X weeks]
Finish flooring                [date]       [date]       [X weeks]
Punch list + final inspections [date]       [date]       [X weeks]
Certificate of Occupancy       [date]       —            —
─────────────────────────────────────────────────────────
TOTAL DURATION:                [X months]
ESTIMATED COMPLETION:          [date]

CRITICAL PATH FLAGS
──────────────────────────────────────────────────────────
⚠ [List critical path items relevant to this project]
⚠ Long-lead items: [cabinets / HVAC equipment / structural engineer / HPRB]

OWNER DECISION DEADLINES
──────────────────────────────────────────────────────────
[Item]                         Decision needed by: [date]
[Item]                         Decision needed by: [date]
(Decisions missed past these dates will push completion)

ASSUMPTIONS
──────────────────────────────────────────────────────────
• [List what was estimated vs. provided]
• [Permit timeline assumed standard unless historic flagged]
• [No allowance for stop-work orders or re-inspections unless noted]

STANDARD CAVEAT
──────────────────────────────────────────────────────────
This is a preliminary schedule for planning purposes. Actual timeline
depends on permit approval timing, inspection scheduling, subcontractor
availability, material lead times, and scope changes. A detailed schedule
with confirmed dates will be issued at construction contract execution.

═══════════════════════════════════════════════════════════
```

---

## CLIENT-FACING LANGUAGE

### Explaining Timeline to Client
> For a project of this scope in DC, the timeline from permit submission to move-in is typically [X] to [Y] months. The biggest variable is permitting — DCRA currently runs [X] weeks for [permit type], and we can't control that clock. What we can control is starting permit prep immediately so we're not adding delays on our end. If you have a hard deadline like [event], we need to [action] by [date] to have a reasonable shot at hitting it.

### Setting Decision Deadline Expectations
> One thing that derails schedules more than anything else is delayed client decisions — especially on tile, cabinets, and fixtures. These items have long lead times and every week of indecision at the wrong moment pushes your completion date by the same amount. We'll build a decision log into the preconstruction package with hard deadlines for each item. Missing those dates moves the schedule — no exceptions.

### Hard Deadline Projects
> If you have a hard deadline — lease ending, baby due, holidays, whatever — tell me now. Hard deadlines require working backward from the completion date to set a permit submission date, and if that date has already passed or is impossible, we need to have that conversation before you spend money on preconstruction.
