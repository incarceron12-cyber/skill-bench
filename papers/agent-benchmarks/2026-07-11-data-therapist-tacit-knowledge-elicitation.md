# Paper Review: Data Therapist — More Elicitation Yield Is Not More Valid Expert Knowledge

- **Paper:** https://arxiv.org/abs/2505.00455v3
- **Authors:** Sungbok Shin, Hyeon Jeon, Sanghyun Hong, and Niklas Elmqvist
- **Date read:** 2026-07-10
- **Venue / source:** CHI 2026 manuscript; immutable arXiv preprint v3
- **Tags:** expertise-elicitation, mixed-initiative-systems, tacit-knowledge, dataset-documentation, prompt-effects, expert-disagreement, provenance
- **Local PDF:** `data/papers/pdfs/2505.00455v3-data-therapist-eliciting-domain-knowledge-from-sub.pdf` (23 pages; SHA-256 `277ed7549798385fda59bf0ed4f82f4ff6e53a1de657cba5b3c6cedea10eceaf`)
- **Local text:** `data/papers/text/2505.00455v3-data-therapist-eliciting-domain-knowledge-from-sub.txt` (SHA-256 `7b3e3913f6215e63346b2c90760fbaad5b97ad562bbf202759968ea571d5cb51`)
- **Official materials inspected:** paper-linked OSF node https://osf.io/e4fxu/ via its disclosed view-only link; local archive and provenance at `data/sources/releases/2505.00455v3-data-therapist/provenance.json`

## One-sentence contribution

Data Therapist demonstrates a plausible mixed-initiative interface in which an LLM turns tabular data, predefined dataset-documentation questions, and prior expert annotations into selectable follow-up probes and multigranular annotations, but its six-person, expert-confounded comparison measures annotation production and perceived knowledge difficulty—not capture fidelity, downstream benchmark utility, or superiority to human elicitation—and its own results expose specialization-conditioned disagreement and probe-shaped coverage as the central validity problems.

## Why this matters for skill-bench

This review advances charter objectives A, B, and F by testing an AI-assisted front end for converting domain expertise into structured records. The general cross-domain hypothesis is: **LLM-generated probes can increase the number and topical breadth of candidate expert statements, but those statements become benchmark evidence only when probe provenance, expert correction, contextual scope, corroboration, transformation lineage, and downstream utility are separately established.** Accounting, political science, and usable security are methodological cases, not a proposal to narrow `skill-bench` to datasets or visualization.

The paper adds something genuinely different from the existing ACTA/CDM review. ACTA starts from tasks and critical incidents and asks for cues, strategies, thresholds, novice contrasts, and counterfactuals. Data Therapist starts from a dataset and alternates between expert-initiated annotation and machine-initiated questions tied to the whole table or selected cells. That interaction can reveal data provenance, collection, interpretation, limitations, and intended use without requiring a skilled interviewer at every moment. It also makes the elicitation instrument an observable treatment: which questions were generated, prioritized, displayed, deleted, answered, rejected, revised, or never offered affects what “expert knowledge” exists in the resulting record.

The concrete artifact is this paper-and-release audit and its elicitation-event crosswalk. It clarifies that annotation count, question difficulty, topic overlap, and professional authority are different estimands. Useful transfer means the next real elicitation session preserves those distinctions and does not unblock the pending elicitation-session contract or manufacture expert validation from this study.

## Research question and claim boundary

The paper asks whether an LLM-guided, mixed-initiative system can help domain experts externalize tacit context around data and how its annotations differ from those produced with a human interviewer (Abstract; Sections 1 and 5, pp. 2–3, 15–17). The system is intended to bridge reality and representation, support table/row/column/cell annotations, enable lightweight analysis, check response quality and contradiction, show progress, and broaden coverage (Section 3, pp. 6–8).

The evidence supports bounded claims that:

- six participants could use the deployed interface for 45-minute annotation sessions;
- LLM and predefined questions elicited a substantial fraction of annotations in the three reported pairs;
- the two experts within a domain often supplied non-overlapping topics, especially when political-science regional specializations differed;
- the released materials contain real study datasets, 155 labeled expert-response rows, prompt prose, and topic-similarity labels; and
- LLM-prompted answers were, on the reported difficulty scale, mostly about concepts above lay level but below the most specialized human-authored material (Sections 6.1–6.3, pp. 17–20).

It does **not** establish that more annotations are more complete or accurate, that the LLM elicited tacit rather than readily verbalized knowledge, that its relevance/contradiction checks were correct, that it reduced participant burden, that condition differences were caused by the tool, that its structured knowledge base improved a visualization or benchmark, or that the method generalizes across experts, datasets, tasks, or professions.

## Methodology

### System and elicitation loop

The client–server web application presents four coupled views: a scrollable spreadsheet, simple histogram/scatterplot analysis with cross-filtering, a question list, and an annotation list. Experts can contribute in three modes (Sections 4.1–4.5, pp. 8–10):

1. **general annotation** applying to the dataset;
2. **data-specific annotation** attached to a row, column, cell, or selected region; or
3. **question answer** responding to a machine- or framework-generated probe.

The paper says annotations can be reviewed and edited, the latest annotated dataset is continuously saved, and annotations can be exported as JSON. Figure 4 shows fields such as question, `Made by DT`, response, and location. It does not describe immutable edit history, deletion/withdrawal semantics, correction lineage, or stable row identity after sorting/version changes.

On upload, the backend generates 30 questions from the tabular dataset. Each new annotation generates five more; falling below ten queued questions triggers ten additional questions. Ten are displayed at once, initially split evenly between LLM-generated questions and predefined questions based on the seven Datasheets genres—**motivation, composition, collection process, preprocessing, uses, distribution, and maintenance** (Sections 2.2 and 4.6, pp. 4, 11–12). Experts may answer or delete displayed questions. Question priority sums integer 1–5 scores for originality, recency, and LLM-rated importance; ties are random. Predefined questions are balanced toward themes with more unanswered items.

Answers pass two model-mediated checks: whether the answer addresses the question and whether it contradicts prior annotations. A failed relevance check returns feedback and invites revision (Figure 3, pp. 10–11). The paper calls this verification, but the released prompt only asks whether an answer “appropriately addresses” the question. It does not check factual support, source authority, uncertainty, or whether the question's presupposition is valid. The contradiction prompt compares text against previous records but has no temporal, scope, authority, or conditional-applicability model.

The paper's model description is internally time-varying. The introduction says GPT-4; the implementation specifies OpenAI `o1` for initial question generation and GPT-4o for all other calls (Section 4.8, p. 14). No exact snapshots, API dates, decoding parameters, retrieval corpus, retry policy, prompt hashes, or call logs are supplied. “Built-in RAG” is mentioned for initial questions without identifying retrievable sources (Section 4.7, p. 13).

### Released prompt and artifact inspection

The paper-linked OSF snapshot materially improves inspection. The September 2025 ZIP contains all three input datasets, one merged response/coding CSV per domain, and the prompt/pseudocode file. The latter confirms that the whole dataset, all prior questions/annotations, and most recent selected data/annotation can enter later prompts. It also confirms that “importance” is delegated to the LLM and that contradiction output is only a proposed alert plus conflicting text records. This creates a path-dependent elicitation process: early annotations alter later candidate questions, and question selection is partly random.

The release is not a runnable implementation. It contains no application code, dependency lock, deployed server snapshot, exact predefined-question bank, event log, question queue, model-call record, participant protocol, consent form, raw recording, analysis code, or item-level difficulty table. The README calls the prompt material “codes,” but it is 71 lines of prose/pseudocode. The three response CSV schemas differ: Accounting and Political Science have eight columns, Usable Security seven; headers are partly unnamed; location encodings vary; and malformed JSON-like strings occur in cells.

A direct parse found 48 Accounting records (24 `A`, 24 `B`; 29 labeled similar), 69 Political Science records (34 `A`, 35 `B`; 13 similar), and 38 nonblank Usable Security records (15 `A`, 23 `B`; 26 similar): 155 records total. The papers' three displayed condition totals imply 154 annotations (74 human-assisted plus 80 Data Therapist), so the release and manuscript do not provide a one-to-one analysis inventory.

### Participants, assignment, and procedure

The manuscript repeatedly conflicts over its participant frame. It says “four sets of two” and “four different domains,” yielding eight participants (Introduction and Section 5.1, pp. 3, 15), but Table 1 contains only six participants and Sections 5.1–5.2 name only Accounting, Political Science, and Usable Security. The conclusion again says four groups (p. 21). The three reported pairs include two CPAs, two political scientists, and two usable-security researchers/students with 2.5–8 years of experience. All but one are male. Each received a $20 gift card after roughly two two-hour sessions.

Within each domain, one expert was assigned Data Therapist and the other a study-administrator “human interviewer.” The paper reports no random assignment. The human interviewer's expertise, training, script, and fidelity are not specified, yet Section 5 says the human interviewer's domain knowledge is treated as gold standard (p. 15). This is especially problematic because the participants—not the interviewer—are the domain experts.

Each pair jointly selected a familiar but non-expert-challenging dataset in advance. After 15–20 minutes of instruction, both conditions typed annotations for 45 minutes. Human-interview participants used Google Sheets; the interviewer intervened if asked, if content was insufficient, or after 20 seconds of inactivity. Data Therapist participants had the integrated spreadsheet, plots, and question interface. Thus the treatment changes interface, analysis affordances, prompt policy, timing of intervention, and interlocutor—not only LLM versus human questions.

At least a day later, participants rated their own and the paired expert's annotations on a 1–5 **knowledge difficulty** scale: 1 means comprehensible to lay audiences, 3 known to domain experts but not lay audiences, and 5 only some specialized experts understand (Section 5.3, pp. 16–17). This is not usability difficulty, annotation quality, correctness, informativeness, or tacitness. Participants were not described as blinded to author, condition, or their own annotations.

### Analysis

The authors report counts by origin and location, manually group annotation topics as shared, DT-exclusive, or HI-exclusive based on aligned topic and goal, and compare difficulty distributions (Section 6, pp. 17–20). No coder count, independent labels, agreement statistic, adjudication record, codebook version, qualitative method, statistical model, confidence interval, or clustered analysis is reported in the paper. The OSF CSVs expose final `S`/`D` labels and counterpart IDs but no coder provenance.

The design has one participant per condition per domain. Condition is therefore perfectly confounded with expert identity, specialization, writing behavior, dataset familiarity, and interface. Annotation rows are repeated outputs from the same six people, not independent samples. No causal Data Therapist-versus-human effect is identified.

## Evidence and results interpretation

### Annotation yield is descriptive, not quality evidence

For the three displayed domains, Table 3 reports 24, 32, and 24 DT annotations and 24, 35, and 15 human-assisted annotations. DT answers are split among direct annotations, LLM questions, and predefined questions. These values show that participants used all three paths. They do not show complete coverage: the candidate-question denominator, displayed/deleted/ignored questions, annotation length, factual validity, unique evidence, correction rate, and saturation are absent.

The aggregate row cannot be reconciled with the displayed domains. Human domain counts sum to 74, not the printed 96; DT domain counts sum to 80, not 108. The displayed human components sum to 34 unaided and 40 interviewer-aided, not printed totals 46 and 50. Displayed DT components sum to 33 direct, 35 LLM-answer, and 12 predefined-answer annotations, not 40, 47, and 22. The gap exactly looks like an undisclosed fourth group (22 human and 28 DT annotations). Table 4 means also cannot be arithmetic means of the three displayed domains; the implied missing fourth-group scores are plausible. The paper neither identifies nor explains this hidden contribution to headline totals.

The abstract's statement that Data Therapist was “5 percentage points less difficult to use” than a human annotator is not supported by the described measure. The rating is difficulty of annotation content for a non-expert, where lower can mean **less specialized knowledge**, not easier tool use. No usability scale was administered. Even as annotation difficulty, Table 4's printed means include the unexplained group and have no uncertainty.

### Topic overlap reveals scope, not machine accuracy

The strongest empirical observation is the specialization effect. Reported DT overlap with HI topics is 58% in Accounting and 71% in Usable Security, but only 5 of 28 DT Political Science annotations overlap. The paper attributes the latter to different regional expertise—Southeast Asia versus Northeast Asia (Section 6.2, pp. 18–19). This invalidates “human annotations as gold standard” while supplying a more useful insight: different qualified experts answer different latent questions because their scope differs.

Neither shared nor exclusive topics directly measure quality. Shared content can be obvious, mutually primed, or wrong; exclusive content can be valuable specialist evidence, irrelevant digression, or unsupported inference. The released Political Science rows include broad causal and predictive claims, such as economic or geographic conditions causing repression, with no source citation or confidence. The model accepted them because topical relevance is not evidentiary validity.

The paper reports that none of the chosen predefined-question annotations aligned with HI topics and that LLM-generated questions aligned more often. This may indicate contextual adaptation, but it does not show that the LLM recovered missing tacit knowledge. The LLM can exploit prior familiarity with public datasets, as participants and authors themselves note (Section 7.1, p. 20), while the fixed Datasheets questions deliberately cover governance categories a spontaneous interviewer may omit. Overlap rewards imitation of one comparator, not comprehensive or consequential coverage.

### Difficulty results do not establish tacit-knowledge capture

The paper explicitly concedes that difficulty is not a proxy for tacit knowledge. It reports similar concentration around levels 2–3, 45% of LLM-aided annotations at level 3 or higher, and 12.7% at level 4 or higher versus 21% for human annotations (Section 6.3, pp. 19–20). Without item-level ratings, rater identity, self/other split, uncertainty, or released analysis, these are unauditable manuscript reports.

Even if exact, asking a difficult question differs from eliciting a correct, incident-grounded answer. Difficulty can rise with jargon, obscurity, narrow specialization, or ambiguous wording. It does not establish hidden-requirement value, observable consequence, or downstream usefulness.

### Post-v3 downstream artifact is only a design ideation trace

The OSF node later added a seven-page “Evaluation of annotations with visualization designers” PDF in December 2025, after immutable v3's October update. It lists proposed analytical questions, features, and chart types from four numbered participants for Accounting and Security. This is useful evidence that transformed annotations can seed design ideas. But it provides no participant credentials, recruitment, protocol, condition comparison, source-annotation links, rating, created visualization, correctness check, stakeholder outcome, or analysis. It is post-v3 supplemental evidence and cannot retroactively validate the paper's claim that the knowledge base improves visualization design. No released artifact tests benchmark authoring.

## Unique insight

The deepest transferable insight is that **an AI elicitor changes the distribution of expert testimony before any analyst begins coding it**. Data Therapist's output is not simply “what the expert knows.” It is the result of:

`dataset view → model/predefined candidate questions → priority/random tie-break → displayed subset → expert answer/delete/ignore choice → model acceptance/revision pressure → prior-annotation-conditioned follow-up → location binding → export`

Each edge is a selection or transformation event. Early questions can anchor what the expert attends to; the fixed seven-genre framework can manufacture apparent completeness; relevance feedback can push answers toward the model's framing; and accepted but unsupported statements become context for later questions. Conversely, selectable questions and direct annotations preserve some expert agency and can lower the skill threshold for structured contribution. The correct unit is therefore an **elicitation event ledger**, not only the final annotation.

A second insight is that **coverage is plural**. More annotations, more metadata genres, more table locations, more overlap with another expert, and more professionally consequential knowledge are separate quantities. A tool can improve one while degrading another. `skill-bench` should measure candidate yield, evidence-backed novelty, scope discovery, contradiction discovery, correction, observability, and downstream checkability independently.

A third insight is that **expert disagreement often localizes construct scope before it signals error**. The political-science pair had matched degrees and years but different regional expertise. For benchmark construction, the correct response is not to pick the annotation set most similar to an LLM or average both. It is to preserve observer scope, identify conditional applicability, seek counterexamples, and decide whether a task variation fairly requires one specialist perspective.

Finally, an LLM answer validator has no inherited epistemic authority. It can check textual responsiveness or surface contradiction, but it cannot establish factual truth, professional approval, source authority, temporal validity, or benchmark fairness. Calling this “verification” risks laundering a dialogue-management function into an evidence-quality gate.

## Transferable design patterns

### 1. Preserve the elicitation instrument as treatment

For every candidate statement, record:

- dataset/source and exact version shown;
- visible row/column/cell selection using stable identifiers, not display coordinates alone;
- question origin: expert, interviewer, predefined framework, or model;
- exact prompt/model/context hashes and generation time;
- candidate queue, priority components, random seed/tie result, and displayed position;
- expert action: spontaneous annotation, answered, deleted as irrelevant, skipped, revised, or withdrawn;
- machine feedback and before/after answer;
- parent annotations used to generate the follow-up; and
- exported statement hash plus correction/supersession lineage.

This turns probe anchoring, omission, and path dependence into inspectable evidence.

### 2. Separate dialogue checks from evidence checks

Use distinct statuses:

1. `responsive_to_question` — a dialogue-management judgment;
2. `internally_consistent` — with scope/time caveats;
3. `capture_confirmed_by_contributor`;
4. `corroborated_by_source_or_observation`;
5. `scope_reviewed`;
6. `transformation_reviewed`; and
7. `benchmark_utility_validated`.

A model may assist with the first two. It cannot confer the latter five. Contradictions should create linked unresolved records, not force the expert to choose one globally “right” answer when both may be context-dependent.

### 3. Protect an unprompted opportunity window

Before exposing Datasheets genres, rubric categories, or LLM questions, invite a free task/dataset walkthrough and one concrete consequential incident. Label this material `SPONTANEOUS`. Then expose structured probes and label resulting content `PROBED`. This permits a bounded comparison of what the schema recovers versus what it anchors. It directly complements ACTA/CDM's instruction to obtain uninterrupted recall before imposing analytic categories.

### 4. Treat location as applicability evidence, not truth

A cell/row/column target should carry dataset identity, stable key, selector semantics, valid time, scope, and transformation behavior under sorting/filtering/version changes. Location-tagging usefully narrows applicability, but it does not prove the annotation. If a statement is generalized from selected rows to a population, preserve that inference and its evidence separately.

### 5. Evaluate useful yield, not annotation volume

For a real `skill-bench` session, compare generic, ACTA/CDM, and mixed-initiative phases on:

- unique candidate statements per contributor-hour;
- statements with concrete incident/source evidence;
- expert corrections and question rejections;
- contradictions and context splits discovered;
- claims surviving independent corroboration;
- candidate primitives with fair observable consequences;
- downstream builder misinterpretations caught at read-back; and
- participant burden, comprehension, withdrawal, and reciprocal utility.

Do not aggregate these into one efficacy score until their decision use is validated.

### 6. Require downstream transformation tests

A structured annotation is not useful merely because a designer can propose a chart or a builder can draft a rubric. Sample downstream artifacts must link each decision back to source statements; experts must inspect whether meaning and scope survived; and held-out cases must test whether the resulting requirement/check distinguishes supported professional consequences from plausible alternatives and hidden obligations.

## Limitations and validity threats

1. **Six versus eight participant contradiction.** The immutable paper names four groups/eight participants but discloses only three domains/six people.
2. **Headline totals include an unexplained group.** Tables 3–4 aggregate counts and means not derivable from displayed domains; no exclusion or fourth-domain account is given.
3. **One expert per condition per domain.** Tool effects are inseparable from participant identity, specialization, writing style, familiarity, and motivation.
4. **No reported randomization or crossover.** Assignment policy is unknown, and no participant uses both elicitation modes.
5. **Treatment bundles multiple differences.** Data Therapist versus Google Sheets changes interface, visual analysis, question generation, intervention policy, and interaction partner.
6. **Human comparator authority is unspecified.** The study administrator's interviewing/domain expertise, script, and fidelity are absent, despite “gold standard” language.
7. **Tiny, homogeneous sample.** Six reported participants, five men, three data-centric domains, one pair each, and unusually low compensation do not support cross-domain or population claims.
8. **Expertise basis is coarse.** Degree, title, and years do not establish task-specific performance; the political-science result demonstrates specialization mismatch.
9. **Difficulty is construct-invalid for usability or tacitness.** The scale measures who might understand content, not ease of tool use, correctness, quality, or hidden expertise.
10. **No independent qualitative reliability.** Topic grouping lacks coder-level labels, agreement, codebook history, and adjudication provenance.
11. **No inferential uncertainty.** Annotation rows are clustered within six people, yet no participant-level model, interval, randomization test, or sensitivity analysis is reported.
12. **Overlap is not a gold-standard metric.** One expert's omission does not make another's exclusive topic wrong; shared topics can also be invalid.
13. **Probe anchoring and omission are unmeasured.** There is no randomized question exposure, unprompted baseline, candidate/display/delete log, or order analysis.
14. **Path dependence is uncontrolled.** Earlier annotations condition later questions; random tie-breaking has no reported seed; condition outputs cannot be exactly replayed.
15. **Model identity and retrieval are under-specified.** GPT-4, `o1`, and GPT-4o descriptions coexist; exact snapshots/settings and “built-in RAG” evidence are absent.
16. **Validation is textual, not epistemic.** The prompt checks appropriateness and text contradiction, not factuality, source authority, valid time, or professional legitimacy.
17. **No hallucination/error audit.** Released statements contain broad causal interpretations without citations, but no independent domain review or correction outcome is reported.
18. **Correction and withdrawal lineage is absent.** The UI supports review/edit, yet neither paper nor release preserves versions, deletions, rejected model feedback, or consent withdrawal effects.
19. **Privacy and release authority are unclear.** IRB approval and recording permission are reported, but public-release consent, de-identification procedure, accounting-data provenance, and annotation-use boundaries are not.
20. **No burden evidence.** Session duration and $20 compensation are known; workload, usability, fatigue, trust, dropouts, refusals, and participant preference are not measured.
21. **Seven genres are supplied categories, not discovered dimensions.** Apparent metadata coverage can reflect instrument structure rather than naturally externalized tacit expertise.
22. **No downstream validity in v3.** The paper tests neither visualization quality nor benchmark authoring; the later designer list has no evaluative protocol or outcome.
23. **Mutable and incomplete release.** The OSF node is unregistered and mutable, has no license, and omits code, logs, raw ratings, protocol, and analysis. Local hashes preserve only the inspected state.
24. **Paper/release inventory mismatch.** The released 155 labeled records do not transparently reconcile to the three-domain 154 annotation total or hidden aggregate group.
25. **Audience model is undefined.** “Lay audience” varies by task and consequence; one scalar difficulty rating cannot establish what a benchmark agent or artifact consumer needs explained.

## Reproducibility and operational realism

Reproducibility is moderate for inspecting the elicitation concept and weak for replaying the system or study. The immutable paper provides architecture, equations, task timing, participant table, prompt formulas, and reported results. The official September ZIP preserves the three datasets, merged response/coding tables, and prompt text at OSF file-version 1. These are meaningful primary artifacts, and the local provenance record preserves hashes and the mutable-node timing boundary.

Exact reproduction is impossible from the release. There is no frontend/backend source, environment lock, API configuration, model-call trace, generated-question inventory, question priority state, random seed, exact predefined question set, event log, saved annotation versions, study script, raw recordings, item-level ratings, coder assignments, or analysis notebook. Hosted OpenAI behavior and the AWS deployment are mutable. The paper's model naming and participant inventory are internally inconsistent.

Operational realism is mixed. The interface offers useful contributor control: experts can annotate directly, bind statements to data regions, choose questions, delete irrelevant prompts, revise rejected answers, and export structured records. Those features plausibly support asynchronous micro-contributions. But the study does not measure setup/support labor, participant comprehension of model transformations, correction cost, privacy review, analyst cleanup, or downstream expert review. A 45-minute session producing dozens of statements can create more verification work than it saves.

The OSF release is also operational evidence of transformation loss. Final CSVs preserve text, coarse origin/condition, topic similarity, intent labels, and unstable location encodings, but omit the full interaction state needed to distinguish spontaneous knowledge, machine-shaped answers, rejected prompts, revisions, and model interpretations. A polished annotation table is therefore insufficient as the authoritative elicitation record.

## Concrete changes for skill-bench

1. **Refine the existing real-session template rather than create a parallel elicitation subsystem.** When it is exercised, add a linked machine-readable event stream for candidate/display/delete/answer/reject/revise/withdraw and prompt/model/context identity. The pending `build-elicitation-session-contract` already has the correct dependency and must remain blocked until a consented real contribution exists.
2. **Add an unprompted-before-probed phase to the next real session.** Preserve uninterrupted task/data explanation before showing schema categories or model questions; compare evidence-backed novelty and omissions, not rubric completeness.
3. **Treat generated questions as analyst interventions.** Each answer must inherit question origin and instrument provenance. It must not inherit LLM authority or be labeled spontaneous expert testimony.
4. **Replace “verified answer” with typed checks.** Keep responsiveness and textual contradiction separate from contributor capture approval, source corroboration, scope validity, and benchmark utility.
5. **Preserve independent expert scope and disagreement.** Do not use overlap with one paired expert as truth. Record role, specialization, context, and valid-time; test context splits and conditional task variants before adjudicating.
6. **Version multigranular targets.** Bind annotations to stable source-pack identifiers and selectors with hashes and valid time so sorting, filtering, row insertions, and dataset updates cannot silently move their applicability.
7. **Measure burden and reciprocal utility.** Record contributor time, rejected questions, corrections, review time, privacy concerns, withdrawal, reusable outputs, and accepted primitives per hour; annotation count alone is a throughput metric.
8. **Require a downstream fidelity gate.** Before an annotation becomes a requirement, hidden consequence, skill, rubric, or grader criterion, preserve the builder transformation, expert read-back, counterexample, observable consequence, and claim limit.
9. **Keep model-derived summaries non-authoritative.** A thematic summary or inferred annotation should be labeled model-derived and separately approved; downstream artifacts inherit provenance, never expert approval.
10. **Do not infer low-cost feasibility.** Six participants receiving $20 in a research study do not establish sustainable expert recruitment, fair compensation, retention, or near-zero-cost participation.

## Action items for repository

- [x] Read and verify the complete immutable arXiv v3 PDF/text.
- [x] Acquire and inspect the complete paper-linked OSF study ZIP, prompts, three response tables, README, and post-v3 designer artifact with file-level provenance and timing boundaries.
- [x] Reconstruct the mixed-initiative loop, seven Datasheets genres, participant assignment, study procedure, measures, and results with page/file evidence.
- [x] Audit participant-count, aggregate-table, release-inventory, construct, assignment, disagreement, correction, privacy, model, and downstream-use limits.
- [x] Compare against `docs/concepts/cognitive-task-analysis-to-benchmark-authoring.md` and `templates/expertise-elicitation-session.md`.
- [x] Add no duplicate build task: findings refine the existing expertise-transfer, expert-participation, evidence-chain, and blocked real-session work.
- [ ] Exercise the existing template with a consented real contributor before implementing the elicitation-session contract; do not simulate testimony or treat this paper as expert validation.
