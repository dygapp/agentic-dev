---
id: rule:exact-machine-identifiers
type: rule
status: active
scope:
  phases: []
  activities: [documentation, communication, review, implementation]
  technologies: []
  artifacts: [machine-identifier, human-facing-content]
  risks: [identifier-precision]
---

# 精确机器标识保持原样

Skill 调用名、文件名与路径、Branch、Commit SHA、Issue / PR 编号、代码标识符、配置键、数据库字段、API / CLI、命令与参数、协议值、真实日志和错误信息必须保持可精确匹配的原始形式。

保留对象原样不意味着周围叙述需要切换成英文；解释和结论仍遵守当前人类语言规则。