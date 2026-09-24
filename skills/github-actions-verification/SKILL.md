---
name: github-actions-verification
description: Establishes or optimizes an observable, traceable, cost-aware GitHub Actions verification path for a Consumer Repository. Use when GitHub Actions provides completion evidence and branch/PR trigger choice, CI observability, layered verification, prebuilt runtime containers, artifact reuse, timeouts, cancellation, or diagnostics materially affect reliable verification.
---

# github-actions-verification

## 目的

为使用 GitHub Actions 的仓库建立或改进可观察、可追溯、成本有界的验证路径，使 CI 结果能够成为与目标状态匹配的当前证据。

## 输入

- Consumer Repository Authority；
- Required verification claims；
- Existing workflows / branch / PR topology；
- Runtime、artifact 与成本约束；
- Consumer-local constraints。

## 流程

1. 读取 Consumer 当前 workflow、触发拓扑、Consumer-local constraints 与权限，不从 `agentic-dev` 推断项目事实。
2. 明确哪些 claim 必须由 Actions 证明，以及对应 exact branch / PR / commit baseline；触发成功、run 创建或单个 job 成功不能替代 claim 所需 Completion Evidence。
3. 设计最小分层验证：优先复用缓存、预构建运行环境与已有 artifact，但不得牺牲 exact-subject identity、可追溯性和 Evidence currentness。
4. 配置合理 timeout、cancellation、失败诊断与关键日志 / Evidence 保留。新的 run 开始前清理或隔离会污染判断的 stale temporary evidence；不得让旧 artifact 冒充当前 run 输出。
5. 触发后按 exact commit 读取 run / job / step 终态；异步状态按有界观察处理。涉及共享 review environment / database / slot 时维护真实 resource owner / lifecycle；自动验证会污染后续人工复核基线时，先保存当前自动 Evidence，再恢复来源明确、可重复构建的人工 review baseline。
6. Workflow artifact 默认只是一次运行的临时 Evidence。只有当前 Authority 明确接受并确需后续稳定消费时才晋升为持久输入，并验证完整性、provenance、持久位置与受影响 Current Evidence。
7. 复用祖先 commit 的 CI / Runtime / Human Review Evidence 支持当前 commit 时，必须取得 ancestor→current 精确 diff，证明**每个具体 claim**不受差异影响，并记录 ancestor SHA、current SHA、差异范围、原 Run / Review 与 claim mapping；祖先 Run / Review 不能描述为当前 Head 的 Run / Review。若 diff 修改 Roadmap、Requirement、Specification、Architecture、Acceptance 或 Human Review 语义，这些语义 claim 本身视为受影响：必须在当前 Head 重新复核，不能用“docs-only”整体继承祖先结论。无法证明不受影响的 Product / Requirement 语义返回 `clarify-intent` / `specify`，Architecture / cross-unit HOW 返回 `clarify-architecture` / `technical-plan`，需要新的人工确认时返回相应 Human Authority / `human-review`。
8. 终态失败不是默认退出条件。先恢复失败 job / step / logs / artifacts，区分 implementation defect、stale verification contract、Runtime / environment 与 external dependency。只要当前 Consumer Scope 与写入授权已覆盖修复，就继续进入 `systematic-debug` 或等价诊断闭环，实施最低必要修复并重跑；只有确认是不改变代码 / 配置语义的临时故障时才直接重跑同一 Head。任何修复产生新 commit 后都重新绑定 exact Head，再取得 Completion Evidence。
9. 只在以下任一条件成立时结束当前执行闭环：
   - 目标 exact commit 的所需 jobs 已完成成功，必要 logs / artifacts 可恢复，Completion Evidence 已验证；
   - 出现当前 Authority 无法自动解决的真实权限、Product / Business 或 Architecture blocker；
   - 当前 Runtime 在 direct path 与已声明 automated alternate 均无法继续恢复必要 Evidence；
   - 已达到与正常基线相称的有界观察上限。
   后三种只能报告 blocker / 未完全验证，不能报告 Verification PASS，也不得因为当前技术上可执行而越权 merge、release 或 deploy。

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

Secrets / credentials、组织级策略、生产部署、不可逆共享状态或仓库保留给人工的权限需要升级。请求人工前先验证当前 connector / API / Actions、Repository Evidence 与等价自动路径确实不足，并把请求缩到最小不可替代动作。本 Skill 不授予 Consumer 写入或部署权限。
