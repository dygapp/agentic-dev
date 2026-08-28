# Issue #33 验证证据边界定向处理计划

**状态：** Completed

## Goal

基于 Issue #33 在 PR #15 与 PR #16 中新增的真实 Consumer Evidence，定向收敛验证契约、数据库运行验证、人工评审环境和视觉证据边界。

## Authority / Inputs

- 根目录 `AGENTS.md`
- `docs/project/project-roadmap.md`
- Issue #33 在 2026-08-27 与 2026-08-28 新增的 Consumer Evidence
- 现有 Operating Guide、`systematic-debug` 与 `github-actions-verification`

## Scope

1. 明确陈旧验证契约的识别与正确修复层；
2. 避免 Workflow 无必要重复维护产品语义断言；
3. 强化数据库 Migration 的干净数据库、完整迁移链与应用启动证据；
4. 区分 Automated Verification State 与 Human Review Baseline；
5. 明确 Functional Browser Evidence 与 Visual Fidelity Evidence 的声明边界；
6. 强化可写 bind mount 的 ownership、cleanup 与可重复恢复验证；
7. 增加与上述真实失败模式对应的定向 Behavior Eval；
8. 更新 Issue #33 与 Project Roadmap 的处理状态。

## Non-goals

- 不修改 Method、Architecture 或 Skill Contract；
- 不新增 Skill、Method 阶段、固定 Consumer 模板或特定容器拓扑；
- 不把单个 Consumer 的 Workflow、数据结构或视觉结论推广为跨项目事实；
- 不扩大 Human Visual Review 的原始结论。

## Work Items / Order

1. 完成证据与现行 Authority 对照；
2. 修订 Operating Guide 与两个既有 Skill 的最小行为边界；
3. 补充容器化验证参考；
4. 新增 3 个定向 Behavior Eval；
5. 完成静态检查并创建 PR；
6. 在隔离 Fresh Runtime 中运行定向与回归场景并进行人工语义评分；
7. 完成最终 AI Review、Issue 回写和路线图收敛。

## Current Evidence

- Fresh Runtime 运行内容对应 PR #37 语义基线：`01b5838d618819dbcfc034e1d3229dd0274eb4e1`；
- Fresh Runtime Eval：`6 / 6 PASS`；
- 人工语义评分：`35 / 35 PASS`；
- 隔离与污染检查：PASS；
- 最终 AI Review：PASS，Blocking / Medium Finding 为 `0 / 0`；
- PR #37：Ready to Integrate，合并仍由 Human Authority 决定。

## Completion Criteria

- 新增规则与 Issue #33 Evidence 一致且未越过证据边界；
- 文档、Skill、参考与 Eval 语义一致；
- 定向与必要回归场景通过有效 Fresh Runtime 和逐断言人工语义评分；
- 最终 AI Review 不存在未解决的 Blocking 或 Medium Finding；
- PR 达到 Ready to Integrate，合并仍由 Human Authority 决定。
