# LQCDMaster: executable scientific traces are unusually rich, but the released evaluator cannot reconstruct the paper’s correctness claims

## Bottom line

LQCDMaster is one of the strongest released examples of an agent producing and actually running specialized scientific-computing code. The immutable paper and paper-time repository snapshot expose a planner–critic–executor–critic workflow, five procedural Skills, deterministic Wick-contraction generation, Slurm submission/monitoring, generated PyQUDA programs, scheduler logs, numerical outputs, 70 task prompts, reference programs/data, and two 70-task experiment trees. This is materially stronger evidence than plausible code, self-reported completion, or a polished scientific narrative.

The central validity problem is nevertheless decisive: **the release preserves execution evidence but not an executable evaluation record**. It contains no scorer, comparison script, score rows, per-task tolerance/convention decisions, adjudication record, or table-building program. A repository-wide filename audit found no file containing `score`, `grade`, `eval`, or `compare`; the five `benchmark.py` files generate references rather than score submissions. Consequently the reported `63 exact / 3 convention mismatch / 4 failure` GPT-5.4 table and either of the conflicting DeepSeek tables cannot be reconstructed from released bytes.

A small raw-output audit shows why that missing layer matters. GPT-5.4 local-pion task 1 agrees with the released reference to about `6.0e-14` maximum complex absolute difference. Local-kaon task 2 has real parts agreeing at that level but every displayed imaginary part has the opposite sign; the aggregate summary still calls all 20 local-2pt tasks “Exact,” while it separately classifies whole-correlator sign changes in two nonlocal tasks as convention mismatches. Without the comparator and adjudication policy, “exact,” “relative error,” and “convention mismatch” are not stable, reproducible labels.

The deterministic contraction boundary is also weaker than the paper’s framing suggests. In the pinned release, a direct call to `generate_einsum` for a representative baryon three-point task returns 2,252 characters of code that fails Python compilation with an unterminated string literal at generated line 25 and assigns comma-separated contractions inside `B.data = (...)`, which would form a tuple rather than a summed tensor after quoting were repaired. Released DeepSeek traces explicitly notice and rewrite this defect. The model is therefore not merely assembling trusted generated contractions; at least in this path it must diagnose and repair the supposedly trusted generator output, while the executor critic treats the generator watermark as a trust signal.

The strongest warranted claim is narrow but valuable: **at one pinned configuration of LQCDMaster, the authors preserve substantial evidence that two named configured systems generated PyQUDA programs, submitted many of them to a real Slurm/GPU environment, and often produced numerical artifacts close to author-generated references on one lattice configuration**. The release does not establish the paper’s exact success counts, independent physical correctness, validated expert knowledge transfer, model-isolated capability, reproducible efficiency, scientific novelty, professional equivalence, or readiness for consequential LQCD research.

## Source and reading record

### Complete primary source read

- Haofei Gao et al., *LQCDMaster: Agentic Scientific Computing for Lattice Quantum Chromodynamics Research*.
- Immutable record: <https://arxiv.org/abs/2607.15001v1>; PDF: <https://arxiv.org/pdf/2607.15001v1>.
- Local PDF: `data/papers/pdfs/2607.15001v1-lqcdmaster.pdf` (17 pages; 1,875,556 bytes; SHA-256 `4239004b9522f3c2b84eb8065799103110c413d19e30cf5257c518ff2cc22dd1`).
- Local full text: `data/papers/text/2607.15001v1-lqcdmaster.txt` (47,370 characters; SHA-256 `e281c4489ff967b2d9f5823344fe5b588240f07435e0b98453a6a9d3ee427089`).
- Local arXiv source: `data/papers/source/2607.15001v1-source.tar.gz` (SHA-256 `be0016519017f4314bdd203799ff8bab111b893b0d8038ec8ed589111d969384`).
- Read through the complete abstract, Sections 1–5, both appendices, tables, data/code statement, and references. The arXiv API reports v1 published 16 July 2026 and contains no withdrawal/retraction notice.

### Official release audited

- Official repository: <https://github.com/sjtu-sai-agents/LQCD_Master>.
- Pinned commit: [`e4a443e08d5904371fc280ce93c00ff84df21893`](https://github.com/sjtu-sai-agents/LQCD_Master/commit/e4a443e08d5904371fc280ce93c00ff84df21893), authored and committed 16 July 2026 at 07:35 UTC, about six hours before arXiv publication.
- Local archive: `data/sources/releases/2607.15001v1-lqcdmaster/sjtu-sai-agents-LQCD_Master-e4a443e.zip` (94,871,614 bytes; SHA-256 `92d0d4daa73b0639dfefb367c9252784c7a1c045b2ff18b877b45ffacf7f0526`).
- Extracted snapshot: `data/sources/releases/2607.15001v1-lqcdmaster/repository/LQCD_Master-e4a443e08d5904371fc280ce93c00ff84df21893/` (8,243 files; 531,963,666 bytes).
- Provenance and inventory: `data/sources/releases/2607.15001v1-lqcdmaster/provenance.json` and `inventory.json`.

The commit’s timing supports paper-time relevance but does not prove that every retained result was generated by exactly these bytes. The release also has unresolved reuse terms: the README displays an MIT badge and links `LICENSE`, but the pinned snapshot contains no license file and GitHub detected no license. This review treats the archive as inspection evidence, not as permission for downstream redistribution.

### Verification performed for this review

- Recounted all task and reference files by family.
- Audited planner/executor/configuration code, Skills, generator code, both aggregate summaries, all experiment-tree artifact types, representative trajectories, generated programs, submission/monitor records, logs, and outputs.
- Counted direct recorded tool calls in the non-duplicated `generation.json` stage traces.
- Compared representative released numerical outputs with released reference files using complex-valued NumPy loads.
- Invoked the pinned `generate_einsum` implementation for meson 2pt, baryon 2pt, meson 3pt, and baryon 3pt requests; compiled the returned snippets; and compiled the repository’s Python architecture/utilities. Meson 2pt, baryon 2pt, and meson 3pt snippets parsed; representative baryon 3pt output did not.
- Ran `python -m py_compile` over `core_architecture/*.py`, `utils/*.py`, and all `utils/generate_einsum/**/*.py`; repository source compilation passed. This checks source syntax, not GPU behavior or generated-snippet correctness.

No local AMD GPU/Slurm/PyQUDA environment or 573 MB gauge configuration was available, so this review did not rerun the scientific jobs. It inspected the released execution evidence and exercised the CPU-callable generator boundary instead.

## One-sentence contribution

LQCDMaster connects domain procedures, deterministic symbolic contraction generation, code-producing agents, HPC execution, and retained numerical artifacts in one inspectable scientific workflow, revealing that execution provenance and numerical agreement still require an independently specified evaluator and scientific claim boundary.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through bounded expansion and consolidation at the tacit-expertise-to-executable-work boundary. The concrete evidence is an immutable full-paper record, a paper-time official snapshot, a 70-task/reference inventory, Skill/routing audit, real generator execution, stage-trace census, numerical spot checks, and case-study provenance audit. It clarifies what executable scientific traces support—and what they do not—when comparator semantics, expert authority, alternative-solution admissibility, and table reconstruction are absent. Classification: expansion plus validation. Lattice QCD is a demanding mechanism case for cross-domain benchmark design, not a scope commitment.

Useful completion is a reusable distinction between **job execution**, **implementation conformance**, **physical correctness**, and **scientific consequence**, without adding an LQCD-specific schema or pilot.

## Research question and claimed contribution

The paper asks whether an agentic system equipped with expert procedural knowledge and symbolic contraction tools can autonomously translate natural-language LQCD requests into executable PyQUDA workflows and complete tasks spanning local/nonlocal two-point functions, Wilson loops, meson/baryon three-point functions, and harder new calculations.

Its claimed contributions are:

1. a planner–critic–executor–critic workflow for scientific code generation and HPC execution;
2. expert-authored Skills encoding LQCD and PyQUDA procedures;
3. a deterministic `generate_einsum` tool intended to move error-prone Wick contractions out of free-form model generation;
4. a 70-task benchmark across five observable families;
5. experiments with GPT-5.4 and DeepSeek-V4-Pro;
6. wall-clock/GPU-time comparisons with estimated expert implementation time; and
7. harder diagonal-Wilson-line and multi-hadron case studies.

The right benchmark question is not merely whether the system can emit runnable code. It is: **which retained evidence makes a generated scientific program correct for the requested observable, rather than merely executable or numerically similar to one shared implementation?**

## Methodology and system

### Workflow

`core_architecture/orchestrator.py` coordinates a planner, plan critic, executor, executor critic, Slurm submission, monitoring, and optional rewrite. The planner creates a structured YAML plan from the task and configuration facts. Critics identify plan/code defects; the executor emits `main.py`, test/full submission scripts, and analysis reports. Test submissions and monitors preserve Slurm job IDs, final states, exit codes, output paths, and excerpts. Full trajectories retain revisions and failures rather than only final prose.

This is strong operational design. A representative `2pt_local/task_1` chain binds the task prompt to planner revisions, generated code, test submission metadata, GPU output, and a 72-row numerical result. The diagonal case preserves an initial out-of-memory failure, a revised implementation, a completed monitored job, and 401 `.npy` files across the two executor directories. These are real failure-and-repair traces, not simulated narratives.

However, `submit_test_result.json` records scheduler acceptance, not task correctness. In the diagonal case it says `ok: true` because `sbatch` returned job `117100983`; only `test_monitor.json` later establishes `COMPLETED` with `0:0`. Neither record verifies that the scientific observable is correct. This distinction must remain explicit in any benchmark schema.

### Skills and routing

The release contains five Skills, including `lqcd-physics-correlator` and `pyquda-tool`. They provide operator conventions, propagator/inversion recipes, known ensemble parameters, PyQUDA APIs, code patterns, and instructions to use `generate_einsum`. `configs/skills.yaml` enables the two domain Skills, forces the correlator Skill for planner stages and PyQUDA Skill for executor stages, and maps executor access to `execute` and `generate_einsum`.

This is a substantial procedural scaffold. It is not a released expertise-validation record:

- the Skills have no claim-level source spans, author identity, reviewer identity, review date, version, disagreement history, or signed acceptance;
- the paper says LQCD experts annotated procedures, but does not report an elicitation protocol, number/qualification of reviewers per Skill, independent review, agreement, correction log, or held-out validation;
- parameters and code templates overlap the task solution process, so skill-enabled performance is configured-system conformance, not isolated backbone knowledge;
- `SkillSelection` includes selected names and routing mode at runtime, but the experiment records do not retain that selection object as a first-class per-stage artifact;
- generated-code watermarks and tool traces show some tool adoption, but they do not identify which Skill clauses changed which code spans.

The direct trace census found 91 `generate_einsum` calls covering 58 GPT task directories and 114 calls covering 59 DeepSeek task directories. DeepSeek traces also retain 214 `execute` calls over 59 tasks; GPT traces retain none in the direct stage records. These counts establish calls recorded in released stage traces, not universal Skill loading, causal benefit, or correctness.

### Deterministic contraction generator

Moving Wick contraction algebra into deterministic code is the paper’s most distinctive design choice. It narrows the model’s role and can make topology/sign structure inspectable. The tool returns structured terms for two-point functions and generated PyQUDA blocks for three-point functions.

The release nevertheless undermines a blanket “validated generator” interpretation:

1. There is no `test*.py` file in the pinned repository and no released regression suite for contraction identities, gamma conventions, flavor mappings, topology counts, numerical equivalence, or generated-code compilation.
2. A direct representative baryon-3pt call returned syntactically invalid code (`SyntaxError: unterminated string literal`, generated line 25).
3. The same output wraps multiple signed `contract(...)` calls as comma-separated elements inside `B.data = (...)`, a tuple-forming structure rather than an arithmetic sum.
4. DeepSeek experiment traces explicitly identify this tuple defect and rewrite it, proving the model sometimes repairs the trusted tool rather than merely pasting it.
5. Executor critiques repeatedly treat the `# FROM generate_einsum` watermark as grounds to trust the contraction block, even though a watermark establishes origin, not validity or unchanged use.
6. The generator code prints the full meson-3pt block as a side effect and has heterogeneous return contracts (`n_terms`, `n_topologies`, or only `ok`), making systematic validation less uniform.

A deterministic generator can reduce stochastic model error, but only a validated versioned generator plus generated-artifact tests supports that warrant. Here, shared generator/reference assumptions can create correlated agreement, and model repairs reopen the free-form error surface.

## Benchmark and evidence audit

### Task composition

The released prompt counts match the paper:

| Family | Tasks | Released reference files |
|---|---:|---:|
| Local 2pt | 20 | 20 |
| Nonlocal 2pt | 10 | 10 |
| Wilson loop | 12 | 1 shared table |
| Meson 3pt | 13 | 26 (vector and axial files per process) |
| Baryon 3pt | 15 | 15 |
| **Total** | **70** | **72 files** |

Tasks specify operators, sources, momenta, stout parameters, projectors, currents, output format, and (for 3pt) source–sink separation. The unit of work is meaningful scientific code production and execution, not short-answer recall. Families increase in implementation difficulty and exercise propagator inversion, link transport, sequential sources, gamma/color contractions, MPI gathering, and file production.

Coverage is still narrow in scientific-inference terms:

- every reported benchmark result uses the same C24P29 ensemble and configuration `10000`;
- tasks are templated variations within five related workflows, not independent projects;
- prompts and reference programs are public in the same repository;
- no held-out task/reference split or contamination assessment is released;
- there is no task-author provenance, independent solver construction, item review record, item-level difficulty evidence, or alternate-solution corpus;
- single-configuration correlator agreement is an implementation/debug check, not an ensemble-level physics result with statistical uncertainty.

### Reference construction and evaluator absence

Each family has a `standard/benchmark.py` that generates author reference outputs. These programs are valuable inspectable oracles, but the benchmark release has no executable submission comparator. There is no formal definition of:

- which output file maps to which reference file;
- accepted shapes, ordering, omitted columns, or time windows;
- absolute versus relative error and the norm/denominator used;
- zero/near-zero handling and complex-valued comparison;
- whether real and imaginary parts are both scored;
- tolerance (`1e-3` is stated informally in paper/README, but not bound to code);
- whole-sign, complex-conjugation, gamma-phase, current-orientation, and operator-normalization equivalences;
- malformed, missing, partial, or extra outputs;
- which executor revision is scored after retries; or
- who adjudicates a mismatch as convention-equivalent rather than incorrect.

This is not a cosmetic release omission. In the raw spot check, GPT local-kaon output is the complex conjugate of the released reference to numerical precision: the real parts agree and the imaginary signs reverse. The aggregate summary labels the entire local family exact, while explicitly assigning convention-mismatch status elsewhere. A comparator that ignores tiny imaginary components, recognizes conjugation, or compares only a real projection could reasonably pass it—but those are different estimands and must be declared.

The paper’s “machine precision” language should therefore be read as author-reported comparison under an unreleased procedure. Raw numerical closeness is strong conformance evidence only after the observable representation and admissible equivalence class are frozen.

### Experiment record completeness

The release is unusually rich:

- each model tree has 70 `trajectory_full.json` files;
- GPT has 73 `generation.json`, 73 submission records, and 73 monitor records;
- DeepSeek has 72 of each, reflecting retries/revisions;
- generated `main.py`, scripts, critiques, static-analysis records, scheduler logs, and many numerical outputs are present;
- full trajectories expose plan and executor rewrites rather than laundering retries from the denominator.

The records are not sufficient to reconstruct reported benchmark tables:

- no score row or item adjudication record is present;
- no table-building code is present;
- no cryptographic binding connects a score label to exact task, reference, generated program, output, comparator, and executor revision;
- model API request/response identities, endpoint revision, sampling parameters, token usage, and provider receipts are not preserved as complete per-trial manifests;
- aggregate directories are named `GPT_5.4` and `DeepSeek`, and summaries name endpoints, but the raw JSON does not establish immutable model weights or endpoint behavior;
- GPU/software environment details appear opportunistically in logs (for example QUDA version and accelerator identity), not as a normalized per-run environment lock;
- the large gauge configurations and runnable cluster environment are not included.

The configured-system identity is thus partially documented, not replayable. Results measure the whole package—backbone endpoint, prompts, forced Skills, generator version, critics, rewrite policy, PyQUDA/QUDA environment, HPC queue, reference implementation, and adjudication—not a backbone model in isolation.

### Reported results and internal discrepancy

The paper reports GPT-5.4 at 90.0% task success with 63 exact matches, three convention mismatches, and four failures. The pinned GPT summary agrees with that total and identifies two nonlocal sign flips plus one baryon sign flip.

DeepSeek is inconsistent across paper and release:

- the paper appendix table totals **56 exact, 3 convention mismatches, 11 failures**;
- `experiments/LQCD_Master_DeepSeek/summary.md` and the top-level README total **56 exact, 2 convention mismatches, 12 failures**;
- the category-level difference is local 2pt: the paper reports `16 exact / 1 mismatch / 3 failure`, while the release summary reports `16 exact / 0 mismatch / 4 failure`;
- the release summary describes local task 11 as about 0.16% relative error and classifies it as a failure, not a convention mismatch.

Both totals equal 70, so this is classification drift rather than a missing item. The released materials do not resolve whether paper-time adjudication treated local task 11 as a convention mismatch, whether another item changed class, or which comparator/version produced either table. The discrepancy remains unresolved and blocks exact reproduction of the paper’s DeepSeek result.

Single runs per task also prevent repeat-reliability estimates, confidence intervals, rank probabilities, or separation of systematic generator errors from stochastic model errors. Reporting “accuracy” after counting convention mismatches as success is defensible only if convention equivalence is predeclared, independently checked, and tied to intended use.

## Timing, efficiency, and human comparison

The GPT summary reports 80.8, 49.6, 42.5, 81.1, and 137.0 wall-clock minutes across the five categories, with 48.9 total GPU minutes. The paper compares this with expert estimates of approximately 1, 2, 4, 4, and 8 hours per task family and concludes substantial acceleration.

The traces support real wall-clock and scheduler timing evidence, but the efficiency comparison is not a controlled human study:

- expert times are round estimates without sample size, participant qualifications, task assignment, measurement method, uncertainty, or retained work logs;
- agent wall time includes queue delay differently from GPU runtime, while human time is not decomposed into active work, waiting, execution, review, and correction;
- benchmark/reference/Skill/generator development and expert verification costs are excluded;
- failed jobs, retries, reviewer adjudication, and post-run scientific validation are not costed consistently;
- no human and agent produce independently blinded artifacts under the same environment and acceptance test;
- no API token/cost ledger is released.

The evidence supports that the released workflow can turn around many templated jobs quickly on the authors’ infrastructure. It does not establish net labor savings, quality-adjusted cost advantage, or faster professional research after verification burden.

## Harder scientific case studies

### Diagonal Wilson-line distribution-amplitude task

This is the best operational case. The task requires a Coulomb-gauge-fixed input, five body-diagonal wall-source momenta, recursive averaging over six shortest paths per diagonal step, both directions through `z=12`, and production over many configurations. The trace catches a planner’s wrong gauge path and multigrid structure, revises the plan, records an executor out-of-memory failure, rewrites memory handling, and preserves a completed Slurm monitor. The release includes 401 `.npy` files across two executor revisions, including many configuration-specific outputs.

This demonstrates planning repair, runtime failure recovery, sustained GPU execution, and artifact production. It does not independently establish the recursive transport convention, normalization, physical interpretation, equality to an established implementation, or novelty. No external reference array, independent implementation, scientific test suite, uncertainty analysis, or expert acceptance record is released. “Job completed and produced 201 arrays” is not “new observable is correct.”

### Multi-hadron tasks

The multi-hadron tree contains 14 full trajectories, 22 executor-generation/submission/monitor sets, and thousands of text outputs across multiple tests. Prompts include combined six- and nine-quark operators and explicitly prohibit factorizing them into products of separate hadron correlators. Planner critics catch structured-plan defects such as wrong MPI layouts and underspecified composite operators.

This is valuable stress evidence for iterative specification repair. It is not a controlled case-study sample: multiple task families, repeated `test_*` directories, and unsuccessful/revised attempts are present without a frozen selection rule or aggregate result manifest. The release lacks independent reference outputs and scientific adjudication for the headline “new tasks” claim. Successful scheduler completion and plausible multi-hadron code do not verify that all Wick topologies, symmetries, projections, signs, and normalization are correct.

## Unique insight and evidence

### Evidence actually established

The paper and pinned release jointly establish:

1. a real open scientific-code agent architecture;
2. procedural LQCD/PyQUDA guidance available to the configured system;
3. deterministic contraction machinery with inspectable source;
4. 70 public prompts and author-generated reference outputs;
5. extensive generated programs, revisions, Slurm records, logs, and numerical artifacts;
6. real examples of runtime failure and repair;
7. author-reported aggregate outcomes under two named commercial endpoints; and
8. harder case-study execution artifacts beyond the benchmark’s single configuration.

### Unique insight: scientific execution closes one loop while leaving the evaluator loop open

LQCDMaster shows that scientific-agent validity has at least four distinct loops:

`request → plan/code → executable job → artifact`

is the **execution loop**. LQCDMaster closes this unusually well.

`artifact → frozen comparator → declared equivalence class → score/adjudication`

is the **evaluation loop**. The release leaves it open.

`score → independent physical assumptions/checks → scientifically valid observable`

is the **scientific-validity loop**. One shared implementation and one configuration do not close it.

`valid observable → ensemble analysis/interpretation → external scientific consequence`

is the **research-consequence loop**. The paper does not evaluate it.

This decomposition prevents two common promotions:

- **scheduler success → task success**: `sbatch` acceptance and exit code zero establish process execution, not scientific correctness;
- **numerical agreement → truth**: agreement may result from a correct independent implementation, but also from shared conventions, shared code, shared bugs, answer access, representation choices, or an adjudicator’s post hoc equivalence decision.

The relevant benchmark primitive is therefore not simply a reference number. It is a versioned **solution-equivalence contract** binding the intended observable, authoritative derivation, implementation independence, accepted transformations, comparator code, tolerances, near-zero policy, artifact mapping, and expert adjudication. Without that contract, “machine precision” is descriptive rather than a stable validity claim.

This sharpens adjacent reviewed work:

- Like BrainPilot, LQCDMaster shows that domain material being present or loaded is not evidence that expert knowledge was source-faithful, adopted, or beneficial. LQCDMaster adds stronger downstream execution evidence but still lacks clause-to-artifact-to-consequence lineage.
- Like ReasFlow, it turns procedures into reusable guidance; unlike a purely procedural card, it can exercise code on real infrastructure. Yet shared procedure/generator/reference assumptions create correlated correctness risk.
- Like Opti-Agent-Bench, it makes module boundaries and failures inspectable. LQCDMaster’s missing scorer shows why module execution telemetry cannot substitute for end-to-end validity.
- Executable scientific-workspace designs preserve commands, reads/writes, and artifacts; LQCDMaster confirms that these are necessary for operational realism but insufficient unless evaluator and claim records are equally reconstructible.

## Reproducibility and operational realism

**Paper inspectability: strong.** The 17-page paper clearly describes architecture, task families, aggregate outcomes, timings, two model conditions, limitations, and case studies. It discloses sign conventions and DeepSeek failures rather than presenting only a headline score.

**Release inspectability: unusually strong for execution, weak for scoring.** The paper-time snapshot contains architecture, prompts, Skills, tools, reference programs/data, trajectories, programs, Slurm records, logs, and outputs. It lacks evaluator code, score rows, adjudication, table builders, environment locks, complete model-call manifests, and a valid license file.

**Computational reproducibility: limited.** The reference and generated code are inspectable, but rerunning requires unavailable large gauge data, PyQUDA/QUDA versions, AMD GPU cluster configuration, Slurm setup, resource cache, and commercial model endpoints. Paths are hard-coded to `/public/share/...` and `/public/home/...`. The release is an evidence archive, not a portable reproduction package.

**Operational realism: high for one implementation layer.** Real lattice sizes, propagator inversions, MPI/GPU execution, scheduler queues, out-of-memory recovery, many configurations, and numerical artifacts are far more realistic than toy code benchmarks. Realism remains narrow: tasks stop before robust ensemble statistics, uncertainty propagation, renormalization, continuum/finite-volume analysis, data governance, collaboration, peer review, replication, and scientific decision consequences.

**Empirical inference: weak to moderate.** Seventy tasks give within-suite breadth, but each is a single public templated task on one configuration, with one trial per configured system and no executable released scoring. The data support a rich configured-system case study, not a general model, expertise-transfer, or scientific-automation claim.

## Limitations and validity threats

### Expertise and configured-system identity

1. Skill claims lack source-span provenance, reviewer authority, version history, disagreement, and signed approval.
2. Skill selection/loading is not retained as a first-class per-stage record.
3. Tool calls show opportunity/use, not which clauses were adopted or whether they improved artifacts.
4. Skills, generator, critics, and backbone vary together; there is no no-Skill or no-generator ablation.
5. Exact model versions, endpoint state, sampling parameters, and complete request/response manifests are absent.
6. Results identify configured systems, not isolated backbone capability.

### Generator and correlated-oracle risk

7. No formal generator test suite is released.
8. The current baryon-3pt generator emits non-compiling code in a representative direct call.
9. Its comma-separated sink contractions encode a tuple instead of a sum after quote repair.
10. DeepSeek repairs generated contraction code, reopening model-generated algebra risk.
11. Critics trust watermarks without verifying generated-code identity or tests.
12. Reference implementations and agent tooling may share conventions and conceptual machinery.
13. Agreement with one implementation does not detect shared bugs or prove implementation independence.

### Benchmark and scoring

14. All benchmark results use one ensemble configuration.
15. Public prompts, reference programs, data, and Skills create contamination/copying risk.
16. No held-out tasks, private references, or split rationale are released.
17. No scorer, comparator, score record, or table-building code is released.
18. Error norm, denominator, complex handling, near-zero policy, shape policy, and tolerance are not executable.
19. Convention equivalences are not predeclared in a machine-readable contract.
20. GPT local-kaon raw complex conjugation is labeled exact without released rationale.
21. The paper and release disagree on DeepSeek’s mismatch/failure classification.
22. Retry-to-final-score selection and executor revision identity are not score-bound.
23. Single trials provide no reliability or uncertainty estimate.
24. “Accuracy” counts convention mismatches as success without independent equivalence adjudication.

### Execution, timing, and consequence

25. Scheduler acceptance, process completion, output presence, and physical correctness are distinct states.
26. Hard-coded private-cluster paths and absent gauge data prevent portable replay.
27. Environment identity is distributed through logs rather than normalized and hash-bound.
28. Human-time estimates are not a controlled comparative study.
29. Expert verification, benchmark construction, retries, infrastructure, and maintenance costs are omitted.
30. No evidence measures net labor saved after scientific validation.
31. Case studies lack independent references, replication, or external expert acceptance artifacts.
32. Multi-hadron case selection and success criteria are not frozen.
33. No result establishes ensemble-level physics, novelty, publication quality, or downstream research consequence.
34. Missing `LICENSE` leaves release reuse terms unresolved despite the README badge.

## Transferable benchmark-design implications

### Retain

1. **Artifact-first scientific work.** Preserve task, plan, critiques, generated program, scripts, submission, monitor, logs, outputs, and revisions.
2. **Separate submit from monitor.** Scheduler acceptance and final job state must be different typed events.
3. **Preserve failures and repair.** The diagonal out-of-memory trace is more diagnostic than a cleaned final success.
4. **Use deterministic domain tools where appropriate.** Symbolic generators can narrow model discretion if versioned and validated.
5. **Expose reference implementations.** Inspectable oracle construction is better than unexplained labels.
6. **Evaluate on real infrastructure.** HPC execution catches memory, API, MPI, file, and environment failures absent from static code grading.
7. **Keep family-specific outcomes.** Local/nonlocal, gauge, meson, and baryon tasks diagnose different failure surfaces.
8. **Disclose convention issues rather than hiding them.** Convention-equivalent results should remain separate from byte/numeric identity.

### Repair

1. **Release an executable evaluator.** It must map exact artifacts to references and emit immutable item-level score records.
2. **Freeze a solution-equivalence contract.** Declare observable representation, accepted transformations, norms, tolerances, near-zero handling, shapes, time windows, and disqualifying failures before trials.
3. **Bind every result row.** Hash task, Skill bundle, generator, prompts, model configuration, environment, code, output, reference, comparator, adjudication, and table-builder.
4. **Validate the generator as software.** Add unit, property, compilation, topology, sign, flavor, mutation, and numerical tests; do not trust a watermark.
5. **Separate generator output from model edits.** Store original generated bytes, patch/diff, reason, tests, and reviewer acceptance.
6. **Use independent oracles.** Compare against separately implemented formulations or analytical/metamorphic invariants, not only one related code path.
7. **Record expert authority.** Bind each procedural claim and equivalence judgment to source spans, reviewer qualifications, disagreement, and approval.
8. **Retain routing/adoption lineage.** Record selected Skills, delivered clauses, code spans affected, and verification consequences.
9. **Add repeated and ablated trials.** Cross no-Skill/Skill, no-generator/generator, and shared/independent oracle conditions under matched budgets.
10. **Measure human work directly.** Use comparable tasks, logs, active/wait/review time, quality gates, multiple qualified participants, and uncertainty.
11. **Package a portable replay slice.** Include a small lawful fixture, pinned container/environment, CPU-safe checks where possible, and one end-to-end scorer smoke test.
12. **Resolve licensing before reuse.** A badge is not a license grant.

## Concrete repository actions and tests for skill-bench

The reusable tests are cross-domain:

1. **Completion-state separation:** a job can be submitted, run, exit zero, emit an artifact, pass format checks, pass numerical checks, and pass expert/scientific review independently. The benchmark must not collapse these states.
2. **Comparator mutation:** flip imaginary signs, conjugate complex outputs, permute rows, omit columns, change normalization, alter tiny denominators, and introduce a shared constant bug. Require declared behavior for each mutation.
3. **Generator trust:** inject syntax errors, tuple-versus-sum defects, wrong topology signs, stale generator hashes, and model edits after generation. A watermark alone must never satisfy validation.
4. **Oracle independence:** run shared-code and independently implemented references plus metamorphic invariants; report correlated-failure risk rather than treating agreement as truth.
5. **Result reconstruction:** rebuild every aggregate table from item score records and fail release validation on any unbound, overwritten, or manually adjudicated cell.
6. **Expertise adoption:** distinguish Skill availability, routing, loading, clause adoption, artifact delta, independent check, and downstream consequence.
7. **Alternative-path admissibility:** score two scientifically equivalent implementations that differ in representation and one superficially close implementation that changes the intended observable.

These implications overlap existing `skill-bench` contracts for configured-system identity, procedural Skills, artifacts, traces, metrics, and result reconstruction. To avoid duplicate building, this review adds no queue task; its evidence should inform consolidation and future fixtures rather than create an LQCD-specific subsystem.

## Claim boundary

The immutable v1 paper and paper-time pinned repository establish a real LQCD-oriented agent workflow with procedural Skills, symbolic contraction tooling, 70 public tasks, author reference implementations/data, extensive generated PyQUDA code, Slurm/GPU execution records, numerical outputs, retries, and harder case-study artifacts. Direct review confirms that the repository source compiles, several generator paths emit parseable snippets, representative pion output is extremely close to the released reference, and real execution/failure-repair evidence is retained.

They do **not** establish the exact published score tables from released bytes; a stable definition of exactness or convention equivalence; resolution of the DeepSeek `3/11` versus `2/12` mismatch/failure discrepancy; correctness of the baryon-3pt generator; independence of references from shared assumptions; source-faithful or expert-validated Skills; isolated backbone capability; repeat reliability; portable reproduction; controlled human-time savings; physical correctness beyond one implementation/configuration; case-study novelty or scientific acceptance; professional equivalence; consequential-research readiness; or MIT-licensed reuse.

The durable lesson is positive but bounded: **scientific-agent benchmarks should preserve LQCDMaster’s execution chain and add an equally rigorous, independently inspectable evaluation and scientific-validity chain.**
