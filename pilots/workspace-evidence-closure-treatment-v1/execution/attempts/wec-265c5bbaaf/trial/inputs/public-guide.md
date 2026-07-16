# Workspace evidence-closure procedure

Use a durable workspace record while completing the task:

1. Inventory every explicit obligation in the authorized source before editing.
2. For each obligation, record its source locator and current status.
3. Check the final native artifact against every obligation; record pass/fail/unknown separately.
4. Preserve already-correct content and record any newly introduced error check.
5. Bind the checked artifact by SHA-256 and state whether the report is fresh.

Write `outputs/workspace.json` with keys `obligations`, `checks`, `artifact_sha256`, `report_fresh`, and `new_errors`. This record is procedural guidance, not an evaluator oracle: private expected values, checks, labels, and rationales are not available.
