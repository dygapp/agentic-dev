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

V3-03 已完成并通过 PR #106 集成，集成提交为 `3043e95193f462348dd9fcb99f8a1871145d503d`。`docs/architecture/consumer-lifecycle.md` 已成为使用方初始化、采用、升级、普通运行与重新进入上游的长期规范权威。

V3-04 已由 Issue #107 正式启动，直接消费 V3-02 的 Skill / Guide overlap 审计与 V3-03 的使用方生命周期边界，不重新执行仓库盘点或重新设计 V3-03。

上述评估只作为证据与复核输入；长期结论以已经集成的仓库权威为准。

## 3. 当前规划主线

v3 按以下有限子任务顺序推进：

1. **V3-01 — 知识与能力所有权模型 — 已完成并集成**  
   已建立四维所有权判断矩阵，作为后续审计的分类依据。
2. **V3-02 — 当前仓库所有权审计 — 已完成并集成**  
   已按规范正文 / 规则族审计当前仓库并形成后续 disposition 候选；未执行物理迁移。审计矩阵：`docs/project/current-repository-ownership-audit-v3.md`。
3. **V3-03 — 使用方初始化、采用、升级与普通运行生命周期 — 已完成并集成**  
   长期权威：`docs/architecture/consumer-lifecycle.md`。
4. **V3-04 — 技能重分类与准入 — 状态见 Issue #107**  
   工作产物：`docs/project/skill-reclassification-admission-v3.md`。确认当前 Skill 身份、跨 owner overlap、历史设计 currentness、新 Skill 准入和 supporting-resource 边界。
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

`using-agentic-dev.md` 保留 Guide 主身份。V3-03 已将其中初始化 / 采用 / 基线升级的长期规范生命周期语义归入 `docs/architecture/consumer-lifecycle.md`；路由、新上下文中的资源发现等普通运行发现语义仍等待 V3-06。V3-04 只处理 Guide 与 Skill procedure / inventory 的边界，不执行 Guide 物理拆分。

## 7. Consumer 初始化与演进方向

V3-03 将“使用方生命周期”定义为可复用工程能力，而不是新的产品开发方法阶段，也不因为它具有过程顺序就自动成为 Skill。

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

必须保持三类状态职责分离：

- **上游评估基线**：最近完整比较并完成采用决定的精确上游边界；
- **当前本地资产来源**：每个当前本地资产的真实来源与后续使用方本地演进；
- **仅升级使用的决策历史**：此前保留、覆盖、拒绝和取代判断的证据。

一个基线指针不能代表“全部上游已采用”。已有使用方升级失败或中断时，不推进上游评估基线，不声明升级完成，也不因为一次升级尝试自动使原有当前所有者失效。

采用 / 升级同时控制两侧当前有效性：上游候选固定为精确标识；完成前重新确认使用方侧相关仓库权威 / 本地所有者。如果本地发生实质漂移，只重算受影响的决定与验证；无法安全判断影响范围时失败关闭。

重新进入上游后必须区分采用路径与非采用路径。只读比较、研究、实验或验证只能形成分析 / 证据，不修改使用方当前状态，也不推进上游评估基线。

采用 / 升级完成前存在生命周期层面的验证责任；具体测试、运行 / 发现规则、Skill 行为与证据声明继续由真实语义所有者和使用方仓库权威决定，V3-03 不复制第二份验收规则正文。

进入普通运行后，使用方默认只依赖本地当前状态。本地发现信息陈旧、缺失或歧义本身不允许自动打开上游；普通路径先失败关闭到使用方当前权威。只有显式基线升级、确认本地必要可复用能力缺失且使用方仓库权威允许、明确 `agentic-dev` 实验 / 验证、使用方仓库权威明确要求，或首次采用时，才允许重新进入上游。

V3-03 只固定这些生命周期语义，不冻结目录、metadata 字段、Manifest / Catalog、安装方式或资源发现算法。

## 8. V3-04 技能重分类与准入

V3-04 当前结论以 `docs/project/skill-reclassification-admission-v3.md` 为项目级审计记录，稳定长期 Skill 规则提升到 `docs/architecture/skill-architecture.md`。

当前确认：

- 现有 9 个 Skill 的独立身份继续成立，没有证据要求新增第 10 个 Skill、删除或合并现有 Skill；
- `execute-unit` 保持单执行单元实施 / 验证职责，但 Engineering Discipline 详细规则应由 `engineering-disciplines.md` 单点拥有，Skill 只做薄消费；
- `converge` 保持 Feature-wide 收敛过程，跨职责验证规则继续由对应验证工程能力持有；
- `github-actions-verification` 保持平台专项 Skill，GitHub Actions 平台过程可以详细，但通用外部操作 / 验证规则不由它拥有；
- verification / external-operation rule families 当前都没有足够证据形成新的通用 Skill；
- 使用方生命周期不会因为具有过程顺序就转化为 adoption / upgrade Skill；
- `first-batch-skill-design.md` 只保留第一批 Skill 的历史实现设计 / Evidence 身份，不再与当前 Skill Architecture / Contracts / `SKILL.md` 平行；
- 新 Skill 准入必须同时证明 Trigger、Inputs、Procedure、Outputs、Exit / Return / Escalation、Composability、Ownership、Evidence 与 Evaluation；
- supporting resource 只有直接服务一个 Skill 且不独立拥有跨 Skill 规范语义时，才继续作为 Skill 内部资源。

V3-04 不把“可复用”“Agent 会读取”“内容重要”“存在步骤”或“被多个 Skill 消费”单独视为 Skill 准入理由，也不创建 Rule Super Skill、Stage Router Skill 或完整生命周期 Controller。

## 9. v1 / v2 必须保留的成果

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

V3-03 进一步显式保护：上游评估基线与当前本地资产来源分离、仅升级使用的决策历史不进入普通新上下文、部分完成 / 失败升级不制造完成状态、上游更新不自动改变普通运行。

V3-04 进一步保护：Skill 只拥有稳定独立 procedure，Engineering Discipline / Consumer Lifecycle / Repository Policy / Guide 不为了运行时激活便利被机械 Skill 化，supporting body 不因物理目录自动取得平级规范所有权。

v3 不以“重新设计”为理由推翻这些已经通过真实 Consumer 验证的行为。

## 10. 当前非目标与 ADR Gate

V3-04 不：

- 重新设计 V3-03 使用方生命周期；
- 批量新增、删除或重写当前 Skill；
- 创建 Rule Super Skill、Stage Router Skill 或 adoption / upgrade Skill；
- 实现新的 Rule Index / Manifest / Catalog；
- 实现 Front Matter generator；
- 冻结统一 metadata schema；
- 物理移动、拆分、重命名或删除 Guide / Authority；
- 修改使用方仓库；
- 实现完整资源发现 / 路由架构；
- 启动 V3-05～V3-08；
- 启动 WI-06 / WI-07 / WI-09 或其他独立候选。

v3 不用一个“大 ADR”承载全部探索。只有专项分析形成跨任务长期约束、存在实质替代方案与长期后果、且决定已经稳定时才创建或更新 ADR。

高概率 ADR 候选仍包括：

- 知识与能力所有权架构；
- 以技能承担过程型能力，与以 Guide / Rule 承担普通运行过程之间的长期边界；
- 面向 Agent 的资源 metadata / 派生资源索引（仅在 V3-05 / V3-06 证明需要后）。

目录名、字段名、文件拆分数量等局部实现选择不自动 ADR 化。

## 11. 当前 Gate

V3-04 跟踪入口：Issue #107。  
工作产物：`docs/project/skill-reclassification-admission-v3.md`。  
长期 Skill 准入权威：`docs/architecture/skill-architecture.md`。

V3-04 的精确审查、集成与完成状态以 Issue #107 和 GitHub 当前状态为准，本文件不复制瞬时 PR 状态。

V3-04 完成 Gate 为：

> 当前 9 个 Skill 的身份与主要 overlap 均有明确结论；Skill、工程纪律 / 画像 / 使用方生命周期、仓库本地规则、Guide 与平台专项过程边界稳定；历史 Skill design 不再形成平行 current Authority；新 Skill 准入与 supporting-resource 规则已进入长期 Skill Architecture；高影响 Skill ownership / admission 歧义不存在未解决的 Blocking / Medium finding。

如果 Issue #107 仍开放，应继续完成上述未满足 Gate；如果 Issue #107 已以完成原因关闭，则 V3-04 已收口，V3-05 只成为下一规划候选。只有新的 V3-05 规划权威建立后才能启动 V3-05。

无论 V3-04 状态如何，本阶段结论都不自动授予 Guide 物理迁移、metadata / 资源发现实现、Consumer Repository 修改或后序阶段权限。