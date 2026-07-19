# Good Benchmarks: strong practitioner falsification heuristics, not a validated universal task-quality rule

## Source and review status

**Deep review of the complete immutable primary source.** I read the full seven-page arXiv v1 essay, checked the layout-preserving extraction against the retained PDF and TeX source, and audited the roles played by its five citations against locally retained full sources and source-level records. This is a practitioner methods essay, not an empirical benchmark study.

- **Paper:** Ivan Bercovich, *Good Benchmarks*, arXiv:2607.12217v1 (13 July 2026), <https://arxiv.org/abs/2607.12217v1>
- **Local PDF:** `data/papers/pdfs/2607.12217v1-good-benchmarks.pdf` (7 pages; SHA-256 `9ffe44881bf33f9beaa96de400dc195cc1b776b224b808aa29a20aaa695e02a0`)
- **Local text:** `data/papers/text/2607.12217v1-good-benchmarks.txt` (25,409 bytes; SHA-256 `2cc843d67d924f162fa6ed0a54b21abbc91b2f00044a5f65de965fcf5cffe8dd`)
- **Canonical abstract HTML:** `data/papers/source/2607.12217v1-abs.html` (SHA-256 `ccb1ca4fa17340925cb79883e2787b4fde562009b4c24972307c91f179431407`)
- **TeX source:** `data/papers/source/2607.12217v1-source.tar` (SHA-256 `93ae7e9408f7dc6269cf64bbf0b7bd0baab42c220bd65f0d5d27707b1f886c8c`)
- **Related rendering:** <https://ivanbercovich.com/2026/good-benchmarks>. Search results identify this as the author's 12 July personal-blog rendering of the same text; it is not independent corroboration.
- **Release boundary:** the manuscript and canonical arXiv record provide no paper-specific code, task set, review ledger, trial matrix, or artifact-release URL. Exact-title, arXiv-ID, and code searches found the paper, mirrors, and the related blog, but no verifiable paper-specific artifact release. This is evidence about the discoverable release surface at review time, not proof that no private authoring evidence exists.

## Bottom line

The essay's most useful contribution is a compact **task-falsification workflow**. A candidate task should survive an exploratory same-information oracle, independent verifier construction, alternative-valid-solution tests, environment determinism and exploit probes, repeated agent failures, crux alignment, and domain-plus-evaluation review before its difficulty is interpreted as capability evidence. These are valuable review questions because they target concrete failure signatures rather than merely asking whether a task “looks realistic.”

The paper does not test that workflow. It reports no sampling frame, candidate or rejection counts, before/after task versions, reviewer assignments, agreement, defect taxonomy with frequencies, trial matrix, controlled comparison, downstream score changes, cost distribution, or release. Statements such as “very few people” write full requirements, “the hardest tasks tend to be hard the first time,” feedback that does not converge “tends” to indicate trouble, and fewer tasks being better are practitioner generalizations, not demonstrated estimates (Sections 3–10, pp. 2–6).

Several categorical recommendations also become wrong outside a narrow terminal-task construct. “Grade outcomes, not process” cannot govern work where authorization, evidence provenance, safety controls, communication, audit trail, or a mandated professional procedure is itself consequential. “Nothing ambiguous is left” and verifier equivalence are aspirational for deterministic engineering endpoints, but realistic knowledge work can legitimately contain incomplete, conflicting, or judgment-dependent evidence. The repair is not to reject such work; it is to type ambiguity, authority, admissible alternatives, evidence views, decision thresholds, and human adjudication while bounding the claim.

The defensible verdict is therefore: **retain the essay as high-value practitioner testimony and a source of task-health falsification probes; do not promote its seven properties into validated universal admission rules, treat Terminal-Bench experience as a representative study, or narrow `skill-bench` to deterministic outcome-only engineering tasks.**

## Why this matters for skill-bench

This review advances charter objectives A, B, D, and E through narrow expansion and immediate consolidation. It tests whether a concise practitioner account adds a missing authoring primitive or merely restates mechanisms already present in the charter, canonical taxonomy, task-health, projection, artifact-admissibility, metric, and validity contracts.

The general hypothesis is:

> Candidate quality is better assessed by whether the task survives distinct attempts to falsify solvability, fairness, observer adequacy, environmental validity, admissible-solution coverage, and construct-aligned difficulty than by one global quality checklist.

The concrete artifact is this source-located retain/repair/reject analysis. Useful completion means preserving nonduplicate probes, identifying where the advice overreaches, and declining to create a coding-specific schema or unevidenced gate.

## One-sentence contribution

The essay turns Terminal-Bench practitioner experience into a compact task-falsification workflow centered on same-information solvability, two-sided verifier validity, environment control, trajectory inspection, and construct-aligned difficulty, but does not empirically validate that workflow or its categorical outcome-only and authorship rules.

The essay asks what makes an agent benchmark task good, drawing examples and claimed lessons from conversations with Terminal-Bench contributors and the author's task-review experience (opening and Section 2, pp. 1–2). Its answer is seven nominal properties:

1. **verifiable** — a program should almost always reject errors and accept correct solutions, and remain operationally stable over repeated runs;
2. **well-specified** — the public description should determine the correct-outcome boundary closely enough that two experts would write extensionally equivalent verifiers;
3. **solvable** — a same-information, resource-valid witness or convincing argument exists;
4. **difficult for a good reason** — failure reflects the target capability rather than missing hints, clerical formatting, arbitrary thresholds, scale, or infrastructure friction;
5. **realistic and valuable** — a practitioner recognizes paid work in the task;
6. **outcome-verified** — grade the requested end state rather than one implementation path; and
7. **robust** — pin dependencies and remove time, hardware, and live-service variance not intended by the task (Section 1, pp. 1–2).

The paper then offers a lifecycle: start from remembered work; keep instructions brief and outcome-oriented; require an exploratory oracle; control the environment; attack the verifier; inspect batches of trajectories and compare failure with the stated crux; and combine domain expertise with benchmark-evaluation expertise in iterative human review (Sections 2–9, pp. 2–6).

## Methodology and evidentiary status

### What the paper actually does

This is a first-person synthesis of practitioner conversations and accumulated review experience. The opening names twelve contributors and “many other” Terminal-Bench participants, but gives no interview protocol, questions, dates, recording or coding method, participant roles, quotation ledger, dissent, saturation rule, consent statement, or mapping from a recommendation to a source. The voice shifts between “I,” “we,” and categorical imperatives, so reader cannot distinguish the author's opinion, Terminal-Bench policy, contributor consensus, or an observed frequency.

Examples are diagnostic vignettes, not retained cases. The paper discusses prompt token removal, complex JSON, hard-coded diagnostic oracles, synthetic ciphers, library-specific tests, agent failure convergence, review nonconvergence, and domain-review disputes (Sections 3–9, pp. 2–6), but releases no task IDs, versions, verifier diffs, trajectories, labels, denominators, or counterexamples. The claim that some tasks took more than forty hours or months of review is useful labor testimony, not a cost distribution (Section 10, p. 6).

### Citation audit

The citations provide context, but they do not validate the whole prescription:

| Citation | What it can support | What it cannot support here |
|---|---|---|
| Terminal Wrench, arXiv:2604.17596 [1] | A substantial released corpus of accepted exploit trajectories and concrete verifier/environment failure modes. The full source and release were previously audited in `papers/agent-benchmarks/2026-07-14-adversarial-verifier-hardening-validity.md`. | Universal hack prevalence, verifier completeness, or the seven-property authoring framework. The audited corpus is model/prompt/snapshot selected and contains contested legitimacy boundaries. |
| Jagged technological frontier [2] | Field-experiment evidence that AI effects vary across tasks within a bounded consulting-work setting, making one monotone human-to-model difficulty ordering implausible. | The essay's intrinsic-difficulty taxonomy, its claim that “hardest tasks” start hard, or a criterion for admitting terminal tasks. “Outside the jagged frontier” is an analogy, not an operational item label. |
| DeepMind specification-gaming post [3] | Primary production/research examples showing that optimized agents can exploit misspecified objectives. | Prevalence, error rates, or evidence that a particular candidate verifier is sound. It is an illustrative case collection. |
| Terminal-Bench, arXiv:2601.11868 [4] | Existence and broad design of a terminal-agent benchmark with realistic command-line tasks. | The essay's uncited “thousands of hours,” peer-review quality, contributor expertise distribution, TB3 workflow, or recommendation effectiveness. Those remain author testimony unless a task/review ledger is inspected. |
| METR reward-hacking post [5] | Primary operational examples that frontier agents sometimes exploit task/evaluator weaknesses. | A representative rate, causal account of all exploitability, or proof that outcome-only grading is sufficient. |

The strongest source-level corroboration is therefore asymmetric: reward-hacking and false-accept failures are empirically concrete, while brevity, human-only authorship, reviewer continuity, complete specification, and quality-over-quantity remain largely experience-based prescriptions.

## Unique insight

The essay's distinctive insight is not “realistic tasks are good.” It is the combination of **same-information solvability** and **observed crux alignment**:

```text
public task + permitted environment
→ exploratory witness using no privileged author knowledge
→ independently defensible acceptance boundary
→ diverse admissible solutions and invalid contrasts
→ repeated configured-agent trials
→ observed earliest failure causes
→ comparison with declared construct-relevant crux
→ task revision, claim contraction, or retirement
```

A canonical answer can pass while proving very little. If it jumps directly to an author-known value, it does not show that a solver can recover the answer from disclosed evidence. Conversely, low model success is not difficulty evidence until failures are shown to arise at the intended crux rather than from format, timeout, dependency, observer, or verifier defects (Sections 3, 5, and 8, pp. 2–5).

This is already compatible with `skill-bench`'s root/surface separation, projection conformance, execution validity, task health, artifact admissibility, and claim-centered validity. The nonduplicate emphasis is procedural: **run the same-information witness and preserve a predeclared-crux versus observed-root comparison as review evidence.** It should be an exercised audit, not another static schema.

## Retain, repair, or reject

| Recommendation | Decision | Source location | Reason and skill-bench transfer |
|---|---|---|---|
| Require reliable error detection and correct-solution acceptance | **Retain, repair** | §1 p. 1; §7 pp. 4–5 | Keep two-sided acceptance-boundary testing, invalid/insufficient-evidence outcomes, diverse valid alternatives, and versioned grader revisions. “All-but-guaranteed” needs measured populations and uncertainty, not intuition. |
| Use two independent experts' verifier agreement as specification heuristic | **Retain as probe** | §1 p. 1 | Strong disagreement is diagnostic. Agreement is not validity: shared assumptions, examples, or training can produce the same wrong boundary. Preserve independent definitions and disagreement, then test cross-acceptance. |
| Remove all ambiguity | **Repair** | §1 pp. 1–2; §3 p. 2 | Remove accidental ambiguity and hidden obligations. Preserve professionally legitimate uncertainty, contradiction, conditional applicability, and decision thresholds as the construct. |
| Require an exploratory, same-information oracle | **Retain** | §5 pp. 3–4; §6 p. 4 | Distinguish a canonical witness from proof of solvability/completeness. Log evidence access and prohibit privileged ground truth. Add alternative witnesses and resource-valid execution. |
| Start from real paid work and practitioner language | **Retain, repair** | §2 p. 2; §10 p. 6 | Use observed work, artifacts, incidents, and recipient consequences with provenance. A remembered task and professional-sounding language do not establish frequency, consequence, representativeness, or ecological validity. |
| Prefer brief goal statements | **Retain as heuristic, reject as KPI** | §1 p. 2; §4 p. 3 | Brevity can reduce accidental obligations and method prescription. It can also hide necessary authority, safety, evidence, handoff, or artifact conventions. Measure requirement coverage and comprehension, not token count. |
| Grade outcomes rather than implementations | **Retain as default anti-path-coupling rule** | §4 p. 3; §7 pp. 4–5 | Accept multiple legitimate methods. Separately grade consequential process, provenance, authorization, safety, evidence-use, communication, and audit obligations when publicly grounded. |
| Do not tell agents how tests work | **Repair** | §4 p. 3 | Keep exact private cases/weights/implementation hidden when needed, but disclose every obligation's public basis and admissible evidence. Hidden test mechanics must not become surprise requirements. |
| Pin environment and avoid live services | **Retain conditionally** | §1 p. 2; §6 p. 4 | Essential for static, reproducible constructs. For live-information or production-operation constructs, version and log service/index/time state, use health evidence and invalid-run policy, and bound replication instead of deleting realism. |
| Probe reward hacking and rerun the witness after a fix | **Retain** | §6 p. 4 | Matches adversarial verifier revision evidence. Add held-out adaptive attacks, valid-alternative suites, collateral checks, and old/new bridge matrices; one fixed exploit corpus is not correctness. |
| Infer fairness by temporarily naming the method | **Retain only as a localization probe** | §7 p. 4 | A guided pass can show that approach selection contributed to failure. It cannot show the original task was fair, the method is unique, or the verifier accepts other valid methods. Treat prompt change as an intervention. |
| Inspect batches of failures and test crux alignment | **Retain** | §8 p. 5 | Predeclare intended crux, preserve trajectory evidence, code earliest supported causes independently, and compare distributions. Five trials are diagnostic examples, not reliability estimates. |
| Keep authorship and review human | **Reject as categorical rule; retain authority separation** | §9 pp. 5–6 | Human authors can be wrong and model assistance can be useful. Require accountable human ownership, source provenance, transformation lineage, independent domain and evaluation review, and measured correction—not a human/AI purity label. |
| Use a domain-capable benchmark reviewer, ideally continuously | **Retain as hypothesis** | §9 p. 6 | Domain and evaluator expertise are distinct and both needed. Reviewer continuity may preserve context but can reduce independence and create shared blind spots. Cross with a fresh final reviewer and measure time, defects, disagreement, and correction. |
| Cite authoritative support for disputed “standard practice” | **Retain, repair** | §9 p. 6 | Preserve source authority, scope, freshness, local variation, and counterevidence. Published guidance does not automatically override current practitioner judgment or contextual exceptions. |
| Prefer fewer, better tasks | **Retain as governance stance, not evidence** | §10 p. 6 | Task count is not quality, but a tiny curated suite can have weak coverage and unstable ranking. Require assembly arguments, lineage clusters, precision, renewal burden, and sensitivity to alternate valid portfolios. |

## Where the advice conflicts with or sharpens the repository

### 1. Verifier equivalence versus plural evidence

The charter requires plural measurement across correctness, process, artifact quality, judgment, safety, efficiency, preference, readiness, and diagnosis. The essay's ideal programmatic separator is appropriate for narrow predicates, but many professional artifacts need multiple observers and bounded human judgment. `skill-bench` should seek criterion-specific reliability and admissibility, not force one total binary oracle.

### 2. Complete specification versus public basis/private consequence

The paper is right that undisclosed conventions create unfair failures. The repository's stronger rule is not exact disclosure of every private check; it is **public basis, private consequence**. The requirement, authority, and professional consequence must be disclosed, while exact perturbations, examples, weights, or exploit probes may remain held out. This reduces both hidden-obligation unfairness and evaluator-cue leakage.

### 3. Outcome latitude versus consequential process

The adversarial-verifier review already finds that canonical-path coupling creates false rejects, but WindowsWorld and HealthAdminBench show the opposite failure: final state alone can miss transient reversal, evidence acquisition, dependency, authorization, side effects, or professional handoff. The correct split is:

- reject implementation checks with no construct basis;
- retain consequential stages with explicit authority, alternative routes, temporal/durability semantics, and admissible evidence views; and
- report path, stage, outcome, collateral effect, and safety separately.

### 4. Task-level cleanliness versus suite-level validity

ECBD shows why individually good tasks do not establish a good benchmark. The essay largely stops at task curation. It does not define intended use, construct coverage, eligible population, assembly, dependence, weighting, missingness, uncertainty, decision loss, contamination operation, or claim transport. A suite of elegant, robust, authentic tasks can still be a biased convenience sample or support only a narrow configured-package claim.

## Limitations and threats to validity

1. One author's synthesis; contributor roles and attribution of specific claims are absent.
2. No systematic interview, observation, coding, Delphi, survey, or ethnographic method.
3. No candidate-task population, denominator, rejection count, defect rate, or sampling frame.
4. No before/after task artifacts or measured effect of applying the guidance.
5. No reviewer assignment, independence, agreement, adjudication, or error study.
6. No task-level time/cost ledger despite labor claims.
7. No test of whether two experts produce extensionally equivalent verifiers.
8. No empirical definition or coding reliability for “interesting,” “intrinsic,” “realistic,” “valuable,” or “professional recognizes it.”
9. Difficulty is discussed without a target population, configured-system class, item-response model, or temporal calibration rule.
10. Repeated verifier success is recommended without perturbation distribution, hardware matrix, confidence bound, or stopping rule.
11. “Batch of 5” trajectory inspection is a debugging heuristic, not repeated-reliability estimation.
12. The same community appears to generate tasks, norms, reviews, and lessons, creating shared-assumption and survivorship risks.
13. Successful/merged tasks are more visible than abandoned proposals; rejection reasons are not released.
14. Human-only authorship is asserted from stylistic experience, not compared against controlled human/model-assisted authoring.
15. Continuous shepherd review may improve context while reducing final-review independence.
16. Outcome-only language under-observes provenance, authorization, safety, communication, and audit constructs.
17. Complete unambiguity can exclude legitimate professional judgment and messy evidence central to `skill-bench`.
18. Avoiding all live services improves repeatability but can remove the time/index/service conditions of retrieval and operational work.
19. Concise instructions can hide domain conventions unless public basis and evidence access are validated.
20. A canonical oracle proves one accepted path, not all-path fairness, optimality, verifier completeness, or realistic resource use.
21. Temporarily naming a method changes the task treatment and cannot certify original fairness.
22. Cited reward-hacking examples support falsification need but not the full authoring framework.
23. Citation [4] does not by itself verify the essay's claimed labor, peer-review, contributor, or TB3 process facts.
24. No contamination protocol is proposed beyond general robustness; task exposure, search-time leakage, memorization, and evaluator-cue leakage remain distinct.
25. No suite assembly, score aggregation, uncertainty, ranking stability, maintenance, retirement, or downstream-use framework is supplied.
26. No paper-specific artifact release permits independent replay of examples or review conclusions.

## Reproducibility and operational realism

**Textual reproducibility: high.** The immutable PDF, full extraction, canonical HTML, and TeX source are retained and hash-verified. Section/page claims are straightforward to inspect.

**Method reproducibility: low.** There is no operational checklist with decision rules, source task set, author/reviewer ledger, trial corpus, or acceptance history. Another team can apply the prose, but cannot reproduce how the stated Terminal-Bench lessons were derived or estimate reviewer agreement.

**Operational realism: bounded but meaningful.** The advice reflects experience with executable command-line tasks where environments and deterministic verifiers can often be controlled. That substrate gives its exploit, dependency, oracle, and alternate-implementation advice practical force. It also explains the blind spots: many knowledge-work outputs have legitimate ambiguity, multiple evidence views, non-executable quality dimensions, organizational authority, recipients, and consequences that cannot be reduced to one stable binary endpoint.

## Transfer to skill-bench

## Action items

1. **Do not add a new schema or queue task.** Existing expertise-transfer, task-projection, benchmark-bundle, artifact-view admissibility, execution-validity, task-health, metric-monitoring, and validity-argument contracts can represent every defensible obligation.
2. **Exercise two probes in the next real pilot audit:**
   - run an exploratory same-information witness and prove that every used fact was publicly supplied or legitimately discoverable under the pinned environment; and
   - predeclare each task's intended crux, independently code earliest supported trial-failure causes, and compare the observed distribution with the declaration.
3. **Preserve disagreement rather than forcing checklist closure.** Have one domain-capable and one evaluation-capable reviewer independently define obligations, admissible alternatives, and acceptance predicates; retain disagreements and adjudication evidence.
4. **Use a two-sided verifier matrix.** Include canonical, independently derived, metamorphic, boundary, invalid, exploit, insufficient-evidence, and alternate-representation cases. Rerun it for every grader revision and preserve historical scores.
5. **Keep outcome and consequential process separate.** Remove checks for arbitrary implementation choices, but retain disclosed provenance, authorization, safety, handoff, evidence-use, and audit consequences with typed observers.
6. **Treat the essay as practitioner testimony in synthesis.** It sharpens review questions but does not validate a task-quality intervention. Any future adoption claim requires prospective use on candidate tasks with retained first-pass reviews, time, defects found, revisions, independent final audit, trial behavior, and claim contraction.

## Verdict

**High practical relevance, low empirical validation, no new contract required.** The paper is best used as an adversarial review lens: demand a same-information witness, attack both sides of the acceptance boundary, watch failures, and ask whether observed roots match the declared crux. Its universal-sounding rules need repair wherever professional work contains legitimate ambiguity, consequential process, plural evidence, live context, or human judgment. The repository should retain the falsification workflow and reject both coding-scope narrowing and outcome-only dogma.