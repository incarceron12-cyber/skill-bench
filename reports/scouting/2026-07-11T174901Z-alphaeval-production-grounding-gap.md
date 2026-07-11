# Scouting note — AlphaEval production-grounding validity gap

**Timestamp:** 2026-07-11T17:49:01Z  
**Scope:** Narrow expansion against charter objectives A/B/D after confirming 112 completed tasks, two pending consolidation tasks, one blocked real-elicitation task, and no ready review task. This run did not repeat broad benchmark discovery.

## Substantive finding (triage only)

**AlphaEval: Evaluating Agents in Production**

- Immutable arXiv record: https://arxiv.org/abs/2604.12162v1
- Immutable PDF target: https://arxiv.org/pdf/2604.12162v1
- Official project page: https://alphaeval.ai/
- arXiv/search metadata describes 94 production-grounded tasks sourced through seven companies across six O*NET domains, plus a reusable pipeline from authentic production requirements to automated benchmark tasks.
- This is directly relevant to skill-bench because it appears to connect naturally occurring organizational demand, requirement transformation, executable tasks, and automated evaluation. The nearest reviewed comparisons cover session-to-task projection (EnterpriseClawBench), occupational framing (GDPval), expert-authored long-horizon tasks (Agents' Last Exam), and production evaluation operations, but not this reported multi-company requirement-to-benchmark pipeline.
- **Evidence status:** arXiv/search metadata and URL verification only. The PDF, partner and task sampling, requirement intake, transformation procedure, environments, graders, baselines, statistics, confidentiality constraints, and any public release were not read during scouting. The task/company/domain counts remain metadata-level author claims pending full-text verification. No claim is made that the tasks are representative, that production grounding survives transformation, that automated graders are valid, or that benchmark performance predicts production readiness.

## Benchmark implication to test

A full review should treat production provenance as only the beginning of an evidence chain. It should separate observed company requirement, selected contribution, confidentiality-driven projection, authored task obligations, environment realization, grader-observable consequences, configured-system trial, and licensed deployment claim. It should inspect independence among company contributors, task authors, grader builders, and validators; identify what production context or consequences were removed; and test whether task and domain sampling supports anything beyond the participating cases.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier and production-system evidence), B (expertise/requirement-to-evaluation methodology), and D (cross-family consolidation input).
- **Evidence/artifact sought:** immutable-v1 full-paper review and a pinned official-release audit if artifacts are inspectable.
- **Uncertainty clarified:** whether authentic production provenance survives task/grader transformation and what inference population the resulting scores support.
- **Mode/balance:** one narrow review task restores a ready expansion item while two consolidation tasks remain pending; no second source was added.
- **Duplication/scope:** repository search found only an AlphaEval citation in acquired ALE text, not a review or queue task. Participating companies are evidence cases, not a commitment to one profession or enterprise-only scope.
- **Useful completion:** reconstruct the requirement-to-benchmark chain with page/file evidence, preserve sampling/confidentiality/release limits, compare against existing projection and validity machinery, and add only nonduplicate implications.

Added `review-alphaeval-production-grounded-validity` (priority 50). No second task was added.
