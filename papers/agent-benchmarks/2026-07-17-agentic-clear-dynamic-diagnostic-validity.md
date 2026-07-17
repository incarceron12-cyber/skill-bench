# Agentic CLEAR: open-taxonomy compression is not validated root-cause diagnosis

- **Paper:** <https://arxiv.org/abs/2605.22608v1>
- **Authors:** Asaf Yehudai, Lilach Eden, Michal Shmueli-Scheuer
- **Date read:** 2026-07-17
- **Source:** complete immutable arXiv v1, submitted 21 May 2026
- **Local PDF:** `data/papers/pdfs/2605.22608v1-agentic-clear.pdf` (14 pages; SHA-256 `690003da572c98cd2fb7c1ac19ad36cefb4dbe2cd78327c1b10bc1ebb497b2aa`)
- **Local text:** `data/papers/text/2605.22608v1-agentic-clear.txt` (SHA-256 `46fb2513ccb45eefc25ebb9a4192892363fd4e853310b3651a18b9bd9694ca42`)
- **Official release inspected:** <https://github.com/IBM/CLEAR/tree/28a16d4f055697292908a5b87b3fd30ab21dc6e6>; local archive `data/sources/releases/2605.22608v1-agentic-clear/IBM-CLEAR-28a16d4.zip` (137 files; SHA-256 `81320bf7b8b07716db928f4044ac56c8d233da33b5409734bb4accee838ecdb6`)
- **Release provenance:** `data/sources/releases/2605.22608v1-agentic-clear/provenance.json`
- **Timing boundary:** the inspected commit is dated 16 June 2026, 26 days after immutable v1. It is post-v1 release evidence, not proof of the paper-time implementation.
- **Tags:** trajectory-evaluation, dynamic-taxonomy, llm-judge, diagnostic-validity, root-cause, trace-normalization, issue-induction

## One-sentence contribution

Agentic CLEAR operationalizes dynamic, multi-level trace review across heterogeneous agent systems, but its released evidence validates open-vocabulary issue discovery and outcome association only weakly—not category stability, evaluator correctness, causal root localization, or intervention utility.

## Bottom line

Agentic CLEAR supplies useful machinery for turning heterogeneous agent traces into a navigable review surface: normalize each LLM call, judge steps and whole trajectories, generate task-specific rubrics, synthesize recurring issue phrases, map them back to traces, and expose system/node/trace views. Across 1,129 traces from four benchmarks and seven configured settings, it also shows that judge scores can be associated with native success labels and that induced issue phrases can be mapped onto all twelve non-execution categories used from TRAIL.

The paper does **not** validate automatic root-cause diagnosis. Its sole category-alignment study uses only 117 TRAIL trajectories, maps system-level issue phrases to TRAIL categories with another LLM plus author verification, then propagates those phrase-level mappings to traces. The best macro-F1 is 0.459 when partial matches count, below a level that would justify autonomous diagnosis. No independent annotators judge whether each generated issue is true, whether its supporting trace evidence is sufficient, whether a node is the earliest cause rather than the surface location, whether categories remain stable under resampling/order/judge changes, or whether a developer acting on the dashboard improves a system.

The release makes the identification problem sharper. The pipeline is a cascade of model-mediated transformations:

`raw observability record → selected LLM-call rows → compact/truncated textual trace → judge critique/score → sampled low-score critique set → induced issue phrases → optional LLM deduplication → LLM issue-to-record remapping → frequency/dashboard`

A displayed “recurring root cause” is therefore not a direct property of raw execution. It is a compressed, judge-conditioned hypothesis whose denominator, evidence view, transformation lineage, stability, and validation status must remain visible.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C by testing a scalable diagnostic layer rather than treating trace dashboards as evidence of causality. The four benchmark families are methodological substrates, not a proposal to narrow `skill-bench` to web, software, or API agents.

The concrete lesson is a claim ladder:

1. **surface observation:** a preserved state/action/artifact fact;
2. **judge observation:** a model says a criterion or quality dimension is weak;
3. **candidate issue:** multiple judge texts are compressed into a phrase;
4. **stable category:** the phrase and its membership survive specified perturbations;
5. **criterion-aligned diagnosis:** independent labels support the category on held-out traces;
6. **supported root:** temporal/dependency evidence identifies an earlier cause rather than the failure surface;
7. **actionable diagnosis:** a targeted intervention changes the expected failure while preserving irrelevant behavior.

Agentic CLEAR provides useful implementation evidence for levels 1–3 and limited criterion-association evidence for level 5. It does not establish levels 4, 6, or 7. `skill-bench` should retain dynamic issue discovery as a **review-queue and hypothesis-generation mechanism**, not promote its output directly into root-cause labels, task revisions, skill lessons, or benchmark validity claims.

## Research question and claim boundary

The paper asks whether an automatic, taxonomy-free, multi-level LLM evaluation pipeline can surface useful system-, trace-, and node-level patterns across heterogeneous agents without benchmark-specific rubrics or extensive manual annotation (Sections 1–3, pp. 1–4).

### What the evidence supports

- The authors processed 1,129 reported traces across four benchmark families, seven agent/model settings, and two judge models (Table 1, p. 5).
- The method emits step, full-trace, generated-rubric, node-aggregate, and system-aggregate views and links aggregate issue phrases back to instances (Algorithm 1, pp. 2–3).
- GPT-5 and OSS-120B produce materially different issue vocabularies and emphases; the paper explicitly observes this dependence (Section 5, pp. 5–6).
- On 117 TRAIL traces, transitive category predictions exceed the two reported baselines on macro-F1 only for some judge/matching choices; GPT-5 full+partial reaches micro-F1 0.497 and macro-F1 0.459 (Table 2, p. 6).
- Judge scores contain setting-dependent association with native trajectory success: reported AUCs range from 0.409 to 0.890 across setting, judge, and score construction (Table 3, p. 7).
- Task-description-only rubrics fail when consequential requirements are absent from the public request: the paper's τ²-Bench analysis says they can reward completion when policy requires refusal (Section 6.3, pp. 7–8).

### What the evidence does not support

- That induced issues are generally correct, complete, nonredundant, stable, or calibrated.
- That node association identifies a causal origin or “root cause.”
- That taxonomy alignment demonstrates instance-level evaluator truth rather than shared semantic resemblance.
- That success-prediction AUC validates diagnostic categories, judge scores, or professional-quality measurement.
- That the tool reduces human labor, shortens debugging time, improves agent quality, or is cost-effective; none is measured.
- That findings transfer beyond the selected benchmark traces, agent implementations, judges, prompts, and trace representations.
- That generated rubrics fairly recover hidden policy, environment state, expert conventions, safety constraints, or domain authority.
- That a dashboard output is production-ready evidence for system changes, benchmark maintenance, capability claims, or deployment decisions.

## Methodology and system reconstruction

### Trace corpus and configured settings

Table 1 reports seven settings totaling 1,129 traces:

| Benchmark | Agent/backbone setting | Traces | Source |
|---|---|---:|---|
| AppWorld | CUGA / GPT-4o | 417 | leaderboard |
| GAIA | HAL Generalist / Claude 4.5 Sonnet | 165 | HAL |
| GAIA | HAL Generalist / GPT-4.1 | 165 | HAL |
| GAIA | HF DeepResearch / Claude 4.5 Sonnet | 165 | HAL |
| GAIA | HF DeepResearch / OpenAI o3 | 117 | TRAIL |
| SWE-bench Verified Mini | HAL Generalist / Claude 4.5 Sonnet | 50 | HAL |
| τ²-Bench Airline | HAL Generalist / Claude 3.7 Sonnet | 50 | HAL |

The corpus is curated rather than sampled from a defined agent-trajectory population (Section 4, p. 5). AppWorld contributes 36.9% of traces, GAIA 54.2%, and the remaining two families 8.9%; the paper provides no population weights, task-overlap table, invalid/missing trace accounting, attempt policy, seed/repetition design, collection dates, environment versions, or per-setting LLM-call counts. “Tens of thousands of LLM calls” is not accompanied by a denominator table.

The statistical units differ throughout the study: 1,129 traces, many more step/node LLM calls, 195 reported trace-level issue phrases across configurations, 27 system-level issue phrases in the TRAIL alignment (15 GPT-5 and 12 OSS-120B), twelve TRAIL categories, and seven setting-level AUC rows. These are not interchangeable sample sizes. No inferential uncertainty accounts for repeated tasks, shared configurations, category dependence, or generated-issue selection.

### Raw trace to intermediate representation

The paper describes OpenTelemetry-compatible ingestion, Langfuse conversion, and an intermediate representation centered on LLM inputs, outputs, node identities, and metadata (Section 3.1, p. 3). The release implements MLflow and Langfuse adapters. Each output CSV row is one LLM invocation with node name, task/step identifiers, model input, response, available-tool schema, metadata, and optional `traj_score` (`docs/agentic/intermediate-representation.md`).

This is an inspectable and reusable normalization boundary, but it is lossy by design. The paper says it focuses on LLM interactions because they govern decisions and are stochastic (p. 3). The released adapters retain token/latency/cost metadata where supplied, but downstream judging primarily sees the textualized calls. Non-LLM environment transitions, rendered state, database changes, deterministic program execution, hidden policy state, human messages outside captured calls, and harness-level failures can be absent or only indirectly represented.

Adapter semantics are also treatment variables. Langfuse accepts every `GENERATION` observation and derives component names from framework metadata. MLflow recognizes several model-span patterns and walks parent chains while skipping wrapper names. These heuristics can alter node assignment and evidence inclusion. The paper reports no cross-adapter conformance set where equivalent raw executions yield equivalent normalized views.

### Compact trace and evidence view

The released formatter deduplicates repeated model-input histories by node, reconstructs available tool definitions, and emits ordered markdown blocks. Under an explicit context budget it preserves responses up to a fixed limit and proportionally truncates input content; a final middle-out cap can remove the center of a long trajectory (`compact_trace_formatter.py`; `base_evaluator.py`).

This makes scale practical, but the exact view given to the judge must be treated as part of evaluator identity. A causal precursor can disappear through parent-span selection, history deduplication, response truncation, proportional input truncation, or middle-out capping. Neither the paper nor release attaches an evidence-sufficiency judgment, omitted-content manifest, transformation hash, or causal-coverage check to a diagnosis.

### Per-step and per-trace judging

Algorithm 1 invokes a step judge for every input/output pair, a full-trace judge for every trajectory, a rubric generator from task text, and a rubric evaluator over the trace (pp. 2–3). The paper uses GPT-5 and OSS-120B in high-thinking mode as judges (Section 4, p. 5).

The post-v1 release exposes three related instruments:

- a step prompt judging correctness, completeness, clarity, relevance, efficiency, robustness, best practices, actionability, and transparency;
- a full-trajectory prompt with those nine dimensions plus objective understanding, information completeness, execution quality, user experience, and final deliverable;
- a task-success prompt that requests binary success and a failure “root cause.”

The default fourteen dimensions are broad and partly dependent. “Correctness,” “completion,” “execution quality,” and “final deliverable” can all respond to the same failure. The full-trace prompt asks the judge to write detailed feedback as “chain-of-thought” and then produce an overall score as a “weighted average,” but no weights are specified. The resulting scalar is model-authored rather than an auditable aggregation rule.

The released task-success evaluator goes further than the paper's validated evidence: it asks the same judge to identify a root cause from task text plus compact trace. There is no structural dependency graph, counterfactual test, competing-cause record, or evidence threshold. “Root cause” here is a field name for an LLM explanation, not an established causal estimand.

### Generated rubrics

For each task, the rubric generator sees only the task objective and creates three to five “essential,” “non-overlapping,” and “testable” criteria. A second call marks each criterion fulfilled from trace evidence and reports the fraction fulfilled (`rubric_generator.py`; `rubric_evaluator.py`).

This separates criterion generation from criterion application, but both stages use the same configured judge family and neither has independent source authority. The paper's own rubric analysis is the decisive negative case: AppWorld's generated workflow rubrics are qualitatively related to native state assertions, while τ²-Bench rubrics can reward complying with a surface request that policy says to refuse (Section 6.3, pp. 7–8). The method therefore recovers **disclosed apparent requirements**, not hidden-but-fair consequences, authoritative policy, or professional conventions.

The release parser also trusts structurally weak outputs. It does not validate that three to five rubrics are present, IDs are unique, criteria are atomic, all expected IDs are returned, fulfillment values are valid, or the model-reported score equals the computed fraction. If the model provides a numeric score, that score is retained even if inconsistent with parsed fulfillment. Missing rubric results reduce the counted fulfilled total while preserving the expected denominator, silently behaving like failures rather than invalid observations.

### Dynamic issue induction, deduplication, and remapping

The paper describes CLEAR as clustering and summarizing trace/node feedback into recurring issues (pp. 2–3). The release reveals a more precise pipeline:

1. keep evaluation texts whose score is below a configurable threshold;
2. optionally sample a maximum number with probability weighted toward lower scores;
3. concatenate up to 100 texts per synthesis batch;
4. ask the judge for recurring issue phrases;
5. on later batches, ask only for issues “new” relative to the accumulated list;
6. optionally invoke another judge prompt to merge near-duplicates up to a maximum count;
7. remap each resulting issue to each low-scoring critique with a binary LLM call;
8. assign zeros to high-scoring, missing, or unparseable mappings and count mapped records for dashboard frequency (`full_pipeline.py`; `eval_utils.py`; `propmts.py`).

This is not conventional embedding clustering, and it has strong path dependence. Batch order determines which issues are deemed “already identified”; weighted sampling conditions discovery on the same judge's scores; issue count is capped; deduplication can merge distinctions; and remapping asks the same model family whether its own compressed categories are implied by its earlier critique. Frequencies are therefore **post-selection membership rates among evaluator outputs**, not raw failure prevalence.

The invalidity semantics are particularly unsafe for diagnostic claims. A mapping parse failure defaults to an all-zero issue vector. A failed mapping call leaves initialized zeros. High-score rows bypass mapping. Missing evaluation text also yields zeros. These cases can appear issue-free unless the separate error column is inspected. The dashboard denominator can consequently mix true absence with exclusion, failed observation, and model/parser invalidity.

### Human-taxonomy alignment study

The alignment experiment uses 117 GAIA/HF DeepResearch/o3 traces from TRAIL. TRAIL supplies twenty human-authored categories; the authors retain twelve non-execution categories covering 94% of labels because Agentic CLEAR focuses on reasoning/planning (Section 6.1, p. 6).

The validation chain is:

1. generate system-level issues from the 117 traces;
2. have Claude Opus 4.6 map each generated issue to TRAIL as full or partial category matches;
3. have the paper authors verify those mappings;
4. propagate each issue-to-category mapping to traces on which CLEAR assigned that issue;
5. compare the derived trace/category matrix with TRAIL labels.

All 15 GPT-5 and 12 OSS-120B issue phrases map to at least one retained category, covering twelve and ten categories respectively. That phrase-level coverage is unsurprising given broad categories and permissive partial matching; it does not measure whether an issue is true on a trace. At instance level, GPT-5 full+partial reaches micro-F1 0.497 and macro-F1 0.459; GPT-5 full-only reaches 0.467/0.368; OSS-120B full+partial reaches 0.427/0.374 (Table 2, p. 6).

The study lacks independent mapping coders, mapping agreement, blinded adjudication, confidence, category-wise support, threshold calibration, held-out issue induction, or a second trace sample. Author verification is not independent human annotation of generated diagnoses. Because Claude maps outputs from GPT-5/OSS-120B and TRAIL itself is a model-facing taxonomy, semantic agreement can reflect shared language rather than correct evidence localization.

### Success association

Table 3 reports ROC AUC for three score constructions against native trajectory labels: mean step score, full-trace score, and fraction of generated rubrics fulfilled (p. 7). There are 42 AUC cells: seven settings × two judges × three methods. Full-trace scoring is often strongest, but not uniformly. Across all cells, results range from 0.409 to 0.890. AppWorld is consistently high; τ²-Bench never exceeds 0.618; GAIA and SWE-bench vary by method and judge.

AUC shows ranking association under each observed setting. It does not identify score calibration, decision thresholds, error costs, rank uncertainty, or causal diagnosis. It is also partly circular as validation of “insight quality”: both the score and textual issue originate from the same judge view, while native labels may encode hidden state unavailable to the judge. High AUC for a scalar does not validate the attached explanation; low AUC can arise from an insufficient evidence view rather than poor semantic judgment.

## Unique insight and evidence interpretation

The paper's most important empirical finding is not that dynamic taxonomies replace expert taxonomies. It is that **diagnostic output is representation- and judge-conditioned even before any causal claim is made**. GPT-5 produces longer, more domain-specific issue phrases than OSS-120B; dataset changes appear to affect issue profiles more than one architecture comparison; and rubric validity collapses when public text omits consequential policy (Sections 5–6, pp. 5–8).

The unique transfer is a distinction among three operations that the paper often rhetorically compresses:

- **description:** what pattern a judge says appears in selected evidence;
- **localization:** where in the normalized trace that pattern is visible;
- **causal diagnosis:** which earlier event or component generated the consequential failure.

Node grouping supports localization only at the component label assigned by the adapter. A planning node can contain an early mistake, receive an already-corrupted input, or merely verbalize a failure caused by missing environment state. Calling its recurring phrase a “root cause” requires dependency evidence and alternatives, not just node membership.

Dynamic categories are still valuable because a fixed taxonomy cannot anticipate every artifact, policy, tool, or domain failure. But “dynamic” introduces a measurement obligation: category identity itself must be versioned and tested for stability. If category phrasing, boundaries, membership, or rank change with trace order, sample, judge, prompt, or cap, a dashboard comparison across systems or time can be taxonomy drift rather than behavior drift.

## Comparison with related reviewed systems

- **STRACE** (`papers/agent-benchmarks/2026-07-09-strace.md`) explicitly models execution dependencies and backward causal slices. Agentic CLEAR is stronger as a general trace-review product but weaker as causal evidence: node grouping is not dependency tracing.
- **Signals** (`papers/agent-benchmarks/2026-07-14-signals-trajectory-triage-sampling-validity.md`) separates enriched review yield from population prevalence. CLEAR's low-score sampling and issue remapping need the same inclusion-probability boundary; dashboard frequency is not prevalence when discovery is outcome-conditioned.
- **AgentRewardBench** (`papers/agent-benchmarks/2026-07-10-agentrewardbench-judge-reliability.md`) tests judge outputs against expert trajectory labels and exposes evidence-view dependence. CLEAR validates only one 117-trace category slice and does not independently label issue truth or root support.
- **Tool-Veritas audit** (`papers/agent-benchmarks/2026-07-13-tool-calling-evaluator-validity-audit.md`) insists that evaluator verdicts, observations, targets, and corrections are empirical objects. CLEAR's generated rubrics and binary mappings lack that independent predicate-level validation.
- **EvalAgent** (`papers/agent-benchmarks/2026-07-12-evalagent-domain-evaluation-skill-validity.md`) separates executable evaluator production from measurement validity. CLEAR's package and dashboard establish inspectable evaluator engineering, not validity of induced criteria or categories.
- **Auto Benchmark Audit** (`papers/agent-benchmarks/2026-07-14-auto-benchmark-audit-task-defect-validity.md`) treats automated findings as candidates requiring adjudication and repaired-form reruns. CLEAR issues should receive the same lifecycle before they alter benchmark tasks, rubrics, or lessons.

## Limitations and validity threats

1. **Curated corpus without a sampling frame.** The 1,129 traces provide heterogeneous cases, not representative agent-work prevalence.
2. **Strong family imbalance.** GAIA and AppWorld supply 91.1% of traces.
3. **No repeated agent runs.** Environment, model, and agent stochasticity are not separated from configured-system differences.
4. **No repeated judge runs.** Category, mapping, and score stability under endpoint nondeterminism is unknown.
5. **No clustered uncertainty.** Shared tasks, agents, sources, and categories are treated descriptively without intervals.
6. **Trace adapters are unvalidated transformations.** Node names, ordering, content selection, and metadata extraction can differ by observability framework.
7. **LLM-call-only view is incomplete.** Consequential environment state and non-LLM execution can be missing.
8. **Truncation can remove causes.** Input histories are deduplicated and compacted; long traces can lose middle evidence.
9. **Broad dependent dimensions.** The fourteen default criteria overlap and have no empirically validated weighting model.
10. **Overall score is under-specified.** The prompt requests a weighted average but defines no weights or deterministic recomputation.
11. **Rubrics are generated from surface intent only.** Hidden-but-fair policy, state, safety, and professional requirements can be absent.
12. **Criterion generation and application are not independent.** The same judge family authors and grades apparent requirements.
13. **Rubric parser lacks semantic validation.** Missing/duplicate/non-atomic criteria and inconsistent model-computed scores can survive.
14. **Issue discovery is outcome-conditioned.** Only below-threshold evaluation text enters synthesis, and optional sampling favors lower judge scores.
15. **Issue induction is order-dependent.** Later batches are instructed not to repeat earlier phrases.
16. **Deduplication is another uncalibrated judge call.** Merge errors can erase real distinctions or retain paraphrases.
17. **Remapping is self-referential.** A judge maps categories synthesized from judge critiques back onto those critiques.
18. **Invalid mappings default toward absence.** Parse/call failures can become all-zero issue vectors.
19. **Frequency is not failure prevalence.** It is conditional on inclusion, synthesis, category cap, deduplication, mapping, and valid output.
20. **Only one narrow human-label comparison.** Category F1 uses 117 TRAIL traces and twelve retained labels.
21. **Category mapping is not independently coded.** Claude Opus 4.6 mapping plus author verification has no agreement or blinding evidence.
22. **Partial matching changes the claim.** Best macro-F1 depends on allowing broader/adjacent categories as matches.
23. **Moderate best alignment.** Macro-F1 0.459 is useful candidate-generation evidence, not autonomous diagnostic reliability.
24. **No localization accuracy test.** The paper does not compare cited steps/nodes with human-supported evidence locations.
25. **No causal-root test.** Node occurrence and failure explanations are not dependency or counterfactual evidence.
26. **AUC does not validate explanations.** Success association of judge scores cannot establish issue truth or actionability.
27. **Native labels have unequal observability.** Hidden state and policy can make trace-only evaluation impossible, as τ²-Bench demonstrates.
28. **No intervention study.** Developers do not repair systems from CLEAR findings and rerun held-out/equivalent tasks.
29. **No human-utility study.** Time saved, review burden, trust, false leads, and decision quality are unmeasured.
30. **No cost report.** The paper says tens of thousands of calls but gives no token, dollar, latency, or human-audit totals.
31. **No paper-run artifact release.** The archived repository contains sample traces/results, not the 1,129-trace corpus, issue mappings, experiment manifests, or analysis notebooks.
32. **Post-v1 release timing.** The inspected implementation may not match paper-time prompts, parsers, defaults, or outputs.
33. **No test suite in the inspected archive.** Among 137 files, the only test-named path is an example tool config; no unit/integration tests validate adapters, parsers, invalid handling, category induction, or frequency calculations.
34. **Mutable provider identity.** Model aliases/endpoints and LiteLLM/provider behavior are not frozen as immutable realizations.
35. **Cache identity is weak.** Existing outputs are reused by path unless overwrite is set; the cache does not prove prompt/model/data/config hash equivalence.

## Reproducibility and operational realism

Reproducibility is **moderate for inspecting the post-v1 instrument and weak for reproducing the paper experiment**. The release is substantial: 63 Python files, trace adapters, intermediate representation documentation, prompts, three trajectory evaluators, dynamic issue synthesis/remapping, dashboard code, provider abstraction, caching, concurrent execution, 25 raw sample trace JSON files, twenty processed sample trajectories, and a precomputed dashboard archive. The sample archive exposes twenty full-trajectory and twenty rubric evaluations plus system issue outputs. This is enough to audit how claims are operationalized.

It is not enough to replay the paper. The official archive lacks the reported benchmark corpus, exact paper prompts/configurations, result tables, 195 issue records, 117-trace prediction matrix, TRAIL mapping decisions, author verification records, judge raw responses, token/cost ledger, exclusions, and statistical analysis. The commit postdates v1, has no lockfile or paper-run container, and the inspected archive contains no automated tests.

Operationally, the package has real strengths: OpenTelemetry-adjacent ingestion, per-step provenance fields, node/system/trace navigation, raw judge responses, timestamps, model name, elapsed time, optional provider parameters, parallel calls, resumable outputs, and explicit parse-null possibilities. It also has fail-open edges. Many failures return `None` and disappear from result files; summaries scan only saved successes; rubric/mapping invalidity can act like failure or absence; provider usage is not stored with every trajectory judgment; and cache reuse is path-based rather than hash-bound. A production diagnostic service would need an eligibility ledger whose denominator includes attempted, skipped, cached, truncated, invalid, failed, and successfully judged units separately.

The benchmark traces contain real multi-step tool use and heterogeneous agent architectures, which is more realistic than final-answer-only evaluation. Yet the framework observes chiefly textual LLM calls. Professional artifacts, structured environment state, source authority, private policy, human acceptance, and consequential side effects need additional evidence channels and domain-authorized criteria. The dashboard is best viewed as an **exploratory observability instrument**, not an autonomous evaluator.

## Transferable design implications for skill-bench

### Retain

1. **Multi-resolution observations.** Preserve raw state/action evidence, step/node observations, trace observations, and portfolio patterns as separate records.
2. **Adapter-normalized trace views.** Support heterogeneous harness traces through an intermediate representation, but hash the adapter and retain the raw source.
3. **Backlinks from category to evidence.** Every aggregate issue should link to concrete trace/state/artifact locators.
4. **Dynamic candidate discovery.** Use open-vocabulary synthesis to surface unanticipated failure hypotheses for human review.
5. **Judge-comparison views.** Different judges expose diagnostic sensitivity; disagreement should be visible rather than silently averaged.
6. **Native-outcome association as one check.** AUC or similar association can test whether an observation contains outcome signal, while remaining distinct from category/root validity.

### Repair

1. **Represent the complete transformation chain.** Record raw-trace hash, adapter/version, normalized-view hash, omitted channels, truncation/dedup manifest, judge/prompt hash, critique, synthesis sample policy/seed/order, category version, merge lineage, mapping call, and invalid state.
2. **Use typed category states.** `candidate`, `stable`, `criterion_aligned`, `supported_root`, and `intervention_validated` must not collapse into one “issue” field.
3. **Separate surface and root.** A node/step locator identifies where evidence appeared. Root status requires a dependency path, temporal precedence, alternatives considered, and support threshold.
4. **Fail closed.** Missing evidence, parse failure, provider failure, category-map failure, or truncated required state must become `invalid`/`insufficient_evidence`, not issue absence.
5. **Specify denominators.** Report attempted traces/calls, eligible synthesis pool, sampled critiques, valid mappings, excluded high-score cases, invalid outputs, category cap, and membership frequency separately.
6. **Freeze category versions.** Do not compare systems or periods across a regenerated taxonomy without bridge mappings and stability evidence.
7. **Keep generated rubrics non-authoritative.** They may propose apparent requirements; expert/source-backed criteria and private-but-fair consequences remain independently versioned.
8. **Preserve plural graders.** Deterministic artifact/state checks, model observations, and human/domain observations should coexist before adjudication.

### Test

1. **Adapter conformance:** feed semantically equivalent MLflow/Langfuse fixtures and verify node/order/content equivalence or typed differences.
2. **View sufficiency:** plant failures visible only in omitted environment state, intermediate screenshots, or the truncated middle; require abstention rather than confident diagnosis.
3. **Category stability:** rerun induction across trace bootstrap samples, order permutations, judge seeds/models, prompt variants, and category caps; report split/merge/membership stability.
4. **Held-out criterion validity:** independently label candidate issue truth, evidence location, surface/root status, and severity on held-out traces with adjudication and clustered intervals.
5. **Negative cases:** include successful traces that contain alarming language, legitimate retries, repeated polling, correct refusals, and downstream symptoms caused upstream.
6. **Causal slice test:** compare node grouping with dependency-backed slices and planted upstream/downstream faults.
7. **Intervention utility:** assign developers candidate diagnoses versus raw traces under matched review budgets, implement blinded fixes, and rerun equivalent held-out tasks. Measure true repair, regressions, false leads, time, and cost.
8. **Taxonomy drift bridge:** regenerate categories on a later instrument version and test whether apparent issue-frequency changes survive a frozen bridge taxonomy.

## Action items for repository

- [x] Read the complete immutable v1 PDF/text and preserve versioned provenance.
- [x] Inspect the complete official 137-file archive at commit `28a16d4f055697292908a5b87b3fd30ab21dc6e6` with its post-v1 timing boundary.
- [x] Reconstruct all seven settings and the 1,129-trace denominator.
- [x] Audit adapters, compact trace view, step/full/rubric/task-success prompts, issue induction/dedup/remapping, dashboard frequency, invalid handling, caching, concurrency, and sample outputs.
- [x] Separate issue discovery, category stability, criterion alignment, root support, success association, and intervention utility.
- [x] Compare with STRACE, Signals, AgentRewardBench, Tool-Veritas, EvalAgent, and Auto Benchmark Audit.
- [x] Add no queue task: the requirements refine existing trace/evidence-view, grader observation, root/surface attribution, task-health, metric-monitoring, validity-argument, and compounding-lesson machinery. A new subsystem would duplicate those contracts.
