# DeployBench: fresh-machine execution is a prerequisite witness, not research reproduction—and the hidden target helps create the reported “completion-judgment” gap

## Source and review status

**Deep review of the complete immutable primary paper plus a pinned-release audit.** I read the full 25-page arXiv v1 paper, inspected all 51 released task quartets at the closest public paper-time commit, statically checked every shell and Python evaluator file, and reconstructed AdaLoRA from task metadata through reference setup, verifier execution, output log, parser, and verdict. I also traced Ward’s QEMU verifier and SILT’s compatibility rewrite as contrasting system and legacy cases.

- Paper: Yuanli Wang et al., *DeployBench: Benchmarking LLM Agents for Research Artifact Deployment*, arXiv:2606.05238v1, <https://arxiv.org/abs/2606.05238v1>
- Version read: immutable v1, submitted 3 June 2026; the acquired arXiv metadata contains no withdrawal or retraction notice
- Local PDF: `data/papers/pdfs/2606.05238v1-deploybench.pdf` (25 pages; 592,863 bytes; SHA-256 `1b7520ca2168c15f08186d9f6556fcd6c13c43a771ad705fde1f8d11368b5766`)
- Local full text: `data/papers/text/2606.05238v1-deploybench.txt` (87,422 characters / 87,612 bytes; SHA-256 `21624e12efb54d39d762f0c7df83bf069d5e76733cdf838cd9bd7fcfd1094561`)
- Official repository: <https://github.com/pentium3/DeployBench>
- Closest public paper-time snapshot: commit `b45062e56e99658ea674c473921346ced5481e01`, dated 1 June 2026, two days before v1; tree `313992adf77cc40336a6ca78cf376d781db38d5f`
- Local archive: `data/sources/releases/2606.05238v1-deploybench/pentium3-DeployBench-b45062e.zip` (258,235 bytes; SHA-256 `10a2ca0df0d4e521f39db0949b25e9385ecba09b97c2e6d960c078d533ab842a`; `unzip -t` passed; intentionally ignored)
- Later comparison snapshot: commit `be8f68a328fe6dcda137d46adb05f330d546d394`, dated 30 June 2026. Only `README.md` differs across the same 206 release paths; all task quartets are byte-identical in the bounded comparison.
- Provenance: `data/sources/releases/2606.05238v1-deploybench/provenance.json`
- Machine-readable release audit: `data/sources/releases/2606.05238v1-deploybench/release-audit.json`

The public snapshot contains 51 `task.json`, 51 `setup_reference.sh`, 51 `verify.sh`, and 51 `task_parser.py` files. It does **not** contain the third-party `code.zip` inputs, paper PDFs, paper/repository URLs or commit identities, cloud-image/runner construction, model trajectories, verifier logs, result matrix, diagnostic reports, human labels, or table-reproduction code. I did not provision the costly Google Cloud CPU/GPU/QEMU matrix, download all mutable third-party assets, or rerun the four model systems. Release findings below are static or explicitly identified synthetic parser-conformance results, not a reproduction of paper scores.

## One-sentence contribution

DeployBench usefully makes **environment readiness for one authored experiment projection** an executable, fresh-machine gate across 51 unusually heterogeneous research artifacts, but its paper and release support configured-system success on those private projections—not general research reproduction—and its headline completion-judgment diagnosis conflates false success claims, honest partial abstention, hidden-target mismatch, evaluator mutation, and deployment failure.

## Why this matters for skill-bench

Knowledge-work agents often inherit a prerequisite substrate: a spreadsheet must recalculate, a database must accept migrations, a notebook must run, a document renderer must preserve structure, or a scientific artifact must execute before substantive work is possible. DeployBench isolates this boundary better than benchmarks that hand agents a working container.

Its strongest transferable idea is a **deployment witness chain**:

```text
identified source artifact and paper target
→ frozen input repository/assets and clean base image
→ agent-created environment and compatibility changes
→ independent execution of a bounded target
→ native runtime evidence and outputs
→ parser/verdict
→ downstream-use eligibility
```

Each arrow needs its own identity and evidence. Passing the final parser only supports the claim that one authored projection ran under one environment snapshot. It does not by itself establish source preservation, exact paper replication, result agreement, scientific validity, maintainability, security, portability, professional utility, or readiness for downstream research.

This review advances charter objectives A, B, and C through expansion and release validation. DeployBench is a methodological case about executable prerequisites across AI, systems, and scientific computing—not a proposal to narrow `skill-bench` to software deployment.

## Research question and defensible claim boundary

The paper asks whether an LLM agent can turn a minimal Ubuntu VM, paper, and code repository into an environment that executes a lightweight target derived from a designated paper experiment (Sections 1 and 3, pp. 1–5). It contributes:

1. 51 tasks from 49 public artifacts dated 2008–2025: 25 AI/ML, 19 systems, and 7 scientific-computing tasks;
2. 11 primary language ecosystems, 22 GPU tasks, 5 QEMU/custom-kernel tasks, and 10 designated legacy tasks;
3. manually constructed reference deployments and task-specific experiment scripts;
4. a two-stage released evaluator surface: experiment/log production followed by per-task parsing;
5. 204 single model–task runs using four models under OpenHands on fresh Google Cloud VMs;
6. descriptive analyses of success, runtime/tokens, failure locations, command phases, recovery, and stop type.

The strongest defensible empirical claim is:

> Under the authors’ reported June 2026 task projections, Ubuntu/Google Cloud infrastructure, OpenHands policy, prompts, budgets, mutable external services, and hidden evaluation implementation, four configured model systems had different deterministic verdict totals; 83 of the 154 failed runs passed the generic log layer but failed the task-specific check, and stop/report behavior differed by configured model.

The evidence does **not** establish general research-artifact deployment capability; paper-result reproduction; source or artifact representativeness; verifier soundness/completeness; stochastic reliability; exact model effects; causal root causes; cost-effectiveness; portability to another cloud/date; scientific or professional validity; downstream usability; production fitness; or readiness.

## Methodology and system

### Task sourcing and construction

The authors selected top-venue papers, prioritized widely used public repositories, and favored artifact-evaluated systems papers where available. They manually attempted candidates and excluded artifacts judged broken, incomplete, unreproducible, or dependent on unavailable datasets/weights (Section 3.2, p. 4). Each retained task received a fresh-VM reference deployment, a lightweight experiment target, a setup script, a verifier, and a 10–60 minute agent budget. Three author-constructors assigned easy/medium/hard labels from dependency layers, GPU/QEMU needs, legacy repair, and observed debugging.

This creates a useful feasible-task instrument but an outcome-conditioned corpus. There is no venue sampling frame, candidate count, rejection ledger, independent artifact-author review, authoring time, inter-rater agreement, or distribution over real deployment demand. “Widely used” is not operationalized. The 49-artifact set supports coverage examples, not prevalence or population-level deployment claims.

The released `papers.csv` reproduces the 51 task labels and metadata, but supplies only paper titles—not source-paper URLs, repository URLs, release tags, source commit hashes, asset versions, licenses, or input hashes. `task.json` points to a non-released `code.zip`; 26 of 51 `deploy_prompt` values are blank. Consequently, the public release cannot reconstruct the actual paper/repository input identity or prove that a rerun uses the evaluated source state.

### Configured system and execution environment

All runs use OpenHands on fresh Google Cloud Ubuntu 22.04 VMs with 16 vCPUs and 64 GB RAM. GPU tasks receive one NVIDIA L4 without preinstalled CUDA drivers. Docker is prohibited; five tasks may build and boot nested QEMU systems. Per-task agent budgets vary from 600 to 3,600 seconds, with separate verifier budgets in the task metadata. The same system prompt asks the agent to read the paper/repository, build natively, run a **simple smoke test**, avoid the full paper experiment, and write `RUNBOOK.MD` (Section 4.1 and Figure A1, pp. 6 and 18–19).

The paper does not release the VM image digest, base-image provisioning, OpenHands commit/configuration, adapter code, maximum-step policy per model, network/credential rules, third-party source placement, runner orchestration, or teardown/reset evidence. “Fresh VM” is paper-reported. The released task definitions contain historical absolute paths and cannot independently instantiate the environment.

The agent can use web lookups and the setup scripts are now public. Future use therefore needs a leakage policy: an internet-enabled agent can potentially retrieve the benchmark repository and copy exact reference repairs or infer the hidden target. The paper-time experiment may predate public release, but that does not protect subsequent scores.

### Hidden target and two-stage verifier

The paper describes a global rule-based parser followed by task-specific checks (Section 3.3, pp. 4–5). The release exposes a slightly different implementation decomposition: each `verify.sh` executes the target and writes `output.log`; each `task_parser.py` examines log/artifact evidence and emits JSON. All 102 shell scripts pass `bash -n`, and all 51 parsers pass Python AST parsing.

The experiment target is not merely observed; in some tasks the evaluator helps construct it. Six of 51 released verifier scripts contain installation or remote-download operations. Ward’s verifier installs `expect` if absent before booting QEMU. AdaLoRA’s verifier downloads the DeBERTa snapshot if missing and monkey-patches the imported experiment module’s `os.path.isdir` behavior so a local model directory is treated differently. These interventions can be legitimate verifier dependencies, but they mean final success is partly a property of evaluator-supplied assets/code paths rather than only the state left by the agent. Evaluator mutation must be recorded separately from agent-created readiness.

Forty-two of 51 verifier scripts contain at least one `|| true`, often for cleanup or diagnostic tolerance but sometimes around execution/extraction paths. All 51 write `VERIFY_EXIT_CODE`; only one parser (`qsym_sec18`) mentions that marker. Only three parsers perform explicit numeric conversion, three invoke a structured parser, and six read more than the main log as text. These counts are static surface indicators, not proof that the remaining checks are invalid, but they show that most final verdicts depend on filename/nonempty-file predicates and fatal-substring absence rather than semantic result comparison.

### End-to-end reconstruction: AdaLoRA

The released AdaLoRA path is concrete:

1. `task.json` gives a 2,400-second agent budget, 900-second verifier budget, L4-class GPU condition, and no task-specific hint.
2. `setup_reference.sh` builds Python 3.9.19, installs a pinned PyTorch/CUDA and Hugging Face stack, installs AdaLoRA/transformers code editable, and downloads `microsoft/deberta-v3-base` without a model revision/hash.
3. `verify.sh` deletes the old output directory, checks CUDA, downloads the model if absent, imports `run_glue.py`, modifies its view of the local model directory, and runs three steps of CoLA training/evaluation with AdaLoRA arguments.
4. `output.log` records runtime text and an exit marker.
5. `task_parser.py` requires code sentinels, absence of four fatal substrings, and three nonempty paths: `rank_pattern.json`, `trainer_state.json`, and `train_results.json`.

This is substantially better than an import-only smoke test: it reaches the paper’s LoRA path, GPU framework, model, dataset API, trainer, and output machinery. But it does not compare result values, validate JSON schemas, inspect the rank pattern, check model provenance, require the logged exit marker to be zero, or establish agreement with a paper result.

A bounded synthetic conformance test in `release-audit.json` created only the code sentinels, three one-byte expected files, and an `output.log` containing `VERIFY_EXIT_CODE=1`. The released parser returned `{"status":"success"}`. This does **not** show that the complete `verify.sh` pipeline can be bypassed—the verifier deletes prior outputs and tries the experiment—but it proves that the final parser’s success rule is inconsistent with its own logged nonzero exit evidence. A partial run that leaves expected files and fails without one of four substrings can therefore be misclassified unless unreleased orchestration separately enforces shell exit status.

### Contrasting reconstructions: Ward and SILT

Ward’s verifier checks a harder system path: locate `ward.efi`, boot it under QEMU/KVM, run `lebench`, extract a CSV from serial output, and render a PDF. Yet its parser only requires nonempty CSV/PDF files and absence of six substrings. It does not parse the CSV schema/row count, validate the PDF type, verify benchmark values, or check `VERIFY_EXIT_CODE`. The same isolated contradictory-exit fixture returns success. Again, the experiment execution is meaningful, but the terminal verdict loses much of that evidence.

SILT demonstrates compatibility repair. The reference setup downloads OpenSSL 1.0.2u, creates a new 52-line `tbb::atomic` wrapper backed by `std::atomic`, adds a private-header compatibility shim, and injects flags across the build. This tests useful modernization work. It does not show reproduction of the untouched 2011 artifact; it shows that one author-written compatibility projection builds and passes a selected modern check. The compatibility patch is both an oracle witness and a transformation whose effect on original semantics needs separate validation.

## Evidence and reported results

### What the paper reports

Across 51 single attempts per model, reported success counts implied by Table 2 are 26/51 for GPT-5.3-Codex, 14/51 for Gemini-3.1-Pro, 6/51 for Grok-4.20, and 4/51 for GPT-5.4-Mini. Of 154 failed runs, 71 are caught by the global layer and 83 only by the task-specific layer (Table 4, p. 8). Average per-task token input is extremely large—0.64M to 2.54M depending on system—while runtime averages 6.1–18.1 minutes (Table 3, p. 7).

Among failed runs, 97 end by explicit self-stop, 37 by timeout, and 20 by maximum steps (Table A10, p. 24). The paper says 55 self-stopped failures report `SUCCESS`, 32 report `PARTIAL`, and ten have another/no identified runbook status; 81 of the 97 run what authors label a meaningful pre-finish check and 16 only a shallow check (Section 5.3, pp. 9–10). Failed-command heuristic labels associate successful runs with more Inspect/Adapt and failed runs with more Loop behavior (Table 6, p. 9).

### What the public release establishes

- Exactly 51 metadata/reference/verifier/parser quartets and 51 matching `papers.csv` rows exist.
- Task definitions cover CPU, GPU, QEMU, legacy, multi-language, and external-asset cases.
- Every reference/verifier shell file is syntactically parseable by Bash, and every parser is Python-AST parseable.
- The AdaLoRA, Ward, and SILT task projections are substantive enough to expose real dependency, toolchain, compatibility, and runtime boundaries.
- Most parser surfaces are narrow; contradictory nonzero verifier-exit evidence is accepted by at least the two reconstructed parsers when tested in isolation.
- The closest paper-time and later inspected snapshots have byte-identical task definitions, reducing one narrow release-drift concern.

### What remains unauditable

- whether all 51 reference scripts succeeded on the reported clean image;
- exact source repositories, commits, paper files, and asset snapshots used;
- the 204 trajectories, VM final states, output logs, parser verdict records, and task-level result matrix;
- the global-parser implementation described in the paper if it is distinct from released per-task parsers;
- the 154 diagnostic-agent reports and heuristic mapping outputs;
- model/API snapshot identity, seeds, service failures, retries, missing-run policy, and prices;
- task-level repeats or confidence intervals;
- commands that regenerate Tables 2–7 and Appendix Tables A2–A10.

## Unique insight: completion is a calibrated evidence claim, not a stop action

DeployBench’s most important insight is not simply that agents stop too early. It is that completion judgment requires a traceable comparison between the public assignment, the agent’s self-check, the private instrument, and the permissible downstream claim:

```text
public target basis
→ agent-inferred completion proposition
→ chosen self-check and evidence view
→ self-reported status (success / partial / blocked)
→ independent target execution
→ parser/verdict
→ discrepancy classification
```

The paper collapses distinct discrepancies into “completion-judgment error.” That overstates the evidence:

1. **False success:** 55 self-stops claim `SUCCESS` and fail. This is genuine overclaim evidence, conditional on verifier validity.
2. **Honest partial abstention:** 32 self-stops claim `PARTIAL` and fail. Failure is consistent with the self-report, not a RUNBOOK/verifier mismatch. The paper’s statement that 87/97 self-stops show mismatch incorrectly includes these 32 aligned partial reports.
3. **Hidden-target mismatch:** an agent can run a meaningful smoke test that is weaker or different from the authors’ undisclosed target. AdaLoRA’s toy `loralib` test is inadequate for the verifier, but the public system prompt explicitly requests a simple smoke test and says not to run full paper experiments. This is partly a task-disclosure/projection problem, not pure metacognitive failure.
4. **Blocked stopping:** terminating with `PARTIAL` under a bounded budget can be rational abstention; continuing may waste compute or worsen state. No utility or optimal stopping policy is defined.
5. **Instrument inconsistency:** a parser may ignore its own nonzero verifier-exit marker or observe only nonempty artifacts. Then apparent self-check/verifier disagreement can originate in the evaluator.
6. **Invalid environment/service:** external downloads, GPU drivers, mutable package indices, and verifier-installed dependencies can fail independently of the target capability.

For `skill-bench`, completion should therefore be a typed claim with evidence, not inferred from whether the agent called `finish`. Score at least: self-status calibration, evidence-view sufficiency, substantive endpoint, abstention appropriateness, invalid-environment status, and downstream eligibility. A benchmark can reward honest partial status even when endpoint success is zero, without promoting partial work into task completion.

## Limitations and validity threats

### Construct and task projection

- A lightweight author-written target covers selected dependencies, not the full paper experiment, paper result, scientific conclusion, artifact maintainability, or downstream research use.
- Two entries are GitHub projects rather than paper artifacts, and two papers contribute CPU/GPU variants; the unit is task projection, not always unique paper.
- The public prompt’s “simple smoke test” and hidden designated experiment are not guaranteed to identify the same target. Hidden consequences are fair only when the public basis makes the required boundary inferable.
- Reference setup success proves one witness, not accepted-path completeness. Alternative valid toolchains, newer compatible libraries, different model caches, and equivalent outputs are not systematically tested.
- Compatibility code can alter semantics. Build/run success does not validate behavioral equivalence to the original artifact.

### Sampling and inference

- Feasibility screening excludes broken and unavailable artifacts, producing a healthy-artifact conditional corpus.
- Top venues, public popularity, and artifact badges are convenience/quality filters, not a deployment-demand sampling frame.
- Difficulty is assigned by three author-constructors with no independent labels or agreement. Results are not monotonic for every model; for GPT-5.3-Codex, reported hard performance exceeds medium performance.
- Each model–task cell appears to have one run. There is no stochastic reliability, clustered uncertainty, or variance decomposition across artifact, domain, task variant, model, and service state.
- Comparing four configured packages under one scaffold is descriptive. It does not identify a causal base-model effect.

### Measurement and verifier validity

- The released parsers often reduce rich experiment evidence to fatal-substring absence and nonempty paths.
- Fifty parsers do not inspect the logged verifier exit marker; isolated AdaLoRA and Ward fixtures accept an explicit nonzero marker.
- Fatal-substring lists have false-negative and false-positive risk; generic `OOM`, `Killed`, or `ERROR:` matching is not a typed failure model.
- Six verifiers install/download dependencies or assets, so evaluator action can repair or change the final environment.
- No negative conformance suite, near-valid failure fixtures, alternate-valid setups, parser mutation tests, or independent artifact-author review is released.
- The paper’s “global parser”/“task-specific check” conceptual layers do not map transparently onto the released `verify.sh`/`task_parser.py` layers.

### Completion and diagnosis

- `PARTIAL` plus verifier failure is aligned calibration, yet the paper counts it in the reported 87/97 mismatch.
- Self-stop is a termination mechanism, not a failure cause. It may follow a dependency defect, time judgment, honest abstention, or false confidence.
- “Meaningful check” is author-coded from trajectories, with no released protocol beyond examples, annotator count, agreement, or labels.
- The diagnostic model sees the private reference script, final VM, and verifier logs. Its reports are then mapped with keyword/regex heuristics; there is no human adjudication or diagnostic accuracy study.
- Failure-pattern counts union causes over failed runs at task level and permit multiple labels. They do not establish the earliest causal defect or a unique root cause.
- Recovery labels are deterministic heuristic priorities over next actions. Their outcome association is confounded by model, task difficulty, command count, soft-timeout semantics, and prior failure severity; it is not evidence that Inspect/Adapt interventions cause success.

### Reproducibility and operational realism

- Positive: immutable paper, compact official release, complete task-definition quartets, explicit paper/release timing, syntax-valid files, diverse native stacks, and byte-stable task definitions across the inspected month.
- Negative: inputs and paper result corpus are absent; external artifacts and package indices are mutable; several downloads lack revision/hash pins; VM image and runner are absent; reference scripts contain oracle compatibility code; no full replay command or cost record exists.
- Google Cloud L4/KVM availability and unrestricted native root installation are real infrastructure conditions but not universal laboratory or enterprise environments.
- The model receives root-capable tooling and network access. Filesystem, credential, host-service, and network containment are not documented with executable canaries.
- Tokens and runtime are reported, but API/cloud prices, failed-service costs, verifier cost, human authoring, and diagnostic-review burden are omitted.
- Publishing exact setup and verifier scripts makes the benchmark inspectable but creates direct oracle leakage for future web-enabled evaluations. Public and held-out operations need separate governance.

## Relation to existing evidence

- **PaperBench** begins after much of environment construction and scores dense replication rubrics. DeployBench adds a fresh-machine prerequisite gate; PaperBench shows why passing that gate is not replication completion and why local rubric credit cannot substitute for downstream execution.
- **SciAgentArena** mixes scientific subtasks and dependent pipelines, exposing propagation and configured-system effects. DeployBench isolates a narrower prerequisite but likewise cannot promote a successful projection into scientific autonomy, novelty, or impact.
- **Harness-Bench** demonstrates that workspace setup is not equivalent to an enforced outer sandbox. DeployBench’s clean VMs improve state independence, but absent image/runner/canary evidence still blocks reproducible isolation claims.
- **SciVisAgentBench and artifact-view admissibility** show that native structure, render, execution, and semantic content are distinct witnesses. DeployBench often executes rich targets and then collapses them to sparse filename/log predicates.
- **Task health and validity arguments** already separate reference witness, contrast evidence, instrument defects, bounded claim, and operational role. DeployBench reinforces those contracts; it does not require a new deployment-specific schema.
- **Completion/abstention machinery** should distinguish false success, honest partial status, invalid environment, and budget stop. DeployBench’s self-stop table is direct evidence that endpoint failure alone cannot diagnose calibration.

## Transfer to skill-bench

### Retain

1. Start selected executable-artifact tasks from a genuinely clean, independently attested environment rather than a hand-prepared container.
2. Bind source paper, repository, assets, base image, task projection, reference witness, verifier, parser, and trial state as independently hashed components.
3. Use a bounded native execution target that crosses key dependency layers instead of accepting imports, builds, or self-authored toy checks alone.
4. Preserve generic runtime failures separately from task-specific semantic checks.
5. Include heterogeneous prerequisite structures—legacy compatibility, GPU/toolchain, service, native build, and nested VM—across domains where they test a general hypothesis.
6. Keep agent self-status, self-check command, self-check evidence, independent verdict, and discrepancy reason.

### Repair

1. **Freeze source identity:** record paper version, repository commit/tree, submodules, patch lineage, asset URLs/revisions/hashes, licenses, and valid time.
2. **Separate evaluator mutation:** run verification dependencies in a protected observer environment where possible. If the verifier installs/downloads anything into the target, record that delta and prohibit it from satisfying agent requirements.
3. **Make public basis explicit:** disclose the required experiment family, critical dependencies, and acceptance consequence without revealing private expected outputs. Test whether independent experts infer the hidden target from the public task.
4. **Harden parsers:** require zero execution status; parse schemas and semantic values; validate provenance and freshness; distinguish missing, malformed, stale, partial, and contradictory evidence; use negative and alternate-valid fixtures.
5. **Preserve evidence views:** retain command, exit status, stdout/stderr, native artifact hashes, parsed values, service state, and environment manifest rather than only a terminal Boolean.
6. **Type completion:** score `claimed_success`, `claimed_partial`, `blocked`, `timeout`, `budget_stop`, `service_invalid`, and `harness_invalid` separately. Do not label every failed self-stop a completion-judgment error.
7. **Validate compatibility transformations:** bind every patch to the broken premise, authorized scope, tests, source semantics, and downstream result; a reference patch is not automatic ground truth.
8. **Operate against leakage:** use public development tasks and held-out rotating evaluation projections/assets; log network retrieval and search-time exposure.
9. **Estimate reliability and cost:** repeat selected cells, cluster by source artifact, report invalid/service denominators, and include cloud/API/verifier/human burden.

### Test

A compact cross-domain prerequisite-gate conformance slice should include:

- one executable spreadsheet/notebook or scientific pipeline;
- one stateful service/database workflow;
- one native code/toolchain artifact;
- optionally one nested-VM/system case where justified.

For each, plant: a clean success, nonzero execution after partial artifacts, stale/wrong source commit, missing external asset, evaluator-supplied dependency, semantically wrong but nonempty output, accepted alternate setup, honest partial abstention, false success, and service-invalid run. Assert distinct verdicts and claim ceilings. Compare a disclosed target family with an under-specified “smoke test” condition to quantify how much apparent completion error is caused by task projection rather than agent calibration.

## Concrete repository actions

1. **No new queue task.** Existing benchmark-bundle artifact/check and environment records, artifact-view admissibility, task-health transitions, metric monitoring, validity arguments, execution-isolation evidence, and completion/abstention fields already house these requirements. A DeployBench-specific contract would duplicate completed machinery.
2. Use `data/sources/releases/2606.05238v1-deploybench/release-audit.json` as evidence when the next artifact-verifier conformance work is consolidated: require parser/execution-status consistency, evaluator-delta separation, source identity, semantic output checks, alternate-valid setups, and typed partial/invalid outcomes.
3. Add DeployBench to topic navigation as a release-audited environment-prerequisite case, but defer grouped synthesis changes until a consolidator compares it with PaperBench, SciAgentArena, Harness-Bench, and existing completion/abstention evidence.
4. Keep the release ZIPs ignored and re-fetchable by immutable commit/hash; retain the compact provenance and audit records in Git.

## Bottom line

DeployBench identifies a real missing boundary: consequential knowledge work on executable artifacts cannot begin if the environment is not runnable, and import/build checks are weaker than executing a task-specific path. Its 51 task projections span more infrastructure diversity than most agent benchmarks, and the released scripts make several hard cases inspectable.

The claim boundary is narrower than the paper’s framing. The benchmark measures whether one configured system leaves a VM that passes one author-written, sometimes evaluator-assisted projection. The release cannot reconstruct the evaluated inputs or results, most parsers discard rich runtime evidence, and single attempts provide no reliability estimate. Most importantly, the “completion-judgment” headline mixes 55 false success reports with 32 honest partial reports and with agents following a public instruction to run a simple smoke test while being graded on an undisclosed stronger target.

For `skill-bench`, retain fresh-state execution as a prerequisite gate, but do not confuse it with task completion or professional utility. Preserve the source-to-environment-to-execution-to-evidence chain, fail closed on contradictory verifier evidence, validate alternate paths and compatibility transformations, and measure false confidence, honest abstention, hidden-target mismatch, environment invalidity, and substantive deployment failure as different phenomena.