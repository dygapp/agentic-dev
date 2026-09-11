# V3-07 — agentic-dev 自采用与发现机制切换

**状态：** candidate validation PASS / cutover pending  
**跟踪：** Issue #113  
**启动基线：** `master@5ae0e144d30c6010fadf8e3beff3c12ce4b7a147`

## 1. 目的

本文记录 `agentic-dev` 对已经集成的使用方生命周期、资源模型与资源发现架构的**自采用结果、候选验证、replacement 与切换证据**。

本文是项目级实施 / 证据记录，不重新定义使用方生命周期、资源身份、资源发现语义、Method / Skill Contract 或 Consumer 项目事实。

长期规范 owner 保持在：

- `docs/architecture/consumer-lifecycle.md`；
- `docs/architecture/agent-resource-model.md`；
- `docs/architecture/resource-discovery-architecture.md`。

## 2. 当前 self-runtime surface

基于 V3-06 集成后的 `master` 恢复，当前普通 Fresh Context 的实际入口为：

```text
AGENTS.md
→ README.md
→ docs/project/project-roadmap.md
→ 当前 Issue / 项目 Authority
→ docs/guides/rule-activation-guide.md 的手工职责 / 风险导航
→ 按需 Guide / Skill / Engineering Capability / Repository-local Rule
```

其中：

- `AGENTS.md` 持有稳定 Repository Governance / Authority Boundary；
- README / Roadmap 持有当前项目恢复入口；
- `rule-activation-guide.md` 仍维护手工“职责 / 风险 → 来源”表；
- `consumer-local-rule-activation.md` 仍保留 v2 ordinary runtime 的 Manifest / Catalog、routing、Stage Return、fail-closed 等说明；
- `skills/README.md` 是当前 Skill inventory；
- `docs/architecture/engineering-disciplines.md` 单点持有当前 3 个工程纪律；
- `docs/technology-profiles/README.md` 是当前技术画像 inventory；
- `docs/guides/verification-evidence-rules.md` 持有跨职责验证规则族；
- `docs/guides/external-operation-guidelines.md` 持有仓库外部操作治理；
- v2 metadata / routing project contracts 仍承担过渡兼容 / 历史设计解释。

当前仓库**不存在实际版本化的 Activation Manifest / Runtime Catalog 文件**。因此自采用不能把逻辑契约误当作已存在运行资产，也不能为了迁移形式完整性创建空容器。

## 3. 是否需要 Reviewed Discovery Map

结论：**需要一个小型 Reviewed Discovery Map。**

依据：

1. `rule-activation-guide.md` 已经长期维护跨资源职责 / 风险导航，证明这类正规化不是假想需求；
2. 当前有 9 个 Skill、3 个工程纪律、技术画像、跨职责验证规则和外部操作规则；
3. 多个资源按条件横切执行 / 收敛 / 平台 / 外部操作职责；
4. V3-02 已确认 Guide catch-all 与派生路由不应继续成为长期语义 owner；
5. 如果不提取 Map，V3-06 的长期发现语义虽已建立，运行层仍会继续依赖 Guide 中的第二份手工路由表。

Map 的目标不是提高“智能程度”，而是把已经存在的跨资源派生判断从 Guide 中独立出来，并给它 source binding / coverage lifecycle。

## 4. 是否需要 Runtime View / Catalog

结论：**当前不需要。**

原因：

- 状态恢复可以在 Local Discovery Entry 层结束，不加载 Map；
- 需要跨资源发现时只读取一个 Map，不加载所有 Skill / owner；
- routing-only 只返回 locator，不读取完整 Skill；
- execute 才加载一个主 Skill 与真实命中的最小 supporting context；
- 当前没有证据证明第二个 compact Runtime View 能进一步带来足以抵消生成、currentness 与分发成本的收益。

因此 V3-07 不建立 Runtime Catalog、generator、Manifest 或其他第二运行投影。

## 5. Candidate discovery mechanism

候选机制由两项构成：

1. `docs/discovery/README.md` — Local Discovery Entry；
2. `docs/discovery/reviewed-discovery-map.md` — Reviewed Discovery Map。

Local Discovery Entry 只负责稳定入口、Map 指针、routing-only / execute 加载边界和失败关闭路径；Map 只保存 locator、跨资源派生提示、coverage / source binding 与真实 owner 指针。

两者都不拥有规范正文，不保存 Issue / PR / Actions 状态，不创建第二 `active/current` 真值。

## 6. Coverage 与 binding 结果

候选 Map 已区分：

- **membership-reviewed**：Skill / Technology Profile 等 inventory 只校验成员集合；普通说明文字变化不机械使整个范围 stale；
- **semantic-reviewed**：工程纪律、GitHub Actions Skill、技术画像正文、生命周期、验证 / 外部操作、术语、提交、AI 复核等被提炼触发语义的 source 绑定当前 identity；
- **current-locator**：AGENTS / README / Roadmap 与稳定架构 locator 只验证 path / authority role / owner currentness。

已确认 coverage anchors 能覆盖当前仓库普通运行需要跨资源发现的主要资源家族，同时不把 current project state 放入派生 Map。

## 7. Candidate validation 中发现并修复的问题

### M1 — membership 与 semantic source binding 混淆

初版把 `skills/README.md`、技术画像 inventory 的整个文件 identity 当作 coverage currentness。这样 inventory 的普通说明修改也会让 Map 全范围 stale，同时 `github-actions-verification` 自身语义变化反而可能漏检。

修复：

- inventory 改为 membership-reviewed；
- GitHub Actions Skill、Vue 画像正文等实际派生语义 source 单独 semantic-reviewed；
- source identity 变化后先判断语义影响，不允许只刷新 identity。

### M2 — 外部操作过度激活

初版把普通只读 GitHub / Repository 状态恢复也纳入 `external-state-write`，会让 Fresh Context 状态检查机械加载完整外部操作 Guide。

修复：

- 改为 `external-state-mutation`；
- 只有写入、副作用、授权或其他具体外部风险命中时才加载详细规则；
- 纯只读 current-state recovery 不因为“使用了 GitHub”自动扩上下文。

### M3 — Map 重复发现架构算法

初版 Map 尾部再次列出完整 primary / supporting / routing / Stage Return / fail-closed 算法，存在第二发现架构 owner 风险。

修复：

- Map 只保留 candidate discovery 必要使用边界；
- 完整发现语义统一指向 `docs/architecture/resource-discovery-architecture.md`。

修复后未发现新的未解决 Blocking / Medium。

## 8. Candidate 验证矩阵

本轮基于候选 Local Discovery Entry / Map 和当前真实 source，逐项执行 Fresh Context / routing 语义验证。

| 场景 | 实际解析 | 结果 |
|---|---|---|
| Fresh Context / Current Work | `AGENTS.md → README.md → Roadmap → GitHub current state`；状态恢复可在入口层停止，不要求读取 Map | PASS |
| routing-only | Map 只返回 primary responsibility / source locator；明确禁止仅因 locator 命中加载完整 Skill | PASS |
| 核心职责 execute | primary 例如 `execute-unit` 时只加载 `skills/execute-unit/SKILL.md` + 当前必需 Authority / supporting context | PASS |
| GitHub Actions | 只有 completion evidence / trigger / gate / artifact / log / timeout / observability 等真实条件命中时加入 `github-actions-verification`；source 直接 semantic-reviewed | PASS |
| 工程纪律 | 三个 Discipline 作为 supporting constraints 按事实命中，不夺取 primary responsibility | PASS |
| Vue 3 + TypeScript | 当前任务真实涉及 Vue 3 / TypeScript 且画像会影响正确实施时发现 `vue3-typescript.md`；membership + semantic binding 均可验证 | PASS |
| 验证规则 | verification currentness / visual / human-review baseline / database migration / evidence reuse / completion claim 可按稳定 section 独立发现 | PASS |
| 外部操作 | external mutation / media / async / shared-resource / artifact-promotion / dependent-PR topology 可按条件发现；只读状态恢复不机械加载 | PASS |
| Stage Return | 具体失效语义仍由 Method / Skill Contract owner 决定；一旦返回，Local Entry 按 V3-06 丢弃旧 decision 并重新发现 | PASS |
| stale source | semantic-reviewed identity 不匹配时相关提示退出可信范围，不能只刷新 hash | PASS |
| coverage drift | Skill / Profile membership 变化时相关范围先 stale；未复核前 no-match 不能证明无适用资源 | PASS |
| missing selector | 回到本地 current Authority / semantic owner，不按近似路径猜测 | PASS |
| ambiguity | 无法可靠区分 primary 时停止高影响动作并本地 fail-closed | PASS |
| no-match + governance fact | 明确禁止解释为“无规则”，回到本地 Authority 扩大最小读取 | PASS |
| ordinary runtime | 所有回退和 currentness 检查均使用本仓库本地 source；不访问 upstream、不依赖历史聊天或个人记忆 | PASS |

**Candidate validation：PASS。**

## 9. Context-cost 结论

候选机制没有要求普通 Fresh Context 总是加载完整 Map：

```text
只恢复状态 / Gate
→ Local Discovery Entry 层停止

需要跨资源 routing
→ 读取 Map
→ 不加载完整 Skill

真正执行职责
→ Map + 一个 primary Skill
+ 当前真实命中的最小 supporting context
```

因此当前不增加 Runtime View。后续如果真实使用证明 Map 自身成为显著固定成本，再以新的证据评估 compact projection，而不是提前建立第二层。

## 10. V2 资产迁移 disposition

| 当前资产 | V3-07 disposition |
|---|---|
| `rule-activation-guide.md` | cutover 时降为人类初始化 / 采用 / 兼容说明；移除手工职责 / 风险路由表的 current 身份 |
| `consumer-local-rule-activation.md` | 保留 Consumer-local 使用说明；ordinary discovery / routing / Manifest-Catalog 规范正文改为指向 V3-05 / V3-06，不再作为第二 owner |
| `consumer-local-activation-metadata-contract-v2.md` | 降为 v2 历史设计 / 验证证据；长期资源模型 / 发现语义由 V3-05 / V3-06 取代 |
| `consumer-local-runtime-routing-interface-v2.md` | 降为 v2 历史 routing contract / evidence；长期 routing 语义由 V3-06 取代 |
| Activation Manifest / Runtime Catalog | 当前仓库不存在物理 current 文件，不新建、不删除；只处理文档中的过渡描述 |
| 手工职责 / 风险表 | 已在 candidate Map 中重建为有 coverage / source binding 的派生映射 |

## 11. Cutover 原则

下一拟集成状态必须保证：

```text
candidate assets + validation PASS
→ 新 Local Discovery Entry / Reviewed Discovery Map 标为 current
→ 同一 PR 把旧 v2 手工 current discovery surface 降级
→ AGENTS / README / Roadmap / Guide 稳定指针切换
→ v2 project contracts 明确 historical / compatibility 身份
→ post-cutover Fresh Context 再验证
```

PR 分支中 candidate 与 master current 机制可以并存用于验证；**集成后的 master 不允许两个机制同时 current**。

## 12. 当前 Gate

Candidate validation 已通过，未解决 Blocking / Medium = 0。

下一实际步骤：执行同一 PR 内的原子 cutover 修订；修订后重新建立精确 Head 证据、执行 post-cutover 验证与高影响 AI 复核。