# 核心 Skill Contract Matrix

**状态：** Draft — 下一阶段待复核  
**性质：** Skill 设计输入，尚未冻结为最终实现契约

本文记录当前 8 个核心候选 Skill 的初始契约。下一阶段应先复核本矩阵，再开始正式编写 `SKILL.md`。

## 1. Contract Matrix

| Skill | 主要输入 | 主要输出 | Exit Condition | Escalation |
|---|---|---|---|---|
| `clarify-intent` | User Intent + Authority Context | Clarified Goal / Scope / Product Decisions | 不再存在阻塞 Intent 的关键歧义 | 多种解释会导致不同 User-visible Behavior |
| `specify` | Clarified Intent + Governance / Domain Context | WHAT / WHY Specification | Fresh Agent 能判断 Required Behavior 与 Completion | Requirement Conflict 或 Product Decision 未解决 |
| `technical-plan` | Specification + Architecture / Code Constraints | Durable Technical Decisions | 实施前技术不确定性已解决 | Major Architecture / Irreversible Trade-off 超出授权 |
| `slice-work` | Specification + Optional Plan | Vertical Context-fit Execution Units | Coverage、Dependency、Completion Condition 一致 | 无法在不改变 Scope / Design 的情况下安全拆分 |
| `readiness-check` | Spec + Plan + Units + Governance | PASS 或 Findings | 无 Blocking Finding | 权威冲突或高影响 Choice 未解决 |
| `execute-unit` | One Unit + Minimum Authority Context + Current Code / Tests | Implementation + Current Evidence | Completion Condition 有当前证据 | 必须改变 Product Intent 或动作超出授权 |
| `systematic-debug` | Observed Problem + Expected Behavior + Runnable Context | Root Cause + Minimal Fix + Regression Evidence | Root Cause 已处理且 Regression Pass | Expected Behavior 未定义/冲突，或修复要求重大设计变更 |
| `converge` | Specification + Plan + System State + Evidence | READY 或 GAPS | Feature 与权威 Intent 收敛 | Gap 需要 Product / Architecture Authority |

## 2. `clarify-intent`

### Purpose

只解决定义正确 Product Intent 所必需的歧义。

### Inputs

- Requested Outcome
- Relevant System / Domain Context
- Applicable Governance / Authority

### Outputs

- Goal
- In Scope / Out of Scope
- Key Observable Behaviors
- Confirmed Product Decisions
- Remaining Blocking Questions

### Must Not

- 提前设计实现细节；
- 消除所有技术不确定性；
- 生成大篇幅永久讨论记录。

### Exit

不存在会显著改变 Scope、User-visible Behavior 或 Acceptance 的未决问题。

## 3. `specify`

### Purpose

创建或更新 WHAT / WHY 权威。

### Inputs

- Clarified Intent
- Repository Governance
- Relevant Domain Authority
- Existing Specification（如修改已有行为）

### Outputs

按需包含：

- Goal
- Scope
- Observable Behaviors
- Business Rules
- Boundary / Failure Behavior
- Acceptance Criteria
- Non-functional Constraints

### Must Not

默认写入：

- Source Paths
- Classes
- Framework Details
- Persistence Choices
- Construction Steps

### Exit

Fresh Agent 可以独立判断要交付什么以及什么情况下算完成。

## 4. `technical-plan`

### Purpose

只有在必要时解决长期技术设计问题。

### Use When

Specification 无法直接、安全映射到当前 Architecture。

### Inputs

- Specification
- Relevant Architecture / ADRs
- Current Codebase State
- Technical Constraints

### Outputs

只记录跨 Unit 有长期价值的技术决策：

- Technical Approach
- Boundaries
- Data / Contracts
- Important Seams
- Migration Strategy
- Test Strategy
- Risks

### Must Not

变成长期保存的逐文件施工脚本。

### Exit

不存在阻塞实施的技术不确定性。

## 5. `slice-work`

### Purpose

将 Intent / Design 转换为适合 AI 执行的纵向工作单元。

### Inputs

- Specification
- Optional Technical Plan

### Outputs

每个 Execution Unit 至少包含：

- id
- goal
- specification trace
- completion condition
- dependencies
- relevant constraints

### Quality Properties

- vertical
- independently verifiable
- bounded
- traceable
- context-fit
- low hidden coupling

### Must Not

把易过时的 File Paths 作为长期 Unit Identity 的必填字段。

### Exit

Execution Units 对需求形成合理覆盖，可以进入 `readiness-check`。

## 6. `readiness-check`

### Purpose

在实施前提供统一 Gate，替代无差别人工 Review。

### Inputs

- Specification
- Optional Technical Plan
- Execution Units
- Governance / Context Authority

### Checks

#### Specification

- Clarity
- Boundary Completeness
- Acceptance Observability

#### Design

- Coverage of Spec
- No Silent Redefinition of Intent

#### Execution

- Requirement Coverage
- No Material Orphan Work
- Correct Dependencies
- Context-fit
- Independent Completion Conditions

#### Governance

- No Conflict with Higher Authority

### Outputs

- `PASS`
- 或按优先级整理的 Blocking / Non-blocking Findings

### Must Not

作为 Checker 时静默修改权威 Artifacts。

### Exit

不存在 Blocking Finding。

## 7. `execute-unit`

### Purpose

使用最小 Fresh Context，实现并证明一个 Execution Unit。

### Inputs

- Current Execution Unit
- Relevant Spec Sections
- Relevant Technical Plan Decisions
- Relevant Governance / Domain Context
- Actual Current Code / Tests

### Procedure Shape

1. Load Minimum Authority.
2. Inspect Current Repository State.
3. Create JIT Plan if useful.
4. Establish Expected / Failing Evidence.
5. Implement.
6. Run Targeted Verification.
7. Use Systematic Debugging on Unexpected Failure.
8. Review when risk warrants.
9. Record Current Evidence.

### Outputs

- Implementation
- Tests / Evidence
- Result State
- Required Authoritative Artifact Update（如有）

### Must Not

- 依赖完整 Conversation History；
- 自动执行整个 Feature；
- 自动进入 Shared Integration State。

### Exit

当前证据支持 Unit Completion Condition。

## 8. `systematic-debug`

### Purpose

通过定位 Root Cause 修复缺陷，而不是连续猜 Patch。

### Inputs

- Observed Symptom
- Expected Behavior / Authority
- Reproduction Environment
- Relevant Code / System State

### Procedure Shape

1. Reproduce.
2. Establish Expected vs Actual.
3. Investigate Root Cause.
4. Form Falsifiable Hypothesis.
5. Establish Failing / Reproduction Evidence.
6. Apply Minimal Root-cause Fix.
7. Run Regression Verification.

### Outputs

- Root-cause Statement
- Minimal Fix
- Regression Evidence
- Escalation if Expected Behavior is Undefined

### Exit

Root Cause 已处理且当前 Regression Evidence 通过。

## 9. `converge`

### Purpose

判断整个 Feature 是否真正符合权威 Intent。

### Inputs

- Specification
- Technical Plan（如存在）
- Execution Units / Status
- Current Implemented System
- Current Verification Evidence

### Checks

- Missing
- Partial
- Contradicting
- Unrequested Behavior
- Obsolete Plan
- Missing Verification
- Cross-unit Integration Gap

### Outputs

```text
READY
```

或：

```text
GAPS
```

并生成必要的补充/修正 Execution Work。

### Must Not

把“所有 Ticket 都 Done”当作 Feature 完成证据。

### Exit

Implementation、Intent 和 Current Evidence 已收敛。

## 10. 下一阶段待解决问题

以下问题暂不冻结：

1. `clarify-intent` 与 `specify` 是否始终保持两个独立 Skill，还是允许 Small-change Path 合并？
2. `readiness-check` 应由 User 显式调用，还是由 Workflow 自动调用？
3. 哪些 Verification 行为继续内嵌在 `execute-unit` / `converge`，哪些值得形成独立 `verify-evidence` Skill？
4. `code-review` 是否值得独立 Skill 化？
5. `handoff` 是否进入第一批实现？
6. Execution Unit 的 Reference Implementation 采用什么持久化形式？
7. Skill 如何发现 Repository-specific Build / Test Commands，而不绑定特定工具？

这些问题应在第一版稳定 Skill Release 前解决，但不影响当前方法基线。
