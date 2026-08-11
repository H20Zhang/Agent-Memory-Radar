# Visual Assets

Generated research visuals are organized by scope:

```text
assets/
├── papers/YYYY/<paper-id>-overview.png
└── digests/
    ├── weekly/<YYYY-Www>-research-map.png
    ├── monthly/<YYYY-MM>-design-space-map.png
    └── yearly/<YYYY>-research-map.png
```

The scheduled curator owns these assets. See [`../VISUAL_POLICY.md`](../VISUAL_POLICY.md) for generation, evidence, and multi-role QA requirements.

Binary images should be committed to `main` together with the Markdown page that embeds them. Do not leave orphaned images or Markdown references to missing assets.
