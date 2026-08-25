# Agent Memory Radar

**中文** | [English](README.en.md)

*面向 LLM 与多模态 Agent 的长期记忆研究地图。*

**Radar Family：** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 秒：最新时间线](#timeline) · [3 分钟：7/30 天变化](#periods) · [5 分钟：领域地图](#field-map) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library)

最后更新：**2026-08-25**

<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>
## Latest Timeline：最新接受的 Agent Memory 证据

> **迁移说明：** 这些现有记录没有可靠保存历史 Radar 接受时间，因此暂按论文原始发布日期排序；v2 切换后的新记录统一使用 `radar_published_at`，不得把论文日期伪装成 Radar 接受时间。

<a id="entry-2608-21230"></a>
<details><summary><strong>2026-08-25 · Utility Under Attack</strong> · 来源排序的效用边界 <!-- timefirst:area=provenance-ranking-utility-frontier --> — 来源权重必须在抵抗污染的同时保留低信任渠道中的合法证据。 <!-- timefirst:delta=source-trust-to-measured-utility-frontier --></summary>

**问题。** 加法式 provenance weight 能否压制持久 poison，同时保留 untrusted channel 中的 answer-bearing evidence？ <!-- timefirst:question=preserve-useful-evidence-while-suppressing-poison -->

**证据。** 这组污染使 clean accuracy **.850→.300**；shipped weight 仅到 **.317**，stronger weight 恢复到 **.475**，却令`genuine untrusted evidence recall` **99.17%→0%**、accuracy **.8583→.0417**。 <!-- timefirst:evidence=ranking-weight-changes-later-answers-and-evidence-recall~genuine-untrusted-evidence-recall -->

**限制。** 攻击针对具体 query，label 被假设为正确，且 `bounded source occupancy is proposed but not tested`；单一 stack 与两个权重不能证明 provenance 普遍失效。 <!-- timefirst:caveat=targeted-attack-and-constructed-provenance-extremes~bounded-source-occupancy-is-proposed-but-not-tested -->

**地图。** `early_signal` — 来源排序形成可测的检索效用边界，但单一实现不足以修改长期地图。

**链接。** [论文](https://arxiv.org/abs/2608.21230) · [中文深读](papers/2026/2608.21230.zh.md) · [英文深读](papers/2026/2608.21230.md)

</details>

<a id="entry-2608-20664"></a>
<details><summary><strong>2026-08-25 · DreamBench-SWE</strong> · 可执行的记忆卫生 <!-- timefirst:area=executable-memory-hygiene --> — 在给 hygiene mechanism 记功前，早期项目状态必须改变后续可执行 patch。 <!-- timefirst:delta=memory-score-to-executable-later-behavior --></summary>

**问题。** 持久项目状态是否改变后续软件行为？Typed consolidation 与 sleep 能否击败强 verbatim archive？ <!-- timefirst:question=test-executable-memory-and-mechanism-attribution -->

**证据。** 结果显示，no-memory 通过 **21/180**、verbatim **82/180**、hybrid **83/180**、literal Mem0 **97/180**；持久状态有效，但 `all preregistered hybrid versus verbatim raw typed tests fail to reject`。 <!-- timefirst:evidence=earlier-state-changes-executable-patches-with-null-mechanism-tests~all-preregistered-hybrid-versus-verbatim-raw-typed-tests-fail-to-reject -->

**限制。** 这套评测主要由人工样例与精确回忆任务构成；维护开销悬殊（`hybrid consumes 174.205m vs 2.209m tokens`），外部系统的机制对照又因合规检查失败无法运行。 <!-- timefirst:caveat=authored-recall-fixtures-and-null-mechanism-attribution~hybrid-consumes-174.205m-vs-2.209m-tokens -->

**地图。** `early_signal` — 可执行行为提高了评估门槛，但这套参考方案尚未获得长期机制归因。

**链接。** [论文](https://arxiv.org/abs/2608.20664) · [中文深读](papers/2026/2608.20664.zh.md) · [英文深读](papers/2026/2608.20664.md)

</details>

<a id="entry-2608-20631"></a>
<details><summary><strong>2026-08-25 · Weighted Memory Tree</strong> · 选择驱动的工作记忆 <!-- timefirst:area=selection-driven-working-memory --> — 后续行动之前，保留策略决定哪些实时执行分支继续活跃。 <!-- timefirst:delta=linear-history-to-active-retention-control --></summary>

**问题。** 任务树能否比线性执行历史更有效地选择、折叠、衰减与抑制工作状态？ <!-- timefirst:question=select-active-execution-state-before-later-actions -->

**证据。** 三个模型上，`coupled package reports` GAIA-Text 平均 **+9.97pp** accuracy、**−32.8%** prompt tokens；stored view 会改变 episode 内后续行动。 <!-- timefirst:evidence=package-improves-gaia-and-reduces-prompt-tokens~coupled-package-reports -->

**限制。** 每道题都新建 tree，组件未被隔离，ablation 会反转，且 `cross session persistence is not evaluated`；没有 seed、uncertainty 或 artifact。 <!-- timefirst:caveat=within-task-package-only-and-missing-uncertainty~cross-session-persistence-is-not-evaluated -->

**地图。** `early_signal` — 在单次任务内，活跃保留可能先于检索，但这项 3/5 的整套结果不足以增加长期记忆节点。

**链接。** [论文](https://arxiv.org/abs/2608.20631) · [中文深读](papers/2026/2608.20631.zh.md) · [英文深读](papers/2026/2608.20631.md)

</details>

<a id="entry-2608-20274"></a>
<details><summary><strong>2026-08-25 · Break It Down, Pass It On</strong> · 技能粒度与迁移 <!-- timefirst:area=skill-granularity-transfer --> — 当写入单元匹配后续复用时，程序性记忆可从平均伤害转为小幅收益。 <!-- timefirst:delta=whole-task-skills-to-subtask-transfer-units --></summary>

**问题。** 按子任务写入持久技能，是否比整任务级的文本或代码记忆更稳定地迁移？ <!-- timefirst:question=match-skill-write-granularity-to-later-consumer -->

**证据。** 结果显示，任务级 no-memory/text/code 为 **22.1/20.9/18.0%**，子任务级为 **24.8/26.7/25.3%**；`two model frozen library replay` 报告子任务技能 **+9.9pp**。 <!-- timefirst:evidence=subtask-skills-change-later-task-success~two-model-frozen-library-replay -->

**限制。** 两类架构的写入次数、查询次数与来源轨迹不同；许多模型和领域切片反转，区间也重叠，且 `full induction and maintenance cost is missing`。 <!-- timefirst:caveat=heterogeneous-effects-and-coupled-agent-architectures~full-induction-and-maintenance-cost-is-missing -->

**地图。** `early_signal` — 写入粒度是因果设计问题，但一项异质研究无法建立普遍的子任务优势。

**链接。** [论文](https://arxiv.org/abs/2608.20274) · [中文深读](papers/2026/2608.20274.zh.md) · [英文深读](papers/2026/2608.20274.md)

</details>

<a id="entry-2608-19993"></a>
<details><summary><strong>2026-08-25 · Optimal Skill Selection</strong> · 有预算的技能集合选择 <!-- timefirst:area=budgeted-skill-set-selection --> — 技能访问是受上下文成本约束的集合效用，而不是彼此独立的 top-k relevance。 <!-- timefirst:delta=independent-skill-ranking-to-budgeted-set-value --></summary>

**问题。** 选择器能否在固定 token budget 下刻画互补、冗余与有害的技能组合？ <!-- timefirst:question=select-complementary-skill-sets-under-budget -->

**证据。** 受控实验从 `controlled case moves` **0% single skill→93% complementary pair→56% 加入 irrelevant procedure**；BPS 达到 **.73**，released alternative 为 **.20–.52**，且少用 28% tokens。 <!-- timefirst:evidence=skill-set-composition-causally-changes-execution~controlled-case-moves -->

**限制。** 任务经过筛选，所有单能力组合都必须失败；BPS 从 **63,596 次执行**中学习，对照方法却没有配平监督，且 `training cost may dominate saved context`。 <!-- timefirst:caveat=capability-gated-benchmark-and-unmatched-supervision~training-cost-may-dominate-saved-context -->

**地图。** `early_signal` — 集合效用不同于单项相关性，但单一、强监督的固定代码库不会改变领域地图。

**链接。** [论文](https://arxiv.org/abs/2608.19993) · [中文深读](papers/2026/2608.19993.zh.md) · [英文深读](papers/2026/2608.19993.md)

</details>

<a id="entry-2608-20202"></a>
<details><summary><strong>2026-08-24 · MemTrapBench</strong> · 使用方记忆伤害 <!-- timefirst:area=consumer-side-memory-harm --> — 相关历史在进入当前 Actor 前，仍可能需要适用性 Gate。 <!-- timefirst:delta=relevant-memory-to-applicability-gated-use --></summary>

**问题。** 当当前任务不再需要或支持过去的 reasoning pattern 时，语义相关的 memory 是否会因果改变并损害后续回答？ <!-- timefirst:question=test-harm-from-inapplicable-memory-use -->

**证据。** 在 `adversarial stress test` 上，Gemini/Qwen 的 no-memory 得分为 **85.16 / 81.83**，最强 memory arm 为 **71.17 / 70.99**；有限的 `trap free history controls` 先保持 Task Boundary 表现，再由 trap semantics 让分数从 **94.39→31.05**。 <!-- timefirst:evidence=trap-semantics-change-later-answers~trap-free-history-controls -->

**限制。** 每个 query 都可独立解答，prior dialogue 则专门生成 trap；`taxonomy matched prompt mitigation` 没有 uncertainty、neutral-prompt control、`framework cost matching` 或现实 prevalence 证据。 <!-- timefirst:caveat=adversarial-construction-and-missing-controls~taxonomy-matched-prompt-mitigation -->

**地图。** `early_signal` — 检索后的 applicability 成为可测的 consumer boundary；但一篇 work-in-progress synthetic benchmark 不能说明 memory 普遍有害，也不修改长期地图。

**链接。** [论文](https://arxiv.org/abs/2608.20202) · [中文深读](papers/2026/2608.20202.zh.md) · [英文深读](papers/2026/2608.20202.md)

</details>

<a id="entry-2608-19652"></a>
<details><summary><strong>2026-08-24 · StateMemBench / StateMem</strong> · 演化状态解析 <!-- timefirst:area=evolving-state-resolution --> — 历史被取回后还要解析出当前有效状态，不能直接沿用已取代的值。 <!-- timefirst:delta=stored-history-to-operative-state-resolution --></summary>

**问题。** 多 session 更新后，memory 能否区分当前值与 superseded value，并重新计算 dependent decision？ <!-- timefirst:question=resolve-supersession-before-current-action -->

**证据。** 在 DeepSeek 上，persistent StateMem 为 **0.363**，Dense 为 **0.205**；supersession 让分数 **0.174→0.298**。最强的 `matched answer time tracing` 相对 generic-summary control 增加 **15.0–31.7pp**，但需要读取 full transcript。 <!-- timefirst:evidence=supersession-and-tracing-improve-current-state~matched-answer-time-tracing -->

**限制。** 这套 benchmark 与方法的 policy family 对齐；移除 dependency propagation 反而 **0.363→0.373**，而且 `persistent ingestion costs 165 to 600 calls`，完整 lifecycle cost 未报告。 <!-- timefirst:caveat=aligned-benchmark-and-large-ingestion-cost~persistent-ingestion-costs-165-to-600-calls -->

**地图。** `early_signal` — 状态取代与 consumer-side resolution 不同于 recall；一项 synthetic、single-run 研究尚不足以增加长期 Field Map 节点。

**链接。** [论文](https://arxiv.org/abs/2608.19652) · [中文深读](papers/2026/2608.19652.zh.md) · [英文深读](papers/2026/2608.19652.md)

</details>

<a id="entry-2608-19564"></a>
<details><summary><strong>2026-08-24 · Remember, Verify, or Ask?</strong> · 记忆承诺治理 <!-- timefirst:area=memory-commitment-governance --> — 候选信息在持久提交前必须经过 authority 与 scope 判断。 <!-- timefirst:delta=candidate-information-to-authority-aware-commitment --></summary>

**问题。** 一条 acquired update 在影响未来状态前，应持久写入、仅当前使用、向世界核验，还是向用户澄清？ <!-- timefirst:question=choose-authority-aware-commitment-action -->

**证据。** 在 `Qwen few-shot accuracy` 从 **0.557→0.771** 后，clarification recall 仍只有 **0.333**；policy 把 erroneous persistence 从 **0.243→0.100**，而 Qwen 的 `label tool agreement` 只有 **0.229**。 <!-- timefirst:evidence=prompts-reshape-commitment-action-selection~label-tool-agreement -->

**限制。** 这项 `70-item synthetic test` 含很强的 category signal，而且 `selected actions are not executed`；没有真实 write、later retrieval、downstream outcome 或完整成本。 <!-- timefirst:caveat=synthetic-rubric-and-nonexecuted-actions~selected-actions-are-not-executed -->

**地图。** `early_signal` — 候选承诺是 storage 前的治理边界；该 benchmark signal 不证明 persistent-memory policy 已改善。

**链接。** [论文](https://arxiv.org/abs/2608.19564) · [中文深读](papers/2026/2608.19564.zh.md) · [英文深读](papers/2026/2608.19564.md)

</details>

<a id="entry-2608-19197"></a>
<details><summary><strong>2026-08-21 · SPADE</strong> · 训练侧环境记忆 <!-- timefirst:area=training-side-environment-memory --> — 有界 buffer 把过去的可执行环境提供给后续课程设计。 <!-- timefirst:delta=static-designer-to-retrieved-environment-history --></summary>

**问题。** 在 designer、corpus grounding 与 GRPO recipe 保持不变时，跨 episode 的环境记忆是否优于不使用 memory 的自适应训练循环？ <!-- timefirst:question=test-environment-memory-in-training-loop -->

**证据。** 完整配置所选 checkpoint 的平均分为 **58.3**，官方无记忆 launcher 为 **53.2**，形成 `selected suite memory gap`；AIME 2026 则从无记忆配置的 **75.0** 降至 **74.4**。 <!-- timefirst:evidence=memory-path-package-ablation~selected-suite-memory-gap -->

**限制。** 每个配置只有一次 run，并采用 `suite selected checkpoints`；移除 memory 也会移除 demonstration tokens，released sampler 还没有显式 seed。 <!-- timefirst:caveat=single-run-and-selection-bias~suite-selected-checkpoints -->

**地图。** `early_signal` — 训练侧持久状态可以影响后续经验生成，但一套共同适应的 package 不能单独证明 regret retrieval、FIFO retention 或稳定方向。

**链接。** [论文](https://arxiv.org/abs/2608.19197) · [中文深读](papers/2026/2608.19197.zh.md) · [英文深读](papers/2026/2608.19197.md)

</details>

<a id="entry-2608-18704"></a>
<details><summary><strong>2026-08-21 · MemFuse</strong> · 多源证据访问 <!-- timefirst:area=multi-source-evidence-access --> — 保留来源的融合记忆，只有配合补全碎片证据的访问循环才产生价值。 <!-- timefirst:delta=provenance-plus-evidence-completion --></summary>

**问题。** 记忆能否拼合分散在多源中的信息，同时返回原始支撑？最近的有界对照使用同一事件流和读取模型，并把最终证据限制为 20 条。 <!-- timefirst:question=fuse-fragments-with-source-traceability -->

**证据。** 总体得分达到 **0.4659 / 0.4574 / 0.4698**，但 `agentic retrieval ablation` 会损失 **0.1036**，明显大于移除 graph/fusion 的总体影响。 <!-- timefirst:evidence=overall-gain-dominated-by-agentic-access~agentic-retrieval-ablation -->

**限制。** 基准为合成数据，且 `Qwen ingestion tokens 达 93.27M`；Gemini 设置仍由 long context 胜出，也没有生命周期匹配的 `stateful raw-search control`。 <!-- timefirst:caveat=synthetic-benchmark-and-high-ingestion-cost~qwen-ingestion-tokens -->

**地图。** `early_signal` — 该结果把来源保真的组织与证据补全访问拆成两个阶段；单套 package 不足以建立持久的 graph-memory 方向。

**链接。** [论文](https://arxiv.org/abs/2608.18704) · [中文深读](papers/2026/2608.18704.zh.md) · [英文深读](papers/2026/2608.18704.md)

</details>

<a id="entry-2608-18719"></a>
<details><summary><strong>2026-08-21 · Competence, Not Accuracy</strong> · 技能更新治理 <!-- timefirst:area=skill-update-governance --> — 技能准入的 Judge gate 在提交持久 edit 前，必须证明同题判别能力。 <!-- timefirst:delta=benchmark-accuracy-to-gate-discriminability --></summary>

**问题。** 一个不看参考答案的 judge 能否在自己将要治理的候选分布上区分正确与错误尝试？最近的对照在同一批 SkillOpt 轨迹上比较边际 AUC 与同题 AUC。 <!-- timefirst:question=qualify-judge-before-skill-commit -->

**证据。** 去除题目难度混杂后，Factual-QA AUC 从 **0.855 降至 0.735**；`research math within-question AUC` 为接近随机的 **0.489**。 <!-- timefirst:evidence=within-question-audit-reveals-difficulty-confound~research-math-within-question -->

**限制。** 能力超过 floor 只是必要条件；`open ended judge transfer` 尚未验证，早期 bare-letter probe 还曾制造 false null。 <!-- timefirst:caveat=diagnostic-sensitive-and-open-tasks-untested~open-ended-judge-transfer -->

**地图。** `early_signal` — 准入边界新增了部署前诊断，但单个 gate study 不改写持久治理结论。

**链接。** [论文](https://arxiv.org/abs/2608.18719) · [中文深读](papers/2026/2608.18719.zh.md) · [英文深读](papers/2026/2608.18719.md)

</details>

<a id="entry-2608-18852"></a>
<details><summary><strong>2026-08-21 · SkillGate</strong> · 程序性记忆访问 <!-- timefirst:area=procedural-memory-access --> — 带 Oracle 监督的局部选择通道改变 episode 中途暴露哪个固定 skill。 <!-- timefirst:delta=outcome-only-to-oracle-local-selector-channel --></summary>

**问题。** 带 Oracle 监督的局部选择通道能否比 outcome-only training 更好地训练早期 skill-read 动作？最近的运行固定初始化、数据、100 步与超参数，但同时改变三项 loss design。 <!-- timefirst:question=test-oracle-local-selector-supervision -->

**证据。** 成功率从 **47.0% 升至 53.2%**，oracle exposure 从 **54.3% 升至 83.9%**，misleading exposure 从 **69.6% 降至 21.8%**；`oracle local selector channel` 同时包含特权 utility、read-call masking 与 selector-mass normalization。 <!-- timefirst:evidence=oracle-channel-changes-skill-exposure~oracle-local-selector-channel -->

**限制。** 每个设置只有一次 16-H800 run；`verified single oracle identity` 不能代表开放、持续变化或组合式 skill library。 <!-- timefirst:caveat=single-run-and-oracle-dependent-training~verified-single-oracle -->

**地图。** `early_signal` — 技能是否存在与受监督 access policy 是否会用它是不同阶段；单次训练不能建立趋势，也不能单独归因 credit location。

**链接。** [论文](https://arxiv.org/abs/2608.18852) · [中文深读](papers/2026/2608.18852.zh.md) · [英文深读](papers/2026/2608.18852.md)

</details>

<a id="entry-2608-19013"></a>
<details><summary><strong>2026-08-21 · Harness Continual Learning</strong> · 持续 Harness 状态演化 <!-- timefirst:area=harness-state-evolution --> — 候选 harness 只有通过当前收益、历史保留与 validity 检查才会提交。 <!-- timefirst:delta=unbounded-updates-to-guarded-harness-commit --></summary>

**问题。** 冻结模型的 Agent 如何更新 memory、interface、capability map 与 router，又不静默遗忘旧行为？最近的治理对照扫描 historical-loss bound。 <!-- timefirst:question=guard-nonparametric-agent-state-commit -->

**证据。** 无限制 commit 最终为 **60.13**，低于 `b=1` 的 **63.46**；`memory update ablation` 为 **62.28 / 0.83 forgetting**，Full HCL 为 **63.41 / 0.45**。 <!-- timefirst:evidence=retention-bound-and-memory-stage-witness~memory-update-ablation -->

**限制。** 四个 harness component 共同适应，因此 `package gain not memory gain`；historical anchors 不完备，也未报告完整 lifecycle cost。 <!-- timefirst:caveat=coadaptive-package-and-incomplete-anchors~package-gain-not-memory -->

**地图。** `early_signal` — 提交边界已超出 memory store，但单套 packaged system 不足以建立持久 evolution architecture。

**链接。** [论文](https://arxiv.org/abs/2608.19013) · [中文深读](papers/2026/2608.19013.zh.md) · [英文深读](papers/2026/2608.19013.md)

</details>

<a id="entry-2608-17911"></a>
<details><summary><strong>2026-08-18 · CABLE</strong> · 检索与访问 <!-- timefirst:area=retrieval-access --> — 存储链接只有能触达宿主检索器遗漏的证据，才值得付出额外成本。 <!-- timefirst:delta=structure-as-retriever-complement --></summary>

**问题。** 在最终证据条数不变时，记忆中预存的链接能否找到同一宿主检索器漏掉的证据？最接近的生命周期对照沿用 A-MEM 宿主，并固定证据条数。 <!-- timefirst:question=links-reach-host-missed-evidence -->

**证据。** 在同一 A-MEM 宿主和最终证据预算下（`matched A-MEM host budget`），LoCoMo Qwen3.5 从 **71.23 升至 74.81**，MA-LongMemEval Qwen 从 **59.33 升至 65.33**。 <!-- timefirst:evidence=same-host-budget-locomo-and-ma-longmemeval-gains~matched-a-mem-host-budget -->

**限制。** 时序推理子集（`temporal-reasoning slices`）反而下降；写入阶段额外的查询生成与验证，也未与强在线搜索对照做全生命周期成本匹配。 <!-- timefirst:caveat=temporal-regression-and-unmatched-ingestion-cost~temporal-reasoning-slices -->

**地图。** `early_signal` — 这项结果落在组织 → 访问边界：预存关系只有改变宿主接口的证据可达性才有价值；单篇论文不改写持久地图。

**链接。** [论文](https://arxiv.org/abs/2608.17911) · [中文深读](papers/2026/2608.17911.zh.md) · [英文深读](papers/2026/2608.17911.md)

</details>

<a id="entry-2608-17756"></a>
<details><summary><strong>2026-08-18 · D²ACCI</strong> · 评估与治理 <!-- timefirst:area=evaluation-governance --> — 记忆功能不再凭 aggregate score 晋级，而要同时通过 paired evidence、protected slice 与 stage-level promotion gate。 <!-- timefirst:delta=aggregate-score-to-promotion-contract --></summary>

**问题。** 一项记忆功能应如何在阶段归因成立、受保护子集不退化时才获准上线？最接近的对照是在同一运行环境中成对比较基线与候选功能。 <!-- timefirst:question=promotion-under-stage-and-non-regression-evidence -->

**证据。** 补充信息抽取、会话记忆检索与 Forget Guard 均出现显著的成对增益；LoCoMo 和 LongMemEval 上的 `BM25/RRF null result` 仍不显著，只进入监控标记。 <!-- timefirst:evidence=paired-gains-and-bm25-rrf-null-results~bm25-rrf-null-result -->

**限制。** 这组结果来自诊断协议的部署证据，并非新记忆架构的独立效果；结论仍受 `trace coverage dependence`、评估器和上线阈值约束。 <!-- timefirst:caveat=protocol-evidence-not-new-architecture~trace-coverage-dependence -->

**地图。** `early_signal` — 这项工作落在治理边界：无显著差异的结果和无回归要求开始约束功能上线，但一套协议不足以重写地图。

**链接。** [论文](https://arxiv.org/abs/2608.17756) · [中文深读](papers/2026/2608.17756.zh.md) · [英文深读](papers/2026/2608.17756.md)

</details>

<a id="entry-2608-17587"></a>
<details><summary><strong>2026-08-18 · WER</strong> · 记忆学习与演化 <!-- timefirst:area=memory-learning-evolution --> — 执行结果用于训练 skill-writer policy，而不只是触发又一次 inference-time reflection。 <!-- timefirst:delta=execution-feedback-trains-writer-policy --></summary>

**问题。** 程序性记忆的技能编写策略能否从冻结执行器的成功与失败轨迹中学习，而不只是反思已有技能文本？最接近的对照固定了优化器骨干和细化流程。 <!-- timefirst:question=writer-policy-learning-from-execution -->

**证据。** 在同一 Qwen3-4B 优化器和细化流程下，BFCL v4 从 **67.28 升至 76.63**，tau2 从 **40.43 升至 50.72**；额外增加一轮时出现 `extra refinement regression`。 <!-- timefirst:evidence=same-backbone-gains-then-extra-refinement-regresses~extra-refinement-regression -->

**限制。** 主要替代解释是更昂贵的执行采样和 `programmatic verifier cost`；可靠验证器是否可得、成本多高，决定这套编写策略学习循环能否迁移。 <!-- timefirst:caveat=rollout-and-verifier-cost~programmatic-verifier-cost -->

**地图。** `early_signal` — 这项结果落在写入 / 更新边界：学得的编写策略成为持久程序状态，但单篇论文不能建立稳定方向。

**链接。** [论文](https://arxiv.org/abs/2608.17587) · [中文深读](papers/2026/2608.17587.zh.md) · [英文深读](papers/2026/2608.17587.md)

</details>

<a id="entry-2608-17588"></a>
<details><summary><strong>2026-08-18 · TRUSS</strong> · 程序性记忆治理 <!-- timefirst:area=procedural-memory-governance --> — 生成的 skill 必须成为可执行 artifact，并在持久化前通过 static 与 shadow-execution certification。 <!-- timefirst:delta=generated-text-to-certified-artifact --></summary>

**问题。** 生成的技能在进入持久程序性记忆前，能否通过静态约束、受控影子执行和溯源记录得到可靠认证？最接近的对照是在同一批 SkillInject 产物上使用 LLM 检查器与静态检查器。 <!-- timefirst:question=certify-generated-skills-before-persistence -->

**证据。** 在同一批 SkillInject 产物上，LLM 检查器达到 **44.64% precision / 19.05% recall**，静态检查器达到 **81.55 / 94.05**，完整 TRUSS 认证达到 **100 / 100**（`full TRUSS certification`）。 <!-- timefirst:evidence=matched-skillinject-certification-results~full-truss-certification -->

**限制。** 这项增益属于整套 `executor-dependent package`，不能把结果单独归因于技能表示或某一个检查器。 <!-- timefirst:caveat=package-and-executor-confounding~executor-dependent-package -->

**地图。** `early_signal` — 这项结果落在写入 → 上线 / 治理边界：生成出合理文本不等于获得可复用能力，现有证据不足以改写持久地图。

**链接。** [论文](https://arxiv.org/abs/2608.17588) · [中文深读](papers/2026/2608.17588.zh.md) · [英文深读](papers/2026/2608.17588.md)

</details>

<a id="entry-2608-17534"></a>
<details><summary><strong>2026-08-18 · ArborMem</strong> · 状态定位 <!-- timefirst:area=state-localization --> — 读取路径先识别当前活跃的历史分支，再恢复其 trajectory，最后补充检索。 <!-- timefirst:delta=localize-state-before-retrieval --></summary>

**问题。** 在长期交互中，Agent 能否先定位当前轮次要接续的历史轨迹，再恢复该分支并补充检索？最接近的对照是在同一流程中移除状态定位。 <!-- timefirst:question=localize-active-trajectory-before-retrieval -->

**证据。** 在固定的 LongMemEval 子集上，移除状态定位后，30B 设置从 **82 降至 70**，4B 设置只从 **48 降至 46**，说明定位效果随模型变化（`model-dependent localization effect`）。 <!-- timefirst:evidence=localization-ablation-model-dependent~model-dependent-localization-effect -->

**限制。** 该消融只支持状态定位边界，不能单独证明记忆森林表示（`forest representation not isolated`）；更便宜的状态索引仍是有力替代方案。 <!-- timefirst:caveat=forest-representation-not-isolated~forest-representation-not-isolated -->

**地图。** `early_signal` — 这项结果在访问之前增加了状态定位边界；一项随模型变化的结果不足以升级持久地图节点。

**链接。** [论文](https://arxiv.org/abs/2608.17534) · [中文深读](papers/2026/2608.17534.zh.md) · [英文深读](papers/2026/2608.17534.md)

</details>

<a id="entry-2608-16168"></a>
<details><summary><strong>2026-08-17 · QUMem</strong> · 消费端状态重建 <!-- timefirst:area=consumer-state-reconstruction --> — 检索到的历史证据还要在检索后重建 query-conditioned 的当前用户状态。 <!-- timefirst:delta=retrieval-to-consumer-state-reconstruction --></summary>

**问题。** 检索到证据之后，系统是否仍需显式重建与当前查询相关的用户状态？最接近的对照是在同一套分类型检索流程中移除重建步骤。 <!-- timefirst:question=reconstruct-current-user-state-after-retrieval -->

**证据。** 在 PersonaMem + GPT-4o-mini 上，完整系统为 **61.02**，去掉情景记录后为 **58.38**，去掉分类型拆解后为 **57.11**，去掉重建后为 **54.51**；重建步骤带来的降幅最大（`reconstruction largest ablation`）。 <!-- timefirst:evidence=reconstruction-largest-ablation-on-personamem~reconstruction-largest-ablation -->

**限制。** 由于没有匹配证据综合预算（`matched evidence synthesis budget`），部分重建增益可能来自更多下游计算，而非独立的状态抽象。 <!-- timefirst:caveat=retrieval-and-synthesis-budget-not-matched~matched-evidence-synthesis-budget -->

**地图。** `early_signal` — 这项结果落在访问 → 使用方状态边界：检索到证据不等于已经可复用，仍需独立证据才能改写地图。

**链接。** [论文](https://arxiv.org/abs/2608.16168) · [中文深读](papers/2026/2608.16168.zh.md) · [英文深读](papers/2026/2608.16168.md)

</details>

<a id="entry-2608-16114"></a>
<details><summary><strong>2026-08-17 · HyperSkill</strong> · 程序性记忆结构 <!-- timefirst:area=procedural-memory-structure --> — 高阶 trajectory relation 作为同一 structural access package，共同参与 retrieval、skill ranking 与 maintenance。 <!-- timefirst:delta=higher-order-relations-in-access-package --></summary>

**问题。** 轨迹之间的高阶关系能否实质改变程序性记忆的检索、技能排序和维护？最接近的对照是从同一系统中移除超图访问路径。 <!-- timefirst:question=higher-order-relations-in-skill-access -->

**证据。** 超图访问路径消融（`hypergraph path ablation`）显示：Qwen3 在 xBench / GAIA / WebWalkerQA 上为 **52.00 / 36.97 / 50.59**，移除该路径后为 **41.00 / 35.76 / 44.71**。 <!-- timefirst:evidence=hypergraph-path-ablation-across-three-benchmarks~hypergraph-path-ablation -->

**限制。** 这项消融同时改变了表示和访问流程，存在 `representation access confounded`；只有固定任务拆解、双路径检索、排序和维护，才能把差异归因于表示方式。 <!-- timefirst:caveat=representation-and-access-pipeline-confounded~representation-access-confounded -->

**地图。** `early_signal` — 这项结果落在组织 → 访问 / 维护边界：当前证据支持整套结构化访问方案，不足以证明超图本身不可替代。

**链接。** [论文](https://arxiv.org/abs/2608.16114) · [中文深读](papers/2026/2608.16114.zh.md) · [英文深读](papers/2026/2608.16114.md)

</details>

<a id="entry-2608-12888"></a>
<details><summary><strong>2026-08-13 · ReFind</strong> · 原始状态检索 <!-- timefirst:area=raw-state-retrieval --> — 结构化记忆必须击败对 raw log 的 stateful iterative search，而不是只胜过 single-shot BM25 稻草人对照。 <!-- timefirst:delta=stronger-raw-control-for-structure --></summary>

**问题。** 结构化记忆究竟应击败怎样的原始记录对照？ReFind 给出的最强相近方案是有状态的迭代搜索，它支持会话、时间、局部上下文操作，并记录已经查看的会话。 <!-- timefirst:question=strongest-raw-control-for-structured-memory -->

**证据。** 在固定的 LongMemEval-S/M 上，ReFind 得到 **93.2 / 89.3**，通用 Agent BM25 为 **78.7 / 82.2**，单次搜索对照为 **84.7 / 68.9**，形成 `stateful raw-search advantage`。 <!-- timefirst:evidence=stateful-raw-search-outperforms-weaker-controls~stateful-raw-search-advantage -->

**限制。** 语义和行动任务仍缺少严格匹配的在线延迟、token 用量与 `full lifecycle cost`，因此不能断言原始记录搜索普遍优于结构化记忆。 <!-- timefirst:caveat=semantic-tasks-and-lifecycle-cost-unmatched~full-lifecycle-cost -->

**地图。** `early_signal` — 这项结果抬高了访问边界的原始记录基线，并收紧结构化方案的主张；单篇论文不能建立持久结论。

**链接。** [论文](https://arxiv.org/abs/2608.12888) · [中文深读](papers/2026/2608.12888.zh.md) · [英文深读](papers/2026/2608.12888.md)

</details>

<a id="periods"></a><a id="changes"></a><a id="whats-changing"></a>
## 7 天 / 30 天：记忆生命周期发生了什么变化

> **时间口径：** 滚动窗口只按 `radar_published_at` 判断。时间线中的八条迁移记录没有可重建的 Radar 接受时间，因此只作为领域地图的历史上下文，不支撑当前窗口判断。

<a id="last-7-days"></a>
### 过去 7 天：2026-08-19—2026-08-25

- **`new_signal` · Provenance ranking utility frontier：来源排序的效用边界。** 支撑：[2608.21230](#entry-2608-21230)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（measure poison rejection beside useful evidence retention）：在相同 context 下同时报告 attack suppression 与 trusted/untrusted answer-evidence recall。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="provenance-ranking-utility-frontier" state="new_signal" supports="2608.21230" confidence="medium" implication="measure-poison-rejection-beside-useful-evidence-retention" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Executable memory hygiene：可执行记忆卫生。** 支撑：[2608.20664](#entry-2608-20664)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（require later executable behavior and a strong verbatim control）：在给 typed consolidation 记功前配平 sleep compute。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="executable-memory-hygiene" state="new_signal" supports="2608.20664" confidence="medium" implication="require-later-executable-behavior-and-a-strong-verbatim-control" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Selection driven working memory：选择驱动的工作记忆。** 支撑：[2608.20631](#entry-2608-20631)；置信度：**low**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate active retention from long term persistence）：在 token-matched control 下分别隔离 scoring、decay、folding 与 suppression。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="selection-driven-working-memory" state="new_signal" supports="2608.20631" confidence="low" implication="separate-active-retention-from-long-term-persistence" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Skill granularity transfer：Skill 粒度与迁移。** 支撑：[2608.20274](#entry-2608-20274)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（match write units to the same later consumer）：固定 source trajectory、actor、retrieval call 与 lifecycle cost 后再比较 task/subtask skill。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="skill-granularity-transfer" state="new_signal" supports="2608.20274" confidence="medium" implication="match-write-units-to-the-same-later-consumer" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Budgeted skill set selection：有预算的 skill set 选择。** 支撑：[2608.19993](#entry-2608-19993)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（match selector supervision and full training cost）：在未筛选任务上测试 complementarity，并用 outcome-data collection 抵扣 saved context。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="budgeted-skill-set-selection" state="new_signal" supports="2608.19993" confidence="medium" implication="match-selector-supervision-and-full-training-cost" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 记忆使用伤害（memory consumption harm）让 applicability 成为 retrieval 后的独立判断。** 支撑：[2608.20202](#entry-2608-20202)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（test useful retention beside trap rejection）：用同时包含 memory-required、neutral 与 adversarial case 的 workload，在匹配 context 与 lifecycle cost 后测试拒绝 trap 是否误伤有用记忆。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="memory-consumption-harm" state="new_signal" supports="2608.20202" confidence="medium" implication="test-useful-retention-beside-trap-rejection" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 状态取代解析（state supersession resolution）把 current state 与 retrieved history 分开。** 支撑：[2608.19652](#entry-2608-19652)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate persistent updates from answer time resolution）：匹配 ingestion 与 transcript access，再独立改变 retirement、dependency check 与 recomputation。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="state-supersession-resolution" state="new_signal" supports="2608.19652" confidence="medium" implication="separate-persistent-updates-from-answer-time-resolution" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 记忆承诺治理（memory commitment governance）位于持久写入之前。** 支撑：[2608.19564](#entry-2608-19564)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（execute commitment choices before claiming utility）：真实执行 write、check 与 clarification，并跟踪 later retrieval、task outcome 与 authority-aware cost。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="memory-commitment-governance" state="new_signal" supports="2608.19564" confidence="medium" implication="execute-commitment-choices-before-claiming-utility" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 多源证据补全（multi source evidence completion）把组织与访问拆开。** 支撑：[2608.18704](#entry-2608-18704)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate organization from evidence completing access）：在匹配完整生命周期成本后，分别归因 fused representation 与 answer-time search。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="multi-source-evidence-completion" state="new_signal" supports="2608.18704" confidence="medium" implication="separate-organization-from-evidence-completing-access" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Judge gate 判别力（judge gate discriminability）应先于持久技能准入。** 支撑：[2608.18719](#entry-2608-18719)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（qualify judge on candidate distribution）：先在真实 optimization traces 上做同题判别，再让 judge 控制 commit。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="judge-gate-discriminability" state="new_signal" supports="2608.18719" confidence="medium" implication="qualify-judge-on-candidate-distribution" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Selector local credit 让技能访问成为可学习阶段。** 支撑：[2608.18852](#entry-2608-18852)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（credit sparse memory actions locally）：分别报告特权 selector supervision、loss masking、skill exposure 与 downstream execution。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="selector-local-credit" state="new_signal" supports="2608.18852" confidence="medium" implication="credit-sparse-memory-actions-locally" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 受约束的 Harness 演化（guarded harness evolution）把 commit 视为持续状态边界。** 支撑：[2608.19013](#entry-2608-19013)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（guard harness state before commit）：同时检查当前效用、历史保留与 validity，并分别归因共同适应的组件。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="guarded-harness-evolution" state="new_signal" supports="2608.19013" confidence="medium" implication="guard-harness-state-before-commit" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 训练侧环境记忆（training side environment memory）开始引导后续课程生成。** 支撑：[2608.19197](#entry-2608-19197)；置信度：**low**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（match retrieved training memory to static replay）：在归因 memory policy 前，用 token-matched static、random 与 score-shuffled example 对照 retrieved history。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="training-side-environment-memory" state="new_signal" supports="2608.19197" confidence="low" implication="match-retrieved-training-memory-to-static-replay" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

<a id="last-30-days"></a>
### 过去 30 天：2026-07-27—2026-08-25

- **`new_signal` · Provenance ranking utility frontier：来源排序的效用边界。** 支撑：[2608.21230](#entry-2608-21230)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（measure poison rejection beside useful evidence retention）：在相同 context 下同时报告 attack suppression 与 trusted/untrusted answer-evidence recall。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="provenance-ranking-utility-frontier" state="new_signal" supports="2608.21230" confidence="medium" implication="measure-poison-rejection-beside-useful-evidence-retention" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Executable memory hygiene：可执行记忆卫生。** 支撑：[2608.20664](#entry-2608-20664)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（require later executable behavior and a strong verbatim control）：在给 typed consolidation 记功前配平 sleep compute。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="executable-memory-hygiene" state="new_signal" supports="2608.20664" confidence="medium" implication="require-later-executable-behavior-and-a-strong-verbatim-control" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Selection driven working memory：选择驱动的工作记忆。** 支撑：[2608.20631](#entry-2608-20631)；置信度：**low**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate active retention from long term persistence）：在 token-matched control 下分别隔离 scoring、decay、folding 与 suppression。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="selection-driven-working-memory" state="new_signal" supports="2608.20631" confidence="low" implication="separate-active-retention-from-long-term-persistence" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Skill granularity transfer：Skill 粒度与迁移。** 支撑：[2608.20274](#entry-2608-20274)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（match write units to the same later consumer）：固定 source trajectory、actor、retrieval call 与 lifecycle cost 后再比较 task/subtask skill。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="skill-granularity-transfer" state="new_signal" supports="2608.20274" confidence="medium" implication="match-write-units-to-the-same-later-consumer" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Budgeted skill set selection：有预算的 skill set 选择。** 支撑：[2608.19993](#entry-2608-19993)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（match selector supervision and full training cost）：在未筛选任务上测试 complementarity，并用 outcome-data collection 抵扣 saved context。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="budgeted-skill-set-selection" state="new_signal" supports="2608.19993" confidence="medium" implication="match-selector-supervision-and-full-training-cost" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 记忆使用伤害（memory consumption harm）让 applicability 成为 retrieval 后的独立判断。** 支撑：[2608.20202](#entry-2608-20202)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（test useful retention beside trap rejection）：用同时包含 memory-required、neutral 与 adversarial case 的 workload，在匹配 context 与 lifecycle cost 后测试拒绝 trap 是否误伤有用记忆。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="memory-consumption-harm" state="new_signal" supports="2608.20202" confidence="medium" implication="test-useful-retention-beside-trap-rejection" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 状态取代解析（state supersession resolution）把 current state 与 retrieved history 分开。** 支撑：[2608.19652](#entry-2608-19652)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate persistent updates from answer time resolution）：匹配 ingestion 与 transcript access，再独立改变 retirement、dependency check 与 recomputation。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="state-supersession-resolution" state="new_signal" supports="2608.19652" confidence="medium" implication="separate-persistent-updates-from-answer-time-resolution" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 记忆承诺治理（memory commitment governance）位于持久写入之前。** 支撑：[2608.19564](#entry-2608-19564)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（execute commitment choices before claiming utility）：真实执行 write、check 与 clarification，并跟踪 later retrieval、task outcome 与 authority-aware cost。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="memory-commitment-governance" state="new_signal" supports="2608.19564" confidence="medium" implication="execute-commitment-choices-before-claiming-utility" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 多源证据补全（multi source evidence completion）把组织与访问拆开。** 支撑：[2608.18704](#entry-2608-18704)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate organization from evidence completing access）：在匹配完整生命周期成本后，分别归因 fused representation 与 answer-time search。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="multi-source-evidence-completion" state="new_signal" supports="2608.18704" confidence="medium" implication="separate-organization-from-evidence-completing-access" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Judge gate 判别力（judge gate discriminability）应先于持久技能准入。** 支撑：[2608.18719](#entry-2608-18719)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（qualify judge on candidate distribution）：先在真实 optimization traces 上做同题判别，再让 judge 控制 commit。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="judge-gate-discriminability" state="new_signal" supports="2608.18719" confidence="medium" implication="qualify-judge-on-candidate-distribution" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · Selector local credit 让技能访问成为可学习阶段。** 支撑：[2608.18852](#entry-2608-18852)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（credit sparse memory actions locally）：分别报告特权 selector supervision、loss masking、skill exposure 与 downstream execution。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="selector-local-credit" state="new_signal" supports="2608.18852" confidence="medium" implication="credit-sparse-memory-actions-locally" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 受约束的 Harness 演化（guarded harness evolution）把 commit 视为持续状态边界。** 支撑：[2608.19013](#entry-2608-19013)；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（guard harness state before commit）：同时检查当前效用、历史保留与 validity，并分别归因共同适应的组件。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="guarded-harness-evolution" state="new_signal" supports="2608.19013" confidence="medium" implication="guard-harness-state-before-commit" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

- **`new_signal` · 训练侧环境记忆（training side environment memory）开始引导后续课程生成。** 支撑：[2608.19197](#entry-2608-19197)；置信度：**low**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（match retrieved training memory to static replay）：在归因 memory policy 前，用 token-matched static、random 与 score-shuffled example 对照 retrieved history。精确合成时间：`2026-08-25T00:45:00Z`。 <!-- timefirst:direction key="training-side-environment-memory" state="new_signal" supports="2608.19197" confidence="low" implication="match-retrieved-training-memory-to-static-replay" timing="radar_published_at" synthesized="2026-08-25T00:45:00Z" prior="none" -->

时间视角：[周度](digests/README.zh.md) · [月度](digests/monthly/2026-08.zh.md) · [年度](digests/yearly/2026.zh.md)

<a id="field-map"></a><a id="research-map"></a>
## 领域地图

`经验 / 原始记录 → 写入 → 组织 → 状态定位 → 访问 / 准入 → 使用方状态 → 更新 / 演化 / 遗忘 → 治理 / 成本 / 溯源`

| 生命周期边界 | 核心问题 | 当前信号 |
|---|---|---|
| **写入（Write）** | 什么值得持久化？如何生成可复用产物？ | 记忆粒度与写入策略都应随工作负载和反馈变化。 |
| **组织（Organize）** | 哪些关系值得预先计算？ | 预存关系只有改变宿主接口的证据可达性，才能抵消维护成本。 |
| **状态定位** | 当前轮次要恢复哪条历史轨迹？ | 在判断内容相关性之前，可能要先定位当前交互状态。 |
| **访问 / 准入** | 什么应该检索、扩展或拒绝进入上下文？ | 原始记录搜索、图扩展和准入判断是不同操作。 |
| **使用方状态** | 下游 Agent 最终应该看到什么？ | 检索到的证据可能仍需重建或重新绑定。 |
| **演化 / 遗忘** | 哪类自适应状态应该改变？ | 内容、读写策略、关系和反馈入口需要分开判断。 |
| **治理 / 成本** | 哪些产物或功能可以上线？ | 认证、成对证据、溯源与全生命周期成本正成为一等约束。 |

[进入完整研究问题地图 →](categories/README.md) · [看这个方向如何被评价 →](https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-memory)

<a id="reading-paths"></a>
## 阅读路径

| 你想回答的问题 | 建议顺序 | 应该带走什么 |
|---|---|---|
| **结构何时值得额外成本？** | ReFind → CABLE → ArborMem → QUMem | 从原始记录基线、互补关系读到状态定位和面向使用方的状态重建，逐层检查每个阶段是否提供了无法低成本替代的操作。 |
| **程序性记忆如何成为可治理的能力？** | HyperSkill → WER → TRUSS | 表示与关系、技能编写策略学习和运行时认证分别对应不同问题。 |
| **如何对记忆功能做因果归因？** | D²ACCI → QUMem → ReFind | 先看阶段轨迹与上线门槛，再考察状态重建和原始记录对照如何改变归因。 |

<a id="library"></a>
## Research Library

按研究问题、研究脉络或年份查找长期资料；如果只知道问题、不知道论文名，从问题索引进入：

- [中文研究资料库](library/README.md)
- [英文研究资料库](library/README.en.md)
- [设计锚点](papers/anchors.md)

<a id="how-to-use"></a>
## 如何使用

先扫时间线摘要；需要判断一项工作时，原地展开问题、对照、关键证据、限制和地图状态。看近期变化用 7 天 / 30 天综合，按研究问题追踪脉络则进入领域地图、阅读路径或研究资料库。

## Scope / About / Contributing

收录标准：信息需要跨交互或推理步骤持久存在，或被系统显式管理，并实质改变 Agent 的后续行为。普通固定式 RAG、单纯的长上下文 / KV-cache 优化，以及与持久 Agent 状态无关的持续学习通常不在范围内。

这个仓库是一张**经过筛选的研究地图，不是关键词信息流**。负结果、基线反转以及不利的成本或归因证据都会保留。

[Suggest a paper](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [Report a correction](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [Contribution guide](CONTRIBUTING.md)
