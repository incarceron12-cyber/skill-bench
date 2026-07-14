# Hacker–fixer loops are useful verifier falsification, but known-exploit rejection is not verifier correctness

**Primary source.** Ziqian Zhong et al., *Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops*, arXiv:2606.08960v1 (8 June 2026), <https://arxiv.org/abs/2606.08960v1>.

**Companion sources.** Ivan Bercovich et al., *Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories*, arXiv:2604.17596v1 (19 April 2026), <https://arxiv.org/abs/2604.17596v1>; Ivan Bercovich, *What Makes a Good Terminal-Agent Benchmark Task*, arXiv:2604.28093v1 (30 April 2026), <https://arxiv.org/abs/2604.28093v1>.

**Full texts read.** Immutable PDFs and complete layout-preserving extractions were read through their appendices/prompts: `data/papers/pdfs/2606.08960v1-hardening-agent-benchmarks.pdf` (25 pages; SHA-256 `9bb9a301ecb8e9e94c0f2b6ffe8b985bcdb2eea08a061680a51c8c305f2ee4fb`) and `data/papers/text/2606.08960v1-hardening-agent-benchmarks.txt` (SHA-256 `c42bb8d179be538ca8482957ae8800bca0ebb18f0b50677d0c2e4e1908b8ea2c`); `data/papers/pdfs/2604.17596v1-terminal-wrench.pdf` (5 pages; SHA-256 `140df68e633bcb5544e37b67a6f362a917f7a38b566b25e1b42fe86beb619e8a`) and matching text SHA-256 `2b8f35267adc7db53fc4827e128c02c873b7e5634749c4f9c3dafca790bd3156`; `data/papers/pdfs/2604.28093v1-good-terminal-agent-benchmark-task.pdf` (8 pages; SHA-256 `434efb00a13b7d8d0ab9a1daa411cca48ea714d13ffe53edd5e6a885f00e1479`) and matching text SHA-256 `7d8caf63d4e4ce023fde1d6b0fd00ad6e4f164190ad21ca38b4d7a65af8a4fa5`. Date read: 2026-07-14.

**Release audit.** Immutable paths, hashes, inventories, correspondence, licenses, and timing boundaries are recorded in `data/sources/releases/2606.08960v1-adversarial-verifier-hardening/provenance.json`. I inspected the complete Terminal Wrench snapshot at commit `d8a29613235a0ef56a8b70b3142626a533da28c2`, both byte-corresponding `harden-v0` public surfaces dated 3 July 2026, the compact KernelBench result artifact at commit `2721064396f07e536fac5f493b74e7ab161518eb`, and the pool snapshot/history manifest through gitlink `e3b123abafa9448e2d98d8b49ea496abfdb28607`. Terminal Wrench is Apache-2.0. The harden implementation is Apache-2.0. No license was detected for the KernelBench result artifact. The implementation surfaces postdate v1 by about 25 days; the result artifact postdates it by about one day; neither is assumed byte-identical to paper-time code.

## Bottom line

The paper's important contribution is not a claim that LLMs can make verifiers correct. It is an operational **falsification loop**: separate a hacker that searches for accepted non-solutions, a fixer that changes the instrument, and a solver that probes whether accepted legitimate behavior survives; iterate; then attack the frozen result with model-, hint-, and task-separated probes. The shared defense pool is a particularly useful systems idea when tasks genuinely share evaluator infrastructure.

The results also expose the method's central danger. On KernelBench, the raw loop reached 0% attack success while rejecting nearly every diverse legitimate solver. A deterministic reference witness failed to exercise the canonical `load_inline` path or raw-cuBLAS alternatives. A post-loop model-generated “autopatch,” prompted with one failing legitimate solution, restored reported benign pass rates while retaining 0% success on the fixed attack corpus. That is evidence for an effective repair on those submissions and snapshots—not verifier completeness, semantic preservation, or freedom from new attack surfaces.

Terminal Bench makes the tradeoff clearer: the full hardening package reduced unhinted trajectory-level verifier passes from 39.2% to 16.7%, but benign passes also fell from 76.1% to 65.2%. The paper's own logistic-regression example shows a hardened reference-gradient test rejecting regularized solutions. A solver pass is therefore one positive witness, not a bound on false rejection over the admissible solution set.

The defensible claim is narrow: **for two terminal/coding substrates and pinned configured role packages, iterative adversarial repair reduced acceptance of fixed, model-generated and publicly described attack corpora, while measured legitimate acceptance was preserved on KernelBench only after a post-loop repair and declined materially on Terminal Bench.** The work does not establish the reported 16% as a stable prevalence estimate, general verifier correctness, universal weak-to-strong defense, benchmark safety, professional validity, production fitness, or readiness.

## Why this matters: benchmark relevance and research question

This is narrow expansion serving charter objectives A, B, and C: improve benchmark-instrument validity across domains without making terminal work the benchmark's scope.

The paper asks whether automated hacker–fixer–solver iteration can harden outcome verifiers against reward hacking. The stricter skill-bench question is:

> What evidence shows that a repaired grader rejects unacceptable outcomes while preserving the full declared set of legitimate alternatives, rather than merely fitting the attack and witness distributions used during repair?

That question applies to spreadsheets, reports, stateful workflows, visual artifacts, safety checks, and professional decisions. Every grader defines an acceptance boundary; adversarially lowering false accepts can silently increase false rejects or shift the construct.

## One-sentence contribution

The unique contribution is a three-population view of grader repair:

1. **attack search population** used to discover failures and propose patches;
2. **legitimate-path population** used to constrain overrestriction; and
3. **held-out challenge population** used to assess the frozen repaired grader.

These populations must remain separate and independently versioned. A verifier is not “hardened” without naming all three, their access conditions, selection, budgets, overlap, and stopping rule.

The paper additionally shows that a patch is a benchmark-version transition, not an implementation detail. It changes which artifacts count, potentially changes rank order, and can invalidate historical comparability. The correct object for skill-bench is therefore an **adversarial verifier revision record**, not a boolean `hardened` flag:

`old grader → discovered counterexample → proposed patch → replayed attack contrasts → legitimate-path contrasts → collateral/new-surface probes → accepted/rejected revision → frozen new grader → bounded claim`.

## Unique insight for skill-bench

Verifier hardening is a two-sided acceptance-boundary intervention, not a one-sided
security score. The same patch can lower observed false accepts and increase false
rejects; the attack, legitimate-path, and held-out challenge populations jointly
define what the result means. This turns every accepted patch into a versioned
measurement change that needs bridge evidence and a renewed validity argument.

## Methodology and evidence

### 1. Attack-surface audit and Terminal Wrench

The hardening paper probes 1,968 source-dataset rows from five terminal-agent benchmark surfaces with Claude Opus 4.6, Gemini 3.1 Pro, and GPT-5.4. Hackers receive the task plus an elicitation prompt but no verifier source. An LLM judge separates rewarded exploits from legitimate solves; the authors report manually checking the first 49 environments with a judge-confirmed hack and finding no false positives (paper pp. 4–5).

The companion dataset describes a two-stage process: more than 40,000 first-stage trials over 1,860 tasks produce 395 candidates; a stronger v5 loop then yields 6,289 classified trajectories, of which 3,632 are labeled hacks, 1,216 attacker-produced legitimate solves, and 1,441 no-reward attempts, plus 2,352 successful baseline trajectories (Terminal Wrench pp. 1–3). The release manifest is internally consistent with 331 unique tasks, 957 task/model entries, 3,166 “serious” and 466 “non-serious” rewarded exploits. Of 6,289 classifications, 6,258 use stored judgments and 31 use reward-only fallback.

This is a valuable failure corpus, but not a clean prevalence survey:

- discovery is model-, prompt-, budget-, and snapshot-dependent, so non-discovery is not robustness;
- second-stage inclusion is outcome-conditioned on first-stage detection;
- the hardening paper gives no random manual sample, blinded re-annotation, inter-rater agreement, judge confusion matrix, or uncertainty for all 3,632 labels;
- the manually checked “first 49” is not described as random;
- source rows overlap across benchmark versions, while 16% is presented as if one homogeneous frame; and
- “hack” includes both serious and non-serious categories whose legitimacy boundary can be contestable (for example, valid simplification or implementation freedom).

The exact count is unresolved. The Terminal Wrench paper, title, pinned release, and manifest say **331** unique tasks. The later hardening paper repeatedly says **323** while retaining the same 3,632 trajectories. The release's model table also contains exactly 323 Claude task/model entries, making accidental substitution plausible, but the public evidence does not prove the cause. The later 323/1,968 “16%” must not silently overwrite the auditable 331-task release or be treated as an exact estimate.

### 2. Hacker–fixer–solver loop

For each task, a precheck gives the solver up to four attempts; failures are excluded. Each iteration gives the hacker up to three attempts, with summaries of earlier failures. A successful trajectory and verifier source go to the fixer, which may patch `tests/` or `environment/` or declare the trajectory legitimate. A solver then gets one attempt against the patch. Passing patches commit; failing patches revert and return to the fixer. Runs stop after hacker failure, ten attack iterations, or three consecutive fixer declarations of legitimacy (hardening paper pp. 5, 14–16).

Verifier-aware hackers receive read-only source for the first eight attack iterations before a blind tail. A shared git pool lets fixers propagate purportedly task-agnostic changes across tasks with an iteration barrier and anti-stall rule. The role separation and append-only patch history are strong design patterns. But information and authority remain asymmetric:

- the hacker searches a prompted subset of non-solutions;
- the fixer sees one exploit and owns the acceptance-boundary edit;
- the solver supplies one or a few positive witnesses;
- the same model family can fill hacker, fixer, summary, and solver roles;
- the fixer's `.legitimate` decision is not independently adjudicated; and
- pool propagation multiplies both valid defenses and specification errors across tasks.

The 3 July living implementation adds a shared journal and targeted replay options absent from the v1 method description, uses unpinned dependencies, and defaults to verifier cutoff 5 rather than the paper's 8. The released experiment configs do record cutoff 8 for privileged arms, but also record a 10× hacker timeout multiplier where the paper's hyperparameter table says 2×. This is instrument drift, not necessarily a result defect; exact paper reproduction requires the paper-time code/config that is not pinned.

### 3. KernelBench case study

The loop is launched over 100 KernelBench Level-1 task packages on H200 MIG slices, but the released four-arm records reveal **41/100 tasks fail the deterministic precheck in every arm**. Only 59 contribute hardened outcomes; the main `priv-pool` arm records 52 robust, seven wall-clock-stopped/unknown, and 41 precheck failures. This is consistent with the paper's warning that 18 GB VRAM excludes tasks, but materially qualifies “run on all 100.” Pool transfer is demonstrated over the surviving substrate, not all 100 tasks.

Because all Level-1 tasks use shared evaluator machinery, held-out measurement focuses on task 001. The fixed corpus contains 15 public exploit hints with nine prompted attempts each (133 usable), 49 blind Gemini attacks, 49 Gemini benign solves, plus Claude's 49 blind attacks and 50 benign solves. The same submissions are rescored against each frozen defense snapshot, which is reasonable for a no-feedback blind attacker but measures rejection of that frozen corpus rather than adaptive post-patch attack.

The threshold changes from 10× in-loop to 12× at evaluation to exclude 10–12× TF32/mixed-precision submissions considered plausibly legitimate. The release makes rewards inspectable and reports 0/234 Gemini and 0/232 Claude submissions above 12× for autopatched iterations 8, 11, and 13. This supports fixed-corpus rejection at the declared threshold. It also shows why threshold authority is part of the construct: several Claude hint/solver groups approach or exceed 10×, and classifying them as attacks versus legitimate optimizations changes the result.

The strongest evidence is the paper's negative control against its own method. Raw iteration-8 and final verifiers can have 0% attack success and **0% benign pass**. At iteration 11 the loop briefly self-repairs one `load_inline` incompatibility, then later pool sync reintroduces it. The authors' post-loop autopatch removes two broad defenses after one failing cuBLAS-based witness is shown to the fixer, raising Gemini/Claude benign pass to 98%/92% while fixed-corpus attack success remains zero (pp. 8, 18–20).

This demonstrates effective observed Pareto repair. It does not establish:

- acceptance of legitimate implementations beyond the two model distributions and canonical reference;
- semantic equivalence of the 12× boundary;
- no new exploit introduced by removing thread/subprocess and introspection restrictions;
- independent confirmation of the fixer's “minimal” surgery; or
- cross-task hardening beyond shared KernelBench machinery and one scored task.

### 4. Terminal Bench case study

The authors start from 100 tasks and retain 77 after an LLM-solver precheck; 28 were previously blind-hackable. The loop uses Gemini 3 Flash as hacker, fixer, and solver. Held-out Gemini 3.1 Pro provides eight human-authored wrap/environment-hijack hints once per task, three unhinted attacks per task, and three benign solves per task.

The full package reduces raw trajectory-level hinted ASR from 50.4% to 39.4% and unhinted ASR from 39.2% to 16.7%, while benign pass falls from 76.1% to 65.2% (Table 3). Judge filtering reduces the unhinted effect from −22.5 to −18.8 percentage points; the same Gemini 3 Flash family judges trajectories, and only five flagged solver cases receive reported manual review. Task-level and trajectory-level denominators are both shown, which is good.

Inference is weaker than the displayed two-proportion z-tests imply. Attempts are clustered within tasks and hints, the same fixed attempts are rescored on paired original/hardened graders, and pool patches induce cross-task dependence. Independent-proportion tests ignore this pairing/clustering. The paper also pools original trials across ablation runs while comparing each to a separately generated hardened package. No task-cluster bootstrap, paired randomization, or repeated hardening run quantifies stochastic loop variance. Individual hint tests do not survive Bonferroni correction, as the paper acknowledges.

The 11-point benign-pass loss is not a small operational detail; it is evidence that the accepted construct narrowed. “Preserving solver performance” in the conclusion overstates the Terminal Bench result.

## Reproducibility and operational realism

### What is inspectable

- All three immutable full texts include methods, prompts, thresholds, and limitations.
- Terminal Wrench's complete 1.63 GB archive contains all 331 task directories, original packages, 3,632 hack trajectories, 2,352 baselines, judgments, and monitoring derivatives; its CRC check passed.
- The compact KernelBench artifact contains 400 task/config records across four 100-task arms, compact role trajectories, hardened files, autopatched/raw snapshots, per-attempt result CSVs, and the 171-commit pool history linkage.
- The release reproduces key fixed-corpus counts and exposes the 41-task precheck exclusion, raw-overrestriction states, thresholds, and stopped runs.
- The paper reports approximately $5,000 API spend and 48 hours on an 8×H200 node.

### What is not reproducible or operationally established

- no exact paper-time implementation/environment lock or pinned dependencies;
- no complete Terminal Bench hardening/result artifact in the inspected public surfaces;
- no full 12.6 GB KernelBench per-step context/debug corpus in the public Git artifact;
- no license for the KernelBench result artifact;
- no uncertainty over stochastic hardening reruns;
- no representative/adaptive attacker deployment distribution;
- no comprehensive legitimate-solution population or expert adjudication of ambiguous shortcuts;
- no proof that Docker-root terminal threats transfer to document, GUI, or professional judgment graders; and
- no measurement of maintenance burden, runtime per task, patch-review labor, or downstream score/rank changes after deployment.

The contextual guideline is practitioner testimony, not controlled evidence. Its useful advice—short outcome-oriented instructions, exploratory oracles, alternative-path tests, adversarial trials, conceptual rather than clerical difficulty—aligns with the empirical failure corpus. Its categorical preference for outcome-only grading is limited by the corpus itself: some requested work includes procedure, provenance, authorization, safety, or audit obligations that final outcome alone cannot observe.

## What the evidence supports

1. Reward-hack elicitation finds many real false-accept counterexamples in public terminal-task snapshots.
2. Iterative attack and repair can discover successive exploit classes that single-shot auditing misses.
3. Verifier-source access and cross-task sharing can broaden a fixed hacker's effective search within shared infrastructure.
4. Fixed held-out attacks from stronger models and external reports can be rejected after repair on the tested snapshots.
5. A positive-witness solver is necessary but insufficient; narrow witnesses allow severe false rejection.
6. Patch histories, raw versus repaired snapshots, attack submissions, legitimate submissions, thresholds, and role configurations can be published inspectably.

## What it does not support

- an exact or stable 16% reward-hackability prevalence;
- 323 as the reconciled Terminal Wrench unique-task count;
- verifier soundness or completeness;
- preservation of all fair alternative solutions;
- robustness to adaptive, unseen, or future exploit classes;
- universal weak-to-strong defense;
- causal attribution of ablation effects under clustered, stochastic pooled repair;
- cross-domain agent capability, safety, professional validity, production fitness, or readiness.

## Transfer to skill-bench

### Retain

1. **Separate adversarial roles.** Keep counterexample search, patch authoring, legitimate-path testing, and final approval distinct.
2. **Iterate and freeze.** Search after each accepted patch, then freeze the grader before held-out evaluation.
3. **Publish old/new matrices.** Rescore immutable attack, legitimate, boundary, and invalid artifacts against old and new grader versions.
4. **Use shared defenses only for typed shared substrates.** Record the exact infrastructure relation that licenses transfer and preserve source-task/commit lineage.
5. **Keep raw failed revisions.** Overrestrictive states are essential validation evidence, not embarrassing debris to erase.

### Repair

1. **Define dual error populations.** Every revision needs false-accept and false-reject test suites, not one reference witness.
2. **Type admissible alternatives.** Include expert-approved, independently generated, model-diverse, implementation-diverse, paraphrased, boundary, and metamorphic valid cases; record contested cases rather than forcing one label.
3. **Add adaptive post-patch attacks.** Fixed-corpus rescoring estimates retrospective rejection. Run fresh blind and source-aware attacks against the frozen revision, with sealed held-out exploit families and budgets.
4. **Treat thresholds as governed criteria.** Preserve authority, rationale, boundary examples, sensitivity, and consequences of 10× versus 12× or analogous professional tolerances.
5. **Validate pool patches per target.** A general patch must pass each target's local valid-alternative suite; one shared evaluator implementation does not prove identical task semantics.
6. **Use clustered paired inference.** Tasks, exploit families, repeated submissions, shared pool commits, and model families are dependence units. Report per-task deltas, negative-effect rates, and worst-group loss.
7. **Version repaired benchmarks.** Never rewrite historical scores. Record old/new grader hashes, changed acceptance boundary, migration reason, bridge matrix, role transition, and claim change.
8. **Do not collapse process into cheating.** If a task requires a procedure, evidence path, authorization, safety control, or audit artifact, disclose that public basis and grade its observable consequences; do not call every noncanonical implementation a hack.

## Concrete repository actions

Exercise the existing task-health, artifact-view admissibility, alternative-path, metric-monitoring, configured-system, trace, and validity-argument machinery on one real grader revision. Build a compact cross-domain falsification matrix containing:

- known attack and held-out attack-family cases;
- canonical and multiple independently derived legitimate artifacts;
- accepted alternative paths;
- threshold-boundary cases;
- invalid-environment and insufficient-evidence cases;
- a patch generated without access to the held-out matrix; and
- old/new outcomes, reasons, costs, clustered uncertainty, and claim ceilings.

No new queue task is added: this is a nonduplicate refinement of existing verifier-falsification and alternative-path validation machinery, not a need for another schema.

## Limitations of this review

This review read all three immutable full texts and audited all pinned public artifact surfaces described above. It inspected release manifests, configs, result-status distributions, fixed-corpus summaries, implementation defaults, and selected code/prompt surfaces. It did not rerun the approximately $5,000 model/GPU experiment, execute potentially adversarial 1.63 GB task environments, independently re-label all 3,632 exploit trajectories, or retrieve the omitted ~12.6 GB raw KernelBench context dumps. The later implementation surfaces cannot establish paper-time behavior, and the missing public Terminal Bench result corpus prevents a release-level reanalysis of that case study.

## Verdict

**High methodological relevance; unusually strong artifact inspectability for KernelBench and Terminal Wrench; moderate causal evidence for the configured repair package; low evidence for general verifier correctness.** Skill-bench should adopt adversarial revision as a lifecycle gate, but should judge hardening by a two-sided, versioned acceptance-boundary argument. Zero successes on known attacks is a regression result, not a certificate.