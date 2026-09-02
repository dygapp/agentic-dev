# WI-04 — Technology Profile 最小契约

## 状态

**当前。**

基线：`master@6130d7251d81bbfc9f13b2dd827b6a40dfd09076`（PR #48 已合并）。

本 Plan 只执行 Engineering Capability Foundation v1 的 **F2 / WI-04**。它不启动 Vue 3 + TypeScript 具体 Research，不扩大到第二个 Technology Profile、Task-oriented Skill 或 Runtime / Distribution。

## 目标

形成一个足以承载真实 Technology Profile / Verification Profile 的最小规范契约，并完成当前仓库权威接入。

完成后，Fresh Context 应能直接进入 WI-05，而无需重新讨论：

- Technology Profile 是什么；
- 最少必须包含哪些内容；
- Verification Profile 如何表达；
- Consumer 如何选择、限制、补充或覆盖；
- Research 如何进入 Profile；
- Profile 如何更新与取代；
- Profile 为什么不自动等于 Skill。

## 权威输入

执行本 Plan 时读取：

1. `AGENTS.md`；
2. `docs/project/project-roadmap.md`；
3. `docs/project/engineering-capability-foundation-v1.md`；
4. `docs/architecture/engineering-capability-architecture.md`；
5. `docs/architecture/engineering-disciplines.md`；
6. 本 Plan。

如需检查 Skill 边界，再加载 `skill-architecture.md` / `skill-contracts.md`；不默认加载 Vue、TypeScript、Element Plus、Spring 或其他技术 Research。

## 范围

### 必须完成

- 定义 Technology Profile 最小职责；
- 定义 Profile Identity / Version / Applicability；
- 定义 Evidence Baseline / Freshness / Conflict 要求；
- 区分官方技术语义、Engineering Default、Conditional Guidance、Known Misuse；
- 定义 Existing Capability Reuse 与项目自有实现边界；
- 定义 Consumer Override Boundary；
- 定义 Technology Profile 组合 / 拆分规则；
- 定义 Verification Profile 最小契约；
- 定义 Research → Profile 准入门槛；
- 定义 Profile 与 Engineering Discipline / Skill 的关系；
- 定义 Profile Targeted Eval 要求；
- 定义 Producer / Trigger / Consumer / Persistence / Update / Supersede / Escalation；
- 接入 Repository Authority；
- 完成项目级 AI Review。

### 明确不做

- 不研究 Vue 3 / TypeScript 的具体官方实践；
- 不建立 Vue 3 + TypeScript Profile 实例；
- 不引入 Element Plus、Spring、Gradle；
- 不新增 Task-oriented Skill；
- 不修改 Core Method；
- 不创建 Runtime Adapter；
- 不要求固定 YAML / JSON schema；
- 不固定 Consumer 的 Build / Test / Lint 命令。

## 设计约束

### Profile 不是框架百科

只保留会改变工程判断、误用识别、能力复用或验证责任的知识。API 罗列、教程步骤、单项目风格默认留在 Research / Consumer-local Authority。

### Profile 不是“一技术一文件”

允许多个技术在存在稳定联合工程边界时组成一个 Profile，但每个技术仍需有独立版本 / 适用范围和证据锚点。不得因技术经常一起使用就自动组成大 Stack Profile。

Foundation v1 预期允许 `Vue 3 + TypeScript` 作为一个组合 Profile；Element Plus 不自动进入。

### Verification Profile 不固定命令

标准化的是：

```text
验收义务
→ 技术变更类型
→ 验证层
→ Evidence Responsibility
→ Consumer 当前机制
→ Current Evidence
```

精确命令仍由 Consumer Repository Authority 和实际仓库状态解析。

## 完成条件

WI-04 只有在以下条件全部满足时才可以关闭：

- `docs/architecture/technology-profile-contract.md` 形成单一规范入口；
- `AGENTS.md` 能发现其 Authority 位置；
- 契约足以承载一个 Vue 3 + TypeScript 真实 Profile；
- 契约没有变成框架百科模板；
- Profile / Verification / Consumer Override / Lifecycle / Eval 边界闭合；
- 没有机械新增 Skill；
- 没有开始 WI-05 具体技术研究；
- 最终 AI Review 不存在 Blocking / Medium Finding；
- 达到 `Ready to Integrate`，等待 Human / Repository Integration Decision。

## 下一步

只有本契约实际集成后，才进入：

> **F3 / WI-05 — Vue 3 + TypeScript Technology Profile**

WI-05 应基于本契约重新读取当前官方资料并记录精确版本 / 日期基线，不能复用聊天中的未固化框架知识作为项目事实。
