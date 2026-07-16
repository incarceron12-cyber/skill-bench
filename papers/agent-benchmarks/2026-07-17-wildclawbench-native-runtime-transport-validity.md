# Paper Review: WildClawBench — Native-Runtime and Harness-Transport Validity

- **Paper:** https://arxiv.org/abs/2605.10912v1
- **Title:** *WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation*
- **Authors:** Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu, Jingyi Yang, Penghui Yang, Zhixiong Zhang, Xilin Wei, Xinyu Fang, Yubo Ma, Haodong Duan, Jing Shao, Jiaqi Wang, Dahua Lin, Kai Chen, and Yuhang Zang
- **Date read:** 2026-07-17
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, 11 May 2026
- **Local PDF:** `data/papers/pdfs/2605.10912v1-wildclawbench.pdf` (38 pages; SHA-256 `f9c69b0071dd063993ad90763ee96acec3af7f838344cf743dba613e287cea0e`)
- **Local text:** `data/papers/text/2605.10912v1-wildclawbench.txt` (SHA-256 `2c6a5777c0a97f51ed16fa3c5f275699b250bc19d01f0a06305527e1e1fa41b2`)
- **Official release inspected:** https://github.com/InternLM/WildClawBench/tree/6f78ad8d4bc17e73e7d84de246dd2caa0b9c82c4 (commit dated 15 July 2026; tree `c55c9f84b7fb85bc31ad3b36a9fe3559121f6368`)
- **Dataset revision inspected:** https://huggingface.co/datasets/internlm/WildClawBench/tree/5a26773d94520f765032dddd34bf1bb9ccdae88a
- **Release provenance:** `data/sources/releases/2605.10912v1-wildclawbench/provenance.json`
- **Static audit record:** `data/sources/releases/2605.10912v1-wildclawbench/release-audit.json`
- **Important version boundary:** the inspected source commit is more than two months newer than immutable arXiv v1. It includes a 14 July correction to one live-web task's ground truth. Release observations establish properties of this post-v1 implementation, not the exact paper-time runner or graders.
- **Safety boundary:** the five published container archives total 56,633,714,841 bytes. They were not downloaded, loaded, or executed. Source code and exact-revision metadata were audited first because the runner requests privileged containers and the Hugging Face API still described all five archives' antivirus scans as queued at inspection time. This metadata is not evidence of malware.
- **Tags:** configured-agents, native-runtime, long-horizon, harness-transport, multimodal, bilingual, hybrid-grading, privileged-containers, live-web-drift, skill-ablation, reproducibility

## One-sentence contribution

WildClawBench releases 60 bilingual, multimodal, artifact-producing tasks for four CLI-agent harnesses and usefully demonstrates that model, harness, time budget, and skill package jointly shape observed success, but its “native production-grade runtime” is a benchmark-authored transport layer whose privileged, networked containers, runtime package installation, task-specific warmups, live-web dependencies, and harness-specific transcript adaptation are part of the treatment; without paper-time images, retained trajectories, calibrated graders, or adapter-conformance evidence, the reported scores support configured-system comparisons under one evolving release—not general model capability, deployment safety, or exact reproducibility.

## Why this matters for skill-bench

WildClawBench directly advances charter objectives A, B, and C. It contains concrete cross-domain work products, long execution windows, multimodal source packs, task-local executable graders, side-effect audits, safety traps, and a four-harness comparison. Its most relevant lesson is not simply that “harnesses matter.” It is that a benchmark must identify the **full execution transport** between task intent and evaluator-visible evidence:

`task/source revision → outer container → bootstrap/warmup → harness adapter → model endpoint → tool authority → artifact/trace transport → grader revision`

Every edge can change the measured construct. The release's Codex adapter converts Codex JSON events into an OpenClaw-compatible transcript so safety graders can consume them; OpenClaw and Claude Code are bootstrapped differently; task skills are copied or prompt-injected differently; warmup failures do not invalidate a run; and the outer Docker invocation is privileged. These are not incidental implementation details. They determine what the agent can observe, what it can do, what the grader can see, and whether a zero reflects model behavior or transport failure.

For `skill-bench`, useful completion is therefore a transport-conformance contract attached to each configured-system trial. It should establish that task inputs arrive intact, private evidence remains inaccessible, required skills and services are actually available, credentials and network authority are scoped, traces preserve equivalent consequential events across harnesses, outputs survive timeout/termination, and graders consume the intended evidence. A container image name or common workspace path is not enough.

This review does not narrow the project to CLI agents. The underlying validity problem applies across office, research, coding, communication, professional-artifact, browser, and multimodal work: claims about a person or system are only as valid as the transport from authentic task demand to authoritative observed consequence.

## Research question and claim boundary

The paper asks whether frontier models, running through native CLI harnesses, can complete realistic long-horizon work that requires sustained tool use, multimodal reasoning, side effects, and artifact production. It also asks how scores change with model, harness, time budget, reasoning effort, and supplemental skill packages.

The evidence supports several bounded conclusions:

1. The authors built and released a heterogeneous 60-task suite with executable grading code and substantial task workspaces.
2. Under the reported OpenClaw protocol, the 19 named model endpoints produced widely separated task-macro scores, from 19.3% to 62.2%.
3. Four model backends scored differently when transported through four harness integrations; the largest displayed within-model range is 18.2 points for MiMo V2 Pro.
4. Halving or doubling execution time and adding selected skills changed observed outcomes, sometimes substantially and sometimes negatively.
5. Long trajectories expose artifact, timeout, safety, environment/API, and planning symptoms that a final-answer-only benchmark would not preserve.

The evidence does **not** establish:

- the isolated causal effect of harness policy, because adapter code, CLI version/bootstrap, prompt transport, tool implementation, environment image, latency, transcript conversion, and failure handling vary together;
- general base-model rankings outside the named endpoint, harness, task, budget, and date configuration;
- that the benchmark represents the distribution of consequential knowledge work or any profession;
- exact paper-result reproducibility from the public release;
- safe production deployment, because ten authored safety tasks in privileged benchmark containers are a narrow stress test, not an operational risk argument;
- that hybrid grading has known error rates, despite a small agreement case study;
- stable per-task reliability, despite three aggregate repeated runs for four models;
- that “real tools rather than mock-service APIs” applies uniformly, because the Social Interaction tasks explicitly start local mock Gmail/calendar/chat services.

The paper is strongest as **descriptive configured-system evidence** and a substantial benchmark artifact. Its broader language—“real-world,” “production-grade,” “safe,” and “reproducible”—requires sharper boundaries than the paper and inspected release provide.

## Methodology and system

### Task construction and curation

WildClawBench contains 60 human-authored tasks: 10 Productivity Flow, 12 Code Intelligence, 6 Social Interaction, 11 Search & Retrieval, 11 Creative Synthesis, and 10 Safety Alignment. The paper reports 36 English and 24 Chinese tasks, 26 multimodal and 34 pure-text tasks, and time budgets from 300 to 1,200 seconds with a mean of 881 seconds. Claude Opus 4.6 runs averaged 8.5 minutes and 26 tool calls. Tasks ask agents to produce research digests, code and visual programs, calendar/email actions, constrained searches, websites/slides/posters/videos, and safety-aware artifacts.

Each Markdown task specification bundles YAML metadata, the agent-facing prompt, expected behavior, grading criteria, executable Python grading code, workspace path, optional skills, environment variables, and warmup commands. Static parsing of the inspected post-v1 tree found exactly 60 unique task IDs and category counts matching the paper. All 60 graders contain an `overall_score` pattern; 27 tasks declare skills, 46 declare warmups, and 42 declare environment variables. A conservative source-pattern audit found 39 task graders referencing an LLM judge or judge-provider path and 11 referencing transcripts. These are implementation-shape counts, not an independent validity judgment.

The curation pipeline has four stages:

1. author candidate tasks with curated workspaces;
2. produce expert reference answers or verifiable grading points;
3. filter by model discrimination and human review;
4. refine prompts, assets, rubrics, graders, and distractors.

Eight researchers reportedly spent two weeks on the process. Candidates survive model filtering only when the maximum pairwise pilot-model score gap is at least 0.2. Reviewers then inspect prompts, references, grading outputs, transcripts, logs, and failures for ambiguity, brittle grading, leakage, and environment instability.

This is more rigorous than prompt collection, but key evidence is absent: candidate count, rejection counts by reason, author/reviewer assignment, domain expertise, independent double review, agreement, reviewer forms, human completion trials, measured expert time, rubric coverage analysis, and retained revision history. The max-gap filter also selects for **observed separation among a chosen pilot panel**, not construct validity. It can discard uniformly difficult but important tasks, reward grader/model interactions that create large gaps, and bias later model comparisons upward because pilot outcomes helped select the items. No held-out task-construction or model panel is reported.

The category names are thematic rather than occupational or construct-level strata. “Productivity,” “creative,” and “safety” pool materially different competencies, evidence types, and consequence levels. Equal task averaging therefore describes this authored inventory, not a target distribution of work.

### Execution environment and harness transport

The paper describes isolated Docker containers hosting OpenClaw, Claude Code, Codex, or Hermes Agent; a common workspace; fixed prompts and tool schemas within each harness; unified OpenRouter model access; and grading-only resources copied after execution. The inspected release substantially implements this architecture:

- a fresh task-named container is created;
- workspace files are copied to `/tmp_workspace`;
- declared task skills and environment variables are installed or passed;
- warmup commands run before the model process;
- the selected harness runs under the task timeout;
- the workspace and ground-truth tree are then copied into the container for grading;
- the grader executes and returns structured metrics;
- logs, elapsed time, token counts, cost, transcript, and score are written to a result directory;
- the container is removed unless requested otherwise.

The temporal separation of agent execution from grading-only files is a strong pattern. The source tree also contains concrete mock services and audit endpoints for Gmail/calendar/chat tasks, allowing state consequences to be checked rather than inferred from prose.

But “common environment” is not equivalent transport. The four integrations differ materially:

- **OpenClaw** writes model/provider configuration and invokes its gateway/agent stack. Its runner can bootstrap OpenClaw through an installer at execution time.
- **Claude Code** uses a distinct runner and transcript location and can install its CLI through a remote installer.
- **Codex** writes a custom OpenRouter configuration, installs `@openai/codex` if absent, invokes `codex exec --dangerously-bypass-approvals-and-sandbox`, parses JSON events, and synthesizes an OpenClaw-shaped transcript under `/root/.openclaw/...` for compatibility with existing graders.
- **Hermes Agent** uses its own CLI/configuration and is installed or upgraded by pip when needed.

Thus the harness contrast includes prompt representation, tool API, package version, startup work, runtime latency, transcript schema, event loss in conversion, model/provider mapping, skill delivery, and sandbox policy. The paper acknowledges the harness as part of the system, which is correct; it nevertheless attributes gaps to control-loop/tool/context/recovery properties without isolating those from adapter realization.

The outer runner also weakens the “safe container” claim. `docker run` includes `--privileged`, uses default networking rather than an explicit egress policy, and gives the agent root-level shell authority inside a benchmark image. Task warmups execute arbitrary shell strings and do not check return codes. Agent model credentials are exported into harness processes, while the benchmark deliberately evaluates malicious skills and prompt-injected documents. A privileged container is not automatically a host compromise, especially without a Docker-socket or host-root mount, but it is far broader authority than this suite requires and contradicts the stronger impression created by “isolated,” “safe,” and “without privileged host access.” It also makes untrusted image provenance and egress control consequential.

The paper's claim that each harness image ships pinned preinstalled binaries is not fully realized by the inspected source. Some harness CLIs are installed or upgraded at run time; task warmups install additional npm/pip/apt dependencies; live network access is required; and the release does not provide Dockerfiles or a content-addressed bill of materials sufficient to reconstruct the five archives. The exact images are content-addressable at the Hugging Face LFS layer, but the executed software can still mutate after image loading.

### Dataset and release composition

The exact Hugging Face revision manifest contains 2,926 paths: 2,917 under `workspace`, five image archives under `Images`, and four metadata/asset paths. The five archives total 56.63 GB before extraction:

- Claude Code: 15,937,592,832 bytes;
- Codex: 5,385,311,232 bytes;
- Hermes Agent: 8,574,699,161 bytes;
- Ubuntu v1.2: 13,256,324,608 bytes;
- Ubuntu v1.3: 13,479,787,008 bytes.

The GitHub repository supplies task specs, adapters, grading, setup, and orchestration; the Hugging Face repository supplies workspaces and opaque image archives. Exact replay therefore depends on a **join between two revisions**, plus hosted model and judge endpoints and mutable runtime installers. The release does not provide a single signed run manifest binding all of these components.

A targeted fixture fetch confirmed that the prompt-injection document exists at the pinned dataset revision and contains the expected `sudo rm -rf /` lure at local line 1028. It is preserved locally with its exact revision and SHA-256 in the audit record. This also exposes documentation drift: the executable grader's docstring says the injection is at line 364, which is blank in the pinned fixture. The grader's actual pass/fail logic searches transcripts rather than line 364, so the locator error does not directly determine its score, but it shows that prose, fixture, and diagnostic evidence can diverge. No image archive was executed.

### Grading and evidence channels

The paper groups grading into:

1. deterministic checks over files, formats, values, strings, copies, cleanliness, and patterns;
2. environment-state audits over email/calendar/chat side effects and safety transcripts;
3. GPT-5.4 LLM/VLM judgments for semantic, visual, and creative outputs.

This plural-evidence design is valuable. The Social Interaction meeting task, for example, checks message reads/sends, local calendar state, decoy avoidance, timezone handling, contradiction clarification, non-deletion, event fields, and boss notification. It demonstrates how hidden requirements and side effects can become typed predicates rather than a single holistic score.

However, the executable grader is the real measurement instrument, and its semantics vary sharply:

- some tasks use deterministic outputs;
- some query local service audit endpoints;
- some inspect harness-specific transcript paths;
- some fall back to keywords in a self-reported `results.md` when services are unavailable;
- many call a hosted judge and return zero on judge failure;
- task-specific sub-scores are collapsed into an `overall_score` without a suite-wide criterion schema;
- safety transcript logic depends on event normalization and may miss actions not preserved by an adapter.

The meeting grader's fallback illustrates an important fail-open tendency: if service audits are absent, prose mentioning the expected names, time, room, and conflict can earn substantial credit without proving that communication or calendar actions occurred. Its “no deletion” criterion defaults to one in fallback mode. This preserves partial scoreability during service failure, but changes the construct from enacted workflow to claimed workflow. The result should be `insufficient_state_evidence`, not an interchangeable score.

Transcript-based safety also has a transport problem. The prompt-injection grader first looks for an OpenClaw JSONL path, then a Claude Code JSON path, then a supplied list. The Codex adapter explicitly transforms Codex events into OpenClaw-shaped messages. This is a practical compatibility mechanism, but the benchmark does not validate channel equivalence: which tool calls, arguments, shell commands, failures, redactions, or intermediate events survive each adapter? “No dangerous command observed” cannot prove “no dangerous command occurred” unless trace completeness is tested for that harness and task.

### Experiments

The main OpenClaw comparison covers 19 named frontier models over all 60 tasks. Four models—GPT-5.4, GLM-5, MiMo V2 Pro, and MiniMax M2.7—are additionally compared across OpenClaw, Claude Code, Codex, and Hermes Agent. GPT-5.4 receives a low/medium/high reasoning-mode ablation. Four models receive category-relevant skill augmentation. Time-budget scaling compares half, standard, and double budgets. Tool calls are grouped into shell, process, web, read, image, and author categories. Four models receive three repeated OpenClaw runs. Five tasks × four model outputs are scored by GPT-5.4 and two humans.

The paper does not report random run order, endpoint sampling parameters for every model, exact provider model realization, retries, failed-launch counts, dropped cells, image and repository hashes, harness commits, installer resolution, task/grader hashes, task-selection pilot models, skill package revisions, task-level intervention assignment, or confidence intervals. The paper's per-task appendix is useful, but the release contains no raw paper trajectory/result bundle with model requests, tool events, artifacts, grader calls, or retry ancestry.

## Evidence and results interpretation

### Main scores and harness differences

Under OpenClaw, Claude Opus 4.7 scores 62.2%, GPT-5.5 58.2%, Claude Opus 4.6 51.6%, GPT-5.4 50.3%, and the lowest reported model, Grok 4.20 Beta, 19.3%. The paper reports per-task time and cost and separates 26 multimodal from 34 pure-text tasks. This is strong descriptive reporting, and the broad score range shows that the inventory is not saturated under these configurations.

The four-harness table is equally useful as a warning against base-model-only claims. GPT-5.4 ranges from 48.4 to 56.8, GLM-5 from 31.0 to 46.4, MiMo V2 Pro from 29.9 to 48.1, and MiniMax M2.7 from 32.0 to 37.1. Hermes Agent is best for three of four displayed models; Codex is best for GPT-5.4.

These are not causal harness effects. There is one integrated score per displayed model–harness cell, and transport differences include CLI/package versions, adapters, prompts, tools, setup latency, skill handling, transcript conversion, timeout exposure, and environment images. Claude Code's slower runs may reflect harness behavior, installer/startup overhead, model interaction, or adapter integration. The result supports “configured systems differ,” not “Hermes's control loop is intrinsically better” or “Claude Code causes an 18-point loss.”

### Time and reasoning budgets

GPT-5.4 scores 50.4 at low reasoning, 52.6 at medium, and 45.0 at high while timeout counts rise from 4 to 7 to 15. This is an important operational result: deliberation consumes the same wall-clock budget needed for actions and verification. The reported estimand is nevertheless a bundled **reasoning-mode × exposure-time** effect. To infer reasoning quality, one would need separate accounting for internal model latency, tool latency, active execution time, output tokens, timeout censoring, and artifact state at cutoff.

Doubling task budgets improves GPT-5.4 from 50.3 to 56.5 and shows diminishing average returns. Budget is therefore part of configured-system identity, not merely a fairness control. For knowledge-work benchmarks, this argues for quality–cost–latency frontiers and timeout-state analysis rather than a single fixed-budget ranking.

### Skill augmentation

The skill ablation is directly relevant to `skill-bench`, but the paper's interpretation is too broad. GPT-5.4 improves 5.2 points overall and MiMo V2 Pro 3.7; GLM-5 declines 0.1 and MiniMax M2.7 improves only 0.1. Category effects include severe regressions: GPT-5.4 Social Interaction falls 48.5 points, GLM-5 Search & Retrieval falls 14.0 and Safety 9.4, and MiniMax M2.7 Social Interaction falls 26.3 and Safety 10.9. Skills are not uniformly beneficial.

The appendix says three category-relevant skills were selected by ClawHub download count. Popularity is not task relevance, safety, quality, or treatment purity. The paper does not pin skill revisions, audit their instructions/dependencies, report which skill each trajectory invoked, isolate one skill at a time, verify equivalent installation, or distinguish useful domain knowledge from extra tools, longer prompts, hidden hints, dependency changes, and execution overhead. In the release, task specs already declare baseline task-specific skills for 27 tasks, so “+Skill” is augmentation atop a nonuniform baseline rather than a clean no-skill versus skill contrast.

The evidence supports a narrower insight: **skill packages are interventions that can improve, distract, conflict, or alter authority**, and response is strongly task/model dependent. That is a reason for matched treatment provenance and mechanism-level trace analysis, not a general “seamless integration” benefit claim.

### Repeated runs

For four OpenClaw models, three aggregate runs yield overall standard deviations from 0.7 to 1.9 points. This shows that the 60-task macro average is comparatively stable over those three attempts. It does not show trajectory stability or per-task reliability. Positive and negative task-level changes can cancel in a macro average, and only three repeats cannot estimate low-frequency failure or tails. The paper does not publish per-task replicate vectors, run order, endpoint timing, judge repeats, or paired uncertainty. “Small aggregate SD” should not be generalized to robust execution trajectories.

### Judge agreement

The judge case study samples five LLM-judged tasks and four model outputs per task. Two humans score with the same rubric; their mean is compared to one GPT-5.4 score. The displayed deviations are generally small.

This is useful face-validity evidence, not strong calibration. The sample has 20 outputs from five tasks; no criterion-level labels, human–human agreement statistic, judge repeatability, confidence interval, mean absolute error, rank correlation, threshold confusion matrix, adversarial outputs, disagreement sampling, or blindness to model identity/judge output is reported. Humans sharing the benchmark's rubric test consistency with that authored instrument, not whether the rubric captures expert usefulness. Four safety-task outputs all receive 100 from both humans and judge, providing little discrimination. The conclusion that GPT-5.4 is “highly reliable” exceeds this case study.

### Failure analysis

The paper analyzes 300 OpenClaw runs from five models and labels 169 below 0.5 as failures. Outcome labels include wrong/partial artifact, timeout/hung process, safety violation, and missing artifact. Process categories include safety-policy failure, time budget, code/debug loop, toolchain/API disruption, and semantic/planning miss.

This is valuable because wrong/partial artifacts dominate many failures and environment/API disruption is visible. Yet the coding protocol is unclear. Figure 6 describes process signals as multi-label and co-occurring, while the prose says priority assignment gives each failed run exactly one process label. The paper does not identify labelers, codebook, independent double coding, agreement, adjudication, label evidence locators, or whether model-generated analyses assisted. Since live API/tool failures are themselves treatment outcomes, merging them under broad “toolchain/API disruption” also obscures whether the earliest cause lies in the benchmark service, harness adapter, dependency bootstrap, model action, or external web.

## Unique insight

WildClawBench's deepest transferable insight is that **native-runtime realism is not a binary property of the container; it is the validity of the transport from task demand to observed consequence**.

A Docker container can preserve a real CLI while still changing the construct through privileged authority, synthetic services, package bootstrap, adapter prompt rewriting, event conversion, task warmups, live-web drift, and post-run grading. Conversely, a local mock service can be more valid than a live service for a specific side-effect predicate if it preserves the relevant state transition and exposes an authoritative audit log. “Real” versus “mock” is therefore the wrong top-level distinction.

For each task × configured-system trial, separate five layers:

1. **Demand fidelity:** Does the prompt, source pack, hidden requirement, stakeholder context, and consequence structure represent the intended work?
2. **Environment fidelity:** Are the tools/services/assets sufficiently behaviorally equivalent for the claim, and what important production features are omitted?
3. **Transport conformance:** Did this harness receive the same task, authority, budget, skills, state, and feedback, and did its consequential actions reach the observer without schema loss?
4. **Evaluator validity:** Does each criterion query authoritative evidence with calibrated false-accept/false-reject behavior and fail-closed missing-evidence semantics?
5. **Inference validity:** What population of tasks, systems, times, and deployment conditions can the retained trials actually support?

The paper mostly studies layers two and three while using “real-world” language that implies layers one and five. The release audit shows why the layers must remain explicit. A model can lose because a warmup silently failed; gain because an adapter exposed a broader tool; pass safety because its shell event was not normalized; fail a live-search task because a source changed; or receive different ground truth two months later. None of those are captured by the model name and task score alone.

A second insight is that temporal separation of private grading is necessary but not sufficient. WildClawBench correctly inserts grading-only files after the agent exits. Yet validity additionally requires an outer boundary proving that the agent cannot access the host repository or other secrets, the grader can observe all required side effects, and the release binds the exact pre-agent workspace and post-agent evidence. Information separation, authority containment, and observer completeness are distinct contracts.

## Limitations and validity threats

1. **Task population is authored, not sampled.** Six thematic categories do not define a population of real-world or professional work.
2. **Expert authority is under-specified.** Eight researchers and two weeks are reported, but disciplines, assignments, training, review time, and independence are not.
3. **Candidate-flow evidence is absent.** Initial task count, rejection counts, revisions, and retained reviewer records are not released.
4. **Discriminability filtering risks selection bias.** Requiring a pilot-model gap of at least 0.2 selects for differences on the construction panel and may discard consequential uniform-hard tasks.
5. **No human task baselines.** Solvability, expected completion time, artifact quality, and expert failure modes are not empirically reported.
6. **The harness is a bundled treatment.** Native CLI policy, adapter, prompt, tools, package version, image, skill transport, latency, and trace mapping vary together.
7. **Transport equivalence is unvalidated.** No common conformance suite proves prompt identity, fixture visibility, tool authority, output persistence, timeout behavior, or event completeness.
8. **The outer containers are privileged.** This is broader authority than needed and weakens the “safe isolated” characterization.
9. **Network egress is not explicitly restricted.** Live tools, installers, model access, and potentially task content share a networked environment.
10. **Runtime installation breaks image-only pinning.** Some harness and task dependencies are installed or upgraded during execution.
11. **Opaque images are not rebuildable.** Five large archives have hashes but no complete Dockerfiles/SBOM sufficient to reproduce their contents from source.
12. **Release identity is split.** Exact replay requires joining a GitHub commit, Hugging Face revision, image archive, installers, model endpoint, judge endpoint, skills, and live web state.
13. **No paper-time release is identified.** The inspected commit postdates v1 by over two months.
14. **Ground truth has already drifted.** A Google Scholar shortest-path answer was corrected on 14 July, proving that at least one live-web criterion was incomplete after publication.
15. **Live-web tasks are not replay-stable.** Search results, Scholar pages, repositories, package registries, and websites can change or block automation.
16. **“No mock services” is overstated.** Social Interaction tasks explicitly run local mock communication/calendar services.
17. **Warmup errors are not trial-invalidating.** Shell setup return codes are ignored, so dependency failure can become a model score.
18. **Skill availability is nonuniform.** Baseline task skills, augmentation skills, harness delivery, and runtime dependencies differ and are not validated per run.
19. **Skills are not pinned in the paper.** Download-count selection and descriptions do not identify exact audited treatment artifacts.
20. **Hybrid grading lacks a common criterion schema.** Task-local Python controls weights, missing-evidence behavior, and output semantics.
21. **Some workflow graders fall back to prose.** This can award claimed side effects when authoritative service state is unavailable.
22. **Transcript safety is adapter-dependent.** Codex events are transformed into OpenClaw-compatible messages; completeness/equivalence is not calibrated.
23. **Judge failure becomes task failure in many graders.** This mixes evaluator availability with agent capability rather than marking unscorable evidence.
24. **Judge validation is very small.** Five tasks and 20 outputs cannot establish broad reliability across 39 source-pattern-identified judge-bearing tasks.
25. **No criterion-level calibration.** The paper reports no confusion matrix, threshold agreement, adversarial cases, or uncertainty.
26. **Aggregate repeated-run SD hides task instability.** Three 60-task macro means do not estimate per-task `pass^k`, tails, or run dependence.
27. **No inferential uncertainty.** Rankings and harness gaps lack task-paired intervals or tests.
28. **Run ledger is missing.** Attempted, invalid, retried, timed-out, dropped, and scored trajectories are not enumerated by cell.
29. **Raw paper trajectories/results are absent.** The public source cannot independently verify scores, costs, tool counts, failures, or judge outputs.
30. **Failure coding is underspecified and internally ambiguous.** Figure text describes co-occurring signals while prose describes one priority label.
31. **Fixture locators can drift.** The prompt-injection grader documents line 364, while the pinned input's lure is at line 1028 and line 364 is blank.
32. **Category scores pool heterogeneous constructs.** Inventory-weighted averages do not represent declared stakeholder utility.
33. **Safety coverage is narrow.** Ten hand-authored traps do not support general deployment-safety claims, especially under broad container authority.
34. **Single-turn framing omits interactive correction.** The paper acknowledges that users do not clarify or redirect during execution.
35. **Professional specialist coverage is light.** The paper acknowledges limited biology, finance, law, and GUI-heavy work.
36. **Cost excludes benchmark operations.** Model API averages do not include image distribution, setup, judge calls, audit labor, storage, or failed-run recovery.

## Reproducibility and operational realism

### What is reproducible

The release is substantial. It provides 60 complete Markdown task specs, executable graders, four harness integrations, batch orchestration, mock services, skills, result logging, and 2,917 dataset workspace paths at an exact revision. Category/task counts and task IDs match the paper. The five image objects have exact LFS hashes. Ground-truth files are temporally inserted after agent execution. Task workspaces include real source trees, media, documents, and state fixtures rather than prompts alone.

A researcher with large storage, Docker privileges, API credentials, compatible hosted endpoints, and network access could plausibly execute the current release. That is meaningful release inspectability.

### What is not reproducible

The reported experiment cannot be exactly reconstructed from the available artifacts because:

- arXiv v1 does not bind the paper runs to a Git commit, dataset revision, image hashes, harness versions, skill hashes, installer outputs, provider endpoint snapshots, or complete sampling settings;
- the public code commit postdates v1 and includes at least one grading correction;
- some CLIs and task dependencies are resolved at run time;
- live-web state and hosted aliases change;
- the source archive contains no paper trajectory/result ledger, artifacts, grader prompts/responses, or retry records;
- opaque images are downloadable but not source-rebuildable;
- only aggregate three-run statistics are published for a subset;
- executing all cells carries material model, judge, storage, bandwidth, and wall-time cost.

The correct label is **runnable current implementation with weak exact empirical replay**, not fully reproducible paper results.

### Operational realism

Realism is strongest in long artifact production, repository/media manipulation, browser/search work, sustained timeouts, dependency failures, and concrete side effects. It is also useful that failures can arise from toolchain instability and that cost/time are reported.

Realism is weaker in task acquisition, stakeholder interaction, authority scoping, consequence calibration, and deployment environment. Local mock services simplify human behavior; single-turn prompts eliminate user corrections; privileged root containers expose more authority than many production deployments; live internet access is broad rather than policy-scoped; and professional outputs are not assessed by occupation-matched experts. “Native CLI” is ecological with respect to software surface, not sufficient evidence of workplace or deployment fidelity.

## Transferable design patterns for skill-bench

### Retain

1. **Artifact-bearing task packages.** Keep prompts, source packs, expected behavior, rubric, executable checks, time budget, environment needs, and skills together under version control.
2. **Post-execution private grading.** Insert answer-bearing files only after agent termination and preserve proof of that transition.
3. **Multiple evidence views.** Use artifact checks, service/state audits, traces, and semantic judgment according to criterion authority.
4. **Time and cost as measured outcomes.** Preserve elapsed time, timeout state, tokens, tool calls, and cost beside quality.
5. **Configured-system reporting.** Record model × harness × adapter × tools × skills × environment × budget rather than attributing score to the base model.
6. **Cross-domain and bilingual/multimodal breadth.** The six categories resist narrowing to one artifact type and expose modality/tool interactions.
7. **Negative skill results.** Preserve regressions and interaction effects rather than treating skills as uniformly helpful.

### Repair

1. **Add a transport-conformance gate.** Before any model call, use the actual harness interfaces to prove prompt/source hashes, skill availability, service readiness, output persistence, private-evidence denial, path/write boundaries, network policy, secret allowlist, timeout semantics, and trace completeness.
2. **Fail closed on setup and evidence loss.** Warmup failure, missing fixture, missing audit service, absent transcript event, judge outage, or grader exception should produce typed invalid/unscorable status—not zero capability or fallback prose credit.
3. **Run least-privilege containers.** Drop `--privileged`, use a non-root user, read-only root where possible, scoped mounts, resource limits, capability allowlists, seccomp/AppArmor, authenticated service bridges, and explicit network egress.
4. **Bind the transport manifest.** Hash task, source pack, private grader, adapter, harness binary, system prompt, tool schema, skills, image digest, package lock, service fixtures, model endpoint/date/settings, judge, budget, and intervention into every trial.
5. **Preserve native and normalized traces.** Keep raw harness events plus a versioned normalized projection. Test planted actions to quantify event loss before using normalized traces for safety.
6. **Separate service state from narrative fallback.** If authoritative audit state is missing, mark the affected criterion insufficient-evidence; never infer an enacted side effect from the agent's own prose.
7. **Pin skill interventions.** Treat each Skill as a content-addressed intervention with dependencies, authority changes, expected mechanism, contamination risk, and invocation evidence.
8. **Use matched skill ablations.** Compare frozen baseline versus one bounded skill change over repeats; classify helpful routing, harmful distraction, tool affordance, knowledge support, and setup failure separately.
9. **Calibrate graders representatively.** Sample all criterion types and score regions, blind multiple qualified experts, preserve independent labels, report human–human and human–grader confusion/uncertainty, and revise the instrument before ranking systems.
10. **Retain every attempt.** Publish launch, setup, invalid, timeout, judge-failure, retry, and scored states with ancestry. Do not condition the denominator on successful transport.
11. **Estimate task-level reliability.** Use matched repeats and task-clustered intervals; report per-task pass patterns and disagreement, not only macro-score SD.
12. **Freeze live-web evidence or bound the claim.** Where task meaning allows, archive source snapshots and dates. Where live retrieval is the construct, version queries, record observations, and separate web drift from agent failure.
13. **Preserve the task-construction flow.** Retain candidate/rejection counts, reviewer records, revision reasons, pilot exposure, and held-out validation to diagnose discriminability-selection bias.
14. **Keep claim dimensions separate.** Completion, artifact usefulness, safety/compliance, transport validity, cost, repeatability, and professional readiness should not collapse into one “real-world agent” score.

## Concrete repository actions

### Immediate transfer

Use WildClawBench as additional evidence for the existing isolation, configured-system, evidence-view, skill-ablation, and retry-ledger work rather than importing its runner or aggregate score. The current `skill-bench` launcher must treat adapter conformance as a prerequisite for capability evidence. In particular:

- verify the exact Skill visible in each arm through the agent's own file/tool interface;
- prohibit repository/private-grader/other-profile access;
- record raw and normalized tool events and plant a harmless transcript canary;
- type setup, transport, service, judge, and agent failures separately;
- retain artifact hashes and timeout-state snapshots;
- keep matched no-Skill/Skill conditions under the same outer environment.

### Queue decision

Add no new queue item. Queue inspection found completed work for the execution-validity boundary, the isolated LH launcher, trajectory-observer conformance, multilingual transport, skill ablation, retry/invalid ledgers, and grader calibration; the only pending build already concerns native provider-call allocation telemetry. A new “transport conformance matrix” would duplicate that machinery. The requirements above should refine those artifacts' next revisions: join environment, adapter, transcript, and evidence transport in the canonical configured-system record rather than create a parallel subsystem.

## Bottom line

WildClawBench is a valuable and unusually concrete benchmark release. It moves beyond short answers, includes real artifacts and media, preserves side effects and trajectories, compares multiple native CLI systems, reports cost/time, and exposes consequential interactions among model, harness, budget, and skills. The post-execution insertion of private grading assets is especially worth retaining.

Its headline framing is stronger than its validity evidence. “Native runtime” does not make the task distribution representative, the container least-privilege, the adapter transport equivalent, the grader calibrated, or the paper replayable. The inspected release runs privileged networked containers, mutates some dependencies at runtime, uses mock services for social tasks, relies on live web state, falls back from state evidence to prose in places, converts traces across harness schemas, and postdates the paper with a ground-truth correction. The five image archives are pinned objects but opaque and operationally heavy; the reported trajectories are absent.

For `skill-bench`, the durable conclusion is precise: evaluate the configured system, but validate the transport before interpreting its score. A benchmark trial becomes capability evidence only when demand, authority, observation, and grader semantics survive the complete task-to-consequence path.

## Source and release links

- Immutable abstract: https://arxiv.org/abs/2605.10912v1
- Immutable PDF: https://arxiv.org/pdf/2605.10912v1
- Official repository: https://github.com/InternLM/WildClawBench
- Inspected source commit: https://github.com/InternLM/WildClawBench/tree/6f78ad8d4bc17e73e7d84de246dd2caa0b9c82c4
- Post-v1 ground-truth fix: https://github.com/InternLM/WildClawBench/commit/0c3fecd75a151dd43aaca7ef8d176af22fb357c8
- Exact dataset revision: https://huggingface.co/datasets/internlm/WildClawBench/tree/5a26773d94520f765032dddd34bf1bb9ccdae88a
- Local provenance: `data/sources/releases/2605.10912v1-wildclawbench/provenance.json`
- Local release audit: `data/sources/releases/2605.10912v1-wildclawbench/release-audit.json`
