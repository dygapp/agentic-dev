---
name: readiness-check
description: Performs a read-only pre-execution gate across specification, optional technical plan, execution units, domain and architecture authority, artifact lifecycle responsibilities, and governance. Use immediately before execution to return PASS or evidence-backed findings; never repair authoritative artifacts inside the check.
---

# readiness-check

## Purpose

在进入执行前执行统一、只读的就绪门禁，判断当前规格说明、可选技术计划、执行单元、验收责任归属 / 计划验证覆盖、相关领域 / 架构 / ADR 权威、长期权威产物生命周期责任与治理上下文是否已经足以安全进入实施。

本 Skill 只负责发现和分类 Readiness Findings，不修改 Specification、Technical Plan、Execution Units、ADR 或其他权威 Artifact。

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
- 目标是让 Checker 自动补写或改写 Specification、Technical Plan、ADR 或 Execution Units；
- 当前工作实际上是在实施某个 Unit，而不是判断其是否 Ready。

如果在缺少必要输入的情况下被调用，应停止 Gate，并指出应返回的职责层；不得通过猜测或补写输入来制造 `PASS`。

## Inputs

- Specification
- Optional Technical Plan
- Execution Units
- Governance / Context Authority
- Relevant Domain Authority（如存在）
- Relevant Architecture / ADR Authority（如存在）

只要求当前 Gate 所需的最小权威上下文，不要求加载完整 Conversation History 或完整仓库内容。

## Authority Sources

遵循当前 Repository Authority Hierarchy。

检查时遵守以下规则：

1. Repository Instructions、Method、Architecture 与其他更高优先级 Authority 约束低优先级 Artifact。
2. Specification 定义 Product / Feature 的 WHAT / WHY；Technical Plan 与 Execution Units 不得反向改变已确认 Intent。
3. Technical Plan 只在存在时作为 Design Readiness 输入；其内容不得通过 Silent Redefinition 改写 Specification。
4. Execution Units 必须可追溯到 Specification，并遵循已确认的 Durable Technical Decisions、当前有效 Domain / Architecture / ADR Authority 与 Governance Rules。
5. Domain Authority 提供跨功能持续有效的业务事实；Architecture Context 提供当前有效架构状态；ADR 提供满足条件的重要架构决定及其理由。低层 Artifact 不得静默覆盖。
6. Conversation History 不构成权威来源。
7. `readiness-check` 没有修改更高层 Authority 以消除 Finding 的权限。

如果 Authoritative Sources 发生冲突，形成 Blocking Finding 并升级，而不是自行选择一个解释继续。

## Procedure

### 1. Confirm Checkable Inputs

确认存在可检查的 Specification 和至少一个由 `slice-work` 形成的 Candidate Execution Unit，并识别当前适用的 Domain / Architecture / Governance Authority。

“可检查”是语义要求，不等于必须存在独立文件。当前场景、Repository Authority 或其他已授权输入如果已经明确提供足以判断本 Gate 的 Specification、Candidate Execution Units 与治理事实，应直接据此检查；不得仅因隔离工作目录中没有对应 Markdown / JSON 等 Artifact 文件而把已提供的输入判定为缺失。反之，不能从文件名、编号、标签或顺序推断未被权威输入明确提供的事实。

Roadmap / Backlog / Issue 中的顺序、`EU-xx` / Unit ID、标签或“当前 / 下一项”名称不能证明这些输入存在，也不能证明 Readiness 已经通过。只有 Planning / Requirement Candidate 时，应按最早缺失职责返回 `clarify-intent` / `specify`；Specification Ready 后仍缺少 Candidate Execution Units 时才返回 `slice-work`。不得在 Gate 内根据编号补造 Specification 或 Units。

当 Gate 因预编号的 Planning / Requirement Candidate 缺少上游输入而阻止继续时，结论应显式保持完整状态边界：Specification Ready 且必要 Technical Planning 完成后，才由 `slice-work` 形成 Candidate Execution Units，并可为这些 Candidate Units 分配稳定 Identifier；随后仍必须重新进入 `readiness-check`。Identifier 本身不构成 Readiness PASS，也不授予 Execute 权限。

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
- 已识别的 Domain Authority Candidate 是否已完成 `specify` 验证和授权路由。

如果问题需要改变或补充 Product Intent，Blocking Finding 应返回 `clarify-intent` / `specify`，而不是由 Checker 决定需求。

### 3. Check Design Readiness

如果存在 Technical Plan，检查：

- 是否覆盖相关 Specification；
- 是否存在 Silent Redefinition of Intent；
- 实施前必须解决的 Durable Technical Decisions 是否已经解决；
- 是否与当前有效 Architecture / ADR Authority 一致；
- 是否仍存在会跨 Unit 影响实现的重大技术不确定性。

同时分别检查：

- 是否存在应更新 Architecture Context、但尚未进入适当 Repository Authority 的架构权威缺口；
- 是否存在满足 ADR 条件、但尚未创建、更新或取代 ADR 的决策记录缺口。

任一缺口存在时形成 Blocking Finding，并返回 `technical-plan` 完成 Architecture Authority 更新与必要 ADR 评估。

如果没有 Technical Plan，不因“没有文档”本身判定失败。只有当输入表明实施前仍存在必须持久协调的技术决定、未处理的 Architecture Context 变化或满足条件的 ADR 时，才形成 Blocking Finding 并返回 `technical-plan`。

### 4. Check Execution Readiness

检查 Execution Unit Set：

- 每个 Unit 当前是否仍明确处于 Candidate 状态，且没有把 Identifier、Roadmap 顺序或历史命名当作 Readiness / Execute 授权；
- 需求是否同时获得合理实现覆盖与验证覆盖；
- 每项必需行为 / 验收义务是否有明确的实现责任 / 验证责任，或有真实跨执行单元原因支持的显式功能整体验证责任；
- 计划验证证据是否足以区分所承接义务是否满足，而不是只写“代码完成”“测试通过”或覆盖主路径；
- 分页、排序、边界 / 失败、多状态、跨入口等关键差异是否具有与规格说明风险相称的验证场景；
- 是否存在重要孤立工作项或未归属的验证义务；
- 每个 Unit 是否具有明确 Goal 与 Specification Trace / Reference；
- Completion Condition 是否可观察、可验证；
- Dependencies 是否真实、顺序合理且没有隐藏前置条件；
- Unit 是否 Bounded、Context-fit，并适合 Fresh Agent 独立执行；
- Unit 是否包含超出 Specification Scope 的未授权工作；
- Unit 是否遵守当前有效 Architecture / ADR Constraints。

需要重新塑形、补充或拆分执行单元，补齐验收责任归属，或增强计划验证覆盖时，阻塞性发现返回 `slice-work`。检查者不替执行单元选择测试框架、固定证据格式，也不自行补写责任归属映射。

### 5. Check Governance Readiness

检查当前工作是否违反：

- Repository Instructions；
- 当前有效 Domain Authority；
- Engineering / Governance Rules；
- 当前有效 Architecture Context / ADR；
- Authority、Impact、Reversibility 相关的 Human Escalation Boundary。

如果继续执行需要未授权的高影响、不可逆、安全 / 隐私敏感或重大架构决策，形成 Blocking Finding 并升级到相应 Human / Repository Authority。

如果当前工作已经要求创建或重大更新长期权威产物，但无法确定 Producer、Trigger、Consumer、Persistence、Update、Supersede 或 Escalation 责任，形成 Artifact Lifecycle Gap，阻止 `PASS` 并返回拥有相应事实或决定的职责层。

如果问题不是授权冲突，而是需要形成新的长期领域事实，返回 `clarify-intent` / `specify`；需要更新 Architecture Context 或形成新的长期架构决定时，返回 `technical-plan`。本 Skill 不决定或持久化这些权威。

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

不存在阻塞性发现，包括未归属的验收责任 / 验证责任、无法证明所承接义务的计划验证覆盖、未处理的领域 / 架构权威或产物生命周期缺口，并且 `PASS` 有当前权威输入支持。

如果存在 Blocking Finding，本 Skill 应输出 Findings 并停止继续进入 Execute；这表示 Readiness Gate **未满足 Exit Condition**，当前 Workflow 应返回相应职责层处理。

## Escalation Conditions

出现以下情况时必须升级：

- Authoritative Sources Conflict；
- 高影响 Choice 无法由 Agent 在授权范围内自主裁决；
- 通过 Gate 必须改变 Product Intent；
- 通过 Gate 必须选择或改变 Major Architecture Direction；
- 继续执行需要未授权的 Shared / Production / External Side Effect；
- 涉及 Destructive / Hard-to-reverse、Security 或 Privacy Sensitive Decision。

普通、低影响、可逆且可由现有权威或证据判断的问题，不升级给 Human。需要新的长期架构决定但尚未触发 Human Escalation 时，返回 `technical-plan`，而不是把“需要 ADR”本身等同于必须人工批准。

## Context Rules

- Authority First；
- 使用 Progressive Disclosure，只加载四维 Gate 判断所需上下文；
- Conversation History 不作为权威知识；
- Candidate Execution Unit 可以已有 Identifier，但 Identifier 本身不参与 PASS 推断；
- Planning / Requirement Candidate 不因预编号进入本 Gate 的可检查 Unit Set；
- 不默认加载完整 Codebase；只有当前 Authority / Design 判断确实需要时才读取相关上下文；
- Findings 必须基于当前输入和当前权威证据，不能依据未经验证的假设；
- 只检查当前工作已经暴露的生命周期责任，不为了形式完整性要求每个阶段创建 Artifact；
- User 不必显式调用，Controller / Workflow Runtime 可以自动发起；
- 保持独立 Skill Contract，不与 `slice-work` 或 `execute-unit` 合并；
- Gate 结束后不自动推进完整生命周期。

## Allowed Sub-skills / Disciplines

- Context Discipline
- Verification-before-claim（仅用于 Gate 结论的证据要求）
- Human Escalation
