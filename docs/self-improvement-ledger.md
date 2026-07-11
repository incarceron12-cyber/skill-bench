# Self-Improvement Ledger

This ledger tracks changes to the research/build system itself. The goal is evidence-driven improvement, not unconstrained self-modification.

| Date | Hypothesis | Change / experiment | Evidence to observe | Outcome | Decision |
|---|---|---|---|---|---|
| 2026-07-10 | A shared queue and role-separated cron workers will reduce duplicated work while increasing useful output cadence. | Introduce `data/work_queue.json`, queue CLI, project rules, review checker, and 24/7 staggered workers. | Duplicate-task rate, queue throughput, review quality failures, meaningful commits, benchmark artifacts produced, Samuel's assessment. | Pending first 24-hour run. | Evaluate after 24 hours. |
| 2026-07-10 | A canonical charter and explicit document hierarchy will reduce mission drift and premature narrowing while allowing working methods to evolve. | Add `PROJECT_CHARTER.md`; make `.hermes.md`, the research agenda, README, and compounding system subordinate to it; require charter alignment checks for task selection and consolidation. | Queue balance across charter objectives, diversity of pilots/research, fewer scope-conflicting artifacts, and Samuel's assessment of clarity. | Pending observation. | Preserve founding intent; adapt working sections with evidence. |
| 2026-07-11 | Comparing widely used benchmark families with newer designs that explicitly address their limitations will reveal reusable strengths, inherited validity threats, and higher-leverage improvements for `skill-bench`. | Add a benchmark-landscape research program to `.hermes.md`; organize reviews by theme; seed balanced family-comparison tasks; require strengths, limitations, successor changes, evidence strength, and concrete design transfers. | Coverage across benchmark families; proportion of reviews with explicit retain/repair analysis; new cross-family conclusions; design changes linked to comparative evidence; reduced duplicate or unindexed reviews; Samuel's assessment of usefulness. | Pending comparative reviews and first consolidation cycle. | Keep if it produces cross-family design decisions rather than a larger paper catalog. |

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
