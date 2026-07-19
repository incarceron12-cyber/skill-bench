# Alipay-PIBench measures a benchmark-aligned payment package, not yet payment expertise or production safety

## Source, release, and review status

**Deep review of the complete immutable primary source and timing-aware official release.** I read the full 17-page arXiv v1 paper, checked the layout-preserving extraction against the PDF, and audited all 18 released task packages, their instructions, Skills, rubric definitions, evaluator entry points, runtime/scoring code, and release-level tests. I also ran the release's own top-level tests in their intended import configuration.

- **Paper:** Shiyu Ying et al., *Alipay-PIBench: A Realistic Payment Integration Benchmark for Coding Agents*, arXiv:2607.14573v1 (16 July 2026), <https://arxiv.org/abs/2607.14573v1>.
- **Local PDF:** `data/papers/pdfs/2607.14573v1-pibench.pdf` (17 pages; SHA-256 `0a14b114e4c6dc28b0d6e37c911e1594d835efb3ddde58c1cd282afb9a82872c`).
- **Full text read:** `data/papers/text/2607.14573v1-pibench.txt` (SHA-256 `23fcdd5574b02378095fe219b6d32bd811103eec4188b6505294349a55e5e743`).
- **Official arXiv source:** `data/papers/source/2607.14573v1-source.tar` (SHA-256 `aab4ebf1b3b94125d654e9c9cdad7bb198e8da47b50474309936fd7df72a675b`).
- **Timing-appropriate official release:** inclusionAI/PIBench commit `e2782ad0d2b0559170401680e6d06be1ee1eac17`, <https://github.com/inclusionAI/PIBench/commit/e2782ad0d2b0559170401680e6d06be1ee1eac17>.
- **Local release:** `data/sources/releases/2607.14573v1-pibench/repository/PIBench-e2782ad0d2b0559170401680e6d06be1ee1eac17`; archive and acquisition hashes are in `data/sources/releases/2607.14573v1-pibench/provenance.json`; compact counts are in `inventory.json`.

ArXiv v1 appeared at 05:08 UTC and the repository's initial commit at 10:30 UTC on the same day. The next commit, `17c8c42e77f27a64548b07d1693979ac51c66fb2`, changes only the English and Chinese README paper links. This establishes a relevant official release, not byte identity with the instrument or runtime that produced the paper tables. No paper-run result rows, trajectories, run manifests, or table-building scripts are released.

## Relevance, charter fit, and decision filter

This review advances charter objectives A, B, and C by examining a high-consequence case where repository editing, domain guidance, executable behavior, business-state consistency, security obligations, and semantic judging meet. The general uncertainty is: **what does a matched guidance-package contrast establish when the intervention, task requirements, and evaluators share the same product-document lineage?** Payment is a bounded mechanism case, not a proposal to narrow `skill-bench` to fintech.

The concrete evidence is an inspectable chain from nine source projects and Alipay documentation through 18 task packages, one 101-file guidance corpus duplicated into every task, 459 released rubric definitions, evaluator programs, a privileged Docker runner, and manuscript aggregate tables. Useful completion is a claim boundary and reusable retain/repair/test guidance. Existing configured-system, procedural-package, artifact-view, action-authority, validity, task-health, metric, trace, and release-custody machinery can represent the requirements; a payment-specific schema or pilot would duplicate rather than compound.

## One-sentence contribution

Alipay-PIBench's real contribution is to split repository-level payment integration into functional-loop and risk-hardening scenarios and observe the same modified repository through structural, executable, and semantic checks; however, its six-model Skill contrast compares a huge benchmark-aligned official guidance package against its absence without released repeats, uncertainty, raw outcomes, judge calibration, treatment-adoption evidence, or independent payment validation, so it supports manuscript-reported configured-package efficacy on 18 authored tasks—not payment expertise, transaction safety, professional correctness, production fitness, or readiness.

## Research question and intended construct

The paper asks three questions: how well six models complete Alipay integration tasks, how access to `alipay-payment-integration` changes Rubric Pass Rate (RPR), and what static, unit, integration, end-to-end, and LLM-assisted methods reveal (paper §4, p. 9). The intended construct includes product selection, server-side credentials/signing, frontend/backend coordination, trusted outcome confirmation, payment-to-business-state consistency, idempotency, abnormal-state handling, refunds, and fund-safety controls (abstract and §1, pp. 1–3).

These are meaningful obligations, but the study observes several narrower objects that must remain separate:

1. **repository conformance:** expected code/configuration/interface patterns are present;
2. **fixture or sandbox execution:** a selected path responds under one environment and test setup;
3. **authored state-transition conformance:** tested local states change as the evaluator expects;
4. **semantic-judge agreement:** one model observer accepts a diff/evidence packet against authored criteria;
5. **configured Skill-package effect:** RPR changes when a fixed package is installed;
6. **source-faithful product integration:** implementation matches authoritative, version-valid platform semantics;
7. **professional correctness and safety:** acceptable alternatives, threat boundaries, failure recovery, reconciliation, and operational controls are adequate;
8. **production fitness/readiness:** real credentials, services, users, counterparties, operations, compliance, monitoring, rollback, and repeated reliability are validated.

PIBench directly measures the first five to varying degrees. The paper sometimes names the latter three as capabilities or safety, but no evaluator inherits those claims merely because its rubric uses payment terminology.

## Methodology and evidence

### Task construction

The suite crosses nine named Alipay products/projects with Basic and Advanced scenarios (paper §3.1, pp. 4–5). Basic starts before target-product integration and asks for the core payment loop. Advanced starts from a separately prepared integration and asks for hardening against invalid/duplicate notifications, non-idempotent updates, abnormal states, and unsafe refunds (§3.2, pp. 5–7). The two scenarios are progressive conceptually but are **not longitudinal states produced by one agent**; each has its own authored repository snapshot, instruction, rubrics, and evaluator.

The product range and stacks are useful: Node/Express/MySQL, Next/TypeScript/Node, PHP/Apache/MySQL, Laravel/PHP/SQLite, Node/TypeScript/MongoDB, Java/Spring/MySQL, Node/Express/SQLite, and Next/TypeScript/Postgres. Yet “realistic” means adapted business-style repositories, not sampled production integration incidents. The paper cites project repositories or sites and says product requirements are grounded in Alipay Open Platform documentation, but gives no exact upstream commits, acquisition dates per file, licenses/permissions per adapted fixture, task-author qualifications, source-span-to-obligation map, expert-review protocol, disagreement record, or independent practitioner acceptance study.

All 18 release packages are present. A static audit found 459 rubric definitions. Release totals match almost all paper Table 1 rows, but the two BillExpress Advanced counts are interchanged relative to the manuscript: the paper reports 40 Order-QR and 41 QR items, while the release contains 41 and 40 respectively. The total remains unchanged, so aggregate agreement cannot identify whether this is a table-label error or release drift.

The target product is explicit in each task name, metadata, instruction, and often fixed endpoint/API requirements. Thus the benchmark tests implementation of a disclosed product more than open-ended product selection. Several instructions also expose evaluator-facing interfaces and expected state semantics, which is fair public basis but reduces the inference that agents independently recovered hidden domain structure.

### Rubric-derived evaluators

The paper says scenario rubrics are the common source for deterministic and LLM-assisted evaluators (§3.2–3.3, pp. 6–8). Static checks inspect SDK/OpenAPI use, secret placement, hooks, state/refund models, and suspicious bypasses. Integration/E2E checks exercise startup, gateway/fixture interaction, endpoints, state transitions, duplicate requests, invalid signatures, wrong amounts, exceptional states, and refund boundaries. Some tasks use live Alipay sandbox support; others use deterministic mocks or fixtures. LLM review covers product fit, signing/confirmation placement, state-machine coherence, and cross-component linkage.

This plural observer stack is the paper's strongest design feature. Its own method diagnostics show why: under with-Skill, Basic Static averages 92.79% while Integration and E2E average 73.16% and 78.24%; Advanced E2E averages 97.03% while LLM assessment averages 61.05% (§4.4, pp. 13–15). The authors correctly warn that method subsets differ, so these are not strictness or accuracy comparisons.

Release inspection narrows the claim further:

- Every task directory has `static.py`, `integration.py`, and `e2e.py` entry points, but no standalone deterministic `unit.py`; native project tests may be called inside other phases. “Unit” is therefore not an inspectable uniform release phase.
- Only six task directories contain `evaluation/llm_assisted/review_prompt.md`, although LLM execution logic exists in more task-local forms. Semantic observer implementation and evidence packaging are heterogeneous.
- Rubric IDs are not globally unique: 459 definitions contain 325 distinct ID strings. Task identity must therefore be part of every criterion key.
- Criterion `dimension` is inconsistent: some tasks use functionality/security/correctness/frontend, others `quality`, and 98 BillExpress definitions omit it. The scorer silently defaults missing dimensions to `quality`.
- The released scorer computes a weighted mean over per-rubric `weight`; it does not reconstruct paper method groups from an explicit typed method field. Most task files encode family-level weight sums through repeated item weights, but the mapping is implicit in IDs and scripts. In the released JSAPI Basic task, five static items and three Mini Program/client items each have weight `.125`, jointly summing to one, while 13 integration items sum to two and five judge items sum to one. That does not transparently reproduce the paper's declared `static=1`, `integration=2`, `e2e=2`, `llm=1` method formula (§3.3.2, p. 9). A paper row cannot be rebuilt from release criteria without a versioned method-assignment and table builder.
- Missing, invalid, or out-of-range criterion results fail closed in the runtime, which is good. But evaluator error is scored as zero in RPR, mixing agent failure with measurement/service invalidity even though metadata records some infrastructure flags.

The evaluators are extensive but co-authored observers. Static pattern checks can detect expected forms but not semantic completeness; mocks establish behavior against the mock; sandbox calls establish selected transport against one sandbox state; one canonical path does not prove alternative-path completeness; and an LLM reading a bounded diff/evidence view cannot prove runtime behavior or judge its own omitted evidence.

### Skill intervention

The nominal contrast holds model, Claude Code 2.1.200 harness, task, repository, environment, and evaluator fixed, while installing or withholding the official `alipay-payment-integration` Skill (§3.2 and §4.1, pp. 7, 9). This is much cleaner than changing prompt and grader together.

But the treatment is not a concise neutral procedure. Release audit found the same `SKILL.md` hash in all 18 tasks and 1,818 copied reference-file instances representing 101 unique files, each duplicated into every task. It includes payment-product routing, mandatory workflow, sandbox creation, SDK reminders, online-document fetching, five-language examples, security red lines, and product-specific code examples. It changes information, token availability, routing, interaction policy, tool use, and potentially network retrieval—not just “expertise.”

More importantly, the Skill's mandatory protocol conflicts with the benchmark interaction. `SKILL.md` requires a full plan, service disclaimer, explicit user agreement, and a hard stop at `<BLOCKING_CONFIRMATION>` before integration. Every released task has only one user turn. Six task prompts explicitly say this is an automated benchmark and instruct the agent not to stop for confirmation; others simply request direct completion. Thus the with-Skill arm contains an unresolved instruction conflict between safe interactive procedure and benchmark completion. The study does not report whether agents opened the Skill, which clauses they consumed, whether they ignored the confirmation gate, or how such conflict affected outcomes. A higher score could reward selective noncompliance with the Skill's own asserted safety policy.

The package also shares criterion content with the tasks and evaluators: server-side signing, no client private key, trusted confirmation, idempotency, exact product APIs, and state transitions recur across Skill, instructions, and checks. Literal answers need not leak for criterion-aligned coaching to occur. Shared evaluators across arms prevent grader drift, but not **intervention–instrument coupling**. The estimand is efficacy of an official, evaluator-aligned guidance corpus on its corresponding authored product tasks.

### Configured systems, repetition, and aggregation

The six manuscript model variants all run through Claude Code 2.1.200, so results are configured model–harness endpoints rather than model-only ability (§4.1, p. 9). Every trial starts in a fresh Docker container, which addresses cross-trial file/cache/service carryover. The release runner, however, launches containers with `--privileged`, grants passwordless sudo, may start nested Docker, and leaves network enabled unless a named network is supplied. This is process separation, not a least-privilege security sandbox. It is especially important because the agent can receive real sandbox keys through a read-only mount and, for many tasks, a copied file inside writable `/workspace`; traces and diffs are explicitly treated as sensitive in the README.

The paper defines a trial index and says repeated task trials are first averaged (§3.3.2, p. 9), but never reports the target or realized repeat count, seeds, ordering, invalid rows, retries, missingness, service failures, or uncertainty intervals. “Paired” means matched task/configuration, not common random numbers or paired stochastic attempts. Manual trace inspection is cited to explain four negative cells, but those traces and the coding protocol are unavailable.

RPR gives each available method its declared relative weight and macro-averages task means. This is a defensible inventory score, but it combines heterogeneous criterion authority and observer validity. Method availability changes the denominator by task; product/scenario averages therefore compare differently composed instruments. There is no sensitivity analysis for weights, gating critical safety criteria, or treating infrastructure/judge invalidity as missing rather than substantive failure.

### Results

The manuscript reports with-Skill overall mean RPR from 68.58% to 91.37%, and a mean with-minus-without contrast of +10.31 percentage points across 108 model×product×scenario cells, positive in 101, negative in four, and effectively unchanged in three (§4.2–4.3, pp. 10–13). Basic gains average +11.27 and Advanced +9.35. The largest displayed gains occur in low-baseline cells, while output tokens per unit RPR improve in 11 of 12 model×scenario averages.

These are substantial descriptive effects, but no confidence interval, task-clustered bootstrap, randomization inference, repeat variance, family-level uncertainty, multiplicity treatment, or raw row ledger is available. The low-baseline association is partly mechanical because bounded scores have more headroom and is analyzed post hoc without a matched counterfactual. Output/RPR is a ratio with unstable interpretation near low RPR and excludes input tokens, Skill-reading tokens, tool calls, wall time, sandbox calls, generation failures, judge cost, and operational labor. It is correctly not called end-to-end cost, but the RQ2 summary's “more efficiently” and “for developers” goes beyond the measured output-token ratio.

## Unique insight: consequential integration needs a typed proof ladder, not more rubric items

PIBench reveals a general benchmark-design fact: high-consequence integration is not one endpoint. The necessary evidence ladder is:

```text
authoritative requirement and valid-time scope
→ fair task obligation
→ repository structure
→ dependency/build/startup
→ request/response transport
→ authenticated counterparty result
→ authorized local state transition
→ idempotent/recoverable business consequence
→ reconciliation, monitoring, and collateral-state evidence
→ repeated operational reliability
→ professional acceptance and readiness
```

A criterion at one rung cannot stand in for a later rung. Source text does not prove a fair/current obligation; expected code does not prove execution; mock execution does not prove external transport; transport does not prove authenticated payment success; one success does not prove business-state consistency; local consistency does not prove fund safety; safety predicates do not prove monitoring or recovery; and benchmark success does not prove production readiness.

The Basic/Advanced split is useful because it exposes this ladder, but it should not become a compensatory scale. In consequential workflows, critical predicates such as secret confinement, signature verification, amount/app/seller binding, idempotent terminal transitions, and refund authority should have explicit applicability and gate semantics. A high mean cannot compensate for a failed critical boundary. At the same time, a checker must admit legitimate alternative implementations and distinguish `not_applicable`, `insufficient_evidence`, `invalid_environment`, and substantive failure.

The Skill result adds a second ladder:

```text
package available → surfaced → opened → relevant clause consumed
→ clause adopted at a decision opportunity → code/state effect
→ independently verified consequence → held-out transfer
```

PIBench observes availability and endpoint RPR, but releases no mediation evidence. Without the middle, the +10.31 points cannot distinguish information supply, benchmark-cue exposure, routing, code-example copying, forced deliberation, selective Skill violation, or genuine procedural adoption.

## Comparison with adjacent reviewed evidence

- **SkillsBench** is broader and reports repeated configured-system trials, invocation rates, costs, and negative task effects, but selects a Skill-responsive inventory and co-designs task/Skill/verifier. PIBench is narrower and more consequential, yet has the same package-efficacy-versus-transfer boundary with weaker uncertainty and no raw rows.
- **SkillGenBench** treats corpus-to-procedure generation as the intervention and exposes source/package/executor parity problems. PIBench uses an official package, but does not establish clause provenance, valid-time authority, adoption, or independently authored transfer.
- **Harness-Bench** requires outer-envelope and adapter evidence before interpreting model/harness differences. PIBench fixes one harness but its released `--privileged`, sudo, nested-Docker, network-enabled container is not a strong isolation boundary.
- **API-Bank and ToolBench**, as synthesized in `docs/concepts/web-tool-computer-benchmark-evolution.md`, move from call selection toward API interaction but do not by themselves validate durable business consequences. PIBench usefully adds repository and local state, but its mocks/sandbox paths still stop short of production transaction and reconciliation evidence.
- **SWE-bench/HumanEval/LiveCodeBench evolution** shows why executable equivalence is stronger than text matching but remains bounded by issue/task provenance and test coverage. PIBench's domain checks add consequence-specific predicates; they do not remove verifier incompleteness.
- **Executable-science and artifact reviews** such as LQCDMaster, FORMA, Imaging-101, SciVisAgentBench, and Anchor separate pipeline execution, native artifact/state, observer views, and source correctness. PIBench needs the same representation/admissibility and projection-drift discipline for code, logs, gateway traces, and database state.
- **Context-to-Execution Integrity and UnderSpecBench** separate request, authority, exact effect, and complete mediation. PIBench mostly assumes task-author authority and tests intended integration; it does not validate real merchant/user authorization, affected-party consent, compliance, or irreversible-effect governance.

## Limitations and validity threats

### Construct, sampling, and source authority

1. **Nine purposively selected product/project pairs are not a work distribution.** Product diversity is useful coverage, not representativeness of integrations, organizations, incident rates, or developer demand.
2. **Target products are disclosed.** Product-selection language overstates what fixed product metadata and endpoint requirements test.
3. **Basic/Advanced are authored snapshots, not observed progression.** The design cannot estimate whether a Basic implementation survives later hardening or whether defects propagate.
4. **Requirement provenance is coarse.** Platform documentation is cited, but obligation-level URLs/versions/spans, authority, scope, freshness, contradictions, and transformation review are absent.
5. **Repository provenance is incomplete.** Exact upstream commits, adaptation diffs, fixture licenses, and source-to-task lineage are not supplied.
6. **Expert validation is unreported.** “Manually reviewed” lacks reviewer roles, qualifications, independence, item decisions, agreement, adjudication, and accepted-alternative records.

### Intervention validity

7. **The Skill is a compound 101-file treatment.** Guidance, code examples, online retrieval rules, interaction policy, and safety text vary together.
8. **Intervention and instrument share lineage.** Criterion-aligned procedure can raise the co-authored score without establishing transfer or professional validity.
9. **The Skill conflicts with one-turn execution.** Mandatory user confirmation cannot occur; several prompts explicitly override it. Treatment fidelity and safety interpretation are unresolved.
10. **No adoption trace is reported.** Installed is not opened, consumed, followed, or causally used.
11. **No negative controls or ablations.** Irrelevant, stale, task-scrubbed, checklist-only, examples-only, and policy-only packages are absent.
12. **One harness bounds transport.** Claude Code familiarity and Skill discovery are part of the configured treatment; findings need not transfer to other harnesses despite the later release supporting three adapters.

### Measurement and analysis

13. **The released score mapping is not fully reconstructable from the paper.** Method assignments are implicit, one sampled task's weights do not transparently match the stated method formula, and no table builder binds released files to rows.
14. **Criterion semantics are inconsistent.** Missing dimensions default silently; rubric IDs repeat across tasks; criterion weights and criticality lack a cross-task contract.
15. **Mock/sandbox evidence is bounded.** It does not establish production gateway behavior, settlement, reversals, disputes, reconciliation, fraud/risk controls, observability, or compliance.
16. **Static checks remain gameable.** Presence, strings, hooks, and code patterns are not semantic proofs.
17. **LLM judge validity is absent.** Judge model/version/prompt coverage, repeated-call stability, expert agreement, false-positive/negative profiles, and evidence-view sufficiency are not reported.
18. **Errors are mixed into zero scores.** Retaining diagnostics does not make invalid measurement a capability failure.
19. **Compensatory RPR can hide critical failures.** No noncompensatory safety gate or decision-loss basis is validated.
20. **Method subsets differ by task.** A normalized weighted average still combines different instruments and does not create a common latent scale.
21. **Repeat count and uncertainty are missing.** Cell means and 101/108 signs cannot support reliability or stable rank claims without a complete clustered trial ledger.
22. **Post-hoc low-baseline analysis is headroom-confounded.** Larger bounded-score gains at low baseline are not evidence of a particular recovery mechanism.
23. **Output/RPR is not efficiency or developer value.** It omits most resources and no human developer outcome is measured.

### Reproducibility and operational realism

24. **No raw paper outcomes are released.** The +10.31-point contrast, repeats, negative cells, trace explanations, method bars, token ratios, and table denominators cannot be independently reconstructed.
25. **Release timing is close but post-publication.** Official relevance is clear; paper-time byte identity is not.
26. **A naive whole-tree pytest fails collection.** Duplicate task-local test module names and missing default `PYTHONPATH` produce six collection errors. The intended top-level command `PYTHONPATH=src python -m pytest -q tests` passes 31 tests and 76 subtests, validating runtime contracts but not any payment task or paper score.
27. **The runtime is highly privileged.** `--privileged`, passwordless sudo, optional nested Docker, and default network access weaken containment and make execution-policy identity material.
28. **Secret exposure is consequential.** Runtime inputs may be copied into agent-visible `/workspace`; traces can contain complete inputs/commands. Read-only mounting prevents mutation, not disclosure or exfiltration.
29. **Live dependencies age.** Provider endpoints, package repositories, Docker images, Alipay sandbox behavior, documentation, and model aliases require frozen identities or explicit transport evidence.
30. **No production consequence evidence exists.** No real transaction ledger, settlement/reconciliation, fraud event, rollback, operator review, user impact, repeated reliability, or deployment decision is measured.

## Transfer to skill-bench

### Retain

1. Keep the **functional-loop versus risk-hardening fork** as two distinct task claims, not a single difficulty ladder.
2. Retain plural structural, executable, state, and semantic observers, with criterion-to-observer lineage.
3. Reuse the same frozen evaluator across treatment arms.
4. Give each trial a fresh state and preserve files, traces, gateway requests, database states, and criterion-level evidence.
5. Report product/task heterogeneity and negative intervention effects rather than only an overall mean.
6. Treat high-consequence integration as a chain of typed evidence joins and critical gates.

### Repair

1. Bind every obligation to source URL/version/span, authority, valid time, scope, public basis, task transformation, and independent review.
2. Preserve exact upstream repository commit, license, adaptation diff, scenario seed state, and Basic→Advanced relationship.
3. Separate criterion `method`, `dimension`, `criticality`, `applicability`, `observer`, `evidence_view`, `weight`, and gate semantics; make task-qualified criterion IDs mandatory.
4. Freeze a paper-row reconstruction manifest: task, condition, attempt, model endpoint, harness, Skill hash, container digest, runtime inputs, evaluator/judge version, result, invalidity, resources, and table-builder hash.
5. Treat infra/judge invalidity separately from substantive failure and disclose complete eligible/attempted/valid/retried denominators.
6. Validate deterministic and semantic observers against seeded defects, legitimate alternatives, qualified expert labels, repeated calls, and cross-observer disagreement.
7. Record the full Skill exposure/adoption chain and instruction conflicts; do not call package presence transfer.
8. Use equal resource envelopes and ablate procedure, examples, raw documentation, retrieval, and policy components. Add irrelevant/stale/subtly unsafe negative-control packages.
9. Use task-clustered paired inference over prespecified tasks and repeated attempts; report effect distribution, harms, uncertainty, and sensitivity to weights/gates.
10. For safety/readiness claims, require authenticated external state, business-state reconciliation, collateral effects, recovery/rollback, monitoring, operator review, repeated reliability, and stakeholder decision evidence.
11. Replace privileged/default-network execution with a declared outer envelope and canaries, or explicitly limit claims to that permissive runtime.
12. Keep package efficacy, held-out procedure transfer, professional correctness, safety, production fitness, and readiness as separate validity arguments.

### Concrete cross-domain test

Use two unrelated consequential integration tasks—for example, one financial-state workflow and one non-financial authorization/state workflow—without making either a permanent domain. Freeze independently authored obligations and observers before treatment outcomes. For each task, run repeated no-package, checklist-only, examples-only, full-package, irrelevant-package, and subtly defective-package arms under the same model/harness/tool/network/budget envelope. Preserve package hashes; natural and forced discovery; clause reads; adoption at decision opportunities; code and native-state deltas; authenticated/mock transport labels; critical-gate results; new errors; invalid trials; complete cost; and task-clustered paired effects. Then transport the unchanged package to an independently authored equivalent form and observer. The general hypothesis is that source-faithful procedural guidance improves critical consequence gates without increasing unauthorized or collateral effects; the design must be able to reject it.

## Concrete repository action

No new build or consolidation task is warranted. The evidence reinforces existing grouped conclusions rather than changing them: shared task/Skill/evaluator lineage identifies package efficacy, plural observers do not inherit professional validity, permissive execution limits safety claims, and consequence promotion requires authenticated state plus decision evidence. Apply the retain/repair/test requirements when the next cross-domain procedural-transfer or consequential-action pilot is authored, using existing benchmark-bundle, procedural-package, trace, artifact-admissibility, execution-validity, task-health, metric, resource, action-authority, and validity-argument contracts.

## Claim boundary

Alipay-PIBench v1 contributes a timely 18-task, nine-product repository benchmark; a useful functional-versus-hardening decomposition; a substantial inspectable evaluator release; and manuscript-reported evidence that an official Alipay guidance package is associated with higher rubric completion for six model endpoints through Claude Code. Its method disagreements are valuable evidence that code presence, selected execution, and domain-semantic acceptance are not interchangeable.

It does **not** establish that the official release generated the paper tables; that the reported repeats, means, ranks, signs, or token ratios are reproducible; that only procedural knowledge differs between conditions; that the Skill was correctly adopted; that its mandatory confirmation policy was followed; that rubric passes imply source-faithful or alternative-complete implementation; that mocks or sandbox calls establish transaction correctness, fund safety, reconciliation, compliance, or operational reliability; that the LLM judge is calibrated; that the model ranking transports across harnesses; or that any tested system is professionally correct, production-fit, safe for real funds, or ready for deployment.