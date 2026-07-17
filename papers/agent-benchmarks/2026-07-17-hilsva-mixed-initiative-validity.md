# HiLSVA: mixed-initiative controls are inspectable mechanisms, not demonstrated effective oversight

## Bottom line

HiLSVA combines editable plan-first execution, action approval, direct ParaView manipulation, stepwise state history, selectable autonomy, and retrieval-based test-time adaptation in one substantial scientific-visualization prototype. The paper's 12-person study is useful evidence that participants across three coarse expertise strata could operate this configured system on four prescribed cases, answered 11.75/12 mostly scaffolded interpretation questions on average, and rated its control and provenance affordances highly.

The study does **not** show that mixed initiative improves completion, visualization quality, verification, or scientific reasoning. For the first three tasks, autonomy mode changes together with task within each participant; the balanced assignment controls mode frequency but does not turn different task realizations into a clean paired mode treatment. Mixed initiative additionally bundles human involvement with retrieval-based learning. The reported time contrast is nonsignificant, all modes apparently reached completion, no independent artifact-quality scores are reported, the questionnaire is post-study rather than condition-specific, and no intervention-level analysis connects control availability to use or consequence. The final mode choice is observational: seven of 12 participants chose full autonomy.

The strongest transferable contribution is therefore an **intervention-accounting boundary**:

```text
control available
→ user exposed to a decision opportunity
→ control exercised with typed intent and authority
→ agent receives and semantically adopts/rejects it
→ authoritative artifact/state changes at the intended locus
→ independent quality/preservation check
→ task or decision consequence
→ burden, reliance, and bounded collaboration claim
```

HiLSVA establishes mechanism availability and positive perceived control. It does not preserve enough study evidence to validate most later links.

## Why this matters to the charter

This review advances charter objectives A, B, and C through a bounded scientific-visualization stress test of a general knowledge-work question: when an agent exposes plans, approvals, state history, direct manipulation, and uncertainty prompts, what evidence shows that a human intervention actually improves consequential work?

- **Concrete evidence:** immutable paper, full paper-linked study instrument, and complete official post-v1 code archive at an exact commit.
- **Uncertainty clarified:** the distinction among interaction availability, exercise, uptake, state effect, artifact quality, task outcome, burden, and professional utility.
- **Mode:** validation-oriented expansion with consolidation implications.
- **Useful completion:** retain the intervention and provenance primitives while refusing to infer effective oversight, expert validity, safe execution, or professional utility from completion and global self-report.

Scientific visualization is the study substrate, not a scope commitment.

## Sources and reading record

### Primary paper read in full

- Kuangshi Ai, Patrick Phuoc Do, and Chaoli Wang, *HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization*.
- Immutable arXiv v1: <https://arxiv.org/abs/2606.26614v1>, submitted 25 June 2026.
- Local PDF: `data/papers/pdfs/2606.26614v1-hilsva-mixed-initiative-scientific-visualization.pdf` (12 pages; SHA-256 `d654d2d27be8a429e89b21cc3fda61e4d24012d76d628624e8d099644f1b8bb3`).
- Full layout extraction: `data/papers/text/2606.26614v1-hilsva-mixed-initiative-scientific-visualization.txt` (SHA-256 `e6494b6150c56ddd33a9e74f3f9cf9b4424990237016b54faf64669d79547a71`).
- Metadata: `data/papers/source/2606.26614v1-metadata.xml`.

The complete extraction was read through architecture, five case studies, participant table, statistical tests, limitations, conclusion, appendix, and references. Page references below use PDF pages.

### Paper-linked user-study document read in full

- Canonical document: <https://hilsva.github.io/static/pdfs/user_study_doc.pdf>.
- Local PDF: `data/sources/pdfs/2606.26614v1-hilsva-user-study-document.pdf` (15 pages; SHA-256 `31b1ef6179e3ad6291bb8247d78116a38d1f95d62987085f5c1bcf272770a2c1`).
- Full text: `data/sources/2606.26614v1-hilsva-user-study-document.txt` (SHA-256 `91af1850823cea93de50c0819601958ddc2330af79466f339f6d32879a136e0a`).

The instrument supplies the interface instructions, exact autonomy settings, four task cases, 12 interpretation questions, and 14 post-study items. It contains an unresolved instruction—participants may “pause, ask questions [and resume?]”—which is small but illustrates that the administered protocol is not a finalized preregistration.

### Official release audit

- Repository: <https://github.com/KuangshiAi/HiLSVA>.
- Exact commit inspected: `63b99042b3f190e79ea4ded41fb8daa52e5cb4cc` (251 tracked files).
- Local archive: `data/sources/releases/2606.26614v1-hilsva/KuangshiAi-HiLSVA-63b9904.zip` (SHA-256 `3fd6d05e31c1b3db87405009d502f7e991880e49d855c9c1adec5d6890c06325`).
- Provenance: `data/sources/releases/2606.26614v1-hilsva/provenance.json`.

The commit is dated 26 June 2026, one day after immutable v1. It is post-v1 release evidence, not the exact paper-time or study implementation. The full archive was extracted and statically inspected, including approval guards, autonomy settings, learning repository, run/state records, Docker configuration, ParaView integration, and test configuration. The archive includes no study logs, participant allocations, screenshots, videos, ratings, task graders, analysis script, or `tests/` directory despite pytest configuration.

## One-sentence contribution

HiLSVA makes plan, approval, execution, direct manipulation, rollback, provenance, autonomy, and feedback-based retrieval jointly available in one native scientific-visualization workflow, but evaluates that bundle primarily through completion, easy interpretation questions, timing, and global perception rather than intervention consequences.

## Research questions and claim boundary

The paper asks how a mixed-initiative SciVis system can:

1. preserve human control while coordinating specialized tool agents;
2. support plan editing, guarded execution, direct manipulation, rollback, and workflow reuse;
3. adapt during use through self-reflection and human feedback;
4. support novice, domain-scientist, and SciVis-expert participants across autonomy settings; and
5. balance automation time against perceived control and transparency.

The evidence supports narrower claims:

- a substantial implementation exposes the named interaction affordances;
- 12 participants completed an administered four-case study with this configured prototype;
- interpretation-question accuracy was near ceiling;
- mean execution time increased monotonically from full autonomy to mixed initiative, but the omnibus and corrected pairwise tests were nonsignificant;
- participants rated the overall system highly, especially revisitability, feedback clarity, and perceived control;
- seven participants chose full autonomy, two half autonomy, and three mixed initiative for the final task.

It does **not** establish that mixed initiative improves task completion, visualization correctness or quality, error detection, realized repair, scientific insight, trust calibration, expert-level performance, safe execution, LTT efficacy, cross-tool generality, professional usefulness, or readiness. The abstract's statement that mixed initiative “improves task completion” is not supported by a reported completion comparison; all participants completed the study, and no mode-level failure inventory is shown.

## Methodology and system

### Mixed-initiative architecture

HiLSVA extends Magentic-UI with an orchestrator, ParaView MCP agent, code agent, file surfer, web surfer, and self-improving agent. The orchestrator creates an editable plan, delegates steps, monitors progress, and may replan. Users can edit and approve plans, approve actions, intervene through chat or the ParaView GUI, return control, revisit prior steps, and save workflows (Sections 3.1–3.4, pp. 3–5).

The release confirms mechanism-level availability:

- `AutonomySettings.tsx` defines full autonomy as no cooperative plan approval, autonomous execution, approval policy `never`, and disabled self-improving hooks. Disabling it restores an `auto-conservative` approval policy, not one fixed experimental mode.
- `approval_guard.py` supports `always`, `never`, `auto-conservative`, and `auto-permissive` decisions. Conservative classification uses another model over a short action view; malformed classifier output defaults to approval **being required**, while absent/unrecognized human input can fall back to configurable default approval.
- `guarded_action.py` gates an action only when the tool metadata and active policy route it through the guard. This is a real enforcement point, but the release contains no coverage audit proving every consequential ParaView, filesystem, code, browser, or external action is correctly typed.
- the database stores messages, run state, plans, plan metadata, and team results; agents expose `save_state`/`load_state` paths.

Availability is not exercise. The paper does not report plan edits, approval requests, denials, interruptions, GUI interventions, rollbacks, branches, clarifications, or saved/reused workflows by participant, task, mode, correctness, or consequence.

### Provenance and rollback claim

The paper says each step records planned and executed actions, software states, and visualization outputs and that arbitrary prior ParaView states are “faithfully recovered” (Section 3.2 and tornado case, pp. 4 and 6). This is a useful design target, but the release does not provide an end-to-end state-equivalence test or retained replay ledger. Some state paths are visibly partial: the aggregate MCP workbench's `save_state` returns a dummy state with a TODO; browser restoration revisits live URLs; run and plan schemas accept broad JSON/string state without a typed completeness contract.

That does not prove ParaView rollback fails—the system may preserve it through separate application-specific paths—but it prevents the repository from licensing “faithful” whole-workflow restoration. A valid rollback claim needs pre/post native-state hashes, renderer/environment identity, replay result, allowed invariances, and collateral-state checks.

### Retrieval-based test-time adaptation

The self-improving agent retrieves knowledge before a step, reflects afterward, and requests feedback below a confidence threshold subject to an intervention budget. The paper describes semantic similarity × confidence × recency × validity weighting and explicitly calls the mechanism retrieval-based rather than weight adaptation (Section 3.3, pp. 4–5).

The release exposes a serious authority boundary:

- `aria_knowledge_repository.py` persists one `knowledge_repo_shared.json` across sessions rather than a session-local repository;
- human feedback defaults to confidence 1.0 in the paper's formulation, while agent learning may also enter as “valid” knowledge;
- items have source, confidence, status, recency, and optional metadata, but no evidence locator, contributor authority scope, contradiction relation, held-out validation gate, downstream-use boundary, or split firewall;
- updates overwrite the shared JSON file without an evident append-only event log or lock in the inspected class.

The study does not state whether the repository was reset between participants, tasks, or modes. If it was shared, participant order and prior feedback could change later treatments; if reset, the cross-task LTT story differs. Either way, the missing reset/persistence ledger blocks attribution. Q13's 4.50/5 perceived benefit from accumulated knowledge shows that participants noticed or endorsed the feature, not that retrieved items were correct or improved outcomes.

### Execution containment

The paper calls execution sandboxed, safe, isolated, and reproducible (Sections 3.1–3.2, pp. 3–4). The release shows Docker-based process separation, but not a security or reproducibility proof:

- agents share a host-mounted workspace;
- containers join a Docker bridge network and browser/web retrieval is a core feature;
- the ParaView launcher publishes ports and uses a mutable `latest` image;
- the README likewise names mutable image defaults;
- no network-denial policy, host-filesystem canary, cross-session interference test, secret-access test, image digest, or threat model is released;
- full-autonomous mode intentionally disables action approval.

Docker isolation is useful containment. It is not evidence of “safe execution,” and a writable shared host mount is simultaneously a collaboration mechanism and a cross-agent/cross-session risk surface.

## User-study design

### Participants and procedure

The study recruits three SciVis experts, four domain scientists familiar with scientific data but limited in visualization tools, and five novices with neither domain nor visualization expertise. Recruitment source, inclusion rules, demographics, exact disciplines, prior ParaView/VTK experience, and how labels were assigned are not reported. Participants use one RTX 5090 workstation with two 32-inch 4K displays, receive $30, and complete the study independently while two authors administer sessions. IRB approval and hard-copy consent are reported (Section 4.3, pp. 8–9).

The paper says all 12 completed the full study. The study document specifies a five-minute introduction, ten-minute exploration, 35-minute four-case stage, and ten-minute questionnaire. Yet Table 2 reports mean completion time 45.08 minutes, ranging from 27 to 67, without defining timeout, pause, retry, crash, assistance, or excluded-time policy. The authors report occasional crashes and GUI inconsistencies in qualitative feedback, but no participant/task failure ledger.

### Conditions and assignment

For hurricane, foot, and tornado, each participant uses each of three modes exactly once:

1. **full autonomous:** no plan/user/action approvals and no self-improving agent;
2. **half autonomous without LTT:** user guidance available, LTT disabled;
3. **mixed initiative with LTT:** user guidance plus retrieval/reflection/intervention settings (`max interventions=5`, `top-k=3`, score threshold `.55`, confidence threshold `.65`).

Assignments are balanced so every mode appears equally often across participants. The allocation matrix is not released. This is a balanced incomplete task × mode arrangement, not a clean repeated-measures trial of the same task or defect under every mode. Within a participant, each mode's time comes from a different case. Across participants, balancing can reduce average task confounding, but the analysis should model participant and task jointly and preserve the allocation. A Friedman test over each participant's three mode times treats them as comparable blocks while leaving task, order, carryover, and task-by-mode effects unmodeled.

The study also cannot isolate “mixed initiative” from LTT: the authors state this explicitly (p. 8). Nor does it isolate plan review, action guards, GUI control, rollback, uncertainty prompts, or retrieval. The fourth combustion task is post-treatment preference observation: participants choose a mode after exposure to all three, so its time cannot estimate a mode effect.

### Tasks and outcomes

The four administered cases are detailed and native-tool-grounded, but strongly prescribed:

- hurricane specifies slice location, colormap, histogram, ten contour lines, and output paths;
- foot specifies tissue colors, anatomy-reference retrieval, isosurface adjustment, and screenshots;
- tornado specifies three parameter trials, rollback to a preferred trial, glyph settings, and output;
- combustion specifies paths, variables, colormap, isovalue, and animation exports.

The 12 questions are mostly direct recall or multiple choice. Several answers are given by task wording or elementary definitions—for example, contours highlight equal-value structures; isovalue controls shown density; arrow orientation represents velocity direction; an isosurface equals the selected value. Near-ceiling Q&A therefore supports instruction comprehension and basic visualization literacy under scaffolding, not expert-comparable artifact quality or scientific reasoning.

Crucially, the paper does not report independent grading of saved screenshots, ParaView state, generated animations, histogram values, anatomy interpretation, parameter compliance, replay integrity, or collateral damage. “Completion” is undefined beyond finishing the administered session. Logged visualizations are said to support analysis, but no artifact rubric, rater authority, blinding, agreement, criterion table, or retained outputs are reported.

## Evidence and results interpretation

### Timing

For the first three tasks, mean mode times are:

- full autonomy: `9.83 ± 3.27` minutes;
- half autonomy: `11.67 ± 4.44`;
- mixed initiative: `13.50 ± 4.46`.

The Friedman test is nonsignificant (`χ²(2)=5.09`, `p=.078`, Kendall's `W=.19`), and Holm-corrected pairwise Wilcoxon tests find no significant pair. Full autonomy versus mixed initiative is assigned Cliff's `δ=-.51`, but this independent-sample dominance statistic is not the natural paired effect for a within-participant design, and the paired observations are different tasks. The paper appropriately declines to call the speed contrast reliable, then interprets it as an oversight–efficiency tradeoff. The time ordering is descriptive; the “oversight” benefit was not behaviorally measured, so only added interaction time is observed.

### Accuracy and expertise

Average Q&A is `11.75/12`; nine participants score 12, and three score 11. Kruskal–Wallis tests find no expertise differences in completion time (`H=.92`, `p=.63`) or exploration time (`H=.28`, `p=.87`). Group Q&A rates are reported as 100%, 100%, and 95%.

With groups of 3, 4, and 5, ceiling questions, no artifact-quality endpoint, and no no-agent expert baseline, failure to reject group differences cannot support the conclusion that HiLSVA enables novices to achieve “expert-comparable performance.” The study is explicitly underpowered for fine-grained group effects. It shows that all three labeled groups answered this instrument similarly, not equivalence and not expertise transfer.

The claim that no data hallucinations occurred also lacks a defined opportunity set, observer, evidence view, adjudication protocol, or denominator. It should be treated as an informal observation, not an estimated failure rate.

### Final autonomy choice

Seven participants choose full autonomy for combustion, two half autonomy, and three mixed initiative. This is valuable negative evidence against a universal “more involvement is better” thesis. It may reflect perceived agent reliability, task familiarity, fatigue, latency, low intervention value, limited expertise to guide, or a preference for speed. Because combustion is one fixed final task and choice follows three prior exposures, it does not establish stable user preference or optimal allocation.

A benchmark should treat mode choice as a decision requiring opportunity, expected loss, competence, confidence, and consequence—not as proof that autonomy is beneficial.

### Questionnaire and qualitative evidence

All participants answer 14 post-study five-point items; the overall mean is 4.66. Highest means include revisitability (`5.00`), feedback clarity and provenance usefulness (`4.92` each), autonomy adjustment (`4.83`), and action review/control (`4.75`). These are strong perception results for the overall bundle.

They are not condition comparisons: participants do not rate each autonomy mode separately, and there is no baseline interface. Several items restate advertised features after demonstration and repeated use. Q10 has zero variance, which may indicate a genuinely salient affordance, demand/ceiling effects, or both. Q13 cannot validate LTT because participants cannot independently observe whether retrieved knowledge caused correct behavior.

The appendix collapses SciVis experts and domain scientists into one “expert” group (`n=7`) and compares it with novices (`n=5`), despite those being substantively different authority classes. The reported Mann–Whitney `p=.080`, Cliff's `δ=-.63` is exploratory and uncorrected among many possible questionnaire/group contrasts.

Selected quotations identify useful hypotheses—iterative refinement, text controllability, uncertainty prompts—and negative cases—latency, crashes, GUI inconsistency, verbosity, and novices wanting more guidance. No transcript corpus, codebook, coding method, rater reliability, participant-by-theme matrix, or negative-case counts are released. Quotes establish existence, not prevalence.

## Unique insight: mixed initiative must be measured as realized state transition, not interface inventory

HiLSVA's interface inventory is unusually rich, but that richness creates the central evaluation problem. A plan editor, action guard, rollback button, direct GUI, uncertainty prompt, and knowledge retrieval may all be present while contributing nothing—or causing harm—on a particular task.

The evaluable unit is an **intervention episode**, not a feature checkbox:

1. **Opportunity:** what decision, uncertainty, defect, or irreversible consequence was present?
2. **Availability and exposure:** which control was shown, when, and with what information?
3. **Exercise:** did the user inspect, approve, reject, edit, intervene, rollback, branch, or abstain?
4. **Authority and basis:** was the input factual correction, scoped preference, domain judgment, safety veto, or unsupported guess?
5. **Receipt and uptake:** did the agent parse the intended proposition and adopt, reject, or distort it?
6. **State effect:** which native artifact/state loci changed, under which environment and transformation identity?
7. **Verification:** did an independent admissible observer confirm intended repair and collateral preservation?
8. **Consequence:** did task quality, decision loss, safety, handoff, or recipient outcome improve?
9. **Burden and reliance:** what time, attention, latency, rework, confidence, and future verification behavior resulted?

Availability supports an interface claim. Exercise supports an interaction claim. Verified state improvement supports an oversight claim. Downstream outcomes support bounded utility. These claims must not inherit one another.

## Comparison with adjacent reviewed evidence

- **SciVisAgentBench:** it provides heterogeneous artifact graders and an evaluator-admissibility lesson, but narrows cases to one reference and does not test human steering. HiLSVA restores interaction and direct manipulation but omits independent artifact grading. Together they motivate crossing a frozen agent state/intervention opportunity with native-state, rendered-view, code, and expert-admissible checks rather than substituting usability for quality.
- **Pista:** both expose semantic operations, editable plans, and branchable state. Pista's 16-person within-subject study better measures inspectability and prompt burden, yet still lacks shared defect opportunities and proposition-level repair. HiLSVA has broader native-tool mechanisms but even less intervention-consequence accounting.
- **HANSEL:** HANSEL preserves shared wrong-agent opportunities and released human outcome rows, showing that lower review burden can coexist with confident errors. HiLSVA has no wrong-state strata, confidence calibration, or released participant rows. Its high perceived control cannot establish calibrated oversight.
- **Shared lesson:** human-facing evidence, controls, and provenance are candidate instruments. They require fidelity, exposure, adoption, state-effect, quality, and burden validation before they can license collaboration or safety claims.

## Limitations and validity threats

1. Twelve participants provide limited precision and no task-population generalization.
2. Recruitment source, demographics, disciplines, inclusion rules, and expertise-label criteria are absent.
3. The “domain scientist” category does not establish authority for each dataset or interpretation criterion.
4. Participants and administrators are unblinded to modes and system goals.
5. Two authors administer sessions; assistance and intervention rules are not reported.
6. The exact participant × task × mode allocation is unreleased.
7. Each participant uses each mode on a different task; mode and task vary together within person.
8. Task order appears fixed (hurricane, foot, tornado, combustion), and no period/carryover analysis is reported.
9. LTT persistence/reset across tasks and participants is unspecified.
10. The released implementation uses one shared cross-session knowledge file, creating a plausible contamination/order boundary.
11. Mixed initiative bundles human guidance with LTT; the paper acknowledges no isolated LTT effect.
12. Plan editing, approval, rollback, direct manipulation, uncertainty prompting, and retrieval are not factorially separated.
13. Mode-level feature exposure and exercise counts are absent.
14. No intervention is linked proposition-by-proposition to agent receipt, state change, or re-verification.
15. Completion is not operationally defined by artifact criteria.
16. No independent artifact grading, blinded review, rater agreement, or criterion outcomes are reported.
17. Saved screenshots, state, animations, logs, and videos are not released.
18. The 12 interpretation questions are near-ceiling and mostly scaffolded recall/multiple choice.
19. No unassisted expert or novice baseline exists.
20. Nonsignificant group tests do not demonstrate expert equivalence.
21. Timing analysis does not jointly model participant, task, mode, order, or task-by-mode heterogeneity.
22. Cliff's delta is not a natural paired effect measure for the stated within-participant comparison.
23. Corrected pairwise p-values, allocation rows, and raw timing observations beyond Table 2 are absent.
24. Completion time exceeds the nominal 35-minute task stage for many participants without a timeout/pause/failure policy.
25. Final mode selection is confounded by one fixed task, fatigue, prior exposure, perceived reliability, and latency.
26. The questionnaire is global rather than per-mode or baseline-comparative.
27. Fourteen related items lack a stated scale model, reliability analysis, preregistration, or multiplicity plan.
28. Q13 perceived learning does not validate knowledge correctness, retrieval relevance, or causal benefit.
29. Qualitative quotes lack released transcripts, codebook, independent coding, prevalence, and negative-case accounting.
30. “No hallucinations” has no defined detector, denominator, observer, or uncertainty.
31. Case studies are authored demonstrations, not independent trials.
32. The half-cylinder scientific-analysis case is excluded from the user study, so scientific-insight claims rest on demonstration.
33. Direct GUI manipulation may create state changes that textual agent traces do not semantically explain; capture completeness is untested.
34. Whole-workflow rollback/state equivalence is asserted without released replay tests or hashes.
35. The aggregate MCP workbench release has dummy state serialization, exposing an incomplete state-contract boundary.
36. Action-guard coverage and classifier accuracy are untested; controls can be disabled.
37. Docker containers share a writable host mount and network; no security canaries or threat model support “safe execution.”
38. Mutable `latest` images and commercial model endpoints prevent exact environment replay.
39. The exact study code, model endpoint dates, prompts, seeds, retries, failures, tokens, and API costs are absent.
40. Latency, crashes, and GUI inconsistencies are reported qualitatively but not quantified by mode or outcome.
41. The post-v1 release has no retained study data, graders, analysis, or tests.
42. No recipient, scientific decision, delayed audit, reuse episode, team handoff, or professional consequence is observed.

## Reproducibility and operational realism

**Mechanism inspectability is moderate to good.** The immutable paper, exact study instrument, complete 251-file post-v1 archive, autonomy configuration, approval logic, state records, learning repository, Docker recipes, and ParaView interfaces make the system substantially more inspectable than a conceptual mockup.

**Empirical reproducibility is poor.** The release omits participant allocation, raw logs, approvals, edits, interventions, screenshots, ParaView states, videos, questionnaire rows, qualitative corpus, artifact graders, statistical script, endpoint snapshots, and exact study build. The three large scientific environments, commercial model calls, mutable images, browser state, and GPU/GUI behavior further complicate replay. A fresh run would evaluate the archived configured prototype, not reproduce the reported study without correspondence evidence.

**Operational realism is mixed.** Native ParaView, raw scientific data, code generation, GUI manipulation, web references, iterative parameters, animation, state history, latency, and occasional crashes are meaningful workflow features. Conversely, prescribed short cases, administrator presence, easy interpretation questions, no real research objective, no independent quality review, and no downstream scientific decision make this a laboratory prototype study rather than evidence of professional scientific collaboration.

## Transfer to skill-bench

### Retain

1. Expose plans as editable, versioned artifacts rather than hidden reasoning.
2. Pause at consequence-bearing actions with explicit approval scope and evidence.
3. Preserve native pre-intervention state, branch lineage, and direct artifact manipulation.
4. Let human and agent exchange initiative rather than fixing one autonomy level globally.
5. Keep retrieval/reflection state independent from model identity and version it explicitly.
6. Measure autonomy choice as an outcome rather than assuming maximal human involvement is optimal.
7. Keep time, artifact quality, intervention efficacy, control, trust, and professional consequence separate.

### Repair

8. Add a typed intervention episode linking opportunity, exposure, exercise, authority, content, receipt, adoption/rejection, changed loci, verification, collateral effects, burden, and consequence.
9. Cross conditions on identical frozen pre-intervention states or matched defect opportunities; do not compare different tasks as though mode were the only change.
10. Factor plan visibility, approval, local edit, direct manipulation, rollback, uncertainty query, and learned guidance where causal attribution matters.
11. Grade native application state, rendered views, exported artifacts, task requirements, and scientific interpretation through separate admissible observers.
12. Record task/order/mode allocation, reset/persistence policy, participant/task clustering, missingness, crashes, retries, and service drift.
13. Treat human feedback as scoped evidence, not confidence-1 truth; preserve contributor authority, locators, contradictions, validation, and rollback.
14. Validate rollback with exact state identity, renderer/environment pins, allowed invariances, and collateral-state checks.
15. Validate guards with a complete action inventory and planted harmful/benign cases; distinguish control disabled, classifier missed, user approved, and action blocked.
16. Replace “sandboxed therefore safe” with an outer-envelope record: image digest, mounts, network, credentials, host access, cross-session canaries, and residual threat model.
17. Use condition-specific perception items plus behavioral calibration: correct approve/reject/edit/escalate decisions under reliable, uncertain, misleading, and harmful agent states.
18. Preserve participant-level records and report joint quality–time–burden estimands rather than completion and timing alone.

### Test before adopting

- **Frozen-state oversight factorial:** one valid state, one visible defect, one hidden structural defect, one uncertain preference, and one consequential action; cross no control, plan-only, approval, local edit, rollback, and uncertainty prompt.
- **Adoption audit:** plant human feedback that is correct, context-limited, contradictory, and wrong; verify agent interpretation, scope, state effect, and held-out behavior.
- **Rollback conformance:** mutate native state across chat, code, direct GUI, web, and files; roll back and test exact/allowed-equivalent restoration plus branch isolation.
- **Autonomy allocation study:** let participants choose or delegate per decision under known reliability/cost strata; score decision loss, appropriate escalation, time, and confidence calibration.
- **Cross-domain transport:** apply the same intervention ledger to a spreadsheet semantic diff and a document/source-provenance correction before claiming general mixed-initiative validity.

## Concrete repository actions

- Added this full-paper, full-study-document, exact-commit deep review.
- Updated the paper index from acquisition-pending to deep-review complete with the exact artifact path and release timing boundary.
- Added HiLSVA to topic navigation as a mixed-initiative, intervention-accounting, state-provenance, and human-study validity case.
- **No new queue task added.** Existing interaction evidence, feedback/recovery, artifact-view admissibility, configured-system identity, compounding-lesson, longitudinal, task-health, metric, validity, and execution-isolation machinery already has homes for the requirements. HiLSVA contributes high-value planted contrast cases rather than a nonduplicate subsystem.

## Assessment

- **Evidence tier:** B — complete immutable paper and study instrument read; full exact-commit post-v1 release inspected; empirical records absent.
- **Most reusable contribution:** a rich set of decision-time controls around native artifact execution.
- **Strongest evidence:** all 12 participants operated the prototype, near-ceiling scaffolded Q&A, high perceived control/provenance, and an explicit nonsignificant time ordering across balanced mode exposure.
- **Most serious identification flaw:** mode is observed on different tasks within each participant, while mixed initiative also bundles LTT and no intervention-to-consequence records are reported.
- **Most serious operational warning:** the release's shared cross-session knowledge file and broad host-mounted/networked Docker envelope undermine unqualified adaptation-isolation and safe-execution claims.
- **Safe claim:** in one administered four-case ParaView study, 12 participants across three author-defined expertise strata completed the session, answered mostly scaffolded interpretation questions accurately, and rated HiLSVA's overall controls and provenance highly; mean execution time was descriptively lowest under full autonomy, but mode differences were not significant, and most participants chose full autonomy for the final task. The evidence does not establish that mixed initiative or LTT improves artifact quality, verification, scientific reasoning, calibrated oversight, safety, professional utility, general transfer, or readiness.
