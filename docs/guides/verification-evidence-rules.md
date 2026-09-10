# 跨职责验证与证据规则

本文承载不属于单一核心 Skill、但会按条件约束多个执行 / 收敛职责的 reusable verification rule families。

本文不重新定义 `execute-unit`、`converge` 或平台专项 Skill 的完整过程。只有当前任务实际满足对应 trigger 时才读取相关 section；GitHub Actions 等平台实现细节继续由对应平台 Skill 单点拥有。

## 1. Verification Contract Currentness

Trigger：验证失败、断言与当前 Requirement / Specification / Architecture 疑似不一致，或既有测试 / Workflow 可能已经陈旧。

规则：

- 验证产物只有与当前 Consumer Authority 一致时才定义有效 expected behavior；
- 验证失败时先区分 implementation defect、stale verification contract、runtime/environment problem 与 external dependency problem；
- 不因为测试或 Workflow 已存在就默认其断言高于当前 Requirement / Specification / Architecture；
- 如果验证契约已经陈旧，先回到其 semantic owner 修正，再重新取得 Current Evidence；
- 不通过修改产品实现去迎合已经失效的验证断言。

## 2. Visual Evidence

Trigger：Requirement 明确要求现网站点复刻、设计稿还原、品牌视觉一致性或其他视觉 fidelity。

规则：

- 浏览器功能验证可以证明路由、交互、资源加载和其他可机器判定行为，但不能单独证明视觉一致性；
- 视觉结论应按风险使用原始运行证据、参考截图、真实资源、AI 视觉对照和人工视觉复核；
- 除非 Requirement 已提供可机器判定的完整视觉容差契约，不得把“功能通过”扩大成“视觉通过”；
- 人工视觉复核可能暴露实现缺陷、产品歧义、Authority gap 或环境问题，必须按真实问题分类，不把所有发现静默压缩成纯视觉调整。

## 3. Human Review Baseline Isolation

Trigger：自动验证会修改数据库、文件、导航、缓存或其他共享状态，并且同一环境随后用于 Human Review。

规则：

- 先保留自动验证的 Current Evidence；
- Human Review 前从来源明确、可重复构建的 baseline 恢复环境；
- 只准备明确用于人工复核的示例数据；
- 自动测试后的残留状态不能静默成为 Human Review baseline；
- 自动验证状态与 Human Review baseline 可以具有不同生命周期和资源租约策略，具体实现服从 Consumer / platform policy。

## 4. Database Migration Completion Evidence

Trigger：当前变化包含数据库 schema / migration lifecycle，并且运行环境或 CI 条件允许取得完整初始化证据。

规则：

最终完成验证至少应覆盖一次：

```text
Fresh Database
→ Full Migration Chain
→ Application Startup
```

SQL 文件检查、编译、单元测试或只在已有数据库上执行增量 migration，不能单独证明新环境可初始化。

如果当前环境确实无法取得这类证据，应明确说明证据缺口和替代验证边界，不得把较弱证据描述为完整 migration completion evidence。

## 5. Evidence Claim Reuse Across Commits

Trigger：拟复用祖先提交上的 CI / Review / Runtime evidence 支持后继提交的 Current Evidence Claim。

规则：

只有同时满足以下条件，才可以按具体 claim 复用未受影响的祖先证据：

1. 能取得 ancestor evidence SHA 到 current target SHA 的精确差异；
2. 能逐项证明差异不会影响该 evidence claim；
3. 与该 claim 相关的 Authority / Requirement / Specification / Architecture / acceptance semantics 未改变；
4. Consumer Repository Policy 允许这种 claim-level reuse。

复用时必须记录 ancestor SHA、current SHA、差异范围和 claim mapping。

受影响或无法证明不受影响的 claim 必须重新取得定向验证或相应复核。祖先 Run 不得被描述为当前目标提交的 Run。

## 6. Evidence Type Must Match Claim

Trigger：任何 completion / pass / ready-to-integrate 结论。

规则：

- 实现存在、静态检查、历史 evidence 或只覆盖主路径的证据不能替代当前声明真正需要的完成证据；
- 快速反馈与 completion verification 可以分层，中间修复可以优先低成本定向验证，但最终声明仍必须满足完整必要证据；
- 诊断 / runtime observation 可以支持诊断、终止、改道或调整验证路径，但不能仅因同属“当前证据”就自动替代 completion evidence；
- 显式归属 feature-wide convergence 的验收义务保持待验证，必须由 `converge` 独立重新检查。

顶层 Evidence-before-claims Principle 仍由 `docs/method/principles.md` 拥有；本文只保存跨职责、按条件激活的证据类型约束。

## 7. Platform Boundary

当当前任务涉及 GitHub Actions trigger、gate、container/runtime reuse、artifact/log handling、timeout/cancellation 或平台成本 / observability 时，读取：

`skills/github-actions-verification/SKILL.md`

当临时 artifact / snapshot 被接受为长期稳定输入、异步外部操作或共享资源 lifecycle 成为问题时，读取：

`docs/guides/external-operation-guidelines.md`

本文不复制这些 owner 的详细过程。