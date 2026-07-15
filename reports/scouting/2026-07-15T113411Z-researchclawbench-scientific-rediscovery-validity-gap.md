# Scouting note — paper-grounded scientific rediscovery validity gap

**Timestamp:** 2026-07-15T11:34:11Z

**Scope:** Narrow expansion against charter objectives A/B. Queue inspection found 265 tasks: 259 completed, four blocked, one pending human prerequisite, and one pending consolidation; no source, research, or review task remained. The corpus already covers scientific workflow execution, heterogeneous suite aggregation, research judgment, replication rubrics, and deployment of research artifacts, so this run searched only for a missing source-to-task/criterion design rather than repeating broad benchmark discovery.

## Substantive finding — triage only

**ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research** — Wanghan Xu et al.; arXiv:2606.07591v5.

- Immutable current record: https://arxiv.org/abs/2606.07591v5
- Immutable current PDF: https://arxiv.org/pdf/2606.07591v5
- Official repository: https://github.com/InternScience/ResearchClawBench
- The arXiv API identifies v5 as the current immutable version, originally submitted 28 May 2026 and updated 3 July 2026 in `cs.LG`, `cs.AI`, and `cs.CL`; its summary contains no withdrawal or retraction notice. Versioned v5 abstract, PDF, and HTML endpoints and the official repository returned HTTP 200 during scouting.
- The abstract reports 40 tasks across 10 scientific domains. Each task is reportedly grounded in a published target paper, supplies related literature and raw data, withholds the target paper, and uses expert-curated multimodal weighted criteria to score target-result rediscovery while nominally leaving room for new discovery.
- It reports evaluation of seven autonomous-research agents under a unified protocol and 17 native LLMs through a lightweight `ResearchHarness`. The abstract reports average scores of 21.5 for Claude Code and 20.7 for Claude-Opus-4.7 under the two respective evaluation paths, and names protocol mismatch, evidence mismatch, and missing scientific core as frequent error categories. These are author-reported abstract claims, not independently verified findings.
- Search-indexed official repository surfaces expose task, evaluation, contribution, and submission-validator directories/pages. The repository states that new submissions pass through a Hugging Face Space and pull-request review. Those pages, repository history, task bytes, dataset revision, rubrics, harness, validators, licenses, and paper/release correspondence were not inspected during scouting.
- Repository-wide exact-title, ID, and project-name searches found no local ResearchClawBench review or task. The closest completed reviews are SciAgentArena, AstaBench, AARRI, and PaperBench. ResearchClawBench is potentially distinct because its instrument appears to transform a hidden published study plus selected related literature/raw data into a rediscovery task and weighted multimodal criterion set.
- An initially surfaced task-authoring guideline (`2604.28093`) was rejected as a duplicate: it is already acquired and treated as a fully read companion source in the adversarial-verifier-hardening review. No task was added for it.
- This is **metadata, abstract, endpoint, official-release-location, and duplicate triage only**. The paper body, appendices, version history, target studies, literature/data packages, rubrics, model outputs, statistics, prompts, harness, repository, and dataset were not read or audited. No claim is made that target-paper withholding prevents contamination, that supplied packages are sufficient or professionally authorized, that criteria reward valid alternative discoveries, that reported scores are reliable or commensurate across tasks, or that the benchmark establishes novelty, autonomous science, scientific validity, cross-domain capability, production fitness, or readiness.

## Why this is distinct

The potentially reusable measurement chain is `published target study and result → target-study selection and licensed construct → supplied literature/raw-data evidence view → withheld-information and contamination boundary → agent experiment/analysis/artifact → criterion-level evidence and admissible alternatives → rediscovery score → independent scientific correctness/novelty → cross-domain or autonomous-research claim`. Each transformation can fail separately.

A target-paper-derived rubric can provide unusually concrete result evidence, but it can also turn science into reconstruction of one hindsight-visible analytical path. A full audit should determine whether alternative hypotheses, protocols, representations, null findings, and scientifically valid disagreements are admitted; whether criteria are independently authored or merely decomposed from the target; and whether the same hidden publication shapes task, oracle, error taxonomy, and score. Science is a bounded stress case for source-to-task projection and long-horizon artifact grading, not a scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent benchmark research) and B (source/expert evidence into tasks, artifacts, and grading).
- **Concrete evidence/artifact:** immutable-v5 deep review plus pinned official-release audit, with explicit v1→v5 change inspection and paper/release correspondence.
- **Uncertainty clarified:** whether a paper-grounded hidden-target design measures bounded result rediscovery, target reconstruction, package-conditioned analysis, or a defensible broader scientific-research construct.
- **Mode:** narrow expansion; scientific research is one cross-domain stress case, not the benchmark's permanent domain.
- **Duplication/scope:** no local duplicate; SciAgentArena, AstaBench, AARRI, and PaperBench are mandatory comparators.
- **Useful completion:** separate package conformance, rediscovery, independent judgment, novelty, scientific validity, reliability, cost, cross-domain capability, and readiness; retain/repair/test existing machinery rather than introducing a science-specific subsystem without evidence.

Added one task: `review-researchclawbench-scientific-rediscovery-validity` (priority 10). The pending criterion-operating-envelope consolidation, blocked empirical matrix repair, and human elicitation prerequisite remain higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Queue validation passed before the addition. Pre-existing modified/untracked README, site, paper-source, release, and script artifacts were not touched.
