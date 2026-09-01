# 工程能力扩展实施计划

## 目标

在项目路线图（Project Roadmap）与工程能力架构（Engineering Capability Architecture）完成集成后，按可独立复核的小阶段推进 `agentic-dev` 工程能力扩展，避免把工程纪律（Engineering Discipline）、技术配置档（Technology Profile）、Skill、专项评估（Targeted Eval）、Consumer Adoption 和运行时分发混在一个大任务中实施。

## 权威与输入

执行本 Plan 时必须重新读取当时当前有效的：

- `AGENTS.md`；
- `docs/project/project-roadmap.md`；
- `docs/architecture/engineering-capability-architecture.md`；
- 涉及 Skill 时的 `docs/architecture/skill-architecture.md` 与 `skill-contracts.md`；
- 涉及 Research 时的 `docs/research/README.md` 与相关研究材料。

本 Plan 只协调实施顺序，不定义新的 Method、Architecture 或 Skill Contract。

## 范围

本轮长期工作拆为以下独立工作项（Work Item）。每个 Work Item 完成后先形成当前证据和必要的 AI Review，再决定是否进入下一项。

### WI-01 — 工程纪律范围设计

目标：定义首批 Engineering Discipline 研究范围和选择标准，不一次研究全部工程纪律。

主要工作：

- 对现有 Embedded Discipline、PR #41 配置 / 能力复用结论、PR #42 Karpathy Research 做覆盖检查；
- 将候选方向按当前价值、与现有规则重叠度、可形成 Targeted Eval 的程度排序；
- 只选择首批 1～2 个方向进入详细研究。

完成条件：

- 有明确候选清单和优先级；
- 说明为什么首批只选择 1～2 个方向；
- 没有因为列出候选就自动新增 Skill。

### WI-02 — 首项工程纪律研究与候选能力

目标：对 WI-01 选择的第一项工程纪律完成 Research → Candidate Capability 收敛。

主要工作：

- 优先读取高质量原始 / 官方 / 成熟来源；
- 按 Engineering Capability Architecture 记录来源、基线、证据类型、适用范围、时效性、冲突和可验证性；
- 判断结论属于现有 Embedded Discipline 补强、独立 Discipline 规范，还是 Task-oriented Skill 候选；
- 设计有辨识力的 Targeted Eval。

完成条件：

- Research 与候选能力职责边界清晰；
- 存在可执行的 Eval 设计；
- 没有未经验证直接修改 Method / Skill Implementation。

### WI-03 — 第二项工程纪律研究（条件性）

只有 WI-02 完成且第一项研究没有暴露需要先调整能力架构的问题时再进入。

目标与完成条件同 WI-02，但必须与第一项形成独立职责，避免为了数量重复建设。

### WI-04 — Technology Profile 最小契约

目标：在研究具体框架前，定义 Technology Profile 的最小结构与质量门槛。

至少解决：

- Profile 的适用技术 / 版本 / 范围；
- 官方语义与成熟工程实践如何区分；
- 默认规则、常见误用和项目覆盖边界；
- Verification Profile 如何表达；
- Profile 如何被 Consumer 选择、覆盖、更新和取代；
- 哪些内容必须保持 Research 而不能进入 Profile。

完成条件：

- Profile 结构足以支持一个真实技术研究；
- 不创建大而全的框架百科模板；
- 不预设每个 Profile 都需要对应 Skill。

### WI-05 — Vue 3 + TypeScript Profile 研究

目标：以当前有效的 Vue 3 / TypeScript 官方资料为主，成熟工程实践为辅，完成第一项 Technology Profile 研究和候选 Profile。

完成条件：

- 证据满足质量门槛；
- 明确版本、适用范围、默认工程规则、常见误用和 Verification Profile；
- 形成 Targeted Eval；
- 通过 AI Review 后才进入正式能力基线。

### WI-06 — 下一项技术选择

只有 WI-05 完成后才决定下一项：

- Element Plus；或
- Spring Framework / Spring Boot / Spring MVC。

选择依据应来自 WI-05 的实际结果、当前 Consumer / 项目价值和研究复用关系，不在本 Plan 中提前锁死全部顺序。

### WI-07 — 任务型 Skill 提炼

当至少一个 Discipline 或 Technology Profile 已经稳定，并且出现具有独立输入、过程、输出和退出条件的重复工程职责时，再评估是否提炼 Task-oriented Skill。

完成条件：

- Skill 职责与 Profile / Discipline 边界清晰；
- Contract 与 Targeted Eval 完整；
- 不形成 `vue-skill`、`spring-skill` 这类框架百科 Skill；
- 不扩大 Core Method 生命周期。

### WI-08 — Consumer 采用

选择已经进入 `agentic-dev` 正式基线的能力，通过 Existing Consumer baseline upgrade 推动 Reference Consumer 采用。

优先验证：

- 通用能力与 Consumer-local Authority 的组合；
- Profile / Skill 是否真实改善实现和验证质量；
- 是否出现错误默认值、过度约束或能力缺口；
- 是否需要回写上游能力。

Consumer Adoption 不是前面所有研究的启动条件，而是正式能力的重要现实验证阶段。

### WI-09 — 运行时与分发规划

只有前述能力已经证明存在跨 Runtime 交付价值时，才进入 Runtime Adapter / Distribution 的独立规划。

不得在此前阶段顺带实现 Marketplace、Plugin Bundle、Controller 或统一安装器。

## 非目标

本 Plan 不负责：

- 一次完成所有工程纪律；
- 一次完成 Vue、Element Plus、Spring、Gradle 等全部 Profile；
- 预先确定一批新的 Skill 名单；
- 修改已稳定的 Core Method 以适应某个框架；
- 让 `jilinjobs-cms` 再次成为唯一实验来源；
- 在 Research 阶段直接把外部最佳实践升级为规范权威。

## 完成与交接

本 Plan 不以“所有 WI 一次完成”为单次执行目标。

每个 Work Item 应单独关闭并留下当前可验证结果；跨 Fresh Context 时，新的 Agent 从 `AGENTS.md`、Project Roadmap、Engineering Capability Architecture 和本 Plan 的下一个未完成 Work Item 恢复，不依赖历史聊天。

如果长期路线、能力分层或 Work Item 顺序发生实质变化，应优先更新对应长期权威；本 Plan 只同步必要的协调状态，不维护第二份项目路线图。
