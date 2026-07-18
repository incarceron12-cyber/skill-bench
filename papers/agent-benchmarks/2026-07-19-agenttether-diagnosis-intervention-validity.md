# AgentTether: repair-package efficacy does not validate root localization or transferable memory

## Source and review status

**Deep review of the complete immutable primary source.** I read the full 12-page arXiv v1 paper and checked the method, equations/descriptions, figures, tables, denominators, ablations, and availability statement against the preserved PDF, layout text, and TeX source archive.

- **Paper:** Chenyu Zhao et al., *AgentTether: Graph-Guided Diagnosis and Runtime Intervention for Reliable LLM Agent Operation*, arXiv:2607.06273v1, <https://arxiv.org/abs/2607.06273v1>
- **Version read:** immutable v1, submitted 7 July 2026; no withdrawal/retraction notice
- **Local PDF:** `data/papers/pdfs/2607.06273v1-agenttether.pdf` (12 pages; SHA-256 `cea3202f209976220a0269ff6b047f6bfb6c0b5293e9065d751df768cedc8916`)
- **Full local text:** `data/papers/text/2607.06273v1-agenttether.txt` (SHA-256 `25365adbbd11286521d33d7fca6bcfb399132c67177ce352f8040225f9cd0068`)
- **TeX source:** `data/papers/source/2607.06273v1-source.tar` (SHA-256 `5cfc34c06b7c247ea5689df6e7d504791e086f25b0cf926aae6c678c5d7c1a33`)
- **Acquisition/release provenance:** `data/sources/releases/2607.06273v1-agenttether/provenance.json`

The paper-linked anonymous 4open.science repository was unavailable at acquisition. Its canonical URL redirected to a repository-file API that returned HTTP 401 `{"error":"not_connected"}`; the metadata, file, and zip routes failed alike. Headers and body are preserved beside the provenance manifest. Therefore **no implementation, task membership, trace, Repair Memory record, intervention log, raw outcome, or table-building artifact was inspected**. All experimental evidence below is manuscript-reported rather than independently recomputed.

## One-sentence contribution

AgentTether joins trace compression, graph-anomaly localization, LLM-authored repair guidance, within-task cross-attempt state, and guarded runtime corrections into one retry wrapper, but its selected initially-failed-task results establish only a configured **diagnosis-plus-guidance-plus-monitoring package effect**: the study does not independently validate the selected root, isolate what Repair Memory stores or transfers, reconcile environment state across retries, or show that endpoint repair was caused by the diagnosed transition.

## Why this matters for skill-bench

This paper addresses a central charter objective: benchmark output should diagnose and help repair failures, not merely produce a final score. Its strongest engineering idea is the separation of three moments that are often collapsed:

1. **post-run localization:** nominate evidence-bearing suspicious transitions;
2. **between-run guidance:** transform a diagnosis into scoped correction state;
3. **during-run control:** decide whether and how to reassert that correction.

That separation is reusable across professional domains. A spreadsheet agent may need an upstream evidence-selection correction preserved through later formula and formatting work; a research agent may need a source-authority warning kept active until synthesis; a workflow agent may need a prerequisite checked before an irreversible state change. Banking is therefore a bounded mechanism case, not a proposal to narrow `skill-bench` to customer service.

The validity lesson is equally important: **a repaired endpoint cannot back-validate every upstream stage of the package**. AgentTether's guidance is generated from a detector packet, full failure evidence, an analyst model, prior repair state, and later verifier explanations; runtime checks can catch loops, unsatisfied expected actions, or destructive drift even if the nominated “root” is wrong. Three retries add further rescue opportunities. Successful completion may validate the whole configured support package while leaving root localization, diagnosis fidelity, memory necessity, semantic adoption, and intervention mechanism unresolved.

This review advances charter objectives A–C through targeted expansion and validation. Useful transfer is a typed diagnosis-to-intervention evidence chain and stricter denominators, not another domain-specific repair subsystem.

## Research question and claim boundary

The paper asks whether failed stateful tool-agent runs can be recovered by combining dependency-aware graph diagnosis, persistent repair guidance, and sparse runtime intervention; whether the package transfers across agent model families; and what runtime intervention adds beyond post-run guidance (§§I, IV, pp. 1–7).

### Strongest defensible claims

The manuscript reports that:

- one Qwen3.7-max initial run over 261 τ-bench tasks left 123 failures: Retail 26/114, Airline 14/50, and Banking 83/97 (§IV-A, Table I, pp. 7–8);
- on those same selected failed runs, “resolved” means success in any of up to three later repair iterations; blind retry resolves 53/123, post-run-only AgentTether 74/123, and full AgentTether 85/123 (Table I, p. 8);
- on the 83 Qwen Banking failures, full versus post-run-only has 13 helped and 3 hurt task outcomes, a manuscript-reported exact McNemar `p=.021`; Retail has 1/0 and Airline 2/2 (Table III, p. 9);
- on a separate GPT-5.4 Banking initial run, 86/97 tasks fail, of which blind retry resolves 15, post-run-only 52, and full AgentTether 56 (§IV-C and Fig. 5, p. 9);
- removing the offline HGT or Repair Memory from the full Qwen package lowers reported repair from 85/123 to approximately 57/123 and 64/123 respectively (Table II, p. 9);
- the detector-union packet covers the paper's earliest-violated-action proxy in 56/78 selected Qwen Banking behavioral failures; its peak is a median 5.5 Transition Units from that proxy, versus 6.0 for recency and 10.0 for frequency (§IV-B, pp. 8–9);
- runtime intervention can hurt: the three Banking hurt cases average 29.3 interventions, compared with 11.3 in the 13 helped cases (§IV-D, pp. 9–10).

These support a bounded conclusion: on manuscript-reported, model-specific, initially failed τ-bench runs, the full configured package has a higher cumulative any-retry resolution rate than the named baselines, and runtime intervention has a positive paired net result on Qwen Banking under the paper's trial protocol.

### Claims not licensed

The study does **not** establish:

- root-cause accuracy, earliest cause, necessity, sufficiency, or a causal transition graph;
- that the analyst's final turning point agrees with an independent label;
- that repair success was mediated by the selected root or guidance proposition;
- transferable memory across tasks, users, domains, or models;
- a model-family transfer effect on common failed cases;
- repeated-run reliability, calibrated success probabilities, or a prospective repair policy;
- equal environment state, world history, evaluator behavior, or resource opportunity across retry arms;
- production observability, safety, professional validity, deployment value, or readiness.

The paper itself appropriately limits production generalization in §V (pp. 10–11), but its “root cause,” “causal,” “transfer,” “oracle-free,” “reliability layer,” and “practical” language often outruns the reported design.

## Methodology and system

### 1. Attempt population and repair estimand

All approaches share one initial execution. Only tasks that fail this realization enter repair, with at most three later iterations; a condition is counted resolved if one later run succeeds (§IV-A, pp. 7–8). This is a useful operational estimand:

> Among this model/configuration's failures on one initial attempt, what fraction obtain at least one success under this bounded adaptive retry package?

It is not a task-population capability rate or per-attempt reliability. Reconstructing the full-suite arithmetic from the reported counts, the Qwen initial run succeeds on 138/261 (52.87%); carrying initial successes forward and adding full-package repairs yields 223/261 (85.44%). This latter number is only an **initial-success-or-any-repair composite**, not 85.44% reliability on fresh independent trials. Domain composites are 113/114 Retail, 47/50 Airline, and 63/97 Banking. For GPT-5.4 Banking they are 67/97. The paper wisely reports conditional repair rates instead, but readers must not promote them into unconditional or repeated operational reliability.

The selection is outcome-conditioned and model-specific. Retail's selected failures are much easier for blind retries (23/26) than Banking's (22/83). GPT-5.4 and Qwen Banking have different failed sets (86 versus 83), so comparing their conditional percentages does not rank the models or demonstrate transport on common units.

The report does not identify initial-attempt seed/temperature, repeated initial runs, per-iteration seeds, environment reset/persistence semantics, invalids/timeouts, retry exceptions, evaluator disagreements, or exact stopping ledger. “Cumulative repair” and average resource use therefore mix early stopping with up to three opportunities. The first guided iteration accounts for 36 of 49 Qwen and 47 of 56 GPT repairs (the percentages in Fig. 5 imply exact integer counts), while later iterations contribute smaller selected increments; no per-iteration invalid or new-regression table is shown.

### 2. Trace acquisition and Transition Units

The wrapper monkey-patches known LLM SDK entry points and records LLM calls, tool invocations, environment responses, request/response payloads, and session context (§III-B, pp. 4–5). It compresses execution into ordered Transition Units `TU_k=(o_k,b_k,a_k,f_k)`:

- observation/context;
- natural-language belief/reasoning;
- action (tool call or text response);
- execution/environment feedback.

Derived status, error signature, inferred intent, artifacts, spans, metrics, logs, and verification records can attach to each TU. This is a useful behavioral unit: finer than a final artifact, more semantic than raw events, and stable enough to anchor evidence and correction.

But “complete behavioral trace” is stronger than the instrumentation warrant. SDK monkey-patching does not automatically capture hidden model state, provider routing/version, uninstrumented SDKs, direct subprocess or network calls, asynchronous actors, environment snapshots, permission changes, caches, clocks, credentials, external service mutations, or an evaluator's hidden state. Natural-language “belief” may be unavailable, model-generated, or behaviorally unfaithful. TU identity is a projection whose coverage and semantic equivalence need adapter-level tests.

### 3. Critical Transition Graph

Each TU is a node. Directed temporal edges link adjacent units; dependency edges link units sharing inferred artifacts, state, or error signatures (§III-C, pp. 5–6). This preserves non-local links better than a flat trace and can nominate upstream evidence packets.

Calling the graph “causal” is not yet warranted. Shared artifact/signature and temporal precedence are association or dataflow candidates, not identified causal edges. The paper does not specify edge extractors, ambiguity resolution, edge precision/recall, direction for the displayed unordered dependency notation, latent common causes, omitted dependencies, alternative graph validity, or perturbation tests. The release blocker prevents inspection of whether edge construction uses model inference, string matching, manually coded τ-bench fields, or benchmark-aware checks.

### 4. Dual detectors and evidence views

The offline detector is a heterogeneous graph transformer trained self-supervised for 20 epochs over 21,143 success-only trajectories: 11,079 TerminalBench, 10,010 SWE-smith, and therefore only 54 described as other operational traces (§III-C and §IV-A, pp. 5–7). It reconstructs telemetry edges and masked categorical fields, then scores edge/attribute surprise. The run-local Isolation Forest uses 25 graph-contextual features, 100 trees, maximum subsample 256, one-hop context, and seed 42. The union of their anomaly frontiers becomes suspicious substructures.

There are four important boundaries:

1. **Success-only is not “normal” by definition.** Successful runs can contain unnecessary, unsafe, or fragile processes, while valid alternative paths can be rare and anomalous.
2. **Cross-domain structure is a hypothesis, not demonstrated transport.** Nearly all named offline training records are software/terminal trajectories; τ-bench semantics are excluded, but tool and telemetry taxonomies may still be mismatched.
3. **Outcome/status-bearing fields may make anomaly easier without identifying cause.** The feature schema includes status, phase, outcome, verification, and error information. That can be legitimate post-run evidence, but it is not a pure behavior prior.
4. **Union increases opportunity to cover a proxy.** The paper reports no frontier size, evidence-packet length, false-positive burden, random/size-matched packet control, precision, or coverage–compression curve. Coverage cannot be interpreted without how many TUs are retained.

The no-HGT ablation shows that removing this input from the entire downstream package lowers endpoint resolution. It does not independently prove detector accuracy: packet content, analyst prompt evidence, guidance, Repair Memory, and runtime checks all change downstream.

### 5. Analyst, feedback builder, and localization evidence

For each suspicious region, the method keeps a peak-scoring TU plus local/dependency context and detector signals. An analyst LLM sees this packet and outcome-failure evidence, then emits root cause, turning point, and recovery hints. A feedback builder converts these into concise directives and an injection plan, deliberately avoiding exact parameter values (§III-C, p. 6).

This is a multi-stage transformation:

`trace projection → graph edges → detector frontiers → compact packet → analyst diagnosis → recovery hints → directive/injection plan`.

V1 validates none of those semantic transformations independently. Its only localization analysis is detector-packet coverage **before analyst confirmation**. On 78 Qwen Banking failures with violated action checks, `g` is the position of the earliest violated τ-bench gold action and `p̂` the peak detector TU. The packet contains `g` in 56 cases (71.8%), and median `|p̂-g|` is 5.5 TUs, only half a TU better than recency's 6.0 (§IV-B, pp. 8–9). No confidence interval, paired distribution, packet-size control, exact-hit rate, signed error, task cluster, analyst-point accuracy, explanation correctness, or human adjudication appears.

Moreover, `g` is defined by the **earliest externally visible violated required action**, not an independently established causal root. Missing required actions do not naturally occupy an executed TU; a malformed argument may reflect earlier misunderstanding; and a gold-path action list may exclude valid alternatives. The paper acknowledges `g` as a conservative proxy, but then interprets packet coverage and endpoint ablations as root localization. At best, the result supports moderate proximity/coverage to one benchmark-derived violation marker.

### 6. Repair Memory lifecycle

Repair Memory is read before new guidance and updated after each run with which directives are “fixed” or “unresolved” (§III-C, p. 6). This is conceptually valuable: feedback should have lifecycle state rather than be repeatedly pasted. But the paper does not specify the record schema, writer/reader prompts, authority, evidence locators, status criteria, contradiction handling, version hashes, update atomicity, rollback, correction deletion, stale-state detection, or whether memory contains only directives or also task-specific observations and evaluator explanations.

Most importantly, this is **within-task, within-repair-episode state**, not demonstrated reusable memory. The ablation removes accumulated repair state across up to three retries on the same selected failure and lowers endpoint repair. It may show value from additional task-specific context, repeated outcome-conditioned guidance, attempt history, or longer prompt exposure. There is no memory reuse on a held-out task, equivalent form, new user, new domain, or new model. The GPT experiment reruns the AgentTether method on GPT-specific failures; it does not transfer a Qwen-derived Repair Memory into GPT-5.4.

### 7. Runtime Check–Decide–Inject policy

At tool returns and text responses, the wrapper checks (§III-D, pp. 6–7):

- exact repeated tool calls;
- embedding-based intent drift with risk-tier thresholds and five-step EMA;
- expectation deviation from guidance/memory;
- unresolved structural checks after progress or before submission.

Evidence grounding, cooldown/deduplication/caps, and a minimal-response policy gate interventions. Tool-return corrections are appended to the result; text corrections become synthetic user messages. Interventions stop after expected corrective actions complete; following expected state-changing action, only loop breaking remains active.

This is the paper's most operationally useful design. It types trigger, evidence, channel, spacing, cap, and stop behavior. Yet the mechanism is a treatment bundle. Runtime intervention is generated from active guidance **and the verifier's explanation** (§III-D, p. 7), so it can introduce information beyond a simple persistence reminder. The synthetic-user channel changes participant role and authority. Appending text to a tool result changes the semantics and provenance of environment feedback. Embedding thresholds are fixed but uncalibrated by domain/model; “expected corrective action” is itself analyst-derived; and no trigger-level confusion matrix, false-intervention denominator, opportunity count, no-op/sham arm, threshold sweep, or channel ablation is reported.

Table III does show collateral risk: three Banking tasks succeed post-run-only and fail with intervention. Helped cases average 11.3 interventions and hurt cases 29.3, but this is post-treatment descriptive selection—not evidence that high intervention count causes harm. Long/difficult cases can both trigger more and fail more. The paper correctly presents adaptive intervention strength as future work.

### 8. Baselines and treatment parity

Blind retry receives no feedback; outcome feedback receives evaluator assessment; Reflexion receives agent-authored reflection; post-run-only AgentTether receives detector/analyst/memory guidance; full AgentTether adds runtime checks and corrections (§IV-A, pp. 7–8). These are sensible practical packages, not matched single-variable interventions.

They differ in information content, model calls, prompt length, timing, cross-iteration state, verifier access, opportunities, and early stopping. “Auxiliary roles are fixed across approaches” means the simulator/evaluator identity is common and AgentTether roles use DeepSeek-V4-Pro, but approaches that do not call analyst/verifier cannot have the same realized auxiliary treatment. Reflexion also uses the repaired agent itself. The result compares configured support policies, not graph diagnosis against an equal-information nongraph diagnosis.

The component ablations are closer but still alter downstream context. A stronger design would retain packet size and analyst budget, replace graph selection with random/recency/frequency packets, freeze diagnosis text while toggling memory lifecycle, replay identical trigger opportunities with real versus sham corrections, and cross diagnosis correctness with intervention availability.

## Evidence and result interpretation

### Endpoint repair

Table I's paired task counts are the strongest evidence. On the 123 Qwen failures, full AgentTether resolves 85 versus 53 for blind retry and 74 for post-run-only. Banking drives most of the gain and most selected failures. Outcome feedback is below blind retry overall (48 versus 53), and Reflexion is near it (55). AgentTether also uses fewer reported agent turns and fewer “method tokens” than blind retry, though it is slower than post-run-only.

The manuscript's efficiency accounting needs careful wording. “E2E Tokens” includes agent and AgentTether analyst/verifier input/output but excludes τ-bench user-simulator/evaluator calls as fixed. Banking values are enormous—1.197 million average method tokens for full AgentTether and 1.376 million for blind retry across repair iterations. Averages are conditional on initially failed tasks and affected by early stopping. They omit initial shared-run cost, benchmark user/evaluator tokens, offline HGT training, embeddings, telemetry/storage, engineering, provider spend, and human review. This supports a conditional method-token comparison, not low cost or deployment value.

Wall time is 15.59 minutes full, 13.47 post-run-only, and 16.32 blind retry overall. Full being faster than blind despite auxiliary work is plausible under fewer turns; without run-level distributions, invalids, concurrency policy, provider dates, and repeated timing, it is descriptive rather than a stable latency advantage.

### Runtime intervention effect

The within-failure-set full versus post-run-only pairing is the cleanest ablation. Banking's 13 helped/3 hurt yields a positive net and reported exact test; Retail and Airline are tiny/neutral. This supports a Banking-specific package increment. It does not establish that intent drift, structural checks, or a particular channel caused the gain, and no multiplicity policy covers three domains plus other comparisons.

### Cross-model result

GPT-5.4 has 86 initially failed Banking tasks, compared with Qwen's 83. Its blind/post/full repair counts are 15/52/56. This shows the package can be run with a second agent model and obtain substantial manuscript-reported repair on that model's selected failures. It does not show diagnosis “transfer” in the usual sense:

- task units differ after conditioning on model-specific initial failure;
- no common-failure intersection or equivalent difficulty analysis is shown;
- DeepSeek analyst/verifier and method remain the same, but no Qwen memory, detector update, or learned repair object is transported;
- only one domain is used;
- no repeated model endpoints or uncertainty are reported.

The proper label is **cross-model application of one configured repair method**, not transferred Repair Memory or a model-invariant effect.

### “Oracle-free” boundary

AgentTether does not require a reference answer to build its detector and does not use τ-bench gold actions for runtime localization according to the method. That is a useful distinction. It nevertheless activates only after an outcome failure signal, gives the analyst outcome-failure evidence, derives expected actions through model judgments, and evaluates success with τ-bench's benchmark evaluator. Table IV's undifferentiated “Oracle-Free” checkmark should therefore be read narrowly as “no ground-truth answer/test supplied to the repair method,” not no observer, verifier, policy, or failure oracle.

## Unique insight

AgentTether's durable contribution is a **diagnosis-to-control chain**, but its study reveals that every join needs separate evidence:

```text
failed outcome observation
→ trace/event coverage
→ Transition Unit projection
→ dependency-edge support
→ anomalous packet selection
→ independently adjudicated locus/diagnosis
→ guidance proposition and public basis
→ memory write/read/status transition
→ actual decision opportunity
→ trigger and verifier disposition
→ delivered correction channel
→ semantic access/adoption
→ intended action/state change
→ accepted repair
→ collateral/new-error check
→ repeated equivalent-case effect
→ held-out transfer
→ operational value
```

No arrow inherits the next. In particular:

- packet overlap with an earliest violated action does not prove a root;
- a plausible diagnosis does not prove that guidance encodes it faithfully;
- stored guidance does not prove retrieval or adoption;
- a trigger does not prove a needed intervention;
- a repaired endpoint does not prove diagnosis mediation;
- an endpoint package gain does not prove cross-task memory;
- lower turns on selected failures do not prove production reliability or value.

A decisive future experiment is a **diagnosis × intervention factorial**. Independently blind-adjudicate diagnosis correctness, then randomize matched failed cases to correct diagnosis, plausible-wrong diagnosis, surface-only diagnosis, and sham text; cross these with no runtime control, generic checkpoints, diagnosis-bound control, and deliberately mistimed control. Preserve equal information/resource envelopes and isolated retry state. If diagnosis-bound intervention helps mainly when diagnosis is independently correct—and changes the nominated action/state without extra collateral failure—the root-to-repair bridge gains evidence. Endpoint repair alone cannot supply that bridge.

This sharpens adjacent reviews rather than duplicating them:

- **STRACE** proposes structural causal slices and persistent updates but has weaker intervention validation; AgentTether adds a complete support loop while retaining inferred-graph risk.
- **Causal Agent Replay** executes typed suffix interventions and exposes actor/world/observer replay assumptions; AgentTether instead injects broad guidance into fresh adaptive retries, so it supports operational package repair but even less isolated causal attribution.
- **Who&When Pro** knows the injected construction delta but cannot promote it to a natural root; AgentTether starts from organic configured failures but lacks known-root or counterfactual labels.
- **The Compliance Trap** separates delivery, action change, propagation, and recovery; AgentTether measures directive survival but not proposition-specific access/adoption or accepted state repair.
- **AFTER** requires held-out task/role/model transfer edges; AgentTether's Repair Memory never leaves the source task episode.
- **UniClawBench** exposes semantic leakage through evaluator-generated follow-up; AgentTether likewise injects verifier-informed corrections, making final success evaluator-assisted package performance rather than unaided reliability.

## Limitations and validity threats

1. Only one initial attempt per task/model is reported; the failure set is realization-dependent.
2. All repair analyses condition on that observed initial failure.
3. Any-success over up to three adaptive retries is not per-attempt reliability.
4. Initial successes and selected failures belong to very different domain mixtures.
5. GPT and Qwen conditional sets are not common task populations.
6. No repeated initial-run or repair-run uncertainty is reported.
7. Seeds/sampling settings for repaired agents are not specified in the paper.
8. Provider endpoint revisions and run dates are absent.
9. Environment reset versus persistence across retries is not specified.
10. Stateful tool mutations can change the starting world for later attempts.
11. Invalid runs, timeouts, exceptions, missing judgments, and retries are not ledgered.
12. Early stopping changes attempts and resource opportunity by condition.
13. No per-iteration new-error or regression denominator accompanies cumulative repair.
14. SDK monkey-patching may miss uninstrumented calls and hidden state.
15. “Complete trace” excludes provider, world, service, clock, permission, and collaborator state unless separately captured.
16. Natural-language beliefs are not validated as faithful internal reasoning.
17. TU construction correspondence and adapter conformance are not evaluated.
18. Shared artifact/error-signature edges are not automatically causal dependencies.
19. Dependency edge extraction, precision/recall, ambiguity, and direction are under-specified.
20. Offline “normal” training consists only of success-labeled trajectories, which can contain bad process.
21. Named HGT counts leave only 54 of 21,143 trajectories outside TerminalBench/SWE-smith.
22. Cross-domain telemetry transport from software tasks to τ-bench is assumed, not measured.
23. Status/outcome/verification features can expose symptoms without identifying roots.
24. The union of detectors has no packet-size or random-size-matched control.
25. No coverage–compression, precision, false-positive, or review-burden curve is reported.
26. The localization target is earliest violated gold action, not an independently established cause.
27. Missing required actions and valid alternative paths complicate positional targets.
28. Packet coverage is only 56/78 and does not validate the analyst's final turning point.
29. Median peak error 5.5 versus recency 6.0 has no uncertainty or paired test.
30. Communication-only failures are excluded from localization analysis.
31. No human/expert blind diagnosis, agreement, or adjudication is reported.
32. Analyst input includes outcome-failure evidence in addition to detector evidence.
33. Diagnosis-to-guidance semantic fidelity is not evaluated.
34. Guidance can encode several directives, so repair cannot identify one root.
35. Repair Memory schema, status rules, evidence, versions, and rollback are unavailable.
36. Memory states are model/analyst-authored rather than independently verified facts.
37. Removing memory also removes task-specific cross-iteration context and exposure.
38. No held-out task, form, role, domain, user, or model consumes a source memory.
39. GPT reruns the method; it does not receive transferred Qwen memory.
40. Runtime triggers have no labeled opportunity denominator or confusion matrix.
41. Intent thresholds and EMA are fixed without calibration evidence.
42. “Expected” actions derive from guidance/memory and can preserve a wrong diagnosis.
43. Verifier explanations contribute to injected corrections, broadening the treatment.
44. Synthetic user messages change authority and participant-role semantics.
45. Appended tool-return guidance changes environment-feedback provenance.
46. Trigger caps/cooldowns are specified but no fire/eligible/suppressed ledger is released.
47. Helped/hurt intervention counts are post-treatment descriptive subsets.
48. More interventions may mark harder tasks rather than cause failure.
49. No no-op, generic-checkpoint, sham, timing, channel, or threshold factorial is reported.
50. Baselines differ in information, model calls, context, state, timing, and opportunities.
51. Outcome feedback and Reflexion are not equal-information controls for graph selection.
52. HGT and memory ablations change the whole downstream package.
53. Only Banking has a significant runtime increment; Airline is neutral.
54. No correction for the study's many domain/component/model comparisons is stated.
55. Task/template/domain clustering is not modeled.
56. Conditional method-token averages omit the shared initial run and evaluator calls.
57. Offline training, embeddings, storage, engineering, and human costs are omitted.
58. Huge Banking token counts limit “practical” interpretation without priced total cost.
59. Wall time is single-study provider latency, not a stable operational property.
60. “Oracle-free” still relies on a failure signal, analyst/verifier judgments, and benchmark outcome evaluation.
61. τ-bench checks selected policy/state outcomes, not production reliability or professional validity.
62. No recurrence study tests whether fixes remain useful after the three-iteration episode.
63. No safety, authorization, privacy, stakeholder, or collateral-state evaluation supports deployment.
64. No human debugging-time or decision-quality study establishes operational value.
65. The anonymous release is disconnected, so implementation and result correspondence are unaudited.
66. Raw tasks-as-run, traces, memories, interventions, outcomes, and analysis inputs are unavailable locally.
67. Reported counts and tests cannot be independently reconstructed.
68. The paper's production framing exceeds its single benchmark, two model labels, and one cross-model domain.

## Reproducibility and operational realism

**Paper inspectability: moderate.** The method description, hyperparameters, main denominators, resource averages, paired helped/hurt counts, and immutable TeX are available. The 261-task and 123-failure accounting is internally coherent, and the GPT Banking figure is arithmetically coherent with 86 failures.

**Result reproducibility: low at acquisition.** The advertised repository is disconnected. There is no accessible exact implementation, environment image, task membership, model receipt, run date, seed, initial trace, retry trace, memory record, intervention log, raw evaluator output, invalid ledger, or table-builder input. The paper's aggregate tables remain author reports.

**Operational realism: bounded.** τ-bench provides stateful policy-governed tool interactions and verifiable consequences, and the wrapper's hook/trigger/channel/stop design is closer to an operating repair system than a static benchmark. But it remains one synthetic benchmark substrate. Retry state semantics, live service mutability, permissions, privacy, rollback, real user authority, stakeholder acceptance, production failure prevalence, maintenance burden, and downstream value are unmeasured. The correct claim is configured benchmark repair, not production reliability.

## Transfer to skill-bench

### Retain

1. Transition Units as typed decision–execution–feedback anchors, with raw-event locators retained.
2. Separate post-run diagnosis, between-run repair state, and runtime intervention records.
3. Dependency candidates in addition to temporal adjacency, while labeling their evidence status.
4. Explicit trigger, verifier, channel, cooldown, cap, stop, and suppressed-intervention records.
5. Helped and hurt paired outcomes rather than gain-only reporting.
6. Model-specific initial-failure denominators and a bounded retry budget.
7. Separate agent turns, wall time, and complete method-token accounting.

### Repair

1. Rename CTG edges `dependency_candidates` until extraction or intervention evidence validates causal use.
2. Record TU projection coverage, omitted events, adapter identity, raw-event spans, and semantic stability.
3. Bind every diagnosis to packet size, selected/omitted TUs, edge evidence, analyst identity, outcome view, and independent disposition.
4. Keep `earliest_violated_requirement`, `selected_anomaly`, `analyst_turning_point`, `supported_cause`, `best_repair_locus`, and `surface_failure` separate.
5. Make Repair Memory an immutable lifecycle ledger: proposition, source attempt, evidence, authority, status, read/write receipt, contradiction/supersession, scope, target opportunity, and rollback.
6. Distinguish within-task retry state from held-out transferable procedural memory.
7. Preserve initial state, pre/post state deltas, reset/rollback receipts, and invalidity for every attempt.
8. Record all eligible trigger opportunities, fires, suppressions, verifier dispositions, delivered propositions, adoption evidence, state effects, collateral failures, and cost.
9. Type injected channels and authority: tool-result annotation, system guidance, benchmark supervisor, synthetic user, real user, or policy gate.
10. Report current-iteration success, cumulative any-success, attempts-to-repair, unresolved censoring, recurrence, and equivalent-form reliability separately.

### Test

1. **Known-locus conformance:** planted malformed argument, missing prerequisite, stale source, contradictory evidence, redundant cause, downstream symptom, valid alternate route, and communication-only failures.
2. **Packet controls:** graph, recency, frequency, random size-matched, full trace, and oracle-local packet under equal analyst/token budgets.
3. **Diagnosis × intervention factorial:** independently correct/plausible-wrong/surface/sham diagnosis crossed with none/generic/diagnosis-bound/mistimed runtime control.
4. **Memory lifecycle:** no memory, repeated static guidance, typed fixed/unresolved ledger, corrupted status, stale memory, contradiction, rollback, and held-out equivalent-form reuse.
5. **World-state policy:** fresh reset, intentional persistence, rollback, partially irreversible action, and invalid reset; require state receipts.
6. **Trigger calibration:** true/false opportunities, threshold/cooldown/cap sweeps, channel arms, suppression correctness, and over-intervention harm.
7. **Mediation:** verify diagnosis proposition → delivered guidance → actual opportunity → adopted action → intended state delta → accepted repair, not endpoint only.
8. **Reliability and value:** repeated seeds, prospective stopped policy, new-error/side-effect vectors, total cost, reviewer time, recurrence, and human-assisted repair utility.
9. **Transfer:** frozen source memory to held-out task/form/domain/model under equal evidence volume, with task/author/verifier lineage and untouched transport sets.

## Concrete repository actions

- [x] Read the complete immutable v1 PDF/text and verify source identity against the TeX archive and provenance manifest.
- [x] Reconcile 261 assigned tasks, 123 Qwen failures, domain-specific failure sets, 85 repairs, 83/86 Banking denominators, and the implied unconditional composites.
- [x] Separate detector-packet coverage from analyst localization, causal root, guidance fidelity, and endpoint repair.
- [x] Separate within-task Repair Memory from cross-task/model procedural transfer.
- [x] Compare AgentTether explicitly with STRACE, Causal Agent Replay, Who&When Pro, The Compliance Trap, AFTER, and UniClawBench.
- [x] Update `data/papers/index.json` and `papers/topic-index.md`.
- [x] Add no build/consolidation task. Existing benchmark-bundle trace/recovery records, compounding-lesson lifecycle, longitudinal streams, configured-system identity, validity arguments, metric monitoring, task health, execution isolation, and the internal intervention-attribution work already house these requirements. An AgentTether-specific schema or another synthetic repair pilot would duplicate active machinery.

## Bottom line

AgentTether is a useful systems hypothesis and one of the clearest end-to-end sketches of a failed-run support loop: compress behavior into decision units, nominate dependency-linked anomalies, author scoped guidance, retain fixed/unresolved state, and intervene sparingly when re-execution drifts. Its manuscript-reported endpoint evidence is nontrivial. On one shared Qwen initial run, full AgentTether resolves 85/123 selected failures versus 53/123 under blind retry; runtime intervention has a positive paired Banking increment with acknowledged hurt cases; and a second model shows the same broad package ordering on its own Banking failure set.

The diagnosis claims remain much weaker. The sole localization target is the earliest violated benchmark action, detector packets cover only 56/78 cases, the peak's median distance barely improves on recency, and the final analyst diagnosis is not independently scored. Guidance, memory, verifier explanations, generic loop/expectation checks, three adaptive retries, and changing context all provide routes to repair without a correct root. The memory never crosses a task episode; the GPT result is method reuse, not memory transfer. Retry-world state and invalids are unspecified, and the disconnected release prevents implementation or raw-result audit.

`skill-bench` should retain the staged architecture but impose a stricter claim boundary: report AgentTether-like results as **configured evaluator-assisted repair-package effects** until independent diagnosis labels, equal-information controls, attempt/world-state ledgers, proposition-level mediation, collateral outcomes, repeated equivalent cases, and held-out transfer establish the later joins. The most useful next evidence is not another aggregate repair table; it is the diagnosis × intervention factorial that tests whether a correct independently adjudicated diagnosis is actually what makes the repair work.

## Source links

- Immutable abstract: <https://arxiv.org/abs/2607.06273v1>
- Immutable PDF: <https://arxiv.org/pdf/2607.06273v1>
- Immutable source: <https://export.arxiv.org/e-print/2607.06273v1>
- Paper-linked unavailable repository: <https://anonymous.4open.science/r/AgentTether-9416/>
- Local provenance: `data/sources/releases/2607.06273v1-agenttether/provenance.json`
