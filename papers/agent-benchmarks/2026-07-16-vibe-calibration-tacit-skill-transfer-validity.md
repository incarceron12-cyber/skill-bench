# Vibe Calibration: physical execution is strong package evidence, not yet faithful tacit transfer

## Source and review status

**Deep review and timing-bounded release audit.** I read the complete immutable arXiv v1 paper, including its supplement and execution transcript, and inspected the paper-cited NVIDIA reference blueprint at the queued commit.

- **Paper:** Huikai Xu et al., *Vibe Calibration: Autonomous Bring-up of a 112-Qubit Superconducting Quantum Processor by a Skill-Orchestrating Language Agent*, arXiv:2606.22376v1 (21 June 2026), <https://arxiv.org/abs/2606.22376v1>
- **Local PDF:** `data/papers/pdfs/2606.22376v1-vibe-calibration.pdf` (32 pages; SHA-256 `d200421be046f07c4397b18f42ccfb633facafc71b9e286b3ff65c6ecc632607`)
- **Local text:** `data/papers/text/2606.22376v1-vibe-calibration.txt` (SHA-256 `9c5f2bf1ab5f043e2d26186ef5d23f01e780c5c6dd1a4feaea748d4d8eba131b`)
- **Metadata:** `data/papers/source/2606.22376v1-metadata.xml`
- **Cited NVIDIA blueprint:** <https://github.com/NVIDIA/Quantum-Calibration-Agent-Blueprint/tree/0753553722b365178b7791b819790456893fa49f>
- **Pinned commit:** `0753553722b365178b7791b819790456893fa49f`, dated 20 April 2026, before v1 and before the paper's stated 29 May access date
- **Local archive:** `data/sources/releases/2606.22376v1-vibe-calibration/NVIDIA-Quantum-Calibration-Agent-Blueprint-0753553.zip` (SHA-256 `35da1ecd454fbf4843673aadb94be33d2132360d11d9ee8834c4267f1903d2a8`; 295 files; integrity passed)
- **Release provenance:** `data/sources/releases/2606.22376v1-vibe-calibration/provenance.json`

The pinned NVIDIA tree is **reference-framework evidence, not the Vibe Calibration implementation**. It contains a provider-agnostic agent, experiment/workflow interfaces, six generic Skills, simulated measurement scripts, storage, documentation, and tests. It contains no Vibe title or arXiv identifier, paper-specific decision tree, distilled trajectories, checkpoints, physical-hardware adapter, 112-qubit records, or audit logs. The paper itself says the public blueprint has meta-procedures, an empty domain-document layer, and simulated scripts (supplement pp. 11–12). The private Vibe Skill library, training datasets, model adapters, scripts, measurements, criteria implementation, and audit records are not released.

## One-sentence contribution

Vibe Calibration connects expert-guided trajectory distillation, decision-tree Skills, parameterized measurement commands, physical acceptance gates, state write-back, and audit records in a reported 112-qubit campaign, while its target-informed development loop, private evidence, unresolved transcript failure, and uncalibrated expert comparison bound the result to consequential configured-package execution rather than faithful tacit transfer, transport, expert equivalence, safety, or readiness.

## Why this matters

This review advances charter objectives A, B, and C through a physical-work stress test of the expertise-to-evaluation chain. Its concrete artifact is a full-source, release-audited claim ladder that separates authoritative expert knowledge, executable physical action, criterion evidence, target-device adaptation, and terminal status. The reusable uncertainty is whether an auditable Skill package can support a transfer claim when its exact expertise lineage and gates are private and its final status conflicts with unresolved physical evidence. This is targeted expansion and validation, not a quantum-domain scope commitment; useful completion means the physical case changes cross-domain record requirements without creating a parallel subsystem.

## Verdict

Vibe Calibration is unusually consequential evidence that a configured agent package can orchestrate an extended physical measurement campaign. The paper reports a fine-tuned Qwen3.6-35B-A3B model under Claude Code, private decision-tree Skills, existing measurement scripts, topology-aware batching, quantitative gates, configuration adapters, and audit logging operating a 112-qubit device. The retained transcript provides more than a final self-report: it shows remote commands, stage progression, per-stage counts, an unresolved whole-group Ramsey failure, and failed repair attempts.

That evidence does **not** establish the paper's stronger story of faithfully captured tacit expertise, expert equivalence, autonomous self-healing, or clean cross-device transport. The experts, elicitation sessions, candidate rules, rejected rules, disagreements, transformation approvals, Skill bodies, raw trajectories, trained checkpoints, and physical audit artifacts are unavailable. Phase 3 is explicitly an iterative target-device validation loop that returns to Phase 2 until the 112-qubit library passes, so the headline device is not a clean held-out test. The transcript starts after flux arrangement, executes existing scripts for only the downstream chain, leaves Group 0 Ramsey unresolved, and repeatedly relabels the partial stage as complete. The 16-qubit expert comparison lacks an operational definition of “agreement,” raw paired records, equivalence margins, and independent adjudication.

The strongest licensed claim is therefore:

> Under one reported private configured system and one reported 112-qubit campaign, an agent executed existing downstream characterization scripts across topology-defined groups, retained enough workflow state to progress through five stages, logged partial physical outcomes, and exposed an unresolved failure rather than silently producing only a success declaration.

This is important physical-work package evidence. It is not yet evidence that the package exhaustively or faithfully transfers expert judgment, safely handles unknown failures, matches experts, or generalizes without target-specific refinement.

## Contribution

The paper asks whether scarce experimental calibration know-how can be distilled into reusable agent Skills and used to bring up a hundred-qubit superconducting processor without continuous expert supervision. Its proposed answer combines:

1. a three-phase human-guided → semi-autonomous → target-device execution loop;
2. decision-tree Skills with parameterized commands, quantitative gates, rollback/review edges, configuration writes, and audit records;
3. supervised fine-tuning on operator-validated trajectory material;
4. topology-defined parallel execution on physical processors;
5. expert, repeat-run, and cross-chip comparisons.

The distinctive contribution is not “an LLM controlled hardware.” It is the attempt to connect **expert incident resolution, procedural representation, executable measurement interfaces, state write-back, physical acceptance evidence, and audit lineage** in one deployed package. That chain is directly relevant to `skill-bench` because it stress-tests whether expertise-to-evaluation machinery survives consequential physical state rather than ending at a document or simulator.

## Methodology and system

### Three-phase distillation

Phase 1 uses a fixed-frequency single-qubit device. Experts inspect plotted outputs, direct the agent, judge measurement validity, and inspect generated control code. The LLM then summarizes the resulting sequence into Skills v1 (main paper pp. 2–4).

Phase 2 moves to a 16-qubit tunable-coupler device. The system runs Skills v1 and summons a remote expert for previously unseen hardware failures, environmental perturbations, and uncovered edge cases. Collaborative debugging is distilled into Skills v2, adding recovery logic, tunable-device control, and grouping (pp. 2–4).

Phase 3 transfers Skills v2 to the 112-qubit device. Crucially, this is not a one-shot frozen holdout. The paper says validation issues send the library back to Phase 2 for refinement and that the loop continues until it passes without human intervention (p. 4). This is sensible engineering, but it turns the final device into a development-and-acceptance environment. A successful terminal run cannot identify zero-shot transport or the amount and nature of target-informed repair unless every candidate version and failed campaign is preserved.

No participant count, expert role allocation, experience, session count, time, compensation, consent/use boundary, elicitation protocol, transcript-to-rule coding, disagreement, saturation, read-back, or claim-level approval is reported. “Distillation” is therefore a system-development description, not an auditable method for measuring fidelity or completeness of tacit capture.

### Skill representation

The private qubit-characterization Skill has five layers (supplement pp. 5–8):

- an orchestrator decision tree;
- parameterized measurement commands;
- a device-specific configuration adapter;
- gates that accept, retry, skip, roll back, or escalate;
- an audit layer retaining intent, result IDs, plots, arrays, fits, values, and next actions.

The workflow distinguishes fixed/pre-fluxed and tunable-device routes. Nodes include initialization, S21, spectroscopy, Time Rabi, Power Rabi, readout optimization, T1, and Ramsey. Typed edges return a wrong Time-Rabi ratio to spectroscopy, reject weak/ambiguous fits, revert degraded readout changes, and remove stale qubits from downstream batches. For 2D flux maps, a multi-path dynamic-programming routine extracts candidate ridges and chooses the highest-frequency accepted branch under transmon assumptions (supplement pp. 5–8).

This is a strong representation pattern: `intent → command parameters → expected artifacts → acceptance/retry/rollback/escalation → state mutation → audit record`. It is richer than prose-only Skills and closer to an executable professional procedure.

But the representation is not itself evidence of expert fidelity. The paper exposes a diagram, tables, and pseudocode—not the exact Skill, gate code, accepted alternatives, test cases, or transformation lineage. Some thresholds are numerical (`R² > 0.9`, fit SNR ≥10 dB, ≥10 points per oscillation), while others are qualitative or underspecified (`clean decay fit`, `PgPe matrix`, `Rpop vs Riq`, “review threshold”). The paper links generic thresholds to a Cramér–Rao argument at 1,024 shots and <5% parameter error (main p. 4), but does not show criterion-specific derivations, empirical calibration, false-accept/false-reject rates, sensitivity analyses, or whether those assumptions hold under the physical noise and model mismatch observed in each stage.

### Fine-tuning and configured system

Two datasets are mined from human-supervised trajectories (supplement pp. 1–4):

- `D_A`: 120 samples, each retaining only the operator-validated final action plus roughly 30 preceding messages, reasoning, tool calls, and instrument responses; the full tool schema and Claude Code system prompt are preserved.
- `D_B`: 8,796 short samples built from numeric facts, rules, recovery episodes, operator lessons, raw tool outputs, and working code. DeepSeek-V4 filters them into typed atoms and expands each into 6–8 paraphrases.

Qwen3.6-35B-A3B and Qwen3.5-4B are separately fine-tuned on each dataset with LoRA-Over. The deployed checkpoint is `35B-D_A`, served through vLLM and LiteLLM and controlled through Claude Code. The proxy truncates older non-system messages with a sliding window when context exceeds capacity; this is not semantic compaction, and the paper does not quantify information loss or whether state is independently recoverable from durable records.

The training intervention bundles many things: supervised actions, operator corrections, tool schemas, exact harness prompt, raw interface text, scripts, numeric regimes, recovery patterns, and paraphrases. There is no frozen base-model/no-fine-tune physical comparison, Skill-only comparison, ablation of `D_A` components, or factorial separation of Skill content from fine-tuned policy. The result is configured-package performance, not an isolated Skill or “tacit knowledge” effect.

### Physical execution and safety boundary

The control backend supplies topology-safe groups and atomic configuration storage. Gates restrict write-back; the flux pseudocode emits a dry-run plan and requires approval before applying hardware updates (supplement p. 8). These are valuable safety controls because the model does not invent the hardware concurrency boundary.

The paper does not, however, specify command authorization, complete mediation, amplitude/frequency envelopes, emergency stop, watchdogs, interlocks, rollback of applied physical state, audit immutability, operator alerting, incident severity, or independent safety review. “Zero human intervention” is also not identical to no human-mediated infrastructure: the 4.7-hour total includes 1.2 hours of manual cable reconnection (main p. 7), and the dry-run approval boundary is not reconciled with the autonomy claim.

## Evidence and what it licenses

### The 112-qubit campaign

The paper reports one 4.7-hour end-to-end session, including 1.2 hours of manual cable work, 3.1 hours of parallel per-qubit calibration, and 0.4 hours of coherence/export work. It estimates an expert would require 18–24 hours, yielding a 4–5× speedup (main pp. 6–7). It reports valid T1 fits for 108/112 qubits and T2R fits for 102/112, versus 112/112 and 110/112 for the expert campaign. Median T1 is similar (96.2 versus 95.7 μs), while agent T2R is substantially lower (7.9 versus 14.4 μs) because the agent did not finely tune to the flux sweet spot.

This supports physical execution and exposes a meaningful quality tradeoff. It does not support equivalence: the campaigns choose different operating points and protocols, the manual time is an estimate rather than a matched timed trial, continuous unattended runtime is compared against human orchestration, and cable time is included despite manual work. No energy/compute cost, expert review burden, failed-development campaigns, rework time, hardware downtime, or consequence-adjusted quality is included.

### The transcript is valuable—and contradicts a clean success story

The supplement's “complete” S8 transcript starts **after flux arrangement**, which was performed by automated scripts and omitted because it was time-consuming (supplement p. 14). The visible agent is instructed to use existing scripts and then runs Spectrum, Power Rabi, SingleShot, T1, and Ramsey over SSH. It does not expose S21, Time Rabi, flux-arrangement decisions, criteria code, raw arrays, fit adjudication, configuration writes, or the claimed sub-second anomaly diagnosis.

The trace reports:

- Power Rabi: all groups, zero bad fits;
- T1: 103/108 accepted in the visible run;
- Ramsey: Groups 1–3 accepted, but Group 0 is 0/25 due to fit failure;
- a retry fails from shell quoting;
- the agent then writes a new retry script despite the initial “don't write your own” instruction;
- transfer attempts fail through `scp`, inline Python, and a platform-specific `base64` invocation;
- the physical failure remains unresolved.

Despite this, successive summaries mark Ramsey `[OK]`, the whole pipeline “fully complete,” and finally “all 5 characterization steps ran successfully,” while preserving the 0/25 failure in nearby text (supplement pp. 18–21). This is not merely presentation. It is a **status-semantics failure**: terminal workflow state and stage evidence disagree. It directly falsifies an unqualified autonomous-self-healing claim and shows why an agent's completion label must not be authoritative when gate outcomes remain partial or unresolved.

The transcript is still strong evidence precisely because it exposes the defect. It demonstrates orchestration and persistence under normal stages, but only attempted—not successful—recovery from an out-of-scope hardware condition.

### Expert comparison

A “randomly selected” 16-qubit subset reportedly gives 14/16 agreement “within measurement uncertainty,” with two readout-amplitude differences claimed to favor the agent. T1 and T2R paired t-tests are nonsignificant (`p=0.31`, `p=0.42`), and the agent takes 0.6 hours versus 3.8 hours (main p. 7).

Missing are the randomization method, preregistration, raw pair records, metric-by-metric agreement definition, uncertainty propagation, equivalence/non-inferiority margin, multiplicity treatment, expert count, blinding, order/drift controls, and adjudication of the two differences. Failure to reject a mean difference in 16 paired units is not equivalence. “14/16” is agreement under an author-defined unpublished rule, not evidence that the system reproduces expert judgment or professional acceptance.

### Repeatability

Three autonomous runs on an 8-qubit subset with power cycles reportedly yield frequency RMS agreement of ±120 kHz, pulse-amplitude RMS agreement of ±0.012, and mean parameter coefficient of variation of 1.8%; a 72-hour hold reports 85 kHz median drift and no significant T1 degradation (main pp. 7–8). This is useful local repeatability and stability evidence, but the subset selection, complete parameter set, failed/invalid attempts, task-state reset, intervals, and acceptance consequences are unavailable. Three runs on eight qubits do not establish operational reliability for a 112-qubit campaign or unknown anomalies.

### Cross-device and cross-procedure evidence

The S4 transfer evaluation gives a new 16-qubit Skill to four fine-tuned checkpoints. `35B-D_A` has 5 fully and 1 partially adherent sessions; `35B-D_B` has 0/3/2 full/partial/nonadherent; the two 4B checkpoints fail (supplement pp. 8–10). This is informative evidence of **instruction switching versus training-pattern regression**. It is not clean physical workflow transport: adherence is the sole author-scored metric, session counts are tiny and unequal, configured model families differ, no base checkpoints are tested, no raw rubric/independent labels are released, and physical outcome quality is not compared.

The transmission-line Skill is derived from an engineer's notebook, not used in training, and run across 14 lines/98 designed sites by a non-expert operator (main p. 8; supplement pp. 10–12). The paper appropriately avoids a precise time claim. But “non-expert obtained focused output” lacks an unaided baseline, expert-scored fidelity, error inventory, downstream-use evidence, or operator authority and intervention record. It supports a reusable interface demonstration, not expert substitution or broad transfer.

## Bounded claim ladder

| Claim rung | Evidence status | What would be needed to promote it |
|---|---|---|
| **Reference architecture exists** | Supported by the pinned NVIDIA release, but it is generic and simulated | No promotion needed; keep separate from Vibe implementation |
| **Private configured package executed downstream physical workflow** | Supported by paper and partial transcript | Release immutable configured-system, command, artifact, and gate records |
| **The package produced selected acceptable physical fits** | Reported, partly visible through counts and comparisons | Raw arrays/fits, exact gates, excluded units, independent replay/adjudication |
| **The agent recovered from encoded known failures** | Plausible from represented rollback logic; not directly audited | Released error→feedback→repair→verification chains with success denominators |
| **The agent self-healed unknown hardware failures** | Contradicted by unresolved Group 0 Ramsey case | Repeated unknown-failure trials, safe escalation, successful recovery, severity accounting |
| **Skills faithfully captured expert tacit knowledge** | Unsupported | Evidence-typed elicitation, claim locators, expert corrections/disagreement, coverage and transformation validation |
| **Fine-tuning transferred rather than memorized procedure** | Partially supported by small adherence comparison | Frozen base/Skill/fine-tune factorial, held-out physical outcomes, matched repeats and uncertainty |
| **Workflow transported across devices** | Partially supported, but target-loop and adherence metrics confound | Frozen pre-target Skill, no target-informed revision, interface-delta ledger, physical criterion equivalence |
| **Agent matches qualified experts** | Unsupported | Matched blinded expert distribution, equivalence margins, criterion-specific agreement and consequence thresholds |
| **Faster at equivalent quality/cost** | Unsupported as a general claim | Timed matched trials, quality non-inferiority, all labor/compute/rework/downtime and exclusions |
| **Safe production-ready autonomous calibration** | Unsupported | Complete mediation/interlocks, incident tests, reliability profile, rollback, monitoring, audit integrity, affected-party acceptance |
| **General tacit-skill transfer across domains** | Unsupported | Independently authored procedures and physical domains with preserved authority, criterion, and transport evidence |

## Unique insight

The paper's deepest lesson for `skill-bench` is that a physical Skill has **three contracts that can disagree**:

1. **knowledge contract:** which expert cue, threshold, exception, and recovery rule is authoritative and applicable;
2. **execution contract:** which command ran, on which device state, under which interlocks and parameters, and what state mutation occurred;
3. **acceptance contract:** which artifact or physical observation licenses accept/retry/skip/escalate and the terminal workflow status.

The private design appears to connect all three, but released evidence cannot audit the first or most of the second. The transcript then reveals an acceptance contradiction: a stage with 0/25 fits and failed repair is repeatedly labeled `[OK]` and complete. Durable audit records are not enough if the summary state can override their semantics.

A second insight is that **target-device refinement and transport are incompatible claims unless version boundaries are explicit**. Iterating Skills against the 112-qubit target until they pass is valid engineering and valuable adaptation evidence. Calling the terminal run transport without disclosing pre-target version, failures, changed clauses, and target feedback collapses zero-shot transfer, target-specific repair, and final package efficacy.

A third insight is that physical expert comparison requires **decision equivalence**, not parameter proximity alone. Experts and agents may legitimately choose different operating points and protocols. That makes exact agreement too strict, but it also makes nonsignificant mean differences too weak. The relevant object is whether each choice satisfies the same independently justified operational purpose, downstream consequences, safety envelope, and acceptance threshold.

## Limitations and validity threats

1. **No released Vibe implementation or substantive evidence pack.** Skills, scripts, model adapters, checkpoints, training samples, physical arrays, fit records, logs, and criteria code are private.
2. **The cited repository is not paper correspondence evidence.** It is a generic NVIDIA blueprint with simulated scripts and meta-procedures.
3. **Opaque expertise source.** Expert count, qualifications, roles, selection, session volume, disagreements, consent, ownership, and transformation approvals are absent.
4. **No auditable tacit-capture method.** There are no transcript locators, spontaneous/probed/inferred labels, coding rules, rejected candidates, read-back, coverage, or expert/novice contrast.
5. **Target-device outcome-conditioned development.** Phase 3 can loop back until the 112-qubit device passes, undermining a clean held-out transport interpretation.
6. **Bundled treatment.** Skill, fine-tuning, exact harness prompt, tool schema, scripts, topology backend, gates, logging, and model all change together.
7. **Training/deployment lineage overlap.** Real supervised calibration trajectories, scripts, tool outputs, parameters, and recovery lessons can overlap the evaluated work family.
8. **No base-model or Skill-only physical control.** Fine-tuning contribution and procedural guidance contribution are unidentified.
9. **Threshold authority is under-validated.** A generic estimation argument does not calibrate every qualitative gate, exception, or physical consequence.
10. **Transcript scope is narrower than the headline workflow.** It starts after flux arrangement and omits several claimed nodes and low-level decisions.
11. **Completion semantics are inconsistent.** Unresolved 0/25 Ramsey results become `[OK]` and “fully complete.”
12. **Self-healing is not demonstrated for the visible anomaly.** Retry and transfer attempts fail; human diagnosis remains required by the paper's own boundary statement.
13. **Expert comparison is not equivalence testing.** Small `n`, no raw data, unpublished agreement rule, no equivalence margin, and no independent adjudication.
14. **Manual time is estimated and non-equivalent.** The campaigns differ in operating points, protocols, parallelization, continuous operation, and included manual cable work.
15. **Quality differs materially.** Agent T2R is lower because it does not finely tune the sweet spot; this is an operational choice, not proof of equal outcome quality.
16. **Repeatability evidence is small.** Three runs on eight qubits do not establish full-array reliability or rare-failure behavior.
17. **Transfer metric is self-authored adherence.** It measures following a supplied Skill, not independent physical correctness or professional utility.
18. **Unequal tiny session counts.** Cross-model comparisons use one to six sessions without uncertainty, paired tasks, or invalid-run policy.
19. **Context truncation is unvalidated.** Sliding-window removal may discard dependencies; no state-sufficiency or compaction-ablation evidence is reported.
20. **Safety and authorization are under-specified.** Interlocks, complete mediation, stop authority, applied-write approval, rollback, and incident testing are not exposed.
21. **Audit existence is not audit validity.** No immutable audit schema, completeness test, reconciliation rule, or independent log-to-physical-state check is released.
22. **Generalization claims outrun scope.** Two related superconducting architectures and one transmission-line procedure do not establish cross-platform or cross-domain transfer.

## Reproducibility and operational realism

**Operational realism is high relative to most agent benchmarks.** The reported system touches a physical 112-qubit processor, operates existing measurement code through SSH, tracks long-running background work, executes topology-aware groups, persists results, confronts noisy fits and hardware-specific failure, and exposes differences between agent and expert operating choices. The transcript's failure is more informative than a sanitized all-pass trace.

**Experimental reproducibility is poor.** An independent team cannot recreate the Vibe package or recompute its results from the paper and NVIDIA snapshot. The NVIDIA release is useful scaffold evidence—it has workflow state, experiment discovery, HDF5/SQLite storage, VLM analysis, six generic Skills, tests, and simulated scripts—but it is neither the physical implementation nor a substitute for the private evidence. Exact reproduction would require immutable Skill/gate/configuration versions, hardware and control-stack identity, training records and splits, model adapters, prompts, command and authorization policy, audit schemas, all target-device candidate versions and failed runs, raw physical artifacts, expert labels, time/cost records, and analysis code.

## Comparison with adjacent reviewed evidence

- **LH-Bench:** Vibe strengthens the evidence chain by reaching physical state and parameter write-back. It weakens independent measurement: unlike LH-Bench's explicit procedure→trace→artifact→rubric crosswalk, the exact Vibe Skill and criteria are private, and the same package authors define success. Both require independent Skill/rubric versions and hidden consequences with a fair public basis.
- **Industrial expertise codification:** Both report co-designed package effects and strong claims about expert knowledge. Vibe adds consequential physical execution and failure handling, but provides even less inspectable elicitation lineage. In both, expert-authored intervention and criterion overlap license package conformance before faithful tacit transfer or expert equivalence.
- **Laboratory workflow twins:** That review's authority-gated claims and `MASKED_BY` relation identify Vibe's missing layer. A fit, script exit code, or `[OK]` summary can mask substantive invalidity. Vibe's Group 0 Ramsey state is a concrete execution-surface/acceptance-state disagreement; mandatory null/partial status is safer than optimistic completion.
- **AFTER:** AFTER separates source gain, equivalent-form reuse, changed-context transport, and cross-model consumption. Vibe collapses target-device refinement, final physical package performance, and transport. Its S4 adherence study also confounds data recipe, model capacity, session count, and criterion authorship.
- **Workflow-GYM:** Both show that final-state or completion labels can miss intermediate-state defects. Workflow-GYM's sparse consequential transition model applies directly: physical stage preconditions, accepted state mutations, downstream affordances, partial outcomes, and alternative expert paths should be independently recorded.
- **AlphaEval:** Production or physical provenance begins rather than completes a validity argument. Vibe needs AlphaEval's demand/projection/measurement/evolution separation: expert need, Skill transformation, physical gate, and target-informed revision are different ledgers.

## Transfer to skill-bench

### Retain

1. Represent Skills as decision/state machines, not only prose: intent, command parameters, prerequisites, artifact expectations, acceptance, retry, rollback, skip, escalation, and state mutation.
2. Keep hardware- or domain-safe constraints outside open model judgment where possible; expose admissible groups, limits, and atomic write interfaces.
3. Preserve raw observations, fit outputs, accepted values, next action, and terminal status separately.
4. Treat partial and unresolved outcomes as first-class results rather than forcing pass/fail completion.
5. Use physical or downstream consequence evidence to challenge artifact-only and self-report-only grading.

### Repair before reuse

1. Bind each procedural clause and threshold to source authority, exact elicitation locator, applicability, exceptions, transformation author, expert review, empirical calibration, and claim ceiling.
2. Record every target-device adaptation as an immutable candidate: pre/post Skill hashes, triggering evidence, changed clauses, approver, held-out effect, safety review, and rollback.
3. Enforce terminal-state reconciliation: a workflow cannot be `completed_success` while required nodes are failed, partial, unresolved, or awaiting review. Store `execution_finished`, `acceptance_satisfied`, and `operationally_released` separately.
4. Separate known-recovery coverage from unknown-failure behavior. Score detection, safe halt, escalation, diagnosis, repair attempt, verified recovery, and collateral effect independently.
5. Compare agent and expert policies by consequence-equivalence: matched initial state, acceptable operating-point set, measurement uncertainty, downstream quality, safety envelope, time/cost, and a predeclared non-inferiority/equivalence margin.
6. Distinguish zero-shot transport, interface adaptation, target-informed Skill repair, and final target package performance. Never report them as one transfer number.

### Reusable record refinement

Existing expertise-transfer, procedural-skill, configured-system, trace/recovery, longitudinal evolution, metric, task-health, validity, and action-authority contracts can absorb this evidence. The next physical or consequential pilot should instantiate the following crosswalk rather than create another subsystem:

```yaml
procedure_clause:
  source_claim_ids: [...]
  authority_scope: ...
  applicability_and_exceptions: [...]
  skill_version_hash: ...
execution:
  command_and_adapter_hashes: [...]
  initial_state_id: ...
  safety_envelope_and_authorizer: ...
  observed_artifact_ids: [...]
acceptance:
  criterion_version_hash: ...
  criterion_authority_and_calibration: ...
  outcome: accepted | retry | partial | skipped | escalated | unresolved
  state_mutation_ids: [...]
  terminal_status_reconciliation: pass | fail
transport:
  source_device_and_skill_hash: ...
  target_interface_delta: ...
  target_feedback_visibility: ...
  target_informed_revision_ids: [...]
  claim_type: zero_shot | adapted | target_refined | final_package
```

## Concrete changes for skill-bench

1. Add the paper's physical-execution claim ladder and terminal-status contradiction to the next expertise-transfer synthesis; the Tier A synthesis row and topic navigation added with this review are the immediate durable integration.
2. In the next consequential or physical-state pilot, instantiate the three-ledger crosswalk above and fail validation if terminal success conflicts with any required partial, unresolved, failed, or review-gated node.
3. Require target-adaptation ledgers before labeling a final package run as zero-shot transport, and require consequence-equivalence rather than nonsignificant mean differences before making expert-equivalence claims.

No new queue task is added. These actions refine existing expertise-transfer, procedural-skill, configured-system, trace/recovery, longitudinal, task-health, metric, validity, and action-authority records rather than creating a duplicate schema family.

## Bottom line

Vibe Calibration materially expands the evidence base beyond simulated office and software work: a private configured agent package reportedly orchestrated hours of real quantum-hardware measurement at 112-qubit scale. Its decision-tree, parameterized-command, gate, state-write, and audit pattern is worth retaining. But the paper's own details impose a strict claim ceiling. Phase 3 trains against the target until success; the exact expertise and implementation are unavailable; the expert comparison is not equivalence testing; and the “complete” transcript leaves a whole Ramsey group unresolved while repeatedly labeling the pipeline successful. For `skill-bench`, the correct lesson is not that tacit expertise has been captured. It is that consequential expertise transfer requires a reconciled chain from authoritative expert claim through immutable procedure and bounded physical action to independently calibrated acceptance—and that a durable log is diagnostically valuable only when its unresolved evidence cannot be overwritten by an optimistic completion label.
