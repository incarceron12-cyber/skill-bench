# Scouting note — behavior-grounded hidden-requirement validity

**Timestamp:** 2026-07-14T22:41:16Z  
**Scope:** Narrow expansion against charter objectives A/B. At intake the queue had 232 tasks: 226 completed, four blocked, two pending human decisions, and no worker research/review task. Existing work covers underspecification, personal context, delegation demand, consent, and contextual integrity, but repository searches found no treatment of implicit requirements reconstructed from a user's behavior chain.

## Substantive finding (triage only)

**MapSatisfyBench: Benchmarking Satisfaction-Aware Map Agents through Behavior-Grounded Implicit Decision Factors**

- Immutable record: https://arxiv.org/abs/2606.17453v2
- Immutable PDF: https://arxiv.org/pdf/2606.17453v2
- Immutable HTML: https://arxiv.org/html/2606.17453v2
- The arXiv API identifies Lubin Bai, Mengyu Cao, Sixue Wang, Zhongwei Wan, Yue Pan, Jiale Hou, Xiang Li, and Xiuyuan Zhang; category `cs.AI`; v1 submitted 16 June 2026 and v2 updated 17 June 2026. The metadata summary contains no withdrawal notice. All three versioned arXiv URLs returned HTTP 200.
- The **v2 abstract** proposes a restore-identify-filter framework: reconstruct complete user needs from behavior-chain evidence, identify implicit decision factors, and retain factors only when they affect acceptance and are recoverable from information available before the query. It reports construction from large-scale anonymized real-world data, five ground-truth dimensions, full-chain evaluation, and a gap between explicit completion and satisfaction-aware evidence acquisition. These are author-reported abstract claims, not verified findings.
- Targeted searches found no clear official code or dataset surface. A full review must follow artifact links from the paper itself and explicitly record non-release if none exists.
- The distinctive validity question is whether historical behavior supports a **fair hidden consequence**. A later realized choice can reveal a plausible preference without proving current intent, authorization, causal satisfaction, or uniqueness. Reconstruction and filtering may introduce hindsight leakage, outcome-conditioned selection, annotator inference, privacy-induced construct changes, and false rejection of alternative acceptable choices.
- This is metadata, abstract, URL, and duplicate triage only. The PDF body, appendices, data, annotations, prompts, tasks, evidence views, trajectories, scores, results, statistics, and privacy process were not read or audited. No claim is made that MapSatisfyBench establishes satisfaction, personalization, professional validity, capability, privacy safety, or readiness.

## Benchmark implication to test

Behavior-derived hidden requirements need an authority-preserving chain: `versioned behavior event → observation/consent/privacy transform → reconstructed need → candidate implicit factor → pre-query evidence and availability → identifiability/alternative hypotheses → task projection → agent evidence access and adoption → action/options → acceptance and downstream consequence → bounded claim`. The key fairness test is not merely whether an oracle can infer a factor after seeing the behavior chain; it is whether the evaluated agent could legitimately identify the same factor from authorized pre-decision evidence, while preserving uncertainty and multiple acceptable actions.

A full audit should reconstruct one released item end to end if inspectable and compare the method with UnderSpecBench, HippoCamp, JobBench's delegation-demand ladder, SovereignPA-Bench, and contextual-integrity evidence. It should separate observed past preference, inferred present need, authorized use, recoverability, chosen action, acceptance, and realized satisfaction rather than collapse them into one label.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark mechanism) and B (hidden-requirement/evidence-to-evaluation methodology).
- **Evidence/artifact sought:** immutable-v2 deep review, release/non-release audit, and one behavior→factor→evidence→task→score reconstruction.
- **Uncertainty clarified:** whether behavior-grounded factors are fair, identifiable task requirements or hindsight-derived proxies for one historical choice.
- **Mode/balance:** one low-priority review task restores a minimal worker research backlog behind human and operational blockers; no broad search bundle was added.
- **Duplication/scope:** adjacent sources do not audit this reconstruction mechanism; maps are a bounded method case, not a proposal to narrow the benchmark.
- **Useful completion:** preserve temporal evidence boundaries, consent/authority, transformations, alternative hypotheses/actions, annotation reliability, filtering/selection, agent evidence access, outcome definitions, privacy effects, and strict claim ceilings.

Added `review-mapsatisfybench-behavior-grounded-hidden-requirements` (priority 16). The shared-workspace human–AI collaboration paper found in the same narrow search was not queued because HAS-Bench, DeskCraft, interaction-evidence conformance, and simulated-participant work already cover that boundary more directly.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 45 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.
