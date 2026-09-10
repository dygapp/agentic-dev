# 规则治理与知识激活 v2 协调计划

## 目标

协调 Issue #92 所跟踪的“规则治理与知识激活 v2”有限里程碑。

长期目标、设计约束、阶段边界与完成定义统一以：

`docs/project/rule-governance-knowledge-activation-v2.md`

为准。本计划只保留协调结果与集成边界，不复制第二份长期 Authority。

启动基线：`master@b6a20053a7a6f4f53915bea8218604720412c302`  
跟踪入口：Issue #92 / PR #93

## 已完成

- Phase A — Consumer-local Runtime Target / Acceptance
- Phase B — Rule Ownership / Guide Decomposition
- Phase C — Minimal Metadata / Catalog Contract
- Phase D — Discovery → Routing → Skill Interface
- Phase E — Baseline Adoption / Consumer-local Projection
- Root Bootstrap / `AGENTS.md` 职责收敛
- Phase F — 真实 Consumer 验证：R1～R5 PASS
- Phase G — Candidate Drift T1～T4 定向重验：PASS
- Final AI Review 中发现的 reusable Guide 两项中等级问题已修复并完成 Consumer 定向重验
- README / Roadmap / v2 项目记录已收敛为与瞬时 PR 状态解耦的稳定后态

## 最终验证锚点

Phase F：

`docs/project/consumer-local-runtime-validation-result-v2.md`

Phase G Candidate Drift：

`docs/project/consumer-local-runtime-candidate-drift-review-v2.md`

冻结 reusable candidate：

`29f88efd25232e57ccb4a82ffff039be047e4d1e`

Consumer 最终定向重验：

- Repository：`dygapp/jilinjobs-cms`
- Head：`c29da21b41ff3ddad023ecb64e3628dc3136a77e`
- Workflow Run：`34450265966`
- Artifact ID：`10141246815`
- Artifact digest：`sha256:7d1a9dc47a6192e4b6c010585d2c69ff387392083448b504c89848465a74fb06`
- T1～T4：全部 PASS
- ordinary runtime upstream access：0
- Blocking / Medium reusable findings：`0 / 0`

## 当前 Gate

v2 内部完成定义已经满足，当前只剩：

> **人工集成决策。**

PR #93 是否已经实际集成、Issue #92 是否已经关闭，直接从 GitHub 当前事实读取；本计划不复制瞬时 PR 状态。

无论当前集成结果如何，都不会自动启动新的有限里程碑。WI-06、WI-07、WI-09、第四 Engineering Discipline、Issue #71 等仍只是候选，必须由新的人工路线决策选择。

## Fresh Context 最小输入

如果 PR #93 尚未集成、当前任务是审查 v2 候选，按需读取：

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`
- `docs/project/consumer-local-runtime-validation-result-v2.md`
- `docs/project/consumer-local-runtime-candidate-drift-review-v2.md`
- PR #93 / Issue #92

只有具体语义审查需要时再读 Phase A～E Contract、Guide、Skill / Architecture；不恢复完整实验历史。

如果 PR #93 已集成，则 v2 作为已完成能力基线使用，本计划不再作为普通 Fresh Context 默认输入。

## 范围控制

本里程碑不：

- 修改或合并 Consumer 实验 Branch；
- 将 Consumer 验证视为正式 Consumer adoption；
- 产品化 Runtime Rule Index；
- 引入向量 / 图数据库、MCP、Rule Super Skill、Stage Router Skill；
- 增加新的 Runtime Eval 场景；
- 启动 WI-06 / WI-07 / WI-09 / Issue #71 候选实施。

后续如果出现新的 reusable 问题，以新的 Evidence / Planning 边界处理，不为了维持本计划“当前”而无限追加状态。

## 完成

当前协调结论：

> **规则治理与知识激活 v2 已具备进入人工集成决策的条件。**

该结论不等于人工批准，也不授予 Merge。实际集成由人工权威或仓库策略决定；精确集成事实由 Git / PR #93 / Issue #92 保存，不要求合并后再创建纯状态同步提交。
