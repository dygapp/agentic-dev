# Foundation v1 F4 — Existing Consumer Adoption Handoff

**状态：Completed / Superseded by Foundation v1 Closure Plan。**

## 1. 目的

本文为 Engineering Capability Foundation v1 的 **F4 — 一次 Existing Consumer Adoption** 提供跨 Repository 交接与证据回传边界。

F4 的目标不是由 `agentic-dev` 会话直接开发 Consumer，而是验证已经集成的 Engineering Discipline、Vue 3 + TypeScript Technology Profile 与 Consumer-local Authority 在一个真实工作单元中的组合是否可用。

Foundation v1 只执行一次受控 Adoption，不把该阶段扩展成新的长期 Experiment。

F4 已由 Issue #52 完成 Evidence Review 并判定 PASS；本文件保留为历史 Handoff 与 Evidence Contract，不再承担当前执行职责。

## 2. 当前 agentic-dev 基线

F4 使用的 `agentic-dev` 集成基线：

`master@b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`

该基线已经完成：

- F1：首批两个 Engineering Discipline 正式集成；
- F2：Technology Profile / Verification Profile 最小契约集成；
- F3：Vue 3 + TypeScript Profile 正式集成；
- Vue 3 + TypeScript Capability Eval：`9 / 9 PASS`、`41 / 41 assertions PASS`。

## 3. Consumer 候选与 Repository Boundary

Foundation v1 的优先 Reference / Integration Consumer：

`dygapp/jilinjobs-cms`

但 F4 必须保持 Repository / Conversation Boundary：

- 当前 `agentic-dev` 项目会话只允许修改 `dygapp/agentic-dev`；
- 不在当前项目会话中修改 Consumer 文件、Branch、Commit、PR 或 Workflow；
- Consumer baseline upgrade、真实 Feature / Execution Unit 实施、验证与 PR 收敛必须在 `jilinjobs-cms` 自己的项目会话中执行；
- Consumer 正在进行中的独立任务不得因为 F4 被打断、改写或抢占；
- `agentic-dev` 只定义 Adoption 目标、上游能力基线、证据需求和通用 Finding 的处理方式；
- Consumer Repository Authority 始终决定 Consumer 的 Product Scope、Architecture、实际依赖版本、命令和验证环境。

该边界是 F4 的执行约束，不把跨 Repository 工具能力解释为跨项目写授权。

## 4. 启动条件

Consumer 会话只有在以下条件成立后才启动 F4 实施：

1. Consumer 当前正在进行的上游 Authority / Planning / Implementation 工作已经按其自身流程到达可继续下一真实工作单元的状态；
2. Consumer 会话重新读取当时实际的默认分支、`AGENTS.md`、`README.md`、Project Roadmap、Consumer-local Development Method 和当前工作 Authority；
3. 记录 Consumer 当前采用的 `agentic-dev` baseline；
4. 记录准备升级到的 `agentic-dev@b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`；
5. 选择一个真实、边界明确、会实际触达 Vue 3 + TypeScript 的工作单元。

如果 Consumer 当前任务仍在进行中，F4 保持 **Pending Consumer Execution**，`agentic-dev` 不以等待为理由启动第二个 Consumer 或增加新的 Profile / Discipline。

上述启动条件已经由 `dygapp/jilinjobs-cms` F4 Adoption 满足，保留为历史复核依据。

## 5. Consumer baseline upgrade 要求

Consumer 会话需要比较其实际旧 baseline 到 `b80b2b1b7cea38eed0aef9807879e2a0d56afd2f` 的变化，并只固化对该 Consumer 持续有价值的通用规则。

F4 重点验证三类新增能力：

### 5.1 Engineering Discipline

- Implementation Minimality & Speculative Complexity Control；
- Surgical Change & Diff Scope Control。

Consumer-local 化时应验证：

- 是否帮助 Agent 拒绝没有当前证据支持的额外抽象、配置、依赖、扩展点和“顺便优化”；
- 是否允许当前工作真正需要的局部准备性重构、验证代码、Authority 同步和必要 cleanup；
- 是否没有退化成“代码越少越好”或“只能改最少文件”。

### 5.2 Technology Profile / Verification Profile

F4 采用：

`docs/technology-profiles/vue3-typescript.md`

但 Profile 是默认工程基线，不覆盖 Consumer-local 事实。

Consumer 会话必须从实际仓库解析：

- Vue / TypeScript / Vue Language Tools / `vue-tsc` 的真实版本；
- 当前 package scripts、tsconfig / extends 链；
- 实际 build、type-check、test、browser / visual 命令；
- 当前 Architecture / ADR / project rules；
- 组件库等不在 Profile 范围内的技术 Authority。

不得为了匹配 Profile 的研究锚点版本机械升级 Consumer 依赖。

### 5.3 Consumer Override

需要明确记录：

- 哪些 Profile 规则直接适用；
- 哪些 Engineering Default 被 Consumer-local Authority 合理覆盖；
- 哪些规则因为 Consumer 技术版本不适用；
- 是否存在 Profile 错误默认值、过度约束或缺失边界。

普通项目偏好不能改写客观技术语义；反过来，Profile 也不能覆盖已确认的 Consumer Architecture / Product Scope。

## 6. Adoption Unit 选择规则

Foundation v1 只选择 **一个**真实工作单元。

该 Unit 应同时满足：

- 属于 Consumer 当前 Roadmap，而不是为了实验人工发明；
- 会实际修改 Vue 3 + TypeScript 代码；
- 范围足以观察 Engineering Minimality / Diff Scope；
- 有真实 Acceptance / Verification Obligations；
- 可以在单个 PR 或清晰 Evidence Boundary 内判断结果；
- 不要求为了实验新增第二个 Technology Profile、Task-oriented Skill 或 Runtime Adapter。

如果 Consumer 当前已有合适的下一 Vue / TypeScript 实施 Unit，应直接采用；如果没有，不为完成 F4 人工制造虚假 Feature，等待下一个真实适用 Unit。

实际采用的唯一 Unit：**Party Column Route Currentness Execution Unit**，Consumer PR #49。

## 7. Adoption Evidence

Consumer 会话完成该 Unit 后，应向 `agentic-dev` 回传最小但充分的 Evidence：

### 7.1 Baseline

- Consumer Repository；
- Consumer 起始 commit；
- Consumer 原 `agentic-dev` baseline；
- Consumer 升级后 baseline：`b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`。

### 7.2 Unit

- Unit / PR 标识；
- 当前 Authority / Specification / Plan 入口；
- 实际变化范围；
- 为什么该 Unit 适合作为 F4 Adoption 样本。

### 7.3 Capability Consumption

至少说明：

- Minimality Discipline 实际影响了哪些实施判断；
- Diff Scope Discipline 实际影响了哪些范围判断；
- Vue 3 + TypeScript Profile 中哪些规则实际适用；
- 哪些规则被 Consumer-local Authority 覆盖或因版本不适用；
- Verification Profile 如何映射到实际验证命令与证据。

这里记录关键判断，不要求保存完整 Agent reasoning 或调用流水。

### 7.4 Current Evidence

至少记录与本次声明匹配的：

- Consumer 目标 Head / commit；
- type-check / build；
- 当前 Unit 要求的 test / browser / visual / integration evidence；
- PR / CI / Review 结果；
- 后继提交 Evidence Claim 影响判断（如适用）。

### 7.5 Findings

只按以下类别回传：

- **Blocking General Finding**：当前通用能力导致 Adoption 无法正确完成；
- **Medium General Finding**：存在真实通用缺口，需要在 Foundation v1 Closure 前修复；
- **Consumer-local Finding**：只属于 Consumer 产品 / 架构 / 版本 / 环境，不要求 `agentic-dev` 修改；
- **Low / Future Improvement**：可以进入 Post-v1 Backlog，不阻塞 F4。

不得因为 Consumer 出现一个局部问题就自动提升为新的 Engineering Discipline、Technology Profile 或 Skill。

## 8. F4 完成判定

F4 可以关闭，当且仅当：

1. 一个真实 Consumer Unit 已完成 baseline upgrade 和能力采用；
2. 有 Current Evidence 证明该 Unit 的实际验证闭环；
3. 新 Engineering Discipline 没有造成不可接受的过度约束或范围退化；
4. Vue 3 + TypeScript Profile 能在 Consumer 真实版本 / Authority 下正确应用或被合理覆盖；
5. Verification Profile 能映射到 Consumer 的实际验证责任；
6. Blocking / Medium General Finding 已处理并重新验证，或明确证明不存在；
7. Consumer-local Finding 没有被错误回写为 `agentic-dev` 通用规则；
8. F4 没有扩展到第二个 Consumer 或第二个 Adoption Unit。

Issue #52 Evidence Review 已确认上述条件全部满足：

- Blocking General Finding：`0`；
- Medium General Finding：`0`；
- Consumer-local Finding 保持 Consumer-local；
- Consumer PR #52 只作为 post-adoption evidence，不计为第二个 Adoption Unit。

因此 F4 已关闭并进入 F5 Closure。

## 9. 最终状态

`F4 — PASS / Completed`

正式 Evidence Review：Issue #52（completed）。

本文件不再是当前执行入口。Foundation v1 后续执行职责由：

`tasks/plans/20260903/01-foundation-v1-closure.md`

接替。

## 10. 生命周期

- **Producer：** `agentic-dev` Foundation v1 项目治理职责；
- **Trigger：** PR #50 实际合并，F3 完成并进入一次受控 Consumer Adoption；
- **Consumer：** Consumer 项目会话、`agentic-dev` F4 Evidence Review、F5 Closure Review；
- **Persistence：** 作为 F4 历史执行 / handoff Plan 保存；
- **Update：** F4 已关闭，后续只在其 Evidence 被证明无效时修正，不继续承载新 Adoption；
- **Supersede：** 已由 `tasks/plans/20260903/01-foundation-v1-closure.md` 接替当前执行职责；
- **Escalation：** 后续新的 Consumer Adoption 需要新的 Milestone / Roadmap Decision，不能继续扩展 Foundation v1。