# Paper Review: Harness-Bench — Execution Isolation and Harness Effects

- **Paper:** https://arxiv.org/abs/2605.27922v1
- **Authors:** Yilun Yao, Xinyu Tan, Chao-Hsuan Liu, Yaoming Li, Zhengyang Wang, Wenhan Yu, Zhewen Tan, Yuxuan Tian, Guangxiang Zhao, Lin Sun, Xiangzheng Zhang, Tong Yang
- **Date read:** 2026-07-10
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, 27 May 2026
- **Local PDF:** `data/papers/pdfs/2605.27922v1-harness-bench-measuring-harness-effects.pdf` (16 pages; SHA-256 `859570aa22270af5203be6042595cce1add19dcef2976db748550462ceb2709e`)
- **Local text:** `data/papers/text/2605.27922v1-harness-bench-measuring-harness-effects.txt` (SHA-256 `325bc529857dcec2faa8aa60b3c8dac89afcb62d37b9710eeefa916b797af3c4`)
- **Official release inspected:** https://github.com/Qihoo360/harness-bench/tree/1025086a446653702b80cfb48babbeec35db6b2c (commit `1025086a446653702b80cfb48babbeec35db6b2c`; tree `49208501704f1d7e2ada03800ac14621f760e1b6`)
- **Release provenance:** `data/sources/releases/2605.27922v1-harnessbench/provenance.json`
- **Release archive:** `data/sources/releases/2605.27922v1-harnessbench/Qihoo360-harness-bench-1025086a.zip` (SHA-256 `2519480acf7050a4d696f68f5ee653101638a231de3fcc3f3e4f133c71f9d2e2`)
- **Important version boundary:** the inspected commit is a “Harness-Bench 2.0” update dated 23 June 2026, after immutable arXiv v1. It is implementation evidence for the later official release, not proof of the exact paper-time code.
- **Tags:** configured-agents, harness-effects, execution-isolation, filesystem-boundaries, workspaces, trace-evaluation, failure-attribution, reproducibility

## One-sentence contribution

Harness-Bench makes the model–harness pairing, rather than the base model, the reporting unit across a full 106-task × 8-model × 6-harness matrix and preserves artifacts, traces, usage, and grader signals, but its evidence establishes **descriptive variation among integrated configurations**, not isolated harness mechanisms—and inspection of the later official runner shows that a directory named “sandbox” is often only a fresh working directory, not an enforced filesystem or network security boundary.

## Why this matters for skill-bench

This paper directly addresses the failure that blocked `skill-bench`'s first genuine LH pilot ablation: changing process `cwd` did not make Hermes file tools task-scoped. Harness-Bench supplies the right high-level lesson—evaluate a complete configured system and inspect execution evidence—but its release also demonstrates why path assignment, isolated state directories, and fresh fixtures are insufficient as an isolation proof.

The central transfer is therefore stricter than “use a sandbox.” A valid trial environment needs an **observed access-boundary contract**: which paths, processes, network destinations, secrets, skills, rubrics, and evaluator artifacts the agent can and cannot reach, plus preflight canaries proving those properties through the actual harness tool interfaces. The inspected release creates a unique workspace and generally isolates `HOME`, but most adapters launch host processes with inherited environment and network access. For Hermes, `cwd=workspace` and an isolated `HOME` do not prevent `../` traversal, absolute-path reads, or access to the repository that contains `ground_truth.json`, `oracle_grade.py`, and `llm_rubric.py`.

This advances charter objectives A and C without narrowing the benchmark to one profession: execution containment and configured-system identity are cross-domain prerequisites for interpreting any artifact-producing knowledge-work trial. The concrete completion criterion is not adoption of Harness-Bench's runner; it is a launcher canary that proves `skill-bench`'s actual agent tools see only the assigned source pack and condition-specific Skill, write only to a unique trial root, and cannot read private graders or repository calibration files.

## Research question and claim boundary

The paper asks: when task environment, nominal budget, timeout, and evaluator are held fixed, how much does performance vary across complete harness configurations paired with the same model backends? It also asks which trace-level symptoms recur when plausible reasoning fails to become verifiable action.

The design supports three bounded claims:

1. Scores under the reported protocol differ substantially among complete model–harness configurations on the fixed 106-task inventory.
2. A base-model label is insufficient provenance for executable-agent performance; the harness, tools, state policy, permissions, and recovery behavior belong in the measured-system identity.
3. Failed trajectories exhibit recurring contract, recovery, evidence, artifact-commitment, and continuation symptoms that final-answer scoring would hide.

It does **not** identify the causal effect of any individual harness mechanism, establish that all harnesses received equivalent effective tool access or time, estimate repeated-run reliability, show that the filesystem/network boundary resisted adversarial or accidental escape, or license professional-capability and deployment-safety claims. The paper itself correctly says the comparisons are configuration-level diagnostics rather than causal decompositions (Sections 1 and 3.1, pp. 2 and 4), but “harness effects” can still be misread causally unless adapter and environment integration are treated as part of each treatment.

## Methodology

### Task construction and validation

The paper reports 106 offline tasks across eight workflow categories: software engineering and codebase maintenance (22), data/BI/finance analytics (14), workspace/tool/multimodal operations (15), knowledge/evidence/retrieval (13), office/business communication (12), vertical professional workflows (12), long-running autonomy/state adaptation (11), and SRE/DevOps/release operations (7) (Figure 2, p. 4). Tasks require final artifacts and include deterministic or rubric-based evaluators. Five representative cards cover spreadsheet/memo production, iterative repair, database migration safety, customer-support routing, and research-claim evidence auditing (Appendix D, pp. 14–16).

Candidate admission uses four author-reviewed criteria: realism, solvability with shipped resources, oracle-checkability, and integrity against hidden-answer access or fixture modification (Section 3.2, pp. 4–5). These are sensible task-health gates, but the paper does not provide the candidate pool, rejection counts, reviewer number or qualifications, review form, inter-reviewer agreement, human baselines, measured completion times, or adversarial integrity-test procedure. “Manually reviewed” is therefore process description, not independently quantified validity evidence.

Inspection of the later official tree found 106 task directories, 106 `task.yaml` files, 106 oracle modules, 90 `ground_truth.json` files, 86 task-specific LLM-rubric modules, and 28 hooks modules. All 106 manifests include `task_id`, title, class, and timeout, but the runner's `TaskSpec` loads only IDs, prompt paths, fixtures, oracle/hooks, timeout, and tags. Category, difficulty, explicit evaluator version, required tools, network policy, budget, integrity policy, and protected paths are not represented in the loaded task contract. The paper's richer conceptual manifest is therefore not fully enforced by the inspected release schema.

### Factorial configuration design

The main experiment is a complete 106 tasks × 8 API backends × 6 configurable harnesses matrix: 5,088 trajectories. The harnesses are OpenClaw, NanoBot, Hermes, ZeroClaw, NullClaw, and Moltis; the model backends are Claude Opus 4.6, Claude Sonnet 4.6, Gemini 3.1 Pro Preview, Qwen 3.6 Plus, GLM 5.1, Kimi K2.5, GPT-5.4, and DeepSeek V4 Flash (Section 4.1 and Appendix B, pp. 6 and 12). Codex with its default GPT-5.4 stack contributes another 106 reference trajectories but is correctly excluded from the configurable factorial, for 5,194 total.

The intended controls are task prompt and fixtures, initial workspace, budget, timeout, evaluator, and minimal required permissions/tools. Native prompting, action format, tool interface, state policy, retry, and recovery behavior vary with harness (Table 1, p. 6). This is a useful ecological comparison of integrated configurations, not a component ablation. It deliberately preserves treatment bundles that may matter in deployment.

There is one reported trajectory per task × model × harness cell. The paper explicitly defines harness dependence as variance over harness-level task averages, **not repeated-run stochastic variance** (Section 4.3, p. 7). It reports no randomization order, endpoint dates, sampling temperature/reasoning effort, retries, failed-launch handling, confidence intervals, paired tests, or cell-level missingness. A full factorial removes allocation imbalance across declared cells, but it does not quantify run noise or operational missingness.

### Setup, workspace, and execution evidence

The paper describes a setup–execution–judge pipeline. The runner renders the task, initializes a fresh offline sandbox from fixtures, runs the native harness under workspace constraints, records model messages, tool calls, workspace changes, and usage, then judges the final workspace and trace. Reference artifacts, hidden answers, and evaluators are said to remain unavailable during execution (Section 3.3, p. 5).

The later official runner does create a unique path with timestamp and UUID, copies only `fixtures/` into `workspace/in` and creates `workspace/out`, writes prompts to the surrounding run directory, and runs the oracle after execution. Harness-specific state and configuration are usually copied under the run directory with `HOME` redirected there. This provides fresh state and helps prevent cross-trial memory contamination.

However, for most adapters “sandbox” is a naming convention, not a kernel-enforced boundary:

- Hermes runs `subprocess.run(..., cwd=ctx.workspace)` with inherited host environment plus an isolated `HOME`; no mount namespace, container, chroot, seccomp, filesystem allowlist, or network restriction appears in the adapter.
- OpenClaw, NanoBot, Moltis, NullClaw, and ZeroClaw are similarly launched as host subprocesses. Some harnesses have their own workspace policies, but those policies differ and the benchmark runner does not independently test or enforce them.
- ZeroClaw's adapter appends the benchmark workspace, the entire run directory, and the harness home to `allowed_roots`; source-config roots may remain because the adapter adds rather than replaces values.
- Codex alone explicitly requests its native `workspace-write` sandbox, so containment technology itself differs by treatment.
- NanoClaw delegates to an external script/container convention, but the inspected adapter does not verify the mount is read/write scoped, the image digest, or network mode.
- The usage proxy routes model traffic for accounting; it is not a general network firewall.

Because the official repository's `tasks/<id>/ground_truth.json`, oracle, and LLM rubric are adjacent to the runner process and host-readable, any harness tool capable of absolute path access or parent traversal can potentially inspect private evaluation material. The task prompt often includes the absolute workspace path, making location discovery easy. Copying only fixtures into the workspace does not protect evaluator files when the process can read outside it.

The release also reveals effective-workspace variation. Hermes uses the benchmark workspace as process `cwd`; OpenClaw and NanoBot configure internal harness workspaces under their isolated homes while relying on the absolute benchmark path in the prompt; Moltis runs from the run directory while pointing a data directory at the benchmark workspace; NullClaw rewrites prompts and relies on its own workspace policy. These are legitimate configuration differences, but they mean a score gap may arise from adapter path plumbing or visibility, not a general property of the named harness.

### Scoring, tracing, and aggregation

Completion uses task-specific deterministic validators where possible and rubric judgment where necessary. Process scoring uses a fixed Claude Sonnet 4.6 judge over reconstructed traces for robustness, tool-use appropriateness, and consistency. Security is binary. The paper defines:

`TaskScore = Security × Completion × mean(Robustness, ToolUse, Consistency)`

and reports components, tokens, and turns separately (Section 3.4, pp. 5–6). Multiplication makes any explicit security violation fatal and prevents high completion from wholly masking poor process. Separate reporting is essential because the aggregate's dimensions are not interchangeable.

The later release complicates interpretation. Its process grader truncates serialized trace payloads at 24,000 characters, grades the incremental/final proxy trace, defaults process to 1.0 when trace extraction or rubric parsing fails, and defaults security to 1.0 when no usable rubric or explicit security key exists. If neither oracle outcome nor quality exists, combined scoring also substitutes an effective outcome of 1.0. These are fail-open operating choices. They may not describe the earlier experiment, but they show that a nominal multiplicative security gate is only as trustworthy as missing-evidence semantics.

The release stores a result JSON containing paths, adapter metadata, usage summary, oracle output, scoring, and traces, and generally retains the final workspace. It does not content-address the final artifact tree in the result, record task/oracle/rubric/harness commits or environment image digests, or support replicate IDs in output naming: a later run of the same task/configuration writes the same `<task_id>.json`. Thus the public code structure supports diagnosis but not an immutable multi-replicate evidence ledger without additional machinery.

## Evidence and results interpretation

Aggregated over all eight backends and 106 tasks, reported harness scores range from 52.4 for OpenClaw to 76.2 for NanoBot, a 23.8-point difference; completion ranges from 60.0 to 81.6 percent. Hermes scores 71.2 with 80.4 completion and uses substantially more reported tokens and turns than NanoBot (Table 2, p. 6). Codex scores 80.4 but is a separate specialized-system reference, not a controlled harness contrast.

These large descriptive gaps are enough to reject base-model-only reporting. They are not sufficient to rank harness engineering quality generally. Harness averages pool eight model interactions and 106 equally weighted tasks; category sizes differ; each cell has one stochastic attempt; native prompts, tools, permissions, context policies, and adapters all vary; and the paper does not provide uncertainty or a per-cell validity audit. The stronger-model/lower-harness-variance pattern in Figure 3 is suggestive, but no inferential model, uncertainty interval, monotonicity test, or correction for bounded mean–variance relationships is given.

Category-level harness variance is highest for data/BI/finance, workspace/tool operations, and software engineering, and lowest for office/business communication (Appendix C, pp. 13–14). This supports a useful hypothesis: harness mediation becomes more visible as work demands structured state manipulation. It does not establish that language-centric professional work is harness-independent, because category composition, task difficulty, grader sensitivity, and sample size all differ.

Among failed trajectories, the paper reports non-exclusive symptoms: contract/format 36.4%, tool/recovery 24.6%, evidence/grounding 14.6%, artifact commitment 11.1%, and state/continuation 9.3% (Table 3, p. 8). The taxonomy is highly relevant to `skill-bench`, but methodology is underspecified. The analysis uses oracle outcomes, process notes, failure notes, and structured fields without explaining who labeled failures, whether labels were human or model-produced, the exact failed-trajectory denominator, label definitions, double-coding, agreement, or adjudication. The rates should therefore be treated as exploratory symptom prevalence, not validated causal attribution.

## Unique insight

The deepest insight is that **environment equivalence is itself an empirical property of each harness adapter, not a consequence of assigning the same workspace path**.

Harness-Bench rightly treats native execution behavior as the intervention. But a benchmark still needs a common outer envelope. If one harness's file tools honor `cwd`, another uses a configured internal workspace, another runs in a native sandbox, and another can traverse the host filesystem, then “same initial sandbox” describes fixture creation—not equivalent observability, authority, or containment. Those differences may be exactly what an ecological system comparison should measure, but the benchmark must distinguish:

1. **Intended harness treatment:** prompts, context policy, action protocol, memory, tool UX, recovery, and native permissions.
2. **Adapter realization:** path rewriting, environment propagation, config copying, process invocation, timeout, and trace extraction.
3. **Outer environment validity:** fixture identity, inaccessible private material, write boundaries, network policy, secret isolation, resource budgets, and clean reset.

Only the first two should vary in a harness comparison; the third must satisfy a shared validity contract or mark the cell invalid. Otherwise, an “effect” can be an evaluator leak, missing input mount, different timeout, credential exposure, or repository escape.

This sharpens the paper's “execution alignment” concept. The paper defines correspondence among reasoning, observations, actions, workspace state, and evaluator conditions (Section 5.2, p. 9). For causal diagnosis, that correspondence must be represented as observable edges, not inferred from the final symptom. A missing artifact after a tool error might originate in tool visibility, feedback delivery, state tracking, recovery policy, path mapping, or evaluator mismatch. “Execution alignment failure” is a valuable family of symptoms; it is not yet a root-cause label.

## Transferable design patterns

### 1. Make the configured system the reporting unit

Preserve separate, immutable identities for model endpoint/date, harness and adapter commit, system/developer prompts, tool schemas, skills, memory/reset policy, permissions, environment image, evaluator, judge, budget, timeout, and feedback policy. Report base-model aggregates only as secondary summaries over declared configurations.

### 2. Require outer-envelope canaries before paid trials

Before calling a model, exercise the **same file, shell, browser, and network interfaces the harness will expose**. The canary should prove:

- fixture and prompt hashes match the assigned task;
- the working directory and resolved output root are unique;
- allowlisted inputs and the condition Skill are readable;
- sibling/parent trial directories, repository files, private rubrics, ground truth, calibration cases, and unrelated Skills are unreadable;
- writes outside the output root fail;
- unauthorized network destinations fail while required model/provider routes work;
- inherited secrets and host environment variables are absent or explicitly allowlisted;
- process/session state is empty at start and attributable at end.

A path printed by `pwd` is not a filesystem-boundary test. Record every probe, expected result, observed result, tool interface, and environment hash; any unexpected access makes `valid_environment=false` before capability scoring.

### 3. Separate adapter conformance from harness performance

Run zero-cost adapter tests for prompt delivery, fixture visibility, output persistence, timeout enforcement, state reset, trace completeness, and error propagation. Adapter failures should not be scored as model capability failures. Conversely, native harness policy failures can remain part of an ecological configuration score if the outer envelope is valid and the claim says so.

### 4. Use fail-closed evidence semantics

Missing traces, missing security judgments, missing oracle outputs, unknown model identity, and inaccessible artifacts must yield `unscorable` or `invalid`, never an effective score of 1. Preserve partial evidence for diagnosis without promoting it into a passing aggregate. Security checks should be deterministic where possible; an LLM trace judgment cannot prove that an unobserved forbidden read did not occur.

### 5. Preserve immutable trial evidence

Hash or archive initial workspace, final workspace, prompt, component versions, environment manifest, trace, usage, validator output, and grader prompt/response. Use unique trial IDs and replicate IDs; never overwrite `<task_id>.json`. Link every score to the exact artifact and grader version that produced it.

### 6. Estimate variability at the correct levels

Repeat matched task × model × harness cells, randomize or block run order, preserve launch failures, and report paired task-level differences with task-clustered uncertainty. Model task, domain, model backend, harness, and interaction effects rather than treating variance among six harness means as run reliability. Report cost and timeout censoring jointly with quality.

### 7. Keep symptom, surface, and root cause distinct

Retain the paper's five symptom families, but link them to evidence-bearing transitions such as:

`tool request → tool observation → state update → recovery decision → artifact write → verification`

A root-cause label requires the earliest supported broken edge and its evidence locator. “Contract/format failure” is a surface if an earlier workspace-path error prevented the correct generator from running.

## Limitations and validity threats

1. **Single-attempt cells provide no run-reliability estimate.** The 5,088 main trajectories exactly equal the factorial cell count. Harness dependence is explicitly cross-harness variance, not stochastic variance.
2. **Complete configurations are bundled treatments.** Prompt, tool interface, state, permissions, recovery, context policy, and adapter implementation vary together. The design cannot identify mechanism-level effects.
3. **Outer-envelope equivalence is asserted, not demonstrated.** The paper reports sandboxing and hidden-answer protection but no adversarial canary results, mount/network policy, or escape audit.
4. **The later official runner is mostly host-process isolation.** Unique directories and redirected `HOME` do not prevent absolute-path reads, parent traversal, process access, or network use. This directly weakens integrity claims if the paper-time runner behaved similarly.
5. **Private grader material can be host-readable.** In the later tree, ground truth, oracle, hooks, and rubrics remain under the same repository from which host subprocesses run; they are outside the copied workspace but not necessarily outside agent reach.
6. **Effective workspace behavior differs by adapter.** Some harnesses use the benchmark workspace as `cwd`, others configure internal workspaces and depend on absolute prompt paths. Integration friction can masquerade as harness quality.
7. **Budget control is under-specified.** The paper says budget and timeout are fixed, but gives no common numerical budget, enforcement algorithm, or overrun handling. The later runner has no typed token/turn/tool budget and allows model-config timeout to override task timeout.
8. **No statistical uncertainty or paired inference is reported.** Large pooled averages can hide task interactions, run noise, endpoint instability, and adapter failures.
9. **Process grading is unvalidated.** Claude Sonnet 4.6 judges all traces, but no rubric prompt, judge repeat, calibration set, human agreement, position/style bias analysis, or uncertainty is reported in the paper.
10. **Security at 100% is not persuasive safety evidence.** Every harness has 100% security in Table 2. Without deterministic event instrumentation and negative controls, this may reflect sparse violations or low detector sensitivity. The later release is explicitly fail-open on absent rubric evidence.
11. **Failure labels lack a reproducible coding protocol.** Label authority, definitions, denominator, agreement, and adjudication are absent. Non-exclusive symptom rates should not be interpreted causally.
12. **Task realism and integrity review are not quantified.** No candidate flow, reviewer credentials, agreement, human baselines, or red-team escape results accompany the four admission criteria.
13. **Task and domain weighting are inventory-dependent.** Equal task weighting and unequal category sizes do not represent a declared distribution of consequential work.
14. **Model and harness versions are insufficiently pinned in the paper.** Display names and qualitative harness labels do not identify commits, provider endpoint snapshots, reasoning settings, tool versions, or adapter hashes.
15. **Offline tasks trade drift resistance for ecological omissions.** They exclude live services, stakeholder feedback, evolving authorization, long-term memory, and irreversible consequences (acknowledged in Section 6, p. 9).
16. **The public release is temporally misaligned.** The inspected commit is a post-v1 2.0 update and contains no result trajectories. Its code can reveal current design properties but cannot independently reproduce or forensically verify the 5,194 reported paper runs.
17. **Artifact quality is mostly reduced to oracle predicates.** Deterministic checks are valuable for contracts and consistency, but they do not establish stakeholder usefulness, professional judgment, clarity, or readiness.
18. **Multiplicative aggregation embeds an unvalidated utility model.** Equal averaging of process dimensions and multiplication with completion/security impose strong compensation and gate assumptions. Separate dimensions are more defensible than the single score.

## Reproducibility and operational realism

At the paper-description level, reproducibility is moderate: the task count, matrix, model and harness names, setup–execution–judge flow, score formula, broad controls, and representative tasks are disclosed. The official release is substantial: 1,087 tracked files, 106 task packages, executable oracles, adapters, hooks, tracing, usage accounting, and a CLI. The offline source packs and deterministic checks reduce live-service drift.

Exact empirical reproduction is currently weak. The immutable v1 paper does not pin harness/adapter commits, provider endpoint dates, environment images, model settings, run order, launch-failure policy, raw results, full judge prompts/responses, or repeated seeds. The inspected official archive postdates v1 and contains no result trajectories. Reproducing all 5,194 calls would also be expensive and historical endpoints may no longer exist.

Operational realism is strongest where tasks require concrete filesystem artifacts, multi-file consistency, tool recovery, and preserved state. It is weakest at the security boundary and professional-validity boundary. Host-process harnesses can be realistic deployment stacks, but then their ambient filesystem/network authority must be measured, not hidden behind the word “sandbox.” Likewise, a passed oracle demonstrates task-package predicates, not that a memo, migration plan, support decision, or evidence audit is professionally acceptable.

## Concrete changes for skill-bench

1. **Refine the active LH launcher gate rather than add another task.** `build-lh-pilot-grader-ablation` already requires the correct zero-cost canary. Expand its acceptance record to cover actual tool-interface reads/writes, parent and absolute paths, private grader denial, condition-Skill visibility, network egress, inherited secrets, unique output root, state reset, and artifact hashes.
2. **Treat canary failure as environment invalidity, not agent failure.** Preserve the attempt and diagnostics, set `valid_environment=false` and `capability_evidence=false`, and prohibit condition-effect estimates until both matched arms pass identical outer-envelope checks.
3. **Use a real isolation substrate for Hermes trials.** A task-scoped container/mount namespace or equivalent allowlist must expose the source pack read-only and output root read/write while excluding the repository and other profiles. `cwd`, prompt wording, and `HOME` redirection are not sufficient.
4. **Pin the adapter as an independent component.** Record launcher/adapter hash separately from Hermes version and model. Path rewriting, environment filtering, and trace capture are part of trial provenance and potential root causes.
5. **Make missing evidence fail closed.** A missing trace, unknown component version, absent artifact, or unexecuted security probe should produce `unscorable`, never a default-perfect process/security/outcome component.
6. **Preserve a transition-level trace.** Map request, observation, recovery, write, and verification edges to the existing error→feedback→repair→verification contract. Use Harness-Bench's symptom taxonomy only as surface labels until an earliest supported cause is located.
7. **Do not import the aggregate score.** Keep completion predicates, process diagnosis, security/compliance, artifact quality, cost, and expert readiness separate as required by the charter. Harness-Bench supports configured-system provenance and execution diagnosis, not professional-validity aggregation.
8. **When the pilot expands, add matched repeats and task-clustered uncertainty.** One run per arm can demonstrate plumbing but cannot estimate reliability. Preserve all launch and timeout outcomes under a frozen selection policy.
9. **Carry environment-validity evidence into the pending validity argument.** A narrow task-completion or Skill-effect claim requires valid and comparable environments; professional capability and deployment readiness remain separately blocked.
10. **Add no new queue item.** These are nonduplicate acceptance criteria for `build-lh-pilot-grader-ablation` and refinements for existing configured-system, trace, and validity contracts.

## Action items for repository

- [x] Read the complete immutable v1 PDF/text and verify task, matrix, scoring, result, limitation, and appendix claims with page/section evidence.
- [x] Inspect the complete official 1,087-file release at pinned commit `1025086a446653702b80cfb48babbeec35db6b2c` and preserve its archive/provenance.
- [x] Keep paper claims separate from observations about the post-paper Harness-Bench 2.0 release.
- [x] Distinguish intended harness treatment, adapter realization, and outer-environment validity.
- [x] Map isolation-canary and fail-closed evidence requirements to `build-lh-pilot-grader-ablation`.
- [x] Add no duplicate build task; the active launcher continuation already owns useful completion.
