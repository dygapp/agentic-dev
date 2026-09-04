# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的 Project Roadmap，记录当前有效的项目阶段、能力基线、已完成里程碑、当前决策状态与下一步边界。

本文属于 `docs/project/*` 项目级权威，不覆盖更高优先级的 Method、Architecture、Contract、Engineering Discipline 或 Technology Profile Authority。Consumer Repository 不自动继承本文中的 `agentic-dev` 项目事实。

## 1. 路线图使用规则

本文只维护当前有效路线；历史细节由 Git 历史、已关闭 Issue / PR、Milestone / Closure 文档保留。

状态语义：

- **Completed**：完成条件已有当前 Git / PR / Issue / Eval / Review 证据支持；
- **Current**：当前正在执行的有限里程碑；
- **Decision Pending**：上一里程碑已完成，但下一有限里程碑尚未由 Human Authority 选择；
- **Post-v1 Backlog**：保留为候选，但不是当前承诺。

不得因为出现新的外部资料、Consumer Finding 或有价值候选而静默扩展当前路线。

## 2. 当前阶段

当前长期阶段仍为：

> **Engineering Capability Expansion & Method Evolution（工程能力扩展与方法演进）**

该阶段已经完成两个有限里程碑：

1. **Engineering Capability Foundation v1**；
2. **Engineering Discipline Expansion v1**。

当前项目状态：

> **Post-Milestone Decision / Stable Maintenance**

即：当前没有自动续接的活动能力里程碑。下一项正式能力建设必须由新的 Human Milestone Decision 显式启动。

## 3. 总体路线状态

| 路线 | 状态 | 当前边界 |
|---|---|---|
| Core Method | Stable Maintenance | 只有高质量通用证据揭示生命周期 / Authority 缺口时定向修改 |
| Engineering Disciplines | Completed / Conditional Expansion | 当前已有三项 Discipline；不自动启动第四项 |
| Technology Profiles | Foundation Completed / Post-v1 Backlog | Technology Profile Contract 与 Vue 3 + TypeScript Profile 已完成；WI-06 未启动 |
| Consumer Adoption | Foundation Completed | Foundation v1 唯一 Existing Consumer Adoption 已完成；普通 Consumer Feedback 继续作为候选输入 |
| Task-oriented Skills | Post-v1 Backlog | WI-07 未启动；只有出现独立稳定任务职责并经 Milestone Decision 才进入 |
| Runtime / Distribution | Post-v1 Backlog | WI-09 未启动；Runtime Adapter、Marketplace、Plugin Bundle、Controller、统一安装器均不是当前工作 |

## 4. 当前能力基线

### 4.1 Engineering Capability Foundation v1

**Completed**。

主要集成事实：

- 首批 Engineering Disciplines：PR #48，merge `6130d7251d81bbfc9f13b2dd827b6a40dfd09076`；
- Technology Profile / Verification Profile Contract：PR #49，merge `16151149ab52211e266839a110fc9a3c73415623`；
- Vue 3 + TypeScript Profile：PR #50，merge `b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`；
- Existing Consumer Adoption Handoff：PR #51，merge `18a48bcada8b4eeb0e6d8c3043b21c54aa8e492b`；
- F4 Evidence Review：Issue #52，Blocking / Medium General Finding = `0 / 0`；
- Foundation Closure：`docs/project/engineering-capability-foundation-v1-closure.md`。

Foundation v1 正式能力基线：

`b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`

### 4.2 Existing Consumer continuous-evolution experiment

Issue #33 已以：

> **PASS / Completed**

关闭。

最终：

- Blocking / Medium Finding = `0 / 0`；
- 未解决 Method / Contract Gap = `0`；
- 待补 Skill / Eval = `0`。

Issue #33 现在只作为历史 Evidence Source，不再承担活动路线总控职责。

### 4.3 Engineering Discipline Expansion v1

**PASS / Completed**。

启动基线：

`master@a0aece02414aa36ca7421db391cb3124ad0780f2`

唯一候选：

> **Data Access Scope & Boundedness Control（数据访问作用域与有界性控制）**

Architecture Fit：

> **Independent Engineering Discipline + thin `execute-unit` consumption**

Fresh Runtime Targeted Eval：

```text
新场景：   8 / 8 PASS，41 / 41 assertions PASS
历史回归： 4 / 4 PASS，19 / 19 assertions PASS
合计：    12 / 12 PASS，60 / 60 assertions PASS
```

ZIP SHA-256：

`d32233916e2ce923f2f052fe6750eda4bf0674992906bd18223b43f83f21a855`

AI Review：

- Pre-Runtime：PASS，Blocking / Medium = `0 / 0`；
- Final：PASS，Blocking / Medium = `0 / 0`；
- Final Review ID：`5104594425`。

Integration：

- PR #56：merged；
- merge commit：`8d0c7ccd1b13db05540fefc619725f9d1f7fc2de`。

Closure：

- `docs/project/engineering-discipline-expansion-v1.md`
- `docs/project/engineering-discipline-expansion-v1-closure.md`

第三项 Engineering Discipline 已进入 Repository Authority。

### 4.4 Issue #58 外部证据与评审环境生命周期维护

Issue #58 的 Consumer Evidence 触发了一次 **Stable Maintenance** 定向修订，而不是新的能力里程碑：

- 临时执行证据被适当 Authority 接受并成为长期输入时，显式晋升为 Consumer 可持续维护的持久来源，保留 provenance / integrity，并对 Promotion 后的最终状态重新取得 Current Evidence；
- 长生命周期单实例 Review Environment 显式定义 owner、lease、stale-run 与释放 / 接管策略，区分自动 Verification 和有效 Human Review lease；
- 不修改 Core Method、Principles、Skill Contract、Data Access Engineering Discipline，不新增 Skill，也不采用机械 `latest-head-wins`。

Fresh Runtime Targeted Eval：

```text
新场景：   2 / 2 PASS，15 / 15 assertions PASS
历史回归： 3 / 3 PASS，19 / 19 assertions PASS
合计：     5 / 5 PASS，34 / 34 assertions PASS
```

ZIP SHA-256：

`26ddf975a181438071cfb8453cc30fa877943c9bb652f190999e761d0fca56cc`

Integration Reference：

- PR #59；
- 是否已经进入默认分支，以 GitHub 中 PR #59 的 merged 状态和 merge commit 为准；本文不复制“等待合并 / 已合并”的瞬态状态，避免为记录上一个 PR 的合并事实机械创建后续状态 PR。

该维护不改变当前 **Post-Milestone Decision / Stable Maintenance** 状态，也不自动启动 WI-06、WI-07、WI-09 或新的 Engineering Discipline。

## 5. 当前 Engineering Discipline Inventory

当前正式 Engineering Disciplines：

1. **Implementation Minimality & Speculative Complexity Control**；
2. **Surgical Change & Diff Scope Control**；
3. **Data Access Scope & Boundedness Control**。

规范入口：

`docs/architecture/engineering-disciplines.md`

当前没有第四项 Discipline 的活动 Research / Draft / Eval 计划。

## 6. 当前 Skill / Profile 状态

- Skill Inventory：8 个 Core Skills、1 个 Platform-specific Skill；
- Engineering Discipline Expansion v1 未新增 Skill；
- Technology Profile Contract 已集成；
- 当前代表性 Technology Profile：Vue 3 + TypeScript；
- Element Plus、Spring Framework / Spring Boot / Spring MVC、Gradle 等仍是未来候选，不构成当前路线承诺。

## 7. Post-v1 Backlog

以下候选继续保留，但均为 **Decision Pending / Not Started**：

### WI-06 — 第二及后续 Technology Profile

候选可能包括：

- Spring Framework / Spring Boot / Spring MVC；
- Gradle；
- Element Plus；
- 其他后续证据支持的技术栈。

Vue Profile 完成或本次 Discipline Closure 都不会自动触发 WI-06。

### WI-07 — Task-oriented Skill 提炼

只有出现可证明的独立稳定任务职责，且具有明确 Inputs / Procedure / Outputs / Exit / Escalation，才重新评估。

不得机械创建 `vue-skill`、`spring-skill`、`data-access-skill` 等技术百科式 Skill。

### WI-09 — Runtime Adapter / Distribution

包括未来可能的：

- Runtime Adapter；
- Marketplace；
- Plugin Bundle；
- Controller；
- 统一安装 / 分发机制。

当前没有真实多 Runtime 交付需求足以使其成为活动里程碑。

### 其他候选

- stacked PR + squash merge 的 review ancestry / integration ancestry topology；
- 新的 Engineering Discipline Research Candidate；
- Consumer Feedback 形成的通用能力候选。

这些候选必须重新经过 Evidence / Architecture Fit / Milestone Decision，不能直接进入当前 Authority。

## 8. 下一步决策规则

下一正式 Milestone 必须：

1. 由 Human Authority 显式选择；
2. 有清晰的单一或有限目标；
3. 在开始时冻结 Completion Definition；
4. 明确非目标与范围扩张门禁；
5. 根据能力类型走 Research → Architecture Fit → Draft → Targeted Eval → AI Review → Integration；
6. 不因为新候选出现而自动追加到同一里程碑。

在新的 Milestone Decision 之前，不进行：

- 第二 Technology Profile 正式建设；
- 新 Task-oriented Skill 正式建设；
- Runtime / Distribution 实施；
- 第四 Engineering Discipline 正式建设；
- 第二次正式 Foundation-style Consumer Adoption Gate。

## 9. 新上下文恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根目录 `AGENTS.md`；
2. 读取本文确认当前状态为 **Post-Milestone Decision / Stable Maintenance**；
3. 读取 `docs/project/engineering-capability-foundation-v1-closure.md` 与 `docs/project/engineering-discipline-expansion-v1-closure.md` 了解最近两个完成边界；
4. 读取当前 GitHub `master`、Open PR / Issue，确认是否存在晚于本文的新 Milestone Decision；
5. 按任务需要读取 Method / Architecture / Discipline / Technology Profile Authority；
6. 不自动恢复 Issue #33 为活动 Experiment；
7. 不把 WI-06、WI-07、WI-09 或其他 Post-v1 Candidate 当作已启动工作；
8. 不依赖历史聊天或个人记忆补充未固化项目事实。

## 10. 更新触发条件

出现以下情况时更新本文：

- Human Authority 选择新的有限 Milestone；
- 当前 Repository Authority 发生新的能力集成；
- 高质量 Evidence 导致现有 Method / Architecture / Discipline / Profile 需要正式修订；
- 当前路线与 GitHub 集成事实不再一致。

普通 Consumer-local Finding、单个新外部来源或尚未 Architecture Fit 的 Candidate 不要求更新本文。
