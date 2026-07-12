# SovereignNegotiation-Bench: a hidden utility is not a user mandate, and agreement is not user benefit

**Source.** Dylan Zongmin Liu, *SovereignNegotiation-Bench: Evaluating User-Owned Personal Agents in Delegated Bargaining Under Privacy, Consent, Evidence, and Institutional Pressure*, arXiv:2607.02814v1 (2 July 2026), <https://arxiv.org/abs/2607.02814v1>.

**Full text read.** Immutable seven-page v1 local PDF: `data/papers/pdfs/2607.02814v1-sovereignnegotiation-bench.pdf` (SHA-256 `50c7ac5d6d2093251dd4213bce445dd383cac66b45ef8f170e100b31b2f64eb9`). Complete local text extraction (`pdftotext -layout`): `data/papers/text/2607.02814v1-sovereignnegotiation-bench.txt` (SHA-256 `5b7a80b7acf22c78332762b0bdc86326e6476204cfb614bbac472f6292be9c3e`). Date read: 2026-07-13.

**Release boundary.** The immutable paper and arXiv metadata contain no repository, dataset, DOI, project page, or download URL. They describe an **intended anonymous artifact** containing a “v3 validation package” (pp. 1–3, 5–7). Exact-title and artifact-name searches performed during acquisition found no verifiable author- or institution-owned release as of 2026-07-12. Consequently, none of the claimed 240 scenarios, 13,440 trajectories, 61,135 parsed actions, prompts, policies, private labels, metrics, hashes, audit records, or recomputation scripts was inspected or replayed. This review treats the paper—not the intended package—as the only available primary evidence.

## Bottom line

The paper makes an important construct correction: a delegated negotiator can reach an agreement while leaking information, exceeding consent, inventing evidence, conceding below the user's interests, or waiving escalation. Agreement and even joint surplus are therefore inadequate endpoints for user representation.

Its benchmark evidence does not yet validate **user-owned mandate fidelity**. The decisive labels—private utility, reservation value, forbidden disclosures, minimum acceptable outcome, required evidence, safe concession range, and escalation appropriateness—are author-created and evaluator-only (pp. 1–3). The paper does not explain how a real user's mandate was elicited, consented to, represented, corrected, contested, or made available to the agent. Indeed, it says personal agents may know reservation values and consent boundaries (p. 1), then says all policies see only observable state while these labels remain hidden (pp. 1–2). A system cannot be judged for faithfully applying a user-owned threshold it was never authorized to see unless the benchmark separately establishes which visible instruction entails the expected behavior.

The reported experiment is also exactly one apparent trajectory per `240 scenarios × 4 model families × 14 policies = 13,440` cells. The paper gives no scenario sampling method, policy prompts, model identities, run dates, invalid-run policy, repeat reliability, bootstrap unit, weight vector, metric definitions, or audit sampling/adjudication protocol. Its strongest result is therefore descriptive and narrower than its framing: on unavailable synthetic authored cases, the integrated `FullSovereign` wrapper scores best under an unavailable author-defined composite that rewards the safeguards explicitly bundled into that wrapper.

The transferable design is a **mandate-to-consequence crosswalk** that keeps six things distinct: user-originated authority, agent-visible mandate evidence, private evaluator state, attempted disclosure/commitment, realized counterpart consequence, and claim-licensing evidence. Without that chain, “user utility” can mean author preference, “consent” can mean scenario metadata, and “sovereignty” can become rubric compliance.

## Why this matters: charter relevance and research question

This is narrow expansion advancing charter objectives A, B, and C. Personal negotiation is a bounded methodological case, not a scope boundary. It tests a general knowledge-work question: when an agent acts as a representative under asymmetric pressure, does it preserve the principal's authorized interests rather than optimize the easiest observable completion signal?

The paper asks whether agreement-focused evaluation misses privacy, consent, evidence, concession, escalation, and auditability failures, and whether an integrated policy wrapper improves the resulting joint score (pp. 1–4). The auditable question is narrower: under 240 unavailable synthetic scenarios and author-defined hidden labels, how do 14 unavailable wrappers applied to four unspecified model families differ on one composite and selected components?

## One-sentence contribution

SovereignNegotiation-Bench usefully separates deal completion from representative fidelity, but it substitutes evaluator-authored hidden labels for a demonstrated user mandate and therefore does not establish that its preferred behavior is user-owned.

## Methodology and system

### Construct and scenario schema

Each scenario is defined as `(O, H)` (pp. 2–3). Observable state `O` contains a visible goal, current message, evidence snippets, consent instructions, prior preference summaries, tool affordances, and a neutral counterpart profile. Hidden state `H` contains private utility, reservation value, forbidden disclosures, minimum acceptable outcome, required evidence, escalation appropriateness, pressure type, and safe concession range. A policy maps `O` to a multi-round trajectory beginning from an opening counterpart message; this is explicitly not a deployed turn-by-turn A2A environment (p. 3).

Half of the 240 scenarios are said to be symmetric personal-agent negotiations and half asymmetric user-to-company negotiations (p. 3). Examples include cost sharing, scheduling, refunds, subscription cancellation, platform appeal, reimbursement, and support escalation (pp. 1, 4). The paper does not report a domain taxonomy, source frame, scenario counts by activity, authoring protocol, author expertise, source provenance, candidate/rejection inventory, difficulty calibration, naturalness study, expert review, user review, or transformation lineage. “Synthetic but controlled” is candidly acknowledged (p. 5), but control is not demonstrated without the scenario files.

The term **private utility** is especially ambiguous. It may mean evaluator-only ground truth, information private from the counterpart but visible to the user's agent, or an underlying user preference only partially communicated to the agent. Those are different experimental conditions. The paper collapses them by placing utility and reservation value in `H` while describing `O` as the only policy input. This prevents attribution among failure to follow disclosed instructions, reasonable uncertainty about undisclosed preferences, and evaluator disagreement with an agent's defensible choice.

### Policies, counterpart, and treatment identity

Fourteen baselines reportedly include agreement-oriented, direct, consent-only, evidence-only, fairness-aware, company-policy-following, LLM-judge-guarded, and full-sovereign wrappers (p. 3). `FullSovereign` combines privacy minimization, consent checking, evidence grounding, concession discipline, escalation rules, and audit logging and is explicitly a scaffold rather than a new model.

No policy prompt, control-flow description, tool contract, judge prompt, model assignment, counterpart policy, turn budget, stopping rule, temperature, seed, retry rule, or treatment hash is included. The opening counterpart message appears fixed in `O`, while the model “emits an auditable trajectory” (pp. 2–3); it is unclear whether subsequent counterpart turns are generated, scripted, replayed, or synthesized inside one model response. Institutional “pressure” may therefore be authored text rather than an interactive counterparty treatment.

The comparison also risks criterion–treatment isomorphism: `FullSovereign` names and implements the same dimensions used to construct SNS. This can establish package compliance on the authored instrument, but not that the package discovered or preserved latent user interests. A stronger test would independently author mandates and outcomes, hide rubric wording from policy designers, compare modular ablations, and evaluate on held-out mandate families and alternative legitimate strategies.

### Runs and configured systems

The claimed count factorizes exactly: `240 × 4 × 14 = 13,440`. This implies one apparent trajectory per scenario/model-family/policy cell, although the paper never explicitly states repetitions. “Four model families” are not named; exact snapshots, provider settings, scaffold versions, prompts, dates, budgets, token use, cost, latency, errors, timeouts, refusals, parser failures, retries, replacements, and exclusions are absent.

The 61,135 parsed action rows average about 4.55 rows per trajectory, but the action ontology and parser are unavailable. Frozen prompts and provider-form responses would be useful provenance if released; assertions that hashes and a local gate exist are not substitutes for accessible records or provider-signed authenticity (pp. 5–7).

### Metrics and aggregation

The paper lists agreement success, user utility, privacy leakage, consent violation, evidence grounding, unsupported claims, over-concession, escalation quality, manipulation capture, auditability, and unnecessary burden (pp. 3–4). It defines an index

`SNS = w_a A + w_u U + w_e E + w_q Q − w_p P − w_c C − w_o O − w_m M − w_b B`

and correctly warns that SNS is not a universal utility function (p. 3). But v1 provides neither numeric weights nor component operationalizations, normalization, denominators, missingness rules, dependence structure, decision threshold, sensitivity analysis, or justification for interpersonal comparability. Escalation appears in the metric list but not transparently in the displayed formula; “manipulation capture” and “unnecessary burden” are named without definitions. Agreement, utility, privacy, and consent are shown for seven baselines, while the remaining components and seven policies are omitted from the main table.

A weighted score can reverse rankings as weights change. Reporting components helps, but the central “best sovereign negotiation score” claim remains unauditable without weights and sensitivity bounds. Agreement and utility may also be mechanically coupled to authored reservation thresholds, while privacy, consent, unsupported claims, and concession can overlap causally and statistically.

### Human audit

The paper reports 300 blinded items and 900 labels from three annotators (pp. 1, 4). Privacy leakage has pairwise agreement .947 and Fleiss' κ .888; consent violation has .958 and .904. Unsupported claims have κ .599 and over-concession .213. The decision to keep normative dimensions separate is sound.

However, it does not specify who annotators were, their qualifications, compensation, training, instructions, evidence view, unit sampled, stratification, prevalence, independence, number of labels per dimension, adjudication, missing labels, or whether the 300 items were trajectories or action rows. Pairwise agreement is omitted for two dimensions. “Blinded” is not defined: annotators may be blind to policy, model, metric label, or treatment, and each choice controls different bias. High agreement on an unavailable synthetic label set supports neither user consent nor professional validity.

## Evidence and reported results

Among seven displayed policies, AgreementMaximizer has agreement .861, utility .480, privacy leakage .160, consent violations .096, and SNS .554; FullSovereign has .789, .805, .031, .004, and .720 respectively (pp. 3–4). This is a useful demonstration that the benchmark's agreement and risk labels are not identical.

Table 2 reports bootstrap intervals, including FullSovereign SNS `.720 [.713, .725]`, and paired differences over 960 cells for each comparator (p. 4). The 960 denominator equals `240 scenarios × 4 model families`, confirming paired comparisons across scenario/model cells. But these are clustered: four observations share a scenario, all policies share authored labels, and scenarios may share templates. The paper does not state whether bootstrapping resampled trajectories, scenarios, templates, or model families. Cell bootstrap intervals would be too narrow for generalization to new scenario families or models.

The symmetric/asymmetric gaps are descriptive, not an identified institutional-pressure effect (p. 4). The two scenario sets can differ in domain, utility scale, evidence availability, counterpart script, concession opportunity, and grader behavior. No matched scenario transformation or random assignment isolates asymmetry. `FullSovereign`'s smaller gap therefore does not demonstrate causal resistance to institutional pressure.

No raw results, audit records, or release permit recomputation. The paper's claim that a prompt scan found zero strategy-label hits only addresses literal label strings, not semantic rubric cues, wrapper–criterion co-design, hidden-label inference, or model pretraining contamination.

## Unique insight: a representative needs a provenance-bearing mandate, not merely a hidden score function

The paper's strongest conceptual move is separating agreement from faithful representation. Its own schema reveals the next necessary distinction. A valid delegated-action benchmark needs at least:

1. **mandate origin:** real user, consenting proxy, domain expert, policy author, or synthetic generator;
2. **authority scope:** decisions, disclosures, commitments, concessions, evidence claims, and escalation rights the principal delegated;
3. **agent-visible mandate:** exact instructions, preference summaries, evidence, uncertainty, and correction channels available at decision time;
4. **evaluator-only state:** protected test facts used to assess consequences, without pretending undisclosed preferences were commands;
5. **counterpart-private state:** information legitimately hidden from the representative rather than hidden merely for grading;
6. **action and information flow:** proposed and realized disclosures, claims, concessions, commitments, waivers, and escalations;
7. **consequence state:** agreement, user-side utility under an explicit model, option preservation, privacy exposure, burden, and reversibility;
8. **adjudication basis:** why an action follows from the public mandate, which alternatives were legitimate, and whose normative judgment controls; and
9. **claim ceiling:** synthetic policy compliance, proxy-preference fidelity, real-user benefit, professional validity, privacy compliance, or deployment readiness.

This avoids two symmetric errors. If the agent is denied the reservation value, penalizing it for crossing that value tests clairvoyance or conservative defaults—not mandate obedience. If the value is disclosed in the user mandate but hidden only from the counterpart, then leakage and concession discipline are valid trace-level constructs, but the benchmark must represent separate visibility principals rather than one undifferentiated `H`.

The right intervention is a factorial visibility design: cross `user-authorized and agent-visible / user-authorized but deliberately withheld / evaluator-authored only` preferences with `counterpart-visible / counterpart-private` information, while preserving matched consequences. This distinguishes instruction following, uncertainty management, confidentiality, and rubric compliance.

## Comparison with adjacent reviewed evidence

- **JobBench** (`papers/agent-benchmarks/2026-07-12-jobbench-delegation-desire-validity.md`) asks whether people want to delegate tasks and identifies control, review, and stakeholder harms. SovereignNegotiation-Bench tests behavior after delegation but supplies no real delegation choice or user mandate. Together they require a chain from willingness and retained control to authorized action and consequence—not an assumption that a synthetic user delegated everything.
- **HAS-Bench** (`papers/agent-benchmarks/2026-07-13-hasbench-configurable-human-participation-validity.md`) varies human-participation configurations and exposes the cost of treating a nominal role as actual authority. SovereignNegotiation similarly names a user principal without recording an actual participant, correction, veto, or review path. Its “consent” is scenario state, not human consent.
- **ClawSafety** (`papers/agent-benchmarks/2026-07-10-clawsafety-cross-domain-injection-validity.md`) distinguishes malicious information exposure, adoption, attempted action, and realized harm. Negotiation needs the analogous disclosure/commitment chain: sensitive fact available → disclosure proposed → counterpart receives it → counterpart exploits it → utility changes. A lexical leak flag alone cannot establish downstream harm.
- **UnderSpecBench** (`papers/agent-benchmarks/2026-07-13-underspecbench-action-boundary-validity.md`) shows why private intended action and public authorization must be separate. SovereignNegotiation has the same problem for reservation values, evidence standards, and escalation: evaluator-only expectations are not automatically fair public requirements.

Existing participation, authority-lineage, action-safety, trace, metric, task-health, and validity contracts are the appropriate homes. A negotiation-specific schema would duplicate machinery and narrow the project.

## Limitations and validity threats

1. **No released evidence.** Every central scenario, prompt, trajectory, policy, grader, metric, hash, and audit claim is inaccessible.
2. **Intended artifact presented as validation support.** Describing file counts and gates does not make results artifact-backed for an independent reviewer.
3. **User ownership is simulated.** No user supplied, consented to, corrected, or ratified a mandate.
4. **Visibility contradiction.** Reservation values and private utilities are described as information personal agents may know but are placed in evaluator-only `H`; the paper does not resolve whether agents can access them.
5. **No public-basis crosswalk.** Hidden safe concessions, evidence requirements, and escalation labels are not shown to follow from visible instructions.
6. **Unknown authoring validity.** Scenario sources, author expertise, selection, transformations, rejected cases, and independent review are absent.
7. **Unknown counterparty mechanism.** Institutional pressure is not specified as interactive, scripted, replayed, or model-generated.
8. **Criterion–treatment co-design.** FullSovereign bundles the exact dimensions rewarded by SNS; no independent rubric authorship or held-out mandate family tests transfer.
9. **Undefined metrics.** Component predicates, weights, scales, denominators, missingness, overlap, and sensitivity are unavailable.
10. **Agreement is not user benefit.** The paper correctly states this, but its utility score is likewise not demonstrated to represent experienced or expected user welfare.
11. **One apparent run per cell.** Exact factorization suggests no stochastic repeats; run-to-run reliability is unknown.
12. **Incomplete configured-system identity.** Model families, snapshots, providers, prompts, budgets, tools, settings, and dates are absent.
13. **No invalid-run policy.** Parser errors, malformed actions, refusals, API failures, timeouts, retries, and exclusions are unreported.
14. **Dependence ignored or unclear.** Four model cells share each scenario and many scenarios may share templates; the bootstrap unit is unspecified.
15. **Asymmetry is confounded.** Symmetric and institutional scenario sets are not matched interventions.
16. **Audit provenance is insufficient.** Annotator identity, expertise, evidence view, sampling, blinding target, training, and adjudication are absent.
17. **Normative reliability is weak.** Over-concession κ=.213 directly limits strong claims on a central construct.
18. **Prompt leakage scan is narrow.** Zero literal strategy-label hits does not test semantic cueing or wrapper–grader dependence.
19. **No cost or burden estimate.** Escalation, refusal, logging, evidence checks, delay, and failed agreement have user costs not reported.
20. **No human or expert baseline.** The benchmark cannot distinguish model failure from authored mandate ambiguity or difficult normative disagreement.
21. **No naturalistic policy corpus.** Company-facing cases cannot establish institutional or legal realism.
22. **No privacy/compliance validity.** Synthetic leak labels do not establish contextual integrity, legal consent, confidentiality, or deployment safety.

## Reproducibility and operational realism

The proposed evidence package is unusually well conceived in outline: raw prompts and outputs, provider-form responses, parsed actions, hashes, audit labels, recomputation code, and leakage checks would support substantially better inspection than aggregate tables. Separating component scores and acknowledging low normative agreement are also strengths.

Actual reproducibility is currently absent because that package is neither linked nor discoverable. Even if released exactly as described, provider-side authenticity would remain unverifiable without signed receipts, as the paper acknowledges (p. 5), and scenario/metric validity would still require independent mandate and observer audits. Operational realism is deliberately limited to synthetic trajectory generation rather than live turn-taking, real users, real companies, binding commitments, or real evidence systems. The evidence can at most support a synthetic configured-policy stress test.

## Transfer to skill-bench

1. **Require principal-specific visibility.** Replace binary observable/hidden state with visibility and authority by principal: user, user agent, counterpart, tool, evaluator, grader, and auditor.
2. **Bind every private check to a mandate basis.** A concession, disclosure, evidence, or escalation check must cite the visible user instruction, authorized policy, or explicitly labeled synthetic design hypothesis that makes the consequence fair.
3. **Separate disclosure stages.** Record information availability, proposed disclosure, transmitted content, recipient access, downstream use, and utility consequence rather than one leakage bit.
4. **Separate authorization from utility.** An action can be authorized but low utility, unauthorized but accidentally beneficial, or uncertain because preferences were withheld. Score these independently.
5. **Use matched visibility conditions.** Test agent-visible confidential preferences, genuinely unknown preferences requiring clarification, and evaluator-authored preferences that cannot license obedience claims.
6. **Preserve option value.** Grade commitments, waivers, reversibility, escalation rights, and repair—not only terminal agreement and immediate utility.
7. **Validate normative labels.** For concession and manipulation, record evidence views, alternative-valid actions, annotator authority, disagreement, adjudication, and abstention; do not bury low agreement in SNS.
8. **Estimate clustered and repeated uncertainty.** Repeat stochastic runs and resample mandate/scenario families, not trajectory rows; report model-family and policy interactions.
9. **Predeclare composite sensitivity.** Publish weights, normalization, missingness, dependence, threshold/loss basis, and ranking stability across plausible weights.
10. **Bound claims.** A passing synthetic slice may support compliance with disclosed mandate predicates on those cases. It cannot establish real-user benefit, consent, negotiation competence, privacy compliance, institutional fairness, or deployment readiness.

## Concrete repository actions

No new build or consolidation task is added. The evidence refines existing participation/authority, action-safety, trace, metric-monitoring, task-health, validity-argument, and evaluator-observation work. The next applicable cross-domain pilot should instantiate a principal-specific mandate/visibility crosswalk and matched visible-versus-withheld preference conditions before adding a negotiation-specific subsystem.

## Assessment

**Evidence tier:** full immutable paper with descriptive synthetic results; no verifiable instrument, release, trace, or recomputation evidence.  
**Most reusable contribution:** treating agreement, utility, privacy, consent, evidence, concession, escalation, and auditability as separate outcomes of delegated representation.  
**Most serious flaw:** evaluator-only author labels stand in for a user-originated, agent-visible mandate, so the benchmark cannot distinguish faithful representation from compliance with an inaccessible rubric.  
**Claim skill-bench may safely make:** delegated-agent evaluation must trace principal authority and information visibility through disclosure, commitment, consequence, and adjudication; agreement alone—and hidden author utility alone—cannot establish user benefit or mandate fidelity.
