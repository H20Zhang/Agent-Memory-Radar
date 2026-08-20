# Memory Learning & Evolution

[← Research Map](../README.md) · [English](../memory-learning-evolution.md) · [首页](../../README.md)

> **核心问题：** 到底哪一种 persistent/adaptive state 应该 evolve？系统依据什么 feedback 知道自己该改什么？

## 当前判断

“Self-evolving memory”太容易把多个变量混在一起。至少要拆成：

`what state evolves × feedback surface × update rule × access policy × governance × transfer`

SkillEvo 主要改变 feedback surface；ERSkill 把 read policy/router 本身变成可演化 state；HyperSkill 则让 relational structure 同时进入 retrieval 和 maintenance。

## Strongest signal

SkillEvo 的 matched feedback comparison 表明，multi-turn interaction 在 single-turn QA 已趋于饱和后仍能持续暴露可修复 defect。HyperSkill 又说明 representation 只有在 relation 真正参与 read/update operator 时才值得额外复杂度。

因此“多存经验 + 反复 reflection”并不是一个足够精确的 research variable。

## 最大未解问题

Evolved artifact / policy / structure 是否能跨 consumer model、toolset、domain 与 workload transfer？如果只能在原 simulator/benchmark 上越调越好，那么 rollout 与 maintenance cost 很可能只是过拟合成本。

## 下一项 decisive evidence

在同一 base memory 与 budget 上独立变化：

`feedback richness → representation → update rule → read-policy evolution → governance`

然后做 cross-domain / cross-model transfer，并把 rollout、edit、maintenance、regression/bloat 一起计费。

## 继续读

[SkillEvo 中文笔记](../../papers/2026/2608.13120.zh.md) · [HyperSkill 中文笔记](../../papers/2026/2608.16114.zh.md) · [ERSkill](../../papers/2026/2608.12720.md)
