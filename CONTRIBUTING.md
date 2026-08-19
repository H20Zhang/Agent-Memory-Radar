# Contributing

Agent Memory Radar is a curated research map, not an exhaustive paper feed. Contributions are most useful when they improve a **research conclusion**, expose a stronger comparison, or repair evidence/provenance — not when they only increase paper count.

## What belongs in the radar

A paper is in scope when both are true:

1. **Persistent or managed memory is substantive** — information survives across interaction/reasoning steps or is explicitly written, transformed, retrieved, updated, forgotten, or evolved.
2. **That memory materially changes future agent behavior** — for a language or multimodal agent, not merely an offline storage/indexing benchmark with no agent-memory implication.

Typical in-scope questions include long-term episodic/semantic memory, procedural/skill memory, structured memory, multimodal memory, memory retrieval/access, consolidation/forgetting/conflict repair, memory-policy learning/evolution, provenance/authority/safety, and lifecycle cost.

Usually out of scope:

- ordinary fixed RAG where no persistent memory mechanism is studied;
- generic long-context modeling or prompt compression with no memory-system question;
- KV-cache / serving-state optimization unrelated to agent memory semantics;
- unrelated continual learning or fine-tuning;
- promotional submissions whose central evidence cannot be checked.

## Suggest a paper

[**Suggest an Agent Memory paper →**](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml)

The most useful suggestions identify:

- the smallest research delta that makes the paper worth adding;
- which memory lifecycle boundary changes (`write / organize / read / update-forget / learning-evolution / evaluation`);
- the closest baseline or design predecessor;
- the strongest evidence or ablation;
- negative results, unmatched budgets, missing baselines, or other causal confounders.

A positive headline result is not required. Strong negative controls and careful analyses are valuable when they change how prior memory work should be interpreted.

## Suggest a correction

[**Report a research correction →**](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml)

Use it when you find something that could change a reader’s conclusion, including:

- wrong taxonomy or importance framing;
- duplicate/canonical paper-version errors;
- broken paper/code/project links;
- incorrect benchmark numbers or unsupported method descriptions;
- a missing stronger baseline or simpler matched alternative;
- lifecycle-cost accounting that excludes important write/read/update work;
- a visual that implies a mechanism, causal edge, or result the evidence does not establish.

Please link a primary source when possible and distinguish verified facts from your interpretation.

## Evidence standard

The radar keeps **relevance separate from importance** and asks three questions for every strong claim:

1. **What memory boundary actually changed?**
2. **Compared with what — especially the simplest matched alternative?**
3. **Does the evidence isolate that stage rather than crediting the whole architecture?**

We prefer full-paper evidence, matched comparisons, component ablations, negative controls, and lifecycle cost accounting. If a gain may instead come from a richer representation, better retrieval interface, larger context/budget, stronger base model, different training distribution, or another confound, preserve that alternative explanation.

## Pull requests

Small, auditable pull requests are welcome for factual corrections, broken links, taxonomy fixes, documentation improvements, and validation/tooling changes. For a new paper, an issue suggestion is usually the fastest path because accepted papers require full-paper review and synchronized canonical JSON + research note + category/README updates.

Before submitting code changes, run:

```bash
pip install -r requirements.txt
python scripts/validate.py
```

## Licensing of contributions

By contributing, you agree that:

- research notes, category maps, compactions, canonical paper data, and original radar visuals are contributed under **CC BY 4.0**;
- maintenance code under `scripts/` and `.github/workflows/` is contributed under the **MIT License**.

See [`LICENSE.md`](LICENSE.md) for scope details.

Thanks for helping keep the map useful, evidence-grounded, and research-first.