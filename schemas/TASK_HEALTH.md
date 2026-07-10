# Task health and lifecycle contract v0.1

`task-health.schema.json` and `scripts/validate_task_health.py` add the operating
layer between an immutable benchmark instrument and claims that a task is fit
for a particular role over time:

```text
origin / selection -> exact-version witness -> contrasts / replicate policy
                   -> health evidence -> adjudication / immutable revision
                   -> role transition or retirement
```

This advances charter objective C with reusable cross-domain infrastructure. It
does not make the LH pilot the benchmark's permanent domain. The bounded
hypothesis is that capability probes, regression guards, critical diagnostics,
and calibration items are evidence-backed states of versioned instruments—not
static suite labels or pass-rate aliases.

## Enforced boundaries

1. **Immutable operating basis.** Tasks, suites, graders, harnesses,
   environments, trials, transcripts, measurements, and benchmark versions are
   path/version/SHA-256 bound. `--check-paths` checks local existence and bytes.
2. **Selection history.** Origin and privacy are typed. Treatment-outcome-
   influenced admission cannot be relabeled confirmatory, transfer, or
   operational evidence; this carries the SkillsBench selection warning into an
   executable boundary.
3. **Narrow reference claims.** A reference attempt must pass and can claim only
   `witness_pass_for_exact_versions_only`. It establishes one executable route,
   not ambiguity, validity, plural-path acceptance, capability, or readiness.
4. **Contrast and replication semantics.** Positive and negative boundary cases
   are both required. The policy names `k`, grouping, seed/reset/fingerprint,
   independence threats, and empirical reporting; it does not derive `p^k` from
   pooled pass@1.
5. **Evidence-backed role changes.** Regression graduation requires acceptable
   repeat stability, invalid-run rate, and unresolved-instrument-invalidity
   signals plus an owner-defined consequence. Saturation alone is rejected.
6. **Fail-closed adjudication.** The observation basis and immutable evidence
   view are typed; agent-failure and accepted-alternative decisions require a
   transcript artifact. Task, grader, harness, environment, or observability
   defects are excluded from capability aggregation. Instrument defects require
   a distinct same-type replacement version and matching revision.
7. **No historical rewriting.** Revisions preserve old scores (or void them
   while preserving the record), state comparability, and bind old/new versions.
8. **Coverage-aware retirement.** Retirement records replacement, critical
   coverage, evidence, and comparability rather than deleting saturated items.

## Calibration fixture

`tests/fixtures/valid-task-health.json` uses the non-releasable LH pilot solely
to exercise the contract. It includes:

- the retained one-arm v6 attempt as a narrow exact-version witness;
- builder-authored repeat, saturation, contrast, and owner records explicitly
  labeled synthetic rather than observed health evidence;
- a capability-to-regression transition shape with all required evidence types;
- a planted grader-defect adjudication that creates `grader-v2`, excludes the
  affected result from capability aggregation, and preserves the old score;
- explicit denial of agent capability, treatment effect, grader accuracy,
  professional validity, production relevance, and release-readiness claims.

The replacement grader and health measurement are inert fixture records, not
claims that the live pilot grader is defective or corrected.

## Rationale and provenance

| Choice | Evidence or project adaptation |
|---|---|
| Maintained task evidence history and typed capability/regression roles | `docs/concepts/anthropic-agent-evaluation-lifecycle.md`, Unique insight and Concrete transfer |
| Reference witness is an exact-version smoke test | same concept note, tensions 3 and semantic invariant 2 |
| Replicate grouping and independence threats | same concept note, tensions 4 and semantic invariant 7 |
| Defects create new versions and preserve old scores | same concept note, semantic invariants 3–4 |
| Saturation cannot alone graduate or retire critical coverage | same concept note, semantic invariants 1 and 6 |
| Outcome-conditioned selection history | `papers/agent-benchmarks/2026-07-10-skillsbench-paired-skill-efficacy.md`, Transferable design pattern 1 and Concrete change 6 |

Anthropic's article is an official experience report, not a controlled study;
SkillsBench establishes the selection threat in its own released inventory but
not this schema's validity across domains. The contract remains a project design
hypothesis pending real task operations, expert review, and cross-domain use.

## Validate

```bash
python scripts/validate_task_health.py --check-paths \
  tests/fixtures/valid-task-health.json
python -m unittest tests.test_validate_task_health -v
```
