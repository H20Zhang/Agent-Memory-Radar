# Memory Learning & Evolution

[English](../memory-learning-evolution.md) · [← Research Map](../README.md) · [Research Library](../../library/README.md)

> **Core question：** Memory 系统到底应该让什么 evolve——persistent content、relation、writer/read policy，还是 artifact promotion/governance？

## 当前判断

“Self-evolving memory” 这个标签太粗。最近的工作已经把 adaptive state 拆成至少三类：

- **HyperSkill：** relation structure 真正进入 retrieval/ranking/maintenance。
- **WER：** 从 execution feedback 学 **skill-writer policy**，而不是只改当前 artifact。
- **TRUSS：** 不直接学 writer，而是用 static + runtime evidence 决定 candidate skill 是否可以被 promote 为 persistent capability。
- **Harness Continual Learning：** 把 memory、interface、capability map 与 router 作为联合 version 的 harness state，并在 commit 前检查 retention。

SkillEvo / ERSkill 则分别提醒：feedback surface 与 read policy evolution 也是独立变量。

## Strongest signal

WER 的 matched untrained-optimizer control 说明，学习 writer policy 本身能产生明显增益；TRUSS 的 detection ladder 说明，只做 LLM/static inspection 仍会漏掉 runtime behavior。HCL 又把 whole-harness commit 加入边界。它们共同表明：**artifact generation、writer learning、execution feedback、promotion gate 与 harness update 不应被打包成一个“skill memory”模块。**

## Biggest unresolved question

这些 evolved artifacts / policies 是否能跨 executor、domain、code version 与更长 state stream 稳定迁移？如果 synthesis、verifier、rollout、historical replay 很贵，break-even point 在哪里？

## Next decisive evidence

固定 executor、task distribution 与 skill format，独立变化：

`writer training × feedback richness × read policy × commit certification × retention budget`

同时报告 task utility、regression、library bloat、rollout/verifier cost 与 cross-domain transfer。
