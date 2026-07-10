# Paper Review: ResearchRubrics — Expert Rubric Authoring and Judge Reliability

- **Paper:** https://arxiv.org/abs/2511.07685v1
- **Authors:** Manasi Sharma et al.
- **Date read:** 2026-07-10
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, 10 November 2025
- **Local PDF:** `data/papers/pdfs/2511.07685v1-researchrubrics.pdf` (27 pages; SHA-256 `8c2da4367453de7b13d4ef9c30ac3446b40abee8e5124699a0f5e8700380f223`)
- **Local text:** `data/papers/text/2511.07685v1-researchrubrics.txt` (SHA-256 `05cef6e0af6842e86cfc16328beecbdd67dfbbdb1cc41387e85f22444bae8d60`)
- **Official code inspected:** https://github.com/scaleapi/researchrubrics/tree/2dc80e2d4c38ddd80439517c259d93c6954b193f (commit `2dc80e2d4c38ddd80439517c259d93c6954b193f`; tree `ebbf51a0bc58e37d3e01419c5ddbecf1351b72f6`; post-v1 release)
- **Official dataset inspected:** https://huggingface.co/datasets/ScaleAI/researchrubrics/tree/85de3115053d1453ed612caacf4a405edc1ad756 (revision `85de3115053d1453ed612caacf4a405edc1ad756`; post-v1 release)
- **Release provenance:** `data/sources/releases/2511.07685v1-researchrubrics/provenance.json`
- **Tags:** expert-rubrics, long-form-artifacts, llm-judge, implicit-requirements, criterion-dependence, dynamic-evidence, validity

## One-sentence contribution

ResearchRubrics demonstrates a costly human author–review–final-review pipeline for turning 101 open-ended prompts into 2,593 weighted criteria and shows that criterion-level binary LLM grading agrees with one expert label substantially better than ternary grading, but it does not establish that its criteria are atomic, professionally authoritative, source-verifiable, independent, or reliable enough to license deployment decisions.

## Why this matters for skill-bench

This is unusually direct evidence for charter objectives B, C, and F: it exposes the actual boundary between expert labor, rubric decomposition, scalable judging, and claims about artifact quality. Its strongest lesson is not “use more criteria.” It is that **authoring effort, criterion applicability, judge reliability, evidence authority, and score interpretation are separate contracts**. ResearchRubrics invests over 2,800 reported human hours in the first of these, partially studies the fourth, and leaves the others under-specified.

The released corpus is valuable because it makes the instrument inspectable. The 101 tasks span ten labels and each has 20–43 criteria. Yet inspection also contradicts a clean “atomic rubric” story: the median criterion is 28 words, the mean is 34.4, the longest is 317 words, and 1,603/2,593 criteria contain an example marker such as “e.g.”, “i.e.”, “such as,” or “for example.” Examples can clarify a construct, but they can also bundle multiple predicates, anchor judges to named answers, and become a hidden reference answer. Fine-grained is therefore not synonymous with atomic or non-leading.

The paper is also a useful warning about hidden requirements. Implicit criteria are the largest category (1,021/2,593, 39.4%; paper Figure 4b, p. 6), and the paper treats omissions of these criteria as a central system failure. Some implicit consequences—side effects in a treatment explanation, for example—are professionally fair. Others may be author preferences never disclosed to the evaluated system. `skill-bench` should preserve the paper's expert elicitation pattern while retaining its stronger public-basis rule: a private check may test a fair consequence of a disclosed requirement, not reward an undisclosed topical checklist merely because an author expected it.

## Research question and claim boundary

The paper asks three linked questions:

1. Can broad, realistic deep-research prompts be evaluated without a single reference report by using many human-written criteria?
2. Can an LLM apply those criteria at scale with adequate agreement to expert labels?
3. Which rubric-writing choices improve or degrade human–LLM agreement?

The evidence supports bounded claims that the authors released a large human-written prompt/criterion inventory; three commercial deep-research systems satisfy materially different fractions of that fixed inventory; binary labels from three named LLM judges reach macro-F1 values of 0.717–0.760 against the study's expert labels; and adding short examples is associated with modestly higher agreement while one specific automatic expansion treatment sharply lowers it (Sections 3–4, pp. 4–11).

It does **not** show that the prompts sample real professional work, that each criterion is correct or independent, that the human labels are reliable ground truth, that judge agreement transfers to new artifact types or rubric authors, that criteria requiring current-source verification can be judged from response text alone, or that a normalized compliance score is a calibrated sufficiency or deployment threshold.

## Methodology

### Prompt sourcing and expert authoring

ResearchRubrics contains 101 single-turn prompts and 2,593 criteria, 20–43 per prompt (Section 3, pp. 4–6; Appendix B.1, pp. 16–17). Initial ideas came from user forums, Q&A sites, and brainstorming, then were adapted. No source-site inventory, sampling frame, inclusion/exclusion protocol, frequency weighting, or preserved raw-to-adapted lineage is reported. The ten released domain labels range from 5 Current Events tasks to 17 AI & ML tasks; this is purposive diversity, not a population sample.

The paper calls its contributors experts but defines them as people with strong STEM backgrounds and task-design/evaluation skill, not domain specialists for every prompt. Participants self-selected familiar domains. Expert 1 drafts a prompt and criteria, Expert 2 iterates with Expert 1 until acceptance, and Expert 3 performs a final “independent” review and adjustment (Figure 2 and Section 3.1, pp. 4–5). This is a sensible quality workflow. However, the paper does not report contributor count beyond the three pipeline roles, qualifications by task, training materials, compensation, time allocation, disagreement rates, number of revision rounds, rejected prompts/criteria, adjudication records, or whether the same three people filled the roles repeatedly. “2,800+ hours” is not decomposed into sourcing, writing, review, response labeling, or analysis.

The method therefore supports **reviewed task-design authority**, not domain-professional authority. For `skill-bench`, those must remain different contributor roles and approval claims.

### Complexity annotation

Tasks receive Conceptual Breadth, Logical Nesting, and Exploration labels, each at three levels (Table 2, p. 5). The definitions are practical authoring prompts: number/diversity of sources, dependent reasoning steps, and underspecification. But the paper calls the axes independent/orthogonal without reporting annotators, inter-rater reliability, adjudication, empirical correlations, or validation against measured human difficulty. Prompt length changes with these labels (Appendix C, pp. 19–22), and domain, prompt length, criterion count, and complexity are not disentangled. Stratified model scores are descriptive slices, not isolated effects of breadth, nesting, or exploration.

### Rubric construction and aggregation

Criteria are assigned one of six declared axes: Explicit Requirements, Implicit Requirements, Synthesis, References/Citation Quality, Communication Quality, and Instruction Following (Table 3, p. 6). Positive and negative weights nominally range from −5 to +5. Absolute weights 4–5 are called mandatory/critical; smaller absolute weights are optional. Ternary judge multipliers are 1, 0.5, or 0, and the weighted numerator—including penalties—is divided by the sum of positive weights (Equation 1, p. 7).

This representation has four important properties:

1. **Mandatory is not a gate.** A response can miss a +5 “mandatory” requirement and compensate with many optional points. Conversely, one severe negative criterion merely subtracts weight; there is no explicit veto, safety gate, or readiness threshold.
2. **The denominator defines an achievement scale, not calibrated quality.** A score of 0.60 is not empirically tied to “adequate,” expected loss, expert acceptance, or deployment readiness despite the paper's deployment-oriented prose.
3. **Criterion dependence is ignored.** Overlapping subrequirements, examples, citation checks, and synthesis checks can reward or penalize the same evidence multiple times. There is no dependency graph, mutually exclusive group, prerequisite relation, or effective-information analysis.
4. **Applicability is missing.** Every criterion is judged for every response to its task; there is no not-applicable/insufficient-evidence state or conditional trigger.

The paper's failure-category statistic averages within-task shares only over tasks containing that category (Equation 2, p. 7). The authors correctly warn these category rates need not sum to one. These figures describe where failed checks are labeled; they do not estimate independent causal failure mechanisms.

### Systems, responses, and judge protocol

The study evaluates OpenAI Deep Research, Gemini Deep Research, and Perplexity Deep Research on all 101 prompts. Their PDF reports are converted to Markdown. The manuscript does not pin endpoint snapshots, retrieval dates, search environments, generation settings, retry policies, or raw response artifacts, even though many tasks depend on current information (Section 4.1, p. 8).

GPT-5, Claude Sonnet 4.5, and Gemini 2.5 Pro judge each response criterion. Ternary grading distinguishes satisfied/partial/not satisfied; binary grading collapses partial into not satisfied. Table 6 reports macro F1 against expert judgments by response system and judge model: 0.717–0.760 binary versus 0.527–0.567 ternary (pp. 10–11).

Nine expert annotators provide “ground truth” across 303 responses (101 × 3), but the manuscript does not state which labels each person made, how many raters saw each response–criterion pair, whether labels were independently duplicated, how disagreements were adjudicated, whether annotators saw source pages, or whether assignment was balanced by domain. No class prevalences, per-class F1, confusion matrices, confidence intervals, inter-human reliability, or adjudication rate are reported. Macro F1 against one final human label measures concordance with that labeling procedure; it does not validate the label as truth.

The grading prompt instructs the judge to use only evidence present in the document (Appendix E, p. 25). That is appropriate for presence and writing-quality criteria. It is structurally insufficient for many source claims: a judge cannot establish that a cited page exists, is authoritative/current, or entails a claim merely from the submitted report. The paper reports citation counts and “accuracy” (Section 4.2, p. 10), but does not specify a source-fetching protocol or release citation-level labels. This limits the evidence to document-level rubric adherence, not independently verified factual grounding.

### Rubric-design ablations

The paper compares original criteria with (a) examples removed versus retained and (b) original criteria versus approximately 100-word LLM-expanded criteria. Short examples improve macro F1 by roughly 0.02–0.04; expansion lowers it by roughly 0.15–0.20 (Table 7, p. 11). This is useful evidence that transformation is a treatment and that verbose automatic elaboration can distort emphasis.

The ablation is nevertheless under-specified. It does not report the number of labels, paired assignment, randomization, model/temperature for transformations, manual checks of semantic preservation, confidence intervals, hypothesis tests, or human relabeling under each transformed criterion. “Catastrophically” describes a large observed difference, not a demonstrated mechanism. The result supports immutable transformation lineage and revalidation—not a universal prohibition on assisted rubric editing.

## Evidence and results interpretation

The three systems score 0.566–0.677 under ternary grading and 0.487–0.615 under binary grading (Table 5, p. 8). The inventory is therefore discriminative for these systems. Logical-nesting slices generally decline with depth, and implicit/synthesis criteria contribute many observed failures (Figures 5–6, pp. 8–9). Response length correlates modestly with score for Gemini and ChatGPT, around 0.20–0.28 depending on measure and grading scheme (Figures 7 and 18, pp. 9, 23–24).

These are descriptive results from one task inventory and one generation period. The paper overreaches when it infers “fundamental architectural limitations” from similar patterns across three proprietary systems (pp. 8, 11–12). The systems may share search, prompting, report-length, source-selection, or judge-interaction biases; no architecture is observed or manipulated. Likewise, “performance collapse” beyond four steps or 35 human-equivalent minutes is not backed by a controlled threshold analysis or reported human-time measurement.

The release inspection found several concrete integrity issues that matter for interpretation:

- Dataset composition matches 101 rows and 2,593 rubric records across ten observed domain values.
- There are 2,274 positive, 318 negative, and one zero-weight criterion.
- One criterion has weight +10 despite the paper's declared [−5, 5] range; three criteria use an undocumented `Miscellaneous` axis; the zero-weight criterion affects no score.
- Two exact criterion strings recur, leaving 2,591 unique texts rather than 2,593 unique texts as stated on p. 4.
- A heuristic finds 131 time-sensitive criteria across 56 tasks; neither dataset nor evaluator binds them to source snapshots, retrieval dates, or acceptable knowledge windows.

These are small fractions of a large corpus, but they show why “human-written and reviewed” cannot replace schema validation, linting, and versioned evidence provenance.

## Unique insight

The deepest insight is that **rubric decomposition creates an executable theory of expert attention, not neutral ground truth**. Every split, example, weight, and implicit criterion decides what the evaluator can see and what counts twice. ResearchRubrics successfully makes much of that theory inspectable, but its score treats the resulting criteria as additive, independent evidence. The released data show why that assumption is unsafe: long example-rich criteria often encode multiple answer elements, criteria can overlap, and hidden contextual expectations dominate the inventory.

This yields a four-stage authority chain for `skill-bench`:

`professional claim → elicited evidence → criterion/check → judge observation → permissible score claim`

Authority can fail at every arrow. A qualified task designer may not be a domain authority; a domain-authoritative statement may be context-specific; a criterion may bundle or distort it; a judge may lack source access; and an aggregate may exceed what its component observations license. “Expert-written” should therefore be metadata about origin, never a terminal validity label.

A second insight is that examples are dual-use. They can improve judge consistency by defining a decision boundary, as Table 7 suggests, while simultaneously leaking answer anchors and shrinking legitimate solution diversity. Examples should be typed as `boundary_case`, `non_exhaustive_instance`, `counterexample`, or `reference_answer_fragment`, with disclosure and authoring independence recorded. Agreement improvement alone is not sufficient evidence that an example preserves construct breadth.

## Transferable design patterns

### 1. Preserve the three-role authoring pattern, but type authority

Keep draft → adversarial/review iteration → final independent release review. Record person/role, claimed qualifications, domain scope, conflicts, prior exposure, exact edits, decision, and unresolved disagreement. Separate `task_design_authority`, `domain_claim_authority`, `artifact_convention_authority`, and `release_authority`; approval in one role must not propagate to another.

### 2. Make each criterion a versioned evidence object

A criterion should have a stable ID; immutable text/hash; polarity; importance; source claim/evidence locators; public basis; applicability predicate; observable; decision rule; examples with type and exhaustiveness; dependency/exclusion relations; grader access needs; and licensed claim. Require a split review when one criterion contains multiple independently falsifiable predicates.

### 3. Separate requirements, gates, and preferences

Do not encode “mandatory” only as weight magnitude. Use:

- **hard gate:** safety, legality, artifact integrity, or minimum validity condition;
- **required scored criterion:** necessary but not independently decisive;
- **optional preference:** quality improvement;
- **penalty:** observed harmful/irrelevant behavior;
- **diagnostic-only check:** informative but excluded from the headline score.

The released +10 and zero-weight anomalies illustrate why validators must enforce declared ranges and semantics.

### 4. Match judge evidence access to the predicate

Presence/format checks may use the artifact alone. Citation existence needs resolver access or a frozen source pack. Entailment needs cited passage retrieval. Authority and freshness need source metadata and a task-time policy. Professional acceptability needs a qualified reviewer or validated proxy. A judge that lacks required evidence must return `insufficient_evidence`, not guess satisfied/not satisfied.

### 5. Calibrate criteria, judges, and aggregation separately

For each grader version, preserve duplicated human labels, independent assignment, adjudication, per-class confusion, prevalence, uncertainty, and slices by criterion family/domain/length. Then test score aggregation against an external decision such as expert artifact acceptability. Macro F1 on criterion labels does not calibrate a task score or deployment threshold.

### 6. Treat rubric transformations as interventions

Store before/after hashes, transformation method/model/prompt, editor, semantic-diff review, examples added/removed, and held-out revalidation. Evaluate both agreement and construct preservation. A transformation that raises agreement by anchoring judges to one answer may worsen validity.

### 7. Version dynamic evidence

Every time-sensitive criterion needs an `as_of` time, acceptable source window, frozen source snapshot or declared live-retrieval policy, authority rules, and retirement/revalidation trigger. Otherwise score drift can reflect the world changing rather than the configured agent changing.

## Limitations and validity threats

1. **No task-population sampling frame.** Forum/Q&A/brainstormed prompts establish variety, not prevalence or ecological representativeness.
2. **Expertise is task-design expertise, not demonstrated domain-professional expertise.** Familiarity is self-selected and qualifications are not linked to prompts or criteria.
3. **The 2,800+ hours are unauditable as a cost model.** No allocation, participant count, compensation, throughput, rejected work, or revision distribution is reported.
4. **Human ground truth is under-specified.** Nine annotators and 303 responses are reported, but label assignment, duplication, adjudication, source access, class balance, and inter-rater reliability are absent.
5. **Criterion atomicity is asserted more strongly than demonstrated.** Many criteria are long and example-rich; no atomicity rubric, split protocol, or independence audit is reported.
6. **Implicit requirements risk hidden obligations.** The benchmark rewards expected content even when the prompt does not disclose its basis; professional fairness is not independently validated.
7. **Additive weighting ignores dependence and vetoes.** Correlated criteria can double-count evidence, while mandatory failures remain compensable.
8. **Weights and thresholds lack empirical calibration.** The six verbal levels, integer weights, partial-credit value 0.5, and compliance denominator are design choices, not estimated utilities.
9. **The complexity taxonomy lacks reliability and construct validation.** Orthogonality, annotation agreement, and relation to human difficulty are not tested.
10. **Dynamic-source validity is unresolved.** Current-event and dated requirements have no frozen source packs, retrieval timestamps, or versioned answer boundaries.
11. **The judge cannot verify many evidence predicates.** Artifact-only prompts cannot independently check URL existence, citation entailment, authority, or freshness.
12. **Macro F1 hides operational errors.** No per-class confusion, confidence intervals, repeated judge runs, calibration, or severe-error analysis is reported.
13. **The ablations lack inferential detail.** Pairing, sample sizes, randomization, transformation model, semantic audits, and uncertainty are absent.
14. **Response-system reproducibility is weak.** Proprietary agents, mutable web results, undocumented run settings, and unreleased raw responses prevent exact replication.
15. **Architecture claims are not identified.** Three correlated commercial systems and descriptive slices cannot distinguish architecture from harness, retrieval, prompt, source, or judge effects.
16. **Length remains a confound.** Criterion-level grading reduces holistic impression bias but rewards coverage; no information-preserving length intervention separates verbosity from content.
17. **Release integrity is imperfect.** A +10 weight, zero weight, undocumented axis, and duplicate texts violate manuscript-level expectations despite multiple human reviews.
18. **Paper/release synchronization is not exact.** The pinned code commit and dataset revision postdate arXiv v1 and verify released artifacts, not manuscript-time bytes.

## Reproducibility and operational realism

Reproducibility is moderate for the released evaluator and weak for the reported experiment. The immutable paper, complete 101-row dataset, pinned 27-file code tree, prompts, binary evaluation logic, and compliance formula are locally preserved. The code can evaluate a report criterion by criterion with Gemini 2.5 Pro, retry calls, track token/cost estimates, and chunk very large documents.

The release is not a full reproduction package. It contains no model responses, expert labels, ablation variants/results, analysis notebooks, environment lockfile, tests beyond placeholders, or exact manuscript-time model configuration. The paper's ternary experiment is not the release's current binary evaluator. The release defaults to a preview Gemini endpoint and unbounded dependency versions; its claimed typical cost/time is documentation, not a measured run ledger.

Release inspection also exposes operational evidence loss. Although the requested JSON includes `evidence_quotes` and `missing_elements`, the `EvaluationResult` and output JSONL discard both and truncate reasoning to 500 characters in the DataFrame path. Outputs do not record grader prompt hash, model response ID, endpoint date, source access, retry count, criterion ID, rubric dataset revision, or document hash. Failed calls return score 0, and batch processing continues, so an evaluator outage can be conflated with task noncompliance unless consumers inspect `success`. Chunk synthesis keeps extracted evidence but does not preserve chunk locators in final records. These are material provenance gaps for diagnostic evaluation.

Operational realism is mixed. Long, heterogeneous reports and open-ended prompts resemble real research outputs better than short QA. Criterion-level review is closer to professional checking than reference overlap. But the benchmark remains single-turn, artifact-only, and detached from stakeholder clarification, source-pack custody, work traces, review/repair, organizational constraints, and consequential decisions. It is best evidence for **scalable application of a fixed authored checklist to long-form documents**, not a complete evaluation of research practice.

## Concrete changes for skill-bench

1. **Refine the existing rubric/check contract rather than add a new subsystem.** When the benchmark bundle next changes, require criterion IDs, polarity, applicability, hard-gate versus scored semantics, dependency links, evidence-access requirements, example types, and immutable source/criterion hashes.
2. **Use this evidence in `build-validity-argument-contract`.** A criterion-level label may support a narrow artifact predicate; aggregate compliance must not automatically support professional capability or readiness. Require an external threshold/loss basis.
3. **Use this evidence in `build-expert-participation-contract`.** Separate task-design expertise from domain authority and preserve author–reviewer–final-review transformations, disagreement, time, compensation, and reciprocal output.
4. **Use this evidence in `build-task-health-lifecycle-contract`.** Add criterion-health checks for duplicated text, undeclared categories, out-of-range/zero weights, dynamic-source expiry, and judge error slices. Instrument defects should create a new version, not rewrite prior scores.
5. **Use this evidence in `build-metric-monitoring-contract`.** Define the eligible criterion population, missing/invalid grader policy, task clustering, criterion dependence, aggregation, uncertainty, and alert semantics before monitoring a “compliance” percentage.
6. **Preserve evidence quotes and insufficiency states in grader records.** Never collapse grader failure or unavailable source evidence into score zero. Hash artifact, rubric, prompt, model, and source snapshot for every observation.
7. **Pilot an atomicity/independence review on the LH adoption rubric.** Have a second reviewer mark bundled predicates, overlapping consequences, answer-anchoring examples, and applicability conditions before any model-based grader calibration.

## Action items for repository

- [x] Read the complete immutable v1 PDF/text and record page/section evidence.
- [x] Inspect the complete official code release at pinned commit `2dc80e2d4c38ddd80439517c259d93c6954b193f` and official dataset at immutable revision `85de3115053d1453ed612caacf4a405edc1ad756`.
- [x] Validate corpus counts and inspect rubric weights, axes, duplicates, lengths, example prevalence, and time-sensitive criteria against the released JSONL.
- [x] Separate paper claims, released-artifact observations, and `skill-bench` adaptations.
- [x] Map implications to the existing expertise-transfer, participation, validity, task-health, and metric tasks.
- [x] Add no queue task: the evidence sharpens existing nonduplicate contracts and does not justify another parallel build.
