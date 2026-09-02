# Technology Profile 最小契约

**状态：** Baseline v0.1  
**性质：** Technology Profile / Verification Profile 规范性契约

## 1. 目的

本文定义 `agentic-dev` 中 Technology Profile（技术配置档）与其 Verification Profile（验证配置档）的最小长期契约。

目标不是建立统一的框架百科模板，而是回答：

> **一项特定技术工程知识在什么条件下可以成为可复用 Profile，以及后续 Agent 如何可靠判断它适用于什么、默认应怎么做、哪些做法应避免、如何验证，并在 Consumer Repository 中如何被选择、限制、补充或覆盖。**

本文受 `AGENTS.md`、Core Method、Engineering Capability Architecture 和当前 Engineering Discipline Authority 约束，不创建新的 Method Stage，也不要求 Technology Profile 自动形成 Task-oriented Skill。

## 2. Profile 的职责边界

Technology Profile 描述特定技术体系下会稳定影响工程判断的：

- 当前有效技术语义与官方支持边界；
- 默认工程规则和成熟实践；
- 常见误用与高风险错误模式；
- 框架 / 标准库 / 现有生态能力的优先复用边界；
- 何时允许或需要项目自有实现；
- 与当前技术变更类型匹配的 Verification Profile；
- Consumer-local Authority 的选择、限制、补充和覆盖边界。

Technology Profile 不负责：

- 复制官方文档的完整 API / 教程内容；
- 保存某个 Consumer 的项目目录、业务事实、精确依赖版本或本地命令；
- 规定所有项目必须采用相同架构、代码风格或测试框架；
- 替代 Specification、Technical Plan、Architecture / ADR 或 Execution Unit；
- 自动执行完整开发任务；
- 因技术名称存在就建立对应 Skill。

只有会改变工程决策、实现边界、误用判断或验证责任的技术知识，才应进入长期 Profile。

## 3. Profile 最小结构

一个拟进入 Repository Authority 的 Technology Profile 至少必须能够回答以下八类问题。载体可以是一个文件或一组具有单一当前入口的文件，不要求固定 YAML / JSON schema。

### 3.1 Identity & Applicability

至少明确：

- Profile 的名称 / 稳定标识；
- 覆盖的技术或技术组合；
- 研究与验证所针对的主要版本 / 版本范围；
- 适用运行条件、工程假设或已知不适用范围；
- 当前 Profile baseline / revision。

版本范围不能只写“最新版本”。快速演进技术应保留可追溯的研究版本或发布日期锚点。

### 3.2 Evidence Baseline

Profile 的规范性结论必须可以回溯到满足 Engineering Capability Architecture 证据门槛的来源。

至少保留：

- Provenance：官方文档、规范、仓库、成熟开源项目、专家原始材料或 Consumer / Eval Evidence；
- Baseline：版本、Commit、发布日期或其他可识别锚点；
- Evidence Type：官方语义 / 官方推荐 / 成熟工程实践 / 专家经验 / Eval / Consumer Observation；
- Applicability：证据实际支持的技术版本和场景；
- Freshness：研究时的有效性检查；
- Conflict：重大来源冲突及当前裁决或 Pending 状态。

Profile 不要求在正文每句话后重复完整引用，但任何会影响工程行为的规则必须有可追溯证据链。

### 3.3 Official Semantics & Support Boundaries

记录会影响正确实现的官方语义和支持边界，例如：

- 生命周期；
- API / 类型系统语义；
- 官方支持 / 不支持的组合；
- 已弃用或替代路径；
- 与兼容性、运行时或构建相关的关键限制。

这一部分只保留工程判断真正需要的语义，不复制官方参考手册。

如果成熟开源实践或专家建议与当前官方语义冲突，不能静默用“最佳实践”覆盖官方事实。

### 3.4 Engineering Defaults

记录在适用条件成立、且 Consumer 没有更具体权威时，Agent 应优先采用的默认工程做法。

每项默认规则至少应能够判断：

- **为什么现在适用**；
- **解决什么当前工程责任**；
- **何时不再适用或需要重新评估**。

默认规则不得只是“通常大家这么写”。应优先选择能够减少错误、降低不必要复杂度、正确利用技术能力并提升可验证性的稳定实践。

### 3.5 Common Misuse & Avoid

记录具有辨识价值的常见误用，包括：

- 对官方语义的误解；
- 重复实现框架已经可靠提供的能力；
- 为假想未来过度抽象；
- 技术上可运行但违反生命周期 / 类型 / 状态管理 / 资源管理等稳定边界的做法；
- 容易导致验证盲区的实现方式。

该部分必须说明“为什么有问题”和适用条件，不建立无上下文的禁止清单。

### 3.6 Capability Reuse & Extension Boundary

Profile 必须说明：

- 当前技术体系已经提供哪些应优先检查和复用的能力类别；
- 何时薄适配比重新实现更合适；
- 何时现有能力因功能、安全、性能、可观察性、生命周期或其他当前契约不匹配，可以基于证据采用项目自有实现；
- 不为了复用扩大依赖面、改变产品行为或覆盖 Consumer Architecture Authority。

该部分具体化 Engineering Discipline 中的 Existing Capability Reuse / Implementation Minimality，但不能放宽其通用边界。

### 3.7 Consumer Override Boundary

Profile 是可复用默认基线，不是 Consumer 的最终项目事实。

Consumer Repository 可以：

- 显式选择适用 Profile / baseline；
- 固化自己的精确技术版本、项目架构、目录规则和依赖约束；
- 为项目特有原因限制、补充或覆盖 Engineering Default；
- 指定真实 Build / Test / Lint / Browser / CI / Human Review 命令与证据载体；
- 禁用与当前项目不匹配的可选指导。

但 Consumer-local 规则不能通过普通项目偏好改写客观的技术语义。如果项目有意使用官方不推荐、已弃用、实验性或兼容性受限路径，应由 Consumer Authority 明确记录这一事实、适用理由和风险，而不是让 Profile 静默变成错误。

当 Profile 与 Consumer 发生冲突时，至少区分：

1. 合理项目特化；
2. Consumer 使用的 Profile / 技术 baseline 已陈旧；
3. `agentic-dev` Profile 本身存在通用缺口。

### 3.8 Lifecycle

每个 Profile 必须明确或可从当前仓库权威中确定：

- Producer；
- Trigger；
- Consumer；
- Persistence；
- Update；
- Supersede；
- Escalation。

Profile 的当前入口只能有一个。旧版本可以保留用于历史追溯，但必须明确 Superseded / Replaced 关系，避免多个 Profile 同时被解释为当前规范。

## 4. 规则强度与表达

为了避免把所有工程建议写成绝对规则，Technology Profile 的规范性内容至少应在语义上区分以下类型；不强制使用固定字段名。

### 4.1 Technology Constraint

来自当前技术语义、支持边界或明确兼容性约束。违反它通常意味着实现错误、未支持组合或已知高风险行为。

Consumer 如果必须偏离，应显式记录版本、实验性能力或风险依据，不能把普通偏好当作覆盖事实。

### 4.2 Engineering Default

在通常适用条件下优先采用的成熟工程做法。

Consumer 可以因更具体项目事实覆盖，但应有可说明的当前原因，而不是机械复制或机械拒绝 Profile。

### 4.3 Conditional Guidance

只在特定变更类型、规模、风险或运行条件成立时适用。Profile 必须写明触发条件。

### 4.4 Known Misuse / Avoid

用于识别常见错误或高风险模式。必须同时说明违反了什么语义 / 工程责任，以及合法例外的判断边界（如存在）。

## 5. Technology Profile 的组合与拆分

Technology Profile 不要求“一项技术一个文件”，也不允许为了便利形成大而全 Stack Profile。

允许组合多个技术的条件是：

- 它们在真实工程任务中形成稳定且高频的联合决策边界；
- 大量关键规则、误用或验证责任只有结合后才有意义；
- 拆分会产生重复、冲突或使 Agent 无法可靠应用规则；
- 每个组成技术仍保留独立的版本 / 适用范围和证据锚点。

例如 Foundation v1 可以建立：

> **Vue 3 + TypeScript Technology Profile**

因为组件模型、响应式状态、模板类型检查、Composition API 与 TypeScript 类型边界会共同影响前端实现和验证。

但 Element Plus 不因为常与 Vue 一起使用就自动进入同一 Profile；只有研究证明它与 Profile 当前职责存在不可合理分离的稳定工程边界时才可调整，否则保持 Post-v1 独立候选。

当一个组合 Profile 逐渐包含多个可独立演进的框架、工具和大量无关规则时，应评估拆分，而不是继续扩充一个“前端大全”。

## 6. Verification Profile 最小契约

Verification Profile 是 Technology Profile 的必要组成部分或受其引用的独立能力，用于把技术变更映射到合理的验证责任。

它不固定项目命令，也不替代 Execution Unit 已经分配的验收义务。

### 6.1 Change Type

识别当前技术体系下会显著影响验证路径的变更类型，例如：

- 类型 / 编译期变化；
- 组件或模块行为变化；
- 生命周期 / 状态变化；
- 公共 API / Contract 变化；
- 构建 / 打包变化；
- 浏览器 / Runtime 行为；
- 样式 / 视觉变化；
- 性能、安全或兼容性敏感变化。

Profile 不要求穷举所有变更，只保留会改变验证责任的稳定分类。

### 6.2 Verification Layers

针对 Change Type，说明通常需要考虑哪些验证层级，例如：

- type check / compile；
- unit / component test；
- integration / contract test；
- build；
- runtime / browser behavior；
- visual evidence；
- performance / security / compatibility evidence。

这些是验证层级，不是固定命令清单。

### 6.3 Evidence Responsibility

每个 Verification Profile 应能够帮助 Agent 判断：

```text
当前验收义务
→ 技术变更类型
→ 应由哪个验证层证明什么
→ Consumer 当前可用机制
→ 已执行的 Current Evidence
```

Profile 不能只因为“type check + build 都通过”就宣称业务验收义务已闭环。

### 6.4 Risk Escalation

明确什么情况需要扩大验证，例如：

- 公共契约变化；
- 生命周期或并发变化；
- 多入口 / 多状态行为；
- 用户可见视觉变化；
- 安全 / 隐私 / 性能敏感路径；
- 框架升级或跨版本兼容性。

扩大验证必须与当前风险和责任相关，不为了完整性机械运行所有层级。

### 6.5 Consumer Resolution

具体命令、测试框架、fixture、浏览器工具、CI 工作流和 Human Review 证据必须从 Consumer Repository Authority、当前依赖和实际仓库状态解析。

如果 Profile 建议某验证层，但 Consumer 当前没有对应机制：

- 不编造命令或工具；
- 判断该层是否是当前 Completion 的必要证据；
- 必要时建立最小验证能力、返回上游规划职责或保持 Not Completed；
- 不通过降低验收义务来制造 PASS。

## 7. Research → Profile 准入门槛

Research 中的内容只有满足以下条件才进入 Profile：

- 对当前技术版本仍有效；
- 有足够权威或多来源成熟证据；
- 会实际改变工程选择、误用识别或验证责任；
- 适用范围可以说明；
- 与当前 Repository Authority 不冲突；
- 能够形成有辨识力的 Targeted Eval 或 Review Heuristic。

以下内容默认继续留在 Research，不进入 Profile：

- API / 配置项罗列；
- 教程式步骤；
- 单个项目的目录或代码风格；
- 单一低权威个人偏好；
- 缺少版本锚点的旧经验；
- 尚未解决的重大来源冲突；
- 只因为“可能以后有用”的知识。

## 8. Profile 与 Engineering Discipline / Skill 的关系

Technology Profile 必须服从当前 Engineering Discipline，并把通用原则具体化到技术上下文。

例如：

- Engineering Discipline 要求避免推测性抽象；Profile 可以说明该技术中常见的无必要扩展点或错误抽象方式；
- Engineering Discipline 要求精准修改；Profile 可以说明某技术变更会确定性地产生哪些必要伴随文件或验证责任。

Profile 不得复制一套新的通用工程纪律来与 `docs/architecture/engineering-disciplines.md` 竞争权威。

Profile 也不自动产生 Skill。只有后续出现具有独立 Use When / Inputs / Procedure / Outputs / Exit / Escalation 的稳定任务过程，才按 Skill Architecture 另行评估。

## 9. Targeted Eval 要求

Technology Profile 在正式集成前必须具有针对其实际规范性声称的 Targeted Eval。

至少应验证：

- 能否识别适用 / 不适用范围；
- 能否区分 Technology Constraint、Engineering Default 与 Conditional Guidance；
- 能否优先检查并复用技术体系已有能力，而不是重复实现；
- 能否识别典型误用而不过度禁止合法方案；
- 能否在 Consumer Authority 更具体时正确服从或升级；
- 能否根据技术变更类型选择合理验证层，而不是使用固定命令或主路径证据冒充完成；
- 能否保持 Implementation Minimality 与 Surgical Change 等当前 Engineering Discipline。

Targeted Eval 应围绕 Profile 的真实决策价值设计，不为了覆盖官方文档知识点建立百科问答测试。

## 10. Profile 实例的最小完成条件

一个 Technology Profile 只有同时满足以下条件，才可以进入最终 AI Review / Ready to Integrate：

- Identity / Version / Applicability 明确；
- Evidence Baseline 可追溯且检查过 Freshness；
- Official Semantics / Support Boundaries 已收敛到真正影响工程判断的内容；
- Engineering Defaults 有适用条件和理由；
- Common Misuse 有辨识价值并保留合法边界；
- Capability Reuse / Project-owned Implementation 边界明确；
- Consumer Override Boundary 明确；
- Verification Profile 能把主要技术 Change Type 映射到验证层与 Evidence Responsibility；
- Research 内容已经过准入筛选，没有变成框架百科；
- Targeted Eval 有有效当前 PASS 证据；
- AI Review 不存在未解决 Blocking / Medium Finding；
- 未因 Profile 的存在机械新增 Skill。

## 11. 生命周期

- **Producer：** 当前 `agentic-dev` Repository Authority 授权的 Technology Profile / Engineering Capability 维护职责；
- **Trigger：** Foundation Roadmap、成熟外部技术实践、Targeted Eval、Consumer Adoption 或技术版本变化产生稳定 Profile 需求；
- **Consumer：** Consumer Agent、`execute-unit`、后续 Task-oriented Skill、Verification capability 与 Runtime Adapter；
- **Persistence：** 进入与 Technology Profile 层次匹配的当前 Repository Authority，并保持单一可发现入口；
- **Update：** 官方版本 / 支持边界变化、外部依据失效、Eval 失败、Consumer 回归或上游 Method / Discipline / Architecture 变化时重新检查；
- **Supersede：** 新 baseline 必须明确取代关系、适用版本范围和当前入口，旧内容只作为历史证据保留；
- **Escalation：** 如果 Profile 需要改变 Core Method、重大 Architecture / Contract、Human / Integration Boundary，覆盖 Consumer Authority，或外部权威冲突无法裁决，返回相应更高层处理。

## 12. Foundation v1 的应用边界

Foundation v1 使用本契约只完成一个代表性实例：

> **Vue 3 + TypeScript Technology Profile**

WI-04 只建立本文契约，不在本阶段研究 Vue / TypeScript 具体规则。

本文集成后进入 WI-05；WI-05 必须按本契约完整走通 Research → Candidate Profile → Architecture Fit → Draft Profile → Verification Profile → Targeted Eval → AI Review → Integration Decision。

Foundation v1 不因为本契约已经存在就自动启动 Element Plus、Spring、Gradle 或其他 Profile；这些继续保持 Post-v1 Backlog。
