# Plomada

Plomada is an operating system I'm building for small residential design-build contractors in Washington, DC. It grew out of running my own firm, BBCDC Construction & General Contractors, where the same steps repeated on every job: qualify the lead, give a fast ballpark, schedule around DC permitting, cost the work and buy it out.

This repo holds **Module 1: the Lead Engine**.

## What the Lead Engine does

- An intake form captures what a contractor needs to know before driving to a site visit: lead source, project type, DC neighborhood, stated budget, timeline, property status, whether an architect is involved, who makes the decision, and how the project is funded.
- Every lead is saved to a local SQLite database and listed newest first.
- Each lead has fields for a qualification score, a go / no-go verdict and a drafted reply, so an AI step can grade the lead and write the first response.

It runs on the two-tier model I used at BBCDC: every lead gets a free ballpark before anyone commits time to a site visit.

## Run it

```bash
npm install
npm start   # http://localhost:3000
```

Node.js, Express and sql.js. No external services.

## The rest of the system

The other Plomada modules started as AI skills on Claude that I used in the business. They're in [ai-skills](ai-skills/):

- ballpark cost ranges for DC renovation work
- preliminary schedules with DC permit and inspection milestones
- job costing with labor burden, overhead and target margins
- material takeoffs and trade scope packages from plan sets
- DC property feasibility reports from PropertyQuest and zoning rules
- lead qualification

Built by Miles Gray, licensed general contractor, Washington, DC.
