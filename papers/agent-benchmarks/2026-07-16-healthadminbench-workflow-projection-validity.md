# HealthAdminBench: fine-grained workflow checks expose reliability failure but do not validate occupational automation

**Source type:** Deep review of the complete immutable arXiv v1 paper and a pinned official post-v1 release

**Paper:** Suhana Bedi et al., *HealthAdminBench: Evaluating Computer-Use Agents on Healthcare Administration Tasks* (arXiv:2604.09937v1, 10 April 2026)

**Immutable record:** https://arxiv.org/abs/2604.09937v1

**Local PDF:** `data/papers/pdfs/2604.09937v1-healthadminbench.pdf` (24 pages; SHA-256 `c6a368240c731a4eae8803acdbeac9cb20f49e05c0288f5e5c41c08e80d0dcd8`)

**Local text:** `data/papers/text/2604.09937v1-healthadminbench.txt` (94,135 characters; SHA-256 `f47895671d6226ab4f82d7fa3f6b9518c53cfbc79f8911a1a0e57e229a9dc97b`)

**Official repository:** https://github.com/som-shahlab/health-admin-bench

**Pinned archive:** `data/sources/releases/2604.09937v1-healthadminbench/som-shahlab-health-admin-bench-e71a8f4.zip` (SHA-256 `d7b14776fc13f7cc5ef43c1c7989deeb0de05b9c51d00ee5b81fc1017cf6b8db`)

**Release provenance:** `data/sources/releases/2604.09937v1-healthadminbench/provenance.json`

**Date read and audited:** 2026-07-16

> **Timing boundary.** The audited official commit `e71a8f4d6923037805b7f51fbbf608d12ea56cf5` was authored on 12 June 2026, 63 days after immutable arXiv v1. It is release evidence, not proof of manuscript-time byte identity. It contains no tracked raw paper-result table, `benchmark_results.json`, `benchmark_report.txt`, or result trajectories; `scripts/results.png` is not an auditable result ledger.

## One-sentence contribution

HealthAdminBench converts observed healthcare-administration work into 135 synthetic cross-portal GUI tasks and 1,698 state/text checks, making long-horizon workflow breakage unusually inspectable, but its partially audited expert projection, path-heavy scoring, conjunction arithmetic, single-shot trials, mutable hosted environment, and absent raw results support only configured-system performance on this instrument—not clinical or administrative safety, occupational capability, reliability, economic value, production fitness, or deployment readiness.

## Why this matters

The paper is unusually close to skill-bench's central expertise-to-evaluation chain:

`professional observation → expert-edited task → synthetic multi-system state → action path and artifact mutations → subtask observations → end-to-end claim`.

Its strongest evidence is not that healthcare work has been automated. It is that high average criterion completion can coexist with low all-criteria completion, especially when information, documents, and identifiers must survive cross-system handoffs. That is a reusable stress case for consequential knowledge work in any domain.

The source also reveals where this chain remains unauditable. More than 100 hours of shadowing and practicing administrators are reported, yet the released tasks contain no source observation, contributor, authority, disagreement, or transformation lineage. Fine-grained checks mix required outcomes with benchmark-prescribed clicks. The resulting score is diagnostically richer than final-answer accuracy but cannot by itself show that the instrument preserved professional requirements or that each failed check is an independent capability failure.

This advances charter objectives A and B through expansion and evidence-backed consolidation. Healthcare administration is a bounded high-stakes methodological case, not a scope commitment.

## Research question and claim boundary

The paper asks how well frontier computer-use agents execute end-to-end healthcare-administration workflows across an EHR, two payer portals, and a fax system, and whether domain guidance, structured observations, and domain-specific fine-tuning improve performance (paper §§1, 3–5, pp. 1–10).

The defensible empirical question is narrower: for seven model–harness configurations, what fraction of 135 author-defined task conjunctions and 1,698 released criteria pass in one reported trajectory per condition under task-dependent step budgets, synthetic local browser state, screenshot or accessibility-tree observations, portal guidance, and a mixture of deterministic and GPT-5.4 grading?

The study does **not** estimate real administrator performance, error cost, throughput, recovery burden, policy compliance, patient or revenue outcomes, human oversight needs, deployment reliability, or labor substitution. The benchmark's all-subtask task score is an instrument-defined strict endpoint, not a production reliability rate.

## Methodology and system

### Workflow selection and expert projection

The authors construct three revenue-cycle task families: 60 prior-authorization tasks, 60 appeals/denials tasks, and 15 durable-medical-equipment tasks. They report more than 100 hours observing real administrative work, use MedHELM's “Administration and Workflow” category to guide selection, and design all 135 tasks with practicing healthcare administrators (paper §3.1, p. 4; §3.4, pp. 5–6).

A formal audit covers only 40 tasks: 20 prior-authorization and 20 appeals/denials items stratified across difficulty. Two revenue-cycle experts independently judge goal realism, practice fidelity, and success criteria. Their feedback changes terminology, plan types, constraints, routing rules, and eligibility checks; patterns are then propagated to related unaudited tasks. DME receives iterative testing but no formal expert audit (paper §3.4, p. 6).

This is valuable evidence that expert review found material projection defects. It is not a complete content-validity study:

- the paper reports neither task-level reviewer assignments nor ratings, agreement, disagreements, adjudication, acceptance thresholds, or before/after records;
- “decades of combined experience” does not identify role, setting, payer, task-specific authority, or independence;
- systematic propagation from 40 reviewed items to 95 others is an analyst transformation without a reported re-review;
- DME's standardized-workflow rationale does not substitute for expert review;
- no sampling frame ties the 135 tasks to frequency, consequence, regional/payer heterogeneity, or the observed-work corpus;
- the release has no task-level provenance, expert, contributor, source, or transformation fields (audited across all 135 v2 and v3 task JSON records).

The projection therefore supports “expert-involved synthetic cases,” not representative hospital work or professionally validated coverage.

### Environment and state authority

Four Next.js interfaces emulate an EHR, two payer portals, and fax. Synthetic patient records and a fixed benchmark date (25 February 2026) make temporal decisions repeatable. The authors intentionally remove MFA, CAPTCHAs, session timeouts, and deployment-specific access constraints (paper §§3.1–3.3, pp. 4–5; Appendix A.5, p. 20).

The pinned release makes the execution surface inspectable. `harness/environment.py:123-154` creates a fresh browser context and navigates to the task start; `:259-265` says there is no server-side initialization; portal state lives in `localStorage`. Final evaluation reads `portals_state` and constructs aliases such as `aetna_state`, `anthem_state`, `signals`, and `full_state` (`:828-971`). Cleanup removes only `portals_state` (`:973-993`). Downloads are written to the shared OS temporary directory under their suggested filename (`:744-775`) and are not deleted by `clear_state`.

This yields stronger per-browser state isolation than a shared mutable backend, but not a complete reset or isolation proof. Authentication keys such as `healthportal_session` and `healthportal_user` are separate local-storage entries in the portal code and are not cleared by the harness. Download names can collide across attempts or concurrent runs. The browser has no declared network-denial boundary. The default runner targets the mutable hosted `https://emrportal.vercel.app`; local execution is possible, but the README uses `npm install`, and the paper/release do not provide a paper-time image digest or hosted-deployment identity. A new browser context mitigates some residue; no pre/post canary proves exact initial state, clean temp files, portal-build identity, or fault-free reset.

The synthetic state is authoritative for **benchmark mutations**. It is not evidence that the replicas faithfully implement payer policy, proprietary portal behavior, permissions, exception handling, or real organizational side effects.

### Task, subtask, and dependency design

Every task JSON exposes a public goal, difficulty, challenge type, start configuration, expected metadata, a detailed hidden `step_by_step` witness, and binary evaluators. The audited release matches the paper's headline inventory in both `benchmark/v2` and `benchmark/v3`: 135 tasks, 1,698 criteria, 1,177 JMESPath checks, and 521 LLM-judge checks. It also exactly matches the six paper category totals: 419 information retrieval, 515 documentation, 292 form completion, 200 resolution, 149 document handling, and 123 clinical reasoning.

The task records are highly inspectable. For example, `benchmark/v3/tasks/prior_auth/emr-hard-1.json` exposes a 25-step witness and 23 checks spanning clinical-note reading, tab visits, document download/upload, payer submission, calculated dosage, note content, and referral clearing. That is much richer than a terminal screenshot.

However, the task schema does not represent dependency semantics. Across all 1,698 checks, the audit found no `depends_on`, `dependencies`, or `prerequisite` field. `harness/evaluation.py:165-284` runs every check independently, sums equal points, and defines task pass as 100%. A later release script retrospectively classifies 473 checks as process and 1,225 as outcome using hard-coded query regexes (`scripts/recompute_accuracy_without_process_checks.py:75-230`). That useful repair is not part of the paper's stated method, and the raw input it expects—`wandb_export_v2_trajs_with_usage.csv`—is absent from the pinned tree.

The released records therefore mix at least three meanings:

1. **path observance**, such as clicking Diagnoses, Services, or Coverages tabs;
2. **intermediate consequential state**, such as downloading a required document;
3. **final outcome**, such as a submitted authorization and cleared referral.

A single upstream omission can fail many descendant checks. Conversely, a correct final submission can fail a prescribed-click check even if the information came from another admissible view. The hidden witness proves one route; it does not prove each click is construct-essential or that alternative professional routes are invalid.

The Pydantic task schema also omits the released eval `category` field (`harness/config/task_schema.py:30-99`), so ordinary model parsing silently discards it. Diagnosis scripts recover categories from raw JSON, but the core `EvaluationResult` does not preserve them (`harness/evaluation.py:239-254`). This weakens the claimed built-in capability diagnosis unless downstream analysis rejoins results to the exact task version by position.

### Grading

Deterministic checks query browser state and require exact or containment matches (`harness/evaluators/jmespath_evaluator.py`). This is strong where the serialized state is authoritative and the predicate is sufficient. It is weaker for interaction flags such as `signals.clicked_diagnoses_tab`, which show an event but not what the agent learned, and for broad fields where successful mutation does not establish policy legitimacy or collateral-state preservation.

The 521 free-text checks use GPT-5.4, with three runs and majority vote by default in the audited release (`harness/config/task_schema.py:68-95`; `harness/evaluators/llm_judge.py:42-95`). The prompt usefully instructs the judge to use only the submitted field and quote evidence (`llm_judge.py:104-148`). Invalid judge output is coerced to zero rather than typed separately (`:150-188`).

Paper Appendix B validates 60 LLM-judged submissions selected from one Claude Opus 4.6 accessibility-tree/general-guidance condition: 30 judge-pass and 30 judge-fail. Four humans provide two labels per item. Human–human agreement is reported as 93.3%; 112/120 individual human labels agree with the judge (93.3%) (paper p. 21).

This balanced, outcome-stratified sample cannot estimate judge accuracy at the benchmark's natural prevalence. It tests one agent and one condition; it reports agreement rather than sensitivity, specificity, class-conditional error, or criterion-family heterogeneity. Four conflicted items are not adjudicated, and no rater expertise, rubric training, agreement statistic correcting chance, repeated judge stability, or error-cost analysis is given. Agreement supports a bounded consistency claim, not the paper's broad conclusion that the rubrics are reliable or GPT-5.4 is adequate for all 521 criteria.

### Experimental design and operating policy

Seven configured systems come from five models: standardized harness agents plus native Claude Opus 4.6 and GPT-5.4 computer-use systems. Primary results use screenshots and portal guidance; native CUAs use vendor loops rather than the shared action/prompt loop (paper §4, pp. 7–9). The comparison therefore correctly reveals orchestration effects but cannot isolate model capability. Observation modality also changes action grounding and budget: the audited settings double screenshot-only step limits (`harness/config/settings.py:103-147`).

The paper reports single-shot trajectories and acknowledges limited recovery (p. 10). The release runner defaults to one run, while its module docstring advertises five; stochastic seeds do not pin external model behavior. Runtime exceptions are excluded by default (`FailurePolicy.EXCLUDE`), while retry and zero-score are optional (`harness/reproducibility.py:41-45, 80-105, 229-351`). The paper does not identify which policy, attrition, provider failures, retries, or environment faults produced the reported tables. Excluding failed runs can inflate capability estimates if failures are treatment-related.

## Evidence and results

The best task success is 36.3% for Claude Opus 4.6 CUA; GPT-5.4 CUA has the highest subtask success at 82.8% and 26.7% task success. DME is easiest for both CUAs; appeals/denials is hardest. Information retrieval is strongest, while reasoning and task resolution are weaker. Portal guidance and accessibility-tree observations improve both metrics (paper Figures 3–4 and 7, pp. 7–10, 22).

These results are credible evidence that the selected configured systems often leave at least one released obligation unsatisfied and that execution package and observation design materially affect measured performance. They do not identify occupational reliability.

Most importantly, the subtask/task gap is not itself evidence of error compounding. Task success is an all-check conjunction over 3–27 criteria (release audit; mean 12.58). Under an intentionally unrealistic independent, homogeneous 82.8% check-pass model, expected all-check success at the mean length is about 9.3%, below GPT-5.4 CUA's observed 26.7%. For Claude Opus CUA, 78.4% implies about 4.7% versus 36.3% observed. The difference shows that criterion difficulty, task length, within-task dependence, and system/task heterogeneity dominate simple multiplication. To identify propagation, the benchmark would need prerequisite edges, earliest failed transition, descendant masking, repeated trials, and counterfactual repair—not merely two aggregate rates.

The manual failure analysis names hidden dependencies, file-operation avoidance, and long-horizon information loss (paper §4.5, p. 9). These are plausible and align with the task structure, but the paper reports no sample, codebook, rater count, agreement, frequencies despite saying the three modes account for a majority, or causal intervention. They are mechanism hypotheses.

The fine-tuning study randomly holds out 35 tasks, trains Qwen-3.5-27B once on 100 step-by-step trajectories, and reports 40.0% task success versus 17.1% base and 25.7% Claude Opus 4.6. The task-success contrast to Claude is not statistically significant; only the subtask contrast is (Appendix E, pp. 23–24). One small random split, one epoch, no split-family/near-duplicate analysis, no repeated training seed, and co-designed task-specific demonstrations support a benchmark adaptation result—not general domain expertise transfer or real-enterprise improvement.

## Unique insight

HealthAdminBench's durable insight is that **fine-grained workflow evaluation needs a dependency-aware consequence graph, not a flat checklist or a terminal-only score**.

A useful task model is:

`requirement authority → stage precondition → admissible evidence acquisition → state/document handoff → committed mutation → downstream affordance → final consequence`.

HealthAdminBench observes many nodes but not the edges. This matters because the same failed check can mean different things:

- a required fact was never available;
- the agent did not inspect it;
- it inspected but did not retain it;
- it retained but transformed it incorrectly;
- the destination mutation failed;
- the mutation succeeded but documentation or verification failed;
- one upstream defect masked all descendants;
- the checker required one witness path despite an equivalent outcome.

Flat all-check scoring is defensible as a strict task endpoint only after each check's necessity, authority, public basis, dependency, and evidence sufficiency are validated. Fine-grained scores should remain diagnostic observations; they should not be interpreted as independent capability units or averaged into a reliability claim without a declared estimand.

A second insight is that **expert involvement must survive projection as data**. The paper's expert review materially changed terminology, constraints, and routing rules—the exact kind of tacit requirement skill-bench seeks. Yet none of those changes are traceable from source observation to task atom to environment affordance to checker. “Expert-designed” is therefore metadata at paper level, not auditable authority at requirement level.

## Comparison with adjacent reviewed benchmarks

- **Workflow-GYM** spans 338 longer procedures in 56 native applications and has broader professional/software coverage, but its task/check release was unavailable and final-state grading was largely unauditable. HealthAdminBench is far more inspectable and adds dense cross-system checks. It repairs release transparency, not occupational sampling, task-level expert lineage, transition dependencies, or clean-state proof. Both show that a reference procedure is only a solvability witness.
- **WorkArena/WorkArena++** use a real ServiceNow substrate with reusable setup, oracle, validator, and teardown components. WorkArena++ makes sequential composition and prerequisites more explicit than HealthAdminBench's flat criteria, but remains concentrated in one platform and weakly work-sampled. HealthAdminBench adds observed domain workflows and heterogeneous simulated organizations; it trades native enterprise fidelity for cross-portal control and synthetic state authority.
- **OfficeBench** makes cross-store office mutations inspectable but uses brainstormed synthetic tasks and many narrow existence/keyword checks. HealthAdminBench improves observed-work grounding, requirement density, document transfer, explicit commit actions, and text-rubric inspection. It still inherits OfficeBench's central issue: selected state predicates do not prove collateral safety, policy authority, artifact usability, or professional acceptance.

The correct progression is not “generic GUI benchmark → healthcare-ready automation.” It is `atomic state checks → cross-system consequential transitions → dependency-aware diagnosis → externally validated professional and operational claims`.

## Limitations and validity threats

### Content and ecological validity

- No task-frequency, consequence, payer, institution, geography, or occupational sampling frame.
- Only 40/135 tasks receive formal expert audit; DME receives none; propagated corrections are not re-audited.
- No task-level source, contributor, authority, disagreement, transformation, consent, or approval lineage is released.
- Synthetic policies and interfaces are asserted consistent with reality but not compared against production behavior or outcomes.
- Clinical-reasoning checks inside administrative tasks raise additional authority and safety questions not validated by administrator involvement alone.

### Measurement validity

- The all-check conjunction mixes path, stage, and outcome requirements without dependency edges or severity weights.
- Equal binary points treat a tab visit, correct identifier, supporting-document transfer, policy decision, and final submission as exchangeable at the subtask level.
- Process flags can reward canonical navigation without proving cognition; final mutations can miss invalid provenance and collateral effects.
- The released schema drops criterion categories from parsed evaluator records, requiring fragile positional rejoining for category analysis.
- LLM-judge validation is small, balanced on judge outcome, single-system, and reports agreement rather than natural-prevalence error or consequential loss.
- No typed `invalid_run`, `insufficient_evidence`, `grader_error`, or `environment_fault` outcome is preserved in paper metrics.

### Experimental and statistical validity

- Native CUA versus standardized-harness rows confound model, prompt loop, tool semantics, action batching, stopping, memory, and provider behavior.
- Screenshot and accessibility treatments differ in both observability and allowed steps.
- One trajectory per task/condition gives no exact-item reliability estimate.
- Bootstrap intervals over tasks do not address shared templates, checks, task families, authors, or environment components.
- Pairwise significance in 33/42 comparisons has no reported multiplicity correction.
- Aggregate subtask/task gaps do not identify propagation; criterion count and dependence are unmodeled.
- The fine-tuning claim rests on one 35-item split and no training/split replication; its task-success superiority is not significant.

### Safety, privacy, and operational validity

- Synthetic data avoids direct patient-data exposure in the benchmark but does not evaluate HIPAA/security controls, minimum-necessary access, auditability, human approval, identity, permissions, or data retention.
- Removed MFA, CAPTCHA, timeout, policy drift, and access constraints exclude important production failure surfaces.
- No wrong-recipient, duplicate submission, irreversible side effect, rollback, escalation, or severe-error loss analysis licenses “safe automation.”
- No human baseline, time-on-task, correction cost, exception distribution, oversight burden, or downstream acceptance supports economic or labor claims.

## Reproducibility and operational realism

**Inspectability: high for the post-v1 task and harness snapshot.** All 135 v2 and 135 v3 task files, portals, evaluator code, prompts, SFT split, tests, runner, and Apache-2.0 license are present. Static audit reproduces the paper's task/check/category counts. V2 and v3 have the same task paths, goals, evals, and metadata; 75 website records differ, while the other 60 task JSON objects are identical.

**Exact paper-result reproducibility: low.** The audited commit postdates v1 by 63 days. No raw paper trajectories, per-task outcomes, judge outputs, attrition/retry ledger, paper command manifest, model snapshot ledger, or tracked result table is present. Hosted interfaces and provider APIs are mutable. The README's current model list extends beyond the paper, and the release cannot establish which code or portal build generated Figures 3–7.

**Operational realism: bounded.** Cross-portal navigation, forms, documents, commits, long horizons, and realistic failure logic are valuable. Browser-local synthetic state, shared temp downloads, omitted authentication/session friction, clean fixed policies, no human handoff, and no organizational consequence mean the instrument is a controlled workflow simulator, not a production trial.

## Transferable benchmark lessons

1. **Preserve observed-work lineage.** Every requirement atom should link to observation/interview evidence, contributor authority and scope, edits, disagreements, task projection, environment affordance, and checker.
2. **Represent sparse dependency graphs.** Mark precondition, postcondition, descendant checks, masking, alternative routes, and whether a stage is construct-essential or merely diagnostic.
3. **Separate process from consequence before scoring.** Do not discover this distinction post hoc through regexes. Keep path evidence, intermediate state, final outcome, collateral effects, safety gates, and artifact quality as typed observations.
4. **Treat conjunction as an endpoint, not an explanation.** Report strict completion alongside dependency-adjusted diagnostic profiles; do not call the aggregate subtask/task difference error propagation without transition evidence.
5. **Bind categories through the result contract.** Criterion ID, category, authority, severity, dependency, grader version, evidence view, and outcome status must survive parsing and trial capture.
6. **Fail closed on run validity.** Preserve provider, parser, judge, environment, timeout, retry, reset, and missing-evidence failures separately from substantive agent failures.
7. **Canary all state surfaces.** Check browser state, authentication/session keys, downloads, output roots, hosted/local build identity, and cleanup before admitting capability evidence.
8. **Calibrate judges on natural and consequential strata.** Report class prevalence, sensitivity/specificity, criterion family, agent diversity, disagreement/adjudication, and expected loss—not only balanced agreement.
9. **Cross expertise interventions independently.** Portal guidance and task demonstrations should be versioned separately from task/check authorship and evaluated against independent rubrics to distinguish localization, canonical-path imitation, and transferable procedure.
10. **Bound high-stakes claims.** Synthetic success can support instrument completion and local failure diagnosis. Safety, occupational reliability, production readiness, and economic value require human baselines, severe-error analysis, organizational outcomes, oversight, and prospective operation.

These requirements already have executable homes in skill-bench's expertise-transfer, participation-lineage, task-projection, benchmark-bundle, artifact-view, task-health, metric-monitoring, execution-validity, and validity-argument records.

## Concrete repository actions

1. **No duplicate build task.** The missing task-level authority/projection lineage is covered by the completed expertise-transfer and task-projection contracts; dependency-aware criterion semantics are already canonical and implemented in the benchmark bundle. HealthAdminBench should become external validation evidence for exercising those fields in the next cross-domain workflow pilot.
2. **Retain two planted conformance cases.** Add, when an existing pilot is next extended, (a) one upstream document-acquisition defect with masked descendant checks and (b) one alternative valid route that reaches the same authoritative state without a prescribed tab click. Require root/surface separation and no double-counted descendants.
3. **Require a workflow run-validity canary.** Existing execution-isolation machinery should verify clean browser/session state, clean download/output roots, pinned environment build, fault/retry status, and exact criterion/result joins before a workflow score enters a validity argument.
4. **Do not import the paper's safety, reliability, automation, or economic language into canonical claims.** Record HealthAdminBench as strong post-v1 release inspectability and useful configured-system evidence with the professional and operational ceilings above.

No new queue item is added because the implications refine completed, nonduplicate machinery rather than identify a missing subsystem.
