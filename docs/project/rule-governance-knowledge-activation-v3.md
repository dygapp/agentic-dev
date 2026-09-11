# 规则治理与知识激活 v3 — 知识与能力所有权收敛

**状态：** 规划中  
**跟踪：** Issue #94  
**启动基线：** `master@3c31ae96683c4a653f001402b889b40e87df976b`

## 1. 目标

v3 的首要目标不是继续增加 Rule Index、Manifest、Catalog 或其他发现技术，而是先解决更上游的问题：

> `agentic-dev` 中的长期知识、规则和 Agent 能力是否被正确的**语义所有者**持有？

v1 / v2 已验证最小上下文、Consumer 本地普通运行、来源时效性和渐进式披露的重要性。当前进一步暴露出：如果核心方法、技能、可复用工程能力、仓库本地规则、项目权威与 Guide 的边界本身不清楚，任何新的发现机制都会继承并放大所有权债务。

因此 v3 采用以下顺序：

```text
先确定语义所有者
→ 再审计现有内容
→ 再确定 Consumer 生命周期
→ 再判断技能 / 可复用工程能力边界
→ 最后才设计 metadata / discovery
```

其中 `metadata`、`discovery` 等仅在需要指代具体技术机制时保留原样，不把它们扩展成文档主体语言。

## 2. 启动依据

规则治理与知识激活 v2 已通过 PR #93 集成。v2 的可复用结果继续作为 v3 必须保护的已验证基线。

在正式启动 v3 前，临时评估分支 `eval/rule-governance-v3-gpt6-review` 对候选治理方向进行了独立挑战：

- 首轮评审发现原候选没有为工程纪律、技术画像、验证画像等“跨项目可复用、但不具有独立任务流程”的能力提供明确归属；
- 该问题经当前正式工程能力架构复核后接受；
- 候选修订为四维所有权判断，并补充“可复用工程能力 / 工程纪律 / 画像”语义所有者；
- 定向复评后阻塞、中等、低等级问题均为 0。

V3-01 随后又通过独立 holdout 复核发现并修正“项目 / 产品权威”过宽的问题：仓库协作、授权、验证、复核和集成政策即使经过正式决定，也仍由仓库本地政策拥有，不因为“项目已经决定”就自动成为项目 / 产品权威。定向复评通过后，V3-01 已完成并通过 PR #100 集成。

V3-02 基于 V3-01 的四维模型完成当前仓库语义所有权审计。收敛过程中先通过 Repository Evidence 自查识别并修正 Research / Eval current control body 的目录机械分类风险；随后独立复核发现并修正 Consumer adoption acceptance 被整体归为 Evidence 的所有权问题。最终定向复核不存在未解决的 Blocking / Medium finding。V3-02 已完成并集成，其审计矩阵成为 V3-03～V3-06 的直接分析输入。

V3-03 已由 Issue #104 正式启动，候选长期 owner 为 `docs/architecture/consumer-lifecycle.md`。本阶段不重新做 inventory，而是把 V3-02 已识别的 Consumer lifecycle 规则族从 Guide / completed-project transitional contract 中提炼为单一规范性可复用工程能力。

上述评估只作为证据与复核输入；长期结论以已经集成的仓库权威为准。

## 3. 当前规划主线

v3 按以下有限子任务顺序推进：

1. **V3-01 — 知识与能力所有权模型 — 已完成并集成**  
   已建立四维所有权判断矩阵，作为后续审计的分类依据。
2. **V3-02 — 当前仓库所有权审计 — 已完成并集成**  
   已按规范正文 / 规则族审计当前仓库并形成后续 disposition 候选；未执行物理迁移。审计矩阵：`docs/project/current-repository-ownership-audit-v3.md`。
3. **V3-03 — Consumer 初始化、采用、升级与普通运行生命周期 — 当前**  
   跟踪 Issue #104；候选 PR #106。目标是建立单一 lifecycle owner，明确一次性初始化 / 采用 / 升级与 ordinary local-only runtime 的边界。
4. **V3-04 — 技能重分类与准入**  
   判断现有 Guide / Rule 中哪些属于已有技能、可复用工程能力、仓库本地规则或真正的新技能候选。
5. **V3-05 — 面向 Agent 的结构化资源模型**  
   在所有权已经确定后，定义哪些长期资源需要结构化 metadata，以及普通 Markdown 与 `SKILL.md` 的兼容边界。
6. **V3-06 — 资源发现架构**  
   判断所有权修正后还需要多复杂的仓库资源发现机制；不得预设一定需要统一 Index。
7. **V3-07 — `agentic-dev` 自采用**  
   让 `agentic-dev` 自身使用与 Consumer 相同的核心模型，避免维护两套架构。
8. **V3-08 — Consumer 验证**  
   在真实 Consumer 上验证初始化、升级、普通运行、来源时效性、上下文成本和失败关闭行为。

只有前序 Gate 满足后才能进入后序任务；Roadmap 顺序不自动授予执行权限。

## 4. V3-01 已确认的所有权模型

当前正式分类至少区分以下语义所有者：

1. 核心方法 / 原则；
2. 技能 / 过程型能力；
3. 可复用工程能力 / 工程纪律 / 画像；
4. 仓库本地政策 / 规范 / 规则；
5. 项目 / 产品权威资源；
6. Guide；
7. 研究 / 输入 / 证据。

同时把以下维度与语义所有者分开判断：

- 适用范围与来源状态；
- 运行与生命周期角色；
- 载体与权威形式。

Architecture、Contract、Profile、`SKILL.md`、Guide、ADR、Requirement、generated index 等文件或载体形式不能直接替代语义所有权判断。

正式判断矩阵：`docs/project/knowledge-capability-ownership-model-v3.md`。

## 5. V3-02 已完成的审计结论

V3-02 不按目录判断身份，而按规范正文 / 规则族判断。已识别并形成 disposition 候选的主要 ownership debt 包括：

1. `docs/guides/*` 中混入人类说明、仓库本地规范、可复用工程能力、Consumer 生命周期和普通运行发现语义；
2. 已完成 v2 的 `docs/project/*` 中仍有若干 discovery / adoption / runtime 契约继续支撑当前行为；
3. `rule-activation-guide.md` 属于手工派生导航而不是规范正文 owner，未来如果出现新的 current discovery mechanism 必须显式取代而不能长期并存；
4. Skill、工程纪律和验证规则之间存在需要 V3-04 逐规则族复核的正文重叠风险；
5. Research / Eval 的 current lifecycle、isolation、scoring、execution control body 不能因目录位置整体降格为 Evidence；
6. Consumer adoption acceptance 中“采用完成前必须验证”的责任属于 Consumer lifecycle / adoption verification，而被检查的 runtime / discovery 规则继续由各自 semantic owner 持有，V3-08 只消费派生验收输入。

审计矩阵只形成 disposition 候选。V3-02 已完成并不授权立即迁移；后续必须由 V3-03～V3-06 在各自 Gate 下设计和验证真实 owner / replacement。

## 6. Guide 边界

Guide 的边界保持为：

> 面向人，以及初始化、首次采用、基线升级等低频启动场景，解释如何理解、选择和采用 `agentic-dev`。

Guide 可以在初始化或升级时被 Agent 完整读取；这种一次性 token 成本本身不是问题。

Guide 不应继续承担：

- 普通运行中的核心 Agent 执行过程；
- 仓库本地政策的默认正文；
- 项目权威的事实正文；
- 可复用工程能力的默认容器；
- “不属于核心方法 / 技能”内容的兜底容器。

`using-agentic-dev.md` 保留 Guide 主身份。V3-03 正在将其中 initialization / adoption / baseline upgrade 的长期 normative lifecycle 归入 `docs/architecture/consumer-lifecycle.md`；routing / Fresh Context discovery 等 ordinary runtime discovery 语义仍等待 V3-06，当前不执行 Guide 物理拆分。

## 7. V3-03 Consumer 生命周期候选

V3-03 将 Consumer lifecycle 作为**可复用工程能力**，而不是新的 Product Development Method Stage，也不因为它有过程顺序就自动 Skill 化。

候选长期 owner：

`docs/architecture/consumer-lifecycle.md`

上层分类：

`docs/architecture/engineering-capability-architecture.md`

当前生命周期主线为：

```text
upstream reusable source
→ new Consumer initialization / first adoption
   OR Existing Consumer explicit baseline upgrade
→ reusable delta classification
→ per-item adopt / retain-or-override / reject-not-applicable / supersede-remove
→ Consumer-local current owner / capability candidate
→ adoption verification
→ evaluated upstream baseline advance
→ ordinary runtime local-only
→ explicit upstream re-entry condition
```

必须保持三类状态职责分离：

- evaluated upstream baseline：最近完整比较并完成 adoption 判断的 exact upstream boundary；
- active local asset provenance：每个 current local asset 的真实来源与后续本地演进；
- upgrade-only decision history：此前 retain / override / reject / supersede 的判断证据。

一个 baseline pointer 不能代表“全部 upstream 已采用”。Existing Consumer upgrade 失败或中断时，不推进 evaluated baseline，不声明 upgrade complete，也不因为 upgrade attempt 自动使原 current owner 失效。

采用 / 升级完成前存在 lifecycle-level verification responsibility；具体测试、runtime / discovery rule、Skill behavior 与 Evidence Claim 继续由真实 semantic owner 和 Consumer Authority 决定，V3-03 不复制第二份验收规则正文。

进入 ordinary runtime 后，Consumer 默认只依赖 Consumer-local current state。local discovery stale / missing / ambiguous 本身不允许自动打开 upstream；普通路径先 fail-closed 到 Consumer Current Authority。只有显式 baseline upgrade、确认本地必要 reusable capability 缺失且 Consumer Authority 允许、明确 `agentic-dev` experiment / validation、Consumer Authority 明确要求或首次采用时，才允许重新进入 upstream。

V3-03 只冻结这些 lifecycle semantics，不冻结目录、metadata 字段、Manifest / Catalog、安装方式或 discovery algorithm。

## 8. v1 / v2 必须保留的成果

v3 必须继续保护至少以下已经验证的长期成果：

- 薄启动入口；
- 仓库 / Consumer 权威优先；
- 渐进式披露；
- 证据先于结论；
- 规范正文单点所有权；
- 派生发现机制不拥有规范正文；
- 陈旧、缺失、歧义时失败关闭；
- 主职责与最小辅助上下文分离；
- 只做路由判断时不机械加载完整技能；
- 真正进入职责时按需加载技能；
- 阶段返回后重新判断；
- Consumer 普通运行只依赖 Consumer-local 现行资源；
- 基线采用逐项采用、保留 / 覆盖、拒绝、取代；
- 同一运行范围 / 发现职责不并行维护多个现行派生机制。

V3-03 进一步显式保护：evaluated baseline 与 active asset provenance 分离、upgrade-only history 不进入普通 Fresh Context、partial / failed upgrade 不制造完成状态、upstream 更新不自动改变 ordinary runtime。

v3 不以“重新设计”为理由推翻这些已经通过真实 Consumer 验证的行为。

## 9. 当前非目标与 ADR Gate

V3-03 当前不：

- 实现新的 Rule Index / Manifest / Catalog；
- 实现 Front Matter generator；
- 冻结统一 metadata schema；
- 创建 Rule Super Skill / Stage Router Skill；
- 批量新增或改造技能；
- 物理移动、拆分、重命名或删除 Guide / Authority；
- 修改 Consumer Repository；
- 实现完整 resource discovery / routing architecture；
- 启动 V3-04～V3-08；
- 启动 WI-06 / WI-07 / WI-09 或其他独立候选。

v3 不用一个“大 ADR”承载全部探索。只有专项分析形成跨任务长期约束、存在实质替代方案与长期后果、且决定已经稳定时才创建或更新 ADR。

高概率 ADR 候选仍包括：

- 知识与能力所有权架构；
- 以技能承担过程型能力，与以 Guide / Rule 承担普通运行过程之间的长期边界；
- 面向 Agent 的资源 metadata / 派生资源索引（仅在 V3-05 / V3-06 证明需要后）。

目录名、字段名、文件拆分数量等局部实现选择不自动 ADR 化。

## 10. 当前 Gate

当前正式工作入口：Issue #104 — V3-03 Consumer 初始化、采用、升级与普通运行生命周期。  
当前候选：PR #106（Draft）。

V3-03 当前允许形成和收敛 Consumer lifecycle Authority、父级能力分类、稳定 Root 指针与项目恢复入口，并执行与风险相称的 AI 复核。

V3-03 Gate 为：

> 初始化、首次采用、baseline upgrade、local projection、adoption verification、baseline advance、ordinary runtime 与 upstream re-entry 形成单一一致生命周期；与 Method、Guide、Skill、V3-05、V3-06、V3-08 的 semantic owner 边界清晰；v2 已验证行为完整保留；高影响 lifecycle ambiguity 的 Blocking / Medium finding 为 0。

达到 Gate 后，只能进入 PR #106 的人工集成决策。只有 V3-03 实际集成并完成必要 Post-Integration closure 后，才判断是否正式启动 V3-04；不自动获得物理迁移、Skill 重构、metadata / discovery 实现或 Consumer 修改权限。