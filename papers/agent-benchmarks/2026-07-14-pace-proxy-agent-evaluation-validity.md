# PACE: cross-instrument proxy prediction is a sentinel, not an agent evaluation

- **Primary source:** Yueqi Song et al., *PACE: A Proxy for Agentic Capability Evaluation*, immutable arXiv v2, 6 July 2026, https://arxiv.org/abs/2607.02032v2
- **Full-text evidence read:** `data/papers/pdfs/2607.02032v2-pace.pdf` (26 pages; SHA-256 `0af39b8c953f0a432735e00f1ea0cf9fa6eb631a643c421fa4d616f0d838fa7b`) and `data/papers/text/2607.02032v2-pace.txt`
- **Official code audited:** https://github.com/neulab/pace at paper-time commit `7f1fd4cc37ecfab8d7517779c37e274500a7cf16` (16:40:27 UTC, 38 minutes before the v2 update) and post-v2 acquisition commit `dc2ef80e00addd519e7d8479f875cc3ecb46c6cb`
- **Official dataset audited:** https://huggingface.co/datasets/neulab/pace-bench at revision `ce177cfe25bc8c8259cadecb56d4db8d9d36ab18`
- **Release provenance:** `data/sources/releases/2607.02032v2-pace/provenance.json`; the complete 26,940-entry Git tree manifest, all core PACE scripts and selections at both code revisions, and all four dataset JSONL files are preserved locally. The repository contains about 16.8 GB of uncompressed blobs, mostly raw model outputs, so vendored benchmark copies and raw outputs were manifest-audited rather than duplicated.
- **Date read:** 2026-07-14
- **Evidence status:** full immutable paper read; official paper-time code and pinned dataset inspected and computationally audited. The paper is a submission in progress, not a peer-reviewed result.
- **Tags:** proxy evaluation, cross-instrument validity, agent benchmarks, nested validation, benchmark cost, response matrices, drift

## Why this matters for skill-bench

PACE asks a valuable operational question: can a cheap panel of static items forecast the mean score that a model would receive on an expensive agent benchmark? On 14 contemporary models and four OpenHands-index target score matrices, its selected atomic-item panels correlate well with held-out-model aggregate scores. That supports a bounded claim: **within this model family, target version, source pool, and harness frame, a fitted proxy can be a low-cost screening signal for when to run the full suite.**

It does **not** establish that atomic items substitute for agent evaluation, that selected items identify causal agent capabilities, or that the proxy is safe for routing or deployment decisions. More seriously, the released headline path is not a clean nested leave-one-model-out estimate: it searches thousands of hyperparameter combinations against the same 14 held-out outcomes it reports, and its “global” SVD basis includes the held-out model’s source-score row despite the paper saying otherwise. The paper also provides no uncertainty intervals, family-holdout, scaffold-holdout, temporal validation, residual diagnostics, or decision-loss study.

For `skill-bench`, PACE should therefore become a **proxy → sentinel → periodic full-suite** operating pattern, never a replacement instrument. A proxy may triage routine model/configuration candidates after it has been calibrated against full knowledge-work runs; full-suite sentinels must detect drift, rare-skill reversals, safety failures, and diagnostic loss.

## One-sentence contribution

PACE selects cheap static source items and fits their model-response patterns to forecast four expensive agent-benchmark aggregate scores, showing a potentially useful screening mechanism while leaving cross-instrument construct equivalence unestablished.

### Research question and scope

The research question is explicit: can performance on cheap, non-agentic evaluations predict performance on expensive agentic benchmarks? PACE differs from within-benchmark compression: it selects columns from a separate source instrument and learns a mapping to each target benchmark’s mean score (paper §§1–2, pp. 2–4).

The concrete contribution has two parts:

1. **PACE**, a source-item selection and regression procedure combining target-relevance (“Local”) and leverage-times-relevance (“Global”) selections.
2. **PACE-Bench**, a released materialization of the fitted `C=100` panels for GAIA, SWE-bench Verified, SWE-bench Multimodal, and SWT-Bench.

This cross-instrument move is the paper’s genuinely new and important idea. Efficient Benchmarking reduces the number of tasks *inside* an agent benchmark; PACE asks whether another, cheaper instrument can forecast the expensive score at all. That shift also makes validity harder: preserving one target aggregate does not preserve the target construct, task-level failures, workflow evidence, or consequences of use.

## Methodology reconstructed

### Evaluation frame

The study uses 14 models: three Claude configurations, GPT-5.2 and GPT-5.2-Codex, two Gemini 3 previews, DeepSeek V3.2, GLM 4.7, Kimi K2/K2.5, MiniMax M2.1/M2.5, and Qwen3-Coder-480B-A35B-Instruct (paper §4.1, p. 6; release `scripts/pacebench/config.py:25-31`).

The four target matrices are:

- GAIA: 165 instances;
- SWE-bench Multimodal: 102;
- SWE-bench Verified: 500;
- SWT-Bench: 430.

The paper says all target results come from OpenHands Index under the OpenHands Software Agent SDK (§4.1, pp. 6–7). This is a configured-system frame, not a model-only capability frame: target outcomes depend on the OpenHands harness, tool policy, environment versions, budgets, and benchmark grading. Those component versions are not enumerated in the paper.

The candidate source pool contains 19 evaluations covering 11 author-assigned capability categories. The paper’s Table 1 lists 59,714 nominal source instances; the reproducibility checklist reports an SVD over a 14 × 44,238 matrix (p. 22), implying filtering or unavailable model-item cells that the main method does not reconcile with Table 1. Source scores are produced through `lm-evaluation-harness` or benchmark-specific code (§4.1, p. 6).

### Selection

For each target and training-model fold, PACE computes item-wise absolute Spearman correlation between source-item scores and target mean scores. “Local” ranks by this target relevance. “Global” multiplies target relevance by an SVD leverage score. A split `q` assigns an initial budget to both paths, and overlap is filled until their union contains `C` unique source columns (paper §3.2, pp. 5–6; release `selection.py:48-137`).

This is supervised feature selection over models: every item’s relevance is estimated from only 13 training model points in each nominal leave-one-model-out fold. The capability labels are not inputs to selection; they are attached afterward at benchmark level.

### Prediction

For absolute score prediction, the implementation embeds selected source columns into low-rank Local and Global spaces, computes Spearman-weighted one-dimensional projections, fits one-dimensional OLS, and mixes the two predictions (`regression/absolute.py:23-27`). Pairwise prediction fits a logistic/Bradley–Terry-style model to source-score differences (paper §3.1, pp. 4–5).

The target-instance bootstrap draws 300 resamples of target columns, applies the same resampled columns across training models, tiles each model embedding 300 times, and pools the resulting labels (`bootstrap.py:24-44`). This changes the fitted objective, but it does not create 300 independent model observations and is not used to produce prediction intervals.

### Validation and reported evidence

The paper labels the protocol “strict LOOCV”: one of 14 models is held out, selection and regression use the other 13, and predictions are collected over 14 folds (§4.1, p. 7). At `C=100`, Table 2 reports:

| Target | MAE | Spearman | pair accuracy |
|---|---:|---:|---:|
| GAIA | 5.77% | 0.79 | 83.33% |
| SWE-bench Verified | 2.09% | 0.67 | 78.54% |
| SWE-bench Multimodal | 2.23% | 0.89 | 85.39% |
| SWT-Bench | 5.12% | 0.89 | 90.11% |
| **Macro average** | **3.80%** | **0.81** | **84.37%** |

The bootstrap ablation improves average MAE from 4.57% to 3.80% and Spearman from 0.66 to 0.81 (Table 3, p. 9). The budget sweep ranges from 25 to 500 items; MAE is best at 400, while pair accuracy is best at 500 (Appendix D, p. 17). Lasso and Ridge baselines overfit more strongly than PACE (Appendix E, pp. 17–18).

These are useful point estimates. They are not accompanied by error bars, confidence intervals, repeated splits, model-family holdouts, or external replication; the paper itself answers “No” to the statistical-significance checklist item (p. 22).

## Unique insight

### 1. Cross-instrument prediction can be operationally useful without construct equivalence

The observed model response matrix has enough shared low-dimensional ordering that cheap static items forecast four expensive aggregate scores reasonably well in this narrow frame. This is useful for screening because the decision “is this candidate obviously noncompetitive?” requires less evidence than “can this agent perform realistic knowledge work?”

This distinction is the key transfer. Proxy usefulness is a property of a **specified prediction target and candidate population**, not evidence that the proxy measures the target construct. `skill-bench` can exploit the former without pretending the latter.

### 2. A high aggregate correlation can coexist with diagnostic reversal

SWE-bench Verified’s selected panel is dominated by VisualWebBench and VisualPuzzles, even though the target is text-only repository repair (paper §5.1 and Appendix C, pp. 8 and 16). The authors interpret this as frontier-model discrimination after direct coding capabilities saturate. A more defensible interpretation is narrower: these items are correlates of model ordering in this 14-model sample. They do not show that multimodal understanding causes SWE-bench success or that the proxy preserves code-localization, patching, testing, or recovery failures.

The release therefore demonstrates why `skill-bench` must keep score prediction, construct interpretation, and diagnosis separate. A proxy can rank systems while entirely reversing which tasks or capabilities appear important.

### 3. Proxy maintenance is a lifecycle problem, not a one-time compression

The source and target response populations, harness, benchmark versions, and model families all define the mapping. The paper acknowledges calibration-set and static-source-pool drift (Appendix F, p. 19), but does not operationalize it. The correct design object is not a timeless “lite benchmark”; it is a versioned proxy calibration with explicit validity period, sentinels, residual monitoring, and retirement triggers.

## Release audit and reproducibility

### Paper/release correspondence

The latest public code commit before arXiv v2 is `7f1fd4c…`; the next two commits occur after v2, ending in `dc2ef80…` with message `planbench fix`. Core PACE code, README, config, and released selection CSVs are byte-identical between the preserved paper-time and latest snapshots; the later commit affects upstream evaluation machinery. The Hugging Face dataset revision predates v2 by about 33 minutes.

The release is unusually inspectable in one respect: it publishes the core selection/regression code, per-target selection weights, and four runnable proxy datasets. The full Git tree manifest contains 23,930 blobs and about 16.8 GB of uncompressed content, including standardized matrices and raw outputs. Re-running upstream evaluations would nevertheless require many proprietary model endpoints, mutable benchmark dependencies, OpenHands target records, and benchmark-specific credentials; the repository is not a cheap independent replication package.

### Materialized panel audit

The official selection CSV and dataset contain 412 rows:

| target file | rows | unique `(benchmark, subdir, instance_id)` | unresolved content |
|---|---:|---:|---:|
| GAIA | 100 | 100 | 1 |
| SWE-bench Verified | 100 | 100 | 3 |
| SWE-bench Multimodal | 105 | 100 | 2 |
| SWT-Bench | 107 | 100 | 1 |

Rows above 100 represent Local/Global path overlap with separate coefficients; the union remains 100. Seven rows cannot be reconstructed from current upstream datasets. That is direct evidence of source-version drift before any future-model drift is considered.

The dataset card’s “distinct instances” counts (80/97/96/100) group on bare `instance_id`; this collapses legitimate ID collisions across source benchmarks. Its prose first advises grouping by `instance_id` alone, while its usage code correctly groups by both `instance_id` and `source_benchmark` (`dataset/README.md:90-95, 105-110, 142-146`). Consumers following the prose can silently merge different items. A proxy release needs a globally unique source-instance key and an executable duplicate/weight aggregation rule.

### The released validation is not fully nested

This is the most consequential audit finding.

1. The README’s reproduction command uses `--auto-tune --strict-budget` (`README.md:54-62`).
2. Task A’s strict auto-tuner evaluates `q × nc_h × nc_d × m`; with the released default grids this is up to 11 × 10 × 10 × 11 = 12,100 configurations per target, before budget choice.
3. Each candidate produces nominal leave-one-model-out predictions, but `_autotune_task_a*` then selects the best configuration by comparing those predictions with **all 14 target outcomes** (`cli.py:463-501` and following).
4. The selected configuration’s same 14 predictions are reported as LOOCV performance. Frozen configuration comments explicitly say they were found by exhaustive sweep (`config.py:48-58`); Task B pinned configurations are “tuned on LOMO pair accuracy” (`config.py:104-113`).

The item selection inside each fold excludes the held-out target label, but hyperparameter/model selection does not. A defensible estimate requires nested validation: for each outer held-out model, tune all selection, rank, mixture, regularization, and budget hyperparameters using only inner folds among the remaining models; then evaluate once on the outer model. With only 14 models and thousands of candidate configurations, this omission can materially inflate reported performance.

### The “Global” SVD is transductive despite the paper’s claim

The paper says the held-out model “is not in the SVD decomposition” and is projected afterward (§3.2, p. 5). The released CLI instead computes `Vt_full = svd(X_v)` once on the complete source matrix before LOOCV (`cli.py:93-114`) and passes that basis into every Global fold. The selection code calls this “non-leaky” because it uses only `X` (`selection.py:140-147`).

Using the evaluated model’s source-score row without its target label is transductive rather than target-label leakage, and deployment does make that row available. But it contradicts the paper’s inductive description and weakens the “unseen model” claim: the representation itself has seen the held-out model. An inductive test should recompute the source SVD on the 13 outer-training models and project the held-out row afterward. Both transductive and inductive estimands may be useful, but they must not be conflated.

## Limitations and validity threats

### Statistical and sampling limits

- **Four targets, one target-harness ecosystem.** All targets use OpenHands-index results; three are software-engineering benchmarks. There is no harness holdout, embodied/office/production target, or human-evaluated professional artifact target.
- **Fourteen correlated frontier models.** Several are versions from the same provider/family. Leave-one-model-out does not test a held-out family, architecture, training regime, scaffold, or future time period.
- **Hyperparameter multiplicity.** Thousands of configurations are selected on 14 outcome points without nested validation.
- **No uncertainty.** The target-instance bootstrap is used as pooled training augmentation, not to report uncertainty over models, target items, source items, hyperparameter selection, or pairwise decisions.
- **Dependent pair metric.** Pairwise accuracy reuses model pairs across folds and directions; percentages are not independent Bernoulli trials.
- **No residual diagnostics.** The paper does not report which model families or targets are systematically over/under-predicted, calibration slopes, prediction intervals, or out-of-domain flags.

### Construct and diagnostic limits

- The target is the mean score of a particular benchmark/harness version, not “agentic capability” as a general latent trait.
- Benchmark-level capability labels are many-to-many and nearly all selected items inherit instruction-following and reasoning labels. Selection counts therefore cannot identify causal or unique skills.
- Aggregate prediction can hide task/check/slice reversals, rare catastrophic failures, side effects, unsafe actions, artifact defects, and workflow breakdowns.
- Static source calls omit interaction, long-horizon state, recovery, environment manipulation, handoffs, and professional artifact conventions by construction. Correlation does not show those constructs are dispensable.
- A proxy optimized for mean absolute error or rank can be particularly bad at threshold decisions near a deployment or routing cutoff; no decision-loss analysis is supplied.

### Operational realism and cost limits

The roughly 100× claim compares marginal proxy inference with target subsampling at matched plotted quality using estimated per-instance Claude Sonnet 4.5 costs (Table 1; Figure 1). It does not amortize the initial full target runs for 14 calibration models, scoring 44,238 valid source columns, benchmark setup, proprietary endpoints, failed runs, proxy refresh, or sentinel full suites. Nor does it price the consequences of a false routing or readiness decision.

PACE-Bench is public and weighted, so direct optimization and contamination are straightforward; the paper acknowledges gaming (Appendix F, p. 19). Seven unresolved released items and a post-v2 PlanBench fix already demonstrate mutable-source burden. The release’s broad upstream-license inheritance also makes redistribution and commercial operation more complex than the “minutes of static evaluation” framing suggests.

## Comparison with existing `skill-bench` evidence

### Versus Efficient Benchmarking

`papers/agent-benchmarks/2026-07-09-efficient-benchmarking-ai-agents.md` studies **within-target** task reduction and finds rank can remain stable when absolute scores degrade. PACE studies **cross-instrument** prediction. Both support rank-first routine screening and periodic full recalibration, but PACE adds a stronger construct-substitution risk: its selected items can be unrelated in surface and workflow to the target.

Efficient Benchmarking’s middle-difficulty panel tries to preserve target response information. PACE’s relevance filter tries to exploit covariance across a small model population. They should be separate panel types with separate validity arguments and drift tests.

### Versus Agent Psychometrics

`papers/agent-benchmarks/2026-07-09-agent-psychometrics.md` predicts task-level outcomes from task artifacts and decomposes model/scaffold effects. PACE predicts benchmark-level means from another response instrument. Agent Psychometrics can support difficulty and task-level diagnosis; PACE loses that granularity. Both are observational and cannot turn correlated features/items into causal capability explanations.

For `skill-bench`, task/check-level psychometric models are the safer source of diagnostic adaptation; PACE-style cross-instrument panels are only an operational screening layer above immutable configured-system records.

## Transferable design: proxy → sentinel → periodic full suite

No new schema family is required. Existing response-matrix, configured-system, metric-monitoring, task-health, and validity-argument machinery can represent the following bounded policy.

### 1. Define the proxy claim before fitting

A proxy record must bind:

- exact source item/check IDs, graders, versions, visibility, costs, and weights;
- exact target suite, target aggregate, harness/tools/environment, grader, and time window;
- calibration model/configuration population and family/provider clusters;
- intended use: triage, full-suite scheduling, or low-stakes rank screening;
- explicitly excluded uses: capability certification, professional validity, safety, readiness, and autonomous routing;
- loss function and abstention policy, not only MAE/correlation.

### 2. Use honest outer validation

At minimum:

- outer leave-one-family/provider-out and temporal-forward folds;
- all source-item selection, SVD fitting, hyperparameters, mixture weights, budget, and threshold selection nested inside each outer fold;
- inductive SVD as the primary estimate, with transductive results labeled separately;
- cluster-aware intervals over model families and target tasks/checks;
- residual and calibration plots by family, scaffold, domain, artifact type, failure root, and score region.

Fourteen models are insufficient for confident routing thresholds. If data are scarce, report the proxy as exploratory and widen abstention rather than optimize a larger grid.

### 3. Preserve diagnostics with sentinels

Every routine proxy run should include a small immutable sentinel set sampled from the **real target instrument**, stratified to retain:

- rare expert traps and safety-critical gates;
- long-horizon state/recovery requirements;
- artifact-view and provenance checks;
- known proxy-residual outliers;
- domain and work-shape coverage;
- previously saturated and newly difficult checks.

A proxy score may schedule a full run; it may not overwrite sentinel failures. Any critical sentinel failure triggers the full suite and invalidates capability/readiness inference.

### 4. Periodically run the full suite and monitor transport

Run a predeclared full-suite sample on a cadence determined by candidate volume and risk, and always after:

- a new model family/provider or scaffold/tool/memory/skill configuration;
- target/source/grader/environment version change;
- proxy residual or interval breach;
- rank reversal near a decision threshold;
- source-panel saturation, missing items, contamination, or unresolved content;
- sentinel failure or new failure root.

Update proxy weights only as a new immutable version. Never rewrite old predictions. Track cost including calibration and full-suite refresh, then compare against the loss from false accept/reject and missed diagnostics.

### 5. Keep the claim ceiling explicit

A valid proxy result can support: “this configured system is predicted, within this calibrated population and interval, to obtain target aggregate X; schedule/skip one low-stakes full run under policy Y.” It cannot alone support claims about agentic capability, professional-quality work, safety, production fitness, routing benefit, or deployment readiness.

## Concrete repository actions

1. **Consolidation:** add cross-instrument proxies as a distinct operating object in `docs/benchmark-design-taxonomy.md`, separate from within-suite reduced panels and adaptive task selection. Include calibration population, nested-validation status, transductive/inductive status, decision loss, sentinel coverage, and retirement triggers.
2. **Validation using existing machinery:** when `skill-bench` has enough full configured-system response matrices, run a retrospective comparison of (a) within-suite mid-difficulty panel, (b) task/check-level psychometric prediction, and (c) cross-instrument proxy. Predeclare family/time outer folds and measure aggregate error, pair reversals, critical-gate recall, root-cause/slice coverage, abstention, and total lifecycle cost.
3. **Do not build a new proxy schema now.** The available evidence is a 14-model exploratory correlation study with non-nested tuning and transductive representation leakage. Existing metric, validity, task-health, and configured-system contracts are the appropriate implementation homes until empirical `skill-bench` response data reveal a non-overlapping contract gap.

No new queue task is added: these actions are consolidation/validation refinements to existing benchmark-operation machinery, and creating a proxy subsystem before full cross-domain response matrices exist would optimize infrastructure ahead of evidence.

## Claim ledger

| Claim | Evidence supports? | Boundary |
|---|---|---|
| PACE predicts the four studied target means for these 14 model records with the reported point metrics | Partially | Paper tables support the calculation, but tuning is not nested and Global SVD is transductive |
| Cheap static items can be useful screening signals | Yes, bounded | Only for this calibration population, target/harness versions, and low-stakes use |
| The selected items measure the target’s agentic capabilities | No | Correlation and benchmark-level labels do not establish construct equivalence or causality |
| Capability allocation plots diagnose what each target uniquely requires | No | Labels are overlapping and post hoc; odd cross-modal selections show discrimination, not causal requirement |
| The proxy is about 100× cheaper operationally | Partially | Marginal per-candidate estimate; excludes calibration, full-suite acquisition, refresh, setup, failures, and decision loss |
| PACE generalizes to genuinely unseen model families/scaffolds/time periods | No | Only leave-one-record-out among 14 related models; no family/scaffold/temporal holdout |
| PACE can replace realistic knowledge-work evaluation | No | It does not preserve artifacts, workflows, safety gates, task-level diagnostics, or professional validity |
| PACE supports routing or deployment decisions | No | No threshold, abstention, utility/loss, or prospective routing study |
