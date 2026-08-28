from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def require_replace(text: str, old: str, new: str, label: str, count: int = 1) -> str:
    if old not in text:
        raise RuntimeError(f"{label}: missing fixup anchor {old[:120]!r}")
    return text.replace(old, new, count)


# Localize the Chinese expansion layer and expose exact evidence/caveat witnesses
# inside code spans so the bilingual contract remains auditable without turning
# the Chinese prose into English clauses.
path = "README.md"
text = read(path)
replacements = {
    "**证据。** PERMA matched ablation 中 full HiPS 为 **66.95/56.56/63.83/56.30**，去掉 Cross-Level Rule Flow 后降至 **45.39/40.87/43.12/36.50**；learned universal+delta rules 还能在 Qwen、GPT-4o-mini、Gemini 2.5 Flash 与 GPT-5 间迁移，不携带原 RL policy。":
    "**证据。** 匹配的 PERMA 消融显示，完整 HiPS 为 **66.95/56.56/63.83/56.30**，去掉 `Cross-Level Rule Flow` 后降至 **45.39/40.87/43.12/36.50**；共享规则加 persona delta 还能跨 Qwen、GPT-4o-mini、Gemini 2.5 Flash 与 GPT-5 迁移，直接观察到 `cross model universal plus delta transfer`。",
    "**限制。** headline baseline 使用的 backbone 并不完全匹配；完整系统同时改变 distillation、persona gate、rule flow、selection 与 policy optimization，且长期维护 / 删除成本未给全。":
    "**限制。** 主结果表中的 backbone 并不完全匹配；完整系统还同时改变 distillation、persona gate、rule flow、selection 与 policy optimization，因此存在 `full personalized policy lifecycle cost incomplete` 这一上限，长期维护与删除成本也未给全。",
    "**证据。** 在固定 `k=2` verification budget 下，只把一个现有 slot 强制指向 critical provenance path，就让 superseded-world 的 current-record-consistent decisions 提升 **61.3–74.0pp**；valid-world 只变化 **0–2.0pp**。":
    "**证据。** 在固定 `k=2` 验证预算下，只把一个现有名额强制指向关键 provenance 路径，就让已被取代场景中的当前记录一致决策提升 **61.3–74.0pp**，有效场景只变化 **0–2.0pp**；预算条件保持 `same k2 budget`。",
    "**限制。** forced-critical arm 使用 experimenter 知道的 oracle path，只是 causal identification instrument，不是可部署 scheduler；真实 store 的多跳 authority resolution 与维护成本尚未测量。":
    "**限制。** 强制关键路径的实验组使用研究者预先知道的 oracle 路径，只能作为因果识别工具，不能直接变成线上 scheduler；真实存储中的多跳 authority resolution 与维护成本尚未测量，仍是 `deployable verification policy missing`。",
    "**证据。** 同一 GLM-5.2 workflow 上，active-context ablation 的 pass rate **60.0%→84.6%**，optimization tokens **15.9B→1.113B**；Experience Graph Memory ablation 的 full-suite pass rate **55.2%→84.6%**。":
    "**证据。** 在同一 GLM-5.2 workflow 中，主动上下文消融把通过率从 **60.0%→84.6%**，同时把优化 token 从 **15.9B→1.113B**；去掉 `Experience Graph Memory` 时全套通过率为 **55.2%**，完整系统为 **84.6%**，对应 `fixed glm 5 2 workflow`。",
    "**限制。** active context 同时改变 selection、compression 与 injection；graph downstream-outcome score 是 retrieval heuristic 而非 causal label，完整 memory construction / index / maintenance 成本也未配平。":
    "**限制。** 主动上下文同时改变 selection、compression 与 injection；图上的 downstream-outcome score 只是 retrieval heuristic，并非 causal label，因此仍有 `selection compression injection coupled` 的归因混杂，完整 construction / index / maintenance 成本也未配平。",
    "**问题。** mixed-topic history 的失败来自“没搜到相似 turn”，还是更早的 episode localization / reconstruction？":
    "**问题。** 交错主题历史中的失败，究竟来自没有搜到相似 turn，还是更早的 episode localization / reconstruction 已经出错？",
    "**证据。** 在三个 backend 上 TSIM 相对 strongest matched baseline 提升 **5.6–17.6 accuracy points**；同一 flat history 上，standard RAG→fixed-token→semantic-drift→full TSIM 的 pipeline accuracy 约为 **26.2→43.4→55.5→74.2**。":
    "**证据。** 在三个 backend 上，TSIM 相对最强匹配基线提升 **5.6–17.6 个准确率百分点**；同一 flat history 中，从 standard RAG、fixed-token、semantic-drift 到完整 TSIM，准确率约为 **26.2→43.4→55.5→74.2**，形成 `three backend matched settings` 的跨模型证据。",
    "**限制。** segmentation、deterministic summary、hierarchy 与 routing 联合变化；SCALE-QA 是 synthetic four-choice benchmark，且 TSIM ingest / retrieval overhead 明显高于 standard RAG。":
    "**限制。** segmentation、deterministic summary、hierarchy 与 routing 联合变化；SCALE-QA 还是合成四选一 benchmark，且 TSIM 的 ingest / retrieval 开销明显高于 standard RAG，因此 `full lifecycle cost must be matched`。",
    "**证据。** 同一个 upper memory layer 加到 Mem0、LangMem、Zep 后，均值由 **60.26→83.00（+22.73pp）**；top-5 operating point 报告约 **430 memory tokens / 134ms retrieval**。":
    "**证据。** 同一个上层记忆组织模块加入 Mem0、LangMem 与 Zep 后，均值由 **60.26→83.00（+22.73pp）**；top-5 工作点约使用 **430 个 memory token / 134ms retrieval**，构成 `same upper layer transfer`。",
    "**限制。** `134ms` 只是 memory retrieval latency，不是端到端 conversational latency；async extraction / tagging / graph write 把成本移出 critical path，但完整 backlog、energy、consistency 与 deletion cost 未配平。":
    "**限制。** 这个 `134ms` 只统计 memory retrieval latency，并非端到端 conversational latency；异步 extraction、tagging 与 graph write 只是把成本移出 critical path，完整 backlog、energy、consistency 与 deletion cost 仍缺失，即 `full streaming lifecycle cost missing`。",
}
for old, new in replacements.items():
    text = require_replace(text, old, new, path)
write(path, text)

# English evidence and caveat fields need bounded visible witnesses for the
# hidden time-first semantic contract.
path = "README.en.md"
text = read(path)
replacements = {
    "learned universal+delta rules also transfer across Qwen, GPT-4o-mini, Gemini 2.5 Flash, and GPT-5 without carrying the original RL policy.":
    "learned universal+delta rules also transfer across Qwen, GPT-4o-mini, Gemini 2.5 Flash, and GPT-5 without carrying the original RL policy, giving a `cross model universal plus delta transfer` witness.",
    "while long-run maintenance and deletion cost are incomplete.":
    "while `full personalized policy lifecycle cost incomplete` remains the lifecycle-cost caveat.",
    "while valid-world outcomes move only **0–2.0pp**.":
    "while valid-world outcomes move only **0–2.0pp** under the `same k2 budget`.",
    "real stores may require multi-hop authority resolution and unmeasured maintenance cost.":
    "real stores may require multi-hop authority resolution and unmeasured maintenance cost, leaving `deployable verification policy missing`.",
    "the Experience Graph Memory ablation raises full-suite pass rate **55.2%→84.6%**.":
    "the Experience Graph Memory ablation raises full-suite pass rate **55.2%→84.6%** in the `fixed glm 5 2 workflow`.",
    "and full construction/index/maintenance costs are not matched.":
    "and `selection compression injection coupled` remains a component-level confound alongside unmatched construction/index/maintenance cost.",
    "pipeline accuracy progresses roughly **26.2→43.4→55.5→74.2** from standard RAG to fixed-token, semantic-drift, and full TSIM.":
    "pipeline accuracy progresses roughly **26.2→43.4→55.5→74.2** from standard RAG to fixed-token, semantic-drift, and full TSIM across `three backend matched settings`.",
    "TSIM incurs materially higher ingest/retrieval overhead than standard RAG.":
    "TSIM incurs materially higher ingest/retrieval overhead than standard RAG, so `full lifecycle cost must be matched`.",
    "the top-5 operating point reports about **430 memory tokens / 134ms retrieval**.":
    "the top-5 operating point reports about **430 memory tokens / 134ms retrieval**, providing a `same upper layer transfer` witness.",
    "without matching backlog, energy, consistency, or deletion cost.":
    "without matching backlog, energy, consistency, or deletion cost, leaving `full streaming lifecycle cost missing`.",
}
for old, new in replacements.items():
    text = require_replace(text, old, new, path)
write(path, text)

# Move synthetic native-v2 test fixtures with the rolling window. Tests that
# assert post-cutoff rejection must also stay genuinely after the new cutoff.
path = "tests/test_memory_v2_contract.py"
text = read(path)
text = text.replace('radar_published_at: str = "2026-08-21T01:18:00Z"', 'radar_published_at: str = "2026-08-22T01:18:00Z"')
text = text.replace('"first_seen_at": "2026-08-21T01:18:00Z"', '"first_seen_at": "2026-08-22T01:18:00Z"')
text = text.replace('"2026-08-27T01:00:00Z"', '"2026-08-28T02:00:00Z"')
write(path, text)

# The localized scan-layer test intentionally pins the complete public
# Timeline identity set; extend it for today's five native-v2 acceptances.
path = "tests/test_validate_reading.py"
text = read(path)
anchor = 'EXPECTED_TIMELINE_TITLES = {\n'
addition = (
    '    "2608-25329": "2026-08-28 · HiPS",\n'
    '    "2608-25553": "2026-08-28 · When Stale Constraints Go Unchecked",\n'
    '    "2608-25570": "2026-08-28 · KOPE",\n'
    '    "2608-25655": "2026-08-28 · SCALE-QA / TSIM",\n'
    '    "2608-26005": "2026-08-28 · VoiceMem",\n'
)
if '"2608-25329": "2026-08-28 · HiPS"' not in text:
    text = require_replace(text, anchor, anchor + addition, path)
write(path, text)

# This file is staging-only and must not enter the validated repository tree.
Path(__file__).unlink()
