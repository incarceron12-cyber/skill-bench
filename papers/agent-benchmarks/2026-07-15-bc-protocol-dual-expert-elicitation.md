# Paper Review: BC Protocol — Judge-Preferred Dialogue Is Not Yet Validated Expertise Transfer

- **Paper:** Bo Zou and Chao Xu, *BC Protocol: Structured Dual-Expert Dialogue for Eliciting High-Quality Chain-of-Thought Post-Training Data*
- **Primary source:** https://arxiv.org/abs/2605.25549v1 (immutable v1, 25 May 2026)
- **Date read:** 2026-07-15
- **Tags:** expertise-elicitation, dual-expert-dialogue, tacit-knowledge, chain-of-thought, participant-selection, counterfactual-probing, model-judges
- **Local PDF:** `data/papers/pdfs/2605.25549v1-bc-protocol-dual-expert-elicitation.pdf` (44 pages; SHA-256 `c044b0af696d0a8771a702d3ab13d2bc091b49a8d9f8b96eed6fda0f844d6968`)
- **Local text:** `data/papers/text/2605.25549v1-bc-protocol-dual-expert-elicitation.txt` (SHA-256 `ddd1bf5470bca2d6d3f5349abdb3f62e5ee4189c8602bcc73fd86a7c0e4fe22e`)
- **Official arXiv source archive:** `data/papers/source/2605.25549v1-source.tar.gz` (SHA-256 `d8d1c6763d52437783d7230648b00700122fa2abd7b05bfdaa34c9c1bdc92daa`)
- **Review status:** complete full-text and source-package audit. The paper repeatedly refers to supplementary topics, paired JSONL samples, prompts, raw ratings, and aggregate results, but none is in the arXiv PDF or source package. Exact-title/ID searches found no verifiable author-owned GitHub or Hugging Face release.

## One-sentence contribution

The paper articulates a useful mixed-initiative pattern—pair a domain expert with an epistemically vigilant elicitor who probes omitted premises, counterexamples, and counterfactuals—but its only experiment compares 20 post-processed dialogue samples with 20 solo-written samples from the same author-expert and shows chiefly that model judges can recognize and reward dialogue-preserved hesitation; it does not validate the Participant Aptitude Model, selection-over-prescription, capture of actual tacit cognition, substantive correctness, downstream training value, cross-domain transport, or production economics.

## Why this matters for skill-bench

This review advances charter objectives A, B, and F by auditing a direct proposal for turning expert interaction into candidate reasoning material. The general hypothesis worth retaining is: **a prepared but non-peer elicitor can use clarification, premise challenge, rejected alternatives, and counterfactual perturbation to expose decision boundaries that solo expert writing omits.** Narrative fiction is a methodological case, not a domain commitment.

The concrete artifact is a claim-bounded review and comparison against the repository's existing elicitation machinery. It clarifies that six outcomes must remain separate:

1. **elicitation yield:** new propositions, cues, alternatives, thresholds, and caveats per expert-hour;
2. **capture fidelity:** whether the record preserves what the contributor meant;
3. **substantive validity:** whether claims are correct, authorized, scoped, and corroborated;
4. **transformation fidelity:** whether transcription, segmentation, cleanup, and prose/CoT conversion preserve meaning;
5. **benchmark utility:** whether the material yields fair, observable requirements, variants, checks, or failure signatures; and
6. **downstream utility:** whether guidance, training, or evaluation using it improves held-out behavior.

The paper measures none of these directly. Its five model-judge dimensions concern surface properties of a transformed text. Therefore it should refine the next consented pilot, not unblock the blocked elicitation-session contract or license a new subsystem.

## Research question and defensible claim boundary

The paper asks how to systematically elicit high-quality expert chain-of-thought for post-training and whether a structured domain-expert/knowledge-engineer dialogue produces better intrinsic text than solo expert writing (Abstract; Sections 1, 3, and 4, pp. 1–3, 9–27).

The evidence supports bounded claims that:

- the two authors developed a three-stage preparation → voice dialogue → post-processing workflow;
- their single author-pair produced 20 dialogue-derived and 20 solo-written items on paired narrative-fiction topics;
- three named model families assigned much higher **D3 naturalness-of-reasoning-process** ratings to the dialogue-derived texts and higher **D4 information-density** ratings to solo texts;
- D1 completeness and D5 counterfactual density favored dialogue weakly and nonsignificantly, while D2 implicit-premise externalization was essentially equal; and
- the authors report collecting 20 dialogue samples in approximately three hours, including post-processing (Sections 4–5, pp. 23–32).

It does **not** establish that the dialogue reconstructs the expert's actual causal cognition rather than co-constructing a plausible account; that its statements are professionally correct; that a second expert would agree; that participant traits cause quality; that selection outperforms a stronger protocol; that voice causes the result; that the output improves a model; that the method transfers to medicine, law, finance, or engineering; or that it is scalable and cost-effective.

## Methodology and system

### Roles and Participant Aptitude Model

The protocol defines C as the domain expert with crystallized intelligence and B as the knowledge engineer with fluid intelligence. Both are intended to be equal co-explorers rather than interviewer/repository or student/authority. The Participant Aptitude Model assigns six dimensions (Sections 3.2.1–3.2.8, pp. 10–18):

1. truth-seeking epistemic orientation;
2. epistemic vigilance, especially for B;
3. complementary fluid/crystallized intelligence profiles;
4. a calibrated cognitive gap;
5. calibrated ignorance—knowing what one does not know precisely enough to ask informative questions; and
6. complementary framing/deepening preferences.

Sections 3.2.2–3.2.8 classify truth-seeking and epistemic vigilance as hard constraints and the other four as soft pairing optimizers. This is conceptually useful as a candidate role-fit model, but it is not an assessment model in the empirical sense: there are no items, behavioral anchors, assessors, reliability results, thresholds, candidate pool, rejected pairs, or criterion outcomes. The paper acknowledges this on pp. 36–37.

The manuscript also contradicts itself. Section 6.1 calls the “two hard-constraint dimensions” calibrated ignorance and epistemic vigilance (p. 32), and the conclusion calls calibrated ignorance a “non-negotiable hard constraint” (p. 40), while the formal model classifies calibrated ignorance as soft and truth-seeking as hard. A production screen cannot be replicated when its veto dimensions change across sections.

### Selection-over-Prescription and dialogue control

The authors deliberately reject a rigid script. B is expected to notice missing premises, ask follow-ups, challenge the expert's frame, introduce counterexamples, and decide when further inquiry would create rationalization rather than information. The paper names the graduated follow-up/counterexample/counterfactual activity the SNAKE mechanism. B controls termination when perceived “cognitive residual” is exhausted (Sections 3.3–3.3.1, pp. 18–21).

The strongest concrete probe is counterfactual perturbation: change an unstated load-bearing premise and ask C to rerun the judgment. Guidance says to perturb implicit rather than stated premises, wait for natural pauses, limit probes by load-bearing-claim density, and use open or deliberately incomplete “decoy” forms. These are reusable elicitation moves.

But “selection-over-prescription” is an untested comparative claim. The study varies neither participant selection nor process prescription. Both roles are the authors who created the protocol; there are no alternative B/C pairs, screening decisions, scripted-dialogue arm, interviewer-training arm, or cost allocation between selection and protocol design. The very extensive 20-page role theory and facilitation guidance also show that selection and prescription are not cleanly separable.

### Voice and post-processing

The protocol mandates voice on the theory that writing triggers polish and omission, while real-time speech preserves hesitation, correction, trial-and-error, and prosodic cues (Section 3.4, pp. 21–23). Post-processing then transcribes, segments judgment units, filters incomplete or logically gapped fragments, removes small talk and auxiliary questions, and formats coherent reasoning paragraphs while purportedly preserving hesitation and self-correction (Section 3.5, p. 23).

This creates an important unmeasured transformation layer. The paper does not identify who transcribed, segmented, excluded, edited, or summarized; how many source segments were discarded; whether C approved transformed items; whether B's words remain; what “logical gap” criteria were used; or how editors avoided selecting samples that best exemplified the theory. A cleaned text cannot establish live-cognition fidelity without audio-to-text locators and before/after transformations.

### Experiment

The domain is narrative-fiction judgment. Group A contains 20 post-processed B–C voice-dialogue samples; Group B contains 20 solo CoTs written by the same C on the same topics (Sections 4.1–4.2, pp. 23–25). The paired same-expert design usefully controls contributor identity, but the analysis discards that pairing.

The comparison bundles at least four treatments:

- voice versus writing;
- two-person probing versus solo production;
- live interaction versus reflective composition; and
- dialogue-specific post-processing versus direct authored text.

No factorial or matched arm separates them. The manuscript says solo writing was completed before Group A's dialogue was “compiled,” which does not unambiguously say it preceded the dialogue itself; the unreleased topic list and timestamps are needed to audit carryover.

Five 1–5 model-judge dimensions are completeness, implicit-premise externalization, naturalness of reasoning process, information density, and counterfactual density. GPT-4o, Claude Opus 4.5, and Gemini 2.5 Pro each score every item/dimension from `{preamble, cot_body}` with group labels removed, yielding 600 calls. Three ratings are averaged per item/dimension; groups are compared with Mann–Whitney U, Cliff's delta, and Krippendorff's alpha (Sections 4.3–4.4, pp. 25–27).

### Why “blind” judging does not remove treatment recognition

D3's rubric explicitly rewards “trial and error, hesitation, and self-correction,” exactly the features the intervention and post-processing are designed to preserve. Group labels may be absent, but dialogue-derived and solo-written genre is the treatment itself and is plainly inferable from those features. The D3 result is therefore close to a manipulation check or source-format classifier: the post-processed dialogue looks like the rubric's definition of live reasoning. It does not show that the reasoning is true, genuinely causal, expert-equivalent, or useful for learning.

## Evidence and statistical interpretation

### Reported results

Table 1 reports (Section 5.1, pp. 27–28):

| Dimension | Dialogue mean | Solo mean | p | Cliff's delta | Krippendorff alpha |
|---|---:|---:|---:|---:|---:|
| D1 completeness | 2.91 | 2.63 | .256 | +.21 | -.01 |
| D2 implicit premises | 2.85 | 2.88 | .859 | -.04 | +.38 |
| D3 naturalness | 4.80 | 1.30 | 2.4e-8 | +1.00 | -.06 |
| D4 information density | 3.02 | 4.07 | 1.1e-4 | -.73 | -.14 |
| D5 counterfactual density | 1.50 | 1.20 | .101 | +.27 | -.03 |

Two dialogue items are excluded from D4 due to incomplete judge JSON, leaving 18 versus 20. The paper elsewhere says only three Claude calls required up to three retries and the other 597 succeeded first try (p. 26), so the surviving missing outputs and group-specific exclusion need a call-level account.

### What the result actually distinguishes

The robust pattern is a surface tradeoff: dialogue-derived text contains more overt hesitation/revision markers, while solo text is more compressed. That is useful for deciding how to preserve alternative branches in an elicitation record. It is not evidence that one format contains more correct expertise or is better post-training data. The authors' phrase “dead conclusion stacking” assigns low epistemic status to concise expert writing without an external correctness or downstream criterion.

D1, D2, and D5—the dimensions closer to the claimed mechanism of exposing missing reasoning—do not show reliable advantages. The paper reclassifies these nulls as possible “trainable gains” after describing the authors as an untrained baseline. This is a future hypothesis, not support for the current protocol. D2 also exposes criterion invalidity: the authors suspect judges confuse compressed terminology with premise externalization (pp. 30–31).

### Statistical validity threats

1. **Wrong independence structure for the strongest design feature.** Items are matched by topic and contributor, yet the authors use an unpaired Mann–Whitney test. A paired ordinal analysis or within-topic permutation would preserve the design and expose heterogeneous topic effects.
2. **Twenty pairs, not 600 independent evidentiary units.** The 600 calls are repeated ratings across 40 texts, five dimensions, and three fixed model judges. They do not increase participant, pair, topic, or domain replication.
3. **One B–C pair is the participant-level sample.** Item-level significance cannot support generalization over elicitors, experts, pair compatibility, or domains.
4. **No multiplicity policy.** Five dimensions are tested at alpha .05 without a preregistered primary outcome or correction. D3/D4 are large enough to remain notable, but “trends” should not be promoted.
5. **Judge dependence and shared bias.** Cross-vendor models are not independent human validators, may share training data and stylistic preferences, and receive criteria written around the intervention.
6. **Agreement is poor or unidentified.** Four of five alpha values are negative or near zero. Ceiling/floor prevalence can depress alpha, but directional group means do not establish item-level interchangeable measurement. D2's alpha .38 is still below the paper's own stated expectations.
7. **Ordinal-score averaging.** Averaging three 1–5 judgments creates pseudo-continuous values without validating equal intervals or judge calibration.
8. **No item-level release.** Pair effects, order, judge rationales, retry outcomes, missingness, alpha computation, and exact tests cannot be reproduced.
9. **No human substantive review.** Human fatigue is asserted as a reason to avoid human judges, but no sampled expert adjudication tests whether model preferences track factual or professional quality.

### Cost evidence

The paper reports 20 dialogue samples from two 1–1.5-hour sessions, roughly three hours total including post-processing, or about nine minutes per sample (Section 5.6, pp. 31–32). This empirical rate is approximately 6.7 samples/hour, not the abstract/introduction's claimed 10–20 per hour. There are no labor rates, screening costs, preparation time, transcription/tool cost, discarded-fragment denominator, correction/review time, solo-writing time, API judge cost, or participant burden measures.

The near-zero-marginal-cost counterfactual claim is explicitly unvalidated (Section 6.4, pp. 34–36). D5 is low in both arms and nonsignificant; there is no Expert Solo + post-hoc augmentation arm at equivalent counterfactual density. Online probing consumes session time and expert attention, so “no double payment” is not a measured cost result.

## Unique insight

The paper's best transferable insight is narrower and more useful than its post-training rhetoric: **elicitor capability is part of the measurement instrument, and the instrument's highest-value act may be locating the expert's decision boundary rather than asking for more explanation.** A counterfactual that changes an unstated premise can expose which cues are load-bearing, which alternatives were rejected, and where advice stops applying. Those are exactly the primitives needed for fair task variations and diagnostic rubrics.

But this creates a paired danger: **a skilled elicitor can also manufacture apparent reasoning.** The evidence path is:

`topic selection → expert solo account or B-framed dialogue → B's premise choice/challenge → socially co-constructed response → B's stopping decision → transcription → segmentation/filtering/editing → judge rubric → model preference`

Every edge changes what is observed. Hesitation can be genuine retrieval, conversational repair, uncertainty, or performance; a counterfactual answer can reveal a stable policy or induce novel speculation; a coherent rationale can be post-hoc in both solo and dialogue conditions. Calling the output “externalized K” skips the capture-validity problem.

A second insight is that **selection and protocol should be treated as separable interventions even if both matter.** The paper turns non-procedural elicitor skill into a reason not to standardize. For benchmarking, the safer response is to preserve practitioner discretion while logging enough behavior to audit it: exact probes, targeted premise, response, revisions, stopping reason, and downstream yield. Standardizing the record is not the same as scripting the conversation.

A third insight is that **naturalness, completeness, density, and truth can move independently.** Dialogue can be more visibly exploratory yet less concise; solo prose can be compressed yet correct; either can omit a decisive cue. `skill-bench` should not optimize one scalar “CoT quality” score. It should test claim-level provenance and consequence.

Finally, the paper's mutual-information language is illustrative, not a formal result. The latent expert knowledge K is neither observed nor defined as a random variable; no Q/K distribution, entropy, mutual information, or residual is estimated. The equations cannot establish that calibrated ignorance maximizes information or that stopping reaches zero residual.

## Comparison with existing skill-bench evidence

### Data Therapist

Data Therapist makes model-generated questions and prior annotations explicit elicitation treatments; BC instead places treatment selection in a human B's tacit vigilance. Both can anchor attention and create path dependence. Data Therapist's lesson remains applicable: preserve candidate-question origin, display/order, answer/rejection/revision, and parent context. BC adds premise-target and stopping-decision provenance. Neither establishes truth from conversational yield.

### SimInstruct

SimInstruct experimentally shows that interlocutor traits change expert verbosity and that compliant simulated novices can suppress productive friction. BC's human elicitor plausibly supplies more adaptive friction, but its single pair and missing transcript prevent testing this. Both methods should label prompted material by intervention and measure thresholds/contraindications surviving read-back, not words or judge preference.

### Laboratory workflow twins

The workflow-twin review supplies the missing authority boundary: a contributor may be authoritative about one layer and unauthorized about another, and transformation into a graph/task does not inherit approval. BC's equal co-explorer relation is psychosocially useful but must not erase decision rights. B may identify gaps and propose counterfactuals; C remains the source for bounded domain claims, while corroboration and independent review remain separate.

### Existing session template and participation contract

`templates/expertise-elicitation-session.md` already contains uninterrupted recall, exact probes, incident timelines, rejected alternatives, counterfactual variations, read-back, evidence labels, contradiction handling, transformation review, yield, and burden. `schemas/EXPERT_PARTICIPATION.md` already prevents transformations from inheriting expert authority. BC therefore implies refinements to session execution and later event logging, not a parallel contract.

## Limitations and validity threats

1. **One author-pair, one domain.** The only B and C are protocol inventors; there is no population evidence.
2. **Participant selection is unaudited.** Expertise, performance basis, relationship history, conflicts, and aptitude assessments are not independently documented.
3. **Aptitude dimensions are unmeasured.** No instrument, threshold, assessor reliability, pairing comparison, or criterion validation exists.
4. **Hard/soft constraint contradiction.** Calibrated ignorance changes from soft to hard across Sections 3.2, 6.1, and 7.
5. **Selection-over-prescription is not tested.** No selection or prescription intervention varies.
6. **Treatment bundle.** Voice, interlocutor, adaptive probing, real-time production, and post-processing all differ from solo writing.
7. **No voice-only or text-dialogue controls.** The claim that text “must never” be used is unsupported by the design.
8. **Potential order/carryover ambiguity.** “Solo before dialogue compiled” does not clearly establish solo before dialogue conducted; timestamps/topics are unavailable.
9. **Topic/sample selection unknown.** No sampling frame, inclusion/exclusion log, difficulty balance, or complete topic list is public.
10. **Post-processing selection bias.** Fragment filtering and cleanup lack operators, rules, counts, versions, and expert approvals.
11. **No capture-fidelity criterion.** Natural-looking revision is not evidence that text reconstructs the cognition used in the original decision.
12. **Social co-construction.** B's framing, decoys, and counterfactuals can create reasoning that C had not previously used.
13. **No substantive correctness.** Creative judgment has no unique answer, and no independent expert checks premises, examples, or professional legitimacy.
14. **Rubric-treatment circularity.** D3 rewards exactly the dialogue markers the method preserves.
15. **Blinding is superficial.** Source genre is recognizable even when group labels are absent.
16. **Poor cross-judge reliability.** Four alpha values are negative/near zero; the paper's ceiling explanation does not validate item-level measurement.
17. **Unpaired analysis of paired items.** The test ignores topic matching and supplies no pair-level effects.
18. **Pseudoreplication rhetoric.** 600 calls obscure 20 topic pairs and one human pair.
19. **No multiple-testing correction or preregistered primary outcome.** Directional nulls are interpreted through a postulated trainable-gains layer.
20. **Group-specific missingness.** Two dialogue D4 outputs are dropped without raw call/retry evidence or sensitivity analysis.
21. **Model identity/replay gaps.** Exact snapshots, dates, temperatures, seeds, proxy behavior, prompt text, and parser code are absent.
22. **No human criterion baseline.** Cross-vendor agreement cannot establish absence of shared stylistic bias.
23. **No downstream model evidence.** The paper explicitly defers fine-tuning; “directly usable” and “trainable value” are not demonstrated here.
24. **Genre lock-in is preliminary companion-paper evidence.** It is disclosed without released experiment and shows that surface format can dominate learned behavior.
25. **Counterfactual-density metric is unvalidated.** Load-bearing-claim detection, denominator reliability, domain transport, and relation to outcomes are unknown.
26. **Cost claim is incomplete and internally strained.** Observed throughput is about 6.7/hour, below the claimed 10–20/hour, with key costs omitted.
27. **No burden, safety, or governance evidence.** Consent, allowed training/publication use, compensation, withdrawal, privacy, fatigue, and reciprocal value are absent.
28. **No cross-domain evidence.** Medicine, law, finance, and engineering are proposals, not tested transfer.
29. **Information-theoretic account is metaphorical.** No latent knowledge or information quantity is operationalized.
30. **Missing claimed supplements.** The arXiv source archive contains only `main.tex`, three figure PDFs, and `00README.json`; it omits the stated JSONL groups, topic list, prompts, raw ratings, aggregate results, analysis, audio, and code.

## Reproducibility and operational realism

Manuscript-level inspectability is moderate. The immutable PDF gives role theory, facilitation guidance, five rubric anchors, model-family labels, top-line statistics, and cost prose. The complete arXiv source package allows an exact audit of what was submitted.

Study reproducibility is weak. Despite repeated “supplementary” references, the source archive has no supplement. No raw audio/transcript, paired items, topic list, exact judge prompts, API dates/settings, responses/rationales, retry/missingness records, code, statistics, post-processing log, or consent materials are released. Exact-title/ID searches found only arXiv/aggregator and author-organization pages, not an author-owned study release. An independent team can imitate the protocol but cannot verify a single item-level score or replay the analysis.

Operational realism is also weak-to-mixed. Voice dialogue, flexible questioning, and a small number of expert hours are plausible authoring practices. The paper acknowledges a difficult stopping judgment, unstandardized pairing, genre lock-in, and manual post-processing. But those are precisely the labor- and validity-critical components omitted from cost and release evidence. A pipeline whose quality rests on selecting rare practitioners cannot claim scalable deployment without recruitment yield, assessor reliability, pair failure rates, training, compensation, retention, transformation QA, and downstream acceptance evidence.

## Transfer to skill-bench

### Retain

- Equal co-exploration rather than passive expert extraction.
- A prepared elicitor who understands enough to detect skipped steps but is not so embedded that all premises feel obvious.
- Premise-level clarification, counterexamples, rejected alternatives, and counterfactual perturbations at consequential decision points.
- Expert-controlled corrections and visible uncertainty rather than polished-answer pressure.
- Stopping as an explicit recorded judgment rather than a hidden session artifact.

### Repair before use

- Treat B/C role fit as a hypothesis with behavioral evidence, not personality labels or one-veto intuition.
- Preserve unprompted recall before B imposes frames, then label every intervention and response.
- Record the exact premise B thought was omitted, why it was probed, C's response, correction, and whether C says the branch reflects prior practice or new speculation.
- Keep raw audio/transcript immutable; represent segmentation, deletion, cleanup, and prose/CoT conversion as reviewable transformations with locators and hashes.
- Separate contributor capture approval from corroboration, scope validity, transformation fidelity, benchmark utility, and release authority.
- Compare matched elicitation conditions using contributor/topic clusters and paired analyses; do not count repeated judge calls as independent expertise samples.
- Validate candidate primitives on held-out task variants and expert review before calling them transferred expertise.

### Bounded pilot implication

When the already-requested consented micro-pilot occurs, add a **BC-inspired phase after uninterrupted incident recall**, not before it. At one or two verified turning points, the interviewer should:

1. identify an apparently omitted premise and record that analyst hypothesis;
2. ask one clarification or counterexample;
3. use one disclosed counterfactual only if it tests a load-bearing decision boundary;
4. ask whether the response describes actual prior reasoning, retrospective explanation, or new speculation;
5. read back the resulting cue/threshold/caveat; and
6. measure whether it yields a corroborated, observable candidate primitive without excessive burden.

Useful completion would be evidence that the phase produces at least one additional incident-grounded decision boundary or valid counterexample that survives contributor correction and downstream transformation review. A longer or more natural-sounding transcript is not sufficient.

## Concrete repository actions

1. **Do not add a new schema or build task.** The blocked `build-elicitation-session-contract`, existing participation contract, expertise-transfer schema, and session template already hold the necessary objects; their real-session prerequisite remains unmet.
2. **Refine execution of the future consented session.** Preserve an unprompted baseline, then log BC-inspired premise/counterfactual interventions, stopping decisions, actual time, corrections, and accepted observable primitives.
3. **Keep participant-selection claims provisional.** Record task-specific authority and behavioral elicitation evidence; do not operationalize “fluid intelligence,” truth-seeking, or calibrated ignorance as veto labels without validated assessment.
4. **Require downstream and substantive validation.** Neither model-judge naturalness nor dialogue form can approve a requirement, private check, procedural skill, or training artifact.
5. **No duplicate queue task added.** The evidence sharpens an already blocked human-validation path rather than justifying more synthetic machinery.

## Bottom line

BC Protocol contributes a valuable elicitation move: use a cognitively adjacent, skeptical collaborator to locate omitted premises and test decision boundaries. Its experiment, however, demonstrates that model judges strongly distinguish dialogue-like exploratory prose from compressed solo prose—not that the dialogue captures true tacit expertise or produces useful post-training data. For `skill-bench`, the right transfer is a logged, consented, claim-level intervention inside the existing incident-based workflow, followed by capture, corroboration, transformation, and benchmark-utility gates. The wrong transfer is a “natural CoT” score or an unvalidated personality screen standing in for expertise validity.
