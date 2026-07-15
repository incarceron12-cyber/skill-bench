# AdaRubric: adaptive criteria are a candidate instrument, not an adaptive validity argument

- **Paper:** Liang Ding, *AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning*
- **Immutable version read:** arXiv:2603.21362v3, updated 10 May 2026, <https://arxiv.org/abs/2603.21362v3>
- **Date read:** 2026-07-15
- **Full-text evidence:** `data/papers/pdfs/2603.21362v3-adarubric.pdf` (12 pages; SHA-256 `4c328caeac7ef6027460da8b9ff4938eb64a156606a8787ca4f3de61fbdeed38`) and `data/papers/text/2603.21362v3-adarubric.txt` (66,667 bytes; SHA-256 `88b3672c400a04a8273d72c146a7cba7dae715ac5b6a190713736eb5458230bc`). The immutable API summary contains no withdrawal or retraction notice.
- **Metadata:** `data/papers/source/2603.21362v3-metadata.xml`.
- **Official release inspected:** paper-linked <https://github.com/alphadl/AdaRubrics>, pinned at commit `d16cd65944c190c1daa6a46e11ce8b104178b85e`, tree `d29931f323f980131bed4cf91395f2eb87f5caea`; archive `data/sources/releases/2603.21362v3-adarubric/alphadl-AdaRubrics-d16cd65.zip` (SHA-256 `72475440edb67e23fcacc87ceff5c8636f283d663ff7425fb319cee419a2d38f`); provenance `data/sources/releases/2603.21362v3-adarubric/provenance.json`.
- **Release timing boundary:** the pinned release postdates v3 by 28 days. Its bundled PDF is byte-identical to immutable v3, but commit `f3ce82b5b8b9a98336cea02ceb86f7b645720865` explicitly changed defaults to match the paper after v3. The archive is therefore a post-v3 implementation, not proven paper-time experiment code.
- **Tags:** adaptive-rubrics, trajectory-grading, LLM-as-judge, confidence-weighting, preference-learning, instrument-validity, release-drift

## One-sentence contribution

AdaRubric proposes a useful separation between task-conditioned criterion generation, step-by-dimension trajectory observation, and noncompensatory filtering, and reports higher aggregate human-score correlation and downstream training success than fixed-rubric baselines; however, the paper omits the item-level evidence needed to identify those effects, treats inter-run agreement as deployment validity, and its official implementation contradicts core paper claims about validation, call topology, confidence weighting, caching, multimodality, and reliability, so the evidence supports a candidate grading architecture rather than a reliable evaluator or reward mechanism.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through a cross-domain grader case, not a commitment to web agents or reward learning. The general uncertainty is whether an LLM can project a public task description into useful task-specific criteria and then use those criteria to produce trustworthy observations, decisions, or rewards.

AdaRubric is directionally right that a fixed Helpfulness/Fluency/Safety rubric is often irrelevant to goal-directed work. Its strongest reusable design move is the three-stage separation:

`task description → generated criterion set → trajectory observations → aggregation/filter/decision`

That separation creates inspectable places to test projection error, evidence-view insufficiency, observer error, and decision policy. But “adaptive” does not repair the authority chain. A criterion generated from model parametric knowledge can be relevant yet unauthorized, complete-looking yet omit a hard gate, or professionally plausible yet impose a hidden obligation. Reliability of repeated scores cannot establish criterion authority, correctness, consequence validity, or fitness for reward learning.

The release audit adds a sharper lesson: **paper-to-implementation correspondence is itself part of grader validity**. Here the released code operationalizes confidence as a score penalty rather than a statistical weight, performs one trajectory-wide call rather than `K×N` evaluator calls, and contains no empirical datasets or training scripts. A benchmark must hash and conformance-test the exact generator, rubric, observer, aggregation, filter, and reliability implementation used for every claim.

## Research question and claim boundary

The paper asks whether task descriptions can elicit task-specific evaluation dimensions from an LLM, whether step-level confidence-weighted scoring aligns better with human judgments than fixed rubrics, and whether filtered scores produce better DPO/PPO training signals (Sections 1 and 3, pp. 1–4).

The reported evidence supports, at most, these bounded descriptive claims:

1. In the author-reported aggregate tables, AdaRubric variants have higher Pearson correlation with the study's human score/rank target than the listed fixed-rubric and direct-judge baselines on sampled WebArena, ToolBench, and AgentBench trajectories (Table 1, p. 4).
2. The reported three-run score agreement is higher for AdaRubric variants than for listed baselines (Table 3, p. 4).
3. Under the un-released trajectory, pair-generation, training, and evaluation pipeline, models trained from AdaRubric-selected preferences have higher reported benchmark success/completion rates than the listed training baselines (Tables 2, 4, 7, 8, and 12, pp. 4–7 and appendix).
4. Five unspecified domain experts give generated dimensions high mean relevance, orthogonality, and completeness ratings on 60 tasks, though below the expert-designed rubric condition (Table 9, pp. 6–7).

The evidence does **not** establish:

- criterion-level equivalence to expert requirements;
- criterion authority, fair public basis, or professional validity;
- complete or orthogonal task coverage;
- decision equivalence at a consequential acceptance threshold;
- independent repeated-rubric stability, because the rubric-generation repeat topology is not reported;
- that the DimensionAwareFilter improves judgment rather than selecting an easier subset;
- causal reward quality or that training gains originate in rubric adaptivity rather than trajectory selection, compute, data composition, or evaluator leakage;
- cross-domain preference transfer rather than benchmark/configuration transfer;
- multimodal support “without modification” in the released implementation;
- deployment-grade reliability, production fitness, cost-effectiveness, or readiness.

## Methodology and system

### Task-conditioned rubric generation

A task is represented as instruction, domain, context, and expected tools/modalities. The generator asks an LLM for five dimensions, weights, and concrete 1–5 anchors. The paper defines validity as task relevance, semantic orthogonality, completeness, and calibration and says generated rubrics undergo cosine-distance, weight-sum, and five-level checks, with one retry and a domain-template fallback (Section 3.2, pp. 2–3).

The intended unit is unclear. The paper calls `R(T)` task-conditioned, says rubrics are generated “per task type,” and claims they are cached across a task family. The study does not define the equivalence relation that determines when two instructions share a rubric. This matters: instance-specific generation risks answer-conditioned or hidden-obligation criteria, while family caching risks underfitting task-specific requirements.

The release supplies a concrete prompt and model schema, but not the stated validation policy:

- `adarubric/generator/prompts.py` asks for dimensions “directly derived” from the task, but also injects one supply-chain search example into every default generation. This is a criterion prior, not neutral elicitation.
- `adarubric/generator/llm_generator.py` checks only duplicate dimension names and corrects `task_id`. It does not compute cosine distance, normalize or check weights within 1%, retry a semantically invalid rubric, or fall back to a domain template.
- `adarubric/core/models.py` requires all five anchor keys and positive weights, but permits one to ten dimensions and does not require weights to sum to one. The aggregator later normalizes arbitrary positive weights.
- The repository contains no cache. `AdaRubricPipeline.run` regenerates a rubric on every invocation unless the caller explicitly supplies one. Thus the paper/README claim of cached task-family rubrics and `>95%` generation-cost reduction is not realized or benchmarked in the pinned release.

More fundamentally, task relevance and completeness cannot be validated by dimension-name distance, weight arithmetic, and populated anchors. Those are structural checks. They do not test whether a mandatory requirement was omitted, whether two differently worded criteria depend on one event, whether an alternative valid path is admitted, or whether a threshold has a fair public basis.

### Trajectory evidence view and step scoring

The paper defines each trajectory step as `(thought, action, observation)` and says each step–dimension cell receives an ordinal score and confidence representing relevance (Section 3.3, p. 3). The released prompt sends the entire textual trajectory and all dimensions in one LLM request. It includes agent thoughts, actions, action inputs, and observations, but omits `Trajectory.final_answer`. It also has no authoritative environment state, artifact view, screenshots, source files, tool-state queries, or independent outcome oracle.

This evidence view creates several validity threats:

1. A final answer or artifact can be the primary outcome but is invisible to the judge.
2. Agent thoughts are untrusted self-reports that can anchor or mislead the judge.
3. Text observations can be stale, partial, or agent-controlled representations of environment state.
4. Every dimension is scored at every “applicable” step, but applicability is represented only by self-reported confidence; there is no explicit `not_applicable` or `insufficient_evidence` state.
5. Missing steps and dimensions are only logged. Unknown dimensions are dropped; absent dimensions can become zero at aggregation. Instrument invalidity is therefore convolved with substantive failure.

The paper states that evaluation costs `K×N` calls per trajectory—about 40 calls for WebArena—and Algorithm 1 depicts a model invocation per step and dimension (pp. 3 and 8/Appendix A). The released `LLMTrajectoryEvaluator` makes **one structured call per full trajectory** that requests every step–dimension score. This changes context competition, correlated errors, cost, latency, and call independence. No paper-time evaluation implementation or call log resolves which topology produced the tables.

### Confidence aggregation is internally inconsistent

The default paper equation computes:

`sum_k(score[k,j] × confidence[k,j] × recency_weight[k]) / sum_k(recency_weight[k])`

while Appendix B's BLUE argument instead describes normalization by the sum of confidence. The released `WeightedMeanAggregator` matches the former: it multiplies the score by confidence but does **not** include confidence in the denominator.

That is not ordinary confidence weighting. It treats low confidence/relevance as evidence of low quality. A direct execution against the pinned code produced:

- one score of `5` at confidence `0.2` → dimension/global score `1.0`;
- one fully relevant score of `5` plus one purportedly irrelevant score of `5` at confidence `0.1` → score `2.75`.

Thus adding an irrelevant but excellent step can turn an exemplary dimension into a failing one. The behavior directly conflicts with the prompt's instruction that confidence should be low when a step is not directly relevant. The test suite codifies this behavior (`tests/test_evaluator.py::test_confidence_weighting` expects `4 × .5 = 2`) rather than detecting it as a mismatch.

The paper's BLUE argument also assumes confidence is inversely related to noise variance. Confidence is generated by the same judge in the same call as the score; no independent calibration or causal evidence supports that interpretation. Appendix B reports a mild residual/confidence association, but gives no raw residuals, estimator comparison protocol, held-out split identity, clustered uncertainty, or calibration curve. Even a correctly normalized estimator would be only as meaningful as this unvalidated confidence channel.

### Aggregation and DimensionAwareFilter

Weighted mean, geometric mean, minimum score, absolute threshold, percentile, dimension-aware threshold, and composite filters are useful separable policies. Proposition 3.1 correctly states a simple algebraic fact: a positive weighted average can pass while one component is below its own threshold, whereas a conjunction of per-dimension thresholds cannot (Section 3.4, pp. 3–4).

The proposition does not establish that generated dimensions or thresholds are valid, independent, complete, or calibrated. It proves only that a conjunction enforces its own component thresholds. A spurious generated dimension can veto a legitimate trajectory; an omitted hard gate remains invisible; dependent dimensions can multiply one defect; and a universal default threshold of 2.5 has no decision-loss basis.

Table 1 reports higher human correlation for `AdaRubric-DA`, while Table 10 says DimensionAwareFilter retains only 61.5% of pairs. The paper does not state whether correlation is calculated on a common fixed trajectory set or only retained observations. If the filter removes cases according to the evaluator's own score vector, then correlation after filtering is an outcome-conditioned estimand and is not comparable to an unfiltered baseline. If DA denotes another operation, that operation is not defined. This ambiguity prevents attributing the reported `+0.05 r` to better measurement.

### Human targets and agreement

For human correlation, the paper says 300 randomly sampled trajectory pairs per benchmark are annotated by three annotators, with `κ > 0.82`, a written protocol, paired bootstrap tests, and average 95% Pearson intervals of ±0.02 (Section 4.1, pp. 3–4). Critical details are absent:

- source and generation of candidate trajectories;
- whether 300 pairs means 600 unique trajectories, overlapping pairs, or 300 trajectory records;
- annotator qualifications, assignments, independence, compensation, and benchmark-specific authority;
- whether annotators use generated, manual, or shared rubric dimensions;
- exact human target—ordinal score, pairwise rank, consensus, or adjudicated score;
- kappa variant and unit, disagreement distribution, adjudication, missingness, and criterion-level labels;
- bootstrap resampling unit and handling of shared tasks, trajectories, annotators, and pairs.

Pearson correlation tests linear co-movement of aggregate scores. It does not test bias, calibration, threshold agreement, severe omission, criterion confusion, or acceptance decisions. Because trajectories and pairs are nested within benchmark tasks and judged by the same configured evaluator, a trajectory-level bootstrap can materially understate uncertainty.

The separate rubric-quality study has five domain experts rate every dimension across 60 tasks on relevance, orthogonality, and completeness, reporting `κ=0.79` (Section 5.7 and Table 9, pp. 6–7). The paper does not identify expert domains, matching to tasks, rubric-generation repeats, rating anchors, blind/randomized presentation, reference rubric authorship, adjudication, uncertainty, or item-level omissions. Mean Likert similarity to an expert-designed condition does not establish that generated criteria encode the same obligations or decisions.

### Reliability topology

The paper applies Krippendorff's alpha across three independent evaluator runs and declares `α ≥ 0.80` a deployment criterion (Section 3.6 and Table 3, pp. 3–4). Three-run agreement can support a narrow repeated-observation stability claim if items, missingness, scale level, and run independence are correctly specified. It cannot establish accuracy, criterion validity, decision validity, safety, service reliability, or deployment fitness. Consistently wrong judgments can have alpha one.

The released reliability helper does not reproduce the reported benchmark analysis. `evaluate_consistency` repeats **one trajectory under one fixed rubric**, treats rubric dimensions as alpha “items,” and computes one global alpha across a runs × dimensions matrix. Dimension-level alpha is set to `1.0` only when run variance is numerically zero and otherwise to `NaN`. It neither repeats rubric generation nor estimates benchmark-level task/trajectory reliability. Different dimensions are treated as exchangeable items even though they represent different constructs and mean levels. The repository includes no empirical matrices to replay Table 3.

This is precisely the distinction highlighted by the Many-Facet review: repeat agreement, rater severity, task/criterion interaction, and decision validity are different estimands. AdaRubric reports only an aggregate repeat statistic and then overpromotes it to “deployment-grade.”

### Preference learning and downstream evaluation

The paper reports DPO results on three benchmarks, cross-domain transfer, SWE-bench Lite, multimodal extensions, and PPO training (Sections 4.3–5.6 and Tables 2, 4, 7, 8, and 12, pp. 4–8). These sections are too under-specified to identify a reward mechanism:

- no released trajectory corpus, rubric corpus, score matrix, pair dataset, train/dev/test manifest, training code, or model checkpoints;
- no trajectory-generating agent/harness configurations, attempt counts, seeds, invalid-run policy, or environment snapshots;
- no DPO sample counts, pair overlap/dependence, epochs, learning rate, batch size, optimizer, decoding configuration, or uncertainty across training seeds;
- no matched data-volume control after filters retain different fractions;
- no separation of rubric-generation, scoring, filter, margin, and pair-composition effects;
- no clustered confidence intervals or repeated training runs for success-rate deltas;
- no contamination audit for public benchmark tasks or model priors;
- no cost, token, latency, or human-review ledger beyond approximate evaluator calls and wall-clock multipliers.

The PPO account is internally inconsistent: Section 5.6 says the policy is trained “with ... 1,000 rollouts,” while Table 8 and Appendix D report outcomes at 1K, 3K, and 5K rollout steps. The paper does not explain whether these are cumulative rollouts, optimizer steps, or separate checkpoints.

The claimed multimodal extension is not represented in the release. `TrajectoryStep` stores text fields; the OpenAI-compatible client sends text chat messages; the evaluator prompt has no image parts, screenshots, renderer identity, or multimodal evidence model. An image might be pre-captioned into `observation`, but that is a modification and a different evidence view. Consequently, the post-v3 release cannot substantiate “without modification” VisualWebArena/OSWorld evaluation.

The release's `DPOPairGenerator` is generic score-gap plumbing. It does not require DimensionAwareFilter survivors, preserve trajectory text in `DPOPair`, implement DPO training, or capture the paper's experimental split. Its existence establishes implementability of pair IDs and margins, not reproduction of the reward-learning results.

## Evidence interpretation

### What is genuinely useful

1. **Task-conditioned criteria are a testable alternative to universal chat rubrics.** The paper correctly surfaces rubric specification as a major source of judge error.
2. **Criterion vectors should remain visible.** Per-dimension observations expose compensation that one scalar hides.
3. **Aggregation and gating should be explicit policies.** Weighted, geometric, minimum, and conjunction policies imply different error costs and should not be silently substituted.
4. **Rubric generation and trajectory evaluation are separate stochastic components.** They need separate repeats, versioning, and validity evidence.
5. **Generated criterion quality should be inspected by humans and downstream behavior.** The paper attempts both, even though its implementation is insufficient.
6. **Paper/release conformance can reveal hidden instrument changes.** Here it exposes differences that materially change the claimed estimator and operating cost.

### What the headline numbers do not show

- `r = 0.79` is aggregate score co-movement under an under-described human target, not criterion correctness or decision equivalence.
- `α ≈ 0.83` is reported inter-run agreement, not deployment validity.
- `+6.8–8.5%` downstream success is an author-reported package association without released data, seeds, uncertainty, or component identification.
- expert means around 4/5 are rubric-plausibility judgments without criterion-level authority, omission, threshold, or alternative-path adjudication.
- a per-dimension conjunction prevents arithmetic masking only for the dimensions and thresholds already admitted; it cannot validate them.

## Unique insight

AdaRubric exposes a **two-source instrument-variance problem** that aggregate judge studies often miss:

`task sample × trajectory sample × rubric-generation draw × judge draw × aggregation/filter policy × decision threshold`

The paper mostly fixes or leaves implicit the rubric draw and reports agreement across judge runs. But an adaptive-rubric system can be stable under one cached rubric while a regenerated rubric changes dimensions, weights, hard gates, or evidence demands. Conversely, regenerated rubrics may differ in wording while preserving decisions. Reliability therefore needs a crossed design:

1. hold trajectory fixed and repeat judgment under one rubric;
2. hold trajectory fixed and regenerate rubrics;
3. cross multiple rubric draws with multiple judge draws;
4. map generated dimensions to authorized reference obligations;
5. test criterion and decision behavior on legitimate alternatives, omissions, hard gates, invalid evidence, and threshold-near cases.

This separates at least six claims:

- **rubric adaptability:** dimensions change with disclosed task requirements;
- **criterion validity:** generated dimensions represent authorized obligations and fair consequences;
- **judge repeatability:** repeated observations under one instrument agree;
- **instrument repeatability:** regenerated rubrics preserve licensed measurement/decision behavior;
- **decision equivalence:** authorized and generated instruments make accept/reject/escalate decisions with bounded loss;
- **reward usefulness:** using the resulting preferences causally improves held-out behavior without unacceptable regressions.

Neither Pearson correlation nor alpha entails the next claim. This extends the completed generated-rubric meta-evaluation: that paper tests aggregate induced-score alignment across five repositories per paper; AdaRubric tests task-conditioned trajectory scoring and reward use. Both stop before criterion and decision validity. AdaRubric additionally shows why fixed-rubric/fixed-trajectory repeats cannot estimate adaptive-instrument variance.

## Comparison with existing project evidence

- **LLM-generated rubric meta-evaluation:** both studies use score correlation as evidence for generated rubrics. The prior review distinguishes criterion, measurement, and decision equivalence. AdaRubric adds a dynamic trajectory setting but supplies less inspectable empirical material and no criterion mapping; its adaptive generation therefore remains candidate nomination.
- **AgentRewardBench:** that study shows observer-view and predicate-specific error surfaces against preserved human labels. AdaRubric exposes thoughts/actions/observations but not authoritative state or final artifacts and provides no criterion-level confusion matrix. Its aggregate correlation cannot localize task, trace, rubric, judge, or aggregation error.
- **Many-Facet rater effects:** alpha measures repeat agreement only. It does not estimate rater severity, rubric-draw effects, task/criterion interactions, bridge stability, or decision error.
- **Criterion operating-envelope synthesis:** a criterion can be replayable in one environment without transporting or preserving decisions. AdaRubric does not preserve engine/environment, grader service date, task-family equivalence, threshold-loss basis, or bridge items; zero-shot/multimodal tables therefore do not establish transport.
- **ResearchRubrics and PaperBench:** those reviews preserve criterion provenance, hierarchy, dependencies, and local evidence. AdaRubric's flat generated dimensions have no source authority, requirement mapping, applicability, dependency, or hard-gate lineage.

The nonduplicate conclusion is that adaptive rubric systems need **crossed rubric-draw × observer-draw conformance plus criterion/decision adjudication**. A stable fixed rubric is not evidence that the adaptive generator is stable or valid.

## Limitations and validity threats

1. One-author report with broad experiments but no released empirical corpus, analysis package, training code, or checkpoints.
2. The 300-pair human sample's unit, overlap, trajectory source, and clustering are under-specified.
3. Human annotator qualifications, assignment, independence, rubric, target variable, and adjudication are absent.
4. Kappa variant and unit are not defined for either human study.
5. Pearson correlation does not test score bias, calibration, threshold agreement, severe errors, or decision loss.
6. Bootstrap resampling unit and dependence handling are not reported.
7. The DimensionAware correlation comparison may be conditioned on evaluator-selected survivors.
8. Task-to-task-type caching equivalence is undefined.
9. Rubric-generation repeat variance is not reported.
10. Criterion relevance, completeness, orthogonality, authority, dependency, and fair public basis are conflated.
11. Generated criteria can add hidden obligations from model priors.
12. Human rubric-quality means have no item-level omissions, confusion, uncertainty, or expert-task matching.
13. Self-reported judge confidence is not independently calibrated.
14. Paper confidence aggregation, Appendix BLUE rationale, and release implementation are inconsistent.
15. Low confidence/relevance lowers released scores rather than merely lowering evidentiary weight.
16. Agent thoughts can mislead the judge; final answers and authoritative environment/artifact state are absent.
17. Missing steps/dimensions and invalid observations are not represented with fail-closed typed states.
18. Paper `K×N` call topology contradicts the release's one full-trajectory call.
19. Paper validation/retry/fallback claims are not implemented in the pinned release.
20. Paper/README caching and `>95%` cost-reduction claims are not implemented or empirically supported.
21. The released reliability helper does not reproduce the paper's benchmark-level alpha analysis.
22. Alpha agreement is overpromoted to a deployment criterion.
23. No rater severity, task/criterion interaction, repeat-service drift, or decision-loss analysis is reported.
24. DPO/PPO trajectory generation, pair counts, split lineage, hyperparameters, and training seeds are missing.
25. Filtered methods can change data volume and composition without matched controls.
26. Training gains have no repeated-seed uncertainty or component-factorial identification.
27. Public benchmark and model-prior contamination are not audited.
28. SWE-bench correlation against a binary oracle is not human professional judgment.
29. Cross-domain results test a small benchmark set, not professional or domain transport.
30. Multimodal support is absent from the pinned text-only implementation.
31. PPO rollout accounting is internally inconsistent.
32. Approximate calls and wall-clock multipliers are not a total cost/latency/audit frontier.
33. Current release defaults were changed after v3 to match the paper, so paper-time code identity is unresolved.
34. Release tests are structural unit tests with mocked LLM responses; they do not validate empirical claims or paper conformance.
35. In the available project environment, 81 synchronous release tests passed, while 13 async tests could not execute because `pytest-asyncio` was not installed; creating an isolated dev environment was blocked by disk quota. This is an environment-bound verification limit, not evidence that those async tests fail.

## Reproducibility and operational realism

**Instrument inspectability is moderate.** The immutable PDF preserves equations, prompts at a conceptual level, aggregate tables, ablations, and limitations. The pinned release preserves 54 files, typed models, concrete prompts, aggregators, filters, reliability helpers, tests, a lockfile, and an exact post-v3 commit. Static code inspection and local execution reproduced the released confidence-aggregation behavior.

**Empirical reproducibility is weak.** The repository has no benchmark trajectories, generated rubrics, human labels, pair tables, run manifests, API responses, training scripts/configs, model outputs, checkpoints, statistical notebooks, or result-reproduction commands. The paper does not pin exact benchmark revisions, task IDs, agent/harnesses, environment images, GPT endpoint snapshot, evaluator request logs, or data splits. The bundled paper establishes authorship correspondence, not result correspondence.

**Operational realism is limited.** Multi-step trajectory evaluation, explicit criteria, filtering, and preference construction are realistic system components. But the released observer sees a textual self-report, not authoritative final artifacts or state; invalid evidence can become a score; criteria have no authority workflow; thresholds have no loss basis; model/service drift is not monitored; and no human escalation or task-health lifecycle is exercised. The system is alpha-stage grading plumbing, not a validated production evaluator.

## Transfer to skill-bench

### Retain

1. Generate or select criteria as a separately versioned stage before grading.
2. Preserve dimension-level observations rather than only a scalar.
3. Make aggregation, noncompensatory gates, and pair selection explicit, hashable policies.
4. Repeat both rubric generation and judgment; do not call either deterministic because temperature is zero.
5. Test generated rubrics intrinsically, behaviorally, and against downstream decisions.
6. Treat the exact implementation and call topology as part of instrument identity.

### Repair

1. A generated dimension must be a `candidate` with links to public requirement, source/expert authority, applicability, dependency, alternative path, required evidence, threshold, and consequence. Parametric plausibility confers no authority.
2. Replace confidence-as-penalty with explicit applicability/evidence states. If confidence weighting is retained, predeclare its estimand, denominator, calibration method, and missingness behavior.
3. Cross rubric draws and observer draws. Estimate rubric-selection, judge, task, trajectory, and interaction variance separately.
4. Use a common fixed artifact/trajectory set when comparing graders. If a filter changes eligibility, report selection and downstream utility separately rather than labeling post-selection correlation as evaluator accuracy.
5. Preserve final artifact/state and evidence-view admissibility. Agent thoughts are optional untrusted context, not authoritative evidence.
6. Validate hard gates and dimension thresholds against boundary cases and declared asymmetric loss.
7. Fail closed on missing steps, missing dimensions, invalid JSON, unavailable state, unsupported modality, and unpinned renderer/environment.
8. Factor generation, judge, confidence, aggregation, filter, pair margin, and training-data-volume effects; use repeated training seeds and clustered uncertainty.
9. Preserve total calls, tokens, latency, provider failures, cost, human review, and audit routing.
10. Require paper/release conformance tests before treating implementation artifacts as evidence for reported tables.

### Minimal validation design

Use two materially different knowledge-work artifact families and freeze a set of public requirements, authorized criteria, valid alternatives, and threshold-near artifacts. For each task:

- generate multiple rubrics under independently seeded/configured calls;
- map each candidate to authorized obligations as `preserved`, `omitted`, `spurious`, `split`, `merged`, `contradictory`, `threshold_shifted`, or `evidence-view_shifted`;
- cross every rubric draw with repeated judge calls on the same artifacts;
- include planted omitted hard gates, redundant compensating dimensions, not-applicable criteria, invalid evidence, misleading self-report, valid alternative paths, and final-artifact/trace disagreement;
- report criterion confusion, score bias/calibration, threshold agreement, severe-error loss, rubric and judge variance components, clustering, invalid burden, and total cost;
- only then test downstream preference training on held-out task families with matched data volume and multiple seeds.

This design can distinguish useful automated criterion nomination from criterion authority, repeatable observation, equivalent decisions, and causal reward utility.

## Concrete repository actions

1. **Index this review as release-audited under rubrics/graders.** It materially changes the grouped conclusion by adding crossed rubric-draw × observer-draw variance and exact implementation-conformance requirements.
2. **Do not add a parallel schema or build task.** Existing criterion provenance/dependency/applicability, artifact/evidence-view admissibility, configured grader identity, task health, metric monitoring, response matrices, and validity arguments are the correct homes. The generated-rubric calibration proposed by the prior review is still not ready without authorized expert criteria.
3. **When that calibration is scheduled, add one conformance case for confidence semantics and one for call topology.** A low-confidence not-applicable step must not silently lower substantive quality, and a one-call full-trajectory judge must not be compared with `K×N` independent calls as though they were the same instrument.
4. **No new queue item.** These are nonduplicate refinements to an already identified future calibration, not a new subsystem or currently executable expert-validated task.

## Action items completed

- [x] Read the complete immutable v3 PDF/text and verified the metadata has no withdrawal notice.
- [x] Inspected the complete 54-file official release at pinned post-v3 commit and established the bundled-PDF/timing boundary.
- [x] Reconstructed generation, evidence view, confidence aggregation, filtering, reliability, human studies, DPO/PPO, zero-shot, multimodal, cost, and limitations.
- [x] Executed the released confidence aggregation and preserved the exact counterexample results.
- [x] Compared with generated-rubric meta-evaluation, AgentRewardBench, Many-Facet rater effects, and criterion operating-envelope synthesis.
- [x] Mapped findings to existing contracts and added no duplicate build task.
