---
name: github-actions-verification
description: Establishes or optimizes an observable, traceable, cost-aware GitHub Actions verification path for a Consumer Repository. Use when GitHub Actions provides completion evidence and branch/PR trigger choice, CI observability, layered verification, prebuilt runtime containers, artifact reuse, timeouts, cancellation, or diagnostics materially affect reliable verification.
metadata:
  agentic-dev-id: "skill:github-actions-verification"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
---

# github-actions-verification

## 目的

为使用 GitHub Actions 的仓库建立或改进可观察、可追溯、成本有界的验证路径，使 CI 结果能够成为与目标状态匹配的当前证据。

## 输入

- Consumer Repository Authority；
- Required verification claims；
- Existing workflows / branch / PR topology；
- Runtime、artifact 与成本约束；
- 当前任务适用的 Rule candidates。

## 流程

1. 读取 Consumer 当前 workflow、触发拓扑和权限，不从 `agentic-dev` 推断项目事实。
2. 明确哪些 claim 必须由 Actions 证明，以及对应 branch/PR/commit baseline。
3. 通过 Rule Discovery 加载 verification / operations / repository / technology 相关 Rules。
4. 设计最小分层验证：优先复用缓存、预构建运行环境与已生成 artifact，但不得牺牲可追溯性。
5. 配置合理 timeout、cancellation、失败诊断与关键日志/证据保留。
6. 触发后按精确 commit 读取 run/job/step 终态；异步状态按有界观察处理。
7. 只在所需 jobs 对目标 commit 完成且证据可观察时报告通过。

## 输出

- Workflow / verification-path change（如获授权）；
- Exact commit/run evidence；
- Failure diagnostics / cost notes / blockers。

## 退出条件

所需 GitHub Actions 路径能对目标 claim 提供可观察、可追溯且成本有界的当前证据；或已明确不能在当前权限/能力内完成的 blocker。

## 升级

Secrets/credentials、组织级策略、生产部署、不可逆共享状态或仓库保留给人工的权限需要升级。本 Skill 不授予 Consumer 写入或部署权限。
