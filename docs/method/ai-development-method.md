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

进入 **Ready to Integrate** 前，工作必须满足与自身规模相称的收敛语义：当前权威 Intent、当前实现状态与当前 Verification Evidence 必须彼此一致，并且不存在已知的 Blocking Gap。

普通与复杂 Feature 通过 Stage 6 `Converge` 显式完成这一判断。小型安全修改可以轻量执行相同收敛语义，不要求为了流程完整性制造重型 Feature-wide 报告或独立持久 Artifact，但 **Execution Unit Completion 本身不能直接等同于 Ready to Integrate**。

Standalone Defect 不要求机械进入完整 Feature Workflow；它在满足既有 Expected Behavior、完成 Root-cause Fix 与 Regression Verification 后，还必须完成与缺陷范围相称的最终 Closure Check，确认当前证据充分、没有已知阻塞回归或未经授权行为，才能进入 Ready to Integrate。

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

### ADR 产生规则

技术规划不仅消费已有 ADR，也必须判断新形成的 Durable Technical Decision 是否需要提升为架构决策记录（Architecture Decision Record，ADR）。

Technical Plan 与 ADR 的职责不同：

- **Technical Plan** 记录当前 Feature 或一组 Execution Units 为安全实施而需要持续协调的 HOW；
- **ADR** 记录会跨越当前 Feature、对后续工作形成长期架构约束，且需要保留决策背景、取舍或替代关系的重要架构决定。

当技术决定具有以下一项或多项特征时，应显式评估是否形成或更新 ADR：

- 预计约束未来多个 Feature、模块或独立工作流；
- 改变系统级 Component、Data、Integration、Deployment 或 Shared / Public Contract Boundary；
- 替换成本较高、难以安全回滚，或会形成长期兼容 / 迁移义务；
- 存在多个具有实质不同长期后果的合理方案，需要保留选择理由与主要 Trade-off；
- 后续 Agent 若不知道该决定及其理由，容易重新打开已关闭的架构选择或产生相互冲突的实现。

以下情况通常不形成 ADR：

- 只服务当前 Feature 的技术协调决定；
- 单个 Execution Unit 内的局部、低影响、可逆实现选择；
- Exact File、Command、Edit Sequence 等 JIT Execution Detail；
- 尚未形成稳定决定的探索记录。

ADR 是**条件性长期权威产物**，不是新的方法阶段，也不要求每次 Technical Planning 都创建。方法不规定固定 `adr/` 目录、文件名或模板；Consumer Repository 应根据自身 Repository Authority 选择合适载体。

形成 ADR 不自动意味着必须由 Human 批准。是否升级仍按 Authority、Impact、Reversibility 判断；Major Architecture Direction、难以逆转的高影响 Trade-off 或超出 Agent Authority 的决定必须升级。

如果 Execute、Systematic Debugging 或 Converge 才暴露新的长期架构决定，不应在代码或局部 Plan 中静默固化；应回退到 Technical Planning，完成相应架构决策判断后再继续实施。

已有 ADR 被新决定取代时，应保留可追溯的 Superseded / Replaced 关系，而不是静默覆盖历史决策背景。

### Exit Condition

实施前必须解决的技术不确定性已经解决；需要形成或更新的长期架构决定已经进入适当的 Repository Authority，且不存在尚未处理的 ADR / Architecture Authority Gap。

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

如果当前 Technical Planning 产生或更新了 ADR / Architecture Decision：

- 相关 Execution Units 必须引用并遵守当前有效的架构约束；
- 不得让 Technical Plan 或 Unit 静默覆盖已确认 ADR；
- 若存在未解决的 ADR / Architecture Authority Gap，不得进入 Execute。

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

Unit 成功退出 Execute 只证明当前 Unit 已完成，不自动证明整个 Feature / Change 已满足进入 Ready to Integrate 所需的最终收敛语义。

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
- Architecture / ADR Gap

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

### 比例化执行

Converge 的语义要求不因工作规模较小而消失，但执行强度应与工作复杂度成比例。

对于只有一个 Execution Unit 的小型安全修改，可以轻量执行同一收敛检查：确认该 Change 的权威 Scope 已完整实现、当前证据支持 Completion、没有已知 Blocking Gap，也没有未经授权的 Product / External Behavior。此时不要求重型报告、独立长期 Artifact 或人为制造额外流程层级。

轻量 Convergence 仍然是与 Unit Verification 逻辑上不同的最终完成判断；不得因为 Unit 已 Completed 就自动推出 `READY`。

### Exit Condition

Feature Behavior、Implementation State 和 Verification Evidence 已与 Specification 收敛一致，且实现未违反当前有效的长期 Architecture / ADR Authority。

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
      ↓
Defect Closure Check
      ↓
Ready to Integrate
```

如果 Debug 过程中发现 Expected Behavior 本身未定义或错误，则回退到 Clarify Intent / Specification。

如果 Fix 涉及重大架构变化，则按需进入 Technical Planning。

### Standalone Defect Closure

Standalone Defect 在进入 Ready to Integrate 前，应至少确认：

- Expected Behavior 仍有当前权威支持；
- Root Cause 已处理，而不是只让症状暂时消失；
- Regression Evidence 来自修复后的当前状态；
- Repository Rules 要求的相关验证已经完成；
- 没有已知会阻塞该缺陷修复交付的回归、未经授权 Product Behavior 或 External Side Effect；
- 调查过程没有暴露尚未处理的 Requirement / Major Design / Authority Gap。

该 Closure Check 是与缺陷规模相称的最终收敛检查，不要求为了形式完整性创建 Feature Specification、Execution Unit Set 或调用完整 Feature `converge` 流程。

`systematic-debug` 负责证明 Root Cause Fix 与 Regression Evidence；它本身不自动执行 Integration，也不因为 Regression Test 通过就拥有 Merge / Push / Release / Deploy 权限。

## 10. 阶段回退

本方法不是单向瀑布。

```text
Execute
  ├─发现 Requirement Ambiguity → Specification / Clarify
  ├─发现 Technical Design Invalid → Technical Planning
  ├─发现新的长期 Architecture Decision → Technical Planning / ADR Evaluation
  ├─发现 Unit Too Large → Slice Again
  ├─出现 Unexpected Failure → Systematic Debugging
  └─发现 Feature Gap → Converge → New Execution Units
```

Systematic Debugging 或 Converge 发现新的长期 Architecture Decision 时，也应按同样原则回退到 Technical Planning，而不是在当前阶段静默建立长期架构约束。

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
- ADRs（由真实长期架构决策按需产生）

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
| ADR | 条件长期；只在需要跨 Feature 保留架构约束与决策理由时产生 |
| Specification | Feature 权威产物 |
| Technical Plan | 条件长期；服务当前 Feature / Execution Units 的 HOW 协调 |
| Execution Unit | 工作生命周期 |
| JIT Execution Plan | 临时 |
| Code / Tests | 长期系统事实 |
| Verification Evidence | 当前状态证据 |
| Handoff | 临时 Transition State |

不存在“一个阶段必须对应一个文件”的要求，也不存在“进入 Technical Planning 就必须创建 ADR”的要求。

## 15. 按复杂度选择流程

### 小型安全修改

```text
Intent
 ↓
Lightweight Specification / Execution Unit
 ↓
Execute
 ↓
Targeted Verification
 ↓
Lightweight Convergence
 ↓
Ready to Integrate
```

`Lightweight Convergence` 只表示以与工作规模相称的方式应用 Stage 6 完成语义；它不要求重型报告，也不能由 Unit Completed 状态自动替代。

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
 ↓
Ready to Integrate
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
Converge / Full Verification
 ↓
Ready to Integrate
```

Technical Planning 中如果形成跨 Feature 的长期架构决定，应在进入 Slice & Ready 前完成相应 ADR / Architecture Authority 的持久化；如果没有这类决定，则不创建 ADR。

### Standalone Defect

```text
Observed Defect
 ↓
Systematic Debugging
 ↓
Regression Verification
 ↓
Defect Closure Check
 ↓
Ready to Integrate
```

方法必须与工作复杂度成比例，避免流程主义；比例化不能被解释为跳过最终的权威、实现与当前证据一致性判断。