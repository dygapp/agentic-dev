# 规则治理与知识激活 v3 — 知识与能力所有权收敛

**状态：** 规划中  
**跟踪：** Issue #94  
**启动基线：** `master@3c31ae96683c4a653f001402b889b40e87df976b`

## 1. 目标

v3 的首要目标不是继续增加 Rule Index、Manifest、Catalog 或其他发现技术，而是先解决更上游的问题：

> `agentic-dev` 中的长期知识、规则和 Agent 能力是否被正确的**语义所有者**持有？

v1 / v2 已验证最小上下文、使用方本地普通运行、来源时效性和渐进式披露的重要性。如果核心方法、技能、可复用工程能力、仓库本地规则、项目权威与指南的边界本身不清楚，任何新的发现机制都会继承并放大所有权债务。

v3 顺序保持：

```text
语义所有者
→ 当前仓库审计
→ 使用方生命周期
→ Skill / 可复用工程能力边界
→ 长期资源模型
→ 资源发现架构
→ agentic-dev 自采用
→ Consumer 验证
```

## 2. 已完成收敛

规则治理与知识激活 v2 已通过 PR #93 集成，已验证行为继续作为 v3 必须保护的基线。

V3-01～V3-06 已完成并集成：

- **V3-01 — 知识与能力所有权模型**：PR #100；建立语义所有者、适用范围 / 来源状态、运行 / 生命周期角色、载体 / 权威形式四维判断；
- **V3-02 — 当前仓库所有权审计**：完成主要 rule family / semantic body 审计并独立复核；
- **V3-03 — 使用方生命周期**：PR #106；长期权威 `docs/architecture/consumer-lifecycle.md`；
- **V3-04 — 技能重分类与准入**：PR #108；当前 9 个 Skill 身份继续成立，Skill 准入与 supporting resource 边界进入 Skill Architecture；
- **V3-05 — 面向 Agent 的结构化资源模型**：PR #110；长期权威 `docs/architecture/agent-resource-model.md`；
- **V3-06 — 资源发现架构**：PR #112，集成提交 `5ae0e144d30c6010fadf8e3beff3c12ce4b7a147`；长期权威 `docs/architecture/resource-discovery-architecture.md`。

V3-06 已固定 Local Discovery Entry、current resource set、可选 Reviewed Discovery Map、可选纯生成 Runtime View、一个主职责 + 最小辅助上下文、routing-only / 按需 Skill、Stage Return、fail-closed、coverage currentness 与 v2 replacement / compatibility 边界。

历史 GPT / 其他 AI 评估只作为挑战和复核证据；长期结论以已经集成的仓库权威为准。

## 3. 当前规划主线

v3 按以下有限子任务推进：

1. **V3-01 — 知识与能力所有权模型 — 已完成并集成**
2. **V3-02 — 当前仓库所有权审计 — 已完成并集成**
3. **V3-03 — 使用方初始化、采用、升级与普通运行生命周期 — 已完成并集成**
4. **V3-04 — 技能重分类与准入 — 已完成并集成**
5. **V3-05 — 面向 Agent 的结构化资源模型 — 已完成并集成**
6. **V3-06 — 资源发现架构 — 已完成并集成**
7. **V3-07 — `agentic-dev` 自采用与发现机制切换 — 状态见 Issue #113**
8. **V3-08 — Consumer 验证**
9. 独立复核
10. 必要 ADR、正式 v3 设计与实现规划

只有前序门禁满足后才能进入后序任务；路线顺序不自动授予执行权限。

## 4. V3-01～V3-02：所有权与审计

V3-01 的正式判断矩阵为：

```text
语义所有者
+ 适用范围 / 来源状态
+ 运行 / 生命周期角色
+ 载体 / 权威形式
```

Architecture、Contract、Profile、`SKILL.md`、Guide、ADR、Requirement、Front Matter 或派生索引都不能单独替代语义所有权判断。

V3-02 按 semantic body / rule family 审计，而不是按目录判断身份。已确认的主要债务包括：

- Guide 混入普通运行发现、仓库本地规则和可复用工程能力；
- 已完成 v2 的 `docs/project/*` 中仍承载过渡发现 / 采用 / 运行契约；
- `rule-activation-guide.md` 的手工职责 / 风险导航属于派生发现，不是长期规范 owner；
- Skill / Engineering Discipline / Verification Rule 存在重复正文风险；
- Research / Eval 不能仅因目录位置整体降为“不可执行证据”。

这些债务分别由 V3-03～V3-07 在真实 replacement 成立后处理，不允许提前物理删除 current owner。

## 5. V3-03：使用方生命周期

长期语义所有者：

`docs/architecture/consumer-lifecycle.md`

核心边界：

```text
上游可复用来源
→ 初始化 / 首次采用 或显式基线升级
→ 逐项 adopt / retain-or-override / reject-not-applicable / supersede-remove
→ 使用方本地候选状态
→ 采用验证
→ 上游评估基线推进
→ 只依赖本地当前状态的普通运行
→ 显式重新进入上游
```

必须保持：上游评估基线、本地资产实际来源和升级历史分离；普通运行默认不访问 upstream；升级失败不推进基线；重新进入上游必须有显式生命周期触发。

## 6. V3-04：Skill 重分类与准入

稳定结果已经进入 `docs/architecture/skill-architecture.md` 与相关契约 / Skill：

- 当前 9 个 Skill 身份继续成立；
- `execute-unit` 只薄消费工程纪律；
- `converge` 保持功能整体收敛过程；
- `github-actions-verification` 保持平台专项非核心 Skill；
- 验证 / 外部操作规则族没有证据形成新的通用 Skill；
- 使用方生命周期不转化为采用 / 升级 Skill；
- `first-batch-skill-design.md` 只保留历史设计 / Evidence 身份；
- 新 Skill 必须通过当前 Skill Architecture 准入门禁。

## 7. V3-05：面向 Agent 的资源模型

长期权威：

`docs/architecture/agent-resource-model.md`

核心模型：

```text
规范 / 事实正文
→ 资源固有结构
→ 派生发现投影
```

稳定边界包括：

- 资源是稳定语义 / 生命周期单元，不等同于任意文件；
- mixed 文件可以包含多个资源单元；
- 资源身份、V3-01 四维、本地 locator 与真实关系必须可恢复，但不要求统一 metadata block；
- `SKILL.md` `name / description`、技术画像版本 / 适用范围等原生字段继续由真实 owner 维护；
- 跨资源职责 / 条件 / 风险正规化提示属于派生发现层；
- 当前资源集合不由统一 `state` 字段维护；
- Activation Manifest 是混合过渡载体，长期 provenance / locator / supersede 等固有事实迁出前不得整体删除；
- Runtime Catalog 只能作为派生运行投影。

## 8. V3-06：资源发现架构

长期权威：

`docs/architecture/resource-discovery-architecture.md`

最小逻辑：

```text
本地当前资源与稳定入口
→ 可选 Reviewed Discovery Map
→ 可选纯生成 Runtime View
→ 临时发现决策
```

主要结论：

- Manifest + Catalog 两层不是必选；
- Local Discovery Entry 必须稳定可达；
- 小型仓库可以只依赖固定 Authority Entry 与资源原生信息；
- 需要跨资源语义正规化时只维护一个 current Reviewed Discovery Map；
- Map 不拥有规范正文，但 semantic-reviewed 映射必须有 source binding 与 coverage lifecycle；
- Runtime View 只能做确定性投影，不能独立维护语义；
- current resource set 来自真实 owner / V3-01 / 原生状态 / supersede-disable 事实；
- 一次发现一个主职责 + 最小辅助上下文；
- routing-only 不加载完整 Skill；execute 才按需加载；
- Stage Return 后旧 discovery decision 失效并重新发现；
- stale / missing / coverage drift / ambiguity 失败关闭到本地当前权威；
- ordinary runtime 不自动访问 upstream；
- candidate 新机制可以与旧 current 机制在分支上并存验证，但集成后的同一 runtime scope 只能有一个 current discovery mechanism。

## 9. V3-07：agentic-dev 自采用

跟踪：Issue #113。  
项目记录：`docs/project/rule-governance-v3-v3-07-self-adoption.md`。

基于 `agentic-dev` 当前真实仓库状态，V3-07 已裁决：

- 当前仓库没有实际版本化 Activation Manifest / Runtime Catalog 文件；
- 当前存在持续跨资源正规化需求，因此需要一个小型 Reviewed Discovery Map；
- 当前没有证据要求第二层 Runtime View / Catalog / generator；
- `agentic-dev` 自身 Local Discovery Entry 为 `docs/discovery/README.md`；
- Reviewed Discovery Map 为 `docs/discovery/reviewed-discovery-map.md`；
- Map 是非规范性派生输入，不进入 Repository Authority 顺序；
- `rule-activation-guide.md` 降为低频初始化 / 采用 / 升级导航，不再维护 ordinary runtime 手工职责表；
- `consumer-local-rule-activation.md` 保留 Consumer-local 落地说明，不再作为 Manifest / Catalog / routing / Stage Return / fail-closed 的第二规范 owner；
- v2 metadata / routing project contract 保留历史设计 / Evidence 价值，不再承担当前长期发现 owner。

Candidate validation 已覆盖 Fresh Context、routing-only、execute、GitHub Actions、工程纪律、技术画像、验证规则、外部操作、Stage Return、stale / missing / coverage drift / ambiguity、no-match 与 local-only ordinary runtime。候选验证阶段发现的 membership/source binding、外部操作过度激活和 Map 重复算法问题均已修正。

V3-07 当前必须在拟集成状态继续验证**current mechanism 唯一性、cutover 后入口、v2 资产降级和 source binding currentness**，并完成最终高影响 AI 复核。

## 10. v1 / v2 必须保留的成果

v3 必须继续保护：

- 薄启动入口；
- 仓库 / Consumer 权威优先；
- 渐进式披露；
- 证据先于声明；
- 规范正文单点所有权；
- 派生发现机制不拥有规范正文；
- 陈旧、缺失、歧义时失败关闭；
- 主职责与最小辅助上下文分离；
- routing-only 不机械加载完整 Skill；
- execute 时按需加载 Skill；
- Stage Return 后重新发现；
- Consumer 普通运行只依赖本地 current resources；
- 基线采用逐项采用 / 保留覆盖 / 拒绝 / 取代；
- 同一运行范围 / 发现职责不并行维护多个 current 派生机制。

V3-03～V3-07 的任务是把这些行为从过渡设计提升到正确的长期 semantic owner / 本地运行机制，而不是借“重构”为理由推翻真实 Consumer 已验证行为。

## 11. 当前非目标与 ADR 门禁

V3-07 不：

- 重新定义 V3-01～V3-06；
- 修改任何 Consumer Repository；
- 直接执行 V3-08；
- 创建 Rule Super Skill / Stage Router Skill / Runtime Controller；
- 全仓批量增加 Front Matter 或统一 YAML / JSON schema；
- 为形式完整创建 Manifest / Catalog / generator；
- 建立数据库、向量库、图数据库、MCP 服务或后台 daemon；
- 启动 WI-06 / WI-07 / WI-09 或其他独立候选。

v3 不用一个“大 ADR”承载全部探索。只有专项分析形成跨任务长期约束、存在实质替代方案与长期后果、且决定已经稳定时才创建或更新 ADR。

当前高概率 ADR 候选继续包括：

- 知识与能力所有权架构；
- Skill 承担过程型能力与 Guide / Rule 承担普通运行内容之间的长期边界；
- 面向 Agent 的资源模型 / 派生发现架构（在 V3-07 / V3-08 自采用与 Consumer 证据完成后再判断是否需要单独 ADR 化）。

目录名、字段名、文件拆分数量或具体序列化格式不自动 ADR 化。

## 12. 当前门禁

V3-07 跟踪入口：Issue #113。  
工作产物：

- `docs/discovery/README.md`；
- `docs/discovery/reviewed-discovery-map.md`；
- `docs/project/rule-governance-v3-v3-07-self-adoption.md`。

V3-07 的精确审查、集成与完成状态以 Issue #113 和 GitHub 当前状态为准，本文件不复制瞬时 PR 状态。

V3-07 完成门禁为：

> 已恢复 `agentic-dev` self-runtime surface；Map / Runtime View 必要性由真实仓库复杂度裁决；稳定 Local Discovery Entry 已形成；Reviewed Discovery Map coverage / source binding / currentness / review lifecycle 完整；candidate 验证通过；v2 current discovery / routing 资产完成 migration / compatibility / historical disposition；replacement 以单一拟集成状态完成，同一 runtime scope 只有一个 current discovery mechanism；post-cutover Fresh Context / routing / Skill loading / Stage Return / fail-closed 复验通过；高影响自采用与 replacement 不存在未解决 Blocking / Medium；未修改 Consumer Repository、未提前执行 V3-08。

如果 Issue #113 仍开放，应继续完成上述未满足门禁；如果 Issue #113 已以完成原因关闭，则 V3-07 已收口，**V3-08 只成为下一规划候选**。只有新的 V3-08 Planning Authority 建立后才能启动 V3-08。