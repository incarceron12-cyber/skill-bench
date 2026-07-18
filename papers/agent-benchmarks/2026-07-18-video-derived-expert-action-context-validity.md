# Video anomaly localization proposes interview targets, not verified expert knowledge

## Source and review status

**Deep review of the complete immutable arXiv v1 paper and its complete author-linked prior paper, plus a time-bounded release audit.**

- **Primary paper:** Ryo Sakai and Kaname Yokoyama, *Anomalous Frame Detection Using VLM-Based Description Comparison for Extracting Expert-Specific Actions and Contextual Decision-Making Scenes with Intra-Video Self-Similarity*, arXiv:2607.11957v1 (12 July 2026), <https://arxiv.org/abs/2607.11957v1>
- **Local PDF:** `data/papers/pdfs/2607.11957v1-video-derived-expert-action-context-validity.pdf` (16 pages; 2,003,055 bytes; SHA-256 `14a085c9969b5be3f631ced184070a817615c80f97dda6a4a5a7d161d2df3186`)
- **Complete text:** `data/papers/text/2607.11957v1-video-derived-expert-action-context-validity.txt` (98,216 characters; SHA-256 `2b28b1c90efaefb9fb718f41d27432bd28baabef5dc0a5172cea91db751b1170`)
- **API metadata:** `data/papers/source/2607.11957v1-metadata.xml`
- **Author-linked prior paper:** Ryo Sakai, Yongpeng Cao, and Nobutaka Kimura, *Anomalous Frame Detection by Grouping Frame Similarities between Two Videos Computed by Vision-Language Model to Extract Expert Workers' Unique Actions*, arXiv:2607.10598v1, <https://arxiv.org/abs/2607.10598v1>
- **Prior PDF/text:** `data/papers/pdfs/2607.10598v1-prior-anomalous-frame-actions.pdf` (11 pages; SHA-256 `7f19c480546c1fe6ee129283ba32db3d0e040798a28c467c38fe1e777388c2cd`) and `data/papers/text/2607.10598v1-prior-anomalous-frame-actions.txt` (SHA-256 `c4e1c062e4ce1cb458812be223b345a6bd7c385f8fc390ed61018413b828ee87`)
- **Release audit:** `data/sources/releases/2607.11957v1-video-expert-anomaly/release-audit.json`
- **Release boundary:** neither paper/API record links code, data, annotations, videos, prompts-as-files, configurations, or result ledgers. Exact-title, arXiv-ID, author/title, and GitHub searches on 18 July 2026 found the two arXiv records and third-party mirrors, but no author-verifiable artifact release. This is a time-bounded absence finding, not proof that no differently named or later release exists. The present paper calls the prior work “under review”; the newly acquired immutable prior v1 is the auditable record, not evidence of IEEE acceptance.

## One-sentence contribution and verdict

The paper adds a segment-level, intra-video-self-similarity route to a prior frame-level VLM anomaly detector and reports higher temporal interval overlap on 12 planted scene-difference pairs, but it localizes visually unusual intervals in scripted first-person recordings: it does not observe an expert decision, establish operator expertise, validate the deviation as correct, recover rationale or thresholds, project a benchmark primitive, teach a novice, or measure any downstream consequence.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, C, and E through a bounded maintenance case that probes a general authoring question: can passive work records identify high-value places to ask experts about tacit cues without requiring an interviewer to anticipate every issue? The paper supplies a plausible **candidate-discovery instrument**. Its central validity error is treating a paired-video anomaly as if it already contained verified expert know-how.

The reusable chain is longer:

```text
manual authority and version
+ actor/task/site-qualified paired recordings
→ observed action/scene/state difference
→ detector-ranked candidate interval
→ qualified expert confirms difference semantics
→ expert supplies or rejects contextual rationale
→ corroboration, scope, threshold, exceptions, and consequences
→ authorized benchmark primitive and fair public basis
→ task/check projection
→ held-out agent/novice use and downstream consequence
→ bounded transfer claim
```

No arrow inherits the authority of the previous one. Useful completion is therefore a claim boundary and an authoring workflow that reuses existing provenance, elicitation, participation, artifact-view, task-health, metric, and validity machinery—not a video-specific subsystem.

## Research question and bounded answer

The paper asks whether a training-free VLM pipeline can compare a manual-based work video with an “expert” work video and automatically localize both (1) added or skipped actions and (2) scenes with different targets or locations that might reflect contextual judgment (Introduction and Sections III–IV, PDF pp. 1–8).

The evidence supports a narrow answer:

1. On 15 authored action-pair evaluations, an InternVL2 caption/similarity condition selected on those same pairs obtains mean temporal interval IoU of `0.65`; the prior method rerun on the expanded data obtains `0.59` (Table II, PDF p. 11).
2. On 12 authored scene-pair evaluations, a Qwen3-VL pairwise scene comparator over self-similarity-derived segments obtains mean temporal interval IoU of `0.61`, versus `0.33` for the prior method, `0.46` for direct frame-pair comparison, and `0.43` for whole-video comparison (Table II, p. 11).
3. Segmenting caption sequences before pairwise scene comparison is a plausible way to reduce frame-level description instability and quadratic pairwise cost; the shown failure also demonstrates that the prompt defines what can be observed (Sections IV-D–E and VI, pp. 7–12).

The paper does **not** establish candidate event precision/recall, calibrated discovery coverage, independent expert-label reliability, real expertise, tacit knowledge, decision rationale, safe omission, professional correctness, transfer into guidance, novice learning, operational benefit, or generalization beyond the small scripted indoor setup.

## Methodology and system reconstruction

### 1. Paired recording design

The input is a first-person manual video `V_M` and a first-person purported expert video `V_E`. The authors define three detectable difference types (Sections III and V, pp. 3–9):

- **A: added action** in `V_E`, such as checking an outlet box or related equipment before breaker shutdown;
- **B: skipped manual action**, such as omitting a door check or not removing PC memory; and
- **C: different work scene**, including a different distribution board/room, different lighting, an opened door, equipment on a desk, or an action that moves the operator to a different target.

These are not naturally occurring expert incidents. The experiment says a “worker” first follows the manual and then performs a recording while **adding actions corresponding to expert behavior**, omitting specified actions, or using a different scene (Section V-A, p. 8). No count of unique operators across all tasks, qualifications, maintenance role, experience, selection rule, expert/novice contrast, independent task authority, or evidence that any added/skipped behavior came from actual expert practice is reported. The action and scene conditions are constructed targets for anomaly localization.

The 27 headline “task scenarios” are 15 action-pair evaluations plus 12 scene-pair evaluations, not 27 independent professional tasks (Section V-B, pp. 8–10):

- action pairs: 7 for task 1, 7 for task 2, and 1 for task 3;
- scene pairs: 8 for task 1 and 4 for task 2;
- at least one task-1 and one task-2 scene pair are explicitly reused from action extraction;
- manual recordings and actors are reused across multiple pairings; and
- only three task scripts are represented.

The observational clusters are therefore task, building, actor, manual recording, expert recording, and pair—not 27 independent units. The paper reports only the pair-macro mean.

### 2. Frame-level action pipeline

For every frame, a VLM `M_cap` receives a prompt asking for the concrete visible action and target while avoiding location or goal. Captions are “cleaned” by replacing each frame's caption with whichever caption in that video's caption pool best matches the image in a joint image-text embedding. Corrected captions are embedded with ImageBind, and all cross-video cosine similarities form an `N_M × N_E` map (Section IV-B, pp. 5–6; Appendix A-C, p. 13).

For each target-video frame, the method takes its maximum similarity to any frame in the other video. A frame is anomalous when that maximum is at most `τ` times the average of all framewise maxima. The reported interval is the **first through last** anomalous frame (Section IV-C and Algorithm 1, p. 6).

The current paper chooses scan direction from video length: if `N_M < N_E`, it assumes an expert-added action and scans columns; otherwise it assumes a skipped action and scans rows (p. 6). This is a brittle semantic shortcut. The immutable prior paper instead explicitly assumes addition-versus-skip type is known from task definition or expert annotation (prior Section III, PDF pp. 3–4). Duration does not identify action semantics: pacing, pauses, camera startup, repeated steps, and irrelevant footage can reverse the inference. The current paper neither highlights nor validates this changed assumption.

The first-to-last rule also collapses potentially disconnected low-similarity frames into one continuous candidate interval. A stray false positive before or after the true event expands the entire prediction. The reported IoU penalizes that span, but the output representation hides candidate count, fragmentation, false alarms, and review burden.

### 3. Segment-level scene pipeline

For scene candidates, the method reuses corrected captions to build a self-similarity matrix within each video. It binarizes each matrix at OpenCV grayscale threshold `100`, finds diagonal connected components above an unspecified area threshold, and treats their diagonal extents as semantically stable video segments (Section IV-D, pp. 6–7).

For every cross-video segment pair, frames are sampled at equal intervals. Qwen3-VL-Instruct sees image pairs and answers whether they show the same location. SentenceBERT compares the free response with “Yes” and “No” templates; a dissimilarity probability above `0.5` yields a zero. If **any** sampled pair is judged different, the entire segment pair gets similarity zero. The action filter is then applied column-wise to identify an interval in `V_E` (Section IV-E, pp. 7–8).

This is a location/scene detector, not a decision detector. The VLM is explicitly asked “Do the two images show the same location?” (Appendix A-C, p. 13). It receives no manual clause, system topology, load state, hazard, operator intention, alternative considered, or consequence. Figure 11's failure is revealing: an open versus closed panel door is missed because both images are at the same location; the authors correctly attribute the miss to prompt granularity (Section VI, p. 12). The observer cannot recover a construct absent from its evidence view and question.

The “sampling process was performed five times” (Section V-C, p. 10), but the paper does not define whether the reported `0.61` is averaged over five stochastic frame samples, which seeds/frames were used, whether each pair contributes five dependent observations, or the variance across repeats. The connected-component area threshold, frame rate/downsampling, sampled-frame count per segment, model snapshots, decoding, hardware, batching, and invalid-output policy are also absent.

### 4. Ground truth and metrics

An unspecified person manually annotates one start/end interval for each target action or scene. The paper reports no annotator count, expertise, instructions, blind status, adjudication, repeated labels, boundary tolerance, action/scene ontology, alternative valid intervals, or agreement (Section V-C, pp. 9–10).

`Acc_union` is temporal interval intersection-over-union, computed per pair and averaged across pairs. For action pairs, a wrong addition-versus-skip direction is forced to zero. Thus the headline `65%` and `61%` are **mean interval IoUs**, not “extraction rates” in the usual recall sense and not accuracies over frames or candidates. They do not reveal:

- whether every intended event generated a candidate;
- how many extra candidates a reviewer would inspect;
- frame/event precision and recall;
- false-positive duration or candidate-review minutes;
- performance by actor, task, site, anomaly type, or full/partial scene change; or
- uncertainty over pairs, recordings, labels, or model calls.

A method that proposes one broad interval can score moderate overlap while imposing high review burden; a method that finds a useful sub-event can score poorly despite enabling elicitation. A candidate-discovery instrument needs both coverage and burden denominators.

### 5. Comparators and selection

The action comparison includes the prior BLIP-2 method, whole-video Qwen3-VL, direct pairwise Qwen3-VL, and the proposed frame pipeline. The authors test five caption VLMs on the same 15 action pairs and choose InternVL2 because its `0.65` is highest (Table I, p. 10). The `0.65` is therefore model-selection performance, not untouched confirmatory performance.

The action threshold `τ=0.6` is inherited “with reference to” the prior work. The prior immutable paper chose `0.6` through a sensitivity sweep on 11 task-1/task-2 pairs that substantially overlap the present action setup and reported `0.669` on those same tuning data (prior Sections V–VI, PDF pp. 6–8). The current `0.65` should not be described as dataset-independent zero-shot validation.

The scene comparison includes the prior frame method, five prior-plus-location-prompt variants, whole-video comparison, naive direct frame pairing, and the proposed segment pipeline. However:

- models and parameter counts differ across conditions;
- the whole-video method requires a human to normalize free-form timestamps for scoring (Appendix A-B, p. 13);
- model snapshots, call counts, tokens, hardware, and complete resource use are absent;
- no paired per-pair results or uncertainty are provided; and
- scene thresholds and segmentation choices have no held-out tuning account.

The reported inference times—roughly 0.5–36 minutes per pair—show practical variation, but the unit, hardware, video duration/frame count normalization, preprocessing cache, and five-sample accounting are not specified. They do not establish comparable cost or deployability.

## Evidence interpretation

### What is genuinely learned

1. **Passive records can support anomaly-first elicitation.** Manual/expert video comparison can surface intervals an interviewer might not nominate in advance.
2. **Semantic segmentation can stabilize coarse visual comparison.** On this authored sample, segment-level scene comparison materially exceeds the paper's frame-level location-prompt variants.
3. **Observer prompts define the candidate construct.** “Same location?” detects location differences and misses state differences at one location; this is direct evidence for evidence-view and criterion alignment.
4. **Action and context require distinct evidence.** A visible extra step, a different target, and the reason for selecting that target are separate objects even if they occupy the same interval.
5. **Candidate retrieval is a useful but low claim rung.** Automating where to look may lower expert-review cost without automating what the interval means.

### What the headline numbers do not license

- `27` is the sum of 15 action-pair and 12 scene-pair evaluations with explicit reuse, not 27 independent tasks or incidents.
- `65%` and `61%` are pair-macro temporal IoUs, not event recall, candidate correctness, expert-knowledge coverage, or learning rates.
- a visible difference from a manual is not automatically expert-specific, safe, effective, or tacit;
- a different room, panel, lighting condition, or door state is not evidence that an expert made a contextual decision;
- a scripted worker performing an “expert behavior” does not establish expert authorship or authority;
- a manually planted and annotated target is not discovery of previously unknown know-how;
- localization does not codify rationale, cue, threshold, exception, source authority, or consequence;
- no novice or agent consumes the candidate, and no behavior, artifact, safety, efficiency, or training outcome is measured.

## Unique insight for `skill-bench`

> **Video difference detection should be treated as a proposal generator for critical-incident elicitation, not as an expertise extractor. Its output is an evidence-located question: “what, if anything, made this deviation appropriate here?”**

This changes benchmark authoring. Instead of promoting an anomalous interval directly into a hidden check, use it to create a review packet:

```yaml
candidate_interval:
  manual_video: {id: ..., version: ..., frames: ...}
  comparison_video: {id: ..., actor_role: ..., frames: ...}
  detector: {component_hash: ..., prompt: ..., score: ..., repeat: ...}
  observed_delta:
    type: action_presence | action_absence | target | location | state | timing | unknown
    observer: model_proposal | analyst_confirmed
  confounds: [camera, lighting, pacing, site, equipment_state]
  expert_disposition: approved_difference | incidental | unsafe | wrong | unresolved
  rationale_claims: []
  authority_scope: ...
  public_basis: ...
  primitive_projection: cue | threshold | contradiction | procedure | exception | failure_signature
  consequence_evidence: ...
```

The highest-value candidates are not necessarily the largest visual anomalies. A subtle gauge reading, sound, force, timing change, omitted step, or off-camera state may drive expert judgment while producing little visual difference. Conversely, a different building can dominate pixels/captions while being irrelevant. Discovery evaluation should therefore report a **risk–coverage–burden frontier**: authoritative incidents recovered, false/irrelevant proposals, omitted incident classes, review minutes, and consequence-weighted misses.

A second insight is that the manual/expert contrast has no intrinsic direction of truth. Manuals can be incomplete or stale; experts can use legitimate alternatives, local workarounds, unsafe shortcuts, or habits. Benchmark authoring must preserve three authorities separately: the manual's normative scope, the actor's demonstrated practice, and independent evidence about consequences. “Expert skipped it” cannot become a rewarded omission without adjudication.

A third insight is that “decision scene” must be decomposed into at least four records:

1. **observable context:** target, location, state, timing, tool, or surrounding evidence;
2. **choice set:** available actions/targets and constraints;
3. **decision rationale:** cue, trade-off, threshold, exception, uncertainty;
4. **consequence:** what happened or would fairly happen under alternatives.

The paper measures only coarse parts of the first. A benchmark claim about judgment needs all four, with authority and uncertainty.

## Relation to adjacent evidence

- **ACTA/CDM:** video anomalies can nominate concrete incidents for a Simulation Interview or Critical Decision Method probe. ACTA supplies the missing timeline, cues, options, difficulty, novice errors, and read-back. The anomaly detector should select interview targets; it does not replace elicitation.
- **ArtisanCAD:** recordings/macros show performed operations but not the semantics added during abstraction. Both require field-level transformation provenance and expert approval before a model/analyst interpretation is called expert procedure.
- **Vibe Calibration:** physical execution, acceptance gates, and consequences can validate a procedure. The present paper stops before rationale, gates, state mutation, or consequence; it is far lower on the transfer ladder.
- **SciDiagramEdit:** a before/after delta is a naturally occurring candidate transition, not self-authenticating intent. The video case is weaker because its deltas are scripted rather than naturally accepted professional revisions.
- **Context-Mediated Domain Adaptation:** an observed edit/delta and a model-generated interpretation have different authorship. Here, a VLM's location/action anomaly is likewise a proposal requiring contributor/expert disposition.
- **Artifact-view admissibility:** first-person RGB frames are one representation. They cannot observe off-camera instruments, force, sound, hidden topology, manual authority, or rationale. Missing evidence must produce `insufficient_evidence`, not “no know-how.”

Existing expertise-transfer, participation, elicitation template, task projection, artifact-view admissibility, metric-monitoring, task-health, and validity-argument machinery can represent these boundaries. The blocked real elicitation-session contract remains the right eventual test; no duplicate video schema or queue task is warranted.

## Limitations and validity threats

1. **Scripted rather than natural expertise.** Workers are instructed to add, omit, or relocate predefined behavior.
2. **No operator authority.** Unique worker count, qualifications, experience, maintenance role, and selection are absent.
3. **No manual authority record.** Manual source, version, approval, completeness, validity time, and local applicability are absent.
4. **Deviation is presumed valuable.** Added actions may be redundant; omissions may be unsafe; environmental changes may be irrelevant.
5. **No expert/novice contrast.** The study cannot show that detected behavior is expert-specific.
6. **No rationale evidence.** No interview, think-aloud, stimulated recall, cue report, choice set, threshold, or uncertainty is collected.
7. **No consequence evidence.** Safety, quality, time, error prevention, and downstream state are unmeasured.
8. **Headline unit inflation.** Fifteen action pairs plus twelve scene pairs are called 27 scenarios despite pair reuse and only three task scripts.
9. **Cluster dependence.** Actors, manual recordings, expert recordings, tasks, and buildings are reused without cluster-aware analysis.
10. **Action/scene overlap.** The same pair can be both an action and scene evaluation; the estimands are not exclusive.
11. **Ground-truth authorship is unspecified.** There is no annotator count, expertise, protocol, agreement, or adjudication.
12. **One interval per pair.** The design excludes realistic multiple anomalies and disconnected events.
13. **First-to-last collapse.** Disconnected false positives become one broad span, hiding candidate fragmentation.
14. **Misnamed metric.** `Acc_union` is interval IoU, while prose calls it extraction rate or accuracy.
15. **No retrieval denominators.** Event/frame precision, recall, candidate count, false duration, and review burden are absent.
16. **No uncertainty.** There are no per-pair values, distributions, intervals, tests, or cluster bootstrap.
17. **Undefined five repetitions.** Sampling-repeat aggregation, seeds, variance, and dependence are not explained.
18. **Model selection on evaluation pairs.** InternVL2 is chosen as the best of five on the same 15 action pairs used for reporting.
19. **Threshold reuse/tuning overlap.** `τ=0.6` comes from prior sensitivity analysis on substantially overlapping task structure/data.
20. **Direction heuristic is invalidated neither theoretically nor empirically.** Video length is used to infer addition versus omission.
21. **Prior/current assumption drift is not discussed.** The prior assumes known deviation type; the current implementation substitutes length.
22. **Scene label is visually constructed.** Different building, room, lighting, door state, or target is not a labeled decision rationale.
23. **Prompt under-observes state.** “Same location?” predictably misses open-versus-closed state at one location.
24. **Any-pair segment rule may amplify noise.** One sampled “No” marks the whole segment pair dissimilar; false-positive behavior is unreported.
25. **Segmentation under-specified.** Connected-component area threshold, frame sampling count/rate, preprocessing, and boundary behavior are absent.
26. **Model/configuration identity is incomplete.** Exact checkpoints, decoding, seeds, libraries, hardware, invalid outputs, and retry policy are missing.
27. **Baseline parity is incomplete.** Models, prompts, human post-processing, and resources differ.
28. **Compute comparison is not reproducible.** Per-pair time lacks hardware, video size/frame count, caching, and repeat accounting.
29. **No released evidence pack.** Videos, annotations, pair manifests, outputs, per-pair scores, and analysis code are unavailable.
30. **No held-out task/site/actor test.** All evidence is internal to three simulated indoor scripts.
31. **No temporal-knowledge evaluation.** Speed, timing, ordering, and reordering are explicitly outside the method.
32. **RGB observability ceiling.** Off-camera state, sound, force, instrument readings, and organizational context can be expert-critical.
33. **No codification artifact.** The study produces intervals, not validated rules, source packs, procedures, or rubrics.
34. **No recipient test.** Novice uptake, correction burden, retention, and performance are absent.
35. **No operational safety evidence.** Critical-infrastructure motivation does not make simulated localization evidence safety-valid.
36. **Generalization is untested.** The authors appropriately leave broader practical tasks to future work.

## Reproducibility and operational realism

**Manuscript reproducibility is strong:** immutable current and prior PDFs, complete text extractions, metadata, hashes, exact equations, and appendix prompts are preserved. The prior audit is particularly useful because it reveals the original known-direction assumption and same-data threshold sweep.

**Experimental reproducibility is poor.** A third party cannot reconstruct a reported row without the 27 pair identities, source recordings, exact frames, labels, overlap graph, model/checkpoint snapshots, frame extraction settings, caption outputs, segment boundaries, sampled image pairs, repeats/seeds, invalid-output handling, hardware, per-pair scores, or table builder. The paper provides enough detail to build a similar detector, not reproduce its evidence.

**Operational realism is low to moderate for authoring triage and low for knowledge transfer.** Positive features are egocentric video, multiple rooms/buildings, action additions/omissions, scene/state changes, training-free models, and minutes-scale processing. Negative features are scripted anomalies, one anomaly per pair, stable indoor conditions, no authenticated experts, no live manual authority, no safety adjudication, no workflow integration, no review burden, no downstream trainee, and no released records. It is a formative detector study, not a maintenance-training or critical-infrastructure validation.

## Transfer to `skill-bench`

### Retain

1. Use passive artifact/video differences to **propose** critical incidents that structured interviews may miss.
2. Preserve action, target/location, object state, timing/order, and hidden-context anomalies as distinct candidate types.
3. Store detector prompt/evidence view because observability and criterion wording determine what can be surfaced.
4. Keep candidate localization separate from semantic authorization and benchmark projection.

### Repair before use

1. Freeze manual/source authority, paired-recording lineage, actor role, task/site/state covariates, and recording transformations.
2. Require a qualified expert disposition for every proposed interval: relevant, incidental, unsafe, wrong, ambiguous, or unresolved.
3. Follow approved intervals with ACTA/CDM probes for cues, options, thresholds, exceptions, novice contrast, and consequences; preserve exact video/frame locators and read-back corrections.
4. Evaluate discovery with event precision/recall, consequence-weighted recall, false/irrelevant proposal rate, interval burden, expert review minutes, and cluster-aware uncertainty—not only temporal IoU.
5. Hold out actors, sites, task forms, and anomaly classes; separate detector development, threshold/model selection, and confirmatory evaluation.
6. Compare RGB-only detection with additional admissible evidence views where the construct requires audio, instruments, force, logs, manuals, or system topology.
7. Project only expert-approved, source/corroboration-backed claims into public requirements/private consequences; an anomaly alone must never become a hidden obligation.
8. Test the complete transfer chain: anomaly-guided elicitation versus unguided ACTA, accepted primitive quality, task/check validity, agent or novice uptake, correction burden, and downstream consequence.

## Action items

- [x] Read and verify the complete immutable v1 paper and preserve its PDF/text/metadata paths and hashes.
- [x] Acquire and read the complete author-linked immutable prior v1 paper; verify its method, threshold selection, data overlap, and known-direction assumption.
- [x] Audit exact-title/arXiv/author/GitHub release surfaces and preserve a time-bounded release record.
- [x] Reconstruct pair collection, frame/segment pipelines, comparators, labels, metric semantics, and exact pair denominators.
- [x] Separate visual difference, candidate retrieval, expert-authorized interpretation, rationale, primitive projection, recipient uptake, and consequence.
- [x] Map implications to existing cross-domain machinery. No nonduplicate build/consolidation task is justified.
- [ ] If a consented real elicitation pilot becomes available, compare unguided ACTA with anomaly-nominated incident probing under the existing blocked session-contract gate; do not simulate testimony.
