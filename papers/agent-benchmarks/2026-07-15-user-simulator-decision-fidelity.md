# Simulated Customers Never Walk Away: real outcomes expose simulator error, but future-outcome stratification is not an online user model

## Source and review status

**Deep review of the complete immutable primary source.** I read the full 19-page arXiv v1 paper and checked the extraction, title, page count, and hashes against the preserved PDF. The paper states that its protocol, prompts, analysis code, and conversation-level derived statistics are released, but neither the PDF nor the arXiv metadata supplies a repository, DOI, dataset identifier, or artifact URL. Raw conversations and payment records are explicitly private. The empirical implementation and reported statistics therefore remain manuscript-reported rather than independently replayed.

- Paper: Liang Chen, *Simulated Customers Never Walk Away: Decision Fidelity of LLM User Simulators Measured Against Real Purchase Outcomes*, arXiv:2606.20708v1, <https://arxiv.org/abs/2606.20708v1>
- Version read: immutable v1, submitted 16 June 2026
- Date read: 2026-07-15
- Local PDF: `data/papers/pdfs/2606.20708v1-user-simulator-decision-fidelity.pdf` (19 pages; SHA-256 `a5bc3f026a9a6bccc04f1e6dc345d826bc0e7de7487bfa34cca33689aa27df5c`)
- Full local text: `data/papers/text/2606.20708v1-user-simulator-decision-fidelity.txt` (SHA-256 `e243e3bf0906a3d1229c025473f89925e0e5bb67e1e6116ef975de445afa0cbd`)
- Evidence status: full paper read; no inspectable release or raw outcome corpus
- Tags: user simulation, consequential outcomes, persuasion, teacher forcing, latent state, intervention validity, clustered inference

## One-sentence contribution

The paper makes an important construct correction—human-sounding or assigned-goal behavior does not validate whether a simulator reproduces stopping, refusal, and commitment under real stakes—and supplies a clean same-history next-turn probe against payment-linked production dialogue, but its future-outcome contrast measures simulator error heterogeneity across realized buyer/non-buyer strata rather than proving that the simulator had enough observable information to identify who should disengage, and it does not validate free-running agent evaluation or tactic effects.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C by testing a load-bearing assumption in interactive benchmarks: a fluent model-backed user can be treated as the human side of a task. The source adds evidence that this substitution can preserve surface interaction while deleting the decision boundary that matters operationally—whether the counterparty continues, refuses, revises, or exits.

The cross-domain issue is broader than sales:

```text
real participant population and stakes
→ observable pre-decision context
→ latent willingness / authority / preference state
→ simulator evidence view and policy
→ generated response or non-response
→ agent adaptation
→ realized action, stopping, burden, and consequence
```

Assigned-goal simulators fix the latent state by construction. Outcome-free realism studies can validate style or disclosure without validating the transition from uncertainty to refusal, commitment, escalation, withdrawal, or silence. Yet an outcome-conditioned discrepancy also does not by itself show that a simulator could have inferred the represented person's latent state from its allowed evidence. `skill-bench` therefore needs both **decision-consequence fidelity** and **information sufficiency** before a synthetic participant can support human-interaction claims.

## Research question and defensible claim boundary

The paper asks whether LLM user simulators reproduce the decision-state dynamics of real users facing consequential choices, rather than merely communicating like role-playing humans (pp. 1–5). It evaluates next-turn state discrepancies after identical production conversation prefixes and compares those discrepancies between customers who eventually paid and those who did not.

The strongest defensible claim is:

> On selected outcome-balanced subsets of one Chinese matchmaking-sales corpus, under an unreleased profile-conditioned simulator and LLM state instrument, the reported conversation-level ordinal next-turn bias is more engagement-positive for eventual non-payers than for eventual payers; this contrast persists in one alternative simulator, one alternative instrument, and one prompt variant that globally licenses disengagement.

The evidence does **not** establish human-equivalent simulation, population representativeness, an online ability to identify future buyers or non-buyers, a causal willingness-decay mechanism, free-running dialogue fidelity, the causal effect or real loss of sales tactics, improved production-agent quality, transport to other decisions or cultures, professional validity, safety, deployment fitness, or readiness.

## Methodology and system

### Production population, provenance, and outcome linkage

ZhenaiSales contains 2,790 production conversations between a deployed LLM sales agent and real parent customers of a Chinese relationship-matchmaking platform. The paper reports 793 converted conversations with a verified successful payment order and 1,997 non-converted conversations. Ninety-eight percent have demographic profiles; conversations contain 6–80 turns with median 16. Buyer dialogues are truncated at the first payment timestamp, removing a reported mean of 19 post-payment messages (pp. 2, 7; Appendix D, p. 16).

The extraction specification includes personalized enterprise-WeChat messages, non-broadcast/nonempty/nondeleted records, one production app identifier, successful order action code 3, and exclusion of 20 internal test users. Profiles include child age, education, occupation, and income plus parent location and housing/vehicle status (pp. 6–7, 16).

This is materially stronger outcome provenance than assigned-goal role-play. Important denominators remain unspecified:

- observation window and minimum follow-up for labeling a conversation non-converted;
- whether later, off-platform, canceled, refunded, duplicate, or externally attributed payments exist;
- whether one customer contributes several conversations or one conversation can link to several orders;
- customer/session identity resolution and clustering;
- extraction dates, market/geography, product/price regimes, and production-agent versions;
- missing profile handling beyond the aggregate 98%;
- conversation, profile, and outcome join failures;
- sample selection from the 2,790 records into each experimental panel.

Payment is a consequential observed endpoint, but it is not a complete measurement of willingness. Non-payment can reflect affordability, timing, channel switching, service mismatch, family disagreement, censoring, or an already-satisfied need. Payment can reflect forces not visible in the probe prefix. The paper acknowledges payment as a coarse proxy (p. 11), but often interprets the contrast as a specific latent willingness-decay mechanism.

The ethics statement reports platform authorization, analysis on platform infrastructure or de-identified exports, pseudonymization, paraphrased quotations, a disclosed AI assistant, and use under platform terms (p. 13). It does not report individual research consent, an institutional ethics review, privacy-review protocol for model calls, purpose-specific permission for demographic inference, data-retention/deletion controls, or whether proprietary simulator/judge providers received de-identified profile and dialogue content. Platform authorization and terms-of-service disclosure are not the same evidence as participant consent for research or external model processing.

### Teacher-forced probe construction

For each sampled real conversation, probes are placed at 30%, 60%, and 90% of user turns after skipping the opening greeting and deduplicating repeated indices. At each probe:

1. the real next user turn is scored under the preceding real history;
2. the simulator receives the identical real prefix plus the user's demographic profile and generates one next turn;
3. the same LLM instrument scores both turns;
4. ordinal simulated-minus-real depth is averaged within conversation (pp. 5–6, 16).

This is a strong local control. It removes accumulated rollout divergence and holds the observed agent treatment/history fixed between branches. It measures a **one-step conditional response operator** at realized histories.

It is not a free-running user simulation. The simulator never determines whether the conversation reaches the next probe, how its response changes the agent's next action, when silence terminates the episode, or whether repeated generated turns preserve a latent decision state. Probe positions are fractions of the *completed real conversation's* eventual length, information unavailable online. Late probes therefore condition on future duration and survival in the real dialogue. Short-dialogue index deduplication likely explains why 374 conversations yield 1,109 rather than 1,122 probes, but the paper does not report the deduplication/missingness flow by outcome.

### Simulator and decision-state instrument

The primary simulator receives a natural-language profile and real prefix and is instructed to answer as the parent in brief, colloquial Chinese. The instructed variant additionally permits disinterest, perfunctory replies, impatience, topic changes, stalling, and non-response. A DeepSeek-V4-Flash simulator is used as a family swap (pp. 6, 9; Appendix B, pp. 15–16).

The instrument maps the latest user message in causal context to engagement stage (`resisting`, `exploring`, `engaging`, `considering`, `deciding`), emotion, blocker, convergence delta, and a key span. The paper's scalar depth assigns 0–4 to those ordered stages. A separate check compares causal versus full-context labeling, and a DeepSeek instrument re-scores 150 conversations (pp. 6, 9, 15–16).

The implementation identity is incomplete. “Claude” is not an exact model endpoint; the original Chinese prompts, system messages, provider dates, temperature, seeds, sampling/retry policy, invalid JSON rate, fallbacks, profile-rendering code, and instrument versions are absent from the paper. Appendix A/B summarizes translated prompts rather than supplying exact executable bytes. The claimed release could resolve some gaps, but no artifact locator is present.

The instrument has no reported human validation. A shared judge removes some *common* additive history bias, not arbitrary classification error. Style-dependent source effects, terse-message interpretation, profile stereotypes, model-family shared priors, and category-boundary errors can differ between real and generated text. Swapping to another LLM family demonstrates model-judge robustness of the reported direction, not construct validity or human agreement.

### Estimands and the future-outcome identification problem

For each probe, depth bias is `D(h) = depth(simulated) - depth(real)`. The primary endpoint averages within conversation, then subtracts buyer mean bias from non-buyer mean bias:

`Δ = E[D̄ | eventual non-payment] - E[D̄ | eventual payment]`.

A one-sided conversation-level permutation test with 20,000 shuffles and Cohen's `d` are reported. Bootstrap intervals accompany principal estimates (pp. 5, 7–9, 16).

The contrast is useful: it detects a simulator whose errors are unevenly distributed across consequential realized outcomes. But the paper's formulation overstates what this identifies.

The simulator is conditioned on profile and history, **not on eventual outcome or the real user's private latent state**. Stratifying afterward by realized `y` asks whether the simulator's independent next-turn draw matches the particular real user's state within future-outcome groups. If histories and profiles do not identify the private causes of eventual payment, even a simulator that perfectly samples `P(next turn | observable history, profile)` cannot reproduce each realized user's outcome-correlated latent state. Conversely, a simulator could reduce `Δ` by receiving an outcome proxy or memorizing group-correlated features without becoming a faithful interactive person.

Thus the observed contrast can arise from at least three different gaps:

1. **behavioral support gap:** the model cannot generate realistic refusal/silence;
2. **state-inference gap:** the required latent willingness is not recoverable from allowed context;
3. **population/proxy gap:** eventual payment strata differ for reasons not represented by the proposed state instrument.

The paper argues that the model “has access to the same prefix” and therefore lacks a behavioral mode rather than information (p. 10), but same observable prefix does not imply access to the real person's private motivation, financial constraints, family state, competing offers, or future shocks. The instructed arm shows that a global disengagement license does not assign disengagement to the same future-outcome strata; it does not distinguish missing inference signal from missing behavioral mode.

The proposition's cancellation claims are also narrower than the prose. Additive history bias cancels only under the assumed additive/shared form. An “outcome-independent simulator shift” cancels by definition; this is algebra, not evidence that actual style or profile errors are outcome-independent. `Δ = 0` is necessary but radically insufficient for distributional fidelity: equal nonzero bias in both strata, excessive variance, random state assignment, wrong transition timing, or compensating category errors can all yield zero. Likewise, a buyer mean bias of `+0.09` does not establish that buyers are reproduced “nearly perfectly”; Table 2 still reports a 12.9-point increase in buyer `considering`, and no paired agreement, transition matrix, distributional distance, or calibration curve is reported.

### Sampling, dependence, missingness, and censoring

The primary panel has 374 conversations (181 non-buyers, 193 buyers; 1,109 probes). Simulator-swap and instructed panels each have 200; instrument swap has 150; the action-conditioned analysis has 595 probes. The paper says outcome-balanced samples are drawn and real labels are reused, but does not specify randomization, seeds, eligibility, overlap among panels, why panel sizes differ, why the primary panel is not exactly balanced, or why only 595 probes enter the action analysis.

Conversation-level aggregation appropriately avoids treating repeated probes as independent in the primary test. It does not address repeated customers, shared templates/agent versions, time cohorts, or overlap across robustness panels. Permuting outcome labels assumes exchangeability of conversation-level errors under the null; profile, history length, sales-agent behavior, and calendar/product regimes may differ by outcome. The reported descriptive difference remains meaningful, but its nominal inference is not a population-randomized contrast.

No missing/invalid-generation, malformed-instrument, timeout, API failure, profile-missing, ambiguous-payment, or exclusion ledger is reported. Bootstrap unit and method are not specified. The robustness panels appear selected from the same corpus rather than independent replications.

### Action-conditioned analysis

A DeepSeek instrument assigns the preceding agent move to one of six categories for 595 probes. The paper compares real and simulated resisting/considering proportions after each action using cell-wise Fisher exact tests (pp. 9–10).

This can localize where one-step response discrepancies are largest. It cannot show that pitching causes real customers to leave, that the simulator rewards a policy in a free-running training loop, or that a production agent optimized against the simulator loses revenue. Agent actions were not randomized; action choice responds to prior customer state. The real/simulated observations are paired at each probe, but Fisher exact tests treat counts as independent rather than using paired methods, and several probes remain nested in conversations. Multiple action×state tests receive no multiplicity correction. Action labels are model-assigned without human validation. The phrase “misprices tactics” is therefore a plausible downstream-risk hypothesis, not a measured causal or reinforcement-learning consequence.

## Evidence

The manuscript reports:

- primary Claude simulator: non-buyer mean depth bias `+0.396`, buyer `+0.092`, `Δ=+0.304`, `d=0.38`, one-sided permutation `p=0.0002` on 374 conversations;
- DeepSeek simulator: `Δ=+0.330`, `d=0.41`, `p=0.002` on 200;
- instructed Claude simulator: non-buyer `+0.098`, buyer `-0.187`, `Δ=+0.285`, `d=0.34`, `p=0.008` on 200;
- DeepSeek instrument: `Δ=+0.351`, `d=0.42`, `p=0.015` on 150;
- primary non-buyer resistance declines from 25.1% real to 13.5% simulated and `considering` rises from 21.9% to 40.1%, while `deciding` remains 4.3%;
- binary resistance and deep-funnel alternative codings preserve a positive contrast;
- the reported positional contrast grows from `+0.054` at 30% to `+0.706` at 90%; and
- after pitch-labeled actions, `considering` is 45.3% for real turns and 75.2% for simulated turns in the selected probe analysis (pp. 7–10, 16–18).

These are coherent manuscript-level sensitivity checks around one corpus. They are not cross-population replication: the simulator and judge swaps reuse the same underlying production source, likely overlapping conversations, the same outcome definition, the same probe design, and related LLM-based state ontology. The temporal gradient is consistent with accumulated disengagement but is also mechanically entangled with relative-position selection, realized conversation length, and future survival.

## Unique insight

> **A synthetic participant needs an observable-state sufficiency test as well as an outcome-conditioned fidelity test.**

The paper usefully proves that marginal human-likeness can hide consequence-correlated errors. The missing companion is to determine whether the simulator was given enough legitimate information to reproduce the relevant decision state. `skill-bench` should represent:

```text
population / participant unit
→ real stakes and outcome observation window
→ authorized observable context at decision time
→ latent-state target and its independent evidence
→ simulator identity, evidence view, policy, and stopping semantics
→ one-step and free-running transition behavior
→ outcome-stratified discrepancy
→ agent-policy interaction effect
→ realized consequence and claim ceiling
```

This separates five fidelities that should never be collapsed:

1. **communicative fidelity:** style, pacing, disclosure, affect, and language;
2. **assigned-goal fidelity:** consistency with a benchmark-authored objective;
3. **state-transition fidelity:** movement among uncertainty, resistance, commitment, revision, and exit under matched observable history;
4. **decision fidelity:** calibrated choice/stopping behavior across a real target population under real or validated stakes;
5. **consequence fidelity:** whether agent policies selected or trained under simulation preserve ranking, effects, harms, burden, and outcomes with real participants.

A sixth prerequisite is **information sufficiency**: can the allowed evidence identify the state the benchmark expects the simulator to reproduce? If not, the valid construct may be population-level stochastic response rather than person-specific simulation. A benchmark must not grade a simulator for failing to know a hidden future, nor certify it merely because an outcome-bearing profile makes the future easy to predict.

## Comparison with adjacent skill-bench evidence

- **HAS-Bench** types participant roles, permissions, channels, and authority, but its main “human” participants are simulators. This paper adds direct outcome-conditioned behavioral evidence that simulator realization can change the construct even when channel structure is fixed. HAS-Bench still needs matched real-participant behavior, burden, and effects.
- **DeskCraft** exposes authored interaction opportunity, trigger, message, adoption, state repair, endpoint, burden, and consequence as separate links. The present paper adds that the participant's *stopping and willingness transition* must be validated; a simulator that always supplies the next authored phase cannot model exit.
- **UniClawBench** implements a role-separated evaluator-to-simulator repair channel. Its simulator renders benchmark feedback rather than a natural user's endogenous willingness. Outcome-conditioned fidelity and semantic-leakage audits are different requirements: one tests participant behavior, the other tests information content.
- **SovereignPA-Bench** separates current intent, memory, third-party pressure, evidence, consent, and burden. That decomposition is needed here because payment does not by itself reveal current intent, permission, or the private cause of stopping.
- **MapSatisfyBench** uses later behavior to nominate hidden factors but must separate hindsight, prediction, current applicability, authority, and acceptance. This paper similarly uses eventual payment to stratify probe error; future outcome is valid evaluation evidence, not automatically agent-visible or simulator-identifying state.
- **Participation-treatment and interaction-evidence synthesis** already separates participant realization, availability, exercise, uptake, effect, and burden. The new nonduplicate link is simulator decision-state/outcome validity plus observable-state sufficiency before treating an interaction treatment as a model of people.

## Limitations and validity threats

1. One production domain, platform, language, product, cultural context, and parent-mediated decision process.
2. No source-frame dates, market coverage, price regimes, production-agent version history, or population sampling weights.
3. “Non-converted” observation window and censoring policy are unspecified.
4. Later/off-platform/canceled/refunded/duplicate payment handling is unspecified.
5. Customer-to-conversation and conversation-to-order cardinality are unspecified; customer clustering is absent.
6. Experimental-panel eligibility, random selection, seeds, overlap, attrition, and size differences are unexplained.
7. Missing profiles, failed joins, malformed model outputs, timeouts, retries, and invalid trials have no ledger.
8. Probe locations depend on completed real-conversation length and therefore future information/survival.
9. Teacher forcing measures one-step responses, not free-running dialogue state, stopping, silence, or agent adaptation.
10. The simulator receives demographic profile but not real private motivation, constraints, competing options, or future outcome.
11. Future-outcome stratification conflates behavioral-support, state-inference, and unobserved-information gaps.
12. The claim that the model lacks a behavioral mode rather than information is not identified.
13. Eventual payment is a coarse proxy for latent willingness and may reflect unobserved factors after the probe.
14. Outcome-conditioned mean bias is not the paper's stronger distributional equality definition.
15. `Δ=0` is insufficient for fidelity and can hide equal bias, wrong variance, random assignment, timing error, or compensating categories.
16. Buyer mean bias near zero does not establish paired or distributional fidelity; buyer `considering` still shifts materially.
17. “No fabricated purchases” refers to an LLM-assigned `deciding` stage on one next turn, not completed simulated payment behavior.
18. The ordinal depth scale assumes ordered/equal increments; binary sensitivity helps but does not validate state labels.
19. No human annotation validates stages, emotions, blockers, action labels, or source-style effects.
20. Same-instrument subtraction cancels only restricted shared bias forms, not arbitrary source- and outcome-dependent error.
21. Cross-family LLM judging demonstrates model robustness, not criterion truth or human reliability.
22. Primary Claude model endpoint, exact Chinese prompts, decoding, dates, seeds, retries, and fallback behavior are absent.
23. Robustness panels reuse one corpus and are not independent cross-population replications.
24. Conversation-level aggregation does not address customer, template, agent-version, calendar, or panel-overlap dependence.
25. Permutation exchangeability is questionable when outcome strata differ in profiles, histories, duration, and treatment path.
26. Bootstrap method/unit and multiplicity policy are unspecified.
27. The action-conditioned analysis uses observational agent actions and cannot identify tactic effects.
28. Fisher exact tests ignore real/sim pairing and repeated probes within conversations.
29. Action categories and the 595-probe subset are not independently validated or fully explained.
30. No free-running or agent-policy experiment shows changed task score, policy ranking, training signal, revenue, harm, or quitting behavior.
31. No retrieval-grounded, fine-tuned, replay, non-LLM, or externally gated willingness simulator is tested.
32. No negative control checks a context variable unrelated to willingness or a consequence where engagement should not decay.
33. Release claims have no artifact locator; analysis, prompts, derived statistics, and extraction code cannot be inspected.
34. Raw conversation and payment evidence cannot be audited; privacy can justify this but remains an evidence limitation.
35. Platform authorization and terms do not document individual research consent, ethics review, external-model data flow, or demographic-inference permission.
36. Single-author analysis and unreleased code/data increase undetectable specification and reporting risk.
37. The causal explanation from instruction tuning is plausible but untested.
38. Cross-domain transport from matchmaking sales to fundraising, negotiation, support, or knowledge-work collaboration is unsupported.
39. No evidence licenses production-agent quality, professional validity, safety, deployment fitness, or readiness claims.

## Reproducibility and operational realism

**Conceptual reproducibility is moderate.** The paper defines the probe protocol, state schema, depth codings, estimand, sampling positions, permutation count, principal prompts in translated summary form, extraction logic, and aggregate tables. Another group with outcome-linked dialogue could implement a related study.

**Exact reproducibility is low.** The claimed release is unlocatable; raw data are private; exact prompts/model endpoints, sample IDs, seeds, response cache, invalid ledger, state/action annotations, derived table, and analysis code are unavailable. Neither results nor corpus linkage can be independently recomputed.

**Operational realism is high at stakes/provenance and low-to-moderate at evaluated interaction.** Real customers, real sales dialogue, and verified payments are unusually consequential evidence. But the administered test is an offline one-turn counterfactual using a model-assigned state, not an agent interacting with a free-running person or simulator. It observes neither simulator-driven stopping nor resulting agent policy/consequence. The source is therefore best treated as a strong **falsification of marginal/assigned-goal simulator validation**, not as a validated simulator benchmark or production agent evaluation.

## Transfer to skill-bench

### Retain

1. **Use real consequential outcomes where ethically and operationally feasible.** Role-play and fluency cannot validate endogenous commitment or withdrawal.
2. **Hold observable history fixed for local simulator audits.** Same-prefix probes isolate one-step participant response from accumulated agent divergence.
3. **Report outcome-stratified errors as well as marginals.** Aggregate realism can hide concentrated errors in failure, refusal, harmed, burdened, or non-adopting groups.
4. **Preserve stopping and silence.** Non-response, withdrawal, deferment, refusal, escalation, and revocation are first-class terminal/transition states, not malformed interaction.
5. **Keep simulator and observer swaps.** They are useful sensitivity analyses when clearly bounded below human or consequential validation.
6. **Use noncompensatory claim ceilings.** A simulator may pass communication tests while failing state-transition, decision, consequence, authority, or burden validity.

### Repair

1. **Add an observable-state sufficiency audit.** For each expected participant state, document what evidence was available to the real participant, simulator, agent, and evaluator; test whether independent humans/models can infer the state from the allowed view before requiring person-specific reproduction.
2. **Separate population from person fidelity.** Estimate calibration/distributional distance for `P(response/state | authorized observable context)` and separately test any claim of reproducing a particular person's latent trajectory.
3. **Use matched latent-signal interventions.** Hold history text fixed while varying independently validated willingness evidence; include positive, negative, ambiguous, stale, and unobservable-state cases. Cross simulator policy (`persona`, `disengagement license`, calibrated external state, replay) with state evidence.
4. **Add free-running conditions.** Compare one-step teacher forcing with bounded rollouts that preserve stop/non-response, agent adaptation, state persistence, and terminal outcomes. Record divergence and invalidity rather than assuming compounding direction.
5. **Measure policy transport directly.** On safely consented or inert tasks, compare agent-policy rankings and tactic effects under simulator versus real/replay participants. Do not infer policy effect from response-category differences alone.
6. **Version participant realization.** Pin model, prompt, profile/state, sampling, timeout, non-response semantics, retries, and fallback; distinguish model simulator, scripted state machine, replay, consented human, and hybrid.
7. **Use plural state metrics.** Report transition matrices, paired agreement, distributional/calibration distances, timing, stopping hazards, error severity, and group-wise differences—not one mean-depth contrast.
8. **Model hierarchy and censoring.** Preserve participant/customer, conversation, probe, agent version, calendar/product cohort, payment follow-up window, missing joins, and repeated panels; use dependence-aware uncertainty.
9. **Validate state/action labels.** Use blinded human labels with identical evidence views, disagreement/adjudication, abstention, source-style checks, and criterion-level errors.
10. **Keep consequence, authority, and privacy separate.** A payment-linked record strengthens outcome evidence but does not automatically authorize demographic simulation or establish the cause, legitimacy, or user benefit of the decision.

## Concrete repository actions

No new build task is added. Existing participant-realization, interaction-evidence, configured-system, trace, metric, task-health, validity, participation/consent, and longitudinal contracts can host the requirements. The evidence changes canonical synthesis by adding one missing gate to the interaction ladder:

`participant realization → observable-state sufficiency → one-step transition fidelity → free-running fidelity → agent-policy transport → real consequence`.

For the next simulator-mediated interactive pilot, add a compact cross-domain falsification matrix rather than a simulator-specific schema:

- communicative match versus decision-state match;
- assigned goal versus endogenous/uncertain goal;
- state observable versus intentionally unobservable;
- continue versus legitimate stop/refuse/silence;
- teacher-forced versus free-running;
- no participant signal versus calibrated signal;
- simulator versus replay/consented human where justified;
- marginal versus consequence-stratified reporting.

Useful completion is not a higher simulator score. It is correctly rejecting person-specific fidelity when latent state is unavailable, detecting consequence-correlated stopping errors when it is available, and bounding any simulator-mediated agent result below demonstrated policy transport and real consequence.

## Claim ceiling

The immutable v1 paper supports a consequential methodological warning: on one selected production sales corpus, reported profile-conditioned LLM simulators produce more engagement-positive next-turn states than real users specifically in the eventual non-payment stratum, and a global disengagement instruction can improve the marginal while preserving the stratum contrast. It does not establish that future buyer/non-buyer state was identifiable from the simulator's evidence, that the model rather than missing private information caused the discrepancy, that real users are reproduced distributionally or in free-running dialogue, that pressure tactics causally lose sales, or that simulator-trained/evaluated agent rankings transport to people. For `skill-bench`, communicative, assigned-goal, state-transition, decision, and consequence fidelity—and observable-state sufficiency—must remain separate validity claims.