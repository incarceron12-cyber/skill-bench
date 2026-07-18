# Cheap Code, Costly Judgment: a useful failure-to-control hypothesis without a released failure-to-outcome ledger

## Bottom line

Davis et al. offer a valuable process hypothesis for agent-mediated knowledge work: recurring failures should not merely be repaired or added to prose guidance; an authorized expert should decide whether they reveal a structural class and, when they do, convert that judgment into architecture or an enforceable control that changes subsequent work. The sharpest example is not “write better documentation.” It is to externalize the **relevance operator** that maps a planned change to the exact constraints governing it, then inject those constraints before action while retaining deterministic downstream gates. This separates available knowledge from contextually binding knowledge and is directly relevant to `skill-bench`.

The 12-week first-person case is rich enough to generate that theory, but not to test it. One author was the sole practitioner, primary note-taker, codebook lead, and central interpreter. The 88 episode-bounded notes were incidents the Subject considered salient, not a denominator of all agent episodes or failures. The private product repository, 137,000-word note corpus, coded incident table, analytic memos, agent transcripts, deployment records, and accessibility outcomes are not released. Only 10 incidents were independently re-coded, with unexplained 10-versus-7 denominators, no chance-corrected agreement, and disagreements resolved as boundary cases by the author team. The paper describes only two linked incidents from the 55 architecture/control incidents and provides no row-level chain from failure occurrence through interpretation, intervention, verification, recurrence, later throughput, and product consequence.

Repository scale is evidence of activity and a large governance substrate, not evidence that governance caused sustainable productivity, maintainability, accessibility, or production reliability. The reported 18,662 commits, 420 KLOC of production code, and 1.16 MLOC of tests/lints/documentation/tooling have no non-agentic or less-governed baseline, independence unit, defect denominator, code-survival measure, maintenance observation, or recipient outcome. “No defects observed under the project’s checks” is circular when those checks are the proposed treatment. The `$60K` accounting is useful but lacks a conventional-work baseline and omits the health cost the paper itself reports.

The paper-linked release is inspectable and internally valid as a **53-pattern catalogue and starter kit** at pinned pre-v2 commit `e9088ba5f6f1db81eac547bdcf0f26703d6807a6`; its validator passes all 53 entries. It is not the private DocAble product, repository history, complete field notes, or paper’s exact 41-mechanism/10-family empirical catalogue. Its entries explain portable intent, failure classes, prerequisites, costs, and known-use abstractions, but generally replace product paths with role-shaped descriptions. That improves transferability while severing the evidence needed to verify when each mechanism arose, which incidents motivated it, whether it was actually installed, whether failures recurred, and what changed afterward.

The warranted conclusion is therefore narrow: **one highly experienced engineer produced a plausible, source-inspectable middle-range theory and a reusable pattern catalogue from a sustained agentic build; the available evidence does not establish governance conversion as the cause of velocity, quality, maintainability, professional accessibility, or cross-project transfer.** For `skill-bench`, the contribution should become a testable event lineage, not a mandate to build a “tower of governance.”

## Source and reading record

### Complete immutable primary source read

- James C. Davis, Paschal C. Amusuo, Tanmay Singla, Berk Çakar, and Kirsten A. Davis, *Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering*.
- Immutable record: <https://arxiv.org/abs/2607.01087v2>; PDF: <https://arxiv.org/pdf/2607.01087v2>.
- Local PDF: `data/papers/pdfs/2607.01087v2-cheap-code-costly-judgment.pdf` (13 pages; 442,758 bytes; SHA-256 `1e6a290bbe174c368dee1a394dc446a0a7241c4294f960d92afaef8a9b5c8215`).
- Local full text: `data/papers/text/2607.01087v2-cheap-code-costly-judgment.txt` (102,629 characters; SHA-256 `1093684e9b91cc5999af83a8b0e64d48dbcaf31080ceeb8dcdb0260bc71e0aae`).
- Official source archive: `data/papers/source/2607.01087v2-source.tar.gz` (SHA-256 `a0b7184c26d8a70f8b983e431fb5ba6c7f581762faaec28656e1c72912c22719`); extracted at `data/papers/source/2607.01087v2/`.
- Metadata and version history: `data/papers/source/2607.01087v2-metadata.xml` and `data/papers/source/2607.01087v2-abs.html`. V1 was submitted 1 July 2026; v2 was submitted 4 July 2026. The acquired summary contains no withdrawal notice.
- I read the complete paper, figures, tables, threats, ethics statement, references, and principal TeX/data macros. The source records 137,000 words of field notes, although the final paper reports the 88 episode-bounded entries rather than exposing or analyzing that word count as a denominator (`data/data.tex`, lines 8–11).

### Official paper-linked release audited

- Release site named by the paper (p. 10, §X): <https://davisjam.github.io/agent-governance-mechanisms/index.html>.
- Official repository: <https://github.com/davisjam/agent-governance-mechanisms>.
- Pinned paper-time commit: [`e9088ba5f6f1db81eac547bdcf0f26703d6807a6`](https://github.com/davisjam/agent-governance-mechanisms/commit/e9088ba5f6f1db81eac547bdcf0f26703d6807a6), committed 4 July 2026 at 02:56:44 UTC, before v2 submission.
- Snapshot: `data/sources/releases/2607.01087v2-agent-governance-mechanisms/agent-governance-mechanisms-e9088ba5f6f1.tar.gz` (SHA-256 `714b47b3951b0c284fb68716bec0ae161a05d6f2a69d4a84af1e3b5101a3f8a6`).
- Extracted tree and provenance: `data/sources/releases/2607.01087v2-agent-governance-mechanisms/repository/` and `data/sources/releases/2607.01087v2-agent-governance-mechanisms/provenance.json`.
- Acquisition reports 236 tree entries, 201 blobs, 1,560,547 uncompressed file bytes, no GitHub release, and a top-level MIT license.
- I inspected the README, complete 53-row census, abstraction glossary, catalogue authoring rules, dynamic-context and component-zone entries, portable Skill, starter material, and representative agent/model/product patterns. I ran `python3 catalog.py validate`: it validated 53 entries—22 agent, 11 models-bridge, and 20 product—with zero issues.

The release boundary is crucial. The public tree is a pattern catalogue and starter kit. It is neither the private accessibility-remediation product repository nor the 88-note corpus. It supports catalogue structure and portable mechanism descriptions, not independent reproduction of the case, its chronology, repository counts, accessibility claims, or theory.

## One-sentence contribution

The paper turns a practitioner’s recurring move—interpret a repeated agent failure as a missing abstraction or guardrail, then encode that judgment into the environment—into a falsifiable five-stage process theory, while the release turns many resulting mechanisms into portable design patterns but omits the incident-to-intervention-to-outcome evidence needed to test the theory.

## Why this matters for skill-bench

This review advances charter objectives A, B, C, and E through bounded expansion into a general expertise-transfer question: **how can situated expert judgment discovered during work become durable, inspectable machinery without being mistaken for validated universal procedure?** Software engineering is the mechanism case, not a scope commitment.

The concrete evidence is a complete immutable-paper/source audit, inspection and validation of the pinned official catalogue, reconstruction of the field-study and coding process, and a claim-boundary analysis. The uncertainty clarified is whether governance conversion is observed expertise transfer or a retrospective theory over selected activity. The answer is mixed: the paper identifies a compelling candidate transformation, and the catalogue exposes its proposed outputs, but there is no released lineage proving that the transformations were correctly inferred, installed, effective, or transferable.

The reusable benchmark object is not a list of controls. It is a challengeable chain:

```text
eligible work episode
→ observed failure and consequence
→ recurrence/class evidence
→ expert local-versus-structural interpretation
→ candidate architecture/control and authority
→ installed version and enforcement path
→ mechanism-level conformance test
→ later opportunities for recurrence
→ recurrence / counterexample / collateral burden
→ artifact, recipient, and operational consequence
→ retain / revise / retire decision
```

No arrow should inherit the validity of its predecessor. A salient incident does not prove a class; a class interpretation does not prove the proposed mechanism fits; a passing mechanism test does not prove product quality; fewer detected recurrences can reflect lower exposure or observer blindness; a large governance substrate does not prove net value.

Classification: narrow expansion with direct validation implications. Useful completion is this source-grounded review and a nonduplicative mapping into existing trace, compounding-lesson, task-health, metric, validity, participation, and configured-system machinery. No new schema task is needed.

## Research question and claim boundary

The paper asks: **“Through what process can high-velocity agentic implementation be converted into governable progress?”** (§III-A, p. 3). Its answer is the “cheap-code, costly-judgment” loop:

1. velocity exposes ambiguity, drift, weak boundaries, and missing oracles;
2. the human architect distinguishes a local defect from a recurring structural failure class;
3. judgment is converted into soft governance or deterministic architecture/control;
4. later agents inherit a narrower, more explicit action space; and
5. repeated conversion increases the environment’s capacity to absorb future agent work (Fig. 4, p. 8).

This is appropriately framed as candidate middle-range theory and accompanied by future propositions rather than estimated effects. The paper nevertheless sometimes moves from theory-building language to stronger statements: that quality was sustained without implementation inspection, mechanisms enforce quality, agentic velocity can be sustained, and the product was deployed at agentic speed. Those statements exceed the disclosed observations because product correctness, maintenance, accessibility, escaped defects, recurrence, and comparative velocity are not measured independently.

The release strengthens the claim that a substantial, coherent pattern representation exists. It does not establish that the pattern catalogue is the exact empirical codebook, that all entries were induced during the 12 weeks, or that the patterns caused any reported outcome.

## Methodology and system

### Case boundary and practitioner

The bounded case is one expert software engineer’s 12-week primary work activity on a greenfield document-accessibility remediation system (§§III–IV, pp. 3–5). The Subject is a paper author and software-engineering professor with 16 years of professional/academic engineering experience and approximately 100,000 lines of pre-GenAI coding experience. He controlled goals, acceptance criteria, architecture, validation, and deployment. Claude implemented through the “Claude for VSCode” chat interface; the Subject reports inspecting almost no agent-produced code (§IV-B, p. 5).

The case has meaningful real-world pressures: a regulatory deadline, mixed Office/PDF inputs, syntactic and semantic WCAG obligations, preservation/auditability needs, an immature remediation tool ecosystem, SaaS deployment, and users from multiple institutions (§IV-A/B, pp. 4–5). Development proceeded through feasibility, PowerPoint prototype, format expansion, SaaS, standards conformance, and hardening stages. Users reportedly exposed semantic-equivalence failures that external checkers missed.

Configured-system identity is insufficient for comparative inference. “Claude,” “Claude for VSCode,” “Sonnet,” and “Opus” do not pin exact model versions, endpoint revisions, context limits, settings, system instructions, tools, prompts, conversation reset, retry policy, or assignment procedure. Four Max 20x accounts were saturated, with estimated weekly token use inferred from an external issue rather than provider receipts. No agent-task or transcript ledger is released.

### Data sources and incident construction

The empirical record has two stated sources (§III-C, p. 3):

- 88 contemporaneous episode-bounded field notes; and
- 18,662 repository commits plus approximately 1.6 million lines of “active artifacts.”

Each recorded episode became a critical incident. Analytic memos captured triggering condition, inputs, Subject interpretation, engineering response, observed outcome, and apparent later effect. This is exactly the right conceptual shape for a governance-conversion ledger.

But incident construction is outcome- and salience-conditioned: an episode enters the corpus because the Subject judged it salient enough to record. The paper does not disclose all delegated tasks, agent runs, failures, repairs, accepted changes, silent successes, failed proposed controls, reverted mechanisms, or days with no note. Therefore 35 control incidents and 20 architecture incidents are distributions **within selected notes**, not prevalence among work episodes or failures. There is no way to estimate selection sensitivity or compare converted versus unconverted failures.

The repository is a different representation, not fully independent evidence. It can corroborate that files/commits changed, but the same Subject and agents generated those artifacts; the authors selected which commits “underpinned” themes; and neither commit locators nor the private tree are released. Repository presence cannot independently validate the Subject’s rationale, a control’s enforcement, correct classification, or downstream effect.

### Codebook development and reflexivity

The Subject led 11 codebook iterations. LLMs normalized notes, compared incidents with candidate codebooks, suggested themes, and found repository evidence, while the author team retained interpretive authority (§III-C, p. 3). The final corpus has three first-level classes and nested categories; 72/88 incidents are engineering reflections, including controls (35), architecture (20), economics (8), conceptual framing (7), and AI capability (2) (Table I, p. 6).

A second author independently re-coded a stratified sample of 10 incidents from the codebook without the Subject’s labels. Reported agreement is 10/10 on incident class, 6/7 on category, and 5/7 on the third layer; all 10 summaries were judged supported (§III-C, p. 3). This is a useful check but weak reliability evidence:

- the sampling strata and randomization are not specified;
- only 10/88 incidents were checked;
- the denominator falls from 10 to 7 without explanation in the paper;
- no independent coding of all candidate episodes, mechanism mappings, temporal effects, or negative cases occurred;
- no chance-corrected or prevalence-adjusted agreement is reported;
- the same author team judged disagreements “boundary cases rather than errors”; and
- codebook versions, instructions, labels, disagreements, adjudication, and memos are unavailable.

Reflexivity consisted partly of four talks over six weeks. The Subject repeatedly articulated intuitions to institutional, research, and teaching audiences, but audience response was “uncritical,” so the talks offered articulation rather than external challenge (§III-C, p. 4). This may improve construct explicitness while also allowing an emerging theory to shape later note salience and interpretation. The paper does not separate contemporaneous observation, contemporaneous interpretation, post-talk reframing, and retrospective coding.

### Two detailed conversion episodes

The strongest empirical material is two linked examples (§V-B, p. 6).

**Component/zone model.** Whole-repository agent audits of architectural boundaries became expensive, nondeterministic, and too large for context. The Subject interpreted accumulating drift as a representation problem, created typed component/zone objects with filesystem scope, boundary type, and checks, then progressively replaced audit crews with static/dynamic analyses. The release’s `component-zone-model.md` describes a typed ownership/seam registry, reverse mapping, and consumers, with the important warning that a wrong centralized model misroutes every consumer.

**Dynamic context injection.** Agents lacked tacit knowledge of which constraints governed target files and spent time discovering violations after changes. The Subject created a file-to-constraint slicing mechanism and injected applicable constraints into the brief before editing. The release carefully distinguishes advisory forward injection from hard downstream gates and names over-injection, under-injection, registry drift, and adapter maintenance as failure surfaces (`agent/context-and-dispatch/dynamic-context-injection.md`).

These examples make the proposed mechanism plausible. They do not provide dates, exact triggering runs, first and repeated failures, affected tasks, before/after violation rates, precision/recall of the mapping, token/time savings, false constraints, later recurrences, collateral failures, or independent artifact outcomes. The May 28 note excerpt says meta-coding “saved about a day,” but no baseline or timing method substantiates that estimate.

### Governance repertoire and release mismatch

The paper reports 41 representative mechanisms across 10 families: five agent-governance and five product-governance families (Table II, p. 7). It reports one 14-mechanism stack around orchestrator/sub-agent failures and a support apparatus comprising 238 KLOC of lints, 405 KLOC of tests, 247 KLOC of agent-referenced documentation, 110 KLOC of agent infrastructure, and 162 KLOC of tools.

The pinned release validates **53 mechanisms across 11 families and three roles**: 22 agent, 11 models-bridge, and 20 product entries (`INDEX.md`). This is not necessarily a contradiction—the public catalogue may elaborate or split paper mechanisms—but no crosswalk identifies which 41 correspond to which 53, which entries were in the empirical codebook, or which were added/reframed for publication. The repository was created 2 July, after v1 submission and two days before v2; it is a publication artifact, not a contemporaneous 12-week record.

The release’s authoring rule is strong: a mechanism must kill a recurring class, be distinct, and use real examples. Yet the portable catalogue intentionally removes private paths and mostly names abstractions such as a component registry, dispatch tool, event bus, or lint runner. “Known uses” demonstrate intended shape, not inspectable occurrence, chronology, or efficacy. Catalogue validity and case-study validity must remain separate.

## Evidence and claim audit

### What the evidence supports

1. A sustained first-person agent-mediated development case occurred, according to the immutable paper and source.
2. The Subject maintained 88 selected contemporaneous notes and the team built an 11-iteration qualitative codebook.
3. The selected corpus is dominated by interpreted controls and architecture.
4. The paper gives two concrete, coherent failure-to-mechanism narratives.
5. The TeX source contains detailed, internally reconcilable definitions for many reported code/support counts.
6. A public, internally validated, portable 53-entry mechanism catalogue exists at a pinned paper-time commit.
7. The authors state falsifiable future propositions and acknowledge N=1, construct, reflexivity, external-validity, and health limitations.

### What repository scale cannot establish

The source macros define 422,455 production lines and 1,161,688 support-apparatus lines, yielding the reported 2.75× ratio. They also distinguish tests, lints, load-bearing documentation, tooling, and infrastructure (`data/data.tex`, lines 74–113). This precision makes the count semantics more inspectable than many production reports.

But lines and commits remain activity measures. They do not show:

- what proportion was agent-generated, duplicated, generated, dead, or later removed;
- semantic complexity or independent task size;
- commit independence under hundreds of small agent commits;
- defect density, escaped defects, security, performance, reliability, or maintainability;
- control correctness, false-positive burden, bypasses, and repair cost;
- whether governance caused the volume or the volume induced governance;
- whether a smaller system would have delivered equal or better user value; or
- whether code/support growth is net benefit rather than governance overhead.

The release itself warns that every mechanism taxes future changes and context and may create “a tower of governance nobody wants” (`README.md`, lines 34–43). The paper provides no net-value estimator to show its own apparatus stayed below that threshold.

### Product and accessibility outcomes

The system reportedly processes Office and PDF files, passes or substantially improves accessibility checks, handles one course deck in about 60 seconds for roughly `$1`, and was used by at least one colleague with minimal concerns (§IV-B, p. 5). Users also reported outputs that passed checkers while losing semantic equivalence. This is valuable operational failure evidence.

There is no disclosed:

- document/user/institution denominator;
- input distribution or severity;
- independently validated before/after WCAG compliance;
- accessibility-professional or disabled-user evaluation;
- semantic-fidelity error rate;
- corruption, regression, or harmful-remediation rate;
- uptime, incident, rollback, privacy, security, or support record;
- recipient correction/rejection burden;
- longitudinal maintenance evidence; or
- comparison with manual/commercial remediation.

“Production,” “deployed,” and checker improvement describe environment state and intended use, not demonstrated professional efficacy. In a domain where the paper itself says accessibility is underspecified and checker passage can miss semantic loss, deterministic internal controls cannot serve as the sole outcome observer.

### Cost and comparative productivity

The reported `$60K` consists of `$50K` Subject salary, `$2K` OpenAI/Vertex inference, `$6K` Google Cloud hosting, and `$2K` Claude subscriptions (§IV-B, p. 5). This usefully resists the fiction that agent work costs only tokens.

Still missing are working hours, overtime, task-level cost allocation, failed/repeated calls, infrastructure amortization, collaborator/user time, downstream correction, and a matched conventional or less-governed baseline. The ethics section reports obsessive tool use, degraded attention to relationships, physical strain, and prolonged work (p. 10). Those are real labor and safety consequences, not peripheral anecdotes. A productivity claim that excludes them is incomplete.

The two subsequent 50 KLOC and 36 KLOC projects allegedly made faster initial progress after carrying governance lessons forward (§VII-B, p. 9). No task scope, chronology, baseline, controls, quality, or outcomes are reported. This is a transfer anecdote, not evidence that the catalogue generalizes.

### Testable propositions are not tested here

The paper’s four future questions are valuable:

- does higher velocity reduce time to surface structural classes?
- do soft/review controls saturate as velocity rises?
- does deterministic conversion sustain velocity?
- do human judgment and authority moderate outcomes?

The case supplies no varied velocity condition, review-centered comparator, non-conversion arm, fixed agent capability, divided-authority case, escaped-defect series, or structural-fix lag analysis. Control accumulation and ongoing activity are compatible with the theory but also with reverse causality, maturation, increased requirements, one expert’s preferences, and outcome-conditioned documentation. The propositions remain hypotheses.

## Unique insight

### Tacit expertise includes relevance and conversion operators, not only rules

The paper’s deepest transferable idea is that tacit expertise is not exhausted by writing down “the rules.” An expert also knows:

- which rule applies to this state and planned action;
- whether an observed defect is local or class-level;
- which representation makes the class impossible;
- when advisory guidance needs deterministic enforcement;
- whether a failed mechanism needs a complement, revision, or retirement; and
- whether the expected benefit justifies its future burden.

Dynamic context injection captures the first operator as `target files → applicable constraints`; governance conversion captures the second and third as `failure evidence → structural class → intervention shape`. These are expertise-to-evaluation primitives. A benchmark that gives an agent all rules in one giant Skill tests recall under a flooded context, not contextual judgment. A stronger task presents incomplete, changing evidence and asks the configured system to select applicable constraints, classify recurrence, propose the smallest sound intervention, preserve alternatives, and verify later consequences.

### Externalization is an intervention, not proof of transfer

Turning judgment into a typed model, lint, gate, Skill, or catalogue entry changes the system. It may improve work, overfit one failure, hide a symptom, create false positives, narrow legitimate alternatives, or shift burden elsewhere. The public pattern text preserves author interpretation; it does not prove another engineer or domain agent will apply the pattern correctly.

For `skill-bench`, expertise transfer should therefore have at least four independently evaluated objects:

1. **interpretation fidelity:** was the failure class and context boundary correctly inferred?
2. **mechanism conformance:** was the proposed/installed mechanism implemented and enforced as specified?
3. **counterfactual efficacy:** on eligible future opportunities, did it reduce the intended class relative to a matched alternative?
4. **net professional consequence:** did artifact quality, recipient outcome, safety, time, and maintenance improve without unacceptable false blocks or governance burden?

### Negative and unconverted cases are essential

A governance benchmark built only from successful conversions would teach the evaluator the theory it is meant to test. It needs:

- one-off bugs where a new control is over-engineering;
- apparent recurrence with distinct root causes;
- structural classes best solved by changing requirements rather than adding a gate;
- controls that suppress valid alternatives;
- architecture that centralizes a wrong assumption;
- recurrence after installation;
- nonrecurrence because exposure disappeared;
- soft guidance that is sufficient at low volume;
- failed or reverted controls; and
- divided-authority situations where the correct artifact is an escalation/handoff rather than unilateral change.

That last point links expertise with organizational authority. Correct judgment without authority cannot produce system change; authority without independent challenge can institutionalize one person’s mistake.

## Comparison with adjacent reviewed evidence

### Production-agent-systems map

`docs/production-agent-systems.md` already preserves `source → extraction → review → implication → implementation → verified artifact` and `task → environment → trace → artifact/state → grader → diagnosis`. Governance conversion adds a missing middle transition: a diagnosed recurrence can produce a **versioned change to the work environment**, which must then be evaluated on later opportunities. It does not overturn the map or justify process optimization for its own sake. It refines “verified artifact” into installation conformance plus subsequent effect and burden.

Anthropic/Amazon production-evaluation reviews already require task/trial/grader/trace identity, task health, operational metrics, and failure attribution. This paper adds firsthand qualitative evidence about **control discovery**, not measured production efficacy. The sources are complementary: production-eval guidance describes how to monitor systems; this case hypothesizes how expert interpretation converts monitored failures into architecture and controls. Neither independently validates professional construct coverage.

### Domain-expert participation ethnography

The participation ethnography (`papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md`) shows expert authority decaying through developer, synthetic, and model-judge transformations. This case has the inverse concentration: the Subject holds practitioner, architect, note-taker, mechanism-author, analyst, and much decision authority. That preserves situated rationale but reduces independent challenge and makes approval tautological.

Together they imply that governance conversion needs **authority lineage without authority inheritance**. A practitioner can author an interpretation and mechanism; a separate reviewer should test evidence support, another observer should verify implementation, and later trials should establish effect. A public catalogue derived by its originating expert remains expert-authored, not externally expert-approved or empirically validated.

### Existing compounding and validity machinery

The repository’s compounding-lesson contract already represents candidate lessons, evidence locators, authority, contradiction/supersession, held-out validation, downstream dependencies, and rollback. Task-health, metric-monitoring, configured-system, trace, participation, and validity-argument contracts cover adjacent boundaries. Governance-conversion evidence can be represented as a typed candidate lesson whose proposed action is an environment component change, linked to later trials and validity claims. A new standalone governance schema would duplicate those objects before real data exercises them.

## Reproducibility and operational realism

**Manuscript inspectability: moderate.** The immutable v2 paper gives the research question, case boundary, six development stages, Subject background, costs, selected incident counts, codebook process, partial recoding, two conversion examples, mechanism families, source-size definitions, propositions, threats, and ethics. The TeX source clarifies line-count categories and hidden macro values. It does not expose the corpus or analysis chain.

**Qualitative reproducibility: weak.** The 88 notes, 137,000-word corpus, analytic memos, codebook versions, full coded table, LLM-analysis prompts/outputs, stratified sample rule, second-author labels, disagreements, incident-to-commit links, negative cases, and chronology are unavailable. Another team could imitate the method but could not reproduce the themes or test saturation/selection.

**Engineering reproduction: blocked.** The private product repository, 18,662-commit history, exact cloc scripts/inputs, agent transcripts/configuration, deployment data, validation artifacts, accessibility measurements, and outcome ledgers are absent from the paper-linked release. The code/support totals and mechanism installation cannot be independently replayed.

**Catalogue reproducibility: strong for structure, weak for empirical lineage.** The pinned public catalogue is complete, licensed, readable, and validates with its stdlib tool. It supports navigation and adaptation. It does not preserve the paper’s exact 41-to-53 crosswalk, incident evidence, product code, enforcement checks, or outcome measurements.

**Operational realism: high for pressures, low for outcome verification.** The case includes deadline shifts, weak tooling, semantic requirements, users, cloud deployment, concurrent agents, context loss, shared-resource contention, staged gates, architecture drift, governance overhead, and worker health harm. Those are realistic hidden states. The observation is nonetheless one extraordinary expert, one toolchain, one greenfield product, one institution-centered context, and no conventional team or divided authority.

**Causal inference: very weak.** There is no treatment assignment, comparator, time-series effect model, independent endpoint, or denominator of opportunities. The case is suitable for generating constructs and candidate mechanisms, not estimating whether governance sustains velocity or quality.

## Limitations and validity threats

### Sampling, selection, and chronology

1. The 88 notes are Subject-selected salient episodes, not all tasks, failures, or decisions.
2. No eligible-episode denominator permits prevalence or conversion-rate estimates.
3. Note frequency, missing days, revisions, and timing relative to talks are undisclosed.
4. No protocol actively searches for disconfirming, failed, reverted, or unnecessary controls.
5. Only two of 55 control/architecture incidents are described in depth.
6. The paper does not release installation dates, first recurrence, exposure counts, or post-control recurrence windows.
7. “Compounding” can reflect project maturation, changing requirements, or survivorship rather than causal control value.

### Reflexivity and qualitative reliability

8. The Subject is practitioner, participant, note author, primary codebook developer, and theory source.
9. LLM-assisted normalization/theme/corroboration may reinforce candidate codebooks; prompts and outputs are absent.
10. Eleven iterations indicate active construct formation but no frozen chronology shows when categories stabilized.
11. Independent recoding covers only 10 incidents; category and third-layer denominators drop to seven without explanation.
12. No chance-corrected agreement, confidence interval, independent adjudicator, or member/peer challenge is reported.
13. Four talks produced articulation but explicitly uncritical external response.
14. Repository corroboration is not independent of the Subject/agents and lacks released locators.

### Configured system and exposure

15. Exact Claude/Sonnet/Opus models, versions, prompts, tools, policies, retries, and context are unpinned.
16. Agent tasks, attempts, failures, acceptances, silent successes, and model receipts are unavailable.
17. Estimated token use comes from opaque subscriptions and an external estimate.
18. Agent capability, project complexity, concurrency, and governance all change over time.
19. No lower-velocity, oversight-centric, soft-control, or no-conversion comparator exists.
20. The Subject’s broad authority is constitutive of the case and may not transfer to teams.

### Mechanism and outcome identification

21. A salient failure does not prove a recurrent structural class.
22. An installed artifact does not prove enforcement or correct scope.
23. A passing internal check may share assumptions with the mechanism under test.
24. Fewer observed failures can reflect reduced exposure, changed instrumentation, suppression, or observer blindness.
25. No mechanism-level precision/recall, false-positive burden, bypass rate, or maintenance cost is reported.
26. “No defects observed under project checks” is not independent defect evidence.
27. The 14-layer defense stack may indicate prudent depth, duplicated controls, or unresolved root causes; no marginal ablation distinguishes them.
28. Support-apparatus size is neither quality nor net value.
29. Subsequent-project transfer is anecdotal and measured only as claimed faster initial progress.

### Product, professional, and production validity

30. Accessibility-check improvement is not semantic accessibility or equal effectiveness.
31. Users explicitly found checker-passing semantic-equivalence loss.
32. No disabled-user, accessibility-expert, or independent professional outcome study is reported.
33. User/document/institution denominators and error severities are absent.
34. No security, privacy, uptime, incident, rollback, correction, or maintenance series is disclosed.
35. One `$1`/60-second deck observation does not establish population cost or quality.
36. “Production” and “deployed” are state descriptions, not readiness or beneficial-use evidence.

### Cost, labor, and ethics

37. `$60K` has no matched baseline, task allocation, labor-hour denominator, or complete downstream burden.
38. Hosting, subscriptions, inference, and salary are rounded; retry and failed-work costs are unavailable.
39. Obsessive use, physical strain, and relationship harm are reported but excluded from productivity accounting.
40. An extreme work pattern can create apparent calendar velocity that is neither safe nor sustainable.

### Release and transfer

41. The release has 53 mechanisms/11 families versus the paper’s 41/10, without a crosswalk.
42. The repository was created after v1 and is a publication catalogue, not contemporaneous case evidence.
43. Portable descriptions intentionally omit private implementation and incident locators.
44. Catalogue validation checks schema/link consistency, not mechanism efficacy.
45. Mechanisms tailored to one high-intensity operation can over-govern smaller or unlike workflows.
46. Software patterns do not automatically transfer to research, finance, healthcare, office work, or other professional artifacts.
47. Current agents may help suggest controls after seeing examples, complicating the paper’s human-only judgment boundary over time.

## Transfer to skill-bench

### Retain

1. **Failure-to-conversion as a longitudinal benchmark object.** Preserve observed episode, class hypothesis, intervention, installation, later opportunity, recurrence, and consequence as distinct records.
2. **Architecture versus control.** Ask whether a state can be made unrepresentable or must be detected, and preserve mixed/soft/hard enforcement rather than calling prose a guardrail.
3. **Contextual relevance operators.** Evaluate selection of applicable constraints from scope/state, not only recall of a full rule list.
4. **Authority as a condition.** Record who may propose, install, override, approve, and retire environment changes; make escalation a valid action when authority is absent.
5. **Counterexamples and retirement.** Require evidence for one-off status, failed conversions, false blocks, legitimate alternatives, changed exposure, contradiction, supersession, and rollback.
6. **Net governed throughput.** Keep output quality, recurrence, false-positive burden, human judgment time, agent cost, maintenance, safety, and recipient consequence separate.
7. **Descriptive pattern catalogue.** Pattern cards that name intent, failure class, prerequisites, enforcement, costs, known uses, and adjacent mechanisms are useful authoring aids if their evidence status remains explicit.

### Repair before reuse

8. Define the eligible episode/opportunity population before selecting incidents.
9. Preserve contemporaneous observation separately from practitioner interpretation and retrospective theory coding.
10. Require at least one independent interpretation or explicit disagreement for high-consequence classes.
11. Bind class claims to multiple occurrences or a defensible structural-certainty argument; do not manufacture controls for isolated defects.
12. Version the configured agent, environment, mechanism, observers, and exposure state at every comparison.
13. Verify enforcement with planted conformance cases, then test efficacy on held-out natural/counterfactual opportunities.
14. Use an independent professional endpoint; never let the installed checker be the only evidence that the checked product is good.
15. Report negative space: successful ungoverned work, failures not converted, proposed controls rejected, controls removed, and recurrence despite controls.
16. Charge full costs, including attention, review, maintenance, false blocks, infrastructure, correction, and health/safety burden.
17. Prevent catalogue authorship from inheriting empirical-validation or cross-domain authority.

### Cross-domain pilot design

Use two unlike work shapes—for example, an evidence-based memo/source pack and a structured spreadsheet/workspace artifact—to test the general hypothesis without turning `skill-bench` into a coding benchmark. For each shape:

- plant repeated and superficially similar-but-distinct failure episodes;
- include one genuine one-off where creating a control is over-engineering;
- vary whether the actor has authority to change the environment;
- compare local repair, soft guidance, deterministic control, and architecture where legitimate;
- freeze independent endpoint checks before the conversion proposal;
- expose later eligible opportunities plus one distribution shift and one legitimate exception;
- score classification, intervention fit, conformance, recurrence, collateral restriction, artifact quality, human burden, and cost separately; and
- preserve whether the mechanism should be retained, narrowed, complemented, or retired.

The claim would be bounded to whether a configured system can perform and justify governance conversion under authored calibration cases. Professional or production generality would still require real expert and operational validation.

## Claim ledger

| Claim | Status after full-paper/source/release audit |
|---|---|
| A 12-week first-person case and 88 selected contemporaneous notes are reported | Supported by immutable paper/source; corpus unreleased |
| Repository had 18,662 commits, 420 KLOC product, and 1.16 MLOC support | Author-reported with detailed source macros; private repository/count replay unavailable |
| Selected incidents often concern architecture/control | Supported within the selected corpus; not a prevalence estimate |
| Codebook is independently reliable | Weak bounded check only: 10 incidents, unexplained 7-case nested denominators, no released labels/adjudication |
| Failures caused the reported governance mechanisms | Plausible from two narratives; full lineage unavailable |
| Governance mechanisms reduced recurrence | Not measured |
| Governance sustained velocity | Not tested against a comparator or valid longitudinal estimand |
| Governance sustained software quality/maintainability | Not established |
| The system improved professional accessibility | Not established; checker-passing semantic failures were observed |
| The system was deployed/used | Author-reported bounded operational state; no production reliability or benefit study |
| `$60K` is complete comparative development cost | Rejected; useful partial accounting without baseline/full burden |
| Judgment was transferred into context/architecture/control artifacts | Supported as practitioner interpretation and catalogue representation; fidelity/effect not independently validated |
| Public catalogue reproduces the case | Rejected; it is a 53-pattern starter catalogue, not the private product/history/notes |
| Public catalogue is internally inspectable | Supported; pinned 53-entry validator passes |
| Catalogue mechanisms generalize across teams/domains | Not tested |
| Four theoretical propositions are supported | Grounded as hypotheses, not tested |
| Governance conversion is a useful benchmark hypothesis | Supported as a design hypothesis with explicit validation requirements |

## Concrete repository actions

- [x] Read the complete immutable v2 PDF/text, official source, metadata, and v1/v2 history.
- [x] Audited and locally validated the official pinned pre-v2 53-entry catalogue and Skill.
- [x] Reconstructed case boundary, incident construction, codebook, partial recoding, two conversion examples, cost, mechanism counts, theory, threats, and ethics.
- [x] Separated paper claims, TeX count definitions, catalogue evidence, and unavailable private case artifacts.
- [x] Compared nonduplicatively with the production-agent-systems map and domain-expert participation ethnography.
- [x] Derived a cross-domain failure-to-conversion lineage and strict claim ceilings.
- [x] Added no queue task. Existing compounding-lesson, task-health, trace/configuration, metric-monitoring, participation, and validity machinery can represent the proposed lineage; a new governance subsystem would duplicate those contracts before real evidence exercises them.
