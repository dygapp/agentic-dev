# 核心 Skill Contract Matrix

**状态：** Reviewed Baseline v0.1  
**性质：** 第一批核心 Skill 的实现契约基线

本文记录第一批 8 个核心 Skill 的已复核契约。Skill 实现必须遵循本文，同时继续受 `AGENTS.md`、`docs/method/ai-development-method.md` 与 `docs/architecture/skill-architecture.md` 的更高优先级约束。

## 1. Contract Review 结论

当前 8 个核心 Skill 可以进入第一批设计与后续实现，不存在必须先修改方法基线才能解决的职责断层。

复核后确认以下边界：

1. `clarify-intent` 与 `specify` 保持独立 Skill。前者解决 Product Intent 层关键歧义，后者负责形成或更新 WHAT / WHY 权威。小型安全修改可以采用轻量路径，但不合并两者的语义职责。
2. `technical-plan` 处理跨 Execution Unit 有持续协调价值的长期技术决定，并对其中形成的长期技术决策执行 ADR 评估；只有跨功能形成长期架构权威的决定才按条件形成或更新 ADR。Execute 内的 JIT Execution Plan 只服务当前 Unit，默认不持久化。
3. `slice-work` 负责生成和塑形 Execution Units；`readiness-check` 是独立 Gate，只检查跨 Artifact 一致性与阻塞项，不静默修改权威 Artifact。
4. `execute-unit` 只执行并证明一个 Execution Unit，不自动执行整个 Feature，也不自动进入 `converge` 或 Integration。
5. `systematic-debug` 是 Defect / Unexpected Failure 的调查路径，可以由 `execute-unit` 调用，也可以独立用于缺陷工作；它不替代普通 TDD 的预期失败步骤。
6. `converge` 负责 Feature-wide 收敛检查。发现 Gap 时描述缺口并触发必要的重新切分或阶段回退，不通过静默修改 Specification / Technical Plan / ADR 来“修平”差异。
7. Verification-before-claim、Code Review、TDD、Context Discipline 和 Human Escalation 暂继续作为内嵌纪律，不进入第一批独立 Skill。
8. `handoff` 暂不进入第一批核心 Skill。它属于 Transition Skill，后续在核心 Feature / Defect 路径稳定后再评估。

## 2. Contract Matrix

| Skill | 主要输入 | 主要输出 | Exit Condition | Escalation |
|---|---|---|---|---|
| `clarify-intent` | User Intent + Authority Context | Clarified Goal / Scope / Product Decisions | 不再存在阻塞 Intent 的关键歧义 | 多种解释会导致 materially different User-visible Behavior，或 Scope / Intent 需要改变 |
| `specify` | Clarified Intent + Governance / Domain Context + Existing Specification（如有） | WHAT / WHY Specification | Fresh Agent 能判断 Required Behavior、Boundary 与 Completion | Requirement / Authority Conflict 或 Product Decision 未解决 |
| `technical-plan` | Specification + Architecture / ADR / Code Constraints | Durable Technical Decisions + 条件性 ADR / Architecture Authority Update，或确认无需长期 Technical Plan | 技术不确定性已解决，且需要形成或更新的长期架构决定已进入适当 Repository Authority | Major Architecture、Destructive / Irreversible Trade-off 或未授权 External Effect |
| `slice-work` | Specification + Optional Technical Plan | Vertical Context-fit Execution Units | Requirements 获得合理 Execution Coverage，Units 可进入 Readiness Gate | 无法在不改变 Scope / Intent / Required Design 的情况下安全拆分 |
| `readiness-check` | Spec + Optional Plan + Units + Governance | `PASS` 或 Blocking / Non-blocking Findings | 无 Blocking Finding | Authoritative Sources Conflict 或高影响 Choice 无权自主裁决 |
| `execute-unit` | One Unit + Minimum Authority Context + Current Code / Tests | Implementation + Current Evidence + Result State | Completion Condition 有当前证据支持 | 必须改变 Product Intent / Major Design，或动作超出授权 / 不可逆 / 安全隐私敏感 |
| `systematic-debug` | Observed Problem + Expected Behavior + Runnable Context | Root Cause + Minimal Fix + Regression Evidence | Root Cause 已处理且 Regression Evidence 通过 | Expected Behavior 未定义/冲突，或修复要求重大设计变更 |
| `converge` | Specification + Optional Plan + Units + System State + Evidence | `READY` 或 `GAPS` | Feature 与权威 Intent、Architecture / ADR Authority 和 Current Evidence 收敛 | Gap 需要 Product / Architecture Authority，或权威来源冲突 |

## 3. `clarify-intent`

### Purpose

只解决定义正确 Product Intent 所必需的关键歧义。

### Use When

- 新 Feature / Change 仍存在可能显著改变 Goal、Scope、User-visible Behavior、Business Boundary、Acceptance Result 或重大非功能义务的问题；
- Existing Intent 需要重新确认；
- Execute / Debug / Converge 发现上游 Product Intent 不明确并发生阶段回退。

### Do Not Use When

- 仅剩普通、低影响、可逆的实现细节；
- 问题已经属于纯技术设计选择；
- Intent 已足够明确，只需要结构化为 Specification。

### Inputs

- Requested Outcome
- Relevant System / Domain Context
- Applicable Governance / Authority
- Known Scope

### Authority Sources

遵循 Repository Authority Hierarchy。只加载解决当前 Intent 歧义所需的最小权威上下文，不把 Conversation History 当作权威事实。

### Procedure

1. 提取 Goal、Known Scope 与当前已确认约束。
2. 识别只会 materially affect Product Intent / Acceptance 的未决问题。
3. 对普通、低影响、可逆的实现不确定性不升级。
4. 对需要 Human Authority 的高影响歧义提出最小必要问题。
5. 收敛已确认 Product Decisions，并区分仍阻塞的问题。

### Outputs

- Goal
- In Scope / Out of Scope
- Key Observable Behaviors
- Confirmed Product Decisions
- Remaining Blocking Questions（如有）

### Exit Conditions

不存在会显著改变 Goal、Scope、Product Behavior 或 Acceptance Result 的关键未决问题。

### Escalation Conditions

- 多种合理解释会产生 materially different User-visible Behavior；
- Scope / Intent 需要改变；
- Authoritative Sources Conflict；
- 决策属于 Agent 未获授权的高影响事项。

### Context Rules

- Authority First；
- Progressive Disclosure；
- 不依赖完整 Conversation History；
- 不生成大篇幅永久讨论记录。

### Allowed Sub-skills / Disciplines

- Context Discipline
- Human Escalation

## 4. `specify`

### Purpose

创建或更新 WHAT / WHY 权威，让 Fresh Agent 能独立理解 Required Behavior 与 Completion。

### Use When

- Intent 已足够明确，需要形成 Feature Specification；
- Existing Specification 需要因已确认 Product Decision 更新；
- 阶段回退要求修正 WHAT / WHY 权威。

### Do Not Use When

- 仍存在阻塞 Product Intent 的关键歧义；
- 工作主要是跨 Unit 的技术映射问题；
- 只需要当前 Unit 的临时施工计划。

### Inputs

- Clarified Intent
- Repository Governance
- Relevant Domain Authority
- Existing Authoritative Behavior
- Existing Specification（如修改已有行为）

### Authority Sources

遵循 Repository Authority Hierarchy。Specification 只能固化已确认的 Product / Domain / Governance 事实，不通过实现细节反向发明需求。

### Procedure

1. 确认 Goal 与 Scope。
2. 组织 Observable Behaviors 与 Business Rules。
3. 补齐 Boundary / Failure Behavior。
4. 定义可观察、可验证的 Acceptance Criteria。
5. 记录 Relevant Non-functional Constraints。
6. 排除默认不属于 Specification 的 HOW 细节。
7. 进行 Fresh-Agent Spec Ready 自检。

### Outputs

按需包含：

- Goal
- Scope
- Observable Behaviors
- Business Rules
- Boundary / Failure Behavior
- Acceptance Criteria
- Relevant Non-functional Constraints

### Exit Conditions

Fresh Agent 只读取 Specification 与最小必要 Repository Context，就能判断：

1. 要做什么；
2. 不做什么；
3. 什么情况下算完成；
4. 是否仍存在关键歧义。

### Escalation Conditions

- Requirement / Authority Conflict；
- Product Decision 未解决；
- Specification 需要 materially change 已确认 Scope / Intent。

### Context Rules

- WHAT / WHY 优先；
- 默认不写 Source Paths、Classes、Framework Details、Persistence Choices 或逐步施工指令；
- Conversation History 不作为权威输入。

### Allowed Sub-skills / Disciplines

- Context Discipline
- Human Escalation

## 5. `technical-plan`

### Purpose

在 Specification 无法直接、安全映射到当前技术系统时，解决跨 Execution Unit 有持续协调价值的长期 HOW 决策，并判断其中形成的长期技术决策（Durable Technical Decision）是否需要进入 ADR / Architecture Authority。

### Use When

典型触发包括：

- Cross-module Behavior
- New Data / Persistence Model
- New External Integration
- Migration
- Shared / Public Contract Change
- Deployment Topology Change
- Significant Architecture Trade-off

如果 Execute、Systematic Debugging 或 Converge 暴露新的长期架构决策，也应返回 `technical-plan` 完成相应 ADR 评估。

### Do Not Use When

- Specification 可以直接、安全映射到实现；
- 只需要当前 Execution Unit 的文件级操作顺序或测试命令；
- 技术选择属于普通、低影响、可逆的局部实现细节。

### Inputs

- Specification
- Current Architecture
- Relevant ADRs
- Current Codebase State
- Technical Constraints

### Authority Sources

Specification 定义 WHAT / WHY，Architecture / ADR / Current Codebase 提供技术约束。Technical Plan 不得静默重定义 Product Intent，也不得静默覆盖当前有效 ADR。

### Procedure

1. 判断是否存在必须跨 Unit 持久协调的技术不确定性。
2. 若不存在，不创建为创建而创建的长期 Plan，并返回 Slice & Ready。
3. 若存在，识别 Technical Approach、Boundaries、Data / Contracts、Important Seams 等必要决定。
4. 评估 Migration、Testing Strategy、Risks / Constraints。
5. 检查是否擅自改变 Specification 或违反当前有效 Architecture / ADR Authority。
6. 对已经形成的长期技术决策执行 ADR 评估：判断其是否需要跨功能长期约束后续工作，以及保留选择理由、主要权衡或替代关系是否具有持续价值。
7. 需要 ADR 时，判断创建、更新或取代关系，并保留必要的 Context、Decision、Alternatives / Trade-offs、Consequences 与 Superseded / Replaced 关系；不强制固定 `adr/` 目录、文件名或模板。
8. 对超出授权的重大架构方向（Major Architecture Direction）、高影响难逆权衡或其他未授权 External Effect 升级。
9. 检查最终 Technical Plan 与 ADR / Architecture Authority 是否一致，并确认不存在未处理的架构权威缺口。

### Outputs

只记录当前功能跨 Unit 有持续价值的技术决策：

- Technical Approach
- Component Boundaries
- Data / Contract Design
- Important Seams
- Migration Strategy
- Testing Strategy
- Risks / Constraints

若某项决定满足 ADR 条件，附加形成或更新相应 ADR / Architecture Authority；若不满足，则继续留在 Technical Plan，不为了形式完整性制造 ADR。

若无需长期 Technical Plan，则明确返回“不需要 Technical Planning”，不制造持久 Artifact 或 ADR。

### Exit Conditions

实施前必须解决的技术不确定性已经解决，且未改变 Specification Intent；需要形成或更新的长期架构决定已经进入适当 Repository Authority，不存在未处理的 ADR / Architecture Authority Gap。

### Escalation Conditions

- 重大架构方向（Major Architecture Direction）；
- Destructive / Hard-to-reverse Data Operation；
- Security / Privacy Sensitive Decision；
- 未授权 Shared / Production / External Side Effect；
- Agent 无权自主决定的高影响或不可逆权衡；
- 必须改变 Product Intent 才能继续。

### Context Rules

- 允许读取 Relevant Architecture / ADR / Current Code；
- Technical Plan 只持久化当前功能跨 Unit 的 Durable Decisions；
- 跨功能、需要长期约束后续工作的架构决定按条件进入 ADR / Architecture Authority；
- 文件级施工步骤、Exact Test Commands 和 Local Implementation Details 留给 JIT Execution Plan；
- 不强制固定 Technical Plan 文件、ADR 目录或统一模板。

### Allowed Sub-skills / Disciplines

- Context Discipline
- Human Escalation
- Design Quality

## 6. `slice-work`

### Purpose

将 Specification 与可选 Technical Plan 转换为适合 Fresh Agent 独立执行和验证的纵向 Execution Units。

### Use When

- Specification 已 Ready；
- Optional Technical Plan 已完成或确认不需要；
- 需要把 Feature 工作组织为一个或多个可执行单元；
- Converge 发现 Gap，需要形成新的或修正后的 Execution Work。

### Do Not Use When

- Product Intent 仍有阻塞歧义；
- 必要 Technical Planning 尚未完成；
- 当前只是单 Unit 内的临时 JIT 施工计划。

### Inputs

- Specification
- Optional Technical Plan

### Authority Sources

Specification 决定需求覆盖范围；Technical Plan（如存在）提供跨 Unit 技术约束。Execution Unit 不得新增未被授权的 Product Scope。

### Procedure

1. 建立 Specification Coverage 视图。
2. 按 Observable Behavior / Verifiable Outcome 优先形成 Vertical Units。
3. 为每个 Unit 定义 Goal、Spec Trace、Completion Condition、Dependencies、Constraints。
4. 检查 Bounded、Context-fit、Independent Verification 与 Hidden Dependency。
5. 调整过大、横向分层或高度耦合的 Unit。
6. 形成可交给 Readiness Gate 的完整 Unit Set。

### Outputs

每个 Execution Unit 至少包含：

```text
id
goal
spec_reference
completion_condition
dependencies
constraints
```

### Exit Conditions

- Requirements 获得合理 Execution Coverage；
- Unit 边界、依赖与 Completion Condition 足够明确；
- Unit Set 可以进入 `readiness-check`。

### Escalation Conditions

- 无法在不改变 Scope / Intent 的情况下安全拆分；
- 必须新增 Major Design Decision 才能确定 Unit Boundary；
- 权威来源之间存在冲突。

### Context Rules

- 长期 Unit Identity 不依赖易过时的精确 File Paths；
- 只保留执行所需的 Durable Constraints；
- 不把 JIT 文件级操作计划提前固化到 Unit。

### Allowed Sub-skills / Disciplines

- Context Discipline
- Human Escalation

## 7. `readiness-check`

### Purpose

在实施前提供统一 Gate，检查 Specification、Design、Execution Units 与 Governance 是否可以安全进入 Execute。

### Use When

- Slice & Ready 已形成一个或多个 Execution Units；
- Technical Plan 存在时已经形成；
- Execute 前需要统一判断 Blocking Findings。

对小型安全修改，可以由 Controller / Runtime 轻量执行同一 Gate 语义，不要求用户显式手工调用。

### Do Not Use When

- 仍处于 Intent Clarification；
- 还没有可检查的 Specification / Unit；
- 期望 Checker 直接修改权威 Artifact。

### Inputs

- Specification
- Optional Technical Plan
- Execution Units
- Governance / Context Authority

### Authority Sources

按 Repository Authority Hierarchy 检查冲突。Checker 不拥有修改更高层权威以消除 Finding 的权限。

### Procedure

1. 检查 Specification Readiness：Clarity、Boundary、Acceptance Observability。
2. 检查 Design Readiness：覆盖 Specification，无 Silent Redefinition；Technical Planning 产生或更新 ADR 时，相关 Units 必须遵守当前有效的架构约束。
3. 检查 Execution Readiness：Coverage、Orphan Work、Dependencies、Context-fit、Completion Conditions。
4. 检查 Governance Readiness：不违反 Repository Instructions、Engineering Rules、Architecture Decisions / ADR；存在未解决的 ADR / Architecture Authority Gap 时判为 Blocking。
5. 将 Findings 区分为 Blocking / Non-blocking。
6. 若无 Blocking Finding，输出 `PASS`。

### Outputs

- `PASS`
- 或按优先级组织的 Blocking / Non-blocking Findings

每个 Blocking Finding 应指出应回到哪个职责层处理，但不由 `readiness-check` 静默修复权威 Artifact。

### Exit Conditions

不存在 Blocking Finding。

### Escalation Conditions

- Authoritative Sources Conflict；
- 高影响 Choice 无法由 Agent 在授权范围内自主裁决；
- 需要改变 Product Intent / Major Architecture 才能通过 Gate。

### Context Rules

- 尽量由 AI 自动完成；
- User 不必显式调用，Controller / Workflow Runtime 可以自动发起；
- 仍保持独立 Skill Contract，不与 `slice-work` 合并。

### Allowed Sub-skills / Disciplines

- Context Discipline
- Verification-before-claim（仅用于 Gate 结论的证据要求）
- Human Escalation

## 8. `execute-unit`

### Purpose

使用最小 Fresh Execution Context，实现并证明一个 Execution Unit。

### Use When

- 当前 Unit 已满足 Readiness；
- 必要 Specification / Technical Plan / Governance Context 可获取；
- 可以检查 Actual Current Repository State 并运行必要验证。

### Do Not Use When

- 当前目标实际上是整个 Feature；
- Unit 仍有阻塞性 Requirement / Design 问题；
- 需要未授权 Shared Integration / Production Side Effect 才能继续。

### Inputs

- Current Execution Unit
- Relevant Specification Sections
- Relevant Technical Plan Decisions
- Relevant Governance / Domain Context
- Actual Current Code / Tests

### Authority Sources

按 Repository Authority Hierarchy 加载最小必要权威。实际代码与测试用于确定 Current System State，但不能反向覆盖更高层 Product Authority。

### Procedure

1. Load Minimum Authoritative Context。
2. Inspect Actual Repository State。
3. 从 Repository Rules 与实际仓库状态发现可用 Build / Test / Lint / Verification 方式；不硬编码通用命令，不把未经验证的命令当作事实。
4. Create JIT Execution Plan if useful。
5. Establish Expected / Failing Evidence when there is a stable behavior seam。
6. Implement 当前 Unit 所需最小变更。
7. Run Targeted Verification。
8. 对 Unexpected Failure 调用 `systematic-debug`。
9. 如果实施暴露新的跨功能长期架构决策，不在代码或局部 JIT Plan 中静默固化；返回 `technical-plan` 完成 ADR 评估。
10. Review when risk warrants，并逻辑区分 Specification Compliance 与 Engineering Quality。
11. Record Current Evidence。

### Outputs

- Implementation
- Tests / Verification Evidence
- Result State
- Stage Return / Authoritative Update Required（如执行发现上游事实或长期 Architecture / ADR Authority 必须改变）

`execute-unit` 不通过静默修改 Product Intent、Major Technical Design 或 ADR 来让当前实现“通过”。

### Exit Conditions

当前证据支持该 Unit 的 Observable Completion Condition。

### Escalation Conditions

- 必须改变 Product Intent / Scope；
- 必须改变 Major Architecture Direction；
- Destructive / Hard-to-reverse Action；
- Security / Privacy Sensitive Decision；
- 未授权 Shared / Production / External Side Effect；
- 权威来源冲突。

普通、低影响、可逆的 Local Implementation Choice 由 Agent 自主处理。

### Context Rules

默认只加载：

- Repository Rules
- Current Execution Unit
- Relevant Specification Sections
- Relevant Technical Plan Decisions
- Relevant ADR / Domain Context
- Relevant Current Code / Tests

不依赖完整 Conversation History。JIT Execution Plan 默认随当前 Execution Context 结束。

### Allowed Sub-skills / Disciplines

- `systematic-debug`
- Verification-before-claim
- TDD（when useful）
- Code Review（risk-based discipline）
- Context Discipline
- Human Escalation

## 9. `systematic-debug`

### Purpose

对 Observed Defect 或 Unexpected Failure 进行可证伪的 Root-cause Investigation，并实施最小 Root-cause Fix。

### Use When

- 已存在可观察 Symptom / Failure；
- `execute-unit` 遇到 Unexpected Failure；
- 独立 Defect Workflow 需要 Reproduce → Diagnose → Fix → Regression。

### Do Not Use When

- 只是 TDD 中预期的初始 Failing Evidence；
- Expected Behavior 尚未定义，应该先回到 Clarify / Specification；
- 已知需要 Major Architecture 重新设计，应该进入 Technical Planning。

### Inputs

- Observed Symptom
- Expected Behavior / Authority
- Reproduction Environment
- Relevant Code / System State

### Authority Sources

Expected Behavior 必须来自 Applicable Authority；Current Code / Runtime Evidence 用于解释 Actual Behavior，不能自行定义 Expected Behavior。

### Procedure

1. Reproduce。
2. Establish Expected vs Actual。
3. Investigate Root Cause。
4. Form Falsifiable Hypothesis。
5. Establish Failing / Reproduction Evidence。
6. Apply Minimal Root-cause Fix。
7. Run Regression Verification。
8. 如果 Root Cause 暴露新的跨功能长期架构决策，返回 `technical-plan` 完成 ADR 评估，不在 Debug 中静默建立长期 Architecture Authority。
9. Review if warranted。

### Outputs

- Root-cause Statement
- Minimal Fix
- Regression Evidence
- Required Stage Return / Escalation（如 Expected Behavior、Design 或长期 Architecture / ADR Authority 不再有效）

### Exit Conditions

Root Cause 已处理，且当前 Regression Evidence 通过。

### Escalation Conditions

- Expected Behavior 未定义或与权威冲突；
- 修复要求 materially change Product Intent；
- 修复要求 Major Architecture Direction；
- 需要未授权或不可逆 External / Data Action。

### Context Rules

- 优先最小 Reproduction Context；
- 不通过连续猜 Patch 替代 Root Cause；
- Regression Evidence 必须是当前状态证据。

### Allowed Sub-skills / Disciplines

- Verification-before-claim
- Code Review（risk-based discipline）
- Context Discipline
- Human Escalation

## 10. `converge`

### Purpose

从 Feature-wide 视角判断 Current System 是否真正符合权威 Specification 与当前有效 Architecture / ADR Authority，并形成 `READY` 或 `GAPS`。

### Use When

- 相关 Execution Units 已完成或达到可收敛检查的状态；
- 需要确认整个 Feature，而不是单个 Unit；
- 需要在 Ready to Integrate 前进行 Feature-wide Review / Full Verification。

### Do Not Use When

- 只是验证单个 Execution Unit；
- 当前仍存在明显未执行的必要 Unit；
- 期望用“所有 Ticket Done”替代 Feature Evidence。

### Inputs

- Specification
- Technical Plan（如存在）
- Relevant Architecture / ADR Authority
- Execution Units / Status
- Current Implemented System
- Current Verification Evidence

### Authority Sources

Specification 是 Feature Intent 的主要权威；Technical Plan 不能覆盖 Product Intent，且实现不得违反当前有效 Architecture / ADR Authority。Current System / Evidence 只用于判断是否收敛。

### Procedure

1. 检查 Missing Behavior。
2. 检查 Partial Implementation。
3. 检查 Contradiction with Specification。
4. 检查 Unrequested Behavior。
5. 检查 Obsolete Technical Plan。
6. 检查 Unverified Critical Behavior。
7. 检查 Cross-unit Integration Gap。
8. 检查 Architecture / ADR Gap，包括实现违反当前有效 ADR，或存在应形成 / 更新但尚未进入 Repository Authority 的长期架构决定。
9. 形成 `READY` 或 `GAPS`。
10. 对可在现有 Intent / Design 下修正的 Gap，描述补充/修正 Execution Work，并交回 `slice-work` 塑形为 Units。
11. 对需要改变 Product Intent 的 Gap，回到相应上游阶段或升级 Human Authority；对需要新的长期架构决定的 Gap，返回 `technical-plan` 完成 ADR 评估。

### Outputs

```text
READY
```

或：

```text
GAPS
- Gap description
- Authority / evidence reference
- Required stage return or execution-work direction
```

### Exit Conditions

Feature Behavior、Implementation State 和 Current Verification Evidence 已与 Specification 收敛一致，且实现未违反当前有效 Architecture / ADR Authority，可以进入 **Ready to Integrate**。

### Escalation Conditions

- Gap 需要 Product Authority；
- Gap 需要 Major Architecture Authority；
- Authoritative Sources Conflict；
- 需要未授权 Shared / Production / External Side Effect 才能证明收敛。

### Context Rules

- Feature-wide，但仍遵循 Progressive Disclosure；
- 不把 Conversation History 当作完成证据；
- 不因 Ticket / Unit 状态为 Done 就声明 READY；
- READY 必须由当前证据支持。

### Allowed Sub-skills / Disciplines

- Verification-before-claim
- Code Review（risk-based discipline）
- Context Discipline
- Human Escalation

## 11. 第一批范围决定

### 11.1 第一批核心 Skill

第一批进入设计与后续实现的 Skill 固定为：

1. `clarify-intent`
2. `specify`
3. `technical-plan`
4. `slice-work`
5. `readiness-check`
6. `execute-unit`
7. `systematic-debug`
8. `converge`

### 11.2 暂不独立实现

第一批不新增：

- `verify-evidence`
- `code-review`
- 独立 `tdd`
- 独立 `context-discipline`
- 独立 `human-escalation`
- `handoff`
- `research`
- `prototype`
- Project Bootstrap Skill

这些能力要么继续作为 Embedded Discipline，要么等待核心路径稳定后再单独评估。

## 12. 原待解决问题的处理结果

1. **`clarify-intent` 与 `specify` 是否合并？**  
   不合并。Small-change Path 可以轻量执行或由 Runtime 连续编排，但保持两个独立语义契约。

2. **`readiness-check` 显式还是自动调用？**  
   User 不必显式调用。Controller / Workflow Runtime 可以自动发起；它仍保持独立 Gate Contract。小型安全修改可以轻量满足同一 Readiness 语义，避免流程主义。

3. **是否拆分 `verify-evidence`？**  
   第一批不拆。Verification 继续内嵌于 `execute-unit` 与 `converge`，并作为 Verification-before-claim Discipline。

4. **是否拆分 `code-review`？**  
   第一批不拆。Review 继续按风险触发，并保持 Specification Compliance / Engineering Quality 两个逻辑 Verdict。

5. **`handoff` 是否进入第一批？**  
   不进入。它属于 Transition Skill，不是核心 Feature / Defect Path 的必要前置。

6. **Execution Unit 的 Reference Implementation 用什么持久化形式？**  
   第一批不规定统一持久化形式。只冻结逻辑契约；Markdown Task、Issue、Runtime Object 等均可作为载体。

7. **如何发现 Repository-specific Build / Test Commands？**  
   由 `execute-unit` 在 Fresh Execution Context 中，从适用 Repository Rules 与 Actual Current Repository State 发现并验证，不在通用 Skill 中硬编码特定工具命令。
