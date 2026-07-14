# Scouting note — PaperBench replication-artifact validity gap

**Timestamp:** 2026-07-14T21:05:58Z  
**Scope:** Narrow expansion against charter objectives A/B/C. The queue contained 227 tasks before this addition: 220 completed, four blocked, two pending human decisions, and one pending consolidation; no source/research/review task remained. The benchmark-landscape program and state-of-the-art map explicitly name PaperBench under long-horizon research and artifact generation, but the repository had only citation mentions—no acquisition record, review, scouting note, or queue task.

## Substantive finding (triage only)

**PaperBench: Evaluating AI's Ability to Replicate AI Research**

- Immutable record selected for review: https://arxiv.org/abs/2504.01848v3
- Immutable PDF: https://arxiv.org/pdf/2504.01848v3
- Official PaperBench release surface: https://github.com/openai/frontier-evals/tree/main/project/paperbench
- Official project page: https://openai.com/index/paperbench/
- The arXiv API identifies Giulio Starace and 12 coauthors, categories `cs.AI`/`cs.CL`, initial submission on 2 April 2025, and latest immutable version `v3` updated 7 April 2025. The summary contains no withdrawal notice. Versioned v1 abstract/PDF URLs, the project page, and the current GitHub subtree returned HTTP 200; the reviewer must acquire v3 rather than silently reading an earlier version.
- The **v3 abstract** describes 20 ICML 2024 Spotlight/Oral paper-replication tasks, hierarchically decomposed author-co-developed rubrics totaling 8,316 individually gradable criteria, an LLM judge plus a separate judge benchmark, frontier-agent trials, and a top-ML-PhD comparison. It reports 21.0% average replication score for the best tested agent and says models did not outperform the human baseline. These are author-reported abstract claims, not independently verified findings.
- The current `openai/frontier-evals` repository is a non-fork MIT project whose observed `main` head is commit `51052cede8cc608f95bb00346635e03759013e5a` dated 21 April 2026—more than a year after immutable arXiv v3. It is a post-paper artifact unless a paper-time release identity is recovered. No repository files, task bytes, rubrics, graders, run records, or result matrices were inspected during scouting.
- The distinctive validity question is not merely whether agents can write research code. PaperBench connects a long-horizon persistent artifact to thousands of hierarchical partial-credit criteria, author participation, judge validation, and a time-budgeted human comparison. A deep review must determine whether dependent criteria inflate apparent progress, whether one rubric tree admits legitimate alternative replications, whether artifact execution and scientific result fidelity are separately observed, and whether human and agent environments, assistance, compute, stopping, and missing runs are comparable.
- This is **metadata, abstract, URL, release-location, and duplicate triage only**. The full paper, appendices, task/rubric data, judge benchmark, agent/human attempts, statistical analyses, code, environments, and costs were not read or audited. No claim is made that PaperBench establishes successful replication, scientific validity, expert equivalence, general research capability, scalable grading validity, or readiness.

## Benchmark implication to test

Research-replication evaluation needs an explicit chain: `source paper and selected contribution → immutable task/environment/compute contract → author/expert authority and rubric transformation → obligation/dependency graph with valid alternatives → agent actions and persistent code/results artifact → executable and scientific-result observations → criterion applicability/dependence → judge evidence view and calibrated reliability → paper-level aggregation → human/configured-system comparison → bounded replication claim`. Fine-grained partial credit can improve diagnosis while still double-counting one upstream failure or rewarding conformance to one authored path.

The full review should compare PaperBench with AstaBench's heterogeneous suite aggregation, AARRI's research-judgment lifecycle, ResearchRubrics' criterion-authoring boundary, SciVisAgentBench's artifact-view admissibility, and the repository's dependency-aware scoring machinery. Transfer should reuse artifact, evidence-view, configured-system, metric, task-health, and validity records rather than create a science-specific schema.

## Charter decision filter and queue action

- **Objectives advanced:** A (long-horizon research benchmark frontier), B (expert rubric/artifact-to-claim validity), and C (evidence for dependency-aware grading and configured human/agent comparison).
- **Evidence/artifact sought:** immutable-v3 deep review, timing-bounded official release audit, and one replayed released grader/judge-validation result if inspectable.
- **Uncertainty clarified:** whether hierarchical partial credit, author co-development, and a judge benchmark support full-replication or expert-comparison claims, and which observations remain missing.
- **Mode/balance:** one low-priority review task restores a minimal research backlog behind the pending consolidation and human blockers; no broad search or source bundle was added.
- **Duplication/scope:** fills an explicit landscape gap and complements rather than repeats AstaBench, AARRI, ResearchRubrics, and artifact-evaluation reviews; research replication is a bounded test of reusable machinery, not a permanent domain choice.
- **Useful completion:** preserve task/paper sampling, rubric lineage/dependence/alternatives, environment/artifact identity, agent/human configurations and time, invalids/missingness, judge labels/evidence/reliability, aggregation, uncertainty, cost, release drift, and strict claim ceilings.

Added `review-paperbench-replication-artifact-validity` (priority 19). No second task was added.

## Operational note

The required initial `git pull --ff-only` could not authenticate to the HTTPS GitHub remote (`could not read Username`). Local `main` was 33 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.
