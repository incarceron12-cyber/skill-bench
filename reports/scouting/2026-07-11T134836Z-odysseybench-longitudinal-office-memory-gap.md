# Scouting note — OdysseyBench longitudinal office-memory validity gap

**Timestamp:** 2026-07-11T13:48:36Z  
**Scope:** Narrow expansion against charter objectives A/B/D after confirming 104 completed tasks, two pending consolidation tasks, one blocked real-elicitation task, and no ready review/source backlog. This run did not repeat broad discovery.

## Substantive finding (triage only)

**OdysseyBench: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows**

- Immutable arXiv v1 record: https://arxiv.org/abs/2508.09124v1
- Immutable PDF: https://arxiv.org/pdf/2508.09124v1
- Official repository: https://github.com/microsoft/OdysseyBench
- Repository HEAD observed during scouting: `3389881fa9e1dbc6e13c5b0706da8007e88d09d4`
- The repository already holds the acquired but unreviewed v1 PDF and 87,239-character extraction at `data/papers/pdfs/2508.09124v1-odysseybench-evaluating-llm-agents-on-long-horizon.pdf` and `data/papers/text/2508.09124v1-odysseybench-evaluating-llm-agents-on-long-horizon.txt`.
- Search/arXiv metadata describes office workflows spanning Word, Excel, PDF, email, and calendar, with two reported splits: OdysseyBench+ and OdysseyBench-Neo. This is directly relevant to the unresolved boundary between remembered interaction history and consequential downstream work.
- **Evidence status:** metadata, repository-presence, and local-acquisition triage only. The paper, tasks, histories, graders, experiments, and release were not read during scouting. No claim is made that the tasks are realistic or longitudinal, that history use causes performance, that selected evaluators cover professional outcomes, or that either split improves on OfficeBench.

## Benchmark implication to test

A full audit should separate history retrieval, temporal recognition, reasoning, application action, artifact/state consequence, and environment validity. It should determine whether histories preserve actual workflow dependencies or merely provide answer-bearing context; whether OdysseyBench+ reuse and Neo synthesis support different inference populations; and whether graders observe complete consequential outcomes, sparse predicates, or reference-path compliance. The completed OfficeBench and LongMemEval-v2 reviews provide the nearest nonduplicate comparisons.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark evidence), B (realistic longitudinal-work and memory validity), and D (professional-family consolidation).
- **Evidence/artifact sought:** immutable-v1 full-paper review plus pinned official-release audit with page/file locators.
- **Uncertainty clarified:** what capability the benchmark can distinguish among context retrieval, memory use, workflow execution, and professional outcome production.
- **Mode/balance:** one narrow review task restores a ready review item while two consolidation tasks remain pending; no additional source was added.
- **Duplication/scope:** OdysseyBench appears only as an unaudited landscape member and local unreviewed acquisition; no queue task or review covers it. Office workflows are a substrate case, not a permanent domain choice.
- **Useful completion:** reconstruct both split lineages, history/task/environment/grader contracts, baselines and release drift; inspect representative tasks/evaluators; preserve claim limits; derive only nonduplicate retain/repair/test implications.

Added `review-odysseybench-longitudinal-office-memory-validity` (priority 52). No second task was added.
