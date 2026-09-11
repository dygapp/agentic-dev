# V3-07 — agentic-dev 自采用与发现机制切换

**状态：** candidate validation  
**跟踪：** Issue #113  
**启动基线：** `master@5ae0e144d30c6010fadf8e3beff3c12ce4b7a147`

## 1. 目的

本文记录 `agentic-dev` 对已经集成的使用方生命周期、资源模型与资源发现架构的**自采用结果、候选验证、replacement 与切换证据**。

本文是项目级实施 / 证据记录，不重新定义：

- 使用方生命周期；
- 资源身份；
- 资源发现语义；
- Method / Skill Contract；
- Consumer 项目事实。

长期规范 owner 分别保持在：

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
- `rule-activation-guide.md` 当前仍维护手工“职责 / 风险 → 来源”表；
- `consumer-local-rule-activation.md` 当前仍保留 v2 ordinary runtime 的 Manifest / Catalog、routing、Stage Return、fail-closed 等说明；
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
5. 如果不提取 Reviewed Discovery Map，V3-06 的长期发现语义虽已建立，运行层仍会继续依赖 Guide 中的手工第二份路由表。

Map 的目标不是提高“智能程度”，而是把已经存在的跨资源派生判断从 Guide 中独立出来，并给它 source binding / coverage lifecycle。

## 4. 是否需要 Runtime View / Catalog

结论：**当前不需要。**

原因：

- 当前 Map 规模预计足够小，可被普通 Fresh Context 直接按需读取；
- 当前没有运行证据证明第二个 compact 视图能显著降低 token / wall-clock / IO；
- 引入 Runtime View 会额外产生生成 / currentness / 分发责任；
- V3-06 已明确 Runtime View 只是可选优化，不是发现语义的必要层。

因此 V3-07 不建立 Runtime Catalog、generator、Manifest 或其他第二运行投影。

## 5. Candidate discovery mechanism

候选机制由两项构成：

1. `docs/discovery/README.md` — Local Discovery Entry；
2. `docs/discovery/reviewed-discovery-map.md` — Reviewed Discovery Map。

### 5.1 Local Discovery Entry

只负责：

- 指向当前仓库权威 / 当前工作恢复入口；
- 指向 current Reviewed Discovery Map；
- 说明 routing-only / execute 的加载边界；
- 说明 stale / missing / coverage drift / ambiguity 的 fail-closed 入口。

不维护完整职责表、方法摘要或规则正文。

### 5.2 Reviewed Discovery Map

只保存：

- 稳定 resource / selector 引用；
- 跨资源职责 / 条件 / 风险提示；
- routing-only / execution 等加载提示；
- coverage anchors 与 source binding；
- 真实 owner 指针。

不保存：

- 规范正文；
- Requirement / Architecture / Rule 摘要；
- 第二 `active/current` 状态；
- Issue / PR / Actions 当前状态；
- expected answer；
- 数值优先级。

## 6. Coverage anchors

候选 Map 的主要覆盖边界由真实 owner / inventory 锚定：

| Coverage | Anchor | 当前用途 |
|---|---|---|
| 核心 / 平台 Skill membership | `skills/README.md` | 检测 Skill 新增、删除、重分类 |
| 工程纪律 membership / semantics | `docs/architecture/engineering-disciplines.md` | 3 个工程纪律及其触发语义 |
| 技术画像 membership | `docs/technology-profiles/README.md` | 检测画像新增、删除、替换 |
| 使用方生命周期 | `docs/architecture/consumer-lifecycle.md` | 初始化 / 采用 / 升级 / 重新进入上游 |
| 验证规则族 | `docs/guides/verification-evidence-rules.md` | 条件性验证 / 证据资源单元 |
| 外部操作规则族 | `docs/guides/external-operation-guidelines.md` | 外部写、异步、共享资源等条件资源 |
| 仓库语言 / 术语 | `docs/guides/terminology-guidelines.md` | `agentic-dev` 自身面向人的表达约束 |
| Git 提交规范 | `docs/guides/git-commit-guidelines.md` | 提交时按需读取 |
| 高影响 AI 复核 | `docs/project/ai-review-guidelines.md` | 高影响仓库变更时按需读取 |

README / Roadmap / 当前 Issue 属于 current-locator，不把其正文 hash 作为发现 Map 的语义 coverage anchor。

## 7. V2 资产迁移 disposition

| 当前资产 | V3-07 disposition |
|---|---|
| `rule-activation-guide.md` | candidate 验证通过并 cutover 时降为人类说明 / compatibility pointer；移除手工职责 / 风险路由表的 current 身份 |
| `consumer-local-rule-activation.md` | 保留 Consumer-local 使用说明；普通运行 discovery / routing / Manifest-Catalog 规范段改为指向 V3-05 / V3-06 长期架构，不再作为第二 owner |
| `consumer-local-activation-metadata-contract-v2.md` | 降为 v2 历史设计 / 验证证据；长期资源模型 / 发现语义由 V3-05 / V3-06 取代 |
| `consumer-local-runtime-routing-interface-v2.md` | 降为 v2 历史 routing contract / evidence；长期 routing 语义由 V3-06 取代 |
| Activation Manifest / Runtime Catalog | 当前仓库不存在物理 current 文件，不新建、不删除；只处理文档中的过渡描述 |
| 手工职责 / 风险表 | 迁移到 Reviewed Discovery Map，并纳入 coverage / source binding |

在 candidate 验证通过前，上述旧入口仍保持 current compatibility freeze。

## 8. Candidate 验证矩阵

| 场景 | 预期 | 当前状态 |
|---|---|---|
| Fresh Context / Current Work | 从 Local Discovery Entry 回到 AGENTS + README/Roadmap + current Issue，不复制项目状态 | PENDING |
| routing-only | 只返回主职责 / 指针，不加载完整 Skill | PENDING |
| 核心职责 execute | 只加载主 Skill + 真正必要辅助资源 | PENDING |
| GitHub Actions | 条件命中时按需加载平台 Skill，不夺取主职责 | PENDING |
| 工程纪律 | 只在当前责任真实需要时进入 supporting set | PENDING |
| Vue 3 + TypeScript | 条件命中时发现当前技术画像 | PENDING |
| 验证规则 | visual / migration / evidence reuse / completion claim 等按 section 发现 | PENDING |
| 外部操作 | write / async / shared-resource 等按条件发现 | PENDING |
| Stage Return | 丢弃旧 discovery decision 并重新发现 | PENDING |
| stale / missing / coverage drift / ambiguity | fail-closed 到本地当前权威 | PENDING |
| no-match + governance fact | 不解释为无规则 | PENDING |
| ordinary runtime | 不读取 upstream / 历史聊天 / 个人记忆 | PENDING |

验证通过前不得执行 current mechanism cutover。

## 9. Cutover 原则

最终拟集成变更必须保证：

```text
candidate assets + validation PASS
→ 新 Local Discovery Entry / Reviewed Discovery Map 成为 current
→ 同一提交 / PR 中把旧 v2 手工 current discovery surface 降级
→ Bootstrap / README / Roadmap 指向新入口
→ 再做 post-cutover Fresh Context 验证
```

PR 分支中 candidate 与 master current 机制可以并存用于验证；**集成后的 master 不允许两个机制同时 current**。

## 10. 当前 Gate

当前只完成了 self-runtime 恢复、Map / Runtime View 必要性裁决和 candidate 设计边界。

下一实际步骤：

1. 建立 candidate Local Discovery Entry；
2. 建立 Reviewed Discovery Map；
3. 执行 candidate validation；
4. 修复发现；
5. AI 复核；
6. 只有通过后才进行原子 cutover。