---
id: rule:human-facing-chinese-default
type: rule
status: active
scope:
  phases: []
  activities: [documentation, communication, review]
  technologies: []
  artifacts: [human-facing-content]
  risks: []
---

# 面向人的内容默认自然中文

`agentic-dev` 的文档、Issue、PR、Review、状态说明与面向用户的协作输出默认使用自然、完整、连续的中文。不要为了显得专业或便于检索机械进行中英文并列。

机器接口、代码、路径、命令、协议字段和必须逐字匹配的对象按其原始标识保留。Consumer 的主导语言由 Consumer 自己的 Repository Authority 决定。