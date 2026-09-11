# 规则治理与知识激活 v3 — 知识与能力所有权收敛

**状态：** 规划中  
**跟踪：** Issue #94  
**启动基线：** `master@3c31ae96683c4a653f001402b889b40e87df976b`

## 1. 目标

v3 的首要目标不是继续增加 Rule Index、Manifest、Catalog 或其他发现技术，而是先解决更上游的问题：

> `agentic-dev` 中的长期知识、规则和 Agent 能力是否被正确的**语义所有者**持有？

v1 / v2 已验证最小上下文、使用方本地普通运行、来源时效性和渐进式披露的重要性。如果核心方法、技能、可复用工程能力、仓库本地规则、项目权威与指南的边界本身不清楚，任何新的发现机制都会继承并放大所有权债务。

因此 v3 采用以下顺序：

```text
先确定语义所有者
→ 再审计现有内容
→ 再确定使用方生命周期
→ 再判断技能 / 可复用工程能力边界
→ 再定义长期资源模型
→ 最后设计资源发现架构
```

## 2. 启动依据与已完成收敛

规则治理与知识激活 v2 已通过 PR #93 集成。v2 的可复用结果继续作为 v3 必须保护的已验证基线。

V3-01 已通过 PR #100 集成四维所有权判断：

```text
语义所有者
+ 适用范围 / 来源状态
+ 运行 / 生命周期角色
+ 载体 / 权威形式
```

V3-02 已完成当前仓库语义所有权审计，审计矩阵成为 V3-03～V3-06 的直接分析输入；最终独立复核不存在未解决的阻塞或中等级问题。

V3-03 已通过 PR #106 集成，`docs/architecture/consumer-lifecycle.md` 成为使用方初始化、采用、升级、普通运行与重新进入上游的长期规范权威。

V3-04 已通过 PR #108 集成。当前 9 个技能身份继续成立；工程纪律、技能契约与 `execute-unit` 已收敛为单点正文 + 薄消费；新技能准入与支持资源边界进入 `docs/architecture/skill-architecture.md`；`first-batch-skill-design.md` 只保留历史设计 / 证据身份。

V3-05 已通过 PR #110 集成，集成提交为 `640f1e3a8e7b5a6e67ad9ea028e51ba621e37964`。`docs/architecture/agent-resource-model.md` 已成为长期资源语义与最小结构契约。

V3-06 已由 Issue #111 正式启动，工作产物为 `docs/architecture/resource-discovery-architecture.md`。本阶段只消费 V3-01～V3-05 与 v2 已验证行为，不重新定义前序所有权 / 生命周期 / 技能 / 资源身份，也不提前执行 V3-07 自采用。

历史 GPT / 其他 AI 评估只作为挑战和复核证据；长期结论以已经集成的仓库权威为准。

## 3. 当前规划主线

v3 按以下有限子任务顺序推进：

1. **V3-01 — 知识与能力所有权模型 — 已完成并集成**  
   已建立四维所有权判断矩阵。
2. **V3-02 — 当前仓库所有权审计 — 已完成并集成**  
   审计矩阵：`docs/project/current-repository-ownership-audit-v3.md`。
3. **V3-03 — 使用方初始化、采用、升级与普通运行生命周期 — 已完成并集成**  
   长期权威：`docs/architecture/consumer-lifecycle.md`。
4. **V3-04 — 技能重分类与准入 — 已完成并集成**  
   项目级裁决：`docs/project/skill-reclassification-admission-v3.md`；稳定准入规则进入技能架构。
5. **V3-05 — 面向 Agent 的结构化资源模型 — 已完成并集成**  
   长期权威：`docs/architecture/agent-resource-model.md`。
6. **V3-06 — 资源发现架构 — 状态见 Issue #111**  
   工作产物：`docs/architecture/resource-discovery-architecture.md`。目标是定义最小本地发现 / 路由架构和 v2 replacement / compatibility 边界。
7. **V3-07 — `agentic-dev` 自采用**  
   让 `agentic-dev` 自身使用与使用方相同的核心模型，避免维护两套架构。
8. **V3-08 — 使用方验证**  
   在真实使用方上验证初始化、升级、普通运行、来源时效性、上下文成本和失败关闭行为。

只有前序门禁满足后才能进入后序任务；Roadmap 顺序不自动授予执行权限。

## 4. V3-01 所有权模型

当前正式分类至少区分：

1. 核心方法 / 原则；
2. 技能 / 过程型能力；
3. 可复用工程能力 / 工程纪律 / 画像；
4. 仓库本地政策 / 规范 / 规则；
5. 项目 / 产品权威资源；
6. 指南；
7. 研究 / 输入 / 证据。

同时把适用范围、来源状态、运行 / 生命周期角色、载体 / 权威形式与语义所有者分开判断。

Architecture、Contract、Profile、`SKILL.md`、Guide、ADR、Requirement、Front Matter 或派生索引等载体 / 表示不能直接替代语义所有权判断。

正式判断矩阵：`docs/project/knowledge-capability-ownership-model-v3.md`。

## 5. V3-02 已完成的审计结论

V3-02 不按目录判断身份，而按规范正文 / 规则族判断。主要所有权债务包括：

1. `docs/guides/*` 混入人类说明、仓库本地规范、可复用工程能力、使用方生命周期和普通运行发现语义；
2. 已完成 v2 的 `docs/project/*` 中仍有若干发现 / 采用 / 运行契约继续支撑当前行为；
3. `rule-activation-guide.md` 是手工派生导航而不是规范正文语义所有者，未来只能由经验证的新发现机制显式取代；
4. 技能、工程纪律和验证规则存在正文重叠风险，已由 V3-04 处理主要技能重叠；
5. Research / Eval 的现行控制正文不能因目录位置整体降格为证据；
6. 使用方采用验收中的生命周期验证责任属于使用方生命周期，被检查的运行 / 发现规则继续由真实语义所有者持有。

审计处理结论只有在对应 V3-03～V3-06 阶段形成替代语义所有者 / 机制并通过门禁后才能实施。

## 6. 指南边界

指南的边界保持为：

> 面向人，以及初始化、首次采用、基线升级等低频启动场景，解释如何理解、选择和采用 `agentic-dev`。

指南可以在初始化或升级时被 Agent 完整读取；这种一次性 token 成本本身不是问题。

指南不应继续承担：

- 普通运行中的核心 Agent 执行过程；
- 仓库本地政策的默认正文；
- 项目权威的事实正文；
- 可复用工程能力的默认容器；
- “不属于核心方法 / 技能”内容的兜底容器。

`using-agentic-dev.md` 保留指南主身份。V3-03 已提取长期生命周期语义，V3-04 已处理指南与技能语义所有者边界；V3-06 当前处理普通运行资源发现 / 路由和现行派生入口的 replacement。现有指南的物理去重 / 指针切换留给 V3-07 自采用。

## 7. 使用方生命周期

V3-03 将“使用方生命周期”定义为可复用工程能力，而不是新的产品开发方法阶段，也不因为具有过程顺序就自动成为技能。

长期语义所有者：

`docs/architecture/consumer-lifecycle.md`

生命周期主线为：

```text
上游可复用来源
→ 新使用方初始化 / 首次采用
   或已有使用方显式基线升级
→ 可复用变化分类
→ 逐项 adopt / retain-or-override / reject-not-applicable / supersede-remove
→ 使用方本地候选状态
→ 采用验证
→ 上游评估基线推进
→ 仅依赖本地当前状态的普通运行
→ 显式重新进入上游
```

必须保持：

- 上游评估基线与当前本地资产来源分离；
- 仅升级使用的决策历史不进入普通新上下文；
- 升级失败 / 中断不推进上游评估基线；
- 采用后的本地资源由使用方当前仓库权威管理；
- 普通运行默认不访问上游；
- 重新进入上游必须有生命周期允许的显式触发。

V3-05 / V3-06 的资源来源与普通运行发现语义必须服从这些边界，一个上游基线指针不能代表所有上游资源都已采用。

## 8. V3-04 技能重分类与准入

V3-04 的项目级结果：`docs/project/skill-reclassification-admission-v3.md`。

稳定长期结论已经进入 `docs/architecture/skill-architecture.md` 与相关契约 / 技能：

- 现有 9 个技能的独立身份继续成立；
- `execute-unit` 只薄消费工程纪律；
- `converge` 保持功能整体收敛过程，跨职责验证规则由验证工程能力持有；
- `github-actions-verification` 保持平台专项非核心技能；
- 验证 / 外部操作规则族当前没有证据形成新的通用技能；
- 使用方生命周期不转化为采用 / 升级技能；
- `first-batch-skill-design.md` 只保留历史设计 / 证据身份；
- 新技能必须满足当前 Skill Architecture 准入门禁；
- 支持资源只有直接服务父技能且不拥有独立规范语义时才保持内部资源身份。

V3-06 不重新裁决这些技能身份，只定义发现层怎样定位、按需加载并在阶段返回后重新发现。

## 9. V3-05 面向 Agent 的资源模型

V3-05 长期权威：

`docs/architecture/agent-resource-model.md`

核心模型：

```text
规范 / 事实正文
→ 资源固有结构
→ 派生发现投影
```

长期边界包括：

- 资源单位是具有稳定语义身份 / 生命周期的逻辑资源，不是任意文件；
- mixed 文件可以包含多个资源单元；
- 资源身份、V3-01 四维所有权、本地 locator 与真实关系必须可恢复，但不要求统一 metadata block；
- `SKILL.md` 的 `name / description`、技术画像版本 / 适用范围等原生字段继续由真实语义所有者维护；
- 跨资源 `responsibility / conditions / risks` 正规化提示属于派生发现层；
- 当前资源集合由真实语义所有者 / V3-01 维度 / 原生状态 / supersede / disable 事实形成，不保留统一 `state` 真值；
- 资源固有结构可以由当前仓库明确授权的伴随描述 / Authority Map 承载，但那种表示与正文共同受语义所有者生命周期管理，不是可删除 cache；
- Activation Manifest 是混合过渡载体，长期 provenance / locator / supersede 等固有事实迁出前不得整体删除；
- Runtime Catalog 可以是纯派生投影。

## 10. V3-06 资源发现架构

V3-06 长期候选：

`docs/architecture/resource-discovery-architecture.md`

### 10.1 最小逻辑

当前候选把发现收敛为：

```text
本地当前资源与稳定入口
        ↓
可选：Reviewed Discovery Map
        ↓
可选：纯生成 Runtime View
        ↓
临时发现决策
```

关键结论：

- Manifest + Catalog 两层不再是必选架构；
- 小型仓库可以直接依赖固定 Authority Entry 与资源原生发现信息；
- 需要跨资源职责 / 条件 / 风险正规化时，只维护一个 current Reviewed Discovery Map；
- Reviewed Discovery Map 不拥有规范正文，但其 semantic-reviewed 映射需要显式维护 / 复核，删除后不能由生成器静默重建；
- Runtime View 只做确定性运行投影，可以删除 / 重建，不独立维护语义；
- 一个已复核映射及其纯生成运行视图属于同一 current discovery mechanism。

### 10.2 current set 与任务事实

发现层不保存第二 `active` 真值；每次根据真实本地权威、V3-01 维度、资源原生状态和真实 supersede / disable 关系形成当前资源集合。

任务事实单独从当前目标、权威状态、Work / Readiness / Evidence、Observed Problem 与 only-known conditions / risks 解析，不写回资源 metadata，也不猜测未知条件。

### 10.3 主职责与最小辅助上下文

一次发现决策只有一个当前主职责。使用方权威优先；基础缺口拥有阶段返回；expected behavior 未定义时 unexpected failure 不自动进入 `systematic-debug`；验证、平台、外部操作、工程纪律等只要不改变职责所有权就保持辅助上下文。

routing-only 只返回主职责、理由和必要资源指针，不机械加载完整 Skill；真正执行职责时才加载主 Skill 和当前必要辅助资源。

### 10.4 Stage Return 与失败关闭

Stage Return 后必须丢弃旧 routing decision 作为继续授权，重新读取受影响本地权威、重新形成任务事实并重新发现。

派生映射陈旧、locator / selector 丢失、owner 不清、no-match 但仍存在风险、主职责歧义、override / supersede 不清或高影响授权边界不清时，普通运行失败关闭到本地当前权威，不自动访问 upstream。

### 10.5 v2 replacement

V3-06 当前候选将：

- `rule-activation-guide.md` 视为 V3-07 切换前的过渡派生导航；
- `consumer-local-rule-activation.md` 保留人类采用 / 本地化 Guide 身份，其普通运行 discovery / routing 规范正文由本架构接管后待 V3-07 物理去重；
- v2 metadata / routing project docs 保留历史项目契约与兼容输入身份；
- V2 Activation Manifest 在 V3-07 中拆分固有事实、已复核派生映射与纯运行投影；
- V2 Runtime Catalog 收敛为可选纯生成 Runtime View；
- 手工职责 / 风险路由表在新 current mechanism 验证切换后不能继续作为平行机器路由真值。

## 11. v1 / v2 必须保留的成果

v3 必须继续保护至少以下已经验证的长期成果：

- 薄启动入口；
- 仓库 / 使用方权威优先；
- 渐进式披露；
- 证据先于声明；
- 规范正文单点所有权；
- 派生发现机制不拥有规范正文；
- 陈旧、缺失、歧义时失败关闭；
- 主职责与最小辅助上下文分离；
- 只做路由判断时不机械加载完整技能；
- 真正进入职责时按需加载技能；
- 阶段返回后重新判断；
- 使用方普通运行只依赖本地现行资源；
- 基线采用逐项采用、保留 / 覆盖、拒绝、取代；
- 同一运行范围 / 发现职责不并行维护多个现行派生机制。

V3-03 保护使用方生命周期状态职责；V3-04 保护技能 / 工程能力真实所有权；V3-05 保护“真实长期资源 ≠ Manifest 记录”和“原生资源结构 ≠ 派生发现提示”；V3-06 在此基础上把已验证 routing 行为提升到长期发现架构，而不强制保留 v2 物理容器。

v3 不以“重新设计”为理由推翻已经通过真实使用方验证的行为。

## 12. 当前非目标与 ADR 门禁

V3-06 不：

- 重新定义 V3-01～V3-05；
- 创建 Rule Super Skill / Stage Router Skill / Runtime Controller；
- 把完整开发生命周期塞入 Adapter / generator；
- 全仓批量增加 Front Matter 或统一 YAML / JSON schema；
- 修改任何使用方仓库；
- 直接执行 V3-07 / V3-08；
- 在 replacement 验证并集成前删除当前 v2 discovery / activation 入口；
- 建立数据库、向量库、图数据库、MCP 服务或后台 daemon；
- 启动 WI-06 / WI-07 / WI-09 或其他独立候选。

v3 不用一个“大 ADR”承载全部探索。只有专项分析形成跨任务长期约束、存在实质替代方案与长期后果、且决定已经稳定时才创建或更新 ADR。

当前高概率 ADR 候选继续包括：

- 知识与能力所有权架构；
- 技能承担过程型能力与指南 / Rule 承担普通运行内容之间的长期边界；
- 面向 Agent 的资源模型 / 派生发现架构（仅在 V3-06 收口和后续自采用证据证明其长期架构价值后决定是否单独 ADR 化）。

目录名、字段名、文件拆分数量或某个具体序列化格式不自动 ADR 化。

## 13. 当前门禁

V3-06 跟踪入口：Issue #111。  
工作产物：`docs/architecture/resource-discovery-architecture.md`。

V3-06 的精确审查、集成与完成状态以 Issue #111 和 GitHub 当前状态为准，本文件不复制瞬时 PR 状态。

V3-06 完成门禁为：

> 已明确最小发现架构及 Manifest / Catalog / Reviewed Discovery Map / Runtime View / generator 是否需要；current resource set 不制造第二状态真值；任务事实、资源原生结构、已复核派生映射和纯生成运行视图边界明确；候选发现、一个主职责、最小辅助上下文、routing-only / Skill execution、Stage Return 与 fail-closed 接口稳定；v2 discovery / routing 资产完成 replacement / compatibility 处置；V3-07 可以直接消费该架构自采用；高影响发现架构歧义不存在未解决的 Blocking / Medium。

如果 Issue #111 仍开放，应继续完成上述未满足门禁；如果 Issue #111 已以完成原因关闭，则 V3-06 已收口，V3-07 只成为下一规划候选。只有新的 V3-07 Planning Authority 建立后才能启动 V3-07。

无论 V3-06 状态如何，本阶段结论都不自动授予 Consumer Repository 修改、V3-07 / V3-08 执行或提前删除当前 v2 current 入口的权限。