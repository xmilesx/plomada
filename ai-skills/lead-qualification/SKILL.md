---
name: lead-qualification
description: >
  Qualifies incoming leads for BBCDC Construction using the Plomada two-tier model. Scores budget alignment, flags red flags, and outputs a clear next-step recommendation. Use this skill whenever a new inquiry, lead, or prospect is described — even loosely. Triggers on phrases like "I got a call", "someone reached out", "new inquiry", "prospect wants", "potential client", "they contacted me", "should I meet with them", "is this worth pursuing", "what do I do with this lead", "they found us on Google", "architect referred someone", "past client sent someone", "is this a good lead", "how do I respond", "should I send a quote", "they want a proposal", "what's the next step", "I have a meeting with", "site visit request", or any time a potential project and client situation is described. Also triggers when the user is drafting a response to a new inquiry or deciding whether to invest time in a prospect. Outputs a qualification score, red flag list, and exact recommended next step.
---

# Lead Qualification Gate — Plomada

Protect estimating time. Qualify before you invest.
The goal: determine in 2 minutes whether this lead deserves a site visit.

---

## TRIGGER PHRASES (broad — if someone new is being described, run this)

- "I got a call / email / inquiry / message"
- "new lead" / "someone reached out" / "potential client" / "they found us"
- "architect referred" / "past client sent" / "referral from"
- "should I meet with them" / "is this worth my time" / "good lead?"
- "they want a quote" / "they want a proposal" / "can you come look at it"
- "I have a site visit scheduled" / "meeting with a prospect"
- "how do I respond" / "what do I say" / "draft a response"
- Any description of a new person + project = run this skill

---

## QUALIFICATION INPUTS

Extract what you can from the user's description. Ask only for what's truly missing.

```
LEAD SOURCE: [Google organic / GBP / Google Ads / referral (who?) / past client / architect / Houzz / direct / unknown]
PROJECT TYPE: [gut reno / kitchen+bath / addition / underpinning / historic / design-build / other]
NEIGHBORHOOD: [specific or general DC area]
STATED BUDGET: [$X / "they didn't say" / "they said they need a quote first"]
TIMELINE: [start date or "ASAP" or vague]
PROPERTY STATUS: [vacant / occupied during construction / rental / primary residence]
ARCHITECT INVOLVED: [yes — who / no / not yet]
DECISION MAKER: [present / unclear / mentioned a spouse/partner/investor not yet involved]
FUNDING: [cash / construction loan / HELOC / unknown]
HOW THEY FOUND YOU: [specific if known]
```

---

## SCORING CRITERIA

Score each factor. Total = qualification recommendation.

### Green Flags (+1 each)
- [ ] Budget stated and within realistic range for project type
- [ ] Referred by architect or trusted past client
- [ ] Timeline is realistic (60+ days out)
- [ ] Decision maker will be present at site visit
- [ ] Funding plan confirmed (construction loan approved, cash available)
- [ ] Project type matches BBCDC specialization (gut reno, historic, underpinning, design-build)
- [ ] Neighborhood is BBCDC's active market (DC proper)
- [ ] Has or is getting drawings/plans

### Red Flags (−1 each, some are disqualifying)
- [ ] Budget not stated and prospect resists sharing range
- [ ] Budget stated and significantly below realistic range (>20% below low)
- [ ] "I'm getting multiple bids" / "comparing a few contractors" (low commitment signal)
- [ ] Wants detailed estimate before any commitment (estimating for free)
- [ ] No decision maker available for site visit
- [ ] Timeline is "ASAP" with no flexibility (construction loan not in place, rushed decision)
- [ ] Project type outside BBCDC core (simple handyman, new construction, commercial)
- [ ] Found via low-quality source (random Google Ads click with no specific project)
- [ ] Unclear funding (no loan approval, no clear cash source)
- [ ] Previous contractor fired / project already started and gone wrong (high conflict risk)

### Hard Disqualifiers (automatic decline regardless of score)
- Budget stated and more than 30% below realistic range
- Wants free detailed estimate as condition of engaging
- No decision maker will ever be available (investor-only, absentee, committee)
- Project type BBCDC doesn't do (e.g., new ground-up commercial)

---

## QUALIFICATION SCORE → RECOMMENDATION

| Score | Recommendation |
|---|---|
| 5+ green, 0–1 red | ✅ PRIORITY LEAD — Schedule site visit immediately. Propose preconstruction at meeting. |
| 3–4 green, 0–2 red | ✅ QUALIFIED — Schedule site visit. Send budget alignment script first. |
| 2–3 green, 2–3 red | ⚠️ CONDITIONAL — Get budget and decision maker confirmed before site visit. |
| Any hard disqualifier | ❌ DECLINE — Use redirect language. Do not schedule site visit. |
| Budget unknown + other flags | ❓ GET BUDGET FIRST — Do not schedule until budget range is confirmed. |

---

## LEAD SOURCE NOTES

Apply these weights when evaluating source quality:

| Source | Notes |
|---|---|
| Architect referral | Highest quality. Architect pre-qualifies. Prioritize. |
| Past client referral | High trust, high conversion. Prioritize. |
| Google organic / GBP | Good. High intent. Qualify budget before site visit. |
| Google Ads | Lower average quality in DC market. Stricter budget gate. |
| Houzz | Tends toward lower project value. Watch budget carefully. |
| Nextdoor / neighborhood apps | Occasional. Often smaller scope. Filter quickly. |
| Direct (no clear source) | Neutral. Run full qualification. |

---

## OUTPUT FORMAT

```
═══════════════════════════════════════════════════════════
PLOMADA LEAD QUALIFICATION — [Project Type] | [Neighborhood]
═══════════════════════════════════════════════════════════

LEAD SUMMARY
──────────────────────────────────────────────────────────
Source:            [source + referrer if applicable]
Project:           [type + brief description]
Location:          [neighborhood]
Stated budget:     [$X / not stated]
Timeline:          [stated timeline]
Decision maker:    [present / unclear / not available]
Funding:           [confirmed / unconfirmed / unknown]

QUALIFICATION SCORE
──────────────────────────────────────────────────────────
Green flags:       [X] — [list them]
Red flags:         [X] — [list them]
Hard disqualifiers: [none / list if present]

VERDICT
──────────────────────────────────────────────────────────
[✅ PRIORITY / ✅ QUALIFIED / ⚠️ CONDITIONAL / ❌ DECLINE / ❓ GET BUDGET FIRST]

RECOMMENDED NEXT STEP
──────────────────────────────────────────────────────────
[Specific action — not vague. Example: "Call back today, confirm budget range using 
script below before confirming site visit. If budget aligns, schedule for this week 
and plan to present preconstruction proposal at the meeting."]

ESTIMATED PROJECT RANGE (if enough info to run ballpark)
──────────────────────────────────────────────────────────
[Run ballpark if project type + neighborhood + rough scope is known]
[Skip if insufficient info — note "run ballpark generator once more details confirmed"]

═══════════════════════════════════════════════════════════
```

---

## RESPONSE TEMPLATES

### Initial Response to New Inquiry (email / text)
> Thanks for reaching out. [Project type] renovations in [neighborhood] are exactly the kind of work we specialize in. Before we schedule a site visit, I'd like to make sure we're aligned on investment range so we're not wasting each other's time. Projects like yours typically run between [LOW] and [HIGH] depending on scope and existing conditions. Does that range work for your budget? If so, I'd love to set up a time to walk the property.

### Budget Probe (when budget not stated)
> One quick question before we set up a time — do you have a target investment range in mind? I ask because projects of this type in DC can range quite a bit depending on scope, and I'd rather have that conversation upfront than after we've both invested a few hours. No wrong answer — just helps me come prepared.

### Preconstruction Proposal at Site Visit
> Based on what I saw today, this is absolutely a project we can take on. To do this right — and give you a budget you can actually rely on — the next step is a formal preconstruction engagement. That's a paid service: [$X], fully credited toward construction if we proceed. It covers a detailed scope document, trade partner input, a permit feasibility review, and a preliminary schedule. I can have the agreement to you by [day]. Want to move forward?

### Conditional Hold (budget unknown, not responded yet)
> Before confirming the site visit, send the budget probe script. Do not schedule until budget range is confirmed or prospect explicitly asks to discuss at the visit.

### Decline — Budget Misaligned
> Thanks for thinking of us for this project. Based on what you've described, projects of this scope in DC typically run between [LOW] and [HIGH]. That's higher than the budget you mentioned, and I'd rather be upfront now than put us both through a process that doesn't end in a project we can build responsibly. If the budget changes or you want to talk through a more focused scope, I'm happy to revisit. Best of luck with it.

---

## REFERRER TRACKING NOTE

If lead came from a referral, log the referrer:
- Name of referring architect or past client
- This feeds Plomada's referrer performance tracking
- Over time: number of leads sent, conversion rate, total contract value generated per referrer
- High-value referrers get proactive relationship maintenance (thank-you note, project update, lunch)
