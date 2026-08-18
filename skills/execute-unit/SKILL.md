---
name: execute-unit
description: Implements and verifies exactly one ready execution unit in minimal fresh context using current repository evidence. Use when a single unit is ready to execute; discover repository-specific verification, route unexpected failures through systematic-debug, and stop after evidence supports or fails the unit completion condition.
---

# execute-unit

## Purpose

使用最小 Fresh Execution Context，实现并证明一个 Execution Unit。

本 Skill 一次只负责一个 Current Execution Unit。它不自动遍历 Feature / Queue，不自动进入 `converge`，也不承担 Merge / Push / Release / Deploy 等 Integration 行为。

完成状态必须由当前 Verification Evidence 支持，而不是由“代码已经修改”“测试看起来应该通过”或 Conversation History 中的旧结论支持。

## Use When

- 当前 Execution Unit 已通过适用的 Readiness 检查；
- Relevant Specification / Technical Plan / Governance Context 可获取；
- 可以检查 Actual Current Repository State；
- 可以在当前授权范围内实施并运行必要验证；
- 当前目标明确是一个 Unit，而不是整个 Feature。

## Do Not Use When

- 当前目标实际上是执行整个 Feature 或自动遍历多个 Units；
- Unit 仍存在 Blocking Requirement / Design / Governance Finding；
- 必须先改变 Product Intent / Scope 或 Major Technical Design 才能继续；
- 需要未授权 Shared Integration / Production / External Side Effect 才能继续；
- 当前问题是 Feature-wide 收敛判断，应使用 `converge`；
- 当前问题只是塑形或调整 Execution Units，应返回 `slice-work`；
- 当前已经出现 Unexpected Failure，需要 Root-cause Investigation 时，应进入 `systematic-debug`。

如果 Current Unit 本身过大、边界失真或无法在当前 Context 中安全完成，不通过扩大 Context 或顺手执行相邻工作来“做完”，而应返回 `slice-work`。

## Inputs

- Current Execution Unit
- Relevant Specification Sections
- Relevant Technical Plan Decisions（如存在）
- Relevant Governance / Domain Context
- Actual Current Code / Tests

Current Unit 应至少能提供：

- Identifier
- Goal
- Specification Trace / Reference
- Observable Completion Condition
- Dependencies
- Relevant Constraints

只加载执行当前 Unit 所需的最小权威上下文；不要求完整 Feature History、完整 Conversation History 或完整 Codebase。

## Authority Sources

遵循当前 Repository Authority Hierarchy，并坚持 Authority First。

执行时遵守以下规则：

1. Repository Rules 约束可执行动作、工程规则、验证要求和授权边界。
2. Current Execution Unit 定义本次执行工作边界，但不能覆盖更高层 Specification / Technical Plan / Governance Authority。
3. Relevant Specification 定义当前 Unit 必须满足的 WHAT / WHY。
4. Relevant Technical Plan（如存在）提供跨 Unit Durable Technical Constraints，不应被当前局部实现静默改写。
5. ADR / Domain Context 提供相关长期约束和事实。
6. Current Code / Tests 用于确定 Actual Current System State，但不能反向定义或覆盖 Product Requirement。
7. Conversation History 不构成权威事实来源。
8. 未经当前仓库证据确认的 Build / Test / Lint / Verification 命令不能被当作仓库事实。

如果权威来源冲突，停止当前 Unit 的相关实施并按 Escalation Conditions 处理；不要通过局部 Patch 选择一个方便实现的解释。

## Procedure

### 1. Confirm One-unit Execution Boundary

先确认当前工作只有一个 Execution Unit。

检查：

- Current Unit 的 Goal；
- Spec Reference；
- Observable Completion Condition；
- Dependencies；
- Relevant Constraints；
- 是否仍满足此前 Readiness 所依赖的关键前提。

如果当前请求实际包含多个 Units：

- 只执行被明确选定的 Current Unit；
- 如果没有唯一 Current Unit 被明确选定，停止并返回协调层或要求先选定一个 Unit，不由 `execute-unit` 自行挑选；
- 即使多个 Units 都 Ready，且用户要求“一次全做完”，也不得在同一次 Skill invocation / Fresh Execution Context 中顺序执行多个 Units；
- 一个 Unit 完成后立即停止；后续 Unit 必须由协调层重新选定，并在新的 `execute-unit` invocation / Fresh Execution Context 中执行；
- 不自动继续下一个 Unit；
- 不把 Queue Management 混入本 Skill。

如果 Unit 边界已失效、过大或必须新增未授权 Scope 才能完成，返回 `slice-work` 或相应上游职责。

### 2. Load Minimum Fresh Execution Context

建立当前 Unit 的 Fresh Execution Context，默认只加载：

- Repository Rules；
- Current Execution Unit；
- Relevant Specification Sections；
- Relevant Technical Plan Decisions；
- Relevant ADR / Domain Context；
- Relevant Current Code / Tests。

使用 Progressive Disclosure：只有当前问题需要时才继续加载额外文件、接口、测试、配置或文档。

Fresh Execution Context 是逻辑上下文边界，不要求绑定某个特定 Agent Runtime、窗口、线程或子代理机制。

不要依赖完整 Conversation History 来恢复权威事实。

### 3. Inspect Actual Repository State

在形成具体施工判断前检查当前仓库实际状态。

按需确认：

- 当前相关文件和代码结构；
- Existing Tests / Fixtures / Build Configuration；
- Repository-specific Engineering Rules；
- 已存在的实现入口与扩展点；
- 当前分支 / 工作状态中与 Unit 相关的已有变化；
- 当前可用的 Build / Test / Lint / Verification 机制。

不要因为 Technical Plan、旧 Task 或 Conversation History 中提到过某个文件、类、命令，就假设它当前仍然存在或适用。

### 4. Discover Verification Mechanisms from the Repository

从 Repository Rules 和 Actual Repository State 发现当前可用的验证方式。

可能包括但不限于：

- Existing Test Runner；
- Targeted Test Commands；
- Build / Compile；
- Lint / Static Analysis；
- Type Check；
- Integration / Contract Test；
- Repository-specific Validation Script；
- 可观察的 Manual / Runtime Evidence（在仓库和授权允许时）。

本 Skill 不硬编码任何语言、框架或工具的通用命令。

只有在仓库中实际发现、验证或由 Repository Rules 明确规定的命令，才可以作为当前 Verification Mechanism 使用。

如果无法确定必要验证方式：

- 继续检查最小相关仓库上下文；
- 不凭经验编造“应该可用”的命令；
- 如果验证缺失会阻止 Completion Claim，则当前 Unit 不能满足 Exit Condition。

### 5. Create a JIT Execution Plan if Useful

只有当前 Unit 的复杂度确实需要时，形成临时 JIT Execution Plan。

JIT Plan 可以包含：

- 当前实际相关文件；
- Concrete Edit Sequence；
- Exact Verification Commands；
- Local Implementation Details；
- 当前 Unit 内必要的短期检查顺序。

JIT Plan：

- 只服务 Current Unit；
- 不改变 Unit Goal / Specification；
- 不升级为跨 Unit Technical Plan；
- 默认随当前 Execution Context 结束；
- 不要求持久化为长期 Artifact。

如果执行中发现某个决定实际需要跨多个 Units 长期协调，则停止把它当成 JIT Detail，返回 `technical-plan`。

### 6. Establish Expected / Failing Evidence When Useful

当存在稳定的 Behavior Seam 时，在实施前建立能区分“当前未满足”和“实施后满足”的证据。

可以使用：

- Existing Failing Test；
- 新增或调整的 Targeted Test；
- 可重复的行为检查；
- 其他由仓库实际机制支持的 Failing / Expected Evidence。

TDD 是 when useful 的内嵌纪律，而不是所有 Unit 的机械要求。

普通 TDD 中预期的初始 Failing Evidence 不进入 `systematic-debug`。

如果出现的是 Unexpected Failure、环境异常、未知回归或无法解释的非预期结果，则转入 `systematic-debug`。

### 7. Implement the Minimum Current-unit Change

只实施满足 Current Unit Goal / Completion Condition 所需的最小变更。

遵守：

- 不扩大未经授权的 Product Scope；
- 不自动修复与当前 Unit 无关的相邻问题；
- 普通、低影响、可逆的 Local Implementation Choice 由 Agent 自主处理；
- 不为了局部实现便利静默改变 Specification；
- 不为了绕过实现困难静默改变 Major Technical Design；
- 不把当前 Unit 变成整个 Feature 的重构机会。

发现超出 Unit 边界但会阻塞完成的问题时，记录并返回相应职责层，而不是顺手接管。

### 8. Run Targeted Verification

实施后运行与 Current Unit Completion Condition 直接相关的当前验证。

优先：

- 最小、针对性的验证；
- 能直接覆盖当前 Required Behavior 的证据；
- 仓库规则要求的必要检查。

根据变更风险和仓库约束，再按需扩大到：

- broader regression tests；
- build / compile；
- lint / static analysis；
- integration checks；
- 其他必要验证。

不得把历史通过结果、未执行命令、旧日志或推测结果当作 Current Evidence。

### 9. Handle Unexpected Failure Systematically

如果 Targeted Verification、Build、Runtime 或其他执行步骤出现 Unexpected Failure：

- 不连续尝试随机 Patch；
- 不凭直觉宣布失败与当前 Unit 无关；
- 调用或进入 `systematic-debug` 的 Root-cause Workflow。

Debug 结果可能：

- 在当前 Unit 内形成 Minimal Root-cause Fix 后返回验证；
- 暴露 Expected Behavior 缺失并返回 `clarify-intent` / `specify`；
- 暴露 Major Design 问题并返回 `technical-plan`；
- 暴露授权 / 高影响问题并升级 Human Authority。

### 10. Review When Risk Warrants

根据变更风险决定是否执行额外 Review。

Review 逻辑上至少区分两个维度：

**Specification Compliance**

- 当前实现是否满足 Current Unit 对应的 Required Behavior；
- 是否遗漏 Boundary / Acceptance；
- 是否增加未经请求的 Product Behavior。

**Engineering Quality**

- 实现是否与当前 Architecture / Repository Rules 一致；
- 是否引入明显隐藏耦合、脆弱性或不可维护结构；
- 测试 / 验证是否与变更风险相称。

这两个维度不要求两个独立 Reviewer Agent，也不要求每个低风险 Unit 都执行重型 Review 流程。

### 11. Detect Required Stage Return or Escalation

执行中如果发现当前权威已不足以安全继续，不通过 `execute-unit` 静默修正上游事实。

典型返回：

- Requirement / Expected Behavior 不明确 → `clarify-intent` / `specify`；
- Durable Cross-unit Technical Decision 缺失或失效 → `technical-plan`；
- Unit Boundary / Dependencies 失效 → `slice-work`；
- Unexpected Failure → `systematic-debug`。

出现 Human Escalation 条件时停止未经授权的动作。

如果阶段回退改变了项目事实，应更新对应 Authoritative Artifact，而不是只在当前执行上下文中记住。

### 12. Record Current Evidence and Result State

记录当前 Unit 的结果，至少说明：

- 实施了什么与 Current Unit 直接相关的变更；
- 实际运行了哪些验证；
- 验证结果是什么；
- 当前证据是否支持 Observable Completion Condition；
- 是否存在 Stage Return / Authoritative Update Required；
- 是否存在仍未解决但不影响当前 Completion 的 Non-blocking Observation（如有）。

不要将“Implementation exists”与“Unit completed”混为一谈。

### 13. Evaluate Exit Condition

只有在当前证据支持 Current Unit 的 Observable Completion Condition 时，`execute-unit` 才完成。

如果：

- 必要验证未运行；
- 当前证据失败；
- Completion Condition 无法被现有证据判断；
- 仍有 Blocking Requirement / Design / Governance 问题；

则不得声明 Unit Complete。

完成当前 Unit 后停止。本 Skill 不自动执行下一个 Unit，也不自动进入 `converge`。

## Outputs

输出 Current Unit Execution Result，按需包含：

- Implementation
- Tests / Verification Evidence
- Result State
- Stage Return / Authoritative Update Required

建议结果语义明确区分：

- **Completed** — 当前证据支持 Unit Completion Condition；
- **Not Completed** — 当前证据不足、失败或仍有 Blocking Issue；
- **Stage Return Required** — 需要返回上游职责更新权威或重新塑形；
- **Escalation Required** — 需要 Human / Explicit Policy 才能继续。

这些是结果语义，不要求固定机器协议、YAML、JSON 或特定 Tracker 状态。

不得仅输出“代码已实现”而缺少 Current Evidence。

## Exit Conditions

当前证据支持该 Execution Unit 的 Observable Completion Condition。

具体意味着：

- Current Unit 所需实现已存在于当前系统状态；
- 必要 Targeted Verification 已实际运行；
- 当前 Verification Evidence 与 Completion Condition 一致；
- 没有尚未解决的 Blocking Requirement / Design / Governance 问题；
- 没有通过静默改变 Product Intent / Major Design 来获得“通过”。

完成一个 Unit 不等于 Feature 已 Converged，也不等于 Ready to Integrate。

## Escalation Conditions

出现以下情况时必须停止未经授权动作并升级或返回上游：

- 必须改变 Product Intent / Scope；
- 必须改变 Major Architecture Direction；
- Destructive / Hard-to-reverse Action；
- Security / Privacy Sensitive Decision；
- 未授权 Shared / Production / External Side Effect；
- Authoritative Sources Conflict；
- Agent 无权自主决定的高影响或不可逆事项。

普通、低影响、可逆的 Local Implementation Choice 由 Agent 自主处理，不升级给 Human。

## Context Rules

- Authority First；
- Progressive Disclosure；
- 默认建立最小 Fresh Execution Context；
- 不依赖完整 Conversation History；
- Current Code / Tests 表示 Current System State，但不能反向覆盖 Product Authority；
- Repository-specific Verification Commands 必须运行时从 Repository Rules / Actual State 发现，不硬编码；
- JIT Execution Plan 默认临时存在，随 Current Unit Execution Context 结束；
- 不把单 Unit Local Details 提前升级为 Durable Technical Plan；
- 一次只执行一个 Unit；
- 不自动遍历 Queue；
- 不自动调用 `converge`；
- 本 Skill 不承担 Merge / Push / Release / Deploy；Integration 由仓库 Policy / Human Authority 在本方法终点之外处理；
- Completion Claim 必须符合 Verification-before-claim。

## Allowed Sub-skills / Disciplines

- `systematic-debug`
- Verification-before-claim
- TDD（when useful）
- Code Review（risk-based discipline）
- Context Discipline
- Human Escalation