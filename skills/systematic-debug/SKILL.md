---
name: systematic-debug
description: Investigates an observed defect or unexpected failure through reproduction, authority-backed expected-versus-actual analysis, falsifiable root-cause hypotheses, minimal fix, and regression evidence. Use for unexpected failures or standalone defect work; not for expected initial TDD failures or undefined product behavior.
metadata:
  agentic-dev-id: "skill:systematic-debug"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
---

# systematic-debug

## 目的

对已观察到的 defect / unexpected failure 建立可证伪根因，再做最小修复和回归验证；不把猜测当根因。

## 输入

- Observable failure / defect；
- Expected behavior Authority；
- Relevant code/runtime state；
- 当前任务适用的 Rule candidates。

## 流程

1. 稳定复现问题，并记录 actual behavior 与最小触发条件。
2. 从权威来源确认 expected behavior；若产品行为本身未定义，返回 Clarify/Specify，而不是自行定义。
3. 通过 Rule Discovery 加载与当前 failure、technology、artifact、risk 相关的 Rules。
4. 收集能区分原因的证据，形成有限、可证伪的 root-cause hypotheses。
5. 逐一验证假设，直到证据支持根因；不得同时做多项无关“可能修复”。
6. 实施针对根因的最低必要修复。
7. 运行回归与必要邻接验证，确认原 failure 消失且没有已知相关回归。

## 输出

- Reproduction / expected-vs-actual；
- Evidence-backed root cause；
- Minimal fix；
- Regression evidence / unresolved blocker。

## 退出条件

根因有证据支持，修复与根因一致，当前回归证据支持预期行为；或已明确应返回上游 Authority。

## 升级

预期行为冲突、需要改变产品意图/重大架构、不可逆数据风险或权限不足时升级。
