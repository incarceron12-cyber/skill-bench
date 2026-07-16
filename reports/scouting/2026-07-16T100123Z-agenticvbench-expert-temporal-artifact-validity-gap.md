# Scouting note — AgenticVBench expert temporal-artifact validity gap

**Timestamp:** 2026-07-16T10:01:23Z  
**Scope:** Narrow comparative expansion under charter objectives A/B/C. Queue intake showed 318 tasks: 313 completed, three blocked, two pending, and no pending source/research/review task. Existing coverage is strong, so this run searched specifically for a successor-style test of the recently reviewed CutVerse temporal-artifact boundary rather than repeating a broad benchmark search.

## Substantive finding — triage only

**AgenticVBench: Can AI Agents Complete Real-World Post-Production Tasks?** — Zongheng Cao, Yi Zheng, Rui Song, and Xinyu Hu, arXiv:2605.27705v1.

- Immutable record: https://arxiv.org/abs/2605.27705v1
- Immutable PDF: https://arxiv.org/pdf/2605.27705v1
- Project page: https://agenticvbench.com/
- Official repository pinned at scouting time: https://github.com/PhiloLabs/agentic-vbench/tree/2933a7bfa1bd6134f0a5f76d7efc728f081dd53e
- Project-linked dataset location: https://huggingface.co/datasets/philolabs/agenticvbench (returned HTTP 401 during unauthenticated scouting)

The arXiv API identifies immutable v1, submitted and last updated 26 May 2026, with no withdrawal notice in the summary. The author-reported abstract describes 100 tasks in four post-production families, derived from workflows contributed by 20 industry experts averaging six years of experience; mixed programmatic verifiers and expert rubrics; frontier systems run through vendor-native and open-source harnesses; same-task human expert performance; and substantial harness-dependent differences in score, tool use, and failure mode. These are abstract claims requiring full-paper verification.

The arXiv HTML and PDF, project page, and official GitHub repository were reachable. GitHub API verification found an unarchived Apache-2.0 repository whose mutable `main`/`HEAD` was `2933a7bfa1bd6134f0a5f76d7efc728f081dd53e`, committed 15 July 2026—50 days after arXiv v1. Its complete API tree contained 1,592 entries and exposed task directories for assembly, repair, sequencing, and understanding, including instructions, environments, solution witnesses, and judge/test paths. Scouting inspected only URL status and tree metadata, not file contents or execution. The post-v1 timing means the release cannot automatically evidence the paper-time instrument or results.

Repository-wide exact-title/ID search found no existing AgenticVBench review or queue task. The paper is cited incidentally in the EnterpriseClawBench extraction. CutVerse is the nearest completed review, but its audited release lacked the claimed benchmark and its screenshot milestones did not observe native project structure, rendered temporal behavior, creative quality, or recipient use.

This is **metadata, abstract, URL, repository-metadata/tree, access-state, and duplicate triage only**. The paper, appendices, task bytes, source assets, expert contribution records, rubrics, judges, human study, harnesses, trajectories, results, statistics, and release code were not read or audited. No claim is made that AgenticVBench repairs CutVerse, samples professional work, transfers expertise, observes temporal/native-artifact correctness, supports a valid human comparison, identifies a harness effect, reproduces, or establishes capability, professional validity, production fitness, or readiness.

## Why this is distinct

AgenticVBench is valuable as a direct comparative validity test, not simply another media benchmark. It appears to add four things that CutVerse claimed weakly or did not release: a substantial inspectable task tree; a larger and more explicitly characterized expert-contributor pool; mixed deterministic/expert evaluation; and same-task human plus multi-harness comparisons. A full audit can therefore ask whether those apparent repairs actually close the evidence chain:

`professional workflow provenance → task/source projection → native and rendered temporal artifact evidence → programmatic/expert criterion authority → configured harness trial → human comparison → bounded professional-use claim`.

The key uncertainties are whether expert contribution is task-level and independently approved; whether judges inspect editable projects and time-indexed audio/video rather than proxies; whether programmatic and expert criteria have typed precedence and reliability; whether human and agent administrations are comparable; and whether harness comparisons hold task, model, observation, action, budget, retry, and grader conditions sufficiently fixed for causal language.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic knowledge-work and benchmark-frontier comparison), B (expert-workflow-to-task/rubric transformation), and C (temporal artifacts, plural graders, configured-system trials).
- **Concrete evidence/artifact:** immutable-v1 deep review and commit-pinned release audit, with one end-to-end representative task path from each reported family.
- **Uncertainty clarified:** whether a seemingly more inspectable successor repairs temporal-artifact, expert-authority, human-baseline, and harness-validity gaps exposed by CutVerse.
- **Mode:** narrow expansion feeding comparative consolidation/validation; post-production is a bounded stress case for reusable benchmark machinery, not a scope commitment.
- **Duplication check:** no exact local coverage. Required comparison with CutVerse, DeskCraft, Workflow-GYM, SciVisAgentBench, and configured-system evidence prevents isolated collecting.
- **Useful completion:** reconciled paper/release/task/result denominators and explicit retain/repair/test conclusions with strict claim ceilings.

Added one task: `review-agenticvbench-expert-temporal-artifact-validity` (priority 18). No second task was added.
