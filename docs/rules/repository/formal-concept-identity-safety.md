---
id: rule:formal-concept-identity-safety
type: rule
status: active
scope:
  phases: []
  activities: [documentation, review]
  technologies: []
  artifacts: [human-facing-content, authority]
  risks: [semantic-drift]
---

# 正式概念身份安全

语言重写、中文化或术语整理只能改变面向人的表达，不得把具有不同职责或生命周期的正式对象合并，也不得改变 Method stage、gate、artifact、Skill、Rule 或 Architecture 概念的正式身份。

当一个中文名称可能对应多个正式对象时，必须用对象类型或精确标识消除歧义；稳定 Skill 调用名和机器标识保持原样。