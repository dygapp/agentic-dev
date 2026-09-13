---
id: rule:implementation-minimality
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: []
  artifacts: [code, configuration, test]
  risks: []
---

# 实现最小化

在满足当前权威需求、验证责任、有效长期约束和工程健康的前提下，选择当前证据支持的最低必要复杂度。新增抽象、配置、扩展点、依赖、层次或分支必须能追溯到当前真实责任；仅服务假想未来需求的复杂度默认不进入当前实现。

最低必要复杂度不等于最少代码行。失败路径、安全边界、当前验证入口、已有多个真实消费者的稳定抽象以及正确复用框架所需的薄适配，可以是必要复杂度。