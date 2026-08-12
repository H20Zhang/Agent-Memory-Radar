# Visual Assets

Research visuals are published as compressed WebP under one stable namespace:

```text
assets/visuals/
├── <arxiv-id>.webp
├── weekly-<YYYY-Www>-research-map.webp
├── monthly-<YYYY-MM>-design-space-map.webp
└── yearly-<YYYY>-research-map.webp
```

Per-paper figures are required for papers with importance >= 4 and optional when a lower-importance paper materially benefits from visual explanation. Weekly, monthly, and yearly compactions also require research maps. See [`../VISUAL_POLICY.md`](../VISUAL_POLICY.md) for grounding and iterative visual-QA requirements.

A visual is **published** only when the WebP exists on `main`, the corresponding Markdown page embeds that exact path, and the canonical record has passed grounding/link/path verification. A local render or draft brief is not publication and must never be marked `generated`.

Binary images should be committed together with the Markdown page that embeds them. Do not leave orphaned images, references to missing assets, or canonical `generated` states whose binary is absent.
