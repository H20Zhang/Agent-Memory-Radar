# Agent Memory Research Problems

[Home](../README.md) · [Reading Paths](../README.md#reading-paths) · [What’s Changing](../README.md#whats-changing)

The taxonomy is organized by **which memory lifecycle boundary changes**, not by application domain.

| Research problem | Core question | Current claim |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What should persist, and what should reach the current consumer? | **QUMem + QCR:** archival evidence and actor-facing state are different objects; reconstruction/rebinding can matter more than another storage schema. |
| [Retrieval & Access](retrieval-access.md) | Which historical state is active, what evidence is reachable, and when should memory be withheld? | **ReFind + ArborMem + CABLE + RippleMem:** state localization, direct search, complementary expansion, and recollection are distinct operators; structure must extend reach rather than duplicate the host interface. |
| [Write, Update & Consolidation](write-update-consolidation.md) | What persistent unit should be written, preserved, corrected, or forgotten? | **LycheeMemory V2 + FTA-Mem + Sleeping Agent:** granularity, transformation frequency, preservation contract, and forgetting are separate controls. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | What adaptive state should evolve, and from what feedback? | **SkillEvo + WER + TRUSS + ERSkill:** artifact edits, writer learning, runtime certification, and read-policy evolution are different state transitions. |
| [Evaluation & Analysis](evaluation-analysis.md) | What makes memory worth deploying? | **D²ACCI + Explicit State Elicitation + Demystifying:** endpoint success and interpretable state are insufficient; promotion needs paired causal evidence, traceability, and lifecycle accounting. |

## Cross-cutting model

`archive / representation → state localization → access / expansion / admission → consumer state → update / evolution → governance / cost / provenance`

The strongest current correction is **stage attribution at finer granularity**. ReFind says semantic preprocessing must beat competent raw-state search. ArborMem asks which historical state is active before retrieval. CABLE asks whether stored relations reach evidence outside the host retriever's neighborhood. QUMem/QCR show that selected evidence may still need reconstruction/rebinding. D²ACCI then asks whether any claimed improvement is statistically paired, protected against slice regressions, and localizable in traces.

## Researcher checklist

When comparing two memory systems, ask what was actually held fixed:

1. **Representation / state:** same raw evidence, persistence semantics, and active-state assumptions?
2. **Access:** same interface, candidate/evidence budget, iteration, expansion, and admission policy?
3. **Consumer state:** same retrieved evidence but different reconstruction/rebinding?
4. **Update / evolution:** same feedback, executor, write budget, maintenance, and promotion rule?
5. **Lifecycle:** same construction + serving cost, provenance, authority, safety, and revocation semantics?

If several stages move together, the result supports the package more strongly than any one mechanism.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive research problems.
