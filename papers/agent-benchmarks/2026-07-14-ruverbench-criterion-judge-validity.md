# Paper Review: RuVerBench — Criterion-Level Judge Reliability Under Long Outputs

- **Paper:** https://arxiv.org/abs/2606.29920v1
- **Authors:** Yangda Peng, Yunjia Qi, Hao Peng, Haotian Xia, Guanzhong He, Xintong Shi, Richeng Xuan, Songyuanyi Lu, Yixian Liu, Zhichao Hu, Yuhong Liu, Lei Hou, Bin Xu, Juanzi Li
- **Date read:** 2026-07-14
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, 29 June 2026
- **Local PDF:** `data/papers/pdfs/2606.29920v1-ruverbench.pdf` (17 pages; SHA-256 `dd80a9824904ab20b0410361fe10307529b687c5923068371bf71be45cbfd990`)
- **Local text:** `data/papers/text/2606.29920v1-ruverbench.txt` (SHA-256 `75e3744069fc8273b82cb9fe3f3fe83f76247e07a0a40d7edb31a528ade6ffc9`)
- **Official release inspected:** https://github.com/THU-KEG/RuVerBench/tree/4e2992e3fa85448b4ba7a85741b65e09e4bec016 (commit `4e2992e3fa85448b4ba7a85741b65e09e4bec016`; tree `0fe1b0b63734e499cac7ea65e663a921886b8570`; corrected post-v1 snapshot)
- **Release provenance:** `data/sources/releases/2606.29920v1-ruverbench/provenance.json`
- **Tags:** llm-judge, rubric-verification, long-context, human-annotation, batching, self-voting, clustered-measurement, release-audit

## One-sentence contribution

RuVerBench turns 2,458 human-labeled criterion decisions over 284 deep-research reports and 210 coding trajectories into a direct meta-evaluation of LLM judges, usefully showing large domain-, category-, prompt-, batching-, and vote-dependent error surfaces; but its verifiability-conditioned rubric selection, shared answer-bearing criteria, unqualified “gold” adjudication, output-level dependence, absent uncertainty, and aggregate-only result release mean it validates configured agreement with one annotation policy—not portable judge reliability, professional quality, or autonomous grading fitness.

## Why this matters for skill-bench

RuVerBench addresses a measurement-layer question that `skill-bench` cannot evade: even if a benchmark has an explicit rubric, **can the configured observer determine whether one criterion was met from the evidence it receives?** The paper improves on holistic judge comparisons by making the unit of judgment an individual criterion and by using long reports and tool-rich coding trajectories rather than short chat answers (Sections 1 and 3, pp. 1–4).

Its strongest evidence is diagnostic rather than endorsing. The best reported Deep Research judge reaches `94.7` average category-balanced accuracy, while the best Agentic Coding judge reaches `89.4`; the released aggregate audit implies 91 and 70 wrong criterion labels respectively for those top systems. Prompt wording can move some weaker coding judges by more than ten points, batching can lose tens of points, and different high-scoring judges make different errors (Tables 2–3 and Figures 5–6, pp. 5–8). A rubric does not become a trustworthy grader merely because a strong model can read it.

The deeper lesson is that “judge reliability” belongs to a **criterion-instance observer transaction**:

`criterion policy × applicability × artifact/trace evidence view × prompt and call topology × model endpoint × parser/invalid policy × label authority × target population`.

RuVerBench varies several of these dimensions but often interprets the result as a model property. For `skill-bench`, the evidence instead supports versioning the whole transaction and licensing only a bounded concordance claim.

This advances charter objectives A–C through a cross-domain measurement case. Deep research and coding are stress substrates, not a proposal to narrow the benchmark to either domain.

## Research question and claim boundary

The paper asks:

1. How accurately do current LLMs classify whether a long agentic output satisfies one rubric?
2. How does reliability vary by domain and normalized criterion category?
3. How do prompt strictness/flexibility, multi-rubric batching, and repeated self-voting change agreement with adjudicated human labels?
4. Do similarly scoring judge models fail on the same criteria?

The paper and release support bounded claims that:

- the authors assembled 1,615 Deep Research and 843 Agentic Coding binary criterion labels over 494 scored outputs;
- on those fixed outputs, tested judge configurations differ materially by domain and criterion category;
- prompt realization changes positive and negative recall in different directions;
- large coding batches often underperform single-criterion calls in the exported fixed-subset summaries;
- majority voting can reduce some stochastic errors, but gains are model- and domain-specific and non-monotonic;
- aggregate judge scores conceal different false-positive/false-negative profiles.

They do **not** establish that adjudicated labels are objective truth, that the selected criteria represent professional-quality requirements, that long context causes the domain gap, that one judge is generally reliable, that batching itself causes every exported delta, that three to five votes reliably improve every model, that the results transfer to unreleased tasks or evidence views, or that any judge is fit for autonomous reward, monitoring, capability, professional-validity, production, safety, or readiness decisions.

## Methodology and system reconstruction

### Source tasks, outputs, and the true sampling unit

Deep Research combines rubrics and prompts from ResearcherBench, ResearchRubrics, and DeepResearch Bench II. It uses released OpenAI Deep Research and Gemini 3 Pro answers where available; ResearchRubrics answers are newly generated through Tongyi Deep Research using MiniMax 2.1 or Kimi 2.5 (Section 3.1 and Appendix A, pp. 3, 11–12). Agentic Coding uses OctoBench tasks, rubrics, scaffolds, Docker environments, and tool configurations, with trajectories generated by GPT-5.2, GLM-5.1, Kimi K2.5, and MiniMax 2.1.

The manuscript reports 2,458 “instances,” but these are **criterion decisions nested in 494 outputs**, not 2,458 independent agent executions. The local release audit found:

- 1,615 Deep Research criteria nested in 284 scored reports, with 1–20 criteria per report (median 4.5; mean 5.69);
- 843 Agentic Coding checks nested in 210 trajectories, with 1–11 checks per trajectory (median 4; mean 4.01);
- 298 packaged Deep Research records, of which 14 lack final taxonomy and are excluded from scoring;
- 217 unique packaged coding trajectories, of which 210 match scored cases and seven are extra unscored records.

The report or trajectory is therefore the minimum dependence cluster. Criteria from one output share the prompt, generator, content, source benchmark, evidence omissions, and often related requirements. Treating criterion rows as independent would overstate precision and effective sample size.

The paper says generated outputs record generator identity, prompt, and decoding configuration (Appendix A, p. 11). The public benchmark files do not expose those fields per output: Deep Research response records contain only `id`, `question`, and `response`; coding trajectory metadata contains `max_tokens`, `session_id`, and `biz_id`. The coding task file preserves scaffold identity, but output-generator assignment and decoding lineage are not recoverable from the released rows.

### Rubric filtering changes the construct

The authors manually inspect source rubrics, remove criteria that are subjective, unverifiable from available context, dependent on missing external information, multi-condition, or duplicated, and then downsample for evaluation cost while preserving source/category coverage (Section 3.2 and Appendix A, pp. 3–4, 11). This is sensible for obtaining labelable items, but it conditions the benchmark on **cheap observer verifiability**.

Consequently, RuVerBench does not sample the full rubric population faced by realistic knowledge work. It preferentially excludes precisely the criteria likely to require external evidence, plural professional judgment, dependency reasoning, or consequence assessment. A high score estimates agreement on the post-filtered criterion population; it cannot justify replacing experts on the excluded population.

The release exposes no pre-filter counts, rejected-rubric manifest, downsampling code, inclusion probabilities, source-by-stage funnel, or category-assignment protocol. The normalized taxonomy is single-label even when criteria require several abilities. Its reliability is not reported. Local inspection illustrates the boundary: a causal-relation criterion containing “1994” is classified as `numbers`, and criteria requiring correct program names are classified as `format`. These labels may be useful coarse slices, but category differences cannot be treated as clean latent verifier abilities.

### The criteria often contain the expected answer

Deep Research judges receive only the question, generated report, and criterion—not the underlying sources. Many `facts`, `logic`, and `numbers` criteria state the exact fact or conclusion that should appear. The resulting task is generally **criterion-coverage or entailment verification**, not independent factuality verification. A judge can match an answer-bearing criterion to the report without determining whether either is true in the world.

Coding judges receive serialized tools and messages and are instructed to inspect assistant messages, internal `reasoning_content` where available, and tool calls (Appendix C, pp. 13–15). They do not receive an independently queried repository state or functional execution result as part of the judge prompt. Some task-completion predicates may therefore remain under-observed even when a trajectory narrates success. Internal reasoning is also a variable evidence channel: it can reveal intent, leak hidden policy cues, or be absent across generator/scaffold configurations.

Thus the two domains use materially different observer views and criterion semantics. Deep Research primarily checks answer-bearing textual coverage; Agentic Coding checks trajectory behavior, hidden reasoning, and tool messages. The lower coding score cannot be attributed to length alone.

### Human annotation and adjudication

For each domain, the authors recruit four or five candidate annotation teams, select the highest-pilot-accuracy team, provide additional training, answer questions, and update the guideline. A hired team and an “independent internal group” then label all final criteria separately. They agree on 90.44% of criteria with Cohen’s `κ = 0.808`; every disagreement is rechecked and adjudicated (Section 3.2 and Appendix B, pp. 4, 12). Total labor is about 500 person-hours.

This is stronger than single-label annotation, but several validity boundaries remain:

- the source and authority of pilot labels are not described;
- selecting teams on pilot accuracy and revising the shared guideline optimize agreement with the authors' policy, not external construct validity;
- “independent” applies to the two final label passes, not to guideline creation, source rubric lineage, or adjudication;
- adjudicator identities, number, blinding, decision rule, rationale, uncertainty, and changed-label lineage are absent;
- only undergraduate education is guaranteed; coding annotators need technical English/Python/Linux/tool knowledge, but no domain-professional qualifications are reported for 35 Deep Research domains;
- hired/internal BAcc against adjudicated labels is partly circular because adjudication was produced by rechecking their disagreements;
- annotator-level labels, guideline, pilot records, rationales, and adjudications are not released, so the reported agreement and label authority cannot be independently audited.

The final labels are useful adjudicated observations under a shared policy. Calling them “gold ground truth” overstates their authority.

### Judge configurations and prompts

The main benchmark evaluates 18 hosted or open-weight model families. Appendix Table 7 specifies thinking mode and maximum output tokens, but the experiment lacks a complete immutable trial manifest: exact endpoint realization, API date per run, provider revision, request/response IDs, retry history, token use, truncation, invalid outputs, and raw predictions are not released (pp. 12–15).

Single-criterion prompts differ by domain. Deep Research asks whether a response “adequately covers” a criterion and emphasizes semantic equivalence. Agentic Coding uses `success`/`fail` and instructs the judge to inspect all assistant messages, reasoning, and tool calls. The strategy study adds “strict” or “flexible” suffixes, batches criteria into keyed JSON, or samples nine temperature-1 judgments for nested majority votes (Section 4.4 and Appendices C–D, pp. 7–8, 13–16).

These are not presentation details. They change threshold, evidence salience, output schema, dependence among criterion decisions, token competition, parse risk, and cost. RuVerBench usefully demonstrates that call topology is part of grader identity.

### Metrics and aggregation

For each category, the paper computes balanced accuracy as mean positive and negative recall, then macro-averages the four category BAcc values with equal category weight (Section 4.1, pp. 4–5). This prevents the 82.8% positive prevalence in Agentic Coding from making an always-positive judge appear strong. It also imposes an unvalidated policy: every normalized category and both error directions receive equal importance regardless of criterion frequency, severity, dependence, or downstream loss.

Local release recomputation confirms the class totals:

- Deep Research: 631 positive and 984 negative labels;
- Agentic Coding: 698 positive and 145 negative labels.

The category-macro score can differ from artifact-frequency-weighted summaries. For example, GPT-5.4's Agentic Coding score is `89.39` category-macro BAcc, approximately `88.41` when category BAcc is weighted by released criterion counts, and `91.70` raw accuracy. None is intrinsically correct; each answers a different policy question.

The paper reports no output-clustered confidence intervals, task bootstrap, repeated main-run stability, hypothesis tests, rank uncertainty, calibration, severity weighting, or decision-loss analysis. The fixed strategy subset has 60 reports/303 criteria and 42 trajectories/177 checks, but its seed alone does not supply uncertainty.

## Evidence and result interpretation

### Main results show a conditional error surface, not portable reliability

Gemini-3.1 Pro Preview leads Deep Research at `94.7` Avg BAcc; GPT-5.4 leads Agentic Coding at `89.4` (Table 2, pp. 5–6). Category profiles differ: semantic `logic`/`facts` criteria are often harder in Deep Research, while `tools`/`rules` are prominent coding bottlenecks. The released leaderboard adds useful positive/negative recall and bias fields that make strict/permissive behavior inspectable.

However, the paper's suggestion that the domain gap is “consistent with” 7.1K versus 49.4K average tokens is descriptive, not identified. Domain simultaneously changes source benchmarks, criterion language, positive prevalence, output generators, prompts, evidence views, scaffold traces, hidden reasoning, and required state tracking. No within-domain length-matched analysis, truncation audit, or task-cluster model separates length from these factors. The raw predictions needed to test length × criterion family × prevalence interactions are absent.

### Error overlap does not establish that rubric difficulty is unimportant

The paper reports only 16.1% and 20.6% average error-set overlap among three frontier judges and interprets this as model profile dominating inherent rubric difficulty (Section 4.3, pp. 6–7). The corrected release preserves aggregate overlap tables and model-specific error counts but not the underlying prediction matrices or a fully specified overlap estimator.

Low overlap is compatible with model-specific errors, but it is not evidence against item difficulty. Sparse error sets mechanically limit overlap; judges can share a broad difficulty gradient while failing on different borderline items; different false-positive/false-negative thresholds can decorrelate binary error sets; and criteria are nested within outputs. Difficulty requires repeated item-response evidence or an explicit item/rater model, not one overlap percentage.

### Prompt variants mostly move the acceptance threshold

Prompt effects are highly asymmetric. On the fixed coding subset, Qwen3.5-27B's strict prompt raises overall BAcc by `11.8` points while changing positive recall by `-0.9` and negative recall by `+24.6`; Kimi K2.6's flexible prompt lowers overall BAcc by `2.5` while positive recall falls `23.1` and negative recall rises `18.1` (released prompt table; Table 3, p. 7). These are threshold and policy shifts, not generic “better prompting.”

The paper reasonably concludes that weaker models are prompt-sensitive, but it supplies no paired cluster intervals and tests only one fixed subset. A prompt should be selected against declared false-accept/false-reject costs and held-out criteria, not optimized on the same benchmark score and called reliable.

### Batching results combine attention, schema, and invalid-output effects

Large coding batches often show dramatic losses in the exported summaries—up to roughly 35 points for some model/settings (Figure 5 and Table 10, pp. 8, 16). This strongly warns against assuming batched grading is equivalent to isolated grading.

It does not isolate divided attention. Batching also changes output format, keyed-object completeness, shared-context interactions, completion length, parser exposure, and criterion ordering. Raw strategy outputs, token counts, parse-failure counts, and latency are absent. Moreover, the immutable v1 text says responses still unparsable after correction are assigned a uniformly random label and retained (Appendix C, p. 12), whereas the corrected public code maps parse errors, missing IDs, and invalid results to `fail`. With coding labels 82.8% positive, fail-on-parse is especially consequential. The post-v1 tree cannot establish which policy produced the paper table.

The paper describes batching as an efficiency–accuracy trade-off, but reports no dollars, tokens, cache behavior, wall time, throughput, retries, or human audit burden. Fewer API calls plausibly improve one efficiency dimension; the operational frontier was not measured.

### Voting helps some configurations, not consistently all

The paper says self-voting improves both domains and is mostly saturated by three to five votes (Section 4.4, p. 8). The corrected exported table is more qualified:

- Qwen3.5-27B is below its one-vote Deep Research baseline at three and five votes;
- GPT-OSS-120B is below its one-vote Agentic Coding baseline at five, seven, and nine votes, reaching `-3.6` points at nine;
- several curves peak and then fall.

Thus voting often helps, especially for some coding judges, but is not consistently beneficial. The binomial explanation in Appendix D assumes independent identically distributed votes with fixed per-item correctness above 0.5. The experiment reports one nine-sample sweep per item and nested odd-vote aggregates, not repeated independent voting ensembles with intervals. Correlated endpoint errors and systematic per-item error cannot be removed by majority vote; the paper acknowledges the latter but overstates consistency.

## Official-release audit

### What the corrected snapshot enables

The complete 76-file official snapshot was inspected. It provides:

- normalized prompts, reports, coding tasks, tool/message trajectories, final binary labels, and taxonomy assignments;
- the exact 2,458 final-label denominator and 494 scored-output boundary;
- fixed strategy subsets with seed and category distribution;
- judge prompts, batching code, parsing logic, voting aggregation, and leaderboard computation;
- aggregate main leaderboard, strategy tables, error-overlap summaries, and generated figures;
- example prediction files and code that compiles under static checks.

This is enough to audit criterion nesting, label prevalence, evidence views, prompts, parser semantics, score aggregation, and release denominators.

### What remains unauditable

The snapshot omits:

- full raw predictions for all 18 judges and all strategy runs;
- per-request prompts, outputs, usage, retries, parse states, timestamps, and endpoint identities from the paper run;
- annotation guideline, pilot gold, candidate-team records, independent labels, adjudication rationales, and worker-level metadata;
- pre-filter rubrics, rejection reasons, sampling funnel, category coding protocol, and taxonomy reliability;
- per-output generator identity and decoding configuration despite the manuscript's recordkeeping claim;
- cost/latency records, clustered uncertainty analysis, and paper-time environment lock.

The pinned commit is dated 11 July 2026 and explicitly fixes result packaging after v1. The initial repository predates v1, but the paper pins no commit. The corrected tree is valuable release evidence, not guaranteed paper-time implementation. The manuscript/release parse-policy mismatch and absent raw outputs prevent exact score replay.

## Unique insight

RuVerBench's deepest contribution is to expose a **three-stage selection problem in grader validation**:

1. **criterion selection:** retain criteria that the available observer view can label cheaply and “objectively”;
2. **label-policy selection:** train/select annotators against a pilot, share a guideline, and adjudicate disagreements;
3. **observer selection:** optimize prompt, batching, voting, parser, and model against those final labels.

A high agreement score after all three stages is useful, but it is not a context-free property of the judge. It says the configured observer recovers one post-filtered annotation policy on one output population. It does not establish that the criterion was professionally legitimate, that omitted evidence was unnecessary, that the adjudicated policy is uniquely correct, or that agreement survives a new artifact family.

This suggests a stronger object for `skill-bench`: a **verifier acceptance surface**, not a scalar verifier accuracy. It should be indexed by criterion family, applicability, evidence view, output/trajectory cluster, rubric source, label authority, prevalence, severity, prompt realization, execution topology, model/provider, parser state, and time. Agreement, stability, construct validity, and decision loss remain separate outcomes.

## Comparison with existing project evidence

- **AgentRewardBench** evaluates success, side effect, and repetition labels over web trajectories and exposes unequal human/model evidence views, rare-label effects, and weak adjudication lineage. RuVerBench adds criterion-level verification over much longer textual and coding outputs, complete double annotation, prompt/batch/vote interventions, and a larger judge matrix. It still lacks released plural labels and gives judges answer-bearing criteria, so its “gold” remains policy-bound.
- **Rubric Modification and Human/Autorater Agreement** shows that examples, decomposition, call separation, and aggregation are measurement interventions, not harmless formatting. RuVerBench independently confirms execution-topology sensitivity at long context, while adding binary accuracy against newly adjudicated labels. Neither establishes construct preservation or professional decision validity.
- **ResearchRubrics** contributes expert-authored deep-research criteria and released rubric artifacts. RuVerBench reuses that source but filters it for verifier observability and evaluates coverage without source access. This is evidence about criterion recognition, not external factuality or expert-artifact quality.
- **Many-Facet human/AI rater analysis** supplies the missing conceptual model: item, criterion, rater, task, and interaction effects should be separated. RuVerBench reports slices and overlaps but does not fit a clustered or many-facet reliability model.

Together, these sources reject “choose the highest-scoring judge” as an adequate grader-validation protocol.

## Limitations and validity threats

1. **Criterion rows are not independent executions.** The 2,458 labels nest within 494 shared outputs.
2. **Selection is conditioned on verifiability.** Subjective, externally grounded, composite, and missing-evidence criteria are removed.
3. **The filtering funnel is unavailable.** No pre-filter counts, exclusions, probabilities, or downsampling implementation are released.
4. **Source coverage is not work-population sampling.** Four benchmark sources do not estimate prevalence across professional criteria.
5. **Deep Research criteria often disclose the expected fact.** Coverage agreement is not factual verification against sources.
6. **Coding evidence is trajectory-limited.** The judge does not independently inspect repository state or execute functional checks.
7. **Hidden reasoning is a variable observer channel.** Availability and semantics differ by generator/scaffold and can leak policy cues.
8. **Human authority is under-specified.** Undergraduate education and technical annotation skill do not establish expertise over 35 research domains.
9. **Pilot gold is unexplained.** Team selection above 90% accuracy depends on an unspecified authority target.
10. **Shared training can manufacture consistency.** Guideline revision and common policy reduce disagreement without proving construct validity.
11. **Adjudication is opaque.** No adjudicator, rationale, uncertainty, blinding, or changed-label lineage is released.
12. **Agreement with adjudicated gold is partly circular.** The final label was produced by resolving the two component label sets.
13. **Taxonomy validity is unmeasured.** Single-label categories mix abilities and have no coder-reliability evidence.
14. **Domain and length are confounded.** Sources, prompts, labels, generators, evidence views, and criterion types all change with length.
15. **Generator provenance is incomplete in the release.** Per-output model and decoding fields promised by the paper are absent.
16. **No raw prediction matrices.** Confusions, length effects, item difficulty, parse failures, and overlap cannot be independently recomputed.
17. **No output-clustered uncertainty.** Scores and strategy deltas omit intervals and effective sample size.
18. **No repeated main judgments.** Endpoint stochasticity and temporal drift are not estimated for leaderboard scores.
19. **Macro BAcc encodes an unvalidated utility policy.** Categories and error directions receive equal weight regardless of severity or use.
20. **Strategy subset inference is weak.** One seeded subset and many model/condition comparisons lack paired clustered intervals or multiplicity control.
21. **Prompt effects are threshold effects.** Positive and negative recall frequently move sharply in opposite directions.
22. **Batching is a bundled intervention.** Attention, output schema, ordering, parse risk, completion budget, and shared context change together.
23. **Paper and release invalid policies conflict.** Immutable v1 says random labels after parse correction; corrected code emits `fail`.
24. **Voting gains are non-monotonic.** Exported runs contradict a universal or consistent-improvement reading.
25. **Voting independence is assumed, not tested.** One nested nine-sample sweep does not estimate ensemble uncertainty.
26. **Error overlap is not item difficulty.** Sparse thresholded error sets cannot identify whether rubric difficulty drives failures.
27. **No cost or latency evidence.** Efficiency claims omit tokens, dollars, cache effects, throughput, and audit burden.
28. **Contamination is uncontrolled.** Public source benchmarks and criteria may be known to later judge models; no private holdout or exposure audit is reported.
29. **Hosted model identity is mutable.** Names, thinking levels, and token caps do not freeze endpoint behavior.
30. **Binary labels erase partial/applicability states.** `not_applicable`, insufficient evidence, partial fulfillment, and consequential severity collapse into yes/no.
31. **No professional or consequential validation.** Agreement is not linked to stakeholder decisions, artifact acceptance, harm, or deployment loss.

## Reproducibility and operational realism

Reproducibility is **strong for inspecting the released benchmark and scoring design, moderate for generating new configured-judge observations, and weak for reproducing the paper tables exactly**. The immutable PDF/text, complete benchmark inputs, outputs, final labels, taxonomies, prompts, fixed subset, aggregation code, and aggregate tables are available. A researcher can run a new OpenAI-compatible endpoint and score its predictions.

Exact replay is blocked by absent paper-run predictions and request manifests, mutable endpoints, missing annotation artifacts, unreleased filtering/sampling lineage, and the post-v1 packaging fixes. The requirements file uses broad minimum versions rather than a lock. The package can regenerate figures from aggregate tables, but that verifies plotting, not the empirical run.

Operational realism is mixed. The judged artifacts are genuinely long; coding trajectories contain tools, failures, repairs, and scaffold constraints; and criterion-level verification resembles real evaluation pipelines. Yet the benchmark freezes one output per case, strips criteria that exceed the observer view, provides no live source/repository query to judges, measures no downstream decision, and reports no cost/latency/audit frontier. It is a useful grader-calibration corpus, not a demonstration that model judges can supervise consequential knowledge work autonomously.

## Transfer to skill-bench

### 1. Make verifier identity transactional and immutable

Every criterion observation should bind:

- criterion text/hash, source authority, dependencies, applicability, severity, and public/private status;
- required evidence channels and actual evidence locators;
- output/trajectory/artifact/environment versions and cluster ID;
- prompt, examples, ordering, batch membership, execution plan, model/provider, decoding, and date;
- raw response, parse result, retry/fallback lineage, invalid/insufficient state, cost, and latency;
- label-policy version and exactly which claim the observation may support.

A prompt suffix, batch size, evidence channel, parser fallback, or vote rule creates a new grader realization.

### 2. Preserve plural labels before adjudication

Store every human/model/deterministic observation independently with authority, qualifications, evidence view, rationale, uncertainty, and independence links. Adjudication should have an explicit policy, adjudicator, evidence, changed fields, and disagreement type. An adjudicated label is a versioned resolution, not an overwrite of the original observations or automatic truth.

### 3. Calibrate on output clusters and excluded criterion families

Use task/output-cluster resampling or hierarchical models. Report confusion matrices and intervals by criterion source/family, applicability, trace length, output length, generator/harness, evidence view, prevalence, severity, and prompt realization. Include challenge sets for externally grounded, dependent, partially satisfied, not-applicable, insufficient-evidence, and plural-judgment criteria rather than validating only criteria preselected for cheap binary labeling.

### 4. Separate observer capacity from evidence sufficiency

For planted cases, compare artifact-only, full trace, structured state, and environment/source-query views while holding the criterion fixed. If required evidence is absent, the only valid outcome is `insufficient_evidence`; it must not become a random or negative label. Test whether extra hidden reasoning helps legitimate verification or merely leaks intent/policy cues.

### 5. Treat prompt, batching, and voting as interventions

For each intervention, preserve paired item IDs and estimate:

- positive/negative recall and calibrated probability change;
- parse/invalid/missing rates;
- criterion-order and batch-composition effects;
- repeated-run stability and correlated errors;
- token, dollar, latency, and human-audit burden;
- downstream expected loss under a declared decision.

Do not optimize on one benchmark score and relabel the winner “reliable.”

### 6. Use cascades with explicit claim ceilings

Deterministic state checks, semantic model judges, and qualified human review should provide complementary typed observations. Route high-loss disagreements, missing evidence, rare categories, and unstable criteria to audit. Agreement on RuVerBench-like criteria can license a narrow configured concordance claim; professional capability, grader accuracy in a new domain, production fitness, safety, and readiness require separate evidence.

## Concrete repository implications

1. Existing benchmark-bundle grader/evidence-view records should treat criterion batch membership, ordering, prompt policy, parser state, and vote lineage as grader identity—not runtime trivia.
2. Existing plural-judgment machinery is the correct home for independent labels, framework/policy provenance, and adjudication; no new annotation subsystem is warranted.
3. Existing metric-monitoring machinery should require output-cluster units, eligible criterion population, prevalence, invalid/missing policy, confusion intervals, source/category/length slices, and cost/latency.
4. Existing task-health and validity-argument contracts should block the upgrades `agreement → accurate grader → professional-quality evaluator → autonomous reward/monitoring fitness` unless each warrant has independent evidence.
5. A future real grader calibration should include a matched isolated-versus-batched comparison with planted parse failures, unequal label prevalence, missing evidence, dependent criteria, and repeated votes. This is already within the plural-grader/metric/validity machinery; no duplicate queue task is added.

## Action items completed

- [x] Read the complete immutable v1 paper, including annotation, prompt, strategy, ethics, and qualitative-error appendices.
- [x] Inspect the complete official corrected release with explicit post-v1 timing limits.
- [x] Verify 494 scored outputs, 2,458 criteria, source/score denominator boundaries, label prevalence, criterion clustering, evidence views, prompts, parser behavior, aggregation, and release omissions.
- [x] Recompute release-supported case/check distributions and compare macro-category BAcc with alternative descriptive summaries.
- [x] Test the paper's prompt, batching, voting, error-overlap, length, and reliability interpretations against released evidence and identify what absent raw predictions prevent.
- [x] Compare nonduplicatively with AgentRewardBench and the rubric-modification review.
- [x] Map findings to existing grader, evidence-view, plural-judgment, metric, task-health, and validity contracts; add no duplicate task.
