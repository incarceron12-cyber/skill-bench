# Context-mediated domain adaptation: edit capture is not yet tacit-expertise transfer

## Source and review status

**Deep review of the complete immutable arXiv v2 paper plus a release audit.** I read the full 34-page paper, including its exact generation and extraction prompts, implementation, sequential five-participant study, results, limitations, and references. I also compared the v1/v2 source trees and audited the complete author-linked OSF view-only snapshot available on 16 July 2026.

- **Paper:** Anton Wolter, Leon Haag, Vaishali Dhanoa, and Niklas Elmqvist, *Context-Mediated Domain Adaptation in Multi-Agent Sensemaking Systems*, arXiv:2603.24858v2, DOI `10.1145/3812772`, <https://arxiv.org/abs/2603.24858v2>
- **Local PDF:** `data/papers/pdfs/2603.24858v2-context-mediated-domain-adaptation.pdf` (34 pages; SHA-256 `64a8eaf8157bda6a68c9ee1278f0c5da9a79b16af084ec11fbb1acac993b4d01`)
- **Local text:** `data/papers/text/2603.24858v2-context-mediated-domain-adaptation.txt` (SHA-256 `7cc14f90a86bad0d41347289111c8e79d6d6c30f63b0abb13d2e818dc5e40084`)
- **Prior version:** `data/papers/pdfs/2603.24858v1-context-mediated-domain-adaptation.pdf` and `data/papers/text/2603.24858v1-context-mediated-domain-adaptation.txt`
- **Acquisition and release provenance:** `data/sources/releases/2603.24858v2-context-mediated-domain-adaptation/provenance.json`
- **OSF snapshot inventory:** `data/sources/releases/2603.24858v2-context-mediated-domain-adaptation/osf-file-inventory.json`
- **Author-linked project:** <https://osf.io/84f3s/overview?view_only=6b4f191fa0d341c4803bf53d3229e3fd>

The arXiv metadata contains no withdrawal notice. Source-level comparison found no substantive method, result, or limitation change from v1 to v2; v2 updates publication metadata, citations/formatting, and image encodings. The OSF node reports pre-v1 modification dates, but it is private, view-only, and not a frozen registration. Its current 15-file state is therefore a timestamped release snapshot, not an immutable paper-time revision.

The snapshot contains nine CSV tables, two SQL schema files, and four result figures. It does **not** contain the complete application, executable analysis scripts promised on p. 23, Langfuse traces, exact study instructions/protocol, think-aloud transcripts or coding records, model configuration, consent text, extraction-validation judgments, or a data dictionary. Raw participant tables remain local and untracked because stable pseudonymous IDs are combined with age, job, experience, and research-background fields and the view-only materials do not establish redistribution permission.

## One-sentence contribution

The paper contributes a useful engineering pattern—preserve an AI artifact's initial state, user-modified state, interaction type, and source links; ask a model to propose reusable context; inject that context into later generation—but its five-person fixed-order study and current release establish only **edit capture, model-generated candidate-knowledge storage, and temporal eligibility for later use**, not correct tacit-knowledge extraction, contributor approval, semantic adoption, quality improvement, cross-user transfer, or professional utility.

## Why this matters to `skill-bench`

This review advances charter objectives A, B, and C by auditing a distinct expertise-to-evaluation pathway:

```text
expert edits an AI artifact
→ system interprets the delta as a reusable proposition
→ proposition enters shared context
→ later configured system may change behavior
→ later artifact may improve
```

The concrete evidence is an immutable-paper and release-level reconstruction of that chain. The uncertainty clarified is where an edit-derived record changes status from observed delta, to model interpretation, to contributor-authorized domain claim, to promoted intervention, to adopted guidance, to validated downstream effect. This is narrow methodological expansion; visualization research-question generation is a case, not a scope boundary. Useful completion is a stricter claim ladder and matched test design, not a new edit-memory subsystem.

## Research questions and contribution boundary

The paper asks how user modifications can be captured and transformed into reusable domain knowledge (RQ1), how expertise can propagate bidirectionally between edits and agent reasoning (RQ2), and whether accumulated knowledge improves later generation quality and reduces correction effort (RQ3; pp. 3–4).

It contributes:

1. **BDAR**, a before/after artifact representation with generation and modification metadata (pp. 7–8);
2. **ACO**, a shared context object whose entries are classified as terminology evolution, methodological refinement, or conceptual-depth change (pp. 7–9);
3. three interaction modes—direct manipulation, prompt-based regeneration, and context-based generation (pp. 8, 10–13);
4. an asynchronous Next.js/FastAPI/LangGraph/PostgreSQL prototype with edit, task, and provenance tables (pp. 9–22);
5. exact generation and extraction prompt templates (pp. 17–20); and
6. an exploratory fixed-order study of five visualization-literacy researchers editing research questions for three papers (pp. 22–32).

The strongest defensible claim is:

> Seedentia stored initial/final text states and interaction records, and Gemini 2.0 Flash Lite generated human-readable candidate context entries linked to source question IDs in one small sequential study.

The evidence does not establish that the entries encode tacit rather than explicit or model-supplied knowledge; are factually correct, scoped, novel, or contributor-approved; were actually present in every claimed later prompt; were noticed or semantically adopted by the generator; caused later output differences; improved artifacts; reduced burden; transfer across people or tasks; remain valid over time; preserve participant permissions; or substitute for expert judgment.

## Methodology and system reconstruction

### Participants, task, and sequence

Five PhD students/postdoctoral or research staff with self-reported visualization-related backgrounds and one to nine years of experience participated (p. 22). The released participant table records all five `expertise_verification_status` values as `pending`; credentials or task-specific performance were not independently validated. “Domain expert” is therefore a recruitment characterization, not an audited claim-specific authority state.

Each participant processed three recent visualization-literacy papers. For each paper, the system generated three research questions plus contribution summaries from title, abstract, full text, generic question-writing guidance, and—after participant 1—accumulated prior entries. Participants rated each question from 1 to 5 before editing, then used direct edits or prompt regeneration until satisfied. Sessions reportedly lasted approximately 45–60 minutes and encouraged think-aloud commentary (pp. 23–24).

The design is a single fixed accumulation sequence: P1 receives no prior entries; P2 receives P1's entries; and so on. It also allows within-participant accumulation across papers. Paper order was reportedly randomized “where feasible” (p. 24), but the release's `paper_order` field is empty for all 26 session rows, and no randomization seed or assignment record is available. Participant identity, order, accumulated context volume/content, calendar time, paper, familiarity, and treatment are therefore entangled.

### Edit/event capture

The database design usefully separates:

- `evaluation_research_questions`: initial/current question and contribution, character/word edit distances, finalization, quality rating, and extraction status;
- `ai_entity_edits`: direct edit, prompt modification, regeneration, or quality-rating event, with original/new values and optional user prompt;
- `implicit_domain_knowledge`: candidate text, one category, and source-question IDs;
- `evaluation_sessions`: participant, state/context snapshots, metrics, trace ID, and status; and
- task/log tables for attempts, errors, API calls, and workflow execution (pp. 14–21; released SQL schemas).

This is a valuable **potential** lineage. The released realization is much thinner. `entity_metadata_id` is empty in all 97 edit rows; all 26 released session rows lack `agent_context_snapshots`, `metrics_snapshot`, `edit_distance_score`, `semantic_similarity_score`, `langfuse_trace_id`, `actual_duration`, and `paper_order`; 10 of 26 sessions are not finalized; and only 16 have an `agent_task_id`. The released data preserve artifact deltas and source IDs, but not the executed prompt/context/traces needed to prove downstream presentation or adoption.

### Candidate extraction

Whenever question generation begins, the pipeline processes unprocessed final-versus-initial pairs. Gemini is prompted as an “expert in Visualization Literacy research,” shown the before/after question and contribution, optionally shown existing entries, and instructed to return zero to three actionable insights under the three predefined categories, avoiding minor rewording and duplicates (pp. 19–20).

This is not a neutral decoder of participant intent. The extractor is supplied:

- an expert role;
- a fixed ontology;
- examples of the desired kind of generalization;
- an actionability objective for future generation;
- an instruction to infer significance and deduplicate; and
- only endpoints, not the participant's reason for editing, alternatives considered, or think-aloud evidence.

The resulting entry can therefore mix observed delta, prompt-induced interpretation, model prior, and analyst ontology. For example, deleting a word is interpreted in the paper as a preference for concise domain discourse, while adding physiological signals is expanded into possible biofeedback and real-time monitoring (pp. 27–29). Those are plausible hypotheses, not entailed domain claims. No participant acceptance/correction UI or independent expert validation of the extracted proposition is reported.

### Promotion, retrieval, and generation

All extracted entries appear to be immediately available as shared generation context. User-specific knowledge is theoretically said to take precedence over project and global context (p. 7), but the exact selection, ranking, token limit, conflict rule, consolidation algorithm, validity time, and rejection/rollback behavior are not specified. The generation prompt tells the model to “learn from” accumulated expansion, refinement, and condensation patterns (pp. 17–18).

That establishes an intended injection mechanism, not realized use. The current release has no executed generation prompts, context snapshots, selected-entry ledger, model outputs tied to entry exposure, or counterfactual generations. A source link from an entry to an edit supports backward provenance; it does not support forward evidence that the entry was retrieved, presented, adopted, or causally useful.

## Evidence

### Paper-reported observations

The paper reports 47 refined questions and 46 extracted entries across five participants (p. 24), distributed as 26 conceptual-depth, 10 terminology, and 10 methodological entries (Table 6, p. 27). It reports baseline ratings that are generally higher for P4/P5 than P1, shorter selected session durations for later participants, non-monotonic edit distance, and no observed saturation. The authors explicitly acknowledge that `n=5`, participant differences, paper difficulty, familiarity, interruptions, and absence of a control condition preclude causal attribution (pp. 24–25, 29–32).

The four stated hypotheses do not form a coherent success pattern (p. 30):

- decreasing edit distance was not observed uniformly;
- decreasing time was described as consistent, but timing was secondary and confounded;
- increasing ratings were observed descriptively, without a baseline/control;
- saturation was not observed.

These results demonstrate that people used the interface and that the extractor produced records. They do not validate RQ3.

### Release audit

The OSF snapshot permits useful integrity checks but does not reproduce the manuscript exactly:

- it contains **48** finalized question rows (16 three-question sessions), not 47;
- it contains **47** candidate-knowledge rows, not 46;
- the extra released entry makes P5's count 2 rather than Table 6's 1 and conceptual-depth count 27 rather than 26;
- all 47 entries have one valid source-question link and no exact duplicate text;
- 45 of 48 question rows are marked `knowledge_extracted=true`;
- the event table contains 27 direct edits and 9 prompt modifications, matching the per-session counts in Table 4 but not the narrative's “28” and “7” (p. 25);
- the paper calls `0.78` a “slope” on p. 26 and a “correlation” on p. 31 without defining the regression unit or releasing analysis code. Recomputing from Table 6's five participant-level edited-field/entry pairs gives an OLS slope of about `0.751`, Pearson `r≈0.559`, and `R²≈0.313`, so the published `0.78` is not recoverable from that table alone; and
- 26 session rows include questionnaire/abandoned or otherwise non-question sessions alongside the 16 question-generation sessions. Null `questions_count` rows have extreme elapsed durations in the derived participation table, illustrating why row eligibility must be explicit.

These discrepancies may reflect a snapshot taken after the manuscript analysis, a different eligibility filter, or reporting defects. Because the OSF node is not registered and no analysis script/data dictionary is present, the review cannot adjudicate which. They weaken release correspondence; they do not imply misconduct or invalidate the narrower capture-feasibility claim.

### What is and is not observed

| Chain link | Evidence status |
|---|---|
| Participant made a direct edit or requested regeneration | Supported by released event and before/after records, with some missing metadata |
| Delta was linked to a source question | Supported for all 47 released candidate entries |
| Model produced a categorized candidate proposition | Supported by stored rows and disclosed extraction prompt |
| Candidate proposition matches participant intent | Not tested; no contributor review or think-aloud linkage |
| Candidate is factually/ professionally authoritative | Not tested; extractor role prompt and participant label provide no authority inheritance |
| Candidate was promoted under a validation rule | No separate promotion gate; apparent immediate storage/use |
| Candidate was selected and delivered in a later generation | Intended by design; executed prompt/context evidence is absent from release |
| Generator adopted the candidate semantically | Not observed |
| Candidate caused a later behavior/output difference | Not identified; no matched no-entry or shuffled-entry condition |
| Later artifact quality improved | Not identified; different participants self-rate different generated questions in fixed order |
| Cross-user/domain transport or lasting utility | Not tested |

## Unique insight

The paper's deepest transferable contribution is the **edit-to-claim boundary**. Before/after artifact states are high-value evidence because they capture what an expert actually changed without demanding a complete verbal specification. But an edit is not self-interpreting. The correct unit is:

```text
artifact/version and contributor authority
→ edit event and interaction mode
→ exact delta
→ participant rationale, if available
→ one or more model/analyst interpretations
→ contributor acceptance, correction, rejection, or unresolved status
→ source/corroboration, scope, valid time, contradiction, and allowed use
→ independent promotion decision
→ retrieval opportunity and selected delivered context
→ recipient/model receipt, adoption, or justified rejection
→ changed reasoning/action/artifact
→ independently measured consequence, burden, and transport
```

No arrow inherits the status of the previous one. A participant-authored delta can yield a model-authored interpretation; provenance to the delta does not make that interpretation expert-approved. A stored interpretation can be eligible for retrieval without being delivered. Delivered text can change lexical output without transferring a valid procedure or improving professional quality.

A second insight is that **interaction mode is part of evidence authority**. A direct edit originates in participant action but may encode style, local preference, factual correction, experimentation, or mere deletion. A prompt-regenerated final state is jointly produced by participant instruction and another model call; treating the entire output delta as participant knowledge launders model-added content into expertise. Context-based generation is later-system output, not new expert evidence at all. These modes need different transformation and approval semantics.

A third insight is that sequential accumulation requires two denominators:

1. **capture denominator:** eligible edits, attempted extractions, empty/failed outputs, accepted/rejected/corrected candidates, and retained propositions;
2. **use denominator:** later decision opportunities, selected/delivered propositions, inspected/adopted/rejected propositions, relevant changes, improvements/regressions, and expired or contradictory entries.

Counting 46 or 47 stored entries reports only one numerator in the first denominator. It says nothing about correctness or value.

## Relation to existing evidence and machinery

- **Data Therapist** shows that an AI elicitor changes the distribution of testimony; this paper adds a post-artifact route where a model changes the interpretation of an edit. Both require spontaneous/probed/model-inferred status and contributor correction rather than “verification” by role prompt.
- **Laboratory workflow twins** supplies claim-level role authority and mandatory nulls. Here, five participants' broad expert label and Gemini's “expert” system prompt cannot authorize every generalized methodological or conceptual claim.
- **AFTER** supplies immutable candidate/version/promotion/rollback and typed transfer-edge logic. Seedentia stores flat entries with no independent promotion, held-out validation, branch, expiry, or rollback evidence.
- **AgencyBench** separates evaluator-disclosed repair from unaided capability. Analogously, later Seedentia generation under injected candidate context is a configured intervention, not proof that the base system learned or that an expert procedure transferred.
- **Networked Intelligence** separates storage/routing from receipt, adoption, decision change, and consequence. Seedentia's source-question links and intended prompt injection stop before those latter states.

Existing `expertise-transfer`, `expert-participation`, `compounding-lessons`, configured-system, longitudinal-stream, evidence-state, metric, task-health, and validity-argument records can carry these requirements. The blocked `build-elicitation-session-contract` already calls for spontaneous/probed/inferred status and must remain blocked until a consented real contribution exists. No parallel edit-memory schema is warranted.

## Limitations and validity threats

1. **Five-person fixed sequence:** participant, calendar order, accumulated context, and treatment are inseparable.
2. **No control or counterfactual generation:** there is no no-context, shuffled/irrelevant-context, raw-delta, accepted-entry, or explicit-guidance comparison.
3. **Different people rate different outputs:** higher later self-ratings are not within-rater artifact comparisons or independent quality judgments.
4. **Self-rating after generation only:** the instrument does not compare initial and final quality under a common rater, blind independent experts, or a downstream criterion.
5. **Expertise is not claim-specific:** participant credentials/performance are not audited; released verification status remains pending.
6. **Prompt regeneration confounds authorship:** model-produced changes can be treated as evidence of participant expertise.
7. **Endpoint deltas omit rationale:** intent, rejected alternatives, uncertainty, and local context are absent from extraction input.
8. **Extractor priors shape the result:** expert role, fixed taxonomy, examples, and actionability instructions encourage broad generalization.
9. **No extraction-validity study:** no independent labels, participant acceptance, agreement, factual verification, false-positive/negative audit, or repeated extraction reliability.
10. **Immediate promotion:** no typed candidate/quarantine state, authority gate, held-out validation, contradiction adjudication, expiry, or rollback is demonstrated.
11. **Deduplication is unspecified:** “intelligent” consolidation has no similarity threshold, merge semantics, uncertainty, or false-merge audit.
12. **Forward provenance is absent:** source links exist, but selected context, exact delivered prompt, receipt, adoption, and causal output effects are unreleased.
13. **No model pin:** “Gemini 2.0 Flash Lite” lacks exact endpoint/date, decoding parameters, retry policy, and executed call records.
14. **No repeated generations:** stochastic extraction/generation reliability and category stability are unknown.
15. **Order and paper assignment are unavailable:** the released `paper_order` field is empty and no randomization record exists.
16. **Timing is not comparable:** interruptions, familiarity, lack of speed incentive, and derived null-session rows make duration a weak burden measure.
17. **Edit distance is not quality:** deeper editing can indicate worse baselines, greater expertise, changing ambition, or engagement.
18. **Entry count is not knowledge:** extraction volume can rise mechanically with edits and model verbosity.
19. **Published/released count drift:** 47/46 question and 47/46 entry boundaries plus interaction-count discrepancies lack a reproducible eligibility rule.
20. **Undefined `0.78`:** “slope” and “correlation” are used inconsistently and cannot be recovered from the displayed participant table.
21. **No long-term state evidence:** retention, drift, contradiction, revocation, forgetting, and stale-domain behavior are untested.
22. **No cross-task/domain transfer:** all work is visualization-literacy research-question generation from three papers.
23. **No professional consequence:** longer or more conceptually elaborate questions are not shown to be novel, feasible, useful, adopted, or scientifically valuable.
24. **Operational claims overreach:** “production-ready,” “privacy-preserving,” “full reproducibility,” and automatic cross-domain scalability are not supported by released code, access-policy tests, traces, or deployments (pp. 9, 21, 31).
25. **Consent/use boundary is incomplete:** timestamps and broad booleans exist, but consent text, transformation comprehension, shared-context permission, withdrawal propagation, and redistribution basis are unavailable.
26. **Burden is undermeasured:** no workload, correction effort for extracted entries, trust calibration, privacy concern, refusal, dropout, or maintenance labor is reported.
27. **Release is partial and mutable:** the current OSF snapshot is useful but omits the promised analysis code and core executed-system evidence and is not a frozen registration.

## Reproducibility and operational realism

Operational realism is **moderate for interaction capture and low for validated adaptation**. Direct editing, prompt regeneration, asynchronous processing, persistent shared state, retries, source-linked records, and cross-session accumulation resemble real collaborative systems. The study also surfaces a realistic tension: later users may edit more because better scaffolds support deeper work, so “less editing” is not necessarily the right objective.

Reproducibility is **moderate for paper/release descriptive counts and poor for the claimed adaptation mechanism**. A third party can inspect questions, deltas, ratings, candidate entries, event counts, and schemas. They cannot replay extraction or generation, reconstruct exact delivered contexts, reproduce published filtering, validate qualitative coding, or estimate effects. Exact reproduction would require immutable code/container/model manifests; participant/order/paper assignment; executed prompts and responses; retry/invalid logs; candidate and deduplication events; contributor review; context-selection and delivery logs; frozen pre-generation state; all raw outcomes; and executable analysis with explicit eligibility rules.

## Claim ladder

| Claim | Status from this source | Evidence needed for promotion |
|---|---|---|
| Initial/final artifact states and edit events can be stored | Supported in one text prototype | Replay/conformance tests across artifact types and failure cases |
| A model can generate candidate reusable propositions from deltas | Supported | Repeated extraction records and explicit candidate status |
| Candidates faithfully represent participant intent | Unsupported | Blind participant acceptance/correction plus rationale-linked adjudication |
| Candidates are valid domain knowledge | Unsupported | Claim-specific authority, sources/corroboration, scope/time, disagreement and independent expert review |
| Candidate context reaches later generation | Intended, not auditable from release | Exact selected-entry and executed-prompt/context logs |
| Later model adopts the proposition | Unsupported | Proposition-level output/trace evidence and justified rejection semantics |
| Candidate context causes changed behavior | Unsupported | Frozen-state matched no/raw/accepted/shuffled-context interventions |
| Edit-derived context improves artifact quality | Unsupported | Blind independent artifact judgment or consequential checks with paired uncertainty |
| The method transfers knowledge across users | Unsupported; fixed order bundles user and treatment | Counterbalanced/crossover users with accepted entries and recipient-state controls |
| The method extracts tacit expertise | Unsupported | Unprompted/probed/explicit/model-inferred distinctions, novice/expert contrasts, contributor validation |
| The system reduces expert burden | Unsupported | Total capture, review, correction, maintenance, privacy, and downstream-use time/cost |
| The method generalizes across tasks/domains | Untested | Multiple materially different artifacts/domains with transport and harm/non-inferiority tests |
| The system is privacy-preserving or production-ready | Unsupported | Purpose/consent/access/deletion audits, threat model, operational reliability and deployment evidence |

## Transfer to `skill-bench`

### Retain

1. Preserve initial and final native artifact versions rather than only a final prose claim.
2. Record edit type, field, timestamp, source artifact, prompt instruction, and generation context separately.
3. Keep source links from every interpreted proposition back to exact deltas.
4. Separate persistent domain context from task-specific procedure and configured-system identity.
5. Treat later context exposure as an explicit intervention and measure both quality and correction burden.

### Repair before reuse

1. Type the interpretation author: `participant_stated`, `participant_direct_edit`, `participant_prompt_intent`, `model_generated_delta`, `model_inferred`, or `analyst_inferred`.
2. Keep raw delta, candidate interpretation, contributor response, and promoted proposition as immutable distinct objects; authority must not propagate across transformation.
3. Require contributor correction/acceptance plus scope, valid time, applicability, confidence, allowed use, and withdrawal behavior before calling an entry expert-approved.
4. Quarantine candidates until independent validation; preserve contradictions and alternatives rather than silently deduplicating them.
5. Record opportunity, selection, delivery, receipt, adoption/rejection, decision/artifact change, and consequence separately.
6. Use blind, counterbalanced, frozen-state comparisons with no context, raw delta, contributor-approved proposition, irrelevant/shuffled proposition, and explicit public guidance.
7. Measure false promotions, missed knowledge, regression/harm, burden, maintenance, and privacy—not only entry count, length, ratings, and edit distance.

## Concrete repository actions

1. **No new queue task.** Existing expertise-transfer, participation, candidate-lesson, longitudinal, configured-system, metric, and validity machinery already covers the identified requirements; another schema would duplicate them.
2. **Keep the elicitation-session contract blocked.** When a consented real contribution eventually exercises the existing template, include one direct-edit event and preserve raw delta → candidate interpretations → contributor correction/approval. Do not simulate testimony to unblock it.
3. **For a future bounded validation, use a small factorial rather than another uncontrolled accumulation sequence:** `no context / raw edit delta / model interpretation / contributor-approved interpretation / shuffled interpretation`, with frozen recipient state, counterbalanced order, exact context-delivery logs, blind artifact evaluation, and total contributor review burden. The licensed result should remain an edit-derived context intervention effect until cross-user, cross-task, and professional consequences are directly tested.

## Bottom line

Seedentia demonstrates a promising capture interface and a useful provenance skeleton. Its genuinely novel benchmark lesson is negative but constructive: **an expert edit is strong source evidence and weak interpreted-claim evidence**. The model that explains the edit is another contributor to the chain, not a transparent extractor of tacit knowledge. `skill-bench` should retain before/after artifacts and edit provenance, but require explicit transformation authorship, contributor review, promotion controls, delivery/adoption evidence, matched downstream effects, and burden/privacy accounting before promoting edit capture into expertise-transfer claims.