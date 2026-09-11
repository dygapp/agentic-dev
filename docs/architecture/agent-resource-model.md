# 面向 Agent 的资源模型

**状态：** V3-05 候选 v0.1  
**性质：** 跨仓库可复用的资源语义与最小结构契约  
**跟踪：** Issue #109

## 1. 目的

本文定义 `agentic-dev` 面向 Agent 的长期资源模型，回答：

> 当一个现行长期资源需要被 Fresh Context、按需职责或后续发现机制可靠识别时，哪些语义必须稳定表达，哪些信息只能由发现层派生，怎样在不复制规范正文的前提下保持当前性、来源和取代关系。

本文建立在以下已集成结论之上：

- V3-01：先判断语义所有者，再分别判断适用范围 / 来源状态、运行 / 生命周期角色、载体 / 权威形式；
- V3-02：目录、文件名和 Markdown 形式不能决定资源身份，现有 Guide / Project / Research / Skill 目录中存在 mixed / transitional / derived 情况；
- V3-03：使用方采用完成后，普通运行默认只依赖使用方本地当前资源；上游来源不等于当前权威；
- V3-04：Skill 只拥有稳定独立执行过程，工程纪律 / 生命周期 / 仓库本地规则 / Guide 不为了激活方便而 Skill 化；Skill 支持资源不因物理目录获得平级所有权。

V2 的 `consumer-local-activation-metadata-contract-v2.md` 继续作为已经过真实使用方验证的过渡输入，但其字段和 Manifest / Catalog 设计必须在本文中重新裁决，不能自动成为 v3 架构。

## 2. 三层模型

V3-05 把资源相关信息分成三层。

```text
规范 / 事实正文
→ 资源固有结构
→ 派生发现投影
```

### 2.1 规范 / 事实正文

这是资源真正拥有的长期语义，例如：

- 方法 / 原则正文；
- Skill procedure；
- 工程纪律或技术画像规则；
- 仓库本地政策；
- Requirement / Specification / Architecture / Roadmap；
- Guide 的人类说明；
- Research / Eval 的证据正文。

**正文始终由真实语义所有者持有。**

资源模型、metadata、Manifest、Catalog 或未来 Index 都不能取得第二份规范正文所有权。

### 2.2 资源固有结构

资源固有结构只表达不会因某次查询或某个模型判断而改变的长期身份 / 生命周期事实，例如：

- 资源稳定身份；
- 语义所有者类别；
- 适用范围；
- 来源状态；
- 运行 / 生命周期角色；
- 载体 / 权威形式；
- 当前 / 已取代 / 历史等当前性；
- 本地可读取位置；
- 必要的来源、取代或父资源关系。

这些信息可以由资源自身、同目录契约、仓库本地 Authority Map、sidecar 或其他稳定载体共同表达；**本文不要求一种统一序列化格式。**

### 2.3 派生发现投影

派生发现投影服务 V3-06 的候选筛选、路由和最小上下文选择，例如：

- 当前职责候选；
- 条件 / 风险标签；
- routing-only / execution 等加载提示；
- 查询索引；
- Runtime Catalog；
- 其他可以从当前资源结构和正文重新建立的导航信息。

派生投影：

- 不拥有规范正文；
- 可以删除 / 重建；
- 不能覆盖 Repository Authority；
- source stale / missing / ambiguous 时必须失败关闭；
- 是否存在、采用何种物理形式由 V3-06 决定。

## 3. 什么构成“资源”

V3-05 的资源单位不是“一个 Markdown 文件”，而是：

> **具有可独立识别的长期语义身份、生命周期和当前性边界，并可能被独立发现、采用、更新、取代或按需加载的最小稳定单元。**

一个资源可以是：

- 整个文件；
- 一个稳定 section；
- 一个 `SKILL.md` 与其受控 supporting body 形成的复合资源；
- 一个由多个文件组成、但只有一个 current entry 的技术画像；
- 当前仓库权威显式指定的逻辑入口。

行号、临时分支、Issue 评论、一次运行结果或会话中的临时对象不能作为长期资源唯一身份。

## 4. 什么时候需要结构化

不是所有长期文档都必须建立独立结构化描述。

一个资源至少满足以下一项时，才需要让其长期身份可以被机器可靠恢复：

1. **独立发现**：Fresh Context 或按需职责需要在多个候选资源中独立找到它；
2. **条件采用 / 加载**：它只在特定技术、职责、生命周期或使用方采用条件下生效；
3. **多版本 / 取代**：存在 current / superseded / historical 或 adopted / local 演进，需要可靠区分当前入口；
4. **跨仓采用**：它作为可复用能力可能被使用方采用，并需要保留来源状态与本地当前所有权的分离；
5. **派生发现输入**：V3-06 必须稳定识别它，才能生成不会拥有正文的索引 / Catalog / 路由投影。

以下情况默认**不要求**新增独立资源描述：

- `AGENTS.md`、README 等已经由固定 Repository Bootstrap 规则直接定位，且不需要在多个同类候选中选择；
- 只由一个父 Skill / 画像内部加载的 supporting resource；
- 一次性计划、临时分析或只服务当前执行上下文的工作产物；
- 普通历史证据，不参与当前发现；
- 已有 current owner 的派生目录清单或人类索引，本身不需要成为第二资源 owner；
- 仅因为仓库新增一个 Markdown 文件。

如果固定入口后续需要参与统一发现、采用或多版本 currentness 判断，可以再进入结构化范围；本文不预先要求全仓覆盖。

## 5. 最小逻辑资源结构

以下名称表示**逻辑字段身份**，不是强制 YAML / JSON key。物理实现可以采用不同字段名，但不得合并掉这些正交语义。

### 5.1 稳定资源身份

每个被独立结构化的资源必须有稳定 identity。

要求：

- 在当前发现 / 采用范围内可唯一定位该逻辑资源；
- identity 不等于当前路径；
- 路径变化不应自动改变语义身份；
- 真实语义所有者被取代时，必须显式决定保留 identity 还是建立新 identity，不能只按标题复用。

### 5.2 语义所有者

使用 V3-01 已确认的所有者类别：

- 核心方法 / 原则；
- Skill / 过程型能力；
- 可复用工程能力 / 工程纪律 / 画像；
- 仓库本地政策 / 规范 / 规则；
- 项目 / 产品权威资源；
- Guide；
- 研究 / 输入 / 证据。

派生投影不成为新的规范正文所有者。

### 5.3 适用范围

表达当前资源语义直接在哪个范围有效，至少保持 V3-01 的：

- 跨仓库可复用；
- 仓库本地；
- 外部输入；
- 仅历史。

适用范围不能与“任务 / 模块 / 条件标签”混为同一个 `scope`。

### 5.4 来源状态

表达资源怎样进入当前仓库，至少保持：

- 本仓原生；
- 从上游采用；
- 从外部输入提升；
- 派生投影；
- 外部未采用；
- 历史来源。

规则继续是：

```text
来源 ≠ 当前权威
```

### 5.5 运行 / 生命周期角色

表达资源在哪些生命周期中可能被消费，例如：

- 启动 / 初始化；
- 首次采用；
- 基线升级；
- 普通运行；
- 职责按需加载；
- 验证 / 复核；
- 仅历史 / 证据。

该维度描述生命周期，不直接规定 V3-06 的“如何路由 / 是否立即加载”。

### 5.6 载体 / 权威形式

表达 Agent 应怎样理解其承载形式，例如：

- 方法 / 原则文档；
- 架构 / 契约文档；
- `SKILL.md`；
- 工程纪律 / 技术画像；
- Repository Policy / Standard；
- Requirement / Specification / ADR / Roadmap / Work Authority；
- Guide；
- Research / Eval / Evidence；
- supporting resource；
- derived projection。

载体只决定读取 / 维护方式，不决定语义所有者优先级。

### 5.7 当前性

结构层至少必须区分：

- 当前有效；
- 已被取代；
- 仅历史 / 证据；
- 当前仓库明确禁用 / 不参与当前运行（只有仓库真实存在此状态时）。

普通运行和 V3-06 的 current set 只能消费当前有效资源。

`rejected / not-applicable` 的采用决定仍属于使用方升级历史，不要求制造一个可发现的当前资源。

### 5.8 本地位置

结构层必须能够定位当前仓库中可读取的正文：

```text
local path
+ optional stable selector
```

规则：

- 普通运行只解析当前仓库本地对象；
- selector 可以是稳定 heading / section identity；
- 行号不能作为唯一长期 selector；
- locator 不拥有正文语义；
- 路径 / selector 被取代时必须更新相应结构或派生投影。

### 5.9 条件来源 / 关系

只有真实需要时记录：

- 上游来源及精确采用基线；
- supersedes / superseded-by；
- derived-from；
- supporting-for / parent-resource；
- 当前仓库权威明确存在的 override 关系。

不建立为了“更完整”而维护的大型资源图。

关系只帮助追溯、当前性和发现，不创造 Authority priority。

## 6. 不进入资源固有结构的内容

以下信息默认属于正文或 V3-06 派生层，不进入最小长期资源结构：

- 规则完整正文或摘要；
- `required_checks`；
- 当前 Issue / PR / Actions 状态；
- Roadmap 当前 Gate 的副本；
- 模型推荐答案或预期选择；
- 当前会话已加载哪些资源；
- 固定 Top-K / ranking score；
- 为某次任务生成的临时查询词；
- 由具体 Consumer 决定的 Build / Test / Deploy 命令，除非它们本身就是该 Consumer 的本地权威正文。

### 6.1 职责、条件和风险标签

V2 的 `responsibility / conditions / risks` 主要服务运行时发现。

V3-05 的裁决是：

- 资源正文中真实存在的职责、适用条件和风险边界继续由真实 owner 持有；
- 如果 V3-06 需要用紧凑标签做候选筛选，可以建立**派生发现提示**；
- 派生提示必须可回溯当前 owner，不能变成独立规范正文；
- owner 语义变化后，旧提示不能只重算 hash 就自动恢复当前性；
- V3-05 不冻结标签词表。

## 7. 物理表示兼容

V3-05 标准化逻辑语义，不强制一种文件格式。

### 7.1 普通 Markdown

普通 Markdown 可以继续不带 Front Matter。

如果资源需要结构化，其逻辑结构可以来自：

- 文档自身稳定区块；
- 同目录或仓库级 sidecar；
- 当前仓库 Authority Map；
- V3-06 后续决定的可重建派生描述；
- 其他不会复制规范正文的稳定表示。

V3-05 不要求把所有 Markdown 重写成统一模板。

### 7.2 `SKILL.md`

当前 `SKILL.md` 已使用 Agent Skills 兼容的最小：

```yaml
name: ...
description: ...
```

裁决：

- `name` 可以作为 Skill 当前原生稳定 identity 的重要输入；
- `description` 继续服务 Skill 发现 / 互操作，但不替代 Purpose、Use When、Do Not Use When、Inputs、Outputs、Exit 等 Skill Contract 正文；
- V3-05 不要求把 V3 四维所有权全部塞进 Skill Front Matter；
- 若 V3-06 需要更多发现信息，优先派生或使用兼容 sidecar，不通过扩张 `SKILL.md` Front Matter 建立第二套 Skill Contract。

### 7.3 技术画像 / 验证画像

`technology-profile-contract.md` 已明确技术画像可以是一个文件或一组具有单一 current entry 的文件，并且不要求固定 YAML / JSON schema。

因此：

- 画像继续保留自身契约结构；
- 资源模型只要求其稳定身份、所有权四维、当前性和本地入口可被恢复；
- 技术版本 / 证据基线等画像专有字段仍由画像契约拥有，不提升为所有资源的统一字段。

### 7.4 仓库本地规则 / 项目权威

仓库本地 Policy、Requirement、Specification、Architecture、Roadmap 等可以保持各自原生格式。

如果它们进入统一发现，只提供 locator 与资源身份；不得把当前政策正文、业务值、架构决定或 Gate 复制进 metadata。

高频变化的 Current Authority 应优先使用“定位当前 owner”的模式，不因为正文正常变化就机械失效资源 identity。

### 7.5 Skill supporting resources

V3-04 边界继续生效：

- supporting resource 直接服务父 Skill procedure；
- 不独立拥有跨 Skill / 跨仓库规范语义；
- 生命周期随父 Skill 管理；
- 默认不建立平级独立资源 identity。

只有 supporting resource 真正形成独立语义所有者或被多个职责独立消费时，才重新进入 V3-01 / V3-04 判断，而不是由 V3-05 metadata 自动升级。

## 8. 当前性与来源绑定

V3-05 只固定当前性原则，不实现发现算法。

### 8.1 原生结构与正文共同维护

如果资源固有结构与正文由同一 owner 一起维护，则正文更新不要求通过额外 hash 证明“当前”。当前 Git 状态本身就是版本化资源状态。

只有结构中存在从正文**提炼出来的语义提示**时，才产生额外 stale 风险。

### 8.2 派生语义提示

如果 V3-06 生成职责 / 条件 / 风险等语义提示：

- 必须绑定被审阅的 owner / selector identity；
- source 语义变化后旧提示先失效；
- 生成器不能仅更新 hash / commit id 就自动证明提示仍然正确；
- 必须重新判断变化是否影响派生语义。

这保留 v2 `semantic-reviewed` 的有效原则，但把它明确放在**派生发现层**，而不是所有资源的统一 identity 模式。

### 8.3 纯定位投影

如果派生结构只定位当前 Authority，并不复制其语义：

- source 正文正常更新不使 locator 自动 stale；
- path / selector / authority role 被取代时才需要更新；
- V3-06 可以保留 v2 `current-locator` 的思想，但它是发现绑定策略，不是资源所有权类别。

## 9. V2 metadata / Manifest / Catalog disposition

| V2 项 | V3-05 裁决 | 后续责任 |
|---|---|---|
| `id` | **保留并收窄**：稳定资源 identity 进入资源固有结构；不要求等于 upstream id 或路径 | V3-05 |
| `kind` | **取代 / 拆分**：不能用一个枚举同时表示 Authority / Skill / Discipline。改由“语义所有者 + 载体形式”正交表达 | V3-05 |
| `source` | **保留概念**：本地 locator + 可选稳定 selector；不拥有正文 | V3-05 |
| `activation_role` | **拆分**：生命周期角色进入 V3-05；routing / constraint / execution 等加载语义由 V3-06 派生 | V3-05 / V3-06 |
| `scope` | **拆分**：V3-01 的适用范围进入资源固有结构；任务 / domain activation scope 留给 V3-06 | V3-05 / V3-06 |
| `responsibility` | **移出固有结构**：作为 V3-06 可选派生路由提示；Skill 自身职责仍由 Skill Contract / `SKILL.md` 拥有 | V3-06 |
| `conditions` | **移出固有结构**：可作为 V3-06 派生提示，必须 source-bound | V3-06 |
| `risks` | **移出固有结构**：可作为 V3-06 派生提示，不冻结全局 taxonomy | V3-06 |
| `origin` | **取代**：由 V3-01 来源状态 + 条件 provenance 表达，避免 `consumer/adopted` 过粗 | V3-05 |
| `state` | **保留语义、调整身份**：最小 current / superseded / historical / explicit-disabled 当前性；reject / not-applicable 留在升级历史 | V3-05 |
| `relations` | **保留但收窄**：只记录真实 supersede / derived / supporting / 明确 override 关系，不建立优先级图 | V3-05 |
| `semantic-reviewed` | **保留原则、下移**：作为 V3-06 派生语义提示的 currentness 绑定方式 | V3-06 |
| `current-locator` | **保留原则、下移**：作为 V3-06 纯 locator 投影的绑定方式 | V3-06 |
| Activation Manifest | **不进入资源固有模型**：继续作为 v2 过渡兼容；V3-06 决定是否保留、简化或取代 | V3-06 |
| Runtime Catalog | **明确为派生投影**：可删除 / 重建，不拥有规范正文；物理存在与否由 V3-06 决定 | V3-06 |

因此 v3 不再把“Manifest 中的一条 record”与“真实长期资源”视为同一个对象。

## 10. V3-06 的输入契约

V3-06 可以假定 V3-05 已经固定以下事实：

1. discovery 的候选对象是**资源**，不是任意文件；
2. 资源身份由 V3-01 四维所有权 + currentness + locator 等长期语义构成；
3. 规范正文不进入 Catalog / Index；
4. routing / conditions / risks 等紧凑信息属于可重建派生提示；
5. 普通运行只能读取使用方本地 current resource；
6. derived projection stale / missing / ambiguous 时必须失败关闭；
7. `SKILL.md`、普通 Markdown、技术画像和仓库本地规则允许不同物理表示；
8. 不要求全仓 Front Matter。

V3-06 必须自行回答：

- 是否还需要 Manifest / Catalog 两层；
- 是否需要单一派生 Index；
- 如何生成 / 更新 / 校验派生发现信息；
- 查询维度与候选选择算法；
- primary / supporting routing；
- Stage Return 后如何重新发现；
- 与当前 `rule-activation-guide.md` 的显式取代关系。

V3-06 不得重新定义 V3-05 已固定的资源身份和所有权语义。

## 11. 使用方采用边界

V3-03 使用方生命周期继续约束 V3-05：

- 上游可以提供可复用资源模型和候选结构；
- 使用方逐项采用后，本地资源由使用方当前仓库权威管理；
- 普通运行不依赖 upstream online lookup；
- 上游 provenance 只用于升级 / 追溯，不自动成为普通运行依赖；
- 使用方可以保留、覆盖、拒绝或取代上游资源，但必须保持当前本地 owner 清晰；
- 一个 baseline pointer 不代表所有上游资源都已采用。

## 12. 非目标

本文不要求：

- 全仓统一 YAML / JSON / Front Matter；
- 所有 Markdown 都有 resource id；
- Runtime Catalog / Activation Manifest 必须存在；
- Rule Index / Manifest generator；
- 数据库、向量库、图数据库、MCP 服务或后台 daemon；
- 一个全局 priority score；
- 把职责 / 条件 / 风险标签提升为规范正文；
- 把 Guide / supporting resource / derived projection 自动升级为平级 owner；
- 修改任何使用方仓库。

标准化的是**资源语义、所有权维度、当前性和固有 / 派生边界**，不是统一文件格式或发现实现。