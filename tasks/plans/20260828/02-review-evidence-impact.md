# Issue #33 PR #18 实验证据定向处理计划

**状态：** In Progress

## Goal

基于 Issue #33 中 Consumer PR #18 新增的真实证据，定向处理 Human Review Finding 分类、外部媒体资源真实性验证，以及后继提交对既有验证证据的影响判断。

## Authority / Inputs

- 根目录 `AGENTS.md`
- `docs/project/project-roadmap.md`
- Issue #33 最新 Consumer Evidence
- Consumer PR #18、Runtime Head `25006e1281f16c30458566286cb8bca8de306540`、最终 Head `23d2b4f5094de1dbf98673c743b9ae8bd620fb6a`
- `agentic-dev@df4d6a607597eeb3684279e269cb073fcb398f83` 的现有 Operating Guide 与 Skills

## Scope

1. 明确 Human Review Finding 可能属于视觉、实现、产品语义、长期权威或 Runtime 问题，并按现有职责路由；
2. 对外部二进制 / 媒体资源核对真实内容类型，不信任名称或扩展名；
3. 允许在严格差异影响检查后按声明复用祖先提交证据，同时保持当前 Head、Authority 与验收语义边界；
4. 增加一个针对后继提交证据影响判断的 Behavior Eval；
5. 更新 Issue #33 与 Project Roadmap 状态。

## Non-goals

- 不修改 Method、Architecture 或 Skill Contract；
- 不新增 Skill、Method 阶段、固定 Consumer 模型或路径规则；
- 不把内容能力 / 首页投放策略固化为跨项目领域事实；
- 不规定 docs-only 一律跳过 Runtime、Human Review 或 CI；
- 不把祖先 Run 改称为当前 Head 的 Run，也不授予 Merge / Release / Deploy 权限。

## Work Items / Order

1. 完成 Consumer Evidence 与当前 Authority 对照；
2. 修订 Operating Guide、`github-actions-verification` 及 Evidence Reference；
3. 新增定向 Behavior Eval，并登记运行范围；
4. 更新 Project Roadmap 与 Issue #33；
5. 完成静态检查、Draft PR 和变更复核；
6. 在隔离 Fresh Runtime 中运行定向与必要回归场景，逐断言人工语义评分；
7. 完成最终 AI Review 并判断 Ready to Integrate。

## Completion Criteria

- 规则按 Evidence Claim 与精确差异影响判断，不按文件扩展名机械复用或失效；
- Human Review、Runtime Verification 与 Authority / Requirement / Architecture Review 的证据边界清晰；
- 文档、Skill、Reference 与 Eval 语义一致；
- Fresh Runtime 定向与回归评估有效且完成逐断言人工语义评分；
- 最终 AI Review 不存在未解决的 Blocking 或 Medium Finding；
- PR 达到 Ready to Integrate，合并仍由 Human Authority 决定。
