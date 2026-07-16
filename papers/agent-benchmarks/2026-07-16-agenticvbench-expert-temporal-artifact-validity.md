# AgenticVBench: a substantially inspectable temporal-artifact suite, but release defects and missing human evidence cap its claims

## Source and review status

**Deep review of the complete immutable primary paper and a commit-pinned official release.** I read the complete 22-page arXiv v1 PDF/text and audited the complete official repository snapshot, including all 101 released task records, all 36 Repurpose rubrics, and one task from each of the four reported families end to end. The snapshot is dated 15 July 2026, roughly seven weeks after v1; it is acquisition-time implementation evidence, not proof of the paper-time tasks, graders, environments, or results.

- **Paper:** Zongheng Cao, Yi Zheng, Rui Song, and Xinyu Hu, *AgenticVBench: Can AI Agents Complete Real-World Post-Production Tasks?*, arXiv:2605.27705v1, https://arxiv.org/abs/2605.27705v1
- **Version read:** immutable v1, submitted 26 May 2026; metadata has no withdrawal/retraction notice
- **Date read:** 2026-07-16
- **Local PDF:** `data/papers/pdfs/2605.27705v1-agenticvbench.pdf` (22 pages; SHA-256 `7c3782400559fd35f242bbb78d036082b71980aa7e921f4b707ac5fbdd1ea2d3`)
- **Local text:** `data/papers/text/2605.27705v1-agenticvbench.txt` (SHA-256 `3ebf47850030d82ba43246decf7be835cdf6c0ee42eb012b89f9145c517e4451`)
- **Official release audited:** https://github.com/PhiloLabs/agentic-vbench/tree/2933a7bfa1bd6134f0a5f76d7efc728f081dd53e
- **Release provenance:** `data/sources/releases/2605.27705v1-agenticvbench/provenance.json`
- **Static audit:** `data/sources/releases/2605.27705v1-agenticvbench/release-audit.json`
- **Dataset access boundary:** the paper-linked `PhiloLabs/agentic-vbench` Hugging Face page returned HTTP 401 when acquired; the release instead downloads task media from `ameddserM/agentic_vbench_video_*`. The observed 401 is only an access-state fact, not proof of permanent unavailability.

## One-sentence contribution

AgenticVBench combines 100 long-horizon post-production tasks, expert-derived briefs, deterministic temporal/artifact verifiers, open-ended editorial rubrics, three repeated rollouts, cost accounting, and configured model–harness comparisons; unlike CutVerse, its later release exposes the complete reported four-family task count and substantive graders, but neither v1 nor the release establishes task-population representativeness, source rights, expert-approval lineage, human-reference comparability, grader validity, or auditable paper results.

## Why this matters

This review advances charter objectives A, B, and C by testing whether a newer temporal-artifact benchmark repairs the exact gaps exposed by CutVerse. The answer is mixed and useful:

- **Retain:** executable artifact outputs, criterion-specific temporal views, golden/broken anchors, must-preserve checks, repeated trials, configured-system identity, and a real task/grader release.
- **Repair:** public-basis consistency, source rights and hashes, expert contribution lineage, human/reference denominators, rater protocol, rubric sign/dependency semantics, missingness, cluster-aware uncertainty, and release/result correspondence.
- **Test before stronger claims:** verifier soundness against alternate valid outputs, editorial-rater reliability, human–agent environment comparability, harness interventions, professional acceptance, and downstream utility.

The general lesson is not to narrow skill-bench to video. AgenticVBench demonstrates that **a temporal artifact can be highly inspectable while the claim chain above it remains invalid**. Executable checks do not automatically establish fair requirements, professional quality, calibrated expertise, human equivalence, or capability.

## Research question and defensible claim boundary

The paper asks whether frontier multimodal agents can complete realistic post-production tasks and how much model behavior changes with the harness. It constructs four workflow-oriented families: Assembly, Repair, Sequencing, and Repurpose (Sections 1–2, pp. 1–5), then reports seven models in 20 model–harness combinations, three attempts per task, human reference deliverables, and task-family diagnostics (Section 3 and Appendices A–H, pp. 5–22).

The strongest defensible claim is:

> The authors report evaluating 20 configured model–harness packages three times on 100 authored media tasks. The selected instrument combines exact ordering/selection checks, reference-relative repair measures, and binary editorial rubrics, and produces materially different descriptive scores and failure signatures across task families and harness packages.

The evidence does **not** establish that:

- four recurring author-selected families represent post-production work frequency, consequence, language, region, genre, or tool ecology;
- 20 experts independently approved every task and criterion, or that their authority survives team operationalization;
- public media are licensed for benchmark redistribution or derivative processing;
- every hidden check is a fair consequence of the public brief;
- the reported 96.4–98.2% agreement is inter-expert reliability, calibrated model validity, or held-out criterion accuracy;
- the student-editor subset is numerically or procedurally representative of the 100 tasks or equivalent to the industry-expert pool;
- a common model effect is isolated when native prompts, planning, tool surfaces, sub-model routing, defaults, and providers differ;
- a 20-point within-model spread is caused by one harness feature rather than the whole configured treatment;
- three repetitions yield stable rankings without task-clustered uncertainty and complete missingness accounting;
- under-30-minute agent runs are comparable to tasks said to require 0.5 hours to one week of human work;
- the post-v1 release reproduces v1 tasks, judges, scores, trajectories, human labels, or result tables;
- scores establish professional acceptance, production fitness, labor substitution, safety, or readiness.

## Methodology and system

### Expert pool and task authoring

The paper reports screening about 50 candidates and accepting 20 after portfolio review, interview, and calibration. Table 6 allocates them across traditional studios (4), AI film studios (4), independent creators (3), and video-AI companies (9), averaging 4–10 years by group (Appendix D, pp. 17–18). Experts independently drafted briefs; the team retained recurring long-horizon, verifiable families; experts and the team then reviewed generated programmatic tasks or authored Repurpose briefs and rubrics (Sections 2.1–2.3, pp. 2–3).

This is materially stronger than attaching an occupational label to internal task writers. The calibration exercise also tries to turn “good pacing” into observable checks and requires items to be grounded in the brief, observable, binary/deterministic, and independent of hidden author intent (Appendix D, p. 18).

But the paper does not publish expert-level IDs, qualifications, task assignments, contribution counts, time, review decisions, rejected items, conflicts, disagreement, or compensation amount. “Industry-standard” and “market rates” are not cost evidence. Task authors may also review their own work, and “independent reviewer from the expert pool **or project team**” does not guarantee independent domain validation (Section 2.8, p. 5). The release contains no expert contribution, consent, approval, review, or reason-code records. It therefore supports an expert-involved authoring description, not task-level professional authority.

The family selection itself is outcome-conditioned on verifiability: aesthetic evaluation without reference and ideation without structured requirements are excluded (Section 2.2, p. 2). That is sensible for reliable scoring but changes the target construct. The benchmark samples work that is both long and benchmarkable, not all consequential post-production expertise.

### Four task families

**Assembly (18).** Each task asks the agent to map candidate clips to four storyboard slots using description, shot size, angle, lens, and movement, then submit an MP4 plus manifest. The release's task 1 contains 12 candidates, exact hidden picks, and an SSIM “honesty” check sampling three internal frames per claimed segment. Reward chance-corrects exact per-slot selection against 1/3. This tests selected clip identity plus sparse render correspondence—not whether the five cinematic fields were independently validated, whether another clip is professionally acceptable, or whether continuity across assembled cuts is good.

**Repair (18).** The paper injects one localized audio, visual, or timeline defect and scores relative to broken and golden anchors, with a smaller preservation term (Sections 2.5 and H.1, pp. 3–4 and 20–21). The released shot-swap example instead computes whole-video PSNR against the hidden original, with reported swap-range IoU only diagnostic. Its public task asks for the exact two misplaced ranges, yet range correctness contributes nothing if the rendered video happens to resemble the reference. The release also requests `output.mp4`/`output.json`, whereas paper Table 2 specifies `fixed.mp4`/`report.md`. This is substantive post-v1 drift, not a cosmetic rename.

**Sequencing (28).** Agents order 7–20 shuffled clips from a synopsis. The score multiplies normalized footrule, LIS, and adjacent-pair fidelity, while the release additionally scales by SSIM honesty over every segment. This is a strong inspectable consequence check for clip ordering. Yet the original sequence is treated as uniquely correct even where narrative editing could admit alternatives; no expert-equivalence set or alternate-order adjudication is published.

**Repurpose (36).** Agents condense four-minute-to-three-hour sources into brief-constrained deliverables. The paper reports 1,069 approximately-30-item rubrics over Format, Visual, Narrative, Sound, and optional Penalty pillars (Section 2.7, p. 5). The release contains **1,137 items**, not 1,069: 196 deterministic, 626 `opus-vision`, 290 `gemini-audio`, and 25 `gemini-video`. The later runner uses Claude Opus 4.7 per visual item and Gemini 3.1 Pro for audio/video items, plus Whisper, ffprobe, scene detection, OCR, and handcrafted parsers. That is a substantive and unusually inspectable multi-view evaluator, but it is not the paper leaderboard's human grading and has no released calibration labels.

### Quality control

The paper claims four gates: authoring feasibility/observability, asset decoding and provenance/license metadata, author plus independent review, and golden/adversarial verifier tests (Section 2.8, p. 5). Those are excellent categories to retain. The release only partially realizes them. All 100 reported tasks have instructions, setup, solution, and judges, and all 142 Python files compile. But there are no QC ledgers, candidate/rejection records, adversarial submissions, acceptance decisions, reviewer identities, or calibration results. Oracle scripts are generally witnesses, not completeness tests; Repurpose's “oracle” explicitly just copies the source and is not a real solve.

### Configured systems and trials

The paper gives model/harness versions, 200 turns, 30-minute wall-clock cap, 4 vCPU/8 GB Modal sandboxes, native tool surfaces, fresh sandboxes, and K=3 independent provider-sampling attempts (Appendix A, pp. 12–13). This is far more operational detail than CutVerse. It correctly says the pinned harness images encode prompts, retries, tool descriptions, and defaults.

However, “held constant” does not mean treatment-equivalent. Provider defaults are not overridden; OpenClaw alone gets typed image/TTS/music/video primitives and managed sub-models; native harnesses expose different planners and prompts; OpenClaw's idle timeout is changed; endpoint snapshots and all sub-model versions are not fully pinned. The results identify 20 configured packages. The paper's feature-level explanations—Codex deliberation, OpenClaw routing, Claude planning, OpenCode caching—are trajectory interpretations, not randomized component effects.

### Human reference and grader calibration

Appendix C says three university film-program editors independently complete each selected task, with the same source materials and scoring but natural editing tools. Per-task medians are averaged by family (pp. 16–17). This improves on an unconstrained “human ceiling,” yet the paper never reports the subset size, task IDs, sampling algorithm, editor count, experience distribution, hours, time limits, pay, invalids, tool versions, or family-level uncertainty. Calling the red line “expert human reference” obscures that the described executors are trained students, not necessarily the 20 industry experts who authored the benchmark.

The same recruitment pipeline supplies Repurpose editors and graders, excluding self-grading. The paper reports raw agreement of 96.9% Visual, 96.4% Narrative, and 98.2% Sound “after calibration” (Appendix F, p. 19), but omits the number of items, submissions, graders, duplicate assignments, class prevalence, human–human agreement, adjudication, held-out split, confusion matrices, clustering, and uncertainty. It is unclear whether Figure 5 is human–human, model–human, or reconciled agreement. The assertion that it shows a “valid proxy” is unsupported.

### Cost and denominators

The paper usefully reports about $7,477 estimated inference cost and separate token buckets (Appendix G, pp. 19–20). Yet its audit denominators do not reconcile. A complete 100-task × 20-combination × 3-repeat campaign implies 6,000 task rollouts. Repurpose reports the expected 2,160 rows (36×20×3), but the non-Repurpose audit reports 4,610 rows, while 64×20×3 implies 3,840—**770 fewer**. Table 5 also labels 80 benchmark–combination cells per repeat as “rollout evals,” collapsing thousands of task executions into suite cells. No task-level run ledger explains stale, duplicate, retried, or extra rows. Costs may be useful operational estimates, but the empirical denominator is not auditable.

## Evidence and result interpretation

The paper reports a best configured stack near 31%, family gaps of 43–65 points from its human reference, a 20-point GPT-5.5 Assembly spread across harnesses, and task-specific oracle-hint/field-removal changes (Section 3, pp. 5–8). It also reports failure counts—153 Repurpose and 237 Repair—coded into long-context loss, temporal reasoning, modality misalignment, and hallucinated grounding.

These findings support descriptive diagnosis under the authors' instrument. They do not support causal bottleneck or ranking claims:

- top-five combinations are selected before ablation, inducing winner-selection and limiting generality;
- the intervention combines information and difficulty changes rather than isolating a latent skill;
- failure coding has no sample frame, codebook, raters, duplicate labels, agreement, adjudication, or denominator relative to all attempts;
- tasks, rubrics, authors, sources, durations, and criterion counts cluster outcomes, but no hierarchical/task-clustered uncertainty is reported;
- K=3 is averaged, while pass-at-k, worst-case reliability, variance components, and missingness sensitivity are absent;
- no released results or trajectories allow recomputation.

One trajectory is especially revealing. The highest-scoring cited KNEAD Repurpose run builds a 60-second video without ever sending source pixels to Gemini; it chooses four fixed offsets and narrates from the brief (Appendix B.3, pp. 15–16). This is valuable failure evidence: structural and rubric success can coexist with non-adoption of the authoritative source. But without released criterion outputs and comparison to source-grounding checks, it is an anecdote, not an estimated prevalence.

## Release audit and reproducibility

The post-v1 archive is a major improvement over CutVerse: 872 files, Apache-2.0 code, Harbor wrappers, 100 task directories matching the reported 18/18/28/36 counts, substantive setup/solution/judge code, and 36 full rubrics. It contains 101 task records because an additional `agentic_vbench_understanding` prototype sits beside the frozen four-family suite; README still correctly describes the scored four-family total as 100.

Reproducibility remains bounded:

1. **No empirical artifacts.** The archive has no paper trajectories, result ledgers, human submissions, labels, agreement tables, calibration data, ablation outputs, or leaderboard table.
2. **Source assets are remote.** Media are downloaded at image-build time. Only all 28 Sequencing tasks (plus the extra Understanding prototype) pin a material SHA-256. Assembly, Repair, and Repurpose use mutable `main` or unversioned URLs without checksum verification.
3. **Rights evidence is absent.** Of 101 task TOMLs, 88 omit a license field and 13 say `unknown-research-use-only`; none supplies affirmative task-level redistribution/derivative rights. A repository Apache license does not license third-party films, broadcasts, music videos, talks, or festival submissions.
4. **Internet leakage is live.** 100/101 task environments allow internet. Assembly/Sequencing prompts prohibit searching for source films, but there is no network allowlist or retrieval audit. Public source titles in Repurpose and release-visible hidden rubrics further increase contamination and criterion-learning risk.
5. **Paper/release drift is material.** The release's 1,137 Repurpose items differ from the paper's 1,069; the released grader stack is model-based rather than the paper's human leaderboard grading; repair outputs differ; and no exact paper commit is identified.
6. **Hosted access is unstable.** The paper-linked dataset page returned 401 while task Dockerfiles point to a different account. A runnable future build depends on those mutable assets and external APIs.

Thus reproducibility is **high for static inspection of the later task/grader definitions, moderate for rebuilding some tasks while remote assets remain stable, and absent for reproducing v1 results or human claims**.

## Unique insight: observer richness cannot rescue an incoherent criterion contract

AgenticVBench repairs CutVerse's sparse-screenshot problem by observing manifests, source clips, rendered video, frame windows, audio, transcripts, metadata, and model judgments. Yet the release exposes a deeper failure: **more evidence channels do not make the score valid when the public requirement, criterion polarity, source authority, and aggregation semantics disagree**.

The KNEAD task makes this concrete:

- the public brief requires **1280×720**, but released rubric F-02 requires **1920×1080**;
- the release audit finds analogous brief/rubric resolution contradictions in 13 of 36 Repurpose tasks;
- KNEAD criterion N-01 positively states that the central turn is present, gives it weight `-45`, but omits the `narrative_essential` flag that the scorer requires to invert a good-state negative item; the implementation therefore penalizes a passing central-turn judgment;
- at least four other released rubrics use the same positive-state/negative-weight pattern (the central turn in `horror-raremedium`, `romance-pickup`, `scifi-lie`, and `silent-piper`) without the flag;
- the aggregate then clips total/ceiling into [0,1], allowing large penalties and criterion dependencies to alter scores without a released validity study.

This is not merely a software bug. It identifies a cross-domain benchmark primitive: each criterion needs a **signed semantic contract**:

```text
public basis
→ criterion proposition
→ polarity (desirable state or violation state)
→ applicability
→ authoritative evidence view
→ observer and threshold
→ dependencies/gates
→ contribution to score
→ licensed interpretation
```

A criterion's prose, sign, inversion flag, and aggregator must be mechanically checked for consistency. A richer judge cannot infer which layer is authoritative when the brief and hidden rubric conflict.

## Limitations and validity threats

### Expertise, content, and source validity

1. No task-level expert identity, qualification, role, contribution, approval, disagreement, or review lineage is released.
2. Author self-review and project-team review are permitted; independence is not guaranteed.
3. Verifiability-conditioned family selection omits legitimate but hard-to-grade creative work.
4. No production-work sampling frame, frequency/consequence weights, languages, regions, or recipient population support representativeness.
5. Video-AI-company experts are nearly half the pool, potentially weighting agent-system perspectives over broader production roles.
6. Publicly accessible media are not necessarily licensed media; release metadata provides no affirmative rights.
7. Team operationalization can change expert standards, but no before/after criterion lineage is visible.

### Task, artifact, and grader validity

8. Assembly exact picks can reject professionally equivalent clips; its cinematic variables are not independently validated.
9. Repair reference similarity can reward reference imitation while underweighting diagnosis/report correctness and alternate valid restorations.
10. Sequencing assumes one original narrative order is the only acceptable order.
11. Repurpose rubric count differs between paper and release (1,069 vs 1,137).
12. Thirteen released Repurpose tasks contain explicit brief/rubric resolution contradictions.
13. At least five good-state negative criteria lack the inversion flag and can penalize success.
14. Rubric criteria overlap heavily: motif presence, cold comprehension, causal order, arc, and turn can score the same evidence repeatedly.
15. Binary model judgments do not remove judgment; they shift ambiguity into evidence extraction and thresholds.
16. One-fps visual sampling can miss short events, transitions, sync drift, and wrong intervals.
17. Audio transcription and model listening do not establish mix/mastering or narrative quality without validated error rates.
18. No released human labels, confusion matrices, planted cases, calibration split, or abstention policy validates the later judges.
19. Oracle/broken anchors prove selected witnesses and endpoints, not verifier completeness over legitimate alternatives or adversarial outputs.
20. Hidden rubrics include obligations that can conflict with public briefs, violating public-basis fairness.

### Human/reference validity

21. Human subset size, task IDs, sampling, editor allocation, completion time, tools, invalids, and uncertainty are missing.
22. University film-program editors are not automatically equivalent to the 20 industry experts or a professional studio team.
23. Humans and agents use materially different tools and time regimes; identical scoring does not create treatment equivalence.
24. Raw 96.4–98.2% agreement lacks unit, prevalence, rater count, human–human reliability, holdout, and uncertainty.
25. The same recruitment pipeline supplies editors and graders, but authority, conflicts, and task familiarity are not reported.
26. “Valid proxy for expert rubric scoring” exceeds the published calibration evidence.

### Experimental and statistical validity

27. Model, provider, harness prompt, defaults, tools, sub-models, observation routing, planning, and retries vary together.
28. Within-model harness contrasts identify package differences, not specific harness mechanisms.
29. K=3 without task-clustered uncertainty cannot establish stable rankings or operational reliability.
30. Failed rollouts score zero, while missing token rows remain zero-cost; capability and cost missingness are treated differently.
31. The 6,770 cost-audit rows exceed the nominal 6,000 task rollouts by 770, entirely in non-Repurpose, without reconciliation.
32. Failure categories lack coding protocol and reliability.
33. Ablations are selected on top-five outcomes and bundle information/difficulty interventions.
34. Thirty-minute agent caps conflict with claimed human durations up to one week, changing the construct.
35. Family macro scores aggregate heterogeneous criterion counts, difficulty, duration, and observer types without a validated common scale.

### Operational realism and reproducibility

36. The exact paper-time code/data release is not pinned.
37. No trajectories, scores, human submissions, labels, or aggregation inputs reproduce v1 results.
38. Most media URLs and dependencies are mutable; 72/101 task Dockerfiles lack material checksums.
39. Rights and attribution are missing or explicitly unknown for every released task record.
40. Internet access permits source lookup despite prompt-only prohibitions.
41. Mutable proprietary APIs and managed sub-models prevent exact reruns.
42. The release's extra Understanding task and changed rubric/task surfaces show continuing suite evolution after v1.
43. No recipient acceptance, editability, delivery integration, safety, accessibility, or labor-outcome study supports readiness.

## Transfer to skill-bench

1. **Retain criterion-specific temporal observers.** Use native structure, manifests, rendered frame/audio windows, technical metadata, and expert views according to what each criterion can prove. Do not collapse them into one “artifact quality” score.
2. **Add a signed criterion conformance check to existing rubric machinery.** Validate public basis, proposition polarity, negative-weight semantics, inversion, dependencies, and aggregation. Plant brief/rubric conflicts and good-state-negative bugs; fail the instrument before any agent trial.
3. **Bind expert authority at task and criterion level.** Record author, reviewer, domain scope, transformation by project staff, approval state, disagreement, and expiration. “Expert-authored suite” is not enough.
4. **Treat source rights and immutability as execution validity.** Require origin, license/permission, attribution, transformation history, versioned URL, checksum, technical metadata, and a retrieval/access canary for every asset.
5. **Separate five claim rungs:** workflow provenance, executable task conformance, temporal artifact quality, professional acceptance, and deployment readiness. AgenticVBench supplies meaningful evidence mainly for the middle two.
6. **Make the human comparison an explicit instrument.** Publish selected task IDs, sampling probabilities, editor authority, tools, time, assignment, invalids, repeated grading, rater evidence views, agreement, adjudication, and uncertainty. Never label trained-student performance “expert” without qualification.
7. **Preserve a complete run ledger.** Reconcile task×system×repeat expectations with attempted, valid, agent-failed, environment-failed, judge-failed, retried, excluded, and scored rows before reporting cost or capability.
8. **Evaluate configured-system interventions experimentally.** A harness comparison should either hold prompt/tool/observation policies constant through adapters or manipulate one declared component; otherwise report package contrasts only.
9. **Calibrate model graders with planted temporal cases and alternate valid artifacts.** Include right frame/wrong interval, source-not-used, plausible render/wrong native state, correct alternate sequence, AV drift, title-only compliance, brief/rubric contradiction, and missing evidence.
10. **Keep this as a cross-domain validation case.** The existing artifact-view, criterion, task-health, validity, metric, participation, execution-isolation, and source-provenance machinery already has homes for these requirements. No media-specific subsystem is warranted.

## Concrete repository actions

1. Preserve `data/sources/releases/2605.27705v1-agenticvbench/release-audit.json` as the exact post-v1 audit record, especially the 101-task inventory, 1,137-item rubric census, source/license/checksum gaps, and 13 public/private resolution contradictions.
2. In the next criterion/rubric consolidation, add the signed semantic chain—public basis → proposition → polarity → applicability → observer → dependency → aggregation—and cite AgenticVBench's released defects as falsification evidence.
3. In the next temporal-artifact fixture, include one brief requiring 1280×720 while a private criterion demands 1920×1080, and one desirable criterion with negative weight but missing inversion; the validator must reject both before execution.
4. Keep AgenticVBench below professional-validity/capability/readiness tiers until task-level paper results, human subset records, grader labels, and rights/version manifests are available.
5. **No new queue task added.** Existing rubric/public-basis, artifact-view, expert-participation, task-health, validity, metric, source-provenance, and temporal-conformance work already covers the evidence-implied changes; another task would duplicate the queue.

## Assessment

**Evidence tier:** full immutable paper plus substantive post-v1 task/grader release; strong inspectability of later executable task conformance, weak correspondence to v1 empirical and human claims.

**Most reusable contribution:** combining rendered temporal outputs with manifests, source-relative checks, must-preserve regions, expert criteria, repeated configured-system trials, and cost accounting.

**Most serious finding:** the later release is executable enough to falsify its own instrument: 13 Repurpose briefs contradict hidden resolution checks, at least five desirable negative-weight criteria can penalize success, and no released human/calibration evidence repairs those defects.

**Safe claim for skill-bench:** richer temporal artifact views and expert-derived criteria materially improve diagnostic evaluation, but only a versioned, rights-aware, signed criterion contract with independent human calibration and reconciled trial denominators can support professional-quality or capability claims.
