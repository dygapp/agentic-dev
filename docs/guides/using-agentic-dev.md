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

## 4. 软件项目为什么需要两层 Clarification

普通软件开发并不总是从“需求已经足够明确，可以直接写 Specification”开始。

当多个当前或预期 Feature 共同依赖的长期 Requirement / Architecture Context 缺失、冲突或需要重建时，如果只在单个 Feature 内不断补洞，项目级事实很容易散落到局部 Specification、Technical Plan 或聊天上下文中。

`agentic-dev` 因此区分两类不同 work kind：

```text
Software Project Clarification
        ↓ 建立 / 重建长期本地上下文
Clarified Project Context Ready
        ↓ Repository 再选择具体 Feature / Change
AI Development
Clarify Intent
→ Specification
→ Technical Planning? ...
```

前者回答：

> 后续多个 Feature 可以共同依赖什么长期 Requirement / Architecture Context？

后者回答：

> 当前这个 Feature / change 具体做什么、如何规划并完成？

这两层不能互相替代，也不要求每个普通 Feature 都重新执行项目级澄清。

## 5. 什么时候使用 Software Project Clarification

`method:software-project-clarification` 面向普通软件 Consumer 项目的项目级或重大范围前置澄清。

典型适用场景包括：

- greenfield software project / new product，需要从原始输入建立初始 Requirement Authority；
- legacy modernization / rewrite，需要从旧系统、旧文档和当前决策中重建可信长期上下文；
- Requirement Authority 已碎片化、冲突或不足，多个 Feature 无法可靠进入 Specification；
- major domain / product boundary restructuring；
- 多个计划 Feature 共同被同一个尚未解决的长期 architecture driver 阻塞。

以下情况通常**不需要**进入该 Method：

- 普通单 Feature、bugfix、小范围变更；
- 已有稳定 Requirement / Architecture Context 下的日常开发；
- 只是技术复杂、文档很多，但长期上下文本身并没有缺失或冲突；
- `agentic-dev` 自身的 Method / Skill / Rule / Architecture capability evolution。

Method 存在于 upstream capability corpus，不等于 Consumer 自动采用。只有 Consumer 显式 adopt / adapt，并把相应 `work kind → Method` mapping 写入自己的 local selector 后，ordinary runtime 才能选择它。

## 6. Software Project Clarification 的四个阶段

正式生命周期为：

```text
Establish Context
→ Requirement Clarification
→ Architecture Clarification?（条件阶段）
→ Clarification Convergence
→ Clarified Project Context Ready
```

### Establish Context

先确定本次澄清的范围与证据边界：哪些是 current Authority，哪些只是 legacy、reference、analysis、conversation 或 unknown；同时确认长期 semantic owner 是否已经存在、是否冲突、是否需要重建。

目标不是建立完整 source catalog，而是避免把不同可信度、不同历史时期的材料平权混成当前事实。

### Requirement Clarification

处理 Problem / Behavior / Constraint / Acceptance 及其长期语义，典型工作包括：

```text
extract requirement facts
→ normalize ownership / terminology
→ detect gap / conflict / ambiguity
→ classify requirement / external / design
→ resolve high-impact unknowns
→ promote confirmed facts to durable Authority
→ cross-authority consistency check
```

关键点不是“多问需求问题”，而是让真正长期成立的事实进入 Consumer-local Requirement / Domain owner。

聊天、候选清单、比较表、流程图、分析报告等默认只是工作证据或派生视图；只要可以从 Authority 唯一再生，就不应自动成为第二套长期事实源。

### Architecture Clarification（条件阶段）

Architecture Clarification **已经作为新 Method 的 canonical 条件阶段整理出来**，但当前证据成熟度低于 Requirement Clarification。

它只在下面这种情况进入：

> 多个当前或预期 Feature / change 在进入可靠 Specification 前，共同依赖一个尚未解决的长期 architecture driver。

可能涉及：

- shared capability / shared contract；
- core data / system boundary；
- security / integration / deployment topology；
- high-cost-to-reverse structural decision；
- 成熟 reference implementation 能显著降低系统性探索成本；
- 多个局部实现已经显示出抽取 shared capability 的信号。

它的目标是把必须提前解决的长期结构问题放入真实 Architecture owner，而不是提前完成整个系统的技术设计。

因此以下内容仍留在 Feature Technical Planning / JIT Execution：

- 单个 Feature 的普通 HOW；
- 低影响、易逆的局部设计；
- 精确的类 / 函数 / 文件组织；
- 当前 Execution Unit 的施工步骤。

如果 Architecture Clarification 暴露出新的业务多解、Requirement conflict 或未定义 Product Boundary，应返回 Requirement Clarification；Architecture 不能自行创造 Product Requirement。

当前 v1 对 Architecture Clarification 只固化 **bounded、conditional、anti-BDUF** 的最小 contract。它还没有像 Requirement Clarification 一样获得完整的跨案例历史证据；后续应根据真实 Consumer 的正向、负向和演进型架构案例继续修订。

### Clarification Convergence

Convergence 不是检查“文档是否都写完”，而是确认后续 Feature Development 的输入是否已经可靠。

真正存在 blocker 时必须保持 NOT READY。只有长期 owner、关键 Requirement / Architecture 冲突、必要 semantic review 和剩余 non-blocking open item 都符合 Method Gate，才能声明：

```text
Clarified Project Context Ready
```

这个声明不等于已经创建 Specification、Execution Unit，也不授予 Execute / Integrate Authority。

## 7. Requirement Clarification、Specification 与 Technical Planning 的边界

可以用三层语义理解：

### Requirement / Domain Authority

拥有跨多个 Feature 持续成立的 Product / Domain 事实、规则、状态、边界、数据语义和重要约束。

### Feature Specification

拥有当前 change 的具体范围、可观察行为、失败行为与验收标准。它可以引用长期 Requirement / Domain Authority，但不应为了“自包含”复制整个项目基线。

### Technical Planning / Architecture

Feature-specific、可逆的实现 HOW 继续属于 Technical Planning。

只有跨多个 Feature、长期持续、且必须在可靠 Specification 前解决的 structural driver，才提升到项目级 Architecture Clarification；Technical Planning 与 Architecture Clarification 必须更新同一个长期 Architecture owner，不能形成平行 Authority。

如果普通 Feature 流程发现系统性长期缺口，应返回真实长期 owner 或项目级澄清责任；只有 Consumer-local selector 已采用并匹配 `method:software-project-clarification` 时，才进入完整 Method。upstream capability 的存在本身不构成隐式 adoption。

## 8. 普通 Feature / Change 如何工作

当 Consumer 已经拥有足够稳定的 local Requirement / Architecture Context 后，普通软件 / 产品变更继续使用 AI Development Method：

```text
Clarify Intent
→ Specification
→ Technical Planning?（条件阶段）
→ Slice & Ready
→ Execute
→ Converge
→ Ready to Integrate
```

`Clarify Intent` 只解决当前 Feature 会实质改变 Goal、Scope、Observable Behavior、Business Boundary、Acceptance 或重大非功能义务的高影响歧义，不重新分析整个项目。

Integration 本身不属于通用 Method；merge、release、deploy 等仍由目标仓库策略和人工 Authority 决定。

每个阶段可以使用对应 Skill，也可以在不需要独立 Skill 时由 Agent 直接按 Authority 工作。Rule 根据当前 phase / activity / technology / artifact / risk 独立发现，并不固定挂在某个 Skill 后面。

## 9. Clarification 当前没有新增 Skill / Rule / 固定 Artifact schema

新增 Software Project Clarification Method 不意味着同时为每个阶段创建 Skill。

当前没有足够证据证明 `requirement-analysis`、`architecture-framing` 等局部 procedure 已经跨 Consumer 稳定到值得独立 Skill；也没有为了新 Method 批量创建 Clarification Rules。

同样，Method 不要求一个固定的“Clarification Handoff”文档或统一目录结构。默认长期保存的是各自真实 semantic owner，例如 Requirement Authority、必要的 Domain / Terminology Authority、Architecture Context / State、条件性的 ADR；source inventory、ambiguity matrix、comparison table、flow/state view、review scratchpad 等默认属于 transitional / disposable artifact。

未来只有真实 Consumer Evidence 证明某个 procedure 或 policy gap 具有独立、稳定、可复用价值时，才评估新增 Skill / Rule。

## 10. Rule Discovery 为什么存在

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

## 11. Consumer 首次采用

首次采用不是复制整个仓库。大致过程是：

1. 恢复 Consumer 自己的 Project / Repository Authority；
2. 选择精确 upstream baseline；
3. 判断哪些 Method / Architecture / Skill / Rule / Tool contract 需要 adopt / adapt / reject；
4. 把接受的 capability 写入 Consumer-local canonical owner；
5. 建立 Consumer 自己的 capability profile / Method selector / Skill / Rule discovery；
6. 验证 ordinary runtime 不在线依赖 upstream；
7. 记录 evaluated baseline。

对于 `software-project-clarification`，Consumer 只有在确认自身确实存在对应 work kind 时才建立 local selector mapping；不能因为 upstream inventory 中出现该 Method 就自动注册。

upstream Project Charter / Capability Profile / Roadmap / Evolution 只用于 provenance / understanding，不复制为 Consumer Project state。

正式过程由 `docs/methods/consumer-adoption.md` 定义；人类操作说明见 `adopting-agentic-dev.md`。

## 12. Existing Consumer 升级

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

Consumer-local Rule 可以继续保持本地差异，例如不同仓库拥有不同 Git commit type / scope。upstream Project state 不属于 upgrade synchronization object。

如果 upstream 新增 `software-project-clarification`，Existing Consumer 也应先评估自己是否存在该 work kind、现有 Requirement / Architecture Authority 是否已经通过其他本地方式承担同等责任，再决定 adopt / adapt / reject；不能仅因为 baseline 更新就改变 ordinary Feature runtime。

正式过程由 `docs/methods/consumer-upgrade.md` 定义；人类说明见 `upgrading-agentic-dev.md`。

## 13. 如何理解 Skill 与 Rule

不要把它们理解成 `Skill → Rule` 固定流水线。

例如一次 Git / GitHub 操作：

- Skill 可以定义如何安全读取、执行、写后验证；
- Rule 可以定义当前仓库允许什么操作、commit message 如何表达、何时必须人工授权；
- 某些 Rule 即使没有对应 Skill 也仍然独立生效。

这使通用 procedure 可以复用，同时保留 Consumer-specific policy。

## 14. 当你想新增长期内容时

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

## 15. 推荐阅读顺序

如果你第一次了解项目：

1. 本文；
2. `docs/project/README.md` 与 `project-charter.md`；
3. `docs/methods/README.md`；
4. `docs/architecture/README.md`；
5. `docs/rules/README.md`；
6. `skills/README.md`。

如果你要理解普通软件 Consumer 从项目前置澄清到 Feature 开发的完整关系，继续阅读：

1. `docs/methods/software-project-clarification.md`；
2. `docs/methods/ai-development.md`；
3. 目标 Consumer 自己的 Project Capability Profile / Method selector 与 Requirement / Architecture Authority。

如果你只是使用现有 Consumer 做普通开发，不需要每次重新阅读 upstream Guide 或 upstream Project Knowledge；Consumer-local Repository Authority 应已经提供 Agent 所需入口。