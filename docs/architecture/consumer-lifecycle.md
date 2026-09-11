# Consumer 初始化、采用、升级与普通运行生命周期

**状态：** 候选 v0.1（V3-03）  
**性质：** 规范性可复用工程能力架构  
**跟踪：** Issue #104

## 1. 目的

本文单点定义 Consumer 使用 `agentic-dev` 时的长期生命周期语义：

- 新 Consumer 如何建立最小本地权威并完成首次采用；
- Existing Consumer 如何显式评估新的 upstream baseline；
- reusable delta 如何逐项形成采用决定；
- adopted change 如何成为 Consumer-local current asset；
- adoption / upgrade 何时可以声明完成并推进 evaluated baseline；
- 完成后为什么 ordinary runtime 必须回到 Consumer-local；
- 哪些条件允许显式重新进入 upstream。

本文解决的是 **Consumer lifecycle**，不是软件产品开发阶段。它不新增 `docs/method/ai-development-method.md` 中的方法阶段，也不替代 Consumer Repository Authority、Skill Contract、资源发现架构或具体平台过程。

## 2. 权威与边界

本文属于跨仓库可复用工程能力。发生冲突时：

1. Consumer 自己的 Repository Authority 决定 Consumer 项目事实、授权、集成策略与本地 currentness；
2. `agentic-dev` Core Method / Principle 决定通用开发阶段、职责与完成语义；
3. 本文只拥有 upstream adoption / upgrade / ordinary-runtime re-entry 的生命周期语义；
4. Skill 的职责、输入、Procedure、Exit / Stage Return 由 Skill Architecture / Contract / `SKILL.md` 拥有；
5. metadata、Manifest、Catalog、source identity 与 discovery / routing 的具体结构和算法由后续资源模型与发现架构拥有；
6. Consumer 验证项目只验证本文及其他 owner 的行为，不取得这些规则的语义所有权。

因此：

```text
Consumer lifecycle
≠ Product development Method stage
≠ Skill procedure
≠ Discovery implementation
≠ Consumer project fact
```

## 3. 核心不变量

### 3.1 显式采用

upstream reusable capability 不因为存在、被读取、被复制或版本更高，就自动进入 Consumer current state。

必须经过显式采用：

```text
upstream candidate
→ compare against Consumer Current Authority
→ per-item decision
→ Consumer-local durable result
```

### 3.2 来源不等于当前权威

采用完成后：

```text
upstream provenance
≠ Consumer current authority
```

`adopted_from` 只说明来源，不把 future upstream commit 变成 Consumer 的自动更新通道。

### 3.3 evaluated baseline 不等于 adopted asset baseline

必须分离：

- **evaluated upstream baseline**：Consumer 最近完整比较并完成采用判断的 exact upstream baseline；
- **active local asset provenance**：每个 current local asset 实际采用或演进自哪个来源；
- **upgrade-only decision history**：retain / override / reject / supersede 等升级判断记录。

三者不能由一个“当前 baseline”字符串替代。

### 3.4 逐项采用，不做整库继承

baseline upgrade 的单位是对 Consumer 有持续意义的 reusable delta，而不是整个 upstream repository。

至少逐项区分：

- `adopt`；
- `retain / override`；
- `reject / not applicable`；
- `supersede / remove`。

upstream project-only 状态、Research / Eval / historical evidence 默认不投射为 Consumer ordinary-runtime Authority。

### 3.5 现有本地 semantic owner 优先

如果 Consumer 已有正确 owner 承载 adopted change，应更新现有 owner，而不是机械增加一份 upstream copy。

目标是：

```text
one current semantic owner
+ optional provenance / decision evidence
```

而不是：

```text
local rule body
+ copied upstream rule body
+ discovery summary body
```

### 3.6 采用完成前必须验证

首次采用或 baseline upgrade 只有在必要验证完成后才能声明完成，并推进 evaluated baseline。

本文拥有“必须验证后才能完成 adoption / upgrade”这一生命周期责任；具体被验证规则、测试方式、平台步骤和 Evidence Claim 仍由各自 semantic owner、Consumer Authority 与验证能力决定。

### 3.7 ordinary runtime local-only

采用完成后，Consumer ordinary runtime 必须只依赖 Consumer-local current state，不把 upstream repository 作为持续运行依赖。

### 3.8 upstream re-entry 必须显式

upstream 新提交、模型好奇、local discovery stale 或 routing ambiguity 都不能自行触发“读取最新 upstream 并改变当前行为”。重新进入 upstream 必须满足本文定义的显式条件。

## 4. 生命周期状态模型

本文定义五个语义状态。实现不要求使用这些名称、字段或固定目录。

### 4.1 `INITIALIZING`

适用于尚未完成首次采用的新 Consumer。

目标是建立足以继续工作的最小 Consumer-local Authority，而不是复制完整 `agentic-dev` 结构。

允许形成：

- 稳定 Repository Bootstrap / Authority Boundary；
- README 或等价人类入口；
- 当前真实需要的 Requirement / Specification / Architecture / Verification / Integration Authority；
- 当前需要采用的 reusable capability；
- 必要的 Roadmap / Task / Plan，但仅在真实协调需求存在时。

不允许为了模板完整预建空 Requirement、Architecture、ADR、Skill、Catalog 或历史目录。

### 4.2 `ADOPTION_EVALUATION`

适用于首次采用，也适用于 Existing Consumer 的显式 baseline upgrade。

此状态允许读取 upstream，但必须固定候选来源与比较边界，并针对 reusable delta 做逐项决定。

### 4.3 `LOCAL_PROJECTION_PENDING_VERIFICATION`

逐项决定已经形成，Consumer-local candidate owner / capability 已按需要更新，但 adoption / upgrade 尚未完成。

此时：

- candidate baseline 不能被声明为新的 evaluated baseline；
- 未验证的 candidate asset 不得仅因被写入工作分支或临时目录就自动成为 ordinary-runtime current owner；
- currentness 仍由 Consumer 自己的 Repository Authority / integration policy 决定；
- existing Consumer 不得因为升级未完成就丢失原有可用 current owner。

### 4.4 `ORDINARY_RUNTIME`

首次采用或 upgrade 验证完成后的稳定状态。

普通 Fresh Context 只消费 Consumer-local current state；upstream 仅保留 provenance 与未来显式升级意义。

### 4.5 `REENTRY_REQUESTED`

Consumer 在 ordinary runtime 中命中显式 upstream re-entry 条件时进入的过渡判断状态。

它只决定是否进入新的 `ADOPTION_EVALUATION` / experiment path，不授权直接用 upstream 内容覆盖本地 current owner。

## 5. 新 Consumer 初始化与首次采用

### 5.1 初始化先建立 Consumer 身份，再采用 reusable capability

新项目启动不是“安装 agentic-dev 模板”。应先确定：

- Consumer repository identity；
- Repository Authority / Knowledge Boundary；
- 当前目标与人工授权边界；
- 当前明确输入；
- 最小验证 / 集成策略；
- 当前真正需要的 reusable capability。

`agentic-dev` 自身 Roadmap、Issue / PR、当前里程碑、仓库提交习惯和 project-only policy 不自动继承。

### 5.2 原始需求输入与 Consumer Authority

原始需求、外部文档和研究资料默认是输入，不因为存在于仓库或带有 `approved` / `confirmed` 标签就自动成为 Consumer Authority。

如果人工已明确指定某份资料为当前权威需求，可以直接按该授权建立其 Consumer Authority 身份，不要求重复形式审批；仍需明确当前范围、优先级和无法解析的外部引用。

如果没有原始需求，不制造空 Requirement。后续在真实产品意图出现时由相应 Method / Skill owner 形成。

### 5.3 首次采用与普通项目初始化分离

Consumer-native Authority 与 reusable capability adoption 可以在同一初始化工作中完成，但语义必须分离：

```text
Consumer-native project fact
≠ adopted reusable capability
```

首次采用只选择当前 Consumer 真实需要、具有持续约束或能力价值的 reusable content。

### 5.4 首次采用完成 Gate

首次采用只有在以下条件满足后才能离开 `INITIALIZING` / adoption flow：

1. Consumer 有可恢复的最小 Repository Authority；
2. upstream candidate identity 已固定；
3. 当前相关 reusable items 已逐项判断；
4. adopted items 已形成 Consumer-local durable owner / capability；
5. reject / not-applicable items 不进入 active ordinary runtime；
6. Consumer-specific override / precedence 保持明确；
7. 必要 adoption verification 已完成；
8. first evaluated upstream baseline 可以被真实记录；
9. 新 Fresh Context 不依赖 upstream 即可继续 ordinary work。

## 6. Existing Consumer baseline upgrade

### 6.1 upgrade 是显式低频操作

Existing Consumer 不在普通任务中持续跟随 upstream latest。一次 upgrade 必须由 Consumer Authority、维护者或明确任务显式启动。

### 6.2 upgrade 最小输入

至少需要：

- Consumer Current Repository Authority；
- current Consumer-local capability / discovery state；
- previous evaluated upstream baseline；
- candidate exact upstream baseline；
- 两个 baseline 的实际 reusable delta；
- 与当前 delta 相关的 retained / overridden / rejected history；
- 当前 Consumer 技术栈、平台、验证与项目约束中的最小必要事实。

不为了升级读取全部历史聊天或 unrelated upstream project history。

### 6.3 upstream delta 先分类，再决定

至少区分：

- Method / Principle；
- Skill / Skill Contract；
- Engineering Discipline；
- Technology / Verification Profile；
- reusable Guide / lifecycle / runtime capability；
- Runtime Adapter / platform capability；
- `agentic-dev` project-only；
- Research / Eval / historical evidence。

只有 Consumer 可能持续消费的 reusable delta 进入 adoption decision。

## 7. 单项 Adoption Decision

### 7.1 `adopt`

适用于 Consumer 需要该 reusable change，且与 Consumer Current Authority 不冲突。

结果：

- 创建或更新正确的 Consumer-local semantic owner / capability；
- 保留真实 `adopted_from` provenance；
- 必要时更新 local discovery representation；
- 进入 adoption verification。

### 7.2 `retain / override`

适用于 Consumer 已有更具体的合法本地规则，或明确继续保留旧本地行为。

结果：

- current local owner 保持；
- 记录 candidate baseline 已被评估；
- 必要时记录 override / retain relation；
- 不伪造 active asset 已采用自 candidate baseline。

### 7.3 `reject / not applicable`

适用于当前 Consumer 不使用对应平台 / 能力、变化只属于 upstream 自己，或 Consumer 明确不采用。

结果：

- 仅在 upgrade history 中保留必要判断；
- 不创建 active runtime record；
- 不复制规范正文；
- 不制造 disabled placeholder 只为“目录完整”。

### 7.4 `supersede / remove`

适用于现有 local adopted asset 经新的显式决定不再 current。

结果必须保证：

- 新 current owner 已经可用并通过相应验证，或 Consumer 明确决定该能力不再需要；
- 旧 asset 从 current routing / active set 退出；
- 历史 provenance 可以保留；
- 新旧两份正文不能同时被解释为 current owner。

## 8. 三类 baseline / provenance 状态

### 8.1 Evaluated Upstream Baseline

只回答：

> Consumer 最近完整评估到哪个 exact upstream baseline？

它是比较边界，不是本地所有资产的版本声明。

### 8.2 Active Local Asset Provenance

每个 current local adopted asset 保留自己的实际来源。它可以早于当前 evaluated baseline，也可以经过 Consumer-local 演进后不再与某个 upstream 文件一一对应。

### 8.3 Upgrade-only Decision History

用于下一次 upgrade 理解此前的 retain / override / reject / supersede 决定。

它默认不进入 ordinary Fresh Context，也不是 current runtime Authority。

### 8.4 重新评估旧决定

旧 decision 至少在以下情况下重新进入 upgrade 判断：

- Consumer 技术栈或平台改变；
- 原 not-applicable capability 变为 applicable；
- Consumer override 被删除或实质变化；
- upstream 后续变化再次修改同一 semantic owner；
- Consumer 实际使用证据表明旧判断不再成立。

## 9. Adoption verification 与 baseline advance

### 9.1 生命周期责任

所有首次采用和 baseline upgrade 都必须在完成声明前验证 Consumer-local 结果。

验证目标不是证明“upstream 是正确的”，而是证明：

- 当前 adopted / retained 结果与 Consumer Authority 一致；
- current owner / supersede 关系没有产生双 owner；
- Consumer-local ordinary path 仍能恢复；
- 被采用能力所要求的具体行为和证据满足其真实 owner 的验收义务。

### 9.2 Baseline Advance Gate

只有以下条件满足后，candidate baseline 才能成为新的 evaluated upstream baseline：

1. candidate exact identity 已确认；
2. reusable / project-only / research / evidence delta 已分类；
3. Consumer 相关 reusable delta 均已逐项决定；
4. adopted / retained local owners 已按需要更新；
5. rejected / not-applicable 不进入 active runtime；
6. superseded old asset 不再作为 current owner；
7. Consumer Authority precedence 未被 upstream 覆盖；
8. lifecycle-level adoption verification 已完成；
9. 各具体 semantic owner 要求的必要验证已经满足；
10. ordinary-runtime local-only 路径仍成立；
11. baseline advance 没有被描述为“全部 upstream 内容均已采用”。

### 9.3 失败或中断

任一关键 Gate 未完成时：

- 不推进 evaluated upstream baseline；
- 不声明 adoption / upgrade complete；
- 不通过修改一个 baseline pointer 掩盖 partial state；
- Existing Consumer 原有 current owner 不因 upgrade attempt 自动失效；
- candidate local change 的 currentness 继续由 Consumer 自己的 Repository Authority / integration policy 判断。

本文不强制 Consumer 使用 PR、事务提交或某种回滚机制，但要求 completion claim 与真实 current state 一致。

## 10. Ordinary runtime

### 10.1 local-only 默认路径

进入 `ORDINARY_RUNTIME` 后，普通 Fresh Context 默认只读取：

- Consumer stable Bootstrap / Current Authority；
- Consumer-local current discovery entry；
- 当前任务命中的 local semantic owner；
- 当前真正需要的 local Skill / capability；
- current Work / Evidence。

默认不读取：

- upstream repository；
- upstream latest；
- adoption / upgrade decision history；
- previous baseline diff；
- rejected candidates；
- upstream Roadmap / Issue / PR / project state；
- upgrade reasoning transcript。

### 10.2 upstream 新提交不改变 ordinary runtime

upstream 从 `B1` 变化到 `B2` 时，只表示未来存在新的 upgrade candidate。

在 Consumer 没有显式进入新的 adoption / upgrade flow 前：

```text
Consumer ordinary runtime @ local state L1
+ upstream moves B1 → B2
=
Consumer ordinary runtime remains L1
```

### 10.3 local discovery 问题不自动升级为 upstream dependency

如果 local discovery stale / missing / ambiguous，运行时应先按 Consumer-local discovery / fail-closed 规则回到 Consumer Current Authority。

这本身不是 upstream re-entry 条件。只有确认 Consumer-local 必要 reusable capability 实际缺失，并且 Consumer Authority 允许从 upstream 重新解析时，才进入显式 re-entry。

## 11. Upstream re-entry

### 11.1 允许的显式条件

ordinary runtime 只有在以下至少一个条件成立时才重新进入 upstream：

1. 明确启动新的 baseline adoption / upgrade；
2. Consumer-local 必要 reusable capability 经确认缺失，且 Consumer Authority 允许从 upstream 解析 / 采用；
3. 当前任务被明确声明为 `agentic-dev` experiment / validation；
4. Consumer Repository Authority 明确要求读取或比较 upstream；
5. 新 Consumer 正处于首次采用流程。

### 11.2 不构成 re-entry 的信号

以下情况单独存在时不允许自动读取 upstream 改变当前行为：

- upstream 有新 commit / tag / release；
- local metadata / Catalog stale；
- routing 出现歧义；
- Agent 不确定但 Consumer Current Authority 尚未读完；
- 某条 upstream rule 看起来“更新”或“最佳实践更强”；
- 为了完整性想同步全部 upstream 文档。

### 11.3 re-entry 不等于 adoption

即使允许读取 upstream，也必须重新经过：

```text
read / compare upstream
→ classify
→ per-item decision
→ local projection
→ verification
→ baseline advance
```

不能把“允许查看 upstream”解释成“允许覆盖 Consumer current state”。

## 12. 与其他 owner 的责任分界

### 12.1 Core Method / Principle

继续拥有软件开发阶段、WHAT / WHY 与 HOW 边界、Stage Return、Evidence principle、Human Escalation 等通用开发语义。

Consumer lifecycle 不创建新的 Product Development Stage。

### 12.2 Guide

`using-agentic-dev.md` 继续面向人和低频初始化 / 采用 / 升级场景解释“如何使用”。

长期 normative lifecycle 由本文拥有。后续可以把 Guide 中重复的规范正文缩为说明与指针，但 V3-03 本身不执行物理拆分。

### 12.3 Skill / V3-04

V3-04 判断哪些流程具有独立 Skill 身份以及现有 Skill / Guide / Discipline 的重叠。

本文不因为 adoption 是一个过程就自动创建 `adoption-skill`、`upgrade-skill` 或 Super Skill。

### 12.4 Structured Resource Model / V3-05

V3-05 决定 evaluated baseline、provenance、decision history、current asset 等长期状态需要哪些结构化 representation / metadata。

本文只定义必须表达的语义，不冻结字段名、文件格式或目录。

### 12.5 Discovery Architecture / V3-06

V3-06 拥有 ordinary runtime 的 resource discovery、routing、source currentness、derived Catalog / Index 与 fail-closed discovery behavior。

本文只拥有：ordinary runtime 必须 local-only，以及何时允许 upstream re-entry。

### 12.6 Consumer Validation / V3-08

V3-08 在真实 Consumer 中验证本生命周期与其他 owner 的组合行为，包括初始化、upgrade、local-only runtime、override、re-entry 与 failure behavior。

V3-08 的 acceptance checklist 是验证输入，不成为本文的第二规则 owner。

## 13. v2 transitional-current 资源的后续 disposition

V3-03 集成后，以下长期关系成立；物理处理仍需相应后续 Gate：

- `docs/project/consumer-local-baseline-adoption-projection-v2.md`：其 durable adoption / baseline lifecycle 被本文取代；原文件可转为历史设计 / Evidence 候选；
- `docs/guides/using-agentic-dev.md`：保留 Guide 主身份；其中重复 lifecycle normative body 后续缩为本文指针；
- `docs/guides/consumer-local-rule-activation.md` §10～11：baseline state / local projection 的生命周期语义由本文拥有；具体 discovery representation 等待 V3-05 / V3-06；
- 同文件 §13：adoption verification responsibility 由本文拥有；具体 runtime/discovery checks 仍归原 semantic owner，派生 checklist 作为 V3-08 输入；
- `docs/project/consumer-local-rule-runtime-target-v2.md`：其中 local-only ordinary-runtime invariant 由本文承接；discovery / routing 目标由 V3-06 承接。

在本文通过 Gate 并正式集成前，上述 v2 / Guide 入口继续保持现行兼容，不提前删除或失效。

## 14. 代表性场景

V3-03 的语义至少必须能一致解释以下场景：

| 场景 | 正确生命周期结果 |
|---|---|
| 新 Consumer 有明确原始需求 | 建立最小 Consumer Authority，按明确授权形成需求身份，再选择性首次采用 reusable capability |
| 新 Consumer 没有原始需求 | 不制造空 Requirement；先建立最小治理骨架，后续按真实工作形成项目 Authority |
| Existing Consumer 发现 upstream 新 baseline | ordinary runtime 不变；只有显式 upgrade 才进入比较 |
| upstream 新规则与 local override 冲突 | 可 `retain / override`；推进 evaluated baseline 不伪造该 asset 的 provenance |
| upstream 新 Skill 当前 Consumer 不使用 | `reject / not applicable`，不进入 active runtime |
| upgrade 中途失败 | evaluated baseline 不推进；不得声明 upgrade complete；旧 current owner 不自动失效 |
| local discovery stale | 先 fail-closed 到 Consumer Current Authority，不自动在线读取 upstream |
| Consumer 明确缺少必要 reusable capability | 经 Consumer Authority 允许后显式 re-entry，再走 adoption flow |
| upstream 在 ordinary runtime 中继续提交 | 不改变 Consumer local current behavior |

## 15. V3-03 Gate

V3-03 只有在以下条件满足后才可以声明完成：

- 初始化、首次采用、baseline upgrade、local projection、adoption verification、baseline advance、ordinary runtime 和 upstream re-entry 构成单一一致生命周期；
- evaluated baseline、active asset provenance 与 upgrade-only decision history 职责分离；
- `adopt / retain-or-override / reject-not-applicable / supersede-remove` 语义稳定；
- partial / failed upgrade 不会制造假的完成状态或隐式覆盖；
- ordinary runtime local-only invariant 与显式 re-entry 条件清晰；
- 与 Method、Guide、Skill、V3-05、V3-06、V3-08 的 owner 边界明确；
- v1 / v2 已验证的 Consumer-local-first、逐项采用、local override、provenance separation、progressive disclosure 与 fail-closed 成果未被破坏；
- 高影响 lifecycle ambiguity 经与风险相称的 AI 复核后不存在未解决的 Blocking / Medium finding。

达到 Gate 后，只进入“是否启动 V3-04”的规划判断；本文不授权物理 Guide 迁移、Skill 重构、metadata / discovery 实现或 Consumer 修改。
