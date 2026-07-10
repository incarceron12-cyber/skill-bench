# Cognitive task analysis as an evidence-generating authoring method

**Status:** deep primary-source method review and skill-bench adaptation  
**Reviewed sources:** Militello et al., *Applied Cognitive Task Analysis (ACTA) Methodology* (NPRDC-TN-98-4, November 1997); Hoffman et al., *Protocols for Cognitive Task Analysis* (expanded IHMC edition, 2008), checked against the archived 2005 DTIC edition.  
**Canonical records:** [ADA335225](https://apps.dtic.mil/sti/citations/ADA335225) and [ADA475456](https://apps.dtic.mil/sti/citations/ADA475456)

## Evidence and scope

This review is based on the complete local reports, not abstracts:

- `data/sources/ADA335225-applied-cognitive-task-analysis-methodology.txt` (complete OCR of the 193-page scan; SHA-256 `706a1744c7acb86d7355d3b659ea0bda2ed45d4a16a604f0f1f6bffbbafc2e5d`)
- `data/sources/pdfs/ADA335225-applied-cognitive-task-analysis-methodology.pdf` (SHA-256 `947b271f5df2fbdb09f76b585c32f4fb237617e18a6611cab13a0511115f5b97`)
- `data/sources/ADA475456-2005-protocols-for-cognitive-task-analysis-dtic.txt` and `data/sources/pdfs/ADA475456-2005-protocols-for-cognitive-task-analysis-dtic.pdf`
- `data/sources/ADA475456-2008-protocols-for-cognitive-task-analysis-ihmc.txt` and `data/sources/pdfs/ADA475456-2008-protocols-for-cognitive-task-analysis-ihmc.pdf`
- `data/sources/ADA335225-applied-cognitive-task-analysis-methodology.provenance.json` and `data/sources/ADA475456-protocols-for-cognitive-task-analysis.provenance.json` record URLs, acquisition methods, page counts, and hashes.

The ACTA scan is image-only; its complete Internet Archive OCR is readable but flattens some tables. Important procedures and evaluation values were checked against the repeated job aids and report tables in the same scan/OCR pair. The cleaner 2008 IHMC text extraction preserves PDF page breaks and was used to verify the companion protocols. Page references below are printed report/PDF page labels, not text-extraction line numbers.

## Contribution and research question

The ACTA project asks whether cognitive task analysis can be made usable by non-specialist instructional designers without losing the experience-based judgments that behavioral decomposition omits. Its contribution is not merely an interview guide. It is a compact transformation system:

1. locate cognitively demanding work;
2. elicit contextual examples, cues, strategies, and novice contrasts;
3. reconstruct judgment in a challenging incident;
4. consolidate statements into a Cognitive Demands Table; and
5. turn those demands into training objectives and materials.

The companion protocols broaden this into a field-research repertoire: document analysis, recent-case walkthroughs, proficiency scaling, workplace observation, decision/action requirements analysis, protocol coding, Critical Decision Method (CDM), and Goal-Directed Task Analysis. This broader source answers a second question that ACTA leaves underdeveloped: how should an analyst establish who counts as an expert, triangulate interviews with observed work and documents, preserve the temporal structure of decisions, and verify the resulting model?

For skill-bench, the relevant general hypothesis is: **structured critical-incident elicitation can produce better provenance-bearing benchmark primitives than generic requests for “expert best practices,” but the elicited claims still require corroboration, variation sampling, and artifact-level validation.** This advances charter objectives B and C without selecting any particular profession.

## Method and system

### ACTA's four-stage core

**Task Diagram.** The expert decomposes a named task into roughly three to six broad steps, marks which require judgment/problem solving, and only decomposes further when the first level is too broad. The diagram is explicitly a roadmap, not a complete process model (ACTA pp. 5–6; final job aid D-37–D-38).

**Knowledge Audit.** For the cognitively demanding parts, the interviewer requests concrete examples across recurring expertise categories: past/future projection, big-picture integration, perceptual noticing, job smarts, improvisation/opportunities, and self-monitoring; anomalies and misleading equipment are optional probes. Every example is followed by “what cues and strategies?” and “why difficult for a less-experienced person?” (ACTA pp. 7–9; D-39–D-40). This order was empirically revised to avoid repeatedly switching the expert between expert and novice perspectives (p. 38).

**Simulation Interview.** A challenging paper, video, or interactive scenario is segmented into major events/turning points. For each event the interviewer elicits actions, situation assessment, critical cues, and likely novice errors (ACTA pp. 10–11; D-41–D-42). The report removed an alternatives probe because novice interviewers could not distinguish it from likely-error material and reversed assessment/action order to fit natural storytelling (p. 38). Low fidelity is acceptable; challenge and decision relevance matter more than visual realism.

**Cognitive Demands Table (CDT).** Interview material is consolidated into difficult cognitive elements, why each is difficult, common errors, and cues/strategies. The table is the bridge from talk to application. ACTA's evaluation then required users to derive at least ten learning objectives and revise a manual (pp. 26–29). For benchmark authoring, the analog is not “copy the table into a rubric”; it is to translate each supported demand into a claim, primitive, critical-incident variation, artifact obligation, and observable check.

### The companion protocol's controls

The expanded protocol supplies controls absent from a one-session ACTA recipe:

- **Bootstrap before interviewing.** Analyze basic documents so expert time is not spent defining elementary concepts, while remembering that procedures omit local heuristics and workarounds (2008 pp. 6–7).
- **Define expertise empirically.** Combine breadth/depth of career experience, performance evidence, and peer/sociometric judgments; years alone are insufficient (pp. 16–18). Select participants across assignments and local contexts, including people doing the work daily (pp. 18–20).
- **Observe the work system.** Workspace, activity, role, location, SOP, decision-requirement, and action-requirement analyses reveal artifacts, coordination, interruptions, and actual deviations that retrospective accounts can miss (chapters 4–5).
- **Use CDM for consequential incidents.** CDM performs multiple passes: incident selection, uninterrupted recall, elicitor retelling/correction, verified timeline and decision points, deepening, then counterfactual “what if?” probes (2008 pp. 99–115). Its Decision Requirements Table separates cues/variables, needed information, hypotheticals, options, goals, rationale, situation assessment, and time/effort.
- **Verify transformations.** For protocol coding, independent coders compare both selected passages and assigned codes; disagreements diagnose an underspecified coding scheme rather than merely being averaged away (2008 pp. 82–85). The report gives 85% as a practitioner rule of thumb, not a universal validity threshold.

### Edition distinction

The archived 2005 DTIC report is a 109-page protocol collection attributed principally to Hoffman. It covers bootstrapping, proficiency scaling, workplace analysis, protocol analysis, cognitive modeling, and a shorter GDTA treatment. The expanded 2008 IHMC edition is 135 pages, explicitly credits Crandall, Klein, Jones, and Endsley, reorganizes GDTA, and adds the full standalone CDM chapter with six sweeps, boilerplate forms, final integration, and Decision Requirements Table. Therefore the 2008 CDM details must not be cited as if they appeared in the 2005 accession edition.

## Evidence

ACTA evaluated 23 graduate psychology students with no target-domain, CTA, or substantial course-design experience across firefighting (12) and electronic warfare (11). After a shared two-hour introduction, matched students were randomized to unstructured interviewing or an additional six-hour ACTA workshop. Each led one expert interview, observed another, and created a CDT, learning objectives, and manual revisions in a controlled four-hour session (ACTA pp. 25–27).

The strongest evidence is **feasibility**, not superiority:

- Among ACTA users, 92% of firefighting and 94% of electronic-warfare CDT items were coded as cognitive. A domain expert judged 95% and 90%, respectively, as information likely known by experienced personnel (pp. 33–34).
- Firefighting outputs were mostly accurate (89% of manual modifications and 92% of objectives), but electronic-warfare accuracy fell to 65% and 54%. The authors attribute this to technical terminology and domain unfamiliarity (p. 34). This is direct evidence that extracting a valid judgment does not guarantee faithful professional wording or artifact construction.
- Cognitive-category coding reached 74% agreement on 30% of data; task-specific firefighting coding reached 81% on 40%. Firefighting expert agreement ranged from 71.4% to 90.1% depending on rating, while electronic-warfare experts failed the authors' adequacy criterion (34.2%–67.9%) because ship and teaching contexts differed (pp. 27–29).
- ACTA users consistently covered broad categories such as information collection and situation analysis, but did not produce identical demands. Specific-item overlap was abandoned because granularity and wording made matching too inferential (pp. 35–36).
- The ACTA versus unstructured comparison found few robust differences. Samples were tiny, within-group variance was large, and the control group had already learned cognitive concepts and the CDT representation—likely contaminating the treatment contrast (pp. 36–38). Confidence improved, but the study does not establish that ACTA uniquely produces better downstream artifacts.
- The attempted CDM criterion failed: only two firefighter and three electronic-warfare experts were available, below the authors' typical minimum of six, so those outputs were not comprehensive enough to serve as ground truth. Qualitatively, CDM yielded broader demands with much greater depth (Appendix C, pp. C-4–C-5).

These results support a bounded claim: briefly trained novices can use the structure to obtain useful cognitive material. They do **not** establish complete expertise capture, stable item-level reproducibility, benchmark validity, or superiority over a well-prepared semi-structured interview.

## Unique insight

The most important transferable insight is that **expertise elicitation is a sequence of lossy transformations, and disagreement identifies scope before it identifies error**.

The electronic-warfare raters did not merely disagree because one rater was noisy. Their standards differed by ship type, sea experience, and course responsibility. A benchmark pipeline that collapses this disagreement into one “expert-approved” rule launders a conditional practice into a universal requirement. Skill-bench should preserve:

`incident evidence → expert interpretation → context/scope → analyst coding → primitive → scenario variation → check`

Each arrow needs its own author, evidence locator, and review state. A contradiction should trigger a context split, counterexample probe, or unresolved-variation record before adjudication.

A second insight is methodological: **representation can act as both instrument and treatment**. ACTA's control group saw the CDT and cognitive concepts, which may have structured its interviews. The same confound threatens skill-bench whenever experts see the target rubric schema before elicitation. Schema-shaped prompts can improve usable output while manufacturing apparent consensus around categories the benchmark designer supplied. Elicitation records must therefore distinguish spontaneous incident content from probe-elicited and analyst-inferred content.

## Limitations and threats

1. **Small, underpowered comparison.** Eleven ACTA users across two domains cannot support broad effect estimates; the report itself calls group comparisons non-robust.
2. **Treatment contamination.** Both groups received cognitive framing and CDT training, so ACTA-specific causal effects are unidentified.
3. **Criterion failure.** The planned in-depth CDM reference was incomplete and excluded.
4. **Weak item-level reliability.** Category consistency is not semantic agreement. The study abandoned exact overlap analysis.
5. **Expert sampling is context-sensitive.** One or two raters cannot represent heterogeneous professional environments; selecting the “most recent sea experience” rater resolves logistics, not construct validity.
6. **Retrospective and elicitor effects.** Memorable incidents, articulation skill, interviewer skill, probe wording, and supplied scenarios shape what is said. Neither report supplies prospective recall validation.
7. **Application gap.** ACTA validates training-material production, not benchmark task fairness, hidden checks, grader reliability, or agent performance.
8. **Streamlining tradeoff.** The authors explicitly suspect ACTA is less comprehensive and more superficial than CDM or intensive modeling (ACTA p. 39).
9. **Operational cost.** ACTA requires preparation, expert access, interviews, consolidation, and review. CDM sessions may last hours, with transcription and analysis taking comparable time (2008 pp. 103–104).
10. **Historical and domain limits.** The reports predate current AI-mediated work and primarily study military/firefighting/training applications. Their primitives are cross-domain candidates, not contemporary universal facts.

## Reproducibility and operational realism

The reports are unusually reproducible at the procedural level: they include scripts, table structures, workshop materials, and revision rationales. They are less reproducible empirically: raw transcripts, coder assignments, transformed data, randomization details, and analysis code are unavailable. Percent agreement ignores chance agreement and was sometimes measured only until a threshold was reached. The reports do not estimate analyst hours per usable claim, saturation, or test–retest stability.

A realistic skill-bench elicitation therefore needs a session ledger rather than only a polished output. It should retain participant scope, interviewer preparation, exact probe, spontaneous/probed/inferred status, incident timeline, artifacts referenced, contradictions, transformations, review decisions, and time cost. It should also separate four checks:

1. **capture fidelity:** did the record accurately preserve what the contributor meant?
2. **corroboration:** is the claim supported by another expert, observed artifact, source, or performance evidence?
3. **scope validity:** where does the claim apply, and what variation changes it?
4. **benchmark utility:** does the claim produce a fair scenario distinction and observable consequence?

## Mapping to skill-bench primitives

| CTA output | Benchmark primitive | Required guardrail |
|---|---|---|
| Task Diagram expertise hotspot | workflow stage / decision locus | do not treat three-to-six steps as a complete workflow |
| Knowledge Audit example | elicited claim + incident evidence | label spontaneous, probe-elicited, and analyst-inferred content |
| cue or pattern | source-pack evidence locator / observation requirement | record modality, availability, ambiguity, and provenance |
| “why difficult for novices” | failure hypothesis / hidden-requirement candidate | validate in trials; expert prediction is not observed agent failure |
| anomaly or misleading equipment | contradiction or trap | require authority, scope, freshness, and public-basis fairness |
| improvisation / SOP departure | conditional procedure or caveat | safety/compliance review; never equate workaround with approved practice |
| self-monitoring | verification or recovery requirement | specify observable state and threshold |
| Simulation/CDM turning point | critical-incident scenario and difficulty knob | preserve event order and counterfactual variation |
| likely novice error | planted failure signature / grader test case | calibrate against accepted alternatives |
| action, assessment, cue | trace edge and artifact/check crosswalk | avoid grading private reasoning unless externally observable |
| Decision Requirements Table | decision record: information, options, goals, rationale, time | preserve rejected alternatives and uncertainty |
| rater disagreement | contradiction / context split | no silent majority vote or authority laundering |
| client interview | stakeholder decision and artifact convention | include downstream usefulness, not practitioner preference alone |

## Concrete next actions

1. Use `templates/expertise-elicitation-session.md` for the next real expert contribution. It combines a lightweight ACTA pass with optional CDM deepening and records transformation provenance rather than pretending the interview directly emits rubric truth.
2. Extend the expertise-transfer contract with a typed elicitation-session record only after exercising the template once. The needed fields are probe origin, response evidence locator, spontaneous/probed/inferred status, incident/timepoint, contributor scope, corroboration and contradiction links, transformation lineage, and capture/scope/benchmark-utility reviews.
3. In the first pilot, compare a short generic “best practices” interview against the structured session on useful-yield measures: unique evidence-backed primitives per expert-hour, contradiction discovery, expert correction rate, downstream checkability, and unsupported-claim rejection. Do not use rubric completeness as the primary outcome because the elicitation schema itself can manufacture that completeness.
4. Require at least one expert read-back/correction pass and one independent context challenge before promoting a claim into a hidden check. CDM retelling validates capture; it does not validate universality.

## Bottom line

ACTA provides a practical front end for finding cues, judgments, anomalies, strategies, and novice failure hypotheses. CDM and the broader CTA protocols supply the missing temporal, observational, participant-selection, and verification controls. Their combined lesson is not “interview experts and write down rules.” It is to treat expertise transfer as an auditable, context-sensitive evidence pipeline whose outputs remain hypotheses until corroborated, transformed into observable consequences, and tested.