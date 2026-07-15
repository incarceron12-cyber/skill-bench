# Paper Review: The Saturation Trap — Intervention-Timing Construct Reliability

- **Paper:** https://arxiv.org/abs/2606.04296v1
- **Author:** Manvendra Modgil
- **Date read:** 2026-07-15
- **Version read:** immutable arXiv v1, submitted 2 June 2026
- **Local PDF:** `data/papers/pdfs/2606.04296v1-intervention-timing-saturation-trap.pdf` (11 pages; SHA-256 `b478eb1b669b392f759a91b2943b20bc1931efefc12ca53b37c5acf4a17d0a37`)
- **Local text:** `data/papers/text/2606.04296v1-intervention-timing-saturation-trap.txt` (SHA-256 `ddccb91c0523b340c53485bd8c579eb1807c54b010f621a27513a4d1a8c3e2d6`)
- **Official repository inspected:** https://github.com/2025eb1100268-tech/intervention-timing-saturation-trap/tree/55c8bd26f5303807c7f134df24275b9de9fca187
- **Release provenance:** `data/sources/releases/2606.04296v1-intervention-timing/provenance.json`
- **Important version boundary:** the requested repository commit is dated 15 June, thirteen days after v1. Its audit says the v1 replay passed `Δt=0`, disabling decay. The repository is therefore post-v1 correction evidence, not proof of the paper-time implementation.
- **Tags:** intervention-timing, supervision-policy, inter-rater-reliability, saturation, llm-judge, decision-validity, temporal-evidence-view

## One-sentence contribution

The paper is a valuable negative measurement case: three annotators place sparse pause/reflect/clarify labels very differently on one 56-action coding trace, state-level alarms fire persistently, and LLM judges are unstable and expensive; however, the release reveals that the headline saturation mechanism was produced with decay disabled, while the human target, observer evidence time, action-index semantics, annotator authority, and intervention utility are too under-specified to establish that intervention timing itself is generally unreliable.

## Why this matters for skill-bench

A realistic knowledge-work benchmark may score whether an agent should ask, defer, escalate, verify, pause, or hand control to a person. Those are not ordinary artifact labels. They are **policy decisions indexed by an information time, available action set, authority, capacity, and loss function**. Agreement on an exact action index is neither necessary nor sufficient for a good intervention policy: two reviewers can choose nearby safe moments with equivalent consequences, while three reviewers can agree on a moment that is costly or ineffective.

This review advances charter objectives A, B, C, and E by exposing a missing validity boundary between trajectory observation and supervision action. The transferable object is not an affect model or a coding-only pause taxonomy. It is:

`decision time → admissible evidence prefix → risk/opportunity state → available intervention → authority and burden → response/uptake → counterfactual consequence → policy value`

That chain applies to research review, compliance escalation, source clarification, artifact verification, and other knowledge-work domains without narrowing the benchmark to coding or affective monitoring.

## Research question and claim boundary

The paper asks which of four detector families best aligns with human judgments about when to interrupt an autonomous coding agent: absolute affect-state thresholds (A6), composite state/action patterns (A8), regex reasoning features (A9), or zero-shot LLM judges (A10) (Sections 1, 3–4, pp. 1–4).

The full paper and post-v1 release support the following bounded findings:

1. three released annotators produce materially different sparse binary label vectors on one 56-action `astropy__astropy-13398` trajectory;
2. the released scripts reproduce pairwise location κ of `0.349`, `0.092`, and `-0.181`, and three-rater nominal α of `0.047` for any intervention location, `0.226` for reflect, `-0.025` for pause, and `-0.106` for clarify;
3. under the paper's unreleased HEART implementation and released result records, A6 level triggers remain active over 39.3–83.1% of five selected trajectories;
4. one small judge configuration never fires, while two larger judge realizations fire more often but have low and run-sensitive overlap with one selected annotator;
5. the post-v1 implementation audit establishes that the replay path hard-coded `Δt=0`, so exponential decay never ran and all 43 zero-signal actions checked in one state trace left the 18-vector unchanged exactly;
6. the released labels and reliability scripts are independently recomputable, but the state replay, LLM sweep, and paper–trajectory correspondence are not fully reproducible from the public package.

The evidence does **not** establish that intervention timing is a unitary low-reliability construct across agents, trajectories, domains, expert populations, or consequences; that any annotator is correct; that a detector would fail against a consequence-grounded or set-valued target; that pause/reflect/clarify are the right action set; that affect transitions are useless; or that any proposed intervention improves success, safety, cost, or human workload.

## Methodology and system reconstruction

### Trajectories and sampling

The labeled unit is one 56-action Claude trajectory from the `20250514_aime_coder` SWE-bench-Verified evaluation, selected because it ultimately succeeds but contains an extended mechanical struggle over a rotation-matrix bug (Section 4.1, p. 4). A second 59-action trace is used only for state saturation, and four additional traces were operational pilots; the final saturation table contains five traces of 28–59 actions (scope clarification and Table 1, pp. 2, 5).

This is purposeful mechanism sampling, not a trajectory population. All five tasks are Astropy coding traces, all labeled inference comes from one successful trace, and no selection ledger describes how these five were chosen from available runs. Task, repository, agent, scaffold, successful endpoint, trajectory length, and observed struggle are therefore inseparable. “Five independent trajectories” means five trace records, not independent draws from a declared task or agent population.

### HEART engine, observer, and guideline layers

The paper separates a proprietary 18-dimensional affect engine, an observer mapping thoughts/tool calls/observations into engine events, and guideline triggers over resulting state (Section 3, pp. 3–4). The engine allegedly decays emotion toward a baseline, applies momentum, energy normalization, conflict dampening, and Big-Five coupling. It is calibrated to psychological priors rather than agent behavior. The paper says engine constants and first-pass thresholds were not fitted to the labels.

This separation is conceptually useful: state construction and action policy should not be treated as one opaque score. But neither the patented engine nor its observer/adapter is released. The result depends on at least three unvalidated translations:

`agent event → observer signal → human-like latent affect → intervention rule`.

A fixed, untuned instrument can still be invalid. The paper offers no human-affect labels, observer agreement, event-mapping audit, construct validation for applying human-like frustration to an agent, or evidence that the 18-dimensional state is relevant to intervention consequences.

### The post-v1 `Δt=0` audit changes the saturation claim

The post-v1 `paper2/prereg/DT_AUDIT.md` traces the actual replay path: parser timestamps are synthetic ordinals and unused; `_apply_event` calls `_tick_decay(0.0)`; the wall-clock decay path is never invoked. Thus the v1 result is a pure accumulator with no inter-action recovery. The repository's top-level README explicitly says Paper 2 “corrects and extends Paper 1.”

This materially contradicts v1's mechanism language. V1 describes per-emotion exponential decay and argues that agents provide no recovery signal, so state remains saturated (Sections 3 and 5, pp. 3, 5–6). The audit shows that state could not decay between actions even if elapsed time should have permitted it. The five-trace result remains evidence that **this zero-decay implementation plus these event mappings and thresholds** becomes persistent. It is not evidence that an operational wall-clock-calibrated affect monitor structurally saturates because agents fail to recover.

The later release reports 65 measured inter-action gaps from five different instrumented mini-model debugging runs, with pooled median 1.53 seconds and tool-dependent heavy tails up to 15.87 seconds (`paper2/reports/TIMING_REPORT.md`). Those post-v1 runs use injected bugs and a fallback harness, not the paper's trajectories. They demonstrate that cadence is nonzero and tool-dependent, reinforcing that timing semantics are a configured-environment component rather than repairing v1.

### Human annotation target

Three annotators independently label each of 56 actions with three booleans:

- **pause:** halt and reconsider because the trajectory looks problematic;
- **reflect:** step back and consider alternatives when grinding without metacognition;
- **clarify:** articulate uncertainty before proceeding when confused or searching aimlessly.

The brief says intervention should be exceptional. One annotator initially marked clarify on 53/56 actions; that pass was discarded, the brief was clarified to emphasize sparsity, and the annotator relabeled (Section 4.2, p. 4). The retained positive counts are A: `4/5/2`, B: `1/4/2`, C: `0/2/13` for pause/reflect/clarify (Table 3, p. 7).

The complete-crossed assignment is a strength: all three rate the same actions, blind to each other, detector outputs, and engine state. But “trained annotators” is not operationalized. The paper and release omit identities, qualifications, recruitment, training duration/materials, calibration cases, compensation, order, interface, annotation time, rationales, uncertainty, repeat labels, and whether all raters saw exactly the same trajectory fields. The retained JSON contains only positive booleans, not evidence views or reasons. The discarded-and-rebriefed pass also means the final labels were not produced under one untouched verbatim protocol; the changed instruction is itself an unreported instrument version.

### Temporal evidence-view and action-index ambiguity

This is the most consequential construct defect. The rubric asks whether the agent should have been interrupted **before this action**. Yet the A10 prompt supplies the current action's thought, proposed tool/action, and its resulting **observation**, then asks whether intervention should occur before that action (`scripts/llm_calibration.py`, lines 108–129). An observation produced by executing the action is unavailable before execution. The macro condition also supplies the full prior trajectory, while the current observation remains hindsight evidence.

The paper says each annotated action includes thought, tool call, and environment observation, but does not specify the human annotation interface or whether humans similarly saw the current observation (Sections 4.1–4.2, p. 4). The state observer also parses action and observation before producing state, but the exact trigger-to-boundary alignment is unreleased. Consequently, at least three targets may be conflated:

1. **pre-action gate:** intervene before action `t`, using only state through `t-1` plus a proposed action if available;
2. **post-action checkpoint:** intervene after observing action `t` and before `t+1`;
3. **retrospective blame:** after seeing later trajectory evidence, identify an earlier point where intervention would have been useful.

These targets have different admissible evidence and different indices. Exact-index disagreement can be manufactured by a one-step convention shift even when reviewers identify the same episode. A valid benchmark must freeze the boundary and forbid future/current-observation leakage.

### Trigger families

A6 applies absolute state thresholds: frustration `≥0.7`, a five-emotion sum `≥1.5`, and confusion `≥0.6` without a reflection flag. A8 combines rolling affect changes with repeated tool/error patterns. A9 uses regex dictionaries for hedging, assertion, cycling, recognition, and tone changes. A10 applies each intervention rubric in a separate model call with either three prior thoughts or the running history (Section 4.3, pp. 4–5).

These are not treatment-equivalent competitors. They receive different evidence: latent observer state, structured tool/error history, thought text, or truncated thought/action/observation context. Their outputs also differ semantically: a level alarm, repeated-pattern event, linguistic feature, and normative decision. Comparing F1 does not isolate architecture quality from evidence sufficiency, target mapping, or output topology.

Pause, reflect, and clarify are also neither mutually exclusive nor ordinal. Annotator A assigns pause and reflect together at actions 9, 33, and 42; annotator B does so at 44. The LLM sweep instead makes three independent calls. Agreement on “type” therefore mixes multi-label action selection, severity, and vocabulary preference. No policy says whether simultaneous actions are permissible, which dominates, or what operational behavior each causes.

### LLM judge sweep

The paper evaluates one 56-action trajectory across `gpt-5.4-mini`, `gpt-5.4`, and an isolated Claude realization under windowed and macro context (Table 2, p. 6). Each intervention is judged separately. The main OpenAI script uses a “default false; when uncertain, false” system instruction and nominal deterministic decoding; the extended script omits the explicit `temperature=0.0` argument even though the paper says deterministic decoding. Model snapshots, endpoint dates, provider response IDs, seeds, retry policy, and raw trajectories are absent.

The released Claude v2 report is particularly informative about instability: windowed/reflect moves from 6 fires and F1 `.545` in one fresh-subagent run to 13 fires and F1 `.222` in another purportedly identical fresh-subagent run. The v2 implementation also uses six separate subscription-backed subagents rather than the same API mechanism as the OpenAI rows. This is evidence that configured judge realization matters, not a clean cross-vendor capability ranking.

The reported F1 code contains a small but meaningful semantics defect. When the detector predicts no positives but human positives exist, precision is undefined, recall is zero, and the code reports F1 as `N/A`. Standard binary F1 is normally defined as zero for this case (for example, `TP=0, FP=0, FN>0`). The paper's “dash denotes undefined (no true positives)” hides a definite total-miss outcome and makes the zero-firing floor look like missing information rather than failure under the selected binary target.

## Evidence and findings

### Recomputable human-label result

The release provides three complete 56-action label vectors and self-contained scripts. I reran both scripts successfully from commit `55c8bd2`; they regenerated the reported overlap and α reports. The raw overlap is more informative than a single coefficient:

- no action is flagged by all three annotators;
- six actions are flagged by two annotators: `{0, 2, 18, 33, 42, 44}`;
- 23/56 actions are flagged by at least one annotator;
- A and B share three locations, A and C share three, and B and C share none;
- base rates differ from 6 to 15 any-type flags.

This establishes poor exact-action reproducibility under this retained protocol. It does not reveal whether disagreement arises from temporal indexing, evidence view, action vocabulary, threshold/loss preferences, annotator competence, misunderstood instructions, or genuine policy plurality. The discarded 53/56 pass is direct evidence of rubric-comprehension sensitivity, but its raw labels and exact first/second briefs are not released.

The paper appropriately notes the kappa prevalence paradox and reports raw counts. Still, Landis–Koch bands and Krippendorff's generic `.667` guidance are not a validity theory for an intervention policy. There are no uncertainty intervals, trajectory-cluster replication, intrarater repeats, event-window tolerance analyses, or consequence-weighted comparisons. With one trace and three raters, α is a descriptive coefficient, not a stable population estimate.

### Saturation result

The released summaries show all five state traces cross frustration `.7` and stay above it, with A6 sustained-frustration rates from 39.3% to 79.7%. The per-action JSON permits inspection of these recorded outputs. But the raw SWE-bench traces, observer, engine, and trigger layer are absent; all engine-dependent scripts fail without proprietary modules. More importantly, post-v1 audit evidence shows no decay was possible. Therefore:

- **supported:** the recorded zero-decay accumulator reaches and retains the clamp on five selected traces;
- **not supported:** an operational, wall-clock-decaying affect monitor inevitably saturates because agents lack recovery;
- **still useful:** level-trigger persistence is a generic policy warning—once a state remains over threshold, an alarm needs edge semantics, hysteresis, cooldown, or an explicit repeated-action policy.

The later transition report shows that simple repairs are not automatically valid: acceleration fires zero times, and plateau-no-recovery fires on more than half the actions of two trajectories even before cooldown. The human-overlap section is redacted. Moving from levels to derivatives is therefore a hypothesis, not validated intervention timing.

### LLM judge result

The selected single-annotator F1 values are low and unstable, and the flagship OpenAI rows consume roughly 990k reported tokens at an estimated `$13.87` across six cells. These records support a narrow operational conclusion: per-action model judging over cumulative context can be costly, deferential, and realization-sensitive.

They do not identify a clean capability/context floor. There is one trace, one run for most cells, only 2–5 positive labels per type, no repeated OpenAI calls, no uncertainty, and a methodologically different Claude path. Full context changes both information and prompt length; it sometimes raises and sometimes lowers firing. The paper's abstract says frontier and cross-vendor models “only escape the zero-firing floor with full-trajectory context,” but released clean Claude windowed cells fire 7, 13, and 12 times. That wording is false for the Claude rows and should be limited to the selected OpenAI pattern.

Nor is F1 against Annotator A an authority-backed target. The paper does not explain why A is “primary,” compare every detector against all three raters, fit a perspectivist distribution, or evaluate the six 2-of-3 locations prospectively. It rightly refuses a post-hoc consensus rescore after looking at detector outputs, but that leaves the headline detector comparison tied to one unexplained viewpoint.

## Unique insight: timing is a policy equivalence problem, not an exact-index classification problem

The paper's strongest transferable lesson is more precise than “humans disagree.” An intervention benchmark must define the equivalence class of acceptable policies before measuring reliability.

Exact action matching assumes one uniquely correct instant. Real supervision often permits a **window**: intervene any time after sufficient warning appears but before an irreversible or costly boundary. Different actions may also be equivalent under the intended loss: clarify now, verify one step later, or pause before execution could all prevent the same consequence at different burden.

A better construct ladder is:

```text
frozen information boundary
  → observable event/risk state
  → acceptable intervention window or policy set
  → intervention type and authority
  → burden/capacity constraints
  → uptake and state change
  → prevented defect / introduced delay or harm
  → expected decision loss
```

This yields distinct estimands that must not be collapsed:

1. **Exact-location reliability:** do observers choose the same index under one convention?
2. **Event-window reliability:** do choices fall in the same predeclared acceptable region?
3. **Type reliability:** conditional on a shared opportunity, do observers choose the same action?
4. **Detector agreement:** does a monitor reproduce one observer or policy distribution?
5. **Downstream utility:** does acting on the trigger improve outcomes at acceptable burden?
6. **Decision validity:** is the policy preferable under declared error costs, authority, and review capacity?

The paper measures mostly the first and fourth on one trace. It does not measure the fifth or sixth. Low exact-index α can coexist with high policy utility; high detector F1 can coexist with needless interruptions. For `skill-bench`, escalation and clarification should be evaluated as configured intervention policies, not free-floating labels.

## Comparison with adjacent reviewed evidence

- **Expert disagreement** (`papers/agent-benchmarks/2026-07-11-expert-disagreement-human-feedback-validity.md`) shows that aggregation changes the target and that low agreement can reflect evidence gaps, rubric comprehension, scale use, framework differences, or value conflict. This paper supplies an especially clear rubric-comprehension failure but lacks the repeat/framework/context tests needed to call disagreement inherent.
- **HAS-Bench** (`papers/agent-benchmarks/2026-07-13-hasbench-configurable-human-participation-validity.md`) separates participant availability, event exercise, uptake, effect, and burden. An intervention-timing label establishes only a proposed event; it does not establish exercise, uptake, benefit, or real-human burden.
- **Agentic Confidence Calibration** (`papers/agent-benchmarks/2026-07-14-agentic-confidence-calibration-validity.md`) separates risk prediction from thresholded action and realized decision loss. HEART state and LLM verdicts are likewise candidate signals; neither selects an optimal intervention policy without transport, capacity, and outcome evidence.
- **Who&When Pro** (`papers/agent-benchmarks/2026-07-15-whowhen-pro-failure-attribution-validity.md`) shows that a known intervention index is not automatically a causal root. Here the converse matters: a disputed human timing index is not automatically invalid if multiple points are consequence-equivalent. Both require explicit intervention-to-consequence evidence.
- **Existing action/intervention guidance** in configured-system, trace, metric-monitoring, task-health, validity, participation, and artifact-transition contracts already has homes for evidence time, authority, action, consequence, burden, and claim ceilings. This source does not justify a new schema subsystem.

## Limitations and validity threats

1. All label-based results use one selected 56-action successful coding trajectory.
2. The five saturation traces are all Astropy coding runs with no declared sampling frame.
3. Three annotators cannot estimate a broad expert or operator population.
4. Annotator qualifications, authority, recruitment, training, compensation, and assignment are absent.
5. No within-annotator repeat distinguishes instability from stable disagreement.
6. The first degenerate annotation pass was discarded after rebriefing; raw first-pass labels and exact instrument versions are absent.
7. The retained label files contain no rationales, uncertainty, evidence locators, or observation-time metadata.
8. “Before action” conflicts with A10's inclusion of the current action's resulting observation.
9. Human and detector action-index/evidence-boundary correspondence is not demonstrated.
10. Exact index scoring has no tolerance window or policy-equivalence relation.
11. Pause, reflect, and clarify overlap conceptually and empirically; no action-composition policy is declared.
12. No intervention is actually executed, so benefit, harm, delay, uptake, and burden are unknown.
13. No irreversible boundary, risk severity, or false-interrupt/false-defer loss is specified.
14. α/κ have no confidence intervals and are based on one trajectory cluster with sparse positives.
15. Generic agreement cutoffs do not establish the reliability required for this decision.
16. Annotator A is used as the primary detector target without a disclosed authority or selection rule.
17. Detector scores against the other two annotators are not reported.
18. No prospective consensus, distributional, event-window, or consequence-grounded target is tested.
19. HEART is proprietary; observer, engine, guideline code, and psychological calibration cannot be audited.
20. Observer mappings from agent events to human-like affect are unvalidated.
21. Post-v1 audit shows replay decay was disabled by `Δt=0`, contradicting the v1 recovery mechanism.
22. Raw source trajectories are not released, blocking action-level label/evidence and parser audits.
23. Five recorded saturation outputs do not support trajectory- or domain-population generalization.
24. The claimed structural saturation result confounds zero decay, event mapping, clamp, thresholds, and selected traces.
25. A8/A9 results are discussed qualitatively but not fully tabulated with uncertainty in the paper.
26. Trigger families receive different evidence and produce different semantic object types.
27. The extended OpenAI sweep does not explicitly set temperature despite the deterministic-decoding claim.
28. Model snapshots, dates, provider IDs, seeds, retries, and invalid-output handling are incomplete.
29. Most judge cells have one realization; the one repeated clean Claude cell changes substantially.
30. Claude is subscription/subagent-based and not treatment-equivalent to OpenAI API calls.
31. Macro context changes prompt length and evidence simultaneously; truncation is position-dependent.
32. The abstract's claim that cross-vendor models escape zero firing only with full context is contradicted by clean Claude windowed firing.
33. F1 is reported `N/A` rather than zero for total-miss cells with positive human labels.
34. Cost is estimated using rough token splits/rates and omits annotation, trajectory, and intervention costs.
35. The post-v1 release mixes Paper 1 and companion Paper 2 artifacts, requiring careful timing separation.
36. Later transition-trigger human-overlap results are redacted, so the proposed repair is not validated.
37. No general autonomy, safety, professional-validity, production, or readiness claim is licensed.

## Reproducibility and operational realism

Reproducibility is **strong for the narrow retained label-vector statistics**. The immutable v1 paper, all three complete retained label files, self-contained κ/α scripts, coincidence details, and result reports permit exact recomputation. I reran `scripts/irr.py` and `scripts/krippendorff_alpha.py`; both reproduced the declared values and checks.

Reproducibility is **weak for the system and detector claims**. The package omits the proprietary HEART engine, observer, guideline implementation, raw SWE-bench traces, paper-time repository commit, raw annotation interface/instructions and discarded pass, OpenAI/Claude run manifests, and many raw judge outputs. Engine-dependent scripts cannot execute. The post-v1 commit is valuable precisely because it records an adverse audit, but it cannot retroactively make v1 reproducible.

Operational realism is low for intervention validity. Coding trajectories and real tool observations are more realistic than isolated text classification, and per-action monitoring surfaces genuine runtime cost. Yet no intervention is enacted; no operator receives a notification; no agent is paused, clarified, or repaired; no downstream result, latency, attention burden, false-alarm fatigue, or accountability transfer is measured. The zero-decay replay is also unlike a wall-clock runtime monitor. This is an incisive construct-warning study, not evidence for deploying or rejecting a supervision policy.

## Transfer to skill-bench

### 1. Freeze the temporal decision boundary

Every intervention opportunity should declare:

- checkpoint identity (`pre_action`, `post_action_pre_next`, `post_artifact`, or retrospective audit);
- latest admissible event and excluded future channels;
- proposed action visibility versus executed-action observation visibility;
- exact state/trace prefix hash;
- latency and expiry semantics.

A grader must fail closed if it uses observations unavailable at the declared decision time.

### 2. Replace point labels with predeclared policy targets where warranted

Depending on the domain, represent one of:

- exact mandatory gate tied to a hard authority boundary;
- acceptable event window with earliest-warning and latest-safe boundaries;
- set of consequence-equivalent interventions;
- risk score plus frozen threshold/loss/capacity rule;
- distribution of framework-indexed observer choices;
- explicit deferral/escalation policy.

Do not introduce tolerance after inspecting detector outputs.

### 3. Separate signal, decision, and consequence

Store candidate state/risk signals independently from the intervention policy. For each intervention preserve availability, trigger, exercise, response, uptake, state change, prevented/introduced defect, burden, and counterfactual basis. Agreement with a label is one observer metric; utility requires matched intervention evidence.

### 4. Evaluate policy-level reliability and utility

A bounded validation should compare, under frozen evidence views and equivalent forms:

- no intervention;
- fixed checkpoints;
- event-window or deterministic rule;
- model/state detector;
- human/operator policy;
- sham/no-op interruption where feasible.

Report exact/window/type agreement, false interruption, missed severe boundary, task outcome, recovery, latency, operator workload, and declared expected loss separately. Repeated tasks and multiple unlike work shapes are required before transport claims.

### 5. Preserve disagreement rather than laundering consensus

Collect observer role/authority, exact evidence view, rationale, uncertainty, repeat labels, framework/policy, and action costs. Test rubric comprehension and index convention before interpreting α. If stable policies differ, preserve them as policy alternatives and make the aggregation/selection rule explicit.

### 6. Treat timer and recovery semantics as configured components

Pin wall-clock/logical-time source, cadence distribution, pause periods, decay or forgetting rule, missing timestamps, tool latency, edge/level semantics, hysteresis, cooldown, and reset policy. A fixed threshold over a pure accumulator is a different instrument from a wall-clock-decaying risk monitor.

## Concrete repository actions

1. **Add no new schema or build task.** Existing configured-system, trace/intervention/recovery, participation, task-health, metric-monitoring, validity, and plural-observer machinery can represent the requirements. The pending `validate-intervention-attribution-rungs` task already exercises intervention, sham, repair, alternatives, and consequence boundaries; this review should refine its evidence-time and acceptable-window checks rather than create a duplicate.
2. **For any future escalation/clarification pilot, predeclare the checkpoint and policy equivalence class.** Include planted one-step temporal-leakage and index-shift mutations, and reject graders that consume the current action's unavailable observation.
3. **Do not use v1's five-trace result as evidence for affective-monitor structural saturation.** Cite it only as a zero-decay level-trigger failure discovered and bounded by the post-v1 audit.
4. **Do not optimize F1 to one primary annotator.** First establish observer authority, repeat reliability, admissible evidence, acceptable intervention windows, and downstream decision loss.

## Action items completed

- [x] Read the complete immutable v1 PDF/text.
- [x] Inspected the pinned official post-v1 repository, all retained labels, reliability reports/scripts, saturation/sweep reports, LLM prompt/metric code, and the companion `Δt` audit/timing/transition evidence.
- [x] Reran both released self-contained reliability scripts and reproduced their declared checks.
- [x] Separated paper claims, post-v1 correction evidence, released-artifact evidence, and `skill-bench` adaptations.
- [x] Compared directly with expert-disagreement, HAS-Bench, Agentic Confidence Calibration, Who&When Pro, and existing intervention-policy machinery.
- [x] Added no duplicate queue task and made no autonomy, safety, professional-validity, production, or readiness claim.
