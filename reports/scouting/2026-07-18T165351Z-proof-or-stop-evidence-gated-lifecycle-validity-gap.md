# Scouting note — evidence-gated lifecycle validity gap

- **Timestamp:** 2026-07-18T16:53:51Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, targeted primary-source search, and exact repository duplicate/mechanism searches only. The PDF/source body, claimed open-source implementation, preregistration, 24-task ablation, 9,240 cells, mechanism/tamper fixtures, self-application corpus, or cross-vendor exhibit were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Proof-or-Stop: Don't Trust the Agent, Trust the Evidence — Loop Engineering for Verifiable Evidence-Gated Lifecycle Control** — Jek Huang, Jeffery Hsia, Jiayi Sun, Freddie Shi, Wei Huang, and Ian H. White; arXiv:2607.14890v1.

- Immutable record/PDF/source: https://arxiv.org/abs/2607.14890v1 · https://arxiv.org/pdf/2607.14890v1 · https://export.arxiv.org/e-print/2607.14890v1
- The arXiv API identifies a 16 July 2026 submission in `cs.AI` and `cs.SE`; its summary contains no withdrawal or retraction notice. Record, PDF, and source endpoints returned HTTP 200 in this check, with 44,282 HTML bytes, 1,079,574 PDF bytes, and 348,697 source bytes.
- The abstract presents lifecycle transitions such as reviewed, tested, done, and ready-to-merge as claims that require fresh, tracked-source-state-bound, mechanically verifiable evidence under an explicit trust model. It explicitly denies that gate-admissible evidence proves semantic program correctness.
- The abstract reports 10/10 unattended-loop scenarios with zero false-DONE; rejection of 18 receipt-tamper classes; a preregistered 9,240-cell control-policy ablation over 24 tasks; an A4-versus-A2-prime reduction in visible-pass/hidden-fail amplification from 31/1,800 to 2/1,800 injected cells; a near-compute A3-versus-A4 contrast of 14/1,800 versus 2/1,800; and self-application records covering 565 stories, 1,007 review findings, and a 68-row high/critical cross-vendor exhibit. These are author-stated claims awaiting full-paper and artifact verification.
- The abstract says the implementation is open source, but the arXiv metadata/abstract exposed no implementation URL and targeted web search did not establish an authoritative repository during this run. Locating the paper-linked release and determining whether the preregistration, raw cells, fixtures, corpus, and table builder are actually inspectable are part of the review—not evidence supplied by scouting.
- Exact title, arXiv-ID, `false-DONE`, `gate-admissible evidence`, receipt-tamper, and visible-pass/hidden-fail searches found no local review, queue task, or prior scouting note. Adversarial verifier hardening, task-health lifecycle, historical provenance boundaries, configured-system identity, and release reconstruction are adjacent; none audits this claimed evidence-to-lifecycle transition-control experiment.

## Why this is a narrow, useful gap

The reusable chain is:

`agent/reviewer lifecycle claim → source-state identity → typed evidence request → fresh observation/receipt → trust-model admissibility check → lifecycle gate decision → permitted transition or stop → later hidden/substantive consequence → tamper/replay audit → bounded control-policy claim`.

This directly advances charter objectives A, B, and C. The candidate could sharpen a core benchmark distinction: a model saying work is complete, a mechanical check admitting evidence, and the work being substantively correct are separate states. It may also supply an empirical comparison of merely adding a reviewer versus enforcing review as a transition gate.

The likely validity boundary is equally important. Passing co-designed gate scenarios does not establish gate completeness, and rejecting named tamper classes does not establish security under key compromise or semantic deception. Injected visible-pass/hidden-fail cells may validate sensitivity to the authored fault distribution without transporting to natural benchmark defects. Self-application is selected, endogenous evidence unless version history, eligibility, missingness, counterfactual policy, and table reconstruction are preserved. Coding is therefore a bounded mechanism case, not a benchmark scope commitment or a reason to optimize Hermes for its own sake.

A full review should reconstruct actors, states, predicates, evidence freshness and source bindings, receipt/key semantics, trust assumptions, hidden-failure generation, policy arms and compute parity, unit and clustering, confidence interval, invalid/missing cells, model/harness identity, preregistration correspondence, self-application selection, and release completeness. It should test stale evidence, source drift, replay, key compromise, path substitution, partial checks, coherent malicious artifacts, legitimate alternative evidence, reviewer dependence, and fail-closed invalidity where artifacts permit.

## Charter decision filter and queue action

- **Objectives advanced:** A (production evaluation and lifecycle-control frontier), B (claim→evidence→transition warrants), and C (provenance, gate, receipt, task-health, and release-validation machinery).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit and feasible mutation/replay of the claimed implementation and experimental artifacts.
- **Uncertainty clarified:** whether enforced evidence gates reduce false lifecycle promotion under a declared trust model, or mainly pass co-designed mechanical checks and selected injected failures.
- **Mode:** narrow expansion. The queue had one autonomous review, one prerequisite review, one downstream build, and one human-decision task after recent consolidation; one distinct review restores a small research buffer without broad benchmark collecting.
- **Duplication/scope check:** exact and mechanism searches were negative. Existing work supplies adjacent contracts but not this control-policy experiment. Reuse existing configured-system, provenance-boundary, task-health, grader, evidence-chain, metric, release, and validity machinery; add no coding-specific subsystem absent evidence.
- **Useful completion:** reproduce the claim-to-gate design and reported comparisons from source-located evidence where possible, audit soundness and completeness against adversarial and valid-alternative mutations, and preserve semantic-correctness, professional-validity, reliability, production-fitness, and readiness claim ceilings.

Added one task: `review-proof-or-stop-evidence-gated-lifecycle-validity` (review, priority 52). No second source was queued. SearchOS-V1 was not reconsidered because prior scouting explicitly deferred it as overlapping existing search-state work unless release inspection revealed distinct evidence.
