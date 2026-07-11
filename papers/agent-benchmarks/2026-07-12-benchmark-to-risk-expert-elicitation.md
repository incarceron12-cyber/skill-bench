# Paper Review: Mapping AI Benchmark Data to Quantitative Risk Estimates Through Expert Elicitation

- **Paper:** https://arxiv.org/abs/2503.04299v2
- **Authors:** Malcolm Murray, Henry Papadatos, Otter Quarks, Pierre-François Gimenez, and Simeon Campos
- **Date read:** 2026-07-12
- **Venue / source:** arXiv preprint
- **Tags:** expert-elicitation, consequential-validity, risk-modeling, cybersecurity, benchmark-interpretation, structured-judgment
- **Version read:** immutable v2, submitted 10 March 2025
- **Local PDF:** `data/papers/pdfs/2503.04299v2-benchmark-to-risk-expert-elicitation.pdf` (23 pages; SHA-256 `d27d10005b94667689e69eaa857b66e340e81fd05d8f95424d6b25b0dcf3dcf7`)
- **Local text:** `data/papers/text/2503.04299v2-benchmark-to-risk-expert-elicitation.txt` (SHA-256 `9e37ace3c6887011482c3a66bbf903d78bcb74b032584ee272063e5774303b1e`)

## One-sentence contribution

The paper pilots a structured process for turning a benchmark capability boundary into an expert-judged conditional event probability, but its most defensible result is not the reported cyber-risk uplift: it is an empirical demonstration that the benchmark-to-consequence **warrant** is a high-variance, assumption-sensitive object that must be elicited and tested separately from the benchmark score.

## Why this matters for skill-bench

This review advances charter objectives A, B, and E. `skill-bench` already separates measurements, validity claims, expert participation, and monitoring metrics; this paper tests the difficult bridge between them. Its bounded cybersecurity case asks a general cross-domain question: when an agent can complete benchmark tasks, what additional evidence licenses a prediction about a consequential workflow state?

The concrete artifact is this source-grounded review and a reusable benchmark-to-consequence inference-chain design. The uncertainty clarified is whether expert elicitation can directly promote a benchmark result into a quantitative risk estimate. The study shows it can produce numbers, rationales, and visible disagreement, but does not show those numbers are calibrated, causally identified, externally valid, or decision-useful. This is expansion with immediate consolidation implications, not a proposal to narrow the benchmark to cybersecurity.

Useful completion means repository reports cannot silently move from “configured system solved task X” to “system raises outcome probability by Y.” Each intermediate target, assumption, evidence view, aggregation rule, and unresolved crux must remain inspectable.

## Research question

The paper asks whether performance on an existing AI capability benchmark can inform quantitative estimates used in a real-world risk model. Its pilot focuses on one conditional node in a six-component cyberattack scenario: the probability that a cybercrime group successfully develops and deploys malware, given that it completed earlier attack steps and has access to an LLM’s capabilities (Sections 4.1–4.1.1, pp. 3–4).

That question is narrower than “What is cyber risk?” The complete model also needs actor counts, attempt rates, probabilities of initial access and objective achievement, model-capability access, and damage severity. The study estimates none of those. It asks experts how one conditional success probability changes as the hypothetical model’s maximum reliably solved Cybench task increases.

## Methodology

### Scenario and estimand

The authors describe a targeted attack on an S&P 500 company as a six-component pathway containing frequencies, conditional probabilities, and eventual economic damage (Figure 2 and Section 4.1.1, p. 4). They isolate Step 4, successful malware development and deployment. Participants are instructed to estimate:

> `P(malware development/deployment succeeds | prior steps succeeded, actor can access and use the stated model capabilities)`

They are given a 25% no-LLM baseline from a separate, then-forthcoming forecaster study. Access probability is explicitly outside the elicited target, and the model may be used through any scaffold (chatbot, tools, or otherwise). This separation is conceptually valuable, although the open scaffold policy leaves the treatment heterogeneous.

### Mapping benchmark evidence to scenarios

Cybench contains 40 capture-the-flag tasks. The authors select five predominantly offensive, malware-adjacent tasks spanning First Solve Time (FST) from seven to 330 minutes: *It Has Begun*, *Network Tools*, *Unbreakable*, *Just Another Pickle Jail*, and *Frog WAF* (Section 4.1.2 and Table 1, pp. 5–6). Experts are told, for each condition, that the displayed task is the hardest task the hypothetical LLM can solve. The five tasks therefore function simultaneously as concrete capability descriptions and ordered anchors on FST.

The evidence packet is not the original benchmark alone. Because original README coverage was inconsistent, the authors generated uniform summaries with Claude 3.5 Sonnet from task files and had a Cybench creator review them (Section 4.2, p. 6; Appendix B, pp. 15–23). The appendices reveal that these summaries include challenge overviews, detailed exploitation paths, security controls, and “skills required/learned.” Thus the elicitation treatment combines task identity, FST, author-generated interpretation, and solution-adjacent capability framing. It cannot isolate which element changed judgments.

FST is treated as a difficulty axis because Cybench reported that high-FST model successes rarely occurred without lower-FST successes, and external evaluations located current model frontiers around lower FST ranges (pp. 5–6). Yet the experts themselves challenged this ordering: tediousness, specialized knowledge, and benchmark idiosyncrasy can raise FST without implying broad operational capability (p. 8 and Appendix A).

### Elicitation protocol and sample

The two-hour remote workshop adapts the IDEA protocol—Investigate, Discuss, Estimate, Aggregate—a modified Delphi approach intended to resolve ambiguity and expose evidence rather than force consensus (pp. 3 and 6). For each task, participants receive 15 minutes:

1. 7.5 minutes to read and record an initial probability plus rationale;
2. 5 minutes to inspect peer estimates and discuss in a moderated subgroup;
3. 2.5 minutes to submit a revised estimate.

Twenty experts selected for expertise at the cybersecurity/AI intersection were invited; eleven accepted, nine attended initially, two left after one hour, and seven answered all questions. Participants represented research labs, government, academia, and think tanks; those able to accept payment received $200 (Section 4.3, p. 6). The paper lists nine consenting names and affiliations but does not provide a predeclared expertise rubric, years of operational malware experience, elicitation training, conflicts, recruitment frame, or participant-level role mapping.

Participants were split into two groups, balancing organizations and sectors. This produced two deliberative clusters rather than seven independent observations. Two experts’ responses were excluded after post-workshop discussion established question misinterpretation (Section 5, p. 6). Appendix A’s displayed table is also sparse: several cells and rationales are blank, so the complete analysis dataset and exclusion lineage are not independently reconstructible from the manuscript.

### Aggregation and interpolation

The authors pool groups and report mean final estimates with confidence intervals, then fit an MCMC-based Bayesian interpolation from FST to estimated malware-success probability (pp. 6–7). They say Bayesian modeling reduces overfitting and gives less weight where experts disagree, but do not specify the likelihood, functional form, prior, hierarchical structure, monotonicity constraint, chain diagnostics, posterior summaries, interval definition, or code. Figure 3 is explicitly illustrative rather than a source of precise point estimates.

This matters because the observations are repeated judgments from the same experts, nested within two discussion groups, based on five deliberately ordered tasks. A model that treats estimates or task anchors as independent would understate dependence. The paper supplies no calibration questions or seed variables with known outcomes, no performance weighting of experts, no holdout event, and no comparison against alternative pooling rules.

## Evidence and results

The manuscript reports a 25% baseline, approximately 30–35% estimated success with current-model Cybench capability, and roughly 40–65% for systems reaching the high-FST end (Introduction, pp. 1–2). The raw appendix better communicates the evidence than those ranges. Final estimates for *Frog WAF*, for example, split near 38% in Group B and 70–75% in Group A (Appendix A, p. 15). The groups developed different warrants:

- **Group A:** hard CTF performance indicates technically meaningful assistance to relatively weak cybercrime groups and approaches real offensive complexity.
- **Group B:** isolated CTFs omit messy integration, defensive evasion, and the skill of orchestrating models, so they weakly predict end-to-end malware operations.

Discussion changed some extreme initial judgments—the first-task 75% estimate became 30%—which shows value in assumption exposure. But deliberation also induced within-group dependence and possibly convergence around local narratives. The authors appropriately acknowledge ordered-task upward pressure, short deliberation, ambiguity over defense strength, actor skill, time horizon, consistency versus one-shot success, retries, and task representativeness (pp. 8–9).

The study empirically supports only that a small group of invited experts, under this information and discussion protocol, produced different conditional probabilities and articulated identifiable validity cruxes. It does **not** validate the true probability, the 25% baseline, the FST mapping, the reported intervals, or a causal LLM uplift.

## Unique insight

The paper’s unique contribution for `skill-bench` is to make the **inference gap observable as data**. Expert disagreement is not merely annotation noise to average away. Here it localizes a contested causal/generalization warrant: whether solving isolated technical challenges transfers to orchestrated action under realistic defenses and organizational constraints.

That suggests a stronger benchmark design than a direct score-to-risk curve. Treat each consequence estimate as the end of a typed chain:

1. **benchmark observation:** a pinned configured system succeeds under defined retries, tools, and environment;
2. **capability interpretation:** the observation supports a bounded capability description;
3. **scenario applicability:** the capability is available, relevant, and usable by a specified actor under stated conditions;
4. **workflow effect:** it changes one conditional transition probability relative to a defined counterfactual;
5. **outcome composition:** the transition combines with other dependencies, frequencies, controls, and severity;
6. **decision use:** a stakeholder applies a threshold and loss model.

Experts may provide evidence at links 2–4, but their judgment does not convert links 5–6 into empirical facts. More importantly, elicitation should record rival warrants—not merely pooled probabilities—because those warrants tell benchmark builders which study to run next. In this pilot, an uplift study measuring end-to-end actor performance under realistic defenses would resolve more uncertainty than adding another CTF at a finer FST increment.

A second insight is that benchmark metadata can become an intervention. FST, task descriptions, generated “skills” summaries, ordering, and claims about reliable solution each shape the expert’s mental model. A consequence-elicitation record therefore needs immutable information-condition provenance, just as an agent trial needs model and harness provenance.

## Transferable design patterns

### 1. Benchmark-to-consequence inference record

This is a `skill-bench` adaptation, not an artifact supplied by the authors:

```yaml
inference_id: consequence-inference/...
benchmark_evidence:
  configured_system_ref: ...
  task_population_ref: ...
  measurement_ref: ...
  reliability_definition: ...
  information_packet_ref_and_hash: ...
capability_claim:
  bounded_text: ...
  supported_and_excluded_interpretations: [...]
scenario_node:
  event: ...
  conditioning_events: [...]
  actor_population: ...
  environment_controls: ...
  time_horizon: ...
  treatment_access_and_use_policy: ...
counterfactual:
  baseline_source_ref: ...
  treatment_contrast: ...
elicitation:
  protocol: ...
  participant_authority_and_scope_refs: [...]
  initial_estimates_and_rationales: [...]
  discussion_group_and_exposure: ...
  revised_estimates_and_corrections: [...]
  assumption_and_crux_records: [...]
aggregation:
  estimand: ...
  dependence_model: ...
  pooling_rule_and_code_ref: ...
  uncertainty_and_sensitivity: ...
calibration:
  seed_questions: [...]
  held_out_validation: [...]
claim_boundary:
  licenses: ...
  does_not_license: [...]
  next_discriminating_evidence: ...
```

This should link to, not duplicate, existing validity-argument, metric-monitoring, expert-participation, and elicitation-session objects.

### 2. Preserve disagreements as competing model specifications

When groups disagree because they assume different actor expertise, defenses, scaffolds, or task-to-work transfer, do not report only a wider interval. Convert each disagreement into an explicit scenario fork or sensitivity variable. Pool only judgments that target the same estimand and information condition.

### 3. Separate five quantities

A benchmark report should never collapse:

- benchmark success probability under a pinned system;
- probability that the actor can access and effectively use that capability;
- conditional workflow-transition probability;
- frequency and severity of the final outcome;
- utility or loss supporting a decision.

The paper explicitly separates capability access from conditional success and final damage, but its headline “risk” language can still invite readers to conflate them.

### 4. Elicit warrants before probabilities

A better protocol would first ask participants to define the actor, environment, defense, time, retries, model reliability, and relevant transfer mechanism; then resolve incompatible targets; then elicit probabilities. Probability revision should preserve whether movement came from corrected ambiguity, new evidence, social influence, or changed assumptions.

### 5. Use consequence elicitation to design validation studies

The main output should be a ranked list of uncertainty-reducing experiments. In this case: matched human/LLM uplift studies on end-to-end malware-development workflows, factorial variation in actor expertise and defenses, and repeated tasks testing whether FST predicts transfer after controlling for task family and specialized knowledge.

## Limitations

1. **Tiny, selected, clustered sample.** Seven complete respondents, two discussion groups, and post hoc exclusions cannot support stable population claims about cyber experts.
2. **Expertise is asserted, not operationalized.** No eligibility rubric, proficiency measure, calibration score, role-specific authority, or analysis by relevant experience is reported.
3. **No expert calibration.** Participants answer no seed questions with knowable outcomes; equal averaging has no demonstrated calibration advantage.
4. **Ambiguous and changing estimand.** Defense, actor skill, duration, reliability, retries, scaffold, and representativeness were interpreted differently. Excluding two respondents does not establish that the remaining five or seven targeted one quantity.
5. **Order confounds capability with anchoring.** All tasks appear in ascending FST, creating the upward-pressure bias participants noticed. There is no randomization or counterbalancing.
6. **Task identity is confounded with FST.** Five distinct technical domains are not interchangeable difficulty doses. A nonlinear curve through them cannot establish an FST effect.
7. **Information packet is a co-authored treatment.** LLM-generated, benchmark-author-reviewed summaries include inferred skill and exploitation framing; packet effects are not tested.
8. **Hypothetical capability is under-specified.** “Hardest task the model can solve” does not define success frequency, attempts, budget, scaffold, contamination, or whether lower tasks are reliably mastered.
9. **Baseline is imported and unauditable here.** The 25% counterfactual comes from a forthcoming study, so uplift inherits its population, scenario, and calibration uncertainty.
10. **No empirical consequence outcomes.** There is no observed malware campaign, actor uplift trial, longitudinal prediction, or outcome validation.
11. **Bayesian model is not reproducible.** Priors, likelihood, dependence assumptions, code, diagnostics, and numerical posterior table are absent.
12. **Intervals are unclear.** The manuscript calls them confidence intervals despite Bayesian interpolation and does not define their statistical target.
13. **Deliberation changes independence.** Peer-visible estimates and subgroup discussion are protocol features, but pooled uncertainty must model induced dependence.
14. **No aggregation sensitivity.** Means are not compared with medians, quantile aggregation, group-specific mixtures, or assumption-conditioned estimates.
15. **Post hoc exclusion risk.** Misinterpretation is a legitimate exclusion reason, but predeclared rules and immutable correction records are absent.
16. **External validity is narrow.** One attack node, one benchmark, five hand-selected tasks, and one expert pool cannot generalize to cyber risk broadly, other professions, or other harms.
17. **Decision usefulness is untested.** No regulator, developer, or operator uses the estimates in a documented choice, threshold, or mitigation allocation.
18. **Severity is outside scope.** The elicited conditional probability is not expected harm; calling it quantitative “risk” requires the omitted frequencies and consequences.
19. **Paper claims sometimes outrun evidence.** Calling Group B a “conservative lower bound” is unjustified; a lower estimate is not a statistical or epistemic bound without evidence that its assumptions are directionally conservative.
20. **Difficulty smoothness is proposed, not shown.** FST enables ordering, but five selected tasks and expert disagreement do not verify smooth difficulty or smooth consequence mapping.

## Reproducibility and operational realism

The immutable v2 PDF and full local extraction make the narrative, appendix rationales, and generated task packets inspectable. The paper preserves more judgment-level evidence than a result-only report, especially through initial/final estimates and rationales.

Analytical reproducibility is poor. There is no workshop instrument, original Google Sheet, moderation transcript, complete inclusion/exclusion log, analysis code, Bayesian specification, posterior samples, or machine-readable dataset. Several appendix entries are blank. The headline ranges and interpolation cannot be independently regenerated from the paper alone.

Operational realism is similarly mixed. The six-node scenario, conditional structure, explicit baseline, real experts, and paid two-hour workshop are closer to decision analysis than generic benchmark interpretation. Yet the evaluated task fragments remain far from end-to-end offensive operations, model access/use is unconstrained, and no affected organization, real deployment decision, observed control, or consequence closes the loop. The work is best treated as a pilot elicitation-method case, not a validated cyber-risk model.

## Concrete changes for skill-bench

1. **Represent consequence promotion as a linked inference chain, not a score transform.** Reuse existing validity arguments for claim boundaries, metric specifications for estimands and uncertainty, participation records for expert authority/consent, and elicitation records for information exposure and correction.
2. **Add `information_condition` and `disagreement_crux` requirements to the future elicitation-session contract.** Preserve packet hashes, ordering, peer estimates viewed, moderation exposure, initial/revised values, rationale changes, and whether disagreement reflects different targets or beliefs. This refines the already blocked `build-elicitation-session-contract`; it does not justify implementing it before a real consented session.
3. **Require consequence reports to expose excluded links.** A task score may support a bounded capability claim while access probability, workflow uplift, outcome frequency, severity, and decision utility remain unsupported.
4. **Treat expert disagreement diagnostically.** Before aggregation, classify disagreements by scenario ambiguity, benchmark-transfer warrant, baseline, causal mechanism, or value/decision threshold; design the next pilot around the dominant crux.
5. **Predeclare aggregation and sensitivity.** Dependence-aware pooling, calibration/seed policy, exclusion criteria, missingness, subgroup treatment, and alternate pooling rules belong in metric-monitoring evidence.
6. **Prefer direct uplift trials where feasible.** Consequential claims about knowledge work should compare matched actors or systems on realistic workflows, rather than asking experts to infer end-to-end effects from adjacent benchmark items.
7. **Keep claim scope narrow.** This study supports a method-feasibility observation and an identified inference dispute; it does not support a calibrated cyber uplift, expected harm, deployment threshold, or general benchmark-to-risk conversion function.

## Action items

- [x] Preserve and read the complete immutable v2 PDF/text primary source.
- [x] Reconstruct the scenario node, Cybench task mapping, IDEA-derived workshop, sample attrition, information condition, aggregation, and stated results with page evidence.
- [x] Separate benchmark observation, conditional capability, access/use, workflow probability, harm severity, and decision use.
- [x] Map nonduplicate implications into existing validity, metric, participation, and elicitation machinery.
- [ ] When a real consented elicitation session exists, test whether typed information conditions and disagreement-crux coding can be completed reliably without laundering analyst inference into expert evidence.
- [ ] In a future consequential pilot, compare expert score-to-outcome estimates against a matched direct uplift study and evaluate calibration, not merely convergence.
