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

## Charter relationship

The system serves [`PROJECT_CHARTER.md`](../PROJECT_CHARTER.md). It is infrastructure for researching, learning, building, validating, and consolidating the knowledge-work benchmark—not a separate self-improvement project. Its cadence and tools may evolve, but its priorities must remain charter-aligned.

## 24/7 compounding cadence

Work runs continuously in staggered, role-separated cycles:

1. **Orchestrate:** inspect the queue, recent evidence, workstream balance, and charter alignment.
2. **Scout:** expand into high-value primary sources and alternative benchmark approaches.
3. **Acquire/extract:** preserve full text, artifacts, metadata, and provenance.
4. **Research/review:** read deeply and convert evidence into concepts and design implications.
5. **Build/validate:** create schemas, validators, graders, tasks, fixtures, trials, and tests.
6. **Consolidate:** merge findings into canonical documents, remove duplication, and prevent premature narrowing.
7. **Brief:** explain learning, implementation, benchmark impact, system health, and decisions to Samuel four times daily.

A 15-minute heartbeat is a coordination frequency, not an output quota. Workers may perform no-ops when the queue is healthy or when additional activity would be duplicative. Research/build work continues overnight; human-facing updates are consolidated.

Every cycle should be evaluated by whether it advances a charter objective and produces useful evidence, understanding, or benchmark infrastructure—not by source count, commits, or run frequency.

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
