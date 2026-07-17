# Paper Review: DevicesWorld — Cross-Device State and Verifier Validity

- **Paper:** https://arxiv.org/abs/2607.13465v1
- **Authors:** Huatao Li, Xinwei Geng, Yuheng Wang, Yutong Li, Runde Yang, Hantao Chen, Shu Yao, Jingru Fan, Xuhui Ren, Yuanyuan Zhao, Fei Huang, Chen Qian
- **Date read:** 2026-07-17
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, submitted 15 July 2026
- **Local PDF:** `data/papers/pdfs/2607.13465v1-devicesworld.pdf` (21 pages; SHA-256 `cc72e228f20018b32a34d1d77ad90b625d286ccce842fe0b7311e9d1441f4163`)
- **Local text:** `data/papers/text/2607.13465v1-devicesworld.txt` (SHA-256 `e3decae7819f431ce3b3fa347e17889225aaabb5931382303504878cb05c21ff`)
- **Official repository inspected:** https://github.com/AgenticOrgLab/DevicesWorld at commit `91653ecf565052f52b95524c4f6abe9aa15aa4ed` (16 July 2026)
- **Release provenance:** `data/sources/releases/2607.13465v1-devicesworld/provenance.json`
- **Tags:** cross-device, heterogeneous-environments, distributed-state, strict-conjunction, partial-checks, cleanup, reliability, release-unavailable

## One-sentence contribution

DevicesWorld proposes a 6,140-task executable benchmark that routes actions across up to four Android, Linux, and simulated-smart-home instances and jointly checks distributed endpoint state; its strongest transferable contribution is the distinction between **local action success, persisted endpoint state, and joint workflow completion**, but the unreleased instrument, unstated 200-task subset identity, one-attempt design, equal-weight partial checks, undocumented failure coding, and absent reset audit prevent independent support for its scale, reproducibility, diagnostic, reliability, transfer, or professional-validity claims.

## Why this matters for skill-bench

Consequential knowledge work often crosses substrates even when the substantive task is not “computer use”: a fact is read from one system, transformed under a policy in another, entered into a third, and expected to remain consistent across records. DevicesWorld makes the **location and role of state** explicit. It also correctly warns that issuing a write, seeing a plausible interface, and observing a persisted result are different events (Section 4.3.3, pp. 14–15).

The paper therefore advances charter objectives A and B by exposing a cross-domain measurement boundary: a strict conjunction over endpoint checks can establish bounded final-state conformance, but it cannot by itself establish that information was acquired from the intended source, transferred without semantic loss, used under the right authority, or produced a professionally acceptable consequence. This is a cross-substrate mechanism study, not a reason to narrow `skill-bench` to phones, IoT, or GUI operation.

## Research question and claim boundary

The paper asks whether configured agents can acquire information, choose device targets, operate incompatible interfaces, preserve cross-device dependencies, and jointly satisfy final conditions distributed across Android, Linux, and SmartHome environments (Sections 1–2, pp. 1–5).

The manuscript provides a coherent proposed task contract, aggregate results for five configured systems, and a failure vocabulary grounded in endpoint and trajectory symptoms. The reported tables are internally consistent with **200 attempted tasks per system and 1,000 total attempts**: success counts implied by 0.5-point increments are 24, 19, 24, 21, and 25; the corresponding failed-run denominators are 176, 181, 176, 179, and 175. Budget-exhaustion percentages imply 44, 112, 67, 70, and 77 runs, totaling 370/887 failed runs = 41.7%; the remaining 517/887 = 58.3% are failed completion declarations (Table 1 and Figure 4, pp. 9–11). This arithmetic reconciles the termination headline, but the paper never states the subset size or publishes its identifiers.

The evidence does **not** independently establish that 6,140 executable tasks exist, that the selected 200 are representative of them, that initialization/verifiers/cleanup are correct, that 28.7% corresponds to a reproducible item set, that device-role or information-transfer failures were reliably coded, or that 12.5% is an operational reliability estimate. The official repository still contained only `README.md` and a teaser image at the review-time re-check; it said “Benchmark coming soon.”

## Methodology and system

### Task and environment model

A task contains a natural-language goal, concrete devices, task-specific initialization, heterogeneous observations and actions, generated results, a verifier returning strict success and partial score, and cleanup. The joint state is modeled across Android, Linux, and SmartHome; every action names a target device. Android builds on AndroidWorld, Linux on OSWorld, and SmartHome is a new simulation whose state must be queried explicitly (Sections 2 and 3.2, pp. 3–6).

The proposed suite contains 6,140 tasks, with up to four concrete device instances. The paper names direct transfer, transformation, multi-source integration, synchronization, conflict resolution, conditional action, infeasibility reporting, multi-endpoint consistency, and device control as task patterns. It lists common mobile apps, desktop applications/files, and 11 smart-home device categories (Section 3.1, p. 5). No counts by pattern, device topology, application, horizon, verifier type, source/output role, or difficulty are provided.

The formulation usefully separates the target device from the action. It does not encode a task-level dependency graph, claim provenance, source authority, information identity, permissible transformation, or collateral-state constraints. Those relations are discussed in prose but are not visible in an inspectable schema.

### Construction and quality control

The pipeline samples a task configuration; uses an LLM to design scenario semantics and source→transformation/decision→output→outcome dependencies; applies an “independent review-and-repair” stage; deterministically creates format-valid resources; assembles setup, evaluation, cleanup, and limits; then runs deterministic validation, runtime tests, repairs, and exclusion (Section 3.3, pp. 6–8).

This is a sensible projection pipeline because it recognizes several common benchmark defects: inaccessible prerequisites, unsupported operations, malformed resources, setup that pre-solves the task, hidden verifier obligations, and incomplete cleanup. The paper says intended outcomes are tested to pass, missing or incorrect outcomes to fail, and cleanup to remove “principal task states” (pp. 6–7).

However, the evidence is a method description rather than an audit. The paper does not identify:

- generator/reviewer models, prompts, versions, or sampling settings;
- what “independent” means or whether reviewers were people, models, or programs;
- human author/reviewer counts, qualifications, agreement, or labor;
- candidate, rejection, repair, and finalization denominators;
- proportions that are generated, task-specific-builder-derived, or manually designed;
- a natural-user-needs sampling frame;
- positive/negative verifier calibration cases or alternative valid solutions;
- full-state cleanup diffs, repeated initialization checks, or cross-task order tests.

The claim that release review checks naturalness and requirement/verifier alignment is therefore an undocumented procedure, not evidence of user, expert, ecological, or professional validity.

### Evaluation design and configured systems

Four direct baselines—GPT-5.5, Qwen3.7-Plus, Gemini-3.1-Pro-Preview, and Claude Opus 4.8—use the same stated direct protocol and context settings. UFO3 uses GPT-5.5 but adds hierarchical planning, device agents, and an output adapter. Every task allows up to 50 actions; direct systems receive current observations/screenshots, prior action/feedback, and textual history from the latest ten steps; temperature is zero (Section 4.1, pp. 8–9).

The fixed subset is described as coverage-driven and stratified, but selection also “prioritize[s]” natural instructions, clear sources, repeatable initialization, and automatically verifiable outcomes. This is a **health-selected evaluation subset**, not a random sample from the 6,140. The paper gives no stratum counts, selection code, task IDs, exclusions, or weighting back to the suite. Neither the 6,140-task suite nor the fixed subset can be inspected.

One apparent attempt per system-task is reported. Temperature zero does not remove provider, GUI, emulator, application, timing, or service variation. There are no repetitions, seeds, confidence intervals, paired tests, missing/invalid/retry policy, run dates, provider snapshots, environment versions, or task-clustered uncertainty. UFO3 is appropriately described as a package comparison rather than a clean planner ablation: it changes prompts, history, action representation, orchestration, and internal decision rounds (pp. 9–10, 14).

### Scoring

Strict success requires every required condition. Partial task score is the fraction of enabled scoring conditions passed; Mean Score macro-averages task scores (Section 4.1, p. 9). This preserves task weighting despite different numbers of checks, but it gives every check within a task equal weight regardless of dependency position, semantic importance, difficulty, reversibility, or stakeholder consequence.

The reported 28.7% concerns failed runs with at least one **final score-enabled condition** satisfied (Sections 4.2 and 4.3.4, pp. 10, 15). It is evidence of nonzero checked endpoint attainment, not necessarily evidence that the agent acquired the required information, transferred it, made useful progress, or left a partially useful artifact. A trivial file-existence check and a high-consequence correct action both count as “at least one.” Conversely, useful intermediate source acquisition is invisible unless represented by a final scored check.

The exact partial-positive count is unavailable. With 887 inferred failures, 254 gives 28.64% and 255 gives 28.75%; either could be displayed as 28.7 depending on the unreported rounding convention. Item-level scores and aggregation code are required to reconcile it. Mean Scores likewise cannot be reproduced or interpreted without check counts and semantics.

## Evidence and results

Table 1 reports success of 9.5–12.5% and Mean Score of 0.201–0.262. UFO3 has the highest strict success (12.5%, inferred 25/200), while GPT-5.5 has the highest Mean Score (0.262). The small observed differences are not accompanied by uncertainty, and the authors appropriately avoid claiming a significant winner (pp. 9–10).

The reported zero successes on tasks involving all three environment classes is uninterpretable without the number of such tasks per system and their difficulty/profile. It may identify a hard stratum, but it cannot estimate three-class success or isolate heterogeneity from longer horizon, more checks, more devices, or harder local interfaces (p. 10).

Costs are operationally striking but under-specified. Average tokens per task range from 278k to 606k and duration from 4.5 to 12.0 minutes. The paper reports no input/output split, screenshot/token conversion, planner/device-agent inclusion boundary, dollar cost, cached-token policy, failed-call accounting, or provider rate. It acknowledges that UFO3 action counts omit planner/device-agent decision rounds and durations include service/device latency, limiting strict comparison (pp. 9–10).

### Failure analysis

The authors inspect trajectories, action feedback, and evaluator traces, first separating budget exhaustion from failed completion declarations and then assigning each failure one primary category based on the “earliest major deviation that dominates” later failure (Section 4.3, pp. 10–15).

Budget-exhausted categories are source-information acquisition (B1), target-side operation (B2), and recovery after explicit error (B3). Failed completion declarations are omitted subgoal (D1), device-role/target confusion (D2), incorrect output/state (D3), unconfirmed persistence (D4), and incomplete distributed conditions (D5). This vocabulary is useful because it distinguishes attempted action from persisted state and local completion from global closure.

But the coding study is not reproducible. The paper does not report coder identities, codebook, training, blinding, adjudication, agreement, sampled versus complete trajectories, missing/ambiguous labels, or raw annotations. “Earliest major deviation” is a causal judgment, not a direct observation. B1 can be GUI localization or retrieval; B2 can be grounding, unsupported interface behavior, or planner payload loss; B3 explicitly mixes model and runtime/tool instability; D3 can be source-value corruption, representation error, or verifier intolerance. Assigning one category forces dependency-chain failures into mutually exclusive bins and discards secondary causes.

The paper often uses careful language—especially that not every failure is coordination and that UFO3 differences are descriptive. Even so, statements about weak role maintenance, information preservation, or recovery are hypotheses from selected traces unless the underlying access, transfer, role-state, attempted action, endpoint, and environment-error events are separately instrumented.

## Unique insight

DevicesWorld's deepest transferable insight is an **edge-and-endpoint validity chain**:

`source available → source accessed → value/claim captured → source identity and authority retained → permitted transformation performed → target device selected → action attempted → endpoint state persisted → collateral state acceptable → all distributed postconditions jointly satisfied → cleanup/reset verified`

A final conjunction observes only the right end of this chain. It cannot determine which earlier edge failed unless trace events and dependency links are recorded. Likewise, a correct source and target endpoint do not prove the intended transfer path: the target value might be guessed, leaked in prompts/history, independently retrieved, or reconstructed from another source. For `skill-bench`, cross-substrate tasks should therefore make **dependency-edge fidelity** and **endpoint-state validity** separate score/diagnosis families.

A second insight is that “device” should be generalized to a **state-bearing role-bound endpoint**. Two phones of the same class can differ because one is the authoritative source and another the required destination; two filesystems or SaaS tenants can have the same distinction. Persistent semantic role binding matters more than hardware labels. This transfers directly to a professional workflow spanning an inbox, ticketing tenant, spreadsheet, and approval system.

A third insight is negative: **strict conjunction is closure evidence, not coordination evidence**. A task with more endpoints, checks, local failure opportunities, and horizon will have lower success even if cross-device coordination adds no distinct difficulty. A valid coordination claim needs matched tasks that hold local operations, information, checks, and budgets constant while varying the dependency topology or role-binding requirement.

## Limitations and validity threats

1. **The benchmark is unreleased.** The official repository contains only a README and teaser; no task, runtime, verifier, result, or trajectory claim is independently inspectable.
2. **The 6,140 count is unauditable.** There is no deduplication, validity, pattern, application, topology, difficulty, or authoring-origin ledger.
3. **The evaluation subset is unnamed.** Its size is inferable as 200 per system but not stated, identified, or released.
4. **Selection is health-conditioned.** Prioritizing repeatable, natural, automatically verifiable tasks can produce a favorable operational subset and an unknown target population.
5. **No suite-to-subset transport argument exists.** Results on selected healthy tasks do not estimate performance over all 6,140 or realistic user demand.
6. **No repeated reliability evidence exists.** One attempt per task cannot estimate completion probability, environmental variance, or operational reliability.
7. **Temperature zero is insufficient control.** GUI, emulator, application, provider, timing, and adapter behavior remain stochastic and mutable.
8. **No uncertainty is reported.** Tasks and generated variants may be clustered, yet scores are presented as unqualified point estimates.
9. **Zero three-class successes lacks a denominator.** The result cannot support a prevalence or comparative claim.
10. **Task generation and review are under-specified.** Models, prompts, humans, independence, qualifications, labor, attrition, and agreement are absent.
11. **Naturalness is asserted, not validated.** No user-demand frame, domain expert review, user study, or observed workflow evidence is reported.
12. **Professional consequence is absent.** No stakeholder consumes an output, and the IoT substrate is simulated.
13. **Task semantics are not inspectable.** Fair public basis, authority, ambiguity, infeasible-request policy, and alternative valid solutions cannot be audited.
14. **Verifier soundness/completeness is not measured.** Claimed positive/negative runtime tests have no cases, counts, results, or legitimate-alternative study.
15. **Equal-weight checks have unvalidated semantics.** Check fractions do not equal useful work, information transfer, or consequence.
16. **The 28.7% partial-progress label overreaches.** It records at least one final check, not necessarily useful or causally connected progress.
17. **Partial-positive counts are unreconciled.** With 887 inferred failures, the rounded percentage does not identify an exact numerator.
18. **Source access and semantic transfer are not separately scored.** Endpoint correctness cannot prove the intended information path.
19. **Device-role state is inferred, not observed.** Wrong-location outputs suggest role confusion but do not measure internal role binding.
20. **Attempt and persistence are conflated in aggregate scores.** The failure taxonomy distinguishes them, but public metrics do not.
21. **Collateral changes are unreported.** Required endpoints can pass while unrelated state is damaged unless explicit negative checks exist.
22. **Cleanup is weakly specified.** Removing “principal task states” or “reducing” residual state is not full reset equivalence.
23. **No cleanup order audit exists.** Cross-task leakage, contamination, and order effects are unmeasured.
24. **Environment identity is absent.** Images, application versions, locale, device dimensions, clocks, network policy, and dependency locks are not reported.
25. **Tool/runtime failures contaminate model attribution.** B3 explicitly mixes agent errors with timeouts and adapter instability.
26. **Failure coding is unaudited.** No coder protocol, agreement, adjudication, sampling rule, or released labels support prevalence claims.
27. **Single-primary-cause coding discards chains.** A source failure can mask target, persistence, and closure opportunities.
28. **The causal rule is subjective.** “Earliest major deviation that dominates” requires counterfactual judgment, not just timestamping.
29. **UFO3 is a treatment bundle.** Planner, prompts, histories, orchestration, and adapters differ, so architecture effects are not isolated.
30. **Resource accounting is incomplete.** Very high token counts lack modality, cache, input/output, internal-round, failure, and dollar-cost boundaries.
31. **Changing device availability is not tested.** It motivates the paper but no availability perturbation or recovery experiment is described.
32. **Security and authorization are absent.** Cross-device data movement and smart-home actions need consent, least privilege, and prohibited-consequence checks.
33. **Reproducibility is claimed prematurely.** A prose specification and placeholder repository cannot reproduce tasks or results.
34. **No contamination analysis is reported.** Public task generation, model-assisted authoring, and future public release can expose task/verifier patterns.

## Reproducibility and operational realism

Reproducibility is currently limited to reading the immutable manuscript and checking arithmetic implied by its aggregate table. The local PDF and extraction span all 21 pages and are hash-pinned. The official repository was re-checked at review time through GitHub's API: HEAD remained `91653ecf565052f52b95524c4f6abe9aa15aa4ed`, and the root still contained only `README.md` and `assets/`. The pinned local archive and commit metadata preserve that timing boundary.

The following are unavailable: 6,140 tasks, fixed-subset IDs, builders, device images/emulators, setup, action routing, verifiers, cleanup, dependency records, raw attempts, trajectories, evaluator traces, aggregate scripts, environment locks, and licenses for the benchmark package. A zero-model setup/verifier/cleanup reproduction is therefore impossible. The manuscript's executable, reproducible, and diagnostic claims remain author reports.

Operational realism is mixed. Actual heterogeneous interfaces, multiple same-type instances, distributed source/output state, up to 50 actions, explicit queries, persistence checks, infeasible-request patterns, and cleanup are valuable. But synthetic generated tasks, simulated SmartHome state, unknown user-demand sampling, no affected stakeholder, no authorization or privacy policy, selected healthy tasks, one-shot attempts, and absent reset evidence sharply bound real-world inference.

## Transfer to skill-bench: concrete changes

1. **Represent endpoint roles independently of substrate type.** Record stable endpoint ID, environment/store class, semantic role (`authoritative_source`, `transformation_workspace`, `required_destination`, `approval_endpoint`, `verification_endpoint`), authority, and valid interval.
2. **Add typed dependency edges.** Each edge should identify source claim/value, source endpoint and locator, required transformation, target endpoint/field, permitted invariances, confidentiality/authorization, and downstream checks.
3. **Instrument the full information-flow chain.** Separate availability, access, capture, retention, transformation, attempted write, persisted state, and verified consequence before assigning a root cause.
4. **Keep endpoint and global closure scores separate.** Report node/check attainment, dependency-edge fidelity, required conjunction, prohibited/collateral changes, and cleanup/reset rather than collapsing all partials into one mean.
5. **Model prerequisite masking.** If source acquisition fails, target-side and global-verification opportunities are censored or not reached—not evidence that those capabilities failed.
6. **Calibrate strict conjunction against topology.** Create matched forms that vary same-type role binding and cross-substrate edges while holding local operations, information, check count, horizon, and budget as constant as possible.
7. **Require post-write persistence observations.** Record action issued, UI acknowledgement, re-query/reopen, authoritative state, and verifier observation as distinct events.
8. **Add collateral-state and authorization checks.** Correct required endpoints must not excuse unauthorized messages, overwritten source records, privacy violations, or unsafe device actions.
9. **Treat cleanup as measured trial validity.** Capture pre-state, post-evaluation state, cleanup action, post-cleanup diff, residual exceptions, next-trial canary, and invalidation policy.
10. **Preserve complete run accounting.** Report selected, initialized, attempted, valid, retried, failed-provider, failed-environment, scored, and excluded counts by system and topology.
11. **Estimate repeated reliability.** Repeat equivalent tasks under reset and order perturbations; report task/topology-clustered uncertainty and environment-error rates.
12. **Use existing contracts.** These requirements refine benchmark-bundle task projections, traces, artifact views, persistent workspaces, task health, metric monitoring, validity arguments, and trial-accounting machinery; do not create a device-specific schema.

## Action items for repository

- [x] Read the complete immutable arXiv v1 PDF/text with page and section evidence.
- [x] Re-check and archive the official repository at the review-time HEAD.
- [x] Reconcile the implied 200-task-per-system denominator and 887-failure termination accounting.
- [x] Separate device availability, source access, semantic transfer, role binding, attempted action, persistence, endpoint state, collateral state, cleanup, reliability, and consequence claims.
- [x] Record release absence rather than infer task/runtime behavior.
- [x] Add one nonduplicate consolidation task to integrate cross-substrate dependency-edge and endpoint-state boundaries into the canonical synthesis; no device-specific build contract is warranted before release evidence exists.
