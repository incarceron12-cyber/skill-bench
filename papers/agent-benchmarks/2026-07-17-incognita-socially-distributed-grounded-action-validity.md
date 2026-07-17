# Paper Review: Incognita Observes Routed Messages and Mediated State Changes, Not Socially Distributed Expertise

- **Paper:** Dan C. Hsu and Luke Lu, *Evaluating Generative Agents with Actions Grounded in Socially Distributed Task Environments using Incognita*, https://arxiv.org/abs/2607.02975v1
- **Date read:** 2026-07-17
- **Venue / source:** immutable 13-page arXiv v1 preprint, marked “under review”
- **Tags:** distributed-knowledge, grounded-action, role-simulation, information-routing, stateful-evaluation, stopping, tau-bench, release-inspectability
- **Local PDF:** `data/papers/pdfs/2607.02975v1-incognita-socially-distributed-task-environments.pdf` (13 pages; SHA-256 `682af281e8cbaf8bc12463ddf8923af32c733d817cde3c4ec2e2a90d5e5b9924`)
- **Local text:** `data/papers/text/2607.02975v1-incognita-socially-distributed-task-environments.txt` (SHA-256 `611ce52c11bb68937f727546dc17df8d72778f858b08a09135491ed24f3e998a`)
- **API metadata:** `data/papers/source/2607.02975v1-metadata.xml`
- **Release status:** no official code, task corpus, trajectories, evaluator, or result artifact is cited in the complete paper. Targeted title/author/project searches found no author-identified release as of the review date. Unofficial implementations were not substituted.

## Verdict

Incognita proposes a useful composition that many social-agent evaluations omit: one evaluated agent must route messages among isolated model participants; only specialist participants can propose scoped operations; a deterministic subsystem is said to validate and execute accepted reads/writes over canonical state; and the inherited τ-bench evaluator scores terminal state. This makes a consequential distinction between **saying that work is done** and **realizing an accepted state change**. Its minimal test-agent prompt also exposes source selection and premature stopping instead of supplying a tool catalog and policy.

The empirical study is nevertheless much less identified than its framing suggests. It contains only 18 transformed retail tasks, three per reported social-breadth level, repeated ten times for each of three model snapshots. There is no centralized τ-bench control, disclosed-role control, direct-tool control, oracle routing policy, or matched transformation audit. “Social breadth” is the number of distinct specialists in one reference solution, not an isolated intervention: task content, operation family, argument burden, user disclosure, policy demands, feasible alternatives, and baseline difficulty may all change with it. The paper correctly says difficulty remains multidimensional, but still organizes its central figure by breadth without task-level estimates or uncertainty.

More seriously, no release permits inspection of the transformation, task cards, disclosure gate, entity–tool whitelist, admission logic, canonical transition code, reward replay, run records, or failure classifier. The paper names five failure categories in a figure but does not define or annotate them. It reports process proxies—fraction of hidden user fields disclosed, any specialist contacted, any accepted write, and the complement of “premature finalization”—without showing that received content was understood, justified the operation, survived mediation, or caused reward. The system can therefore observe routed contact and selected state events, but the manuscript does not demonstrate its stronger semantic chain.

For `skill-bench`, retain the architecture and sharpen the event model. A socially distributed episode should separately record possession, contact opportunity, message receipt, proposition-level adoption, justified operation request, specialist acceptance/rejection, exact realized state effect, and endpoint consequence. Do not infer tacit expertise, human collaboration, organizational authority, professional validity, reliability, safety, or readiness from role labels, model-generated dialogue, contact breadth, or sparse terminal reward.

## One-sentence contribution

Incognita composes role-isolated model interaction, specialist-mediated operations, canonical state mutation, explicit finalization, and inherited terminal reward in an 18-task/540-trial retail study, but supports only a preliminary configured-simulator description because the transformed tasks, implementation, trajectories, failure labels, controls, and uncertainty are unavailable.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through narrow expansion into a cross-domain measurement problem: consequential knowledge work often separates who knows something, who may be contacted, who can act, and what state records the consequence. Retail is a bounded substrate, not a scope commitment.

Incognita joins several already reviewed boundaries without replacing them:

- **Organizational tacit-knowledge simulation** makes planted possession and complete dialogue logs inspectable but stops at generated-description recovery. Incognita adds mediated writes and endpoint state reward, but does not release the possession, dialogue, or state lineage needed to inspect that join.
- **YIELD** provides real historical dialogue but no response to a model-generated question. Incognita produces interactive simulated responses, but those responses are another configured model component and have no human/expert validity.
- **EntCollabBench** exposes role-scoped tool surfaces and persistent service effects. Incognita further hides capabilities behind neutral specialist names and makes source discovery part of the task, but a specialist route still does not establish delegated authority or professional collaboration.
- **τ-bench** supplies the source task/reward family. Reusing its endpoint observer preserves some score mechanics, not task equivalence, because Incognita changes prompt visibility, policy access, tool access, interaction topology, and stopping.

The distinct uncertainty clarified here is whether a benchmark can connect social information acquisition to executable consequences without collapsing all intermediate stages into contact or final success. The paper supplies a promising architecture; absent artifacts and controls prevent validation. Useful completion is therefore a bounded claim ceiling plus reusable retain/repair/test requirements, not an Incognita-specific schema or retail pilot.

## Contribution and research question

The paper asks how to evaluate a generative agent when task-relevant information is partitioned among role-isolated participants and consequential actions are available only through interaction with those participants (Abstract and Section 1, pp. 1–2). It contributes:

1. a “socially distributed task environment” framing;
2. a POMDP description in which directed messages are actions and participant replies are observations;
3. Incognita, a Concordia-based social layer coupled to a deterministic grounded subsystem and offline evaluator;
4. Incognita-Retail, described as a transformation of τ-bench retail;
5. an explicit `FINAL` action interpreted as completion belief;
6. process measures for disclosure, participant contact, accepted writes, and finalization; and
7. a preliminary 540-trial comparison of three OpenAI model snapshots.

The strongest defensible research question is narrower than “collaborative agency”: under one fixed model-simulated environment, do three evaluated model configurations differ in terminal reward and coarse interaction events? The paper-reported answer is yes descriptively. It does not identify whether differences arise from knowledge acquisition, semantic integration, action planning, simulator compatibility, disclosure behavior, operation mediation, reward coupling, or stochastic run composition.

## Methodology and system

### Intended information-to-action architecture

The test agent sees seven neutral participant names—`USER`, Aster, Boreal, Cygnus, Dorian, Elara, and Fenn—and a generic objective to resolve the user's request (Appendix A.1, pp. 9–10). It receives no goal, policy, capability list, exploration hint, irreversibility warning, or direct tool access. Each turn is one JSON message to one recipient or a final message to `USER`.

The six specialists correspond to account, returns/exchanges, catalog, order records, identity lookup, and pending-order operations (Appendix A.3, pp. 10–12). Prompts instruct them to disclose reactively, remain within remit, avoid referrals, and summarize rather than reveal all records. Tool names are absent from prompts and are said to be bound separately through an entity–tool whitelist. The USER answers only from progressively disclosed goal-card memory. Specialists have only their local dialogue; the evaluated agent alone sees global interaction history (Section 2.3, p. 4).

A specialist may propose a read or write. The grounded subsystem is said to verify that the operation belongs to that specialist and that arguments are admissible, then execute it over canonical state (Section 2.4, pp. 4–5). Reads return narrated observations; accepted writes mutate state. After `FINAL`, the evaluator compares terminal database state with a replayed gold state and, where applicable, uses inherited natural-language assertions (Section 2.6, p. 5).

This is a strong conceptual separation:

`message → participant observation → proposed operation → admission → execution → canonical state → terminal observer`

But only the prompts are reproduced. The paper does not disclose the task-card schema, deterministic renderer, goal-card fields, per-field disclosure policy, tool schemas, whitelist, proposal parser, argument validator, operation receipts, state schema, gold replay, natural-language judge prompt, or transformation code. The exact mechanism cannot be audited from v1.

### LLM components and configured-system identity

Appendix B (pp. 12–13) identifies the evaluated systems as:

- `gpt-5.2-2025-12-11`, high reasoning effort, temperature 1;
- `gpt-5.4-2026-03-05`, high reasoning effort, temperature 1; and
- `gpt-5.5-2026-04-23`, high reasoning effort, temperature 1.

The USER, all six specialists, and disclosure gate use `gpt-5.4-2026-03-05` at temperature 0. Natural-language reward assertions use `gpt-4.1-2025-04-14` at temperature 0 when applicable. This disclosure is better than family names alone: the environment is explicitly a model-mediated treatment, not a deterministic social world.

Still missing are provider/API version, prompts for the disclosure gate, seeds, request IDs, token/turn/context limits, reasoning settings for environment models, retries, timeouts, invalid-JSON handling, simulator invalidity, truncation, service failures, tool-call/proposal decoding, and trial-level component hashes. Temperature 0 does not make hosted simulators deterministic, and all three evaluated models interact with a fixed `gpt-5.4` ecology that may favor stylistic/protocol compatibility with one condition.

### Task construction and transformation validity

The paper says a centralized source task—user interaction, policy context, and tool interface—is transformed into a task card whose content is selectively rendered by role and time (Section 2.2, p. 4). Demand-side information moves behind a USER disclosure gate; operational knowledge and actions move behind specialists. The source task's terminal reward is retained.

That is not enough to establish semantic preservation. At least five constructs change simultaneously:

1. **initial information:** source goal/policy/tool descriptions are hidden;
2. **action interface:** direct tools become free-text requests to stochastic specialists;
3. **policy location:** operating rules are embedded in specialist prompts rather than supplied to the test agent;
4. **interaction cost and observability:** one recipient per turn replaces source dialogue/tool calls; and
5. **completion interface:** explicit self-finalization becomes part of the score-generating process.

An unchanged terminal checker can still grade a different and potentially harder task. No source-task IDs, before/after cards, path-equivalence proof, reference traces, alternative valid paths, feasibility audit, task attrition, or source-versus-transformed baseline is reported. “Preserving final-state reward semantics” should therefore mean **reusing an inherited terminal observer**, not proving construct, difficulty, or solution-set equivalence.

### Study design and statistical units

The corpus has 18 tasks stratified over social breadth 1–6, ten repetitions per task, and three model conditions: 540 trial records in principle (Section 3, pp. 5–6). Figure 2 has 30 trials per model/breadth cell, implying three tasks per breadth. Social breadth is the number of distinct specialists used by the reference solution.

The experiment says it “varies only the evaluated agent,” but this describes intended configuration, not statistical control. USER, specialist, and disclosure outputs can vary by trial; their realized observations and accepted proposals are post-treatment parts of each trajectory. Tasks are repeated clusters, breadth cells contain only three task identities, and model conditions apparently reuse task definitions but not matched simulator draws. No pairing strategy, common random numbers, run seed, task order, blocked analysis, mixed model, task-clustered interval, or model-by-task table is provided.

The 180 trials per model are therefore not 180 independent work constructs. Even a naive trial-level Wilson interval is wide: 16/180 has an approximate 95% interval of 5.5%–14.0%, and 31/180 has 12.4%–23.4%; these are illustrative only and overstate inferential information when repeated tasks and stochastic shared simulator components are ignored. Within a breadth cell, 8/30 and 9/30 have naive intervals of roughly 14.2%–44.4% and 16.7%–47.9%. The paper reports point estimates only.

No human, scripted, random-routing, direct-tool, fully disclosed, centralized τ-bench, oracle-source, oracle-operation, or no-social-partition baseline appears. The design therefore describes model-conditioned behavior inside one package; it does not estimate the effect of social distribution, mediation, hidden capabilities, or breadth.

## Evidence and results

### Terminal reward

Paper-reported success is 0/180 for GPT-5.2, 16/180 (8.9%) for GPT-5.4, and 31/180 (17.2%) for GPT-5.5 (Figure 2 and Section 3, p. 6). GPT-5.4 succeeds only at breadth 3 and 4. GPT-5.5 reports nonzero cells at every breadth, from 30.0% at breadth 3 to 3.3% at breadth 6.

These counts support a descriptive configured-system ordering on the selected transformed task repetitions. They do not establish monotonic breadth difficulty: GPT-5.5 scores 13.3%, 13.3%, 30.0%, 23.3%, 20.0%, and 3.3% from breadth 1 through 6. Task identity and burden vary inside that sequence. Nor do they establish reliability: pass@10, pass-all, task-level variance, retry benefit, failure correlation, and repeat stability are absent.

Terminal reward is conjunctive across operative database and natural-language channels. That preserves an outcome gate, but the paper does not report channel-specific outcomes, judge applicability, natural-language judge error, replay failures, alternative acceptable states, collateral mutations, or invalid trials. A zero can arise from no interaction, wrong user understanding, failed disclosure, wrong specialist, rejected operation, wrong arguments, simulator error, incorrect write, missing natural-language assertion, or checker incompleteness.

### Process metrics

Figure 3b reports, across model conditions:

- disclosure coverage: 0.06 → 0.17 → 0.45;
- entity-contact breadth divided by six: 0.30 → 0.68 → 0.68;
- write rate: 0.00 → 0.13 → 0.36; and
- non-premature rate: 0.00 → 0.13 → 0.42.

These are useful observables, but their labels exceed what they prove:

- **Disclosure coverage** is the fraction of locked USER subfields revealed. It measures gate emission, not whether the agent asked a discriminating question, received the intended proposition, retained it, reconciled it, or used it.
- **Entity-contact breadth** counts distinct named specialists addressed and divides by all six, not by task-relevant specialists. It mixes useful source selection with broad or wasteful broadcast behavior and ignores message content, response, and repeated burden.
- **Write rate** is merely at least one accepted write. It does not distinguish necessary, correct, authorized, premature, harmful, collateral, or reverted writes.
- **Non-premature rate** is one minus a failure label whose operational rule is not supplied. It is not an independent measure of calibrated stopping.

The saturation of contact breadth from GPT-5.4 to GPT-5.5 while disclosure and writes rise could mean later models ask better user questions and convert interactions into operations. It could also reflect gate compatibility, task mix, longer trajectories, or different acceptance behavior. Without event-linked propositions and matched task trajectories, the mechanism is not identified.

### Failure composition and finalization

The paper treats `FINAL` as an observable commitment that the goal is satisfied (Section 2.5, p. 5). Premature finalization falls from 100% to 87% to 58%; success rises from 0% to 8.9% to 17.2%. Figure 3a additionally names execution error, goal-belief error, environment-belief error, and natural-language communication failure.

Explicit finalization is worth retaining. Calling it a direct readout of “task-completion belief,” however, is stronger than the evidence. A model may finalize because of turn limits, misunderstood protocol, inability to identify a recipient, malformed-output recovery, refusal, context exhaustion, or strategic stopping—not because an internal probability crossed a completion threshold. The formal quantity `q_t = E[G(s)]` is an analytic metaphor; no confidence report, probability, threshold, or calibration observation is elicited.

Most importantly, v1 never defines the five terminal failure categories, their precedence, annotator/algorithm, evidence view, invalid category, or reproducibility. The percentages in Figure 3 cannot be independently reconstructed, and category labels risk inferring latent belief causes from surface trajectories. “Environment-belief” and “goal-belief” require proposition-level evidence or controlled repair tests; otherwise they are analyst interpretations rather than observed roots.

### Negative and missing evidence

The paper reports no:

- per-task table, trajectory examples, state diffs, operation receipts, or failure cases;
- confidence intervals, tests, task-clustered uncertainty, variance components, or repetition analysis;
- token counts, turns, latency, calls, retries, dollars, invalid outputs, service failures, or censoring;
- centralized/source-task comparison or transformation conformance test;
- human/expert participants, task-authoring protocol, professional review, or user-simulator validation;
- unauthorized-operation probes, privacy tests, harmful-write audit, false-accept/false-reject rate, or collateral-state observer coverage;
- code, task data, run manifest, result tables, prompts beyond participant roles, or evaluator artifacts.

The manuscript appropriately calls the study preliminary and says reliability remains low. That caution should govern every downstream use.

## Unique insight

The deepest transferable insight is that **socially distributed action is not one transition from “communication” to “success”; it is a typed chain with several independently falsifiable joins**:

`authoritative knowledge exists`
`→ a participant possesses and may disclose it`
`→ the agent has a contact opportunity`
`→ a message reaches that participant`
`→ a proposition is returned`
`→ the agent semantically adopts it with scope and uncertainty`
`→ the proposition justifies a concrete operation request`
`→ the specialist accepts or rejects that request under its remit`
`→ the grounded subsystem realizes an exact state effect`
`→ the terminal observer recognizes the intended consequence`

Incognita's architecture can in principle expose most of this chain. The reported metrics directly expose only contact, gate disclosure count, at least one accepted write, finalization, and endpoint reward. They do not establish proposition identity, semantic adoption, justification, authority, acceptance reasons, exact effect lineage, or observer completeness.

A second insight is that **mediation is simultaneously a realism mechanism and a treatment confound**. Replacing direct tools with LLM specialists tests whether the evaluated model can communicate in a way that another configured model translates into operations. A failed state change may originate in the test agent's knowledge/routing, the specialist's interpretation/proposal, admission code, execution, or observer. Unless each boundary has an immutable request/response/receipt and matched conformance probes, “agent failure” launders environment-component errors into capability conclusions.

Third, **retaining a source benchmark's terminal reward does not retain its construct**. The checker can remain byte-identical while information visibility, policy access, action affordances, cost, stochasticity, and feasible paths change. Transformation validity needs a bridge: source/transformed task identity, public-requirement equivalence, path witnesses, alternative-solution tests, observer equivalence, and matched controls.

Fourth, **breadth is a design attribute, not automatically a difficulty scale**. Reference-solution specialist count can be useful for stratification, but only after separating task family, operation count, user-field count, argument dependencies, irreversible writes, and alternative routes. Otherwise breadth is a label on a three-task cell, not a calibrated social-complexity axis.

Finally, **finalization is valuable as an action-boundary observation but weak as latent-belief evidence**. A benchmark should record the explicit closure claim, unresolved critical propositions, performed effects, stop reason, budget/censoring, and perhaps calibrated confidence. Post-hoc failure before required operations supports “unsupported closure”; it does not by itself identify why the model believed, chose, or was forced to stop.

## Limitations and validity threats

1. **No official release:** transformed tasks, code, trajectories, state records, evaluator, and results are not inspectable.
2. **Only 18 tasks:** each breadth level appears to contain three task identities, limiting coverage and task-level inference.
3. **Retail-only substrate:** one customer-service transformation does not establish cross-domain social-distribution capability.
4. **No task sampling frame:** source-task selection, exclusions, representativeness, and attrition are absent.
5. **No authoring/validation protocol:** no evidence identifies who transformed tasks, checked equivalence, or reviewed professional legitimacy.
6. **Transformation bundle:** goal, policy, tools, participants, interaction protocol, and stopping all change together.
7. **No source-task control:** inherited reward reuse is not tested against centralized τ-bench performance on the same tasks/configurations.
8. **No direct-tool/disclosed-role controls:** social mediation, hidden capabilities, and information partition cannot be isolated.
9. **Reference breadth is endogenous:** one reference solution may not be minimal, unique, or required for alternative valid paths.
10. **Breadth confounding:** specialist count co-varies with task content, operations, arguments, user fields, and baseline difficulty.
11. **Only three tasks per breadth:** 30 trial observations do not create 30 independent tasks.
12. **Repeated-task dependence ignored:** ten repetitions are pooled without task-clustered uncertainty or paired analysis.
13. **Simulator stochasticity unpaired:** no common random numbers, saved seeds, or matched environment trajectories are reported.
14. **Shared model ecology:** all participant simulators use GPT-5.4, potentially creating model-specific communication compatibility.
15. **Hosted-component mutability:** request IDs, API version, run dates, seeds, retries, and service errors are absent.
16. **Disclosure gate unspecified:** prompt, field policy, trigger logic, leakage rate, false withholding, and reproducibility are unavailable.
17. **Task card unspecified:** role/timing projections and public/private requirement boundaries cannot be audited.
18. **Whitelist/admission unspecified:** entity ownership, argument validity, rejected proposals, and false admission are not inspectable.
19. **Canonical-state claim unverified:** state schema, transaction semantics, rollback, concurrency, reset, and collateral effects are absent.
20. **Gold replay may be nonunique:** one replayed state can reject legitimate alternatives unless equivalence is tested.
21. **Natural-language judge unvalidated:** applicability, prompt, evidence view, agreement, invalid handling, and error rates are absent.
22. **Conjunctive reward opacity:** DB and NL channel outcomes are not separately reported.
23. **Contact is not source selection:** normalized breadth rewards any distinct contact, including irrelevant ones.
24. **Disclosure is not receipt/adoption:** emitted fields are not linked to understood or used propositions.
25. **Any-write proxy:** accepted-write presence ignores correctness, necessity, authorization, collateral effects, and reversals.
26. **Undefined premature finalization:** no executable definition, evidence rule, budget boundary, or label precedence is given.
27. **Latent-belief overinterpretation:** finalization does not identify an internal completion probability or causal belief error.
28. **Undefined failure taxonomy:** execution, goal-belief, environment-belief, and communication categories lack protocols and examples.
29. **Root/surface conflation:** a missing endpoint can originate in the agent, simulator, mediator, executor, or observer.
30. **No invalid-trial account:** malformed JSON, timeouts, simulator failures, judge failures, and censored runs have no denominator.
31. **Point estimates only:** no intervals, tests, model-by-task effects, or uncertainty accounting is reported.
32. **No reliability profile:** ten runs are not summarized as pass@k, pass-all, task variance, correlated failure, or retry value.
33. **No cost evidence:** calls, messages, tokens, latency, dollars, and coordination burden are missing.
34. **No human/expert validation:** role prompts and user simulation do not establish tacit expertise, human collaboration, or professional practice.
35. **No authority semantics:** specialist capability and accepted operation do not establish principal authorization or delegated accountability.
36. **No safety evidence:** no unauthorized, privacy, harmful-write, irreversible-action, or false-accept controls are reported.
37. **No contamination analysis:** public τ-bench task lineage and possible model familiarity are not examined.
38. **No examples or negative cases:** qualitative failure claims cannot be checked against complete evidence views.
39. **Static participant prompts only:** reproduced prompts do not establish how tools, proposals, disclosure, and reward actually behaved.
40. **Readiness unsupported:** sparse selected-task success and absent operational evidence preclude deployment or professional-reliability claims.

## Reproducibility and operational realism

**Paper inspectability is moderate; experimental inspectability is low.** The immutable PDF provides exact model snapshots, temperatures, test-agent output format, full USER behavior prompt, and all six specialist role/conduct/operating prompts. It clearly marks the study preliminary and discloses LLM use in agents, environment participants, disclosure, judging, code assistance, and manuscript preparation.

Exact reproduction is impossible from v1. The source tasks and transformed cards are unnamed; the code, dependencies, Concordia configuration, tool schemas, renderer, gate, validators, state snapshots, reward implementation, trial seeds, trajectories, outputs, and analysis are absent. Search found only the paper and third-party summaries, not an author-identified repository or dataset. The reported 540 rows therefore cannot be replayed, reclassified, or audited for missingness, cost, task dependence, or paper-table consistency.

Operational realism is mixed. Positive features include role-local views, no direct test-agent tools, explicit recipient choice, confirmation rules before selected writes, read/write distinction, canonical persistent state, explicit closure, and terminal state evaluation. These are meaningful synthetic workflow mechanics.

Missing are real people and expertise; source authority; organizational permissions; authenticated delegation; availability and scheduling; refusal and strategic withholding; inconsistent or stale evidence; privacy and affected-party constraints; asynchronous work; artifacts and handoffs; alternative legitimate procedures; repair and escalation; human burden; and independently validated professional consequences. Model participants are useful environment components, not evidence that real users or specialists behave this way. The proper operational description is **a proposed LLM-mediated retail transition environment**, not a validated organization, collaboration simulator, or expertise-transfer benchmark.

## Transfer to skill-bench

### Retain

- The architectural separation of social interaction, operation mediation, canonical execution, and offline evaluation.
- A minimal agent interface that requires discovering source roles instead of exposing a complete tool catalog.
- Role-local participant views while preserving a global evaluated-agent trace.
- Explicit read/write distinction and exact state receipts.
- Explicit finalization as a scorable action boundary.
- Terminal reward plus process observations, kept plural rather than collapsed into one scale.
- Source benchmark lineage, provided transformation validity is separately established.

### Repair before reuse

1. **Represent the complete information-to-effect chain.** Give each required proposition an immutable ID and record possession/authority, contact opportunity, request, delivered response, agent adoption evidence, operation justification, specialist disposition, execution receipt, state delta, and terminal criterion.
2. **Freeze transformation lineage.** Bind source task/version, transformed task card, role projection, public basis, source and transformed observers, reference witnesses, alternative paths, and equivalence review.
3. **Separate participant realization from role label.** Record model/prompt/tool/view/state for every USER, gate, and specialist component independently; treat their errors as environment evidence until localized.
4. **Instrument mediation.** Preserve proposed operation, typed arguments, specialist rationale, acceptance/rejection reason, validator result, exact effect, rollback, and collateral state—not merely “any accepted write.”
5. **Make stopping auditable.** Record explicit closure claim, confidence if requested, unresolved critical propositions, stop reason, budget/censoring, performed effects, and post-hoc support. Avoid naming latent belief roots without evidence.
6. **Use task-relative source-selection metrics.** Report relevant-contact recall/precision, required-source opportunity, redundant/unnecessary contacts, repeated burden, unanswered contacts, and semantic claim yield—not contact count divided by six.
7. **Add matched controls.** For each task, compare centralized/direct-tool, fully disclosed mediated, hidden-role mediated, oracle routing, and intended Incognita conditions under matched task forms and simulator draws.
8. **Calibrate social breadth.** Cross breadth with operation count, user fields, argument dependencies, reversibility, and task family; validate minimal/alternative specialist sets instead of assuming one reference path.
9. **Fail closed on environment validity.** Separate malformed agent output, participant/gate failure, operation rejection, executor fault, observer invalidity, budget exhaustion, and substantive agent failure.
10. **Release immutable evidence.** Publish task cards, source IDs, code commit, component hashes, per-trial manifests, redacted trajectories, operation receipts, before/after state, channel scores, usage/cost, label protocol, and analysis.

### Tests the paper implies

- **Transformation bridge:** run the same configured model on source τ-bench, disclosed mediated, and socially distributed forms; estimate task-level paired deltas and adjudicate changed legitimate solution sets.
- **Possession-to-effect mediation:** plant required propositions and check each chain stage; test whether endpoint failures can be localized before assigning root labels.
- **Gate conformance:** use deterministic answerable/unanswerable/user-refusal cases to estimate false disclosure, false withholding, scope loss, and repeated-question behavior.
- **Operation admission conformance:** test correct, wrong-role, malformed, unauthorized, stale, duplicate, irreversible, and alternative-valid proposals with exact receipts.
- **Breadth factorial:** hold source task and operation burden fixed while varying only role partition; separately vary information partition and operation mediation.
- **Stopping calibration:** compare explicit confidence/unresolved-claim declarations with required effects under matched budgets; distinguish voluntary closure from forced termination.
- **Reliability/cost:** report per-task repeated-run distributions, pass-all/pass@k, correlated simulator failures, turns, calls, tokens, latency, and dollars.
- **Negative controls:** contacting all six specialists, eliciting all user fields, or producing any write must not score as good process when contacts are irrelevant, disclosure is unnecessary, or writes are wrong.

## Concrete repository actions

1. **No new build task.** The required objects already belong in the benchmark-bundle trace/state-effect records, execution-validity boundary, task-health lifecycle, metric specifications, validity arguments, and existing authority/handoff concepts. Creating an Incognita-specific contract would duplicate machinery and narrow scope.
2. Use this review in the next consolidation of distributed knowledge and collaboration evidence. The durable synthesis should join the organizational-simulation possession/referral layers, YIELD's question→answer boundary, EntCollabBench's capability/handoff/authority contracts, and Incognita's mediation→state-effect layer.
3. For any future multi-participant pilot, require at least one negative trace where contact occurs but no proposition is adopted, one where a justified proposal is rejected correctly, one where an accepted write is wrong, and one where endpoint reward passes through an impermissible route. These discriminate transport, semantics, admission, effect, and observer validity without committing the project to retail.

## Bounded claim ceiling

The full v1 paper supports this statement:

> In an unreleased 18-task Incognita-Retail implementation described by the authors, three configured OpenAI model snapshots produced different paper-reported terminal rewards and coarse contact/disclosure/write/finalization summaries across 540 repeated trials. The architecture is designed to route messages through model-simulated participants and mediate operations into canonical state before inherited τ-bench-style evaluation.

It does **not** support claims of validated socially distributed expertise, human or organizational collaboration, causal benefit from social breadth, preserved τ-bench task equivalence, semantic knowledge adoption, accurate failure-root attribution, calibrated completion belief, reliable operation, safety, cross-domain capability, professional validity, cost-effectiveness, or deployment readiness.
