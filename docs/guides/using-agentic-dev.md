---
id: guide:using-agentic-dev
type: guide
status: active
---

# 使用 agentic-dev

本文是面向人的总览指南。它帮助你理解 `agentic-dev` 如何组织 AI 开发工作，但不参与 ordinary Agent runtime，也不替代 Project / Method / Architecture / Skill / Rule 的正式定义。

## 1. 先区分 Project Knowledge 与 reusable Capability

`agentic-dev` 同时维护两类长期知识：

- **Project Knowledge**：只描述 `agentic-dev` 自身——为什么存在、当前采用哪些 capability、当前走到哪里以及为什么演进成今天这样；
- **Reusable Capability**：Method / Architecture / Skill / Rule / Tool contract，可以在显式 adoption / upgrade 中被 Consumer adopt / adapt / reject。

核心原则：

> **Project 不传播，Capability 传播。**

Project Knowledge 的入口见 `docs/project/README.md`；边界定义见 `docs/architecture/project-knowledge-architecture.md`。

## 2. 五类核心 capability

### Method：一类复杂工作怎样从开始走到完成

Method 定义进入条件、阶段 / 状态、阶段责任、Gate、返回和完成语义。某个 Repository 实际采用哪些 Method、如何选择它们，由该 Repository 自己的 Project Capability Profile 或等价 Authority 持有；Human inventory 见 `docs/methods/README.md`。

### Skill：责任明确后，怎样稳定执行一个有界能力

Skill 具有 Trigger / Inputs / Procedure / Outputs / Exit / Escalation。它可以服务某个 Method，也可以在其他明确任务中复用。

### Rule：当前条件成立时必须遵守什么

Rule 是 policy / constraint / default / invariant / completion requirement。它不要求依附 Skill，可以横切 Method stage、Skill、direct Agent work、repository operation 或 verification。

### Architecture：这些能力长期是什么关系

Architecture 定义可复用 capability 的边界、ownership、组合方式和运行不变量。

### Guide：给人看的解释层

Guide 把以上 canonical owner 重新组织成人容易理解的说明、教程和导航。它可以重复解释，但不能成为第二套 Authority。

## 3. Agent 和人从不同入口进入同一套体系

Agent：

```text
AGENTS.md
→ Project Roadmap + Project Capability Profile + GitHub current state
→ Method Selection（若适用）
→ current Method stage / direct responsibility
    ├─→ relevant Architecture
    ├─→ Skill discovery / invocation（如需要）
    └─→ Rule Discovery → applicable Rules
→ execute / verify
```

人：

```text
README.md
├─→ docs/project/README.md
└─→ Guides / directory README
    → 理解 Project / Method / Skill / Rule / Architecture
```

这两个视窗不是两套方法。规范语义和 Project fact 只保存在各自 canonical owner 中。

## 4. 新软件项目不是直接从 Feature Development 开始

`method:ai-development` 面向具体 Feature / change，它假设当前 Repository 已经拥有足以判断 Goal、Scope、Behavior 与 Acceptance 的 Requirement Baseline，以及当前 Feature 真正需要的最小 Architecture Context。

因此一个新项目的典型上游关系是：

```text
Raw Project Inputs
        ↓
Requirement Baseline Establishment
        ↓
Requirement Baseline Ready
        │
        ├─ no systemic architecture blocker
        │       ↓
        │   AI Development
        │
        └─ systemic architecture blocker
                ↓
        Architecture Clarification
                ↓
        Architecture Context Ready
                ↓
        AI Development
```

这里是三个不同 work kind，不再通过一个 `Software Project Clarification` super-method 串联。

这样做有两个目的：

- 新项目可以明确回答“怎样从原始资料建立完整 Requirement Baseline”；
- 简单项目不因为进入项目建立流程就被迫执行独立 Architecture Clarification。

## 5. Requirement Baseline Establishment 做什么

`method:requirement-baseline-establishment` 用于：

- greenfield software project / new product；
- 已有大量客户材料，但尚未形成稳定 Requirement Authority；
- legacy modernization / rewrite；
- Requirement Authority 碎片化、冲突、重复或 owner 不清；
- 多个 Feature 被同一组系统性 Requirement gap 阻塞。

主路径是：

```text
Establish Sources & Authority
→ Extract Requirement Facts
→ Structure Requirement Authority
→ Resolve Requirement Unknowns
→ Review Requirement Baseline
→ Requirement Convergence
→ Requirement Baseline Ready
```

重点不是“多问需求问题”，而是把 Raw Inputs 转换为长期、可定位、可维护、单一事实归属的 Requirement Authority。

## 6. Requirement Facts 应怎样分析

需求分析优先从这些事实出发：

```text
业务对象
业务活动 / workflow
业务规则
状态 / 生命周期
Actor / responsibility
外部依赖 / 输入输出
```

核心问题是：

> 谁，在什么条件下，对什么业务对象做什么，受到什么规则与状态约束，最终产生什么业务结果？

页面、按钮、菜单、API、数据库表、类 / package 等通常是后续设计结果，不应默认成为 Requirement boundary。

`jilinjobs` 的历史 Evidence 证明：能力边界、唯一事实归属和高价值歧义比穷举全部 L3 更重要；因此通用 Method 不要求固定 L1/L2/L3 编号，也不要求在项目启动时穷举未来所有 Scenario。

## 7. Requirement Authority 怎样组织

通用 ownership 由 `architecture:requirement-authority` 定义。推荐 Human IA 是：

```text
docs/requirements/
├── README.md
├── index.md
├── overview/
├── business/
├── aspects/
├── non-functional/
└── analysis/
```

Consumer 可以调整物理路径，但应保持职责边界。

### README

回答：

> 这套 Requirement 体系怎么用？

它是 Human Navigation / Usage Guide，不维护完整 Requirement inventory，也不复制业务事实。

### index

回答：

> 当前某类 Requirement 的唯一 Authority 在哪里？

它是 Requirement Authority Index / Locator，可以记录名称、分类、owner 与必要关系，但不复制业务规则正文。

### Requirement owner docs

回答：

> Requirement 事实到底是什么？

真正的业务事实进入 overview / business / aspects / non-functional 等 owner。

### analysis

保存临时 source inventory、comparison、ambiguity list、flow/state view 等工作材料；默认非 Authority，稳定结论必须 promote 到真实 owner。

更完整的人类操作说明见 `establishing-requirement-baseline.md`。

## 8. 需求会话为什么采用 Derive → Default → Ask → Review

AI 驱动需求分析最容易失控的一种方式是：只要 AI 不能立刻确认，就把所有可能分支都变成人工问题。

`method:requirement-baseline-establishment` 的默认顺序是：

```text
Authority 能回答
→ 直接使用

能唯一推导
→ 自动推导

有明确 Project Requirement Default
→ 应用默认

属于 Design Item
→ 推迟

没有 Evidence 支持额外机制
→ 默认不新增机制

只有真实 Blocking Ambiguity / Conflict
→ Ask Human

Capability 达到可读状态
→ Human Review
```

也就是说：

> **Question 是异常路径，不是主路径。**

人工主要是 Product / Domain Authority 与 Reviewer，而不是逐字段 Requirement Generator。

## 9. 怎样避免无休止的需求问答

### 只问真正会改变结果的问题

一个候选问题只有在多个合理答案会实质改变 Scope、State、Permission、Data Semantics、Business Result、Compliance 或 Acceptance，并且不解决会阻塞 Requirement Baseline 时，才升级为 Human Blocking Question。

### 能推导的直接推导

如果上游核心规则已经唯一决定下游结果，就不要再逐项询问每种角色、每个状态或每个异常分支。

### 不做否定式穷举

没有 Evidence 时，不通过以下问题让人工证明功能不存在：

```text
是否需要审核？
是否需要复核？
是否需要版本？
是否需要通知？
是否需要归档？
是否需要批量导入？
是否需要自动同步？
```

没有 Evidence 支持时，默认不新增额外业务机制。如果某类行为确实是项目级重复默认，应先形成显式 Project Requirement Default，再复用于后续 Capability。

### 使用 Delta Conversation

普通会话只输出当前需要处理的增量，不反复打印全部历史确认内容。每个问题只包含：Decision、必要 Context、Impact、Options / expected answer。

### 用 Capability Review 代替逐条确认

AI 先根据 Authority、确定性推导和 Project Default 形成一个完整 Capability Requirement，再由人工做一次总体 Review。发现问题及时修正，不要求所有正常路径都在生成前逐条获得人工批准。

## 10. Requirement 下钻什么时候停止

当 Goal / Scope、核心业务对象、Actor / Responsibility、主要状态与转换、关键规则、数据范围、跨 Capability 输入输出、主要失败结果、Out of Scope 与 Acceptance 已足以唯一决定业务行为时，应停止继续 Requirement 下钻。

如果后续问题主要变成：

```text
字段
按钮
菜单
页面布局
API
数据库
事务
缓存
类 / 包
```

通常已经进入 Specification / Technical Planning / Execute 责任。

## 11. Architecture Clarification 为什么独立

`method:architecture-clarification` 只处理这种问题：

> 多个当前或预期 Feature 共同依赖一个长期、高成本难逆、会阻塞可靠 Specification / Planning 的 systemic architecture driver。

可能包括：

- shared capability / shared contract；
- core data / structural boundary；
- security / integration / deployment topology；
- 高成本难逆结构决策；
- 多个局部实现暴露出的 shared capability extraction 信号。

它不是所有新项目的必经步骤。简单项目、成熟技术栈或已有足够 Architecture Context 的项目，可以在 `Requirement Baseline Ready` 后直接开始 Feature Development。

Feature-specific、低影响、易逆 HOW 仍属于 `method:ai-development` 的 Technical Planning / JIT Execution。

Architecture Clarification 暴露出 Product / Requirement ambiguity 时必须返回 Requirement owner；Architecture 不能通过技术判断创造产品需求。

## 12. 普通 Feature / Change 如何工作

当 Requirement Baseline 和当前必要 Architecture Context 已足够稳定后，普通 Feature / change 使用 `method:ai-development`：

```text
Clarify Intent
→ Specification
→ Technical Planning?（条件阶段）
→ Slice & Ready
→ Execute
→ Converge
→ Ready to Integrate
```

`Clarify Intent` 只解决当前 Feature 的高影响产品意图歧义，不重新分析整个项目。

如果 Feature 流程发现系统性上游缺口：

- Requirement Baseline gap → 返回 Requirement owner / `method:requirement-baseline-establishment`；
- systemic architecture gap → 返回 Architecture owner / `method:architecture-clarification`。

Integration 本身不属于通用 Method；merge、release、deploy 等仍由目标仓库策略和人工 Authority 决定。

## 13. 当前为什么没有新增 Requirement / Architecture Skill

Method 已经有真实 work kind、阶段与 Gate Evidence，但并不意味着每个阶段都值得立即形成 Skill。

当前没有足够跨 Consumer Evidence 证明 `requirements-analysis`、`requirement-elicitation`、`architecture-framing` 等 procedure 已经稳定到应该成为独立 Skill。

因此当前先固化：

- Method lifecycle / Gate；
- Requirement Authority Architecture；
- Human Guide；
- 与 AI Development 的返回边界。

只有未来真实 Consumer 使用证明某个 procedure 可独立调用、重复出现且能显著减少错误时，再评估 Skill admission。

## 14. Rule Discovery 为什么存在

随着 Rule 数量增长，把全部规则塞进 prompt 会增加上下文、引入无关约束并降低可维护性。

因此 ordinary runtime 使用：

```text
current task facts / responsibility
→ bounded task signals
→ Rule Discovery
→ 少量 {id, path}
→ 只读取候选正文
→ Agent 做最终语义适用性确认
```

具体 Repository 的 Rule root / Tool locator 属于它自己的 capability instance；通用 discovery contract 属于 Architecture。

人可以通过 `docs/rules/README.md` 浏览当前所有 Rule；Agent 不使用这个 README 进行 runtime routing。

## 15. Consumer 首次采用

首次采用不是复制整个仓库。大致过程是：

1. 恢复 Consumer 自己的 Project / Repository Authority；
2. 选择精确 upstream baseline；
3. 判断哪些 Method / Architecture / Skill / Rule / Tool contract 需要 adopt / adapt / reject；
4. 把接受的 capability 写入 Consumer-local canonical owner；
5. 建立 Consumer 自己的 capability profile / Method selector / Skill / Rule discovery；
6. 验证 ordinary runtime 不在线依赖 upstream；
7. 记录 evaluated baseline。

对于 Requirement Baseline Establishment / Architecture Clarification，Consumer 应根据自己的真实 work kind 决定是否注册 local selector mapping；不能因为 upstream inventory 出现 Method 就自动改变 ordinary Feature runtime。

upstream Project Charter / Capability Profile / Roadmap / Evolution 只用于 provenance / understanding，不复制为 Consumer Project state。

正式过程由 `docs/methods/consumer-adoption.md` 定义；人类操作说明见 `adopting-agentic-dev.md`。

## 16. Existing Consumer 升级

升级不是“同步最新版”。正确思路是：

```text
当前 Consumer Project + capability state
→ 选择精确 upstream candidate
→ 比较 reusable capability semantic delta
→ retain / adopt / adapt / replace / reject
→ 必要时更新 Consumer-local capability profile
→ targeted revalidation
→ 记录新的 evaluated baseline
```

Existing Consumer 如果已经用自己的方式建立稳定 Requirement / Architecture Authority，可以保留或 adapt；不需要因为 upstream 新增 Project Establishment Method 就机械重建需求基线。

正式过程由 `docs/methods/consumer-upgrade.md` 定义；人类说明见 `upgrading-agentic-dev.md`。

## 17. 如何理解 Skill 与 Rule

不要把它们理解成 `Skill → Rule` 固定流水线。

例如一次 Git / GitHub 操作：

- Skill 可以定义如何安全读取、执行、写后验证；
- Rule 可以定义当前仓库允许什么操作、commit message 如何表达、何时必须人工授权；
- 某些 Rule 即使没有对应 Skill 也仍然独立生效。

这使通用 procedure 可以复用，同时保留 Consumer-specific policy。

## 18. 当你想新增长期内容时

先问“它真正拥有哪类语义”：

- 当前项目使命、核心需求、capability instance、Roadmap 或稳定演进摘要 → Project；
- 一类复杂工作的阶段 / Gate / 完成模型 → Method；
- 可复用长期结构 / ownership / 不变量 → Architecture；
- 有界稳定执行能力 → Skill；
- 条件性 policy / constraint / default / invariant → Rule；
- 只是给人解释 → Guide；
- 只有证据和探索价值 → Research；
- 只是实施过程 / 当前一次 Gate → GitHub Issue / PR / Actions。

不要因为内容很重要、有步骤、文件很短、当前仓库正在使用或希望减少文件数量就决定类型。

## 19. 推荐阅读顺序

如果你第一次了解项目：

1. 本文；
2. `docs/project/README.md` 与 `project-charter.md`；
3. `docs/methods/README.md`；
4. `docs/architecture/README.md`；
5. `docs/rules/README.md`；
6. `skills/README.md`。

如果你要理解新软件 Consumer 从原始需求到 Feature 开发的完整关系，继续阅读：

1. `docs/methods/requirement-baseline-establishment.md`；
2. `docs/architecture/requirement-authority-architecture.md`；
3. `docs/guides/establishing-requirement-baseline.md`；
4. `docs/methods/architecture-clarification.md`（仅当存在 systemic architecture driver 时）；
5. `docs/methods/ai-development.md`；
6. 目标 Consumer 自己的 Project Capability Profile / Method selector 与 Requirement / Architecture Authority。

如果你只是使用已有稳定 Consumer 做普通开发，不需要每次重新阅读 upstream Guide 或重跑 Requirement Baseline Method；Consumer-local Repository Authority 应已经提供 Agent 所需入口。