---
name: review-change
description: Reviews a final repository change against current authority, scope, contracts, applicable rules, and evidence, then reports actionable findings or a bounded pass conclusion. Use when repository policy or the user requests an independent or high-impact change review; do not use as a substitute for implementation verification or human integration approval.
metadata:
  agentic-dev-id: "skill:review-change"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
---

# Review Change

## 目的

基于当前 Repository Authority 与最终变更状态进行独立复核，发现会阻止安全接受的语义、范围、授权、生命周期或证据问题。

## 输入

- 当前目标基线与拟接受变更；
- 当前 Repository Authority；
- 精确 diff / changed files；
- 当前验证证据；
- 适用 Rule candidates。

## 流程

1. 重新读取当前 Authority 和最终变更，不依赖作者说明或旧 Review 结论。
2. 明确本次 review claim：要判断的是哪些变更是否可安全接受，而不是重新设计目标。
3. 从变更事实提取 review signals，读取 Rule Discovery 返回的适用 Rules。
4. 根据变更影响选择复核深度：普通变更执行通用 consistency / regression / scope / evidence / lifecycle 检查；命中下述高影响 Authority 条件时，追加 **Authority-chain semantic review**。
5. 检查 authority consistency、语义回归、scope、授权边界、证据与长期 artifact lifecycle；技术专项检查只在对应 Rule 适用时进行。
6. Authority-chain mode 中按语义责任链挑战 currentness、ownership、downstream projection、replaceability、conflict classification 与 source promotion；只有命中再生性条件时才执行 bounded code-holdout / regenerability challenge。
7. 记录可执行 findings，区分阻塞、中等与低 / 非阻塞问题；每项 finding 指向具体事实和影响。
8. 修复发生后重新读取最终变更，并只复用能够证明仍不受影响的旧结论。
9. 没有未解决的阻塞或中等级 finding 时，可报告 review 通过。

## 权威链语义复核

### 触发边界

该模式只用于会实质改变或重组长期 Authority chain 的高影响变更，例如：

- bulk Authority restructure；
- canonical owner 的 fold / replace / retire / archive；
- Requirement / Domain / Specification / Interface 的重大 convergence；
- Product / Architecture 明确声明 replaceability 或发生 technology substitution review；
- heterogeneous legacy / historical / current source reconstruction；
- high-impact semantic migration。

普通代码修复、局部文案修改或没有跨层 Authority 影响的常规 PR 不因为本模式存在而自动执行 full regenerability。

### 语义问题

1. **Current owner transition**：canonical owner 或 lifecycle 改变后，Current locator、selector、verification consumer 与 durable current-state wording 是否都已迁移；historical / archive / provenance 引用是否被明确限制在非 Current 角色，而不是 ordinary runtime dependency。
2. **Single semantic owner + bounded projection**：重复表达是合法 locator / summary / observable projection，还是 competing Current truth；每层是否只拥有自己的 semantic responsibility。
3. **Downstream observable projection**：Requirement / Domain 中已经接受、且需要用户、运营人员或维护者观察、失败或验收的语义，是否存在 Current Observable / Failure / Acceptance projection；fold / merge / archive 是否产生 orphan capability。
4. **Replaceability seam**：只有在明确 replaceability boundary 命中时，检查替代实现维持 compatibility 所需的 stable interface、failure semantics 与 responsibility split 是否可以脱离被替换源码恢复。
5. **Conflict classification**：Authority、implementation 与 verification 冲突时，先基于 owner / currentness / provenance 判断是 implementation defect、stale Authority 还是 stale verification contract；不得因为“代码当前如此”自动覆盖 Product / Architecture truth。
6. **Source role / promotion boundary**：用于当前 claim 的 source 是 canonical Authority、bounded canonical data、implementation evidence、historical evidence、Human decision 还是 unresolved material；Evidence 不得越权 promotion 成更高层 truth。

### 有界可再生性挑战

当变更涉及大规模 Authority restructuring、明确 replaceability、major Specification / Interface convergence、heterogeneous reconstruction 或 high-impact semantic migration 时，追加反事实挑战：

- 不读取当前 implementation，Current Authority 是否足以恢复 Product behavior、stable contracts、failure semantics、responsibility boundaries 与 acceptance / verification obligations？
- 若替换 implementation technology，stable compatibility seam 是否仍能从 Current Authority 确定？

该 challenge 可以是针对受影响 capability / seam 的 bounded dry-run，不要求每个高影响 Review 都重建完整系统；implementation 可以在设计冻结后作为 comparison / oracle 使用，但不能反向成为缺失 Authority 的默认答案。

## 输出

- findings（严重程度、位置 / 事实、影响、建议修复边界）；或
- bounded pass conclusion；
- 未完成验证 / 人工决策等剩余边界。

## 退出条件

已检查的范围不存在未解决的阻塞或中等级 finding，或已经准确列出必须返回上游 / 人工处理的 blocker。

## 升级

- Repository Authority 自身冲突；
- 需要改变产品 / 方法 / 架构目标而不是修复当前变更；
- 需要人工承担的高影响、难逆或集成决定。

Review 通过不等于 merge / release / deploy 授权。