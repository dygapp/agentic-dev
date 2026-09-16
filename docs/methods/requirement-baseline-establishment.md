---
id: method:requirement-baseline-establishment
type: method
status: active
---

# 需求基线建立方法

## 1. 目标

本方法面向普通软件 Consumer 项目的项目建立或重大需求基线重建，负责把原始、碎片化、不同可信度且可能相互冲突的 Project Inputs，收敛为一套可持续维护、具有明确 semantic ownership、可由 Fresh Context Agent 直接消费的 Requirement Baseline。

它解决的是：

> 后续 Feature Development 应该依赖什么长期 Requirement Authority，以及这些长期事实如何从原始材料被提取、组织、推导、确认和复核。

本方法不负责具体 Feature Specification，也不负责长期 Architecture decision。完成后只声明 `Requirement Baseline Ready`；如果仍存在阻塞多个 Feature 的长期 architecture driver，由 Repository-local Method selector 决定是否进入 `method:architecture-clarification`。具体 Feature / change 再进入 `method:ai-development`。

## 2. 进入条件

满足以下任一情况时，可以选择本 Method：

- greenfield software project / new product 尚不存在可靠 Requirement Baseline；
- 原始需求材料已经较完整，但尚未形成稳定的 Requirement Authority、边界、索引与事实归属；
- legacy modernization / rewrite，需要从旧系统、旧文档、现行规则和当前决策重建可信需求基线；
- Requirement Authority 已碎片化、冲突、重复或长期 owner 不清晰；
- 多个当前或预期 Feature 因同一组系统性 Requirement gap / conflict / ambiguity 无法可靠进入 Specification。

以下情况不应机械进入完整 Method：

- 单个 Feature 的局部产品意图歧义；
- 普通 bugfix 或小范围 change；
- 已有稳定 Requirement Baseline，只需要增量更新一个长期事实；
- 单 Feature 的实现 HOW 或局部 Architecture choice；
- 只是文档很多、技术复杂，但长期 Requirement Context 本身已足够稳定。

## 3. 与其他 Method 的关系

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

本 Method 是新项目进入普通 Feature Development 的上游 Project Establishment work kind，但不是每个 Feature 都要重复执行的前置步骤。

Requirement Baseline 一旦有效，后续普通 Feature 直接按 Repository-local selector 进入 `method:ai-development`。只有基线本身出现系统性缺口、冲突或需要重建时，才重新进入本 Method 或返回其中拥有该责任的阶段。

## 4. 生命周期

```text
Establish Sources & Authority
→ Extract Requirement Facts
→ Structure Requirement Authority
→ Resolve Requirement Unknowns
→ Review Requirement Baseline
→ Requirement Convergence
→ Requirement Baseline Ready
```

正式阶段六个：

1. Establish Sources & Authority；
2. Extract Requirement Facts；
3. Structure Requirement Authority；
4. Resolve Requirement Unknowns；
5. Review Requirement Baseline；
6. Requirement Convergence。

Project Terminology Governance 不增加新的 Method 阶段。Consumer 确有跨 Capability terminology need 时，只把 terminology responsibility 嵌入上述六阶段；没有真实需要时不建立 glossary 或额外流程。

### 4.1 Stable phase identities

- Establish Sources & Authority → `establish-requirement-sources`；
- Extract Requirement Facts → `extract-requirements`；
- Structure Requirement Authority → `structure-requirements`；
- Resolve Requirement Unknowns → `resolve-requirements`；
- Review Requirement Baseline → `review-requirements`；
- Requirement Convergence → `requirement-convergence`。

这些 token 只属于 `method:requirement-baseline-establishment`。

## 5. Establish Sources & Authority

先明确当前需求建立可以使用哪些输入、它们具有何种事实地位，以及哪些现有长期 owner 可以继续使用。

原始输入可以包括：

- 客户 / 用户描述；
- 访谈与会话决定；
- 合同、招标文件、法规、制度；
- PRD、原型、历史需求文档；
- legacy system / historical behavior；
- 外部接口、数据、第三方约束；
- 当前 Repository 已有 Requirement / Domain / Architecture Authority；
- 其他 reference / analysis material。

至少区分：

- current authoritative input；
- legacy input；
- reference input；
- external dependency；
- analysis material；
- conversation / human decision；
- unknown。

不得把“材料存在”“旧系统这样做”“历史文档这样写”直接等同于当前 Requirement。

如果项目已有 terminology / domain glossary / naming owner，本阶段确认它是否已经承担唯一 current terminology ownership、其 source role 是否清楚，以及 Requirement Authority Index 或等价 locator 是否可以定位。不要为了目录归属或历史命名把既有唯一 owner 强制迁移成新的 Requirement artifact，也不要再建立第二 owner。外部协议、政策原文或历史 schema 中的名称可以保留原样，但不能因为来源存在就自动成为内部 canonical terminology。

不要求建立永久 source catalog。只有当前澄清、复核或跨上下文恢复确实需要的 source inventory 才暂存；其默认是 transitional artifact，不自动成为 Requirement Authority。

退出条件：后续事实抽取可以明确判断来源可信度、时间边界与当前 Authority owner，不会把不同历史时期或不同证据等级平权混合。

## 6. Extract Requirement Facts

需求抽取优先从业务语义出发，而不是从 UI、数据库或代码结构出发。

至少检查六类事实：

- business object；
- business activity / workflow；
- business rule；
- state / lifecycle；
- actor / responsibility；
- external dependency / input / output。

一个高价值事实表达通常能够回答：

> 谁，在什么条件下，对什么业务对象执行什么活动，受到什么规则与状态约束，最终产生什么业务结果？

同时识别：

- product / domain goal and boundary；
- data semantics；
- failure / exception behavior；
- quality / compliance requirement；
- acceptance intent；
- out-of-scope boundary。

当同一长期业务概念跨多个 Capability / source 出现时，同时识别 terminology candidate，例如：并行中文称谓、多个英文业务词、current / legacy / external 名称映射，以及可能影响角色、状态、数据语义或下游业务命名的近义词。候选只进入临时 analysis workspace，不在抽取阶段直接建立 canonical term。

页面、按钮、菜单、API shape、数据库表、类 / 包、事务 / 缓存等默认不作为需求边界来源；只有它们本身是合同、法规、外部接口或其他 authoritative constraint 时，才作为 Requirement 保留。代码 identifier 的大小写、后缀、package layout 等技术命名也不是 terminology candidate，除非其背后暴露了尚未解决的业务语义歧义。

退出条件：主要长期业务事实已经能够被识别，并可以进入 ownership / capability boundary 分析；不要求在此阶段穷举未来所有 Feature 细节。

## 7. Structure Requirement Authority

把已提取事实组织到明确的长期 semantic owner，而不是建立第二套持久业务模型。

通用 ownership 与推荐 `docs/requirements` 信息架构由 `architecture:requirement-authority` 定义。本阶段至少完成：

- project / system scope 与责任边界；
- Requirement Capability / durable business owner 划分；
- cross-capability Requirement 的归属；
- non-functional Requirement 的归属；
- Requirement Authority Index / locator；
- transitional analysis artifact 与 durable Authority 的边界。

如果 terminology candidate 只在单一 Capability 内使用且真实 owner 已清晰，继续由该 Capability owner 持有；只有术语跨多个 Capability / Feature 长期成立、存在 canonical naming / alias mapping 需要且独立 owner 能减少语义漂移时，才建立或复用 Project Terminology Authority。物理路径不由本 Method 固定，但必须能由 Requirement Authority Index 或等价 locator 找到。

Requirement Capability 边界优先依据：

- 核心业务对象；
- 主要业务结果；
- 生命周期；
- Actor / responsibility；
- 可独立验收的长期业务责任；
- 事实是否能够由一个 owner 合理承担。

不得仅因为存在不同页面、菜单、微服务、数据库表或代码模块就建立新的 Requirement Capability。

本 Method 不要求 Consumer 使用 `L1/L2/L3` 编号；也不要求一次性穷举全部未来 Scenario。目标是让主要长期事实都有 owner，后续 Feature 可以确定性地找到需求来源。

退出条件：核心事实已经有唯一长期 owner，Requirement index 可以定位主要 Authority，且不存在明显重复 / 平行事实源。

## 8. Resolve Requirement Unknowns

### 8.1 先分类，不默认提问

每个未决项至少分为：

- **Confirmed**：已有 Authority 明确支持；
- **Deterministically Derived**：可由已确认事实唯一推导；
- **Authoritative Default**：已存在于 Requirement Authority 中、具有明确适用范围的 Project Requirement Default；
- **Provisional Minimal Default**：没有 Evidence 支持额外业务机制时，为形成可 Review 的完整 Capability 草稿而采用的最小工作假设；
- **Material Ambiguity**：存在多个合理业务解释；
- **Conflict**：多个 Authority 给出相互不兼容事实；
- **External Dependency**：依赖外部事实或材料；
- **Design Item**：属于 Architecture / Technical Planning / Execute 的 HOW；
- **Unsupported Assumption**：当前没有 Evidence 支持、也不满足最小默认边界的其他假设。

Terminology candidate 在本阶段还应能区分：existing canonical terminology、deterministically derived terminology、material terminology ambiguity、Capability-local term、technical naming item 与 external / legacy source name。只有前述分类不足以安全决定 canonical business meaning 时，才可能升级为 Human Blocking Question；若业务含义已经确定，只剩 canonical naming / alias mapping / cross-capability naming coordination，则记录为 non-blocking terminology decision，留到 Capability-level Review 集中确认。

“未知”不等于“必须问人”。

### 8.2 Derive → Default → Ask → Review

需求讨论遵守以下顺序：

1. 当前 Authority 已能回答 → 直接使用，不提问；
2. 已确认事实可唯一推导 → 自动推导，不提问；
3. 当前 Requirement Authority 已建立明确 Project Requirement Default → 按其 scope 应用，不提问；
4. 属于 Design Item → 推迟到正确责任层，不提问；
5. 缺少 Evidence 支持额外业务机制 → 可以采用 Provisional Minimal Default 形成当前 Capability 草稿，不逐项提问；
6. 只有真实 Material Ambiguity / Conflict 会产生实质不同产品结果，并阻塞当前 Requirement Baseline 时，才 Ask Human；
7. 完成一个 Requirement Capability 后进行整体 Review，集中确认自动推导、Authoritative Default 与 Provisional Minimal Default 的结果，允许人工一次性纠错 / 补充。

没有 Evidence 时，默认**不额外创造**审核、审批、复核、通知、整改、版本、归档、自动同步、批量能力、额外状态、额外角色或类似业务机制。这个“最小行为”只是减少无效询问的 drafting default，不自动等于已确认长期 Requirement。

Project Requirement Default 若要跨多个 Capability 直接复用，必须先进入真实 Requirement Authority，并明确其适用范围与必要 override 条件；聊天中的口头习惯、模型常识或历史项目经验不能直接充当 Authoritative Default。

Provisional Minimal Default 必须在当前 Capability Human Review 中可见。只有 Review 通过、Product / Requirement Authority 明确认可，或其结果随后被其他有效 Authority 支持后，相关长期事实才能 promote 到 durable Requirement owner；在此之前不得把 provisional default 当成已确认基线事实传播到其他 Capability。

### 8.3 Human Question Gate

一个候选问题只有同时满足以下条件才升级为 Human Blocking Question：

1. 当前 Authority 无法唯一回答；
2. 不能由已确认事实唯一推导；
3. 没有适用且已确认的 Authoritative Default；
4. 不是可以安全推迟的 Design Item；
5. 存在两个或以上合理业务解释；
6. 不同答案会实质改变 Scope、State、Permission、Data Semantics、Business Result、Compliance 或 Acceptance；
7. 不解决会阻塞当前 Requirement Baseline。

Terminology 不绕过这七项条件。只有 terminology ambiguity 同时会实质改变 business meaning / scope、responsibility、data semantics、Acceptance 或其他产品语义，并且阻塞当前 Requirement Baseline 时，才升级为 Human Blocking Question。业务语义已经确定但仍需统一 canonical Chinese / English naming、alias mapping 或 cross-capability naming 的情况，记录为 non-blocking terminology decision，在 Capability-level Review 集中确认；拼写风格、大小写、类名后缀、package layout 等继续属于 Technical / Code convention。

否则应推导、应用 Authoritative Default、采用可 Review 的 Provisional Minimal Default、记录为 non-blocking open item，或推迟到后续责任层。

### 8.4 Conversation protocol

会话只是需求获取渠道，不是长期 Authority。

普通需求会话默认使用 delta-only 输出：

- 不重复长篇重述已确认历史；
- 每个问题只给出 Decision、必要 Context、Impact 与 Options / expected answer；
- 先问上游控制性问题，再推导下游结果；
- 不通过逐项“是否需要某机制”的否定式穷举完成需求确认；
- Human Decision 应尽快 promote 到真实 Requirement Authority，后续会话重新从 Authority 恢复。

问题数量应由真实 Blocking Ambiguity 数决定，而不是为了形成“完整讨论”凑足固定数量。连续没有真实 blocking question 时，应停止提问并继续完成当前 Capability。

## 9. Clarification Depth Stop Condition

当以下信息已经足以唯一决定主要业务行为与验收时，Requirement 下钻应停止：

- Goal / Scope / Out of Scope；
- 核心业务对象；
- Actor / Responsibility；
- 主要状态与转换；
- 关键业务规则；
- 数据范围 / 语义；
- 跨 Capability 输入输出；
- 主要失败 / exception 结果；
- Acceptance。

如果继续下钻主要产生字段、按钮、页面布局、API、数据库、事务、缓存、类 / 包或施工顺序，则默认已经进入 Design / Technical Planning / Execute 责任。

如果继续讨论 terminology 主要只剩 identifier casing、package / filename style、DTO / Entity suffix 等技术表达，也应停止 Requirement 下钻并交给对应 Technical / Code convention owner。

如果下游结果已经由上游规则唯一决定，也必须停止逐项追问并直接记录推导结果。

## 10. Review Requirement Baseline

### 10.1 Capability-level Human Review

每个主要 Requirement Capability 达到可读状态后，可以进行一次整体 Human Review，重点查看：

- 范围是否正确；
- AI 自动推导是否符合意图；
- Authoritative Default 是否被正确应用；
- Provisional Minimal Default 是否合理、是否应确认 / 修正 / 删除；
- 是否遗漏真实高价值业务规则；
- 是否错误创造额外机制；
- remaining ambiguity 是否确实需要人工裁决。

如果当前 Baseline 使用 Project Terminology Authority，Review 还应集中检查少量真正需要人工的 terminology decision：影响业务含义 / 责任 / Acceptance 的 material ambiguity 应在进入 Review 前按 Question Gate 正确处理；业务语义已经确定但仍需统一 canonical naming / alias mapping / cross-capability naming coordination 的 non-blocking decision 可以在本次 Review 集中确认。已经由 Current Authority 唯一决定的术语不逐条重复确认。确认结果必须写回真实 terminology owner，而不是只修改候选表或 Review Draft。

人工主要作为 Product Authority / Reviewer，而不是逐字段需求生成器。

如果 Consumer 已采用 `architecture:human-review` 与 `skill:human-review`，本阶段可以调用该 Skill 生成结构化 Markdown 评审草稿、分类人工反馈并完成语义回写。没有显式交付格式要求时，不因为进行 Capability-level Human Review 自动生成 DOCX、HTML 或其他最终交付物。

人工评审产生的展示性修改只作用于评审投影；会改变长期需求语义的反馈必须回写真实 Requirement owner。若当前执行者没有对应写入授权，应明确输出 Required Authority Action，而不是让决定停留在评审草稿或会话中。

Consumer 未采用 `skill:human-review` 时，本 Method 的 Capability-level Human Review 责任仍然成立；Skill 是可复用执行能力，不是本阶段存在的前提。

### 10.2 Independent semantic review

以下任一情况成立时，在 Baseline Ready 前必须执行独立语义复核：

1. 从 legacy / heterogeneous sources 重建 Requirement Baseline；
2. Requirement Authority 发生大规模重构、批量迁移、结构化改写、摘要化或 AI 辅助语义收敛；
3. 多个 Authority 冲突并发生长期事实合并、取舍或覆盖；
4. 一次处理批量改变业务状态、生命周期、权限、范围、数据语义或验收不变量。

Review 必须可以核对 source / decision / resulting Authority；格式、链接、lint 或“Fresh Context 可读”不能单独证明语义正确。

## 11. Requirement Convergence

只有同时满足以下条件，才可以声明 `Requirement Baseline Ready`：

1. Project Goal / Scope / Out of Scope 明确；
2. 产品 / 系统责任边界明确；
3. 主要 Requirement Capability 已建立并有明确 owner；
4. 核心业务对象、Actor、规则、状态 / lifecycle 与重要 data semantics 可定位；
5. 同一长期事实没有已知平行 Authority；
6. cross-capability Requirement 已正确归属；
7. 重要可验收 NFR 已有 owner；
8. 会阻止后续可靠 Feature Specification 的 Requirement conflict / ambiguity 已关闭；
9. remaining open item 已明确为 external / design / non-blocking，并有 owner 或处理路径；
10. Requirement Authority Index 可以让 Fresh Context Agent 定位最小必要需求上下文；
11. 命中强制 independent semantic review 的场景已经 PASS；
12. Fresh Context Agent 可以在不依赖历史聊天或临时 analysis artifact 的情况下理解一个主要 Requirement Capability 的长期事实；
13. 不存在仍被当成 durable Requirement 使用、但尚未经过 Capability Review / Authority promotion 的 Provisional Minimal Default；
14. 如果建立了 Project Terminology Authority，durable canonical terminology 已实际写回并重新读取确认，temporary candidate inventory 不再承担 Current Authority，locator 可以让相关下游任务按需发现它。

真正存在 blocker 时必须保持 NOT READY。

## 12. Requirement Authority Artifact lifecycle

Requirement Authority 的结构、README / index / fact owner 边界、推荐目录、producer / consumer / update / supersede / escalation contract 由 `architecture:requirement-authority` 统一定义。

本 Method 只负责在正确阶段产生或更新这些 owner，不复制第二套信息架构正文。

默认 transitional / disposable：

- source inventory；
- extraction table；
- ambiguity candidate list；
- terminology candidate inventory；
- comparison matrix；
- flow / state / relationship view；
- human review batch；
- conversation scratchpad。

只要能够从 Requirement Authority 唯一再生，就不应为了 AI 理解方便建立新的持久中间 Authority。跨需求、功能规格、架构与技术方案通用的人工评审草稿、派生视图与反馈回写边界由 `architecture:human-review` 持有。

## 13. Return contract

完成后只声明：

```text
Requirement Baseline Ready
```

它不等于：

```text
Architecture complete
Specification created
Execution Unit created
Execute / Integrate authority granted
```

下一步由 Repository-local Method selector 根据当前 work kind 决定：

- 没有 systemic architecture blocker → 可进入具体 Feature 的 `method:ai-development`；
- 存在多个 Feature 共同依赖、长期、高成本难逆并阻塞可靠开发的 architecture driver → 可进入 `method:architecture-clarification`；
- 后续 Feature 发现局部 Requirement ambiguity → 返回真实 Requirement owner；
- 后续发现系统性 Requirement Baseline gap → 返回本 Method 中拥有该责任的阶段，必要时重新选择完整 Method。

## 14. Skill / Rule 边界

本 Method 当前不要求新的 `requirements-analysis`、`requirement-elicitation` 或 terminology Skill。只有未来真实 Consumer 使用证明某个 procedure 在多个 Repository 中稳定、可独立调用并能显著减少重复错误时，才评估 Skill admission。

`skill:human-review` 是跨需求、功能规格、架构与技术方案复用的人工评审 supporting capability，不拥有需求抽取、需求分析、terminology ownership 或 Requirement Baseline lifecycle，因此不改变上述 Skill 准入结论。

同样不因为本 Method 增加 terminology responsibility 就复制一组 Requirement / Terminology Rules。`Derive → Default → Ask → Review`、Question Gate、Depth Stop 与 terminology admission 都属于本 Method / Requirement Authority 的过程与 ownership contract；只有未来出现能够独立于 Method 存在的 policy gap 时，才进入 Rule owner。

## 15. Evidence maturity

本 Method 的 v1 contract 主要来自大型真实 Consumer 项目前期需求分析的正向与负向历史 Evidence：包括能力边界重构、穷举式 L3 清单退出、持久中间业务模型退出、AI-ready 迁移中的语义漂移反例、术语 ambiguity → Human Decision → Authority Promotion 闭环，以及长期问答循环的真实摩擦。

Project Terminology Governance 的当前增量同样主要来自该历史 Consumer corpus，并由现有 Requirement Authority / Question Gate / Human Review 语义共同约束。它建立的是有条件的 terminology owner 与 lifecycle，不证明固定 glossary 路径、完整术语表模板或历史编号体系应传播到其他 Consumer。

这些 Evidence 用于提炼可复用责任和 anti-pattern，不证明任何历史目录、阶段名或具体模板应被机械复制到其他 Consumer。