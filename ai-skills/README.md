# Construction AI Toolkit

AI skills I built and used to run BBCDC Construction & General Contractors, a licensed design-build firm in Washington, DC that does historic renovation, structural underpinning and complex residential and commercial work.

Each folder is a Claude skill: a written procedure plus the domain rules the model follows, so the same request gets the same quality of answer every time. They encode how my firm priced, scheduled, costed and qualified work.

| Skill | What it does |
|---|---|
| [ballpark-generator](ballpark-generator/SKILL.md) | Turns a project type, DC neighborhood and rough scope into a free first-tier cost range, with the caveats a client needs to hear. The first gate in my two-tier sales model: ballpark before any site visit. |
| [lead-qualification](lead-qualification/SKILL.md) | Scores a new inquiry on budget fit and red flags and gives the exact next step. Feeds the Plomada (this repo) lead engine. |
| [schedule-generator](schedule-generator/SKILL.md) | Builds a preliminary construction schedule with DC permit and inspection milestones, decision deadlines for long-lead selections, and phasing for occupied homes. |
| [job-costing](job-costing/SKILL.md) | Takes takeoff quantities and produces a fully costed estimate: labor hours, burdened rates, overhead allocation, target margins and a Profit First breakdown (Simple Numbers method). |
| [material-takeoff](material-takeoff/SKILL.md) | Reads uploaded plan sets and breaks them into trade scope packages: MEP bid packages, framing counts, drywall sheet counts and rough pricing. |
| [dc-feasibility](dc-feasibility/SKILL.md) | Pulls a DC property's records (PropertyQuest, listing data), applies the zoning rules and produces a client-ready feasibility report. The sample in `generate_report.py` uses a fictional address. |

## How they fit together

A lead comes in and gets qualified. A good lead gets a ballpark the same day. If the owner wants to go further, the feasibility report answers what DC will let them build, the takeoff and costing produce the real number, and the schedule shows how long permitting and construction will take.

I'm turning this flow into software in Plomada (this repo), an operating system for small design-build contractors.

Miles Gray, licensed general contractor, Washington, DC.
