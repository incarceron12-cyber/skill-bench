# SovereignPA-Bench: separating observable state from hidden labels is useful, but “user sovereignty” remains an author-defined prompt-policy score

**Source.** Dylan Zongmin Liu, *SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints*, arXiv:2607.05363v1 (6 July 2026), <https://arxiv.org/abs/2607.05363v1>.

**Full text read.** Immutable 10-page v1 local PDF: `data/papers/pdfs/2607.05363v1-sovereignpa-bench.pdf` (SHA-256 `6d5d09e169789995808e8676c8b9741e82bf94e54bc24d4a610d0acb50b4398b`). Complete local `pdftotext -layout` extraction: `data/papers/text/2607.05363v1-sovereignpa-bench.txt` (SHA-256 `569c96718c4d5c0d83464c08af9bcdf5bc4b55d5f4736bc3c8e2ad306d9fb10a`). PDF title, sole-author byline, arXiv v1 marker, 10-page count, and extraction through Appendix C were verified locally. The arXiv API summary contains no withdrawal notice. Date read: 2026-07-13.

**Release search.** The paper repeatedly describes an “uploaded,” “submitted,” and eventually public artifact containing scenarios, 3,840 prompts/outputs/provider responses, parsed actions, metrics, code, hashes, and 720 audit labels (pp. 1–3, 6, 9–10), but provides no URL, DOI, repository, archive identifier, manifest, or access procedure. The arXiv record links only the abstract and PDF. The arXiv source archive contains the manuscript, styles, figures, and generated tables, not the claimed benchmark artifact. Exact-title, author, file-name, and `FullSovereign` searches found no verifiable author- or institution-owned release. Therefore none of the scenarios, prompts, hidden labels, policy instructions, parsers, metric definitions, weights, logs, annotations, or results could be independently inspected or replayed. The paper is the only primary evidence reviewed here.

## Bottom line

SovereignPA-Bench identifies a real measurement omission: successful completion can coexist with stale-preference use, unnecessary disclosure, absent consent, unsupported claims, manipulation uptake, over-concession, bad escalation, or excessive confirmation burden. Its strongest reusable design move is to place **current user intent, remembered preference, platform/counterparty pressure, visible evidence, consent/privacy policy, and tool context in separate state fields**, while keeping evaluator labels out of the agent-visible prompt. Reporting utility and risk components separately is also preferable to a completion-only score.

But the paper does not yet establish an executable benchmark of user sovereignty. It reports frozen prompt-response generations and parsed actions, not actions in a service, browser, operating system, or stateful simulator. No tool protocol, transition system, initial/final state, attempted-versus-realized action record, parser specification, or environment evidence is described. “HiddenLabels” are still an author-defined oracle despite the paper calling the schema “no-oracle.” The 120 synthetic scenarios have no documented sourcing, construction protocol, independent user/expert review, rejected-item inventory, or affected-party authority. The exact metric predicates and weights are omitted, and the unavailable human-audit package is not shown to validate automatic scoring.

The intervention comparison is also co-designed with the instrument. `FullSovereign` explicitly prompts the same current-intent, consent, privacy, evidence, manipulation, escalation, and auditability concepts that define the authored score, then is compared once per scenario–model cell with weaker or partial prompts. Its higher score demonstrates alignment between one bundled scaffold and its own benchmark vocabulary on synthetic prompt responses; it does not isolate a general sovereignty capability, user representation, safer tool action, or improved user outcome.

The durable transfer to skill-bench is therefore an **authority–mediation–action ledger**, not a new sovereignty scalar: preserve who can set or revise intent, what evidence establishes current authority, what a counterparty/platform can propose versus authorize, what disclosure/action consent covers, which observations reach the agent, what action is attempted and realized, what burden and utility result, and which affected party validates the consequence. Do not let an evaluator-authored ideal action inherit the authority of a real user.

## Relevance to skill-bench and research question

This is narrow expansion serving charter objectives A and B. Personal agents are a methodological case, not a scope commitment. The general question is how a knowledge-work benchmark should evaluate representative action when current instructions, historical context, third-party incentives, evidence quality, permission, and interaction burden conflict.

The paper asks whether personal agents preserve “user sovereignty”—current interests, privacy, consent, evidence, low burden, and resistance to manipulative incentives—rather than maximize immediate completion (pp. 1–2). The auditable question is narrower: on 120 author-designed text scenarios, do four named model families produce parsed responses that score better under a bundled prompt naming the benchmark’s criteria than under seven weaker or partial prompt policies?

## One-sentence contribution

SovereignPA-Bench turns conflicts among current intent, stale memory, platform pressure, evidence, consent, and burden into separate prompt-state and scoring fields, but its unavailable author-defined oracle and non-executed parsed actions do not establish representative user action.

## Construct

The proposed scenario state is

`(current intent, memory, platform/counterparty pressure, visible evidence, consent/privacy policy, tool context)`

with an agent-visible `ObservableState` and evaluator-only `HiddenLabels` containing answer keys, risks, and violation conditions (pp. 2–3). An action receives positive components for task/agreement success, preference alignment, evidence grounding, and auditability, and penalties for privacy leakage, consent violation, over-concession, manipulation capture, and unnecessary burden (p. 3).

This decomposition is useful because it rejects three shortcuts:

1. more memory is not automatically better when memory is stale;
2. task completion is not legitimate action when permission or disclosure boundaries are violated; and
3. refusal or repeated confirmation is not automatically safe when it destroys utility or imposes avoidable burden.

The unique insight is that **representation is a conflict-resolution problem among differently authorized signals**, not just retrieval plus task execution. A remembered preference, current request, platform recommendation, visible receipt, consent boundary, and escalation channel have different issuers, validity times, purposes, and powers. Their presence in one prompt does not make them commensurate facts.

However, “user sovereignty” is not independently established as a single construct. It combines correctness, preference fidelity, privacy norms, consent procedure, evidentiary standards, resistance to persuasion, negotiation posture, escalation policy, auditability, and burden. These can conflict across users and contexts. Calling the combination sovereignty does not supply a user utility function, legal policy, professional standard, or affected-party threshold. The paper acknowledges that its aggregate is only a reporting index (pp. 3, 6, 9), but still uses that index as the primary policy-ranking outcome.

## Methodology and system

### Scenario construction and sampling

The suite contains 120 synthetic scenarios in eight named domains: preference evolution, privacy boundary, consent boundary, evidence grounding, refund negotiation, platform integrity, platform appeal, and support escalation. A “hard” subset concentrates stale preference/current-intent conflicts, useful but privacy-risky information, low-friction settlement pressure, missing evidence, and obstructed escalation (pp. 3–5, 10).

The paper is admirably explicit that this is a compact stress suite rather than a broad or naturalistic sample. But it gives no construction method beyond “carefully designed”:

- no source frame, search protocol, real incident/user trace, or domain standard;
- no number of candidates, rejection reasons, deduplication, or template clusters;
- no scenario counts by domain or hard-set admission rule;
- no authoring instructions, generator identity, or LLM contribution boundaries;
- no independent reconstruction of current intent, allowed disclosures, evidence sufficiency, reasonable concession, manipulation, escalation, or burden;
- no participant, user, privacy expert, consumer advocate, platform representative, or affected-party review; and
- no transformation lineage from a real norm or policy into `HiddenLabels`.

The sole author reports LLM assistance in ideation and code guidance (p. 7), but the amount and location are unspecified. Consequently, the suite is evidence of one authored normative stress design, not user demand, natural conflict prevalence, legally valid consent, representative platform behavior, or professional consensus.

### Policy baselines and configured systems

Eight prompt policies are compared (p. 3):

- `Direct` prioritizes immediate completion;
- `Memory` adds preference and memory updates;
- `Consent` prioritizes consent boundaries;
- `Evidence` emphasizes grounding;
- `SafetyPrompt` adds generic safety guidance;
- `ReActToolUse` emphasizes structured action;
- `LLMJudgeGuard` adds a judgment/guardrail prompt; and
- `FullSovereign` combines current intent, consent, privacy, evidence, manipulation resistance, escalation policy, and auditability.

The four model rows are Claude 3.7 Sonnet (2025-02-19), Gemini 2.5 Pro Preview, GPT-4.1 (2025-04-14), and Llama 3.3 70B Instruct (p. 4). Each model–scenario–policy cell appears to have one frozen response: `120 × 4 × 8 = 3,840`.

This is a useful paired layout because policies see the same scenario–model units. It is not a component ablation or capability comparison. The policies are non-orthogonal, semantically nested, and likely differ in length, explicit criteria, requested output structure, deliberation, and grader-cue exposure. The exact prompts are unavailable. `FullSovereign` names essentially every scored dimension, so the study measures a configured instruction package whose content was designed around the instrument. There is no independent rubric, held-out synonym/form, unseen domain, unrelated negative control, semantic prompt-equivalence check, token-budget control, or factorial decomposition.

Configured-system identity is incomplete: provider endpoints, system messages, decoding parameters, context limits, tool schemas, response format, parser/retry policy, run dates, token budgets, latency, cost, and open-weight serving stack are absent. One run per cell supplies no within-condition repeatability or expected-risk estimate.

### “Executable” environment and action evidence

The paper says scenarios contain tools and models choose actions, but reports only prompts, outputs, provider-form files, and **parsed actions** (pp. 2–3, 7, 9). It does not define an API, action grammar, simulator, service state, transition function, execution log, or initial-to-final state check. The ethics statement confirms there are no real accounts, emails, payments, or platform actions (p. 7).

This matters because proposed and realized behavior are different:

- drafting a private disclosure is not sending it;
- requesting consent is not obtaining valid consent;
- citing a receipt is not using it successfully in an appeal;
- selecting escalation is not reaching a human channel;
- rejecting a sponsored option is not preserving downstream alternatives; and
- emitting an audit note is not creating a durable, accurate audit trail.

Without execution, the instrument can score intended/proposed action in text. It cannot establish tool competence, state consequence, prevented harm, successful negotiation, reversibility, collateral effects, or recovery. “Executable benchmark” and “trajectory” overstate the described artifact.

### Hidden labels, automatic metrics, and aggregate score

The paper’s information firewall is directionally sound: policies receive `ObservableState`; evaluator-only answer/risk labels are applied after generation (pp. 2–3). But a private label is still an oracle. Calling the formulation “no-oracle” appears to mean no oracle leakage to the policy, not absence of an oracle.

Central scoring details are missing:

- exact component predicates and value ranges;
- metric weights `w_i` and penalties `λ_j`;
- parser rules from free-form output to action;
- handling of multiple, conditional, malformed, refused, or unparseable actions;
- evidence required to label alignment, unsupported claim, manipulation, concession, escalation, burden, or auditability;
- overlap/dependence among components;
- missing/invalid-run treatment; and
- bootstrap resampling unit and replicate count.

The appendix states that task-heavy, privacy-heavy, and burden-heavy reweightings preserve the `FullSovereign` rank, but supplies neither weight vectors nor tables (pp. 9–10). Rank robustness across undisclosed hand-chosen alternatives does not validate the aggregate or its decision threshold. The very narrow bootstrap intervals around means reflect repeated authored rows; they do not address uncertainty from scenario construction, normative labels, policy prompts, parser error, model stochasticity, or generalization to new users and conflicts.

### Human audit

Three blinded annotators label 240 items, producing 720 labels. Reported Fleiss κ is .702 for privacy leakage, .852 for consent violation, .578 for unsupported claims, .470 for over-concession and bad escalation, and .397 for manipulation capture (pp. 4–6). This is valuable evidence that the latter judgments are less repeatable under the undisclosed audit protocol.

Yet the audit cannot be treated as automatic-metric calibration from the paper alone. It does not report:

- who annotators were or what authority/expertise they had;
- recruitment, compensation, training, rubric, examples, or adjudication;
- whether each item included scenario state, policy prompt, output, parsed action, or hidden labels;
- how 240 items were sampled across 3,840 runs, domains, models, policies, and outcomes;
- whether annotators labeled automatic-metric dimensions independently or saw author labels;
- accuracy, precision/recall, confusion matrices, prevalence-adjusted uncertainty, or disagreements between automatic and human labels;
- whether the same scenario appeared under several policies, violating nominal item independence; or
- raw labels and timestamps.

Agreement among three unknown annotators on authored text scenarios supports panel-relative repeatability for the displayed categories. It does not establish contextual-integrity norms, valid consent, user endorsement, manipulation truth, or that the automatic score is calibrated.

## Evidence and bounded findings

Table 2 reports mean `SovScore` from .759 (`Direct`) to .820 (`FullSovereign`), with `FullSovereign` privacy leakage .011, consent violation .009, evidence grounding .879, and task success .753. `Direct` has slightly higher task success (.767) but worse reported risks. On paired scenario–model units, `FullSovereign` beats `Direct` on 451 of 466 non-tied pairs and `LLMJudgeGuard` on 232 of 299 (pp. 4–5). The same rank order is reported across the four model families and the 128-run-per-policy hard subset.

These results support only bounded descriptive claims:

1. Under the authors’ parser and metric, a bundled prompt naming the complete criterion set scored highest on these synthetic prompts across the four model rows.
2. Completion and authored risk labels can diverge; a completion-only report would hide dimensions the benchmark designers care about.
3. The paired design reduces between-scenario noise for comparisons among the eight prompt packages on the fixed suite.
4. Three annotators were more repeatable on privacy/consent labels than manipulation/escalation labels under the unreleased protocol.
5. The paper describes an unusually complete artifact layout, even though that artifact is currently unavailable for inspection.

The evidence does **not** establish:

- that `FullSovereign` improves outcomes for real users;
- valid representation of current user intent or affected-party preferences;
- consent validity under law, policy, power imbalance, revocation, or delegated authority;
- actual privacy protection, evidence use, negotiation success, escalation, or tool safety;
- manipulation detection rather than agreement with author framing;
- causal effects of individual scaffold components;
- general sovereignty capability or comparison among foundation-model families;
- prevalence, severity, frequency, or loss from the represented risks;
- cross-user, cross-cultural, cross-platform, professional, or production validity; or
- deployment fitness or readiness.

## Unique insight: authority and mediation must survive the whole action chain

The paper’s six-part state should become a typed chain rather than a flat prompt object:

1. **principal and affected parties** — whose interests and rights are at stake;
2. **intent claim** — request/preference, issuer, scope, valid time, confidence, and revocation/supersession relation;
3. **memory evidence** — original event, transformation, staleness, authorization, and current applicability;
4. **platform/counterparty proposition** — informational claim, incentive, recommendation, demand, obstruction, or permitted offer, without assuming authority over the user;
5. **evidence state** — provenance, visibility, sufficiency, contradiction, and permitted use;
6. **consent state** — actor, action, object/data, recipient, purpose, scope, duration, revocability, and whether confirmation is required or already valid;
7. **public action basis** — what the visible state authorizes or leaves unresolved;
8. **legitimate terminal set** — inspect, draft, ask, act, negotiate, appeal, escalate, defer, refuse, or preserve alternatives;
9. **attempted action/disclosure** — proposed tool call, recipient, payload, scope, and rationale;
10. **policy/environment decision** — allowed, blocked, transformed, or unavailable;
11. **realized state and information flow** — actual mutation, disclosure, counterparty response, residual risk, and reversibility;
12. **utility and burden** — completion, delay, confirmations, attention, opportunity loss, and correction work;
13. **affected-party review** — whether the result served the principal and respected other legitimate claims; and
14. **bounded verdict** — observed policy adherence, unresolved disagreement, invalid environment, and the claim ceiling.

No link inherits the next. Current-looking text need not come from an authorized principal. A platform offer can be real but manipulative or simply legitimate bargaining. A request for consent can be unnecessary burden; a recorded “yes” can be invalid for the actual payload or recipient. A proposed safe action can fail in execution. An author-approved outcome can remain unacceptable to the represented user.

This chain generalizes to assistants handling workplace files, client communications, approvals, vendor negotiation, research evidence, finance operations, and organizational escalation without making personal agents the benchmark’s scope.

## Limitations and validity threats

1. **No inspectable benchmark release.** The claimed artifact has no public locator, so scenarios, prompts, labels, code, metrics, annotations, and runs are unauditable.
2. **Unspecified synthetic authoring.** No source frame, candidate inventory, templates, rejection rules, or independent scenario review is reported.
3. **No user authority.** No user, affected party, domain expert, privacy expert, or consumer representative validates intended actions or tradeoffs.
4. **Normative construct bundling.** “Sovereignty” combines heterogeneous and potentially conflicting values without an empirically supported composition rule.
5. **“No-oracle” misdescription.** `HiddenLabels` contain answer keys and violation conditions; they are a private authored oracle, merely withheld from the policy.
6. **Not demonstrated executable.** The described evidence stops at text outputs and parsed actions, with no action runtime or state-transition validation.
7. **Unspecified tools.** Tool context, action space, action syntax, affordances, failure modes, and execution semantics are absent.
8. **Parser validity unknown.** No parsing protocol, malformed-output handling, parser audit, or alternative-expression test is reported.
9. **Metric definitions missing.** Component predicates, weights, penalties, dependencies, thresholds, and missingness rules are unavailable.
10. **Intervention–instrument co-design.** The strongest policy explicitly names the same concepts used to score it.
11. **Bundled, nonfactorial policies.** Prompt length, structure, deliberation, tools, safety cues, and criterion disclosure vary jointly.
12. **No independent measurement.** There is no held-out rubric, evaluator vocabulary, scenario form, or downstream outcome.
13. **One apparent run per cell.** The exact 3,840 count leaves no repeated stochastic trials within model–scenario–policy cells.
14. **Incomplete configured identity.** Prompts, decoding, endpoints, dates, tool contracts, budgets, retries, costs, and serving stack are missing.
15. **Potential template clustering.** Scenario dependence is not characterized; bootstrap/sign tests treat authored units more cleanly than source/template uncertainty permits.
16. **Sign-test estimand is narrow.** Extremely small p-values describe fixed-suite prompt-policy ordering, not effect transport to new users or environments.
17. **Undisclosed reweightings.** Robustness claims cannot be checked and do not cover plausible stakeholder-specific loss functions.
18. **Audit sampling unknown.** The 240-item selection may not represent domains, policies, models, errors, or difficult disagreements.
19. **Audit authority unknown.** Agreement among three unspecified raters is not user validation or normative truth.
20. **No human–automatic calibration.** Agreement is reported among humans, not between human labels and the automatic benchmark metrics.
21. **Manipulation remains weakly observed.** κ=.397 underscores framework dependence; no independent platform-pressure ground truth exists.
22. **Burden is asserted, not operationalized in the paper.** No time, turns, interruptions, cognitive work, user corrections, or measured experience are reported.
23. **No severity or consequence model.** Binary leakage/violation rates do not capture recipient, sensitivity, persistence, reversibility, loss, or remediation.
24. **No population claim.** Eight stress categories and 120 authored items do not represent personal-agent use, platforms, cultures, or professional work.
25. **No longitudinal user state.** “Evolution” is supplied within a scenario, not accumulated through persistent interactions and verified updates.

## Reproducibility and operational realism

Conceptual reproducibility is low to moderate. The paper names state fields, policy families, model rows, dimensions, paired analysis, and a desirable artifact layout. Another group could construct a related stress suite.

Exact reproducibility is poor. The artifact is unavailable; prompts, scenarios, labels, parsers, metrics, weights, raw runs, annotations, environment, and analysis code cannot be inspected. The manuscript’s figures and tables are generated from included source files, but they contain reported aggregates rather than primary run evidence.

Operational realism is low. Conflicts among stale memory, current intent, private context, evidence, negotiation pressure, and escalation obstruction are plausible. But all scenarios are synthetic and text/tool based; no account, email, payment, platform, recipient, tool action, or persistent environment is touched (pp. 6–7). There is no actual consent interaction, service response, information transfer, action consequence, correction loop, or user outcome. This is best treated as an unreleased prompt-policy stress test, not a production personal-agent benchmark.

## Transfer to skill-bench

1. **Retain typed signal roles.** Current instruction, remembered preference, third-party pressure, evidence, permission, and tool affordance need separate issuers, authority, valid time, purpose, and supersession relations.
2. **Keep utility and risks plural.** Completion, alignment, evidence, privacy, consent, manipulation, concession, escalation, auditability, and burden should remain criterion-level observations until an explicit stakeholder/loss policy aggregates them.
3. **Separate disclosure from consequence.** A public skill may teach privacy/consent procedure, but independent checks must inspect attempted payload, recipient, purpose, actual transfer, residual state, recovery, and user-visible result.
4. **Add current-versus-stale contrast families.** Use matched cases where memory is current, superseded, ambiguous, or unauthorized; include negative controls where using memory is appropriate so generic refusal does not look safe.
5. **Cross consent necessity with burden.** Include valid standing permission, action-specific confirmation, revocation, excessive confirmation, and unanswerable confirmation cases; grade useful completion and burden separately.
6. **Treat platform mediation as typed evidence, not an adversarial label.** Test legitimate recommendations, disclosed incentives, misleading pressure, blocked escalation, and uncertain cases. Preserve disagreement rather than forcing every concession into manipulation.
7. **Require affected-party and domain authority.** Author hidden labels do not become user interests. For consequential pilots, independently validate action boundaries, acceptable alternatives, and loss/severity with people authorized for those claims.
8. **Evaluate realized action.** A benchmark that claims consent-aware agency must execute in an inert or safely isolated stateful environment and preserve proposal → policy decision → state/information-flow consequence → recovery evidence.
9. **Factor interventions.** Cross guidance dimensions prospectively, repeat cells, use held-out forms and independent graders, and preserve `insufficient`/disagreement outcomes. Do not infer general transfer from a scaffold optimized for its own rubric vocabulary.
10. **Bound the claim.** A successful slice can establish that one configured system selected independently reviewed actions on versioned synthetic conflict cases. It cannot alone establish faithful representation, user benefit, professional competence, privacy safety, production fitness, or readiness.

## Concrete repository actions

No new build or consolidation task is added. Existing participation/consent, authority and information-flow, expertise-transfer, task-projection, artifact/state, action-safety, metric, task-health, validity, trace, and root/surface contracts already host the authority–mediation–action chain. A personal-agent or “sovereignty” schema would duplicate these primitives and risk canonizing one author’s normative aggregate.

When the queued second-pilot reliability work or a future diverse pilot next exercises consequential communication, include one current-versus-stale authority contrast and one necessary-versus-burdensome consent contrast, while retaining actual information-flow/state evidence. This is a fixture refinement, not a new queue task.

## Assessment

**Evidence tier:** full immutable paper with reported synthetic prompt-policy results and human inter-rater statistics; claimed benchmark/run/audit artifact unavailable.  
**Most reusable contribution:** separate current intent, memory, platform pressure, evidence, consent/privacy policy, and tool context, then report completion and risk dimensions separately.  
**Most serious flaw:** the complete scaffold and the hidden metric are co-designed around an unreleased author-defined oracle, while “execution” stops at parsed text actions and no represented user validates the normative labels.  
**Claim skill-bench may safely make:** representative knowledge-work action should preserve typed authority, evidence, consent, mediation, attempted and realized consequence, utility, burden, and affected-party review as separate links; a hidden-label prompt-policy score cannot by itself establish user sovereignty, benefit, safety, professional validity, production fitness, or readiness.
