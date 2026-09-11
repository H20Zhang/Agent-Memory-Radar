from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone, timedelta
import json, os, re

ROOT=Path('.')
FIRST_SEEN='2026-09-11T00:25:15Z'
RADAR_TS=os.environ['RADAR_TS']
TODAY=RADAR_TS[:10]
OLD_TS='2026-09-03T01:19:15Z'
SEVEN_START='2026-09-05'; THIRTY_START='2026-08-13'; END=TODAY

papers=[
{
'id':'2609.10263','title':'What Should an Agent Forget? Separating What Is Stored from What Is Used','authors':['Yuhang Li','Yuchen Li'],'published':'2026-09-09','published_at':'2026-09-09T14:48:09Z','primary_category':'write_update_consolidation','direction':'query-conditioned-storage-use-separation','importance':4,'relevance':1.0,'code_url':None,
'tags':['forgetting','supersession','query-conditioned-memory','knowledge-update','governance','long-term-memory'],
'analysis':{
'tldr':'RD-Forget keeps the source archive intact while constructing a query-conditioned answer-time memory view that suppresses superseded same-slot facts for current-state questions and can recover them for historical questions. The strongest evidence is a matched Luna ablation, so the defensible claim is about use control rather than physical deletion.','problem':'Persistent history can contain facts that are obsolete for a current-state answer but still necessary for historical or evolution queries. Storage retention and answer-time influence therefore need separate policies.','core_idea':'A frozen LM curator extracts query-relevant evidence into semantic slots, links same-slot replacements, preserves complementary multi-hop relations, and packs an eligible view under a 2,048-token memory budget. Superseded entries stay in the retained source archive and can become eligible again for historical intent.','memory_design':{'write':'Source observations remain in a retained archive; query-time curation materializes active and superseded entries rather than destructively rewriting the archive.','organize':'Atomic facts receive subject|relation|scope slots and replacement links so competing values are distinguished from complementary relations.','read':'The current query controls curation, eligibility, lexical ranking, LM selection, and budgeted packing; historical intent can rescue superseded evidence.','update_forget':'Forgetting is query-local suppression of superseded evidence in the used view. It is not physical erasure; older source observations remain available for later recuration.'},
'compared_to':['ACE and ReasoningBank under the same answering pipeline as contextual system baselines','Matched GPT-5.6-Luna variants that disable forgetting, archive rescue, semantic slots, relation closure, or question-conditioned curation on the same 264 tasks'],
'evidence':'Across Qwen3.5-flash, GPT-5.6-Luna, MiniMax-M2.5, and Kimi-K2.5, RD-Forget is best in all 12 model-by-main-suite cells. In the matched Luna batch, Full scores 91.86/93.59/74.00 on AMB-Text/LME-KU/MAB-FC; removing forgetting falls to 68.60/60.26/51.00, and removing query conditioning falls to 77.91/82.05/56.00.','why_it_matters':'The useful lifecycle boundary is storage versus admission to the current consumer. A memory can remain retained while its authority for one query is revoked, so evaluation should separate preservation, current-state suppression, historical recovery, and final behavioral effect.','limitations':['The retained archive means the method does not implement privacy deletion, legal erasure, or storage minimization.','The curator receives the current question and task metadata; model-based evaluation is within-protocol rather than an independent external judge.','The main system comparisons change memory organization, so component attribution should rely on the matched ablations.','The paper reports answer-time token caps but not a complete construction, curation, retrieval, latency, and maintenance cost frontier.'],'confidence':'high'}},
{
'id':'2609.08279','title':'What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory','authors':['Chen Shen'],'published':'2026-09-08','published_at':'2026-09-08T05:48:10Z','primary_category':'evaluation_analysis','direction':'restore-counterfactual-eviction-audit','importance':4,'relevance':0.99,'code_url':None,
'tags':['forgetting','eviction','counterfactual','evaluation','longmemeval','retrieval-failure','lifecycle-cost'],
'analysis':{
'tldr':'The paper adds a per-question restore counterfactual that distinguishes evidence destroyed by eviction from evidence retained but missed by retrieval and evidence the reader still fails to use. It is a diagnostic instrument, not a new memory policy.','problem':'Budget-accuracy curves conflate three different failure locations: the store may have evicted indispensable evidence, the retriever may fail to surface retained evidence, or the reader may fail even when evidence is present.','core_idea':'For each oracle-answerable policy error, restore the question gold evidence into the same read-time pipeline and rerun the frozen reader. Combine whether correctness flips with whether gold evidence survived the store to label the error irreversible, recoverable, or residual.','memory_design':{'write':'The audit does not change the original write path; it evaluates external stores after an eviction policy has enforced a token budget.','organize':'Stored units remain LongMemEval-S turn/session units so gold evidence can be aligned exactly with retained versus evicted state.','read':'The restore intervention holds reader, prompt, decoding, judge, and retrieval setting fixed while injecting gold evidence to localize the failure stage.','update_forget':'Eviction is treated as destructive forgetting for task evidence. The audit measures its task cost but does not prescribe whether retention is desirable under privacy or deletion obligations.'},
'compared_to':['Ordinary budget-versus-accuracy evaluation that cannot localize loss','FIFO, random, redundancy-aware, and LLM-importance eviction at 80k/30k/8k budgets under both top-k and forced-gold read regimes'],
'evidence':'Under realistic top-k retrieval at 80k tokens, the irreversible share among restoration-corrected errors is 0.71 FIFO, 0.73 random, 0.67 redundancy-aware, and 0.60 LLM-importance; at 8k it reaches 1.00 for all four. An exploratory matched-accuracy analysis detects no policy-pair difference in irreversible rate at 1.2–6 percentage-point resolution, while detecting a deliberately destructive control.','why_it_matters':'A single memory accuracy number cannot tell whether to spend engineering effort on retention, retrieval, or consumer utilization. Restore counterfactuals make those remedies separable and require retrieval regime to accompany budget-frontier claims.','limitations':['The study uses LongMemEval-S, two readers, one primary judge, and gold evidence labels; the instrument is mainly a benchmark audit.','Derived or heavily consolidated memories are excluded because their units no longer align cleanly with gold source units.','Restoring gold evidence changes the read-time context and relies on oracle-answerability assumptions; residual errors remain reader-dependent.','The null among matched-accuracy policy pairs is specific to tested policies, budgets, and statistical resolution and does not identify a universally best eviction policy.'],'confidence':'high'}},
{
'id':'2609.08273','title':'MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging','authors':['Junxi Wang','Te Sun','Jiayi Zhu','Chen Zhang','Siyuan Li','Xuyang Liu','Zichen Wen','Xiaobing Tu','Jinkui Ren','Xiantao Zhang','Ziqi Yuan','Linfeng Zhang'],'published':'2026-09-08','published_at':'2026-09-08T05:30:30Z','primary_category':'representation_organization','direction':'event-structured-posthoc-compression','importance':4,'relevance':0.99,'code_url':'https://github.com/Celina-love-sweet/MemForest',
'tags':['compression','event-tree','temporal','merging','retrieval','multimodal-memory','efficiency'],
'analysis':{
'tldr':'MemForest post-processes accumulated memory into semantic-temporal EventTrees, progressively merges similar nodes, and optionally changes retrieval with anchor-guided temporal propagation. It shows a useful quality/size/speed tradeoff, but compression and AGPR must be credited separately.','problem':'External memory grows continuously, increasing storage and retrieval work. Generation-time summarization does not bound an already accumulated store, while generic pruning or merging can ignore event continuity and temporal structure.','core_idea':'Partition memory nodes using global embedding similarity plus local temporal continuity, build a maximum spanning tree within each event, then repeatedly merge high-weight pairs with an LM until a target compression ratio. AGPR reranks a larger candidate pool using temporal proximity to anchor hits.','memory_design':{'write':'MemForest consumes memory nodes already produced by an underlying system such as Mem0 or M3-Agent; it is a post-processing compression stage rather than the original writer.','organize':'Nodes are assigned to event-centric units using semantic similarity and temporal continuity, represented as EventTrees, and progressively merged by LM-generated fused nodes.','read':'Base similarity retrieval can operate on the compressed store; optional AGPR adds temporal-neighborhood propagation around high-similarity anchors.','update_forget':'Compression destructively replaces pairs with fused nodes to reach a preset ratio. Incremental updates, conflict-aware deletion, provenance preservation, and long-run repartitioning policy are not evaluated.'},
'compared_to':['The uncompressed Mem0 and M3-Agent stores','Random Pruning, KMeans, DART, StreamMeCo, Random Merging, and ToMe at matched compression ratios','MemForest without AGPR versus MemForest+AGPR to separate representation compression from the changed retrieval policy'],
'evidence':'With Mem0, 50% compression retains 97.1% of the uncompressed aggregate performance and MemForest+AGPR retains 98.3%; at 70% compression plain MemForest falls to 93.3%, showing a quality boundary. Retrieval time at 50%+AGPR falls from 0.48 to 0.24 s on LoCoMo, 8.30 to 4.32 s on LongMemEval, and 4.90 to 2.78 s on PersonaMem. Experiments average three runs and use GPT-4o-mini for merging.','why_it_matters':'The result makes post-hoc store size a first-class lifecycle variable: compression should be evaluated against strong pruning/merging controls while separately pricing the retrieval policy used to recover lost temporal structure.','limitations':['AGPR changes the read policy together with the compressed representation, so quality gains of the combined package cannot be assigned to compression alone.','LM fusion can erase provenance, exact wording, or conflicting states; those failure modes are not directly evaluated.','The study is largely static post-processing; incremental repartitioning, update invalidation, and sustained maintenance cost are not characterized.','Reported retrieval speed excludes the complete lifecycle cost of embedding, partitioning, repeated LM merges, storage updates, and future recompression.'],'confidence':'high'}}]

for p in papers:
    rec={
      'id':p['id'],'title':p['title'],'authors':p['authors'],'published':p['published'],'first_seen':FIRST_SEEN[:10],
      'published_at':p['published_at'],'first_seen_at':FIRST_SEEN,'radar_published_at':RADAR_TS,'time_provenance':'native_v2','map_delta':'early_signal','direction_keys':[p['direction']],
      'paper_url':f"https://arxiv.org/abs/{p['id']}",'code_url':p['code_url'],'project_url':None,'primary_category':p['primary_category'],'tags':p['tags'],'relevance':p['relevance'],'importance':p['importance'],
      'visual_explainer':{'status':'blocked','path':None,'format':'webp','generator':'gpt-image','grounding':'full-paper','last_verified':TODAY,'blocker':'No paper-specific visual has yet passed grounded VISUAL_POLICY.md review; the bilingual deep note is the current researcher-facing explanation.'},
      'provenance':{'discovered_from':[f"https://arxiv.org/abs/{p['id']}"],'analyzed_from':[f"https://arxiv.org/abs/{p['id']}",f"https://arxiv.org/html/{p['id']}"],'last_verified':TODAY},'analysis':p['analysis']}
    out=ROOT/'data'/'papers'/f"{p['id']}.json"
    if out.exists(): raise SystemExit(f'duplicate {p["id"]}')
    out.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

notes_en={
'2609.10263':'''# RD-Forget: separate what remains stored from what is allowed to influence this answer

[中文](2609.10263.zh.md) | **English** · [Home](../../README.en.md) · [Research Library](../../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.10263) · **Published: 2026-09-09** · **Importance: 4/5** · **Confidence: high**

> **Research delta.** RD-Forget makes forgetting query-local: source observations remain retained, while a question-conditioned view decides which states may influence the current answer. The strongest evidence is a matched ablation of use control, not a deletion mechanism.

## Problem
A fact may be obsolete for a current-state question and still indispensable for a historical question. Treating storage retention and present use as one decision either lets stale state leak into current answers or destroys history that a later query needs.

## Mechanism
The archive remains intact. For each query, a frozen LM curator extracts the smallest useful evidence set, assigns `subject|relation|scope` slots, and marks older same-slot values as superseded while keeping complementary relations needed for multi-hop chains. Eligible entries are ranked and selected, then packed into a **2,048-token memory-view budget**. Historical intent can re-enable superseded entries.

`retained source archive → query-conditioned curation → slot-scoped supersession → eligibility/rescue → budgeted evidence view → answer`

## Closest comparison
The useful causal comparison is the paper's matched GPT-5.6-Luna batch on the same 264 tasks. It disables forgetting, archive rescue, semantic slots, relation closure, or question-conditioned curation one at a time. ACE and ReasoningBank provide broader system baselines but change more than the use-control stage.

## Decisive evidence
Matched Full reaches **91.86 / 93.59 / 74.00** on AMB-Text / LME-KU / MAB-FC. Removing forgetting falls to **68.60 / 60.26 / 51.00**, the largest deficit on all three suites; removing question-conditioned curation falls to **77.91 / 82.05 / 56.00**. Across four backbones, RD-Forget is best in all 12 main-suite cells. The evidence supports a strong use-admission effect under this protocol.

## Main caveat
This is **not physical forgetting**. The original archive remains available and can be recurated. The method therefore does not establish privacy erasure, data minimization, or storage deletion. The curator also sees the current question and task metadata, and model-based evaluation is within-protocol. Complete curation/retrieval/latency/maintenance cost is not reported as a matched frontier.

## Memory lifecycle
| Stage | What RD-Forget does |
|---|---|
| Write | Retains source observations; answer-time curation materializes derived entries. |
| Organize | Uses semantic slots and explicit supersession links to separate competing values from complementary relations. |
| Read | Builds a query-conditioned eligible view and packs selected entries under a fixed budget. |
| Update / forget | Suppresses superseded evidence for a particular use context while preserving historical recoverability. |

## Why it matters
The important boundary is **authority to use**, not simply existence in storage. Future evaluations should score current-state suppression, historical recovery, and downstream behavior separately, with destructive deletion evaluated as a different lifecycle operation.

## Related reading
- [StateMemBench / StateMem](2608.19652.md): resolves superseded state at consumer time rather than defining forgetting as deletion.
- [When Stale Constraints Go Unchecked](2608.25553.md): shows that retained provenance still needs the right verification allocation.
- [What Eviction Destroys](2609.08279.md): audits actual destructive eviction and therefore supplies the complementary deletion-side view.
''',
'2609.08279':'''# What Eviction Destroys: localize forgetting loss before choosing a policy

[中文](2609.08279.zh.md) | **English** · [Home](../../README.en.md) · [Research Library](../../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.08279) · **Published: 2026-09-08** · **Importance: 4/5** · **Confidence: high**

> **Research delta.** A restore counterfactual turns a budget-accuracy drop into three different diagnoses: evidence was destroyed by eviction, retained but missed by retrieval, or surfaced yet still not used. It is an evaluation instrument, not a new memory policy.

## Problem
A smaller memory store can lower answer accuracy for different reasons. Without locating the failure, a better retriever can be prescribed for an item that was already deleted, or a retention policy can be blamed when the reader simply failed to use available evidence.

## Mechanism
For every oracle-answerable policy error, the audit restores the question's gold evidence into the read-time context and reruns the same reader. A wrong→correct flip plus missing gold units means **irreversible** eviction loss; the same flip with all gold retained means **recoverable** retrieval miss; remaining wrong answers are **residual** utilization failures.

`budgeted store → ordinary retrieval/reader error → restore same gold evidence → correctness flip × retention state → failure location`

## Closest comparison
The relevant baseline is the ordinary budget-versus-accuracy frontier. The paper evaluates FIFO, random, redundancy-aware, and LLM-importance eviction at 80k/30k/8k tokens under top-k and forced-gold read regimes, holding the reader-side protocol fixed for the counterfactual.

## Decisive evidence
Under top-k at **80k**, irreversible share among errors corrected by restoration is **0.71 FIFO / 0.73 random / 0.67 redundancy-aware / 0.60 LLM-importance**. At **8k**, it becomes **1.00** for all four policies. Recoverable errors exist under top-k but disappear under forced-gold by construction, demonstrating why retrieval regime belongs in any budget frontier. Importantly, an exploratory matched-accuracy comparison finds **no detectable difference** in irreversible rate among policy pairs at 1.2–6pp resolution, although the audit detects a deliberately destructive control.

## Main caveat
The audit depends on LongMemEval-S gold evidence and an oracle-answerable filter, so it is mainly a benchmark-analysis tool. Its units must align with source turns/sessions, which excludes many derived-summary stores. Restoring gold also changes the read context, and residual error remains reader-dependent. The null result is bounded to the tested policies and budgets.

## Memory lifecycle
| Stage | What is measured |
|---|---|
| Write | Held outside the audit; stored units come from the benchmark history. |
| Organize | Keeps source-aligned units so retention can be checked exactly. |
| Read | Separates retrieval miss from utilization failure through a paired gold-restore intervention. |
| Update / forget | Measures task evidence irreversibly lost by eviction under an explicit token budget. |

## Why it matters
This changes the evaluation question from “which eviction policy has the best accuracy?” to **which lifecycle stage caused each lost answer?** It also prevents forced-gold and top-k results from being compared as if they measured the same object.

## Related reading
- [The Compaction Cliff](2608.22752.md): asks which memory types survive compression but does not localize each lost answer with restoration.
- [RD-Forget](2609.10263.md): separates retained history from query-local use without destructive deletion.
- [Agent Memory evaluation genealogy](https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-memory): benchmark-level context lives in the sibling radar.
''',
'2609.08273':'''# MemForest: post-hoc memory compression is useful, but keep retrieval recovery separate

[中文](2609.08273.zh.md) | **English** · [Home](../../README.en.md) · [Research Library](../../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.08273) · [Code](https://github.com/Celina-love-sweet/MemForest) · **Published: 2026-09-08** · **Importance: 4/5** · **Confidence: high**

> **Research delta.** MemForest treats an already accumulated memory store as a compressible systems object: event-centric partitioning and progressive merging reduce node count, while a separate temporal-propagation retriever can recover some quality. The two interventions should not be credited as one mechanism.

## Problem
Memory systems continuously accumulate nodes. Generation-time summarization may shorten each write but does not bound the total store, while generic pruning or merging ignores that distant semantically similar nodes and nearby semantically different nodes can belong to the same event.

## Mechanism
MemForest first combines global embedding similarity with a local temporal window to partition nodes into event units. Each unit becomes a maximum spanning tree. High-weight pairs are progressively merged by an LM until the target compression ratio is reached. Optional **AGPR** starts from similarity candidates and reranks them using temporal proximity to anchor hits.

`existing memory nodes → semantic+temporal event partition → EventTree → progressive LM merge → compressed store → optional AGPR`

## Closest comparison
The clean representation comparison is compressed MemForest against Random Pruning, KMeans, DART, StreamMeCo, Random Merging, and ToMe at the same compression ratio, with the original Mem0 or M3-Agent store as the 100% reference. AGPR is a changed read policy and should be reported separately from plain MemForest.

## Decisive evidence
With Mem0 at **50% compression**, plain MemForest retains **97.1%** of uncompressed aggregate performance and MemForest+AGPR retains **98.3%**. At **70%**, plain MemForest falls to **93.3%**, making the quality boundary visible rather than hiding it. With 50% compression+AGPR, reported retrieval time falls **0.48→0.24 s** on LoCoMo, **8.30→4.32 s** on LongMemEval, and **4.90→2.78 s** on PersonaMem. Results are averaged over three runs; GPT-4o-mini performs node merging.

## Main caveat
AGPR changes the retrieval policy at the same time that the store is compressed, so its extra quality cannot be assigned to EventTree compression. More importantly, LM-generated fusion can lose exact wording, provenance, or conflicting states; incremental repartitioning and update invalidation are not tested. Retrieval-time speedups omit the full cost of embeddings, partitioning, repeated LM merges, storage rewrites, and future recompression.

## Memory lifecycle
| Stage | What MemForest does |
|---|---|
| Write | Starts after another memory system has produced nodes. |
| Organize | Groups nodes into semantic-temporal EventTrees and destructively fuses selected pairs. |
| Read | Uses ordinary similarity retrieval or optional AGPR temporal propagation. |
| Update / forget | Enforces a target node-reduction ratio through merging; online incremental maintenance is unresolved. |

## Why it matters
Post-hoc memory size should be treated like an index-maintenance problem: compare compression under the same quality target, then price read recovery and maintenance separately. The next decisive experiment is a growing stream with provenance-aware merges, invalidation, and full amortized cost.

## Related reading
- [The Compaction Cliff](2608.22752.md): stresses typed preservation under compression.
- [LeanMem](2608.03463.md): changes the write contract earlier in the lifecycle rather than compressing an accumulated store later.
- [VoiceMem](2608.26005.md): exposes a different online/streaming cost boundary.
'''}

notes_zh={
'2609.10263':'''# RD-Forget：把“仍然存着”与“这次允许使用”分开

**中文** | [English](2609.10263.md) · [返回首页](../../README.md) · [研究资料库](../../library/README.md)

[论文](https://arxiv.org/abs/2609.10263) · **发布日期：2026-09-09** · **重要性：4/5** · **置信度：高**

> **研究增量。** RD-Forget 把遗忘变成查询局部的使用控制：原始历史继续保留，但当前问题只看到经过筛选的记忆视图。最强证据来自匹配消融，因此可归因的是“使用准入”，不是物理删除。

## 问题
同一条旧事实对当前状态问题可能已经失效，对历史问题却仍然必要。如果把保存和使用绑成一个决策，要么旧状态继续污染当前答案，要么为了避免污染而把未来仍有价值的历史删掉。

## 机制
系统保留原始历史。每次查询到来后，冻结的语言模型整理器提取最小必要证据，为事实分配 `subject|relation|scope` 槽位，并把同槽位的旧值标成已被替代；多跳推理需要的互补关系继续保留。随后系统做资格筛选、排序与选择，并把最终视图限制在 **2,048 个记忆 token** 内。历史意图可以重新允许旧状态进入当前视图。

`保留原始历史 → 按查询整理 → 槽位级替代关系 → 使用资格 / 历史恢复 → 有预算的证据视图 → 回答`

## 最近的对照
最有因果价值的是同一批 264 个任务上的 GPT-5.6-Luna 消融：分别关闭遗忘、历史恢复、语义槽位、关系闭包和问题条件化整理。ACE 与 ReasoningBank 可用于系统层比较，但同时改变的环节更多。

## 决定性证据
完整配置在 AMB-Text / LME-KU / MAB-FC 上得到 **91.86 / 93.59 / 74.00**。关闭遗忘后降为 **68.60 / 60.26 / 51.00**，三个数据集都是最大降幅；关闭按问题整理后为 **77.91 / 82.05 / 56.00**。四种基础模型的 12 个主实验组合中，RD-Forget 全部最高。现有证据足以说明当前协议下的使用准入很重要。

## 主要限制
这里的“遗忘”**不是物理删除**。原始历史仍然存在，也能被后续问题重新整理，因此不能把结果解释为隐私擦除、数据最小化或合规删除。整理器还看到了当前问题与任务元数据，模型评判属于协议内评估；构建、整理、检索、延迟和长期维护也没有形成完整的匹配成本曲线。

## 记忆生命周期
| 阶段 | RD-Forget 的作用 |
|---|---|
| 写入 | 保留源观察；回答时再物化派生事实。 |
| 组织 | 用语义槽位和替代链接区分竞争状态与互补关系。 |
| 读取 | 按当前问题构建可用视图，并在固定预算内选择证据。 |
| 更新 / 遗忘 | 对当前用途压制已被替代的状态，同时保留历史可恢复性。 |

## 为什么重要
真正需要单独测量的是**某条记忆是否有权影响当前行为**。后续实验应把当前状态压制、历史恢复、真正删除以及下游行为分别计分。

## 延伸阅读
- [StateMemBench / StateMem](2608.19652.zh.md)：把旧状态解析成当前可执行状态。
- [When Stale Constraints Go Unchecked](2608.25553.zh.md)：说明保留来源信息仍不足以保证正确使用。
- [What Eviction Destroys](2609.08279.zh.md)：从真正的破坏性淘汰一侧补上对照。
''',
'2609.08279':'''# What Eviction Destroys：先定位遗忘损失，再比较策略

**中文** | [English](2609.08279.md) · [返回首页](../../README.md) · [研究资料库](../../library/README.md)

[论文](https://arxiv.org/abs/2609.08279) · **发布日期：2026-09-08** · **重要性：4/5** · **置信度：高**

> **研究增量。** 恢复反事实把“预算变小后准确率下降”拆成三类：证据被淘汰摧毁、证据仍在但检索漏掉、证据已经出现但读者没有正确使用。它是诊断工具，不是一种新的记忆策略。

## 问题
记忆预算下降后出现错误，修复方法取决于错误发生在哪一层。已经被删掉的证据无法靠更强检索器找回；仍在存储中的证据也不该被误判为淘汰策略的问题。

## 机制
对每个“完整金标准证据下本可回答、当前策略却答错”的问题，审计器把该问题的金标准证据恢复到读取上下文，并用同一个读者重新回答。错误转正确且存在被淘汰证据，记为不可恢复；错误转正确且证据都仍在，记为可恢复的检索漏失；恢复后仍错误，则归入使用失败。

`有预算的存储 → 正常读取失败 → 恢复同一金标准证据 → 正确性变化 × 保留状态 → 定位失败阶段`

## 最近的对照
最直接的基线是普通的预算—准确率曲线。论文比较 FIFO、随机、冗余感知和 LLM 重要性淘汰，在 80k / 30k / 8k 三档预算下分别使用 top-k 与强制金标准读取，并保持反事实中的读者侧协议不变。

## 决定性证据
在更现实的 top-k、**80k** 预算下，恢复后可纠正错误中的不可恢复占比分别为 **0.71 / 0.73 / 0.67 / 0.60**；预算降到 **8k** 后四种策略都达到 **1.00**。top-k 下仍存在可恢复错误，而强制金标准读取按构造不会有这一类，因此两种读取协议不能混在同一预算曲线上。更重要的负结果是：在准确率匹配后，测试策略之间的不可恢复率差异在 1.2–6 个百分点分辨率内**没有被检出**，但故意破坏的对照可以被检出。

## 主要限制
审计依赖 LongMemEval-S 的金标准证据和“可由金标准回答”的筛选，因此主要适用于基准分析。存储单元还必须与原始轮次或会话对齐，很多派生摘要型记忆无法直接套用。恢复金标准证据本身会改变读取上下文，残余错误也依赖读者。策略间的无差异结论只适用于本论文的策略、预算和统计分辨率。

## 记忆生命周期
| 阶段 | 测量对象 |
|---|---|
| 写入 | 不改变原有写入路径。 |
| 组织 | 保持源对齐单元，才能准确判断哪些证据仍存在。 |
| 读取 | 用成对恢复干预区分检索漏失与使用失败。 |
| 更新 / 遗忘 | 在明确 token 预算下测量淘汰造成的不可恢复任务损失。 |

## 为什么重要
问题从“哪个淘汰策略分数最高”变成**每个丢失答案到底坏在哪个生命周期阶段**。这会直接改变下一步应该优化保留、检索还是消费端使用。

## 延伸阅读
- [The Compaction Cliff](2608.22752.zh.md)：研究压缩后哪些类型需要精确保留。
- [RD-Forget](2609.10263.zh.md)：保留历史但改变当前使用资格。
- [Agent Memory 评测脉络](https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-memory)：基准演进由兄弟 Radar 维护。
''',
'2609.08273':'''# MemForest：把后处理压缩和读取补偿分开归因

**中文** | [English](2609.08273.md) · [返回首页](../../README.md) · [研究资料库](../../library/README.md)

[论文](https://arxiv.org/abs/2609.08273) · [代码](https://github.com/Celina-love-sweet/MemForest) · **发布日期：2026-09-08** · **重要性：4/5** · **置信度：高**

> **研究增量。** MemForest 把已经累积的记忆存储当成可压缩的系统对象：先按事件组织，再逐步合并节点；另一套时间传播检索可以补回部分质量。压缩和读取策略是两个干预，不能合并归因。

## 问题
外部记忆会持续增长。写入时缩短每条内容并不能约束总节点数，而通用裁剪或合并又可能忽略两个记忆特征：远距离节点可能语义相似，时间相邻节点也可能语义差异很大却属于同一事件。

## 机制
MemForest 用全局向量相似度与局部时间连续性把节点分到事件单元，每个事件构造成最大生成树，然后反复选择高权重节点对，由语言模型融合成新节点，直到达到目标压缩率。可选的 AGPR 先取更大的相似度候选集，再利用锚点附近的时间距离重新排序。

`已有记忆节点 → 语义+时间事件划分 → EventTree → 逐步语言模型合并 → 压缩存储 → 可选 AGPR`

## 最近的对照
表示层最干净的比较，是在相同压缩率下把 MemForest 与随机裁剪、KMeans、DART、StreamMeCo、随机合并和 ToMe 比较，并以未压缩的 Mem0 或 M3-Agent 为 100% 参考。AGPR 改变了读取策略，应与纯 MemForest 分开报告。

## 决定性证据
在 Mem0 上压缩 **50%** 时，纯 MemForest 保留未压缩平均性能的 **97.1%**，加入 AGPR 后为 **98.3%**；压缩到 **70%** 时纯 MemForest 降到 **93.3%**，质量边界是可见的。50% 压缩并使用 AGPR 后，检索时间在 LoCoMo 上从 **0.48→0.24 秒**、LongMemEval 从 **8.30→4.32 秒**、PersonaMem 从 **4.90→2.78 秒**。结果取三次运行平均，节点合并使用 GPT-4o-mini。

## 主要限制
AGPR 与压缩同时改变读取路径，因此组合方案多出来的质量不能归因给 EventTree 压缩。语言模型融合还可能损失原文、来源或冲突状态，论文没有直接测这些失败。当前实验主要是静态后处理，也没有给出持续更新、失效处理和长期重压缩策略。检索加速数字不包含向量化、分区、多次语言模型合并、存储改写与未来维护的完整生命周期成本。

## 记忆生命周期
| 阶段 | MemForest 的作用 |
|---|---|
| 写入 | 从其他记忆系统已经生成的节点开始。 |
| 组织 | 按语义与时间形成 EventTree，并破坏性融合选中的节点对。 |
| 读取 | 可使用普通相似度检索，也可加入 AGPR 时间传播。 |
| 更新 / 遗忘 | 通过合并达到目标节点压缩率；在线增量维护仍未解决。 |

## 为什么重要
后处理记忆大小应像索引维护一样评估：先在同一质量目标下比较压缩，再单独计算读取补偿和维护成本。下一步最有判别力的是增长数据流上的来源保留、失效处理与摊销成本实验。

## 延伸阅读
- [The Compaction Cliff](2608.22752.zh.md)：强调压缩过程中的类型化精确保留。
- [LeanMem](2608.03463.zh.md)：在生命周期更早的写入阶段改变记忆契约。
- [VoiceMem](2608.26005.zh.md)：给出另一种在线流式成本边界。
'''}
for pid,text in notes_en.items(): (ROOT/'papers'/'2026'/f'{pid}.md').write_text(text,encoding='utf-8')
for pid,text in notes_zh.items(): (ROOT/'papers'/'2026'/f'{pid}.zh.md').write_text(text,encoding='utf-8')

# Timeline entries.
def entry_en(pid,title,label,area,delta,question,evidence,ew,caveat,cw,maptext,code=None):
    code_link=f' · [Code]({code})' if code else ''
    return f'''<a id="entry-{pid.replace('.', '-')}"></a>\n<details><summary><strong>{TODAY} · {label}</strong> · {area} <!-- timefirst:area={area.lower().replace(' ','-')} --> — {delta} <!-- timefirst:delta={papers_by_id[pid]['direction']} --></summary>\n\n**Question.** {question} <!-- timefirst:question={papers_by_id[pid]['direction']} -->\n\n**Evidence.** {evidence} `{ew}`. <!-- timefirst:evidence={papers_by_id[pid]['direction']}~{ew.replace(' ','-')} -->\n\n**Caveat.** {caveat} `{cw}`. <!-- timefirst:caveat={papers_by_id[pid]['direction']}~{cw.replace(' ','-')} -->\n\n**Map.** `early_signal` — {maptext}\n\n**Links.** [Paper](https://arxiv.org/abs/{pid}) · [中文深读](papers/2026/{pid}.zh.md) · [English deep note](papers/2026/{pid}.md){code_link}\n\n</details>\n\n'''
def entry_zh(pid,label,area,delta,question,evidence,ew,caveat,cw,maptext,code=None):
    code_link=f' · [代码]({code})' if code else ''
    return f'''<a id="entry-{pid.replace('.', '-')}"></a>\n<details><summary><strong>{TODAY} · {label}</strong> · {area} <!-- timefirst:area={area_map[pid]} --> — {delta} <!-- timefirst:delta={papers_by_id[pid]['direction']} --></summary>\n\n**问题。** {question} <!-- timefirst:question={papers_by_id[pid]['direction']} -->\n\n**证据。** {evidence} `{ew}`。 <!-- timefirst:evidence={papers_by_id[pid]['direction']}~{ew.replace(' ','-')} -->\n\n**限制。** {caveat} `{cw}`。 <!-- timefirst:caveat={papers_by_id[pid]['direction']}~{cw.replace(' ','-')} -->\n\n**地图。** `early_signal` — {maptext}\n\n**链接。** [论文](https://arxiv.org/abs/{pid}) · [中文深读](papers/2026/{pid}.zh.md) · [英文深读](papers/2026/{pid}.md){code_link}\n\n</details>\n\n'''
papers_by_id={p['id']:p for p in papers}
area_map={'2609.10263':'query-conditioned-storage-use','2609.08279':'restore-counterfactual-eviction-audit','2609.08273':'event-structured-posthoc-compression'}
new_en=''.join([
entry_en('2609.10263',papers_by_id['2609.10263']['title'],'RD-Forget','Write / Update → query-conditioned use','keeps history stored while suppressing superseded state only for the current use context.','Does forgetting require deleting old memory, or can the system preserve history while changing which state is admissible for the current query?','Matched Luna Full scores 91.86/93.59/74.00; removing forgetting falls to 68.60/60.26/51.00, the largest deficit on all three suites, giving','matched Luna forget ablation largest deficit','The archive is retained, the curator sees the question/task metadata, and lifecycle cost is incomplete; this cannot support privacy-erasure claims, so','retained archive is not physical erasure','Storage/use separation is a strong lifecycle coordinate; one paper does not establish a durable forgetting direction.'),
entry_en('2609.08279',papers_by_id['2609.08279']['title'],'What Eviction Destroys','Evaluation → forgetting failure localization','restores gold evidence per question to separate eviction destruction from retrieval miss and reader failure.','When a budgeted memory answer fails, was indispensable evidence deleted, merely not retrieved, or present but unused?','At top-k/80k, the irreversible share among restoration-corrected errors is 0.71 FIFO, 0.73 random, 0.67 redundancy-aware, and 0.60 LLM-importance; the matched-accuracy policy comparison is null at the reported resolution, giving','irreversible share 0.67 to 0.73','The audit needs benchmark gold evidence and source-aligned units, while restoration changes the read context;','gold restore is a benchmark audit','Failure localization raises the evaluation standard without selecting a best eviction policy.'),
entry_en('2609.08273',papers_by_id['2609.08273']['title'],'MemForest','Representation → post-hoc compression','compresses accumulated memory with EventTrees and separately adds temporal propagation at read time.','Can an already accumulated external-memory store be compressed without conflating representation savings with a changed retrieval policy?','With Mem0, plain MemForest at 50% compression retains 97.1% of baseline aggregate performance; at 70% it retains 93.3%, while 50%+AGPR roughly halves LoCoMo retrieval time, giving','fifty percent compression retains 97.1 percent','AGPR changes retrieval with compression, LM fusion may lose provenance/conflicts, and full repartition/merge maintenance cost is missing;','agpr changes retrieval with compression','Post-hoc compression is a useful systems coordinate; the combined retrieval package does not isolate EventTree causality.',papers_by_id['2609.08273']['code_url'])])
new_zh=''.join([
entry_zh('2609.10263','RD-Forget','写入 / 更新 → 按查询控制使用','保留完整历史，但只对当前用途压制已被替代的状态。','遗忘是否必须删除旧记忆，还是可以保留历史、只改变当前问题允许使用的状态？','匹配的 Luna 完整配置为 91.86/93.59/74.00；关闭遗忘后降到 68.60/60.26/51.00，三个数据集都是最大降幅，对应','matched Luna forget ablation largest deficit','原始历史仍被保留，整理器还看到了问题与任务元数据，而且没有完整生命周期成本；因此不能把它解释为隐私擦除，即','retained archive is not physical erasure','“存储”和“当前允许使用”值得分开评测；单篇论文不足以形成稳定遗忘方向。'),
entry_zh('2609.08279','What Eviction Destroys','评测 → 定位遗忘失败','逐题恢复金标准证据，把淘汰摧毁、检索漏失和读者使用失败分开。','有预算的记忆答错时，关键证据究竟已被删除、仍在但没检索到，还是出现后没有被正确使用？','在 top-k、80k 预算下，恢复可纠正错误中的不可恢复占比为 FIFO 0.71、随机 0.73、冗余感知 0.67、LLM 重要性 0.60；准确率匹配后的策略差异没有被检出，对应','irreversible share 0.67 to 0.73','该审计依赖基准金标准和源对齐单元，恢复证据本身也会改变读取上下文，即','gold restore is a benchmark audit','它提高了失败定位的评测标准，但并没有选出一个普适最优淘汰策略。'),
entry_zh('2609.08273','MemForest','表示与组织 → 后处理压缩','用 EventTree 压缩已累积记忆，并把时间传播检索作为另一项读取干预。','已经持续增长的外部记忆能否被压缩，同时不把表示层节省和新的检索策略混成一个收益？','在 Mem0 上，纯 MemForest 压缩 50% 后保留基线平均性能的 97.1%，压缩 70% 时为 93.3%；50% 压缩并加入 AGPR 后 LoCoMo 检索时间约减半，对应','fifty percent compression retains 97.1 percent','AGPR 与压缩同时改变读取，语言模型融合还可能损失来源和冲突状态，且缺少持续分区与合并的完整维护成本，即','agpr changes retrieval with compression','后处理压缩值得成为独立系统坐标；组合检索方案不能证明 EventTree 是全部收益来源。',papers_by_id['2609.08273']['code_url'])])

# Direction lines use one canonical support each.
def dir_en(pid,label,claim,imp,witness):
 key=papers_by_id[pid]['direction']; return f'- **`new_signal` · {label} · {claim}** Supports: [{label}](#entry-{pid.replace(".", "-")}); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication ({imp}): {witness}. Exact synthesis time: `{RADAR_TS}`. <!-- timefirst:direction key="{key}" state="new_signal" supports="{pid}" confidence="medium" implication="{imp}" timing="radar_published_at" synthesized="{RADAR_TS}" prior="none" -->'
def dir_zh(pid,label,claim,imp,witness):
 key=papers_by_id[pid]['direction']; return f'- **`new_signal` · {label} · {claim}** 支撑：[{label}](#entry-{pid.replace(".", "-")})；置信度：**medium**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（{imp}）：{witness}。精确合成时间：`{RADAR_TS}`。 <!-- timefirst:direction key="{key}" state="new_signal" supports="{pid}" confidence="medium" implication="{imp}" timing="radar_published_at" synthesized="{RADAR_TS}" prior="none" -->'
new_dirs_en=[
 dir_en('2609.10263','RD-Forget','Storage and current-use authority should be evaluated separately.','separate-retention-from-query-local-admission','hold the source archive and reader fixed, then vary supersession/admission and destructive deletion independently'),
 dir_en('2609.08279','What Eviction Destroys','Budget loss needs stage-local diagnosis before policy ranking.','audit-eviction-retrieval-and-utilization-separately','report retrieval regime and use paired restoration to separate destroyed evidence, retrieval misses, and reader failures'),
 dir_en('2609.08273','MemForest','Post-hoc store compression and retrieval recovery are separate interventions.','match-compression-and-read-policy-costs','compare equal compression ratios first, then vary AGPR separately and include merge/update maintenance cost')]
new_dirs_zh=[
 dir_zh('2609.10263','RD-Forget','应分别评测“仍被保留”和“当前有权使用”。','separate-retention-from-query-local-admission','固定源历史与读者，再分别改变替代状态准入和破坏性删除'),
 dir_zh('2609.08279','What Eviction Destroys','比较淘汰策略前，应先定位预算损失发生在哪一层。','audit-eviction-retrieval-and-utilization-separately','必须报告读取协议，并用成对恢复区分证据摧毁、检索漏失与读者使用失败'),
 dir_zh('2609.08273','MemForest','后处理存储压缩与读取补偿是两个不同干预。','match-compression-and-read-policy-costs','先在相同压缩率下比较表示，再单独改变 AGPR，并计入合并、更新和维护成本')]

def update_readme(path,lang):
    t=path.read_text(encoding='utf-8')
    t=re.sub(r'(Last updated:|最后更新：) \*\*\d{4}-\d{2}-\d{2}\*\*',lambda m:m.group(1)+f' **{TODAY}**',t,count=1)
    marker='<a id="entry-2608-29606"></a>'
    if marker not in t: raise SystemExit('timeline marker missing')
    t=t.replace(marker,(new_en if lang=='en' else new_zh)+marker,1)
    a='<a id="last-7-days"></a>'; b='<a id="last-30-days"></a>'; c='<a id="field-map"></a>'
    s=t.index(a); m=t.index(b,s); e=t.index(c,m)
    thirty=t[m:e]
    # Keep only existing direction list items; all current native supports remain inside the new 30-day window.
    old_lines=[line for line in thirty.splitlines() if line.startswith('- **`') and 'timefirst:direction' in line]
    old_lines=[line.replace(OLD_TS,RADAR_TS) for line in old_lines]
    if lang=='en':
      seven=f'{a}\n### Last 7 days: {SEVEN_START}—{END}\n\n'+"\n".join(new_dirs_en)+'\n\n'
      thirty_new=f'{b}\n### Last 30 days: {THIRTY_START}—{END}\n\n'+"\n".join(new_dirs_en+old_lines)+'\n\n'
    else:
      seven=f'{a}\n### 过去 7 天：{SEVEN_START}—{END}\n\n'+"\n".join(new_dirs_zh)+'\n\n'
      thirty_new=f'{b}\n### 过去 30 天：{THIRTY_START}—{END}\n\n'+"\n".join(new_dirs_zh+old_lines)+'\n\n'
    t=t[:s]+seven+thirty_new+t[e:]
    path.write_text(t,encoding='utf-8')
update_readme(ROOT/'README.en.md','en'); update_readme(ROOT/'README.md','zh')

# Update Library research lines without creating a parallel map.
for path in [ROOT/'library/README.en.md',ROOT/'library/README.md']:
    t=path.read_text(encoding='utf-8')
    t=t.replace('[The Compaction Cliff](../papers/2026/2608.22752.md) → [MemGuard](../papers/2026/2608.21867.md)', '[The Compaction Cliff](../papers/2026/2608.22752.md) → [MemForest](../papers/2026/2609.08273.md) → [MemGuard](../papers/2026/2608.21867.md)')
    t=t.replace('[The Compaction Cliff](../papers/2026/2608.22752.zh.md) → [MemGuard](../papers/2026/2608.21867.zh.md)', '[The Compaction Cliff](../papers/2026/2608.22752.zh.md) → [MemForest](../papers/2026/2609.08273.zh.md) → [MemGuard](../papers/2026/2608.21867.zh.md)')
    t=t.replace('[StateMemBench / StateMem](../papers/2026/2608.19652.md) → [When Stale Constraints Go Unchecked]', '[StateMemBench / StateMem](../papers/2026/2608.19652.md) → [RD-Forget](../papers/2026/2609.10263.md) → [When Stale Constraints Go Unchecked]')
    t=t.replace('[StateMemBench / StateMem](../papers/2026/2608.19652.zh.md) → [When Stale Constraints Go Unchecked]', '[StateMemBench / StateMem](../papers/2026/2608.19652.zh.md) → [RD-Forget](../papers/2026/2609.10263.zh.md) → [When Stale Constraints Go Unchecked]')
    t=t.replace('[Demystifying Agent Skills](../papers/2026/2608.14036.md) →', '[What Eviction Destroys](../papers/2026/2609.08279.md) → [Demystifying Agent Skills](../papers/2026/2608.14036.md) →')
    t=t.replace('[Demystifying Agent Skills](../papers/2026/2608.14036.zh.md) →', '[What Eviction Destroys](../papers/2026/2609.08279.zh.md) → [Demystifying Agent Skills](../papers/2026/2608.14036.zh.md) →')
    path.write_text(t,encoding='utf-8')

# Closed W36 digest: membership is Radar acceptance, not source publication.
w36_en=f'''# Agent Memory Weekly — 2026-W36\n\n[中文](2026-W36.zh.md) · [All compactions](../README.md)\n\n**Window:** 2026-08-31 to 2026-09-06  \n**Accepted papers:** 2  \n**Highest importance:** 4/5\n\n## The week in one sentence\n\nThe important movement was not a new memory architecture: **Hindsight Memory-PRM raised the causal standard for learning memory operations, while Agent Zero Memory showed how much can already move under a fixed memory package by changing retrieval/backbone.** Together they make component attribution, downstream behavioral effect, and lifecycle cost harder requirements for any future “memory gain.”\n\n## What actually changed\n\n### 1. Memory learning needs intervention-calibrated credit, not successful-trajectory correlation\n\nHindsight Memory-PRM holds the scaffold, retriever, answerer, and judge fixed while improving the supervision used for Write / Merge / Noop. On LoCoMo, **63.4 outcome-only → 70.2 observational → 77.5 full**; the last **+7.3 points** comes from intervention-calibrated flip/toxicity information, while matched-scale and shuffled-flip controls stay near 70.5. Its deletion audit also finds that removing the **74.6%** of entries outside every read path changes accuracy by only **−0.1 points**.\n\nThe cost is part of the result: the offline audit is about **1.6M API calls / $1.1k** on LoCoMo and **9.8M / $6.5k** on LongMemEval. Entry-presence utility still is not the ideal causal contribution of the original write/merge action.\n\n### 2. A richer memory package still needs a strong interface control\n\nAgent Zero Memory exposes one history through episodic, graph, and documentary views with provenance links and citation-locked reading. But its cleanest matched result is narrower: with gpt-5.6-sol and the rest of the pipeline fixed, LongMemEval is **95.20 hybrid / 94.00 embedding-only / 93.60 grep-only / 93.40 lexical-only**. A separate fixed-memory/retriever/control backbone sweep spans **92.20–95.60** while per-query cost changes by roughly **30×**.\n\nThat supports complementary retrieval and strong backbone/cost sensitivity. It does **not** isolate the causal value of three stores, provenance locking, or the intent gate because remove-one-component ablations are missing and build/maintenance cost is incomplete.\n\n## Research-design implication\n\nThe next memory paper should state exactly which lifecycle stage is being credited. For learned writes, compare observational supervision with paired downstream interventions and price the audit. For multi-view stores, freeze the reader, source archive, interface, and resource budget, then remove one store/provenance/admission mechanism at a time. A package score is evidence for the package until this decomposition exists.\n\n## Field Map\n\nBoth accepted works are `early_signal`. They sharpen the evidence standard for learning and provenance-aware access, but two different direction keys do not establish one reinforced trend and do not justify a durable Field Map edit.\n\n## Coverage note\n\nThis closed compaction contains exactly the native records whose `radar_published_at` falls in 2026-08-31 through 2026-09-06: **Hindsight Memory-PRM (2608.29605)** and **Agent Zero Memory (2608.29606)**. Later September papers are not backdated into W36 by source publication date.\n'''
w36_zh=f'''# Agent Memory 周报 — 2026-W36\n\n**中文** · [English](2026-W36.md) · [全部合成](../README.zh.md)\n\n**窗口：** 2026-08-31 至 2026-09-06  \n**Radar 接受论文：** 2  \n**最高重要性：** 4/5\n\n## 一句话判断\n\n这一周真正变化的不是出现了新记忆架构，而是**Hindsight Memory-PRM 抬高了记忆操作学习的因果证据门槛，Agent Zero Memory 则说明在固定记忆系统后，仅检索接口和基础模型变化就能带来不可忽略的波动**。以后任何“记忆带来增益”的结论，都更需要组件归因、下游行为效应和生命周期成本同时成立。\n\n## 真正发生的变化\n\n### 1. 学习记忆操作需要干预校准，而不只是成功轨迹相关性\n\nHindsight Memory-PRM 固定框架、检索器、回答器和评判器，只改变 Write / Merge / Noop 的监督信息。LoCoMo 从 **63.4 outcome-only → 70.2 observational → 77.5 full**；最后 **+7.3 个百分点**只增加干预校准的翻转 / 毒性信息，而匹配规模和打乱翻转标签的对照都停在约 70.5。删除审计还显示，去掉 **74.6%** 从未进入读取路径的条目，准确率只变化 **−0.1 个百分点**。\n\n这项提升有明确代价：离线审计在 LoCoMo 约需 **160 万次 API 调用 / 1,100 美元**，LongMemEval 约需 **980 万次 / 6,500 美元**。而且“条目存在与否”的效用仍不等于原始写入或合并动作的理想因果贡献。\n\n### 2. 更复杂的记忆系统仍然需要强接口对照\n\nAgent Zero Memory 把同一历史暴露为时间线、图和文档三种视图，并保留来源链接与引用约束。但最干净的匹配结果更窄：固定 gpt-5.6-sol 与其余流程后，LongMemEval 为 **95.20 hybrid / 94.00 embedding-only / 93.60 grep-only / 93.40 lexical-only**。另一组固定记忆、检索器与控制逻辑的基础模型扫描在 **92.20–95.60** 之间变化，而单查询成本相差约 **30 倍**。\n\n这些证据支持“检索通道互补”和“基础模型 / 成本敏感”，却不能单独证明三存储、来源约束或意图门控是 headline 的原因，因为缺少逐组件移除实验，构建与维护成本也不完整。\n\n## 研究设计含义\n\n下一篇记忆论文应明确自己在给哪个生命周期阶段记功。学习写入时，应把观察性监督与成对下游干预比较，并把审计计算量计入成本；多视图存储则应固定读者、源历史、接口和资源预算，再逐项移除存储、来源约束和使用准入。没有这种拆分时，总分只能证明整套系统。\n\n## 领域地图\n\n两篇接受工作都是 `early_signal`。它们分别抬高了学习归因和来源感知读取的证据标准，但属于不同方向键，不能合并成强化趋势，也不足以修改稳定 Field Map。\n\n## 覆盖说明\n\n本闭周期合成只包含 `radar_published_at` 落在 2026-08-31 至 2026-09-06 的两条原生记录：**Hindsight Memory-PRM（2608.29605）**与 **Agent Zero Memory（2608.29606）**。9 月后续论文不会因为来源发布日期而被回填进 W36。\n'''
(ROOT/'digests'/'weekly'/'2026-W36.md').write_text(w36_en,encoding='utf-8')
(ROOT/'digests'/'weekly'/'2026-W36.zh.md').write_text(w36_zh,encoding='utf-8')

# Update compaction indexes.
for path in [ROOT/'digests'/'README.md',ROOT/'digests'/'README.zh.md']:
    t=path.read_text(encoding='utf-8')
    if '2026-W36' not in t:
      marker='| **Weekly** |'
      idx=t.index(marker)
      if path.name=='README.md': row='| **Weekly** | [2026-W36 — Attribution before architecture](weekly/2026-W36.md) ([中文](weekly/2026-W36.zh.md)) | Two early signals raise the bar for intervention-calibrated memory credit and component-matched multi-view memory evaluation; the durable map stays unchanged. |\n'
      else: row='| **周报** | [2026-W36 — 先做归因，再谈架构](weekly/2026-W36.zh.md) ([English](weekly/2026-W36.md)) | 两个早期信号分别抬高记忆操作因果归因与多视图记忆组件对照的门槛；稳定地图不变。 |\n'
      t=t[:idx]+row+t[idx:]
    t=t.replace('W35 and the 2026-08 monthly digest are closed','W36, W35, and the 2026-08 monthly digest are closed')
    t=t.replace('W35 与 2026-08 月报已经封存','W36、W35 与 2026-08 月报已经封存')
    path.write_text(t,encoding='utf-8')

# Advance validator's repository-owned exact public cutoff/window constants.
v=ROOT/'scripts'/'validate_reading.py'; t=v.read_text(encoding='utf-8')
t=re.sub(r'SYNTHESIS_TIMESTAMP = "[^"]+"',f'SYNTHESIS_TIMESTAMP = "{RADAR_TS}"',t,count=1)
t=re.sub(r'"last-7-days": \(date\([^\n]+\), date\([^\n]+\)\),',f'"last-7-days": (date(2026, 9, 5), date(2026, 9, 11)),',t,count=1)
t=re.sub(r'"last-30-days": \(date\([^\n]+\), date\([^\n]+\)\),',f'"last-30-days": (date(2026, 8, 13), date(2026, 9, 11)),',t,count=1)
v.write_text(t,encoding='utf-8')

# Update current-date fixtures that construct repository-valid period projections; leave adversarial timestamps untouched where not exact replacements.
test=ROOT/'tests'/'test_memory_v2_contract.py'; tt=test.read_text(encoding='utf-8')
tt=tt.replace('synthesized: str = "2026-09-03T01:19:15Z"',f'synthesized: str = "{RADAR_TS}"')
tt=tt.replace('### 过去 7 天：2026-08-28—2026-09-03','### 过去 7 天：2026-09-05—2026-09-11')
tt=tt.replace('### 过去 30 天：2026-08-05—2026-09-03','### 过去 30 天：2026-08-13—2026-09-11')
tt=tt.replace('### Last 7 days: 2026-08-28—2026-09-03','### Last 7 days: 2026-09-05—2026-09-11')
tt=tt.replace('### Last 30 days: 2026-08-05—2026-09-03','### Last 30 days: 2026-08-13—2026-09-11')
test.write_text(tt,encoding='utf-8')
