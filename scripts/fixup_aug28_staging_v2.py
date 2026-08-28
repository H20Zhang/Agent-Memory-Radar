from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def save(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def rep(text: str, old: str, new: str, label: str, count: int = 1) -> str:
    if old not in text:
        raise RuntimeError(f"{label}: missing anchor {old[:120]!r}")
    return text.replace(old, new, count)


# Finish Chinese localization at both scan and expansion layers.
path = "README.md"
text = load(path)
for old, new in {
    "· 有预算的陈旧记忆验证 <!-- timefirst:area=stale-memory-verification-allocation --> — provenance 完整仍不够；稀缺 verification slot 必须分配到真正可能失效的约束。":
    "· 有预算的陈旧记忆验证 <!-- timefirst:area=stale-memory-verification-allocation --> — 仅保留 provenance 仍不够；稀缺 verification slot 必须分配到真正可能失效的约束。",
    "· Episode integrity reconstruction <!-- timefirst:area=episode-integrity-reconstruction --> — 对交错 conversation 先恢复 coherent episode，再做层级检索与 evidence assembly。":
    "· 片段完整性重建 <!-- timefirst:area=episode-integrity-reconstruction --> — 对交错 conversation 先恢复 coherent episode，再做层级检索与 evidence assembly。",
    "· Streaming dual-brain memory <!-- timefirst:area=streaming-dual-brain-memory --> — 将 factual/entity state 与 affect/persona state 分成并行 streaming memory path，并让上层 organization/routing 可跨 backend 复用。":
    "· 流式双脑记忆 <!-- timefirst:area=streaming-dual-brain-memory --> — 将 factual/entity state 与 affect/persona state 分成并行 streaming memory path，并让上层 organization/routing 可跨 backend 复用。",
    "**限制。** segmentation、deterministic summary、hierarchy 与 routing 联合变化；SCALE-QA 还是合成四选一 benchmark，且 TSIM 的 ingest / retrieval 开销明显高于 standard RAG，因此 `full lifecycle cost must be matched`。":
    "**限制。** 这些 segmentation、deterministic summary、hierarchy 与 routing 会联合变化；SCALE-QA 还是合成四选一 benchmark，且 TSIM 的 ingest / retrieval 开销明显高于 standard RAG，因此 `full lifecycle cost must be matched`。",
    "**限制。** 这个 `134ms` 只统计 memory retrieval latency，并非端到端 conversational latency；异步 extraction、tagging 与 graph write 只是把成本移出 critical path，完整 backlog、energy、consistency 与 deletion cost 仍缺失，即 `full streaming lifecycle cost missing`。":
    "**限制。** 这个 `134ms` 只统计记忆检索延迟，并非端到端对话延迟；异步抽取、标注与图写入只是把成本移出关键路径，完整的积压、能耗、一致性与删除成本仍缺失，即 `full streaming lifecycle cost missing`。",
    "对应 `fixed glm 5 2 workflow`。":
    "对应 `fixed glm 5.2 workflow`。",
}.items():
    text = rep(text, old, new, path)
save(path, text)

path = "README.en.md"
text = load(path)
text = rep(text, "in the `fixed glm 5 2 workflow`.", "in the `fixed glm 5.2 workflow`.", path)
save(path, text)

# Test fixtures should remain inside today's 7-day window while being newer
# than every real acceptance, so the helper's insertion point is unambiguous.
path = "tests/test_memory_v2_contract.py"
text = load(path)
text = rep(text, 'radar_published_at: str = "2026-08-22T01:18:00Z"', 'radar_published_at: str = "2026-08-28T00:30:00Z"', path)
text = rep(text, '"first_seen_at": "2026-08-22T01:18:00Z"', '"first_seen_at": "2026-08-28T00:30:00Z"', path)
text = rep(text, "marker = '<a id=\"entry-2608-17911\"></a>'", "marker = '<a id=\"entry-2608-25329\"></a>'", path)
text = rep(text, 'record["published_at"] = "2026-08-22T00:00:00Z"', 'record["published_at"] = "2026-08-28T00:31:00Z"', path)
save(path, text)

Path(__file__).unlink()
