# Engineering Capability Foundation v1 收敛路线

## 1. 目的

本文定义 `agentic-dev` 当前 **Engineering Capability Foundation v1（工程能力基础版 v1）** 的有限里程碑范围、实施步骤、完成条件和范围冻结规则。

它解决的问题不是“未来还有哪些能力值得研究”，而是：

> **当前这一轮工程能力扩展做到什么程度即可正式关闭，并形成一个可版本化、可复用、可继续演进的基础基线。**

本文属于 `docs/project/*` 项目级权威，用于约束 `agentic-dev` 自身当前里程碑；不修改 Core Method、Engineering Capability Architecture、Skill Contract，也不由 Consumer Repository 自动继承。

## 2. 里程碑起点与当前进度

本里程碑的起点为 PR #46 合并后的：

`master@350e6607bae6101869d97903b56993820ba73265`

此前已经完成：

- Engineering Capability Expansion 路线切换；
- Engineering Capability Architecture；
- WI-01 工程纪律范围设计；
- WI-02 实现最小化与推测性复杂度控制 Research / Candidate Design；
- WI-03 精准修改与差异范围控制 Research / Candidate Design。

因此 Foundation v1 不重新研究已经关闭的前置问题，从 WI-03V 开始收敛。

当前进度快照：

- **F1 / WI-03V 已完成**：PR #48 已合并，集成提交为 `6130d7251d81bbfc9f13b2dd827b6a40dfd09076`；首批两个 Engineering Discipline 已完成 Fresh Runtime `13 / 13 PASS`、`62 / 62 assertions PASS` 并进入当前 Repository Authority；
- **F2 / WI-04 已完成**：PR #49 已合并，集成提交为 `16151149ab52211e266839a110fc9a3c73415623`；Technology Profile / Verification Profile 最小契约与 `docs/technology-profiles/` 实例入口已进入当前 Repository Authority；
- **F3 / WI-05 当前**：PR #50 已形成 Vue 3 + TypeScript Validated Draft，Fresh Runtime Targeted Eval 为 `9 / 9 PASS`、`41 / 41 assertions PASS`，当前待最终 AI Review 与 Integration Decision；
- F4、F5 尚未开始。

当前状态以 `docs/project/project-roadmap.md` 为准；本节只提供与本里程碑完成边界对应的进度快照，不另建第二套路线路径。

## 3. Foundation v1 的完成定义

Foundation v1 只要求证明以下完整能力链已经在 `agentic-dev` 中真实闭环：

```text
成熟外部证据 / 当前仓库证据
        ↓
Research
        ↓
Candidate
        ↓
Architecture Fit
        ↓
Draft Capability
        ↓
Targeted Eval
        ↓
正式 Engineering Capability
        ↓
Technology Profile Contract
        ↓
一个代表性 Technology Profile
        ↓
一次 Existing Consumer Adoption
        ↓
Foundation v1 Closure Review
```

只有当上述链路全部具有当前可验证证据时，Foundation v1 才能标记为完成。

Foundation v1 **不以能力数量最大化为目标**，也不要求在一个里程碑中覆盖所有工程纪律、技术栈、Skill 或 Runtime。

## 4. 固定五个阶段

### F1 — 首批 Engineering Discipline 正式化

对应 WI-03V。**已完成。**

目标：

- 对 WI-02 / WI-03 Candidate 执行正式 Architecture Fit Review；
- 形成未集成 Draft Capability；
- 建立必要的薄消费入口；
- 物化并运行 Fresh Runtime Targeted Eval；
- 执行必要历史回归；
- 修复验证暴露的边界问题；
- 完成最终 AI Review；
- 由 Human Authority / Repository Policy 决定是否集成。

完成条件：

- 首批两个 Discipline 均有 Research、Candidate、Architecture Fit、Draft 和当前 PASS 证据；
- 适用历史行为没有语义回归；
- 正式能力已实际集成；
- 没有为了完成数量目标机械新增 Skill；
- Phase 3 可以关闭。

当前证据：PR #48 已完成上述闭环并实际集成，因此 F1 已关闭。

### F2 — Technology Profile 最小契约

对应 WI-04。**已完成。**

目标：定义 Technology Profile / Verification Profile 的最小结构和治理边界，而不是开始堆叠具体框架知识。

至少明确：

- 技术与版本适用范围；
- 官方语义、成熟实践和项目覆盖规则的区分；
- 默认工程规则与常见误用；
- Verification Profile 表达；
- Consumer 选择与覆盖边界；
- Evidence、Update、Supersede 生命周期；
- Profile 与 Skill 的非一一对应关系。

完成条件：

- 最小契约足以承载一个真实 Technology Profile；
- 不形成框架百科模板；
- 不预设任何 Profile 必须生成 Skill。

当前证据：PR #49 已将 `docs/architecture/technology-profile-contract.md`、Profile 实例目录和相关 Authority 实际集成，因此 F2 已关闭。

### F3 — 一个代表性 Technology Profile

对应 WI-05，Foundation v1 固定使用：

> **Vue 3 + TypeScript**

**当前：Validated Draft / Targeted Eval PASS / Pending Integration。**

目标：以官方当前有效资料为主、成熟工程实践为辅，完整走通一次：

```text
Research
→ Candidate Profile
→ Architecture Fit
→ Draft Profile
→ Verification Profile
→ Targeted Eval
→ AI Review
→ Integration Decision
```

当前证据：

- Vue stable research anchor：`3.5.42`；
- TypeScript research anchor：`7.0.2`；
- Vue Language Tools research anchor：`3.3.11`；
- `C-VTS-01`～`C-VTS-09`：`9 / 9 PASS`；
- assertions：`41 / 41 PASS`；
- 未发现 Eval contamination；
- PR #50 实际合并前仍不能把 F3 标记为已完成。

完成条件：

- Vue 3 + TypeScript Profile 已实际集成；
- 有明确版本、适用范围、默认规则、误用边界与验证要求；
- Targeted Eval 有当前 PASS 证据；
- Consumer-local Authority 的覆盖关系明确。

Foundation v1 到此**不得自动继续 Element Plus、Spring、Gradle 或其他 Technology Profile**。

### F4 — 一次 Existing Consumer Adoption

对应 WI-08，但在 Foundation v1 内只执行一次受控 Adoption。

优先 Reference Consumer：

`dygapp/jilinjobs-cms`

目标：选择一个真实、边界明确的开发工作单元，验证：

- Existing Consumer baseline upgrade；
- 新 Engineering Discipline 与 Consumer-local Authority 的组合；
- Vue 3 + TypeScript Profile 的实际可用性；
- Verification Profile 是否能够指导真实验证；
- 是否出现错误默认值、过度约束或通用能力缺口。

完成条件：

- 只完成一次明确目标的 Adoption；
- Blocking / Medium 的通用问题已经回写并重新验证；
- Low / Future Improvement 可以记录为后续 Backlog，不要求在本里程碑继续扩展；
- 不把 Consumer Adoption 重新扩展成无限 Experiment。

### F5 — Foundation v1 Closure

目标：执行一次项目级 Closure Review，并正式关闭本轮工程能力基础建设。

至少确认：

- Core Method 未因技术能力扩展产生不必要变化；
- Engineering Capability Architecture 已真实承载 Discipline、Profile、Verification 和 Consumer Adoption；
- 首批两个 Engineering Discipline 已正式集成；
- 至少一个 Technology Profile 已正式集成；
- 新增能力具备当前专项评估证据；
- Existing Consumer Adoption 已完成；
- 没有形成 Super-skill 或框架百科 Skill；
- Post-v1 Backlog 已与当前完成条件分离。

Closure Review 通过后：

- 在 `project-roadmap.md` 标记 **Engineering Capability Foundation v1 = Completed**；
- 记录最终集成 baseline；
- 根据 Human / Repository Policy 创建适当 Tag 或 Release 标记；
- 再决定下一里程碑，而不是在当前里程碑末尾自动续接新范围。

## 5. 四条范围冻结规则

### 5.1 首批 Engineering Discipline 固定为两个

Foundation v1 只正式化：

1. Implementation Minimality & Speculative Complexity Control；
2. Surgical Change & Diff Scope Control。

Code Review、Testing、Refactoring、Dependency Management、API Evolution、Performance、Security、Error Handling 等仍可作为未来候选，但**不得成为 Foundation v1 的新增完成前置条件**。

F1 已按该范围完成。后续阶段不得因为发现新的工程纪律而重新打开 F1 或增加第三个 Discipline 作为 Foundation v1 前置条件。

### 5.2 首批 Technology Profile 固定为一个

Foundation v1 只要求完成：

> Vue 3 + TypeScript

Element Plus、Spring Framework / Spring Boot / Spring MVC、Gradle 以及其他技术栈统一进入 Post-v1 Backlog。

除非 Vue 3 + TypeScript 无法证明 Technology Profile Architecture 的可行性并暴露结构性阻塞，否则不得为了“覆盖更全面”增加第二个 Profile。

### 5.3 Skill 数量不是完成指标

Foundation v1 可以在**新增 0 个 Task-oriented Skill** 的情况下完成。

只有存在独立、稳定、可复用的任务职责，并满足 Engineering Capability Architecture 与 Skill Contract 的准入要求时，才允许建立新 Skill。

不得为了证明工程能力扩展“有产物”而把 Discipline 或 Profile 机械包装成 Skill。

### 5.4 Runtime / Distribution 不属于 Foundation v1

Runtime Adapter、Marketplace、Plugin Bundle、统一安装器、Controller、跨 Runtime Distribution 等不属于 Foundation v1 Completion Gate。

这些事项统一进入后续独立里程碑候选，例如：

> Distribution & Runtime Integration v1

Foundation v1 只需要确保当前能力架构没有阻止未来 Runtime Adapter，不要求本轮实现它们。

## 6. Post-v1 Backlog

以下内容明确不阻塞 Foundation v1：

- 第二个及后续 Technology Profile；
- Element Plus；
- Spring Framework / Spring Boot / Spring MVC；
- Gradle；
- MyBatis / Flyway / Redis / Database 等技术 Profile；
- 通用 Code Review Discipline；
- Testing Discipline；
- Refactoring Discipline；
- Dependency / Framework Upgrade Skill；
- 新 Task-oriented Skills；
- Runtime Adapter；
- Distribution / Marketplace / Plugin / Controller。

它们可以保留为后续路线输入，但只有 Foundation v1 Closure 后的新 Roadmap / Milestone Decision 才能把其中项目提升为当前工作。

## 7. 范围变更门禁

Foundation v1 执行期间，新增工作只有以下情况可以进入当前 Completion Scope：

1. 当前 F1～F5 的 Blocking 缺口；
2. 不修复就无法验证当前定义能力的 Architecture / Contract / Authority 冲突；
3. 当前 Targeted Eval 或 Consumer Adoption 明确证明现有完成条件不可成立。

以下理由不足以扩大里程碑：

- 新发现一个优秀外部项目；
- 新发现一个值得研究的工程纪律；
- 某框架也很常用；
- 某 Skill 看起来可能有价值；
- “顺便一起做更完整”；
- 为了覆盖更多技术栈而增加样本。

如果确实需要改变 F1～F5 或四条冻结规则，应显式修改本文和 Project Roadmap，并说明原完成定义为什么失效；不能通过临时 Plan、Research 或聊天静默扩展。

## 8. 进度表达

Foundation v1 的进度只使用固定五个阶段表达：

```text
F1 Discipline Formalization       已完成
F2 Technology Profile Contract    已完成
F3 Vue 3 + TypeScript Profile     当前（Validated Draft / Pending Integration）
F4 Consumer Adoption              待开始
F5 Foundation v1 Closure          待开始
```

内部可以继续拆成小 Work Item 或 PR，但不得通过增加内部步骤改变五个阶段的总体完成定义。

## 9. 生命周期责任

- **Producer：** Human Authority，或在当前项目级治理下获授权维护 Project Roadmap / Milestone 的 Agent；
- **Trigger：** PR #46 完成首批两个 Discipline Candidate Research，同时需要给当前工程能力扩展建立明确有限终点；
- **Consumer：** Project Roadmap、当前 Engineering Capability Expansion Plan、后续 Fresh Agent、Human Review / Integration Decision；
- **Persistence：** 作为 `docs/project/*` 项目级权威长期保存，直到 Foundation v1 Closure 或被显式取代；
- **Update：** F1～F5 状态变化、完成定义被验证证明无效、或 Human Authority 明确调整里程碑时更新；
- **Supersede：** Foundation v1 Closure 后，由新的项目里程碑 / Roadmap 状态接替当前执行职责；本文保留历史完成边界，不继续承担下一里程碑总控；
- **Escalation：** 如果范围变化需要改变 Core Method、Engineering Capability Architecture、Skill Contract 或重大项目方向，返回对应更高权威处理，不在本文中静默改变。