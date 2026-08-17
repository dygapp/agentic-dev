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

### 2.5 Project Initialization Skills

可以按需提供项目初始化 Skill，用于建立：

- Repository Instructions
- Authority Hierarchy
- Governance
- Context / Document Locations
- Verification Commands
- Integration Policy

Project Bootstrap 不属于正常 Feature Workflow。

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

可选 Metadata：

- priority
- status
- risk
- owner / worker
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

标准化的是语义职责，而不是具体工具 Harness。
