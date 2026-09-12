---
name: technical-plan
description: Resolves durable cross-unit HOW decisions, maintains cross-feature architecture context changes, and conditionally persists ADRs for decisions whose background or trade-offs need durable history. Use for cross-module, data, integration, migration, shared contract, deployment topology, or significant architecture work; skip when only local reversible implementation details remain.
---

# technical-plan

## Purpose

在 Specification 无法直接、安全映射到当前技术系统时，解决跨 Execution Unit 有持续协调价值的长期 HOW 决策。

本 Skill 不是默认阶段产物生成器。若不存在必须跨 Unit 持久协调的技术不确定性，应明确返回“不需要 Technical Planning”，不制造长期 Technical Plan。

当技术规划改变需要跨当前功能持续消费的架构状态时，本 Skill 负责形成或更新适当的 Architecture Authority Artifact；其中只有需要长期保留决定背景、主要权衡或替代关系的重要架构决定才形成或更新架构决策记录（Architecture Decision Record，ADR）。ADR 是 Architecture Context 中的条件性决策记录，不等同于全部架构状态，也不是 Technical Plan 的固定组成部分。

## Use When

当 Specification 已 Ready，但实施前仍存在需要跨 Execution Unit 持续协调的技术问题时使用。

典型触发包括：

- Cross-module Behavior；
- New Data / Persistence Model；
- New External Integration；
- Migration；
- Shared / Public Contract Change；
- Deployment Topology Change；
- Significant Architecture Trade-off。

如果多个 Execution Units 必须共享同一个长期技术决定才能安全实现或保持一致，也属于适用场景。

如果 Execute、Systematic Debugging 或 Converge 暴露了新的长期架构状态、长期架构决策或现有 Architecture Context 失效，也应回到本 Skill 完成 Architecture Authority 更新与必要 ADR 评估，而不是在代码、局部计划或下游 Artifact 中静默固化。

已经确认的技术要求会改变跨功能持续有效的 Architecture Context、需要维护 Architecture Authority 时，即使不需要单独持久化 Technical Plan，也属于本 Skill。

## Do Not Use When

- Specification 可以直接、安全映射到实现，且不存在需要维护的 Architecture Context 或需要评估的 ADR；
- 只需要当前 Execution Unit 的文件级操作顺序、Exact Test Commands 或 Local Implementation Details；
- 技术选择属于普通、低影响、可逆的局部实现细节；
- Product Intent / Specification 本身仍有阻塞问题；
- 当前目标是拆分 Execution Units、执行代码或验证实现。

不要因为“技术上还有很多细节没决定”就自动创建长期 Plan。只有对跨 Unit 安全实施和持续协调有价值的决定才属于本 Skill。

同样，不要因为进入 Technical Planning 就自动创建 ADR。只有满足长期架构权威条件的决定才进入 ADR。

## Inputs

- Specification
- Current Architecture
- Relevant ADRs
- Current Codebase State
- Technical Constraints

只加载判断和解决当前 Durable Technical Uncertainty 所需的最小技术上下文，不要求预先读取完整 Codebase 或完整 Conversation History。

## Authority Sources

遵循当前 Repository Authority Hierarchy，并坚持 Authority First。

技术规划时遵守以下规则：

1. Specification 定义 WHAT / WHY，Technical Plan 不得重新定义 Product Intent。
2. Architecture Context 提供当前有效的长期技术状态；ADR 提供满足条件的重要架构决定及其理由。两者都不能被 Technical Plan 静默覆盖。
3. Current Codebase State 用于判断当前系统真实结构、能力和技术限制，但不能反向覆盖更高层 Product Authority。
4. Technical Constraints 只有在具有当前权威依据时才能成为长期设计约束。
5. Conversation History 不构成权威事实来源。
6. 当前 Unit 的临时施工信息不是 Durable Technical Authority。
7. 需要改变长期 Architecture Context 时，必须更新适当的架构权威；满足 ADR 条件时再处理 ADR 的创建、更新或取代关系。

如果权威来源之间发生冲突，停止相关规划并升级；不得自行选择一个方便实现的解释继续。

## Procedure

### 1. Confirm Specification Readiness

确认 Specification 已经足以判断 Required Behavior、Scope、Boundary 与 Acceptance。

如果仍存在会 materially change Product Intent / Acceptance 的问题，返回 `clarify-intent` / `specify`。

不要用 Technical Planning 来填补 Requirement 缺口，也不要通过技术选择静默定义产品行为。

### 2. Determine Whether Technical Planning Is Needed

识别实施前仍存在的技术不确定性，并逐项判断：

- 是否影响多个 Execution Units；
- 是否需要跨 Unit 保持一致；
- 是否会改变共享 Contract、Data Model、Integration、Migration、Deployment 或 Architecture Boundary；
- 如果留到各 Unit 独立决定，是否会造成返工、冲突、不可安全拆分或不可安全实施；
- 是否属于需要长期保存的 Durable Decision，而不是单 Unit JIT Detail。

如果这些条件都不成立、Specification 可以直接安全映射到实现，并且不存在需要维护的 Architecture Context 或需要评估的 ADR，输出：

```text
不需要 Technical Planning
```

然后退出，不创建长期 Artifact。

如果不需要单独持久化 Technical Plan，但已经确认 Architecture Context 必须更新，继续执行第 8 步；“无需 Technical Plan Artifact”不等于“无需维护 Architecture Authority”。

### 3. Frame the Durable Technical Questions

如果需要 Technical Planning，只保留必须在实施前解决、且对多个 Unit 有持续价值的问题。

按需考虑：

- Technical Approach；
- Component Boundaries；
- Data / Contract Design；
- Important Seams；
- Migration Strategy；
- Testing Strategy；
- Risks / Constraints。

不要为了填满分类而制造决策；某一类不适用时可以省略。

### 4. Inspect Relevant Current System State

使用 Progressive Disclosure 读取与当前技术问题直接相关的：

- Architecture；
- Relevant ADR；
- Current Code / Interfaces / Data Structures；
- Existing Shared Contracts；
- Deployment / Integration Constraints；
- Repository Rules。

只读取足够判断真实技术边界的上下文，不为了“全面了解代码库”扩大范围。

### 5. Evaluate Technical Options

对需要决策的问题评估可行方案，重点判断：

- 是否满足 Specification；
- 是否符合已有 Architecture / ADR；
- 是否减少跨 Unit 隐藏耦合；
- 是否支持可验证的实施边界；
- 是否引入 Migration / Compatibility / Operational Risk；
- 是否存在高影响、不可逆或超出 Agent Authority 的权衡（Trade-off）。

普通、低影响、可逆的局部实现选择不需要在长期 Technical Plan 中冻结，可以留给 Execute。

### 6. Prevent Silent Redefinition of Intent

对每个拟定技术决定检查：

> 这个决定是否只是 HOW，还是实际上改变了 Specification 所定义的 WHAT / WHY？

如果技术方案要求改变：

- Product Goal；
- Scope；
- User-visible Behavior；
- Acceptance Result；
- 已确认 Business Rule；

则不得在 Technical Plan 中直接接受该变化。返回 `specify` / `clarify-intent`，必要时升级 Human Authority。

### 7. Resolve or Escalate Blocking Trade-offs

如果一个技术问题属于普通、低影响、可逆且 Agent 有权限的选择，由 Agent 自主决定并继续。

出现以下情况时停止并升级：

- 重大架构方向（Major Architecture Direction）；
- Destructive / Hard-to-reverse Data Operation；
- Security / Privacy Sensitive Decision；
- 未授权 Shared / Production / External Side Effect；
- Irreversible / High-impact Trade-off；
- 必须改变 Product Intent 才能继续。

升级时只提出解除当前阻塞所需的技术决策，不扩大为无关架构讨论。

### 8. Maintain Architecture Context and Evaluate ADR Persistence

在长期技术决策已经形成后，先判断它是否改变需要跨当前功能持续消费的系统结构、组件与数据边界、共享 / 公共契约、集成 / 部署约束或其他 Architecture Context。

如果不改变跨功能持续有效的架构状态，决定可以继续留在当前 Feature 的 Technical Plan。

如果改变 Architecture Context：

1. 按当前 Repository Authority 选择适当的架构说明、契约、模型、代码或其他可发现载体；
2. 创建或更新相应 Architecture Authority Artifact；
3. 旧架构状态失效时，显式更新状态、引用或取代关系，避免新旧约束同时被视为有效；
4. 对重大架构方向、高影响难逆权衡或超出 Agent Authority 的决定，在接受或持久化为当前权威前升级。

完成 Architecture Context 判断后，再评估其中的重要决定是否需要 ADR。ADR 用于保留决定背景、主要权衡、后果或替代关系，不用于复制全部当前架构状态。

当决定具有以下一项或多项特征时，应显式评估形成或更新 ADR：

- 预计约束未来多个功能、模块或独立工作流；
- 改变系统级组件、数据、集成、部署或共享 / 公共契约边界（Shared / Public Contract Boundary）；
- 替换成本较高、难以安全回滚，或形成长期兼容 / 迁移义务；
- 多个合理方案具有实质不同的长期后果，需要保留选择理由与主要权衡；
- 后续 Agent 若不知道该决定及其理由，容易重新打开已关闭的架构选择或产生冲突实现。

以下内容通常不形成 ADR：

- 只服务当前功能的普通 Technical Plan Decision；
- 单 Unit 内局部、低影响、可逆的实现选择；
- 文件、命令、编辑顺序等 JIT Detail；
- 尚未形成稳定决定的探索记录。

如果需要 ADR：

1. 判断应创建新的 ADR、更新现有 ADR，还是以新决定取代旧 ADR；
2. 保留足以解释决定的 Context、Decision、主要 Alternatives / Trade-offs 与 Consequences；
3. 新决定取代旧 ADR 时显式保留被取代 / 替换（Superseded / Replaced）关系；
4. 按当前 Repository Authority 选择适当载体，不强制固定 `adr/` 目录、文件名或模板；
5. 对重大架构方向、高影响难逆权衡或超出 Agent Authority 的决定，在接受或持久化为当前权威前升级。

如果不满足 ADR 条件，不为了形式完整性制造 ADR；但只要决定已经改变 Architecture Context，仍必须完成前述 Architecture Authority 更新，不能只留在 Technical Plan。

### 9. Record Durable Technical Decisions

只记录对当前功能及其跨 Unit 实施有持续协调价值的最终技术决定。

按需包含：

- Technical Approach；
- Component Boundaries；
- Data / Contract Design；
- Important Seams；
- Migration Strategy；
- Testing Strategy；
- Risks / Constraints。

每项决定应足以约束后续 `slice-work` 和 Execute，但不要提前写入：

- 精确 Source File Paths；
- 逐文件 Edit Sequence；
- Exact Test Commands；
- 临时 Debug 步骤；
- 当前 Unit 的 Local Implementation Details。

这些内容属于 Execute 内的 JIT Execution Plan。

需要跨功能持续有效的架构状态不应只埋在 Technical Plan 中；它们应按第 8 步进入相应 Architecture Authority，其中满足条件的重要决定再形成或更新 ADR。

### 10. Check Cross-unit and Architecture Coherence

检查最终 Technical Plan、Architecture Authority 与相关 ADR：

- 是否覆盖所有必须在实施前解决的 Durable Technical Questions；
- 不同技术决定之间是否互相一致；
- 是否与 Specification、当前 Architecture Context、有效 ADR 冲突；
- 是否仍存在会阻止安全切分或实施的跨 Unit 技术不确定性；
- 是否存在应更新 Architecture Context 但尚未进入适当 Repository Authority 的架构权威缺口；
- 是否存在满足 ADR 条件但尚未创建、更新或取代 ADR 的决策记录缺口；
- 本次新增或重大修改的长期架构权威是否具有明确的生命周期责任；
- 是否错误持久化了只属于单 Unit 的施工细节。

如果仍存在 Blocking Technical Uncertainty、Architecture Authority / ADR Gap 或 Artifact Lifecycle Gap，则继续在当前职责内解决或按 Escalation Conditions 升级。

### 11. Produce the Result

如果无需长期 Technical Plan Artifact，且没有 Architecture Authority 更新：

```text
不需要 Technical Planning
```

不创建长期 Plan Artifact。

如果需要，则输出只包含 Durable Technical Decisions 的 Technical Plan，并按第 8 步形成必要的 Architecture Authority 更新与条件性 ADR。如果不需要 Technical Plan Artifact、但需要 Architecture Authority 更新，则明确前者不需要并完成后者。

`technical-plan` 到此退出，不自动创建 Execution Units，也不自动进入 Execute。

## Outputs

### No Durable Technical Planning Needed

```text
不需要 Technical Planning
```

这表示不要求为了流程完整性创建空 Plan 或 ADR。只有不存在待完成的 Architecture Authority 更新时，Specification 才可以直接、安全进入 Slice & Ready。

### Durable Technical Planning Needed

按需输出：

- Technical Approach
- Component Boundaries
- Data / Contract Design
- Important Seams
- Migration Strategy
- Testing Strategy
- Risks / Constraints

这些是语义类别，不是固定模板。只记录对当前功能跨 Unit 协调有持续价值的内容。

### Architecture Authority Update

当决定改变跨功能持续有效的 Architecture Context 时，形成或更新 Consumer Repository 选择的架构权威载体，并按需说明：

- 当前有效的架构状态；
- 适用范围与消费者；
- 更新与取代关系；
- 必要的 Authority / Escalation 状态。

### Conditional ADR

只有满足 ADR 条件时，附加形成或更新决策记录。内容应足以记录：

- Context / Decision；
- 主要 Alternatives / Trade-offs；
- Consequences；
- 适用范围；
- 必要的 Superseded / Replaced 关系。

不要求：

- 固定文件名或目录；
- 每个 Technical Plan 都有 ADR；
- 特定 Architecture Diagram；
- YAML Front Matter；
- 一个阶段必须对应一个独立文件。

## Exit Conditions

`technical-plan` 只有在以下条件满足时才完成：

- 实施前必须解决的跨 Unit 技术不确定性已经解决，或已经确认不存在这类不确定性；
- 最终决定与 Specification Intent 一致，没有 Silent Redefinition；
- 对当前功能需要长期协调的技术边界已经形成足够清晰的 Durable Decisions；
- 需要形成或更新的 Architecture Context 已经进入适当 Repository Authority；
- 满足 ADR 条件的重要决定已经形成、更新或取代相应 ADR；
- 不再存在会阻止安全进入 Slice & Ready 的 Blocking Technical Uncertainty、Architecture Authority / ADR Gap 或 Artifact Lifecycle Gap。

“无需 Technical Planning”本身也是合法完成结果。

## Escalation Conditions

出现以下情况时必须停止并升级或返回上游：

- 重大架构方向（Major Architecture Direction）；
- Destructive / Hard-to-reverse Data Operation；
- Security / Privacy Sensitive Decision；
- 未授权 Shared / Production / External Side Effect；
- Agent 无权自主决定的高影响或不可逆权衡；
- 必须改变 Product Intent / Specification 才能继续；
- Authoritative Sources Conflict。

普通、低影响、可逆且可由现有技术证据判断的局部实现选择不升级给 Human，也不要求进入长期 Technical Plan 或 ADR。

## Context Rules

- Authority First；
- Progressive Disclosure，只加载解决 Durable Technical Uncertainty 所需的上下文；
- Conversation History 不作为权威知识；
- 允许读取 Relevant Architecture / ADR / Current Codebase State，但 Current Code 不能反向覆盖 Product Authority；
- Technical Plan 只持久化当前功能跨 Unit 有持续协调价值的 Durable Decisions；
- 跨功能持续有效的架构状态进入 Architecture Authority；其中需要保留背景、权衡或替代关系的重要决定按条件进入 ADR；
- 文件级施工步骤、Exact Test Commands 与 Local Implementation Details 留给 Execute 内 JIT Execution Plan；
- 不强制固定 Technical Plan 文件、ADR 目录、Diagram、Markdown / YAML 模板；
- 不自动调用 `slice-work`、`readiness-check`、`execute-unit` 或接管后续生命周期。

## Allowed Sub-skills / Disciplines

- Context Discipline
- Human Escalation
- Design Quality
