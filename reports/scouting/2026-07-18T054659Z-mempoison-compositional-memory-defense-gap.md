# Scouting note — compositional persistent-memory defense validity gap

- **Timestamp:** 2026-07-18T05:46:59Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, HTML external-link triage, exact repository duplicate searches, and a pinned Hugging Face API/tree plus dataset-structure inspection only. The PDF body, appendices, case semantics beyond one schema/sample inspection, author validation records, generation prompts, memory-system implementations, defense code, model outputs, judges, or result tables were **not** deeply read, downloaded into the repository, reproduced, or audited during scouting.

## Substantive candidate — triage only

**MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents** — Jifeng Gao, Kang Xia, Yi Zhang, Xiaobin Hong, Mingkai Lin, Xingshen Wei, Wenzhong Li, and Sanglu Lu; arXiv:2607.14651v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.14651v1 · https://arxiv.org/pdf/2607.14651v1 · https://arxiv.org/html/2607.14651v1
- Pinned dataset revision: https://huggingface.co/datasets/MemPoison/MemPoison/tree/12d0821a9a304d50485cf08ecf27ec874f98f836
- The arXiv API reports v1 submitted and last updated 16 July 2026 in `cs.CR` and `cs.AI`; its summary contains no withdrawal or retraction notice. Immutable record, PDF, and HTML endpoints returned HTTP 200; the PDF response reported 2,050,943 bytes.
- The abstract describes 1,227 hand-validated cases spanning four attack types, three injection channels, three memory substrates, seven open-weight and three closed-weight model families, and three tiers: direct single-record corruption (L1), compositional multi-record corruption (L2), and context-triggered dormant corruption (L3). It reports that write-time consistency defenses suppress direct attacks but fail more often on compositional and dormant cases, and introduces mechanistic influence decomposition. These are author-stated abstract claims awaiting full-paper verification.
- The paper HTML did not expose an author release link in targeted external-link triage. Targeted search nevertheless found a public, ungated CC-BY-4.0 Hugging Face dataset under the matching `MemPoison` identity. The API pins revision `12d0821a9a304d50485cf08ecf27ec874f98f836`, reports last modification 6 May 2026, and exposes only `.gitattributes`, a 139-byte metadata-only README, and `MemPoison_full1227.json` (3,198,888 bytes; Git object `c79c06d24c9cb5c43d1a1f3bf8a4191aa62b53d8`). Structural inspection confirmed a 1,227-item JSON list with fields for case/family identity, attack type, injection channel/turns, difficulty, context, domain, clean/poison anchors, and trigger tasks. Counts are 353 L1, 253 L2, and 621 L3; channels are 481 user-input, 513 tool-return, and 233 cross-agent cases. Every row carries `tier: gold_seed`. The matching count and taxonomy make the dataset a high-confidence candidate release, but absent an author link or informative card means authority, paper-version correspondence, validation provenance, and completeness remain unverified.
- Exact ID/title searches found no local review or queue task. A prior scout explicitly deferred MemPoison because of overlap and said to reconsider only if release inspection revealed distinct evidence. The newly pinned 1,227-row release does so: it makes family dependence, multi-record composition, dormant trigger conditions, injection-channel variation, and all-row `gold_seed` labeling inspectable rather than merely abstract claims.

## Why this is now a narrow, useful gap

The reusable chain is:

`source actor/channel and authority → candidate memory write → write-time observer and admission → versioned stored records → later retrieval opportunity and composition → trigger/context realization → proposition or instruction adoption → attempted and realized action/artifact/state effect → affected-party consequence → detection/quarantine/repair/forgetting → retained benign utility`.

Existing reviews separate memory authority, lifecycle operations, conflicting-memory consumption, context compaction, persistent writes, prompt-injection exposure, and action consequence. They do not directly audit the case where **each admitted record may look benign in isolation but a later joint retrieval or contextual trigger creates the harmful treatment**. This is a useful stress test for non-local observer coverage: record-level write filters cannot establish composition-level safety unless the benchmark preserves which records were admitted, co-retrieved, semantically combined, adopted, and consequential.

The release also raises sharp validity questions. All 1,227 cases are labeled `gold_seed` despite a large, patterned family structure; generated variants may be clustered rather than independent; clean/poison anchors and trigger prompts may co-author both treatment and oracle; synthetic enterprise/coding/desktop/web labels do not establish natural prevalence or professional harm; a memory substrate may expose different write/retrieval opportunities; attack success can conflate storage, retrieval, adoption, answer-text agreement, attempted action, and realized effect; and a write-time-defense comparison may change the information or utility envelope. Mechanistic influence scores require independent validation before they support causal localization. The early dataset timestamp, missing paper link, sparse card, and absent visible implementation/results further require release reconciliation.

This is a cross-domain memory-governance and observer-composition case, not a proposal to narrow `skill-bench` to security or adopt an attack benchmark.

## Charter decision filter and queue action

- **Objectives advanced:** A (context/memory, safety, benchmark validity, and diagnostic evaluation), B (authority-to-memory-to-consequence chain), and D/E (cross-source consolidation and decision-relevant learning).
- **Concrete evidence:** immutable-v1 full-paper review plus pinned-release audit of case generation/validation, family and split dependence, memory substrates, write/retrieval/trigger realization, defense treatments, judges, result accounting, and reproducibility with page/file/revision locators.
- **Uncertainty clarified:** whether L2/L3 results identify a structural blind spot in record-level defenses or mainly reflect co-authored synthetic compositions, trigger/oracle coupling, substrate-specific retrieval, and text-level outcome observers.
- **Mode:** narrow expansion. The autonomous queue has one consolidation task and no source/research/review task; one bounded audit restores evidence flow without repeating broad discovery.
- **Duplication/scope check:** surrounding memory and safety links are reviewed, but the released composition/trigger case graph is distinct. Reuse existing memory-lifecycle, authority, information-flow, observer, consequence, task-health, and configured-system machinery; add no MemPoison-specific schema or pilot absent stronger evidence.
- **Useful completion:** reconcile paper and dataset versions; audit all declared denominators and family/split structure; distinguish write admission, persistence, retrieval, composition, trigger, adoption, attempted/realized effect, harm, recovery, and benign utility; reproduce or decisively bound reported tables where artifacts permit; and preserve blocked prevalence, causal-mechanism, professional-safety, and readiness claims.

Added one task: `review-mempoison-compositional-memory-defense-validity` (review, priority 58). No second source was queued.
