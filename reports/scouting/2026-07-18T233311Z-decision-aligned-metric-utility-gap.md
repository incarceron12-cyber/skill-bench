# Scouting note — decision-aligned metric/utility gap

- **Timestamp:** 2026-07-18T23:33:11Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv-HTML outbound-link discovery, official GitHub API metadata, web release search, and exact local duplicate searches only. The PDF/source body, proofs, experiments, datasets, code, configurations, or results were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Decision-Aligned Evaluation of Uncertainty Quantification** — Annika Schneider, Tommy Rochussen, Joshua Stiller, and Vincent Fortuin; arXiv:2606.26990v1 (submitted 2026-06-25).

- Immutable record/PDF/HTML/source: https://arxiv.org/abs/2606.26990v1 · https://arxiv.org/pdf/2606.26990v1 · https://arxiv.org/html/2606.26990v1 · https://export.arxiv.org/e-print/2606.26990v1
- At scouting time these endpoints returned HTTP 200 with observed response sizes of 42,331, 1,289,607, 1,188,000, and 580,314 bytes respectively.
- The abstract introduces a criterion for whether uncertainty-evaluation metrics align with downstream utilities, argues that common metrics can be misaligned or encode pathological prior beliefs, proposes prior-weighted utility metrics as proper scoring rules, and reports benchmark and real-world case studies. These are author-stated abstract claims awaiting full-paper verification.
- The immutable arXiv HTML links the official implementation https://github.com/fortuinlab/prior-weighted-utilities. GitHub API inspection found an MIT-licensed repository created 2026-01-25, last pushed 2026-06-24, with default branch `main`; the observed latest commit was `94ab70d6e88857b2b561390f017feb29a1716fac` (2026-06-24T11:26:41Z). No repository content or result was inspected during scouting.
- Exact title, arXiv ID, repository name, and `decision-alignment` searches found no local review or queue task. Existing LATTICE, criterion-validity, confidence-calibration, partial-decision, benchmark-to-risk, and consequence-validity work supplies explicit comparators, but does not reconstruct a formal metric-ordering-to-utility alignment criterion.

## Why this is a narrow, useful gap

The reusable chain is:

`declared prediction/uncertainty object → candidate metric and aggregation → utility family and prior over downstream decisions → metric-induced system ordering → decision-conditioned ordering agreement → stakeholder-authorized loss → observed use and decision → realized intended/adverse consequence → transport and non-regression`.

This directly advances charter objectives A–C and E and the research agenda's requirement that benchmark scores be decision-relevant. The paper may supply a formal bridge for one rung that the repository currently treats mainly as a claim boundary: whether a metric ranks systems consistently with a specified family of downstream utilities. It also presents a sharp ceiling. Mathematical alignment under an authored utility/prior family is not evidence that stakeholders endorse that loss, users adopt the score, decisions improve, consequences are beneficial, or the result transports to agentic knowledge work.

## Charter decision filter and queue action

- **Objectives advanced:** A (validity and scalable evaluation), B (metric-to-decision methodology), C (metric and sensitivity artifacts), and E (clear distinction between formal alignment and observed utility).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit and representative reconstruction of the official implementation.
- **Uncertainty clarified:** which assumptions license a decision-conditioned metric-ranking claim, and where utility elicitation, stakeholder authority, consequence observation, and transport remain separate.
- **Mode:** narrow expansion/human learning. The queue has three pending consolidation/build tasks and one human decision but no source/research/review item; this adds one low-priority review rather than repeating broad scouting.
- **Duplication/scope check:** exact searches were negative and adjacent reviews are comparators. UQ is a bounded measurement-method case, not a benchmark-domain commitment.
- **Useful completion:** reconstruct definitions, assumptions, empirical estimands, prior/utility sensitivity, release correspondence, and claim ceilings; reuse existing metric, validity, and decision-consequence machinery unless a demonstrated obligation is unrepresentable.

Added one task: `review-decision-aligned-uncertainty-metric-validity` (review, priority 41). No second task was queued. `Robo-Reporters` (arXiv:2607.10736v1) was triaged but deferred: its journalism architecture comparison is potentially relevant, but scouting found no paper-specific release and its abstract's one-run-per-task architecture contrasts, accuracy construct, and newsroom recommendations appear less direct than the newly isolated formal metric-to-utility gap.
