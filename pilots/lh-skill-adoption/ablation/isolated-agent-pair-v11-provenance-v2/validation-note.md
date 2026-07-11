# Provenance v2 configured-pair validation note

The predeclared v11 attempt exposed the same hashed provenance-v2 public contract to both conditions while preserving the v8 task/source pack and public-Skill treatment. Explicit zero-call and in-trial file-tool canaries passed in both arms. They proved task-scoped cwd, contract/source visibility, condition-specific Skill visibility, private repository denial, and the unique writable output root under launcher hash `b1990ac42f5fcf506171487f18d98c30915c170d8a726e466d1c3f42b4eed917`.

Both concurrent arms then failed at the provider boundary: each exhausted three OpenAI Codex calls because the stream produced no SSE event within the frozen 12-second threshold after first byte. Neither arm produced a memo or matrix, and both usage records mark token/cost accounting unavailable and `failed=true`. All canaries, redacted transcripts, empty stderr, failed usage records, trial reports, component hashes, and fail-closed missing-artifact grader records are retained.

Therefore provenance v2 was **not exercised on a non-planted artifact**. The missing-artifact grader outputs are execution-integrity records, not evidence that either agent violated provenance. There were no prospective-marker abstentions or substantive parser decisions to inspect, and no meaningful legacy counterfactual comparison. No extra pair was run and no threshold or instrument was changed.

This result clarifies service availability, not capability or treatment. Skill effect, capability, professional/expert validity, reliability, generalization, and release readiness remain false. A future separately queued continuation should wait for demonstrated provider availability, then rerun one frozen matched pair without tuning.
