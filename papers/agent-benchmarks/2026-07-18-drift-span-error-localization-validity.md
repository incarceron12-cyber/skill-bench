# Paper Review: DRIFT/TELBench span-localization validity

- **Paper:** <https://arxiv.org/abs/2606.02060v2>
- **Authors:** Jiaming Wang, Ziteng Feng, Jiangtao Wu, Ruihao Li, Qianqian Xie, Yuxiang Ren, He Zhu, Xueming Han, Fanyu Meng, Junlan Feng, Jiaheng Liu
- **Date read:** 2026-07-18
- **Version read:** immutable arXiv v2, updated 2 June 2026
- **Local PDF:** `data/papers/pdfs/2606.02060v2-drift-deep-research-error-localization.pdf` (28 pages; SHA-256 `cf501782769204615fb0333bf7e84bd07a773012b59e31b2bfa8f97133448462`)
- **Local text:** `data/papers/text/2606.02060v2-drift-deep-research-error-localization.txt` (SHA-256 `68390cc89c54a26e3dff5a3c92b0cdfda6c84a79cf4778d66d22e6c40e72a819`)
- **Official code inspected:** <https://github.com/NJU-LINK/DRIFT/tree/1280b373b5af1954bf0577bf6d58b38e1bce341e>
- **Official dataset inspected:** <https://huggingface.co/datasets/NJU-LINK/TELBench/tree/307d870d7424be265653bb7a566793cc217105be>
- **Release provenance:** `data/sources/releases/2606.02060v2-drift/provenance.json`
- **Timing boundary:** the pinned code commit is dated 4 June and the pinned dataset revision reports 4 June, two days after immutable v2. They are acquisition-time official releases, not proved paper-time artifacts.
- **Tags:** trajectory-diagnosis, semantic-spans, evidence-support, first-error, annotation-validity, root-surface, release-correspondence

## One-sentence contribution

TELBench provides an unusually inspectable positive-case benchmark for finding expert-adjudicated harmful spans in 1,000 real research-agent trajectories, and DRIFT shows that a claim/support/dependency-shaped prompt pipeline agrees with those labels much better than generic full-context prompting; however, the study validates agreement with one outcome-aware, LLM-prefilled, lossy-span annotation instrument—not causal roots, repair utility, professional truth, or monitoring readiness—and the released runner materially differs from the four-stage method and prompts reported in v2.

## Why this matters for skill-bench

A useful knowledge-work benchmark should not stop at “the memo is wrong” or “the task failed.” It should identify the earliest supported breakdown and show how that breakdown propagated into later evidence use, decisions, artifacts, and checks. DRIFT's strongest reusable idea is to make **claim state** the bridge between raw activity and diagnosis:

`raw event → semantic span → claim introduced → claim becomes consequential → support state → later reuse/finalization → surfaced failure`

This is better than treating every failed search, tentative hypothesis, or tool retry as an error. The paper's distinction between exploration and commitment is directly applicable to messy professional work: weak evidence is not automatically a failure, but adopting it past a declared decision threshold can be.

The evidence also shows why `skill-bench` must not collapse different diagnostic claims. TELBench's released target is an expert-approved span set under one evidence view. That is not automatically:

1. the first raw event where the system diverged;
2. the earliest necessary or sufficient cause of the bad artifact;
3. a source-external factual or professional error;
4. the best locus for intervention;
5. a diagnosis that repairs future work;
6. a production-ready monitor.

This review advances charter objectives A–C by examining a general diagnostic-measurement mechanism. Deep research is a bounded case because its traces make evidence adoption visible; it is not a proposal to narrow `skill-bench` to research QA.

## Research question and licensed claim boundary

The paper asks whether long research-agent trajectories can be normalized into semantic spans, annotated for harmful error commitments, and audited more accurately by a claim-centric pipeline than by bare or generic agentic readers (Sections 1, 3–5, pp. 1–8).

### What the evidence supports

- The authors report collecting 2,790 trajectories from 465 public tasks crossed with three base-model families and two agent frameworks (p. 3).
- They define a useful annotation distinction: a span is erroneous when it introduces, relies on, amplifies, or finalizes a mistaken, unsupported, contradicted, or premature judgment that affects the answer path; failed searches, recovered mistakes, tentative hypotheses, and tool noise are not errors by themselves (p. 3).
- The released TELBench payload is complete and inspectable. Publisher-checksum-verified local parsing confirms 1,000 unique trajectories, 11,934 spans, and 2,552 gold error assignments; all cases contain at least one error.
- Under the reported prompts and labels, DRIFT improves macro-F1 over the bare baseline for four displayed backbone families. Overall DRIFT F1 ranges from 48.41% to 54.91%, while first-error accuracy remains only 19.9%–24.1% (Table 2, pp. 6–7).
- The method's modular ablation is directionally consistent across reported models: claim extraction contributes the largest increase, with support and dependency stages adding further agreement (pp. 8, 17).
- The released code is a small executable package with data loading, sanitization, an on-demand span store, prompts, a concurrent runner, per-case logs, token capture, and a deterministic scorer. Its two release tests pass when the package source is placed on `PYTHONPATH`.

### What the evidence does not support

The study does not establish that the gold span is a causal root, that all relevant evidence survives normalization and segmentation, that annotations are independent of answers or LLM proposals, that the fault taxonomy is reliable, that DRIFT generalizes to no-error trajectories, that its diagnosis guides effective repair, that it improves human debugging, that released code reproduces the paper tables, or that span agreement licenses professional-validity, capability, safety, production-fitness, or readiness claims.

## Methodology and system

### Trajectory frame and configured systems

The authors begin with GAIA validation, XBench, and a 200-task downsample from BrowseComp test, totaling 465 tasks. Each task is run under GPT-5, Gemini 2.5 Pro, and Claude Sonnet 4.5 crossed with MiroFlow and OAgent, yielding exactly 2,790 trajectories (p. 3). Search and page reading are partially standardized to Serper and Jina, while framework-native non-retrieval tools remain different; Appendix B lists MiroFlow-specific vision, audio, and E2B code services but gives much less detail for OAgent (p. 12).

This is a useful configured-system corpus rather than a representative sample of research-agent traffic. The full corpus is a balanced design by nominal task/configuration crossing, but the released Verified-1K is selected after outcome, annotation, observability, boundary-stability, benign-distractor, and coverage review. Consequently, its framework, benchmark, model, outcome, difficulty, stage, and fault frequencies are **benchmark-construction frequencies**, not natural failure prevalence.

The paper reports one trajectory per task/configuration for corpus creation. The three repetitions mentioned on p. 6 apply to auditor settings, not repeated source-agent executions. Source-agent stochasticity, web-index time, page mutability, tool failures, and framework variance are therefore folded into each recorded trace.

### Raw event to semantic span: the unvalidated projection

Framework logs are normalized into execution units; tool calls are folded with results; nested subagent actions are expanded; manager messages are treated mainly as contextual summaries; boundaries are introduced when targets, candidates, time scopes, verification criteria, or objectives change (p. 3). LLM-assisted audits and human overrides handle abnormal and stratified cases.

This projection is sensible, but it is also a measurement treatment. It can:

- combine a mistaken commitment and later correction into one span;
- separate a claim from the evidence that gives it meaning;
- reorder nested multi-agent events according to reconstructed “semantic” rather than wall-clock/dataflow order;
- suppress manager messages that caused a worker action;
- fold tool calls and outputs such that actor, request, observation, and adoption become inseparable;
- hide omitted logs as apparent lack of support.

The released JSONL contains ordered span text, but not the original raw traces, normalization records, boundary proposals, human overrides, adapter versions, omitted-event manifests, or raw-event-to-span maps. The paper's case study 2 labels a worker report unsupported partly because corresponding worker tool calls are absent from the **visible** trajectory (pp. 19–20). That may identify unsafe adoption under the observed evidence view, but without raw-trace completeness it cannot distinguish agent fabrication from observability loss or projection omission.

No segmentation reliability statistic is reported. “Stable enough for evaluation” is a selection judgment, not demonstrated inter-segmenter agreement or invariance. Span IDs are therefore valid targets only conditional on this unreleased projection.

### Error annotation authority and hindsight

Two frontier LLMs from different families first propose high-recall error candidates with rationales and evidence references. Two experts sampled from a seven-person pool then inspect full trajectories, revise or add labels, and adjudicate disagreements and low-confidence/boundary cases. Annotators are described as experienced with agent systems, browsing, and tool-use failures; each reportedly spent more than 300 hours (p. 3).

Important safeguards are absent or ambiguous:

- The paper says “two expert annotators” but does not specify whether they label independently before discussion, how cases are allocated, whether both see every trajectory, or who adjudicates their disagreement.
- It reports no raw agreement, chance-adjusted agreement, per-fault agreement, boundary-distance agreement, confidence distribution, disagreement count, revision rate from LLM prefill, or expert-only control sample.
- The interface shows the task **ground-truth answer**, highlighted LLM candidate spans, proposed rationales, and stage cues (p. 12). Experts are therefore not blinded to outcome or suggestions.
- The paper does not report whether experts possess domain authority for the many subject-matter questions, whether they verify external sources, or whether the gold answer itself can be wrong or underdetermined.
- The released data includes only final stage and fault maps. It omits candidate proposals, initial independent labels, rationales, evidence locators, confidence, corrections, annotator IDs, adjudication lineage, and rejected candidates.

Outcome and proposal visibility are consequential. An annotator who knows the reference answer can work backward to find a plausible span explaining it, and a red-highlighted candidate can anchor the review. This does not invalidate the labels; it changes their construct to **outcome-aware expert adjudication of proposed harmful spans**. It is not blind detection of a failure from the same information available to the evaluated auditor.

The label definition also merges several predicates: mistaken, unsupported, contradicted, premature, consequential, adopted, amplified, and finalized. A span can be unsupported because the trajectory lacks evidence even when the claim is externally true; case study 2 intentionally labels a correct final answer's evidence chain erroneous. Conversely, trajectory-internal support can be internally coherent but factually false if all visible sources or extracted facts are wrong. TELBench principally measures conformance to a visible-evidence commitment policy, not full factual or professional correctness.

### Mechanism taxonomy

All spans receive one of eight workflow stages. Error spans receive exactly one of 18 faults in six families. The fault taxonomy is induced after binary labels: three LLMs write rationales, 4,631 cleaned keys are shuffled and hierarchically merged, humans normalize boundaries, and the taxonomy is back-labeled onto all errors (pp. 15–16).

The process is useful for exploratory vocabulary discovery, but “stable category structure” is asserted rather than tested. Random shuffle, chunking, model, prompt, reduction order, manual merges, and forced single-fault assignment can all change categories. No independent back-labelers, agreement, held-out induction, bootstrap/order stability, multi-label alternative, category confusion, or cross-framework invariance is reported. Fault frequencies and stage-by-fault plots should be treated as descriptions under one induced codebook—not an established ontology or root-cause distribution.

### TELBench selection and released population

From 2,790 traces, 1,890 have at least one annotated error. The authors retain 1,000 with clear boundaries, internal evidence, stable segmentation, benign distractors, and stratified coverage, then manually assign 600 easy and 400 hard cases based on length, evidence directness, distractors, and subtlety (p. 4).

The release confirms:

- 373 BrowseComp, 348 GAIA, and 279 XBench cases;
- 511 OAgent and 489 MiroFlow cases;
- 702 incorrect-answer and 298 correct-answer cases;
- 600 easy and 400 hard cases;
- 3–47 spans per case, mean 11.934 and median 10;
- 1–11 gold errors per case, mean 2.552;
- 2,552/11,934 = 21.38% positive spans.

All 1,000 cases are positive. This is a localization benchmark, not a monitor-calibration set. It cannot measure trajectory-level specificity, false alarms on fully healthy traces, abstention, positive predictive value under realistic low prevalence, or whether a system knows when no harmful commitment exists. The bare prompt permits an empty set, but the benchmark never rewards a correct empty decision.

Selection also creates a construct-aligned shortcut surface. My local audit found that 798/1,000 cases label the final span as erroneous. A predictor selecting only the last span obtains macro precision 0.798, recall 0.414, F1 0.508, and first-error accuracy 0.200. Using the hidden stage annotations to predict every `decide` or `finalize` span yields macro F1 0.660 and first-error accuracy 0.428. Stage labels are correctly withheld from evaluated prompts, so these are not admissible leaderboard baselines. They are diagnostic evidence that label topology is strongly tied to recognizable commitment/finalization language. Auditors can score well by learning the annotation policy's discourse locations without reconstructing support or causal dependency. A future benchmark should include stage-matched negative commitments, correct finalizations, recovered claims, and no-error traces.

Hard cases are longer and more densely labeled by construction: the release averages 14.06 spans and 3.86 gold errors for hard cases versus 10.52 and 1.68 for easy cases. Difficulty performance therefore mixes length, positive-set size, implicitness, and author judgment. It is not a calibrated latent difficulty scale.

### DRIFT's paper-time logic

The paper presents a global Claim Keeper; a Support Seeker assigning direct, weak, missing, or conflicting support; six routed Specialist Auditors; and a final Dependency Tracer (pp. 5–6, 23–28). Claims record introduction, first consequential use, downstream uses, type, and commitment status. The final stage should mark only unsupported/conflicting claims that are committed, reused, amplified, or finalized.

This architecture encodes a good diagnostic prior: local suspiciousness is insufficient; harmfulness depends on claim state and use. Yet all stages are produced by language models from the same span representation. A graph edge is a model assertion, not observed dataflow. “Support” is evaluated only from trajectory text, not from frozen authoritative source bytes. The pipeline has no independent entailment verifier, no competing dependency graph, no counterfactual repair, and no intervention on the source agent. Better agreement can arise from decomposition, more calls/tokens, prompt-label alignment, or stage-language exploitation; it does not establish causal tracing.

### Metrics, repetitions, and uncertainty

The paper reports per-case macro precision, recall, F1, and exact first-error accuracy, with each setting repeated three times (p. 6). These metrics appropriately keep span-set overlap and first-locus agreement separate. The result itself is sobering: DRIFT's best shown overall first-error accuracy is 24.1%, and hard-split values are 7.25%–12.0% (Table 2). This supports the conclusion that earliest-label agreement remains difficult.

But the analysis omits:

- dispersion or confidence intervals over the three repeated calls;
- task-, source-task-, benchmark-, or configured-source-agent-clustered uncertainty;
- prediction invalidity, retries, provider failures, and missing rows;
- significance tests for methods or model ordering;
- run-level seeds, endpoint snapshots, temperatures, and per-repetition outputs;
- a held-out development/test boundary for prompt tuning;
- correction for the public release exposing gold labels and annotations.

The 1,000 rows also arise from only 465 source questions, with up to six configured trajectories per question. Treating rows as independent would overstate evidence when question structure drives labels. Macro-F1 is useful descriptive agreement, not a population parameter with demonstrated precision.

## Evidence and result interpretation

DRIFT consistently exceeds the reported bare and generic-agent baselines on macro-F1. This is credible evidence that a claim/support-oriented workflow is better aligned with TELBench's claim/support-oriented annotation policy than a single read or repurposed coding agents. Module additions show monotonic reported gains, and the package records per-stage outputs, making mechanism inspection possible.

The causal interpretation is weaker. DRIFT and the target share vocabulary and logic: commitment, unsupported claim, consequential use, and first harmful span. That is legitimate instrument design, but it creates criterion coupling. No independently authored annotation policy, alternate span representation, external-evidence condition, intervention condition, or repair test shows that gains transfer beyond this rubric.

The paper's headline says DRIFT improves localization and first-error accuracy “by up to 30 percentage points.” Table 2 supports large macro-F1 gains for some backbone/split combinations, but first-error gains are much smaller in the displayed rows. More importantly, first-error **label agreement** should not be renamed root-cause accuracy. The earliest labeled commitment may be downstream of an omitted observation, faulty query construction, framework scheduling error, source defect, or earlier tentative hypothesis that became harmful only later. The benchmark intentionally labels commitments rather than every precursor. That is a defensible construct, but it is not causal origin.

The reported cost evidence is token accounting only. DRIFT uses roughly 17.7k–53.0k average tokens per case depending on backbone, compared with about 6.0k–14.3k for bare prompting (Table 5, p. 16). It omits wall time, provider cost, failure/retry overhead, expert construction labor, and human review saved. No study shows that higher label agreement shortens debugging or improves repairs.

## Release audit and reproducibility

The dataset release is strong for row-level inspection. It is public, Apache-2.0, publicly decryptable, checksum-verified, and structurally complete. Local parsing reproduces the advertised 1,000 rows and 11,934 spans. IDs and source IDs are unique, gold IDs are ordered, stage labels cover every span, and fault labels cover every gold error.

The release does not include the other 1,790 trajectories, raw framework logs, span-construction code/records, annotation UI code, annotator proposals, rationales, agreement tables, reviewer assignments, difficulty decisions, source-task crosswalk, corpus-generation manifests, paper predictions, three repeats, evaluation tables, or analysis notebooks. Paper-level dataset construction and reported scores therefore cannot be independently rebuilt.

More seriously, the post-v2 code is not the four-stage method printed in the paper:

1. The release implements three model calls—Claim Keeper, Support Seeker, Dependency Tracer—not the paper's routed six Specialist Auditors and final reducer.
2. `build_support_context_request_prompt` exists but `run_drift` never calls it. Context requests are generated deterministically from claim endpoints and the first 160 characters of claim text.
3. The span store tokenizes the full generated claim, scores chunks by summed term frequency, keeps at most four matches per query and eighteen chunks total, and falls back to the last chunk when an explicitly requested span has no lexical hit. This is a lexical retrieval treatment, not the paper's described specialist graph audit.
4. After the Dependency Tracer predicts spans, `add_late_support_endpoints` automatically appends consequential/finalized claim completion endpoints that occur after the first predicted error, regardless of the Support Seeker's support status. This deterministic post-processing is aligned with a dataset where 79.8% of final spans are positive and can improve follow-up recall without validating dependency.
5. Provider exceptions are converted into empty fallbacks rather than invalid trials. Unless consumers inspect `_fallback_error`, failed model calls can become ordinary negative predictions and enter metrics.
6. The scorer reports missing prediction IDs but scores every gold case using `pred.get(cid, [])`; missing rows therefore become empty predictions in the fixed denominator. That is defensible only if invalid/provider-failure counts remain separately reported.
7. The release's two tests check prompt naming and dependency-trace sanitization. They do not test paper-score reproduction, support retrieval, no-error behavior, automatic endpoint additions, provider-failure semantics, or annotation stripping end to end.

This does not make the release useless. It is a compact, runnable **post-v2 realization** of a related claim-centric auditor. It cannot be cited as the exact implementation that produced Table 2 without a version correspondence manifest and released predictions. The paper's complete appendix prompts also differ from `src/drift_open/prompts.py`; reproducibility requires binding each result to prompt/code/data/model hashes, not merely method names.

## Unique insight

The deepest transferable insight is that diagnostic validity has two independent projections:

```text
execution projection
raw events/state → normalized events → semantic spans

causal-semantic projection
spans → claims → support states → dependencies → harmful commitments
```

An auditor can agree perfectly with the second projection while the first omitted the actual cause. Conversely, a raw-event locator can be temporally exact but semantically unhelpful if it marks a harmless search rather than the point where unsupported evidence became decision-relevant. A useful benchmark must preserve and validate both projections.

This yields a claim ladder that TELBench currently reaches only partway:

1. **span agreement:** prediction matches an adjudicated semantic span;
2. **commitment-policy agreement:** prediction identifies where the annotation policy says a weak/false claim became harmful;
3. **evidence-view sufficiency:** required raw state and source evidence demonstrably survived normalization;
4. **supported dependency:** observed data/control/evidence-use links connect precursor, adoption, and surface;
5. **earliest supported cause:** alternatives are considered and an earlier supported locus is absent;
6. **repair utility:** changing the diagnosed locus improves equivalent held-out outcomes;
7. **professional validity:** domain-authorized evidence says the diagnosis and repair matter in the target workflow;
8. **operational readiness:** calibrated prevalence, false alarms, abstention, cost, drift, and human consequences support deployment.

TELBench directly measures rung 1 and is intentionally designed around rung 2. DRIFT's internal records are hypotheses toward rungs 3–4. Neither paper nor release establishes rungs 5–8.

The benchmark's all-positive composition adds a second insight: **localization among known failures and monitoring under unknown failure prevalence are different instruments**. A system can have good positive-case span F1 while flooding healthy trajectories with alarms. Positive-case diagnosis should not be promoted into a monitor without a probability sample, no-error trajectories, abstention policy, prevalence-aware precision, and review-cost measurement.

## Comparison with adjacent reviewed work

- **STRACE** (`papers/agent-benchmarks/2026-07-09-strace.md`) aims to infer execution dependency graphs and causal slices for optimization. TELBench is stronger on released span labels and benchmark inspectability, but neither validates inferred roots with counterfactual repair.
- **Who&When Pro** (`papers/agent-benchmarks/2026-07-15-whowhen-pro-failure-attribution-validity.md`) has a known injected action but weak evidence that it is the unique earliest sufficient cause. TELBench has natural trajectories and human-adjudicated commitments but no controlled intervention. Together they show that intervention identity and annotation agreement are different, incomplete forms of causal evidence.
- **AutoTrace** (`papers/agent-benchmarks/2026-07-18-autotrace-trigger-causal-chain-validity.md`) separates authoritative outcome contrast from mechanism and endpoint truth. TELBench similarly should separate answer truth, visible-evidence support, harmful commitment, and root-cause truth.
- **Agentic CLEAR** (`papers/agent-benchmarks/2026-07-17-agentic-clear-dynamic-diagnostic-validity.md`) compresses model critiques into dynamic issues without root validation. TELBench offers a sharper fixed span target, while DRIFT's generated claim ledger remains an unvalidated intermediate rather than an observed causal graph.
- **Signals** (`papers/agent-benchmarks/2026-07-14-signals-trajectory-triage-sampling-validity.md`) distinguishes enriched review yield from prevalence. TELBench is deliberately enriched for verifiable error-bearing cases and therefore cannot estimate production failure or alert rates.

## Limitations and validity threats

1. The 465-task corpus is a selected public-benchmark frame, not a target knowledge-work population.
2. One source-agent run per task/configuration leaves execution stochasticity unmeasured.
3. Search/page state is mutable and collection-time retrieval snapshots are unreleased.
4. Framework tools remain partly non-equivalent despite shared search/read interfaces.
5. Raw logs are projected into semantic spans through unreleased, partly subjective transformations.
6. Nested action order and manager-summary handling may remove or reorder causes.
7. No raw-event-to-span lineage permits projection auditing.
8. No segmentation agreement or perturbation study establishes boundary stability.
9. Missing visible support can reflect observability loss rather than agent error.
10. LLM candidates and rationales prefill expert review.
11. Experts see the gold answer, candidate highlights, rationales, and stage cues.
12. Expert independence, allocation, blinding, training, and adjudication are under-specified.
13. No binary-label, boundary, stage, or fault agreement statistic is reported.
14. No candidate acceptance/rejection or correction rate quantifies automation anchoring.
15. Annotator domain authority and external-source verification are not established.
16. Gold-answer error and underdetermination are not audited.
17. The binary target merges falsity, missing support, conflict, prematurity, adoption, and harmfulness.
18. Trajectory-internal support is not external factual or professional truth.
19. The fault taxonomy is LLM-induced and manually normalized without stability or held-out reliability evidence.
20. Exactly one primary fault erases co-causes and alternative descriptions.
21. The Verified-1K is selected after error annotation and boundary/observability review.
22. Selection attempts, exclusion counts by reason, and inclusion probabilities are unreleased.
23. All 1,000 cases are error-positive, so specificity and healthy-trace false alarms are unmeasured.
24. Final spans are positive in 79.8% of released cases, creating a strong discourse-position shortcut.
25. A hidden-stage `decide/finalize` oracle reaches macro-F1 0.660, showing stage-label topology stronger than paper auditors.
26. Easy/hard labels combine length, positive count, evidence subtlety, distractors, and judgment.
27. Multiple configured trajectories share source questions, but uncertainty does not cluster by question.
28. Three auditor repetitions have no reported variance, confidence intervals, or raw predictions.
29. Endpoint/model versions, sampling seeds, invalid outputs, retries, and provider failures are not bound to tables.
30. Prompts may have been tuned on the same public 1,000 labels; no development/test boundary is stated.
31. DRIFT's claim/support/dependency vocabulary is tightly coupled to the annotation definition.
32. Better target agreement does not prove source support, causal dependency, or earliest cause.
33. No correction, deletion, replay, or intervention validates a diagnosis.
34. No study measures diagnosis-guided repair, human debugging utility, regressions, or false leads.
35. Token accounting is not total diagnostic cost or cost per useful repair.
36. The release postdates v2 and is not proved to be the paper-time implementation.
37. Released DRIFT omits the paper's Specialist Auditor stage.
38. The released context-request prompt is dead code in the runner.
39. Released lexical claim retrieval is capped and can omit decisive evidence.
40. Released post-processing automatically adds late claim endpoints without checking support status.
41. Provider exceptions fall back to apparently ordinary empty outputs unless error metadata is audited.
42. Only two narrow release tests exist; no table-reproduction or behavioral conformance suite is provided.
43. Paper predictions, repeats, costs, annotation records, and analysis scripts are absent.
44. Public gold and annotation maps create saturation/contamination risk for future leaderboard use.
45. No evidence supports professional capability, cross-domain diagnostic validity, production monitoring, safety, or readiness.

## Reproducibility and operational realism

**Dataset inspectability is high; experiment reproducibility is low-to-moderate.** The official payload is complete, integrity-checked, parseable, and rich enough to audit every released span, gold set, stage, fault, and coarse metadata field. The released runner is readable and executable, and its minimal tests pass. This is substantially stronger than a paper with no rows or code.

Exact paper reproduction remains blocked. Raw source trajectories and their projection lineage are absent; annotation histories and agreement are absent; the complete corpus and selection ledger are absent; paper predictions/configurations are absent; and the available runner changes the architecture and prompts. A reproducer can evaluate a new configured release auditor against the public rows, but cannot establish that it has recreated Table 2 or the original gold construction.

**Operational realism is moderate for recorded research-agent diagnosis and low for monitoring/readiness.** The traces come from real runs with search, tools, failed exploration, and correct-answer/unsafe-evidence cases. That is valuable. Yet public benchmark questions, post-hoc answer-aware adjudication, an all-positive enriched set, missing raw state, and no human repair workflow differ sharply from production review. Real operation requires no-error traffic, unknown prevalence, frozen evidence access, source authority, false-alarm cost, escalation/abstention, drift, privacy, review time, and demonstrated intervention utility.

## Transfer to skill-bench

### Retain

1. **Claims as stateful objects.** Record introduction, tentative/committed/finalized state, support, contradiction, adoption, reuse, and artifact consequence separately.
2. **Benign exploration negatives.** Failed searches, retries, hypotheses, and recovered mistakes are essential hard negatives.
3. **First locus and full chain as separate scores.** Exact earliest agreement and set/edge coverage answer different questions.
4. **Positive cases with correct outputs but bad evidence.** Outcome correctness should not erase unsupported process risk.
5. **Multi-resolution evidence.** Preserve raw events, normalized events, semantic spans, claims, support records, and surfaced checks as linked—not substitutable—views.
6. **Executable release rows.** TELBench's checksum-verified JSONL and small scorer are worth emulating.

### Repair

1. **Freeze both projection lineages.** Bind each semantic span to raw event IDs, actor, wall/causal order, omitted channels, normalization code/hash, boundary proposal, override, and transformation rationale.
2. **Separate predicates.** Label factual status, source entailment, authority, scope/freshness, observability sufficiency, commitment status, harmful consequence, recovery, and surface/root status independently.
3. **Blind and pluralize annotation.** Include answer-withheld and proposal-withheld independent rounds, expert authority/scope, initial labels, confidence, disagreement, and adjudication; report agreement at raw-event, span, predicate, and fault levels.
4. **Add no-error and stage-matched controls.** Include correct finalizations, legitimate commitments, weak-but-nonconsequential evidence, recovered errors, alarming language without failure, and fully healthy trajectories.
5. **Preserve source-task clusters and selection ledgers.** Report all 2,790 dispositions and cluster uncertainty by original task/configuration.
6. **Bind release correspondence.** Every table should reference immutable data, prompt, runner, model endpoint, provider policy, raw predictions, invalid rows, scorer, and analysis hashes.
7. **Fail closed on missing evidence/provider failure.** `insufficient_observability` and `invalid_trial` must not become “no error.”
8. **Do not auto-promote endpoints.** Every propagated span needs an explicit supported reuse/finalization edge, not a deterministic completion heuristic.

### Test

1. **Projection conformance:** independently segment a stratified raw-trace sample and perturb fold/order/boundary policies; measure label and rank stability.
2. **Observer factorial:** answer visible/withheld × LLM prefill visible/withheld × stage cue visible/withheld × raw/span evidence view.
3. **Stage-shortcut controls:** compare claim-centric auditors against position-, discourse-, stage-, and finalization-matched baselines on held-out no-error and recovered-error cases.
4. **External-evidence sufficiency:** freeze authoritative source bytes and distinguish unsupported-in-trace from externally false, externally true-but-unlogged, and unobservable.
5. **Causal intervention slice:** on an existing artifact-heavy pilot, plant one upstream evidence-selection defect and one downstream surface defect; run original, injected, repaired, sham, and dual-fault continuations under repeated seeds.
6. **Repair utility:** compare raw-trace review with diagnosis-assisted review under matched human time; measure correct repair, false leads, recurrence, collateral regression, artifact quality, and cost.
7. **Monitoring bridge:** evaluate on a probability sentinel stream containing healthy and invalid traces before estimating alert precision, prevalence, or review burden.

## Concrete repository actions

- [x] Read the complete immutable v2 PDF/text and preserve exact paths and hashes.
- [x] Inspect the complete pinned official 43-blob code release and checksum-verified decrypted 1,000-row TELBench payload.
- [x] Reconstruct collection, semantic projection, annotation, taxonomy, selection, configured auditor, metrics, and cost claims.
- [x] Audit all released rows for counts, uniqueness, positive density, stage/fault coverage, outcome/framework/benchmark composition, and position/stage shortcut baselines.
- [x] Run the released test suite successfully with the pinned package source on `PYTHONPATH`.
- [x] Separate span agreement, commitment-policy agreement, evidence-view sufficiency, dependency support, causal root, repair utility, professional validity, and operational readiness.
- [x] Compare nonduplicatively with STRACE, Who&When Pro, AutoTrace, Agentic CLEAR, and Signals.
- [x] Add no queue task. Existing trace/evidence-view, root/surface, intervention/recovery, validity, task-health, metric-monitoring, and compounding-lesson machinery already houses the requirements; prior diagnostic reviews already specify the needed original/injected/repaired/sham empirical slice. Another DRIFT-specific contract would duplicate that work.

## Bottom line

TELBench is a valuable positive-case localization release. Its full 1,000-row payload is inspectable, its label policy correctly distinguishes exploration from harmful commitment, and the reported results show that explicit claim/support structure can materially improve agreement over generic reading. The low hard-split first-error accuracy is itself useful evidence that early commitment localization remains unsolved.

The benchmark should be described precisely: it measures agreement with outcome-aware expert-adjudicated harmful semantic spans under a lossy trajectory-internal evidence view. It does not validate causal roots, and its all-positive, finalization-heavy selection does not validate monitoring. The post-v2 release is a related three-call auditor whose dead context-request prompt, lexical evidence cap, automatic late-endpoint addition, and specialist-stage omission prevent treating it as the exact paper instrument. `skill-bench` should retain claim-state and benign-exploration structure while requiring raw-to-span lineage, predicate-separated labels, blinded plural annotation, no-error controls, and intervention/repair evidence before a localized span becomes a root cause or a compounding lesson.

## Source links

- Immutable abstract: <https://arxiv.org/abs/2606.02060v2>
- Immutable PDF: <https://arxiv.org/pdf/2606.02060v2>
- Official code: <https://github.com/NJU-LINK/DRIFT>
- Pinned code: <https://github.com/NJU-LINK/DRIFT/tree/1280b373b5af1954bf0577bf6d58b38e1bce341e>
- Official dataset: <https://huggingface.co/datasets/NJU-LINK/TELBench>
- Pinned dataset: <https://huggingface.co/datasets/NJU-LINK/TELBench/tree/307d870d7424be265653bb7a566793cc217105be>
- Local provenance: `data/sources/releases/2606.02060v2-drift/provenance.json`
