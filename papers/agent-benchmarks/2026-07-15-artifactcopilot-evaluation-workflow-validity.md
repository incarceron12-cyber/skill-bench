# ArtifactCopilot: proof-carrying review workflow, but not autonomous artifact evaluation

## Bottom line

ArtifactCopilot's revised v3 paper makes a useful methodological move: it converts a descriptive professional policy into a phased evidence workflow whose outputs carry criterion links, execution records, intervention burden, confidence cues, and deterministic badge derivations. Its strongest evidence is that explicit `ArtifactGuide` guidance improves three coding agents over a short ACM-policy prompt on one 60-artifact, author-adjudicated instrument, and that ArtifactCopilot completes all administered runs while producing structured reports. The weak Reusable recall and route-dependent mismatches are equally important: organizing evidence is easier than establishing claim support, legitimate transfer, or equivalence among valid review paths.

The paper does **not** establish autonomous artifact evaluation, expert substitution, general evaluator reliability, or professional readiness. The 60 reference decisions were produced by two authors using the same finalized rubric supplied to the agents, after a 24-artifact calibration/adjudication cycle. Agreement therefore measures conformance to a jointly authored instrument, not independent truth or official badge reproduction. The experiment excludes broken-link artifacts, oversamples predicted boundary and negative cases, reports three-run means without inferential uncertainty, compares differently configured harnesses, and cannot separate policy decomposition, phase skills, orchestration, packet checking, or model effects. The eight-person report study measures confidence and perceptions—not decision correctness, time saved, downstream review quality, or automation bias.

The most important release finding is version discontinuity. Immutable v1 was a different 20-page system centered on an Artifact Evaluation Graph, environment normalization, error recovery, 48 artifacts, 85.42% badge agreement, and a reported $0.091 mean cost. Immutable v3 is a 12-page redesign centered on ArtifactGuide, phased skills, packet checking, 60 artifacts, 70.56% exact agreement, repeated runs, and a user study. The v3 paper does **not** describe the old AE Graph. Its cited open artifact is a Figshare secret-share URL, while the separately found restricted Zenodo record appears aligned with the v1-era artifact and cannot establish v3 implementation identity. “ArtifactCopilot” is therefore not one stable instrument across versions.

The transferable result for `skill-bench` is a **proof-carrying review packet with explicit route and intervention provenance**, not a badge oracle:

`policy/authority → criterion version → permitted review phase and route → observed state/action/evidence → intervention/evidence level → check validity → criterion conclusion → decision rule → reviewer adoption/adjudication`

Every arrow needs its own evidence. Completion, report production, badge concordance, repeated-run reliability, reviewer usefulness, and professional decision validity must remain separate outcomes.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, and C through narrow expansion into executable evaluation of complex professional artifacts. Software artifact review is a methodological case, not a scope commitment. The general hypothesis is that expert policy can become a state-aware, evidence-bearing workflow that supports rather than replaces professional judgment.

The concrete evidence is the full immutable v3 paper, a direct v1/v3 source comparison, public release metadata, and preserved failed-access evidence for both candidate release locations. The uncertainty clarified is what policy-grounded criteria, structured execution, repeated agreement, and report-use evidence license. Useful completion means retaining evidence packets and intervention lineage while refusing to promote same-rubric agreement, report availability, or reviewer confidence into evaluator validity or expert substitution.

## Sources and reading record

### Immutable primary paper read in full

- Zhaonan Wu, Yanjie Zhao, Zhenpeng Chen, Zheng Wang, and Haoyu Wang, *Agent-Based Software Artifact Evaluation*.
- Immutable arXiv v3: <https://arxiv.org/abs/2602.02235v3>; PDF: <https://arxiv.org/pdf/2602.02235v3>.
- Version read: v3, submitted 14 July 2026; read 15 July 2026. The metadata contains no withdrawal notice.
- Local PDF: `data/papers/pdfs/2602.02235v3-artifactcopilot.pdf` (12 pages; SHA-256 `5073e25f4155b233bc098d230c95f13951123885ea4efe57ad764667e905d93a`).
- Local full-text extraction: `data/papers/text/2602.02235v3-artifactcopilot.txt` (96,724 bytes; SHA-256 `d7cf9a991c0b58fd7bb9139076bbc04b4e0af017800361d49d2ba41b81cdd193`).
- Acquisition/release provenance: `data/sources/releases/2602.02235v3-artifactcopilot/provenance.json`.

The complete v3 text was read from policy grounding and rubric calibration through the phased system, experimental design, metric tables, mismatch analysis, report study, validity discussion, and references. Page references below use the 12 PDF pages; extracted form-feed boundaries were checked against the PDF.

### Version-history evidence

ArXiv records v1 on 2 February 2026, v2 on 3 February, and v3 on 14 July. Because v3 is a material redesign rather than a normal revision, immutable v1 was additionally fetched and compared:

- v1 PDF: `data/papers/pdfs/2602.02235v1-artifactcopilot.pdf` (20 pages; SHA-256 `1c702e53c77740b7e43028129cb48fa7af2daa3dfcc4ce4fdbb739b446dc1450`).
- v1 text: `data/papers/text/2602.02235v1-artifactcopilot.txt` (96,199 bytes; SHA-256 `d6a7bb64882bf98cf6047fe40838807d31475bec75de50147a307fb7cbfeb748`).

V1 studied manual interventions on an exploration/validation split and built an execution-normalization and README-derived Artifact Evaluation Graph system. It reported 48 artifacts, 85.42% match to human badges, 45/48 zero-human-intervention cases, and $0.091 mean API cost (v1 pp. 1–3 and evaluation sections). V3 replaces those research questions, system description, sample, metrics, and headline results. It adds ArtifactGuide, 20 interviews, 24 calibration artifacts, phase skills/checkers, 60 newly adjudicated artifacts, three-run comparisons, and an eight-person report study. An AE Graph is absent from v3 and must not be silently imported into a v3 review.

### Release boundary

Two different records must not be conflated:

1. **The source actually cited by v3** is the Figshare share URL <https://figshare.com/s/4a21d79f93f92d11f2a1> (reference [1], v3 p. 11). A direct review-time request returned an AWS WAF challenge (`HTTP 202`), so no file list, checksums, rubric examples, phase skills, reports, traces, result tables, or code could be inspected. The response is preserved at `data/sources/releases/2602.02235v3-artifactcopilot/figshare-share-response-{headers.txt,body.html}`.
2. **The separately discovered Zenodo record** <https://zenodo.org/records/18410765> identifies a restricted anonymous ISSTA 2026 “Artifact of ArtifactCopilot,” version v1.0, created before v1 and modified one day before v3. Its files endpoint returned `HTTP 403`; no file names or checksums are public. V1 explicitly discusses Zenodo as an artifact source, while v3 cites Figshare. The record may be related, but available metadata cannot establish its contents or correspondence to v1, v2, or v3.

The paper calls ArtifactGuide's full examples “available in our open-source artifact” (Section III-C, v3 p. 4), but that claim was not operationally verifiable from this environment. Reproducibility and implementation observations below are therefore bounded to the paper and public record metadata; no code or dataset behavior is claimed.

## One-sentence contribution

ArtifactCopilot turns a policy-derived rubric into phase-bounded, intervention-aware evidence packets and deterministic badge traces, but its same-rubric author references, route sensitivity, unvalidated checker, and confidence-only user study support reviewer assistance rather than autonomous or expert-equivalent evaluation.

### Research question and claim boundary

V3 asks four empirical questions (Section V, p. 6):

1. How closely does ArtifactCopilot align with human adjudication?
2. How does it compare with baseline agents under increasingly structured review guidance?
3. How stable are outcomes across three repeated runs?
4. How useful are its reports to experienced software researchers?

It contributes two linked instruments:

- **ArtifactGuide:** an availability gate, five four-level dimensions, representative-workflow criteria, intervention levels, evidence levels, and nested badge rules derived from ACM policy, public venue guidance, interviews, and manual calibration (Sections III-B–C, pp. 3–4; Tables I–II, p. 4).
- **ArtifactCopilot:** fixed phase order, phase-specific skills, tool scopes and completion contracts, transient versus persistent memory, intervention annotation, structural and dialogue packet checks, and reports whose badge decisions link back to evidence (Section IV, pp. 5–6).

The evidence licenses a bounded claim: on this purposively stratified, same-rubric-adjudicated 60-artifact set, the tested explicit guidance changes the output agreement of named configured systems, and ArtifactCopilot has a conservative, report-producing operating profile under three administered attempts.

It does **not** establish that ArtifactGuide is the authoritative or complete operationalization of ACM badge policy; that ArtifactCopilot reproduces venue decisions; that human adjudication is criterion-independent truth; that its packet checker verifies factual evidence; that one route is complete over legitimate workflows; that results transfer across models, venues, artifact types, or time; or that reports improve reviewer correctness, speed, workload, committee decisions, reproducibility, or downstream reuse.

## Methodology and system

### From policy to ArtifactGuide

Phase 1 combines ACM v1.1 policy, ICSE/ASE/FSE/ISSTA guidance, and public review forms. This is a stronger source basis than free-form rubric generation, but the paper does not preserve a criterion-to-source crosswalk showing which policy sentence, venue convention, or community expectation authorizes each gate, score boundary, or weightless threshold (Section III-B, p. 3). The guide claims alignment without redefining badges; that claim needs inspectable transformation lineage.

Phase 2 uses one-on-one semi-structured interviews with 20 people having one or more of AEC service, artifact preparation, or substantial reproduction experience. Participants first elicit dimensions, then inspect the draft and discuss boundaries. Two authors code records and resolve differences by discussion; a rule is generalized when recurring across multiple participants; the final five interviews add no dimensions (Section III-B, pp. 3–4).

This is meaningful calibration evidence, not a complete expertise study. The paper does not report counts by role, venue or domain; years or number of reviews; recruitment and compensation; interview guide; transcripts; codebook; independent coding agreement; recurrence threshold; contradictory views; withdrawals; or changes attributable to specific evidence. “No new dimensions” is thematic saturation under this recruitment and interview procedure, not evidence that decision boundaries or criterion completeness saturated.

Phase 3 starts from 642 research-track papers at four recent conferences, filters to publicly accessible artifacts, stratifies by official badge status, and selects 16 badged plus eight unbadged artifacts. Two authors initially agree on 83.3% of availability gates, 74.2% of 120 dimension judgments, and only 54.2% of final badge types. A third author adjudicates, rules are revised, the same two reviewers re-review the same 24 cases, and residual disagreement disappears; interview participants raise no objections in member checking (Section III-B, p. 4).

This is a productive instrument-development loop. It is not held-out reliability or construct validation. The final full agreement is partly designed: the same cases and disagreement causes were used to alter the rubric, adjudicate the labels, and retrain interpretation. No untouched artifacts or independent reviewers test whether the clarified guide transports. “No objection” is weaker than independent criterion application, alternative-rubric comparison, or consequential validation.

### What ArtifactGuide operationalizes

The availability gate requires public downloadability, an entry point, and paper relation/material beyond text. Five dimensions score reject, weak reject, weak accept, or accept (Tables I–II, p. 4):

1. documentation quality;
2. environment reconstruction;
3. workflow executability;
4. claim support; and
5. reusability.

Representative workflow rules require documentary grounding, an evaluation-relevant operation, interpretable output, paper/target mapping, and a stated coverage limit. Intervention levels range from running as documented (`I0`) through semantic changes to algorithm/model/metric/core processing (`I4`). Evidence ranges from no executable evidence (`E0`) through static/precomputed material (`E1`) to reviewer-executed representative (`E2`) or near-full paper-facing (`E3`) output. Functional requires availability, dimensions 2–4 at least weak-accept, E2+, and no I4; Reusable adds dimensions 1 and 5 plus transfer validation.

These distinctions transfer well: execution is not claim support; static output is not reviewer-observed execution; and reviewer repair must not be laundered into original artifact quality. Yet several boundaries remain authored rather than validated:

- `WA` is declared as the positive threshold without a loss or downstream-decision study.
- “Representative,” “valid output,” “main result,” “semantic-preserving,” “low intervention,” and “new input/configuration/scenario” retain substantial judgment.
- Dimensions are dependent. Environment enables execution; execution enables claim support; documentation affects route discovery and repair; reusability requires functional evidence. A single error can cascade into multiple negative dimensions and the final badge.
- The badge rules permit one canonical-looking path to dominate even when multiple legitimate routes exist; the paper's own mismatch analysis shows route choice changes outcomes.
- Environment/service unavailability, artifact defect, evaluator setup error, and resource-policy exclusion are not cleanly separated.
- The guide is co-developed and then used both to create references and to guide candidates, making criterion agreement partly endogenous.

### ArtifactCopilot orchestration and evidence packets

ArtifactCopilot processes availability, D1, D2, D3, D4, D5, and report generation in fixed order (Figure 2 and Section IV, pp. 5–6). Each phase skill specifies objective, tool scope, evidence contract, and completion criteria. Working memory retains transient planning; persistent memory receives only committed phase summaries, logs, and intervention records. The availability gate can early-stop. The report includes deterministic badge derivation, criterion-linked dimension scores, intervention/evidence levels, and confidence/cross-validation flags.

The packet checker performs structural file checks and a maximum five-turn dialogue check for evidence–conclusion consistency. Failed packets are revised before transition. This is a promising proof-carrying pattern: evidence is explicit, phase admission is fail-closed, and report claims have locators.

However, the paper provides no checker calibration, prompt/model identity, independent labels, false-accept/false-reject study, or adversarial packets. File existence is not evidence truth. A dialogue model checking logs supplied by the same review agent can share the same misconception or accept fabricated/irrelevant evidence. Confidence is estimated from evidence completeness and intervention burden, but no calibration curve connects it to error probability. The script-based intervention rules are not described or inspectable. Persistent summaries may omit contrary raw evidence, and phase commitment can amplify an early route mistake.

The fixed sequence also constrains legitimate professional behavior. Section V-C reports that ArtifactCopilot sometimes tries one documented entry point, encounters a failure, and commits to a low score while Codex explores another documented route and recovers (pp. 8–9). That is not merely weaker execution; it shows orchestration is part of the measurement instrument. A robust workflow needs route-set provenance, bounded backtracking, alternative-path equivalence, and an explicit distinction among `artifact_path_failed`, `environment_invalid`, `budget_exhausted`, and `all_admissible_paths_failed`.

### Evaluation sample and reference decisions

The authors exclude 24 calibration artifacts and broken links from the 642-paper source pool, leaving 369. A manual pre-label without full execution yields 104 likely Functional, 246 boundary, and 19 clearly failing Availability cases. The 60-case evaluation sample contains 30 likely Functional, 20 boundary, and 10 predicted Availability failures. Two authors then independently apply the finalized guide; a third adjudicates disagreements from preserved evidence. Initial badge-level Cohen's kappa is 0.85. The final distribution is 6 no badge, 20 Available only, 13 Available+Functional, and 21 Available+Functional+Reusable (Section V-A, pp. 6–7).

This improves on using historical badges blindly. But “human-adjudicated” needs a narrow reading:

- reference reviewers are authors of the instrument, not independent AEC panels;
- references and candidates use the same guide, creating rubric-alignment bias acknowledged by the authors (Section VI-C, pp. 10–11);
- the paper gives kappa only at final badge level, not gate/dimension confusion, rater identities, uncertainty, or adjudication rate;
- discussion adjudication can produce a consensus label without resolving legitimate policy plurality;
- broken-link exclusion removes a consequential real-world failure class before evaluating availability and operational robustness;
- the 30/20/10 allocation deliberately changes prevalence, so precision, recall, and agreement are instrument-sample properties rather than venue-population estimates; and
- the paper does not report the exact sampling algorithm, source IDs, artifact snapshots, reference evidence packets, or release-time hashes.

The reference is best understood as an **author-adjudicated ArtifactGuide label set**, not official badge truth or expert-independent correctness.

### Configured systems and treatment comparability

The comparison crosses OpenHands, Cline, Codex, and ExecutionAgent with ACM policy, ArtifactGuide, and Skills+ArtifactGuide, then adds ArtifactCopilot (Section V-A and Table IV, pp. 7–8). All use a named DeepSeek-V4 Flash backend where possible; Codex reaches it through CC-Switch. Framework defaults remain in place, while budgets differ: OpenHands has 150 iterations and ten retries, Cline 150 requests and no timeout, ExecutionAgent 150 steps and one retry, and ArtifactCopilot 150 steps. The experiments use Ubuntu 22.04 and A100-80GB hardware.

This is a configured-system comparison, not a clean model, rubric, skill, or orchestration ablation. Native tool interfaces, context management, retry semantics, termination, prompt topology, report parsing, and model adapter behavior differ. The same model name does not guarantee equivalent provider realization. No endpoint digest, temperature/seed, prompt hashes, filesystem/network isolation, environment reset, cache policy, run order, or per-run resource ledger is reported. Skills and guide were authored with ArtifactCopilot's phases, so treatment fit may differ by harness. ArtifactCopilot itself is not shown under ACM-only, guide-only, or skills-without-packet-checking conditions; the effect of orchestration cannot be isolated.

## Evidence and results interpretation

### Agreement, not correctness

ArtifactCopilot's three-run mean exact four-level badge agreement is 70.56%; dimension accuracies range from 93.33% for documentation to 77.78% for reusability. Functional precision is 98.55% with 70.59% recall; Reusable precision is 87.44% with only 49.21% recall (Table III, p. 7). These figures support a conservative operating profile on this sample. They do not support autonomous acceptance: nearly three in ten badge labels differ from the authored reference, and half of reference Reusable positives are missed.

The degradation from observable documentation and availability toward claim support and reuse is constructively diagnostic. Reuse is not just more execution. It requires choosing an admissible transfer, judging whether the change is substantive, and deciding whether evidence transports. The system's best-supported use is to assemble review evidence and identify uncertain boundaries for humans, not issue badges.

### Guidance treatment

For OpenHands, Cline, and Codex, ArtifactGuide improves exact badge agreement over ACM policy by 7.22, 18.34, and 16.12 percentage points respectively; adding phase skills raises it further. The abstract's 10.55–28.34 point statement refers to Skills+Guide versus ACM for these three agents (Table IV, p. 8). ExecutionAgent does not follow this pattern and remains weak.

The direction is useful: executable criteria and staged guidance alter behavior materially. The causal interpretation remains limited because guidance conditions are not reported with randomized order, paired uncertainty, environment reset, or semantic-token budget control. More detailed guidance can improve conformance by teaching the scoring instrument, narrowing routes, or exposing evaluator cues—not only by transferring professional evaluation skill. Because references are defined under the same guide, criterion disclosure mechanically improves access to the target policy.

### Repeated runs and missingness

Table V reports each baseline's best RQ2 protocol, introducing outcome-conditioned configuration selection before stability comparison (p. 8). Codex has the strongest exact three-run badge consistency (37/60) and Functional agreement (49/60); ArtifactCopilot reaches 32/60 and 45/60, respectively, but is the only system with zero reported failure and has one three-way badge divergence. ArtifactCopilot's mean reported API cost is $0.125 per artifact run, versus $0.043–$0.093 for selected baselines.

This separates report availability from label recurrence, which is good. Yet the paper does not define every denominator and missing-run rule precisely, release run ledgers, provide confidence intervals, or account for artifacts clustered across systems/protocols/runs. Three attempts weakly estimate reliability. “Zero failure” means the pipeline emitted a report; it does not establish that cloning, services, evidence collection, or packet conclusions were valid. Conversely, baseline parse/context/workspace failures are system invalidity observations, not negative artifact labels. Cost excludes human adjudication, report consumption, infrastructure, environment runtime, and engineering, and wall-clock burden is absent.

### Mismatch analysis

The authors classify mismatches into claim mapping, reuse transfer, route/resource, run failure, and artifact content (Figure 4, p. 9). Claim mapping and reuse dominate, while baseline-specific infrastructure and context failures differ. This is valuable qualitative evidence that surface disagreement has heterogeneous roots.

But the coding method is not reported: no coder count, codebook, independent agreement, overlap policy, denominator construction, severity, evidence examples, or uncertainty appears. Counts therefore describe an author analysis, not a reproducible failure taxonomy. Categories also mix causes and surfaces: route choice can cause claim-mapping failure; resource failure can be environment invalidity; artifact content can trigger route recovery; context overflow is a harness–model interaction. `skill-bench` should retain raw mismatch, supported earliest cause, and unresolved rival cause separately.

### Reviewer study

Eight participants with at least three years of software-engineering research experience review eight paper–artifact pairs drawn from prior work in the authors' lab. A Latin-square assignment gives each participant four tasks—two with a generated report and two without—yielding 32 records. Different reviewers see each artifact under both conditions. Mean confidence is 4.06 with reports versus 3.63 without. Report perceptions are favorable: evidence location 4.44, boundary clarity 4.50, dimension clarity 4.62, uncertainty helpfulness 3.75, trust calibration 4.06, and overclaim risk 1.56. In 15/16 with-report reviews, reviewer decisions agree with the report (Section V-E and Figure 3, pp. 9–10).

This establishes that selected experienced researchers generally liked and followed these reports in a small controlled task. It does not show that reports improve decisions:

- the eight lab-associated artifacts are not sampled from the 60-artifact evaluation or a venue population;
- participants are experienced researchers, but AEC service, domain fit, and artifact-review expertise are not specified;
- no gold/adjudicated decision, error rate, evidence-location test, review time, workload, recall of caveats, or downstream committee outcome is measured;
- agreement with a visible recommendation can reflect correct assistance, shared rubric, or automation anchoring;
- confidence can increase when correctness does not;
- 32 records are crossed by only eight participants and eight artifacts, but no participant/artifact model or inferential uncertainty is reported; and
- report generation cost and review burden are absent.

The licensed result is perceived usefulness and recommendation uptake, not reviewer decision quality, efficiency, calibrated trust, or professional equivalence.

## Unique insight: evidence packets need route-completeness and adoption validity

ArtifactCopilot extends rubric work in a nontrivial way. ResearchRubrics makes criteria inspectable but mostly judges a final document. PaperBench inspects files and logs but collapses dependent evidence into compensatory local credit. ArtifactCopilot instead requires phase-bounded evidence packets, intervention provenance, and a decision derivation. That is closer to how consequential review should work.

Its failures reveal the missing layer: **a proof-carrying packet is only as valid as its route coverage, observer, and downstream use**. An internally consistent packet can be wrong because it followed a nonrepresentative route, failed to inspect an admissible alternative, accepted a misleading log, misclassified a repair, or inherited an incomplete criterion. A report can then raise reviewer confidence without improving the decision.

For `skill-bench`, represent evaluator assistance as three linked but separately validated objects:

1. **Review-route contract:** admissible paths, required and optional phases, prerequisites, backtracking policy, resource substitutes, stop reasons, and equivalence boundaries.
2. **Evidence packet:** actual path, environment/state identity, tool actions, raw and transformed observations, interventions, insufficiency/invalidity, packet-check results, contradictions, and criterion conclusion.
3. **Adoption event:** which reviewer saw which packet fields, inspected which locators, accepted/rejected/revised which conclusions, time/burden, confidence before/after, and decision correctness or consequence where independently available.

This adds the missing bridge between “the evaluator emitted a traceable report” and “the report improved professional evaluation.” Neither report production nor 15/16 recommendation agreement supplies that bridge.

## Comparison with adjacent reviewed work

- **ResearchRubrics:** both translate expert judgment into criteria. ArtifactCopilot adds phase-scoped evidence collection, interventions, and decision traces; ResearchRubrics has a more inspectable released criterion corpus. Both risk criterion-authority laundering, shared-rubric agreement, criterion dependence, and uncalibrated thresholds.
- **PaperBench:** both evaluate research artifacts with dense evidence. PaperBench observes generated repositories and partial reconstruction; ArtifactCopilot reviews supplied artifacts against badge gates. ArtifactCopilot's noncompensatory badge prerequisites are preferable to PaperBench's recursive compensatory root score, but route completeness and packet-check validity remain untested.
- **Auto Benchmark Audit:** both use agents to inspect complex packages and emit path-grounded findings. ABA correctly motivates candidate-finding adjudication; ArtifactCopilot should similarly treat phase conclusions and badges as review candidates, not authoritative truth. Both need clean sentinels, known-defect controls, independent adjudication, and repaired-form revalidation.
- **AgentRewardBench:** both demonstrate that evaluator identity and evidence view define the measurement. AgentRewardBench exposes unequal human/model observation; ArtifactCopilot adds richer execution packets but does not validate its packet observer. Both require plural immutable observations and explicit invalid/insufficient states.
- **Artifact-view and task-health contracts:** existing `skill-bench` machinery already represents authoritative views, transformations, evidence sufficiency, configured components, adjudication, revisions, and retirement. ArtifactCopilot adds no need for a new schema; it supplies test cases for route-set completeness, packet-checker calibration, intervention attribution, and reviewer adoption.

## Limitations and validity threats

### Content and criterion authority

1. Policy and venue sources are named, but criterion-level source/authority transformations are not released in the paper.
2. Twenty interviewees have heterogeneous overlapping artifact experience; qualifications and role counts are not linked to criteria.
3. Interview prompts, transcripts, coding, contradictions, recurrence threshold, and independent coding agreement are absent.
4. Final-five thematic saturation does not establish criterion completeness or boundary saturation.
5. The 24-artifact calibration set is conditioned on public accessibility and official badge strata, not a population sample.
6. Initial final-badge agreement is only 54.2%, demonstrating substantial judgment before same-case revision and adjudication.
7. Full agreement after revising rules and re-reviewing the same cases is not held-out reliability.
8. Member non-objection is not independent criterion validation or policy authority.
9. Weak-accept thresholds, intervention boundaries, representative workflow, valid output, main claim, and reuse remain judgment-laden.
10. Dimension dependence and cumulative badge gates can propagate one route error into several labels.
11. Legitimate alternative workflows and transfer cases are not systematically represented or tested.

### Reference and sample validity

12. Human references are authored under the same finalized guide given to evaluated systems.
13. Reference reviewers are paper authors; independent AEC or venue-level adjudication is absent.
14. Kappa is reported only for initial badge labels, without dimension/gate agreement or adjudication prevalence.
15. Broken-link artifacts are excluded, removing an important availability and operational-failure class.
16. The 30/20/10 pre-label strata deliberately distort prevalence; precision and recall do not transport to venue populations.
17. Source IDs, artifact snapshots, evidence packets, labels, and exact sample-selection records were not inspectable.
18. Historical official badges are neither the primary reference nor used as an independent validity criterion.

### System and configured-treatment validity

19. ArtifactCopilot's packet checker has no calibration, adversarial test, independent evidence, or false-accept/false-reject analysis.
20. Structural packet completeness does not establish evidence truth, causal execution, or claim entailment.
21. Confidence and cross-validation flags are uncalibrated.
22. Intervention classification rules and phase skills are unavailable for inspection here.
23. Persistent summaries may omit contradictory raw observations; no information-loss audit is reported.
24. Fixed phase order and limited recovery can convert one path failure into a badge error.
25. Environment, service, artifact, evaluator, and budget failures are not consistently separated.
26. The four baseline harnesses use different defaults, retries, stopping rules, interfaces, and model adapters.
27. A common backend label does not isolate the harness or guarantee equivalent provider realization.
28. ArtifactCopilot lacks component ablations for guide, skills, controller, memory, checker, and report derivation.
29. Guidance can expose the scoring instrument and improve evaluator-cue compliance without demonstrating transferred expertise.
30. Run order, reset, caches, network, seeds, model parameters, prompt hashes, and isolation evidence are not reported.

### Measurement and inference

31. Three-run means have no paired intervals, hierarchical uncertainty, hypothesis tests, or multiplicity control.
32. Artifact, system, protocol, and run dependence is ignored in headline metrics.
33. Best-protocol selection before stability comparison is outcome-conditioned.
34. Failure-rate and missing-output semantics are insufficiently specified for reconstruction.
35. Report production is counted as completion even though evidence validity is not independently established.
36. The mismatch taxonomy lacks a reproducible coding protocol, agreement, and root/surface distinction.
37. Costs are mean API estimates only; wall time, compute, environment work, human audit, and report consumption are absent.
38. The paper supports neither population frequency nor cost-effectiveness.

### Human-use and consequence validity

39. The user study has eight participants, eight lab-associated artifacts, and 32 dependent records.
40. It measures self-reported confidence/perception, not review correctness, time, workload, evidence-location performance, or downstream outcomes.
41. Fifteen-of-sixteen agreement with the supplied report may measure anchoring or shared-rubric uptake rather than decision quality.
42. Participant AEC experience, task-domain fit, assignment details, and prior artifact familiarity are under-specified.
43. No inferential model accounts for participant/artifact clustering.
44. No report-defect or misleading-confidence controls test calibrated distrust.
45. Increased confidence without an external correctness criterion cannot support trust-calibration claims.

### Reproducibility and lifecycle

46. V1 and v3 are materially different instruments under the same title and system name.
47. V3 omits the v1 AE Graph/environment-normalization method; old and new results are not longitudinally comparable.
48. The v3-cited Figshare package could not be inspected because the endpoint returned a WAF challenge in this environment.
49. The restricted Zenodo record exposes neither files nor checksums and is not the release cited by v3.
50. Paper-version correspondence, paper-time code, task identities, run ledgers, reports, prompts, and raw labels are unavailable.
51. DeepSeek-V4 Flash realization, CC-Switch behavior, package versions, and execution environments are not frozen sufficiently for exact replay.
52. The paper's “open-source artifact” and full-guide-example claims remain operationally unverified here.

## Reproducibility and operational realism

Paper inspectability is strong: immutable v3 fully specifies the high-level gate, dimensions, intervention/evidence levels, phase order, headline metrics, and study design. Version inspection is also unusually informative because v1 remains immutable and proves that the named system changed constructs, components, sample, and claims.

Experiment reproducibility is weak. Neither candidate release exposed inspectable files in this run. The paper does not provide task IDs, artifact snapshots, reference packets, raw predictions, trial traces, failure ledgers, prompts, seeds, analysis code, participant forms, or per-record study outcomes. Exact table reconstruction and checker validation are impossible from the available evidence. The v3 Figshare link may become accessible through an interactive WAF-cleared client, but unavailable inspection remains missing evidence, not proof that files do not exist.

Operational realism is mixed. Real public research artifacts, dependency setup, execution, claim mapping, interventions, failures, and bounded reuse are substantially more realistic than final-answer grading. Repeated runs and reviewer-facing reports add useful operational dimensions. Yet excluding broken links, using one GPU/software environment, allowing framework-specific defaults, omitting service/network/reset identity, and measuring no committee process or downstream reproduction constrains the claim. This is evidence about **agent-assisted rubric-guided review of selected accessible software artifacts**, not general professional artifact evaluation.

## Transfer to skill-bench

### Retain

1. Policy/source grounding before criterion construction.
2. Analytic dimensions with noncompensatory minimum gates for named decisions.
3. Separate execution, claim support, documentation, and reuse observations.
4. Explicit representative-workflow, intervention, and evidence levels.
5. Phase skills with objective, tool scope, evidence contract, and completion conditions.
6. Transient planning separated from committed auditable evidence.
7. Criterion-linked reports with raw evidence locators and deterministic decision derivation.
8. Repeated trials that report recurrence, divergence, invalidity, and cost separately.
9. Reviewer-facing uncertainty and override rather than opaque autonomous decisions.

### Repair

10. Bind every criterion and boundary to policy, venue, expert, and artifact evidence with transformation/authority lineage.
11. Validate revised criteria on untouched artifacts with independent reviewers and alternative legitimate paths.
12. Represent route sets, backtracking, substitutes, stop reasons, and equivalence—not only one committed phase path.
13. Separate task/artifact defect, environment invalidity, service failure, evaluator failure, budget censoring, and substantive rejection.
14. Preserve raw observations alongside summaries and test packet checkers against fabricated, incomplete, contradictory, and irrelevant evidence.
15. Treat confidence as a calibrated prediction with a named target and decision loss, not an evidence-completeness heuristic.
16. Factor guide, phase skills, orchestration, checker, memory, and report treatments when causal attribution matters.
17. Use paired clustered uncertainty at the artifact level; never treat repeated runs or dimensions as independent rows.
18. Validate report assistance with correctness, evidence-location accuracy, time, burden, override quality, automation-bias controls, and downstream use.
19. Version system identity at every material redesign; old and new ArtifactCopilot results must not share an implicit scale.
20. Publish immutable source/task/run/report/adjudication manifests and exact release correspondence.

### Test before adopting

- Route-completeness contrast set: one failed documented path plus one legitimate alternative, one prohibited semantic repair, one bounded substitute, and one true environment invalidity.
- Packet-checker calibration: supported, contradicted, insufficient, irrelevant-log, fabricated-log, wrong-artifact, and stale-service packets with independent labels.
- Intervention attribution: matched original versus repaired artifacts where path/configuration/I3/I4 boundaries have independently adjudicated consequences.
- Decision-level validation: compare packet-assisted and unassisted reviewers on correctness, time, severe errors, evidence inspection, override, confidence calibration, and audit burden.
- Version bridge: run common immutable artifacts through v1 and v3 only if both implementations become available, reporting construct/component changes rather than a false longitudinal trend.
- Cross-domain transport: apply the packet pattern to a non-software artifact with different authority, representations, and legitimate workflows before claiming general evaluator machinery.

## Concrete repository actions

- Added this full-text deep review and preserved the materially different immutable v1 for version comparison.
- Updated the release provenance to separate the v3-cited Figshare record from the restricted Zenodo candidate and to record failed access without claiming file absence.
- Updated the paper index and topic navigation from acquisition-pending to deep-review complete with release unavailable/unverified.
- **No new queue task added.** Existing artifact-admissibility, task-health, execution-validity, validity-argument, metric, grader-observation, reliability, and expert-participation machinery already provides the canonical homes. The evidence supplies validation cases—route completeness, packet-checker calibration, version discontinuity, and report-adoption validity—not a nonduplicate subsystem.
- The grouped synthesis and state-of-the-art map were not changed. The source reinforces existing separation among criterion authority, evidence views, task health, metric estimands, and claim validity; it does not overturn a grouped conclusion or justify narrowing the benchmark to software artifacts.

## Assessment

- **Evidence tier:** B — full immutable v3 read; immutable v1 compared; release metadata and access failures preserved; implementation, datasets, raw runs, and user-study records unavailable.
- **Most reusable contribution:** phase-bounded, intervention-aware evidence packets with criterion-linked deterministic decision traces.
- **Most serious validity flaw:** candidates and human references are aligned to the same author-built rubric, so badge agreement is not independent evaluator correctness.
- **Most serious operational flaw:** fixed route commitment can turn a recoverable alternative workflow into a negative decision while packet consistency makes the route look auditable.
- **Most serious lifecycle flaw:** v1 and v3 are different systems and evaluation programs under one name, while release correspondence is not inspectable.
- **Safe claim:** explicit operational criteria and phased evidence organization improve agreement and report production for selected configured agents on one author-adjudicated 60-artifact sample. They do not establish autonomous artifact evaluation, expert substitution, general evaluator reliability, reproducibility, professional readiness, or production fitness.
