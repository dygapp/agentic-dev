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

如果澄清过程识别了会约束后续多个功能的长期领域事实（Durable Domain Fact），应把它作为领域权威（Domain Authority）候选交给 Specification 阶段验证，并按 Consumer Repository Authority 交给有权维护领域事实的职责确认和持久化；不得因为事实首先出现在会话、Feature 输入或临时 Plan 中，就自动把它提升为长期权威。

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

### 领域权威候选与更新

Specification 主要形成当前功能的 WHAT / WHY 权威，同时必须判断其中确认的业务术语、业务不变量、跨功能规则或其他领域事实是否需要进入长期领域上下文（Domain Context）。

满足以下条件时，应显式评估创建或更新领域权威产物（Domain Authority Artifact）：

- 该事实预计会被多个功能、缺陷处理或独立工作流持续消费；
- 后续 Agent 若只读取单个 Feature Specification，容易遗漏该事实或产生冲突解释；
- 该事实需要独立于当前功能生命周期持续维护；
- 当前工作修正了已有长期领域事实，且旧事实继续作为有效权威会误导后续工作。

Feature Specification 可以引用长期领域权威，但不得静默覆盖它。是否接受候选并更新 Domain Context，由 Consumer Repository Authority 指定的产品 / 领域责任方决定；Agent 只有在获得相应授权时才能执行该更新。Execute、Systematic Debugging 或 Converge 如果发现长期领域事实缺失、冲突或已失效，应返回 Clarify Intent / Specification 完成候选验证，再交由上述责任方确认；不得只在代码、测试、聊天或局部计划中完成事实提升。

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

技术规划不仅消费已有 ADR，也必须判断新形成的长期技术决策（Durable Technical Decision）是否需要提升为架构决策记录（Architecture Decision Record，ADR）。

Technical Plan 与 ADR 的职责不同：

- **Technical Plan** 记录当前功能（Feature）或一组执行单元（Execution Units）为安全实施而需要持续协调的 HOW；
- **ADR** 记录会跨越当前功能、对后续工作形成长期架构约束，且需要保留决策背景、权衡（Trade-off）或替代关系的重要架构决定。

架构上下文（Architecture Context）描述当前有效的系统结构、组件与契约边界、技术约束以及实现必须遵守的架构状态。它可以由当前代码、架构说明、公共契约和有效 ADR 共同构成。ADR 只记录满足条件的重要架构决定及其理由，不等同于全部 Architecture Context，也不应被用来复制所有当前架构状态。

Technical Planning 如果改变了需要跨当前功能持续消费的架构状态，应更新适当的架构权威产物（Architecture Authority Artifact）；其中只有需要长期保留决定背景、主要权衡或替代关系的决定才形成或更新 ADR。局部、可逆且只服务当前功能的技术协调仍留在 Technical Plan 中。

当技术决定具有以下一项或多项特征时，应显式评估是否形成或更新 ADR：

- 预计约束未来多个功能、模块或独立工作流；
- 改变系统级组件、数据、集成、部署或共享 / 公共契约边界（Shared / Public Contract Boundary）；
- 替换成本较高、难以安全回滚，或会形成长期兼容 / 迁移义务；
- 存在多个具有实质不同长期后果的合理方案，需要保留选择理由与主要权衡；
- 后续 Agent 若不知道该决定及其理由，容易重新打开已关闭的架构选择或产生相互冲突的实现。

以下情况通常不形成 ADR：

- 只服务当前功能的技术协调决定；
- 单个执行单元内的局部、低影响、可逆实现选择；
- 精确文件、命令、编辑顺序等即时执行细节（JIT Execution Detail）；
- 尚未形成稳定决定的探索记录。

ADR 是**条件性长期权威产物**，不是新的方法阶段，也不要求每次 Technical Planning 都创建。方法不规定固定 `adr/` 目录、文件名或模板；Consumer Repository 应根据自身仓库权威（Repository Authority）选择合适载体。

形成 ADR 不自动意味着必须由人工批准。是否升级仍按权限（Authority）、影响（Impact）、可逆性（Reversibility）判断；重大架构方向（Major Architecture Direction）、难以逆转的高影响权衡或超出 Agent 授权边界的决定必须升级。

如果 Execute、Systematic Debugging 或 Converge 才暴露新的长期架构决定，不应在代码或局部计划中静默固化；应回退到 Technical Planning，完成相应架构决策判断后再继续实施。

已有 ADR 被新决定取代时，应保留可追溯的被取代 / 替换（Superseded / Replaced）关系，而不是静默覆盖历史决策背景。

### Exit Condition

实施前必须解决的技术不确定性已经解决；需要形成或更新的长期架构决定已经进入适当的仓库权威，且不存在尚未处理的 ADR / 架构权威缺口（Architecture Authority Gap）。

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

上述内容不要求采用固定字段名或固定模板，但整个执行单元集合必须能够显式回答：每项必需行为 / 验收义务由哪个执行单元承担实现与验证责任，或者为什么必须由功能整体验证承担。

### 质量属性

每个 Execution Unit 应尽量满足：

- Vertical
- Independently Verifiable
- Bounded
- Traceable
- Context-fit
- Low Hidden Dependency

### 验收义务与验证责任闭环

切分与就绪阶段不只检查实现范围是否被执行单元覆盖，还必须建立验收义务到验证证据的可执行闭环：

```text
规格验收义务（Specification Acceptance Obligation）
→ 实现责任 / 验证责任（Implementation / Verification Responsibility）
→ 计划验证证据（Planned Verification Evidence）
→ 已执行的当前证据（Executed Current Evidence）
```

规则：

- 每项必需行为 / 验收义务必须明确归属某个执行单元，或在行为只有跨执行单元组合后才能被有效证明时，明确归属功能整体验证责任（Feature-wide Verification Responsibility）；
- 实现责任与验证责任可以由同一执行单元承担，也可以在有真实跨执行单元原因时分开，但不能让验证责任处于未归属状态；
- 计划验证证据必须足以区分义务是否真实满足，不能只写“代码完成”“测试通过”或其他无法对应具体行为的宽泛条件；
- 分页、排序、边界 / 失败、多状态、跨入口等容易被主路径遗漏的行为，应按规格说明风险设计足以证明其关键差异的验证场景；
- 不要求一条验收义务对应一个测试，也不规定必须使用自动化测试、E2E、CI 或特定证据格式；证据类型与强度应和行为、风险及仓库规则相称；
- 功能整体验证责任只用于确实需要组合状态才能证明的行为，不能作为推迟普通执行单元级验证的兜底标签；
- 实现存在、代码检查通过或某条邻近路径已经验证，不自动等同于该验收义务已获得验证覆盖（Verification Coverage）。

该闭环可以通过执行单元字段、覆盖视图或 Consumer 仓库选择的等价载体表达，不要求新增固定长期产物。

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

如果当前 Technical Planning 产生或更新了 ADR / 架构决策（Architecture Decision）：

- 相关执行单元必须引用并遵守当前有效的架构约束；
- 不得让 Technical Plan 或执行单元静默覆盖已确认 ADR；
- 若存在未解决的 ADR / 架构权威缺口，不得进入 Execute。

#### Execution Readiness

- 需求同时具有实现覆盖（Implementation Coverage）与验证覆盖；
- 每项必需行为 / 验收义务都有明确的实现与验证责任，或有合法且显式的功能整体验证责任；
- 计划验证证据足以证明所承接的义务，而不是只覆盖主路径；
- 不存在重要孤立工作项或未归属的验证义务；
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
- 当前执行单元承接的验收义务与计划验证证据
- Relevant Technical Plan Decisions
- Relevant Architecture / ADR / Domain Context
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

当前执行单元的完成条件，以及由当前执行单元承担验证责任的必需行为 / 验收义务，已经有**当前证据**支持。

声明执行单元 `Completed` 前必须回到其规格追踪检查义务闭环；实现存在、代码检查或未覆盖关键差异的主路径证据不能替代必要的已执行的当前证据。

如果某项义务已基于真实跨执行单元原因显式归属功能整体验证责任，执行单元结果必须保留该 `Pending` 责任，不能把执行单元完成陈述为该义务已经获得证据。执行单元成功退出执行只证明当前执行单元自身的实现与验证责任已完成，不自动证明整个功能 / 变更已满足进入 `Ready to Integrate` 所需的最终收敛语义。

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

`converge` 必须重新从规格说明建立功能整体覆盖，不把切分 / 就绪检查阶段形成的责任归属或计划证据视为完成证据。此前显式归属功能整体验证责任的义务在本阶段到期，仍缺少已执行的当前证据时必须阻止 `READY`。

- Missing Behavior
- Partial Implementation
- Contradiction with Specification
- Unintended / Unrequested Behavior
- Obsolete Technical Plan
- Unverified Critical Behavior
- Cross-unit Integration Gap
- 架构 / ADR 缺口（Architecture / ADR Gap）
- 长期权威产物的生命周期缺口（Artifact Lifecycle Gap）

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

Feature Behavior、Implementation State 和 Verification Evidence 已与 Specification 收敛一致，实现未违反当前有效的领域、架构 / ADR 权威，且本次工作产生或改变的长期权威事实已经完成适当的生命周期闭环。

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
  ├─发现长期领域事实缺失或冲突 → Specification / Domain Authority Update
  ├─发现 Technical Design Invalid → Technical Planning
  ├─发现新的长期架构状态或决策 → Technical Planning / Architecture Authority / ADR 评估
  ├─发现 Unit Too Large → Slice Again
  ├─出现 Unexpected Failure → Systematic Debugging
  └─发现 Feature Gap → Converge → New Execution Units
```

Systematic Debugging 或 Converge 发现长期领域事实缺口时，应回退到 Clarify Intent / Specification；发现新的长期架构状态或决策时，应回退到 Technical Planning，而不是在当前阶段静默建立长期权威。

一旦回退改变了项目事实，必须更新对应权威 Artifact，不能只在当前聊天中临时修补。

## 11. Context Model

### 11.1 长期权威产物的生命周期闭环

长期权威产物（Durable Authoritative Artifact）只有在以下生命周期责任明确时，才形成闭环：

| 责任 | 必须回答的问题 |
|---|---|
| Producer | 哪个方法职责或已授权角色负责确认并形成该产物？ |
| Trigger | 什么事实或变化使创建、提升或重大更新成为必要？ |
| Consumer | 哪些后续阶段、Skill、人员或系统依赖它？ |
| Persistence | 它以什么受仓库权威管理的载体长期保存和被发现？ |
| Update | 新证据、需求变化或系统变化出现时，谁在什么条件下维护它？ |
| Supersede | 旧内容失效时，如何标明取代、保留必要历史并避免新旧同时生效？ |
| Escalation | 哪些权限冲突、高影响变化或难逆决定必须交给人工或更高权威？ |

Producer 是逻辑责任，不要求对应独立 Skill、固定人员或固定文件。Trigger 也不意味着每次进入某个阶段都必须创建产物；只有信息具备跨当前工作持续存在的权威、协调或追溯价值时才持久化。

如果当前工作新增或重大修改长期权威产物，却无法回答上述责任，应视为产物生命周期缺口（Artifact Lifecycle Gap），返回拥有相应事实或决策的职责层处理。不得用临时 Plan、会话历史、代码注释或下游 Skill 的推测代替缺失的生命周期责任。

### 11.2 Governance Context

长期存在：

- Repository Rules
- Engineering Principles
- Authority Rules

### 11.3 Domain Context

领域上下文保存跨功能持续有效的业务语言与领域事实，例如：

- Glossary
- Durable Domain Facts

其生命周期规则是：

- **Producer：** Consumer Repository Authority 指定的产品 / 领域责任方，或被明确授权承担该职责的 Agent；Clarify Intent 与 Specification 负责识别和验证候选，但阶段转换本身不授予长期领域权威写入权限；
- **Trigger：** 当候选事实会被多个后续工作消费，或现有领域权威已不再准确时，评估创建或更新；
- **Consumer：** Specification、Technical Planning、Slice & Ready、Execute、Systematic Debugging 与 Converge 按当前工作需要消费相关部分；
- **Persistence：** 使用 Consumer Repository 选择的领域文档、术语表、规则集或其他可发现的权威载体，不规定固定目录或模板；
- **Update / Supersede：** 由拥有相应产品或领域权限的职责更新；旧事实失效时应显式标明取代关系或同步修正引用，避免冲突事实同时被视为有效；
- **Escalation：** 当权威来源冲突、改变产品意图或业务边界、存在多种 materially different 的解释，或 Agent 无权确认领域事实时，升级给相应 Human / Repository Authority。

Feature Context 中出现的业务信息不会仅因被实现或验证就自动成为 Domain Context。代码和测试可以提供当前系统行为证据，但不能单独授予业务事实长期权威。

### 11.4 Architecture Context

架构上下文保存跨功能持续有效的系统结构、组件与数据边界、共享 / 公共契约、集成与部署约束以及其他当前架构状态。它与 Domain Context 的边界是：Domain Context 说明业务世界中必须成立的事实，Architecture Context 说明技术系统为满足权威意图而采用并持续受约束的结构与状态。

其生命周期规则是：

- **Producer / Trigger：** Technical Planning 在当前系统证据与有效架构权威基础上确认；当技术工作改变了需要跨当前功能持续消费的架构状态，或现有架构说明已与有效系统状态不一致时，创建或更新；
- **Consumer：** Technical Planning、Slice & Ready、Readiness、Execute、Systematic Debugging 与 Converge 按需消费；
- **Persistence：** 使用 Consumer Repository 选择的架构说明、契约、模型、代码或其他可发现的权威载体；不同载体的权威关系由该仓库定义；
- **Update / Supersede：** 架构变化被确认并实施时同步维护；旧约束失效时显式更新状态、引用或取代关系，不能让过期说明继续与当前有效架构并列；
- **Escalation：** 重大架构方向、高影响或难逆权衡、权威冲突以及超出 Agent 授权的共享 / 外部影响，按 Authority、Impact、Reversibility 升级。

ADR 是 Architecture Context 中按条件产生的决策记录：它解释重要架构决定的背景、选择、权衡、后果与替代关系，但不是全部当前架构状态。架构事实变化不必机械创建 ADR；只有满足第 5 节条件的长期决定才创建或更新 ADR。

### 11.5 Feature Context

Feature 生命周期：

- Specification
- Optional Technical Plan

### 11.6 Execution Context

单 Execution Unit 生命周期：

- Current Unit
- 负责的验收义务
- 计划验证证据
- Relevant Code / Tests
- JIT Execution Plan
- 已执行的当前证据

### 11.7 Coordination Context

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
| Domain Context | 按需长期；Clarify / Specification 识别和验证候选，由 Repository Authority 授权的领域责任方确认并维护更新与取代关系 |
| Architecture Context | 按需长期；由 Technical Planning 维护跨功能持续有效的架构状态 |
| ADR | 条件长期；属于 Architecture Context 中的决策记录，只在需要跨功能保留架构约束与决策理由时产生 |
| Specification | Feature 权威产物 |
| Technical Plan | 条件长期；服务当前功能与执行单元的 HOW 协调 |
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

Technical Planning 中如果形成跨功能的长期架构决定，应在进入 Slice & Ready 前完成相应 ADR / 架构权威（Architecture Authority）的持久化；如果没有这类决定，则不创建 ADR。

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
