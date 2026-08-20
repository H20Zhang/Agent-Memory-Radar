# Agent Memory Radar

*A living research map of memory systems for LLM and multimodal agents.*

Track the latest work on long-term memory, episodic/semantic/procedural memory, retrieval and access, memory evolution, benchmarks, lifecycle cost, provenance, and safety.

[Latest Papers](#latest-papers) · [What’s Changing](#whats-changing) · [Reading Paths](#reading-paths) · [Research Map](#research-map)

> **Field thesis.** Agent memory is best understood as a sequence of control boundaries: `archive / representation → state localization → access / admission → consumer state → update / evolution → governance / cost`. The useful question is not “which memory architecture wins?” but **which stage earns its complexity against the simplest matched alternative**.

Last updated: **2026-08-20** · Follow updates by starring the repository · Related: [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)

## Latest Papers

### [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](papers/2026/2608.17911.md)
`Retrieval & Access` · `episodic` `graph` `structured` · **4/5** · 2026-08-18

**Research take.** A memory edge should not merely be plausible; it should reach evidence the host retriever would otherwise miss. CABLE makes graph construction explicitly **retriever-complementary**.

[Paper](https://arxiv.org/abs/2608.17911) · [Code](https://github.com/TanZheling/CABLE) · [Research note](papers/2026/2608.17911.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Semantic graph links often duplicate the host retriever's direct neighborhood and add construction cost without extending evidence reach.

**Core mechanism.** `direct semantic neighborhood + antecedent-query candidates → subtract overlap → verify complementary candidates → directed links`; at query time `host seeds → one-hop expansion → novelty filter → fixed-size evidence set`.

**Compared with.** The same A-MEM host retrieval and final evidence-count budget, plus SimpleMem and Mem0g integrations.

**Evidence to remember.** A-MEM LoCoMo Qwen3.5 **71.23→74.81**; MA-LongMemEval Qwen **59.33→65.33**. Negative result: temporal-reasoning slices fall **1.33/2.67 points** in the reported Qwen/GPT settings.

**Open question.** Does write-time complementary linking still beat strong online search when total lifecycle cost and acting-agent side effects are matched?

</details>

### [D²ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](papers/2026/2608.17756.md)
`Evaluation & Analysis` · `structured` `general-agent` · **4/5** · 2026-08-18

**Research take.** Memory changes should be **promoted by paired, traceable evidence**, not by an aggregate score. D²ACCI makes protected slices, stage traces, and accept/feature-flag/reject gates explicit.

[Paper](https://arxiv.org/abs/2608.17756) · [Research note](papers/2026/2608.17756.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** End-to-end memory scores rarely identify which pipeline stage caused a gain or whether protected slices silently regress.

**Core mechanism.** `typed stage traces → paired baseline/candidate artifacts → significance + protected slices + DCR → accept | monitor | feature-flag | reject`.

**Compared with.** Result-only evaluation and five paired memory interventions.

**Evidence to remember.** Supplement extraction **+2.71pp (p=.0009)**, session retrieval **+3.67pp (p=.0026)**, Forget Guard **+1.92pp (p=.0030)**; BM25/RRF is statistically null and remains feature-flagged. Trace-rich root-cause agreement rises to **κ=.571/.619 vs .258/.272** result-only.

**Open question.** Does this promotion discipline transfer across memory stacks and predict deployment utility beyond benchmark diagnostics?

</details>

### [Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback](papers/2026/2608.17587.md)
`Memory Learning & Evolution` · `procedural` `text` · **4/5** · 2026-08-18

**Research take.** WER trains the **skill writer from execution consequences**: candidate skills are run by a frozen agent, verified, and converted into RL/refinement states rather than judged only as text.

[Paper](https://arxiv.org/abs/2608.17587) · [Code](https://github.com/littlepkk/WER4skill-optimizer-training) · [Research note](papers/2026/2608.17587.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Inference-time self-refinement can repair one skill without teaching the model how to write a better next skill from execution evidence.

**Core mechanism.** `candidate skill → frozen executions → programmatic verifier → group-relative RL → mixed success/failure records → next refinement state`.

**Compared with.** The same Qwen3-4B optimizer backbone under the same refinement workflow but without optimizer training.

**Evidence to remember.** BFCL v4 **67.28→76.63 (+9.35)** trained vs untrained optimizer; tau2 **40.43→50.72 (+10.29)**. One extra refinement step regresses **76.63→75.33**.

**Open question.** Can execution-grounded skill-writer training work where reliable verifiers and cheap rollouts are unavailable?

</details>

### [TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation](papers/2026/2608.17588.md)
`Memory Learning & Evolution` · `procedural` `structured` · **4/5** · 2026-08-18

**Research take.** TRUSS makes a generated skill an artifact that must be **certified by both static obligations and controlled execution** before becoming reusable procedural state.

[Paper](https://arxiv.org/abs/2608.17588) · [Research note](papers/2026/2608.17588.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Skill text can look safe/correct while inducing unsafe tool actions or side effects that artifact inspection never observes.

**Core mechanism.** `generate → static function/safety gate → shadow execution with brokered tools → provenance trace → function/safety record → refine → re-check → promote`.

**Compared with.** LLM checking, static checking alone, and no-skill/intermediate-generation conditions.

**Evidence to remember.** SkillInject detection moves from LLM checker **44.64% precision / 19.05% recall** to static **81.55/94.05** to full TRUSS **100/100**. SkillGenBench effectiveness **17.11→52.94%** and security **50.80→100%**, but the final delta bundles several stages.

**Open question.** Which safety properties and execution environments are sufficient before a skill can be trusted across different target agents?

</details>

### [ArborMem: Navigating Interaction States with Memory Forests](papers/2026/2608.17534.md)
`Retrieval & Access` · `episodic` `hierarchical` `timeline` · **4/5** · 2026-08-18

**Research take.** ArborMem separates **state localization from evidence retrieval**: first decide which historical interaction state the user resumed, restore that branch, then fetch supplemental evidence.

[Paper](https://arxiv.org/abs/2608.17534) · [Research note](papers/2026/2608.17534.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Interleaved projects and backjumps make topically relevant history state-incompatible; ordinary retrieval does not first identify which trajectory is active.

**Core mechanism.** `new turn → localize parent state → restore branch-local trajectory → retrieve cross-branch facts/records → answer → commit new state`.

**Compared with.** LongMemEval/LoCoMo/BEAM/BranchMemEval baselines plus a fixed-subset state-localization ablation.

**Evidence to remember.** Gains over the strongest compared baseline: **+9 LongMemEval, +10.31 LoCoMo, +3.36 BEAM100K, +5 BranchMemEval**. Removing localization drops the 30B subset **82→70**, but only **48→46** for 4B; atomic-fact retrieval is also load-bearing.

**Open question.** Can branch-state localization remain stable when turns are genuinely multi-intent and routing errors become persistent structure?

</details>

### [Explicit State Elicitation Is Not Enough: A Controlled Audit of Memory-Policy Classification](papers/2026/2608.17247.md)
`Evaluation & Analysis` · `semantic` `structured` `personalization` · **3/5** · 2026-08-18

**Research take.** A readable intermediate memory-state label is not automatically a useful state variable. On matched counterfactuals, taxonomy instructions help; forcing explicit state output does not significantly improve policy accuracy.

[Paper](https://arxiv.org/abs/2608.17247) · [Research note](papers/2026/2608.17247.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Structured intermediate labels can be correlated with final policy while adding no causal reasoning benefit.

**Core mechanism.** Audit shortcuts → build **40 matched four-way families / 160 examples** → compare clean, taxonomy-only, explicit-state, forced-label, and semantic-evidence conditions.

**Compared with.** Taxonomy-only prompting is the cleanest control for explicit state-output prompting.

**Evidence to remember.** Llama **44.0 clean → 53.1 taxonomy → 44.6 explicit state**; GPT-OSS **54.8→59.8→58.1**. Llama semantic evidence is **55.8 vs 63.3** policy-only (**−7.5; Holm .0146**).

**Open question.** Does explicit state become useful when the evaluation includes actual responses, tools, and memory mutation rather than classification only?

</details>

### [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](papers/2026/2608.16168.md)
`Representation & Organization` · `semantic` `structured` `timeline` `personalization` · **4/5** · 2026-08-17

**Research take.** The important delta is not another typed store. QUMem treats retrieved history as evidence for **query-conditioned user-state reconstruction**, and that read-side reconstruction is the largest component in its ablation.

[Paper](https://arxiv.org/abs/2608.16168) · [Research note](papers/2026/2608.16168.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Fixed memory boundaries and one-shot retrieval can split coherent events and miss preference evolution/contextual validity.

**Core mechanism.** `history → semantic episodes → typed facts/preferences/insights → information needs → typed multi-query retrieval → user-state inference → action`.

**Compared with.** A-MEM, Mem0, Zep, plus ablations removing episode construction, typed decomposition, or user-state reconstruction.

**Evidence to remember.** PersonaMem GPT-4o-mini **61.02 vs 52.99** strongest baseline; ablation **61.02 full → 58.38 w/o episodes → 57.11 w/o decomposition → 54.51 w/o reconstruction**. KnowU-Bench success **17.4% vs 12.8%**.

**Open question.** Does explicit reconstruction still win when retrieved evidence and synthesis budget are matched against a simpler provenance-aware alternative?

</details>

### [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](papers/2026/2608.16114.md)
`Memory Learning & Evolution` · `procedural` `structured` `graph` · **4/5** · 2026-08-17

**Research take.** HyperSkill makes trajectory relations operational in **dual-path retrieval, cross-trajectory skill ranking, and maintenance**; the caveat is that its no-hypergraph ablation also changes the access pipeline.

[Paper](https://arxiv.org/abs/2608.16114) · [Research note](papers/2026/2608.16114.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Flat trajectory/skill stores lose higher-order relations among subtasks, reusable skills, and outcomes.

**Core mechanism.** `task → subtask + trajectory retrieval → fuse trajectory hyperedges → co-occurrence-ranked skills → execute → extract/update → prune/merge`.

**Compared with.** No Memory, experiential-memory baselines including PlugMem, and an internal flat-skill structural-pipeline ablation.

**Evidence to remember.** Qwen3 success **52.00 / 36.97 / 50.59** on xBench / GAIA / WebWalkerQA; **w/o hypergraph 41.00 / 35.76 / 44.71**.

**Open question.** Does a hypergraph still win when a flat/binary store receives the same decomposition, dual-path controller, ranking, and maintenance budget?

</details>

### [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Skill Retrieval](papers/2026/2608.16071.md)
`Retrieval & Access` · `procedural` `structured` `text` · **3/5** · 2026-08-17

**Research take.** Procedural-memory relevance should align with **capability + parameter structure**, not just the outer skill document. Retrieval gains are real, but online query expansion is inconsistent.

[Paper](https://arxiv.org/abs/2608.16071) · [Code](https://github.com/MatZaharia/Skill2Query) · [Research note](papers/2026/2608.16071.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** User goals and developer-facing skill documents describe the same capability from different perspectives.

**Core mechanism.** `skill → capability/parameter/example graph → structured pseudo-queries → offline augmentation / online expansion / retriever training`.

**Compared with.** Zero-shot, Few-shot, SkillFlow-style generation and BM25/dense/SkillRouter retrieval.

**Evidence to remember.** ToolQA offline SkillRouter R@1 **35.80→47.34%**; removing the skill graph drops Exec-Pass **42.85→22.63%**. Online expansion helps some settings and hurts others.

**Open question.** Does capability-grounded retrieval improve long-horizon execution once retrieval, invocation, and skill utility are separated?

</details>

### [FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue](papers/2026/2608.16303.md)
`Write, Update & Consolidation` · `episodic` `structured` `timeline` `personalization` · **3/5** · 2026-08-17

**Research take.** Memory-unit granularity is workload-dependent. Situation-level units beat coarse sessions on sparse dialogue and cost less than turn-pair memory, but turn-pair is slightly more accurate on denser LoCoMo.

[Paper](https://arxiv.org/abs/2608.16303) · [Research note](papers/2026/2608.16303.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Sparse long-term dialogue makes session memory too coarse and turn-pair memory redundant/expensive.

**Core mechanism.** `dialogue → situation windows → Fact-Time-Affect units → carry/fuse boundary evidence → temporal links → structured context`.

**Compared with.** Session-level and turn-pair construction controls plus dialogue-memory systems.

**Evidence to remember.** ES-MemEval: session **31.76 F1 / 1.58M tokens**, turn-pair **37.06 / 6.40M**, FTA-Mem **38.71 / 4.99M**. On LoCoMo, turn-pair **38.28 vs 37.35 F1** but **7.04M vs 3.39M** construction tokens.

**Open question.** Can a writer adapt memory-unit granularity online as evidence density changes?

</details>

## What’s Changing

The useful unit here is a **design-space shift**, not a paper count.

| Current shift | New evidence | Research implication |
|---|---|---|
| **The read path is decomposing before and after retrieval.** | ArborMem + CABLE + ReFind/RippleMem | Evaluate `state localization → direct retrieval → complementary evidence expansion` separately; “retrieval quality” is now too coarse a causal unit. |
| **Intermediate state needs causal evidence, not interpretability alone.** | D²ACCI + Explicit State Elicitation + Demystifying Agent Skills | Promotion should depend on matched downstream effects and traceable stages; readable labels/representations are not mechanisms by themselves. |
| **Procedural evolution is becoming execution-grounded.** | WER + TRUSS + SkillEvo | Train or certify persistent skills from consequences of execution, while separating writer learning, runtime checking, refinement, and governance. |
| **Consumer state and lifecycle cost remain distinct boundaries.** | QUMem + QCR + FTA-Mem + Total Recall | Retrieved records, actor-facing state, construction cost, and serving cost belong to different accounting stages. |

### Current compactions

| Horizon | Current synthesis | What to take away |
|---|---|---|
| **Weekly** | [2026-W33](digests/weekly/2026-W33.md) · [2026-W32](digests/weekly/2026-W32.md) | Closed weeks preserve earlier local shifts; W34 remains open. |
| **Monthly** | [2026-08 · rolling through Aug 20](digests/monthly/2026-08.md) | August now adds state localization, retriever-complementary expansion, promotion protocols, and execution-grounded skill optimization/certification. |
| **Yearly** | [2026 · rolling, incomplete](digests/yearly/2026.md) | Current coverage supports a multi-stage state-interface view, but it is not a full-year reconstruction. |

[Browse all research compactions →](digests/README.md)

## Reading Paths

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **How the read path decomposes beyond top-k** | [ReFind](papers/2026/2608.12888.md) → [ArborMem](papers/2026/2608.17534.md) → [CABLE](papers/2026/2608.17911.md) → [RippleMem](papers/2026/2608.13334.md) | Raw-state search is the control; active-state localization can precede retrieval; complementary structure should extend reach; recollection can continue after first-hop evidence. |
| **Why retrieved evidence is not automatically usable state** | [QUMem](papers/2026/2608.16168.md) → [QCR](papers/2026/2608.12847.md) → [Explicit State Elicitation](papers/2026/2608.17247.md) | Reconstruction/rebinding can help, but an explicit intermediate state must be causally validated rather than credited because it is interpretable. |
| **How procedural memory becomes executable adaptive state** | [SkillEvo](papers/2026/2608.13120.md) → [WER](papers/2026/2608.17587.md) → [TRUSS](papers/2026/2608.17588.md) → [ERSkill](papers/2026/2608.12720.md) | Feedback can drive artifact edits, train the writer, certify runtime behavior, or evolve the read policy; these are different adaptive-state locations. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**ReFind** raises the baseline: complex memory must beat a competent raw-state access interface.

**QUMem** shows the next boundary: retrieving evidence is not the same as reconstructing the state an actor should consume.

**D²ACCI** supplies the evaluation discipline: promote a memory mechanism only when paired evidence localizes the benefit and protects against regression.

Together they turn “which memory architecture wins?” into **which stage changed, compared with what, and what evidence isolates it?**

</details>

## Research Map

`archive / representation → state localization → access / admission → consumer state → update / evolution → governance / cost / provenance`

### Key Anchors

These are **design points, not a ranking**. The set changes slowly.

| Boundary | Work | Why it is useful |
|---|---|---|
| Lifecycle contract | **[LeanMem](papers/2026/2608.03463.md)** | Different evidence types need different persistence/update semantics. |
| Cross-modal access | **[V-Mem](papers/2026/2608.01543.md)** | Same-round identity is an access operator when similarity cannot bridge modalities. |
| Raw-state control | **[ReFind](papers/2026/2608.12888.md)** | Raw archival state + stateful query-time search is the control for semantic preprocessing. |
| Consumer state | **[QCR](papers/2026/2608.12847.md)** | Correctly retrieved history may still require target-conditioned rebinding. |
| Controller coupling | **[PMCoder](papers/2026/2608.06811.md)** | Retrieval and controller state can influence one another bidirectionally. |
| Learned utility state | **[RoMeRL](papers/2026/2608.02508.md)** | Sparse feedback can be concentrated in bounded semantic utility state. |
| Authority | **[AuthMem-Bench](papers/2026/2608.01679.md)** | Semantically correct memory can still be wrong when source authority is lost. |
| Descendant revocation | **[SkillJack](papers/2026/2608.03509.md)** | Provenance must survive experience → skill transformation and deletion. |

<details>
<summary><strong>How the anchor set is being challenged</strong></summary>

**ArborMem** proposes state localization as an earlier access boundary; **CABLE** makes retriever-complementary reachability explicit; **QUMem** strengthens post-retrieval consumer-state reconstruction; **D²ACCI** may become an evaluation-discipline anchor if its promotion protocol transfers across stacks; **WER/TRUSS** move procedural evolution toward execution-grounded writer training and certification. None yet requires expanding the bounded anchor set.

[See the full anchor notes →](papers/anchors.md)

</details>

### Research Problems

| Research problem | Core question | Current claim |
|---|---|---|
| **[Representation & Organization](categories/representation-organization.md)** | What should persist, and what should reach the current consumer? | Archival evidence and actor-facing state are different objects. |
| **[Retrieval & Access](categories/retrieval-access.md)** | Which historical state is active, what evidence is reachable, and when should memory be withheld? | State localization, direct retrieval, expansion, and admission are separable controls. |
| **[Write, Update & Consolidation](categories/write-update-consolidation.md)** | What persistent unit should be written, preserved, corrected, or forgotten? | Granularity, preservation contract, and transformation frequency are separate controls. |
| **[Memory Learning & Evolution](categories/memory-learning-evolution.md)** | What adaptive state should evolve, and from which feedback? | Writer policy, artifact state, read policy, structural relations, and governance should not be conflated. |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | What makes memory worth deploying? | Endpoint quality is insufficient; promotion needs causal attribution, lifecycle cost, trust, and non-regression evidence. |

<details>
<summary><strong>Retrieval & Access — what exactly happens before evidence reaches the model?</strong></summary>

**Current evidence.** ReFind is the raw-state anchor; ArborMem, CABLE, RippleMem, TRACE-Memory, Skill2Query, MESA, and MAP-Graph expose different read operators.

**Strongest signal.** “Retrieval” is splitting into **state localization → seed retrieval → evidence completion/expansion → admission**. CABLE further says stored links should be complementary to the host retriever rather than duplicate it.

**Biggest unresolved question.** Which of these operators should be precomputed versus reconstructed online once total write + query cost and error propagation are matched?

**Next decisive evidence.** Same raw archive/model/task with state localization, raw search, complementary linking, recollection, and admission toggled independently under one end-to-end budget.

</details>

<details>
<summary><strong>Representation & Organization — archive faithfully, or optimize for the consumer?</strong></summary>

**Current evidence.** LeanMem and QCR as anchors; QUMem is the strongest current challenger.

**Strongest signal.** The archival object and actor-facing state need not be identical; reconstruction/rebinding can dominate another storage schema.

**Biggest unresolved question.** Which transforms preserve provenance/fidelity under preference drift, binding shift, and conflicting memories?

**Next decisive evidence.** Hold retrieval fixed and compare raw evidence, source summaries, target-conditioned support, and reconstructed state under matched synthesis cost.

</details>

<details>
<summary><strong>Write, Update & Consolidation — what should one persistent unit be?</strong></summary>

**Current evidence.** LeanMem, LycheeMemory V2, FTA-Mem, Scrub Jay, and Sleeping Agent.

**Strongest signal.** Boundary/granularity, transformation frequency, field preservation, and forgetting are separate decisions; the preferred granularity can flip with evidence density.

**Biggest unresolved question.** Can a streaming controller adapt granularity and preservation contracts without one expensive LLM decision per turn?

**Next decisive evidence.** Sparse+dense acting-agent streams with controlled write budgets, conflicts, temporal drift, preservation metrics, and downstream action quality.

</details>

<details>
<summary><strong>Memory Learning & Evolution — what exactly should evolve?</strong></summary>

**Current evidence.** RoMeRL as an anchor; SkillEvo, WER, TRUSS, ERSkill, HyperSkill, AMD, MemoryCPT, and HyMeS place adaptive state at different layers.

**Strongest signal.** Execution feedback can update the artifact, train the writer, certify a candidate, or evolve the read policy. Treating all four as “self-improving memory” hides the real state transition.

**Biggest unresolved question.** Which adaptive-state location transfers across consumers/domains strongly enough to justify rollout, verification, and maintenance cost?

**Next decisive evidence.** Freeze experience/task distribution and independently vary feedback, writer learning, artifact refinement, read-policy evolution, certification, and governance under matched cost.

</details>

<details>
<summary><strong>Evaluation & Analysis — when has a memory mechanism actually earned promotion?</strong></summary>

**Current evidence.** AuthMem-Bench/SkillJack are trust anchors; D²ACCI, Explicit State Elicitation, Demystifying Agent Skills, Total Recall, and Practice Makes Unsafe expose causal and lifecycle blind spots.

**Strongest signal.** Intermediate labels, retrieval scores, and endpoint success can all be non-causal or incomplete. D²ACCI adds an explicit promotion contract based on paired effects, protected slices, and localizable traces.

**Biggest unresolved question.** Can one deployment-facing evidence vector connect causal stage attribution to real user utility, cost, authorization, and long-lived descendant effects?

**Next decisive evidence.** Long-running acting-agent deployments with paired interventions, stage traces, protected slices, full offline+online cost, and revocation outcomes.

</details>

[Explore the full research-problem map →](categories/README.md)

## How to Use This Radar

- **Scan:** title, category, importance, date, and **Research take** decide whether a paper deserves attention.
- **Compare:** expand the 60-second view for mechanism, closest control, decisive evidence, and the question most likely to change the importance judgment.
- **Deep dive:** paper notes expose the memory lifecycle, causal comparison, evidence, caveat, and related reading.
- **Build a mental model:** use [Reading Paths](#reading-paths) for sequence, [Research Map](#research-map) for design space, and [What’s Changing](#whats-changing) for temporal movement.

## What Counts as Agent Memory?

A work is included when **information persists or is explicitly managed across interaction/reasoning steps and materially changes a language or multimodal agent’s future behavior**.

Typical in-scope work changes at least one lifecycle boundary: what gets written, how memory is organized, how active state/evidence is located, how memory is retrieved/admitted, how it is transformed for the current consumer, how it is updated/forgotten/evolved, or how persistent state is evaluated for cost, authority, safety, and downstream effect.

Usually out of scope: ordinary fixed RAG with no persistent memory contribution, generic long-context modeling, KV-cache optimization, or unrelated continual learning. Work at the retrieval/memory boundary may also appear in [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) when adaptive information acquisition is itself the research contribution.

## About the Radar

This is a **curated research map, not an exhaustive keyword feed**. Every strong entry should answer:

1. **What memory boundary actually changed?**
2. **Compared with what — especially the simplest matched alternative?**
3. **Does the evidence isolate that stage rather than crediting the whole architecture?**

Negative results and baseline reversals stay when they change the interpretation. Relevance and importance are scored separately.

Research notes, digests, category maps, canonical paper data, and original radar figures are available under **CC BY 4.0**; maintenance code is under **MIT**. See [LICENSE.md](LICENSE.md) and [CITATION.cff](CITATION.cff).

## Contributing

The most valuable contributions change a research conclusion: a missing paper, stronger baseline, wrong taxonomy/importance, incorrect benchmark number, unsupported mechanism claim, broken provenance, or misleading visual.

[Suggest a paper](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [Report a correction](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [Contribution guide](CONTRIBUTING.md)

<details>
<summary><strong>Methodology & maintenance</strong></summary>

See the [maintainer guide](docs/MAINTENANCE.md), [curation protocol](CURATION.md), [compaction protocol](COMPACTION.md), [visual grounding rules](VISUAL_POLICY.md), [taxonomy](taxonomy.yaml), and [structured paper records](data/papers/).

</details>
