# Representation & Organization

[Research Map](../README.md#research-map) · [All research problems](README.md) · [Reading Paths](../README.md#reading-paths)

How agent memory is represented, structured, and transformed for the current consumer.

## Current argument

**Agent Zero Memory** adds a provenance/admission boundary to representation: the same history is exposed as timeline, graph, and documentary views, while citation lock restricts the final answer to evidence actually opened. Its cleanest ablation isolates hybrid retrieval rather than the three-store organization, so architecture attribution still needs matched store/provenance interventions and full build/maintenance cost.

Representation now has **three separable stages**: archive organization, state localization, and actor-facing reconstruction. **SCALE-QA / TSIM** shows that a flat interleaved turn stream may first need to be reconstructed into coherent episodes before ordinary retrieval can work reliably. **QCR** and **QUMem** then show that even selected evidence can still be the wrong representation for the acting consumer: source trajectories or typed historical facts may need target-conditioned rebinding/state reconstruction. **VoiceMem** adds a streaming multimodal boundary: factual/entity state and affect/persona state can require different paths, while the upper organization/routing layer may stay portable across backends. Structure earns its cost only when a downstream operation can exploit it under matched construction and query budgets.

| Date | Paper | Tags | Importance | Research take |
|---|---|---|---:|---|
| 2026-08-30 | [Agent Zero Memory](../papers/2026/2608.29606.md) | `episodic` `semantic` `structured` `graph` `hierarchical` `timeline` `general-agent` | 4/5 | Provenance-linked parallel views plus citation-locked reading make evidence admission explicit; the matched ablation supports hybrid retrieval, not the causal value of the three-store architecture. |
| 2026-08-26 | [VoiceMem](../papers/2026/2608.26005.md) | `semantic` `structured` `graph` `multimodal` `personalization` | 4/5 | A shared upper organization/routing layer improves several interchangeable backends, but retrieval latency is not end-to-end latency and asynchronous write cost remains incomplete. |
| 2026-08-26 | [SCALE-QA / TSIM](../papers/2026/2608.25655.md) | `episodic` `hierarchical` `text` `general-agent` | 4/5 | Flat interleaved history benefits from episode reconstruction before evidence assembly; segmentation, summaries, hierarchy, and routing remain package-confounded. |
| 2026-08-17 | [QUMem](../papers/2026/2608.16168.md) | `semantic` `structured` `timeline` `personalization` | 4/5 | The biggest ablation effect comes after storage/retrieval: query-conditioned user-state reconstruction turns distributed historical evidence into currently applicable state. |
| 2026-08-13 | [Beyond Retrieval / QCR](../papers/2026/2608.12847.md) | `procedural` `text` `web-agent` | 4/5 | Same selected trajectory, different delivery: target-bound workflow/rebinding support beats raw trace by 10.7pp while halving online tokens. |
| 2026-08-10 | [Muscle Memory](../papers/2026/2608.08995.md) | `procedural` `structured` `personalization` | 3/5 | Early signal: stable recurring intent may be compiled into executable specialists rather than retrieved as text. |
| 2026-08-06 | [Activity Frames](../papers/2026/2608.05784.md) | `episodic` `structured` `timeline` | 3/5 | Deterministic compilation is a credible alternative to LLM-based construction for high-volume personal activity memory. |
| 2026-08-04 | [LeanMem](../papers/2026/2608.03463.md) | `episodic` `semantic` `structured` | 4/5 | Heterogeneous lifecycle semantics: profile, evolving event, and source-grounded evidence should not share one storage contract. |
| 2026-08-03 | [PGMem](../papers/2026/2608.01708.md) | `episodic` `semantic` `graph` `personalization` | 3/5 | Persona representation is load-bearing; graph expansion matters more mainly at longer context. |

**Biggest unresolved question:** when should the system preserve full-fidelity archival state, reconstruct coherent episodes, and synthesize a smaller consumer state—and how can multimodal/factual/affective paths do so without hallucinating current state, dropping provenance, or shifting lifecycle cost off the critical path?

**Next decisive evidence:** freeze the source stream, retrieved evidence, consumer, and synthesis budget; independently vary episode segmentation/localization, raw versus target-conditioned reconstruction, factual-versus-affective organization, and backend choice under conflict, drift, interleaving, streaming latency, and full write/query maintenance cost.

**Continue:** [Retrieval & Access →](retrieval-access.md)