# AI Agent 驱动软件开发方法

**状态：** Baseline v0.1  
**性质：** 规范性文档

## 1. 目标

本文定义一套不依赖编程语言、框架、Issue Tracker、Agent 产品和业务领域的通用 AI Agent 驱动软件开发方法。

方法重点解决：

- 如何从 Intent 进入可执行工作；
- 如何管理 Specification 与 Technical Design；
- 如何按 AI Context Capacity 拆分工作；
- 如何使用 Fresh Context；
- 如何验证完成状态；
- 何时由 AI 自主处理，何时必须人工介入。

## 2. Feature 主流程

```text
Governance / Domain Context
            │
            ▼
      1. Clarify Intent
            │
            ▼
      2. Specification
            │
       Spec Ready Gate
            │
            ▼
  3. Technical Planning?
       │             │
      no            yes
       │             ▼
       │       Technical Plan
       └──────┬──────┘
              ▼
      4. Slice & Ready
              │
       Execution Units
              │
       Readiness Gate
              │
              ▼
        5. Execute
              │
      Fresh Execution Context
      JIT Execution Planning
      Implementation / TDD
      Verification / Review
              │
              ▼
       6. Converge
              │
       Feature-wide Review
       Full Verification
              │
              ▼
      Ready to Integrate
              │
        Human / Policy
```

正式方法阶段只有六个：

1. Clarify Intent
2. Specification
3. Technical Planning（Optional）
4. Slice & Ready
5. Execute
6. Converge

Integration 不属于通用开发生命周期，因为它依赖具体仓库和运行环境的授权策略。

## 3. Stage 1 — Clarify Intent

### 核心问题

> 真正需要解决的问题或达成的结果是什么？

### 输入

- User / Stakeholder Intent；
- 当前 System / Domain Context；
- 已存在的 Authority Constraints；
- 已知 Scope。

### 工作原则

只澄清可能显著改变以下内容的问题：

- Product Goal；
- User-visible Behavior；
- Business Boundary；
- Acceptance Result；
- Significant Non-functional Obligation。

不要求消除所有实现层不确定性。

### 最小输出

- Goal
- In Scope
- Out of Scope
- Key Observable Behaviors
- Confirmed Decisions
- Remaining Blocking Questions（如仍存在）

不强制创建单独 Clarification 文档，可以直接作为 Specification 的输入。

### Exit Condition

不存在会显著改变 Goal、Scope、Product Behavior 或 Acceptance Result 的关键未决问题。

## 4. Stage 2 — Specification

### 核心问题

> 系统必须做什么？为什么？

### 输入

- Clarified Intent；
- Governance Context；
- Domain Context；
- Existing Authoritative Behavior。

### 最小语义内容

Specification 至少应让 Fresh Agent 独立理解：

- Goal
- Scope
- Observable Behaviors
- Business Rules
- Boundary / Failure Behavior
- Acceptance Criteria
- Relevant Non-functional Constraints

### 默认禁止写入

除非属于外部强制要求，否则 Specification 不应默认包含：

- Source File Paths；
- Class / Function Names；
- Framework-specific Construction Details；
- Database Implementation Choices；
- Step-by-step Edit Instructions。

### Spec Ready Gate

Fresh Agent 只读取 Specification 和最小必要 Repository Context，应能判断：

1. 要做什么；
2. 不做什么；
3. 什么情况下算完成；
4. 是否还存在关键歧义。

高影响歧义必须在实施前解决。

## 5. Stage 3 — Technical Planning（Optional）

### 核心问题

> Specification 应如何映射到当前技术系统？

### 触发条件

当 Specification 无法直接、安全地映射到实现时才进入。

典型情况：

- Cross-module Behavior；
- New Data / Persistence Model；
- New External Integration；
- Migration；
- Shared / Public Contract Change；
- Deployment Topology Change；
- Significant Architecture Trade-off。

### 输入

- Specification；
- Current Architecture；
- Relevant ADRs；
- Current Codebase State；
- Technical Constraints。

### 输出

只记录跨 Execution Unit 有持续协调价值的技术决策：

- Technical Approach
- Component Boundaries
- Data / Contract Design
- Important Seams
- Migration Strategy
- Testing Strategy
- Risks / Constraints

### Exit Condition

实施前必须解决的技术不确定性已经解决。

## 6. Stage 4 — Slice & Ready

### 核心问题

> 如何把工作拆成 Fresh Agent 可以独立实现和验证的单元？

### Execution Unit

Execution Unit 是本方法的逻辑工作单位，与 Jira、GitHub Issue、Markdown Task 等具体工具无关。

最小字段：

- Identifier
- Goal
- Specification Trace / Reference
- Observable Completion Condition
- Dependencies
- Relevant Constraints

### 质量属性

每个 Execution Unit 应尽量满足：

- Vertical
- Independently Verifiable
- Bounded
- Traceable
- Context-fit
- Low Hidden Dependency

### Readiness Gate

正式执行前统一检查四个维度。

#### Specification Readiness

- 无阻塞性歧义；
- Acceptance 可观察、可验证；
- Scope 足够明确。

#### Design Readiness

存在 Technical Plan 时：

- 覆盖相关 Specification；
- 没有擅自改变需求；
- 必要技术决定已确认。

#### Execution Readiness

- Requirements 有 Execution Coverage；
- 不存在重要 Orphan Work；
- Dependencies 真实且顺序合理；
- Unit 满足 Context-fit；
- Unit 有明确 Completion Condition。

#### Governance Readiness

- 不违反 Repository Instructions、Engineering Rules 和已确认 Architecture Decisions。

### 默认升级规则

Readiness Check 尽量由 AI 自动完成。

只有 Agent 无权自主解决的问题才升级给 Human。

## 7. Stage 5 — Execute

### 核心问题

> 能否使用最小权威上下文，在一个 Fresh Context 中实现并证明当前 Execution Unit？

### Execution Context

默认加载：

- Repository Rules
- Current Execution Unit
- Relevant Specification Sections
- Relevant Technical Plan Decisions
- Relevant ADR / Domain Context
- Relevant Current Code / Tests

不依赖完整 Conversation History。

### 内部执行循环

```text
Load Minimum Authoritative Context
        ↓
Inspect Actual Repository State
        ↓
Create JIT Execution Plan if useful
        ↓
Establish Expected / Failing Evidence
        ↓
Implement
        ↓
Run Targeted Verification
        ↓
Debug if necessary
        ↓
Review when risk warrants
        ↓
Record Verified Result
```

### JIT Execution Plan

临时执行计划可以包含：

- 当前实际相关文件；
- Concrete Edit Sequence；
- Exact Test Commands；
- Local Implementation Details。

默认随当前执行 Context 结束，不进入长期知识库。

### Exit Condition

当前 Execution Unit 的 Completion Condition 已经有**当前证据**支持。

## 8. Stage 6 — Converge

### 核心问题

> 当前系统整体状态是否真正符合权威 Feature Intent？

### 输入

- Specification；
- Technical Plan（如存在）；
- Execution Units；
- Current System / Code State；
- Current Verification Evidence。

### 检查内容

- Missing Behavior
- Partial Implementation
- Contradiction with Specification
- Unintended / Unrequested Behavior
- Obsolete Technical Plan
- Unverified Critical Behavior
- Cross-unit Integration Gap

### 输出

只能形成两类主要结果：

```text
READY
```

或：

```text
GAPS
→ New / Corrected Execution Units
```

### Exit Condition

Feature Behavior、Implementation State 和 Verification Evidence 已与 Specification 收敛一致。

随后工作进入：

> **Ready to Integrate**

## 9. Defect Workflow

缺陷默认不走完整 Feature Workflow。

```text
Observed Symptom
      ↓
Reproduce
      ↓
Determine Expected Behavior
      ↓
Root Cause Investigation
      ↓
Hypothesis
      ↓
Failing / Reproduction Evidence
      ↓
Minimal Fix
      ↓
Regression Verification
      ↓
Review if warranted
```

如果 Debug 过程中发现 Expected Behavior 本身未定义或错误，则回退到 Clarify Intent / Specification。

如果 Fix 涉及重大架构变化，则按需进入 Technical Planning。

## 10. 阶段回退

本方法不是单向瀑布。

```text
Execute
  ├─发现 Requirement Ambiguity → Specification / Clarify
  ├─发现 Technical Design Invalid → Technical Planning
  ├─发现 Unit Too Large → Slice Again
  ├─出现 Unexpected Failure → Systematic Debugging
  └─发现 Feature Gap → Converge → New Execution Units
```

一旦回退改变了项目事实，必须更新对应权威 Artifact，不能只在当前聊天中临时修补。

## 11. Context Model

### 11.1 Governance Context

长期存在：

- Repository Rules
- Engineering Principles
- Authority Rules

### 11.2 Domain Context

按项目需要长期存在：

- Glossary
- Durable Domain Facts
- ADRs

### 11.3 Feature Context

Feature 生命周期：

- Specification
- Optional Technical Plan

### 11.4 Execution Context

单 Execution Unit 生命周期：

- Current Unit
- Relevant Code / Tests
- JIT Execution Plan
- Targeted Evidence

### 11.5 Coordination Context

当前 Workflow / Session 生命周期：

- Queue / Progress
- Temporary Rulings
- Blockers
- Verification Status
- Remaining Work

Conversation History 不属于权威 Context Layer。

## 12. Controller / Worker Model

运行环境支持时，推荐采用 Controller / Worker。

Controller 维护 Coordination Context。

Worker 每次只获得一个 Execution Unit 所需的 Fresh Execution Context。

这是推荐实现，不是方法硬性要求。

方法真正要求的是：

> Coordination Context 与 Execution Context 逻辑分离。

## 13. Human Escalation

统一判断三个维度：

1. **Authority** — Agent 是否被授权作出这个决定或执行这个动作？
2. **Impact** — 是否显著改变 Product Behavior 或 External State？
3. **Reversibility** — 是否可以安全、低成本回滚？

### Agent 默认自主处理

- 普通 Code Structure；
- 低影响 Local Implementation Choice；
- 可逆 Technical Detail；
- Test / Build / Lint Investigation；
- 可以由 Code / Evidence 判断的事实。

### Human / Explicit Policy 必须介入

- Product Behavior 存在多种 materially different 的合理解释；
- Scope / Intent 改变；
- Destructive / Hard-to-reverse Data Operation；
- Security / Privacy Sensitive Decision；
- Major Architecture Direction；
- Authoritative Sources Conflict；
- 未授权的 Shared / Production / External Side Effect。

## 14. 工作产物策略

| Artifact | 生命周期 |
|---|---|
| Repository Rules | 长期 |
| Governance / Engineering Principles | 长期 |
| Domain Context | 按需长期 |
| ADR | 条件长期 |
| Specification | Feature 权威产物 |
| Technical Plan | 条件长期 |
| Execution Unit | 工作生命周期 |
| JIT Execution Plan | 临时 |
| Code / Tests | 长期系统事实 |
| Verification Evidence | 当前状态证据 |
| Handoff | 临时 Transition State |

不存在“一个阶段必须对应一个文件”的要求。

## 15. 按复杂度选择流程

### 小型安全修改

```text
Intent
 ↓
Lightweight Specification / Execution Unit
 ↓
Execute
 ↓
Verify
 ↓
Ready to Integrate
```

### 普通 Feature

```text
Clarify
 ↓
Specification
 ↓
Slice & Ready
 ↓
Execute
 ↓
Converge
```

### 复杂 Feature

```text
Clarify
 ↓
Specification
 ↓
Technical Plan
 ↓
Slice & Ready
 ↓
Execute
 ↓
Converge
 ↓
Full Verification
```

方法必须与工作复杂度成比例，避免流程主义。
