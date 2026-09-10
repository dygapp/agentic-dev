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
- Phase F — 真实 Consumer 验证：R1～R5 PASS

Phase F 结果：

`docs/project/consumer-local-runtime-validation-result-v2.md`

## 当前工作项

### Phase G — Candidate Drift 定向重验 Gate

Final AI Review 在 Phase F 后修复两项 Medium，并改变 reusable Guide 集合。旧 Phase F Candidate 为：

`ec945368678715732fe729c331bd3bcdd919bbdd`

当前冻结 reusable candidate：

`29f88efd25232e57ccb4a82ffff039be047e4d1e`

影响分析：

`docs/project/consumer-local-runtime-candidate-drift-review-v2.md`

当前只需在既有 Consumer 实验状态上执行：

```text
T1 updated adopted Guide ordinary local-only
T2 Consumer override after updated local Guide
T3 incremental baseline adoption ec945... → 29f88...
T4 updated source identity / Catalog currentness
```

R2 Stage Return / ambiguity 和 R5 stale / rebuild 核心机制可以复用既有 Phase F Evidence，只补受当前 source identity 变化影响的 currentness 检查。

## 定向重验之后

T1～T4 PASS 且 Blocking / Medium reusable finding = 0 / 0 后：

```text
Final AI Review affected-dimension recheck
→ v1 / Authority / stale / root-bootstrap regression closure
→ README / Roadmap / PR / Issue stable-state convergence
→ Ready to Integrate
```

如果定向重验暴露 Blocking / Medium reusable gap，只返回真正受影响的 owner 修订并定向重验，不机械重跑完整 Phase F。

## 当前最小输入

`agentic-dev`：

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`
- `docs/project/consumer-local-runtime-validation-result-v2.md`
- `docs/project/consumer-local-runtime-candidate-drift-review-v2.md`
- `docs/guides/consumer-local-rule-activation.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/verification-evidence-rules.md`
- Issue #92 / PR #93

Consumer 定向重验必须在其独立授权上下文中执行；本 `agentic-dev` 会话不修改 Consumer。

## 范围控制

Phase G 不：

- 修改 Consumer Repository；
- 合并 Consumer 实验 Branch；
- 将验证视为 Consumer 正式 adoption；
- 产品化 Runtime Rule Index；
- 引入向量 / 图数据库、MCP、Rule Super Skill、Stage Router Skill；
- 继续增加新的 Runtime Eval 场景；
- 启动 WI-06 / WI-07 / WI-09 / Issue #71 候选实施。

## 完成

定向 Consumer Evidence 与 Final AI Review 都通过后，把 PR #93、README、Roadmap、Issue #92 和项目记录收敛为“已具备进入人工集成决策的条件”。

实际 merge 前 Issue #92 保持 open；PR #93 保持 Draft，直到最终 AI Review 完成。合并仍由人工权威或仓库策略决定。