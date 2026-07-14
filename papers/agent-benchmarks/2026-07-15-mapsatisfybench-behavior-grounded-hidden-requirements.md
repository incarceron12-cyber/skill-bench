# MapSatisfyBench: observed behavior can nominate hidden factors, but it does not make them current intent or acceptance probability

## Source and review status

**Deep paper review; no release available.** I read the complete immutable arXiv v2 PDF and its full local layout extraction. The source PDF itself ends mid-sentence on page 22; the extraction faithfully preserves that incomplete ending.

- Paper: Lubin Bai et al., *MapSatisfyBench: Benchmarking Satisfaction-Aware Map Agents through Behavior-Grounded Implicit Decision Factors*, arXiv:2606.17453v2, <https://arxiv.org/abs/2606.17453v2>
- Local PDF: `data/papers/pdfs/2606.17453v2-mapsatisfybench.pdf` (22 pages; SHA-256 `d48e297e2c6aa6087f17e8c87610350ad2a71facab35bb309c36ab135472e489`)
- Local text: `data/papers/text/2606.17453v2-mapsatisfybench.txt` (SHA-256 `894b20010a360475a0f8ff535f594fd4c53d82a940dc277f4124e68f3f5c9ced`)
- Date read: 2026-07-15
- Release status: the immutable paper and arXiv record provide no official MapSatisfyBench dataset, code, grader, prompt package, or run archive. The only GitHub URL is a related-work citation to LBS-IntentBench. Targeted title/ID searches found no author-owned release. The appendix's translated example is paper evidence, not a benchmark release.

## One-sentence contribution

MapSatisfyBench proposes a useful restore–identify–filter authoring pattern that uses later behavior to nominate omitted decision factors and then retains only factors with pre-response support, but its selected private logs, expert/LLM co-authored labels, hand-designed weights, simulated user, model judge, and unreleased instrument measure agreement with reconstructed factor rubrics—not observed user satisfaction, current authorization, causal acceptance, or generally valid personalization.

## Why this matters for skill-bench

This review advances charter objectives A and B through narrow expansion into a missing authoring mechanism: deriving candidate hidden requirements from behavior chains rather than only from an expert interview, task prompt, or author oracle. Maps are a bounded method case, not a scope boundary.

The general benchmark question is:

> When may past and later behavior be used to construct a fair hidden requirement for an earlier decision, and what additional evidence distinguishes availability, prediction, authority, causal relevance, and user-valid consequence?

The paper's strongest idea is the **time firewall**: post-response behavior may help a benchmark author discover a candidate factor, but the evaluated agent must be able to recover that factor from information available before its response (pp. 4–5, 13–14). Its central error is then to collapse a much longer chain—historical choice → inferred preference → current applicability → response-factor satisfaction → acceptance probability—into one weighted rubric score without validating the transitions.

## Research question and defensible construct

The paper asks whether map agents can recover implicit decision factors from context, profile, and spatiotemporal evidence, acquire missing evidence through tools, and return a response likely to satisfy a user rather than merely complete the explicit request (pp. 1–3).

The auditable construct is narrower:

> On 500 selected, author-annotated map interactions, under a GPT-5.3 user simulator, a 22-tool replay environment, one sampled agent trajectory, and repeated GPT-5.3 judging, how well does a configured model's response satisfy explicit and implicit factor rubrics reconstructed from private behavior-chain evidence and projected into the sandbox?

The study does not directly observe satisfaction, acceptance, counterfactual choice, current user endorsement, consent to profile use, downstream trip outcome, or a real map-service action. `AR` is the product of two rubric scores, not an empirically estimated acceptance probability.

## Methodology and system

### 1. Restore–identify–filter construction

An instance is formalized as `x = (q, g, h−, r, h+)`: root query, spatiotemporal environment, pre-query context/profile, response, and post-query behavior. Authors use `h+` with the earlier state to restore a “complete need,” compare that need with `q` to identify omitted factors, then retain only factors supported by `g` or `h−` so that the evaluated agent could in principle recover them without seeing the future (pp. 4–5).

This is better than grading every hindsight-derived inference. It distinguishes **factor discovery evidence** from **agent-admissible evidence**. But the paper does not preserve that distinction as an inspectable item lineage. It does not report the source response `r`, exact post-query event window, competing continuations, time from response to behavior, or whether a later action followed the evaluated response, another intervention, changed circumstances, or simple habit. The claim that restoration “does not use post-query outcomes to rewrite the query retroactively” sits uneasily with the stated use of subsequent operation trajectories to select targets, slots, and preferences (p. 13). The filter prevents direct future leakage into the agent view; it does not prevent hindsight from determining which pre-query correlation becomes the gold factor.

Selection requires a coherent task, explicit-task validity, a valid `h+` behavioral anchor, and at least one retained implicit factor (p. 5). This is an outcome- and construct-conditioned challenge set. It excludes ordinary map requests with no hidden factor, ambiguous cases with no identifiable continuation, factors that require clarification, and potentially cases where behavior contradicts the inferred need. It therefore cannot estimate the prevalence of underspecification, hidden preferences, or satisfactory behavior in map traffic.

The paper says the source is “large-scale, real-world anonymized map-service logs” but gives no log population size, date range, market/geography frame, user/session inclusion rules, candidate count, attrition at each filter, repeated-user handling, sampling weights, sensitive-attribute policy, anonymization transform, consent basis, retention policy, or privacy audit (pp. 4–5). The 500 retained items are a selected benchmark set, not a probability sample.

### 2. Ground-truth projection and annotation

Each item receives five annotation families: explicit factors `E`, implicit factors `Zeval`, clarification policy `C`, expected tool trajectory `T`, and factual requirements `F` (p. 5). Each implicit factor has a rubric, hard/soft type, and evidence-supported weight. Three LLMs first generate candidate annotations; humans select, correct, merge, or reject them; human cross-validation and an independent consistency review follow (pp. 5, 12–13).

This is a sensible multi-stage workflow, but the evidence needed to evaluate it is absent:

- the three candidate-model identities and prompts;
- annotator and “expert” counts, qualifications, training, independence, and domain authority;
- agreement threshold, pre-adjudication agreement, rejection rate, disagreement categories, and adjudication lineage;
- whether reviewers saw post-query behavior, reconstructed full intent, model candidates, and one another's decisions;
- alternative acceptable factors, abstentions, non-identifiable items, and user confirmation;
- task-level mappings from raw events through transformations to each rubric and weight.

The pipeline makes one panel's reconstruction internally consistent. It does not establish that the represented person currently endorsed the factor, that the factor caused the historical choice, or that satisfying it would increase future acceptance.

### 3. Evidence-supported weights

The implicit-factor weight is `userpref(zi) × CurrentNeed(zi)`. Historical preference strength is a within-dimension behavior ratio, adjusted by hand-set recency and momentum coefficients. Current need receives one of four hand-set values—1.2, 1.0, 0.8, or 0.5—based on relevance, continuity, invalidity, or conflict (pp. 13–14). When only profile/history exists, current need defaults to **1.0**; when only current evidence exists, user preference defaults to **1.0** (p. 13).

These are transparent authoring rules, not learned or calibrated acceptance effects. A historical tendency remains fully active when there is no current-session evidence, rather than becoming uncertain. “Hard” and “soft” differ only in their per-factor satisfaction scale; both enter the same compensatory weighted mean. Violating one hard constraint merely contributes zero for that factor and can be offset by other factors (pp. 5–6). That contradicts the paper's language that hard factors are necessary constraints and weakens the interpretation of `IISR` and `AR` as acceptability measures.

No observed accept/reject outcome is regressed on factors; no held-out choice, counterfactual option set, calibration curve, discrimination test, threshold, or user study validates the weights. A ratio of chosen brands estimates historical frequency among logged behaviors, not preference utility, causal importance, or willingness to reject an alternative.

### 4. Deterministic replay sandbox and simulated user

The evaluated business agent can answer, clarify, or call 22 map tools. A GPT-5.3 user simulator is given the private `full_intent` and instructed to disclose only what the business agent asks, while exact and embedding retrieval serve mock tool responses (pp. 5–6, 16–20).

The “deterministic” label is overstated. The experiment uses GPT-5.3 at temperature 1.0 for the user, judge, and LLM fallback tool simulator; open-text tool arguments use embedding retrieval; and a fallback generates a tool response when retrieval fails (pp. 7, 16–20). The paper does not provide seeds, cached response hashes, model snapshots, fallback incidence, simulator repeats, or per-call invalidity. Same database and inventory do not imply same interaction when model-backed components are stochastic.

The user simulator is also not behaviorally validated. Its prompt forces passivity, forbids unsolicited corrections even after a wrong answer, and can terminate after an incomplete response if no question is asked (pp. 16–19). That policy may make profile retrieval look preferable to clarification, but it is an evaluator intervention—not evidence of natural user patience, willingness to disclose, or satisfaction. The private full intent is supplied as authoritative and complete; real users can be uncertain, change their minds, reject the annotator's abstraction, or hold several acceptable options.

### 5. Metrics and grading

Seven per-item metrics are macro-averaged (pp. 6–7):

- `ECR`: mean binary satisfaction of explicit factors;
- `IISR`: weighted satisfaction of implicit factors;
- `TS`: Jaccard overlap between one expected and observed tool set;
- `IFS`: mean support of required factual claims by tool output;
- `Eff = 1 / (1 + actual turns / reference turns)`;
- `AR = ECR × IISR`; and
- `SES = AR × Eff`.

The plural measurements are useful. Their interpretations are not all justified:

1. **`AR` is not acceptance probability.** Multiplying two rubric averages does not produce a calibrated probability without an outcome model. Partial `ECR` can also leave `AR > 0` despite explicit failure, contrary to the text's statement that `ECR = 0` when the stated task fails.
2. **Hard constraints do not gate.** One failed hard factor can be compensated by several satisfied soft factors.
3. **One gold tool set penalizes legitimate alternatives.** Jaccard treats extra verification or equivalent tool paths as errors without cost- or necessity-aware adjudication.
4. **Efficiency is structurally punitive.** At the reference turn count, `Eff = 0.5`; it approaches 1 only at zero turns. The paper calls the reference a human-expert median but reports no human sample, protocol, dispersion, or task-level budget validation (p. 7).
5. **Clarification policy is not substantively scored.** Turn count does not distinguish a necessary high-value question from redundant burden, nor an efficient but unjustified assumption from calibrated action.
6. **Judge and gold are co-designed.** GPT-5.3 participates in screening/simulation/judging around expert-corrected rubrics; repeated judging can reduce call noise but cannot validate the criterion.

The reliability study uses 68 trajectories and reports tolerance agreement and MAE only for ECR and IISR (pp. 14–15). It does not report annotator count, independent human agreement, label distribution, prompt versions, per-factor results, confidence intervals, disagreements, or judge-vote instability. The stated `N=68` is also arithmetically difficult to reconcile with reported accuracies: `.9841`, `.9062`, and `.8906` are not integer multiples of `1/68`, suggesting unexplained metric-specific missingness or denominators. Low MAE against a reference produced within the same rubric pipeline does not establish acceptance validity.

### 6. Configured systems, trials, and statistics

The paper reports 12 non-thinking model rows and three thinking-mode rows. All are run at temperature 1.0. Each configured model produces one trajectory per item, and that fixed trajectory is judged three times with majority voting (pp. 7–9). Thus the repeated unit is the judge call, not agent behavior. There is no estimate of trajectory stochasticity, pass-at-k, expected utility, or repeatability.

The main tables provide means only. There are no confidence intervals, paired tests, task/user/template clustering, repeated-user adjustment, multiplicity controls, invalid/timeout/malformed-call counts, retry policy, token use, latency, or cost. Grouped domain/source averages pool systems and overlapping multi-label items, so they do not isolate domain or evidence-source difficulty.

The online/offline comparison uses 100 sampled items and two model settings with single means. Offline and live runs differ by tool evidence and resulting trajectories, but no matched item differences, intervals, equivalence margins, invalids, or trace audits are shown (p. 15). Calling small mean differences “stability” and the offline advantage “expected” is interpretation, not an equivalence test.

The profile-evidence condition directly exposes summaries and categorical history. Qwen and Gemini IISR increase by approximately 2.6% and 3.7% relative to their thinking rows (pp. 15–16). This shows sensitivity to a bundled information-delivery intervention. It does not separately identify profile availability, tool discovery, retrieval, interpretation, or adoption, and no uncertainty establishes that the small changes are stable.

## End-to-end paper-item audit: Ningbo MixC charging station

Appendix C provides the only inspectable translated item (pp. 20–22), task `d3238e6b28bf53f6e7bc30cb1536e2a8`. It permits a partial reconstruction but not a raw-log audit:

1. **Root request:** “Go to a charging station near MixC.”
2. **Pre-query context:** the user is in Ningbo and the displayed recent chain includes earlier driving, a rejected station list, clarification of “Ningbo MixC,” the statement that “there is a parking lot and a charging station,” and a repeated request.
3. **Restored private need:** choose a station associated with a parking lot, plan by driving, and prefer TELD where possible.
4. **Factor 1:** parking-lot association, soft, weight `1.2`, supported directly by current dialogue. This is omitted from the root query but explicitly present in the visible conversation—not an inference from behavior alone.
5. **Factor 2:** driving mode, soft, weight `0.8179`. The number reconstructs as `0.852 × 0.8 × 1.2 = 0.81792`: 85.2% local driving preference, routine-history recency 0.8, and increasing/current support 1.2.
6. **Factor 3:** TELD priority, soft, weight `0.4851`. It reconstructs as `(38 / 94) × 1.0 × 1.2 ≈ 0.4851`, plus recent TELD statements/actions.
7. **Expected evidence/action:** search the named landmark, search nearby charging POIs, query user-action summary, then request driving navigation.
8. **Grading target:** check explicit factors, the three weighted preferences, one expected tool set/parameters, factual grounding, and turns.

This example demonstrates that the weighting rules can be followed mechanically from the *projected summary*. It does not expose the raw anonymized events, original agent response, actual post-query behavior `h+`, candidate alternatives, rejected annotation variants, tool-return corpus, grader rubric, or scored trajectory. Therefore it cannot establish that TELD caused acceptance, that the profile was current or authorized for this use, that parking association was soft rather than required, or that another charging station would dissatisfy the user.

It also reveals the method's mixed constructs. Parking association is recoverable from explicit prior dialogue; driving is inferred from historical frequency plus immediate actions; TELD is inferred from brand behavior and recent language. Those are three different evidence/authority types, yet all become commensurate weights in one satisfaction mean.

## Evidence and claim limits

### Supported by the paper

1. The authors specify a coherent restore–identify–filter authoring method and a five-part task reference separating explicit factors, implicit factors, clarification, tools, and factual requirements.
2. The appendix makes the factor-weight arithmetic and one translated projected item inspectable.
3. The reported configured systems score substantially higher on explicit-factor completion than on weighted implicit-factor satisfaction, and tool-set overlap is below 0.50 for every main row.
4. Directly supplying profile summaries changes the scores of two tested model settings modestly.
5. A 68-trajectory same-rubric study reports close human-reference/model-judge score agreement, subject to unexplained denominators and limited reporting.

### Not established

- actual user satisfaction or accepted-response probability;
- causal effects of satisfying any inferred factor on choice or outcome;
- current user intent, permission, consent, or normative authority of behavioral history;
- completeness or uniqueness of the reconstructed hidden factors;
- benefit over clarification for real users, or a calibrated burden/quality tradeoff;
- representative map-query prevalence, user diversity, or domain difficulty;
- general personalization, memory, professional knowledge-work, or cross-domain capability;
- deterministic or exactly reproducible sandbox behavior;
- stable model rankings under repeated trajectories or new users/tasks;
- privacy, fairness, production safety, economic value, or deployment readiness.

## Unique insight: behavior is evidence about a requirement, not authority for the requirement

MapSatisfyBench usefully separates future behavior from the evaluated agent's evidence view, but `skill-bench` needs a fuller **behavior-to-requirement validity chain**:

```text
raw event and actor
→ session/entity linkage
→ temporal ordering and valid window
→ observed choice/action
→ plausible goals and rival explanations
→ candidate factor
→ pre-decision support available to the agent
→ current applicability
→ issuer/subject authority and permitted use
→ alternative acceptable factors/actions
→ clarification policy
→ agent access, interpretation, and adoption
→ attempted and realized consequence
→ affected-party acceptance/correction
→ bounded score and claim
```

No arrow is automatic. A repeated action may reflect availability, default ranking, price, coercion, prior system recommendations, shared-device use, or a stale habit. Later action may reveal what happened without revealing why it happened. A profile may predict a choice while lacking authority to make that choice for the user. A factor may be useful for ranking yet too uncertain or sensitive for silent action. A single realized choice does not eliminate acceptable alternatives.

For benchmark authoring, hindsight behavior should therefore nominate a **candidate hidden factor**, never directly create a private obligation. Promotion requires an evidence record with rival explanations, temporal/current applicability, purpose/consent boundary, independent reconstruction, and at least one counterfactual or affected-party validation path. If those are unavailable, the task can validly test evidence retrieval and rubric following, but its claim must stop before satisfaction or representative action.

## Comparison with adjacent reviewed evidence

- **UnderSpecBench** fixes a private intended transition while weakening public action/object/scope cues. MapSatisfyBench is stronger in requiring pre-response evidence for retained factors, but weaker in treating one reconstructed full intent and expected tool path as authoritative. Together they require separate private intent, public support, resolvable uncertainty, legitimate terminal sets, and alternative-path adjudication.
- **HippoCamp** shows that contextual availability, authorization, access, interpretation, adoption, answer acceptance, consequence, and user validation are separate stages. MapSatisfyBench advances from context toward interactive choice, but still skips authorization, causal adoption, realized consequence, and affected-user validation.
- **SovereignPA-Bench** separates current intent, stale memory, third-party pressure, evidence, consent, and burden. MapSatisfyBench's historical profile and current need should receive the same typed issuer, valid-time, purpose, supersession, sensitivity, and consent treatment instead of becoming scalar multipliers.
- **JobBench** uses historical worker delegation ratings as a portfolio-selection signal but does not call them current consent or worker benefit. MapSatisfyBench should apply the same ceiling: historical behavior can select and weight candidate authoring cases, not prove current satisfaction or authorize silent personalization.
- **PISAS/contextual-integrity evidence** shows that information relevance and information-flow legitimacy are different. A profile feature may improve prediction while its use remains inappropriate for the present purpose, recipient, or represented person.

## Limitations and validity threats

1. No official dataset, code, grader, prompts, trajectories, or results are released.
2. The source PDF ends mid-sentence, leaving the final sample requirement incomplete.
3. The private-log population, date range, candidate count, geography, sampling frame, and filter attrition are absent.
4. Selection conditions on a coherent hindsight anchor and at least one recoverable hidden factor.
5. Repeated users/sessions and resulting dependence are not characterized.
6. Anonymization, consent, sensitive-attribute use, withdrawal, retention, and privacy review are unspecified.
7. Post-query behavior helps select the gold need, creating hindsight-conditioned labels even when it is hidden from the agent.
8. The original response and alternative interventions between query and later behavior are not modeled.
9. Later action is treated as a need anchor without causal or counterfactual validation.
10. Alternative acceptable choices and non-identifiable needs are not represented.
11. The three candidate LLMs, annotator/expert panel, training, authority, and review views are unspecified.
12. No pre-adjudication agreement, rejection rate, disagreement taxonomy, or correction lineage is reported.
13. No represented user validates the reconstructed full intent, factor types, or weights.
14. Historical behavior ratios conflate preference with opportunity, ranking, defaults, and constraints.
15. Recency, momentum, relevance, continuity, and conflict coefficients are hand-set and uncalibrated.
16. Absent current evidence defaults historical preference to fully active rather than uncertain.
17. Hard constraints enter a compensatory mean and therefore do not behave as necessary gates.
18. `AR` is an uncalibrated product of rubric scores, not observed probability.
19. One expected tool set can reject equivalent, safer, or more efficient trajectories.
20. Turn-based efficiency does not grade question value, necessity, answerability, or burden.
21. The simulated user has evaluator-authored full intent and an unvalidated passive-disclosure policy.
22. GPT-5.3 is reused across screening/simulation/judging roles, creating shared blind spots.
23. Temperature-1 user and fallback simulation contradict strong determinism claims without seeds/cache hashes.
24. One agent trajectory per item provides no behavioral repeatability estimate.
25. Three judge calls on one trajectory do not estimate configured-agent reliability.
26. Judge validation covers only ECR and IISR on 68 cases and omits human agreement and criterion validity.
27. Reported agreement percentages do not match an obvious denominator of 68.
28. Main tables omit intervals, paired tests, task/user clustering, multiplicity, and missing/invalid runs.
29. Domain/source analyses pool overlapping labels and model rows, confounding task mix with configured-system mix.
30. The offline/live comparison is not an equivalence test and lacks paired uncertainty.
31. Profile delivery is a bundled information/interface intervention, not a clean retrieval-versus-reasoning decomposition.
32. No token, latency, infrastructure, annotation, privacy, or monetary cost is reported.
33. No real user outcome, map action, trip completion, correction, or longitudinal acceptance is measured.

## Reproducibility and operational realism

**Conceptual reproducibility is moderate; exact and empirical reproducibility are low.** The paper defines the instance tuple, factor records, weight formula, prompts, metrics, aggregate results, and one translated item. Another group could build a related benchmark.

Exact reproduction is impossible from the available evidence. The 500 items, raw behavior chains, anonymization transforms, annotation candidates/decisions, tool corpus, retrieval index, 22 tool schemas, rubric prompts, model snapshots, seeds, caches, trajectories, judge votes, invalid-run inventory, and analysis code are unavailable. Proprietary and future-dated model/service identities further limit replay.

Operational realism is mixed. Real map-service logs, underspecified requests, contextual history, POI search, routing, and clarification are ecologically meaningful ingredients. But the administered environment is a model-mediated replay with a private full-intent simulator, fixed mock data, no actual booking/navigation/action, and no user-observed consequence. The benchmark is best understood as an unreleased **behavior-inspired factor-recovery and rubric-conformance instrument**, not a validated user-satisfaction or production map-agent evaluation.

## Transfer to skill-bench

### Retain

1. **Restore–identify–filter as candidate generation.** Use later outcomes and expert reconstruction to discover hidden-factor hypotheses, then require independent pre-decision support before exposing them to scoring.
2. **Typed factor decomposition.** Keep explicit requirement, implicit factor, evidence locator, hard/soft status, clarification policy, tool expectation, and factual requirement separate.
3. **Agent-time evidence firewall.** Record exactly which evidence existed and was accessible before action; never expose author hindsight or later behavior to the evaluated system.
4. **Plural decision metrics.** Separate public-task completion, evidence acquisition, factual grounding, hidden-factor handling, clarification burden, action/state consequence, and affected-party review.
5. **Profile-delivery ablations.** Compare no access, discoverable tool access, direct supplied summary, and clarification—while pinning the remaining system and measuring access, adoption, consequence, and burden separately.

### Repair

1. Replace “ground-truth hidden requirement” with a versioned `candidate_factor` containing raw-event provenance, actor/entity binding, source valid time, inference method, rival explanations, confidence, current-applicability evidence, authorization/purpose, sensitivity, and status.
2. Keep factor **predictive strength**, **current applicability**, **normative authority**, **decision criticality**, and **causal outcome evidence** as separate fields. Do not multiply them into one unlabeled weight.
3. Require positive, negative, superseded, contradictory, and no-current-evidence cases. Include cases where history should be ignored and where clarification is the only legitimate path.
4. Admit sets of acceptable factors, answers, and tool trajectories; preserve abstention and unresolved non-identifiability. Grade extra tools by risk/cost rather than raw set mismatch.
5. Make hard constraints noncompensatory only when their public basis and authority are validated; otherwise label them hypotheses or clarification triggers.
6. Validate acceptance interpretations with held-out affected-party choice/correction or a predeclared behavioral outcome model. Until then call the metric `weighted_factor_satisfaction`, not accepted-response probability.
7. Measure clarification calibration: necessity, answerability, information gain, burden, and downstream improvement—not merely turn count.
8. Separate screening model, user simulator, tool fallback, grader, and human adjudicator identities; preserve evidence views, votes, disagreement, invalidity, and retries.
9. Use repeated agent trajectories, user/task clustering, explicit invalid denominators, paired interventions, and uncertainty appropriate to the inference population.
10. For private behavioral data, require contribution/consent scope, permitted inference/use, de-identification lineage, sensitive-field policy, withdrawal boundary, and affected-party review.

## Concrete repository actions

1. **No new build task.** Existing authority/participation, expertise-transfer, evidence-state, benchmark-bundle, contextual-integrity, artifact/state, task-health, metric-monitoring, validity-argument, and repeated-trial machinery already has homes for these requirements. A map- or personalization-specific schema would duplicate the backlog.
2. In the next hidden-requirement pilot, add a four-condition authoring calibration set: `(history supports / history conflicts) × (current context activates / current context is silent)`, plus matched cases where inspection resolves uncertainty and where clarification is required. Preserve affected-party or expert adjudication and legitimate alternative sets.
3. Add a validity regression case where a behavior-derived factor predicts a prior choice but lacks current authority; the validator/report must permit a narrow predictive-evidence claim while rejecting “required,” “satisfying,” “accepted,” and “authorized action” upgrades.
4. Add a metric regression demonstrating that a compensatory weighted mean can pass despite a failed hard factor and that multiplying rubric means does not license a probability label without calibration evidence.

## Claim ceiling

MapSatisfyBench supports the methodological claim that later behavior can help authors discover candidate omitted decision factors and that those factors can be filtered to require pre-response evidentiary support, projected into explicit rubrics, and used to diagnose configured-system differences on an unreleased 500-item map suite. It does **not** establish observed satisfaction, calibrated acceptance probability, current user intent, consented personalization, causal benefit from profile use, representative map-agent capability, general hidden-requirement competence, professional validity, privacy safety, production effectiveness, or deployment readiness. Its most transferable lesson is a boundary: **behavior can provide predictive and authoring evidence about a requirement, but authority, current applicability, causal consequence, and user acceptance each need separate validation.**
