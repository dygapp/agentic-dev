# 资源发现架构

**状态：** V3-06 候选 v0.1  
**性质：** 跨仓库可复用的本地资源发现与职责路由架构  
**跟踪：** Issue #111

## 1. 目的

本文定义 `agentic-dev` 的长期资源发现架构，回答：

> 在使用方仓库已经拥有当前资源和仓库权威的前提下，新上下文或当前职责怎样只依赖本地事实找到真正需要的资源，确定一个主职责、最小辅助上下文和可解释阶段动作，同时避免把发现层升级成第二份方法、规则或当前状态真值。

本文直接消费：

- `docs/architecture/consumer-lifecycle.md`；
- `docs/architecture/agent-resource-model.md`；
- 当前 Method / Skill Contract；
- v2 已通过真实使用方验证的发现、路由、按需加载与失败关闭行为。

V3-06 **不重新定义资源身份**。发现架构只能组织、筛选、定位和加载 V3-05 已定义的真实资源。

## 2. 必须保持的不变量

### 2.1 仓库权威优先

发现结果不能覆盖使用方仓库权威，也不能通过数值优先级、命中分数或模型置信度重写项目事实。

### 2.2 普通运行只依赖本地当前资源

使用方完成采用 / 升级后，普通运行默认只读取使用方本地当前资源。发现失败、索引陈旧或 no-match 都不构成自动访问 upstream 的理由。

### 2.3 派生发现不拥有规范正文

发现映射、索引、Catalog、查询提示、路由结果和运行 trace 都不能保存第二份 Requirement、Architecture、Policy、Rule 或 Skill procedure。

### 2.4 不维护第二当前状态真值

资源是否当前有效，继续由：

```text
当前仓库权威
+ V3-01 四维语义
+ 资源原生当前状态（如有）
+ 真实取代 / 禁用关系
```

共同确定。

发现层可以缓存或投射当前候选，但不得独立声明某资源 `active` 并在真实语义所有者已经变化后继续把它当作当前事实。

### 2.5 渐进式披露

发现目标不是“命中越多越好”，而是：

> 不遗漏当前正确工作所必需的资源，同时不加载明显无关正文。

### 2.6 一个主职责

一次发现 / 路由决策只能有一个当前**主职责**。验证、工程纪律、平台能力、外部操作规则等可以构成辅助上下文，但只要没有改变当前职责所有权，就不能夺取主职责。

如果一次用户请求包含多个彼此独立的目标，应先按当前仓库权威与工作关系拆成可顺序处理的当前目标，再分别形成发现决策；不能为了“一次回答全部”把多个独立职责平铺成多个同时有效的主职责。

### 2.7 同一发现职责只有一个 current 派生机制

同一 Runtime scope 中，新的派生发现机制一旦正式取代旧机制，旧 Index / Catalog / manual router 必须退出 current surface 或明确降为历史 / 兼容证据。

一个已复核发现映射及其**由同一映射确定性生成的运行视图**属于同一个发现机制；只要运行视图不独立维护语义，就不构成第二套 current discovery truth。

## 3. 最小发现架构

V3-06 不把 v2 的“两层 Manifest + Catalog”提升为必选架构。长期逻辑为：

```text
本地当前资源与稳定入口
        ↓
可选：已复核发现映射
        ↓
可选：纯生成运行视图
        ↓
每次任务的临时发现决策
```

后两层都可以不存在。小型仓库可以直接从稳定入口和资源原生发现信息完成发现。

### 3.1 本地当前资源与稳定入口

这是发现的真实输入，包括：

- 仓库根 Bootstrap / Authority Entry；
- 当前 Requirement / Specification / Architecture / Roadmap 等项目权威入口；
- 当前本地 Policy / Standard；
- 已采用的 Skill / Engineering Discipline / Technology / Verification Profile；
- 其他 V3-05 判定需要独立发现的当前资源。

这些是真实资源，不是发现层复制品。

### 3.2 已复核发现映射

当资源异构程度或条件激活复杂度使固定入口 + 原生资源信息不足以低成本、稳定发现时，可以维护一个**已复核发现映射（Reviewed Discovery Map）**。

它是**非规范性、但需要维护的派生语义输入**。它可以记录：

- 对真实资源的稳定引用；
- 本地 locator / selector；
- 资源原生发现信息的引用；
- 为跨资源查询正规化并经过复核的职责 / 条件 / 风险提示；
- `routing-only / execution` 等非规范性加载提示；
- 派生语义提示所需的 source binding；
- 纯定位条目所需的 locator binding；
- 它声称覆盖的发现范围及相应 **coverage anchors**。

它不保存：

- 规范正文或摘要；
- 第二份 `active/current` 真值；
- 当前 Gate / Issue / PR / Actions 状态副本；
- 固定推荐答案；
- 全局数值 priority；
- 隐藏 Method / Stage / Skill routing 语义。

“派生”只表示它不拥有规范正文，不表示其中已经完成的语义复核可以靠生成器随意重建。

### 3.3 纯生成运行视图

如果运行时确实需要更紧凑的入口，可以从：

- 当前真实资源状态；
- 当前已复核发现映射（如有）；
- 资源原生发现信息；

确定性生成一个 compact Runtime View / Catalog。

该运行视图：

- 可以删除 / 重建；
- 不独立维护语义映射；
- 不拥有 current-state 真值；
- 不允许出现映射层没有的“智能补充”；
- 只是同一发现机制的运行投影。

### 3.4 临时发现决策

每次任务根据当前事实产生一个临时**发现决策**。它只服务当前判断，不构成长久权威，也默认不持久化。

至少能够表达：

- 当前主职责；
- `routing-only` 或真正执行；
- `continue / return / fail-closed / escalate` 等阶段动作；
- 主资源指针；
- 最小辅助资源指针；
- 真正执行时需要加载的 Skill；
- 简短可解释理由；
- 哪个旧 routing / Readiness / Execute 状态已经失效（如有）。

字段名不是固定协议；重要的是职责与生命周期边界。

## 4. 何时不需要持久化发现映射

以下条件同时成立时，可以只使用固定本地入口与资源原生信息：

- 当前独立发现资源数量较少；
- 主要 Authority Entry 稳定且可直接定位；
- Skill / Profile 已有足够原生发现信息；
- 条件性横切资源很少；
- 新上下文可以在可接受的读取成本内可靠得到正确主职责与辅助集合；
- 不存在需要跨多个 mixed resource 做稳定语义切片发现的持续问题。

这种仓库不因为使用 `agentic-dev` 就必须新增 Manifest、Catalog、Discovery Map 或生成器。

## 5. 何时需要已复核发现映射

出现以下持续需求之一时，映射才有明确价值：

- 多类异构资源需要统一按职责 / 条件筛选；
- mixed resource 的稳定区块需要独立发现；
- 多个工程纪律 / 验证能力 / 平台能力按条件横切多个职责；
- 资源规模使每次从目录 / Guide 手工扫描成本明显过高；
- 需要保存已经完成的跨资源语义正规化判断，而不把这些判断塞回真实 owner；
- 需要机器可读 trace 来验证 ordinary runtime 没有访问 upstream 或加载无关能力。

即使需要，也只维护**一个 current 已复核发现映射**。如果另有 Runtime Catalog，它只能由该映射和当前真实资源生成，不能独立维护另一套职责 / 条件 / 风险语义。

## 6. 发现覆盖边界

只有逐条 source binding 还不足以保证发现完整性：仓库可能新增一个应被发现的资源，而旧条目本身全部仍然“新鲜”。因此 Reviewed Discovery Map 必须明确自己**声称覆盖什么**，并绑定覆盖范围的真实入口。

### 6.1 coverage scope

Map 可以只覆盖部分资源，例如：

- 当前 Skill inventory；
- 可独立消费的工程纪律 / 验证能力；
- 技术 / 验证画像；
- 某组条件性仓库本地规则；
- 已明确拆分的 mixed-resource sections。

Map 不要求覆盖所有 Markdown，也不能把“当前仓库全部文件”作为模糊完整性声明。

### 6.2 coverage anchor

每个声称完整覆盖的范围必须关联能够反映真实 membership 的本地 current anchor，例如当前仓库明确指定的：

- 资源 inventory / Authority Map；
- Skill / Profile current entry；
- 稳定资源描述集合；
- 其他能够由仓库权威确认该发现范围 membership 的入口。

coverage anchor **不拥有资源正文，也不重新定义资源身份**；它只让发现层知道“这个范围的成员集合是否发生变化”。

如果当前仓库没有可靠 anchor，Reviewed Discovery Map 就不能声称该范围完整。该范围 no-match 时必须回到本地 Authority Entry 做扩展发现。

### 6.3 coverage drift

以下变化会使对应覆盖范围失效：

- 新增一个应该独立发现的资源；
- 删除 / supersede 一个已发现资源；
- mixed-resource section 被拆分、合并或重新分类；
- current inventory / Authority Entry membership 发生变化；
- 覆盖范围本身被当前仓库权威调整。

发生 coverage drift 后，不能因为旧条目的 source hash 都没变就继续声称 Map 完整。

## 7. Activation Manifest 与 Runtime Catalog 的长期裁决

### 7.1 Activation Manifest

V2 Activation Manifest 是已经验证过渡期价值的**混合载体**，但不再是 v3 必选架构层。

它当前可能同时保存：

- 长期 provenance / locator / supersede 等固有事实；
- 跨资源职责 / 条件 / 风险等已复核派生发现提示；
- 运行时 `active / loading` 等过渡字段。

V3 长期方向：

1. 固有事实进入真实资源结构、当前仓库明确授权的资源描述或 V3-03 采用 / 升级历史；
2. 仍有长期发现价值的已复核派生提示进入 Reviewed Discovery Map；
3. 纯运行过滤 / compact projection 进入可删除 Runtime View；
4. Manifest 原先承担的“有哪些 current discovery records”必须改由真实资源 membership + coverage anchors 判断；
5. 不再要求一个独立 Manifest 同时承担上述责任。

在 V3-07 自采用完成迁移并验证 replacement 之前，现有 Manifest 语义继续作为兼容输入，不能提前整体删除。

### 7.2 Runtime Catalog

Runtime Catalog 被收敛为**纯生成运行视图的一种可选物理实现**。

如果 Consumer 很小，可以不存在独立 Catalog；如果需要 compact runtime entry，可以生成一个 Catalog。无论是否存在，它都：

- 可删除 / 确定性重建；
- 不拥有规范正文；
- 不拥有 current-state 真值；
- 不独立保存新的语义复核结论；
- 只投射当前可验证的资源引用与已复核派生提示。

因此 V3 不再要求“Manifest 维护输入 + Runtime Catalog 运行投影”必须物理分成两层。

## 8. 当前资源集合

### 8.1 current set 是运行时逻辑集合，不是新 Authority

发现前先从当前仓库事实确定当前资源集合。它不是必须持久化的新文件，也不是派生索引里的独立状态表。

至少排除：

- 仅历史 / 证据资源；
- 外部未采用资源；
- 已被真实 owner 明确 supersede 的旧资源；
- 当前仓库明确 disabled / excluded 的资源；
- locator / selector 已不可解析且无法由当前权威确认身份的资源。

### 8.2 mixed resource 按资源单元处理

一个 mixed 文件不能整体进入或退出 current set。发现粒度必须服从 V3-05 已确定的稳定资源单元。

### 8.3 派生层中的 current filtering

Reviewed Discovery Map 或 Runtime View 可以只暴露当前候选，但 filtering 必须从真实 owner / 关系重新计算或验证，并同时确认相关 coverage anchor 没有发生未复核 membership drift。

禁止：

```text
旧 Catalog 里仍写 active
→ 就把已经被真实 owner 取代的资源继续视为当前
```

## 9. 当前任务事实

资源集合说明“现在有哪些资源”，任务事实说明“这次正在解决什么”。两者必须分开。

### 9.1 最小事实信号

每次发现按当前可观察事实解析：

- **目标事实**：当前要求澄清、规格、规划、切分、就绪、执行、调查、收敛、平台验证或外部操作中的什么责任；
- **权威事实**：当前任务依赖的本地权威是否存在、当前、可解析、无冲突；
- **生命周期事实**：当前 Work / Readiness / Execute Authority / Evidence 的实际状态；
- **问题事实**：问题是已定义 expected behavior 下的实现 / runtime 异常，还是 Product Intent / Specification / Architecture / Authorization 自身缺失或冲突；
- **已知条件 / 风险**：只有当前证据已经支持、且会改变所需资源集合的条件。

### 9.2 任务事实不是资源 metadata

这些事实：

- 随任务变化；
- 默认不持久化进资源结构或 Reviewed Discovery Map；
- 不成为未来任务的默认真值；
- 可以作为当前查询输入；
- 未知值不得为了提高召回率而猜测。

## 10. 候选发现

候选发现使用：

```text
当前资源集合
+ 当前任务事实
+ only-known 条件 / 风险
```

得到值得继续做 applicability / currentness 判断的候选资源。

候选可以直接来自稳定本地入口 / 资源原生发现信息，也可以由 Reviewed Discovery Map 加速；发现映射不是唯一入口。

### 10.1 候选命中不等于适用

候选只代表“需要进一步判断”，不能直接推出：

- 该规则当前已经适用；
- 该 Skill 必须加载；
- 该资源可以覆盖使用方权威；
- 当前阶段仍可继续执行。

### 10.2 不使用固定 Top-K

如果 6 个资源都对当前正确执行必需，就必须保留 6 个；如果只有 1 个，就不为了固定数量补足。

目标是**最小正确集合**，不是固定大小集合。

### 10.3 zero-match

zero-match 只有在相关 coverage scope 的 anchors 与语义映射都 current 时，才表示“该已覆盖范围内没有命中”。它仍不能自动证明当前任务完全没有适用规则。

以下任一情况必须回到本地 Authority Entry 扩展发现：

- 当前任务落在 Map 未声明覆盖的范围；
- 相关 coverage anchor 不存在或陈旧；
- membership 已变化但映射尚未复核；
- 任务明显仍包含治理、验证或风险事实。

### 10.4 ambiguity

允许读取少量 routing / constraint owner 消歧。仍无法可靠区分时停止高影响动作，进入本地 fail-closed / 必要人工升级，而不是按模型概率猜主职责。

## 11. 主职责解析

一次发现决策只允许一个主职责。

解析顺序：

1. **使用方仓库权威优先**：项目事实、权限和当前约束先由本地权威决定；
2. **基础缺口拥有阶段返回**：Product Intent / Specification / Architecture / Authorization 基础出现缺口时，拥有该缺口的职责成为新的主职责；
3. **当前请求职责**：前置基础仍有效时，当前明确要求执行的稳定职责保持主职责；
4. **unexpected failure 不自动等于 debug**：只有 expected behavior 已明确、问题属于实现 / runtime 非预期失败时，`systematic-debug` 才成为主职责；
5. **辅助责任不夺取主职责**：验证、平台、外部操作、工程纪律等只要没有改变职责所有权，就保持辅助上下文。

该顺序只描述 discovery 如何消费现有 Method / Skill Contract，不创建新的方法优先级。

## 12. 最小辅助上下文

辅助资源只有同时满足以下条件才进入集合：

- 当前触发 / 条件由事实支持；
- 它会改变主职责的正确执行或完成声明；
- 没有被更具体的使用方当前权威合法覆盖 / 取代；
- source / locator / 派生语义绑定当前有效；
- 若依赖 Reviewed Discovery Map，该资源所属 coverage scope 当前完整。

“可能有用”“主题相关”“以后也许需要”都不足以进入辅助集合。

## 13. routing-only 与按需 Skill

### 13.1 routing-only

当前目标只需要：

- 判断下一职责；
- 判断 Stage Return；
- 判断当前 Readiness / Execute Authority 是否仍有效；
- 解释为什么需要返回某职责；

且现有本地权威 + 资源原生发现信息 / 派生提示已经足够时：

```text
resolve responsibility
→ 返回主职责 + 理由 + 必要资源指针
→ stop
```

不得因为发现了 Skill locator 就加载完整 Skill。

### 13.2 真正执行职责

只有当前任务要继续执行主职责时才：

1. 确认对应本地 Skill 当前可用；
2. 加载该主职责的完整 Skill；
3. 加载主 Skill 当前需要的最小本地权威与辅助约束；
4. 按 Skill Contract 执行；
5. 出现 Stage Return signal 时停止当前职责并重新发现。

### 13.3 平台专项 Skill

平台专项 Skill 只有在：

- 当前平台条件真实命中；
- 主职责确实需要可分离的专项过程；
- 不改变主职责；
- 当前仓库权威允许；

时作为辅助能力按需加载。

普通运行不批量加载所有 Skill。

## 14. Stage Return 与旧状态

Stage Return 后：

```text
停止当前职责
→ 丢弃旧发现决策作为继续授权
→ 重新读取受影响的本地当前权威
→ 重新形成当前任务事实
→ 重新发现 / 路由
```

如果 Product Intent、Specification、durable Technical Plan、Architecture / ADR 或 Execution Unit scope / acceptance ownership 发生实质变化，旧 Readiness / Candidate Unit 只对应旧语义基础，必须按当前 Method / Skill Contract 回到必要上游职责。

如果 `systematic-debug` 只修复实现缺陷，没有改变这些基础，则取得匹配回归证据后可以恢复原执行路径，不机械重跑完整生命周期。

## 15. 失败关闭与本地回退

以下情况停止依赖当前派生发现：

- Reviewed Discovery Map / Runtime View 陈旧；
- coverage anchor 陈旧、缺失或 membership 漂移；
- locator / selector 丢失；
- 当前语义所有者不明确；
- no-match 但仍存在治理 / 风险事实；
- 多个主职责无法可靠区分；
- override / supersede 关系不明确；
- 高影响授权、重大 Architecture、安全 / 隐私或不可逆边界不清；
- 需要的 Skill 本地不存在或身份无法确认；
- 资源原生结构与伴随描述 / 派生提示发生矛盾。

回退：

```text
停止使用当前派生结果
→ 回到使用方本地当前权威 / 稳定 Authority Entry
→ 按问题扩大最小本地读取
→ 重新确定资源与职责
→ 只有本地权威 / 权限要求时才升级人工
```

普通运行的 fail-closed 不自动打开 upstream。

## 16. Reviewed Discovery Map 的维护与 currentness

### 16.1 纯定位映射

如果映射条目只保存 resource ref + locator，不提炼规则适用语义：

- 正文普通内容变化不自动使 locator 陈旧；
- 路径、selector 或 authority role 被取代时才需要更新；
- runtime 始终读取真实 current source。

这继承 v2 `current-locator` 的有效思想。

### 16.2 语义提炼映射

如果映射条目保存跨资源正规化职责 / 条件 / 风险提示：

- 必须绑定已复核 source / selector identity；
- source 语义变化后旧提示立即退出可信候选；
- 不能只重算 hash / commit id 就自动恢复；
- 必须重新判断变化是否影响派生语义；
- 新的语义映射只有经过当前仓库允许的人工 / AI 复核后才能重新进入 current map。

这继承 v2 `semantic-reviewed` 原则，但绑定的是**派生提示**，不是资源身份本身。

### 16.3 coverage binding

Map 还必须验证自己声称完整覆盖的 coverage anchors：

- anchor membership 未变化：可以继续使用现有映射；
- membership 变化且能够精确定位受影响资源：只让对应映射 / coverage scope 失效；
- 无法可靠判断影响范围：整个相关 coverage scope 失败关闭；
- 不得仅重算 anchor hash 就自动把新增 / 重分类资源视为已完成语义映射。

这解决“已有条目都没变，但出现了尚未纳入发现的新资源”的集合陈旧问题。

### 16.4 删除与重建边界

Reviewed Discovery Map 不拥有规范正文，所以删除它不会删除项目 / 规则事实；但如果其中包含已复核的跨资源语义映射，删除后不能声称生成器可以无语义判断地自动恢复同等发现能力。

删除后只有两条安全路径：

1. 退回稳定本地 Authority Entry + 资源原生发现信息工作；或
2. 重新执行必要语义复核，建立新的 current Reviewed Discovery Map。

因此“可从真实 owner 重新分析得到”不等于“可确定性生成”。

## 17. 纯生成 Runtime View 的重建

Runtime View 必须能够从：

- 当前真实资源状态；
- 当前资源原生发现信息；
- 当前 Reviewed Discovery Map（如有）；
- 当前 coverage anchor identities；

**确定性重建**。

生成过程只做：

- source / selector resolution；
- coverage/current-set filtering；
- schema / reference validation；
- 已复核派生提示的投影；
- compact serialization。

它不做新的语义判断。

如果某项内容删除后既不能从真实 owner 恢复，也不能从 current Reviewed Discovery Map / 持久采用历史恢复，它就不是纯 Runtime View 数据。

## 18. Generator / Runtime Adapter 边界

生成器 / 适配器是**可选优化**，不是发现架构的规范语义所有者。

可以：

- 解析稳定 locator / selector；
- 校验 schema / resource reference；
- 校验 source binding / coverage anchors；
- 根据显式、已复核映射做确定性过滤；
- 生成 compact Runtime View；
- 暴露选定本地 source / Skill；
- 输出可观察 discovery trace；
- 返回 stale / missing / ambiguity signal。

不可以：

- 通过 LLM 自动发明职责 / 条件 / 风险；
- 静默修改资源语义或 Reviewed Discovery Map；
- 维护隐藏 Method Stage / Stage Router；
- 自动访问 upstream 并改变 ordinary runtime；
- 缓存第二份 Requirement / Architecture / Rule 正文；
- 通过算法优先级覆盖仓库权威；
- 接管完整开发生命周期。

## 19. V2 资产处置

| 当前 v2 资产 / 规则族 | V3-06 处置 | replacement / compatibility |
|---|---|---|
| `docs/guides/rule-activation-guide.md` | **过渡派生导航** | 在 V3-07 自采用切换到新发现入口前继续 current；其手工职责 / 风险表不能与新 current Reviewed Discovery Map 长期并行 |
| `docs/guides/consumer-local-rule-activation.md` 人类 adoption / localization 说明 | **保留 Guide 身份** | 继续解释采用后的本地运行；长期规范发现语义由本架构单点拥有后，应删减为说明 / 指针 |
| `consumer-local-rule-activation.md` 普通运行 discovery / routing 规范段落 | **被本架构 supersede 的兼容正文候选** | 本架构集成后长期语义 owner 转移完成；物理去重 / 指针调整留 V3-07 自采用，期间不得继续独立演进第二套语义 |
| `consumer-local-activation-metadata-contract-v2.md` | **历史项目契约 + 过渡兼容输入** | 长期资源语义已由 V3-05 接管；发现绑定 / 派生语义由本架构接管；V3-07 完成自采用迁移后降为历史证据 |
| `consumer-local-runtime-routing-interface-v2.md` | **历史项目契约 + 已验证行为输入** | 主职责、辅助上下文、routing-only、Stage Return、fail-closed 等长期语义由本架构接管；V3-07 后不再作为 current runtime owner |
| V2 Activation Manifest | **混合过渡载体** | 固有 provenance / locator / supersede 先迁入真实资源结构 / 采用历史；仍有价值的已复核语义映射迁入 Reviewed Discovery Map；membership 完整性由 coverage anchors 接管；迁移验证前不得整体删除 |
| V2 Runtime Catalog | **旧的纯运行投影** | 可以被 Runtime View 复用、简化或取消；只要 replacement 已验证即可删除 / 重建 |
| 手工 responsibility / risk routing 表 | **派生导航** | V3-07 自采用时只能保留人类说明或由 current discovery mechanism 派生；不得与机器 current routing 长期双维护 |

## 20. 替代时序

V3-06 只确定长期架构和 replacement 关系，不在本阶段提前拆掉现有入口。

迁移顺序：

```text
V3-06 架构集成
→ V3-07 agentic-dev 自采用
   → 检查是否真的需要 Reviewed Discovery Map
   → 建立 / 选择实际本地 discovery entry
   → 为需要完整覆盖的范围确定 coverage anchors
   → 迁出 Manifest 中长期固有事实
   → 如需要，迁移 / 复核跨资源派生语义映射
   → 如需要，生成纯 Runtime View
   → 验证 coverage/current-set/routing/fail-closed/no-upstream
   → 切换 root / Guide 指针
   → 旧 current 派生机制退出 current surface
→ V3-08 真实使用方验证
```

因此“本架构已经定义 replacement”不等于“旧 v2 入口现在可以删除”。

## 21. V3-07 自采用输入契约

V3-07 可以直接假定：

1. 发现长期基础是真实本地资源与稳定入口；
2. Manifest + Catalog 两层不是必选架构；
3. 小型仓库可以不维护任何持久化派生发现映射；
4. 需要跨资源语义正规化时，只维护一个 current Reviewed Discovery Map；
5. Map 声称完整覆盖的每个范围必须有 current coverage anchors；没有可靠 anchor 的范围不能把 no-match 当作完整发现结果；
6. Runtime View 只是同一机制的可选纯生成投影，不能独立维护语义；
7. current resource set 从真实 owner / V3-01 维度 / 关系形成，不维护第二 `active` 真值；
8. routing 使用当前任务事实 + only-known 条件，不猜未知风险；
9. 一次决策只有一个主职责 + 最小辅助集合；
10. routing-only 不加载完整 Skill，执行时才按需加载；
11. Stage Return 后重新发现；
12. stale / missing / ambiguity / coverage drift 回到本地当前权威；
13. 普通运行不访问 upstream；
14. V2 Manifest 的长期事实必须先迁出，再允许移除过渡容器；
15. 已复核派生语义映射删除后需要重新复核，不能由 generator 静默恢复。

V3-07 的任务是**把这套架构投射到 `agentic-dev` 自己的真实仓库状态并验证**，而不是重新设计上述发现语义。

## 22. 非目标

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