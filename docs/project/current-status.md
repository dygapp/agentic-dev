# agentic-dev 当前状态与下一步核心目标

本文记录 `agentic-dev` 仓库自身的当前项目状态、近期工作边界与新上下文恢复入口。本文属于 `docs/project/*` 项目级权威，不修改也不覆盖更高优先级的 Method、Architecture 或 Contract Authority。

## 当前基线

截至 2026-08-24：

- 当前阶段仍为 **Skill Operationalization & Method Validation**，没有创建新的方法阶段；
- 第一批 8 个核心 Skill 的 Skill Engineering Baseline 已关闭；
- Issue #18 的首轮真实 Consumer Experiment 已完成；
- 验收到验证的闭环定向强化已通过 PR #30 合并到 `master`；
- PR #30 的 Merge commit 为 `a6ea8ccfb23cb0837d4721192470e3bd11597059`；
- 针对性全新运行时评估为 `4 / 4 PASS`，合计 `21 / 21` 条断言通过；
- 最终 AI 复核没有未解决的阻塞性或中等级别发现；
- Issue #18 已按 `completed` 关闭，相关临时分支已经删除。

`a6ea8ccfb23cb0837d4721192470e3bd11597059` 是 PR #30 的能力集成提交，不是要求后续实验永久固定使用的静态版本。每个新的 Consumer Experiment 开始时，仍应读取并记录当时实际使用的精确 `agentic-dev` baseline。

## 下一步核心目标：继续演进验证

下一步工作的核心目标是：**基于已经完成 Greenfield Bootstrap 和首个真实纵向切片的 Consumer Repository，验证项目在后续真实开发中的继续演进能力。**

优先使用已有真实 Consumer Repository 开展新的真实纵向工作，不为了重复证明启动能力而重新执行同类 Bootstrap。验证重点包括：

1. Fresh Agent 能否只依靠已持久化的 Consumer Authority、当前代码与验证证据恢复工作；
2. Consumer Authority、Specification、必要的 Technical Plan 和长期产物能否随着新需求正确增量演进；
3. 新的真实纵向切片能否完成 `slice-work → readiness-check → execute-unit → converge` 的完整闭环；
4. 每项规格验收义务能否持续闭环到实现责任、验证责任、计划验证证据与已执行的当前证据；
5. `converge` 能否继续独立重建功能整体覆盖，而不依赖执行状态或历史证据；
6. 人工介入是否继续受 Authority、Impact、Reversibility 与 Consumer Repository Policy 约束。

这项工作继续属于 **Skill Operationalization & Method Validation**，不表示重新打开 Core Skill Engineering，也不创建新的方法阶段。

## 工作边界

- Issue #18 保持关闭，不用于承载新的实验；
- 只有新的 Consumer 工作被明确标记为 `agentic-dev` Experiment / Validation 时，才创建新的 Tracking Issue；
- 新实验应在开始时记录 Consumer baseline、精确的 `agentic-dev` baseline、Runtime / Model、Goal 与 Scope；
- 普通 Consumer 开发不要求向 `agentic-dev` 回传过程记录；
- 只有真实证据暴露可重复、稳定的职责缺口时，才依次判断 Usage Guide、Skill Implementation、Contract 或 Method 是否需要修改；
- 不因单次项目特例或 Runtime 限制机械新增核心 Skill、Super-skill、流程层级或评估；
- 当前不继续扩大方法论研究样本；
- Distribution、Bootstrap 自动化、Controller / Runtime Orchestration 仅在真实使用证明必要时评估。

## 新上下文恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根目录 `AGENTS.md`；
2. 读取本文，确认当前阶段、已完成基线与下一步核心目标；
3. 读取当前 GitHub `master`，确认是否存在晚于本文的新集成状态；
4. 判断当前工作是普通 Consumer 开发，还是明确的 `agentic-dev` Experiment / Validation；
5. 只加载当前工作真正需要的 Method、Operating Guide、Skills、Consumer Authority 与当前证据；
6. 不依赖 Issue #18、历史聊天或个人记忆补充未固化的项目事实。

## 本轮继续演进工作的收敛条件

一次新的继续演进验证应至少满足：

- 新的真实纵向工作达到由当前证据支持的 `Ready to Integrate`，或者明确记录无法达到该状态的阻塞事实；
- 如果属于实验，相应 Tracking Issue 已记录 Final Summary 与可核实的 Consumer Evidence Reference；
- 新发现已完成 Usage Guide / Skill Implementation / Contract / Method / Project Rule / Runtime 分类；
- 只有证据充分时才提出或实施 `agentic-dev` 修改；
- 如果没有暴露通用缺口，明确记录“不需要修改 `agentic-dev`”也是有效结论。
