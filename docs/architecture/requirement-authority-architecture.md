---
id: architecture:requirement-authority
type: architecture
status: active
---

# Requirement Authority 架构

## 1. 目标

本 Architecture 定义普通软件 Consumer 中长期 Requirement Authority 的 semantic ownership、推荐信息架构、Human / Agent 导航边界与 artifact lifecycle。

它不规定某个项目必须使用完全相同的物理目录名，也不定义 Feature Specification 内容。其目标是确保：

- 同一长期业务事实只有一个长期 owner；
- Fresh Context Agent 可以从有限入口确定性找到当前 Requirement；
- Human Navigation、Authority Locator 与 Requirement Fact 不互相复制职责；
- 临时分析资产不会逐渐变成隐藏的第二套需求事实源；
- Requirement Baseline 可以被后续 `method:ai-development` 稳定消费。

## 2. Semantic ownership

一个 Consumer 至少需要区分以下责任：

### Requirement Human Navigation

回答：

> 这套 Requirement 体系如何组织、如何维护、如何阅读？

它只服务人类理解与使用，不拥有 Requirement inventory 或业务事实。

### Requirement Authority Index

回答：

> 当前某类 Requirement 的唯一 Authority 在哪里？

它拥有 Requirement → owner locator / relation 的全局定位责任，但不复制 Requirement 正文。

### Requirement Fact Authority

回答：

> 当前长期 Requirement 事实到底是什么？

真正的 Product / Domain / NFR 事实必须进入这里，而不是停留在 README、index、聊天、分析表或派生视图中。

### Requirement Analysis Workspace

回答：

> 当前分析、比较、抽取、歧义整理过程中有哪些临时工作材料？

默认非 Authority；只要事实已经 promote 到 durable owner，分析资产可以退出、归档或删除。

## 3. 推荐 `docs/requirements` 信息架构

默认推荐：

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

这是推荐 Human IA / physical projection，不是硬编码 runtime contract。Consumer 可以根据项目规模、既有 Repository Authority 或组织习惯调整路径，只要保持本 Architecture 的 semantic ownership 不被破坏。

## 4. `README.md` 与 `index.md` 的边界

### 4.1 `README.md` — Human Navigation / Usage Guide

`README.md` 只负责：

- 解释 Requirement 目录的目的；
- 说明各类 owner / 子目录职责；
- 说明如何新增、修改、复核 Requirement；
- 说明 Authority / non-Authority 边界；
- 指向 `index.md` 作为当前 Requirement Authority Locator。

`README.md` 不应：

- 维护完整 Requirement 文件清单；
- 复制业务规则、状态、权限等事实；
- 成为 Agent ordinary runtime 的 Requirement router；
- 维护会随业务内容频繁变化的 inventory。

### 4.2 `index.md` — Requirement Authority Index

`index.md` 拥有：

- Requirement / Capability stable label（项目确有需要时）；
- 名称；
- Requirement 分类；
- unique owner locator；
- 必要的跨 owner relation / dependency；
- 当前有效性或状态（只有项目确实需要时）。

`index.md` 不应：

- 重写完整业务事实；
- 复制 owner 文档中的规则 / 状态 /验收；
- 解释 Requirement Method；
- 变成第二份“总需求说明书”。

原则：

```text
README.md = 如何使用这套 Requirement 体系
index.md  = 当前 Requirement Authority 在哪里
owner docs = Requirement 事实是什么
```

## 5. `overview/` responsibility

`overview/` 用于项目级、跨多个 Capability 持续成立的 Requirement Context，例如：

- Project / Product Goal；
- In Scope / Out of Scope；
- 产品 / 系统责任边界；
- Actor / stakeholder overview；
- Requirement Capability Map；
- project-wide business constraints；
- 必要术语 / domain-wide semantics；
- project-wide external dependency overview。

这里的“系统边界”描述产品责任：系统负责什么、不负责什么、与哪些外部主体交换什么；它不等于内部模块划分、部署拓扑或 component architecture。

### 5.1 Project Terminology Authority

项目级术语治理是 Requirement Authority 内的**可选横向 semantic owner**，不是每个 Consumer 必须建立的 glossary，也不要求固定物理路径。

只有出现真实跨 Capability / Feature 的 terminology need 时才建立或扩展，例如：

- 同一长期业务概念存在多个中文名称并可能造成业务理解偏差；
- 同一业务概念存在多个英文 business term，可能形成并行领域命名；
- current / legacy / external 名称需要稳定映射；
- 术语差异会影响 actor、state、data semantics、fact ownership、cross-capability interaction 或 Acceptance；
- 多个 Specification、Design、Interface、Test 或带业务语义的代码对象需要共享同一 semantic root。

单一 Capability 内已经由真实 Requirement owner 清楚定义、且不会向外形成 naming drift 的局部词，不机械提升为项目级术语。

Project Terminology Authority 只拥有跨 Capability 长期稳定的：

- canonical Chinese business term；
- 确有英文命名需要时的 canonical English business semantic root；
- 最小 definition / distinction boundary；
- historical / external / alias mapping 及其 source role；
- applicability / scope；
- 必要的真实 Requirement owner reference。

它不拥有 Capability 内完整业务规则、状态机、权限或 Acceptance，也不拥有字段字典、API 字典、数据库字典、language/framework code style、package layout 或 identifier casing。

原则：

```text
Terminology Authority = 选择哪个业务概念 / business semantic root
Technical convention   = 该词根怎样按语言 / 框架形成 identifier
```

例如项目内部 canonical semantic root 为 `employment-scheme` 时，Requirement、Specification、business-oriented filename、domain type 可以复用该业务词根；Kotlin / Java 中是否形成 `EmploymentScheme`、package / filename 如何组织仍由技术命名规范决定。外部 contract 若固定使用 `employmentPlan`，可以保留该 external name 及其 source role，但不能反向制造第二套内部 canonical domain term。

术语候选优先从 current Requirement / Domain Authority 提取。分析阶段可以暂存 synonym / translation / legacy mapping candidate，但候选清单、Issue、聊天或 Review Draft 默认都是 non-Authority；确认后的 durable terminology 必须写回唯一 terminology owner，随后候选资产退出 Current consumption。

术语确认遵守现有 Requirement Question Gate：Current Authority 已能唯一决定时直接使用；只有不同答案会实质改变 business meaning、canonical identity、中英文 semantic mapping、legacy / external mapping、cross-capability naming 或 Acceptance / responsibility interpretation 时，才升级 Human Authority。

Canonical terminology 变化时不得 blind global search-replace。应先更新 true owner，再区分 current internal canonical reference、external preserved name、legacy source name 与 historical provenance，只迁移真正属于 Current internal semantics 的引用。

## 6. `business/` responsibility

`business/` 是主要纵向 Requirement Fact Authority。

一个 Requirement Capability 应尽量独立承担一组长期、可持续、具有共同业务目标或结果的事实。边界优先根据：

- 核心业务对象；
- 主要业务活动 / outcome；
- 生命周期；
- Actor / responsibility；
- 关键规则；
- 独立验收意义；
- fact ownership 是否能够保持清晰。

不得仅根据 UI 页面、菜单、微服务、数据库表、代码 package 或组织部门机械拆分 Requirement Capability。

一个 Capability owner 的正文通常需要能够表达：

- Goal / Scope / Out of Scope；
- Actors / Responsibilities；
- Core Business Objects；
- Business Scenarios / Activities；
- Business Rules；
- State / Lifecycle；
- Data Semantics / Range；
- Inputs / Outputs / Dependencies；
- Boundary / Failure Behavior；
- Acceptance；
- Remaining external / design / non-blocking items。

这是一组 semantic responsibilities，不要求所有 Consumer 使用完全相同章节模板。

## 7. `aspects/` admission

横向 Requirement owner 不是“无法分类内容”的收容目录。

只有同时满足以下条件，才应建立独立 aspect owner：

1. 事实跨多个 Requirement Capability 持续成立；
2. 具有独立业务 / Product / Acceptance 意义；
3. 不能合理归属于任何单一 Capability owner；
4. 建立独立 owner 能减少事实复制或冲突，而不是制造额外同步层。

如果一个横向事实本质上可以由某个 Capability、project overview 或 NFR owner 清晰承担，就不应为了对称性再创建 aspect。

## 8. `non-functional/` responsibility

这里持有真正可验收、跨实现方案持续成立的系统性质，例如：

- security / privacy；
- performance / capacity；
- availability / reliability；
- compatibility；
- accessibility；
- compliance；
- retention / audit obligation；
- 其他明确可验收 NFR。

框架选择、缓存策略、数据库索引、线程模型等普通实现 HOW 不因为与性能或可靠性有关就自动成为 NFR Requirement。

## 9. `analysis/` responsibility

`analysis/` 默认是非 Authority workspace，可用于：

- source inventory；
- extraction table；
- ambiguity / conflict candidate；
- terminology candidate inventory；
- comparison matrix；
- flow / state / relationship view；
- migration analysis；
- human review batch；
- conversation scratchpad。

这些资产必须明确：

- Producer；
- 当前用途；
- Authority promotion path（如果其结论需要长期保存）；
- exit / archive / delete boundary。

只要派生表达能够从当前 Requirement Authority 唯一再生，就不应默认成为长期同步对象。

## 10. Requirement Fact ownership

长期事实只进入一个真实 owner。

如果多个文档需要同一事实：

- 其他文档引用 owner；
- 描述本地适用范围或输入输出；
- 不复制完整规则正文。

跨 Capability 关系可以出现在 index / overview 中作为 locator / relation，但业务规则正文仍属于真实 fact owner。

Human Decision、会话结论、Issue comment 或 review note 本身不自动成为 Requirement Authority；确认的长期事实必须 promote 到真实 owner。

## 11. Requirement Capability 与 Scenario 粒度

本 Architecture 不要求通用 `L1/L2/L3` 编号体系。

Consumer 可以根据项目需要使用 Domain / Capability / Scenario 等层级，但通用原则是：

- Domain / overview 用于组织大范围上下文；
- Capability 是主要长期 fact owner；
- Scenario / Feature 只在当前业务理解、验收或后续开发需要时向下展开；
- 不把全量未来 Scenario 穷举当成 Requirement Baseline Ready 的必要条件。

主要长期事实都有 owner、主要边界清晰、后续 Feature 能确定性地找到 Requirement，比“列出了多少 L3”更重要。

## 12. Fresh Context consumption

普通 Fresh Context Feature Agent 不应默认扫描整个 `docs/requirements`，也不应因为项目存在 terminology owner 就预加载整份 glossary。

推荐消费路径：

```text
Repository Authority
→ Requirement Authority Index
→ current Feature / Capability owner
→ explicitly related overview / aspect / NFR owner
→ related Project Terminology Authority（仅当前任务涉及 business naming / mapping 时）
→ Specification / Technical Plan
```

典型 terminology 按需读取 trigger 包括：新增或修改跨 Capability business object / actor / state / activity；Specification 引入长期新业务术语；Technical Plan / code generation 创建带业务语义的 module、file、class、event、interface-model 名称；出现两个以上疑似同义 / 近义 business terms；legacy / external schema 需要映射当前内部语义。

`README.md` 主要供人理解，不作为 Agent runtime 的 Requirement locator。`analysis/` 也不进入 ordinary runtime，除非当前任务明确需要原始 Evidence、历史原因或尚未 promote 的分析材料。

## 13. Artifact lifecycle

### 13.1 Producer

主要 producer：

- `method:requirement-baseline-establishment`；
- 后续 Feature / Clarification 中经 Repository Authority 确认需要提升的长期 Requirement fact；
- Human / Product Authority 的长期决定。

### 13.2 Trigger

典型 trigger：

- 新项目建立 Requirement Baseline；
- Requirement fact 被确认或变更；
- 长期 owner 缺失、冲突或拆分 / 合并；
- Feature 中发现具有跨 Feature 长期价值的新业务事实或 terminology；
- External / policy change 改变长期 Requirement。

### 13.3 Consumer

主要 consumer：

- `method:ai-development`；
- `method:architecture-clarification`；
- Feature Specification；
- Technical Planning；
- verification / review；
- Human Product / Requirement Review。

### 13.4 Persistence

长期 Requirement Fact 必须保存在 Consumer Repository Authority 可定位的 durable owner 中。默认推荐 `docs/requirements/**`，但 Consumer 可以使用等价结构。

Project Terminology Authority 若被采用，也必须是 Requirement Authority Index 或等价 locator 可发现的 durable owner；本 Architecture 不要求固定 `terminology.md` 文件名或目录。

### 13.5 Update

修改事实时优先更新真实 owner，再最小传播 locator / relation / affected reference。不得在下游 Specification、Technical Plan 或聊天中静默覆盖上游 Requirement。

### 13.6 Supersede

新 owner 替代旧 owner 时，应更新当前 index / references，并删除或明确废止旧 current Authority；历史由 Git / Issue / PR 保留，不通过长期兼容文档维持两套事实。

### 13.7 Escalation

发现以下情况时返回拥有该责任的 Requirement Method / Human Authority：

- current Authority 冲突；
- unique owner 不清晰；
- 多个合理答案会实质改变 Product behavior / Acceptance；
- 变更超出当前授权；
- 批量语义变换需要独立 review。

## 14. 与 Feature Specification 的边界

Requirement Authority 持有跨多个 Feature 长期持续成立的事实；Feature Specification 只拥有当前 change 对这些事实的具体适用、范围、Observable Behavior、Failure Behavior 与 Acceptance Criteria。

Specification 不应为了自包含复制完整 Requirement Baseline。

Feature 中确认的新术语、不变量、规则或 data semantics 如果具有长期跨 Feature 价值，应提升到真实 Requirement owner；如果其核心问题是跨 Capability canonical business naming，则进入已建立的 Project Terminology Authority，再由 Specification 引用。

## 15. 与 Architecture 的边界

Requirement 描述系统必须做什么、什么业务事实成立、系统必须具有什么可验收性质。

Architecture 描述系统如何被长期组织，以及哪些结构约束跨 Feature 持续成立。

Requirement Authority 可以拥有产品 / 系统责任边界，但不拥有内部 component boundary、deployment topology、framework composition 等普通 architecture fact。

两者存在冲突时，Architecture 不通过技术判断覆盖 Requirement；先返回 Requirement owner 解决 Product / Domain fact。