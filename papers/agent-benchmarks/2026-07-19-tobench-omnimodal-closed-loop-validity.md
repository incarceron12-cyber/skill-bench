# TOBench: closed-loop multimodal work is the right execution target, but the benchmark does not identify closed-loop correction or evaluator validity

## Source and review status

**Deep review of the complete immutable primary paper plus a timing-appropriate official release audit.** I read the full 43-page arXiv v1 paper and inspected the pinned official repository, including the generation prompts and code, evaluator synthesis prompt, reference evaluator, runtime evaluator, workspace initialization, MCP configurations, candidate records, and test runner. I did not reproduce paper scores because the 100 executable task packages, assets, criteria, ground-truth workspaces, generated evaluators, run traces, and score records are not in the GitHub release; the README points to a Hugging Face dataset URL whose API returned HTTP 401 during this audit.

- **Paper:** Zhiqiang Liu et al., *TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents*, arXiv:2605.16909v1, <https://arxiv.org/abs/2605.16909v1>
- **Version read:** immutable v1, submitted 16 May 2026; no withdrawal notice in acquired metadata
- **Local PDF:** `data/papers/pdfs/2605.16909v1-tobench.pdf` (43 pages; SHA-256 `96f27d6e6931d9b90a419cd403ea6ccda45ebbe9590173a5c5d06c1a42f814f5`)
- **Local full text:** `data/papers/text/2605.16909v1-tobench.txt` (SHA-256 `e93c429e5ab2917609e4786fe2f2191dc70113fc389cecee0fd9677471183676`)
- **Official repository:** <https://github.com/Pi3AI/TOBench>
- **Pinned release:** commit `a3b9a27a1f9975cb4275e79920f6af2498f7d4e6`, committed 11 May 2026—four days before arXiv v1
- **Archive:** `data/sources/releases/2605.16909v1-tobench/Pi3AI-TOBench-a3b9a27.zip` (SHA-256 `4b944b3b4ea7c586453595e64a35b8e6d2e402c5597abd592c573049ae61bbb5`; ZIP CRC passed; 967 regular files)
- **Provenance:** `data/sources/releases/2605.16909v1-tobench/provenance.json`
- **Date read:** 19 July 2026

The pinned release is close enough in time to be relevant implementation evidence, but the paper does not name an experimental commit. Repository facts below are therefore distinguished from paper claims rather than projected backward into the reported runs.

## One-sentence contribution

TOBench proposes 100 task-oriented, cross-tool, multimodal artifact workflows over 27 MCP servers, task-specific mixed deterministic/model evaluators, and a generate–inspect–revise agent loop, but its paper and partial release support **configured-system end-state conformance on an unreleased authored suite**, not identified self-correction, evaluator accuracy, task-generation validity, occupational realism, human parity, or reproducible benchmark scores.

## Why this matters for `skill-bench`

TOBench is unusually close to the charter's central execution problem. It tries to turn broad user scenarios into multimodal source packs, tool-accessible workspaces, explicit role/domain rules, native artifacts, artifact inspection, repair, and criterion-level evaluation. Its two families—Customer Service and Intelligent Creation—span documents, spreadsheets, slides, PDFs, images, audio/video, browser retrieval, maps, finance, and filesystem operations. The general hypothesis is cross-domain: **knowledge-work agents need to inspect the consequences of their own tool use, not merely emit tool calls or plausible final prose**.

The audit exposes four boundaries that must remain separate:

1. prompting an agent to inspect and revise is not evidence that it performed causal self-correction;
2. generating executable criteria is not evidence that those criteria faithfully implement the public task;
3. mixing deterministic and model observers is not validation of the resulting Boolean conjunction;
4. role-flavored synthetic scenarios are not a sample of professional demand or user acceptance.

This review advances charter objectives A–D through expansion, validation, and transfer into existing artifact-view, requirement-projection, evaluator-assurance, trial-ledger, and feedback-intervention machinery. It is not a proposal to narrow `skill-bench` to MCP tasks or multimodal artifact production.

## Research question and defensible claim boundary

The paper asks whether current agents can complete real-world task-oriented omni-modal workflows that combine heterogeneous inputs, executable tools, intermediate artifact inspection, and revision under task-specific constraints (Abstract and Sections 1–3). It contributes:

1. 100 executable tasks across two macro families and 20 subcategory slices;
2. an MCP environment reported as 27 servers and 324 tools;
3. an LLM-assisted pipeline for scenario discovery, difficulty-conditioned task generation, asset curation, and evaluator synthesis;
4. final-workspace and trajectory-aware criteria divided into format, judge-based, and tool/result checks;
5. one main configured-agent result table containing 19 named model rows, plus average tool-call, token, and reported API-cost summaries;
6. paper-reported manual review/audit of generated evaluation points and evaluator scripts, a 94% human benchmark, and a trajectory failure taxonomy.

The strongest defensible claim is narrower:

> On the authors' selected 100 task packages, under their unreleased experimental task/evaluator versions and reported model–tool–runtime configurations, configured systems achieved different strict all-criteria pass rates, with Qwen3.5-Plus reaching 41%, while the paper reports a 94% human result without enough method detail to interpret it as a population benchmark or expert ceiling.

The evidence does **not** establish that the benchmark samples real-world or professional work, that agents performed causal inspection-driven repair, that criterion generators produce sound and complete task specifications, that the reported evaluator is calibrated for criterion truth, that all tasks and attempts were valid, that scores are reproducible from public assets, that model labels isolate model effects, or that any system is ready for autonomous customer or creative work.

## Methodology and system

### Scenario and task generation

The benchmark starts from two broad families with ten subcategories each. A model receives a category/subcategory and available MCP descriptions, proposes ten scenario domains, and then generates easy, medium, and hard candidates for each domain. The task prompt requests a role, domain rules, user introduction/instruction, input-file descriptions, required MCP servers, feasibility, realism, and a final reflection/revision step. This produces roughly 600 candidates, from which the authors say 100 executable tasks are selected and instantiated with assets (Section 2.2 and Appendix C).

This is a useful structured ideation pipeline, but the paper does not supply a candidate ledger. There is no stable candidate ID, generator model/version, sampling seed, acceptance/rejection reason, author/reviewer assignment, per-task human time, duplicate policy, independently observed user episode, or comparison against a held-out work-demand frame. “Realistic user needs” is a prompt instruction and author judgment, not measured provenance.

Difficulty is likewise authored rather than calibrated. The prompt varies requirement complexity, ambiguity, and workflow length, but the final 100-task distribution and human difficulty evidence are not reported in a form that permits item-level reconstruction. A generated easy/medium/hard triplet is useful coverage design; it is not an interval scale or proof that the intended mechanism causes observed score differences.

### What the release reveals about generation

The pinned repository contains two different 600-candidate collections:

- `pipeline/data`: 200 JSON domain records containing 600 nested tasks, exactly 200 labeled easy, medium, and hard, with 577 unique task names;
- `pipeline/distill/outputs`: another 200 JSON domain records containing 600 nested tasks, again 200 per difficulty, with 573 unique task names.

The two collections have no byte-identical top-level domain records. Their category labels also differ (`Customer_Service` versus `Custom_Service` for 120 records), and MCP names vary in case and spelling. The first collection includes required names such as `Image-Processing-Toolkits`, `Image_Processing_Toolkits`, `yfinance-mcp-server`, and `arxiv-mcp-server`; the runtime configurations use a separate naming layer. These are direct release observations, not claims about the final 100 tasks.

Crucially, these JSON records are **candidate specifications**, not executable benchmark tasks. They contain generated role/rules/request/input descriptions, but no hydrated assets, `task_config.json`, `initial_workspace`, `groundtruth_workspace`, task-local evaluator, or run result. The archive contains no `tasks/` tree and no `task_config.json` files. The generation script's trajectory/evaluation enrichment block is commented out. The README instead instructs users to download and unzip the dataset separately to `./tasks`.

This distinction prevents a common counting error: the release contains two 600-candidate stores, while the paper reports a curated 100-task executable benchmark. Neither candidate store can be treated as the released score-bearing suite.

### Tool environment and configured systems

The paper reports 27 MCP servers and 324 tools, extending Toolathlon with office, browser, search, media, image generation, and image-processing capabilities (Section 2.2 and Appendix A). The pinned `mcp_details_summary.json` has 27 server rows but 333 declared tools. Most counts match the paper's appendix; the release reports ten arXiv tools where the paper reports four, contributing six of the nine-tool difference. The remaining discrepancy is not reconciled in the paper or release. This is version drift or inventory-definition drift, not evidence that either count is intrinsically wrong.

The tool mix is substantively broad: the release summary includes Word (54), PPTX (37), Playwright (31), video/audio editing (27), Excel (25), image processing (24), and finance (23) among others. It supports real composition pressure. Yet tool count is not an independent construct measure. Several servers are wrappers around overlapping operations; tool discoverability, schema quality, server reliability, and provider access differ substantially. Counting endpoints can exaggerate functional diversity while hiding unavailable credentials and external-service failures.

The paper runs one agent configuration per named model row with the relevant MCP subset and a 100-turn cap. These are configured packages, not isolated base-model comparisons: model endpoint, system prompt, OpenAI-Agents-style runtime, multimodal observation handling, tool schema, context policy, and provider behavior jointly define the treatment. Table 2 records average tool calls, tokens, and API cost, but the paper provides no complete per-row model snapshot/date, decoding configuration, retries, service-failure ledger, or released traces.

### Workspace initialization and operational envelope

The repository's runtime deletes an existing per-attempt agent workspace, copies an `initial_workspace`, runs an optional preprocessing command, and initializes MCP-specific state. The filesystem server is rooted at the agent workspace. This is stronger than reusing an uncontrolled folder.

It is not a demonstrated sandbox. The terminal MCP allows `python`, `curl`, `wget`, `git`, `kubectl`, shell operators, and arbitrary flags while relying on an `ALLOWED_DIR` environment variable. Other MCP servers can reach live web and provider services. The release has no outer containment test for network, process, credentials, filesystem escapes, secret isolation, or cleanup. A server policy configuration is not evidence that every implementation enforces it.

The runtime also supports `--allow_resume`; when enabled with a checkpoint, workspace reinitialization is skipped. Resume is legitimate, but a benchmark report must identify whether an attempt began from a fresh snapshot or inherited prior state. The paper does not release per-attempt workspace hashes or reset canaries.

Operational realism is mixed. Native office/media artifacts, web retrieval, tool composition, and output inspection resemble meaningful digital production. Tasks remain authored, self-contained requests without live organizational identities, permissions, customer consequences, stakeholder review, collaboration, changing upstream state, or downstream use. “Customer Service” here denotes a scenario family, not interaction with a real customer or service system.

## Evaluation design and the closed-loop validity problem

### Criterion types and strict task pass

The paper divides approved criteria into format constraints, judge-based multimodal constraints, and tool/result constraints. A task evaluator consumes the trajectory, final workspace, and tool log and emits a binary criterion vector. Task success is strict conjunction: every criterion must pass (Section 2.3).

This is a valuable move beyond final-answer matching. It can test native filenames and structure, visible appearance, source/tool use, and externally grounded facts. Strict conjunction also avoids allowing severe requirement failures to be hidden by an average.

But strictness and validity are different. Conjunction amplifies every false negative and every irrelevant criterion. It says nothing about whether the criterion set is complete, whether required views are admissible, whether alternative valid artifacts pass, or whether one observer failure should invalidate rather than fail an attempt. No criterion-count distribution, severity taxonomy, dependency graph, applicability rule, alternative-artifact suite, or task-level criterion matrix is released.

### Evaluator synthesis is benchmark compilation

The repository's synthesis prompt asks a model to turn the task, rules, workspace, reference result, and tool information into executable Python. The reference evaluator supplies helper functions for file discovery, office conversion, media extraction, image inspection, trajectory/tool-log parsing, and model judging. The generated evaluator is therefore not a neutral after-the-fact reader; it is a **compiled interpretation of the task** with access to privileged reference artifacts and implementation helpers.

That architecture is scalable, but it creates five independent validity obligations:

1. **requirement projection:** every public/authorized requirement maps to a criterion;
2. **no hidden obligation:** criteria do not add author preferences absent from the task;
3. **view admissibility:** native state, render, trajectory, and model judgment are used only for propositions they can establish;
4. **alternative validity:** materially equivalent compliant outputs pass;
5. **observer failure typing:** missing/corrupt artifacts and model/service/parser failures are not silently turned into substantive criterion failure.

The paper reports no held-out compilation test for these obligations. An evaluator that executes successfully is syntactically usable, not semantically sound and complete.

### Runtime Boolean collapse

The audited runtime treats the task-local evaluation script as a process oracle. If the script returns nonzero, the attempt fails; if it returns zero and task status is `SUCCESS`, the task passes. The wrapper does not preserve a typed criterion ledger. It also maps any nonzero evaluator process—including malformed generated code or infrastructure error—to `pass: false` with stdout as the failure, while outer exceptions become `evaluation_error`. Thus criterion failure, evaluator-program failure, dependency failure, and some service failures can enter the same Boolean denominator unless task-local code distinguishes them perfectly.

This matters especially for model judges. A VLM timeout, parse failure, inaccessible render, or uncertain view is not evidence that the agent's artifact violated the requirement. `invalid_observer`, `invalid_artifact`, `insufficient_evidence`, and `criterion_fail` need separate terminal states before strict aggregation.

### “Human audited” is authoring provenance, not evaluator validation

The paper says all generated evaluation points are manually reviewed to remove omissions, unsupported assumptions, and duplicates, and every synthesized evaluator is manually audited before use (Sections 4.1–4.2). That is important benchmark-construction labor. But it reports no evaluator-validation sample, agreement statistic, confusion matrix, false-positive/false-negative rate, alternative-valid artifact study, or released audit record.

The missing method details include the number and qualifications of reviewers, assignment and independence, review checklist, test artifacts, blinding, disagreements, adjudication, code execution tests, criterion-by-criterion changes, rejected evaluators, and held-out regression fixtures. Consequently, “human audit” establishes only a reported curation step. It does not estimate criterion accuracy, requirement coverage, generated-code soundness, task-pass accuracy, or robustness to legitimate alternatives and adversarial artifacts.

### The 94% human benchmark is not interpretable as a human ceiling

The abstract, Figure 1, and introduction report 94% human performance and contrast it with Claude Opus 4.6 at 32% and the strongest model, Qwen3.5-Plus, at 41%. The experiment and appendix do not describe how the human number was produced: participant count, recruitment, occupations, task assignment, qualifications, training, interface/tool access, time and turn limits, retries, collaboration, internet use, completion attempts, missingness, evaluator access, or uncertainty are absent. The result is also absent from Table 2's task-family/difficulty breakdown.

Therefore 94% is an unauditable paper-reported reference point—not a population estimate, expert ceiling, matched human–agent comparison, proof of task solvability under the agent condition, or evidence that the evaluator accepts ordinary human alternatives. The 62-point Claude/human gap and 53-point best-model/human gap are descriptive arithmetic over incomparable and underspecified conditions, not calibrated distance to professional competence.

### Closed-loop prompting is not identified self-correction

TOBench's central claim is “closed-loop multimodal verification”: generate, inspect, and revise. Task rules explicitly instruct inspection in examples, and the failure taxonomy includes missing self-verification. That makes the mechanism plausible, but the experiment does not identify it.

A successful endpoint can result from a correct first attempt, inspection-driven revision, repeated generation, or evaluator-aligned artifact shaping. There is no matched factorial separating:

- equal-budget retry without inspection;
- generic “review your work” prompting;
- deterministic consequence-only feedback;
- visual render access without revision authority;
- criterion-level evaluator disclosure;
- self-generated critique from benchmark-evaluator disclosure;
- inspection-disabled execution with the same total tokens/steps/latency.

Nor does the release preserve proposition-level traces showing `observed defect → supported diagnosis → targeted change → criterion-local repair → no collateral regression`. A higher endpoint score can arise from better initial planning, extra tokens, direct instruction decomposition, another attempt, judge-aligned feedback, or actual visual repair. The paper's qualitative trajectory categories do not separate these paths.

TOBench is importantly different from AgencyBench. AgencyBench directly returns observer scores and reasons after failure, measuring oracle-assisted repair. TOBench asks the configured target to inspect artifacts through its own available tools, which is closer to self-review. But absent attempt-level deltas and matched controls, an endpoint pass cannot show that inspection occurred, found a defect, or caused repair. The reported estimand is **configured endpoint conformance with inspection tools available**, not a self-correction effect.

## Evidence and results

The paper reports one main configured run for 19 named model rows—eight closed-source and eleven open-source—over the 100 tasks (Section 5 and Table 2), despite describing these as 15 contemporary models in the abstract and experimental text. The broad result is low performance: even strong configured systems pass only a minority of tasks. Qwen3.5-Plus reaches 41%; the best closed-source rows, Claude Opus 4.6 and Gemini 3 Pro, reach 32%. Performance varies by family, difficulty, tool count, and input/output modality. The paper does not report the planner-condition factorial described in the earlier draft of this review; its closed-loop claim is inferred from task instructions, tool traces/error coding, and endpoint evaluation rather than a controlled planner ablation.

These results credibly support two bounded observations:

1. the selected suites are difficult for the tested configured systems under strict authored evaluators;
2. the reported strongest model score (41%) remains far below the paper's 94% human reference point, although the missing human protocol prevents a matched comparison.

They do not establish a general omni-modal capability scale. The 100 tasks are dependent products of 20 generated slices, tool and modality labels overlap, and difficulty/tool count are not randomized. A task involving more tools also tends to involve more requirements, artifact types, and service exposure. Aggregate correlations and group rates cannot identify which component causes failure.

The paper's failure analysis is directionally useful: models omit requirements, choose inappropriate tools, fail to inspect outputs, mis-handle intermediate artifacts, and stop after superficially plausible creation. But the manuscript does not publish the trajectory sample frame, coder protocol, independent coding, agreement, denominator, multi-label rule, earliest-cause policy, or complete trace corpus. These are authored diagnoses, not prevalence estimates.

No task-level result matrix, replicate data, confidence interval, model/service invalid-run count, cost, latency, or score-building script is released. Percent differences of a few tasks should not be treated as stable rankings. A nominal 100-task single run makes one percentage point equal one task; shared tool/service failures and task-family dependence further reduce effective sample size.

## Unique insight

TOBench's most transferable insight is that **closed-loop benchmark validity requires two independently auditable loops, not one**:

```text
Target loop
public task → tool action → native artifact/state → derived inspection view
→ defect proposition → targeted revision → changed artifact/state

Measurement loop
public/authorized requirement → criterion proposition → admissible evidence view
→ observer result → typed failure/invalidity → task decision → licensed claim
```

The first loop tests whether an agent can improve work after inspecting consequences. The second tests whether the benchmark can validly recognize those consequences. TOBench composes both loops, but the release closes neither evidence chain: target traces and executable task packages are absent, while generated criteria and human audit records are absent.

This creates a distinctive circularity risk. If the target's self-review model and the benchmark's model judge share model families, visual conventions, or criterion language, an artifact can become more judge-legible without becoming more professionally correct. Conversely, a valid artifact can fail because the generated evaluator expects one reference layout or transformation. “Agent inspected it” and “judge accepted it” are not independent witnesses when their models, prompts, or render views overlap.

The correct unit is therefore not only a final task Boolean. It is a linked record:

```text
requirement authority
× criterion/view/observer identity
× target inspection proposition
× revision delta
× criterion-local re-observation
× collateral-state result
× observer validity state
× cost and attempt identity
```

A closed-loop capability claim should require causal evidence that a supported defect proposition changed the relevant artifact and repaired the intended criterion. An evaluator-validity claim should independently test positive, near-miss, alternative-valid, adversarial, corrupt, and observer-failure fixtures. One loop cannot certify the other.

## Comparison with adjacent benchmark evidence

### Workflow-GYM

Workflow-GYM stresses long GUI transitions in professional software and exposes residual-state and stage-bypass problems. TOBench broadens the artifact/tool/modal mix and makes agent-side inspection central, but its tasks are generated rather than practitioner-proposed and its executable suite is unavailable. Both need sparse consequential stage transitions, initial-state canaries, and criterion-view contracts; neither can infer professional workflow validity from a strict final-state score.

### UI-CUBE

UI-CUBE provides deterministic local application-state predicates and fresh containers, making prompt–state–predicate consistency inspectable. TOBench supports far richer native artifacts and live tools, but uses heterogeneous generated evaluators and external services. It therefore gains content breadth while losing observer and environment determinism. UI-CUBE's trial-accounting and release-drift failures apply more strongly here: TOBench releases neither the 100 task packages nor per-attempt records.

### PPT-Eval

PPT-Eval exposes task-specific executable rubric programs over native OOXML, package diffs, renders, and model judgments. It demonstrates that plural artifact views require frozen transformations, typed observer failures, alternative fixtures, and noncompensatory completion semantics. TOBench generalizes the same architecture across many artifact types but releases only a reference evaluator, not the realized 100 evaluator programs. Its evaluator-validity claim is therefore less inspectable.

### AgencyBench

AgencyBench preserves evaluator-derived feedback and revised attempts, making feedback leakage directly auditable. TOBench instead asks the target to inspect through its own tools rather than explicitly feeding benchmark judge reasons back. That is a cleaner conceptual separation, but absent released traces and matched controls, the repair mechanism remains unidentified. Both should report first attempt, retry-only gain, generic-review gain, consequence-feedback gain, criterion-disclosure gain, and collateral regressions separately.

## Limitations and validity threats

### Task content, generation, and expertise

- Two macro families and 20 generated slices are designed breadth, not occupational or user-demand sampling.
- No observed-work source, stakeholder, author qualification, role-to-task assignment, frequency/consequence weight, or rejected-candidate ledger supports “real-world” or “professional” generalization.
- Model-generated roles and domain rules can create benchmark-shaped exact obligations rather than authentic ambiguity or recipient utility.
- Final selection from roughly 600 candidates to 100 is opaque and likely favors asset availability, tool feasibility, and grader expressibility.
- Difficulty is authored and bundles requirement count, ambiguity, horizon, modality, and tool/service exposure.
- The release's two different 600-candidate stores and naming drift make generation lineage unclear.

### Construct and configured-system validity

- “Omni-modal tool use” bundles perception, planning, tool discovery, API schema interpretation, external retrieval, artifact manipulation, rendering, self-review, and stopping.
- Model rows identify configured model–prompt–runtime–tool–endpoint packages, not base-model effects.
- Endpoint scores do not reveal how much success came from first-pass generation versus inspection-driven repair.
- Tool count is neither capability dimensionality nor experimentally isolated complexity.
- Strict all-criteria pass measures authored contract conformance, not downstream usefulness, safe handling, or professional acceptance.

### Evaluator validity

- Realized task criteria and generated evaluator programs are unreleased.
- A reference workspace is a solvability/example witness, not a complete equivalence class.
- No requirement-to-criterion coverage audit or no-hidden-obligation audit is published.
- No alternative-valid, near-miss, adversarial, prompt-injection, corrupt-artifact, or observer-failure fixture suite is reported.
- Model, native, rendered, trajectory, and external-result views have different authority but are collapsed into binary criteria.
- Nonzero evaluator process status can collapse criterion and infrastructure failure.
- Reported manual review/audit has no released protocol or outcome records and cannot be promoted to task-level evaluator accuracy.
- Strict conjunction magnifies criterion false negatives and criterion-count differences.

### Experimental and statistical validity

- No repeated independent runs, confidence intervals, task-cluster analysis, or paired pre/post-inspection transition table is reported.
- The task is the nominal unit, but tasks share generators, subcategories, servers, assets, evaluator templates, and service outages.
- No matched-budget/no-feedback/generic-review/inspection-access factorial identifies closed-loop correction.
- Difficulty, tool count, and modality analyses are observational and heavily confounded.
- Failure coding lacks a released codebook, sampling frame, agreement, and denominators.
- Missing, timed-out, service-invalid, artifact-invalid, observer-invalid, and scored attempts are not reconciled.

### Reproducibility and operational realism

Positive release evidence includes an MIT license, pinned runner, 27 MCP configuration files, broad local server code, generation prompts, 1,200 candidate specifications across two stores, reference evaluator helpers, and a workspace-reset path. Static inspection is meaningful.

Exact reproduction is not possible from the inspected release:

1. no `tasks/` tree or `task_config.json` exists in the GitHub archive;
2. the linked Hugging Face dataset returned HTTP 401 to an unauthenticated API request on 19 July 2026;
3. no final 100-task manifest, source assets, initial/ground-truth workspaces, criteria, generated evaluator programs, or human-attempt records are present;
4. no paper-run traces, artifacts, criterion vectors, invalid-run ledger, human protocol, or table builder is present;
5. no exact experimental commit, model endpoint snapshots, run dates, complete configs, or cost/latency ledger is bound to the paper;
6. paper and pinned release tool totals differ (324 versus 333);
7. external search, maps, finance, media, model, and web services can drift or require credentials;
8. process and network containment are configured but not conformance-tested;
9. resume can preserve workspace state unless attempt identity records the policy; and
10. generated evaluators expand the trusted computing base without released task-level tests.

Operational realism is strongest at the artifact/tool composition layer and weakest at organizational consequence. The environment can exercise genuine editing, retrieval, conversion, and visual inspection. It does not reproduce permissions, customer accountability, stakeholder clarification, approval, audit, collaboration, service-level obligations, or real recipient use.

## Transfer to `skill-bench`

### Retain

1. **Inspection-capable artifact work.** Require agents to derive admissible views of their own native outputs when the task construct includes self-review.
2. **Cross-tool composition.** Include tasks where evidence must move between retrieval, analysis, and artifact-production tools rather than reward isolated API calls.
3. **Task-local criteria.** Bind each task to explicit format, content, provenance, tool/result, preservation, and safety propositions.
4. **Native plus derived evidence.** Preserve native bytes/state separately from render, transcription, extraction, screenshots, and model observations.
5. **Strict mandatory gates.** Do not compensate away hidden requirements, safety constraints, invalid artifacts, or delivery failures.

### Repair

1. **Separate the two loops.** Record target self-inspection and benchmark evaluation as different evidence chains with independently versioned models, prompts, views, and propositions.
2. **Compile with proof obligations.** Every generated criterion/evaluator must link to public authority, admissible view, polarity, applicability, tolerance, dependencies, and positive/near-miss/alternative/observer-failure fixtures.
3. **Type invalidity before aggregation.** Preserve `criterion_fail`, `invalid_artifact`, `insufficient_evidence`, `observer_invalid`, `environment_invalid`, and `service_invalid` separately.
4. **Identify correction causally.** Keep first attempt, equal-budget retry, generic review, consequence-only feedback, criterion disclosure, and ecological expert feedback as distinct conditions.
5. **Record proposition-level repair.** Link observed defect, evidence locator, diagnosis, revision delta, criterion-local recheck, new defect, and cost.
6. **Bind the release.** Hash task instruction, source pack, initial state, tools, server code/images, criteria, evaluator program, transformations, models, self-review policy, and score builder in one manifest.
7. **Audit tool realization.** Maintain declared-versus-connected-versus-called tool inventories and conformance tests; endpoint count alone is not coverage.
8. **Prove reset and containment.** Run absence/presence canaries, protected-state hashes, external-effect ledgers, and filesystem/network boundary tests.

### Test

Use a small cross-domain pilot with the same initial artifact and agent first attempt, then randomly assign the repair opportunity:

- no second attempt;
- equal-budget retry with no new information;
- generic self-review;
- render/native-view access with no criterion hints;
- consequence-only feedback from an admissible deterministic observer;
- criterion-level evaluator disclosure;
- authorized expert/user feedback where available.

Measure criterion-local repairs, unchanged failures, collateral regressions, new defects, observer invalidity, endpoint acceptance, time/tokens/cost, and reviewer burden. Cross target self-review and evaluator model families where possible to detect shared-judge alignment. This tests TOBench's general closed-loop hypothesis without narrowing `skill-bench` to one modality or tool stack.

## Concrete repository actions

1. **No duplicate queue task added.** The required fields and experiments already have homes in the completed artifact-view, task-projection, evaluator-assurance, feedback/recovery, configured-system, trial-ledger, and persistent-workspace machinery.
2. Use TOBench as a future conformance case for generated evaluators: require requirement coverage, no hidden obligations, alternative-valid fixtures, observer-failure typing, and process-versus-criterion failure separation.
3. In the next cross-domain repair pilot, include a self-inspection arm and explicitly distinguish it from AgencyBench-style evaluator disclosure.
4. Do not import TOBench scores or “real-world,” “professional,” “self-correction,” evaluator-accuracy, human-parity, or readiness claims into canonical benchmark evidence until an immutable release exposes the 100 task packages, realized evaluator programs, attempt ledger, traces/artifacts, human protocol/attempts, audit records, and table reconstruction.

## Bottom line

TOBench chooses an important target: agents should produce multimodal work through real tools, inspect the consequences, and repair failures. Its broad MCP/artifact architecture and generated task-local evaluator pipeline are valuable design evidence. The strongest lesson, however, is not that the endpoint scores demonstrate self-correction. It is that closed-loop capability and closed-loop measurement are separate systems, each requiring its own provenance, evidence views, interventions, failure states, and validation.

The unreleased executable suite, opaque 600-to-100 selection, divergent candidate stores, paper/release tool-count drift, absent evaluator programs and run records, undescribed 94% human benchmark, undocumented human-audit process, Boolean failure collapse, and uncontrolled inspection mechanism sharply bound the claim. Retain inspection-capable artifact work and cross-tool composition; repair task provenance, evaluator compilation assurance, release closure, trial accounting, and causal repair measurement before treating endpoint scores as evidence of autonomous real-world knowledge work.