---
name: github-actions-verification
description: Establishes or optimizes an observable, traceable, cost-aware GitHub Actions verification path for a Consumer Repository. Use when GitHub Actions provides completion evidence and branch/PR trigger choice, CI observability, layered verification, prebuilt runtime containers, artifact reuse, timeouts, cancellation, or diagnostics materially affect reliable verification.
---

# github-actions-verification

## Purpose

在使用 GitHub Actions 的 Consumer Repository 中，建立或优化**可观察、可追踪、成本可控**的 CI 验证路径，使 Agent 能够重新取得与当前提交对应的证据，并将验证 Runtime 的复杂度控制在完成声明真正需要的范围内。

本 Skill 是平台专项非核心 Discipline Skill。它实现既有的“证据先于结论（Evidence Before Claims）”、外部操作闭环和 `execute-unit` 验证纪律，不新增 Method 阶段，也不拥有 Merge、Release 或 Deploy 权限。

## Use When

出现以下任一情况时可以使用：

- Consumer Repository 使用 GitHub Actions 产生执行单元（Execution Unit）或 Feature 的验证证据；
- 当前 Agent 无法可靠枚举、读取或关联某类 GitHub Actions Run；
- 需要在 direct push 与 Branch → PR 路径之间选择更可观察的验证路径；
- CI 同时包含后端、前端、数据库、浏览器或其他多 Runtime 集成验证；
- 环境准备、镜像构建或依赖安装显著拖慢反馈周期；
- 需要区分 Fast Feedback 与 Completion Verification；
- 需要通过 Artifact、日志、trace、截图或 Runtime diagnostics 增强失败可诊断性；
- 长运行、过期 Run 或重复环境准备正在降低验证效率。

## Do Not Use When

- Repository 不使用 GitHub Actions，且当前问题与 GitHub Actions 无关；
- 只需要运行一个已经稳定、可观察、低成本的本地验证命令；
- 问题本质是 Product Intent、Specification 或 Major Architecture 决策；
- 需要修改产品完成条件来让 CI 更容易通过；
- 目标是自动接管完整 GitHub 项目生命周期；
- 目标是自动 Merge、Release、Deploy 或执行破坏性清理；
- 只是为了形式完整性给所有 GitHub Repository 增加 PR、容器或复杂 Workflow。

## Inputs

按需读取：

- Consumer Repository Authority / Repository Policy；
- Current Execution Unit / Completion Condition；
- Relevant Technical Plan / Verification Strategy（如存在）；
- `.github/workflows/` 中与当前验证相关的 Workflow；
- 当前 Branch / PR / Commit 状态；
- 当前 GitHub Runtime / Connector 能力；
- Current CI Runs、Jobs、Steps、Logs、Artifacts；
- 与失败直接相关的 Runtime / container / service configuration。

## Authority Sources

按以下边界工作：

1. Consumer Repository Authority 决定项目事实、Integration Policy、允许的 Branch / PR / CI 规则。
2. Current Execution Unit / Specification 决定需要证明什么，不由本 Skill 改写 Completion Condition。
3. Existing Technical Plan / Verification Strategy 决定已确认的长期 HOW；本 Skill 不静默覆盖 Durable Decision。
4. 当前 GitHub Repository、Workflow 和 Runtime 状态决定实际可用的 trigger、日志、Artifact 和 API 能力。
5. `agentic-dev` Method / External Operation Guide 提供 Evidence、Authority、Reversibility 与 Integration Boundary。
6. Conversation History 和未验证的工具假设不构成当前事实。

## Procedure

### 1. Confirm GitHub Actions Verification Scope

先确认 GitHub Actions 在当前工作中承担的职责：

- Fast Feedback；
- Completion Verification；
- Integration / E2E verification；
- Runtime diagnostics；
- 或其中组合。

确认当前需要证明的 Completion Condition，不把“Workflow 成功”机械等同于“Execution Unit Completed”。

### 2. Inspect Repository and Runtime Capabilities

读取实际状态，至少按需确认：

- Workflow trigger；
- Branch / PR policy；
- 当前 Agent 能否枚举对应 Actions Run；
- 能否读取 Jobs / Steps / Logs / Artifacts；
- 当前 CI 是否依赖 secrets、service containers、external services 或 privileged operations；
- 当前验证的主要时间成本和失败点。

不得假设某个 GitHub Connector、CLI 或 API 一定可用。

### 3. Select an Observable Execution / Trigger Path

根据以下维度选择路径：

- Isolation；
- Reversibility；
- Evidence Observability；
- Repository Policy；
- 工作风险与持续时间。

如果当前 Runtime 对 PR-triggered Runs 的可观察性明显优于 push-triggered Runs，可以采用：

```text
Task / Feature Branch
→ Pull Request
→ pull_request-triggered GitHub Actions
→ Current Evidence
```

这只是 Runtime 适配，不把 PR 提升为通用 Method 强制规则。

详细决策见 `references/branch-pr-verification-path.md`。

### 4. Match Evidence to the Claim

区分证据用途：

- **Completion Evidence**：与当前提交和 Completion Condition 匹配、实际执行并满足完成要求的证据；
- **Diagnostic / Runtime Observation**：用于证明 Runtime、Tooling、Failure、阻塞或异常耗时等当前事实。

Diagnostic / Runtime Observation 可以支持 diagnose、abort、reroute 和 workflow optimization，但不能单独替代 Completion Evidence。

详细规则见 `references/evidence-observability.md`。

### 5. Layer Fast Feedback and Completion Verification

优先把验证组织成成本递增的层次：

```text
Cheap / Targeted Checks
        ↓
Build / Static / Unit Verification
        ↓
Runtime / Integration Verification
        ↓
Completion E2E when required
```

中间修复迭代不要求无条件重复最高成本环境准备；但在声明 Completed 前，仍必须取得 Completion Condition 所要求的完整当前证据。

### 6. Reuse Stable Runtime Instead of Rebuilding It Repeatedly

当数据库、浏览器、Java/Node Runtime、HTTP Server 或其他稳定依赖反复准备且成本较高时，优先评估：

1. 官方或 Vendor-maintained 预构建镜像；
2. 当前平台可稳定访问的可信 Registry，例如 GHCR、MCR、Docker Hub；
3. GitHub Actions service containers；
4. Build Artifact 在 Job 之间传递；
5. Consumer 自有的薄封装镜像；
6. 只有确有必要时，才在每次 CI 从头构建完整 Runtime。

多容器不是目标本身；只有当不同 Runtime 生命周期、依赖或诊断边界值得独立时才拆分。

详细 Pattern 见 `references/containerized-e2e.md`。

### 7. Bound Runtime Cost and Stale Work

对于长运行或昂贵验证：

- 设置与正常基线相称的 Job / Step timeout；
- 对同一 PR/ref 的过期 Run 使用可用的 cancellation / concurrency 机制；
- 避免新的提交继续等待已经失去价值的旧 Run；
- 对可缓存或可复用的稳定依赖使用 Repository Policy 允许的复用机制。

### 8. Make Failures Diagnosable

如果原始 Job Log、Connector 日志读取或远程 Runtime 可观察性不足，不根据 Step 名称猜根因。

优先让 Workflow 产出最小必要诊断证据，例如：

- service / container state；
- runtime logs；
- structured test reports；
- browser trace / screenshot；
- health checks；
- diagnostics artifact。

取得新证据后，再交给 `systematic-debug` 做 Root-cause Investigation。

详细 Pattern 见 `references/diagnostics-and-runtime-cost.md`。

### 9. Run, Re-read, and Verify

执行或调整 Workflow 后，重新读取 GitHub Source of Truth：

- Run event；
- Head SHA；
- status / conclusion；
- Jobs / Steps；
- 必要 Logs / Artifacts；
- PR / Branch 与当前提交的对应关系。

当某个 Artifact 本身构成必要验证证据（Verification Evidence）时，Artifact 上传步骤（upload step）的 `success` 不能单独证明 Artifact 实体已经存在。应重新读取当前 Run 的 Artifact 集合，并核对 Artifact 名称、Run 与 Head SHA 的对应关系；如果“缺少该 Artifact”本身应使验证失败，则 Workflow 应采用缺失即失败（fail-on-missing）的配置，例如 GitHub Actions `upload-artifact` 的 `if-no-files-found: error`。

该规则只在 Artifact 本身承担必要证据职责时适用，不要求所有 Completion Verification 都生成 Artifact。

只使用与当前目标提交真实关联的 Evidence。

### 10. Continue Through Asynchronous Intermediate States

如果当前调用要求实际取得 GitHub Actions 结果或完成验证，Workflow 触发（dispatch）/ 重跑（rerun）响应只表示操作已经进入 `Act`，不是本 Skill 的默认退出条件。

当 Run 处于 `queued`、`pending` 或 `in_progress`，并且当前 Runtime 能继续读取 Actions 状态时：

1. 使用与正常运行基线相称的间隔重新读取 Run；
2. 持续核对 event、Head SHA、status / conclusion 与当前 PR / Branch 的关联；
3. Run 进入失败终态时取得必要 Jobs、Steps、Logs 或 Artifacts；
4. 如果修复属于当前 Scope 且已经授权，使用 `systematic-debug` 取得 Root Cause、执行最小修复并重新运行验证；
5. 重新进入观察与证据核对，直到取得目标证据或出现真实阻塞。

等待必须有界：结合正常耗时、Job / Step timeout、当前运行进度和 Repository Policy 设置轮询间隔与观察上限。不得无限轮询，也不得仅因为异步运行尚未结束就要求 Human “继续执行”。

当前执行闭环可以在以下情况结束：

- Completion Condition 所需证据已经从当前 Run 取得并核对；
- 出现需要 Human Authority 的权限、业务、架构、安全或高影响决定；
- Runtime 无法继续取得必要证据，且没有 Repository Policy 允许的替代路径；
- 达到有界观察上限，当前状态被准确记录为 `Executed but not fully verified`（已执行但未完全验证），没有声明完成。

如果调用范围只要求设计或优化验证路径，而不要求实际触发并等待运行，应明确输出 Evidence Retrieval Plan 和尚未执行的验证状态；不得把计划写成已经取得的 Completion Evidence。

### 11. Return Verification Result to the Caller

返回：

- Selected Verification Path；
- Workflow / Runtime adjustments（如有）；
- Current Evidence references；
- Completion Evidence status；
- Diagnostic / Runtime observations；
- Remaining blocker / escalation（如有）。

本 Skill 自身不把整个 Feature 标记为 `Ready to Integrate`，也不自动执行下一个 Execution Unit。

## Outputs

按需输出：

- Observable GitHub Actions Verification Path；
- Workflow / Runtime Optimization；
- Evidence Retrieval Plan；
- Current Completion Evidence；
- Diagnostic / Runtime Evidence；
- Required follow-up / escalation。

## Exit Conditions

当以下条件满足时，本 Skill 可以结束：

- 当前验证路径符合 Consumer Repository Policy；
- 如果调用只要求设计验证路径，Agent 已明确如何取得完成声明需要的当前证据，并保持实际验证为未执行状态；
- 如果调用要求实际完成验证，必要的 Current Evidence 已经取得并核对，或者已经准确记录真实阻塞 / 有界观察上限；仍可观察的 `queued`、`pending` 或 `in_progress` Run 本身不满足退出条件；
- Workflow 成本与当前验证风险基本相称，不存在已知的无界长运行路径；
- 需要的 Runtime / Integration 验证边界清晰；
- 当前失败如果仍存在且修复已获授权，已经取得足以进入 `systematic-debug` 的可观察证据，并保持修复、重跑与复验仍属于当前执行闭环；
- 未越权执行 Integration / Release / Deploy。

## Escalation Conditions

出现以下情况时停止未经授权的调整并升级：

- Repository Policy 明确要求 Human 决定 Branch / PR / CI 策略；
- 需要改变 Product Completion Condition 或 Specification；
- 需要 Major Architecture / Deployment Topology Decision；
- 涉及 secrets、production credentials、security-sensitive permission；
- 需要不可逆或高影响 External / Data Operation；
- 需要 Release / Deploy / Merge 权限但当前未授权；
- 当前 Runtime 无法取得必要 Completion Evidence，且没有仓库允许的可替代路径。

Run 仍在正常异步执行、且 Runtime 仍可观察，不单独构成 Human Escalation Condition。

## Context Rules

- Authority First；
- Progressive Disclosure；
- 只读取当前验证路径需要的 Workflow / Run / Runtime 信息；
- GitHub 当前状态优先于旧聊天和缓存印象；
- PR、GHCR、MCR、Docker、多容器均是条件性实现手段，不是 Method 强制语义；
- 不把 Consumer-specific 镜像版本、目录或 Workflow 结构写成跨项目事实；
- 修改外部状态时遵循 `docs/guides/external-operation-guidelines.md`。

## References

- `references/branch-pr-verification-path.md`
- `references/evidence-observability.md`
- `references/containerized-e2e.md`
- `references/diagnostics-and-runtime-cost.md`

## Allowed Sub-skills / Disciplines

- Verification-before-claim
- Context Discipline
- Human Escalation
- `systematic-debug`（Unexpected Failure / Root-cause Investigation）
