---
id: rule:execution-continuity-and-stop-condition
type: rule
status: active
distribution: release-input
release-target: software-development
scope:
  phases: []
  activities: [design, documentation, implementation, verification, review, external-operation]
  technologies: []
  artifacts: []
  risks: []
---

# 执行连续性与停止条件

任何子任务、工具调用、Job、Eval、测试、构建、提交、推送或委派运行进入终态，都不等同于整个当前任务已经完成。

## 子操作终态后重新计算剩余责任

每次子操作进入成功、失败、取消、超时或其他终态后，Primary Agent 必须：

1. 重新读取并吸收该步骤产生的当前 Evidence；
2. 对照当前用户目标、Repository Authority、当前责任、Gate 与完成条件，重新计算仍未完成的责任；
3. 确定下一项仍在当前授权与责任边界内的必要动作；
4. 只要存在可继续自动完成的剩余责任，且没有满足合法停止条件，就继续执行，不得因为某个局部步骤已经结束而静默停止或把局部完成误报为整体完成。

失败或未验证结果同样必须进入上述责任重算；不得因为某个子操作失败就跳过当前能力范围内仍可执行的诊断、修复、重新验证或证据恢复。

## 合法停止条件

连续执行只在以下至少一种条件成立时停止：

- 当前责任已经满足其明确完成条件；
- 当前 Method、Skill 或其他 Authority 明确定义的退出边界已经到达；
- 用户明确要求暂停、停止或只执行到当前边界；
- 下一步明确要求新的 Fresh / Independent Context，当前上下文应完成证据交接后停止；
- 下一步需要不可替代的 Human Authority、决策或输入；
- 当前权限、凭证、能力或环境形成无法在当前责任内关闭的真实 blocker；
- 有界异步观察达到既定上限，并明确保留为未完成或未验证状态。

Skill 或 Method 的退出边界只结束该责任本身，不自动证明更大的用户任务已经完成。不得在 Skill 内越过其自身 Exit Condition；如果同一个 Primary Agent 同时承担更高层协调责任，应先退出当前 Skill，再回到上层 Authority 重新计算剩余责任，由上层流程决定是否进入下一责任。

## 最终输出前检查

准备结束当前执行、报告完成或把工作交还给用户前，必须能够明确指出当前满足的是哪一种合法停止条件，并确认没有仍在当前授权与能力范围内、且属于当前任务的已知剩余责任。无法给出合法停止理由时，应继续执行，而不是输出一个只描述局部状态的结束性答复。

## 连续执行不扩大成本或权限

连续执行只要求关闭剩余责任，不授予新的权限，也不构成启动额外模型、provider、CLI、authenticated runtime 或其他高成本执行面的理由。下一动作仍应优先使用当前 Primary Agent、Repository Runtime 与确定性工具，并遵守当前适用的执行上下文 / 被测 Runtime、授权、人工介入和证据匹配约束。
