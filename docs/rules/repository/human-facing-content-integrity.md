---
id: rule:human-facing-content-integrity
type: rule
status: active
scope:
  phases: []
  activities: [documentation, communication, review, implementation]
  technologies: []
  artifacts: [human-facing-content, machine-identifier, authority]
  risks: []
---

# 面向人的内容完整性

编写或修改文档、Issue、PR、Review、状态说明及其他人类可读内容时，同时保持语言一致性、机器标识精度和正式概念身份。

## 默认自然中文

`agentic-dev` 的面向人内容默认使用自然、完整、连续的中文。不要为了显得专业或便于检索机械进行中英文并列。Consumer 的主导语言由 Consumer 自己的 Repository Authority 决定。

## 精确机器标识保持原样

Skill 调用名、文件名与路径、Branch、Commit SHA、Issue / PR 编号、代码标识符、配置键、数据库字段、API / CLI、命令与参数、协议值、真实日志和错误信息必须保持可精确匹配的原始形式。

保留机器对象原样不意味着周围叙述需要切换成英文。

## 正式概念身份不得被语言重写改变

中文化、术语整理或表达优化只能改变面向人的表达，不得把具有不同职责或生命周期的 Method stage、gate、artifact、Skill、Rule、Architecture 等正式对象合并，也不得改变其正式身份。

当一个自然语言名称可能对应多个正式对象时，必须用对象类型或精确标识消除歧义。