# Agent Memory Research Problems

[中文](README.md) | **English** · [Home](../README.en.md) · [Research Library](../library/README.en.md)

Organize the field by **memory lifecycle boundary**, not by method name or application domain.

`archive → write → organize → state localization → access/admission → consumer state → update/evolution → governance/cost/provenance`

| Research problem | Core question | Current view |
|---|---|---|
| **Representation & Organization** | What should persist, and what should reach the consumer? | **QUMem / QCR:** archival evidence and actor-facing state are different objects; post-retrieval reconstruction/rebinding can matter more than another storage schema. |
| **Retrieval & Access** | When is raw search enough, and when do structure or state localization earn their cost? | **ReFind → CABLE → ArborMem:** raise the raw baseline, require structure to change reachability, and recognize that some workloads need active-state localization before retrieval. |
| **Write, Update & Consolidation** | How large should a persistent unit be, what should it preserve, and when should it change or disappear? | Granularity, preservation contract, transformation frequency, and forgetting are separate controls. |
| **Memory Learning & Evolution** | What actually evolves: artifact, writer/read policy, relations, or governance? | **HyperSkill / WER / TRUSS:** relation structure, writer learning, and runtime certification are now distinct research questions. |
| **Evaluation & Analysis** | What evidence is sufficient to deploy a memory feature? | **D²ACCI + Demystifying:** endpoint scores and retrieval labels are insufficient; stage traces, paired controls, protected slices, utility, and lifecycle cost all matter. |

## Cross-cutting correction

The read path is becoming more causally decomposed:

`localize historical state → retrieve/admit evidence → reconstruct consumer state`

ReFind says semantic preprocessing must beat a competent raw interface; CABLE requires graph edges to alter reachability relative to the host retriever; ArborMem moves state localization before retrieval; QUMem moves current-state reconstruction after retrieval.

Future comparisons should therefore ask **which stage changed, which stages were held fixed, and where the extra lifecycle cost was paid**.

## Researcher checklist

1. **Representation:** same raw evidence and preservation fidelity?
2. **State localization / access:** same active-state assumptions, query interface, evidence budget, and iteration?
3. **Consumer state:** same retrieved evidence, different reconstruction/rebinding only?
4. **Evolution:** same feedback, writer/read policy budget, update budget, and governance?
5. **Lifecycle:** same construction + serving cost, provenance, authority, promotion, and revocation semantics?

If several stages move together, the experiment supports the **package** more strongly than any named module.
