# Ontology-conformant reference recovery is not tacit-knowledge extraction

## Source and review status

**Deep review of the complete immutable arXiv v1 paper and static audit of the complete timing-appropriate official release.**

- **Paper:** Lorenzo Lamazzi, Aldo Gangemi, Alessio Giberti, Andrea Giovanni Nuzzolese, Vittorio Andrea Rocca, Mattia Torta, and Francesco Poggi, *Tacit Knowledge Extraction via Logic Augmented Generation and Active Inference*, arXiv:2605.07639v1 (8 May 2026), <https://arxiv.org/abs/2605.07639v1>.
- **Local PDF read in full:** `data/papers/pdfs/2605.07639v1-tacit-knowledge-neurosymbolic.pdf` (17 pages; SHA-256 `6e1011cba22dbcc5625c673ec5ef70b38cd7331fedee17e58b894dd63069c204`).
- **Complete local text read:** `data/papers/text/2605.07639v1-tacit-knowledge-neurosymbolic.txt` (SHA-256 `ec9ab7469f0959464f4522e91b2796baefb1c1e563b904c350f27ea66d4fa22d`).
- **Immutable source inspected:** `data/papers/source/2605.07639v1-source.tar` (SHA-256 `793c52486e90e8fc2fd38435bdef1f01d13757c0b6a02096be90d2e54a167e25`). It contains the TeX, bibliography, styles, and six manuscript images, but no annotations, generated graphs, run rows, analysis code, or evaluation program.
- **Official release audited:** commit `2d7cb5c49d64443dcc28d9ff4fb2ae820db9edc1`, archived at `data/sources/releases/2605.07639v1-tacit-knowledgex/LoLmz-tacit-knowledgex-2d7cb5c.zip`; provenance: `data/sources/releases/2605.07639v1-tacit-knowledgex/provenance.json`. The commit predates arXiv v1 by 4:02:11, making it timing-appropriate official evidence, not proof of paper-run byte identity.
- **Execution boundary:** no paid provider was called. The audit is static because reproducing the reported matrix requires proprietary APIs and because the release contains neither frozen expected outputs nor evaluation code.

This advances charter objectives A, B, D, and E through a bounded repair-video case that tests a general question: when does a model-derived addition become authorized expertise rather than a plausible completion?

## One-sentence contribution

The paper combines ontology-prompted RDF extraction with a second prompt that guesses omitted procedural elements and reports near-perfect reference-relative tool/artifact scores on three repair videos, but its evidence establishes only ontology-shaped extraction plus model-prior imputation against an opaque video-derived reference—not tacit cognition, semantic procedure quality, expert authorization, recipient usability, downstream benefit, manufacturing transfer, or operational readiness.

## Why this matters

`skill-bench` needs to turn tacit domain expertise into tasks, source packs, procedures, and checks without laundering model guesses into expert requirements. This paper sits exactly at that transformation boundary. Its most useful feature is the explicit conceptual split between source-grounded observations and inferred additions (Sections 2–3, PDF pp. 3–8). Its central validity failure is then scoring inferred additions against a reference annotation and calling improved entity recall “tacit knowledge” and “semantic quality” without identifying which additions were expert-held, necessary, correct in context, or useful to a novice.

The defensible chain is:

```text
source video/transcript
→ observable or verbalized operation/entity candidate
→ ontology-shaped representation
→ model-prior proposal for an omitted element
→ proposition-level source/reference match
→ qualified expert disposition and applicability
→ executable procedure/check projection
→ novice or agent adoption
→ task and safety consequence
→ bounded transfer claim
```

The paper measures parts of the first five links for tools and artifacts. It does not measure the rest. That distinction is reusable across domains and does not make device repair or manufacturing the benchmark scope.

## Research question and defensible answer

The paper asks whether Logic-Augmented Generation (LAG) can produce ontology-grounded procedural knowledge graphs from instructional videos or Whisper transcripts and whether an “Active-Inference-inspired” prompt can recover implicit tools, artifacts, operations, warnings, and contextual constraints omitted from the explicit input (Sections 1–4, pp. 1–10).

A bounded answer is supported:

1. Under five named model labels and two source modalities, the authors report parseable, ontology-vocabulary-conforming Turtle outputs for three iFixit videos (Section 5.1, pp. 10–11).
2. Against an undisclosed expert annotation of tool/artifact entities at operation level, reported LAG precision is 1.00 while recall varies; direct-video Gemini conditions often recover more entities than transcript conditions (pp. 11–13).
3. A transcript-only enrichment prompt increases reference-relative recall for every displayed configuration; the paper reports final F1 above 0.95 for tools and artifacts and exact best scores of 0.989/0.994 for Gemini 2.5 Flash (pp. 12–15).
4. The bracket/tweezers example demonstrates a real and useful category: an entity visible in video but absent from narration can be guessed from a transcript and confirmed against video (p. 13).

The study does **not** establish extraction of knowledge held tacitly by an expert. The reference objects may be explicit in video, explicit elsewhere in the transcript, or annotation conventions; model priors may guess them without recovering a person's rationale. The paper appropriately defers operation decomposition, instruction quality, and practical usefulness to a future user study (pp. 10, 11–12), but later claims “semantic quality,” “real-world knowledge transfer,” and practical feasibility beyond that evidence (pp. 14–16).

## Methodology and system

### Dataset, source, and reference

The dataset is three public iFixit videos: iPhone 11 battery replacement, Google Pixel 6a display replacement, and Sega Game Gear speaker replacement (Table 1, p. 9). They are authored instructional demonstrations, not raw recordings of experts being unable to articulate judgments. The transcript path uses Whisper ASR; the paper does not report Whisper model/version, language/configuration, transcription date, correction protocol, word error rate, or whether the supplied release transcript is raw or manually repaired (Sections 3.2 and 4.1, pp. 6–9).

An unspecified “pool of domain experts” identifies more than 90 operations and annotates tools and artifacts. Participant count, credentials, device-specific authority, instructions, independent labeling, agreement, adjudication, exact operation boundaries, entity normalization, and annotation files are absent (Section 4.3, p. 10). Matching is described only as TP/FP/FN “at the operation level.” It is unclear how synonyms, repeated entities, optional tools, equivalent methods, wrong-operation/right-video entities, and disagreements are handled.

This matters because the reference is the entire empirical authority for precision and recall. A perfect precision claim cannot be audited without raw predictions, counts, and matching rules.

### LAG intervention

The LAG condition inserts the full OWL ontology, transcript or YouTube URL, and a long extraction prompt into one model call. The prompt requires one process, ordered steps and operations, source locators, tools/artifacts, and Turtle using only ontology classes/properties. It also adds editorial and decomposition rules not entailed by the ontology—for example when a new step begins, what counts as atomic, title-case names, stable IRI patterns, and when to synthesize transcript text (`LAG/input/prompt.txt`, lines 25–220).

The ontology is a compact procedural vocabulary with Process, Step, Operation, Tool, Artifact, OperationSpecification, and ContentFragment plus sequence, provenance, tool, artifact, instruction, specification, and timestamp properties (`LAG/input/ontology.ttl`). SHACL shapes require names, indices, process/step membership, first/last links, basic ranges, and timestamp ordering (`LAG/input/shapes.ttl`). They are structural contracts, not a model of physical possibility, device compatibility, safety, optimality, or expert authority.

The paper says generated graphs are validated and only passing graphs reach GraphDB (Section 3.2, p. 7). The release does not implement that pipeline. `LAG/main.py` builds one prompt, calls a provider, and writes the raw response to `.ttl`; it imports no RDF parser, SHACL engine, or GraphDB client and performs no retry, code-fence stripping, global class check, semantic validation, or store load. The prompt itself asks for Turtle “in one single code block,” while the runner writes the response unchanged—an implementation path that can make otherwise valid Turtle unparsable. The shapes are present but never invoked by released code.

Accordingly, paper-reported compliance may come from unreleased manual or separate processing. It cannot be attributed to the archived runner, and it does not isolate “logic augmentation” from ordinary schema-in-prompt constrained generation.

### “Active Inference” intervention

The authors explicitly do not implement a cognitive active-inference architecture; the term denotes a prompt inspired by observation, hidden-state inference, policy reconstruction, affordances, prior beliefs, and self-assigned confidence (Section 2, pp. 3–4; Section 3.3, pp. 7–8).

The released module is even narrower than the architecture diagram suggests. `active_inference/main.py` concatenates the prompt with one text fragment and makes one provider call. The frozen example is only “Now you can take out the taptic engine.” The prompt asks a model cast as an electronic-repair expert to produce JSON-like steps, tacit operations/warnings/artifacts/tools, justifications, and confidence. It receives neither the LAG graph nor the OWL ontology, does not compute a graph gap, does not retrieve evidence, does not iterate, does not request an expert, does not validate JSON, and does not merge output into RDF. The confidence scale is prompted verbal calibration, with no empirical target.

This is best described as **structured model-prior completion**. It can nominate useful candidates; it cannot by itself distinguish a physically necessary hidden state from a common but inapplicable tool, an alternative valid procedure, a source-visible omission, or a hallucination.

### Configurations, repetition, scoring, and cost

The paper labels Gemini 3.1 Pro, Gemini 2.5 Flash, Claude Opus 4.6, GPT-5.2 Chat, and Gemma 4 31b-it; only Gemini receives direct video (Table 2, p. 10). All models receive the same prompt structure and source within modality. However, exact provider snapshots, dates, model IDs, decoding parameters, seeds, output caps for most providers, retries, invalid outputs, and selection rules are absent. Release adapters use provider defaults; Claude alone fixes `max_tokens=64000` and adaptive thinking. The configured model comments contain names that do not all match the paper exactly.

“Each experiment” is said to be repeated five times, with outputs “highly consistent” (p. 10), but the paper gives no unit count, per-run rows, seeds, variance, confidence intervals, paired tests, cluster treatment, or rule for combining runs. Figures report aggregate scores without exact denominators. Three videos, their operations, and repeated model calls are dependent clusters, not independent evidence for broad procedural transfer.

Cost is reported in dollars per video minute/hour (Table 3, p. 15), but token counts, video durations used in each aggregate, call counts, failed/retried calls, pricing date, local hardware/energy, Whisper cost, annotation/review labor, validation/storage, and human verification are omitted. Gemma is assigned $0 API fee, not zero compute cost. The cost table therefore estimates selected provider-call charges, not end-to-end knowledge-transfer cost.

## Evidence interpretation

### What is genuinely learned

1. **Representation constraints and knowledge authority are separable.** A graph can use only allowed predicates and still contain unsupported or contextually wrong assertions.
2. **Source modality is an intervention.** Video can expose entities absent from narration; transcript-only evaluation should record that evidence-view ceiling rather than calling omissions model failures without qualification.
3. **Model priors can act as candidate-recall amplifiers.** The enrichment prompt can propose reference-listed objects that source-only extraction misses. This can reduce expert search burden if proposals remain visibly unapproved.
4. **Entity recovery is a tractable low rung.** Tools/artifacts admit cleaner comparison than instruction quality, sequencing, rationale, thresholds, and execution—which the paper itself defers.
5. **A neuro-symbolic label does not imply symbolic enforcement.** The archived ontology and shapes constrain a prompt and provide potential validators, but the released execution path does not invoke them.

### Why the reported gains do not establish tacit knowledge

The enrichment's target is defined by reference membership. Consider the tweezers example (p. 13): the tool is visible in the video but absent from the quoted transcript. For a transcript-only model, predicting tweezers is an inference that happens to match multimodal evidence. It is not evidence that the tool was unarticulable, experience-based, necessary, uniquely appropriate, or newly elicited from the technician. It is **cross-view recovery via model prior**.

Other proposed additions can be still weaker. “Align the bracket so that its screw holes line up” (pp. 13–14) is plausible procedural completion, but the paper supplies no expert disposition, alternative method, tolerance, failure consequence, or execution test. A high entity F1 does not validate inferred operations, warnings, specifications, causal ordering, or novice-facing instruction quality.

The perfect post-enrichment precision is especially underdetermined. If the reference enumerates visible tools/artifacts and matching accepts any reference member attached to an operation, a model can improve by guessing common repair objects. Without false-candidate rows, operation-level counts, and blinded adjudication, one cannot tell whether constraints suppress hallucination, the small reference is permissive, outputs were normalized or selected, or five-run variability was collapsed favorably.

## Unique insight

> **Tacit-knowledge extraction must be evaluated as authority-preserving proposition promotion, not as reference-relative completion. A model-generated missing element is a candidate whose evidentiary status is “proposed from prior,” even when it matches a video annotation; ontology conformance and entity recall do not upgrade its authorship.**

For `skill-bench`, each proposed primitive should preserve at least:

```yaml
candidate_claim:
  proposition: "Tweezers are required to position this bracket"
  source_view: transcript_only
  source_locator: "435.58–459.38 s"
  observation_status: absent_from_view
  derivation: model_prior_completion
  model_and_prompt_hash: ...
  reference_match:
    status: matched
    reference_authority: video_annotation
    match_rule: ...
  modality_corroboration:
    status: visible_in_video
    locator: ...
  necessity: unknown
  alternatives: []
  expert_disposition: unreviewed
  applicability: unresolved
  consequence_evidence: none
  projection_status: candidate_only
```

The important distinction is between **existence**, **use in this demonstration**, **requirement**, **appropriateness**, and **decision consequence**. A visible tool establishes existence/use; it does not establish that every competent execution requires it. A model's justification is evidence about the model's prior, not the expert's rationale. Confidence generated in the same call is not calibrated correctness.

A second insight is that evaluation should cross source view and authority intervention. A useful factorial would compare transcript-only, video-only, transcript+video, model-prior completion, and expert-clarified completion on frozen claims. Outcomes should separate candidate recall, unsupported additions, expert acceptance, necessity/alternative classification, instruction fidelity, execution success, safety defects, and review minutes. This identifies whether model priors reduce elicitation burden without silently manufacturing obligations.

## Relation to adjacent evidence

- **Industrial expertise codification:** two real Siemens experts supplied rules that improved five co-designed outputs, but criterion overlap bounded transfer. The present paper has a more inspectable ontology/prompt release but a weaker expertise channel: the model, not a documented expert elicitation, authors the “tacit” additions.
- **Laboratory workflow twins:** role-gated nulls prevent operators from asserting design knowledge they are not authorized to supply. The present enrichment does the opposite: it prompts a model to fill hidden states, then lacks a claim-level authority gate. The laboratory review's `unknown/pending convergence` treatment is safer than confidence-scored completion.
- **Video-derived action/context candidates:** visual anomalies can nominate interview targets but do not contain rationale or authority. Here a video reference can corroborate that a guessed tool appeared, but still cannot turn appearance into tacit necessity or expert judgment.
- **Organizational simulation:** planted-identifier recovery measures routing/coverage, not tacit expertise. Here reference-listed entity recovery likewise measures completion against planted/annotated entities, not semantic transfer. Both benefit from complete traces while requiring real authority and downstream validation for stronger claims.

Existing expertise-transfer, evidence-chain, participation, artifact-view admissibility, benchmark-bundle, metric-monitoring, task-health, and validity machinery already has homes for these distinctions. The gap is disciplined instantiation, not another source-specific schema.

## Limitations and validity threats

1. Three selected public repair videos are a tiny convenience sample and only a proxy for manufacturing.
2. Instructional demonstrations contain deliberately explicit teaching, unlike naturally tacit work.
3. Whisper model/configuration, ASR errors, and transcript corrections are undisclosed.
4. The expert pool's size, credentials, sampling, device authority, independence, and conflicts are absent.
5. Annotation instructions, raw labels, disagreements, adjudication, and exact counts are unreleased.
6. Operation boundaries and entity matching/normalization are under-specified.
7. Entity precision/recall does not evaluate operation correctness, ordering, warnings, thresholds, rationale, or instruction utility.
8. “Tacit” combines video-visible-but-unspoken, common prior, physically necessary state, warning, affordance, and speculative completion.
9. No expert confirms that inferred additions reflect held knowledge or are necessary/applicable.
10. Model-generated justifications are not expert provenance.
11. Self-assigned confidence is uncalibrated and has no empirical target.
12. Active inference is prompt inspiration, not a formal active-inference model or iterative evidence-seeking process.
13. The active module does not consume the LAG KG/ontology, detect graph gaps, or merge output into RDF.
14. The released LAG runner does not execute RDF parsing, SHACL, global checks, or GraphDB loading claimed in the paper pipeline.
15. The prompt requests fenced Turtle while the runner writes raw output, creating an unhandled parse risk.
16. Structural ontology/SHACL conformance is not semantic correctness or procedural completeness.
17. Perfect precision is unauditable without raw predictions, counts, matching code, and invalid-run policy.
18. Five repeats have no disclosed rows, seeds, dispersion, uncertainty, or aggregation rule.
19. Video, operation, and repeated-call clustering is ignored.
20. Provider snapshots, decoding settings, retries, and exact configured-system identities are incomplete.
21. No no-ontology, schema-only, prompt-only, ordinary chain-of-thought, retrieval, or expert-clarification ablation isolates the claimed mechanisms.
22. Direct-video and transcript conditions differ in evidence availability and cannot identify model quality alone.
23. No held-out video, device family, repair type, instructor, camera style, ASR condition, or professional domain tests transfer.
24. No novice/agent uses the graph to execute a task; clarity, error, safety, time, retention, and correction burden are unmeasured.
25. The KnowledgeX manufacturing/AR application is illustrated, not evaluated with participants, outcomes, or comparison.
26. Cost omits local compute, ASR, validation, storage, annotation, expert verification, retries, and error consequences.
27. `$0` for Gemma means no API charge in the authors' setup, not zero resource cost.
28. No outputs, annotations, run manifests, metrics, analysis scripts, or paper-result ledger are released.
29. The timing-appropriate commit is not proven byte-identical to paper runs.
30. “Semantic quality,” “real-world knowledge transfer,” and practical feasibility exceed the measured construct.

## Reproducibility and operational realism

Manuscript inspectability is moderate: immutable PDF/text/source, three source URLs, model labels, prompts, ontology, shapes, one complete transcript, one fragment, provider adapters, and cost/F1 figures are preserved. The repository's small 22-file surface is fully auditable, and the paper candidly identifies the active-inference analogy and defers user validation.

Exact reproduction is poor. The release lacks two transcripts/videos as frozen inputs, annotations, outputs, repeats, run IDs, provider dates/snapshots, request settings, validation/store code, scoring/matching code, cost ledger, and analysis artifacts. The archived code demonstrates how to make one paid call and save output, not how to reconstruct a paper row. No result can be replayed offline.

Operational realism is low for knowledge transfer and moderate for candidate-generation research. Public repair videos contain real fine-grained manipulations and safety constraints; ontology source locators and multimodal comparisons are useful. But there is no authenticated expert elicitation, live industrial observation, versioned procedure authority, alternative-path adjudication, human review workflow, recipient, execution, maintenance, privacy/access control, or measured consequence. The real manufacturing and AR figures are project context, not outcome evidence.

## Transfer to skill-bench

### Retain

1. Separate source-grounded observations from inferred additions at proposition level.
2. Preserve source modality and exact locators; missingness under transcript-only access is not missingness under video access.
3. Use ontology/schema checks as structural gates while keeping semantic correctness and authority separate.
4. Treat model-prior completion as a candidate-recall intervention that may lower expert review burden.
5. Score discrete entity recovery only as one low-rung diagnostic, not as overall procedural or semantic quality.

### Repair before reuse

1. Freeze reference annotations, counts, matching rules, raw predictions, repeats, and configured-system identities.
2. Give every inferred claim a derivation type: observed, stated, ontology-entailed, model-prior-proposed, analyst-inferred, expert-corrected, or independently corroborated.
3. Require qualified expert disposition for necessity, alternatives, applicability, exception, and consequence before promotion into a task requirement or hidden check.
4. Cross evidence views and interventions: transcript/video/both × no completion/model completion/expert clarification.
5. Evaluate proposition-level precision/recall, expert acceptance, review burden, instruction fidelity, execution success, safety, and downstream artifact consequence separately.
6. Fail closed when RDF/JSON parsing, SHACL, global sequence checks, evidence locators, or authority reviews are absent; preserve invalid outputs rather than silently selecting a valid run.
7. Keep model confidence as an uncalibrated proposal feature unless validated against held-out expert dispositions and outcomes.

### Do not infer

Do not infer that a source-visible but unspoken tool is tacit expertise, that a reference-matching guess is expert-authored, that schema compliance is semantic validity, that entity F1 measures procedure quality, that a generated justification is rationale evidence, or that three repair videos establish manufacturing or cross-domain transfer.

## Concrete repository actions

1. **Index this review as expertise-representation and proxy-validity evidence.** Update `data/papers/index.json` from awaiting review to deep release audit, preserving the paper/release timing boundary and exact review path.
2. **Add no build or consolidation task.** The paper exercises obligations already represented by provenance/derivation, evidence-view admissibility, participation/authority, expertise-transfer, metric, task-health, and validity contracts. A new schema would duplicate mature machinery.
3. **Use the next real consented expertise pilot as the validation gate.** If video/transcript evidence is available, compare model-prior proposals with expert clarification and record acceptance, alternatives, correction burden, and downstream consequence. Do not simulate testimony or unblock the elicitation-session contract with this paper.

## Claim boundary

The source supports a promising ontology-shaped candidate extraction pattern and manuscript-reported evidence that a second model-prior prompt can recover many tool/artifact labels absent from a first-pass representation. The complete official release confirms prompts, a procedural ontology, SHACL shapes, provider adapters, one transcript, and one enrichment fragment.

It does not show that the archived runner enforces its symbolic validators, that scores are reproducible, that inferred additions are tacit or expert-authorized, that graph instructions are semantically correct or useful, that confidence is calibrated, that novices perform better, or that the method transfers to manufacturing. For `skill-bench`, the correct transfer is an authority-preserving candidate-promotion ladder—not automated conversion of plausible completions into benchmark truth.
