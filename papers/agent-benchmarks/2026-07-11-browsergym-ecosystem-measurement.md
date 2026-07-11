# BrowserGym: interface normalization is not measurement equivalence

**Source type:** Deep review of the complete immutable arXiv v2 paper and a pinned official post-paper release  
**Paper:** Thibault Le Sellier De Chezelles et al., *The BrowserGym Ecosystem for Web Agent Research* (arXiv:2412.05467v2, 10 December 2024)  
**Immutable paper:** https://arxiv.org/abs/2412.05467v2  
**Local PDF:** `data/papers/pdfs/2412.05467v2-browsergym-ecosystem-measurement.pdf` (SHA-256 `622c2dedd3f22c2e3a23fd8dc475da0a95cc73b01ffd7f96a826585b3fbc23d8`, 30 pages)  
**Local text:** `data/papers/text/2412.05467v2-browsergym-ecosystem-measurement.txt` (SHA-256 `246ebb014209b8f5e873c7dca8a84104c07ee67977f2e3b33081c6425bfe9894`)  
**Official release:** https://github.com/ServiceNow/BrowserGym  
**Pinned archive:** `data/sources/releases/2412.05467v2-browsergym-ecosystem-measurement/browsergym-9e779f087de9a65668b6974d11f9ce9816026e96.tar.gz` (SHA-256 `3da71fa10f263a70f0bd610cf399243c914c303cdace0935f250b748e0c35707`)  
**Release provenance:** `data/sources/releases/2412.05467v2-browsergym-ecosystem-measurement/provenance.json`

> **Timing boundary.** The reviewed commit `9e779f087de9a65668b6974d11f9ce9816026e96` is dated 17 March 2026 and adds TimeWarp; it is not the December 2024 manuscript-time implementation. The paper supports claims about the published design and experiment. The snapshot supports claims about later official code only.

## Review judgment

BrowserGym's durable contribution is a useful **transport and experiment substrate**: heterogeneous web tasks can share a Gym loop, rich browser observations, configurable actions, task registration, trace capture, and study orchestration. That sharply reduces integration work and makes configured-agent comparisons easier to run.

Its stronger rhetoric about “consistent evaluation” is not established. The common interface deliberately preserves benchmark-specific setup, termination, reward, evaluator, seed, backend, and action defaults. The later code audit makes this concrete: MiniWoB reads a page-global reward; WebArena wraps its original evaluator with a fabricated two-item trajectory and special assertion fallback; AssistantBench scores the last chat answer with its own permissive parsing; WebArena Verified stops tracing and computes backend/UI/retrieval checks. These are different measurement instruments behind one method signature. BrowserGym standardizes how a trial is invoked, not what its score means.

## One-sentence contribution

BrowserGym makes heterogeneous browser-agent experiments operationally composable, but neither its abstraction nor its 2024 model comparison demonstrates evaluator equivalence, common construct measurement, or pooled cross-benchmark validity.

## Research question and contribution

The paper asks whether fragmented web-agent benchmarks and implementations can be exposed through one extensible environment and experiment framework, then uses that framework for a six-model, multi-benchmark comparison (pp. 1–2, 8–16). It contributes:

1. a Gymnasium-compatible browser loop over Chromium and Playwright;
2. common observations: chat/goal, tabs, URL, screenshot, DOM, accessibility tree, element properties, focus, prior action/error, and elapsed time;
3. raw-Python or mapped high-level browser actions;
4. an `AbstractBrowserTask` setup/validate/teardown interface and registered environment IDs;
5. benchmark metadata, suggested action/seed/step settings, dependency graphs, and backend preparation;
6. AgentLab studies, parallel execution, traces, replay-oriented reproducibility tools, model adapters, and token/cost tracking;
7. a large experiment across MiniWoB, WorkArena L1–L3, WebLINX, WebArena, VisualWebArena, and AssistantBench.

The paper's useful hypothesis is infrastructural: reducing adapter friction should permit broader comparisons and make benchmark-specific overfitting more visible. It does not directly test whether the adapters preserve original scores or whether broader evaluation improves validity.

## Methodology and system

### Common observation and action envelope

BrowserGym treats browser interaction as a POMDP with `reset()` and `step()` (paper §3, pp. 5–8). The observation supports both rendered and structured evidence. BrowserGym IDs injected into DOM/AXTree align elements with bounding boxes and screenshots. Action errors are returned to the agent rather than necessarily invalidating the episode, enabling repair. Actions range from raw Python with a Playwright page to a restricted mapped function vocabulary.

The release confirms substantial normalization but also configurable treatment variation. `browsergym/core/.../env.py` lets callers override viewport, delay, timeout, locale, timezone, headless mode, browser/context arguments, tags marked, and action mapping; its own documentation warns several overrides can alter difficulty. Raw Python is executed when no mapping is supplied. A new browser context is created per task, but that is browser-state separation, not a network, host-filesystem, credential, or arbitrary-code sandbox. A shared observation schema therefore does not imply a shared information budget or safety boundary.

The generic task interface returns a scalar reward, done flag, user message, and untyped task-specific info. It does not require criterion identity, score semantics, evidence views, invalid-trial status, reset proof, or side-effect ledger. Those omissions are precisely where benchmark identity resides.

### Registration, metadata, reset, and orchestration

The paper says each adapter retains task metadata, default train/test split, optional dependency graph, suggested action set, seeds, and maximum steps (pp. 8–10). WebArena-like backends require explicit restoration; AgentLab sequences agents with resets and can respect dependency graphs, although the paper notes this limits parallelism to roughly 2–4 tasks. Failures can be relaunched up to three times (§5.1–5.2).

These facilities retain rather than erase benchmark differences, which is the correct engineering choice. But retry and reset semantics become part of the estimand. The paper does not specify whether failed infrastructure attempts are excluded, replaced, or counted for Table 2, nor provide an attrition ledger. “Relaunch incomplete/error tasks” can silently turn availability-conditioned performance into the reported score unless attempt history and inclusion rules are explicit.

The post-paper release's benchmark layer carries backend preparation and dependency metadata, but WorkArena itself is not implemented in this archive as a local adapter package; the snapshot includes WorkArena metadata and action subsets while relying on separately versioned ecosystem packages. This makes a BrowserGym commit necessary but insufficient configured-environment identity.

### Adapter and evaluator audit

The pinned release demonstrates four materially different contracts:

- **MiniWoB:** seeded page JavaScript generates the goal and exposes global reward/done state. The adapter binarizes positive raw reward and terminates on wrong page/URL. It changes viewport, removes the human reward display, and applies a 1.5 screenshot scale partly because that worked for Claude 3.5. This is an agent-treatment choice, not neutral transport.
- **WebArena:** task JSON and the upstream evaluator are loaded from the separately installed `webarena` package. BrowserGym rewrites site URLs, authenticates, sets geolocation, and enforces an authorized-domain list. At validation it constructs a fake two-element trajectory because the upstream evaluator only needs the final answer for some checks. It catches an `AssertionError` from fuzzy matching and converts it to score 0. The wrapper therefore changes error semantics and cannot preserve trajectory-sensitive evaluation by construction.
- **AssistantBench:** the module loads a mutable Hugging Face dataset with `trust_remote_code=True`, fixes locale/timezone and starts at Google. Validation occurs only after an assistant chat answer; custom parsing coerces JSON, strings, numbers, commas, percentages, and lists before benchmark-specific matching. This is open-web question answering, unlike consequential browser-state tasks.
- **WebArena Verified (post-paper):** the evaluator stops Playwright tracing, builds a network trace, evaluates retrieval/backend/UI state, and averages component scores when present. This later adapter is much richer than the generic scalar interface exposes and illustrates schema loss: typed evaluator statuses and errors are logged but collapsed to one float upstream.

The audit therefore answers the central question: **normalization mostly preserves task identity in adapter code, but hides it at the top-level score interface.** A valid analysis must carry adapter, upstream dataset/package, evaluator composition, task split, backend image/state, defaults, and invalid/retry policy alongside every score.

## Evidence and results

The experiment uses one GenericAgent configuration, including full thought history, with six model checkpoints. Parsing failures receive up to four model attempts before task failure (paper §6.1, pp. 14–15). Vision-capable models always receive screenshots. Benchmark settings and episode counts differ by family; WorkArena L2/L3 use 235-task curricula, while MiniWoB and WorkArena L1 use multiple seeds.

Table 2 reports task success rate and naive standard error for between 181 and 2,650 episodes per benchmark. Claude 3.5 Sonnet leads most rows and reaches 39.1% on WorkArena L2; GPT-4o leads VisualWebArena at 26.7%. Claude's listed total cost across benchmark rows is about $1,029, with costs reported only for that model. Some WorkArena L3 cells are not executed and shown as gray 0.0; non-Claude L3 results are partly reused from WorkArena++ because the authors expected similar scores (pp. 14–15).

This is broad operational evidence, not a clean model-only factorial:

- models differ in provider and multimodal eligibility;
- the agent includes model-facing parsing retries and vision-dependent inputs;
- some cells are imported or skipped;
- task units are clustered by template, seed, website, and dependency chain, violating the independence assumed by `σ/√N`;
- no repeated run estimates backend/model stochasticity;
- success rates are not put on a common construct scale across benchmarks;
- only one agent scaffold is tested, so model × scaffold interactions are unknown.

The paper itself observes that BrowserGym's API appears less suited to AssistantBench than action tasks (p. 15). That is crucial counterevidence to representation neutrality. The experiment demonstrates that a common runner can execute broad coverage; it does not establish fair ranking across all web-agent implementations or a general “web capability” score.

## Unique insight

BrowserGym exposes a distinction that benchmark programs often miss:

> **Interface interoperability and measurement interoperability are separate claims.**

A common `reset/step/reward` shape is valuable plumbing. It does not make reward units exchangeable, observations equivalent, resets equally strong, tasks equally mutable, or failure handling comparable. In fact, the best unifying substrate should preserve benchmark-specific semantics rather than flatten them. The missing layer is an explicit adapter conformance record that states what is preserved, transformed, defaulted, dropped, or reinterpreted.

For skill-bench, this becomes a three-part configured-evaluation identity:

1. **canonical benchmark contract:** task, source/environment state, evaluator, split, and intended defaults;
2. **adapter realization:** field/action mappings, transformed observations, termination/reward translation, unsupported semantics, and conformance tests against native execution;
3. **trial policy:** scaffold, model, tools, budgets, retries, invalid-run handling, reset evidence, and aggregation.

Only native-vs-adapted differential tests can support semantic preservation. API uniformity alone cannot.

## Limitations and validity threats

1. **No adapter-equivalence validation.** The paper reports no matched native-versus-BrowserGym runs, agreement rates, or task-level score diffs.
2. **Construct pooling risk.** Binary “success” refers to synthetic UI reward, database/UI mutation, final-answer matching, or offline imitation depending on family.
3. **Configured-system confounding.** Observation formatting, vision access, parser retries, thought history, action sets, step caps, provider APIs, and benchmark defaults interact with models.
4. **Weak uncertainty.** Episode-level standard errors ignore template/seed/site/dependency clustering and shared backend shocks; no stochastic repetitions are reported.
5. **Incomplete cells and reused evidence.** Some WorkArena L3 cells are skipped or imported rather than generated under the exact reported configuration.
6. **Retry/invalid ambiguity.** Relaunch mechanisms are described, but Table 2 lacks attempted-run counts, failure causes, exclusion/replacement rules, and availability estimates.
7. **Reset evidence is procedural, not demonstrated.** Backend preparation and sequencing exist, yet no per-trial reset attestations or contamination checks accompany results.
8. **Version incompleteness.** Logging package versions/commit/OS/time helps, but upstream packages, datasets, browser binaries, backend images, service state, model serving, locale/region, and credentials also determine the environment.
9. **Safety and isolation.** Raw Python is explicitly risky. Browser contexts and URL allowlists do not establish host/network isolation, policy compliance, authorization, or rollback.
10. **Trace diagnosis is largely manual.** AgentXRay improves inspection, but the paper provides no coded failure taxonomy, rater protocol, frequencies, or root-cause reliability.
11. **Dynamic-source threats.** Open web, demo instances, bot detection, localization, collisions, and silent model updates limit replication; the authors acknowledge these.
12. **Post-paper drift.** The audited 2026 release includes benchmark families and evaluator paths absent from v2, while separate dependencies carry important WorkArena/WebArena semantics.

## Reproducibility and operational realism

**Inspectability: moderate to high for the substrate.** The paper specifies core interfaces; the official snapshot exposes observation extraction, action execution, task registration, adapters, evaluator wrappers, metadata, dependency handling, and tests.

**Exact paper reproduction: low.** The paper does not pin manuscript commits or provide complete per-episode records in the reviewed source. Model APIs and websites are mutable; some results are reused; upstream benchmark packages and backend images are separate. The 2026 archive cannot establish 2024 byte identity.

**Operational realism: heterogeneous.** Browser interaction, live services, enterprise software, state mutation, and open-web retrieval are realistic dimensions. But benchmark families range from synthetic microtasks to offline one-step imitation and open-web QA. BrowserGym is a research framework, as the paper explicitly states, not a secured deployment environment. Its realism must be claimed per task family and configuration, never inherited from the substrate brand.

## Relevance to skill-bench

## Transfer to benchmark design

### Retain

- A common execution protocol with typed, rich observations and explicit action errors.
- Benchmark adapters rather than rewriting all tasks into one lowest-common-denominator format.
- Registered task identity, benchmark metadata, dependency graphs, and backend preparation hooks.
- Full trace/artifact capture, configured model adapters, usage/cost tracking, and inspectable studies.
- Explicit benchmark-specific defaults rather than pretending one action/step policy fits all.

### Repair

1. Version the **native benchmark**, **adapter**, **upstream evaluator/dataset**, **backend image/state**, and **runner** independently.
2. Require an adapter manifest for every mapped field/action/reward/termination/error, including unsupported or lossy semantics.
3. Add differential conformance cases that run native and adapted paths from the same frozen state and compare score, termination, side effects, and evaluator evidence.
4. Preserve typed criterion observations and evaluator statuses; never collapse all component outcomes and invalid states into an unqualified scalar.
5. Separate infrastructure failure, invalid artifact/action, agent-declared infeasibility, substantive failure, timeout, safety termination, and evaluator defect.
6. Record every attempt, retry cause, replacement decision, reset attestation, and score-inclusion rule. Report both capability-conditional and service-availability estimands where relevant.
7. Aggregate within declared score families; do not average heterogeneous benchmark success rates into “general web ability” without a validity argument and weighting basis.
8. Use clustered uncertainty and repeated trials appropriate to template, seed, site, task dependency, backend, and model stochasticity.
9. Treat observation/action defaults as experimental treatments. Pin screenshots, DOM/AXTree transformation, viewport, locale, timezone, delay, action vocabulary, parser retries, and step budgets.
10. Enforce an outer sandbox and network/credential policy independently of browser context and URL checks.

These requirements already belong in skill-bench's configured-system, execution-validity, task-health, metric-monitoring, validity-argument, artifact-view, and trace contracts. No new build task is justified.

## Concrete changes

1. **Consolidation:** use BrowserGym as the web/tool-family example for the distinction between substrate interoperability and measurement equivalence; preserve family-specific score semantics in the state-of-the-art map.
2. **Validation:** add one native-versus-adapter differential conformance scenario to an existing execution-validity slice. Plant a scorer-status loss and an infrastructure retry to verify they cannot become ordinary 0 scores or silently replaced trials.
3. **Authoring rule:** require every benchmark-family adapter to declare canonical defaults, transformations, dropped evidence, upstream versions, reset mechanism, and claim-preserving conformance evidence before cross-family reporting.
4. **Reporting rule:** publish family-level scores and typed validity bounds; prohibit an omnibus “knowledge-work capability” aggregate merely because tasks share a runner.

## Claim boundary

The immutable v2 paper establishes that a GenericAgent could be launched through a common BrowserGym/AgentLab interface across several heterogeneous 2024 web benchmarks and that the reported configured model systems had widely different task success rates. The later official release establishes that diverse adapter and evaluator semantics remain behind the common API. Neither source establishes native/adapted score equivalence, a common latent construct, causal model-only rankings, production safety, professional knowledge-work validity, or deployment readiness.