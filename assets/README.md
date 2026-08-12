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

## Binary publication through the GitHub connector

When the text-file contents API is insufficient for a WebP, use the Git data path rather than declaring binary upload unavailable:

1. Encode the final QA-passed WebP as base64 and call `create_blob` with `encoding=base64`.
2. Create text blobs for the Markdown/JSON changes that reference the image.
3. Create one tree from the current `main` base tree containing the binary and all referencing text paths.
4. Create one commit from that tree and update `refs/heads/main` non-forcibly.
5. Fetch the committed paths from `main` and only then set/retain `visual_explainer.status = generated`.

A failed text-file upload is therefore **not** evidence that binary publication is unavailable. Record the exact failed Git-data step if blob/tree/commit/ref publication itself fails.
