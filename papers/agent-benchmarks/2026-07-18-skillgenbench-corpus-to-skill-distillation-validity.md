# SkillGenBench isolates a useful corpus-to-procedure treatment, but v1 does not yet isolate or reproduce skill-generation quality

## Source, release, and review status

**Deep review of the complete immutable primary source and pinned official release.** I read the full 24-page arXiv v1 paper and appendices, checked the PDF against the complete text extraction, and inspected the complete 2,602-file official repository snapshot at commit `5a8bd61d8191e34fa1bbbffbff7f70db1d2a027d`. I audited the task/source/evaluator inventory, generation and execution runners, method profiles, representative instructions and verifiers, and attempted the released generation and evaluation entry points.

- **Paper:** Yifan Zhou et al., *SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents*, arXiv:2605.18693v1 (18 May 2026), <https://arxiv.org/abs/2605.18693v1>.
- **Local PDF:** `data/papers/pdfs/2605.18693v1-skillgenbench.pdf` (24 pages; SHA-256 `3b2d204855c71e86abcd9e4038194e4b9edda2424b8007c9f9f9f99f62938f3c`).
- **Full text read:** `data/papers/text/2605.18693v1-skillgenbench.txt` (SHA-256 `b799a31645db9682f11a2e63a0d584f305a3609c826d8c33989d7c0bf8c7c524`).
- **Official arXiv source:** `data/papers/source/2605.18693v1-source.tar.gz` (SHA-256 `4cb8ea9dc2875ddb6a152087537956ed2661a88d84a98197615067ca83fb7571`).
- **Pinned official release:** QuantaAlpha/SkillGenBench commit `5a8bd61d8191e34fa1bbbffbff7f70db1d2a027d` (15 May 2026), <https://github.com/QuantaAlpha/SkillGenBench/commit/5a8bd61d8191e34fa1bbbffbff7f70db1d2a027d>.
- **Complete local release snapshot:** `data/sources/releases/2605.18693v1-skillgenbench/QuantaAlpha-SkillGenBench-5a8bd61.zip` (407,510,785 bytes; SHA-256 `a76152071ed02b8a58462f24fe1d6ac84948acffe087d9aaa19371b1cbe5e215`; intentionally untracked because of size).
- **Release provenance:** `data/sources/releases/2605.18693v1-skillgenbench/provenance.json`; complete commit/tree metadata and README are preserved beside it.

The pinned commit predates arXiv v1 by three days, so it is a plausible paper-time candidate, not proof that its bytes generated every manuscript row. The snapshot grants no reuse license: it contains no `LICENSE` or `COPYING`, and README line 126 says `TBD`.

## Relevance, charter fit, and decision filter

This review advances charter objectives A and B by testing a central expertise-to-evaluation uncertainty: **when does a corpus-derived procedural artifact transfer source-grounded capability, rather than provide task hints, a compressed answer key, benchmark-specific formatting, or an executor-specific prompt treatment?** It is expansion with direct consolidation implications. Agent Skills are a treatment mechanism and inspectable artifact class, not the scope of `skill-bench`.

The concrete evidence is a paper-and-release audit of the chain `source corpus → generated procedure package → executor exposure/use → artifact/state → verifier → result`. Useful completion is a bounded claim and a reusable experimental design: retain pre-task distillation and fixed-executor comparisons, but require input parity, artifact identity, adoption evidence, untouched task families, and result reconstruction before calling the effect reusable procedural transfer.

## One-sentence contribution and assessment

SkillGenBench's genuine contribution is to make the generated procedural package—not merely a model with or without a supplied Skill—the nominal experimental object and to contrast task-conditioned with pre-task, collection-level generation; however, v1 exposes task-selected source bundles, execution-time documentation, unequal no-Skill and Skill runners, no released generated Skills or result rows, an incomplete baseline release, broken generation entry point and task manifests, and unresolved table denominators, so it supports a valuable benchmark design proposal plus manuscript-reported configured package effects, not an isolated or reproducible measure of reusable skill-generation quality.

## Research question and intended construct

The paper asks whether a generator can transform visible repositories or documents into a standardized `SKILL.md` that helps a separate fixed executor complete hidden-test tasks. It distinguishes:

1. **Task-conditioned generation:** source material and downstream task are visible while generating a focused Skill.
2. **Task-agnostic generation:** one collection-level Skill is generated before downstream tasks are revealed and reused without regeneration.
3. **Repository-grounded sources:** procedure is implicit across code, configuration, scripts, entry points, assets, dependencies, and runtime conventions.
4. **Document-grounded sources:** rules, prerequisites, branches, parameters, and ordered procedures are explicit but dispersed across long text; the paper separately analyzes code documentation and domain-knowledge documentation.

This is a useful construct fork. Task-conditioned performance estimates a package produced with task hindsight; task-agnostic performance can estimate reusable distillation only if source visibility, generation budget, package identity, executor context, routing, and held-out task lineage are controlled. Neither is intrinsically “expertise”: corpus authority, source correctness, procedural fidelity, task applicability, executor adoption, endpoint correctness, and professional consequence remain separate.

## Methodology and evidence

### Benchmark construction

The paper reports a five-stage model-assisted process (paper §3.3 and Appendix F):

1. construct entity/relation knowledge graphs and community summaries from each source;
2. generate practical computation-bearing scenarios;
3. jointly generate task specifications, solution code, and normal/edge/adversarial test cases;
4. screen with a strong solver under corpus-free and with-corpus conditions, returning tasks with corpus-free pass rate at least 20% or with-corpus pass rate at least 50% for refinement;
5. iteratively refine a reference Skill against test feedback and retain only tasks it can solve, followed by manual review.

The manual pass reportedly inspected 678 candidates and retained 187 (27.6%) under moderate difficulty, clear specification, quantitative evaluability, sufficient test coverage, and test-case quality. The final suite contains 123 code-repository, 28 code-documentation, and 36 domain-documentation tasks. The release matches those 187 IDs exactly across `data_source/` and `skill_evaluation/`, all marked enabled. It contains 32 repository collections, nine code-document collections, and 36 one-task domain-document collections.

The construction is more inspectable than an unexplained benchmark scrape, but its selection target matters. Tasks are optimized to be difficult without the selected corpus, not too easy with raw corpus, and solvable after a reference Skill is iteratively repaired against the tests. That selects for **reference-Skill-mediated benchmark fit**. It does not establish natural work prevalence, source completeness, general procedural importance, or a generator-independent task population. The final “human verification” section gives criteria and aggregate attrition but not reviewer count, qualifications, independent coding, item decisions, disagreements, adjudication, or task/source/verifier change lineage.

### Generation and execution protocol

The manuscript reports five generator methods across six generation backbones, with Claude Code as the common generation runtime and MiniMax-2.5 as the fixed executor. Temperature is reported as zero, generation has 16,384 output tokens, up to three refinement iterations/45 turns, and a 1,800-second timeout; downstream execution also uses temperature zero, 16,384 output tokens, and 1,800 seconds. Each package is evaluated up to three times, and an item passes if any trial passes.

The paper's primary Table 2 reports source-family pass@3. Method averages range from 10.8% to 14.4% on code repositories and 21.4% to 25.0% on documents; no generated method consistently dominates the no-Skill row. Appendix Table 4 explicitly notes roughly ±5 percentage-point task-bootstrap half-widths and says most pairwise method differences are not distinguishable. This is an important restraint: the evidence does not support a stable generator ranking.

The fixed downstream model is a strong design choice, but “fixed executor” is not enough. The treatment actually includes generated package, package layout, Skill-tool affordance, forced invocation, runtime profile, task documentation, and an agent loop. The release makes several of those differ by condition.

### Static diagnostics and failure taxonomy

The paper supplements endpoint success with rule-based package diagnostics: contract, environment readiness, source grounding, procedural coverage/state handling, constraints, and safety/hygiene. It also classifies completed verifier failures into source-specific mechanisms: code repositories are dominated by runtime/dependency, interface/schema, and asset/artifact errors; code documentation by interface/schema; domain documents by state/rule and numeric/formula errors.

The unique empirical insight is not that one static score predicts quality—it does not—but that procedural packages need plural observation. Source grounding, structural completeness, deployability, executor adoption, and downstream correctness are non-equivalent. SkillNet has the highest reported grouped static score while SkillSeekers has the highest dynamic source averages. That mismatch is useful evidence against scoring `SKILL.md` appearance as transfer.

Yet these diagnostics are unreproducible in the pinned release. No static-diagnostic implementation, generated-Skill inventory, per-package diagnostic rows, failure labels, annotation protocol, or result table is present. Table 3 says it uses a “canonical six-backbone generated-skill inventory,” for which one Skill per 187 tasks would yield 1,122 packages per method; the displayed `N` values instead range from 1,093 to 1,138, with no missing/multiple-package ledger or weighting rule.

## Release audit and reconstruction failures

### What is inspectable

The release contains all 187 evaluation bundles, task instructions, inputs, documentation, tests, 187 `task.toml` files, Docker definitions, a no-Skill runner, a Claude-agent runner, result-record formats, and one naive generation implementation. Evaluators are heterogeneous despite the paper's deterministic emphasis:

- 123 code-repository tasks divide into 60 heuristic, 36 ground-truth, and 27 reference evaluators;
- all 28 code-document and 36 domain-document tasks are labeled heuristic;
- reference modes are 118 `none`, 66 `single_file`, and three `directory`.

Many checks are executable, but “heuristic” or pixel/reference comparison is not automatically a valid correctness observer. The representative AnimeGAN task, for example, gates dimensions and a sky-region `B > R` color heuristic, then uses MAE ≤ 28 against one reference image; SSIM and PSNR are logged but not thresholded. This checks one authored visual witness and coarse channel behavior, not acceptable Shinkai-style diversity or professional image quality.

### The released generator does not run

A direct dry-run attempt of the README's generation entry point failed immediately:

```text
ModuleNotFoundError: No module named 'generated_skills_layout'
```

`baseline/naive_prompt/generate_skill.py` inserts `<repo>/eval` into `sys.path`, but the imported modules live in `<repo>/scripts`. Even after that import defect, its discovery function calls strict `json.loads` on task manifests. All 187 released `data_source/**/task.json` files are invalid JSON because their final property has a trailing comma: 122 fail at line 14 and 65 at line 12. The release therefore cannot enumerate a single generation task through its supplied implementation without repair.

Only `baseline/naive_prompt/` and shared helpers are released. SkillNet, SkillSeekers, SkillCreator, and the adapted EvoSkill implementation/assets used for the main comparison are absent. There are no `generated_skills/`, paper result rows, static diagnostic rows, failure labels, raw trajectories, exact run manifests, or table builders.

### Source-to-evaluation projection drifts

The `data_source` package is not byte-identical to the evaluation contract. A direct audit found 67 of 187 `expected_output_file` values differ between source `task.json` and evaluation `task.toml`. For AnimeGANv3_gen04, generation-time materials request a 1280×1024 file named `shinkai_candidate_006.png`, while the evaluation instruction and verifier require 2048×1365 `shinkai_landscape.png`. A task-conditioned Skill generated from the former and executed against the latter is exposed to a changed target. The paper's case study follows the latter. This is task/Skill/evaluator projection drift, not merely packaging style.

The paper's four case studies are also not fully reconciled to the pinned instrument: StyleTransfer_gtb01 and AnimeGANv3_gen04 are present, but the named Faker_gen08 and PDFPlumber_gen03 IDs are absent (the release has other Faker and PDFPlumber tasks). A case narrative may describe an earlier or renamed item, but without migration lineage it cannot anchor a released row.

### No-Skill is not treatment-parity evidence

The release's profile registry maps `noskill` to a one-shot host-side direct-LLM runner. Skill-assisted methods use Claude Code CLI with an agent loop, staged Skill package, filesystem tools, and forced Skill-tool invocation. The registry includes a `noskill_claude` parity profile, but the paper does not identify it and the primary no-Skill row is invariant across generation backbones.

The direct no-Skill runner receives the task instruction plus an 8,000-character digest of evaluation documentation. The Skill-assisted executor also mounts task documentation and receives the generated Skill. Thus the contrast is not cleanly `same executor + Skill versus no Skill`; and it is not `compressed Skill versus raw corpus denied`. It mixes runtime topology and still gives downstream raw/task-selected documentation. A gain could arise from extra context, forced deliberation, tool routing, task-target hints, or harness compatibility; a loss could arise from mandatory adoption of a bad package. Generated-Skill presence and required tool call also do not show semantic adoption.

### Reported table denominators do not reconcile

For Kimi K2.5 + Naive Prompt, Table 2 reports 9.8% on 123 Code tasks and 17.2% on 64 Doc tasks. The task-weighted overall is 12.33%, which matches Figure 7's 12.3% but not Appendix Table 4's 17.1%. Table 4 also gives 17.1% while Table 2's visible source cells cannot produce it under task weighting. This is not a rounding issue.

The primary metric is described as pass@3, but execution stops after the first pass and marks later trials `skipped_after_pass`. That correctly computes an “any success within at most three attempts” endpoint, but it does not yield three exchangeable trial outcomes per task or a per-attempt success probability. The bootstrap resamples task-level pass@3 indicators only; it does not capture generator-call uncertainty, Skill-generation variability, executor repeat variance, collection clustering, or shared source/task lineage. Temperature zero does not eliminate provider/runtime nondeterminism.

The release can dry-run the evaluation orchestration and writes complete placeholder records, but that verifies record plumbing, not container readiness or any paper score. Full reproduction additionally requires external repositories, built Docker images, proprietary APIs, absent methods, and unlicensed source assets.

## Unique insight: the generated procedure must be treated as a mediated intervention, not a score-bearing answer

SkillGenBench identifies the right missing experimental object. The reusable chain is:

```text
versioned source corpus and authority
→ source-selection/projection view
→ generation regime, method, model, tools, budget, and feedback
→ exact candidate procedure package and provenance
→ structural/source-fidelity/deployability observations
→ downstream task-family opportunity
→ retrieved/staged package and executor evidence view
→ invocation and proposition/step-level adoption or rejection
→ plan/code/action/artifact transition
→ independent verifier evidence
→ task consequence and bounded transfer claim
```

No edge inherits the next. A source-derived statement is not source-faithful; source fidelity is not applicable procedure; a valid `SKILL.md` is not loaded; loading is not semantic adoption; adoption is not correct execution; passing one co-authored verifier is not reusable expertise; same-collection reuse is not cross-source or professional transfer.

The key experiment is therefore a **mediated, equal-envelope intervention**, not a generator leaderboard. Freeze executor, task prompt, tools, runtime, documentation exposure, budgets, retries, and verifier. Generate the package before an untouched task family is selected. Preserve the exact package once, reuse it without edits, and cross at least:

1. no package/no corpus;
2. no package/raw corpus under the same retrieval budget;
3. generated package/no raw corpus;
4. generated package plus raw corpus;
5. source-faithful reference package;
6. irrelevant or deliberately defective package negative controls.

Then observe generation cost, package size, retrieval, forced versus natural invocation, proposition-level adoption, artifact/state changes, endpoint effects, new errors, and amortized value across eligible tasks. This separates compression from extra information, package quality from executor sensitivity, and reusable procedure from task-hindsight answer encoding.

## Limitations and validity threats

### Construct and task construction

1. **Reference-Skill selection coupling.** Tasks are iteratively retained after reference-Skill test feedback, favoring one authored procedure/check chain.
2. **Task-conditioned Skills can encode the target.** “Safety” discourages brittle leakage, but no released detector or information-bound quantifies how much task/output structure is copied into the Skill.
3. **Task-agnostic is mostly same-collection reuse.** The 36 domain-document collections have one task each, so that source family cannot demonstrate within-collection reuse at all.
4. **Source authority is unmodeled.** Repository/document presence does not establish correctness, currency, legitimacy, or professional authority.
5. **Task realism is proposed, not validated.** Model-generated function tools and selected media transformations are not sampled work demand or downstream recipient consequence.
6. **Human review is aggregate-only.** Qualifications, item decisions, agreement, adjudication, and repair lineage are absent.

### Treatment and measurement

7. **No-Skill runtime is unequal.** Direct one-shot LLM and Claude Code agent-loop profiles differ beyond Skill presence.
8. **Raw documentation remains available downstream.** Skill effects do not isolate compression or exclusive procedural transfer.
9. **Invocation is forced.** Required Skill-tool use measures compliance with a treatment; it does not show natural routing, reliance, or correct adoption.
10. **Generator adaptation is method-specific.** Four implementations and exact integration diffs are absent; EvoSkill is explicitly a benchmark adaptation, not its native loop.
11. **Static diagnostics are unvalidated proxies.** Rules and rows are unreleased; package appearance does not predict execution.
12. **Verifier semantics are heterogeneous.** Heuristics, exact checks, and single-reference media comparisons support different claims and are not one correctness scale.
13. **Any-of-three hides attempt reliability.** Early stopping is appropriate for budgeted solve-any success but cannot establish repeat reliability.
14. **Uncertainty ignores major levels.** Task bootstrap alone omits collection, source, package-generation, and executor variance.
15. **Costs are underreported.** Time/token limits are given, but call counts, actual tokens, prices, failures, retries, and complete resource ledgers are absent.

### Release conformance and reproducibility

16. **All 187 generation manifests are invalid JSON.** The released generator uses strict parsing.
17. **The generation import path is broken.** The documented entry point fails before task discovery.
18. **Four of five baseline implementations are missing.** Main comparisons cannot be regenerated.
19. **No generated packages or raw runs are released.** Static, dynamic, failure, repeat, and cost claims cannot be rebuilt.
20. **Sixty-seven source/evaluation filenames drift.** At least one representative item also changes dimensions and filename.
21. **Case-study IDs drift.** Two of four named cases are not in the pinned 187-task release.
22. **Tables do not reconcile.** Kimi/Naive overall results and static inventory denominators conflict.
23. **Release identity and rights remain incomplete.** The commit predates v1 but is not explicitly bound to paper rows and grants no license.

## Comparison with adjacent reviewed evidence

- **SkillsBench** estimates configured downstream efficacy under no/curated/self-generated Skill conditions. SkillGenBench usefully moves the intervention upstream to a dedicated generator, but its unequal no-Skill runtime and absent generated artifacts weaken that isolation.
- **LH-Bench** makes expert procedural packages, artifacts, and criteria visible. SkillGenBench supplies corpus-to-package generation regimes, but does not establish expert authority or procedural fidelity.
- **AFTER** separates procedure refinement and transfer edges. SkillGenBench's pre-task library is the cleaner anti-hindsight idea, but same-collection tasks and missing package/result lineage prevent transfer attribution.
- **ReasFlow** shows why paper-derived model-inferred guidance is not source-author or expert-approved knowledge. SkillGenBench likewise needs typed authorship and source-span lineage rather than treating generated `SKILL.md` as extracted procedure.
- **Online skill and memory budget value** requires equal resource envelopes, opportunity denominators, adoption, and amortization. SkillGenBench reports generation limits and pass@3 but not full generation/execution cost or reusable library value per eligible future task.

Together these sources support separate claims for source-faithful distillation, package deployment, configured executor benefit, cross-task reuse, cross-executor transfer, and professional consequence—not one “skill quality” score.

## Transfer to skill-bench

### Retain

1. Treat procedural artifact generation as its own versioned benchmark component, separately swappable from executor and grader.
2. Preserve both task-conditioned and pre-task task-agnostic regimes, labeling hindsight and intended reuse explicitly.
3. Cross implicit repository procedures with explicit-but-dispersed documents as different evidence structures, not a difficulty scale.
4. Make exact generated packages and structural diagnostics inspectable alongside downstream effects.
5. Use executable checks where the construct permits them and maintain a source-aware failure taxonomy.
6. Report non-benefit and negative transfer rather than assuming a Skill helps.

### Repair

1. Bind each generated clause/operation to source spans, scope, validity time, authority, omissions, contradictions, and generation transformations.
2. Freeze source/task/check splits by collection and procedural family; task-agnostic claims need at least two untouched tasks per source unit and preferably held-out families.
3. Enforce an equal executor/runtime/tool/context/budget envelope for no-Skill, raw-corpus, generated-Skill, and reference-Skill arms.
4. Separate package presence, load, retrieval, invocation, proposition-level adoption, artifact/state effect, endpoint success, and consequence.
5. Predeclare whether the estimand is any-success-within-budget, per-attempt reliability, expected quality, or amortized portfolio value; retain every attempted/skipped/invalid row.
6. Validate static rules against source fidelity, expert review, downstream failures, and adversarial packages; never aggregate them into intrinsic quality without evidence.
7. Reconstruct every paper row from immutable package, task, executor, environment, verifier, attempt, resource, and table-builder identities.
8. Add irrelevant, source-faithful-but-inapplicable, task-leaking, malformed, and subtly incorrect package controls.

### Concrete cross-domain test

Select two unlike existing pilots with at least four tasks per procedural family. Generate one package from the source pack before two held-out tasks are revealed, then reuse the exact bytes. Cross no context, equal-budget raw context, generated package, package plus raw context, and independently approved reference procedure under one executor/runtime. Add a task-conditioned package as an explicit hindsight upper bound and a task-ID/output-name scrub test for leakage. Score source-clause fidelity, natural/forced invocation, adoption, artifact/state predicates, independent recipient-facing checks, new errors, generation plus execution cost, and family-clustered uncertainty. The general hypothesis is that a compact source-faithful procedure can improve held-out work under a fixed envelope; the test should be allowed to falsify that hypothesis.

## Concrete repository action

No new queue task is warranted. Existing `procedure-package`, `procedure-instrument-layers`, `ablation-preflight`, configured-system, task-health, resource-observation, metric-monitoring, trace, release-manifest, and validity-argument machinery already hosts the required design. The nonduplicate action is to require the equal-envelope, pre-task package-identity and adoption checks when the next procedural-transfer pilot is assembled, rather than add a SkillGenBench-specific schema or narrow the benchmark to Agent Skills.

## Claim boundary

SkillGenBench v1 contributes a distinct and important benchmark question, a 187-task inspectable evaluation-bundle release, a useful task-conditioned versus pre-task generation fork, and manuscript-reported evidence that configured generated-Skill packages often fail and can induce negative transfer. Its fixed-model aspiration and plural artifact/execution diagnostics are worth retaining.

It does **not** establish that the pinned release generated the manuscript results; that the supplied generation path runs; that the five methods are reproducible; that no-Skill and Skill treatments differ only by the generated package; that task-agnostic performance demonstrates reusable procedural abstraction; that static scores measure intrinsic Skill quality; that pass@3 rows establish reliability; that source-family gaps identify repository-versus-document cognition rather than task/environment/verifier composition; or that the results support expert knowledge transfer, professional capability, cost-effectiveness, production fitness, or readiness.