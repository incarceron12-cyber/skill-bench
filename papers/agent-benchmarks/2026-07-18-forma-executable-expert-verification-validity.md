# FORMA: executable evidence trails are promising, but selective agreement with the same catalogue is not independent scientific verification

## Bottom line

FORMA makes a valuable design move: it turns an expert-style review sequence into an inspectable computational product rather than asking a model for a label and a post-hoc explanation. Numerical spectra become detected features and continuum structure; 10–20 Redrock redshift candidates are tested in parallel; contested features are audited; competing hypotheses are compared; a second auditor re-reads selected evidence and domain rules without seeing the synthesis reasoning chain; and a report preserves accepted evidence, rejected alternatives, concerns, uncertainty, and a defer/review disposition. The paper-time repository exposes the implementation, prompts, knowledge base, deterministic tools, two FITS examples, and two counterfactual trace packages. This **evidence → alternatives → audit → disposition** structure is directly relevant to realistic knowledge-work evaluation.

The empirical claim is much narrower than “executable scientific verification.” From a purposively sampled 1,149-spectrum subset of the DESI EDR visual-inspection (VI) catalogue, the authors retain only 331 medium-or-higher-credibility definite predictions (28.8% coverage), exclude unknown/deferred outputs, and report 316/331 binary QSO-versus-galaxy agreements (95.5%) with DESI labels. The medium threshold is chosen on the same evaluation set after observing the coverage–agreement trade-off; no development/evaluation chronology, held-out threshold set, uncertainty interval, selective-risk analysis, Redrock-only comparator, repeated full-pipeline reliability, or independent scientific follow-up is reported. Because both DESI inspectors and FORMA receive Redrock candidate solutions, agreement can reflect a shared proposal channel. The paper itself argues that Redrock can anchor multiple human inspectors to the same low-SNR coincidence. That critique also weakens DESI agreement as independent validation of FORMA.

The credibility label is not an independently specified score. A DeepSeek-V4-Pro Result Auditor assigns `HIGH/MEDIUM/LOW` from a mutable knowledge base and a long prompt; the paper explicitly says there is no detailed hand-crafted scoring specification. The auditor is hidden from the synthesis chain of thought, but it shares the base model, evidence pipeline, adopted catalogue, tools, knowledge, and task-specific rules. This is useful **procedural separation**, not statistical, implementation, model, or evidence independence.

The official paper-time snapshot supports implementation inspection and narrow example replay, but not reconstruction of the headline catalogue results. It contains no 1,149-case manifest, 331-case cohort, per-case result ledger, aggregate score table, confusion-matrix builder, sample-selection code, threshold analysis, or table-building pipeline. The two released counterfactual summaries reproduce only the paper’s **modified-knowledge-base** columns (86/100 and 99/100 `NEEDS_REVISION`), while the original-KB columns (97/100 and 100/100) have no released summaries. Their runners import a nonexistent `AstroAgent` package even though the snapshot contains `FORMA`, so they fail at the import boundary without undocumented source rewriting. The examples still establish retained outputs and reported run counts; they do not make Table B1 or Figure 2 reproducible.

The strongest warranted conclusion is therefore: **one configured FORMA implementation produces rich, challengeable spectroscopy reports; its auditor often rejects two hand-forged defects in one QSO example; and its selectively retained decisions agree frequently with DESI binary labels on one sampled catalogue.** The evidence does not establish source-faithful transfer of a validated expert procedure, independent scientific correctness, calibrated autonomous acceptance, improvement over Redrock, cross-catalogue transfer, production reliability, cost-effectiveness, or readiness to admit conclusions into scientific use.

## Source and reading record

### Complete immutable primary source read

- Haosong Wang et al., *Executable verification through formalized expert reasoning in astronomical spectroscopy*.
- Immutable record: <https://arxiv.org/abs/2607.06128v1>; PDF: <https://arxiv.org/pdf/2607.06128v1>.
- Local PDF: `data/papers/pdfs/2607.06128v1-forma.pdf` (26 pages; 1,839,340 bytes; SHA-256 `9f609c3a3b72fe07e0fbfbff2613417e532369b7ea4ea7837db7b2d57bc4c3f0`).
- Local full text: `data/papers/text/2607.06128v1-forma.txt` (142,299 bytes; SHA-256 `1265f366c41fa09e5288e9663b99ba5aba89e8126d4521a4d93c9d32ae5ca282`).
- Local arXiv source: `data/papers/source/2607.06128v1-source.tar.gz` (1,575,456 bytes; SHA-256 `bedb8ab38b1efbaa41e0faccc99f01c76768b3035362d516fc3987a70dcbce61`).
- Read through the complete abstract, Sections 1–4, Method, Appendices A–B, figures, table, code statement, and references. The immutable v1 record was submitted 7 July 2026 and the acquired metadata contains no withdrawal notice.

### Official paper-time release audited

- Paper code statement: extracted text lines 281–282; official repository: <https://github.com/SpecSurvey-In-AI-era/FORMA>.
- Pinned paper-time commit: [`f88f14ca682179ae3213aaf2888a554fab1e6627`](https://github.com/SpecSurvey-In-AI-era/FORMA/commit/f88f14ca682179ae3213aaf2888a554fab1e6627), committed 6 July 2026 at 15:31:58 UTC, before v1 submission.
- Local snapshot: `data/sources/releases/2607.06128v1-forma/FORMA-f88f14ca6821.tar.gz` (2,373,384 bytes; SHA-256 `0ee3d9b3f6afe473798d5dfbd4ce826b71e5161c9d24deea8f839359b61dff5c`).
- Extracted repository and provenance: `data/sources/releases/2607.06128v1-forma/repository/` and `data/sources/releases/2607.06128v1-forma/provenance.json`.
- Snapshot inventory: 189 tree entries, 140 blobs, no GitHub release, and no top-level license. `pyproject.toml` says MIT, `package.json` says ISC, and the README says only research/educational use; redistribution terms are ambiguous.

### Verification performed for this review

- Reconstructed the full sample and reported decision denominators from the paper.
- Inspected the implementation tree, runtime configuration, all principal Skills/prompts, knowledge-base rules, batch entry point, output contract, both counterfactual packages, batch runners, and retained summaries.
- Verified that the two released 100-run summaries sum correctly by verdict and confidence.
- Calculated reported agreement rates and Wilson 95% descriptive intervals from disclosed counts.
- Audited the complete 140-blob paper-time tree for evaluation/catalogue/score/table/test artifacts.
- Tested import identity with the pinned source on `PYTHONPATH`: `FORMA` imports, while the released counterfactual runners’ `AstroAgent` import raises `ModuleNotFoundError`.

No paid model call was made. The catalogue results cannot be rerun because the release omits the evaluation cohort/results and requires a commercial endpoint, Redrock/template assets, DESI data, and undocumented paper-time run manifests.

## One-sentence contribution

FORMA operationalizes scientific review as a retained chain of deterministic evidence extraction, constrained alternatives, feature and result audits, and explicit deferral, while exposing why an LLM-assigned credibility gate and selective agreement with a shared catalogue/proposal channel cannot by themselves establish independent verification.

## Why this matters for skill-bench

This review advances charter objectives A and B through bounded expansion and validation at the expertise-to-executable-evaluation boundary. Astronomy is a demanding mechanism case, not a scope commitment. The concrete evidence is a full immutable-paper audit, a pinned implementation/prompt/knowledge-base audit, denominator reconstruction, counterfactual-release audit, import check, and claim-boundary analysis.

The uncertainty clarified is whether an executable expert-reasoning trace validates the conclusion it accompanies. FORMA shows that trace structure can be substantially better than opaque answer grading while validity remains unresolved at four separate boundaries: whether the procedure is source-faithful, whether the configured workflow conforms to it, whether the conclusion is independently correct, and whether a thresholded decision is safe for downstream use.

Useful completion is a reusable non-inheriting ladder:

`procedure provenance → protocol conformance → selective reference agreement → independent correctness → downstream scientific utility → production readiness`

No rung licenses the next. The repository already has claim-validity, observer/evidence-view, metric, task-health, artifact, trace, expert-authority, and executable-consequence machinery capable of representing this distinction, so this review does not add a duplicate schema task.

## Research question and claim boundary

The paper asks whether expert scientific verification can be rendered executable rather than left as an exclusively human bottleneck. In spectroscopy, the system should not merely predict type/redshift; it should extract observations, propose physically allowed hypotheses, challenge alternatives, enforce numerical and astrophysical constraints, preserve the evidential path, and accept, reject, or defer a proposed interpretation.

The paper claims:

1. a general five-requirement executable-verification protocol;
2. a six-step, four-module spectroscopy implementation;
3. a credibility rating distinct from model self-confidence;
4. a 1,149-spectrum DESI VI evaluation without an added SNR cut;
5. a coverage–agreement trade-off, including 331 medium-or-higher definite predictions at 95.5% binary agreement;
6. more concentrated redshift residuals at higher credibility;
7. evidence that low credibility is not merely low SNR;
8. two counterfactual evidence-ablation tests, each repeated 100 times under two knowledge-base conditions; and
9. a representative low-luminosity AGN case aligned with an expert-supported interpretation.

The paper and release support existence of the workflow, disclosed sample construction, reported aggregate counts, retained example outputs, and two released modified-KB batch summaries. They do not support a general claim that the workflow independently verifies scientific truth before use. “Expert-adjudicated” is a reference-label provenance description, not evidence that every selected label is independently correct—especially where the paper argues that multiple inspectors may share Redrock anchoring.

## Methodology and system

### Expertise elicitation and transformation

The Method says the architecture derives from structured interviews with DESI collaboration members and visual-inspection protocol documents (text lines 890–911). It identifies three expert stages:

1. **Visual Perception:** inspect morphology/features and form candidate interpretations;
2. **Hypothesis Inference:** predict companion-line positions, compute line-wise redshifts, and compare consistency; and
3. **Result Validation:** repeatedly challenge detections, noise distinctions, and physical plausibility while using Redrock overlays as guides.

This is plausible cognitive decomposition. It is not an auditable expertise-transfer study. The paper does not identify the interview count, participants, qualifications, role in DESI inspection, recruitment, consent, protocol, questions, recordings, coding method, disagreements, saturation, rejected procedures, source-document versions, or expert approval of the transformed modules/prompts/knowledge base. Author affiliations and manuscript editing do not establish that a specific expert endorsed every encoded fatal rule, threshold, or tool behavior.

The transformation also changes the procedure. Humans visually inspect a graphical spectrum with templates; FORMA runs CWT and continuum fitting on numerical arrays, presents selected evidence to LLM agents, gives them a curated textual knowledge base, and enforces prompt-defined rules. That may be an effective engineering realization, but representation, preselection, tool thresholds, and textualization are treatments. “Mirrors expert reasoning” should mean structural inspiration unless clause-level source and expert validation are retained.

### Six-step workflow

**Step 1 — Visual Interpreter.** FITS B/R/Z arrays are loaded; masked and overlap pixels are excluded; per-pixel uncertainty is retained; multi-scale CWT detects peaks/troughs; features receive centres, amplitudes, widths, and quality flags; a Chebyshev continuum is fitted; and Redrock supplies top candidate redshifts. The paper says only redshift, not Redrock class, is forwarded (lines 934–960).

**Step 2 — Single-Hypothesis Evaluation.** Roughly 10–20 candidates are assigned to parallel LLM agents. Each receives a `z ± 0.1` window, spectrum summary, predicted rest lines, nearby CWT features, a procedural Skill, Gaussian/double-Gaussian fallback tools, and deterministic redshift conversion. It marks lines `LIKELY/MARGINAL/NOT_FOUND/MASKED`, chooses a systemic anchor, classifies the source, and emits a catalogue/report (lines 971–988).

**Step 3 — Feature Auditor.** One LLM examines cross-hypothesis feature conflicts, orphan/inconsistent doublets, composite profiles, and suspicious raw regions, then returns `KEEP/REMOVE/FLAG` and cleaned catalogues (lines 990–1001).

**Step 4 — Hypothesis Synthesis.** Another LLM compares cleaned alternatives, reads selected spectrum regions and knowledge, checks morphology, chooses a best/runner-up hypothesis, or returns `Cannot confirm` (lines 1007–1016). The released Skill explicitly warns that predicted-position matching creates confirmation loops and that spacing selected by the pipeline is not independent evidence. This is an unusually candid and useful anti-circularity instruction.

**Step 5 — Result Auditor.** A second adversarial LLM sees the synthesis verdict and adopted catalogue but not its reasoning chain. It can query raw regions and the same knowledge base, checks physical/classification consistency and unexplained verified features, and outputs `CONFIRM/NEEDS_REVISION/UNCERTAIN` plus `HIGH/MEDIUM/LOW` (lines 1018–1029).

**Step 6 — Report Writer.** A final module consolidates metadata, all hypotheses, cleaned evidence, synthesis/audit disagreement, potential issues, feature score, credibility, redshift uncertainty, manual-review recommendation, and a plain-language conclusion (lines 1031–1048).

The workflow preserves useful observer boundaries, but “independent auditor” needs qualification. The Result Auditor is independent only of the synthesis reasoning chain. It is not independently authored, modeled, trained, sampled, evidenced, or tooled. It shares DeepSeek-V4-Pro, the upstream catalogue, deterministic preprocessing, knowledge base, prompts from the same team, and raw input. Common-mode errors can survive every stage.

### Feature score versus credibility

The feature score imitates the DESI VI 0–4 convention: 4 means at least two secure features; 3 means one secure feature plus continuum support or many weak features; 2 is a single strong but unidentified emission feature; 1 is unidentified features; 0 is no signal (lines 1050–1057). Appendix A demonstrates that this count does not stratify agreement: Figure A3 reports approximately flat 89.9–90.8% accuracy as the threshold rises, and VI quality remains similarly distributed across feature-score bins.

The paper appropriately rejects feature count as sufficient. But the replacement “credibility score” is not a score in the usual reproducible sense. It is an ordinal LLM judgment assigned without a detailed hand-crafted scoring specification (lines 1067–1078). The knowledge base and prompt contain explicit class rules, fatal problems, line-width thresholds, edge/OH warnings, completeness rules, and confidence definitions. The resulting label is a configured judge decision—not a model-independent measurement of evidential sufficiency.

Calling it “well-calibrated” is unsupported. Calibration requires a declared target probability/decision, reliability estimates, and held-out comparison. The paper presents monotonic selective agreement on the same dataset used to choose the threshold. It does not report calibration curves, expected calibration error, Brier/log loss, confidence-conditioned empirical probabilities with intervals, repeated-rating stability, or prospective threshold performance.

## Dataset and reference authority

### Sampling frame

The five DESI EDR VI files contain approximately 22,000 spectra: 2,718 BGS, 3,561 LRG, 10,315 ELG, 3,779 QSO, and 1,717 missed-QSO records (lines 1105–1112). The evaluation construction is:

1. collect `VI_SPECTYPE=QSO` across all five catalogues;
2. collect `VI_SPECTYPE=GALAXY` from each ELG/LRG/BGS pipeline-named catalogue;
3. retrieve spectra by `TARGETID`, `TILEID`, RA, and DEC;
4. sum per-arm median coadd SNR;
5. rank within class, stratify high/medium/low at 4:4:2; and
6. randomly sample 300 per class, except uniqueness of `TARGETID–TILEID` leaves 249 BGS.

The final set is 300 QSO + 300 ELG + 300 LRG + 249 BGS = 1,149 (lines 1113–1126). This gives balanced designed class coverage, not prevalence-weighted survey performance. Stars are omitted even though `VI_SPECTYPE` can be star. Binary QSO/galaxy agreement collapses distinct LRG/ELG/BGS decisions and does not test star rejection.

The paper does not release the sampled IDs, random seed, duplicate-removal order, candidate population counts after selection, missing/retrieval failures, or exact catalogue file hashes. Therefore sample reconstruction and clustered leakage checks are blocked. `TARGETID–TILEID` uniqueness does not establish unique astrophysical source, plate/field independence, or absence of related observations.

### DESI labels and shared proposal channel

DESI VI is stronger than a single unreviewed label. Appendix A reports multiple independent inspectors, automatic merging only when redshifts differ by less than 0.0033, quality differs by at most one, and spectral type agrees; inspectors can flag bad redshift, class, or spectrum (lines 1180–1190).

However, the FORMA paper does not report, for its 1,149 selected records:

- number and identities/qualifications of inspectors;
- individual labels, disagreement, merge versus adjudication route, or unresolved status;
- whether every `VI_SPECTYPE` used was consensus-qualified;
- missing labels/flags and inclusion policy;
- `VI_QUALITY` distribution by retained credibility/class;
- scientific follow-up or independently confirmed labels; or
- whether the evaluators selecting/analysing cases were blinded to FORMA outputs.

The paper itself argues that Redrock overlays can anchor all inspectors at low SNR, yielding consensus around noise (lines 1191–1225). FORMA also begins from Redrock candidate redshifts. Human labels are not passed as accepted answers, but the shared proposal generator creates correlated evidence. A system can agree with the catalogue because both adjudication processes test the same candidate—not because FORMA independently discovered or verified the correct physical interpretation.

A Redrock-only or candidate-ranking baseline is therefore essential. The paper cites Redrock as a hypothesis source but reports no baseline binary agreement, redshift agreement, selective coverage, or incremental correction attributable to FORMA. It also does not compare a deterministic-rule auditor, one-agent workflow, no-knowledge-base condition on the main corpus, no-raw-spectrum auditor, alternate base model, or independently authored expert audit. The evidence does not identify which module creates the selective accuracy pattern.

### Development/evaluation chronology

The run is described as zero-shot without dataset-specific training (lines 129–130). That does not establish held-out evaluation. Prompts, CWT thresholds, knowledge rules, confidence definitions, class diagnostics, and the operational medium threshold can be manually developed against the same catalogue or examples without model training.

No chronology is reported for interviews, KB/prompt authoring, tool thresholds, pilot spectra, error analysis, rule changes, sample draw, main execution, threshold selection, or manuscript figures. The repository contains self-evolution code that can compare outputs with `VI_Z/VI_SPECTYPE` when enabled, although `.env_example` defaults `SELF_EVOLVE=false`; no per-trial manifest establishes the paper’s exact setting. Absent a frozen development set and immutable predeclared analysis, “zero-shot” licenses only “no reported model fine-tuning on this dataset,” not untouched evaluation.

## Evidence and denominator audit

### Coverage–agreement result

At the low-or-higher threshold, the paper reports 70.4% coverage and 90.0% binary agreement; at medium-or-higher, 28.9% and 95.5%; high has 18 cases and 100% agreement (lines 141–146). The medium-or-higher matrix contains:

- expert QSO: 100 agreements / 103 retained;
- expert galaxy: 216 / 228 retained;
- total: 316 / 331 = 95.468%, reported as 95.5%; and
- 15 disagreements.

The medium coverage is 331/1,149 = 28.808%, consistent with 28.9% after rounding. The disclosed counts imply descriptive Wilson 95% intervals of approximately 92.7–97.2% overall, 91.8–99.0% for QSO, 91.0–97.0% for galaxy, and 82.4–100% for the 18/18 high tier. These intervals are calculations for interpretation, not paper-reported inference. They omit task/source clustering, threshold selection, and model/judge uncertainty.

The rounded 70.4% is consistent with 809/1,149 definite low-or-higher cases, and 90.0% is consistent with 728/809 agreements. That reconstruction would imply that moving to medium-or-higher defers 478 additional cases and removes 66 of 81 disagreements but also 412 agreements. Because the paper does not disclose the underlying low-threshold count/table, those integers remain a rounding-consistent reconstruction rather than an independently verifiable result.

This is a selective classifier. Its central operational object is a **risk–coverage curve**, not accuracy alone. The paper does not report:

- per-class coverage denominators at each threshold;
- false-accept/false-defer costs;
- the composition and severity of the 15 retained errors;
- redshift-catastrophe rates among binary agreements;
- coverage by SNR, VI quality, catalogue/source, redshift, ambiguity, or artifact flags;
- repeated-run threshold crossings;
- whether deferred cases are harder for experts or more scientifically consequential; or
- downstream bias from analysing only the selected subset.

The stated per-class agreements—97.1% QSO, 93.8% LRG, 94.5% ELG, 95.0% BGS—lack class-specific retained denominators/confusion counts in the text or release. Without coverage by class, these conditional rates cannot show equitable or representative automation.

### Redshift and SNR evidence

Figure 2c qualitatively shows tighter residual distributions at higher credibility with `|Δz| ≤ 0.01` as a reference tolerance. Figure 2d shows variation within the low tier by an SNR ratio. The paper provides no bin counts, numerical residual summaries, confidence intervals, catastrophic-outlier counts, alternative tolerance sensitivity, regression controlling class/redshift, or released arrays. The text’s inference that credibility “reflects evidential support” is stronger than correlation permits.

The SNR analysis shows only that the ordinal label is not perfectly identical to one summed median-SNR indicator. Credibility rules explicitly use local SNR, edge zones, masked regions, line inventory, widths, and skyline coincidence. It may be a nonlinear data-quality/feature-detectability function rather than a distinct measure of scientific validity. A matched or conditional comparison is needed to separate information quality from reasoning quality.

### Error severity and scientific correctness

Binary QSO-versus-galaxy agreement treats all disagreements alike. It does not distinguish an innocuous LRG/BGS subtype mismatch, QSO missed as galaxy, galaxy promoted to QSO, severe redshift error, physically impossible line catalogue, or uncertainty that should trigger follow-up. Conversely, binary class agreement can coexist with a scientifically unusable redshift or wrong evidence path.

No independent expert panel audits a stratified sample of FORMA reports, retained errors, agreements, and deferred cases. No follow-up observations establish truth. The low-luminosity AGN example is explicitly an expert-supported candidate rather than a discovery (lines 197–204), which is appropriately cautious but cannot validate recovery. The evidence supports catalogue concordance and an interpretable candidate report, not scientific correctness.

## Counterfactual evidence-ablation audit

### Design

Starting from one broad-line QSO at `z=2.92`, the authors create two forgeries (Appendix B, lines 1262–1281):

1. remove the Lyα region and delete corresponding catalogue/hypothesis entries; and
2. narrow three broad lines to approximately 900–1,000 km/s and rewrite catalogue entries accordingly.

The spectrum and upstream records are co-edited so the Result Auditor receives internally aligned but physically inconsistent evidence. Upstream feature detection, hypothesis generation, single-hypothesis evaluation, Feature Auditor, and synthesis are held fixed; only the Result Auditor is rerun 100 times. The official example README is even clearer: upstream files were manually edited, the full upstream pipeline was deliberately not rerun, and the experiment isolates the last-line-of-defence auditor.

This is a useful component test. It asks whether one observer reacts to a meaningful intervention when superficial upstream consistency is preserved. It does **not** show that the complete workflow catches naturally occurring errors, that upstream modules would produce those exact forged records, or that the system distinguishes the planted defect from unrelated distribution-shift cues.

### Reported and released results

Table B1 reports:

| Forgery | Original KB `NEEDS_REVISION` | Modified KB `NEEDS_REVISION` |
|---|---:|---:|
| Lyα removed | 97/100 | 86/100 |
| Broad lines narrowed | 100/100 | 99/100 |

The modified KB removes the directly relevant textual criterion. The corresponding confidence shifts from mostly LOW under original KB to more MEDIUM under modified KB (lines 1291–1311).

The pinned release contains exactly two `_summary.json` files:

- Lyα: 86 `NEEDS_REVISION`, 14 `CONFIRM`; 75 MEDIUM, 25 LOW; total recorded time 9,103 seconds (91.03 seconds/run).
- Narrow lines: 99 `NEEDS_REVISION`, 1 `CONFIRM`; 23 MEDIUM, 77 LOW; total recorded time 12,539 seconds (125.39 seconds/run).

These match the **modified-KB** columns, not the original-KB columns. The original-KB 97/100 and 100/100 records are absent. The release also does not pin an explicit KB-diff manifest showing which bytes produced each summary. The current `classification.md` contains fatal Type-1 QSO rules, so the relationship between current KB, removed-rule KB, and reported original condition is not reconstructible from one snapshot.

The batch scripts are not runnable as released: they insert a path ending in `src` and import `AstroAgent.*`, while the snapshot’s package is `FORMA`; a direct import check produces `ModuleNotFoundError: No module named 'AstroAgent'`. The scripts hard-code `deepseek-v4-pro`, a mutable API base URL, temperature 0.1, and disabled thinking, but do not preserve provider response IDs, exact endpoint revision, seeds, token usage, cost, retry ledger, invalid-call denominator, or raw original-KB attempt set.

The 100 repetitions are therefore useful reported stochastic evidence for one auditor/input pair, with partial retained evidence for two cells. They are not a reproduced four-cell experiment. A stronger test would cross many source spectra, defect types, sham edits, irrelevant-region edits, natural upstream errors, KB rules, base models, and auditor implementations while reporting sensitivity, false-positive rate on untouched controls, severity, and clustered uncertainty.

## Unique insight

### The evidence path is an evaluated artifact, but an evaluated path is not independent truth

FORMA’s most transferable contribution is to make the reasoning substrate itself inspectable:

`observation → feature claim → hypothesis → alternative → deterministic check → audit revision → credibility/disposition → report`

This is better than treating a final label as the only artifact. It enables checks such as:

- was the cited feature actually observed at the claimed location?
- was its uncertainty and instrumental context retained?
- which alternatives were considered and why rejected?
- which numerical relations were computed deterministically?
- did the auditor have a meaningfully independent evidence view?
- what unresolved issue caused deferral?

But every arrow can be jointly wrong. A shared feature extractor can omit the decisive signal; a candidate generator can constrain all downstream alternatives; a knowledge base can encode a false or context-inappropriate rule; two agents using the same model can share an error; a report can faithfully preserve a circular evidential path; and a credibility gate can select cases that resemble its authored criteria without identifying truth.

For `skill-bench`, “auditable” should mean **challengeable provenance**, not “verified.” Preserve at least five separate observations:

1. **protocol conformance:** did the system execute required evidence/alternative/audit operations?
2. **reference agreement:** does the resulting decision match an authorized reference, conditionally on coverage?
3. **independent correctness:** does evidence not coupled to the proposal/reference process support the conclusion?
4. **decision validity:** was accept/defer/reject calibrated to intended loss and population?
5. **downstream consequence:** did use of the decision improve the recipient’s work without unacceptable harm/burden?

### Deferral changes the estimand

The 95.5% headline is not performance over 1,149 items. It is agreement among 331 items passing a judge-authored credibility policy. Deferral is legitimate and often professionally correct, but it creates an eligibility mechanism. The benchmark must report selected risk and population coverage together, retain all deferred cases, and test whether selection hides the hardest or most consequential work.

A benchmark should not score defer as simple failure or silently remove it. It should separate:

- correct defer due to insufficient evidence;
- unnecessary defer despite sufficient evidence;
- defer caused by invalid tooling/environment;
- defer that reaches an authorized reviewer with useful evidence;
- defer that creates no completed handoff; and
- accepted decision later contradicted by independent evidence.

This connects FORMA’s credibility gate to existing `skill-bench` abstention, handoff, metric, and validity machinery without requiring an astronomy-specific contract.

## Comparison with adjacent reviewed work

- **ResearchRubrics:** makes expert attention explicit as criteria but shows that authored checks, judge access, and score claims require separate authority and calibration. FORMA goes further by linking criteria to raw numerical evidence and alternatives, but its unstructured credibility label is less reproducible than a criterion ledger and has no expert-label reliability study.
- **PaperBench:** preserves dense implementation/execution/result criteria yet its scalar measures partial rubric attainment rather than replication. FORMA similarly promotes a configured aggregate judgment toward “verification.” Both need noncompensatory claim gates and independent correctness evidence; FORMA adds selective coverage as a central estimand.
- **LQCDMaster:** closes much of the scientific execution loop but leaves evaluator and independent-physics loops open. FORMA closes more of the evidential-audit representation while lacking execution-scale scientific outputs and an independent truth loop. Together they show that rich traces and executable tools are necessary but not self-validating.
- **Expert-disagreement study:** warns that expert labels may represent framework-conditioned judgments rather than one truth. FORMA’s DESI reference has stronger procedural consensus than a single rater, but individual labels/disagreement are not preserved for the selected cohort and a shared Redrock proposal can induce consensus. Agreement should remain observer- and procedure-indexed.
- **Executable-consequence work in `skill-bench`:** already separates output, state transition, recipient uptake, action, and consequence. FORMA’s accepted/deferred report stops before scientific use; “allowing outputs to be evaluated before they enter use” is a workflow affordance, not evidence of beneficial downstream use.

## Reproducibility and operational realism

**Paper inspectability: moderate to strong.** The 26-page paper discloses architecture, prompts/tools at a useful level, sample construction, principal counts, feature-score failure, two counterfactual manipulations, and important scientific limits. It does not disclose chronology, exact full-corpus configuration, threshold predeclaration, statistics, costs, failures, or per-case outputs.

**Release inspectability: strong for implementation, weak for headline evaluation.** The pinned tree contains executable architecture, prompts, KB, deterministic tools, quick-start material, two standard FITS files, forged spectra, upstream traces, and modified-KB batch summaries. It has no tests, evaluation cohort, main result ledger, aggregate builder, original-KB summaries, or stable runner for the examples.

**Computational reproducibility: limited.** The release requires Python/Docker dependencies, Redrock and templates, DESI data, and a mutable commercial endpoint. Model identity is a provider name rather than immutable weights. The `.env_example` and README disagree on defaults such as harness concurrency (50 versus 3) and CWT SNR threshold (8.0 versus README 5.0), and no paper-trial manifest resolves exact settings. Code availability supports inspection, not Figure 2 reconstruction.

**Operational realism: meaningful but bounded.** Numerical FITS input, instrumental masks, multi-arm spectra, template candidates, deterministic measurements, OH/edge effects, abstention, alternative hypotheses, and human-readable audit reports are materially realistic. The evaluation omits ingestion operations at catalogue scale, API failure handling evidence, service quotas, security/privacy, latency/cost budgets, monitoring, version drift, expert handoff completion, correction/update workflows, downstream analyses, and external confirmation.

**Empirical inference: weak to moderate.** A 1,149-case designed sample and 331 retained decisions provide a nontrivial case study, but one catalogue, one base model, one run per main item, same-set threshold choice, missing per-case data, coupled Redrock proposals, and no comparator/independent truth sharply limit causal and general claims.

## Limitations and validity threats

### Expertise and protocol provenance

1. Interview participants, count, authority, instruments, transcripts, coding, disagreement, and consent are absent.
2. Visual-inspection documentation versions and claim-level source locators are not preserved.
3. No expert signs off the transformed prompts, KB rules, tools, thresholds, or failure dispositions.
4. Human visual review and numerical-array/CWT-to-text review are different interventions.
5. Domain rules in a mutable KB are treated as standards without source, scope, valid time, or disagreement metadata.

### Data and reference construction

6. The 1,149 sampled IDs, random seed, source hashes, selection script, and missingness are unreleased.
7. Balanced class sampling does not estimate survey prevalence or production utility.
8. Stars and other classes are omitted; QSO/galaxy scoring collapses subclasses.
9. Individual VI observations, disagreement, merge/adjudication route, quality, and flags are absent for the cohort.
10. DESI experts and FORMA share Redrock proposal anchoring, weakening independence.
11. The paper challenges low-SNR VI truth while using VI type/redshift as its evaluation reference.
12. No external follow-up or independent panel establishes scientific correctness.

### Configured system and identification

13. No Redrock-only baseline identifies incremental verification value.
14. No module, prompt, KB, tool, raw-evidence, or model ablation is run on the main corpus.
15. The “independent” auditor shares model, upstream evidence, KB, tools, and authorship.
16. No full-pipeline repeated runs quantify stochastic classification, redshift, credibility, or threshold instability.
17. Exact endpoint revision, request/response IDs, seeds, token/cost records, retries, and invalids are absent.
18. Zero-shot training language does not establish untouched development or predeclared analysis.

### Scoring, selection, and statistics

19. Credibility is an LLM ordinal judgment without a deterministic scoring specification.
20. The operational medium threshold appears selected from the same set used to report agreement.
21. Conditional agreement is foregrounded while 71.2% of cases are outside the medium definite pool.
22. Class-specific coverage and retained denominators are absent.
23. No uncertainty, clustering, multiple-threshold correction, or selection-aware inference is reported.
24. The 18/18 high tier is too small for a 100% reliability claim; a descriptive Wilson lower bound is about 82.4%.
25. Binary agreement hides error severity, subtype errors, redshift failures, and downstream consequence.
26. Redshift and SNR figures lack released arrays, bin counts, numerical summaries, and controlled analyses.
27. “Well-calibrated” and “tracks evidential sufficiency” exceed the reported monotonic association.

### Counterfactual evidence

28. Only one source spectrum and two obvious defect families are tested.
29. Spectrum and upstream catalogues are manually co-edited; the full upstream pipeline is not rerun.
30. No untouched/sham/irrelevant-edit false-positive controls are reported.
31. Original-KB summary records are absent; released summaries cover only modified-KB results.
32. Released example runners import nonexistent `AstroAgent` paths and are not runnable unchanged.
33. KB variant bytes/diffs, model receipts, invalid attempts, retries, seeds, token use, and costs are missing.
34. The counterfactual test establishes auditor sensitivity to planted defects, not natural-error detection or whole-system robustness.

### Transfer and readiness

35. General transfer beyond spectroscopy is proposed through analogy, not tested.
36. No independent domain instantiation validates the five-requirement protocol.
37. The low-luminosity AGN case is a candidate aligned with expert interpretation, not confirmed discovery.
38. No downstream study shows that accepting medium/high cases improves scientific analysis.
39. Manual-review workload, handoff quality, false deferral cost, and reviewer correction burden are unmeasured.
40. Production reliability, endpoint drift, throughput, total cost, observability, rollback, and governance are untested.

## Transfer to skill-bench

### Retain

1. **Evidence-to-alternatives-to-audit structure.** Require a candidate conclusion to carry observation locators, uncertainty/context, plausible alternatives, disconfirming tests, deterministic checks, unresolved issues, and a disposition.
2. **Typed observer evidence views.** Record what each stage can see. “No chain of thought” is only one independence dimension; also record model, prompt/KB, preprocessing, tools, upstream records, authorship, and data overlap.
3. **Deterministic/model boundary.** Keep arithmetic, transforms, schema checks, and artifact measurements in versioned deterministic tools where feasible, while retaining their inputs/outputs and validation status.
4. **Explicit defer/review.** Do not force a decision when evidence is insufficient; preserve why and what evidence would resolve it.
5. **Counterfactual evidence tests.** Plant evidence-removal, contradiction, and alternative-consistency cases that test whether decisions depend on the intended evidence.

### Repair

6. **Do not call an ordinal judge label a calibrated score without calibration evidence.** Name it `auditor_credibility_label` until held-out risk/coverage and repeat reliability are established.
7. **Report selective risk and coverage jointly.** Include full denominator, class/critical-slice coverage, false accept/defer, threshold sensitivity, repeated-run crossings, invalids, and clustered uncertainty.
8. **Use independent comparators.** Compare proposal engine alone, deterministic rules, one-stage judge, full workflow, alternate model/KB, and independent expert/scientific evidence.
9. **Preserve source-authority lineage.** Bind each procedure/rule to exact source/expert authority, scope, valid time, disagreements, transformation history, and approval.
10. **Separate conformance from correctness.** A complete evidence trail may support process compliance even when the conclusion is wrong; an independently correct conclusion may arise through an invalid shortcut. Score both.
11. **Predeclare thresholds and chronology.** Freeze development corpus, prompts/KB/tools, evaluation cohort, threshold/loss policy, and analysis before main trials.
12. **Retain all attempts and deferred cases.** Never construct the published denominator only from valid, confident, or favorable outputs.

### Test

13. In an existing cross-domain pilot, use the current observer/metric/validity machinery to compare matched conditions: proposal only; proposal plus evidence extraction; proposal plus alternatives; full audit; and a sham auditor. Freeze independent endpoint checks and evaluate protocol conformance, selected risk, coverage, independent correctness, burden, and downstream utility separately.
14. Add sham and orthogonal counterfactuals: remove decisive evidence, alter irrelevant evidence, insert a plausible competing explanation, corrupt a deterministic tool output, and modify a KB rule. The expected outcome is not always rejection; it is a predeclared disposition tied to the affected warrant.
15. For human review, sample agreements, errors, and deferrals across confidence and consequence strata. Preserve independent labels, disagreement, evidence view, correction, and whether the audit report reduces review time or improves decisions.

## Claim ledger

| Claim | Status after full-paper/release audit |
|---|---|
| A paper-time implementation and structured audit workflow exist | Supported |
| The workflow retains evidence, alternatives, audit outputs, and reports | Supported by code/examples; not all main trials released |
| The method is source-faithful to validated expert practice | Not established |
| Main sample is 1,149 with disclosed class totals | Author-reported; construction described, manifest unreleased |
| Medium-or-higher set is 331 with 316 binary agreements | Author-reported counts arithmetically consistent; raw rows unreleased |
| 95.5% is performance over the full evaluation population | Rejected; it is conditional on 28.8% selected coverage |
| Credibility is calibrated | Not established |
| FORMA improves over Redrock | Not tested |
| Auditor judgment is independent | Only chain-of-thought-separated; broader independence rejected |
| Counterfactual auditor sensitivity is robust | Bounded support for two planted defects on one source; only modified-KB summaries released |
| Figure 2/Table B1 are reproducible from release | Blocked |
| Decisions are independently scientifically correct | Not established |
| Cross-domain executable verification is demonstrated | Not tested |
| Production/scientific-use readiness is established | Not established |

## Action items completed

- [x] Read the complete immutable v1 PDF/text and arXiv source.
- [x] Audited the complete official paper-time repository snapshot and provenance.
- [x] Reconstructed sample, coverage, agreement, and counterfactual denominators.
- [x] Inspected expertise transformation, modules, prompts, tools, KB, score construction, and evidence views.
- [x] Audited selective coverage, shared Redrock channel, threshold chronology, comparator absence, and scientific-truth boundary.
- [x] Verified released counterfactual summaries and bounded their reproducibility.
- [x] Compared the mechanism with ResearchRubrics, PaperBench, LQCDMaster, expert disagreement, and executable-consequence work.
- [x] Added no queue task: the evidence sharpens existing observer, metric, task-health, claim-validity, authority, abstention, and executable-consequence contracts; a new FORMA-specific build would duplicate them.
