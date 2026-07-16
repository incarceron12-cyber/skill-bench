# The Compliance Trap: eventful trajectories, but E–P–R does not yet identify a memory-consumption mechanism

## Source and review status

**Deep review of the complete immutable primary source.** I read the full 25-page arXiv v1 paper, including Appendices A–G, and checked definitions, equations, tables, task accounting, controls, and limitations against the preserved PDF/HTML evidence.

- **Paper:** Yixiong Chen, Xinyi Bai, and Alan Yuille, *The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory*, arXiv:2607.10608v1, <https://arxiv.org/abs/2607.10608v1>
- **Version read:** immutable v1, submitted 12 July 2026; metadata contains no withdrawal/retraction notice
- **Local PDF:** `data/papers/pdfs/2607.10608v1-compliance-trap.pdf` (25 pages; SHA-256 `adf8426ba1a9120f62eb2310628803df7a0534da77444e31b7c460ba48f55e05`)
- **Full local text:** `data/papers/text/2607.10608v1-compliance-trap.txt` (SHA-256 `a7507fa9a175ff526da1286be1745b8fb3d42a80931e0edf0867a88e286ce642`)
- **Immutable arXiv HTML:** `data/papers/source/2607.10608v1.html` (SHA-256 `03a97cbe6e330a3f6b5d3ad577e21d7a2738d66a77e46fdbe0fe78ef81e303e1`)
- **Acquisition/release provenance:** `data/sources/releases/2607.10608v1-compliance-trap/provenance.json`

No verified author-owned benchmark, code, task, memory, trajectory, label, or result release was located. The immutable nine-member arXiv source archive contains manuscript and figure sources but omits the paper-named `analysis/gate_annotation_results.json`, all MemTrapBench tasks and memory trios, trajectories, per-trace labels, result rows, and runnable analysis. The paper says release will occur “on acceptance” (Appendix A, p. 14). This is an acquisition-time limit, not proof that no later release will appear.

## Charter fit and decision filter

This review advances charter objectives A–C by testing a general benchmark-design uncertainty: **what evidence is required to trace a delivered prior experience through adoption, changed action, propagation, repair, and realized consequence?** Browser tasks are a methodological test bed, not a scope commitment. The concrete artifact is a claim-bounded audit and retain/repair/test mapping into the existing experience-memory and trajectory contracts. Useful completion means preserving the paper's event-level advance without promoting schedule contrasts, post-treatment subsets, or baseline-action matching into unsupported causal mechanisms.

## One-sentence contribution and assessment

The paper proposes Entry–Propagation–Recovery (E–P–R), compares no-memory trajectories with helpful, conflicting, and same-site irrelevant memories under early, persistent, and late schedules on WebArena and a 231-task synthetic MemTrapBench, and reports that plausible conflicting guidance often changes behavior and sharply lowers success when repeatedly visible.

**Assessment:** This is a valuable move from retrieval and endpoint accuracy toward action-and-consequence traces, but the named phases are mostly schedule or baseline-similarity proxies, the “compliance” subset is selected by a treatment-induced action, recovery is not task-correct-path recovery, and the factorial changes memory identifiability and wording rather than independently toggling Entry and Grounding; v1 therefore supports configured-package sensitivity to authored context, not a three-stage causal mechanism, scale law, safety result, or validated memory controller.

## Research question and strongest defensible claim

The paper asks where injected memory first changes an interactive trajectory, whether that change persists under repeated exposure, and whether the agent returns after harmful divergence. It evaluates Qwen3.5, Gemma-4, and Gemini-3 configurations using BrowserGym AXTree observations and ReAct-like actions, with greedy decoding for open-weight models (§3 and Appendix A, pp. 3–5, 14).

The strongest defensible claim is:

> On the authors' selected WebArena tasks and synthetic long-horizon browser instrument, fixed plausible task-wrong text changes configured agents' actions and outcomes relative to same-task no-memory runs. Persistent visibility is generally more harmful than one early exposure; same-site irrelevant text is near zero on average; and outcome damage is concentrated among traces whose treatment action an uncalibrated judge labels aligned with the wrong recommendation. On MemTrapBench, system-prompt and observation-footer delivery yield similar conflicting-memory endpoint deltas for three open-weight models.

This does **not** establish an independently validated memory-consumption mechanism, causal mediation through the labeled phases, natural prevalence, scale-dependent vulnerability, recovery competence, professional validity, safety, production fitness, or deployment readiness.

## Methodology and system

### 1. Content and schedule interventions

A short text passage is injected as helpful, conflicting, or same-website cross-task control memory. Helpful and conflicting WebArena passages use matched DO/DON'T/NOTE structure and similar length; conflicting passages refer to real UI elements but prescribe a task-wrong strategy. WebArena memories are hand-authored. MemTrapBench tasks and memory trios are drafted by Claude Opus 4.7 from family blueprints and reviewed by hand (§3.3 and Appendix A, pp. 5, 14).

Schedules are:

- **early:** visible only at the first decision;
- **persistent:** visible at every decision;
- **late:** first visible after step 3.

For each task/model cell, the authors retain one no-memory run and memory-condition runs under the same environment seed. Open-weight decoding is greedy; episodes allow 15 actions and 600 seconds. Same-seed pairing is good design, but “differ only when memory injection differs” is stronger than the evidence: mutable browser state, serving kernels, timeouts, provider behavior, and environment realization can still differ, and no repeated determinism audit or raw run ledger is released (Appendix A, p. 14).

### 2. What E–P–R actually measures

The conceptual phases are useful; their operationalizations are not interchangeable with them (paper §3.1 and Appendix B, pp. 4, 15):

| Named phase | v1 operationalization | What is observed | What remains unidentified |
|---|---|---|---|
| Entry | first post-injection action divergence or recommendation-aligned action | treatment changes an emitted action relative to one baseline realization | semantic adoption, decision opportunity, necessity, or why the action changed |
| Propagation | persistent-versus-early endpoint-effect ratio | repeated visibility changes final success more/less than one exposure | whether the first change persisted, repeated independent re-entry, changed state, or simple dose/salience |
| Recovery | later action re-alignment with the no-memory trace; separately final success | some later action resembles a baseline action, and endpoint may/may not pass | return to a task-correct reachable state, repair of irreversible effects, or policy-level recovery |
| Late schedule | memory first appears after step 3 | treatment effect after an authored delay | recovery after known harmful divergence; many runs have not diverged before treatment |

A persistent/early ratio is unstable near zero—the paper suppresses values when `|Δearly| < 2 pp`—and is a ratio of endpoint effects under two treatment packages, not a direct observation that one initial action propagated. Late injection probes history-conditioned treatment sensitivity, not Recovery. The paper itself says MemTrapBench is the more direct recovery readout, but its released-free per-trace measure still uses baseline-like action matching rather than an independently defined correct-state set.

### 3. WebArena task pools and outcome selection

The full pre-check uses 684 non-map WebArena tasks with online-generated memory formats. Effects are small and inconsistent: Qwen3.5-9B changes −1.9 points and Qwen3.5-27B +1.7 under unconditional contrastive memory; quality gating changes these to −2.3 and −1.7 (§4.1, Table 1, p. 6). The online memory generation, retrieval candidates, quality scorer, thresholds, invalids, and exact rows are not released or sufficiently specified for replay.

The main 77-task pool retains tasks whose binary outcome changes among no-memory, early-helpful, or early-conflicting runs on either Qwen model (Appendix A, p. 14). This is explicitly outcome-conditioned selection. It is useful for mechanism scouting but inflates sensitivity and couples selection to two evaluated models. Figure 3 then reports model-specific `n=67–77` or `n=74` without a complete invalid/missing ledger. The paper appropriately warns that absolute effects may be inflated, but claims about general WebArena behavior cannot be based on this pool.

There is also an internal configuration contradiction. The main paper presents Gemini-3-Flash in the WebArena 77 figure/table narrative (§4.2–4.3, pp. 6–7), while Appendix A says Gemini-3-Flash is queried “on MemTrapBench only” (p. 14). Without result rows and configurations, the Gemini WebArena condition cannot be reconciled.

### 4. Recommendation Compliance Rate and Damage Per Compliance

For persistent conflicting memory, Gemini-3-Flash at temperature 0 judges whether the treatment's first action plausibly executes the first primitive of the recommendation, using the memory DO excerpt, baseline first action/start URL, and treatment first action/pre/post URLs. `YES` defines `C_RCR`; `NO` and `UNCLEAR` do not. No human labels, duplicate judgments, agreement, model-swap, prompt perturbation, adversarial cases, or false-positive/false-negative study calibrates this observer (Appendix B, pp. 15–16).

Damage Per Compliance is the paired mean `y_no-memory − y_conflict` among `C_RCR` (§3.2, p. 4). Pairing preserves same-task outcome differences, but it does **not** “remove the selection-bias confound.” `C_RCR` is defined by a post-treatment action and judge comparison with the baseline action. Conditioning on it changes the estimand to damage among observed treatment compliers and can induce selection across task difficulty, baseline strategy, action observability, and model. It is not an all-task causal mediation effect or a common principal stratum across models.

Table 2 reports RCR 63–72% and DPC point estimates from 2.1 to 25.5 points, with intervals excluding zero only for Gemini-3-Flash and Qwen3.5-27B (p. 7). The prose calls the Gemma-E4B endpoint `−2.1` in one place even though the table's paired DPC is `+2.1`; it also describes 63–72% as approximately scale-independent without a model-comparison test. Different compliant task sets (`N=67–77`, `|C|=42–54`) and broad intervals do not establish a shared compliance rate or scale law.

The “stronger agents suffer larger absolute damage” result is therefore conditional and partly arithmetic: when model-specific selected subsets have higher paired baseline success but treatment success falls toward a similar floor, the difference is larger. Baseline capability, compliant subset composition, architecture, and floor are not independently manipulated. Appendix F itself shows the scaling direction reverses across Qwen3.5 and Gemma-3 on the full-distribution early-memory study (Table 26, p. 24).

### 5. MemTrapBench construction and operational realism

MemTrapBench has a 16-task S1 pilot plus 231 main S2–S8 tasks on a shared HTML/JS browser skeleton. The main set spans four diagnostic labels—Decoy, Uptake, Grounding, Override—and seven structural templates. Every task has a goal, plausible decoy, and helpful/conflicting/cross-task memory trio (Appendix D, pp. 17–20).

This is a controlled synthetic mechanism probe, not external validation in the ecological sense. Task, trap, memory, diagnostic label, correct path, and verifier are co-authored from the same blueprint and reviewed by the same study process. The paper reports one no-memory and one persistent-conflicting rollout during construction “to confirm the correct path succeeds and the trap action lies on a wrong path” (§3.3, p. 5), but does not identify the rollout model, acceptance/rejection counts, failed candidates, independent task authors, alternative valid strategies, or verifier audit. This can outcome-select items during construction even if selection is not performed after the headline model sweep.

The tasks are intentionally executable and long (median 15 steps), but they omit professional source packs, human stakeholders, real memory provenance, authority disputes, permissions, artifact acceptance, or downstream use. Shared generated templates induce clustering. The 10,000-resample task bootstrap treats rows as exchangeable and does not report template/site/blueprint-clustered uncertainty.

### 6. Per-trace annotations and recovery

The paper says 4,851 non-baseline traces (3 models × 231 tasks × 7 conditions) are labeled for `adopted@1`, `diverged`, `recovered`, and `success`, and names an unreleased JSON file (Appendix E.1, pp. 19–21). It does not specify whether these labels are deterministic, heuristic, human, or model-judged beyond action-string rules; no label examples, ambiguous-state policy, reliability, or adjudication are provided.

`diverged` is first disagreement in action verb or target browser `bid`; text differences are ignored. `recovered` means later re-alignment with a baseline-like action. Under different reached states, the same action can be invalid or have different consequences; conversely, a legitimate alternate route can remain different and still recover. The baseline itself is not necessarily correct—main-set no-memory success is only 10.8–32.9%. Therefore baseline-action similarity is neither necessary nor sufficient for task-correct recovery.

Table 22 illustrates the construct problem. Persistent conflicting `adopted@1` is only 0.4–7.8%, while WebArena RCR is 63–72%; the paper explains that strategic memory may become actionable later. That means a first-exposed-decision Entry metric misses most purported uptake on this instrument. Meanwhile 45–61% of diverged conflicting traces “recover” at the action level, but only 1.3% succeed. This is strong evidence that the similarity label does not represent repaired consequential state—not that agents possess recovery capability which mysteriously fails to protect outcomes.

A stronger design would freeze the first actual decision opportunity for each proposition, define permissible action/state sets, record the introduced delta and reversibility, then distinguish attempted repair, accepted repair, residual collateral state, and endpoint recovery.

### 7. The 2×2 “causal” probe

The Decoy factorial uses 32 tasks per cell and varies:

- `E+`: one target memory versus `E−`: target plus three sibling conflicting memories, requiring semantic task matching;
- `G+`: original real UI labels versus `G−`: an LLM rewrite replacing labels, color, and position phrases with plausible nonexistent alternatives.

These are useful stress interventions but do not orthogonally toggle Entry and Grounding (Appendix E.2, pp. 20–22). The Entry manipulation jointly changes context length, candidate count, distractor competition, scope ambiguity, and selection burden. The Grounding manipulation changes wording, specificity, plausibility, lexical overlap, and actionability; “zero rewrite-label hits” only establishes literal absence in rendered HTML. Neither manipulation directly observes whether the model adopted the memory.

The reported outcome-scale main effects are substantial for grounding and for Qwen Entry (Table 23, p. 22), but no task-level rows, exact assignment, repeated realizations, multiplicity policy, or clustered model are available. Calling a small additive interaction support for a **multiplicative** E–P–R decomposition is not justified. A product of conditional gate probabilities is largely a chain-rule accounting identity; equating that positive product to a signed success-rate delta additionally requires an effect-magnitude term and explicit conditioning population. The paper reports neither the gate values needed to audit its claim that the product reproduces every WebArena helpful delta nor a mediation analysis.

### 8. Channel and horizon controls

Moving the same persistent memory from system prompt to observation footer changes conflicting deltas by at most 0.5 points for three open-weight models (Tables 5/25, pp. 8, 24). This supports position robustness for **two prompt placements**. It does not support the broader statement that system instruction, tool output, and page content share the same dynamics: no tool-output or environment-page arm is run, and helpful effects change by 4.4–16 points across the two tested placements.

The horizon comparison spans MiniWoB++, selected WebArena, and MemTrapBench. Conflicting damage is small on median-two-step MiniWoB and larger on the longer instruments (Tables 6/27, pp. 9, 25). But benchmark, tasks, baselines, memory generation, environment, action opportunities, and only MiniWoB's three seeds change with horizon. This is a boundary-condition association, not evidence that trajectory length causes propagation. A valid horizon test would truncate/extend matched tasks while preserving the decision and trap.

### 9. Retry-on-fail

Retry-on-fail runs no memory first and, only after observed failure, runs a second full attempt with persistent helpful memory. It can outperform one always-memory attempt on this instrument (Table 29, p. 25). The comparison bundles outcome-oracle access, extra attempts, extra token/time budget, fresh environment/reset semantics, and treatment routing. It is not a within-trajectory Recovery intervention.

The retry-no-memory control is essential but reveals unresolved nondeterminism: despite the paper's claim that greedy same-seed baselines are effectively deterministic, a second no-memory attempt adds 2.0–2.7 points. The prose variously calls this 2–3, 2.6–5.6, and “sampling diversity”; Table 29 reports only 2.0–2.7. Main-set denominators also fall to 211–213 for Qwen3.5-9B and 229 for Gemma despite Appendix D's “zero tasks dropped” accounting and 231-task headline. Missing/invalid/retry eligibility rules are not reconciled.

The result supports a bounded policy hypothesis—failure-conditioned extra compute plus helpful content can beat one uniform exposure—not a deployment recipe, cost-normalized advantage, or recovery mechanism. The paper appropriately labels it diagnostic evidence, but stronger comparisons require equal total attempts/budget, predeclared failure observability, retained invalids, reset identity, and cost/latency accounting.

## Evidence and claim boundaries

### Supported by the manuscript-reported v1 study

1. Fixed task-wrong textual guidance can alter action traces and endpoint success in selected and synthetic browser tasks.
2. Persistent conflicting exposure is more damaging than one early exposure for some configured systems, and is directionally harmful across the main reported MemTrapBench systems.
3. Same-site irrelevant memory has near-zero average endpoint effect in the reported cells, arguing against context length alone.
4. Helpful and conflicting text can have asymmetric endpoint effects, and placement changes helpful effects more than conflicting effects in the tested open-weight systems.
5. Baseline-like action re-alignment and task success disagree sharply, showing that action similarity cannot substitute for consequential state recovery.
6. The synthetic Decoy interventions show endpoint sensitivity to target identifiability and literal UI-reference availability, although the named gate causes remain bundled.
7. Shorter and longer benchmark families show different damage patterns, warranting matched horizon experiments.
8. Failure-conditioned second attempts with helpful content outperform no-memory second attempts in the reported synthetic instrument, at higher opportunity/budget.

### Partially supported

- **Entry:** treatment affects early actions, but opportunity and semantic adoption are not consistently measured.
- **Propagation:** persistent exposure changes outcomes more than early exposure in some cells, but repeated entry, changed state, dose, and true persistence are not separated.
- **Recovery:** final consequences often remain bad after baseline-like actions recur; the similarity measure itself is not validated recovery.
- **Compliance trap:** selected treatment-following traces have large paired damage, but post-treatment selection and observer error limit causal and cross-model interpretation.
- **Content rather than channel:** robust across system-versus-footer placement for conflicting text only; not tested across tool/page/memory-system channels.
- **Stronger-agent conditional damage:** higher-baseline selected subsets can lose more points, but no general scale law or common complier population is identified.

### Not supported

- a validated E–P–R causal mechanism or mediation decomposition;
- scale-independent compliance or stronger-model vulnerability as a general law;
- task-correct recovery capability from baseline-action re-alignment;
- natural prevalence or severity of harmful real memory consumption;
- independent benchmark, memory, label, judge, or verifier validity;
- causal horizon dependence, channel invariance beyond two placements, or cost-effective routing;
- safety, professional knowledge-work capability, production fitness, economic utility, or deployment readiness.

## Relevance to skill-bench

The paper's durable insight is not a scalar “compliance trap.” It is that **post-retrieval evaluation needs an opportunity-conditioned intervention chain with irreversible state consequences**.

## Unique insight

The reusable contribution is the chain itself, with each rung retained independently:

```text
versioned prior experience and authority
→ current-task applicability / admissible role
→ delivered evidence view and schedule
→ first proposition-specific decision opportunity
→ access and interpreted recommendation
→ adoption / rejection / deferral with chosen action
→ induced state delta and reversibility
→ repeated re-entry or propagation through dependencies
→ correction signal and repair opportunity
→ attempted repair and accepted state transition
→ residual/collateral consequence
→ final artifact/state outcome, cost, and bounded claim
```

No link inherits the next. Endpoint damage does not prove adoption; changed action does not prove recommendation use; repeated visibility does not prove propagation; a baseline-like later action does not prove repair; and repair attempt does not erase irreversible state.

This extends adjacent evidence:

- **MemSyco-Bench** types whether history should be ignored, constrained, deferred, superseded, or used, but stops at judged text. Compliance Trap adds chosen browser action and endpoint consequence, while weakening authority and observer validity.
- **Plans Don't Persist** fixes a replay prefix but discards the counterfactual action. Compliance Trap retains freely chosen actions, yet lacks proposition-specific context removal, derived-trace audits, and frozen-prefix action twins.
- **STRACE** distinguishes a surface event from an earliest supported cause. E–P–R event labels should remain observations until dependency evidence or controlled slices support a root cause.
- **ClawArena** supplies temporal supersession and workspace-state consequences, but its feedback and authored truth are confounded. Compliance Trap adds matched memory schedules but has less realistic source authority and no evolving claim state.
- The existing `pilots/experience-memory-transfer/` fixture already records available → accessed → adopted, stale action, harmful transfer, quarantine, retry, and state deltas. This paper's nonduplicate addition is to require **first actual opportunity, repeated re-entry, repair opportunity, accepted repair, residual state, and opportunity-conditioned denominators** in the next empirical exercise—not a new memory subsystem.

## Limitations and validity threats

1. The WebArena 77 pool is selected on outcome changes under two evaluated models.
2. MemTrapBench goals, traps, memories, diagnostic labels, expected paths, and checks share one synthetic authoring lineage.
3. Construction-time rollouts can select executable model-sensitive traps, but the model, candidate pool, and rejection history are absent.
4. E–P–R phase names outrun their proxies: first-action difference, schedule-effect ratio, delayed exposure, and baseline-action re-alignment.
5. The first exposed step is not necessarily the first decision opportunity where strategic memory is actionable.
6. RCR uses one uncalibrated Gemini judge with no human labels, repeats, model swap, agreement, or adversarial audit.
7. DPC conditions on a treatment-induced action/judge label and does not identify an all-task mediation effect or common complier stratum.
8. Model-specific compliant sets, baselines, and sample sizes undermine scale-independent compliance and stronger-agent comparisons.
9. Baseline-action matching is neither necessary nor sufficient for return to a correct reachable state.
10. The unreleased 4,851-trace annotation procedure lacks observer identity, ambiguity rules, reliability, examples, and adjudication.
11. The Entry factorial jointly changes candidate count, context length, distractor competition, scope matching, and identifiability.
12. The Grounding factorial jointly changes literal label availability, wording, specificity, plausibility, lexical overlap, and actionability.
13. Small additive interactions on the success-rate scale do not validate a multiplicative causal gate chain.
14. Single greedy runs dominate; environment/provider nondeterminism is neither repeated nor bounded by a run ledger.
15. Task/template lineage is clustered, but uncertainty resamples tasks as exchangeable and does not report template-clustered estimates.
16. The horizon comparison changes benchmark, task, baseline, memory process, and environment together.
17. The channel comparison tests system prompt versus observation footer only, not tool outputs or page-authored evidence.
18. Retry-on-fail receives a success signal, extra attempt, extra compute, and reset; it is not within-trajectory repair or a matched-budget policy comparison.
19. Missing/invalid accounting is inconsistent with the zero-drop claim, especially retry denominators of 211–229 from a 231-task set.
20. No benchmark, task, memory, prompt, trajectory, label, result, judge-output, or analysis release permits independent replay.
21. Internal report inconsistencies include Gemini WebArena participation, DPC sign prose, no-memory retry magnitude, and deterministic-versus-retry behavior.
22. The domains are synthetic/web-browser interaction; no source authority, represented user, professional artifact, stakeholder acceptance, or downstream operational consequence is validated.

## Transfer to skill-bench: retain, repair, test

### Retain

1. Same-task no-memory/helpful/conflicting/irrelevant pairing with immutable content and schedule identity.
2. Separate behavior-selection rate from conditional consequence, while clearly labeling post-treatment estimands.
3. Full attempted-run accounting and paired task-level uncertainty.
4. Positive-use controls so rejecting all historical guidance cannot pass.
5. Delivery-placement and short-horizon boundary controls.
6. Separate trajectory similarity, state repair, and final outcome.
7. Invalid/missing/service outcomes and all retries as first-class records.

### Repair

1. Define the first **actual proposition-specific opportunity**, not simply step 1 or first exposure.
2. Bind memory to source authority, valid time, task scope, admissible role, and current evidence precedence before calling compliance harmful.
3. Replace single-baseline exact action matching with allowed action/state sets, task-correct invariants, state deltas, and legitimate alternate paths.
4. Record repeated exposure, access, adoption rationale, state mutation, propagation dependency, correction cue, repair action, accepted transition, reversibility, and residual collateral state separately.
5. Calibrate compliance/recovery observers with blinded human or deterministic labels, duplicate ratings, model swaps, abstention, and adversarial alternatives.
6. Estimate all-task intention-to-treat effects separately from treatment-selected complier descriptions; use prospective encouragement or principal-stratum assumptions only when defensible.
7. Cross Entry and Grounding with matched-capacity content variants that do not change candidate count, wording quality, or scope ambiguity together.
8. Cluster by template/source/task lineage, repeat stochastic/provider components, and retain every invalid denominator.
9. Compare policies at matched total attempts, tokens, time, environment resets, and access to outcome signals.
10. Freeze environment and configured-system identities, with canaries for baseline determinism and mutable service state.

### Test before stronger claims

Use the existing experience-memory-transfer pilot machinery on two unlike knowledge-work actions with one reversible and one irreversible consequence. Pre-register matched arms for no memory, authorized helpful, plausible conflicting, irrelevant, stale/superseded, and corrupted memory; cross single versus persistent delivery only after freezing the first decision opportunity. Instrument access, adoption, first action, downstream state, correction availability, repair, residual state, artifact outcome, and cost. Include deterministic negative controls and repeated configured-agent runs. This would test whether E–P–R adds diagnosis beyond existing authority and evidence-to-action records without narrowing the benchmark to web browsing.

## Reproducibility and operational realism

**Conceptual reproducibility is moderate.** The paper states task pools, memory forms, models, serving stack, decoding, schedules, action-divergence rule, RCR evidence view, principal statistics, synthetic families/templates, and several controls. The full appendix is unusually ambitious and exposes outcome selection, task accounting, examples, and boundary probes.

**Result reproducibility is poor.** No tasks, memories, prompts, trajectories, result rows, per-trace labels, code, exact online-retrieval implementation, environment snapshot, seeds, judge outputs, or analysis scripts are released. The paper-named annotation file is absent from the arXiv source archive. Internal contradictions remain unresolved: Gemini WebArena participation; `+2.1` versus `−2.1` DPC prose; deterministic baselines versus retry-no-memory gains; zero dropped tasks versus 211–229 retry denominators; and retry-no-memory magnitude wording. Mutable preview models and web environments further limit replay.

**Operational realism is low to moderate.** Free browser actions, long trajectories, irreversible form/state mistakes, timeouts, controls, and explicit retry policies are closer to agent operation than static QA. Yet the main validating instrument is a shared generated skeleton with co-authored goals, decoys, memories, and expected paths. There are no real experience sources, professional authority, permissions, stakeholders, heterogeneous artifacts, accepted alternatives, or downstream users. The study is a useful internal mechanism probe, not evidence about consequential professional memory use.

## Concrete repository action

No new build task is warranted. The existing experience-memory-transfer, information-flow, source-authority, longitudinal stream, trace, artifact/state consequence, task-health, metric, validity, and execution contracts already provide implementation homes. A duplicate E–P–R schema would add labels without evidence. The next nonduplicate action is empirical: add opportunity/adoption/repair/residual-state observations when the existing cross-domain memory pilot is next exercised with real or independently reviewed scenarios.

## Bottom line

*The Compliance Trap* correctly moves attention downstream of retrieval and demonstrates that plausible prior guidance can change actions and harm outcomes in long synthetic browser trajectories. Its own evidence also shows why the phase labels must be treated cautiously. Entry is often first-action difference rather than semantic uptake; Propagation is a persistent/early endpoint ratio; late exposure is not Recovery; and “recovered” baseline-like actions coexist with almost universal failure. The post-treatment compliance subset, bundled factorial, outcome-selected WebArena pool, generated benchmark, uncalibrated judge, single-run cells, and absent release prevent mechanism, scale, safety, or readiness claims. For `skill-bench`, retain the eventful trajectory and repair it into an authority-aware, opportunity-conditioned chain from delivered experience through adoption, state change, repair opportunity, accepted correction, residual consequence, and cost.