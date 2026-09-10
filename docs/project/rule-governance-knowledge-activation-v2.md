# 规则治理与知识激活 v2

## 状态

**有限里程碑内部完成定义已满足 — 已具备进入人工集成决策的条件**

人工决策日期：2026-09-10  
跟踪入口：Issue #92 / PR #93  
启动基线：`master@b6a20053a7a6f4f53915bea8218604720412c302`

长期阶段保持：

> **工程能力扩展与方法演进**

实际是否已集成 v2，以 Git / PR #93 当前事实为准；本文不复制瞬时 PR 状态。

## 1. 核心目标

v1 已证明最小规则激活、来源追溯和 fail-closed 的价值；v2 解决真实 Consumer 长期独立运行：

> 让 `agentic-dev` 的可复用方法 / 规则 / Skill 能被 Consumer 选择性采用并固化为 Consumer-local 可发现资产；完成 adoption 后，ordinary Consumer runtime 只依赖 Consumer Repository，不把 upstream 作为日常运行依赖。

Consumer 自己的 Repository Rules、Requirement / Specification、Domain / Architecture / ADR、Verification / Integration Rules 与 adopted reusable capability 必须能进入同一本地发现路径，同时始终保持 Consumer Repository Authority 优先。

## 2. 最高设计约束

### 2.1 Consumer-local-first

```text
Consumer-local Runtime Target
→ Discovery / Routing / Skill / Authority 机制
→ agentic-dev reusable capability / adoption model
```

Consumer 验证是最终完成门禁，不是附加实验。

### 2.2 单点 semantic owner

同一规范性规则只有一个长期正文 owner。Metadata、Catalog、导航只保存发现所需的最小信息和 source pointer，不复制规则正文，也不形成第二套 Authority。

### 2.3 Adoption 后脱离日常 upstream

只有显式 baseline upgrade、Consumer 本地确实缺少必要方法 / Skill、明确 `agentic-dev` 实验，或 Consumer Authority 要求时才重新读取 upstream。

### 2.4 最小机制优先

当前没有证据要求 Runtime Rule Index 服务、向量 / 图数据库、MCP 规则服务、全仓统一 Front Matter、Rule Super Skill、大量专项 Skill 或固定 Consumer 目录模板。

## 3. 最终运行模型

v2 收敛后的 ordinary Consumer 路径是：

```text
Fresh Consumer Task
→ Thin Consumer-local Bootstrap
→ Consumer-local Discovery Entry
→ Activation Manifest / optional Runtime Catalog
→ 最小 local Authority / rule-module
→ primary responsibility + supporting constraints
→ routing-only 或按需加载 Skill
→ Execute / Verify / Stage Return
```

关键边界：

- Catalog / Manifest 不拥有项目事实或规则正文；
- Consumer-native Authority 与 adopted reusable asset 可同路发现，但保留来源身份；
- 一个当前 primary responsibility + 最小 supporting set；
- routing-only 不机械加载完整 Skill；
- 真正进入稳定职责时才加载对应 Skill；
- Stage Return 后重新 routing；
- stale / missing / ambiguity / conflict / high-impact fail-closed 到 Consumer-local Current Authority；
- ordinary runtime 不访问 upstream。

## 4. Phase A～E 设计结果

### Phase A — Consumer-local Runtime Target / Acceptance

**已完成。**

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`

冻结 Consumer-local 独立运行目标与 CL-01～CL-12 验收矩阵。

### Phase B — Rule Ownership / Guide Decomposition

**已完成。**

- `docs/project/rule-ownership-decomposition-audit-v2.md`

Principle、核心 Skill、Engineering Discipline、Guide Rule Module、Platform capability 与 Consumer-native Authority 保持各自 semantic owner；Guide 不按章节机械拆分。

Final AI Review 进一步完成了实际去重：`using-agentic-dev.md` 不再重复维护核心 Skill-owned 执行过程，跨职责验证规则归位到 `docs/guides/verification-evidence-rules.md`。

### Phase C — Minimal Metadata / Catalog Contract

**已完成。**

- `docs/project/consumer-local-activation-metadata-contract-v2.md`

采用 `Activation Manifest → optional Runtime Catalog → Consumer-local semantic owner`，并区分 `semantic-reviewed` 与 `current-locator` source binding。

### Phase D — Discovery → Routing → Skill Interface

**已完成。**

- `docs/project/consumer-local-runtime-routing-interface-v2.md`

冻结一个 current primary responsibility + 最小 supporting constraints；`routing-only` 与 Skill execution 分离；Stage Return 后重新 routing；Runtime Adapter 不拥有 Method 语义。

### Phase E — Baseline Adoption / Consumer-local Projection

**已完成。**

- `docs/project/consumer-local-baseline-adoption-projection-v2.md`
- `docs/guides/consumer-local-rule-activation.md`
- `docs/guides/rule-activation-guide.md`
- `docs/guides/verification-evidence-rules.md`

冻结：

- `last evaluated upstream baseline` 与 active local asset 的 `adopted_from` 分离；
- adoption decision history 只在显式升级时使用；
- partial adoption / override / reject / supersede 可审计；
- adopted change 必须成为 Consumer-local current asset；
- ordinary runtime 不读取 upstream 或 upgrade history。

## 5. Phase F — 真实 Consumer 验证

**已完成 / PASS。**

结果：

`docs/project/consumer-local-runtime-validation-result-v2.md`

真实 Consumer：`dygapp/jilinjobs-cms`。

冻结 Consumer base：

`d653495ed2ff61daa33c04f20d9281ba249d4979`

Phase F 开始时冻结的 `agentic-dev` Candidate：

`ec945368678715732fe729c331bd3bcdd919bbdd`

R1～R5 全部 PASS；ordinary runtime upstream access = 0；Base Drift = NO IMPACT；Blocking / Medium reusable finding = `0 / 0`。

最终实验 Head：

`14f2ad7f142f970188a4b7823a158e7026043f5a`

Workflow Run：`34447281667`。

Phase F PASS 只证明 v2 Candidate 能在真实 Consumer 中本地运行，不授权 Consumer 实验分支合并或正式 baseline adoption。

## 6. Phase G — Candidate Drift 与收敛

**已完成。**

Phase F 后的 Final AI Review 发现并修复两个中等级问题：

1. `consumer-local-rule-activation.md` 的冲突措辞可能被理解为 ordinary runtime 需要当前 upstream；
2. `using-agentic-dev.md` 仍重复维护核心 Skill-owned 过程语义。

第二项修复同时新增 `verification-evidence-rules.md` 作为真正跨职责验证规则的 semantic owner，并更新薄导航。

因此冻结新的 reusable candidate：

`29f88efd25232e57ccb4a82ffff039be047e4d1e`

影响判断与结果：

`docs/project/consumer-local-runtime-candidate-drift-review-v2.md`

真实 Consumer 基于原 Phase F 状态完成 T1～T4 定向重验：

```text
T1: PASS
T2: PASS
T3: PASS
T4: PASS
```

最终 Consumer revalidation Head：

`c29da21b41ff3ddad023ecb64e3628dc3136a77e`

Current Evidence：

- Workflow：`Phase G Candidate Drift Revalidation`
- Run：`34450265966`
- Artifact ID：`10141246815`
- Artifact digest：`sha256:7d1a9dc47a6192e4b6c010585d2c69ff387392083448b504c89848465a74fb06`
- Manifest currentness：PASS
- Catalog currentness / rebuild：PASS
- ordinary runtime upstream access：0
- Blocking / Medium reusable findings：`0 / 0`

旧 Phase F R2 / R5 核心机制与 Bootstrap slimming claim 经影响映射仍可复用；新的 source identity 已由 T4 取得 currentness evidence。

## 7. Root Bootstrap / AGENTS 职责收敛

v2 期间确认根 `AGENTS.md` 曾同时承载稳定仓库治理、当前里程碑 / 阶段、候选状态、方法摘要、复核细则、表达细则与 Research 生命周期，违背薄启动与 Progressive Disclosure。

已经实施：

- `AGENTS.md` 只保留稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；
- `README.md` 承载简短当前状态；
- Project Roadmap 承载详细当前路线、Gate 与候选；
- Method / Principle / Architecture / Skill / Guide 恢复各自单点 semantic ownership；
- Git / PR / Issue / Actions 保存精确外部状态与证据；
- 当前阶段、里程碑进展、候选路线、Issue / PR 状态、实验进展和下一工作项不得重新堆入 `AGENTS.md`。

相对 v2 启动基线，Root Bootstrap 完成实质减法；这一边界也在 Consumer Phase F 中得到真实验证。

## 8. 非目标与停止边界

v2 不：

- 产品化 Runtime Rule Index；
- 引入向量 / 图数据库或 MCP 规则服务；
- 全仓统一 Front Matter；
- 创建 Rule Super Skill / Stage Router Skill；
- 强制 Consumer 采用固定目录或全量 reusable inventory；
- 自动合并 Consumer 实验分支；
- 自动启动 WI-06、WI-07、WI-09、第四 Engineering Discipline 或 Issue #71。

后续如果出现新的 reusable 设计问题，应以新证据和新的规划边界处理，不继续无限扩张本里程碑。

## 9. 完成定义与最终结论

以下条件均已满足：

1. Consumer-local Runtime Target、discovery、semantic owner、routing 与 Skill activation 边界一致；
2. 同一规范性规则保持单点长期正文 owner；
3. stale / missing / ambiguity / conflict / high-impact 均有明确 fail-closed；
4. baseline adoption / upgrade 支持 adopt / retain-or-override / reject / supersede；
5. Consumer-native 与 adopted reusable asset 能由同一本地入口协调，同时保持 Consumer Authority 优先；
6. 真实 Consumer 在 ordinary Fresh Context 中不依赖 upstream 仍能正确发现、路由并按需执行 Skill；
7. Consumer 验证无未解决 Blocking / Medium reusable finding；
8. 没有第二套 Authority、机械 metadata 维护、全库复制或超级能力；
9. Root AGENTS / Bootstrap 保持稳定治理入口，不重新累积项目状态、baseline history 或重复方法正文；
10. Phase G Candidate Drift 定向重验已补齐 Phase F 后 reusable changes 的 Current Evidence；
11. README、Roadmap、项目记录和 adoption / usage 入口能让新上下文恢复稳定最终状态。

因此当前结论为：

> **规则治理与知识激活 v2 已具备进入人工集成决策的条件。**

这不等于人工批准，也不授予 Merge。实际集成以及 Issue #92 最终关闭仍由人工权威或仓库策略决定；精确集成事实由 Git / PR #93 保存，不要求合并后再创建纯状态同步提交。
