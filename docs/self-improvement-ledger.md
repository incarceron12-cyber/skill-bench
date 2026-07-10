# Self-Improvement Ledger

This ledger tracks changes to the research/build system itself. The goal is evidence-driven improvement, not unconstrained self-modification.

| Date | Hypothesis | Change / experiment | Evidence to observe | Outcome | Decision |
|---|---|---|---|---|---|
| 2026-07-10 | A shared queue and role-separated cron workers will reduce duplicated work while increasing useful output cadence. | Introduce `data/work_queue.json`, queue CLI, project rules, review checker, and 24/7 staggered workers. | Duplicate-task rate, queue throughput, review quality failures, meaningful commits, benchmark artifacts produced, Samuel's assessment. | Pending first 24-hour run. | Evaluate after 24 hours. |

## Evaluation dimensions

- **Research signal:** proportion of discovered sources selected for deep review.
- **Evidence quality:** reviews based on full text rather than abstracts.
- **Conversion:** proportion of reviews that create a benchmark-design change.
- **Build throughput:** verified schemas/scripts/tasks produced.
- **Duplication:** repeated work on the same source/concept.
- **Consolidation:** reduction of redundant docs and unresolved notes.
- **Human value:** decisions clarified and concepts Samuel reports understanding better.
- **Cost discipline:** useful artifacts per agent run/token/API cost.

## Rules

1. Every substantial process mutation gets a row.
2. Define evidence before declaring improvement.
3. Prefer bounded changes that can be reverted.
4. Do not optimize activity metrics at the expense of benchmark quality.
5. Consolidation is part of the improvement loop, not optional cleanup.
