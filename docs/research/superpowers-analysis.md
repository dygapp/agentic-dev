# 研究总结 — obra/superpowers

**研究日期：** 2026-08-17  
**性质：** 非规范性研究输入

## 1. 项目定位

上游仓库：

https://github.com/obra/superpowers

该项目更强调 Agent 执行阶段的纪律、编排、验证、调试和隔离。

在当前研究中，它主要用于验证 Execution Discipline，而不是重新定义方法主生命周期。

## 2. 主要观察

### 2.1 Detailed Plan 更适合执行时生成

Superpowers 倾向于使用非常具体的 Plan：

- Exact Files
- Test Commands
- Edit Steps

这与 Durable Ticket 的行为导向并不真正冲突，只要把它们分成不同 Artifact。

因此当前方法明确区分：

- Durable Technical Plan
- Durable Execution Unit
- Transient JIT Execution Plan

### 2.2 Controller / Worker 是有效的 Context Model

Coordinator 保留 Workflow State，Fresh Worker 执行单个工作单元。

当前方法吸收其逻辑分层：

- Coordination Context
- Execution Context

但不要求必须使用 Subagent。

### 2.3 Completion Claim 必须有证据

这一点被提升为当前方法的顶层原则：

> No Completion Claim Without Current Evidence.

### 2.4 Debugging 值得形成独立 Workflow

Systematic Debugging 强调：

```text
Reproduce
→ Root Cause
→ Hypothesis
→ Failing Evidence
→ Minimal Fix
→ Regression
```

因此当前架构把 `systematic-debug` 列为核心候选 Skill。

### 2.5 Execution Isolation 有独立价值

Branch、Worktree、Sandbox、Temporary Workspace 都可以帮助区分 Baseline State 和 Changed State。

当前方法保留抽象原则，不强制 Git Worktree。

### 2.6 Human Intervention 应集中在授权边界

普通、低影响、可逆的实现歧义由 Agent 自主处理。

Destructive、Irreversible、Security-sensitive 或 Authority-sensitive 决策才升级。

### 2.7 两类 Review Verdict 可以逻辑分离

- Specification Compliance
- Engineering Quality

但不要求一定使用两个 Reviewer Agent。

## 3. 本方法吸收的内容

- JIT Execution Planning
- Controller / Worker Logical Separation
- Evidence-before-claims
- Systematic Debugging
- Execution Isolation
- Reversible-decision Autonomy
- Spec Compliance / Engineering Quality Separation

## 4. 未直接照搬的内容

- 2–5 分钟级永久 Task Decomposition
- Mandatory Git Worktrees
- 所有场景强制 TDD
- 每个微任务多个 Reviewer Agents
- 固定完整 Command Lifecycle

## 5. 参考

- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/blob/main/README.md
