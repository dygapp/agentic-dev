---
name: external-operation
description: Safely performs authorized changes to external or shared state such as GitHub objects, CI runs, remote APIs, review environments, or other mutable services. Use when a task requires an external write or asynchronous external state transition; do not use for read-only inspection or purely local edits.
metadata:
  agentic-dev-id: "skill:external-operation"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
---

# External Operation

## Purpose

对已授权的外部可变状态完成“读取真实状态 → 最小操作 → 重新读取验证 → 汇报”的闭环，不把工具调用成功误报为目标状态完成。

## Inputs

- 目标外部对象与期望状态；
- 当前 Repository / Human Authority；
- 可用工具与认证边界；
- 当前外部状态；
- 与操作相关的 Rule candidates。

## Procedure

1. 重新读取目标外部对象的当前事实，确认请求目标、作用域和授权。
2. 提取当前 operation signals，并读取 Rule Discovery 返回的适用 operation Rules。
3. 选择满足目标的最小必要、优先可逆操作；不顺带修改无关状态。
4. 执行写操作。
5. 重新读取事实来源验证目标状态，而不是只检查写 API 的成功响应。
6. 对异步操作在授权范围内执行有界观察、诊断和必要重试；达到终态、真实阻塞或观察上限后停止。
7. 只汇报当前证据能够支持的结果；未验证状态必须明确保留为未验证。

## Outputs

- 已执行操作；
- 验证后的当前外部状态；
- 必要诊断 / 当前证据；
- 未验证边界或真实 blocker；
- 需要人工权威时的最小 escalation。

## Exit Conditions

目标状态已由重新读取的当前证据确认；或已识别无法在当前授权 / 能力内解决的真实 blocker；或异步观察达到既定有界上限并准确保留未验证状态。

## Escalation

- 授权无法从当前 Authority 判断；
- merge / release / deploy / destructive remote operation 等被仓库策略保留给人工；
- 高影响或难逆共享状态变化存在多个实质不同方案；
- 当前环境缺少完成或验证操作所需 credentials / capability。

本 Skill 不授予任何外部写权限。