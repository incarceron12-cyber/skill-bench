# Scouting note — HippoCamp personal-context validity gap

**Timestamp:** 2026-07-11T15:04:10Z  
**Scope:** Narrow expansion against charter objectives A/B/D after confirming 108 completed tasks, two pending consolidation tasks, one blocked real-elicitation task, and no ready source/review backlog. This run did not repeat broad discovery.

## Substantive finding (triage only)

**HippoCamp: Benchmarking Contextual Agents on Personal Computers**

- arXiv record: https://arxiv.org/abs/2604.01221
- Official project page: https://hippocamp-ai.github.io/
- Official repository: https://github.com/synvo-ai/HippoCamp
- Repository HEAD observed during scouting: `e7eda45b2d3c3b37cbaae77d175ed730a53be691`
- Search/arXiv metadata describes a benchmark for contextual agents operating over realistic multimodal personal file systems, with search, perception, reasoning, and file-management demands. This is a direct but currently uncovered boundary between context availability and consequential user-specific action.
- **Evidence status:** metadata, project/repository presence, and URL verification only. The paper, participant/data provenance, task suite, file systems, graders, experiments, privacy process, and release were not read during scouting. No claim is made that the environments are representative, that personalization is measured validly, that file actions have complete consequence coverage, that privacy protections are sufficient, or that the release reproduces the paper.

## Benchmark implication to test

A full paper-and-release audit should separate personal-context availability, authorized access, relevant retrieval, multimodal perception, user-specific inference, action execution, and intended/collateral file-state consequences. It should inspect whether a small number of contributed digital environments licenses only case-specific claims; whether tasks evaluate contextual action or mostly answer retrieval questions; and whether provenance, consent, privacy, alternate paths, and evaluator evidence are inspectable. Workspace-Bench and LongMemEval-V2 provide the nearest nonduplicate comparisons.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark evidence), B (context-to-consequential-action validity), and D (workspace/memory family comparison).
- **Evidence/artifact sought:** immutable full-paper review plus pinned official-release audit with page/file locators.
- **Uncertainty clarified:** what capability HippoCamp can distinguish among file access, retrieval, multimodal understanding, personalization, action, and state consequence.
- **Mode/balance:** one narrow review task restores a ready review item while two consolidation tasks remain pending; no second source was added.
- **Duplication/scope:** repository search found no HippoCamp acquisition, review, index entry, or queue task. Personal computing is a substrate case, not a permanent domain choice.
- **Useful completion:** reconstruct participant/data/task/environment/grader contracts, inspect representative tasks and evaluators, preserve privacy/sample/release limits, and derive only nonduplicate retain/repair/test implications.

Added `review-hippocamp-personal-context-validity` (priority 51). No second task was added.
