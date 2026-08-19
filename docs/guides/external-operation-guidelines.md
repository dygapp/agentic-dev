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

## 2. Analyze

执行外部写操作前，Agent 应