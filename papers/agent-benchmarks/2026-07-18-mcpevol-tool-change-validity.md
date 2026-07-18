# MCPEvol-Bench: independent version trials reveal interface sensitivity, not agent adaptation

## Source and review status

**Deep review of the complete immutable primary source; empirical release unavailable or unlinked.** I read the full 40-page arXiv v1 paper, including all appendices and prompts, and inspected the complete arXiv source archive. The rendered paper and metadata provide no benchmark release URL. The source contains a commented-out code/data claim pointing to an anonymous 4open URL; that URL returned HTTP 401, and exact-title, arXiv-ID, and release-token searches found no verifiable author-owned empirical repository. Results, server mutations, tasks, trajectories, human judgments, and run records therefore could not be replayed.

- **Paper:** Huanxi Liu et al., *MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers*, arXiv:2607.14642v1 (16 July 2026), <https://arxiv.org/abs/2607.14642v1>
- **Local PDF:** `data/papers/pdfs/2607.14642v1-mcpevol.pdf` (40 pages; SHA-256 `ebfd92cb244e795c3605d20122020879cc834184874cf82568d4757f819de76e`)
- **Full local text:** `data/papers/text/2607.14642v1-mcpevol.txt` (131,439 bytes; SHA-256 `c0396195e6aebebf8cd0fa4e2027fca3545e7a677399307d4f618074bbab6ec8`)
- **Metadata:** `data/papers/source/2607.14642v1-metadata.xml` (SHA-256 `47f12a6f8d9633ad206b0c1d5a0833f4a30f2aa13c30a818f4f0269db987cec9`)
- **Complete arXiv source:** `data/papers/source/2607.14642v1-source.tar.gz` (SHA-256 `2345495bc24dfc31b5ecf4b5273627f32dd1e92f5cc9ce9e711b3d83c9df46f0`)
- **Release-search provenance:** `data/sources/releases/2607.14642v1-mcpevol/provenance.json`

## One-sentence contribution

MCPEvol-Bench usefully turns external-tool change into a version-paired evaluation object—201 tasks over 123 MCP servers, with original, three-mutation, and five-mutation configurations—but its independent fresh runs measure sensitivity to synthetic interface/context perturbations, not adaptation over time, and neither the semantic equivalence of task consequences nor the reported causal effect of individual mutations is established.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, and C through a cross-domain configured-system question:

> When an external tool changes, what evidence shows that the task stayed equivalent, the agent observed the change, and its behavior adapted—rather than merely responding differently to a changed prompt, tool inventory, implementation, or grader?

The benchmark’s strongest reusable idea is not MCP-specific. Realistic knowledge work depends on spreadsheets, databases, SaaS applications, document APIs, internal services, and policy documents that change while users expect important outcomes to remain stable. A version-paired task can expose brittle workflows only if six identities remain separate:

```text
intended user obligation
→ tool contract version and semantic delta
→ realized environment and observation
→ agent history/exposure and state
→ artifact/state consequence
→ version-conditioned measurement
```

MCPEvol-Bench freezes the task instruction and candidate server set, but does not establish the other joins strongly enough to call the observed score difference “adaptation.” The general design lesson is to measure **compatibility, sensitivity, recovery, and learning as different estimands**.

## Research question and construct

The paper asks whether tool-using LLM agents preserve task performance as MCP servers evolve. It motivates this with two empirical streams (paper pp. 3, 16–17; extraction lines 155–199, 879–961):

1. 1,869 remotely hosted Smithery endpoints monitored weekly for 12 weeks, whose reported availability falls from 72.7% to 52.0%; and
2. 515 deployable NPM-published servers reconstructed from 9,273 historical versions and 6,436 tools, where 54.6% of initial tools are reported modified or deprecated in the latest version.

Those observations establish that availability and interfaces change. They do not establish that the paper’s synthetic mutations reproduce the consequential semantics, frequencies, dependencies, or migration practices of production tool evolution. Nor do they show that dynamic server discovery itself “overcomes” API inflexibility: MCP standardizes discovery and invocation shape, but discovered contracts and implementations can still change.

The paper uses “adaptability,” “robustness,” “stability,” and “evolutionary competency” almost interchangeably. They should be separated:

- **cross-version compatibility:** one policy succeeds under multiple frozen versions;
- **perturbation sensitivity:** an otherwise fixed configured system changes outcome when a tool version changes;
- **online recovery:** within a run, the system detects a failure and repairs its plan;
- **longitudinal adaptation:** exposure to earlier versions or feedback changes retained state and improves later performance;
- **forward transfer:** adaptation generalizes to an unseen server, mutation, or equivalent task.

The experiment directly addresses the first two, partially observes recovery behavior, and does not identify the last two.

## Methodology and system

### Server and task construction

The authors filter collected MCP servers to exclude proprietary-key or third-party-dependent instances, then use LLM assistance and expert annotation to retain 123 servers exposing 1,272 tools across nine categories (pp. 5–6; lines 253–285). They bundle servers as an NPM package. Tasks are generated by DeepSeek-Chat from random same-category groups of two to five servers, without naming the tools. Candidate tasks must receive LLM scores of at least 9/10 for solvability and 6/10 for practical utility, after which LLM-agent rollouts are assessed by an LLM judge and human review. The final set has 201 tasks, averaging 25.90 tools in context, 4.37 calls, and 3.76 servers.

This is a plausible generation funnel, but the paper does not report:

- the number of initial servers, generated candidates, rejected tasks, or reasons at each benchmark-construction gate;
- who the task reviewers were, their instructions, independent labels, adjudication, or agreement;
- executable reference outcomes, allowed alternative workflows, state-reset manifests, or task-specific consequence predicates;
- whether task admission depended on success by models related to those later evaluated;
- task clusters, source-server overlap, near duplicates, or train/test contamination analysis.

The “practical utility” score is an authoring heuristic, not evidence that users perform or value these workflows. Excluding credentialed and externally integrated servers improves deployability but removes many high-consequence tools; Appendix C simply asserts that this does not compromise generalizability (pp. 14; lines 738–745), without evidence.

### Synthetic tool evolution

The empirical history is compressed into 18 observed patterns and then 11 mutation operators at tool, parameter, and description levels (pp. 5–6, 17, 20; lines 287–355, 932–961, 1115–1154). Claude-Opus-4-5 selects one operator per round and modifies AST-anchored TypeScript snippets. DeepSeek-Chat generates parameter-coverage tests; a changed server must pass syntax and “functional integrity” checks before another round. Each task is then run on original, three-round, and five-round server configurations.

The prompts reveal an important tension. Several operators explicitly require backward compatibility or preservation of core functionality: tool addition must leave existing tools unchanged; optional parameter expansion must preserve old calls; replacement must cover old use cases; removal migrates behavior; description-only operators must not change schema or logic (pp. 20, 24–31; lines 1115–1148, 1420–1907). The benchmark therefore often tests whether added descriptions, options, or distractor tools perturb a fresh policy even when the old workflow should still work.

That is useful evidence of **context/interface sensitivity**. It is not necessarily evidence that an agent failed to adapt to a genuinely necessary migration. The paper’s train-ticket example makes the distinction concrete: optional `minPrice` and `maxPrice` parameters are added while backward compatibility is promised, yet GPT-5.4 supplies both as zero and fails (pp. 21–22; lines 1241–1263). The failure shows schema-induced over-action. A compatibility oracle should separately test that the old call still returns the old consequential result before scoring the agent.

The generated tests are also too weak to certify semantic equivalence. Their prompt requests expected status (`Success` or `Validation Error`) plus parameter and boundary coverage (p. 38; lines 2273–2313). It does not require old/new output equivalence, task-level postconditions, invariant state transitions, alternative valid behavior, metamorphic properties, side-effect checks, or independent human approval. “Passes generated tests” therefore means the mutated interface executes under generated cases, not that each original task has the same meaning and attainable consequence.

### Trial design and configured systems

Twelve models are run with temperature 0.2 against fixed candidate server sets and a common multi-turn prompt (pp. 6–7, 35; lines 357–386, 2099–2130). Dynamic tool retrieval is intentionally bypassed. Cleanup runs after each evaluation; the software stack and host CPU are reported (p. 15; lines 861–874).

This design isolates server-version presentation better than a live-service benchmark, but it does not form a longitudinal sequence. The paper does not report that one agent instance experiences early, then middle, then late versions; retains memory; receives a changelog; or updates a workflow. Each version appears to be an independent task execution initialized from the current tool descriptions. There is no before/after agent-state hash, exposure ledger, update event, checkpoint, retention probe, or unseen-version transfer test.

Consequently, a late-version decline estimates a configured cross-version contrast. It cannot show whether the agent “learned,” “adapted,” forgot, or recovered. The memory/plan/reflection additions in Table 4 are separate late-stage scaffolds, not adaptation mechanisms evaluated through an exposure sequence; no matched resource envelope, prompt details, repeated uncertainty, or component interaction is reported (p. 9; lines 472–489).

The execution envelope is also under-specified. Appendix B says tasks use isolated directories and strict file permissions, while mutations run in a closed sandbox (p. 14; lines 728–736). Third-party NPM packages are executable code, however, and no container/VM identity, network policy, process/syscall boundary, filesystem allowlist, resource limit, escape canary, package lock, or per-trial environment hash is provided. File permissions alone do not establish safe or comparable isolation.

### Measurement

DeepSeek-Chat scores Task Fulfillment and Planning Effectiveness from the task, tool list, final answer, and trajectory on 1–10 scales (pp. 6–7, 35–38; lines 370–386, 2133–2268). The prompt also defines Information Grounding, but the main tables omit it. The prose calls the dimensions Task Fulfillment and “Planning Effectiveness,” while the released prompt calls the latter “Planning Efficiency” and returns `planning_and_efficiency`. This is not just naming: effectiveness and efficiency are different constructs.

The rubric has internal dependence despite instructing independence. Task fulfillment says a met subgoal via a redundant path should still count as met, yet “perfectly executed” later requires zero redundancy, graceful recovery from any failure, ideal parameters, and minimal rounds. These contradictory instructions allow the judge to leak efficiency into fulfillment. The metric also asks an LLM to infer the denominator of “distinct explicit sub-goals” and atomic claims without a task-specific frozen decomposition.

The main values are reportedly averages over five “independent evaluations” with prompt shuffling; Table 7 reports variances below 0.2 (pp. 14–15; lines 747–858). It is unclear whether these are five independent agent trajectories, five rejudgments of one trajectory, or both. If they are rejudgments, they quantify judge instability, not operational agent reliability. No seeds, per-task records, missing/invalid calls, retry policy, paired confidence intervals, task-cluster uncertainty, or model-by-version interaction test is reported.

Human validation uses three unnamed experts to rank early/middle/late trajectories for three frontier models. Three LLM judges’ per-task rankings are compared with the average human rank using mean Spearman correlation, reported as 0.73–0.85 (pp. 15–16; lines 818–858). The paper does not state expert qualifications, sample size beyond implying all tasks, blind/order protocol, tie handling, inter-expert agreement, disagreement distribution, or confidence intervals. Averaging three ranks can create ties, while the displayed closed-form Spearman formula assumes an ordinary three-item rank vector. Agreement on relative trajectory ordering does not validate the absolute 1–10 scale, the task oracle, professional consequence, or the attribution of a difference to tool evolution.

## Evidence and results

### What the manuscript reports

Across the three version configurations, GPT-5.4 task fulfillment falls from 7.23 to 6.24 (13.7%), and Claude-Sonnet-4-6 from 7.22 to 6.18 (14.4%); Claude-Opus-4-6 falls less, from 7.15 to 6.77 (Table 3, pp. 7–8; lines 328–410). A single-category LLM trajectory classifier reports planning and reasoning errors increasing by 35.6% and 34.1% (pp. 8; lines 418–434). A selected historical subset of 50 server versions and 86 tasks shows current-versus-historical gaps of 4.1–12.3% for three models (p. 9; lines 472–504).

These are material descriptive contrasts if the manuscript records are accurate. But no per-task data or release permits reconstruction, and no uncertainty accompanies the headline stage differences.

### ECS does not measure adaptation

The Evolutionary Competency Score computes, for each task, mean task-fulfillment across three versions minus its sample standard deviation, then averages over tasks (pp. 7, 14–15; lines 375–386, 756–816). It prevents a consistently poor system from looking “stable,” but it has three construct defects:

1. **Direction blindness:** score sequences `{9, 5, 9}` and `{5, 9, 9}` have the same mean and standard deviation although one recovers and the other improves after an initial low score; reversing any sequence leaves ECS unchanged.
2. **Noise conflation:** judge noise, stochastic retries, environment faults, beneficial improvements, and harmful regressions all increase the same penalty.
3. **No adaptation event:** the formula contains no exposure, state update, recovery time, retained change, or held-out transfer term.

ECS is therefore a conservative cross-version level-and-dispersion index under an arbitrary penalty coefficient of one. It is not an adaptation estimand, and its scale lacks a stakeholder loss or decision threshold.

### Mutation attribution is not causal

The paper says operators are selected adaptively by Claude-Opus-4-5 based on each server. Multiple operators may affect one server, and the resulting score difference is divided equally among them to produce Figure 6(b) (p. 15; lines 875–877). This makes claims such as tool addition `−0.96` or description update `−0.81` descriptive allocations, not causal operator effects. Operator choice is confounded by server, task, baseline difficulty, prior mutation history, mutation round, and the mutation model’s judgment; equal splitting assumes away interactions. No randomized operator assignment, factorial design, matched counterfactual mutation, order balancing, or clustered uncertainty is reported.

Likewise, the error analysis forces exactly one “earliest root cause” into six supposedly orthogonal labels (pp. 39–40; lines 2319–2409). Syntax, semantic-parameter, planning, reasoning-observation, and redundancy errors can coexist and mask one another. The manuscript provides no human validation, disagreement, denominators, or transition evidence for the reported percentage increases. The labels are diagnostic hypotheses from a configured judge, not established causal roots.

### Synthetic-real similarity does not validate task consequences

The paper compares embeddings of simulated code diffs with real consecutive-version diffs. Evol-versus-real cosine similarity is 0.63/0.52/0.53 for BGE-M3/CodeT5/StarCoder2, compared with 0.71/0.46/0.45 for real-versus-real and 0.42/0.32/0.30 for random pairs (pp. 9, 15; lines 490–504, 818–826). Higher embedding similarity than random on selected encoders shows lexical/representation proximity under those models. It does not show that mutation frequencies, dependency breakage, user obligations, migration costs, security effects, or task outcomes match real evolution.

The historical-version subset improves ecological relevance, but it is heavily selected: broken or undeployable versions are removed, leaving 50 versions and 86 tasks from the much larger history. Current and historical versions differ chronologically and may differ in documentation quality, functionality, dependencies, and task fit. The experiment is not a controlled validation of synthetic mutations and does not establish transport to current production services.

## Unique insight

The paper’s unique insight for `skill-bench` is a **version-pair validity boundary**:

> A frozen task instruction does not make two tool environments equivalent. Versioned evaluation needs a signed claim about which user obligations and consequences are invariant, which interface changes are visible, and which old/new workflows remain valid.

This yields a more useful test matrix than one aggregate “adaptability” score:

| Question | Required contrast | Bounded claim |
|---|---|---|
| Does the old workflow still work? | old workflow replayed on old/new environments | backward compatibility |
| Can a fresh agent use each version? | reset agent on old/new with matched resources | cross-version sensitivity |
| Can an agent detect and recover? | planted break with within-trial repair opportunity | online recovery |
| Does prior exposure help? | reset vs retained-state arms over ordered versions | longitudinal adaptation |
| Does the update transfer? | unseen mutation/server/equivalent form | forward transfer |
| Is the outcome still professionally acceptable? | version-specific artifact/state and consequence checks | bounded utility/validity |

MCPEvol-Bench primarily fills the second row and provides qualitative material for the third. Calling all rows “adaptation” obscures the exact capability and repair mechanism.

A second insight is that **backward-compatible evolution can function as an interface-placebo test**. If old calls and consequences are mechanically proven invariant, then performance loss after description-only or additive changes isolates susceptibility to irrelevant context and affordance expansion more cleanly than a genuinely breaking migration. That is potentially more diagnostic than the paper’s interpretation—but only with executable old/new compatibility witnesses and matched observation hashes.

## Limitations, reproducibility, and operational realism

- The source’s code/data sentence and anonymous URL are commented out; the rendered paper contains no release link. The anonymous URL returned HTTP 401. Tasks, NPM package, server versions, mutations, tests, trajectories, judgments, human ranks, and result tables are unavailable for audit.
- The paper gives no immutable package/server source commits, licenses, SBOM, dependency locks, mutation diffs, task IDs, split manifest, or model endpoint snapshots.
- The empirical collection dates, weekly timestamps, endpoint identities, failure adjudication, deduplication rules, and raw availability/version records are not released.
- Task selection is LLM-mediated and rollout-conditioned, but the selection funnel and model-family overlap are not quantified.
- Functional integrity relies on model-generated tests whose expected status does not establish semantic or consequential equivalence.
- No predeclared mutation assignment, task-equivalence block, operator randomization, order counterbalancing, agent exposure sequence, or untouched transport set is described.
- Five “independent evaluations” are not operationally defined; variance without the unit of replication cannot support reliability.
- The cost statement gives approximately $0.26 for a “single evaluation” under DeepSeek pricing but does not identify which calls it includes, total trials, failed calls, mutation costs, human labor, or complete benchmark cost.
- The paper reports only endpoint and judge scores. It does not measure documentation lookup, changelog use, detection latency, recovery attempts, retained workflow state, rollback, side effects, collateral artifact changes, or downstream user consequence.
- File permissions do not substantiate the claimed safe sandbox for executing mutable third-party packages.
- The paper’s limitation section acknowledges constrained servers but dismisses the resulting generalization threat without evidence.

## Claim ceiling

### Supported, conditional on manuscript accuracy

1. Tool contracts and remotely hosted MCP services change frequently in the authors’ sampled sources.
2. The authors constructed a broad synthetic package of versioned MCP servers and fixed-instruction tasks using 11 inspectable mutation prompts.
3. Under the reported configured harness and LLM judge, several models score lower on later synthetic configurations than on original configurations.
4. Description-only and backward-compatible additive changes provide a potentially useful interface-sensitivity stressor.
5. The paper supplies detailed generation, mutation, execution, judging, and error-classification prompts that make conceptual auditing possible.

### Not supported

- longitudinal adaptation, learning, retention, or forward transfer;
- causal effects of individual mutation operators;
- semantic equivalence of original and evolved task consequences;
- reliable model ranking under clustered/repeated uncertainty;
- validated root-cause error percentages;
- professional workflow quality, user utility, safety, or deployment readiness;
- representativeness of production tool evolution or credentialed consequential tools;
- reproducibility of the benchmark or empirical results from an available release;
- a universal or “standard” benchmark of agent adaptability.

## Transfer to `skill-bench`

## Concrete changes

### 1. Add a version-pair invariant record to future dynamic-environment pilots

For every old/new environment pair, preserve:

- immutable environment, adapter, tool-schema, implementation, dependency, and observation hashes;
- a typed diff (`additive`, `subtractive`, `breaking`, `description_only`, `behavioral`, `dependency`, `availability`);
- declared invariant user obligations and allowed changed obligations;
- old-workflow-on-new and new-workflow-on-old compatibility witnesses where applicable;
- task-specific old/new artifact or state postconditions;
- semantic equivalence evidence, authority, unresolved differences, and fair public basis;
- environment-invalid, migration-required, and task-no-longer-equivalent outcomes.

Existing benchmark-bundle, task-health, validity-argument, execution-isolation, and longitudinal records can host these fields or linked artifacts; no MCP-specific schema is warranted.

### 2. Report a contrast vector, not ECS alone

Keep at least these separate per task and configured system:

- original-version level;
- reset-agent version effect with paired uncertainty;
- monotone harmful regression and beneficial improvement;
- environment-invalid/missingness rate;
- within-trial recovery opportunity, exercise, success, and cost;
- retained-state minus reset adaptation effect;
- unseen-version transfer;
- artifact/state consequence quality and collateral effects.

Aggregate only after defining the target version/task population, dependence structure, stakeholder loss, and decision threshold. A symmetric dispersion penalty should not erase direction or convert judge noise into “adaptability.”

### 3. Use backward-compatible mutations as negative controls

Description-only edits, optional parameters with proven defaults, and irrelevant tool additions can test whether the agent overreacts to affordance/context changes. Precondition this on deterministic compatibility replay and identical consequence checks. Pair them with genuinely breaking migrations and no-change sham versions. This separates contextual distraction, schema handling, necessary migration, and ordinary run variance.

### 4. Treat mutation and diagnosis as causal hypotheses

Randomize eligible mutations within server/task blocks, freeze one mutation per contrast, balance order, retain no-change controls, and estimate paired effects with task/server clustering. For diagnosis, preserve all candidate symptoms and the evidence chain from first changed observation to action and consequence; do not force one root label without adjudication or intervention evidence.

### 5. Freeze the exposure and information policy

Record whether each arm sees only current schemas, prior schemas, changelogs, documentation, prior trajectories, verifier feedback, or retained memory. A “reset-current” arm measures fresh compatibility; a “history-plus-change-note” arm measures use of explicit migration evidence; a retained-state arm measures learning only if state transitions are audited and later tested on untouched equivalent forms.

## Next actions and queue decision

No new build task was added. The evidence refines existing executable homes rather than revealing a separate subsystem: benchmark-bundle component/version identity, task-health environment histories, validity arguments, execution envelopes, and longitudinal reset/retention arms already cover the required machinery. The next useful implementation is to apply the version-pair invariant and contrast vector when a real pilot changes one of its tool or environment dependencies, not to build an MCP-only benchmark.
