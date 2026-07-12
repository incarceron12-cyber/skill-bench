# Paper Review: ELAIPBench's Competitive Payoff Rewards Difficulty, but Does Not Establish Incentive Compatibility

- **Paper:** https://arxiv.org/abs/2510.10549v2
- **Authors:** Xinbang Dai, Huikang Hu, Yongrui Chen, Jiaqi Li, Rihui Jin, Yuyang Zhang, Xiaoguang Li, Lifeng Shang, and Guilin Qi
- **Date read:** 2026-07-12
- **Venue / source:** immutable arXiv v2 (2026-01-07)
- **Tags:** expert-participation, incentives, adversarial-authoring, verification, difficulty, benchmark-validity
- **Local PDF:** `data/papers/pdfs/2510.10549v2-elaipbench.pdf` (24 pages; SHA-256 `6d4da1bdb89a740e62247fb73ef8ec4fdff020ee7cd3be27084dda4219eb3b93`)
- **Local text:** `data/papers/text/2510.10549v2-elaipbench.txt` (SHA-256 `75897588e6f4789556fa39f6502898ca46d571c9fceb0baeb408b042796e49f4`)
- **Official release:** `data/sources/releases/2510.10549v2-elaipbench/elabench.jsonl` (403 rows; SHA-256 `a92c7ad68c802e38c2637ee47b4f2fdf24454faf417c88b5e66b099e9d8507fa`); provenance at `data/sources/releases/2510.10549v2-elaipbench/provenance.json`, pinned to official commit `83bf09a83de9b6919190d6a26e51b0ca5a129d26`

## One-sentence contribution

ELAIPBench turns expert question authoring into a three-role writer–evidence-verifier–answer-verifier contest and releases 403 full-paper MCQs, but its mechanism is a useful workflow hypothesis rather than a demonstrated Nash equilibrium: payoffs, assignment, histories, rejection denominators, and behavioral contrasts are too incomplete to establish incentive compatibility, contributor welfare, or superior item validity.

## Why this matters for skill-bench

This review advances charter objectives A, B, and F through targeted expansion into a real compensated authoring mechanism. Its concrete evidence is a full-paper reconstruction plus an audit of the complete released table. It clarifies whether performance-contingent pay can obtain difficult, evidence-grounded expert contributions under limited resources.

The cross-domain lesson is not to copy AI-paper MCQs. It is to test whether **role-separated incentives create independent evidence about distinct item properties**—public basis, answerability, difficulty, and artifact validity—without paying contributors to exploit a single fallible opponent. This is human learning, not a scope commitment to academic QA. Useful completion means preserving payoff and item histories, estimating acceptance and labor denominators, and validating quality against an independent criterion rather than equating verifier outcomes with truth.

## Research question and claimed mechanism

The benchmark asks whether LLMs can answer exact-match single- and multiple-answer questions from full AI papers. The methodological question relevant here is whether adversarial expert roles and contingent bonuses produce questions that are simultaneously difficult and answerable.

Twenty annotators from “top universities” were assigned fixed roles: ten Question Writers, four Evidence Verifiers, and six Answer Verifiers. The team included one professor, one postdoc, eight PhD students, eight current master's students, and two completed master's graduates; all had authored at least one AI paper (main text §3.1; Appendix A.3.1, pp. 3, 15). Role allocation, recruitment frame, screening failures, conflicts, and whether expertise matched each selected paper are not reported.

The workflow (§3.2, pp. 3–5) was:

1. A writer selected a non-canonical paper they knew well, uploaded its extracted text, and authored a question, options, answer, and verbatim evidence for every option.
2. GPT-4o-mini, Qwen2.5-14B-Instruct, and GLM-4-Flash attempted the question with the full paper. If **any** answered correctly, the writer had to revise it; only questions all three missed advanced.
3. An Evidence Verifier answered using the excerpts. A correct match caused both writer and verifier to receive a Level-1 bonus; failure caused revision and loss/reduction of bonus.
4. An Answer Verifier answered from the full paper without external evidence. Correct within 20 minutes labeled the item easy and rewarded the verifier; correct after 20 minutes labeled it moderate and rewarded the writer; incorrect labeled it hard and gave the writer the larger bonus.

The manuscript says annotators received “a base payment of 30 CNY per question they generate,” plus Level-1 30 CNY or Level-2 60 CNY bonuses, and total collection cost exceeded 50,000 CNY (about USD 7,000) over six months (§3.2 and §6, pp. 3, 9). Appendix A.2 instead says writers receive 30 CNY for each “well-written and verified” question and that failed verification reduces reward (pp. 12–14). It mentions base rewards, partial deductions, and timing penalties for verifiers but gives no complete payoff table. Consequently, participant utility cannot be reconstructed.

## Methodology and evidence

### Released instrument

The final set contains 403 questions from 137 papers: 88 labeled SA-MCQ and 315 MA-MCQ; 85 easy, 109 moderate, and 209 hard; 129 ML, 54 CV, and 220 NLP (§3.3, p. 5). Each item is exact-match: one extra or omitted option scores zero. The paper reports 403 as the retained set, but not candidate submissions, revisions, model-filter failures, evidence failures, withdrawals, or author-level concentration.

The official JSONL includes `paper_id`, `question_type`, `question`, `answer`, `relevant_passage`, and complete `paper_content`. It does **not** include writer/verifier IDs, difficulty, discipline, timestamps, attempts, revisions, automatic-review outputs, verifier responses, payoff events, evidence per option, provenance for source publication, or adjudication. Thus the release supports final-item inspection but not mechanism evaluation.

A local audit reproduced 403 rows and 137 paper IDs. Seventy-nine papers have three questions, 29 have four, 17 have two, 11 have one, and one has five. Median whitespace-token counts are 98 for questions, 295 for evidence, and 9,306 for paper text. Paper content is internally stable within each `paper_id`.

The audit also found release-integrity defects relevant to the mechanism's strongest claims:

- Four MA-MCQ rows violate the stated two-or-three-correct-options rule: rows 68 and 274 have one answer; rows 279, 399, and 400 have all four answers (five violations total).
- The paper reports 88 SA and 315 MA items, but answer cardinality yields 90 single-answer records because two MA labels carry one answer.
- Rows 191 and 193 duplicate the same question, paper, and answer.
- Three all-four-correct questions remove distractor discrimination entirely.

These defects do not invalidate the corpus, but they falsify the release-level claim that every MA item obeys the announced answer-cardinality constraint and show that passing the workflow is not equivalent to specification conformance.

### Model and human evidence

Seven base models, seven explicit reasoning configurations, and seven reasoning models were evaluated with three API calls, temperature 0.1, and exact-match accuracy (§4.1 and Appendix A.5, pp. 5–6, 16). Best reported model accuracy was 39.95%. The “human” 48.14% is the single Answer Verifier outcome used to assign difficulty, not a separately sampled human baseline: easy and moderate are 100% by construction, while hard is reported as 0% for Answer Verifiers and 100% for Evidence Verifiers (Table 2, p. 6). This comparison is outcome-conditioned and circular; it cannot estimate broader expert performance or a model–human gap.

The automatic filter conditions the released benchmark on failure by three named models. This is legitimate for constructing a challenge set, but it makes difficulty model-relative and induces selection bias. It cannot show that the mechanism increased general construct difficulty compared with fixed-pay or non-adversarial authoring.

The paper manually examines 30 errors drawn from incorrect LRM/CoT outputs and proposes analytical error, harmful verification, and overconfidence (§4.3, pp. 6–7). It gives no annotator count, blind coding procedure, agreement, denominator by model, or uncertainty. Claims that harmful verification causes over half of errors are exploratory.

## The Nash-equilibrium claim does not follow

The paper states that careful annotation is a Nash equilibrium because deviations are caught by cross-validation and reduce compensation (§§1, 3.2.3, pp. 2, 5). It supplies neither a formal game nor behavioral evidence.

A Nash-equilibrium argument requires players, action spaces, information sets, assignment probabilities, payoff functions, costs of effort, beliefs, and best-response analysis. Here:

- the full payoff function is internally incomplete;
- effort is unobserved and has no modeled cost;
- writers know the three filter models and benefit when one Answer Verifier fails;
- verifier heterogeneity and paper familiarity affect outcomes but are not randomized or modeled;
- evidence verifiers are rewarded for matching the writer's keyed answer, which is treated as truth;
- no independent adjudicator resolves a writer–verifier disagreement;
- anonymity reduces direct collusion but does not prevent repeated-game learning, shared priors, or platform-mediated signaling;
- there is no evidence on deviations, failed checks, revisions, bonuses, response-time distributions, or changes in behavior;
- there is no fixed-pay, noncompetitive, alternative-payoff, or blinded baseline.

Most importantly, the writer's reward rises when the Answer Verifier fails. That can reward valid depth, but also obscurity, ambiguity, formatting burden, niche familiarity, extraction defects, or a verifier-specific knowledge gap. Evidence verification checks whether excerpts reproduce the writer's key; it does not independently prove that the full question has one fair, professionally meaningful interpretation. “Careful annotation” is not a single action and need not be each role's unique best response.

The mechanism therefore has **partial incentive alignment**: it makes some observable failures costly and difficulty valuable. It does not establish incentive compatibility, equilibrium uniqueness, truthful elicitation, or that the rewarded property is deep comprehension.

## Unique insight

ELAIPBench exposes a crucial distinction: **competitive verification is valuable only when each role owns a different, independently observable predicate.** Its roles appear separate, but all quality authority ultimately collapses onto the writer's keyed answer and one verifier's success or failure.

For `skill-bench`, authoring incentives should be attached to typed outcomes:

- **public-basis validity:** an independent reviewer can locate the disclosed requirement;
- **answer/artifact admissibility:** accepted alternatives and contradictions are adjudicated independently of the author;
- **difficulty/discrimination:** multiple target-system and human observations with uncertainty;
- **diagnostic value:** failures map to distinct causes rather than ambiguity or environment defects;
- **maintenance value:** the item survives challenge, contamination, and version changes;
- **participation quality:** contributors understand use, receive agreed value, and can dispute transformations.

No role should be paid merely because another person or model failed. Pay should combine a noncompetitive base for completed labor with claim-specific bonuses triggered by independent, versioned evidence. Difficulty bonuses should require validity gates first and use a population estimate, not one opponent.

A second insight is that outcome-conditioned human results can masquerade as validation. Since answer-verifier behavior defines easy/moderate/hard and is then reported as human performance, the benchmark uses the same observation for construction, labeling, and comparison. `skill-bench` should separate authoring observations, calibration observations, and confirmatory expert trials.

A third insight concerns cost. Over 50,000 CNY and six months produced 403 accepted items—at least about 124 CNY per retained item if all reported expenditure is allocated to the final set—but this ratio is not a replacement-cost estimate. Missing rejected candidates, contributor hours, coordination, platform development, role-specific pay, and author concentration make neither unit labor nor scalability identifiable. ELAIPBench is stronger than the Benchmark Ceiling paper because it reports a real corpus, people, duration, and total spend; it still cannot identify scarcity or marginal incentive effects.

## Limitations and claim boundaries

1. **No incentive comparison.** There is no randomized or matched contrast against fixed pay, cooperative review, alternative bonuses, or different role structures.
2. **Incomplete payoffs.** Main-text and appendix descriptions differ; verifier base rates, penalties, time basis, assignment volume, and realized earnings are absent.
3. **No mechanism denominators.** Candidate items, revisions, exclusions, failed filters, evidence failures, author attrition, and dispute outcomes are unavailable.
4. **No formal game.** Costs, actions, beliefs, repeated interactions, truth state, and best responses are unspecified; “Nash equilibrium” is assertion, not theorem or estimate.
5. **Difficulty is endogenous and opponent-relative.** Three model failures and one Answer Verifier's response define admission and difficulty.
6. **Human comparison is circular.** The reported human score reuses construction labels and one assigned verifier rather than independent expert trials.
7. **Expertise validity is coarse.** Publication and degree status do not establish paper-specific competence; no calibration or role-level performance is reported.
8. **Truth authority is concentrated.** The writer supplies the key; Evidence Verifiers match it; no independent adjudication or accepted-alternative process is described.
9. **Released data violate stated rules.** Five MA labels violate answer cardinality and one question is duplicated.
10. **Quality is not construct validity.** Exact-match MCQs improve scoring reproducibility but may measure option discrimination, paper familiarity, or adversarial puzzle solving rather than realistic research work.
11. **No contributor-welfare evidence.** Gender is 80% male; geography, recruitment access, pay adequacy, hours, burden, satisfaction, disputes, withdrawal, and payment distribution are missing.
12. **No role mobility or concentration analysis.** Fixed assignment can confound role with person; item and earnings concentration cannot be audited.
13. **No contamination control beyond advice.** Writers are told to avoid canonical papers, but no exposure audit, publication cutoff, or memorization test is reported.
14. **Weak statistical treatment.** Three API calls do not address question/paper clustering; model comparisons lack confidence intervals or paired analyses.
15. **Release timing boundary.** The pinned official dataset commit predates arXiv v2; it is official release evidence, not proof of the exact unpublished analysis snapshot.
16. **Narrow external validity.** AI-paper MCQs, university annotators, Chinese-currency pay, and one platform do not establish transfer to professional artifacts, other labor markets, volunteer reciprocity, or cross-domain experts.

## Reproducibility and operational realism

Manuscript and final-corpus reproducibility are good relative to many participation studies: the immutable v2 PDF is locally retained, the official 403-row JSONL is pinned and hashed, full paper text and evidence are embedded, and exact-match scoring can be reconstructed. The final corpus is inspectable enough to detect rule violations.

Mechanism reproducibility is poor. The platform, source code, instructions as displayed, assignment logs, model-filter outputs, revision histories, timers, verifier decisions, payments, and candidate corpus are not released. Another team could imitate the prose workflow but could not reproduce the payoff process or test its claimed equilibrium.

Operational realism is mixed. Six months, 20 qualified participants, role specialization, automatic challenge filtering, revision loops, timed review, and a reported budget provide useful implementation texture. Yet only survivors are visible. The hidden failed-work and compensation ledger is exactly what determines affordability, fairness, and incentive effects.

## Transfer to skill-bench: concrete changes

1. **Treat this as evidence for a bounded author–challenge–adjudicate experiment, not a proven mechanism.** Use the completed expert-participation contract for consent, pay, reciprocity, and authority; do not add another schema.
2. **Freeze a complete payoff table before participation.** Record base pay, bonus triggers, deductions, time compensation, dispute pay, platform fees, expected value, and who bears revision risk.
3. **Gate difficulty bonuses on independent validity.** Public basis, source authority, accepted alternatives, environment integrity, and grader soundness must pass before difficulty can earn a bonus.
4. **Use multiple blinded challengers and separate calibration.** Authoring reviewers should not become the confirmatory human baseline. Model filters should define a versioned selection population, not universal difficulty.
5. **Preserve every candidate and state transition.** Invitation, submission, automatic-filter result, evidence review, revision, adjudication, acceptance, retirement, contributor minutes, and payment belong in denominators.
6. **Pay for adjudication-safe disagreement.** A verifier should be rewarded for a well-supported challenge even if it disagrees with the writer; an independent authority should resolve the key.
7. **Audit specification conformance automatically.** The released one-answer/four-answer MA rows and duplicate question are simple validator failures that should block release.
8. **Estimate incentive effects experimentally.** Randomize or rotate otherwise comparable contribution units among fixed-base cooperative review and base-plus-validity-gated challenge bonuses; compare accepted validity-bearing outputs per contributor and coordinator minute, disagreement, revision, welfare, and retention.
9. **Keep quality, welfare, cost, and scarcity separate.** Do not infer expert validity from credentials, incentive compatibility from accepted outputs, fairness from anonymity, or scalability from total spend.
10. **Return reciprocal value and preserve consent.** ELAIPBench reports payment but not comprehension, rights, attribution, or reusable contributor outputs; existing participation gates remain necessary.

## Action items

- [x] Read and hash the complete immutable v2 paper and verify key claims against the PDF extraction.
- [x] Inspect the complete pinned official 403-row dataset and provenance.
- [x] Reconstruct roles, information flow, admission, evidence verification, difficulty assignment, stated compensation, costs, and claim boundaries.
- [x] Audit the Nash-equilibrium claim against required assumptions and observed evidence.
- [x] Compare nonduplicate lessons with the expert-participation ethnography and Benchmark Ceiling labor review.
- [x] Map findings into existing participation, validity, task-health, and metric machinery without adding a duplicate build task.
- [ ] When a consented expert pilot becomes possible, preregister a small cooperative-versus-validity-gated incentive comparison with complete labor, candidate, payment, dispute, and welfare denominators.

No new queue task is added. The existing blocked real-contribution gate (`build-elicitation-session-contract`) and completed expert-participation, validity-argument, task-health, and metric-monitoring contracts are the correct homes; creating an implementation task before a consented contribution would duplicate existing machinery and invite synthetic testimony.