# Scouting note — multidimensional agent-reliability gap

**Timestamp:** 2026-07-11T00:38:39Z  
**Scope:** Narrow search against charter objectives A/C after confirming 73 completed tasks, one pending consolidation task, one blocked task, and no pending source/research/review work. This run targeted operational reliability beyond average benchmark success rather than repeating broad agent-benchmark discovery.

## Substantive finding (triage only)

**Towards a Science of AI Agent Reliability**

- Immutable arXiv record: https://arxiv.org/abs/2602.16666v3
- Immutable PDF location: https://arxiv.org/pdf/2602.16666v3
- Authors: Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan.
- The arXiv API reports a twelve-metric framework spanning consistency, robustness, predictability, and safety, evaluated on 15 models across two benchmarks. Its stated motivation is that mean task success hides whether failures repeat, respond to perturbations, can be anticipated, or have bounded severity.
- This candidate is distinct from the local task-health contract (instrument operation and role transitions), metric-monitoring contract (population/aggregation/alert semantics), Agent Psychometrics review (task-level performance prediction), and validity-centered review (claim/evidence arguments). It appears to join repeated-run behavior, perturbation response, failure prediction, and severity into one empirical profile.
- This is **arXiv API metadata and abstract triage only**. The full paper, appendices, code, benchmark configurations, prompts, perturbations, result tables, and supplemental materials were not read during scouting. No claim is made that the twelve metrics are valid, independent, prospectively predictive, safety-calibrated, deployment-ready, or portable to realistic knowledge work.

## Benchmark implication to test

Reliability should potentially be treated as a configured-system profile rather than a synonym for mean success. A full audit should determine whether replicate units are independent; perturbations preserve task meaning; predictability is evaluated prospectively rather than fitted and scored on the same failures; error severity has domain-grounded consequence scales; and uncertainty reflects task, run, benchmark, and model dependence. It should also test whether the proposed metrics fit existing trial, validity, task-health, and monitoring records without a new schema.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier production-agent evaluation) and C (diagnostic, scalable evaluation infrastructure).
- **Evidence/artifact sought:** immutable-v3 full-paper review plus pinned paper-linked-materials audit, reconstructing all estimands, treatments, sampling units, uncertainty, thresholds, and claim limits with page/file evidence.
- **Uncertainty clarified:** what reliability adds beyond success rate; which perturbation, repeatability, predictability, and severity claims are supported; and which fields or trials realistic knowledge-work evaluation needs.
- **Mode/balance:** one narrow expansion task at priority 64; review/research/source backlog was empty while consolidation remained represented.
- **Duplication/scope:** repository search found no occurrence of arXiv `2602.16666` or the title. The evaluated benchmarks are methodological cases, not domain commitments.
- **Useful completion:** separate capability accuracy from reliability; preserve configured-system, benchmark, dependence, and generalization limits; compare against existing local contracts; add no duplicate implementation task.

Added `review-agent-reliability-profile` (priority 64). No second task was added. TAG (`2607.02615v2`) was triaged but deferred because its test-driven artifact loop overlaps recent artifact-integrity and grader-intervention work; BankerToolBench was already explicitly deferred in an earlier scouting note.
