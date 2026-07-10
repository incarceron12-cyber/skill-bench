# Paper Review: Expert Evaluation and the Limits of Human Feedback in Mental Health AI Safety Testing

- **Paper:** https://arxiv.org/abs/2601.18061v3
- **Authors:** Kiana Jafari et al.
- **Date read:** 2026-07-11
- **Venue / source:** FAccT 2026; immutable arXiv v3
- **Local PDF:** `data/papers/pdfs/2601.18061v3-irreducible-disagreement.pdf` (27 pages; SHA-256 `09269b91bda2b55de23c669316d718589cd306a83c0b86a7fd5bee0fac174223`)
- **Local text:** `data/papers/text/2601.18061v3-irreducible-disagreement.txt` (SHA-256 `9054075ba1f5176d21e2567868300dfe6e2bfe0f34c86dad17c6d5251851aade`)
- **Official dataset inspected:** https://github.com/sisl/lohfmh-dataset/tree/7efae6a08adf3cb573bf7dcfd161d28bd9912983
- **Local release:** `data/sources/releases/2601.18061v3-lohfmh-dataset/sisl-lohfmh-dataset-7efae6a.zip` (SHA-256 `79b0343a4443739bbec996cdee014172a46ccb49a6ac80f758b60c9887b9fec4`)
- **Release provenance:** `data/sources/releases/2601.18061v3-lohfmh-dataset/provenance.json`
- **Tags:** expert-disagreement, human-feedback, validity, aggregation, adjudication, perspectivism, safety

## One-sentence contribution

The paper gives a useful small-panel existence proof that three psychiatrists can apply the same eight-factor rubric to the same 360 synthetic mental-health responses yet produce very low agreement and coherent rater-specific score patterns; its evidence supports preserving plural judgments and treating aggregation as a policy decision, but does not identify the disagreement as *irreducible*, prove that each post-hoc framework caused the ratings, or show that consensus is invalid across expert evaluation generally.

## Why this matters for skill-bench

This advances charter objectives A, B, E, and F by challenging the assumption that an expert rubric becomes ground truth after averaging or adjudication. `skill-bench` already preserves plural observations and adjudication lineage, but the paper sharpens a missing boundary: **some disagreement may be the construct**. A rating is indexed not only by observer and evidence view, but by an evaluative framework, intended use, stakeholder authority, and error trade-off. A mean can be mathematically well-defined while licensing no coherent professional interpretation.

The transferable hypothesis is cross-domain, not clinical: when legitimate professional schools prioritize different consequences, evaluator disagreement should first trigger a validity investigation—not automatic consensus, majority vote, or a larger panel. Useful benchmark machinery must distinguish remediable disagreement (unclear rubric, insufficient evidence, rater drift) from stable framework-conditioned disagreement and unresolved value conflict.

## Research question and claim boundary

The study asks whether certified experts provide a reliable signal when evaluating isolated AI mental-health responses and whether observed disagreement reflects measurement error or different clinical frameworks (Sections 1 and 2.5, pp. 2–5).

The evidence supports narrower claims:

- in this complete-crossed panel, single-rater ICCs were poor for every factor (0.087–0.295), and averaged-rater ICCs remained below 0.60 (Table 1, p. 8);
- rater score distributions were strongly directional, especially for boundaries and empathy (Section 4.3, pp. 9–10; Table 20, p. 27);
- disagreement varied by factor, risk type, and model output source (Sections 4.2 and 4.4, pp. 8–11);
- three post-rating interviews yielded different articulated priorities about safety, engagement, and cultural context (Section 5, pp. 11–13).

It does **not** establish that disagreement is irreducible, that the three named orientations are exhaustive or prospectively stable, that framework rather than rubric defects or evidence insufficiency caused the scores, that mean labels are always incoherent, that additional independent experts cannot improve a decision, or that this clinical pattern generalizes unchanged to other professions. The authors appropriately call the result an existence proof and request replication (Section 6, p. 13), but stronger causal and universal language elsewhere exceeds the design.

## Methodology and system

### Cases and response generation

The research team authored 360 synthetic prompts, crossing three severity levels and three communication-directness levels across symptom/risk families. Severity was informed by named assessment instruments, but the prompts are researcher-authored vignettes rather than sampled patient interactions. Four model endpoints each answered 90 prompts: `gpt-5-2025-08-07`, Claude 4 Sonnet, Grok-4-0709, and Llama 3.2, reportedly with default API parameters (Section 3.1, pp. 5–6). Model allocation is balanced, but the paper does not report prompt-to-model randomization, endpoint dates, seeds, full generation requests, failures, or repeated outputs.

The released `raw_prompts.csv` confirms 360 unique rows, balanced 120/120/120 by severity and directness and 90 per model. It also reveals author clustering—144 prompts by Akanksha, 108 by Darja, and 108 by Nina—and malformed or overloaded metadata: `Age` includes `Moderate` and “Roomate implies a bit older,” while `Gender` includes `Moderate`. These release defects do not invalidate the ratings but weaken claims that demographic/context fields were controlled and expose undocumented author/item dependence.

### Rubric and evidence view

The rubric synthesizes prior mental-health and communication frameworks into eight five-point factors: harm severity, harm likelihood, correctness, relevance, active listening, empathy/validation, boundaries/disclaimers, and actionability/encouragement (Section 3.2, p. 6; Tables 6–13, pp. 21–24). Every rater saw the prompt, one model response, and all descriptors; model identity was hidden (Section 3.3, pp. 6–7).

Several factors embed unobserved or contested quantities. Harm likelihood asks for probabilities of user action without a user population or longitudinal evidence. Relevance level 5 rewards anticipating hidden concerns. Correctness mixes literature, professional experience, common sense, and citation behavior. Boundaries encode one particular disclosure/referral progression. The framework therefore combines observable text properties, counterfactual outcomes, professional norms, and policy preferences on nominally common scales. The very low correlation structure may partly diagnose a non-unidimensional instrument rather than irreducible expert philosophy.

### Expert panel and procedure

Three U.S.-trained certified psychiatrists were purposively selected for differences in subspecialty, experience (4, 13, and 8 years), practice setting, theoretical orientation, and therapeutic modalities (Section 3.3 and Table 14, pp. 6 and 25). They completed a 90-minute calibration on held-out examples, then independently rated every response on all factors. All three later participated in 45–60 minute semi-structured interviews (Table 15, pp. 25–26).

The complete-crossed design is a strength: every item receives every expert view, avoiding assignment confounding. But three purposively differentiated raters cannot separate framework effects from individual effects. Framework, experience, subspecialty, practice setting, AI-deployment priors, scale-use style, and identity are perfectly confounded. The paper reports no repeat ratings, prospective framework declaration, counterbalanced calibration condition, or second panel. Thus neither within-rater stability nor framework-level replication is observable.

The study says raters were blind to model source, not to prompt authorship. Released rows retain an `Author` field, and the interview protocol explicitly probes “self-rating bias” and whether authorship affected ratings (Table 15, p. 26). At least two prompt author first names match paper authors with clinical roles. The paper does not state whether that column was hidden in the interface, which experts authored prompts, or report the authorship-bias analysis. This is a material hindsight and non-independence ambiguity.

### Quantitative analysis

The primary statistics are ICC(2,1) for one rater and ICC(2,k) for the three-rater average, ordinal Krippendorff alpha, mean absolute deviation (MAD), rater means, pairwise directions, correlations, Friedman tests, effect sizes, and bootstrap/permutation comparisons (Section 3.4, p. 7). Table 1 reports 2,000-bootstrap 95% intervals.

Using two-way random-effects absolute-agreement ICC is directionally suitable for a fully crossed panel, but the inferential population is unclear: the three raters were purposively selected, not sampled from a defined rater universe. The paper does not specify bootstrap unit or preserve item/risk/author clustering. It interprets pooled ICC 0.269 as 27% “true” response variance and 73% “rater disagreement and measurement error” (p. 8), an over-simple decomposition given item-by-rater interactions and a multidimensional ordinal instrument. Alpha details—distance function, missing-value handling, and bootstrap scheme—are absent.

MAD comparisons treat the same 360 items repeatedly across eight factors and three raters. The paper reports a suicide–ADHD difference with bootstrap and permutation p-values but does not explain whether resampling respects item, condition, author, and model dependence or adjust the many risk/severity/model comparisons. “Highest on safety-critical items” is also selective: psychosis/hallucination risk has slightly higher MAD (0.602) than suicide (0.598), and risk type is confounded with authored condition content.

### Qualitative analysis

The authors use reflexive thematic analysis of three post-hoc interviews, explicitly seeking explanations for quantitative patterns (Section 3.4, p. 7). The appendix supplies a condensed protocol and coding themes, which is better disclosure than many benchmark studies.

However, no interview transcripts, analysis code, coding memos, codebook evolution, negative cases, researcher positionality/reflexivity account, second-coder comparison, participant member-check, or quotation-to-rating linkage is released. Reflexive thematic analysis does not require inter-coder reliability, but it does require methodological transparency about interpretation; here, the three elegant framework profiles may be plausible narratives without enough evidence to distinguish stable evaluative philosophy from retrospective sense-making. The interviews happened after all ratings and explicitly asked about disagreement, creating hindsight and demand-characteristic risks.

## Evidence and results

### Reliability and directional patterns

All single-rater ICCs are below 0.40: boundaries is lowest at 0.087 and active listening highest at 0.295. Three-rater-average ICCs range 0.223–0.556. Krippendorff alpha ranges from -0.203 for boundaries to 0.209 for active listening (Table 1, p. 8). These are compelling evidence that a randomly selected single label—or even the simple average of this panel—is not a stable instrument under the paper's chosen agreement criteria.

The strongest descriptive result is not one coefficient but the rater-by-factor surface. Rater C gives boundaries a 2 on 332/360 items, while Rater A uses 3–5; their means differ by 1.69 points. Rater C is simultaneously strict on quality factors and high on estimated harm, which supports coherent directional scoring rather than symmetric noise (Section 4.3, pp. 9–10). Yet consistency of direction does not prove clinical legitimacy or causal framework attribution. It could also reflect threshold use, rubric interpretation, prior beliefs about AI deployment, or a near-degenerate scale response.

The paper states four factors have negative alpha, but severity's reported alpha is -0.001 with an interval crossing zero and likelihood is -0.014 with an interval crossing zero. Only boundaries has clearly below-zero uncertainty. “Worse than chance” should not be generalized across factors.

### High-stakes and model-specific disagreement

MAD is highest for hallucination reinforcement (0.602), suicide support (0.598), and self-harm support (0.566), and lowest for ADHD behavior (0.461) (Table 2, p. 9). This supports heterogeneous disagreement by authored risk category, not a general law that stakes increase disagreement. Severity is non-monotonic (high 0.552, low 0.512, moderate 0.497), and categories differ simultaneously in content, prompt authorship, assessment basis, and possible model behavior.

Model-specific MAD ranges narrowly from roughly 0.502 to 0.546 overall but differs substantially by factor (Table 4, p. 10). Since each prompt receives only one model response rather than all four matched responses, model is partly confounded with item realization; no repeated generations or paired prompt-model factorial identifies model style as the cause.

### Release audit

The pinned official revision contains README, license, `raw_prompts.csv`, and one 360-row rating CSV per expert. It does **not** contain analysis code, environment/endpoint manifest, participant protocol beyond the paper appendix, interview audio/transcripts/codes, calibration examples, a separate rubric artifact, or paper result tables.

All three expert files contain the same 360 prompts/responses. Two files each have one blank rating despite every row being marked `Completed=checked`; the paper's pairwise direction counts of 2,878/2,879 rather than 2,880 expose these missing cells, but no missingness policy is stated. There are 8,638 observed ratings, not the nominal 8,640. The abstract/method wording also alternates among “1,080 expert annotations,” “1,080 response-level annotations per rater,” and 8,640 factor ratings. The files make the hierarchy clear—360 responses × 3 experts = 1,080 response-expert records, containing nominally 8 ratings each—but the paper's unit labels are inconsistent.

## Unique insight

The paper's most valuable insight is not “experts cannot agree.” It is that **aggregation changes the target**. There are at least four distinct objects:

1. an expert's observation under a specific evidence view;
2. that expert's framework-conditioned judgment and rationale;
3. a decision rule combining judgments for a declared stakeholder/use and error loss;
4. a claim about professional quality, safety, or readiness.

A mean is only object 3, not a discovered version of object 2 or proof of object 4. If no expert endorses the midpoint, the aggregate can still be a defensible governance policy—but only if its weighting, affected stakeholders, loss trade-offs, and excluded interpretations are explicit. Conversely, preserving every dissenting label is not enough: a benchmark still needs a decision procedure. “Do not aggregate” is incomplete unless the system declares when to stratify, escalate, veto, seek context, collect outcomes, or report a distribution.

This yields a practical identification ladder for `skill-bench`:

`item/evidence defect → rubric comprehension → scale-use stability → framework stability → framework-conditioned judgment → stakeholder decision rule → licensed claim`

Only after earlier explanations are tested should disagreement be labeled framework-conditioned or provisionally irreducible. The paper jumps too quickly from directional scores plus post-hoc interviews to the last explanation.

## Limitations and validity threats

1. **Three raters cannot identify a framework effect.** Person, framework, experience, specialty, practice, culture, and AI priors are perfectly confounded.
2. **No intrarater replication.** Each rating occurs once, so stable philosophy cannot be separated from within-person noise or drift.
3. **Post-hoc framework elicitation.** Interviews after ratings and statistical inspection invite hindsight rationalization and demand effects.
4. **Thin qualitative audit trail.** No transcripts, coding materials, negative cases, reflexivity statement, member-check, or item-level quote linkage are released.
5. **Novel rubric is not validated.** Several factors mix observable text, counterfactual outcomes, hidden user context, professional norms, and policy preferences.
6. **Calibration has no ablation.** The claim that more calibration risks conformity is plausible but untested; no no-calibration or extended-calibration arm exists.
7. **Purposive U.S. panel.** It is intentionally diverse but not representative of psychiatrists, patients, cultures, or stakeholder groups.
8. **Synthetic, single-turn cases.** No real-user sampling, multi-turn history, body language, outcomes, or longitudinal consequences establish ecological validity.
9. **Prompt author/rater ambiguity.** Released author identity and the interview's self-rating probe are not reconciled with blinding or independence.
10. **Item construction is clustered.** Three named authors contribute unequal prompt blocks; uncertainty does not clearly account for author/risk/item dependence.
11. **Model comparison is unpaired.** Each prompt has one model response, with no repeated generations, making model-specific disagreement descriptive only.
12. **Endpoint realization is incomplete.** Default parameters, access dates, full request records, seeds, and provider outputs are not archived.
13. **Missing ratings are under-specified.** Two blank cells coexist with completion flags; alpha/ICC missingness handling is not disclosed.
14. **Ordinal-scale analysis is incomplete.** Alpha distance and bootstrap details are absent; ICC variance language overstates a clean true/error decomposition.
15. **Multiple comparisons.** Numerous risk, severity, condition, factor, and model analyses lack a declared family-wise analysis plan.
16. **“Irreducible” is not experimentally established.** No prospective framework declaration, repeated panel, framework-matched replication, richer context, outcome evidence, or alternative rubric tests reducibility.
17. **Legitimacy is asserted.** The study does not independently establish that every articulated framework or every application of it is clinically defensible for AI.
18. **Aggregation critique is one-sided.** An unendorsed midpoint may still be an explicit social-choice policy; preserving disagreement does not by itself choose safe action.
19. **Deployment recommendations are untested.** Framework weighting, conservative escalation, and dynamic selection receive no intervention or outcome evaluation.
20. **Safety claim boundary is narrow.** Low agreement shows instrument instability, not which response is safe, which expert is right, or whether the models caused harm.

## Reproducibility and operational realism

Reproducibility is moderate for auditing raw ratings and weak for reproducing the analyses or explanatory claims. The immutable PDF/text, exact prompt/response rows, three expert rating tables, rubric appendix, model identifiers, and participant summaries permit independent recomputation of many descriptive statistics. The released complete-crossed labels are unusually valuable.

Exact reproduction is blocked by absent analysis code, calibration examples, endpoint request manifests, generation timestamps/parameters, randomization/allocation code, interview transcripts and coding trail, and explicit missing-value/bootstrap procedures. The repository's README promises “dataset and code,” but commit `7efae6a` has no analysis code. The two blank ratings and malformed demographic fields require undocumented cleaning decisions.

Operational realism is deliberately limited. Synthetic single-turn responses isolate rating disagreement but omit longitudinal outcomes, dynamic user context, care access, cultural fit, real deployment consequences, and stakeholder preferences. This makes the source a strong measurement-validity case study, not a clinical benchmark template and not evidence that all knowledge-work expert ratings are unstable.

## Transfer to skill-bench

### Preserve framework-indexed observations

Extend the conceptual interpretation of existing grader/human-observation records—not necessarily the schema—with:

- observer identity/authority and independence relation;
- evidence view and missing context;
- prospectively declared evaluative framework or school, with source and scope;
- criterion interpretation, threshold, rationale, uncertainty, and veto status;
- repeat-observation link and calibration exposure;
- framework confidence (`declared`, `elicited`, `analyst_inferred`) and stability evidence.

Analyst-inferred post-hoc labels must never silently become expert-endorsed framework metadata.

### Separate aggregation from adjudication

Store aggregation as a versioned governance operation with intended use, stakeholder set, weighting/selection rule, error-loss basis, dissent preserved, whether any expert endorses the output, and excluded interpretations. Adjudication should be optional. Allowed dispositions should include `resolved_specification_error`, `resolved_evidence_gap`, `resolved_rater_error`, `framework_stratified`, `policy_selected_with_dissent`, and `unresolved_value_conflict`.

### Require reducibility tests before an “irreducible” label

For consequential plural judgments, test at least:

1. rubric comprehension and evidence sufficiency;
2. within-rater repeat stability;
3. prospective framework declaration;
4. multiple experts per claimed framework;
5. framework-by-item interaction on held-out cases;
6. alternate rubric/context conditions;
7. outcome or stakeholder evidence where available.

Until then, use `unresolved_systematic_disagreement`, not `irreducible_disagreement`.

### Report a disagreement surface, not one agreement score

Estimate disagreement by criterion, severity/consequence, task family, source author, configured system, evidence view, and stakeholder/framework. Preserve prevalence, missingness, clustered uncertainty, and scale distributions. A low pooled ICC cannot alone license abandoning a criterion; a high pooled agreement cannot license professional validity.

### Connect dissent to claims and decisions

A validity argument should state whether a score means agreement with one declared framework, a distribution over frameworks, a stakeholder-selected policy, a minimum/veto safety rule, or unresolved conflict. Broad “expert quality” and “professional consensus” claims remain unsupported where disagreement is systematic and the decision rule is undisclosed.

### Benchmark test implied by the source

Use a small cross-domain **plural-judgment calibration slice** before changing the core schema: plant independent labels where (a) a missing evidence view explains disagreement, (b) repeat rating exposes instability, (c) two prospectively declared frameworks yield stable different thresholds, and (d) a policy-selected aggregate is not endorsed by any rater. Verify that the evidence-chain audit blocks consensus/professional-validity upgrades while preserving all observations and a declared governance decision. This is a non-clinical machinery test, not a claim that disagreement is equally prevalent across domains.

## Concrete next actions

1. Add one nonduplicate build task for a plural-judgment/aggregation conformance slice using existing participation, grader, metric, task-health, validity, and evidence-chain records; extend schemas only if the exercised fixture reveals an unrepresentable obligation.
2. Update the canonical taxonomy during the next consolidation to distinguish `unresolved_systematic_disagreement`, framework-conditioned replication, policy aggregation, and adjudicated factual/specification error.
3. In future expert pilots, collect unprompted/prospective framework declarations and repeat a small held-out subset; do not force consensus or treat post-hoc analyst themes as expert metadata.
4. Preserve the paper's clinical limits: do not turn its three orientations into a universal knowledge-work taxonomy or use its reliability thresholds mechanically across constructs.

## Action items completed

- [x] Read and verified the complete immutable v3 PDF/text.
- [x] Inspected the complete pinned official dataset revision and all five released files.
- [x] Audited released row counts, factor values, missingness, balance, author clustering, and metadata defects.
- [x] Separated empirical findings, author prescriptions, clinical-domain limits, and `skill-bench` adaptations.
- [x] Added one nonduplicate evidence-driven build task; no clinical benchmark or new standalone subsystem proposed.
