# Scouting note — intervention-timing construct reliability gap

**Timestamp:** 2026-07-15T08:34:28Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 258 tasks: 251 completed, four blocked, two pending human decisions, and one pending cross-domain attribution build. The recent corpus covers expert disagreement, configurable human participation, confidence-based selective review, feedback interventions, and intervention-to-root attribution, but not whether humans can reproducibly identify *when* and *how* an agent should be interrupted.

## Substantive finding — triage only

**The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents** — Manvendra Modgil; arXiv:2606.04296v1.

- Immutable record: https://arxiv.org/abs/2606.04296v1
- Immutable PDF: https://arxiv.org/pdf/2606.04296v1
- Official repository: https://github.com/2025eb1100268-tech/intervention-timing-saturation-trap
- The arXiv API identifies immutable v1, submitted 2 June 2026 in `cs.AI`; its summary contains no withdrawal notice. The versioned abstract and PDF endpoints returned HTTP 200 during scouting.
- The abstract describes four intervention-trigger families—absolute state thresholds, composite state/action patterns, regex reasoning-feature extraction, and zero-shot LLM judging—on five SWE-bench-Verified debugging trajectories. It reports threshold saturation that fires on 39–83% of actions, strong model/context/cost dependence for LLM judges, and a three-annotator overlap study on one 56-action trajectory.
- The author-reported human reliability is near zero for intervention location (Krippendorff's alpha `+0.047`; best pairwise Cohen's kappa `+0.349`) and weak or degenerate for intervention type. These are abstract claims, not independently verified results. The tiny trajectory and overlap samples may support a sharp falsification of one labeling protocol while remaining insufficient for prevalence, universality, or policy recommendations.
- GitHub verification found the linked repository public, live, unarchived, and MIT-licensed. Mutable `main` resolved to `55c8bd26f5303807c7f134df24275b9de9fca187`, last pushed 15 June 2026. A reviewer must pin that commit and audit released labels, scripts, traces, configurations, and paper–release correspondence.
- Repository-wide exact title/ID and concept searches found no duplicate. The closest local reviews concern irreducible expert disagreement, configurable participation, confidence calibration, feedback interventions, and causal attribution; none audits the temporal-location and intervention-type reliability of a human-supervision trigger.
- This is **metadata, abstract, endpoint, repository-metadata, and duplicate triage only**. The paper and release were not read or executed during scouting. No claim is made about annotation correctness, detector accuracy, affect-model validity, trajectory representativeness, general agent behavior, downstream utility, safety, professional validity, production fitness, or readiness.

## Why this is distinct

An intervention score presupposes an identifiable target. If qualified reviewers disagree about the event location or intervention type, detector F1 against a single label can reward one annotator's policy rather than a stable property of the trajectory. This differs from asking whether human assistance was available, whether a confidence score predicts failure, or whether an injected fault caused an outcome.

The reusable chain for `skill-bench` is `trajectory and observer view → candidate intervention opportunity → reviewer policy/authority → acceptable event window and action set → intervention execution → counterfactual artifact/state consequence → burden and decision loss`. Timing, intervention type, downstream utility, and stakeholder loss are distinct estimands. A full audit could determine whether event windows, risk states, policy sets, deferral regions, or consequence-based comparisons are better posed than one exact action-index label for realistic knowledge work.

## Charter decision filter and queue action

- **Objectives advanced:** A (human/agent evaluation frontier), B (valid conversion of judgment into criteria), and C (intervention and selective-review measurement).
- **Concrete evidence/artifact:** immutable-v1 full-paper review plus commit-pinned official-release audit.
- **Uncertainty clarified:** whether intervention timing/type is reproducibly measurable under the paper's protocol, which failure is target unreliability versus detector failure, and what claim survives the small clustered sample.
- **Mode:** narrow expansion feeding consolidation/validation; no coding, affect-model, or autonomous-agent scope commitment.
- **Duplication/scope:** no local duplicate; adjacent disagreement, participation, confidence, feedback, and attribution sources are required comparators.
- **Useful completion:** reconstruct samples, labels, assignment, trigger semantics, metrics, uncertainty, costs, and release fidelity; compare alternative estimands; preserve strict claim ceilings; propose no new machinery unless a non-overlapping implementation gap remains.

Added one task: `review-intervention-timing-construct-reliability` (priority 14). No additional source was queued because the existing attribution build and human prerequisites remain higher priority.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Pre-existing untracked paper source trees and the AgentFootprint release ZIP were not modified.
