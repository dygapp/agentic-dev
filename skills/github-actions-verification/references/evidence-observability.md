# 证据可观察性

## 目的

当前证据（Current Evidence）首先描述证据的时效性和当前状态关联，不表示任何 Current Evidence 都足以支持任何声明。Agent 必须让证据用途与声明类型匹配。

## Completion Evidence

用于证明 Execution Unit / Feature 完成条件的证据，应满足：

- 来自当前目标提交、当前可验证系统状态，或来自已验证祖先状态且已经通过完整后继差异证明不会影响该具体声明；
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

如果 Evidence 的 Head SHA 与当前目标提交不一致，不能直接用于当前 Completion Claim。只有在祖先关系和完整差异可确认、差异对具体声明无影响、相关 Authority / Requirement / Specification / Architecture / Acceptance 语义未改变，并且 Repository Policy 允许时，才可以按声明复用。

复用时至少记录：

```text
Evidence Commit SHA
Current Target SHA
Compare Range
Original Run / Review
Reusable Claim
Invalidated / Re-run Claim
```

文件扩展名、`docs-only` 标签、变更文件数量或“最终提交只改文档”不能代替影响分析。祖先 Run 仍是祖先提交的 Run，不得重命名为当前 Head Evidence；当前 Head 自身需要的 CI、Authority Review 或其他检查仍应按 Repository Policy 取得。

## Artifact 实体验证

当 Artifact 本身被用于证明完成、失败、诊断或其他当前状态时，必须区分：

```text
Artifact upload step success
≠
Artifact entity exists
```

上传步骤的 `success` 只说明该 Step 按当前配置正常结束；在允许缺少文件的配置下，它可能没有实际创建 Artifact。

因此，当 Artifact 本身属于必要 Evidence 时：

1. 重新读取当前 Run 的 Artifact 集合，而不是只读取 upload step conclusion；
2. 核对预期 Artifact 的名称、Run ID 与 Head SHA；
3. 必要时结合 upload step log，确认实际输入路径是否产生文件并被上传；
4. 如果缺少预期 Artifact 本身应使验证失败，则 Workflow 应采用缺失即失败（fail-on-missing）的行为，例如 GitHub Actions `upload-artifact` 的 `if-no-files-found: error`；
5. 如果 Artifact 只是可选诊断产物，则可以允许其缺失，但不得把 upload step 的 `success` 汇报成“Artifact 已存在”。

本规则不要求所有 Completion Verification 都生成 Artifact。只有当 Repository Policy、Verification Strategy、Completion Condition 或当前验证设计明确让 Artifact 承担证据职责时，才要求验证 Artifact 实体及其关联关系。

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
