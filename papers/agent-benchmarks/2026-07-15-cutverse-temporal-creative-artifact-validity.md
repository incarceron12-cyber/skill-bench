# CutVerse: milestone screenshots do not establish temporal creative-artifact validity

## Source and review status

**Deep review of the complete immutable primary paper and a commit-pinned official release.** I read the full 30-page arXiv v1 PDF/text and audited the complete 253-file official repository snapshot. The snapshot is 20 days newer than v1 and is therefore post-v1 implementation evidence, not proof of the paper-time task suite, parser, grader, environments, or results.

- **Paper:** Haobo Hu et al., *CutVerse: A Compositional GUI Agents Benchmark for Media Post-Production Editing*, arXiv:2605.19484v1, https://arxiv.org/abs/2605.19484v1
- **Version read:** immutable v1, submitted 19 May 2026; metadata contains no withdrawal/retraction notice
- **Date read:** 2026-07-15
- **Local PDF:** `data/papers/pdfs/2605.19484v1-cutverse.pdf` (30 pages; SHA-256 `79800c281a634758ad2ed71bc703dd2990842a659a533e1df7d4b7118502fc58`)
- **Local text:** `data/papers/text/2605.19484v1-cutverse.txt` (SHA-256 `d750092bd0e15cc2f031f9c05f1f2a6ec4b472f6137dafadff9a1806bd3d80ba`)
- **Official HTML:** `data/papers/source/2605.19484v1/2605.19484v1.html` (SHA-256 `779af3d455368b69e90629fd5102b43000478ed3f54b25749060a1e23f847ed8`)
- **Official release inspected:** https://github.com/CUC-MIPG/CutVerse/tree/8b40dc18e1385bf6a9710cd999b22e4c51d602c8 (commit dated 8 June 2026)
- **Release provenance:** `data/sources/releases/2605.19484v1-cutverse/provenance.json`
- **Static release audit:** `data/sources/releases/2605.19484v1-cutverse/release-audit.json`
- **Version boundary:** the only observed `Preview` tag points to a different commit; the archived default-branch snapshot postdates v1 by 20 days and says the runnable OSWorld-Win harness was merged on 8 June
- **Tags:** computer use, media post-production, temporal artifacts, expert demonstrations, milestone grading, judge validity, release audit

## One-sentence contribution

CutVerse contributes a rare expert-demonstrated frame for 186 live media-editing tasks across dense professional applications and decomposes long GUI interaction into 631 visually queried milestones, but its evidence observes selected interface states rather than editable project structure, exported temporal behavior, creative quality, or professional acceptance; the paper leaves the parser, judge study, trial denominators, and headline rates under-specified, while the inspected release contains a generic Windows runner, one Notepad example, and placeholder evaluators—not the claimed benchmark or result evidence.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through a narrow methodological case with reusable implications across domains. Time-based creative work makes a general benchmark-design failure unusually visible:

```text
expert intent
→ source-media rights and constraints
→ editable project state
→ ordered/time-indexed transformations
→ rendered/exported behavior
→ perceptual and semantic quality
→ recipient acceptance and downstream use
```

CutVerse records an expert interaction witness and asks VLMs questions about selected screenshots. That is potentially useful evidence for GUI execution and local state transitions. It is not evidence for most later links. A clip can look aligned in one screenshot while drifting during playback; a transition icon can appear while the effect is on the wrong interval; an export dialog can appear while the export fails; a flattened output can look plausible while the project is not editable; and a canonical expert path can be unnecessary even when the result is correct.

The transferable lesson is not “skill-bench should become a video benchmark.” It is that **temporal/compositional artifacts require observer coverage over time, structure, render, and consequence—not merely more screenshots or a longer trajectory**.

## Research question and defensible claim boundary

The paper asks whether current computer-use agents can execute realistic long-horizon media post-production workflows in live professional software, and whether expert demonstrations can be parsed into milestone-driven trajectories that support scalable automated evaluation (Sections 1 and 3, pp. 3–8).

The strongest defensible paper claim is:

> The authors report constructing 186 task episodes from ten creators, spanning a heterogeneous set of editing/generative applications, and evaluating five differently configured screenshot-action systems in resettable Windows environments. Under the authors' unreleased milestone protocol, system completion and execution measures diverge, and core editing categories receive lower reported rates than setup/file-management categories.

The evidence does **not** establish that:

- the 186 tasks represent professional post-production frequency, consequence, or quality;
- expert recordings preserve tacit decision logic rather than one successful motor path;
- parser-generated milestones are accurate, complete, or invariant to legitimate alternate workflows;
- selected screenshots prove temporal synchronization, cross-modal alignment, editable-project integrity, export correctness, or creative quality;
- 98.3%/99% “human agreement” means expert-level judge validity without a sampling frame, label protocol, human reliability, class balance, confusion matrix, or uncertainty;
- Table 3's “task success,” Table 8's completion/execution distinction, and the abstract's 36.0% headline share one auditable estimand;
- model rows are comparable model effects rather than model–prompt–history–resolution–coordinate–action-space packages;
- one attempt per model–task, absent run accounting and uncertainty, supports reliability or stable rankings;
- the post-v1 release reproduces any paper result;
- CutVerse establishes professional capability, production fitness, creative acceptance, safety, or readiness.

## Methodology and system

### Expert demonstrations and task construction

Appendix A.1 reports ten “professional creators” who define tasks, record ground-truth videos, instantiate VM checkpoints, review parsed milestones, and refine generated QA pairs (p. 14). The resulting corpus is reported as 186 tasks, 2.43 hours of recording, 3,484 GUI interactions, and 631 milestones, with mean 18.73 interactions and a maximum trajectory of 239 steps (Section 3.3, p. 7; Appendix B, p. 23).

This is more direct domain participation than tutorial-trained internal authorship. Yet the paper reports no recruitment frame, occupations, years or type of practice, application-specific authority, task allocation, independence, compensation, conflicts, contribution time, rejection counts, disagreement, or task-level provenance. “Original expert recorder reviews their own parsed task” improves internal correspondence but does not supply independent validation. The same person can author the instruction, demonstrate the route, and approve the milestone questions, creating task–trajectory–grader co-design.

Task sampling is a designed taxonomy, not a professional work population. Nine categories range from launch/setup and import to timeline editing, effects, masking, audio, and export (Table 2, p. 6). The paper says seven professional applications in the abstract and contributions, but Table 10 names eight environments after adding Jimeng to the seven-software evaluation subset (pp. 23–24). Counts also heavily favor effects/visual tuning (51/186) and export/delivery (29/186), with no source population or frequency/consequence weights. Coverage breadth therefore supports a heterogeneous case set, not occupational representativeness.

### Source media, licensing, and public basis

The paper describes fixed source content, asset libraries, audio waveforms, generated clips, and task-specific VM checkpoints, but supplies no task-level source manifest, origin, license, consent, checksum, transformation history, or redistribution status. The inspected repository has no benchmark media and no top-level license file. This blocks both legal reproducibility and construct audit: source compression, frame rate, color space, duration, audio offset, font/plugin availability, and prior project state can determine whether an apparent failure belongs to the agent or environment.

For skill-bench, source-media rights are not an administrative afterthought. They are part of trusted evidence and release validity. A task should bind every asset to origin, permitted use, immutable hash, technical metadata, and any transformation that changes the graded target.

### Recording and parser transformation

Figure 3 depicts synchronized MKV screen video plus timestamped interaction events transformed into action captions, before/after observations, grounding, hierarchical milestones, and QA pairs (p. 5). Section 3.2 says high-frame-rate recordings and low-level I/O logs are synchronized and discretized (pp. 6–7). Appendix A.1 adds LLM-generated context-rich QA from pre/post screenshots followed by recorder refinement (p. 14).

This is a promising expertise-to-evaluation pipeline, but the paper gives no recorder software/version, event schema, clock source, synchronization tolerance, frame-selection rule, lost-event rate, parser model/prompt/version, segmentation algorithm, milestone boundary criterion, QA generation model, acceptance/revision rate, double annotation, parser precision/recall, or inter-rater agreement. Nor does it show that audio was retained in the judge evidence view. A screenshot-only milestone cannot observe a beat alignment or playback transition, even when the underlying demonstration was audiovisual.

Most importantly, parser output is a **projection of one witness path**. It may preserve what the recorder did while losing why they did it, what alternatives were valid, which state changes were merely incidental, and which downstream consequences matter. Calling the resulting capabilities “transferable” (Section 3.2, p. 7) outruns evidence: no cross-task, cross-application, or held-out transfer study is reported.

### Task, temporal, and compositional representation

The paper frames each task as a POMDP with screenshot and action history, excluding accessibility trees and application APIs (Appendix A.2, pp. 14–15). Agents emit low-level mouse/keyboard operations, including drag, held keys, waits, and termination. This authentically stresses pixel grounding and motor coordination.

However, the benchmark's *measurement representation* remains sparse. QA examples ask whether a slider displays a value, a clip edge appears shortened, audio fills a visible gap, a mask covers the canvas, the playhead advances, or an export progress dialog appears (Table 11, pp. 25–26). These are local visual predicates. They do not represent:

- time interval, frame range, track/layer identity, or sample-accurate offset;
- temporal relation such as overlaps, precedes, fades through, remains synchronized, or loops continuously;
- source→project→render lineage;
- editable native project graph, missing media, proxy/relink state, keyframes, expressions, nested compositions, and parameter interpolation;
- render settings, codec/container, frame rate, color space, audio channels/loudness, dropped frames, or export completion;
- cross-application handoff identity and whether imported/exported bytes are the intended artifact;
- must-preserve and forbidden-change predicates;
- legitimate equivalence classes and alternative workflows.

The term “compositional action space” therefore refers mainly to coordinated low-level inputs. It is not yet an executable compositional **artifact contract**.

### Environment and execution

The paper reports Windows 11 Pro Hyper-V VMs, a task-specific checkpoint, identical source files/input formats/software configurations, and live screenshot-driven pyautogui execution (Sections 3.2, 3.4, and 4.1, pp. 6–9). That design can reduce state drift.

Yet it provides no image or checkpoint hashes, OS build, display scaling, application/plugin/font versions, activation/license state, GPU/display stack, locale, color management, cache status, network policy, source-pack inventory, reset conformance, application health, timing policy, or state-delta canaries. “Exact same system states” and “guarantees reproducibility” are assertions rather than published conformance evidence.

The post-v1 release includes substantive Hyper-V lifecycle and low-level screenshot/action machinery. `agent/vm_manager.py` can restore a named checkpoint, start the VM, discover its IP, and wait for service health. But the archive contains no paper VM image or snapshot manifest. Its own `REVIEWLOG.md` records a real operational failure mode: `/screen` can work while screenshot capture fails when the service runs in non-interactive Session 0. Health therefore does not imply valid observation.

### Configured agent treatments

Five systems are reported: Claude Opus 4.6, Gemini 3 Flash, Qwen3-VL-32B-Thinking, UI-TARS-1.5, and EvoCUA-32B (Table 6, p. 17). They differ materially:

- screenshot size and preprocessing;
- absolute versus normalized coordinates;
- history of four, five, or ten images/turns;
- explicit thinking versus none/optional;
- OSWorld-style versus CutVerse-specific prompts;
- single-action versus compound action arrays;
- support for held keys and extra primitives;
- output JSON/XML/Python-like formats and parsers.

Gemini alone receives a CutVerse-specific planner with compound actions and milestone-completion metadata (Appendix A.4.5, pp. 21–22). These differences are not nuisance details; they determine what behavior is possible and how state is observed. Results identify configured packages, not base-model capability.

The paper reports local CUDA/PyTorch/vLLM/Transformers versions and GPU allocation for open models (Table 7, p. 22), which is useful, but omits proprietary endpoint snapshots, evaluation dates, decoding settings for every model, retry/rate-limit policy, malformed-output handling, action timeout, wall-clock cap, and exact runner commit.

### Evaluation and scoring

CutVerse says each long task is decomposed into a hierarchy of visually verifiable milestones. GPT-5.4 and Claude-4.6-Opus judge grounded QA over intermediate states, and an intermediate failure can dictate overall task failure (Figure 3 and Section 3.4, pp. 5 and 8). Table 3 reports task- and milestone-level rates by category; Table 8 distinguishes self-reported completion from “execution accuracy” through a consistency gap (pp. 8 and 23).

The score contract is not fully specified. The paper does not publish:

- number of QA items per milestone or task;
- conjunction/disjunction/dependency rules;
- whether judges see one frame, before/after pairs, a video window, audio, action log, or task history;
- prompt, response schema, model snapshots, sampling, retries, parser failures, disagreement handling, abstention, or fallback;
- criterion weights, task aggregation, model aggregation, macro/micro policy, or missing-result treatment;
- how milestone ordering and alternative routes are handled;
- when a failed intermediate state remains recoverable in the final artifact;
- whether final output or native project is inspected at all.

The post-v1 release does not repair this gap. Its `tasks/` directory contains only `README.md` and `example_notepad.yaml`; the task schema forwards an arbitrary `task_config`. `scripts/run_benchmark.py` defaults to a no-op stub evaluator; `agent/evaluator/vlm_evaluator.py` explicitly raises `NotImplementedError`; `agent/loop.py` stops on model-reported milestone completion and passes only the full trajectory plus the **last observed screenshot path** to an evaluator. There are no 186 task records, source media, expert logs, parsed trajectories, 631 milestones, QA records, paper outputs, human labels, or result tables. The release is a generic harness snapshot, not an inspectable CutVerse benchmark release.

## Evidence and result interpretation

### What the reported numbers support

Table 3 shows much higher rates in setup/file-management categories than in core editing categories. For example, Claude's reported task rates range from 1.000 on generative workflow to 0.286 on masking/matting/tracking, and Gemini ranges from 1.000 to 0.381 (p. 8). Table 8 reports 59/186 Claude tasks and 61/186 Gemini tasks as incomplete, while Qwen and UI-TARS exceed 50% incomplete (p. 23). These are useful descriptive signals that the selected instrument distinguishes task families and that self-reported completion does not guarantee judged execution.

They do not identify why. Category, application, expert author, path length, action mix, source asset, criterion count, judge difficulty, and configured harness co-vary. The paper's claim that software complexity is a “direct proxy” for multimodal reasoning difficulty (Section 5.2, p. 11) is unsupported without matched tasks or a measurement model.

### Numerical and estimand inconsistencies

Three unresolved inconsistencies materially limit interpretation:

1. **36.0% headline:** the abstract says existing agents achieve “only 36.0% task success” (p. 1), but Table 3 reports overall task success from 44.1% to 68.3%, and Table 8's implied execution accuracies are 31.8%–58.1%. No aggregation producing 36.0% is defined.
2. **Success versus completion:** Table 3 labels the overall values “Task Success Rate,” while Table 8's incomplete counts imply those same values are completion rates (`1 - incomplete/186`) and then subtracts a separate consistency gap to obtain execution accuracy. Thus the main table's “success” appears to be model completion declaration, not verified success.
3. **Seven versus nine applications:** the abstract and contribution claim seven applications, while Table 10 names After Effects, ComfyUI, DaVinci Resolve, JianYing, Jimeng, Keling, Premiere Pro, and Photoshop—eight names in that table, and the text elsewhere presents a seven-software evaluation subset. The task/software population and which environments enter reported rates are not reconciled.

These are not cosmetic labels. They change the measured event and denominator. Until task-level outcomes and an aggregation script are released, the headline rate and ranking are not auditable.

### Human-alignment study

The paper reports 300 agent trajectories assessed by “professional creators” and QA-grounded judges, with 98.3% agreement for GPT-5.4 and 99% for Claude-4.6-Opus (Section 3.4, p. 8). No additional method or table supplies:

- trajectory/task/model sampling and whether hard/failed/ambiguous states were enriched;
- number, identity, role, independence, and assignment of human raters;
- label unit, class prevalence, duplicate labels, agreement among humans, or adjudication;
- judge prompt/evidence view, endpoint, decoding, invalid outputs, and retries;
- contingency table, sensitivity, specificity, chance correction, task clustering, or confidence interval;
- whether the judge was calibrated on held-out examples;
- whether agreement is on each QA, milestone, or task.

At 99% with potentially imbalanced true/false questions, raw agreement can coexist with poor minority-class recall. Reusing the task authors/recorders as raters can also preserve shared assumptions. The evidence supports a reported agreement statistic under an under-specified protocol—not the paper's statement that automated models match expert-level judgment or that humans can be “relegated” to ground-truth curation.

### Trial denominators, reliability, uncertainty, and cost

The paper appears to report one outcome per model–task cell: 186 tasks × five systems. It reports no repeated attempts, seeds, order, concurrency, attempted/valid/retried/dropped runs, environment/setup failures, API failures, malformed actions, judge failures, manual reruns, or confidence intervals. Table 8's “incomplete” category mixes policy failure with possible execution/runtime failure unless a hidden ledger separates them.

No token, API, GPU, VM, storage, wall-clock, creator, annotation, judge, or adjudication cost is reported. This is a major omission for a benchmark involving five screenshot-heavy agents, paid professional software, 930 nominal task executions, two frontier judges, VM checkpoints, and human review. A single-attempt table estimates neither per-task success probability nor operational reliability.

## Release audit and reproducibility

The complete archived post-v1 repository has 329 ZIP entries, 253 files, and 8.34 MB uncompressed. Static compilation of all 127 Python source strings found no syntax errors. It contains a Windows Local Engine, model adapters, agent loop, Hyper-V manager, Electron UI, and suite runner. This is real infrastructure, not an empty landing page.

However, the empirical correspondence is low:

- the commit is 20 days post-v1 and the `Preview` tag points elsewhere;
- README says the runnable OSWorld-Win code was merged on 8 June, after v1;
- `PROJECT_BRIEF.md` still says no implementation is included, revealing mutable/reassembled release documentation;
- `PROGRESS.md` labels the VLM evaluator as a placeholder and says a real VM end-to-end task remained pending;
- only one Notepad example exists under `tasks/`;
- the default evaluator is inconclusive and the VLM evaluator is unimplemented;
- there is no paper task corpus, source media, licensing manifest, parser, parsed demonstration corpus, milestone QA inventory, environment image/checkpoint manifest, result ledger, trajectory, judge output, alignment annotation, or cost record;
- ROADMAP places protocol, dataset, evaluator toolkit, and benchmark-subset release in future phases;
- no repository license file was present in the inspected archive.

Thus reproducibility is **moderate for inspecting a later generic Windows GUI harness, low for recreating a fresh CutVerse-like run, and absent for reproducing v1 results**. A new user would need private tasks, assets, paid applications/licenses, snapshots, parser output, judge implementation, and scoring semantics. Any new run would concern a newly assembled instrument, not v1, unless byte-level correspondence were established.

## Unique insight: temporal evidence must be layered by what it can prove

CutVerse's deepest transferable insight is negative but constructive: **a state transition visible at one instant is not a temporal artifact judgment**.

Skill-bench should separate at least five evidence layers:

1. **Interaction conformance:** did the configured system emit valid actions and reach observable GUI states?
2. **Native project state:** do tracks, layers, clips, keyframes, effects, assets, parameters, links, and editability satisfy typed structural predicates?
3. **Rendered temporal behavior:** over declared time intervals, do visual/audio streams exhibit required synchronization, continuity, timing, and absence of glitches?
4. **Creative/professional judgment:** is the result coherent, intentional, aesthetically and technically acceptable under a calibrated expert protocol?
5. **Operational consequence:** can a recipient open, revise, deliver, and use the artifact under real constraints, with rights, safety, and preservation intact?

A criterion should name its authoritative layer and admissible observer. Examples:

- “effect control reads 71” may admit a native parameter parser or correctly scoped UI view;
- “cross dissolve occurs over frames 240–252” requires project-timeline structure and/or frame-window render evidence;
- “audio hit aligns to impact” requires an audiovisual temporal observer with tolerance and calibration;
- “project remains editable” requires native graph/media-link inspection, not an MP4;
- “cut feels professionally paced” requires plural expert judgment and cannot be laundered into one hidden screenshot check;
- “export succeeded” requires file identity, decodability, declared technical properties, and potentially playback—not a progress dialog.

This layered view also avoids canonical-path grading. Expert demonstration can supply one solvability witness and candidate stage boundaries. The benchmark must independently establish which transitions are construct-essential, which consequences are path-invariant, and which alternate routes are admissible.

## Limitations and validity threats

### Content and expertise validity

1. Ten creators are described without recruitment, roles, qualifications, application-specific authority, assignment, independence, compensation, conflicts, or contribution time.
2. Recorder self-review does not establish independent task/rubric validity or disagreement.
3. No occupational/workflow population, inclusion process, task frequency, consequence weighting, or recipient study supports professional representativeness.
4. Taxonomy counts are designed coverage, heavily concentrated in effects and export.
5. “Seven applications” is inconsistent with the broader set of named environments.
6. Source media lack task-level origin, rights, consent, hashes, and technical metadata.
7. Generated-content services add mutable model/provider outputs unless frozen assets and endpoints are recorded.
8. One expert path proves one feasible route, not necessity, uniqueness, or transferability.

### Parser and trajectory validity

9. Recorder/event schemas, clocks, synchronization tolerance, frame selection, segmentation, and parser versions are absent.
10. Parser precision/recall, lost events, milestone boundary reliability, QA acceptance/revision rates, and independent agreement are unreported.
11. Before/after screenshots can miss intermediate temporal behavior and audio entirely.
12. Milestones can encode benchmark-author procedure rather than path-invariant consequences.
13. No alternative workflow adjudication or equivalence policy is specified.
14. No evidence shows the claimed atomic capabilities transfer across tasks or applications.
15. Action counts measure one recorded path and do not form a calibrated complexity scale.

### Artifact and grader validity

16. QA examples primarily observe UI appearance, not native project graphs, time intervals, audiovisual playback, or exported bytes.
17. A progress dialog is not export completion; a timeline view is not full temporal correctness; a flattened render is not editability.
18. Criterion inventory, dependencies, weights, conjunction semantics, and aggregation are unreleased.
19. Judge evidence views, prompts, model snapshots, decoding, retries, malformed output, abstention, and disagreement policy are absent.
20. Raw 98.3%/99% agreement lacks sampling, prevalence, human reliability, contingency tables, clustering, and uncertainty.
21. Agreement against task co-authors is not independent professional acceptance.
22. Two model judges sharing benchmark assumptions are not model-agnostic validity.
23. No creative-quality, coherence, accessibility, technical-delivery, recipient-utility, or downstream-use protocol is reported.
24. Safety, rights, preservation, unauthorized changes, and side effects are absent from scoring.

### Experimental and statistical validity

25. Model, prompt, observation history, coordinate system, action vocabulary, batching, and parser differ by row.
26. Gemini receives a distinct CutVerse-specific planner and compound-action treatment.
27. Proprietary endpoints, dates, full decoding, retry, invalid-action, timeout, and service-failure policies are not pinned.
28. No repeated trials or task-clustered uncertainty support reliability or stable rankings.
29. Category/application/path-length comparisons are confounded by author, assets, action mix, criterion count, and harness.
30. “Software complexity” is not experimentally identified as reasoning difficulty.
31. The abstract's 36.0% is not reconciled with Tables 3 and 8.
32. Table 3 appears to call completion declarations task success, while Table 8 separately derives execution accuracy.
33. Attempted, valid, retried, excluded, and scored denominators are absent.
34. No cost or human-burden accounting accompanies scalability claims.

### Reproducibility and operational realism

35. The inspected release is post-v1 and not tagged as the exact paper implementation.
36. The paper's 186 task records, media, demonstrations, parser outputs, milestones, QA, environments, and results are absent.
37. The released VLM evaluator is a placeholder and default evaluation is inconclusive.
38. The generic loop exposes only the final observed screenshot to the evaluator interface, not native project or temporal render views.
39. Real VM execution remained pending in release progress notes; screenshot health can fail despite service health.
40. Environment/version/checkpoint identity and reset conformance are not published.
41. Paid software, activation, plugins, fonts, codecs, GPU/display behavior, caches, and generated-service state complicate replay.
42. No license file or source-media rights manifest supports redistribution.
43. No public evidence supports professional capability, reliability, production fitness, or readiness.

## Comparison with adjacent evidence

- **DeskCraft** releases native-artifact checks and phased desktop tasks in a later snapshot, but demonstrates that structural endpoint conformance is below creative/professional acceptance. CutVerse has stronger direct creator-demonstration claims yet releases none of its task/artifact checks and relies more heavily on screenshot milestones.
- **Workflow-GYM** emphasizes long expert procedures and final-state checks. Its core warning transfers directly: a reference path is a solvability witness, a stage check observes a selected transition, and a final artifact observes selected consequences. CutVerse needs the same transition-system contract, extended over time-indexed media.
- **OSWorld 2.0** makes evolving obligations, dense checkpoints, alternate path allowance, artifact checks, and separate safety diagnostics more explicit. CutVerse's milestones add media-specific temporal hypotheses but lack OSWorld 2.0's clearer checkpoint/release machinery and still need dependency/value semantics.
- **SciVisAgentBench** separates executable code, structured state, rendered images, domain-specific measures, and model judgment. CutVerse should retain that evaluator-admissibility discipline and add temporal windows/audio; one screenshot representation cannot serve every media predicate.
- **Delegate52 and skill-bench artifact-transition evidence** separate requested change, must-preserve state, forbidden changes, forward result, and recovery. CutVerse currently asks whether a milestone appeared, but does not test collateral edits, project integrity, or legitimate recovery from a bad edit.
- **Claw-Eval and trajectory-observer evidence** separate final response, action trace, and external state while warning that more channels are not independent truth. CutVerse similarly needs criterion-specific views: action logs for motor/process claims, native project state for structure, audiovisual playback for time, exported bytes for delivery, and experts for creative acceptance.

Across these sources, the retain/repair/test decision is clear:

| Retain | Repair | Test before stronger claims |
|---|---|---|
| expert-recorded feasible workflows; resettable live software; low-level interaction; sparse semantic milestones; task-family diagnostics | task-level expert/source lineage; temporal/native/render/export observer contracts; alternate paths; criterion dependencies; run ledger; configured-system hashes; judge abstention; rights/version/reset manifests | parser fidelity; milestone necessity/sufficiency; temporal observer accuracy; creative expert reliability; cross-app transfer; repeated-run reliability; professional acceptance; recipient utility |

## Transfer to skill-bench

1. **Represent temporal artifact predicates in existing machinery.** Extend a future cross-domain conformance fixture—not a media-specific subsystem—with time basis, interval/frame/sample locator, track/layer identity, source→project→render lineage, required evidence views, synchronization tolerance, permitted invariances, must-preserve/forbidden-change predicates, and `insufficient_evidence`/`invalid_artifact` outcomes.
2. **Make demonstration status explicit.** Record expert trajectory as `solvability_witness`, not oracle. Link each proposed milestone to public requirement, expert rationale, pre/post state, downstream consequence, alternative-path policy, and independent review status.
3. **Use plural artifact views.** For time-based work, preserve native editable state, deterministic structural extracts, rendered video/audio windows, export metadata/decodability, and relevant trace slices. Never infer temporal behavior from a static screenshot unless the criterion itself is static.
4. **Calibrate temporal observers with planted cases.** Include correct timing, one-frame/one-beat drift around tolerance, right appearance at wrong interval, wrong track, missing media, visually plausible flattened output with broken native project, export-dialog-without-file, codec/frame-rate mismatch, and correct alternative workflow. Estimate false pass/fail per observer.
5. **Separate creative acceptance.** Keep deterministic technical conformance apart from calibrated expert quality, editability, recipient utility, and readiness. Report rater authority, evidence view, repeated items, agreement, adjudication, and uncertainty.
6. **Require a fail-closed trial ledger.** Preserve attempted, environment-valid, agent-valid, judge-valid, retried, excluded, and scored cells; pin model, adapter, prompt, action schema, observation policy, software stack, VM image/checkpoint, source pack, judge, and all transformations.
7. **Do not import CutVerse's 36.0%, rankings, judge-agreement claim, or professional conclusion** into canonical evidence until task-level records, aggregation code, result ledgers, and judge annotations reconcile the stated estimands and denominators.

These requirements fit the existing benchmark-bundle artifact views, initial-state conformance, artifact-transition, trace/evidence-view, dynamic-criteria, task-health, metric-monitoring, and validity-argument machinery. **No new queue task is added**: the evidence is a high-value temporal conformance case for a future diverse-pilot validation slice, not justification for another overlapping contract or a media-only benchmark branch.

## Action items

1. Use `data/sources/releases/2605.19484v1-cutverse/release-audit.json` as the release-health evidence record; do not treat the post-v1 harness as the v1 benchmark.
2. When the next artifact-transition or multimodal conformance pilot is extended, add one small time-based synthetic case with native structure plus rendered temporal output and the planted failures above.
3. Require any future creative-work pilot to preserve source rights/provenance and an editable deliverable alongside its export.
4. Keep CutVerse at a methodological relevance tier until a benchmark/task/result release permits empirical replay and criterion-level audit.

## Completion checklist

- [x] Read the complete immutable 30-page v1 paper and preserved full text.
- [x] Audit the complete commit-pinned official post-v1 archive and preserve the timing boundary.
- [x] Reconstruct expert authoring, parser projection, task/action representation, VM execution, configured agents, graders, results, and judge study.
- [x] Audit task, evaluator, runner, environment, result, and release surfaces end to end where present.
- [x] Separate interaction, trajectory, native project, rendered temporal output, creative quality, professional acceptance, capability, reliability, and readiness.
- [x] Compare directly with DeskCraft, Workflow-GYM, OSWorld 2.0, SciVisAgentBench, Delegate52/artifact-transition, and trajectory-observer evidence.
- [x] Map nonduplicate implications to existing skill-bench contracts without creating a media-specific subsystem.
