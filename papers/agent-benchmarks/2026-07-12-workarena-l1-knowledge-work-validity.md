# WorkArena L1: enterprise UI realism is not knowledge-work validity

**Source type:** Deep review of the complete immutable arXiv v5 paper and a paper-aligned official release snapshot  
**Paper:** Alexandre Drouin et al., *WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?* (ICML 2024; arXiv:2403.07718v5, 23 July 2024)  
**Immutable paper:** https://arxiv.org/abs/2403.07718v5  
**Local PDF:** `data/papers/pdfs/2403.07718v5-workarena-l1.pdf` (SHA-256 `686792a9085d998be3ac3de3e9c126fd0a9256b6ccb313aa006edb62f7645295`, 21 pages)  
**Local text:** `data/papers/text/2403.07718v5-workarena-l1.txt` (SHA-256 `218bc2731ca2596117dbb35291a0774db16779ad8edbeca132366aed1c3dceab`)  
**Official repository:** https://github.com/ServiceNow/WorkArena  
**Pinned archive:** `data/sources/releases/2403.07718v5-workarena-l1/workarena-b11908298f2e870a18e4a25cfa972ccd33cac3de.tar.gz` (SHA-256 `b66d1c9c3c6757a975ace3bf15462fcf44bbbd813a9013c3fd6e9f95dbb19cc9`)  
**Release provenance:** `data/sources/releases/2403.07718v5-workarena-l1/provenance.json`

> **Version boundary.** The API summary records no withdrawal or retraction. Commit `b11908298f2e870a18e4a25cfa972ccd33cac3de` (17 July 2024) is the last official-repository commit before the immutable v5 update. No paper-aligned tag exists. The snapshot already contains emerging compositional code; this audit attributes L1 claims only to the atomic task modules. No ServiceNow instance was provisioned and no reported trial was reproduced.

## Review judgment

WorkArena's durable contribution is an inspectable bridge from generated natural-language instructions to a real enterprise application's UI and selected native state. Its 33 task families exercise difficult ServiceNow widgets, and its validators frequently inspect database records, list queries, logged-in identity, or chart state rather than demanding one action trajectory. This is a meaningful repair over toy pages and demonstration matching.

The title's stronger construct—“common knowledge work”—is not established. The 19,912 count is a parameter pool dominated by six filter templates and five create-record templates, not 19,912 sampled work activities. Tasks are explicit atomic operations with no stakeholder context, policy judgment, exception handling, collaboration, artifact handoff, or observed professional consequence. Evaluators inspect selected requested fields or UI state, but generally do not establish complete run-attributable change, absence of collateral effects, authorization, or usability. WorkArena L1 measures configured-agent success on **explicit ServiceNow UI operations**, not occupational knowledge-work capability, productivity, or readiness.

## One-sentence contribution

WorkArena L1 makes parameterized enterprise-UI execution and selected native-state validation inspectable, while its evidence bounds the construct to explicit atomic ServiceNow operations rather than representative or professionally validated knowledge work.

## Research question and contribution

The paper asks how well LLM-based browser agents can perform enterprise-software tasks inspired by daily knowledge work, and whether BrowserGym features help (§§1, 3–5, pp. 1–9). It contributes:

1. 33 task classes and 19,912 parameter configurations across list filtering/sorting, form creation, knowledge-base retrieval, catalog ordering, dashboard reading, menu navigation, and user impersonation;
2. template-generated explicit goals, task seeds, setup, validation, teardown, and Playwright oracle functions;
3. execution on remote ServiceNow Personal Developer Instances;
4. BrowserGym's chat, screenshot/DOM/AXTree observations, augmented element IDs, browser actions, and optional raw Python;
5. configured GPT-4o, GPT-3.5, Llama-3-70B, and GPT-4o-with-vision comparisons plus feature ablations.

The strongest general contribution is **typed task lifecycle machinery over native application state**. The weakest link is the promotion from platform resemblance to knowledge-work representativeness.

## Methodology and system

### Task frame, generation, and coverage

The paper groups 33 task classes into 12 list, five form, one knowledge-base, nine catalog, four dashboard, and two menu tasks (Table 6, pp. 13–18). Parameter counts sum to 19,912, but 12 list classes contribute 6,900 instances and five form classes contribute 5,000. Large combinatorial pools are capped at 1,000 randomly selected configurations (p. 13). Thus the relevant independent units are at most task families/templates, not parameter rows.

Goals explicitly disclose the target operation and values (pp. 3–4, 14–17). The tasks mainly test UI grounding and execution: configure a filter, sort columns, create a record, retrieve a planted fact, order configured hardware, read a chart, navigate to a module, or impersonate a named user. The motivating onboarding narrative is not executed end to end. The paper supplies no occupational sampling frame, work-frequency data, SME elicitation protocol, expert/novice contrast, consequentiality assessment, or professional acceptance study. ServiceNow's customer reach establishes platform adoption, not task representativeness.

The knowledge-base family is especially synthetic: 100 facts are embedded verbatim in GPT-4-generated articles; GPT-4 produces ten question variants, GPT-3.5 screens them, and GPT-4 repairs failures (pp. 18–19). This is controlled retrieval through a realistic UI, not evidence about messy organizational knowledge.

### Environment, observation, action, and budgets

Tasks run on free remote ServiceNow developer instances. BrowserGym exposes chat, URL/tab state, prior action errors, screenshot, HTML, and AXTree, with injected element IDs and clickability/visibility metadata (pp. 5–6). The reported WorkArena agents use AXTree rather than HTML because raw DOMs span roughly 40K–500K tokens; prompts are truncated from the end to 40K, 15K, or 8K tokens by model (pp. 5–7). Actions use element-ID primitives, while BrowserGym can also execute arbitrary Python with Playwright.

Every reported L1 episode has a 15-step cap even though Table 6's human-coded oracle averages exceed 15 actions for all five form tasks and all six filter tasks; the paper argues multi-action mode can compensate, but final best configurations disable multi-action (pp. 6–7, 13). Difficulty therefore includes an action-accounting policy that is not neutral across task families. Models also receive parser retries up to four times, model-specific prompt/history features, and configurations selected by random search on MiniWoB and WorkArena before a different-seed evaluation. Results are configured-system outcomes, not model-only effects.

### Setup, reset, and run attribution

The paper describes four task methods: `setup`, `teardown`, `validate`, and optional `cheat` (p. 6). The paper-aligned release makes the lifecycle more concrete:

- `tasks/base.py:107–157` creates a fresh user and credentials per starting task; `base.py:185–202` deletes that user.
- Form validation retrieves a submitted record by a browser-local `sys_id`, compares requested fields, and deletes encountered IDs in teardown (`form.py:774–922`).
- Catalog validation retrieves the created request and checks item, quantity, and options; teardown deletes that request (`service_catalog.py:463–558`).
- List, dashboard, navigation, and impersonation tasks mostly do not persist new task-owned data.

This is stronger than a shared dirty browser session. It is not a full reset attestation. Cleanup is object-specific and not verified after execution. There is no before/after fingerprint, orphan scan, asynchronous-job/cache/session check, teardown-failure record, collision test, or invalid-run rule. Fresh user identity also does not isolate shared catalog state—the release explicitly disables “Add to Cart” because carts are shared between sessions (`service_catalog.py:230–249`).

### Evaluator predicates and accepted alternatives

The evaluator family is heterogeneous:

- **Sort:** one-column sorting reads the live list API; multi-column sorting regex-matches URL query order (`list.py:424–490`).
- **Filter:** parses the ServiceNow encoded query and compares kind, condition count, column set, and value set (`list.py:755–861`). This accepts condition order alternatives but evaluates query construction rather than the resulting record set.
- **Forms:** checks only requested fields in the created record. The code's own caveat says extra fields are not checked (`form.py:774–783`). A browser event listener tries to detect edits outside task fields (`form.py:354–373`), but it is page/interaction dependent rather than a database delta audit.
- **Catalog:** checks one created request, item, quantity, and requested options, rejecting multiple item kinds (`service_catalog.py:474–558`).
- **Knowledge:** passes when any expected or model-generated alternative answer is a substring of the last assistant message (`knowledge.py:216–242`). It does not observe search, article access, citation, or source use.
- **Dashboard:** rereads current Highcharts state and regex-extracts numbers from the last message (`dashboard.py:442–593`). It mutates the page by forcing all charts to render and removing controls/click behavior to simplify retrieval (`dashboard.py:241–294`).
- **Menu/impersonation:** exact URL equality or current impersonated identity (`navigation.py:124–143,202–233`).

These predicates often admit alternative action paths, a genuine strength. But they cover selected terminal facts. They do not generally test unauthorized actions, unrelated state mutations, duplicate records beyond the observed object, quality of communication, or downstream professional usability. Raw-Python availability also makes the action/security envelope part of interpretation.

## Evidence and results

The final evaluation samples ten seeds per WorkArena task family. The paper reports stratified bootstrap means and standard deviations over 1,000 bootstrap samples (pp. 7–8). GPT-4o achieves 42.7% ±1.5, GPT-4o with vision 41.8% ±1.7, Llama-3-70B 17.9% ±1.5, and GPT-3.5 6.1% ±1.3. All systems score 0% on list filtering; GPT-4o is strongest on knowledge retrieval and catalog ordering (Table 2, p. 7).

The experiment demonstrates substantial configured-system performance differences and severe sensitivity to task family. It does not justify the paper's “emergent capabilities” interpretation:

- only ten parameter instances per family are used, despite highly unequal configuration pools;
- bootstrap resampling does not address dependence within shared templates, UI components, backend, or tuned scaffold;
- there are no repeated executions per exact instance to estimate model/backend stochasticity;
- configurations are selected using WorkArena, making the benchmark both development and evaluation family even with a new seed;
- the 15-step cap interacts with oracle length and disabled multi-action;
- model context sizes, truncation, prompting flags, and serving differ;
- no human baseline, task-time, correction burden, or professional threshold is measured in L1;
- no raw episode inventory, attrition/retry ledger, or cost is reported.

The ablations support narrower scaffold findings. Chain-of-thought and action history often help these configurations; extra prompt features can hurt; vision adds little overall; and thought history may entrench errors (pp. 8–9). Each row changes one flag from a model-specific initial configuration, not a full factorial, and the ablation seed differs from Table 2. These are local interactions, not stable component causal effects.

## Unique insight

> **Native-state validation can strengthen outcome evidence while still measuring a benchmark-shaped projection of work.**

WorkArena shows why “programmatic” is not a sufficient grader description. A validator may query the real application database yet inspect only requested fields, a URL, a query string, or one chat substring. Native substrate answers *where* evidence comes from; the predicate defines *which consequences count*. Neither supplies omitted professional requirements.

For `skill-bench`, every stateful task should therefore separate:

1. **work basis:** role, demand, authority, frequency, stakeholder, and legitimate alternatives;
2. **initialized state:** task-owned versus shared objects and precondition fingerprint;
3. **intended delta:** required records/fields/artifacts and accepted equivalence;
4. **preserved region:** forbidden or unchanged objects/fields;
5. **observer coverage:** which state, render, trace, and communication views can establish each criterion;
6. **terminal consequence:** downstream recipient/use, reversibility, safety, and cleanup;
7. **claim ceiling:** UI-operation success versus workflow, professional, productivity, or readiness interpretation.

WorkArena implements pieces 2–4 unevenly. Its key lesson is not “use ServiceNow”; it is to make the projection boundary falsifiable.

## Limitations and validity threats

1. **No task-demand provenance.** Platform popularity and author plausibility do not establish commonness, occupational coverage, or frequency.
2. **Parameter-count inflation.** 19,912 configurations are clustered within 33 classes and seven operation categories.
3. **Atomic explicit work.** Tasks omit problem recognition, prioritization, ambiguity, policy, exception handling, collaboration, handoff, and multi-step workflow consequence.
4. **Observer incompleteness.** Selected terminal predicates do not establish complete correctness, collateral-state preservation, authorization, or usability.
5. **Path-shaped checks.** Filter/sort validators partly inspect encoded queries/URLs rather than extensional result equivalence; dashboard UI is modified to fit the intended construct.
6. **Weak answer provenance.** Knowledge/dashboard checks observe final strings, not evidence access, entailment, or adoption.
7. **Reset not proven.** Object-specific teardown and fresh users are not canonical backend restoration; shared cart handling reveals cross-session state.
8. **Configured-system confounds.** Prompt truncation, histories, parser retries, action vocabulary, model context, provider, and step cap all interact.
9. **Budget unfairness risk.** Many oracle paths exceed the 15-step cap while best reported agents do not use multi-action.
10. **Weak uncertainty.** Ten seeds per family and bootstrap SE do not model exact-instance stochasticity, template clustering, or backend shocks.
11. **No L1 human/professional criterion.** Feasibility is supported by oracles, not measured human effort, expert acceptance, or downstream use.
12. **Mutable dependencies.** ServiceNow, browser behavior, historical model APIs, installer state, generated task files, and separately versioned BrowserGym/AgentLab limit exact reproduction.
13. **Contamination.** Public templates, configs, validators, oracles, and fixed planted knowledge are calibration/training material.
14. **Safety omitted.** Admin-like privileges and impersonation are graded for completion without authorization, privacy, least privilege, malicious instruction, or rollback evaluation.
15. **Impact claims unsupported.** Productivity, accessibility, labor forecasting, and real-world impact are discussed but not measured.

## Reproducibility and operational realism

**Inspectability: high for paper-time L1 task code.** The immutable paper specifies families, counts, agent settings, and aggregate results; the paper-aligned official snapshot exposes configurations, setup, oracles, validators, teardown, and tests. The archive timing is pinned and distinguished from the later WorkArena++ snapshot.

**Exact reproduction: low.** No frozen ServiceNow backend image, paper result trajectories, exact instance list per run, attrition ledger, or complete environment lock was identified. Historical model APIs and remote developer instances are mutable. This review statically inspected code but did not execute the service-backed benchmark.

**Operational realism: mixed.** The real enterprise UI, nested frames, dynamic widgets, database state, identity, catalog requests, and difficult accessibility trees are credible interaction challenges. Synthetic planted content, generated values, explicit instructions, admin-like affordances, atomic episodes, simplified pages, and absent stakeholders/consequences make it an enterprise-UI testbed rather than a validated sample of professional work.

Maintenance burden is material: remote instances must be installed/configured, UI fields and reports patched, generated configs refreshed, chart/list/form internals tracked, and validators adapted to ServiceNow changes. Oracles help detect breakage but are witnesses, not proof that every accepted path and collateral effect remains valid.

## Comparison with BrowserGym and WorkArena++

- The [BrowserGym review](2026-07-11-browsergym-ecosystem-measurement.md) shows that a common runner does not make native evaluators equivalent. L1 supplies one concrete family whose scalar reward hides query-, state-, URL-, identity-, and answer-based semantics.
- The [WorkArena++ review](2026-07-11-workarena-plus-compositional-validity.md) shows that L2/L3 reuse and compose L1 setup/oracle/validator machinery. Composition repairs horizon and prerequisite structure, not L1's missing work provenance or predicate coverage; it can multiply atomic observer gaps.
- L1 has simpler terminal semantics than WorkArena++'s history-dependent sequential validators, but weaker workflow realism. The correct evolution claim is **atomic UI/state predicates → executable composition**, not **simple work → validated planning or professional work**.

## Transfer to skill-bench

### Retain

- Parameterized task setup with deterministic seeds and explicit lifecycle hooks.
- Real application state and backend-aware checks rather than trajectory imitation alone.
- Alternative action paths where terminal predicates genuinely establish equivalence.
- Per-task identity and task-owned-object cleanup.
- Oracles as feasibility and maintenance witnesses, versioned separately from graders.
- Family-level reporting that exposes major UI/operation differences.

### Repair

1. Bind every task to a work-activity source, role/authority, stakeholder, frequency/consequence evidence, and explicit claim ceiling.
2. Count and resample at the template/work-family level; retain parameter-instance identity and dependence clusters.
3. Define intended and collateral state regions, with before/after fingerprints and run-attributable object lineage.
4. Test validators with independently valid alternatives, shortcut states, pre-satisfied states, duplicate/unrelated records, direct mutation, reversal, and teardown failure.
5. Separate final answer correctness from source access, entailment, adoption, citation, and downstream use.
6. Preserve criterion vectors and evidence views instead of flattening heterogeneous predicates into one unqualified success rate.
7. Treat step cap, multi-action accounting, observation transform, parser retry, and raw-code access as configured treatments.
8. Report exact attempts, infrastructure failures, invalid runs, retries, runtime, cost, cleanup outcomes, and repeated-instance reliability.
9. Add authorization, privacy, least-privilege, collateral-change, and rollback criteria for consequential state mutation.
10. Freeze or fingerprint backend/install/browser/task/evaluator identities and maintain bridge cases across upgrades.

## Relevance

WorkArena is directly relevant as an anchor for stateful browser evaluation, task projection, native-state observers, lifecycle maintenance, and the limitations inherited by composed successors. It is not a reason to narrow `skill-bench` to ServiceNow or computer use; its reusable lesson is to separate realistic substrate, sampled work demand, observer coverage, and licensed claims.

## Concrete changes

1. **Consolidation:** replace the repository's WorkArena audit-gap statements with a bounded L1 row: strong enterprise-UI/native-state evidence; weak work sampling, collateral-state, human/professional, and exact-reproduction evidence.
2. **Validation:** reuse existing task-health, state-delta, artifact-view, execution-validity, metric, and validity contracts to add WorkArena-derived adversarial cases: semantically equivalent filter order, correct result via noncanonical query, extra form field, duplicate record, shared-state collision, teardown orphan, and correct answer without observed evidence access.
3. **Reporting:** prohibit parameter-pool size and platform market reach from serving as occupational coverage evidence; report task-family clusters and operation-specific outcomes.
4. **No new schema task:** the identified requirements already have executable homes in existing contracts and pilots.

## Claim boundary

The immutable v5 paper establishes that the authors defined 33 parameterized ServiceNow task classes and evaluated several configured 2024 agents, with GPT-4o reaching about 43% and all systems failing list filtering in the reported sample. The paper-aligned release establishes that L1 tasks use fresh users, generated goals, task-specific oracles, heterogeneous native/UI validators, and object-specific teardown. Neither source establishes representative knowledge work, occupational capability, isolated reasoning, productivity, accessibility benefit, full state integrity, professional usability, safety, cross-software transfer, exact reproducibility, or deployment readiness.