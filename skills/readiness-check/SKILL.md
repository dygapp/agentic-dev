# readiness-check

## Purpose

在进入 Execute 前执行统一、只读的 Readiness Gate，判断当前 Specification、可选 Technical Plan、Execution Units 与 Governance Context 是否已经足以安全进入实施。

本 Skill 只负责发现和分类 Readiness Findings，不修改 Specification、Technical Plan、Execution Units 或其他权威 Artifact。

## Use When

- `slice-work` 已形成一个或多个 Execution Units；
- Specification 已存在并可用于判断 Scope、Behavior 与 Acceptance；
- Technical Plan 如有必要，已经形成并可检查；
- 当前工作即将进入 Execute，需要统一判断是否存在 Blocking Finding；
- Controller / Workflow Runtime 需要自动执行 Execute 前 Gate。

对小型安全修改，可以轻量执行同一 Gate 语义，不要求 Human 显式调用本 Skill。

## Do Not Use When

- 当前仍处于 Intent Clarification；
- 尚没有可检查的 Specification；
- 尚没有可检查的 Execution Unit；
- 目标是让 Checker 自动补写或改写 Specification、Technical Plan 或 Execution Units；
- 当前工作实际上是在实施某个 Unit，而不是判断其是否 Ready。

如果在缺少必要输入的情况下被调用，应停止 Gate，并指出应返回的职责层；不得通过猜测或补写输入来制造 `PASS`。

## Inputs

- Specification
- Optional Technical Plan
- Execution Units
- Governance / Context Authority

只要求当前 Gate 所需的最小权威上下文，不要求加载完整 Conversation History 或完整仓库内容。

## Authority Sources

遵循当前 Repository Authority Hierarchy。

检查时遵守以下规则：

1. Repository Instructions、Method、Architecture 与其他更高优先级 Authority 约束低优先级 Artifact。
2. Specification 定义 Product / Feature 的 WHAT / WHY；Technical Plan 与 Execution Units 不得反向改变已确认 Intent。
3. Technical Plan 只在存在时作为 Design Readiness 输入；其内容不得通过 Silent Redefinition 改写 Specification。
4. Execution Units 必须可追溯到 Specification，并遵守已确认的 Durable Technical Decisions 与 Governance Rules。
5. Conversation History 不构成权威来源。
6. `readiness-check` 没有修改更高层 Authority 以消除 Finding 的权限。

如果 Authoritative Sources 发生冲突，形成 Blocking Finding 并升级，而不是自行选择一个解释继续。

## Procedure

### 1. Confirm Checkable Inputs

确认存在可检查的 Specification 和至少一个 Execution Unit，并识别当前适用的 Governance / Context Authority。

如果缺失：

- Specification 缺失或尚不可判定时，返回 `specify` 或必要时 `clarify-intent`；
- Execution Units 缺失时，返回 `slice-work`；
- 必要 Authority 无法确定或互相冲突时，形成 Blocking Finding 并升级。

不得在本 Skill 内补写这些 Artifact。

### 2. Check Specification Readiness

检查：

- Goal / Scope 是否足够清楚；
- 是否仍存在会 materially affect Product Intent / Acceptance 的阻塞歧义；
- Boundary / Failure Behavior 是否足以支持执行判断；
- Acceptance Criteria 是否可观察、可验证；
- Unit 所依赖的 Required Behavior 是否存在权威定义。

如果问题需要改变或补充 Product Intent，Blocking Finding 应返回 `clarify-intent` / `specify`，而不是由 Checker 决定需求。

### 3. Check Design Readiness

如果存在 Technical Plan，检查：

- 是否覆盖相关 Specification；
- 是否存在 Silent Redefinition of Intent；
- 实施前必须解决的 Durable Technical Decisions 是否已经解决；
- 是否仍存在会跨 Unit 影响实现的重大技术不确定性。

如果没有 Technical Plan，不因“没有文档”本身判定失败。只有当输入表明实施前仍存在必须持久协调的技术决定时，才形成 Blocking Finding 并返回 `technical-plan`。

### 4. Check Execution Readiness

检查 Execution Unit Set：

- Requirements 是否获得合理 Execution Coverage；
- 是否存在重要 Orphan Work；
- 每个 Unit 是否具有明确 Goal 与 Specification Trace / Reference；
- Completion Condition 是否可观察、可验证；
- Dependencies 是否真实、顺序合理且没有隐藏前置条件；
- Unit 是否 Bounded、Context-fit，并适合 Fresh Agent 独立执行；
- Unit 是否包含超出 Specification Scope 的未授权工作。

需要重新塑形、补充或拆分 Unit 时，Blocking Finding 返回 `slice-work`。

### 5. Check Governance Readiness

检查当前工作是否违反：

- Repository Instructions；
- Engineering / Governance Rules；
- 已确认 Architecture Decisions；
- Authority、Impact、Reversibility 相关的 Human Escalation Boundary。

如果继续执行需要未授权的高影响、不可逆、安全 / 隐私敏感或重大架构决策，形成 Blocking Finding 并升级到相应 Human / Repository Authority。

### 6. Classify Findings

将所有 Finding 分为：

- **Blocking**：当前问题使安全进入 Execute 的必要条件不成立；
- **Non-blocking**：值得记录，但不影响当前工作安全进入 Execute。

不要因为一般优化建议、风格偏好或普通低影响可逆实现细节而制造 Blocking Finding。

每个 Blocking Finding 至少说明：

- Dimension：Specification / Design / Execution / Governance；
- Finding：具体阻塞事实；
- Evidence：支持该判断的当前输入或权威依据；
- Return To：应返回处理的职责层；
- Escalation：是否需要 Human / Explicit Policy 介入。

### 7. Produce Gate Result

如果不存在 Blocking Finding，输出：

```text
PASS
```

如存在 Non-blocking Findings，可以在 `PASS` 后列出；它们不得改变 Gate Verdict。

如果存在 Blocking Finding，不输出 `PASS`。按优先级列出 Blocking Findings，并可附 Non-blocking Findings；当前 Workflow 应返回 Finding 指定的职责层。

`readiness-check` 不自动调用 `execute-unit`，也不自行修复 Finding。

## Outputs

### No Blocking Finding

```text
PASS

Non-blocking Findings:  # optional
- ...
```

### Blocking Findings Exist

```text
Blocking Findings:
1. Dimension: <Specification | Design | Execution | Governance>
   Finding: <blocking fact>
   Evidence: <current authoritative evidence>
   Return To: <responsibility layer>
   Escalation: <none | Human / Explicit Policy>

Non-blocking Findings:  # optional
- ...
```

输出只描述 Gate 结论与 Finding，不包含对权威 Artifact 的静默改写。

## Exit Conditions

不存在 Blocking Finding，并且 `PASS` 有当前权威输入支持。

如果存在 Blocking Finding，本 Skill 应输出 Findings 并停止继续进入 Execute；这表示 Readiness Gate **未满足 Exit Condition**，当前 Workflow 应返回相应职责层处理。

## Escalation Conditions

出现以下情况时必须升级：

- Authoritative Sources Conflict；
- 高影响 Choice 无法由 Agent 在授权范围内自主裁决；
- 通过 Gate 必须改变 Product Intent；
- 通过 Gate 必须选择或改变 Major Architecture Direction；
- 继续执行需要未授权的 Shared / Production / External Side Effect；
- 涉及 Destructive / Hard-to-reverse、Security 或 Privacy Sensitive Decision。

普通、低影响、可逆且可由现有权威或证据判断的问题，不升级给 Human。

## Context Rules

- Authority First；
- 使用 Progressive Disclosure，只加载四维 Gate 判断所需上下文；
- Conversation History 不作为权威知识；
- 不默认加载完整 Codebase；只有当前 Authority / Design 判断确实需要时才读取相关上下文；
- Findings 必须基于当前输入和当前权威证据，不能依据未经验证的假设；
- User 不必显式调用，Controller / Workflow Runtime 可以自动发起；
- 保持独立 Skill Contract，不与 `slice-work` 或 `execute-unit` 合并；
- Gate 结束后不自动推进完整生命周期。

## Allowed Sub-skills / Disciplines

- Context Discipline
- Verification-before-claim（仅用于 Gate 结论的证据要求）
- Human Escalation
