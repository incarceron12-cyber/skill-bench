# Scouting note — workflow-derivation validity gap

**Timestamp:** 2026-07-13T18:43:14Z  
**Scope:** Narrow expansion against charter objectives A/B. Queue inspection found 180 tasks: 176 completed, two blocked, two pending (one build and one consolidation), no claimed work, and no pending source/research/review task. The reviewed corpus covers expert research rubrics, cognitive traps, research judgment, finance spreadsheet artifacts, and professional workflow state, but not a released benchmark centered on auditable stepwise derivations for financial research.

## Substantive finding (triage only)

**BigFinanceBench: A Workflow-Grounded Benchmark for Financial-Research Agents**

- Immutable arXiv record: https://arxiv.org/abs/2606.03829v1
- Immutable PDF: https://arxiv.org/pdf/2606.03829v1
- Official repository: https://github.com/Rogo-Technologies/big-finance-benchmark
- Project page: https://bigfinancebench.com/
- The arXiv API identifies Alex Wang, Georg Meinhardt, Jacob Katz, Joseph H. Kim, Pratyush K. Chaudhary, Chase Blagden, and Eric Xu; v1 was submitted 2 June 2026 in `cs.AI`, with no later version returned during this run.
- The abstract describes 928 expert-authored open-ended financial-research tasks. Each pairs a reference answer with a point-weighted rubric intended to decompose the derivation into independently checkable steps, totaling 36,241 rubric points.
- The abstract frames auditability around source selection, reporting period and accounting definition, assumptions, and calculation—not only final-answer agreement. It reports ten evaluated frontier/open-weight agents, a best aggregate rubric score of 58.8%, and nonuniform performance across workflow types. These are discovery leads only; denominators, task admission, agent configurations, retrieval access, repeats, uncertainty, grader behavior, and comparison validity require full-paper and release verification.
- The repository and project URLs resolved successfully during this run. The official Git repository advertised by search resolved at discovery HEAD `244fb7a4d57e0f6f5ac1d82c50f55c355f49a4bb`. Its files, history, dataset coverage, licensing, scorer, prompts, results, and relation to arXiv v1 were **not** inspected during scouting.
- Repository-wide duplicate search found neither the title nor arXiv ID. ResearchRubrics addresses expert criterion authoring; MBABench addresses native finance spreadsheets; AARRI addresses research judgment and legitimate non-completion; the consulting benchmark addresses expert-authored traps. None currently provides a full review of this benchmark's source-to-derivation-to-rubric chain and released public/held-out lifecycle.
- This is **metadata/abstract and URL triage only**. The paper, appendices, official repository, dataset, rubric records, graders, and result artifacts were not fully read or audited. No claim is made that the tasks represent financial-research work, that rubric points are independent or complete, that the reference derivation admits valid alternatives, that a score localizes causal failure, or that any system is professionally ready.

## Benchmark implication to test

A derivation rubric could connect evidence retrieval, source authority, period/definition choice, assumptions, transformations, calculations, and final claim into a diagnostically useful chain. But decomposing one reference answer can also encode one analyst's path, double-count shared upstream errors, reward exposed evaluator cues, or reject legitimate alternate derivations. A full audit should test whether BigFinanceBench supplies evidence for workflow diagnosis beyond final-answer scoring and whether its source/rubric machinery adds nonduplicate obligations to existing evidence-chain, dynamic-criterion, artifact-view, metric, and validity contracts. Finance is a bounded test of reusable derivation machinery, not a scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent and expert-rubric research) and B (expertise-to-evaluation through auditable derivations).
- **Evidence/artifact sought:** immutable full-paper review plus a pinned audit of the official repository/dataset, with exact task/rubric, grader, result, split, and release provenance.
- **Uncertainty clarified:** whether stepwise rubric credit validly observes workflow quality and localizes failures, or primarily measures agreement with one authored derivation and judge implementation.
- **Mode/balance:** narrow expansion; a build and consolidation task remain ready, while research/review backlog was empty.
- **Duplication/scope:** nonduplicate source-to-derivation question; the finance domain tests cross-domain evidence/rubric machinery and does not redefine the benchmark.
- **Useful completion:** verify headline claims from full text; pin and inspect release artifacts; audit task/SME sourcing, source and temporal controls, public/held-out coverage, alternate paths, criterion dependence, aggregation, grader reliability, configured systems, uncertainty, contamination, and reproducibility; preserve strict professional-validity, representativeness, readiness, and general-capability ceilings.

Added `review-bigfinancebench-workflow-derivation-validity` (priority 48). No second task was added.
