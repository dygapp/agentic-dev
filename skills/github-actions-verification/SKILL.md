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
- 自动化验证与人工评审共用 Runtime，但测试数据、静态资源或容器写入可能污染 Human Review Baseline；
- 环境准备、镜像构建或依赖安装显著拖慢反馈周期；
- 需要区分 Fast Feedback 与 Completion Verification；
- 需要通过 Artifact、日志、trace、截图或 Runtime diagnostics 增强失败可诊断性；
- 长运行、过期 Run、共享外部资源争用或重复环境准备正在降低验证效率。

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
- 与失败直接相关的 Runtime / container / service configuration；
- Workflow 使用的固定域名、代理名、端口、部署 / 评审槽位、临时数据库或其他共享外部资源及其 owner / lifecycle；
- Human Review Baseline / fixtures，以及自动测试可能修改的数据库、文件、缓存或其他共享状态。

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

证据类型必须与声明类型匹配：

- Functional Browser Verification 可以证明路由、交互、资源加载和已编码断言；
- Visual Fidelity 需要与视觉 Requirement 对应的参考证据和判断路径；没有完整机器可判定容差时，Functional Browser PASS 不能单独替代 AI 视觉对照与 Human Visual Review；
- Human Review 的原始结论应按实际范围记录，不得把“基本通过、暂未发现新的阻塞问题”扩大为“完全一致”或无条件验收。

Workflow 应优先承载运行环境、部署链路和正式测试套件的执行语义，例如构建、服务就绪、HTTP / API 可达和测试结果。具体产品展示语义应尽量由正式测试套件承担；如果 Workflow 必须重复同一产品语义，应共享同一配置或契约来源，避免形成第二份 hard-coded assertion。

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

当当前变更包含数据库 Migration，且 Runtime / CI 条件允许时，Completion Verification 至少应覆盖一次：

```text
Fresh Database
→ Full Migration Chain
→ Application Startup
```

SQL 文件检查、编译、单元测试或只在已有数据库上执行增量 Migration，不能单独证明新环境初始化可用。

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

### 7. Separate Automated Verification State from Human Review Baseline

如果自动化验证完成后还要暴露同一 Runtime 供人工评审，不得默认把测试结束时的数据库、文件、导航、缓存或会话状态直接作为 Human Review Baseline。

优先建立以下可验证闭环：

```text
Automated Verification
→ Collect Current Evidence
→ Recreate / Reset Known Baseline
→ Seed Explicit Human Review Fixtures
→ Start / Expose Review Runtime
→ Verify Review Baseline and Access Path
```

具体要求：

- 明确自动测试会修改哪些共享状态，以及 Human Review 实际需要哪些示例数据；
- 基线应来源明确、可重复构建；优先从 Versioned Static Baseline、migration / seed 或等价权威来源恢复；
- 自动测试数据只有在被明确采纳为 Human Review Fixture 时才可以保留，不能因共用环境而意外泄漏；
- 对容器可写的 host bind mount，显式处理 UID / GID、ownership、permissions 与 cleanup；不得假设 runner 普通权限的 `rm -rf` 一定成功；
- 清理和恢复必须重新验证，包括测试数据已移除、版本化资源已恢复、人工示例数据已准备、服务健康与评审地址可访问；
- Reset 路径应在授权的临时 / 评审环境中具备可重复执行性；不得把该规则解释为对生产或未授权共享数据执行 destructive cleanup。

详细 Pattern 见 `references/containerized-e2e.md`。

### 8. Bound Runtime Cost, Stale Work, and Shared Resource Contention

对于长运行或昂贵验证：

- 设置与正常基线相称的 Job / Step timeout；
- 对同一 PR/ref 的过期 Run 使用可用的 cancellation / concurrency 机制；
- 避免新的提交继续等待已经失去价值的旧 Run；
- 对可缓存或可复用的稳定依赖使用 Repository Policy 允许的复用机制。

如果不同 PR、Branch、ref 或 trigger 会争用固定域名、代理名、端口、部署 / 评审槽位、临时数据库、单例服务或其他排他资源，先区分 Workflow 的逻辑标识与资源的真实冲突域：

1. 列出当前 Run 会取得、修改或暴露的共享外部资源及其 owner / lifecycle；
2. 让 concurrency group、lock、lease 或等价机制覆盖所有争用同一资源的触发路径，而不是默认只按 PR / ref 分组；
3. 对资源彼此独立的运行保留并行能力，不把 Repository 级单例并发推广为通用默认；
4. 把 Run cancellation 与外部资源释放分别验证；取消 Run 或终止进程后，外部资源仍可能短暂残留；
5. 只对当前 Workflow 拥有且授权可处理的资源执行有界等待、重试、释放或接管，不盲目清理生产资源或其他 owner 的资源；
6. 取得资源或启动进程后，重新核对资源归属，并验证目标地址、服务或结果对应当前 Run / Head 和预期环境。

```text
Identify Shared Resource
→ Match Lock Scope
→ Acquire / Release with Ownership
→ Verify Target Availability
```

详细 Pattern 见 `references/diagnostics-and-runtime-cost.md`。

### 9. Make Failures Diagnosable

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

### 10. Run, Re-read, and Verify

执行或调整 Workflow 后，重新读取 GitHub Source of Truth：

- Run event；
- Head SHA；
- status / conclusion；
- Jobs / Steps；
- 必要 Logs / Artifacts；
- PR / Branch 与当前提交的对应关系。

当某个 Artifact 本身构成必要验证证据（Verification Evidence）时，Artifact 上传步骤（upload step）的 `success` 不能单独证明 Artifact 实体已经存在。应重新读取当前 Run 的 Artifact 集合，并核对 Artifact 名称、Run 与 Head SHA 的对应关系；如果“缺少该 Artifact”本身应使验证失败，则 Workflow 应采用缺失即失败（fail-on-missing）的配置，例如 GitHub Actions `upload-artifact` 的 `if-no-files-found: error`。

该规则只在 Artifact 本身承担必要证据职责时适用，不要求所有 Completion Verification 都生成 Artifact。

Evidence 必须与当前目标提交和具体声明建立可审计关联；关联不等于所有 Evidence 都必须由同一个 Head SHA 的同一种 Run 产生。

### 10.1 Evaluate Evidence Reuse Across Descendant Commits

当高成本 Runtime / Human Review Evidence 来自当前目标提交的祖先提交时，默认先把它视为待重新验证的旧证据，不因后继提交看起来是 `docs-only`、文件数量少或 CI 仍为绿色就自动继承。

只有同时满足以下条件，才可以按 Evidence Claim 复用未受影响的祖先证据：

1. 已确认祖先 Evidence Commit 是当前目标提交的祖先，并取得两者之间的完整、精确差异；
2. 逐项说明差异为什么不能改变该证据所支持的行为、环境、数据、资源或人工判断对象；
3. 差异没有改变与该声明相关的 Repository Authority、Requirement、Specification、Architecture、Acceptance、Workflow、Runtime 配置、Migration、Fixture 或版本化资源；
4. 当前 Repository Policy 允许按影响范围分层验证，并且当前 Head 已完成其自身需要的检查；
5. 记录 Evidence Commit SHA、Current Target SHA、compare range、原 Run / Review 引用、可复用的具体声明和仍需重新验证的声明。

Evidence reuse 是**按声明**的，不是给整个提交一次性盖章：

- 祖先 Runtime Run 可以继续证明未受后继差异影响的既有 Runtime 行为，但不能被改称为当前 Head 的 Run；
- Human Review 只能复用未改变评审对象、基线和判断语义的部分；Human Review 暴露的新 Product / Requirement / Domain / Architecture Finding 必须重新读取 Authority 后路由；
- 文档文件也可能改变 Requirement、Specification、Architecture、Acceptance 或 Project State；文件扩展名不能证明无影响；
- 如果差异触及或可能触及某项声明，或者无法证明无影响，则重跑该声明所需的验证或重新取得相应 Human / Authority Review；
- Review Runtime 的偶发启动失败可以记录为 Runtime Observation；只有它阻断当前仍需取得的证据时才阻止完成，不用于否定已经正确关联且未受影响的其他证据。

### 11. Continue Through Asynchronous Intermediate States

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

### 12. Return Verification Result to the Caller

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
- 已识别的排他外部资源具有匹配真实冲突域的并发 / 锁边界，以及有界、可验证且符合 owner / 授权约束的释放路径；
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
- 共享资源 owner 不明确，或继续操作需要清理、接管生产 / 其他 owner 的资源；
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
