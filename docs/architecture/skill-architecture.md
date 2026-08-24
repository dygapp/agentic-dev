# Skill 架构

**状态：** Baseline v0.1  
**性质：** 规范性架构文档

## 1. 目标

Skills 用于实现已经确定的开发方法，而不是另外定义一套生命周期。

当前架构明确避免创建类似 `develop-feature` 的超级 Skill。

## 2. Skill 分类

### 2.1 Workflow Skills

负责推动工作在方法阶段之间转换。

当前候选：

1. `clarify-intent`
2. `specify`
3. `technical-plan`
4. `slice-work`
5. `readiness-check`
6. `execute-unit`
7. `converge`

通常由 User、Controller 或 Workflow Runtime 显式发起。

### 2.2 Discipline Skills / Embedded Disciplines

负责规定阶段内部如何高质量工作。

候选能力：

- Test-driven Development
- Code Review
- Verification-before-claim
- Code / Design Quality
- Context Discipline

并不是每个 Discipline 都应该做成独立 Skill。

只有当某个 Discipline：

- 有独立可复用流程；
- 被多个 Workflow 重复调用；
- 复杂度足以独立维护；

时，才考虑升级为正式 Skill。

### 2.3 Investigation Skills

只在出现特定未知问题时调用。

候选：

- `systematic-debug`
- `research`
- `prototype`

其中 `systematic-debug` 已进入第一批核心候选，因为 Defect 需要独立处理路径。

### 2.4 Transition Skills

用于 Context / Session 切换。

候选：

- `handoff`

Handoff 只转移 Working State，不复制 Project Knowledge。

### 2.5 Project Initialization / Bootstrap Capabilities

项目初始化可能需要建立或确认：

- Repository Instructions
- Authority Hierarchy
- Governance
- Context / Document Locations
- Verification Commands
- Integration Policy

这类能力统称为 Project Initialization / Bootstrap Capability。它可以由 Skill、Template、Script、Setup Workflow 或人工引导实现，不预设必须 Skill 化。

Project Bootstrap 不属于正常 Feature Workflow。

仅当真实使用证明某个 Bootstrap Capability：

- 能跨多个项目重复使用；
- 具有独立、稳定的 Procedure；
- 输入、输出与 Exit Condition 可以明确；
- 主要承载可复用能力，而不是某个项目自己的事实与决策；

时，才考虑将其升级为正式 Skill。

**“可复用”本身不足以成为新增 Skill 的理由。**

### 2.6 Reusable Capability 与 Project Rule 边界

本架构区分三类内容。

#### Reusable Skill

Skill 表达可跨项目复用的执行能力。它应具有清晰职责、稳定 Procedure、明确输入输出和 Exit Condition，并能独立组合使用。

Skill 不保存某个具体项目的长期事实，也不拥有覆盖项目权威的权限。

#### Project Rule

Project Rule 表达当前 Repository 的具体 Authority、Policy、Context 与约束，例如：

- 权威来源和优先级；
- 当前阶段；
- 文档与任务位置；
- Verification / Integration Policy；
- 当前项目允许或要求使用哪些 Skills。

Project Rule 应固化在当前项目的 `AGENTS.md`、规范文档、配置或其他合适的 Repository Artifact 中。

Project Rule 可以选择、要求或限制 Reusable Skills，但 Skill 不得反向覆盖 Project Authority。

#### Bootstrap / Setup Capability

Bootstrap / Setup Capability 使用可复用流程帮助项目建立或更新 Project Rules。其产物通常是项目实例自己的 `AGENTS.md`、配置、目录约定或其他 Repository Artifact。

它可能最终实现为 Skill，但只有跨项目真实使用证据证明其具有稳定独立职责时才这样做；不得因为某条规则“可能在别的项目也有用”就提前创建 Skill。

### 2.7 平台专项 Reusable Skills

当真实 Consumer Evidence 证明某个平台或工具生态存在稳定、可复用且足够复杂的操作能力时，可以建立**平台专项非核心 Skill**。

这类 Skill：

- 实现既有 Method / Contract / Governance 语义，不新增 Method 阶段；
- 可以包含平台专有对象、API、CI/CD 机制和运行模式；
- 只有在 Consumer 实际满足触发条件时才加载，不成为所有项目的默认依赖；
- 必须服从 Consumer Repository Authority、Repository Policy 与 Runtime 实际能力；
- 不得把平台实现细节反向升级为通用 Method 强制规则；
- 不得接管完整 Feature 生命周期、Integration、Release 或 Deploy。

平台专项 Skill 与第一批核心 Skill 是组合关系，而不是替代关系。核心 Workflow Skill 可以在当前工作确实需要时调用平台专项 Skill，以取得更可靠的实现或验证能力。

真实 Consumer Experiment 已证明 GitHub Actions 验证存在独立可复用的路径选择、证据可观察性、Runtime 成本控制和诊断流程，因此允许新增：

- `github-actions-verification`：面向使用 GitHub Actions 的 Consumer，建立或优化可观察、可追踪、成本可控的 CI 验证路径。

该 Skill 属于平台专项非核心 Discipline Skill，不计入第一批 8 个核心 Skill，也不意味着重新打开核心 Skill Engineering。

### 2.8 当前 Skill 清单（Skill Inventory）

当前仓库实际实现并维护 9 个 Skill：

| 分类 | 数量 | 当前成员 | 状态语义 |
|---|---:|---|---|
| Core Skills | 8 | `clarify-intent`、`specify`、`technical-plan`、`slice-work`、`readiness-check`、`execute-unit`、`systematic-debug`、`converge` | 历史基线已关闭；Issue #18 触发 `slice-work` / `readiness-check` / `execute-unit` 定向 Hardening，待针对性验证重关 |
| Platform-specific Skills | 1 | `github-actions-verification` | 由真实 Consumer Evidence 支持的非核心 Skill |
| Future Experimental Skills | 0 | 无 | 只在新的真实证据暴露稳定职责缺口时评估 |

因此，“第一批 8 个核心 Skill”描述的是核心基线，不是仓库全部 Skill 数量。`github-actions-verification` 是当前第 9 个已实现 Skill，但不是“第 9 个核心 Skill”，其存在不重新打开 Core Skill Engineering。当前定向重开来自 Issue #18 的通用方法证据，与平台专项 Skill 数量无关，也不改变 Skill Inventory。

### 2.9 产物生命周期与 Skill 边界

长期权威产物的生命周期由 Method 职责和 Consumer Repository Authority 共同决定，不由新增的 Artifact Management Super-skill 接管：

- `clarify-intent` 可以识别长期领域事实候选，`specify` 负责在权威输入支持下验证相关 WHAT / WHY；需要独立长期维护的候选由 Consumer Repository Authority 指定的领域责任方确认并持久化，阶段转换本身不授予写入权限；
- `technical-plan` 负责判断并维护跨功能持续有效的 Architecture Context 变化，其中满足条件的重要架构决定按需形成或更新 ADR；
- `execute-unit`、`systematic-debug` 与 `converge` 可以发现权威产物缺口，但必须返回拥有该事实或决定的上游职责层，不得在下游静默提升长期权威；
- Project Rule、Repository Policy 或人工权威决定具体载体、写入权限与集成方式，Skill 不强制固定目录、模板或审批流程。

这类职责分配落实产物生命周期闭环（Artifact Lifecycle Closure），但不新增方法阶段、Domain Context Skill、Architecture Management Skill 或完整生命周期 Super-skill。

## 3. 第一批 8 个核心 Skill

| Skill | 类型 | 核心职责 |
|---|---|---|
| `clarify-intent` | Workflow | 消除 Intent 层关键歧义 |
| `specify` | Workflow | 形成或更新 WHAT / WHY 权威 |
| `technical-plan` | Workflow | 按需解决长期 HOW 决策 |
| `slice-work` | Workflow | 形成 Context-fit 的纵向 Execution Units |
| `readiness-check` | Workflow | 判断是否可以进入实施 |
| `execute-unit` | Workflow | 实现并验证一个 Execution Unit |
| `systematic-debug` | Investigation | Reproduce、Diagnose、Fix、Regression |
| `converge` | Workflow | Feature-wide Completion Check |

这 8 个 Skill 已完成 Contract Review，作为第一批核心 Skill 的设计与后续实现范围。

正式实现 `SKILL.md` 时必须遵循 `skill-contracts.md` 的已复核契约，不得通过实现扩大职责边界。

### 3.1 第一批暂不独立 Skill 化的能力

以下能力第一批不独立实现：

- `verify-evidence`；
- `code-review`；
- 独立 `tdd`；
- 独立 `context-discipline`；
- 独立 `human-escalation`；
- `handoff`。

其中前五项继续作为 Embedded Discipline；`handoff` 继续保留为 Transition Skill 候选，待核心 Feature / Defect 路径稳定后再评估。

## 4. 暂不独立 Skill 化的横切规则

### Context Discipline

- Authority First
- Progressive Disclosure
- 不依赖 Conversational Memory
- 不重复持久化已有 Durable Knowledge

### Human Escalation

统一使用：

- Authority
- Impact
- Reversibility

### Verification-before-claim

任何完成或状态声明必须有当前证据。

### Review Semantics

逻辑上保持两个 Verdict：

- Specification Compliance
- Engineering Quality

不要求一定使用两个 Reviewer Agent。

### TDD

当存在稳定 Behavior Seam 时，优先：

```text
Expected Behavior
→ Failing Evidence
→ Minimal Implementation
→ Passing Evidence
```

不强制把所有工作都机械套入测试仪式。

## 5. Skill 调用关系

```text
clarify-intent
      ↓
specify
      ↓
technical-plan?  (conditional)
      ↓
slice-work
      ↓
readiness-check
      ↓
execute-unit
      │
      ├─ embedded verification
      ├─ embedded / optional TDD
      ├─ systematic-debug on failure
      ├─ platform-specific verification skill when applicable
      └─ review when risk warrants
      ↓
converge
```

Workflow Skill 不允许静默接管整个生命周期。

`execute-unit` 不得自动：

- 执行所有剩余 Units；
- 自动 Converge；
- Merge / Push / Release；
- 执行 Destructive Cleanup。

## 6. Execution Unit 作为统一工作协议

本方法不绑定任何 Task Management Tool。

Execution Unit 可以由以下载体承载：

- GitHub Issue
- Jira
- Linear
- Markdown Task
- Runtime Object
- 其他 Tracker

最小逻辑契约：

```text
id
goal
spec_reference
completion_condition
dependencies
constraints
```

除上述最小字段外，整个 Unit Set 还必须表达以下逻辑关系，但不要求采用固定字段名或固定模板：

```text
Specification Obligation
→ Implementation / Verification Responsibility
→ Planned Verification Evidence
```

其中：

- `spec_reference` 或等价 Coverage View 必须能识别 Unit 承接的 Required Behaviors / Acceptance Obligations；
- `completion_condition` 与 Planned Verification Evidence 必须足以证明这些义务，而不只是证明实现存在或主要 Happy Path 可用；
- 只有确实需要跨 Unit 组合状态才能证明的义务，才可以显式归属 Feature-wide Verification Responsibility；
- `execute-unit` 形成 Executed Current Evidence，`converge` 仍独立从 Specification 重新检查 Feature-wide Coverage；
- 不要求一条 Acceptance 对应一个测试，也不规定测试层级、CI 平台或证据载体。

可选 Metadata：

- priority
- status
- risk
- owner / worker
- acceptance ownership
- planned verification
- evidence references

长期 Execution Unit 不要求精确 File Paths。

## 7. 未来 SKILL.md 推荐结构

Workflow Skill 统一采用：

```text
Purpose

Use When

Do Not Use When

Inputs

Authority Sources

Procedure

Outputs

Exit Conditions

Escalation Conditions

Context Rules

Allowed Sub-skills / Disciplines
```

三个最重要的字段：

### Authority Sources

明确 Skill 应信任哪些来源，以及冲突优先级。

### Exit Conditions

防止无限分析和过度处理。

### Escalation Conditions

同时避免两种错误：

- 一有歧义就问人；
- 无授权仍擅自决定。

## 8. Non-goals

本架构不强制：

- Slash Command Naming Convention
- One Artifact per Stage
- One Issue Tracker
- One Agent Runtime
- Subagents
- Git Worktrees
- Particular TDD Framework
- Mandatory Technical Plan
- Multiple Reviewer Agents
- Automatic Integration
- Project Bootstrap 必须实现为 Skill
- Project Rule 必须采用一种固定文件布局
- 所有 Consumer 使用同一个平台专项 Skill

标准化的是语义职责，而不是具体工具 Harness。
