# technical-plan

## Purpose

在 Specification 无法直接、安全映射到当前技术系统时，解决跨 Execution Unit 有持续协调价值的长期 HOW 决策。

本 Skill 不是默认阶段产物生成器。若不存在必须跨 Unit 持久协调的技术不确定性，应明确返回“不需要 Technical Planning”，不制造长期 Technical Plan。

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

## Do Not Use When

- Specification 可以直接、安全映射到实现；
- 只需要当前 Execution Unit 的文件级操作顺序、Exact Test Commands 或 Local Implementation Details；
- 技术选择属于普通、低影响、可逆的局部实现细节；
- Product Intent / Specification 本身仍有阻塞问题；
- 当前目标是拆分 Execution Units、执行代码或验证实现。

不要因为“技术上还有很多细节没决定”就自动创建长期 Plan。只有对跨 Unit 安全实施和持续协调有价值的决定才属于本 Skill。

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
2. Architecture / ADR 提供已确认的长期技术约束和决策。
3. Current Codebase State 用于判断当前系统真实结构、能力和技术限制，但不能反向覆盖更高层 Product Authority。
4. Technical Constraints 只有在具有当前权威依据时才能成为长期设计约束。
5. Conversation History 不构成权威事实来源。
6. 当前 Unit 的临时施工信息不是 Durable Technical Authority。

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

如果这些条件都不成立，并且 Specification 可以直接、安全映射到实现，输出：

```text
不需要 Technical Planning
```

然后退出，不创建长期 Artifact。

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
- 是否存在高影响、不可逆或超出 Agent Authority 的 Trade-off。

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

- Major Architecture Direction；
- Destructive / Hard-to-reverse Data Operation；
- Security / Privacy Sensitive Decision；
- 未授权 Shared / Production / External Side Effect；
- Irreversible / High-impact Trade-off；
- 必须改变 Product Intent 才能继续。

升级时只提出解除当前阻塞所需的技术决策，不扩大为无关架构讨论。

### 8. Record Durable Technical Decisions

只记录对跨 Unit 实施有持续协调价值的最终技术决定。

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

### 9. Check Cross-unit Coherence

检查最终 Technical Plan：

- 是否覆盖所有必须在实施前解决的 Durable Technical Questions；
- 不同技术决定之间是否互相一致；
- 是否与 Specification、Architecture、ADR 冲突；
- 是否仍存在会阻止安全切分或实施的跨 Unit 技术不确定性；
- 是否错误持久化了只属于单 Unit 的施工细节。

如果仍存在 Blocking Technical Uncertainty，则继续在当前职责内解决或按 Escalation Conditions 升级。

### 10. Produce the Result

如果无需长期 Technical Planning：

```text
不需要 Technical Planning
```

不创建长期 Plan Artifact。

如果需要，则输出只包含 Durable Technical Decisions 的 Technical Plan。

`technical-plan` 到此退出，不自动创建 Execution Units，也不自动进入 Execute。

## Outputs

### No Durable Technical Planning Needed

```text
不需要 Technical Planning
```

这表示 Specification 可以直接、安全进入 Slice & Ready；不要求为了流程完整性创建空 Plan。

### Durable Technical Planning Needed

按需输出：

- Technical Approach
- Component Boundaries
- Data / Contract Design
- Important Seams
- Migration Strategy
- Testing Strategy
- Risks / Constraints

这些是语义类别，不是固定模板。只记录对跨 Unit 有持续价值的内容。

不要求：

- 固定文件名或目录；
- 固定 ADR；
- 特定 Architecture Diagram；
- YAML Front Matter；
- 一个阶段必须对应一个独立文件。

## Exit Conditions

`technical-plan` 只有在以下条件满足时才完成：

- 实施前必须解决的跨 Unit 技术不确定性已经解决，或已经确认不存在这类不确定性；
- 最终决定与 Specification Intent 一致，没有 Silent Redefinition；
- 对需要长期协调的技术边界已经形成足够清晰的 Durable Decisions；
- 不再存在会阻止安全进入 Slice & Ready 的 Blocking Technical Uncertainty。

“无需 Technical Planning”本身也是合法完成结果。

## Escalation Conditions

出现以下情况时必须停止并升级或返回上游：

- Major Architecture Direction；
- Destructive / Hard-to-reverse Data Operation；
- Security / Privacy Sensitive Decision；
- 未授权 Shared / Production / External Side Effect；
- Agent 无权自主决定的高影响或不可逆 Trade-off；
- 必须改变 Product Intent / Specification 才能继续；
- Authoritative Sources Conflict。

普通、低影响、可逆且可由现有技术证据判断的局部实现选择不升级给 Human，也不要求进入长期 Technical Plan。

## Context Rules

- Authority First；
- Progressive Disclosure，只加载解决 Durable Technical Uncertainty 所需的上下文；
- Conversation History 不作为权威知识；
- 允许读取 Relevant Architecture / ADR / Current Codebase State，但 Current Code 不能反向覆盖 Product Authority；
- 只持久化跨 Unit 有持续协调价值的 Durable Decisions；
- 文件级施工步骤、Exact Test Commands 与 Local Implementation Details 留给 Execute 内 JIT Execution Plan；
- 不强制固定 Technical Plan 文件、ADR、Diagram、Markdown / YAML 模板；
- 不自动调用 `slice-work`、`readiness-check`、`execute-unit` 或接管后续生命周期。

## Allowed Sub-skills / Disciplines

- Context Discipline
- Human Escalation
- Design Quality
