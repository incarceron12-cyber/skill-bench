# HANSEL: evidence breadcrumbs reduce review burden, but support-path compression is not verification completeness

## Bottom line

HANSEL makes a valuable interface move: project a long web-agent trajectory into a small set of live, replayed pages with highlighted snippets, while retaining the full trajectory and letting a reviewer interact with the pages. Its 45-trajectory technical study supports a narrow extraction result: against two authors' adjudicated **support-path** page labels, one GPT-5.4 configuration recovered 87 of 98 labeled pages while selecting 104 of 271 visited pages. Its released 14-participant study supports a narrow human-use result: under eight fixed tasks and one bundled interface treatment, participants submitted answers faster, reported less effort, and strongly preferred HANSEL.

Neither result establishes verification completeness or effective oversight. The annotation rule deliberately excludes abandoned, failed, blocked, and navigation paths, even though these may contain the negative or contradictory evidence needed to test “cheapest,” “latest,” coverage, and failed-constraint claims. Snippet evaluation reports precision only on predicted snippets; there is no snippet-recall denominator. Page-state replay, highlight fidelity, temporal/source identity, unsupported-answer flags, contradiction coverage, and reviewer inspection are not technically evaluated. The released prompt also says to “always keep the last page” whenever the agent answered, which conflicts with a reliable zero-evidence warning for answers unsupported by visited pages.

The human study identifies a **bundle**, not breadcrumb causality: HANSEL adds selected pages, titles/descriptions, highlights, embedded live state, action replay, grid/carousel layouts, and direct interaction relative to source links, while both conditions retain step-by-step trajectories. Accuracy rose from 75.0% to 82.14%, but the mixed model was nonsignificant (`p=.29`). On the 28 wrong-agent opportunities per condition, participants corrected 19 with HANSEL and 17 with baseline. Nine HANSEL wrong-answer submissions remained wrong, with mean confidence 5.67/7 in the released data. Faster, easier review therefore coexists with confidently missed errors.

The transferable result for `skill-bench` is a **loss-accounted evidence projection**, not an “interactive verification” oracle:

`authoritative raw state/trajectory → typed inclusion and omission decisions → projected evidence with source/state identity → reviewer exposure and inspection → supported judgment → correct accept/reject/correct/escalate action → artifact/decision consequence`

Every arrow needs separate evidence. Compression, extraction agreement, interactivity, preference, time, error correction, calibrated reliance, and professional utility must not inherit one another.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, and C by studying scalable human review of long agent traces, converting the findings into a cross-domain evidence-projection boundary, and identifying executable contrast cases for existing trace, artifact-view, metric, task-health, and validity machinery. Web navigation is the experimental substrate, not a project scope commitment.

- **Concrete evidence:** the full immutable paper, full paper-linked pre-v1 supplement, prompt, protocol, surveys, all 112 participant-task rows, and analysis notebook.
- **Uncertainty clarified:** when trajectory compression reduces burden without establishing complete, faithful, or causally useful verification evidence.
- **Mode:** validation-oriented expansion with consolidation implications.
- **Useful completion:** preserve HANSEL's evidence-view idea while separating support extraction, omission risk, state replay, human inspection, correct judgment, burden, trust calibration, and consequence.

## Sources and reading record

### Primary paper read in full

- Yujin Zhang and Daye Nam, *HANSEL: Extracting Breadcrumbs from Web Agent Trajectories for Interactive Verification*.
- Immutable arXiv v1: <https://arxiv.org/abs/2606.18671v1>; submitted 17 June 2026; no withdrawal/retraction notice in the acquired metadata.
- Local PDF: `data/papers/pdfs/2606.18671v1-hansel.pdf` (13 pages; SHA-256 `c668a64e39b8d86cb06861b29fe7339ade0285dd0e96d462a8756b5078b35541`).
- Full layout text: `data/papers/text/2606.18671v1-hansel.txt` (SHA-256 `1c62913fcd15c8784ad3059d2df215372a3a72766f31b5eaf2863bcac11628c6`).
- Manuscript source: `data/papers/source/2606.18671v1.tar.gz` (SHA-256 `da8952a6752bbad736585846fb500868e35206897b191824847556719b4b29fd`).
- Acquisition and release provenance: `data/sources/releases/2606.18671v1-hansel/provenance.json`.

The complete paper was read through the formative trajectory analysis, extraction pipeline, implementation, technical evaluation, user study, discussion, limitations, conclusion, and references. Page references below use PDF pages.

### Paper-linked supplement audited in full

The paper links <https://github.com/cloudsreal/hansel_study>. The complete 14-file repository is pinned at commit `a23466cf71eb4e466ffaa7a59b4f672f74f80658`, tree `95f7df43a16c8e80014aa4384bcd456219da3962`, dated 29 April 2026—before arXiv v1, but not proven to be the exact study build.

- Archive: `data/sources/releases/2606.18671v1-hansel/cloudsreal-hansel_study-a23466c.zip` (SHA-256 `843a3b8ae24499fcf99777f630a08d2a010990039ef567aeb63fb87af2285a89`).
- Extracted root: `data/sources/releases/2606.18671v1-hansel/repository/hansel_study-a23466cf71eb4e466ffaa7a59b4f672f74f80658/`.
- Extraction prompt: `prompt.md`.
- Complete protocol: `study/User Study Protocol.pdf`.
- Participant/task responses: `study/analysis/Task Response Form.csv`.
- Timing/correctness table: `study/analysis/Time for each task - Sheet1.csv`.
- Merged participant table: `study/analysis/merged_raw_by_participant.csv`.
- Analysis: `study/analysis/section7_paper_analysis.ipynb`.
- Recruitment, pre-task, task, and group-specific post-study survey PDFs under `study/survey/`.

The supplement substantially improves study inspectability: all 14 × 8 = 112 task records are present, the condition schedule and wording are visible, and the notebook implements the reported accuracy, correct-only time/effort, preferences, and five rating comparisons. It contains **no** HANSEL implementation, technical-evaluation trajectories, page/step ground-truth labels, extraction outputs, snippet labels, replay scripts, reconstructed page states, system screenshots/state archives, participant interaction logs, screen recordings, interview transcripts, qualitative codebook, page-visit table, or technical cost/run ledger. No license is present.

## One-sentence contribution

HANSEL converts a web agent's long action trajectory into a smaller, interactive set of model-selected page and snippet views, reducing review burden while leaving projection completeness and verification validity as separate empirical questions.

## Research question and claim boundary

HANSEL asks whether web-agent trajectories can be converted from passive logs into a concise, interactive post-hoc evidence view that makes agent answers easier to verify. It contributes:

1. a standardized observation–reasoning–action trajectory representation;
2. an LLM projection from trajectory steps to evidence pages, snippets, titles, and descriptions;
3. replay of per-page actions in an Electron `BrowserView`, with injected snippet highlights;
4. a 45-task extraction study; and
5. a controlled eight-task user study with 14 participants.

The conceptual contribution is strong: a reviewer often needs an **entry point into authoritative state**, not another natural-language explanation. The claim boundary is narrower than the paper's recurring “verifiable evidence” language. The system presents model-selected, current live pages reconstructed through action replay. Those views may be useful evidence candidates; they are not shown to be authoritative snapshots, complete verification bases, or faithful explanations.

## Methodology and system

### Trajectory sample and authored reference

The authors use HAL browser-use trajectories from two benchmarks (Section 3.1, pp. 3–4):

- **AssistantBench:** all 33 development tasks begin with o3-medium trajectories reported at 38.8% accuracy. Tasks without an answer or without web interaction are removed, leaving 22.
- **Online-Mind2Web:** Claude Sonnet 4 trajectories are reported at 40.0% accuracy. Open-ended tasks without one verifiable answer are removed, leaving 140; 23 are randomly sampled with a fixed but unreleased seed.

The resulting 45 trajectories contain 592 steps and 271 page visits. A “page” is one consecutive URL run; a nonconsecutive revisit to the same URL counts again. The first author labels evidence steps as those contributing to the reasoning leading to the final answer. Failed attempts, overhead, blocked pages, and retries without new information are negative. A page is positive if it contains at least one positive step. A second web-agent-familiar annotator labels all records; Cohen's kappa is 0.803 for steps and 0.878 for pages, followed by discussion adjudication (p. 3).

This is good evidence that two informed annotators can apply the authors' **contribution-to-final-path** rule consistently. It is not a ground truth for a minimal sufficient verification set:

- a failed search path may establish that a source was inaccessible or that an alternative was not checked;
- an abandoned branch can contain a cheaper or otherwise disqualifying candidate;
- a blocked page can make a completeness claim unverified;
- navigation/filter state may be decisive even if no visible fact directly supports the final answer;
- “contributed to the answer” is endogenous to the agent's chosen path, while verification asks whether that path omitted requirements or contrary evidence.

The sample is also outcome-conditioned. AssistantBench excludes no-answer/no-web runs; Online-Mind2Web excludes open-ended tasks; the later human study again excludes cases with little progress or usable outcome. This creates a best-case substrate for support-path review and omits important abstention, recovery, and empty-evidence cases.

### Evidence extraction

The LLM receives the user query, final answer, and all standardized trajectory steps. It groups consecutive equal URLs, drops failed/blocked/abandoned paths, and returns page titles, descriptions, selected steps, and exact visible snippets (Section 4.1, pp. 5–6). The paper reports GPT-5.4 at temperature 0.7 (Section 4.4, p. 7).

The released prompt reveals important behavior not fully visible in the system diagram:

- it says to keep only the final plan and drop failed, blocked, unrelated, redirected, and retry pages;
- it asks for “all trajectory steps” but explicitly narrows output to the successful path;
- it requires `agent_answered`, answer text, and answer step to be copied rather than checked;
- it says to **always keep the last page before final answer or termination** when `agent_answered=true`;
- it defines snippets as exact visible labels or text, but supplies no formal unsupported/contradicted/insufficient state;
- the shown JSON template is syntactically missing a comma between `page_title` and `description`, although actual model parsing behavior is unreleased.

The always-keep-last rule is especially important. The paper says an unsupported answer can produce no evidence page and thereby expose a gap (pp. 1, 6, 11). But the released prompt forces one last page for any answered trajectory. Without released outputs and zero-evidence tests, the advertised unsupported-answer behavior is not established and may be structurally discouraged.

### Live reconstruction and highlighting

HANSEL parses actions for each selected page, opens a live page in Electron, replays waiting/clicking/scrolling/filter actions, and injects CSS to highlight selected snippets (Section 4.2–4.4, pp. 6–7). This is more actionable than a bare URL or screenshot. It is not preserved state in the archival sense:

- the paper describes current live pages, not frozen DOM/network/session snapshots;
- no source timestamp, content hash, URL canonicalization, session/cookie identity, viewport, locale, personalization, or dependency version is recorded;
- action replay can fail or land on changed content;
- exact text may occur multiple times, disappear, or be rendered dynamically;
- no replay success, state-equivalence, highlight-localization, or stale-page metric is reported;
- Section 8.1 explicitly celebrates seeing whether a price has changed on revisit, confirming that the view can show current state rather than the state that supported the original agent answer.

Interactive current evidence can be useful for rechecking. It must not be described as the exact historical state without an independent state-fidelity witness.

## Technical evidence and what it supports

### Page extraction

Against 98 adjudicated positive pages among 271 page visits, HANSEL selects 104 pages. The reported micro metrics imply 87 true positives, 17 false positives, and 11 false negatives:

- precision `87/104 = 0.837`;
- recall `87/98 = 0.888`;
- F1 `0.861`;
- output reduction `(271-104)/271 = 61.6%`.

These are useful extraction statistics on the selected corpus. “Trajectory volume” means **page-count output**, not review time, bytes, visual complexity, action count, or semantic burden. A 61.6% page reduction does not show that 61.6% of review work disappears.

Counts are pooled across pages. No task-macro distribution, bootstrap interval, task-clustered uncertainty, per-task failures, benchmark interval, repeated LLM extraction, temperature sensitivity, or error-severity weighting is reported. Eleven omitted support pages can be more consequential than many correctly omitted navigation pages.

### Snippets

Two annotators judge the 159 predicted snippets on correctly extracted pages. They mark 141 valid, giving precision 0.887 and kappa 0.742 before consensus (Section 5, p. 7). A snippet is valid if visually observable and supportive of the final answer.

There is no reference inventory of all required snippets and therefore no snippet recall, omission rate, contradiction coverage, constraint coverage, or claim-to-snippet completeness. The evaluation also conditions on correctly selected pages, excluding snippet behavior on false-positive pages and omitted pages. High predicted-snippet precision cannot license “minimal sufficient evidence.”

### Missing technical tests

The technical evaluation does not test:

- unsupported-answer or no-evidence flag precision/recall;
- whether an extracted page actually entails the answer;
- whether all task constraints and comparison alternatives are represented;
- contradictory, negative, temporal, authority, freshness, or provenance evidence;
- page-state replay success or historical equivalence;
- exact highlight localization;
- reviewer-visible state after page mutation, login, personalization, or bot defenses;
- repeated extraction reliability;
- model/version/prompt/seed/retry/invalid-output sensitivity;
- tokens, latency, API cost, rendering cost, or failure rate.

The technical corpus, labels, outputs, and implementation are absent from the supplement, so even the reported tables cannot be independently reconstructed.

## Human study

### Design and participants

Fourteen English-proficient AI-tool users from one research university complete all eight fixed tasks in a within-subject alternating schedule (Section 6, pp. 7–8). Seven are in computing/engineering, three in business/economics, two in law, one in cognitive science, and one in communication/journalism. Eight report no agent-mode use; only two report modest web-task proficiency.

The released protocol adds details absent or compressed in the paper:

- group assignment alternates by enrollment order rather than random allocation;
- Group A receives `H-B-H-B-H-B-H-B`; Group B receives the inverse;
- all participants see the same fixed task order;
- both interfaces are demonstrated for about ten minutes, in group-dependent order;
- participants are told the agent uses a strong model with well-designed prompts and is “generally reliable”;
- remote participants control the researcher's machine over video conferencing;
- participants have five minutes per task and may search externally;
- the researcher is present and asks for the correct answer;
- $25 compensation is promised.

Each task is shown in both conditions to seven participants, so interface exposure is balanced within task. However, allocation is quasi-random at best, condition alternates deterministically, period/learning effects are fixed, task order is not randomized, and no group/sequence interaction is modeled.

### Task and treatment construction

The eight tasks comprise four author-defined pairs: pricing calculation, sorting/filtering, selection under constraints, and information retrieval. Tasks 1, 4, 5, and 8 have correct agent answers; Tasks 2, 3, 6, and 7 have wrong answers. Thus each condition receives 28 correct-agent and 28 wrong-agent opportunities across participants.

The treatment is not evidence-page compression alone:

- **Both conditions:** query, final answer, related pages, and step-by-step action trajectory.
- **Baseline:** source links opening pages.
- **HANSEL:** model-selected page subset, model-generated titles/descriptions, highlights, embedded `BrowserView`, replayed page state, grid/carousel organization, and direct editing/navigation.

The study therefore estimates the effect of this complete presentation-and-interaction package under the fixed task schedule. It cannot attribute outcomes to selection, titles, highlights, replay, interactivity, or reduced page count separately.

Task selection again favors usable trajectories. The authors reject many AssistantBench cases where the agent made little progress or used an unexpected strategy, because participants would need to start over (Sections 6.2 and 8.2, pp. 8, 11). Those cases are exactly where a verification system must signal insufficiency or route mismatch rather than look helpful.

### Accuracy and error opportunities

The released 112-row table reproduces the paper's counts:

| Agent-answer stratum | Baseline | HANSEL |
|---|---:|---:|
| Correct agent answer | 25/28 participant answers correct (89.3%) | 27/28 (96.4%) |
| Wrong agent answer | 17/28 corrected (60.7%) | 19/28 corrected (67.9%) |
| Overall | 42/56 (75.0%) | 46/56 (82.14%) |

The logistic mixed model uses interface and task fixed effects plus a participant random intercept. The interface estimate is positive but nonsignificant (`β=0.71`, `SE=0.67`, `z=1.06`, `p=.29`; Section 7.1, p. 9). There is no task-random generalization, condition-by-task heterogeneity, group/sequence term, or power/precision interval.

For wrong-agent tasks, “participant answer correct” is a reasonable correction/error-detection endpoint because an incorrect supplied answer creates a shared opportunity. But only two additional corrections under HANSEL separate conditions. The paper's statement that participants “rated” error identification higher refers to retrospective self-report, not demonstrated detection accuracy.

The released task rows expose a trust warning. Of 28 wrong-agent opportunities under HANSEL, nine remain wrong (32.1%). Their mean submitted confidence is 5.67/7. Baseline has 11 wrong submissions with mean confidence 4.36/7. These are descriptive, selected-error summaries rather than a preregistered calibration analysis, but they directly refute any inference that higher HANSEL confidence is necessarily better calibrated.

### Time and effort

The paper analyzes completion time and effort only on the 88 correct participant submissions. The released data reproduce:

- baseline: 42 correct records, mean 167.7 seconds;
- HANSEL: 46 correct records, mean 130.4 seconds;
- mixed-model interface estimate `-43.20` seconds, `SE=10.03`, `t=-4.31`, `p<.001`;
- participant-median effort: 4.39 baseline versus 2.89 HANSEL, Wilcoxon `V=7`, `p=.012`, reported `r=.67`.

Correct-only analysis avoids conflating a quick wrong acceptance with efficient verification, but it conditions on a post-treatment outcome that differs by interface. It changes the estimand to time/effort **among successful submissions under each condition**, not total review burden or intention-to-treat efficiency. The released all-record raw means are 172.57 seconds baseline and 127.84 seconds HANSEL; these descriptive means also favor HANSEL, but no all-task model, timeout/censor policy analysis, or speed–accuracy joint estimand is reported. One baseline record is exactly five minutes.

Effort and time omit setup, extraction latency, replay failures, generation cost, page-load delay, researcher support, follow-up checking, and lifecycle maintenance. The experiment measures participant task time in an administered interface, not total system-review cost.

### Preferences and qualitative claims

All 14 participants prefer HANSEL and select it as easier for verification. Five paired Likert comparisons favor HANSEL with unadjusted reported p-values from `.0013` to `.0127`; no multiplicity family or correction appears in the paper or notebook. Feature ratings favor highlights (4.79), direct interaction (4.64), and titled evidence pages (4.43).

These are strong perception results under a visibly richer interface. They do not identify which feature caused preference, and demand effects are plausible: the protocol describes HANSEL's evidence pages, state, highlights, views, and interaction in more detail than the baseline; participants know the study concerns verification; and the researcher is present.

Qualitative findings appropriately reveal both strategies: some users treat pages as independent-check starting points, while others treat highlights as confirmation and stop checking (Sections 7.4–8.1, pp. 10–11). Yet the release omits recordings, transcripts, interaction events, page-visit counts, codebook, participant-by-theme matrix, and negative-case table. Initial open coding is done by the first author and refined with the second by consensus; no independent summative reliability is reported. Selected quotations support mechanism hypotheses, not prevalence.

## Unique insight: compression requires an omission ledger

HANSEL's key insight is correct but incomplete: reviewers should not have to reread every low-level action. The benchmark-design lesson is not “show fewer pages.” It is **make evidence projection an explicit, falsifiable transformation**.

A support-path extractor asks, “Which visited pages helped produce this answer?” A verifier needs a broader question: “Which observations are necessary to test the answer, its requirements, alternatives, provenance, and failure conditions?” The two sets overlap but are not identical. For a “cheapest” claim, a page supporting the chosen item is insufficient without coverage of candidate space, filters, sorting, exclusions, time, and source authority. Failed and blocked paths may be decisive insufficiency evidence.

Every projected review packet should therefore preserve:

1. the immutable source trajectory/state identity;
2. the projection algorithm/configuration identity;
3. every included unit and its criterion/claim role;
4. every omitted unit with a typed reason;
5. explicit contradiction, negative-search, blocked-route, and unavailable-evidence records;
6. projection uncertainty and `insufficient_evidence`/`unsupported` states;
7. transformation/replay identity and fidelity evidence;
8. reviewer exposure and actual locator inspection;
9. judgment, confidence, correction/escalation, and consequence.

Compression is valid only relative to a named decision and loss function. Omitting redundant navigation may be harmless; omitting one disqualifying alternative may dominate the decision. Page-count reduction alone cannot express that asymmetry.

## Comparison with adjacent reviewed evidence

- **Pista:** Pista compresses many spreadsheet mutations into semantic operations; HANSEL compresses trajectory pages into support breadcrumbs. Both lower the unit of inspection while making the projection itself an evaluated artifact. Pista needs operation/range/dependency fidelity; HANSEL needs page/snippet/state/omission fidelity. Neither preference, richer explanation, lower prompting, nor lower time proves correct oversight.
- **ArtifactCopilot:** ArtifactCopilot organizes criterion-linked phase packets; HANSEL organizes answer-linked page packets. ArtifactCopilot exposes route-completeness risk, while HANSEL's explicit dropping of abandoned/failed/blocked paths makes that risk concrete. Both need raw observations, alternative-route and contradiction records, packet-checker calibration, reviewer inspection, and adoption/decision validity.
- **Pista's oversight ladder:** HANSEL provides stronger shared wrong-answer opportunities than Pista's unmatched stochastic defects, but only eight fixed tasks and 28 wrong-answer opportunities per condition. It reaches burden and bounded correction observations, not faithful evidence projection, calibrated reliance, or artifact/professional consequence.
- **Existing trajectory observers:** a structured view can improve navigation without validating the labels or omissions that structure it. Developer diagnosis, end-user answer verification, grader adjudication, and professional approval require different evidence selections and authority.

## Limitations and validity threats

1. The 45-task corpus is small and split across two benchmarks/configured agents.
2. AssistantBench removes no-answer and no-web trajectories.
3. Online-Mind2Web removes open-ended tasks and samples only single-answer cases.
4. The random seed and eligible task IDs are unreleased.
5. The evidence definition follows the agent's final reasoning path rather than an independent verification obligation set.
6. Failed, abandoned, blocked, and retry paths are excluded even when they may prove incompleteness or contrary evidence.
7. Annotation authority is two system-familiar annotators, one a paper author; domain/source authority is not established.
8. Adjudication removes disagreement from final labels without preserving contested cases.
9. Page metrics are pooled without task-clustered uncertainty or macro distributions.
10. Extraction is tested once despite temperature 0.7.
11. GPT-5.4 endpoint identity, date, seed, retries, token limits, invalid outputs, and costs are absent.
12. The released prompt's forced last-page inclusion conflicts with a clean unsupported-answer signal.
13. Snippet evaluation measures precision only and conditions on correctly selected pages.
14. No snippet-recall, requirement-coverage, contradiction, negative-evidence, or entailment test exists.
15. “61.6% trajectory volume reduction” is page-count compression, not measured cognitive or operational burden.
16. No state-replay, temporal fidelity, source identity, session, personalization, or highlight-localization test is reported.
17. Live replay can expose current content rather than the historical state supporting the answer.
18. The implementation, technical corpus, labels, outputs, and replay records are unreleased.
19. The user study selects eight usable trajectories and excludes important route-mismatch/little-progress cases.
20. Four task pairs are author-matched by type/complexity without independent equivalence evidence.
21. Four correct and four wrong answers are fixed by task; only eight tasks support inference.
22. Group allocation alternates enrollment rather than using reported random assignment.
23. Task order is fixed and condition alternates deterministically.
24. Interface, task, position, group, learning, and fatigue are only partially separated; no sequence/group interaction is tested.
25. The treatment bundles selection, titles, descriptions, highlighting, embedding, replay, layouts, and interaction.
26. Participants are university-affiliated AI users, not sampled professionals or affected decision makers.
27. Researcher presence, remote control, explicit verification instructions, and “strong/reliable agent” framing differ from ordinary use.
28. Accuracy improves by four of 56 records but the modeled contrast is nonsignificant and has no interval.
29. Correct-only time and effort condition on post-treatment success.
30. No speed–accuracy, decision-loss, timeout, or severe-error estimand is reported.
31. Confidence is higher under HANSEL even among its wrong submissions; calibration is not modeled.
32. Five paired post-study rating tests lack multiplicity correction or a preregistered family.
33. Preference and feature ratings are vulnerable to treatment richness and demand effects.
34. Interaction logs, page inspections, correction paths, external searches, and replay failures are not released.
35. Qualitative transcripts, codebook, videos, page counts, and independent coding agreement are absent.
36. No delayed use, repeated task, handoff, recipient decision, downstream consequence, or professional workflow is observed.
37. No implementation or data license is present, limiting reproducible reuse.

## Reproducibility and operational realism

**Human-study reproducibility is moderate by HCI-paper standards.** The pre-v1 supplement exposes exact condition schedules, task wording, agent-answer correctness strata, forms, 112 timing/correctness rows, participant responses, and executable R analysis logic. Core counts and descriptive means can be reconstructed. Exact qualitative results and behavior claims cannot: recordings, logs, transcripts, page visits, codebook, and task-state packages are absent. The notebook may install `lme4` and `lmerTest` from current CRAN, so dependency versions are not frozen.

**Technical reproducibility is poor.** The prompt is released, but the implementation, standardized trajectories, eligible sample, labels, extraction outputs, state-replay inputs, browser environment, page snapshots, and run ledger are absent. Mutable web pages and a named preview-generation model without endpoint pinning make future reruns non-equivalent.

**Operational realism is mixed.** Real open-web trajectories, live pages, filtering/sorting mistakes, external search, direct correction, bot defenses, and current-page change are more realistic than static answer review. But the administered university study, five-minute tasks, fixed ground truth, selected usable paths, researcher machine, and no consequential action evaluate an interface prototype—not production oversight, long-term use, professional verification, or readiness.

## Transfer to skill-bench

### Retain

1. Project raw trajectories into decision-relevant evidence views rather than forcing full-log consumption.
2. Preserve direct access to authoritative/native state alongside summaries.
3. Keep full trace access available as a fallback and record when reviewers expand beyond the projection.
4. Represent page/state actions, filters, queries, scroll positions, and source identity—not URL alone.
5. Separate extraction accuracy, burden, answer correctness, correction, confidence, preference, and consequence.
6. Use shared wrong-answer/defect opportunities when testing review assistance.

### Repair

7. Replace “final successful path” labels with claim/criterion-specific verification obligations including alternatives, contradictions, negative evidence, blocked routes, and uncertainty.
8. Add an omission ledger: every removed trace unit needs a typed policy reason and authority.
9. Distinguish `supports`, `contradicts`, `qualifies`, `coverage evidence`, `failed access`, `irrelevant`, and `unknown` rather than evidence/non-evidence.
10. Pin historical state snapshots and separately label live refreshes; verify replay equivalence before calling state preserved.
11. Evaluate snippet/page recall, requirement coverage, contradiction coverage, unsupported-answer detection, and severity-weighted loss—not precision and page count alone.
12. Record extraction repeats, model/prompt/version hashes, invalid outputs, latency, tokens, cost, and service failures.
13. Log reviewer exposure, opened locators, dwell/action events, external search, full-trace fallback, correction, and escalation.
14. Analyze all-task speed–accuracy/decision-loss jointly; keep correct-only efficiency as a secondary conditional estimand.
15. Test confidence calibration with faithful, incomplete, misleading, contradicted, and empty packets.
16. Factor the bundle: links; selected pages; verified titles; highlights; replayed state; direct interaction; and cognitive-forcing prompts.
17. Generalize over task and reviewer populations only after crossed hierarchical designs and professional/recipient validation.

### Test before adopting

- **Projection contrast set:** one redundant-navigation case, one omitted disqualifying alternative, one blocked authoritative source, one stale page, one repeated URL with changed state, one unsupported memory answer, and one contradictory source.
- **State-fidelity test:** frozen historical snapshot versus current live replay versus intentionally divergent session/personalization, with exact expected `valid`, `stale`, `diverged`, or `insufficient` outcomes.
- **Human study:** identical frozen trajectories crossed with full trace, support-only projection, loss-accounted projection, misleading/incomplete projection, and loss-accounted projection plus forcing prompts; measure severe-error detection, correct accept/reject/correct/escalate action, confidence calibration, time, actions, and total review cost.
- **Cross-domain transport:** apply the same projection contract to a spreadsheet semantic diff and a criterion-linked artifact-review packet before claiming domain-general oversight support.

## Concrete repository actions

- Added this full-text, full-supplement deep review.
- Updated the paper index from acquisition-pending to deep-review/release-audited status.
- Added HANSEL to topic navigation and the oversight synthesis because it adds a distinct loss-accounted evidence-compression boundary and released shared-error human records.
- **No new queue task added.** Existing trace/evidence-view, artifact-admissibility, interaction, task-health, metric, validity, and review-burden machinery already provides homes. The paper supplies nonduplicate validation cases, not a new schema.

## Assessment

- **Evidence tier:** B — complete immutable paper and full pre-v1 supplement audited; human quantitative records inspectable; technical corpus/implementation and qualitative records absent.
- **Most reusable contribution:** interactive evidence views as compact entry points into the underlying state.
- **Strongest evidence:** lower task time and effort plus strong preference under one 14-participant, eight-task bundled study; page-support extraction agreement on 45 selected trajectories.
- **Most serious construct flaw:** support-path contribution labels omit the alternatives, contradictions, blocked routes, and negative evidence needed to validate many answers.
- **Most serious system flaw:** “preserved state” is unvalidated live action replay, not an immutable historical-state witness.
- **Most serious human-factors warning:** 32.1% of wrong-agent HANSEL opportunities remained wrong, and those wrong submissions were highly confident in the released records.
- **Safe claim:** on eight fixed web tasks with 14 university-affiliated participants, HANSEL's bundled interactive evidence interface reduced successful-task time and perceived effort and was preferred, while producing a small nonsignificant accuracy difference. On 45 selected trajectories, one extractor matched adjudicated support-page labels reasonably well while reducing selected page count. The study does not establish complete or faithful verification evidence, calibrated oversight, general error detection, professional validity, production utility, or readiness.
