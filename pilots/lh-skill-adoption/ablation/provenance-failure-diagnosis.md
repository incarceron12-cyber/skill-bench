# LH evidence-provenance failure diagnosis (v8/v10)

## Scope and evidence

This is a frozen exact-version diagnostic, not a rescore. `provenance-failure-diagnosis.json` hashes the public task, public Skill, source pack, grader, all four v8/v10 gradable output pairs, and their historical grader records. `scripts/diagnose_lh_provenance.py` replayed every historical failure exactly and created only temporary, builder-authored counterfactuals. No agent call or instrument change occurred.

Charter objective advanced: executable diagnostic evaluation (objectives B/C). The reusable question is whether an artifact failure originated in disclosure, realization, convention parsing, or grader scope—not whether this pilot domain is privileged.

## Predeclared hypotheses and observations

| Hypothesis | Result | Exact-version observation |
|---|---|---|
| H1 agent omission | Partly supported, not sufficient | One v10 public-Skill matrix row attaches `0.46` to E01 although that value belongs to E02. That is a real row-level realization error. It does not explain the recurrent whole-memo failures. |
| H2 instruction insufficiency | Supported | The task says to cite evidence IDs and the Skill says every material number needs an evidence ID. Neither discloses that only `[E01]`/`[E01, E02]` syntax is recognized, nor how prospective program thresholds should be marked. |
| H3 artifact-convention mismatch | Supported | v10 no-skill uses conventional `(E01, E02)` citations. They are visible to a reader but invisible to the square-bracket-only parser. Replacing only parenthetical groups with brackets in a temporary calibration copy reduced its diagnostics from 14 to 12; it did not make the artifact pass. |
| H4 grader false rejection | Supported as a lexical-scope defect | The grader matches every numeric token on a memo line only against cited `reported_value` fields. It therefore rejects source-supported scope numbers such as 92 runs and 31 tasks, plus prospective confidence levels, thresholds, sample sizes, list references, and dates. The task explicitly requires a decision threshold and minimum experiment, making some novel program-set numbers legitimate and unavoidable. |

Across the four retained artifacts, replay produced 48 diagnostics: 37 artifact-convention mismatches, one definite matrix realization error, and 10 grader-scope false-rejection candidates. These categories diagnose the interface; they do not establish that every underlying statement is semantically sound.

## Root-cause conclusion

The repeated binary failure cannot responsibly be labeled solely `artifact_structure_failure`. The earliest supported causes are mixed:

1. **public contract under-specification** (exact syntax and prospective-number semantics are hidden);
2. **artifact convention mismatch** (parenthetical and ranged forms are parser-invisible);
3. **grader scope error** (lexical matching conflates sourced measurements with task-required governance/design numbers and ignores numeric scope fields); and
4. **one observed artifact realization error** (wrong single-row numeric attribution).

The public Skill did not prevent failure, but these records do not identify a Skill effect. The grader remains a narrow lexical conformance check and cannot establish entailment, judgment quality, professional validity, capability, or readiness.

## One minimal versioned correction

Version the public artifact contract and grader together: disclose accepted `[E##]` syntax and introduce an explicit machine-readable marker for prospective program-set numbers on which the provenance grader **abstains**, rather than treating them as source measurements. Do not silently broaden citation parsing and do not rewrite v8/v10 scores.

Before any fresh agent trial, require conformance cases for bracketed groups, conventional parentheses, ranges, dates, prospective thresholds, mixed sourced/prospective lines, and wrong-row attribution. The correction passes only after independent review of abstention boundaries and frozen positive/negative regression tests. Whether it improves agent behavior remains unresolved until a fresh matched validation.
