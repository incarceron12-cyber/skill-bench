# KINA: elegant proxy and tournament theorems do not validate the realized coverage or incentive system

- **Paper:** Sheng Jin et al., *Knowledge Index of Noah's Ark*, arXiv:2606.05104v2, <https://arxiv.org/abs/2606.05104v2>
- **Date read:** 2026-07-16
- **Status:** deep review of the complete immutable v2 paper plus release audit
- **Local PDF:** `data/papers/pdfs/2606.05104v2-kina.pdf` (46 pages; SHA-256 `aacf3c07ee155a728a546637de7258701149a59acc4ce5bd540c26c6db1a8c69`)
- **Local text:** `data/papers/text/2606.05104v2-kina.txt` (complete layout extraction; SHA-256 `eefa83faee7dfae9b3d4b7a946ab09a0f818d7b33adb7cb268c3d506a67c9b33`)
- **Official dataset:** `data/sources/releases/2606.05104v2-kina/KINA-hf-06868ee42583bf953adc980e1f49b6af5e6938c6.json` (899 rows; SHA-256 `23481c90f80017944b95e833aa71486a2fac3818aef6b312c78eaa10aaa6e284`)
- **Official code:** `data/sources/releases/2606.05104v2-kina/2077AI-KINA-69a97f3.zip`, linked by the paper-linked dataset and pinned to commit `69a97f305af11d0001854d3392b8410f92fbaae3` (SHA-256 `66fc6d39181e3bb53e4cb469f6632f065672c3a907b525a2aae77d8797d8b8dd`)
- **Release provenance:** `data/sources/releases/2606.05104v2-kina/provenance.json`

## One-sentence contribution

KINA contributes two unusually explicit benchmark-construction ideas—submodular coverage of expert-elicited disciplinary anchors and a bonus-on-bar reviewer tournament—but the theorems apply to idealized proxy and payment systems whose anchors, scores, costs, assignments, payments, audits, and candidate histories are unreleased, while the observed tournament contrast changes both pay and audit regime and the public 899-item release does not conform to several paper-level coverage, source, licensing, and holdout claims.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, and F through a bounded study of how expert coverage judgments and reviewer incentives might become benchmark machinery. The reusable question is not whether `skill-bench` should adopt disciplinary MCQs. It is whether formal guarantees can discipline a cross-domain task-selection and expert-review process without laundering assumptions about expert authority, population coverage, effort, or item validity into stronger claims.

The concrete evidence is the complete 46-page primary source, including proofs, manuals, prompts, taxonomy, experiment appendix, and datasheet, checked against all 899 released items and the complete pinned 11-file code release. This is expansion and human learning, not a scope commitment to knowledge exams. Useful completion means retaining the formal separation between a selection objective and its optimization guarantee, and between a payment rule and its behavioral assumptions, while requiring evidence that the implemented objects and treatment actually instantiate them.

## Research question and claim ladder

KINA asks how a compact knowledge benchmark can address three weaknesses at once (abstract; §§1–3, pp. 1–4):

1. select items for disciplinary coverage rather than availability or difficulty alone;
2. make costly reviewer effort privately worthwhile rather than paying a flat rate that allegedly permits “lazy consensus”;
3. expose whether model rankings survive a bounded test budget.

The paper reports 899 ten-option items, 12 top-level disciplines, 70 fields, and 261 fine-grained subfields. It evaluates 42 models from 13 labs using four calls per item, and evaluates five configured systems with provider-native web search. The strongest reported direct score is 53.17%.

The valid claim ladder is narrower than the paper's integrated story:

- **Mathematical:** the stated max-coverage objective is monotone submodular under nonnegative fixed support scores; cardinality-only greedy selection approximates that objective.
- **Mechanism-theoretic:** under effort-induced first-order stochastic dominance (FOSD), independent score noise/types, positive minimum winning-probability gain, and a mechanism-invariant monotone release aggregator, sufficiently large tournament bonuses expand the set of reviewer types for whom high effort pays.
- **Realization:** the actual anchor elicitation, calibration, constrained selection, review scoring, bonus, audit, penalty, appeal, and refinement system must match those mathematical objects.
- **Empirical:** a treatment comparison must isolate the tournament from audit, time, reviewer composition, task composition, learning, and selection changes, and must observe an independent quality outcome.
- **Validity/use:** accepted MCQs must support declared coverage and model-comparison interpretations; neither theorem establishes realistic knowledge work, professional competence, contributor welfare, certification, or deployment readiness.

KINA provides the first two as conditional arguments. Its released evidence is insufficient for the latter three.

## Methodology and system reconstruction

### Coverage proxy and constrained selection

For each domain `d`, experts provide a prototype containing methods, problems, theorems, concepts, and applications plus a small anchor set. An LLM produces a structured signature for each candidate and scores item alignment. Small expert-labeled item and pair sets calibrate alignment, shared-support, and near-duplicate models. Sparse nearest-neighbor comparisons plus anchor comparisons yield support scores. The final objective sums, over weighted reference-bank anchors, the maximum support offered by any selected item (§3.1, pp. 3–4; Appendix B, pp. 16–18).

That max-coverage objective is straightforwardly monotone submodular. Proposition 1's proof correctly reduces it to a nonnegative weighted sum of per-anchor maximum functions. Under a pure cardinality constraint, standard greedy therefore obtains the familiar `(1 - 1/e)` approximation.

The implemented problem is not the theorem's cardinality-only problem. KINA adds lower/upper stratum quotas and pairwise duplicate constraints. Appendix B says feasibility is not guaranteed, uses “greedy-with-repair” or a small mixed-integer program, and explicitly disclaims a general approximation guarantee under the full constraint set (p. 18). Bootstrap lower quantiles are called robustness summaries, not confidence bounds. A “typical domain” reportedly uses two experts for about ten total hours, 120–160 item labels, 60–80 pair labels, and 25–30% overlap; total KINA spend is approximately USD 100,000. “Domain,” expert counts, total labor, and the mapping from these typical quantities to 70 fields or 261 claimed subfields are not specified.

### Authoring and four-stage quality process

Candidates undergo (§4, pp. 4–5; Appendix E, pp. 28–39):

1. rule checks for cosine similarity below 0.8, unique options, Markdown/LaTeX rendering, and failure by at least three of five flagship models;
2. double-blind review by two screened reviewers under the tournament;
3. three-LLM feature/failure analysis and majority admission;
4. a GPT-5.2-Pro diagnosis/refinement loop with human re-review for flagged items.

Reviewers are described as graduate students at top-tier universities or senior industry experts. Screening asks for academic background, authoritative sources, a 3–6-question coverage plan, willingness to revise, responsibility attribution, and rule comprehension. The last two “stress tolerance” questions reward applicants for accepting the process and blaming their own understanding rather than the standard; they measure compliance orientation as well as expertise and could select against legitimate critical disagreement (Appendix E.1, pp. 28–29).

The annotation manual requires self-contained, source-grounded, representative questions; at least six statements for pseudo-MCQs; ten non-subset options; and explanations for all distractors. Reviewers check alignment, factuality, source authority, logic, option structure, and rendering. Appeals go to re-evaluation or a Core Committee. Repeated superficial approval can lead to removal and compensation forfeiture. Approximately one-third of accepted items reportedly required refinement.

### Tournament mechanism and proof

Two reviewers choose low or high effort. Each receives base payment; only the reviewer with the higher noisy validated score receives bonus `B`, and only if the winning score crosses bar `τ` (Appendix C, pp. 18–21). The key assumptions are:

- high effort FOSD-improves latent review quality;
- a strictly increasing transform of latent quality plus iid continuous noise forms the score;
- qualities, noise, and iid continuous reviewer cost types are independent;
- the minimum high-versus-low effort gain in winning probability, `Δp_min`, is positive;
- released quality is a coordinatewise nondecreasing function of the two reviews and mechanism-invariant independent factors.

For cost type `κ`, tournament effort gains `B Δp - κ`; flat payment yields `-κ`. Thus types below `B Δp_min` choose high effort regardless of opponent action. FOSD then propagates from the larger high-effort mixture to a monotone release aggregator. The appendix also gives expected bonus expenditure and a reduced-form whitelist continuation value.

This is a comparative sufficient-condition result, not truthfulness or a full repeated-game equilibrium. The paper says so. But its actual system adds stochastic audits, joint penalties, removals, appeals, discipline-specific scarcity pricing, work-in-progress limits, and a whitelist. Those change payoff, dependence, participation, and release processes. They are not the theorem's mechanism-invariant residual.

### Empirical tournament comparison

Table 5 compares the first approximately 1,000 submitted items under flat payment **without audit** to a later tournament phase **with bonus and audit** (§5.3, pp. 7–8). Reported caught-flaw rate rises from 0.41 to 0.58, asymmetric catch rate falls from 0.49 to 0.32, and post-approval audit-flagged rate falls from 0.087 to 0.034. The authors appropriately label this observational and note time and reviewer-pool confounding.

The contrast is even less diagnostic than that caveat suggests. Audit is both an incentive and a measurement process, and only the later phase is described as having it. The theorem requires the other release factor `Z` to be mechanism-invariant; the empirical implementation deliberately violates that condition. “Caught-flaw rate” can rise because standards, item mix, reviewer learning, logging, revision policy, or audit threat changed. “Reviewer-asymmetric catch rate” falling does not identify greater effort: correlated omissions, shared standards, easier-to-detect flaws, or fewer total flaws could also reduce asymmetry. No phase denominators beyond the approximate first 1,000 submissions, uncertainty, task/reviewer clusters, score distributions, payment events, audit sample counts, or independent final-item quality measurements are provided.

### Model evaluation and rank thinning

The paper reports AVG@4 at default temperature, 32K maximum new tokens, and 16K/medium reasoning budget (§5; Appendix F, pp. 39–44). Table 13 gives across-call standard deviations, but raw responses, item-level outcomes, API dates, exact model snapshots for all providers, invalid-output rules, and analysis code are absent.

The “bootstrap” stability study actually draws stratified subsamples of 50%, 70%, or 90% of the same 899 released items for 1,000 replications, recomputes the already selected top-ten ranking, and compares it with the full-set ranking. It reports Kendall tau of 0.89/0.93/0.97 and rank-one retention of 0.94/0.98/1.00. This is useful **internal thinning stability conditional on this released set and these model outcomes**. It is not uncertainty over anchor elicitation, candidate selection, future equivalent forms, repeated model calls, provider drift, or the disciplinary item population. Restricting to the full-sample top ten also omits entry/exit instability at the top-ten boundary. The asserted roughly two-point 95% resolution threshold is not accompanied by a pairwise method or interval table.

Five native-web configured systems gain 1.50–5.17 points with unlimited turns. Search providers, indices, policies, query counts, dates, result exposure, contamination, and costs are unmatched. The paper correctly limits this to integrated-system effectiveness, but its proposed “two distinct retrieval functions” is post-hoc speculation, not mechanism identification.

## Evidence and release audit

### What the release supports

The pinned Hugging Face JSON parses as 899 rows with unique integer IDs 0–898, ten A–J options per row, one keyed answer, nonempty option explanations, and no exact duplicate question strings. Top-level counts exactly reproduce the paper's 12-discipline distribution. The pinned code can format prompts, call OpenAI-compatible endpoints, retain raw responses/usage, extract letters through `lighteval`, and compute a Pass@1-style score over 1, 4, or 8 samples.

This supports inspectable final-question text and exact-letter scoring. It does not support replay of selection, review, incentive, refinement, rank stability, or the paper's model table.

### Release conformance failures

A complete local audit found:

1. **260, not 261, unique released discipline paths.** Every row has a three-level path, but the 899 records instantiate only 260 unique strings. The paper, appendix taxonomy, README, and dataset card claim 261. Taxonomy breadth is therefore not release-conformant as stated.
2. **No released source fields.** Contrary to the paper's claim that each item ships with option-level sources and originating material, and the dataset card's `question_source` description, all 899 released rows have only `index`, `discipline`, `question`, `options`, and `correct_answer`. None of 8,990 option objects has a `source`; no row has `question_source` or `question_material`. Explanations are present, but evidence traceability is not.
3. **Strong answer-position imbalance.** A–J counts are `[187, 87, 90, 87, 75, 69, 96, 66, 46, 96]`; uniformity gives chi-square 141.01 with 9 df (`p ≈ 6.38e-26`). A is keyed more than four times as often as I. The paper supplies no position-bias or answer-permutation test. Ten options lower uniform chance only if answer placement and model position preferences are controlled.
4. **Claimed process artifacts are absent from the acquired release.** The paper itself contains portions of manuals and LLM prompts in Appendix E, but the pinned dataset and official repository do not contain the claimed anchor sets, selection scores, calibrator labels, rubric weights, judge outputs, reviewer identities/assignments, payment/audit/appeal logs, candidate/revision/rejection ledger, raw model trials, or rank-analysis inputs. The official repository has only 11 files beyond directories and is an inference/scoring utility.
5. **Holdout claims conflict with public state.** The datasheet says the test split is an encrypted archive with a canary and an open development split, and that leaderboard submissions use a holdout protocol (p. 46). The pinned Hugging Face release exposes all 899 questions and keyed answers as a plain JSON test file; no dev/test split, encryption, or canary is present.
6. **Licenses conflict.** The datasheet says dataset CC-BY-4.0 and code MIT. The pinned dataset card declares ODC-By, while `pyproject.toml` declares Apache-2.0 and the repository has no license file. These are operational provenance defects, not merely editorial differences.
7. **Process descriptions conflict.** The main paper specifies four stages; the datasheet calls collection three-stage while separately mentioning refinement. The dataset card's mutable results table also includes models absent from immutable v2, illustrating why release-time results must not be treated as paper-time evidence.

The released first item itself illustrates why explanation presence is not source validation: several terse distractor explanations make unsupported substantive claims, yet the source objects required to adjudicate them are absent. This review does not attempt a disciplinary factual audit; it establishes that the advertised evidence chain cannot be inspected.

## Unique insight: a formal guarantee needs an instantiation witness

KINA's strongest transferable contribution is not either headline theorem alone. It is the opportunity to separate **objective guarantee**, **behavioral guarantee**, and **realized-system evidence**.

For coverage:

`expert population and mandate → elicited anchors/weights → agreement and unresolved omissions → candidate-to-anchor evidence view → calibrated support scores → constrained optimizer realization → selected task lineage → external coverage/omission challenge`.

For incentives:

`participant eligibility and rights → complete payoff/cost/information game → randomized assignment and treatment → effort opportunity → observable review predicates → independent audit/adjudication → payment/appeal/welfare outcome → retained-item validity and cost`.

A proof over fixed support scores says nothing about whether experts supplied the right anchors, whether a judge scored them validly, or whether the released set contains them. A proof that a bonus can reward high effort says nothing about realized `Δp_min`, score validity, collusion, joint-penalty fairness, attrition, or item quality. In both cases, `skill-bench` needs an **instantiation witness**: immutable records binding every theorem variable and assumption to an observed implementation object, plus falsification tests for the links the theorem treats as given.

The empirical comparison also reveals an important design error: audit cannot simultaneously be an unrecorded treatment component and the outcome authority used to validate the payment treatment. A clean study must hold audit probability and audit protocol fixed across pay arms, or explicitly estimate the combined package effect and stop attributing it to the tournament theorem.

## Limitations, validity threats, and operational realism

### Coverage and construct validity

1. The approximation is only to an authored proxy, not population or professional-work representativeness.
2. Anchor elicitation has no panel composition, independent replication, agreement, dissent, omission challenge, or stakeholder weighting evidence.
3. Candidate support and duplicate scores depend on LLM signatures/calibrators whose models, prompts, labels, performance, and outputs are unreleased.
4. Actual quota/duplicate-constrained selection lacks the cardinality-only approximation guarantee.
5. Difficulty-conditioned admission (three of five models must fail) can distort coverage toward the blind spots of named construction models.
6. Counts are highly unequal: Engineering and Science comprise 509/899 items, while three disciplines have 13–19 each. CIP branch count is a design allocation, not an inference-population distribution.
7. MCQ knowledge accuracy does not measure realistic multi-step knowledge work, artifact production, tool judgment, or professional consequence.

### Incentive and participation validity

8. The theorem assumes effort improves quality and score visibility enough that `Δp_min > 0`; neither is estimated or released.
9. Validated-score rubric weights, bar, base pay, bonuses, costs, realized earnings, penalties, and discipline pricing are absent.
10. Tournament and flat phases differ in audit, time, and likely participant/task composition; no causal incentive effect is identified.
11. Jointly penalizing both reviewers after an audit failure can punish a diligent dissenting reviewer and alter reporting, risk, appeal, and attrition behavior.
12. Competitive pay may crowd out cooperation or reward scoring tactics; no fixed-audit cooperative/base-pay arm tests this.
13. Screening includes compliance and self-blame items, potentially excluding experts who challenge flawed standards.
14. No contributor counts, demographics, hours, acceptance/revision burden, withdrawals, welfare, pay adequacy, disputes, appeal outcomes, concentration, consent instrument, attribution, or reusable reciprocal output are reported.
15. An ethics assurance in the datasheet is not a reproducible participation-governance record.

### Measurement and reliability

16. Internal thinning stability is not benchmark-form, item-universe, future-version, or API-time stability.
17. Item, subfield, author, source, reviewer, and four-call dependence are not modeled.
18. Tiny discipline denominators make several “diagnostic” spreads unstable; the paper acknowledges this but still advances broad humanities/social-science interpretations.
19. Answer-position imbalance creates an avoidable scoring nuisance.
20. Native search treatments are incomparable and uncontrolled for search-time contamination.
21. Final exact-letter scoring does not validate item keys, accepted alternatives, explanation quality, or source entailment.

### Reproducibility and operations

Final-corpus replay is moderate: the immutable paper and keyed JSON are retained, and the compact code exposes prompt and letter scoring. Mechanism reproducibility is poor. There is no executable coverage selector, anchor pack, selection ledger, reviewer platform, payment table, audit sampler, appeal log, refinement trace, raw trial matrix, or analysis notebook. The public code postdates paper v2 and cannot reproduce AVG@4 tables without unpublished outputs and provider configurations.

Operational texture is useful: a three-month collection window, approximately USD 100,000 total spend, work-in-progress caps, scarcity pricing, appeals, audits, and removal rules show awareness of real coordination. But affordability is not identifiable without candidates, rejected/revised units, people, hours, role costs, platform/LLM spend, and maintenance. The inconsistent license and holdout declarations also weaken the claimed 36-month maintenance/leaderboard plan.

## Transfer to `skill-bench`

### Retain

1. Declare the exact coverage proxy and its claim ceiling; never call an optimizer guarantee a representativeness guarantee.
2. Use anchor-level diminishing-return selection as one portfolio-construction signal alongside validity, workflow structure, failure signatures, cost, and affected-stakeholder coverage.
3. Make expert-review compensation an explicit mechanism with a complete payoff table rather than an undocumented operational detail.
4. Report rank/decision stability under bounded budgets, but name the sampling population and target decision precisely.
5. Preserve appeals, independent audits, candidate histories, and accepted/rejected alternatives as first-class evidence.

### Repair and test

1. **Coverage instantiation witness:** version experts/mandates, anchors, weights, disagreements, candidate scores, calibration sets, model/prompts, quota constraints, optimizer output, repairs, omitted-anchor challenges, and released-item links. Replicate anchors with independent panels and test coverage against held-out experts and use cases.
2. **Incentive experiment:** preregister comparable contribution units randomized between fixed audit + adequate base pay and the same fixed audit + validity-gated bonus. Keep task allocation, standards, audit probability, adjudicators, and appeal rights fixed. Measure independent defect detection, false challenge, retained validity, contributor/coordinator minutes, earnings distribution, burden, attrition, disputes, and cost per validity-bearing artifact.
3. **Assumption checks:** estimate score reliability, score–independent-audit association, winning-probability gain, cost distributions, dependence between reviewers, and treatment-specific missingness before invoking the theorem.
4. **Release conformance:** fail release if taxonomy paths, source fields, split/holdout claims, licenses, prompt/scorer versions, or analysis inputs disagree with the declared instrument.
5. **Decision stability:** resample at task-lineage/domain clusters, include system entry/exit around the compared set, incorporate repeated-run uncertainty, and use equivalent-form or future-form bridges. Stability of adjacent rank is not capability validity.
6. **Answer-position control:** randomize option order per trial with key-preserving transformations, or balance positions and report permutation sensitivity.

### Do not infer

Do not infer population representativeness, expert consensus, realistic knowledge work, professional competence, general capability, incentive compatibility, truthful review, superior item validity, contributor benefit, affordability, certification, or deployment readiness from the optimization proof, tournament proof, observational phase comparison, MCQ scores, or adjacent-rank stability.

## Comparison with ELAIPBench and existing repository machinery

ELAIPBench (`papers/agent-benchmarks/2026-07-12-elaipbench-expert-author-incentives.md`) provides a real writer–evidence-verifier–answer-verifier contest but no formal game or fixed-pay contrast. KINA improves the **theoretical rung**: it specifies effort costs, winning probabilities, score noise, an effort threshold, and FOSD propagation. It also reports an observational flat-versus-tournament phase comparison and total spend.

KINA does not repair ELAIPBench's empirical gaps. Both hide candidate/revision/payment histories and contributor welfare; both condition admission on named model failure; both lack independently released mechanism evidence. KINA's comparison additionally bundles audit with tournament. Its theorem therefore supplies a useful preregistration template, not evidence that the realized mechanism caused better items.

No new schema is warranted. Existing expert-participation records can hold consent, payment, decision rights, transformation lineage, and reconsent; expertise-transfer records can hold anchors and authoring evidence; task-health can hold candidate/revision/audit/adjudication history; metric monitoring can define defect and coverage estimands; validity arguments can cap claims; and response/cluster machinery can represent decision stability. The missing next step is a consented, preregistered real-contribution comparison, already gated by the blocked elicitation-session work—not another synthetic contract.

## Concrete repository actions

- [x] Read and hash the complete immutable v2 paper, including proofs, manuals, prompts, experiment details, datasheet, and final page.
- [x] Audit all 899 pinned official dataset rows and the complete official code archive with release-timing boundaries.
- [x] Reconstruct the coverage objective, theorem assumptions, complete stated workflow, payment model, empirical phase comparison, model evaluation, and rank-thinning estimand.
- [x] Identify release-level taxonomy, source-evidence, answer-position, holdout, license, and process conformance defects.
- [x] Compare KINA with ELAIPBench and map nonduplicate requirements to existing participation, expertise-transfer, task-health, metric, and validity machinery.
- [ ] At the first consented expert-authoring opportunity, preregister the fixed-audit base-pay versus fixed-audit validity-gated-bonus comparison described above. Do not simulate contributors or treat internal fixtures as incentive evidence.

No new queue task is added: the real-participant prerequisite remains unmet, and creating another build task would duplicate existing contracts and the blocked `build-elicitation-session-contract` gate.

## Bottom line

KINA deserves credit for stating where its mathematical claims stop: one theorem optimizes a proxy, and the other depends on strong behavioral assumptions. The central failure is the missing bridge from those abstractions to the realized benchmark. The constrained selector is not covered by the cardinality-only guarantee; the tournament comparison adds audit only in the tournament phase; and none of the anchor, score, payment, audit, candidate, or bootstrap records needed to test implementation are released. The public corpus itself exposes 260 rather than 261 discipline paths, no source fields, a severe answer-position imbalance, and declarations of encryption and licenses that do not match the pinned artifacts.

For `skill-bench`, the durable lesson is to require an instantiation witness for every formal guarantee. A theorem should make a benchmark claim narrower and more falsifiable—not provide a prestigious label for an unreleased pipeline.