# Consumer-local Baseline Adoption / Projection 契约 v2

## 状态

**Phase E 结果 — Baseline Adoption / Consumer-local Projection**

上层输入：

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`
- `docs/project/rule-ownership-decomposition-audit-v2.md`
- `docs/project/consumer-local-activation-metadata-contract-v2.md`
- `docs/project/consumer-local-runtime-routing-interface-v2.md`
- `docs/guides/using-agentic-dev.md` §6.1

本文冻结 upstream capability 如何经过显式采用，形成 Consumer-local current assets。它不规定固定目录、包管理器、安装器或配置格式。

## 1. 核心目标

Baseline adoption 不是“把 upstream 更新到最新版”，而是：

```text
Current Consumer Authority
+ previous evaluated upstream baseline
+ candidate upstream baseline
        ↓
识别 reusable delta
        ↓
逐项 adopt / retain-or-override / reject-not-applicable / supersede
        ↓
形成 Consumer-local semantic owners / capabilities / discovery metadata
        ↓
验证
        ↓
ordinary runtime 再次只依赖 Consumer-local state
```

任何 baseline pointer 都不能替代逐项 adoption decision。

## 2. 三类本地状态必须分离

### 2.1 Upstream Evaluation State

只回答：

> Consumer 最近显式比较、评估到哪个 exact upstream baseline？

至少包含：

- upstream repository identity；
- exact evaluated commit / tag；
- previous evaluated baseline；
- evaluation date / current local change reference（按 Consumer 需要）。

这个状态**不表示该 baseline 的全部规则都已采用**。

### 2.2 Active Consumer-local Capability State

ordinary runtime 真正消费的当前状态，包括：

- Consumer-native semantic owners；
- adopted reusable rule / module；
- locally available Skill / Engineering Discipline / Technology Profile；
- Activation Manifest / Runtime Catalog active records；
- Consumer-specific override / supersede 关系。

每个 adopted active asset 保留自己的 `adopted_from` provenance。它可能早于当前 evaluated upstream baseline。

### 2.3 Adoption Decision History

只在显式 baseline adoption / upgrade 时读取，用于回答：

- 某个 upstream change 是否曾被评估；
- 当时是 adopt、retain / override、reject / not applicable 还是 supersede；
- 为什么当前 local asset 没有随 upstream 一起变化；
- 后续是否因为 Consumer 条件变化需要重新评估。

它不是 ordinary runtime Authority，也不进入普通 Fresh Context 默认加载集合。

Consumer 可以把这三类状态放在一个或多个现有文件中；v2 只要求职责分离，不要求固定物理文件。

## 3. 为什么不能只有一个 baseline 指针

假设：

```text
B0 → B1
```

B1 同时包含：

- 一个 Consumer 需要的新 reusable rule；
- 一个 Consumer 已有更具体 override 的修改；
- 一个 Consumer 不使用的平台 Skill；
- 一个 `agentic-dev` project-only 状态变化。

Consumer 可以合法地：

```text
rule A → adopt
rule B → retain local override
skill C → not applicable
project state D → exclude
```

此时 Consumer 可以把“last evaluated upstream baseline”推进到 B1，但不能声称本地所有 active asset 都来自 B1。

因此：

- evaluated baseline 是**比较边界**；
- `adopted_from` 是**单个本地资产来源**；
- runtime currentness 由 Consumer-local source identity 决定；
- 三者不能互相替代。

## 4. Upgrade 输入

一次显式 baseline upgrade 至少读取：

- Consumer Current Repository Authority；
- Consumer current local discovery / capability state；
- previous evaluated upstream baseline；
- candidate exact upstream baseline；
- 两个 baseline 之间的实际 diff；
- previously retained / overridden / rejected decisions；
- Consumer 当前技术栈、平台、验证方式和项目约束中与变化相关的最小事实。

ordinary work 不需要读取这些 upgrade-only 输入。

## 5. Upstream Delta 分类

先按 owner / capability layer 分类，避免把 upstream 项目状态当成可复用变化。

至少区分：

```text
method / principle
skill / skill contract
engineering discipline
technology / verification profile
reusable guide rule
runtime adapter / platform capability
agentic-dev project-only
research / eval / historical evidence
```

默认：

- `agentic-dev project-only` 不进入 Consumer adoption；
- Research / Eval / historical evidence 只在它们支撑一个正式 reusable change 时作为证据读取，不直接投射到 Consumer runtime；
- upstream Roadmap、Issue / PR 状态、当前里程碑和仓库提交风格不自动成为 Consumer 项目规则。

## 6. 单项 Adoption Decision

每个可能影响 Consumer 的 reusable delta 必须形成一个明确决策。

### 6.1 `adopt`

适用：

- Consumer 确实需要该变化；
- 与 Consumer Current Authority 不冲突；
- 对后续工作具有持续约束或能力价值。

结果：

- 创建或更新 Consumer-local semantic owner / capability；
- 更新 local Manifest / Catalog active record；
- 保存 exact `adopted_from` provenance；
- 验证 local source currentness 与 runtime discoverability。

### 6.2 `retain / override`

适用：

- Consumer 已有更具体、合法的 local Authority；
- upstream 新 default 不应覆盖当前项目特化；
- 或 Consumer 选择继续保留已采用的旧 local behavior。

结果：

- Consumer current owner 不变；
- 必要时记录 `overrides` / retain relation；
- 记录本轮已评估 candidate baseline；
- 不伪造 `adopted_from = candidate baseline`；
- ordinary runtime 继续只发现 local current owner。

### 6.3 `reject / not applicable`

适用：

- 当前 Consumer 不使用对应平台 / 技术 /职责；
- 规则只属于 upstream 自己；
- 没有持续协调价值；
- 或 Consumer Authority 明确不采用。

结果：

- 只保留 upgrade decision history；
- 不创建 active runtime record；
- 不复制规则正文；
- 不为了 Catalog 完整而制造 disabled 占位资产。

### 6.4 `supersede / remove`

适用：

- 当前 local adopted asset 被新的显式决定取代；
- upstream change 与 Consumer 决定共同确认旧本地语义不再 current。

结果：

- 新 current owner 可发现；
- 旧 active record 从普通 runtime 集合移除或明确 superseded；
- 历史 provenance 可以保留；
- 不允许新旧正文同时作为 current owner。

## 7. Projection Target

`adopt` 的结果必须投射到 Consumer-local、ordinary runtime 可取得的对象，而不是只写入 upgrade report。

可能的 target：

### 7.1 Consumer-native / adopted local rule owner

适合：

- repository governance；
- consumer adoption / bootstrap rule；
- reusable Guide Rule Module；
- Consumer-specific override。

可以进入 Consumer 已有的 AGENTS / local method / guide / policy / module 等合适载体，但应遵守入口职责：**不要把易变化 baseline 历史、项目状态或大量条件规则继续堆入最高优先级 Bootstrap。**

### 7.2 Local Skill / capability installation

适合：

- 核心 Skill；
- platform-specific Skill；
- Technology / Verification Profile；
- 其他需要完整可执行内容的 reusable capability。

要求：

- Consumer ordinary runtime 能从本地解析；
- exact source / version 可追溯；
- 不依赖当前 upstream 在线内容；
- current / superseded identity 明确。

v2 不规定复制目录、Git submodule、package、Plugin 或其他具体交付方式。

### 7.3 Discovery metadata

所有需要 ordinary runtime 发现的 current asset 才进入 active Manifest / Catalog。

Metadata 只保存发现信息；adoption decision history 不应因为“可追溯”而全部进入 Catalog。

## 8. Existing Local Owner 优先复用

Baseline upgrade 不能因为 upstream 出现新 rule 就机械创建新文件。

如果 Consumer 已有一个 semantic owner 可以正确承载 adopted change：

```text
upstream reusable delta
→ update existing Consumer-local owner
→ update discovery metadata if needed
```

优于：

```text
existing local rule
+ copied upstream rule
+ catalog summary
```

同时维护三份正文。

例如 Consumer 已在 local Development Method 中拥有等价方法语义时，可以更新该 owner，而不是额外 vendor 整份 upstream Guide。

## 9. Previously Rejected / Retained Change 的后续处理

把 evaluated baseline 从 B0 推进到 B1 后，下一次 B1 → B2 比较不会自动再次显示 B0 → B1 中被拒绝或保留的变化。

因此 upgrade-only decision history 必须支持在以下条件重新评估旧决定：

- Consumer 技术栈 / 平台变化；
- 原先 not-applicable 的 capability 变为 applicable；
- Consumer local override 被删除或发生重大变化；
- upstream 后续变化实质修改同一 semantic owner；
- 当前 Consumer 真实使用证据表明旧决定不再成立。

这不要求 ordinary runtime 加载完整历史，只要求 baseline upgrade 能识别相关旧 decision。

## 10. Baseline Advance Gate

只有以下条件满足后，才能把 candidate baseline 记录为新的 **evaluated upstream baseline**：

1. candidate exact commit 已确认；
2. reusable / project-only / research / eval delta 已分类；
3. 对当前 Consumer 相关 delta 已逐项做 adoption decision；
4. adopted / retained local owners 已完成必要修改；
5. rejected / not-applicable 不进入 active runtime；
6. superseded old asset 不再参与 Current routing；
7. active Manifest / Catalog 与 local source identity 一致；
8. 当前 Consumer Authority precedence 没有被 upstream 覆盖；
9. 必要静态 /行为验证完成；
10. baseline advance 不被描述成“全部 upstream 规则已采用”。

任一关键项未完成时，保持 previous evaluated baseline，或明确记录 upgrade 尚未完成；不得只更新 baseline 字符串制造完成状态。

## 11. Ordinary Runtime Boundary

Upgrade 完成后，普通 Fresh Context 只读取：

- Consumer Bootstrap / Current Authority；
- local Manifest / Catalog；
- selected local semantic owners；
- selected local Skill / capability；
- current Work / Evidence。

不默认读取：

- upstream repository；
- adoption decision history；
- previous baseline diff；
- rejected candidate；
- upstream Roadmap / Issue / PR；
- upgrade reasoning transcript。

这使 adoption 的复杂度停留在显式升级时，而不是永久转化成每个开发任务的上下文成本。

## 12. 与真实 Consumer 当前模式的关系

`dygapp/jilinjobs-cms` 已经验证了若干正确方向：

- ordinary development 优先 Consumer-local Method；
- exact upstream baseline 被记录；
- reusable 与 `agentic-dev` project-only 被区分；
- 部分 upstream change 会被选择性固化；
- Consumer-specific override 优先。

v2 不要求推翻这些实践，而是补足两个结构化边界：

1. **baseline history / adoption decision 不应持续堆入普通 Bootstrap / Fresh Context；**
2. **last evaluated baseline 与 active asset 的 `adopted_from` 必须分离。**

真实 Consumer Phase F 可以在不改变产品路线的前提下验证这种收敛是否降低恢复成本并保持现有语义。

## 13. Phase E 静态验收

进入 Phase F 前，设计必须能回答：

- exact baseline 如何追溯；
- partial adoption 如何表示；
- local override 如何保留；
- reject / not-applicable 为什么不会进入 runtime；
- active asset 实际来自哪个 baseline；
- previously rejected change 何时重新评估；
- superseded asset 如何退出 current routing；
- upgrade 完成后 ordinary runtime 为什么不需要 upstream 或 adoption history；
- Consumer AGENTS / Bootstrap 为什么不会因为多轮 baseline upgrade 无限增长。

## 14. Phase E 完成结论

当前最小 Adoption / Projection 模型为：

```text
Explicit Baseline Upgrade
        ↓
Exact Upstream Diff
        ↓
Reusable Delta Classification
        ↓
Per-item Adoption Decision
        ↓
Consumer-local Semantic Owner / Capability
        ↓
Active Manifest / Catalog
        ↓
Validation
        ↓
Advance evaluated baseline
        ↓
ordinary runtime returns local-only
```

Phase E 不需要新的通用安装器或分发平台即可成立。

下一阶段必须在真实 Consumer 中验证：

> 这种职责分离是否真的能在不访问 upstream 的 Fresh Context 中保持正确发现、Consumer override、Stage Return、Skill activation、baseline lifecycle 与可维护性。

这属于 Phase F — 真实 Consumer 验证。