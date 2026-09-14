---
id: method:ai-development
type: method
status: active
---

# AI Agent 驱动软件开发方法

## 1. 目标

本方法定义与语言、框架、Issue 系统和具体 Agent 产品无关的软件开发生命周期。它只拥有“工作处于什么状态、下一职责是什么、何时可以返回或前进”的长期语义；具体工程约束由 Rule 按任务发现，具体可复用执行闭环由 Skill 实现。

## 2. 生命周期

```text
Clarify Intent
→ Specification
→ Technical Planning? (conditional)
→ Slice & Ready
→ Execute
→ Converge
→ Ready to Integrate
→ repository / human authority
```

正式方法阶段只有六个：

1. Clarify Intent；
2. Specification；
3. Technical Planning（条件阶段）；
4. Slice & Ready；
5. Execute；
6. Converge。

Integration 不是通用方法阶段。merge、release、deploy 与其他外部副作用由目标仓库策略和人工权威决定。

## 3. Clarify Intent

解决会实质改变 Goal、Scope、User-visible Behavior、Business Boundary、Acceptance 或重大非功能义务的歧义。

优先从当前 Repository / Domain Authority 解析；普通、低影响、可逆实现选择不升级到产品意图层。

退出条件：不存在会显著改变目标、范围、产品行为或验收结果的关键未决问题。

对应 Skill：`clarify-intent`。

## 4. Specification

形成当前功能 WHAT / WHY Authority。至少覆盖：

- Goal；
- In Scope / Out of Scope；
- Observable Behavior；
- Business Rules；
- Boundary / Failure Behavior；
- Acceptance Criteria；
- 必要非功能约束。

Specification 不默认持有实现路径、类/函数、框架构造或施工顺序。

当确认的业务术语、不变量或跨功能规则需要独立于当前功能持续维护时，形成 Domain Authority Candidate，并按目标仓库权威决定是否提升。

退出条件：新的 Agent 只读取 Specification 与最小必要仓库上下文，即可判断做什么、不做什么、什么算完成，并且没有高影响歧义。

对应 Skill：`specify`。

## 5. Technical Planning

仅在 Specification 无法直接、安全映射到当前系统时进入，例如：跨模块、新数据模型、外部集成、迁移、共享契约、部署拓扑或重大架构权衡。

Technical Plan 只保存跨 Execution Unit 持续有协调价值的 HOW；精确文件、命令与编辑顺序属于临时 JIT Execution Plan。

技术决定若会跨当前功能长期约束后续工作，应更新真实 Architecture Context；只有决定背景、主要权衡或替代关系具有长期价值时才形成/更新 ADR。

退出条件：实施前必须解决的技术不确定性已关闭，长期 Architecture / ADR 责任已进入正确 owner；或已经确认无需独立 Technical Planning。

对应 Skill：`technical-plan`。

## 6. Slice & Ready

把 Ready Specification 与必要 Technical Plan 切为 context-fit Execution Units。

每个 Unit 必须：

- 边界明确；
- 尽量纵向并形成可观察行为；
- 可独立实现和验证；
- 明确 Authority inputs、Dependencies、Out of Scope、Completion Conditions 与 Verification responsibility；
- 能由一个 Fresh Context Agent 完成理解、实现与验证。

`slice-work` 形成 Units；`readiness-check` 在 Execute 前执行只读门禁。Readiness PASS 不自动授予后续 Unit、merge、release 或 deploy 权限。

## 7. Execute

每次只执行一个 Ready Execution Unit。

执行上下文必须重新读取当前 Unit、直接 Authority 与代码事实，形成临时 JIT Execution Plan，并通过 Rule Discovery 加载当前任务真正适用的 generation / verification / operations / repository / technology Rules。

意外失败进入 `systematic-debug`；预期 TDD 初始失败不等同于 defect。

完成声明必须由与 Unit Completion Conditions 匹配的当前证据支持。Execute 停在 Unit 边界，不自动进入下一 Unit 或 Integration。

对应 Skill：`execute-unit`；异常诊断 Skill：`systematic-debug`。

## 8. Converge

在功能/变更范围内对当前 Authority、最终实现与当前 Evidence 做整体收敛。

Converge 必须区分：

- Verification：当前事实是否满足 claim；
- Review：实现本身是否安全、合理、符合约束；
- Convergence：整个目标是否与权威意图、长期 artifact responsibility 和当前证据一致。

发现缺口时返回拥有该责任的上游层，不在 Converge 中静默重设计。

退出条件：不存在已知阻塞缺口，Authority、实现和当前证据一致，可报告 `Ready to Integrate`。

对应 Skill：`converge`。高影响变更是否需要独立 review，由当前 Repository Rule 发现并触发 `review-change`。

## 9. Fresh Context 与渐进式披露

Fresh Context 是逻辑属性：当前执行者不依赖此前未持久化推理历史。可以由新聊天、子 Agent、新 CLI 会话或其他隔离执行者实现。

普通上下文只加载：

- Repository Authority；
- 当前工作对象；
- 直接相关 Specification / Technical / Architecture / Domain Authority；
- Rule Discovery 返回的少量候选正文；
- 当前需要的 Skill；
- 相关代码、测试与当前 Evidence。

不得为了“完整”预加载全量 Rules、全量 Skill、完整 Research 或历史项目记录。

## 10. Rule Discovery

Rule 不是方法阶段，也不是 Skill。它是执行工作时必须遵守的条件、约束、默认值、不变量或完成声明要求。

Rule Discovery 的规范架构见 `docs/architecture/rule-discovery-architecture.md`：工具只扫描 Rule 自身 Front Matter，确定性返回少量 locator；LLM 读取候选正文后做最终语义适用性确认。

目录分类不参与匹配，不维护中心 Rule Map / Manifest / Catalog。

## 11. Artifact lifecycle

长期知识只进入真实 semantic owner；会话推理、临时探索、JIT 施工计划和阶段流水账默认不持久化。

典型长期 owner 包括：

- Repository / Domain Authority；
- Method / Architecture；
- ADR；
- Specification；
- 必要 Technical Plan；
- Rule；
- Skill；
- code / tests；
- 需要跨阶段恢复的 Project Roadmap。

已有长期 artifact 被新结论取代时，应更新或删除 current owner；历史由 Git / Issue / PR 保存，不通过旧 Markdown 兼容层维持。

## 12. Human escalation

Agent 默认自主处理局部、低影响、可逆且不改变外部可观察产品行为的执行判断。

以下情况需要按目标仓库权威升级：

- 改变产品意图或范围；
- 多种选择产生实质不同的用户可见行为；
- 权威来源冲突；
- 重大架构方向或高成本难逆权衡；
- 安全、隐私或不可逆数据风险；
- 超出授权的共享 / 生产 / 外部副作用；
- merge、release、deploy 或 destructive remote operation 被仓库策略保留给人工。

核心原则：人工负责不可逆的意图与授权决策；AI 负责授权范围内可逆的执行判断。