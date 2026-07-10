# Paper Review: SkillsBench — Paired Procedural-Skill Efficacy

- **Paper:** https://arxiv.org/abs/2602.12670v4
- **Authors:** Xiangyi Li et al.
- **Date read:** 2026-07-10
- **Venue / source:** arXiv preprint
- **Version read:** immutable v4, 14 June 2026
- **Local PDF:** `data/papers/pdfs/2602.12670v4-skillsbench-benchmarking-how-well-agent-skills-wor.pdf` (42 pages; SHA-256 `e987ebc3f0084a1ffc8acbca58259e33120b95fcef3876abfad060e169cf210b`)
- **Local text:** `data/papers/text/2602.12670v4-skillsbench-benchmarking-how-well-agent-skills-wor.txt` (SHA-256 `236191d785df4984f51c1cda7a88540f9e38b256b4d731d3da298d012f3ef2`)
- **Official release inspected:** https://github.com/benchflow-ai/skillsbench/tree/44cdda48f6e8c4d381f4f5075c0f4a051ba69e98 (commit `44cdda48f6e8c4d381f4f5075c0f4a051ba69e98`; tree `a0d1a819fccfac4c6710429f10887fe4b8bbe966`)
- **Release provenance:** `data/sources/releases/2602.12670v4-skillsbench/provenance.json`
- **Tags:** procedural-skills, paired-evaluation, configured-agents, deterministic-verifiers, selection-bias, criterion-leakage, artifact-quality

## One-sentence contribution

SkillsBench turns a procedural Skill into an explicit experimental intervention and evaluates 87 containerized tasks under matched no-Skills and curated-Skills conditions across 18 model–harness configurations, providing strong evidence that the **curated packages selected for this deliberately Skill-responsive inventory** increase deterministic task completion, but not an unbiased estimate of Skills' effectiveness in ordinary work or proof of professional artifact quality.

## Why this matters for skill-bench

This is the closest large evaluation of the intervention that `skill-bench` has already made ablation-ready. It advances charter objectives A and B by showing that a Skill's effect must be estimated within a fully identified configured system, and objective C by exposing what the current LH pilot must preserve before it can call a no-skill/public-skill difference capability evidence.

The paper's breadth is important: positive aggregate deltas appear in all eight domains and all 18 model–harness configurations (Sections 5.1–5.2, pp. 5–7). But the benchmark was built by retaining tasks that are “significantly easier with Skills” and rejecting tasks with no measurable separation (Section 3, p. 4; Appendices B.4–B.10, pp. 16–17). The headline +16.6 percentage points is therefore a **conditional efficacy estimate after enrichment for treatment responsiveness**, not a population-average claim about adding Skills to arbitrary knowledge work. This distinction is the review's central transfer: `skill-bench` should use paired trials to test a prespecified task portfolio, never use observed lift as an admission criterion for the same confirmatory score.

The release also sharpens the existing intervention/instrument boundary. Skills, tasks, oracles, and verifiers live in one contributor package; maintainers require a with/without comparison before merge; and the paper praises Skills for encoding “the exact file-format constraint the verifier inspects” and “the algorithmic invariant the verifier asserts” (Appendix F.4, p. 28). Anti-leakage checks may prevent literal answers while still allowing criterion-aligned procedural coaching. That is useful deployment evidence, but it does not by itself show transfer to new instances, new verifiers, or professional judgment outside the package.

## Research question and claim boundary

The narrow research question is: for a fixed task, configured model–harness system, environment, and deterministic verifier, how much does access to a curated procedural package change pass probability? A broader methodological question asks whether paired evaluation can measure inference-time augmentations without folding their effect into one raw agent score.

The evidence supports three bounded claims:

1. On this fixed 87-task inventory, the selected curated packages improve task-macro binary completion for every tested model–harness configuration.
2. Realized lift is configuration-dependent: the same nominal Skill interface is mediated by discovery, context construction, and harness execution.
3. Curated procedural content is not interchangeable with the paper's self-generation protocol.

It does **not** establish that Skills generally improve an unselected work distribution; that shorter or fewer Skills causally outperform longer bundles; that a passed deterministic verifier implies professional acceptability; or that the Skill rather than its scripts, extra context, task matching, or verifier alignment caused the gain.

## Methodology

### Benchmark construction and sampling

The paper reports 400 candidate submissions from 142 contributors, filtered to 87 tasks in eight domains (22% acceptance). The retained set contains 6 Core tasks estimated under one human hour, 53 Extended tasks estimated at 1–4 hours, and 28 Extreme tasks estimated above four hours (Section 3, pp. 3–4; Appendix M.8, p. 38). Domain counts range from 5 Media tasks to 16 Software Engineering tasks; the paper correctly marks Cybersecurity and Media slices as descriptive because they have fewer than eight tasks (Appendix M.9, p. 38).

Each package contains a human-authored instruction, Docker environment and fixed inputs, curated `environment/skills/`, held-out oracle, and deterministic verifier. Automated gates check structure, oracle success, instruction provenance, and obvious Skill-to-solution leakage; at least one maintainer then reviews realism, data, oracle, Skill quality, and anti-cheating. The current repository policy is stronger than the paper's minimum description: it requires two reviews and a trajectory audit before merge (`MAINTAINER.md`, pinned release lines 7–53).

This is purposive contributor sampling, not probability sampling of jobs, organizations, or professional decisions. “Real work” is reviewed but no sampling frame, expert-population distribution, or independent ecological-validity study is provided. Contributor-estimated completion times are reviewed by matching maintainers, without reported human completion measurements or inter-rater agreement.

### Intervention and matched conditions

For each task and configuration, the main experiment compares:

- **No Skills:** instruction and task data, without task Skill content.
- **Curated Skills:** the complete task Skill directory, including `SKILL.md`, scripts, examples, and references.

Task environment, verifier, and nominal resource limits stay fixed. Skills are exposed using each harness's native mechanism before the task instruction (Appendix N.2–N.3, p. 42). This is matched at the task/configuration level, but individual stochastic runs are not paired by random seed or shared latent randomness; “paired” means the arms share the task and configured stack.

A diagnostic self-generated arm uses two isolated sessions: a creator sees the instruction/environment and writes packages; a clean solver receives those packages. Implementations differ: Claude regenerates per trial in a shared sandbox, while Codex and Gemini reuse one generated package per task/configuration. Claude also uses a different reasoning-effort level from its baseline. The resulting −8.1 to −11.5 pp deficits are informative failure cases, not a clean control for procedural text (Appendix D.6, pp. 21–23).

### Configured-system matrix, repetitions, and aggregation

The main aggregate spans 18 configurations: 15 models through OpenHands plus GPT-5.5/Codex, Opus 4.7/Claude Code, and Gemini 3.1 Pro/Gemini CLI (Section 4 and Appendix D.2, pp. 5, 20). This design correctly treats model and harness as a joint configuration. Cross-harness comparisons for three model families show material differences, but harness implementations, model endpoints, context behavior, and native Skill familiarity still vary jointly.

Each configuration × task × condition cell targets three selected public result files, yielding 9,396 slots. Unscored, stale, or rate-limited runs are rerun; healthy verifier-scored outcomes are preferred; timeout rows are used as failures when healthy replacements are unavailable (Section 4, p. 5; Appendix N.3, p. 42). The primary metric first averages three binary rewards per task, then macro-averages over 87 tasks. Absolute lift is the arm difference. Normalized gain divides lift by remaining baseline headroom.

This aggregation gives each task equal weight, which is defensible for an inventory score. However, Figure 1's 95% Wald intervals use `n` equal to result-file count (261 per arm) rather than cluster or paired resampling over the 87 task units (Appendix G, p. 28). Repeated trials within a task share task, Skill, verifier, and likely correlated failure modes. Separate binomial arm intervals also do not directly quantify uncertainty in the paired delta. Task-cluster bootstrap or a task-level paired permutation/bootstrap should be the primary uncertainty calculation.

### Verification, cost, and evidence

All 87 main tasks use deterministic test-script verification; 85 use pytest and two direct Python checks. Main reward is binary: all required assertions pass or the task fails (Appendix B.3, p. 16). The release inspection found 78 of 87 `test.sh` files with an obvious binary 1/0 reward pattern and nine other reward-producing patterns; this is a structural check, not an independent rerun.

Across configurations, the paper reports mean task-macro pass rates of 33.9% without Skills and 50.5% with curated Skills, a +16.6 pp absolute lift and 25.5% mean normalized gain. Configuration lifts range +4.1 to +25.7 pp (Table 2, p. 6). Thirteen of 87 tasks have negative aggregate deltas. Skills are invoked at rates from 46.4% to 99.2%, and high invocation does not guarantee completion (Appendix K, p. 33).

Cost reporting is unusually useful: tokens are available for all configurations, LiteLLM cost for ten, and mean agent wall time is reported per condition. Skills can either raise or reduce token use depending on the configuration; some expensive Claude/OpenHands conditions get cheaper with Skills while others consume more (Appendix L, pp. 33–35). This argues against treating Skill overhead as a constant.

## Evidence and results interpretation

The aggregate provides convincing descriptive evidence of positive efficacy **within the released instrument**. Full coverage across the declared 9,396-slot frame, three repeats per cell, task-macro aggregation, and explicit configured-system identities are meaningful strengths. Negative-task reporting and trajectory audits also prevent the paper from presenting Skills as universally helpful.

The strongest mechanistic evidence comes from audited failures, not the average. Curated Skills can bridge obscure APIs, canonical scientific methods, regulatory schemas, and verifier-critical invariants. Conversely, Skills hurt when a heavyweight pipeline crowds out a simpler route, suppresses a stronger native strategy, or commits the agent to a brittle solver it cannot debug (Appendix F.3, p. 28). Those are reusable failure signatures for guidance design: applicability boundary, expected cost, fallback path, and diagnostic checks should be first-class Skill fields.

The self-generated audit is also valuable because it reveals multiple causal pathways hidden by one score: packages can go undiscovered, creator work can displace solver work, consumed packages can harden false assumptions, and creator access to the graded sandbox can leak instance details (Appendix D.6.1, pp. 22–23). It does not justify the simpler conclusion that agents cannot author useful Skills.

The quantity and complexity analyses are observational subgroup comparisons. Tasks with one, 2–3, or at least four Skills are different tasks; compact, standard, detailed, and comprehensive groups have different no-Skills baselines and only five tasks in the comprehensive group (Appendix F.1–F.2, p. 28). Without within-task rewrites or randomized bundle pruning, “focused Skills outperform exhaustive ones” is a hypothesis, not a causal ablation.

## Unique insight

The deepest insight is that **a Skill-efficacy benchmark can become an efficacy-enriched instrument without containing literal answer leakage**. SkillsBench blocks filenames, magic numbers, expected outputs, and verbatim oracle commands, yet task admission explicitly favors measurable separation and task review co-optimizes task, Skill, oracle, and verifier. This creates three nested estimands:

1. **Package efficacy:** does this curated package improve this jointly reviewed task/verifier?
2. **Class transfer:** does the package improve independently authored equivalent instances and verifiers from the same work class?
3. **Portfolio value:** does adding Skills improve a prespecified distribution of consequential work, including neutral and harmful cases?

The paper measures the first well. Its prose sometimes reaches toward the second and third. `skill-bench` should record these as distinct validity claims rather than arguing over whether Skills “work.”

Release inspection makes the gap concrete. At the pinned commit there are 232 Skill instances but 195 unique directory names; 180 names occur on only one task and only 15 recur across tasks. Name reuse is an imperfect proxy—different names can encode related procedures and same names can drift—but it shows that most packages are not empirically tested on another benchmark task. In the `llm-prefix-cache-replay` example, the instruction specifies S3FIFO and report fields, the Skill specifies exact longest-prefix, rounding, ghost, frequency, and eviction semantics, and the verifier checks precisely those totals and selected request indices. This is excellent package-level assistance and weak evidence of transfer to a new cache problem.

A second insight is that harness mediation is part of the treatment. Skill availability, discovery, reading, execution, and downstream verification form a causal chain. The proper unit is not “model + text” but `task × model × harness × Skill package × discovery policy × tool/environment × verifier × feedback policy`. The existing `skill-bench` component hashes and recovery edges are therefore necessary rather than bureaucratic detail.

## Transferable design patterns

### 1. Prespecify the confirmatory portfolio

Separate authoring/calibration from evaluation:

- an **authoring set** may require observable Skill lift to debug intervention plumbing;
- a **confirmatory set** must be frozen before outcome collection and include positive, null, and negative expected effects;
- a **transfer set** should use independently authored equivalent forms, perturbed evidence, or different verifier implementations;
- a **deployment-weighted set** should reflect a declared work distribution rather than equal task counts.

Never retire or reject a valid task solely because its observed Skill delta is small if that task contributes construct coverage. Store `selection_stage`, `selection_features`, whether treatment outcomes were visible, and an estimand label.

### 2. Add a treatment-exposure chain

For each trial preserve distinct events:

`available → surfaced → discovered → opened → relevant section consumed → prescribed resource invoked → procedure instantiated → artifact consequence observed`.

An invocation rate based on any read is useful but insufficient. SkillsBench's generated-pack failures show that availability is not exposure, and exposure is not correct use.

### 3. Test transfer across authoring boundaries

For a Skill claim beyond one package, require at least one of:

- another task instance not seen by the Skill author;
- an independently authored verifier testing the same professional consequence;
- a structurally different task from the same procedure class;
- a paraphrased or perturbed source pack preserving the construct;
- a holdout where scripts/templates remain useful but exact file names and constants change.

Record task author, Skill author, verifier author, shared source lineage, review participants, and outcome visibility. “No literal leakage found” is not equivalent to authoring independence.

### 4. Use task-clustered paired uncertainty

Compute per-task arm differences from all valid repeats, then bootstrap or permute tasks—not raw result files. Report the distribution of task effects, negative-effect rate, and domain intervals separately from a macro mean. Preserve invalid-environment and rerun reasons; do not silently substitute healthier rows. If multiple attempts are selected after failures, version and publish the selection algorithm before runs.

### 5. Separate deterministic correctness from professional quality

A binary verifier can establish exact values, schemas, constraints, and artifact integrity. It cannot alone establish clarity, defensibility, stakeholder fit, visual quality, judgment under ambiguity, or readiness for consequential use. Keep deterministic completion, artifact-quality review, expert readiness, process diagnosis, and cost as separate score families. The current LH adoption pilot already has the correct architecture; SkillsBench supplies evidence for running the paired intervention, not for collapsing these tiers.

### 6. Give Skills applicability and fallback contracts

Retain the paper's best authoring recommendation as typed fields: intended task class, preconditions, contraindications, expected token/tool/time cost, fast path, full path, fallback, verification steps, and known failure signatures. Evaluate routing decisions as well as eventual pass/fail.

## Limitations and validity threats

1. **Outcome-conditioned task admission biases the headline lift upward.** Tasks are required to be Skill-dependent and candidates without measurable separation are rejected. The +16.6 pp mean is valid for the enriched inventory, not an estimate for arbitrary work.
2. **Task–Skill–verifier co-design remains.** The public contribution workflow asks one submission to include all components and a with/without result. Literal answer audits do not eliminate criterion alignment, shared assumptions, or tuning to observed failures.
3. **Cross-task reuse is mostly untested.** In the inspected release, 180 of 195 unique Skill directory names occur once. The study has broad task coverage but limited direct evidence that a package transfers across independent instances.
4. **The “focused is better” result is not randomized.** Skill count and length are task-level attributes confounded with domain, difficulty, baseline, author, scripts, and package quality; the comprehensive group has five tasks.
5. **The self-generated arm is not a clean comparator.** Discovery failures, creator/solver interference, differing package reuse, sandbox carryover, task-instance access, and one reasoning-effort mismatch all vary with condition.
6. **Uncertainty ignores task clustering and pairing.** Wald binomial intervals over 261 result files treat repeats as independent Bernoulli observations and do not estimate the paired lift directly.
7. **Healthy-first result selection complicates operational estimates.** Rerunning stale, rate-limited, or unscored rows improves measurement cleanliness but conditions away some production unreliability. Timeout backfill and runtime-error treatment should be preregistered and separately reported.
8. **Deterministic pass/fail has a narrow validity basis.** It is strong for computable consequences, weak for subjective artifact quality and professional readiness. Human inspection occurs during task review, but no systematic artifact-quality labels, agreement, or threshold calibration accompany the 9,396 trials.
9. **Domain slices are small and not sampled from professions.** Eight labels establish artifact/workflow diversity, not representativeness. Legal and healthcare coverage is especially limited, and five Media tasks cannot support stable domain inference.
10. **Harness comparisons are ecologically useful but causally bundled.** Native loading, prompts, context windows, tool loops, model training familiarity, and endpoints differ. Same-model cross-harness observations do not hold all these factors fixed.
11. **Contamination remains plausible.** Public tasks, Skills, and repositories can enter future training. Paired arms reduce some model-level contamination effects, but memorized task or Skill content can interact with condition.
12. **Release/paper synchronization is imperfect.** The inspected commit is dated 8 July 2026, after v4 on 14 June. The pinned tree verifies current structure and policy, not exact paper-time bytes. The paper also derives aggregate cost/results from external Hugging Face snapshots rather than bundling all results in the Git tree.
13. **Normalized gain can distort comparison.** It is unstable near high baselines and macro-averaging per-configuration gains answers a different question from applying the formula to aggregate means. Absolute paired differences should remain primary.
14. **No expert-authority reliability is reported.** Maintainer review is substantial, but the paper does not report reviewer qualifications per task, inter-reviewer agreement, adjudication rates, or independent expert validation of the procedures.

## Reproducibility and operational realism

Reproducibility is strong at the task-package level. The paper specifies the directory contract, controlled resource fields, network policy, oracle requirement, verifier interface, two-arm protocol, aggregation, and model–harness configurations. The official repository at the pinned commit contains 87 runnable task directories, 87 task manifests, Skills for every task, 86 conventional `test_outputs.py` files, contributor/maintainer policies, and an explicit trajectory-audit workflow. The immutable commit/tree and selected blob IDs are recorded in the local provenance manifest.

Exact aggregate reproduction is expensive and time-sensitive. It requires proprietary model access, historical model endpoints, four harnesses, 9,396 selected trajectories, and external result snapshots. “Temperature 0” does not make interactive tool-using agents deterministic. The paper lists display/model IDs but the inspected Git commit postdates v4, and the result-selection process spans public result files across versions. A future replication should pin every task tree, harness commit, model endpoint/date, Skill hash, selection-policy version, container digest, and raw result ID.

Operational realism is mixed in the right way for a diagnostic benchmark: tasks produce code, spreadsheets, media, scientific analyses, and structured reports in containers; costs range over orders of magnitude; and Skills can help or harm. But network/resource isolation and deterministic outputs deliberately omit stakeholder interaction, authorization, irreversible side effects, evolving organizational context, and many subjective quality judgments. SkillsBench is best treated as high-quality evidence for **controlled procedural-package efficacy**, not a complete simulation of consequential knowledge work.

## Concrete changes for skill-bench

1. **Refine the active LH pilot's validity statement, not its schema.** The no-skill/public-skill contrast should be labeled package efficacy on a prespecified pilot task. A professional-capability claim remains blocked until independent artifact/expert evidence exists.
2. **Add selection provenance to the genuine-run report.** State that the pilot existed before outcomes, list every attempted trial, preserve invalid-environment outcomes, and prohibit outcome-based row replacement except under a frozen mechanical rule.
3. **Use task/equivalent-form paired inference when the pilot expands.** Three repeats on one task estimate run variability, not cross-task generality. Add at least one independently authored equivalent form before a transfer claim.
4. **Extend exposure diagnostics in the existing trace contract.** Distinguish Skill mounted, surfaced, opened, resource invoked, procedure instantiated, and consequence verified. This is a nonduplicative refinement of `build-lh-pilot-grader-ablation`, not a new queue item.
5. **Keep deterministic and expert score families separate.** A verifier pass can support a narrow artifact predicate; only qualified review can support professional acceptability or readiness. Route these claim limits into the pending validity-argument contract.
6. **Carry task-selection history into task health.** The pending task-health contract should record whether treatment outcomes affected admission and forbid using the same outcome-enriched inventory as evidence for a deployment-population effect without an explicit generalization argument.
7. **Add applicability/fallback fields only when the procedural-skill contract next changes.** Expected cost, preconditions, contraindications, fast path, and fallback directly target the observed negative-effect mechanisms; no standalone build task is needed.

## Action items for repository

- [x] Read the complete immutable v4 PDF/text and record hashes and page evidence.
- [x] Acquire and inspect the official repository at pinned commit `44cdda48f6e8c4d381f4f5075c0f4a051ba69e98`; preserve immutable commit/tree URLs, inventory, selected blob IDs, and scope in `data/sources/releases/2602.12670v4-skillsbench/provenance.json`.
- [x] Distinguish package efficacy, class transfer, and deployment-portfolio value.
- [x] Map nonduplicate refinements to `build-lh-pilot-grader-ablation`, `build-validity-argument-contract`, and `build-task-health-lifecycle-contract`.
- [x] Add no new queue task: the evidence sharpens three existing tasks and does not justify another parallel contract.
