# Scouting note — WorkArena++ compositional validity gap

**Timestamp:** 2026-07-11T11:33:48Z  
**Scope:** Narrow expansion against charter objectives A/B/D after confirming 100 completed tasks, three pending tasks, one blocked real-elicitation task, and WorkArena as the remaining explicit primary-source gap in the professional benchmark synthesis. This run did not repeat broad discovery.

## Substantive finding (triage only)

**WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks**

- arXiv record: https://arxiv.org/abs/2407.05291
- Official repository: https://github.com/ServiceNow/workarena
- Repository HEAD observed during scouting: `a772230a94cf1caf4166b8ead3983f3b3786455b`
- Search metadata describes 682 tasks intended to represent realistic workflows performed by knowledge workers. The official repository links the paper and is also the implementation surface inherited by the newly reviewed BrowserGym ecosystem.
- This is high leverage because the professional evolution synthesis explicitly withholds WorkArena claims pending a primary-source audit, while the BrowserGym audit now makes adapter-level measurement equivalence an active consolidation question.
- **Evidence status:** search metadata and repository-presence triage only. The paper, appendices, task definitions, composition procedure, ServiceNow environment, evaluators, experiments, and release history were not read. The immutable arXiv version must be resolved by the reviewer. No claim is made that task composition preserves realistic workflow structure, that 682 tasks represent knowledge work, that reset/evaluator behavior is valid, or that BrowserGym preserves WorkArena semantics.

## Benchmark implication to test

A full audit should distinguish longer or compositional task syntax from consequential workflow validity. It should inspect task provenance, dependency and state transitions, initial-state/reset guarantees, alternate valid paths, evaluator predicate coverage, partial-credit semantics, and the exact BrowserGym coupling. Comparison with base WorkArena should identify which weaknesses WorkArena++ actually repairs and what empirical evidence supports the repair.

## Charter decision filter and queue action

- **Objectives advanced:** A (benchmark frontier), B (realistic task and validity methodology), and D (family evolution consolidation).
- **Evidence/artifact sought:** version-preserving full-paper review and pinned official-release audit with page/file locators.
- **Uncertainty clarified:** whether compositional enterprise workflows provide stronger knowledge-work evidence or mainly concatenate authored subtasks under incomplete state predicates.
- **Mode/balance:** one narrow review task; the ready queue already contains one build and two consolidation tasks, so no additional source was added.
- **Duplication/scope:** the canonical synthesis explicitly labels WorkArena a gap; no review or queued task covered it. Enterprise web software is a substrate case, not a benchmark-domain commitment.
- **Useful completion:** reconstruct the task, environment, reset, evaluator, experimental, cost, and release contracts; inspect representative base/plus tasks and BrowserGym integration; derive bounded retain/repair/test implications.

Added `review-workarena-plus-compositional-knowledge-work-validity` (priority 53). No second task was added.
