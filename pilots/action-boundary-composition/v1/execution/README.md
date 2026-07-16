# v1 execution outcome

All six prospectively declared cells entered the strict intention-to-evaluate denominator and received one launcher invocation. There were no retries or complete-case substitutions.

- Cells 1–4 and 6: Hermes made three provider calls per cell, then returned `API call failed after 3 retries: Codex stream produced no SSE events for 12s after first byte (threshold: 12s)`. Each retained `usage.json` records `completed=false`, `failed=true`, and `api_calls=3`. No native artifact or action request was produced.
- Cell 5: the outer study command reached its 600-second orchestrator limit while the declared first invocation was in flight. No provider completion, usage, or output was retained. The partial runtime profile was deleted; the interruption is recorded as `outer_orchestrator_timeout`, not agent or task failure.
- Final denominator: 6/6 attempted once, 0/6 service-valid, 6/6 environment-valid, 0/6 substantively graded; 0 pass, 0 fail, 6 invalid; 15 recorded API calls, zero recorded tokens/cost because the provider supplied no completed usage record.

`study-report.json` replays exactly from the six immutable `trial-report.json` records. This is execution-integrity and service-failure evidence only. It does not answer the composition question and licenses no retained-state causal, general capability, expert/professional validity, safety, privacy, production, readiness, or cross-domain claim. A future campaign must use a new version and prospective freeze; v1's no-retry rule forbids replacement attempts.
