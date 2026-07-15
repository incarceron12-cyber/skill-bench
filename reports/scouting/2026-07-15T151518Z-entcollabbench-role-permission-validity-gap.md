# Scouting note — role-specialized collaboration and approval-validity gap

**Timestamp:** 2026-07-15T15:15:18Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Initial queue inspection found 275 tasks: 270 completed, three blocked, one pending human prerequisite, and one pending build; no source, research, review, or claimed backlog remained. The corpus already covers typed handoffs, simulated participant graphs, enterprise substrates, native-state predicates, workflow composition, action authority, and collaboration repair. This run therefore searched only for an instrument that jointly exercises role permissions, delegation, stateful closure, and policy-grounded approval rather than repeating broad enterprise-benchmark discovery.

## Substantive finding — triage only

**Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows** — Tao Yu et al.; arXiv:2605.08761v1.

- Immutable record: https://arxiv.org/abs/2605.08761v1
- Immutable PDF: https://arxiv.org/pdf/2605.08761v1
- Surfaced release candidate: https://huggingface.co/datasets/Kirito-Lab/EntCollabBench
- The arXiv API identifies immutable v1, submitted 9 May 2026, and its summary contains no withdrawal or retraction notice. The versioned abstract, PDF, and HTML endpoints returned HTTP 200 during scouting.
- The abstract introduces `EntCollabBench`, a permission-isolated synthetic organization with 11 specialized agents across six departments. It describes a Workflow subset with collaborative enterprise-state mutation and an Approval subset with policy-grounded decisions, evaluated through execution traces, database-state verification, and deterministic policy adjudication.
- The abstract reports failure concentrations in delegation, context transfer, parameter grounding, workflow closure, and decision commitment. These are author-reported abstract claims, not independently verified findings. Role assignment, actual permission, information availability, delegation attempt, semantic uptake, realized state change, workflow closure, policy correctness, and professional collaboration are separate estimands.
- Structural inspection of immutable-v1 HTML—not a full reading—confirmed sections on task scope, Workflow and Approval construction, multi-agent formulation, execution environment, evaluation procedure, judgment mechanism, experiments, a human-judgment comparison, policy/task examples, agent prompts/hyperparameters, delegation-chain position, prefix decay, closure, tool bottlenecks, fallback actions, parameter semantics, coordination cost, approval commitment, limitations, and broader impact.
- No project or dataset link appeared among the paper HTML's external links. Search surfaced a public `Kirito-Lab/EntCollabBench` Hugging Face dataset and collection, but author ownership and official-paper status were not established. The dataset API returned exact revision `df95c87317863d507f229df190b2c0a29c4e4afc`, created 9 May and last modified 13 May 2026. Its revision-pinned tree exposes four JSON files, `seed.zip`, `local_data.zip`, an overview image, and a card describing 300 tasks: 160 single and 40 multi-task MCP workflows plus 80 single and 20 multi-task approvals. This was release-location and manifest triage only; task records and archives were not inspected.
- Repository-wide exact-title, arXiv-ID, and project-name searches found no local review or queue task. The closest evidence is AgentCoop, HAS-Bench, TheAgentCompany, WorkArena/WorkArena++, and Context-to-Execution Integrity. Those sources separately cover handoffs, simulated participation policies, integrated workplace substrate, native-state observation/composition, and mediated action authority; none locally reviewed source combines those primitives in this exact role-isolated workflow-plus-approval design.
- `Can Agent Benchmarks Support Their Scores?` (2605.10448v1) was surfaced by the same search but rejected as a duplicate because it already has a full local review, release audit, and conformance build.
- This is **metadata, abstract, endpoint, section-structure, release-location, and manifest triage only**. The paper body, appendices, tables, task records, policy documents, seed state, evaluator implementation, model configurations, runs, statistics, costs, human labels, archives, and paper/release correspondence were not read or audited. No claim is made that roles reflect real organizations, permission boundaries are complete, delegations transfer meaning, state checks observe intended consequences, approval policies are professionally authorized, failure categories are valid, the surfaced release is official or reproducible, or the benchmark establishes professional collaboration, safety, capability, production fitness, or readiness.

## Why this is distinct

The reusable chain is `organizational source and role authority → task projection → role-specific information and permissions → delegation request → recipient interpretation and acceptance → tool/action attempt → intended and collateral state → cross-role workflow closure → policy evidence and approval commitment → observer/adjudicator decision → coordination cost and downstream consequence`. A successful endpoint can hide unauthorized access, wrong-role work, lost context, accidental state agreement, or an invalid approval rationale; conversely, a blocked endpoint may reflect a sound permission boundary or environment fault rather than weak collaboration.

The design may offer a compact stress substrate for typed authority and handoff machinery, but a synthetic organization can co-author the roles, policies, tasks, tools, state, and oracle. A full audit should therefore test semantic instance conformance, permission and information-flow realization, accepted alternate delegation paths, complete intended/collateral state observation, approval-policy authority and ambiguity, environment/service invalidity, clustered task dependence, repeated reliability, and whether the human comparison validates criterion decisions or only selected labels.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent evaluation), B (role/policy expertise into tasks and checks), and C (handoff, authority, state, and trace infrastructure).
- **Concrete evidence/artifact:** immutable-v1 deep review plus a timing-aware, exact-revision audit of the surfaced 300-task release if its official status can be verified.
- **Uncertainty clarified:** whether role specialization and deterministic state/policy checks identify collaboration and approval quality, or only conformance to an author-defined synthetic organization.
- **Mode:** narrow expansion/validation; enterprise workflow is a cross-domain stress case, not a permanent scope commitment.
- **Duplication/scope:** no local duplicate; mandatory comparison with AgentCoop, HAS-Bench, TheAgentCompany, WorkArena/WorkArena++, and Context-to-Execution Integrity prevents a parallel collaboration schema without evidence.
- **Useful completion:** separate role availability, authority, access, delegation, uptake, action, state, closure, approval correctness, observer validity, reliability, coordination cost, professional collaboration, safety, and readiness.

Added one task: `review-entcollabbench-role-permission-validity` (priority 7). The pending consented expert micro-pilot and evidence-acquisition build remain much higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing untracked paper-source, release-archive, and site files were not touched.
