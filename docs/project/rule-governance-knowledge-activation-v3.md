# 规则治理与知识激活 v3 — 知识与能力所有权收敛

**状态：** 规划中  
**跟踪：** Issue #94  
**启动基线：** `master@3c31ae96683c4a653f001402b889b40e87df976b`

## 1. 目标

v3 的首要目标不是继续增加 Rule Index、Manifest、Catalog 或其他发现技术，而是先解决更上游的问题：

> `agentic-dev` 中的长期知识、规则和 Agent 能力是否被正确的**语义所有者**持有，并能被真实 Consumer 以本地、可持续的方式使用？

v1 / v2 已验证最小上下文、使用方本地普通运行、来源时效性和渐进式披露的重要性。如果核心方法、Skill、可复用工程能力、仓库本地规则、项目权威与指南的边界本身不清楚，任何新的发现机制都会继承并放大所有权债务。

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

V3-01～V3-07 已完成并集成：

- **V3-01 — 知识与能力所有权模型**：PR #100；建立语义所有者、适用范围 / 来源状态、运行 / 生命周期角色、载体 / 权威形式四维判断；
- **V3-02 — 当前仓库所有权审计**：完成主要 rule family / semantic body 审计并独立复核；
- **V3-03 — 使用方生命周期**：PR #106；长期权威 `docs/architecture/consumer-lifecycle.md`；
- **V3-04 — 技能重分类与准入**：PR #108；当前 9 个 Skill 身份继续成立，Skill 准入与 supporting resource 边界进入 Skill Architecture；
- **V3-05 — 面向 Agent 的结构化资源模型**：PR #110；长期权威 `docs/architecture/agent-resource-model.md`；
- **V3-06 — 资源发现架构**：PR #112；长期权威 `docs/architecture/resource-discovery-architecture.md`；
- **V3-07 — `agentic-dev` 自采用与发现机制切换**：PR #114，集成提交 `2fe193035c629f6b8805fd473bd322f70fe6e172`；当前 self-runtime 入口 `docs/discovery/README.md`，Reviewed Discovery Map 为 `docs/discovery/reviewed-discovery-map.md`。

V3-07 已证明 `agentic-dev` 自身不需要 Manifest / Runtime Catalog / generator；其 ordinary runtime 使用一个 Local Discovery Entry + 一个非规范性 Reviewed Discovery Map，旧 Guide 手工 routing surface 已退出 current discovery responsibility。

历史 GPT / 其他 AI 评估只作为挑战和复核证据；长期结论以已经集成的仓库权威为准。

## 3. 当前规划主线

v3 按以下有限子任务推进：

1. **V3-01 — 知识与能力所有权模型 — 已完成并集成**
2. **V3-02 — 当前仓库所有权审计 — 已完成并集成**
3. **V3-03 — 使用方初始化、采用、升级与普通运行生命周期 — 已完成并集成**
4. **V3-04 — 技能重分类与准入 — 已完成并集成**
5. **V3-05 — 面向 Agent 的结构化资源模型 — 已完成并集成**
6. **V3-06 — 资源发现架构 — 已完成并集成**
7. **V3-07 — `agentic-dev` 自采用与发现机制切换 — 已完成并集成**
8. **V3-08 — Consumer 验证与持续有效性复核 — 状态见 Issue #115**
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

V3-02 按 semantic body / rule family 审计，而不是按目录判断身份。已确认的主要债务包括：Guide 混入 ordinary discovery / reusable capability；已完成项目记录承载 current contract；手工 derived router 与真实 owner 重叠；Skill / Discipline / Verification Rule 复制风险。V3-03～V3-07 只有在真实 replacement 成立后才逐项实施 disposition。

## 5. V3-03：使用方生命周期

长期语义所有者：`docs/architecture/consumer-lifecycle.md`。

核心主线：

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

长期权威：`docs/architecture/agent-resource-model.md`。

核心模型：

```text
规范 / 事实正文
→ 资源固有结构
→ 派生发现投影
```

资源是稳定语义 / 生命周期单元，不等同于任意文件；原生身份 / provenance / locator / supersede 等真实长期事实由 semantic owner 生命周期管理；跨资源职责 / 条件 / 风险正规化属于派生发现层；current resource set 不由第二统一 `state` 真值维护。

## 8. V3-06：资源发现架构

长期权威：`docs/architecture/resource-discovery-architecture.md`。

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
- Reviewed Discovery Map 只有真实跨资源正规化需要时才维护；
- Map 不拥有规范正文，semantic-reviewed mapping 必须有 source binding / coverage lifecycle；
- Runtime View 只能是确定性投影；
- 一次发现一个主职责 + 最小辅助上下文；
- routing-only 不机械加载完整 Skill；
- execute 才按需加载；
- Stage Return 后旧 discovery decision 失效；
- stale / missing / coverage drift / ambiguity 失败关闭到本地当前权威；
- ordinary runtime 不自动访问 upstream；
- 集成后的同一 runtime scope 只能有一个 current discovery mechanism。

## 9. V3-07：agentic-dev 自采用 — 已完成

项目记录：`docs/project/rule-governance-v3-v3-07-self-adoption.md`。

最终结果：

```text
AGENTS / README / Roadmap / GitHub current state
→ 按需 docs/discovery/README.md
→ 按需 docs/discovery/reviewed-discovery-map.md
→ current semantic owner / primary Skill
```

当前仓库没有物理 Activation Manifest / Runtime Catalog，也没有证据要求 Runtime View / generator。Map 区分 membership-reviewed / semantic-reviewed / current-locator；非规范性、不进入 Repository Authority；`rule-activation-guide.md`、`using-agentic-dev.md`、`consumer-local-rule-activation.md` 已退出平行 ordinary routing owner。

Candidate validation、post-cutover validation 与最终高影响 AI Review 均通过，Blocking / Medium = 0。Issue #113 已完成关闭。

## 10. V3-08：Consumer 验证与持续有效性复核

跟踪：Issue #115。  
项目记录：`docs/project/rule-governance-v3-v3-08-consumer-validation.md`。  
协调计划：`tasks/plans/20260911/06-rule-governance-v3-v3-08-consumer-validation.md`。

### 10.1 目标

V3-08 验证 V3-03～V3-07 是否真正服务真实 Consumer，而不是只在 `agentic-dev` 自身成立。

Primary real Consumer：`dygapp/jilinjobs-cms`。

当前 `agentic-dev` 会话只读 Consumer。需要 baseline upgrade、local projection 或 controlled negative test 时必须进入 Consumer 自己的 Repository Authority / 独立会话；V3-08 Authority 不授予 Consumer merge 权限。

### 10.2 Gate A 当前设计

Gate A 已固定五个轨道：

- **Track A — Pre-upgrade read-only observation**：真实 old-baseline ordinary runtime / state conflict 对照；
- **Track B — Existing Consumer explicit baseline upgrade**：exact baseline comparison + per-item adoption / local projection；
- **Track C — Post-adoption runtime / fail-closed**：local-only、primary/supporting、drift、coverage、Stage Return；
- **Track D — Sustained validity**：使用 Consumer 后续真实项目演进，不人为制造业务任务；
- **Track E — First-adoption coverage**：按 claim 复用历史 Evidence；不足时使用最小隔离 fixture，不破坏成熟 Existing Consumer。

Consumer 当前 evaluated baseline 为 `d9fad0da83dbdb61cac5eb9778b0258c6861eef1`；V3-08 candidate upstream baseline 固定为 `2fe193035c629f6b8805fd473bd322f70fe6e172`。两者 exact compare 为 34 commits ahead / 0 behind，必须分类 reusable 与 `agentic-dev` project-only，不允许复制完整 upstream。

### 10.3 当前真实 Consumer finding

Gate A 只读恢复发现：Consumer 当前静态 `docs/work/current/*` 仍保存 EU-54 Readiness PENDING / Execute NOT GRANTED，而 Issue #60 Current Evidence 与活动 implementation PR 已进入 Readiness PASS / Execute lifecycle。

这不是纯 current-locator 的正常漂移，而是**两个 current surface 的状态冲突**。V3-08 的预期是：发现冲突 → 回到 Consumer Authority / Current Evidence / 外部事实对账 → fail-closed 或取得足够授权依据后继续；不得静默猜测，也不得新造“GitHub 永远高于 Work artifact”的通用优先级。

该 finding 初步属于 Consumer-local state-governance / source-currentness，是否修复 Consumer 状态 owner / 回写策略由 Consumer Repository 决定。

### 10.4 Context-cost 假设

Consumer 当前声明的五个默认 Fresh Context 入口文件静态大小合计约 `90,984 bytes`，其中 `docs/project/development-method.md` 约 37.5 KB。该数字只是静态文件大小，不等于 token 或每次真实读取成本。

Gate A 的可证伪假设是：state-only / routing-only 场景不应为了保险机械加载完整 Consumer-local Method / Skills。Existing `docs/README.md` 是 Local Discovery Entry 的强候选，但不是预设答案；是否需要 Consumer-local Reviewed Discovery Map 同样必须由 local inventory / measured cost / correctness 决定。

### 10.5 与当前 Consumer Execute 的隔离

Consumer 当前 EU-54 已进入独立 Execute 生命周期，因此：

```text
EU-54 未自然收口
→ V3-08 只允许 Track A 旁路只读观察

EU-54 收口后
→ 重新读取届时 latest Consumer main / Authority
→ 若无 conflicting active Execute work
→ 才建立独立 baseline-upgrade experiment branch
```

这样避免方法升级反向扩大当前产品 EU scope，或把两类 Evidence 混成同一 claim。

## 11. v1 / v2 必须保留的成果

v3 必须继续保护：薄启动入口、Consumer Authority 优先、渐进式披露、证据先于声明、规范正文单点所有权、派生发现不拥有正文、stale / missing / ambiguity fail-closed、主职责 + 最小辅助、routing-only / execute 分离、Stage Return rediscovery、ordinary runtime local-only、基线逐项采用，以及同一 runtime scope 不并行维护多个 current derived mechanism。

V3-08 的责任是取得真实 Consumer Evidence；不能为了证明新模型成功而改变这些已验证行为或把 Consumer 改造成 `agentic-dev` 镜像。

## 12. 当前非目标与 ADR 门禁

V3-08 不：

- 重新定义 V3-01～V3-07 作为默认起点；
- 在 `agentic-dev` 会话直接修改 Consumer Repository；
- 强制 Consumer 使用 Reviewed Discovery Map / Runtime View / Manifest / Catalog；
- 用 context-cost 优化覆盖 correctness / Authority / fail-closed；
- 把 Consumer 产品事实提升为通用规则；
- 因单次 Consumer PASS 就关闭 v3；
- 自动进入独立复核 / ADR / 正式实现规划；
- 启动 WI-06 / WI-07 / WI-09 或其他独立候选。

v3 不用一个“大 ADR”承载全部探索。只有专项分析形成跨任务长期约束、存在实质替代方案与长期后果、且决定已经稳定时才创建或更新 ADR。资源模型 / 派生发现架构是否需要单独 ADR，应在 V3-08 Consumer Evidence 与后续独立复核之后判断。

## 13. 当前门禁

V3-08 跟踪入口：Issue #115。  
当前 Gate：**Gate A — Validation Design**。

Gate A 完成条件由 `docs/project/rule-governance-v3-v3-08-consumer-validation.md` 单点记录；本文件只保留阶段边界：

> Primary Consumer、exact baselines、Active Consumer Work 隔离、Tracks A～E、Evidence Contract、negative-test 边界、context-cost 口径与 Consumer handoff 均明确；Current State conflict 已纳入 fail-closed / classification；first-adoption 有 closure 路径；风险 / AI 复核不存在未解决 Blocking / Medium；未修改 Consumer Repository、未提前进入 Consumer 写实验。

Gate A PASS 只允许把验证设计交给 Consumer 独立会话；它不等于 V3-08 PASS。

V3-08 后续必须满足 Issue #115 Gate B～D：真实 Consumer runtime Evidence → finding classification / impact review → 必要修订与重验 → sustained-validity / first-adoption closure → 高影响复核 → Blocking / Medium = 0。

如果 Issue #115 仍开放，应继续 V3-08 当前未完成 Gate；如果 Issue #115 已以完成原因关闭，则 V3-08 已收口，**独立复核只成为下一规划候选**，仍需新的规划权威才能启动。