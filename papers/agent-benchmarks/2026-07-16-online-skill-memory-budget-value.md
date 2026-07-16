# Online skill and memory value: budget parity is necessary, but allocation effects remain unidentified

## Source and review status

**Deep review; no implementation release.** I read the complete immutable arXiv v1 paper, including implementation details, prompt changes, failure audits, and per-run tables. I also fetched the complete paper-linked project page. It links only to arXiv and exposes no code, data, trajectories, task order, configuration manifest, or analysis artifacts.

- **Paper:** Sina Hajimiri et al., *Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents*, arXiv:2606.15017v1 (12 June 2026), <https://arxiv.org/abs/2606.15017v1>
- **Local PDF:** `data/papers/pdfs/2606.15017v1-online-skill-memory-budget.pdf` (18 pages; SHA-256 `bf3e2ada6e5e4dc8a69af4a0a728c4d1f0317d2c16b1cc69c64e96d87e7c5836`)
- **Local text:** `data/papers/text/2606.15017v1-online-skill-memory-budget.txt` (SHA-256 `5755ea4164c28041d5aba8be1099bc35d9ce3ffaeedf28c8c489cb4b56091816`)
- **Metadata:** `data/papers/source/2606.15017v1/metadata.xml`
- **Project-page capture and acquisition record:** `data/sources/releases/2606.15017v1-online-skill-memory-budget/provenance.json`

The immutable metadata contains no withdrawal notice. Because no study release is available, all empirical details below are paper reports rather than independently replayed results.

## One-sentence contribution

The paper correctly reframes online skill, workflow, and memory augmentation as a **resource-allocation treatment** whose auxiliary calls and injected context must be charged against direct acting, and reports that a longer, pruned vanilla actor sits on a better success–token frontier than AWM, ASI, or ReasoningBank in the tested configurations; however, approximate rather than enforced budget matching, a compound vanilla control, order-dependent online state, only three runs, and no released records prevent attribution to “skills versus more acting” or a general deployment-value conclusion.

## Why this matters to `skill-bench`

This review advances charter objectives A, B, and C by testing two canonical principles: configured-system evaluation and cost-aware usefulness. Its concrete evidence is a full-source audit of an intervention comparison that charges the entire configured package rather than actor calls alone. The clarified uncertainty is whether a skill or memory package creates net value after opportunity cost, task order, persistence, judge defects, reliability, and operational burden are included. This is cross-domain methodological expansion—the web benchmarks are experimental substrates, not a proposed scope boundary. Useful completion is a reusable allocation estimand and evidence ladder, not another memory-specific schema.

## Verdict

The paper's strongest contribution is conceptual and operational: it makes the denominator honest. A workflow extractor, skill synthesizer, verifier, retriever, and the resulting prompt expansion all consume deployment resources. Comparing an augmented ten-step actor with an unaugmented ten-step actor estimates a package contrast under unequal total compute, not the value of allocating a fixed budget to augmentation.

The reported results are substantial within the tested package matrix. Across 475 WebArena tasks in Shopping, Reddit, and Admin, three models, four methods, and three runs, the authors report that `Vanilla-IB` has the highest task-weighted average success for every model. It also uses fewer mean tokens than every augmented method for Gemini 3 Flash and Qwen 3.6-27B. On 33 WorkArena-L1 task types with Qwen, Vanilla-IB and ReasoningBank both report 55.56% success, while Vanilla-IB uses fewer tokens than ReasoningBank. The module decomposition shows a credible “double charge”: auxiliary inference consumes tokens directly, and retrieved material enlarges every later actor prompt (main pp. 5–7, Tables 1–3).

But `Vanilla-IB` is not actually token-matched trial by trial. It raises the horizon from 10 to 15 steps **and** applies accessibility-tree pruning; 15 steps are chosen as a practical approximation because augmented costs vary by task and method. Some vanilla trials exceed some augmented budgets, and many leave budget unused (p. 5). The pruning ablation usefully shows that the longer horizon drives most success improvement while pruning drives token reduction (p. 8, Table 5), but it does not create a randomized fixed-budget allocation experiment. Therefore the evidence supports a narrow claim:

> For the tested paper-defined configurations and reported runs, a 15-step actor with deterministic accessibility-tree pruning had a better observed aggregate success–token frontier than the tested online AWM, ASI, and ReasoningBank packages.

It does **not** establish that extra actor steps dominate online reusable knowledge under a truly fixed budget, that the result transfers to offline/amortized skills, that module-free operation minimizes dollar/latency/energy/human cost, or that online skill and memory modules lack conditional value.

## Research question and estimand

The explicit question is whether, under a fixed inference budget, tokens should be allocated to online reusable-knowledge machinery or to additional direct environment interaction (pp. 1–2). This is better posed as a family of estimands:

1. **Configured-package frontier:** success and reliability as functions of total realized resources for each complete system.
2. **Allocation effect at budget `B`:** outcome difference when the same admissible resource envelope is allocated to augmentation versus direct action.
3. **Module mediation:** whether a candidate lesson is generated, retained, retrieved, presented, adopted, and causally changes action or outcome.
4. **Amortized portfolio value:** discovery plus maintenance cost divided across future eligible uses, including expiry, transport, and parallelism.

The paper directly estimates only a sparse version of (1). It approximates (2), audits pieces of (3), and explicitly excludes offline amortization in (4). That distinction should control how `skill-bench` reports skill efficacy.

## Methodology and system

### Tasks and repeated sequence

WebArena contributes 187 Shopping, 106 Reddit, and 182 Admin tasks. WorkArena-L1 contributes 33 ServiceNow task types; the paper reports three seeds per type. The online methods process tasks sequentially and use earlier trajectories to alter later behavior (main pp. 4–5). The paper does not disclose task order, whether order changes across runs, reset boundaries, category batching, or order seeds. Since learned state and reuse opportunity depend on predecessor tasks, “three independent runs” do not separate model/environment randomness from curriculum realization.

### Treatments

The compared packages are (pp. 4–5):

- **AWM:** induces natural-language workflows from prior trajectories and retrieves them later.
- **ASI:** synthesizes, verifies, stores, and invokes Python functions wrapping browser actions.
- **ReasoningBank:** creates and retrieves reasoning lessons from successes and failures.
- **Vanilla-IB:** no cross-task auxiliary state, a 15-step horizon instead of 10, and deterministic pruning of duplicated accessibility-tree text.

Vanilla-IB, AWM, and ASI use the same ASI-derived codebase and prompts; ReasoningBank uses its own agent logic but is moved to the common BrowserGym evaluation harness (Appendix A, p. 13). Actor temperature is zero for Vanilla-IB/AWM/ASI but 0.7 for ReasoningBank because its default is retained. This preserves each method's authored package but weakens component-level causal attribution: method, prompt/control logic, temperature, and module all vary.

For GPT-5.4-mini, the authors append instructions requiring a reasoning summary, forbidding clarification, and enforcing an action format because augmentation induction depends on textual reasoning. The same prompt is applied to every method, which is symmetric at the prompt level but not at the utility level: the augmentation packages consume the trace, while vanilla does not need it (Appendix C, pp. 13–14). The authors acknowledge that this leaves an unmeasured efficiency advantage for vanilla.

### Resource accounting and outcomes

Success is the native task result. Total tokens include actor and all auxiliary prompts/completions. The paper reports means and sample standard deviations over three runs, plus actor/module decomposition for Gemini and Any-of-3/All-of-3 on Shopping (pp. 5–8). This is materially better than actor-only accounting.

Still missing are cached-token policy, provider-specific token counting, dollar prices, latency, parallel worker occupancy, GPU time/energy, module storage, retries, judge calls, environment-reset cost, implementation labor, and human review. Token count is one resource coordinate, not total cost. Tokens are also not equivalent across Gemini, GPT, and self-hosted Qwen, or between prompt and completion processing.

## Evidence

### Aggregate frontier

Table 1 reports WebArena task-weighted average success/token pairs:

- Gemini: Vanilla-IB `50.74%, 71.9K`; best augmented success ASI `47.86%, 107.1K`.
- GPT: Vanilla-IB `36.63%, 90.4K`; best augmented success ASI `32.14%, 101.4K`; AWM and ReasoningBank use slightly fewer aggregate tokens but have materially lower success.
- Qwen: Vanilla-IB `47.44%, 93.1K`; best augmented success ASI `45.61%, 127.7K`.

On WorkArena-L1, Vanilla-IB and ReasoningBank both report `55.56%`, with `109.4K` versus `120.3K` tokens; AWM reports `53.53%, 102.8K` (p. 6, Table 2). These observations put Vanilla-IB on the reported Pareto frontier. They do not establish statistical dominance: there are no paired task-level differences, confidence intervals, hierarchical models, multiplicity controls, or equivalence/non-inferiority margins.

### Budget sweep and compound-control ablation

On Gemini Reddit, increasing vanilla's horizon closes and then exceeds AWM success while remaining below AWM token use through 25 steps (pp. 6–7, Figure 2). This is useful dose–response evidence for one model/domain pair, but the figure does not provide repeated-run uncertainty at every horizon or perform the corresponding budget sweep for each augmentation method.

Table 5 separates horizon and pruning. Relative to plain ten steps, 15 steps generally raise success; pruning consistently lowers tokens, but success effects vary. This demonstrates that the strong baseline is a package built from two mechanisms. It does not isolate an allocation effect at exactly equal realized budgets.

### Reliability

Shopping Any-of-3 and All-of-3 differ sharply around each three-run mean. For Gemini Vanilla-IB, the mean is 47.77%, Any-of-3 is 54.01%, and All-of-3 is 42.25%; for GPT ReasoningBank, the corresponding values are 26.38%, 35.29%, and 17.64% (pp. 7–8, Table 4). This demonstrates task-level instability despite similar aggregate run means.

The paper calls these “bounds on latent capability,” but that wording is too strong. Any-of-3 is an optimistic finite-repeat union and All-of-3 a stringent finite-repeat intersection under one task order/environment policy. Neither bounds a stable latent capability without assumptions about independent draws, stationary task success probability, invalid runs, online state, and environment faults. They are nevertheless useful **repeat-profile observations**.

### Module quality failures

The appendices are the paper's most diagnostically valuable evidence:

- **ASI verification confounds:** induced functions can fail immediately, after which primitive actions recover and the episode passes, causing a broken function to be stored. In GPT Shopping, 32 of 44.3 average verification attempts fail before the second action; 54.2% of those failures recover and are retained (pp. 14–15, Table 6).
- **AWM label contamination:** 49.5% of Gemini and 52.3% of GPT Shopping induction events originate from trajectories that the ground-truth evaluator marks failed, because induction trusts an incomplete LLM judge (p. 15, Table 7).
- **ReasoningBank label contamination:** 52.9% of Gemini and 59.5% of GPT Shopping success-labeled memories arise from ground-truth failures; false negatives also occur (pp. 15–16, Table 8).
- **Evidence-view insufficiency:** the quality-control judge receives textual output and sometimes terminal browser state, not the intermediate states needed to verify navigation-dependent claims. More model capability cannot recover absent evidence (p. 16).
- **Invocation pressure:** retrieved ReasoningBank items are mentioned 8–12 times per task on average, with at least one mention in over 95% of Gemini tasks and over 75% of GPT tasks. This establishes presentation/reference, not correct adoption or causal effect (pp. 15–16).

These audits explain why module overhead can actively degrade performance: online augmentation is not merely extra context; it is a stateful evidence-production pipeline whose false promotions create downstream treatment contamination.

## Unique insight

The paper's deepest transferable lesson is that “skill value” has **two denominators and one dependency graph**:

1. **Opportunity denominator:** tasks on which a candidate skill could validly apply under the current environment/interface/version.
2. **Resource denominator:** all resources consumed to induce, verify, store, retrieve, inject, interpret, execute, repair, and retire it, including the direct-action opportunity cost.
3. **Dependency graph:** an upstream trajectory and judge decision can alter the shared module state used by every downstream task.

A package can look helpful if only successful invocations are counted, only actor tokens are charged, or corrupted predecessor state is ignored. Conversely, a package can look wasteful during a short online evaluation but become valuable after offline cost amortization over a stable, high-reuse deployment. Therefore `skill-bench` should not report one undifferentiated “skill gain.” It should report:

- eligibility and opportunity;
- candidate generation and authority;
- verification evidence sufficiency;
- promotion correctness;
- retrieval/presentation;
- adoption/invocation;
- local effect and downstream effect;
- complete resource ledger;
- persistence/order sensitivity;
- amortization horizon and expiry.

A second insight is that **fault repair changes the estimand for stateful systems**. The authors immediately rerun infrastructure-failed tasks so a module can still learn from them (p. 9). For a stateless actor, substituting the rerun is local. For a stateful online method, retry timing changes both the current score and all future shared state. A valid protocol must predeclare whether invalid episodes are retried in place, omitted with a null transition, or replayed from a checkpoint; otherwise “repair” is an unrecorded treatment intervention.

## Limitations and validity threats

1. **No released study artifacts.** Code, trajectories, task orders, seeds, module states, token ledgers, judge records, and analysis scripts cannot be inspected or replayed.
2. **Approximate budget matching.** A fixed 15-step horizon is not an exact equal-resource intervention; realized budgets overlap and leave different headroom.
3. **Compound vanilla treatment.** Extra steps and accessibility-tree pruning both differ from the nominal vanilla actor.
4. **Asymmetric treatment utility of the common prompt.** Required reasoning text feeds induction but is overhead for vanilla.
5. **Configured methods differ beyond module type.** ReasoningBank retains a different control stack and temperature.
6. **Unreported task order.** Online learning is path-dependent, but order identity/randomization and category boundaries are absent.
7. **Only three runs.** Sample standard deviations do not support reliable uncertainty for task-clustered, order-dependent contrasts.
8. **No paired or hierarchical inference.** Aggregate means omit task-level covariance, domain/model interactions, and multiple comparisons.
9. **Any/All terminology overreaches.** Three-run unions/intersections are repeat profiles, not assumption-free latent-capability bounds.
10. **Retry policy can alter future treatment.** Immediate infrastructure-failure reruns affect the shared state stream; counts and exact transition semantics are not reported.
11. **Success-only primary quality.** Native endpoint success does not measure collateral effects, professional artifact quality, recovery severity, or accepted alternative paths.
12. **Incomplete total-cost accounting.** Tokens omit latency, prices, GPU/energy, concurrency, storage, maintenance, judge expense, and human labor.
13. **No amortization experiment.** The online setting cannot answer when an offline library repays discovery cost over repeated stable use.
14. **No cross-task transfer design.** Later tasks may share templates or categories with earlier tasks, but source→target similarity, novelty, and leakage are not reported.
15. **Module use is only partly observed.** Memory mentions show exposure/reference, not faithful adoption or counterfactual action change.
16. **Judge errors contaminate the treatment.** LLM quality control lacks sufficient trajectory state; the comparison partly measures implementation defects in promotion policy.
17. **Task families are narrow.** Three WebArena domains and WorkArena-L1 under one model do not establish general knowledge-work allocation effects.
18. **Model/version and service transport are unknown.** Results bind to named 2026 models, prompts, harness, and environment versions not preserved in a manifest.
19. **No safety or consequence-adjusted utility.** More steps and retrieved procedures may produce different harmful or irreversible actions even at similar endpoint success.
20. **No independent release correspondence.** The project page provides presentation evidence only.

## Reproducibility and operational realism

Operational realism is moderate. The systems interact with browser environments, consume large realized contexts, experience server/browser faults, maintain cross-task state, and face dynamic element identifiers. The paper usefully treats parallelism and fault tolerance as operational properties: stateless tasks can run independently, while online shared state serializes work and makes local replay insufficient (pp. 8–9).

Experimental reproducibility is poor. The paper names upstream codebases and a common harness, but no exact commits, dependency lockfiles, task order, prompts as executed, state snapshots, raw outputs, token receipts, environment versions, or result matrices are released. Exact reproduction would require immutable configured-system manifests, per-trial component/token/latency records, shared-state hashes before and after each task, task-order seeds, infrastructure-invalid labels and retry transitions, native evaluator outputs, all candidate/promotion/retrieval records, and analysis code.

## Claim ladder

| Claim | Status from this source | Promotion evidence |
|---|---|---|
| Auxiliary modules create direct and injected-context token overhead | Supported for the reported packages; Gemini decomposition is explicit | Released per-call ledgers and replay across configurations |
| Vanilla-IB is on the reported tested success–token frontier | Supported descriptively | Raw paired task records and uncertainty preserve the result |
| Fixed-budget direct acting outperforms augmentation | Not identified: budgets are approximate and treatment is compound | Enforced per-trial budgets, matched pruning/prompts, randomized allocation |
| Online modules reduce reliability | Not established generally; three-run profiles and module defects are suggestive | Order-randomized repeated streams with invalid handling and clustered inference |
| Skill/memory modules are not worth their cost | Unsupported outside tested online packages | Full resource/loss function, deployment horizon, amortization, maintenance, safety |
| Offline reusable skills lack value | Explicitly out of scope | Separate discovery and serving ledgers over stable repeated eligible work |
| Result transfers to realistic knowledge work | Weakly supported by one WorkArena-L1/model package comparison | Diverse professional tasks, artifacts, consequences, models, repeated orders |

## Transfer to `skill-bench`

### Retain

1. Charge every configured component, including module prompts/completions and context injected into later actor calls.
2. Compare a skill package against a strong budget-aware actor, not only a nominal equal-step baseline.
3. Preserve per-component resource use rather than one pooled token total.
4. Repeat task-level trials and retain the response matrix; aggregate run means hide instability.
5. Treat online promotion quality and shared-state lineage as part of the intervention, not invisible scaffold internals.
6. Record parallelism and fault-repair semantics because they affect operational cost and the treatment itself.

### Repair before reuse

1. Predeclare a resource vector—not just tokens—and enforce or model budget parity per task.
2. Factor direct-action budget, observation compression, skill access, skill generation, and persistence rather than bundling them.
3. Randomize or counterbalance task order and preserve shared-state hashes at each transition.
4. Require quality-control evidence views sufficient for the claimed lesson; recovery after a failed skill call must not verify that skill.
5. Separate exposure, invocation, adoption, and causal outcome effect.
6. Evaluate online, offline-amortized, stale-environment, and cross-domain transfer regimes separately.
7. Use paired task contrasts or hierarchical models with task/order/run clustering and predeclared equivalence or decision thresholds.

### Reusable allocation record

Existing configured-system, metric-monitoring, task-health, longitudinal, trace/recovery, validity-argument, and compounding-lesson contracts can absorb this evidence. A skill ablation should instantiate, not merely describe:

```yaml
allocation_trial:
  eligible_task_and_order_seed: ...
  initial_shared_state_hash: ...
  resource_envelope:
    prompt_tokens: ...
    completion_tokens: ...
    tool_calls: ...
    wall_time: ...
    compute_and_price_basis: ...
    human_review_minutes: ...
  allocation:
    direct_observe_act: ...
    candidate_generation: ...
    verification: ...
    retrieval_and_injection: ...
    repair_and_maintenance: ...
  module_flow:
    opportunity: ...
    generated_candidate: ...
    verification_evidence_sufficient: ...
    promoted: ...
    retrieved: ...
    invoked_or_adopted: ...
    local_and_downstream_effect: ...
  final_shared_state_hash: ...
  invalid_or_retry_transition: ...
  outcome_and_consequence_vector: ...
```

## Action items

1. **Refine the next procedural-skill pilot analysis, without adding a new subsystem.** Add the allocation record above to one existing matched skill/no-skill design; report direct acting, intervention overhead, injected-context overhead, trial outcome, and reliability separately. This is a requirement refinement for existing configured-system/metric/longitudinal machinery, not a new queue task.
2. **Use a small order-aware factorial before making a skill-value claim.** Compare equal-envelope `baseline`, `stronger direct actor`, `offline public skill`, and `online evolving skill` conditions with the same observation pruning, prompt obligations, grader, and retry policy. Counterbalance at least two task orders and freeze candidate/promotion evidence. The licensed result should remain a configured-package allocation effect until cross-task and cross-domain transport are directly tested.

No new build task is added: the repository already has the necessary schema homes and a healthier consolidation/build backlog. The nonduplicate contribution is the allocation estimand and the warning that online invalid-run repair mutates future treatment.