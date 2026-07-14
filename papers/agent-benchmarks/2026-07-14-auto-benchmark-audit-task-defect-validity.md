# Auto Benchmark Audit: candidate defect discovery is not automatic task invalidation

## Bottom line

Auto Benchmark Audit (ABA) makes a valuable benchmark-operations move: treat the benchmark itself as an inspectable, versioned object and ask an agent to compare each task's public instruction, environment, reference solution, and grader. The paper audits 34,285 sampled tasks from 168 benchmark families and emits path-grounded findings under instruction, environment, and evaluation categories. Its strongest evidence is not the headline 25.7% major-issue rate. It is the narrower result that one configured auditor recovers many independently documented task changes on three small issue sets while also generating enough false or nonmatching findings that human adjudication remains indispensable.

The headline prevalence and score-correction interpretations exceed the evidence. The 25.7% is the fraction of administered tasks that **Claude Opus 4.7 labeled major**, not an expert-confirmed defect prevalence estimate. Human confirmation covers selected findings, not a probability sample of clean and flagged tasks, so specificity, negative predictive value, and false-negative prevalence are unknown. The severity thought experiment—whether five hypothetical competent developers would converge—was never conducted with five developers. It is an auditor prompt, not observed inter-rater evidence.

Removing flagged tasks raises mean scores and changes ranks, but that operation changes the task population and its difficulty. It does not show that the filtered score is less biased or closer to capability: no repaired equivalent forms are rerun, no external criterion is improved, and the trajectory auditor sees outcome-bearing evidence. The paper's outcome cross-tab shows flags are not restricted to failures; it does not identify what ranks would have been under defect-free versions of the same construct.

The unique transferable insight is a **candidate-defect lifecycle**, not an auto-delete rule:

`immutable task/environment/grader → auditor identity and admissible evidence view → candidate finding → independent adjudication and missed-defect probe → retain/quarantine/repair decision → new version → equivalent-form rerun → historical-score and construct sensitivity`

Automated audit output should trigger review. It must not silently become task ground truth, a deletion mask, or retrospective score correction.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, C, and D. It studies a cross-domain benchmark-hardening method, turns it into a bounded lifecycle for expertise-to-evaluation and task health, and audits whether the released implementation supports the paper's claims. Coding, terminal, science, medical, and professional tasks are measurement cases—not a scope commitment.

The concrete evidence is the complete immutable v2 paper, immutable v1 comparison, full post-v2 official archive, and an independent recomputation of the released BenchGuard precision/recall tables. The uncertainty clarified is when an automated finding licenses investigation, quarantine, repair, score qualification, or no action. Useful completion means preserving the distinction among auditor label prevalence, confirmed defect prevalence, task-set filtering sensitivity, and repaired-instrument validity.

## Sources and reading record

### Immutable primary source read in full

- Junlin Wang, Federico Bianchi, Shang Zhu, Fan Nie, Yongchan Kwon, Bhuwan Dhingra, and James Zou, *Automated Benchmark Auditing for AI Agents and Large Language Models*.
- Immutable v2: <https://arxiv.org/abs/2605.26079v2>; PDF: <https://arxiv.org/pdf/2605.26079v2>.
- Local PDF: `data/papers/pdfs/2605.26079v2-auto-benchmark-audit.pdf` (39 pages; SHA-256 `baf37c7e7ba39eac1fe1e07df870220096c3db326eae99144527388e401f8ddd`).
- Local layout text: `data/papers/text/2605.26079v2-auto-benchmark-audit.txt` (SHA-256 `af7d624e1af354ff2ab860d0ec3bf52e1e590f690cf629e81f0b60988517c49a`).
- Immutable v1: `data/papers/pdfs/2605.26079v1-auto-benchmark-audit.pdf` and `data/papers/text/2605.26079v1-auto-benchmark-audit.txt`; hashes are in the provenance record.
- Provenance: `data/sources/releases/2605.26079v2-auto-benchmark-audit/provenance.json`.
- Date read: 2026-07-14. The complete text was read from the abstract through selection, pipeline, validation, leaderboard sensitivity, prompts, case studies, limitations, ethics, provenance, and release plan. v1/v2 comparison indicates mostly editorial changes, a corrected repository URL, and clarification of the Opus 4.6 BenchGuard comparison—not a material redesign.

### Official release inspected

- Repository: <https://github.com/IsThatYou/auto-bench-audit>.
- Pinned commit: `f74341939a0dbb7a67fe1643609214f4e546df87`; tree `fb45e598fe92f0d16aa1cd686d50d17c1a96da52`.
- Archive: `data/sources/releases/2605.26079v2-auto-benchmark-audit/IsThatYou-auto-bench-audit-f743419.zip` (SHA-256 `0bdb7a7a3f5f6ee768718ee5a0b81b466a7b975e9203f28fec4d69ec037b48a1`; 4,427 files, 312,319,019 compressed bytes).
- Timing boundary: the commit is dated 2026-05-27, after arXiv v2 on 2026-05-26. It is review-time implementation evidence, not demonstrated paper-time code. GitHub exposed no tag or release at acquisition.

The complete archive member table and all text/code/JSON relevant to the auditor, prompts, BenchGuard validation, Terminal-Bench PR comparison, and leaderboard recomputation were inspected. The archive contains substantial code and leaderboard matrices, but **not the complete 34,285 per-task audit records claimed in the release plan**. That absence blocks independent reproduction of the prevalence table and exclusion masks.

## One-sentence contribution

ABA operationalizes path-grounded candidate issue discovery across heterogeneous benchmark artifacts at scale, but its configured-auditor labels require independent adjudication and repaired-form validation before they can support defect, deletion, or score-correction decisions.

## Research question

The paper asks whether an agentic auditor can inspect heterogeneous benchmark artifacts at scale, find benchmark defects that manual review misses, and quantify how those findings affect capability measurements.

It contributes:

1. an evidence-collection agent that downloads a benchmark and writes a common task manifest;
2. a task auditor with static and trajectory evidence modes;
3. a path-cited finding record containing category, subtype, severity, claim, consequence, evidence, and suggested fix;
4. a portfolio of 168 benchmark families and 34,285 administered tasks across nine domains;
5. validation against Terminal-Bench 2 maintainer changes, BenchGuard issue sets, and selected manual review; and
6. task-exclusion sensitivity analyses for five public leaderboards.

The defensible contribution is a scalable **candidate issue discovery and triage system**. The evidence does not establish authoritative defect labels, unbiased corpus-wide defect prevalence, corrected capability estimates, or an autonomous benchmark-maintenance policy.

## Methodology and system

### Portfolio and task sampling

The portfolio combines two purposive sources (Section 3.1 and Appendix B, pp. 4, 15–19):

- benchmarks named in headline tables by at least two of five recent frontier-model reports; and
- in-scope NeurIPS 2025 Datasets & Benchmarks papers.

The study excludes subjective evaluation, evaluation-methodology benchmarks, and specialized audio, video, embodied-3D, and remote-sensing systems. This defines ABA's operating range; it does not sample a population of all AI benchmarks.

Within benchmark, Table 4 shows frequent caps of 100, 200, or 500 tasks. The release's `scripts/sample_tasks.py` sorts discovered task IDs and draws `random.sample` with default seed 42; `multi_domain_streaming_pipeline.py` defaults to 100 but accepts a configured cap. The released code makes a reproducible sampling mechanism available, but the complete paper-run `sampled_tasks.json` records are absent. Consequently, the exact correspondence between Table 4 and release-time selection cannot be replayed from this archive.

The resulting 34,285 observations are heavily clustered by benchmark, source, template, author, environment, and grader. Domain percentages are descriptive shares of ABA labels in this purposive, capped portfolio. They are not population prevalence estimates, and treating each task as independent would understate uncertainty.

### Configured auditor

The paper pins Claude Code v2.1.96 with Claude Opus 4.7, default system prompt, sampling, agent loop, file/shell/search tools, and fresh sessions (Section 3.1 and Appendix C.4, pp. 4, 26). It reports `bypassPermissions` inside a sandbox limited to the per-task evidence directory and read-only benchmark checkout. This is materially better configured-system disclosure than naming a model alone.

Important residual identity gaps remain:

- model alias resolution is asserted through the pinned CLI but no provider snapshot hash exists;
- default temperature, max tokens, system prompt, and loop are intentionally inherited rather than serialized;
- no repeated audit estimates within-task auditor stochasticity;
- no second auditor family measures model-specific issue construction;
- the evidence collector is itself agentic, so omitted, wrong, or selectively resolved paths can change downstream findings; and
- the release archive does not preserve the paper's complete manifests, conversations, audit records, or sandbox canary results.

### Evidence views and modes

Static mode sees task instruction, reference answer/solution, tests, repository, dataset, and collector notes. Trajectory mode additionally sees selected agent predictions, metrics, test output, and full trajectory (Section 2 and Appendix C.3, pp. 3, 23–25).

That distinction is useful, but it is not merely “more evidence.” Trajectory mode receives post-treatment information correlated with the measured outcome. It can discover real runtime defects, but it can also reverse-engineer failures and tests. Static and trajectory findings therefore estimate different observer-conditioned constructs. Their disagreement should not be read as static error without independent adjudication.

The paper reports trajectory mode flags 8.5 percentage points more major tasks and 6.1 points more tasks overall on eight benchmarks, with average “max-severity agreement” of 53% after excluding tiny AIME (Section 5, pp. 8–9). Footnote 4 defines this quantity asymmetrically as the fraction of trajectory-major issues also called major by static mode—not a conventional symmetric agreement coefficient. It does not measure chance-corrected agreement or root-cause identity.

### Finding and severity contract

A finding contains category, severity, evidence path, claim/why-it-matters, and suggested fix (Section 2, pp. 2–4). Appendix C adds subtype and finding ID. The rubric asks a thought experiment: would most of five competent domain developers, given the public prompt, reliably produce a test-passing solution? Severity 0 is clean, 1 a discoverable interpretive gap, and 2 a major gap no expertise can bridge (Appendix A/C, pp. 15, 25).

This is a valuable fairness boundary: hard but clear tasks remain clean; private tests may enforce consequences of disclosed requirements but not arbitrary implementation details. Yet the record collapses several distinct claims:

- public-basis/specification defect;
- environment availability defect;
- gold-answer error;
- verifier false reject;
- verifier false accept;
- temporal dependency drift; and
- expected disagreement among legitimate professional methods.

These require different evidence and remediation. A wrong gold answer may be repaired; an unstable live dependency may require freezing; an underdetermined professional judgment may require plural scoring rather than disclosure of one answer.

There is also paper/code drift. The paper specifies 0–2, but `src/bench_audit/audit_models.py` accepts task-finding severity through 3 and the BenchGuard converter maps 3 to `CRITICAL`. The released BenchGuard artifacts include only LOW/MEDIUM/HIGH, but the executable contract is broader than the paper's declared scale.

## Evidence and what it establishes

### Corpus-wide ABA labels

Table 1 reports 14,024 major findings affecting 8,819 of 34,285 tasks: 25.7% of administered tasks had at least one major finding, while 15.1% had minor but no major finding (p. 5). Domain major-label shares range from 13.2% in math to 42.2% in safety/alignment.

These are internally coherent counts of auditor output. They establish where this configured auditor concentrates concern under this sampling and rubric. They do **not** establish true defect rates because:

1. most tasks were not independently labeled;
2. clean tasks were not sampled for false negatives;
3. confirmation sampling is not probability-linked to the 34,285-task corpus;
4. task clusters and benchmark caps are not weighted to a target population;
5. the same auditor defines labels and severity; and
6. the released archive omits the complete records needed to inspect duplicates, invalid audits, confidence, and task-level evidence.

### Terminal-Bench 2 maintainer-change comparison

The paper interprets 21 in-rubric issues from an open PR touching 22 documented tasks, excludes four due-diligence/resource/oracle cases, and reports 14/21 strict and 17/21 partial-plus recall (Section 4.1 and Appendix D.1, pp. 7, 26, 30). For seven major tasks outside the PR, authors manually review 11 findings and report 8/11 strict and 9/11 partial-plus precision.

This is useful external corroboration, but weaker than “ground truth” implies:

- PR #53 was open at release capture, not evidence of merged fixes or post-fix validity;
- authors manually decompose a multi-purpose PR into issue units and decide what is in rubric;
- a code change can acknowledge operational pain without validating ABA's root cause or severity;
- the PR comparison is neither blinded nor independent at the adjudication stage; and
- the denominator excludes changes judged out of scope.

The release's `finding_judgments.json` contains 29 findings across 17 listed tasks, with 13 `yes`, 1 `partial`, and 15 `no` support judgments. This is not the exact 21-issue gold denominator in Table 2; it is a broader finding-to-PR support record with explicit exclusions. The distinction reinforces the need to preserve candidate finding, external change, alignment judgment, and final adjudication as separate objects.

### BenchGuard issue-set validation: independently recomputed

The archive contains normalized ABA findings, all pairwise alignment-judge verdicts, and generated reports for BixBench and ScienceAgentBench. I independently recomputed each finding's and gold issue's best verdict from those released pairs:

| Set | Gold issues | ABA findings on revised tasks | Strict recall | Partial-plus recall | Strict precision | Partial-plus precision |
|---|---:|---:|---:|---:|---:|---:|
| BixBench Verified-50 | 24 | 28 | 15/24 = 62.5% | 19/24 = 79.2% | 14/28 = 50.0% | 20/28 = 71.4% |
| ScienceAgentBench | 12 | 27 | 10/12 = 83.3% | 11/12 = 91.7% | 11/27 = 40.7% | 14/27 = 51.9% |

The recomputation exactly matches Table 2 and the released reports (paper p. 7; archive `benchmarks/benchguard/output/{normalized,matches,reports}/`). This verifies aggregation from released judgments, not the truth of the gold sets or alignment judge.

The validation has material limits:

- gold sets contain only 36 issues across 29 revised tasks;
- the same Gemini 3 Flash alignment judge and BenchGuard protocol determine semantic match;
- no uncertainty interval or repeated judge reliability is reported;
- ScienceAgentBench emits 27 findings for 12 issues, giving high recall but only 40.7% strict precision;
- partial match means same functional area but a genuinely different problem, so partial-plus is not confirmation of the gold defect; and
- wrong-ground-truth issues may be disadvantaged because ABA's converter has no distinct ground-truth category.

The result supports human-in-the-loop triage: the auditor catches many known issues but cannot safely adjudicate or remediate alone.

### Manual confirmation

Section 4.3 reports review of 56 major and 30 minor static findings across 12 frontier benchmarks and 25 major trajectory findings from SWE-bench Verified (p. 8). Strict/partial-plus precision is 73%/91%, 63%/83%, and 92%/96%, respectively. Appendix D.3 instead says **54** major static findings (p. 27), an unresolved denominator inconsistency.

The paper does not report reviewer count, qualifications by domain, assignment overlap, blinding, independent ratings, adjudication, agreement, sampling probabilities, or verbatim label records. Calling this “domain expert” validation is therefore not operationally auditable. The ethics section simultaneously says the study “involves no human subjects” while the methods call this an internal human-rater study; regardless of regulatory classification, the measurement contribution requires a reproducible rater protocol.

Reviewing only emitted findings estimates a selected positive predictive value. It cannot estimate recall, specificity, clean-task validity, or prevalence. Relative to 34,285 tasks, the static major, static minor, and trajectory review counts are tiny and outcome-selected; that fact is descriptive, not itself a criticism if claims remain narrow.

## Leaderboard sensitivity is not score correction

The paper combines public per-task result matrices with static/trajectory flag masks for DABstep, SWE-bench Pro, SWE-bench Verified, Terminal-Bench 2, and SWE-bench Multilingual (Appendix E, pp. 28–35). It reports that excluding flagged tasks raises mean scores on all five; the abstract highlights 9.9 and 9.6 percentage-point average increases for SWE-bench Verified and Terminal-Bench 2, and middle ranks can move substantially.

This establishes **deletion sensitivity**: published scores and ranks depend on task inclusion. It does not establish that the filtered leaderboard better measures capability.

Let the original score be the mean over task set `T`, and the filtered score over `T \ F`, where `F` is selected by an outcome-informed auditor. Their difference combines at least four effects:

1. genuine removal of invalid measurements;
2. change in task difficulty and content composition;
3. model-by-task interactions that alter ranks; and
4. auditor selection related to observed failure, complexity, or evidence availability.

The paper's Figure 8 cross-tab refutes only the strongest claim that trajectory flags are *exclusively* failed tasks: passed-and-flagged cells are nontrivial. It does not establish independence between flags and outcomes, nor does it identify a causal correction. The auditor directly sees status, test outputs, and trajectories. No held-out auditor, hidden-outcome condition, repaired-task rerun, matched replacement task, or external criterion is used.

A valid repair analysis would retain the original task, create a new version with the defect resolved, run the same configured systems on both under matched conditions, and estimate:

- original-form score;
- deletion-mask score;
- repaired-equivalent-form score;
- common-task paired change;
- content/construct shift;
- rank and decision sensitivity; and
- uncertainty clustered by task family and system.

The release archive contains public leaderboard matrices and refresh scripts but not the full audit masks or complete per-task findings. Therefore the paper's 9.9/9.6-point results and Figures 7–12 cannot be independently recomputed from the pinned archive. The available refresh scripts also draw mutable public leaderboard data; the JSON snapshots are post-v2 and must be treated as a later release state.

## Release audit, cost, and operational realism

### What is reproducible

The post-v2 archive exposes:

- auditor schemas and runners;
- static and trajectory prompt templates;
- the task rubric;
- evidence-collection and seeded sampling scripts;
- 146 benchmark configurations;
- complete BenchGuard normalized findings, pair judgments, and reports;
- Terminal-Bench PR summaries and finding judgments;
- large public leaderboard snapshots, per-row outcomes, task matrices, and 20 refresh scripts; and
- dependency lock/configuration files.

The BenchGuard table is reproducible from archived judgments. The code makes the intended audit workflow inspectable.

### What is not reproducible

Despite the paper's claim that “all task annotations,” “per-task audit findings,” manifests, run scripts, and scoring scripts are released (pp. 2, 39), the pinned archive does not include the corpus-wide `task_audits_static`/trajectory records, conversations, paper-run manifests, sampled-task ledgers, domain aggregation tables, task exclusion masks, or a self-contained figure/table reproduction script. A scan of all 4,115 JSON files found no corpus-wide `TaskAuditRecord` objects; only the small BenchGuard normalized subsets and PR judgment file carry finding-level evidence.

This prevents audit of:

- how invalid/agent-error sessions enter denominators;
- whether all cited paths resolved at paper time;
- finding duplication and category/severity consistency;
- confidence distributions;
- exact sampled task IDs and source revisions;
- the 25.7% aggregation; and
- the score/rank sensitivity masks.

### Cost

Appendix C.5 samples 10 audits from each of six benchmark runs (60 conversations) and reports means from $0.40 to $0.80, with an unweighted mean near $0.60 per task (p. 26). At that mean, 34,285 audits imply roughly $20,571 of model-call cost, before evidence acquisition, compute, retries, engineering, or human adjudication. This is a rough extrapolation, not a paper-reported total. The paper reports no dispersion, sampling uncertainty, failed-call cost, collector cost, trajectory-generation cost, or total study spend. “Affordable to any team that can run the benchmark” is a judgment, not an empirical cost-effectiveness result.

Operationally, the system can lower review search cost, but the dominant unresolved cost is likely expert adjudication and repair validation. Precision around 41–73% means a large finding stream still creates substantial review load.

## Unique insight: defect evidence must be lifecycle evidence

ABA's most important idea is that benchmark validity is not fixed at publication. The missing step is to model a finding as an evidence-bearing state transition rather than a binary deletion bit.

A reusable record should distinguish:

1. **Instrument identity:** immutable task, instruction, source pack, environment, grader, harness, and release version.
2. **Auditor identity:** model/provider/scaffold/tools/prompt/rubric/defaults, collector version, budget, sandbox, seed, and evidence view.
3. **Candidate finding:** category, affected projection, claim, severity rationale, evidence locator, confidence, and suggested remedy.
4. **Observer status:** static, trajectory, outcome-visible, external-source-visible, and any information entitlement.
5. **Adjudication:** reviewers, domain authority, blinding, independent labels, disagreement, alternative legitimate paths, and decision.
6. **Missed-defect evidence:** reviewed clean sentinel tasks and known-defect controls, not positive findings alone.
7. **Action:** retain, annotate, quarantine, repair, retire, split criterion, broaden verifier, freeze dependency, or escalate.
8. **Version transition:** exact changed loci and old/new hashes without rewriting historical scores.
9. **Revalidation:** reference witnesses, negative controls, alternative valid solutions, environment canaries, and repeated trials.
10. **Measurement impact:** original, deletion, repaired common-form, replacement-form, rank, cost, and claim sensitivity.
11. **Claim ceiling:** what the evidence licenses and explicitly excludes.

This lifecycle preserves ABA's scale advantage while preventing auditor authority laundering. A maintainer change, expert agreement, executable counterexample, and repaired rerun are distinct evidence types; none should overwrite the others.

## Limitations and validity threats

### Construct and content

1. The rubric targets prompt/test convergence and misses benchmark forms with subjective, plural, preference-based, or consequential human evaluation.
2. The “five developers” construct is simulated by one auditor rather than measured.
3. One rubric merges ambiguity, environment, wrong truth, and grader incompleteness despite different remedies.
4. Domain-standard knowledge versus hidden obligation is itself domain- and stakeholder-dependent.
5. The portfolio is purposive and excludes seven classes; domain label shares do not generalize beyond it.
6. Benchmark-level caps alter domain composition and effective weighting.
7. No expert task-author or affected-user evidence tests whether a suggested clarification changes the intended construct.

### Auditor validity

8. One model/harness produces the corpus-wide labels.
9. No repeated runs estimate within-task stochasticity.
10. No independent collector audit measures missing or incorrectly mapped artifacts.
11. Static and trajectory modes have unequal, outcome-conditioned evidence views.
12. Path citation establishes locator existence, not evidentiary entailment or completeness.
13. Confidence is recorded in code but not calibrated against correctness.
14. Paper severity is 0–2 while code accepts 0–3.
15. The asymmetric “max-severity agreement” is not inter-rater agreement.

### Validation

16. BenchGuard validation has only 36 gold issues and uses an LLM semantic alignment judge.
17. Partial match is not confirmation of the same defect.
18. PR evidence is author-decomposed, open at capture, and can reflect maintenance choices outside ABA's causal framing.
19. Manual confirmation lacks reviewer identities/qualifications, overlap, blinding, adjudication, agreement, and released labels.
20. The 56-versus-54 major-static denominator conflicts between Section 4.3 and Appendix D.3.
21. Positive-finding review cannot estimate false negatives, specificity, or prevalence.
22. The case-study “Disagree” example demonstrates that plausible evidence still requires authority and adjudication.

### Score and claim validity

23. Filtering changes construct coverage and difficulty as well as measurement error.
24. No repaired-task reruns estimate the counterfactual score under valid versions.
25. Outcome-bearing trajectories create selection/endogeneity risk.
26. Cross-tabs do not establish independence or causal score inflation.
27. Rank movement is decision sensitivity, not evidence that the new ordering is truer.
28. Model-by-task missingness and differing trial counts require explicit eligibility and aggregation policies.
29. No clustered uncertainty or multiplicity analysis accompanies many model/rank comparisons.
30. “25.7% problematic” and “score increases” should not be promoted to benchmark-invalidity or capability-correction claims.

### Reproducibility and operations

31. The official commit postdates v2 and has no immutable release tag.
32. Complete paper-run annotations, manifests, conversations, sampled IDs, and exclusion masks are absent.
33. Mutable refresh scripts and live upstream sources can change leaderboard matrices.
34. Model aliases and CLI defaults are not fully immutable.
35. Cost evidence is a 60-conversation sample without variance or full pipeline/human cost.
36. Suggested fixes are not tested for verifier soundness, alternative-path completeness, or construct preservation.

## Transfer to skill-bench

### Retain

1. **Audit the instrument before scoring systems.** Inspect instruction, sources, environment, artifact contract, grader, and reference witness together.
2. **Use typed evidence views.** Static and outcome-visible trajectory audit are separate observer conditions.
3. **Require concrete locators.** Candidate findings should cite immutable file/line/artifact evidence.
4. **Separate difficulty from unfairness.** Hard-but-clear tasks remain valid candidates.
5. **Provide suggested remediation.** Findings should be actionable, not generic quality labels.
6. **Publish sensitivity.** Show how task-health decisions affect component scores, ranks, claims, and costs.
7. **Keep historical versions.** Repairs create new instruments; they do not rewrite old outcomes.

### Repair

8. **Rename outputs candidate findings.** Only adjudication can promote them to confirmed defects.
9. **Split issue predicates.** Instruction public basis, source authority, environment availability, gold correctness, false reject, false accept, and temporal drift need separate fields.
10. **Add clean sentinels and known-defect controls.** Positive-review precision alone is insufficient.
11. **Use plural adjudication.** Preserve reviewer authority, independent labels, disagreement, and alternative legitimate paths.
12. **Calibrate severity empirically.** Ask actual experts or representative contributors whether multiple solutions converge; do not reify the five-developer prompt.
13. **Fail closed on missing evidence.** `insufficient_evidence` and collector errors must remain outside clean/defect denominators.
14. **Separate delete from repair estimands.** Always report original-task, common-task deletion, and repaired-form results.
15. **Bind auditor and source identity.** Hash model/scaffold/prompt/rubric/collector/environment and upstream task release.
16. **Preserve claim ceilings.** Auditor prevalence is not defect prevalence; deletion sensitivity is not corrected capability.

### Test

17. **Blind outcome-view ablation.** Compare static, trajectory-with-outcome-hidden, and full trajectory audits against independent adjudication.
18. **Repeated multi-auditor design.** Estimate within-auditor recurrence, between-auditor disagreement, criterion-level reliability, and cost/yield.
19. **Probability sentinel.** Randomly review clean and flagged tasks with known inclusion probabilities to estimate false negatives and prevalence.
20. **Repair counterfactual.** For each confirmed defect, create an immutable repaired form, validate legitimate alternatives, and rerun matched configured systems.
21. **Adversarial auditor controls.** Plant plausible-but-unsupported path claims, stale sources, misleading references, and equivalent alternative solutions.
22. **Decision-loss evaluation.** Measure review time, accepted fixes, rejected findings, new defects introduced, score qualification decisions, and maintenance burden—not recall alone.

## Concrete repository actions

- Added this deep, release-audited review and indexed it under rubrics/graders/task health.
- Updated `data/papers/index.json` from acquisition-pending to fully reviewed/release-audited with exact artifact paths and claim boundary.
- **No new build task added.** Existing task-health, validity-argument, metric-monitoring, artifact-admissibility, adversarial-verifier, execution-validity, lifecycle, and repeated-evaluation machinery already contains the necessary homes. A new ABA-specific contract would duplicate those layers. The evidence should instead inform future consolidation of candidate-defect → adjudication → repair → revalidation transitions.
- Canonical synthesis was not changed in this run. The source materially sharpens a lifecycle boundary but does not overturn the existing principle that task health, grader evidence, metric estimands, and validity claims remain separate.

## Assessment

- **Most reusable contribution:** path-grounded, task-level pre-measurement auditing across instruction, environment, reference, and grader.
- **Strongest evidence:** released BenchGuard judgments reproducibly show 62.5–83.3% strict recall but only 40.7–50.0% strict precision on two small issue sets; useful triage, unsafe automatic adjudication.
- **Unique insight for `skill-bench`:** automated audit is a candidate-defect discovery intervention embedded in a versioned maintenance lifecycle.
- **Most serious validity flaw:** auditor-label prevalence and deletion sensitivity are discussed too readily as benchmark-defect prevalence and corrected capability.
- **Most serious reproducibility flaw:** the complete 34,285 task records and task exclusion masks promised by the paper are absent from the pinned release.
- **Safe claim:** ABA demonstrates scalable, evidence-linked candidate issue discovery and substantial leaderboard sensitivity to a configured exclusion rule. It does not establish corpus-wide defect prevalence, authoritative severity, corrected model capability, professional validity, or an autonomous benchmark-maintenance policy.
