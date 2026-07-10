# Paper Review: GDPval — Occupational Breadth Is Not Yet Occupational Validity

- **Paper:** https://arxiv.org/abs/2510.04374v1
- **Authors:** Tejal Patwardhan, Rachel Dias, Elizabeth Proehl, Grace Kim, Michele Wang, Olivia Watkins, Simón Posada Fishman, Marwan Aljubeh, Phoebe Thacker, Laurance Fauconnet, Natalie S. Kim, Patrick Chao, Samuel Miserendino, Gildas Chabot, David Li, Michael Sharman, Alexandra Barr, Amelia Glaese, and Jerry Tworek
- **Affiliation:** OpenAI
- **Date read:** 2026-07-10
- **Source:** immutable arXiv v1 dated 5 October 2025
- **Tags:** occupational-sampling, expert-authored-tasks, multimodal-artifacts, pairwise-grading, economic-validity, human-baseline, cost-modeling
- **Local PDF:** `data/papers/pdfs/2510.04374v1-gdpval-evaluating-ai-model-performance-real-world-economically-valuable-tasks.pdf` (29 pages; SHA-256 `a04cca8451c486d871f8d2c6c57b8bc03b45daf1b5b0269146929bc8bf688dec`)
- **Local text:** `data/papers/text/2510.04374v1-gdpval-evaluating-ai-model-performance-real-world-economically-valuable-tasks.txt` (SHA-256 `92a03a19512a851c1f2824bb707d36ff96f338b039e55e9b0e2b46a72bc0edbb`)
- **Official dataset:** https://huggingface.co/datasets/openai/gdpval at revision `11e7900cdcac61bc4daf59e65feb238acda98fbf`; provenance `data/sources/releases/2510.04374v1-gdpval/provenance.json`
- **Local release evidence:** `data/sources/releases/2510.04374v1-gdpval/tasks.jsonl` (220 rows; SHA-256 `2bf53b4c2d811ed3bae8ec6f14533e03b3ae96b60d221746f3f7258e50da70c4`), complete pinned tree manifest, dataset card, and one complete spreadsheet reference/deliverable pair. The remaining approximately 2.29 GB binary corpus was not mirrored locally; exact pinned object metadata and URLs are retained. The pinned release revision postdates arXiv v1 and is release evidence, not the exact paper-time corpus.

## One-sentence contribution

GDPval constructs 1,320 one-shot, file-rich tasks from experienced professionals across 44 high-wage, predominantly digital occupations in nine large U.S. sectors, evaluates configured frontier systems against one human deliverable through occupation-matched pairwise judgments, and releases a 220-task equal-per-occupation subset whose breadth is unusually useful but whose scores do not by themselves identify occupational capability, expert parity, economic value, or augmentation benefit.

## Why this matters for skill-bench

This review advances charter objectives A, B, E, and F. GDPval is the closest reviewed primary source to the charter's broad knowledge-work ambition: it begins with sectors and occupations rather than one artifact type, pays professionals to transform work experience into multimodal tasks, preserves human work products, and uses occupational experts for subjective artifact comparison. The concrete evidence is the full paper, complete public metadata and rubric corpus, pinned file tree, and a structurally inspected spreadsheet pair.

The uncertainty clarified is where **portfolio breadth ends and validity begins**. GDPval establishes that broad professional task acquisition is operationally possible. It does not establish that five or thirty selected tasks represent an occupation, that an equally weighted occupation macro-average measures economic exposure, that one submitted human artifact is an expert ceiling, or that a pairwise preference can be substituted for task acceptability in a workflow cost model.

This is expansion and human learning with direct consolidation value, not a proposal to adopt GDP weighting or to narrow `skill-bench` to U.S. digital work. Useful completion means preserving GDPval's strong acquisition patterns while preventing sector labels, expert credentials, human comparisons, and wage multipliers from laundering a task sample into a labor-market claim.

## Research question and claim ladder

The paper asks whether model capability on “real-world economically valuable tasks” can provide an earlier signal of potential economic impact than observed adoption or productivity. Its operational answer is a chain:

```text
large-GDP sectors
→ high-total-wage, predominantly digital occupations
→ expert-authored and reviewed self-contained tasks
→ model and one human deliverable
→ occupation-matched pairwise preference
→ model-versus-human win rate
→ stylized speed/cost scenarios
→ potential economic impact
```

The first five links are partially instantiated. The later links are progressively less supported. A score licenses a claim about configured systems on selected, one-shot GDPval tasks under the observed judging protocol. It does not alone license occupation-level replacement, economy-wide value, deployment readiness, or realized productivity.

## Methodology and system

### 1. Sector and occupation frame

GDPval selects nine sectors above 5% of Q2 2024 U.S. GDP, then aims to select five occupations per sector with high total compensation and predominantly digital work (paper pp. 2–3, 24–29). Occupations are assigned to the sector employing the largest share of that occupation. Total wages are employment multiplied by mean annual wage (or hourly wage times 2,080 hours). A GPT-4o classifier labels O*NET tasks digital/non-digital; task relevance, importance, and frequency are normalized and averaged, and occupations above a 0.60 weighted digital share are eligible. Missing task ratings are imputed within occupation or replaced by task-frequency proxies (paper pp. 24–27).

This is a principled **frame construction**, not probability sampling of work. It excludes sectors below 5%, physical/manual activity, proprietary-tool work, communication, substantial tacit knowledge, and sensitive real context. It also favors occupations with large aggregate payroll rather than high marginal consequence, public value, scarcity, or automation exposure. Retail contributes only four released occupations, yielding 44 rather than 45 total; the paper does not explain this departure in the main selection rule.

The comparison to Acemoglu–Autor task-content measures is convergent evidence that the digital classifier tracks cognitive/nonmanual occupational content (paper pp. 27–28). It does not validate the 0.60 threshold, GPT-4o's task labels, or GDPval task representativeness.

### 2. Expert recruitment and task authoring

Task authors need at least four years in the occupation, a strong resume, video interview, background check, training, and quiz; selected contributors average 14 years, fewer than 10% of applicants are accepted, and each occupation has at least five professionals (paper pp. 3, 20). Compensation is described only as “well compensated.” No counts by author/reviewer role, geography, seniority, employer type, demographics, rejection reason, pay rate, hours, consent terms, ownership, or attrition are reported.

Experts author a request, optional references, and a deliverable based on professional experience, map it to O*NET occupational tasks, and rate difficulty, representativeness, completion time, and quality. Model screening flags scope and completeness concerns but does not alter tasks. Human review has at least three stages: general requirements, occupation-specific feasibility/representativeness, and iterative feedback; each task receives at least three and on average five reviews (paper pp. 3–4, 20–21).

Review authority is real but not independent. High-performing authors are selected by researchers and promoted into reviewer and lead-reviewer roles from the same pool. The paper reports no independent initial ratings, disagreement ledger, inter-reviewer reliability, reviewer blinding, or held-out external occupational audit. Post-revision mean quality (4.55/5) and representativeness (4.43/5) describe the surviving curated corpus; they cannot estimate initial quality, defect-detection sensitivity, or population representativeness (paper p. 19).

### 3. Task and artifact structure

The full set has 30 tasks per occupation; the public gold subset has five, for 1,320 and 220 tasks respectively. The gold subset reports 208 O*NET task statements, 25 of 35 skills, and 26 of 41 general work activities, while only 14.15% of the 1,470 listed occupation-specific O*NET tasks appear (paper pp. 2, 19). Most tasks involve several labels, so counts are neither a sampling distribution nor evidence that high-frequency work is proportionately represented. The paper does not disclose the gold-subset selection mechanism, exclusions, seed, stratification, difficulty balancing, or relationship to model outcomes.

Tasks average 9.49 self-reported hours in gold and 8.63 in full; distributions are strongly right-skewed (gold max 100 hours; full max 605). Reviewers validate estimates, but no instrument, raw estimates, corrections, or agreement is released (paper pp. 12, 19). Tasks are self-contained, precisely specified, one-shot digital deliverables, explicitly excluding many context-discovery, interaction, tacit, proprietary, and communication demands (paper pp. 8–9). The under-contextualized ablation shortens prompts to 42% of original length and lowers GPT-5 performance, but uses an earlier gold version and confounds removal of realistic ambiguity with removal of task-relevant instructions, locations, and formatting expectations (paper pp. 16–17).

### 4. Human and model evaluation

For gold tasks, additional occupation-matched experts compare unlabeled human and model deliverables given the request and references. Each model has three completions per task and each completion receives three human grades: nine comparisons per prompt/model (paper pp. 4–6). Grading averages 109 minutes for a first grade. Judges provide rationales; model failure rationales are clustered, and a separate audit rates GPT-5 losses as catastrophic, bad, acceptable-but-subpar, or an original-judge disagreement (paper pp. 7, 12, 16).

The evaluated object is a configured package, not a base model. OpenAI models receive web search, code interpreter, extra packages, background sampling, and an OpenAI production container. Claude is sampled through its UI specifically to enable upgraded file-creation features. Prompts are shared only imperfectly, harnesses differ, and costs are unavailable for Claude, Gemini, and Grok (paper pp. 5–6, 22–23). These choices are defensible for package evaluation but do not isolate model effects.

Blinding is incomplete: characteristic phrasing and self-identification may reveal origin (paper p. 5). More importantly, a “human” arm is one task deliverable, not a sampled distribution of expert work. Pairwise preference against that artifact mixes system quality, human-author quality, stylistic match, judge preference, and task-specific reference quality. A model win does not establish that it meets a professional acceptance threshold; a human win does not establish that the model is unusable.

### 5. Automated grader

The experimental GPT-5-high grader assigns model win/tie/loss and reports 65.7% agreement with humans versus 70.8% human inter-rater agreement. Agreement is `1 - |score difference|` over {0, .5, 1}, so adjacent disagreement receives half credit; no chance correction, class-balanced result, calibration curve, occupation-level reliability, or equivalence/noninferiority test is supplied (paper pp. 21–22). The five-point gap is therefore not evidence that the grader substitutes for experts.

The estimate excludes system errors, invalid grader outputs, and 12 of 220 tasks that are difficult for the grader because of internet, non-Python execution, fonts, or audio (paper pp. 21–22). This is outcome/feasibility-conditioned evidence over the easier-to-observe subset. Agreement is also lower on capable OpenAI outputs, consistent with self-preference risk, so average agreement is not transportable across model mixtures.

### 6. Speed and cost model

Human completion time is validated self-report; human cost is time times occupation median wage. Model time/cost comes from three API samples. Review cost is observed first-grade time times median wage. The paper plugs pairwise model win rate into “try once, then redo” and repeated-resampling formulas (paper pp. 12–13).

This is a scenario calculation, not an observed augmentation experiment. It treats “beats one human artifact in pairwise preference” as the probability that an expert accepts an output, assumes repeated samples have a stationary independent success probability, assumes review identifies acceptability without error, and equates rejection with doing all work from scratch. It omits integration, prompting, correction, verification, organizational overhead, correlated failures, catastrophic loss, and the quality distribution of ordinary human work. Median wages underprice the deliberately senior recruited experts, as the authors note. The resulting speed/cost ratios are useful sensitivity inputs, not estimates of realized savings or replacement value.

## Public release inspection

The pinned 2026 dataset revision contains exactly five tasks per occupation and 20 retail tasks. All 220 metadata rows were parsed. The release has 261 reference paths and 248 expert-deliverable paths, all present in the 552-file pinned tree; 95 tasks have no reference file and 35 have no released deliverable file. The complete binary corpus is approximately 2.29 GB and was not mirrored, so this review does not claim artifact-level inspection of every task.

The metadata contains 10,453 human-authored rubric items—14 to 137 per task, mean 47.51—with signed weights from -85 to +20. All `required`, `read_only`, and optional `form_content` fields are null; tags are heterogeneous (`true`, `false`, `baseline`, `content`, `tools`, `mgmt_pref`, and combinations). These are rich task-specific criteria, but the paper does not document their authoring, revision, intended semantics, dependence, normalization, grader access, or relationship to the headline pairwise judgments. A sum of criteria would overweight tasks with more items unless explicitly normalized, and correlated microcriteria can multiply one underlying requirement.

The paper says it open-sources prompts and references (paper p. 8), while the later pinned release also exposes expert deliverable paths and 10,453 rubric criteria. That is a release expansion, not a contradiction attributed to paper-time v1. It creates a clear contamination boundary: public human artifacts and rubrics are valuable for audit and grader research but cannot remain private evaluation targets.

The inspected accountant task makes the task structure concrete. Its reference workbook has 1,517 data rows and eight columns; the expert workbook has ten columns and a second calculation sheet. The deliverable contains quarter-on-quarter formulas, marked sample rows, and a sheet recording 90% confidence, 10% error, and sample size 65. This verifies readable cross-artifact structure, not correctness or professional quality. Its 38 rubric items include exact file/sheet conventions, formulas, row identity, selection consequences, and formatting—precisely the requirement→affordance→witness→check lineage `skill-bench` needs.

No license declaration appears in the pinned dataset card/API metadata. Public accessibility must not be treated as permission for unrestricted redistribution or derivative benchmark release.

## Evidence and what it supports

**Strongly supported:**

1. OpenAI operationalized a broad occupational acquisition program with experienced contributors, repeated review, 1,320 task packages, multimodal references, and human artifacts.
2. The public gold metadata spans 44 occupations and nine sectors with equal five-task cells and unusually diverse file types.
3. Under the reported configured systems and pairwise protocol, frontier model packages often produce artifacts that some occupational judges prefer to the single human reference; performance is heterogeneous by task, occupation, sector, duration, and format.
4. Scaffold changes that mandate rendering/inspection materially changed behavior: visual inspection rose from 15% to 97%, black-square PDF artifacts disappeared, and reported human preference improved five percentage points (paper p. 7). This supports verification scaffolding as a treatment worth testing.

**Partially supported:**

- Occupational content authenticity: credentials, reviews, O*NET mapping, and post-review ratings are meaningful content evidence, but there is no sampled work diary, employer validation, independent reviewer reliability, or task-frequency weighting.
- Human-relative artifact quality: repeated pairwise ratings provide comparative evidence, but only against one human artifact and without a professional acceptability threshold.
- Automated-grader utility: moderate agreement suggests triage potential, not expert equivalence or unbiased population scoring.

**Not supported by v1:**

- “Expert parity” as equivalence to an expert population. The headline 47.6% wins-or-ties and “just over half the tasks” wording on paper p. 6 is itself difficult to reconcile from extracted text, and neither formulation is a parity test.
- Occupation-level capability, because five gold or thirty full tasks are not shown to estimate each occupation's work distribution.
- Economic representativeness, because occupation selection uses GDP/payroll while score aggregation and task allocation are equal-cell, not employment-, wage-, time-, frequency-, or consequence-weighted.
- Augmentation savings, because no human-plus-model workflow was run.
- Deployment readiness, safety, or substitution, because one-shot artifacts omit interaction, proprietary systems, tacit context, communication, and consequential use.

## Unique insight

GDPval's distinctive lesson is that **breadth has at least four different denominators**:

1. **frame breadth:** which sectors and occupations are eligible;
2. **content breadth:** which work activities and task families are represented;
3. **assembly breadth:** how tasks are sampled and weighted in the administered suite;
4. **inference breadth:** which worker, occupation, economic, or deployment population the result claims to describe.

GDPval is strong on frame breadth and artifact diversity, weaker on content-frequency evidence, undocumented on gold assembly, and too broad in some interpretive language. `skill-bench` should never allow a broad list of professions to stand in for a defensible sampling distribution.

A second insight is that the human artifact and the human judge play different roles. The task author supplies one witness; the grader supplies a preference observation; neither is an expert-population upper bound. Human-relative evaluation should record witness provenance and quality, judge evidence view, acceptability thresholds, and disagreement separately.

A third insight is that occupational value cannot be appended after scoring. GDP share, aggregate wages, task duration, and median wage describe different estimands. If an evaluation wants a “share of work,” “value exposed,” or “augmentation savings” claim, task-frequency weights, worker/population weights, quality thresholds, review/correction policies, dependence, and loss from errors must be designed before assembly—not multiplied onto an equal-cell average afterward.

## Limitations

1. **Convenience within a principled frame.** Sector and occupation selection is top-down, but task authoring is not probability sampling from occupational work.
2. **Equal task quotas.** Thirty/full and five/gold tasks per occupation ignore occupational size and within-occupation task frequency.
3. **Unreported gold selection.** The paper does not explain which five tasks survive, why, or whether outcomes informed selection.
4. **Restricted construct.** Self-contained digital artifact production excludes many central professional activities and tacit/contextual demands.
5. **Single human witness.** Model scores are relative to one submitted artifact, not an expert-performance distribution or minimum standard.
6. **Incomplete blinding and harness asymmetry.** Style can reveal systems, and tool/UI/container conditions differ.
7. **Nested dependence.** Three samples and three ratings per task are not independent tasks; no task/occupation-clustered uncertainty is reported in text.
8. **Weak human reliability reporting.** The ordinal agreement statistic is not chance-corrected and no occupation/task/rater variance decomposition is given.
9. **Automated-grader selection.** Invalid/system outputs and 12 difficult tasks are excluded; model-family bias varies.
10. **Rubric process absent from paper.** The later release's 10,453 criteria lack documented provenance, dependence, calibration, and aggregation semantics.
11. **Post-selection quality ratings.** High ratings after iterative revision do not measure reviewer accuracy or coverage.
12. **Self-reported time.** Extreme right tails and unknown validation changes make duration/value estimates uncertain.
13. **Wage is not task value.** Median wages omit overhead, seniority, consequence, consumer surplus, and output quality.
14. **No augmentation trial.** Cost equations substitute pairwise preference for acceptance and assume repeated independent attempts.
15. **No catastrophic-loss model.** The paper explicitly omits disproportionate costs despite identifying catastrophic outputs.
16. **No contributor economics.** Recruitment conversion is reported, but compensation, time by role, retention, and cost per released task are absent.
17. **No consent/ownership lineage.** Privacy scrubbing and image permissions are discussed, but contributor purpose, withdrawal, attribution, and transformation rights are not.
18. **No dataset license found.** Reuse terms are operationally ambiguous.
19. **Release/paper timing boundary.** The pinned public revision is months later; public rubrics/deliverables must not be projected backward as paper-time evidence.
20. **Limited reproducibility.** Full private tasks, model outputs, human ratings/rationales, task-review histories, grader prompt/training data, and analysis code are unavailable.

## Reproducibility and operational realism

The public task metadata is unusually auditable: prompts, pinned file locators, expert artifacts, and detailed criteria make it possible to reconstruct task packages and inspect real file conventions. The preserved spreadsheet pair confirms that at least one package contains executable formulas and structured selection state rather than a prose-only answer. The complete pinned tree prevents mutable-main URL drift.

The central published results are not independently reproducible. The 1,320-task full set is private; the human/model deliverables used for comparisons, rating table, rater assignments, rationales, grader sweeps, model configurations, exact prompts, analysis code, and gold selection record are not released. The public grader is a service rather than a pinned executable instrument. The paper's package lists help reconstruct an OpenAI container, but Claude UI sampling and proprietary services remain mutable.

Operational realism is mixed by design. Artifact formats, long completion estimates, subjective quality, and occupation-matched review are substantial advances over exam questions. Conversely, complete one-shot context, no collaboration, no proprietary systems, no organizational state, and no downstream consequences remove exactly the context discovery and judgment loops that often make professional work consequential. GDPval should be treated as a broad **artifact-production slice**, not a simulation of occupations.

## Transfer to skill-bench

### Preserve

1. **Top-down frame before task solicitation.** Declare domain/occupation eligibility and exclusions rather than accepting whatever contributors happen to offer.
2. **Separate author, reviewer, lead reviewer, grader, and researcher rights.** Preserve promotions and transformations as lineage, not generic “expert reviewed.”
3. **Require a real witness artifact.** Use it as a feasibility and grader-calibration witness, never as an unquestioned gold optimum.
4. **Support multimodal references and deliverables.** Predeclare authoritative structured views, renders, and controls.
5. **Capture review and completion cost.** But preserve raw time, role, compensation basis, uncertainty, and skew rather than only wage-multiplied means.
6. **Treat verification prompts as interventions.** GDPval's rendering result motivates no-skill/public-skill and inspection-tool ablations.

### Correct

1. **Create a sampling frame record:** eligible work universe, exclusions, source version, occupational/activity weights, author coverage, realized task mixture, and generalization boundary.
2. **Separate four claims:** task-package performance, occupation-family performance, occupational-work-share performance, and economic/deployment impact. Require new evidence at every upgrade.
3. **Represent human baselines as distributions:** multiple independently produced witnesses where feasible, witness qualifications/time/context, professional acceptability gate, and judge disagreement.
4. **Use hierarchical estimands:** task-family and occupation clustering, equal-cell versus population-weighted views, and sensitivity to alternate legitimate assemblies.
5. **Bind value to loss:** time and wages are descriptors; consequential value needs acceptance policy, correction path, error severity, asymmetric loss, and downstream use.
6. **Fail closed on grader exclusions:** an ungradable task remains part of coverage/missingness evidence; it must not silently disappear from the denominator.
7. **Firewall public artifacts:** public witness/rubric tasks become calibration or regression items, not secure capability items.

## Concrete next actions

1. **No new schema task.** The existing expertise-transfer, expert-participation, benchmark-bundle/artifact-view, task-projection, task-health, metric-monitoring, and validity-argument contracts can represent these obligations. The pending ECBD cross-record audit is the right implementation path.
2. **Extend that audit's assembly section conceptually with four denominators:** frame, content, realized assembly, and inference population; report equal-cell and any justified weighted estimand separately.
3. **For the next real expert-reviewed pilot, obtain two independent witness artifacts or one witness plus a predeclared professional acceptability review.** Never call one artifact an expert ceiling.
4. **Record expert labor empirically:** applicant funnel, author/reviewer/grader hours, compensation or reciprocal value, revision counts, defect yield, attrition, and cost per accepted task.
5. **Add a public/private task role transition:** once rubrics or human deliverables are exposed, mark capability use contaminated and retain the task for calibration, grader studies, or regression only.
6. **Test an observed augmentation workflow before making savings claims:** model attempt → expert review → correction/rejection → final artifact, with total time, cost, error severity, and comparison to matched unaided work.

## Action items

- [x] Read and verify the complete immutable arXiv v1 paper.
- [x] Parse all 220 public metadata rows and 10,453 rubric items at the pinned release revision.
- [x] Verify all 509 referenced/deliverable paths against the complete pinned tree.
- [x] Structurally inspect one complete accountant spreadsheet reference/deliverable pair.
- [x] Separate paper-time claims, later release evidence, and `skill-bench` adaptations.
- [x] Audit occupational sampling, expert roles, pairwise grading, grader reliability, cost equations, and claim boundaries.
- [x] Map findings to existing contracts without adding a duplicate task.
- [ ] Run a consented, matched expert-plus-agent augmentation study before licensing productivity or savings claims.
