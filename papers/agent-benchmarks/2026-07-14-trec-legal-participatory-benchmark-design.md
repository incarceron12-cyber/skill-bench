# Paper Review: Participation Becomes Benchmark Evidence Only When It Changes Authority, Not Merely Attendance

- **Paper:** https://arxiv.org/abs/2203.06246v1
- **Authors:** Fernando Delgado, Solon Barocas, and Karen Levy
- **Date read:** 2026-07-14
- **Venue / source:** PACM HCI 6(CSCW1), Article 51; immutable arXiv v1; DOI `10.1145/3512898`
- **Tags:** participatory-design, domain-expertise, common-task, interactive-evaluation, adjudication, metric-validity, expert-labor
- **Local PDF:** `data/papers/pdfs/2203.06246v1-participatory-design-trec-legal.pdf` (23 pages; SHA-256 `d13192a00949c0ec51745c7e729eb58cb6e1a0b877deba03057aacad1d816112`)
- **Local text:** `data/papers/text/2203.06246v1-participatory-design-trec-legal.txt` (SHA-256 `5c6f8b7cddbbd0cc8505bad3008b14fa1dc1227e7e379127b14c46fef6e76868`)
- **Primary-track evidence:** `data/sources/trec-legal-track/provenance.json` (34 official/cited records; all local paths and hashes reverified), with six annual overview texts and five protocol/reflection texts under `data/sources/trec-legal-track/text/`; local judgment and evaluation artifacts under the ignored `data/sources/trec-legal-track/artifacts/`

## One-sentence contribution

Delgado, Barocas, and Levy reconstruct the 2006–2011 TREC Legal Track as a rare case in which litigators helped originate the problem, author simulated matters, define the operative relevance target, train technical teams, adjudicate disputed labels, and reshape later rounds—but the strongest transferable lesson is narrower than the paper's co-design rhetoric: **participation affected the benchmark because domain practitioners held explicit authority over requirements and disputed evidence, while the archival record does not show representative stakeholder control, causal benefit from participation, or valid simulation of litigation as a whole.**

## Why this matters for skill-bench

This review advances charter objectives A, B, and F through expansion into a multi-year participatory benchmark venue. The concrete evidence is the complete 23-page case-study paper plus a hash-verified pack of all six official annual overviews, the core interactive protocols and reflections, and representative topics, judgments, adjudication states, and executable metric artifacts. The uncertainty clarified is what must be observable before `skill-bench` calls benchmark authoring “participatory” rather than expert consultation.

The general cross-domain hypothesis tested by this legal case is: **a role-play can serve as a boundary object through which experts and builders jointly discover hidden requirements, but only if experts can alter the task, define or contest the measurement target, inspect system behavior, and force instrument revision.** The case motivates that hypothesis; it does not establish that simulation is sufficient, participation is low cost, or one authoritative expert represents a profession or affected community.

This is not a proposal to narrow `skill-bench` to law or document retrieval. The reusable machinery is a typed decision-rights and disagreement lineage spanning task origin, scenario construction, clarification, assessment, adjudication, metric interpretation, and benchmark revision. Useful completion means future benchmark records can distinguish attendance, advice, authorship, operational authority, veto, adjudication, and release-claim approval—and can show which contribution actually changed which benchmark version.

## Research question and claim boundary

The paper asks why robust participation took hold in the Legal Track, how it was operationalized, and whether it helped lawyers and computer scientists translate and resolve concerns across disciplinary boundaries (pp. 2, 7). It interprets the venue as participatory design even though participants themselves described it as information-retrieval evaluation rather than “co-design” or “AI” (pp. 8–9).

The evidence supports a historical claim that a small, high-status group of legal and technical professionals built an unusually interactive evaluation program and repeatedly revised it in response to observed failures. It supports concrete claims that lawyers originated the venue, authored fictional complaints and production requests, assessed documents, served as Topic Authorities (TAs), supplied clarification and examples, and finally adjudicated selected disagreements.

It does **not** establish:

- that the venue represented litigants, junior review workers, civil-society interests, or the legal profession;
- that the simulation validly reproduced litigation strategy, confidentiality, privilege, adversarial negotiation, production consequences, or professional liability;
- that participation caused better systems or later TAR adoption;
- that TA guidance transferred tacit expertise comprehensively;
- that one TA's relevance conception was a profession-wide truth;
- that the model was affordable without NIST infrastructure, pro bono firms, volunteers, and several years of iteration; or
- that the process generalizes to domains without codified duties, high-status experts, or established institutions.

## Methodology

### Retrospective case study

The authors use an illustrative historical case study, not an intervention study. They report qualitatively reviewing and coding 76 official Legal Track documents—protocols, annual overviews, lessons-learned memos, and participant proceedings papers—plus 26 research and legal publications, for 102 documents total (pp. 7–8). They add seven approximately one-hour semi-structured interviews conducted over June–July 2021. Interviewees included the majority of coordinators and all coordinators who served for at least two rounds. Interviews covered entry into the venue, coordinator roles, differences from other TREC tracks, and lawyer–computer-scientist interaction (p. 8).

The first author had worked in e-discovery for more than a decade and participated marginally through his employer's 2008 and 2009 teams, but was neither a central team member nor a coordinator (p. 9). This insider knowledge aids interpretation and creates an actor–analyst perspective the paper discloses.

Important analytic details are absent: the paper gives no interviewee role table, invitation/refusal denominator, demographic or institutional coverage, interview guide, codebook, coder count, agreement procedure, negative-case protocol, saturation claim, member checking, or archive-to-theme trace. The interviews occurred roughly a decade after the track and sampled coordinators—not participating teams, volunteer assessors, professional reviewers, unsuccessful would-be participants, affected litigants, or critics. Coordinator recollection therefore disproportionately shapes the paper's explanation of why the venue “worked.”

### Primary-record audit performed for this review

The local evidence pack does not reproduce all 102 documents studied by the authors. It does, however, permit direct checking of the central mechanism claims against 34 official or paper-cited records:

- every annual NIST overview from 2006 through 2011;
- the 2007 interactive-task page, 2008 and 2009 interactive guidelines, 2008 topic guidelines, 2009 TA reflections, and 2006–2009 lessons-learned memo;
- representative official topics, qrels, pre/post-adjudication records, evaluation drivers, and metric sources from every year.

All 34 manifest records and all extracted-text hashes were reverified locally with zero missing paths or mismatches. The pack contains inspectable evolution rather than only retrospective testimony. For example, the 2010 message-level pre/post files each contain 25,507 rows, with 870 rows changed between states; the document-level pair each contains 46,331 rows, with 1,815 changed. These counts demonstrate preserved adjudication effects, though they do not identify which changes were correct or caused by participation.

## System and benchmark evolution

### 2006–2007: realistic corpus and requests, weak authority alignment

The 2006 track began as a conventional shared task over roughly seven million heterogeneous tobacco-litigation records. Lawyers associated with the Sedona Conference authored five fictional complaints and mapped them to production requests. The 2006 overview records 43 selected topics, six teams, and 31 scored runs. It also exposes early projection failures: topics were screened by organizers and a professional searcher before final assessors were recruited; assessment guidance changed during review; assessors differed in broad versus narrow interpretations; and some conducted independent legal research (`2006-overview.txt`, lines 203–216 and 300–367).

Sampling was not incidental infrastructure. Because exhaustive review was impossible and high recall made ordinary shallow pooling unsafe, organizers sampled documents beyond submitted pools and estimated precision and recall. The 2007 overview reports 13 teams, 68 ad-hoc runs, pools extending to 25,000 per run, and a new deep-sampling estimator. The final negotiated Boolean query averaged only 22% estimated recall, but no submitted run exceeded it on mean estimated Recall@B (`2007-overview.txt`, lines 196–303 and 454–486). The result showed both task difficulty and measurement dependence; it was not a clean comparison of generic search methods.

The 2007 interactive pilot introduced human search processes, but the primary records describe independent assessors and participant–assessor agreement rather than the mature TA authority structure. The paper appropriately dates the formal TA role to 2008 (pp. 11–12).

### 2008–2010: Topic Authority as requirements owner and adjudicator

The 2008 protocol made three consequential changes: one experienced attorney became the sole Topic Authority for a topic; teams could use up to ten hours of that TA's time through calls, email, questions, and exemplar judgments; and each team had to classify the full collection as relevant/not relevant. The TA had three roles: clarify scope, guide first-pass assessors, and issue final decisions on appealed judgments (`2008-overview.txt`, lines 1030–1078).

This is the strongest evidence for genuine influence. The expert did not merely annotate a builder-defined test. The TA instantiated the target that systems were asked to reproduce, authored evolving guidance, and could overturn labels used in scoring. Teams could inspect preliminary scores and sampled labels, appeal judgments they believed contradicted prior guidance, and receive a final TA disposition. In 2008, 966 assessments were appealed; 762 (78.9%) were changed in the appealing team's favor, overwhelmingly on one topic (`2008-overview.txt`, lines 1391–1410). That magnitude shows that initial “ground truth” was a revisable output of role-governed disagreement, not an untouched expert fact.

Yet access was unequal and private. TAs were asked not to volunteer team-specific information learned through one interaction to another team. Most teams used little of the ten-hour allowance: excluding one intensive team, 2008 teams averaged about 60 minutes, while one used 485 minutes (`2008-overview.txt`, lines 1268–1319). The 2009 TA reflections say very few teams used much allotted time and many failed to formulate useful questions. TAs preferred iterative, exemplar-linked, grey-area questioning and often live calls because these exposed their thought process (`2009-topic-authority-reflections.txt`, lines 7–81).

The 2009 overview reports a positive but inconclusive association between TA minutes and post-adjudication F1, `r = 0.424`, 95% CI `[-0.022, 0.730]`. It explicitly says the data cannot establish significance and that interaction quality may matter more than quantity (`2009-overview.txt`, lines 970–1023). Appeals rate correlated strongly with score improvement, `r = 0.862`, but this is mechanically and behaviorally endogenous: teams with better TA understanding could both choose more successful appeals and already classify better, while appeals directly changed the labels used to score them (lines 1025–1088). Neither result identifies a causal participation effect.

The venue learned from this dependence. In 2008–2009, only participant-appealed labels reached TAs, so teams that did not appeal left likely errors intact. In 2010, professional review firms performed all first-pass review; about 10% of sampled messages received a second assessment; selected non-appealed cases also went to the TA; and adjudication was blinded to initial label, proposed alternative, appealing team, and appeal status (`2010-overview.txt`, lines 1142–1201). This is instrument redesign caused by observed process failure.

The 2010 evidence also undercuts any simple “human gold standard.” Across 2,769 twice-assessed messages, raw agreement was 90.9%, but positive-set overlap was only 50.4%; the overview correctly notes that class imbalance inflated overall agreement (`2010-overview.txt`, lines 1577–1641). TAs changed about 38% of appealed messages and 24% of sampled non-appealed messages; 870 of 25,507 released message-level labels differ between the preserved pre/post files. However, dual assessments came from the same review firm and could even have been produced twice by the same person, so they are repeated decisions, not necessarily independent raters.

### 2011: constrained feedback, calibration, and explicit effort

The final year merged interactive and learning tasks. Ten organizations ranked all 685,592 documents for three topics and supplied a probability of responsiveness for every document. Teams could request up to 1,000 binary TA determinations per topic, staged 100/200/700, but after a kickoff no other open-ended TA communication was allowed (`2011-overview.txt`, lines 19–35 and 198–227). This changed the expert channel from evolving dialogue toward a bounded label budget.

The gold standard used 16,999 sampled documents. Four professional review companies supplied assessments pro bono at the company level; reviewers were apparently paid. Most random-stratum documents received two assessments, and TAs blindly adjudicated disagreements (`2011-overview.txt`, lines 81–131). Teams self-reported setup, search, review, and analysis effort ranging from a few hours to hundreds, with one run reporting 655 total hours (lines 229–300). These are useful operational fields, not controlled cost estimates.

The evaluation separated ranking from self-calibration. Teams often achieved useful ranking at selected cutoffs, but most dramatically overestimated recall, creating a concrete premature-stopping hazard (`2011-overview.txt`, lines 433–507). The overview also states that F1 adds no information beyond recall given cutoff and total prevalence, despite earlier years using balanced F1 to symbolize the legal tradeoff between exhaustiveness and affordability (lines 340–348). Metric meaning therefore evolved with the decision problem; “the metric was co-designed” should not imply one stable validated scalar.

## Evidence and strength of support

### What is strongly supported

1. **Practitioner-originated problem framing.** The archival account consistently places attorney Jason Baron and legal organizations upstream of the track proposal, rather than as late-stage validators (paper pp. 9–11).
2. **Substantive expert roles.** Lawyers authored matters and requests, assessed records, provided examples and clarification, trained reviewers, adjudicated disputed labels, and reflected publicly on system and human-review failures.
3. **Iterative instrument change.** The official records preserve movement from ad-hoc assessment to a TA-centered interactive protocol, then professional and dual assessment, blind adjudication, sampled non-appeal escalation, bounded active feedback, probability calibration, effort reporting, and explicit claim restrictions.
4. **Disagreement as evidence.** Appeals, pre/post qrels, dual assessments, uncertainty intervals, and low positive overlap make judgment instability inspectable rather than hiding it behind a single final label.
5. **Operational burden.** The task constrained topics because interactive evaluation was resource intensive, depended on volunteers and pro bono firms, capped TA time and team count, and still reported delays, incomplete phases, assessment defects, and data problems.

### What is interpretive or weakly supported

1. **“Neutralized” knowledge asymmetry.** Giving TAs target and adjudication authority shifted some power, but technical coordinators still controlled sampling, metric estimators, schedules, eligibility, release artifacts, and protocol revision. The study does not measure perceived power or decision influence across roles.
2. **Participation caused successful translation.** TAR later gained legal legitimacy, but the paper supplies no counterfactual, adoption pathway analysis, or separation of Legal Track effects from data growth, vendors, court decisions, cost pressure, and parallel research.
3. **Persistent rejection of simplification.** The track preserved large corpora and high-recall concerns, yet also simplified aggressively: fictional complaints, one TA per topic, binary responsiveness, sampled labels, static snapshots, selected topics, compressed vendor roles, and no real production consequences.
4. **Mutual learning.** Coordinator interviews and TA reflections report learning, but there are no pre/post measures, participant interviews, retained learning tests, or evidence that unsuccessful and peripheral participants learned similarly.
5. **Better performance from interaction.** The minute–F1 association is imprecise and confounded; appeal–gain is endogenous to both label revision and team choice. No randomized or matched interaction treatment exists.

## Unique insight

The paper's most valuable implication is not “include experts.” It is that **participation is a versioned causal input to the benchmark instrument**. A contribution becomes consequential when it changes one of five loci:

`problem legitimacy → task/source construction → operative requirement → evidence/adjudication rule → interpretation/revision decision`

The Legal Track placed lawyers at several of these loci. It also preserved evidence that their interventions changed labels and later protocols. `skill-bench` should therefore evaluate participation by contribution-to-change lineage, not by participant count, workshop hours, or an undifferentiated `expert_involved` flag.

A second insight is that **role authority and epistemic truth are different**. The TA's label was authoritative because the simulated vendor was tasked with reproducing that attorney's conception—not because the TA represented the only professionally valid interpretation. This distinction is essential for knowledge-work benchmarks. A task may validly test fidelity to a named decision owner while supporting no claim about universal best practice. The benchmark must bind authority to role, matter, source set, time, and decision scope.

Third, **adjudication is itself a treatment over measurement**. Appeals documentation helped TAs notice subtle evidence but could reveal the desired answer and the appealing team; blind adjudication reduced that influence but removed salience cues and coincided with lower overturn rates. There is no context-free “expert adjudication.” Evidence view, party identity, rationale visibility, time, and prior guidance can all alter the label. These must be configured and compared, not buried in the final qrel.

Fourth, **the benchmark can teach the experts and thereby change its construct**. TAs learned that human review was inconsistent; technical teams learned that relevance was dynamic and strategic; metrics shifted from balanced F1 toward decision-calibrated recall estimation. This is productive, but it means later rounds do not measure the same fixed instrument. Benchmark evolution must preserve bridge items, version boundaries, and claim reassessment rather than treating cumulative improvement as comparable progress.

Finally, the case exposes a participation-validity tension: private iterative access makes the simulation more realistic and creates richer requirements, but it also gives systems non-equivalent information and allows the evaluated teams to influence the labels that score them. Co-design and confirmatory evaluation therefore need separate phases or explicit treatment records.

## Transferable design patterns

### 1. Participation decision-rights record

For every expert or stakeholder contribution, preserve:

- role and expertise basis, constituency represented, and exclusions;
- whether the person may propose, author, review, adjudicate, veto, or approve a release claim;
- exact contribution and evidence locator;
- benchmark locus affected: problem, source, task, skill, criterion, grader, metric, validity claim, or release;
- disposition, disagreement, rationale, and responsible decision owner;
- before/after artifact hashes and benchmark versions; and
- whether authority is role-local, matter-local, domain-local, or asserted to generalize.

Attendance without a disposed contribution is engagement evidence, not co-design evidence.

### 2. Requirement-clarification ledger

TA interaction suggests a reusable event structure:

```yaml
clarification_event:
  task_version: ...
  expert_role: named decision owner and scope
  requester: configured team/agent
  trigger: source inspection | exemplar | ambiguity | contradiction | boundary case
  question: ...
  evidence_view: exact documents and prior guidance visible
  response: ...
  status: new_rule | refinement | exception | unresolved | superseded
  affected_requirements: [...]
  visibility: shared | condition_private
  elapsed_expert_minutes: ...
  downstream_artifact_hashes: [...]
```

Private clarification is a scaffold treatment. If it is not made common, matched performance comparisons must model unequal evidence exposure.

### 3. Plural disagreement and adjudication states

Never retain only the final expert label. Preserve independent first-pass observations, assessor identity class, evidence view, confidence/abstention, appeal source, rationale visibility, adjudicator state, changed/not-changed disposition, and scoring impact. Sample non-appealed items to estimate errors that active teams fail to surface. Report raw agreement, positive-set overlap or class-appropriate reliability, and uncertainty separately.

### 4. Metric-to-professional-consequence warrant

The track translated recall into completeness and precision into review burden, but equal-weight F1 did not encode all legal costs and was later treated as redundant for cutoff decisions. For each metric, require:

- eligible population and sampling estimator;
- professional consequence represented;
- asymmetric false-negative/false-positive and stopping losses;
- decision threshold and uncertainty rule;
- expert and affected-party dispositions;
- excluded consequences; and
- version trigger when task, prevalence, unit, or use changes.

A professional's acceptance of familiar metric language is not evidence that the aggregation is valid.

### 5. Separate co-design from confirmatory evidence

Use an exploratory authoring phase where experts and systems may interact, appeal, and revise freely. Freeze task, guidance, adjudication policy, metric, and source access before confirmatory trials. If interactive clarification remains part of the target workflow, randomize or standardize access, log all information flow, cluster by task/expert, and treat clarification as a configured intervention rather than background labor.

### 6. Participation claim ladder

Keep claims distinct:

1. `consulted`: input was solicited;
2. `contributed`: a preserved artifact or disposition exists;
3. `influenced`: a versioned benchmark change traces to it;
4. `held_authority`: the contributor owned a bounded decision or adjudication;
5. `represented_constituency`: sampling and governance support a representation claim;
6. `improved_validity`: comparative evidence shows a validity improvement;
7. `improved_outcomes`: downstream consequences improved.

The Legal Track strongly supports levels 2–4 for selected lawyers. It does not establish levels 5–7 broadly.

## Comparison with existing skill-bench evidence

The 2026 domain-expert participation ethnography (`papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md`) shows expert authority decaying through developer/model transformations under deadline and labor pressure. TREC Legal supplies the complementary positive mechanism: authority can be retained when experts own explicit requirements and adjudications, but this is expensive and still requires evidence-view and representation limits.

SimInstruct (`papers/agent-benchmarks/2026-07-11-siminstruct-simulated-novice-elicitation.md`) treats a generated novice as an elicitation intervention over expert behavior. TREC Legal shows a richer reciprocal simulation in which technical teams' questions and exemplars refine the TA's own target. Both cases warn that simulation is not neutral evidence collection: interlocutor behavior selects what expertise becomes visible. Unlike SimInstruct, TREC preserves repeated task revisions and many judgment artifacts; unlike TREC, SimInstruct experimentally varies at least one persona factor. Neither validates simulation against downstream professional consequences.

The nonduplicate synthesis is: **participation lineage governs whose authority survives; elicitation treatment records govern what expertise became observable; adjudication lineage governs how disagreement became measurement; validity arguments govern which claims those records license.** Existing expert-participation, expertise-transfer, benchmark-bundle, metric-monitoring, task-health, and validity contracts are the correct homes. A new standalone “participatory benchmark” schema would duplicate them.

## Limitations and validity threats

1. **Coordinator-centered interview sample.** Seven coordinators cannot represent teams, assessors, professional reviewers, litigants, judges, affected parties, or nonparticipants.
2. **Retrospective recall.** Interviews occurred about a decade after the track; no procedure triangulates specific memories against dated records at the quotation level.
3. **Under-specified qualitative analysis.** No codebook, coder roles, reliability, negative-case protocol, saturation, member checking, or theme audit trail is released.
4. **Actor–analyst proximity.** The first author's industry history and marginal 2008–2009 participation provide access and possible success-story bias; disclosure is not independent validation.
5. **Retrospective relabeling.** Participants did not use “participatory design” or “co-design”; the paper's conceptual mapping is analytically useful but not an observed self-description.
6. **Selection on a celebrated case.** An illustrative successful precedent cannot estimate how often participatory benchmark efforts fail or which mechanism is necessary.
7. **Narrow and elite participation.** High-status litigators and technical researchers dominated; document reviewers, public-interest groups, plaintiffs, defendants, and broader civil society lacked comparable authority.
8. **Representation is not demonstrated.** One TA intentionally supplied one operative conception. That supports client-fidelity simulation, not professional consensus or affected-community legitimacy.
9. **Simulation compression.** Fictional complaints, public data, fixed snapshots, bounded topics, binary labels, and no case consequences omit confidentiality, negotiation, sanctions, changing litigation strategy, and client incentives.
10. **Task target is endogenous.** Team questions and exemplars refine TA guidance; teams then appeal labels and may influence the final qrels used to score them.
11. **Unequal information exposure.** Private TA interaction, different minutes, and non-shared team-specific refinements make runs different treatments, not solely different retrieval systems.
12. **Participation effect is unidentified.** No randomized, matched, or prospective contrast isolates TA interaction, role-play, appeals, or practitioner authorship.
13. **Minute–performance evidence is weak.** The 2009 estimate has a confidence interval crossing zero and omits interaction quality, team resources, prior skill, and topic clustering.
14. **Appeal–gain circularity.** Appeals directly modify scoring labels; successful appeals and score gains are not independent evidence of system capability or participation benefit.
15. **Adjudicator evidence-view effects.** Rationale-bearing appeals may cue TAs; blind appeals may hide decisive features. The protocol change was not randomized.
16. **Human labels remain noisy.** In 2010, positive overlap was about 50%; “dual” assessments could come from the same individual; only selected disagreements were adjudicated.
17. **Low-prevalence fragility.** Annual reports show small numbers of false-positive labels can dominate estimated recall/F1 on rare topics.
18. **Metric warrant changed.** Balanced F1 was normatively interpreted, but 2011 calls it redundant for cutoff decisions; no stable loss function validates aggregation across years.
19. **Cost is incomplete.** TA allocations, assessor batches, pro bono firms, and team hours are visible, but recruitment, coordination, adjudication, infrastructure, and opportunity costs are not totaled.
20. **Incentives are selective.** TA reflections call participation professionally valuable, but there is no invitation denominator, refusal, attrition, compensation, burden distribution, or dissent account.
21. **Cross-year comparability is explicitly invalid.** Corpora, topics, protocols, assessment, metrics, and configured systems changed; the 2011 overview forbids direct performance comparisons.
22. **No downstream causal evidence.** Later TAR legitimacy and adoption cannot be attributed to the track from this study.
23. **Partial study-corpus reproduction.** The local 34-record pack verifies the central track mechanisms but not all 102 documents analyzed by the paper or the interview corpus.
24. **Ignored large artifacts require reconstruction.** The 148 MB qrel/evaluation directory is intentionally not versioned; provenance hashes and URLs support refetching, but a clean clone lacks those files until reacquired.

## Reproducibility and operational realism

Manuscript reproducibility is moderate. The immutable 23-page paper identifies its archive classes, interview count and timing, sampling frame for coordinators, and first-author positionality. Study reproduction is weak because interviews, transcripts, codebook, coding, document inventory, and claim-level source mapping are unavailable.

The benchmark record is unusually inspectable for a historical venue. Official annual reports document topics, roles, protocols, sampling, uncertainty, runs, interaction time, effort, appeals, assessor disagreement, and known defects. The local pack includes qrels, pre/post adjudication states, and executable evaluation sources. This supports auditing how measurement changed; it does not make the underlying corpora or full event history turnkey reproducible.

Operational realism is the case's strength and its claim boundary. The records preserve underspecified requests, evolving relevance, exemplar questioning, scarce expert time, unequal team behavior, reviewer inconsistency, low-prevalence estimation, data-rendering defects, appeals burden, blinded adjudication tradeoffs, large workspaces, self-reported effort, and premature-stopping risk. But the simulation is realistic with respect to one vendor–senior-attorney relationship, not civil discovery in full. `skill-bench` should emulate this honesty by naming the modeled relationship and omitted institutional consequences.

## Concrete repository actions

1. **Do not add a duplicate schema task.** Existing participation, expertise-transfer, benchmark-bundle, metric, task-health, validity, and longitudinal contracts can carry these requirements.
2. **Treat participation as typed decision rights plus change lineage.** A future consolidation should add the participation claim ladder and contribution→artifact-version edge to canonical synthesis, not create a scalar participation score.
3. **Record clarification as a configured intervention.** Interactive expert access needs event locators, visibility, expert minutes, affected requirements, and equivalent-access checks.
4. **Preserve pre-adjudication evidence.** Do not overwrite observations with final labels; bind every score change to the adjudicator's evidence view and policy version.
5. **Validate adjudication views prospectively.** On planted ambiguous cases, compare rationale-visible, blind, and neutral-salience adjudication to test cueing versus omission without claiming professional fidelity.
6. **Separate role-local fidelity from universal correctness.** A benchmark may test alignment with a named expert decision owner while explicitly excluding profession-wide best-practice claims.
7. **Make participation burden a plural outcome.** Track expert, assessor, builder, and coordination time; representation; disagreement; claim-blocking; and reciprocal value separately.
8. **Freeze confirmatory versions.** Co-design and appeals may revise exploratory tasks; released comparative trials need frozen source, guidance, access, adjudication, metric, and validity records.
9. **Require affected-party coverage before representation claims.** Professional authority alone cannot license claims that a benchmark represents all people bearing the workflow's consequences.

## Action items

- [x] Read and verify the complete immutable arXiv v1 PDF/text.
- [x] Reverify all 34 primary-pack local paths and hashes and audit all six annual overviews plus core protocols, reflections, judgment, adjudication, and metric artifacts.
- [x] Reconstruct the 2006–2011 task, role, assessment, metric, and adjudication evolution with paper-page and primary-file evidence.
- [x] Separate archival observations, coordinator interpretations, primary-record verification, and `skill-bench` adaptations.
- [x] Compare the case with the existing domain-expert participation ethnography and SimInstruct review.
- [x] Preserve claim ceilings for representativeness, simulation validity, causality, cost, tacit transfer, professional validity, and cross-domain generalization.
- [x] Add no duplicate queue task; route implications into existing contracts and future canonical consolidation.
