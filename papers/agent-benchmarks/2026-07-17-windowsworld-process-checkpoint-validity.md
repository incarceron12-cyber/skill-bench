# WindowsWorld: trajectory-wide checkpoints increase observability but do not establish process or professional validity

## Source and review status

**Deep review, release audited.** I read the complete immutable 20-page arXiv v1 paper, inspected its manuscript source, and audited the complete official repository at the task-specified commit. I read `benchmark.json`, the benchmark runner, VLM evaluator, result summarizer, environment/reset implementation, setup/evaluator documentation, action spaces, and release provenance. I also ran a zero-call static audit over all 181 released task records.

- Paper: Jinchao Li et al., *WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments*, arXiv:2604.27776v1, <https://arxiv.org/abs/2604.27776v1>
- ACL record: <https://aclanthology.org/2026.findings-acl.750/>
- Local PDF: `data/papers/pdfs/2604.27776v1-windowsworld.pdf` (20 pages; SHA-256 `70f2901aec8c35f50f00191548c49597e61a81b3cd7198a5985ccf5d55ab6b80`)
- Local text: `data/papers/text/2604.27776v1-windowsworld.txt` (117,261 characters; SHA-256 `d459b74f4f2261f582b735db80b259233d56c4490ed2259516abc26b5dff949f`)
- Manuscript source: `data/papers/source/2604.27776v1.tar.gz` (SHA-256 `b47840aad4a5a86e45d8674bf10f75ec8d31e46d5d720de11f4160b1eccef903`)
- Official repository: <https://github.com/HITsz-TMG/WindowsWorld>
- Audited commit: `fbccd464f94fec9e284e139f97bf96d0b192f580`
- Release archive: `data/sources/releases/2604.27776v1-windowsworld/HITsz-TMG-WindowsWorld-fbccd46.zip` (SHA-256 `1c40ec3bd1c3c2230cc5c16bf461b4ead1c0540ee2b857354795cb1dfa729da1`)
- Release provenance: `data/sources/releases/2604.27776v1-windowsworld/provenance.json`
- Date read and audited: 2026-07-17

> **Version boundary.** The audited commit is dated 11 May 2026, eleven days after immutable arXiv v1. It is official post-v1 release evidence, not proof of exact manuscript-time code. The release contains no paper-run trajectories, task-level verdict matrix, judge outputs, environment-health ledger, or auditable result table. No Windows VM was available, so no model or environment execution was attempted; the release audit is static and zero-call.

## One-sentence contribution

WindowsWorld usefully packages 181 Windows tasks dominated by multi-application workflows and scores 899 authored milestones from complete screenshot trajectories, but equal-weight trajectory-wide VLM judgments, a terminal-action shortcut for infeasible tasks, invalid released records, an unenforced task-setup contract, single-shot aggregate results, and unvalidated occupation labels limit the evidence to performance on an authored GUI package—not process fidelity, cross-application causality, professional capability, reliability, safety, or readiness.

## Why this matters for skill-bench

This review advances charter objectives A and B through comparative validation research. WindowsWorld tests a general benchmark-design hypothesis: **can intermediate observations make long-workflow failures visible without forcing one authored action sequence?** The answer is partly yes. Sparse state descriptions can distinguish early from late observable attainment when terminal success is near floor. Yet the released implementation shows that a “checkpoint” is not automatically a valid process measure. It can be a transient screen appearance, a reversible state, a path cue, a dependent prerequisite, or an independently useful consequence; the headline average erases those differences.

The source is therefore valuable for a general distinction:

- `trajectory evidence that a state appeared`
- `≠ durable stage completion`
- `≠ causal progress toward the terminal outcome`
- `≠ professionally valid process execution`.

This is not a Windows or GUI scope commitment. The same distinction applies to research, analysis, office artifacts, healthcare administration, software work, and any benchmark that awards process credit.

## Research question and defensible claim boundary

The paper asks whether GUI agents can complete realistic, profession-specific cross-application workflows and whether intermediate checkpoint scoring better diagnoses long-horizon failure than final success alone (paper §§1, 3–4, pp. 1–9).

The paper and release support these bounded observations:

1. the authors assembled 181 tasks across 17 named Windows applications, 16 generated personas, and four author-defined levels;
2. 141/181 tasks involve at least two listed applications, and 130 feasible tasks are labeled L2 or L3;
3. the release contains 899 milestone strings, which is 4.97 per task when all 181 records—including L4 records with no milestones—form the denominator;
4. the evaluated configured systems receive substantially more intermediate credit than final task credit on this instrument;
5. the benchmark varies observation package, model/agent package, task level, application count, instruction language, and fixed nominal step budget; and
6. a two-annotator comparison on a selected 100-task trajectory sample reports strong agreement with the Qwen3-VL-Plus judge.

The evidence does **not** establish that the tasks represent any occupation, that application count isolates coordination, that milestones are necessary or sufficient workflow stages, that intermediate fractions are interval-scaled progress, that a transient attained state remained valid, that the VLM saw sufficient authoritative evidence, that the released runner reproduces paper conditions, that model rankings are repeatable, or that low scores imply professional unreadiness.

## Methodology and system

### Task generation and occupational grounding

A DeepSeek-V3.2 generator receives one of 16 persona profiles, application dependencies, difficulty rules, and web search. Automated refinement performs embedding deduplication at cosine threshold 0.85, URL/file checks, dependency rewriting, and metric refinement. Four postgraduate annotators then reject ambiguous, subjective, or unavailable tasks; an environment generator synthesizes supporting files (paper §3.3, pp. 4–5; Appendix D, pp. 16–18).

This is a scalable task-authoring pipeline, not an expertise-elicitation study. The paper reports no observed-work sample, practitioner interview, occupational taxonomy source, task-frequency frame, artifact corpus, expert/novice contrast, role-specific authority check, or downstream recipient review. The 16 labels include malformed released values such as `IT Useristrator` and `Useristrative Assistant`, illustrating that persona text was not a stable occupational instrument. Four postgraduate reviewers were paid USD 1.50 per task, but their domain experience, assignments, agreement, revision ledger, and independence are not reported (paper “Ethical Considerations,” p. 9).

The released records preserve persona, instruction, preconditions, proposed environment setup, metrics, and a coarse validity flag. They do not preserve source URLs for occupational routines, author/reviewer identities, requirement-level evidence, disagreement, review decisions, expert approval, or the transformation from work observation to checkpoint. “Professional-grade” is therefore an authorial framing, not a validated claim.

### Difficulty and cross-application construct

The four levels are defined by bundled features:

- L1: one application;
- L2: two or three applications and a linear flow;
- L3: at least two applications or complex reasoning, often conditional logic or calculations;
- L4: an intentionally infeasible task (paper §3.2, p. 4; generator prompt, pp. 16–17).

The release exactly contains 39/80/50/12 L1/L2/L3/L4 records and app-count distribution 40/43/86/10/2 for one through five listed apps. These strata simultaneously change app count, task family, milestone count, nominal steps, generated content, conditionality, external dependencies, and likely evaluator evidence burden. L3 even admits two applications if “complex reasoning” is asserted. App labels are metadata, not evidence that information actually crossed boundaries or that switching caused failure.

The paper's step-matched comparison reports one L1/L2 subset with 10.92 versus 11.26 estimated minimum actions and sharply lower L2 scores (p. 9). It does not report subset size, selection algorithm, task IDs, model/observation condition, matching tolerance, uncertainty, or adjustment for task family, checkpoint content, artifact obligations, evaluator visibility, and external dependencies. Estimated minimum actions are also author/expert path properties, not observed equal treatment. The comparison weakens a pure length explanation but does not identify a causal cross-application effect.

### Checkpoint construction and score semantics

The paper defines

`S_int = mean_k J(trajectory, checkpoint_k)` and `S_final = J(trajectory, terminal criterion)`

with Qwen3-VL-Plus as a binary judge (paper §3.5, p. 6). It says generated checkpoints were refined from action constraints to semantic states and human-verified as “path-essential,” so shortcuts and alternative menu/keyboard routes remain admissible.

The release reveals a materially narrower implementation:

- `hf_run.py:420-521` sends the instruction, complete action list, every captured screenshot, milestone strings, and final criterion to one Qwen call;
- the prompt says actions are only supporting evidence and absent screenshot evidence should fail (`hf_run.py:458-489`);
- `hf_run.py:400-417` equally averages the returned milestone booleans and separately binarizes the final result;
- there is no dependency graph, necessity type, weight, severity, durable-state requirement, observer identity, checkpoint timestamp, terminal recheck, or collateral-state check;
- the judge receives screenshots after executed actions but not native document structure, filesystem state, email server state, spreadsheet formulas, saved-file hashes, browser history, or an explicit authoritative final snapshot.

The central phrase “intermediate-state checkpoint” is therefore misleading. The judge scans a **trajectory-wide evidence bundle** and asks whether a state appeared. The paper itself says false positives occur when an action appears successful before later occlusion and false negatives when a briefly achieved state becomes invisible after switching windows (Appendix C.1, p. 13). That is evidence of an observer/time-policy problem, not merely visual ambiguity.

A milestone such as “file is open” can pass even if the file is later corrupted or the wrong output is sent. Conversely, a professionally valid shortcut may never expose the exact screen named by a milestone. No terminal recheck tests whether earlier prerequisites still hold, and no masking rule prevents one upstream defect from producing several correlated failures. The 899 booleans are authored observations, not 899 independent capability units.

The static audit also found that at least 283/899 milestone strings contain coarse path/action cues such as opening, active-window state, using a named operation, visiting, copying, searching, or tab interaction. This is a conservative lexical count, not a semantic classification, but it directly contradicts any blanket claim that all released checks are action-independent consequences.

### Infeasible-task scoring is a terminal-action test

The most severe validity defect is executable and unambiguous. For every L4 task, `hf_run.py:424-456` ignores the task's success criterion and screenshots. It returns success if the action list is empty or its final action contains `FAIL`; otherwise it returns failure. It does not require the agent to inspect the resource, identify the correct obstacle, avoid harmful partial actions, explain the reason, preserve state, or perform a required communication.

The released L4 set is not homogeneous. Some criteria ask only for correct error reporting, but others require emailing a missing-file explanation, preserving absence of a download, or producing/sending an artifact if available. One L4 record (`win_soc_l4_001`) even contains five intermediate checks, all ignored by the L4 branch. Universal immediate `FAIL` earns full L4 credit, and an empty trajectory also passes. The paper's claim that L4 measures “self-awareness,” infeasibility recognition, or negative-constraint handling (pp. 6–7) is not licensed by this evaluator. UIPath's reported 50% L4 score is particularly uninterpretable because the paper itself notes that it often deems tasks incomplete.

### Environment, setup, and reset

The system builds on OSWorld and uses VMware Windows images, snapshots, PyAutoGUI or `computer_13`, screenshots, accessibility trees, and optional set-of-marks. The runner assigns nominal budgets of 15/25/40/20 steps by level (`hf_run.py:324-337`; paper Table 2, p. 7).

The environment implementation can revert to a named `init_state` snapshot and apply executable `config` setup operations when `env.reset(task_config=...)` receives a compatible task (`desktop_env/desktop_env.py:242-301`). The advertised WindowsWorld path does not do this:

- `benchmark.json` records use descriptive `environment_setup`, not the OSWorld `config` or `evaluator` fields;
- all 181 records lack both `config` and `evaluator`;
- `hf_run.py:294-310` calls `env.reset()` with no task record;
- for `evaluation_metrics`, `DesktopEnv` substitutes a no-op/infeasible metric because actual scoring happens in `hf_run.evaluate()` (`desktop_env/desktop_env.py:335-363`).

The VM may have been manually or globally pre-populated with merged assets, but the release does not provide an executable mapping from 130 declared files across 112 setup-bearing tasks into the reset snapshot, a snapshot hash, an inventory, per-task precondition checks, or task-specific cleanup. The repository contains no `.xlsx` or `.docx` task assets. README installation points to a mutable OneDrive VM image and says any VMware version is acceptable; it also warns newer versions do not support Chinese (`README.md:26-40,82-97`).

This blocks task-level setup provenance and clean-reset verification. It also makes the 21 records explicitly marked `validity_info.is_valid = false` consequential: they remain in `benchmark.json` and the runner applies no validity filter. The invalid set spans all levels (5 L1, 9 L2, 5 L3, 2 L4) and records missing files or inaccessible URLs. Reported denominators are not reconciled with these flags.

### Step budget and configured-system comparability

The nominal “step” is a prediction-loop iteration, but one model response can contain multiple actions. `hf_run.py:337-393` appends and executes every returned action before incrementing `step_index`. Thus a 40-step cap is not necessarily 40 atomic GUI actions. Agent-S3, UiPath, pure-model, and CoAct paths also differ in orchestration, grounding, internal budgets, and action semantics. CoAct has separate orchestrator/coding/CUA limits and a default cut-off of 200 (`hf_run.py:594-607`), while the paper groups rows by model/agent labels.

These are configured packages, not model-only comparisons. App-count and level effects can also be budget effects: higher levels receive larger caps, while failures may emit fewer or more batched actions. The release logs screenshot/action records and prediction seconds but not token usage, judge usage, provider retries, wall-clock environment operations, or paper-result manifests.

## Evidence and results

### Main configured-system results

Table 2 reports one aggregate per named model/agent and observation package. Gemini-3-Flash Hybrid has the highest reported average final score, 20.44%, and intermediate score, 50.32%. Final scores generally fall with level, while intermediate scores remain more dispersed when final outcomes approach floor (paper pp. 7–8).

This supports a descriptive claim: on these runs, the trajectory-wide judge marked many authored milestones even when it did not mark the terminal criterion. It does not show “latent competence” or causal progress. High intermediate/low final can arise from genuine partial work, transient states, checkpoint redundancy, repeated prerequisite credit, path cues, evaluator false positives, later reversal, or terminal observer insufficiency.

No trial repeats, random seeds, task-level results, missing-run table, confidence intervals, clustered uncertainty, judge-call failures, environment invalids, retries, or raw cost ledger are released. Some table percentages are inconsistent with the nominal level denominators—for example 41.94% cannot be an integer numerator over all 39 L1 tasks—yet neither paper nor release states cell-specific denominators. `show_result.py:68-151` silently skips tasks without parseable result files and chooses the latest result directory; its fallback parser can use the first two arbitrary numbers in a file (`show_result.py:10-32`). It macro-averages available task fractions by level and then all available tasks (`show_result.py:153-224`) without an invalid/missingness ledger. The reported matrix is therefore not denominator-auditable.

### Judge agreement

The paper selects 100 stratified L1–L3 tasks (24/50/26), covering 518 checkpoints. Two human annotators independently label trajectories; their “consensus” is compared with the VLM. Reported Pearson correlations are 0.9108 for intermediate task scores and 0.8316 for final scores; Cohen's kappa is 0.8668 at checkpoint level and 0.8271 for final judgments, with confidence intervals (paper §3.5, p. 6; Appendix C.1/Table 7, pp. 13, 19).

This is useful evidence that judge and consensus labels often agree on the selected evidence bundles. It does not validate checkpoint authority or process meaning. The paper omits trajectory/system sampling, class prevalence, human-human agreement, consensus/adjudication rule, annotator blinding, task/checkpoint clustering in intervals, criterion-family error, natural failure prevalence, model-judge repeatability, and consequential false-pass/false-fail loss. The same incomplete screenshot bundle constrains both humans and VLM, so agreement can reproduce observer insufficiency. The cited false-positive/negative cases confirm that attainment time and visibility policy affect labels.

### Error and persona analyses

The paper reports first-failure distributions over feasible L2–L3 screenshot-only trajectories and persona-level aggregate scores (Tables 4 and 8, pp. 8, 20). But checkpoint order is authored chronology, checkpoints are dependent, and the release does not preserve one monotone stage ledger. “First failed checkpoint” is not necessarily the earliest causal failure: later screenshots may establish a later state, an earlier state may be transient, and one missed upstream fact can mask descendants.

Persona comparisons inherit generated-task composition, app, artifact, level, criterion, and budget differences. No repeated system-task observations or hierarchical model separates these factors. Occupation labels therefore organize the suite; they do not estimate occupational strengths or weaknesses.

## Unique insight

WindowsWorld's distinctive lesson is that **path tolerance and process validity are separate properties**.

A checkpoint can avoid exact click imitation yet still fail as a process measure. A valid process observation needs at least:

```text
public requirement / authority
→ stage precondition
→ admissible evidence views
→ state transition or decision
→ durability / reversal policy
→ downstream dependency
→ terminal recheck or preserved consequence
→ separate collateral and safety observations
```

WindowsWorld implements free-path trajectory search for a state description, but omits most of the remainder. The resulting `S_int` is best described as **mean authored milestone attainment under one trajectory-wide VLM observer**. Calling it “progress” adds an unsupported value and causality interpretation.

The general repair is not click-by-click trajectory matching. It is a **typed checkpoint ledger**:

- checkpoint role: `prerequisite`, `diagnostic_exposure`, `decision`, `committed_mutation`, `independent_value`, `terminal_gate`, `safety_side_effect`;
- public basis and requirement authority;
- dependency/masking and alternative-route set;
- authoritative evidence view and observation time;
- attainment, durability, reversal, and terminal-recheck status;
- criterion weight/value basis and dependence group;
- invalid/insufficient-evidence/environment/grader outcomes;
- earliest supported cause versus visible failed consequence.

This machinery already exists across skill-bench's dependency-aware criteria, artifact-view admissibility, trace, execution-validity, task-health, validity-argument, and metric contracts. No WindowsWorld-specific subsystem is warranted.

## Comparison with adjacent reviewed benchmarks

- **OSWorld 2.0** uses much denser final-state checks, dynamic requirements, self-hosted services, explicit safety diagnostics, and release identities. Its checkpoints are still authored and weakly calibrated, but they more often inspect authoritative final state and separate safety. WindowsWorld is cheaper and more trajectory-visible; it does not repair durability, dependency, side-effect, or release-verification validity.
- **OfficeBench** grades typed final-state stores and more readily admits alternative action paths, but often uses weak existence/keyword predicates. WindowsWorld adds GUI execution and trajectory-wide partial observations while weakening authoritative artifact/state inspection. Together they show that neither app count nor path tolerance is sufficient; state-delta and evidence-view coverage are required.
- **Workflow-GYM** uses expert witness paths and native professional applications but withholds its full task/check release. WindowsWorld is more inspectable at the task-string level, yet its process checks are less professionally grounded and its setup/result chain is not executable from the task records. Both demonstrate that one authored path or milestone set is not a validity argument.
- **WorkArena++** composes executable setup/oracle/validator components and exposes a dependency-order problem. WindowsWorld exposes milestone strings but no dependency graph or native state validators. WorkArena++ risks history-dependent polling; WindowsWorld risks trajectory-wide transient credit. Both need terminal invariant rechecks and criterion-level outcomes.
- **AutomationBench** has synthetic rather than native apps, but task-local serialized state, fresh initialization, deterministic assertions, and initial-state guards make its observer/reset chain substantially more auditable. WindowsWorld has a more realistic GUI surface but weaker transition, setup, state-delta, and result provenance.
- **HealthAdminBench** preserves 1,698 released criterion definitions and observed-work motivation, yet mixes path/stage/outcome checks without dependencies. WindowsWorld has the same flat-checklist problem with much weaker occupational lineage and artifact authority, plus the L4 terminal-`FAIL` shortcut.

The comparative conclusion is not that final-state grading always dominates process grading. It is that **process evidence should be added only where it identifies a consequential stage, and its temporal/dependency semantics must survive into the result record**.

## Limitations and validity threats

### Content and professional validity

1. Persona-conditioned generation is not occupational sampling or expertise elicitation.
2. No task-frequency, consequence, role-authority, stakeholder, or artifact-acceptance frame supports “professional-grade.”
3. Four postgraduate reviewers' expertise, assignments, agreement, and revision lineage are unreported.
4. The released task records lack source-to-requirement-to-checkpoint provenance.
5. Human rejection of ambiguity may preferentially remove legitimate judgment, exception, and multiple-solution work.
6. App count, level, task family, horizon, criterion count, artifacts, external dependencies, and budgets are confounded.
7. The step-matched comparison is under-specified and does not isolate switching.

### Measurement validity

8. Equal checkpoint fractions conflate prerequisites, transient views, reversible states, useful outcomes, and terminal gates.
9. No dependency, masking, severity, necessity, sufficiency, or weight-value model exists.
10. At least 283 released milestone strings retain coarse path/action cues.
11. Whole-trajectory evidence permits transient attainment credit without terminal durability.
12. Screenshots/actions are insufficient observers for many document, spreadsheet, email, filesystem, and web-content claims.
13. No collateral-state, authorization, safety, integrity, recipient, or artifact-usability checks are systematic.
14. L4 scoring accepts an empty trajectory or final `FAIL` regardless of reason or state.
15. L4 criteria are heterogeneous and sometimes require consequences that the evaluator ignores.
16. Human/VLM agreement can reproduce a shared inadequate evidence view.
17. Judge calibration omits natural prevalence, class-conditional errors, task/checkpoint clustering, repeatability, and decision loss.
18. First-failure indices over dependent authored checkpoints are not causal roots.

### Experimental and statistical validity

19. Reported results appear single-shot; exact-task stochastic reliability is unknown.
20. No raw task-level matrix, trial traces, judge outputs, costs, invalids, retries, or denominator ledger is released.
21. Table percentages are not always compatible with nominal task counts, and missingness is unexplained.
22. The summarizer silently skips absent/unparseable results and chooses the latest run.
23. Prediction-loop steps can contain multiple atomic actions; caps are not common action budgets.
24. Model, harness, grounding model, observation, action schema, orchestration, context, and budget differ across rows.
25. No paired/task-clustered uncertainty supports model, modality, level, persona, or app-count comparisons.
26. Persona analyses confound occupation label with generated task composition.
27. Language comparison changes instruction language against a primarily single-language interface and reports no matched translation audit or uncertainty.

### Reproducibility and operational validity

28. The audited official release postdates arXiv v1 and contains no paper-run result evidence.
29. Twenty-one task records are explicitly invalid yet remain runnable and unfiltered.
30. Eleven L4 records omit `intermediate_checks`; one other L4 record's five checks are ignored.
31. No task has executable `config` or `evaluator` fields; the advertised runner resets without passing task setup.
32. Descriptive setup requests 130 files, but no task asset files or executable generation/setup mapping are released.
33. VM image, snapshot, installed-app, locale, credential, network, and task-overlay identities are not pinned in a release manifest.
34. README allows varying VMware versions and uses a mutable OneDrive image.
35. Live URLs and email behavior add time, network, account, and service variance without health/invalid-run policy.
36. Snapshot restoration is implemented but no reset-differential or residual-state conformance report is published.
37. Qwen judge endpoint/model behavior is mutable and judge calls have no retry/invalid-output evidence contract.
38. No safety, privacy, authorization, rollback, or production-consequence study licenses autonomous use.

## Reproducibility and operational realism

**Task-string inspectability: high.** The complete 181-record benchmark, prompts, runner, environment base, agent adapters, and scoring code are public and pinned for this audit. The static audit exactly reproduces the paper's level, app-count, and 4.97-checkpoint headline counts.

**Instrument conformance: low.** Released task setup is descriptive rather than executable in the advertised runner; invalid records are included; L4 semantics collapse to a terminal action; authoritative state observers and terminal rechecks are absent; and result aggregation lacks fail-closed missingness.

**Paper-result reproducibility: low.** There is no manuscript commit, exact VM/snapshot identity, retained result matrix, trajectories, judge outputs, provider ledger, or per-cell denominator. Historical proprietary model endpoints and the mutable Qwen judge further block exact replay.

**Operational realism: bounded.** Real Windows applications, GUI focus, clipboard transfers, document formats, and cross-application state create meaningful execution friction. Synthetic generated tasks/files, live-service fragility, absent organizational permissions and recipients, weak state authority, and no professional acceptance make this a cross-application GUI stress instrument—not a production workflow trial.

## Transfer to skill-bench

### Retain

1. Cross-representation workflows where evidence must move among applications or stores.
2. Sparse milestone observations as diagnostics when terminal success is near floor.
3. State descriptions rather than exact click sequences where the state is truly consequential.
4. Separate intermediate vectors and strict terminal outcomes; never hide the vector behind one score.
5. Explicit infeasible/abstention cases, but only with reason and state consequences checked.
6. Human comparison of model-judge outputs, with stronger sampling and error analysis.
7. Fixed, declared configured-system budgets and complete trace capture.

### Repair

1. Type every checkpoint by role, dependency, authority, evidence view, durability, and terminal-recheck policy.
2. Treat trajectory occurrence, durable stage completion, and terminal consequence as separate observations.
3. Preserve alternative routes without accepting arbitrary transient or action-like cues.
4. Replace universal `FAIL` scoring with a reason-specific refusal/abstention contract: exposure, evidence inspected, calibrated reason, permitted partial action, prohibited side effects, required escalation/communication, and final state.
5. Bind task setup to executable, hashed overlays and prove preconditions/reset with canaries before admitting a trial.
6. Filter or separately operate invalid tasks; report eligible, attempted, valid, scored, missing, retried, and excluded denominators.
7. Use authoritative artifact/state observers where screenshots cannot establish a claim; use `insufficient_evidence` rather than forced false.
8. Recheck prerequisites and preserved invariants at termination and prevent masked descendants from being counted as independent failures.
9. Equalize or record atomic actions, tool calls, wall time, tokens, judge calls, and environment operations; a prediction turn is not a universal step.
10. Require repeated exact-task trials and family/task-clustered uncertainty before ranking or difficulty claims.
11. Preserve occupation/persona labels only as unvalidated authoring metadata until observed-work and expert/recipient evidence supports stronger claims.
12. Fail closed on release identities, environment health, task setup, judge parse/call status, and result completeness.

## Concrete repository actions

1. **No duplicate build task.** WindowsWorld's needed fields already have homes in the benchmark-bundle dependency-aware criteria, artifact-view admissibility, execution-validity, task-health, metric-monitoring, validity-argument, expertise-transfer, and trace/root-cause records.
2. **Retain two future conformance cases in existing validation work:** (a) a transient checkpoint that is later reversed or invalidated, requiring terminal recheck and no durable credit; and (b) an infeasible task where immediate generic `FAIL` is wrong because correct completion requires evidence inspection, a specific reason, preserved state, and a bounded escalation or communication.
3. **Reporting rule:** call a flat VLM average over trajectory-visible milestones “milestone attainment under observer X,” not “process progress,” unless dependency, durability, value, and observer sufficiency have been validated.
4. **Comparative synthesis:** place WindowsWorld between OfficeBench and OSWorld 2.0 as a release-inspectable cross-application/trajectory-observer case with high task-string coverage but low occupational, setup, state-authority, reliability, and claim validity.

## Claim ceiling

The immutable paper and audited post-v1 release establish that WindowsWorld packages 181 generated Windows GUI tasks, 141 with at least two listed applications, and uses one Qwen3-VL-Plus trajectory observer to average 899 authored milestone judgments and separately judge terminal criteria, except that L4 is scored by empty/final-`FAIL` action. Reported configured systems often receive more milestone than terminal credit. These sources do not establish representative professional work, process fidelity, causal cross-application coordination difficulty, durable progress, reliable model rankings, safe refusal, clean environment execution, paper-result reproducibility, occupational capability, economic value, production reliability, or deployment readiness.