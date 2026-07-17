# User-authored agent rules are candidate local contracts, not validated collaboration criteria

## Bottom line

Dong et al. identify a useful vocabulary for behavior that software developers explicitly requested from coding agents: follow standards and project workflows; preserve code quality; understand context, work incrementally, validate, and stay in scope; communicate, clarify, plan, and learn from feedback. The 23-page arXiv paper extends the 91-project rule-file analysis with interviews of 15 experienced engineers and an LLM-assisted analysis of 1,000 prototyping prompts, proposing a Context-Adaptive Behavior (CAB) framework whose expectations vary by time horizon and type of work. The five-page official CHI EA paper contains only the rule-derived taxonomy and reports useful file-level prevalence percentages.

The distinctive contribution is the **source channel**: naturally authored project rules expose candidate operating requirements before researchers turn them into rubrics. That is closer to expertise-to-evaluation than an invented generic checklist. But a rule file is simultaneously a local preference, a prompt intervention, an organizational artifact, and a possible response to prior agent failures. It does not establish that its author is professionally authoritative, that the rule is current or generally applicable, that an agent actually obeyed it, or that obedience improved collaboration, quality, productivity, safety, or downstream outcomes.

The paper's three studies do not validate those missing links. Study 1 derives a 15-attribute codebook from 15 files and applies an unnamed frontier LLM to the rest; only five files/95 segmented rules are checked, with no released corpus, prompt, codebook, labels, authoring population, disagreement ledger, or independent human-reliability estimate. Study 2 is underreported: all 15 frequent agent users come from the same company, the interview analysis is informed by Study 1's codebook, and recruitment, protocol, duration, recording, coding roles beyond “two co-authors,” saturation, negative cases, and disagreement are absent. Study 3 compares a different tool, interface, user population, task purpose, and instruction channel at once. Its “type of work” contrast therefore bundles work type with user expertise, product affordances, rule-file friction, and reactive prompting.

For `skill-bench`, the safe transfer is a **rule-to-criterion projection record**, not the paper's taxonomy as a universal rubric:

`rule span → author/authority/scope/valid time → candidate obligation or preference → applicability and conflicts → required observation view → task opportunity → realized behavior → artifact/state/consequence → burden and affected-party disposition → bounded claim`.

Each arrow needs evidence. A declared rule can nominate a test; it cannot grade itself.

## One-sentence contribution

The paper turns naturally authored project instructions into a 15-attribute candidate behavior vocabulary and proposes contextual adaptation, supplying a valuable pre-rubric evidence channel without validating the rules as authoritative, observable, beneficial, or general evaluation criteria.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, and E through narrow expansion into a direct expertise-to-evaluation transformation. Software engineering is the empirical setting, not a benchmark scope commitment. The general hypothesis is that naturally authored operating rules can supply high-value candidate requirements when their authority, context, conflicts, observability, realization, and consequences remain explicit.

- **Concrete evidence:** complete immutable arXiv v1 PDF/text plus the complete official five-page CHI EA paper and provenance record.
- **Uncertainty clarified:** whether developer-authored runtime instructions are evidence of a professional criterion, an intervention, a local preference, a workaround, or a validated collaborative behavior.
- **Mode:** expansion with consolidation-ready authoring and validation implications.
- **Duplication check:** Human Oversight studies reported lifecycle practices; Domain-Expert Participation studies authority through transformation; ResearchRubrics studies criterion authoring; Consulting Cognitive Traps studies expert-visible decision boundaries. This paper uniquely starts from naturally authored project instruction files and compares them with interview ideals and prototyping prompts.
- **Useful completion:** retain the 15 behaviors as a candidate vocabulary and the context-adaptation premise, while preventing local declarations from becoming universal hidden obligations or unsupported collaboration-quality claims.

## Sources and reading record

### Full primary source read

- Tao Dong, Harini Sampath, Ja Young Lee, Sherry Y. Shi, and Andrew Macvean, *From Correctness to Collaboration: Toward a Human-Centered Framework for Evaluating AI Agent Behavior in Software Engineering*.
- Immutable arXiv v1: <https://arxiv.org/abs/2512.23844v1>, submitted 29 December 2025. The retained metadata contains no withdrawal or retraction notice.
- Local PDF: `data/papers/pdfs/2512.23844v1-context-adaptive-agent-behavior-taxonomy.pdf` (23 pages; SHA-256 `fd373c01c9cc918f7adff2dd43367894966769f49ad5fe0dd279dd2cb4f1c970`).
- Local text: `data/papers/text/2512.23844v1-context-adaptive-agent-behavior-taxonomy.txt` (SHA-256 `a686a74d3ca10c7d289c71eaf0c95c538aa72203adb6097db54fe43c0d78314f`).
- Metadata HTML: `data/papers/source/2512.23844v1-metadata.html` (SHA-256 `5b09e8fe11d5813a204d77573592896e6fba7afa93af00bf8d520f1db2ef8d46`).

The full paper was read through all three studies, discussion, limitations, disclosure, and references. Page references use PDF pages; extraction line ranges are supplied for auditability.

### Official conference version read

- Tao Dong, Sherry Shi, Harini Sampath, and Andrew Macvean, *From Correctness to Collaboration: A Human-Centered Taxonomy of AI Agent Behavior in Software Engineering*, CHI EA '26, DOI <https://doi.org/10.1145/3772363.3798733>.
- Official Google Research page: <https://research.google/pubs/from-correctness-to-collaboration-a-human-centered-taxonomy-of-ai-agent-behavior-in-software-engineering/>.
- PDF: `data/sources/pdfs/1036663-from-correctness-to-collaboration.pdf` (5 pages; SHA-256 `15ad2c4378f895942eae2f106db6fd2ac58a4beddf145d19711caf9c5a2e6f81`).
- Text: `data/sources/1036663-from-correctness-to-collaboration.txt` (SHA-256 `c6fc4ae5417af13a77688a200a4b61571e11ee493697b672dd42833151021232`).
- Provenance: `data/sources/1036663-from-correctness-to-collaboration.provenance.json`.

The official paper is five pages, not ten. It omits Ja Young Lee and contains Study 1 only; the arXiv version adds the interview-derived time-horizon and prompt-derived work-type studies. The conference paper says its annotator prompt and full codebook are supplemental, but neither the PDF nor official publication page exposes a supplement link. No rule corpus, codebook, prompt, interview material, prototyping prompt sample, labels, or analysis package was available. The arXiv paper should not be described as the official conference paper's full version without further provenance evidence.

## Research question and contribution

The overarching question is: **what core behaviors should an intelligent software-engineering agent be evaluated for?** The paper answers with two related objects (arXiv pp. 1–2; extraction lines 7–87):

1. a current enterprise taxonomy from 91 project-level agent-rule files; and
2. a CAB framework intended to adapt that taxonomy along a current-to-aspirational time horizon and an enterprise-production-to-rapid-prototyping work-type axis.

The evidence supports bounded claims that:

- selected early adopters at one large company authored rule files containing the reported behavior categories;
- the authors' content-analysis procedure organized those rules into four themes and 15 attributes;
- selected experienced engineers at the same company discussed code quality, standards, problem solving, collaboration, and learning when comparing junior developers with agents;
- selected prompts from one prototyping product contain some similar requests plus more UI/UX, explanation, and expert-persona language; and
- behavior requirements plausibly vary by context and maturity target.

It does **not** establish that:

- the 91 files represent developers, projects, the company, software engineering, or knowledge work generally;
- expressed rules are effective, desirable to all affected parties, current, non-conflicting, or actually followed;
- the 15 attributes are exhaustive, mutually exclusive, stable, independently reliable, or causally linked to collaboration quality;
- the interview themes are saturated, prevalent, independently coded, or longitudinal evidence of a time horizon;
- the prototyping differences are caused by work type rather than users, product, interface, task mix, or instruction-channel differences;
- a human or LLM judge can validly infer all 15 behaviors from a trajectory and output;
- more communication, clarification, planning, memory, or autonomy is always better; or
- CAB scores predict quality, productivity, trust, professional acceptance, safety, or readiness.

## Methodology and evidence

### Study 1: 91 project rule files

The authors collected 91 markdown rule files from distinct company projects in July 2025 (arXiv pp. 4–5; lines 164–192). The official version adds that collection occurred about one month after company support for agent rules was introduced, making this explicitly an **early-adopter snapshot** (official pp. 2–3; extraction lines 113–124). Two co-authors collaboratively and iteratively open-coded 15 files, producing 15 behavior codes grouped into four themes. An unnamed frontier reasoning LLM segmented and multi-labeled the remaining files, with up to three codes per rule and a `TBD` option.

On five randomly selected files, the model segmented 95 rules—reported as about 7.2% of all rules—and achieved 94.4% pair precision, 91.2% pair recall, and “zero hallucination” against human assessment (arXiv pp. 4–5; lines 171–192). This is useful evidence that the authors performed a small annotation check, but its interpretation is narrow:

- the 15 codebook-development files are not said to be random, diverse, or disjoint from iterative annotator tuning;
- the paper does not define who produced the validation labels, whether they labeled independently, how disagreements were resolved, or whether the LLM's segmentation was itself treated as ground truth;
- multi-label pair precision/recall does not test category completeness, segmentation stability, theme validity, prevalence estimation, or whether `TBD` items reveal missing categories;
- “zero hallucination” is undefined and is not equivalent to zero miscoding;
- one five-file validation set provides no uncertainty interval, per-code performance, rare-code performance, repeated-run stability, or project clustering analysis;
- the model, version, prompt, decoding, codebook, inputs, outputs, and labels are unreleased; and
- there is no author/project population denominator, number of unique rule authors, author role/seniority, rule age, revision history, conflict rate, or rule-use telemetry.

The official paper reports file-level prevalence: project workflows/conventions occur in 92.31% of files, project-context-before-action in 90.11%, and the least frequent attributes include collaborative planning/trade-offs at 8.79% and task focus at 9.89% (official Table 1, pp. 2–3; lines 128–168). Those figures describe **file mentions**, not behavior importance, rule counts, unique user prevalence, execution frequency, compliance, or outcome value. Files differ in length and projects may share authors or templates. A common rule can be a response to frequent failure, boilerplate propagation, or cheap codification; a rare rule can be critical but hard to state.

### The taxonomy

The 15 attributes are (arXiv Table 1, p. 6; lines 237–280):

- follow established best practices;
- follow project workflows and conventions;
- maintain code style;
- write readable and maintainable code;
- build robust and performant software;
- understand project context before acting;
- validate work proactively;
- work incrementally and iteratively;
- maintain task focus;
- infer intent from context;
- learn by example;
- communicate effectively;
- seek help and clarification;
- plan collaboratively and analyze trade-offs; and
- learn from feedback and past experiences.

This vocabulary is useful, but it mixes different ontological levels:

- **artifact properties:** readable, maintainable, robust, performant code;
- **trajectory operations:** inspect context, run tests, make incremental changes;
- **interaction policies:** ask, explain, plan, seek approval;
- **scope/authority constraints:** stay focused, hand off tool-restricted steps;
- **configured-system state:** persistent lessons and feedback memory; and
- **source-relative conformance:** local style, workflows, and best practices.

A single “behavior score” would therefore combine properties requiring different evidence views, timing, authority, and causal interpretations. The paper itself recognizes interplay and bounded agency (arXiv pp. 10–11; lines 423–462), but provides no dependency graph, applicability policy, conflict-resolution method, observer specification, scoring procedure, or validation outcome.

The rules also contain genuine tensions:

- infer low-stakes intent versus stop and clarify under ambiguity or risk;
- maintain strict task focus versus leave the code cleaner than found;
- follow global best practice versus prioritize local convention;
- act incrementally versus minimize interruption and latency;
- expose plans/reasoning versus avoid communication noise;
- learn from past interactions versus honor changed context, privacy, deletion, and scope; and
- challenge a user request versus respect user authority.

These are not taxonomy defects; they are evidence that a criterion needs an **applicability and precedence contract**. The correct behavior depends on stakes, reversibility, uncertainty, authority, source validity, work purpose, and affected parties.

### Study 2: 15 experienced engineers and the “time horizon”

The paper reports semi-structured interviews with 15 experienced software engineers from the same company who frequently used agents (arXiv pp. 11–16; lines 465–667). Most reportedly had more than six years of experience, used agents daily, and had supervised or mentored juniors multiple times. Interviews used a mind-mapping exercise about core engineering values, followed by comparison of junior developers and agents. Two co-authors conducted thematic analysis “informed by” Study 1's codebook.

The finding is conceptually useful: participants expected junior developers to internalize standards and improve through social feedback, whereas they described current agents as static tools whose apparent improvement depends on user-provided prompts and context. That distinguishes immediate task conformance from longitudinal learning and motivates retention/transfer tests.

Methodological reporting is too thin for stronger claims. The paper omits recruitment route and denominator, eligibility thresholds, participant roles and project diversity, exact demographics, interview dates/duration, compensation, consent/ethics process, recording/transcription, complete protocol, interviewer identities, open-versus-deductive coding balance, coder assignment, independent coding, disagreements, codebook changes, saturation/stopping, negative cases, participant-by-theme counts, and member checking. Selected quotations establish that particular participants expressed each idea; they do not establish theme prevalence or completeness.

Calling this a “Time Horizon” axis is also stronger than the design. No participant, agent, team, or requirement is followed over time. The study contrasts reported present expectations for agents with social-development expectations for junior humans and a future aspiration for metacognitive agents. That is a **normative maturity contrast**, not observed temporal evolution. Human and agent conditions differ in embodiment, employment, accountability, training, memory, access, social role, and time scale; “junior developer” is an elicitation anchor, not a matched comparator or validated AGI criterion.

### Study 3: 1,000 prototyping prompts and the “type of work”

The authors randomly sampled 1,000 users with at least ten interactions in July 2025, then randomly selected 1,000 prompts. An LLM filtered 488 prompts as behavior-related, clustered them, and classified them into 13 author-refined themes. One author labeled 25 prompts for a reported F1 of 83%, precision 81%, and recall 85% (arXiv pp. 16–18; lines 670–780).

The analysis finds familiar requirements—standards, quality, context, validation, planning, clarification, feedback—plus more expert-persona prompting, UI/UX emphasis, and requests for explanation. Code-quality language is less prominent. These observations plausibly nominate contextual differences.

They do not isolate “type of work.” Enterprise rule files and prototyping prompts differ simultaneously in:

- persistent project configuration versus in-session requests;
- early enterprise rule authors versus users ranging from professionals to hobbyists;
- brownfield production code versus UI-focused exploration;
- one coding agent versus a different prototyping product;
- rule-file availability and friction;
- project and task distributions;
- opportunity to react to earlier outputs and failures; and
- likely stakes, artifact maturity, time budget, and deployment path.

The paper does not state whether prompts were one-per-user, how turns/sessions/projects were clustered, whether selection happened before seeing prompt content, how privacy/consent were handled, how behavioral filtering was validated, what the 13 themes were in full, or how many prompts supported each comparison. Only 25/488 classified prompts were human-checked, by one author, with no uncertainty or per-theme performance. Reactive prompts such as “why do you always make the same mistake?” are post-outcome evidence: they express frustration and a candidate failure history, not a clean pre-task requirement. Expert-persona requests may signal low articulability, imitation, convention, or prompt folklore—not verified expert standards.

The paper says the two settings demonstrate taxonomy generalizability and CAB utility (arXiv pp. 20–21; lines 871–886). The evidence supports a weaker conclusion: the same broad labels can describe selected text from both settings while their emphasis appears different. It does not establish measurement invariance, taxonomy completeness, causal adaptation, improved evaluation, or transport beyond software work.

## Unique insight: rules are pre-rubric evidence with dual treatment status

The paper's deepest transferable insight is not the four categories. It is that naturally authored rule files can reveal **candidate hidden work requirements and interaction boundaries in the language users already employ**. Unlike retrospective generic “what should an agent do?” prompts, these files are attached to real projects and intended to affect runtime behavior.

That advantage creates a dual status:

1. **Evidence channel:** the rule is evidence that at least one author wanted a behavior in a declared project context.
2. **Configured intervention:** showing the rule to the agent changes the evaluated system.

A benchmark must preserve both. If a task and grader are derived from a rule and the same rule is supplied to the agent, success estimates the configured package's rule-following under that disclosure—not unaided professional knowledge. If the rule is hidden, the benchmark needs an independent public/fair basis; otherwise it rewards an undisclosed local preference. If the grader simply checks whether an agent echoed a prescribed plan or explanation, it may measure evaluator-cue compliance rather than useful collaboration.

Rules also have **authority ceilings**. A project member may legitimately define local naming and workflow conventions while lacking authority to define security policy, organization-wide best practice, affected-user preference, or professional quality generally. The author, approver, scope, valid time, conflict set, and downstream stakeholder therefore matter at the claim level. A developer's instruction to “never ask questions” or “always update lessons_learned.md” is not made safe, efficient, privacy-preserving, or universal by appearing in a real repository.

Finally, CAB's strongest premise should be reformulated: context adaptation is not movement along two scalar axes, but **selection among conditionally applicable, sometimes conflicting obligations**. Work purpose and maturity are useful context features, but so are stakes, reversibility, user expertise, authority, uncertainty, artifact destination, promotion path, evidence availability, affected parties, and burden budget.

## From candidate behavior to observable checks

A behavior should be admitted only after decomposing what can be observed and what claim that observation licenses:

| Candidate attribute | Required evidence views | Safe local observation | Missing validity evidence |
|---|---|---|---|
| Follow standards/workflows | authoritative rule/version, applicability, trace, artifact/native state | named applicable step or state conformed | authority, currentness, conflict resolution, downstream value |
| Readable/maintainable/robust/performant | native artifact, executable tests, static/runtime measures, qualified review | selected predicates passed under pinned observers | future maintenance, reliability, performance transport, professional acceptance |
| Understand context before acting | availability/access trace, cited/adopted propositions, action dependency | relevant evidence was accessed before a linked action | comprehension, causal necessity, completeness, better outcome |
| Work incrementally | action/state deltas, checkpoints, rollback evidence | changes stayed within declared increments | optimal granularity, reduced risk/burden, no added delay/error |
| Validate proactively | test/check identity, execution receipt, coverage/authority, repairs | declared check ran and result affected action | check validity, independence, complete obligations, final quality |
| Maintain task focus | public scope, authorized mutation zones, collateral-state observer | no undeclared mutation under the observer | completeness of scope and collateral observer, legitimacy of omitted cleanup |
| Infer intent | admissible intent set, ambiguity, selected interpretation, consequence | one authorized interpretation was selected | true/current user intent, whether clarification would dominate |
| Communicate/explain | message content/timing, user exposure, comprehension/adoption | required proposition was delivered | fidelity, usefulness, cognitive burden, calibrated trust |
| Seek clarification | uncertainty/opportunity, question, authority route, response, uptake | question was asked at a declared trigger and response used | trigger calibration, interruption cost, decision improvement |
| Plan/trade-offs | plan options, assumptions, approval, trace/state alignment | options and selected plan were exposed before action | option completeness, plan fidelity, user comprehension, better consequence |
| Learn from feedback | feedback authority, state update hash, later opportunity, adoption, retention/forgetting | a scoped update changed later behavior | generalization, non-interference, privacy, safety, long-run value |

This table makes clear why a trajectory-only LLM “report card,” suggested in the discussion (arXiv p. 19; lines 808–825), is insufficient for many attributes. A transcript can show that the agent claimed to read context, run tests, or follow a plan; native tool receipts and state are needed to establish realization. A passing test does not establish maintainability. A clear explanation does not establish user comprehension or correct reliance. An update to memory does not establish useful learning.

## Comparison with adjacent reviewed evidence

- **Human Oversight in Practice:** that interview study describes how selected experienced users allocate control, co-planning, monitoring, and review. The present rule corpus captures one a-priori control artifact and candidate interaction policies. Together they require separation of declared rule, enforceable treatment, actual exposure/behavior, human action, artifact/state consequence, and burden. Neither validates current developer heuristics as best practice.
- **Domain-Expert Participation:** participation evidence shows that authority does not propagate through developer/model transformations. Here, rule authorship similarly provides provenance, not automatic domain authority or approval for taxonomy→criterion→judge transformations. Missing author identity, decision rights, consent, and review materials sharply limit the “user-grounded” claim.
- **ResearchRubrics:** ResearchRubrics makes criterion text and release defects inspectable but exposes hidden obligations, dependence, evidence-view, and threshold problems. The present paper is upstream: it nominates candidate criteria from rules but releases neither corpus nor codebook. Both require atomic applicability, typed authority, transformation lineage, and independent grader validation.
- **Consulting Cognitive Traps:** the trap framework ties a naive path to an expert cue, operation, decision boundary, and consequence. Agent rules frequently name preferred procedures without demonstrating the failure or consequence that justifies them. Rule-derived tests become stronger when a critical incident, contrast case, or downstream state shows why the instruction matters.

Together, these sources support a chain from **declared local expectation → authority and applicability → projected criterion → observed realization → consequence**, not a shortcut from user-written text to a universal collaboration score.

## Reproducibility and operational realism

**Primary-source inspectability is moderate.** The immutable 23-page arXiv paper reports all three broad study pipelines, examples, core taxonomy, selected interview quotations, and limitations. The official conference paper adds file-level prevalence and verifies that Study 1's taxonomy was published at CHI EA '26. Both sources are preserved with hashes.

**Analytic reproducibility is low.** The 91 rule files, rule segments, author/project metadata, codebook, annotator prompt/model/version, human labels, `TBD` records, file-level coding table, 15 interview transcripts/protocol/codebook, 1,000 prompt sample, 488 filtered prompts, 13-theme output, analysis scripts, disagreement records, and audit trail are unavailable. The official paper's promised supplement could not be located from its PDF or publication page. Exact counts beyond the conference table and reported validation summaries cannot be recomputed.

**Operational realism is meaningful but bounded.** Rule files and prompts were reportedly used in real company products and projects; examples reveal brownfield constraints, tool handoffs, validation commands, local precedence, memory workarounds, reactive frustration, and planning/clarification needs. This is valuable demand evidence. Yet no agent trajectory, artifact, test result, user response, intervention, productivity measure, defect, review outcome, or downstream consequence is analyzed. The studies examine **instructions and accounts**, not realized collaboration.

The two versions also create a provenance caution. The official CHI EA paper has four authors and one study; arXiv v1 has five authors and three studies. The latter is a complete primary source for CAB, while the former verifies only the taxonomy study and its reported frequencies. Claims about interviews or prototyping must cite arXiv v1, not the conference version.

## Limitations and validity threats

1. Study 1 comes from one large technology company and 91 projects.
2. Collection occurred roughly one month after agent-rule support launched, selecting early adopters and immature practices.
3. The sampling frame, search procedure, eligible project count, inclusion/exclusion rules, and collection completeness are absent.
4. Files are project-level, not independent user responses; unique author count, shared templates, copied rules, and project clustering are unknown.
5. Rule authors' roles, expertise, authority, tenure, demographics, and affected-party representation are unknown.
6. A rule expresses a declaration, not actual behavior, compliance, usefulness, correctness, or organizational consensus.
7. Rules may be workarounds for model defects, prompt folklore, stale instructions, boilerplate, or reactions to prior incidents.
8. Rule valid time, revision history, supersession, conflicts, and deprecation are not reported.
9. Two authors derived the codebook collaboratively, but independent initial coding and disagreement evidence are absent.
10. The 15 codebook-development files are not said to be random or selected for maximum variation.
11. No saturation, stopping, category-completeness, negative-case, or residual-`TBD` analysis is reported.
12. The unnamed LLM annotator, model version, prompt, settings, codebook, and outputs are unavailable.
13. Only five files and 95 segmented rules were checked; no uncertainty, per-code performance, rare-category recall, or repeated-run stability is reported.
14. Human validation-label production, segmentation authority, duplication, and adjudication are underdescribed.
15. Pair precision/recall does not validate taxonomy construct meaning, prevalence, or downstream criterion validity.
16. “Zero hallucination” is undefined and does not mean zero segmentation or classification error.
17. File-level percentages ignore rule counts, author dependence, file length, severity, and opportunity.
18. Frequency is not importance, effectiveness, or professional legitimacy.
19. The taxonomy mixes artifact qualities, trajectory operations, interaction policies, authority constraints, and persistent-system properties.
20. Categories and attributes overlap and have no reported dependency, exclusion, precedence, or applicability model.
21. Conflicting rules—clarify versus infer, local versus global, strict scope versus cleanup—are discussed narratively but not coded or resolved.
22. Functional correctness is treated as an often-unmentioned baseline, making absence from rules uninterpretable.
23. Study 2 has only 15 frequent users, all at the same company as Study 1.
24. Recruitment, eligibility, refusals, roles, team overlap, agent versions, and configured systems are absent.
25. Demographics are shown only as coarse figure summaries; participant-level accounting is unavailable.
26. Interview date, duration, recording/transcription, compensation, ethics/consent, and full guide are not reported.
27. The Study 1 codebook informed interview analysis, risking confirmation and restricting emergent themes.
28. “Two co-authors” conducted thematic analysis without coder roles, independence, agreement, disagreement, or audit trail.
29. No saturation, stopping rule, member checking, participant-by-theme matrix, prevalence, or systematic negative-case analysis is reported.
30. Junior developers and AI agents are asymmetric comparison objects; no matched work episodes or longitudinal development is observed.
31. The “time horizon” is a present-versus-aspirational interpretation, not a longitudinally measured axis.
32. AGI-oriented implications exceed the sampled accounts and measured constructs.
33. Study 3 samples only users with at least ten interactions, excluding non-adopters, unsuccessful beginners, and low-use users.
34. It is unclear whether 1,000 prompts are one per user or how sessions/users/projects are clustered.
35. Enterprise rules and prototyping prompts differ in persistence, affordance, purpose, and post-treatment timing.
36. Work type, user expertise, product, interface, stakes, rule friction, and task mix are confounded.
37. LLM filtering/clustering/classification can shape both the eligible corpus and resulting themes.
38. Only 25 prompts receive a one-author classification check; no filter validation, per-theme metrics, uncertainty, or repeated-run stability is reported.
39. Reactive prompts after failures are analyzed as expectations without separating pre-task requirements from outcome-conditioned complaints.
40. Expert-persona prompts do not identify actual expert standards or user knowledge.
41. The full 13-theme structure, counts, examples by cluster, and comparison statistics are absent.
42. Two software contexts cannot establish CAB completeness, measurement invariance, or cross-domain transfer.
43. No behavior is projected into a fully specified task, observer, grader, metric, or validity argument.
44. The paper proposes human or calibrated-LLM report cards without calibration evidence for these attributes.
45. Communication quantity, explanation, planning, and clarification can increase burden or induce misplaced trust; no user study measures either.
46. Persistent learning proposals omit scope, authority, privacy, deletion, contradiction, poisoning, and non-interference evidence.
47. No outcome data establish collaboration quality, quality, maintainability, productivity, safety, trust calibration, or professional acceptance.
48. The underlying materials and claimed conference supplement are unavailable, preventing independent reconstruction.
49. The arXiv and conference versions differ materially in title, authorship, scope, and available quantitative detail.
50. Transfer beyond selected software settings remains an untested hypothesis.

## Transfer to `skill-bench`

### Retain

1. Use naturally authored rule/configuration files as one elicitation channel for candidate requirements, procedures, handoffs, preferences, and failure histories.
2. Preserve the broad taxonomy as a search vocabulary, not a universal rubric.
3. Treat standards, quality, problem solving, and collaboration as plural dimensions rather than letting endpoint correctness exhaust evaluation.
4. Preserve context adaptation: requirements vary with work purpose, maturity, stakes, reversibility, expertise, and promotion path.
5. Record tensions explicitly rather than forcing one behavior everywhere.
6. Treat rules as configured interventions when supplied to the evaluated system.
7. Separate present task conformance from longitudinal learning, retention, transfer, and safe forgetting.

### Repair

8. For every source rule, retain immutable span/hash, author role and authority basis, project/scope, valid time, provenance, revision/supersession, intended audience, and disclosure status.
9. Classify the rule as `mandatory obligation`, `conditional procedure`, `local convention`, `optional preference`, `prohibition`, `handoff/approval boundary`, `evidence-source directive`, or `candidate failure response`.
10. Require an applicability predicate, precedence/conflict links, affected parties, public/fair basis, and authority-specific approval before projection.
11. Keep rule authorship, taxonomy coding, criterion drafting, grader implementation, and release approval as distinct transformations.
12. Record whether the rule is supplied to the agent, hidden as a fair consequence, or used only for diagnosis; do not confuse rule-following with unaided expertise.
13. Map each criterion to required observer views and explicit `insufficient_evidence` states. Trajectory narration cannot prove native state, test validity, maintainability, learning, or user comprehension.
14. Decompose opportunity, exposure, behavior, artifact/state result, downstream consequence, burden, and affected-party judgment.
15. Use matched positive/negative and conflict cases before calling a rule a valid criterion.
16. Validate human/model judges separately by attribute, evidence view, severity, context, and missingness.
17. Preserve local preferences without aggregating them into professional quality unless qualified independent evidence licenses that interpretation.
18. Estimate reliability and transport at the user/project/task level; do not treat rule mentions or prompts as independent population observations.

### Test

- **Rule realization:** same task with a rule absent, merely present, demonstrably read, and enforceably mediated; observe behavior and state separately.
- **Authority:** identical rule text authored by a local maintainer, organization policy owner, unqualified contributor, and external template; test whether the evaluation routes or weights it appropriately.
- **Applicability conflict:** infer-versus-clarify, local-versus-global style, strict-scope-versus-safe-cleanup, and speed-versus-maintainability cases with public stakes and precedence.
- **Observer sufficiency:** transcript only versus native trace/state/test/artifact views; measure false acceptance and abstention for each attribute.
- **Consequence:** matched rule-conformant and nonconformant work products evaluated for downstream review burden, defects, rework, recipient comprehension, or selected state loss.
- **Disclosure:** no-rule, public-rule, and independently derived criterion conditions to separate package efficacy, evaluator-cue compliance, and underlying capability.
- **Context transport:** reuse one source-derived behavior across software and at least one non-code knowledge-work artifact with re-authorized applicability and domain-specific consequences.
- **Longitudinal learning:** feedback delivered with scoped authorization, later equivalent and conflicting opportunities, retention/forgetting probes, privacy deletion, and collateral behavior checks.

## Concrete repository actions

- Added this deep comparative review based on the complete immutable arXiv v1 paper and complete official CHI EA paper.
- Updated `data/papers/index.json` to record deep-review completion and the review path.
- Added the review to `papers/topic-index.md` under expertise transfer.
- **No new queue task added.** Existing expertise-transfer, participation/authority, task-projection, configured-system, interaction/feedback, artifact/state, evidence-view, task-health, metric, and validity machinery already provides homes for rule-to-criterion projection and the proposed validation cases. Adding a coding-specific rule schema would duplicate those contracts and risk scope narrowing.
- `docs/research-synthesis-index.md` was not expanded: the core grouped conclusion—source provenance does not propagate authority through transformation, and criteria require applicability, observability, and consequence evidence—is already canonical there. This review adds a new source channel and test cases rather than changing that conclusion.

## Assessment

- **Evidence tier:** B — complete immutable paper and official conference version read; real project rule and prompt channels; small reported annotation checks; no study artifacts, coded data, independent reliability, realized behavior, or outcomes.
- **Relevance tier:** A — directly informs the expertise-to-evaluation authoring graph, but with weak evidence for criterion validity.
- **Most reusable contribution:** project rule files as pre-rubric evidence of candidate local operating requirements and interaction boundaries.
- **Strongest empirical evidence:** 91 selected early-adopter project files contained a diverse set of explicit standards, procedures, quality requirements, problem-solving heuristics, and collaboration directives; the official paper reports file-level mention frequencies.
- **Most serious methodological limitation:** three opaque, non-equivalent qualitative pipelines with minimal human-validation samples and no released corpus, codebook, prompts, labels, interview materials, disagreement, or saturation evidence.
- **Most serious validity warning:** naturally authored rules are simultaneously preferences and interventions; projecting them directly into hidden universal criteria would launder local declarations into professional truth and conflate rule compliance with collaborative benefit.
- **Safe claim:** in a July 2025 early-adopter snapshot from 91 projects at one large technology company, selected rule files expressed candidate standards, quality, problem-solving, and collaboration expectations that the authors organized into 15 attributes. Interviews with 15 experienced users and selected prototyping prompts suggest that desired emphasis may differ between present and aspirational systems and between two software contexts. The studies do not establish taxonomy completeness, representative prevalence, criterion or judge validity, realized behavior, collaboration quality, productivity, professional validity, cross-domain transfer, or readiness.
