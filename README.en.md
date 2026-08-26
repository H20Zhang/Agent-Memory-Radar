# Agent Memory Radar

[中文](README.md) | **English**

*A research map of long-term memory systems for LLM and multimodal agents.*

**Radar Family:** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 sec: Timeline](#timeline) · [3 min: 7/30-day changes](#periods) · [5 min: Field Map](#field-map) · [15 min: Reading Paths](#reading-paths) · [Browse all](#library)

Last updated: **2026-08-26**

<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>
## Latest Timeline

> **Migration notice.** These existing records lack reliable historical Radar acceptance timestamps, so they remain ordered by their original paper publication dates. Every post-v2-cutover record uses `radar_published_at`; a paper date must never be presented as a Radar acceptance time.

<a id="entry-2608-23471"></a>
<details><summary><strong>2026-08-26 · InjecMEM</strong> · Single-Interaction Memory Injection <!-- timefirst:area=single-interaction-memory-injection --> — One ordinary write can be retrieved later and steer a related response. <!-- timefirst:delta=ordinary-write-to-later-consumer-steering --></summary>

**Question.** Can an attacker without store access persist influence through one ordinary interaction? <!-- timefirst:question=test-single-interaction-persistent-steering -->

**Evidence.** MemoryOS reaches **46.5% retrieval**, **76.6% conditional steering**, and `35.6% joint end to end success`; MemGPT reaches **18.1%** jointly. <!-- timefirst:evidence=write-retrieval-and-consumer-influence-are-jointly-observed~joint-end-to-end-success -->

**Caveat.** The strongest attack is white-box, needs near-verbatim storage, fails zero-shot across a held-out model family, and `attacker optimization cost is unreported`. <!-- timefirst:caveat=white-box-near-verbatim-and-incomplete-cost~attacker-optimization-cost-is-unreported -->

**Map.** `early_signal` — A single security study does not change the durable map.

**Links.** [Paper](https://arxiv.org/abs/2608.23471) · [中文深读](papers/2026/2608.23471.zh.md) · [English note](papers/2026/2608.23471.md) · [Code](https://github.com/BlueBlood6/InjecMEM)

</details>

<a id="entry-2608-22767"></a>
<details><summary><strong>2026-08-26 · EARM</strong> · Retrieval-Experience Amortization <!-- timefirst:area=retrieval-experience-amortization --> — The access policy persists earlier relevance judgments for later reranking. <!-- timefirst:delta=stateless-reranking-to-persistent-score-history --></summary>

**Question.** Can sparse past relevance scores reduce later reranker calls without losing answer accuracy? <!-- timefirst:question=amortize-reranking-through-persistent-experience -->

**Evidence.** Top-10 accuracy is **82.21 semantic / 88.83 observed-only / 91.62 full**, while `reranker calls fall 307982 to 78736`. <!-- timefirst:evidence=completed-score-history-changes-later-ranking~reranker-calls-fall-307982-to-78736 -->

**Caveat.** The store, candidate set, IDs, and question order are fixed; `matrix maintenance and deletion costs are missing`, and one temporal slice regresses. <!-- timefirst:caveat=fixed-order-store-and-incomplete-lifecycle-cost~matrix-maintenance-and-deletion-costs-are-missing -->

**Map.** `early_signal` — One low-confidence study does not establish a learned-access direction.

**Links.** [Paper](https://arxiv.org/abs/2608.22767) · [中文深读](papers/2026/2608.22767.zh.md) · [English note](papers/2026/2608.22767.md) · [Code](https://github.com/FengQi-HITSZ/earm)

</details>

<a id="entry-2608-22752"></a>
<details><summary><strong>2026-08-26 · The Compaction Cliff</strong> · Constraint-Preserving Compaction <!-- timefirst:area=constraint-preserving-compaction --> — Different memory types receive different distortion contracts. <!-- timefirst:delta=uniform-summary-to-typed-preservation-contract --></summary>

**Question.** Can compaction retain exact constraints across repeated compression and still improve later behavior? <!-- timefirst:question=preserve-constraints-through-repeated-compaction -->

**Evidence.** Five 50% rounds move Sonnet constraint recall **.53→.10**, while TypeCompact remains about **.96**; at 50%, `mars fl nearly ties constraint recall 0.99 versus 1.00`. <!-- timefirst:evidence=typed-retention-preserves-constraints-across-rounds~mars-fl-nearly-ties-constraint-recall-0.99-versus-1.00 -->

**Caveat.** Behavioral controls omit MaRS-FL, tokens are mismatched, classifier κ=.45, and `classification and query scope costs are excluded`. <!-- timefirst:caveat=closest-control-missing-from-behavior-and-upstream-cost-omitted~classification-and-query-scope-costs-are-excluded -->

**Map.** `early_signal` — Typed preservation is a signal, not a durable compaction node.

**Links.** [Paper](https://arxiv.org/abs/2608.22752) · [中文深读](papers/2026/2608.22752.zh.md) · [English note](papers/2026/2608.22752.md) · [Code](https://github.com/searchsim-org/cikm26-knowledge-triage)

</details>

<a id="entry-2608-22533"></a>
<details><summary><strong>2026-08-26 · CONTRAMEM</strong> · Contrastive Procedural Memory <!-- timefirst:area=contrastive-procedural-memory --> — Same-task outcome variation becomes supervision for a curated skill bank. <!-- timefirst:delta=single-success-to-heterogeneous-outcome-contrast --></summary>

**Question.** Does contrasting heterogeneous trajectories build more transferable procedures than self-memory under matched source count? <!-- timefirst:question=separate-contrast-from-success-coverage -->

**Evidence.** Macro success moves **26.2 no-memory→47.2 self-memory→55.3 shared**, and `matched three trajectory construction moves 70.0 to 77.5`. <!-- timefirst:evidence=contrastive-bank-changes-later-tool-success~matched-three-trajectory-construction-moves-70.0-to-77.5 -->

**Caveat.** The bank is frozen at test time, 23 slices regress, broader coverage is an alternative attribution, and `offline construction cost is incomplete`. <!-- timefirst:caveat=offline-package-with-regressions-and-coverage-confound~offline-construction-cost-is-incomplete -->

**Map.** `early_signal` — One offline package does not establish contrastive memory as a trend.

**Links.** [Paper](https://arxiv.org/abs/2608.22533) · [中文深读](papers/2026/2608.22533.zh.md) · [English note](papers/2026/2608.22533.md)

</details>

<a id="entry-2608-22339"></a>
<details><summary><strong>2026-08-26 · BASM</strong> · Skill-Validity Boundaries <!-- timefirst:area=skill-validity-boundaries --> — Applicability and recovery fields gate imitation after retrieval. <!-- timefirst:delta=relevant-procedure-to-state-conditioned-use --></summary>

**Question.** Can explicit skill boundaries suppress an inapplicable procedure before the actor chooses the wrong tool? <!-- timefirst:question=gate-retrieved-skills-by-current-state -->

**Evidence.** Qwen3-8B BFCL is **34.13 Base / 33.88 Procedure / 38.88 BASM**; `boundary knockout recovers 69.4 percent of the wrong tool gap`. <!-- timefirst:evidence=boundary-text-changes-later-tool-choice~boundary-knockout-recovers-69.4-percent-of-the-wrong-tool-gap -->

**Caveat.** The package changes failed-trajectory admission, representation, retrieval, checker, and repair; `agentdojo utility remains below no memory` for Qwen3-8B. <!-- timefirst:caveat=multi-stage-package-and-non-pareto-results~agentdojo-utility-remains-below-no-memory -->

**Map.** `early_signal` — Validity boundaries refine a research question without changing the Field Map.

**Links.** [Paper](https://arxiv.org/abs/2608.22339) · [中文深读](papers/2026/2608.22339.zh.md) · [English note](papers/2026/2608.22339.md)

</details>

<a id="entry-2608-21867"></a>
<details><summary><strong>2026-08-26 · MemGuard</strong> · Persistent Verifier Governance <!-- timefirst:area=persistent-verifier-governance --> — Verifier evidence persists across admission, retrieval, maintenance, and archival. <!-- timefirst:delta=one-shot-filter-to-lifecycle-verifier-state --></summary>

**Question.** Does retaining verifier state beyond admission improve later behavior over a verifier-only filter? <!-- timefirst:question=test-persistent-verifier-state-after-admission -->

**Evidence.** Full MemGuard beats verifier-only means in all 16 cells; Qwen Plus includes **67.4/63.7** and **58.4/52.0**, but `closest contrast has no reported significance test`. <!-- timefirst:evidence=persistent-governance-changes-later-task-means~closest-contrast-has-no-reported-significance-test -->

**Caveat.** Multiple lifecycle operations change together, simplified descriptors nearly match full, and `governance dollars energy privacy deletion are missing`. <!-- timefirst:caveat=bundled-governance-and-incomplete-lifecycle-cost~governance-dollars-energy-privacy-deletion-are-missing -->

**Map.** `early_signal` — Persistent verifier metadata is one signal, not a new durable stage.

**Links.** [Paper](https://arxiv.org/abs/2608.21867) · [中文深读](papers/2026/2608.21867.zh.md) · [English note](papers/2026/2608.21867.md) · [Code](https://github.com/whyyyyy123/MemGuard)

</details>


<a id="entry-2608-21230"></a>
<details><summary><strong>2026-08-25 · Utility Under Attack</strong> · Provenance-Ranking Utility Frontier <!-- timefirst:area=provenance-ranking-utility-frontier --> — Source priors must resist poison without excluding legitimate low-trust evidence. <!-- timefirst:delta=source-trust-to-measured-utility-frontier --></summary>

**Question.** Can additive provenance weights suppress persistent poison while preserving answer-bearing evidence from untrusted channels? <!-- timefirst:question=preserve-useful-evidence-while-suppressing-poison -->

**Evidence.** Poison moves clean accuracy **.850→.300**; shipped weights reach **.317**, while stronger weights recover **.475** but collapse genuine untrusted-evidence recall **99.17%→0%** and accuracy **.8583→.0417**. <!-- timefirst:evidence=ranking-weight-changes-later-answers-and-evidence-recall~genuine-untrusted-evidence-recall -->

**Caveat.** The attack is query-targeted, labels are assumed correct, and `bounded source occupancy is proposed but not tested`; one stack and two weights do not establish a universal provenance failure. <!-- timefirst:caveat=targeted-attack-and-constructed-provenance-extremes~bounded-source-occupancy-is-proposed-but-not-tested -->

**Map.** `early_signal` — Provenance becomes a measurable retrieval-utility frontier, but one implementation does not revise the durable map.

**Links.** [Paper](https://arxiv.org/abs/2608.21230) · [中文深读](papers/2026/2608.21230.zh.md) · [English note](papers/2026/2608.21230.md)

</details>

<a id="entry-2608-20664"></a>
<details><summary><strong>2026-08-25 · DreamBench-SWE</strong> · Executable Memory Hygiene <!-- timefirst:area=executable-memory-hygiene --> — Earlier project state must change a later executable patch before hygiene mechanisms receive credit. <!-- timefirst:delta=memory-score-to-executable-later-behavior --></summary>

**Question.** Does persistent project state change later software behavior, and do typed consolidation and sleep beat a strong verbatim archive? <!-- timefirst:question=test-executable-memory-and-mechanism-attribution -->

**Evidence.** No memory passes **21/180**, verbatim **82/180**, hybrid **83/180**, and literal Mem0 **97/180**; persistent state matters, but `all preregistered hybrid versus verbatim raw typed tests fail to reject`. <!-- timefirst:evidence=earlier-state-changes-executable-patches-with-null-mechanism-tests~all-preregistered-hybrid-versus-verbatim-raw-typed-tests-fail-to-reject -->

**Caveat.** The benchmark is fixture-heavy and mostly exact recall; hybrid consumes **174.205M vs 2.209M tokens** for verbatim, while native external-system mechanism contrasts fail conformance. <!-- timefirst:caveat=authored-recall-fixtures-and-null-mechanism-attribution~hybrid-consumes-174.205m-vs-2.209m-tokens -->

**Map.** `early_signal` — Executable behavior raises the evaluation bar, but the reference package does not earn a durable mechanism claim.

**Links.** [Paper](https://arxiv.org/abs/2608.20664) · [中文深读](papers/2026/2608.20664.zh.md) · [English note](papers/2026/2608.20664.md)

</details>

<a id="entry-2608-20631"></a>
<details><summary><strong>2026-08-25 · Weighted Memory Tree</strong> · Selection-Driven Working Memory <!-- timefirst:area=selection-driven-working-memory --> — A retention policy decides which live execution branches remain active before later actions. <!-- timefirst:delta=linear-history-to-active-retention-control --></summary>

**Question.** Can a task tree select, fold, decay, and suppress working state more effectively than linear execution history? <!-- timefirst:question=select-active-execution-state-before-later-actions -->

**Evidence.** Across three models, the coupled package reports **+9.97pp** average GAIA-Text accuracy and **−32.8%** prompt tokens versus linear history; the stored view changes later within-task actions. <!-- timefirst:evidence=package-improves-gaia-and-reduces-prompt-tokens~coupled-package-reports -->

**Caveat.** Each question starts fresh, components are not isolated, ablations reverse, and `cross session persistence is not evaluated`; no seeds, uncertainty, or artifact are available. <!-- timefirst:caveat=within-task-package-only-and-missing-uncertainty~cross-session-persistence-is-not-evaluated -->

**Map.** `early_signal` — Active retention may precede retrieval inside an episode, but this 3/5 package result adds no long-term-memory node.

**Links.** [Paper](https://arxiv.org/abs/2608.20631) · [中文深读](papers/2026/2608.20631.zh.md) · [English note](papers/2026/2608.20631.md)

</details>

<a id="entry-2608-20274"></a>
<details><summary><strong>2026-08-25 · Break It Down, Pass It On</strong> · Skill-Granularity Transfer <!-- timefirst:area=skill-granularity-transfer --> — Procedural memory can shift from average harm to small gain when the write unit matches later reuse. <!-- timefirst:delta=whole-task-skills-to-subtask-transfer-units --></summary>

**Question.** Does inducing persistent skills per subtask transfer more reliably than whole-task text or code memories? <!-- timefirst:question=match-skill-write-granularity-to-later-consumer -->

**Evidence.** Task no-memory/text/code scores **22.1/20.9/18.0%**, while subtask scores **24.8/26.7/25.3%**; a two-model frozen-library replay reports **+9.9pp** for subtask skills. <!-- timefirst:evidence=subtask-skills-change-later-task-success~two-model-frozen-library-replay -->

**Caveat.** Architectures, write/query counts, and source trajectories differ; many cells reverse, intervals overlap, and `full induction and maintenance cost is missing`. <!-- timefirst:caveat=heterogeneous-effects-and-coupled-agent-architectures~full-induction-and-maintenance-cost-is-missing -->

**Map.** `early_signal` — Granularity is a causal question, but one heterogeneous study cannot establish a universal subtask advantage.

**Links.** [Paper](https://arxiv.org/abs/2608.20274) · [中文深读](papers/2026/2608.20274.zh.md) · [English note](papers/2026/2608.20274.md)

</details>

<a id="entry-2608-19993"></a>
<details><summary><strong>2026-08-25 · Optimal Skill Selection</strong> · Budgeted Skill-Set Selection <!-- timefirst:area=budgeted-skill-set-selection --> — Skill access is a set-level utility problem under context cost, not independent top-k relevance. <!-- timefirst:delta=independent-skill-ranking-to-budgeted-set-value --></summary>

**Question.** Can a selector capture complementary, redundant, and harmful skill combinations under a fixed token budget? <!-- timefirst:question=select-complementary-skill-sets-under-budget -->

**Evidence.** A controlled case moves **0% one-skill→93% complementary pair→56% with irrelevant procedure**; BPS reaches **.73** versus **.20–.52** for released alternatives with 28% fewer tokens. <!-- timefirst:evidence=skill-set-composition-causally-changes-execution~controlled-case-moves -->

**Caveat.** Tasks are filtered so every one-capability hybrid fails, BPS learns from **63,596 executions**, baselines lack matched supervision, and `training cost may dominate saved context`. <!-- timefirst:caveat=capability-gated-benchmark-and-unmatched-supervision~training-cost-may-dominate-saved-context -->

**Map.** `early_signal` — Set-level utility differs from item relevance, but one fixed, highly supervised coding library does not alter the Field Map.

**Links.** [Paper](https://arxiv.org/abs/2608.19993) · [中文深读](papers/2026/2608.19993.zh.md) · [English note](papers/2026/2608.19993.md)

</details>

<a id="entry-2608-20202"></a>
<details><summary><strong>2026-08-24 · MemTrapBench</strong> · Consumer-Side Memory Harm <!-- timefirst:area=consumer-side-memory-harm --> — Relevant prior history can still require an applicability gate before it reaches the current actor. <!-- timefirst:delta=relevant-memory-to-applicability-gated-use --></summary>

**Question.** Can semantically related memory causally worsen a later answer when the current task no longer needs or supports its prior reasoning pattern? <!-- timefirst:question=test-harm-from-inapplicable-memory-use -->

**Evidence.** On the adversarial stress test, no-memory scores **85.16 / 81.83** on Gemini/Qwen, while the strongest memory arms reach **71.17 / 70.99**; limited `trap free history controls` preserve Task Boundary performance before trap semantics cut **94.39→31.05**. <!-- timefirst:evidence=trap-semantics-change-later-answers~trap-free-history-controls -->

**Caveat.** Every query is standalone-solvable and prior dialogue is generated to plant a trap; `taxonomy matched prompt mitigation` lacks uncertainty, neutral-prompt control, framework-cost matching, and real-world prevalence evidence. <!-- timefirst:caveat=adversarial-construction-and-missing-controls~taxonomy-matched-prompt-mitigation -->

**Map.** `early_signal` — Post-retrieval applicability becomes a measurable consumer boundary, but one work-in-progress synthetic benchmark does not show that memory is generally harmful or change the durable map.

**Links.** [Paper](https://arxiv.org/abs/2608.20202) · [中文深读](papers/2026/2608.20202.zh.md) · [English note](papers/2026/2608.20202.md)

</details>

<a id="entry-2608-19652"></a>
<details><summary><strong>2026-08-24 · StateMemBench / StateMem</strong> · Evolving-State Resolution <!-- timefirst:area=evolving-state-resolution --> — Superseded history must be resolved into the current operative state, not merely retrieved. <!-- timefirst:delta=stored-history-to-operative-state-resolution --></summary>

**Question.** Can memory distinguish current values from superseded ones and recompute dependent decisions after multi-session updates? <!-- timefirst:question=resolve-supersession-before-current-action -->

**Evidence.** On DeepSeek, persistent StateMem reaches **0.363** versus Dense **0.205**; supersession moves **0.174→0.298**, while the strongest `matched answer time tracing` adds **15.0–31.7pp** over a generic-summary control but uses the full transcript. <!-- timefirst:evidence=supersession-and-tracing-improve-current-state~matched-answer-time-tracing -->

**Caveat.** The benchmark is aligned to the method's policy family; removing dependency propagation improves **0.363→0.373**, and `persistent ingestion costs 165 to 600 calls` per scenario without full lifecycle accounting. <!-- timefirst:caveat=aligned-benchmark-and-large-ingestion-cost~persistent-ingestion-costs-165-to-600-calls -->

**Map.** `early_signal` — State supersession and consumer-side resolution are distinct from recall, but one synthetic, single-run study does not add a durable Field Map node.

**Links.** [Paper](https://arxiv.org/abs/2608.19652) · [中文深读](papers/2026/2608.19652.zh.md) · [English note](papers/2026/2608.19652.md)

</details>

<a id="entry-2608-19564"></a>
<details><summary><strong>2026-08-24 · Remember, Verify, or Ask?</strong> · Memory Commitment Governance <!-- timefirst:area=memory-commitment-governance --> — Candidate information must pass authority and scope decisions before durable commitment. <!-- timefirst:delta=candidate-information-to-authority-aware-commitment --></summary>

**Question.** Should an acquired update persist, remain local, be verified against the world, or be clarified with the user before it affects future state? <!-- timefirst:question=choose-authority-aware-commitment-action -->

**Evidence.** Qwen few-shot accuracy rises **0.557→0.771**, but clarification recall remains **0.333**; policy reduces erroneous persistence **0.243→0.100**, while `label tool agreement` is only **0.229** on Qwen. <!-- timefirst:evidence=prompts-reshape-commitment-action-selection~label-tool-agreement -->

**Caveat.** The 70-item synthetic test has strong category signal, and `selected actions are not executed`; no write, later retrieval, downstream outcome, or complete cost is observed. <!-- timefirst:caveat=synthetic-rubric-and-nonexecuted-actions~selected-actions-are-not-executed -->

**Map.** `early_signal` — Candidate commitment is a governance boundary before storage; this benchmark signal does not establish a persistent-memory policy improvement.

**Links.** [Paper](https://arxiv.org/abs/2608.19564) · [中文深读](papers/2026/2608.19564.zh.md) · [English note](papers/2026/2608.19564.md)

</details>

<a id="entry-2608-19197"></a>
<details><summary><strong>2026-08-21 · SPADE</strong> · Training-Side Environment Memory <!-- timefirst:area=training-side-environment-memory --> — A bounded buffer feeds prior executable environments into future curriculum design. <!-- timefirst:delta=static-designer-to-retrieved-environment-history --></summary>

**Question.** Does cross-episode environment memory improve an adaptive training loop beyond the same designer, corpus grounding, and GRPO recipe without memory? <!-- timefirst:question=test-environment-memory-in-training-loop -->

**Evidence.** The selected full checkpoint averages **58.3** versus **53.2** for the official no-memory launcher, a `selected suite memory gap`; AIME 2026 instead moves **75.0→74.4** with memory. <!-- timefirst:evidence=memory-path-package-ablation~selected-suite-memory-gap -->

**Caveat.** Each condition is one run with `suite selected checkpoints`; removing memory also removes demonstration tokens, and the released sampler lacks an explicit seed. <!-- timefirst:caveat=single-run-and-selection-bias~suite-selected-checkpoints -->

**Map.** `early_signal` — Training-side persistent state can shape future experience generation, but one co-adaptive package does not isolate regret retrieval, FIFO retention, or a durable direction.

**Links.** [Paper](https://arxiv.org/abs/2608.19197) · [中文深读](papers/2026/2608.19197.zh.md) · [English note](papers/2026/2608.19197.md)

</details>

<a id="entry-2608-18704"></a>
<details><summary><strong>2026-08-21 · MemFuse</strong> · Multi-Source Evidence Access <!-- timefirst:area=multi-source-evidence-access --> — Provenance-preserving fused memory is useful only with an access loop that completes fragmented evidence. <!-- timefirst:delta=provenance-plus-evidence-completion --></summary>

**Question.** Can a memory join evidence fragmented across sources while returning the original support? The closest bounded controls share the event stream, reader setting, and final top-20 evidence budget. <!-- timefirst:question=fuse-fragments-with-source-traceability -->

**Evidence.** Overall reaches **0.4659 / 0.4574 / 0.4698**, but the `agentic retrieval ablation` costs **0.1036**, much more than removing graph/fusion overall. <!-- timefirst:evidence=overall-gain-dominated-by-agentic-access~agentic-retrieval-ablation -->

**Caveat.** The benchmark is synthetic and `Qwen ingestion tokens reach 93.27M`; long context still wins in the Gemini setting, with no lifecycle-matched stateful raw-search control. <!-- timefirst:caveat=synthetic-benchmark-and-high-ingestion-cost~qwen-ingestion-tokens -->

**Map.** `early_signal` — The result separates provenance-preserving organization from evidence-completing access; one package does not establish a durable graph-memory direction.

**Links.** [Paper](https://arxiv.org/abs/2608.18704) · [中文深读](papers/2026/2608.18704.zh.md) · [English note](papers/2026/2608.18704.md)

</details>

<a id="entry-2608-18719"></a>
<details><summary><strong>2026-08-21 · Competence, Not Accuracy</strong> · Skill-Update Governance <!-- timefirst:area=skill-update-governance --> — Judge gates must prove same-question discriminability before committing persistent skill edits. <!-- timefirst:delta=benchmark-accuracy-to-gate-discriminability --></summary>

**Question.** Can a reference-free judge distinguish correct from incorrect attempts on the exact candidate distribution it will govern? The closest control compares marginal and within-question AUC on the same SkillOpt traces. <!-- timefirst:question=qualify-judge-before-skill-commit -->

**Evidence.** Factual-QA AUC falls **0.855→0.735** after removing item-difficulty confounding, while the `research math within-question AUC` is **0.489**, near chance. <!-- timefirst:evidence=within-question-audit-reveals-difficulty-confound~research-math-within-question -->

**Caveat.** Competence above the floor is only necessary; `open ended judge transfer` is untested, and an early bare-letter probe produced a false null. <!-- timefirst:caveat=diagnostic-sensitive-and-open-tasks-untested~open-ended-judge-transfer -->

**Map.** `early_signal` — The admission boundary gains a pre-deployment diagnostic, but one gate study does not rewrite durable governance guidance.

**Links.** [Paper](https://arxiv.org/abs/2608.18719) · [中文深读](papers/2026/2608.18719.zh.md) · [English note](papers/2026/2608.18719.md)

</details>

<a id="entry-2608-18852"></a>
<details><summary><strong>2026-08-21 · SkillGate</strong> · Procedural-Memory Access <!-- timefirst:area=procedural-memory-access --> — An oracle-local selector channel changes which fixed skill files the policy exposes mid-episode. <!-- timefirst:delta=outcome-only-to-oracle-local-selector-channel --></summary>

**Question.** Does an oracle-supervised local selector channel improve an early skill-read decision beyond outcome-only training? The closest run fixes initialization, data, 100 steps, and hyperparameters but changes three coupled loss-design choices. <!-- timefirst:question=test-oracle-local-selector-supervision -->

**Evidence.** Success rises **47.0%→53.2%**, oracle exposure **54.3%→83.9%**, and misleading exposure **69.6%→21.8%**; the `oracle local selector channel` combines privileged utility, read-call masking, and selector-mass normalization. <!-- timefirst:evidence=oracle-channel-changes-skill-exposure~oracle-local-selector-channel -->

**Caveat.** Each setting has one 16-H800 run, and `verified single oracle identity` does not represent open, evolving, or compositional skill libraries. <!-- timefirst:caveat=single-run-and-oracle-dependent-training~verified-single-oracle -->

**Map.** `early_signal` — Skill availability and supervised access are distinct stages; a single training run does not establish a trend or isolate credit location.

**Links.** [Paper](https://arxiv.org/abs/2608.18852) · [中文深读](papers/2026/2608.18852.zh.md) · [English note](papers/2026/2608.18852.md)

</details>

<a id="entry-2608-19013"></a>
<details><summary><strong>2026-08-21 · Harness Continual Learning</strong> · Harness-State Evolution <!-- timefirst:area=harness-state-evolution --> — Candidate harnesses are committed only after current, historical-retention, and validity checks. <!-- timefirst:delta=unbounded-updates-to-guarded-harness-commit --></summary>

**Question.** How can a frozen-model agent update memory, interface, capability map, and router without silently forgetting earlier behavior? The closest governance control sweeps the historical-loss bound. <!-- timefirst:question=guard-nonparametric-agent-state-commit -->

**Evidence.** Unrestricted commitment ends at **60.13** versus **63.46** at `b=1`; the `memory update ablation` is **62.28 / 0.83 forgetting** versus **63.41 / 0.45** for Full HCL. <!-- timefirst:evidence=retention-bound-and-memory-stage-witness~memory-update-ablation -->

**Caveat.** Four harness components co-adapt, so `package gain not memory gain`; historical anchors are incomplete and full lifecycle cost is not reported. <!-- timefirst:caveat=coadaptive-package-and-incomplete-anchors~package-gain-not-memory -->

**Map.** `early_signal` — The commit boundary extends beyond the memory store, but one packaged system does not establish a durable evolution architecture.

**Links.** [Paper](https://arxiv.org/abs/2608.19013) · [中文深读](papers/2026/2608.19013.zh.md) · [English note](papers/2026/2608.19013.md)

</details>

<a id="entry-2608-17911"></a>
<details><summary><strong>2026-08-18 · CABLE</strong> · Retrieval & Access <!-- timefirst:area=retrieval-access --> — Stored links only earn their cost when they reach evidence the host retriever misses. <!-- timefirst:delta=structure-as-retriever-complement --></summary>

**Question.** Can stored memory links reach evidence missed by the same host retriever without increasing the final evidence budget? The closest lifecycle-matched control uses the same A-MEM host and evidence count. <!-- timefirst:question=links-reach-host-missed-evidence -->

**Evidence.** Under a matched A-MEM host budget and the same final evidence budget, LoCoMo Qwen3.5 moves **71.23→74.81** and MA-LongMemEval Qwen moves **59.33→65.33**. <!-- timefirst:evidence=same-host-budget-locomo-and-ma-longmemeval-gains~matched-a-mem-host-budget -->

**Caveat.** Temporal-reasoning slices regress, and the extra write-time generation and verification have not been lifecycle-cost-matched against a strong online-search control. <!-- timefirst:caveat=temporal-regression-and-unmatched-ingestion-cost~temporal-reasoning-slices -->

**Map.** `early_signal` — At the organize → access boundary, a relation must change reachability relative to the host interface; one paper does not rewrite the durable map.

**Links.** [Paper](https://arxiv.org/abs/2608.17911) · [中文深读](papers/2026/2608.17911.zh.md) · [English note](papers/2026/2608.17911.md)

</details>

<a id="entry-2608-17756"></a>
<details><summary><strong>2026-08-18 · D²ACCI</strong> · Evaluation & Governance <!-- timefirst:area=evaluation-governance --> — Memory features face paired evidence, protected slices, and stage-level promotion gates instead of aggregate-score promotion. <!-- timefirst:delta=aggregate-score-to-promotion-contract --></summary>

**Question.** How should a memory feature be promoted only when stage attribution and protected-slice non-regression both hold? The closest control is a paired baseline and candidate in the same runtime. <!-- timefirst:question=promotion-under-stage-and-non-regression-evidence -->

**Evidence.** Supplement extraction, session-memory retrieval, and Forget Guard show significant paired gains, while the **BM25/RRF null result** on LoCoMo / LongMemEval remains a monitored flag. <!-- timefirst:evidence=paired-gains-and-bm25-rrf-null-results~bm25-rrf-null-result -->

**Caveat.** This is deployment evidence from a diagnostic protocol, not an isolated effect of a new memory architecture; trace coverage dependence, evaluators, and promotion thresholds constrain the conclusion. <!-- timefirst:caveat=protocol-evidence-not-new-architecture~trace-coverage-dependence -->

**Map.** `early_signal` — At the governance boundary, null results and non-regression begin to constrain feature promotion, but one protocol does not rewrite the map.

**Links.** [Paper](https://arxiv.org/abs/2608.17756) · [中文深读](papers/2026/2608.17756.zh.md) · [English note](papers/2026/2608.17756.md)

</details>

<a id="entry-2608-17587"></a>
<details><summary><strong>2026-08-18 · WER</strong> · Memory Learning & Evolution <!-- timefirst:area=memory-learning-evolution --> — Execution outcomes train the skill-writer policy rather than merely prompting another inference-time reflection. <!-- timefirst:delta=execution-feedback-trains-writer-policy --></summary>

**Question.** Can a procedural-memory writer policy learn from a frozen executor's successful and failed trajectories rather than only reflecting on skill text? The closest control fixes the optimizer backbone and refinement workflow. <!-- timefirst:question=writer-policy-learning-from-execution -->

**Evidence.** With the same Qwen3-4B optimizer and workflow, BFCL v4 moves **67.28→76.63** and tau2 **40.43→50.72**; an extra refinement regression appears in the additional round. <!-- timefirst:evidence=same-backbone-gains-then-extra-refinement-regresses~extra-refinement-regression -->

**Caveat.** More expensive rollouts and programmatic verifier cost are the main alternative explanation; verifier availability and cost govern whether the writer-learning loop transfers. <!-- timefirst:caveat=rollout-and-verifier-cost~programmatic-verifier-cost -->

**Map.** `early_signal` — At the write/update boundary, the learned writer becomes persistent procedural state, but one work does not establish a durable trend.

**Links.** [Paper](https://arxiv.org/abs/2608.17587) · [中文深读](papers/2026/2608.17587.zh.md) · [English note](papers/2026/2608.17587.md)

</details>

<a id="entry-2608-17588"></a>
<details><summary><strong>2026-08-18 · TRUSS</strong> · Procedural Memory Governance <!-- timefirst:area=procedural-memory-governance --> — Generated skills become executable artifacts that must pass static and shadow-execution certification before persistence. <!-- timefirst:delta=generated-text-to-certified-artifact --></summary>

**Question.** Before a generated skill enters persistent procedural memory, can static obligations, controlled shadow execution, and provenance traces certify it reliably? The closest controls are LLM and static checkers on matched SkillInject artifacts. <!-- timefirst:question=certify-generated-skills-before-persistence -->

**Evidence.** On matched SkillInject artifacts, the LLM checker reaches **44.64% precision / 19.05% recall**, static checking **81.55 / 94.05**, and full TRUSS certification **100 / 100**. <!-- timefirst:evidence=matched-skillinject-certification-results~full-truss-certification -->

**Caveat.** The gain belongs to the full executor-dependent package; it cannot be isolated to skill representation or one checker. <!-- timefirst:caveat=package-and-executor-confounding~executor-dependent-package -->

**Map.** `early_signal` — At the write → promotion/governance boundary, plausible text is not yet a reusable capability; this does not independently rewrite the durable map.

**Links.** [Paper](https://arxiv.org/abs/2608.17588) · [中文深读](papers/2026/2608.17588.zh.md) · [English note](papers/2026/2608.17588.md)

</details>

<a id="entry-2608-17534"></a>
<details><summary><strong>2026-08-18 · ArborMem</strong> · State Localization <!-- timefirst:area=state-localization --> — The read path first identifies the active historical branch, then restores its trajectory before supplemental retrieval. <!-- timefirst:delta=localize-state-before-retrieval --></summary>

**Question.** In a long-running interaction, can the agent localize the historical trajectory resumed by the current turn before branch-local restoration and supplemental retrieval? The closest control removes localization from the same pipeline. <!-- timefirst:question=localize-active-trajectory-before-retrieval -->

**Evidence.** On a fixed LongMemEval subset, removing state localization changes the 30B setting **82→70**, but the 4B setting only **48→46**, a model-dependent localization effect rather than a uniform gain. <!-- timefirst:evidence=localization-ablation-model-dependent~model-dependent-localization-effect -->

**Caveat.** Forest representation not isolated: the ablation supports only the localization boundary, while a cheaper state index remains a strong alternative. <!-- timefirst:caveat=forest-representation-not-isolated~forest-representation-not-isolated -->

**Map.** `early_signal` — State localization becomes a boundary before access; one model-dependent result is insufficient to promote a durable map node.

**Links.** [Paper](https://arxiv.org/abs/2608.17534) · [中文深读](papers/2026/2608.17534.zh.md) · [English note](papers/2026/2608.17534.md)

</details>

<a id="entry-2608-16168"></a>
<details><summary><strong>2026-08-17 · QUMem</strong> · Consumer-State Reconstruction <!-- timefirst:area=consumer-state-reconstruction --> — Retrieved history becomes evidence for reconstructing a query-conditioned current user state after retrieval. <!-- timefirst:delta=retrieval-to-consumer-state-reconstruction --></summary>

**Question.** Does an explicit stage still need to reconstruct a query-conditioned current user state after evidence retrieval? The closest control removes reconstruction from the same typed-retrieval pipeline. <!-- timefirst:question=reconstruct-current-user-state-after-retrieval -->

**Evidence.** Reconstruction largest ablation: PersonaMem + GPT-4o-mini moves from **61.02 full → 58.38** without episodes → **57.11** without typed decomposition → **54.51** without reconstruction, the largest drop. <!-- timefirst:evidence=reconstruction-largest-ablation-on-personamem~reconstruction-largest-ablation -->

**Caveat.** A matched evidence synthesis budget is missing, so some reconstruction gain may come from additional downstream computation rather than a distinct state abstraction. <!-- timefirst:caveat=retrieval-and-synthesis-budget-not-matched~matched-evidence-synthesis-budget -->

**Map.** `early_signal` — At the access → consumer-state boundary, retrieval does not automatically equal reuse; independent evidence is still needed to revise the map.

**Links.** [Paper](https://arxiv.org/abs/2608.16168) · [中文深读](papers/2026/2608.16168.zh.md) · [English note](papers/2026/2608.16168.md)

</details>

<a id="entry-2608-16114"></a>
<details><summary><strong>2026-08-17 · HyperSkill</strong> · Procedural Memory Structure <!-- timefirst:area=procedural-memory-structure --> — Higher-order trajectory relations participate in retrieval, skill ranking, and maintenance as one structural access package. <!-- timefirst:delta=higher-order-relations-in-access-package --></summary>

**Question.** Do higher-order trajectory relations materially change retrieval, skill ranking, and maintenance in procedural memory? The closest control removes the hypergraph path in a system ablation. <!-- timefirst:question=higher-order-relations-in-skill-access -->

**Evidence.** Hypergraph path ablation: Qwen3 reports **52.00 / 36.97 / 50.59** on xBench / GAIA / WebWalkerQA, versus **41.00 / 35.76 / 44.71** without the hypergraph path. <!-- timefirst:evidence=hypergraph-path-ablation-across-three-benchmarks~hypergraph-path-ablation -->

**Caveat.** Representation access confounded: the ablation changes representation and the access pipeline together; decomposition, dual-path retrieval, ranking, and maintenance must be fixed for attribution. <!-- timefirst:caveat=representation-and-access-pipeline-confounded~representation-access-confounded -->

**Map.** `early_signal` — At the organize → access/maintenance boundary, current evidence supports the structural package rather than proving hypergraphs uniquely necessary.

**Links.** [Paper](https://arxiv.org/abs/2608.16114) · [中文深读](papers/2026/2608.16114.zh.md) · [English note](papers/2026/2608.16114.md)

</details>

<a id="entry-2608-12888"></a>
<details><summary><strong>2026-08-13 · ReFind</strong> · Raw-State Retrieval <!-- timefirst:area=raw-state-retrieval --> — Structured memory must beat stateful iterative search over raw logs, not a single-shot BM25 straw control. <!-- timefirst:delta=stronger-raw-control-for-structure --></summary>

**Question.** What raw-state control should structured memory beat? ReFind's closest matched alternative is iterative search with session, time, local-context operations, and seen-session state. <!-- timefirst:question=strongest-raw-control-for-structured-memory -->

**Evidence.** Stateful raw-search advantage: on fixed LongMemEval-S/M, ReFind reports **93.2 / 89.3**, versus **78.7 / 82.2** for generic-agentic BM25 and **84.7 / 68.9** for a one-search control. <!-- timefirst:evidence=stateful-raw-search-outperforms-weaker-controls~stateful-raw-search-advantage -->

**Caveat.** Semantic and acting tasks still lack strictly matched online latency, token use, and **full lifecycle cost**, so raw search cannot yet be claimed to dominate structured memory generally. <!-- timefirst:caveat=semantic-tasks-and-lifecycle-cost-unmatched~full-lifecycle-cost -->

**Map.** `early_signal` — It raises the raw baseline at the access boundary and constrains structure claims without establishing a durable conclusion alone.

**Links.** [Paper](https://arxiv.org/abs/2608.12888) · [中文深读](papers/2026/2608.12888.zh.md) · [English note](papers/2026/2608.12888.md)

</details>

<a id="periods"></a><a id="changes"></a><a id="whats-changing"></a>
## 7 days / 30 days: What Changed in the Memory Lifecycle

> **Timing basis.** Rolling-window membership uses only `radar_published_at`. The eight migrated records in the Timeline have no reconstructable Radar acceptance time, so they remain historical Field Map context and never count as current-window support.

<a id="last-7-days"></a>
### Last 7 days: 2026-08-20—2026-08-26

- **`new_signal` · Single interaction memory injection.** Supports: [2608.23471](#entry-2608-23471); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (measure joint retrieval and steering beside utility): match attack compute and report benign behavior. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="single-interaction-memory-injection" state="new_signal" supports="2608.23471" confidence="medium" implication="measure-joint-retrieval-and-steering-beside-utility" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Retrieval experience amortization.** Supports: [2608.22767](#entry-2608-22767); confidence: **low**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (test learned access on growing shuffled stores): include edit, delete, drift, and total maintenance cost. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="retrieval-experience-amortization" state="new_signal" supports="2608.22767" confidence="low" implication="test-learned-access-on-growing-shuffled-stores" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Constraint preserving compaction.** Supports: [2608.22752](#entry-2608-22752); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (match source aware compaction and retained tokens while charging classification and scope costs): charge classification, scope inference, and retained tokens. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="constraint-preserving-compaction" state="new_signal" supports="2608.22752" confidence="medium" implication="match-source-aware-compaction-and-retained-tokens-while-charging-classification-and-scope-costs" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Contrastive procedural memory.** Supports: [2608.22533](#entry-2608-22533); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate contrast from heterogeneous coverage): match source success diversity and full construction cost. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="contrastive-procedural-memory" state="new_signal" supports="2608.22533" confidence="medium" implication="separate-contrast-from-heterogeneous-coverage" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Skill validity boundaries.** Supports: [2608.22339](#entry-2608-22339); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (test skill boundaries under equal context): isolate boundary text, checker, repair, and failed-trajectory admission. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="skill-validity-boundaries" state="new_signal" supports="2608.22339" confidence="medium" implication="test-skill-boundaries-under-equal-context" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Persistent verifier governance.** Supports: [2608.21867](#entry-2608-21867); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate persistent verifier state from bundled lifecycle operations against a verifier only control): test the closest contrast directly. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="persistent-verifier-governance" state="new_signal" supports="2608.21867" confidence="medium" implication="separate-persistent-verifier-state-from-bundled-lifecycle-operations-against-a-verifier-only-control" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->


- **`new_signal` · Provenance ranking utility frontier.** Supports: [2608.21230](#entry-2608-21230); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (measure poison rejection beside useful evidence retention): pair attack suppression with trusted and untrusted answer-evidence recall under matched context. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="provenance-ranking-utility-frontier" state="new_signal" supports="2608.21230" confidence="medium" implication="measure-poison-rejection-beside-useful-evidence-retention" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Executable memory hygiene.** Supports: [2608.20664](#entry-2608-20664); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (require later executable behavior and a strong verbatim control): match sleep compute before crediting typed consolidation. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="executable-memory-hygiene" state="new_signal" supports="2608.20664" confidence="medium" implication="require-later-executable-behavior-and-a-strong-verbatim-control" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Selection driven working memory.** Supports: [2608.20631](#entry-2608-20631); confidence: **low**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate active retention from long term persistence): isolate scoring, decay, folding, and suppression under token-matched controls. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="selection-driven-working-memory" state="new_signal" supports="2608.20631" confidence="low" implication="separate-active-retention-from-long-term-persistence" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Skill granularity transfer.** Supports: [2608.20274](#entry-2608-20274); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (match write units to the same later consumer): freeze source trajectories, actor, retrieval calls, and lifecycle cost before comparing task and subtask skills. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="skill-granularity-transfer" state="new_signal" supports="2608.20274" confidence="medium" implication="match-write-units-to-the-same-later-consumer" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Budgeted skill set selection.** Supports: [2608.19993](#entry-2608-19993); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (match selector supervision and full training cost): test complementarity on unfiltered tasks and charge outcome-data collection against saved context. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="budgeted-skill-set-selection" state="new_signal" supports="2608.19993" confidence="medium" implication="match-selector-supervision-and-full-training-cost" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Memory consumption harm makes applicability a post-retrieval decision.** Supports: [2608.20202](#entry-2608-20202); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (test useful retention beside trap rejection): use mixed memory-required, neutral, and adversarial workloads under matched context and lifecycle cost. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="memory-consumption-harm" state="new_signal" supports="2608.20202" confidence="medium" implication="test-useful-retention-beside-trap-rejection" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · State supersession resolution separates current state from retrieved history.** Supports: [2608.19652](#entry-2608-19652); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate persistent updates from answer time resolution): match ingestion and transcript access while independently varying retirement, dependency checks, and recomputation. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="state-supersession-resolution" state="new_signal" supports="2608.19652" confidence="medium" implication="separate-persistent-updates-from-answer-time-resolution" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Memory commitment governance precedes durable storage.** Supports: [2608.19564](#entry-2608-19564); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (execute commitment choices before claiming utility): run writes, checks, and clarification through later retrieval and task outcomes under authority-aware costs. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="memory-commitment-governance" state="new_signal" supports="2608.19564" confidence="medium" implication="execute-commitment-choices-before-claiming-utility" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Multi source evidence completion separates organization from access.** Supports: [2608.18704](#entry-2608-18704); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate organization from evidence completing access): attribute fused representation and answer-time search independently under matched lifecycle cost. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="multi-source-evidence-completion" state="new_signal" supports="2608.18704" confidence="medium" implication="separate-organization-from-evidence-completing-access" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Judge gate discriminability precedes persistent skill admission.** Supports: [2608.18719](#entry-2608-18719); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (qualify judge on candidate distribution): use within-question separation on genuine optimization traces before a judge controls commits. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="judge-gate-discriminability" state="new_signal" supports="2608.18719" confidence="medium" implication="qualify-judge-on-candidate-distribution" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Selector local credit makes skill access a learned stage.** Supports: [2608.18852](#entry-2608-18852); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (credit sparse memory actions locally): separate privileged selector supervision, loss masking, skill exposure, and downstream execution. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="selector-local-credit" state="new_signal" supports="2608.18852" confidence="medium" implication="credit-sparse-memory-actions-locally" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Guarded harness evolution treats commit as the continual-state boundary.** Supports: [2608.19013](#entry-2608-19013); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (guard harness state before commit): test current utility, historical retention, and validity while attributing each co-adaptive component separately. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="guarded-harness-evolution" state="new_signal" supports="2608.19013" confidence="medium" implication="guard-harness-state-before-commit" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Training side environment memory guides future curriculum generation.** Supports: [2608.19197](#entry-2608-19197); confidence: **low**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (match retrieved training memory to static replay): compare retrieved history with token-matched static, random, and score-shuffled examples before crediting the memory policy. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="training-side-environment-memory" state="new_signal" supports="2608.19197" confidence="low" implication="match-retrieved-training-memory-to-static-replay" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

<a id="last-30-days"></a>
### Last 30 days: 2026-07-28—2026-08-26

- **`new_signal` · Single interaction memory injection.** Supports: [2608.23471](#entry-2608-23471); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (measure joint retrieval and steering beside utility): match attack compute and report benign behavior. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="single-interaction-memory-injection" state="new_signal" supports="2608.23471" confidence="medium" implication="measure-joint-retrieval-and-steering-beside-utility" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Retrieval experience amortization.** Supports: [2608.22767](#entry-2608-22767); confidence: **low**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (test learned access on growing shuffled stores): include edit, delete, drift, and total maintenance cost. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="retrieval-experience-amortization" state="new_signal" supports="2608.22767" confidence="low" implication="test-learned-access-on-growing-shuffled-stores" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Constraint preserving compaction.** Supports: [2608.22752](#entry-2608-22752); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (match source aware compaction and retained tokens while charging classification and scope costs): charge classification, scope inference, and retained tokens. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="constraint-preserving-compaction" state="new_signal" supports="2608.22752" confidence="medium" implication="match-source-aware-compaction-and-retained-tokens-while-charging-classification-and-scope-costs" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Contrastive procedural memory.** Supports: [2608.22533](#entry-2608-22533); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate contrast from heterogeneous coverage): match source success diversity and full construction cost. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="contrastive-procedural-memory" state="new_signal" supports="2608.22533" confidence="medium" implication="separate-contrast-from-heterogeneous-coverage" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Skill validity boundaries.** Supports: [2608.22339](#entry-2608-22339); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (test skill boundaries under equal context): isolate boundary text, checker, repair, and failed-trajectory admission. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="skill-validity-boundaries" state="new_signal" supports="2608.22339" confidence="medium" implication="test-skill-boundaries-under-equal-context" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Persistent verifier governance.** Supports: [2608.21867](#entry-2608-21867); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate persistent verifier state from bundled lifecycle operations against a verifier only control): test the closest contrast directly. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="persistent-verifier-governance" state="new_signal" supports="2608.21867" confidence="medium" implication="separate-persistent-verifier-state-from-bundled-lifecycle-operations-against-a-verifier-only-control" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->


- **`new_signal` · Provenance ranking utility frontier.** Supports: [2608.21230](#entry-2608-21230); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (measure poison rejection beside useful evidence retention): pair attack suppression with trusted and untrusted answer-evidence recall under matched context. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="provenance-ranking-utility-frontier" state="new_signal" supports="2608.21230" confidence="medium" implication="measure-poison-rejection-beside-useful-evidence-retention" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Executable memory hygiene.** Supports: [2608.20664](#entry-2608-20664); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (require later executable behavior and a strong verbatim control): match sleep compute before crediting typed consolidation. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="executable-memory-hygiene" state="new_signal" supports="2608.20664" confidence="medium" implication="require-later-executable-behavior-and-a-strong-verbatim-control" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Selection driven working memory.** Supports: [2608.20631](#entry-2608-20631); confidence: **low**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate active retention from long term persistence): isolate scoring, decay, folding, and suppression under token-matched controls. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="selection-driven-working-memory" state="new_signal" supports="2608.20631" confidence="low" implication="separate-active-retention-from-long-term-persistence" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Skill granularity transfer.** Supports: [2608.20274](#entry-2608-20274); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (match write units to the same later consumer): freeze source trajectories, actor, retrieval calls, and lifecycle cost before comparing task and subtask skills. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="skill-granularity-transfer" state="new_signal" supports="2608.20274" confidence="medium" implication="match-write-units-to-the-same-later-consumer" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Budgeted skill set selection.** Supports: [2608.19993](#entry-2608-19993); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (match selector supervision and full training cost): test complementarity on unfiltered tasks and charge outcome-data collection against saved context. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="budgeted-skill-set-selection" state="new_signal" supports="2608.19993" confidence="medium" implication="match-selector-supervision-and-full-training-cost" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Memory consumption harm makes applicability a post-retrieval decision.** Supports: [2608.20202](#entry-2608-20202); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (test useful retention beside trap rejection): use mixed memory-required, neutral, and adversarial workloads under matched context and lifecycle cost. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="memory-consumption-harm" state="new_signal" supports="2608.20202" confidence="medium" implication="test-useful-retention-beside-trap-rejection" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · State supersession resolution separates current state from retrieved history.** Supports: [2608.19652](#entry-2608-19652); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate persistent updates from answer time resolution): match ingestion and transcript access while independently varying retirement, dependency checks, and recomputation. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="state-supersession-resolution" state="new_signal" supports="2608.19652" confidence="medium" implication="separate-persistent-updates-from-answer-time-resolution" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Memory commitment governance precedes durable storage.** Supports: [2608.19564](#entry-2608-19564); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (execute commitment choices before claiming utility): run writes, checks, and clarification through later retrieval and task outcomes under authority-aware costs. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="memory-commitment-governance" state="new_signal" supports="2608.19564" confidence="medium" implication="execute-commitment-choices-before-claiming-utility" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Multi source evidence completion separates organization from access.** Supports: [2608.18704](#entry-2608-18704); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate organization from evidence completing access): attribute fused representation and answer-time search independently under matched lifecycle cost. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="multi-source-evidence-completion" state="new_signal" supports="2608.18704" confidence="medium" implication="separate-organization-from-evidence-completing-access" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Judge gate discriminability precedes persistent skill admission.** Supports: [2608.18719](#entry-2608-18719); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (qualify judge on candidate distribution): use within-question separation on genuine optimization traces before a judge controls commits. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="judge-gate-discriminability" state="new_signal" supports="2608.18719" confidence="medium" implication="qualify-judge-on-candidate-distribution" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Selector local credit makes skill access a learned stage.** Supports: [2608.18852](#entry-2608-18852); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (credit sparse memory actions locally): separate privileged selector supervision, loss masking, skill exposure, and downstream execution. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="selector-local-credit" state="new_signal" supports="2608.18852" confidence="medium" implication="credit-sparse-memory-actions-locally" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Guarded harness evolution treats commit as the continual-state boundary.** Supports: [2608.19013](#entry-2608-19013); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (guard harness state before commit): test current utility, historical retention, and validity while attributing each co-adaptive component separately. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="guarded-harness-evolution" state="new_signal" supports="2608.19013" confidence="medium" implication="guard-harness-state-before-commit" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

- **`new_signal` · Training side environment memory guides future curriculum generation.** Supports: [2608.19197](#entry-2608-19197); confidence: **low**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (match retrieved training memory to static replay): compare retrieved history with token-matched static, random, and score-shuffled examples before crediting the memory policy. Exact synthesis time: `2026-08-26T00:27:00Z`. <!-- timefirst:direction key="training-side-environment-memory" state="new_signal" supports="2608.19197" confidence="low" implication="match-retrieved-training-memory-to-static-replay" timing="radar_published_at" synthesized="2026-08-26T00:27:00Z" prior="none" -->

Time view: [weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a><a id="research-map"></a>
## Field Map

`experience/archive → write → organize → state localization → access/admission → consumer state → update/evolve/forget → governance/cost/provenance`

| Boundary | Core question | Current signal |
|---|---|---|
| **Write** | What should persist, and how should reusable artifacts be authored? | Granularity and writer policy depend on workload and feedback. |
| **Organize** | Which relations deserve precomputation? | Relations earn cost when they alter reachability beyond the host interface. |
| **State localization** | Which historical trajectory is active now? | Relevance retrieval may need an earlier state-selection stage. |
| **Access / admission** | What should be retrieved, expanded, or withheld? | Raw search, graph expansion, and admission are different operators. |
| **Consumer state** | What should the downstream actor actually see? | Retrieved evidence may still require reconstruction or rebinding. |
| **Evolution / forgetting** | Which adaptive state changes from which feedback? | Content, writer/read policy, relations, and feedback are distinct axes. |
| **Governance / cost** | Which artifacts/features deserve promotion? | Certification, paired evidence, provenance, and lifecycle cost are becoming first-class constraints. |

[Full research-problem map →](categories/README.en.md) · [How Agent Memory is evaluated →](https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-memory)

<a id="reading-paths"></a>
## Reading Paths

| Question | Read | What to learn |
|---|---|---|
| **When does structure earn its cost?** | ReFind → CABLE → ArborMem → QUMem | Move from a strong raw baseline to complementary relations, state localization, and consumer-state reconstruction; ask whether each stage adds an operation that a cheaper alternative cannot provide. |
| **How does procedural memory become a governed capability?** | HyperSkill → WER → TRUSS | Representation/relations, writer learning, and runtime certification are separate problems. |
| **How should memory features be attributed causally?** | D²ACCI → QUMem → ReFind | Start from stage traces and promotion gates, then see how reconstruction and raw controls change attribution. |

<a id="library"></a>
## Research Library

Browse long-lived work by research problem, research line, or year. If you know the question but not the paper title, start with the problem index:

- [English Research Library](library/README.en.md)
- [中文 Research Library](library/README.md)
- [Design anchors](papers/anchors.md)

<a id="how-to-use"></a>
## How to Use

Scan the Timeline summaries first. Open a disclosure in place when you need the question, closest control, decisive evidence, caveat, and map status. Use the 7-day / 30-day synthesis for recent movement, or Field Map, Reading Paths, and Research Library to follow a research problem over time.

## Scope / About / Contributing

A work is in scope when information persists or is explicitly managed across interaction/reasoning steps and materially changes future agent behavior. Ordinary fixed RAG, generic long-context/KV-cache work, and unrelated continual learning are usually out of scope.

This is a **curated research map, not a keyword feed**. Negative results, baseline reversals, lifecycle-cost evidence, and attribution failures stay visible when they change the conclusion.

[Suggest a paper](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [Report a correction](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [Contribution guide](CONTRIBUTING.md)

Related Radars: [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)
