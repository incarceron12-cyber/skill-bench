# Cross-pilot clean-release conformance gate

`clean-release-manifest.schema.json` and `scripts/validate_clean_release.py` add a small release layer over existing pilot artifacts. They do **not** create another task, trial, task-health, metric, or validity schema.

## Design rationale and provenance

The full OmniaBench paper/release review (`papers/agent-benchmarks/2026-07-17-omniabench-broad-scenario-construct-validity.md`, especially Release defects 1, 4–7, 10 and Repair 10–12) found that a large inspectable release can still contain colliding local IDs, non-parsing environment code, absent result rows, ambiguous aggregation, and executable code without an outer sandbox. This gate converts those defect classes into fail-closed checks while reusing retained package identities and controls.

The v1 fixture selects two zero-call, builder-authored packages whose READMEs explicitly identify their inputs as redistributable internal fixtures:

- `pilots/provenance-first-evaluator/`: evaluates already-authored typed comparisons across structured artifact, action-trace, and handoff shapes.
- `pilots/provenance-observation-derivation/`: derives comparison relations from frozen record/set and ordered-sequence files before applying a decision policy.

They are materially different evaluator stages, not independent evidence of domains, occupations, or capability. All selected parent bytes are pinned and left unchanged.

## Gate semantics

A candidate passes only when:

1. release-item, package, task, component, and control identifiers are unique in their release namespace;
2. every retained path exists and matches SHA-256;
3. JSON components parse and every declared Python evaluator/adapter/replay compiles without importing or executing it;
4. redistribution status points to retained repository evidence rather than being inferred from public availability;
5. all packages reference one canonical, hash-bound aggregation specification (`logical conjunction`; no pooled capability score);
6. result evidence exists, is hash-bound, and satisfies declared JSON-pointer predicates;
7. each no-cost control names one pinned Python runner, exits as expected, and emits exactly the declared JSON result;
8. containment is explicit: these controls execute trusted builder code in subprocesses with timeout only; network and filesystem isolation are **not** upgraded into sandbox claims; and
9. package and release claim ceilings remain false.

Controls run only after static identity, hash, parsing, result-evidence, aggregation, containment, and claim checks pass. The validator does not run model-authored or third-party executable content.

## Reproduce

```bash
python scripts/validate_clean_release.py \
  pilots/cross-pilot-clean-release/v1/manifest.json \
  --output pilots/cross-pilot-clean-release/v1/conformance-report.json
python -m unittest tests.test_clean_release -v
```

A passing report establishes exact loadability and zero-call replay behavior for these retained fixture versions only. It does not establish agent capability, grader truth, professional validity, production safety or fitness, public-release readiness, or cross-domain generalization.
