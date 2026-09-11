# 资源发现架构

**状态：** 基线 v0.1  
**性质：** 跨仓库可复用的本地资源发现与职责路由架构  
**跟踪：** Issue #111

## 1. 目的

本文定义 `agentic-dev` 的长期资源发现架构：在使用方仓库已经拥有当前资源和仓库权威的前提下，让新上下文或当前职责只依赖本地事实找到真正需要的资源，得到：

```text
一个主职责
+ 最小辅助上下文
+ 可解释阶段动作
```

本文直接消费：

- `docs/architecture/consumer-lifecycle.md`；
- `docs/architecture/agent-resource-model.md`；
- 当前 Method / Skill Contract；
- v2 已通过真实使用方验证的发现、路由、按需加载与失败关闭行为。

V3-06 **不重新定义资源身份、方法阶段或 Skill 职责**。发现架构只能组织、筛选、定位和加载真实资源。

## 2. 不变量

### 2.1 使用方仓库权威优先

发现结果不能覆盖使用方仓库权威，也不能通过数值优先级、命中分数或模型置信度重写项目事实。

### 2.2 普通运行只依赖本地当前资源

采用 / 升级完成后，普通运行默认只读取使用方本地当前资源。发现失败、索引陈旧或无命中都不构成自动访问 upstream 的理由。

### 2.3 派生发现不拥有规范正文

发现映射、索引、Catalog、查询提示、路由结果和运行 trace 都不能保存第二份 Requirement、Architecture、Policy、Rule 或 Skill procedure。

### 2.4 不维护第二当前状态真值

资源是否当前有效继续由：

```text
当前仓库权威
+ V3-01 四维语义
+ 资源原生当前状态（如有）
+ 真实取代 / 禁用关系
```

共同确定。发现层只能验证、筛选或投射当前候选。

### 2.5 渐进式披露

目标是**最小正确集合**：不遗漏当前正确工作所必需的资源，同时不加载明显无关正文。

### 2.6 一个主职责

一次发现决策只能有一个当前主职责。验证、工程纪律、平台能力、外部操作规则等可以构成辅助上下文，但只要没有改变职责所有权，就不能夺取主职责。

如果一次请求包含多个彼此独立的目标，应先按当前仓库权威与工作关系拆成可顺序处理的当前目标，再分别形成发现决策；不把多个独立职责平铺成多个同时有效的主职责。

### 2.7 一个 current 发现机制

同一 Runtime scope / discovery responsibility 只能有一个被声明为 current 的派生机制。

一个已复核发现映射及其**由该映射确定性生成的运行视图**属于同一个机制；运行视图不能独立维护另一套语义。

## 3. 最小逻辑架构

V3-06 不把 v2 的 Manifest + Catalog 两层提升为必选架构：

```text
薄本地发现入口
        ↓
本地当前资源与稳定 Authority Entry
        ↓
可选：已复核发现映射
        ↓
可选：纯生成运行视图
        ↓
临时发现决策
```

已复核发现映射和运行视图都可以不存在。

### 3.1 本地发现入口

每个完成 `agentic-dev` 采用、需要普通运行的仓库，都必须能从薄 Bootstrap 到达一个**本地发现入口（Local Discovery Entry）**。

它是稳定 seam，不是新的规则正文 owner。至少指向：

- 当前仓库权威入口；
- 当前发现映射 / 运行视图（如有）；
- 没有派生映射时的原生 current entries；
- 发现失败时的本地 Authority fallback。

它不能复制完整职责 / 风险路由表、当前 Roadmap Gate、规则摘要、完整 Skill 正文或 upstream 项目状态。

物理上可以是 `AGENTS.md` / Authority Map / 小型本地导航 / Runtime View 的稳定指针，不要求统一文件名。

### 3.2 真实本地资源

真实输入包括：

- 当前 Requirement / Specification / Architecture / Roadmap 等项目权威；
- 当前本地 Policy / Standard；
- 已采用的 Skill / Engineering Discipline / Technology / Verification Profile；
- V3-05 判定需要独立发现的其他当前资源。

文件只是载体；mixed 文件按 V3-05 已确定的稳定资源单元处理。

### 3.3 已复核发现映射

当固定入口 + 资源原生信息不足以低成本、稳定发现时，可以维护一个**已复核发现映射（Reviewed Discovery Map）**。

它是**非规范性、但需要维护和复核的派生语义输入**，可以记录：

- 真实资源稳定引用与本地定位信息；
- 资源原生发现信息的引用；
- 跨资源正规化并经复核的职责 / 条件 / 风险提示；
- 非规范性加载提示；
- 来源绑定；
- 声称覆盖的发现范围和覆盖锚点。

它不保存：

- 规范正文或规则摘要；
- 第二份 `active/current` 真值；
- 当前 Issue / PR / Actions / Gate 状态副本；
- 固定推荐答案；
- 全局数值 priority；
- 隐藏 Method / Stage / Skill routing 语义。

“派生”不等于“可以由生成器重新猜出来”。已完成的跨资源语义复核必须显式维护或重新复核。

### 3.4 纯生成运行视图

需要更紧凑运行入口时，可以从当前真实资源、资源原生发现信息和 current Reviewed Discovery Map（如有）确定性生成 Runtime View / Catalog。

它：

- 可以删除 / 重建；
- 不独立维护语义映射；
- 不拥有当前状态真值；
- 不允许出现映射层没有的“智能补充”；
- 只是同一发现机制的运行投影。

### 3.5 临时发现决策

每次任务根据当前事实形成一个临时发现决策。它默认不持久化，也不构成长久权威。

至少能够表达：

- 当前主职责；
- `routing-only` 或真正执行；
- `continue / return / fail-closed / escalate` 等阶段动作；
- 主资源与最小辅助资源指针；
- 真正执行时需要加载的 Skill；
- 简短可解释理由；
- 哪个旧 routing / Readiness / Execute 状态已失效（如有）。

字段名不是固定协议。

## 4. 什么时候需要已复核发现映射

以下条件同时成立时，可以**不维护** Reviewed Discovery Map：

- 独立发现资源数量较少；
- Authority Entry 稳定且可直接定位；
- Skill / Profile 已有足够原生发现信息；
- 条件性横切资源很少；
- 新上下文可在可接受读取成本内可靠得到主职责与辅助集合；
- 不存在跨多个 mixed resource 做稳定语义切片发现的持续问题。

出现以下持续需求之一时，Map 才有明确价值：

- 多类异构资源需要统一按职责 / 条件筛选；
- mixed-resource 稳定区块需要独立发现；
- 工程纪律 / 验证能力 / 平台能力按条件横切多个职责；
- 每次手工扫描目录 / Guide 的成本明显过高；
- 需要保存已经完成的跨资源语义正规化判断；
- 需要机器可读 trace 证明普通运行没有访问 upstream 或加载无关能力。

即使需要，也只维护**一个 current Reviewed Discovery Map**。

## 5. 发现覆盖与集合完整性

只有逐条来源绑定不足以保证发现完整性：仓库可能新增一个应被发现的资源，而所有旧条目仍然“新鲜”。因此 Map 必须明确自己声称覆盖什么。

### 5.1 覆盖范围

Map 可以只覆盖部分资源，例如：

- 当前 Skill inventory；
- 可独立消费的工程纪律 / 验证能力；
- 技术 / 验证画像；
- 某组条件性仓库本地规则；
- 已拆分的 mixed-resource sections。

Map 不要求覆盖所有 Markdown，也不能模糊声称“覆盖整个仓库”。

### 5.2 覆盖锚点

每个声称完整覆盖的范围必须绑定能够反映真实成员集合的本地 current anchor，例如当前仓库明确指定的：

- 资源 membership owner / Authority Map；
- Skill / Profile current entry；
- 稳定资源描述集合；
- 其他能由仓库权威确认成员集合的入口。

覆盖锚点不拥有被覆盖资源正文，也不重新定义资源身份。

如果锚点本身是派生 inventory，它只有满足以下条件才可支撑完整性判断：

- 能从真实 current resources / membership owner 确定性重建；
- 自身来源时效性与成员 identity 可验证；
- 不依赖另一个未绑定手工清单证明自己完整。

否则它只能作为导航提示，不能成为 completeness anchor。

### 5.3 覆盖漂移

以下变化会使对应覆盖范围失效：

- 新增应独立发现的资源；
- 删除 / supersede 已发现资源；
- mixed-resource section 被拆分、合并或重新分类；
- current membership owner / Authority Entry 发生变化；
- 覆盖范围被当前仓库权威调整。

发生覆盖漂移后，不能因为旧条目的 source hash 都没变就继续声称 Map 完整。

## 6. 当前资源集合

当前资源集合是每次发现前形成的**逻辑集合**，不是新的 Authority 或独立状态表。

至少排除：

- 仅历史 / 证据资源；
- 外部未采用资源；
- 已被真实语义所有者明确 supersede 的旧资源；
- 当前仓库明确 disabled / excluded 的资源；
- locator / selector 已不可解析且无法由当前权威确认身份的资源。

Map / Runtime View 可以只暴露当前候选，但 filtering 必须从真实 owner / 关系重新计算或验证，并确认相关覆盖锚点没有未复核成员漂移。

禁止用旧 Catalog 的 `active` 字段覆盖真实 current 状态。

## 7. 当前任务事实

资源集合说明“现在有哪些资源”，任务事实说明“这次正在解决什么”。两者必须分开。

每次发现只使用当前可观察事实：

- **目标事实**：当前请求的真实责任；
- **权威事实**：所依赖本地权威是否存在、当前、可解析、无冲突；
- **生命周期事实**：当前 Work / Readiness / Execute Authority / Evidence 的真实状态；
- **问题事实**：是已定义 expected behavior 下的实现 / runtime 异常，还是上游权威本身缺失 / 冲突；
- **已知条件 / 风险**：只有当前证据已经支持、且会改变资源集合的条件。

这些事实随任务变化，默认不持久化进资源结构或 Reviewed Discovery Map，也不成为未来任务默认真值。未知值不得为了提高召回率而猜测。

## 8. 候选发现

候选发现使用：

```text
当前资源集合
+ 当前任务事实
+ only-known 条件 / 风险
```

候选可以直接来自本地 Authority Entry / 资源原生信息，也可以由 Reviewed Discovery Map 加速；Map 不是唯一入口。

### 8.1 命中不等于适用

候选命中不能直接推出：

- 规则当前已经适用；
- Skill 必须加载；
- 资源可以覆盖使用方权威；
- 当前阶段仍可继续执行。

### 8.2 不使用固定 Top-K

如果 6 个资源都对正确执行必需，就保留 6 个；如果只有 1 个，就不为了固定数量补足。

### 8.3 无命中

无命中只有在相关覆盖范围的覆盖锚点和语义映射都 current 时，才表示“该已覆盖范围内没有命中”；它仍不能自动证明当前任务完全没有适用规则。

以下任一情况必须回到本地 Authority Entry 扩展发现：

- 当前任务落在 Map 未声明覆盖的范围；
- 覆盖锚点不存在或陈旧；
- 成员集合已变化但映射尚未复核；
- 当前仍存在治理、验证或风险事实。

### 8.4 歧义

允许读取少量 routing / constraint owner 消歧。仍无法可靠区分时停止高影响动作，进入本地失败关闭 / 必要人工升级，而不是按模型概率猜主职责。

## 9. 主职责与最小辅助上下文

一次发现决策只允许一个主职责。

解析规则：

1. 使用方仓库权威先决定项目事实、权限与当前约束；
2. 当前 Method / Skill Contract 判定基础权威存在缺口时，拥有该缺口的既有职责成为新的主职责；
3. 前置基础有效时，当前明确请求的稳定职责保持主职责；
4. 只有 expected behavior 已由当前权威明确、且当前调试契约允许时，`systematic-debug` 才成为主职责；
5. 验证、平台、外部操作、工程纪律等只要没有改变职责所有权，就保持辅助上下文。

这些规则只描述 discovery 怎样消费现有 Method / Skill Contract，不创建新的方法优先级或第二份阶段返回规则。

辅助资源只有同时满足以下条件才进入最小集合：

- 当前触发条件有事实支持；
- 会改变主职责的正确执行或完成声明；
- 没有被更具体的使用方当前权威合法覆盖 / 取代；
- 来源 / locator / 派生语义绑定当前有效；
- 若依赖 Map，相关覆盖范围当前完整。

“可能有用”“主题相关”“以后也许需要”都不足以进入集合。

## 10. routing-only 与按需 Skill

### 10.1 routing-only

当前只需要判断下一职责、Stage Return、Readiness / Execute Authority 是否仍有效，且现有本地权威 + 原生发现信息 / 派生提示已经足够时：

```text
resolve responsibility
→ 返回主职责 + 理由 + 必要资源指针
→ stop
```

不得因为发现 Skill locator 就加载完整 Skill。

### 10.2 真正执行职责

只有当前任务要继续执行主职责时才：

1. 确认对应本地 Skill 当前可用；
2. 加载主职责的完整 Skill；
3. 加载当前必要的最小本地权威与辅助约束；
4. 按 Skill Contract 执行；
5. 出现 Stage Return signal 时停止当前职责并重新发现。

平台专项 Skill 只有当前条件真实命中、主职责确实需要且仓库权威允许时，才作为辅助能力按需加载。

普通运行不批量加载所有 Skill。

## 11. Stage Return 与旧状态

V3-06 不维护第二份“哪些变化使 Readiness / Execute Authority 失效”的方法规则；这些判断继续由当前 Method、Skill Contract 与对应 Authority 单点拥有。

发现层只负责以下后果：

```text
现有 owner 判定需要 Stage Return / 旧执行基础失效
→ 停止当前职责
→ 丢弃旧发现决策作为继续授权
→ 重新读取受影响本地当前权威
→ 重新形成任务事实
→ 重新发现 / 路由
```

如果现有 Method / Skill Contract 与证据确认只是实现缺陷修复、上游语义基础仍有效，则可以按原 owner 的规则恢复执行路径；V3-06 不机械要求重跑完整生命周期。

## 12. 失败关闭与本地回退

以下情况停止依赖当前派生发现：

- Reviewed Discovery Map / Runtime View 陈旧；
- 覆盖锚点陈旧、缺失或成员集合漂移；
- locator / selector 丢失；
- 当前语义所有者不明确；
- 无命中但仍存在治理 / 风险事实；
- 多个主职责无法可靠区分；
- override / supersede 关系不明确；
- 高影响授权、重大 Architecture、安全 / 隐私或不可逆边界不清；
- 需要的 Skill 本地不存在或身份无法确认；
- 资源原生结构与伴随描述 / 派生提示矛盾。

回退：

```text
停止使用当前派生结果
→ 回到使用方本地当前权威 / 稳定 Authority Entry
→ 按问题扩大最小本地读取
→ 重新确定资源与职责
→ 只有本地权威 / 权限要求时才升级人工
```

普通运行的失败关闭不自动打开 upstream。

## 13. 已复核发现映射的 currentness

### 13.1 纯定位映射

如果条目只保存 resource ref + locator，不提炼规则适用语义：

- 正文普通变化不自动使 locator 陈旧；
- 路径、selector 或 authority role 被取代时才更新；
- runtime 始终读取真实 current source。

这继承 v2 `current-locator` 的有效思想。

### 13.2 语义提炼映射

如果条目保存跨资源正规化职责 / 条件 / 风险提示：

- 必须绑定已复核 source / selector identity；
- source 语义变化后旧提示立即退出可信候选；
- 不能只重算 hash / commit id 就自动恢复；
- 必须重新判断变化是否影响派生语义；
- 新语义映射只有经过当前仓库允许的人工 / AI 复核后才能重新进入 current Map。

这继承 v2 `semantic-reviewed` 原则，但绑定的是派生提示，不是资源身份本身。

### 13.3 覆盖绑定

Map 必须验证声称完整覆盖的覆盖锚点：

- 成员集合未变化：可继续使用现有映射；
- 变化且能精确定位受影响资源：只让对应映射 / 覆盖范围失效；
- 无法可靠判断影响范围：整个相关覆盖范围失败关闭；
- 不得仅重算 anchor hash 就自动把新增 / 重分类资源视为已完成语义映射。

### 13.4 删除与重建

Reviewed Discovery Map 不拥有规范正文，所以删除它不会删除项目 / 规则事实；但已复核的跨资源语义映射不能由生成器无语义判断地自动恢复。

删除后只有两条安全路径：

1. 退回本地 Authority Entry + 资源原生发现信息；或
2. 重新执行必要语义复核，建立新的 current Map。

“可从真实 owner 重新分析得到”不等于“可确定性生成”。

## 14. 纯生成 Runtime View 与适配器

Runtime View 必须能从：

- 当前真实资源状态；
- 当前资源原生发现信息；
- current Reviewed Discovery Map（如有）；
- 当前覆盖锚点 identities；

确定性重建。

生成过程只做：

- source / selector resolution；
- coverage / current-set filtering；
- schema / reference validation；
- 已复核派生提示投影；
- compact serialization。

生成器 / Runtime Adapter 可以执行这些确定性操作、暴露选定本地 source / Skill、输出 discovery trace 和返回 stale / missing / ambiguity signal。

它们不能：

- 通过 LLM 自动发明职责 / 条件 / 风险；
- 静默修改资源语义或 Reviewed Discovery Map；
- 维护隐藏 Method Stage / Stage Router；
- 自动访问 upstream 改变普通运行；
- 缓存第二份 Requirement / Architecture / Rule 正文；
- 通过算法优先级覆盖仓库权威；
- 接管完整开发生命周期。

如果某项数据删除后既不能从真实 owner 恢复，也不能从 current Map / 持久采用历史恢复，它就不是纯 Runtime View 数据。

## 15. V2 资产处置

| 当前 v2 资产 / 规则族 | V3-06 处置 | replacement / compatibility |
|---|---|---|
| `docs/guides/rule-activation-guide.md` | **过渡派生导航** | V3-07 切换前继续 current；文件可继续保留人类启动导航，但手工职责 / 风险路由不能与新 current Map 长期并行 |
| `docs/guides/consumer-local-rule-activation.md` 人类采用 / 本地化说明 | **保留 Guide 身份** | 继续解释采用后的本地运行；长期规范发现语义由本架构单点拥有后，Guide 应删减为说明 / 指针 |
| `consumer-local-rule-activation.md` 普通运行 discovery / routing 规范段落 | **被本架构 supersede 的兼容正文** | 本架构集成后长期语义 owner 转移完成；物理去重 / 指针调整留 V3-07，期间不得独立演进第二套语义 |
| `consumer-local-rule-activation.md` 采用后验收段 | **派生验收说明 / V3-08 输入** | 生命周期层面的采用验证责任由 V3-03 拥有；其中各项 runtime/discovery 行为由对应真实 owner 持有；V3-08 只消费派生检查项，不让 Guide 成为第二验收 owner |
| `consumer-local-activation-metadata-contract-v2.md` | **历史项目契约 + 过渡兼容输入** | 长期资源语义已由 V3-05 接管；发现绑定 / 派生语义由本架构接管；V3-07 自采用后降为历史证据 |
| `consumer-local-runtime-routing-interface-v2.md` | **历史项目契约 + 已验证行为输入** | 主职责、辅助上下文、routing-only、Stage Return、fail-closed 等长期语义由本架构接管；V3-07 后不再作为 current runtime owner |
| V2 Activation Manifest | **混合过渡载体** | 固有 provenance / locator / supersede 迁入真实资源结构 / 采用历史；有价值的已复核语义映射迁入 Map；成员完整性由覆盖锚点接管；迁移验证前不得整体删除 |
| V2 Runtime Catalog | **旧纯运行投影** | 可以被 Runtime View 复用、简化或取消；replacement 验证后可删除 / 重建 |
| 手工 responsibility / risk routing 表 | **派生导航** | V3-07 后只能保留人类说明或由 current discovery mechanism 派生；不得与机器 current routing 长期双维护 |

## 16. Compatibility Freeze 与原子切换

### 16.1 V3-06 集成后的兼容冻结

V3-06 一旦集成，被本架构 supersede 的 v2 发现 / 路由正文仍可作为**兼容 surface**继续服务当前入口，但不再是可以独立演进的第二规范 owner。

V3-07 完成物理迁移前：

- 新的长期 discovery / routing 语义只进入本架构；
- v2 Guide / project contract 只允许为保持兼容、修复错误或同步指针做必要修改；
- 如果兼容正文与本架构冲突，视为 compatibility defect，按当前 Authority 顺序修正旧 surface；
- 不允许给旧表和新 Map 分别维护两套不同 current routing 结论。

### 16.2 候选机制可以并存，但不能同时 current

V3-07 为验证 replacement，可以在旧机制仍 current 时建立新的**非 current candidate** Map / Runtime View。

切换顺序：

```text
旧机制 current
+ 新机制 candidate / eval-only
→ 验证新机制
→ 单一明确切换点
   → 新机制 current
   → 旧机制 compatibility / historical / non-current
→ 清理旧派生 surface
```

不得存在两个机制同时声明 current 的窗口，也不得先删除旧 current 再验证新候选。

## 17. V3-07 自采用输入契约

V3-07 可以直接假定：

1. 每个普通运行仓库必须能从薄 Bootstrap 到达一个 Local Discovery Entry；
2. 发现长期基础是真实本地资源与稳定 Authority Entry；
3. Manifest + Catalog 两层不是必选架构；
4. 小型仓库可以不维护持久化派生发现映射；
5. 需要跨资源语义正规化时，只维护一个 current Reviewed Discovery Map；
6. Map 声称完整覆盖的范围必须有 current 覆盖锚点；没有可靠锚点的范围不能把 no-match 当作完整结果；
7. Runtime View 是同一机制的可选纯生成投影，不能独立维护语义；
8. current resource set 从真实 owner / V3-01 维度 / 关系形成，不维护第二 `active` 真值；
9. routing 使用当前任务事实 + only-known 条件，不猜未知风险；
10. 一次决策只有一个主职责 + 最小辅助集合；
11. routing-only 不加载完整 Skill，执行时才按需加载；
12. Stage Return 后重新发现；具体上游状态失效条件继续由 Method / Skill Contract 拥有；
13. stale / missing / ambiguity / coverage drift 回到本地当前权威；
14. 普通运行不访问 upstream；
15. V2 Manifest 长期事实必须先迁出，再允许移除过渡容器；
16. 已复核派生语义映射删除后需要重新复核，不能由 generator 静默恢复；
17. V3-06 集成后 v2 发现 / 路由正文进入 compatibility freeze；
18. replacement 验证使用 non-current candidate，切换点必须原子化地完成新 current / 旧 non-current 状态转换。

V3-07 的任务是**把这套架构投射到 `agentic-dev` 自己的真实仓库状态并验证**，而不是重新设计上述发现语义。

## 18. 非目标

本文不要求：

- Activation Manifest 必须存在；
- Runtime Catalog 必须存在；
- Reviewed Discovery Map 必须存在；
- 所有仓库都有生成器；
- 全仓统一 Front Matter / YAML / JSON；
- 数据库、向量库、图数据库、MCP 服务或后台 daemon；
- Rule Super Skill / Stage Router Skill / Runtime Controller；
- 固定 Top-K、全局 priority score 或模型置信度路由；
- ordinary runtime 在线访问 upstream；
- 在 V3-07 前物理删除当前 v2 discovery / activation 兼容入口；
- 修改任何使用方仓库。

标准化的是**本地当前资源如何被最小、可验证、可解释地发现和加载**，不是统一存储格式或运行平台。