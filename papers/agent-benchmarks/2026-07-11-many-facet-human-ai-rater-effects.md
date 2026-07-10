# Paper Review: Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model

- **Paper:** https://arxiv.org/abs/2505.18486v2
- **Authors:** Hong Jiao, Dan Song, and Won-Chan Lee
- **Date read:** 2026-07-11
- **Venue / source:** arXiv preprint
- **Version read:** immutable v2
- **Local PDF:** `data/papers/pdfs/2505.18486v2-many-facet-human-ai-rater-effects.pdf` (29 pages; SHA-256 `4e0ed6bddac7b7915733bc00ce17afb0860761f8e2a7424a46a620186b0b20bd`)
- **Local text:** `data/papers/text/2505.18486v2-many-facet-human-ai-rater-effects.txt` (78,119 bytes; SHA-256 `c14370e2ceaf9c3479d3cce84d5eed0987cdc3454378fc20242fc904fcf92e67`)
- **Official materials boundary:** no paper-linked code, data, FACETS control/output file, complete prompt set, API logs, or external supplement is identified in v2; Appendix A embeds one example prompt/rubric and Appendix B one score-dispersion table.
- **Tags:** many-facet-rasch, llm-judge, rater-severity, automated-scoring, agreement, grader-validity, measurement

## One-sentence contribution

The paper demonstrates on a fully crossed but very small AP Chinese writing sample that agreement alone hides large rater-specific severity and fit differences—ten LLM configurations and two human experts score the same 120 responses, while a Many-Facet Rasch model places students, four prompts, raters, and score thresholds on a common scale—but its unpinned model runs, human-reference dependence, misuse of internal consistency as repeat reliability, thin model specification, and absence of differential-rater, uncertainty, and out-of-sample analyses do not justify treating the favored LLMs as interchangeable or operationally ready graders.

## Why this matters for skill-bench

This advances charter objectives A, B, and C by adding a psychometric lens missing from simple model–human agreement. The reusable insight is not that educational essay scoring should define knowledge-work evaluation. It is that a grader can correlate well with a reference while systematically shifting decisions through severity, compressed scale use, or task-specific misfit. Conversely, a nearly “neutral” severity estimate is only neutral relative to the particular rater panel and identification constraint; it is not evidence of truth or fairness.

The source therefore sharpens existing grader evidence-view, metric, task-health, plural-judgment, and validity machinery. A benchmark should estimate an **error surface indexed by rater × criterion × task family**, distinguish a location shift from irregular response-specific error, and preserve the reference panel and linking design that make severity estimates identifiable. It should not silently severity-adjust a score and then claim the resulting value is professionally correct.

This is bounded transfer. Thirty U.S. college learners writing four short Chinese responses under one exam rubric do not establish the prevalence or form of rater effects in consequential multi-step knowledge work. The paper is useful as a measurement-design case, not as evidence for replacing domain experts with LLM graders.

## Research question and claim boundary

The study asks (p. 3): how accurate are LLM raters against human raters, how consistent are they, and what rater effects do they exhibit? It compares ten named model configurations against two certified AP Chinese raters using holistic and three analytic 0–6 scores.

The evidence supports narrow descriptive claims:

- agreement varies sharply by prompt, criterion, model, and which human is the reference (Tables 1–4, pp. 6–9);
- no AI rater dominates all conditions, although ChatGPT 4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro frequently have the largest reported QWK (pp. 9 and 18–19);
- the fitted severity ordering differs by holistic versus analytic scoring and by analytic trait (Tables 7–11, pp. 13–17);
- Gemini 2.0 is markedly severe in several fitted models, while human raters are generally lenient relative to this twelve-rater panel;
- some raters exhibit infit/outfit outside the authors’ chosen 0.7–1.3 range.

It does **not** establish that either human is a gold standard, that agreement with a human equals scoring accuracy, that alpha across prompts is intrarater repeat reliability, that severity differences are stable across populations or prompts, that a severity-adjusted AI score is interchangeable with expert judgment, or that any tested model is safe for unsupervised operational scoring. The conclusion that results “support the use” of three LLMs (p. 20) is stronger than the design permits.

## Methodology and system

### Participants, responses, and rating design

Thirty U.S. college students enrolled in third- or fourth-year Mandarin courses—18 third-year and 12 fourth-year students—completed two AP Chinese prompt types on two consecutive days: story narration (`SN1`, `SN2`) and email response (`ER1`, `ER2`). This produced 120 student–prompt responses. Two certified AP Chinese raters and ten LLM configurations scored every response, yielding a complete rater crossing rather than disconnected assignments (Methods, pp. 4–5).

Each rating contains one holistic and three analytic scores—Task Completion, Delivery, and Language Use—on 0–6 scales. The complete crossing is the study’s strongest design feature: rater location is not confounded with which responses happened to be assigned to a rater. Repeated prompts per student also allow student and prompt facets in principle.

However, the response sample is only 30 students × four prompts. Day is perfectly confounded with prompt year, and prompt year is nested in the two task types. The paper alternates between “30 essays” (p. 4) and 120 essays/responses (pp. 4–5); the data hierarchy is 30 students, four responses each. It provides no sampling frame, exclusions, missing-response account, or evidence that the response distribution spans operational AP proficiency.

### Human reference and AI prompting

Human rater R1 supplied rubric guidance, public examples, previously scored samples, and holistic-scoring instructions to every AI system over approximately 1.5 years as models became available (pp. 4–5). Appendix A gives one complete SN1 example prompt, rubric, and score-level exemplars (pp. 25–28). The model is told that Task Completion dominates and receives explicit decision rules such as capping a response that addresses only three pictures.

This is not model-independent validation. R1 is simultaneously trainer/reference author and one of the two agreement targets. Higher AI–R1 agreement can reflect successful imitation of R1’s interpretation, shared examples, or reference leakage rather than general scoring validity. The paper does not state whether the 120 evaluated responses appeared among “previously scored samples,” whether R2 independently approved the examples, how many examples each model received, or whether every model received byte-identical context.

The ten labels are product-level names rather than reproducible configured systems. Exact endpoint IDs, provider, access dates, temperature, seed, token settings, system messages, retries, output parser, context truncation, and response logs are absent. Sequential scoring across 1.5 years confounds model family/version with calendar time and potentially changing prompting practice. Each model appears to score each response once, so endpoint nondeterminism and within-model repeat reliability are not measured.

### Agreement and ensemble analysis

Quadratic weighted kappa (QWK) is computed separately between each AI and each human for each prompt and score type; human–human QWK is the baseline (pp. 5–9). This usefully exposes criterion and prompt heterogeneity. It does not make either human a criterion truth. With only 30 responses per prompt, each QWK is noisy, yet the paper supplies no confidence intervals, paired tests, multiplicity control, or score-distribution diagnostics alongside the kappas.

Six ensembles average selected model scores. Models are progressively removed based on observed performance, and the same 120 responses are then used to report improvement. There is no development/test split or predeclared selection rule, so ensemble gains are in-sample model selection. Averaging ordinal 0–6 outputs is also under-specified: the paper does not state rounding or how fractional ensemble values enter QWK.

### “Intra-rater consistency” analysis

Cronbach alpha is calculated across four holistic prompts, four prompts within each trait, twelve prompt–trait combinations, and six combinations within each task type (Table 5, p. 9). These are not repeated ratings of the same response. Alpha here reflects whether a rater preserves student ordering across different prompts/traits under a unidimensional internal-consistency model. It combines student proficiency stability, prompt difficulty/discrimination, trait covariance, and rater behavior.

Calling this “intra-rater consistency across prompts” is therefore misleading. The predictable rise in alpha with 12 rather than four items partly follows test length, which the paper itself notes. It cannot show that an LLM would reproduce its score on a second call, remain stable after endpoint drift, or apply one rubric consistently to equivalent evidence. A proper intrarater study needs repeated blinded ratings, crossed with prompt order and time.

### Many-Facet Rasch model

The reported rating-scale model is:

`log[P(X=k)/P(X=k-1)] = student ability − rater severity − prompt difficulty − category threshold`

with 30 students, four prompts, twelve raters, and common category thresholds (Equation 1 and pp. 5–6). Separate fits are reported for holistic scores, all analytic scores pooled, and each analytic trait. Rater severity, standard error, infit, and outfit are reported; 0.7–1.3 is chosen as the fit window (Tables 7–11).

The complete crossing creates connectivity, but critical identification and specification details are missing: which facet is centered or anchored; how the common score-scale origin is set; whether analytic traits are treated as repeated items or another facet; whether repeated ratings within student are conditionally independent; how missing/invalid outputs are handled; whether category thresholds are ordered; model–data fit beyond rater mean squares; separation/reliability indices; and FACETS version/control syntax. The paper notes that severity is mean-centered and changes with the included raters (p. 19), but does not carry that relativity into its “neutral rater” interpretation.

Most importantly, the additive model estimates average rater severity. It does not model rater-by-prompt, rater-by-trait, rater-by-student, or score-category interactions. The paper informally compares separate trait fits, but conducts no differential rater functioning test. Yet the QWK tables themselves show strong task dependence. A rater can have an acceptable pooled location and fit while being harsh on one task family and lenient on another.

## Evidence and results

Human–human holistic QWK ranges from 0.565 on SN2 to 0.874 on ER2 (Table 1), already showing that reference quality varies by prompt. The best AI–human pairing changes across all four prompts. Analytic Task Completion human–human QWK is 0.715–0.915, while Delivery falls to 0.588 on SN2 and Language Use to 0.488 on SN2 (Tables 2–4). “AI exceeds human agreement” is therefore pairing- and criterion-specific, not evidence that an AI is more accurate than humans.

The severity results are substantively useful. In holistic scoring, R2 is most lenient at −0.81 logits and Gemini 2.0 most severe at 1.25, with nominal SE 0.11 (Table 7). In pooled analytic scoring, the locations narrow: R2 is −0.55 and Gemini 2.0 is 0.76 (Table 8). Trait-specific estimates change again. OpenAI o1 is harshest for Task Completion (0.61); Gemini 2.0 is harshest for Delivery (1.03) and Language Use (1.06) (Tables 9–11). This is direct evidence that “rater severity” is criterion-conditional.

Fit flags are also conditional. Human raters show holistic infit/outfit around 0.58–0.60, which the authors interpret as possible central tendency; ChatGPT 3.5, DeepSeek R1, and Gemini 1.5 Pro exceed 1.3 on holistic fit. For Language Use, OpenAI o1 underfits the chosen lower boundary while Gemini 2.0 exceeds the upper boundary. But mean-square cutoffs are screening rules, not diagnoses. The paper does not inspect residuals, category usage, standardized fit, influence, or response-level cases, so labels such as centrality and misfit remain hypotheses.

The evidence does not support selecting one universally best AI grader. It does support requiring grader calibration by task and criterion and retaining severity/fit as distinct diagnostics from agreement.

## Unique insight

The paper’s deepest transferable insight is that **agreement, severity, and fit answer different questions**:

1. **Agreement:** does a grader rank and score responses similarly to a chosen reference under one prompt population?
2. **Severity:** does it shift the probability of higher categories relative to a linked rater panel?
3. **Fit:** are its response patterns compatible with the additive measurement model?
4. **Decision validity:** do resulting scores support a declared professional claim or action?

None entails the next. A high-QWK grader can be systematically harsh; a mean-centered “neutral” grader can disagree irregularly; a well-fitting grader can faithfully reproduce a flawed rubric; and severity adjustment can improve score comparability without establishing correctness.

This extends the AgentRewardBench review rather than duplicating it. AgentRewardBench shows that judge reliability depends on predicate, evidence view, prevalence, and error cost, and that a human label is not automatically truth. This paper adds **linked rater location and model-fit diagnostics** under a complete crossing. It also complements the plural-judgment review: systematic expert differences may reflect thresholds or evaluative frameworks, but a many-facet location parameter cannot identify which. Severity is descriptive measurement, not adjudication or legitimacy.

The operational implication is a calibration chain:

`connected design → reference-authority audit → agreement surface → rater location → interaction/fit diagnostics → repeat stability → decision-loss analysis → licensed claim`

Skipping from severity estimates to interchangeable grading collapses measurement into governance.

## Limitations and validity threats

1. **Tiny response population:** 30 students and four prompts provide only a narrow empirical base.
2. **Single educational domain:** AP Chinese writing cannot establish transfer to English, STEM, or multi-step knowledge work.
3. **Two human raters:** human authority and population-level rater variability are weakly identified.
4. **Trainer/reference dependence:** R1 trains the AI systems and is then used as an agreement criterion.
5. **Unknown exemplar leakage:** evaluated responses are not shown to be disjoint from “previously scored samples.”
6. **Unpinned configurations:** product names omit exact model IDs and inference settings.
7. **Calendar confounding:** sequential collection over 1.5 years confounds model/version with time and protocol drift.
8. **No repeated model calls:** stochastic intrarater reliability is unobserved.
9. **Alpha construct error:** internal consistency across different prompts/traits is interpreted as repeat rater consistency.
10. **No inferential uncertainty for QWK:** 30-response kappas have no intervals or paired comparisons.
11. **In-sample ensemble selection:** model removal and evaluation use the same responses.
12. **Ordinal averaging under-specified:** ensemble rounding and QWK treatment are absent.
13. **MFR identification incomplete:** anchoring, control file, threshold estimates, convergence, and facet reliability are not reported.
14. **Conditional independence questionable:** four responses and many ratings per student induce dependence not discussed.
15. **Common-threshold assumption untested:** rating-scale thresholds may differ by prompt, trait, human, or model.
16. **No differential rater functioning:** rater-by-task/trait interactions are described indirectly but not formally modeled.
17. **Fit labels overinterpreted:** cutoff violations are called centrality/misfit without residual or case analysis.
18. **Relative neutrality:** zero severity is panel-dependent and changes when raters are added or removed.
19. **No severity-adjusted outcome validation:** the study does not test whether adjustment improves decisions or external criteria.
20. **Human reference not validated:** certification and official rubrics establish relevance, not error-free criterion truth.
21. **No consequential analysis:** fairness, false pass/fail cost, subgroup effects, and audit routing are absent.
22. **No released implementation/data:** exact reproduction and independent model checking are blocked.
23. **Operational cost omitted:** latency, tokens, dollars, failures, and human oversight are not measured.
24. **Interchangeability overreach:** the favored models are not tested under replacement, drift, or held-out-task conditions.

## Reproducibility and operational realism

Reproducibility is weak. The immutable paper preserves the design, main equation, aggregate tables, one full example prompt/rubric, and score dispersions. That is enough to understand the intended analysis but not to reproduce it. Student responses, 1,440 rater–response records with four scores each, complete prompts, human rating records, model outputs, API manifests, FACETS control/output files, cleaning scripts, and ensemble code are unavailable. The exact fitted thresholds and convergence diagnostics are not reported.

Operational realism is also limited. The study uses real learner responses, certified raters, official prompt types, a complete crossing, and a rubric with score exemplars—stronger than abstract judge comparisons. But deployment would require endpoint pinning, repeat-call stability, secure handling, invalid-output policy, drift monitoring, held-out prompt calibration, subgroup fairness, adjudication, and explicit false-pass/false-fail costs. None is exercised. The paper evaluates score concordance on static short responses, not production grader service reliability.

## Transfer to skill-bench

### Add facet-aware diagnostics to existing metric records

Do not create a universal Rasch requirement. For sufficiently connected ordinal human/model grading designs, allow a calibration analysis to record:

- response/work-product facet, task/prompt family, criterion, rater/configuration, and category thresholds;
- anchoring/centering constraints and the exact linked population;
- severity/location estimates with uncertainty;
- infit/outfit or alternative residual diagnostics with declared screening thresholds;
- rater-by-task and rater-by-criterion interaction tests;
- missing/invalid semantics, dependence structure, and software/control-file provenance.

Every estimate must carry a `relative_to_panel` boundary. Removing a grader, changing tasks, or changing rubric categories creates a new calibration frame unless bridge items establish linkage.

### Separate calibration from score authority

A severity-adjusted score should be a derived measurement with immutable links to raw observations, model version, calibration panel, transformation, uncertainty, and intended use. It must not overwrite the original score or become an adjudicated “truth.” Validity arguments should explicitly prohibit upgrades from `relative severity estimated` to `professionally correct`, `fair`, or `deployment ready` without external evidence.

### Require repeat and interaction evidence

A scalable grader study should include blinded repeat calls/ratings, held-out tasks, and a connected assignment design. It should estimate at least:

- within-rater repeat stability;
- rater × task-family and rater × criterion interactions;
- agreement and confusion/cost surfaces against each independent reference;
- bridge-item drift across model/rubric versions;
- decision changes before and after any severity adjustment.

### Preserve plural judgment

Many-facet modeling can describe systematic thresholds, but it cannot decide whether one expert framework is legitimate, whether a disagreement is factual, or how stakeholders should aggregate. Preserve framework-indexed labels and adjudication lineage from the plural-judgment design; use severity as one diagnostic input, not a replacement for governance.

## Concrete changes for skill-bench

1. **Map this source into existing contracts rather than add a parallel psychometrics subsystem.** The metric-monitoring contract should permit panel-relative severity, fit, connectivity, and differential-rater diagnostics with explicit identification and uncertainty.
2. **Use the existing validity argument machinery to block overclaims.** A high QWK or adjusted score can support bounded concordance/comparability claims only for the linked task and rater population.
3. **Extend the planned plural-judgment conformance slice when built.** Include one planted case where two raters have equal pooled agreement but different severity, and one where pooled neutrality hides opposing task-family effects. Verify raw labels remain immutable and adjustment does not imply adjudication.
4. **Require configured-system identity for model graders.** Product family names and one temperature-zero call are insufficient; preserve endpoint/version, prompt and examples, settings, date, retries, output, and repeat evidence.
5. **Do not add a duplicate queue task.** Existing plural-judgment, metric-monitoring, task-health, grader evidence-view, and validity work can absorb these obligations; consolidation should cite this review when those artifacts are revised.

## Action items completed

- [x] Read the complete immutable v2 PDF/text, including methods, all result tables, discussion, references, and appendices.
- [x] Reconstructed sampling, complete crossing, human/AI prompting, QWK, alpha, ensemble, and Many-Facet Rasch analyses with page/table evidence.
- [x] Documented the absence of paper-linked code, data, full prompts, scoring records, and FACETS artifacts.
- [x] Audited human-reference authority, repeated-score dependence, model/time confounding, connectivity, identification, fit, missing uncertainty, and operational claims.
- [x] Compared nonduplicatively with AgentRewardBench and the plural-judgment review.
- [x] Added no queue task because existing build/consolidation work already covers the implied machinery.
