# Imaging-101: stagewise scientific evaluation is valuable, but the released instrument exposes its withheld answers and cannot reconstruct the paper's tables

## Why this matters

Imaging-101 contributes a strong benchmark *shape*: 57 paper-grounded computational-imaging tasks across six domains are projected into preprocessing, forward-physics, inverse-solver, and visualization stages; planning, function, and end-to-end tracks observe different failure surfaces; and the paper openly shows that stage agreement and endpoint quality are not equivalent. The source packages contain unusually rich plans and mathematical formulations, and the paper's concrete convention failures—MRI coil normalization, FFT sign/centering, CT weighting, radio-interferometry closure conventions—are exactly the sort of compact expert procedures that `skill-bench` should try to elicit and test.

The empirical instrument does not yet support the paper's strongest interpretations. The paper says function fixtures and ground truth are withheld and every track runs in an isolated sandbox (pp. 4, 20, 32–34), but the pinned release does the opposite:

- function mode copies the entire `evaluation/` directory, including expected-output fixtures, into the agent workspace;
- end-to-end mode copies the entire `data/` directory, while the released data contain `ground_truth.npz` or `baseline_reference.npz` for 55 of 57 tasks;
- Docker mounts the complete task read-only at `/workspace_src`, which the agent's unrestricted shell can read;
- local fallback executes arbitrary shell commands on the host with the real `HOME`, `PATH`, and network boundary unspecified; and
- the Claude Code path places a readable, reversibly obfuscated ground-truth array in `self_eval.py`.

This is not a theoretical leakage concern. On the hydrated `ct_sparse_view` task, directly copying the released ground truth gives NCC 1.0 and NRMSE 0.0. Gaussian-blurring that leaked image without reading the measurement, implementing the forward model, or running an inverse solver still passes both released boundaries through `sigma=1.5` (NCC 0.9639, NRMSE 0.0665 versus boundaries 0.8693 and 0.0755). The endpoint can therefore reward a reference-derived image that supplies no evidence of the scientific pipeline the task is meant to measure.

Release closure is also incomplete. The live repository named in Appendix A is a single paper-time commit with all 57 reference packages, plans, notebooks, a harness, and a 960-asset hash manifest. The pinned Hugging Face revision has all 57 task names, 6,022 paths, large data/fixtures/reference outputs, and partial run artifacts. But **neither release contains any task-level `evaluation/tests/` source**, despite the paper and both READMEs presenting those tests as the function-level oracle. The released result tree contains no planning corpus, only one named end-to-end model tree, and function metadata for 51 tasks with duplicate and zero-test rows. It cannot rebuild the seven-model planning/function/end-to-end matrices, determine the selected run per duplicate task/model, or audit the claimed 1,437 function checks.

The warranted conclusion is narrower and still useful: **Imaging-101 supplies an inspectable 57-task reference-package design and a compelling hypothesis that cross-track disagreement localizes scientific-coding failures. One representative reference pipeline regenerates successfully. The released evaluation, however, does not establish a hidden-reference, reproducible, verifier-auditable comparison, and numerical agreement with one canonical implementation is not independent physical correctness.** It does not yet license expertise-transfer, scientific-correctness, reliability, professional-utility, or readiness claims.

## Source and reading record

### Complete immutable primary source read

- Siyi Chen et al., *Imaging-101: Benchmarking LLM Coding Agents on Scientific Computational Imaging*.
- Immutable record: <https://arxiv.org/abs/2607.10789v1>; PDF: <https://arxiv.org/pdf/2607.10789v1>.
- Local PDF: `data/papers/pdfs/2607.10789v1-imaging-101.pdf` (45 pages; 6,428,208 bytes; SHA-256 `902a26a10d6c964c0d82fc9650f1818e1e1a497dc80482d4adfdb32bd4aee8c1`).
- Local full text: `data/papers/text/2607.10789v1-imaging-101.txt` (266,867 bytes; SHA-256 `cb51365b7fe4eb3ff5a6e79eb84c8e9d69c9ca85e5651190a2f77371b43813de`).
- Local arXiv source: `data/papers/source/2607.10789v1-source.tar` (7,145,137 bytes; SHA-256 `edc5bf993f010101c444e9cd02c407127fe2fecd7440fb8fd6449eb4a2d4efaa`).
- Read through the abstract, Sections 1–5, complete 57-task appendix, task layout, all planning checklists, forward-model and solver tables, prompts, function/end-to-end protocols, all-task result matrix, additional analyses, biographies, and references. The immutable v1 record was submitted 12 July 2026; acquired metadata contains no withdrawal notice.

### Official releases audited

**GitHub paper-time candidate.** Appendix A names <https://github.com/AI4ImagingLab/imaging-101-release> (paper text lines 783–790). The earlier acquisition followed the stale <https://github.com/HeSunPU/imaging-101> URL, which still returns HTTP 404 and remains in the Hugging Face README. The live repository was found by reading the full appendix rather than treating the stale page as definitive.

- Pinned commit: [`48ab1536b2c31607bf7b6df2d6e296670eee436c`](https://github.com/AI4ImagingLab/imaging-101-release/commit/48ab1536b2c31607bf7b6df2d6e296670eee436c), committed 15 June 2026, before arXiv v1.
- Local archive: `data/sources/releases/2607.10789v1-imaging-101/AI4ImagingLab-imaging-101-release-48ab1536b2c3.tar.gz` (SHA-256 `1bc217bdb8f2036119cf3bb7ca5d3d71c6d91ef49c6c6c8d52e75d493bd27ea1`).
- Tree manifest: `data/sources/releases/2607.10789v1-imaging-101/github-tree.txt` (844 entries).
- Repository-level verification: `python -m pytest -q tests` returned **11 passed**. These cover CLI/asset behavior, not task scientific tests.

**Hugging Face data/results release.** Official dataset: <https://huggingface.co/datasets/starpacker52/imaging-101>.

- Pinned revision: [`a9de559b54849a25988a8a0d8a5e869063a5a7a3`](https://huggingface.co/datasets/starpacker52/imaging-101/tree/a9de559b54849a25988a8a0d8a5e869063a5a7a3), dated 14 June 2026, before v1.
- Complete 6,022-path API inventory: `data/sources/releases/2607.10789v1-imaging-101/hf-dataset-api.json`.
- Git tree: `data/sources/releases/2607.10789v1-imaging-101/hf-tree.txt` (SHA-256 `5969b050ba26196fb58030dfb8437b0ff6fc9b98f06b3e75a9878f382f69e90e`).
- Hydrated card and function-result tables: `data/sources/releases/2607.10789v1-imaging-101/hydrated/`.
- Complete audit record: `data/sources/releases/2607.10789v1-imaging-101/release-audit.json`.

The Hugging Face API reports 3.97 GB storage, while the GitHub `assets_manifest.json` identifies 960 benchmark assets totaling 2.19 GB. The larger release also contains 5,049 result paths. I audited all 6,022 names and Git object records, all 844 GitHub tree entries, and hydrated the four metadata tables needed to test result closure. I did not download all 3.97 GB; payload-level execution was targeted to one representative task and the released hash-aware downloader verified every selected asset.

### Representative execution and planted checks

For `ct_sparse_view`:

1. `scripts/download_assets.py --task ct_sparse_view` downloaded and hash-verified eight pinned assets (3,965,104 bytes).
2. A fresh Python 3.13.14 `uv` environment installed the exact released `requirements.txt`.
3. Released `main.py` completed, regenerating FBP and TV-PDHG outputs.
4. Regenerated results were FBP NCC/NRMSE 0.8139/0.1829, TV-PDHG 0.9659/0.0686, and pass boundaries 0.8693/0.0755.
5. No task pytest could be run because the asserted test sources are absent from both releases.
6. Exact-copy, scale, shift, blur, and missing-pipeline probes were evaluated against the released task metrics; details are retained in `release-audit.json`.

No paid model call was made.

## One-sentence contribution

The paper asks whether frontier coding agents can convert a supplied, expert-curated computational-imaging specification and raw measurements into a numerically correct reconstruction pipeline. It deliberately excludes blind paper-to-code reproduction, human–AI collaborative reproduction, and scientific discovery (p. 3, text lines 124–147). That scope discipline is important: this is a configured scientific-coding benchmark, not a claim that agents independently recover methods from literature.

Its distinctive contribution is a three-view evaluation of one projected workflow:

1. **Planning:** does a proposed approach include required preprocessing, a physically consistent forward operator, and a structurally matched inverse solver?
2. **Function:** does generated module code numerically match captured canonical I/O under function-specific tests?
3. **End-to-end:** does a complete reconstruction meet image-quality thresholds?

The useful research question is not simply which model wins. It is whether disagreement among these views distinguishes missing domain procedure, numerical convention drift, local implementation defect, pipeline integration failure, and an alternative endpoint-valid solution.

## Task construction and expert authority

### Selection and coverage

The final set has 57 tasks: medicine 22, astronomy 9, biology 9, physics 6, earth science 6, and chemistry/materials 5 (pp. 3, 12–15). The paper covers seven recurring measurement families and papers from the 1970s through 2020s. This is a meaningful mechanism portfolio; it is not a representative sample of computational-imaging work.

Selection was guided by domain experts to favor long, coupled pipelines, peer-reviewed grounding, and open-source implementations (pp. 3–4). The paper gives **no candidate denominator**, search frame, inclusion/exclusion protocol, rejected-task ledger, code-quality screen, licensing audit, or distribution of exclusion reasons. Every admitted item conditions on public code/data and successful expert/agent reproduction. This selects for unusually executable and benchmarkable methods, not the broader population of consequential imaging work.

The Hugging Face card labels the dataset MIT, and the GitHub root includes MIT text, but task packages embed papers, derived data, pretrained assets, and upstream implementations with heterogeneous origins. A root license does not establish that every redistributed task asset inherits MIT-compatible rights. Per-task source and license lineage is absent.

### Five construction stages

The paper's construction process is substantively good (pp. 3–4):

1. reproduce one paper/upstream visualization or numerical value;
2. canonicalize into fixed modules and normalized data layout;
3. run the canonical pipeline and calibrate endpoint metric boundaries;
4. capture per-function I/O and synthesize tests; and
5. generate and review README, plan, design, and tutorial.

Claude Code assists reproduction, refactoring, test synthesis, and tutorial generation. A domain expert checks against the publication and upstream behavior. One expert constructs each task; another expert in the same area independently verifies it; disagreement is discussed until agreement (paper lines 199–212). Twelve experts cover six areas: nine senior PhD students and three PhD researchers.

That is stronger than calling an author list “expert verified,” but still under-specified. The paper does not publish:

- names or qualifications mapped to domain and task;
- contributor/independent-verifier assignment;
- source spans and upstream commit for each projected requirement;
- initial disagreement counts, types, or resolutions;
- rejected tasks or failed reproductions;
- expert time, compensation, conflicts, or independence from benchmark authorship;
- per-artifact approval records; or
- whether verification checked only agreement with the canonical implementation or alternative scientifically valid realizations.

Discussion-to-consensus produces a final artifact but erases evidence about ambiguity and convention plurality. “Expert verified” therefore means author-team acceptance of a transformed reference package, not independently replicated scientific truth.

## Methodology and measurement

### Planning

The planner sees README and metadata and creates an approach. The architect is separately conditioned on the **reference approach** to create the design (pp. 20–22). An LLM generates a difference report; two experts from the construction pool, blinded to model identity, assign binary pass/fail per preprocessing, forward physics, and inverse solver. Both must pass; disagreement is scored as failure. Overall requires all three dimensions (paper lines 1219–1246).

The published checklists are unusually concrete. They preserve units, transforms, signs, normalizations, masks, solver family, hyperparameters, and load-bearing choices across all 57 tasks (pp. 22–31). This is a high-value authoring artifact.

But the planning labels have no released candidate plans, LLM difference reports, two individual ratings, disagreement table, adjudication record, judge identity/version, or inter-rater reliability. Treating disagreement as failure is conservative scoring, not evidence of reliable labeling. Experts came from the same pool that authored the references, so criterion independence is limited. “Reasonable alternative” is allowed in prose, but no alternative bank or precedent ledger makes that rule reproducible.

### Function level

The function track supplies README, reference approach/design, signature/docstring, and paired test source; all non-target modules are seeded from the reference (pp. 32–34). Agents may take up to ten ReAct turns. Paper Table 1 reports function counts of 461 preprocessing, 567 physics, and 409 solver functions per model, plus module-level all-or-nothing rates.

The intended strength is local diagnosis. The actual construct is **canonical implementation reconstruction with answer-bearing feedback**:

- tests are shown verbatim;
- the prompt explicitly tells the agent to read fixture files to understand inputs and outputs;
- released runner `VISIBLE_PATHS` copies the entire `evaluation/` tree;
- expected-output fixtures are therefore visible in ordinary runs; and
- Docker's full-task mount makes all reference source and fixtures shell-readable anyway.

This contradicts Table 4's statement that fixture expected values are withheld. It also means ten rounds can optimize directly against the exact oracle, so pass rate combines implementation skill, test/fixture inspection, repair policy, and criterion leakage.

Captured canonical I/O is a useful conformance oracle, but not a complete scientific oracle. Tight `rtol` from `1e-10` to `1e-2` can reject sign, phase, axis, normalization, or library-default variants. Some are genuine physical defects; others may be representation-equivalent or alternative valid implementations. Because every task test file is missing, the release does not allow a reviewer to distinguish them, inspect stochastic moment checks, or test soundness/completeness.

### End-to-end

The paper-time method uses a Planner–Critic–Architect–Coder–Judge pipeline with up to five repair rounds, stdout/stderr and metric feedback, and task-specific NCC/NRMSE or custom thresholds (pp. 35–41). The harness retains the best primary metric across rounds (paper line 2650 onward), which makes the reported result a within-run selected maximum rather than the final policy state.

Thresholds are generally `0.9 × reference NCC` and `1.1 × reference NRMSE` (p. 4). This is simple, inspectable, and permissive enough to admit endpoint-valid alternatives. It is not calibrated against expert accept/reject decisions, physical invariants, downstream utility, or decision loss. The paper acknowledges that visually plausible and metric-good outputs can be physically wrong (pp. 8–9, 45).

The released implementation has three additional validity breaks:

1. **Reference leakage:** ground truth is copied as visible `data/` or reachable via `/workspace_src`.
2. **Metric identity drift:** the regenerated task metric defines dynamic-range NRMSE without amplitude normalization, while generic `Scorer` flux-normalizes and uses L2-relative NRMSE. A half-scale exact image has NCC 1.0 but task NRMSE 0.1212 and fails; generic scoring would remove that scale difference.
3. **Interface mismatch:** generic scorer expects `output/reconstruction.npy` and a 2-D `ground_truth.npy`, while the paper describes `output.npz`, task-specific keys, NPZ references, multidimensional outputs, and custom metrics. Most released task assets do not satisfy the generic path.

The released code is thus an inspectable candidate harness, not a demonstrated reconstruction of the paper-time evaluator.

## Evidence and what it actually supports

### Reported results

Across one reported run per model/task in Table 1:

- planning overall ranges from 38.6% to 52.6%; preprocessing is hardest among plan dimensions;
- function module completion ranges from 1.8% to 22.8%, while individual-function rates are much higher;
- end-to-end success ranges from 7.0% to 29.8%; and
- separately administered Claude Code reaches 32/57 (56.1%) under a richer, incomparable environment.

For Claude-4.6-Opus, Table 2 gives a valuable cross-tabulation: end-to-end success is 5/7 when plan and functions both pass, 8/22 when plan passes/functions fail, 1/6 when functions pass/plan fails, and 3/22 when both fail. This directly demonstrates non-equivalence among local conformance and endpoint quality.

The case studies are the paper's strongest evidence:

- NLOS plans omit intensity-to-amplitude/time compensation while producing plausible images;
- Fourier ptychography plans replace qNewton-PIE with generic optimization;
- MRI code omits MVUE coil normalization;
- T2 fitting falsely converges after rejected LM steps;
- CT library defaults alter the projector;
- a wrong black-hole temporal prior passes one benign sequence; and
- sparse-view CT fails canonical modules but repairs to a self-consistent endpoint solver.

These are concrete failure signatures, not generic “reasoning is hard” anecdotes.

### Reliability and uncertainty

The main 57-task matrices appear to be single attempts. No task-clustered confidence intervals, seed policy, repeatability by model/task, sensitivity to model sampling, or paired statistical comparison is reported. One targeted 50-run MRI study finds the same convention error in 47 runs and success in three. That supports instability on one selected task; it does **not** establish that the model “possesses” the knowledge, because no intervention, latent-knowledge probe, or condition showing reliable retrieval is supplied.

Tasks are clustered by modality, codebase, library, authoring team, and repeated conventions. Function observations within a task share prompts, source package, fixtures, and repair history. Treating all functions or all task rows as independent would understate uncertainty.

Cost is absent. The paper reports Kimi hitting a 32,768-token cap on 219 calls and mean completion length 6,002 tokens, but no complete per-model calls, prompt/completion tokens, wall time, compute/GPU, API price, failed setup runs, installation burden, or total evaluation cost. “Reliable assistance” and comparative efficiency remain unmeasured.

### Release reconstruction audit

The GitHub tree has all 57 task directories and, for every task, README, requirements, main, approach, design, preprocessing, physics, solver, and notebook. The Hugging Face task-name set matches exactly. That is meaningful package inspectability.

But the result release does not close the paper's tables:

- **planning:** no released plan outputs, individual expert labels, judge reports, or all-task planning ledger;
- **function:** 1,353 result rows and 413 run summaries cover 51 tasks, nine literal model-name strings, 375 distinct task/model pairs versus 399 nominal seven-model pairs, 35 duplicate task/model summaries, and 229 result rows with zero tests;
- **end-to-end:** only `results/Vendor2_Claude-4.6-opus/` is released; the other six model trees and the exact seven-model matrix builder are absent;
- **selection:** no immutable rule maps duplicate runs to the published row;
- **instrument:** all task pytest source is absent; and
- **configuration:** no exact API endpoint/model revision, decoding parameters, container digest, package lock, hardware/resource receipts, or table-generation script binds a paper row.

The released result timestamps are 7–12 April 2026, while the only GitHub commit is 15 June. Without an earlier harness snapshot or run-level code hash, the current code cannot be assumed to be the exact evaluator that produced those artifacts.

## Unique insight: cross-track disagreement is a diagnostic object, not a hierarchy of truth

Imaging-101's deepest contribution is the empirical demolition of a tempting assumption: passing a more “end-to-end” test does not subsume local scientific validity.

A useful non-inheriting chain is:

`source-faithful requirement → canonical projection → function conformance → pipeline integration → endpoint metric → physical/scientific correctness → expert acceptance → professional consequence`

The paper provides examples in both directions:

- local parity can fail while an alternative self-consistent pipeline reaches a good endpoint;
- local parity can expose a physical convention error that endpoint metrics miss;
- a plan can be wrong for the reference method but adequate for one benign instance;
- a correct plan can fail in implementation; and
- every local stage can look plausible while integration fails.

Therefore, the tracks should not be averaged into one scientific-capability score. Their joint pattern is evidence for a **failure hypothesis**. To claim a cause, the benchmark needs an intervention: replace only the preprocessing rule, swap a convention-equivalent adapter, freeze all other stages, run a harder instance that stresses the missing prior, or compare candidate outputs against independent invariants.

This transfers beyond imaging. Any professional pipeline with spreadsheet transformations, financial assumptions, legal authority checks, laboratory normalization, or data-cleaning conventions can use the same pattern: endpoint utility and local procedure checks are complementary observers with different blind spots.

## Limitations and validity threats

1. **Admission conditioning.** Only successfully reproduced public-code tasks enter; candidate/rejection denominators are absent.
2. **Canonicalization as treatment.** A four-stage template improves comparability but may rewrite the native workflow and omit coupled iteration, calibration, acquisition, or human judgment.
3. **Authored authority.** Two same-pool experts reach consensus, but assignment, independence, disagreement, and approval lineage are not released.
4. **Reference implementation dependence.** Reproduction of one value/image and captured I/O establish canonical agreement, not complete equivalence to paper claims or physical truth.
5. **Missing verifier source.** None of the 57 task pytest suites is released, blocking the core function-level audit.
6. **Criterion leakage.** Visible tests and fixtures turn function evaluation partly into oracle-directed repair.
7. **Ground-truth leakage.** Visible data, full read-only task mounts, and reversible self-eval blobs expose protected references.
8. **No network/host isolation.** Docker and local fallback do not demonstrate the claimed private execution boundary.
9. **One favorable endpoint instance.** Current tasks generally use one data realization; the paper itself proposes 3–5 instances as future work.
10. **Metric inconsistency.** NRMSE definitions and scale handling differ across task and generic harness code.
11. **Alternative-solution ambiguity.** Planning admits reasonable alternatives, function parity can reject them, endpoint metrics can admit physically wrong shortcuts, and no equivalence adjudication joins these states.
12. **Single-attempt comparison.** Main rankings have no repeated-run or clustered uncertainty.
13. **Configured-system confounding.** Results are joint model–prompt–agent–tool–environment–feedback outcomes; Claude Code is correctly reported separately but called an “upper bound” without a common resource envelope.
14. **Incomplete result release.** Published tables and failure percentages cannot be rebuilt.
15. **Contamination analysis is non-causal.** Publication decade is confounded with code length and modality; Codex “re-cleaning” changes 32 to 30 solved tasks without released paired artifacts.
16. **Cost absent.** Reliability per token, time, compute, and human review is unknown.
17. **Rights under-specified.** Root MIT labels do not establish per-task data/code/paper redistribution rights.
18. **Premature tacit-knowledge language.** The paper calls details absent from written specifications “tacit,” while its own README, plans, checklists, code, fixtures, and papers often encode them. Omission from one prompt is not evidence of tacitness.

## Reproducibility and operational realism

The positive operational pattern is worth retaining:

- hash-addressed external assets;
- per-task requirements;
- typed data keys and shapes;
- source, plan, fixtures, and reference output separated conceptually;
- retained function and some end-to-end traces/results;
- a dry-run CLI and asset tests; and
- one representative reference task that executes cleanly from pinned assets.

The release is not execution-valid for comparative agent measurement. Docker resource caps do not make a private sandbox when `/workspace_src` exposes the whole instrument. Read-only protects benchmark files from modification, not from disclosure. A temporary cwd is not an OS sandbox. A readable obfuscated answer is an answer. Package installation and agent shell imply live network unless explicitly denied. Exact model/provider identities and environment digests are absent from retained paper rows.

Useful reproducibility must therefore be typed:

- **package inspectability:** supported for all 57 reference packages;
- **selected asset integrity:** supported by manifest hashes;
- **reference execution:** demonstrated here for one lightweight task;
- **function verifier reconstruction:** unsupported because tests are missing;
- **paper table reconstruction:** unsupported;
- **hidden-reference execution:** contradicted by release inspection;
- **result reliability:** unsupported; and
- **scientific/professional validity:** unsupported.

## Transfer to skill-bench

### Retain

1. **Stage cards with scientific semantics.** Preserve preprocessing, model, decision/solver, artifact, and presentation as domain-adapted stages—not mandatory universal filenames.
2. **Convention cards.** Encode quantity, units, coordinate frame, axis order, sign/phase, normalization, precision, stochastic policy, valid transforms, forbidden shortcuts, diagnostic signature, and consequence.
3. **Cross-track response matrices.** Report plan/procedure, local checks, integration, endpoint, and independent consequence separately.
4. **Dependency isolation as an estimand.** Seed known-good non-target stages only in a declared local-intervention track; do not mistake that for complete-work capability.
5. **Concrete negative cases.** Build tasks where plausible outputs hide missing normalization, stale authority, wrong convention, or benign-instance shortcuts.
6. **Hash-addressed source packs and generated artifacts.** The asset-manifest pattern is reusable.

### Repair

1. **Private-artifact firewall.** Build trial workspaces from an allowlist; never mount or copy the repository, ground truth, fixtures, reference source, or graders into an agent-readable namespace. Deny network unless retrieval is part of the construct. Canary the actual shell and every file tool.
2. **Oracle-feedback typing.** Separate public tests, public examples, non-answer-bearing diagnostics, hidden tests, metric feedback, and answer-bearing expected outputs. Record what was exposed each round.
3. **Equivalence policy.** Before trials, declare accepted sign/phase/scale/axis/coordinate transforms, alternative solvers, tolerances, stochastic estimands, and disqualifying physical violations.
4. **Plural scientific checks.** Pair canonical parity with adjoint/round-trip/metamorphic tests, conservation/dimensional invariants, multiple data instances, adversarial stress cases, and qualified adjudication.
5. **Projection lineage.** Bind each plan/check to paper span, upstream code commit, expert disposition, transformation, disagreement, and scoped authority.
6. **Selection and uncertainty.** Freeze one attempt policy or predeclare replicate selection; publish all attempts, invalid runs, clustered uncertainty, task-family slices, and cost.
7. **Result closure.** Retain exact task/system/harness/environment hashes, outputs, traces, score rows, and table builder.
8. **Noncompensatory claim gates.** Endpoint metric success cannot average away private-reference leakage, physical-invariant failure, or execution invalidity.

### Claim ladder

Use the following non-inheriting states:

`source package exists → source projection reviewed → canonical reference runs → local numerical conformance → declared-equivalence conformance → endpoint quality on frozen instances → independent physical checks → qualified expert acceptance → workflow consequence → professional readiness`

Imaging-101 supports useful evidence near the first four states for its reference packages, but the evaluated-agent rows cannot currently be promoted through the hidden-execution gate.

## Concrete repository changes

1. **Do not add another schema.** Existing `skill-bench` projection, artifact-admissibility, execution-validity, trace, task-health, metric-monitoring, result-reconstruction, and validity-argument machinery already has homes for every requirement above.
2. **Add Imaging-101 as a Tier A mechanism case during the next synthesis pass.** The reusable insight is cross-track non-equivalence and convention-card authoring; the scope is not computational imaging.
3. **Use its planted failures in existing conformance suites.** Specifically test private-reference reachability, fixture visibility, reversible “obfuscation,” metric-identity drift, one-instance shortcut acceptance, and canonical-parity rejection of declared equivalent transforms.
4. **Require evidence-view canaries before any scientific pilot run.** A passed Docker startup or read-only mount is not enough; the evaluated shell must fail to locate source code, fixtures, references, graders, repository paths, host home, and undeclared network.
5. **If the authors later release task tests and complete rows, re-audit rather than rescore retrospectively.** Bind them to a new immutable release and check whether they are paper-time artifacts before reconstructing Table 1.

No new queue task is added: these are direct refinements to existing machinery, and creating an imaging-specific subsystem would duplicate it and narrow the project.

## Claim matrix

| Claim | Evidence status |
|---|---|
| 57 paper-grounded canonical reference packages exist | **Supported** by paper plus matched pinned GitHub/HF task sets |
| Selected assets are hash-addressable | **Supported** by 960-item manifest; representative download verified |
| One lightweight reference pipeline regenerates | **Supported** for `ct_sparse_view` only |
| Every task was independently expert verified | **Author-reported, incompletely auditable** |
| Function tests are deterministic and complete | **Not auditable**; all task test sources absent |
| Fixtures and ground truth were withheld | **Contradicted by pinned release paths and runner behavior** |
| All tracks ran in isolated sandboxes | **Contradicted for private-data isolation; network/host boundaries unsupported** |
| Published seven-model tables are reproducible | **Unsupported**; result/config/table artifacts incomplete |
| Stagewise tracks expose useful failure signatures | **Supported as case evidence and design hypothesis** |
| Function parity establishes physical correctness | **Unsupported** |
| Endpoint NCC/NRMSE establishes pipeline correctness | **Contradicted by paper cases and planted leaked-reference probe** |
| The benchmark measures intrinsic model capability | **Unsupported**; configured system only |
| Convention failure proves inaccessible tacit knowledge | **Unsupported**; omission/defaulting and prompt/interface effects remain alternatives |
| Skill augmentation would improve transfer | **Hypothesis only**; no skill intervention |
| Reliable professional imaging assistance/readiness | **Unsupported** |

## Overall assessment

**Relevance to `skill-bench`: Tier A mechanism evidence, medium empirical confidence, high design value.** Imaging-101 is unusually relevant because it makes hidden scientific conventions, stage dependencies, canonical checks, and endpoint disagreement concrete across six domains. Its best lesson is not that numerical unit tests solve scientific evaluation; it is that no single observer—plan expert, canonical fixture, or image metric—subsumes the others.

The release audit materially lowers confidence in the reported comparative instrument. The missing tests prevent verifier inspection and the visible answers violate the claimed evaluation boundary. Treat the paper as a rich task-authoring and diagnostic case whose exact model rankings remain manuscript-reported—not as validated evidence that one model or harness can autonomously perform reliable computational imaging.
