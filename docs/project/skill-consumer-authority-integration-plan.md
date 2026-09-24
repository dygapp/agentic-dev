---
id: project:skill-consumer-authority-integration-plan
type: project
status: active
---

# 演进事项 1 — Skill 与 Consumer 项目权威适配方案

## 1. 目的与当前状态

本文是 post-v0.1.0-consumer-feedback-evolution-plan.md 中“演进事项 1 — Skill 与项目权威的适配边界”的当前方案 owner。

本事项来源于真实 Consumer 在引入独立 Visual Design Authority（当前实例为 DESIGN.md）后暴露的适配问题。当前方案不把 DESIGN.md、Visual Design 或任何具体目录提升为 Provider 标准，而是解决更一般的问题：

> 当 Consumer 在现有 Requirement / Specification / Architecture / Technical 之外拥有新的合法 Current Authority 时，Agent 在使用 canonical Skills 完成开发责任的过程中，怎样按需解析、消费、传递、验证并把长期语义返回真实 owner。

当前阶段：

- 证据重新分析：已完成；
- 必要外部研究：已完成到足以支持本方案；
- 方案收敛：本文冻结第一版实施边界；
- canonical Skill / Guide 具体实现：尚未开始；
- 实现前交叉模型评审：计划使用 GPT-6 Sol；评审不是计划成立或推进的硬 Gate，是否跳过由 Human Authority 明确决定；
- 最终高影响变更在集成决策前仍必须按 Provider governance 执行 Fresh / Independent Review。

本轮方案分析基于 master@308c9d4d2b5a344fa18a976f25da6cc14123524f 重新核验；后续实施仍需重新读取届时 exact HEAD。

## 2. Evidence 重新解释

### 2.1 已被当前产品模型消除的问题

Issue #58 反馈中与旧 Method selector、Rule Discovery、Capability Runtime 直接相关的缺口已经随 v0.1.0 产品边界切换退出 Current design，不恢复这些机制。

P4 已验证 Consumer-local Constraints / Policies 的最小发现模型：

~~~text
repository-wide stable policy
→ root AGENTS.md

path / module scoped policy
→ nested AGENTS.md / host-native scoped instructions

activity / semantic scoped policy
→ Consumer-local policy docs + thin locator
~~~

因此本事项不重新设计 Rule Discovery、constraint metadata 或中央 registry。

### 2.2 仍然存在的通用问题

真实 Consumer Evidence 证明：Consumer 可以新增一个独立、长期有效、会直接约束实现与验收的 Current Authority，而 Provider 不应预先知道它的类型。

当前 canonical Skills 已经存在“直接 Authority”“Authority inputs”“真实 owner”等开放表达，但多个关键位置仍把 Requirement / Specification / Architecture / Technical 等名称写成事实上的封闭集合。例如：

- slice-work 的输入与提取过程仍主要从 Specification / Technical Plan / Architecture decisions 出发；
- readiness-check 的输入与验证 contract 固定列举 Domain / Architecture / Requirement / Specification；
- execute-unit 的直接 Authority 固定列举 Specification / Technical / Architecture；
- systematic-debug 用固定三类 Authority 定义 expected behavior；
- converge 的输入和最终验证 contract 固定列举 Specification / Domain / Architecture；
- review-change 的 expected-behavior contract 固定列举 Requirement / Specification / Architecture；
- human-review 的输入、反馈提升与说明文字把长期语义 owner 写成需求、功能规格、架构或技术方案的封闭集合。

这会导致 Consumer 新增 Visual Design、Security、Accessibility、独立 Terminology 或其他合法语义 owner 时，Agent 即使能从 Repository 导航到文件，也不能保证该 Authority 真正进入 Skill 的 correctness / readiness / verification / writeback contract。

### 2.3 Consumer-local 与 Provider 通用责任

Consumer 始终拥有：

- Current Authority 的正文与 semantic owner；
- Authority 的物理组织方式；
- Repository / project knowledge entry 与 locator；
- 某类 Authority 是否存在、何时适用以及 Authority 之间的项目级优先级 / 冲突语义；
- Consumer-local Constraints / Policies。

Provider 只拥有：

- Agent 使用 Skill 时怎样消费“当前责任实际适用的 Authority”的通用 contract；
- Guide 中怎样解释责任导航、bounded context 与跨 Fresh Context 恢复；
- canonical Skills 不把已知 Authority 名称误写成封闭类型系统的通用语义。

## 3. 核心运行模型

本事项冻结以下概念关系。

1. **Agent 是执行主体**：负责恢复 Repository Context、判断责任、选择 / 执行 Skill、解析当前责任适用的 Authority 与 Constraint、取得 Evidence，并在授权范围内完成回写。
2. **Skill 是 procedure / contract**：定义某类责任的 Trigger、Inputs、Procedure、Outputs、Exit 与 Escalation；Skill 本身不是主动“发现”项目事实的主体。
3. **Consumer Current Authority 是当前事实与长期语义 owner**：回答“当前什么事实、contract、设计或决定是正确的”。Authority 集合由 Consumer 自己拥有并允许扩展。
4. **Consumer-local Constraint / Policy 是执行约束**：回答“在这个项目里做这件事还必须遵守什么”。它与 Current Authority 是两条独立输入通道。
5. **Guide 是责任导航**：帮助人和 Agent 判断“当前是什么责任、下一步做什么、应进入哪个 Skill”，不复制 Skill procedure。
6. **Execution Unit 是跨 Fresh Context 的有界执行责任载体**：保存足以恢复 Scope、Authority inputs、Dependencies、Completion Conditions 与 Verification responsibility 的信息，不依赖隐藏聊天历史。

同一物理文件可以包含不同责任内容，但文件名和目录名不自动决定 semantic ownership。例如“术语的正式业务含义”可能属于 Domain Authority，而“同一概念统一采用哪种写法”通常属于 Consumer-local language policy。

## 4. Authority 与 Constraint 的双通道

本事项不得把 Current Authority 与 Consumer-local Constraint 合并成一个新的 Rule / Authority 类型系统。

~~~text
Current Authority
→ 当前什么事实、contract、设计或决定是正确的？

Consumer-local Constraint / Policy
→ 执行当前工作时还必须遵守什么？
~~~

二者都遵守 bounded context / progressive disclosure：

- 只在当前责任需要时恢复；
- verified no-match 正常继续；
- 对 correctness 有实质影响但 applicability / owner / locator 无法可靠恢复时 fail closed 或返回真实责任层；
- 不默认枚举或全量加载 Consumer 项目知识。

## 5. Agent 的两阶段解析

### 5.1 Responsibility Routing

Skill 选择前，Agent 只恢复判断当前责任所需的最小上下文：

~~~text
User Request / Current Work
+ minimal Repository Context
+ installed Skill descriptions
→ Agent 判断当前责任
→ 选择 Skill / Guide
~~~

该阶段不要求先加载全部 Requirement、Architecture、Design、Security 等项目 Authority。

### 5.2 Responsibility Execution

责任和 Skill 确定后，Agent 按 Skill contract 进一步解析：

~~~text
Selected Skill
+ Consumer Repository Authority entry
→ 当前责任实际适用的 Current Authority
+ 当前任务适用的 Consumer-local Constraints
→ 最小必要上下文
→ execute / verify / review
→ durable semantic change 返回真实 owner
~~~

因此正式表述使用“Agent 解析 / 恢复适用 Authority”“Skill 消费 Authority 的 contract”，不再使用“Skill 主动发现 Authority”。

## 6. 可扩展 Authority 模型

Provider 不维护固定 Authority 枚举。

Requirement、Specification、Architecture、Visual Design、Security、Accessibility、Terminology 等都只能作为真实 Consumer 中可能存在的语义 owner 示例。

本事项只建立**开放接入机制**，不建立统一专项 Authority procedure：

- clarify-architecture 继续只负责 systemic Architecture driver；
- establish-requirement-baseline 继续只负责 Requirement Baseline；
- technical-plan 继续只负责跨 Execution Unit 持续有价值的 HOW；
- 新的 Consumer Authority 能被现有流程消费，不代表 Provider 必须提供同名 authoring Skill；
- 只有未来 Evidence 证明某类 Authority 的维护具有稳定 trigger、inputs、可重复 procedure、outputs、exit / escalation 与跨 Consumer 价值时，才单独评估新 Skill。

## 7. 生命周期集成

### 7.1 上游澄清与 Specification

clarify-intent / specify 可以识别“当前责任依赖某个已存在的 Consumer Current Authority”或发现其缺口，但不得因为 Provider 没有同名 Skill 就把该语义吸收到 Requirement / Specification。

WHAT / WHY / Observable Behavior / Acceptance 仍属于 Specification；专项 presentation、security、accessibility 等长期语义只有在 Consumer 已建立对应 owner 时才返回该 owner。

### 7.2 slice-work

slice-work 是跨 Fresh Context 传播的关键桥梁：

- 从当前责任实际适用的 Authority 中提取实现与验证义务；
- 每个 Execution Unit 保留明确的 Authority inputs 或等价 Current locator；
- Unit 不复制 Authority 正文；
- 不把一次规划时的路径永久视为 Current truth。

### 7.3 readiness-check

在 Execute 前重新从 Unit 的 Authority inputs 与当前 Repository 解析适用 Current Authority：

- 检查 owner / locator / currentness / drift；
- readiness 与 verification contract 必须覆盖实际适用 Authority；
- 其他 Consumer Authority 缺口返回其真实 owner / Consumer-local procedure，而不是强行映射到 specify、clarify-architecture 或 technical-plan。

### 7.4 execute-unit

Agent 执行 Unit 时：

- 重新读取 Unit 与当前适用 Authority；
- Authority 进入 implementation correctness 与 Completion Conditions 的判断依据；
- 不能把“读过某文档”误当成 Authority 已激活；
- 实现暴露新的长期语义缺口时返回真实 owner，不由 execution 临时发明。

### 7.5 systematic-debug

Expected behavior 必须来自当前 defect / failure 实际适用的 Current Authority；Requirement / Specification / Architecture 只是常见来源，不是封闭集合。

### 7.6 converge / review-change

最终 readiness / review claim 必须覆盖当前变更实际适用的 Current Authority。Provider 未预先命名某类 Consumer Authority，不能成为忽略它的理由。

### 7.7 human-review

人工评审：

- 读取当前评审目标直接需要的真实 semantic owners；
- 人工确认产生的长期语义必须返回真正 owner；
- Requirement / Specification / Architecture / Technical 作为常见例子，而不是长期 owner 的封闭集合。

## 8. 计划修改范围

### 8.1 Architecture contract

修改 docs/architecture/skill-architecture.md：

- 固化第 3 节的六个核心运行角色；
- 建立 Consumer Authority resolution / Skill consumption contract；
- 明确 Authority 与 Constraint 双通道；
- 明确开放 Authority 集合不等于统一 authoring Skill。

### 8.2 Guides

按“一个 canonical owner + 场景投影”原则调整：

- docs/guides/using-agentic-dev.md：作为用户理解核心运行模型的主要 Guide；
- docs/guides/feature-development.md：说明 Authority 如何经过 planning / slicing / Fresh Context execution 传播和重新解析；
- docs/guides/choosing-next-step.md：明确 Agent 是责任判断主体，Guide 只做导航；Consumer 可存在其他适用 Authority；
- docs/guides/getting-started.md：Bootstrap 只要求建立可恢复的 Consumer project-knowledge / Authority entry，不规定 Authority 类型或目录；
- docs/guides/consumer-local-constraints.md：明确 Authority 与 Constraint 的语义边界；
- docs/guides/human-review.md：与 human-review Skill 保持开放 owner 表述。

Guide 不复制完整 Skill procedure。

### 8.3 Canonical Skills

第一组直接修改对象：

- slice-work
- readiness-check
- execute-unit
- systematic-debug
- converge
- review-change
- human-review

这些 Skill 都跨多个语义 owner 工作，必须把固定 Authority 列举改为“当前责任实际适用的 Consumer Current Authority”，同时保留常见类型作为非穷举例子。

第二组只做边界复核，只有实际存在 closed-set 假设才修改：

- clarify-intent
- specify
- technical-plan

以下专项 owner Skill 默认不因本事项泛化：

- establish-requirement-baseline
- clarify-architecture

以下支持性 Skill 只有直接 contract 被影响时才修改，不为了表面对称扩大范围：

- external-operation
- github-actions-verification
- activate-model-collaboration

## 9. 验证方案

### 9.1 Deterministic contract tests

扩展 tests/test_repository_contracts.py，至少验证：

- canonical Skills / Guides 不把 Consumer Current Authority 限定为固定的 Requirement / Specification / Architecture / Technical 枚举；
- Architecture contract 明确 Agent / Skill / Guide / Authority / Constraint / Execution Unit 的职责；
- Authority 与 Constraint 保持独立；
- 不新增 Authority registry、metadata schema、Rule Discovery 或 Design-specific runtime。

测试避免通过关键词数量实现脆弱的 prose snapshot；只验证真正需要长期保持的 contract。

### 9.2 Bounded Consumer fixture

新增或扩展最小 fixture，使用 Provider 未硬编码的名称，例如 Presentation Authority，验证：

1. Consumer 可以通过自己的 Repository entry 声明该 owner；
2. presentation-related Unit 能把它作为 Authority input；
3. readiness-check 需要确认它 current；
4. execute-unit 的 correctness 必须受它约束；
5. 实现违反它时，converge / review-change 不能仅凭功能测试报告 READY / PASS；
6. human-review 的长期 presentation feedback 返回该 owner；
7. 非 presentation task 不加载该 Authority；
8. locator broken / applicability uncertain 且会影响 correctness 时 fail closed；
9. Provider fixture / Skill 中不硬编码 Presentation / Design 类型才能通过。

第 7、8、9 项是防止重新形成全量加载、文件名猜测和新的固定枚举的负向控制。

### 9.3 真实 Consumer applicability

只有 Provider deterministic fixture 已证明 contract 后，才对 dygapp/jilinjobs-cms 做只读或最低必要 applicability challenge：

- DESIGN.md 仅作为真实开放 Authority 样本；
- 不要求 Consumer 按 Provider 新目录重构；
- 不把 Consumer 当前临时 locator 直接提升为 Provider 标准；
- 只验证新的通用 contract 能否解释并支持该项目的真实 visual responsibility。

## 10. 非目标与负向约束

本事项明确不做：

- 不新增 Design 专用 Skill；
- 不新增 clarify-specialized-authority 之类的大一统专项 Skill；
- 不建立 Authority Registry / Catalog；
- 不建立固定 Authority enum / metadata schema；
- 不恢复 Method selector、Rule Discovery 或 Capability Runtime；
- 不把 DESIGN.md 或 docs/design/ 规定为 Consumer 标准；
- 不把 Design 合并进 Requirement / Architecture / Technical Plan；
- 不把 Current Authority 与 Consumer-local Constraint 合并；
- 不要求 Bootstrap 全量加载所有 Authority；
- 不为未知未来 Authority 预埋 Provider-specific framework；
- 不把一次 Consumer workaround 直接复制为通用机制。

## 11. 实现顺序

实现只在方案评审或 Human Authority 明确允许继续后开始：

1. 先修改 skill-architecture.md，冻结核心运行模型与 Authority consumption contract；
2. 同步 Guides，使用户心智模型和 Feature lifecycle 与 contract 一致；
3. 修改第一组横向 canonical Skills；
4. 复核第二组 / 支持性 Skills，仅在真实 closed-set gap 存在时修改；
5. 增加 deterministic tests 与 bounded fixture；
6. 运行 focused deterministic validation；
7. 如 claim 需要，执行 jilinjobs-cms applicability challenge；
8. 对最终 exact candidate 执行 Fresh / Independent Review；
9. 只有 review claim、Evidence 与 Human integration authority 都满足后再进入集成。

## 12. GPT-6 Sol 实现前交叉评审

在步骤 1 的具体实现前，优先使用 GPT-6 Sol 对本文方案做一次独立评审。评审应重新读取：

- 当前 AGENTS.md；
- project-roadmap.md；
- post-v0.1.0-consumer-feedback-evolution-plan.md；
- 本方案；
- skill-architecture.md；
- 本方案列出的直接 Skill / Guide；
- Issue #58 当前 Evidence 与必要 Consumer 证据。

评审重点：

- 是否错误扩大了 Provider 对 Consumer Authority 的 ownership；
- Authority / Constraint 边界是否仍清楚；
- Agent / Skill 主体关系是否正确；
- 是否存在隐含固定 Authority taxonomy；
- Execution Unit 是否承担了不应有的 Authority ownership；
- 是否遗漏现有 Skill lifecycle 中的关键消费 / writeback 点；
- fixture / negative control 是否足以区分真正泛化与 Design-specific hardcoding；
- 是否可以进一步减小修改面。

期望输出：

- Blocking / Medium / Low findings；
- 必要修改建议；
- 对“可以进入实现 / 建议先修订方案”的明确判断。

该交叉模型评审是质量增强措施，不成为本计划成立或 Roadmap 推进的强制 Gate。若当前 GPT-6 Sol 周额度、Runtime 或调用路径不可用，由 Human Authority 明确决定等待、跳过或改用其他独立评审路径。无论是否执行该增强评审，最终高影响 canonical Skill contract 变化仍必须满足 review-and-verification.md 的 Fresh / Independent Review 要求。

## 13. 方案完成条件

本方案阶段完成的判据是：

- 核心问题已经从 Design-specific 缺口提升为开放 Consumer Authority integration 问题；
- Agent / Skill / Guide / Authority / Constraint / Execution Unit 的责任明确；
- Authority 与 Constraint 双通道明确；
- Consumer ownership 与 Provider contract 边界明确；
- Skill / Guide 修改面已按 current baseline 分类；
- 验证、负向控制、真实 Consumer Evidence 使用边界明确；
- 实现前 GPT-6 Sol 评审路径与非阻塞属性明确；
- 未开始 canonical Skill / Guide 具体实现。
