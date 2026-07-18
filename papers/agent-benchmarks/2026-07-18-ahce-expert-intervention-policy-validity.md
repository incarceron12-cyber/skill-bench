# AHCE: an endpoint gain from a human-coupled package is not learned expert-reasoning transfer

## Bottom line

Wang, He, and Lu offer a useful systems hypothesis: an agent facing a process impasse may benefit more from a small, context-specific human interaction than from an attempt to preload every domain rule. AHCE also separates a timeout/failure trigger, an interactive query-and-synthesis model, and plan/control execution. Ten people with prior Minecraft experience reportedly complete all 15 tasks, giving the study a real-human substrate absent from simulator-only collaboration work.

The evidence does not identify the paper's stronger mechanism. The Problem Identification Module is not learned: it asks after a fixed number of consecutive timeout-defined failures. The Human Feedback Module is said to be trained with GRPO on MuSiQue, but v1 supplies no reward definition, training instances, tool responses, prompts, hyperparameters, checkpoint, or training results. The main comparison changes human access, query policy, synthesis model, planner context, and predefined execution maneuvers together. There is no no-RL HFM, fixed-query policy, direct-answer-through-the-same-QEM arm, equal-transcript arm, or contribution replay. Thus `64% → 96%` and `10% → 82%` are configured-package contrasts, not isolated evidence that a learned policy acquired expert reasoning or that synthesis caused the gain.

The headline magnitudes are also mislabeled. They are **percentage-point changes**: medium rises 32 points, which is a 50% relative increase; hard rises 72 points, which is a 720% relative increase. “Nearly 70%” appears to round the hard percentage-point change, not report a relative change. The closer hard-task HFM contrast is `68% → 82%` against AHCE-log: 14 points, or 20.6% relative. No uncertainty, participant/task/world clustering, assignment ledger, or raw trials are reported.

“Minimal intervention” is supported only by a narrow active-time ratio. For the strongest hard condition, the table reports 79.4 human seconds over 1,265.6 total seconds, whose ratio is 6.27% and explains the displayed 6.3%. The paper does not report request opportunities, number of requests or turns, failed requests, waiting time, repeat contacts, intervention availability, participant preparation, or total expert labor. A small ratio can result from a large agent-time denominator; 79.4 active seconds per hard trial is not zero burden.

The strongest warranted claim is therefore:

> Under the paper's unreleased MineDojo/MP5-core implementation and reported aggregation, a Qwen-planned, vision-controlled package coupled to Minecraft-experienced participants through a Qwen-based interactive HFM and predefined QEM actions achieved higher task-level success and lower recorded active human time than the authors' autonomous and log-sharing packages on 15 curated Minecraft tasks.

This does **not** establish tacit-expertise transfer, participant expertise beyond prior game experience, optimal intervention timing, HFM mechanism causality, human substitution, professional validity, cross-domain transport, reliability, net value, or readiness.

## Source and reading record

### Complete immutable primary source read

- Zhiming Wang, Jinwei He, and Feng Lu, *Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention*.
- Immutable arXiv v1: <https://arxiv.org/abs/2602.22546v1>, submitted 26 February 2026.
- Local PDF: `data/papers/pdfs/2602.22546v1-requesting-expert-reasoning-ahce.pdf` (10 pages; 1,654,679 bytes; SHA-256 `5fe72aa300565593027a67abe3f29fb9ca2675d2e4f17bf532663a729b6ef4db`).
- Local full text: `data/papers/text/2602.22546v1-requesting-expert-reasoning-ahce.txt` (SHA-256 `43e2a2038d6b54442027bef88d3887b58ae72ae9983c2b301d5ec7f294119ac2`).
- Official TeX source: `data/papers/source/2602.22546v1-source.tar.gz` (38 members; SHA-256 `2ffb6dff8485d4a9807fd5b594672c674393865bc2c81ebf0dbcf478204e1a92`).
- Metadata and abstract HTML: `data/papers/source/2602.22546v1-metadata.xml` and `data/papers/source/2602.22546v1-abs.html`.

I read the complete paper and audited the TeX, tables, and figure references. The source archive confirms that the manuscript refers readers to Appendix A.1 for the 15-task list and Supplementary A.2 for participant setup, but contains neither appendix. `main.tex` retains the template warning to delete supplementary pages and comments out a nonexistent `sec/X_suppl`. The archive contains no implementation, data, prompts, run records, consent materials, or result builder.

### Release search boundary

The paper and source provide no project, code, data, model, or result URL. Targeted searches for the exact title, both expanded forms of AHCE, and author/code combinations found the arXiv record and third-party paper listings but no verifiable author-owned release. This is an acquisition-time bounded absence, not proof that no artifact exists elsewhere. Consequently, system and result claims below are paper-reported, not release-audited or replayed.

No paid model calls were made.

## One-sentence contribution

AHCE proposes timeout-triggered real-human consultation, GRPO-trained query/synthesis, and plan/control injection for a Minecraft agent, but its unreleased compound treatment and incomplete human/training evidence support only a configured human-coupled package gain—not learned expert-reasoning acquisition, efficient intervention-policy validity, or cross-domain expertise transfer.

## Why this matters for skill-bench

This review advances charter objectives A, B, C, E, and F through a bounded mechanism case: **what evidence is needed to promote a human interaction from available advice into acquired, adopted, and consequential expertise?** Minecraft is not a scope commitment. The same question applies when a research agent asks a scientist, an operations agent escalates to a specialist, or an office agent requests stakeholder clarification.

AHCE's central design intuition is worth retaining: expert knowledge need not be statically codified if an agent can recognize a decision-relevant gap and ask a low-burden question. But the study shows why endpoint uplift alone cannot distinguish:

```text
impasse opportunity
→ trigger decision
→ participant availability and authority
→ query content
→ human response
→ synthesis/transformation
→ adopted plan or control action
→ environment-state consequence
→ task outcome
→ human and system burden
→ bounded transfer claim
```

The paper reports the endpoint and aggregate active time, describes some intermediate modules, and omits the event-level joins. Useful completion is a strict claim ceiling plus reusable retain/repair/test guidance. Existing participation, evidence-acquisition, configured-system, trace, intervention, resource, task-health, metric, and validity machinery can house the requirements; a Minecraft- or AHCE-specific subsystem is not warranted.

## Research question and claim boundary

The paper asks how an LLM agent can request human help only after autonomous attempts fail and transform unstructured guidance into an executable correction. It frames two knowledge gaps: factual rules such as needing a pickaxe for stone, and contextual heuristics such as digging down to find stone (Introduction, pp. 1–2).

V1 supports that:

1. the authors specify a three-module architecture: PIM trigger, HFM interaction/synthesis, and QEM execution;
2. PIM is an inspectable deterministic policy based on per-subtask timeout and consecutive failures;
3. the HFM text protocol uses `<think>`, `<search>`, `<result>`, and `<Answer>` tags;
4. ten participants with prior Minecraft experience are reported as real response providers;
5. the table reports higher success and lower active human time for Qwen-7B/32B HFM packages than for MP5-core and AHCE-log;
6. a two-task ablation reports a success/burden tradeoff as the failure threshold changes.

V1 does not establish that the participants possess professionally or independently validated expertise; that the requested content is tacit rather than ordinary game knowledge; that the HFM learned a transferable inquiry policy; that the HFM's synthesis is source-faithful; that the synthesized plan rather than QEM maneuvers caused success; that `nmax=3` is prospectively optimal; or that endpoint effects transport across tasks, people, models, environments, or domains.

## Methodology and system

### MP5-core baseline and environment

The authors reimplement MP5, remove its successful-plan memory, replace its performer with vision-only MineDreamer, and replace GPT-4 with Qwen-plus (Section 3, pp. 3–4). These choices reduce two acknowledged advantages—cached solutions and privileged resource coordinates—but also create a new author-built package. The paper supplies no commit, dependency versions, MineDojo/Minecraft version, Qwen-plus snapshot, MineDreamer checkpoint, prompt, action API, timeout, seed, world-generation policy, retry rule, or environment-failure policy.

Each trial reportedly starts in a procedurally generated world. The manuscript does not say whether methods share paired world seeds, whether participants share world realizations, whether some worlds make a task infeasible, or whether biome/resource distance is balanced. QEM's example “escape maneuver” directly addresses world realization. Without paired seeds and state provenance, treatment and environment difficulty remain entangled.

The task suite has 15 curated tasks labeled Easy, Normal/Medium, and Hard by approximate minimum subobjectives (1–3, 4–5, and 6–9). Only one example per category is published. The promised complete list and descriptions are absent. Category names drift (`Simple/Moderate/Hard`, `Easy/Normal/Hard`, and table `Medium`). Task authorship, source, admission/rejection process, dependency graph, success oracle, timeout, alternative solutions, and overlap with MP5 development are unreported.

### Problem Identification Module: a fixed timeout gate, not learned identification

A subtask “fails” when execution steps exceed `smax`; a consecutive-failure counter increments; help is requested when `nfail > nmax` (Section 4.2, p. 4). Main experiments use `nmax=3`. This is a deterministic persistence threshold, not a learned diagnosis of knowledge gaps. No value for `smax`, counter-reset policy, subtask identity rule, timeout handling, irreversible-state detector, uncertainty signal, or distinction between planning, perception, controller, environment, and knowledge failures is given.

The trigger therefore detects repeated noncompletion, not the stated causal construct. It can request help for controller faults or bad worlds and fail to request before an irreversible mistake. The paper does not report trigger opportunities, true/false trigger labels, intervention rate, requests per trial, time-to-request, post-request recurrence, or outcomes conditional on trigger type.

The ablation varies `nmax` on only craft-wooden-sword and craft-stone-pickaxe using the strongest HFM. Raw values, repetitions, participant assignment, world seeds, and numerical uncertainty are absent; only a raster figure is released. The same ablation is used to choose `nmax=3` and justify the main setup, with no separate selection and confirmation tasks. The paper's claim that the 50–60 second plateau is “indispensable cognitive cost” is especially overstrong: a nonzero mean under selected successful configurations does not prove necessity without a no-help/fixed-information/oracle counterfactual and valid censoring.

### Human Feedback Module: core training evidence is missing

The HFM starts from Qwen-2.5-7B-Instruct or Qwen-2.5-32B-Instruct and is said to be GRPO-trained only on MuSiQue so it learns external-knowledge use without Minecraft facts (Sections 4.3 and 5.1, pp. 5–6). The paper prints a generic GRPO objective but omits the operational experiment:

- training split/version and preprocessing;
- mapping from MuSiQue questions/supporting facts to tool interaction;
- identity of the training-time “expert” or search result provider;
- reward components and answer verifier;
- group size, clipping, KL coefficient, learning rate, epochs, batch sizes, context limits, hardware, and seeds;
- base/reference/checkpoint hashes;
- prompt and tag parser;
- invalid query/result behavior;
- number of query turns and stopping policy;
- held-out MuSiQue performance;
- base-versus-trained or SFT-versus-GRPO comparison;
- evidence that Minecraft facts were absent from the base model rather than merely absent from fine-tuning.

Because reward is undefined, “learned policy” is not reproducibly specified. Because there is no untrained-HFM arm, no result isolates learning. MuSiQue may teach multi-hop QA formatting or tool-call syntax, but v1 does not show transfer of question selection, ambiguity clarification, source checking, or plan synthesis.

At runtime, the HFM may issue multiple `<search>` requests and receives human text wrapped as `<result>`, then emits an `<Answer>` plan. No transcript is published. The paper does not disclose what task state, planner history, action log, screenshot, inventory, failures, or prior expert answers the HFM sees; what exact query the participant sees; whether participants can inspect the environment; or whether they may refuse, express uncertainty, correct themselves, or ask for context. Raw guidance cannot be compared with synthesis for factual preservation, unsupported additions, contradiction resolution, or omission.

### Query Execution Module adds a second intervention

QEM injects the HFM plan into the planner system prompt. For execution deadlocks it also parses phrases and inserts predefined low-level actions such as `move_forward(10s)` (Section 4.4, pp. 5–6). This means the treatment combines human content, HFM interpretation, context injection, phrase-to-action routing, and author-coded control priors.

No action library, parser, precedence rule, applicability check, safety guard, or failure handling is released. A successful escape may reflect the prewritten maneuver rather than newly acquired expert knowledge. Conversely, a correct response may fail through planner or performer execution. Without raw-response, synthesized-plan, routed-action, and state-transition lineage, the study cannot locate where benefit or failure arose.

### Human participants and assignment

The paper reports ten participants—seven male, three female—with prior Minecraft experience, each conducting “one full trial for all 15 tasks” (Section 5.1, p. 6). This is the complete participant description. The missing supplement was supposed to provide setup and briefing.

Absent are recruitment, age/location, experience distribution, proficiency assessment, task familiarity, relationship to authors, independent/domain authority, compensation, consent/ethics review, briefing, interface training, permitted information sources, condition assignment, order/counterbalancing, washout, attrition, exclusions, participant-to-method mapping, repeated exposure, and whether the same participant's advice affected multiple conditions. “Prior Minecraft experience” licenses `experienced player`, not a calibrated expert ground truth.

Repeated tasks create person and task dependence. If participants see the same 15 tasks across conditions, learning/carryover is severe; if different participants or worlds supply different conditions, participant/environment confounding is severe. V1 does not state which design applies.

### Comparators do not isolate the HFM

- **MP5-core** has no human channel. AHCE-Qwen versus MP5-core estimates the whole added package, not HFM quality.
- **AHCE-log** shows the historical action log directly to a participant after impasse. It is unclear how the resulting guidance enters planning/control, whether it uses QEM, whether one response or dialogue is allowed, and whether participants receive equivalent state.
- **HFM-7B versus HFM-32B** changes synthesis/query model capacity and likely query content, context use, token/latency, and human response opportunity.

The paper needs at minimum equal-view/equal-execution arms: fixed expert answer through the same QEM, untrained/base HFM, GRPO HFM, raw answer without synthesis, and ideally a scripted rule/wiki answer. Human responses should be replayed or crossed where valid so participant content does not change with the mediator. No such factorial design is present.

## Evidence and result audit

### Main table

The main table reports:

| Method | Medium success | Medium human time | Hard success | Hard human time |
|---|---:|---:|---:|---:|
| MP5-core | 64% | 0 s | 10% | 0 s |
| AHCE-log | 86% | 81.0 s | 68% | 310.1 s |
| AHCE-Qwen-7B | 94% | 57.2 s | 78% | 122.3 s |
| AHCE-Qwen-32B | 96% | 32.7 s | 82% | 79.4 s |

All Easy rows are 100% with identical 251.4-second total time and zero human time. The exact identity is unexplained; it may indicate copied baseline values because no help is triggered, but no run ledger confirms that these are shared observations rather than independently executed conditions.

If the natural balanced interpretation is five tasks per category and ten participant/world repetitions, each category-method cell has 50 trials, and the 2-point granularity is consistent with every displayed rate. The paper never states the category counts, exact denominator per method, missing trials, or whether autonomous rows use the same ten worlds. Thus this is a plausible reconstruction, not an established denominator.

The paper reports averages without standard deviations, intervals, tests, or hierarchical analysis. Tasks are nested in difficulty categories; trials may be repeated within participant; worlds may be paired; participant advice may recur. Treating all observations as independent would be invalid. The 15 curated tasks also do not define a sampling frame for “domain-specific tasks.”

### Headline arithmetic and estimand drift

The abstract's “increasing task success rates by 32% on normal difficulty tasks and nearly 70% on highly difficult tasks” corresponds most plausibly to:

- medium: `96% - 64% = 32 percentage points` (`50%` relative);
- hard: `82% - 10% = 72 percentage points` (`720%` relative).

No ordinary definition yields 32% and nearly 70% as both relative changes. The prose should say approximately 32 and 72 percentage points. The “nearly 70” rounding also obscures whether it refers to the strongest HFM, AHCE-log's 68%, or a generic package.

The mechanism-relevant hard comparison is HFM-32B versus AHCE-log: 14 percentage points (`20.6%` relative). Even that is not a clean HFM effect because query format, interaction, evidence view, execution path, model calls, and active human time differ.

### Human burden metric is incomplete and partly ratio-of-means

The displayed ratios match aggregate time division:

- medium HFM-32B: `32.7 / 433.4 = 7.545%`, shown as 7.5%;
- hard HFM-32B: `79.4 / 1265.6 = 6.274%`, shown as 6.3%;
- hard HFM-7B: `122.3 / 1325.8 = 9.225%`, shown as 9.2%.

This indicates ratio-of-reported-means or exact aggregate equivalence, not necessarily mean per-trial participation ratio. A ratio-of-means weights long trials differently from a mean of trial ratios. The paper does not define whether failed/time-out trials contribute their full time, whether human time is conditional on requests or success, or why MP5-core hard total time is `-`. Missing autonomous failure time blocks equal-envelope efficiency comparison.

Recorded human time begins when a participant reviews a query and ends at submission. It omits availability/waiting, interruption, context switching, training, task familiarization, idle monitoring, rejected/unused advice, post-response correction, accountability, and study administration. Calling it cognitive load is unsupported because no workload instrument or error measure is used. Calling intervention minimal from a denominator dominated by agent runtime is also unsafe.

### Ablation evidence is descriptive, not policy validation

The raster figure reportedly varies `nmax` on two tasks. The text says wooden-sword success stays 100% until `nmax > 5`; stone-pickaxe success drops for `nmax > 3`; participation falls as the threshold rises; and total-time variance increases. No raw data, confidence bands definition, repeat count, participant/world identity, or analysis code exists. The light-blue region is called variance without defining whether it is SD, SE, range, or interval.

Choosing `nmax=3` requires a loss function over success, human burden, delay, and irreversible failure. None is declared. A point that looks visually balanced is an engineering choice, not an optimal learned intervention policy. The fixed threshold also cannot distinguish “ask earlier because state is becoming irreversible” from “ask later because another self-correction is cheap.”

### Failures and adverse effects are absent

The paper narrates two baseline failures but provides no case inventory for:

- unnecessary requests;
- incorrect or incomplete human responses;
- HFM distortion/hallucination;
- repeated clarification;
- correct advice rejected or misapplied;
- QEM parse/maneuver errors;
- post-intervention failures;
- human disagreement;
- harmful delays or irreversible states;
- environment/controller faults incorrectly treated as knowledge gaps.

Without negative and null cases, the claim that raw guidance is unreliable while HFM synthesis mitigates it rests on aggregate contrasts, not observed transformation failures and repairs.

## Unique insight: expert access, expert contribution, and acquired expertise are different states

AHCE's most useful lesson is not “treat the human as a tool.” It is that a benchmark must keep three claims separate:

1. **Access:** the system can contact a person assigned an expert role.
2. **Contribution:** the person provides a scoped response that is authoritative, relevant, and received.
3. **Acquisition:** the system transforms and adopts that response faithfully, produces the intended consequence, and can appropriately reuse or generalize it.

Endpoint success proves none of those joins by itself. A person may supply a common fact; the HFM may already know it; QEM may rescue the run with a prewritten action; or success may occur despite the advice. Conversely, good advice may be lost downstream. The benchmark unit should therefore be an **intervention episode**, linked to but distinct from the trial:

```text
opportunity and frozen state prefix
→ trigger policy and decision time
→ participant realization, expertise scope, and authority
→ exact query and evidence view
→ raw response, uncertainty, and response burden
→ synthesis with source-to-plan entailment
→ adopted planner/control delta
→ authoritative state transition
→ local and terminal consequences
→ recurrence/transfer under a new but related impasse
```

This also clarifies what “minimal” means. Minimality is not a low ratio alone. It is a Pareto statement over quality, severe misses, request count, active and elapsed human time, interruption, model/tool cost, and downstream rework relative to valid alternatives. An intervention can be short but premature, redundant, or wrong; a longer interaction can be efficient if it prevents expensive failure.

Finally, the paper's HFM does not learn **when** to ask. Timing remains a hand-set counter. What may be learned is how to produce tool-tagged queries and a final answer. `skill-bench` should version trigger policy, inquiry policy, transformation policy, and execution policy independently so “learned intervention” does not collapse four mechanisms.

## Comparison with adjacent reviewed evidence

- **YIELD** shows that interviewer-like next turns are not validated information acquisition. AHCE at least sends generated queries to real participants and observes endpoint execution, but publishes no query/response/claim-state lineage. It therefore cannot show what information was caused, acquired, or used.
- **HAS-Bench** supplies a strong availability → exercise → uptake → effect distinction but uses model simulators in main trials. AHCE uses real participants, yet lacks the typed participant authority, event ledger, treatment vector, and burden evidence needed to identify those stages.
- **CentaurEval** warns that a real-human package gain is not contribution necessity or complementarity. AHCE is even less identified: human/no-human and synthesis/log conditions do not hold task, evidence, execution, or interaction treatment constant, and no contribution replay is available.
- **Intervention-timing evidence** requires a frozen decision boundary, acceptable policy set, and consequence-grounded loss. AHCE's timeout counter is inspectable but not validated against knowledge-gap labels, irreversible boundaries, or matched policy outcomes; selecting `nmax=3` from two tasks is not learned or transportable timing.
- **Expert-participation governance** requires purpose, consent, authority, allowed use, transformation approval, attribution/compensation, and withdrawal boundaries. Prior Minecraft experience plus an absent supplement cannot populate those fields.
- Existing `skill-bench` inquiry, participation, intervention, configured-system, resource, validity, task-health, and trace machinery already covers the durable requirements. No AHCE-specific contract is needed.

## Limitations and validity threats

1. Only 15 curated Minecraft tasks; the complete task list and descriptions are missing.
2. Difficulty is approximate subobjective count, not calibrated empirical difficulty.
3. Category naming drifts among Easy/Simple, Normal/Moderate/Medium, and Hard.
4. No task sampling frame, authoring protocol, rejection flow, dependency graph, or alternative-solution policy.
5. Procedural worlds are unversioned and pairing/feasibility across methods is unspecified.
6. MP5-core is an unreleased author reimplementation with multiple component changes.
7. Model/checkpoint, environment, prompt, action-space, timeout, seed, and retry identities are incomplete.
8. PIM detects repeated timeout, not a validated knowledge gap or irreversible decision boundary.
9. `smax`, reset semantics, subtask identity, trigger opportunities, and trigger error rates are absent.
10. `nmax=3` is selected from two reported tasks without a separate confirmation set or declared loss.
11. The HFM GRPO reward and complete training procedure are absent.
12. No base/untrained/SFT/no-RL HFM comparator isolates learned collaboration.
13. No held-out MuSiQue or interaction-policy result validates training.
14. Training-time tool/expert realization and result provenance are unspecified.
15. Runtime HFM prompt, state/evidence view, query limit, stop rule, and invalid behavior are absent.
16. No raw query, response, synthesis, plan, action, or state-transition transcript is published.
17. HFM source-faithfulness, unsupported additions, omission, and contradiction handling are unevaluated.
18. QEM adds predefined control maneuvers, confounding human knowledge with author-coded rescue.
19. AHCE-log's evidence view, interaction mode, and execution route are underspecified.
20. MP5-core versus AHCE changes the full human/query/synthesis/execution package.
21. HFM versus log changes model, query, context, human time, and possibly execution together.
22. No fixed-answer replay, equal-transcript, oracle, wiki, scripted-query, raw-answer, or sham arm.
23. Participant expertise is only “prior Minecraft experience”; proficiency and authority are unmeasured.
24. Recruitment, relationship to authors, compensation, consent, ethics review, and allowed-use terms are absent.
25. The promised participant briefing supplement is not in PDF or source.
26. Participant-to-condition/task/world assignment and counterbalancing are absent.
27. Repeated participant and task dependence is ignored.
28. The percentages have no exact published denominators, missingness ledger, raw counts, or trial rows.
29. No uncertainty intervals, hypothesis tests, task/participant/world clustering, or multiplicity policy.
30. Headline “32%” and “nearly 70%” conflate percentage points and relative changes.
31. The closer HFM hard contrast is 14 points over AHCE-log, not the headline 72-point package contrast.
32. Identical Easy rows are unexplained and may not represent independent condition runs.
33. Failed hard MP5 total time is missing, blocking equal-envelope time comparison.
34. Failure/time-out handling in success and time averages is undefined.
35. Reported participation percentages appear to be ratios of means, not clearly means of trial ratios.
36. Human active time omits waiting, availability, interruption, preparation, monitoring, rework, and accountability.
37. No request count, turns, response length, failed contact, recurrence, or burden distribution is reported.
38. “Cognitive load” is inferred from wall-clock response time without a workload measure.
39. “Minimal” is inferred from a ratio inflated by long agent runtime.
40. The ablation raster has no raw values, repeat count, interval definition, or table builder.
41. The alleged 50–60-second indispensable plateau is observational and selected, not a necessity estimate.
42. No adverse-intervention, incorrect-human, distortion, rejection, or post-intervention failure analysis.
43. No persistence/transfer test shows that acquired guidance helps a later related impasse.
44. No privacy, sensitive-response, malicious-response, unavailable-human, latency, or escalation experiment.
45. No implementation/data/results release permits exact reproduction.
46. No tacit-transfer, expert-substitution, professional-validity, cross-domain, production, or readiness claim is licensed.

## Reproducibility and operational realism

**Paper/source inspectability is moderate.** The complete v1 PDF, text, TeX, main result table, architecture, generic GRPO expression, and raster ablation are preserved. Source inspection exposes the missing appendix/supplement boundary and confirms that no hidden task/participant section exists in the archive.

**Experimental reproducibility is very weak.** No code, data, model checkpoint, prompts, task list, participant instrument, environment manifest, run ledger, human transcript, raw trial outcome, analysis script, or release URL is available. The central HFM cannot be reconstructed because its reward and training pipeline are unspecified. Even the exact success denominators and participant-condition design cannot be recovered safely.

**Operational realism is mixed.** A stateful vision-controlled environment, sequential dependencies, real people, contextual questions, execution failures, and active response time are more realistic than static QA or simulator-only assistance. But Minecraft knowledge is mostly public and low stakes; the task suite is small and authored; participants are not validated domain professionals; consultation is synchronous and apparently always available; QEM uses prewritten rescue actions; and consent, accountability, disagreement, uncertainty, privacy, cost, persistence, and downstream professional artifact quality are absent.

The study is therefore a useful prototype of a real-human consultation pathway, not a validated expertise-transfer benchmark.

## Transfer to skill-bench

### Retain

1. Separate trigger, inquiry/synthesis, and execution modules.
2. Attempt bounded autonomous recovery before escalating when delay is safe and cheap.
3. Measure endpoint quality and human burden separately.
4. Include a naive assistance baseline rather than comparing only human versus no human.
5. Use real participants for claims about human interaction; simulator-only trials cannot inherit those claims.
6. Preserve factual-rule and contextual-heuristic gaps as candidate, not assumed, task labels.

### Repair before reuse

1. **Freeze intervention opportunities.** Record state-prefix hash, decision time, latest admissible observation, trigger signal, available actions, irreversible boundary, and whether a valid no-help continuation exists.
2. **Version four policies independently.** Trigger policy, inquiry policy, response-transformation policy, and execution policy need separate hashes and factorial treatments.
3. **Type participant realization and authority.** Preserve identity pseudonym, expertise scope/evidence, briefing, availability, consent/use, compensation/reciprocity, uncertainty, and whether the response is advice, approval, fact report, preference, or control.
4. **Preserve content lineage.** Store exact query, participant evidence view, raw response, synthesis, entailment/contradiction checks, adopted plan/control delta, and downstream state observations.
5. **Use valid matched arms.** Compare no-help, fixed-information, raw response, base/untrained mediator, trained mediator, and where defensible scripted/oracle channels under equal planner/QEM/tool/time envelopes. Replay the same authorized response across mediator conditions when causally valid.
6. **Measure interaction opportunity and burden.** Report eligible impasses, requests, turns, active response time, elapsed wait, interruptions, unavailable/refused responses, preparation, corrections, rework, and total human plus system cost.
7. **Cluster and repeat appropriately.** Pair environment seeds, counterbalance participant/task/order, use equivalent forms for learning control, repeat stochastic systems, and report participant/task/form/world uncertainty.
8. **Validate transformation and consequence separately.** Score response authority and correctness, synthesis faithfulness, semantic uptake, local state effect, terminal outcome, collateral effects, and recurrence under related impasses.
9. **Predeclare the intervention loss.** Success, severe failure, delay, human burden, privacy, and false-request/missed-request costs determine whether a threshold is useful; a visually balanced point is not an optimum.
10. **Require transport evidence.** A policy trained on QA and tested on public game knowledge is a promising interface result, not expertise transfer across professional domains.

### Bounded validation slice

A reusable cross-domain experiment can be small:

- construct several equivalent-form task families with planted factual, contextual, contradictory, unavailable, and no-help-needed impasses;
- freeze paired states just before each help decision;
- recruit consented contributors with scoped authority or use an explicitly scripted oracle for mechanism-only calibration;
- randomize response presentation through raw, base-synthesis, and trained-synthesis arms while holding QEM and state fixed;
- include no-help, sham-contact, and fixed-information controls where ethical;
- replay adopted plans from the same state to observe local consequences;
- score trigger precision/recall under declared loss, source-to-plan entailment, unsupported additions, uptake, recovery, collateral effects, repeated-impasse transfer, active/elapsed human burden, and complete cost separately.

This would test the general hypothesis that learned mediation improves use of bounded human guidance. It would not by itself establish professional validity or expert substitution.

## Concrete repository actions

1. Index this review as full-paper/source-audited evidence with no release.
2. Add no new build task. The review's requirements refine existing expert-participation, evidence-acquisition, intervention-attribution, configured-system, resource, trace, task-health, metric, and validity machinery.
3. In future human-guidance pilots, prohibit the phrase “expertise transfer” unless the raw contribution, scoped authority, transformation faithfulness, adoption, consequence, and related-impasse reuse are all observed.
4. Treat percentage-point and relative changes as separate typed result fields; never report one with the other's unit.
5. Keep “minimal intervention” unsupported unless request opportunity, interaction counts, active and elapsed burden, missing/unavailable episodes, total cost, and quality loss are jointly reported.

## Action items completed

- [x] Read the complete immutable v1 PDF and full text.
- [x] Audited all 38 official TeX-source members, including tables, figure references, and the missing appendix/supplement boundary.
- [x] Recomputed percentage-point, relative-change, time-reduction, and displayed participation-ratio arithmetic.
- [x] Performed a bounded official-release search and did not substitute third-party summaries for primary evidence.
- [x] Compared the evidence with YIELD, HAS-Bench, CentaurEval, intervention-timing, and participation-governance reviews.
- [x] Added no duplicate task and made no tacit-transfer, expert-substitution, professional-validity, cross-domain, production, or readiness claim.
