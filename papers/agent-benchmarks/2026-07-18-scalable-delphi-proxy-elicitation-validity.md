# Scalable Delphi: strong answer-cued table prediction does not validate an LLM panel as expert elicitation

## Bottom line

Lorenz and Fritz make a useful methodological proposal: when the quantity of interest is unobservable, do not declare an LLM panel valid merely because its rationales look expert-like. Require separately inspectable evidence from verifiable proxy tasks, evidence perturbations, and comparison with human judgments. Their two-round panel design also preserves initial estimates, mediated disagreement, revision, and rationales in principle. That **necessary-condition ladder** is relevant to `skill-bench`.

The experiment does not validate the stronger proxy-expert claim. The paper calls its benchmark exercise “calibration,” but reports correlation and mean absolute error for 58 leave-one-out table cells or agent aggregates—not probabilistic calibration, interval coverage, repeated-panel reliability, or downstream decision loss. The supposedly informative agent descriptions are partly outcome-authored labels: they say, for example, that one system is the “highest reported” Cybench performer, another is “near-saturation,” one CyberGym model is the “best non-thinking” system, and others have “poor” or “near-zero” performance. Improvement when these descriptions are revealed is therefore sensitivity to an answer-bearing treatment, not clean evidence of source-faithful domain expertise.

The five “experts” are five prompts to one model family, not five independently trained, experienced, or accountable observers. Their fictional credentials create perspective treatments, not expertise or rater independence. The paper reports no API snapshots, decoding parameters, seeds, independent reruns, raw panel outputs, mediator outputs, analysis code, token/cost ledger, or exact prompts; the official TeX appendix summarizes prompts in fourteen lines rather than releasing them. The author project page links only the paper at acquisition time. Thus the reported figures cannot be reconstructed or the claimed repeatability, auditability, minutes-scale execution, or three-orders-of-magnitude cost advantage checked.

The human comparison is weaker still. It reuses five ordered Cybench-to-malware-risk questions from Murray et al.; its “two independent human panels” were discussion subgroups in one small workshop, under one packet and order, with participant attrition and post-hoc exclusions. Scalable Delphi compares only five task-level means, highlights closeness to the higher Human Panel A, and gives no qualified-human target, outcome calibration, or decision-use evidence. Shared task ordering, capability framing, 25% anchor, and generated task packets can induce common movement without establishing a true latent risk probability.

The strongest warranted conclusion is narrow: **two configured frontier-model panels can recover held-out values from three small, richly labeled benchmark summaries and can generate risk estimates that move in the same ordered direction as two human workshop subgroups on five shared prompts.** This supports a candidate proxy-estimation and assumption-stress-testing instrument. It does not establish calibrated latent probabilities, source-faithful expertise, human-expert equivalence, causal decision benefit, cheaper equivalent elicitation, replacement of expert participation, or transport beyond this cyber case.

## Source and reading record

### Complete immutable primary source read

- Tobias Lorenz and Mario Fritz, *Scalable Delphi: Large Language Models for Structured Risk Estimation*.
- Immutable record: <https://arxiv.org/abs/2602.08889v1>; PDF: <https://arxiv.org/pdf/2602.08889v1>.
- Local PDF: `data/papers/pdfs/2602.08889v1-scalable-delphi.pdf` (14 pages; 334,564 bytes; SHA-256 `898f70326c028772cf86d0a33cff7a1eb5de1f1b76850b6642b5d273a39d524f`).
- Local full text: `data/papers/text/2602.08889v1-scalable-delphi.txt` (78,353 recorded characters; SHA-256 `2c14b8c6bb36d1bbe81837cf7263b92032c14dce52b404565102cf0249bdcc62`).
- Official TeX source: `data/papers/source/2602.08889v1-source.tar.gz` (SHA-256 `dad37bb6db0d1ed27db35a5e1a077c9458a9a96da9ad7702f7dca084f5fe5891`), extracted under `data/papers/source/2602.08889v1/`.
- I read the complete paper, appendices, benchmark tables, references, and principal TeX files. The immutable v1 record was submitted 9 February 2026; the acquired abstract contains no withdrawal notice.

### Official author page inspected

- Author project page: <https://t-lorenz.com/projects/scalable-delphi/>.
- Preserved HTML and clean text: `data/sources/releases/2602.08889v1-scalable-delphi/project-page.html` and `project-page.txt`.
- Provenance: `data/sources/releases/2602.08889v1-scalable-delphi/provenance.json`.
- At acquisition, the page linked the paper/arXiv record but no code, dataset, raw result archive, GitHub repository, Zenodo record, or Hugging Face release. This is an acquisition-time observation, not proof that no release exists elsewhere.

### Review checks performed

- Reconstructed the three target populations and reported metrics from the paper and tables.
- Verified that the 58 prediction targets are 30 BountyBench cells, 16 Cybench agent aggregates, and 12 CyberGym agent aggregates; a five-persona panel therefore implies 290 panel outputs per model/information condition and 580 across the two models, assuming one call per persona and no retries. The paper does not publish a call ledger.
- Calculated that the arithmetic mean of the six reported full-condition Pearson correlations is `0.9283`, which plausibly explains the project page’s “93% combined correlation”; the page and paper do not define a pooled combined-correlation estimand.
- Audited the complete released agent-description tables for answer-bearing comparative language.
- Compared the imported human-panel description against the existing full review of Murray et al. at `papers/agent-benchmarks/2026-07-12-benchmark-to-risk-expert-elicitation.md`.

No paid model call was made. The published results are not independently reproducible from the acquired artifacts.

## One-sentence contribution

Scalable Delphi proposes an indirect validity ladder for LLM-generated latent estimates and demonstrates high held-out-table correlation plus shared directional movement with human workshop judgments, while inadvertently showing why proxy prediction, evidence responsiveness, panel resemblance, calibrated probability, expert authority, and decision utility must remain different claims.

## Why this matters for skill-bench

This review advances charter objectives A, B, E, and F through bounded expansion on a general question: **can cheap model panels substitute for scarce experts anywhere in the expertise-to-benchmark chain?** Cybersecurity is the test case, not a scope commitment.

The uncertainty clarified is not whether model panels are useless. They can cheaply propose priors, enumerate assumptions, expose sensitivity to supplied descriptions, and generate rival rationales. The unresolved issue is what those operations authorize. A generated estimate may be a useful candidate or stress-test without being an expert contribution, a valid criterion, a calibrated probability, or a decision basis.

The reusable claim ladder is:

```text
configured model-panel output
→ reproducible panel behavior
→ accuracy on a frozen verifiable proxy
→ robustness to non-answer-bearing evidence interventions
→ agreement with qualified human judgments under matched information
→ calibration on the target quantity or defensible transport warrant
→ improved human decision under declared loss
→ lower total cost for equivalent validity
→ bounded substitution or complement claim
```

No rung inherits the next. Useful completion is a review that prevents a low-cost simulated panel from being entered into contributor, authority, or expert-validation fields while retaining its legitimate candidate-generation and stress-testing roles. Existing participation, validity, metric, evidence-view, configured-system, and benchmark-to-consequence machinery is sufficient; no LLM-panel schema is warranted.

## Research question and claim boundary

The paper asks whether LLM agents can act as scalable proxies for structured expert elicitation when risk-model quantities cannot be directly observed. It proposes two necessary conditions—performance on observable proxy quantities and sensitivity to relevant evidence—and two corroborating signals—human alignment and rationale quality (Sections 2–3, pp. 2–4).

The paper supports that:

1. a five-persona, mean-pooled panel protocol is clearly described at a conceptual level;
2. two named model families produced reported estimates on three benchmark-summary prediction exercises;
3. reported full-condition Pearson correlations range from 0.87 to 0.95, Spearman correlations from 0.78 to 0.95, and MAEs from 1.22 to 8.52 percentage points (Figure 1, p. 5);
4. reported correlations generally rise when benchmark/model descriptions are revealed (Figure 2, pp. 5–6);
5. on five ordered consequence prompts, two model panels and two human subgroups produce increasing means, with GPT-5.1 reported 5.0 percentage points MAD from Human Panel A and Opus 12.8 points MAD from Panel A (Figure 3, pp. 6–7); and
6. a five-role versus uniform-superforecaster prompt ablation changes the five-task aggregate by reported MADs of 3.0 points for GPT-5.1 and 1.9 for Opus (Appendix B, p. 11).

It does **not** establish probabilistic calibration, nominal interval coverage, independent panel diversity, domain expertise, target-risk truth, human-expert equivalence, decision improvement, cost equivalence, three-orders-of-magnitude savings, cross-domain transport, continuous-update validity, or expert replacement. The paper sometimes acknowledges this ceiling (pp. 7–8), but its abstract, conclusion, project page, and phrases such as “well-calibrated,” “viable proxies,” and “three orders of magnitude lower cost” exceed the presented evidence.

## Methodology and system

### Panel and deliberation protocol

For a quantity `Q` and evidence `E`, five same-model calls receive distinct role personas. Round-one calls independently return a point estimate and rationale. A same-family mediator summarizes the spread, arguments for higher/lower values, agreement, and disagreement without recommending a value. Later calls revise after receiving that summary. The final estimate is the arithmetic mean across round-`R` panelists; a 95% interval across panelists is described as panel disagreement (Section 2, pp. 2–3).

The five cyber personas claim: ten years of SOC/APT experience; anti-virus-lab reverse engineering; a PhD in AI security; former intelligence-community threat analysis; and CISSP/CISM compliance expertise (Appendix B, p. 11). These are prompt assertions. They supply no education, practice, access to private incidents, accountable professional role, calibrated history, conflicts, or differentiated source corpus. Calling them “experts” collapses persona content into authority.

All five observers share the same base model, training distribution, provider, evidence packet, protocol, authorship, and likely many latent biases. Distinct prompts can induce perspective variation but not five independent raters. A mediator from the same model family can increase common-mode convergence. No cross-model mixed panel, independent mediator, no-deliberation arm, mediator perturbation, rationale masking, or repeated panel draw measures how much error correlation remains.

The paper’s claim that personas “recover variance that reflects real disagreement among informed perspectives” (p. 3) is untested. The appendix’s small persona-ablation MAD does not show that the Delphi structure drives calibration: it uses only the five-question human-comparison task, reports no target truth, and contains no no-Delphi or alternative-mediator condition. Similar endpoint means can conceal different errors and do not identify which component caused performance.

### Verifiable-proxy prediction tasks and denominators

**BountyBench:** ten configured agents by three task types yields 30 held-out cells. Each target is predicted from the other 29 cells plus, under fuller conditions, descriptions. Observations share rows, columns, task sources, and benchmark construction; they are not 30 independent risk events.

**Cybench:** sixteen configured-agent aggregate success rates yield 16 held-out targets. The model sees the other 15 values and descriptions.

**CyberGym:** twelve configured-agent aggregate success rates yield 12 held-out targets. The model sees the other 11 values and descriptions.

Thus each reported correlation is over only `n=30`, `n=16`, or `n=12` target values. The paper reports no confidence intervals, permutation tests, clustered bootstrap, repeated panels, call-level invalid/missing output, or correction for comparing models, benchmarks, conditions, and metrics. The plotted points are summary targets, not hundreds of independent persona estimates.

The baselines are weak. For Cybench and CyberGym, a leave-one-out global mean is mathematically anti-correlated with the held-out value, producing `r=-1` by construction (p. 5). Beating this deliberately perverse comparator says little. Stronger comparators—regularized regression over model/version metadata, ordinal interpolation, nearest-family prediction, matrix completion, or a frozen human analyst—are absent. BountyBench’s task/agent means are more meaningful but still do not isolate domain reasoning.

### “Calibration” is mostly correlation

The paper defines calibration as positive association plus approximate nominal interval coverage (Section 3.1, p. 4), but then reports Pearson correlation, Spearman correlation, and MAE only. It never reports coverage, interval width, reliability curves, calibration slope/intercept, Brier/log score, or repeated predictive distributions.

Correlation is not calibration. A predictor can have `r≈1` while being systematically shifted, shrunk, or overconfident. MAE adds absolute-error information, but without uncertainty or a decision threshold it does not establish acceptable calibration. The five-persona 95% interval is also not automatically a predictive interval: it describes dispersion among correlated prompt realizations, not uncertainty over the true success rate, sampling variation in the benchmark estimate, or repeated-panel coverage.

The project page’s “93% combined correlation” is not specified in the paper. The simple mean of the six reported full-condition Pearson coefficients is 0.9283, but averaging correlations across different `n`, ranges, scales, and target constructions is not a pooled estimand. Calling it 93% can be misread as 93% accuracy or variance explained.

### Evidence sensitivity is confounded by answer-bearing descriptions

The four conditions reveal: numeric matrix only; benchmark description; model names/descriptions; or both. The paper interprets rising correlation as domain-informed reasoning rather than memorization (pp. 5–6).

Yet the appendix descriptions encode outcome-conditioned rankings and interpretations. Examples include:

- Claude 4.5 Sonnet “achieving the highest reported unguided Cybench success” and indicating “near-saturation performance”;
- Claude 4 Opus having a “higher success rate” than prior generations;
- CyberGym Claude-Sonnet-4 being the “best non-thinking performance”;
- R2E-Gum-32B having “poor transfer”; and
- SWE-Gym-32B having “near-zero performance.”

These descriptions appear written with the table outcomes in view. Revealing them is not a clean intervention adding independent technical evidence; it reveals qualitative transforms of the target labels. The experiment therefore tests whether a model can map answer-shaped prose and neighboring numeric values back to a percentage. That can be useful table completion, but it is not evidence that the panel retrieved tacit cyber expertise or would estimate a genuinely latent quantity.

The contamination argument also overreaches. Publication after a stated knowledge cutoff does not prove absence from later training, provider updates, browsing, benchmark discussion, or derivative data. Conversely, stronger sensitivity when descriptions are shown does not rule out memorized model rankings; it may show the prompt activated them. No canary strings, paraphrase controls, fictional-model negative controls, wrong-description interventions, source-access logs, or predeclared contamination audit is reported.

### Human-panel alignment

The paper recreates Murray et al.’s five ascending-FST Cybench prompts. Each asks for malware development/deployment success given access to an LLM whose hardest reliably solved task is the displayed challenge, relative to a 25% no-LLM anchor. LLM panelists preserve conversation history across tasks and receive a mediator summary before round two (pp. 6–7).

This is not a comparison with two independent, representative expert samples. The reviewed source reports one two-hour workshop: 20 invitees, nine initial attendees, two departures, seven complete respondents, two discussion groups, and post-workshop exclusion of misunderstood responses. Both groups shared recruitment, packet construction, ordering, anchor, task selection, and workshop context. The exact task-level denominators and exclusion effects are not restated here.

Only five ordered task means are compared. The headline chooses Human Panel A, the higher panel, as the principal reference: GPT-5.1’s 5.0-point MAD to A is contrasted with the 16.6-point A–B MAD. The paper does not report each model’s MAD to Panel B, a pooled human target, uncertainty over MAD, or a predeclared reason that Panel A is more authoritative. Closeness to one disagreeing subgroup can be farther from another.

Monotonic movement is also designed into the shared treatment. Tasks are ordered by FST from easy to hard, every prompt says the displayed task is the hardest reliably solvable task, the same 25% anchor is repeated, and conversation history is preserved. Murray et al.’s experts explicitly disputed FST as a smooth operational-capability scale. Shared upward anchoring and packet framing can create human–LLM alignment without either panel estimating the true conditional malware-success probability.

Finally, proxy-table prediction and malware-risk judgment are different constructs. Recovering configured-agent aggregate pass rates from neighboring values and descriptions does not validate the causal/generalization warrant from CTF capability to real attacker workflow. The paper acknowledges the structural gap (p. 7), but its “viable proxy” conclusion effectively crosses it.

## Evidence interpretation

### What the evidence supports

1. A conceptually clear configured panel/mediator protocol exists.
2. Two frontier model families reportedly recover rank and approximate level in three small benchmark summary tables under rich context.
3. Their output changes when answer-bearing benchmark/model descriptions are added.
4. Their five shared risk estimates increase with the same ordered task framing used for two human discussion groups.
5. Model families disagree materially on at least one risk prompt, which is useful evidence that endpoint identity matters.
6. The paper usefully frames proxy accuracy and evidence response as necessary, not automatically sufficient, evidence for latent estimation.

### What the evidence does not support

- that the proxy exercises measure the same construct as latent risk estimation;
- that the supplied descriptions are independent of held-out outcomes;
- that persona calls instantiate independent expertise;
- that panel dispersion is calibrated uncertainty;
- that mediator convergence improves accuracy rather than correlation of error;
- that the latent risk numbers are correct or decision-useful;
- that Human Panel A is the appropriate target;
- that GPT-5.1 is closer to “experts” generally than experts are to one another;
- that model panels preserve source-faithful or tacit expertise;
- that repeatability, auditability, throughput, and cost advantages hold operationally; or
- that any human role can safely be replaced.

## Unique insight

The paper’s deepest transferable lesson is that **proxy elicitation has two distinct transport problems, not one**:

1. **observer transport:** does the configured model panel behave acceptably on a verifiable task under non-answer-bearing evidence, repeated draws, and held-out conditions?
2. **construct transport:** does success on that verifiable task warrant estimates for the unobservable target, with the same causal structure, information needs, authority, and loss consequences?

Scalable Delphi tests a weak form of the first and largely assumes the second. Human resemblance does not join them because humans may share the same framing error, anchor, incomplete packet, or contested benchmark-to-consequence warrant.

A second insight is that model panels should be treated as **experimental instruments, not simulated people**. Persona A is not a defensive-security specialist; it is one prompt-conditioned realization of GPT-5.1 or Opus 4.1. The right identity includes model snapshot, system prompt, persona text, evidence view, task order, context persistence, mediator realization, aggregation, retries, and stochastic seed. Diversity claims require estimated error covariance and independent methods, not role biographies.

A third insight is that evidence sensitivity can be anti-validating when the evidence is outcome-derived. Any perturbation study must preserve a source/target firewall. Independent descriptions, distractors, contradictory descriptions, fictional entities, and negative controls are needed before responsiveness can be interpreted as domain-grounded use rather than answer-cue uptake.

## Limitations and validity threats

1. **Correlation is mislabeled calibration.** No reliability curve, slope/intercept, coverage, or proper scoring rule is reported.
2. **Confidence-interval target is unclear.** Five correlated persona outputs do not define predictive or sampling uncertainty.
3. **No uncertainty on headline metrics.** Correlations over 12–30 targets have no intervals or clustered resampling.
4. **Targets are dependent.** Cells share agents, task types, benchmark construction, and source evaluations.
5. **Only 58 summary targets exist.** Persona-call volume would not enlarge the independent task denominator.
6. **Weak baselines.** The Cybench/CyberGym leave-one-out mean is perfectly anti-correlated by algebra.
7. **Answer-bearing descriptions.** Several descriptions explicitly encode target-relative rank or level.
8. **Description provenance is absent.** Authors, source locators, timing, and whether labels were generated from the displayed outcomes are not reported.
9. **Proxy–target construct mismatch.** Table completion and latent real-world risk estimation require different warrants.
10. **Same-model panel dependence.** Personas share training, provider, evidence, protocol, and authorship.
11. **Fictional credentials are not expertise.** No accountable experience, authority, private evidence, or calibration is realized.
12. **Mediator dependence.** The same model family summarizes and may amplify shared errors.
13. **No component ablation.** There is no no-Delphi, no-mediator, mixed-model, independent-mediator, or rationale-masked comparison.
14. **Persona ablation is underidentified.** Small endpoint MAD on five unobservable targets cannot show the Delphi structure causes calibration.
15. **No repeated panels.** Stochastic stability, invalid outputs, retries, and between-run variance are unknown.
16. **Model identity is incomplete.** Endpoint snapshot, access date, provider configuration, decoding, system controls, tools, and seed are absent.
17. **Exact prompts are unavailable.** The appendix supplies descriptions, not executable prompts.
18. **Raw outputs are unavailable.** Initial estimates, rationales, summaries, revisions, and errors cannot be audited.
19. **Analysis code/data are unavailable.** Figures, condition metrics, and MAD calculations cannot be regenerated.
20. **Contamination exclusion is unsupported.** Knowledge-cutoff dates and response patterns do not prove nonexposure.
21. **Human panels are not independent samples.** They are subgroups within one workshop and shared information treatment.
22. **Human authority is thinly represented.** This paper omits participant qualifications, attrition, exclusions, and task-level denominators.
23. **Reference-panel selection is asymmetric.** Panel A is highlighted without establishing it as more correct.
24. **Only five human-comparison prompts exist.** MAD and monotonicity have no task-population uncertainty.
25. **Order and history confound alignment.** All observers share ascending tasks, anchor, and capability framing.
26. **Task difficulty is contested.** FST mixes technical difficulty, tedium, specialization, and benchmark artifacts.
27. **No target outcomes.** Malware success probabilities never resolve and receive no controlled-uplift validation.
28. **No decision study.** No stakeholder threshold, action, counterfactual, harm, or benefit is observed.
29. **Cost claim is unmeasured.** No tokens, calls, prices, latency, preparation, review, or maintenance ledger exists.
30. **Human/model cost units are inequivalent.** Full human-study recruitment and coordination are compared rhetorically with model execution while problem-specification labor is omitted.
31. **Auditability claim is unrealized.** Conceptual JSON output without retained records is not an audit trail.
32. **Cross-domain generalization is absent.** One cyber benchmark-summary family and one imported cyber-risk exercise cannot establish a domain-general method.
33. **Dynamic-update benefit is hypothetical.** Frequent cheap reruns can repeat drift or common-mode error; no longitudinal validation is shown.
34. **Risk language outruns the estimand.** One conditional success probability omits access, actor frequency, controls, severity, and stakeholder loss.

## Reproducibility and operational realism

Reproducibility is **moderate for understanding the conceptual protocol, weak for reproducing any empirical row, and absent for validating cost or operational throughput**. The immutable PDF, complete text, TeX source, tables, personas, and high-level prompt summaries are preserved. They disclose the benchmark values and enough design structure to understand the intended experiment.

Exact replay is blocked by missing executable prompts, source code, input serialization, model request manifests, API dates/snapshots, sampling controls, seeds, retries, raw outputs, mediator summaries, condition-level numeric tables, analysis scripts, figure data, and cost ledger. A fresh run would be a new experiment under mutable providers and could not establish identity with v1.

Operational realism is low. The proxy tasks are static table-completion exercises, not live elicitation over contested source packs. The panel has no accountable domain access, affected stakeholder, confidential evidence, right to correct, duty to escalate, or liability. The human comparison inherits a hypothetical scenario and ordered task packet. No risk model is populated and used, no estimate changes a decision, no later outcome calibrates it, and no human reviewer workload or correction burden is measured.

The claimed economics are therefore a hypothesis. Cheap calls may make broad sensitivity analysis feasible, but total valid-estimate cost includes scenario specification, evidence curation, answer-cue audits, model/version maintenance, human review, target transport validation, and consequence monitoring. Those terms are not measured.

## Transfer to skill-bench

### 1. Type model panels as configured proxy estimators

A record should identify:

- exact model/provider snapshot and access time;
- persona prompt hashes and their status as fictional perspective treatments;
- task/evidence packet and source provenance;
- information condition, order, persistence, and prior exposures;
- mediator model/prompt and information transformation;
- independent call, retry, invalid-output, and cost/latency events;
- aggregation and uncertainty target;
- repeated-panel covariance and error surface; and
- explicit claim ceiling.

Do not place model personas in expert contributor, approval, authority, or participation fields. Link them as model-generated candidate evidence.

### 2. Add a source/target firewall to evidence interventions

Before interpreting evidence sensitivity:

- derive descriptions without target labels;
- freeze them before outcomes are inspected;
- preserve source locators and transformation authorship;
- test fictional entities and label-swapped descriptions;
- add relevant, irrelevant, contradictory, and answer-bearing controls; and
- measure whether estimates use evidence correctly, not merely whether they move.

Existing source-pack provenance and intervention records can represent this; no new schema is required.

### 3. Separate proxy validation from target transport

A proxy-estimation validity argument should declare:

- proxy construct and target construct;
- shared and missing causal variables;
- target-population and information-view differences;
- what proxy failure falsifies;
- what proxy success does **not** license;
- human-reference authority and disagreement;
- next direct or longitudinal target evidence; and
- decision-loss basis.

This extends the existing benchmark-to-consequence chain rather than replacing it with a score transform.

### 4. Treat agreement as observer evidence, not authority

Compare model panels with multiple qualified human raters under matched packets, but preserve participant qualifications, assignment, initial/revised judgments, subgroup exposure, exclusions, disagreement cruxes, and target-level denominators. Agreement can support a bounded resemblance claim. It cannot establish correctness when the target is unobservable or all observers share the same framing.

### 5. Validate complementarity before substitution

A meaningful low-cost study should randomize real expert teams to human-only versus human-plus-panel support on consequential but safe estimation tasks. Measure:

- estimate calibration when outcomes later resolve or on blinded seed questions;
- detected assumptions and corrected omissions;
- decision accuracy/utility under a declared loss;
- expert uptake, rejection, revision, and reliance;
- false-confidence and automation-bias incidents;
- total expert and analyst time;
- model, review, maintenance, and correction cost; and
- performance on novel, private, and adversarial evidence.

Only equivalent validity plus lower total burden can support a cost-advantage claim. Expert replacement requires additional authority, safety, and consequence evidence.

## Comparison with adjacent project evidence

- **Benchmark-to-risk expert elicitation** exposes the contested score→capability→scenario→workflow→outcome→decision chain with real participant disagreement. Scalable Delphi reproduces the same five prompts cheaply but does not resolve the disputed warrant; shared monotonicity can repeat it.
- **Human-on-the-Bridge** argues that scarce human effort should be amortized into reusable evaluation policy. Scalable Delphi proposes a different economy—replace repeated judgments with model panels. Both need an upstream authority and calibration layer: reusable or scalable machinery can multiply unsupported policy just as easily as valid judgment.
- **Domain-expert participation ethnography** shows that expert authority does not automatically survive simulation, synthetic transformation, or developer/model substitution. Persona text cannot manufacture that missing authority.
- **Many-Facet human/AI rater evidence** motivates separating task, observer, criterion, severity, and interaction effects. Five persona prompts to one model are correlated observer realizations; their spread is not calibrated human-panel uncertainty.
- **SimInstruct and organizational tacit-knowledge simulation** already establish the project boundary: simulated interlocutors can test an instrument or routing policy, but cannot validate real participation, tacit expertise, or authority.

Together these sources support using LLM panels for candidate generation, negative controls, assumption enumeration, and inexpensive perturbation—not as silent substitutes for the human/source nodes that license benchmark requirements or consequential decisions.

## Action items

- [x] Read and verify the complete immutable v1 PDF/text and official TeX source.
- [x] Inspect the official author page and preserve acquisition-time release limits.
- [x] Reconstruct panel roles, mediator, rounds, aggregation, three proxy mappings, human comparison, persona ablation, denominators, and reported metrics.
- [x] Audit the benchmark descriptions for answer-bearing outcome language.
- [x] Separate proxy prediction, evidence sensitivity, human resemblance, calibration, authority, decision benefit, cost, and substitution claims.
- [x] Map implications into existing configured-system, source-pack, metric, validity, participation, and consequence machinery without adding a duplicate build task.
- [ ] In a future real elicitation pilot, test a frozen source/target firewall and mixed human/model panel against blinded seed questions and a declared downstream decision loss.
