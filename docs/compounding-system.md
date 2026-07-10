# Compounding System Design

## Objective

Create a system that improves Samuel's understanding and the project repository every day.

The system should not merely send paper summaries. It should:

1. discover relevant papers and benchmark releases,
2. download/read source material,
3. synthesize unique insights,
4. update the repository taxonomy and research agenda,
5. propose benchmark-design moves,
6. commit/push changes to GitHub,
7. send concise Telegram updates that develop Samuel's thinking.

## Daily cadence

### Morning — discovery and triage

Purpose: identify what is new and worth attention.

Output:
- 5–10 candidate papers/releases;
- why each might matter;
- top 2–3 to read deeply.

### Midday — deep paper review

Purpose: read actual downloaded papers and write structured reviews.

Output:
- 1–3 comprehensive paper reviews;
- methodology breakdown;
- unique insight;
- transfer into `skill-bench`.

### Evening — synthesis and benchmark design

Purpose: convert the day's learning into project direction.

Output:
- updated SOTA map;
- new benchmark primitives;
- scenario ideas;
- questions for Samuel;
- repo commit/push summary.

## Compounding artifacts

| Artifact | Path | Why it compounds |
|---|---|---|
| Paper index | `data/papers/index.json` | Prevents rediscovery; tracks status |
| Paper reviews | `papers/<topic>/` | Converts papers into reusable insights |
| SOTA map | `docs/state-of-the-art-map.md` | Accumulates landscape understanding |
| Incentive design | `docs/incentive-design.md` | Evolves strategy for expert contributions |
| Benchmark templates | `templates/` | Converts research insights into buildable specs |
| Task metadata template | `templates/task-metadata.md` | Captures difficulty features, domain primitives, root-cause tags, leakage controls, and response-matrix fields before pilots are built |
| Daily reports | `reports/daily/` | Preserves thinking over time |
| Git commits | GitHub history | Makes progress inspectable and reversible |

## Review standard

Every deep review should answer:

1. What did the authors actually build or measure?
2. What is the unique insight?
3. What methodology matters?
4. What is reusable for benchmark design?
5. What does this reveal about domain knowledge transfer?
6. What should be changed in the repo?
7. What question should Samuel think about next?

## Canonical benchmark-design references

This document defines the repository's research cadence; it no longer maintains
a second copy of benchmark primitives or evaluation layers. Use:

- [`benchmark-design-taxonomy.md`](benchmark-design-taxonomy.md) for the
  authoring lifecycle, measurement stack, configured-system identity,
  longitudinal evolution boundaries, and operating layer;
- [`../schemas/EXPERTISE_TRANSFER.md`](../schemas/EXPERTISE_TRANSFER.md) for the
  executable expert-claim → primitive → scenario → artifact/check procedure; and
- [`../schemas/README.md`](../schemas/README.md) for executable task, trial,
  grader, trace, recovery, and diagnosis contracts.

The critical compounding boundary is that **evaluated-agent evolution,
benchmark-design lessons, and released-instrument changes are different change
planes**. Evidence may produce a candidate lesson, but it must pass its own
provenance, leakage, contradiction, and independent-validation gates before it
changes durable benchmark guidance. This prevents research cadence from being
mistaken for benchmark improvement.

## Strategic idea

The project can be framed as an **expertise-to-evaluation engine**:

> We turn expert tacit knowledge into realistic AI-agent benchmark tasks.

That framing is broader and more defensible than “an AA-Briefcase clone.”
