#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CUTOFF = "2026-08-28T00:53:00Z"
WIN7 = (date(2026, 8, 22), date(2026, 8, 28))
WIN30 = (date(2026, 7, 30), date(2026, 8, 28))

EN_ENTRIES = r'''<a id="entry-2608-25500"></a>
<details><summary><strong>2026-08-28 · CaSKG</strong> · Procedural Edge Calibration <!-- timefirst:area=procedural-edge-calibration --> — A frozen skill library becomes safer to traverse when only supported dependency edges may propagate query relevance. <!-- timefirst:delta=uncalibrated-graph-propagation-to-edge-confidence-calibration --></summary>

**Question.** Against the same frozen Skill1000 and downstream actor loop, does calibrating graph edges improve later execution beyond an existing graph retriever? <!-- timefirst:question=test-edge-calibration-against-matched-graph-control -->

**Evidence.** Against the **Graph-of-Skills control**, six-model macro ALFWorld success moves **80.01→86.79** and ScienceWorld score **72.62→80.50**; CaSKG also uses fewer environment steps in all 12 model×benchmark cells. <!-- timefirst:evidence=matched-graph-retrieval-changes-later-execution~graph-of-skills-control -->

**Caveat.** Counterfactual probes are textual LLM judgments rather than environment interventions; **construction costs are missing**, as are token, latency, dollar, energy, and repeated-seed uncertainty. <!-- timefirst:caveat=textual-counterfactuals-and-incomplete-cost~construction-costs-are-missing -->

**Map.** `early_signal` — One calibrated graph does not establish a durable procedural-memory direction.

**Links.** [Paper](https://arxiv.org/abs/2608.25500) · [中文深读](papers/2026/2608.25500.zh.md) · [English note](papers/2026/2608.25500.md) · [Code](https://github.com/ZhiyuanLi218/Caskg)

</details>

<a id="entry-2608-25329"></a>
<details><summary><strong>2026-08-28 · HiPS</strong> · Personalized Memory-Policy Evolution <!-- timefirst:area=personalized-memory-policy-evolution --> — Shared memory-management rules and persona-local deltas co-evolve from task outcomes instead of remaining one global static policy. <!-- timefirst:delta=global-static-memory-policy-to-hierarchical-personalized-evolution --></summary>

**Question.** Does memory-management policy itself need persistent shared and persona-local state, and which tier matters when the user distribution shifts? <!-- timefirst:question=test-shared-versus-personalized-memory-policy-state -->

**Evidence.** On PERMA, full HiPS reaches **66.95/56.56/63.83/56.30**; removing **Cross-Level Rule Flow** falls to **45.39/40.87/43.12/36.50**, while removing persona gating also causes large OOD drops. <!-- timefirst:evidence=matched-ablation-localizes-ood-personalization-value~cross-level-rule-flow -->

**Caveat.** Headline system comparisons sometimes use **different model backbones**, while distillation, gating, rule flow, selection, and RL co-vary; full continual maintenance cost is incomplete. <!-- timefirst:caveat=heterogeneous-headline-baselines-and-coupled-policy-package~different-model-backbones -->

**Map.** `early_signal` — Personalized policy state is one strong signal, not yet a durable map revision.

**Links.** [Paper](https://arxiv.org/abs/2608.25329) · [中文深读](papers/2026/2608.25329.zh.md) · [English note](papers/2026/2608.25329.md)

</details>

<a id="entry-2608-25553"></a>
<details><summary><strong>2026-08-28 · Stale Constraints</strong> · Freshness-Verification Allocation <!-- timefirst:area=freshness-verification-allocation --> — Correct provenance is insufficient when a budgeted consumer fails to inspect the path that reveals supersession. <!-- timefirst:delta=provenance-availability-to-verification-allocation -->></summary>

**Question.** At the same two-record verification budget, is stale-memory harm caused by reasoning failure or by spending verification on the wrong records? <!-- timefirst:question=isolate-verification-allocation-at-fixed-budget -->

**Evidence.** Under the **forced-critical same-budget** intervention, current-record-consistent decisions rise **34/150→145/150**, **38/150→147/150**, and **38/150→130/150** across primary, replication, and held-out settings; corrected held-out robustness reaches **36/150→146/150**. <!-- timefirst:evidence=fixed-budget-allocation-causally-changes-later-decisions~forced-critical-same-budget -->

**Caveat.** The **experimenter knows critical path** in the intervention, the archive makes supersession discoverable in one request, and storage/index/reconsolidation costs are outside the experiment. <!-- timefirst:caveat=diagnostic-instrument-not-deployable-scheduler~experimenter-knows-critical-path -->

**Map.** `early_signal` — Freshness verification becomes a distinct access decision, but one diagnostic study does not revise the map.

**Links.** [Paper](https://arxiv.org/abs/2608.25553) · [中文深读](papers/2026/2608.25553.zh.md) · [English note](papers/2026/2608.25553.md)

</details>

<a id="entry-2608-25570"></a>
<details><summary><strong>2026-08-28 · KOPE</strong> · Execution-Grounded Experience Graph <!-- timefirst:area=execution-grounded-experience-graph --> — Compiler, correctness, and performance outcomes become persistent graph state that later optimization decisions can reuse under a bounded context. <!-- timefirst:delta=discarded-optimization-trajectories-to-execution-grounded-experience-memory --></summary>

**Question.** With the foundation model and workflow fixed, does persistent decision→outcome graph memory change later kernel execution beyond context construction alone? <!-- timefirst:question=test-experience-graph-under-fixed-workflow -->

**Evidence.** The **graph memory ablation** fixes GLM-5.2 and raises full-suite pass rate **55.2%→84.6%**; on 412 paired valid timing cases, graph memory yields a **1.43×** geometric-mean speedup ratio. <!-- timefirst:evidence=same-workflow-graph-memory-changes-executable-outcomes~graph-memory-ablation -->

**Caveat.** Active-context retrieval, compression, and injection remain coupled; the graph score is observational rather than causal, and **graph maintenance costs are missing**. <!-- timefirst:caveat=integrated-context-package-and-incomplete-lifecycle-cost~graph-maintenance-costs-are-missing -->

**Map.** `early_signal` — Execution-grounded memory is concrete, but evidence is still domain-specific and package-level.

**Links.** [Paper](https://arxiv.org/abs/2608.25570) · [中文深读](papers/2026/2608.25570.zh.md) · [English note](papers/2026/2608.25570.md)

</details>

<a id="entry-2608-25655"></a>
<details><summary><strong>2026-08-28 · TSIM</strong> · Episode-Integrity Reconstruction <!-- timefirst:area=episode-integrity-reconstruction --> — Interleaved chat is first reconstructed into coherent episodes before hierarchical retrieval assembles evidence. <!-- timefirst:delta=flat-turn-retrieval-to-episode-integrity-reconstruction --></summary>

**Question.** When one thread multiplexes unrelated tasks, is the missing operation turn relevance or reconstruction of the prior episode that the current request resumes? <!-- timefirst:question=test-episode-reconstruction-before-retrieval -->

**Evidence.** The staged ablation moves **26.2 standard RAG → 43.4 fixed-token direct → 55.5 semantic-drift direct → 74.2 full TSIM**; across three answer backends TSIM beats the strongest corresponding baseline by **5.6–17.6 points**. <!-- timefirst:evidence=staged-episode-organization-improves-later-answers~semantic-drift-direct-to-full-tsim -->

**Caveat.** **Segmentation summaries and routing** remain coupled, SCALE-QA and TSIM are co-designed, and construction/index/update/query lifecycle cost is not fully matched. <!-- timefirst:caveat=package-attribution-and-codesigned-benchmark~segmentation-summaries-and-routing -->

**Map.** `early_signal` — Episode integrity sharpens state localization, but one co-designed package does not revise the durable map.

**Links.** [Paper](https://arxiv.org/abs/2608.25655) · [中文深读](papers/2026/2608.25655.zh.md) · [English note](papers/2026/2608.25655.md)

</details>

<a id="entry-2608-26005"></a>
<details><summary><strong>2026-08-28 · VoiceMem</strong> · Streaming Dual-Brain Memory <!-- timefirst:area=streaming-dual-brain-memory --> — Factual/entity state and affect/persona state use separate streaming paths behind a backend-portable upper memory layer. <!-- timefirst:delta=single-text-memory-path-to-streaming-dual-state-contracts --></summary>

**Question.** Can a thin upper organization/routing layer improve persistent conversational memory across interchangeable backends while staying within a real-time retrieval budget? <!-- timefirst:question=test-portable-upper-memory-layer-and-realtime-access -->

**Evidence.** With the **same-backend upper layer**, Mem0 rises **61.68→91.20**, LangMem **56.18→71.94**, and Zep **62.93→85.85**; VoiceMem reports **430 memory tokens and 134 ms retrieval** at K=5. <!-- timefirst:evidence=upper-layer-improves-multiple-fixed-backends~same-backend-upper-layer -->

**Caveat.** The dual-brain package co-varies extraction, representation, routing, graph structure, and streaming I/O; **retrieval not end-to-end latency** is the 134 ms figure, and write/maintenance cost is incomplete. <!-- timefirst:caveat=multi-stage-package-and-incomplete-write-cost~retrieval-not-end-to-end-latency -->

**Map.** `early_signal` — Separate factual and affect state contracts are a signal, not yet a durable multimodal-memory node.

**Links.** [Paper](https://arxiv.org/abs/2608.26005) · [中文深读](papers/2026/2608.26005.zh.md) · [English note](papers/2026/2608.26005.md) · [Code](https://github.com/xzf-thu/VoiceMem) · [Project](https://xzf-thu.github.io/VoiceMem/)

</details>

'''

ZH_ENTRIES = r'''<a id="entry-2608-25500"></a>
<details><summary><strong>2026-08-28 · CaSKG</strong> · Procedural Edge Calibration <!-- timefirst:area=procedural-edge-calibration --> — 冻结 skill library 与 actor loop 后，只让有证据支持的 dependency edge 传播 relevance。 <!-- timefirst:delta=uncalibrated-graph-propagation-to-edge-confidence-calibration --></summary>

**问题。** 在同一个 frozen Skill1000 和 downstream actor loop 下，校准 graph edge 是否比已有 graph retriever 更能改善后续执行？ <!-- timefirst:question=test-edge-calibration-against-matched-graph-control -->

**证据。** 相比 **Graph-of-Skills control**，六模型 macro 的 ALFWorld success **80.01→86.79**，ScienceWorld score **72.62→80.50**；12 个 model×benchmark cell 中 environment steps 也都更少。 <!-- timefirst:evidence=matched-graph-retrieval-changes-later-execution~graph-of-skills-control -->

**限制。** Counterfactual probe 是 textual LLM judgment 而非环境 intervention；**construction costs are missing**，token、latency、美元、能耗与 repeated-seed uncertainty 也没有完整报告。 <!-- timefirst:caveat=textual-counterfactuals-and-incomplete-cost~construction-costs-are-missing -->

**地图。** `early_signal` — 单篇 calibrated graph 不足以建立 durable procedural-memory direction。

**链接。** [Paper](https://arxiv.org/abs/2608.25500) · [中文深读](papers/2026/2608.25500.zh.md) · [English note](papers/2026/2608.25500.md) · [Code](https://github.com/ZhiyuanLi218/Caskg)

</details>

<a id="entry-2608-25329"></a>
<details><summary><strong>2026-08-28 · HiPS</strong> · Personalized Memory-Policy Evolution <!-- timefirst:area=personalized-memory-policy-evolution --> — 共享 memory-management rule 与 persona-local delta 根据 task outcome 共同演化，而不是冻结为一个全局策略。 <!-- timefirst:delta=global-static-memory-policy-to-hierarchical-personalized-evolution --></summary>

**问题。** Memory-management policy 本身是否需要持久化的 shared 与 persona-local state；distribution shift 时到底是哪一层起作用？ <!-- timefirst:question=test-shared-versus-personalized-memory-policy-state -->

**证据。** PERMA 上完整 HiPS 为 **66.95/56.56/63.83/56.30**；去掉 **Cross-Level Rule Flow** 降到 **45.39/40.87/43.12/36.50**，去掉 persona gate 也出现明显 OOD 下降。 <!-- timefirst:evidence=matched-ablation-localizes-ood-personalization-value~cross-level-rule-flow -->

**限制。** Headline system comparison 部分使用 **different model backbones**；distillation、gating、rule flow、selection 与 RL 同时变化，完整 continual maintenance cost 也没有配平。 <!-- timefirst:caveat=heterogeneous-headline-baselines-and-coupled-policy-package~different-model-backbones -->

**地图。** `early_signal` — Personalized policy state 是强信号，但不足以改 durable map。

**链接。** [Paper](https://arxiv.org/abs/2608.25329) · [中文深读](papers/2026/2608.25329.zh.md) · [English note](papers/2026/2608.25329.md)

</details>

<a id="entry-2608-25553"></a>
<details><summary><strong>2026-08-28 · Stale Constraints</strong> · Freshness-Verification Allocation <!-- timefirst:area=freshness-verification-allocation --> — Provenance 即使正确，budgeted consumer 若没有检查能暴露 supersession 的路径，旧 constraint 仍会继续伤害行为。 <!-- timefirst:delta=provenance-availability-to-verification-allocation -->></summary>

**问题。** 在相同 two-record verification budget 下，stale-memory harm 来自 reasoning failure，还是 verification budget 花错了地方？ <!-- timefirst:question=isolate-verification-allocation-at-fixed-budget -->

**证据。** **forced-critical same-budget** intervention 把 current-record-consistent decision 从 **34/150→145/150**、**38/150→147/150**、**38/150→130/150**；修正后的 held-out robustness 为 **36/150→146/150**。 <!-- timefirst:evidence=fixed-budget-allocation-causally-changes-later-decisions~forced-critical-same-budget -->

**限制。** Intervention 中 **experimenter knows critical path**，archive 又把 supersession 压成一次 request 可发现；真实 storage/index/reconsolidation cost 没有进入实验。 <!-- timefirst:caveat=diagnostic-instrument-not-deployable-scheduler~experimenter-knows-critical-path -->

**地图。** `early_signal` — Freshness verification 成为独立 access decision，但单篇诊断研究不足以改图。

**链接。** [Paper](https://arxiv.org/abs/2608.25553) · [中文深读](papers/2026/2608.25553.zh.md) · [English note](papers/2026/2608.25553.md)

</details>

<a id="entry-2608-25570"></a>
<details><summary><strong>2026-08-28 · KOPE</strong> · Execution-Grounded Experience Graph <!-- timefirst:area=execution-grounded-experience-graph --> — Compiler、correctness 与 performance outcome 进入 persistent graph state，并在 bounded context 下影响后续优化决策。 <!-- timefirst:delta=discarded-optimization-trajectories-to-execution-grounded-experience-memory --></summary>

**问题。** Foundation model 与 workflow 固定时，decision→outcome graph memory 是否在 context construction 之外改变后续 kernel execution？ <!-- timefirst:question=test-experience-graph-under-fixed-workflow -->

**证据。** **graph memory ablation** 固定 GLM-5.2 workflow，full-suite pass rate **55.2%→84.6%**；412 个 paired valid timing case 上 graph-enabled variant 得到 **1.43×** geometric-mean speedup ratio。 <!-- timefirst:evidence=same-workflow-graph-memory-changes-executable-outcomes~graph-memory-ablation -->

**限制。** Active-context retrieval、compression、injection 仍然耦合；graph score 是 observational heuristic，不是 causal label，而且 **graph maintenance costs are missing**。 <!-- timefirst:caveat=integrated-context-package-and-incomplete-lifecycle-cost~graph-maintenance-costs-are-missing -->

**地图。** `early_signal` — Execution-grounded memory 很具体，但当前证据仍是 domain-specific 与 package-level。

**链接。** [Paper](https://arxiv.org/abs/2608.25570) · [中文深读](papers/2026/2608.25570.zh.md) · [English note](papers/2026/2608.25570.md)

</details>

<a id="entry-2608-25655"></a>
<details><summary><strong>2026-08-28 · TSIM</strong> · Episode-Integrity Reconstruction <!-- timefirst:area=episode-integrity-reconstruction --> — Interleaved chat 先重建为 coherent episode，再由 hierarchical retrieval 组装当前请求需要的 evidence。 <!-- timefirst:delta=flat-turn-retrieval-to-episode-integrity-reconstruction --></summary>

**问题。** 一个 thread 混入多个任务时，缺失的操作究竟是 turn relevance，还是重建当前请求真正接续的 prior episode？ <!-- timefirst:question=test-episode-reconstruction-before-retrieval -->

**证据。** Staged ablation 为 **26.2 standard RAG → 43.4 fixed-token direct → 55.5 semantic-drift direct → 74.2 full TSIM**；三个 answer backend 上 TSIM 比各自最强 baseline 高 **5.6–17.6 points**。 <!-- timefirst:evidence=staged-episode-organization-improves-later-answers~semantic-drift-direct-to-full-tsim -->

**限制。** **Segmentation summaries and routing** 仍耦合，SCALE-QA 与 TSIM 是 co-designed，construction/index/update/query lifecycle cost 也没有全面配平。 <!-- timefirst:caveat=package-attribution-and-codesigned-benchmark~segmentation-summaries-and-routing -->

**地图。** `early_signal` — Episode integrity 把 state localization 进一步具体化，但单个 co-designed package 不足以改图。

**链接。** [Paper](https://arxiv.org/abs/2608.25655) · [中文深读](papers/2026/2608.25655.zh.md) · [English note](papers/2026/2608.25655.md)

</details>

<a id="entry-2608-26005"></a>
<details><summary><strong>2026-08-28 · VoiceMem</strong> · Streaming Dual-Brain Memory <!-- timefirst:area=streaming-dual-brain-memory --> — Factual/entity state 与 affect/persona state 走不同 streaming path，并由可替换 backend 的 upper memory layer 统一路由。 <!-- timefirst:delta=single-text-memory-path-to-streaming-dual-state-contracts --></summary>

**问题。** Thin upper organization/routing layer 能否跨 interchangeable backend 改善 persistent conversational memory，同时满足 real-time retrieval budget？ <!-- timefirst:question=test-portable-upper-memory-layer-and-realtime-access -->

**证据。** 加入 **same-backend upper layer** 后，Mem0 **61.68→91.20**、LangMem **56.18→71.94**、Zep **62.93→85.85**；K=5 时报告 **430 memory tokens 和 134 ms retrieval**。 <!-- timefirst:evidence=upper-layer-improves-multiple-fixed-backends~same-backend-upper-layer -->

**限制。** Dual-brain package 同时改变 extraction、representation、routing、graph structure 与 streaming I/O；134 ms 是 **retrieval not end-to-end latency**，write/maintenance cost 也不完整。 <!-- timefirst:caveat=multi-stage-package-and-incomplete-write-cost~retrieval-not-end-to-end-latency -->

**地图。** `early_signal` — Factual 与 affect state contract 分离是一个信号，不足以建立 durable multimodal-memory node。

**链接。** [Paper](https://arxiv.org/abs/2608.26005) · [中文深读](papers/2026/2608.26005.zh.md) · [English note](papers/2026/2608.26005.md) · [Code](https://github.com/xzf-thu/VoiceMem) · [Project](https://xzf-thu.github.io/VoiceMem/)

</details>

'''

NEW_SIGNALS_EN = r'''- **`new_signal` · Skill edge confidence calibration.** Supports: [CaSKG](#entry-2608-25500); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (compare-calibrated-graph-against-strong-graph-control): treat propagating edges as a retrieval-policy variable rather than free structure. Exact synthesis time: `2026-08-28T00:53:00Z`. <!-- timefirst:direction key="skill-edge-confidence-calibration" state="new_signal" supports="2608.25500" confidence="medium" implication="compare-calibrated-graph-against-strong-graph-control" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Personalized memory policy evolution.** Supports: [HiPS](#entry-2608-25329); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate-shared-and-personal-memory-policy-state): match policy optimization while independently testing shared rules, persona deltas, migration, and maintenance cost. Exact synthesis time: `2026-08-28T00:53:00Z`. <!-- timefirst:direction key="personalized-memory-policy-evolution" state="new_signal" supports="2608.25329" confidence="high" implication="separate-shared-and-personal-memory-policy-state" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Stale memory verification allocation.** Supports: [Stale Constraints](#entry-2608-25553); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate-freshness-verification-from-relevance): evaluate which provenance path receives scarce audit budget before adding more retrieval compute. Exact synthesis time: `2026-08-28T00:53:00Z`. <!-- timefirst:direction key="stale-memory-verification-allocation" state="new_signal" supports="2608.25553" confidence="high" implication="separate-freshness-verification-from-relevance" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Execution grounded experience graph.** Supports: [KOPE](#entry-2608-25570); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (match-execution-grounded-memory-under-fixed-workflow): isolate persistent decision-outcome state from retrieval, compression, and injection while charging graph maintenance. Exact synthesis time: `2026-08-28T00:53:00Z`. <!-- timefirst:direction key="execution-grounded-experience-graph" state="new_signal" supports="2608.25570" confidence="high" implication="match-execution-grounded-memory-under-fixed-workflow" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Episode integrity reconstruction.** Supports: [TSIM](#entry-2608-25655); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate-episode-localization-from-retrieval-strength): independently toggle segmentation, summaries, routing, and evidence budget on naturally interleaved histories. Exact synthesis time: `2026-08-28T00:53:00Z`. <!-- timefirst:direction key="episode-integrity-reconstruction" state="new_signal" supports="2608.25655" confidence="medium" implication="separate-episode-localization-from-retrieval-strength" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Streaming dual brain memory.** Supports: [VoiceMem](#entry-2608-26005); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate-factual-affect-state-contracts-under-realtime-budget): match write cost and end-to-end conversational latency while swapping the same upper layer across backends. Exact synthesis time: `2026-08-28T00:53:00Z`. <!-- timefirst:direction key="streaming-dual-brain-memory" state="new_signal" supports="2608.26005" confidence="medium" implication="separate-factual-affect-state-contracts-under-realtime-budget" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->'''

NEW_SIGNALS_ZH = r'''- **`new_signal` · Skill edge confidence calibration。** 支撑：[CaSKG](#entry-2608-25500)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（compare calibrated graph against strong graph control）：把 propagating edge 当成 retrieval-policy variable，而不是免费结构。精确合成时间：`2026-08-28T00:53:00Z`。 <!-- timefirst:direction key="skill-edge-confidence-calibration" state="new_signal" supports="2608.25500" confidence="medium" implication="compare-calibrated-graph-against-strong-graph-control" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Personalized memory policy evolution。** 支撑：[HiPS](#entry-2608-25329)；置信度：**high**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate shared and personal memory policy state）：在匹配 policy optimization 后独立检验 shared rule、persona delta、migration 与 maintenance cost。精确合成时间：`2026-08-28T00:53:00Z`。 <!-- timefirst:direction key="personalized-memory-policy-evolution" state="new_signal" supports="2608.25329" confidence="high" implication="separate-shared-and-personal-memory-policy-state" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Stale memory verification allocation。** 支撑：[Stale Constraints](#entry-2608-25553)；置信度：**high**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate freshness verification from relevance）：先测 scarce audit budget 到底检查哪个 provenance path，再讨论增加 retrieval compute。精确合成时间：`2026-08-28T00:53:00Z`。 <!-- timefirst:direction key="stale-memory-verification-allocation" state="new_signal" supports="2608.25553" confidence="high" implication="separate-freshness-verification-from-relevance" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Execution grounded experience graph。** 支撑：[KOPE](#entry-2608-25570)；置信度：**high**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（match execution grounded memory under fixed workflow）：把 persistent decision-outcome state 与 retrieval、compression、injection 分开，同时计入 graph maintenance。精确合成时间：`2026-08-28T00:53:00Z`。 <!-- timefirst:direction key="execution-grounded-experience-graph" state="new_signal" supports="2608.25570" confidence="high" implication="match-execution-grounded-memory-under-fixed-workflow" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Episode integrity reconstruction。** 支撑：[TSIM](#entry-2608-25655)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate episode localization from retrieval strength）：在 naturally interleaved history 上独立开关 segmentation、summary、routing 与 evidence budget。精确合成时间：`2026-08-28T00:53:00Z`。 <!-- timefirst:direction key="episode-integrity-reconstruction" state="new_signal" supports="2608.25655" confidence="medium" implication="separate-episode-localization-from-retrieval-strength" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->

- **`new_signal` · Streaming dual brain memory。** 支撑：[VoiceMem](#entry-2608-26005)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate factual affect state contracts under realtime budget）：匹配 write cost 与 end-to-end conversational latency，并在相同 backend 上交换 upper layer。精确合成时间：`2026-08-28T00:53:00Z`。 <!-- timefirst:direction key="streaming-dual-brain-memory" state="new_signal" supports="2608.26005" confidence="medium" implication="separate-factual-affect-state-contracts-under-realtime-budget" timing="radar_published_at" synthesized="2026-08-28T00:53:00Z" prior="none" -->'''


def record_times():
    out = {}
    for p in (ROOT / "data" / "papers").glob("*.json"):
        try:
            r = json.loads(p.read_text())
        except Exception:
            continue
        ts = r.get("radar_published_at")
        if r.get("time_provenance") == "native_v2" and isinstance(ts, str):
            try:
                out[str(r["id"])] = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            except Exception:
                pass
    return out


def filter_direction_blocks(section: str, window: tuple[date, date]) -> str:
    lines = section.splitlines()
    first = next((i for i, line in enumerate(lines) if re.match(r"^- \*\*`", line)), len(lines))
    prefix = lines[:first]
    blocks = []
    starts = [i for i, line in enumerate(lines) if re.match(r"^- \*\*`", line)]
    times = record_times()
    cutoff = datetime.fromisoformat(CUTOFF.replace("Z", "+00:00"))
    for j, s in enumerate(starts):
        e = starts[j + 1] if j + 1 < len(starts) else len(lines)
        block = "\n".join(lines[s:e]).strip()
        m = re.search(r'supports="([^"]+)"', block)
        if not m:
            continue
        ids = [] if m.group(1) == "none" else [x.strip() for x in m.group(1).split(",") if x.strip()]
        ok = True
        for identity in ids:
            t = times.get(identity)
            if t is None or not (window[0] <= t.date() <= window[1]) or t > cutoff:
                ok = False
                break
        if ok:
            block = block.replace("2026-08-27T00:34:29Z", CUTOFF)
            blocks.append(block)
    return "\n".join(prefix).rstrip() + "\n\n" + "\n\n".join(blocks)


def update_readme(path: Path, entries: str, signals: str, zh: bool):
    text = path.read_text()
    text = text.replace("Last updated: **2026-08-27**", "Last updated: **2026-08-28**", 1)
    marker = '<a id="entry-2608-24876"></a>'
    if '<a id="entry-2608-25500"></a>' not in text:
        text = text.replace(marker, entries + marker, 1)

    m7 = '<a id="last-7-days"></a>'
    m30 = '<a id="last-30-days"></a>'
    mf = '<a id="field-map"></a>'
    i7, i30, iff = text.index(m7), text.index(m30), text.index(mf)
    s7 = text[i7:i30]
    s30 = text[i30:iff]
    s7 = filter_direction_blocks(s7, WIN7)
    s30 = filter_direction_blocks(s30, WIN30)
    if zh:
        s7 = re.sub(r"### 过去 7 天：[^\n]+", "### 过去 7 天：2026-08-22—2026-08-28", s7, count=1)
        s30 = re.sub(r"### 过去 30 天：[^\n]+", "### 过去 30 天：2026-07-30—2026-08-28", s30, count=1)
    else:
        s7 = re.sub(r"### Last 7 days: [^\n]+", "### Last 7 days: 2026-08-22—2026-08-28", s7, count=1)
        s30 = re.sub(r"### Last 30 days: [^\n]+", "### Last 30 days: 2026-07-30—2026-08-28", s30, count=1)
    s7 = s7.rstrip() + "\n\n" + signals + "\n\n"
    s30 = s30.rstrip() + "\n\n" + signals + "\n\n"
    text = text[:i7] + s7 + s30 + text[iff:]
    path.write_text(text)


def update_categories_and_library():
    en = ROOT / "categories" / "retrieval-access.md"
    txt = en.read_text()
    if "[CaSKG](../papers/2026/2608.25500.md)" not in txt:
        txt = txt.replace("## Current argument\n", "## Current argument\n\n**CaSKG adds an important structured-control result:** with the same frozen skill library and downstream actor, edge-confidence calibration beats an existing graph retriever; the graph is an amplifying access policy, not free context.\n", 1)
        row = "| 2026-08-26 | [CaSKG](../papers/2026/2608.25500.md) | `procedural` `graph` `structured` `general-agent` | 4/5 | Edge-confidence calibration beats GoS under a frozen skill library and unchanged actor loop; construction/serving cost and statistical uncertainty remain incomplete. |\n"
        pos = txt.index("| 2026-08-24 |")
        txt = txt[:pos] + row + txt[pos:]
        en.write_text(txt)

    zh = ROOT / "categories" / "zh" / "retrieval-access.md"
    txt = zh.read_text()
    if "CaSKG" not in txt:
        txt = txt.replace("## 当前判断\n", "## 当前判断\n\n**CaSKG 把 graph access 本身拆成“有结构”和“可信结构”。** 在同一 frozen Skill1000 与同一 downstream loop 下，calibrated graph 击败 GoS；错误 edge 会放大错误 relevance，因此 relation quality 是一等 access-policy 变量。\n", 1)
        zh.write_text(txt)

    for rel, heading, block in [
        ("library/README.en.md", "### Outcome contrast", "### Full library / vector → graph propagation → edge-confidence calibration\n\n[Optimal Skill Selection](../papers/2026/2608.19993.md) / [SkillGate](../papers/2026/2608.18852.md) → [CaSKG](../papers/2026/2608.25500.md)\n\nProcedural-memory access is not only which skill is relevant. Set complementarity, learned exposure, and relation propagation are distinct mechanisms. CaSKG shows graph retrieval can underperform full-library exposure, so propagating edges should be treated as risky access decisions and compared under full lifecycle cost.\n\n"),
        ("library/README.md", "### Outcome contrast", "### Full library / Vector → Graph propagation → Edge-confidence calibration\n\n[Optimal Skill Selection](../papers/2026/2608.19993.zh.md) / [SkillGate](../papers/2026/2608.18852.zh.md) → [CaSKG](../papers/2026/2608.25500.zh.md)\n\nProcedural-memory access 不只是“召回哪一个 skill”。集合互补性、learned exposure 与 relation propagation 是不同机制。CaSKG 说明 graph retrieval 甚至可能差于 full-library exposure，因此 propagating edge 应作为有风险的 access decision，并在完整 lifecycle cost 下比较。\n\n"),
    ]:
        p = ROOT / rel
        txt = p.read_text()
        if "CaSKG" not in txt:
            txt = txt.replace(heading, block + heading, 1)
            p.write_text(txt)


def roll_contract_dates():
    files = [
        ROOT / "scripts" / "validate_reading.py",
        ROOT / "tests" / "test_memory_v2_contract.py",
        ROOT / "tests" / "test_validate_reading.py",
    ]
    replacements = [
        ("2026-08-27T00:34:29Z", CUTOFF),
        ("(date(2026, 8, 21), date(2026, 8, 27))", "(date(2026, 8, 22), date(2026, 8, 28))"),
        ("(date(2026, 7, 29), date(2026, 8, 27))", "(date(2026, 7, 30), date(2026, 8, 28))"),
        ("2026-08-21—2026-08-27", "2026-08-22—2026-08-28"),
        ("2026-07-29—2026-08-27", "2026-07-30—2026-08-28"),
        ("2026-08-21T01:18:00Z", "2026-08-22T01:18:00Z"),
        ("2026-08-27T01:00:00Z", "2026-08-28T01:00:00Z"),
    ]
    for p in files:
        txt = p.read_text()
        for old, new in replacements:
            txt = txt.replace(old, new)
        p.write_text(txt)


update_readme(ROOT / "README.en.md", EN_ENTRIES, NEW_SIGNALS_EN, False)
update_readme(ROOT / "README.md", ZH_ENTRIES, NEW_SIGNALS_ZH, True)
update_categories_and_library()
roll_contract_dates()
print("rolled Agent Memory public projection to", CUTOFF)
