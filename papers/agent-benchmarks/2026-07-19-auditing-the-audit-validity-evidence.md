# Paper Review: Auditing second-order benchmark-validity evidence

- **Paper:** <https://arxiv.org/abs/2607.02586v1>
- **Title:** *Auditing the Audit: Five Failure Modes in Benchmark-Validity Audits*
- **Authors:** Yanhang Li, Zhichao Fan, and Zexin Zhuang
- **Date read:** 2026-07-19
- **Version read:** immutable arXiv v1, submitted 1 July 2026
- **Local PDF:** `data/papers/pdfs/2607.02586v1-auditing-the-audit-validity-audits.pdf` (18 pages; SHA-256 `3720ae50379fe84cdbafe9e2014e8140a811ef0dbbc33cda6c93d4e2fc67898d`)
- **Local text:** `data/papers/text/2607.02586v1-auditing-the-audit-validity-audits.txt` (SHA-256 `134ec2f86fdbaa7aaacfed56a9363e4a948038577c6233f4caa164763b1c0170`)
- **TeX source:** `data/papers/source/2607.02586v1-auditing-the-audit-validity-audits.tar.gz` (23 members; SHA-256 `ef5afddb7852f30eb4626b5e540b36c977daea7c3a6799dd6e887dcfcea1af39`)
- **Implementation/data status:** unavailable in v1. Appendix K says the bundle and URL are withheld for blind review. Exact-title, arXiv-ID, author, and GitHub searches on 19 July did not identify an author-verified release. No unofficial implementation was substituted.
- **Tags:** validity-audit, assurance, perturbations, scorer-faithfulness, repair-regression, missingness, claim-withholding

## One-sentence contribution

The paper usefully treats a benchmark-validity audit as a **second-order measurement instrument** and gives five concrete ways its implementation can manufacture plausible evidence plus a typed withholding gate, but its public v1 cannot itself pass the strongest form of that due diligence: code, per-item outputs, preregistration, verdict CSV, chronology, and regression tests are absent; perturbation semantics and scorer validity remain partly unvalidated; and zero confirmatory cells follow mechanically because two gates are only proposed, not because the gate has demonstrated discriminative assurance value.

## Why this matters for skill-bench

`skill-bench` now relies on release audits, mutation tests, reconstruction scripts, schema validators, pilot reports, and independent reviews. Those artifacts can look rigorous while silently observing the wrong representation, dropping inconvenient rows, reversing a convention, comparing non-equivalent implementations, or inheriting a stale result after repair. The reusable object is therefore not this paper's safety-benchmark panel. It is the second-order chain:

```text
bounded audit claim
→ immutable target and reference identities
→ audit implementation and observation-path identities
→ independently admissible perturbation or contrast
→ attempted / observed / parsed / paired / eligible denominators
→ correctly oriented and dependence-aware estimand
→ defect chronology and repair lineage
→ clean and adversarial regression evidence
→ typed confirmatory / exploratory / ineligible / withheld disposition
→ bounded downstream use
```

This advances charter objectives A–C without narrowing the benchmark to safety. It adds a needed warning to artifact-heavy knowledge-work evaluation: a deterministic audit can be perfectly reproducible and still faithfully reproduce the wrong projection.

## Research question and claim boundary

The paper asks a prior question to ordinary construct validation: before perturbation evidence is used to assess a benchmark, is the pipeline producing that evidence trustworthy? It limits itself to failures that are silent in headline numbers, actually encountered in the authors' pipeline, and expressible as checkable disclosure gates (C1–C3; Section 2, pp. 2–3). It explicitly describes F1–F5 as illustrative and overlapping, the two-model/five-benchmark study as one exploratory case, and G1–G6 as a withholding/disclosure protocol rather than a validity standard or benchmark verdict (Abstract and Sections 1–2, pp. 1–3).

### Supported by the full paper

1. The paper describes a coherent taxonomy of observation-path, parsing, scorer, uncertainty, and interpretation failures, including one repair-introduced failure (Sections 2 and 4, pp. 2–7).
2. It reports a ten-cell canonical panel with full displayed cell-level summary statistics and typed dispositions: 3 ineligible, 3 scorer-unvalidated, 2 failed G2–G4, 2 exploratory, and 0 confirmatory (Table 3, p. 7; Table 6, p. 15).
3. It distinguishes benchmark reference scoring, the audit scorer actually used, and validation evidence for that scorer (Appendix D, pp. 12–13).
4. It discloses engineering thresholds, a small sensitivity grid, preregistration deviations, a dropped model, an abandoned human audit, and several unfixed issues (Appendices A, E, J, and K, pp. 12–18).
5. The displayed rounded deltas reproduce the reported CSR values approximately, and the displayed status rows reproduce the 3/3/2/2/0 bucket counts. Differences such as displayed Mistral–XSTest `0.990 / 0.012 = 82.5` versus reported CSR `84.86` are compatible with the paper's statement that decisions use unrounded values; raw precision is unavailable.

### Not established

The paper does not establish that the five classes are prevalent or complete; that all were realized exactly as described in executable code; that the perturbations preserve surface meaning or flip the intended construct; that the gate catches unknown failures; that its thresholds optimize any consumer loss; that first-match status precedence leads to better audit decisions; that a cell passing all six gates supplies construct-validity evidence; or that the method improves governance, procurement, professional evaluation, production assurance, or readiness. It issues no benchmark-validity verdict, and neither should `skill-bench` infer one.

## Methodology and system

### Panel, perturbations, and estimand

The canonical case is Qwen-2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 crossed with TruthfulQA, BBQ, ToxiGen, CrowS-Pairs, and XSTest: ten cells, 200 items per benchmark, deterministic decoding, seed 42, one template, and three perturbations in each of three families per item (Section 3, p. 4). Format edits include case, punctuation, label format, choice order, and—in text classification—an instruction prepend. Semantic edits use templates, synonyms, and rule-based restructuring. Attribute edits are benchmark-specific opposite-stem, demographic, toxicity, or safe/unsafe substitutions (Appendix C, p. 12).

For each family, the pipeline averages absolute per-item score changes over three perturbations and 200 items. It then computes:

```text
CSR = |Δattribute| / max(|Δformat|, |Δsemantic|, 0.01)
```

A paired 1,000-resample item bootstrap carries the item's perturbations together. CSR is deliberately unsigned: a high value says only that attribute edits changed scores more than surface edits, not that the change was construct-consistent (Section 3, pp. 4–5; Appendix A, p. 12).

This is an important self-limitation, but it is more damaging than a missing final polish. The authors de-scoped the E3 human audit and renamed “Construct Sensitivity Ratio” to “Contrast Selectivity Ratio” (Appendix K, p. 18). Thus the central perturbation semantics—the thing that makes a perturbation audit a validity audit rather than a string-sensitivity test—remain unvalidated. The paper demonstrates how an audit pipeline can be wrong; it does not demonstrate that the repaired pipeline measures construct sensitivity.

### Five failure mechanisms

| Failure | Mechanism and reported realization | What it actually demonstrates | Remaining assurance gap |
|---|---|---|---|
| **F1 silent no-op** | An edit was applied to a field not consumed by the canonical scorer. TruthfulQA/BBQ format edits were initially 100% no-op on that path; five of six CrowS perturbations edited `question` while PLL read `choices` (pp. 3, 5–6, 16–17). | Audits must check the exact scorer-consumed representation, not an upstream renderer. | The released paper has no executable path witness or per-item diff. G1 permits a pragmatic `<20%` no-op rate without adjusting the estimand for affected items. |
| **F2 regex extraction** | Qwen–TruthfulQA legacy parseability was 44%; defaults and format-dependent extraction contaminated `Δformat`. Option log probabilities made parseability 1 by construction (pp. 3, 5–6). | Response extraction is part of the instrument; parsing error can masquerade as model sensitivity. | Legacy parse failures are dropped when either member fails (Appendix C), so missingness can be perturbation-dependent. A 95% parseability threshold does not prove the retained 95% is unbiased. |
| **F3 non-faithful scoring** | F3a inverted CrowS meaning under naive MCQ loading; F3b exploited correct-first TruthfulQA MC2 ordering; F3c used top-50 log probabilities that omitted target tokens and collapsed ToxiGen scores. F3c was introduced during repair (pp. 3, 5–6). | Benchmark convention, loader order, target-token coverage, and API behavior are load-bearing instrument identity. Repairs create new instruments and new failure opportunities. | Only CrowS/BBQ are described as reference-faithful without qualification. ToxiGen and XSTest remain scorer-unvalidated; shared-prefix token and regex errors remain open. |
| **F4 broken pairing** | Independent original/perturbed resampling broke item coupling; the replacement is item-level paired bootstrap (pp. 3, 5–6). | Dependence structure belongs in the metric contract. | The numerical demonstration is one dropped, out-of-panel legacy Llama cell, not a controlled in-panel before/after. The paper admits CI-width comparisons occur at different CSR magnitudes, so F4's empirical effect is illustrative rather than identified. |
| **F5 archetype mismatch** | CSR rewards diagnostic change but penalizes invariance. BBQ demographic swaps can produce `Δattribute ≈ 0` either because the model is invariant or because the audit is uninformative; CrowS is mixed/ambiguous (pp. 4, 6–7). | Metric polarity and benchmark archetype must be explicit; numerical correctness cannot repair a wrong interpretation. | F5 is not an implementation bug and overlaps with perturbation validity. “Diagnostic/invariance/mixed” labels are proposed, not independently adjudicated, and a three-way label cannot by itself specify signed expected consequences. |

F1, F2, F3, and F4 transfer directly to agentic knowledge-work audits: the analogous mistakes are mutating a rendered view while grading native state, parsing only easy artifact exports, reversing pass/fail or authority order, truncating an evidence view, and bootstrapping dependent checks as independent. F5 transfers as a requirement to specify whether a change should alter, preserve, or conditionally alter each observable consequence.

### Six-point due-diligence gate

The gate is hierarchical:

1. **G1 scorer-faithful audit:** scorer-path no-op rate below 20%; regex parseability at least 0.95. Status: partial.
2. **G2 above-baseline original:** score at least two standard errors above a trivial baseline. Implemented.
3. **G3 non-trivial denominator:** `max(|Δformat|, |Δsemantic|) >= 0.02`. Implemented.
4. **G4 paired uncertainty:** item-paired bootstrap; independent original/perturbed resampling prohibited. Implemented.
5. **G5 archetype disclosure:** diagnostic, invariance, or mixed interpretation. Proposed.
6. **G6 repair regression:** inspect scorer outputs and add a targeted failing test for every scoring-path repair. Proposed.

The first firing condition determines the primary status: F1-ineligible, failed G2–G4, scorer-unvalidated, F5-ineligible, exploratory, then confirmatory selective/non-selective (Section 3 and Table 1, pp. 4–5). Because G5 and G6 are proposed, no row can be confirmatory. The two TruthfulQA rows are “exploratory” even though their CIs are above one; this is a procedural downgrade, not an empirical validation of gate performance (Sections 5–7, pp. 6–8).

Three design choices should not transfer unchanged:

- **G2 conflates system competence with audit integrity.** A below-baseline model can still provide valid evidence about a pipeline or perturbation; it may simply be a poor system for a particular construct claim. Audit validity and target-system eligibility should be separate predicates.
- **G3 selects against surface robustness.** A model that is correctly invariant to format and semantic-preserving edits drives the ratio denominator toward zero. Withholding a ratio is reasonable; requiring nontrivial nuisance sensitivity is not. Prefer a vector of signed effects or a prespecified contrast over ratio eligibility.
- **First-match precedence hides joint failures.** Primary action routing is useful, but assurance needs a complete independent predicate vector. The paper retains only selected secondary flags. An F1 path mismatch, unvalidated scorer, missingness problem, and wrong archetype can coexist and should not be compressed into one bucket.

## Evidence and result interpretation

The displayed ten rows support an **illustrative mechanism and disclosure-vocabulary claim**. They do not support an assurance-effect claim.

The strongest evidence is qualitative and internally candid: a canonical scorer initially ignored a repaired renderer field; format-sensitive regex parsing produced a plausible delta; a benchmark convention reversed meaning; correct-first ordering inflated a score; a repair introduced top-k truncation; and a diagnostic ratio misread an invariance construct. Seven of ten cells reportedly changed qualitative verdict between legacy and repaired pipelines (Figure 3, p. 16). These are precisely the silent defects a clean final table would conceal.

The quantitative evidence is weaker:

- 200 items, two similar-sized open models, five selected safety benchmarks, one main seed, and one main template do not calibrate failure prevalence or transport.
- Item sampling and benchmark-specific attrition are not sufficiently specified in the public paper to reconstruct the analysis population.
- Parse failures are pairwise-dropped, but attempted/parsed/paired/retained counts are not shown per cell.
- Three-seed CSR coefficients and placebo ratios are reported only as summaries from unavailable CSVs (Appendix F, pp. 13–14).
- Threshold sensitivity preserves bucket counts over a small author-chosen grid; this shows local label stability, not threshold validity (Appendix E, pp. 13–14).
- F4 lacks a matched in-panel before/after; F5 is a conceptual reinterpretation rather than a detected software fault.
- CSR's absolute effects discard polarity, while attribute perturbations lack the de-scoped human semantic audit.
- No positive-control pipeline known to be correct, unknown-fault injection set, held-out audit implementation, or independent auditor establishes sensitivity or false-withholding rates.

The five classes also do not map one-to-one to the gate. F1 and F2 share G1; F3 is partly handled by reference scoring and partly by G6; F4 maps to G4; F5 maps to G5; G2 and G3 are additional eligibility choices. Calling the result a unified gate is fair as workflow design, but not evidence that six checks are individually necessary, jointly sufficient, or decision-optimal.

## Unique insight

The paper's most valuable insight is not F1–F5 individually. Most are familiar software or measurement hazards. The unique contribution is that a **validity audit has its own validity argument and repair history**:

```text
first-order benchmark claim
≠ second-order audit observation
≠ assurance-grade audit evidence
≠ permission to use that evidence in a decision
```

A benchmark audit should therefore be treated as a versioned configured instrument, not as commentary attached to a benchmark. Its target snapshot, reference protocol, implementation, perturbation generator, observed representation, parser/scorer, missingness policy, comparison orientation, uncertainty estimator, repaired versions, and report builder all need identities and admissibility evidence.

The paper also exposes a sharper reflexive result: **a public audit should satisfy its own disclosure standard before being used as assurance evidence**. Box 1 says entries missing the visible symptom or per-cell before/after delta are not auditable (p. 8). Appendix J explicitly condenses dates, affected cells, symptoms, and deltas and points to a withheld release bundle for the full chronology (pp. 17–18). The preregistration hash, verdict CSV, raw outputs, exact code, and shipped tests are likewise unavailable. The paper is still valuable as a method proposal and transparent exploratory report, but v1 cannot be treated as the assurance-grade worked example its own strongest gate would demand.

## Limitations and validity threats

1. The taxonomy is selected from one pipeline by silence, realization, and gateability; loud, unrealized, or difficult-to-gate failures are excluded.
2. The classes overlap and are not exhaustive; the paper itself names perturbation non-isolation, template confounding, tokenization, index/filter misalignment, and context contamination as omitted F6–F10 candidates.
3. Only two 7B instruction-tuned models and five safety benchmarks are in the canonical panel.
4. The main analysis uses one seed and one template; supplementary seed/template summaries are unreleased.
5. Llama was dropped after legacy runs and before canonical rerun, so one F4 illustration is outcome- and stage-selected.
6. Analyses after F3b/F3c discovery are exploratory.
7. Exact item selection and per-benchmark candidate/attempted/parsed/paired/eligible denominators are not public.
8. Pairwise dropping when either parse fails can induce perturbation-dependent complete-case bias.
9. A 95% parseability gate does not validate the missingness mechanism or error rate on parsed rows.
10. A `<20%` no-op threshold permits substantial contamination and has no downstream loss basis.
11. Option-logprob “parseability = 1” proves an output exists, not that option tokenization or score extraction is semantically faithful.
12. Shared-prefix option-token collapse is acknowledged but unresolved.
13. ToxiGen's instruction prepend changes task content, not merely format.
14. Semantic and attribute perturbations lack independent item-level equivalence/flip labels.
15. The de-scoped human audit removes evidence needed to interpret signed construct-consistent change.
16. CSR averages absolute per-item changes and loses direction.
17. Ratio behavior couples desired attribute sensitivity to undesired nuisance sensitivity.
18. G3 can exclude correctly surface-invariant systems and does not make CSR a valid construct measure.
19. G2 mixes target-system performance with audit-pipeline validity.
20. Two-SE baselines and fixed thresholds are engineering rules without stakeholder-loss calibration.
21. The sensitivity grid is narrow and author-selected.
22. The paired bootstrap is appropriate for item coupling but benchmark sampling, repeated model calls, seeds, and task-family clusters are not represented in the main interval.
23. The paper reports no multiple-comparison policy for ten cells and several perturbation families, though it avoids confirmatory claims.
24. F4's numerical evidence is not a like-for-like controlled comparison.
25. F5 is an interpretation mismatch, not the same kind of failure as F1–F4.
26. Diagnostic/invariance/mixed labels remain too coarse for conditional or asymmetric professional consequences.
27. First-match precedence suppresses concurrent-failure structure.
28. No positive control or known-clean implementation estimates false withholding.
29. No hidden fault set estimates gate recall against unknown defects.
30. G6 is proposed despite reported tests for only F1, F3c, and F4; not every repair has a visible regression witness.
31. The full chronology required by Box 1 is absent from v1.
32. The preregistration is represented only by an asserted hash and amendment narrative; it cannot be inspected.
33. Raw CSVs, per-item predictions, repair diffs, caches, and table-building code are unavailable.
34. Model revisions are said to be pinned at load time, but exact revisions are not exposed in the paper's visible configuration table.
35. No author-verified release was found as of review, so reported computations were not independently reproduced.
36. The gate has no institutional owner, anti-gaming design, externally validated threshold, or legal-compatibility review.
37. Passing G1–G6 would still not establish benchmark construct validity, governance utility, professional validity, production fitness, or readiness.

## Reproducibility and operational realism

Paper preservation is strong: the immutable PDF, layout extraction, metadata, and complete 23-member TeX/figure source archive are local and hash-verified. The source text agrees with the PDF extraction on the gate, displayed tables, limitations, and release boundary. The rounded Table 6 numbers approximately reproduce CSR and exactly reproduce the reported bucket counts.

Empirical reproduction is blocked. Appendix K promises a future bundle with the canonical pipeline, ten-cell per-item predictions, `PREREG.md`, running audit logs, and regression tests, but says it is not part of v1 and withholds the URL. Current web searches found only arXiv mirrors and no author-identified implementation. Consequently, `cell_validity.csv`, `csr_canonical.csv`, seed/placebo tables, target-token coverage, prompt-path no-op counts, repair history, and figure/table builders were read as manuscript claims, not independently verified observations.

Operational realism is mixed. Strong features include explicit reference-versus-audit-scorer separation, software versions, hardware/cost disclosure (one RTX 4080, about 26 GPU-hours), a repair-introduced regression, residual-issue disclosure, paired uncertainty, and typed abstention. Weak features include a hand-built single-machine research pipeline, absent immutable execution receipts, no cache/state or environment manifest, no external reviewer, no complete denominator ledger, no independent perturbation labels, and no prospective use study. This is a useful exploratory self-audit design, not an assurance service or operational benchmark lifecycle demonstration.

## Transferable benchmark implications

1. **Give every audit an instrument identity.** Bind target task/suite, source/reference release, implementation, harness, environment, perturbation generator, observer view, parser/scorer, metric, missingness policy, uncertainty code, and report builder by version/hash.
2. **Separate path reachability from semantic admissibility.** A mutation reaching the grader-consumed field is necessary; an independent authority must still establish that it preserves or flips the declared requirement and consequence.
3. **Keep complete denominator ledgers.** Record candidate, attempted, executed, observed, parse-valid, pair-complete, eligible, analyzed, and reported counts plus reasons. Never hide differential missingness behind parseability.
4. **Use predicate vectors before disposition precedence.** Preserve every failed, passed, unavailable, and not-applicable check. A primary remediation route may be derived afterward without erasing co-failures.
5. **Separate audit integrity, target-system eligibility, and construct interpretation.** G1/G4/G6-like checks concern the pipeline; G2 concerns the tested system/population; G5 and perturbation labels concern the construct; G3 concerns one ratio estimand. Do not fuse them into one notion of validity.
6. **Prefer signed, consequence-specific contrasts over one ratio.** Declare whether each perturbation should change, preserve, or conditionally change each observable. Include valid alternatives and nuisance controls.
7. **Treat repair as a new instrument version.** Preserve defect discovery, affected cells, visible wrong result, inherited versus introduced provenance, exact diff, before/after observations, targeted failing test, clean negative controls, collateral regressions, and residual status.
8. **Audit the audit's assurance claim.** Method papers and internal reports can be useful while non-confirmatory. Promote them to assurance evidence only when their own required records and executable witnesses are inspectable.
9. **Keep claim ceilings explicit.** Passing pipeline checks licenses, at most, trust in a bounded audit result under the frozen configuration. Benchmark validity and downstream decisions require separate evidence.

## Concrete repository actions

1. **Do not add a new schema task.** Existing provenance-boundary, configured-system, evidence-view, benchmark-bundle, metric-monitoring, task-health, adversarial-verifier, release-reconstruction, and validity-argument machinery already has homes for these requirements.
2. In the next consolidation pass, add an **audit-of-audit assurance boundary** to the canonical taxonomy: target identity → implementation/observation identity → perturbation admissibility → denominator/comparison validity → repair chronology/regression → complete predicate vector → typed disposition → bounded use.
3. Apply the boundary to future internal validation reports. A report that lacks its own attempted/observed/eligible denominators, exact code/input/output hashes, comparison orientation, repair history, or valid-alternative controls should remain `exploratory` or `withheld`, even if all displayed checks pass.
4. Revisit this source only if an author-identified release appears. Pin its publication timing and commit, verify correspondence to v1, reconstruct representative F1–F5 cells, test missingness and polarity mutations, and compare the complete chronology to Box 1 before upgrading the review to release-audited.

No new queue task is justified. The evidence calls for consolidation and reuse of existing contracts, not another parallel subsystem.
