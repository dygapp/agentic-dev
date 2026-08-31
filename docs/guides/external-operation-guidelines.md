# 外部操作协作指南

本文说明 `agentic-dev` 中的 Agent 在具备 GitHub、Repository、Issue、Pull Request、外部 API 或其他可产生外部状态变化的操作能力时，应如何管理分析、执行、验证和汇报。

本文属于项目级操作治理，不新增方法（Method）阶段，也不定义新的 Skill。

## 1. 核心闭环

外部操作统一遵循：

```text
Analyze
  ↓
Act
  ↓
Verify
  ↓
Report
```

GitHub 等可读写系统中可理解为：

```text
Read
→ Decide
→ Write
→ Re-read
→ Report
```

核心要求：

- 外部状态修改前先读取；
- 明确目标、权限和最小必要操作后再执行；
- 写操作后重新读取事实来源（Source of Truth）验证；
- 工具调用成功不等于目标状态完成；
- 只汇报已有当前证据支持的状态。

## 2. 分析（Analyze）：建立真实状态

执行外部写操作前，Agent 应确认：

- 当前仓库权威（Repository Authority）；
- 当前外部对象状态；
- 用户请求的目标结果；
- 当前运行环境（Runtime）可用能力；
- 当前操作授权边界。

不要依据旧聊天、缓存印象或此前状态推断当前外部状态。

### 2.1 能操作不等于已授权

拥有外部工具能力不代表自动获得执行授权。

以下操作仍需遵守人工权威（Human Authority）或仓库策略（Repository Policy）：

- merge；
- release；
- deploy；
- destructive cleanup；
- 不可逆或高影响修改。

### 2.2 多 Repository 操作分别确认授权

同一任务涉及多个 Repository 时，Agent 必须分别确认每个 Repository 的操作授权。某个 Repository 的读写权限、当前认证身份或 Runtime 工具能力，不会自动授予对另一个 Repository 的同类操作权限。

应根据当前 Human Authority 与各 Repository Authority，按需区分：

- 读取文件、提交、PR、Issue 与 Actions 状态；
- 创建或更新 Issue / Evidence；
- 修改文件、Branch、Commit 或 PR；
- 触发、重跑或取消 Workflow；
- Merge、Release、Deploy 或 destructive cleanup。

具体授权组合由当前项目决定，本指南不要求所有 Consumer 使用统一权限矩阵，也不把“上游 Repository 只读”设为通用规则。如果某项跨 Repository 操作的授权不明确，应停止该项操作并确认边界；其他已经明确授权且不依赖该操作的工作可以继续，不应把局部授权缺口扩大成整个任务的默认停止条件。

当这类边界会持续约束后续工作时，应按当前 Repository Authority 固化到可发现的 Project Rule 或等价载体，不能只依赖当前聊天或 Runtime 的临时授权印象。

## 3. 人工介入边界（Human Intervention Boundary）

Agent 不应把所有中间判断都升级给人工。人工介入应集中在真正需要 Human Authority 或人工判断的节点。

### 3.1 默认原则

当以下条件同时满足时，Agent 应尽量自主完成一个完整闭环：

- 目标明确；
- 操作范围明确；
- 权限明确；
- 风险低；
- 操作可逆；
- 不改变长期规则或架构方向。

此时流程应为：

```text
Analyze
→ Act
→ Verify
→ Report
```

而不是在每个中间步骤请求确认。

### 3.2 需要提前人工介入的情况

包括但不限于：

- 目标、范围或验收标准存在关键歧义；
- 将改变 Method、Contract、Repository Authority 或长期治理规则；
- 存在多个长期影响明显不同的方案选择；
- 涉及高影响、不可逆或共享状态变化；
- 当前授权边界无法判断。

### 3.3 不需要频繁确认的情况

通常不需要单独请求确认：

- 文档措辞调整；
- 符合现有规则的文件组织；
- 低影响、可逆的实现细节；
- 已明确目标下的执行步骤。

目标是让人工关注决策和授权，而不是逐步审批 Agent 的每个动作。

## 4. 执行（Act）：执行最小必要操作

完成分析后，只执行当前目标要求的最小外部变更。

原则：

- 一次外部变更保持单一主要目的；
- 不顺带修改无关内容；
- 不为了完整性扩大范围；
- 不基于未经验证的假设继续操作。

### 4.1 验证外部二进制与媒体输入的真实内容

从外部站点、接口、附件或其他 Repository 取得的二进制 / 媒体资源，文件名、扩展名、URL 后缀和响应头只提供线索，不能单独证明内容类型。把资源版本化或交给 Runtime 消费前，应按当前风险执行：

```text
Acquire
→ Verify Content Signature / Media Type
→ Decode or Parse when relevant
→ Normalize when needed
→ Version
→ Verify in Target Runtime
```

具体要求：

- 使用 magic bytes、可靠的媒体类型识别或实际解码 / 解析核对真实格式；图片等资源按需要同时核对尺寸、色彩 / 透明度或其他会影响目标声明的属性；
- 如果真实格式与扩展名、声明类型或目标 Runtime 要求不一致，先判断应更正命名、转换格式还是拒绝输入；不得只改扩展名伪装格式；
- 转换或规范化后重新验证生成物，不把“转换命令成功”当作资源可用；
- 保留当前任务需要的最小来源关系，并在目标 Runtime 中验证加载和展示 / 消费结果；
- 只有内容类型、格式差异会影响当前行为、验证或安全边界时才增加相应检查，不要求对普通文本或所有文件无差别执行昂贵媒体分析。

## 5. 验证（Verify）：写后重新读取事实来源

必须区分：

```text
Mutation Response
≠
Verified External State
```

写 API 返回成功，只证明操作被接受或执行，不代表目标状态已经成立。

外部写操作完成后，应重新读取相关事实来源验证：

- 文件修改后的内容和 Branch 状态；
- Issue 的实际状态；
- PR 的 metadata、changed files、diff；
- Merge 后的目标 Branch 和 commit。

如果验证失败：

```text
Verify Failed
    ↓
Analyze Again
```

不得继续基于错误状态执行后续操作。

### 5.1 异步外部操作属于闭环中间状态

触发 Workflow、Deployment、远程 Job 或其他异步操作，只表示 `Act` 已被接受，不代表 `Verify` 已完成。`queued`、`pending`、`in_progress` 等非终态不能被当作目标状态，也不应仅因为外部系统仍在运行就默认把当前任务交回人工。

当当前目标包含取得执行结果或验证证据，且 Runtime 能继续观察状态时，应在授权范围内保持同一闭环：

```text
Act
→ Observe
→ Collect Current Evidence
→ Diagnose
→ Fix / Retry when authorized
→ Verify
→ Report
```

具体要求：

- 使用与正常运行基线相称的轮询间隔、等待上限、timeout 与 cancellation 策略，避免无限等待；
- 每次观察重新读取当前事实来源，不使用旧状态推断运行已经结束；
- 运行失败时先取得必要日志或诊断证据，再在当前授权范围内修复和重试；
- 只有需要 Human Authority 的权限、业务、架构或高影响决定才升级人工；“仍在运行”本身不是人工决策；
- Runtime 无法继续取得必要证据且不存在已授权的替代路径时，记录为真实阻塞；
- 达到有界观察上限而运行仍未结束时，只能汇报“已执行但未完全验证”的当前状态，不能声明目标完成。

异步闭环可以在以下任一条件成立时结束：目标状态已由当前证据验证；出现真实阻塞；或达到有界观察上限并准确保留未验证状态。后两种结果都不能伪装成完成结论。

### 5.2 并发边界必须匹配真实共享资源

异步运行的逻辑标识不一定等于外部资源的排他边界。不同 PR、Branch、ref 或 Run 可能仍然争用同一个固定域名、代理名、端口、部署 / 评审槽位、临时数据库、单例服务或受限账号资源。

当外部操作会取得或修改共享资源时，应先识别真实冲突域，再选择 concurrency group、lock、lease 或等价机制：

- 同一资源的所有触发路径与 ref 必须进入同一排他边界，不能只按 PR / ref 分组而留下跨组竞争；
- 不共享资源的运行应保留合理并行能力，不能把 Repository 级单例机械推广为所有 Workflow 的固定政策；
- 排他边界只回答“谁不能同时使用资源”，不自动决定竞争 Run 应排队还是取消；只有新 Run 确实取代旧工作，且取消后的资源释放闭环可靠时才使用 cancellation，否则应让独立工作有界排队；
- 取消 Workflow、终止本地进程或成功取得锁，只能证明对应动作发生，不能单独证明外部资源已经释放、归属正确或目标服务可用；
- 对残留资源采用有界等待、重试、释放或接管路径，并在清理前核对资源标识、当前 owner、环境与操作授权；不得盲目清理生产资源、其他 owner 的资源或授权范围外的共享状态；
- 取得资源后重新读取其当前归属和状态，并验证目标地址、服务或结果确实对应当前 Run / Head 和预期环境。

并发与资源生命周期应形成：

```text
Identify Shared Resource
→ Match Exclusivity Scope
→ Acquire / Release with Ownership
→ Verify Target State
```

具体实现由 Consumer Repository、平台能力与资源拓扑决定。本指南不固定 concurrency key，也不要求所有 Consumer 使用同一种锁或清理策略。

## 6. 汇报（Report）：汇报已验证状态

汇报应描述当前已验证状态，而不是仅描述执行过的动作。

状态应区分：

- **已验证（Verified）**：目标状态已确认；
- **已执行但未完全验证（Executed but not fully verified）**：已执行但未完成足够验证；
- **受阻（Blocked）**：未执行；
- **失败（Failed）**：执行后目标未成立。

不要使用模糊表达掩盖验证状态。

## 7. 外部交互语言一致性

除非 Repository Policy、外部平台规范或用户明确要求，面向人的外部协作内容应尽量使用当前工作语言。

例如中文会话默认：

- PR 标题和说明使用中文；
- Issue 标题、正文、评论使用中文；
- Commit 摘要使用中文；
- Review Comment 使用中文。

以下保持原生形式：

- 代码标识符；
- 文件名和路径；
- API / CLI 参数；
- Skill 名称；
- 固定技术术语。

术语呈现方式遵循 `docs/guides/terminology-guidelines.md`。

## 8. GitHub 协作模式

### 8.1 Git / GitHub 执行路径选择

Git 分支（Branch）是 Git 的隔离机制；Pull Request（PR）是 GitHub 提供的协作与集成对象。二者都属于具体 Repository / 平台能力，不是通用 Method 的强制对象。

在 GitHub Consumer 中选择执行路径时，不应只判断“是否能够直接写默认分支”，还应同时检查：

- **隔离性（Isolation）**：未完成工作是否会污染共享权威基线；
- **可逆性（Reversibility）**：失败或方向调整时能否低成本恢复；
- **证据可观察性（Evidence Observability）**：当前 Runtime 能否重新取得验证和 CI 结果；
- **仓库策略（Repository Policy）**：是否要求分支、PR、复核（Review）或特定 CI 触发方式；
- **工作风险与持续时间**：是否需要多轮实现、验证、调试或人工复核。

对于需要多轮修改、CI、调试或 Review 的工作，如果直接修改共享默认分支会降低隔离性、可逆性或证据可观察性，应优先采用当前 Repository / Runtime 支持的隔离路径。

在 GitHub 中，常见路径是：

```text
Task / Feature Branch
→ Pull Request
→ GitHub Actions
→ Current Evidence
→ Ready to Integrate
→ Human / Repository Policy
```

PR 可以同时提供变更复核、CI 触发、证据关联和集成边界。因此，当当前 GitHub Runtime 对 PR-triggered Actions 的可观察性明显优于 push-triggered Actions 时，Agent 可以优先选择该路径。

这不是“所有 GitHub 项目必须使用 PR”的通用规则。如果 Repository Policy 允许直接推送（direct push），且当前 Runtime 能完整取得当前验证证据，低风险工作仍可以采用更轻量路径。

当 GitHub Actions 验证本身需要进一步设计、诊断或优化时，可按条件使用 `github-actions-verification` Skill；本指南只定义协作与授权边界，不承载具体 Workflow、容器或镜像实现方案。

### 8.2 PR 复核

```text
读取 Repository Authority
→ 读取 PR 状态
→ 读取 changed files / diff
→ 判断
→ 执行授权修改
→ 重新读取 PR
→ 验证
→ 汇报
```

### 8.3 Repository 修改

```text
读取当前状态
→ 修改
→ 重新读取
→ 验证
→ 汇报
```

### 8.4 Issue / Evidence 更新

```text
读取 Issue
→ 修改
→ 重新读取 Issue
→ 验证
→ 汇报
```

## 9. 与现有治理规则的关系

本指南落实已有规则，而不替代它们：

- 仓库权威（Repository Authority）；
- 证据先于结论（Evidence Before Claims）；
- 人工升级（Human Escalation）；
- 集成授权（Integration Authorization）；
- Git Commit 规范。

如果外部操作暴露 Method、Contract 或 Skill 问题，应按现有 Authority 顺序处理，不得通过一次操作暗中改变规则。
