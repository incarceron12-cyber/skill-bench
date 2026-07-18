# Paper Review: Decision-Aligned UQ — Formal Metric–Utility Alignment Is Not Stakeholder Utility

- **Paper:** <https://arxiv.org/abs/2606.26990v1>
- **Title:** *Decision-Aligned Evaluation of Uncertainty Quantification*
- **Authors:** Annika Schneider, Tommy Rochussen, Joshua Stiller, Vincent Fortuin
- **Date read:** 2026-07-19
- **Version read:** immutable arXiv v1, submitted 25 June 2026
- **Local PDF:** `data/papers/pdfs/2606.26990v1-decision-aligned-uncertainty.pdf` (45 pages; SHA-256 `e57fa1caaa12396a8b877f5a32a3330a575254665f1179d72301a8ff4264807a`)
- **Local text:** `data/papers/text/2606.26990v1-decision-aligned-uncertainty.txt` (SHA-256 `4f7028cb28831d452b0f30ec5fe479ac1de9e7efa11ca24713df3e84a0759dd5`)
- **TeX source:** `data/papers/source/2606.26990v1-source.tar` (SHA-256 `0faff23c1d5e8740d0614340439f055e6f678595d3b3e977d2f1897acf56d0e4`)
- **Official release:** `data/sources/releases/2606.26990v1-prior-weighted-utilities/fortuinlab-prior-weighted-utilities-94ab70d.zip` (commit `94ab70d6e88857b2b561390f017feb29a1716fac`, one day before v1; SHA-256 `f191c20660f28e31cdf76f8609c3c60864eec2cb7d9fb23374cd3239a4699d0d`)
- **Release provenance:** `data/sources/releases/2606.26990v1-prior-weighted-utilities/provenance.json`
- **Tags:** uncertainty-quantification, metric-validity, decision-utility, proper-scoring-rules, ranking, priors, implementation-audit

## One-sentence contribution

The paper gives a useful formal test for whether a scalar uncertainty metric induces exactly the same ordering and ties as expected utility under one declared decision-family prior, then constructs prior-weighted utility (PWU) scores that satisfy that test by definition; however, the controlled experiments largely compare those metrics against utilities sampled from the same authored priors, the priors are heuristic rather than stakeholder-elicited, “real-world” case studies are offline simulations, and the timing-appropriate code contains a consequential selective-prediction cost bug plus a tie-blind Kendall implementation, so the evidence licenses a bounded metric-construction principle—not stakeholder utility, improved decisions, realized consequences, general metric superiority, or agent readiness.

## Why this matters for skill-bench

`skill-bench` already separates measurements, validity claims, thresholds, decisions, and consequences. This paper sharpens one intermediate link: a benchmark metric can be tested for whether its ordering is coherent with an explicitly declared family of downstream losses. That is stronger than calling a generic average “decision relevant,” but much weaker than showing that stakeholders authorize the utility, users act on the score, decisions improve, or consequences are beneficial.

The transferable chain is:

```text
versioned prediction or benchmark observation
→ candidate metric and aggregation
→ declared action set and utility family
→ authorized prior over utility parameters
→ metric-induced ordering/ties
→ order/tie agreement under held-out systems and cases
→ threshold or selection policy
→ observed uptake and action
→ realized benefit, burden, loss, and harm
→ transport and non-regression
```

The paper formalizes the fourth-to-fifth link. It does not observe the final four links. This advances charter objectives A, B, C, and E without narrowing the benchmark to UQ: the reusable issue is how any score’s ordering relates to a declared decision objective.

## Research question and claim boundary

The central question is: when can a metric over probabilistic predictions be interpreted as ranking predictions exactly as expected downstream utility would under a prior over decision parameters? The authors analyze binary decisions, selective prediction, and top-*k* selection in binary classification and Gaussian regression; extend selected results to multiclass and multivariate cases; and propose PWU metrics as prior-weighted integrals of negative utility (Sections 3–4, pp. 3–8; Appendices C–I, pp. 16–34).

### Supported by the paper and release

1. Decision-alignment is explicitly defined as a strictly increasing transformation between a metric and negative expected utility for every fixed label vector (Definition 3.1, p. 3).
2. Under that definition, strict order and tie preservation are equivalent to decision-alignment for a fixed utility family and prior (Proposition 3.4, pp. 3–4; full proof p. 16).
3. A separability barrier rules out coordinate-dependent metrics as aligned with pointwise-separable utility families under the stated integrability assumptions (Lemma 3.6, p. 4; proof p. 16).
4. For binary cost-sensitive classification, NLL, Brier score, and accuracy have recognizable implicit weighting measures; ECE, MCE, retention AUC, and error detection fail the paper’s alignment condition (Section 3.2, pp. 4–5).
5. PWU metrics are constructed directly as prior-weighted negative utilities, so their alignment is definitional; with finite expectations they are proper, and strict properness additionally requires unique Bayes acts (Propositions 4.1–4.2, p. 8).
6. The paper reports 100 repeated five-fold model comparisons on five binary and five univariate datasets, plus multiclass/multivariate extensions and three offline applied case studies (Section 5 and Appendices J–K, pp. 8–9 and 35–44).
7. The official repository is timing-appropriate, complete as a 64-file code tree, syntactically valid, and contains implementations for preprocessing, training, metrics, sensitivity analysis, and all three case studies.

### Not established

The study does **not** establish that its priors represent stakeholder preferences, that the selected utility families cover consequential outcomes, that a PWU-guided user changes a decision, that such a decision improves welfare, that any affected party accepts the loss function, that average utility is equitable, or that results transport to agentic knowledge work. It does not establish general superiority over every conventional metric: the winning PWU depends on decision family, some conventional metrics align well in particular settings, and the P2P top-*k* PWU is reported as second-best. It also does not establish the published selective-regression empirical values from the released code because the implementation does not match the paper’s per-instance abstention loss.

## Methodology and formal system

### Decision-alignment

For metric `M`, utility family `{Uθ}`, fixed labels `y`, and nonnegative nonzero measure `π`, Definition 3.1 requires a strictly increasing `h_y` such that:

```text
h_y(M_y(f)) = ∫ -U_{θ,y}(f) π(θ)dθ   for every admissible prediction f.
```

The measure need not be finite or normalized, but the integral must be finite. This is an exact functional requirement, not approximate correlation. Proposition 3.4 correctly makes ties first-class: equal metric values must imply equal expected utility, not merely similar rank.

This definition is useful but narrow:

- it is conditional on one authored utility family and measure;
- `h_y` may vary with the full label vector, so alignment is not necessarily one globally stable cardinal calibration;
- it evaluates complete prediction vectors against fixed labels, not prospective decisions under unknown outcomes;
- it concerns ordering and ties, not the magnitude of utility differences, threshold regret, user uptake, or consequences;
- any metric can be made trivially aligned with a utility family defined from the metric itself, as Appendix D acknowledges (p. 21).

Thus decision-alignment diagnoses coherence **relative to a declared family**; it does not discover the right family.

### Separability and the analyzed decisions

The separability barrier is the paper’s most reusable negative result. If every utility is pointwise separable, any aligned metric must be coordinate-independent (Section 3.1, pp. 3–4). This excludes pooled calibration and ranking metrics from exact alignment with the paper’s per-instance binary-decision and selective-prediction families.

The instantiated families are:

- **binary classification:** false-positive/false-negative cost ratio `c`, with Bayes threshold `c`;
- **classification top-*k*:** precision among the selected *k* items;
- **regression selective prediction:** squared-error prediction versus abstention cost `λ`;
- **regression top-*k*:** select by `μ − γσ²`, with selection size *k* and risk aversion `γ`.

These are plausible examples, not a complete action ontology. They omit delayed outcomes, irreversible actions, multi-stage information acquisition, human review capacity, non-additive severe harms, distributional effects, and stateful downstream consequences—all central to agentic knowledge work.

### “Pathological” implicit priors

For binary decisions, the paper recovers NLL weighting `1/[c(1−c)]`, uniform Brier weighting, and accuracy’s point mass at `c=.5` (Proposition 3.7, p. 5). For selective Gaussian regression, NLL aligns only after truncating both variance and abstention-cost domains above `ε`, under a Pareto density concentrated toward the lower boundary (Proposition 3.12, pp. 6 and 19–20). MSE corresponds to always predicting (`λ=∞`).

Calling these priors “pathological” is partly normative. The paper defines pathology as degenerate, uninformative, or placing unbounded mass where UQ is least needed (footnote 7, p. 5). Degeneracy and divergence are formal properties; “uninformative” and “least needed” depend on the decision context. Accuracy at `.5` is inappropriate under asymmetric costs but coherent under symmetric costs. Uniform weighting can be a deliberate robustness policy. The formal result reveals the weighting; stakeholder evidence must decide whether it is unacceptable.

### PWU construction and properness

A PWU metric is simply:

```text
Mπ(f,y) = ∫ -Uθ(f,y)π(θ)dθ.
```

Its decision-alignment follows immediately with `h_y` equal to identity (Proposition 4.1). Properness follows because each negative Bayes-act utility is a proper score and nonnegative integration preserves expected-score optimality, subject to finiteness; strict properness requires uniqueness (Proposition 4.2 and Appendix D).

This is principled but should not be oversold as independent empirical discovery. For a chosen family and prior, PWU is the target expected loss. Exact alignment is built in. The real scientific questions are whether the family, prior, action model, outcome horizon, aggregation, and affected-party tradeoffs are valid—and whether finite implementation preserves the definition.

## Empirical design and evidence

### Controlled datasets

The paper trains ten model classes each for binary classification and univariate regression on five UCI datasets per setting. It uses 100 repeated five-fold splits, averages each model’s metric and utility over folds within repeat, ranks models, and compares rankings with Kendall’s `τ` (Appendix J, pp. 34–36). Multiclass and multivariate experiments use five model classes over five datasets each (Appendix K, pp. 43–44).

For each controlled utility family, only five parameter values are sampled once from the same prior used to define the corresponding PWU, and alignment is averaged over those five utilities (Appendix J.1, pp. 35–37; release evaluation scripts). This creates a strong target-construction coupling:

```text
PWU = Monte Carlo average utility under authored prior A
reported target = average ranking agreement over five utility draws from prior A
```

High alignment is therefore primarily a finite-sample and model-ranking confirmation of the construction. It does not independently validate prior A, the utility family, or downstream use. A stronger test would freeze priors before model inspection, evaluate many held-out parameter draws, include adversarial and stakeholder-derived utilities, and report regret/decision loss as well as ranking.

Reported patterns are also heterogeneous. Binary-decision PWU is strongest across its five datasets, but top-*k* classification is weak or negative for many datasets; on ionosphere, the corresponding PWU median is `−.11`, and on sonar it is `.09` (Table J.2, p. 44). The mushroom top-*k* task is trivial enough to produce `τ=1`, which the sensitivity discussion itself flags as possible saturation (p. 41). “Consistently align” should therefore be read relative to comparators and selected summaries, not as uniformly high alignment.

### Applied case studies

The three cases are more informative because their utility formulas differ from the controlled PWU targets:

1. **Electricity bidding:** models forecast December 2024 wind generation; an analytic bidding rule uses day-ahead and balancing prices, a capacity constraint, and a fixed 1% risk certificate. Daily resampling yields 100 bootstrap ranking panels (pp. 37–39).
2. **Credit approval:** customer-dependent false-positive and false-negative costs are derived from prior literature over PAKDD and Kaggle data (pp. 39–40).
3. **P2P lending:** a fixed budget greedily funds the highest predicted repayment probabilities; realized return depends on loan amount, term, rate, and repayment (pp. 39–40).

These are offline policy simulations using historical labels and authored economic formulas. They do not observe an operator, bank, borrower, lender, market feedback, adoption, legal constraints, distributional consequences, or realized deployment. The electricity PWU medians are only `.16` with intervals crossing zero (Table 2, p. 9). The P2P top-*k* PWU is second-best, not best (Figure J.6, p. 40). These cases support limited out-of-family ranking correspondence, not “realized decision utility” in the ordinary prospective sense.

### Sensitivity analysis

The sensitivity analysis shifts prior modes substantially while leaving the PWU fixed and resampling only five utility parameters from each perturbed prior (Appendix J.3, pp. 40–42). It shows qualitative robustness in these model/dataset panels, but it does not vary:

- stakeholder disagreement or multimodal priors;
- utility-family form, except informal cross-family comparison;
- action availability, review capacity, or delayed outcomes;
- base-rate or dataset shift independently of model resampling;
- prior concentration at fixed mode;
- threshold-selection data versus held-out decision data;
- aggregation across affected groups or severe-tail losses.

The paper’s cross-family robustness argument is post hoc: it observes that some PWUs also correlate with other utilities and speculates that properness explains this (Remark J.1, p. 42). Properness alone does not guarantee useful ranking under an arbitrary decision family.

## Official release audit and representative reproduction

The official commit predates v1 by one day and includes source code for all claimed experiment families. It contains no committed datasets, predictions, model checkpoints, result CSVs, tables, or execution receipts. Full reproduction requires external UCI/Kaggle/ENTSO-E inputs, an ENTSO-E key, and approximately 2,500 reported GPU-hours (Appendix J.4, pp. 42–43). Paper tables therefore cannot be recomputed from the archive alone.

All released Python files pass `py_compile`, and two focused standard-library/Numpy checks reproduced important implementation properties.

### 1. Selective-prediction loss does not implement the paper

Paper Equation in Section 3.3.1 charges each abstained item `λ`; dataset utility is the mean. In `src/metrics/utility/selective_regression.py`, however:

```python
n_abst = np.sum(abst)
cost_abstain = abst_cost * n_abst
cost[abst] = cost_abstain
return -np.mean(cost), n_abst
```

Every abstained row is assigned the **total** abstention cost, so the mean contribution is `λ·n_abst²/n`, not `λ·n_abst/n`. A four-row fixture with two abstentions and `λ=1` produced implementation utility `−1.0` versus paper-formula utility `−0.5`, exactly a factor of two. In general the overcharge factor is `n_abst`.

This function is used both to compute selective-prediction utility targets and inside `selective_prediction_pwu`; it also feeds the electricity case’s selective PWU. Consequently, the released univariate selective-prediction PWU and target rankings implement an abstention-count-dependent, non-pointwise loss that contradicts the theorem and paper description. Without original predictions/results or a corrected rerun, Tables J.3, the regression panels of Figures 2/J.9, and the selective-PWU columns in the electricity study are not auditable as evidence for the stated construction.

### 2. Kendall implementation discards ties and is misinterpreted

`src/utils/metric_correlation.py` accepts only two strict permutations and explicitly assumes “no ties.” Evaluation scripts sort model names by metric values, turning exact ties into arbitrary order. This conflicts directly with Proposition 3.4, where tie preservation is necessary. Saturated top-*k* utilities are especially likely to tie.

The paper also says `τ=.8` means 80% of pairwise model comparisons agree (p. 36). For strict rankings, `τ = (C−D)/(C+D) = 2·agreement−1`; `τ=.8` means **90%**, not 80%, agreement. A five-item fixture with one discordant pair reproduced `τ=.8` and pairwise agreement `.9` from the release helper. This is an interpretation error, while forced tie breaking can also alter the statistic itself.

### Additional release limits

- PWUs use 10,000 fixed-seed Monte Carlo samples per evaluation, but no Monte Carlo error or convergence check is reported.
- Utility parameter names are rounded to two decimals in output labels; distinct draws could collide in column names.
- The five sampled utility parameters are fixed globally, which aids comparability but provides a very small quadrature for the target expectation.
- Repeated split results share the same underlying dataset and many observations; percentile summaries describe rerandomized split/model behavior, not independent deployment populations.
- The release has no tests, result manifests, table-reproduction script, environment image, hardware receipt, dataset hashes, or complete lockfile-to-result provenance.
- External data licensing/access is uneven: two Kaggle sources and ENTSO-E inputs are not redistributed; one electricity source has no explicit license according to the paper.

## Unique insight

The paper’s strongest contribution is a **metric claim ladder**:

```text
metric is proper
≠ metric is aligned with a named decision family
≠ prior/family is authorized and realistic
≠ finite implementation preserves that alignment
≠ model ordering is stable on held-out systems and populations
≠ selecting by the metric improves a decision
≠ stakeholders receive net benefit
```

Properness concerns truthful probabilistic reporting in expectation. Decision-alignment concerns exact order/tie equivalence to one prior-weighted family. Neither chooses the family or prior, validates implementation, or supplies causal outcome evidence.

A second insight is that **utility specification is part of benchmark authorship, not neutral aggregation**. The action set, outcome horizon, cost units, affected parties, prior, concentration, dependence, group aggregation, and severe-harm gates can all change rankings. Making these choices explicit is valuable; calling a heuristic prior “plausible” does not make it authoritative.

A third insight comes from the release defect: formal validity and implementation validity must be linked by executable conformance tests. A one-line vectorization error changed a pointwise abstention utility into a dataset-size-dependent loss, invalidating the theorem-to-result bridge while all code remained syntactically correct.

## Limitations and validity threats

1. Decision-alignment is relative to an authored family and prior; it cannot identify the correct stakeholder utility.
2. The transformation may depend on the full fixed label vector, limiting global cardinal interpretation.
3. Exact alignment is stronger than needed for some decisions and silent about magnitude/regret.
4. The analyzed utility families omit information acquisition, multi-stage action, delayed consequence, irreversibility, and review capacity.
5. “Pathological” combines formal degeneracy/divergence with contestable normative judgments.
6. PWU alignment is true by construction, so controlled experiments are mainly implementation/ranking sanity checks.
7. Controlled target utilities are sampled from the same prior used to define each PWU.
8. Only five utility-parameter draws represent each family per experiment.
9. Priors are heuristic and claimed a priori but have no immutable preregistration or stakeholder elicitation record.
10. The binary prior’s false-negative asymmetry is not universal across domains or affected parties.
11. Independence between *k* and risk aversion in regression is assumed, not evidenced.
12. Rescaling `λ` and `γ` by empirical outcome variance makes the utility population-dependent.
13. Test-label variance is used inside released regression PWU/utility evaluation, making metric semantics depend on the evaluation sample.
14. Ten UCI tabular datasets provide limited evidence for modern agentic knowledge work.
15. Repeated cross-validation splits are dependent and do not sample new domains, institutions, or time periods.
16. Percentile bands are not confidence intervals for a declared target population.
17. Model-pair and dataset clustering are not represented in a hierarchical estimand.
18. Multiple metric–utility–dataset comparisons have no multiplicity or minimum-important-difference policy.
19. Saturated top-*k* tasks can produce ties/trivial success, yet the implementation forces strict rankings.
20. The custom Kendall helper has no tie support despite tie preservation being central to the theorem.
21. The paper misstates the relation between Kendall’s `τ` and pairwise agreement.
22. Sensitivity varies prior modes but not all consequential concentration, family, horizon, group, and tail-loss assumptions.
23. Cross-family robustness is post hoc and not guaranteed by properness.
24. Applied cases are retrospective/offline simulations, not observed decisions or consequences.
25. Electricity bidding uses one month, one wind farm, one fixed risk certificate, and only 31 daily blocks.
26. Electricity median alignment is modest and intervals cross zero.
27. Credit and lending utilities inherit assumptions and data limitations from prior studies.
28. P2P uses a greedy policy and selected worse-grade loans, limiting policy/population transport.
29. No affected-party, fairness, subgroup, or distributional analysis accompanies average economic utility.
30. No user uptake, comprehension, action, workload, delay, burden, or harm is observed.
31. The selective-prediction implementation overcharges abstention by `n_abstain` and breaks pointwise separability.
32. The defect affects both target utilities and PWU metrics, so apparent agreement can persist around the wrong implemented construct.
33. No released prediction/result artifacts allow corrected table reconstruction.
34. Fixed 10,000-sample Monte Carlo integration has no numerical error assessment.
35. No unit tests compare code against paper equations or closed-form special cases.
36. External datasets and credentials prevent turnkey reproduction.
37. The reported full rerun cost is roughly 2,500 GPU-hours.
38. Dataset snapshots, hashes, and complete result-producing environment receipts are absent.
39. First-order predictive distributions exclude richer epistemic representations by design.
40. No evidence licenses general metric superiority, stakeholder utility, professional validity, safety, production fitness, or readiness.

## Reproducibility and operational realism

Paper-level inspectability is strong: the immutable 45-page manuscript includes definitions, full proofs, metric formulas, prior guidance, model descriptions, datasets, case formulas, sensitivity analysis, compute estimates, and result tables. The timing-appropriate official code is also unusually complete structurally.

Result reproducibility is weak-to-moderate. The code archive is syntactically valid and exposes exact priors, seeds, model pipelines, and metric routines, but omits all inputs, predictions, results, and execution receipts. Recreating the full study requires substantial compute and several externally gated datasets. Most importantly, a focused executable audit found that a central released utility does not match the paper equation. Until a corrected rerun is preserved, the regression selective-prediction empirical evidence should be treated as implementation-invalid.

Operational realism is low for decision claims. Historical economic formulas and realistic tabular datasets are better than abstract toy utility alone, but no actual decision-maker, institution, interaction, adoption, or consequence is observed. The experiments evaluate offline model rankings, not an operating decision-support policy.

## Transfer to skill-bench

### 1. Add a metric-to-utility alignment record, not a UQ subsystem

Use existing metric-monitoring and validity machinery to bind:

- immutable metric implementation and aggregation hash;
- observation unit, eligible population, missingness, dependence, and outcome timing;
- action set and parameterized utility/loss family;
- utility authority, affected stakeholders, units, horizon, and prohibited interpretations;
- prior family, parameters, elicitation evidence, disagreement, and version;
- expected-utility computation and numerical error;
- order, tie, cardinal, threshold, and regret estimands separately;
- held-out system/task/time populations and transport boundary;
- implementation-conformance evidence and reassessment triggers.

### 2. Preserve four distinct claims

Report separately:

1. **formal coherence:** theorem/definition under explicit assumptions;
2. **implementation conformance:** executable tests show code matches equations;
3. **empirical ranking transport:** held-out systems/populations preserve useful ordering/ties;
4. **decision consequence:** a frozen policy improves declared loss, workload, or stakeholder outcome.

Never promote (1) directly to (4).

### 3. Treat priors and utility weights as governed benchmark artifacts

Require author/role, affected-party scope, elicitation method, units, context, disagreement, alternatives, validity period, and sensitivity envelope. A generic default may be useful for stress testing but cannot be called stakeholder utility without authorization evidence. Preserve severe noncompensatory gates and distributional outcomes separately from mean utility.

### 4. Test equations against implementations

For every decision-weighted metric, include:

- closed-form and brute-force fixtures;
- one-item and multi-item cases;
- no-action/all-action/mixed-action cases;
- ties and near-ties;
- population-size invariance where the theory requires an average;
- Monte Carlo convergence and fixed-seed independence checks;
- mutation tests for sign, normalization, threshold inequality, and duplicated total costs.

The selective-prediction defect is exactly the kind of theorem-to-code drift these tests should catch.

### 5. Evaluate decisions, not only rank correlations

On a diverse pilot, compare conventional metrics, authored-utility metrics, simple baselines, and oracle-informed bounds under frozen selection/review policies. Report false acceptance/rejection, severe defects, review capacity, delay, cost, regret, and subgroup/tail outcomes. Use held-out tasks and stakeholders; do not sample test utilities from the same prior solely used to construct the metric.

### 6. Preserve ties and multiple estimands

Use tie-aware Kendall variants or explicit partial orders; report pairwise agreement correctly as `(τ+1)/2` only for strict complete rankings. Keep order agreement, top-*k* selection, cardinal correspondence, threshold decisions, regret, and consequence distinct. Forced alphabetical or column-order tie breaking is instrument behavior, not evidence.

## Concrete repository actions

1. **Add no UQ-specific schema.** Existing metric-monitoring, validity-argument, configured-component, participation/authority, task-health, and consequence ladders can represent the obligations.
2. Add one bounded consolidation task to integrate formal metric–utility alignment, utility/prior authority, implementation conformance, tie-aware ordering, and the claim ceiling into the canonical taxonomy and synthesis index alongside LATTICE and Agentic Confidence Calibration.
3. For future decision-weighted pilot scores, require an executable equation-to-code conformance fixture before any ranking or utility claim, then separately test a frozen decision policy on held-out cases.

## Action items completed

- [x] Read the complete immutable v1 PDF/text through all proofs, metric definitions, prior guidance, experiments, sensitivity analysis, reproducibility statement, and result tables.
- [x] Inspected the complete timing-appropriate 64-file official code release and provenance.
- [x] Reconstructed the formal criterion, assumptions, decision families, implicit priors, PWU construction, empirical estimands, models, datasets, case studies, sensitivity, and claim boundaries.
- [x] Executed a syntax check of every released Python file.
- [x] Executed focused fixtures demonstrating the selective-prediction cost defect and the correct `τ=.8 → 90%` pairwise-agreement relation.
- [x] Compared the result against LATTICE’s response→decision→consequence boundary and Agentic Confidence Calibration’s prediction→policy→workload/loss boundary.
