# Paper Review: Evaluating Deep Research Agents on Expert Consulting Work

- **Paper:** https://arxiv.org/abs/2605.17554v3
- **Authors:** Tanmay Asthana, Aman Saksena, and Divyansh Sahu
- **Date read:** 2026-07-10
- **Venue / source:** arXiv preprint
- **Tags:** deep-research-agents, knowledge-work, consulting, cognitive-traps, source-discipline, artifact-evaluation, expert-rubrics, deterministic-verifiers
- **Version read:** immutable v3, 25 June 2026
- **Local PDF:** `data/papers/pdfs/2605.17554v3-evaluating-deep-research-agents-on-expert-consulting-work.pdf` (25 pages; SHA-256 `fefd08603a59a60777475ab18dc9bdbe7dccf54e3b7d7e8cfc6acbf10d91bea3`)
- **Local text:** `data/papers/text/2605.17554v3-evaluating-deep-research-agents-on-expert-consulting-work.txt` (SHA-256 `872990cb4d79f25d7de049a4400bfd3ee14b75f13da92feb58cc3ae8f6222a0c`)
- **Linked release inspected:** `data/sources/releases/2605.17554v3-consulting-benchmark/dra-response-gen-4288.zip` (SHA-256 `3bd2cc70492e376ab0881769b805922ce51ee6c8effd9a97a3f36cf8db7115fb`); manifest: `data/sources/releases/2605.17554v3-consulting-benchmark/provenance.json`

## One-sentence contribution

The paper turns management-consulting tasks into deliberately adversarial source packages by pairing a plausible novice shortcut with an expert derivation, then evaluates 210 agent responses with task-specific binary checks and a five-dimension expert rubric—showing that polished research artifacts can fail through source-authority violations, unreconciled contradictions, cascading calculations, or malformed deliverables even when a broad quality score looks respectable.

## Why this matters for skill-bench

This advances charter objectives A and B: it is primary-source evidence about realistic knowledge-work evaluation and a concrete, if only partially released, method for translating expertise into hidden requirements, trusted-source rules, contradictions, thresholds, artifact conventions, failure signatures, and checks. It is expansion work with a direct consolidation target: the existing expertise-transfer contract already represents these primitives, while the first pilot already plants evidence and causal-overclaim traps. The uncertainty clarified is not whether traps are useful, but **what makes a trap professionally legitimate and diagnostically interpretable**.

The most transferable artifact is the paper’s authoring triple (Appendix L, pp. 15–20):

`Lazy AI Test → Expert Test → Solution Logic`.

This is stronger than adding arbitrary difficulty. The lazy path names a plausible failure; the expert path identifies the cue or operation that distinguishes expertise; and the solution logic provides an auditable derivation. Combined with an authorized-source designation, artifact specification, and trap-specific verifier, it can become an executable critical-incident record. Useful completion for `skill-bench` is therefore not “add consulting prompts,” which would narrow the project. It is to test whether this authoring triple produces reusable, fair traps across domains and whether planted failures yield the predicted diagnostic signals.

The paper must not be treated as a validated or reproducible benchmark release yet. Its linked code snapshot contains a response-generation harness, not the claimed benchmark instrument: no 70-prompt corpus, input documents, grading workbook, verifier specifications, rubric scorer, or result set is present. The manuscript itself says the dataset “will be released” on publication (Section 1; Appendix O), despite the abstract saying the corpus is publicly released. Consequently, the paper supports a design pattern and reports experimental results, but outside readers cannot audit task quality, recompute scores, inspect response-level missingness, or reproduce the central claims from the acquired release.

## Research question

The paper asks whether frontier deep-research agents can produce decision-grade, multi-document management-consulting deliverables when tasks require source discipline, signal extraction, structural obedience, latent decomposition, and precision under consequential error. It also asks whether a dual instrument—task-specific binary checks plus a shared ordinal quality rubric—can distinguish agent-specific failure profiles that a single pass rate would hide.

The evidence supports a narrower conclusion: the instrument produces substantially different continuous score profiles for the three configured systems, and the worked tasks instantiate credible professional failure surfaces. It does not yet establish construct validity, cross-domain generality, reliability of SME scoring, or reproducibility of the benchmark itself.

## Methodology

### Task construction and capability classes

The corpus has 70 management-consulting prompts: 13 constrained-research prompts (CRP), 18 relevance-compression prompts (RCP), 18 structural-compliance prompts (SCP), 13 latent-decomposition prompts (LDP), and 8 failure-sensitive prompts (FSP). Each prompt includes 2–4 mixed-format proprietary files from 2 KB to 430 KB; some require generated DOCX, XLSX, or PPTX artifacts. Tasks are annotated as closed, hybrid, or open corpus, although the authors acknowledge that black-box agents prevent hard enforcement (Sections 3.1–3.2, pp. 3–5).

The five classes target operations rather than topics:

- **CRP:** obey an authorized-source boundary despite easier external alternatives;
- **RCP:** filter a noisy corpus, reconcile qualifiers, and distinguish drivers from outcomes;
- **SCP:** preserve an exact output schema while doing substantive analysis;
- **LDP:** infer latent variables and intermediate calculations before solving;
- **FSP:** avoid a single precision error that cascades into a wrong decision.

The worked examples make the traps concrete. An RCP task requires replacing a headline handle-time benchmark with a footnote-qualified value and not treating an outcome metric as a root cause (Appendix L.2, pp. 16–17). An SCP task hides a non-operational allocation in a PDF appendix and independently checks strict JSON structure (Appendix L.3, pp. 17–18). An LDP task requires deriving coefficients and constraints from three spreadsheets before solving an integer program (Appendix L.4, pp. 18–19). An FSP task requires rejecting a stale `$400` placeholder, fetching a live marine-fuel index, and recognizing a decision flip near `$612/ton` (Appendix L.5, pp. 19–20).

A Principal Expert with more than 15 years of consulting experience reportedly vetted prompt realism, traps, authorized sources, and verifier specifications. However, the paper does not report the SME task-authoring instructions, number or backgrounds of original task writers, rejection/revision rates, how prompts were sampled, or whether experts solved tasks independently before deployment. “SME-authored” is therefore a provenance category, not yet a reproducible elicitation method.

### Scoring instrument and annotation

Each response receives a mean 14.9 binary task-specific checks and five 0–3 ordinal scores:

1. Data Integrity (DI),
2. Analytical Rigor (AR),
3. Relevance & Focus (RF),
4. Execution Precision (EP), and
5. Format & Deliverability (FD).

The relaxed Verifier-Rubric Score equally weights verifier pass rate and scaled rubric mean. The strict VRS sets the whole aggregate to zero if any criterion is zero. `ACCEPT` is a separate gate requiring every criterion above zero, mean rubric score at least 2.5, and verifier pass rate at least 80% (Section 3.3, pp. 4–5).

The phrase “deterministic verifiers” needs qualification. The paper describes binary, task-specific pass conditions, but each verifier is scored by a primary SME and checked by a second SME; the QC protocol asks reviewers to compare a 0/1 judgment against response, file, and citation evidence and manually re-derive selected checks (Appendix N, pp. 21–22). No executable verifier implementation is in the released snapshot. These are best characterized as **deterministically specified binary criteria with human application**, unless executable implementations become available.

One former MBB/Big Four/Tier-2 consultant grades each prompt-agent response. A non-overlapping second SME performs asymmetric QC: confirm, edit with rationale, or reject/return. Final-answer and trap checks are always re-derived; selected numerical, citation-dependent, and output-file checks receive deeper review. Citation QC tests existence, claim support, and authorized-source membership (Appendix N). This is a thoughtful defensibility workflow, but not independent double annotation: the study reports neither inter-rater reliability nor edit/reject rates.

### Agent systems and evidence

The systems are Claude Opus 4.6, o3-deep-research, and Gemini 3.1 Pro deep-research, dispatched through different API adapters. Across 210 attempts, headline results are:

| Metric | o3 | Claude | Gemini |
|---|---:|---:|---:|
| Mean rubric score (0–3) | 1.89 | 1.55 | 1.68 |
| Mean verifier pass rate | 60.2% | 48.6% | 58.2% |
| Mean strict VRS | 61.4 | 38.5 | 52.6 |
| ACCEPT | 15.7% | 12.9% | 12.9% |
| Responses with at least one rubric zero | 10.0% | 41.4% | 30.0% |

The o3–Claude paired VRS difference survives Bonferroni correction (`Δ=22.9`, adjusted `p=.001`); all binary ACCEPT comparisons are non-significant (Section 4, pp. 5–8). Forty-five of 70 prompts reject all three systems, while no prompt accepts all three. Class-specific strict VRS yields different winners: o3 on CRP/FSP/RCP, Claude on LDP, and Gemini on SCP.

Failure tags are generated post hoc by Claude Opus 4.5 from 1,050 SME criterion justifications and weakly cross-checked by regex (mean Jaccard 0.339). Reported signatures—Claude fabrication/file-access failures, o3 cascading calculations/citation hallucination, Gemini technical collapse—are hypotheses supported by counts and examples, not validated root-cause labels. In particular, correlation between a tag and an agent does not localize the earliest causal failure in the trace.

## Unique insight

The paper’s deepest insight is that a good professional trap is a **decision-boundary perturbation with an expert-visible cue**. A stale value, contradictory footnote, wrong aggregation, or latent coefficient matters because resolving it changes a downstream decision or artifact state. This provides a sharper rule than “make source packs messy”: every trap should state the naive operation, expert cue, correction, decision threshold, and counterfactual consequence. Without that chain, a trap may add noise but not measure expertise.

A second insight is that source authority is a typed constraint, not a generic citation count. The CRP examples show three different checks: whether a source exists, whether it supports the claim, and whether it is authorized for this task. Claude’s cited pages could be real yet topically irrelevant; a syntactic URL checker would pass them. `skill-bench` should therefore preserve `existence`, `entailment`, `authority`, `scope`, and `freshness` as separate evidence predicates.

A third insight is the divergence between **continuous diagnosis and readiness gating**. o3’s strict VRS differentiates it from Claude, while all three remain statistically tied at roughly 13–16% ACCEPT. The paper is right that one view cannot substitute for the other. But its strict VRS is not a neutral diagnostic: zeroing the entire score for one rubric failure increases Claude’s penalty by 11.65 points, and Appendix H reports that the zero guard changes no ACCEPT outcomes because every zero-score response already fails another threshold. `skill-bench` should keep component scores and release gates separate rather than bake a catastrophic gate into a continuous capability summary.

## Transferable design patterns

### 1. Extend each trap into a critical-incident record

The existing `expertise-transfer.schema.json` already stores trap mechanism, source IDs, failure signature, fairness basis, and primitive links. The evidence here suggests authoring guidance—not necessarily a new schema—to require or derive:

- `naive_path`: plausible shortcut or surface heuristic;
- `expert_cue`: contradiction, footnote, authority rule, missing variable, or threshold;
- `expert_operation`: reconcile, normalize, weight, decompose, verify, or refuse;
- `solution_derivation`: auditable steps and acceptable alternatives;
- `decision_boundary`: value or state at which the recommendation changes;
- `counterfactual_consequence`: what the naive path gets wrong;
- `trap_check_id`: focused check independent of overall quality;
- `fairness_basis`: disclosed professional requirement whose consequence is held out.

This operationalizes the paper’s Lazy AI Test / Expert Test / Solution Logic without copying its consulting scope.

### 2. Type evidence-authority checks

For any material claim, record separate check results for source resolution, claim support, authority-list membership, temporal validity, and corpus-boundary compliance. For open/live tasks, pin retrieval time, exact page snapshot/hash, acceptable source hierarchy, quote/span, and a threshold region. The FSP fuel-price example is otherwise non-stationary: its golden decision can change with the market, and “Ship&Bunker or similar” leaves authority underspecified.

### 3. Separate trap detection from downstream recovery

A system can notice a contradiction but apply the wrong correction, or miss the cue yet accidentally land in the acceptable numeric range. Grade at least: cue encountered, contradiction represented, authority selected, operation applied, intermediate result, threshold comparison, final decision, and artifact compliance. This turns one pass/fail trap into a causal failure chain compatible with the benchmark bundle’s trace links.

### 4. Keep readiness, diagnosis, and artifact usability plural

Report binary check vectors, ordinal expert dimensions, hard release gates, artifact validity, and human readiness separately. If an aggregate is retained, version its policy and show sensitivity. Do not let a polished format compensate for fabricated data, but also do not erase all partial diagnostic information when a gate fails.

### 5. Treat code/harness fidelity as an environment validity issue

The linked README documents asymmetric observability and access enforcement: only Claude offers hard tool-level IAT-1 enforcement; OpenAI and Gemini closed-corpus results are advisory, and the harness defaults `enforce_iat=False`. Generated files also run in different execution environments. Trials therefore need typed corpus-policy enforcement, model/harness/tool hashes, adapter observability, file-processing transformations, and environment-failure labels. “Identical task package” does not imply an identical information or execution environment.

## Limitations and validity threats

1. **The benchmark artifacts are unavailable.** The release snapshot has 42 response-generation files but no corpus, source packs, grader workbook, verifier specs/implementations, rubric scorer, responses, or results. The abstract’s “publicly released” claim conflicts with the body’s future-release statement. Central evidence cannot be independently audited.
2. **No inter-rater reliability estimate.** One SME grades each response; the second checks defensibility rather than independently rating it. QC can catch errors but cannot estimate scorer exchangeability or organizational disagreement.
3. **Task-authoring validity is underdescribed.** One Principal Expert vets tasks, but there is no reported elicitation protocol, expert-solve baseline, ambiguity adjudication, acceptance rate, item-analysis process, or evidence that each prompt class isolates its named capability.
4. **“Deterministic” is not demonstrated operationally.** Human-scored binary conditions may be precise, but executable behavior, tolerances, extraction logic, and edge cases are unavailable. Mean verifier pass rate can therefore include annotation judgment.
5. **Construct dimensions overlap.** Mean off-diagonal rubric correlation is about 0.60 and DI–EP reaches 0.74. The authors acknowledge two or three latent factors, so five labels should not be interpreted as five independent capabilities.
6. **The failure taxonomy is weakly validated.** A model tags expert comments and regex overlap is only 0.339. No human precision/recall or trace-level causal validation supports labels such as “system collapse” or “systematic pretraining gap.”
7. **Configured systems differ materially.** APIs, internal browsing, file conversion, execution sandboxes, observability, timeouts, and tool enforcement vary. This is production-realistic but prevents attribution to model architecture. The paper’s claim that file failures reflect model code rather than infrastructure is too strong.
8. **Closed-corpus compliance is not controlled.** The paper admits it is measured rather than guaranteed. The linked harness says only Claude has hard IAT-1 enforcement and that enforcement is off by default. Apparent source-discipline differences may partly be environment differences.
9. **Live-data traps impair stability.** A market price can cross the decision threshold, source pages can change, and task dates can become stale. Without snapshots and equivalent-form refresh rules, the correct answer and difficulty drift.
10. **Threshold validity is asserted, not calibrated.** The 2.5 rubric mean and 80% verifier floor lack evidence from human work products, downstream decision loss, or expert readiness judgments. The zero guard is dormant in this sample.
11. **Cross-benchmark comparison is weak.** Binary-check pass rates are compared despite different domains, check counts, check authoring, and human versus LLM grading. The statement that all-check pass probability drops “exponentially” with check count assumes a dependence structure the paper does not test.
12. **Internal numerical inconsistencies reduce auditability.** Appendix H.1.4 reports ACCEPT rates of 9.5%, 9.5%, and 21.4%, contradicting the headline 15.7%, 12.9%, and 12.9%. Nearby prose gives EP pass rates that disagree with Table 14; multiple sections/captions reverse the reported VRS ordering as `Claude > Gemini > o3`; and the narrative math-error count conflicts with Table 9. These are not cosmetic in a paper whose contribution is measurement precision.
13. **Safety and authorization realism are limited.** Tasks simulate consequential recommendations but do not test approval boundaries, privacy, confidential-source handling, or irreversible actions.
14. **External validity is single-domain.** Seventy consulting prompts may expose reusable knowledge-work primitives, but no evidence shows the five prompt classes are exhaustive or stable across law, medicine, engineering, or operations.

## Reproducibility and operational realism

Operational realism is substantial at the task level: mixed proprietary files, generated artifacts, noisy and contradictory evidence, source restrictions, live data, exact structures, business thresholds, and costly errors. The QC protocol is also unusually explicit about final-answer re-derivation, trap checks, citation entailment, and artifact inspection.

Reproducibility is currently poor. The immutable PDF and local extraction are preserved, and the released harness reveals adapter behavior, but the benchmark itself is absent. Exact models are proprietary and time-varying; access policies are not equivalent; no component hashes or full result matrix are supplied; and manuscript inconsistencies prevent clean reconstruction from tables alone. A credible reproduction requires the 70 immutable task packages, source licenses or redistributable substitutes, task/verifier revisions, scorer and tolerance code, all 210 outputs and artifacts, SME/QC edit logs, adapter commits/configuration, web snapshots, exclusion logs, and a script that recreates every table.

## Concrete changes for skill-bench

1. **Use the authoring triple in pilot calibration.** For each existing planted failure in `pilots/lh-skill-adoption/`, document the naive path, expert cue, correct operation, auditable derivation, and downstream decision consequence. Keep these as internal calibration fields where disclosure would leak the check.
2. **Strengthen the evidence-link grader implementation already queued.** Make source existence, locator validity, claim entailment, authority, scope, and freshness separate outputs. This directly extends `build-lh-pilot-grader-ablation`; no duplicate queue task is needed.
3. **Add threshold-crossing fixtures.** Beyond agreement and tiny-ablation overclaims, include one source contradiction where using the superficially plausible row flips the recommendation. Require both contradiction handling and correct downstream recomputation.
4. **Require trap fairness review.** A private trap must be a consequence of a public requirement, have a plausible expert/novice contrast, admit alternative valid procedures, and produce a specific failure signature. Reject “gotcha” formatting or undisclosed obligations.
5. **Do not collapse the pilot into consulting.** Reuse the critical-incident machinery in later pilots with different knowledge structures—e.g., safety constraints, scientific evidence, or operational state—to test whether the trap record generalizes.
6. **Treat unreleased evidence conservatively.** Cite this paper for the proposed method and reported results, but do not use its counts as calibration ground truth until the corpus, response matrix, and grading artifacts can be audited.

## Action items for repository

- [x] Read and preserve the immutable v3 PDF and full local extraction.
- [x] Inspect the complete linked release snapshot and record the missing benchmark/grading artifacts.
- [x] Map the Lazy AI Test / Expert Test / Solution Logic pattern to the existing trap and provenance contracts.
- [x] Identify the existing `build-lh-pilot-grader-ablation` task as the non-duplicate implementation path for typed evidence checks and planted failures.
- [ ] During that build, instantiate one threshold-crossing contradiction fixture and retain component-level results rather than a single aggregate.
- [ ] Reassess reproducibility if the promised corpus, grading workbook, verifiers, and result set are later released.
