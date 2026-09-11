# V3-07 — agentic-dev 自采用与发现机制切换

**状态：** 自采用结果 v0.1  
**跟踪：** Issue #113  
**启动基线：** `master@5ae0e144d30c6010fadf8e3beff3c12ce4b7a147`

## 1. 目的与权威边界

本文记录 `agentic-dev` 对已经集成的使用方生命周期、资源模型与资源发现架构的**自采用、候选验证、replacement 与切换证据**。

本文是项目级实施 / 证据记录，不重新定义使用方生命周期、资源身份、资源发现语义、Method / Skill Contract 或 Consumer 项目事实。

长期规范 owner 保持在：

- `docs/architecture/consumer-lifecycle.md`；
- `docs/architecture/agent-resource-model.md`；
- `docs/architecture/resource-discovery-architecture.md`。

V3-07 的精确审查、集成与完成状态以 Issue #113 与 GitHub 当前状态为准；本文不复制瞬时 PR 状态。

## 2. 自采用前的真实 self-runtime surface

基于 V3-06 集成基线恢复，自采用前普通 Fresh Context 的实际入口为：

```text
AGENTS.md
→ README.md
→ docs/project/project-roadmap.md
→ 当前 GitHub / Issue / Project Authority
→ docs/guides/rule-activation-guide.md 的手工职责 / 风险导航
→ 按需 Guide / Skill / Engineering Capability / Repository-local Rule
```

当前仓库**不存在实际版本化的 Activation Manifest / Runtime Catalog 文件**。v2 对 Manifest / Catalog 的描述属于逻辑契约 / 历史设计，不是本仓库实际物理运行资产，因此 V3-07 没有为了迁移形式完整性创建空容器。

## 3. Map / Runtime View 必要性裁决

### 3.1 Reviewed Discovery Map：需要

依据：

1. 旧 `rule-activation-guide.md` 已长期维护跨资源职责 / 风险 → source 的手工映射，证明跨资源正规化是当前真实需求；
2. 当前仓库有 9 个 Skill、3 个工程纪律、技术画像、跨职责验证规则、外部操作规则、使用方生命周期和仓库本地治理；
3. 多个资源按条件横切执行 / 收敛 / 平台 / 外部操作职责；
4. V3-02 已明确 Guide catch-all、手工 routing 与真实 semantic owner 的重复风险；
5. 如果不提取 Map，V3-06 虽已成为长期发现架构，普通运行仍会依赖 Guide 中的第二份路由表。

因此建立一个小型、非规范性、需复核维护的 Reviewed Discovery Map。

### 3.2 Runtime View / Catalog：当前不需要

当前机制允许：

```text
只恢复状态 / Gate
→ AGENTS + README + Roadmap + GitHub state 后停止

需要跨资源 routing
→ Local Discovery Entry + Reviewed Discovery Map
→ 不加载完整 Skill

真正执行职责
→ 一个 primary Skill
+ 当前真实命中的最小 supporting context
```

没有当前证据证明第二个 compact Runtime View 能带来足以抵消生成、currentness 与分发成本的收益，因此 V3-07 不建立 Runtime Catalog、generator、Manifest 或第二运行投影。

## 4. 自采用后的 current discovery mechanism

`agentic-dev` 自身 ordinary runtime 采用：

```text
AGENTS.md / README.md / Roadmap / GitHub current state
        ↓ 当前任务需要跨资源发现时
`docs/discovery/README.md`
        ↓ 按需
`docs/discovery/reviewed-discovery-map.md`
        ↓
current semantic owner / primary Skill
```

### 4.1 Local Discovery Entry

`docs/discovery/README.md` 只负责：

- 稳定本地入口；
- 状态恢复何时可以停止；
- Map 指针；
- routing-only / execute 加载边界；
- stale / missing / coverage drift / ambiguity 的本地失败关闭路径。

它不定义 Method Stage、Skill Procedure 或完整职责表。

### 4.2 Reviewed Discovery Map

`docs/discovery/reviewed-discovery-map.md` 只保存：

- stable locator / selector；
- 跨资源派生职责 / 条件 / 风险提示；
- membership / semantic / locator binding；
- coverage scope；
- source owner 指针。

Map 不进入 Repository Authority 顺序，不拥有规范正文，不维护第二 `active/current` 真值，也不持久化当前 Issue / PR / Actions 状态。

## 5. Coverage 与 currentness

Map 区分：

- **membership-reviewed**：Skill / Technology Profile 等 inventory 只校验成员集合；
- **semantic-reviewed**：被提炼职责 / 条件 / 风险提示的 source 绑定当前 source identity；
- **current-locator**：AGENTS / README / Roadmap / 稳定 Architecture entry 只验证 path / authority role / owner currentness。

当前 coverage 包括：

- 9 个 Skill inventory；
- GitHub Actions 平台 Skill 的派生触发语义；
- 3 个 Engineering Discipline；
- Vue 3 + TypeScript Technology Profile；
- Consumer Lifecycle；
- Verification / Evidence rule units；
- External-operation rule units；
- `agentic-dev` 自身术语、Git 提交和高影响 AI 复核治理；
- 资源 / Skill / 技术画像等稳定 Architecture locator。

Current Project / Requirement / Issue / PR / Actions 不进入 Map，始终从真实本地 source 恢复。

## 6. Candidate validation 中发现并修复的问题

### M1 — membership 与 semantic source binding 混淆

初版把 inventory 文件整体 identity 当成 coverage currentness，而实际派生语义 source 又没有全部独立绑定。

修复：inventory 改为 membership-reviewed；GitHub Actions Skill、Vue 画像正文、工程纪律、验证 / 外部操作等被提炼语义的 source 使用 semantic-reviewed binding。

### M2 — 外部操作过度激活

初版把纯只读 GitHub / Repository 状态恢复也纳入外部写操作规则，导致 Fresh Context 机械扩上下文。

修复：只有 mutation、副作用、授权或具体外部风险真实命中时才加载详细外部操作 owner；普通只读 current-state recovery 不因此加载完整 Guide。

### M3 — Map 重复发现架构算法

初版 Map 再次列出完整 primary / supporting / routing / Stage Return / fail-closed 算法。

修复：Map 只保留 candidate discovery 必要边界，完整发现语义统一由 `docs/architecture/resource-discovery-architecture.md` 持有。

### M4 — `using-agentic-dev.md` 仍保留普通职责 routing 表

Post-cutover 唯一性检查发现 `using-agentic-dev.md` 仍有“常规功能工作的职责路由”表。V3-02 已明确其 disposition 是 Guide routing reduce / supersede；若继续保留，会形成与 Map / Skill inventory 的平行手工映射。

修复：`using-agentic-dev.md` 只保留人类 + 初始化 / 采用 / 升级说明；ordinary routing 指向 `resource-discovery-architecture.md` 和各仓库自己的 Local Discovery Entry，不再维护第二职责表。

上述修复后，未发现新的未解决 Blocking / Medium。

## 7. Candidate validation

| 场景 | 验证结果 |
|---|---|
| Fresh Context / Current Work | PASS — 状态恢复可在 AGENTS / README / Roadmap / GitHub current state 后停止，不要求读取 Map |
| routing-only | PASS — 返回主职责 / source locator，不因 locator 命中加载完整 Skill |
| 核心职责 execute | PASS — 加载一个 primary Skill + 当前真实必要 supporting context |
| GitHub Actions | PASS — 真实平台条件命中才按需进入专项 Skill |
| Engineering Discipline | PASS — supporting constraint 按事实命中，不夺取 primary responsibility |
| Vue 3 + TypeScript | PASS — membership + profile semantic binding 均可验证 |
| Verification rules | PASS — currentness / visual / human-review baseline / migration / evidence reuse / completion claim 可按资源单元发现 |
| External operations | PASS — mutation / media / async / shared-resource / artifact-promotion / dependent-PR 按条件发现；只读恢复不机械激活 |
| Stage Return | PASS — 具体失效语义由 Method / Skill owner 持有；发现层丢弃旧 decision 并重新发现 |
| stale source | PASS — semantic-reviewed identity 不匹配时退出可信范围，不能只刷新 hash |
| coverage drift | PASS — membership 变化时相关范围先 stale，no-match 不证明无适用资源 |
| missing selector | PASS — 回到本地 current Authority / semantic owner，不猜近似 source |
| ambiguity | PASS — 无法可靠区分 primary 时停止高影响动作并本地失败关闭 |
| no-match + governance fact | PASS — 不解释为“无规则”，回到本地 Authority 扩大最小读取 |
| ordinary runtime | PASS — 不读取 upstream、历史聊天或个人记忆 |

## 8. 原子 cutover disposition

当前拟集成状态同时完成：

- `AGENTS.md`：`agentic-dev` 自身 ordinary runtime Local Discovery Entry 切换到 `docs/discovery/README.md`；Map 明确不进入 Authority 顺序；
- README：自采用状态、Local Entry / Map 与 Consumer 边界更新；
- Roadmap / v3 总规划：当前 Gate 切到 Issue #113；
- `rule-activation-guide.md`：降为低频初始化 / 采用 / 升级 / 实验导航，不再维护 ordinary runtime 手工职责表；
- `using-agentic-dev.md`：降为人类 + 初始化 / 采用 / 升级说明，不再维护 ordinary routing 表；
- `consumer-local-rule-activation.md`：保留 Consumer-local 落地说明，长期资源 / discovery / routing / Stage Return / fail-closed 规范统一指向 V3-03 / V3-05 / V3-06 owner；
- v2 metadata / routing project contracts：继续作为显式版本化的 Phase C/D 冻结历史设计 / Evidence 保存，不再被 current bootstrap / Guide 当作长期 discovery owner；
- 当前仓库不存在物理 Manifest / Runtime Catalog，因此不创建、不删除空容器。

该 disposition 使拟集成后的同一 self-runtime scope 只有：

```text
Local Discovery Entry + Reviewed Discovery Map
```

一个 current discovery mechanism。

## 9. Post-cutover validation

在拟集成分支上重新从稳定入口检查：

1. `AGENTS.md` 明确 self Local Discovery Entry，同时 Map 不属于 Authority；
2. README 与 Roadmap 均指向 V3-07 / Issue #113 和 `docs/discovery/README.md`；
3. `rule-activation-guide.md` 已无 ordinary responsibility / risk table；
4. `using-agentic-dev.md` 已无普通职责 routing table；
5. `consumer-local-rule-activation.md` 已无第二 Manifest / Catalog / routing / Stage Return 规范 owner；
6. Reviewed Map 的 semantic-reviewed source 均来自本 PR 未修改的 current owner，membership / locator 也可从真实本地 source 验证；
7. 状态恢复不要求 Map；只有跨资源发现时加载 Map；execute 才加载完整 primary Skill；
8. stale / missing / coverage drift / ambiguity / no-match 均回到本地当前权威；
9. `agentic-dev/docs/discovery/*` 明确不自动投射给 Consumer；
10. ordinary runtime 不访问 upstream。

**Post-cutover validation：PASS。**

## 10. Context-cost 结论

当前没有 Runtime View 的理由在 cutover 后仍成立：

- 状态恢复路径不加载 Map；
- routing-only 最多读取一个 Map，不加载全部 Skill；
- execute 只加载一个 primary Skill 和真正必要 supporting context；
- 新增 Runtime View 会引入另一套生成 / currentness / 分发责任，但当前没有可测量收益证据。

后续若真实 Consumer / self-runtime 证明 Map 自身成为显著固定成本，再以新的证据与门禁评估 compact projection。

## 11. 当前 Gate

V3-07 的 candidate validation 和 post-cutover validation 均已通过；当前未解决 Blocking / Medium = 0。

剩余门禁：

1. 对最终精确 PR Head 执行高影响 AI 复核；
2. 若复核发现 Blocking / Medium，先修复并重新验证；
3. AI 复核通过后进入集成；
4. 集成后核验 `master` 与 current mechanism 唯一性，并以完成原因关闭 Issue #113；
5. V3-08 只成为下一 Planning Candidate，不自动启动。