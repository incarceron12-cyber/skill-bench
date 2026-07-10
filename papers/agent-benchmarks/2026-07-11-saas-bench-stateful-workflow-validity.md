# SaaS-Bench: weighted final-state checks are not automatically partial-progress evidence

## One-sentence contribution

SaaS-Bench contributes the strongest locally inspected public package yet for cross-application browser workflows—106 explicit tasks, 23 deployable open-source SaaS images, per-run reset, traces, and 1,304 released weighted checks—but its checkpoints mix seeded preconditions, overlapping downstream consequences, weak proxies, and model judgments, so the reported 23–44% checkpoint scores cannot be interpreted straightforwardly as run-attributable professional progress or as evidence that planning and state tracking caused the failures.

## Why this matters

This review advances charter objectives A, B, and C through targeted expansion into a stateful execution instrument. SaaS-Bench directly tests cross-application coordination, persistent backend state, long horizons, multimodal inputs, artifact creation, and recovery. Those properties are relevant to the second `skill-bench` stateful pilot, but the source is a methodological case—not a recommendation to make the benchmark about SaaS or GUI control.

The central transfer is a sharper validity boundary:

> A checkpoint is an evidence claim about one view of state. It becomes partial-progress evidence only if the state was not already satisfied, is attributable to this run, has declared necessity and sufficiency, and is not double-counting the same upstream event through dependent consequences.

SaaS-Bench has unusually rich checks, but does not establish those conditions consistently.

## Research question

The paper asks whether current computer-using agents can leverage realistic SaaS applications to complete long, professional, cross-application workflows, and which failures—planning, state tracking, cross-application context, grounding, or recovery—limit them (paper pp. 1–3, 8–17).

The directly supported question is narrower: under one `browser-use` execution treatment, what fraction of task-authored weighted final-state propositions and all-propositions completion events do 14 named model configurations satisfy on 106 highly specified tasks? Neither application realism nor low completion by itself identifies a latent professional capability or a causal failure mechanism.

## Sources and reading record

**Immutable paper read in full**

- Record: https://arxiv.org/abs/2605.15777v2
- PDF: https://arxiv.org/pdf/2605.15777v2
- Local PDF: `data/papers/pdfs/2605.15777v2-saas-bench-can-computer-use-agents-leverage-real-w.pdf` (24 pages; SHA-256 `99ec0f81715a715fb4709c1810e1537ba5cad294c9a1878bd63531abdfc9a8ed`)
- Local text: `data/papers/text/2605.15777v2-saas-bench-can-computer-use-agents-leverage-real-w.txt` (SHA-256 `42efd1975cdcf8b6db4d43a575f4b4da295fe30ca5c26499fa258f4d702423c3`)
- Date read: 2026-07-11 (local date).

**Official release inspected completely**

- Repository: https://github.com/UniPat-AI/SaaS-Bench
- Pinned commit: `14f0acd0ee871bde7c8e0a2342a2c6ff0535daa2` (tree `0df5c6a69f304f02477930727d103928e35ac17f`, 2026-06-05).
- Local archive: `data/sources/releases/2605.15777v2-saas-bench/UniPat-AI-SaaS-Bench-14f0acd.zip` (358 files; SHA-256 `e884213d8fa917443e3bd51879558da0752a0e5d8660d43c5d62e8e1dbbc1f6f`).
- Provenance: `data/sources/releases/2605.15777v2-saas-bench/provenance.json`.
- Two-task static lineage audit: `data/sources/releases/2605.15777v2-saas-bench/task-trace-summary.json`.
- Docker-image manifest: `data/sources/releases/2605.15777v2-saas-bench/docker-image-manifest.json`, pinning 23 LFS objects at Hugging Face revision `c1a5a27d3a6278e91ea052f2066763af00730a07` (57,730,179,569 bytes / 53.77 GiB).

The code commit is 12 days after arXiv v2. The latest inspected pre-v2 commit, `e982325` (2026-05-19), already has all 106 task triplets; the later commit changes three Agriculture verifiers and one task description, including fail-soft skipped checks. Post-v2 behavior is therefore reported as release evidence, not projected backward into manuscript results.

The 53.77 GiB images were not downloaded and the paper recommends more than 500 GB RAM for parallel execution. No benchmark replay or score replication is claimed. Image hashes are preserved, but inspected materials expose neither application source revisions/build recipes nor a paper result inventory.

## Methodology and system

### Environments and state reset

The authors select 23 open-source applications with authentication, persistent databases, frontend/backend logic, and business constraints, then group them into six domains. They populate schemas using synthetic LLM-generated data or public datasets. Before each trial, Docker applications are restored to a predefined initial state; versions, configuration, seed data, and startup scripts are said to be locked (paper pp. 4–5).

This is materially stronger than a static website. The released app registry and 23 revision-pinned image objects make the package deployable. Yet “real SaaS” and “real professional work” remain distinct claims: the applications are real code, while business context and tasks are authored or synthetic. The paper does not publish application versions, image build provenance, reset hashes, initial-state inventories, state-absence canaries, or post-reset equivalence evidence. The image package supplies opaque tar objects rather than rebuildable projections from upstream source.

The current runner allocates fresh per-slot containers and removes containers/volumes after a task. That is a useful reset mechanism, not a complete equivalence proof. Four compose stacks pull auxiliary images, the code-server image may install packages from the network, and browser search is available. Those mutable dependencies and network paths are not represented in the paper's configured-system record.

### Task and expert pipeline

The paper reports 106 tasks: 74 text-only and 32 multimodal; 99 tasks use at least two applications; application counts are 7/26/53/20 for one/two/three/four apps. Long-horizon status is inferred from Claude Opus 4.6 trajectories: 72/74 text tasks and 19/32 multimodal tasks exceed 100 operations (paper pp. 5–6).

Task creation proceeds from occupational role and workflow seed through Claude Opus 4.6 Builder, human Challenger, and senior Refiner loops, static review, and manual execution against `verify.py`. The appendix says 45% of candidates survive, often after two or three rounds. Static criteria include professionalism, cross-app naturalness, dependency depth, verifiability, narrative coherence, complexity quality, multimodal feasibility, and anti-patterns such as parallel tasking and specification overflow (paper pp. 5–6, 21–23).

This is a valuable authoring pipeline. Its evidence limits are substantial:

- no candidate count, domain flow, rejection table, reviewer count, credentials, role matching, training, compensation, independence, disagreement, or reliability is reported;
- expert review of a co-authored task is not independent professional validation;
- all 106 released descriptions contain exact numbered steps and credentials, frequently exact field values and wording, despite `spec_overflow` being an anti-pattern;
- selection for programmatic verifiability and high operation count can exclude ambiguous, judgment-heavy, collaborative, or stochastic professional outcomes.

The release therefore supports a suite of professionally themed procedural workflows more strongly than broad “professional realism.”

### Execution treatment

All agents use `browser-use`, rendered DOM plus viewport screenshot, a shared prompt, and browser/file actions; direct verifier/database/backend access is prohibited. The paper says timeout, failure cap, step budget, and logging are shared, but does not report their exact values, harness/model revisions, decoding, dates, retry policy, or cost (paper pp. 7–8).

The post-v2 runner defaults to 400 steps, five agent failures, 150-second LLM calls, five model-call retries, and a 600-second client timeout. It creates a fresh Chrome profile and task work directory and records URL, title, model self-evaluation/memory/goal, actions, tool results, and request IDs. This is strong operational evidence, but it is later than v2.

The release also shows treatment details hidden by model-only leaderboard labels. Its long system prompt prescribes app ordering, exact copying, default values for omitted requirements, retry/skip policy, and UI-specific workarounds. It says JavaScript is disabled while instructing agents to open the browser console and call Frappe's `cur_frm.set_value` client API. Thus the evaluated system is not merely model + generic browser: it includes extensive benchmark-specific procedural guidance and an internally inconsistent interface policy.

### Checkpoints and aggregation

Each task defines weighted final-state checks. The paper distinguishes DB/API/file/state checks, regex/document checks, and text/vision LLM judges. A task's Resolved Score is one only when every checkpoint passes; Checkpoint Score is its passed-weight fraction (paper pp. 7–8, 23–24).

A static audit of the pinned release found:

- 106 task triplets and 1,304 unique declared `check(...)` calls;
- 2,192 total declared weight units: 477 weight-1, 766 weight-2, and 61 weight-3 checks;
- 101 verifiers directly use Docker/database access;
- 25 verifiers hard-code an unversioned `gemini-3.0-flash-preview` judge through a mutable external endpoint;
- no released paper trajectories, per-check judgments, aggregate result table, or human execution records.

The per-task macro-average in the current reporting code avoids weighting an entire task merely because it has more checks. Within a task, however, weights remain uncalibrated, dependent checks are additive, seeded preconditions can receive credit, and the package lacks `not_applicable`/`insufficient_evidence` semantics. The post-v2 fail-soft Agriculture change even emits `[SKIP]`, which the generic parser does not recognize as a check while a supplied `SCORE` line changes the denominator. This illustrates why task/grader version identity and missingness semantics matter.

## Evidence and results

### Main performance

The paper reports overall checkpoint scores from 15.8% to 43.9% for 14 named systems; the highest resolved rate is 3.8%. Four models receive three-attempt best-score analysis, with pass@3 improving average best checkpoint score by about 7.5 percentage points overall (paper pp. 7–9).

These numbers demonstrate that the selected configured systems frequently fail released-style checks under a demanding browser treatment. They do not establish a professional-work completion rate:

- there is no human condition or validated professional threshold;
- model labels omit harness prompt/adapter/version identity;
- tasks, checks, apps, domains, and authors are clustered, but no confidence intervals or hierarchical analysis is reported;
- most main-table systems appear to have one run while only four have three; missing/invalid/provider runs are not disclosed;
- the current reporter can represent missing verifier records as zero/SKIP, but the paper does not state whether infrastructure errors enter denominators;
- no raw result inventory permits audit of rankings, domain means, or resolved counts.

### Complexity and checkpoint decay

Scores decline with Opus-estimated operation length, number of checks, application count up to three, and early-to-late checkpoint position. The paper interprets this as long-horizon structural difficulty and says the score gap is driven by complexity rather than random variation (paper pp. 9–11).

That causal language is too strong. App count, path length, checkpoint count, domain, modality, author, artifact type, grader type, and task specificity are positively correlated by design. Operation length is an outcome from one model, not an independent task property. “Early/middle/late” checkpoint order is author-defined and can correlate with app, weight, prerequisite depth, or check type. A ±1 SEM ribbon over correlated authored tasks does not separate these factors.

### Failure analysis

The paper reports failed-check categories dominated by missing entities and trajectory labels such as repeated action, search/scroll thrashing, premature exit, grounding failure, and persistent self-correction. Detailed `bof_023`, `bof_032`, and `bof_155` cases expose undetected corrections, entity-type cascades, overconfident summaries, and run-level path divergence (paper pp. 9–16).

The cases are incisive qualitative evidence. But no coding frame, trajectory sample, coder count, blindness, duplicate coding, agreement, adjudication, or mapping from symptoms to earliest causes is disclosed. “Entity missing” is a verifier observation, not uniquely planning failure: it may arise from navigation, UI grounding, tool semantics, budget, environment failure, wrong entity linkage, or checker mismatch. Likewise, an uncorrected date supports a failure-to-reverify interpretation for that trace, not a suite-level causal rate.

The paper's “Fragility Principle” assumes independent checkpoint pass probability `p`, then applies `p^N`. SaaS checkpoints are visibly dependent; the paper's own entity-cascade case demonstrates this. The formula is a pedagogical counterfactual, not an empirical model of resolved probability.

## Two released task traces

The full static traces and hashes are in `task-trace-summary.json`. They audit requirements, seeded state, and verifier logic; they are not agent executions.

### Trace A: `business_023` expense reimbursement

The public task prescribes nine stages across HRMS, BigCapital, and Twenty: approve a seeded three-line claim, inspect an unpaid-claim report, create a vendor/items/bill, pay it, inspect A/P aging, and create a completed CRM task. Its verifier exposes 11 direct-database checks worth 20 points. This is the released counterpart of the paper's `bof_023` case.

The verifier's native-state access is a major strength, but its semantics show why weight is not progress:

1. the seeded HRMS line items earn two points although the agent did not create them;
2. the vendor check retrieves email but passes on row existence without comparing the required email;
3. bill lookup falls back to any bill of amount 10,350, and bill-ID lookup does likewise, weakening vendor/date linkage;
4. payment is not joined to the target bill/vendor and the reported account name is not required to equal `Bank Account`;
5. unpaid-claim and A/P report *viewing* are unobserved—the checks establish selected state, not that the agent performed those verification stages;
6. bill existence, line items, payment, and paid balance are causally dependent but scored as additive evidence.

A score can therefore include pre-existing correctness, duplicated consequences, and false-positive surfaces. The verifier is diagnostically useful, but its scalar is not a calibrated fraction of work completed.

### Trace B: `healthcare_001` diabetes program

The public task requires a conditional OpnForm questionnaire, two new OpenEMR encounters with vitals/care plans/SOAP notes, and an OnlyOffice workbook with specified headers, two populated rows, and two charts. Its verifier has 12 database checks worth 21 points.

Coverage is sharply uneven:

1. an encounter check passes if a patient has **any** encounter, without a pre-run count or linkage to the latest forms;
2. form checks accept broad type counts but omit labels, required flags, date prefill, scale range, symptom identities, and robust adherence-to-barrier logic;
3. the conditional check can pass when serialized logic contains either `5` or show/hide—not necessarily adherence `< 5`;
4. clinical text checks require only short substrings from much longer prescribed content;
5. the entire workbook deliverable earns one point for a matching file title; cells, patient data, two charts, native structure, and rendered quality are not inspected.

Thus a resolved pass would still not prove the advertised spreadsheet/chart artifact or one coherent new encounter per patient. This is not a minor omission: it means the public construct and private evidence projection diverge in one of the benchmark's core “professional” tasks.

## Unique insight

SaaS-Bench reveals that **checkpoint design needs causal semantics, not just weights**. For a state proposition `C`, a benchmark must separately record:

1. **precondition status** — was `C` already true before the trial?
2. **delta attribution** — did this trial create or preserve the relevant change?
3. **requirement basis** — which public requirement licenses `C`?
4. **necessity/sufficiency** — is `C` required, merely supportive, or only one admissible witness?
5. **dependency parent** — does `C` repeat evidence from an upstream event?
6. **evidence view** — DB row, API response, native artifact, rendered view, trace, or model judgment?
7. **failure semantics** — substantive fail, invalid environment, inaccessible view, not applicable, or grader error?
8. **consequence class** — benign utility, professional correctness, safety gate, integrity, efficiency, or diagnosis?

Only run-attributable, construct-relevant deltas should enter a “progress” estimand. Seeded facts should be readiness canaries or zero-weight context checks. Descendant consequences can remain diagnostic but need dependency-aware aggregation so one upstream defect does not masquerade as many independent failures. Process checks should be required only when the process/stage is itself the construct or final state cannot identify it.

This goes beyond Workflow-GYM's final-state warning and Workspace-Bench's graph warning. Workflow-GYM shows that outcomes can miss stages; Workspace-Bench shows that authored dependency graphs are hypotheses; SaaS-Bench shows that even rich backend checkpoints can distort partial progress unless pre-state, delta, dependency, and evidence admissibility are explicit.

## Limitations and validity threats

### Professional and content validity

- Six thematic domains and selected apps are not an occupational, economic, or work-frequency frame.
- Reviewer authority, role matching, counts, assignment, independence, reliability, costs, and disagreements are absent.
- LLM-generated seed data and exact step-by-step tasks may test procedural compliance more than messy professional judgment.
- Selection favors long, executable, objectively verifiable workflows; consequential but subjective, collaborative, or uncertain work may be excluded.
- A manual expert pass is a solvability witness, not evidence that one path is canonical, the task is representative, or checks cover professional quality.
- Healthcare task content includes clinical prescriptions, but the paper provides no safety/compliance review or evidence that medical content and consequences were validated by appropriately qualified practitioners.

### Task, checkpoint, and artifact validity

- Seeded preconditions can receive score, conflating environment readiness with agent progress.
- Checkpoint weights 1–3 have no documented elicitation, severity model, calibration, or decision meaning.
- Dependency and overlap make weighted criteria non-independent; additive score can multiply one cause.
- Verifiers may use broad fallback queries, substring matches, existence checks, or title-only artifact proxies.
- Alternative valid paths are not represented explicitly; exact-value tasks can reward one authored projection.
- Native structured state is strong evidence for many consequences but cannot establish unobserved report inspection, reasoning, or artifact presentation.
- Twenty-five released verifiers use an unversioned external model judge without prompt-version provenance, repeated judgment, calibration, abstention, or uncertainty.
- The paper reports no verifier false-positive/negative study, negative contrast set, accepted alternatives, or adjudication log.

### Experimental and statistical validity

- Main results lack task-clustered uncertainty and raw per-run records.
- Four models' three runs are insufficient for stable task-level variance estimates, and other systems appear single-run.
- Pass@k/best score measures an opportunity policy, not ordinary single-attempt reliability; retry cost is omitted.
- Complexity analyses are observational and heavily confounded.
- Error categories lack a reproducible annotation protocol and mix root causes with surface symptoms.
- The `p^N` argument assumes independence contradicted by the observed DAG cascades.
- No tokens, monetary cost, wall time, infrastructure cost, retry volume, or human-review burden is reported.

### Reproducibility and operational realism

The release is substantial: all task triplets, harness, app registry, reset orchestration, verifier parser, reporting code, licenses, and revision-pinned image objects are available. Exact paper reproduction is nevertheless not established:

- the inspected code is post-v2 and contains behavior-changing verifier fixes;
- the release has no manuscript result inventory, trajectories, verifier outputs, human traces, or reviewer records;
- Python dependencies such as `browser-use` are unpinned;
- model APIs and the hard-coded judge name/endpoints are mutable;
- app image tarballs are pinned, but upstream source/build recipes and internal version mapping are absent;
- compose auxiliary images and in-container installs can use live network resources;
- no environment-state root, initial-state manifest, reset canary report, invalid-run manifest, or cross-run equivalence evidence is released;
- a post-v2 `[SKIP]` convention and supplied denominator can bypass the generic parser's per-check inventory;
- current setup requires roughly 54 GiB of images, 100 GB disk, and recommends >500 GB RAM, limiting independent reproduction.

Operational realism is also bounded: authentication is simplified, tasks supply credentials and exact steps, agent actions occur in mock organizations, and direct business consequences, collaboration, approvals, privacy, and stakeholder review are largely absent. This is appropriate for safe evaluation but should constrain deployment-readiness claims.

## Comparison with existing skill-bench evidence

### Workflow-GYM

Both sources expose long GUI workflows and final-state grading. Workflow-GYM's dataset was unavailable and its showcase revealed residual state; SaaS-Bench releases all 106 task/check definitions and pinned app images, making checker audit far stronger. Yet SaaS-Bench similarly lacks state-delta canaries and stage-transition evidence. Its exact steps and backend checks reduce ambiguity but increase benchmark-specific procedural disclosure.

### Workspace-Bench

Workspace-Bench's file graphs distinguish availability, relevance, observed use, and causal use. SaaS-Bench's application DAGs are mostly narrative: checker dependencies and shared entity keys are not machine-typed. Its `bof_032` case is direct evidence that one upstream entity error can trigger many descendant failures. The same alternative-path and dependency semantics required for workspace graphs should govern SaaS checkpoints.

### Current taxonomy and second pilot

The existing task-projection manifest, persistent-workspace records, artifact-view admissibility, task-health lifecycle, metric specification, validity arguments, and evidence-chain audit already have homes for every necessary obligation. The `vendor-incident-response` pilot already separates initial inventory, source authority, safe mutation, artifact state, invalid environment, and evidence-chain claims. SaaS-Bench adds a nonduplicate requirement on **checkpoint attribution/dependence**, not a need for a SaaS schema.

## Benchmark relevance

SaaS-Bench is directly relevant to the general hypothesis behind `skill-bench`'s second pilot: useful knowledge-work evaluation needs a configured, persistent environment in which requirements propagate across tools and leave inspectable artifacts and consequential state. Its reusable machinery is the per-trial reset, compact bring-your-own-agent contract, native-state verifier access, multi-view trace, and application/task separation—not its particular SaaS stack or occupational labels.

The release also supplies a concrete stress test for the project's existing contracts. It shows why an evidence chain must bind each check to initial state and run delta; why artifact-view admissibility cannot be replaced by a filename; why task health must include reset and checker conformance; why metric specifications need dependency and missingness semantics; and why a configured-system ID must include prompt, harness, workaround, judge, app, and verifier versions. These obligations generalize to file workspaces, research environments, spreadsheets, clinical administration, engineering systems, and other stateful knowledge work.

## Transferable benchmark-design lessons

1. **Separate readiness checks from progress checks.** Seeded facts and app health belong to environment validity; they should not increase agent score.
2. **Record state deltas.** Bind each final proposition to pre-state, post-state, run ID, and reset evidence.
3. **Type checkpoint dependencies.** Preserve prerequisite, shared-cause, descendant, redundant, gate, and independent relations; report root event and surface failures separately.
4. **Calibrate necessity and sufficiency.** A title or row-existence check may be evidence, but must not stand in for an entire artifact or professional requirement.
5. **Join records across applications.** Cross-app tasks require stable entity/link keys; broad amount/name fallbacks should fail conformance tests.
6. **Use plural checkpoint outcomes.** Distinguish substantive fail, invalid environment, grader error, insufficient evidence, and not applicable; never silently alter denominators.
7. **Validate weak proxies adversarially.** Plant wrong-email, unrelated-same-amount, pre-existing-record, title-only-empty-artifact, missing-chart, and shared-cause cascade cases.
8. **Keep diagnosis outside the score unless validated.** Missing entity is an observation; root-cause labels require trace/state evidence and adjudication.
9. **Version all treatment components.** Model, prompt, harness, workaround policy, browser-use revision, app images, auxiliary images, judge, verifier, task, and feedback policy need separate identities.
10. **Bound claims.** Difficulty for configured browser agents on explicit mock workflows is not equivalent to professional capability, occupational representativeness, safety, or readiness.

## Concrete repository actions

1. **Refine existing cross-record audits; do not add a schema task.** Require every scored checkpoint in future pilots to declare precondition status, run-attributable delta, necessity/sufficiency, dependency parent or independence rationale, evidence view, and invalid/insufficient semantics. This is a consolidation requirement for the existing bundle/evidence-chain machinery.
2. **Apply adversarial checkpoint tests to the second pilot before interpreting a live run.** Add or confirm planted cases for a pre-satisfied requirement, an unrelated record sharing the expected scalar, an artifact with correct title but missing structure, and one upstream defect producing several failed descendant checks. The scalar should not count environment readiness or multiply one cause.
3. **Do not import SaaS-Bench leaderboard values as professional-work facts** until an immutable result inventory exposes task/run validity, configured-system versions, checker outcomes, judge versions, costs, clustered uncertainty, and adjudications.

No new queue task is added. Actions 1–2 fit the already pending `build-vendor-incident-isolated-agent-trial` and the existing evidence-chain/task-health/metric machinery; a separate checkpoint subsystem would duplicate implemented contracts.
