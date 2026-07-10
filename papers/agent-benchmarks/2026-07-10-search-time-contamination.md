# Paper Review: Search-Time Contamination in Retrieval-Enabled Agent Evaluation

- **Paper:** https://arxiv.org/abs/2606.05241v1
- **Authors:** Yongjie Wang, Xinyue Zhang, Kunhong Yao, Zhiwei Zeng, Kaisong Song, Jun Lin, and Zhiqi Shen
- **Date read:** 2026-07-10
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, 3 June 2026
- **Local PDF:** `data/papers/pdfs/2606.05241v1-search-time-contamination-deep-research-agents.pdf` (15 pages; SHA-256 `2423005736b8547a34bee9fedb04fd43534672943f79fc1ebcf22f04062bbd2d`)
- **Local text:** `data/papers/text/2606.05241v1-search-time-contamination-deep-research-agents.txt` (SHA-256 `decd3ce1224c502f81f17b00e2bbfb31505cb0fab1b75941b152c513982a8678`)
- **Paper-linked results:** https://anonymous.4open.science/r/Search-Time_Contamination-25F2/ (linked by v1; not required as evidence for the paper-only claims below)
- **Tags:** search-time-contamination, retrieval, benchmark-leakage, causal-validity, trace-provenance, controlled-access

## One-sentence contribution

The paper turns a vague concern about web-enabled benchmark leakage into a turn-level taxonomy and audit over 6,803 medical QA items, showing that direct retrieval of an exact question–answer pair strongly predicts rapid correct answers; however, only the answer-leakage detector is partly validated, contamination exposure is endogenous, the headline “up to 4%” inflation has no reported counterfactual derivation, and the study therefore establishes a serious audit signal rather than a causal correction to reasoning performance.

## Why this matters for skill-bench

This paper advances charter objectives A, B, and C by locating a validity failure **inside the agent rollout**. Pretraining contamination asks what the model knew before a trial. Search-time contamination asks what the configured system was allowed to retrieve during the trial. In a knowledge-work benchmark, this distinction is decisive: broad retrieval may be part of the target capability, yet retrieval of a mirrored task, private reference answer, or grader artifact bypasses the intended work.

The paper's most useful empirical boundary is narrower than its rhetoric. Benchmark-name or suspicious-host retrieval is not itself evidence of score inflation: Tongyi's benchmark-metadata subset performs worse on two of six datasets, and metadata hazard ratios are below one on five datasets (Tables 2 and 4, pp. 6–7). Exact question–answer retrieval is different: accuracy immediately after detected explicit answer leakage rises to 48–100% across datasets, and time-varying hazard ratios for first correct prediction range from 2.20 to 8.92 (Tables 3–4, p. 7). The design implication is an evidence ladder—**search result exposure → page access → item match → answer-key exposure → answer adoption → measured effect**—not a single `contaminated` flag.

For `skill-bench`, this also prevents accidental scope narrowing. Medical multiple-choice questions are a stress case because exact items and keys are widely mirrored; they are not the benchmark's target work. The reusable hypothesis is that any tool-enabled task needs an explicit information-flow contract and trial-level evidence showing whether retrieval served the professional construct or bypassed it.

## Research question and claim boundary

The paper asks:

1. How often do web-enabled research agents encounter benchmark metadata, exact question context, or exact question–answer pairs during evaluation?
2. How are those events associated with intermediate and final correctness?
3. Do weaker leakage events escalate into explicit answer leakage?
4. Does the pattern appear across search providers and commercial research agents?

The evidence supports these bounded claims:

- Tongyi Deep Research trajectories on the six selected medical QA sets contain detectable benchmark-related URLs and exact question–answer pages at nontrivial rates (Table 1, p. 6).
- On this sample, the partly human-validated explicit-answer detector identifies events followed by large within-trajectory correctness jumps and strong positive associations with first correct prediction (Tables 3–4, p. 7).
- Search backend/source overlap matters: Valyu has no detected leakage on 100 MedQA items but 65/100 on a PubMedQA sample whose source corpus is within its retrieval infrastructure (Appendix F, p. 14).
- Commercial-system observability differs enough that equivalent contamination auditing is not possible from all systems' outputs (Sections 5.6 and 6, pp. 7–8; Appendix C, p. 12).

The evidence does **not** establish that metadata or exact-question retrieval generally causes inflation, that contaminated and uncontaminated questions have equal difficulty, that 4 percentage points is a reproducible correction, that rank changes were measured, that an original source is always an illicit shortcut, that the detector has adequate recall outside one small subset, or that a closed web sandbox by itself measures general knowledge-work capability.

## Methodology

### Data and configured systems

The main study evaluates 6,803 questions from six medical QA sets released from 2020–2025: MedQA (1,273), half of six medical MMLU test subsets (544), half of MedMCQA (2,089), MedXpertQA Text (2,450), HLE-149 (149), and MedBullets5op (298) (Section 5 and Appendix B, pp. 5, 11–12). MMLU and MedMCQA discard the shortest half under the assumption that shorter questions emphasize factual recall. This changes the target population and makes reported prevalence conditional on a reasoning-enriched subset rather than each canonical test set.

Tongyi Deep Research is the primary agent because it exposes queries, returned URLs, visited pages, summaries, and reasoning. The paper compares its base Qwen3-30B-A3B model, a web-disabled Tongyi variant, and web-enabled Tongyi. Generalization checks use the first 100 MedQA questions with Gemini Deep Research, Step Deep Research, and Valyu Deep Research; Valyu is also tested on 100 PubMedQA questions (Sections 5–5.6, pp. 5–8; Appendices C and F, pp. 12–14). Table 8 records materially different models, search engines, browsers, and languages, so cross-agent leakage rates describe configured systems, not model-only vulnerability.

There is no reported random seed, repeated trial, search date/window, search-engine locale, result-cache policy, model endpoint version for every run, or task-order policy. The commercial check is only 200 paid task runs in total and uses a much weaker evidence view than Tongyi. Total reported execution and judging cost is USD 858 (Appendix E, pp. 12 and 14).

### Three contamination labels

The paper defines labels at the search/visit-step level (Section 3.1, pp. 3–4):

- **Benchmark Metadata Leakage (BML):** a search returns a URL matching a common artifact host, exam/question-bank pattern, or benchmark identifier.
- **Question-Context Leakage (QCL):** visited content has high normalized longest-common-substring overlap with the question but does not expose its answer.
- **Explicit Answer Leakage (EAL):** visited content includes the exact question fingerprint and its paired ground-truth answer.

These labels mix distinct predicates. BML is inferred search-result exposure and supposed intent; QCL is lexical content overlap; EAL is a privileged semantic audit using the hidden ground truth. A trajectory may contain several labels, while Table 1's question-level columns allocate items among no-STC, BML-only, BML+QCL, BML+EAL, and all-three groups.

### Detection and human checking

BML uses regular expressions over URLs. Appendix Table 11 (p. 15) includes narrow patterns such as dataset names but also broad patterns including all `github.com`, `facebook.com`, and URL terms such as `question`, `test`, `quiz`, and `MCQ`. The detector therefore cannot support the paper's claim that a match means the agent “seeks dataset-level metadata” rather than task-relevant knowledge. No human precision/recall study of BML is reported.

QCL uses longest common substring divided by question length and excludes EAL cases (Section 3.2, p. 4). The paper does not state the decision threshold, content extraction procedure, normalization details, or any human validation. It consequently cannot be reproduced from the manuscript or interpreted as a calibrated exact-context detector.

EAL sends the question, ground-truth answer, and retrieved content to DeepSeek V4 Pro. Its prompt requires both an extended verbatim question match and an answer explicitly paired with it (Appendix Figure 3, p. 13). MedBullets validation manually labels the first 160 questions and reports 100% precision and 83.33% recall; MedQA manually checks only automatically positive cases and reports 94.87% precision, with no recall estimate (Section 3.2 and Appendix D, pp. 4 and 12–14). The manuscript does not report annotator count, independence, qualifications, disagreement, adjudication, confidence intervals, or per-source errors. “Substantial agreement” therefore overstates a small, incompletely specified validation.

For proprietary systems, the authors cannot apply the same turn-level detector because only final summaries and URL lists are exposed. They instead match question text against visited content and manually verify answer exposure (Section 5.6, p. 7). The resulting Gemini/Step/Valyu rates are not measurement-equivalent to the Tongyi results.

### Performance analysis

The paper uses three analyses:

1. **Question-level splits.** Accuracy is compared between questions with and without BML and among leakage subgroups, explicitly assuming comparable difficulty (Section 4.1, p. 4; Table 2, p. 6).
2. **Immediate prediction shift.** A tentative prediction at the contamination turn is compared with the next turn. Missing intermediate predictions are counted as wrong (Section 4.2, p. 4; Table 3, p. 7).
3. **Time-varying survival models.** BML, QCL, and EAL become absorbing time-dependent covariates in a multivariable Cox model whose event is the first correct intermediate prediction. Kaplan–Meier curves and a second Cox model describe escalation from BML/QCL to EAL (Sections 4.2 and 5.4–5.5, pp. 4, 7; Appendix A, p. 11).

The manuscript does not explain how intermediate predictions are extracted, test proportional-hazards assumptions, account for task clustering, report repeated runs, adjust for multiple comparisons, or model provider/search-result drift. The Cox models estimate conditional association, not a causal treatment effect.

## Evidence and results interpretation

Table 1 (p. 6) shows highly variable exposure. EAL-inclusive question counts are 34/1,273 for MedQA, 42/544 for MMLU, 507/2,089 for MedMCQA, 23/2,450 for MedXpertQA, 3/149 for HLE-149, and 9/298 for MedBullets5op. This supports a prevalence warning under the detector and run conditions, especially for MedMCQA. It does not estimate stable future prevalence because the web index, provider, query policy, and mirrored pages are mutable.

Table 2 usefully falsifies a coarse “repository hit equals advantage” story. BML-associated accuracy is lower on MedQA and MedMCQA, higher on the other four datasets, and QCL-only groups are tiny and erratic. EAL-associated groups are usually much more accurate, reaching 95.65–100% in several cells. Yet these are selected questions: exact mirrored question–answer pages are not randomly assigned, and their existence/retrievability can correlate with age, wording, popularity, source, option format, and intrinsic difficulty.

Table 3 provides the clearest behavioral evidence. Immediately after EAL, correctness rises from 0–20% before exposure to 48–100% after exposure; BML usually shows the opposite change, and QCL is mixed. The worked Chegg example shows the agent explicitly abandoning an earlier option interpretation and adopting the retrieved key (Figure 1, pp. 3–4). This is persuasive process evidence for individual cases. Aggregate jumps are still affected by counting absent pre-event predictions as incorrect and by selecting moments when the agent chose and succeeded in visiting an answer-bearing page.

The Cox results preserve the same pattern: EAL hazard ratios are above one for all six datasets and conventionally significant for five; BML is below one for five; QCL is mixed (Table 4, p. 7). QCL predicts later EAL on four of five reported datasets with hazard ratios 2.50–6.74 (Table 5, p. 8). These models control the three leakage indicators, but not question properties, search policy state, turn-varying confidence, page availability, or task-level dependence. Because agents cause their own retrieval exposure, “independent association” in Appendix A should not be read as identified causal effect.

The paper repeatedly claims inflation “up to 4%” and possible ranking changes (abstract, introduction, conclusion, pp. 1–2 and 8), but no table defines the inflation estimand, reports a contamination-rectified score, or shows a rank comparison. Web-enabled versus web-disabled Tongyi differs by 2.28–14.87 points across the six sets (Table 2), but that contrast bundles legitimate retrieval, agent/tool policy, and contamination. Removing detected cases changes the question population rather than supplying their unobserved clean outcomes. The 4% figure is therefore not auditable from v1 and should be treated as unsupported until a derivation or randomized/replayed mitigation experiment is released.

The commercial results establish source-policy dependence more clearly than agent generality. Gemini visits exact question–answer pages on 60 of 100 MedQA items despite scoring 99% with web and 97% without; Step does so on 9%, and Valyu on 0% (Table 6, p. 8). Appendix F then reports 65/100 PubMedQA leakage for Valyu, whereas the main text says 78% (p. 7 versus p. 14). This unresolved numerical contradiction weakens exact prevalence claims but reinforces the qualitative point: a “curated” corpus is not safe when benchmark items originate in that same corpus.

## Unique insight

The deepest transferable insight is that **contamination is a relation among an evaluation item, an information object, an access event, and the intended construct—not a property of a URL or dataset alone**.

An original clinical article can be:

- legitimate evidence in a literature-synthesis task;
- question-context leakage in a closed-book reasoning test derived from that article;
- the required public source in a provenance task;
- answer leakage only if it exposes a benchmark-specific question/key pairing;
- harmlessly retrieved but unused;
- consequentially incorporated into the final artifact.

The paper partly recognizes this by separating BML, QCL, and EAL, but its BML detector collapses host, intent, exposure, and impropriety. Its recommendation for one shared sandbox likewise controls access while changing the construct: an agent's ability to search the live, messy web is not the same capability as searching a curated corpus.

`skill-bench` should therefore represent a leakage event as a staged, typed relation:

`candidate artifact → returned → visited → content captured → matched to protected object → visible to agent → incorporated → outcome affected`

Each stage needs separate evidence. The protected-object relation should distinguish `task_instance`, `reference_answer`, `private_check`, `rubric`, `calibration_case`, `source_pack`, and `legitimate_domain_source`. Severity and score validity then follow from the public task's allowed-information policy and validity claim, not from a universal blacklist.

A second insight is that contamination correction is a causal problem. An audit can show that an answer key was visible and adopted; it cannot infer the counterfactual clean score merely by comparing self-selected contaminated and clean subsets. A defensible estimate needs paired replay or randomized masking/allowlisting under the same task, configured agent, provider snapshot, and budget. Audit evidence can invalidate or quarantine a trial before it can quantify inflation.

## Transferable design patterns

### 1. Freeze an allowed-information contract

For every task version, declare whether network access is denied, allowlisted, snapshot-based, or open; which source classes are legitimate; which task/reference/rubric objects are protected; and whether exact source-of-item retrieval is part of or outside the construct. Hash the policy with task, harness, environment, and source-pack versions.

### 2. Capture external evidence as trial provenance

Preserve query, search provider/index mode, timestamp, locale, result rank, URL, redirect chain, visit status, content hash or approved snapshot locator, snippet, agent-visible extraction, and citation/use link. A URL list alone cannot establish content exposure; final citations alone cannot reconstruct search intent or intermediate leakage.

### 3. Separate exposure, use, and effect

Emit distinct observations for suspicious result returned, page visited, protected content matched, content supplied to model context, answer adopted, and score invalidated. Use `insufficient_evidence` when proprietary systems omit required trace stages. Do not treat a BML-style host hit as agent intent or score inflation.

### 4. Type leakage mechanisms

Keep at least these boundaries separate:

- **pretraining contamination:** protected content may be in model parameters before the trial;
- **search-time leakage:** a tool retrieves protected benchmark material during the rollout;
- **evaluator-cue leakage:** a Skill, rubric, feedback policy, or examples reveal what private evaluation rewards;
- **cross-trial leakage:** memory or lessons retain private answers/check outcomes;
- **legitimate retrieval:** evidence access is permitted and germane to the professional construct.

A trial may exhibit several mechanisms; one must not stand in as evidence for another.

### 5. Validate detectors by stage and population

Measure URL-detector, content-match, answer-pair, and adoption classifiers separately. Use independently sampled positives and negatives, multiple annotators, explicit adjudication, uncertainty, source/provider slices, and confidence intervals. Human-checking only model-positive cases estimates precision, not recall.

### 6. Estimate effects with access interventions

For calibration items, replay matched conditions with answer-bearing artifacts available versus masked while holding provider snapshot, task, agent, harness, seed/order, tool budget, and legitimate domain evidence constant. Cluster uncertainty by task and repeat stochastic runs. Report audit prevalence separately from paired score effect; never call subset deletion a clean counterfactual.

### 7. Operate public, semi-private, and private forms deliberately

Use public development items for debugging, controlled or canary-seeded forms for leakage audits, and private/equivalent forms for claims vulnerable to exact-item retrieval. Test crawlers and tool-level filesystem/network access before trials. A private file is not protected if the runtime can enumerate repository paths, and a gated URL is not protected if mirrors are indexed.

## Limitations and validity threats

1. **Single-domain concentration.** All six main datasets are medical QA; five are predominantly multiple choice. This is a high-exposure stress case, not prevalence evidence for general knowledge work.
2. **Reasoning-enriched filtering changes the population.** The shortest half of MMLU-Med and MedMCQA is removed without a sensitivity analysis.
3. **No repeated trajectories.** Search and agent stochasticity are not estimated.
4. **Search state is mutable and under-recorded.** Dates, locale, cache, index version, and task order are absent.
5. **BML has likely false positives and false negatives.** Patterns include entire hosts and generic URL terms while omitting unknown mirrors; no human validation is reported.
6. **BML intent is over-inferred.** A returned GitHub or question URL does not show that the model sought benchmark metadata.
7. **QCL is under-specified.** No threshold, extraction details, validation, or sensitivity analysis is provided.
8. **EAL validation is incomplete.** Only the first 160 MedBullets questions support recall; MedQA checks detector positives only; annotation procedures and uncertainty are missing.
9. **Privileged detection does not equal agent use.** The EAL judge sees the ground-truth answer; the paper does not always establish which matched content entered the model's usable context.
10. **Commercial measurements are not equivalent.** Their traces omit queries and intermediate evidence, and leakage is manually reconstructed from final URLs/content.
11. **Question-level comparisons are confounded.** Contamination propensity correlates with benchmark age, source, wording, mirroring, popularity, and likely difficulty.
12. **Immediate shifts are selected and asymmetrically scored.** Missing pre-event predictions count as wrong, mechanically enlarging some post-event gains.
13. **Cox associations are not causal.** Exposure is agent-selected; relevant time-varying and item covariates are omitted; proportional-hazards checks and clustered errors are unreported.
14. **First-correct is a narrow endpoint.** It ignores later regression, final-answer stability, evidence quality, and professional artifact consequences.
15. **Intermediate prediction extraction is unexplained.** This blocks faithful replication of Tables 3–5.
16. **No auditable 4% rectification.** The claimed maximum inflation lacks a displayed formula, corrected score table, or counterfactual experiment.
17. **No demonstrated ranking analysis.** The conclusion says rankings can change without reporting a ranking estimand or table.
18. **Web-on/off is a bundled treatment.** It combines legitimate knowledge retrieval with leakage and cannot isolate either.
19. **Small EAL cells produce unstable extremes.** Several 100% cells contain only one to a few events; confidence intervals are not reported.
20. **Multiple testing is untreated.** Numerous dataset/type hazard tests are interpreted without multiplicity control.
21. **Numerical inconsistency remains.** Valyu/PubMedQA is 78% in Section 5.6 but 65/100 in Appendix F.
22. **Mitigation is proposed, not tested.** No sandbox, controlled-access, masking, or dynamic-item experiment appears in v1.
23. **A shared sandbox changes external validity.** It improves treatment parity but may remove live-web retrieval capabilities central to realistic research work.
24. **Access-control prescriptions are incomplete.** Registration and data-use agreements do not stop mirrors, screenshots, memorization, or malicious redistribution.
25. **Dual-use risk is real.** Publishing exact detection patterns can guide benchmark poisoning or evasion, as the ethics section acknowledges (p. 9).

## Reproducibility and operational realism

Reproducibility is moderate for the conceptual detector and weak for exact regeneration. The immutable paper provides dataset counts, system families, the EAL prompt, broad BML patterns, costs, and numerical tables. Tongyi's observable traces are the right kind of operational evidence: queries, URLs, visits, summaries, and intermediate reasoning permit post-hoc audit rather than relying only on final citations.

Exact replication is blocked by omitted QCL thresholds and intermediate-prediction extraction, incomplete endpoint and search-time pinning, mutable web content/indexes, proprietary commercial systems, no reported run manifest or repeated seeds, and non-equivalent trace access. The anonymous paper-linked repository may improve artifact availability, but the manuscript alone does not preserve a frozen search corpus or enough configuration to recreate exposure rates. Even with code, live-index prevalence is a dated measurement, not a permanent benchmark property.

Operational realism is mixed. Open-web retrieval and exact mirrored question pages are genuine hazards for research agents. Medical MCQ final accuracy, however, omits source authority, contradiction handling, artifact quality, stakeholder decisions, and safety. The proposed isolated sandbox offers internal validity but can suppress the very source-discovery and evidence-reconciliation behavior `skill-bench` seeks to measure. A stronger design uses controlled snapshots for causal calibration and instrument health, alongside explicitly bounded live-web trials for ecological validity.

## Concrete changes for skill-bench

1. **Extend existing trial/trace records rather than create a contamination subsystem.** Add an external-evidence observation with provider/time/query/result/visit/content-hash, protected-object relation, visibility, incorporation status, detector version, and evidence sufficiency. This belongs in the existing benchmark bundle and configured execution record.
2. **Refine task network policies.** The current `allowed`/`denied`/`allowlist` field should reference a hashed information-flow policy that identifies legitimate source classes, protected artifacts, snapshots, and fail-closed behavior.
3. **Feed leakage adjudication into task health.** `build-task-health-lifecycle-contract` should treat confirmed answer-key access, suspected exposure, trace insufficiency, and detector defects as different adjudications. Instrument revisions must not rewrite historical scores.
4. **Bound claims in validity arguments.** A trial with unexcluded protected-content exposure cannot support a reasoning/process claim; it may still support a narrow configured-system outcome claim if retrieval was permitted. Record the alternative explanation and excluded interpretation explicitly.
5. **Specify prevalence and effect separately in metric monitoring.** `build-metric-monitoring-contract` should define eligible population, unit (result/visit/turn/trial/task), detector missingness, provider/time window, task clustering, uncertainty, and audit action. A leakage rate is not an inflation estimate.
6. **Add controlled canaries to execution validation.** Seed non-answering protected markers in private repository, source-pack, and web-snapshot locations; verify that only policy-allowed tools can reach them and that all external observations are captured before accepting a run.
7. **Calibrate with matched masking.** Use equivalent-form items and replayable source snapshots to compare clean versus answer-artifact-exposed conditions. Preserve legitimate domain sources in both arms so the intervention changes only the shortcut.
8. **Do not add a queue task.** The evidence sharpens the pending task-health and metric-monitoring builds plus existing bundle, validity, execution-isolation, and longitudinal leakage boundaries; a separate contract would duplicate those objects.

## Action items for repository

- [x] Read and preserve the complete immutable arXiv v1 PDF and full local extraction.
- [x] Reconstruct datasets, configured systems, taxonomy, detectors, validation, question/turn analyses, costs, and mitigation proposals with page evidence.
- [x] Separate detector prevalence, behavioral association, causal effect, and validity claims.
- [x] Record the unauditable 4% inflation claim, unsupported ranking claim, and Valyu/PubMedQA numerical contradiction.
- [x] Map nonduplicate implications to existing source, trace, execution, validity, task-health, metric, and controlled-access objects.
- [x] Add no build task because existing pending contracts can absorb the requirements.
