# Pezego-HITL: a useful supervision–reuse evaluation shape with an unauditable safety oracle

## Bottom line

Pezego-HITL contributes a valuable evaluation shape for consequential decision support: policy predicates, recommendation utility, latency, precedent reuse, and expert correction burden should be reported together rather than collapsed into answer quality. Its proposed architecture also keeps a location-matched extension officer between generated advice and the farmer, an appropriate authority boundary for high-stakes agricultural recommendations.

The reported evidence does not validate the stronger safety, utility, workload, or field-impact claims. The 1,240-case stream is simulated, but the paper does not explain how cases were generated or sampled, identify the policy/database versions used to score them, release outputs or labels, define invalid cases, report repeats or uncertainty, or expose the automatic judge prompt and criterion-level decisions. More seriously, the judge-calibration statistics are arithmetically incompatible. The reported 16 true positives among 19 modifications and two false positives imply 130/135 correct (`96.3%`) and Cohen's `κ≈0.843`, not the reported `91.9%` accuracy and `κ=0.77`. The same 135 reports are described first as 116 accepted directly and later as 102 unmodified plus 14 “agronomically identical” edits, leaving the reference-label policy unresolved.

The human evidence is useful as formative acceptance evidence, not outcome validation. Thirty extension officers and 36 farmers completed post-workshop/rollout questionnaires, but there is no recruitment denominator for farmers, item nonresponse or attention-check exclusion account, preregistration, comparison group, longitudinal follow-up, linked usage log, independent crop measurement, financial record, harmful-advice surveillance, or observed workload/time study. Farmer reports of crops or money saved and officer estimates of avoided yield loss are perceptions elicited after exposure. They do not show recommendation uptake, agronomic benefit, workload reduction, safe autonomous reuse, or deployment readiness.

The strongest warranted conclusion is narrow: **for one unreleased, author-configured simulated workload, Pezego-HITL is reported to occupy a better automatic-judge/latency point than four configured baselines, while a separate convenience/census-like workshop cohort reports favorable usability and trust perceptions and 19 of 135 workshop recommendations receive substantive officer modification.** This is a promising evaluation design and a source of supervision failure signatures, not a validated agricultural safety or impact result.

## Source and evidence status

**Deep review of the complete immutable primary source; no implementation or study release found in the paper/source package.**

- **Paper:** Shunbao Li et al., *Pezego-HITL: A policy-grounded large language model architecture for agricultural extension in Ghana*, arXiv:2607.13934v1 (15 July 2026), <https://arxiv.org/abs/2607.13934v1>.
- **Date read:** 2026-07-19.
- **Local PDF:** `data/papers/pdfs/2607.13934v1-pezego-hitl.pdf` (37 pages; SHA-256 `3d02f1819ac8a567a7fa9d66f18a07523c9fdfcb80219163458abdc22186ef58`).
- **Local text:** `data/papers/text/2607.13934v1-pezego-hitl.txt` (complete layout-preserving extraction; SHA-256 `2e3f5334d7e9772bc0ef632d60903a864d582d76bd931f031bd0af0de5a13737`).
- **Metadata:** `data/papers/source/2607.13934v1-metadata.xml`.
- **TeX source:** `data/papers/source/2607.13934v1-source.tar` (SHA-256 `3c0a1b51b9004d5e91e347ec7b257fb51ec9e567b67fa2636dd5f3b6b5afc87f`).
- **Machine-readable acquisition record:** `data/papers/index.json` under `arxiv:2607.13934v1`.

The source archive contains the manuscript and five figures. Its only external implementation-like link is the cited Hugging Face page for `Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash`; it provides no Pezego code, data, prompts-as-executed, policy snapshot, VCM contents, telemetry, questionnaires/responses, analysis code, or model outputs. Representative synthesis and critique prompts appear in Appendix C, but the automatic judge prompt does not. The paper gives no repository or dataset URL. This establishes absence from the acquired paper package, not proof that no private system or later release exists.

Page references below use PDF pages.

## One-sentence contribution

Pezego-HITL proposes a policy-grounded generation, audit, expert-verification, and precedent-reuse architecture plus a four-coordinate evaluation of policy alignment, recommendation utility, latency, and supervision burden, but its unreleased simulated workload and inconsistent observer statistics leave the central safety–reuse claim unvalidated.

## Why this matters to `skill-bench`

This review advances charter objectives A, B, C, and E through a bounded mechanism case: **when may a benchmark claim that expert-gated reuse reduces supervision while preserving decision safety and utility?** Ghanaian agricultural extension is the application, not a project scope boundary.

P-EVAL's four-coordinate framing is worth retaining:

```text
policy alignment
× domain utility
× operational latency/resources
× human supervision burden
```

But those coordinates are not interchangeable evidence. A judge pass is not a valid policy decision; a cache hit is not safe reuse; low textual edit distance is not low cognitive burden; questionnaire agreement is not realized utility; and perceived crop savings are not measured agronomic outcomes. Useful completion is therefore a claim ladder and an auditable routing record, not a new agriculture-specific benchmark subsystem.

## Research question and claim boundary

The paper asks how a generative decision-support architecture can dynamically allocate inference-time compute while satisfying safety-critical policy and latency constraints (pp. 2–3). It operationalizes that question through structured retrieval, automated auditing, critique, verified-case memory, and human officer review.

A defensible evidence ladder is:

```text
named and versioned policy authority
→ executable criterion with public applicability basis
→ case provenance and eligible denominator
→ observer with sufficient evidence and calibrated errors
→ candidate recommendation and route
→ expert review / modification / approval
→ reuse eligibility for a new case
→ recipient delivery and comprehension
→ recommendation adoption
→ intended and adverse field consequence
→ workload and total-resource effect
→ longitudinal non-regression under policy/environment change
→ bounded production or readiness claim
```

The paper reports pieces around observer agreement, simulated routes, workshop review, and participant perception. It does not preserve enough lineage to join those pieces or establish the later rungs.

## Methodology and system

### Architecture and configured treatments

Pezego-HITL combines (Figure 1 and §3.1, pp. 6–8):

1. natural-language input validation and schema-aware SQL retrieval;
2. generation from diagnostic and policy context;
3. a constraint-auditing layer for registration, growth-stage compatibility, dosage, and regional restrictions;
4. sequential critique/rewrite;
5. Verified-Case Memory (VCM), which stores expert-approved recommendations;
6. location-matched extension-officer verification before farmer delivery; and
7. logged expert edits intended to update prompts, indexes, and policy gaps.

VCM routing uses `s = 0.6*s_struct + 0.4*s_semantic`, with strict crop, pest, and growth-stage mismatch forcing `s=0`; cases at `s≥0.83` reuse a template (pp. 6–8). This is a sensible typed-first pattern: hard applicability fields gate semantic similarity.

The paper does not specify what `s_struct` contributes after the strict Boolean gate, how geography is normalized, how a cached template is parameterized for dosage/weather/location, how many templates exist, which officer approved each one, whether approval was independent, how contradictory approvals are handled, or what invalidates a case after policy, product, pest, weather, or crop-stage changes. “Aggregated deltas” update prompts and indices, but there is no promotion threshold, authority rule, held-out validation, rollback, or version history. An approved historical answer and a valid current answer are therefore conflated.

The main proprietary configuration uses `gpt-5.4-nano` for four pipeline layers, temperature zero except synthesis at `0.2`, a 16,384-token context, MiniLM-L6-v2 embeddings, SQLite, and Chroma DB. The judge is `gpt-5.5-pro` at temperature zero with chain-of-thought prompting (§4.1, pp. 9–11). The open configuration substitutes `Qwen3.5-9B-DeepSeek-V4-Flash`; hardware, quantization, serving stack, context, and exact endpoint identities are not reported.

Four baselines are described (§4.2, pp. 10–11): direct generation, unstructured vector RAG, SQL/tool RAG without post-generation audit, and multi-agent critique without VCM or expert validation. These are architecture packages, not isolated component ablations. Prompt topology, retrieved evidence, number of calls, context length, and human-review policy differ. The paper gives no randomization, shared-output replay, exact component budgets, or trial manifest.

### Policy and case provenance

The paper refers to registered pesticide active ingredients, Ghana EPA registration, crop stages, dosage limits, pre-harvest intervals, regional bans, environmental safety, and integrated pest management (pp. 2, 6–8, 29–30). It does not identify the actual policy documents, issuing authorities and URLs, publication/effective dates, database tables, extraction process, expert transformation, coverage, conflict policy, or snapshot hashes used in the experiment.

The 1,240 simulated reports are called “representative” of Eastern and Ashanti smallholder scenarios across major and minor crop seasons (§5.2, p. 14). No generation method, source distribution, inclusion/exclusion rule, crop/pest/stage/geography counts, duplicate policy, severity mix, difficulty strata, train/cache/test separation, sampling seed, expert authoring, or independent case validation is described. There is no gold recommendation set. Because the same workload supplies route opportunities, threshold selection, and reported quality, it is impossible to tell whether 59.6% reuse reflects realistic recurrence, constructed cache affinity, duplicate templates, or leakage.

### PAR, AUR, latency, and denominators

P-EVAL defines (§3.2, pp. 8–9):

- **PAR:** a strict conjunction of `M` binary policy constraints per case, averaged over `N` cases;
- **AUR:** the mean fraction of `K` utility requirements such as dosage, dilution, and safety instructions;
- **H:** modification incidence plus normalized edit magnitude; and
- **L:** P95 execution latency.

This separation is conceptually strong. It avoids calling a fluent but banned recommendation useful and recognizes tail latency and expert labor as first-class outcomes.

The implementation is under-specified. The paper does not enumerate `M` or `K`, publish criterion wording and applicability, distinguish `not_applicable` from pass, define multi-chemical or abstention cases, state whether final expert-verified or pre-review drafts are graded, describe parser/invalid outcomes, or give numerator counts. Table 1 reports rounded rates over 1,240 rows, but no row-level outcomes, missingness, confidence intervals, clustered uncertainty, repeated calls, or judge-stability checks. PAR and AUR are both produced by the same unreleased model judge and should be treated as correlated configured-observer outputs, not independent safety and usefulness evidence.

Latency reports only P95. There is no measurement boundary (client, network, queue, API, or server), warm/cold-cache policy, concurrency, geographic endpoint, hardware, sample count per configuration, retry/timeout rule, median or dispersion table, tokens, dollars, energy, or expert-review latency. Claims about spotty rural connectivity and local edge usability are not tested by simulated network impairment or field timing. Server-side precedent reuse does not automatically reduce mobile network round trips; the manuscript later asks for client-side offline caching, acknowledging the missing mechanism (pp. 19–21).

### Automatic-judge calibration

The judge is compared with 135 workshop reports: 19 human “modify” and 116 “accepted directly” decisions (§4.3, pp. 11–12). The paper reports (§5.1, pp. 13–14):

- 16 of 19 modifications detected (`84.2%` recall);
- two false positives (`88.9%` precision);
- `91.9%` accuracy;
- `F1=0.865`; and
- `κ=0.77`.

The precision, recall, and F1 are mutually consistent: `TP=16`, `FN=3`, `FP=2`. With 116 human negatives, this requires `TN=114`. That confusion matrix yields:

- `(16+114)/135 = 96.296%` accuracy;
- expected agreement `≈0.76346`; and
- Cohen's `κ≈0.84342`.

The reported `91.9%` accuracy would mean only 124 correct rows, incompatible with five total errors. The reported `κ=0.77` is also incompatible with the implied marginals. This arithmetic was independently recomputed from the paper's counts. Without the row-level table, no alternative missing/exclusion or label mapping can reconcile the statistics.

A second inconsistency appears in §5.4 (pp. 16–18): the 116 accepted cases become 102 unmodified plus 14 edited but judged “agronomically identical,” while 19 require substantive modifications. The calibration section says 116 were accepted directly. If the 14 were edited, “modify” is not a simple observed button label; it is an adjudicated substantive-equivalence construct. The paper does not state who made that equivalence judgment, whether it preceded judge evaluation, or whether the judge predicted edit incidence, substantive error, PAR failure, AUR failure, or a composite.

Even if the arithmetic were repaired, this is weak judge validation. Officer qualifications are summarized only at cohort level; report-to-officer assignment, number of labels per report, independence, disagreement, adjudication, confidence, evidence access, policy snapshot, and criterion labels are absent. The judge apparently sees recommendation/context, but its exact prompt and evidence view are not released. A single imbalanced 135-row comparison from the same workshops cannot establish a reliable proxy over 1,240 simulated cases, particularly across criterion types and base-model outputs.

### Expert workload

Nineteen of 135 workshop reports required substantive modification (`14.1%`). Modification categories overlap: pesticide selection/dosing 16/19, safety/PPE 9/19, and scouting/cultural controls 9/19 (§5.4, pp. 16–19). Mean word-level edit ratio among the 19 is `38.3%` (median `38.8%`). These are useful failure signatures: apparently acceptable drafts still require local product names and doses, environmental safeguards, and field-practice corrections.

They do not show that VCM reduces workload. There is no no-VCM or prior-workflow workload arm for the 135 reports, no route breakdown, no review time, no interruption/queue delay, no case assignment, no cognitive-load measure, no accepted-but-wrong audit, no downstream quality check, and no repeated-season total. Edit distance is content displacement, not attention, diagnosis difficulty, accountability, or cognitive setup cost. The paper's assertion that VCM “reduces the overall expert modification rate to 14.1%” is causal language unsupported by the workshop design.

The error categories also cut against safe expert substitution. Sixteen of 19 substantive corrections concern pesticide selection or dosing, and nine concern safety/PPE. These are precisely the high-loss predicates the policy/audit machinery is supposed to control. An 85.9% acceptance proportion cannot by itself show that unreviewed recommendations are safe.

### Human questionnaires

The officer survey has 30 respondents, described as the complete smartphone-equipped pilot cohort across targeted Eastern and Ashanti districts (§4.4, pp. 11–12). The farmer survey has 36 Ashanti-region, primarily maize-growing respondents who interacted with the app during field-testing/rollout (§4.5, pp. 12–13). Appendices A–B release item text; D–E report demographics and Likert distributions.

Strengths include participant-role descriptions, complete item wording, five-point response distributions, demographic tables, attention-check intent for officers, and internal-consistency estimates. Officer scales report `α=.967`, `.885`, and `.959`; farmer scales report `.949` and `.944`.

Important limits remain:

- “near-total census” applies only to the equipped officer cohort, not Ghanaian extension officers or even necessarily all officers in the regions;
- invited, eligible, consenting, completed, excluded, and analyzed denominators are not separately reported;
- no farmer sampling frame, recruitment method, number approached, nonresponse, translation validation, interviewer assistance, literacy/acquiescence control, or attention check is provided;
- the paper says the officer attention item filters responses but reports no failures/exclusions;
- high alpha can reflect redundant favorable items and is not construct validity, test–retest reliability, measurement invariance, or freedom from workshop demand effects;
- there is no pre/post measure, comparison group, randomization, behavioral reuse observation, or longitudinal follow-up;
- the same exposed participants rate speed, usefulness, trust, safety, future use, and perceived impact after training/rollout;
- item-level missingness and open-text coding are not reported.

The questionnaire does reveal a meaningful tension. Officers strongly value modification and verification (`S4=4.33`, `S5=4.20`) while the mistake-noticing item has mean `3.37`, with `46.7%` agreeing/strongly agreeing and `30.0%` disagreeing/strongly disagreeing (Table E.8, p. 34). This supports demand for retained human authority, not proof that the loop prevents every bad recommendation or has no overhead.

Farmer trust in officer verification is high (`T4=4.50`) and direct-call usefulness is high (`T5=4.56`; Table E.11, p. 36). These are exposed-user perceptions. The final questions ask whether recommendations saved crops and money, and Figure E.12 displays favorable self-reports, but no yields, treated/untreated plots, pest severity, intervention timing, purchases, expenditures, prices, or independent records are collected. The manuscript's claim that perceived savings demonstrate “direct positive impact” exceeds the measurement.

## Evidence interpretation

### What the source supports

1. A coherent architecture proposal separates policy retrieval/audit, generation, precedent reuse, and officer approval.
2. A useful multi-objective evaluation vocabulary separates policy alignment, agronomic completeness, latency, and supervision burden.
3. On the unreleased 1,240-case simulated stream, the paper reports `PAR=.94`, `AUR=.95`, P95 `12.9s`, and 739/1,240 VCM routes for the proprietary package; the open package reports `.86`, `.88`, and `10.2s` with the same reuse ratio.
4. The paper reports monotonic package improvements from direct generation through structured retrieval and critique under one automatic observer.
5. Nineteen of 135 workshop reports receive substantive officer modifications, concentrated in dosing/product, safety, and field-practice details.
6. Exposed officers and farmers report favorable usability, trust, connection, and future-use perceptions and identify connectivity and localization needs.
7. Human verification is valued by both participant groups, supporting retained review authority as a design requirement.

### What the source does not support

- that the 1,240 cases represent Ghanaian query prevalence or hard/safety-critical cases;
- that the policy database is complete, current, authoritative, or correctly projected into executable criteria;
- that PAR is a valid policy-compliance rate or AUR is a valid agronomic-utility rate;
- that the automatic judge has the reported accuracy or kappa;
- that judge agreement transfers from workshop reports to simulated cases, different model outputs, rare harms, or future policies;
- that 59.6% cache routing is safe, causally improves quality, or remains valid under policy/environment change;
- that `τ=.83` is prospectively Pareto-optimal;
- that VCM reduces expert review incidence, time, cognitive burden, or total staffing needs;
- that latency was measured under rural network or edge-deployment conditions;
- that any recommendation was followed, caused crop protection, avoided financial loss, or avoided harm;
- that questionnaires establish trust calibration, field effectiveness, national generalization, expert substitution, production fitness, or readiness.

## Unique insight: supervision is an allocation policy with two independent risk denominators

P-EVAL's most important idea is not its four reported numbers. It is that human review, automatic auditing, generation, and precedent reuse form an **allocation policy**. That policy has two denominators that the paper does not preserve:

1. **route-opportunity denominator:** every eligible case considered for cache, generation, automatic acceptance, or escalation, including invalid and stale-policy cases;
2. **loss-opportunity denominator:** every case where a wrong route could cause policy, agronomic, financial, environmental, or workload loss, stratified by severity and observability.

A high cache-hit rate can be good for latency while bad for safety if the eligible population is constructed from near-duplicates or stale precedents. A low modification rate can mean high initial quality, reviewer fatigue, weak evidence, lenient equivalence policy, or unobserved false acceptance. A high judge kappa can coexist with poor rare-harm recall. A high survey trust score can be harmful if confidence outruns correction reliability.

The minimum auditable event is therefore not “cache hit” or “expert approved.” It is:

```yaml
supervision_route_event:
  query_and_context_hash: ...
  policy_snapshot_and_effective_time: ...
  candidate_route: cache | generation | escalate | abstain
  eligibility_predicates_and_evidence: ...
  precedent_id_and_approval_scope: ...
  observer_evidence_views: ...
  automatic_checks_and_invalid_states: ...
  human_reviewer_authority_and_decision: ...
  initial_to_final_semantic_delta: ...
  review_time_and_queue_delay: ...
  delivered_recommendation: ...
  uptake_and_field_outcome: ...
  adverse_event_or_later_reversal: ...
  downstream_memory_admission_or_invalidation: ...
```

This event joins existing configured-system, metric, task-health, participation, evidence-view, resource, trace, validity, and compounding-memory machinery. It does not justify a new Pezego-specific schema.

## Comparison with adjacent reviewed evidence

- **AgentRewardBench:** its central warning applies directly: agreement is conditional on predicate, evidence view, prevalence, label policy, and use. Pezego supplies none of the row-level adjudication lineage needed to resolve its internally inconsistent confusion statistics. A model–human kappa cannot by itself establish an autonomous safety judge.
- **Pista and HiLSVA:** editable plans and expert controls create oversight opportunity, not effective oversight. Pezego adds real officers and observed edits, but still lacks matched defect opportunities, proposition-level adoption/repair, collateral verification, review time, and downstream consequences. Text edit distance is no substitute.
- **Online skill/memory budget value:** VCM must be charged for acquisition, expert verification, indexing, retrieval, context/parameter adaptation, audit, policy refresh, false reuse, invalidation, and review—not only generation latency saved. Reuse ratio is not amortized portfolio value.
- **Scalable Delphi:** configured model observers and same-model panels are not domain experts. Pezego does include qualified practitioners, but a single officer decision without independent labels, criterion evidence, or adjudication is still not an error-free gold standard.
- **Production-validity evidence:** offline score improvement, exposed-user perception, and simulated telemetry are separate rungs from prospective field behavior and outcomes. Combining them in one “integrated evidence fusion” set does not make the missing joins disappear.

## Limitations and validity threats

1. The claimed two-year programme has no dates, phases, protocol changes, sample chronology, or frozen analysis cut.
2. The exact policy sources, authorities, versions, effective dates, database schema, and transformation process are absent.
3. The 1,240 cases have no generation, sampling, provenance, strata, deduplication, difficulty, or expert-validation account.
4. “Representative” is asserted without a target query population or sampling frame.
5. Cache construction, template count, source cases, and train/cache/test separation are not reported.
6. The same 739/1,240 route count across two model packages is descriptive workload identity, not replicated generalization.
7. VCM eligibility lacks typed applicability beyond three hard fields plus a composite similarity score.
8. Weather, location, product availability, dosage, and policy-version differences are not shown to be safe under template reuse.
9. No stale-policy invalidation, expiry, contradiction, supersession, reapproval, or rollback mechanism is evaluated.
10. Threshold `τ=.83` appears selected on the reported workload; no held-out threshold validation or loss function is given.
11. The threshold ablation is only a figure; numeric cells, repeats, uncertainty, and routing errors are unavailable.
12. Baselines are compound packages and are not resource- or prompt-matched component ablations.
13. Temperature-zero hosted calls are not proof of determinism; no repeated trials are reported.
14. Exact model snapshots, endpoint dates, system prompts, retries, failures, and provider behavior are not preserved.
15. Open-model hardware, serving, quantization, and configuration are absent.
16. The automatic judge prompt, parser, outputs, reasoning, criterion labels, and invalid-call handling are unreleased.
17. PAR criteria, applicability, conjunction semantics, and numerator counts are not fully specified.
18. AUR criterion inventory, weights, admissible alternatives, and decision threshold are not specified.
19. The same judge produces PAR and AUR, so the apparent two-coordinate result may share observer error.
20. No deterministic replay against the named policy database validates judge policy decisions.
21. Judge calibration statistics are arithmetically inconsistent.
22. The 116 accepted labels are inconsistently described as direct acceptance versus 102 unchanged plus 14 equivalent edits.
23. “Modify” incidence and substantive-correctness adjudication are conflated.
24. Expert labels are mostly single-decision records; independence, disagreement, adjudication, and confidence are absent.
25. Officer evidence access and report assignment are not described.
26. The 135 workshop reports have no sampling frame, route mix, case mix, or linkage to the 1,240 simulated cases.
27. Accepted-but-wrong false negatives receive no independent audit.
28. Edit distance measures lexical change, not cognitive burden, safety importance, review time, or accountability.
29. Modification categories overlap and have no independent coding protocol or agreement.
30. No matched no-VCM, no-draft, alternative-interface, or ordinary-workflow condition identifies workload relief.
31. P95 latency lacks a measurement boundary, concurrency, cache-temperature, network, hardware, timeout, and missing-run policy.
32. No median, distribution table, uncertainty, tokens, dollars, energy, or total human time is reported.
33. Rural network and edge-deployment claims are not tested under field connectivity conditions.
34. The officer cohort is census-like only for the equipped pilot cohort, a selected post-adoption population.
35. Farmer recruitment, approach denominator, nonresponse, exclusion, and representativeness are absent.
36. Attention-check outcomes and item-level missingness are not reported.
37. Translation and interviewer-assistance procedures are not validated.
38. High Cronbach alpha does not establish construct validity and may reflect item redundancy/common method.
39. Surveys are post-exposure and lack baseline, control, randomization, or longitudinal follow-up.
40. Trust and future-use intentions are not calibrated reliance or observed reuse.
41. Farmer crop and financial benefits are unverified self-reports with no counterfactual or records.
42. No real-query corpus, delivery log, adoption record, agronomic measurement, harmful-advice surveillance, or complaint/reversal ledger is released.
43. Participant interaction is asserted, but report counts and participant-to-report links are unavailable.
44. Ethical consent text is shown, but ethics-review body, protocol number, data governance, compensation, withdrawal, and privacy handling are absent.
45. Competing interests are declared absent despite three authors' affiliation with Mutus Tech Ltd; the system ownership/funding relationship is not explained.
46. No code, data, policy snapshot, telemetry, survey responses, analysis scripts, or complete prompts are released.
47. The paper's conclusions use “guarantee,” “prove,” “direct impact,” “cognitive relief,” and “successful deployment” beyond the evidence.
48. Geographic/crop generalization is explicitly limited, while the architecture's broader “scalable template” claim is not independently tested.

## Reproducibility and operational realism

Reproducibility is **good for reading the proposed architecture and questionnaire wording, weak for checking the empirical tables, and effectively absent for replay**. The immutable PDF, text, TeX, figures, representative synthesis/critique prompts, equations, reported tables, and questionnaire items are preserved. The judge arithmetic can be audited because counts are printed, and that audit reveals a material inconsistency.

Reproducing the experiment would require the 1,240 case rows; 135 workshop reports and every officer decision/edit; source→policy-table lineage; VCM state and approvals; exact prompts and model snapshots; per-configuration outputs, route events, criterion observations, token/latency receipts, invalid/retry logs, and analysis code; questionnaire response rows and exclusions; and a hardware/network manifest. None is public in the acquired package.

Operational realism is mixed. The application has real stakeholder roles, smartphones, officer verification, regional context, connectivity constraints, and workshop/rollout exposure. The 19 substantive edits identify plausible high-consequence defects. But the main package comparison runs on simulated cases with an automatic observer; field routing, queue behavior, review time, recommendation uptake, crop outcomes, adverse events, policy drift, and longitudinal maintenance are not observed. The source is best treated as a **configured supervision-routing design plus formative stakeholder evidence**, not a production evaluation.

## Transfer to `skill-bench`

### Retain

1. Report policy/safety, utility, latency/resources, and human burden separately.
2. Use hard typed applicability gates before semantic precedent similarity.
3. Keep an authorized human review step for high-loss advice until safe deferral is empirically established.
4. Preserve the initial draft, final decision, exact edit, route, latency, and memory transition.
5. Treat local dosing, product, PPE, environmental, and scouting corrections as distinct failure signatures.
6. Include participant trust and usability as stakeholder outcomes, but never substitute them for task or consequence validity.

### Repair before reuse

1. Bind every policy check to an authority, source locator, effective interval, transformation, applicability rule, and executable witness.
2. Freeze a case-population manifest and report eligible, scored, invalid, abstained, retried, cached, generated, escalated, modified, and delivered denominators.
3. Preserve criterion-level human and automatic observations independently; audit confusion arithmetic and disagreement before promotion.
4. Calibrate routing by severity-weighted loss, not raw cache hit or aggregate judge rate.
5. Require new-case and policy-drift challenges, negative controls, stale precedents, near-neighbor traps, and held-out threshold selection.
6. Measure review time, queue delay, interruption, diagnosis effort, false acceptance, and total staffing—not edit distance alone.
7. Join technical trials to prospective recipient delivery, uptake, intended outcome, adverse outcome, and reversal evidence before utility claims.
8. Version memory admission, applicability, expiry, supersession, reapproval, and rollback, with policy snapshots and downstream dependencies.
9. Repeat configured trials and estimate uncertainty at case, route, reviewer, model, and time levels.
10. Separate a favorable exposed-user questionnaire from a behavioral adoption or field-impact study.

### Falsifiable cross-domain validation slice

Use a non-agricultural and an agricultural-like policy-constrained task family to test the general mechanism without narrowing the benchmark. For each family, create:

- fresh eligible cases, true near-neighbor cases, semantic lookalikes blocked by one hard field, and precedents made stale by a policy update;
- independent authoritative policy predicates and utility criteria;
- matched no-memory, memory-with-review, and memory-with-risk-based-deferral conditions under the same resource envelope;
- blind criterion-level human and automatic observations with explicit `insufficient_evidence` and adjudication;
- review time, queue delay, false-accept loss, latency, and complete resource records; and
- delayed re-evaluation after a policy version change.

Useful evidence would show prospectively that routing preserves criterion-specific validity within a declared loss bound while reducing total review burden and remaining reversible under policy drift. A high reuse ratio or favorable survey would not count as completion.

## Concrete repository actions

1. **Add no new schema/build task.** Existing configured-system, criterion/evidence-view, grader, metric-monitoring, task-health, resource, participation, validity, longitudinal, and compounding-memory contracts can represent the missing obligations.
2. **Route the synthesis implication to existing consolidation.** The nonduplicate rule is: supervision-routing claims require route-opportunity and loss-opportunity denominators plus policy/memory validity at the moment of reuse. This review should be indexed for later canonical synthesis rather than spawning an agriculture-specific subsystem.

## Claim boundary

Pezego-HITL v1 supports an inspectable architecture proposal, a multi-objective evaluation vocabulary, reported simulated package results, a set of 19 substantive officer correction cases, and favorable post-exposure participant perceptions. It also provides direct negative evidence about the current evaluation instrument: the published judge counts do not reproduce the published accuracy or kappa, and the reference-label policy changes across sections.

It does **not** establish a valid policy oracle, representative case population, calibrated automatic judge, safe cache reuse, causal workload reduction, field latency advantage, recommendation adoption, agronomic utility, avoided harm, crop or financial impact, trust calibration, expert substitution, production fitness, national generalization, or deployment readiness.