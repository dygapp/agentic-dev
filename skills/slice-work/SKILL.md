---
name: slice-work
description: Turns a ready specification and optional technical plan into bounded, traceable, context-fit execution units with observable completion conditions and explicit dependencies. Use before readiness checking or when convergence exposes implementation gaps that need new or corrected execution work.
metadata:
  agentic-dev-id: "skill:slice-work"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
  agentic-dev-release-inputs: "method:ai-development;rule:human-intervention-necessity"
---

# slice-work

## 目的

把当前 Ready Specification 与必要 Technical Plan 切成新上下文可以独立理解、实现和验证的 Execution Units。

## 输入

- Ready Specification；
- Optional Technical Plan / Architecture decisions；
- 当前仓库结构与已知依赖；
- 当前运行环境提供的适用约束 / references 与 Consumer-local policy。

## 流程

1. 提取必须实现的可观察行为与验收责任。
2. 读取并应用当前运行环境为本职责提供的适用约束；Consumer Release 使用随 Skill 打包的 references 与 Consumer-local policy，provider runtime 服从当前 Repository Bootstrap。
3. 优先形成窄而完整的纵向单元；避免按数据库/后端/前端/测试机械横切。
4. 每个 Unit 明确 Scope、Authority inputs、Dependencies、Completion Conditions、Verification responsibility 与明确 Out of Scope。
5. 检查 context-fit：新的 Agent 应能在一个上下文完成理解、实现、验证。
6. 明确依赖顺序，但不得把未来 Unit 的 Execute Authority 提前授予当前 Unit。

## 输出

- Ordered Execution Units；
- Explicit dependencies / blockers。

## 退出条件

每个 Unit 边界可独立执行、可验证、可追溯且 context-fit；不存在隐含的跨 Unit 完成责任。

## 升级

切分暴露未解决的产品歧义、长期技术决定或无法安全拆分的共享高影响变更时，返回相应上游阶段。Skill 不执行 Unit。
