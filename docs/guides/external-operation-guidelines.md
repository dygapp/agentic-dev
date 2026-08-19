# 外部操作协作指南

本文说明 `agentic-dev` 中的 Agent 在具备 GitHub、Repository、Issue、Pull Request、外部 API 或其他可产生外部状态变化的操作能力时，应如何管理分析、执行、验证和汇报。

本文属于项目级操作治理，不新增 Method 阶段，也不定义新的 Skill。

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

在 GitHub 等可读写外部系统中，也可以理解为：

```text
Read
→ Decide
→ Write
→ Re-read
→ Report
```

关键要求：

- 外部状态在修改前先读取；
- 只有目标、权限和最小必要操作明确后才执行写操作；
- 写操作后重新读取 Source of Truth 验证结果；
- 工具调用成功不能替代最终状态验证；
- 最终只汇报已有当前证据支持的状态。

## 2. Analyze — 先建立真实状态

执行任何外部写操作前，Agent 应先确认：

- 当前 Repository Authority；
- 当前外部对象状态；
- 用户请求的目标结果；
- 当前 Runtime 实际可用的读写能力；
- 当前操作是否在 Agent 授权范围内。

对于 GitHub 工作，按需要读取：

- Repository / Branch 当前基线；
- Issue 当前正文与评论；
- Pull Request metadata；
- changed files；
- relevant patch / diff；
- review threads / checks / merge state；
- 与当前决策直接相关的权威文件。

不要依据旧聊天、缓存印象或此前状态推断当前 GitHub 状态。

### 2.1 能操作不等于已授权

外部工具具备写能力，不代表 Agent 自动拥有使用该能力的授权。

进入 `Act` 前仍需遵守 Repository Policy 和 Human Authority，尤其是：

- merge；
- release；
- deploy；
- destructive cleanup；
- 大范围共享状态修改；
- 不可逆或高影响操作。

如果用户只要求分析、复核或给出建议，不应因为工具可用就自动执行写操作。

## 3. Act — 执行最小必要操作

完成分析后，只执行当前目标要求的最小外部变更。

原则：

- 一次外部变更保持单一主要目的；
- 不顺带修改无关文件、Issue、PR 或配置；
- 不为了“完整”扩大变更范围；
- 不因发现邻近问题就自动继续修复，除非它阻塞当前目标且在授权范围内；
- 对于高影响动作，继续遵守 Human / Repository Policy。

如果操作需要多个紧密相关的写步骤，可以作为一个小的 coherent batch 执行，但在基于该结果继续做后续决策前必须完成验证。

## 4. Verify — 写后重新读取 Source of Truth

这是外部操作闭环中的强制步骤。

必须区分：

```text
Mutation Response
≠
Verified External State
```

写 API 返回成功，只能证明操作请求被接受或执行；不能单独证明目标外部状态已经正确成立。

因此，在外部写操作或一个 coherent write batch 完成后，Agent 应重新读取相应 Source of Truth，并按目标验证最终状态。

### 4.1 文件修改

写入 Repository 文件后，至少按需要确认：

- 目标文件内容已更新；
- 操作发生在正确 Branch；
- resulting commit / content SHA 与操作一致；
- 没有覆盖不相关内容。

### 4.2 Issue 修改

创建或更新 Issue 后，至少按需要确认：

- Issue 确实存在；
- title / body / state 符合目标；
- comment 已进入正确 Issue；
- Evidence Reference 没有丢失或写错。

### 4.3 Pull Request 修改

创建或更新 PR 后，至少按需要确认：

- base / head 正确；
- changed files 符合预期；
- title / body / state 正确；
- diff / patch 与目标一致；
- review / check / mergeability 状态没有出现新的阻塞问题。

### 4.4 Merge 等共享状态变化

执行 merge 或其他共享状态变化后，必须重新读取相关对象与目标 Branch，确认：

- 操作确实完成；
- 目标 Branch 已包含预期结果；
- merge commit / resulting SHA 可追踪；
- 没有把“请求成功”误报成“目标状态已完成”。

## 5. 验证失败时回到 Analyze

如果重新读取后的状态与预期不一致：

```text
Verify Failed
    ↓
Analyze Again
```

此时应先判断：

- 写操作是否失败；
- 是否写到了错误对象或 Branch；
- 外部状态是否在操作期间变化；
- 是否出现 merge conflict、权限限制或其他 blocker；
- 是否需要新的授权或新的最小修正。

在状态未确认前，不得继续基于假定结果执行后续操作。

## 6. Report — 汇报已验证状态

外部操作后的汇报应说明**当前已验证状态**，而不仅是“Agent 做过什么”。

常见状态应明确区分：

- **Verified**：目标状态已经通过重新读取 Source of Truth 确认；
- **Executed, not fully verified**：操作已执行，但无法完成足够的结果验证；
- **Blocked**：由于权限、缺少输入或外部限制未执行；
- **Failed**：尝试执行，但目标状态没有成立。

不要使用“已处理”“已完成”等模糊表达掩盖验证状态。

如果汇报中包含 SHA、PR、Issue、Branch、Check Result 等事实，应以当前重新读取的结果为准。

## 7. 外部交互语言一致性

除非 Repository Policy、外部平台规范或用户明确要求使用其他语言，Agent 在执行面向人的外部协作操作时，应尽量使用与当前工作会话一致的自然语言。

例如，当前会话主要使用中文时，默认：

- Pull Request 标题与说明使用中文；
- Issue 标题、正文和评论使用中文；
- Commit 摘要使用中文；
- Review Comment 使用中文；
- 对外状态说明和协作说明使用中文。

当前会话主要使用英文时，默认使用英文。

以下内容保持其原生形式，不为了语言一致性强行翻译：

- 代码标识符；
- 文件名和路径；
- API / CLI 参数；
- Skill 名称；
- 既有英文术语；
- 外部系统要求的固定枚举值；
- 必须原样引用的错误信息或命令输出。

简化原则：

> Human-facing collaboration follows the human working language; machine-facing identifiers preserve their native form.

如果当前 Repository 已有更具体的语言规则，则以 Repository Policy 为准。

`agentic-dev` 的 Commit Message 继续遵守 `docs/guides/git-commit-guidelines.md`，即 `type` / `scope` 使用小写英文，摘要使用中文。

## 8. GitHub 协作的推荐模式

### 8.1 复核现有 PR

```text
读取 Repository Authority
→ 读取 PR metadata
→ 读取 changed files / relevant patch
→ 形成判断
→ 如已获授权，执行最小修正
→ 重新读取 PR / patch
→ 验证
→ 汇报 verified state
```

### 8.2 修改 Repository 文件

```text
读取当前文件与 Branch
→ 判断最小修改
→ 写入
→ 重新读取文件 / Branch
→ 验证内容与 SHA
→ 汇报
```

### 8.3 更新 Issue / Experiment Evidence

```text
读取 Issue 当前状态
→ 核对 Evidence Reference
→ 追加或修正最小内容
→ 重新读取 Issue / comments
→ 验证
→ 汇报
```

## 9. 与现有治理规则的关系

本 Guide 落实现有规则，而不替代它们：

- Repository Authority 决定项目事实；
- Conversation History 不构成项目权威；
- Evidence Before Claims 仍然成立；
- Human Escalation 仍依据 Authority / Impact / Reversibility；
- Merge / Push / Release / Deploy 等继续遵守 Human Authority 或 Repository Policy；
- Git Commit Message 继续遵守 `docs/guides/git-commit-guidelines.md`。

当外部操作暴露 Method / Contract / Skill 问题时，应按既有 Authority 顺序处理，不能通过一次工具操作暗中改变项目规则。
