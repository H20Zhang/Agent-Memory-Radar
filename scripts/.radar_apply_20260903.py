from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_CUTOFF = "2026-09-02T01:11:20Z"
NEW_CUTOFF = "2026-09-03T01:19:15Z"
OLD_7 = "2026-08-27—2026-09-02"
NEW_7 = "2026-08-28—2026-09-03"
OLD_30 = "2026-08-04—2026-09-02"
NEW_30 = "2026-08-05—2026-09-03"
IDENTITY = "2608.29606"
ANCHOR = "2608-29606"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


record = {
    "id": IDENTITY,
    "title": "Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents",
    "authors": ["Ming Wu", "Pengyuan Zhu"],
    "published": "2026-08-30",
    "first_seen": "2026-09-03",
    "published_at": "2026-08-30T06:55:59Z",
    "first_seen_at": "2026-09-03T01:10:47Z",
    "radar_published_at": NEW_CUTOFF,
    "time_provenance": "native_v2",
    "map_delta": "early_signal",
    "direction_keys": ["provenance-aware-layered-memory"],
    "paper_url": "https://arxiv.org/abs/2608.29606",
    "code_url": None,
    "project_url": None,
    "primary_category": "representation_organization",
    "tags": [
        "episodic",
        "semantic",
        "structured",
        "graph",
        "hierarchical",
        "timeline",
        "general-agent",
    ],
    "relevance": 1.0,
    "importance": 4,
    "visual_explainer": {
        "status": "blocked",
        "path": None,
        "format": "webp",
        "generator": "gpt-image",
        "grounding": "full-paper",
        "last_verified": "2026-09-03",
        "blocker": "A paper-specific mechanism figure has not yet passed grounded VISUAL_POLICY.md review; the verified bilingual deep note carries the layered-store, retrieval-control, and lifecycle-cost caveats meanwhile.",
    },
    "provenance": {
        "discovered_from": ["https://arxiv.org/abs/2608.29606"],
        "analyzed_from": [
            "https://arxiv.org/abs/2608.29606",
            "https://arxiv.org/html/2608.29606v1",
        ],
        "last_verified": "2026-09-03",
    },
    "analysis": {
        "tldr": "Agent Zero Memory exposes one persistent history through three provenance-linked views—an episodic timeline, an entity-event graph, and citation-locked documentary memory—and reads them through a routed hybrid-search interface. The cleanest matched evidence supports complementary retrieval channels, not the causal value of the three-store architecture itself.",
        "problem": "A single memory representation can lose temporal change, cross-session associations, or source-faithful durable facts, while a retrieved answer can still overclaim if the final reader is not constrained to evidence it actually opened.",
        "core_idea": "Preserve raw sources while building three parallel, provenance-carrying memory views. At query time, an intent gate and source router launch concurrent agentic searches over each view with hybrid dense-plus-lexical retrieval; the final integrator is citation-locked to opened evidence and may abstain when support is insufficient.",
        "memory_design": {
            "write": "Conversations, files, and connected sources remain in a raw dense-plus-lexical index while memory build extracts timestamped Memory Events, entity-event relations, and curated HDM facts, each with an origin and evidence pointer.",
            "organize": "The same history is exposed as an episodic timeline, an associative entity-event graph, and semantic Hierarchical Documentary Memory rather than being collapsed into one canonical store.",
            "read": "An intent gate skips memory for self-contained turns; otherwise a source router launches three concurrent tool-using search loops. Each uses hybrid embedding plus lexical retrieval with agent-controlled filters, and only opened evidence may be cited by the final answer.",
            "update_forget": "Factual memory is re-synchronized and experiential memory can be refined while timestamps and provenance are retained. The evaluated design does not establish principled conflict arbitration, destructive forgetting, tombstone policy, or bounded-retention behavior.",
        },
        "compared_to": [
            "A fixed-pipeline LongMemEval retrieval ablation: hybrid embedding+lexical versus embedding-only, grep-only, and lexical-only retrieval with gpt-5.6-sol",
            "A fixed memory/retriever/control backbone sweep across eight LLMs to expose model, latency, and price sensitivity",
            "Published LongMemEval and LoCoMo systems only as contextual cross-system references because judge, prompting, retrieval budget, and harness are not matched",
        ],
        "evidence": "With gpt-5.6-sol and every other component fixed, LongMemEval is 95.20 with hybrid retrieval, 94.00 with embedding only, 93.60 with grep only, and 93.40 with lexical only. Under fixed memory, retriever, and control logic, the eight-backbone LongMemEval study spans 92.20 to 95.60 accuracy while per-query cost varies by roughly 30x. The paper also reports 95.60 on LongMemEval and 93.60 on LoCoMo, but those headline comparisons are not matched component controls.",
        "why_it_matters": "The reusable research boundary is provenance-aware admission at read time: retrieval quality, source traceability, and permission to use evidence are separate variables. A convincing next study should freeze the reader, evidence surface, and budget, then independently remove one store, provenance/citation locking, and routing while charging full build and maintenance cost.",
        "limitations": [
            "The paper does not report matched remove-one-store, provenance-off, or intent-gate ablations, so the three-store organization and citation lock are not isolated as causes of the headline benchmark scores.",
            "External LongMemEval and LoCoMo comparisons use heterogeneous judges, prompting, retrieval budgets, and harnesses; the reported +0.73/+1.10 headline deltas are therefore contextual rather than component-attributable.",
            "All benchmark accuracies are single-run under the benchmark LLM judge, leaving judge variance and calibration incompletely characterized.",
            "Query-time latency, token counts, and dollar cost are reported, but extraction, graph linking, indexing, re-synchronization, and ongoing maintenance cost are not fully accounted for.",
            "Conflict arbitration across multiple valid versions/sources and explicit forgetting or tombstone semantics remain future work, so provenance does not by itself establish correct current-state resolution.",
        ],
        "confidence": "high",
    },
}

record_path = ROOT / "data" / "papers" / f"{IDENTITY}.json"
if record_path.exists():
    raise RuntimeError(f"canonical record already exists: {record_path}")
record_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

english_note = """# Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents

[← Latest Papers](../../README.en.md#latest-papers) · [Research Map](../../README.en.md#field-map) · [Representation & Organization](../../categories/representation-organization.md) · [中文](2608.29606.zh.md)

**Paper:** [arXiv:2608.29606](https://arxiv.org/abs/2608.29606) · **Published:** 2026-08-30 · **Importance:** 4/5

> **Research delta.** Agent Zero Memory makes provenance and evidence admission explicit across three parallel memory views. Its cleanest causal evidence isolates the hybrid read interface; it does **not** isolate the three-store architecture as the source of the headline benchmark gain.

## Problem

A single memory representation can flatten different failure modes: temporal supersession, cross-session association, and durable source-grounded facts need not share one organization. Even correct retrieval is insufficient if the final reader can cite evidence it never inspected.

## Mechanism

Raw conversations/files remain searchable while Memory Build derives three provenance-linked views: an episodic Memory Events timeline, an entity-event graph, and semantic Hierarchical Documentary Memory (HDM). A query passes an intent gate and source router, then three concurrent tool-using search loops run hybrid embedding + lexical retrieval with filters. The final integrator is citation-locked to evidence actually opened and may abstain when support is insufficient.

## Compared with

The strongest matched control is **inside the same pipeline**: hybrid retrieval versus embedding-only, grep-only, and lexical-only retrieval with gpt-5.6-sol and the rest fixed. A separate eight-backbone sweep holds memory/retriever/control logic fixed to expose model and economic sensitivity. The external LongMemEval/LoCoMo leaderboard rows are contextual only because judge, prompting, retrieval budget, and harness differ.

## Decisive evidence

On LongMemEval with gpt-5.6-sol and all other components fixed, accuracy is **95.20 hybrid / 94.00 embedding-only / 93.60 grep-only / 93.40 lexical-only**. This is evidence for complementary read channels, not for the causal value of three stores. Holding memory, retrieval, and control logic fixed across eight backbones gives **92.20–95.60** accuracy while per-query cost varies by roughly **30×**, which is useful as a model/cost sensitivity study. The paper also reports **95.60 LongMemEval / 93.60 LoCoMo**, but those cross-system headline scores are not matched component controls.

## Main caveat

The study has no matched **remove-one-store**, **provenance-off/citation-lock-off**, or **intent-gate-off** intervention—`three store component ablation is missing`. Query-time tokens, latency, and dollar cost are reported, but extraction, graph linking, indexing, re-synchronization, and ongoing maintenance are not fully charged. All accuracies are single-run under the benchmark LLM judge; conflict arbitration and explicit forgetting/tombstone semantics remain future work.

## Memory lifecycle

`conversations/files → raw dense+lexical index + events timeline / entity-event graph / HDM → intent gate + source router → three hybrid agentic reads → citation-locked integration / abstention → provenance-preserving update`

Working state is session-bound and useful pieces may be promoted. The paper preserves history and provenance more clearly than it resolves conflicting authorities or bounded retention.

## Why it matters

The important separation is **retrieval quality vs provenance vs evidence admission**. Future architecture claims should freeze reader, evidence surface, and resource budget, then vary one store, routing, or citation/provenance gate at a time while reporting full build, access, update, and maintenance cost.

## Related reading

[ReFind](2608.12888.md) raises the raw-search control that structured memory must beat; [StateMem](2608.19652.md) isolates supersession-aware current state; [When Stale Constraints Go Unchecked](2608.25553.md) shows that provenance still needs the right verification allocation. Agent Zero sits between these concerns by making source traceability and read-time evidence admission explicit.
"""

chinese_note = """# Agent Zero Memory：面向 LLM Agent 的来源可追踪长期记忆

[← 最新论文](../../README.md#latest-papers) · [领域地图](../../README.md#field-map) · [Representation & Organization](../../categories/zh/representation-organization.md) · [English](2608.29606.md)

**论文：** [arXiv:2608.29606](https://arxiv.org/abs/2608.29606) · **发布日期：** 2026-08-30 · **重要性：** 4/5

> **研究增量。** Agent Zero Memory 把“来源可追踪”和“证据能否进入最终回答”做成显式约束，并把同一段历史暴露为三个并行记忆视图。最干净的因果证据只隔离了混合检索接口，**还没有**证明三存储架构本身造成了榜单增益。

## 问题

把所有历史压成一种记忆表示，会把几类不同问题混在一起：时间上的状态取代、跨会话实体关联、以及需要长期保留且能回到原始来源的事实，并不一定适合同一种组织方式。即使检索正确，如果最终读者可以引用自己没真正打开过的证据，来源约束仍然是假的。

## 机制

原始对话和文件继续保留可检索索引，同时 Memory Build 派生三种带来源指针的视图：Memory Events 时间线、entity-event 图，以及语义化的 Hierarchical Documentary Memory（HDM）。查询先经过 intent gate 和 source router，再并行运行三条工具化搜索路径；每条路径都结合向量与词法检索，并允许过滤。最终整合器只能使用本轮真实打开过的证据，证据不足时可以拒答。

## 与什么比较

最关键的对照在**同一条流水线内部**：固定 gpt-5.6-sol 和其他组件，只比较混合检索、纯向量检索、grep 与纯词法检索。另一个八模型实验固定记忆、检索器和控制逻辑，用来观察模型与经济成本敏感性。论文列出的外部 LongMemEval / LoCoMo 成绩由于 judge、prompt、检索预算和 harness 不一致，只能作为背景，不能给某个记忆组件做因果归因。

## 决定性证据

LongMemEval 上，在其余组件固定时，准确率为 **95.20 混合检索 / 94.00 纯向量 / 93.60 grep / 93.40 纯词法**。这说明不同读取通道有互补性，但不能证明三存储设计本身带来增益；可概括为 `hybrid retrieval 95.20 versus 94.00`。固定记忆、检索与控制逻辑后，八个 backbone 的准确率仍在 **92.20–95.60**，而单查询成本相差约 **30×**，更适合作为模型与成本敏感性实验。论文同时报告 **95.60 LongMemEval / 93.60 LoCoMo**，但跨系统 headline score 不是匹配对照。

## 主要限制

论文没有 matched 的 **remove-one-store**、**provenance/citation-lock-off** 或 **intent-gate-off** 干预，因此 `three store component ablation is missing`。查询阶段的 token、延迟和美元成本有报告，但抽取、建图连接、索引、重新同步和长期维护成本没有完整计入。所有 benchmark 准确率都是基于 LLM judge 的单次运行；多来源冲突仲裁以及显式 forgetting / tombstone 仍是未来工作。

## 记忆生命周期

`对话/文件 → 原始向量+词法索引 + events 时间线 / entity-event 图 / HDM → intent gate + source router → 三路混合式 Agent 搜索 → citation-lock 整合 / 拒答 → 保留来源的更新`

工作记忆只在会话内存在，有价值的部分可以晋升为持久状态。当前设计更清楚地保留了历史与来源，但还没有解决多权威冲突和有界保留。

## 为什么重要

真正需要拆开的变量是 **检索质量、来源可追踪性、证据使用权限**。下一步应固定 reader、证据面和资源预算，只改变一个存储视图、routing 或 citation/provenance gate，并把构建、访问、更新和维护成本一起计入。

## 相关阅读

[ReFind](2608.12888.zh.md) 把 raw-search baseline 提高到结构化记忆必须正面比较的水平；[StateMem](2608.19652.zh.md) 单独处理 supersession-aware current state；[When Stale Constraints Go Unchecked](2608.25553.zh.md) 则说明“有 provenance”仍不等于“验证资源分配正确”。Agent Zero Memory 位于这些边界之间，把来源可追踪与读时证据准入做成显式机制。
"""

(ROOT / "papers" / "2026" / "2608.29606.md").write_text(english_note, encoding="utf-8")
(ROOT / "papers" / "2026" / "2608.29606.zh.md").write_text(chinese_note, encoding="utf-8")

# Category projections.
path = "categories/representation-organization.md"
text = read(path)
insert = (
    "**Agent Zero Memory** adds a provenance/admission boundary to representation: the same history is exposed as timeline, graph, and documentary views, while citation lock restricts the final answer to evidence actually opened. Its cleanest ablation isolates hybrid retrieval rather than the three-store organization, so architecture attribution still needs matched store/provenance interventions and full build/maintenance cost.\n\n"
)
text = replace_once(text, "## Current argument\n\n", "## Current argument\n\n" + insert, path)
row = "| 2026-08-30 | [Agent Zero Memory](../papers/2026/2608.29606.md) | `episodic` `semantic` `structured` `graph` `hierarchical` `timeline` `general-agent` | 4/5 | Provenance-linked parallel views plus citation-locked reading make evidence admission explicit; the matched ablation supports hybrid retrieval, not the causal value of the three-store architecture. |\n"
text = replace_once(text, "|---|---|---|---:|---|\n", "|---|---|---|---:|---|\n" + row, path)
write(path, text)

path = "categories/zh/representation-organization.md"
text = read(path)
insert = (
    "**Agent Zero Memory** 又补了一条“来源与准入”边界：同一段历史同时保留为时间线、图和文档三种视图，而 citation lock 只允许最终回答使用本轮真正打开过的证据。现有 matched ablation 只证明混合检索优于单一检索通道，还没有隔离三存储组织本身；要给架构记功，仍需固定 reader / evidence / budget 后做 store/provenance 干预，并补齐构建与维护成本。\n\n"
)
text = replace_once(text, "## 当前判断\n\n", "## 当前判断\n\n" + insert, path)
text = replace_once(
    text,
    "[TSIM 中文笔记](../../papers/2026/2608.25655.zh.md) · ",
    "[Agent Zero Memory](../../papers/2026/2608.29606.zh.md) · [TSIM 中文笔记](../../papers/2026/2608.25655.zh.md) · ",
    path,
)
write(path, text)

# Library research line.
path = "library/README.en.md"
text = read(path)
old_chain = "[ReFind](../papers/2026/2608.12888.md) → [CABLE](../papers/2026/2608.17911.md) / [MemFuse](../papers/2026/2608.18704.md) → [ArborMem](../papers/2026/2608.17534.md) → [QUMem](../papers/2026/2608.16168.md)"
new_chain = "[ReFind](../papers/2026/2608.12888.md) → [CABLE](../papers/2026/2608.17911.md) / [MemFuse](../papers/2026/2608.18704.md) / [Agent Zero Memory](../papers/2026/2608.29606.md) → [ArborMem](../papers/2026/2608.17534.md) → [QUMem](../papers/2026/2608.16168.md)"
text = replace_once(text, old_chain, new_chain, path)
old_para = "“Structured vs raw” is not one decision. Start with a stronger raw-interface baseline, then test whether stored relations change reachability. If history contains interleaved trajectories, localize the active state; retrieved evidence may still need to be converted into actor-facing state."
new_para = old_para + " Agent Zero adds parallel provenance-linked views and citation-locked reading, but its three-store organization still lacks a matched component ablation."
text = replace_once(text, old_para, new_para, path)
write(path, text)

path = "library/README.md"
text = read(path)
old_chain = "[ReFind](../papers/2026/2608.12888.zh.md) → [CABLE](../papers/2026/2608.17911.zh.md) / [MemFuse](../papers/2026/2608.18704.zh.md) → [ArborMem](../papers/2026/2608.17534.zh.md) → [QUMem](../papers/2026/2608.16168.zh.md)"
new_chain = "[ReFind](../papers/2026/2608.12888.zh.md) → [CABLE](../papers/2026/2608.17911.zh.md) / [MemFuse](../papers/2026/2608.18704.zh.md) / [Agent Zero Memory](../papers/2026/2608.29606.zh.md) → [ArborMem](../papers/2026/2608.17534.zh.md) → [QUMem](../papers/2026/2608.16168.zh.md)"
text = replace_once(text, old_chain, new_chain, path)
old_para = "结构化记忆与原始记录不是一次性二选一。先用更强的原始记录接口作为基线，再检验预存关系是否改变可达性；历史若包含多条交错的轨迹，需要先定位当前状态；检索到的证据最后仍可能需要转换为 Agent 实际使用的状态。"
new_para = old_para + " Agent Zero Memory 又加入并行的来源追踪视图和 citation lock，但三存储组织本身仍缺 matched component ablation。"
text = replace_once(text, old_para, new_para, path)
write(path, text)

# Timeline and rolling-period projections.
entry_en = """<a id="entry-2608-29606"></a>
<details><summary><strong>2026-09-03 · Agent Zero Memory</strong> · Provenance-aware layered memory <!-- timefirst:area=provenance-aware-layered-memory --> — exposes one history through three provenance-linked views and restricts final claims to evidence actually opened. <!-- timefirst:delta=single-memory-organization-to-provenance-locked-parallel-stores --></summary>

**Question.** Does provenance-aware parallel memory add beyond a strong retrieval interface, or are the headline gains still package-level? <!-- timefirst:question=isolate-layered-memory-from-retrieval-and-backbone -->

**Evidence.** With gpt-5.6-sol and all other components fixed, LongMemEval is **95.20 hybrid / 94.00 embedding-only / 93.60 grep-only / 93.40 lexical-only**; the separate fixed-memory/retriever/control backbone sweep spans **92.20–95.60** while per-query cost varies by roughly **30×**, giving `hybrid retrieval 95.20 versus 94.00` as the matched witness. <!-- timefirst:evidence=hybrid-retrieval-interface-under-fixed-pipeline~hybrid-retrieval-95.20-versus-94.00 -->

**Caveat.** External SOTA rows use different judges, prompts, retrieval budgets, and harnesses; no matched store/provenance/gate ablation isolates the layered architecture, full build/maintenance cost is incomplete, and `three store component ablation is missing`. <!-- timefirst:caveat=cross-harness-and-missing-component-isolation~three-store-component-ablation-is-missing -->

**Map.** `early_signal` — one paper makes provenance-aware evidence admission worth testing separately, but does not establish a durable layered-memory direction.

**Links.** [Paper](https://arxiv.org/abs/2608.29606) · [中文深读](papers/2026/2608.29606.zh.md) · [English deep note](papers/2026/2608.29606.md)

</details>

"""
entry_zh = """<a id="entry-2608-29606"></a>
<details><summary><strong>2026-09-03 · Agent Zero Memory</strong> · 来源可追踪的分层记忆 <!-- timefirst:area=provenance-aware-layered-memory --> — 同一段历史保留为三种带来源的视图，并把最终回答限制在本轮真正打开过的证据上。 <!-- timefirst:delta=single-memory-organization-to-provenance-locked-parallel-stores --></summary>

**问题。** 来源可追踪的并行记忆是否真的超越强检索接口，还是 headline gain 仍主要属于整套系统？ <!-- timefirst:question=isolate-layered-memory-from-retrieval-and-backbone -->

**证据。** 固定 gpt-5.6-sol 和其他组件后，LongMemEval 为 **95.20 混合检索 / 94.00 纯向量 / 93.60 grep / 93.40 纯词法**；另一组固定 memory / retriever / control 的 backbone sweep 为 **92.20–95.60**，单查询成本却相差约 **30×**。其中最干净的匹配证据可记为 `hybrid retrieval 95.20 versus 94.00`。 <!-- timefirst:evidence=hybrid-retrieval-interface-under-fixed-pipeline~hybrid-retrieval-95.20-versus-94.00 -->

**限制。** 外部 SOTA 成绩使用不同 judge、prompt、检索预算和 harness；论文没有 matched 的 store / provenance / gate ablation 来隔离分层架构，完整构建与维护成本也未补齐，即 `three store component ablation is missing`。 <!-- timefirst:caveat=cross-harness-and-missing-component-isolation~three-store-component-ablation-is-missing -->

**地图。** `early_signal` — 单篇证据足以把“来源追踪下的证据准入”列为值得单测的问题，但不足以建立 durable layered-memory direction。

**链接。** [论文](https://arxiv.org/abs/2608.29606) · [中文深读](papers/2026/2608.29606.zh.md) · [English deep note](papers/2026/2608.29606.md)

</details>

"""

dir_en = f"- **`new_signal` · provenance aware layered memory.** Supports: [2608.29606](#entry-2608-29606); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (separate layered memory from retrieval interface and lifecycle cost): freeze reader / evidence surface / budget, then independently vary one store, provenance/citation lock, and routing while charging build, access, update, and maintenance cost. Exact synthesis time: `{NEW_CUTOFF}`. <!-- timefirst:direction key=\"provenance-aware-layered-memory\" state=\"new_signal\" supports=\"2608.29606\" confidence=\"high\" implication=\"separate-layered-memory-from-retrieval-interface-and-lifecycle-cost\" timing=\"radar_published_at\" synthesized=\"{NEW_CUTOFF}\" prior=\"none\" -->\n"
dir_zh = f"- **`new_signal` · provenance aware layered memory：来源可追踪的分层记忆。** 支撑：[2608.29606](#entry-2608-29606)；置信度：**high**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（separate layered memory from retrieval interface and lifecycle cost）：固定 reader / evidence surface / budget，再分别改变单个 store、provenance/citation lock 与 routing，并完整计入 build、access、update、maintenance cost。精确合成时间：`{NEW_CUTOFF}`。 <!-- timefirst:direction key=\"provenance-aware-layered-memory\" state=\"new_signal\" supports=\"2608.29606\" confidence=\"high\" implication=\"separate-layered-memory-from-retrieval-interface-and-lifecycle-cost\" timing=\"radar_published_at\" synthesized=\"{NEW_CUTOFF}\" prior=\"none\" -->\n"


def patch_readme(path: str, language: str) -> None:
    text = read(path)
    if ANCHOR in text or IDENTITY in text:
        raise RuntimeError(f"{path}: Agent Zero is already projected")
    if language == "en":
        text = replace_once(text, "Last updated: **2026-09-02**", "Last updated: **2026-09-03**", path)
        text = replace_once(text, '<a id="entry-2608-29605"></a>', entry_en + '<a id="entry-2608-29605"></a>', path)
        text = replace_once(text, f"### Last 7 days: {OLD_7}", f"### Last 7 days: {NEW_7}", path)
        text = replace_once(text, f"### Last 30 days: {OLD_30}", f"### Last 30 days: {NEW_30}", path)
        direction = dir_en
        h7 = f"### Last 7 days: {NEW_7}\n\n"
        h30 = f"### Last 30 days: {NEW_30}\n\n"
    else:
        text = replace_once(text, "最后更新：**2026-09-02**", "最后更新：**2026-09-03**", path)
        text = replace_once(text, '<a id="entry-2608-29605"></a>', entry_zh + '<a id="entry-2608-29605"></a>', path)
        text = replace_once(text, f"### 过去 7 天：{OLD_7}", f"### 过去 7 天：{NEW_7}", path)
        text = replace_once(text, f"### 过去 30 天：{OLD_30}", f"### 过去 30 天：{NEW_30}", path)
        direction = dir_zh
        h7 = f"### 过去 7 天：{NEW_7}\n\n"
        h30 = f"### 过去 30 天：{NEW_30}\n\n"

    # Advance the common synthesis cutoff in existing period directions only.
    periods_start = text.index('<a id="periods"></a>')
    field_start = text.index('<a id="field-map"></a>', periods_start)
    before, periods, after = text[:periods_start], text[periods_start:field_start], text[field_start:]
    periods = periods.replace(OLD_CUTOFF, NEW_CUTOFF)

    # Recuris was accepted on 2026-08-27 and therefore leaves the new seven-day window.
    seven_start = periods.index('<a id="last-7-days"></a>')
    thirty_start = periods.index('<a id="last-30-days"></a>', seven_start)
    seven, rest = periods[seven_start:thirty_start], periods[thirty_start:]
    lines = seven.splitlines(keepends=True)
    removed = [line for line in lines if 'supports="2608.24876"' in line]
    if len(removed) != 1:
        raise RuntimeError(f"{path}: expected exactly one Recuris seven-day direction, found {len(removed)}")
    seven = ''.join(line for line in lines if 'supports="2608.24876"' not in line)
    periods = periods[:seven_start] + seven + rest

    if periods.count(h7) != 1 or periods.count(h30) != 1:
        raise RuntimeError(f"{path}: rolling headings are not unique")
    periods = periods.replace(h7, h7 + direction + "\n", 1)
    periods = periods.replace(h30, h30 + direction + "\n", 1)
    write(path, before + periods + after)


patch_readme("README.en.md", "en")
patch_readme("README.md", "zh")

# Advance validator contract and fixtures.
path = "scripts/validate_reading.py"
text = read(path)
text = replace_once(text, f'SYNTHESIS_TIMESTAMP = "{OLD_CUTOFF}"', f'SYNTHESIS_TIMESTAMP = "{NEW_CUTOFF}"', path)
text = replace_once(text, '"last-7-days": (date(2026, 8, 27), date(2026, 9, 2))', '"last-7-days": (date(2026, 8, 28), date(2026, 9, 3))', path)
text = replace_once(text, '"last-30-days": (date(2026, 8, 4), date(2026, 9, 2))', '"last-30-days": (date(2026, 8, 5), date(2026, 9, 3))', path)
write(path, text)

path = "tests/test_memory_v2_contract.py"
text = read(path)
text = text.replace(OLD_CUTOFF, NEW_CUTOFF)
text = text.replace(OLD_7, NEW_7)
text = text.replace(OLD_30, NEW_30)
text = text.replace('date(2026, 8, 27), date(2026, 9, 2)', 'date(2026, 8, 28), date(2026, 9, 3)')
text = text.replace('date(2026, 8, 4), date(2026, 9, 2)', 'date(2026, 8, 5), date(2026, 9, 3)')
text = text.replace('2026-09-02T23:59:59Z', '2026-09-03T23:59:59Z')
write(path, text)

path = "tests/test_validate_reading.py"
text = read(path)
needle = 'EXPECTED_TIMELINE_TITLES = {\n    "2608-29605": "2026-09-02 · Hindsight Memory-PRM",'
replacement = 'EXPECTED_TIMELINE_TITLES = {\n    "2608-29606": "2026-09-03 · Agent Zero Memory",\n    "2608-29605": "2026-09-02 · Hindsight Memory-PRM",'
text = replace_once(text, needle, replacement, path)
write(path, text)

print("Applied Agent Zero Memory canonical, bilingual, time-first, category, library, and validator projections.")
