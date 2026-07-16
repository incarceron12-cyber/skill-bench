# Harness-Induced Belief Divergence: a prompt-mediated self-report study, not yet an agent-harness benchmark

**Reviewed source:** Hikaru Nakamura, *Harness-Induced Belief Divergence*, arXiv:2607.04528v1 (2026), 28 pages.

**Local PDF read:** [`data/papers/pdfs/2607.04528v1-harness-induced-belief-divergence.pdf`](../../data/papers/pdfs/2607.04528v1-harness-induced-belief-divergence.pdf) — SHA-256 `fa3e50735f0a27c100436c4689d5fb07ca449d80ad2b8e91bc68ef914f1c9d10`.

**Full-text extraction read:** [`data/papers/text/2607.04528v1-harness-induced-belief-divergence.txt`](../../data/papers/text/2607.04528v1-harness-induced-belief-divergence.txt) — SHA-256 `a55647bb19c62e05c0fd6ba16e38d65ffe7e1b23a9b90fe60af5b737ec1f4469`.

**arXiv metadata:** [`data/papers/source/2607.04528v1-metadata.xml`](../../data/papers/source/2607.04528v1-metadata.xml).
**Official release audited:** GitHub repository [`Hik289/Harness-induce-bias`](https://github.com/Hik289/Harness-induce-bias), archived at commit `73a4e4df35c6b16220b18efae68bb7f95f56e742`; provenance and archive are under [`data/sources/releases/2607.04528v1-harness-belief-divergence/`](../../data/sources/releases/2607.04528v1-harness-belief-divergence/). The commit was fetched 2026-07-16, after arXiv v1 submission on 2026-07-07; the audit therefore treats it as an official post-v1 implementation, not proof of the exact code state used for v1.

## Why this matters and verdict

The paper asks an important question: can an agent's surrounding harness alter its internal representation of the same task even when task and base model are fixed? Its strongest contribution is **not** evidence that production harnesses cause latent belief divergence during real tool use. It is a useful mechanism probe showing that one model's **structured self-reports change when prompts explicitly describe different observation, blocking, repair, verification, and budget policies**, and that the changes persist over repeated, imagined steps.

That narrower result is credible from the paper's reported design. The broader causal and operational interpretation is not yet identified:

1. The experiment never executes the proposed actions and never observes an environment transition. Every step repeats the original task text plus a harness-authored narrative and the model's prior self-report.
2. Several treatments fabricate the very events whose cognitive effects they report. H3 tells the model that every prior action “succeeded (auto-repaired, 1 retry hidden)” and logs a repair whenever an action exists, without a failure. H4 marks a final verifier as successful unconditionally; H5 deterministically labels checks as skipped or cheap without running them.
3. The measured “belief state” is a constrained verbal report elicited by a detailed schema, not an independently validated latent state. Most outcome-like indicators are later scored against the same model's final self-report or harness-generated flags.
4. The public-benchmark extensions adapt task descriptions from SWE-bench and Terminal-Bench but do not run either benchmark. They therefore test prompt sensitivity on more realistic problem statements, not harness effects on benchmark-solving agents.
5. The official archive contains code sufficient to inspect the mechanism and run small schema/harness tests, but it omits the task data, raw logs, derived tables, and action-analysis scripts needed to reproduce the empirical results. The archive's own smoke suite fails 3 of 7 tests because the eight toy tasks are absent.

**Validity judgment:** useful hypothesis-generating evidence for *prompt-conditioned belief-report divergence*; insufficient evidence for environment-grounded agent belief divergence, behavioral mediation, safety calibration, or outcome-preserving harness equivalence. For `skill-bench`, the paper is most valuable as a warning that harness text, event visibility, and evidence compression are construct-changing interventions that must be versioned and tested—not as a ready metric or benchmark to adopt.

## One-sentence contribution

The paper turns harness-controlled representation, branch visibility, repair compression, verification masking, and evidence retention into explicit experimental treatments and shows that they change one model's schema-constrained task-state reports across imagined multi-step prompts.

## 1. Contribution and research question

The paper introduces the construct **harness-induced belief divergence**: under fixed task, environment, and base model, two harness policies may induce different trajectories over a structured “agent belief state.” It proposes:

- a canonical belief schema containing task progress, uncertainty, risk, constraints, likely failure mode, predicted success, failure-attractor probability, expected repair need, and recommended action;
- six harness views, H0–H5, intended to isolate raw observation, structured observation, risk gating, repair-heavy presentation, selective verification, and cost-aware evidence pruning;
- a scalar `D_belief` and arrival/growth decomposition for comparing final reports across harnesses;
- Belief-Invariant World Model (BIWM) wrappers intended to recover censored, collapsed, masked, or pruned evidence;
- descriptive extensions to SWE-bench Verified and Terminal-Bench descriptions, plus calibration, action-divergence, and failure-attractor analyses.

The research question is well chosen. Agent evaluation often treats the harness as transparent plumbing even though it selects observations, blocks actions, summarizes histories, hides retries, and decides which checks are visible. The paper correctly elevates these choices from implementation details to possible changes in the construct being measured.

## Methodology and system reconstruction

### 2.1 Unit of analysis

The central experiment crosses:

- one base model, reported as `gpt-5.4-mini`;
- eight synthetic code-debugging/task narratives in HIBench-Code v0_toy;
- six harness prompt policies H0–H5;
- horizons `K ∈ {1, 3, 5, 8}`;
- three API seed values, 42–44.

This yields the paper's 576-run Phase-1 grid (`6 × 8 × 4 × 3`). Each run emits `K+1` structured belief reports, steps 0 through K. The release's `scripts/phase1_main.py` implements exactly that grid and pairs each non-H0 final report with H0 for the same task, horizon, and seed.

Later analyses add one-seed long horizons, ten-task Terminal-Bench and SWE-bench slices, grouped task families, BIWM wrappers, and action/self-consistency indicators. These are primarily descriptive. The paper is commendably explicit that its pilot and most extensions are mechanism studies rather than broad population estimates.

### 2.2 What a “rollout” actually does

The release makes the operative intervention much clearer than the abstract terminology. In `core/rollout.py`, every step performs the following:

1. ask the harness to render an observation from the static task object and prior log entries;
2. call the LLM with a system instruction and one user message containing the observation, prior belief report, step number, total horizon, and full output schema;
3. take the model's `recommended_action` string as the candidate action;
4. pass that string through `gate_action`;
5. call harness methods that return synthetic verifier and repair records;
6. append the self-report and harness metadata to history.

There is no shell, repository checkout, test runner, browser, terminal, game, or other task environment. `raw_observation` is the same source text at every step. The selected action is not executed, so there is no action-dependent observation. The paper calls this an “imagined K-step rollout,” but that qualifier does more methodological work than the main framing acknowledges: the system is a recurrent prompt experiment over self-reports, not an agent trajectory through a world.

The prompt also tells the model both `current_step` and `rollout_horizon`. Separate K conditions are therefore not merely longer prefixes of a common process. The model knows from the first call whether the requested trajectory ends at K=1 or K=20, which can directly change its initial and subsequent reports. A K trend mixes repeated conditioning, accumulated self-report, increasing treatment narration, and explicit knowledge of the horizon.

### 2.3 The six treatments

The treatment mechanisms are inspectable and generally match the paper's conceptual taxonomy:

- **H0 raw:** repeats the original task description and, after step 0, the prior recommended action.
- **H1 structured:** adds target state, verifier hint, expected failure modes, risky actions, and structured state labels to the prompt.
- **H2 risk-gated:** adds explicit “risky action blocked” policy text and blocks candidate strings that match a configured risky-action list or destructive keywords.
- **H3 repair-heavy:** announces hidden retries/rollback and collapses every prior action into “succeeded (auto-repaired, 1 retry hidden).” `attempt_repair` returns `occurred=True` whenever a prior action exists, without inspecting `failure_info`.
- **H4 verification-selective:** announces deferred verification. `run_verifier` returns `verified=True` at the configured final horizon regardless of action or task result; the default final-step sentinel is 8 if the caller does not inject `_rollout_horizon`.
- **H5 cost-aware:** truncates the static observation to 200 characters and deterministically labels approximately one-third of steps as receiving a cheap check. No check is executed.

These are effective prompt contrasts, but they are not faithful emulations of production harnesses. H3 and H4 in particular generate groundless positive evidence. The experiment can establish that **telling a model that hidden repair or final verification occurred changes its report**. It cannot establish how hiding *actual* retries or selectively revealing *actual* verifier outcomes changes an acting agent.

### 2.4 Belief representation and distance

The canonical output schema is a practical attempt to turn tacit internal-state hypotheses into auditable fields. It includes:

- four categorical fields (`task_progress`, `uncertainty_level`, `risk_state`, `likely_failure_mode`);
- explicit and inferred constraints;
- three bounded numerical predictions;
- a free-text recommended action.

`D_belief` combines categorical mismatch, failure-mode mismatch, Jaccard distance over constraint strings, numeric absolute differences, and recommended-action mismatch. Version 1.1 decomposes this into an **arrival** term—constraint-set and action mismatch—and a **growth** term—categorical, failure-mode, and numeric mismatch—with fixed 0.30/0.70 weighting.

The decomposition is an honest response to a saturation problem: the paper reports an arrival floor near 0.99 because non-H0 prompts immediately rewrite constraints and recommended action. But that diagnosis also weakens the headline construct. String-set mismatch and action-category mismatch primarily capture what the treatment explicitly inserted into the prompt. Reweighting them away from the K-growth term improves sensitivity to horizon trends, but does not validate the weights or show that the remaining dimensions are latent beliefs rather than treatment-compliant answers.

## 3. Evidence and what it supports

### 3.1 Main descriptive result

The core empirical pattern is large on-arrival divergence between H0 and every non-H0 view, followed by harness-specific growth dynamics. The paper's Table 1 reports near-maximal `D_arrival` across pairs and horizons, while `D_growth` sometimes rises and sometimes falls. The release's descriptive renderer states this plainly: “each non-trivial harness immediately rewrites the constraint set and recommended action at K=1,” and the K signal is carried entirely by `D_growth`.

This supports a narrow result:

> Explicitly changing the policy narrative and evidence presented to a model changes its schema-constrained task-state report, immediately and sometimes cumulatively.

It does **not** support a universal monotonic K-amplification claim. The paper appropriately softens this in later analysis: H1 and H2 show some increasing trajectories; repair-heavy, selective-verification, or cost-aware narratives may stabilize or reverse dimensions. The release even retains an internal note that K amplification is not uniform across harness types.

### 3.2 Public-benchmark extensions

The Terminal-Bench and SWE-bench extensions increase the realism of the *textual task inputs*. The adapters load selected task descriptions, target states, hints, and metadata into the same imagined-rollout object. `scripts/g2_terminal_bench.py` and `scripts/swebench_subset.py` then invoke the same `run_kstep_rollout`; neither launches benchmark containers or evaluates task completion. The source itself labels the SWE-bench run “Imagined rollout … not real docker.”

Consequently, cross-benchmark persistence is evidence that the prompt effect is not unique to eight toy narratives. It is not evidence that harness-induced belief divergence persists during real Terminal-Bench or SWE-bench execution, nor that terminal success is held fixed. “Public benchmark” should be read as **public benchmark task-description sample**, not a benchmark run.

### 3.3 BIWM mitigation

The BIWM family is conceptually useful because it maps distinct information-loss mechanisms to countermeasures:

- canonical schemas for representation differences;
- blocked-action logs for censorship;
- repair unrolling for collapsed retries;
- verification masks;
- shadow evidence for pruning;
- cross-harness aggregation.

But the tests are not independent interventions against external truth. They add or normalize prompt material and then compare the resulting self-report with H0 under the same author-defined distance. A wrapper can reduce `D_belief` partly by steering the output toward the representation favored by the reference harness. “Belief invariance” is therefore operationalized as agreement with H0, not accuracy, decision quality, or calibrated uncertainty. Cross-harness majority alignment compounds this problem: consensus among five treatment-conditioned self-reports need not be closer to the world.

The paper is strongest when BIWM is read as a design vocabulary for preserving provenance and exposing hidden events. Its reported divergence reductions should not yet be treated as evidence that these wrappers improve agents.

### 3.4 Calibration, failure-attractor, repair, and action analyses

The source is admirably candid in `analysis/g4_recompute.py`: there is no environment-grounded outcome, so calibration and AUROC indicators score the step-0 report against the same model's final-step report or against harness flags. A zero self-consistency ECE means the model agrees with itself, not that its success probability is accurate. Repair prediction is especially circular under H3 because the harness marks repair as occurring whenever a previous action exists.

The action result has a similar boundary. The reported action categories are derived from free-text `recommended_action` strings; they are not executed actions. An association between `D_growth` and category mismatch shows that different self-reported states co-occur with different textual recommendations. It does not establish that beliefs mediate behavior, that unsafe retries occur, or that task outcomes change.

The paper reports further grouped action/intervention experiments involving 612 or 840 rollouts, but the archived repository contains no matching action-divergence/UnsafeRetryRate analysis implementation, grouped experiment inputs, or raw outputs. Those numerical claims could not be independently traced from the release.

## Unique insight

The paper's unique and durable insight is a **visibility-state model of harnesses**. A harness does not merely transport model messages. It controls at least five evidence transformations:

1. **representation:** raw versus structured observations;
2. **branch visibility:** which blocked or disallowed actions remain visible;
3. **event compression:** whether failure and repair are collapsed into a net result;
4. **verification visibility:** whether checks and their strength are exposed;
5. **evidence retention:** what is truncated, summarized, or dropped under cost constraints.

These transformations can change a model's stated constraints, uncertainty, risk assessment, and recommendation even when the nominal task is fixed. For benchmark design, that means the harness is part of the treatment and part of the construct definition. A task score without a versioned observation/action/verification protocol cannot support a clean capability claim.

The paper also surfaces a useful distinction between:

- **arrival effects:** immediate construct shifts caused by what the harness reveals or labels; and
- **trajectory effects:** additional divergence caused by repeated interaction and accumulated evidence.

`skill-bench` should preserve this distinction, but ground both terms in real transcript events and independent outcomes rather than prompt-only self-reports.

## Limitations and validity threats

### 5.1 Construct validity: self-report is not demonstrated belief

The model is explicitly instructed to fill a belief ontology. Schema validity proves format compliance, not that fields correspond to stable internal beliefs. The design lacks convergent validation against:

- log probabilities or alternative elicitation formats;
- counterfactual action choices under matched opportunities;
- independent behavioral probes hidden from the belief prompt;
- environment-grounded success/failure and calibration;
- human judgments of whether reported constraints and risks are warranted.

Because treatment text names the intended effects (“be conservative,” “hidden retry,” “key details may be truncated”), demand characteristics are strong. A model can produce the expected report by instruction following without any meaningful internal-state change.

### 5.2 Treatment validity: several harnesses inject invented evidence

H3 fabricates success-after-repair for every prior action. H4 fabricates a successful final verifier. H5 fabricates budget decisions. These implementations test narrative framing, not observation policies over real events. They also make truth-relative analysis impossible: divergence could be appropriate because the prompts describe different worlds, rather than bias under a fixed world.

The paper's premise says task, environment, and model are fixed while harness varies. Operationally, however, H3's world includes alleged hidden failures and retries, H4's includes alleged verifier outcomes, and H2's includes policy blocks. If these events are ungrounded, the prompts are inconsistent accounts of the world. If taken as true, then the information state—not merely presentation—is intentionally different. Either way, “same underlying world” is not experimentally verified.

### 5.3 No action–observation loop or terminal-success control

There is no way to demonstrate “terminal success preserved” because no terminal task is attempted. There is also no exposure to naturally occurring failures, partial progress, tool errors, nondeterministic outputs, or repairs. This removes the phenomenon most important for harness validity: whether two systems receive semantically equivalent, causally grounded evidence after taking comparable actions.

### 5.4 Horizon and repeated-measure confounds

The model sees the requested horizon from the first prompt, and K conditions are separate runs. Longer K therefore changes both the number of self-conditioning cycles and the announced planning horizon. The analysis does not isolate:

- mere repetition of the schema;
- growth in prompt length;
- increasing treatment-label exposure;
- self-anchoring on prior reports;
- announced-horizon effects;
- genuine accumulation of task evidence (which is absent).

API `seed` is sent to the provider, but the release notes that providers may not enforce determinism. Three seed values do not constitute independent models, tasks, or environments; treating repeated generations as independent evidence would overstate sample size.

### 5.5 Metric validity and reference asymmetry

The distance weights are design choices without external validation. Exact-string Jaccard over constraints is sensitive to paraphrase and treatment-inserted labels. Nominal mismatch makes any different failure label maximally distant. The action component depends on categorizing unconstrained free text. The arrival/growth decomposition was introduced after diagnosing saturation, so confirmatory claims based on it need a new preregistered replication.

H0 is treated as the reference, but raw presentation is not established as truthful, complete, or decision-optimal. Lower divergence from H0 is not necessarily better. A structured harness could improve warranted risk recognition and therefore correctly diverge from H0.

### 5.6 Generalization

One model supplies all primary reports. Eight toy tasks, small one-seed public-task samples, and hand-authored harness narratives cannot establish model-, provider-, domain-, or runtime-general effects. The production phenomenon is plausible, but the paper has not estimated it.

## 6. Reproducibility and release audit

### 6.1 What is inspectable

The archived official release contains 51 Python files covering:

- the belief schema and JSON validation;
- LLM calling and logging;
- the imagined-rollout loop;
- H0–H5 render/gate/verifier/repair logic;
- BIWM wrappers and cross-harness alignment;
- metric implementations and specifications;
- Phase-1, long-horizon, Terminal-Bench, SWE-bench, and recomputation scripts;
- seven smoke tests.

All Python files compile under the local audit environment. The implementation is unusually candid in code comments about imagined rollouts, simulated repairs, fake verifier symbols, and self-consistency outcomes. That candor materially improves interpretability.

### 6.2 What is missing

The archive does **not** include:

- `data/hibench_code/v0_toy/tasks.json`;
- Terminal-Bench or SWE-bench adapter data;
- any raw experiment JSONL logs;
- `analysis/phase1_table1.csv` or `analysis/phase1_results.json`;
- the inputs needed by the recomputation scripts;
- the action-divergence and unsafe-retry analysis named in the paper;
- a lockfile or fully pinned environment;
- a license file.

Running the released smoke suite from the archived commit produced **4 passed, 3 failed**. All three failures are `FileNotFoundError` failures caused by the missing eight-task JSON. Compilation passed. The reported 576-run table, BIWM effects, cross-benchmark tables, calibration figures, and grouped action analyses therefore could not be recomputed from the release.

The LLM client supports environment-variable overrides for endpoint and model. Logs identify model/deployment in the rollout record, which is good, but the release does not preserve request IDs, provider snapshot IDs, or raw result artifacts needed to establish that a future rerun uses the same hosted model. API seed support is explicitly best-effort.

### 6.3 Reproducibility grade

- **Concept/mechanism inspectability:** high.
- **Schema and harness unit inspectability:** moderate to high.
- **Paper-number computational reproducibility from release:** low.
- **Hosted-model replicability:** low, due to absent model snapshot and run artifacts.
- **Operational realism:** low; no real executor or benchmark environment.

## Transferable lessons for `skill-bench`

### 7.1 What to retain

1. **Treat the harness as a versioned benchmark component.** Record observation rendering, action filtering, blocked-action visibility, repair policy, verifier schedule, evidence truncation, and retry handling alongside task and grader versions.
2. **Separate arrival from trajectory effects.** Compare systems on the initial evidence packet before interaction, then on divergence induced by actual events over time.
3. **Make hidden-event policy explicit.** Blocked branches, retries, rollbacks, verifier strength, and omitted evidence need provenance-bearing transcript records even when the agent does not see them.
4. **Use matched-world contrasts.** Hold the underlying event ledger fixed, derive alternative harness views from it, and verify that each view is a declared projection rather than an invented world.
5. **Preserve mechanism-specific diagnostics.** Representation, censorship, repair collapse, verification masking, and evidence pruning are different threats and should not be collapsed into one scalar.

### 7.2 What not to adopt

1. Do not call a schema-constrained self-report a latent belief measure without convergent behavioral and outcome validation.
2. Do not use H0 agreement as correctness.
3. Do not treat benchmark task text processed by an LLM as a run of SWE-bench, Terminal-Bench, or another public benchmark.
4. Do not fabricate verifier or repair events to emulate harness behavior in validation experiments.
5. Do not report calibration against a model's later self-report as task calibration.
6. Do not infer behavioral mediation from recommended-action text alone.

### 7.3 Concrete benchmark implications

A `skill-bench` harness-validity probe should begin with a canonical **event ledger** that is independent of every agent-facing view. Each event should have provenance, timestamp/order, action identity, environment observation, verifier identity/strength/result, repair trigger/result, and visibility policy. Alternative harnesses should transform only visibility or representation, with machine-checkable projection rules.

For every matched trial, retain three layers:

- **world truth:** executor and grader events;
- **agent evidence:** exactly what the configured system could observe;
- **agent response:** actions, artifacts, optional elicited state, and timing.

Then evaluate at least four endpoints separately:

1. warranted belief/report change against the event ledger;
2. action change at matched decision opportunities;
3. artifact and task outcome change under independent grading;
4. calibration against environment-grounded outcomes.

The key test is not “did the reports differ?” but “did a declared harness projection omit, distort, or relabel evidence in a way that caused a predictable, consequential error?”

## Concrete repository actions

1. **Build one grounded matched-view harness probe.** Execute a small cross-domain set of deterministic tasks, preserve one canonical event ledger, and replay declared raw/structured/blocked-log/repair-collapsed/verification-masked views. Include a no-op paraphrase control and at least one genuinely consequential hidden event. Measure report, action, artifact, and outcome effects separately.
2. **Add a projection-conformance validator.** It should reject harness views that invent verifier successes, repairs, failures, or world transitions; require every visible item to cite an event-ledger source; and record intentional omissions with authority and reason.
3. **Use belief reports only as secondary diagnostics.** Validate them against hidden behavioral probes and real outcomes before adopting any scalar divergence metric. Pre-register metric weights and analysis after the pilot.

## 9. Charter decision filter

- **Objective advanced:** A (map research on realistic knowledge-work evaluation), B (convert evidence into benchmark-design principles), and C (identify buildable benchmark machinery).
- **Concrete evidence/artifact:** immutable full-paper review plus source-level audit of the official post-v1 archive and an executed smoke/compilation check.
- **Uncertainty clarified:** the paper identifies a real harness-visibility threat, but its evidence supports prompt-conditioned self-report divergence rather than environment-grounded agent belief or behavior divergence.
- **Classification:** expansion plus validation.
- **Duplication/scope check:** complements Harness-Bench execution-isolation work by examining observation/provenance transformations; it does not narrow `skill-bench` to software engineering because the retained primitive—matched world truth, agent evidence, and response—is cross-domain.
- **Useful completion:** a source-grounded validity judgment, reproducibility boundary, and direct specification for a matched-view harness probe rather than a generic summary.

## References

- Nakamura, H. (2026). *Harness-Induced Belief Divergence*. arXiv:2607.04528v1. https://arxiv.org/abs/2607.04528v1
- Official implementation archive: https://github.com/Hik289/Harness-induce-bias/tree/73a4e4df35c6b16220b18efae68bb7f95f56e742
- Related local review: [`2026-07-10-harness-bench-execution-isolation.md`](2026-07-10-harness-bench-execution-isolation.md)
