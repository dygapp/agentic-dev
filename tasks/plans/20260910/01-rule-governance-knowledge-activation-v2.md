# 规则治理与知识激活 v2 协调计划

## 目标

协调 Issue #92 所跟踪的“规则治理与知识激活 v2”有限里程碑。

长期目标、设计约束、阶段边界与完成定义统一以：

`docs/project/rule-governance-knowledge-activation-v2.md`

为准。本计划只维护当前协调状态，不复制第二份长期 Authority。

启动基线：`master@b6a20053a7a6f4f53915bea8218604720412c302`  
跟踪入口：Issue #92

## 已完成

### Phase A — Consumer-local Runtime Target / Acceptance

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`

### Phase B — Rule Ownership / Guide Decomposition

- `docs/project/rule-ownership-decomposition-audit-v2.md`

### Phase C — Minimal Metadata / Catalog Contract

- `docs/project/consumer-local-activation-metadata-contract-v2.md`

### Phase D — Discovery → Routing → Skill Interface

- `docs/project/consumer-local-runtime-routing-interface-v2.md`

### Phase E — Baseline Adoption / Consumer-local Projection

- `docs/project/consumer-local-baseline-adoption-projection-v2.md`
- `docs/guides/consumer-local-rule-activation.md`
- `docs/guides/rule-activation-guide.md`

### Root Bootstrap / AGENTS 收敛

已完成根入口职责归位：

- `AGENTS.md` 只维护稳定 Repository Governance / Authority Boundary / Agent 工作约束；
- README 维护简短当前状态；
- Roadmap 维护详细当前路线与下一 Gate；
- Method / Principle / Skill / Guide 不再由 AGENTS 重复正文；
- baseline history、Issue / PR / Run、当前阶段和历史里程碑不进入 AGENTS ordinary context。

## 当前工作项

### Phase F — 真实 Consumer 验证

验证计划：

`docs/project/consumer-local-runtime-validation-plan-v2.md`

首个 Consumer：

`dygapp/jilinjobs-cms`

实际执行必须切换到 Consumer 自己的 Fresh Context / Repository Authority。本 `agentic-dev` 会话不修改 Consumer。

Phase F 必须覆盖：

```text
R1 Ordinary Fresh Context
R2 Stage Return / Ambiguity / Routing-only
R3 Consumer Override
R4 Baseline Upgrade Lifecycle
R5 Stale / Rebuild
```

同时验证 Consumer Bootstrap / AGENTS 不通过累积当前状态、baseline upgrade 流水和重复方法正文来获得可发现性。

## 当前最小输入

`agentic-dev` 侧：

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`
- `docs/project/consumer-local-runtime-validation-plan-v2.md`
- `docs/guides/consumer-local-rule-activation.md`
- Issue #92

Consumer 侧必须在执行时重新恢复自己的 current Authority，不从本计划复制状态。

## 范围控制

Phase F 前后不得：

- 在本 `agentic-dev` 会话直接修改 Consumer；
- 把 `docs/project/*` 整体投射给 Consumer；
- 为实验发明 Consumer 产品规则 / override；
- 建立 Runtime Rule Index、数据库、MCP、Rule Super Skill；
- 启动 WI-06 / WI-07 / WI-09 或 Issue #71 候选实施；
- 只根据 token / 文件读取下降声明 v2 PASS。

## Phase F 证据返回

至少包含：

- Consumer exact branch / Head / PR / evidence；
- candidate `agentic-dev` exact Head；
- R1～R5 verdict；
- actual local sources / Skill reads；
- upstream access 是否被禁止以及是否发生；
- Consumer override 证据；
- baseline adoption decision；
- stale / rebuild evidence；
- AGENTS / Bootstrap 职责收敛结果；
- Blocking / Medium reusable findings；
- Consumer-only findings；
- `PASS / INCONCLUSIVE / REJECT` 建议。

## 后续

Phase F PASS 后：

```text
Phase G
→ v1 / authority / stale / root-bootstrap regression
→ Final AI Review
→ stable-state convergence
→ Ready to Integrate
```

如果 Phase F 暴露 Blocking / Medium reusable design gap，回到真正拥有该问题的 Phase / Authority 修订并重新验证，不为了保持进度降低验收标准。