# Agent trajectories as programs: procedural-fingerprint validity and release audit

**Paper:** Hamidah Oderinwale, *Agent trajectories as programs: fingerprinting and programming coding-agent behavior*
**Primary source:** [arXiv:2606.16988v1](https://arxiv.org/abs/2606.16988v1), submitted 2026-06-15
**Official implementation:** [ProcGrep](https://github.com/hamidahoderinwale/procgrep)
**Review status:** deep review of the complete immutable v1 paper plus static and bounded executable audit of the author-owned release
**Date read:** 2026-07-16

## One-sentence contribution

ProcGrep proposes that normalized action sequences can be treated as programs, induces recurring subsequences with byte-pair encoding (BPE), and uses their frequency distributions to compare, attribute, search, and score configured coding-agent traces—but its strongest identification and monitoring claims outrun the released study evidence because model, scaffold, interface, task, and time are not jointly isolated, the reported probe is not reconstructible from the paper-time release, and the public dataset appeared after immutable v1.

## Why this matters for skill-bench

The valuable idea is not “a trajectory is the skill.” It is that an execution record can expose **procedural realization** that an endpoint score misses: repeated reading, edit–test loops, premature submission, recovery after an error, or a scaffold-imposed action grammar. This directly advances charter objectives B and C by supplying candidate diagnostic primitives for benchmark traces.

The crucial validity boundary is equally useful. A fingerprint belongs to a **configured system under an observation and normalization policy**, not automatically to a base model, transferable skill, latent intent, or stable behavioral identity. For knowledge work, the same action sequence can be good or bad depending on evidence state, authority, artifact semantics, and task phase; different action sequences can be functionally equivalent. ProcGrep should therefore inform a secondary diagnostic layer, never replace task evidence, artifact/state grading, or causal validation.

## Research question and claimed answer

The paper asks whether coding-agent trajectories admit compact procedural representations that support comparison and programming. It claims:

1. action traces can be canonicalized across interfaces and compressed into reusable procedural tokens;
2. agents have identifiable “behavioral habits,” with a reported 85.7% attribution accuracy versus an 11.1% random baseline on held-out tasks;
3. pairwise Jensen–Shannon divergence (JSD) captures meaningful model and scaffold similarities, including a teacher/student value of 0.25;
4. procedural representations support deterministic search more accurately and efficiently than LLM search;
5. declarative reward rules can score procedures and potentially support monitoring, routing, and behavioral intervention.

The first and fourth claims are plausible engineering contributions and receive direct demonstrations. The paper supports descriptive separability in the observed corpus. It does **not** yet establish stable model identity, transport to new interfaces or work domains, outcome relevance, causal procedural mechanisms, or monitoring/routing utility.

## Methodology and system

### Representation pipeline

The system maps native events into a small canonical action alphabet such as `read_file`, `search_repo`, `edit`, `create_file`, `run_test`, `submit`, `think`, `error`, and `other`. Canonicalization uses ordered regex/rule families over tool names and event text. This creates a lossy cross-interface view while preserving the native sequence as a second resolution.

BPE then repeatedly merges frequent adjacent tokens. The resulting learned vocabulary contains atomic actions and recurring subsequences. Each trajectory is greedily encoded, and a fingerprint is a normalized distribution over induced procedure tokens. ProcGrep compares pooled fingerprints with JSD, localizes differing procedures, runs nearest-centroid attribution, and provides a declarative query/reward interface.

This is an interpretable sequence-statistics pipeline, not program induction in the stronger semantic sense. Tokens have no preconditions, postconditions, data dependencies, authority, artifact effects, or equivalence semantics. Calling the trace a “program” is productive as an interface metaphor, but the implementation represents an observed token string and its subsequence distribution.

### Empirical corpus and comparisons

The paper draws primarily on software-engineering trajectories associated with SWE-bench-family runs. It describes ten agents spanning model and scaffold combinations, with important heterogeneity: SWE-agent and OpenHands interfaces coexist, while Agentless, Moatless, and DARS impose more deterministic scaffolds. Corpus sizes are imbalanced; several tables and figures use different subsets. The paper reports descriptive action distributions, BPE vocabulary diagnostics, pairwise JSD, attribution probes, scaffold classification, representation comparisons, a distillation comparison, deterministic episodic search, reward scoring, and cost/outcome associations.

The reported BPE stopping rule selects vocabulary size 192 at V-measure 0.644. V-measure is computed against agent labels, not independent procedure-intent annotations. This makes the choice a supervised separability selection even though BPE fitting itself is label-free. It is not an intrinsic proof that the vocabulary has discovered semantically coherent procedures.

### Identification

The paper describes an 85.7% agent-attribution result and calls the examples held-out tasks. The paper-time release contains `case-studies/identification_probe_stratified.py`, which uses shuffled `StratifiedKFold` over trajectory rows. It does not pass task IDs as groups. The script fits `StandardScaler` on all rows before folds, though the scaler is effectively redundant for the displayed normalized frequency vectors. More importantly, the vocabulary and feature space are assembled before cross-validation, and vocabulary size is selected using the same agent labels whose separability is later emphasized.

A second script, `multi_agent_analysis.py`, labels its procedure “leave-one-group-out by agent” and calls `leave_one_group_out(..., label_field="agent")`. The library implementation holds out one label group, trains centroids on all other labels, and therefore cannot predict the unseen held-out agent label; this is not the reported task-held-out identification design. The coexistence of these scripts, without the exact result manifest and input JSONLs, prevents reconstruction of which executable procedure generated 85.7%.

### Search and reward demonstrations

The deterministic search study compares ProcGrep queries over canonicalized traces with LLM answers on authored episodic questions. Exact programmatic matching is naturally strong when the target predicate is expressible in the query language. This validates deterministic retrieval for that predicate class, not general semantic trace search. The paper’s latency and accuracy comparisons are useful engineering evidence but depend on query translation being supplied or correct.

The reward layer maps procedural patterns to weights and aggregates matches. It is auditable and deterministic. Its scores encode authored preferences; they are not empirically calibrated rewards, causal outcome predictors, or evidence that optimizing the score improves task performance without gaming.

## Evidence and release audit

### Evidence actually read

- Local immutable PDF: `data/papers/pdfs/2606.16988v1-agent-trajectories-as-programs.pdf` (SHA-256 `1a34c02d9b3c936f9b98dcfce137b12f3ff9965016b886f8bfa0636cbbfc51f2`).
- Full local text: `data/papers/text/2606.16988v1-agent-trajectories-as-programs.txt` (SHA-256 `2053063a9a722e15179b2505afe1199cf90c8e927a8a291564f69c4e2bdaa162`).
- Release provenance: `data/sources/releases/2606.16988v1-procgrep/provenance.json`.
- Paper-time source: author-owned commit `6b8d61c457e086b1f5f3233fd91b9af231fc0f2e`, preserved as `data/sources/releases/2606.16988v1-procgrep/procgrep-paper-time-6b8d61c.tar.gz`.
- Acquisition-time source: commit `08f72a0d39851aba05bcfbf3396b4001db9486a3`, preserved separately as `data/sources/releases/2606.16988v1-procgrep/procgrep-current-08f72a0d.tar.gz`.
- Bounded reconstruction record: `data/sources/releases/2606.16988v1-procgrep/REVIEW_RELEASE_AUDIT.json`.

Immutable v1 contains no withdrawal notice. The paper-time source is correctly separated from later HEAD. A normalized inventory records 82 added and 3 removed paths by acquisition-time HEAD; direct inspection also found substantive changes to core BPE, canonicalization, JSD, probe, examples, adapters, paper text, and tests. Later functionality must not be back-projected into v1.

### What is released at paper time

The pinned source includes the library, 89 tests, case-study scripts, paper source, derived small JSON tables, and figures. It does **not** include the fingerprint JSONLs expected by the headline analysis scripts, raw trajectories, an administered-run manifest, or a complete command-to-table provenance graph. `docs/paper/data/jsd.json` and related JSON files preserve selected displayed outputs, but not sufficient row-level inputs to recompute the attribution, V-measure sweep, pairwise controls, or uncertainty.

The package lock contains a large development dependency graph. On this host, a clean `uv run --frozen pytest` could not complete because creating the environment exceeded local disk quota. As a bounded fallback, direct host-environment execution of the pinned code passed **60 tests** and skipped 29 CLI/plugin-dependent tests; the skipped group required `pytest-console-scripts`, absent from the host environment. This verifies exercised core canonicalization/BPE/JSD/probe/reward behavior, not the paper’s empirical results. The execution limitation is local and should not be misreported as a code defect; it does show that the paper-time release lacks a small, isolated reproduction target for headline findings.

### Public dataset timing and bounded reconstruction

The official README points to [`midah/procgrep-spines`](https://huggingface.co/datasets/midah/procgrep-spines). The pinned dataset revision audited here is `fb7fe6f9ca67f83b2c790934aa0e9a9f2a803019`; its parquet SHA-256/LFS object is `afb834e12f5a4d258eeaf80b115ca7472f74db3dceb956ff5575a0418ee4b767`. Hugging Face reports the artifact modified on 2026-06-19, four days after immutable v1, so it is a post-paper artifact rather than proof of v1 reproducibility.

The parquet has 220,021 rows and columns `spine`, `dataset`, `trace_id`, `agent`, `reward`, `source_url`, and `source_split`. Its rows are already-derived canonical spines, not raw trace events plus pinned adapter decisions. Coverage is highly uneven: ten of twelve dataset labels expose only one agent string, and each dataset is capped around 20,000 rows. It is useful for stress-testing sequence analysis but cannot reconstruct the paper’s ten-agent SWE-bench corpus or identify every model/scaffold/interface component.

I ran one deliberately bounded, independent comparison rather than relabeling this dataset as the paper corpus. In the `nebius/SWE-agent-trajectories` slice, Llama-8B and Llama-70B shared 125 task IDs. After averaging raw canonical-atom frequencies within each task-agent cell and then macro-averaging tasks, JSD was **0.00222 bits** with a paired task-bootstrap 95% percentile interval of **[0.00165, 0.00388]** (2,000 replicates, seed 20260716). A leave-one-task-out nearest-centroid classifier over these task-level raw-action vectors achieved **66.4%** balanced two-class accuracy (250 predictions; chance 50%).

This result confirms a narrow point: coarse procedural composition retains some model-size-associated signal even when task IDs are held out. It does not reproduce 85.7%, use the paper’s BPE representation, cover its ten systems, or establish a stable model fingerprint. The small JSD alongside above-chance classification also demonstrates that aggregate divergence and attribution answer different questions and should not share an implicit decision threshold.

## Relation to existing skill-bench evidence

ProcGrep fills a descriptive layer but does not supersede the project’s existing trace machinery:

- [STRACE](2026-07-09-strace.md) asks whether observed events support an upstream causal failure diagnosis; ProcGrep measures distributional difference and does not establish root cause.
- [Who&When Pro](2026-07-15-whowhen-pro-failure-attribution-validity.md) uses exact-prefix replay plus injected actions to identify a construction intervention. ProcGrep has no matched intervention, so a discriminative token remains a correlate.
- [Claw-Eval](2026-07-15-claw-eval-multichannel-trajectory-validity.md) separates action-log, final-answer, and environment-state evidence. ProcGrep largely occupies the action-log channel; artifact/state disagreement must remain visible.
- [SkillsBench](2026-07-10-skillsbench-paired-skill-efficacy.md) requires a controlled skill/no-skill treatment. A changed fingerprint cannot identify skill efficacy unless harness, task, and grader are held constant and endpoint effects are measured.
- [AFTER](2026-07-13-after-procedural-memory-transfer-validity.md) makes source→target procedure transport explicit. ProcGrep’s within-corpus distinguishability is not transfer across tasks, work contexts, or solvers.
- [Agent Reliability Profile](2026-07-11-agent-reliability-profile.md) requires repeated outcomes and failure-severity/recovery distributions. One pooled fingerprint or cross-sectional classifier does not establish stochastic or operational reliability.
- [Agentic Confidence Calibration](2026-07-14-agentic-confidence-calibration-validity.md) separates trajectory-derived prediction from a review/escalation decision. ProcGrep likewise needs calibration, thresholds, workload, and loss evidence before monitoring use.
- [Harness-Bench](2026-07-10-harness-bench-execution-isolation.md) explains why launcher, tool, permission, and sandbox identities must be controlled. ProcGrep’s strong scaffold signatures are direct evidence for that requirement.

The resulting claim ladder is: **observed discrimination → repeated procedural stability → matched behavior intervention → endpoint/artifact consequence → skill transfer → cross-domain/interface transport → calibrated monitoring decision utility → production fitness/readiness**. Evidence at one rung does not promote itself to the next.

## Unique insight

ProcGrep’s most important contribution is to make **procedural realization a first-class benchmark observation**. Its most important unintended lesson is that procedural fingerprints are especially sensitive to component identity and measurement policy. The observed signature is better formalized as

> `F(task distribution, model, scaffold, tool interface, adapter, canonicalizer, stopping policy, run seed/time, evidence view)`

than as `F(model)`.

That reframing resolves several apparent tensions:

- near-perfect scaffold identification is evidence that traces expose configured-system plumbing, not necessarily deeper problem-solving style;
- teacher/student similarity may reflect inherited behavior, but common interface, task mixture, decoding, or scaffold can produce the same observation;
- an agent can be readily attributable while its fingerprint has no demonstrated relationship to correctness, recovery, cost, or user value;
- cross-interface normalization can improve comparability while simultaneously erasing consequential distinctions or creating regex-induced equivalences;
- a high-capacity vocabulary selected for agent-label separation can amplify stable nuisance cues.

For skill-bench, fingerprints should be used as **diagnostic candidates and falsification targets**: ask whether a purported skill changes the expected evidence-conditioned procedure while preserving endpoint quality, and whether that change survives task, harness, and adapter controls. Do not score agents for conforming to a canonical trace unless experts have established that the procedure is mandatory rather than merely one successful style.

## Limitations and validity threats

### Construct validity

1. **Sequence is not procedure semantics.** Tokens omit arguments, objects, dataflow, pre/post-state, authority, and effects. `read_file → edit` can represent well-grounded repair or blind modification.
2. **Canonicalization is an observer intervention.** Ordered regexes and broad fallbacks decide what distinctions exist. Adapter error and interface-specific wording are not separately estimated.
3. **BPE frequency is not intent discovery.** Frequent adjacency can encode scaffolding boilerplate, trajectory length, or tool grammar. V-measure against agent labels measures label clustering, not procedure completeness/homogeneity against expert intent.
4. **Bagged token distributions lose order and location.** BPE retains local subsequences, but pooled frequencies discard when, under what evidence, and with what consequence they occurred.

### Internal validity

1. **Model and scaffold are not fully crossed.** Several systems bundle model, harness, interface, and policy. Attribution therefore targets configured rows, not isolated models.
2. **Task-held-out reporting is not release-verifiable.** The available attribution script uses row-stratified folds, while the other leave-one-group script has incompatible label-holdout semantics.
3. **Selection leakage is unresolved.** Vocabulary induction and label-informed vocabulary-size selection occur outside a clearly nested task-grouped evaluation.
4. **Repeated-task and attempt dependence are under-specified.** Confidence intervals and hierarchical uncertainty are absent for most headline comparisons.
5. **Descriptive associations invite causal language.** Distillation similarity, release-period clustering, and reward/outcome patterns lack matched interventions that isolate their proposed mechanisms.

### External and consequence validity

1. Evidence is concentrated in coding-agent action logs. Professional knowledge work includes artifact conventions, source authority, handoffs, clarification, compliance, and non-tool judgment not represented by this alphabet.
2. No temporal retest establishes that a fingerprint is “consistent over time” across version, prompt, task-mixture, or interface shifts.
3. Monitoring, routing, and intervention claims lack prospective thresholds, abstention behavior, error costs, reviewer burden, and outcome studies.
4. Search questions are authored for expressibility in the procedural language; semantic or argument-level retrieval remains different.
5. A procedure reward can be Goodharted. No optimization study tests whether increasing score preserves legitimate alternative methods or improves outcomes.

### Reproducibility and operational realism

The algorithmic library is inspectable and core units are executable. The study is not end-to-end reproducible from the paper-time release because row-level inputs, exact split manifest, generated vocabulary, and table provenance are absent. The post-v1 HF data improves inspectability but is sampled, derived, mutable unless revision-pinned, and not the paper corpus. Operationally, the system offers deterministic and cheap queries after ingestion; however, production use would also require adapter conformance, unknown-action rates, trace completeness, privacy/redaction policy, versioned baselines, drift calibration, and decision-linked false-alarm evaluation.

## Transferable benchmark-design primitives

Retain the following ideas, with stricter semantics:

1. **Multi-resolution trace record:** preserve raw event, native action, canonical action, adapter/rule version, arguments or redacted argument hash, timestamp, evidence locator, and resulting state/artifact observation.
2. **Configured-system fingerprint:** bind model, scaffold, harness, tool schema, permissions, prompt/skill package, canonicalizer, task distribution, run policy, and time window. Never label this field only `agent`.
3. **Observer diagnostics:** report unknown-action mass, canonicalization disagreements, information loss, trace gaps, and sensitivity to rule ordering.
4. **Nested held-out evaluation:** learn vocabulary and tune its size inside training tasks; hold out task families and, separately, interface/harness versions. Compare raw atoms, n-grams, BPE, and semantic/state baselines.
5. **Matched invariance and sensitivity tests:** same model across interfaces/scaffolds should reveal nuisance sensitivity; different models under the same scaffold and matched tasks test model-associated signal; repeated versions/time windows test stability.
6. **Outcome-conditioned procedure analysis:** stratify or match by task and success, then test whether a procedural feature predicts recovery, artifact validity, cost, or severe failure beyond endpoint and length baselines.
7. **Procedure obligation class:** distinguish mandatory safety/compliance sequence, recommended expert heuristic, optional style, and observed correlation. Only the first category is eligible for strict trace conformance scoring without additional evidence.
8. **Decision contract:** any drift alert or router must declare reference population, threshold-selection data, abstention path, false-alert/miss loss, review capacity, severe-defect override, and prospective effect measure.

## Concrete changes and next actions

1. **Use the release-audit record as a calibration fixture.** `REVIEW_RELEASE_AUDIT.json` preserves exact dataset revision/hash, matched-task slice, raw-atom comparison, bootstrap policy, task-held-out classifier, and claim limits. It should not become a benchmark score.
2. **Build one cross-component procedural-invariance matrix, not a new trace schema.** Reuse existing configured-system, trace, artifact-view, execution-validity, and metric machinery. Cross task, model, harness/interface, canonicalizer version, and outcome on at least two unlike work shapes; fit representations only on training groups; report signal and nuisance sensitivity separately.
3. **Require trace-derived criteria to cite authority and effects.** A candidate `run_test after edit` criterion needs an expert/source warrant, applicability predicate, event/state evidence, legitimate alternatives, and demonstrated consequence before becoming a rubric check.
4. **Treat fingerprints as diagnostic evidence.** Add them beside endpoint, artifact, environment-state, and human/expert observations. Do not aggregate JSD or attribution accuracy into a general capability score.
5. **For any future monitoring pilot, pre-register the drift decision.** Pin the configured-system baseline and canonicalizer; use repeated windows, clustered uncertainty, missing-trace handling, a probability-sampled sentinel, and measured review/outcome costs.

## Bottom line

ProcGrep is a useful, inspectable toolkit for deterministic analysis of action-sequence regularities and a strong prompt to evaluate *how* agents work rather than only whether they pass. The paper demonstrates descriptive configured-system separability and programmable trace search. It does not yet demonstrate stable model fingerprints, semantic procedures, transferable skill, causal behavioral inheritance, or decision-valid monitoring/routing. Skill-bench should retain multi-resolution procedural diagnostics while adding component identity, task-grouped nesting, observer calibration, state/artifact semantics, expert authority, outcome controls, and explicit claim ceilings.