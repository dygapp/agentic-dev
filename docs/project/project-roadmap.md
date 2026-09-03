# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的项目路线图（Project Roadmap），统一记录项目演进路线、已完成里程碑、当前阶段、当前证据基线、当前核心目标与下一步工作。

本文属于 `docs/project/*` 项目级权威，不修改也不覆盖更高优先级的 Method、Architecture 或 Contract Authority，Consumer Repository 也不得自动继承其中的项目事实。

## 路线图使用规则

本文维护当前有效路线，不要求在项目开始时预知完整演进过程。

路线项使用以下状态语义：

- **已完成**：已有 Git、PR、Issue 或评估证据支持；
- **当前**：正在持续推进的阶段或核心目标；
- **下一步**：已经确定但尚未开始或尚未完成的近期工作；
- **条件性后续**：需要后续证据或阶段成果才能决定是否进入，不构成当前承诺。

路线、里程碑或当前目标发生变化时更新本文。Git 历史保留旧版本，不在 README、Tasks 或聊天中长期维护第二份详细状态。

## 阶段切换

此前阶段：

> **Skill Operationalization & Method Validation**

已经完成其主要使命：第一批核心 Skill 已完成工程闭环，首轮 Greenfield Consumer Experiment 已完成，已有 Consumer 的继续演进又进一步验证并强化了 baseline 升级、外部操作、验证证据、Human Review、共享资源、配置责任和已有能力复用等边界。

Issue #33 已按原始实验目标形成 Final Summary，并以 `PASS / Completed` 关闭；其多轮有效证据足以支持 `agentic-dev` 不再把持续等待该实验新增 Finding 作为下一阶段启动条件。完整结论见 [Issue #33 Final Summary](https://github.com/dygapp/agentic-dev/issues/33#issuecomment-5527800060)。

`dygapp/jilinjobs-cms` 后续主要进入模块化重构、页面内容完善和大平台集成准备，其继续开发仍可提供实践反馈，但不再适合作为 `agentic-dev` 唯一或主要的能力创新来源。

因此当前阶段为：

> **Engineering Capability Expansion & Method Evolution（工程能力扩展与方法演进）**

本阶段从“主要等待 Consumer 暴露问题后定向修补”，转向“主动研究成熟外部实践、形成工程能力、建立专项评估，再推动 Consumer 采用和纠偏”。

本阶段首个有限里程碑：

> **Engineering Capability Foundation v1（工程能力基础版 v1）**

已经完成固定 F1～F5 闭环。完成定义与历史范围冻结见：

- `docs/project/engineering-capability-foundation-v1.md`
- `docs/project/engineering-capability-foundation-v1-closure.md`

Foundation v1 完成后没有自动续接原 Post-v1 Work Item。Human Authority 在 Issue #33 收敛后显式选择新的有限里程碑：

> **Engineering Discipline Expansion v1（工程纪律扩展 v1）**

当前唯一候选：

> **Data Access Scope & Boundedness Control（数据访问作用域与有界性控制）**

完成定义与范围冻结见：

`docs/project/engineering-discipline-expansion-v1.md`

## 总体演进路线

| 路线 | 状态 | 当前目标 |
|---|---|---|
| 建立通用 AI Agent 开发方法基线 | 已完成 | Method、Principles 与第一批 Skill 设计、契约形成稳定基线 |
| 完成第一批核心 Skill 工程 | 已完成 | 8 个 Core Skills 实现、Packaging Hardening、Fresh Runtime Eval 与 Closure Review 完成 |
| 完成首轮方法与 Skill 实证验证 | 已完成 | Greenfield Experiment 与 Existing Consumer continuous-evolution experiment 均已完成，Issue #18 / #33 已关闭 |
| Track A — Method Consolidation | 当前 | Core Method 进入稳定维护；只在高质量证据揭示通用生命周期或权威缺口时定向修改 |
| Track B — Engineering Discipline Expansion | **当前** | Engineering Discipline Expansion v1 只验证并集成 Data Access Scope & Boundedness Control 一个候选 |
| Track C — Technology Engineering Profiles | 已完成 / 条件性后续 | Foundation v1 的 Technology Profile Contract 与 Vue 3 + TypeScript Profile 已完成；WI-06 第二 Profile 未启动 |
| Track D — Consumer Adoption | 已完成 | Issue #52 F4 Evidence Review PASS；唯一 Foundation v1 Existing Consumer Adoption 已完成且 Blocking / Medium General Finding = 0 |
| Track E — Engineering Skills | 条件性后续 | WI-07 保持 Post-v1；只有新的 Milestone Decision 证明存在独立稳定任务职责时才进入 |
| Track F — Runtime / Distribution | 条件性后续 | WI-09 保持 Post-v1；Runtime Adapter、Marketplace、Plugin Bundle、Controller 与统一安装器不自动续接 |

**Engineering Capability Foundation v1：Completed。**

**Engineering Discipline Expansion v1：Current。**

当前里程碑不自动包含第二个 Engineering Discipline、第二个 Technology Profile、新 Task-oriented Skill、Runtime / Distribution 或新的正式 Consumer Adoption Gate。

## 工程能力扩展模型

新的主动演进模型采用：

```text
官方权威实践 / 成熟开源实践 / 专家研究
                    ↓
               Research
                    ↓
         Engineering Capability Fit
                    ↓
      Discipline / Profile / Skill / Adapter
                    ↓
             Targeted Eval
                    ↓
               AI Review
                    ↓
               Integrate
                    ↓
          Consumer Adoption
                    ↓
          Feedback / Revision
```

具体能力生命周期以 `docs/architecture/engineering-capability-architecture.md` 为准；其中 Candidate 在 Targeted Eval 前必须先经过 Architecture Fit Review 并形成 Draft Capability。

Consumer Evidence 仍然是重要输入，但主要承担：

- 验证通用能力是否适合真实工程环境；
- 发现 Profile 或 Skill 与项目实际约束之间的冲突；
- 纠正过度抽象或错误默认值；
- 调整能力优先级；
- 验证 Existing Consumer baseline upgrade 是否可靠。

不再采用：

```text
等待 Consumer 出现问题
        ↓
agentic-dev 才开始研究
```

作为项目唯一的演进模式。

工程能力分层的正式架构见：

`docs/architecture/engineering-capability-architecture.md`

## 已完成里程碑

| 日期 | 里程碑 | 证据 |
|---|---|---|
| 2026-08-17 | 建立 Method 基线并冻结第一批核心 Skill 设计与契约 | `8fccf7232c21`、`b5480db06940`、`992f13a2ed49` |
| 2026-08-17 | 完成 8 个 Core Skills 首轮实现 | `99314b70c05c` 至 `c96cc7e2ac30` |
| 2026-08-18 | 完成首轮 Fresh Runtime Eval 并关闭第一批历史 Skill Engineering 基线 | `498bdfc543bf`、`bf4f4b5e7ba6` |
| 2026-08-18 | 启动首个真实 Consumer Repository 验证 | Issue #18 |
| 2026-08-24 | 完成验收到验证闭环定向强化 | PR #30，行为评估 `4 / 4 PASS`、断言 `21 / 21 PASS` |
| 2026-08-24 | 完成首轮 Consumer Experiment 收敛 | Issue #18 `completed` |
| 2026-08-24 | 建立通用 Project Roadmap 规则 | PR #32，行为评估 `3 / 3 PASS`、断言 `16 / 16 PASS` |
| 2026-08-26 | 明确 Existing Consumer baseline upgrade 生命周期 | PR #34 |
| 2026-08-26 | 完成跨 Repository 授权与异步执行闭环强化 | PR #35，行为评估 `4 / 4 PASS`、断言 `20 / 20 PASS` |
| 2026-08-28 | 完成验证证据边界定向强化 | PR #37，行为评估 `6 / 6 PASS`、断言 `35 / 35 PASS` |
| 2026-08-28 | 完成 Human Review、外部媒体输入和后继提交证据强化 | PR #38，行为评估 `4 / 4 PASS`、断言 `25 / 25 PASS` |
| 2026-08-31 | 完成共享外部资源并发与释放边界强化 | PR #40，行为评估 `4 / 4 PASS`、断言 `25 / 25 PASS` |
| 2026-09-01 | 明确配置责任与已有能力复用边界 | PR #41，行为评估 `4 / 4 PASS`、断言 `25 / 25 PASS` |
| 2026-09-01 | 增加 Karpathy Skills 定向研究并确认“工程纪律可主动研究、无需机械 Skill 化” | PR #42，集成提交 `e1f56238f95a75d95a87b1ad510587d770ae4a63` |
| 2026-09-02 | 建立主动工程能力演进架构并完成 Phase 1 / Phase 2 | PR #43，集成提交 `1eb729333b4aa239dfbb1906b623b61e7c1524a9` |
| 2026-09-02 | 完成 WI-01 工程纪律范围设计并确定首批两个研究方向 | PR #44，集成提交 `070cbb448118a6ee0494063c2d2c8ae689bfb5f3` |
| 2026-09-02 | 完成 WI-02 实现最小化工程纪律 Research / Candidate Design | PR #45，集成提交 `710ebcbf32d1222c4578c4e2fffe90408070e3d8` |
| 2026-09-02 | 完成 WI-03 精准修改工程纪律 Research / Candidate Design | PR #46，集成提交 `350e6607bae6101869d97903b56993820ba73265` |
| 2026-09-02 | 冻结 Engineering Capability Foundation v1 有限完成边界 | PR #47，F1～F5 与范围冻结规则进入项目权威 |
| 2026-09-02 | 正式集成首批两个 Engineering Discipline 并关闭 F1 / WI-03V | PR #48，集成提交 `6130d7251d81bbfc9f13b2dd827b6a40dfd09076`；Fresh Runtime `13 / 13 PASS`、断言 `62 / 62 PASS` |
| 2026-09-02 | 建立 Technology Profile / Verification Profile 最小契约并关闭 F2 / WI-04 | PR #49，集成提交 `16151149ab52211e266839a110fc9a3c73415623` |
| 2026-09-02 | 正式集成 Vue 3 + TypeScript Technology Profile 并关闭 F3 / WI-05 | PR #50，集成提交 `b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`；Capability Eval `9 / 9 PASS`、断言 `41 / 41 PASS` |
| 2026-09-03 | 建立 F4 Existing Consumer Adoption Handoff | PR #51，集成提交 `18a48bcada8b4eeb0e6d8c3043b21c54aa8e492b` |
| 2026-09-03 | 完成 F4 Existing Consumer Adoption Evidence Review | Issue #52；Consumer PR #49 为唯一 Adoption Unit，Blocking / Medium General Finding = `0 / 0` |
| 2026-09-03 | Engineering Capability Foundation v1 Closure Review PASS | `docs/project/engineering-capability-foundation-v1-closure.md`；F1～F5 全部满足冻结完成条件 |
| 2026-09-03 | 完成 Existing Consumer continuous-evolution experiment 收敛 | Issue #33 `completed`；Final Summary 结论 `PASS / Completed`，Blocking / Medium Finding = `0 / 0` |

## 当前证据基线

- 当前阶段：**Engineering Capability Expansion & Method Evolution**；
- **Engineering Capability Foundation v1：Completed**；
- Foundation v1 最终 Closure / Issue #33 收敛后的新里程碑起点：`master@a0aece02414aa36ca7421db391cb3124ad0780f2`；
- Foundation v1 正式 Capability baseline：`b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`；
- Skill Inventory：8 个 Core Skills、1 个 Platform-specific Skill；当前里程碑不以新增 Skill 为完成指标；
- F1 / WI-03V：已完成；PR #48 Targeted Eval `13 / 13 PASS`、`62 / 62 assertions PASS`；
- F2 / WI-04：已完成；Technology Profile / Verification Profile Contract 已集成；
- F3 / WI-05：已完成；Vue 3 + TypeScript Profile 已集成，Capability Eval `9 / 9 PASS`、`41 / 41 assertions PASS`；
- F4 / WI-08：已完成；Issue #52 F4 Evidence Review PASS；
- F5 Closure Review：PASS；Blocking / Medium Closure Finding：`0 / 0`；
- Issue #33 已以 `PASS / Completed` 关闭，Blocking / Medium Finding = `0 / 0`；
- Issue #33 剩余 Post-v1 Candidate 中，Data Access Scope / Boundedness / Lifecycle 被显式选择进入当前 Engineering Discipline Expansion v1；
- stacked PR + squash merge review / integration topology 仍是 Low / Future Improvement Candidate，不属于当前里程碑；
- **Engineering Discipline Expansion v1：Current**；
- ED1 — Milestone Definition：已完成；
- ED2 — Research / Candidate / Architecture Fit：已完成，Architecture Fit = Engineering Discipline；
- ED3 — Draft / Targeted Eval：当前；Fresh Runtime 尚未执行；
- ED4 — AI Review / Integration / Closure：待 ED3 当前证据后执行；
- 当前 Draft 不改变 Core Method，不创建新 Skill，不修改 Technology Profile Contract，不启动第二个 Profile；
- WI-06、WI-07、WI-09 保持 Post-v1 Backlog。

当前里程碑定义：

`docs/project/engineering-discipline-expansion-v1.md`

当前实施 Plan：

`tasks/plans/20260903/02-data-access-discipline.md`

当前 Research：

`docs/research/data-access-scope-boundedness-analysis.md`

## 当前核心目标

当前核心目标是：

> **在不扩大 Post-v1 范围的前提下，完成 Data Access Scope & Boundedness Control 单一 Engineering Discipline 的 Draft、Fresh Runtime Targeted Eval、AI Review 与 Integration Closure。**

当前不启动：

- WI-06 第二个 Technology Profile；
- WI-07 Task-oriented Skill；
- WI-09 Runtime / Distribution；
- stacked PR topology 专项；
- 第二个新的 Engineering Discipline；
- 新的正式 Consumer Adoption Gate。

如果当前 Candidate 在 Architecture / Eval 中证明不成立，可以重分类或拒绝并关闭本里程碑，不为了产物数量强行固化。

## Foundation v1 分阶段结果

### Phase 1 — 演进路线重构

状态：**已完成**。

### Phase 2 — Engineering Capability Architecture

状态：**已完成**。

### Phase 3 — Engineering Discipline Formalization

状态：**已完成**。

结果：首批两个 Discipline 完成 Architecture Fit、Draft、Fresh Runtime Targeted Eval、AI Review 与 Integration。

### Phase 4 — Technology Profile Foundation

状态：**已完成**。

结果：Technology Profile Contract 与唯一代表性 Vue 3 + TypeScript Profile 已集成。

### Phase 5 — Consumer Adoption

状态：**已完成**。

结果：Foundation v1 的唯一 Existing Consumer Adoption 与 Evidence Review 已完成。

### Phase 6 — Foundation v1 Closure

状态：**PASS / Completed**。

完整 Closure Review：

`docs/project/engineering-capability-foundation-v1-closure.md`

## 当前里程碑 — Engineering Discipline Expansion v1

### ED1 — Milestone Definition

状态：**已完成**。

结果：唯一候选、完成条件和范围冻结已进入 `docs/project/engineering-discipline-expansion-v1.md`。

### ED2 — Research / Candidate / Architecture Fit

状态：**已完成**。

结果：

- Issue #33 已核验 Consumer Evidence 与当前外部官方 / 成熟工程 Evidence 已完成综合研究；
- Candidate 核心不是“所有接口分页”，而是 Consumer Scope、Boundedness / Growth、Lifecycle / Freshness、Filtering / Ordering、Window / Pagination、Representation 和 Verification 的组合判断；
- Architecture Fit：**Independent Engineering Discipline + thin `execute-unit` consumption**；
- 不需要 Core Method、Engineering Capability Architecture、Technology Profile 或新 Skill。

### ED3 — Draft / Targeted Eval

状态：**当前**。

当前 Draft：

- `docs/architecture/engineering-disciplines.md`：增加 Data Access Scope & Boundedness Control；
- `docs/architecture/skill-contracts.md`：只补 `execute-unit` 薄消费契约；
- `skills/execute-unit/SKILL.md`：只补实施、验证和 Engineering Quality 判断；
- `evals/behavior/execute-unit.json`：新增 `B-EU-18`～`B-EU-25`。

待验证：

- 新场景 `B-EU-18`～`B-EU-25`；
- 历史回归 `B-EU-01`、`B-EU-06`、`B-EU-09`、`B-EU-13`；
- Fresh Runtime 后逐 assertion 语义评分；
- 进程退出 0 不等于 Eval PASS。

### ED4 — AI Review / Integration / Closure

状态：**待开始**。

只有 ED3 Fresh Runtime Evidence 通过后才进入最终 AI Review / Ready to Integrate。实际 Merge 继续由 Human Authority / Repository Policy 决定。

## 下一步工作

1. 对当前 Draft / Contract / Skill / Eval corpus 执行 Runtime 前 AI Review；
2. 修复所有 Blocking / Medium Finding；
3. 冻结被测 Head；
4. Fresh Runtime 运行 `B-EU-18`～`B-EU-25` 与 `B-EU-01/06/09/13`；
5. 逐 assertion 语义判分并检查隔离 / contamination；
6. 如 PASS，只回写 Evidence、Roadmap / Plan 与 Closure 状态，不在验证后改变受测语义；
7. 最终高影响 AI Review；
8. Ready to Integrate 后等待 Human Integration Decision；
9. 实际集成后关闭 Engineering Discipline Expansion v1，再独立决定下一 Milestone。

WI-06、WI-07、WI-09 以及 stacked-PR topology 在本里程碑中均不启动。

## Issue #33 的收敛结果

Issue #33 已按 Existing Consumer continuous-evolution experiment 的原始目标完成 Final Summary，并以 `completed` 关闭：

[Issue #33 Final Summary](https://github.com/dygapp/agentic-dev/issues/33#issuecomment-5527800060)

最终结论：

- Experiment：`PASS / Completed`；
- Blocking / Medium Finding：`0 / 0`；
- 未解决的 Method / Contract 缺口：`0`；
- 待补 Skill / Eval：`0`；
- Reference Evidence / Runtime Asset Ownership 属于现有规则的正向验证；
- Authority 变化导致 Verification Contract 陈旧已由现有规则与评估覆盖；
- Stacked PR / Squash Merge 的双重祖先关系继续作为 Post-v1 Low / Future Improvement Candidate；
- Data Access Scope / Boundedness / Lifecycle 已由 Human Milestone Decision 显式提升为当前 Engineering Discipline Expansion v1 的唯一候选。

Issue #33 现作为已关闭的历史证据来源，不再承担活动跟踪或路线总控职责。

## 新上下文恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根目录 `AGENTS.md`；
2. 读取本文，确认当前里程碑是 Engineering Discipline Expansion v1；
3. 读取 `docs/project/engineering-discipline-expansion-v1.md` 与 `tasks/plans/20260903/02-data-access-discipline.md`；
4. 读取当前 GitHub `master` / 活动 PR，验证是否存在晚于本文的新集成状态；
5. 读取 `docs/research/data-access-scope-boundedness-analysis.md` 了解 Research / Candidate，不把 Research 当作规范权威；
6. 当前 ED3 读取 `docs/architecture/engineering-disciplines.md`、`docs/architecture/skill-contracts.md`、`skills/execute-unit/SKILL.md` 与 `evals/behavior/execute-unit.json`；
7. 不把 WI-06、WI-07、WI-09、stacked PR topology 或其他 Post-v1 候选自动并入当前范围；
8. Issue #33 只作为已关闭 Evidence Source 按需读取，不恢复为活动 Experiment；
9. 不依赖历史聊天或个人记忆补充未固化的项目事实。

## 更新触发条件

出现以下任一情况时，应更新本文：

- Engineering Discipline Expansion v1 的 ED1～ED4 状态发生变化；
- Targeted Eval / AI Review 证明当前 Candidate 需要重分类、拒绝或改变完成边界；
- 当前 Draft 实际进入 Repository Authority；
- Human Authority 显式改变当前 Milestone；
- 当前路线与 GitHub 集成事实不再一致。

普通局部实现、Consumer-local Finding、其他 Post-v1 候选或新外部研究，不要求更新本文，也不得据此静默扩大当前里程碑。
