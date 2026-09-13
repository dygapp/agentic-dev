---
id: rule:evidence-claim-reuse-across-commits
type: rule
status: active
scope:
  phases: [execute, converge]
  activities: [verification, review]
  technologies: []
  artifacts: [commit, evidence]
  risks: [evidence-reuse]
---

# 跨提交复用证据

复用祖先提交上的 CI、Review 或 Runtime evidence 支持当前提交的 claim 时，必须能够取得精确 diff，并逐项证明该差异不会影响对应 claim，相关 Authority / acceptance semantics 未改变，且仓库策略允许 claim-level reuse。

复用记录至少要能追溯 ancestor SHA、current SHA、差异范围和 claim mapping。受影响或无法证明不受影响的 claim 必须重新取得证据；祖先 Run 不得描述为当前提交的 Run。