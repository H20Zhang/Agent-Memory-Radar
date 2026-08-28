from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTSIDE_SEVEN_DAY = {"2608.18704", "2608.18719", "2608.18852", "2608.19013", "2608.19197"}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


# Natural Chinese map prose for the new episode-integrity entry.
path = "README.md"
text = read(path)
old = "**地图。** `early_signal` — episode integrity 是值得单独测的边界，但当前 package 尚未隔离哪个 representation operation 承担增益。"
new = "**地图。** `early_signal` — 片段完整性值得成为独立测量边界，但当前 package 尚未隔离究竟是哪一种 representation operation 承担增益。"
if old not in text:
    raise RuntimeError("missing SCALE-QA map localization anchor")
text = text.replace(old, new, 1)
write(path, text)

# Advancing the 7-day endpoint from Aug 27 to Aug 28 evicts Aug-21 Radar
# acceptances. Keep them in the 30-day section, but not in the exact 7-day view.
for path in ("README.md", "README.en.md"):
    text = read(path)
    start = text.index('<a id="last-7-days"></a>')
    end = text.index('<a id="last-30-days"></a>', start)
    before, section, after = text[:start], text[start:end], text[end:]
    kept = []
    for line in section.splitlines():
        if "timefirst:direction" in line and any(f'supports="{identity}"' in line for identity in OUTSIDE_SEVEN_DAY):
            continue
        kept.append(line)
    section = "\n".join(kept)
    if not section.endswith("\n"):
        section += "\n"
    write(path, before + section + after)

Path(__file__).unlink()
