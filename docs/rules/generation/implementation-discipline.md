---
id: rule:implementation-discipline
type: rule
status: active
distribution: release-input
release-target: software-development
scope:
  phases: [execute]
  activities: [implementation]
  technologies: []
  artifacts: [code, configuration, test]
  risks: []
---

# 实现纪律：最低必要复杂度与精准差异

实现当前责任时，同时遵守以下边界。

## 最低必要复杂度

在满足当前权威需求、验证责任、有效长期约束和工程健康的前提下，选择当前证据支持的最低必要复杂度。新增抽象、配置、扩展点、依赖、层次或分支必须能追溯到当前真实责任；仅服务假想未来需求的复杂度默认不进入当前实现。

最低必要复杂度不等于最少代码行。失败路径、安全边界、当前验证入口、已有多个真实消费者的稳定抽象以及正确复用框架所需的薄适配，可以是必要复杂度。

## 精准差异范围

最终差异中的每个有意义变化都必须能追溯到当前实现责任、验证责任、已授权权威同步，或由本次修改直接产生且必须闭合的必要清理。

当前变化直接需要、行为保持、范围受控且可验证的准备性重构可以属于同一逻辑变化；相邻独立 Bug、无关 TODO、个人风格清理、大规模无关格式化和其他无法形成当前责任链的修改应移除、记录或另行切分。