---
id: rule:data-access-boundedness
type: rule
status: active
scope:
  phases: [technical-planning, execute]
  activities: [design, implementation]
  technologies: []
  artifacts: [data-access]
  risks: []
---

# 数据访问作用域与有界性

设计或修改集合型数据访问时，先确认当前消费者真正需要的数据作用域，并判断集合是稳定有界、持续增长还是当前无法可靠界定。访问范围、分页 / 窗口、缓存生命周期和验证必须匹配真实消费边界。

不得为了实现方便默认全量读取可能持续增长的数据，也不得用固定小上限静默截断业务正确集合。若当前需求需要完整集合且无法证明有界，应显式设计可扩展访问或返回上游解决范围与契约问题。