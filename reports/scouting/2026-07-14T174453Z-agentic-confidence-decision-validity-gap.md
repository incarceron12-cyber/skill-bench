# Scouting note — trajectory-confidence decision-validity gap

**Timestamp:** 2026-07-14T17:44:53Z  
**Scope:** Narrow expansion against charter objectives A/B/D/E. Queue inspection found 215 tasks: 211 completed, two blocked, one pending build, and one pending human decision; no source/research/review task remained. Existing reviews cover repeated reliability, trace-based root-cause diagnosis, signal-enriched review sampling, and rater calibration, but not whether an agent-trajectory confidence estimate validly supports abstention, escalation, or review allocation.

## Substantive finding (triage only)

**Agentic Confidence Calibration**

- Immutable arXiv record: https://arxiv.org/abs/2601.15778v1
- Immutable PDF: https://arxiv.org/pdf/2601.15778v1
- Immutable HTML: https://arxiv.org/html/2601.15778v1
- Accepted ICML 2026 record: https://openreview.net/forum?id=B1ISNZQHuI
- ICML poster page: https://icml.cc/virtual/2026/poster/65705
- The arXiv API identifies Jiaxin Zhang, Caiming Xiong, and Chien-Sheng Wu as authors; v1 was submitted 22 January 2026 in `cs.AI` and `cs.CL`, with no later arXiv version or withdrawal notice. The versioned abstract, PDF, HTML, accepted OpenReview record, and ICML poster URLs all returned HTTP 200 during this run.
- The **v1 abstract** introduces Holistic Trajectory Calibration (HTC), which derives process-level features across an agent trajectory and applies an interpretable calibrator. It reports better calibration and discrimination than baselines across eight benchmarks, multiple models, and agent frameworks, plus an out-of-domain GAIA result for a pooled General Agent Calibrator. These are author-reported abstract claims, not independently verified findings.
- Search-visible paper metadata describes a 48-dimensional feature set and highlights early-step entropy, confidence gradients, and stability dynamics. Full review must establish which confidence/log-probability observations actually exist for each configured agent, how heterogeneous traces are aligned, whether features are available before the decision they purport to support, and whether feature coefficients diagnose causes or merely predict labels.
- This fills a distinct gap. STRACE localizes supported upstream causes after failures; Agent Reliability Profile measures repeated outcomes; Signals prioritizes trajectories for human review; Many-Facet Rater Effects separates rater and task variation. HTC instead proposes a prospective confidence signal. A lower ECE or higher discrimination score does not by itself show that abstention, escalation, human-review allocation, or autonomous action improves stakeholder outcomes.
- The ICLR OpenReview search result corresponds to an earlier desk-rejected submission, while the separate current ICML record and poster page indicate acceptance. The review must preserve venue/revision identity and inspect both review histories without treating venue status as methodological validation.
- Narrow author/repository searches found no verified official code or data release. Full review should inspect the paper, appendices, accepted OpenReview revisions/rebuttals, author pages, and any linked artifacts before deciding inspectability or reproducibility.
- Repository-wide searches found no existing review or queue task for arXiv `2601.15778`, the title, or HTC.
- This is **metadata, abstract, venue, URL, release-location, and duplicate triage only**. The PDF, appendices, benchmark rows, trajectories, feature code, split manifests, calibrators, labels, result tables, reviews, and any released artifacts were not fully read or audited. No claim is made that HTC is calibrated under knowledge-work shift, identifies root causes, transfers universally, improves human-agent decisions, or supports professional validity, safety, production fitness, or readiness.

## Benchmark implication to test

Confidence needs a typed decision chain: `configured system and task population → immutable trajectory observation available by decision time → confidence feature transformation → calibration population/split → predicted event and time horizon → calibration/discrimination evidence → action policy and threshold → abstention/escalation/review allocation → human burden and delay → corrected or prevented consequence → stakeholder loss`. The predicted event must be explicit: final benchmark pass, criterion failure, unsafe action, invalid environment, or another outcome are not interchangeable.

Full review should test task/trajectory clustering, repeated-run identity, shared-model dependence, class balance, success-oracle validity, post-outcome leakage, log-probability comparability, binning and small-sample sensitivity, held-out-domain selection, pooling weights, threshold transport, covariate shift, selective-risk curves, and decision-cost assumptions. Feature attribution must remain separate from causal root diagnosis. Transfer should reuse configured-system, trace, task-health, reliability, metric-monitoring, rater, participation, and validity machinery rather than creating a calibration-specific schema.

## Charter decision filter and queue action

- **Objectives advanced:** A (production/agent-evaluation frontier), B (measurement-to-decision validity), D (comparative synthesis), and E (clarifying calibration versus utility).
- **Evidence/artifact sought:** immutable-v1/ICML-grounded full review reconstructing benchmark populations, configurations, trajectory observations, labels, features, splits, metrics, uncertainty, transfer, and released evidence.
- **Uncertainty clarified:** whether HTC provides bounded prediction of configured-system task outcomes or supports stronger diagnosis, cross-domain transfer, escalation, and reliability claims.
- **Mode/balance:** one low-priority review task restores a minimal research backlog while leaving the pending interaction build and human decision ahead of it.
- **Duplication/scope:** complements reliability, root-cause, review-sampling, and rater work; calibration is a reusable evaluation layer, not a new benchmark scope.
- **Useful completion:** separate calibration, discrimination, feature attribution, transfer, and policy utility; quantify threshold/loss and burden where evidence permits; preserve strict causal, professional, safety, production, and readiness ceilings.

Added `review-agentic-confidence-calibration-validity` (priority 22). No second task was added.

## Operational note

The required initial `git pull --ff-only` could not authenticate to the HTTPS GitHub remote (`could not read Username`). The run proceeded from local `main`; the pre-existing untracked `data/papers/source/` tree was not modified.
