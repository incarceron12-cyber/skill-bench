# Skill access is not identified expertise transfer: a small medical study exposes package, selection, and rater-noise boundaries

## Source and review status

**Deep review of the complete immutable primary source and timing-bounded linked package.** I read the full 16-page arXiv v1 paper, including the reproducibility supplement, four released aggregate CSVs, ethics/availability statements, and the complete local text extraction. I also inspected the author-linked medical-research-skills archive at the latest repository commit before v1 publication, including the task-matched PCD planner and representative endpoint, validation, differential-expression, and external-validation modules.

- **Paper:** Qianyu Yao et al., *Skill-Augmented AI Agents for Medical Research Analysis: An Exploratory Multi-Model Human Evaluation in an NSCLC Transcriptomic Biomarker Task*, arXiv:2606.11830v1 (10 June 2026), <https://arxiv.org/abs/2606.11830v1>
- **Local PDF:** `data/papers/pdfs/2606.11830v1-skill-augmented-medical-human-evaluation.pdf` (16 pages; SHA-256 `dd37aae91890db2f7aa0dc6035e92cf553ea041be78556da7d042c912b437d06`)
- **Full local text:** `data/papers/text/2606.11830v1-skill-augmented-medical-human-evaluation.txt` (48,831 bytes; SHA-256 `da46ab72ebe9d00eacefb58701e540bc9d2d02b3c40ce798b629229741746c68`)
- **Metadata:** `data/papers/source/2606.11830v1-metadata.xml` (SHA-256 `ed350911358d2f4bc84343a894a635aa62a096ebb066c4a746c92e9b68392df4`)
- **Source supplement and aggregate tables:** `data/papers/source/2606.11830v1/`
- **Linked repository:** <https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills>
- **Timing boundary:** latest repository commit at or before v1 publication `0d839a315d4d1e45219e943f2dab78d2e094cfc0`; subtree tree `3849d857cbbc869a6b3cadb67c7e02dd598ea830`
- **Local archive:** `data/sources/releases/2606.11830v1-medical-research-skills/aipoch-medical-research-skills-0d839a3.zip` (267,257,742 bytes; SHA-256 `39ec754110b2b3e93daf64a3ac8dccfeca6e185083478915b7f54fa04f49cb19`; 1,715 files; integrity passed)
- **Release provenance:** `data/sources/releases/2606.11830v1-medical-research-skills/provenance.json` (SHA-256 `7c819f2bc158e690dec79f0a6bf47fbc17a376fca1d75acdebb2872390a46513`)

The current linked subtree has the same tree hash as the pre-v1 boundary, but that establishes package stability only. The paper does not identify the executed repository commit, selected Skill IDs, mounted subset, routing decisions, opened files, script calls, outputs, platform version, or 21 run records. The archive is therefore **available-package evidence**, not execution correspondence.

## Why this matters for skill-bench

This study is unusually direct evidence about `skill-bench`'s central intervention question: does giving configured agents reusable procedural material improve a downstream work product as judged by humans? Its answer is not “yes, by 0.39 points.” Its real contribution is to expose the minimum causal and measurement chain that such a claim requires:

```text
package exists and is versioned
→ package is mounted in a pinned configured system
→ relevant module is surfaced/opened
→ procedure or executable is adopted correctly
→ artifact changes for the intended reason
→ qualified raters observe comparable evidence
→ ratings are sufficiently reliable for the contrast
→ independent correctness or consequence improves
→ effect transfers beyond the co-aligned task/package/rubric
→ professional fitness or readiness is established
```

The paper provides evidence for package availability, a reported mounted-versus-native strategy association, and noisy perceived-quality ratings. It does not observe the middle execution chain, independently verify biological correctness, or establish the later transfer and readiness rungs. This is cross-domain methodological evidence using biomedical research as a stress test, not a proposal to narrow `skill-bench` to medicine.

## One-sentence contribution and assessment

**Contribution:** The paper compares 9 native and 12 OpenClaw-plus-Skill outputs from six model backbones on one NSCLC transcriptomic planning task, obtains two blinded expert and two non-expert ratings per output, and reports a small directional expert overall-quality difference alongside very low expert agreement.

**Assessment:** The authors correctly call the result exploratory, but unequal model weighting across arms, an unpinned bundled treatment, unexplained output generation/selection, absent Skill-exposure traces and work products, coarse criterion-aligned ratings, unmodeled output/rater dependence, and no biological validation mean even the reported association is not a clean Skill effect; the strongest evidence is that the proposed primary human measure cannot resolve the claimed effect at this sample and calibration level.

## Research question and defensible claim boundary

The paper asks whether autonomous access to a medical research Skill package is associated with higher human-rated research-analysis quality than native model use, and whether the association differs by model backbone (Introduction and Sections 2.1–2.2, pp. 2–3).

The strongest defensible claim is:

> In 21 author-selected, reviewable artifacts from one task, generated under incompletely specified native and OpenClaw-plus-package configurations, the 12 Skill-arm outputs had a 0.39-point higher mean of two expert overall-quality ratings than the 9 native outputs; an output-level bootstrap interval crossed zero, model-balanced descriptive differences were heterogeneous, and single-rating expert ICC was negative.

This does **not** establish a causal Skill effect, correct routing or adoption, improvement from any named module, task-class transfer, expert-knowledge transfer, biological correctness, a valid biomarker, professional acceptability, production fitness, clinical utility, or readiness.

## Methodology and system

### Task and package

Every run receives the same broad prompt: use public transcriptomic data to construct a multi-gene immunotherapy-response signature for NSCLC and explore ferroptosis, cuproptosis, and pyroptosis in resistance. Requested components include dataset/cohort/endpoint choices, preprocessing, differential expression, screening, modeling, validation, immune analysis, interpretation, figures/tables, and manual review points. The “impact factor approximately 5” phrase is an informal completeness target, not an operational standard (Section 2.4, p. 3; Supplement S1, pp. 14–15).

The linked archive contains 141 `SKILL.md` files among 1,715 files: 246 Academic Writing, 666 Data Analysis, 302 Evidence Insight, 489 Protocol Design, and 12 Other files according to the timing-bounded manifest. Inspection confirms both procedural prompts and executable R modules. Representative examples include:

- `Protocol Design/pcd-immune-oncology-research-planner/SKILL.md`: an exact task-family match that requires a curated PCD theme, subtype/prognostic/immune/drug study patterns, Lite through Publication+ plans, dependency maps, validation tiers, figure plans, verified references, and a self-critical risk review. It explicitly distinguishes association, prognosis, and therapy-prediction claims and forbids treated-response claims without treated cohorts (lines 1–258 in the inspected pre-v1 blob).
- `Protocol Design/endpoint-definition-designer/SKILL.md`: requires operational endpoints, timing, capture sources, ambiguity checks, and clarification before completion (lines 1–281).
- `Protocol Design/validation-strategy-designer/SKILL.md`: separates internal, external, temporal, functional, and translational validation and prohibits blanket “validated” language (lines 1–276).
- `Data Analysis/differential-expression-analysis/SKILL.md`: exposes executable R code, input schemas, method choices, adjusted-p-value filtering, outputs, errors, and test data (lines 1–220).
- `Data Analysis/external-model-validation/SKILL.md`: requires a fixed signature and independent expression/survival cohort and emits risk, Kaplan–Meier, heatmap, and time-dependent ROC artifacts (lines 1–308).

This inspection changes interpretation in two ways. First, the intervention contains much more than generic “medical knowledge”: it combines task-matched output scaffolds, claim guardrails, references, scripts, test data, and mandatory sections. Second, the package includes an exact `pcd-immune-oncology-research-planner` whose scope closely matches the task and several expert rubric dimensions. The paper says PCD-specific gene sets or biomarkers were not independently validated in the deployed environment (Section 2.5, pp. 3–4), but it does not report whether this exact planner was available, routed, opened, or adopted in each output. Availability cannot be converted into exposure.

### Configured systems and intervention identity

Six product-level backbones are named: GPT-5.4, Claude Sonnet 4.6, GLM-5.1, DeepSeek-V4 Pro, Kimi K2.6, and MiniMax-M2.7. They were pragmatically selected rather than sampled (Section 2.2, p. 2). Native runs receive the task without the package; Skill runs use OpenClaw with autonomous package access (Sections 2.1 and 2.3, pp. 2–3).

This is not an isolated Skill treatment. At minimum the arm changes package content, OpenClaw orchestration, routing, context management, tool execution, and artifact production. The paper does not identify exact model endpoints/dates, OpenClaw version, package commit or mounted subset, system prompts, tool/network permissions, context policy, budgets, decoding, retries, failure handling, or feedback policy. Native platform/harness identity is also not specified. Thus `strategy` is a bundled configured-package contrast, not `Skill text present versus absent`.

No placebo context, irrelevant Skill, OpenClaw-without-Skills, fixed surfaced-module, procedural-only, executable-only, or cross-platform arm separates package content from extra context and platform effects. The authors appropriately propose irrelevant/placebo Skills and platform replication as future controls (Section 4.7, p. 11).

### Generation frame, selection, and evidence comparability

The final frame contains 21 outputs: every model has two Skill outputs, while GPT, DeepSeek, and MiniMax have two native outputs and Claude, GLM, and Kimi only one (Table S1, p. 15). “Repeated outputs generated during the final evaluation process were retained,” but the paper does not report attempted runs, why only the native arm is uneven, failed/nonreviewable counts, stopping rules, generation order, whether outputs were chosen before ratings, or whether all eligible artifacts were included (Sections 2.2–2.3, pp. 2–3).

Eligibility is deliberately broad: complete reports, partial reports, stage summaries, output files, and archived traces qualify if they contain sufficient task-relevant material (Supplement S2, p. 14). That preserves operational messiness but creates an evidence-view problem. A polished report, a trace, a script bundle, and a stage summary do not expose the same facts to a rater. The paper says full generated materials could include logs, tables, figures, scripts, and intermediate results (Section 4.6, p. 10), but it does not inventory which representation each output contained or require representation-matched grading. A condition effect can therefore include artifact-type and evidence-volume differences.

### Blinding and human review

Model names, families, strategy labels, platform configuration, and “obvious experimental cues” were removed and random IDs assigned (Section 2.6, p. 4). This is useful, but the treatment itself may leave recognizable cues: the task-matched PCD Skill mandates distinctive workload tiers, dependency/evidence maps, sections A–J, a dataset disclaimer, minimal executable version, publication upgrade path, and self-critical review. No reviewer condition-guess test, cue audit, or rewrite-normalization study assesses functional blinding.

Four biomedical-familiar but non-specialist reviewers each rate subsets; every output receives two non-expert ratings. Two experts rate all 21 outputs. The paper does not state expert qualifications, years, institutional independence, NSCLC/transcriptomics/biostatistics authority, recruitment, compensation, conflicts, training, calibration examples, rating order, washout, adjudication, or per-criterion authority. All authors are affiliated with AIPOCH, which also owns the linked package; the manuscript reports voluntary internal document evaluation but no separate conflict-of-interest or funding statement (title page and Section 6, p. 12). Blinding condition labels reduces expectancy but not organizational allegiance or rubric-author dependence.

Non-experts score clarity, completeness, credibility, feasibility/usability, workflow, and perceived risk. Experts score broad methodological components and overall quality. Supplement S3 provides only generic 1/4/7 anchors such as “very poor,” “partially acceptable,” and “excellent,” not criterion-specific decision boundaries or examples (pp. 15–16). Many requested task components and Skill-mandated sections overlap the expert instrument. This is suitable for perceived completeness and rubric conformance, but weak for distinguishing methodologically necessary content from Skill-induced elaboration.

### Analysis and dependence

The primary unit is an output after averaging the two ratings of each reviewer type. Strategy comparisons use Welch tests, Mann–Whitney tests, and nonparametric bootstrap intervals over outputs. Model-level deltas average within model-strategy cells but are called descriptive. Expert ICC uses a two-way absolute-agreement model; non-expert ICC uses one-way random effects because assignments are incompletely crossed. Five strategy outcomes and six model contrasts receive no multiplicity adjustment (Section 2.8, pp. 4–5).

Three design problems remain:

1. **Unequal model composition.** Skill means weight each of six models equally because every model has two outputs. Native means overweight GPT, DeepSeek, and MiniMax because they have two outputs, while Claude, GLM, and Kimi have one. The 0.39 raw arm contrast is therefore partly a model-mixture contrast. Recomputing the mean of the six released model-specific expert deltas gives `0.33`, and unweighted model means are `5.17` native versus `5.50` Skill. This is still descriptive—not a corrected causal estimate—but shows that the headline estimand changes with model weighting.
2. **Output independence is assumed rather than modeled.** Runs share backbone, task, package, prompt, and likely provider/platform state. Two runs in one cell do not create independent task replications. Resampling 21 outputs ignores model clustering and cannot estimate transfer beyond this one task. With six backbone clusters and one task, robust inference is intrinsically weak.
3. **Averaging does not solve rater error.** Both experts rate all outputs, so averaging retains any rater severity, criterion interpretation, and condition-cue effects. The analysis does not model rater × condition, rater × model, order, or criterion interactions. Negative ICC is not fixed by treating the average as a stable latent score.

## Evidence and results

### Primary and secondary associations

The released aggregate table reports:

| Outcome | Native mean | Skill mean | Difference | Output-bootstrap 95% CI |
|---|---:|---:|---:|---:|
| Expert overall quality | 5.11 | 5.50 | +0.39 | −0.04 to 0.90 |
| Expert methodological quality | 4.79 | 5.26 | +0.47 | 0.12 to 0.95 |
| Non-expert quality | 4.47 | 4.72 | +0.26 | −0.25 to 0.80 |
| Non-expert workflow | 4.71 | 5.03 | +0.32 | −0.10 to 0.70 |
| Non-expert perceived risk | 4.93 | 4.63 | −0.30 | −1.02 to 0.42 |

For the primary expert overall measure, Welch `p=0.156` and Mann–Whitney `p=0.150`; for non-expert quality, `p=0.373` and `0.355` (Section 3.2, pp. 5–7). The positive methodological-quality interval is one unadjusted secondary contrast among several, under the same dependence and model-mixture problems. It is hypothesis generation, not a rescued confirmatory result.

The released model-specific expert deltas are `+1.25` GPT, `−0.25` Claude, `+0.50` GLM, `+0.25` DeepSeek, `0.00` Kimi, and `+0.25` MiniMax. Cells contain only one or two native and two Skill outputs. They show heterogeneity in this tiny artifact set, not backbone-specific treatment effects. Kimi's `+1.68` non-expert versus `0.00` expert delta is consistent with presentation/completeness changing without expert-recognized improvement, but one model cell cannot identify that mechanism.

### Reliability is the central empirical result

For expert overall quality, single-rating ICC is `−0.153`, average-rating ICC `−0.360`, and mean absolute expert difference `0.67`; maximum absolute difference is `5.0`. For expert methodological quality, ICCs are `0.016` and `0.032`, mean absolute difference `0.54`, maximum `4.23`. Non-expert one-way ICCs are `0.11` quality, `0.03` workflow, and `0.45` perceived risk (`reviewer_agreement_icc.csv`; Section 3.3, p. 7).

The paper correctly notes that negative ICC can arise when between-output variance is small relative to disagreement. But the implication is stronger than “the 0.39 signal is smaller than the 0.67 mean absolute difference.” A negative single- and average-rating ICC means this rater/instrument/sample combination does not furnish a defensible stable output ranking. Absolute disagreement and treatment-effect magnitude are not commensurate estimators, so their numerical comparison is intuitive rather than a formal noise correction. The needed follow-up is a crossed, calibrated, criterion-specific model with more qualified raters and adjudicated cases—not merely more outputs under the same instrument.

### What the released artifacts reproduce

The source package releases model-strategy counts, five aggregate arm contrasts and bootstrap bounds, six model-level tables, and ICC summaries. These permit table-level consistency checks and the model-balanced calculation above. They do **not** release:

- the 21 work products or representation inventories;
- anonymous output-to-condition/model mapping;
- per-output item ratings or raw rater assignments;
- exact rating forms and criterion item text beyond manuscript descriptions;
- bootstrap/test code, resamples, seeds, or output-level scores;
- generation attempts, failed runs, stopping/selection logs;
- prompts/configurations beyond the user task;
- Skill exposure, routing, tool, trace, cost, or execution records.

Calling the study reproducible at the level of “anonymized output IDs” overstates the release: the supplement says such IDs were used, but does not provide the complete mapping/archive (Supplement S2 and S5, pp. 14–16). The displayed aggregates are partially auditable; the experiment and primary analysis are not independently replayable.

## Unique insight for skill-bench

> **When a procedural package and a human rubric both reward methodological completeness, an observed score lift can arise at four different boundaries—routing, elaboration, correctness, or rater cueing—and a final Likert mean cannot distinguish them.**

This paper adds a missing human-measurement layer to the existing package-efficacy evidence:

1. **Package availability:** a task-relevant Skill exists in the mounted release.
2. **Exposure/routing:** the configured agent surfaced and consumed it.
3. **Adoption:** prescribed decisions or scripts changed the trajectory/artifact.
4. **Criterion conformance:** the output displays rubric-recognizable structure.
5. **Substantive correctness:** cohort, endpoints, methods, gene sets, statistics, and claims are valid.
6. **Independent transfer:** correctness persists on held-out tasks and independently authored criteria.
7. **Consequence/readiness:** qualified stakeholders can use the work safely under a declared threshold.

The study measures an unresolved mixture near rung 4. The exact PCD planner strongly predicts criterion-visible structure—validation sections, dependency maps, limitations, workflows, and figures—while the paper explicitly does not verify PCD gene sets, biomarkers, cohort labels, or biological plausibility (Sections 2.5 and 4.4, pp. 3–4 and 9–10). Therefore a better perceived-quality score can be genuine useful scaffolding and still fail to demonstrate biomedical expertise.

A second insight is that **rater reliability is part of treatment-effect identifiability, not a postscript.** If the observer does not provide stable distinctions among outputs, increasing agent repetitions alone cannot validate the intervention. Trial planning must allocate replication across tasks, agent runs, and raters based on a declared generalization design; it must also decide whether disagreement is noise, framework plurality, criterion ambiguity, or evidence-view insufficiency.

A third insight is that **arm balance must be defined at the estimand level.** Equal output counts are not enough when model composition differs. For a configured-system portfolio effect, freeze model weights. For a per-model package effect, pair within model and aggregate model-level deltas under declared weights. For a general Skill effect, sample independent tasks and packages—the absent dimension here.

## Comparison with adjacent skill-bench evidence

- **SkillsBench:** provides far broader matched package efficacy with repeated deterministic trials, but deliberately enriches for Skill-responsive, task–Skill–verifier-co-designed packages. The medical study avoids deterministic-only quality claims and adds human review, yet has one task, 21 selected outputs, no exposure trace, no fixed harness control, and unreliable ratings. Both support package-level observations; neither alone establishes class transfer or portfolio value.
- **LH-Bench:** shows how expert procedures become observable workflow boundaries and separates process, artifact, and preference, while warning that disclosed Skills can become evaluator cues. The medical rubric remains coarse and the task-matched planner mandates many rewarded structures; a public-skill × independent/shared-rubric design is needed to separate procedural assistance from criterion compliance.
- **Industrial expertise codification:** reports large gains on five co-designed outputs but has no reliability estimate. The medical study's much smaller gain and negative ICC make the same authorship/criterion-overlap problem visible rather than hiding it behind a top-category average. Both need held-out incidents, component ablations, independent criteria, and expert-equivalence margins before “expertise transfer.”
- **Vibe Calibration:** demonstrates physical execution and checkpointed rollback under a highly bundled distilled package, but does not isolate tacit transfer. The medical study sits at the opposite end: subjective plans rather than physical consequences. Together they argue for joint evidence: exposure/adoption traces plus independent outcome predicates, not either final execution or perceived polish alone.
- **Many-facet human/AI rater effects:** shows that agreement, severity, fit, and decision validity are distinct. Here two experts are fully crossed but too few and insufficiently calibrated to identify a stable quality scale; non-experts are incompletely crossed. Future analysis should estimate rater × criterion × task-family effects and preserve panel-relative estimates rather than average disagreement away.
- **Intervention/instrument separation:** the task, task-matched planner, and expert criteria share content such as endpoints, preprocessing, validation, immune analysis, feasibility, and limitations. This is legitimate package-conformance evidence but not independent expertise evidence. Intervention and instrument versions, authorship, shared source lineage, and exact disclosure must remain separate.

## Limitations and validity threats

1. One biomedical task, disease family, data modality, package collection, and organization.
2. Only 21 reviewable outputs; no prospective sample-size or precision design.
3. Unequal native counts make the raw arm contrast partly a model-composition contrast.
4. One or two outputs per model-condition cell cannot estimate stochastic or model-specific effects.
5. One task provides no task-level replication or generalization frame.
6. Native versus Skill arms also differ in OpenClaw orchestration and possibly tools, context, and artifact behavior.
7. Exact model endpoints, dates, harnesses, package commit/subset, prompts, settings, budgets, retries, and feedback policies are absent.
8. No OpenClaw-without-Skill, placebo-context, irrelevant-Skill, fixed-routing, or component arm.
9. The total attempted-run frame, stopping rule, exclusions, failures, and selection timing are missing.
10. “Reviewable” allows non-equivalent representations such as reports, summaries, files, and traces.
11. No per-output artifact/evidence-view inventory establishes comparability.
12. No Skill exposure chain records availability, surfacing, opening, invocation, adoption, or verified consequence.
13. The exact task-matched PCD planner creates strong intervention–task alignment but is not named or traced in executions.
14. The package combines procedural text, scripts, references, test data, and extra context; its active ingredients are unidentified.
15. Blinding may be penetrable through mandatory Skill structure; reviewer condition guesses were not collected.
16. Expert qualifications, criterion-specific authority, recruitment, independence, compensation, training, and calibration are not reported.
17. All authors and the package are affiliated with AIPOCH; no standalone competing-interest/funding disclosure is provided.
18. Generic 1/4/7 anchors do not operationalize complex methodological decisions.
19. Expert overall and methodological ICCs are approximately zero or negative.
20. Non-expert assignments are incompletely crossed and have low quality/workflow ICCs.
21. Averaging two ratings does not model rater severity, rater × condition, order, or framework differences.
22. Output-level tests/bootstrap ignore backbone clustering and shared task/package dependence.
23. Secondary methodological quality has a positive unadjusted interval amid multiple exploratory outcomes.
24. No multiplicity adjustment covers five arm summaries and six model contrasts.
25. Ordinal Likert means, Cohen's `d`, and Welch tests assume scale properties not justified by anchors.
26. The 0.67 disagreement-versus-0.39 effect comparison is descriptive, not a formal measurement-error analysis.
27. No independent deterministic checks audit dataset suitability, endpoint consistency, sample leakage, preprocessing, code execution, or statistical validity.
28. No mechanism-specific gene-set, biomarker, external-cohort, functional, or clinical validation exists.
29. The 21 outputs, raw ratings, exact forms, analysis code, and execution traces are unavailable.
30. Aggregate CSVs reproduce displayed summaries but cannot replay selection, scoring, tests, or bootstrap.
31. Costs, latency, failures, human-review burden, and operational maintenance are unreported.
32. One scenario cannot support disease, modality, workflow, institution, platform, or domain transfer.
33. No expert baseline under matched time/tools establishes equivalence or readiness.
34. Voluntary internal review is reported without institution-specific ethics approval; participant consent/use/withdrawal detail is limited.
35. The work evaluates plans and materials, not executed analyses, validated biomarkers, decisions, or patient outcomes.

## Reproducibility and operational realism

Paper-level reproducibility is moderate: immutable PDF/text/metadata, exact user task, output counts, broad inclusion rules, generic anchors, four aggregate CSVs, and a stable linked package are preserved. Package inspectability is strong—the timing-bounded archive contains source, scripts, references, tests, and exact task-family modules.

Experimental reproducibility is poor. The package commit actually executed is unknown; OpenClaw and native configurations are unpinned; generated materials and raw ratings are withheld; selection and run histories are absent; and aggregate analysis code is not supplied. A reader can inspect what an agent might have used and verify displayed aggregate values, but cannot reconstruct what any agent saw or did, rerun a configuration, validate an artifact, or reproduce the statistical estimates from raw observations.

Operational realism is mixed. Strengths include multiple providers, autonomous routing, partial/nonstandard outputs, human review of reports/logs/scripts, and a realistic methodological task. Weaknesses include one internally authored scenario, no frozen run protocol, no execution correspondence, no cost/failure accounting, no independent biological checks, no stakeholder decision, and no consequential use. The study is best classified as a formative human-rating pilot, not a benchmark validation or deployment evaluation.

## Transfer to skill-bench: concrete benchmark changes

### 1. Require a Skill-treatment exposure and adoption record

For every Skill arm, preserve:

```text
package/version/hash and mounted subset
→ router candidate set and scores
→ surfaced/opened modules and spans
→ scripts/resources invoked with inputs/outputs
→ prescribed decision instantiated or rejected
→ artifact/trace consequence
→ independent check or reviewer evidence
```

A no-Skill/Skill difference without this chain is a configured-package association. It cannot diagnose routing, comprehension, execution, or procedure quality.

### 2. Freeze a factorial configured-system contrast

At minimum compare, under the same model/harness/tools/budget:

1. no package;
2. length-matched irrelevant/placebo package;
3. task-relevant procedural guidance without executables;
4. task-relevant executables without the full guidance scaffold where meaningful;
5. full package.

Cross this with an independently authored criterion set and a shared-source criterion set. Platform replication should use the same package bytes and declared surfacing policy, not a nominally similar integration.

### 3. Balance and preregister the estimand

Freeze attempted runs, eligibility, retries, stopping, model/task weights, invalid-environment policy, and all retained artifacts before ratings. Use within-model paired task contrasts, then aggregate under declared portfolio weights. Replicate over independent tasks/equivalent forms before making class-transfer claims. Bootstrap the generalization unit—tasks for task transfer, models for model portfolios—not raw ratings or repeated outputs.

### 4. Separate criterion-visible quality from substantive outcomes

Maintain distinct score families for:

- presentation/completeness;
- workflow/procedure conformance;
- deterministic data/code/statistical predicates;
- qualified expert methodological judgment;
- biological/domain correctness;
- artifact readiness and downstream consequence.

For a biomedical-style pilot, plant auditable cases such as endpoint/cohort mismatch, train/test leakage, wrong expression-data method, unverified gene-set provenance, unstable feature selection, absent external validation, and therapy claims unsupported by treated cohorts. A polished dependency map should not compensate for these failures.

### 5. Design rater evidence before scaling trials

Use at least a connected, criterion-authority-aware assignment with multiple qualified raters, calibration examples, blinded repeats, condition-guess checks, and adjudication records. Estimate criterion-specific agreement, severity, interactions, and decision consistency. Pilot the instrument first and revise ambiguous criteria before spending on agent repetitions. Preserve disagreements as evidence; do not overwrite them with an average.

### 6. Keep the claim ladder explicit

A validity argument should prohibit upgrades across:

`package available → exposed → adopted → criterion conformance → substantive correctness → held-out transfer → professional validity → production fitness → readiness`.

Each promotion requires its own immutable evidence and generalization boundary. In particular, a higher human quality mean cannot substitute for biological correctness or expert-equivalence evidence.

## Action items

- [x] Read the complete immutable v1 PDF/text, supplement, ethics/availability statements, and all four released CSVs.
- [x] Inspect the complete timing-bounded package manifest and representative task-matched procedural/executable modules.
- [x] Preserve exact source, package, tree, path, page/section, and hash provenance.
- [x] Reconstruct the 21-output matrix, reviewer design, analysis, dependence, and release boundary.
- [x] Recompute the model-balanced descriptive expert delta (`+0.33`) from released model-level values and distinguish it from the raw `+0.39` arm contrast.
- [x] Compare nonduplicatively with LH-Bench, SkillsBench, industrial codification, Vibe Calibration, many-facet rater effects, and intervention/instrument separation.
- [x] Add no new queue task: the requirements refine existing configured-system, procedural-skill, trace/exposure, validity, task-health, metric, participation, and rater-calibration machinery rather than justify medical-specific infrastructure.
