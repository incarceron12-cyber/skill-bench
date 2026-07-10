# Paper Review: AgentRewardBench — Expert-Calibrated Trajectory Judge Reliability

- **Paper:** https://arxiv.org/abs/2504.08942v2
- **Authors:** Xing Han Lù et al.
- **Date read:** 2026-07-10
- **Venue / source:** arXiv preprint
- **Version read:** immutable v2, 6 October 2025
- **Local PDF:** `data/papers/pdfs/2504.08942v2-agentrewardbench-evaluating-automatic-evaluations.pdf` (23 pages; SHA-256 `a5c5aeb2f76a69372a70155d765172dc8af2376ec63a4874460c05b28609c921`)
- **Local text:** `data/papers/text/2504.08942v2-agentrewardbench-evaluating-automatic-evaluations.txt` (SHA-256 `232718a3ca99c33d4b1a0ad127edc53450e7a4de2ae28397acd1b4d96ca16cfd`)
- **Official code inspected:** https://github.com/McGill-NLP/agent-reward-bench/tree/f838338886d723d40b586309465a38277803d9e6 (commit `f838338886d723d40b586309465a38277803d9e6`; tree `b425523d981884e25481ba90480739b15175f2f4`; post-submission but pre-v2)
- **Official dataset revision inspected:** https://huggingface.co/datasets/McGill-NLP/agent-reward-bench/tree/b6d17e646009d6cb63d5dd7be78807b680693f61
- **Release provenance:** `data/sources/releases/2504.08942v2-agentrewardbench/provenance.json`
- **Tags:** llm-judge, human-annotation, trajectory-evaluation, side-effects, observability, class-imbalance, grader-validity

## One-sentence contribution

AgentRewardBench makes automatic trajectory grading itself an evaluation target using 1,302 web-agent trajectories, three expert labels, official rule-based rewards, and twelve LLM-judge configurations, showing that rule graders have high precision but low recall while no tested LLM judge exceeds 70% pooled success precision; however, unequal evidence access, narrow and partly row-order-defined human ground truth, severe label imbalance, absent uncertainty, and release/scoring defects prevent its agreement scores from establishing a generally reliable judge.

## Why this matters for skill-bench

This paper directly advances charter objectives A and C: it evaluates the measurement layer rather than treating a grader as an oracle. Its most useful result is not that LLM judges are more “flexible” than deterministic checks. It is that **grader validity is conditional on a predicate, evidence view, error cost, task population, and decision use**. The official rule graders and LLM judges occupy different operating points: the rule baseline reports 83.8% success precision and 55.9% recall, while the best pooled LLM result reports 69.8% precision and 83.1% recall (Table 1, p. 6). Whether either is preferable depends on whether false acceptance, false rejection, human audit, training-data contamination, or benchmark ranking is the consequential error.

The study is also unusually valuable for exposing observability as a treatment. Human annotators see every screenshot, action, and reasoning step and may inspect the live environment and accessibility trees when needed (Section 3.1, p. 4; Appendix A.2, pp. 14–15). The simplified LLM judge instead receives all actions and agent reasoning but only the final screenshot and/or final accessibility tree (Appendix Figure 5–6, p. 23). The comparison therefore estimates agreement under different evidence channels, not a pure human-versus-model judgment capability contrast.

For `skill-bench`, this supports a strict rule: a grader result must identify both the predicate it claims to observe and the evidence state it actually received. `success`, `side_effect`, and `repetition` are not merely three output fields. They require different temporal and environmental evidence, have different prevalences, and exhibit radically different error profiles.

## Research question and claim boundary

The paper asks:

1. How accurately do rule-based and LLM-based evaluators predict expert labels for web-agent trajectory success?
2. Can a simplified judge using actions, reasoning, and a final browser representation match or outperform more elaborate judge pipelines?
3. How do automatic evaluators change estimated agent success rates?
4. Can judges detect auxiliary failures—unintended side effects and repetitive action cycles?

The evidence supports bounded claims about the released task-agent sample: official rule checks miss many trajectories that the annotation procedure accepts; the tested LLM judges trade higher recall for materially lower precision; no one judge dominates every benchmark; and final-state representation affects success, side-effect, and repetition errors differently (Tables 1–3 and 7–8, pp. 6–8, 17–18).

It does **not** establish that a single human label is objective success, that rule-based false negatives are always verifier defects rather than specification disagreements, that the simplified judge is cost-effective in measured operation, that its results transfer beyond these web environments or model-generated traces, that side effects are adequately observed, or that pooled precision licenses autonomous grading, reward modeling, professional-capability claims, or deployment decisions.

## Methodology

### Task and trajectory sampling

The authors select 351 task specifications across five benchmark families: all 33 AssistantBench validation tasks; 100 VisualWebArena tasks; 100 WebArena tasks; 18 basic WorkArena tasks; and 100 WorkArena++ Level-2 tasks (Section 3.2, p. 5; Appendix A.1–A.2, pp. 14–15). WebArena and VisualWebArena are stratified by domain and original evaluation method, with random sampling of up to eight or nine tasks per subgroup. WorkArena categories are described as approximately balanced. AssistantBench uses live websites and substitutes DuckDuckGo because the original search page blocked automation.

Four agent backbones produce one trajectory per assigned task: GPT-4o (`gpt-4o-2024-11-20`), Claude 3.7 Sonnet, Qwen2.5-VL-72B-Instruct, and Llama-3.3-70B-Instruct. Llama is omitted from the 100 visual tasks and fails to complete two WebArena tasks after repeated environment timeouts. This yields 1,302 unique benchmark–task–agent trajectories: 196 development and 1,106 test (Section 3.3, pp. 5–6; Appendix A.2, p. 14). AgentLab/BrowserGym standardizes the agent representation and flags, with 40K input and 8,192 output-token limits.

This is purposive, stratified coverage rather than a probability sample of web work or knowledge work. Trajectories are clustered by 351 normalized task specifications and generated once per agent configuration; there are no independent reruns with different seeds. Treating 1,302 rows as independent overstates effective sample size for model, task, and benchmark comparisons.

### Expert annotation and adjudication

Six researchers with web-agent and environment knowledge use a custom interface to inspect the goal, every screenshot with action overlay, actions, and agent reasoning. When screenshots are insufficient, they may inspect the environment and accessibility trees. They answer four questions in the released instrument: binary success, binary side effect, four-level optimality, and binary repetition. The paper foregrounds three labels and calls success primary (Section 3.1, pp. 3–4; Appendix A.2, pp. 14–15).

Annotators can mark uncertainty. The first half of annotation occurs with annotators co-located so uncertain cases can be discussed; ambiguous instructions are resolved using the “most lenient” interpretation, and the resulting consensus is intended to align later annotations. This is a pragmatic adjudication workflow, but it is not independent labeling. It can improve consistency while suppressing legitimate disagreement about the construct boundary.

Only GPT-4o's 100 WebArena trajectories are systematically double-annotated according to the paper. It reports 89.3% success agreement (p. 6), but gives no chance-corrected statistic, confidence interval, label-specific agreement, rater assignment, or agreement for side effects and repetition. No held-out expert adjudication study tests whether a reviewer can recover consequential environment state from the preserved trace.

### Released annotation table and the meaning of “ground truth”

Inspection of the pinned `annotations.csv` resolves its apparent 1,408-versus-1,302 discrepancy. It contains exactly 1,302 unique `(benchmark, task, model, experiment)` trajectories plus 106 second annotation rows: 100 GPT-4o/WebArena pairs and six additional pairs. Group sizes are 1,196 singletons and 106 pairs. Thus 1,408 is an annotation-row count, not a conflicting trajectory count.

The release nevertheless reveals a more important validity issue. The scoring code's `infer_annotator_type` designates the **first CSV occurrence** of a benchmark–model–task key as `primary` and every later occurrence as `secondary`; headline metrics use only `primary`. There is no explicit adjudicated-consensus field, annotation timestamp, confidence, rationale, or final-label provenance in the released table. The preserved paired GPT-4o/WebArena rows agree on success for 89/100 pairs, including one `Unsure`/`Successful` pair; the code excludes the unsure pair in category-specific agreement and would therefore compute 89/99, not the paper's reported 89.3%. The pinned release may differ from paper-time labels, but neither the paper nor release provides the lineage needed to reconcile the difference.

The 1,302 row-order-primary labels contain 355 successes (27.3%), 84 side effects (6.5%), and 676 repetition positives (51.9%), plus one unsure success/side-effect/optimality row. Paired-row raw agreement is 89/100 for success, 96/100 for side effects, 60/100 for exact four-level optimality, and 90/100 for repetition in the intended GPT-4o/WebArena subset. These release observations are diagnostic, not substitutes for the paper's unreported adjudication protocol.

### Rule-based and LLM judges

The official rule baseline converts each environment's cumulative reward to success at a threshold above 0.5. This pools heterogeneous task-specific mechanisms including string matching, HTML programs, image queries, URLs, and environment-state checks. It is not one uniform rule grader.

The study evaluates three representation strategies:

- **AER-C/AER-V:** actions, thoughts, and final state, with GPT-4o captioning or vision;
- **NNetNav:** Llama-3.3-70B rates a summary of accessibility-tree changes on a five-point scale, thresholded at four;
- **Simplified judge:** one completion predicts success, side effect, optimality, and repetition from all action/reasoning text plus the final screenshot and/or final accessibility tree.

Twelve LLM-judge configurations are reported, including screenshot/accessibility variants and several backbones (Section 4.1 and Table 1, pp. 6–7). Release defaults specify temperature 0, seed 0, and 1,024 completion tokens, but there are no repeated judge calls to measure residual nondeterminism or endpoint drift. Model identifiers are partly pinned, while hosted-provider realization and retrieval dates are not fully frozen.

The prompt explicitly includes agent reasoning. This makes sycophantic acceptance of a false self-report a designed risk, not merely an incidental error; Section 6 documents grounding mismatch, misleading reasoning, missed instruction details, and misunderstood action intent (pp. 8–9). The judge does not receive intermediate screenshots or accessibility trees, even though side effects and loops are temporal predicates and humans can inspect richer state.

### Metrics, uncertainty, and decision use

Precision for the positive success class is primary because the stated use is rejection fine-tuning or reward modeling, where false-positive accepted trajectories contaminate training. Recall and F1 are secondary (Section 4.2, p. 7). This is one of the paper's strongest methodological choices: it ties metric direction to an error cost.

However, the implementation and reporting stop short of a complete metric specification. Results are pooled at trajectory level without task-cluster adjustment, confidence intervals, bootstraps, hypothesis tests, calibration curves, repeated judge samples, or explicit missing/invalid-response policy in the paper. Benchmark-specific precision varies dramatically—for the same GPT-4o accessibility judge, from 63.0% on VisualWebArena and WorkArena++ to 94.6% on WorkArena (Table 8, p. 18). A pooled 69.8% is not a stable judge property.

Class imbalance is especially consequential. Side effects occur in only 6.5% of released primary rows; reported side-effect precision for simplified judges is just 6.6–14.1% despite recalls as high as 91.7% (Table 7, p. 17). The high repetition F1 values coexist with a released primary prevalence of 51.9%, so they are not comparable evidence of rare-harm detection. The paper does not report prevalence, specificity, negative predictive value, expected loss, or severe-side-effect recall in its main interpretation.

## Evidence and results interpretation

The official rule baseline has the highest pooled success precision, 83.8%, but only 55.9% recall and 67.1% F1. GPT-4o with final accessibility tree has the best reported pooled LLM success precision, 69.8%, with 83.1% recall and 75.9% F1. Thus the paper's “rule-based evaluation underestimates success” conclusion is supported as a descriptive average relative to the selected primary labels, while the recommendation for more flexible grading is incomplete: flexibility shifts error from false rejection toward false acceptance.

The success-rate comparison makes this concrete. Rule rewards usually estimate lower agent success than primary human labels; GPT-4o judging usually estimates higher success. Rankings can reverse—for example, human labels rank GPT-4o above Qwen2.5-VL across the shown benchmark families, while official rewards do not always do so (Table 3, p. 8; Table 6, p. 17). This is strong evidence that evaluator choice is part of the benchmark instrument, not a neutral post-processing step.

The representation ablation is informative but not causal enough for broad prescription. For GPT-4o-mini, screenshot-only success precision exceeds accessibility-only precision (64.5% versus 61.5%), while accessibility-only has higher recall (86.1% versus 78.3%). Removing both final representations worsens success F1 but improves reported repetition F1 relative to screenshots (Table 2, p. 7). Because the study does not repeat calls, hold prompt length constant, report truncation rates, or inspect representation-specific errors systematically, “more information distracts” is a plausible explanation rather than an identified mechanism.

The paper correctly concludes that no tested LLM judge is reliable enough for autonomous acceptance of successful training trajectories: at best, 30.2% of predicted successes are false positives under its primary labels. It overreaches when it describes rule-based evaluation as not reflecting how experts define success without preserving a criterion-level adjudication record. The Acadia exact-match example is persuasive evidence of one brittle check, not proof that every human–rule disagreement is a grader defect. Some disagreements can reflect task ambiguity, hidden environment state, lenient interpretation, or inconsistent human standards.

No measured cost or latency results are reported despite repeated claims that LLM judging is faster or cost-effective. The release contains a cost estimator, but the paper gives no total tokens, dollars, wall time, human hours, audit burden, or cost-quality frontier.

## Unique insight

The deepest insight is that **grader disagreement is a three-way identification problem, not a race to match “human ground truth”**:

`task requirement ↔ observable environment consequence ↔ evaluator evidence view`

A disagreement can originate in the task specification, the environment/check, trace capture, evidence access, interpretation policy, or evaluator. AgentRewardBench exposes several of these simultaneously but collapses them into binary agreement with a row-order-primary human label. Its qualitative examples then recover the missing causal structure: exact-match brittleness is a check-specification problem; believing false agent reasoning is an evidence-weighting problem; missing a purchase action is a requirement-decomposition problem; and unseen intermediate side effects are an observability problem.

This implies a stronger `skill-bench` grader record. A human, deterministic check, and model judge should each emit a **typed observation**, not overwrite one another as truth. Adjudication should compare their required evidence, actual evidence, predicate, and uncertainty, then produce a versioned resolution such as `agent_failure`, `grader_false_accept`, `grader_false_reject`, `trace_insufficient`, `task_ambiguous`, or `environment_state_unavailable`. Instrument defects must create a new task/grader version; old scores remain historical evidence.

A second insight is that one headline reliability number is structurally misleading. Success, side effects, and repetition differ in temporal scope, prevalence, and loss. Even success precision changes by more than thirty points across benchmark slices. A grader is therefore not “69.8% precise” in a portable sense. It has an error surface indexed by predicate × task family × agent/harness × evidence view × threshold × time.

## Transferable design patterns

### 1. Treat evidence access as part of grader identity

Record required and observed channels separately: final artifact, intermediate states, screenshots, structured state, tool results, environment query access, agent reasoning, user-visible response, and hidden/private state. If a side-effect check requires state that was not captured, return `insufficient_evidence`; do not infer “no side effect.”

### 2. Preserve plural observations before adjudication

Store deterministic-check output, model-judge output, each independent human label, uncertainty, evidence locators, and rationale as separate immutable records. Add a distinct adjudicated label with adjudicator IDs, policy, changed fields, and disagreement category. Never use CSV row order as the authority rule.

### 3. Match metrics to decisions and error costs

For training-data acceptance, precision and severe false-accept cost may dominate. For capability measurement, false-negative bias and rank stability matter. For safety, rare-harm recall, specificity, audit rate, and expected loss matter. A single F1 or pooled precision should not serve all uses.

### 4. Estimate clustered and sliced uncertainty

Bootstrap or model at the task level, because several agents execute the same task. Report confusion matrices and intervals by task family, predicate, agent/harness, trace length, evidence channel, and severity. Require repeated judge calls or a justified determinism check before treating one temperature-zero response as stable.

### 5. Use complementary graders, not forced replacement

Deterministic checks are valuable high-precision witnesses for environment facts; model judges can recognize legitimate variants and semantic completion; humans can adjudicate ambiguity and professional acceptability. Route disagreements and low-confidence/insufficient-evidence cases to review. Calibrate ensemble or cascade policies against explicit loss and human burden rather than assuming the flexible grader should replace the rule grader.

### 6. Separate root cause from surface mismatch

Adopt disagreement labels such as `task_spec_ambiguity`, `check_brittleness`, `state_not_captured`, `judge_grounding_error`, `agent_self_report_bias`, `instruction_detail_omission`, `action_semantics_error`, and `human_policy_disagreement`. Preserve the raw mismatch separately from the earliest supported cause.

### 7. Version label-policy and instrument changes

A lenient ambiguity policy, success threshold, final-state representation, prompt order, or added environment access changes the instrument. Hash each version, preserve old results, and require bridge items before comparing scores across versions.

## Limitations and validity threats

1. **Purposive task coverage is not ecological sampling.** Five web benchmark families and 351 tasks provide diversity, not prevalence-weighted knowledge-work coverage.
2. **Single trajectories prevent reliability estimation.** Each task-agent configuration is represented once; service, seed, and environment variance are unmeasured.
3. **Task clustering is ignored.** Up to four agents share each task, but metrics and claims treat trajectory rows as independent and report no clustered uncertainty.
4. **Human evidence access exceeds judge access.** Humans may inspect every screenshot, accessibility trees, and the environment; simplified judges receive action/reasoning text plus only final state.
5. **Agent reasoning is a confounded channel.** It can help interpret intent but also directly mislead the judge, as the paper's own examples show.
6. **“Expert” scope is narrow.** Annotators are web-agent/environment researchers; the paper does not demonstrate domain-professional authority for shopping, enterprise, or real-world task consequences.
7. **Most labels are single-rater.** Only one 100-trajectory subset is systematically double-annotated; side-effect and repetition reliability are not reported in the paper.
8. **Consensus is not independently measured.** Co-located discussion and alignment can produce consistent labels without establishing construct validity.
9. **Adjudication provenance is absent.** The release has no final-consensus field or rationale; scoring selects the first CSV row as primary.
10. **Paper/release agreement is unreconciled.** The paper reports 89.3% success agreement; pinned paired rows and released code imply different raw/exclusion calculations.
11. **The success construct is lenient by policy.** Ambiguous instructions use the most lenient reading, which can systematically make exact rule checks appear overly strict.
12. **Rule graders are heterogeneous.** Pooling string, URL, HTML, image, and environment-state checks hides which mechanisms are brittle or authoritative.
13. **Class imbalance is under-analyzed.** Side effects are rare, and very low precision is obscured by emphasizing recall/F1 without prevalence or loss.
14. **Severity is absent.** A harmless extra click and consequential unintended action share one side-effect label.
15. **Repetition is unusually prevalent.** More than half of released primary trajectories are positive, but duration, cycle length, progress threshold, and operational consequence are not typed.
16. **No inferential uncertainty.** Tables omit confidence intervals, repeated runs, significance tests, calibration, and rank-stability analyses.
17. **Input ablations can change length and truncation.** The study does not establish whether representation effects come from modality, token competition, pruning, or model capability.
18. **Cost-effectiveness is asserted, not measured.** No judge-cost, human-cost, latency, or audit-load results are reported.
19. **Live-site and hosted-model drift weaken reproduction.** AssistantBench uses mutable websites, and provider realizations are not fully archived.
20. **The released corpus was only partially mirrored locally.** Complete tables, code, and immutable tree/LFS manifests were inspected, but the multi-gigabyte trajectory/judgment/screenshot corpus was not downloaded in full; release-level observations about individual traces remain bounded accordingly.
21. **Missing-output semantics are unsafe in code.** Invalid judge responses are represented as `n/a` and can remain in metric denominators; missing parsed tags become numeric zero rather than an explicit invalid observation.
22. **Fallback treatment is not explicit in outputs.** On a bad request, the runner retries with a pruned accessibility tree, but the result does not state which representation actually reached the model.
23. **The released cost estimator is defective.** Its total adds raw cached-token count instead of computed cached-token price, so saved total-price fields are not trustworthy.
24. **No instrument tests or environment lock are released.** The archive has broad minimum dependencies, no lockfile, and no unit tests validating parsing, annotation authority, or metric behavior.

## Reproducibility and operational realism

Reproducibility is moderate for inspecting the instrument and weak-to-moderate for repeating the experiment. The immutable paper, complete 69-file official code archive, annotations, task splits, task IDs, reported result table, prompts, model arguments, and trajectory tree manifests are preserved. The public dataset exposes cleaned trajectories, screenshots, and judge outputs at a pinned revision, so a fully provisioned researcher could retrieve the large corpus and rescore it.

Exact regeneration is substantially harder. It requires multiple self-hosted browser environments, ServiceNow and other credentials, mutable real websites, commercial endpoints, and old model behavior. The repository does not provide an environment lockfile, container, exact service snapshots, test suite, complete run manifest, human annotation UI code, adjudication records, or paper-time result notebook. The GitHub commit predates v2 but postdates the original submission, so it verifies a released implementation rather than immutable paper-time code.

The runner does preserve useful per-judgment operational data: judge/model/provider names, completion arguments, API response, usage, prompt messages, trajectory configuration, and an estimated cost. But it also saves both regular and pruned prompts without recording which fallback was used; silently skips already-existing outputs; handles only a narrow bad-request class; and lacks prompt hashes, dataset revision, environment snapshot, retry count, and calibrated invalid-state handling. The scoring script infers annotation authority from row order and includes missing/invalid outcomes in ways that can conflate evaluator failure with negative prediction.

Operational realism is strongest for trajectory review in resettable browser environments. The paper includes multi-step actions, environment consequences, misleading self-reports, repetition, and side effects—important ingredients missing from artifact-only benchmarks. It remains narrow relative to `skill-bench`: three coarse labels do not assess professional artifact conventions, source provenance, decision thresholds, repair, stakeholder acceptance, or consequential domain safety. It is best treated as a grader-calibration case study, not evidence that browser completion is a sufficient model of knowledge work.

## Concrete changes for skill-bench

1. **Refine existing grader observations rather than create a parallel subsystem.** Require `predicate_id`, required/actual evidence channels, evidence locators, raw output, parsed output, invalid/insufficient states, confidence, prompt/model hashes, retries/fallbacks, and licensed claim.
2. **Use this evidence in `build-validity-argument-contract`.** A model-human agreement score supports a narrow concordance claim for a specified population and evidence view, not “reliable evaluator,” professional capability, or deployment readiness.
3. **Use this evidence in `build-task-health-lifecycle-contract`.** Add disagreement adjudications that distinguish task ambiguity, grader defect, trace insufficiency, and agent failure; any repaired check creates a new instrument version without rewriting old scores.
4. **Use this evidence in `build-metric-monitoring-contract`.** Specify eligible population, unit, task clustering, prevalence, missing/invalid labels, confusion matrix, uncertainty, slices, threshold, error cost, audit route, and grader/service drift.
5. **Add evidence-view parity tests to pilot grader calibration.** Compare artifact-only, trace, and environment-query conditions using planted cases where the final artifact is insufficient to detect an intermediate side effect or failed recovery.
6. **Preserve independent labels and explicit adjudication.** The LH pilot should never select a “primary” expert by file order; contributor authority, independent judgment, disagreement, uncertainty, and final resolution must be versioned.
7. **Use cascades for asymmetric errors.** Keep deterministic checks for authoritative state predicates, model judges for semantic variants, and human review for disputed/ambiguous/high-loss cases. Measure the quality–cost–audit frontier.
8. **Fail closed on grader execution defects.** Parse failure, unavailable source/environment state, fallback representation, or provider failure must produce invalid evidence, never a silent negative label.

## Action items for repository

- [x] Read the complete immutable arXiv v2 PDF/text with page and section evidence.
- [x] Inspect the complete official 69-file code release at pinned commit `f838338886d723d40b586309465a38277803d9e6`.
- [x] Inspect the pinned annotation, split, task-ID, reported-results, and trajectory-tree evidence and preserve release limits.
- [x] Reconcile 1,408 annotation rows with 1,302 unique trajectories and audit paired-label agreement and primary-label prevalence.
- [x] Inspect judge prompts, input construction, model settings, fallback behavior, parsing, scoring, agreement, and cost code.
- [x] Separate paper claims, released-artifact observations, and `skill-bench` adaptations.
- [x] Add no queue task: the evidence sharpens the existing validity, task-health, metric-monitoring, grader-record, and trace-observability work without exposing a nonduplicate subsystem.
