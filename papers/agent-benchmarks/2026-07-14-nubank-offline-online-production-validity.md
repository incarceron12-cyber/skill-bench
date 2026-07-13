# Paper Review: Nubank — Offline-to-Online Production-Evaluation Validity

- **Paper:** https://arxiv.org/abs/2606.08867v2
- **Authors:** Aman Gupta, Kevin Rossell, Edesio Alcobaça, Jose Chrystian Lima Pacheco, Carolina Baptista de Lima, Shao Tang, Luiz Paulo Rabachini, Luis Moneda, Herbert Fei, Daniel Silva, Rohan Ramanath
- **Date read:** 2026-07-14
- **Venue / source:** KDD 2026 industry paper; immutable arXiv preprint
- **Version read:** immutable v2, 13 June 2026
- **Local PDF:** `data/papers/pdfs/2606.08867v2-nubank-production-evaluation.pdf` (12 pages; SHA-256 `af0c2c13515ad001dc2ff17a7824131407f221400aebaf36d75afd0e5ee84995`)
- **Local text:** `data/papers/text/2606.08867v2-nubank-production-evaluation.txt` (SHA-256 `182db3b5e2c864250446cc452bd3006da0b3d139ef1dd2193b4ef4803c1d2df7`)
- **Prior version checked:** immutable v1 PDF/text at the paths recorded in `data/sources/releases/2606.08867v2-nubank-production-evaluation/provenance.json`; all-member source comparison found no substantive manuscript-text change
- **Release status:** no verifiable author- or Nubank-owned code, data, complete prompt, annotation, judge-output, production-record, or supplemental release was found; search and provenance limits are recorded in the same manifest
- **Tags:** production-evaluation, offline-online-validity, customer-support, llm-judge, prompt-optimization, ab-testing, metric-selection, treatment-bundles

## One-sentence contribution

Nubank presents a coherent production loop connecting modular agent context, analyst-labeled binary evaluators, GEPA judge-prompt optimization, offline simulation, progressive rollout, and online customer metrics across five support deployments; it provides unusually direct evidence that selected agent variants improved live tNPS and self-service point estimates, but absent assignment/sample details, metric denominators, intervals, raw results, a quantified correlation, independent human-label reliability, and control of sequential selection or treatment bundles means it does **not** establish that offline scores generally or prospectively predict production impact.

## Why this matters for skill-bench

This paper addresses a link that benchmark projects often assume rather than test:

`offline benchmark observation → candidate selection → live exposure → workflow/customer consequence`.

Its strongest contribution is not the headline `+37` percentage-point AI transactional NPS (tNPS) and `+29` point self-service-rate (SSR) gains. Those are unreproducible point estimates. The valuable pattern is that the authors put offline evaluator outputs and online outcomes in one operational loop, then explicitly use production evidence to revise architecture, routines, tools, and context (Figure 2 and Section 4.4, pp. 3 and 5–6). This is closer to the consequential validity question in the charter than an offline leaderboard alone.

The paper also exposes why that bridge needs a full validity record. The card-delivery variants did not differ only in “agent quality”: they progressively added routines, logistics/customer tools, frustration detection, escalation, card reissue capability, tool-selection hierarchies, conciseness budgets, a model change, and model-specific prompt adaptation (Section 6.3, pp. 7–8). Offline scores selected which variants reached larger traffic, while those same bundled changes could directly affect both offline labels and online outcomes. A retrospective scatter among selected deployments is therefore evidence of **co-movement in one adaptive program**, not a transport coefficient from a frozen benchmark to arbitrary production systems.

This advances charter objectives A–C through a bounded banking-support case. Customer support is a stress substrate for a general production-validity chain, not a proposed scope boundary for `skill-bench`.

## Research question and claim boundary

The paper asks how to build customer-facing ReACT agents at large scale by coordinating context engineering, human-guided prompt iteration, automated evaluation, and online measurement. Empirically, it asks whether optimized binary evaluators can discriminate agent variants and whether offline improvements align with live tNPS/SSR improvements.

The full paper supports bounded claims that:

- three operations analysts majority-labeled five card-delivery evaluator datasets containing 90–888 rows each;
- GPT-4.1-mini judges using GEPA-optimized prompts outperform a majority baseline and starter prompt on four reported held-out test sets (Table 2, p. 7);
- model–model agreement for one evaluator, E1, rises materially after prompt optimization (Figure 7, pp. 7–8);
- Nubank progressively exposed ten post-baseline card-delivery variants and reports that the best selected version improved AI tNPS by 37 points and SSR by 29 points relative to V0 (Sections 6.3–6.3.3, pp. 7–9);
- five selected deployments all have positive reported tNPS deltas, while four have positive SSR deltas (Table 3, p. 9);
- reported AI tNPS remains below separately measured expert-human tNPS by 1.1–23.6 points depending on use case.

It does **not** establish a preregistered prospective relationship between an offline score and a future online effect; universal offline predictiveness; causal contribution of GEPA, modular context, any one tool/routine/model change, or the full framework; comparable AI/human case mix; professional equivalence; safe autonomous banking support; cost savings; production readiness elsewhere; or cross-domain agent capability.

## Methodology and system reconstruction

### Agent and development treatment

The production agent follows ReACT with targeted guardrails and mandatory compliance checks (Sections 3.1 and 4, pp. 2–5). Its context is split into independently versioned instructions, routines translated from human SOPs, response macros, tool specifications and orchestration guidance, and persistent working memory (Section 4.2, pp. 4–5). Infrastructure includes knowledge/RAG, identity/authentication, action APIs, and audit trails. The authors recommend deterministic composite tools for fixed data dependencies, typed schemas and negative invocation guidance, minimal tool outputs, and idempotent actions (Section 4.3, pp. 5–6).

This is operationally specific and transfers well as **configured-system identity**. But it is mostly system description and engineering prescription. No component manifest, hashes, exact model endpoint, retrieval corpus, routine, tool implementation, compliance checker, memory policy, or environment snapshot is released. “Independently versioned” is not enough to reconstruct which versions generated each offline row or online metric.

The lifecycle has a fast loop and a slow loop. Domain experts revise prompt modules; real or simulated conversations are scored offline; versions that improve or preserve metrics are promoted; online A/B metrics then motivate broader architectural changes (Section 4.4, pp. 5–6). Initial deployment is 1–5% traffic, with monitoring of SSR, tNPS, escalation, and error rate; low-confidence, out-of-routine, or data-retrieval failures should escalate to humans (Section 4.5, p. 6). The paper gives no confidence estimator, threshold, calibration, escalation denominator, or monitoring result.

### Offline datasets and labels

The detailed card-delivery case defines five binary evaluators (Table 1, p. 6):

| Evaluator | Rows | Minority frequency |
|---|---:|---:|
| E1 Agent Reissue Failure | 888 | 0.49 |
| E2 Customer Input Verification | 90 | 0.22 |
| E3 Card Delivery Data Check | 816 | 0.43 |
| E4 Response Conciseness | 246 | 0.49 |
| E5 Resolution Completeness | 90 | 0.49 |

The data are derived from real support conversations through minimization and pseudonymization. Three operations analysts with specialized domain knowledge independently provide a binary label and rationale; majority vote becomes ground truth, and rationales are supplied to optimizer reflection (Section 5.2, p. 6).

Important missing lineage prevents stronger interpretation:

- no sampling frame, dates, traffic/version distribution, inclusion/exclusion, duplicate-customer/conversation policy, or synthetic-versus-real row counts;
- no analyst qualification beyond role, label guideline, per-analyst labels, disagreement counts, human–human agreement, uncertainty, adjudication, or rationale release;
- no evidence that train/validation/test splitting is grouped by customer, conversation lineage, issue template, or agent version;
- no prevalence target connecting the curated evaluator datasets to online traffic.

The paper calls its judge process “inter-rater reliability,” but the reported kappa analysis is **model–model agreement after optimization**, not analyst–analyst reliability and not judge–human agreement. Held-out accuracy against majority labels is the latter concordance measure; the human target's own reliability is unreported.

### GEPA optimization and held-out evaluation

All binary evaluators use GPT-4.1-mini as judge and GPT-5.1 as GEPA reflection model. GEPA runs `auto=light`, approximately 500 iterations, reflection minibatches of three, and Pareto candidate selection, using analyst rationales as semantic feedback (Section 5.2, pp. 6–7). The data split is stratified 40/30/30; optimization uses train and validation, and final reported accuracy uses the held-out test set. This is a meaningful safeguard against direct test-label optimization.

The safeguard remains bounded:

1. The exact prompt search, candidate history, split IDs, seeds, optimizer stopping rule, and prompt selected per run are absent.
2. The paper says each experiment was repeated five times and reports the mean plus a 95% interval “across runs,” but does not define whether runs repeat optimization, judge inference, split construction, or all three (p. 7). With temperature zero, an inference-only repeat is not an independent sampling design.
3. The intervals measure run variability, not uncertainty over conversations or target traffic. For the 90-row E2/E5 datasets, a 30% test split is only about 27 rows; E2's `88.89 ± 0.00` can correspond to a fixed 24/27 score and does not imply population precision.
4. E5 is present in Table 1 and online plots but missing from Table 2's evaluator-accuracy results. No explanation is given.
5. The complete optimized prompt is not published. Appendix A abridges its roughly 80 lines and explicitly elides edge-case guidance (pp. 11–12).
6. Even an initially held-out test set can become an adaptive development target when the same suite repeatedly selects ten production variants. The paper does not report test-set renewal, freeze/bridge policy, cumulative accesses, or a final untouched confirmation set.

Table 2 reports the majority baseline, starter, and optimized prompt only for E1–E4. Optimized accuracy is 82.00, 88.89, 73.01, and 76.89 percent respectively; the optimized prompt beats both comparators on those four fixed datasets (p. 7). This demonstrates configured concordance with majority labels, not evaluator validity over live traffic, rare consequential cases, safety, or alternative analyst policies.

### Agreement analysis

Seven judge models—GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini, GPT-5, o3, and o3-mini—score the E1 test set at temperature zero. Pairwise Cohen kappa is low under the starter prompt and much higher after optimization: examples include GPT-4.1/GPT-4.1-mini from 0 to 0.745, GPT-4.1/GPT-4o to 0.895, and GPT-5/o3 to 0.950 (Section 6.2 and Figure 7, pp. 7–8).

This is useful evidence that rubric realization changes cross-model stability. It does not show that every model became more correct, because models can converge on shared errors or on answer-bearing guidance distilled from the same analyst policy. Only E1 receives the reported cross-model analysis; there are no confidence intervals, repeated calls, item clusters, human-model kappa, class-specific recalls, or drift test. The claim that the optimized rubric is “largely invariant” to model architecture is therefore too broad.

### Online experiment and configured variants

The card-delivery experiment compares V0 with ten later variants—consistent with the paper's “10 different variants” and Figure 9's V0–V10, although Section 5.2 calls them “11 variants” when apparently counting V0. V0 has only retrieval and human-transfer tools. Later variants add routines, tools, escalation, action capability, hierarchy/budget controls, and model/prompt changes (Section 6.3, pp. 7–8). Each starts at 1% traffic and may be ramped; evaluator scores exclude non-promising candidates.

The paper repeatedly calls the resulting comparisons A/B tests. It does not report:

- randomization unit, allocation mechanism, concurrent control, blocking/stratification, eligibility, dates, duration, stopping/ramp rules, sample sizes, power, attrition, or crossover;
- whether the same customer can contribute repeated interactions or survey responses;
- whether V0 remains stable across all sequential comparisons;
- exposure noncompliance, model/tool outages, missing outcomes, escalation handling, or survey-response propensity;
- confidence intervals or hypothesis tests for any online effect;
- whether the reported best version and five use cases were selected after observing outcomes.

Accordingly, the `+37` tNPS and `+29` SSR figures are verified as the paper's reported **absolute percentage-point differences** in Figure 3 and Table 3 (pp. 3 and 9), not independently verified estimates. The paper supplies neither underlying promoter/passive/detractor counts nor SSR numerator/denominator from which to recompute them.

### What tNPS, SSR, and “near human” do—and do not—measure

tNPS is collected immediately after support interactions, separately for AI agents and expert humans. SSR is described as the fraction of support needs resolved through automated/self-service channels without human escalation (Section 3.4.3, p. 4). The authors correctly note that the two can trade off: handing hard cases to humans can raise AI tNPS while lowering SSR.

That warning is methodologically central, but the paper does not operationalize either measure. It omits eligible contacts, survey invitation and response rules, promoters/detractors thresholds, bot/human funnel assignment, transfers/returns/recontacts, time horizon for “resolved,” abandoned/invalid sessions, repeated users, and weighting. “AI tNPS within 1–10 points of expert humans” for four deployments compares separate funnels with no case-mix, selection, response, or interval adjustment. It is not evidence of equal task quality, expertise, compliance, or end-to-end customer outcome.

### Five deployment cases

Table 3 reports selected online deltas (p. 9):

| Use case | tNPS gain | SSR gain | AI minus expert-human tNPS |
|---|---:|---:|---:|
| Card delivery | +37 | +29 | −10 |
| Debt management | +40 | +2.9 | −23.6 |
| Credit limit | +4.5 | +7.5 | −7.1 |
| Card management | +38.3 | +4.8 | −1.1 |
| Product explainer | +12.3 | −1.5 | −6.2 |

Only card delivery receives a substantial methods account. Debt management and credit limit receive brief system/result descriptions; card management and product explanation receive no comparable dataset, judge, variant, or experiment methods. The Product Explainer SSR decline is attributed to transient LLM request failures without counts or incident evidence. The five cases demonstrate that favorable selected deployments were observed in several support intents; they are not a representative sample of attempted deployments or proof that the framework generalizes across support, finance, organizations, or knowledge work.

### Offline–online association

Figure 9 plots each deployed card-delivery variant's change in average evaluator failure rate against change in tNPS/SSR relative to V0. The text highlights V8 and V10 at roughly 20–25 point offline failure reductions and 37-point tNPS gain, and V6 near zero on both (Section 6.3.3, pp. 8–9).

No Pearson/Spearman coefficient, slope, interval, p-value, point table, number of included variants, weighting, or outlier/sensitivity analysis is reported. More fundamentally:

- promotion is conditional on offline scores, truncating the observed range and selecting which variants receive enough traffic;
- candidate changes are treatment bundles rather than exchangeable perturbations;
- later variants are adaptively informed by earlier offline and online failures, so points are not independent;
- all deltas share V0, inducing correlated errors;
- the offline metric is an average over five binary failure rates with no documented weighting or applicability denominator;
- no hold-one-version-out prediction or preregistered threshold predicts online effect before exposure;
- both offline and online outcomes can improve from the same direct design change without the offline metric being a portable predictor.

The figure is therefore a useful retrospective diagnostic. It does not “validate predictive power” or show that evaluation-driven development “reliably predicts production impact,” as the abstract and Sections 1/6.3.3 claim.

## Evidence and result interpretation

The most defensible empirical conclusions are narrower than the paper's narrative:

1. **Judge-prompt optimization worked on four reported held-out label sets.** The optimized GPT-4.1-mini configuration has higher accuracy than the starter and majority baselines under the authors' majority-label policy.
2. **A detailed rubric makes judge models agree more on E1.** That is stability evidence, not independent correctness evidence.
3. **Selected configured agents had favorable reported live point estimates.** Card delivery shows especially large reported changes, and all five selected deployments show positive tNPS deltas.
4. **Offline failures and online gains move together descriptively within one adaptive card-delivery program.** The data needed to quantify, reproduce, or prospectively validate that association are absent.
5. **Model replacement is not a component-isolated ablation.** GPT-5 required a new tool-first instruction; the online contrast estimates a model-plus-prompt package, not base-model capability alone (Section 6.3.2, p. 8).

The paper's strongest unsupported leap is from (4) to a general predictive claim. A second leap is from separate-funnel tNPS proximity to “near human” quality. A third is from SSR gain to reduced operating cost: no cost, latency, human-review burden, transfer burden, incident loss, or return-contact measure is reported.

## Unique insight

The paper's deepest transferable lesson is that **offline-to-online validity is a selected intervention graph, not a correlation column**.

A production candidate exists because prior evidence caused a change. The offline instrument then influences whether it is exposed, the online result influences the next candidate, and the traffic/control/metric systems determine which outcomes become observable:

```text
prior production/offline evidence
  → candidate component deltas
  → offline population + evaluator versions
  → promotion/ramp/stop decision
  → assignment and realized exposure
  → online metric observation
  → adjudication and next component deltas
```

Every arrow can induce selection, dependence, missingness, or construct drift. A valid bridge therefore needs more than paired scores. It must preserve candidate genealogy, exact component deltas, pre-exposure prediction, promotion rule, assignment, exposure, outcome definition, uncertainty, and post-result decision. Retrospective co-movement can generate hypotheses; prospective frozen predictions or designed interventions test transport.

A second insight is that **evaluation quality and iteration velocity must be measured separately**. The paper repeatedly says a reliable evaluator accelerates iteration, but reports neither elapsed development time, candidate throughput, analyst hours, GEPA calls/cost, false promotion/rejection, online experiments avoided, nor time to safe resolution. An evaluation can agree with a label set yet slow operation, or enable rapid iteration while optimizing the wrong target.

## Comparison with existing project evidence

- **Anthropic production-evaluation lifecycle** treats tasks as maintained evidence systems with role transitions, repeated trials, transcript adjudication, and retirement. Nubank adds a live candidate-selection/outcome loop, but omits the task-health history needed to know whether repeatedly used evaluator test sets remain confirmatory.
- **Amazon production evaluation** provides a broad trace→metric→dashboard→audit architecture but no quantitative field evidence. Nubank adds selected live point estimates and a retrospective offline/online plot; it still omits the metric population/denominator/uncertainty contracts identified in the Amazon review.
- **AgentRewardBench** directly shows that grader validity depends on predicate and observer view and preserves more explicit expert-versus-automatic error analysis. Nubank's judges use complete conversation text, but the paper reports no human-human reliability, class-specific held-out error surfaces, invalid policy, or outcome linkage per evaluator.
- **RuVerBench** shows that criterion selection, annotation policy, prompt realization, batching, parser, and model jointly define verifier agreement. Nubank independently confirms prompt realization as a large treatment, but tests cross-model agreement only on one evaluator and releases neither labels nor full prompts.
- **Existing configured-system, metric-monitoring, task-health, and validity contracts** already have the right homes for this evidence. What is missing is empirical use of those records in a prospective offline→promotion→online validation study, not another customer-support-specific schema.

## Transferable design patterns

### 1. Add a production-validation episode around existing records

Represent one episode by reference, not duplication:

- immutable offline task/population, rubric/grader, configured-system, task-health, and metric-specification IDs;
- candidate parent, exact changed component hashes, change rationale, and prior evidence locator;
- pre-exposure offline estimate, uncertainty, applicability/missingness, frozen promotion threshold, and predicted online direction/range;
- online eligibility, assignment unit/mechanism, control version, ramp/stop policy, dates, exposure and analysis populations;
- outcome metric/version, numerator/denominator or score distribution, delayed/repeated-user handling, clustered uncertainty, adverse/escalation/invalid outcomes;
- selection history, multiplicity, shared-control and adaptive-dependence links;
- adjudication, decision, rollback, and next-candidate lineage;
- licensed and prohibited claims.

This should be a thin linked record or pilot fixture over the existing bundle/task-health/metric/validity machinery, not a new vertical subsystem.

### 2. Require prospective bridge evidence

Before exposure, freeze at least the candidate identity, offline score, promotion decision, and predicted online direction. For stronger evidence, preregister a mapping or threshold on earlier versions and evaluate it on later versions. Report leave-one-version-out prediction, rank/order stability, and calibration where sample size permits. Keep retrospective scatterplots explicitly exploratory.

### 3. Treat variant histories as dependent

Use candidate lineage, shared baseline/control IDs, calendar windows, and repeated customer/task clusters. Do not analyze V1–V10 as independent rows. Sequential and adaptive experiments need methods that respect shared controls, stopping, ramping, and version genealogy.

### 4. Preserve metric funnels and joint outcomes

For tNPS-like measures, retain eligibility, invitation, response, promoter/passive/detractor counts, survey timing, transfer status, return contacts, customer cluster, and missingness. For SSR, define eligible support need, resolved state, time horizon, escalation/return policy, outages, and invalid sessions. Report the joint tNPS×SSR frontier and safety/escalation outcomes rather than optimizing either marginally.

### 5. Separate model stability, human concordance, and criterion validity

Model–model kappa, judge accuracy against majority labels, human–human agreement, and prediction of an external outcome are different evidence. Record all separately by evaluator and slice. Convergence after prompt optimization should trigger shared-error audits, not automatically license judge portability.

### 6. Renew repeatedly used offline instruments

A held-out set becomes operational development infrastructure after many candidate decisions. Record accesses and decision uses; reserve untouched confirmation forms; add temporal/traffic refreshes and bridge items; and re-estimate prevalence, disagreement, and outcome association after model/tool/policy changes.

### 7. Measure iteration velocity and burden directly

If the intended claim is faster safer iteration, measure candidate cycle time, offline calls/tokens/dollars, analyst hours, experiment traffic, false promotions/rejections, adjudications, incidents, rollback rate, and time to verified improvement. Online gains alone do not identify evaluation efficiency.

## Limitations and validity threats

1. **No public empirical artifacts.** Data, labels, rationales, full prompts, outputs, version manifests, assignments, and metric records are unavailable.
2. **Only four of five evaluator accuracies are reported.** E5 is omitted from Table 2 without explanation.
3. **Conversation sampling is unspecified.** The evaluator datasets have no traffic frame, dates, version mix, exclusions, or customer/conversation clustering.
4. **Human label reliability is absent.** Majority vote hides analyst disagreement; no analyst-level labels, agreement, uncertainty, or adjudication are reported.
5. **“Inter-rater” evidence is model–model agreement.** It does not establish human target reliability or criterion validity.
6. **Rationales and labels share one authority source.** GEPA is optimized toward the same analyst policy used for evaluation.
7. **Split leakage controls are incomplete.** Stratification is reported, but no grouping by customer, conversation family, template, agent version, or time.
8. **Five-run intervals are ambiguous.** The repeated unit is not defined, and run variability is not population uncertainty.
9. **Small test sets produce coarse scores.** E2 and E5 imply approximately 27 test rows under a 30% split.
10. **Temperature-zero/model drift remain.** Hosted endpoint realization, date, retries, and invalid responses are not pinned.
11. **The full optimized prompt is elided.** Exact replication and hidden-policy inspection are impossible.
12. **Repeated operational use erodes holdout status.** Ten candidate decisions can adapt to a nominally held-out evaluator suite.
13. **Cross-model stability is shown only for E1.** No equivalent evidence supports E2–E5 or other use cases.
14. **Agreement lacks uncertainty and error profiles.** Kappa matrices omit intervals, human comparison, prevalence sensitivity, and item-level clustering.
15. **Variant changes are bundled.** Routines, tools, escalation, action authority, budgets, model, and prompt change together.
16. **Online assignment is under-specified.** Randomization, concurrency, eligibility, blocking, duration, stopping, and power are absent.
17. **Sequential selection is ignored.** Poor offline candidates are excluded and promising candidates are ramped, making observed points selected and adaptively dependent.
18. **Shared-control dependence is ignored.** All deltas reference V0, and V0 stability over time is not established.
19. **No online uncertainty.** Every deployment result is a point estimate without sample size, interval, or hypothesis test.
20. **tNPS response selection is unreported.** Survey invitation/response rates, scoring rules, and missingness are absent.
21. **SSR is underdefined.** Eligible needs, resolution horizon, return contacts, transfer handling, outages, and invalid sessions are unspecified.
22. **AI/human comparisons use separate funnels.** Case mix, routing, response propensity, workload, and escalation differ.
23. **Correlation is not quantified.** Figure 9 has no coefficient, slope, interval, table, or explicit denominator.
24. **Correlation is not prospective.** No frozen mapping predicts an unseen version before production exposure.
25. **Offline aggregation is unspecified.** “Average evaluation failure rate” lacks evaluator weighting/applicability policy.
26. **Five use cases are selected, not sampled.** Failed, neutral, or abandoned deployments and their denominator are unknown.
27. **Only one use case has substantial methods.** Card/debt/credit summaries cannot reproduce five-study evidence.
28. **The Product Explainer outage explanation is unsupported.** No incident count or counterfactual estimate is provided.
29. **Escalation calibration is absent.** “Low confidence” has no estimator, threshold, false-escalation, missed-risk, or subgroup analysis.
30. **Safety/compliance evidence is descriptive.** Privacy, DPAs, guardrails, regulated process, audit, and contestation are described without incident/adverse-action rates or test results.
31. **Action correctness is under-observed.** No tool-side-effect, duplicate-action, rollback, financial-loss, or human-adjudication results are reported.
32. **Cost and iteration velocity are asserted.** No tokens, model cost, analyst hours, online traffic cost, latency, or cycle-time comparison is given.
33. **No negative-result denominator.** Eleven card variants and five selected deployments do not reveal all attempted projects or stopped candidates.
34. **Near-human tNPS is not equivalence.** No margin, uncertainty, matched cases, professional-quality rubric, or noninferiority design is provided.
35. **Generalization is narrow.** Five intents at one regulated firm do not support other organizations, domains, languages, policies, or knowledge-work constructs.

## Reproducibility and operational realism

Operational realism is high at the system-description level. The source includes real conversations, domain analysts, live tools and actions, privacy constraints, progressive traffic, human escalation, multiple customer outcomes, provider failures, model migration, and feedback from online operation into architecture. This is substantially more consequential than an offline response benchmark.

Reproducibility is weak. The immutable 12-page paper and abridged prompt allow inspection of the claimed design but not score recomputation, judge replay, configured-agent reconstruction, online effect estimation, or correlation analysis. No official release was found. The v1/v2 source archives were compared directly; v2 changes only the running author header and Figure 9 rendition, so version drift does not explain the missing methods or artifacts.

The correct evidence status is therefore: **production experience plus selected empirical point estimates with a partially described offline validation pipeline**. It is stronger than a generic production-method post, but much weaker than a reproducible field experiment or validated offline-to-online prediction study.

## Concrete changes for skill-bench

1. **Do not add a parallel schema task.** Existing configured-system, grader, task-health, metric-monitoring, execution-validity, validity-argument, and longitudinal records cover most required objects.
2. **Add a thin production-validation-episode fixture during consolidation/building.** Link exact candidate component deltas and offline evidence to a frozen promotion decision, online assignment/exposure record, outcome metric, uncertainty, adverse outcomes, and next decision.
3. **Use a prospective pilot, not a retrospective narrative.** In the next suitable executable pilot, freeze an offline prediction and promotion rule before an external or held-out consequence measurement; keep it internal if no real production outcome is available.
4. **Make evaluator test-set use countable.** Record every candidate decision that consumes a form, and require renewal or untouched confirmation evidence before calling later results held out.
5. **Add a metric-funnel audit.** Any satisfaction/self-service analogue must preserve eligible, observed, missing, escalated, returned, invalid, and clustered units plus the joint quality×automation frontier.
6. **Keep claim ceilings explicit.** Offline concordance can license a bounded grader-observation claim; a randomized live comparison can license a version-specific causal outcome claim if its design is complete; neither alone licenses professional equivalence, safety, general offline predictiveness, production readiness, or cross-domain capability.

## Action items for repository

- [x] Read the complete immutable v2 PDF/text and full appendix.
- [x] Verify v1/v2 stability through the recorded all-member source comparison.
- [x] Audit dataset sizes, split, annotation, GEPA settings, held-out reporting, agreement analysis, card variant genealogy, five deployment point estimates, privacy/safety descriptions, and appendix prompt limits.
- [x] Verify that `+37` tNPS and `+29` SSR are reported percentage-point deltas, while documenting that no denominator or raw record permits recomputation.
- [x] Distinguish model–model agreement from human-label reliability and external validity.
- [x] Bound the offline–online plot as retrospective selected co-movement because no coefficient, uncertainty, prospective prediction, or adaptive-selection correction is reported.
- [x] Compare Anthropic, Amazon, AgentRewardBench, RuVerBench, and existing project machinery.
- [x] Add no queue task: the evidence primarily specifies a linked empirical fixture and prospective validation exercise over existing contracts, not a nonduplicate subsystem.
