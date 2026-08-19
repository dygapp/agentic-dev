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
- 写操作后重新读取 Source of Truth 验证；
- 工具调用成功不等于目标状态完成；
- 只汇报已有当前证据支持的状态。

## 2. Analyze：建立真实状态

执行外部写操作前，Agent 应确认：

- 当前 Repository Authority；
- 当前外部对象状态；
- 用户请求的目标结果；
- 当前 Runtime 可用能力；
- 当前操作授权边界。

不要依据旧聊天、缓存印象或此前状态推断当前外部状态。

### 2.1 能操作不等于已授权

拥有外部工具能力不代表自动获得执行授权。

以下操作仍需遵守 Human Authority 或 Repository Policy：

- merge；
- release；
- deploy；
- destructive cleanup；
- 不可逆或高影响修改。

## 3. Human Intervention Boundary：人工介入边界

Agent 不应把所有中间判断都升级给 Human。人工介入应集中在真正需要 Human Authority 或判断的节点。

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

目标是让 Human 关注决策和授权，而不是逐步审批 Agent 的每个动作。

## 4. Act：执行最小必要操作

完成分析后，只执行当前目标要求的最小外部变更。

原则：

- 一次外部变更保持单一主要目的；
- 不顺带修改无关内容；
- 不为了完整性扩大范围；
- 不基于未经验证的假设继续操作。

## 5. Verify：写后重新读取 Source of Truth

必须区分：

```text
Mutation Response
≠
Verified External State
```

写 API 返回成功，只证明操作被接受或执行，不代表目标状态已经成立。

外部写操作完成后，应重新读取相关 Source of Truth 验证：

- 文件修改后的内容和分支状态；
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

## 6. Report：汇报已验证状态

汇报应描述当前已验证状态，而不是仅描述执行过的动作。

状态应区分：

- Verified：目标状态已确认；
- Executed but not fully verified：已执行但未完成验证；
- Blocked：未执行；
- Failed：执行但目标未成立。

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

## 8. GitHub 协作模式

### PR 复核

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

### Repository 修改

```text
读取当前状态
→ 修改
→ 重新读取
→ 验证
→ 汇报
```

### Issue / Evidence 更新

```text
读取 Issue
→ 修改
→ 重新读取 Issue
→ 验证
→ 汇报
```

## 9. 与现有治理规则关系

本 Guide 落实现有规则，而不替代：

- Repository Authority；
- Evidence Before Claims；
- Human Escalation；
- Integration Authorization；
- Git Commit Guidelines。

如果外部操作暴露 Method、Contract 或 Skill 问题，应按现有 Authority 顺序处理，不得通过一次操作暗中改变规则。
