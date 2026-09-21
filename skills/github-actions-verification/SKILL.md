---
name: github-actions-verification
description: Establishes or optimizes an observable, traceable, cost-aware GitHub Actions verification path for a Consumer Repository. Use when GitHub Actions provides completion evidence and branch/PR trigger choice, CI observability, layered verification, prebuilt runtime containers, artifact reuse, timeouts, cancellation, or diagnostics materially affect reliable verification.
metadata:
  agentic-dev-id: "skill:github-actions-verification"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
  agentic-dev-release-inputs: "rule:async-operation-bounded-observation;rule:human-intervention-necessity;rule:safe-external-write;rule:shared-resource-concurrency-ownership;rule:temporary-evidence-to-persistent-input-promotion;rule:evidence-claim-reuse-across-commits;rule:evidence-type-must-match-claim;rule:human-review-baseline-isolation;rule:verification-contract-currentness"
  agentic-dev-runtime-execution: "external"
---

# github-actions-verification

## 目的

为使用 GitHub Actions 的仓库建立或改进可观察、可追溯、成本有界的验证路径，使 CI 结果能够成为与目标状态匹配的当前证据。

## 输入

- Consumer Repository Authority；
- Required verification claims；
- Existing workflows / branch / PR topology；
- Runtime、artifact 与成本约束；
- 当前运行环境提供的适用约束 / references 与 Consumer-local policy。

## 流程

1. 读取 Consumer 当前 workflow、触发拓扑和权限，不从 `agentic-dev` 推断项目事实。
2. 明确哪些 claim 必须由 Actions 证明，以及对应 branch/PR/commit baseline。
3. 读取并应用当前运行环境为本职责提供的适用约束；Consumer Release 使用随 Skill 打包的 references 与 Consumer-local policy，provider runtime 服从当前 Repository Bootstrap。
4. 设计最小分层验证：优先复用缓存、预构建运行环境与已生成 artifact，但不得牺牲可追溯性。
5. 配置合理 timeout、cancellation、失败诊断与关键日志/证据保留。
6. 触发后按精确 commit 读取 run/job/step 终态；异步状态按有界观察处理。终态失败时先恢复失败 job / step / logs / artifacts，区分实现缺陷、陈旧验证契约、Runtime / 环境问题与外部依赖；在 Consumer 当前 Scope 和写入授权允许时，进入 systematic-debug 或等价诊断闭环并实施最小必要修复。只有不改变代码 / 配置语义的临时故障才可直接重跑同一 Head；任何修复产生新 commit 后，都必须重新绑定新的 exact Head 并重跑、复验。
7. 只在所需 jobs 对当前目标 exact commit 完成且证据可观察时报告通过；无法在授权范围内关闭的失败、权限阻塞或达到有界观察上限时，保持未验证 / blocker 状态而不是伪装完成。

## 可执行路径合同

- `direct-path`：使用当前 Runtime 已授权的 GitHub connector / API / CLI / Actions capability，对目标 exact commit 的 workflow 执行或读取真实 run 状态。
- `automated-alternate`：direct path 不可用时，只允许使用 Consumer Repository 已声明的等价 GitHub Actions transport、connector 或受控 API 路径；替代路径必须维持相同授权边界和 Evidence 可恢复性。
- `evidence-recovery`：恢复并核对 exact commit、event、run、job、step、必要 logs / artifacts 与终态 conclusion；触发成功不能替代这些当前证据。
- `fail-closed`：无法绑定目标 commit、无法恢复 run / job 终态、缺少执行或读取权限，或所有声明路径都不可用时，不报告 Verification PASS，并返回真实 blocker / 未验证边界。

## 输出

- Workflow / verification-path change（如获授权）；
- Exact commit/run evidence；
- Failure diagnostics / cost notes / blockers。

## 退出条件

所需 GitHub Actions 路径能对目标 claim 提供可观察、可追溯且成本有界的当前证据；或已明确不能在当前权限/能力内完成的 blocker。

## 升级

Secrets/credentials、组织级策略、生产部署、不可逆共享状态或仓库保留给人工的权限需要升级。本 Skill 不授予 Consumer 写入或部署权限。
