# 规则治理与知识激活 v3 — 知识与能力所有权收敛

**状态：** 规划中  
**跟踪：** Issue #94  
**启动基线：** `master@3c31ae96683c4a653f001402b889b40e87df976b`

## 1. 目标

v3 的首要目标不是继续增加 Rule Index、Manifest、Catalog 或其他发现技术，而是先解决更上游的问题：

> `agentic-dev` 中的长期知识、规则和 Agent 能力是否被正确的**语义所有者**持有？

v1 / v2 已验证最小上下文、Consumer 本地普通运行、来源时效性和渐进式披露的重要性。如果核心方法、Skill、可复用工程能力、仓库本地规则、项目权威与 Guide 的边界本身不清楚，任何新的发现机制都会继承并放大所有权债务。

因此 v3 采用以下顺序：

```text
先确定语义所有者
→ 再审计现有内容
→ 再确定 Consumer 生命周期
→ 再判断 Skill / 可复用工程能力边界
→ 再定义长期资源模型
→ 最后设计资源发现架构
```

其中 `metadata`、`discovery` 等仅在需要指代具体技术机制时保留原样，不把它们扩展成文档主体语言。

## 2. 启动依据与已完成收敛

规则治理与知识激活 v2 已通过 PR #93 集成。v2 的可复用结果继续作为 v3 必须保护的已验证基线。

V3-01 已通过 PR #100 集成四维所有权判断：

```text
语义所有者
+ 适用范围 / 来源状态
+ 运行 / 生命周期角色
+ 载体 / 权威形式
```

V3-02 已完成当前仓库语义所有权审计，审计矩阵成为 V3-03～V3-06 的直接分析输入；最终独立复核不存在未解决的 Blocking / Medium。

V3-03 已通过 PR #106 集成，`docs/architecture/consumer-lifecycle.md` 成为使用方初始化、采用、升级、普通运行与重新进入上游的长期规范权威。

V3-04 已通过 PR #108 集成，集成提交为 `cd61ab06c0194cc1cf0703aabc8aff5261529950`。当前 9 个 Skill 身份继续成立；工程纪律、Skill Contract 与 `execute-unit` 已收敛为单点正文 + 薄消费；新 Skill 准入与支持资源边界进入 `docs/architecture/skill-architecture.md`；`first-batch-skill-design.md` 只保留历史设计 / Evidence 身份。

V3-05 已由 Issue #109 正式启动，工作产物为 `docs/architecture/agent-resource-model.md`。本阶段直接消费 V3-01～V3-04，不重新执行仓库盘点，也不提前实现 V3-06 discovery。

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
   项目级裁决：`docs/project/skill-reclassification-admission-v3.md`；稳定准入规则进入 Skill Architecture。
5. **V3-05 — 面向 Agent 的结构化资源模型 — 状态见 Issue #109**  
   工作产物：`docs/architecture/agent-resource-model.md`。目标是固定长期资源身份、固有结构与派生发现投影边界，并逐项裁决 v2 metadata 契约。
6. **V3-06 — 资源发现架构**  
   在 V3-05 资源身份稳定后，判断还需要多复杂的发现、索引、查询与路由机制；不得预设一定需要统一 Index / Manifest / Catalog。
7. **V3-07 — `agentic-dev` 自采用**  
   让 `agentic-dev` 自身使用与 Consumer 相同的核心模型，避免维护两套架构。
8. **V3-08 — Consumer 验证**  
   在真实 Consumer 上验证初始化、升级、普通运行、来源时效性、上下文成本和失败关闭行为。

只有前序门禁满足后才能进入后序任务；Roadmap 顺序不自动授予执行权限。

## 4. V3-01 所有权模型

当前正式分类至少区分：

1. 核心方法 / 原则；
2. Skill / 过程型能力；
3. 可复用工程能力 / 工程纪律 / 画像；
4. 仓库本地政策 / 规范 / 规则；
5. 项目 / 产品权威资源；
6. Guide；
7. 研究 / 输入 / 证据。

同时把适用范围、来源状态、运行 / 生命周期角色、载体 / 权威形式与语义所有者分开判断。

Architecture、Contract、Profile、`SKILL.md`、Guide、ADR、Requirement、Front Matter 或 generated index 等载体 / 表示不能直接替代语义所有权判断。

正式判断矩阵：`docs/project/knowledge-capability-ownership-model-v3.md`。

## 5. V3-02 已完成的审计结论

V3-02 不按目录判断身份，而按规范正文 / 规则族判断。主要 ownership debt 包括：

1. `docs/guides/*` 混入人类说明、仓库本地规范、可复用工程能力、Consumer 生命周期和普通运行发现语义；
2. 已完成 v2 的 `docs/project/*` 中仍有若干 discovery / adoption / runtime 契约继续支撑当前行为；
3. `rule-activation-guide.md` 是手工派生导航而不是规范正文 owner，未来只能由经验证的新发现机制显式取代；
4. Skill、工程纪律和验证规则存在正文重叠风险，已由 V3-04 处理主要 Skill overlap；
5. Research / Eval 的 current lifecycle、isolation、scoring、execution control body 不能因目录位置整体降格为 Evidence；
6. Consumer adoption acceptance 的生命周期验证责任属于 Consumer lifecycle，被检查的 runtime / discovery 规则继续由真实 owner 持有。

审计 disposition 只有在对应 V3-03～V3-06 阶段形成替代 owner / mechanism 并通过门禁后才能实施。

## 6. Guide 边界

Guide 的边界保持为：

> 面向人，以及初始化、首次采用、基线升级等低频启动场景，解释如何理解、选择和采用 `agentic-dev`。

Guide 可以在初始化或升级时被 Agent 完整读取；这种一次性 token 成本本身不是问题。

Guide 不应继续承担：

- 普通运行中的核心 Agent 执行过程；
- 仓库本地政策的默认正文；
- 项目权威的事实正文；
- 可复用工程能力的默认容器；
- “不属于核心方法 / Skill”内容的兜底容器。

`using-agentic-dev.md` 保留 Guide 主身份。V3-03 已提取长期生命周期语义，V3-04 已处理 Guide 与 Skill owner 边界；普通运行资源发现、路由和现行派生入口的替代继续等待 V3-06。V3-05 不物理拆分 Guide。

## 7. 使用方生命周期

V3-03 将“使用方生命周期”定义为可复用工程能力，而不是新的产品开发方法阶段，也不因为具有过程顺序就自动成为 Skill。

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
- 普通运行默认不访问 upstream；
- 重新进入上游必须有生命周期允许的显式触发。

V3-05 的资源来源 / provenance 语义必须服从这些边界，一个 upstream baseline pointer 不能代表所有上游资源都已采用。

## 8. V3-04 Skill 重分类与准入

V3-04 的项目级结果：`docs/project/skill-reclassification-admission-v3.md`。

稳定长期结论已经进入 `docs/architecture/skill-architecture.md` 与相关 Contract / Skill：

- 现有 9 个 Skill 的独立身份继续成立；
- `execute-unit` 只薄消费工程纪律，纪律正文由 `engineering-disciplines.md` 单点拥有；
- `converge` 保持功能整体收敛过程，跨职责验证规则由验证工程能力持有；
- `github-actions-verification` 保持平台专项非核心 Skill；
- 验证 / 外部操作规则族当前没有证据形成新的通用 Skill；
- 使用方生命周期不转化为 adoption / upgrade Skill；
- `first-batch-skill-design.md` 只保留历史设计 / Evidence 身份；
- 新 Skill 必须证明稳定触发、输入、过程、输出、退出 / 返回 / 升级、可组合性、所有权边界、证据和可辨识评估；
- supporting resource 只有直接服务父 Skill 且不拥有独立规范语义时才保持内部资源身份。

V3-05 不重新裁决这些 Skill 身份，只消费其资源 / supporting-resource 结果。

## 9. V3-05 面向 Agent 的资源模型

V3-05 长期候选：

`docs/architecture/agent-resource-model.md`

当前核心模型为：

```text
规范 / 事实正文
→ 资源固有结构
→ 派生发现投影
```

### 9.1 规范 / 事实正文

正文只由真实语义所有者持有。metadata、Manifest、Catalog、Index 或其他派生表示不得成为第二规范正文 owner。

### 9.2 资源固有结构

只要求资源长期身份 / 生命周期事实**可稳定恢复**，不要求每个资源新增统一 metadata block。

至少保持：

- 可稳定引用的资源 identity；
- V3-01 四维所有权；
- 当前仓库本地正文 locator；
- 必要 provenance / supersede / supporting 等真实关系；
- 当前有效性可以由真实 owner / V3-01 维度 / 关系无歧义判断。

如果结构由 sidecar / Authority Map 承载，只有当前仓库权威明确指定后才成为资源长期表示的一部分，并与资源正文共同受 owner 生命周期管理；冲突属于 Authority defect，不允许运行时猜测或自动修复。

### 9.3 派生发现投影

V3-06 可以为异构资源生成跨资源职责、条件、风险、路由 / 加载提示、Index 或 Runtime Catalog，但这些投影：

- 不拥有正文；
- 可以删除 / 重建；
- 必须绑定真实 owner；
- stale / missing / ambiguous 时失败关闭；
- 不能维护独立于真实 owner 的 current-state 真值。

### 9.4 原生字段与派生字段

`SKILL.md` 的 `name / description`、技术画像的版本 / 适用范围等是资源自身契约定义的原生结构，继续由原 owner 维护。

只有为了跨资源统一检索而正规化出的 `responsibility / conditions / risks` 等提示才属于 V3-06 派生层。V3-05 不要求所有资源复制同一组字段，也不要求全仓 Front Matter。

### 9.5 v2 metadata disposition

V3-05 逐项裁决 v2：

- `id` → 保留稳定 identity 语义，但优先复用原生身份，不强制新统一字段；
- `kind` → 由语义所有者 + 载体形式取代；
- `source` → 保留本地 locator 概念；
- `activation_role` / `scope` → 拆分长期生命周期 / 适用范围与 V3-06 运行时发现维度；
- `responsibility / conditions / risks` → owner-native 信息保留；跨资源正规化提示留 V3-06；
- `origin` → 由 V3-01 来源状态 + 必要 provenance 取代；
- `state` → 不保留统一状态字段，current set 从真实 owner / V3-01 维度 / 关系派生；
- `relations` → 只保留真实 supersede / derived / supporting / override 关系；
- `semantic-reviewed / current-locator` → 作为 V3-06 派生投影绑定策略继续评估；
- Activation Manifest / Runtime Catalog → 不进入资源固有模型，由 V3-06 决定保留、简化或取代。

## 10. v1 / v2 必须保留的成果

v3 必须继续保护至少以下已经验证的长期成果：

- 薄启动入口；
- 仓库 / Consumer 权威优先；
- 渐进式披露；
- 证据先于声明；
- 规范正文单点所有权；
- 派生发现机制不拥有规范正文；
- 陈旧、缺失、歧义时失败关闭；
- 主职责与最小辅助上下文分离；
- 只做路由判断时不机械加载完整 Skill；
- 真正进入职责时按需加载 Skill；
- 阶段返回后重新判断；
- Consumer 普通运行只依赖 Consumer-local 现行资源；
- 基线采用逐项采用、保留 / 覆盖、拒绝、取代；
- 同一运行范围 / 发现职责不并行维护多个现行派生机制。

V3-03 进一步保护使用方生命周期状态职责；V3-04 保护 Skill / 工程能力真实所有权；V3-05 进一步保护“真实长期资源 ≠ Manifest record”和“原生资源结构 ≠ 派生发现提示”。

v3 不以“重新设计”为理由推翻已经通过真实 Consumer 验证的行为。

## 11. 当前非目标与 ADR Gate

V3-05 不：

- 实现或冻结 Runtime Catalog / Activation Manifest / Rule Index / generator；
- 设计完整资源发现、查询、排序、路由或 Stage Return 算法；
- 全仓批量增加 Front Matter 或统一 YAML / JSON schema；
- 建立数据库、向量库、图数据库、MCP 服务或后台 daemon；
- 物理移动、拆分、重命名或删除全部 Guide / Policy / Project / Research-Eval 资源；
- 修改使用方仓库；
- 重新设计 V3-03 生命周期或 V3-04 Skill 身份；
- 启动 V3-06～V3-08；
- 启动 WI-06 / WI-07 / WI-09 或其他独立候选。

v3 不用一个“大 ADR”承载全部探索。只有专项分析形成跨任务长期约束、存在实质替代方案与长期后果、且决定已经稳定时才创建或更新 ADR。

当前高概率 ADR 候选继续包括：

- 知识与能力所有权架构；
- Skill 承担过程型能力与 Guide / Rule 承担普通运行内容之间的长期边界；
- 面向 Agent 的资源模型 / 派生发现架构（仅在 V3-05 / V3-06 最终证明其长期架构价值后）。

目录名、字段名、文件拆分数量或某个具体序列化格式不自动 ADR 化。

## 12. 当前门禁

V3-05 跟踪入口：Issue #109。  
工作产物：`docs/architecture/agent-resource-model.md`。

V3-05 的精确审查、集成与完成状态以 Issue #109 和 GitHub 当前状态为准，本文件不复制瞬时 PR 状态。

V3-05 完成门禁为：

> 已稳定定义哪些资源需要结构化、资源固有结构与派生发现投影边界、V3-01 四维所有权在资源模型中的恢复方式、Markdown / `SKILL.md` / 画像 / 仓库本地规则 / supporting resource 兼容方式、当前有效性 / provenance / supersede 语义和 v2 metadata / Manifest / Catalog disposition；V3-06 可以直接消费资源身份而无需重新定义；高影响资源模型歧义不存在未解决的 Blocking / Medium。

如果 Issue #109 仍开放，应继续完成上述未满足门禁；如果 Issue #109 已以完成原因关闭，则 V3-05 已收口，V3-06 只成为下一规划候选。只有新的 V3-06 Planning Authority 建立后才能启动 V3-06。

无论 V3-05 状态如何，本阶段结论都不自动授予资源发现实现、全仓结构迁移、Consumer Repository 修改或后序阶段权限。
