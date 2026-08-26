# 已有 Consumer 治理证据定向处理计划

**状态：** In Progress
**日期：** 2026-08-26
**Tracking Issue：** Issue #33

## 目标

基于 `dygapp/jilinjobs-cms` 已有 Consumer 继续演进实验提交的项目治理证据，定向补齐已有 Consumer 的 `agentic-dev` 采用与 baseline 升级边界，以及跨 Repository 授权和异步外部执行闭环。

## 权威与输入

- `AGENTS.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/external-operation-guidelines.md`
- `skills/github-actions-verification/SKILL.md`
- `docs/project/project-roadmap.md`
- Issue #33 及其引用的 Consumer commits
- `agentic-dev` `master@b4e5b2027bdbbe97cc0b7153be65c5afb7a0274e`

## 工作项与顺序

1. PR A：明确已有 Consumer 选择性采用 `agentic-dev`、固化 Consumer-local Authority、恢复本地优先工作和显式升级的生命周期，并收敛当前 Project Roadmap。
2. PR A 合并后，从新的 `master` 创建 PR B。
3. PR B：强化多 Repository 的逐仓库操作授权，以及异步外部执行持续到验证结论或真实阻塞的闭环。
4. 为 `github-actions-verification` 增加最小定向 Behavior Eval，并完成结构验证、Fresh Runtime 执行与人工语义分级。
5. 完成两个 PR 的 AI Review，并把处理状态、集成提交和评估证据回写 Issue #33。

## 非目标

- 不修改通用 Method 或 Skill Contract。
- 不新增 Skill、方法阶段、Issue Template 或固定 Consumer 文档模板。
- 不把 `jilinjobs-cms` 的具体 Repository 权限矩阵推广为所有 Consumer 的固定策略。
- 不把异步持续执行解释为无限轮询或突破 Runtime、Repository Policy 与 Human Authority。
- 不把 Issue #33 的两条正向验证机械转换为新增机制。
- 不自动合并 Pull Request，也不在实验 Final Summary 形成前关闭 Issue #33。

## 完成条件

- 普通 Consumer 工作不再被解释为持续依赖跨 Repository 的 Method 读取；显式升级仍使用精确 baseline 并选择性采用。
- 多 Repository 操作分别确认授权范围，工具能力不会被等同为操作授权。
- 可观察的异步外部运行不会在仅完成触发时被报告为任务终点。
- 定向 Behavior Eval 通过 Fresh Runtime 执行，并由人工逐项完成语义分级；进程退出状态不代替 Eval PASS。
- 中文规范、术语表达、权威边界、范围控制与 Roadmap 状态通过最终 AI Review。
- PR 与 Issue 保留足够的当前证据，后续 Fresh Context 不依赖聊天恢复处理状态。

## 当前状态

- PR A：PR #34 已合并，集成提交为 `b1ed6f1b78eb664e6dcae619b23e2ac1b7c5b522`；
- PR B 分支：`fix/issue-33-external-operation-closure`；
- External Operation Guide、`github-actions-verification` 与 `B-GA-01`：已形成候选修订；
- Eval JSON 结构、Runner 语法、场景注册与 Markdown 结构：`PASS`；
- Fresh Runtime：`B-GA-01`、`B-EU-04`、`B-EU-06`、`B-CG-06` 均为 `PASS`，合计断言 `20 / 20 PASS`；
- 隔离、污染与运行时有效性检查：`PASS`；
- PR B 最终 AI Review：等待最终变更集复核；
- PR B 集成：尚未完成。
