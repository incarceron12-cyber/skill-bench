# Human oversight in practice: a lifecycle allocation pattern, not evidence that current heuristics work

## Bottom line

Dhanorkar, Passi, and Vorvoreanu provide useful descriptive evidence that experienced developers do not confine oversight to watching an agent run or checking its final output. In 17 semi-structured interviews, participants described allocating effort across **a priori control, co-planning, real-time monitoring, and post hoc review**. They also described four post-hoc shortcuts: treating the plan as a proxy for execution, treating passing tests as a correctness guarantee, spot-checking outputs and explanations, and deferring to agents in unfamiliar domains. The paper's distinctive contribution is to locate oversight work across the whole task lifecycle and to show that practical review is budgeted and selective rather than exhaustive.

The evidence is exploratory and retrospective. Twelve participants worked at the authors' large technology company; all were purposively selected experienced weekly users; most delegated small, short tasks; one author conducted every interview and all open coding; the final taxonomy is partly induced by an interview guide explicitly organized before, during, and after deployment. The paper reports no saturation or stopping rule, participant-by-theme matrix, prevalence counts for most themes, independent open coding, negative-case protocol, member checking, observed sessions, retained artifacts, traces, test suites, corrections, incidents, or outcomes. Selected reports establish that these practices and heuristics occurred in this sample—not that they are representative, normatively adequate, accurate, causally effective, safe, productive, compliant, or production-ready.

The central transfer to `skill-bench` is therefore not “copy developer best practices.” It is an **oversight-allocation contract**:

`oversight opportunity → available control/evidence/action → human exposure → effort allocation → judgment/intervention → agent or artifact uptake → independently observed state/consequence → burden and residual risk`.

A benchmark should preserve each link separately at configuration, planning, execution, and review time. Plans, tests, diffs, generated diagrams, model agreement, familiar code, and quick scans are candidate evidence views with known blind spots—not validated grader rules. Human presence, review availability, or a checked box does not establish meaningful oversight.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, C, and E through narrow expansion into observed, production-adjacent oversight work. Software development is the empirical setting, not a scope commitment. The general hypothesis is that realistic knowledge-work evaluation must represent **where humans retain authority, when they can observe or intervene, what evidence they actually inspect, and what review burden they bear**, rather than treating “human in the loop” as one binary feature.

- **Concrete evidence:** the full immutable arXiv v1 paper, including participant table, usage-scenario appendix, complete interview guide, and oversight-work table; official Microsoft Research publication metadata.
- **Uncertainty clarified:** the difference between a reported oversight practice, its realized execution, its decision quality, and its downstream effect.
- **Mode:** human learning with validation implications.
- **Duplication/scope check:** Pista and HANSEL experimentally study particular review interfaces; Human-on-the-Bridge specifies reusable evaluation policy; ArtifactCopilot studies evaluator reports; *Measuring Agents in Production* maps selected team reports. This paper uniquely reconstructs how experienced users say they distribute oversight work around ordinary agent use. It does not justify a coding-only benchmark or a new oversight subsystem.
- **Useful completion:** retain the four lifecycle locations and efficiency–thoroughness tension while refusing to convert participant heuristics into rubric requirements or oversight-effect claims.

## Sources and reading record

### Primary paper read in full

- Shipi Dhanorkar, Samir Passi, and Mihaela Vorvoreanu, *Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents*.
- Immutable arXiv v1: <https://arxiv.org/abs/2606.05391v1>; submitted 3 June 2026. The acquired metadata contains no withdrawal or retraction notice.
- Local PDF: `data/papers/pdfs/2606.05391v1-human-oversight-agentic-systems-practice.pdf` (28 pages; SHA-256 `72f43af45bba81b46d168dc3f7989621871fd2f603503c37c33788d26ae1c10b`).
- Local layout-preserving text: `data/papers/text/2606.05391v1-human-oversight-agentic-systems-practice.txt` (SHA-256 `a42bca97f9e99f9072253a56dca125c2d33bd0fe3406f56b8d04c05c29468504`).
- ArXiv metadata: `data/papers/source/2606.05391v1-metadata.xml` (SHA-256 `0f9927df13033759c2efc354755d7de41b399b58269f16d7a3e771994091ba2c`).

The complete paper was read through methods, findings, discussion, limitations, conclusion, references, participant table, usage scenarios, complete interview guide, and final taxonomy table. Page references below use PDF pages; extraction line ranges are included for auditability.

### Official publication metadata

- Microsoft Research publication page: <https://www.microsoft.com/en-us/research/publication/human-oversight-of-agentic-systems-in-practice-examining-the-oversight-work-challenges-and-heuristics-of-developers-using-software-agents/>
- Preserved clean metadata: `data/sources/microsoft-human-oversight-agentic-systems-practice.md`.
- Provenance: `data/sources/microsoft-human-oversight-agentic-systems-practice.provenance.json`.

The official page identifies the authors and FAccT venue. It supports publication metadata only; the immutable PDF is the full-paper evidence. The paper reports no linked study package, transcripts, codebook, coded table, analysis materials, observed agent sessions, or outcome data.

## One-sentence contribution

The paper identifies four lifecycle locations where experienced developers report doing agent oversight and four efficiency-oriented post-hoc heuristics, making oversight allocation and burden visible while leaving practice prevalence, heuristic accuracy, causal efficacy, and consequence unmeasured.

## Research questions and claim boundary

The paper asks (pp. 2–3; extraction lines 68–107):

1. How do developers oversee software agents in practice?
2. What oversight challenges do developers face, and how do they address them?

Its intended contribution is an early empirical anchor for a literature dominated by conceptual frameworks and narrow laboratory verification tasks. That framing is appropriate if “in practice” is read as **retrospective reports from a purposive intensity sample**, not direct field observation. The authors themselves call the work exploratory, acknowledge that 12 of 17 participants came from one company, and deny that the taxonomy is exhaustive or fully generalizable (pp. 2–3; lines 68–100).

The evidence supports bounded claims that:

- selected experienced developers reported doing oversight before, during, and after agent execution;
- the authors' analysis usefully grouped those reports into control, co-planning, monitoring, and review;
- participants reported information, specification, monitoring, code-comprehension, and repeated-review challenges;
- participants described relying on plans, tests, spot checks, and epistemic deference to make post-hoc review manageable; and
- small task delegation and short runs were common in the reported production-grade use cases.

It does **not** establish:

- population prevalence within the company, software engineering, or knowledge work generally;
- that the four forms are exhaustive, mutually exclusive, naturally occurring rather than interview-shaped, or ordered in every workflow;
- that any practice was actually exercised as reported in a particular session;
- that plans faithfully predicted execution, tests covered relevant requirements, eyeballing detected consequential errors, or agreement between agents was independent evidence;
- that a priori controls were enforceable, co-plans were complete, monitoring cues were calibrated, or post-hoc corrections preserved collateral state;
- that bounded oversight improved quality, safety, productivity, compliance, professional learning, or readiness; or
- that experienced power users model “best practices” for less experienced or resource-constrained users.

The paper occasionally moves from intensity-sample description to stronger language—for example, that seasoned developers' challenges are “likely worse” for users with less accurate mental models (p. 5; lines 220–235), that heuristics are “necessary adaptations” (p. 14; lines 628–644), or that the developer-manager role is emerging (pp. 15–16; lines 671–685). These are plausible hypotheses and interpretations, not comparisons or measured effects in this design.

## Methodology

### Sampling, eligibility, and organizational context

The authors define a software agent as a system that autonomously plans and acts with tools and an environment, excluding simple code completion. They use criterion and snowball sampling through professional contacts. A screener requires at least weekly professional use and self-reported experience; interview opening questions serve as a secondary screen, excluding one participant (pp. 5–6; lines 204–243).

The final sample contains 17 participants:

- 12 used agents daily, four several times per week, and one once per week;
- nine self-described as experienced, four somewhat experienced, and four very experienced;
- 13 had at least seven years of programming experience, two had four to six years, and two had one to three years;
- roles were primarily software engineers, with two engineering managers, one technical program manager, and one data science/ML engineer;
- 15 were men and two women; 14 were in the United States, with one each in India and Brazil;
- participants named a heterogeneous set of products including GitHub Copilot, Cursor, Claude Code, Cline, Codex, Gemini, Kiro, Aider, and CodeWhisperer (Appendix A, pp. 25–26; lines 1156–1219).

Twelve participants worked at the authors' large technology organization, on reportedly distinct teams with no overlapping projects. Recruitment outside the firm was constrained by NDAs, proprietary work, and competitive sensitivity. The authors say the five external participants reported similar experiences, but provide no cross-company coding table or negative-case comparison (p. 6; lines 234–243).

This is a defensible **intensity sample** for discovering candidate practices. It is not a prevalence or comparative sample. Selection favors people who adopted agents, use them often, remain willing to discuss them, and work in resource-rich settings. It excludes non-adopters, former users, failed deployments, people prevented from using agents, and most resource-constrained or non-software workers. The paper reports neither the recruitment funnel nor how many screened, declined, were ineligible, or were inaccessible beyond the one secondary-screen exclusion.

### Interview procedure

The first author conducted all one-hour, one-to-one video interviews in July–August 2025. Interviews were video-recorded and transcribed with Marvin; participants consented, received a US $40 gift card or equivalent, and the study received organizational IRB approval (p. 6; lines 246–260).

The semi-structured guide is unusually inspectable (Appendix C, pp. 26–27; lines 1250–1302). It asks about:

- agent-use scenarios and agent choice;
- custom instructions, connected tools, risks, and evals “before deployment”;
- governance and intervention “at run-time”;
- correctness, goodness, inspected artifacts, and verification “post deployment”; and
- workflow changes and getting unstuck.

This structure is both a strength and a treatment. Temporal anchoring grounds reports in an end-to-end workflow, but the authors explicitly acknowledge that asking what people do before, during, and after execution shaped the four-form taxonomy (p. 6; lines 246–256). “Deployment” also spans local coding-tool use, not only production deployment, potentially cueing governance language. Participants sometimes independently distinguished co-planning from monitoring, which supports—but does not independently derive—the boundary.

The study is an interview study, not ethnography or direct workflow observation. “Lived reality,” “in practice,” and “observed” should therefore be read as analysis of participant accounts. No screen recordings of work, repository artifacts, prompts, instructions, plans, traces, diffs, tests, generated diagrams, code-review decisions, incidents, or before/after outcomes were retained or analyzed in the paper.

### Analysis and researcher roles

Analysis proceeded in three rounds (pp. 6–7; lines 261–277):

1. the first author performed all open coding using in-vivo labels for actions, practices, and challenges;
2. the first author grouped these into 13 axial codes; and
3. the first and second authors performed selective coding into two final categories: forms of oversight work and post-hoc heuristics.

The first two authors met during rounds two and three to resolve ambiguity. Footnote 3 gives two valuable examples: whether control and co-planning should merge, and whether heuristics should be interpreted as risky shortcuts or coping mechanisms. Reinspection led them to keep control/co-planning separate and describe heuristics as imperfect but necessary ways to achieve “good enough” review.

This transparency is useful, but the method has important limits:

- one researcher conducted every interview and all open coding, so interviewer interpretation and initial code construction are not independently checked;
- the second researcher enters after the candidate code universe and 13 axial categories have been formed;
- “regularly met” and “resolve ambiguities” do not reveal disagreement counts, code changes, rejected interpretations, or residual uncertainty;
- no codebook, coded excerpts, participant-by-code table, coder matrix, audit trail, reflexivity statement, member checking, peer debrief beyond the author team, or independent negative-case analysis is reported;
- no saturation, information-power, stopping, or “no new themes” criterion is reported; sample size appears recruitment-constrained rather than analytically justified; and
- the paper does not say whether every participant contributed to each category or whether contradictory cases were systematically sought.

Selected quotations are rich evidence that at least some participants expressed each view. They cannot establish category prevalence, co-occurrence, sequence, or explanatory mechanism.

## Findings and evidence interpretation

### 1. A priori control: reported prevention before prompting

A priori control comprises settings and instructions used to constrain behavior before delegation: autonomy controls, deny lists, library restrictions, repository instruction files, external-contract specifications, global context, and sandboxes (pp. 7–8; lines 287–328). All participants reportedly acknowledged a need to constrain agents, but practices ranged from substantial setup to default agent mode.

The finding broadens oversight beyond terminal review. It also exposes a missing distinction: **declared control is not realized enforcement**. Participants reported relying mainly on prompts, lacking model/configuration visibility, receiving centrally integrated black-box agents, and being uncertain about reasoning and data policies. A deny list, custom instruction, or sandbox is only a control claim until enforcement, visibility, attempted violation, realized prevention, and residual information flow are observed.

### 2. Co-planning: specification, decomposition, and seeded solutions

Co-planning includes drafting and revising plans, task decomposition, iterative prompting, negotiating implementation choices, and providing partial code. Participants described smaller tasks as easier to test and less likely to create broad side effects; detailed context was said to matter for risk-heavy work, while familiar standard solutions could use less specification (pp. 8–9; lines 330–401).

This is simultaneously:

- an oversight opportunity;
- a configured-system intervention;
- human labor and expertise input;
- a restriction of agent autonomy;
- a possible source of solution content; and
- a task-selection mechanism.

A benchmark must not attribute the outcome of a jointly specified, decomposed, seeded solution to unaided agent capability. Nor should it treat the plan as merely process evidence: co-planning changes the treatment. Its benefit must be evaluated against its authoring burden, solution leakage, decision authority, unresolved requirements, and later adherence.

The authors report a genuine design tension: people do not know in advance how much specificity is needed or when hand-holding erases the benefit of delegation. This is stronger benchmark guidance than a universal “write better prompts” prescription. The relevant estimand is quality and loss under a complete human–agent package with its total lifecycle cost, not agent score alone.

### 3. Real-time monitoring: rare, light, and cue-driven in this sample

Most participants reportedly did not proactively inspect reasoning traces; monitoring was commonly a quick glance. The authors hypothesize that task decomposition made this feasible because small tasks ran quickly and could be checked afterward (pp. 9–10; lines 403–441). Participants described three issues:

- stated reasoning can diverge from actual action and be confidently wrong;
- long run time or conversation length acts as an ad hoc cue for drift; and
- mid-run redirection may fail, requiring stop, prompt update, and restart.

This finding should not be converted into “monitoring is unnecessary.” Task size is selected by the user, and the same oversight strategy may both produce short runs and reduce monitoring. The study does not compare large and small tasks, users who monitor and do not, or runs with and without intervention. It does not observe whether quick tasks were low consequence, whether unmonitored errors survived, or whether stop/restart improved outcomes. The authors appropriately call their explanation a hypothesis.

Reasoning traces, elapsed time, token volume, and turn count are therefore **candidate warning signals**, not authoritative state. A useful benchmark should retain signal exposure, alert threshold, inspection, diagnosis, action, restart cost, new context, resumed state, and eventual consequence separately.

### 4. Post-hoc review: dominant in discussion, expensive under cognitive distance

Participants described diffs, line-by-line code review, LLM judges, agent- or human-generated tests, manual functional testing, and re-prompting. Review intensity reportedly increased for changes to legacy and interconnected systems and decreased for prototypes and demos. Two challenges dominated: understanding high-volume code one did not write and re-reviewing after every agent revision because collateral changes may occur (pp. 10–11; lines 443–495).

This is useful evidence that “final review” is not one operation. It can include source inspection, structural diffing, generated explanation, executable tests, manual interaction, and repeated correction. Each view sees different failure classes. Re-review burden also depends on whether the system preserves change locality and provides trustworthy pre/post lineage.

The paper does not observe the correctness, coverage, or cost of any review episode. A participant's statement that they read every line establishes a reported policy, not exposure, comprehension, defect recall, or approval quality. Likewise, “unrestricted” prototype autonomy may be legitimate if consequences are bounded—or unsafe if prototype code migrates into production. Task purpose, promotion path, affected parties, and consequence determine the appropriate review policy.

### 5. The four post-hoc heuristics are failure hypotheses, not best practices

#### Plan as execution proxy

Participants reported using the co-authored plan to avoid inspecting every action or line (pp. 11–12; lines 507–531). This reduces burden only if plan content is complete, the agent adheres to it, and unplanned actions or consequences are independently visible. The paper supplies no plan–trace–state comparison. For `skill-bench`, this motivates planted plan/action divergence, omitted obligation, unplanned collateral change, and stale-plan cases.

#### Passing tests as correctness guarantee

Participants used test results to focus or replace code review and acknowledged that this depends on test quality (pp. 12–13; lines 533–556). The strongest participant formulation makes humans responsible for complete specifications and tests, then treats source code as a black box. This is a coherent verification philosophy only within a validated contract. The study does not inspect requirement coverage, test authorship independence, mutation strength, false accepts, security/performance/maintainability obligations, environmental equivalence, or whether agent and test share the same misconception.

Tests should be typed as executable observers with known scope and blind spots, not “guarantees.” A passing selected suite supports only the predicates and environment it validly observes.

#### Eyeballing as efficient signal

Participants described spot-checking files, method signatures, rationales, summaries, and agent-generated data-flow diagrams (pp. 13; lines 558–576). This is practical information foraging. It can also create selective-attention failure: summaries and diagrams are transformations produced by the same system under review and may omit precisely the problematic change. A benchmark needs shared defect opportunities, exposure locators, omission ledgers, independent native-state comparison, inspection effort, detection, false alarms, and severe-error loss.

#### Trust under unfamiliarity and cross-agent agreement

Participants reported deferring to agents when they lacked library or language expertise; one used agreement between two agents as increased confidence (pp. 13–14; lines 578–590). This is the clearest safety warning. Unfamiliarity reduces the human's ability to validate the output, while shared model training, sources, prompts, or failure modes make cross-agent agreement correlated rather than independent. “It looked legitimate” and “it worked” do not establish maintainability, security, idiomatic quality, or downstream fit.

A realistic benchmark should include familiar/unfamiliar domain conditions and independent authority routing. When the reviewer lacks competence, the valid action may be escalation, additional evidence, constrained execution, or abstention—not increased trust by necessity.

## Unique insight: oversight is a budgeted lifecycle allocation policy

The paper's most reusable insight is not the four labels alone. It is that oversight is **allocated under constraints**. Effort invested before execution may reduce later review; smaller delegated units may make monitoring unnecessary; generated code volume and iteration can make exhaustive review infeasible; familiar contexts permit targeted checks while unfamiliar ones induce deference. Oversight quality therefore cannot be inferred from the presence of one human checkpoint.

Represent oversight as a policy over opportunities:

```text
task/consequence and configured authority
→ oversight opportunity at configuration, planning, execution, or review
→ available evidence views, controls, and interventions
→ human exposure and actual inspection
→ expertise/familiarity and judgment basis
→ accept, reject, constrain, edit, stop, restart, escalate, or defer
→ agent receipt / plan change / artifact or state mutation
→ independent verification and collateral-state observation
→ downstream recipient or operational consequence
→ human time, attention, re-review, delay, and residual risk
```

This yields several non-substitutable measurements:

1. **Availability:** could the human inspect or intervene?
2. **Realization:** did the opportunity occur, and was the relevant control/evidence actually presented?
3. **Exposure:** what did the person inspect, for how long, and with what task/domain familiarity?
4. **Judgment quality:** was the conclusion supported, appropriately uncertain, and routed to the right authority?
5. **Action:** what intervention or approval was attempted?
6. **Uptake:** did the agent or workflow adopt, reject, or bypass it?
7. **Consequence:** did required state improve and collateral state remain acceptable?
8. **Burden:** what time, cognitive work, re-review, interruption, delay, and opportunity cost were incurred?
9. **Residual risk:** what remained unobserved, unsupported, or falsely trusted?

The four paper categories are useful locations on this chain, but not a validated maturity scale or sequence. The correct allocation depends on task consequence, reversibility, observer coverage, agent behavior, human expertise, and available budget. “More oversight” is not automatically better: excessive interruption can add delay and error, while a lightweight verified control may dominate continuous trace reading. The benchmark question is whether a configured allocation policy produces justified decisions and acceptable consequences at a declared burden and loss—not whether a human was nominally in the loop.

## Comparison with adjacent reviewed evidence

- **Pista:** Pista provides operation-level semantic diffs and real-time/local intervention in a small bundled spreadsheet study. It reaches availability, exposure, self-reported inspectability, and attempted edits more directly than this interview paper, but lacks matched defects and realized correction. The present paper explains why such aids enter a broader allocation policy: participants may invest in co-planning and post-hoc review instead of monitoring. Pista cannot assume visibility will be used merely because it exists.
- **HANSEL:** HANSEL compresses long traces into interactive evidence pages and shows lower review burden with limited accuracy evidence. The interview study independently shows why users seek such compression—volume and cognitive distance—but its eyeballing heuristic makes omission risk salient. Both require an omission ledger, exposure events, calibrated accept/reject/correct/escalate outcomes, and severe-error loss.
- **Human-on-the-Bridge:** HOB places scarce human effort upstream in reusable trap, rubric, and recovery policy. This paper places user effort throughout work execution. Both are allocation hypotheses. HOB lacks demonstrated expert authority; the present heuristics lack correctness validation. Reuse or repeated practice scales errors as easily as expertise unless authority, observer validity, maintenance, and consequences are tested.
- **ArtifactCopilot:** ArtifactCopilot constructs phased evidence packets and records interventions, but a report can raise confidence without improving judgment. The present paper's plan/test/summary/diagram heuristics identify exactly the packet elements that need independent fidelity and completeness checks. Report production and human inspection must remain separate from supported adoption and decision correctness.
- **Measuring Agents in Production:** MAP surveys selected deployed/pilot teams and reports bounded workflows, human gates, sensitive context, delayed labels, and mixed evaluation. This study offers a finer-grained account of what selected experienced users say they do at those gates. Both are self-report evidence; neither audits realization or outcomes, estimates representative prevalence, or identifies practice efficacy.

Together these sources support a cross-domain distinction among **oversight policy**, **interface opportunity**, **actual human work**, **judgment/action**, and **consequence**. No source licenses collapsing them into “HITL,” counting human review as ground truth, or treating current developer heuristics as professional standards.

## Limitations and validity threats

1. The sample is only 17 participants and is purposively selected for frequent, experienced agent use.
2. Recruitment through professional contacts and snowballing favors connected and willing users.
3. Twelve participants work at the authors' large technology organization, creating organizational-culture and possible social-desirability dependence.
4. The five external participants are said to echo findings, but no cross-organization table or disconfirming analysis is reported.
5. Non-users, former users, failed adopters, restricted users, and resource-constrained workers are absent.
6. Most participants work in well-resourced firms with rich integrations, early features, and negligible token/compute constraints.
7. The study does not report the recruitment funnel, number screened, refusals, inaccessible candidates, or reasons beyond one secondary-screen exclusion.
8. Experience categories are self-defined and not linked to months, task counts, verified use, or competence.
9. Agent usage frequency and professional usage are self-report rather than telemetry.
10. Participants span different products, models, policies, permissions, organizations, tasks, and versions without configured-system records.
11. Interviews occurred in July–August 2025, but specific agent versions and practice valid times are absent.
12. Fifteen of 17 participants are men; geographic and organizational diversity is narrow.
13. The sample is not designed to estimate population frequencies or differences by role, experience, gender, company, agent, or task.
14. Interviews are retrospective self-report, not ethnographic observation despite “lived reality,” “in practice,” and “observed” wording.
15. No actual prompts, instruction files, plans, traces, diffs, code, tests, diagrams, corrections, incidents, or outcomes are analyzed.
16. Temporal anchoring in the interview guide partly induces the before/during/after taxonomy.
17. The guide uses governance, risks, evals, correctness, and deployment language that may cue oversight-rich accounts.
18. One first author conducted every interview and all open coding.
19. The second coder enters only at selective coding after open and axial codes were formed by the first author.
20. No independent coding agreement, codebook, coder matrix, audit trail, or residual-disagreement record is reported.
21. No reflexivity analysis addresses interviewer employment, organizational relationships, or expectations.
22. No saturation, information-power, analytic stopping, or “no new theme” criterion is reported.
23. No participant member checking, external peer debrief, or independent interpretation is reported.
24. No participant-by-theme matrix, prevalence counts, code frequencies, or negative-case table accompanies selected quotes.
25. “All,” “most,” “several,” “few,” and “rarely” cannot be reconstructed from coded records.
26. Similar practice among external participants is asserted without itemized evidence.
27. The four categories may overlap: custom instructions can encode co-planning; plan review can occur during execution; post-hoc repair becomes planning for the next run.
28. The categories are an organizing device, not demonstrated exhaustive or mutually exclusive natural kinds.
29. Small-task delegation is selected by participants and can jointly cause both low monitoring and easier review; the paper's monitoring explanation is not causal.
30. Participants' reported challenges cannot establish that less experienced users face worse versions without comparison.
31. The study does not identify whether oversight prevented an error, detected one, introduced one, or had no effect.
32. A priori controls are not tested for enforcement, attempted violations, bypass, or residual information flow.
33. Co-planning bundles human expertise, decomposition, solution selection, partial code, and agent work; no component or equal-burden comparator is observed.
34. Reasoning traces and action summaries are recognized as unreliable but never compared with authoritative state.
35. Run time, conversation length, and context size are reported warning cues with no sensitivity, specificity, threshold, or consequence analysis.
36. Stop/restart and re-prompt strategies have no matched outcome, cost, or state-preservation evidence.
37. Post-hoc review intensity is reported, not measured through exposure, defects, recall, false positives, or correction validity.
38. Re-review burden has no time, attention, iteration, latency, or lifecycle-cost estimate.
39. Plan fidelity is assumed by the participant heuristic and not tested against trace or state.
40. Test quality, requirement coverage, mutation strength, independence, environment, false accepts, and collateral obligations are unobserved.
41. Eyeballing and generated diagrams may omit or rationalize defects; no shared-error or omission test is conducted.
42. Cross-agent agreement is not independent when models share training, prompts, retrieval, or error modes.
43. Familiarity and domain competence are not measured, so epistemic deference cannot be calibrated.
44. No direct productivity, merge, quality, safety, security, privacy, compliance, learning, craftsmanship, or professional-identity outcome is measured.
45. The legal and organizational implications are interpretive; no high-risk AI setting, compliance audit, or governance decision is studied.
46. The paper's design recommendations are proposals derived from reports, not evaluated interfaces or demonstrated remedies.
47. No raw transcripts, de-identified excerpts corpus, coded data, analysis script, preregistration, or study package is released.
48. Confidentiality can justify restricted data but does not turn missing audit evidence into positive validity evidence.
49. The official publication page verifies metadata, not methodology or empirical records.
50. Transfer beyond selected software-agent power users remains a hypothesis requiring cross-domain validation.

## Reproducibility and operational realism

**Source inspectability is good for an interview paper.** The immutable 28-page paper reports eligibility, recruitment approach, organizational concentration, compensation, IRB status, interview timing and duration, three-stage coding, two concrete coding disputes, participant-level demographics/tool use, usage scenarios, the complete topic guide, and concise category definitions. These details allow a future team to approximate the instrument and understand how the taxonomy was produced.

**Analytic reproducibility is low.** The recruitment ledger, screener, recordings, transcripts, open codes, 13 axial codes, final codebook, coded matrix, theme counts, disagreement history, negative cases, and analysis materials are absent. Another analyst cannot reconstruct which statements produced each category, whether counts support “most” or “rarely,” or whether a different lens would retain the same boundaries.

**Operational realism is high for reported constraints but unverified for behavior.** Participants appear to be genuine frequent users discussing real professional work, legacy systems, prototypes, sensitive data, instructions, plans, tests, diffs, long contexts, and repeated repair. That is more ecologically informative than an artificial oversight puzzle. Yet no work episode is observed, no configured system is pinned, and no consequence is measured. The study supports situated authoring hypotheses—not production-operation, oversight-effect, reliability, safety, or readiness evidence.

## Transfer to skill-bench

### Retain

1. Represent oversight opportunities at configuration, co-planning, execution, and post-hoc review—not only final approval.
2. Treat task decomposition, plan drafting, seeded partial solutions, and custom instructions as configured interventions and human labor.
3. Preserve different human actions: constrain, specify, inspect, accept, reject, edit, pause, stop, restart, escalate, and defer.
4. Record domain/task familiarity and authority separately from generic “human reviewer” identity.
5. Capture re-review and restart burden across iterations rather than only first-pass review time.
6. Preserve the distinction between prototypes, bounded/reversible work, integrated legacy systems, and consequential production paths.
7. Treat practical satisficing as an empirical condition: people allocate limited attention, so benchmark protocols must measure what they actually inspect.

### Repair

8. For each oversight locus, record opportunity, available controls/evidence, exposure, actual inspection, judgment, action, uptake, state consequence, collateral effects, burden, and residual uncertainty.
9. Validate controls through attempted-violation and enforcement evidence; do not infer realization from configuration text.
10. Validate plans against trace and native pre/post state; include plan-adherent, plan-divergent, omitted-obligation, and unplanned-side-effect cases.
11. Type test suites by requirement authority, authorship, environment, coverage, mutation/adversarial evidence, independence, valid scope, and known omissions.
12. Treat summaries, rationales, diffs, and generated diagrams as transformed evidence views requiring fidelity, completeness, and omission testing.
13. Make warning signals such as time, turns, tokens, and repeated errors calibrated predictions with named targets and loss—not automatic intervention thresholds.
14. Distinguish human availability from exercise and effectiveness; “review required” is not evidence that review occurred or worked.
15. Include no-oversight, fixed-budget, alternative-allocation, and equal-total-burden conditions where causal attribution matters.
16. Report the complete human–agent package: human specification/review time, agent time/cost, restart/rework, downstream delay, quality, severe errors, and residual risk.
17. Use qualified independent reviewers and downstream recipients where the claim requires professional correctness or utility; familiarity-driven deference should trigger escalation tests.
18. Preserve task/participant/system clustering, missing opportunities, invalid evidence, and selective task delegation in the estimand.

### Test before adopting participant heuristics

- **Plan proxy:** identical frozen plans crossed with faithful execution, silent divergence, omitted requirement, and collateral mutation; measure inspection, detection, correction, confidence, and state loss.
- **Test proxy:** passing suites with complete selected predicates, missing boundary cases, shared agent/test misconception, security/performance blind spots, and environment mismatch.
- **Eyeballing:** full native evidence versus faithful summary versus omission-bearing or misleading summary under equal time; retain severe-error recall and false-alarm loss.
- **Unfamiliarity:** familiar versus unfamiliar domain and independent-expert availability; score appropriate accept, inspect, seek evidence, constrain, or escalate decisions.
- **Allocation:** hold total human time fixed while moving effort among pre-control, co-planning, monitoring, and post-hoc review on matched task families; measure endpoint quality, collateral state, residual risk, rework, and total lifecycle cost rather than assuming one universal allocation.
- **Cross-domain transport:** repeat the allocation study on at least one non-code artifact or workflow with different evidence views, authority, reversibility, and consequences before making a general knowledge-work claim.

## Concrete repository actions

- Added this full-text deep review with exact immutable source and official-metadata paths.
- Updated `data/papers/index.json` from acquired/review-pending to deep-review complete.
- Added the review to `papers/topic-index.md` under realistic knowledge work and oversight.
- Updated `docs/research-synthesis-index.md` because the paper materially extends the Pista/HANSEL interface evidence into a lifecycle allocation conclusion: reported oversight policy, interface opportunity, actual human work, judgment/action, and consequence are separate objects.
- **No new queue task added.** Existing configured-system, interaction, feedback/recovery, artifact/state, evidence-view, task-health, metric, participation/authority, reliability, cost, and validity machinery already provides homes for the requirements. The paper supplies nonduplicate validation cases and human-learning evidence, not a new schema.

## Assessment

- **Evidence tier:** B — full immutable primary paper and appendices read; official FAccT metadata verified; rich qualitative instrument disclosure; no study data, observed workflows, or outcomes.
- **Most reusable contribution:** oversight as effort distributed across pre-control, co-planning, monitoring, and review rather than one terminal human gate.
- **Strongest evidence:** selected experienced developers gave detailed, recurring accounts of configuration, specification/decomposition, light monitoring, intensive post-hoc review, and efficiency-oriented heuristics.
- **Most serious methodological limitation:** one-company-heavy retrospective intensity sample plus one-author interviewing/open coding and a temporally structured guide, without saturation, independent initial coding, negative-case ledger, or auditable coded records.
- **Most serious validity warning:** plans, tests, spot checks, generated explanations, and cross-agent agreement are treated by participants as efficient proxies precisely where their fidelity, completeness, and independence are unmeasured.
- **Safe claim:** among 17 purposively recruited experienced weekly software-agent users—12 at one large technology company—participants reported allocating oversight effort before, during, and after execution and using practical shortcuts to manage review burden. The study does not establish representative prevalence, an exhaustive taxonomy, heuristic correctness, causal oversight efficacy, productivity, safety, compliance, professional validity, production fitness, or readiness.
