# Scouting note — evaluator-coupling / reliability validity gap

- **Timestamp:** 2026-07-18T04:36:05Z
- **Evidence status:** arXiv API metadata/abstract, immutable URL checks, arXiv HTML heading/link inspection, targeted web discovery, and exact repository duplicate searches only. The PDF body, appendices, source archive, upstream dataset, metric implementation, or per-seed records were **not** deeply read, downloaded, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Mapping the Evaluation Frontier: An Empirical Survey of the Bias-Reliability Tradeoff Across Eleven Evaluator–Agent Conditions** — Zewen Liu; arXiv:2607.00304v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.00304v1 · https://arxiv.org/pdf/2607.00304v1 · https://arxiv.org/html/2607.00304v1
- The arXiv API reports v1 submitted and last updated 1 July 2026 in `cs.LG`, `cs.AI`, and `cs.CL`; its summary contains no withdrawal or retraction notice. URL checks returned HTTP 200 for the immutable record and PDF; the PDF response reported 415,302 bytes.
- The abstract defines an evaluator–agent design space using evaluator coupling (`γ`), strategy diversity/entropy (`H`), and small-sample reliability expressed as `CV(N)`. It reports 11 conditions, but valid weight vectors for nine, at least five seeds for seven, and a complete three-metric tuple for only five. It further reports a five-condition entropy–coupling correlation after excluding GPT-4o conditions and attributes four degenerate GPT-4o conditions to June 2026 API version drift. These are author-stated abstract claims awaiting full-paper verification.
- Structural HTML inspection exposed Methods sections for data source/metric computation and a GPT-4o caveat, followed by condition survey, empirical frontier, entropy gradient, discussion, broader-impact, and reproducibility sections. The paper says it releases standardized per-condition metrics, but no paper-specific repository or dataset link was exposed in the HTML external links or targeted exact-title/arXiv-ID web searches. This is a time-bounded scouting observation, not proof that no release exists.
- Exact ID/title/signature-phrase searches found no local review, task, or scouting note. Existing reviews discuss evaluator coupling as a validity threat and separately cover grader reliability, rater effects, strategy/equivalence diversity, small-sample agent reliability, intervention–instrument confounding, and version drift; none audits this proposed joint frontier or its estimands.

## Why this is a narrow, useful gap

The relevant chain is:

`task and legitimate solution/strategy space → configured agent/evaluator identities → strategy representation and weight-vector estimator → evaluator–strategy dependence/coupling estimator → repeated-seed score distribution → reliability estimand and sample-size policy → admissible comparison/selection decision → transport under evaluator or API revision`.

This could sharpen a central `skill-bench` tension: a tightly coupled executable or reference-derived evaluator may be stable yet suppress legitimate alternatives, while a plural or weakly coupled observer may admit more strategies but yield noisier finite-sample decisions. The useful object is not a universal scalar frontier but a typed validity audit linking alternative-path acceptance, evaluator dependence, repeat allocation, missing metrics, and version identity.

The abstract also signals severe threats that make a full audit more valuable than direct adoption: only five complete tuples; correlation after condition exclusion; likely non-independent conditions from one upstream dataset; unclear strategy ontology and weight-vector validity; `CV` instability when the mean is near zero; potentially co-derived `γ` and `H`; post-hoc attribution of degenerate conditions to mutable API drift; and no discovered release despite a release claim. A missing point in a small observed region cannot by itself establish an impossibility tradeoff. The review must separate empirical description, metric validity, selection/missingness, version failure, and general evaluation-law claims.

This is a cross-domain evaluator-design mechanism, not a proposal to narrow `skill-bench` to one benchmark family or adopt one metric trio.

## Charter decision filter and queue action

- **Objectives advanced:** A (grader, reliability, and benchmark-validity research), B (separating intervention, instrument, legitimate strategy space, and claim), and D/E (cross-source consolidation and decision-relevant learning).
- **Concrete evidence:** immutable-v1 full-paper/source audit, exact metric and dataset reconstruction, condition/missingness/version ledger, reproducibility check if artifacts can be found, and retain/repair/test implications grounded by page/file locators.
- **Uncertainty clarified:** whether the reported frontier is a meaningful property of evaluator design or an artifact of strategy representation, estimator dependence, sparse/missing conditions, near-zero means, model/API drift, and one inherited dataset.
- **Mode:** narrow expansion. The autonomous queue contains one consolidation task and no source/research/review task; one bounded audit restores evidence flow without restarting broad searches.
- **Duplication/scope check:** adjacent reviews cover components but not this joint empirical claim. Existing grader, metric, configured-system, alternative-path, reliability, task-health, and validity machinery should host any implications; add no frontier-specific schema or pilot absent stronger evidence.
- **Useful completion:** reproduce or decisively bound every reported tuple/correlation where artifacts permit; distinguish stability from validity and strategy diversity from correctness; preserve exclusions and version identity; state the strongest licensed claim and blocked universal-law, capability, professional-validity, and readiness claims.

Added one task: `review-evaluator-coupling-reliability-frontier-validity` (review, priority 55). No second source was queued.
