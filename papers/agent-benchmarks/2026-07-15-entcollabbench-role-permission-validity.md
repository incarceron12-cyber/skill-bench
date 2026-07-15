# EntCollabBench: role-labeled execution is inspectable, but routing is not delegated authority and approval classification is not organizational approval

**Source type:** Deep review of the complete immutable arXiv v1 paper plus static audit of pinned official post-v1 code and dataset releases  
**Paper:** Tao Yu et al., *Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows*  
**Immutable paper:** https://arxiv.org/abs/2605.08761v1  
**Local PDF:** `data/papers/pdfs/2605.08761v1-entcollabbench.pdf` (45 pages; SHA-256 `7c6336a57ee5710379526df6dce2a6bab551cf96f0ef69998103077ac1a15446`)  
**Local text:** `data/papers/text/2605.08761v1-entcollabbench.txt` (SHA-256 `f28640c9b9397176c420fff222b1c64fe1a91ab2f6d279fc3660eeffb33c22e5`)  
**Official repository:** https://github.com/yutao1024/EntCollabBench  
**Pinned code archive:** `data/sources/releases/2605.08761v1-entcollabbench/yutao1024-EntCollabBench-9d085fc.zip` (commit `9d085fcb86adaf20254c09e2ca35123e535a9643`; 1,770 archive entries; SHA-256 `8a021c2579d4c52186dd463a95e5081b23fb4a5699cbee9016defd14fe6872d9`)  
**Pinned dataset revision:** Hugging Face revision `df95c87317863d507f229df190b2c0a29c4e4afc`; four JSON task files preserved under `data/sources/releases/2605.08761v1-entcollabbench/`  
**Release provenance:** `data/sources/releases/2605.08761v1-entcollabbench/provenance.json`  
**Date read/audited:** 2026-07-15 UTC

> **Timing and execution boundary.** The immutable paper is dated 9 May 2026. The pinned code and dataset revisions were observed later and are evidence about an official post-v1 implementation, not proof of manuscript-time implementation identity. This review inspected the full paper, all 300 released task records, authorization/tool/delegation code, prompts, approval workspaces, state-diff machinery, and judge code. It did not provision the Docker services, call evaluated models, or reproduce reported runs. Numerical results remain paper-reported.

## Review judgment

EntCollabBench is a valuable, unusually inspectable step beyond an all-powerful single agent. It distributes enterprise-service tools across 11 independently hosted role agents, attaches fixed per-agent service identities, gives approval specialists isolated document workspaces, seeds task-local databases, records per-agent traces, computes state diffs, and grades conjunctively across the roles named in a reference trajectory. Its strongest evidence is therefore about **role-scoped, stateful, multi-service execution under explicit HTTP routing**. The paper's failure studies—especially incomplete handoffs, wrong dependency order, create-instead-of-update fallback, parameter-semantic errors, and extreme coordination cost—are directly useful.

The broader language needs a sharper boundary. In the audited release, role is primarily a fixed tool-surface and token configuration; delegation is an unauthenticated peer HTTP call carrying free-text work plus trace/depth/session metadata; operational prompts say that no permission or user confirmation is required; and approval agents return text labels without mutating an authoritative approval state. The judge compares each expected role's trace to its reference steps and supporting database diff, or compares approval text to generated reference decisions. It does not evaluate whether a principal had scenario-specific authority, whether authority was validly delegated and accepted, whether separation of duties held, whether an approval changed what could execute, or whether unauthorized yet operationally successful actions were attempted.

The benchmark thus supports a narrower claim than “realistic organizational collaboration”: it tests whether configured models can traverse a generated, role-labeled trajectory and realize selected service-state or policy-classification outcomes. It does **not** yet establish delegated authority, organizational approval validity, representative enterprise work, professional collaboration, safety, or deployment readiness.

## One-sentence contribution

EntCollabBench contributes an inspectable 300-task, 11-agent environment that makes role-scoped tool execution, explicit cross-agent routing, state effects, policy-document decisions, and chain-position failures measurable, while its release shows why **configured role, callable route, semantically usable handoff, delegated authority, approval judgment, and authoritative approval effect must remain separate benchmark constructs**.

## Why this matters to skill-bench

This review advances charter objectives A, B, and C without narrowing skill-bench to enterprise software. The transferable problem appears in any consequential knowledge work: a researcher hands evidence to an analyst; an analyst asks an expert to adjudicate a threshold; a reviewer approves an artifact; an operator acts on the result. A benchmark must distinguish:

1. which component was configured under a role name;
2. which information and tools it could access;
3. which principal authorized the requested operation;
4. what work package crossed the handoff boundary;
5. whether the recipient accepted, rejected, clarified, or modified it;
6. whether the recipient used it correctly;
7. whether an approval was merely stated or changed authoritative state;
8. what consequence occurred and under whose accountability.

EntCollabBench implements parts of 1, 2, 4, 6, and 8's state-effect side. Its central design lesson is not that every benchmark should use many agents. It is that role specialization creates a **validity burden at each organizational boundary**: transport, information sufficiency, permission, authority, uptake, and consequence cannot be inferred from the same trace event.

## Research question and claim boundary

The paper asks whether LLM agents can complete enterprise workflows when responsibility, service access, persistent state, and policy decisions are distributed across specialized roles. Formally, it defines an agent set, service and delegation tools, a permission map from agent to accessible tools, and a delegation map from agent to peers. Given an instruction and starting agent, success requires role-specific calls and explicit delegation, with workflow traces and state diffs or approval outcomes judged against generated ground truth (Sections 3–4, pp. 3–8).

Three empirical questions should be separated:

- **Execution question:** can the configured role-agent network realize selected service-state changes across an expected multi-role workflow?
- **Coordination question:** does free-text routing preserve the objects, parameters, prerequisites, ownership, and downstream action needed by another role?
- **Organizational-authority question:** was each action and handoff permitted by the relevant principal, policy, approval state, role constraints, and separation-of-duties rules?

The paper and release directly address the first and part of the second. They instantiate static service scopes and identity headers, but they do not supply the scenario-specific principals, mandates, capabilities, delegation acceptance, accountable transfer, approval-state transitions, or adversarial negative controls needed to answer the third.

A safe claim is:

> Under the benchmark's generated prompts, fixed role/tool configuration, task-local service databases, explicit HTTP peer routes, and model-judge observer, EntCollabBench measures whether a configured multi-agent system produces reference-compatible role-local traces and selected state or policy-decision outcomes.

It does not license “can collaborate safely in an enterprise,” “respects organizational authority,” “performs valid professional approvals,” or “is ready for deployment.”

## Methodology and system

### Task universe and construction

The benchmark contains 300 task records in four released files:

- 160 single-subtask workflow tasks;
- 40 three-subtask workflow tasks (120 subtasks);
- 80 single-subtask approval tasks; and
- 20 approval multi-task records containing 55 subtasks.

The Workflow Track is generated from 20 manually specified templates over enterprise events, fixture objects, five trigger types, and five governance rules. Each ground-truth step records executing agent, MCP server, tool name, and arguments. The paper requires cataloged tools, role ownership, explicit cross-department routing, and recoverability of every expected argument from the instruction. Both instructions and tool arguments are rendered from the same context (Section 3.3.2 and Appendix D, pp. 5–6, 19–20).

A static count of the pinned release found 1,461 reference steps and 480 delegation steps in the 160 single-subtask workflow records, plus 352 reference steps and exactly 120 delegation steps in the 40 three-subtask records. Starting-role balance is reasonably spread across the eight operational roles, but reference-step burden is not: `collaboration_ops_specialist` accounts for 350/1,461 single-task steps and 86/352 multi-task steps, while other roles appear less often. This matters because the paper itself shows role scores depend strongly on chain position and tool interface.

The Approval Track starts from about 840K characters of GitLab Handbook and GDPR text. A GPT-5.4-Mini classifier and GPT-5.4 extractor generate a 290-rule schema with typed conjunctive predicates, decision classes, approver chains, evidence slugs, and contiguous-substring source citations. Tasks reverse-engineer case fields to fire selected rules, add near-miss distractors, optionally delete a predicate field or provide fulfillment evidence, render local documents, and compute expected per-specialist labels with a deterministic engine (Section 3.3.3 and Appendices B–C, pp. 6, 15–18).

This is good **instrument construction provenance**: policy text, extracted rule, case parameters, evidence document, and expected label are linked. It is not independent substantive validation. The same generated rule schema both defines the case and decides correctness; no domain-professional audit, inter-rater adjudication, jurisdictional interpretation study, real approval population, or outcome follow-through is reported.

### Role and tool isolation

The release implements two real layers of static role separation:

1. `tool/toolsets.py` constructs each role's visible tool list. Operational roles receive common Email/Calendar/Teams/Drive interfaces plus one specialist domain; the knowledge role gets knowledge-only interfaces across ITSM/HR/CSM; approval roles receive only workspace listing and reading.
2. `config/mcp_auth_by_agent.json`, `agent.py`, and `tool/tool_executor.py` attach fixed role-specific service identity headers. Incoming request-supplied authentication metadata is removed and replaced with the process's fixed map. Servers requiring identity reject missing headers.

This is stronger than prompt-only role play. A service tool absent from a role's LangChain tool list is not ordinarily selectable, and fixed runtime headers reduce straightforward identity substitution through incoming metadata. The agent processes also receive separate local workspaces and the benchmark creates isolated service databases per task.

But this is **static capability isolation**, not a complete authorization model:

- Operational agents all receive every common collaboration service, independent of task, object, requester, recipient, data sensitivity, or current approval state.
- The role token is ambient for the process rather than a task-, object-, purpose-, action-, expiry-, or delegator-scoped capability.
- `tool_executor.py` accepts custom payload headers after runtime headers, so the reviewed client layer does not itself prevent overriding a required identity header. Whether a hidden backend rejects such substitution was not testable from the pinned public source.
- The release has no authorization decision ledger joining principal, mandate, protected action fields, exact state effect, and invocation event.
- No matched negative cases ask a role to call an invisible/unauthorized service, impersonate another principal, mutate an out-of-scope object, use stale approval, self-approve, or act outside delegated scope.
- The paper reports role-specific permissions but no denominator or results for attempted unauthorized calls, rejected calls, escapes, false blocks, or observer coverage.

The prompt further weakens organizational interpretation: every operational agent is told “No Permission Required,” not to ask for confirmation, and to proceed independently. That may be a useful automation treatment, but it removes the user-authorization and clarification behavior that real consequential work often requires.

### Delegation mechanism

Each non-approval agent normally receives an `ask_<role>_by_http` tool for every other configured agent; approval agents have no outbound targets. The delegation tool sends:

- a request ID;
- source and target role names;
- one free-text `task_description`;
- recursion depth and route trace;
- session ID, parent role, optional deadline, and server allowlist.

It blocks cycles and a maximum depth, waits synchronously for a peer response, logs start/error/completion, and returns the peer's free-text result. The HTTP client supplies only content-type and accept headers. There is no signed principal identity, user mandate, delegated capability, action/object scope, evidence manifest, structured produced/required artifact contract, acceptance state, refusal reason taxonomy, accountable owner, or nonrepudiable receipt.

The paper's own G.4 analysis is incisive: handoffs fail when omitted, missing article content, issued before a branch exists, duplicating downstream work, or carrying placeholder rather than source content. It correctly says a syntactically present handoff may be semantically incomplete and that valid delegation requires the right role, timing, prerequisites, context, and repair.

The release supports an even sharper conclusion: the mechanism is **routing with synchronous free-text return**, not delegated authority. `source_agent` names a caller in the payload, but the receiving HTTP endpoint does not establish that the originating user authorized the subtask, that the sender was entitled to delegate it, that the recipient accepted accountability, or that the delegated scope constrained later tool calls. A route may be technically successful while authority, responsibility, or professional usability fails.

### Execution, state, and reset

For workflow tasks, the benchmark seeds dedicated databases, stores session-to-database bindings, captures initial and final exports, canonicalizes rows while ignoring selected nonsemantic fields, and computes inserted/deleted/updated record diffs. It clears agent session memory and deletes seeded databases around task execution. The judge receives traces plus a filtered canonical diff for servers observed in the current agent's events.

These are strong design choices relative to answer-only grading. The create-instead-of-update case is especially valuable: a plausible new incident does not satisfy an update to the designated incident. State evidence can expose false completion claims and semantic parameter errors.

Still, observer coverage is selected rather than proven complete. The judge's state evidence is filtered to servers inferred from actual MCP tool names. If a required server is never called, the judge may receive no corresponding diff and must infer missing work from the absent trace. Extra changes on an unobserved or omitted server may fall outside the role-local view. Truncated exports, ignored fields, asynchronous consequences, cross-service links, messages read by recipients, and policy-to-execution effects are not shown to be fully observed. Cleanup code improves isolation, but no reset-differential study, teardown-failure denominator, collision test, or asynchronous residual-state audit is reported.

### Judgment and aggregation

For workflow subtasks, the release builds one judge input for each agent named in reference steps. It gives an LLM judge the role-local reference steps, actual trace events, and related canonical state diff. The prompt allows equivalent implementations, minor ordering differences, and harmless extra steps; missing or contradictory key actions fail. Approval judging compares each expected approval specialist's generated decision/rationale to terminal trace text and asks whether document/rule evidence was read.

One to three configured judge models vote; the paper reports a three-model majority using Gemini-3.1-Pro, GPT-5.4, and Claude-Sonnet-4.6. Subtask success is the conjunction of expected-role passes; task success is the conjunction of all subtasks. If one multi-task subtask fails, later subtasks are skipped and counted failed.

This is not exact trajectory matching, and the state diff provides a useful side-effect witness. Yet the claimed “deterministic policy adjudication rather than natural-language response judging” is too strong. Ground-truth approval labels are generated deterministically, but **observed approval outputs are semantically judged by LLMs**. Workflow completion is also decided by LLM comparison of traces and selected state evidence. The paper's 48/50 and 49/50 agreement on two model outputs supports local agreement on 100 sampled cases, not criterion validity, error severity, per-category reliability, calibration, independence, or robustness to alternative legitimate trajectories.

The judge evaluates only roles present in ground truth. It does not separately penalize unexpected role activation, unauthorized attempts, privacy violations, excessive delegation, collateral effects outside the filtered view, or an impermissible path that happens to reach the expected state. “Harmless extra steps” are left to model interpretation rather than a typed safety/authority oracle.

## Evidence and results

The paper evaluates 12 named model systems. DeepSeek-V4-Pro has the highest reported average task score at 62.00%, followed by DeepSeek-V4-Flash at 57.33% and Claude-Sonnet-4.6 at 52.67% (Table 1, p. 9). On 40 workflow multi-tasks, DeepSeek-V4-Pro reports 78.33% subtask versus 50.00% task success; Claude-Sonnet-4.6 reports 69.17% versus 50.00%. The best reported multi-step approval task score is 40.00%.

The most informative evidence is diagnostic rather than leaderboard-level:

- A downstream knowledge specialist's pass rate varies from 64.4% when starting to 34.4% behind an HR start, showing that a “role score” mixes local operation difficulty with upstream chain exposure.
- Three-subtask approval prefix success reportedly falls from 61.4% after step one to 30.1% after step two and 22.3% at completion; workflow prefixes fall from 77.3% to 61.4% and then 24.5%. Prefix curves localize cascade position better than task pass alone.
- Handoffs fail through omission, incomplete content, wrong ownership, and unmet prerequisites—not merely incorrect recipient names.
- Models may replace an unresolved update with a plausible create operation, producing coherent but wrong persistent state.
- Tool-family selection can be correct while enum, relationship, assignee, status, sender, calendar ID, or task-type semantics are wrong.
- Pseudo tool calls distinguish stated intention from executable invocation.
- Successful coordination can be extraordinarily expensive: one reported DeepSeek task uses 8,908,553 tokens and 239 events; a MiMo approval loop reportedly consumes more than 104 million input tokens in one delegated specialist before context failure.

These observations are credible as examples from the authors' recorded traces and align with inspectable system structure. But the paper gives no released run manifest in the audited snapshot, no per-trial result archive tied to model snapshots, no repeated runs, no confidence intervals, no family-clustered uncertainty, no systematic failure coding protocol, and no human baseline. Temperature zero does not make remote APIs immutable or deterministic. Many model names are mutable or preview identifiers, and token figures of millions per task raise serious reproducibility and operational-cost questions.

The headline average is also hard to interpret as one capability scale. It combines workflow task success, multi-task success, approval labels, different role burdens, skipped downstream subtasks, and generated template families. The 300 records are not 300 independent work constructs: workflow instances derive from 20 shared templates, approval cases derive from one rule schema and construction engine, and multi-task subtasks share chain state.

## Unique insight

> **Organizational collaboration requires a three-contract join: capability scope, handoff contract, and authority/effect contract. A role label or successful route satisfies none of the other contracts automatically.**

1. **Capability-scope contract:** what tools, records, data views, and actions are technically available to this configured component?
2. **Handoff contract:** what responsibility, prerequisite state, evidence, artifact, uncertainty, deadline, and acceptance condition moved from sender to recipient, and did the recipient use it?
3. **Authority/effect contract:** which principal authorized which exact action or decision, may authority be delegated, did the recipient accept accountability, what approval state changed, and what execution was enabled or prohibited?

EntCollabBench substantially implements the first, traces an untyped version of the second, and largely assumes the third. This decomposition explains why its most useful failures occur at boundaries. An HTTP call can be present but unusable; a usable request can be unauthorized; an approval label can be correct but non-authoritative; an authorized decision can still fail to gate execution; and a correct final state can be reached through an impermissible principal or collateral path.

It also clarifies a construction risk: because prompt values and reference arguments share one render context, argument recoverability proves **template consistency**, not information discovery, contextual authority, tacit judgment, or natural coordination. The benchmark asks the model to preserve many already-rendered values through a role-labeled route. That is a legitimate parameter-binding and handoff test, but should not be promoted into broad enterprise-work realism.

## Comparison with adjacent reviewed evidence

- **AgentCo-op:** typed transport is not semantic or receiver-use validity. EntCollabBench's free-text HTTP handoffs make information loss visible, but the judge mainly asks whether expected downstream actions occurred. Neither transport typing nor a successful call establishes completeness, evidence authority, freshness, uncertainty, recipient uptake, or takeover usability.
- **HAS-Bench:** configured social role and authority vocabulary do not identify participant realization or causal participation. EntCollabBench uses real model-backed services rather than merely naming a human role, but “finance/legal/procurement specialist” remains a configured simulator identity. It does not establish professional qualification, decision rights, human participation, burden, or organizational accountability.
- **TheAgentCompany:** workplace-shaped substrate is not occupational, collaboration, consequence, or labor-automation validity. EntCollabBench repairs one limitation by splitting broad access across agents and making explicit handoffs necessary. It still uses synthetic records, generated workflows, fixed role prompts, and no occupational sampling or affected-recipient outcome, so the same claim boundary applies.
- **Context-to-Execution Integrity:** static identity tokens and tool visibility are weaker than a manifest-bound join of protected-field, exact-effect, and invocation authority. EntCollabBench checks that a role can execute and that expected state changes occur; it does not bind each action to task-specific principal, object, approval, sequence, expiry, retry, or delegation authority.
- **WorkArena++:** executable composition raises horizon but does not isolate planning or professional realism. EntCollabBench's role partition adds a real coordination treatment, yet chain length, starting role, tool interface, instruction phrasing, parameter count, and subtask skipping vary together. Multi-agent score drops do not by themselves identify “collaboration ability.”

## Limitations and validity threats

1. **Post-paper release boundary.** The inspected code and dataset revisions postdate v1. They cannot establish exact manuscript-time implementation or reproduce reported runs.
2. **No run reproduction.** Docker services and evaluated models were not executed in this review; the paper exposes no self-contained immutable result bundle sufficient for replay.
3. **Static roles, weak authority semantics.** Role scopes are fixed toolsets and ambient service identities, not task/object/purpose/action-scoped authorization.
4. **No permission negative controls.** The suite does not report matched authorized versus unauthorized calls, token substitution, direct route attempts, self-approval, stale approval, separation-of-duties, or false-block cases.
5. **Operational prompts erase user-confirmation behavior.** “No Permission Required” removes a central real-work uncertainty and safety demand and can reward action under underspecified authority.
6. **Routing is not delegated authority.** HTTP peer calls carry free text and routing metadata, not an authenticated mandate, capability scope, acceptance, accountability transfer, or structured artifact/evidence contract.
7. **All-to-all delegation exposure.** Unless explicitly limited, each operational role receives routes to every other role. This tests recipient selection but not organizational routing entitlements or escalation policy.
8. **Approval has no authoritative effect.** Approval agents emit classifications and rationale; no approval ledger, request lifecycle, signatory eligibility, conflict check, state mutation, or downstream execution gate is exercised.
9. **Generated-policy circularity.** LLM-extracted rules feed both synthetic case creation and deterministic ground truth. Contiguous citations constrain hallucination but do not validate legal interpretation, rule completeness, conflicts, exceptions, jurisdiction, or professional acceptability.
10. **LLM judging remains central.** Approval and workflow outcomes are semantically judged, despite deterministic reference generation and state evidence. Agreement on 100 sampled judgments is too small and narrow for broad evaluator-validity claims.
11. **Expected-role-only evaluation.** Roles absent from the reference are not first-class scored units; unexpected activation, attempted unauthorized action, or needless delegation can escape direct aggregation.
12. **Selected state observer.** Canonical diffs are powerful but filtered by observed servers and configured exports. Omitted fields, unobserved systems, asynchronous effects, message uptake, and collateral state are not proven covered.
13. **Reference-trajectory shaping.** Prompts and expected arguments share a render context. This supports recoverability while making the instrument unusually verifier-shaped and potentially reducing discovery and ambiguity demands.
14. **Alternative-path validity is delegated to judges.** “Equivalent” and “harmless” are not represented by explicit accepted-state sets, forbidden effects, dependency DAGs, or authority rules.
15. **Template dependence.** Twenty workflow templates and one approval-rule engine induce substantial clustering; raw task counts overstate independent workflow and policy breadth.
16. **No occupational provenance.** “Realistic” tasks are author-generated from tool/state fixtures, not sampled from observed work, expert critical incidents, frequency data, professional artifacts, or downstream recipients.
17. **No human baseline or expert adjudication study.** Difficulty and model ranking are not anchored to trained role holders, novices, independent policy professionals, or organizational users.
18. **Confounded collaboration treatment.** Tool access, role prompt, starting position, chain length, interface regularity, parameter burden, context, and failure propagation change together; no all-in-one versus role-split matched ablation isolates specialization.
19. **Strict cascading changes the estimand.** Skipping all later subtasks after one judged failure measures pipeline reliability under an abort policy, not each downstream role's conditional capability.
20. **Cost is operationally extreme.** Reported million-to-hundred-million-token cases make nominal reproducibility and organizational realism questionable; no dollar, latency, energy, or retry distribution is supplied.
21. **Mutable model identities.** Preview and hosted names may change, weakening configured-system identity and longitudinal comparison.
22. **Reset evidence is incomplete.** Per-task databases and cleanup are strong, but no teardown-failure ledger, state fingerprint equivalence, collision test, or asynchronous residual audit is reported.
23. **Safety and privacy claims are unsupported.** Static role scopes do not test malicious inputs, sensitive data minimization, unauthorized information flow, irreversible effects, recovery, or stakeholder harm.
24. **No production-readiness evidence.** Synthetic services, policies, principals, records, recipients, and consequences cannot establish deployment reliability or accountability.

## Reproducibility and operational realism

**Inspectability: high.** The complete immutable paper is detailed; the official release preserves task records, policy documents, seed assets, prompts, tool mappings, identity configuration, HTTP routing, state export/diff code, and judge implementation. Task counts and core structural claims are statically verifiable. The paper candidly analyzes costly and semantically subtle failures.

**Exact reproduction: low to moderate.** The audited release is post-v1, depends on mutable container tags, remote model APIs, environment variables, and public Docker images, and does not include the paper's complete per-model run bundle. Reproduction would require substantial compute and potentially extraordinary token use. Reported remote model identities are not immutable snapshots.

**Operational realism: mixed.** Multiple independently hosted agents, stateful ITSM/HR/CSM/Gitea/collaboration systems, server identities, task-local databases, policy files, and actual state mutation are more operationally meaningful than dialogue-only collaboration. Conversely, prompts disclose expected values and routes, agents are told not to seek permission, handoffs are synchronous free text, approvals have no authoritative state effect, work is synthetic and template-generated, and no humans or affected organizational recipients participate. This is a controlled enterprise-shaped coordination simulator, not an organization.

## Transfer to skill-bench

### Retain

- Separate role processes with explicit tool visibility and task-local identity configuration.
- Task-local seeded state, initial/final snapshots, cleanup, and trace-plus-state triangulation.
- Role-local and end-to-end outcomes rather than one top-level pass alone.
- Prefix/cascade and chain-position diagnostics.
- Failure categories that distinguish omitted handoff, incomplete context, unmet prerequisite, wrong owner, wrong object, wrong parameter semantics, pseudo call, and nontermination.
- Policy source → extracted rule → case → evidence → expected decision provenance, while preserving extraction uncertainty.
- Resource accounting by role and successful/failed task, not only one aggregate average.

### Repair

1. **Type role separately from authority.** Record configured role, realized component, professional/organizational qualification, service access, data entitlement, action scope, decision rights, and accountable principal as distinct fields.
2. **Replace ambient permission with action-scoped authorization evidence.** Bind principal, mandate, object, operation, protected parameters, exact effect, approval dependency, purpose, validity interval, retry/delegation scope, and invocation receipt.
3. **Make handoffs structured and falsifiable.** Include task/object identity, requested delta, prerequisite state, evidence/artifact manifest with hashes, known unknowns, deadline, allowed actions, forbidden effects, acceptance/refusal/clarification, accountable owner, response artifact, and downstream-use evidence.
4. **Separate routing metrics from handoff utility.** Score route selection, message completeness, recipient access, acceptance, semantic uptake, correct downstream action, repair, and end-to-end effect independently.
5. **Turn approval into a stateful governance workflow.** Test requester and approver eligibility, separation of duties, conflicts, evidence sufficiency, ordering, expiry, revocation, escalation, authoritative state transition, execution gating, and unauthorized bypass prevention.
6. **Add matched authorization states.** Hold the requested operation fixed while varying authorized, missing authority, stale/revoked approval, wrong principal, self-approval, excessive scope, legitimate escalation, and justified clarification.
7. **Grade forbidden and collateral effects.** Evaluate all activated roles and attempted actions, not only expected agents; preserve denied attempts, unexpected systems, privacy/data flows, duplicate work, and residual state.
8. **Represent accepted alternatives explicitly.** Use dependency DAGs, terminal invariants, permitted equivalent effects, forbidden states, and professional consequence checks rather than leaving all equivalence to an LLM judge.
9. **Decouple render-context consistency from collaboration difficulty.** Add conditions where required values must be discovered from authoritative sources, where distractors conflict, where the sender lacks information the receiver can access, and where clarification is the valid action.
10. **Run matched architecture ablations.** Compare all-in-one, statically split, dynamically routed, and authority-scoped systems on identical tasks/tool semantics; vary chain position independently from role and interface.
11. **Validate with domain experts and downstream users.** Sample work and approval incidents, audit rule interpretation, measure recipient usability and burden, and bind claims to the represented population.
12. **Report clustered uncertainty and full run identity.** Treat templates/cases as clusters; publish valid/invalid trial inventories, exact configured-system manifests, judge disagreements, costs, and missingness policies.

## Concrete repository actions

1. **Do not create another schema task.** Existing role/participant realization, information-flow entitlement, authority-lineage, handoff-usability, trace, action-safety, artifact/state, metric, task-health, and validity machinery already covers the identified gaps. A benchmark-specific “enterprise collaboration” contract would duplicate general mechanisms and risk scope narrowing.
2. **Index this review at Tier B.** The benchmark is highly relevant for inspectable role-scoped execution, stateful routing, handoff diagnostics, and policy-derived instrument construction. Its authority and approval claim limits must remain explicit.
3. **Use the evidence in existing validation work.** Future authority/handoff fixtures should include EntCollabBench's strongest failure signatures: correct route with missing artifact content; handoff before prerequisite state; upstream duplication of downstream work; successful but wrong-object mutation; expected outcome under an unauthorized principal; approval label with no gating effect; and an unexpected role or collateral action omitted from the reference.
4. **Treat reported model scores as paper evidence only.** Do not import them as calibration targets without immutable run records, model identities, observer manifests, and clustered analysis.

## Assessment

- **Evidence tier:** full immutable paper plus pinned official post-v1 code/dataset release audit; no model-run reproduction.
- **Most reusable contribution:** inspectable role-scoped services plus explicit handoff and task-local state evidence, with diagnostic separation of role-local and end-to-end failure.
- **Most important empirical insight:** chain position and handoff quality can dominate a role score; route occurrence is not enough when prerequisites, ownership, identifiers, or artifacts fail to cross the boundary.
- **Most serious validity risk:** the benchmark promotes fixed tool scopes, free-text peer routing, and generated policy classification toward organizational permission, collaboration, and approval claims without measuring delegated authority or authoritative approval effects.
- **Claim skill-bench may safely make:** multi-agent knowledge-work evaluation should separately observe configured capability, information entitlement, handoff completeness and uptake, delegated authority, approval-state effect, role-local execution, collateral consequences, and end-to-end utility; no one trace edge or final-state pass can substitute for the others.
