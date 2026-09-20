---
id: guide:feature-development
type: guide
status: active
distribution: source-only
---

# Feature Development 使用指南

本文面向人类说明：当 Consumer 已经拥有足够稳定的 Requirement Baseline 与当前 Feature 所需的最小 Architecture Context 后，怎样使用 `agentic-dev` 完成一个普通 Feature / change，从意图澄清一路推进到 `Ready to Integrate`。

规范生命周期由 `method:ai-development` 持有；每个有界执行责任由对应 Skill 持有；条件性约束由 Rule 持有。本文只提供跨这些 canonical owners 的 Human View，不建立新的阶段、Gate、Approval 或 Execute Authority。

## 1. 什么时候进入 Feature Development

普通 Feature Development 不是新项目的起点。

进入 `method:ai-development` 前，至少应满足：

- 当前 Repository Authority 可以恢复；
- 当前 Feature 依赖的 Requirement / Domain facts 已有明确 owner；
- Goal、Scope、主要业务边界与 Acceptance 不需要重新做全项目需求分析；
- 当前 Feature 必需的 Architecture Context 已足够，或能够在 Feature 内安全处理局部、可逆的技术选择。

如果多个 Feature 同时被同一组长期 Requirement gap 阻塞，应返回 Requirement owner，必要时进入 `method:requirement-baseline-establishment`。

如果多个 Feature 共同依赖一个长期、高成本难逆的 systemic architecture driver，应返回 Architecture owner，必要时进入 `method:architecture-clarification`。

因此普通 Feature 的默认入口不是“先写代码”，而是：

```text
Current Repository / Requirement / Architecture Authority
        ↓
Clarify Intent
        ↓
Specification Ready
        ↓
Technical Planning? ── no ──┐
        │ yes                 │
        ↓                     │
Technical Plan Ready          │
        └──────────────┬──────┘
                       ↓
                 Slice Execution Units
                       ↓
                  Readiness Check
                       ↓
                     Execute
                 failure? → Debug
                       ↓
                 Unit Verification
                       ↓
                    Converge
                       ↓
              Ready to Integrate
                       ↓
          Repository / Human Authority
```

这只是人类操作视图；阶段身份、返回路径和完成语义仍以 `method:ai-development` 为准。

## 2. Clarify Intent：只解决真正影响结果的歧义

Clarify Intent 不重新分析整个项目，也不要求把所有实现问题都提前问清楚。

人类应重点判断：当前是否还有多个合理答案会实质改变以下内容：

- Goal；
- Scope；
- User-visible Behavior；
- Business Boundary；
- Acceptance；
- 重大非功能义务。

如果 Authority 已经可以唯一决定结果，就继续推进；如果只是局部、低影响、可逆 HOW，留给后续 Technical Planning 或 Execute。

如果发现的是长期 Requirement / Domain 缺口，不要只在当前 Feature 中补一句临时说明；应返回真实 owner。若发现的是 systemic architecture gap，也应返回 Architecture owner。

Clarify Intent 的目标不是“问得足够多”，而是确保进入 Specification 后，不再存在会改变当前 Feature WHAT / WHY 的关键未知。

## 3. Specification：把 WHAT / WHY 与 Acceptance 写清楚

Specification 是当前 Feature / change 的 WHAT / WHY Authority。

人类阅读 Specification 时，至少应该能回答：

- 为什么要做；
- 做什么；
- 明确不做什么；
- 用户或外部系统能观察到什么行为；
- 哪些业务规则适用于当前 change；
- 边界和失败行为是什么；
- 什么事实能够证明 change 已完成；
- 有哪些必要的非功能约束。

实现路径、文件名、类 / 函数、框架构造、施工顺序等 HOW 默认不属于 Specification。

一个简单判断是：

> 一个新的 Fresh Context 执行者，只读取当前 Authority 与 Specification，是否能够准确判断“要实现什么、什么不实现、怎样验收”？

如果答案是否定的，应先修复 Specification 或上游 Authority，而不是直接进入编码。

规范执行责任见 `skill:specify`。

## 4. Technical Planning：不是每个 Feature 都需要

Technical Planning 是条件阶段。

只有当实施前存在跨一个以上 Execution Unit 持续有价值、且必须先稳定的 HOW 时，才值得形成独立 Technical Plan，例如：

- 跨模块组件边界；
- shared contract；
- 核心数据结构；
- 外部集成；
- migration；
- deployment topology；
- 跨 Unit 测试策略；
- 重要、难逆的技术风险。

如果当前 Specification 可以安全映射到仓库已有模式，而剩余问题只是局部、可逆的实现细节，应跳过独立 Technical Plan，把这些选择留给 JIT Execution Plan。

不要为了“流程完整”强制产生 Technical Plan，也不要用 Technical Plan 重新定义产品行为。

如果 Technical Planning 暴露新的产品语义歧义，应返回 Specification / Requirement owner；如果暴露跨 Feature 长期架构变化，应更新真实 Architecture owner，必要时形成 ADR。

规范执行责任见 `skill:technical-plan`。

## 5. Slice & Ready：形成可独立执行的纵向单元

Ready Specification 与必要的 Technical Plan 确定后，再切 Execution Units。

一个好的 Execution Unit 应让新的 Fresh Context Agent 可以在有界上下文内完成：

```text
理解
→ 实现
→ 验证
```

因此每个 Unit 至少需要明确：

- Scope；
- Authority inputs；
- Dependencies；
- Completion Conditions；
- Verification responsibility；
- Out of Scope。

优先形成窄而完整的纵向单元，不要机械拆成：

```text
数据库 Unit
→ 后端 Unit
→ 前端 Unit
→ 测试 Unit
```

这种横向切分很容易让任何一个 Unit 都无法独立证明用户可观察结果，也容易把完成责任隐藏在多个 Unit 之间。

切分可以明确依赖顺序，但前一个 Unit Ready 或完成不自动授予后一个 Unit 的 Execute Authority。

规范执行责任见 `skill:slice-work`。

## 6. Readiness Check：Execute 前的只读门禁

Readiness Check 的职责是回答：

> 当前这个 Execution Unit 现在是否真的可以安全执行？

它应重新读取当前 Unit、Specification、必要 Technical Plan、Domain / Architecture / Repository Authority 与仓库事实，并检查：

- Authority 是否仍然有效；
- Scope 是否有歧义；
- Dependencies 是否满足；
- 必要技术决定是否已经关闭；
- Completion / Verification 定义是否足够；
- base drift 是否使原计划失效；
- 是否存在 artifact lifecycle、权限或治理 blocker。

Readiness 是**只读 Gate**。发现问题时应报告 finding、影响和真实责任层，然后返回相应 owner 修复；不要在 Readiness 内顺手修改 Specification、Plan、代码或配置。

`PASS` 只表示“当前 Unit 可以进入 Execute”，不代表已经完成，也不授予后续 Unit、merge、release 或 deploy 权限。

规范执行责任见 `skill:readiness-check`。

## 7. Execute：Fresh Context、JIT Plan 与 Rule Discovery

Execute 每次只处理一个 Ready Execution Unit。

开始时应重新读取：

- 当前 Unit；
- 直接 Authority；
- 当前代码 / runtime facts；
- 当前任务通过 Rule Discovery 发现的适用 Rules。

即使 Planning 已经充分，Execute 仍需要一个临时 JIT Execution Plan，用于决定当前代码库里的具体施工顺序。这个 plan 是执行时工作材料，不应因为存在步骤就自动晋升为长期 Technical Authority。

实现过程中：

- 正常施工按当前 Unit 边界连续推进；
- 意外 defect / unexpected failure 进入 `skill:systematic-debug`；
- 预期的 TDD 初始失败不等同于 defect；
- 如果实现暴露 Specification 或 Architecture 的真实缺口，应返回对应 owner，而不是在代码里静默定义新规则。

## 8. Completion Evidence：证明当前 Unit 真的完成

完成声明必须与当前 Unit 的 Completion Conditions 匹配。

不要用以下证据替代真实完成：

- “代码已经写完”；
- “能编译”；
- “静态检查通过”；
- “主路径页面能打开”；
- “历史上跑过一次”；
- “某个脚本成功退出”。

不同 Unit 需要的证据不同。正确的问题是：

> 哪些当前 Evidence 能够区分这个 Unit 的 Completion claim 到底是真的还是假的？

例如涉及权限、失败边界、数据迁移、视觉表现、外部系统或生产行为时，证据组合应覆盖对应风险，而不是套用一份固定的“所有项目最低测试清单”。

如果发现 defect，修复后应留下能够证明原 failure 已消失、必要邻接行为没有已知回归的 regression evidence。

具体 verification policy 由当前适用 Rule 与 Consumer Authority 决定。

## 9. Converge：不是再做一次测试

Converge 处理 Feature / change 整体收敛，必须区分三个不同问题：

- **Verification**：当前事实是否支持某个 claim；
- **Review**：实现本身是否安全、合理、符合约束；
- **Convergence**：Authority、最终实现与当前 Evidence 是否共同满足完整目标。

因此 Unit 都完成并不自动等于 Feature 已经收敛。

Converge 应检查：

- 当前 Specification 的 Acceptance 是否都得到实现与 Evidence 支撑；
- 多个 Unit 组合后是否出现新的边界冲突；
- 长期 Artifact responsibility 是否正确；
- 当前实现是否与 Requirement / Architecture 仍一致；
- 是否还有已知 blocker。

发现缺口时，应返回真实 owner：

```text
局部 Feature 缺口
→ 当前 Feature / Specification owner

系统性 Requirement gap
→ Requirement owner

systemic architecture gap
→ Architecture owner
```

不要在 Converge 中静默重设计，也不要通过降低 Acceptance 来让已有实现“看起来完成”。

只有 Authority、实现和当前 Evidence 一致且没有已知 blocker 时，才可以报告 `Ready to Integrate`。

规范责任见 `method:ai-development` 与 `skill:converge`。

## 10. Human Review 与独立复核放在哪里

Human Review 不是普通 Feature lifecycle 的固定新阶段。

当真实产品意图、长期高影响结构或高风险技术责任需要人工理解和判断时，可以按 `architecture:human-review` / `skill:human-review` 形成结构化 Review Draft，并把 durable decision 回写真正 owner。

独立 Repository change review 也不同于 Human Review：它检查拟集成 change 是否符合当前 Authority、Scope、Rule 与 Evidence，而不是重新定义产品意图。

两类 Review 都不自动授予 merge / release / deploy 权限。

如果当前 Repository Rule 要求高影响 change 进入 independent review，应按 Rule Discovery 的结果执行；不要因为本 Guide 提到了 Review 就把所有 Feature 都增加固定审批。

完整 Human Review 操作说明见 [`human-review.md`](human-review.md)。

## 11. Ready to Integrate 之后发生什么

`Ready to Integrate` 是 `method:ai-development` 的完成状态，不等于已经 merge。

后续 Git / GitHub 操作、PR、独立 Review、Human Integration Decision、merge、release、deploy 和 post-integration closure 都由目标 Repository 的治理与人工 Authority 决定。

因此不要把：

```text
Converge PASS
```

理解成：

```text
自动 merge
→ 自动 release
→ 自动 deploy
```

Feature Development Method 在 `Ready to Integrate` 边界停止。

## 12. 常见误用

### 误用 1：没有恢复 Authority 就开始写 Specification

后果是把聊天、猜测或旧实现当成产品事实。

正确做法：先恢复当前 Repository / Requirement / Domain / Architecture Authority，再判断当前 Feature 的真实 change。

### 误用 2：把 HOW 写进 Specification

例如提前写死类名、文件路径、框架构造和施工顺序。

正确做法：Specification 持有 WHAT / WHY / Acceptance；HOW 进入必要的 Technical Planning 或 Execute。

### 误用 3：每个 Feature 都建立长期 Technical Plan

后果是 planning artifact 膨胀，并把局部可逆施工选择永久化。

正确做法：Technical Planning 是条件阶段，只稳定跨 Unit 持续有价值、实施前必须解决的 HOW。

### 误用 4：按前端 / 后端 / DB / test 机械切 Unit

后果是责任横跨多个 Unit，Fresh Context 无法独立完成和验证。

正确做法：优先切 context-fit 的纵向单元。

### 误用 5：在 Readiness Check 中直接修问题

后果是只读 Gate 与修改责任混合，Finding 的真实 owner 被隐藏。

正确做法：Readiness 只报告 finding，并返回负责层修复后重新检查。

### 误用 6：用低强度证据替代 completion evidence

例如编译通过就声称业务功能完成。

正确做法：Evidence 必须能支持当前 Completion / Acceptance claim。

### 误用 7：Converge 时静默改变目标

后果是让实现反向改写 Authority。

正确做法：缺口返回真实 owner；Authority 修正后重新收敛。

### 误用 8：Unit 完成后自动开始下一 Unit

后果是依赖顺序被误当成 Execute Authority。

正确做法：当前 Unit 在自己的边界停止；下一 Unit 需要当前 Repository Authority 明确允许继续。

### 误用 9：Ready to Integrate 自动等于 merge

后果是 Method completion 与 Repository / Human integration authority 混在一起。

正确做法：进入目标仓库自己的 Integration Gate。

## 13. 人类如何观察一次健康的 Feature lifecycle

一个健康的普通 Feature 通常呈现为：

```text
1. 当前 Authority 能恢复
2. 关键产品意图无 blocker
3. Specification 可以由 Fresh Context 独立理解和验收
4. 只有真正需要时才形成 Technical Plan
5. Execution Units 边界窄、完整、可验证
6. 每个 Unit Execute 前重新通过 Readiness
7. Execute 使用当前代码事实和适用 Rules，而不是依赖旧聊天
8. Defect 有根因和 regression evidence
9. Completion Evidence 匹配实际 claim
10. Converge 后 Authority / implementation / Evidence 一致
11. Ready to Integrate 后停止，等待 Repository / Human integration authority
```

如果流程需要大量人工持续记忆、同一事实出现在多套文档中、每个阶段都产生固定新 Artifact，或任何“通过”状态都自动触发后续副作用，通常意味着责任边界已经开始漂移。

## 14. 规范性归属与推荐阅读

本文只做组合 Human View。需要核对规范语义时，应回到 canonical owner：

- Feature lifecycle：`docs/methods/ai-development.md`；
- Clarify Intent：`skills/clarify-intent/SKILL.md`；
- Specification：`skills/specify/SKILL.md`；
- Technical Planning：`skills/technical-plan/SKILL.md`；
- Slice：`skills/slice-work/SKILL.md`；
- Readiness：`skills/readiness-check/SKILL.md`；
- Execute：`skills/execute-unit/SKILL.md`；
- Debug：`skills/systematic-debug/SKILL.md`；
- Converge：`skills/converge/SKILL.md`；
- Human Review：`docs/architecture/human-review-architecture.md`、`skills/human-review/SKILL.md`；
- Rules / Rule Discovery：`docs/rules/README.md` 与对应 canonical Architecture / Tool contract；
- 项目总体 Human View：[`using-agentic-dev.md`](using-agentic-dev.md)。

若本文与这些 canonical owners 冲突，以 canonical owner 为准并修正本文。