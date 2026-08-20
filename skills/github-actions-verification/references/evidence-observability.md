# 证据可观察性

## 目的

当前证据（Current Evidence）首先描述证据的时效性和当前状态关联，不表示任何 Current Evidence 都足以支持任何声明。Agent 必须让证据用途与声明类型匹配。

## Completion Evidence

用于证明 Execution Unit / Feature 完成条件的证据，应满足：

- 来自当前目标提交或当前可验证系统状态；
- 实际执行，而不是计划执行；
- 与 Completion Condition 直接对应；
- 达到仓库要求的必要验证范围；
- 可以由当前 Repository / Runtime 重新取得或核对。

历史成功、旧日志、代码阅读、推测结果或仅有“Implementation Exists”不能替代 Completion Evidence。

## Diagnostic / Runtime Observation

Human 或 Agent 取得的以下信息可以成为当前 Runtime / Tooling 事实证据：

- Run URL / Run ID；
- UI 截图；
- Step 状态与持续时间；
- 可见日志；
- container / service state；
- trace / screenshot / diagnostics artifact；
- 明确的人工取消、重试或异常环境观察。

这些证据可以支持：

- diagnose；
- abort；
- reroute；
- workflow optimization；
- Runtime / Tooling Finding。

但它们不能因为“也是 Current Evidence”就自动证明 Execution Unit Completed。

## 证据关联检查

读取 GitHub Actions Evidence 时至少核对：

```text
Repository
Workflow
Event
Head SHA
Run status
Run conclusion
Relevant Jobs / Steps
Required Artifacts / Logs
```

如果 Evidence 与当前目标提交不匹配，不用于当前 Completion Claim。

## Connector 可观察性不足时

如果 Agent 知道某个 CI Run 存在，但当前 Connector 无法自动枚举：

1. 不宣称“没有 CI”；
2. 不把未知状态写成 PASS / FAIL；
3. 可以由 Human 临时提供 Run URL / ID；
4. 已知 Run 后重新读取 Jobs / Steps / Logs；
5. 如果该人工补链会持续重复，优先寻找当前 Repository Policy 允许的可自动观察路径，例如 PR-triggered CI；
6. 如果仍无法取得必要 Completion Evidence，则 Completion Claim 保持受阻。

## 证据最小化

Evidence 应足以支持当前声明，但不要求无差别保存完整 CI 日志。优先保留：

- 直接支持 Completion / Failure 判断的结果；
- 能复现或定位当前 Root Cause 的最小诊断信息；
- 能把 Evidence 与 Commit / PR / Run 唯一关联的引用。
