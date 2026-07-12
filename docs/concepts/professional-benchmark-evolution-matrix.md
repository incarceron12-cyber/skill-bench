# Professional knowledge-work benchmark evolution: from plausible deliverables to closed evidence chains

## Scope and evidence status

This note compares the professional-work benchmark families currently supported by full local primary-source reviews and release audits: [GDPval](../../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md), [Workspace-Bench](../../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md), [MBABench](../../papers/agent-benchmarks/2026-07-11-mbabench-spreadsheet-artifact-validity.md), [LH-Bench](../../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md), [Workflow-GYM](../../papers/agent-benchmarks/2026-07-11-workflow-gym-professional-state-validity.md), [SaaS-Bench](../../papers/agent-benchmarks/2026-07-11-saas-bench-stateful-workflow-validity.md), and [Agents' Last Exam](../../papers/agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md). It also deeply inspects the complete official AA-Briefcase-Lite textual release and official evaluation page; the private AA-Briefcase tasks and results remain unauditable.

AA-Briefcase primary evidence:

- official evaluation extraction: `data/sources/aa-briefcase-official-evaluation-page.txt`;
- pinned Lite release: `data/sources/releases/aa-briefcase-lite/ArtificialAnalysis-AA-Briefcase-Lite-4dec557.zip`, commit `4dec557b47d43867a1648c0974db1d8208c8b677`;
- provenance and limits: `data/sources/releases/aa-briefcase-lite/provenance.json`.

This advances charter objectives A, B, D, and E through expansion followed by consolidation. The artifact is a retain/repair/test matrix. It clarifies which newer designs repair limitations of one-shot deliverable benchmarks and whether their evidence demonstrates the repair. It does not rank models, infer occupational readiness, or narrow `skill-bench` to consulting, finance, office software, or GUI use.

## Research question

What design progression is visible across influential or directly relevant professional-work benchmarks, which weaknesses do successors claim to repair, and what evidence shows that those repairs work?

The answer is not a simple chronology. The families improve different links in an evidence chain:

`work frame → task/source package → initialized environment → intervention/workflow → artifact and state delta → admissible checks → aggregation → licensed claim`.

No reviewed family closes every link. The strongest general direction is away from plausible final deliverables plus one scalar and toward versioned, plural evidence about sources, process, native artifacts, state transitions, expert judgment, and task health.

## Comparative evolution matrix

| Family | Construct and unit of work | Inputs → outputs / environment | Scoring | Strength to retain | Limitation or validity threat | Claimed/new repair | Evidence that repair works | Inspectability, cost, lifecycle | Direct relevance |
|---|---|---|---|---|---|---|---|---|---|
| **AA-Briefcase / Lite** | Multi-week business projects decomposed into independently run deliverables | Thousands of private files and 91 tasks; Lite has 67 sources/147 files and four due-diligence deliverables: PDF/LaTeX, XLSX, PPTX, MP4/SRT; offline E2B/Stirrup sandbox | Binary accuracy/critical-insight checks plus pairwise analytical-quality and presentation judgments; synthetic Elo aggregation | Messy cross-source evidence, planted contradictions, professional artifact diversity, explicit source→check traceability, cost/tool-use reporting | “Multi-week” context is shared but each task is reset and does not inherit the agent's own prior work; private scored tasks, outputs, result inventory, judge assignments, and validity evidence are unavailable; pairwise quality lacks an absolute release threshold; composite Elo hides distinct constructs | Adds source pools, hidden requirements, critical-insight checks, holistic artifact comparison, and private capability items beyond short QA | **Partly demonstrated in Lite structure only.** The pinned release contains four task records and 63 checks with evidence locators and pass/fail boundaries. It does not demonstrate private-suite representativeness, grader reliability, longitudinal coherence, or professional acceptance | Lite is Apache-2.0 and textually inspectable; many binary artifacts are LFS pointers in the local snapshot. Private benchmark maintenance, judge cost, and contamination controls are opaque | **A question / B evidence.** Direct architecture, weak public validity evidence |
| **GDPval** | One-shot, self-contained professional artifact production across 44 occupations | Multimodal references → work deliverables; configured tool/container systems | Occupation-matched pairwise preference against one human witness; later public criteria | Top-down occupational frame, experienced contributors, multimodal artifacts, repeated comparisons | Five public tasks per occupation do not represent occupational work; one human witness is not an expert distribution; equal-cell aggregation is not economic weighting; no observed augmentation workflow | Repairs narrow-domain benchmarks with broad occupational acquisition and expert artifact judgment | **Operational breadth demonstrated; inference repair not demonstrated.** Full paper and 220-task release support acquisition breadth but not occupation-level capability, expert parity, or productivity | Public metadata/rubrics are inspectable; full result/rating corpus and 1,320-task set are private; high expert and grading burden is incompletely costed | **Tier A** |
| **Workspace-Bench** | Retrieval, reasoning, and artifact production inside large persona workspaces | Simulated hybrid trees with 20,476 files; task-local and workspace files → artifacts | Model-judged foundational/process/outcome rubrics; authored dependency-graph recovery | Persistent noisy workspace, heterogeneous files, task-level dependency hypotheses, mutation/output collection | File availability, declared relevance, observed access, and causal use are conflated; graph/manifest mismatches; one apparent run; release/paper inconsistencies; generated workspaces are not longitudinal workplaces | Repairs clean task packets by requiring evidence discovery amid distractors and dependencies | **Environment scale demonstrated; “workspace learning” not isolated.** Release audit shows realistic substrate but also repeated synthetic evidence, weak isolation, and graph/placement defects | Large mutable workspace dependencies, post-paper release, host networking/full-access mode; exact paper results not reproducible | **Tier A** |
| **MBABench** | End-to-end editable spreadsheet production | Competition/training cases and starting workbooks → native `.xlsx`; GUI/API/web harnesses | 17 static Accuracy/Formula/Format criteria judged from serialized reference/candidate cells and styles | Native formulas, structure, finance-specific conventions, real large workbooks, explicit configured-system differences | Static serialization does not test recalculation under changed assumptions; no chart/render evidence for visual criteria; final size overstates required delta; one fallible witness anchors judgment | Repairs final-cell benchmarks by scoring formulas, structure, and presentation | **Static defect sensitivity partly demonstrated; maintainability repair not demonstrated.** 408 criterion labels support bounded judge engineering, not professional acceptance or counterfactual integrity | Code and 38-task subset inspectable; results/labels incomplete; commercial interfaces and reported ~$9.1K agent+judge cost limit reproduction | **Tier A** |
| **LH-Bench** | Long-horizon Figma-to-code and programmatic-content work grounded in expert procedures | Real design/data-room inputs → deployed code, videos, animations, presentations; persistent manifests and verifier feedback | Separate process rubrics, artifact/output judgments, and human pairwise preference | Expert procedure→trace boundary→artifact→grader crosswalk; recovery chains; plural tiers; course-level aggregation | Skill and rubric share an expert model, confounding transfer with evaluator cues; seven-run skill ablation; weak individual human/LLM concordance; narrow domains | Repairs generic subjective rubrics with observable expert workflow boundaries and artifact contracts | **Judge consistency repair supported; causal skill benefit weak.** Expert rubrics increase cross-judge κ from .46 to .60, but skill-effect evidence is directional only | Concrete appendices, but proprietary harnesses/models and incomplete release identity make exact reproduction costly | **Tier A** |
| **Workflow-GYM** | Long GUI workflows in 56 specialized software environments | Configured VMs and resources → artifacts/final GUI state; 338 tasks | Rule-, LLM-, or VLM-based all-criteria success, three trials | Real specialist software, long action horizons, expert witness procedures, environment packaging | Unreleased tasks/VMs/graders; model-specific harness confounding; outcome-only checks miss stages; showcase has residual state (`Name exists`) and path ambiguity | Repairs short computer-use tasks with specialized long workflows and VM state | **Difficulty demonstrated; clean-state/professional-work repair not demonstrated.** Showcase directly contradicts agent-only variation | Dataset “coming soon”; licensed software and 56 VMs imply high maintenance; no reported monetary/time cost | **Tier A question, B operational evidence** |
| **SaaS-Bench** | Cross-application browser workflows over persistent backend state | 23 open-source SaaS images and multimodal inputs → database/app state and artifacts | 1,304 weighted checkpoints; all-check resolved score | Deployable public package, per-run reset, native-state checks, cross-app consequences, partial observations | Seeded preconditions earn credit; dependent descendants double-count causes; weak joins/title-only artifact proxies; mutable judges/dependencies; no human threshold | Repairs screenshot-only GUI grading with backend/API/file checkpoints and public task/check code | **State observability repair demonstrated; progress validity not demonstrated.** Release audit finds rich native checks but concrete pre-satisfied, weak-proxy, and dependency defects | Strongest public stateful package, but ~54 GiB images and >500 GB RAM recommendation; no raw paper result inventory | **Tier A** |
| **Agents' Last Exam** | Expert-contributed, executable workflows across 55 software-mediated subdomains | VM `input/software/output/reference` packages → diverse native artifacts and state | Mostly deterministic task-specific graders, partial score and pass; some model judges | Broad executable production system, heterogeneous artifacts, public/private roles, shared lifecycle interface | Convenience coverage is not occupational sampling; 323 reported instances pending QC; mostly single runs; verifier completeness and clean-start not validated; suite membership drifts | Combines broad work taxonomy with executable artifact/state grading and living suites | **Engineering breadth demonstrated; occupational readiness not demonstrated.** Release audit finds ~150 public workflows and strong graders, but also unscored reasoning, a CAM gate bypass, and split drift | Substantial public code; full reproduction needs proprietary software/images/services; private pool and exact result inventory unavailable | **Tier A** |

### OfficeBench / WorkArena boundary

The completed [OfficeBench review](../../papers/agent-benchmarks/2026-07-11-officebench-cross-application-office-validity.md) establishes it as a historical anchor for typed cross-store state transitions and outcome-based task predicates, not professional-work validity: synthetic authoring, app-count confounding, 54 existence-only tasks, weak collateral-state and artifact-usability evidence, and mutable execution remain material limits. The completed [WorkArena L1 review](../../papers/agent-benchmarks/2026-07-12-workarena-l1-knowledge-work-validity.md) closes the WorkArena source gap: its 33 atomic ServiceNow classes provide strong enterprise-UI and selected native-state evidence, but 19,912 template-clustered parameter configurations do not establish sampled work breadth. Fresh users and object-specific teardown are not full reset attestations; heterogeneous query, record, URL, identity, chart, and answer predicates omit broad collateral state and professional usability. WorkArena++ demonstrably composes this machinery, repairing horizon while inheriting the need to validate every atomic observer and work-provenance link.

## AA-Briefcase-Lite full-source audit

### Contribution and system

The official release makes AA-Briefcase's authoring package unusually concrete. Lite defines a fictional private-equity due-diligence week grounded partly in real New Zealand egg-market data. The source pool deliberately mixes real and synthetic documents and cross-source contradictions. Four independently executable tasks produce six files across analytical and presentation modalities. `tasks.jsonl` binds each task to exact mounted sources, context documents, deliverables, rubric, and traceability paths. `grading_rubric_w1.json`, `source_graph_w1.json`, and `traceability_w1.json` bind checks to source files and evidence locations.

The harness is an offline, week-scoped E2B sandbox using Stirrup, a broad document-processing toolchain, image viewing, up to 500 turns, and context summarization. Inputs are read-only; outputs are writable and submitted by exact path. This is strong operational specification for a file-centered configured system.

### Evidence and unique insight

The 63 checks distinguish:

- **A — accuracy/instruction checks**, including native/render conformance and factual thresholds;
- **C — critical insights**, intended to require contradiction reconciliation or trap detection;
- **AQ/P — pairwise analytical and presentation quality**.

The deepest useful pattern is **source-graph-backed critical consequence**: a check records required files, exact source locations, a public task consequence, and explicit positive/negative boundaries. One inspected check requires the deliverable to use a later refined market-share estimate rather than average it with a superseded Slack draft. This is closer to consequential evidence reasoning than generic citation presence.

But the release also reveals a crucial observer-view contradiction. The binary judge prompt says judges see the task, one rubric item, and parsed submission, **never source files**; citations are judged for presence/specificity, not independently cross-checked. Some check boundaries contain extensive source-derived facts and locators, so the judge can test whether the artifact states the expected answer, but cannot establish that the cited source actually entails it or that the agent used the source. The traceability graph is authoring provenance, not trial-level source-use evidence. `skill-bench` must preserve four separate observations: expected source basis, artifact claim, citation locator, and verified source entailment/agent access.

A second insight is that AA-Briefcase's headline “multi-week” structure is **scenario-long but trial-short**. Tasks share context, yet each runs independently without prior model submissions. It measures repeated work against a common source pool, not longitudinal state management, revision, handoff, memory, or compounding artifact quality. This is a legitimate design choice but should not support claims about carrying a professional project across weeks.

### Limitations

1. The scored four scenarios, 91 task packages, source pools, outputs, check inventory, result matrix, and judge records are private.
2. Lite is explicitly smaller, easier, demonstrative, and excluded from leaderboard results; it cannot validate the private benchmark.
3. No contributor/reviewer qualifications, authoring flow, expert disagreement, check validation, grader agreement, false-positive/negative study, or professional acceptance threshold is public in the inspected evidence.
4. Binary no-partial-credit checks can make threshold-near and catastrophic failures observationally identical; dependent checks may multiply one underlying fact.
5. Pairwise analytical/presentation Elo identifies relative preference in the sampled comparison graph, not absolute readiness, correction burden, or stakeholder utility.
6. Overall Elo combines distinct binary and pairwise constructs through synthetic matches. A confidence interval on Elo does not validate the construct aggregation.
7. Tool-call and file-exploration coverage are behavior descriptors, not proof of relevant, correct, or causal evidence use.
8. Estimated wall time derives token counts from a canonical output speed plus tool time, rather than observed end-to-end latency.
9. Context summarization, parser/render versions, sandbox image, exact model/harness settings, missing/abandoned-run policy, and grader assignment policy need immutable identities for comparison.
10. Public tasks, rubrics, source locators, and example submissions are contamination/calibration material, not secure capability items.

### Reproducibility and operational realism

Lite is strong for authoring inspection: Apache-2.0 metadata, exact prompts, task/check records, traceability objects, source manifests, and illustrative submissions are pinned. The local archive preserves 198 paths, though LFS-managed PDF/DOCX/XLSX/PPTX/MP4 objects are pointers rather than downloaded binaries. No score replay was attempted, and no private result can be reproduced.

Operational realism is mixed. Heterogeneous files, contradictory sources, native editable artifacts, strict output contracts, offline tooling, and professional presentation are credible. Fictional organizations, independently reset tasks, no stakeholder interaction, no prior-work carryover, answer-bearing check criteria, and artifact-only judges remove project continuity and direct consequence. The right claim is performance on a realistic **artifact-and-evidence package**, not autonomous multi-week employment.

## Cross-family conclusions: retain, repair, test

### Retain

1. **Broad frames without broad claims:** GDPval/ALE show how to declare occupational coverage; preserve frame, content, assembly, and inference denominators separately.
2. **Messy source packs and explicit authority:** AA-Briefcase and Workspace-Bench make evidence location, contradiction, supersession, and distractors first-class.
3. **Native artifacts plus plural views:** MBABench, LH-Bench, SaaS-Bench, and ALE demonstrate why structured state, executable behavior, renders, traces, and human judgment answer different questions.
4. **Configured environments and reset:** Workflow-GYM and SaaS-Bench show that software/state is part of the instrument.
5. **Expert procedure as observable boundaries:** LH-Bench's strongest evidence concerns rubric observability, not generic expertise branding.
6. **Executable checks as falsifiable instruments:** ALE and SaaS-Bench make graders inspectable enough to adversarially test.
7. **Public/private lifecycle roles:** public packages support audit and calibration; private or refreshed forms are needed for capability evidence.

### Repair

1. Replace “representative” coverage claims with explicit sampling frames and licensed inference populations.
2. Treat references and expert paths as fallible witnesses; encode alternative legitimate paths and reapproval after engineering transformation.
3. Require clean-start, pre/post state, run-attributable deltas, and dependency-aware checkpoint semantics.
4. Bind every criterion to an admissible evidence view; abstain when a screenshot, parsed artifact, or trace cannot establish it.
5. Separate source existence, authority, entailment, citation, observed access, adoption, and causal use.
6. Keep process, artifact correctness, presentation, preference, safety, efficiency, and readiness separate until aggregation is empirically warranted.
7. Report first-attempt reliability, retries, invalid runs, cost, and maintenance burden—not only eventual artifacts or pass@k.
8. Version task, source pack, environment, harness, intervention, artifact parser/renderer, grader, suite membership, and exposure role independently.

### Test in skill-bench

1. **Evidence-chain falsification:** plant an authoritative source, superseded source, lexical distractor, correct uncited claim, precise but non-entailing citation, and source that was never exposed. Grade each stage separately.
2. **State-delta falsification:** plant a pre-satisfied requirement, unrelated same-value record, title-only empty artifact, shared-cause descendant failures, and dirty output path.
3. **Artifact behavior:** mutate authoritative inputs, recalculate in a pinned engine, inspect native and rendered views, and test preserved regions.
4. **Skill/instrument independence:** run no-skill/public-skill × independent/shared-rubric conditions with the environment fixed.
5. **Alternative-path verifier tests:** positive witness, independently valid alternative, minimally wrong contrast, shortcut/adversarial artifact, and renderer/parser drift.
6. **Claim ladder:** permit task-package claims first; require new sampling, expert-threshold, downstream-use, safety, and loss evidence for workflow-family, occupational, or readiness upgrades.

## Adoption and influence: bounded interpretation

The current primary sources establish active benchmark construction and substantial released packages, but this run did not obtain robust longitudinal citation, usage, or independent-replication data for every family. “Influential” is therefore used only in a design-relevance sense unless evidence is explicit. Public leaderboards, model coverage, or occupational breadth do not establish validity. AA-Briefcase's official page reports 46 listed models and a private leaderboard; this demonstrates operator activity, not independent adoption. GDPval's occupational frame and ALE's broad executable suite are anchors because they directly address the charter, not because popularity validates their claims.

## Concrete repository actions

1. Use this matrix as the professional-work evolution view in the SOTA map and synthesis index; keep source-specific detail in full reviews.
2. Do not add another schema task. Existing expertise-transfer, participation, benchmark-bundle, artifact-view, persistent-workspace, task-health, metric, validity, and execution records already house the repairs.
3. Before a second pilot result is promoted, execute the six falsification families above and preserve invalid/insufficient outcomes.
4. Use the completed OfficeBench, WorkArena L1, and WorkArena++ audits to distinguish typed cross-store transitions, atomic native-state predicates, and composed-workflow validity without promoting any of them to professional-work evidence.
