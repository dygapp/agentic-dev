---
name: specify
description: Creates or incrementally updates an authoritative WHAT/WHY specification and evaluates durable domain-fact candidates under repository authority. Use when intent is ready, required behavior needs to be explicit for a fresh agent, or a domain-authority candidate or conflict must be validated and routed.
---

# specify

## Purpose

创建或增量更新 WHAT / WHY Specification，使 Fresh Agent 在最小必要 Repository Context 下能够独立理解系统必须呈现的 Required Behavior、Scope、Boundary 与 Completion。

本 Skill 只固化已经确认的 Product / Domain / Governance 事实，不通过实现细节、当前代码便利性或常见工程实践反向发明需求。

当已确认信息可能跨多个功能持续有效时，本 Skill 还负责验证 Domain Authority Candidate，并按 Consumer Repository Authority 处理其确认、持久化、更新、取代或 Required Authority Action。进入 Specification 阶段本身不授予长期领域权威写入权限。

## Use When

- `clarify-intent` 已经收敛关键 Product Intent，需要形成正式 Feature Specification；
- Existing Specification 需要根据已经确认的 Product Decision 增量更新；
- Execute / Debug / Converge 等阶段回退，已确认需要修正 WHAT / WHY 权威；
- Clarify / Execute / Debug / Converge 已识别长期领域事实候选、缺失、冲突或失效；
- 已存在明确 Requirement，但当前表达不足以让 Fresh Agent 独立判断 Required Behavior 与 Completion。

如果 Intent 已经明确但 Specification 很小，可以使用轻量表达；不为了形式完整而制造与工作复杂度不成比例的文档。

## Do Not Use When

- 仍存在会 materially affect Goal、Scope、Product Behavior 或 Acceptance 的 Blocking Intent Question；
- 当前问题主要是 Specification 如何映射到技术系统；该职责属于 `technical-plan`；
- 当前只需要某个 Execution Unit 的文件级施工步骤、Exact Test Commands 或 Local Implementation Details；
- 目标是拆分 Execution Units、实施代码或执行验证；
- 期望通过阅读代码、数据库结构或现有实现习惯来反向决定未经确认的 Product Requirement。

如果 Product Decision 尚未解决，应返回 `clarify-intent`；不得为了产出 Specification 而猜测补齐需求。

## Inputs

- Clarified Intent
- Domain Authority Candidates（如存在）
- Repository Governance
- Relevant Domain Authority
- Existing Authoritative Behavior
- Existing Specification（如修改已有行为）

只加载形成当前 WHAT / WHY 权威所需的最小上下文。除非权威 Requirement 的理解确有必要，不默认读取完整 Codebase 或完整 Conversation History。

## Authority Sources

遵循当前 Repository Authority Hierarchy，并坚持 Authority First。

形成 Specification 时遵守以下规则：

1. Clarified Intent 提供当前 Feature / Change 已确认的 Goal、Scope、Observable Product Decisions 与剩余边界。
2. Repository Governance 与 Relevant Domain Authority 约束 Specification 可以承诺和必须遵守的行为。
3. Existing Authoritative Behavior 用于识别现有系统已经承诺的 Product Behavior，避免无意删除或冲突。
4. Existing Specification 在增量修改时作为当前 Feature Authority 输入，但不能覆盖更高优先级的已确认 Product / Domain / Governance 事实。
5. Current Code、测试、数据库结构或实现习惯可以反映 Current System State，但不能单独成为新 Product Requirement 的权威来源。
6. Conversation History 不构成权威事实来源。
7. Domain Authority 的确认、更新与取代由 Consumer Repository Authority 指定的产品 / 领域责任方或被明确授权的 Agent 执行；`specify` 的阶段职责不能替代写入授权。

如果 Requirement / Authority Sources 发生冲突，停止相关 Specification 更新并升级；不得自行选择一个更容易实现的解释。

## Procedure

### 1. Confirm Intent Readiness

确认当前输入已经能够确定：

- Goal；
- 主要 Scope；
- 关键 User-visible / System-observable Behavior；
- 会影响 Acceptance 的 Product Decisions。

如果仍存在会 materially change Product Intent / Acceptance 的未决问题，停止并返回 `clarify-intent`。

不要因为纯技术实现方式尚未确定而错误判定 Specification 不可形成。

### 2. Determine Create or Incremental Update Mode

如果不存在 Existing Specification，创建当前 Feature / Change 所需的最小完整 Specification。

如果存在 Existing Specification：

- 识别本次已确认 Product Decision 实际影响的部分；
- 只修改受影响的 WHAT / WHY；
- 保留未受影响且仍有效的 Existing Authority；
- 删除或修正已经与新权威冲突的旧内容；
- 不为了统一措辞而无谓重写整份 Specification。

增量更新必须保持最终 Specification 自洽，不能留下新旧语义互相冲突。

### 3. Establish Goal and Scope

明确系统要达成的 Product Outcome，以及本次 Specification 的边界。

Scope 应足以让 Fresh Agent 判断：

- 哪些行为属于本次工作；
- 哪些明确不属于本次工作；
- 哪些相邻能力只作为依赖或上下文，而不是当前 Requirement。

不要把实现组件、文件或技术层边界误写成 Product Scope，除非它们本身就是外部强制要求。

### 4. Define Observable Behaviors

用用户、外部系统或可观察系统结果描述系统必须做什么。

每个关键行为应说明足够的 Product Semantics，使 Fresh Agent 能区分：

- 触发或适用条件；
- 系统应呈现的结果；
- 与其他关键行为的必要关系。

优先描述 Behavior / Outcome，不描述 Class、Function、Endpoint Construction 或逐步实现过程。

### 5. Capture Business Rules

记录决定 Product Behavior 的业务规则，例如：

- Eligibility / Preconditions；
- 状态与允许行为之间的规则；
- 数据或业务含义上的约束；
- 必须保持的一致性；
- 已确认的优先级或判断口径。

只固化有权威依据的规则。不要把推测、行业惯例或实现方便性写成 Business Rule。

### 6. Define Boundary and Failure Behavior

识别会影响 Product Semantics 的关键边界和失败场景，并说明系统在这些情况下应呈现什么结果。

重点包括：

- 输入或状态不满足业务条件；
- 外部依赖不可用且 Product Behavior 已有要求；
- 关键资源不存在、重复或冲突；
- 权限 / Scope 边界对可见行为的影响；
- 其他会改变 Acceptance 的 Failure / Edge Behavior。

不要求枚举所有技术异常。只有对 Product Behavior 有意义的边界才进入 Specification。

### 7. Define Observable Acceptance Criteria

Acceptance Criteria 应让 Fresh Agent 能基于系统行为和证据判断 Requirement 是否满足。

每条关键 Acceptance 应尽量：

- 对应一个或多个 Required Behaviors / Rules；
- 描述可观察 Outcome；
- 包含必要条件或边界；
- 能区分“完成”和“部分完成”；
- 不通过指定内部实现方式来定义完成。

除非属于外部强制要求，不把“必须修改某文件”“必须使用某框架 / 数据库 / 类结构”作为 Product Acceptance Criteria。

### 8. Record Relevant Non-functional Constraints

只记录对当前 Feature / Change 有权威要求、并且会影响 Acceptance 或技术映射的 Non-functional Constraints。

例如可能包括：

- 明确性能目标；
- 安全 / 隐私义务；
- 兼容性要求；
- 可用性、审计或合规义务；
- 其他已经确认的质量边界。

如果没有相关权威要求，不为了“Specification 看起来完整”而发明 NFR。

### 9. Apply the WHAT / WHY Filter

检查 Specification 是否混入默认不属于该层的 HOW 内容。

除非属于外部强制 Requirement，否则移出或避免写入：

- Source File Paths；
- Class / Function Names；
- Framework-specific Construction Details；
- Database / Persistence Implementation Choices；
- Internal Component Wiring；
- Step-by-step Edit Instructions；
- Exact Build / Test Commands；
- 当前 Unit 的 JIT Execution Plan。

如果某个技术约束确实是外部强制 Requirement，应描述其 Requirement 意义和约束，而不是扩展成施工计划。

### 10. Evaluate Domain Authority Candidates

检查当前 Specification 中已确认的业务术语、业务不变量、跨功能规则或其他领域事实是否需要独立于当前 Feature 长期维护。

满足以下一项或多项时，应显式评估创建或更新 Domain Authority：

- 预计会被多个功能、缺陷处理或独立工作流持续消费；
- 后续 Agent 只读取单个 Feature Specification 时容易遗漏或产生冲突解释；
- 需要独立于当前 Feature 生命周期持续维护；
- 当前工作修正了已有长期领域事实，旧事实继续生效会误导后续工作。

对每个候选明确：

1. 留在 Feature Specification，还是进入 / 更新长期 Domain Context；
2. 哪个授权角色负责确认并形成该权威；
3. Consumer Repository 选择的可发现持久化载体；
4. 何时更新、旧事实如何取代或同步修正引用；
5. 哪些权威冲突、产品意图变化或未授权决定必须升级。

如果 Agent 已获授权且当前任务包含相应更新，可以形成或更新 Domain Authority；否则输出 Required Domain Authority Action 并停止把该候选视为已闭环。不得用代码、测试、聊天或局部计划代替缺失的业务权威确认。

### 11. Check Internal Consistency

检查：

- Goal 与 Scope 是否一致；
- Observable Behaviors 是否落在 Scope 内；
- Business Rules 是否与 Behavior / Boundary 冲突；
- Acceptance Criteria 是否覆盖关键 Required Behavior；
- Existing Specification 增量更新后是否残留过时或矛盾语义；
- 是否出现未经确认的 Product Scope Expansion；
- 是否仍存在 Requirement / Authority Conflict。

发现 Product Decision 缺失时返回 `clarify-intent`；发现 Authority Conflict 时升级，不在 Specification 中静默“修平”。

### 12. Run Fresh-Agent Spec Ready Check

假设一个没有当前 Conversation History 的 Fresh Agent，只读取最终 Specification 与最小必要 Repository Context。

检查它是否能够明确判断：

1. **What** — 系统必须做什么；
2. **Not What** — 哪些相邻行为不属于本次 Scope；
3. **Completion** — 什么可观察结果表示 Requirement 已满足；
4. **Ambiguity** — 是否仍存在会实质改变 Product Behavior / Acceptance 的关键歧义。

如果四项中任一项无法可靠判断：

- 如果缺口属于 Product Intent / Product Decision，返回 `clarify-intent`；
- 如果只是尚未决定 HOW，但 WHAT / WHY 已明确，不阻塞 Specification Ready；
- 如果来源冲突，按 Escalation Conditions 处理。

### 13. Produce or Update the Specification

输出最终 WHAT / WHY Specification，并保持其与当前 Authority 一致。

`specify` 到此退出，不自动创建 Technical Plan、Execution Units，也不自动进入 Execute。

## Outputs

输出 Feature / Change Specification。其语义应按需要覆盖：

- Goal
- Scope
- Observable Behaviors
- Business Rules
- Boundary / Failure Behavior
- Acceptance Criteria
- Relevant Non-functional Constraints
- Domain Authority Update / Supersede（已授权且需要时）
- Required Domain Authority Action（需要但当前无权更新时）

这些是语义要求，不是固定文件模板：

- 不要求固定文件名或目录；
- 不要求固定 Markdown 标题；
- 不要求 YAML Front Matter；
- 不要求一个阶段必须对应一个独立文件。

如果某类内容确实不适用，不为填满格式而发明信息；但省略后仍必须满足 Fresh-Agent Spec Ready Check。

## Exit Conditions

Fresh Agent 只读取最终 Specification 与最小必要 Repository Context，就能可靠判断：

1. 要做什么；
2. 不做什么；
3. 什么情况下算完成；
4. 是否仍存在关键歧义。

并且不存在尚未解决的 Requirement / Authority Conflict 或 Product Decision 缺口阻止上述判断；已识别的 Domain Authority Candidate 已明确判定为留在 Specification、进入 / 更新 Domain Authority，或返回相应 Authority，不只留在会话中。

## Escalation Conditions

出现以下情况时必须停止并升级或返回上游：

- Requirement / Authority Conflict；
- Product Decision 尚未解决，无法在现有权威下确定 Required Behavior；
- Specification 必须 materially change 已确认 Scope / Intent 才能继续；
- Agent 无权自主决定的高影响 Product Choice；
- Agent 无权确认、更新或取代会改变产品意图 / 业务边界的长期领域事实；
- 与 Product Requirement 直接相关的安全、隐私、不可逆或其他 Explicit Policy Decision 尚未确认。

纯技术实现选择、普通低影响可逆 HOW 不升级给 Human；它们留给 `technical-plan` 或 Execute 的适当职责。

## Context Rules

- Authority First；
- Progressive Disclosure，只加载形成当前 WHAT / WHY 所需的最小上下文；
- Conversation History 不作为权威知识；
- 不默认加载完整 Codebase；Current Code 不能反向覆盖 Product Authority；
- Existing Specification 更新时优先增量加载受影响部分，同时检查最终文档的一致性；
- Domain Authority 使用 Consumer Repository 选择的载体和授权流程，不强制固定目录、文件名或模板；
- 不强制固定 Specification 文件、目录、Markdown 模板或 YAML Front Matter；
- 不把 Source Paths、Framework、Persistence、Exact Commands 或 JIT Plan 提前固化到 Specification；
- 不自动调用 `technical-plan`、`slice-work`、`readiness-check`、`execute-unit` 或接管后续生命周期。

## Allowed Sub-skills / Disciplines

- Context Discipline
- Human Escalation
