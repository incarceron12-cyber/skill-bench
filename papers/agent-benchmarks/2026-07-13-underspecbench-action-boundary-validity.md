# UnderSpecBench: fixing the intended action does not isolate safe judgment when the prompt changes its authorization basis

**Source.** Zimo Ji et al., *Coding Agents Are Guessing: Measuring Action-Boundary Violations in Underspecified DevOps Instructions*, arXiv:2607.02294v1 (2 July 2026), <https://arxiv.org/abs/2607.02294v1>.

**Full text read.** Immutable 12-page v1 local PDF: `data/papers/pdfs/2607.02294v1-underspecbench.pdf` (SHA-256 `cfe99b67d28fc7a797000eecc1c00e7cdbb2ad3bd8ab4e7a8e138118ab3270b8`). Complete local text extraction (`pdftotext -layout`): `data/papers/text/2607.02294v1-underspecbench.txt` (SHA-256 `494c434acad0290234820c541078c63a4a87f2819edc2372a1542780d7517bea`). Date read: 2026-07-13.

**Release search.** The immutable paper contains no benchmark repository, dataset DOI, project URL, or pinned revision, although its conclusion says the benchmark, oracles, and harness are released (p. 11). Searches for the exact benchmark name and title found the paper and third-party commentary, but no verifiable author- or institution-owned release. Therefore there is no local release snapshot and no independent task/oracle/result audit. The paper is the only primary evidence reviewed here.

## Bottom line

UnderSpecBench contributes an unusually useful controlled-task pattern: preserve one seeded world and one author-designated safe state transition while perturbing the request's **action, object, and environment/scope attributes**, then score intended change, wrong target, and excess scope separately. That pattern directly advances skill-bench's evaluation of hidden requirements and calibrated clarification.

But the paper does not establish that current agents violate action boundaries in 55.8–67.8% of a representative population, nor that ambiguity alone causes the reported changes. Its 2,208 prompts are a hand-authored, mechanically transformed census of 69 synthetic families, evaluated apparently once per configured system. The prompt manipulations are not semantically validated; the target and blast-radius factors can change what is publicly authorized while the private oracle remains fixed; the axes are not shown to be orthogonal; and no matched alternative-valid-action or permission-policy condition is included. Deterministic scoring makes authored predicates reproducible, not necessarily complete or professionally correct.

The most important design correction for skill-bench is an **authorization-state perturbation contract**: every prompt variant must separately record what action is intended privately, what action is actually licensed by public evidence, what uncertainty is resolvable from the workspace, which terminal actions are legitimate, and what observer evidence can distinguish them. Holding the private answer fixed is not enough.

## Why this matters: charter relevance and research question

This is narrow expansion serving charter objectives A, B, and C. DevOps is a methodological case, not a benchmark scope boundary. The general question is whether a configured agent, given an incomplete request for consequential work, selects a justified action boundary rather than merely producing a plausible state change.

The paper asks how benign instruction underspecification affects action propensity, action quality, non-action disposition, and over-scope behavior across five model–harness configurations (pp. 1–2, 6–9). The auditable question is narrower: on 69 author-constructed container tasks, under fully autonomous no-confirmation policies and author-defined single-safe-action oracles, how do observed state transitions vary across 32 mechanically derived prompt forms?

## One-sentence contribution

UnderSpecBench turns request completeness into a controlled perturbation and observes whether an agent changes the intended object and no more—but it does not validate that the fixed private action remains publicly authorized across those perturbations.

It offers:

1. 69 task families over four DevOps domains and nine operational control surfaces, each said to be grounded in an incident, CVE, news report, or tool documentation (pp. 3–4);
2. a `4 intent × 4 target × 2 blast-radius` prompt matrix, yielding 2,208 variants while environment, tools, and oracle are held fixed (pp. 4–5);
3. isolated network-restricted containers with real, hybrid-emulated, or mock command surfaces (p. 5);
4. three side-effect signals—`INTENDED`, `WRONG_TARGET`, and `OVERSCOPE`—plus safe-success, overstep, and under-completion aggregates (pp. 5–6); and
5. an LLM-judged decomposition of no-action outputs into ask, refuse, and defer, checked against 100 human labels (pp. 6, 8).

Its distinctive move is to make **action-boundary selection** observable in world state instead of treating any apparent completion as success.

## Methodology and system

### Source frame and authoring

Table I enumerates 69 families across work governance, repository state, dependencies, build outputs, quality gates, release orchestration, artifact state, deployment/traffic, and infrastructure/observability (pp. 3–4). Sources are heterogeneous: incidents, CVEs, issue reports, documentation, blogs, and news. A source reportedly establishes destructive semantics and an intended target or scope boundary; the authors then simplify it into a synthetic operation (pp. 3–4).

This is **incident-inspired authoring**, not incident sampling. The paper gives no search protocol, candidate count, inclusion/exclusion criteria, frequency weighting, author expertise, independent professional review, expert solve, rejected family inventory, or incident-to-task transformation record. Many cited sources establish tool behavior rather than an observed failure. Thus “grounded” supports face plausibility for named operations, not representativeness, frequency, severity, or professional consensus.

### Prompt transformation

Each family starts with one hand-written `S0 B0 R0` baseline. The other 31 prompts are mechanically produced by slot substitution (p. 4):

- `S0…S3` progressively weaken action and environment cues;
- `B0…B3` weaken unique target binding; and
- `R0/R1` place the operation on contained versus shared/production surfaces.

The authors map these to ABAC action, object, and environment attributes, with subject fixed (pp. 4–5). They state that axes perturb only natural language while environment, tools, and oracle remain fixed.

That design creates a clean **instrument identity**, but not automatically a valid causal treatment. If `R1` says or implies production while the seeded world and required action remain unchanged, the prompt may alter authorization, expected confirmation, or perceived environment without altering actual consequence. If higher `B` leaves multiple candidates, the private designated target may no longer follow from public evidence. If higher `S` strips the requested operation, acting may be unjustified even when the oracle calls the same state change “safe.” The paper reports no human semantic checks for axis monotonicity, cross-axis orthogonality, naturalness, answerability, public basis, or unchanged legitimate action.

### Environment, tools, and oracle

Each family reportedly runs in an isolated network-restricted Docker container. Git, Make, and ordinary file operations can use real binaries; selected package commands are hybrid emulations; heavy services such as Kubernetes use mocks designed to reproduce command surface, flags, output, exit codes, validation, and state transitions (p. 5). Agent-visible runtime files are separated from agent-invisible reset scripts, initial state, oracle, acting identity, and prompts.

The oracle compares before/after state, command logs, and structured service effects against intended and protected/over-scope sets (pp. 5–6). `INTENDED` recognizes the designated state change; `WRONG_TARGET` recognizes change to another/protected object; `OVERSCOPE` recognizes a broader or more destructive operation. A run can trigger wrong-target and over-scope simultaneously.

The paper does not provide task-level predicates, mock conformance tests, tool/version hashes, container digests, network-canary results, action-trace schema, timeout policy, or accepted alternative transitions. It also slides between two definitions of over-scope: touching the protected set and using an over-broad command, even if the final state is contained. Those require different observations and consequence interpretations.

### Configured systems and permission policy

Five configurations are tested (p. 6): OpenCode with Haiku 4.5, Codex 5.1 mini, or DeepSeek v4; Claude Code with Haiku 4.5; and Codex with Codex 5.1 mini. All use full autonomous execution with per-action confirmation disabled (pp. 5–6).

This is valuable configured-system evaluation, and same-model/different-harness pairs reveal large descriptive differences. However, exact model snapshots, provider, model parameters, scaffold versions, native prompts, tool schemas, clarification affordances, context policy, budgets, retry policy, and run dates are absent. The paper conjectures that Codex's higher ask rate comes from a first-class ask-user affordance (p. 8), but does not inspect or intervene on that mechanism.

No gated, least-privilege, read-only, dry-run, or policy-mediated condition is tested. The study therefore measures behavior under one deliberately permissive action policy; it cannot estimate the safety benefit of permission design or support the recommendation that particular control surfaces should retain a human gate.

### Runs, missingness, uncertainty, and cost

Every configuration is described as running the full 69 × 32 matrix (p. 6), implying one apparent attempt per cell and 11,040 nominal runs overall. The paper never states repetition count explicitly, supplies no per-run inventory, and reports percentages over “scored runs” without defining exclusions. It gives no failed launch, timeout, API error, malformed trace, oracle error, retry, replacement, or invalid-run policy. No costs, token usage, latency, confidence intervals, paired tests, task-family clustering, multiplicity treatment, or random seed policy are reported.

The 2,208 variants are not 2,208 independent task families. Prompt rows cluster tightly within 69 seeded worlds, and families cluster within authoring/source/control-surface groups. Run-weighted pooling and conditioning on action further change the estimand. Treating cell percentages as precise population rates would be pseudoreplication.

## Scoring and evidence

Safe Success requires intended action with neither wrong target nor over-scope. Overstep is wrong-target or over-scope. Under Completion means none of the three signals fired (pp. 5–6). These are sensibly plural observations, although “Action Rate” is effectively the complement of under-completion under the oracle's recognized signal space, not necessarily every attempted action.

For no-action runs, DeepSeek-v4-flash labels final messages as ask, refuse, or defer. One blind human labels 100 stratified cases; the paper reports 85/100 agreement, seven `UNCLEAR`, and Cohen's κ = .860 after excluding those seven (p. 8). This supports limited repeatability of three lexical/semantic disposition labels on selected non-action outputs. It does not validate whether asking was answerable, sufficient, correctly targeted, or safe; whether refusal was professionally justified; or whether deferment preserved useful partial work. Excluding unclear cases inflates the cleaner agreement estimand, and one annotator cannot establish inter-human reliability.

## Reported results and claim limits

Across all runs, Table II reports Safe Success of 15.5–36.8%, Wrong Target of 13.1–31.8%, OverScope of 24.9–44.4%, and Overstep of 27.0–46.3% (p. 7). The abstract's 55.8–67.8% boundary-violation range conditions on acted runs, not all scored runs (pp. 1–2). This denominator distinction matters: a cautious but unhelpful system and an active unsafe system have different operational profiles.

Pooled acted-run Safe Success falls from 67.9% at `B0` to 8.6% at `B3`; Wrong Target rises from 9.6% to 75.1%; OverScope rises from 31.4% to 87.0% (pp. 6–7). Action rates barely differ across `R0/R1` (65.5%/64.0%), and acted-run quality is also flat (p. 7). Runtime control surfaces show much higher OverScope than bounded-object surfaces (p. 9).

These are descriptive associations in this authored, single-policy matrix. Several stronger interpretations are not licensed:

- **“Target ambiguity causes guessing.”** Prompt levels are not validated, runs are apparently single attempts, axes may interact, and high-`B` prompts may remove the public basis for any unique action. The result does show oracle-disagreement after weakened target cues.
- **“Blast radius does not affect caution.”** `R` has only two unvalidated forms. The actual container consequence is fixed and synthetic, so the manipulation may communicate a label rather than instantiate different downside. A null descriptive slope is not evidence of equivalence.
- **“Shared control planes structurally cause over-scope.”** Control surface, task family, command semantics, mock design, oracle breadth, and source grounding vary jointly. Only three families populate one highlighted surface (p. 10). There is no within-family bounded/shared intervention supporting causality.
- **“55.8–67.8% violate a boundary.”** This is acted-run conditional prevalence on retained authored prompts, not deployment incident probability or a representative task-population rate.
- **“Full autonomy is reasonable for bounded objects.”** Safe Success is only 24–35% on those surfaces and no harm/cost, policy intervention, or production validation is measured (p. 9). Lower relative over-scope does not establish acceptable autonomy.

## Unique insight: private intended action, public authorization, and observer verdict are different states

UnderSpecBench's fixed-oracle perturbation exposes a deeper benchmark problem. A task can preserve the same **private intended transition** while changing whether that transition is **licensed by the public request**. These must be modeled separately:

1. `private_intent`: the author's or user's actual desired action and target;
2. `public_authorization`: what action, target, scope, and environment the visible evidence authorizes;
3. `resolvable_uncertainty`: what the agent can determine from tools without asking;
4. `legitimate_terminal_set`: execute, inspect, dry-run, clarify, defer, refuse, or escalate, including alternate safe paths;
5. `attempted_action`: command/tool invocation and proposed target/scope;
6. `realized_effect`: state diff and collateral consequences;
7. `observer_coverage`: which attempts and effects the oracle can actually see; and
8. `verdict`: intended, wrong-target, over-scope, insufficient evidence, invalid environment, or acceptable alternative.

A deterministic oracle can faithfully recognize the author's intended transition while still misclassifying professionally legitimate restraint or an alternative safe action. Conversely, it can miss dangerous attempts blocked by the mock or hidden outside the diff. The key construct is not agreement with private intent; it is **calibrated action selection under the authorization state visible to the agent**.

This yields a stronger factorial design for skill-bench: cross instruction specificity with authority completeness and consequence/permission policy, while using positive and negative near-neighbors. Include cases where asking is required, cases where workspace inspection resolves ambiguity, cases where conservative execution is authorized, and cases where unnecessary asking imposes cost. Otherwise “always ask” can look safe and “always act” can look capable without measuring calibration.

## Comparison with adjacent reviewed evidence

- **ClawSafety** (`papers/agent-benchmarks/2026-07-10-clawsafety-cross-domain-injection-validity.md`) varies adversarial source content and asks whether unauthorized instructions become realized harm. UnderSpecBench instead varies benign request completeness. Both need the same exposure → adoption → attempt → realization ledger, but UnderSpecBench uniquely adds reference/target ambiguity. ClawSafety's utility omission warns against treating non-action as safety.
- **AARRI-Bench** (`papers/agent-benchmarks/2026-07-11-aarri-research-judgment-lifecycle.md`) makes refusal, stopping, dissent, and clarification legitimate professional outcomes when evidence changes the correct action. UnderSpecBench classifies these dispositions but does not grade whether each was the right consequence. AARRI's lexical-verifier defects reinforce the need to separate terminal-action substance from wording.
- **KWBench** (`papers/agent-benchmarks/2026-07-11-kwbench-unprompted-problem-recognition.md`) tests whether an agent changes framing before execution. Its missing framed control motivates an UnderSpecBench-style matched perturbation, while its absence of positive/negative neighbors shows why ambiguity tasks need both “ask” and “act” cases.
- **Consulting cognitive traps** (`papers/agent-benchmarks/2026-07-10-consulting-cognitive-traps.md`) links a novice shortcut to an expert cue and downstream decision consequence. UnderSpecBench supplies a complementary request-boundary perturbation, but lacks the expert-validation and alternative-procedure adjudication needed to make each private oracle professionally authoritative.

Existing action-safety, authority-lineage, benchmark-bundle, validity, task-health, metric, execution-isolation, and evaluator-observation contracts already provide homes for these records. A DevOps-specific schema would duplicate them.

## Limitations and validity threats

1. **No verifiable release.** Despite the release claim, no official task, prompt, oracle, harness, trace, or result repository is linked or discoverable; central claims cannot be independently replayed.
2. **No representative sampling frame.** Sixty-nine families are selected and simplified from heterogeneous public sources without candidate inventory, prevalence weights, or inclusion rules.
3. **Unvalidated transformations.** Mechanical slot substitution is not checked for naturalness, monotonicity, orthogonality, changed presuppositions, answerability, or equivalent public authorization.
4. **Private-intent fairness gap.** The designated target/action stays fixed after visible evidence may cease to identify or authorize it.
5. **Single valid path.** The authors acknowledge defensible alternatives may be rejected (p. 10); no alternative-path discovery or adjudication protocol exists.
6. **Oracle completeness is unevidenced.** Hand-written deterministic checks may miss attempted, indirect, delayed, or semantically equivalent effects; no mutation, soundness, completeness, or observer-canary study is reported.
7. **Mixed environment fidelity.** Real, hybrid, and mock tools have no published conformance tests, and container/network isolation is asserted without evidence.
8. **One permissive permission condition.** Full autonomous no-confirmation execution cannot support policy-effect or ordinary gated-deployment claims.
9. **Incomplete configured-system identity.** Exact model, scaffold, prompt, tool, budget, provider, and execution versions are absent.
10. **No repeated-run reliability.** Apparent one-shot cells provide no stochastic stability, replicate disagreement, or expected-risk estimate.
11. **No invalid/missing policy.** “Scored runs” is undefined, and infrastructure failures may be silently excluded or treated as behavior.
12. **No clustered uncertainty.** Prompt variants share task state and oracle; families share surfaces and authoring. Pooled cell rates do not quantify generalization to new tasks.
13. **Condition-on-action selection.** Acted-run quality is operationally useful but compares selected subsets whose composition changes across prompt levels and systems.
14. **Weak blast-radius intervention.** Two prompt levels do not instantiate actual consequence severity; null slopes cannot establish insensitivity to real downside.
15. **Control-surface confounding.** Runtime versus bounded categories differ in task semantics, mocks, oracle breadth, and family count—not only sharedness.
16. **Non-action validity is narrow.** One human and an LLM judge classify wording, not whether clarification/refusal/deferment was substantively appropriate or useful.
17. **No human baseline.** Experts are not tested under identical ambiguity, workspace, permission, and time constraints.
18. **No cost or latency evidence.** Clarification burden, false abstention, intervention cost, and recovery value are not measured.
19. **Production claim ceiling.** Synthetic no-confirmation containers are stress tests; the paper itself acknowledges richer organizational context and gating (p. 10). They do not estimate incident rates or deployment safety.

## Reproducibility and operational realism

The conceptual package is inspectable enough to reconstruct the intended experiment: a fixed seeded world, prompt matrix, hidden oracle, and action traces. Network restriction, resettable containers, real binaries where feasible, and side-effect scoring are all stronger than final-answer-only evaluation.

Actual reproducibility is poor because the claimed release is not linked, task/oracle code is unavailable, run identities and exclusions are absent, and models/harnesses are incompletely pinned. Operational realism is deliberately limited: simplified single-turn tasks, synthetic/mock services, one private intended action, no organizational policy, no real approvals, and no measured consequence cost. The right interpretation is a proposed stress-test instrument with descriptive paper results—not a production safety audit.

## Transfer to skill-bench

1. **Add no new schema task.** Existing contracts can represent the needed records; duplication would obscure rather than clarify the action boundary.
2. **Require authorization-state records in future pilots.** For each variant, bind private intent, public action/object/environment attributes, resolvable workspace evidence, acceptable terminal actions, alternate valid paths, and prohibited consequences.
3. **Validate prompt transformations before agent trials.** Use blinded expert ratings and semantic checks for naturalness, monotonicity, factor isolation, public basis, answerability, and unchanged consequence. Reject variants that accidentally alter several factors.
4. **Use a calibration matrix, not only ambiguity escalation.** Cross `fully specified / resolvable by inspection / requires clarification` with `bounded / consequential` and `execute / gated` policies. Include matched cases where asking is unnecessary or costly.
5. **Grade a staged action ledger.** Preserve inspect → infer → ask/act → attempt → policy decision → state transition → collateral effect → repair, with explicit insufficient-observation and acceptable-alternative outcomes.
6. **Test oracle soundness and completeness.** Plant equivalent safe commands, alternative paths, blocked dangerous attempts, indirect effects, and no-op/false-positive traces. Record adjudications and instrument revisions in task-health records.
7. **Report the right estimands.** Keep all-run safe useful completion, calibrated clarification, over-refusal, wrong target, excess scope, invalid execution, and acted-run conditional quality separate; use repeated runs and task-family-clustered uncertainty.
8. **Bound claims.** A successful slice may support “this configured system selected authorized actions on these transformed synthetic tasks.” It cannot by itself support professional competence, cross-domain calibration, production safety, or incident-rate claims.

## Concrete repository actions

No new build or consolidation task is added. The evidence refines existing action-safety, authority-lineage, benchmark-bundle, task-health, validity, metric, execution-isolation, and evaluator-observation work. The next relevant pilot should implement the authorization-state calibration matrix and alternative-path oracle tests described above rather than creating a DevOps-specific contract.

## Assessment

**Evidence tier:** full immutable paper with descriptive configured-system results; no verifiable released instrument or run evidence.  
**Most reusable contribution:** fixed-world action/object/environment perturbations with state-based wrong-target and over-scope observations.  
**Most serious flaw:** the benchmark fixes the private safe action while prompt variants may change whether that action is publicly identifiable or authorized, without semantic or expert validation.  
**Claim skill-bench may safely make:** action-boundary evaluation should distinguish intended state change, public authorization, resolvable uncertainty, attempted action, realized consequence, and legitimate clarification/abstention rather than equating completion—or agreement with a private oracle—with safe judgment.
