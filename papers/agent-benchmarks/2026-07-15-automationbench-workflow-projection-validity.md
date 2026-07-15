# AutomationBench: executable multi-app state improves workflow evidence, not production-automation validity

## Source and review status

**Deep review, dual-release audited.** I read the complete immutable 15-page arXiv v1 paper and inspected the official repository at both the last commit on the paper publication date and the latest public `main` revision available during this review. I audited all released task rows, assertion declarations, runner/scorer, API search/fetch layer, representative schemas/routes/state predicates, noise generation, export/evaluation paths, and tests.

- Paper: Daniel Shepard and Robin Salimans, *AutomationBench*, arXiv:2604.18934v1, <https://arxiv.org/abs/2604.18934v1>
- Local PDF: `data/papers/pdfs/2604.18934v1-automationbench.pdf` (15 pages; SHA-256 `348360cd2ccefc52d1a8ea65e0a334cb3363fab85e66f71e09f6f5935233cbc5`)
- Local text: `data/papers/text/2604.18934v1-automationbench.txt` (SHA-256 `1b96efc978a3b44713726322559bf97cfecfa44da4df8eee0b6d3bdbecc2a9bd`)
- Official repository: <https://github.com/zapier/AutomationBench>
- Paper-date snapshot: commit `b0b5c0eade98c76ac180af480a554f6f41023f63` (2026-04-21), archive `data/sources/releases/2604.18934v1-automationbench/zapier-AutomationBench-b0b5c0e-paper-time.tar.gz` (SHA-256 `832736db49878b8f2ac57a608a7398f0eba2ecdb60f14434600daa7faa0874d6`)
- Latest inspected snapshot: commit `eda214109cf891ebe8102ca826b87fb98911e103` (2026-07-07), archive `data/sources/releases/2604.18934v1-automationbench/zapier-AutomationBench-eda2141.tar.gz` (SHA-256 `43bd7c7b5078e7159293cfd93b23f7b328e175e27433af1e38fc591826ec6bad`)
- Provenance: `data/sources/releases/2604.18934v1-automationbench/provenance.json`
- Machine-readable release audit: `data/sources/releases/2604.18934v1-automationbench/release-audit.json`
- Date read: 2026-07-15

> **Version boundary.** Neither paper nor repository identifies a manuscript tag. The paper-date snapshot is only the last public commit on the publication date. The latest snapshot changes 497 files relative to it—48,743 insertions and 15,005 deletions across generated tasks, noise, schemas, routes, assertions, runner, evaluation, and tests—so it is current implementation evidence, not proof of paper-run identity. No paper trajectory/result bundle was found, and no model benchmark run was reproduced.

## One-sentence contribution

AutomationBench releases a large executable world of 600 strict-pass multi-application workflow tasks with exact state assertions and 200 simpler controls, providing unusually inspectable evidence about autonomous action under synthetic SaaS APIs; but generated tasks, authored transition models, uneven observer coverage, unreleased result trials, and absent production transport evidence limit the claim to **conformance in this simulator**, not real workflow automation or business readiness.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C by testing a benchmark mechanism with direct relevance across domains: hidden evidence must be discovered across several state stores, transformed into actions, and verified through terminal consequences rather than answer text. The concrete evidence is the complete paper, two pinned code releases, an executable row/assertion inventory, representative end-to-end predicate audits, and actual release test results.

The unresolved capability question is:

> When does a synthetic multi-app task establish that an agent can automate a real workflow rather than only satisfy a benchmark-authored state machine?

AutomationBench clarifies that long prompts, many app labels, exact predicates, and stateful tools strengthen **instrument conformance** while leaving work demand, transition fidelity, observer completeness, recipient utility, and transport as separate evidence obligations. This is expansion plus validation, not a reason to narrow `skill-bench` to SaaS operations.

## Research question and defensible claim boundary

The paper asks how well agents can autonomously complete long, multi-step workflows across business applications when they must discover relevant APIs and hidden evidence, and reports strict task completion and cost for contemporary models.

The released evidence supports a narrower question:

> Under a named agent scaffold, one versioned synthetic world, one API- or Zapier-shaped tool treatment, a 50-step cap, and task-authored deterministic predicates, what fraction of 600 generated workflow packages reach all required terminal states without violating initially satisfied guard assertions?

It does not establish the fraction of real workflows automatable, professional role capability, production SaaS reliability, time savings, safe autonomy, human-equivalent judgment, or deployment readiness. The paper's production-oriented motivation and “what businesses care about” language exceed the demonstrated inference population.

## Methodology and system

### 1. Suite construction and unit of work

The scored suite contains exactly 100 task rows in each of sales, marketing, operations, support, finance, and HR. A separate simple domain contains 200 rows and is excluded from the main score. Tasks combine 2–5 application families, seeded synthetic app data, distractors/noise, and a natural-language instruction. The paper says tasks were generated and manually sampled rather than derived from observed workflows, transaction logs, support cases, occupational studies, or a practitioner elicitation protocol.

A complete static load of both pinned snapshots recovered the advertised 600 + 200 rows. The paper-time scored rows declare 9,619 assertion instances across 337 assertion-type names; per-domain medians range from seven assertions in finance to 32 in support. These are **not 9,619 independent criteria**. Many are repeated instances, dependent checks, guard predicates, or several views of one consequence. Likewise, six author-assigned business domains and dozens of app labels are coverage metadata, not a probability sample of business work.

The suite deliberately requires single-instruction autonomy. That treatment tests persistent self-directed execution, but it excludes clarification, approval, stakeholder negotiation, escalation, changing requirements, and collaborative handoff. A task can therefore resemble an operations workflow while omitting precisely the authority and exception-management mechanisms that make production automation safe.

### 2. Synthetic world, state, and tool interface

The default paper interface exposes BM25 schema search with top-k five and a generic fetch/execute call. The agent must discover API-like routes, inspect data, and submit reads or mutations. Pydantic models hold one in-memory `WorldState`; app-specific route and implementation modules simulate API semantics. The release also provides broader Zapier-action and task-limited Zapier treatments.

This is stronger than free-form tool hallucination. State is serialized, routes are executable, errors can be returned, and graders can query objects independently of the agent's final prose. Yet the simulator is also the benchmark's authored ontology:

- no authentication, authorization, consent, scopes, tenant boundaries, or least privilege are modeled;
- no rate limits, asynchronous jobs, eventual consistency, webhook races, retries with idempotency keys, partial external failures, provider outages, or concurrency are systematic treatments;
- no production API conformance corpus, contract-test coverage report, response-differential study, or transport experiment is provided;
- all people, transactions, policies, and records are fictional;
- the paper explicitly disclaims exact production behavior.

“API-shaped” therefore describes the observation/action surface, not demonstrated equivalence to any named service. A deterministic simulator can make scores reproducible while deterministically encoding unrealistic transitions.

### 3. Noise and discoverability

Tasks include irrelevant records, misleading strings, alternative candidate objects, cross-app evidence, time-zone traps, and policy-like documents. The meeting-conflict example requires inspecting Zoom, Calendar, Sheets, Gmail, and Slack rather than acting on the most salient event. This is a useful repair over direct slot filling: the agent must search, compare, and commit its decision into mutable state.

But noise is generated from the same authored package and often follows reusable patterns. The release exposes all tasks, data, assertion parameters, schema corpus, hints, and transition code. Public tasks are suitable for development diagnostics, not a durable hidden test. There is no private holdout lineage, template-exposure policy, near-duplicate analysis, contamination monitoring, or proof that unseen parameter values represent unseen workflow structure.

The paper reports that hints raise small-model completion to roughly 80–100%, while the default API interface leaves leading systems below 10%. This is valuable evidence that discoverability/tool affordance dominates the configured task. It also prevents treating the low score as an isolated measure of business reasoning: hidden endpoint search, schema representation, tool vocabulary, context management, and workflow judgment all move together.

### 4. Assertions and score semantics

Each task carries a list of assertion objects. The runner marks assertions already true in the initial world. At scoring time it evaluates the registry function for every assertion and computes a diagnostic fraction over assertions that were not initially satisfied, while retaining any newly broken initial assertions as failures. The official benchmark reward is strict: `1.0` only when the diagnostic fraction equals one; otherwise `0.0`.

This design has three real strengths:

1. scoring consults state rather than the agent's claim of success;
2. alternative trajectories can pass when they reach the same observed outcome;
3. initially true negative/absence predicates act as shotgun guards—remaining true does not inflate progress, but breaking one prevents full completion.

The paper's “no partial credit” statement is accurate for the headline reward, while the release still emits dense assertion-level progress for diagnostics and training. That distinction must be preserved: a training signal based on assertion fractions is not the same estimand as business workflow completion.

Observer coverage is the central weakness. Registry functions range from strong object-field and count checks to narrower lexical/containment predicates. Representative operations checks can validate exact dates, prefixes, app IDs, channel targets, and record status; several negative assertions prohibit unrelated changes. But the suite does not generally attest the complete state delta, authorization, causal source use, recipient comprehension, duplicate side effects outside queried collections, irreversible consequences, or downstream adoption. Exact predicates eliminate judge variance; they do not prove that the predicate set is necessary and sufficient for professional success.

### 5. Reset, attribution, and lifecycle

The runner constructs a fresh `WorldState` for each task and task data are embedded in the row. This is substantially cleaner than resetting a shared remote SaaS installation: pre-state is explicit and in-memory state does not persist between ordinary episodes. The latest export path can serialize task state and metadata.

However, the release does not emit a canonical pre/post state root, assertion observer manifest, complete mutation log, grader read-set, unobserved-delta report, or reset attestation as a standard result artifact. External model/provider calls and pricing remain outside the world snapshot. Reproduction also requires exact code, task, schema, model, scaffold, prompt, provider, and run configuration identities, not merely a task row.

### 6. Baselines and evidence

The paper reports one run per model configuration. Opus 4.7 (max) leads at 9.9% and $1.80 per task; Gemini 3.1 Pro (high) scores 9.6% at $0.54; GPT 5.4 (high) scores 7.6% at $1.93. The two leaders' passing-task Jaccard similarity is 0.17. Gemini moves from 9.6% under default APIs to 12.8% with Zapier tools and 14.3% with task-limited Zapier tools; Haiku moves from 1.5% to 2.0% and 3.8%. The simple-domain result for Haiku is 97%.

These findings support high difficulty and strong tool-surface sensitivity for the tested configured systems. They do not identify a single latent “automation” capability:

- one reported run per cell gives no task-level repeated-trial reliability or confidence interval;
- “run-to-run variance is typically within 1%” has no trial count, systems, dates, dispersion estimator, or raw result inventory;
- model, reasoning effort, provider, prompt behavior, pricing, and possibly snapshot all differ;
- task rows are clustered by generators, apps, predicates, authorship, and shared hidden-data patterns;
- the 0.17 Jaccard statistic is descriptive and highly sensitive to sparse passing sets;
- cost is provider/token-price dependent and excludes setup, retries, latency, review, remediation, and downstream error cost;
- failure percentages are not accompanied by a coding protocol, denominators beyond broad model failures, multiple raters, or agreement.

The paper's false-confidence observation—72% of Opus failures, 91% of Gemini failures, and 84% of GPT 5.4 failures reportedly ended with declared success—is useful as a symptom. It calls for explicit verification behavior and calibrated completion claims, not the conclusion that all failures reflect one reasoning deficit.

## Release audit and reproducibility

The release is highly inspectable but not currently clean under its own full test command.

- `uv run pytest -q` at commit `eda2141` fails during collection with 36 `ModuleNotFoundError` errors because legacy `tests/tools/test_<app>.py` files import removed `automationbench.tools.<app>` modules.
- Restricting the run to the current non-legacy surface with `uv run pytest -q --ignore=tests/tools` executes 627 tests: **625 pass and 2 fail**.
- Both failures are Gmail route tests. The tests submit convenience `{to, subject, body}` payloads, while the current route rejects `body` and requires `raw` or `payload` message semantics.

This does not show that benchmark scores are wrong. It does show release/interface drift exactly where the benchmark claims API fidelity. A benchmark whose transition contracts are ground truth needs zero-drift conformance tests, not only many deterministic graders.

**Instrument inspection: high.** Task rows, state models, routes, schemas, assertions, runner, scorer, noise, and tests are public and versionable.

**Paper-result reproduction: low.** No paper-run trajectories, exact model snapshots, request parameters, per-task verdicts, retries, invalids, costs, or result manifest were identified. The repository moved extensively after v1, and the full current test suite does not collect.

**Operational realism: mixed-to-low.** Cross-app dependencies, hidden records, API discovery, state mutation, distractors, policy evidence, exact terminal checks, and strict completion are credible abstractions of digital operations. Fictional data, authored workflows, no auth/permissions, simplified transitions, absent organizations/recipients, and no real-service transport make this an executable synthetic workflow laboratory rather than production evidence.

## Unique insight: workflow projection requires independent transition and consequence arguments

AutomationBench demonstrates a particularly important separation:

> **A task can have executable state, exact grading, and multiple apps while both the world transition and the success consequence remain author hypotheses.**

The projection chain is:

```text
observed or expert work demand
→ task instruction and hidden requirements
→ initialized synthetic state
→ API schema and observation projection
→ executable transition semantics
→ realized complete state delta
→ grader observer/read set
→ accepted consequence and preserved region
→ configured-system score
→ licensed real-work claim
```

AutomationBench strongly implements the middle of this chain. It does not independently validate the first two or last three links. Because task, state, transition, and grader are co-authored, internal agreement can reward a closed synthetic contract even when production behavior or professional consequence differs.

For `skill-bench`, every executable workflow therefore needs two falsifiable validation packages:

1. **transition transport:** matched action/state cases against a trusted reference implementation or authority, covering normal, invalid, concurrent, retried, and alternate paths;
2. **consequence coverage:** an intent-to-observer map proving which required, forbidden, preserved, authorization, communication, and downstream-use consequences are visible to each grader view.

Strict conjunction should be the top rung only after these criterion-level records remain available. Otherwise a score of one means “all selected predicates passed,” not “the work was safely completed.”

## Comparison with adjacent reviewed benchmarks

- **SaaS-Bench** uses 23 applications and per-run containers with state checks. AutomationBench offers a larger generated workflow suite, exact in-memory initialization, richer public assertion machinery, and several tool-surface treatments. It repairs task scale and reset simplicity, not production transition fidelity, calibrated checkpoint value, or occupational demand provenance.
- **OfficeBench** uses three modeled office stores and typed task predicates. AutomationBench expands app breadth and cross-app search but inherits the same projection issue: selected final-state predicates do not automatically establish complete state preservation, artifact quality, or professional office success.
- **WorkArena L1** grounds actions in a real ServiceNow UI/backend, improving substrate fidelity while remaining atomic and weakly work-sampled. AutomationBench trades native-service fidelity for breadth, compositional workflows, deterministic in-memory reset, and lower execution burden.
- **WorkArena++** makes executable composition and prerequisite structure explicit, but its sequential validators can be history dependent. AutomationBench's predominantly terminal-state scoring better admits alternate paths; it still lacks an explicit dependency DAG and cannot diagnose whether a failed conjunction reflects planning, search, transition errors, or one narrow predicate.
- **OccuBench** lets a language model generate tool observations and uses model-majority verification. AutomationBench is substantially stronger on authoritative serialized state, executable transitions, and deterministic judgment. Both remain synthetic instruments whose occupational labels and internal coherence do not establish domain-valid dynamics or professional transport.
- **TheAgentCompany** provides a coherent multi-service company and LLM coworkers. AutomationBench provides broader app/action coverage, cleaner task-local state, and more deterministic checking, but removes organizational interaction, authority, and sustained workplace context. Neither establishes representative labor automation.

No benchmark dominates all validity layers. AutomationBench's defensible comparative niche is **broad executable multi-app workflow conformance with strict state predicates**.

## Limitations and validity threats

1. No occupational or production-workflow sampling frame, frequency weights, observed session provenance, or practitioner task-authorship protocol is reported.
2. Manual inspection is sample-based and apparently author/developer conducted; no independent expert acceptance, agreement, or domain-specific correctness audit exists.
3. Six domains, 600 rows, 337 assertion types, and many app labels are not independent construct breadth.
4. Generated tasks, noise, hints, schemas, transitions, and graders share authorship and can share blind spots.
5. Single-instruction autonomy excludes clarification, approval, escalation, negotiation, and human handoff.
6. No auth, permissions, consent, tenancy, secrets, or least-privilege behavior is simulated.
7. Rate limits, eventual consistency, retries, idempotency, concurrency, outages, webhooks, and irreversible actions are not systematic instrument dimensions.
8. API shape is not API fidelity; no differential conformance study against live/reference services is reported.
9. Deterministic predicates vary in semantic coverage and do not generally establish complete run-attributable state integrity.
10. Assertion instances are dependent and uncalibrated; diagnostic fractions are not units of work, utility, or safe progress.
11. Negative guards reduce shotgun passing but are not evidence that every collateral region has been enumerated.
12. Public tasks, state, hints, assertion parameters, and code create severe contamination and benchmark-gaming risk.
13. Tool-treatment gains confound discoverability, representation, schema breadth, and planning rather than isolating reasoning.
14. One run per reported cell and no released result matrix block reliability, clustered uncertainty, and missingness audits.
15. Failure-mode claims lack a reproducible coding protocol, rater agreement, and root-versus-surface separation.
16. Cost omits latency, setup, infrastructure, failed-run handling, review, remediation, and business consequence.
17. Large post-paper code drift and no manuscript tag weaken paper-to-release attribution.
18. The latest full test suite has 36 collection errors; the bounded current-surface run still has two route-contract failures.
19. No human baseline, professional acceptance threshold, corrected-work burden, or downstream recipient study exists.
20. No matched live-service or higher-fidelity transport experiment connects simulator success to production behavior.

## Transfer to skill-bench

### Retain

1. Task-local serializable world state and deterministic seeds.
2. Hidden evidence distributed across several stores, with decisions committed into state.
3. Schema search as a distinct discoverability treatment rather than silently exposing task-specific tools.
4. Strict completion plus criterion-level diagnostic records.
5. Initially true guard assertions that do not inflate progress but invalidate collateral damage.
6. Alternative trajectories accepted through terminal-state predicates.
7. Separate simple controls and tool-surface interventions for diagnosis.
8. Public executable tasks as development material, separate from claims about an unseen evaluation set.

### Repair

1. Attach every workflow to a demand source, role, authority, stakeholder, frequency/consequence evidence, and claim ceiling.
2. Define a typed dependency graph with produced/consumed evidence and earliest unsupported obligation.
3. Record canonical pre/post state roots, complete mutation logs, observer read sets, untouched-region canaries, and invalid-run semantics.
4. Validate each transition surface against a trusted reference with normal, edge, invalid, repeated, concurrent, and alternative-action cases.
5. Require authorization, least privilege, privacy, approval, rollback, duplicate suppression, and handoff criteria for consequential actions.
6. Preserve assertion vectors and dependence groups; do not interpret raw assertion fractions as workflow progress or utility.
7. Add adversarial grader tests: pre-satisfied positives, hidden duplicate effects, semantically valid alternatives, lexical decoys, unrelated mutations, reversal, and observer blind spots.
8. Report repeated exact-task trials, family/app clusters, invalid denominators, cost/latency distributions, and scaffold/tool/model identities.
9. Separate public development generators and hints from private or refreshed consequence cases with contamination lineage.
10. Require recipient or expert acceptance for artifact/communication outcomes, not only matching text fields.

## Action items

1. **Validation, non-duplicate:** extend the existing projection/transition conformance work with one matched synthetic-versus-reference API slice. Use the same public task and actions, plant an auth denial, duplicate retry, stale read, concurrent update, and legitimate alternative route, then measure state and score transport. This directly tests the new transition-transport requirement rather than creating an AutomationBench-specific schema.
2. **Consolidation, non-duplicate:** add AutomationBench to the professional and web/tool benchmark maps as high inspectability/high synthetic-state control, moderate workflow composition, and low work-demand, production-transport, authority, and consequence evidence. Include the release-test drift as a lifecycle example.

Useful completion is not another task-count row. It is a falsifiable bridge showing whether one synthetic workflow's accepted state and verdict survive a reference transition implementation and a complete consequence audit.

## Claim ceiling

The immutable paper and paper-date release establish that AutomationBench packages 600 scored generated workflows across six labels plus 200 simple controls, with hidden cross-app evidence, API-shaped tools, task-local synthetic state, deterministic assertions, strict completion, and strong reported sensitivity to model and tool treatment. The latest release confirms substantial inspectable implementation machinery but also extensive post-paper drift and failing test surfaces. Neither source establishes representative business work, faithful production APIs, complete side-effect coverage, professional acceptance, safe autonomous operation, reliable model rankings, cost savings, deployment readiness, or a percentage of workflows automatable. The strongest licensed claim is performance on a versioned synthetic multi-application state-transition instrument.