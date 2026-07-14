# Paper and Release Review: Stochastic Agent Evaluations — Repetition Is Essential, but the Released Ratio Is Not ICC(1,1)

- **Paper:** https://arxiv.org/abs/2512.06710v1
- **Authors:** Zairah Mustahsan, Abel Lim, Megna Anand, Saahil Jain, Bryan McCann
- **Date read:** 2026-07-14
- **Source read:** complete immutable arXiv v1, submitted 7 December 2025
- **Local PDF:** `data/papers/pdfs/2512.06710v1-stochastic-agent-evaluations.pdf` (11 pages; SHA-256 `ac948a4b9efb421fbff810c2af734268a5fa8dfe8369421bcf03f469de7fcc61`)
- **Local text:** `data/papers/text/2512.06710v1-stochastic-agent-evaluations.txt` (SHA-256 `bc10cbdc58860b799600418599dfe8ede475ae8ba1e36550f90b47d0d6acbbd0`)
- **Immutable source:** `data/papers/source/2512.06710v1-source.tar.gz` (SHA-256 `e6ee4a7cd7ceb1cec5dce89f187414eb3cc72068cb8219f02daf522fe855ddf0`)
- **Official release:** https://github.com/youdotcom-oss/stochastic-agent-evals, archived at commit `50bd2cec421320e51a042498a4fb7e8482a70fb5`
- **Release boundary:** the archived commit is dated 17 December 2025, ten days after immutable v1. It is an official review-time release, not demonstrated paper-time code; no tags or GitHub releases existed at acquisition.
- **Release archive/provenance:** `data/sources/releases/2512.06710v1-stochastic-agent-evals/youdotcom-oss-stochastic-agent-evals-50bd2cec.zip`; `data/sources/releases/2512.06710v1-stochastic-agent-evals/provenance.json`
- **Tags:** repeated trials, ICC, reliability, binary outcomes, clustered uncertainty, missingness, replication budgets, configured systems

## One-sentence contribution

The paper correctly makes repeated task-level trials and variance visibility first-class evaluation requirements, but its paper equations and released analyzer compute the variance of finite-trial task means without removing sampling error and then label the resulting ratio ICC(1,1); this is not the stated one-way random-effects ICC estimator, makes the “ICC convergence” curve partly an estimator artifact, and—together with silently omitted release failures, mutable configured systems, an unvalidated stochastic judge, and no formal stopping rule—blocks the claimed universal `8–16`/`≥32` repeat budgets, sub-agent replacement rule, and deployment-reliability interpretation.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, and C through **expansion with immediate validation relevance**. The repository's repeated cross-pilot matrix is blocked before model calls, so the useful question is not whether to repeat trials—it should—but what each repeated design can estimate and how a repeat budget should be frozen.

The paper's strongest general lesson survives the statistical defect: one run per task cannot reveal whether an aggregate score is stable, whether failures recur on the same tasks, or whether provider/environment/grader events dominate variation. Its strongest headline prescription does not survive: a benchmark-relative ICC is not an intrinsic “agent consistency” property, and the released ratio cannot determine a transferable repeat count.

GAIA and FRAMES are methodological cases rather than a scope commitment to QA or retrieval. The reusable hypothesis is cross-domain: repeated knowledge-work trials should distinguish persistent task/system difficulty, within-form stochastic outcome variation, environment and service failures, grader variation, and uncertainty in the suite-level decision.

## Research question and permissible claim

The paper asks how stochasticity in agent evaluations should be quantified, whether stability varies with task difficulty and model capability, and how many trials are needed. It reports repeated binary success labels for GAIA and FRAMES and proposes accuracy, confidence intervals, ICC, between-query standard error, and run metadata on an Evaluation Card (Sections “Recommended Statistical Protocols,” “Experiments,” and “Evaluation Cards,” pp. 3–7).

The full source and release support these bounded findings:

1. the retained configured-system runs show substantial within-query binary variation;
2. the distribution of task-level success frequencies differs across the retained GAIA levels and FRAMES configurations;
3. a single aggregate accuracy omits diagnostically useful task-by-repeat structure;
4. increasing repeated observations changes finite-sample variance estimates, especially on small GAIA Level 3;
5. release artifacts are sufficient to reproduce several published point estimates exactly under the released missing-data and ratio implementation.

They do **not** establish that the reported statistic is ICC(1,1), that higher reported ICC makes an accuracy improvement genuine, that `8–16` or `≥32` trials is a transferable stopping budget, that one sub-agent is operationally more reliable, that scorer variance is minimal, or that any system is professionally valid, production-reliable, safe, or ready for deployment.

## Methodology and system reconstruction

### Task populations and sampling

GAIA uses all 165 validation questions: 53 Level 1, 86 Level 2, and 26 Level 3. FRAMES contains 824 test questions, but the main comparison uses 50 questions said to be sampled with `random_state=42`; deep research uses 100 FRAMES questions. Main GPT-4o-search and GPT-5-search runs use 64 attempts per question; o4-mini-deep-research uses eight because of cost (Datasets and Evaluation Scope, pp. 4–5; Appendix C, p. 10).

The official release confirms the GAIA 165×64 matrices for GPT-4o-search and GPT-5. It also preserves an 824-question GPT-4o-search FRAMES matrix, a 50-question GPT-4o matrix, a 50-question GPT-5-search matrix, and several smaller/deep-research artifacts. The exact 50 question IDs from the GPT-4o file select the matching rows from the 824-question search file and reproduce the paper's GPT-4o-search Table 3 values. The release does not preserve result matrices for every Table 3/5 model, and current runner scripts are edited examples rather than immutable manifests of every reported run.

Task sampling is only one hierarchy. GAIA levels and FRAMES reasoning categories create mixtures; questions may share sources or retrieval infrastructure; all attempts share provider endpoints and a short October 2025 time window. Neither paper nor release models source, category, provider-time, or batch clustering.

### Configured agents and execution

The paper names GPT-4o-search-preview, GPT-4o, GPT-5 with web search, o4-mini-deep-research, Claude 4.5 Sonnet/Haiku, Gemini 2.5 Pro, Qwen3-235B-A22B, and DeepSeek-v3p1, with evaluation conducted in October 2025 (Appendix C, p. 10). Prompts request short final answers; search-enabled endpoints query live external information.

The release exposes more implementation detail but less control than the prose implies:

- model aliases are not immutable endpoint snapshots;
- ordinary OpenAI calls use a 120-second timeout, while deep-research background calls use a 300-second client timeout and poll every 100 seconds;
- `run_model_inference` retries up to three times with delays/backoff;
- trial/query pairs execute through ten threads, coupling attempts to shared service load;
- no per-attempt random seed is passed to model APIs, despite the proposed Evaluation Card's “trials & seeds” field;
- temperature is omitted/provider-default rather than frozen explicitly;
- the GPT-5 path uses the Responses API with web search, while other models use different API paths;
- no token, latency, usage, or cost record is retained in trial schemas.

These are repeated configured-service observations, not controlled draws from model sampling alone. Shared outages, caches, index updates, endpoint routing, retry behavior, and judge calls can correlate attempts.

### Outcome and grader

Every retained output is judged once by o4-mini against the question and ground-truth answer using a TRUE/FALSE structured prompt (Evaluation Scope and Appendix B, pp. 5 and 9–10). The paper acknowledges no formal validation of inter-trial scorer consistency and merely expects scorer variance to be minimal (Limitations, p. 7).

That expectation is unsupported. A stochastic, mutable model judge contributes to within-query variance and can turn a fixed candidate output into different labels. No deterministic equivalence layer, repeated-judge study, human sample, confusion matrix, adjudication, or judge version/date is supplied. The release parser also defaults an unparseable string response to `FALSE`, while structured API failures become missing metrics. Agent variation and observer variation therefore are not identified separately.

### Missing, invalid, and service-failed runs

The paper says failed runs—including timeouts and unrecoverable errors—were recorded as incorrect to reflect deployment conditions (Evaluation Scope, p. 5). The release does something else. Inference or evaluation exceptions produce `metrics=None`; `compute_statistics`, variance decomposition, and ICC routines skip those rows.

This is empirically material:

- the released GPT-5 GAIA matrix has one inference failure, leaving one Level-3 question with 63 scored attempts;
- the 824-question GPT-4o-search FRAMES matrix has 113 metric errors;
- among the 50 Table-3 FRAMES questions, eight attempts have `metric error: Connection error.` and are omitted;
- the deep-research GAIA files contain large, overlapping missing/error patterns, yet the paper reports a single accuracy and ICC without a separate availability denominator.

Thus the paper's intended “failure-as-zero” estimand and released reported estimand differ. Service availability, valid-trial rate, substantive success conditional on validity, and unconditional operational success must be separate.

## What the paper calls ICC

### Stated model

The manuscript states a one-way random-effects model

`Y_ij = μ + α_i + ε_ij`

and identifies ICC(1,1) as `σ_b² / (σ_b² + σ_w²)` (Recommended Protocol and Appendix E, pp. 3–4 and 11). For a balanced design with `k` attempts, the classical one-way ANOVA estimator is:

`ICC(1,1) = (MS_between - MS_within) / (MS_between + (k - 1) MS_within)`.

Equivalently, the between-task variance component removes `MS_within/k` from the observed variance of task means.

### Implemented estimator

Paper Equation 7 and release `eval_runners/analyzer.py` instead calculate:

1. `between = sample variance(task means)`;
2. `within = pooled sample variance within tasks`;
3. `reported ratio = between / (between + within)`.

The task-mean variance still contains within-task sampling noise of approximately `within/k`. It is not an estimate of the random task-effect variance. The release's unequal-trial path pools within variances by degrees of freedom but does not correct between variance for unequal precision.

This defect has four consequences.

1. **Low-repeat inflation.** If every task has the same true success probability `p`, there is no persistent between-task effect. Yet expected variance of task means is about `p(1-p)/k`, so the paper's ratio is approximately `1/(k+1)`, not zero.
2. **Manufactured downward “convergence.”** As `k` increases, finite-trial noise disappears from task means, mechanically lowering the numerator. The paper calls the downward curves “regression to the mean”; much of that pattern is exactly the unremoved sampling term.
3. **Wrong zero-variance behavior.** If every task succeeds on every attempt, repeatability is perfect but both variances are zero; the release returns ICC `0.0`.
4. **Thresholds lose their stated meaning.** Clinical heuristic cutoffs such as `.50` or `.75` cannot be attached to this different ratio, especially for binary outcomes and changing task populations.

At 64 repeats the numerical difference from classical ICC(1,1) can be small because `within/k` is small. That does not rescue the convergence or stopping-rule interpretation, which is precisely about small `k`.

### Binary outcomes and population dependence

Even correctly estimated ICC is population-relative. It rises when the task set contains a wider mixture of near-always-fail and near-always-pass items, without any change in per-task behavior. It can fall when tasks are homogeneous or a stronger system moves many items toward the same success frequency. Adding easy and hard anchors can increase ICC mechanically.

For binary outcomes, `p_i(1-p_i)` also makes within-task variance depend on task success probability: near-zero and near-one tasks look stable, while tasks near `.5` look variable. A high ICC can therefore mean a polarized difficulty mixture, not broadly predictable behavior; deterministic failure contributes as strongly as deterministic success. Comparing ICC across models changes both the system and the induced task-probability distribution, so “consistency independent of accuracy” is not identified.

## Reproduction audit

I parsed the complete retained JSONL matrices directly and recomputed task means, pooled within-task variances, the released ratio, and balanced one-way ANOVA ICC where applicable.

| Released slice | Valid structure | Accuracy | Variance of task means | Pooled within variance | Released/paper ratio | Classical ICC(1,1) |
|---|---:|---:|---:|---:|---:|---:|
| GAIA L1, GPT-4o-search | 53×64 | 0.227005 | 0.100141 | 0.078448 | **0.560734** | 0.557699 |
| GAIA L2, GPT-4o-search | 86×64 | 0.232013 | 0.119419 | 0.061107 | **0.661506** | 0.659706 |
| GAIA L3, GPT-4o-search | 26×64 | 0.066106 | 0.019186 | 0.043975 | **0.303759** | 0.296102 |
| FRAMES 50, GPT-4o | 50×64 | 0.381563 | 0.171178 | 0.069301 | **0.711823** | 0.710519 |
| FRAMES 50, GPT-5-search | 50×64 | 0.773125 | 0.088481 | 0.090099 | **0.495469** | 0.491460 |

The bold values reproduce Tables 2–3 to rounding. This confirms that the published “ICC” is the release ratio, not merely an imprecise description of an unseen correct implementation.

The FRAMES GPT-4o-search reconstruction is especially revealing. Selecting the same 50 qids from the 824-question release yields accuracy `0.6353918651` and ratio `0.7355544556`, exactly the paper's `63.54%` and `0.7355`, **only when eight metric connection errors are omitted**. Treating those errors as incorrect, as the paper says, gives accuracy `0.6340625` and ratio `0.7314058264`.

The retained full FRAMES GPT-4o-search matrix also has 824 questions and a different ratio (`0.756838`), while the paper labels the reported result as `n=50`. This demonstrates how strongly the ratio depends on the chosen task distribution.

## Convergence and repeat-budget audit

The paper reports ratios at 2, 4, 8, 16, 32, and 64 trials, visually declares stabilization around `8–16` for GAIA Levels 1–2 and `≈32` for Level 3, and presents those values as data-driven resampling budgets (Experiments, pp. 5–6).

The claim is not operationally reproducible:

- no convergence tolerance, loss function, precision target, sequential stopping rule, or held-out validation criterion is defined;
- the released bootstrap samples attempts without replacement but does not resample tasks in the trial-count curve, so its percentile band describes subset sensitivity conditional on the exact task set, not population uncertainty;
- no random seed is set in the analysis functions, making bootstrap summaries non-reproducible;
- at all available attempts, every without-replacement resample is identical, so the “bootstrap CI” collapses even though task-population and service-time uncertainty remain;
- only 100 resamples are used for 2.5/97.5 percentiles;
- trial subsets reuse one October run matrix and cannot test temporal/provider drift;
- the uncorrected numerator makes low-`k` values systematically too high;
- the study inspects the curve after observing it and performs no second-matrix confirmation.

The reported `8–16` and `≥32` counts are therefore descriptive waypoints for these task/configuration matrices under this flawed statistic, not transferable budgets. A repeat budget must be derived from the target decision: precision of mean success, probability of recurrent severe failure, per-task success-frequency precision, paired treatment effect, rank stability, or a reliability component all require different designs.

## Accuracy and agent-comparison inference

The manuscript's Equation 3 uses `sqrt(p(1-p)/(Tn))`, treating all task-attempt outcomes as exchangeable Bernoulli draws. Repeats from one task are clustered and have different success probabilities, so that formula is generally inappropriate. The release's main statistics instead form a t interval over task means, which at least keeps tasks as the top-level unit; the implementation and manuscript estimands disagree.

McNemar's test is recommended for two agents on the same items, but repeated attempts make “one paired binary label per item” ambiguous. Valid comparison should preserve a matched task/form/system matrix and cluster over task, with service/invalid outcomes declared prospectively. The paper reports no paired agent-difference intervals or tests despite saying such tests are required.

Most importantly, the claim that accuracy improvement is trustworthy **only if ICC also improves** is false. A paired hierarchical estimate can support a genuine mean improvement while ICC falls because the stronger system changes the task-success distribution. Conversely, ICC can rise through deterministic failure or a more polarized task mixture without capability improvement. Mean effect, repeated-outcome heterogeneity, and operational decision loss are separate estimands.

## Evidence and substantive results

The retained response matrices do show heterogeneous repeat behavior. On GAIA Level 3, GPT-4o-search's released accuracy is about `.066` and its ratio about `.304`; GPT-5's is about `.442` and `.629`. On the selected FRAMES questions, GPT-5-search has higher mean accuracy but a lower ratio than GPT-4o-search. These are useful descriptive examples that mean performance and the shape of task-level success frequencies need not move together (Tables 2–3, pp. 6–7).

The stronger interpretations do not follow:

- “70% of observed variance is trial-to-trial randomness” treats a descriptive ratio as identified causal source attribution;
- “true capability” is not a random task effect and is not isolated from live search, service, retries, or judge variance;
- “GPT-5 is not just more capable but more reliable” compares a changed configured system and changed induced task distribution;
- “deployable improvement” has no deployment population, threshold, severity model, cost, or consequence evidence;
- deep-research comparisons use one agent, only eight intended repeats, substantial release missingness, and no uncertainty suitable for architecture claims.

The budget-allocation observation that more distinct tasks usually improve precision of a suite mean under a fixed call budget is useful. But the paper's example variance ratio is not empirically justified as typical, and optimizing suite-mean precision is not the same as estimating per-task recurrence, tails, severe failures, or ICC.

## Unique insight

The most important transferable insight is that **“reliability” is not one repeated-run number; the repeat design must be keyed to a decision and a variance source**.

For `skill-bench`, preserve at least this ladder:

```text
trial ledger with every intended attempt
  → service availability and trial validity
  → observer/grader repeatability
  → per-task/form outcome distribution and severe-failure recurrence
  → task-population mean and heterogeneity
  → paired configured-system or intervention contrast
  → decision rule, threshold, cost/loss, and operating envelope
  → professional, safety, or readiness claim only with separate validity evidence
```

ICC, even correctly estimated, answers only a population-conditioned variance-ratio question. It does not replace success probability, paired effects, grader reliability, calibration, root-cause diagnosis, or decision utility.

A second insight is an **anchor sensitivity test** for any proposed reliability scalar. Recompute after:

1. adding/removing deterministic easy and hard items;
2. stratifying by task/form family and difficulty;
3. preserving the same tasks while changing attempts;
4. preserving attempts while changing missing/service policy;
5. repeating the grader on fixed outputs.

If the scalar changes because the task mixture widened while per-task behavior did not, it must be labeled benchmark-population-relative rather than agent-intrinsic.

## Limitations and validity threats

1. The paper's variance-of-task-means ratio is not the stated ICC(1,1) estimator.
2. Between-task sampling error is not removed, biasing low-repeat ratios upward.
3. Unequal attempts are handled only in pooled within variance, not in between-component estimation.
4. Zero total variance is hard-coded to ICC zero, including all-success perfectly repeated matrices.
5. Binary outcome variance depends on success probability.
6. ICC is task-population- and difficulty-mixture-dependent.
7. Cross-model ICC comparisons change the induced task-probability distribution.
8. Deterministic failure increases the stated “reliability.”
9. Clinical heuristic ICC thresholds are imported without validation for this statistic or use.
10. The convergence criterion is visual and post hoc.
11. Bootstrap attempt subsets do not capture task-population uncertainty.
12. Bootstrap analysis has no fixed random seed and only 100 iterations.
13. At maximum attempts, without-replacement subset bands collapse mechanically.
14. No independent matrix validates the chosen repeat waypoints.
15. The `8–16`/`≥32` budget claim is configuration-specific, not transferable.
16. Equation 3 ignores within-task clustering and task heterogeneity.
17. Paper and release confidence-interval implementations differ.
18. No paired uncertainty/test is reported for model accuracy differences.
19. GAIA Level 3 has only 26 tasks, limiting between-task estimation.
20. FRAMES main results use an author-selected 50/824 subset.
21. FRAMES task/source and GAIA level/category dependence are unmodeled.
22. Attempts share providers, APIs, search indexes, timing, and threaded execution.
23. No model-call seeds are passed despite “trials & seeds” reporting guidance.
24. Mutable model aliases and web search block exact configured-system replay.
25. Temperature, task order, concurrency, and decoding settings are not fully frozen.
26. Retry behavior changes the unit from one call to an attempt-with-up-to-three-calls.
27. Service failures, retries, and substantive errors are not separated in reported denominators.
28. The paper says failures are incorrect; release analyzers silently omit missing metrics.
29. Exact reproduction found omitted connection errors in the published FRAMES slice.
30. Deep-research release matrices contain substantial missingness.
31. One stochastic o4-mini judgment per output confounds agent and grader variation.
32. Judge repeatability, human validity, class-conditional error, and adjudication are absent.
33. Unparseable string judgments default false while API errors become missing, creating asymmetric invalid handling.
34. Release artifacts do not cover every reported model/result.
35. Current scripts contain overwritten model assignments and settings inconsistent with some retained files.
36. No requirements file is present despite README installation instructions.
37. No total calls, tokens, latency, or monetary cost is reported or retained.
38. Evaluation Card “between-query SE” is not clearly defined or implemented as proposed.
39. The claimed typical variance ratio used in budget analysis is unsupported.
40. Accuracy plus ICC does not establish causal capability improvement.
41. No deployment exposure population, failure severity, threshold, or loss model exists.
42. No evidence licenses professional validity, production reliability, safety, or readiness.

## Reproducibility and operational realism

Paper-level inspectability is moderate: immutable v1 provides the model family names, task counts, broad timing, binary judging prompt, equations, tables, and limitations. Release-level inspectability is unusually useful because complete JSONL matrices preserve qids, trial numbers, prompts, outputs, judge explanations, labels, and many error fields. That allowed exact reconstruction of multiple published results and detection of the estimator and missingness discrepancies.

Exact replay is poor. The official commit postdates v1, is untagged, and lacks exact immutable manifests for all experiments, dependency pinning, all result matrices, seeds, endpoint snapshots, costs, and dataset revisions. Live web/search and proprietary serving state are gone. Current runner scripts are mutable examples; for instance, `frames/run_frames_evals.py` assigns `inference_model_name` twice, while `gaia/run_gaia_evals.py` currently requests five deep-research trials rather than the main 64-trial runs.

Operational realism is mixed. Real API retries, web search, timeouts, connection failures, and repeated model-judge observations are relevant deployment phenomena. But they are pooled into one binary score or omitted rather than attributed, and the task populations are answer-oriented benchmarks rather than consequential professional artifacts. The release is best treated as a valuable repeated-response dataset for auditing measurement choices, not an operational reliability certificate.

## Transfer to `skill-bench`

1. **Keep the blocked repeated matrix frozen.** This review does not justify bypassing its required push/authentication gate. Resume `build-cross-pilot-repeated-task-matrix` only after the exact frozen commit is pushed.
2. **Define the repeat estimand before calls.** For each matrix, state whether repeats estimate suite-mean precision, per-form success frequency, recurrent severe failure, grader stability, paired intervention effect, or temporal/service drift. Do not use one count for all.
3. **Preserve every intended attempt.** Report intended, service-available, execution-valid, grader-valid, and substantively successful denominators separately. Predeclare whether unconditional operational success counts service failures as zero; never silently drop them.
4. **Use clustered/hierarchical inference.** Keep task, form, family, configured system, time/batch, and grader identifiers. Estimate task-level heterogeneity and paired effects with task-clustered intervals; do not treat `n×T` cells as independent.
5. **Do not adopt the released ratio.** If a variance component is needed, use a documented estimator appropriate to balanced/unbalanced binary repeated measures, report uncertainty and boundary behavior, and retain raw per-task frequencies. Call it ICC only if its form/model/unit and assumptions are correct.
6. **Choose repetition adaptively only under a frozen rule.** Predeclare precision/loss targets, minimum and maximum attempts, stopping statistic, alpha/error spending if sequential, and behavior under missing/service events. Validate the rule on a held-out matrix before reusing it.
7. **Repeat observers on fixed artifacts.** A small crossed grader study should separate output variability from evaluator variability before attributing within-task variance to the agent.
8. **Run anchor and missingness sensitivity.** Report estimates by task family/difficulty and under predeclared operational versus capability denominators. Do not compare reliability scalars across changed task mixtures without bridge analysis.
9. **Keep claim ceilings strict.** Repeated internal synthetic tasks can validate launcher, ledger, grader, and estimator behavior. They cannot establish professional capability, production reliability, safety, or readiness.
10. **Add no duplicate queue task.** The existing blocked repeated cross-pilot matrix, task-health, metric-monitoring, configured-system, grader, and validity machinery are the correct implementation homes. The evidence refines that work rather than requiring another schema or model-call task.

## Action items completed

- [x] Read the complete immutable v1 PDF/text through Appendix E.
- [x] Inspected the complete 100-file official release at a pinned post-v1 commit with timing boundaries.
- [x] Reconstructed task sampling, configured systems, repeat design, judge, failure policy, variance equations, ICC claims, convergence procedure, and Evaluation Card.
- [x] Audited binary-outcome, hierarchy, unequal-repeat, shared-service, difficulty-mixture, missingness, grader, cost, and temporal/provider threats.
- [x] Recomputed multiple released results and established that published values use the released non-ICC ratio.
- [x] Reproduced the published FRAMES GPT-4o-search result and demonstrated its silent exclusion of eight connection-error judgments.
- [x] Compared the contribution with Agent Reliability Profile, Agentic Confidence Calibration, and the blocked repeated cross-pilot matrix.
- [x] Mapped nonduplicate implications to existing machinery and added no redundant task.
