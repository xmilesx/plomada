---
name: job-costing
description: Job costing calculator using Simple Numbers (Greg Crabtree) and Profit First methodology. Takes quantity inputs from takeoff and outputs fully costed estimate with labor hours, burdened rates, overhead allocation, target margins, LER validation, and Profit First breakdown. Triggers on "cost this", "price this job", "estimate from quantities", or when user provides scope quantities and wants pricing. Designed for construction/renovation contractors.
---

# Job Costing Skill (Simple Numbers + Profit First)

## Trigger

**User provides:** Quantities from takeoff (SF, fixtures, etc.)
**User says:** "Cost this" / "Price this job" / "Run the numbers" / "What should I charge"

## Input Format

Collect these from user (use defaults where not provided):

```
SCOPE QUANTITIES:
- Framing SF: ___
- Drywall SF: ___
- Plumbing fixtures: ___
- Electrical SF: ___
- HVAC tons: ___
- Sub bids (if known): $___

OVERRIDES (optional):
- Burdened labor rate: $___ (default: $52/hr)
- Target gross margin: ___% (default: 50%)
- Overhead method: fixed $X or X% (default: 12% of direct)
```

---

## DEFAULT PARAMETERS

### Burdened Labor Rate
**Default: $52/hr**

Components (adjust to actuals):
- Base wage: $28/hr
- Payroll taxes (7.65% FICA): $2.14
- Workers comp (8%): $2.24
- Benefits/PTO allowance: $4.00
- Small tools/consumables: $2.00
- Supervision burden: $6.00
- Vehicle/mobilization: $7.62

### Production Rates (SF/labor-hour)

| Task | Default | Range | Notes |
|------|---------|-------|-------|
| Framing - wood (new) | 8 SF/hr | 6-12 | Open layout faster |
| Framing - wood (reno) | 5 SF/hr | 4-7 | Demo, fit, complexity |
| Framing - metal stud | 10 SF/hr | 8-14 | Faster than wood |
| Drywall hang | 25 SF/hr | 20-35 | Height, lifts affect |
| Drywall finish (L4) | 40 SF/hr | 30-50 | Texture adds time |
| Insulation | 50 SF/hr | 40-70 | Batts vs spray |

### Material Costs (per unit)

| Material | Default | Unit | Notes |
|----------|---------|------|-------|
| Lumber (2x4) | $0.45 | LF | Fluctuates — verify |
| Lumber (2x6) | $0.75 | LF | |
| Drywall 1/2" | $14 | sheet | 4x8 |
| Drywall 5/8" Type X | $18 | sheet | |
| Insulation R-13 | $0.50 | SF | Batts |
| Insulation R-19 | $0.75 | SF | |

### Material Factor (SF → material units)
- Framing: ~1.5 BF per SF (walls) — varies by layout
- Drywall: SF ÷ 32 × 1.10 = sheets (with waste)

### Sub Costs (if not provided as bids)

| Trade | Default | Unit | Notes |
|-------|---------|------|-------|
| Plumbing | $1,200 | per fixture | Rough-in, residential |
| Electrical | $12 | SF | Residential, moderate |
| HVAC | $3,200 | per ton | Split system installed |

### Overhead Allocation
**Default: 12% of direct costs**

Alternative methods:
- Fixed $/job (e.g., $8,000 for typical reno)
- % of labor only
- Calculated from annual overhead ÷ projected jobs

### Target Gross Margin
**Default: 50%**

Sell Price = Total Cost ÷ (1 - Gross Margin %)
At 50%: Sell Price = Total Cost ÷ 0.50 = Total Cost × 2

### Profit First Allocations (of revenue)
**Defaults:**
- Profit: 10%
- Owner Pay: 15%
- Tax: 15%
- Operating Expenses: 60%

Adjust based on business maturity and Profit First targets.

---

## CALCULATION WORKFLOW

### Step 1: Direct Labor Cost

```
Labor Hours = Scope SF ÷ Production Rate
Labor Cost = Labor Hours × Burdened Rate
```

### Step 2: Direct Material Cost

```
Material Units = Scope SF × Material Factor
Material Cost = Material Units × Unit Cost
```

### Step 3: Sub Costs

Use actuals if provided, otherwise:
```
Sub Cost = Quantity × Default Rate
```

### Step 4: Total Direct Costs

```
Direct Costs = Labor + Materials + Subs
```

### Step 5: Overhead Allocation

```
Overhead = Direct Costs × Overhead % (or fixed amount)
```

### Step 6: Total Job Cost

```
Total Cost = Direct Costs + Overhead
```

### Step 7: Sell Price (at target margin)

```
Sell Price = Total Cost ÷ (1 - Target Margin)
```

At 50% margin: Sell Price = Total Cost × 2

### Step 8: LER Validation (Simple Numbers)

```
Gross Profit = Sell Price - Direct Costs
LER = Gross Profit ÷ Direct Labor Cost
```

**Target: LER ≥ 2.0**

- LER < 1.5: Job is underpriced or labor-inefficient
- LER 1.5-2.0: Marginal — review scope or pricing
- LER 2.0-3.0: Healthy
- LER > 3.0: Strong margin or sub-heavy job

### Step 9: Profit First Breakdown

```
Profit = Sell Price × 10%
Owner Pay = Sell Price × 15%
Tax = Sell Price × 15%
OpEx = Sell Price × 60%
```

---

## OUTPUT FORMAT

```
═══════════════════════════════════════════════════════════
JOB COST ESTIMATE — [Project Name]
═══════════════════════════════════════════════════════════

INPUTS
──────────────────────────────────────────────────────────
Framing:           _____ SF
Drywall:           _____ SF
Plumbing:          _____ fixtures
Electrical:        _____ SF
HVAC:              _____ tons
Burdened Rate:     $____/hr
Target Margin:     ____%

DIRECT COSTS
──────────────────────────────────────────────────────────
                    Qty      Hours    Labor      Material    Total
Framing             ___ SF   ___ hrs  $_____     $_____      $_____
Drywall             ___ SF   ___ hrs  $_____     $_____      $_____
──────────────────────────────────────────────────────────
Self-Perform Total           ___ hrs  $_____     $_____      $_____

SUBCONTRACTORS
──────────────────────────────────────────────────────────
Plumbing            ___ fix                                  $_____
Electrical          ___ SF                                   $_____
HVAC                ___ ton                                  $_____
──────────────────────────────────────────────────────────
Sub Total                                                    $_____

SUMMARY
──────────────────────────────────────────────────────────
Direct Labor:                          $_____
Direct Materials:                      $_____
Subcontractors:                        $_____
──────────────────────────────────────────────────────────
TOTAL DIRECT COSTS:                    $_____

Overhead (___% of direct):             $_____
──────────────────────────────────────────────────────────
TOTAL JOB COST:                        $_____

PRICING
──────────────────────────────────────────────────────────
Target Gross Margin:                   ____%
SELL PRICE:                            $_____
Gross Profit:                          $_____

LER VALIDATION (Simple Numbers)
──────────────────────────────────────────────────────────
Gross Profit:                          $_____
÷ Direct Labor Cost:                   $_____
= LABOR EFFICIENCY RATIO:              _____

Status: [✓ HEALTHY / ⚠ MARGINAL / ✗ REVIEW PRICING]

PROFIT FIRST ALLOCATION (at sell price)
──────────────────────────────────────────────────────────
Profit (10%):                          $_____
Owner Pay (15%):                       $_____
Tax Reserve (15%):                     $_____
Operating Expenses (60%):              $_____
──────────────────────────────────────────────────────────
Total:                                 $_____

ASSUMPTIONS & NOTES
──────────────────────────────────────────────────────────
• Production rates: [list rates used]
• Material pricing: [date/source]
• Sub costs: [bid or estimated]
• [Any scope-specific notes]

═══════════════════════════════════════════════════════════
```

---

## QUICK REFERENCE

**The Formula:**
```
Sell Price = (Labor + Materials + Subs + Overhead) ÷ (1 - Margin)
LER = (Sell Price - Direct Costs) ÷ Direct Labor
```

**Sanity Checks:**
- LER should be 2.0+ for healthy jobs
- Direct labor typically 25-35% of sell price
- Subs typically priced at cost + 10-15% markup (adjust margin calc if marking up subs)
- If LER < 2.0, either raise price or reduce labor hours

**Common Adjustments:**
- Complex/phased work: reduce production rates 20%
- Occupied reno: reduce production rates 25-30%
- High ceilings (>10'): add 15% to drywall labor
- Historic/sensitive: add 20% contingency
