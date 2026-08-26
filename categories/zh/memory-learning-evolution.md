# Memory Learning & Evolution

[English](../memory-learning-evolution.md) · [← Research Map](../README.md) · [Research Library](../../library/README.md)

> **Core question：** Memory 系统到底应该让什么 evolve——persistent content、relation、writer/read policy，还是 artifact promotion/governance？

## 当前判断

**CONTRAMEM** 用异构 outcome contrast 与局部 curation 构建 frozen procedural bank；**BASM** 在 skill retrieval 后增加 validity boundary。前者不能称为 online self-evolution，后者也没有隔离 failed-trajectory admission、checker 与 repair；两者都只细化研究问题。

“Self-evolving memory” 这个标签太粗。最近的工作已经把 adaptive state 拆成至少三类：

- **HyperSkill：** relation structure 真正进入 retrieval/ranking/maintenance。
- **WER：** 从 execution feedback 学 **skill-writer policy**，而不是只改当前 artifact。
- **TRUSS：** 不直接学 writer，而是用 static + runtime evidence 决定 candidate skill 是否可以被 promote 为 persistent capability。
- **SPADE：** 用跨 episode 的 environment buffer 条件化后续训练课程，但 no-memory 消融仍混入 demonstration token 与 checkpoint selection 差异。
- **Harness Continual Learning：** 把 memory、interface、capability map 与 router 作为联合 version 的 harness state，并在 commit 前检查 retention。

SkillEvo / ERSkill 则分别提醒：feedback surface 与 read policy evolution 也是独立变量。

**Break It Down, Pass It On** 又把 write granularity 拆出来：whole-task skill 在平均上会伤害后续任务，subtask skill 只有小幅平均增益，而且不少 model/domain slice 反转。Granularity 必须在相同 consumer、source trajectory、read/write count 与完整 lifecycle cost 下比较。

## Strongest signal

WER 的 matched untrained-optimizer control 说明，学习 writer policy 本身能产生明显增益；SPADE 的 no-memory run 则提示训练经验生成器也可能拥有跨 episode 状态，但单次 suite-selected comparison 只能支持 package-level signal。TRUSS 的 detection ladder 说明，只做 LLM/static inspection 仍会漏掉 runtime behavior；HCL 又把 whole-harness commit 加入边界。它们共同表明：**training-experience memory、artifact generation、writer learning、execution feedback、promotion gate 与 harness update 不应被打包成一个“self-improvement”模块。**

## Biggest unresolved question

这些 evolved artifacts / policies / curricula 是否能跨 executor、domain、code version 与更长 state stream 稳定迁移？如果 synthesis、environment generation、verifier、rollout、historical replay 很贵，break-even point 在哪里？

## Next decisive evidence

固定 executor、task distribution 与 skill format，独立变化：

`writer training × feedback richness × token-matched curriculum memory × read policy × commit certification × retention budget`

同时报告 task utility、regression、library bloat、rollout/verifier cost 与 cross-domain transfer。
