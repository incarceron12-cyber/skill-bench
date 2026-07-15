# Production selective re-evaluation repairs record shape—not evaluator validity

## Source and review status

**Deep review of the complete immutable arXiv v1 HTML/full text.** I read the full manuscript from abstract through all eight sections, both tables, the figure placeholder, limitations, and references. I also rechecked the immutable metadata for withdrawal language, retried the versioned PDF endpoint, and reviewed the recorded official-release search.

- **Paper:** Niranjan Kumar M, Balaji Nagarajan, Karthik Nair, Faysal Satter, and Nithin Surendran, *Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking*, arXiv:2607.12085v1, <https://arxiv.org/abs/2607.12085v1>
- **Version read:** immutable v1, submitted 13 July 2026; metadata contains no withdrawal or retraction notice
- **Date read:** 2026-07-15
- **Immutable HTML:** `data/papers/source/2607.12085v1/2607.12085v1.html` (SHA-256 `db5c3df21c8b1e9a300448b3e060b989425b301082776968bb26dbd256bb01fd`)
- **Local text:** `data/papers/text/2607.12085v1-production-evaluation-selective-reexecution.txt` (SHA-256 `369e6198bb02caa71abbd3ed216000453c5c27c7ec6ff967b5ff21b290434296`)
- **Metadata:** `data/papers/source/2607.12085v1/metadata.xml` (SHA-256 `61f4087a2078336b6c91d4a8033989d8e614d69fd7388847c909a14f09ad9de7`)
- **Acquisition/release provenance:** `data/sources/releases/2607.12085v1-production-evaluation/provenance.json`
- **PDF boundary:** <https://arxiv.org/pdf/2607.12085v1> still returned HTTP 404 after a fresh retry. No substitute is represented as the arXiv PDF. Section and table locators below refer to the complete immutable HTML rather than invented PDF pages.
- **Release status:** no author-owned code, data, YAML configuration, prompt, schema, annotation guide, model output, cost table, or project repository is linked by v1 or was found in the recorded exact-title/arXiv-ID web and GitHub searches. This is a provisional search result, not proof that no artifact exists.
- **Tags:** production evaluation, LLM judge, selective retry, schema validity, human annotation, missingness, attempt provenance, throughput

## One-sentence contribution

The paper describes a plausible Kubeflow/BigQuery/Parquet pipeline that versions evaluator configurations and selectively retries malformed or schema-invalid judge records at reported two-million-record scale, but it neither specifies the retry transaction well enough to show outcome-neutral idempotent repair nor reports enough human-label, denominator, uncertainty, throughput, cost, or release evidence to promote final-record completeness into judge validity, operational reliability, production utility, or agent quality.

## Why this matters for skill-bench

This paper addresses a real but easily misunderstood operating boundary:

```text
source interaction
→ normalized eligible record
→ configured evaluator attempt
→ parsed/schema-valid observation or typed invalidity
→ retry eligibility and bounded re-execution
→ retained attempt lineage and final observation
→ human/reference comparison
→ population metric
→ monitoring or benchmark decision
```

The distinctive contribution is selective re-execution at the **record** level rather than full-job reruns. That can reduce wasted evaluator work and recover parser or serving failures. Yet a valid row is not necessarily a correct judgment, and a retried row is not automatically comparable with a first-attempt row. If eligibility includes substantive score values, if only successful final attempts survive, or if prompt/model/configuration changes between attempts, the retry loop can become outcome-conditioned selection rather than infrastructure repair.

This advances charter objectives A and C through a bounded retail-conversation case that stress-tests reusable trial, grader, provenance, missingness, and metric machinery. It does not narrow `skill-bench` to retail chat or imply that turn-level conversational scoring is representative of artifact-heavy knowledge work.

## Research question and defensible claim boundary

The engineering question is how to operate high-volume, multidimensional LLM-judge evaluation over production conversational logs while retaining schema consistency, traceability, resumability, and targeted recovery. The empirical questions are whether selected open evaluator configurations agree with available human/reference labels and whether the pipeline handles large record volumes.

The source supports bounded claims that:

- the authors describe a configuration-driven Kubeflow pipeline with BigQuery ingestion, normalization, four round-robin shards, asynchronous bounded-concurrency evaluation, schema-locked Parquet writes, validation, selective re-evaluation, and BigQuery publishing (Sections 3–4);
- the operated workload is reported as approximately 50,000 records per day and more than two million records overall, with a reported 95/5 non-translation/translation mix (Section 5.1 and Table 1);
- four trained annotators each labeled different records in a 12,980-record stratified sample, with one label per record and no inter-annotator reliability estimate (Sections 5.1–5.2);
- Table 2 reports macro F1 from 0.82 to 0.93 and translation acceptability accuracy from 0.78 to 0.89 across five aliased open-model configurations under 4-bit quantization, H100 hardware, batch size 512, and temperature 0.005;
- malformed, incomplete, missing-score, parsing-failed, schema-violating, and out-of-range records are eligible for up to three retries (Sections 4.2, 5.1, and 5.6).

It does **not** establish judge correctness against reliable expert consensus; calibrated 1–5 quality scores; subgroup or long-tail validity; unbiased final-record metrics after retry; exact-once/idempotent execution; reliability over evaluation opportunities; measured throughput or quality–throughput trade-offs; cost savings; downstream customer or associate benefit; professional quality; conversational-agent capability; safe production operation; or cross-domain readiness.

## Methodology and system reconstruction

### Record identity, preprocessing, and sharding

A turn is modeled as prompt, response, and metadata, with metadata including user, conversation, context, timestamps, retail context, source, out-of-coverage status, and tool flags (Section 3.1). Preprocessing renames and casts fields and filters empty prompts/responses, missing user/conversation IDs, and malformed timestamps (Section 3.2). The clean frame is split into four round-robin shards using `df.iloc[i::N]`, re-indexed, and serialized to Parquet. Each record receives a stable global row ID, shard/worker metadata, evaluator model, prompt-template version, configuration hash, and evaluation timestamp.

This is a useful inventory, but key identity semantics are absent:

- no derivation, canonicalization, collision policy, or source-version binding is given for the stable row ID;
- no immutable input-record/content hash connects raw and normalized values;
- the BigQuery snapshot/query, ordering, source revision, deduplication key, and late-arrival policy are unspecified;
- round-robin slicing is deterministic only relative to a frozen ordered frame, which the paper does not define;
- filtering removes records before evaluation without reporting counts, reasons, subgroup effects, or whether those exclusions remain in the operational denominator;
- four near-equal row counts do not establish balanced compute because prompt length, context, translation, and evaluator work can differ sharply.

Thus the manuscript describes fields that could support identity; it does not release evidence that the reported two-million-record corpus had stable record identity or a reconstructable eligibility frame.

### Evaluator and output schemas

YAML configurations and Jinja2 prompts reportedly define rubrics, model settings, task schemas, and output dictionaries (Section 4.1). Non-translation records can receive intent/sub-intent and product-group classifications plus 1–5 scores for dimensions such as helpfulness, clarity, coherence, conciseness, creativity, instruction adherence, tone, and truthfulness. Translation records can receive semantic accuracy, readability, cultural appropriateness, selling relevance, and template fit (Sections 3.2 and 5.3–5.4). Optional rationales are diagnostic, not ground truth.

The multidimensional separation is preferable to one opaque quality score. However, no complete prompt, rubric anchors, schema, dimension applicability rules, evidence-view specification, reference-access rule, weight vector, normalization choice, or rationale policy is released. Section 5.4 says dimensions *can* be z-score or min–max normalized before weighted aggregation; it does not state what was actually used for Table 2 or production outputs. The paper also combines three target-authority mechanisms—single human labels, available gold/expected outputs, and task-specific weak-supervision heuristics—without reporting which record/task uses which authority or how results are separated.

Schema locking can ensure that a field is present and in range. It cannot establish that “truthfulness” is supported by an authoritative source view, that a translation criterion has a fair reference basis, or that 1–5 values are comparable across models, dimensions, languages, days, and prompt versions.

### Selective re-evaluation transaction

The core loop inspects outputs, isolates malformed, incomplete, missing-score, parsing-failed, schema-violating, or out-of-range rows, reruns only those rows up to three times, validates again, and merges by stable row ID (Sections 4.1–4.3, 5.1, and 5.6). Logs reportedly retain regeneration status and execution metadata.

The paper does not provide the minimum transaction semantics needed to evaluate this mechanism:

1. **Eligibility is not cleanly typed.** Parser failure and missing required fields are evaluator-invalid states. An out-of-range score may be parser-invalid, but it is also a model-produced substantive value. No rule separates transport failure, truncation, parse failure, schema failure, judge abstention, insufficient evidence, not-applicable criterion, and substantive low/high judgment.
2. **The retry treatment is unspecified.** It is unclear whether retries reuse exact prompt bytes, model weights/endpoint, decoding seed, batch context, schema/parser, worker, and configuration hash; whether failures trigger prompt repair; or whether retries cross a deployment/configuration boundary.
3. **Attempt retention is unclear.** “Regeneration status” and timestamped logs are not an explicit append-only ledger of every request, raw response, parser output, invalid reason, token/cost/latency, and selection decision. The merge rule, conflict policy, and final-attempt choice are absent.
4. **No outcome firewall is stated.** A safe repair policy should be fixed before observing substantive criterion values and should never retry a schema-valid unfavorable judgment merely because it is inconvenient. The paper gives no executable invariant proving this.
5. **Censoring remains.** After three failures, the paper does not say whether the row is retained as invalid, dropped, blocks publication, or changes the metric denominator.
6. **No recovery evidence is reported.** There is no initial-invalid count, reason distribution, retry-success curve, residual-invalid count, subgroup/model dependence, duplicated-publication count, wall-time/cost saved, or comparison with full rerun.

The mechanism is therefore a credible design pattern but not an empirically validated recovery policy. Its key estimand should be `valid observations / attempted eligible source records`, accompanied by initial/final invalidity and attempt-count distributions—not merely scores among final valid rows.

### Idempotency and reproducibility claim

Section 4.3 says components are stateless and idempotent and that rerunning a failed stage produces identical results without duplication. This claim conflicts with the described system unless “identical” is sharply scoped. The evaluator is stochastic at temperature 0.005, retries regenerate outputs, evaluation timestamps change, model serving can drift, and publishing is described as **append** to partitioned BigQuery tables rather than a released transactional upsert. The paper supplies no idempotency key, exactly-once write protocol, deterministic seed policy, content-addressed output, or replay test.

Likewise, “deterministic Parquet streaming” can mean deterministic column/schema handling; it does not make LLM judgments deterministic or reproduce a BigQuery append. Versioned configuration metadata improves traceability, but no configuration artifact or canonical hash procedure is available to verify exact realization.

### Human validation

The 12,980 validation records are described as stratified-random for balanced classification coverage. Four trained annotators use the same standardized rubric as the evaluators, are blinded to evaluator identity, and label disjoint subsets; each record receives one label (Sections 5.1–5.2). The paper appropriately acknowledges that this design cannot estimate inter-annotator agreement.

Further limits are material:

- the eligible population, dates, stratum construction, allocation counts, inclusion probabilities, and train/calibration/test relationship are absent;
- “balanced coverage” changes class composition, but no weights connect the validation sample to production prevalence;
- annotator roles, domain/language qualifications, training, calibration examples, interface, evidence view, workload, compensation, and adjudication protocol are absent;
- no overlap means annotator threshold and assigned subset are confounded;
- one shared rubric can induce human–judge policy agreement without establishing criterion authority;
- no class-wise support, precision/recall, confusion matrix, subgroup error, interval, repeated-call stability, or drift result is reported;
- the denominator and label mapping behind 89% translation “human-acceptability accuracy” are unspecified;
- numeric helpfulness/truthfulness/clarity labels are collected, but no correlation, absolute error, calibration, or threshold agreement is reported.

The correct interpretation of 0.93 and 0.89 is agreement with the available single-label policy under an incompletely specified sample—not agreement with adjudicated expertise or evidence that production quality is 93% or 89%.

### Model benchmark, throughput, and cost

Table 2 lists five aliased configurations: Llama-family 4B/8B/70B, Qwen3-14B, and “OSS evaluator” 120B. All use 4-bit quantization, H100 hardware, batch size 512, identical prompts/schemas/validation logic, and temperature 0.005. Reported F1 and translation accuracy rise non-monotonically with size.

The paper then asserts a clear quality–throughput trade-off and recommends small-model screening plus large-model escalation. Yet Table 2 reports **no throughput, latency, GPU count, memory, queue time, power, token volume, retry rate, or infrastructure cost by model**. The approximately 50,000 records/day figure is a workload volume, not a measured processing rate unless elapsed window, resources, backlog, and completion denominator are supplied. “No proprietary API cost” only says the evaluators were self-hosted; it does not quantify H100, orchestration, storage, annotation, or engineering cost. The tiered strategy is a reasonable hypothesis, not an evaluated policy.

Model identity is also too vague to reproduce: family aliases, exact checkpoints/revisions, serving software, quantization implementation, context settings, seeds, and weights are absent. Holding hardware class and nominal batch size fixed does not make evaluator behavior the only treatment difference when model architecture, tokenizer, serving realization, memory pressure, invalid-output propensity, and effective throughput differ.

## Evidence interpretation

### What the evidence supports

1. High-volume evaluator operation benefits from separating source-record identity, configuration identity, evaluator attempts, schema validation, and publication.
2. Record-level recovery is more economical in principle than rerunning an entire valid shard when only some outputs are malformed.
3. Schema-invalidity and substantive evaluation are different events and should be measured separately.
4. A single-label human comparison can provide preliminary concordance evidence while remaining explicitly below consensus/reliability evidence.
5. Reported production volume is evidence that the authors encountered an operational scale problem, not evidence that the evaluator produced valid or useful decisions at that scale.

### What the evidence does not support

No raw counts or artifacts allow recomputation of Table 2, the human comparison, initial/final invalid rates, retry recovery, throughput, cost, or publication completeness. The paper offers no downstream A/B or accepted-work outcome. Consequently the closing claim that schema-governed evaluation provides useful enterprise quality signals remains a plausible production experience claim, not a demonstrated utility result.

## Unique insight: retry validity is a selection problem over attempts

The paper's most reusable insight becomes sharper when the selective loop is treated as an estimand rather than a convenience function:

```text
eligible source record
  → attempt 1 raw output
      ├─ substantive valid observation → retain
      ├─ typed evaluator invalidity → eligible retry
      ├─ not applicable / insufficient evidence → abstain, do not launder
      └─ substantive unfavorable result → retain, never retry for outcome
  → attempt 2 ... attempt k under frozen treatment
  → final observation or residual invalidity
```

A final table with one valid row per source record erases the path that produced it. That path matters because invalidity can depend on prompt complexity, language, class, response length, model, or the judgment itself. Retrying until a parser accepts an answer changes the observation process; dropping residual failures changes the denominator. The benchmark must preserve both:

- **evaluation outcome:** what the valid judge observation says; and
- **evaluation-operation outcome:** whether, how, and at what cost a valid observation was obtained.

The loop is legitimate repair only when retry eligibility is fixed and outcome-blind, the evaluator treatment is immutable (or each change creates a new configuration), all attempts survive, residual invalids remain countable, and final-selection semantics are predeclared. Otherwise selective re-execution can create silent informative censoring.

A second insight is that **schema validity, judge validity, and decision validity form separate gates**. A JSON object can be structurally valid but evidentially unsupported; a judge can agree with one human label yet be unfit for a thresholded decision; and a good offline metric can still lack downstream utility. Operational governance must link these gates without allowing one to inherit the authority of another.

## Comparison with existing project evidence

- **Measuring Agents in Production** maps selected practitioner reports but cannot identify which practices work. This paper adds a concrete claimed evaluator pipeline and workload volume, but still releases no realized configuration, logs, or downstream outcomes. It is implementation description plus aggregate point claims, not independent practice efficacy.
- **Nubank offline/online evaluation** at least connects selected offline judge scores to reported live tNPS/SSR, though adaptive selection and absent denominators block predictive claims. This paper stops earlier: it reports judge-label concordance and evaluator operation, with no promotion episode or user/workflow consequence.
- **Anthropic task health** treats instrument defects, transcript adjudication, repeated trials, role changes, and retirement as maintained evidence. Selective retry belongs beneath that lifecycle: it can repair an invalid grader attempt, but cannot certify the task, grader, or claim.
- **Signals trajectory triage** shows why selected streams need explicit eligibility and denominators. Here, schema-invalid rows form an enriched retry stream. Their final valid outputs cannot silently stand in for all attempts or support an invalidity prevalence estimate without the source population and attempt ledger.
- **Partial benchmark decisions** makes efficiency claim-indexed: less work is useful only relative to a declared decision. Selective re-evaluation likewise needs a declared target—recover schema-valid observations under an outcome firewall—not a generic “reliability” or cost claim. Neither selective tasks nor selective attempts validates the completed record.
- **Existing benchmark-bundle, task-health, metric-monitoring, validity-argument, grader evidence-view, and longitudinal/configuration contracts** already provide the right homes. The distinct need is to exercise attempt-level retry and residual-invalid semantics in a fixture, not add a retail-evaluation subsystem.

## Limitations and validity threats

1. No code, data, configuration, prompt, schema, annotation instrument, outputs, logs, or analysis release was found.
2. The immutable PDF remains unavailable; the complete HTML is readable, but Figure 1 is literally a placeholder instructing the author to add `genai_architecture.png`.
3. Stable row-ID construction, source snapshot identity, normalization lineage, collision handling, and deduplication are unspecified.
4. BigQuery query ordering is not frozen, so round-robin sharding is not shown to be deterministic across reruns.
5. Pre-evaluation exclusions have no count, rate, subgroup profile, or retained denominator.
6. Four equal-row shards are not workload-balanced by token length or evaluator complexity.
7. Exact evaluator checkpoints, revisions, serving stack, quantizer, seeds, context settings, and prompt bytes are absent.
8. Rubric anchors, applicability, authority, evidence access, weights, normalization, and aggregation used in results are absent.
9. Human labels, references, and heuristics are pooled as target mechanisms without record-level authority lineage.
10. Retry eligibility conflates transport/parser/schema failures with missing scores and out-of-range model outputs.
11. No outcome firewall prohibits retrying schema-valid unfavorable observations.
12. No append-only raw-attempt ledger or final-attempt selection rule is specified.
13. Residual failures after three retries have no published keep/drop/block policy.
14. No initial-invalid rate, retry-success curve, residual-invalid rate, duplicated-row audit, or subgroup invalidity is reported.
15. Idempotency is asserted despite stochastic regeneration, changing timestamps, and append-style publication.
16. No exactly-once/upsert key or replay evidence supports “without duplication.”
17. The 12,980-row human sample lacks dates, frame, stratum counts, inclusion probabilities, and production weights.
18. Each item has one label, preventing human reliability estimation and confounding annotator with assigned subset.
19. Annotator qualifications, calibration, evidence view, interface, time, burden, and adjudication are absent.
20. Macro F1 aggregation across four classification families and 317 total labels is under-specified.
21. No class-wise results, confusion matrices, intervals, clustered uncertainty, or rare-class error analysis is reported.
22. Translation acceptability has no sample denominator, label rule, language mix, or mapping from judge output to binary accuracy.
23. Numeric quality scores are collected but receive no human agreement, calibration, or validity analysis.
24. Model labels are aliases rather than reproducible component identities.
25. Table 2 reports no throughput or cost despite the quality–throughput conclusion.
26. Daily and total volumes omit time window, GPU count, elapsed processing time, backlog, completion rate, and resource utilization.
27. “No API cost” omits hosting, H100, storage, Kubeflow, BigQuery, annotation, and engineering costs.
28. Temperature 0.005 does not establish repeated-call stability, and no repeat experiment is reported.
29. No temporal holdout, drift study, model-version bridge, or calibration curve supports ongoing production validity.
30. No tool trace, conversation-level dependency, multi-turn outcome, safety incident, privacy audit, or downstream customer/associate outcome is evaluated.
31. Retail text turns from one organization do not transport to artifact-heavy knowledge work, other risk regimes, or professional readiness.

## Reproducibility and operational realism

**Operational realism is moderate to high at the architecture-description level.** Production logs, malformed evaluator outputs, high-volume asynchronous serving, checkpoints, sharding, schema drift, retries, cloud publication, privacy, and model-hosting cost are real operating concerns. The reported two-million-record experience gives the problem more credibility than a toy pipeline proposal.

**Empirical reproducibility is low.** The complete immutable source exposes the narrative, formulas, two aggregate tables, and explicit single-label limitation, but none of the empirical records or executable configurations. Figure 1 is an unfilled placeholder. Table 2 cannot be recomputed; selective retry cannot be replayed; idempotency, exact-once publication, and throughput cannot be tested; and no official release was located. The reported volumes and accuracies are author claims with no independent artifact-level audit.

**Claim realism is mixed.** The paper commendably calls automated scores diagnostic signals and acknowledges model drift and absent inter-annotator agreement. It nevertheless uses “production-grade,” “deterministic,” “idempotent,” “quality-throughput trade-off,” “reliability,” and “useful quality signals” more strongly than the disclosed evidence warrants.

## Transfer to skill-bench

### Retain

- Configuration-driven evaluator schemas and prompt/version provenance.
- Stable source-record identity distinct from shard/worker identity.
- Incremental writes and bounded recovery rather than full-suite reruns.
- Typed validation before population aggregation.
- Separate general and task-specific criterion sets.
- Human audit as a distinct evidence layer rather than a synonym for model scoring.

### Repair

1. **Make evaluator attempts first-class.** Preserve source-record ID/hash, attempt ordinal, parent attempt, raw request/response locators, exact evaluator/parser/schema/config hashes, start/end time, tokens/cost, worker/environment, invalid reason, eligibility decision, and retained-final status.
2. **Enforce an outcome firewall.** Retry only predeclared evaluator-invalid states. Schema-valid pass/fail, low score, abstention, not-applicable, or insufficient-evidence outcomes must not be regenerated to improve completion or scores.
3. **Keep residual invalidity in every denominator.** Report attempted source records, prefilter exclusions, first-attempt valid, recovered by attempt number, residual invalid, missing, delayed, duplicate, and published records by task/model/slice.
4. **Version treatment changes.** Any prompt, schema, parser, model endpoint, decoding, evidence view, or reference change starts a new evaluator configuration; it is not another retry of the same treatment.
5. **Test logical and byte-level idempotency separately.** Logical idempotency means one declared final state per idempotency key under fixed selection rules. Byte identity is not expected when timestamps or stochastic outputs differ. Verify duplicate-safe publication with fault injection.
6. **Separate validation ladders.** Record schema conformance, repeated-call stability, human concordance, criterion/evidence validity, population metric validity, and decision/downstream validity as separate claims.
7. **Measure the operating frontier.** For each evaluator configuration, report eligible records/hour, end-to-end latency distribution, GPU-hours, tokens, storage, invalid/retry rates, residual missingness, human-review hours, and judge-error slices—not parameter count plus accuracy alone.
8. **Use plural human labels where claims require reliability.** Overlap a probability sample, preserve individual labels and evidence views, adjudicate separately, and report uncertainty by conversation/system/language/class clusters.

## Concrete repository actions

1. **Add no new queue task.** Existing trial/configuration, grader-observation, task-health, metric-monitoring, validity, and information-flow machinery can represent the requirements. A production-retail or generic retry schema would duplicate those systems.
2. **Refine the next relevant retry/recovery fixture, not the architecture.** Plant at least: transport failure then valid recovery; malformed JSON then valid recovery; schema-valid unfavorable judgment that must not retry; explicit abstention/insufficient evidence; three-attempt residual invalidity; configuration change that must fork identity; and duplicate publish replay. Assert exact attempted/final denominators and append-only lineage.
3. **Keep the evidence ceiling explicit.** A passing fixture would validate local retry semantics only. It would not validate judge accuracy, throughput economics, production utility, professional quality, capability, safety, or readiness.
4. **Index this review under reliability/traces/recovery.** Canonical synthesis need not change yet: the evidence sharpens existing invalid-attempt, outcome-selection, and denominator boundaries without overturning a grouped conclusion or adding a new relevance tier.

## Action items

- [x] Read the complete immutable v1 HTML/text through all sections, tables, limitations, and references.
- [x] Verify immutable metadata contains no withdrawal/retraction notice.
- [x] Retry the versioned PDF endpoint and preserve the no-substitution boundary after HTTP 404.
- [x] Verify the release audit and record that no official empirical/configuration artifact was found.
- [x] Reconstruct source-record identity, normalization/sharding, evaluator configuration, schemas/dimensions, retry eligibility, human validation, metrics, and claimed operation.
- [x] Separate schema validity, substantive outcome, human concordance, population measurement, operational reliability, downstream utility, and readiness.
- [x] Compare with MAP, Nubank, Anthropic task health, Signals, partial benchmark decisions, and existing contracts.
- [x] Add no duplicate build/consolidation task.

## Bottom line

Selective re-evaluation is valuable because evaluator infrastructure fails at record level, not because a successful retry makes the judgment true. The paper identifies the right operational pain and a plausible high-volume architecture, but its final table hides the attempt-selection process needed to evaluate that architecture. `skill-bench` should preserve every attempt, retry only typed outcome-blind invalidity under a frozen treatment, retain residual failures in denominators, and validate publication under fault injection. Only after those gates should human concordance, metric validity, downstream utility, and reliability be argued—and none is established by this v1 source.
