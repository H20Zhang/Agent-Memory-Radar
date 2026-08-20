# Agent Memory Research Problems

[中文](README.md) | **English** · [Home](../README.en.md) · [Reading Paths](../README.en.md#reading-paths)

The taxonomy is organized by **which memory lifecycle boundary changes**, not by application domain. Use this page to move from papers to research questions.

| Research problem | Core question | Current claim |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What should persist, and what should reach the current consumer? | **QUMem + QCR:** archival evidence and actor-facing state are different objects; reconstruction/rebinding can matter more than another storage schema. |
| [Retrieval & Access](retrieval-access.md) | When should memory stay raw, become structured, or be withheld? | **ReFind + RippleMem + TRACE-Memory:** strong raw-state controls are mandatory; structure earns cost through stronger operators or admission, not by being structured. |
| [Write, Update & Consolidation](write-update-consolidation.md) | What persistent unit should be written, preserved, corrected, or forgotten? | **LycheeMemory V2 + FTA-Mem + Sleeping Agent:** granularity, transformation frequency, preservation contract, and forgetting are separate controls. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | What adaptive state should evolve, and from which feedback? | **SkillEvo + ERSkill + HyperSkill:** feedback source, read-policy evolution, representation, and maintenance should be attributed separately. |
| [Evaluation & Analysis](evaluation-analysis.md) | What makes memory worth deploying? | **Demystifying Agent Skills + Total Recall + Practice Makes Unsafe:** retrieval quality alone misses behavioral utility, lifecycle cost, authority, and descendant effects. |

## Cross-cutting model

`archive / representation → access / admission → consumer state → update / evolution → governance / cost / provenance`

The strongest current correction is **stage attribution**. **ReFind** says semantic preprocessing must beat a competent raw-record interface; **RippleMem** shows structure can still be justified when it enables a stronger read operator. **TRACE-Memory** adds admission: relevant evidence can still be unnecessary. **QUMem** and **QCR** move the next boundary downstream: selected evidence is not necessarily the state an actor should consume. On the write side, **LycheeMemory V2** and **FTA-Mem** show that event-boundary choice is a measurable quality-cost parameter rather than a universal constant.

## Researcher checklist

When comparing two memory systems, ask what was actually held fixed:

1. **Representation:** same raw evidence and preservation fidelity?
2. **Access:** same query interface, candidate/evidence budget, and iteration?
3. **Consumer state:** same retrieved evidence but different reconstruction/rebinding?
4. **Update:** same feedback, write budget, and maintenance frequency?
5. **Lifecycle:** same construction + serving cost, provenance, authority, and revocation semantics?

If several stages move together, the result supports the package more strongly than any one mechanism.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive research problems.
