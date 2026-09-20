---
name: converge
description: Performs feature-wide convergence against specification, domain and architecture authority, applicable project-roadmap state, artifact lifecycle responsibilities, current implementation, and verification evidence. Use after required execution work is complete enough for final review; return READY or route evidence-backed gaps to the responsible layer, then stop at Ready to Integrate.
metadata:
  agentic-dev-id: "skill:converge"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
---

# converge

## 目的

在功能/变更范围内对 Authority、当前实现和当前证据做最终收敛，判断是否达到 `Ready to Integrate`，而不是执行集成。

## 输入

- Current Specification / Domain / Architecture Authority；
- Relevant Execution Units and implementation；
- Current verification evidence；
- 当前任务适用的 Rule candidates。

## 流程

1. 重新读取最终 Authority 与当前实现，不把单个 Unit 的完成自动等同于整体完成。
2. 通过 Rule Discovery 加载 completion、verification、repository、technology 等适用 Rules。
3. 对每项可观察行为、边界、非功能义务和长期 artifact responsibility 建立当前证据对应关系。
4. 检查跨 Unit 接缝、遗漏、未关闭 finding、base drift 与当前状态文档一致性。
5. 缺口按责任层返回 Clarify / Specify / Technical Plan / Slice / Execute / Debug，而不是在 Converge 中静默重设计。
6. 只有不存在已知阻塞缺口且证据匹配目标状态时返回 READY。

## 输出

- `READY TO INTEGRATE`；或
- Evidence-backed convergence gaps 与责任层。

## 退出条件

Authority、实现与当前证据一致，且没有已知阻塞缺口。

## 升级

集成、merge、release、deploy 以及必须由人工承担的高影响决定保持在仓库/人工 Authority。READY 不是集成授权。
