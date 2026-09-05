---
name: slice-work
description: Turns a ready specification and optional technical plan into bounded, traceable, context-fit execution units with observable completion conditions and explicit dependencies. Use before readiness checking or when convergence exposes implementation gaps that need new or corrected execution work.
---

# slice-work

## Purpose

将已经 Ready 的 Specification 与可选 Technical Plan 转换为适合 Fresh Agent 独立执行和验证的纵向 Execution Units。

本 Skill 负责形成和塑形执行单元集合，并建立规格验收义务到实现责任 / 验证责任与计划验证证据的闭环。它不负责最终就绪结论，不负责执行具体执行单元，也不通过拆分过程新增产品范围。

## Use When

- Specification 已满足进入 Slice & Ready 的条件；
- Optional Technical Plan 已完成，或已经确认不需要长期 Technical Planning；
- 需要把一个 Feature / Change 组织成一个或多个可执行工作单元；
- `converge` 发现 Feature Gap，需要形成新的或修正后的 Execution Work。

如果一个纵向 Unit 已经足够 Bounded、Context-fit 且可独立验证，可以只形成一个 Unit；不为了“必须拆分”而制造额外边界。

## Do Not Use When

- 当前只有 Roadmap / Backlog / Issue 中的 Future Work、Planning Candidate 或 Requirement Candidate，尚未形成 Ready Specification；
- Product Intent 仍存在会 materially affect Goal、Scope、Behavior 或 Acceptance 的阻塞歧义；
- 必要的 Technical Planning 尚未完成；
- 当前工作只是单个 Execution Unit 内的临时 JIT 施工计划；
- 目标是判断 Unit Set 是否最终可以进入 Execute；该职责属于 `readiness-check`；
- 目标是直接修改代码、运行测试或完成当前 Unit；该职责属于 Execute。

如果上游输入不足以安全拆分，应停止并返回对应职责层，不通过猜测 Scope、Intent 或 Major Design 来制造 Units。

## Inputs

- Specification
- Optional Technical Plan

只加载完成当前拆分所需的最小权威上下文。除非拆分边界确实依赖，否则不需要预先读取完整 Codebase、完整 Conversation History 或生成文件级施工计划。

## Authority Sources

遵循当前 Repository Authority Hierarchy。

拆分时遵守以下规则：

1. Specification 决定 Product / Feature Scope、Required Behavior 与 Acceptance Boundary。
2. Technical Plan（如存在）只提供跨 Unit 有持续价值的 Durable Technical Constraints，不得反向改变 Specification Intent。
3. Execution Unit 只能承载实现既有 Specification 所需的工作，不得新增未授权 Product Scope。
4. Repository / Architecture / Governance Constraints 只在与当前 Unit Boundary 或执行约束相关时加载，并按权威顺序解释。
5. Conversation History 不构成权威来源。

如果权威来源发生冲突，停止拆分并升级；不得选择一个方便实现的解释继续。

## Procedure

### 1. Confirm Upstream Readiness

确认：

- Specification 已足够明确，可以判断 Goal、Scope、Observable Behavior 与 Completion；
- 如果存在实施前必须长期协调的重大技术决定，它们已经通过 Technical Planning 解决；
- 当前工作确实需要形成 Execution Units，而不是当前 Unit 的 JIT Plan。

Roadmap 顺序、预先出现的 `EU-xx` / Unit ID、Issue 标签或“下一项”名称只可作为待核验线索，不能替代 Specification Readiness。输入仍是 Planning / Requirement Candidate 时，保留其 Backlog / Issue 身份并返回 `clarify-intent` / `specify`；不得为了沿用编号而猜测 Scope、Acceptance 或 Unit Boundary。

如果因为上述 Planning / Requirement Candidate 状态返回上游，结论还应明确后续身份边界：Specification Ready 且必要 Technical Planning 完成后，`slice-work` 才形成 Candidate Execution Units，并可以为这些 Candidate Units 分配或确认稳定 Identifier；这些 Unit 仍保持 Candidate 状态，必须继续进入 `readiness-check`。Identifier 本身不构成 Readiness PASS，也不授予 Execute 权限。已有 Backlog / Issue ID 可以继续作为规划追踪标识，但不得因此提前把当前候选描述成 Execution Unit。

如果 Product Intent 仍阻塞，返回 `clarify-intent` / `specify`。

如果必须先解决跨 Unit 的 Major / Durable Technical Decision，返回 `technical-plan`，必要时按 Authority、Impact、Reversibility 升级。

### 2. Build a Specification Coverage View

从规格说明中识别需要获得实现覆盖与验证覆盖的内容，例如：

- Observable Behaviors；
- Acceptance Criteria；
- Business Rules；
- Boundary / Failure Behavior；
- Relevant Non-functional Constraints。

覆盖视图用于防止遗漏、重复、无来源工作或只有实现范围而没有验证责任的义务。它可以只是当前拆分过程中的工作视图，不要求创建新的长期产物。

对每项必需行为 / 验收义务分别判断：

- 哪个执行单元承担实现责任；
- 哪个执行单元承担验证责任；
- 如果只有跨执行单元组合后才能有效证明，是否具有明确的功能整体验证责任；
- 计划使用什么当前证据区分该义务是否真实满足。

实现责任与验证责任可以相同，也可以基于真实跨执行单元原因分开，但不能让验证责任未归属。功能整体验证责任不能作为推迟普通执行单元级验证的兜底标签。

### 3. Identify Vertical Execution Seams

优先按 Observable Behavior / Verifiable Outcome 识别 Unit 边界。

一个好的候选 Unit 应尽量形成从必要实现到可观察结果的纵向切片，而不是只按技术层拆成“数据库层”“服务层”“接口层”“测试层”等无法独立证明业务结果的横向工作。

拆分时优先考虑：

- 能否独立形成可观察结果；
- 能否在一个 Fresh Execution Context 中理解；
- 能否独立验证；
- 是否减少与其他 Unit 的隐藏耦合。

### 4. Form Candidate Execution Units

每个 Execution Unit 至少定义：

```text
id
goal
spec_reference
completion_condition
dependencies
constraints
```

字段语义：

- `id`：当前工作范围内可稳定引用该 Unit 的标识；不规定统一命名格式。
- `goal`：该 Unit 要实现的单一、清晰结果。
- `spec_reference`：该 Unit 所覆盖的 Specification 行为、规则或 Acceptance 的可追溯引用。
- `completion_condition`：可以用当前证据判断是否完成的可观察条件。
- `dependencies`：进入本 Unit 前真实必须成立的其他工作或条件；没有则明确为空。
- `constraints`：执行时必须遵守、且对该 Unit 有持续价值的权威约束。

不要把精确 Source File Paths、逐文件 Edit Sequence、Exact Test Commands 或其他 JIT Execution Plan 内容作为通用长期字段要求。

除上述最小字段外，执行单元集合必须通过执行单元字段、覆盖视图或等价载体表达：

```text
规格验收义务
→ 实现责任 / 验证责任
→ 计划验证证据
```

不要求固定字段名，也不要求一条验收义务对应一个测试。计划验证证据可以是与行为和风险相称的自动化测试、集成 / 运行时观察、人工可重复检查或仓库规则允许的其他证据；但不能只写“代码完成”“测试通过”或其他无法证明具体义务的宽泛条件。

### 5. Expose Dependencies and Hidden Coupling

检查候选 Units 之间是否存在：

- 隐藏前置条件；
- 循环依赖；
- 错误执行顺序；
- 多个 Unit 共同依赖但未显式表达的 Durable Constraint；
- 一个 Unit 实际需要另一个 Unit 的未完成行为才能验证。

将真实依赖显式化；不要为了表面“独立”而隐瞒耦合。

如果依赖本质上来自尚未解决的 Major Design Decision，返回 `technical-plan`，而不是用临时排序代替设计决定。

### 6. Check Unit Quality

逐个检查候选 Unit 是否尽量满足：

- **Vertical**：围绕 Outcome，而非纯技术层；
- **Independently Verifiable**：Completion Condition 能单独获得证据；
- **验收责任明确**：承接的必需行为 / 验收义务及其验证责任可识别；
- **证据充分**：计划验证证据足以区分所承接义务是否满足；
- **Bounded**：Goal 与 Scope 不无限扩张；
- **Traceable**：能回到 Specification；
- **Context-fit**：适合一个 Fresh Agent 在合理最小上下文中执行；
- **Low Hidden Dependency**：关键依赖已显式表达。

### 7. Reshape Weak Units

对以下候选进行重新塑形：

- **Too Large**：一个 Fresh Context 难以安全理解、实现和验证；
- **Horizontal-only**：只有技术层产物，没有可独立验证 Outcome；
- **Highly Coupled**：必须频繁跨多个 Unit 才能形成证据；
- **Ambiguous Completion**：无法明确判断何时完成；
- **无责任归属的验证**：验收义务没有执行单元级或合法且显式的功能整体验证责任；
- **计划证据薄弱**：只验证主路径，无法证明分页、排序、边界 / 失败、多状态、跨入口等规格说明要求的关键差异；
- **Untraceable**：找不到合法 Specification 来源；
- **Scope-expanding**：包含 Specification 未授权行为。

可通过拆分、合并、调整边界、显式依赖或移除无来源工作来修正。

如果无法在不改变 Product Intent、Scope 或 Required Major Design 的情况下安全塑形，停止并升级，而不是强行输出 Unit Set。

### 8. Check Execution Coverage

回到 Specification Coverage View，确认：

- 必需行为同时获得合理实现覆盖与验证覆盖；
- 每项验收义务都有明确责任，或有真实跨执行单元原因支持的功能整体验证责任；
- 计划验证证据足以证明关键差异，而不只覆盖主路径；
- 没有重要遗漏；
- 没有明显 Orphan Work；
- 没有由 Units 新增未授权 Product Scope；
- Unit 之间的依赖与顺序能够解释。

Coverage 不要求每个 Specification 条目机械映射到唯一 Unit；要求的是整个 Unit Set 能够合理覆盖实施工作，并保持可追溯。

### 9. Produce the Unit Set

输出一个或多个候选 Execution Units。

本阶段可以为已经形成的 Candidate Execution Unit 分配稳定 Identifier，以建立追踪、依赖和后续检查关系。该 Identifier 不表示 Readiness PASS；即使沿用或映射已有 Backlog / Issue ID，也必须继续显式保持候选状态，直到 `readiness-check` 给出最终 Verdict。

`slice-work` 只能说明该 Unit Set 已完成拆分与塑形，可以交给 `readiness-check`；不得自行给出最终 `PASS`，也不自动进入 `execute-unit`。

## Outputs

输出一个或多个 Execution Units，每个至少包含：

```text
id: <identifier>
goal: <single clear outcome>
spec_reference: <trace to authoritative specification>
completion_condition: <observable, verifiable completion condition>
dependencies:
  - <dependency, if any>
constraints:
  - <durable relevant constraint, if any>
```

必要时可以附简短覆盖说明，帮助解释执行单元集合如何覆盖规格说明，以及各项验收责任 / 验证责任与计划证据如何分配；覆盖说明不是新的强制长期产物，也不能替代 `spec_reference`。

无论采用何种载体，输出都必须能恢复：

```text
规格验收义务
→ 实现责任 / 验证责任
→ 计划验证证据
```

输出不包含最终 Readiness Verdict、代码实现或 JIT 文件级施工计划。

## Exit Conditions

只有同时满足以下条件，`slice-work` 才完成：

- 需求已获得合理实现覆盖与验证覆盖；
- 每项必需行为 / 验收义务都有明确责任，或有合法且显式的功能整体验证责任；
- 计划验证证据足以证明所承接义务；
- Unit 边界足够明确；
- Dependencies 与 Relevant Constraints 已显式表达到足以继续检查；
- 每个 Unit 都有可观察、可验证的 Completion Condition；
- Unit Set 可以进入 `readiness-check`。

`slice-work` 的完成只表示拆分职责完成，不表示 Readiness Gate 已通过。

## Escalation Conditions

出现以下情况时必须停止并升级或返回上游：

- 无法在不改变 Scope / Product Intent 的情况下安全拆分；
- 必须新增或选择 Major Design Decision 才能确定 Unit Boundary；
- Authoritative Sources Conflict；
- 继续拆分需要 Agent 无权自主作出的高影响、不可逆或安全 / 隐私敏感决定。

普通、低影响、可逆的 Unit 形状调整由 Agent 自主处理，不因为一般实现细节而升级给 Human。

## Context Rules

- Authority First；
- 使用 Progressive Disclosure，只加载确定 Coverage、Unit Boundary、Dependencies 与 Constraints 所需上下文；
- Conversation History 不作为权威知识；
- Planning / Requirement Candidate 不因 Roadmap 排序、预编号或名称自动成为 Execution Unit；
- Candidate Execution Unit 的 Identifier 不构成 Readiness 或 Execute 授权；
- 长期 Execution Unit Identity 不依赖易过时的精确 File Paths；
- Unit 只保留执行所需的 Durable Constraints；
- Exact File Paths、Edit Sequence、Test Commands 与 Local Implementation Details 留给 Execute 内 JIT Execution Plan；
- 不绑定 GitHub Issue、Jira、Linear、Markdown Task 或特定 Runtime Object；
- 不定义 Controller / Worker 的具体调度协议；
- 不自动调用 `readiness-check`、`execute-unit` 或接管后续生命周期。

## Allowed Sub-skills / Disciplines

- Context Discipline
- Human Escalation
