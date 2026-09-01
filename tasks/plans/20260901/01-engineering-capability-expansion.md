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

## 当前状态

- **WI-01 — 工程纪律范围设计：已完成。** 结果固化于 `docs/project/engineering-discipline-scope.md`；
- **WI-02 — 实现最小化与推测性复杂度控制：Research / Candidate Design 已完成。** Candidate 状态为 `Pending Targeted Eval`，尚未进入规范性能力基线；
- **当前工作项：WI-03 — 精准修改与差异范围控制。** WI-02 未暴露 Engineering Capability Architecture 缺口，条件已满足；
- **WI-03V — 首批工程纪律验证与基线集成门禁：待 WI-03 完成后执行。**

## 范围

本轮长期工作拆为以下独立工作项（Work Item）。每个 Work Item 完成后先形成当前证据和必要的 AI Review，再决定是否进入下一项。

### WI-01 — 工程纪律范围设计

**状态：已完成。**

目标：定义首批 Engineering Discipline 研究范围和选择标准，不一次研究全部工程纪律。

主要工作：

- 对现有 Embedded Discipline、PR #41 配置 / 能力复用结论、PR #42 Karpathy Research 做覆盖检查；
- 将候选方向按当前价值、与现有规则重叠度、可形成 Targeted Eval 的程度排序；
- 只选择首批 1～2 个方向进入详细研究。

完成结果：

- 首项确定为 **Implementation Minimality & Speculative Complexity Control（实现最小化与推测性复杂度控制）**；
- 第二项条件性确定为 **Surgical Change & Diff Scope Control（精准修改与差异范围控制）**；
- Code Review、Testing、Refactoring、Dependency Management、API Evolution、Performance、Security、Error Handling 等方向保留后续优先级，不在首批一次展开；
- 没有因为范围选择新增 Skill 或修改 Method。

详细依据见 `docs/project/engineering-discipline-scope.md`。

### WI-02 — 首项工程纪律研究与候选能力

**状态：Research / Candidate Design 已完成；Candidate Pending Targeted Eval。**

研究对象：**实现最小化与推测性复杂度控制**。

目标：完成 Research → Candidate Capability 收敛。

完成结果：

- 综合 Martin Fowler YAGNI、Kent Beck Simple Design、Google Engineering Practices、Sandi Metz、Go 官方工程实践与本地 PR #41 / PR #42 形成多来源证据；
- 明确“最低必要复杂度”不是机械追求最少代码，而是在当前正确性、可理解性、安全、验证、可修改性和长期权威约束下，拒绝仅服务假想未来的额外功能 / 抽象 / 配置 / 扩展点 / 依赖 / 层次；
- 候选落点判断为 **独立 Engineering Discipline + `execute-unit` 薄执行引用**，当前没有新增 Skill 或 Method 的职责证据；
- 设计 4 个 Candidate Targeted Eval，并要求回归 `B-EU-07` / `B-EU-08`；
- 当前没有修改 Method / Architecture / Contract / Skill Implementation；
- 研究结果固化于 `docs/research/implementation-minimality-and-speculative-complexity-analysis.md`。

Candidate 只有通过后续 WI-03V 的有效 Targeted Eval 和 AI Review 后，才允许进入规范性工程能力基线。

### WI-03 — 第二项工程纪律研究

**状态：当前。**

研究对象：**精准修改与差异范围控制**。

WI-02 已完成 Research / Candidate Design，且没有暴露需要先调整 Engineering Capability Architecture 的问题，因此原条件性进入门槛已满足。

目标：完成该方向的 Research → Candidate Capability 收敛，并与 WI-02 保持职责独立：

- WI-02 关注**方案复杂度是否具有当前正当性**；
- WI-03 关注**最终变更区域是否属于当前工作、验证责任或必要连带清理**。

至少应：

- 获取多来源成熟工程证据；
- 研究最终 diff 可追溯性、必要连带清理、生成 / 格式化差异和顺带修改边界；
- 与当前 Execution Unit 边界、PR #42 `Surgical Changes`、代码复核和 Refactoring 候选关系做对照；
- 形成 Candidate Capability；
- 设计有辨识力的 Targeted Eval；
- 不在 Candidate 未验证时直接修改 Method / Skill Implementation。

### WI-03V — 首批工程纪律验证与基线集成门禁

**状态：待执行。**

触发条件：WI-02 与 WI-03 的 Research / Candidate Design 均完成。

目标：防止“研究完成”被错误等同于“工程纪律已经成为规范权威”。

主要工作：

1. 复核两个 Candidate 的职责是否真正独立且能组合；
2. 将审核后的 Candidate Eval 设计转换为正式隔离 Runtime Behavior Eval；
3. 回归与候选能力直接相关的历史场景，尤其是 PR #41 已验证的配置责任和已有能力复用边界；
4. 在 Fresh Runtime 中执行 Targeted Eval，并按断言进行语义判分；
5. 如果 Eval 暴露边界错误，返回对应 Research / Candidate 修订，不为推进计划强行集成；
6. 只有取得有效当前证据后，才创建或更新规范性 Engineering Discipline，并按需要对 `execute-unit` 等消费者做薄引用 / 执行强化；
7. 对最终规范变更执行 AI Review，确认无 Method / Architecture / Contract / Human Boundary 回归。

完成条件：

- 每个进入正式基线的 Discipline 都有可追溯 Research、Candidate、Targeted Eval 和当前 PASS 证据；
- Pending / Failed Candidate 不被描述为正式能力；
- 没有因为两个 Discipline 都有价值就机械创建两个 Skill；
- 首批 Discipline 的正式消费者、持久化、更新和取代责任已经闭环。

只有 WI-03V 完成后，才把“首批 Engineering Discipline 已完成”作为进入 WI-04 的事实前提。

### WI-04 — Technology Profile 最小契约

目标：在研究具体框架前，定义 Technology Profile 的最小结构与质量门槛。

进入条件：**WI-03V 已完成，首批 Engineering Discipline 已经过专项评估并完成适用的规范集成。**

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

Research / Candidate Design 完成不等于规范集成完成。凡候选能力需要进入正式能力基线，必须经过对应 Targeted Eval 和规范集成门禁；不能为了推进 Work Item 状态绕过验证。

如果长期路线、能力分层或 Work Item 顺序发生实质变化，应优先更新对应长期权威；本 Plan 只同步必要的协调状态，不维护第二份项目路线图。