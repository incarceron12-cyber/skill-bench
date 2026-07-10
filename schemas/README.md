# Benchmark bundle schema v0.1

`benchmark-bundle.schema.json` is the first executable contract for a complete
knowledge-work evaluation evidence chain:

```text
task → source pack → artifact contract → trial trace → rubric result → causal diagnosis
```

It is intentionally a **bundle schema**, not seven disconnected files. A local
schema alone cannot prove that a check names a real grader, that a failed check's
causal slice names real trace events, or that a completed trial covers every
required check and artifact. `scripts/validate_benchmark.py` therefore applies:

1. JSON Schema Draft 2020-12 shape, type, format, and conditional checks;
2. semantic reference checks across task, grader, check, artifact, trace, and
   trial records;
3. completed-trial invariants, including weighted aggregate recomputation;
4. optional verification that local provenance paths exist.

## Design rationale and evidence

| Contract decision | Why it is explicit | Repository evidence |
|---|---|---|
| Task, trial, grader, trace, and artifact are separate records | Final score alone loses stateful execution evidence and prevents diagnosis. | `docs/production-agent-systems.md`, “Complete evidence chains” |
| Every source/check/task design claim can carry provenance | Benchmark authors must be able to distinguish primary, expert, synthetic, reviewed, and derived claims. | `.hermes.md`, “Evidence standard”; `templates/task-metadata.md` |
| Domain primitives map to sources and checks | Tacit expertise becomes testable through hidden requirements, contradictions, thresholds, conventions, traps, and safety constraints. | `.hermes.md`, “Benchmark-building standard”; `templates/task-metadata.md` §4 |
| Artifact declarations and observed artifacts are separate | The expected professional deliverable and the actual immutable trial output serve different purposes. | `templates/task-metadata.md` §5 |
| Checks identify visibility and grader implementation | Public task material must remain separate from private/hidden verifier internals to control leakage. | `docs/state-of-the-art-map.md`, “Benchmark operation layer” |
| Trials record model, scaffold, skills, tool, and memory policy | Results are agent-system results; recording only the base model creates a scaffold confound. | `papers/agent-benchmarks/2026-07-09-agent-psychometrics.md` |
| Failed/error checks require root, surface, and causal-slice events | Failure location may differ from origin; useful runs preserve a compact causal chain. | `papers/agent-benchmarks/2026-07-09-strace.md` |
| Root-cause vocabulary includes task/grader/environment faults | A benchmark must distinguish agent capability failures from invalid or broken evaluation. | `templates/task-metadata.md` §6 and STRACE review limitations |

The fixture `tests/fixtures/valid-benchmark-bundle.json` is deliberately a
failed completed trial. It demonstrates that a score of zero can still preserve
a useful, machine-checkable diagnosis.

## Validate

The validator requires Python's `jsonschema` package (tested with 4.26):

```bash
python scripts/validate_benchmark.py --check-paths \
  tests/fixtures/valid-benchmark-bundle.json
python -m unittest tests.test_validate_benchmark -v
```

`--check-paths` applies only to `provenance.local_path`; trial artifact paths can
refer to external or ephemeral run storage and are not required to be present in
the repository.

## Deliberate v0.1 boundaries

- A bundle contains one task and zero or more trials. Cross-task suites and a
  normalized response-matrix export belong in a later layer.
- Trace payloads are referenced by path rather than embedded, avoiding large or
  sensitive prompt/tool data in benchmark metadata.
- The validator checks edge references and event order, but not dependency-graph
  acyclicity yet.
- Grader entrypoints are contracts, not executed by this slice. Sandboxed grader
  execution and grader-output ingestion remain separate infrastructure work.
- SHA-256 values are required for observed artifacts, but this validator does
  not resolve external run storage or recompute them.
