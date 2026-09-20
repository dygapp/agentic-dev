---
id: guide:upgrading-agentic-dev
type: guide
status: active
distribution: source-only
---

# 升级 Consumer 中的 agentic-dev 能力

本文是 `method:consumer-upgrade` 的人类说明，不替代正式 Method。

## 升级不是覆盖最新版

Existing Consumer 已经拥有自己的 Method / Architecture / Skills / Rules 和本地 adaptation。升级必须以 **当前 Consumer local state** 为起点，而不是把 upstream 当作主副本。

推荐过程：

1. 恢复 Consumer 当前 Authority 与已评估 baseline；
2. 选择一个精确 upstream candidate baseline；
3. 比较真正的 semantic delta，而不是只看文件 diff；
4. 对每项变化决定 retain / adopt / adapt / replace / reject；
5. 只修改已经接受的 Consumer-local owner；
6. 对受影响能力做 targeted revalidation；
7. 记录新的 evaluated baseline。

## 需要特别保护的本地差异

Consumer-local Rule 不应因为 upstream 有同名或类似 Rule 就自动被覆盖。例如两个仓库完全可以拥有不同的 Git commit type / scope、迁移约束或审批边界。

同样，旧 Evidence 不能自动证明新语义；如果升级改变了 Method Gate、Skill behavior、Rule policy 或 discovery contract，需要重新验证对应 claim。

正式过程与完成条件见 `docs/methods/consumer-upgrade.md`。