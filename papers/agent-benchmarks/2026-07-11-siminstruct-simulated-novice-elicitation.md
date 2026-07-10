# Paper Review: Simulated Novices Are Elicitation Treatments, Not Substitute Ground Truth

- **Paper:** https://arxiv.org/abs/2508.04428v2
- **Authors:** Si Chen, Izzy Molnar, Ting Hua, Peiyu Li, Le Huy Khiem, G. Alex Ambrose, Jim Lang, Ronald Metoyer, and Nitesh V. Chawla
- **Date read:** 2026-07-11
- **Venue / source:** immutable arXiv preprint v2; proof-of-concept manuscript
- **Tags:** expertise-elicitation, expert-participation, simulated-users, scaffolding, synthetic-data, persona-effects, reciprocity
- **Local PDF:** `data/papers/pdfs/2508.04428v2-siminstruct-simulated-novice.pdf` (23 pages; SHA-256 `7baa7cd8b249ac50f46beb5191d50a50af83a3a57192fcb9fcf2598f79566348`)
- **Local text:** `data/papers/text/2508.04428v2-siminstruct-simulated-novice.txt` (SHA-256 `ffc46d5253126c0cec315a78a4d858491d659e0da55ed89bdd5c188372dfd554`)
- **Materials boundary:** no paper-linked code, interface, data, consent form, survey, analysis, or supplement URL appears in v2. The PDF embeds the novice prompts, one sample dialogue, two rubrics, and agreement matrices (Appendices A–D, pp. 15–23).

## One-sentence contribution

SimInstruct shows that 18 paid higher-education coaching experts can asynchronously produce 123 multi-turn dialogues with GPT-4-generated novice personas, and that one randomized persona trait changes expert verbosity, but the study measures dialogue form and researcher-rated pedagogical qualities—not whether simulated novices expose tacit decision rules, whether framing or flexibility causes recruitment/retention, or whether the resulting advice survives real novice resistance and implementation.

## Why this matters for skill-bench

This review advances charter objectives B and F through targeted expansion into simulated interlocutors as an expertise-elicitation and reciprocal-participation mechanism. The cross-domain hypothesis is: **a simulated novice can make an expert contribution feel like authentic practice and can systematically vary prompts, but every novice behavior is an elicitation intervention that selects which expertise becomes visible. Its output is candidate evidence until incident grounding, scope, consequence, contributor confirmation, and downstream utility are checked.** Teacher coaching is a methodological case, not a benchmark scope commitment.

The paper differs from Data Therapist, where a model chooses explicit questions about an expert's dataset, and from the 12-week participation ethnography, which tracks authority handoffs under organizational pressure. SimInstruct instead embeds machine choices in a responsive role-play: profile attributes, challenge, initial question, agreement, resistance, detail, and stopping behavior jointly shape the expert's testimony. Its strongest causal evidence—extraversion changing expert word count—therefore warns that the elicitation instrument changes the evidence distribution.

Useful completion is a bounded review that prevents three unsupported inferences: that conversational fluency equals tacit-knowledge capture, that positive comments prove a low-cost recruitment model, or that synthetic privacy avoidance proves ecological validity. No new build task is warranted: the existing expert-participation contract, elicitation template, blocked real-session contract, and Data Therapist event-ledger requirements already provide the implementation homes.

## Research question and claim boundary

The stated research question is: “How effectively does the use of LLM-simulated novices support the generation of high-quality scaffolding dialogues?” (p. 3). The study evaluates this through dialogue statistics, persona–word-count associations, researcher ratings against four recorded coaching sessions, participant feedback, and a downstream fine-tuning comparison (pp. 5–12).

The evidence supports bounded claims that:

- 18 recruited experts completed 123 asynchronous dialogues in two weeks;
- the retained dialogues averaged 15.02 turns and contained substantial expert text;
- among four tested dichotomized traits, high versus low extraversion was associated with about 87 additional expert words in the analyzed subset;
- two researchers rated the synthetic-novice dialogues mostly good/excellent on four authored dimensions, with reported κ = 0.69;
- the four real recordings received higher ratings than the SimInstruct corpus; and
- experts and authors identified excessive novice agreeableness and weak contextual nuance as authenticity problems.

It does not establish capture of tacit expertise, factual or professional correctness of advice, novice learning, implementation success, complete or representative knowledge coverage, reduced expert burden versus alternatives, causal effects of meaningful framing or flexible compensation, recruitment scalability, retention, privacy elimination, or transfer outside one university-centered higher-education coaching network.

## Methodology and system

### Human-centered development and participant frame

Two senior teacher-development experts joined weekly design sessions from January through June 2025 to refine interface, persona generation, and protocol; the July study then ran asynchronously (p. 4). The paper does not report the number or duration of design sessions, how decisions were logged, whether these two later participated or rated data, or which changes they caused.

Eighteen U.S.-based experts with advanced degrees and “extensive coaching experience in higher education” were recruited by email and word of mouth. Expertise has no operational threshold, role distribution, years, task-specific demonstration, institutional diversity, demographics, invitation denominator, refusal count, or attrition account. Participants were paid per completed dialogue using an estimated 5–20 minutes and a $50 hourly rate—roughly $4.17–$16.67 per dialogue by the stated formula—and worked over two weeks (p. 6). The exact total payment, actual time, support time, number assigned/completed per expert, skipped/deleted count, and unpaid survey burden are absent.

The paper states IRB approval (p. 4) but gives no consent procedure, privacy transformation, data retention, downstream training/publication authorization, withdrawal boundary, or handling of potentially identifiable expert text. Replacing real novices removes novice records; it does not make expert contributions non-sensitive.

### Simulated-novice treatment

Each novice combines nine domain-profile attributes, four randomly assigned Big Five traits (neuroticism excluded by author judgment), and one challenge randomly selected from a 40-item expert-authored list. GPT-4 checks profile coherence and generates an initial question; `GPT-4-turbo-preview` produces subsequent replies (pp. 5–6). Exact model snapshots, dates, sampling parameters, seeds, system state, verification prompt, rejection rate, and the full attribute/challenge inventories are unavailable.

The embedded prompts expose substantial treatment design (pp. 15–16). Initial questions must be single, actionable, emotionally honest dilemmas in plain language. Follow-ups must be concise, disclose uncertainty and constraints, ask implementation questions, and may reject one to four suggestions. Yet experts later observed that novices usually agreed and human novices push back more (pp. 11–12). The prompt therefore specifies resistance but the implementation does not reliably realize it.

Experts see only a name and initial question, must elicit missing detail, can delete unrealistic conversations, and decide when a viable strategy exists or the novice seems ready and satisfied (p. 6). This stopping rule is endogenous: a compliant novice can make both the conversation and the expert appear successful earlier. Deleted dialogues and reasons are not reported, so the retained 123 are a selected corpus with an unknown denominator.

Two experts reviewed 30 random profiles before the study and their feedback was incorporated (p. 6). No pre/post profiles, criteria, independent judgments, agreement, defect counts, or held-out realism test are available.

### Dialogue corpus and persona analysis

The retained corpus contains 123 dialogues, 1,848 utterance-level turns, 65,004 novice words, and 38,444 expert words. Mean expert output is 312.55 words (SD 242.41), mean novice output 528.49 (SD 378.40), and mean turns 15.02 (SD 7.77) (p. 6). Authors characterize most dialogues as problem identification → reason exploration → strategy development, but provide no coding protocol, denominator, coder reliability, or item-level labels (pp. 6–7).

For persona effects, records with missing trait values or expert word count ≤100 were removed, leaving 100 of 123 dialogues. Each trait was recoded low/high and fit separately in a linear mixed model with an expert random intercept. Extraversion had Δ = 86.94 words, p = .030; agreeableness, conscientiousness, and openness were null. The authors did not adjust for multiple comparisons because hypotheses were separately theory-motivated (p. 7).

This is the paper's most diagnostic quantitative result but weaker than its rhetoric. Exclusion is outcome-based and removes 23 dialogues; cutpoints, allocation balance, per-expert exposure, challenge/profile covariates, model diagnostics, confidence-interval values, effect uncertainty after four tests, and random slopes are absent. Word count is engagement quantity, not insight, correctness, cognitive depth, or useful primitive yield. Still, randomized persona assignment plausibly shows that simulated behavior changes expert production.

### Comparison with four real coaching sessions

Privacy, scheduling, and recording concerns yielded only four real sessions totaling about 200 minutes over two months (pp. 4–5). These later served as comparison material. The manuscript compares four tool dialogues with those four recordings in prose, yet Figure 9 compares all 123 tool dialogues against four recordings; the exact sampling statement is inconsistent (pp. 7, 21).

Two researchers rated dialogue data using four 1–3 criteria developed by team members with pedagogy/education-research experience: pedagogical relevance, cognitive depth of the simulated question, instructional contextualization, and coverage of concerns. Reported agreement is κ = 0.69, but the statistic's weighting, per-criterion calculation, pooled units, adjudication, and final-score policy are unspecified (pp. 7–8, 21). “Coverage over time” is awkwardly applied to each dialogue and overlaps relevance/context.

The four recorded sessions score 3 on every criterion; SimInstruct averages 2.80 (SD .25). The groups differ in modality (spoken face-to-face versus typed asynchronous), duration, sampling, likely participants, context availability, and only four real sessions. Ratings are not reported as blind. The authors appropriately note that simulated questions can be straightforward and context-poor. “Comparable quality” is therefore an interpretation, not an equivalence test: no margin, confidence interval, matching, or inferential comparison is supplied.

### Synthetic augmentation and model evaluation

The 123 dialogues seed GPT-4o-mini generation: three sampled dialogues condition each new synthetic conversation, malformed outputs are filtered, and the final set has 1,415 dialogues / 9,271 turn examples. Llama-2-7B-chat is fine-tuned for 435 steps on one A100. No held-out split, deduplication, semantic-fidelity audit, expert approval, contamination check, privacy analysis, ablation on expert versus augmented data, or exact generation prompt is reported (pp. 8–9).

Two annotators blind to source rate 220 generated dialogues from fine-tuned LLaMA and GPT-4o on clarity, tone, reflective prompting, and validation. LLaMA means are higher on all criteria, especially reflective prompting (2.67 versus 1.76). Reported pooled quadratic κ is .65 for LLaMA and .53 for GPT (pp. 9, 23). There are no inferential tests, cluster controls, prompt/task construction details, decoding settings, judge expertise basis, per-dialogue paired effects, or comparison to the base LLaMA. Different agreement by model also means score reliability is treatment-dependent. The result is compatible with style imitation from authored criteria and synthetic dialogues; it does not validate the original expert knowledge or prove superiority in novice outcomes.

## Evidence interpretation

### Measured outcomes versus author interpretation

The paper directly measures retained dialogue counts/lengths, one persona association, authored rubric scores, two-rater agreement, and model-response ratings. It also reports qualitative participant impressions, but provides no survey instrument, respondent denominator, response distribution, coding method, quotations beyond one cautionary comment, or negative-case accounting.

Section 5.3.1 asserts that meaningful framing was “key” to recruiting and sustaining engagement and that flexible compensation “contributed to higher engagement and completion rates” (pp. 10–11). Neither variable was randomized, compared, measured, or linked to a denominator. There is no alternative framing, fixed-payment arm, invitation conversion, completion rate, retention measure, baseline, or counterfactual. These are plausible design recommendations and author interpretations—not outcome estimates.

Likewise, autonomy to skip/revise/decline and authentic dialogue may respect professional judgment, but their causal contribution to quality or sustained engagement was not tested. “Co-designer” overstates the disclosed study role for the 18 participants: two senior experts co-designed the tool; the other experts supplied dialogues and optional feedback. Role provenance should remain distinct.

### Simulation does not demonstrate tacit-cue elicitation

The tool elicits advice, follow-up questions, and some reasoning in response to authored teaching challenges. It does not identify cues experts noticed, thresholds for changing strategy, rejected alternatives, expert/novice contrasts, critical incidents, uncertainty calibration, or consequences after implementation. The sample dialogue is dominated by an agreeable novice endorsing survey, assignment choice, and group-work suggestions; it contains little resistance, outcome evidence, or correction (pp. 18–19).

A fluent multi-turn dialogue can therefore expose **articulated coaching behavior** without establishing tacit knowledge. The three-stage structure may partly be induced by the challenge prompt, conversational norms, and completion rule. To promote a statement into a benchmark primitive, `skill-bench` still needs incident/source grounding, applicability, contradiction checks, expert read-back, observable consequences, and validation against plausible alternatives.

### Participation evidence is promising but insufficient

SimInstruct improves over generic labeling in several practical respects: asynchronous work, per-unit payment, scenario deletion, natural professional interaction, and potential reflective value. It also avoids asking vulnerable novices to disclose real problems. These are useful participation hypotheses.

But feasibility is not near-zero cost. Experts were paid at $50/hour, two senior experts contributed six months of weekly design work, the team generated and checked profiles, provided support, rated dialogues, and synthesized data. Recruitment relied on email/word-of-mouth in one professional network. No total cost per retained dialogue, coordination burden, refusal/dropout, return participation, or external recruitment is reported. Meaningful mission framing can also create selection and demand effects: participants sympathetic to AI-in-education may contribute differently from skeptical experts. The sole participant quotation asks that feedback address negative consequences as well as possibilities (p. 10), cautioning against treating mission alignment as endorsement.

### Privacy is displaced, not solved

The design avoids collecting real novices' vulnerable consultations, which is a concrete privacy advantage. But generated profiles can invite experts to reveal real cases or organizational practices; expert text is retained, augmented, used for model training, and rated. The manuscript does not explain whether prompts warn against identifiable disclosures, whether data were de-identified, or whether consent covered synthetic derivation and model training. Ethical burden moves from novice consent to expert contribution governance and simulation validity.

## Unique insight

The deepest insight is that **the simulated novice is an experimental instrument over expert behavior**. The evidence-generation path is:

`expert-authored challenge/profile distribution → model coherence check → generated initial dilemma → model realization of detail/resistance/personality → expert probing/advice → model agreement or pushback → expert stopping/deletion → retained transcript → researcher/synthetic transformation`

Each edge controls which cues, tradeoffs, and procedures become visible. The extraversion result is not just a persona finding; it empirically demonstrates instrument reactivity. A benchmark-authoring workflow must preserve the simulated interlocutor configuration and treat elicited statements as condition-specific observations, not a neutral sample of “the expert's knowledge.”

A second insight is that **productive friction is an elicitation resource**. The authors requested one to four rejected suggestions, yet observed compliant novices. Resistance, conflicting constraints, failed prior attempts, and delayed implementation evidence force experts to expose decision boundaries. Agreeableness produces pleasant, shorter routes to apparent resolution and can systematically omit thresholds, contraindications, and repair strategies—the very primitives a diagnostic benchmark needs.

A third insight is that **reciprocity and measurement can conflict**. A reflective, rewarding interaction may recruit and sustain experts, but a novice optimized to be engaging can bias testimony toward fluent coaching. Participation outcomes and elicitation validity must be measured separately: contributor value, burden, and agency on one side; grounded novelty, contradictions, thresholds, consequences, and downstream checkability on the other.

Finally, replacing scarce real users with simulation changes the construct. It may validly measure how experts respond to a controlled family of presented cases. It cannot by itself establish how experts respond to real users whose misunderstandings, omissions, incentives, emotions, nonverbal cues, and implementation failures are not generated from the benchmark designer's ontology.

## Transfer to skill-bench

### 1. Record simulated interlocutors as elicitation interventions

For any simulated-novice session, preserve:

- challenge source, author/reviewer authority, version, and intended coverage;
- profile attributes, sampling distribution, exclusions, random seed, and assignment;
- full prompts, model snapshot, decoding/tool settings, and response history;
- coherence-check prompt, outcome, retries, and discarded generations;
- resistance/detail/uncertainty behaviors requested and observed;
- expert skips, deletions, revisions, stopping reason, and actual time;
- statement locators tied to the triggering novice utterance; and
- downstream transformations and renewed expert dispositions.

This belongs in the existing elicitation-event and participation lineage, not a new subsystem.

### 2. Add productive-friction probes to the existing session template

After an unprompted critical-incident account, use controlled follow-ups such as:

- the novice rejects the first plausible suggestion for a concrete constraint;
- a prior intervention failed despite apparent compliance;
- evidence contradicts the novice's interpretation;
- two goals cannot both be optimized;
- implementation reveals an adverse effect; and
- the novice asks when *not* to use the proposed strategy.

Label all resulting statements `SIMULATED_PROBED`; do not merge them with spontaneous testimony. Ask the contributor at read-back which cues or boundaries were genuinely representative versus artifacts of the role-play.

### 3. Separate participation and elicitation estimands

A real pilot should report separately:

- invitation → consent → start → completion → return-participation denominators;
- paid and unpaid expert/coordination minutes per retained candidate primitive;
- scenario skip/delete/revision and unrealistic-response rates;
- contributor-rated reciprocal value, reflection, autonomy, and downstream-use comprehension;
- spontaneous versus simulated-probed grounded novelty;
- thresholds, contradictions, contraindications, and failure signatures per hour;
- statements surviving source/incident corroboration and expert read-back; and
- downstream task/check utility on held-out cases.

Do not use dialogue count or word count as an expertise-yield proxy.

### 4. Use matched interlocutor ablations before making mechanism claims

To test whether simulation helps, compare the same qualified contributors or balanced clusters under frozen cases with: static written vignette, neutral simulated novice, friction-seeking simulated novice, and where ethical/feasible a consented real or expert-authored replay. Randomize order, prevent case reuse, model expert clustering, and keep interface/time/compensation fixed. Outcomes should include grounded decision-boundary yield and participant burden—not only length and Likert preference.

### 5. Fail authority closed after augmentation

The 1,415-dialogue corpus is model-derived from 123 expert interactions. Such descendants inherit provenance and authorized purpose, never blanket expert approval. Sampled fidelity review, consent for synthetic derivation, contamination/privacy checks, and claim-specific expert approval are required before using augmented material to author professional requirements, rubrics, or release claims. Existing `schemas/expert-participation.schema.json` already encodes the relevant transformation boundary.

## Limitations and validity threats

1. **Single domain/network.** All participants coach higher-education instructors in the U.S.; recruitment is email/word-of-mouth and likely institutionally proximate.
2. **Coarse expertise evidence.** Advanced degrees and extensive coaching are asserted without role, years, task demonstration, specialization, or coverage boundaries.
3. **Unknown recruitment denominator.** Invitations, refusals, starts, dropouts, return participation, and survey response count are absent.
4. **No participant distribution.** Contributions and outcomes are not reported per expert, so a few prolific experts may dominate 123 dialogues.
5. **No actual burden/cost accounting.** Payment uses estimated 5–20-minute durations; actual time, total cost, support, design, cleanup, and review labor are unavailable.
6. **Framing/flexibility claims are noncausal.** No comparison, manipulation, measured completion rate, or retention outcome supports Section 5.3.1's mechanism claims.
7. **Survey evidence is unreproducible.** Instrument, scale, denominator, item results, coding, and nearly all quotations are absent.
8. **IRB is not downstream-use provenance.** Consent, privacy, retention, public release, augmentation, model-training, and withdrawal terms are undisclosed.
9. **Selected retained corpus.** Experts could delete unrealistic conversations; assigned/generated/deleted counts and reasons are missing.
10. **Mutable model treatment.** GPT-4 and `GPT-4-turbo-preview` lack snapshots, settings, dates, seeds, retry logs, and response archives.
11. **Incomplete persona release.** Full attribute levels, 40 challenges, profiles, coherence prompt, checks, and rejection rates are unavailable.
12. **Outcome-conditioned exclusion.** The persona analysis removes expert word count ≤100 and missing records, reducing 123 dialogues to 100 without sensitivity analysis.
13. **Multiple tests and weak estimand.** Four traits are tested separately without correction; only extraversion reaches p=.030, and word count is not quality.
14. **Under-specified mixed model.** Trait cutpoints, allocation, confidence intervals, random slopes, diagnostics, and challenge/domain covariates are absent.
15. **Pseudo-diversity risk.** Random names/personality/discipline can diversify surface features while the 40 authored challenges bound substantive coverage.
16. **Unreliable resistance manipulation.** The prompt requests rejection, but experts report excessive agreement; realized behavior is not coded or quantified.
17. **Endogenous stopping.** Experts stop when the simulated novice appears ready/satisfied, making compliant model behavior part of the outcome.
18. **Comparator mismatch.** Four spoken face-to-face sessions and typed asynchronous dialogues differ in modality, duration, context, sampling, and nonverbal cues.
19. **Four-versus-123 ambiguity.** The prose says four tool dialogues were compared with four recordings, while Figure 9 labels all 123 tool dialogues.
20. **No equivalence test.** “Comparable” quality rests on descriptive ratings; all real sessions score perfectly and synthetic dialogues score lower.
21. **Potential rater non-blinding.** The paper does not report whether researchers knew data source; rubric developers and evaluators are team members.
22. **Rubric dependence.** Criteria emphasize question form and authored pedagogical norms, overlap conceptually, and do not test advice correctness or outcomes.
23. **Agreement under-specified.** κ=.69 lacks weighting, unit, per-dimension values, raw matrices, adjudication, and uncertainty.
24. **Three-stage structure not reproducible.** No coding procedure or reliability supports the “majority” claim.
25. **No tacit-knowledge measure.** Cues, thresholds, incidents, uncertainty, consequences, expert/novice contrasts, and implementation are not systematically captured.
26. **Synthetic augmentation unaudited.** The 1,415 descendants lack fidelity, duplication, privacy, expert-review, and expert-only-data ablations.
27. **Fine-tuning comparison lacks identification.** No base-LLaMA baseline, matched inference configuration, inferential statistics, held-out data account, or learning-outcome measure.
28. **Treatment-dependent rater reliability.** Separate κ values differ by compared model, but mean differences are interpreted without measurement-error modeling.
29. **No operational release.** Code, UI, raw dialogues, participant materials, profiles, surveys, ratings, and analysis scripts are unavailable.
30. **No real-world consequence evidence.** Neither real novices nor downstream teaching implementations test whether elicited advice is useful, safe, or contextually valid.

## Reproducibility and operational realism

Manuscript-level inspectability is moderate: immutable v2 preserves the complete 23-page paper, exact novice prompts, one conversation, both rubrics, and agreement matrices. The paper discloses corpus totals, model families, compensation basis, study period, a mixed-model formula, and fine-tuning hyperparameters.

Study reproduction is weak. There is no runnable tool; profile/challenge inventory; generated corpus; real recordings; study protocol; consent; survey; event log; model snapshot/configuration; random seed; deletion inventory; raw ratings; analysis code; or augmented dataset. A team could imitate the concept but not replay profile assignment, conversation generation, statistical analysis, qualitative findings, or model comparison.

Operational realism is mixed. The asynchronous interface, per-dialogue payment, deletion autonomy, and real coaching format plausibly reduce scheduling and novice-privacy burdens. The manuscript also honestly records important failure signatures: shallow questions, excessive agreement, missing nonverbal backchannels, fewer turns, and contextual thinness. Yet it omits the labor needed to design 40 challenges, run six months of weekly co-design, support participants, clean dialogues, review deletions, audit model outputs, and govern synthetic reuse. “Scalable” is therefore an architecture claim, not a measured cost or recruitment result.

## Concrete repository actions

1. **Do not create a new contract.** Map simulator configuration, observed behavior, deletion/stopping, and utterance-linked statements into the existing blocked `build-elicitation-session-contract` only after a consented real contribution exercises the template.
2. **Refine the next real-session protocol, not its schema prematurely.** Include an unprompted incident phase followed by disclosed simulated-friction probes; preserve phase labels and contributor read-back.
3. **Use the expert-participation contract for all simulated descendants.** Record compensation, reciprocal output, consent scope, synthetic-derivation authorization, transformation lineage, and post-transformation review.
4. **Treat scenario deletion as evidence.** Retain de-identified rejection reason and generator state where consent permits; unrealistic prompts reveal coverage and validity defects.
5. **Validate elicitation utility downstream.** Count only statements that survive grounding/scope review and produce fair requirements, traps, checks, or counterexamples—not words or dialogues.
6. **Keep participation claims bounded.** Until a measured pilot exists, meaningful framing, flexibility, reflection, and asynchronous role-play remain recruitment hypotheses rather than validated near-zero-cost mechanisms.
7. **Preserve the simulation/real-user construct boundary.** Simulated cases can support controlled task-family coverage; claims about real expert–client work require consented observations, expert-authored critical incidents, or other external validation.

## Action items

- [x] Read and verify the complete immutable arXiv v2 PDF/text.
- [x] Audit embedded prompts, sample dialogue, rubrics, agreement matrices, participant workflow, compensation, persona analysis, real-dialogue comparison, and fine-tuning evaluation.
- [x] Confirm that no paper-linked external materials URL appears in v2 and document the reproducibility boundary.
- [x] Separate measured outcomes from Section 5.3.1 recommendations and author interpretation.
- [x] Compare nonduplicative implications against the Data Therapist and domain-expert participation reviews.
- [x] Add no duplicate build task; findings refine existing participation and elicitation machinery.
- [ ] Exercise simulated-friction probes only with a consented qualified contributor and preserve actual burden, rejection, grounding, and downstream-utility evidence.
