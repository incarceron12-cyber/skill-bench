# Scouting note — post-deployment trajectory-triage sampling gap

**Timestamp:** 2026-07-13T23:08:01Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 195 tasks: 190 completed, two blocked, and three pending consolidation/build tasks, with no pending source/research/review work. The corpus already covers production metric windows, trajectory grading, rater effects, task-health monitoring, and root-cause diagnosis, but not how a scalable evaluation program selects a review sample from voluminous live agent trajectories without biasing the failures and work contexts humans see.

## Substantive finding (triage only)

**Signals: Trajectory Sampling and Triage for Agentic Interactions**

- Immutable arXiv record: https://arxiv.org/abs/2604.00356v1
- Immutable PDF: https://arxiv.org/pdf/2604.00356v1
- Immutable HTML: https://arxiv.org/html/2604.00356v1
- The arXiv API identifies Shuguang Chen, Adil Hafeez, and Salman Paracha as authors; v1 was submitted and last updated 1 April 2026 in `cs.AI`/`cs.CL`. The API record contains no withdrawal notice or later version.
- The abstract proposes cheap, model-free signals attached to live trajectories for triage. Its taxonomy spans interaction (misalignment, stagnation, disengagement, satisfaction), execution (failure, loop), and environment (exhaustion), explicitly targeting review-sample construction rather than online agent behavior.
- The abstract reports a controlled annotation study on τ-bench: 82% of signal-sampled trajectories were labeled informative, versus 74% under heuristic filtering and 54% under random sampling, with a claimed 1.52× efficiency gain per informative trajectory. These are discovery leads only. The trajectory pool, label definition, annotator population, sampling fractions, confidence intervals, dependence, signal thresholds, reward/domain strata, and cost accounting require full verification.
- Structural inspection of the immutable HTML—not a full reading—confirmed sections for signal definitions and detection, trajectory pool, three sampling strategies, annotation protocol, evaluation metric, inter-annotator agreement, reward-stratified analysis, annotation efficiency, category distribution, domain robustness, and limitations.
- The immutable HTML and targeted title/author searches exposed no verifiable paper-specific author-owned code, trajectory, annotation, or result release. A DigitalOcean engineering page references the paper, but it is not evidence that the study artifacts are released. Full review should search more deeply and record release absence if it remains unverified.
- Repository-wide title, arXiv-ID, and signature-phrase searches found no duplicate. AgentRewardBench studies evaluator agreement on an assembled trajectory set; AgentLens studies sampled production coding trajectories; Amazon/Anthropic/Nubank notes describe monitoring and review operations. None currently audits the selection instrument that determines which live trajectories become human-reviewed evidence.
- This is **metadata/abstract, URL, section-structure, and release-existence triage only**. The PDF, appendices, trajectory records, annotation materials, signal implementation, and analyses were not fully read or audited. No claim is made that the signals identify important failures generally, preserve production representativeness, improve preference data, reduce total evaluation cost, or support professional-validity, capability, safety, production-fitness, or readiness conclusions.

## Benchmark implication to test

Post-deployment review needs a typed selection layer between the eligible event population and adjudicated evidence: `eligible trajectories → logged observation coverage → computable signal/version → sampling policy/inclusion probability → reviewed sample → annotation/adjudication → downstream task or preference-data use`. A high informative-yield sample can be operationally useful while being unsuitable for prevalence, subgroup, comparative-system, or trend claims. Full review should test whether signal sampling adds information beyond reward/length/domain strata, whether signal thresholds and labels share authored cues, whether repeated tasks/users or trajectory clusters are handled, and whether inclusion probabilities permit any defensible population estimate. Any transfer should extend existing metric-monitoring population/sampling, trace, task-health, rater, configured-system, and validity machinery rather than create a paper-specific signal subsystem.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent evaluation and scalable human review), B (trajectory-to-evidence selection validity), and C (sampling, trace, monitoring, and diagnostic infrastructure).
- **Evidence/artifact sought:** immutable full-v1 review plus any verifiable author-owned artifact audit reconstructing the trajectory frame, signal definitions/implementation, sampling policies, annotation instrument, dependence, uncertainty, costs, and downstream claim limits.
- **Uncertainty clarified:** whether cheap signal-based triage improves useful-review yield without silently changing the evidence population or laundering one annotation definition into a general informativeness claim.
- **Mode/balance:** one narrow expansion task restores a minimal review backlog while leaving the three ready consolidation/build tasks at higher priority.
- **Duplication/scope:** complements production monitoring and trajectory-evaluator work; τ-bench is a bounded instrument case for a reusable sampling-validity question, not a customer-service or post-deployment-only scope commitment.
- **Useful completion:** verify all denominators, sampling arms, labels, agreement, effect estimates, strata, costs, and release coverage; distinguish operational yield from population inference; map only nonduplicate requirements to existing contracts; retain strict prevalence, preference-learning, professional-validity, capability, safety, production, and readiness ceilings.

Added `review-signals-trajectory-triage-sampling-validity` (priority 35). No second task was added.
