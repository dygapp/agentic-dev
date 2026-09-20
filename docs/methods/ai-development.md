---
id: method:ai-development
type: method
status: active
distribution: release-input
release-target: software-development
---

# AI Agent 驱动软件开发方法

## 1. 目标

本方法定义与语言、框架、Issue 系统和具体 Agent 产品无关的 **Feature / change 从意图澄清到 `Ready to Integrate` 的 AI 驱动开发生命周期**。它只拥有“工作处于什么状态、下一职责是什么、何时可以返回或前进”的长期语义；具体工程约束由 Rule 按任务发现，具体可复用执行闭环由 Skill 实现。

本方法面向**具体 Feature / change**。进入本方法的前提是：当前 Repository 已存在足以支持本次 Feature 判断 Goal、Scope、Observable Behavior 与 Acceptance 的 Requirement Baseline，以及当前 Feature 真正需要的最小 Architecture Context。

如果项目尚无可靠 Requirement Baseline，或多个当前 / 预期 Feature 共同被系统性 Requirement gap / conflict / ownership failure 阻塞，不应在当前 Feature 内局部创造长期事实；目标 Repository 应返回真实 Requirement owner，或在 local Method selector 已采用并命中相应 work kind 时进入 `method:requirement-baseline-establishment`。

如果 Requirement Baseline 已足够，但多个当前 / 预期 Feature 共同依赖一个尚未解决、长期、高成本难逆并阻塞可靠开发的 architecture driver，则返回真实 Architecture owner，或在 local selector 已采用并命中相应 work kind 时进入 `method:architecture-clarification`。

upstream Source capability 存在本身不构成 Consumer runtime 能力；只有已安装 Release 与 Consumer-local Authority 才定义 Consumer 当前可用能力。

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

Integration 不是通用方法阶段。merge 是否发生继续由目标仓库策略和人工权威决定；release、deployment、production operations、incident response 与 service retirement 属于 Consumer-local lifecycle，不作为本 Method 为了“完整”而补建的后续阶段。

### 2.1 稳定阶段身份

当 Rule Discovery 或其他 runtime contract 需要稳定机器身份时，本 Method 对六个阶段定义以下 canonical phase token：

- Clarify Intent → `clarify-intent`；
- Specification → `specification`；
- Technical Planning → `technical-planning`；
- Slice & Ready → `slice-ready`；
- Execute → `execute`；
- Converge → `converge`。

这些 token 只属于 `method:ai-development` 的 phase identity，不是所有 Method 的全局阶段词表。其他 Method 必须由自己的 canonical owner 决定是否定义以及如何定义 phase identity。

## 3. Clarify Intent

解决会实质改变 Goal、Scope、User-visible Behavior、Business Boundary、Acceptance 或重大非功能义务的当前 Feature 歧义。

优先从当前 Repository / Requirement / Domain / Architecture Authority 解析；普通、低影响、可逆的实现选择不升级到产品意图层。

如果当前歧义只影响本 Feature，且长期 owner 明确，则返回并更新该 owner，解决后恢复当前 Feature。

如果发现问题实际属于：

- 多个 Feature 共同依赖的长期 Requirement fact / domain object / lifecycle / terminology / product boundary 缺失、冲突或 owner 不足 → 返回真实 Requirement owner；必要时进入 `method:requirement-baseline-establishment`；
- 多个 Feature 共同依赖的长期 architecture driver → 返回真实 Architecture owner；必要时进入 `method:architecture-clarification`。

不要在当前 Specification 中创建新的项目级 Requirement 或 Architecture 事实。

退出条件：不存在会显著改变目标、范围、产品行为或验收结果的关键未决问题，并且当前 Feature 所依赖的长期 Context 足以继续 Specification。

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

Specification 不默认持有实现路径、类/函数、框架构造或施工顺序，也不为了“自包含”复制完整的 project-level Requirement / Domain Authority。跨多个 Feature 持续成立的长期事实由真实 Requirement / Domain owner 持有；Specification 只拥有当前 change 对这些事实的具体适用、范围、可观察行为与验收。

当当前 Feature 确认的新业务术语、不变量或规则需要跨多个 Feature 长期维护时，形成长期 Authority Candidate，并按目标仓库权威提升并回写到真实 Requirement / Domain owner，而不是永久留在当前 Specification 中成为隐藏项目基线。

当 Specification 新增或实质改变用户可见行为、主要业务流程、失败语义、验收结果，或者同一 Requirement 可以形成多个合理的可观察行为时，应根据 Consumer 当前权威判断是否进入人工评审。Consumer 已采用 `architecture:human-review` 与 `skill:human-review` 时，可以调用该 Skill 生成结构化 Markdown 评审草稿，并把语义反馈回写当前 Specification 或正确的上游 owner。

普通、直接、无歧义地投影既有 Requirement 的 Specification 不要求固定人工审批。`skill:human-review` 的存在本身也不改变本阶段的进入或退出条件。

退出条件：新的 Agent 只读取 Specification 与最小必要的 Requirement / Domain / Architecture Context，即可判断做什么、不做什么、什么算完成，并且没有高影响歧义。

对应 Skill：`specify`。

## 5. Technical Planning

仅在 Specification 无法直接、安全映射到当前系统时进入，例如：跨模块、新数据模型、外部集成、迁移、共享契约、部署拓扑或重大架构权衡。

Technical Plan 只保存跨 Execution Unit 持续有协调价值的 HOW；精确文件、命令与编辑顺序属于临时 JIT Execution Plan。

技术决定若会跨当前功能长期约束后续工作，应更新真实 Architecture Context；只有决定背景、主要权衡或替代关系具有长期价值时才形成 / 更新 ADR。

单个 Feature 中会影响 Architecture 的 HOW 仍属于本阶段。只有当 Technical Planning 发现一个尚未解决的长期 architecture driver 已经超出当前 Feature，并且多个当前或预期 Feature 在进入可靠 Specification / Planning 前共同依赖它时，才升级到 `method:architecture-clarification` 所拥有的 work kind。二者必须更新同一个长期 Architecture owner，不形成平行 Authority。

当当前 change 涉及 legacy / historical / business data migration，且 Consumer 已采用 `architecture:data-migration` 或等价 local Architecture 时，Technical Planning 应按该 Architecture 解析 source role、semantic preservation、identity / duplicate、replay / idempotency、exception disposition 与 reconciliation responsibility；不得把 legacy source 或 migration mapping 反向当成新的 Requirement Authority。数据库 schema / initialization migration 仍由对应 Technical / Rule contract 处理，不因为名称中同样包含 migration 就自动进入该 Architecture。

当 Technical Planning 涉及不可逆或高风险数据迁移、对外或跨团队共享接口的重大改变、生产部署 / 回滚 / 安全边界的重大影响，或会改变已经承诺的稳定兼容边界时，应按 Consumer 当前 Authority 升级人工决定或人工评审。已采用 `skill:human-review` 的 Consumer 可以用它准备结构化 Markdown 评审草稿；人工确认形成的长期架构事实仍必须回写真实 Architecture owner，Feature Technical Plan 不获得平行长期所有权。

普通局部、易逆且不改变外部承诺的实现 HOW 继续由 AI 自主处理，不因为存在人工评审能力而自动增加人工门禁。

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

在功能 / 变更范围内对当前 Authority、最终实现与当前 Evidence 做整体收敛。

Converge 必须区分：

- Verification：当前事实是否满足 claim；
- Review：实现本身是否安全、合理、符合约束；
- Convergence：整个目标是否与权威意图、长期 artifact responsibility 和当前证据一致。

发现缺口时返回拥有该责任的上游层，不在 Converge 中静默重设计：

- 局部 Feature 缺口 → 当前 Feature owner；
- 系统性 Requirement Baseline gap → Requirement owner / `method:requirement-baseline-establishment`；
- systemic architecture gap → Architecture owner / `method:architecture-clarification`。

对于采用 `architecture:data-migration` 或等价 local Architecture 的 legacy / historical / business data migration，Converge 还必须确认 completion evidence 与当前 Acceptance 对齐，至少不会以“脚本执行成功”替代必要的 source / scope coverage、semantic check、exception / conflict disposition、provenance 或 target-side observable verification；具体证据组合仍由当前风险和 Consumer Authority 决定。

不把 Converge 变成项目级需求或架构重建阶段。

退出条件：不存在已知阻塞缺口，Authority、实现和当前证据一致，可报告 `Ready to Integrate`。

对应 Skill：`converge`。高影响变更是否需要独立 review，由当前 Repository Rule 发现并触发 `review-change`。

## 9. Fresh Context 与渐进式披露

Fresh Context 是逻辑属性：当前执行者不依赖此前未持久化推理历史。可以由新聊天、子 Agent、新 CLI 会话或其他隔离执行者实现。

普通上下文只加载：

- Repository Authority；
- 当前工作对象；
- Requirement Authority Index / 当前 Feature 直接相关 Requirement owner（如果 Consumer 建立了该结构或等价入口）；
- 直接相关 Specification / Technical / Architecture / Domain / Project Authority；
- Rule Discovery 返回的少量候选正文；
- 当前需要的 Skill；
- 相关代码、测试与当前 Evidence。

不得为了“完整”预加载全量 Requirements、全量 Rules、全量 Skill、完整 Research 或历史 Project Evolution。

## 10. Rule Discovery

Rule 不是方法阶段，也不是 Skill。它是执行工作时必须遵守的条件、约束、默认值、不变量或完成声明要求。

Rule Discovery 的规范架构见 `docs/architecture/rule-discovery-architecture.md`：工具只扫描 Rule 自身 Front Matter，确定性返回少量 locator；LLM 读取候选正文后做最终语义适用性确认。

本 Method 的 stable phase identities 由 §2.1 持有；Rule Discovery 只能消费这些 identity，不反向拥有或定义它们。

目录分类不参与匹配，不维护中心 Rule Map / Manifest / Catalog。

## 11. 产物生命周期

长期知识只进入真实 semantic owner；会话推理、临时探索、JIT 施工计划和阶段流水账默认不持久化。

典型长期 owner 包括：

- Repository / Requirement / Domain / Project Authority；
- Architecture Context；
- Method / Architecture；
- ADR；
- Specification；
- 必要 Technical Plan；
- Rule；
- Skill；
- code / tests；
- 需要跨上下文恢复的 Project Charter / Capability Profile / Roadmap / Evolution 等项目知识。

Requirement Authority 的通用 ownership / index / Human navigation contract 见 `architecture:requirement-authority`。跨需求、功能规格、架构与技术方案通用的人工评审草稿、派生视图、反馈分类与显式交付边界由 `architecture:human-review` 定义。Project Knowledge 的最小职责与持久化边界由 `docs/architecture/project-knowledge-architecture.md` 定义；并非每个项目都必须使用相同物理文件名。

已有长期 artifact 被新结论取代时，应更新或删除 current owner；历史由 Git / Issue / PR 保存，不通过旧 Markdown 兼容层维持。

## 12. 人工升级

Agent 默认自主处理局部、低影响、可逆且不改变外部可观察产品行为的执行判断。

以下情况需要按目标仓库权威升级：

- 改变产品意图或范围；
- 多种选择产生实质不同的用户可见行为；
- 权威来源冲突；
- 重大架构方向或高成本难逆权衡；
- 安全、隐私或不可逆数据风险；
- 超出授权的共享 / 生产 / 外部副作用；
- merge、release、deploy 或 destructive remote operation 被仓库策略保留给人工。

人工升级负责判断“什么必须由人决定”；人工评审负责在需要时把当前权威内容整理成便于判断的结构化材料，并把人工反馈正确回写。两者不是新的 Method 阶段，也不要求每次人工升级都生成正式评审包。

Consumer 已采用 `skill:human-review` 时，可以在当前责任需要人工集中确认或人工明确要求评审材料时调用。默认只生成结构化 Markdown 评审草稿；最终 DOCX、HTML 等交付格式只有在明确请求后才进入后续交付处理。

核心原则：人工负责不可逆的意图与授权决策；AI 负责授权范围内可逆的执行判断。