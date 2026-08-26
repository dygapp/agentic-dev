# 使用 agentic-dev

本文说明 AI Agent 或开发者如何把 `agentic-dev` 作为方法与 Skills 知识源，用于启动并持续推进真实软件项目。

本文是使用指南（Operating Guide），不重新定义方法（Method）、架构（Architecture）或 Skill 契约（Skill Contract）。发生冲突时，以目标项目自己的仓库权威（Repository Authority）与 `agentic-dev` 的权威层级为准。

## 1. 使用模型

`agentic-dev` 提供三类可复用资产：

- **方法（Method）**：软件开发过程中的阶段、边界、证据和上下文原则；
- **Skills**：执行特定职责的可组合能力；
- **使用指南（Operating Guide）**：说明如何在真实项目中使用 Method 与 Skills。

目标项目仍然拥有自己的项目规则（Project Rules）、需求（Requirements）、架构（Architecture）、代码（Code）、测试（Tests）与集成策略（Integration Policy）。

```text
agentic-dev
Method + Skills + Operating Guide
        │
        │ reusable guidance
        ▼
Consumer Repository
Project Rules + Project Knowledge + Code
```

`agentic-dev` 不替目标项目预定义完整目录、技术栈、文档体系或治理结构。

## 2. 开始前的知识边界

启动一个项目时，Agent 应先明确当前允许使用的权威输入。

至少区分：

1. `agentic-dev` 仓库：提供可复用 Method、Skills 与 Operating Guide；
2. Consumer Repository：提供并逐步形成当前项目自己的 Authority；
3. 当前明确提供的业务 / 产品需求来源；
4. 当前运行环境（Runtime）可直接观察到的能力和状态。

不得把以下内容直接当作目标项目事实：

- 其他聊天中的未固化结论；
- 其他项目的规则；
- 个人记忆或隐含经验；
- `agentic-dev` 中只属于该仓库自己的 Project Rule。

`agentic-dev` 可以指导“如何工作”，但不能替 Consumer Repository 决定“这个项目的事实是什么”。

### 2.1 需求来源与 Consumer 权威

外部提供的需求来源（Requirement Source / Input Material）不会因为被读取、复制到仓库，或自身标记为 `confirmed`、`approved` 等状态，就自动成为 Consumer Repository 的项目权威。

启动或接收需求资料时，Agent 应区分：

```text
Requirement Source / Input Material
        │
        │ explicit adoption into Consumer Authority
        ▼
Consumer Authoritative Requirement
        │
        │ clarified intent + authority
        ▼
Specification
```

其中：

- **需求来源（Requirement Source / Input Material）** 是当前允许用于理解项目的来源资料，可以来自外部文件、其他 Repository、URL、已有系统说明或人工提供的输入；
- **Consumer 权威需求（Consumer Authoritative Requirement）** 是已经被当前 Consumer Repository 明确采纳，并在当前范围内作为项目事实和后续验收依据使用的需求；
- **规格说明（Specification）** 继续由已澄清意图（Intent）与当前 Consumer Authority 收敛形成 WHAT / WHY 权威，不等同于原始来源资料的简单复制。

Greenfield bootstrap 不要求为了表示上述区分而创建固定目录或额外文档，但在把来源资料纳入 Consumer Authority 前，应至少判断：

- **来源关系（Provenance）**：来源是什么，是否需要保留来源关系；
- **当前有效范围（Active Scope）**：来源整体范围与当前 Consumer iteration 的有效范围是否一致；
- **权威优先级（Authority Precedence）**：采纳后它在当前 Repository Authority 中处于什么位置；
- **上游引用（Upstream References）**：来源文件引用的上游规则、需求、架构或项目文档在 Consumer Repository 中是否真实可用。

如果来源文件包含 Consumer Repository 中不存在或未被采纳的 upstream references：

- 不得把这些引用自动视为当前 Consumer Authority；
- 可以保留其 provenance，但应在当前 Repository Authority 中明确其有效边界；
- 只有当前项目确实需要相应长期事实时，才建立或采纳 Consumer-local Authority；
- 不为了让引用“看起来完整”而机械复制整个上游项目的文档体系。

如果某份来源资料已经被人工明确指定为当前 Consumer 的权威需求，可以直接采纳，不要求重复进行形式化审批；但仍应处理当前 Scope、Authority Precedence 与不可解析 upstream references，避免 Fresh Agent 混淆“来源整体语义”和“当前 Consumer 中实际有效的权威”。

## 3. Greenfield Project：建立最小启动骨架

新项目不应从大而全的模板开始。

目标是先建立**足以让 Fresh Agent 正确继续工作的最小仓库权威（Repository Authority）**，然后随真实需求逐步演进。

通常需要先明确：

- 项目目标与当前范围；
- Repository Authority / Knowledge Boundary；
- 当前允许 Agent 自主处理与必须升级给人工的边界；
- 项目是否需要可跨里程碑、阶段或 Fresh Context 恢复的项目路线图（Project Roadmap）；
- 基本验证与集成策略（Verification / Integration Policy）；
- 当前 Requirement / Specification 应保存在哪里；
- 当前项目文档需要遵循的主导语言规则（如已有）；
- 当前实际需要使用的 Skills。

一个小型 Greenfield 项目的初始骨架可以很轻，例如：

```text
<consumer>/
├── AGENTS.md
├── README.md
└── <当前真正需要的项目 Artifact>
```

这只是最小示例，不是固定模板。

如果项目预计会跨越多个里程碑、方法阶段或 Fresh Context，且仅凭当前 Feature / Task Artifact 无法可靠恢复整体路线，应在初始化时建立一个薄的项目路线图。初始内容只需明确：

- 已知项目目标与初步路线；
- 已完成、当前、下一步、条件性和未知部分；
- 当前阶段与当前核心目标；
- 触发路线更新的项目级变化；
- Fresh Agent 应继续读取的权威入口。

可以使用 `docs/project/project-roadmap.md` 等一眼可识别的名称，但 Consumer Repository 可以选择其他可发现载体。README 只链接到当前路线，不并行复制易变化的详细状态。对于小型、一次性或仅含单一局部工作的项目，不要为了套用模板创建项目路线图。

如果 Consumer Repository 尚未明确自然语言规则，人类可读的项目文档默认应沿用当前权威需求与主要项目协作输入的主导语言，避免把 `agentic-dev` 自身或某个 Runtime 的语言习惯无意复制到目标项目。

语言选择是 Consumer Project Rule，而不是 `agentic-dev` Method 约束：

- 不强制翻译 Method 专有术语、代码标识、文件路径、命令、协议名和专有名词；
- 如果语言选择对后续 Fresh Agent、人工复核（Human Review）或长期协作具有持续价值，应在最小 Repository Authority（例如 `AGENTS.md`）中显式固化；
- 如果 Consumer 已经存在明确语言规则，始终以 Consumer Authority 为准。

不要为了“看起来完整”预先创建空的：

- architecture 体系；
- decisions 体系；
- tasks / plans 体系；
- 大量阶段目录；
- 未被当前工作需要的配置或 Skills。

当真实工作产生长期价值时再新增相应产物（Artifact）。

例如：

- Specification 确认的业务术语、不变量或跨功能规则需要被后续多个工作持续消费时，再按 Consumer Repository Authority 形成或更新 Domain / Requirement Authority；
- 出现需要跨执行单元（Execution Units）长期协调的 HOW，再持久化技术计划（Technical Plan）；
- Technical Planning 改变跨功能持续有效的系统结构、组件 / 数据 / 契约边界或集成 / 部署约束时，更新适当的 Architecture Authority；
- Architecture Context 中的重要决定只有在保留选择理由、主要权衡或替代关系具有持续价值时，才形成或更新 ADR / Architecture Decision Artifact；
- 不为了“项目应该有 ADR”预建固定 `adr/` 目录、空 ADR 或统一模板；
- 当项目演进首次满足跨里程碑 / 阶段 / Fresh Context 的长期恢复条件时，再建立或补齐 Project Roadmap；
- 工作复杂到需要跨 Fresh Context 协调时，再建立临时 Plan / Coordination Artifact；
- 进入实现阶段后，再按实际技术栈创建源码、测试与构建结构。

原则是：**Project Structure follows durable need.**

## 4. 使用 Skills

第一批核心 Skills 位于：

```text
skills/
├── clarify-intent/
├── specify/
├── technical-plan/
├── slice-work/
├── readiness-check/
├── execute-unit/
├── systematic-debug/
└── converge/
```

除第一批核心 Skills 外，仓库还可以基于真实 Consumer Evidence 提供**平台专项非核心 Skill**。这类 Skill 只在当前 Repository / Runtime 实际满足触发条件时加载，不成为所有项目的默认依赖，也不得覆盖 Consumer Repository Authority。

当前已经形成的代表性能力：

- `github-actions-verification`：当 Consumer 使用 GitHub Actions 取得验证证据，且 Branch / PR trigger、CI 可观察性、验证分层、容器化 Runtime、Artifact 复用、timeout / cancellation 或 diagnostics 会实质影响验证可靠性时按需使用。

Agent 应根据当前 Runtime 支持的方式读取、安装或暴露所需 Skills。

本文不规定固定的分发 / 安装机制（Distribution / Installation）。只要求：

- 使用来自已确认 `agentic-dev` baseline 的 Skill；
- 不依赖历史测试残留或陈旧复制；
- 不因为 Runtime 安装方式不同而改变 Skill Contract；
- Consumer Repository 的 Authority 始终高于可复用 Skill 对项目事实的推测。

不要求所有 Skills 在每个工作中都出现。

## 5. 常规 Feature 工作流

### 5.1 先判断意图（Intent）是否需要澄清

如果 Goal、Scope、User-visible Behavior、Business Boundary 或 Acceptance 存在会实质改变产品结果的歧义，使用：

```text
clarify-intent
```

如果现有权威已经足够明确，不为了流程完整性制造额外澄清。

如果澄清过程中识别出可能跨多个功能持续有效的业务术语、不变量或规则，将其作为 Domain Authority Candidate 交给 `specify` 验证；不要因为它已经在聊天或 Clarification 中确认，就直接把它提升为长期领域权威。

### 5.2 形成最小充分规格说明（Specification）

使用：

```text
specify
```

Specification 负责 WHAT / WHY，应让 Fresh Agent 能判断：

- 要做什么；
- 不做什么；
- 什么结果表示完成；
- 是否仍存在关键产品歧义（Product Ambiguity）。

Specification 不要求固定文件名、目录、Markdown 模板或 YAML Front Matter。

`specify` 还应判断已确认的领域事实是否需要独立于当前 Feature 长期维护：

- 只服务当前 Feature 的行为继续留在 Specification；
- 会被多个功能、缺陷处理或独立工作流持续消费的事实，按 Consumer Repository Authority 形成或更新 Domain Authority；
- Agent 已获授权时可以执行相应更新；无权确认时输出 Required Domain Authority Action；
- 旧事实失效时显式更新、取代或同步修正引用，避免新旧事实同时被视为有效。

### 5.3 只在需要时创建技术计划（Technical Plan）并评估 ADR

如果存在需要跨 Execution Units 长期协调的 HOW 决策，使用：

```text
technical-plan
```

如果 HOW 可以安全地在单个 Execution Unit 中通过即时计划（JIT Plan）解决，且不存在需要维护的 Architecture Context 或需要评估的 ADR，则不要为了阶段完整性创建永久 Technical Plan。无需单独持久化 Technical Plan Artifact，不会豁免已经触发的 Architecture Authority 更新。

`technical-plan` 形成长期技术决策后，应依次判断 Architecture Context 更新与 ADR 条件产生：

- 只服务当前功能及其执行单元协调的决定，继续留在 Technical Plan；
- 改变未来多个功能持续依赖的系统结构、组件 / 数据 / 集成 / 部署 / 共享契约边界时，形成或更新适当的 Architecture Authority；
- Architecture Context 中需要长期保留背景、重要选择理由、权衡或替代关系的决定，再显式评估形成或更新 ADR；
- 普通局部、低影响、可逆实现选择、即时文件 / 命令 / 编辑细节以及尚未收敛的探索过程，不形成 ADR。

需要更新 Architecture Context 时：

- 使用 Consumer Repository 已有的架构说明、契约、模型、代码或其他可发现载体；
- 同步维护当前有效状态、引用与取代关系；
- 不满足 ADR 条件不代表架构状态可以只留在 Technical Plan。

需要 ADR 时：

- 可以创建新的 ADR、更新现有 ADR，或以新决定取代旧 ADR；
- 新决定取代旧决定时，保留被取代 / 替换（Superseded / Replaced）关系；
- 使用 Consumer Repository 已有的 Architecture / Decision 载体；如果此前没有相应目录，只在真实 ADR 首次产生时再建立，不要求固定目录名或模板；
- 是否需要人工介入仍依据权限（Authority）、影响（Impact）、可逆性（Reversibility）；重大架构方向（Major Architecture Direction）或高影响难逆决定不得由 Agent 静默确认为长期权威。

如果 Execute、`systematic-debug` 或 `converge` 才发现长期领域事实缺失、冲突或失效，应回到 `clarify-intent` / `specify`；发现新的长期架构状态、决定或现有 Architecture Context 失效时，应回到 `technical-plan` 完成 Architecture Authority 更新与必要 ADR 评估。不要把长期权威只留在代码、测试、当前聊天或局部 JIT Plan 中。

### 5.4 切分并检查执行单元（Execution Units）

使用：

```text
slice-work
→ readiness-check
```

Execution Unit 应：

- 范围明确；
- 可独立验证；
- 尽量纵向完成一个有意义的行为结果；
- 适合在 Fresh Execution Context 中执行；
- 不依赖前一个 Worker 未持久化的会话推理（Conversation Reasoning）。

切分结果还应显式建立：

```text
规格验收义务
→ 实现责任 / 验证责任
→ 计划验证证据
```

具体要求：

- 每项必需行为 / 验收义务都由某个执行单元承担实现与验证责任；
- 只有确实必须在多个执行单元组合后才能证明的行为，才显式归属功能整体验证责任；
- 计划验证证据应能证明具体行为及其关键差异，不能只写“代码完成”“测试通过”或主路径；
- 分页、排序、边界 / 失败、多状态、跨入口等行为应按实际规格说明与风险设计足够的验证场景；
- 不要求一条验收义务对应一个测试，也不限定自动化、E2E、CI 或其他固定证据格式。

就绪检查不只检查执行单元能否实施，还应检查验收责任归属和计划验证覆盖是否足以进入执行。需要补充责任或验证覆盖时返回 `slice-work`，检查者不自行改写执行单元。

Readiness 还应确认相关执行单元遵守当前有效的 Domain / Architecture / ADR Authority。如果已经暴露 Domain / Architecture Authority Gap，或当前工作要求创建 / 重大更新长期权威产物却无法确定其生命周期责任，不应进入 Execute；Checker 只返回拥有相应事实或决定的职责层，不自行修复权威。

### 5.5 每个 Unit 使用 Fresh Execution Context

使用：

```text
execute-unit
```

每个 Fresh Execution Context 只执行一个唯一 Current Unit。

Worker 只加载：

- 当前 Unit；
- 必要的 Consumer Repository Authority；
- 必要的 Specification / Technical Plan；
- 当前执行单元承担验证责任的验收义务与计划验证证据；
- 相关 Domain / Architecture / ADR Context（如存在）；
- 当前验证（Verification）所需上下文。

不要把前一个 Worker 的完整聊天历史当作下一个 Worker 的依赖。

遇到非预期失败并需要系统诊断时，可使用：

```text
systematic-debug
```

### 5.6 验证 Runtime 与当前证据

选择验证路径时，不仅要确认验证机制存在，还应确认当前运行环境（Runtime）能够重新取得与目标状态对应的当前证据（Current Evidence）。

遵循以下原则：

- 执行单元完成前回到规格追踪，确认当前证据逐项支持当前执行单元承担验证责任的验收义务；
- 实现存在、代码检查、历史证据或未覆盖关键差异的主路径证据不能代替必要的完成证据；
- 显式归属功能整体验证责任的义务保持 `Pending`，必须由后续 `converge` 独立重新检查；
- 验证路径应具有足够的证据可观察性（Evidence Observability）；Agent 不应选择自己无法重新取得必要完成证据（Completion Evidence）的执行路径；
- 如果当前 Runtime 对某类 CI trigger 或验证结果不可观察，应在仓库策略（Repository Policy）允许范围内切换到可观察路径，而不是把未知状态当作通过；
- 快速反馈（Fast Feedback）与完成验证（Completion Verification）可以分层；中间修复优先取得低成本、针对性的反馈，最终完成声明仍必须满足必要的完整验证；
- 中间修复迭代不要求每次重复支付最高成本的环境准备，但不能因此降低最终 Completion Evidence 的覆盖；
- 高成本且稳定的环境依赖可以通过预构建 Runtime、Artifact 复用、缓存或其他当前平台支持的方式降低重复准备成本；
- 长运行环境准备和验证应具有与正常基线相称的 timeout / cancellation 策略，避免把异常等待当作正常执行；
- Diagnostic / Runtime Observation 可以支持 diagnose、abort、reroute 或调整验证路径，但不能因为同样属于 Current Evidence 就自动替代 Completion Evidence；
- 平台专项实现细节按需下沉到相应 Skill；例如 GitHub Actions 场景可使用 `github-actions-verification`，而不是把 PR、容器或特定 registry 提升为所有 Consumer 的通用规则。

### 5.7 整体收敛

所有当前范围内的 Units 完成后使用：

即使前置的切分、就绪检查与执行已建立义务闭环，`converge` 仍必须独立从规格说明重建功能整体覆盖，不把执行单元状态、计划验证或实现存在当作功能完成证据。

```text
converge
```

只有当前 Intent、Specification、Implementation 与验证证据（Verification Evidence）一致，不违反当前有效的 Domain / Architecture / ADR Authority，本次工作产生或改变的长期权威事实已完成适当生命周期闭环，且不存在阻塞缺口（Blocking Gap），才能达到：

```text
Ready to Integrate
```

如果收敛阶段发现 Domain Authority Gap，应返回 `clarify-intent` / `specify`；发现 Architecture Authority / ADR Gap，应返回 `technical-plan`；发现 Artifact Lifecycle Gap，应返回拥有相应事实或决定的职责层。已有且适用的 Project Roadmap 因本次工作跨越项目级更新触发条件而陈旧时，也属于阻塞性 Artifact Lifecycle Gap；`converge` 只识别并路由到 Consumer 授权的项目治理 / Bootstrap 维护职责，不自行规划路线。不能用 `READY` 绕过。

Merge / Push / Release / Deploy 仍由 Consumer Repository 的人工权威（Human Authority）或仓库策略（Repository Policy）决定。

## 6. 项目如何持续演进

Consumer Repository 应随着真实工作逐步丰富，而不是在初始化时一次设计完成。

### 6.1 已有 Consumer 的采用与基线升级

`agentic-dev` 是可复用 Method、Skills 与 Operating Guide 的上游知识源，不是已有 Consumer 日常开发必须持续读取的运行依赖。

已有 Consumer 在以下情况按需重新读取 `agentic-dev`：

- 明确执行 `agentic-dev` baseline 升级；
- Consumer-local Authority 无法回答当前真正需要的方法或 Skill 问题；
- 当前工作被明确标记为 `agentic-dev` Experiment / Validation；
- Consumer Repository Authority 另有明确要求。

采用或升级时应完成以下最小闭环：

1. 读取并记录当前实际使用的精确 `agentic-dev` baseline；
2. 区分可跨项目复用的 Method、Skills、Operating Guide，与只属于 `agentic-dev` 仓库自身的 Project Rules；
3. 根据 Consumer 的真实需要与现有 Authority 选择性采纳，不机械复制完整文档体系；
4. 将需要长期约束后续工作的已采纳规则固化到 Consumer 自己可发现的 Repository Authority 中，并按需保留来源与 baseline 关系；
5. 由 Consumer Authority 明确本地规则的优先级、更新触发条件与适用范围；
6. 完成升级后，普通开发恢复以 Consumer-local Authority 为主要工作入口。

Consumer 可以使用 `AGENTS.md`、项目开发方法文档、配置或其他合适载体完成本地固化；本指南不要求固定文件名或目录。只服务一次升级判断、没有持续约束价值的分析过程不需要进入长期项目知识。

Consumer-local 规则不能静默改写 `agentic-dev` 的通用 Method 或 Skill Contract；反过来，新的 `agentic-dev` 提交也不会仅因存在就自动覆盖 Consumer 已采纳的项目规则。再次升级必须重新比较当前 Consumer Authority 与新的精确 baseline，并显式处理需要更新、保留或取代的内容。

可以新增：

- 新的项目规则（Project Rules）；
- Project Roadmap（满足项目级长期协调与恢复条件时）；
- Domain / Requirement Artifacts；
- Architecture / Decision Artifacts，包括按条件产生的 ADR；
- Coordination Artifacts；
- 当前项目真正需要的其他 Skills；
- Verification / Integration 规则。

每次新增前都应问：

> 这项内容是否具有当前项目真实、持续的协调或权威价值？

如果没有，就不要仅为了形式完整性持久化。

新增或重大修改长期权威产物时，还应能从当前 Method 与 Consumer Repository Authority 中确定：谁负责确认和形成、什么变化触发、谁会消费、保存在哪里、何时更新、如何取代旧内容，以及哪些情况必须升级。具体载体和写入权限由 Consumer 决定，不要求为此创建统一目录、模板或 Artifact Management Skill。

Project Roadmap 一旦存在并仍然适用，就应在以下项目级变化发生时同步维护：里程碑完成、取消或被取代，当前阶段 / 核心目标改变，已决定的下一步顺序改变，或条件性方向正式进入当前路线。路线尚不确定时记录 Unknown / Conditional，不用猜测填满未来；README、任务清单和状态摘要不应并行维护另一份竞争性的当前路线。

对 ADR 还应额外确认：它记录的是跨功能长期架构约束，而不是当前 Feature 的普通 Technical Plan Decision。已有 ADR 被新决定替代时，应显式维护其状态或替代关系，避免后续 Fresh Agent 同时把新旧决定都当作有效权威。

Project Rule 可以选择、要求或限制 Skills，但 Skill 不得覆盖 Project Authority。

## 7. 中断、恢复与 Fresh Context

会话历史（Conversation History）不是长期项目状态。

工作中断或切换 Context 时，应依赖 Consumer Repository 中已经持久化的：

- Project Rules；
- Project Roadmap（如存在且适用）；
- 当前 Specification / Technical Plan（如存在）；
- 相关 Domain / Architecture / ADR Authority（如存在）；
- Current Unit / Coordination State；
- Verification Evidence；
- 必要的代码与配置。

新的 Agent Context 应从这些 Artifact 恢复工作，而不是要求提供完整旧聊天。存在 Project Roadmap 时，应先用它定位当前阶段、核心目标、下一步和权威入口，再按 Progressive Disclosure 读取当前工作所需的 Specification、Plan、Unit、Evidence 与代码；Roadmap 不替代这些事实来源。

Fresh Context 是逻辑隔离，不要求某一种特定 Runtime 形式。可以是新 Chat、新 Codex session、isolated worker 或其他能够避免依赖未持久化历史 reasoning 的执行环境。

## 8. 实验使用（Experimental Use）：向 agentic-dev 回传实践证据

普通 Consumer Project **不要求**向 `agentic-dev` 提交反馈。

只有当当前工作被明确标记为 `agentic-dev` Experiment / Validation 时，才启用本节规则。

### 8.1 实验隔离

实验应尽量使用独立 Fresh Context，并只把以下内容作为 Consumer Authority / Execution Input：

- 指定的 `agentic-dev` Repository baseline；
- 明确的 Consumer 需求来源；
- Consumer Repository；
- 当前 Runtime 可直接观察到的能力和状态。

即使 Runtime 可能暴露其他会话、个人记忆或历史上下文，也不得把这些内容作为 Consumer 项目事实、规则或需求依据。需要使用的事实必须能回溯到当前 Consumer Authority。

### 8.2 GitHub Issue 作为首选反馈通道

实验期间，使用 `agentic-dev` Repository 的 GitHub Issue 作为首选实验反馈通道（Experiment Feedback Channel）。

Issue 是：

- Evidence 传输通道；
- 跨 Repository / Context 的跟踪入口；
- 后续 `agentic-dev` 分析的输入。

Issue **不是**：

- Consumer Repository 的项目知识库；
- `agentic-dev` Method / Contract Authority；
- 自动成立的方法结论。

如果当前 Runtime 具有 GitHub Issue 写权限，应直接通过 GitHub API / Connector 提交或追加反馈。

如果没有写权限，不得阻塞 Consumer 开发；生成符合以下格式的 Issue Body / Comment，待具备权限后提交即可。

### 8.3 一个实验使用一个跟踪 Issue（Tracking Issue）

默认一个 Consumer Experiment 对应一个 Tracking Issue，不为每个小问题创建独立 Issue。

为了在不依赖 GitHub Issue Template 的情况下保持首轮反馈可检索、可比较，Tracking Issue 使用以下标题约定：

```text
[experiment] <consumer> - <experiment goal>
```

Issue Body 至少包含：

```text
Experiment:
Consumer Repository:
Consumer Baseline / Branch:
agentic-dev Baseline:
Runtime / Model:
Goal:
Scope:
```

其中无法获得的字段应明确写 `Unknown / Not available`，不要静默省略。

开发过程中只在出现有意义的新证据时追加 Comment：

```text
Observed Friction / Finding:
Context / Stage / Skill:
Evidence Reference:
Human Intervention:
Classification Candidate:
- Usage Guide
- Skill Implementation
- Contract
- Method
- Project Rule
- Runtime
- Unknown
```

如果某条 Finding 没有可引用的代码、Commit、PR、命令结果或其他当前证据（Current Evidence），应明确说明证据限制，不把推测写成已确认缺口。

不要提交：

- 完整 Conversation；
- 完整 private reasoning；
- 每次 Skill 调用流水；
- Consumer Repository 已经存在的整份项目文档副本；
- 没有实际影响的普通实现噪音。

### 8.4 实验结束

在同一 Tracking Issue 中追加 Final Summary：

```text
Final State:
Skills Actually Used:
Key Findings:
Human Interventions:
Consumer Evidence References:
Recommended Follow-up:
```

Consumer Agent 可以提出 Classification Candidate，但不能自行把实验观察提升为 `agentic-dev` 的 Method / Contract 结论。

最终是否修改 `agentic-dev`，应回到新的 `agentic-dev` Context，重新读取：

- 当前 `agentic-dev` Authority；
- Experiment Issue；
- Issue 引用的 Consumer Evidence。

再按证据分类处理。

## 9. 推荐启动方式

一个 Greenfield Consumer Experiment 的启动指令应保持很薄。

只需要明确：

- 要创建什么真实项目；
- `agentic-dev` Repository 在哪里；
- 已建立的 Consumer Authority（如有）；
- Requirement Source / 初始业务输入在哪里（如有）；
- Consumer Repository 在哪里；
- 当前工作是否属于 Experiment。

然后让 Agent 自行读取本文和相关 Skills 开始工作，并按第 2 节判断 Requirement Source 是否、以及如何被采纳为 Consumer Authority。

如果仍必须依赖大量未写入 `agentic-dev` 的口头步骤才能启动项目，应把这种情况记录为 Operating Guide / Method 使用证据，而不是用额外聊天指令悄悄补齐。

## 10. 使用目标

`agentic-dev` 的目标不是提前规定项目最终长什么样，而是让 AI 能够：

1. 从最小、明确的 Repository Authority 开始；
2. 根据真实需求逐步建立项目知识与结构；
3. 在需要时选择合适的 Skills；
4. 用 Fresh Context 和 Current Evidence 推进实现；
5. 在项目演进过程中只持久化真正有长期价值的知识；
6. 最终基于整体证据达到 `Ready to Integrate`。
