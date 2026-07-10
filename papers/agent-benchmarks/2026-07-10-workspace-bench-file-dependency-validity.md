# Workspace-Bench 1.0: large-scale file dependencies do not by themselves establish workspace learning

## One-sentence contribution

Workspace-Bench contributes an unusually large, persona-specific file substrate and task-level dependency annotations for agent evaluation, but its evidence supports performance on an authored retrieval-and-artifact suite more strongly than the paper's broader claims about authentic professional work, process-aware dependency reasoning, calibrated difficulty, human capability, or a distinct latent construct called “Workspace Learning.”

## Why this matters

The paper is directly relevant to skill-bench's charter objectives A, B, and C: consequential knowledge work often starts in a persistent, noisy workspace rather than a clean task packet; relevant evidence may be implicit, cross-format, versioned, and dispersed; and success may require preserving existing state while creating or updating multiple artifacts. Workspace-Bench is therefore a useful methodological case, not a proposal to narrow skill-bench to file navigation.

Its most important lesson is a validity boundary: **workspace scale, dependency metadata, and final-artifact rubrics are three different objects**. A large file tree creates a search environment. A dependency graph states an author's theory of relevant evidence. A grader records observations from particular views. None alone proves that the task requires domain judgment, that the graph is complete or uniquely correct, that an agent used the evidence causally, or that the output meets professional standards.

## Research question

The paper asks whether current configured agent systems can complete realistic workspace-grounded tasks by independently discovering, reasoning over, using, and updating explicit and implicit dependencies among heterogeneous files, and whether task difficulty, persona, dependency recognition, harness choice, and cost explain performance differences (paper pp. 1–3, 13–20).

A narrower auditable question is: on a 100-task Lite subset sampled from five simulated workspaces, what fraction of human-authored binary rubric propositions does each model–harness configuration satisfy according to one fixed model judge, and what file nodes/edges can a trace-processing pipeline recover? The paper's data do not identify a single latent “Workspace Learning” capability independently of source retrieval, file parsing, domain reasoning, artifact construction, harness/tool behavior, judge behavior, and task/rubric authorship.

## Sources and reading record

**Paper source read in full**

- Immutable record: https://arxiv.org/abs/2605.03596v4
- Immutable PDF: https://arxiv.org/pdf/2605.03596v4
- Local PDF: `data/papers/pdfs/2605.03596v4-workspace-bench-file-dependency-evaluation.pdf` (30 pages; SHA-256 `d6f5e23fd3ec97e8c293503ac66702dd8ae4c7ae91237c4f6dff25b3e6cc1a18`)
- Local text: `data/papers/text/2605.03596v4-workspace-bench-file-dependency-evaluation.txt` (SHA-256 `2dc939ff32899dda708b74676fc29b989e6f70bd7c70f256d31f7c50be7edb76`)
- Date read: 2026-07-10.

**Official release inspected**

- Repository: https://github.com/OpenDataBox/Workspace-Bench
- Pinned commit: `83689946b4de655df212195ead4f46458e3bc8e6`; local archive `data/sources/releases/2605.03596v4-workspace-bench/OpenDataBox-Workspace-Bench-8368994.zip`.
- Full dataset revision: `3491f9eb611eaf3bd6753048d94e0e049c07ad30`; Lite revision: `60b08b1cc2e8054afbc3ca2160d37876b4f0765c`; workspace revision: `e245d63bfa20cfdb708cd8e78145ffb087155857`.
- Provenance: `data/sources/releases/2605.03596v4-workspace-bench/provenance.json`.
- Release metadata audit: `data/sources/releases/2605.03596v4-workspace-bench/task_lite_clean_en_metadata_table.csv` (100 English Lite tasks, 1,850 rubric rows, 783 dependency edges).
- Targeted task evidence: `data/sources/releases/2605.03596v4-workspace-bench/task-3-trace/` and `task-3-trace-manifest.json` (pinned metadata plus all 37 task-local files; tree SHA-256 `a80656fc31af810c633354c9cf3bbf7ddc4b2b0ff75a44575d5a212dfca71198`).

The official code commit and dataset revisions are dated after arXiv v4. They are **post-v4 release evidence**, not the exact manuscript-time implementation. The full task binaries and multi-gigabyte base workspaces were not mirrored, so this review does not claim a full end-to-end replay.

## Methodology and system

### Workspace construction

The authors choose five internet-company roles—operations manager, logistics manager, product manager, backend developer, and researcher—and define persona profiles with responsibilities, workflows, file-use patterns, and terminology. Agents generate role-conditioned directory trees with controlled noise. A semantic crawler retrieves public artifacts; LLMs generate related emails, notes, and derived documents; domain experts review plausibility, location/content coherence, and whether injected relationships can support tasks (paper pp. 6–7).

This is a **simulated hybrid workspace**, not a de-identified longitudinal snapshot of five real workers. The manuscript begins from 154 scenarios reportedly collected through an internal Lark/ByteDance questionnaire, but does not disclose the questionnaire frame, participant count, consent/redaction process, selection flow, role coverage, or how scenario authenticity survived conversion into generated trees and synthetic content.

### Task and rubric authoring

Domain experts filter questionnaire workflows; 25 role-aligned annotators turn 154 scenarios into 388 tasks. For each task they write an intentionally under-specified request, identify required inputs, produce a reference output, create foundational/procedural/result rubrics, assign capability labels and difficulty, and author a “minimal” file dependency graph. An auxiliary agent rewrites vague criteria into data-grounded assertions, after which experts cross-validate tasks, graphs, outputs, and rubrics (paper pp. 7–8).

The paper does not report annotator qualifications, assignment counts, training, independent duplicate annotation, disagreement, adjudication, inter-rater reliability, rejected-task counts, graph alternatives, or time distributions beyond “>3h” per task and “over 2,500H” overall. “Cross-validation” is a procedure label, not reliability evidence.

### Evaluation system

The paper describes per-task isolated workspace replicas, parallel scheduling, three output-recovery strategies, baseline restoration, and a Seed-2.0-Lite agent judge receiving outputs, original inputs, rubrics, and trajectory (paper pp. 10–12). Metrics are micro-averaged rubric pass rate, thresholded task completion, node/edge F1 against the authored dependency graph, average tokens, and average turns.

The post-v4 release is materially more specific:

- `evaluation/docker/docker-compose.yaml` bind-mounts the entire repository, uses host networking, and sets Codex to `danger-full-access`; this is container packaging, not a demonstrated workspace-only security boundary.
- `agent_runner.py` can copy a standard workspace per case and snapshots changed files, but also recovers expected outputs by basename, declared path, target directory, final response, and a “misplaced outputs” diff. This improves artifact recall while changing strict path-compliance treatment.
- `agent_as_a_judge.py` creates a restricted *judge view* containing task-local `data/` and candidate outputs, but its current rubric prompt does not provide the execution trace. A process rubric therefore may be judged from artifact/input evidence it cannot directly observe. The older `agent_eval.py` path includes only truncated traces and at most ten output files by default.
- The released dependency graph builder in `agent_eval.py` is a deterministic heuristic over recognized read/write/exec events. It carries an `active_inputs` set forward and adds edges to subsequent writes; command tokens containing punctuation are treated as candidate reads. It is not the appendix's model-based trace analyzer, and it does not establish semantic content dependence.
- `filesys_utils.py` restores by path sets and size/mtime differences, whereas the paper says modified nodes are detected by binary hashes. The later isolated-per-case copy path reduces cross-task contamination, but this release behavior cannot be projected backward to v4 results.

These differences make versioned runner, judge, trace normalizer, output collector, and workspace-image identity essential to interpreting any score.

## Evidence and results

### Benchmark composition

The paper reports 388 tasks, 20,476 files, 74 file types, 3,299 directories, 7,399 rubrics, 16 output formats, mean 4.7 required files, mean 5.1 dependency edges, and mean 19.1 rubrics (paper pp. 8–10). Tasks are heavily concentrated in operations and logistics (237/388); roles are not sampled according to an occupational or work-frequency frame.

The pinned post-v4 English Lite table contains 100 tasks: 32 operations, 30 logistics, 17 researcher, 11 backend, and 10 product; 14 easy, 54 medium, and 32 hard. A local parse found 1,850 rubrics: 1,030 `Outcome Evaluation`, 450 `Basic Evaluation`, 339 `Process Evaluation`, and 31 `Result Evaluation`. The label split itself is inconsistent (`Outcome` versus `Result`). It contains 783 graph edges, with 0–100 edges per task, and 1–100 task-local manifest files. Five tasks contain graph filenames not matched by either their released manifest filenames or declared outputs, which is direct post-v4 evidence that graph/manifest conformance needs validation.

The Lite “distribution fidelity” claim is unsupported by a sampling algorithm, target margins, distance statistic, alternate samples, uncertainty, or outcome preservation analysis. Matching a few marginal counts would not preserve joint construct mixture, task-family clusters, rubric severity, file size/modality, dependency topology, or model ranking. The later dataset card repeats the claim but provides no test.

### Configured-system results

Table 4 reports 28 model–harness combinations (four harnesses by seven models), each apparently run once on 100 Lite tasks. The best total rubric pass rate is 61.0% for DeepAgent + GLM-5.1, and task-level pass rates vary sharply with the threshold. No repeated trials, task-clustered confidence intervals, judge uncertainty propagation, missing/invalid-run policy, model-call dates, exact component commits, or multiplicity correction are reported.

The manuscript is internally inconsistent about this experiment:

- the abstract says four harnesses and seven models, average 43.3%, best about 60%;
- the contributions say 15 configurations;
- §5.1 says three harnesses and five models;
- §5.2 says 15 configurations and mean 45.1%;
- Table 4 contains 28 configurations and max 61.0%;
- the conclusion says the best is “nearly 70%”;
- the later full-dataset card says average 47.4% and best 68.7%.

Without an immutable result table and inclusion/missingness manifest, headline averages and rankings are not auditable.

### Difficulty, capability, and dependency claims

The paper defines difficulty three ways: capability composition in §3.3, number of execution steps/collaboration complexity in §4.3, and a separate three-bin dependency-edge density analysis. A decline from easy to hard therefore does not “strongly validate” difficulty: author labels bundle file count, modalities, persona, output complexity, rubric count/severity, dependency structure, and possibly model-facing context. It shows criterion-related ordering for this system sample, not calibrated difficulty or a causal dependency effect.

Node F1 exceeds edge F1, but both compare an extracted trace graph to an author graph. Access is not use; use is not correct interpretation; omission from a trace is not necessarily omission from computation; and a canonical graph need not contain every valid professional path. The later heuristic builder further makes graph scores functions of harness trace schemas and command style. The observed correlation with rubric pass rate cannot isolate “dependency understanding.”

### Human comparison

Twenty “domain experts” receive instructions and workspace files and may use agents, scoring 80.7% (paper pp. 17–18). The paper does not disclose credentials, role matching, task allocation, repeats, time limits, compensation, tools/models, environment parity, output collection, judge identity/blinding, adjudication, or uncertainty. This is a human-plus-unspecified-tools witness condition—not a human ceiling, unaided human baseline, expert parity threshold, or evidence that hard tasks do not challenge humans. Humans and autonomous agents may also differ in GUI access, parsers, search tools, and opportunity to recover from errors.

## Representative task trace: English Lite task 3

The targeted pinned release trace makes the benchmark's strengths and limits concrete.

1. **Request and graph.** Task 3 asks a backend developer to deduplicate project dependencies into `project_dependency_deduplication_list.md`. Its graph contains 37 source-to-output edges: 35 `dependency_item_*.md` files, `package_config.json`, and `project_object_model.xml`, all pointing to the deliverable.
2. **Released files.** All 35 Markdown reports are near-duplicates: each lists the same Java, build, container, security, and recommendation content. `package_config.json` adds five runtime and four development packages. The POM adds Spring starters, MySQL, Lombok, SpringDoc, three JWT artifacts, Commons Lang, tests, and H2. This is cross-format deduplication, but much of the apparent graph breadth is repeated synthetic evidence rather than 37 independent semantic dependencies.
3. **Expected consequence.** Twenty-one rubrics disclose the exact count (43), many exact members, excluded strings, excluded project artifact ID, and Markdown-table convention. Several criteria labeled “Process Evaluation” are actually output-content/source-attribution propositions. A solver can optimize directly against an answer-bearing rubric if metadata is exposed; even without it, the repeated templated files make retrieval largely lexical.
4. **Workspace placement gap.** The released `metadata.json` contains neither `file_system` nor `target_path` entries. The current runner's `_copy_from_manifest` requires `target_path` and skips entries without it; `_resolve_work_dir` falls back from missing `file_system` to `*`. The large base workspace may already contain these files, but because it was not mirrored and task metadata supplies no placement locators, this review cannot verify where the 37 inputs appear in the 20GB workspace or whether an agent must discover them rather than receive task-local injection.
5. **Grader evidence.** The current judge sees task-local inputs and candidate output, plus the exact rubrics; it does not see a trace in the ClaudeCode judge path. It can check membership and formatting, but cannot establish that the agent discovered the intended workspace locations or used every graph edge. No released candidate output or per-rubric judgment accompanies this task in the inspected snapshot, so no actual pass claim is made.

This trace is useful precisely because it separates four claims: files exist; metadata declares a graph; a deliverable can satisfy disclosed propositions; and an execution actually discovered/used those files. Only the first three are represented in the targeted release evidence, and only the first two were directly inspected here.

## Unique insight

Workspace-Bench reveals that **dependency graphs should be treated as contestable authoring hypotheses and measurement instruments, not ground truth about cognition or professional workflow**. They have at least four distinct semantics that the paper partly collapses:

1. **availability graph** — which artifacts exist and where;
2. **relevance graph** — which artifacts can support a requirement;
3. **provenance/derivation graph** — which content or artifact was derived from which source;
4. **observed-use graph** — which reads/writes a configured agent's trace records.

A fifth object—the **causal-use claim** that a source materially affected a decision or output—is not recoverable from path co-occurrence alone. Comparing observed-use edges to a minimal relevance graph can penalize legitimate alternate paths, reward ceremonial reads, and confound harness observability with capability. For skill-bench, graph scoring should therefore be secondary diagnostic evidence, with relation type, authority, valid time, alternative-path sets, evidence-view sufficiency, and adjudication—not a generic capability score.

A second insight is that workspace realism is better expressed as **task-conditional evidence density and distractor structure** than raw file count or gigabytes. If task-local files are injected, repeated templates dominate relevant evidence, or rubrics disclose exact answer atoms, a 20GB background can function mainly as retrieval noise. The construct depends on how relevant, contradictory, obsolete, authoritative, and transform-linked artifacts are distributed and what professional judgment is required after retrieval.

## Limitations and validity threats

### Authenticity, privacy, and provenance

- The workspaces are generated from persona templates, public retrieval, and LLM synthesis. Expert plausibility review does not establish ecological frequency, organizational stakes, or occupational representativeness.
- The manuscript does not document licensing, personal-data review, secrets scanning, redaction, consent, or per-file provenance. Public source retrieval plus generated derivatives creates unresolved license and transformation-lineage questions. The post-v4 code archive's root MIT license even names `WOLF-Bench`, while dataset licenses differ and Lite has no detected license field.
- Five roles in one internet-company framing cannot license broad claims about professional work.

### Task, graph, and rubric validity

- Annotators author tasks, reference outputs, graphs, and rubrics in one pipeline, creating co-design dependence and a canonical-path bias.
- No independent expert alternatives, negative graph edges, graph agreement, admissible path sets, or verifier soundness/completeness tests are reported.
- Binary micro-averaging weights rubric-rich tasks more heavily and treats dependent criteria as independent evidence. Foundational, process, and result criteria are aggregated without validated weights or gates.
- “Intentionally under-specified” tasks risk hidden obligations unless every private consequence has a fair public basis. The paper does not audit this boundary.
- The judge receives source files that the candidate may or may not have accessed, producing evidence-view asymmetry; current release process grading may lack trace evidence entirely.

### Experimental and statistical validity

- One apparent run per task/configuration gives no stochastic reliability.
- Tasks, scenarios, personas, graph families, and rubrics are clustered, but no cluster-aware uncertainty is reported.
- Missing, timeout, API-failure, corrupted-file, and invalid-output handling is not disclosed for paper results.
- Harness/model treatments are not fully pinned, and native tools, context policies, parsers, prompts, and trace schemas differ.
- Cost reports average tokens/turns without wall time, prices, retries, cached tokens, tool costs, output bytes, or uncertainty. Tokens are not comparable across providers without tokenizer/accounting controls.
- Error types come from failed rubric judgments, but no coding protocol, agreement, or evidence-view sufficiency is given.

### Reproducibility and operational realism

The release is substantial—pinned code, metadata, dataset manifests, Docker instructions, per-case workdirs, output manifests, judge records, and task-local data are meaningful progress. Yet exact paper reproduction is not currently demonstrated:

- releases postdate v4 and document file/rubric repairs;
- large workspace archives are mutable external dependencies unless revision/hash pinned locally;
- Docker uses host networking and a repository bind mount with full-access Codex mode;
- the release implementation differs from paper claims about hash rollback, trace-visible judging, and dependency extraction;
- result tables, trajectories, judgments, human artifacts, and human protocol are absent from inspected evidence;
- release metadata contains graph/manifest mismatches and task 3 lacks placement fields required by current injection code.

Operational realism also requires destructive-edit and extraneous-change checks. The runner snapshots and copies changed files for output recovery, then discards/restores workspaces; the rubric set does not systematically score unauthorized edits, deletion of existing evidence, secret access, or workspace integrity. A correct named deliverable can coexist with harmful workspace state.

## Transferable benchmark design lessons

1. **Version the workspace as an instrument.** Record archive/object hashes, file inventory root, permissions, network policy, tool image, task overlays, and cleanup verification separately from the task.
2. **Type dependency relations.** Distinguish contextual support, direct evidence, semantic contradiction, supersession, transformation/lineage, required affordance, observed access, observed write, and claimed causal use.
3. **Support alternative valid paths.** A graph should permit expert-approved equivalence classes and conditional branches; an observed trace should not be forced to copy one canonical graph.
4. **Join requirements to workspace consequences.** Every required/hidden check needs public basis, source authority/scope/valid-time, admissible evidence views, and expected artifact/state consequence.
5. **Grade workspace integrity.** Hash or structurally compare protected files, allowed mutation zones, declared outputs, unauthorized additions/deletions, and sensitive-path access before rollback.
6. **Separate retrieval from judgment.** Report relevant-file discovery, source interpretation, decision quality, artifact correctness, and preservation/safety as separate score families.
7. **Treat Lite as a suite-assembly claim.** Predeclare sampling strata and lineage clusters; compare joint distributions and system rankings with uncertainty and alternate-sample sensitivity; do not infer fidelity from task count or marginal charts.
8. **Calibrate judges by evidence view.** Process criteria require trace/state evidence; structural criteria need authoritative representations; professional-quality criteria need calibrated experts or validated proxies. Missing views should yield `insufficient_evidence`, not a substantive fail.
9. **Use hierarchical estimands.** Macro-average at task or scenario level, retain criterion-family scores, cluster uncertainty by task family/persona, and specify missing/invalid policies.
10. **Preserve human-condition identity.** Record expert role, matching, tools, time, assistance policy, output collection, and adjudication. “Human + tools” is its own configured system.

These requirements already have homes in skill-bench's benchmark bundle, artifact-view admissibility, task projection, task health, metric monitoring, validity arguments, execution-isolation boundary, and pending ECBD cross-record audit.

## Concrete repository actions

1. **Refine the pending ECBD cross-record audit; do not add a duplicate schema.** Its suite-assembly and evidence-view checks should explicitly distinguish availability/relevance/provenance/observed-use graphs, alternative valid paths, and workspace-integrity consequences. Apply the distinction to the LH pilot even though that pilot is much smaller.
2. **Use Workspace-Bench as a future conformance fixture, not a scope commitment.** When a second pilot has a persistent workspace, plant: one authoritative relevant file, one obsolete version, one legitimate alternate source path, one distractor with lexical overlap, one protected file, and one unauthorized-edit case. Verify retrieval, authority/valid-time reasoning, artifact consequence, integrity, and abstention separately.
3. **Require release-level audit fields before importing external scores.** At minimum: immutable workspace hash, overlay placement manifest, task/graph/rubric hashes, runner/judge/trace-normalizer hashes, result inventory, missingness, replicate ID, and evidence-view declarations.
4. **Do not use the paper's 43.3/45.1/47.4 averages, ~60/61/68.7 maxima, human gap, or Lite-fidelity statement as stable comparative facts** until an immutable result inventory resolves the manuscript/release contradictions.

No new queue task is added: action 1 is covered by `build-lh-ecbd-cross-record-audit`; the remaining items are requirements for future diverse-pilot and operating-layer work, not independently justified backlog additions.
