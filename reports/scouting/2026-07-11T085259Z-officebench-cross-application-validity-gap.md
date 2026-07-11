# Scouting note — OfficeBench cross-application validity gap

**Timestamp:** 2026-07-11T08:52:59Z  
**Scope:** Narrow expansion against charter objectives A/B/D after confirming 90 completed tasks, four pending tasks, one blocked real-elicitation task, and an explicit OfficeBench/WorkArena primary-source gap in the professional benchmark synthesis. This run did not repeat broad discovery.

## Substantive finding (triage only)

**OfficeBench: Benchmarking Language Agents across Multiple Applications for Office Automation**

- Immutable arXiv v1 record: https://arxiv.org/abs/2407.19056v1
- Immutable PDF: https://arxiv.org/pdf/2407.19056v1
- Official repository: https://github.com/zlwang-cs/OfficeBench
- The arXiv search record identifies OfficeBench as a 2024 benchmark for office tasks spanning multiple applications; the official repository exists and its HEAD resolved during this scout (`b978b808667c32b52ce19a67ce1def1de9ae02b7`).
- OfficeBench is a high-leverage historical anchor because the already acquired OdysseyBench paper explicitly derives part of its task set from OfficeBench, while the current professional evolution matrix deliberately withholds deep claims pending a primary paper/release audit.
- This is **metadata/search-result and repository-presence triage only**. The paper, appendices, task files, environment, graders, results, and repository history were not read during scouting. No claim is made that tasks are ecologically representative, resets are valid, programmatic checks are complete, alternative workflows are accepted, or reported performance measures professional capability.

## Benchmark implication to test

A full audit should separate realistic-looking task descriptions from valid cross-application execution evidence. It should inspect whether file and application state, intermediate dependencies, destructive side effects, and alternate valid paths are observable; whether reset and version semantics support comparable trials; and whether evaluator predicates cover the consequential artifact/state delta. Comparison with OdysseyBench can then test which weaknesses its longer-horizon successor actually repairs, rather than assuming succession implies improvement.

## Charter decision filter and queue action

- **Objectives advanced:** A (benchmark frontier), B (knowledge-work task and evidence boundaries), and D (historical-anchor-to-successor consolidation).
- **Evidence/artifact sought:** immutable-v1 full-paper review and pinned official-release audit with page/file locators.
- **Uncertainty clarified:** which claims OfficeBench's task, environment, and evaluator design can support, and what OdysseyBench materially changes.
- **Mode/balance:** one narrow expansion task; the existing ready queue otherwise contains one broad landscape research task and consolidation/build work.
- **Duplication/scope:** canonical maps explicitly mark OfficeBench as unaudited; no OfficeBench review or queue task existed. Office automation is a methodological case, not a domain commitment.
- **Useful completion:** reconstruct task origins, environment, reset, interaction, grading, baselines, errors, costs, release timing, and reproducibility; inspect representative tasks/graders; derive bounded retain/repair lessons.

Added `review-officebench-cross-application-office-validity` (priority 56). No second task was added.
