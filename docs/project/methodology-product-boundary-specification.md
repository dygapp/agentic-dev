---
id: project:methodology-product-boundary-specification
type: project
status: active
distribution: source-only
---

# AI 驱动软件开发方法论产品边界重构规范

## 1. 文档职责

本文是下一轮 `agentic-dev` 产品边界与方法论架构重构的项目级规范与验收 Authority。

本文只拥有本轮重构的：

- 问题定义与适用域；
- 目标产品模型；
- Provider / Consumer 边界；
- Guide、Skill、Consumer-local knowledge / rule 的职责边界；
- 新项目 Bootstrap 与已有项目 Adoption 的目标体验；
- 上下文与平台适配约束；
- 旧发布模型的退出边界；
- 重构验收条件。

本文**不**定义具体实施顺序、文件删除清单、迁移脚本、PR 拆分或测试命令。只有本文经过独立复核并冻结后，才根据最终目标模型制定实施方案。

## 2. 本轮重审的根本问题

`agentic-dev` 最初目标是提供一整套面向**软件项目**的 AI 驱动开发方法论。

历史演进中，项目逐步引入 Method、Architecture、Rule、Skill、Guide、Project Capability Profile、Rule Discovery 与 Distribution Build 等结构。部分结构解决了真实问题，例如：

- 大型 Guide / Prompt 全量加载导致上下文膨胀；
- 项目级约束不能全部堆入 `AGENTS.md`；
- Fresh Context 需要从 Repository 恢复事实；
- Consumer-local Requirement、Architecture、技术政策与授权不能被 upstream 覆盖；
- 高影响工作需要可靠 Evidence 与独立复核。

但同时出现两个相互强化的适用域扩张：

1. 面向软件 Consumer 的方法论，被逐步扩展为同时治理 `agentic-dev` Provider 自身的统一 Capability Runtime；
2. Provider 内部为了设计和治理能力而形成的 Method / Architecture / Rule，被逐步提升为需要参与 Consumer runtime / distribution 的一等模型。

结果是原本可以由 Guide + Skill + Consumer-local Authority 解决的问题，需要额外维护：

- Capability 类型体系；
- Method selector；
- Project Capability Profile；
- Rule Discovery runtime；
- Source / Distribution classification；
- Release composition / transformation；
- custom Release Builder / installer；
- Source semantic owner 到 Consumer Skill package 的编译关系。

本轮目标不是否定这些机制曾解决的真实问题，而是：

> **保留经过实践验证的需求，删除因为 Provider / Consumer 同构和统一 Capability Runtime 假设而产生的派生复杂度。**

## 3. 项目适用域

### 3.1 目标对象

`agentic-dev` 的方法论目标对象是：

> **使用 AI Agent 进行需求、设计、实现、验证、复核和收敛的普通软件项目。**

它不是“所有类型项目的通用 AI 治理体系”。

### 3.2 Provider 不要求与 Consumer 同构

`agentic-dev` 本身是研发、验证和维护该方法论与 Skills 的 Provider Repository。

Provider 可以根据自身研发需要使用：

- `AGENTS.md`；
- `docs/**`；
- `tools/**`；
- `evals/**`；
- `tests/**`；
- 其他真正服务本仓维护的治理资产。

但不得因为某项 Consumer-facing 方法论能力存在，就推导出 `agentic-dev` 自身必须完整运行同一套 Consumer runtime。

Provider 可以测试自己的 Skills；**测试产品不等于由产品反向治理 Provider。**

## 4. 方法论的产品定义

重构后的完整 AI 驱动软件开发方法论由三部分共同形成：

1. **Guide / Knowledge Navigation**：帮助人和 AI 理解怎么开始、当前处于什么状态、下一步通常应该做什么，以及 Skills 如何组合；
2. **Skills**：提供真正可执行、可发现、有边界的软件开发能力；
3. **Consumer-local Project Knowledge / Constraints**：由目标软件项目持有自身 Requirement、Architecture、Current Work、技术政策、授权和项目级规则。

其中：

> **`skills/**` 是 `agentic-dev` 唯一正式的 Consumer-facing runtime product。**

Guide 是方法论知识与导航资产，但默认不是需要安装到 Consumer 的独立 runtime namespace。

Method、Architecture、Rule 等概念可以继续作为 `agentic-dev` 内部研发、分析和治理语言存在，只要它们对 Provider 有真实价值；它们不再因为“是一等 Source 类型”而获得 Consumer distribution 身份。

## 5. 第 0～4 层目标模型

下列“层”只描述**责任与加载方式**，不是新的 Capability ontology，也不得因此重新建立一套 Runtime Type System。

### 第 0 层 — Host Adapter，可选

用于特定宿主平台把 Agent 带入正确 Repository。

典型例子是 ChatGPT Project Instructions：

```text
目标 Repository
→ 使用 WebCodex / Repository Runtime
→ 读取当前 AGENTS.md
→ 后续由 Repository Authority 接管
```

约束：

- 只解决“怎样进入项目”；
- 不保存当前 Gate、Issue、Requirement、Architecture 或其他项目事实；
- Codex Work、codex-cli 等已经天然处于 Repository Context 的执行面不要求这一层；
- 换宿主平台可以拥有不同 Adapter，但从 `AGENTS.md` 开始重新汇合。

### 第 1 层 — Repository Bootstrap

主要载体是 Consumer 自己的 `AGENTS.md`。

职责：

- 说明 Repository Authority；
- 指向项目知识的稳定入口；
- 说明怎样发现 / 使用已安装 Skills；
- 说明怎样获取 Consumer-local constraints；
- 保持短、小、稳定。

不得把完整方法论、全部本地规则、当前工作流水账或大型 Guide 塞进根 `AGENTS.md`。

### 第 2 层 — Knowledge / Navigation

包括：

- `agentic-dev` Guides；
- Consumer 自己的 Requirement、Architecture、Project Knowledge、Current Work 等项目文档。

它回答：

> **现在应该做什么，以及为什么？**

Guide 同时服务人和 AI，但采用**按需读取**，不是 ordinary runtime 的固定全量输入。

Consumer 项目事实始终由 Consumer-local 文档拥有；Guide 只能提供判断框架、使用说明和方法导航，不得覆盖项目事实。

### 第 3 层 — Execution

由 `skills/**` 提供。

它回答：

> **这件事具体怎么做？**

每个 Skill 必须具有清晰 Trigger / Purpose、Inputs、Procedure、Outputs / Completion、Exit / Escalation，并携带完成其通用责任所需的 references / scripts / assets。

Skill 不得依赖安装时再从 Provider 的 Method / Architecture / Rule tree 动态编译运行语义。

### 第 4 层 — Local Constraints

由 Consumer 自己拥有的项目级 rules / policies / constraints 构成。

它回答：

> **在这个项目里做这件事时，有什么特殊约束？**

例如：

- 技术栈约束；
- 数据迁移约束；
- 安全与权限约束；
- 代码结构约束；
- 验证要求；
- 部署 / 外部操作政策；
- 项目级术语或审批规则。

这些约束不得全部堆入 `AGENTS.md`，也不得因为多个 Consumer 都可能需要“规则”就自动升级成 upstream Rule Runtime。

## 6. Guide 的重新定位

### 6.1 Guide 不是 Human-only

历史上把 Guide 限定为 Human View，虽然降低了 ordinary Agent 上下文成本，但同时损失了 Guide 作为 AI 方法论知识库和导航层的价值。

新的原则是：

> **Guide 面向人，也面向需要理解方法论、Bootstrap、规划下一步或解释整体工作路径的 AI。**

### 6.2 Guide 不是常驻 Runtime

Guide 可供 AI 使用，不等于每次执行都自动加载。

默认：

- Bootstrap 时按需读取；
- 用户询问“怎么开始”“下一步做什么”“这个方法怎么用”时按需读取；
- 具体实现任务不默认加载整个 Guide corpus；
- Guide 数量增长不得线性增加 ordinary task context。

### 6.3 Guide 不成为第二套执行 Authority

Guide 可以：

- 解释方法论；
- 描述典型流程；
- 帮助选择下一类工作；
- 提供人类可理解的示例；
- 指向对应 Skills。

Guide 不应：

- 维护与 Skill 不一致的执行步骤；
- 保存 Consumer 当前项目事实；
- 成为必须与 Skill 逐字段同步的第二套 procedure；
- 充当隐藏 Method selector / Rule engine。

Bootstrap 是一个明确的**预 Consumer runtime 入口例外**：在目标 Repository 尚未建立、已安装 Skills 尚不可用之前，Bootstrap Guide 可以拥有完成最小项目澄清、创建 Consumer-owned 初始 Repository、安装 Skills 和建立方法论 locator 所需的有界编排。这个例外只存在于“创建 Consumer runtime”之前；Bootstrap 完成后，能够独立复用的执行 procedure 仍由 Skill 持有，Guide 不得复制已有 Skill 的执行 contract。

## 7. Skills 作为唯一 Consumer runtime 产品

### 7.1 Canonical Skill

重构完成后，`skills/<name>/**` 本身就是该 Skill 的 canonical installable package。

Consumer 所需的通用运行语义直接维护在：

```text
skills/<name>/
├── SKILL.md
├── references/**
├── scripts/**
└── assets/**
```

不得继续使用：

```text
Method / Architecture / Rule
→ distribution classification
→ Release Build transformation
→ generated Skill package
```

作为正常发布路径。

### 7.2 标准安装体验

目标安装体验应尽量符合 Agent Skills 生态：

```text
GitHub Repository / exact tag
→ standard Skills-compatible installer
→ Consumer-local Skill installation
```

用户或 Agent 应能够从 `dygapp/agentic-dev` 的 GitHub Repository / 精确版本定位可安装 Skills，而不必理解 Provider 的内部 Source Model。

除非后续 Evidence 证明不可替代，不建立自定义包管理体系、独立 ZIP 语义编译层或必须先执行 Provider Release Builder 才能得到真实 Skill 的模型。

### 7.3 验证复杂度可以保留

简化 Distribution 不等于降低质量要求。

仍可保留严格的：

- Skill schema / metadata validation；
- reference / script 完整性；
- deterministic tests；
- Runtime acceptance；
- Fresh Context；
- negative controls；
- authenticated Codex behavior；
- Consumer fixture；
- representative behavior eval。

原则是：

> **验证可以严格，安装模型保持简单。**

## 8. Consumer-local Project Knowledge

Consumer 始终拥有：

- Product / Domain facts；
- Requirement；
- Specification；
- System Architecture；
- ADR；
- technology policy；
- authorization；
- Current Work / Roadmap；
- code / tests / verification；
- 项目自己的 Guides / Rules / Policies。

`agentic-dev` 不为所有 Consumer 强制同一物理目录，但可以通过 Guide 或 Skill提供推荐结构。

项目事实不得为了让通用 Skill“自包含”而被复制到 upstream 或长期塞入 Skill。

## 9. Consumer-local Rules / Policies

### 9.1 需求边界

本轮冻结以下需求：

- 项目级规则不能全部进入根 `AGENTS.md`；
- 项目级规则不能被 upstream 通用 Skill 吸收；
- 规则数量增长时不能要求 AI 默认全量加载；
- 规则由 Consumer 自己拥有；
- AI 应在适用任务发生时能够找到需要的项目约束。

### 9.2 不预设复杂实现

本规范不提前规定必须继续使用当前五维 Rule metadata、Rule Discovery Tool、Capability Profile 或 GitHub Actions discovery transport。

后续设计应优先验证更简单的组合是否足够，例如：

- 极少量 repository-wide 稳定约束放在根 `AGENTS.md`；
- path / module scoped 约束利用 nested `AGENTS.md` 或宿主原生 scoped instructions；
- activity / semantic scoped policy 使用 Consumer-local 文档与轻量 locator / metadata；
- 某个 Skill 在执行时读取 Consumer 声明的本地约束入口。

只有真实项目证明简单方案无法可靠满足按需发现，才允许重新引入更复杂机制。

## 10. 新项目 Bootstrap

新项目 Bootstrap 是 `agentic-dev` 方法论的一等入口。

目标用户体验：

```text
用户提供：
- agentic-dev GitHub 地址
- 新软件项目的基本情况

AI：
→ 找到 Getting Started / Bootstrap Guide
→ 进行最小化谈判式澄清
→ 确认项目目标、主要使用方、核心范围、明确非目标、已知约束和真实阻塞歧义
→ 建立 Consumer-owned 初始 Repository
→ 安装 agentic-dev Skills
→ 建立最小 AGENTS.md 与必要项目文档
→ 给出下一步方法导航
```

Bootstrap 不要求用户先理解 Method、Rule、Architecture、Capability Profile 等 Provider 内部概念。

谈判式澄清应遵守：

- 能从用户输入直接确认的事实不重复询问；
- 能安全推导的内容先形成候选；
- 普通可逆设计不升级成人工 Product 问题；
- 只有会实质改变项目目标、范围、关键业务边界或长期高成本约束的歧义才请求人工决定；
- 在达到足够建立初始 Repository 的最低阈值后及时停止问答。

Bootstrap 的完成边界是：Consumer-owned Repository 已建立，最小 `AGENTS.md` / 项目知识入口可恢复，所需 Skills 已安装且可发现，并已建立一个指向所采用 `agentic-dev` 精确版本 Guide 入口的薄方法论 locator。到达该边界后，Bootstrap Guide 的预运行时编排结束，普通项目工作切换到 Consumer Repository Authority + installed Skills + Consumer-local constraints。

## 11. 已有项目 Adoption

Existing Project 默认采用最小侵入策略：

```text
Existing Repository
→ 恢复当前 Repository Authority
→ 安装 agentic-dev Skills
→ 进行必要的最小 Bootstrap integration
→ 验证 Skills 可发现 / 可执行
→ 开始使用
```

以下工作默认是**可选治理 / remediation**，不得作为采用 agentic-dev 的强制前置条件：

- 全仓文档重构；
- Requirement Authority 重建；
- Architecture Authority 重建；
- 历史文档清理；
- 目录结构统一；
- Consumer-local Rule 体系重构；
- 大规模项目治理升级。

只有当前 Repository 的真实问题证明这些工作必要时，AI 才建议并在得到相应 Authority 后执行。

## 12. “下一步做什么”作为正式方法论入口

完整方法论必须支持用户直接询问：

> “根据当前项目情况，下一步应该具体做什么？”

AI 的判断来源应是：

```text
Consumer current project facts
+
按需方法论 Guide
→ 判断当前主要缺口 / 下一责任
→ 选择对应 Skill
→ 执行时叠加 Consumer-local constraints
```

不得在没有项目事实和方法导航的情况下，仅凭模型一般经验随机选择工作。

Guide 提供判断框架，Consumer Repository 提供事实，Skill 提供执行能力，Consumer-local rules 提供项目约束。

## 13. Guide 在长期 Consumer 中的可达性

普通执行不得隐式依赖 upstream current state，但 AI 在明确的方法论咨询 / Bootstrap / 导航场景中需要能够获得 Guide。

默认方案冻结为**Consumer-local 薄 locator + 精确版本 Guide 按需读取**：

1. 新项目 Bootstrap 与 Existing Project Adoption 都建立一个 Consumer-owned 薄方法论 locator；
2. locator 只记录所采用 `agentic-dev` 的精确 Repository / tag 或等价不可歧义 ref，以及 canonical Guide 入口，不复制完整 Guide 正文；
3. 只有用户明确请求“怎么开始”“下一步做什么”“这个方法怎么用”等方法论咨询，或 Bootstrap / Adoption 本身需要 Guide 时，AI 才按 locator 读取对应精确版本 Guide；
4. 普通实现、验证、复核等任务继续只依赖 Consumer-local Authority、installed Skills 与当前必要项目知识，不把 upstream Guide 变成隐式 runtime dependency；
5. 精确 Guide source 不可访问时 fail closed：报告方法论导航不可用或请求恢复该精确来源，不回退 `latest`、模型记忆或其他版本 Guide。

该 locator 的具体物理位置由 Consumer Bootstrap 设计决定，可以进入保持有界的 `AGENTS.md` 区块或等价稳定项目入口；不得因此新增独立 Guide Runtime、复制完整 Guide corpus，或恢复“每次启动全量加载”。

## 14. Guide 与 Skill 的 Authority 边界

为了避免双重 Authority：

- Guide 负责解释、导航、组合关系、典型路径和“何时考虑哪类工作”；在 Consumer runtime 尚未建立时，仅 Bootstrap Guide 可以承担 §6.3 定义的有界预运行时编排；
- Skill 负责 Consumer runtime 中可独立复用的执行 contract / procedure；
- Consumer Project Knowledge 负责当前项目事实；
- Consumer-local Rule / Policy 负责项目特殊约束。

当 Guide 与 Skill 对同一可执行 procedure 出现冲突时，说明模型发生漂移，必须修复；不得通过“两个都算 Authority”解决。

## 15. 平台适配边界

ChatGPT + WebCodex 可以使用可选的第 0 层 Project Instructions，负责：

- 指定目标 Repository；
- 指定通过 WebCodex / Repository Runtime 进入；
- 要求先读取 Repository `AGENTS.md`；
- 明确外部会话状态不是 Repository fact。

Codex Work / codex-cli 等已经运行在 Repository Context 中时，直接从 `AGENTS.md` 开始，不需要第 0 层。

方法论不得因为支持某个宿主平台，把该平台的 Project Instructions、Connector、CLI transport 或认证机制提升为所有 Consumer 的通用 Runtime 前提。

## 16. 上下文控制

重构后仍必须保持 Progressive Disclosure：

- 不默认加载全部 Guides；
- 不默认加载全部 Skills；
- 不默认加载全部 Consumer-local Rules；
- 不默认加载完整 Project history；
- 不把“AI 可以读取”误写成“AI 每次都必须读取”。

上下文优化优先通过正确的入口、按需加载和职责边界解决，而不是通过增加更多中间 Runtime 类型解决。

## 17. 旧发布模型的退出边界

当前 Issue #172 路线产生的 Gate A～G、Release Candidate、Runtime Acceptance、Legacy Consumer Coverage Audit 等结果保留为历史 Evidence。

但新的产品边界确认后：

- 不继续执行原 Gate H；
- 不把现有 RC 安装到真实 `dygapp/jilinjobs-cms`；
- 不 force-move / rewrite 已存在的 RC tag；
- 不删除能够解释历史决策和验证结果的 Git / Issue / PR / Actions Evidence；
- 不为了“复用已有投入”继续要求新模型兼容 custom Release Builder / ZIP / composition framework。

此外，Repository-wide asset disposition 必须显式覆盖冻结 RC source tag `agentic-dev-v0.0.0-rc.1` 相对当前已集成基线的 **RC-only delta**。这些尚未进入 `master`、但已经参与 Gate G / Runtime Evidence 的语义和测试不得因为终止旧 Gate H 被整体丢弃；每项 candidate-only change 必须给出 `retain`、`adapt` 或 `drop-with-reason` disposition。该审计不授予整分支合并或继续旧 Release Framework 的权限。

旧 `docs/project/distribution-rebuild-specification.md` 退出 Current Authority，由本文接管新的目标模型；旧文档保留为历史规范与 Evidence locator。

## 18. 反过度设计约束

发现一个新需求时，不得立即新增：

- 一级 Capability type；
- Method runtime；
- Rule runtime；
- Discovery Framework；
- Distribution namespace；
- Release transformation；
- 中央 Registry / Catalog。

新增复杂机制前必须先证明以下已有构件无法合理解决：

```text
AGENTS.md
+
Guides / Project docs
+
Skills
+
Consumer-local lightweight policy
```

设计目标不是建立新的“V5 Capability Model”，而是证明最小产品模型已经足够。

## 19. 验收条件

### 19.1 目标域与产品边界

- `PB-AC-01`：项目明确面向普通软件开发项目，不再以所有类型项目的统一 AI Governance 为默认目标。
- `PB-AC-02`：`agentic-dev` Provider 不再因为 Consumer capability 存在而被要求完整 self-adopt 同一 Consumer runtime。
- `PB-AC-03`：`skills/**` 被确立为唯一正式 Consumer-facing runtime product。
- `PB-AC-04`：Method / Architecture / Rule / Guide 的 Provider 内部存在不再自动产生 Consumer distribution identity。
- `PB-AC-05`：目标模型不要求 Source semantics 经过 distribution classification / transformation 才能形成真实 canonical Skill。

### 19.2 Guide / Navigation

- `PB-AC-06`：Guide 明确同时服务人和 AI 的按需方法理解、Bootstrap 与导航。
- `PB-AC-07`：Guide 不作为 ordinary task 的固定全量输入。
- `PB-AC-08`：除 §6.3 的预 Consumer Bootstrap 有界编排外，Guide 不复制或竞争 Skill procedure，也不成为 Consumer project fact 或项目规则的第二套 Authority。
- `PB-AC-09`：存在明确方式支持“根据当前项目状态，下一步应该做什么”的方法论导航。
- `PB-AC-10`：长期 Consumer 的 Guide 可达性方案明确且不会恢复持续 upstream runtime dependency 或全量 Guide copy。

### 19.3 Bootstrap / Adoption

- `PB-AC-11`：新项目可以从“agentic-dev GitHub 地址 + 基本项目情况”进入最小谈判式 Bootstrap。
- `PB-AC-12`：Bootstrap 能建立 Consumer-owned `AGENTS.md`、必要项目知识入口和 Skills，而不要求用户理解 Provider 内部 Capability 类型。
- `PB-AC-13`：Existing Project 默认采用最小侵入安装路径。
- `PB-AC-14`：全仓治理、Requirement / Architecture rebuild、历史清理和规则体系重构均保持按需可选，不成为 Adoption 固定前置。

### 19.4 Consumer-local knowledge / constraints

- `PB-AC-15`：Consumer Requirement、Architecture、Current Work、技术政策、授权与其他项目事实继续由 Consumer 自己拥有。
- `PB-AC-16`：Consumer-local Rules / Policies 不要求全部进入根 `AGENTS.md`。
- `PB-AC-17`：项目级约束可以按需加载，但第一版不预设必须复制当前完整 Rule Discovery Runtime。
- `PB-AC-18`：Consumer-local constraint 发现机制只有在简单机制经 Evidence 证明不足后才能增加复杂度。

### 19.5 安装、执行与验证

- `PB-AC-19`：每个正式 Skill package 对其通用执行责任自包含，不依赖在线回读 Provider Method / Architecture / Rule tree。
- `PB-AC-20`：支持从 GitHub Repository / 精确版本通过标准 Agent Skills 兼容方式安装 Skills；自定义 ZIP / Builder 不作为普通安装必要前提。
- `PB-AC-21`：普通 Consumer 执行不因 Skill 信息缺口隐式回退到 upstream current state。
- `PB-AC-22`：Codex Work / codex-cli 不依赖 ChatGPT Project Instructions；ChatGPT + WebCodex 可通过可选第 0 层进入相同 Repository Bootstrap。
- `PB-AC-23`：严格 deterministic / runtime / Fresh Context / negative-control / Consumer fixture 验证能力可继续支撑 Skills 产品质量。

### 19.6 历史迁移与收敛

- `PB-AC-24`：现有 Skills、Guides、Methods、Architectures、Rules、Tools、Evals 与 Release infrastructure 完成逐项 disposition，不按目录机械删除。
- `PB-AC-25`：历史 Consumer coverage Evidence 用于证明新模型没有丢失必要软件开发责任。
- `PB-AC-26`：现有 Gate G RC 被保留为历史 Evidence，不再进入原 Gate H 真实 Consumer migration。
- `PB-AC-27`：旧 Distribution Specification 退出 Current Authority，不与本文形成长期双重 truth。
- `PB-AC-28`：本文通过独立高影响语义复核后，才允许制定并执行 Repository 重构方案。
- `PB-AC-29`：Repository-wide asset disposition 显式覆盖冻结 RC source tag `agentic-dev-v0.0.0-rc.1` 的 RC-only delta，所有 candidate-only 语义 / 测试均有 `retain`、`adapt` 或 `drop-with-reason` 处置，不因放弃旧 Release Framework 静默丢失。

## 20. Specification 复核重点

独立复核必须主动寻找以下反例：

1. 是否存在重要的软件开发责任无法归入第 0～4 层；
2. 是否存在必须把 Method / Architecture / Rule 作为独立 Consumer runtime type 才能安全解决的真实场景；
3. Guide + Skill 是否会形成不可避免的双重 Authority；
4. 新项目 Bootstrap 是否能够在有限人工交互下真正建立可继续工作的 Repository；
5. Existing Project 是否能够不经过大规模治理重构就获得有效 Skills；
6. Consumer-local rules 是否可以在不恢复当前复杂 Rule Runtime 的情况下可靠按需应用；
7. `AGENTS.md` 是否能够保持足够薄；
8. 不依赖第 0 层时 Codex Work / codex-cli 是否仍可完整工作；
9. 标准 GitHub Skills 安装路径是否足以表达版本、更新与可验证 provenance；
10. 是否有任何现有复杂机制仍然具有无法由更简单模型替代的必要性。
11. 冻结 RC 相对当前 `master` 的 candidate-only delta 是否全部进入后续 disposition，而不是随着旧 Gate H 终止被遗漏。

发现关键反例时先修改本文，不进入实现。

## 21. 下一阶段

本文候选完成后，顺序固定为：

```text
Specification candidate
→ Independent Semantic Review
→ Specification freeze
→ Repository-wide asset disposition
→ 具体实施方案
→ 实施 / 验证
→ 真实 Consumer adoption validation
```

在 Specification freeze 之前：

- 不删除现有 Capability / Distribution 资产；
- 不修改 `jilinjobs-cms`；
- 不继续旧 Gate H；
- 不把讨论结论提前写成最终 Implementation Architecture。
