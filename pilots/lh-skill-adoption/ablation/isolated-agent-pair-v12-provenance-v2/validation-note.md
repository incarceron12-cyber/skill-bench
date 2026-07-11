# Provenance v2 configured-pair validation note

The predeclared v12 continuation ran one frozen concurrent no-skill/public-skill pair after this scheduled `gpt-5.6-sol`/`openai-codex` run demonstrated provider availability. Both conditions received the unchanged v8 task/source pack and identical provenance-v2 public contract; only the predeclared public Skill treatment differed. Explicit zero-call and in-trial file-tool canaries passed for both arms under launcher hash `b1990ac42f5fcf506171487f18d98c30915c170d8a726e466d1c3f42b4eed917`.

The no-skill arm again failed at the provider boundary after three calls produced no SSE event within the frozen 12-second threshold. It produced no deliverables. Its usage record and fail-closed v2, legacy, and claim-grader records are retained as execution-integrity evidence only, not artifact-quality evidence.

The public-skill arm completed after six calls and produced both deliverables (37,615 total tokens; provider-reported included cost `$0.00`). The private claim calibrator passed contradiction reconciliation and causal-scope checks, but this is only internal instrument output and does not establish expert validity.

## Frozen prospective result and parser review

Provenance v2 **did not pass** the non-planted public-skill artifact: four numeric diagnostics, zero abstentions. Inspection against the frozen public contract separates two causes:

- **One true disclosed-contract failure:** memo line 19 introduced a program-set `95%` governance threshold without the required `{{PROSPECTIVE:...}}` marker.
- **Three instrument-caused false rejections:** memo lines 11, 21, and 42 rendered the source's `>=4` threshold as `4`. The v2 parser compares literal normalized token strings, so `>=4` and `4` differ even though the claim says “at least 4” and cites E10. These are not unsupported values.

The legacy counterfactual also failed with six diagnostics. V2 correctly eliminated the legacy grader's false rejections of scope values `92` and `31`, demonstrating that scope inclusion improved. It did not eliminate comparator-normalization error, and the artifact used no valid prospective marker, so the intended abstention path was not exercised.

No score was rewritten, no parser or threshold was changed, and no additional pair was run. The exact component and attempt hashes are in `component-manifest.json`; grader outputs remain separately replayable.

## Interpretation boundary

The asymmetric provider failure prevents a matched treatment estimate. This single completed arm also cannot establish capability, professional/expert validity, reliability, generalization, or release readiness. Useful continuation is a bounded comparator-normalization correction plus planted reconformance tests; any later configured pair must be separately authorized and must preserve these historical results unchanged.
