# Isolated downstream-operation diagnostic

## Predeclared slice

Each frozen `isolated-agent-v3` handoff was copied byte-for-byte into a fresh consumer workspace. The consumer received only `handoff.json`, a public task, and a manifest; original source packs, producer traces, private rubrics, and the repository were excluded. Both attempts pinned `gpt-5.6-sol` / `openai-codex`, file tools, safe mode, a 900-second timeout, one attempt, and zero retries. The procurement operation required a decision record with an observable approval action and preserved risk control. The operations case required an action record that blocked draining and requested failover confirmation.

## Observed evidence

Both zero-call outer-envelope canaries passed, including denial of producer source-pack, producer-trace, and repository probes. Producer and consumer handoff SHA-256 values matched in both cases. Both agent processes returned zero and wrote usage records, but neither wrote the required operation artifact. The public task said to read `inputs/handoff.json` although the read-only input was mounted as `handoff.json`; both agents failed closed and explicitly reported the missing path. Per the frozen zero-retry policy, no corrected rerun was made. The retained trial reports therefore mark `complete=false` and `grader.outcome=not_scored` rather than converting an interface failure into a substantive downstream-operation failure.

## Diagnostic attribution

- **Producer handoff content:** not implicated by this run. Both frozen producer artifacts had passed their five-dimensional graders and their bytes reached the consumer unchanged, but downstream semantics were not exercised.
- **Consumer execution:** appropriate fail-closed behavior after following the declared path; no unsupported operation was fabricated.
- **Environment:** valid for the configured file-tool surface; both canaries passed and read-only input inventories remained unchanged.
- **Public operation contract:** earliest supported root cause. The task path and mount path disagreed (`inputs/handoff.json` versus `handoff.json`).
- **Check observability:** the grader is replayable on synthetic declared-shape outputs, but had no artifact to observe and correctly abstained.

This bounded failed slice does **not** establish human-recipient usability, expert validity, professional capability, cross-domain generalization, a treatment effect, productivity, downstream impact, or readiness. A future task may predeclare a corrected path and a new attempt; these records must not be overwritten.
