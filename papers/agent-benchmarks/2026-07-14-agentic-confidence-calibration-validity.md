# Paper Review: Agentic Confidence Calibration — Calibrated Failure Prediction Is Not Causal Diagnosis or Decision Utility

- **Paper:** https://arxiv.org/abs/2601.15778v1
- **Authors:** Jiaxin Zhang, Caiming Xiong, Chien-Sheng Wu
- **Date read:** 2026-07-14
- **Source read:** complete immutable arXiv v1, submitted 22 January 2026
- **Local PDF:** `data/papers/pdfs/2601.15778v1-agentic-confidence-calibration.pdf` (37 pages; SHA-256 `02efe75f3cde277d7fd59f70912fbb7f8ebfb3be63762dc866d20c67075fbfbf`)
- **Local text:** `data/papers/text/2601.15778v1-agentic-confidence-calibration.txt` (SHA-256 `e9aed3d7ebc68e11da8e51c746eb9a61eb35b5f064889c21dee98c4c48943936`)
- **Immutable source:** `data/papers/source/2601.15778v1-source.tar.gz` (SHA-256 `2dc36db003f76c73a4b60be08f8748865ae1ce81626fb002f94d24871106bbc6`)
- **Provenance:** `data/sources/2601.15778v1-agentic-confidence-calibration.provenance.json`
- **Venue/release boundary:** the author's current official page labels the work ICML 2026, but OpenReview forum, API, and PDF retrieval remained challenge-blocked on 14 July 2026. No reviews, rebuttal, decision record, or accepted-version manuscript was inspected. Neither v1, its source archive, nor the author's current publication entry links code, trajectories, labels, splits, or a GAC artifact.
- **Tags:** confidence-calibration, trajectory-features, selective-prediction, decision-validity, configured-systems, failure-prediction, logprobs

## One-sentence contribution

The paper turns one completed trajectory's token-confidence trace into 48 summary features and fits regularized logistic predictors of binary final-answer success, reporting better in-sample cross-validated ECE, Brier score, and AUROC than final/global confidence baselines across seven mostly QA/reasoning datasets and GAIA; the useful contribution is treating **configured-trajectory success probability as a separate observation**, but incomplete split/configuration/label provenance, nominally duplicated features, non-nested tuning, weak transfer evidence, invalid online-theory assumptions, and no selective-action experiment block its stronger claims of diagnosis, universal transfer, deployment reliability, or utility.

## Why this matters for skill-bench

`skill-bench` needs to decide which completed or partial runs deserve verification, human review, retry, escalation, or abstention. A calibrated probability of satisfying a declared success predicate could make those allocations more efficient. It is not itself correctness, root cause, professional quality, safety, or readiness.

The paper exposes a missing distinction in the project's reliability stack:

`configured trial + observable trajectory → predicted probability of one outcome → calibrated/discriminative evidence → decision policy → realized loss/workload`

Most of the paper evaluates the middle prediction link. It does not evaluate the final decision link. That boundary is reusable across domains and advances charter objectives A, B, D, and E without making calibration or question answering the benchmark's scope.

## Research question and claim boundary

The empirical question is whether engineered statistics over all generated-token confidence values predict a binary final-answer success label better than verbalized confidence, final-step token confidence, global token-confidence averaging, temperature-scaled versions of the latter two, and several learned baselines (Sections 2–3, pp. 3–9; Appendix A.2, pp. 15–18).

The immutable v1 evidence supports a bounded finding:

- under the paper's unreleased trajectory-generation and labeling pipeline, regularized logistic models over the supplied feature map have favorable reported cross-validated ECE, Brier score, and AUROC on eight benchmark samples;
- trajectory summaries contain predictive information beyond the reported final/global averages in these samples;
- predictive relations vary by benchmark, answer format, model, and framework;
- zero-retraining transfer can work between some source/target pairs and fail badly for others;
- pooling seven development datasets produces lower reported ECE on 165 GAIA validation items than the paper's direct-train and transfer comparisons, while not producing the best Brier score or AUROC (Table 3, p. 9).

It does **not** establish calibrated confidence for repeated attempts, professional artifact quality, causal failure localization, online early warning, intervention benefit, workload reduction, cross-provider logprob comparability, universal transfer, safety, production fitness, or readiness. The paper itself correctly warns that a calibrator may create false security and that evaluation must go beyond calibration metrics (Ethical Statement, p. 10), but its abstract, takeaways, deployment discussion, and conclusion repeatedly outrun that boundary.

## Methodology and system reconstruction

### Target and unit

The formal target is `P(binary task success | features of one completed trajectory)`. A trajectory contains states, actions, observations, and token log-probabilities for generated actions (Section 2.1, p. 3). In practice, however, the predictor only receives 48 summaries of token-confidence and trajectory-length patterns—not tool-return uncertainty, environment state, evidence authority, artifact state, or semantic action correctness.

The observational unit appears to be one generated trajectory per sampled benchmark item. The paper does not report repeated attempts per item, generation seeds, duplicate questions, shared source groups, or an item/trajectory identifier ledger. The probability therefore mixes task difficulty, answer prevalence, configured model/scaffold behavior, trajectory form, and label noise. It is not an intrinsic confidence property of an agent or task.

### Eight benchmark populations

Appendix A.2.1 (pp. 15–16) reports:

- 500 sampled test items each from SimpleQA, HotpotQA, StrategyQA, MATH500, MMLU-Pro, and HLE;
- all 448 GPQA MAIN items, with multiple-choice options removed;
- all 165 GAIA validation items.

Seven sets are primarily static QA or reasoning prompts routed through an agent scaffold; only GAIA centrally requires heterogeneous tools/documents/web interaction. Calling all eight evidence about complex autonomous-agent trajectories therefore stretches construct coverage. The paper also calls the seven-dataset pooled ablation `3,446 trajectories` (Appendix A.4, p. 26), while its declared per-dataset counts imply 3,448. No exclusions explain the two-row difference.

Random subset seeds are not given for task sampling. The shared fixed seed of 42 applies to model evaluation code, not clearly to benchmark sampling. Source release/version, retrieval date, contamination handling, and exact item IDs are absent. GPQA's transformation removes options but gives no answer-normalization or equivalence protocol.

### Configured agents and models

Main experiments use smolagents CodeAct; one GPQA comparison uses OAgents. Named backbones include GPT-4.1, GPT-4o, GPT-OSS-120B/20B, DeepSeek-v3.1, and Qwen3-235B (Section 3.1, p. 5; Appendix A.2.3, p. 17). The paper does not provide exact endpoint snapshots, access dates, prompts, tool schemas, web/search providers, budgets, temperatures, stopping rules, retry/failure policies, tokenization, logprob request settings, or a dataset-by-model assignment table.

This is material rather than clerical. A calibrator predicts a configured system under a particular environment. Trajectory length can encode scaffold budget; token confidence can shift with model, tokenizer, provider truncation, top-k return semantics, and decoding. Cross-dataset transfer performed under an incompletely specified configuration is not evidence of configuration-invariant reliability.

### Success labels and oracle construction

The paper says every final answer is judged by Gemini-2.5-Pro using question, dataset ground truth, and agent answer; a stratified subset allegedly has 90–95% agreement with human experts (Section 3.1, p. 5; Appendix A.2.2, pp. 16–17). It does not report:

- which datasets use exact checks versus the model judge;
- judge endpoint, prompt, date, settings, retries, invalid outputs, or repeated calls;
- human sample size, strata, qualifications, assignment, blinding, instrument, adjudication, or uncertainty;
- class-specific agreement, false-positive/false-negative rates, criterion authority, or disagreement cases;
- whether labels were regenerated for every model/framework configuration.

A 90–95% raw agreement range without counts or prevalence is not a validated oracle. Training and evaluating against the same noisy label policy can yield good calibration to that policy while being miscalibrated to deterministic correctness, expert acceptance, or downstream consequence. HLE and GAIA free-form judging also create task-dependent label error exactly where calibration claims are most consequential.

### The 48-feature map

The paper organizes statistics into Dynamics (19), Position (14), Stability (10), and Structure (5) (Section 2.2, pp. 3–4; Appendix A.5, pp. 27–30). It computes per-step means, standard deviations, entropy, concentration, relative spread, skewness, token/step gradients, first/last summaries, and length statistics.

The design is inspectable, but its semantics are weaker than the names suggest:

1. The method starts from token log-probabilities, then Appendix A.5 switches to unspecified positive confidence values `r`, normalizes them **across token positions in a step**, and calls the resulting positional distribution “attention.” This is not model attention and is not a probability distribution over semantic hypotheses.
2. “Top1Conf” and “TopkConf” are not operationally defined. The manuscript alternates among log-probability, token confidence, top-1, and top-5 terminology without specifying exponentiation, padding, provider top-k behavior, or unavailable mass.
3. At least four nominal dimensions are exact duplicates by the paper's formulas: first spread equals first volatility; last spread equals last volatility; mean attention spread equals mean token volatility; and their standard deviations likewise coincide (pp. 27–29). The advertised 48-dimensional surface therefore contains fewer distinct computed quantities unless an unreleased implementation differs.
4. Undefined statistics for short steps/trajectories are set to zero. Zero can also be a legitimate statistic, so missingness is silently encoded as evidence.
5. Fixed normalization such as `step_count / 10` embeds scaffold/budget conventions and can proxy dataset identity or difficulty rather than transferable epistemic state.
6. Structure and answer-format features can be useful predictors while remaining shortcuts. The paper itself observes that shared output format may drive transfer (p. 8), which weakens the “uncertainty grammar” interpretation.

These summaries can predict failure without revealing what failed. A long trajectory, low final confidence, or volatility may result from a difficult task, a conservative but correct workflow, provider behavior, bad retrieval, tool errors, or a flawed grader. Predictive feature names do not adjudicate among those causes.

### Calibrator and baselines

HTC-Full is ridge logistic regression; HTC-Reduced is lasso logistic regression. Inference baselines include verbalized confidence, final-step and global-trace averages, and temperature-scaled variants. Learned baselines include LSTM, Transformer, MLP, Gaussian process, and XGBoost (Sections 2.3 and 3.1, pp. 4–5; Appendix A.2.4–A.2.5, pp. 17–18).

The comparisons do not isolate “whole trajectory” cleanly:

- final/global baselines are one-dimensional while HTC gets many nonlinear summaries plus structure;
- only SimpleQA learning curves are shown for the five learned alternatives;
- baseline tuning budgets and validation policies are not comparably documented;
- verbalized confidence changes the prompt/trajectory treatment, whereas logprob methods do not;
- no simple task/dataset/model/difficulty baseline tests how much gain comes from configuration or item mix rather than uncertainty dynamics;
- no semantic or tool-state baseline tests whether logprob summaries add value beyond observable execution outcomes.

### Splits, tuning, and uncertainty

Appendix A.2.6 says five-fold stratified cross-validation is used, with an 80/20 train/validation split “within each fold,” and a 15-value regularization grid selected by a combined criterion that maximizes AUROC while minimizing Brier and ECE (p. 18). The combined rule is not formalized. There is no nested outer test fold described separately from hyperparameter selection. If the same folds choose regularization and report performance, results are selection-optimistic.

The paper alternates among one fixed random seed, fold standard deviations, “different random seeds,” and five experimental runs without a complete run identity. It does not report paired fold assignments across methods, item-clustered bootstrap intervals, statistical comparisons, or uncertainty for transfer matrices. For GAIA's 165 items, the origin of the very small GAC standard deviations is especially unclear because GAC is zero-shot and there is only one held-out validation set.

ECE is underspecified: the number of bins `M`, binning strategy, empty-bin handling, and confidence intervals are omitted. ECE can be unstable and prevalence-sensitive at these sample sizes. Brier score is a proper scoring rule but conflates calibration and discrimination; AUROC measures ranking, not probability calibration. Selecting across all three and then presenting metric-specific superiority further complicates interpretation.

## Evidence and results

### In-domain prediction

On the three headline datasets, HTC-Reduced reports ECE/Brier/AUROC of `.068/.140/.752` on SimpleQA, `.102/.213/.706` on GPQA, and `.031/.090/.644` on HLE (Table 1, p. 5). Full tables report favorable point estimates across all eight samples (Tables 4–5, pp. 19–20). This is credible evidence that the engineered representation is predictive under the paper's own folds and labels.

It is not evidence of perfect or decision-ready discrimination. HLE AUROC remains only about `.64`; GAIA direct-trained reduced AUROC is `.686`. A low ECE can coexist with poor separation if predictions sit near the base rate. The paper's claim that lower ECE and Brier are “objectively better aligned with true empirical accuracy” (p. 5) ignores label error, binning, selection, and intended decision loss.

### Cross-domain transfer

Transfer is strongly asymmetric (Table 2, p. 8; Tables 7–10, pp. 23–25). SimpleQA-Reduced transfers well to HotpotQA/StrategyQA but poorly to GPQA (`ECE .304`, `Brier .330`, `AUROC .629`). MMLU-Pro-Reduced transfers favorably to StrategyQA but catastrophically in ECE to HLE (`.504`) despite similar AUROC to direct training (`.645` versus `.644`). Full matrices contain many ECE values above `.3`, `.5`, or `.7`.

That is not “stable cross-domain calibration” (Appendix A.3.3, p. 20). It shows that rank information and probability scale can move independently and that source-target selection matters. The manuscript chooses two favorable source stories in the main text and then generalizes from a heterogeneous matrix without a predeclared transfer population, source-selection rule, or aggregate loss.

### General Agent Calibrator

GAC pools the seven non-GAIA datasets and evaluates on 165 GAIA validation items (Section 3.4, pp. 8–9). GAC-Reduced reports the best ECE (`.118`) but worse Brier and AUROC (`.245`, `.647`) than direct-trained reduced HTC (`.233`, `.686`). This is a useful ECE result for one held-out benchmark under one unresolved configured-system/label setup.

It does not demonstrate a universal reliability layer. GAIA is both the sole held-out benchmark and an author-chosen target after studying the other datasets; only 165 validation items are used; there is no second OOD benchmark, temporal replication, model/provider shift, task-family holdout, or external decision. “Plug-and-play” also conflicts with the grey-box logprob requirement and missing cross-provider feature equivalence.

### Ablation and “interpretability”

The pooled seven-dataset ablation reports all four feature families outperforming category subsets on 3,446 stated rows (Table 11, p. 26). Because datasets have different success rates, formats, trajectory lengths, and possibly configuration mixes, pooled random folds can reward dataset identity. A leave-one-dataset-out ablation would better test universal process signal.

Absolute logistic coefficients and selection frequencies show predictive association after scaling/tuning. They do not show the “signals behind failure,” causal importance, or actionable mechanisms. Correlated and duplicated features make coefficient ranking unstable; no standardization details, coefficient uncertainty, stability selection, perturbation, intervention, or failure-type labels are supplied. STRACE-style root-cause evidence requires state/action/tool dependencies and causal slices; HTC only predicts a final binary label.

## Theoretical claims audit

The theory describes Bayes-optimal predictors under assumptions, not the fitted finite-sample HTC implementation (Appendix A.6, pp. 31–33).

1. **Richer-feature dominance:** Proposition 1 assumes the last-step confidence sigma-algebra is contained in the 48-feature representation and compares Bayes-optimal conditional means. Even if that containment holds, it does not imply a regularized logistic model learned from a few hundred noisy labels will dominate a calibrated last-step model.
2. **Sparse generalization:** Proposition 2 gives a standard bounded-feature complexity result. The paper does not demonstrate the required feature bound, choose `B/R` from the bound, or connect it to calibration error under distribution shift.
3. **Compounding subgoals:** Proposition 3 assumes conditionally independent subgoal correctness and that last-step confidence exceeds the weakest subgoal probability. Neither is tested; the result is a toy inequality, not evidence that the observed feature map measures propagation.
4. **Online prefixes:** Proposition 4 assumes `sigma(phi_prefix_k)` is nested inside `sigma(phi_prefix_k+1)`. Recomputing aggregate means, extrema, entropy summaries, and first/last features on a longer prefix does not generally preserve the prior feature vector, so this nesting does not follow. More information exists in the raw longer trajectory, but not necessarily in the recomputed 48 summaries. No prefix model or early-intervention experiment repairs this gap.

The online-monitor, self-correction, RL-reward, and self-evolving-agent proposals in Appendices A.8/A.10 are therefore future hypotheses, not validated transfers.

## Unique insight

The strongest transferable insight is a **reliability evidence ladder whose links must not be collapsed**:

```text
trajectory signal
  → probability for a precisely versioned success predicate
  → held-out calibration and discrimination
  → transport to a declared target population/configuration
  → thresholded action under explicit loss and capacity
  → observed review workload, missed failures, accepted work, and harm
  → root-cause or professional-validity claim (only with separate evidence)
```

HTC supplies a candidate mechanism for the first prediction and some evidence for the second. It does not supply the remaining links.

A second key distinction is between three objects often called “reliability”:

1. **Observed repeat reliability:** how often the same configured system succeeds over independent attempts (Agent Reliability Profile).
2. **Predicted trial success:** a probability assigned to this attempt from its trajectory (HTC).
3. **Causal diagnosis:** the earliest supported cause of success/failure (STRACE and project root/surface records).

A calibrated predictor can be useful while being causally wrong; a repeat reliability estimate can be correct while unhelpful for triaging one run; a causal diagnosis can be correct without yielding calibrated probabilities. Preserve all three.

## Relation to existing project evidence

- **Agent Reliability Profile** measures empirical repetition, severity, recovery, and cost. HTC predicts a binary outcome from one trace and does not replace repeated attempts or tail estimates.
- **STRACE** tries to localize supported causes through structural dependencies. HTC's coefficients are associative failure predictors, not causal slices or root-cause labels.
- **Signals trajectory triage** separates enriched review yield from population prevalence. HTC scores could rank review queues, but selected rows could not estimate calibration, prevalence, or system reliability without a probability sentinel and inclusion ledger.
- **Many-Facet rater evidence** shows outcome labels and thresholds can be rater-conditioned. HTC collapses one opaque model-judge policy into binary truth and propagates its errors into calibration targets.
- **Validity and metric-monitoring contracts** already separate measurement, population, uncertainty, threshold/loss, action, and licensed claims. They are the correct implementation homes; a new calibration subsystem is unnecessary before an empirical decision study.

## Limitations and validity threats

1. Seven of eight populations are mostly static QA/reasoning rather than consequential long-horizon knowledge work.
2. Only GAIA centrally exercises heterogeneous agent tools and documents.
3. Exact benchmark releases, task IDs, sample seeds, dates, and exclusions are absent.
4. The declared seven-dataset counts imply 3,448 rows, while the pooled ablation reports 3,446 without explanation.
5. One trajectory per task appears to be used; repeated-run identity and stochastic reliability are unmeasured.
6. Model/framework/tool assignment by dataset is incomplete.
7. Endpoint versions, prompts, budgets, temperatures, stop/retry policies, tokenizers, and logprob request semantics are unpinned.
8. Web/search and environment states are not versioned.
9. The binary target mixes task difficulty, configuration, trajectory behavior, and grader error.
10. Gemini judge configuration and complete prompt are unreleased.
11. Human agreement evidence omits counts, strata, expertise, labels, adjudication, and uncertainty.
12. Raw agreement of 90–95% does not establish class-conditional oracle validity.
13. Exact-match versus judge usage by dataset is unclear.
14. GPQA open-ended conversion lacks an equivalence/normalization protocol.
15. Token logprob, confidence, top-1, and top-k transformations are underdefined.
16. “Attention” features normalize over token positions and are not model attention.
17. At least four of the nominal 48 feature dimensions are formula duplicates.
18. Undefined statistics are set to a valid value of zero rather than carrying missingness.
19. Structure features can proxy task, scaffold, budget, or answer format.
20. No task/dataset/difficulty-only baseline quantifies shortcut prediction.
21. No semantic action/tool/environment baseline separates logprob value from observable outcomes.
22. Learned baselines are evaluated deeply only on SimpleQA and have incompletely matched tuning budgets.
23. Verbalized confidence changes the agent prompt and is not a treatment-equivalent comparator.
24. The five-fold/80:20 protocol is ambiguous about outer test folds.
25. Hyperparameter selection and reported evaluation do not clearly use nested cross-validation.
26. The combined AUROC/Brier/ECE selection criterion is unspecified.
27. ECE bins, strategy, empty-bin policy, and uncertainty are omitted.
28. Fold/random-seed/run identities conflict across sections.
29. Item/task/configuration clustering is ignored.
30. No paired uncertainty or significance analysis accompanies method comparisons.
31. Transfer matrices show many severe probability-scale failures despite broad “stable transfer” language.
32. Source/target pairs and the GAIA holdout are author-selected rather than sampled from a declared transfer population.
33. GAC is tested on one 165-item held-out benchmark only.
34. GAC's best ECE coincides with worse Brier/AUROC than direct training, so “best reliability” is metric-dependent.
35. Coefficients and selection frequencies are treated as causal diagnosis without causal labels or intervention.
36. Feature scaling, coefficient uncertainty, and stability under correlated/duplicated features are unavailable.
37. Pooled random-fold ablation may exploit dataset identity rather than universal uncertainty.
38. Bayes-optimal theory does not establish finite-sample logistic HTC performance.
39. The online-prefix theorem assumes nested summary information that the feature map does not guarantee.
40. No online early-warning, abstention, escalation, self-correction, or reward experiment is performed.
41. Runtime analysis excludes trajectory generation, logprob access, labeling, storage of raw traces, and human review.
42. The method cannot support providers that withhold comparable logprobs.
43. Cross-provider logprob equivalence and tokenizer drift are untested.
44. No code, trajectories, labels, splits, configuration manifests, or GAC artifact are linked from inspected sources.
45. OpenReview reviews, decision, and accepted manuscript remained inaccessible; only the author's current venue claim was observed.
46. No evidence licenses professional validity, causal diagnosis, universal transfer, safety, production fitness, or readiness.

## Reproducibility and operational realism

Paper-level inspectability is moderate. The full v1 manuscript and source preserve the task counts, main metrics, transfer matrices, feature formulas/map, model class, regularization grid, broad cross-validation description, theory, selected examples, and CPU-time claims. The explicit feature map is more useful than a vague “trajectory encoder.”

Exact reproduction is poor. The source archive contains TeX, bibliography, and figures—not the “anonymized code base” claimed as supplementary (Reproducibility Statement, p. 10). The author's current publication page links only arXiv/PDF. A renewed GitHub/API search found no paper-linked HTC release; a broad `agentic-uncertainty` repository is a different, post-v1 project and was not treated as HTC evidence. Missing trajectories, labels, judge records, item IDs, split files, prompts, configs, implementation, and GAC weights make the tables unauditable.

Operational realism is low-to-moderate for the question and low for the validation. Predicting failure from completed traces is relevant, and the logistic model is inexpensive after signals exist. But most tasks are short answer benchmarks, only completed trajectories are evaluated, labels come from an underdocumented model judge, no review/abstention action is taken, and total generation/judging/human costs are absent. The reported millisecond overhead is feature-computation overhead, not cost of operating a reliable agent monitor.

## Transfer to skill-bench

### 1. Treat confidence as a typed derived observation

For each confidence record, bind:

- exact configured-system, task, environment, trial, attempt, and trajectory hashes;
- prediction time (`prefix` or `post_hoc`) and channels available at that time;
- target predicate and label authority/version;
- feature extractor, tokenizer/provider logprob semantics, missingness, scaler, calibrator, and training-population versions;
- raw score, calibrated probability, uncertainty, and applicable population boundary;
- prohibited interpretations, including correctness, root cause, professional validity, and safety unless separately evidenced.

Never overwrite the observed trial result or empirical repeated-run profile with a predicted probability.

### 2. Separate calibration, discrimination, transport, and utility

Report at least four ledgers:

- **calibration:** reliability curves, proper score, adaptive/binned diagnostics with bin policy and uncertainty;
- **discrimination:** rank/threshold metrics and class-conditional errors;
- **transport:** performance under held-out task family, system, model/provider, time, and environment shifts;
- **decision utility:** accepted failures, escalated successes, missed severe defects, reviewer workload, latency, and cost under a declared policy.

A lower ECE cannot by itself authorize escalation, acceptance, or deployment.

### 3. Evaluate a predeclared selective-action policy

A useful pilot should compare `review all`, `review none`, a simple observable baseline, and a trajectory-confidence policy under the same capacity. Predeclare:

- action set: accept, verify, retry, escalate, abstain;
- false-accept, false-escalate, delay, and review costs;
- severe-defect gates that override probability;
- review capacity and threshold-selection data;
- held-out evaluation population and clustered uncertainty.

Choose thresholds from expected loss/capacity on calibration data, then freeze them before test. Report workload and realized loss, not only ECE.

### 4. Use repeated attempts and equivalent forms

Cross the same task families with repeated seeds and configured-system versions. Distinguish:

- predicted success for one trajectory;
- empirical success frequency for the task/system cluster;
- within-task ranking of attempts;
- between-task difficulty shortcuts;
- calibration drift after model, scaffold, tool, rubric, or environment changes.

Use bridge items and recalibrate or fail closed after component drift.

### 5. Test signal ablations against semantic and observable state

Before adopting 48 logprob summaries, compare:

- task/configuration/difficulty-only features;
- trajectory length/token budget only;
- deterministic tool and artifact-state observations;
- semantic action/evidence checks;
- provider logprobs;
- combined models.

Plant near-neighbor failures: confident wrong evidence, low-confidence correct verification, long but valid work, premature short completion, provider/tool failure, grader defect, and alternative valid paths. Preserve surface observation versus earliest supported cause.

### 6. Fail closed on unavailable or incomparable logprobs

Record coverage and returned probability mass. Do not impute cross-provider equivalence. Treat tokenizer, endpoint, decoding, top-k truncation, missing logprobs, or extraction changes as instrument changes requiring bridge evidence. A model with no valid confidence channel should produce `insufficient_evidence`, not a synthetic zero or silently substituted verbal score.

## Concrete repository actions

1. **Add no new schema task.** Existing benchmark-bundle configured-component/trace records, metric-monitoring specifications, validity arguments, task health, rater evidence views, and longitudinal versioning can represent the needed boundary.
2. **Add one nonduplicate validation task:** exercise a trajectory-confidence selective-review policy on an existing or future diverse pilot with repeated attempts, a probability-sampled sentinel, frozen thresholds, explicit loss/capacity, simple/semantic baselines, and workload/missed-severe-defect outcomes. This is validation of existing machinery, not another calibration subsystem.
3. **During the next reliability consolidation, preserve the three-way separation** among empirical repeat reliability, predicted single-trial success, and supported causal diagnosis; cite this review's transfer-failure and decision-utility boundary.

## Action items completed

- [x] Read the complete immutable v1 PDF/text through Appendix A.11 and inspect the full arXiv source archive.
- [x] Reconstructed all eight benchmark samples, configured agents/models, label policy, 48-feature map, calibrators, baselines, split/tuning description, metrics, transfer, GAC, ablation, theory, and deployment claims.
- [x] Audited label authority, task/configuration dependence, clustering, repeated-run identity, split leakage, ECE specification, feature duplication/semantics, transfer selection, coefficient causality, and online-theory assumptions.
- [x] Retried OpenReview access and renewed author/GitHub release searches with explicit evidence boundaries.
- [x] Compared nonduplicatively with Agent Reliability Profile, STRACE, Signals, Many-Facet rater evidence, and existing validity/metric contracts.
- [x] Proposed one bounded empirical validation task and no duplicate schema subsystem.
