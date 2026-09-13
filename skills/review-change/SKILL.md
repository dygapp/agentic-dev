---
name: review-change
description: Reviews a final repository change against current authority, scope, contracts, applicable rules, and evidence, then reports actionable findings or a bounded pass conclusion. Use when repository policy or the user requests an independent or high-impact change review; do not use as a substitute for implementation verification or human integration approval.
metadata:
  agentic-dev-id: "skill:review-change"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
---

# Review Change

## Purpose

基于当前 Repository Authority 与最终变更状态进行独立复核，发现会阻止安全接受的语义、范围、授权、生命周期或证据问题。

## Inputs

- 当前目标基线与拟接受变更；
- 当前 Repository Authority；
- 精确 diff / changed files；
- 当前验证证据；
- 适用 Rule candidates。

## Procedure

1. 重新读取当前 Authority 和最终变更，不依赖作者说明或旧 Review 结论。
2. 明确本次 review claim：要判断的是哪些变更是否可安全接受，而不是重新设计目标。
3. 从变更事实提取 review signals，读取 Rule Discovery 返回的适用 Rules。
4. 检查 authority consistency、语义回归、scope、授权边界、证据与长期 artifact lifecycle；技术专项检查只在对应 Rule 适用时进行。
5. 记录可执行 findings，区分阻塞、中等与低 / 非阻塞问题；每项 finding 指向具体事实和影响。
6. 修复发生后重新读取最终变更，并只复用能够证明仍不受影响的旧结论。
7. 没有未解决的阻塞或中等级 finding 时，可报告 review 通过。

## Outputs

- findings（严重程度、位置 / 事实、影响、建议修复边界）；或
- bounded pass conclusion；
- 未完成验证 / 人工决策等剩余边界。

## Exit Conditions

已检查的范围不存在未解决的阻塞或中等级 finding，或已经准确列出必须返回上游 / 人工处理的 blocker。

## Escalation

- Repository Authority 自身冲突；
- 需要改变产品 / 方法 / 架构目标而不是修复当前变更；
- 需要人工承担的高影响、难逆或集成决定。

Review 通过不等于 merge / release / deploy 授权。