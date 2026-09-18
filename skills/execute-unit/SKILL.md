---
name: execute-unit
description: Implements and verifies exactly one ready execution unit in minimal fresh context using current repository evidence. Use when a single unit is ready to execute; discover repository-specific verification, route unexpected failures through systematic-debug, and stop after evidence supports or fails the unit completion condition.
metadata:
  agentic-dev-id: "skill:execute-unit"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
---

# execute-unit

## 目的

在 Fresh Context 中只实现一个 Ready Execution Unit，并取得与该 Unit Completion Conditions 匹配的当前验证证据。

## 输入

- One Ready Execution Unit；
- Direct Specification / Technical / Architecture Authority；
- 当前代码与测试状态；
- 当前任务适用的 Rule candidates。

## 流程

1. 重新读取 Unit、直接 Authority 与当前仓库事实，确认没有使 readiness 失效的 drift。
2. 从当前任务/代码事实提取 task signals，通过 Rule Discovery 加载 generation、verification、technology 等适用 Rules。
3. 形成临时 JIT Execution Plan，只包含本 Unit 的精确施工与验证步骤。
4. 按当前仓库既有模式实施最低必要变更；不顺带处理其他 Unit。
5. 对预期 TDD 失败按计划推进；意外失败调用/转入 `systematic-debug`，不得猜测绕过。
6. 运行与 Completion Conditions 对应的当前验证，并只基于当前证据声明结果。
7. 停在 Unit 完成边界，不自动合并、发布、部署或启动下一 Unit。

## 输出

- Unit implementation；
- Current verification evidence；
- Completion result / blocker。

## 退出条件

当前证据支持全部 Unit Completion Conditions，或已准确识别无法在本 Unit 内关闭的 blocker。

## 升级

上游 Authority 缺口、未授权产品/架构改变、不可逆外部操作或权限阻塞按责任层升级。
