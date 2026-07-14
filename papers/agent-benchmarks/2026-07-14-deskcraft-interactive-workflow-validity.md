# DeskCraft: an authored interaction channel is not yet evidence of proactive human collaboration

## Source and review status

**Deep review of the complete immutable primary source and the official release.** I read the full 42-page arXiv v1 paper and checked claims against the preserved PDF and TeX source. I also audited both identifiable official-release boundaries. The newest public commit at or before v1 submission contains only `LICENSE`; the inspectable benchmark snapshot is 30 days post-v1 and explicitly includes later task repair/QC work. Release observations therefore cannot establish the exact task bytes, runner, or results used in the paper.

- **Paper:** Wenkai Wang et al., *DeskCraft: Benchmarking Desktop Agents on Professional Workflows and Human-in-the-Loop Collaboration*, arXiv:2606.03103v1, https://arxiv.org/abs/2606.03103v1
- **Date read:** 2026-07-14
- **Local PDF:** `data/papers/pdfs/2606.03103v1-deskcraft.pdf` (42 pages; SHA-256 `e7b390d33675f360a286e6da97ad58c6027998343aab1875fee888e8f61e72f2`)
- **Full text:** `data/papers/text/2606.03103v1-deskcraft.txt` (SHA-256 `c8cb643d482d4e5071dd23e69dab37f53e15e8a3d97b3232bb9d604723f61151`)
- **Immutable TeX source:** `data/papers/source/2606.03103v1-source.tar.gz` (SHA-256 `5dad0df8e2dc71571af062cb7db73ebe9d2974267688299dacc7e0588dab10f1`)
- **Release provenance:** `data/sources/releases/2606.03103v1-deskcraft/provenance.json`
- **Paper-time release:** commit `6e458067e22e00ef03ff4c27d98cf4c1cf6333e0`; only `LICENSE`
- **Audited later release:** commit `923f87955ad067ffbcc9c1f05bf8cfd9c3a1b714`, 2 July 2026, 30 days after v1; all 538 task packages parse, but no trajectories, model outputs, simulator judgments, result tables, or analysis corpus are released
- **Tags:** desktop-agents, interactive-evaluation, professional-artifacts, user-simulation, long-horizon-workflows, mixed-initiative-validity

## One-sentence contribution

DeskCraft contributes a broad executable desktop package—538 task records across office, browser, development, design, multimedia, 3D, OS, and multi-application work, including 152 phased interactive tasks—but its most transferable lesson is a validity boundary: exposing a prompted clarification tool and injecting authored goals at fixed trigger points measures endpoint completion under a simulator-mediated protocol, not proactive collaboration, human authority, professional artifact quality, or the causal value of interaction.

## Why this matters for skill-bench

DeskCraft advances charter objectives A and B by putting three desirable benchmark properties in one instrument: native professional artifacts, extended desktop state, and task requirements that arrive over time. It also shows why these ingredients must remain separately observable.

The benchmark's headline construct can be decomposed as:

```text
authored interaction opportunity
→ trigger realization
→ simulator utterance
→ agent receipt
→ semantic adoption or justified rejection
→ state-preserving plan repair
→ endpoint/artifact change
→ recipient acceptance and burden
→ downstream consequence
```

DeskCraft directly specifies the first three links and deterministically grades selected endpoint properties. It does not separately score the middle links, observe a real participant, establish participant authority, measure burden, or observe recipient use and consequence. This is not a reason to reject simulated interaction. It is a reason to call the construct **configured-agent performance under an authored phase protocol** and to retain stronger claims for later validation.

## Research question and defensible claim boundary

The paper asks how current GUI agents perform on professional desktop workflows under standard and interactive settings, whether a 300-step budget recovers success, how performance changes across L1/L2/L3, and how agents handle six authored collaboration-mode labels (Section 5, pp. 6–8).

The strongest defensible claim is:

> On the authors' reported one-attempt 386-record standard and 152-record interactive packages, selected configured model/runner systems achieved low deterministic endpoint success; one Kimi-K2.6 run continued to gain a small number of successes after 100 actions; and two frontier systems had different endpoint rates across authored interaction-mode subsets, with the lowest reported rates on the subset labeled clarification.

The evidence does **not** establish that:

- standard-versus-interactive score differences estimate an interaction effect, because the task sets and application distributions differ and there is no matched no-interaction ablation;
- clarification was necessary, timely, useful, semantically adopted, or lower-burden rather than merely available and evaluator-cued;
- the simulator behaves like a human, has the authority of the intended user, or preserves human preferences under uncertainty;
- the six mode labels identify causal interaction mechanisms rather than overlapping authored scenario categories;
- L3 is a calibrated long-horizon class requiring more than 50 environment actions;
- endpoint checks establish visual quality, document coherence, professional acceptability, preservation, safety, or recipient utility;
- 18 model rows are comparable agent effects rather than configured model–adapter–prompt–action-policy packages;
- reported rates are stable under repeat runs, environment failures, simulator sampling, task clustering, or release repair;
- DeskCraft demonstrates human collaboration, occupational representativeness, professional validity, capability, safety, production fitness, or readiness.

## Methodology and system

### Task frame, applications, and difficulty

The paper reports 538 records: 386 standard and 152 interactive, spanning 11 named applications plus a multi-app category and five broad domains (Figure 1 and Table 2, pp. 2 and 7). The later release contains exactly 538 parseable task JSON packages and the same 386/152 split. It contains 126 L1, 147 L2, and 113 L3 standard records (Appendix Table 10, p. 18). This conflicts with Figure 1's 141 L1, 137 L2, and 108 L3 counts (p. 2), although both sum to 386.

L1 isolates one atomic operation; L2 composes two to four related operations; L3 pursues a high-level objective through dependent subtasks and often multiple deliverables (Section 3.2, p. 4; Appendix F.3, pp. 18–19). This is a useful authoring taxonomy, not a validated difficulty scale. The abstract and Figure 1 associate L3 with “over 50 execution steps,” but construction uses workflow form rather than a demonstrated minimum action path. Reported successful L3 runs can average below 50 in some model/application cells, and no reference-action counts, independent difficulty ratings, item-response analysis, or controlled within-task complexity transformations are supplied.

The sourcing evidence is mixed (Appendix Table 8, p. 17): 204 standard records come from official documentation, 105 are author-designed, 29 from tutorials, 20 from web-development resources, and 28 mixed/unlabeled. Documentation establishes that software operations exist; it does not establish occupational frequency, workflow importance, artifact convention, or professional acceptance. “Practitioners” draft domain verification strategies (Section 4.2, p. 5), while Appendix J says practitioner-seeded workflows were abstracted with consent (p. 42), but the paper gives no practitioner count, roles, qualifications, selection, contribution units, approval scope, disagreement, time, compensation, or task-level lineage.

### Interactive task construction

An interactive task contains two to four phases: the later release has 60 two-phase, 85 three-phase, and seven four-phase records, totaling 403 phase messages, matching the paper's aggregate (p. 6). Each phase has an authored instruction and one of three paper-level triggers:

- `agent_done`: inject after the agent signals completion;
- `agent_asks`: respond after a dedicated clarification call;
- `step_count`: inject after a fixed execution threshold.

The audited later release has `agent_done` in all 152 tasks (308 occurrences), `step_count` in 64 tasks (64 occurrences), and `agent_asks` in 31 tasks (31 occurrences). Step thresholds are overwhelmingly three: 52 of 64, with seven at two, two at four, and three at five. Thus “interruption” is mostly a very early fixed intervention, not an observation that a meaningful subtask boundary, risky action, or user-relevant state has been reached. The paper's own successful Kdenlive case says the original plan was “effectively superseded before substantial editing begins” when the update arrived at step 3 (pp. 38). That case demonstrates retargeting after an early scripted update, not preservation and repair of substantial completed work.

The paper assigns one primary collaboration label per task for non-overlapping analysis, while allowing secondary labels (Appendix C, p. 12). It reports 50 progressive-refinement, 32 ambiguity/clarification, 25 requirement-change, 21 interruption, 17 correction/feedback, and seven multi-step-workflow tasks. Yet the text immediately says “91 of 170 tasks” have a secondary label, contradicting the 152-record interactive frame. The later release has no `primary_collaboration_mode` field; scenario labels are heterogeneous (`ambiguous_instruction`, `ambiguous_scope`, `ambiguous_target`, `ambiguous_detail`, `interruption`, `task_interruption`, `correction`, `error_correction`, and 25 missing `scenario_type` values). The analysis labels and released task fields therefore cannot be joined directly without an absent mapping.

### User simulator and participant realization

The paper says Kimi-K2.5 is the fixed user-simulator backbone (Section 5.1, p. 6). The simulator receives scenario description, persona, authored current and optional next goals, recent conversation, agent reply, and current screenshot; it emits a natural-language message plus phase-completion status (Appendix B, pp. 11–12). This improves reproducibility relative to unconstrained chat because goals and trigger positions are authored.

It is not deterministic participant behavior. The paper does not report endpoint snapshot, temperature, seed, retry, malformed-output rate, fallback rate, or repeated simulator calls. The later implementation defaults to temperature `0.7`, sends screenshot and history to an external API, and falls back to restating the current instruction after errors (`mm_agents/user_simulator.py`, lines 87–111 and 285–310 in audited commit). The paper's phrase “ensuring deterministic user interaction without trajectory drift” (Section 3.3, p. 5) is therefore stronger than the specified evidence. At best, the **goal sequence and trigger policy** are constrained; utterance, screenshot judgment, and API realization may vary.

The simulator is also not an independent participant. It is instructed not to invent requests, to naturally express the authored next phase, and—when an expected clarification occurs—to answer the agent directly and mark the phase complete (Appendix B, pp. 11–12). “Feedback” and “correction” can therefore be authored next-goal delivery rather than a response caused by detecting the agent's actual mistake. The only final outcome observer is the deterministic endpoint evaluator. No human reviews simulator fidelity, message usefulness, authority, frustration, interruption timing, over-questioning, ignored advice, or retained control.

### Prompt treatment and proactive clarification

For tasks containing an `agent_asks` phase, the runtime enables a dedicated `call_user` action and appends explicit guidance: if the instruction is ambiguous or missing details, call the tool and do not pretend the user answered (Appendix A, pp. 11–12). The audited later runner enables this prompt only when a task contains an `agent_asks` trigger (`lib_run_interactive.py`, lines 337–343). The simulator treats `CALL_USER` as a universal intervention signal, but agents on non-ask tasks may not receive the tool/prompt.

This creates a central identification problem:

```text
ask-labeled task content
+ deliberately withheld answer-bearing requirements
+ extra action channel
+ explicit prompt to ask
+ simulator response policy
+ endpoint execution difficulty
→ one binary endpoint score
```

Figure 8's “Ask” rate cannot isolate proactive uncertainty recognition. If the agent does not call, it may never receive requirements needed for endpoint success; if it calls, the score still depends on parser success, simulator wording, context injection, downstream execution, and grader behavior. The paper does not report call rate, precision, recall against independently necessary questions, question timing, question quality, response adoption, redundant calls, burden, or endpoint change conditional on calling. Exposing the channel and seeing low endpoint success supports “this configured package is hard,” not the stated mechanism that agents “rarely seek clarification proactively” (pp. 8–9).

A valid proactive-clarification study needs at least matched task versions and typed observations: missing-information necessity, ask opportunity, tool availability, call occurrence, question relevance, simulator/human answer, semantic incorporation, state transition, endpoint effect, and burden. DeskCraft currently collapses these.

### Execution, stopping, and state carryover

Each agent observes screenshots and selects GUI actions or `DONE`, `ASK`, and `FAIL`; episodes end on completion/failure or budget, while `ASK` does not terminate (Section 3.1, pp. 3–4). The later release preserves GUI state across phases and removes/clears terminal state when more phases remain. This is valuable: updates are not separate reset episodes.

However, the paper does not fully specify runner-specific terminal semantics, action batching, invalid model output, environment setup failure, VM drift, retry, timeout, or exclusion. The later code has distinct generic, GPT-5.4, and Kimi interactive loops. It increments `step_idx` for environment actions but passes `turn_idx` to `should_intervene`; the later `step_count` trigger is therefore a **model-turn threshold**, not necessarily an environment-action threshold (`lib_run_interactive.py`, lines 42–55, 83–93, and 390–411). That diverges from the paper and documentation's execution-step wording whenever a turn emits zero or multiple actions.

For `agent_done` and `step_count`, the later runner advances the authored phase *before* asking the simulator to generate the next message, independently of whether the previous endpoint is complete. This matches the paper's statement that the protocol advances even if the prior phase is unfinished, while the MLLM assesses it (p. 5), but it means phase progression is a benchmark schedule, not participant acceptance. Final endpoint state may preserve requirements across phases; the protocol does not separately score whether each handoff was timely, accepted, or correctly understood.

### Artifact and endpoint evaluation

DeskCraft's strongest engineering choice is native-state inspection. Evaluators parse SVG XML, office formats, Kdenlive XML and media metadata, Audacity waveform/project state, Blender scene graphs, browser databases/tabs, source bundles, tests, and OS configuration (Section 3.4, p. 5; Appendix F.4, pp. 19–20). L3 tasks often require both reusable project and exported deliverable. This is substantially better than screenshot-only success.

The construction procedure also exposes a construct tradeoff. Tasks were retained only when final artifacts could be checked programmatically; prompts requiring manual visual judgment were rejected, and subjective appearance was translated into canvas size, required text, layer names, asset references, slide counts, signal properties, or similar constraints (Appendix F.7, p. 20). That supports structural and functional conformance. It does not establish creative quality, coherence, appropriateness, accessibility, professional convention, preservation of unmentioned state, or recipient acceptance.

The paper sometimes crosses this boundary. The GIMP success analysis says the poster composition is correct “at the visual level” and “looks structurally correct” (p. 32), but no human or image-quality protocol is reported. The Kdenlive interactive case calls a workaround-heavy minimal output a “convincing interactive success” because its files and geometry satisfy revised endpoint requirements (p. 38). Those are author interpretations of selected examples, not measured visual/professional judgments.

### Configured agents, budgets, repetitions, and costs

Table 2 reports 18 named model configurations: three proprietary frontier models, seven open-source generalist VLMs, and eight GUI-specialized systems (pp. 6–7). They are not isolated models. Each row includes model, runner/adapter, prompt, action representation, coordinate handling, tool affordances, parsing, context policy, and environment interaction. The paper does not freeze complete prompts and adapter hashes, endpoint dates, decoding, seeds, hardware, retries, invalid-call handling, or rate failures for all rows.

The main table is presented as one task-level success rate per record. No confidence intervals or task/application-clustered uncertainty are reported. Repeated Kimi-K2.6 results use a “representative task subset,” but subset size, selection, strata, exact repeats, seeds, environment resets, simulator sampling, and dependence are absent (Figure 5, p. 7). `pass@k` and all-k success describe that undisclosed subset, not full-benchmark reliability.

The 300-step analysis is one Kimi-K2.6 run. It reports 13 additional successful tasks after 100 actions and none after 200, but gives no matched repetition or failure disposition (Figure 6, p. 7). Longer trajectories are also observationally associated with L3; task family, application, model, success, and budget censoring are confounded. The evidence does not show that length causes failure or that 100 is an optimal benchmark budget.

No model-token, simulator-token, VM, wall-clock, API, or human-review cost is reported. This is especially important because interactive evaluation adds a second model and screenshot payloads, while the public guide recommends paid cloud VMs and optional paid residential proxies.

## Evidence and results interpretation

### Main results

The paper reports Kimi-K2.6 at 33.8% on the 386 standard records and GPT-5.4 at 27.6% on the 152 interactive records; GPT-5.4 scores 31.6% standard and Kimi-K2.6 25.7% interactive (Table 2, p. 7). Open systems are generally lower. These are bounded endpoint rates on two different record sets. They cannot show that interaction lowers performance, because standard and interactive tasks are not matched and application/domain composition differs.

For standard tasks, GPT-5.4 declines from 39.0% L1 to 40.7% L2 to 9.5% L3, while Kimi-K2.6 reports 41.7%, 41.0%, and 21.6% (Appendix Table 4, p. 13). The L3 cliff is descriptive evidence that the authored L3 package is harder for these configurations. It does not isolate long-horizon planning from application mix, number/type of checks, artifact multiplicity, instruction content, or professional-domain knowledge.

Figure 8 reports endpoint rates by primary interaction label for only Kimi-K2.6 and GPT-5.4. Correction is highest; Ask is lowest. The groups contain as few as seven and at most 50 tasks, overlap in secondary labels, and have no uncertainty or matched content. “Explicit feedback is easier than interruption” and “agents rarely ask proactively” are hypotheses consistent with the figure, not identified mechanisms.

### Release audit and empirical correspondence

The current official archive is useful but cannot reproduce v1 results:

- the public paper-time tree contains only `LICENSE`;
- the later 30-day snapshot contains task packages, assets, evaluators, runners, prompts, and documentation;
- it contains no run-level trajectories, model outputs, simulator messages/judgments, result corpus, or analysis tables;
- its latest commit explicitly adds task loader, VM proxy support, and QC/repair tooling;
- two Calc IDs occur twice, once under L1 and once under L2, with identical ID and instruction: `f7c9725b-9f02-4131-a007-68de65161a3c` and `fb0f694e-fc10-46f9-9fcd-169630844996`.

Thus the later snapshot has 538 records but only 536 unique IDs; the standard split has 386 records but at most 384 unique IDs. Because this snapshot postdates v1, this does not prove paper-time duplication. It does show that record count, unique task identity, difficulty strata, and aggregate denominator need versioned release validation before reuse. It also makes the Figure 1 versus Appendix difficulty-count conflict operationally important.

The paper's appendices say average-step tables were computed from `results/summary_json_collection/non_interactive` (pp. 14–16), but that directory is absent from the archived release. Selected screenshots and narrative case analyses are embedded in the paper; their underlying traces cannot be audited.

### Supported, partial, and unsupported claims

**Supported by manuscript plus later-release structure:** a broad native-artifact desktop task package can encode phased requirements and deterministic endpoint checks; 152 current task packages contain authored multi-phase protocols; native file/runtime checks cover more state than screenshots; reported configured systems have low endpoint agreement; selected runs continue beyond 100 actions; task and interaction categories expose useful diagnostic hypotheses.

**Partially supported:** workflows draw on documentation, tutorials, author design, and unspecified practitioner seeds, but occupational/professional lineage is thin; L3 is structurally more complex but not a calibrated required-action scale; scripted phases improve control but simulator realization is not demonstrated deterministic; final-state conjunction can test retention but does not diagnose semantic adoption; selected case narratives suggest repair behavior but traces are unreleased.

**Unsupported:** causal interaction benefit or penalty; proactive clarification rate or quality; simulator-to-human fidelity; human participation or retained authority; correction, interruption, or ask mechanism effects; professional artifact quality; occupational representativeness; stable 18-agent ranking; reproducibility of reported tables; capability, safety, production fitness, or readiness.

## Unique insight

DeskCraft's deepest transferable insight is that **interaction availability, interaction use, interaction utility, and interaction legitimacy are different measurements**.

A phased simulator can prove:

```text
under this authored trigger schedule,
this configured agent received this additional message,
and the final observable state did or did not satisfy these checks
```

It cannot by itself prove:

```text
the information was genuinely missing
→ the agent recognized uncertainty without evaluator cues
→ the question was necessary and well timed
→ the respondent had authority and supplied a valid preference
→ the agent semantically adopted or appropriately rejected it
→ prior correct work was preserved and the plan repaired
→ the interaction improved the artifact enough to justify user burden
→ a real recipient accepted or benefited from the result
```

This yields six cross-domain design rules:

1. **Treat participant realization as a configured component.** Record human/simulator identity, authority, evidence view, policy, prompt, model snapshot, sampling, fallback, and availability independently from the agent.
2. **Separate offered, exercised, useful, and burdensome interaction.** A tool flag is not a call; a call is not a good question; an answer is not adoption; endpoint success is not net collaboration value.
3. **Counterfactually validate necessity.** Withhold only information whose absence is independently shown to change a legitimate decision, and use matched full-information, no-channel, scripted-channel, simulator, and—where feasible—human conditions.
4. **Trigger on meaningful state, not only clocks.** Fixed early step/turn triggers are reproducible but may miss the intended construct. Bind interventions to inspected state, decision boundary, risk, or completed subtask, and preserve a fixed sentinel arm for comparison.
5. **Grade transition and preservation separately from endpoint.** Observe pre-update valid state, supersession semantics, retained requirements, changed loci, protected state, repair path, final artifact, and causal effect.
6. **Keep structural conformance below professional acceptance.** Native parsers are excellent deterministic observers, but creative/professional quality, coherence, usability, and recipient uptake require calibrated plural grading.

## Limitations and validity threats

1. The 538 frame is a designed corpus without an occupational task population, inclusion probabilities, frequency/consequence weights, or coverage audit.
2. Applications, task families, assets, evaluators, and templates create dependence, but uncertainty is not clustered.
3. Standard and interactive splits are disjoint and differently distributed; their rates do not estimate an interaction effect.
4. Figure 1's L1/L2/L3 counts conflict with Appendix Table 10 and the later release.
5. L3's “over 50 steps” language is not enforced by a released reference path or validated scale.
6. Documentation-derived operations establish software affordances, not professional workflow prevalence or legitimacy.
7. Practitioner count, qualifications, authority, task allocation, review, disagreement, consent scope, and time are absent.
8. The six collaboration labels overlap and have no reported labeling protocol, rater agreement, or released primary-label mapping.
9. Appendix C incorrectly refers to 170 interactive tasks.
10. Only 31 later-release tasks contain `agent_asks`, while the paper analyzes 32 primary clarification records and 34 any-label records; treatment and category differ.
11. Ask tasks receive an extra action channel and explicit prompting, confounding task content, affordance, and evaluator cues.
12. No ask occurrence, timing, relevance, precision/recall, adoption, redundancy, or burden metric is reported.
13. Withheld answer-bearing requirements make ask failure inseparable from downstream execution failure.
14. The simulator is an authored-goal renderer, not an independent human participant.
15. Kimi-K2.5 endpoint, prompt hash, temperature, seed, retries, invalid-output rate, and fallback rate are not reported.
16. The later simulator defaults to temperature .7, contradicting a strong interpretation of deterministic interaction.
17. Screenshot-based phase completion has no calibrated accuracy or evidence-sufficiency study.
18. Fixed step triggers are predominantly at turn 3 and can fire before meaningful work exists to preserve or repair.
19. The later code passes turn count to the trigger while documentation/paper describe execution steps.
20. Phase advancement is scheduled even when prior work is incomplete; it is not user acceptance.
21. Authored correction/feedback may not be contingent on the agent's actual error.
22. No matched simulator-versus-human or alternative-simulator study supports participant fidelity.
23. No authority, consent, refusal, escalation, safety, or prohibited-action semantics are modeled.
24. Final binary state collapses trigger, message, adoption, repair, execution, save/export, and grader failure.
25. Evaluator feasibility selects tasks and excludes subjective visual judgment, narrowing the measured construct.
26. Structural checks do not establish creative quality, coherence, accessibility, preservation, or professional acceptance.
27. Selected narrative cases make visual and interactive-quality judgments without a reported human protocol.
28. Runner, prompt, action-space, parser, and model differences confound the 18 rows.
29. Complete configured-system hashes, endpoint dates, decoding, seeds, retries, invalid handling, and hardware are absent.
30. Repeated-run subset size and selection are absent; `pass@k` does not license full-suite reliability.
31. No confidence intervals, sensitivity analyses, or dependence-aware comparisons are reported.
32. The 300-step result is one configured run and does not identify the causal effect of budget.
33. Invalid environment, setup failure, VM drift, timeout, exclusion, and retry denominators are not reported.
34. Token, API, simulator, VM, wall-clock, proxy, and human-review costs are absent.
35. The exact paper-time empirical implementation is not public.
36. The later release has no trajectories, simulator judgments, outputs, result tables, or analysis corpus.
37. The later release has two duplicate Calc IDs and only 536 unique IDs across 538 records.
38. Post-v1 QC/repair means current task bytes cannot be silently joined to v1 scores.
39. No evidence supports human collaboration, occupational representativeness, professional validity, capability, safety, production fitness, or readiness.

## Reproducibility and operational realism

**Reproducibility is moderate for current task structure and low for v1 empirical claims.** The immutable paper/source preserve formulas, aggregate tables, prompt templates, and selected cases. The later release is unusually substantial: task JSON, assets, evaluators, runners, simulator code, agent adapters, and a VM image link. It supports static package audit and potentially a new evaluation. It does not reproduce v1 because the paper-time public tree is empty of implementation, the current snapshot is post-repair, and trajectories/results/configuration records are absent. A new run would be evidence about the later package and the reuser's configured systems, not a reproduction unless correspondence is established.

**Operational realism is high at the desktop-state and artifact-variety layer, moderate at workflow sequencing, and low at participation/authority/consequence layers.** Native projects, exports, browser state, source bundles, and cross-app handoffs are valuable. Long actions in live applications expose genuine state-tracking and recovery demands. But task frequency and professional authority are not established; interaction is an authored simulator protocol; subjective quality is excluded; and no recipient, organizational handoff, burden, safety, or consequence is observed.

## Comparison with adjacent evidence

- **Workflow-GYM** focuses on professional state-transition validity and task derivation; DeskCraft broadens application/artifact variety and adds phased messages, but neither native state nor source resemblance alone establishes occupational or professional validity.
- **HAS-Bench** makes configurable participant graphs explicit; DeskCraft provides a more concrete desktop interaction loop but repeats the same boundary: simulator identity and graph/channel availability are treatment components, not identified human participation.
- **UnderSpecBench** separates underspecification from action authority. DeskCraft's ask tasks withhold requirements but do not independently establish that asking is necessary, which questions are acceptable, or when abstention/action is authorized.
- **Ambig-DS** emphasizes task-framing ambiguity and rubric leakage. DeskCraft explicitly prompts selected agents to ask, so proactive clarification and evaluator-cue compliance remain confounded without matched disclosure conditions.
- **SovereignPA-Bench** foregrounds consent and mediation. DeskCraft has no refusal, revocation, mandate, or participant-retained authority layer; its simulator always serves authored benchmark goals.
- **Existing artifact-transition machinery** in skill-bench can already represent pre/post views, preservation, changed loci, and admissibility. DeskCraft implies an interaction-episode linkage across those records, not a desktop-specific subsystem.

## Transfer to skill-bench

### Preserve

1. **Native artifact observers:** inspect structured project state and exported deliverables, not screenshots alone.
2. **Phase-conditioned tasks:** allow requirements to clarify, supersede, interrupt, and extend while preserving desktop/artifact state.
3. **Composable trigger records:** distinguish agent inquiry, participant interruption, and post-completion revision.
4. **Reusable plus delivered artifacts:** grade editable source and exported output separately.
5. **Long-budget diagnostics:** record when valid completion occurs rather than treating one short cutoff as capability truth.
6. **Selected recovery traces:** retain examples where agents switch control channels or verify exports, but label them qualitative until sampling/adjudication is specified.

### Repair

1. **Create an interaction-episode record, not a new benchmark family.** Bind trigger policy/realization, participant/simulator identity and authority, evidence view, message, agent receipt, semantic disposition, changed plan/state, endpoint effect, burden, and claim ceiling.
2. **Separate trigger clock from trigger meaning.** Store environment action, model turn, wall time, inspected state, subtask boundary, risk signal, and authored schedule independently.
3. **Use matched interaction ablations.** Full information; missing information/no channel; missing information/scripted answer; simulator answer; and consented human answer where justified. Keep task, grader, environment, and budgets fixed.
4. **Score ask behavior plurally.** Necessity, occurrence, timing, question relevance/specificity, answer authority, adoption, repeat burden, endpoint change, and avoided harm.
5. **Observe state preservation and repair.** Snapshot pre-update satisfied requirements, supersession links, retained constraints, invalidated work, changed loci, recovery actions, final state, and collateral changes.
6. **Add recipient/professional grading only where licensed.** Structural deterministic checks remain one layer; calibrated experts or users assess coherence, visual quality, usability, and acceptance with explicit evidence views.
7. **Fail closed on simulator and environment validity.** Record model/prompt/temperature/seed, malformed/fallback outcomes, VM/setup/retry state, and exclude invalid episodes from capability denominators without erasing them.
8. **Version unique task identity.** Separate record count, unique task ID, task family, phase variant, and release version; reject duplicate IDs across difficulty strata.
9. **Estimate cost and dependence.** Report agent and simulator calls/tokens, VM/wall time, human burden, task-family/application clusters, repeated runs, and uncertainty.
10. **Maintain the claim ceiling.** Passing a phased desktop package supports bounded endpoint conformance under a configured interaction protocol—not human collaboration or professional readiness.

## Concrete repository actions

1. **Add one bounded consolidation task** to integrate an interaction-evidence ladder into `docs/research-synthesis-index.md` and `docs/benchmark-design-taxonomy.md`: offered → exercised → answered → adopted/rejected → state repaired/preserved → endpoint effect → burden → recipient/consequence. Reconcile Workflow-GYM, HAS-Bench, UnderSpecBench, Ambig-DS, SovereignPA-Bench, participation/authority, trace, artifact-transition, metric, task-health, and validity guidance. Do not add a DeskCraft-specific schema.
2. **Do not ingest the later 538 packages as v1 empirical evidence.** If reused, freeze commit `923f879...`, reject or resolve duplicate IDs, label it post-v1, run setup/evaluator canaries, and treat resulting trials as a new package version.
3. **For a future interactive pilot**, use a small cross-domain matched matrix and preserve all intermediate observations before adding another large task corpus. Useful completion is identification of ask necessity, semantic adoption, state-preserving repair, endpoint effect, and burden—not merely a higher binary endpoint rate.

## Action items

- [x] Read the complete immutable 42-page v1 PDF/text and verify claims against TeX/source.
- [x] Audit the only paper-time public commit and preserve that it contains only `LICENSE`.
- [x] Audit all 538 parseable task packages in the 30-day-post-v1 release.
- [x] Reconstruct task frame, difficulty, sourcing, interaction phases/triggers, simulator, endpoint evaluation, configured systems, results, repeated-run and budget analyses.
- [x] Verify 403 phases, 31 ask-trigger tasks, 64 step-trigger tasks, dominant threshold of three, and two duplicate Calc IDs.
- [x] Separate interaction availability, use, utility, authority, burden, endpoint quality, and consequence.
- [x] Map implications into existing cross-domain machinery without proposing a desktop-specific subsystem.
- [ ] Consolidate the bounded interaction-evidence ladder into canonical synthesis.
