# Scouting note — OSWorld 2.0 workflow-validity gap

**Timestamp:** 2026-07-11T09:23:13Z  
**Scope:** Narrow expansion against charter objectives A/B/D after confirming 92 completed tasks, two pending consolidation tasks, two blocked tasks, and an explicit OSWorld 2.0 primary-source/release gap in the interactive-family synthesis. This run did not repeat broad discovery.

## Substantive finding (triage only)

**OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks**

- Immutable arXiv v1 record: https://arxiv.org/abs/2606.29537v1
- Immutable PDF: https://arxiv.org/pdf/2606.29537v1
- Official repository: https://github.com/xlang-ai/OSWorld-V2
- Search metadata identifies a 28 June 2026 submission describing 108 long-horizon computer-use workflows across everyday and professional tasks. The official repository is discoverable; search metadata indicates that official task classes may be distributed through a gated Hugging Face dataset, which the review must verify rather than assume.
- This is high leverage because the repository already contains a full OSWorld 1.0 review and explicitly names OSWorld 2.0 as an unaudited successor. It permits a direct test of whether shifting from shorter tasks to workflows repairs evaluator, environment, side-effect, reliability, and professional-validity limits.
- This is **metadata/search-result and repository-presence triage only**. The paper, appendices, task classes, evaluators, environments, results, and repository history were not read during scouting. No claim is made that task scenarios are ecologically representative, checkpoints are complete, resets are valid, graders cover consequential side effects, or reported performance measures professional capability.

## Benchmark implication to test

A full audit should separate longer nominal horizon from stronger workflow validity. It should inspect task provenance and sampling; checkpoint observability and dependence; whether partial credit tracks meaningful professional progress; reset and environment-health controls; grader coverage of intermediate and unintended state; alternate valid paths; cost and repeatability; and release inspectability. A matched comparison with OSWorld 1.0 should establish which weaknesses are actually repaired and which are merely displaced or made harder to inspect.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier and successor evidence), B (workflow/state/evaluator validity), and D (anchor-to-successor comparison).
- **Evidence/artifact sought:** immutable-v1 full-paper review and pinned official-release audit with page/file locators and an explicit OSWorld 1.0 comparison.
- **Uncertainty clarified:** whether long-horizon workflow and checkpoint design adds valid diagnostic evidence beyond harder computer-use tasks.
- **Mode/balance:** one narrow expansion task; the ready queue otherwise contains only two consolidation tasks, while the completed corpus is already broad.
- **Duplication/scope:** canonical synthesis explicitly marks OSWorld 2.0 as a gap; no existing queue task or review covers arXiv 2606.29537. Computer use is a methodological case, not a domain commitment.
- **Useful completion:** reconstruct construct, task selection, environment, reset, checkpoints, scoring, baselines, errors, cost, maintenance, release timing, and reproducibility; inspect representative released task/evaluator artifacts; derive bounded retain/repair/test conclusions.

Added `review-osworld2-long-horizon-workflow-validity` (priority 58). No second task was added.
