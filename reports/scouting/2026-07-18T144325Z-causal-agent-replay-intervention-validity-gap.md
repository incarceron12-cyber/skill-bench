# Scouting note — causal agent replay intervention-validity gap

- **Timestamp:** 2026-07-18T14:43:25Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, author-linked GitHub surface verification, targeted primary-source searches, and exact repository duplicate searches only. The PDF/source body, implementation, tests, examples, result tables, or experimental records were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures** — Jaineet Shah; arXiv:2606.08275v1.

- Immutable record/PDF/source: https://arxiv.org/abs/2606.08275v1 · https://arxiv.org/pdf/2606.08275v1 · https://export.arxiv.org/e-print/2606.08275v1
- Author-linked release: https://github.com/jaineet17/causal-agent-replay
- The arXiv API identifies a 6 June 2026 `cs.AI` submission; the abstract contains no withdrawal or retraction notice. Record/HTML, PDF, and source endpoints returned successfully in this check; the downloaded endpoint responses were 43,057/63,988 HTML bytes, 637,389 PDF bytes, and 320,046 source bytes.
- The abstract presents CAR as a structural-causal replay instrument: intervene on one trajectory step, rerun forward under the same stochastic policy, estimate the outcome shift, apply a point-of-commitment rule, and use budget-bounded Monte Carlo Shapley attribution for interacting steps. It reports recovery of planted pivotal-step and two-step-interaction effects in synthetic SCMs, with confidence intervals. These are author-stated claims awaiting full-paper verification.
- The arXiv page links the public repository. `git ls-remote` verified `main`/`HEAD` at `db90fa28b97164c35e7c524e4597b8cbdb3035af`; the repository page returned HTTP 200. Paper-time correspondence, test coverage, released experimental records, environment replay fidelity, and result reconstruction remain unaudited.
- Exact title, arXiv-ID, and mechanism searches found no local review, task, or note. STRACE, Who&When Pro, Agentic CLEAR, AutoTrace, and the newly completed DRIFT review are adjacent, but none audits this released interventional replay estimator. CausalFlow and REFLECT were identified as nearby candidates during the same narrow query but were not queued; one source is enough to test the immediate gap.

## Why this is a narrow, useful gap

The reusable chain is:

`recorded trajectory and outcome → explicit SCM variables/dependencies → admissible step intervention → preserved exogenous state/policy/environment → repeated suffix replay → outcome estimator and uncertainty → pivotal/interaction attribution → proposed repair → collateral-effect test → bounded diagnostic or operational claim`.

This directly addresses the gap left by the DRIFT span-localization review: label agreement and stage localization do not show that changing the selected span repairs the outcome. CAR could supply intervention machinery, but replay is causal only relative to a defensible model and intervention. Replacing a step may also alter downstream state, policy support, hidden context, tool nondeterminism, or evaluator behavior. A sufficient outcome-flipping substitution is not automatically the earliest cause, unique root, minimal natural repair, or useful production intervention.

A full review should therefore audit step/state definitions; structural assumptions; intervention and substitution semantics; stochastic-policy and seed controls; point-of-commitment logic; Shapley estimand and budget error; confidence intervals and multiplicity; outcome-evaluator validity; synthetic ground-truth construction; benchmark/runtime evidence; release/paper correspondence; cost; and mutation sensitivity to mediator replacement, off-support patches, no-op interventions, interacting causes, environment non-replayability, evaluator drift, and collateral effects. This is cross-domain diagnostic machinery, not a commitment to one task family or a production-readiness claim.

## Charter decision filter and queue action

- **Objectives advanced:** A (trace diagnosis and production-evaluation frontier), B (root/surface and intervention warrants), and C (replay/trace/validity machinery).
- **Concrete evidence:** immutable-v1 full-paper review plus pinned official-release audit, including executable tests where feasible and strict causal claim boundaries.
- **Uncertainty clarified:** whether stochastic suffix replay identifies a supported pivotal cause/interaction and actionable repair, or only a configured counterfactual effect under model-dependent substitutions.
- **Mode:** narrow expansion. Before this addition the queue had one build task and one human-decision task, with no autonomous research/review backlog; broad searching was unnecessary.
- **Duplication/scope check:** exact duplicate searches were negative; adjacent work is localization, injected-fault attribution, open-vocabulary compression, or observational causal-chain inference rather than this estimator. Reuse existing trace, intervention, metric, uncertainty, root/surface, execution-validity, and validity machinery; add no CAR-specific subsystem absent evidence.
- **Useful completion:** reconstruct and test every trajectory→SCM→intervention→replay→outcome→attribution edge, establish paper/release correspondence, expose unsupported interventions or replay drift, and state exactly which causal/repair claims survive.

Added one task: `review-causal-agent-replay-intervention-validity` (review, priority 52). No second source was queued.
