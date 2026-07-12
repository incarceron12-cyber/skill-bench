# Crossed evaluator-validity audit (fixed-trace slice)

This prospective, builder-authored calibration freezes nine cases across a structured evidence memo and an irreversible delegated action. It instantiates the Tool-Veritas review's five-link warning as executable cases: true failure, irrelevant difference, alternate valid path, stale/wrong target, missing observer view, incomplete communication, and unsafe superficial completion.

`evaluator-inputs.json` contains no reference verdict or rationale. `oracle-private.json` is separately encoded and loaded only after evaluator execution. `audit.py` crosses a retained exact-target native evaluator, a factual-gate-plus-restricted-qualitative evaluator, and four pinned model-judge calls against that reference; it preserves configuration hashes, raw verdicts, abstention, failure-type rows, disagreement loci, sensitivity/specificity, usage, and variance limits.

`model-judge-protocol.json` was frozen before execution. Two fixed-rubric and two regenerated-rubric calls used pinned `gpt-5.6-sol` / `openai-codex` / Hermes oneshot safe mode with no tools. All four returned the same nine verdicts and exactly matched the builder reference (sensitivity and specificity 1.0 with one abstention). This is only observed fixed-trace behavior: regenerated rubric prose was not independently shown criterion-equivalent, and four matches do not establish zero judge variance. The calls used 82,496 total tokens, exceeding the predeclared 50,000-token observation ceiling; `report.json` records this protocol deviation rather than hiding it. An initial four-call launcher attempt failed before provider execution because `none` is not a valid Hermes toolset and is retained under `model-runs-invalid-toolset-attempt/`.

Independent reference authorship and trajectory reruns remain unexecuted. The artifact is therefore a completed **fixed-trace crossed slice**, not the full empirical audit or evidence of evaluator superiority.

Run the deterministic replay and tests (do not rerun paid/provider conditions merely to reproduce the report):

```bash
python pilots/crossed-evaluator-audit/audit.py
python -m unittest tests.test_crossed_evaluator_audit -v
```

`run_model_judges.py` is the archived launcher. Re-execution creates new stochastic observations and must use a new run directory rather than overwrite retained evidence.

Design evidence: `papers/agent-benchmarks/2026-07-13-tool-calling-evaluator-validity-audit.md`, especially lines 128–179. Retained shapes are adapted from `pilots/provenance-first-evaluator/` and `pilots/principal-authority-consequence/`; all cases remain synthetic. No evaluator-superiority, criterion-equivalence, expert/professional-validity, capability, production, or readiness claim is licensed.
