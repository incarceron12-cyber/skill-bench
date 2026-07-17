# CentaurEval: a human–AI pass-rate contrast is not yet a collaboration-necessity or complementarity estimate

## Bottom line

CentaurEval makes a valuable methodological move: it evaluates 45 real participants both without and with a contemporary coding agent, uses executable hidden tests, retains interaction logs, and explicitly tries to create tasks on which human judgment and machine implementation capacity are complementary. Its 45-template bank, dynamic human task generator, 450-instance static model set, standardized cloud IDE, four configured conditions, participant materials, and direct cost disclosure form a more substantial human–agent evaluation package than simulator-only collaboration benchmarks.

The central claim nevertheless exceeds the design. The template admission test establishes **low autonomous-model success on selected generated instances**; it does not test unaided humans or human–AI teams. The main human contrast uses 90 dynamic trials per condition, while autonomous conditions use a different static set of 450 instances, a Docker controller, automated retries, visible-test feedback, and in `C1` researcher repairs. Human-only and human–AI participants solve different dynamically instantiated tasks rather than the same frozen instance, and the paper does not release the assignment matrix, task identities, instance-equivalence evidence, participant rows, interventions, traces, graders, or analysis code. The reported `18.89% → 31.11%` paired contrast is consistent with 17 versus 28 passes across 90 trials, but the paper does not expose the participant-level signs or define the paired statistic sufficiently to audit it.

Most importantly, a team pass does not show that **both** members made necessary, correct, adopted, and consequential contributions. Selected self-reports and summarized logs suggest brainstorming, reframing, implementation, and repair occurred, but there is no opportunity-level intervention ledger, semantic-uptake coding, contribution ablation, frozen-state replay, or independent process annotation. CentaurEval therefore supports a bounded claim that one selected participant population using one Copilot/Claude-Sonnet-4 package achieved more hidden-test passes than the same participants did on different counterbalanced tasks without Copilot. It does **not** establish task-level collaboration necessity, causal synergy beyond additive or tool effects, general human–AI complementarity, ecological/professional validity, productivity, workforce value, or readiness.

The durable lesson for `skill-bench` is a **collaboration-value evidence chain**:

```text
template-level construct claim
→ immutable instantiated task and admissible solution set
→ matched human / agent / team resource envelope
→ contribution opportunity
→ contribution exercised with authority and evidence
→ recipient receipt and semantic uptake
→ authoritative artifact/state consequence
→ independent quality and preservation check
→ matched outcome contrast
→ human burden and total cost
→ bounded complementarity/value claim
```

CentaurEval provides meaningful evidence at the template, configured-condition, endpoint, self-report, and direct-cost levels. It leaves key joins between them unidentified.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, C, E, and F through a narrow coding case that tests a general benchmark-design question: **what evidence licenses saying that consequential work requires and benefits from human–agent collaboration rather than merely showing that a configured team outscored unlike standalone conditions?**

- **Concrete evidence:** the complete immutable 42-page arXiv v3 paper, full local text, API metadata, appendix instruments, and a bounded release search.
- **Uncertainty clarified:** the separation among model-relative task difficulty, human difficulty, team uplift, task-level necessity, realized contribution, complementarity, burden, ecological validity, and value.
- **Mode:** validation-oriented expansion with consolidation implications.
- **Duplication and scope check:** HAS-Bench uses simulated participants; HiLSVA and Pista expose mixed-initiative controls but do not run this four-condition human/agent comparison. Coding is the methodological substrate, not a scope commitment.
- **Useful completion:** retain the real-participant contrast and task-construction ambition, while refusing to infer necessity, synergy, or professional value without matched instances, contribution lineage, resource parity, and consequence evidence.

## Sources and reading record

### Primary source read in full

- Hanjun Luo et al., *CentaurEval: Benchmarking Human-in-the-Loop Value in Agentic Coding*.
- Immutable arXiv v3: <https://arxiv.org/abs/2512.04111v3>, updated 21 May 2026; accepted at ICML 2026.
- Local PDF: `data/papers/pdfs/2512.04111v3-centaureval-human-in-the-loop-value.pdf` (42 pages; SHA-256 `5c691a1cc2475b05c353f52bd52352105920ff1c85f581813a15d8e4f9a893f0`).
- Full layout extraction: `data/papers/text/2512.04111v3-centaureval-human-in-the-loop-value.txt` (SHA-256 `71467103e5603aae1fb53eb87eca0f3c9cc84d628f0e06c3ea183bbbae73cde5`).
- API metadata: `data/papers/source/2512.04111v3-metadata.xml` (SHA-256 `bd5fd377ce0399ac4c288811363c9af50fba25a1c6c3658fcdf091f2fff8d9c6`).

The full extraction was read through the paper, validation appendices, three example tasks, `C1` intervention protocol, participant selection and demographics, consent and questionnaires, human protocol, detailed model/human results, qualitative account, cost accounting, and final case study. Page references below use PDF pages.

### Release-availability boundary

The paper repeatedly says the 450-task toolkit/dataset is released and the impact statement mentions an open-source toolkit and interactive demo (pp. 2, 6, and 10). However, no author-owned task, template, code, data, result, or trace URL appears in the arXiv paper/HTML. The acquisition worker also checked the ICML record and renewed targeted GitHub, Hugging Face, and author searches without finding a verifiable official package. That is a bounded absence as of this review, not proof that no release exists. Third-party notes were not substituted for primary release evidence.

Accordingly, all system behavior, task contents beyond the printed examples, result tables, intervention events, and qualitative findings remain **paper-reported rather than release-audited or replayed**.

## One-sentence contribution

CentaurEval combines model-relative low-success task templates, dynamically generated human tasks, a static 450-instance model suite, executable hidden-test grading, and a 45-person within-subject human-only versus Copilot-assisted study, but its unmatched task/resource envelopes and absent contribution lineage limit the result to a configured participant-package contrast rather than task-level collaboration necessity or causal complementarity.

## Research question and claim boundary

The paper asks whether an evaluation can quantify human value in agentic coding by constructing “Collaboration-Necessary” tasks that are intractable for standalone models and suboptimal for unaided humans but solvable by teams. It formalizes two requirements (p. 3): low autonomous-agent success and a positive expected team-versus-human score margin. It further claims ecological validity from industry-like interaction, strong assistance, and realistic task presentation.

Those are at least six distinct questions:

1. **AI-incompleteness:** does a pinned autonomous configured system fail a frozen task distribution?
2. **Human difficulty:** does a defined human population fail or incur high burden under a matched envelope?
3. **Team uplift:** does an assigned human–agent package outperform a valid human-alone and agent-alone counterfactual?
4. **Collaboration necessity:** on which tasks are contributions from both parties necessary for an accepted outcome?
5. **Complementarity:** are the contributions nonredundant and jointly valuable rather than simply more compute, information, retries, or implementation capacity?
6. **Professional value:** does the collaboration improve consequential work relative to its human, service, review, and coordination costs?

The paper provides useful evidence for 1 under selected configurations and for a narrow version of 3 between `CH` and `C2`. It does not identify 4–6. Its task-level formalism is not actually evaluated at the task level: template admission tests agents only; the human study aggregates different dynamic instances; and no joint counterfactual demonstrates that a passed team instance would fail for the same human and agent separately.

A safe claim is:

> Among 45 selected East-Asian computer-science students/recent graduates who regularly used coding agents, 90 Claude-Sonnet-4/Copilot-assisted dynamic task trials produced 28 hidden-test passes, while 90 counterbalanced human-only dynamic task trials produced 17, under the paper's configured Codespaces protocol.

Even this claim depends on paper-reported task assignment and analysis because trial rows are unavailable. It does not generalize to industry developers, other tools/models, naturally occurring work, or collaboration as a class.

## Methodology and system

### Template bank and the construct contradiction

The bank contains 45 templates in a `3 tracks × 3 difficulty levels` matrix: software development, machine learning engineering, and data science, with five templates per track/difficulty cell (pp. 4–5). Authors wrap algorithmic cores in contextual and relational complexity intended to obstruct direct model decomposition, including underspecified requirements, multimodal specifications, legacy code, domain constraints, repetitive implementation, and unfamiliar APIs.

This is an interesting attempt to create complementary demands, but the paper reveals an unresolved construct tension:

- the design relies on ambiguity, missing specification, misleading artifacts, and deliberately verbose originals “to make it hard for LLM parsing” (pp. 4, 22–25, 42);
- the quality rubric simultaneously requires unambiguous task objectives, complete context, clearly stated constraints, and clearly defined criteria (pp. 21–22);
- the case study says column-merging behavior is intentionally vague and available only through legacy code, while calling the task ecologically valid requirement engineering (p. 42).

A task can fairly require evidence integration or inference, but intentional verbosity or distractors may measure prompt parsing, benchmark-specific trap recognition, or tolerance for obfuscation. `skill-bench` should preserve ambiguity only when it has a public professional basis, source-authority structure, and consequence—not because it selectively defeats one model family.

### Template screening establishes only model-relative selection

Template admission has two model tests (pp. 5 and 18):

- Claude-Sonnet-4 may pass at most 1 of 20 generated instances;
- GPT-4.1 and Gemini-2.5-Pro may each pass at most 1 of 10 generated instances.

All final templates pass; 42 have zero success across all three models. This is concrete evidence of selected model-relative difficulty, but it is also **outcome-conditioned task construction**. The final suite was explicitly selected to defeat the same Claude-Sonnet-4 package central to the human study and then used to argue a fundamental higher-order reasoning wall. Low success on an admission-conditioned bank cannot estimate failure prevalence in a broader work population.

The screen does not include:

- unaided humans;
- human–agent teams;
- a task-level necessity test;
- contribution ablations;
- alternative harnesses or direct model APIs;
- repeated model runs sufficient to estimate a stable success probability;
- a holdout template set untouched by model outcomes;
- a later model/task-health transition rule.

The paper calls each `Pass(A,t)` a one-attempt observation, while the autonomous pipeline iteratively feeds visible-test logs and `C0` allows automatic retries up to 25 (pp. 6–7). The exact relationship among attempt, refinement turn, pass@1, and pass@10 is not operationally reconciled.

### Dynamic instantiation and expert validation

A GPT-4.1 agent orchestrates four tools for technical parameters, implementation constraints, contextual variables, and interface specifications. Logic-critical values are described as rule-based or selected from validated ranges; context is generated at temperature `.7`; a task package and instance-specific evaluation script are emitted together (pp. 5, 18–20).

The static model dataset uses 10 instances per template. Two experts with at least three years of industry or equivalent academic experience document-review all instances. They manually test three initial instances per template and two randomly selected instances among seven extended instances (pp. 21–22). The reported four-dimension Cohen kappas are `.91–1.00` over 90 sampled records. Forty templates pass on first attempt, three are revised, and two are rejected/replaced.

This is stronger quality-control evidence than unchecked generation, but its ceiling is limited:

1. reviewer identities, track-specific authority, training, exact independent labels, disagreement counts, and adjudication changes are unavailable;
2. all retained labels become positive after revision, so the released reliability calculation cannot be checked for prevalence effects or revision leakage;
3. manual testing is not tied to a stated time, tool, feedback, or no-AI condition;
4. “Collaboration-Necessary” is one binary reviewer dimension combining requirement analysis and contextual reasoning, not a demonstrated human-plus-agent counterfactual;
5. generation and evaluation scripts share the same instance parameters, creating coherent co-generation without proving natural-language/specification/verifier equivalence or alternative-solution completeness;
6. the authors assert contextual generation introduces no additional difficulty, but provide no matched instance-equivalence experiment.

The static expert review therefore supports internal coherence and perceived construct fit, not professional authenticity, necessity, or dynamic-instance exchangeability.

### Four conditions are not four levels of one intervention

The paper describes four conditions (p. 7):

- `CH`: participants work without AI in Codespaces;
- `C0`: Copilot runs autonomously, including automatic retries up to 25;
- `C1`: a researcher repairs listed procedural/environment failures but provides no intended semantic help;
- `C2`: participants freely use Copilot.

These are configured packages, not an ordinal dose of “human intervention.” They change participant realization, task set, execution substrate, information flow, retry policy, active time, model-call topology, and authority:

| Boundary | `CH` | `C0` | `C1` | `C2` |
|---|---|---|---|---|
| Actor | selected participant | Copilot controller | Copilot + researcher | participant + Copilot |
| Task realization | dynamic | static 450 | static 450 | dynamic |
| Runtime | Codespaces | local Docker/VS Code controller | local Docker/VS Code controller | Codespaces |
| Feedback | visible tests, human debugging | visible-test logs iteratively fed back | same plus procedural repair | visible tests plus free dialogue |
| Retry/intervention | human iteration | automatic retries, stated up to 25 | researcher interventions, count absent | human-agent turns, mean 57–70 |
| Human burden | up to 60 min/trial | none | researcher burden unreported | up to 60 min/trial |

`C1` also permits judgment-laden repairs: selecting a different port, setting an “implicitly required” environment variable, deciding a command is correct in intent, or installing a declared dependency (pp. 26–27). Those may be reasonable invalid-run repairs, but their opportunity, exercise, latency, changed state, and model continuation are not reported. `C1 − C0` is therefore not a pure “core reasoning” estimand.

### Human study population and assignment

The study recruits 45 participants through personal contacts and university advertisements. All identify as East Asian; ages are 19–26 (mean 21.4); 24 are undergraduate students/graduates, 15 masters, and six doctoral; average internship count is 1.47. Eligibility nominally requires two years of programming, Python/VS Code/track proficiency, and AI-assistant use at least three times per week. Credentials are checked against public profiles, and selected candidates may complete a Copilot screening interview (pp. 7, 27–28).

Calling this group “expert users” is defensible only as **screened frequent student/recent-graduate tool users**. The paper acknowledges demographic and industry-generalization limits. It does not report recruitment flow, number screened, exclusions, failed proficiency interviews, refusal, attrition, withdrawal, incomplete sessions, or deviations.

Each participant completes two `CH` and two `C2` tasks over two sessions separated by about 24 hours. Task sequence is randomly selected from balanced permutations; a Latin square is said to make every problem appear equally across conditions and with different participants (p. 7). This is a genuine within-participant treatment design, but the exact participant × period × template × instance × condition matrix is absent. Because tasks are dynamically instantiated, the participant does not solve the same frozen instance twice. No equivalence-form analysis shows that condition-specific instances have matched hidden tests, wording burden, distractors, implementation volume, or runtime thresholds.

The paper argues expertise and counterbalancing minimize order effects, and participants later report low perceived order effects. Self-reported absence of carryover is not an order analysis. No period, sequence, learning, session, 24-hour deviation, track, template, or participant-random-effect model is reported.

### Time, stopping, and resource envelopes

The main metric section defines a 60-minute timeout per trial; failures/timeouts receive 60 minutes (p. 7). Consent estimates 45–60 minutes per task and 3–4 hours total, with two tasks per session (pp. 29–30). The protocol later says “the total time limit for completing all tasks is two hours” (p. 36), apparently referring to one two-task session but worded inconsistently.

The model controller stops after visible tests pass or a predefined limit. `C0` includes up to 25 automatic retries, and pass@10 is reported, but the paper does not state:

- whether retries are full independent trials, continuation attempts, or best-of-k selections;
- which attempt contributes time/tokens;
- whether failed API calls, environment failures, or researcher repairs are censored;
- model wall-clock limits by condition;
- Copilot rate limits, context windows, tool-call limits, or model-service dates beyond July 2025;
- whether humans may submit multiple times or see backend results;
- whether participants can use internet, documentation, packages, or external communication;
- active versus waiting time.

The conditions therefore do not share a demonstrated resource envelope. “Capability multiplier” and productivity language are especially unsafe when the team receives a person, millions of interaction tokens, different instances, and a different execution path.

## Evidence and result audit

### Denominators recoverable from the printed percentages

The human study contains `45 × 4 = 180` trials: 90 `CH` and 90 `C2`. The reported pass rates exactly correspond to:

- `CH`: `17/90 = 18.89%`;
- `C2`: `28/90 = 31.11%`.

The Claude-Sonnet-4 autonomous rows use 450 static tasks:

- `C0`: `3/450 = 0.67%`;
- `C1`: `13/450 = 2.89%`.

The Table 3 confidence intervals exactly reproduce ordinary Wilson binomial intervals over those denominators: `12.14–28.18`, `22.49–41.28`, `.23–1.94`, and `1.70–4.88`. This confirms that the four displayed intervals concern unlike trial populations and ignore template and participant clustering. They are not intervals for matched human-versus-agent or team-versus-agent effects.

The paper reports a two-sided paired sign test for `CH` versus `C2`, `p=.00739`. That value is almost exactly the two-sided exact sign probability for 13 favorable and two unfavorable signs among 15 non-tied units, but the paper does not define whether a sign is based on participant pass counts, partial score, paired templates, or another summary, nor does it publish the 45 paired rows/ties. The test cannot be audited from aggregate counts. Even if correct, it tests a median directional difference for this assignment; it does not establish task-level necessity, causal mediation by collaboration, or population transport.

### Endpoint gains are real paper-reported observations, but their interpretation is narrower

The main endpoint contrast is 11 additional team passes across 90 trials. Partial pass rises from `33.53%` to `50.27%`; reported mean time falls from `3,203` to `2,791` seconds. These are promising configured-package observations.

The paper calls the time reduction significant but gives no statistic, interval, censoring-aware model, or multiplicity plan. Timeout-capped PAR times combine successful speed, failure, and censoring. A lower average can arise from more passes, different task forms, more model compute, or true human-time savings; it is not standalone productivity evidence.

Difficulty analyses are also post-construction strata, not clean effect modifiers. “Hard” combines algorithmic complexity, implementation scope, estimated expert time, contextual barriers, and template labels. The larger hard-task point gain (`6.7% → 23.3%`) may be important, but no interaction test, template-clustered interval, or task-form equivalence analysis is reported.

### Printed tables contain unresolved numerical and metric inconsistencies

Several results cannot be reconciled from v3:

1. Table 2 reports overall completion times `CH=3,203`, `C0=3,576`, `C1=3,500`, and `C2=2,791` seconds. Table 8's track rows report `CH=2,966/2,791/2,603`, `C2=2,567/2,652/2,551`, and implausibly small autonomous values `C0=216/203/233`, `C1=229/214/262`. Equal-track averages do not recover Table 2, and the autonomous values differ by roughly 3,300 seconds.
2. Table 2 and Table 8 partial-pass cells do not consistently match the detailed Claude table (for example DS `C1` is reported as `31.28` in Table 8 versus `31.00` in Table 7).
3. “Partial Pass@10” is lower than “Partial Pass@1” in several cells (for example Claude-Sonnet-4 overall `15.89` versus `19.24` and hard `9.74` versus `11.63`). That can occur only under a nonstandard averaging definition; no formula is supplied, so the `@10` label is not auditable as a usual best-of-k success metric.
4. The protocol appendix calls the collaboration condition `C3` and human-only `H`, while the main paper uses `C2` and `CH` (p. 35), indicating instrument/version drift.
5. The text says Table 8 “proves” generalizability across tracks despite only 15 selected participants and 30 trials per condition in each track, no interaction inference, and no independent track population.

These are not cosmetic when the benchmark's contribution is quantitative human value. A released typed result ledger and replay script are needed before the table set can support cumulative use.

### Interaction and self-report evidence does not identify contribution

Post-study reports show:

- all 45 used AI for boilerplate;
- 41 used it for debugging;
- 36 for brainstorming;
- 23 for a fundamentally different approach;
- mean team turn count rises from `57.30` on easy tasks to `69.80` on hard tasks;
- confidence rises by `1.60` Likert points and cognitive ease by `.51`;
- trust in code and explanations averages `4.09` and `4.22`;
- task realism averages `4.07`.

These are useful perception and feature-exercise observations. They do not show whether a particular suggestion was correct, novel, adopted, necessary, or outcome-changing. Selecting the top 15 performers and observing that 12 report fundamental AI suggestions is post-outcome conditioning; it cannot show that strategic use caused performance.

High trust is not calibrated trust. No reliable/unreliable suggestion strata, confidence–correctness relation, acceptance/rejection accuracy, overreliance rate, or decision loss is measured. Participant realism ratings establish perceived resemblance among selected frequent AI users after exposure to the study rationale—not ecological validity, occupational sampling, or recipient utility.

### Qualitative evidence is illustrative, not a reproducible process study

The paper says feedback and behavioral logs were reviewed and offers human, AI, team, and failure patterns (pp. 40–42). The final case is genuinely instructive: a participant redirects an agent away from legacy-code brute force; the agent proposes a queue refinement; the participant approves, inspects, and repairs; the final code passes.

But the paper does not report:

- how logs or cases were sampled;
- analyst count, expertise, independence, or blinding;
- a codebook or unit of coding;
- inter-rater agreement;
- participant/task/theme prevalence;
- disconfirming-case search;
- proposition-level attribution;
- original transcript or code/state snapshots;
- translation protocol.

The case dialogue is translated, polished, and summarized; chain-of-thought was not fully visible. It proves existence of one narrated successful trajectory, not prevalence, necessity, or a general co-reasoning mechanism. Likewise, the failure narrative—late intervention after 40 minutes—is a valuable hypothesis about intervention timing but lacks a denominator and matched earlier-intervention counterfactual.

### Human burden and cost are only partially counted

Participants receive `$40` after four tasks and questionnaires; direct compensation totals `$1,800`. The study uses 11 free Copilot Education accounts and 34 Pro accounts costing `$480`, for `$2,280` disclosed direct cash cost (p. 41). The consent estimate implies roughly 135–180 participant-hours for programming alone, plus questionnaires; the payment therefore corresponds to roughly `$10–$13.33` per programmed hour before questionnaire time.

The cost section omits:

- recruitment and screening labor;
- public-profile verification and proficiency interviews;
- expert template authoring, repeated revision, 450 document reviews, and sampled manual testing;
- researcher time for `C1` interventions, spot checks, study administration, log review, and qualitative synthesis;
- Codespaces, backend, Docker, storage, evaluation, and network costs;
- GPT-4.1 task generation and all five-model `C0/C1` evaluations;
- Copilot tokens/calls not captured by subscription prices;
- participant waiting, stress, rework, and opportunity cost;
- maintenance as model-relative necessity decays.

The paper deserves credit for disclosing participant and account cash. It does not estimate total benchmark-authoring cost, evaluation cost, team cost per accepted result, or net value.

### Ethics and participation governance

The paper reports IRB approval, written consent, anonymized accounts, withdrawal, de-identification, and compensation. The appendix provides unusually concrete consent and questionnaire text (pp. 29–34). These are strengths.

Important operational details remain absent: IRB identifier/institution, retention/deletion period, whether raw code/logs may be released, reconsent for new benchmark uses, withdrawal after de-identification, use of public-profile verification, and disposition of incomplete participation. The pre-test warns compensation may be withheld for false information, while the consent says withdrawal is without penalty; the interaction between those rules is not explained.

## Unique insight: complementarity is a contribution-and-counterfactual claim, not a team score

A team can outperform each standalone condition without demonstrating complementarity. The team may receive more total compute, information, attempts, time, tools, or evaluator cues. One member may perform all consequential work. The agent may merely type an already-known solution, or the human may merely restart a stalled process. Conversely, a valuable contribution may not change binary success because a later failure masks it.

A benchmark therefore needs two linked units:

### 1. Task-form counterfactual unit

For an immutable task or validated equivalent-form block, preserve:

- public requirements and hidden-but-fair consequences;
- task/template/form identity and lineage;
- participant/model assignment;
- information, tools, environment, feedback, time, token, call, and retry budgets;
- human-only, agent-only, team, and where ethical/oracle-relevant ablation arms;
- outcome, quality, safety, cost, and missing/invalid status;
- participant, template, form, and run clustering.

This supports a bounded treatment contrast.

### 2. Contribution episode unit

For each genuine opportunity, preserve:

1. the uncertainty, defect, decision, or implementation need;
2. what each participant could observe and was authorized to decide;
3. who initiated which proposal, evidence, question, veto, edit, or action;
4. whether the recipient received and correctly interpreted it;
5. whether it was adopted, rejected, distorted, or superseded;
6. the exact artifact/state loci changed;
7. independent verification and collateral effects;
8. downstream outcome and burden;
9. a contribution ablation or replay where feasible.

Only a join of these records can distinguish:

- **team-package uplift**: one configured team outscores a baseline;
- **division of labor**: different participants perform different observed operations;
- **complementarity**: nonredundant contributions jointly improve outcome under matched resources;
- **necessity**: removing either contribution causes failure for the defined task/configuration;
- **professional value**: outcome improvement exceeds human, service, review, and risk costs for an intended use.

CentaurEval names this hierarchy but measures mainly the first rung.

## Comparison with adjacent reviewed evidence

- **HAS-Bench:** HAS-Bench has a richer participant/authority/event vocabulary but uses model-simulated “humans.” CentaurEval supplies real participants and real burden, but its intervention traces are less operationalized. Together they require participant realization plus availability → exercise → uptake → effect → burden; neither a role label nor a team endpoint is enough.
- **HiLSVA:** HiLSVA exposes plans, approvals, direct manipulation, rollback, and mode choice but lacks independent artifact quality and intervention consequences. CentaurEval has stronger executable endpoints and a human-only arm, but does not connect dialogue episodes to those endpoints. The shared missing link is proposition-level semantic uptake and state consequence.
- **Pista:** Pista demonstrates that richer visibility and local edits can improve perceived control without establishing defect correction. CentaurEval similarly treats frequent strategic use and high trust as co-reasoning evidence; neither has matched error opportunities, realized-repair checks, or calibrated reliance.
- **AgentCo-op:** AgentCo-op's handoff ladder distinguishes transport, parse, meaning, receiver acceptance, next operation, and consequence. CentaurEval's natural-language turns need the same receiver-use evidence. A human prompt and a later pass do not prove semantic adoption or causal contribution.
- **EntCollabBench:** EntCollabBench separates role-scoped capability, routing, delegated authority, and authoritative state effect. CentaurEval's participant has real agency, but contribution authority and responsibility are still untyped; “the human fixed it” or “AI proposed it” requires evidence and state lineage.
- **Human oversight in practice:** interviewees report plans, tests, spot checks, and cross-agent comparison as heuristics, not validated best practices. CentaurEval observes similar monitoring/redirection narratives but does not estimate which practices detect defects, prevent harm, or repay their burden.
- **Expert-participation contracts:** participant consent and benchmark-contributor authority are different. CentaurEval participants are benchmark users, not task-authoring professionals or affected recipients. Their realism ratings cannot substitute for expert task validity, and task reviewers' approval cannot substitute for participant outcome evidence.

## Limitations and validity threats

1. Template admission selects for failure of three named models, including the central team model.
2. Admission tests AI-incompleteness only; it does not test human difficulty or team solvability.
3. “Collaboration-Necessary” is therefore not established as a task property.
4. Necessity is model-, harness-, prompt-, retry-, and date-relative, as the paper acknowledges.
5. No untouched holdout template family tests whether the construction method generalizes beyond outcome-selected templates.
6. Intentional verbosity “to make it hard for LLM parsing” risks benchmark-specific obstruction rather than professional complexity.
7. Underspecified requirements conflict with the quality rule requiring complete, unambiguous specifications.
8. Legacy distractors and hidden interpretation rules may be unfair unless their public source basis and authority are explicit.
9. Generation and evaluation scripts share parameters, supporting coherence but not instruction/verifier equivalence.
10. Alternative valid solutions and verifier completeness are not audited.
11. Expert reviewer identities, domain authority, training, raw labels, and disagreement lineage are absent.
12. Manual testing conditions, time, tools, AI access, and completion outcomes are unspecified.
13. Kappa over selected binary quality labels does not validate collaboration necessity or professional authenticity.
14. Dynamic human tasks and static model tasks are different instance populations.
15. Codespaces human execution and local Docker model execution are not demonstrated equivalent.
16. `CH` and `C2` participants solve different dynamic tasks, not the same frozen instance.
17. The task/form assignment matrix and generated form hashes are not released.
18. No empirical equivalent-form analysis establishes matched wording, hidden tests, implementation scope, or runtime.
19. `C0`, `C1`, `CH`, and `C2` differ in actor, task set, environment, feedback, retry, time, and tool topology.
20. `C1` researcher interventions include judgment-laden procedural repairs and have no event denominator.
21. Automatic retries up to 25 are not reconciled with pass@1/pass@10 or one-attempt validation.
22. Human submission/retry and backend-feedback policies are underspecified.
23. Network, documentation, package, communication, and external-information access are not fully stated.
24. No recruitment-flow, screening, exclusion, attrition, withdrawal, or missing-trial ledger is reported.
25. The participant population is young, academic, geographically/culturally narrow, and selected for frequent AI use.
26. “Expert” status is not anchored to occupational performance or independent track-specific criteria.
27. Track assignment rules are described as guidelines rather than strict criteria.
28. Exact counterbalancing, randomization, period, sequence, and session assignments are unavailable.
29. Participant-perceived absence of order effects is not a carryover analysis.
30. The endpoint intervals ignore participant and template clustering.
31. The paired sign-test unit, tie handling, signs, and participant rows are not reported.
32. No multiplicity plan covers pass, partial pass, time, difficulty, track, self-report, and usage analyses.
33. The claimed significant time reduction has no reported test or censoring-aware analysis.
34. PAR-capped time combines failure and speed and cannot alone establish productivity.
35. Table 2 and Table 8 completion times are mutually inconsistent.
36. Several detailed partial-pass cells disagree across tables.
37. Partial Pass@10 can be below Partial Pass@1 under an undefined nonstandard aggregation.
38. Protocol labels drift from `CH/C2` to `H/C3`.
39. Track consistency does not prove generalizability with 15 selected participants per track and no interaction model.
40. Team turns are activity counts, not useful-contribution, coordination-quality, or burden measures.
41. Self-reported strategic usage is not correctness, uptake, or causal contribution.
42. Top-performer usage analysis conditions on the outcome and has no matched counterfactual.
43. High trust is not calibrated trust and may coexist with overreliance.
44. Confidence and cognitive-load changes have no baseline calibration, uncertainty, or consequence relation.
45. Realism ratings from selected users do not establish ecological or professional validity.
46. Qualitative log analysis lacks sampling, codebook, analysts, reliability, prevalence, and negative-case protocol.
47. The polished/translated case study is illustrative and cannot establish a general co-reasoning mechanism.
48. No contribution ablation or frozen-state replay tests whether human and agent inputs were necessary.
49. Binary hidden tests do not assess readability, maintainability, extensibility, handoff quality, security, or recipient acceptance; the paper lists these as future work.
50. Auto-calibrated efficiency thresholds lack released reference solutions, hardware identities, runs, tolerances, or transport evidence.
51. Direct cash cost excludes most authoring, screening, administration, infrastructure, model, review, and maintenance costs.
52. Participant compensation is low relative to the stated 3–4-hour programming commitment, before questionnaires.
53. Consent materials do not state retention/deletion, future release scope, or reconsent boundaries.
54. No official benchmark/code/data/trace release was verifiable at review time despite release claims.
55. Model/API/Copilot identities are mutable and exact study snapshots are unavailable.
56. No raw participant rows, task instances, hidden tests, logs, judge outputs, or analysis script permit reproduction.

## Reproducibility and operational realism

### Reproducibility

Paper-level transparency is mixed. The appendices provide template thresholds, generator hyperparameters/prompts, validation stages, four quality dimensions, `C1` intervention examples, participant criteria/demographics, consent, questionnaires, high-level protocol, detailed aggregate tables, qualitative examples, and direct cash cost. Those details make a design audit possible.

Claim reproduction is weak. The exact 45 templates, 450 static instances, dynamic human forms, hidden tests, generation code, CentaurEC extension, model prompts, retries, participant assignments, raw outcomes, intervention logs, traces, questionnaire rows, qualitative corpus/codebook, analysis script, and environment manifests are not verifiably released. Contradictory tables and undefined pass@10 semantics cannot be resolved from primary evidence. The result should not be used as a calibration anchor until a versioned release and corrected result ledger exist.

### Operational realism

Codespaces, VS Code, terminals, starter repositories, visible/hidden tests, debugging, legacy code, domain constraints, and long interactive sessions resemble parts of contemporary coding practice. The study also measures genuine human time and exposes real tool interaction rather than simulated dialogue.

Yet the tasks are generated around algorithmic cores, intentionally obfuscated to defeat selected models, solved individually under 60-minute limits, and judged primarily by hidden functional/efficiency tests. There are no stakeholders, evolving requirements, code review, deployment, maintenance, team handoff, security assessment, production data, or downstream users. Standardized tooling improves administration; it does not by itself create ecological validity. The benchmark is operationally richer than function generation and narrower than professional software work.

## Transfer to skill-bench

1. **Type the claim ladder.** Keep task difficulty, human difficulty, team uplift, division of labor, complementarity, necessity, productivity, professional value, and readiness as separate validity claims.
2. **Require task-form identity in human/agent comparisons.** Record immutable instance hashes or validated equivalent-form blocks. A template label is not a matched task.
3. **Represent the full resource envelope.** Pin information, tools, runtime, model/service, prompt, visible feedback, time, calls, tokens, retries, intervention policy, human experience, and waiting time per arm.
4. **Do not order unlike packages on one “intervention level.”** Encode participant realization and treatment vectors independently: no human, procedural operator, free collaborator, expert reviewer, simulator, or replay.
5. **Add contribution episodes to traces rather than a new subsystem.** Reuse participation, trace, artifact/state, metric, and validity records to join opportunity, authority, exercise, receipt, semantic uptake, state effect, verification, consequence, and burden.
6. **Use contribution ablations sparingly but explicitly.** For selected shared defect/opportunity cases, compare frozen pre-intervention state with human input, agent input, both, neither, and replayed equivalent information where ethical and feasible.
7. **Preserve cluster-aware denominators.** Report participants, templates, forms, trials, retries, invalid runs, and contribution opportunities separately; model participant and template/form dependence.
8. **Treat model-relative necessity as task health.** A task can transition from collaboration probe to autonomous regression item as models improve; do not call collaboration necessity permanent.
9. **Make ambiguity professionally fair.** Every hidden consequence should trace to disclosed evidence, authority, source precedence, or legitimate convention. Deliberate verbosity or distractors need an independently validated work analogue.
10. **Validate equivalent forms.** Test hidden-test difficulty, wording burden, implementation volume, solver performance, expert ratings, and condition exchangeability before dynamic forms support treatment comparisons.
11. **Separate endpoint and artifact quality.** Functional/efficiency gates should be joined with maintainability, safety, structure, provenance, handoff, and recipient checks only where those constructs are independently authorized and calibrated.
12. **Measure burden and cost plurally.** Preserve participant active/wait time, interaction turns, review/correction work, cognitive demand, compensation, service spend, administration, authoring, maintenance, and cost per accepted result.
13. **Calibrate trust and intervention timing.** Pair correct/incorrect suggestions and early/late opportunities with acceptance, rejection, repair, collateral effect, confidence, and workload outcomes rather than global trust ratings.
14. **Require a typed result ledger.** Contradictory tables, retries, missingness, and pass@k definitions should fail release validation before headline claims are published.
15. **Do not narrow to coding.** The reusable hypothesis is that complementary expertise plus implementation capacity may improve consequential artifacts. Test the same evidence chain across unlike domains and artifact classes.

## Concrete repository actions

No new queue task is added. The evidence identifies no distinct subsystem beyond already implemented or pending configured-system, participation, intervention, trace, artifact/state, metric, task-health, validity, and human-burden machinery. It should refine the pending consolidation of realized-intervention boundaries rather than duplicate it.

Concrete retained requirements for that consolidation are:

- add `task_form_identity/equivalence_block` and `resource_envelope` to any human/agent treatment comparison;
- separate team-package uplift from contribution, complementarity, necessity, and value claims;
- preserve contribution-opportunity, exercise, semantic uptake, state consequence, independent verification, and burden denominators;
- treat model-relative collaboration necessity as a versioned task-health role;
- require typed result-ledger consistency before human-value claims.

## Bottom line

CentaurEval is worth retaining because it takes the difficult step that many human–agent benchmarks avoid: real people perform both unaided and agent-assisted tasks under executable evaluation, and the paper exposes participant materials and direct cash cost. The observed 17-versus-28 pass contrast is a meaningful signal about one configured participant/Copilot package.

But the benchmark's title claim—human-in-the-loop value—and its “Collaboration-Necessary” construct require more. The selected templates are screened only for model failure; human and agent conditions use different task realizations and execution envelopes; team contributions are not proposition- or state-linked; statistical units and several tables are not auditable; qualitative evidence is selected and summarized; and no official artifact release could be verified. For `skill-bench`, retain the ambition and real-participant design, repair task/resource matching and result reproducibility, and test collaboration as an auditable contribution chain. Do not equate a higher team pass rate with necessity, synergy, complementarity, ecological validity, productivity, professional value, or readiness.