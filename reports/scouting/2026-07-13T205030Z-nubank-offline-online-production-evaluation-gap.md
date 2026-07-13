# Scouting note — offline-to-online production-agent evaluation gap

**Timestamp:** 2026-07-13T20:50:30Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 187 tasks: 183 completed, two blocked, and two pending (one prerequisite-ordered consolidation and one build), with no pending source/research/review work. The reviewed corpus covers production evaluation guidance, configured-system identity, task health, rubric/judge reliability, and benchmark-to-consequence warrants, but not a primary production report linking an offline simulation/evaluation pipeline to randomized online outcomes across multiple live agent deployments.

## Substantive finding (triage only)

**Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework**

- Immutable arXiv record: https://arxiv.org/abs/2606.08867v2
- Immutable PDF: https://arxiv.org/pdf/2606.08867v2
- Immutable HTML: https://arxiv.org/html/2606.08867v2
- The arXiv API identifies Aman Gupta, Kevin Rossell, Edesio Alcobaça, Jose Chrystian Lima Pacheco, Carolina Baptista de Lima, Shao Tang, Luiz Paulo Rabachini, Luis Moneda, Herbert Fei, Daniel Silva, and Rohan Ramanath. v1 was submitted 7 June 2026; the current v2 was posted 13 June 2026 in `cs.CL`.
- The abstract presents a Nubank framework joining structured context engineering, human-in-the-loop prompt iteration, LLM-judge evaluation with measured inter-rater agreement and GEPA optimization, offline simulation, and online validation. It reports five production deployments spanning card delivery, debt management, credit-limit support, card management, and product explanation.
- For card delivery, the abstract reports a 37-percentage-point improvement in AI transactional Net Promoter Score and a 29-point gain in self-service rate over prior agent variants, plus a strong offline/online correlation. It also states that satisfaction in most use cases approaches expert-human-agent levels. These are discovery leads only: deployment and analysis units, assignment, denominators, duration, uncertainty, metric definitions, configured-system changes, selection, repeated-user dependence, comparison construction, safety/escalation, and generalizability require full-paper verification.
- The immutable abstract, PDF, and HTML URLs all returned HTTP 200 during discovery. Targeted title/ID searches did not identify a paper-specific author-owned artifact release; the full paper and author/project searches must establish whether prompts, simulation cases, annotations, judge configurations, or result records are inspectable. The GEPA repository is adjacent implementation evidence, not automatically this study's release.
- Repository-wide duplicate search found neither the title nor arXiv ID. Existing Anthropic and Amazon production notes provide engineering guidance; AgentRewardBench and RuVerBench examine offline judge behavior; the benchmark-to-risk review models consequence warrants. None currently audits a five-deployment offline-to-online evidence chain with live randomized outcomes.
- This is **metadata/abstract and URL triage only**. The paper, appendices, deployment records, prompts, simulations, annotations, experiments, judge optimization, and result artifacts were not fully read or audited. No claim is made that the reported effects are causal beyond their specific experiments, that offline scores generally predict online impact, that near-human satisfaction implies professional equivalence, or that the agents are safe or production-ready in other settings.

## Benchmark implication to test

Production-validity evidence should preserve a chain from offline task/sample provenance through configured-system and evaluator versions to intervention selection, online assignment, exposure, customer/workflow outcome, uncertainty, and deployment decision. A high offline/online correlation can otherwise mix scenario selection, repeated iteration, shared metrics, treatment-bundle changes, and post-selection reporting. This source may provide unusually direct evidence about which offline evaluation signals survive contact with live outcomes and where human annotation and judge optimization accelerate or distort iteration. A full audit should test the exact unit and independence of the claimed association, distinguish held-out prediction from retrospective fit, and map reusable obligations into existing configured-system, task-health, metric-monitoring, validity, participation, and grader machinery rather than create a customer-support subsystem.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier production-agent evaluation), B (evidence from benchmark observation to consequential use), and C (scalable grader, task-health, and configured-system machinery).
- **Evidence/artifact sought:** immutable full-paper review plus any pinned author-owned supplemental artifacts, reconstructing offline instruments, human labels, judge optimization, five deployment studies, online metrics, uncertainty, safety/escalation, and release limits.
- **Uncertainty clarified:** whether and under what bounded conditions offline simulations and optimized judges predict live customer/workflow outcomes, versus reflecting selection, metric, iteration, or treatment-bundle confounds.
- **Mode/balance:** narrow expansion into an empty review backlog; existing consolidation/build work remains higher priority.
- **Duplication/scope:** nonduplicate offline-to-online validity question; customer support and the five named workflows are a bounded production case, not a benchmark-domain commitment.
- **Useful completion:** verify every headline denominator/effect and the correlation unit from full text; separate framework advice from empirical support; audit assignment, missingness, dependence, judge holdouts, safety, configured-system deltas, and reproducibility; compare existing production/judge evidence; retain strict causal-generalization, professional-equivalence, safety, readiness, and cross-domain claim ceilings.

Added `review-nubank-production-evaluation-online-validity` (priority 45). No second task was added.
