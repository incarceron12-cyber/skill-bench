# Configured artifact revision trial

This non-releasable vertical slice applies the DELEGATE-52-inspired requested-delta/preservation split to a fresh configured-agent revision of a retained vendor-pilot artifact.

## Design and provenance

- Original artifact: copied byte-for-byte from `pilots/vendor-incident-response/trials/agent-run-20260711-v2/trial/outputs/incident-brief.md`; SHA-256 `a08c49716c45a2f7a20ba72c2145f48f8b309fa72b59c0391f342cffe50479b4`.
- Method basis: `papers/agent-benchmarks/2026-07-11-delegate52-delegated-artifact-integrity.md`, especially pp. 20–22 and review lines 120–143, 193–199. Release provenance is pinned in `data/sources/releases/2604.15597v1-delegate52/provenance.json`.
- General hypothesis: requested-delta success and collateral preservation can be checked separately on non-planted agent output.
- The public request contains one must-change predicate, explicit preservation/forbidden-change rules, one permitted normalization, and a fail-closed invalid-environment policy.

`launcher.py` snapshots only the request, copied artifact, and signed public source into a read-only bubblewrap namespace; only `/trial/outputs` is writable. The preflight canary makes zero model calls and checks cwd, visibility, private-file denial, write boundaries, and configured tools. The trial pins Hermes `gpt-5.6-sol` / `openai-codex` / file tools / safe mode and retains manifests, hashes, redacted stdout, stderr, and usage.

`validate_revision.py` checks the actual output, exercises no-op/unauthorized-addition/over-edit/normalization/invalid-execution mutations, and replays vendor grader v0.3.0 against its original immutable evidence view with only the revised brief substituted.

## Result boundary

The retained v1 run passed the isolation canary, completed, preserved read-only inputs, made the exact requested insertion, preserved every original nonblank line, and passed all five mutations and the prior grader. This is one configured synthetic attempt. It does **not** establish treatment effect, professional validity, general capability, reliability, cross-domain generalization, real-world safety, or readiness.
