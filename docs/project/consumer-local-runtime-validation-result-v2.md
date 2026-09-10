# Consumer-local Runtime 真实验证结果 v2

## 状态

**Phase F 结果 — PASS**

上层里程碑：Issue #92 / `docs/project/rule-governance-knowledge-activation-v2.md`

真实 Consumer：`dygapp/jilinjobs-cms`

本结果只证明 Rule Governance v2 Candidate 在冻结 Consumer 基线上具备 Consumer-local 持续运行能力；不授权 Consumer 实验分支合并、正式 baseline adoption、产品路线变化或新的 Execute Authority。

## 1. 冻结基线

Consumer Validation Base：

`dygapp/jilinjobs-cms@d653495ed2ff61daa33c04f20d9281ba249d4979`

agentic-dev Candidate：

`dygapp/agentic-dev@ec945368678715732fe729c331bd3bcdd919bbdd`

Consumer Experiment Branch：

`experiment/rule-activation-v2-consumer-validation`

Consumer Final Experiment Head：

`14f2ad7f142f970188a4b7823a158e7026043f5a`

Formal Consumer Adoption：`false`

## 2. Phase F Verdict

- R1 Ordinary Fresh Context：PASS；
- R2 Stage Return / Ambiguity / Routing-only：PASS；
- R3 Consumer Override：PASS；
- R4 Baseline Upgrade Lifecycle：PASS；
- R5 Stale / Rebuild：PASS；
- Base Drift Review：NO IMPACT；
- ordinary runtime upstream access（R1～R3 / R5）：0；
- Blocking reusable finding：NONE；
- Medium reusable finding：NONE。

最终结论：**PASS**。

## 3. Consumer-local 实际投射

实验实际验证了以下最小能力集合：

- thin Consumer Bootstrap / Authority boundary；
- Consumer-native Documentation / Architecture locator；
- Consumer-local Activation Manifest；
- adopted reusable `consumer-local-rule-activation` Guide；
- 一个按需加载的本地 `technical-plan` Skill；
- baseline evaluation state 与 upgrade-only adoption history 分离；
- 一个真实 Consumer-specific Repository Operation Boundary override。

没有把 `agentic-dev/docs/project/*`、完整 upstream Guide / Skill 树、Research / Eval 或项目状态投射给 Consumer。

## 4. 关键行为结论

### R1 — Ordinary Fresh Context

新的 Consumer Fresh Context 只读取 Consumer-local Bootstrap、Manifest、Roadmap / Architecture locator、当前 ADR、adopted Guide 与在真正进入技术规划评估后才加载的本地 `technical-plan` Skill。

它没有把仅为 Planning Candidate 的工作提升为 Execute，也没有制造不存在的 Readiness / Architecture Authority；ordinary runtime upstream access 为 0。

### R2 — Stage Return / Ambiguity

受控架构基础变化场景得到：

```text
primary responsibility = technical-planning
supporting context = execution + readiness
Stage Return = true
systematic-debug = false
routing-only full Skill load = false
old Readiness continues to authorize Execute = false
```

说明 metadata / local modules 能完成职责区分，并在只需 routing 时避免机械加载完整 Skill。

### R3 — Consumer Override

真实 Consumer-specific Repository Operation Boundary 正确覆盖更通用 reusable default；统一 discovery 没有改变 Consumer Repository Authority precedence。

### R4 — Baseline Upgrade Lifecycle

从旧 evaluated baseline 到 v2 Candidate 的显式比较形成了 `adopt / retain-or-override / reject-not-applicable` 三类真实结果。

其中 `last evaluated upstream baseline` 与 active asset 自身 `adopted_from` 保持分离；被拒绝的 upstream 项目状态、Research / Eval、bulk docs 与 online upstream runtime dependency 没有进入 active Manifest。

### R5 — Stale / Rebuild

机器验证确认：

```text
semantic source identity drift
→ stale detected
→ stop trusting derived discovery
→ Consumer-local fail-closed
→ stale rebuild refused
→ source repair
→ catalog delete / rebuild
```

Catalog 删除没有导致规范性 Consumer fact 丢失。

## 5. Current Evidence 层次

Consumer 原始 Evidence 文档记录的 `Validated Runtime Head` 为：

`d728fa493fa8901b02c5d9ba6200275798bcc205`

随后只增加 1 个证据记录提交：

`14f2ad7f142f970188a4b7823a158e7026043f5a`

该提交只新增 `evals/rule-activation-v2/phase-f-evidence.md`，没有改变 Runtime / Consumer-local 资产或验证逻辑。

最终 Current Evidence 使用：

- Workflow：`Phase F Rule Activation Validation`；
- Run：`34447281667`；
- Head：`14f2ad7f142f970188a4b7823a158e7026043f5a`；
- conclusion：`success`；
- Artifact：`phase-f-rule-activation-evidence`；
- Artifact ID：`10140161292`；
- Artifact digest：`sha256:9dbc5516d692ffc2ce0c07b6a118c134d3e488e9a152732ecee4cc0e26a09d8d`。

因此 `d728fa4...` 是 Runtime 候选通过后的运行锚点，`14f2ad7...` 是补入 Evidence 文档后再次通过 Workflow 的最终 Consumer Experiment Head。两者职责不同，不构成相互冲突的 Current Evidence。

## 6. Bootstrap 审计结果

Consumer 冻结基线真实存在：

- `AGENTS.md` 混入易变化的 EU / PR / Run / SHA / 历史状态；
- ordinary Fresh Context 默认读取较大的 Development Method，从而携带 baseline 历史；
- Repository / Method / lifecycle 语义在 Bootstrap 重复；
- Current State 在多个入口重复维护；
- Documentation Authority Map 存在缺失 Architecture locator。

实验采用职责归位后，高优先级入口相对冻结基线为：

- `AGENTS.md`：`+60 / -117`；
- `README.md`：`+21 / -52`；
- `docs/README.md`：`+33 / -55`；
- Roadmap：`+51 / -169`。

这进一步支持 v2 的 Consumer-local Bootstrap 原则：可发现性不能通过持续扩大 `AGENTS.md` / ordinary recovery 输入来获得。

## 7. Findings

Reusable Low：验证流水中 `validator | tee` 若没有 `pipefail`，可能掩盖 validator 非零退出。Consumer 实验已修复并在最终 Head 上重新取得成功 Current Evidence。该问题属于通用 verification evidence hygiene，但不是 Rule Governance v2 Blocking / Medium gap。

Consumer-only：

- frozen Documentation Authority Map 的 Architecture locator 缺失；
- legacy Development Method 仍物理保留部分 baseline 历史，但已退出 ordinary Fresh Context；
- 本地容器 DNS 阻止物理 worktree，实验改用从冻结 base 创建的独立远程 Branch，未触碰 Consumer main 或当前工作分支。

这些都不改变 Phase F PASS。

## 8. Phase G 入口

Phase F 证据已经满足进入 Phase G 的门槛。

Phase G 仍需完成：

1. v1 核心规则与 fail-closed 边界回归；
2. Authority / Method / Architecture / Guide / Skill 一致性复核；
3. Consumer Phase F Evidence 复核；
4. Root Bootstrap / AGENTS 瘦身边界复核；
5. Final AI Review；
6. README / Roadmap / Issue / PR 最终状态收敛；
7. 达到“已具备进入人工集成决策的条件”。

Phase F PASS 本身不授权合并 PR #93。