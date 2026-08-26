# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的项目路线图（Project Roadmap），统一记录项目演进路线、已完成里程碑、当前阶段、当前证据基线、当前核心目标与下一步工作。本文属于 `docs/project/*` 项目级权威，不修改也不覆盖更高优先级的 Method、Architecture 或 Contract Authority，Consumer Repository 也不得自动继承其中的项目事实。

## 路线图使用规则

本文维护当前有效路线，不要求在项目开始时预知完整演进过程。

路线项使用以下状态语义：

- **已完成**：已有 Git、PR、Issue 或评估证据支持；
- **当前**：正在持续推进的阶段或核心目标；
- **下一步**：已经确定但尚未开始或尚未完成的近期工作；
- **条件性后续**：只有新的真实证据满足触发条件时才评估，不构成既定承诺。

路线、里程碑或当前目标发生变化时更新本文。Git 历史保留旧版本，不在 README、Tasks 或聊天中长期维护第二份详细状态。

## 总体演进路线

| 路线 | 状态 | 结果或进入条件 |
|---|---|---|
| 建立通用 AI Agent 开发方法基线 | 已完成 | Method、Principles 与第一批 Skill 设计、契约形成基线 |
| 完成第一批核心 Skill 工程 | 已完成 | 8 个 Core Skills 实现、元数据标准化并完成 Fresh Runtime Eval |
| 开展 Skill Operationalization & Method Validation | 当前 | 使用真实 Consumer Evidence 验证方法、Skills 组合与项目渐进演进 |
| 完成首轮真实 Consumer Experiment | 已完成 | `dygapp/jilinjobs-cms` 完成 Greenfield Bootstrap、信息发布纵向切片与功能整体收敛 |
| 补齐验收到验证的闭环 | 已完成 | PR #30 已合并，Issue #18 已按 `completed` 关闭 |
| 建立通用 Project Roadmap 规则 | 已完成 | PR #32 完成 Method、Bootstrap、Fresh Context 与 `converge` 定向强化；行为评估 `3 / 3 PASS`、断言 `16 / 16 PASS` |
| 验证已有 Consumer 的继续演进 | 当前 | 已通过 Issue #33 在 `dygapp/jilinjobs-cms` 中启动验证，并进入 Consumer 治理证据的分类与定向处理 |
| Distribution、Bootstrap 自动化或 Controller / Runtime Orchestration | 条件性后续 | 只有真实使用证明存在稳定、独立且可复用的职责缺口时才评估 |
| 重新进入 Skill Engineering | 条件性后续 | 只有新的真实证据暴露稳定 Skill Implementation / Contract / Method Gap 时才定向重开 |

## 已完成里程碑

| 日期 | 里程碑 | 证据 |
|---|---|---|
| 2026-08-17 | 建立 Method 基线并冻结第一批核心 Skill 设计与契约 | `8fccf7232c21`、`b5480db06940`、`992f13a2ed49` |
| 2026-08-17 | 完成 8 个 Core Skills 的首轮实现 | `99314b70c05c` 至 `c96cc7e2ac30` 的 Skill 实现提交 |
| 2026-08-18 | 完成首轮 Fresh Runtime Eval 并关闭历史 Skill 工程（Skill Engineering）基线 | `498bdfc543bf`、`bf4f4b5e7ba6` |
| 2026-08-18 | 启动首个真实 Consumer Repository 验证 | `d8b90b1880a1`、Issue #18 |
| 2026-08-19 至 2026-08-20 | 根据真实使用补齐外部操作、平台验证、ADR 与长期权威产物生命周期边界 | `080cbe660db3` 至 `3e0b99d85d96` 的相关提交 |
| 2026-08-24 | 完成验收到验证闭环定向强化及运行时评估 | PR #30、`a6ea8ccfb23c`，行为评估 `4 / 4 PASS`、断言 `21 / 21 PASS` |
| 2026-08-24 | 完成首轮 Consumer Experiment 收敛 | Issue #18 按 `completed` 关闭 |
| 2026-08-24 | 完成通用 Project Roadmap 方法修订及运行时评估 | PR #32，行为评估 `3 / 3 PASS`、断言 `16 / 16 PASS` |
| 2026-08-26 | 明确已有 Consumer 的采用与 baseline 升级生命周期 | PR #34、`b1ed6f1b78eb` |
| 2026-08-26 | 完成跨 Repository 授权与异步外部执行闭环强化 | PR #35、`282358c2f659`，行为评估 `4 / 4 PASS`、断言 `20 / 20 PASS` |

## 当前阶段与证据基线

- 当前阶段：**Skill Operationalization & Method Validation**；
- PR #30 能力集成提交：`a6ea8ccfb23cb0837d4721192470e3bd11597059`；
- PR #31 路线图基线集成提交：`f15d3b42fd56498ffa08633c66b338e28e046542`；
- PR #34 已有 Consumer 采用边界集成提交：`b1ed6f1b78eb664e6dcae619b23e2ac1b7c5b522`；
- PR #35 跨 Repository 授权与异步验证闭环集成提交：`282358c2f6590a2e8e7634cdd16458d89d1ba3b7`；
- Project Roadmap 定向评估：`B-CG-05`、`B-CG-06`、`B-CG-07` 均为 `PASS`，合计断言 `16 / 16 PASS`；
- Skill 清单（Skill Inventory）：8 个 Core Skills、1 个 Platform-specific Skill；
- 首轮 Consumer Experiment：已完成；
- Issue #18：已关闭；
- 已有 Consumer 继续演进实验：已启动；
- 实验跟踪 Issue（Tracking Issue）：Issue #33，保持 `open`；
- Consumer 实验基线：`dygapp/jilinjobs-cms` `main@77958e5af7f8a60f8e09848ec0a3e837970fefa3`；
- 实验使用的 `agentic-dev` baseline：`master@b4e5b2027bdbbe97cc0b7153be65c5afb7a0274e`；
- Issue #33 当前已提交 5 类项目治理证据；已有 Consumer 的采用与升级边界已通过 PR #34 集成，跨 Repository 操作授权粒度与异步外部执行闭环已通过 PR #35 集成；`B-GA-01` 与 3 个当前证据回归场景均为 `PASS`，合计断言 `20 / 20 PASS`；README / Project Roadmap / GitHub Evidence 分工与无 Issue Template 的反馈契约作为正向验证保留。

上述提交是已完成里程碑的证据锚点，不是要求后续工作永久固定使用的静态版本。新的实验或修订开始时，必须读取并记录当时实际使用的精确 `agentic-dev` baseline。

## 当前核心目标

当前核心目标是：**基于已有真实 Consumer Repository 开展继续演进验证；不重复 Greenfield Bootstrap，也不机械扩展方法与 Skill 清单。**

当前优先验证载体是 `dygapp/jilinjobs-cms`。它只提供 Consumer Evidence，其项目事实仍由自身 Repository Authority 决定。

重点验证：

1. Fresh Agent 能否只依靠已持久化的 Consumer Authority、当前代码与验证证据恢复工作；
2. 项目路线、Consumer Authority、Specification、必要的 Technical Plan 和长期产物能否随新需求正确增量演进；
3. 新的真实纵向工作能否完成 `slice-work → readiness-check → execute-unit → converge` 闭环；
4. 验收义务能否持续闭环到实现责任、验证责任、计划验证证据与已执行的当前证据；
5. 人工介入是否继续受 Authority、Impact、Reversibility 与 Consumer Repository Policy 约束。

## 下一步工作

1. 将 PR #35 的精确集成提交与第二阶段结果回写 Issue #33；实验形成 Final Summary 前保持 Issue `open`；
2. 继续让 Fresh Agent 依靠 Consumer Repository Authority 恢复项目状态，并以新的真实纵向工作验证其增量演进能力；
3. 当已有 Consumer 继续演进实验取得足够的纵向工作证据后，形成 Final Summary，并据此判断 Issue #33 的关闭状态与后续条件性工作。

## 尚未确定与条件性后续

- `dygapp/jilinjobs-cms` 的下一个真实纵向切片尚未选择，应由其当前 Repository Authority 和真实项目需要决定；
- 当前证据不支持新增独立 Project Roadmap / Bootstrap Skill；只有后续跨项目真实使用证明存在稳定、独立且可复用的操作职责缺口时才重新评估；
- 不继续扩大方法论研究样本；
- Distribution、Bootstrap 自动化、Controller / Runtime Orchestration 和新的 Skill 只在真实证据满足触发条件时评估。

## 新上下文恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根目录 `AGENTS.md`；
2. 读取本文，确认当前路线、已完成里程碑、当前基线和下一步工作；
3. 读取当前 GitHub `master`，验证是否存在晚于本文的新集成状态；
4. 如果执行 Method 修订，重新读取 Method、Architecture、Contract、Decision、Operating Guide 与相关 Skills；
5. 如果进入 Consumer 验证，切换到 Consumer Repository 并读取其当前默认分支与 Repository Authority；
6. 不依赖 Issue #18、历史聊天或个人记忆补充未固化的项目事实。

## 更新触发条件

出现以下任一情况时，应更新本文：

- 一个项目级里程碑完成、取消或被替代；
- 当前阶段或当前核心目标改变；
- 已确定的下一步工作完成或顺序发生变化；
- 新的真实证据使条件性后续工作进入正式计划；
- 当前路线与 GitHub `master`、Issue、PR 或评估证据不再一致。

普通局部实现、单个 Execution Unit 状态变化或没有项目级影响的修订，不要求更新本文。
