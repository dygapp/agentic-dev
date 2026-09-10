# 规则治理与知识激活 v2 协调计划

## 目标

协调 Issue #92 所跟踪的“规则治理与知识激活 v2”有限里程碑。

长期目标、设计约束、阶段边界与完成定义统一以：

`docs/project/rule-governance-knowledge-activation-v2.md`

为准。本计划只维护当前协调状态，不复制第二份长期 Authority。

启动基线：`master@b6a20053a7a6f4f53915bea8218604720412c302`  
跟踪入口：Issue #92

## 已完成

- Phase A — Consumer-local Runtime Target / Acceptance
- Phase B — Rule Ownership / Guide Decomposition
- Phase C — Minimal Metadata / Catalog Contract
- Phase D — Discovery → Routing → Skill Interface
- Phase E — Baseline Adoption / Consumer-local Projection
- Root Bootstrap / `AGENTS.md` 职责收敛
- Phase F — 真实 Consumer 验证：PASS

Phase F 结果：

`docs/project/consumer-local-runtime-validation-result-v2.md`

真实 Consumer `dygapp/jilinjobs-cms` 的 R1～R5 全部 PASS，ordinary runtime upstream access = 0，Base Drift = NO IMPACT，Blocking / Medium reusable Rule Governance v2 finding = NONE。

## 当前工作项

### Phase G — 收敛与集成准备

当前只执行：

```text
v1 core / fail-closed regression
→ Authority / Method / Architecture / Guide / Skill consistency
→ Consumer Phase F Current Evidence review
→ Root Bootstrap responsibility regression
→ Final AI Review
→ stable-state convergence
→ Ready to Integrate
```

Phase G 不继续设计新 metadata schema、Runtime Index、Guide 拆分或 Skill，也不修改 Consumer。

## 当前最小输入

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`
- `docs/project/consumer-local-runtime-validation-result-v2.md`
- `docs/guides/rule-activation-guide.md`
- `docs/guides/consumer-local-rule-activation.md`
- 只在具体一致性复核需要时读取 Phase A～E contract / Architecture / Skill
- Issue #92
- PR #93

Consumer 原始实验资产只在需要核对 Phase F Evidence Claim 时读取，不作为普通 `agentic-dev` Runtime Authority。

## Phase G Gate

必须确认：

1. Consumer Repository Authority first、Progressive Disclosure、Evidence before claims 与 fail-closed 没有被 v2 削弱；
2. metadata / Catalog 不拥有规则正文，不形成第二套 Authority；
3. routing-only 与 Skill execution 分离，Stage Return 后重新 routing；
4. baseline adoption 后 ordinary runtime local-only，upstream update 不自动改变 Consumer；
5. Phase F Current Evidence 与最终 Consumer Head / Run / Artifact 一致且可追溯；
6. `AGENTS.md` 不重新承担当前阶段 / 里程碑 / baseline history / 方法摘要；
7. v2 没有静默启动 WI-06 / WI-07 / WI-09 / Issue #71 或新的 Runtime infrastructure；
8. Final AI Review Blocking / Medium = `0 / 0`。

## 范围控制

Phase G 不：

- 修改 Consumer Repository；
- 合并 Consumer 实验 Branch；
- 将 Phase F 验证视为 Consumer 正式 adoption；
- 产品化 v1 Runtime Rule Index；
- 引入向量 / 图数据库、MCP、Rule Super Skill、Stage Router Skill；
- 继续增加 Runtime Eval 场景；
- 启动其他候选里程碑。

## 完成

Phase G 全部通过后，把 PR #93、README、Roadmap、Issue #92 和本项目记录收敛为“已具备进入人工集成决策的条件”。

在实际 merge 前 Issue #92 保持 open；PR #93 是否由 Draft 转为 Ready 取决于 Final AI Review 和最终状态复核。合并仍由人工权威或仓库策略决定。