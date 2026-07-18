# Paper Review: Project Kaleidoscope contextual-evaluation validity

- **Paper:** <https://arxiv.org/abs/2607.14673v1>
- **Title:** *Project Kaleidoscope: Contextual, Human-Aligned Evaluation for Real-World AI Applications*
- **Authors:** Leanne Tan, Rohan Jaggi, Shaun Khoo, and Roy Ka-Wei Lee
- **Date read:** 2026-07-18
- **Version read:** immutable arXiv v1, submitted 16 July 2026
- **Local PDF:** `data/papers/pdfs/2607.14673v1-project-kaleidoscope.pdf` (13 pages; SHA-256 `f9510f81dd0083be6da9ab6333ce7b5bd6972233b1b4cd18730f0be0491fdeef`)
- **Local text:** `data/papers/text/2607.14673v1-project-kaleidoscope.txt` (SHA-256 `36b031fb940d516b666718f1a4ab4ff63be8991aa1d6495173d638496e7a66a0`)
- **TeX source:** `data/papers/source/2607.14673v1-source.tar` (SHA-256 `c3a7e24a8efcd96d252d8d42d645c06b3f3a852fbc80f791aff6a37481f81a02`)
- **Official implementation:** <https://github.com/govtech-responsibleai/kaleidoscope>, archived at commit `83bee80aa36b36483cd3b9e5742640f29ab8f372`
- **Linked MetaEvaluator:** <https://github.com/govtech-responsibleai/meta-evaluator>, archived at tagged commit `c0996b1e454440d183be988156853072cc4fa178` (`v0.3.3`)
- **Release provenance:** `data/sources/releases/2607.14673v1-kaleidoscope/provenance.json`
- **Timing boundary:** MetaEvaluator v0.3.3 predates arXiv v1; the archived Kaleidoscope commit is about 19 hours after v1 and is not exact paper-time code.
- **RubricBench artifact:** <https://huggingface.co/datasets/govtech/RubricBench>, metadata/card preserved at revision `89fe84982c687b775a3d55997ca882ff9472b6e1`; the manually gated row-level CSV returned HTTP 401 without credentials.
- **Tags:** contextual-evaluation, persona-generation, rubric-authoring, human-annotation, llm-judge, calibration, production-workflow, validity

## One-sentence contribution

Kaleidoscope contributes a coherent and unusually inspectable application-context → persona → test input → rubric → assisted human label → candidate judge → reliability gate → aggregate workflow, but its evidence establishes an early usable implementation and calibration-set agreement—not representative test coverage, independent human ground truth, held-out judge reliability, valid criteria, governance utility, production fitness, or readiness—and the release reveals that the nominal gate is a fixed `macro F1 >= 0.5` calculated on a user-selected, judge-assisted sample that is reused rather than reserved for untouched validation.

## Why this matters for skill-bench

The useful object is not another leaderboard. It is an **authoring-and-admission chain** for local evaluations:

```text
application profile and source authority
→ proposed personas
→ reviewed persona set
→ generated candidate inputs
→ admitted snapshot
→ criterion definition
→ transformed judge prompt
→ human evidence view and label
→ candidate-judge observations
→ calibration estimate and eligibility decision
→ aggregate or typed abstention
→ local decision claim
```

Kaleidoscope makes many of these stages operational and reviewable. That is directly relevant to charter objectives A–C and F: low-friction contextual task construction, rubric transformation, human contribution, configured judges, missing-result states, and error analysis.

The paper also exposes the central validity danger. A product can make the workflow convenient while every substantive warrant remains open. Generated personas are hypotheses about users; approved synthetic questions are not a representative sample; an LLM-suggested label selected by one product user is not independent domain ground truth; a prompt augmenter can change a criterion; agreement on a small co-designed calibration sample is not transport reliability; and majority voting among models sharing prompts, providers, or training data is not independent evidence. `skill-bench` should preserve this chain while preventing each arrow from inheriting authority from the previous one.

## Research question and claim boundary

The paper asks whether product teams can practically build application-specific functional evaluations by combining persona-based test generation, configurable rubrics, human review, and automated judges admitted only after local agreement with human labels. It explicitly distinguishes this from universal capability benchmarking and broader safety/security evaluation (Section 1, pp. 1–2).

### Supported by the full paper and release

1. A working post-v1 repository implements target setup, generated/sampled/manual personas, weighted question generation, target calls, response- and claim-level rubrics, judge-assisted annotation, multiple candidate judges, macro-F1 gating, majority/tie/no-judge/pending/override outcomes, snapshots, exports, tests, and cost fields.
2. An eight-user, four-team, three-week formative pilot produced about 12 runs, 180 generated cases, and 40 reviewed outputs; six users answered the questionnaire, five reporting greater evaluation efficiency (Section 5, pp. 4–5).
3. A 108-pair development dataset was independently labeled by two annotators across 14 binary dimensions. The paper reports model/prompt comparisons, three judge calls per configuration combined by majority vote, and criterion-specific variation (Appendix B, pp. 9–13).
4. Multi-metric prompts performed poorly or unevenly; prompt iteration did not repair the bracket architecture; selected single-metric configurations modestly improved empathy and verbosity; augmentation improved structure but worsened specificity (Tables 6–14, pp. 10–12).
5. The runtime implementation fails closed at the row level when no judge passes, a vote ties, or an eligible judge score is missing (`metrics_service.py`, lines 61–104, 240–296).

### Not established

The evidence does not establish that personas cover affected users; generated/admitted inputs approximate the deployment distribution; reviewers are representative, trained, blinded, independent, or authoritative; one annotation per answer/rubric is stable; assisted labels are unbiased; custom criteria are source-supported; augmentation preserves construct and decision boundary; `F1 >= 0.5` is an appropriate gate; candidate selection survives untouched validation; judges are independent; majority vote improves correctness; aggregate rubric scores support governance thresholds; or the workflow reduces total review cost, improves product decisions, catches consequential failures, remains reliable under drift, or is production-ready.

## Methodology and system

### Context, personas, and generated cases

Users provide organization, purpose, target users, knowledge base, rubrics, and goals. Sparse setup can be supplemented by public web search (Section 4.1, p. 3). Personas are generated from that profile, sampled from NVIDIA Nemotron personas, or manually entered. Each contains title, background, style, and use case; generated personas are pending until edited, approved, or rejected. Questions are then spread across persona, typical/edge type, in-/out-of-KB scope, input style, and language (Section 4.2 and Table 1, pp. 3–4).

After pilot feedback, the defaults became 70/15/10/5 percent for typical-in, edge-in, typical-out, and edge-out with a KB, or 80/20 typical/edge without one (Appendix A.3, p. 8). The release distributes inputs evenly across approved personas and then applies those fixed weights (`docs/.../5_creating-evaluation-set.md`, lines 66–89).

This is controlled **synthetic stratification**, not representativeness. No observed usage distribution, affected-user sampling frame, persona recall measure, stereotype audit, or held-out coverage test determines the strata or weights. Indeed, the initial equal allocation was changed because pilot users found it unrealistic (Section 5.1.1, p. 5), demonstrating that generation policy is a treatment requiring validation, not a neutral approximation. The release's persona prompt hard-codes Singapore-government archetypes and asks the model to vary demographics, urgency, and digital literacy; it has no explicit prohibited-stereotype rules, evidence locators, uncertainty, or population weights (`persona_generation.md`, lines 22–47).

The release does preserve candidate review state, source type, type/scope labels, language, input style, and snapshot-linked answers. It does not preserve a persona coverage warrant, represented population, context evidence locator, reviewer identity, rejection reason, criterion-to-persona consequence, or generated-candidate/admitted denominator in the paper's pilot report.

### Rubrics and judge-prompt transformation

Users choose presets or define a criterion, labels, and preferred outcome. The system uses one metric per judge prompt after multi-metric experiments showed large per-criterion differences (Section 4.4, p. 4; Appendix B.3–B.5, pp. 10–11). Custom rubrics are expanded by an LLM into a structured prompt with observable failure conditions and a reasoning scaffold. The release's augmentation prompt explicitly instructs a Singapore-government-chatbot context even though the platform advertises arbitrary HTTP targets (`rubric_augmenter.py`, lines 18–88).

The transformation boundary is weak. Generated prompts are accepted if they exceed 200 characters and contain `{{ Question }}` and `{{ Answer }}`; no semantic check verifies that labels, scope, exceptions, public basis, authority, or decision boundary were preserved (lines 138–145, 183–203). A fallback silently creates a simpler prompt when generation fails. Rubric edits purge stale scores, which is good operational hygiene, but the database stores mutable text and timestamps rather than immutable criterion, transformation, augmenter, input, and prompt hashes.

The paper's augmentation evidence is formative model selection on the same development dataset. Four augmenters × three detail levels × two selected criteria produce 24 configurations; the best configuration is selected on the reported data. Structure improves modestly while specificity worsens, and specificity has low human agreement (κ=0.317) (Appendix B.6, pp. 12–13). This supports “augmentation is criterion-dependent,” not “augmentation reliably operationalizes custom intent.”

### Human review

The UI shows candidate labels, highlighted claims, and judge verdicts. Reviewers must choose a rubric label rather than merely click approve/reject (Section 4.3, p. 4). This is better than invisible automation, but it is still **post-assistance labeling**: the annotator sees the baseline judge's recommendation and reasoning before committing. No unassisted-first label, reveal event, change reason, confidence, time, or anchoring randomization is reported.

The paper's experiment used two annotators who independently labeled all 108 pairs and were evaluated separately rather than collapsed into consensus (Appendix B.1, p. 9). RubricBench's public card reports 87.10% raw agreement but per-criterion agreement ranges from 70.37% for specificity to 99.07% for bias. The paper reports no annotator recruitment, domain credentials, training, blinding, order, time, compensation, adjudication, comments analysis, or uncertainty around agreement.

More importantly, the archived Kaleidoscope product does not implement multi-annotator lineage. Its `Annotation` row has only `(answer_id, rubric_id, option_value, notes, timestamps)`, a unique constraint permits exactly one row per answer/rubric, and no annotator ID or evidence-view identity is stored (`database/models.py`, lines 597–615). Thus the experimental two-annotator protocol is not the runtime annotation contract. The paper correctly lists multiple annotators as future strengthening (Section 6, p. 6).

### Candidate judges, gating, and aggregation

The paper creates three candidate judges per rubric, scores calibration units, and admits only those with Macro F1 above 0.5; if none passes, no aggregate is produced (Section 4.5, p. 4). The release uses `RELIABILITY_THRESHOLD = 0.5` and admits `>= 0.5`, a small boundary mismatch with the paper's `> 0.5` (`metrics_service.py`, lines 52, 256–270). It binarizes every rubric as `best_option` versus all other labels and computes macro F1 over overlapping selected rows (lines 552–645). Missing or unrecognized judge labels are skipped rather than represented in the metric denominator; errors resolve to reliability zero at the caller.

The release has useful explicit aggregate states: `majority`, `majority_tied`, `no_aligned_judge`, `pending`, and human `override`. But eligibility and scoring are not separated into calibration and untouched validation sets. The same user-selected annotated rows establish eligibility, and judges score the whole snapshot, including those rows. The documentation merely recommends 10–20 annotations from 50 cases and calls a “representative sample” sufficient without defining selection or uncertainty. No confidence interval, minimum per class, prevalence check, cluster handling, resampling, threshold-loss basis, correction for trying multiple judges/prompts, or context-shift validation accompanies the 0.5 gate.

Majority vote adds another unvalidated step. Three judges may share the same generated prompt, provider infrastructure, examples, source evidence, or correlated model lineage. The pilot mostly used only the default judge despite the jury design (Section 5.1.1, p. 5). The paper's experiment instead repeats each configuration three times and majority-votes stochastic outputs before comparing to humans (Appendix B.2, p. 9); this estimates one configuration's self-consistency treatment, not independent jury value.

## Evidence and result interpretation

The evidence ladder is:

1. **Workflow existence:** strong. Complete archives expose schemas, prompts, UI, persistence, tests, and explicit missing/tie states.
2. **Early usability:** weak but relevant. Eight users exercised four organizational cases for three weeks; only six answered the survey; there is no comparator, task timing, review-time measurement, error-catch outcome, or independent observation.
3. **Development-set judge agreement:** moderate as a diagnostic existence claim. Two labels per 108 synthetic pairs expose large criterion variation and low-agreement dimensions.
4. **Prompt-architecture selection:** exploratory. Criteria and configurations were selected iteratively on a shared development set, best configurations were reported, and no untouched test set or multiplicity control exists.
5. **Context validity, expert alignment, decision utility, and production fitness:** unsupported.

The headline contribution should therefore be read as **inspectable workflow machinery with useful failure states**, not “human-aligned evaluation.” The trusted-reference language is too strong for a one-row, judge-assisted runtime label. Macro F1 measures resemblance to the available labels under a selected prevalence; it does not validate the labels, criteria, sample, threshold, or decision.

## Unique insight

Kaleidoscope's unique transferable insight is that contextual evaluation needs **two admissions, not one**:

```text
case admission:
context evidence → persona/case proposal → human review → versioned evaluation set

observer admission:
criterion evidence → judge realization → human comparison → reliability decision → eligible observer
```

Most systems implement the second weakly and assume the first. Kaleidoscope implements both interfaces, but validates neither warrant. This separation is powerful for `skill-bench`: a reliable judge on an unrepresentative case set does not repair coverage, and a representative case set scored by an invalid observer does not produce a valid measurement.

A second insight is that **criterion transformation is part of the instrument**. Custom natural language is not the criterion after an augmenter adds exclusions, failure patterns, persona guidance, and decision scaffolds. That transformation needs immutable lineage and semantic review just like task generation.

A third is that abstention must be typed. Kaleidoscope's no-aligned-judge, tied, pending, and override states are better than forcing a score. Yet the reason must remain visible through population aggregation: `no judge passed`, `insufficient calibration cases`, `class absent`, `judge output invalid`, `human disagreement unresolved`, and `context shifted` are not interchangeable missingness.

## Limitations and validity threats

1. Four use cases, eight users, six survey responses, three weeks, and no controlled comparator.
2. Pilot application details, cases, outputs, labels, and results are redacted for privacy, preventing independent pilot audit.
3. No participant roles, domain authority, sampling frame, training, blinding, compensation, or decision rights are reported.
4. Approximately 180 generated cases and 40 reviews do not establish per-use-case candidate/admission/review denominators.
5. Efficiency is self-report, not measured labor, elapsed time, cost, error yield, or decision benefit.
6. Personas are generated archetypes or generic dataset samples, not observed user strata.
7. Fixed persona equality and type/scope weights lack population warrants.
8. No stereotype, excluded-user, perturbation, or persona-coverage audit is reported.
9. Web supplementation can import mutable, unauthorized, stale, or scope-inappropriate context.
10. Generated case review has no reported reviewer identity, rejection reason, or coverage impact.
11. Rubric authority and public basis are not recorded.
12. LLM augmentation may add or shift requirements; release validation is syntactic only.
13. The augmentation prompt is hard-coded to Singapore-government chatbots despite generic target claims.
14. Experiment criteria and prompt/model configurations are selected iteratively on one shared development dataset.
15. Best-configuration reporting is outcome-conditioned and uncorrected for multiplicity.
16. No untouched validation, cross-application transport, or temporal replication is reported.
17. The 108 pairs are synthetic and concentrated in four government-chatbot systems with contrastive prompt styles.
18. RubricBench's listed sample counts sum to 104 rather than 108 (30+30+16+28), an unresolved card-level accounting defect.
19. Two annotators are insufficient for stable disagreement analysis, and their identities/qualifications are absent.
20. Raw agreement is not chance-corrected reliability; per-dimension prevalence is consequential.
21. Judge-assisted labeling risks anchoring and correlated error.
22. Runtime annotations have no annotator ID and permit only one label per answer/rubric.
23. Runtime selection is user-controlled; no random, stratified, cluster-aware, or frozen sampling protocol is enforced.
24. The paper's `Macro F1 > 0.5` and code's `>= 0.5` differ at the boundary.
25. The fixed 0.5 threshold has no risk, loss, sample-size, or uncertainty justification.
26. Macro F1 can be unstable or misleading on 10–20 selected cases and absent classes.
27. Missing/unrecognized labels can disappear from overlap rather than enter an invalid-output denominator.
28. No confidence intervals, minimum class counts, effective sample sizes, or repeated-run uncertainty govern admission.
29. Candidate judges and prompts are selected and gated on the same sample; no nested or untouched validation exists.
30. Calibration rows are reused in whole-snapshot scoring, so reported aggregates mix fitted and unfitted observations.
31. Majority-vote value is not tested against the best individual judge or human adjudication.
32. Judge errors are correlated through prompts, data, providers, training, and assistance views.
33. Three stochastic repeats of one judge are not three independent judges.
34. The pilot mostly used the default judge, so jury usability and benefit are unvalidated.
35. Claim extraction/checkworthiness adds another model-controlled inclusion stage without recall validation.
36. “Any unsupported claim fails the response” is a strict policy choice, not a validated universal accuracy rule.
37. Snapshot identity does not by itself hash target, KB, web context, rubric, prompt, provider, model endpoint, and selection policy.
38. The archived Kaleidoscope commit postdates v1; exact paper-time implementation correspondence is unknown.
39. MetaEvaluator is a generic pre-v1 library; no paper experiment scripts or result tables were found in either archive.
40. The manually gated RubricBench CSV was not retrievable without credentials, so row-level labels and reported analyses were not independently recomputed.
41. No total token/currency table, human-time burden, latency distribution, or cost-adjusted utility is reported.
42. No governance threshold, stakeholder loss, downstream action, rollback, drift monitor, or prospective decision study is evaluated.
43. Input-output evaluation does not cover agent traces, tool use, retrieval behavior, long horizons, or side effects; the paper acknowledges this.
44. There is no professional-validity, production-reliability, or readiness evidence.

## Reproducibility and operational realism

Paper preservation is strong: immutable PDF, text, TeX, metadata, and hashes are local. Release inspectability is also good: both official repository archives are complete and timing-aware. The post-v1 Kaleidoscope package includes a substantial FastAPI/SQLAlchemy backend, Next.js UI, Docker setup, prompts, provider configuration, exports, and backend/UI tests. MetaEvaluator v0.3.3 provides separate human-result and judge-result records, configurable scoring, annotator aggregation, and invalid-result handling, but it is not demonstrated as the exact experiment runner.

A released deterministic slice was executed from the pinned Kaleidoscope archive with its locked Python 3.13 environment: `pytest -q tests/unit/test_metrics_service.py tests/unit/test_persona_sampler.py tests/unit/test_persona_generator.py tests/unit/test_system_rubrics.py`. Result: **37 passed, 1,195 warnings in 4.83 seconds**. The warnings were dominated by SQLAlchemy table-cycle and legacy-API notices. Passing establishes implementation conformance for selected metric/persona/rubric behaviors only, not empirical reproduction or evaluation validity.

Reproduction of Appendix B remains blocked. Neither archive contains RubricBench experiment scripts, prompt variants, raw predictions, run seeds, model endpoint snapshots, costs, or generated tables. The public dataset card and API metadata were preserved at revision `89fe849...`, but the gated CSV returned HTTP 401. Therefore the 108-pair results, label distributions, three-repeat votes, and tables were read from immutable v1 and the official card but not recomputed.

Operational realism is mixed. The product handles partial failures, retries, pending rows, ties, no-qualified-judge states, overrides, token/cost fields, provider diversity, uploads/exports, and snapshots. Conversely, its default annotation recommendation, one-label database constraint, fixed gate, mutable context, absent immutable configured-system hashes, and reuse of calibration units make it an alpha workflow rather than a defensible production measurement system.

## Transferable benchmark implications

1. **Separate case admission from observer admission.** A task/case needs context authority, population/coverage warrant, candidate/admitted denominators, and review lineage independent of judge calibration.
2. **Treat persona strata as hypotheses.** Record represented population, source, weight basis, excluded groups, stereotype review, perturbations, and coverage uncertainty; do not label equal synthetic allocation representative.
3. **Version criterion transformations.** Preserve original criterion, authority, augmenter configuration, generated prompt, diff, reviewer decision, semantic-equivalence claim, and all hashes.
4. **Require unassisted-first labels for calibration.** Assistance may follow, but retain pre-assistance label, reveal event, post-assistance label, confidence, rationale, and change reason.
5. **Split development, gate calibration, and untouched validation.** Judge/prompt selection cannot share the only sample used to license deployment scoring.
6. **Make eligibility threshold estimands explicit.** Store class counts, invalid/missing outputs, sampling policy, clusters, interval, threshold/loss basis, multiplicity, and expiry/context-shift triggers.
7. **Model jury dependence.** Provider/model/prompt/evidence-view diversity is configuration metadata, not assumed independence; compare jury against constituents on untouched labels.
8. **Propagate typed abstention.** Preserve no-qualified-observer, tie, pending, invalid output, unresolved human disagreement, insufficient sample, and shifted context separately.
9. **Keep claim ceilings local.** A passing judge gate supports at most “agreement with these labels on this sample under this configuration”; professional quality and governance decisions require separate validity arguments.

## Concrete repository actions

1. **Do not add a new schema task.** Existing criterion lineage, expert-participation, grader evidence-view, metric-monitoring, configured-system, task-health, release, and validity contracts already provide homes for every requirement above. The evidence calls for a crosswalk/conformance fixture, not another subsystem.
2. In the next consolidation pass, add a canonical **dual-admission boundary**: case admission and observer admission must be separately evidenced, versioned, and capable of abstaining.
3. When a contextual-eval pilot is next built, require three disjoint partitions—prompt/rubric development, eligibility calibration, untouched context-shift validation—and preserve candidate/generated/admitted/reviewed/scored denominators.
4. Add a future planted conformance case to the existing machinery where an augmenter introduces an unsupported obligation, a calibration sample omits one class, and three correlated judges pass an apparent majority; the expected outcome is failed eligibility/validity, not an aggregate score.

No new queue task is justified: these refinements overlap existing contracts and the repository currently needs consolidation and validation rather than another parallel build.
