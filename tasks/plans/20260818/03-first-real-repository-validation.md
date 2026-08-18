# 首次真实 Repository 验证

## 状态

Ready for Execution。

当前不绑定具体 Consumer Repository 或虚构需求。执行开始条件是出现一个真实 Feature / Defect Work Item。

## Goal

在独立 Consumer Repository 中，使用 `agentic-dev` 当前 `master` 的 Method、Project Rules 与第一批 8 个核心 Skills 完成一次真实软件工作，验证该体系是否能够在不依赖历史 Conversation 的情况下自然推进到 `Ready to Integrate`，并用真实证据识别是否存在 Runtime、Skill、Contract、Method 或 Project Rule Gap。

本轮目标是验证真实使用效果，不是继续扩展 Eval Framework。

## Authority / Inputs

执行时只使用以下输入：

1. `agentic-dev` 当时的 `master` commit，并记录 commit SHA；
2. Consumer Repository 自己的 Repository Authority，例如 `AGENTS.md`、项目文档、源码、测试与配置；
3. 一个真实存在的 Feature / Defect Work Item；
4. 当前 Runtime 可以直接观察到的能力与行为。

不得把历史聊天、其他项目经验或未固化个人记忆当作 Consumer Repository 的事实。

## Pilot Work Item 选择

优先选择满足以下条件的真实工作：

- 来自 Consumer Repository 的真实待办，而不是为了验证临时创造的需求；
- 范围中等、可回滚、风险可控；
- 有明确可执行的 Verification；
- 最好能够自然形成 2–3 个 Execution Units，以观察 Fresh Context 与组合调用；
- 不要求必须使用全部 8 个 Skills；
- 不为了满足验证形式人为拆分本来只需要一个 Unit 的简单工作。

如果当前没有这样的真实 Work Item，本 Plan 保持 Ready，不以模拟任务代替。

## Runtime Preparation

在 Consumer Repository 的干净 branch / worktree / workspace 中执行。

- 不复用历史 Eval 留下的 `.agents/`、workspace 或 results；
- 从已记录 SHA 的 `agentic-dev` Skills 源重新安装或加载 Skills；
- 使用当前 Runtime 实际支持的安装 / discovery 方式，不在本 Plan 中预设工具路径；
- 记录实际安装方式以及 8 个 Skills 是否可发现；
- 不复制 `agentic-dev/evals` corpus、expected answers 或历史运行结果到 Consumer Repository。

安装 / discovery 如果失败，直接记录 Runtime / Distribution Evidence，不先建设通用 Installer Framework。

## Execution

### 1. 从 Consumer Repository Authority 开始

Fresh Coordination Context 只读取完成当前工作所需的 Repository Authority 与真实 Work Item。

先确认 Intent 和已有权威是否足够；不得通过回忆其他会话补全缺失事实。

### 2. 自然使用 Workflow Skills

按真实需要使用：

```text
clarify-intent?
→ specify
→ technical-plan?  (conditional)
→ slice-work
→ readiness-check
→ execute-unit
→ converge
```

规则：

- 不要求每个 Skill 都必须触发；
- `technical-plan` 只有存在需要长期固化的 HOW 决策时才使用；
- Defect 如果需要诊断，可自然进入 `systematic-debug`；
- 不为了验证覆盖率制造不必要 Artifact 或流程阶段。

### 3. Fresh Execution Context

每次 `execute-unit` 只执行唯一 Current Unit。

当 Work Item 自然形成多个 Units 时：

- Coordination Context 只保留队列、当前状态、必要 Artifact Reference 与 Blocker；
- 每个 Unit 使用新的 Fresh Execution Context；
- Worker 只加载当前 Unit 和必要 Repository Authority；
- 不把前一个 Worker 的完整 Conversation History 传给下一个 Worker。

本轮允许人工充当 Controller。没有真实证据前不实现 Controller Framework。

### 4. Converge

所有计划 Units 完成后执行 Feature-wide / Defect-wide convergence。

只有当前实现、Intent、Specification（如存在）与 Verification Evidence 已收敛，且没有 Blocking Gap，才达到 `Ready to Integrate`。

Merge / Push / Release / Deploy 继续由 Consumer Repository 的 Human Authority / Repository Policy 决定。

## Minimum Evidence

本 Plan 内只保留最小验证记录，不新增独立 Validation Report 目录。

执行完成后补充：

- Consumer Repository 与 baseline / branch；
- `agentic-dev` commit SHA；
- Runtime / model；
- 实际 Skill 安装 / discovery 方式；
- 实际使用或观察到的 Skills；
- Execution Units 与各自 Evidence Reference；
- Verification Commands / Results；
- 发生过的 Human Intervention，以及是否属于 Authority / Impact / Reversibility 边界；
- 最终状态：`Ready to Integrate` / Blocked；
- 发现的 Gap Classification。

不保存完整 prompt、完整 reasoning 或重复 Repository Knowledge。

## Gap Classification

发现问题后先分类，再决定是否修改 `agentic-dev`：

- **Runtime / Distribution Gap**：安装、发现、调用、Fresh Context 启动等 Runtime 问题；
- **Skill Implementation Gap**：现有 Contract 正确，但 `SKILL.md` 行为不符合；
- **Contract Gap**：职责、输入输出或 Stage Return 本身定义不足；
- **Method Gap**：生命周期、Authority、Execution / Convergence 语义存在缺口；
- **Project Rule Gap**：Consumer Repository 缺少自身必要的项目级权威或约束。

只有真实证据支持时才修改对应层。不得因为一次不便就新增 Skill 或 Runtime Layer。

## Success Criteria

首轮验证成功不要求证明整个方法“最终正确”，只要求获得足够真实证据继续收敛：

- Skills 能从记录的 `agentic-dev` baseline 在干净 Consumer Repository 中重新安装 / 加载并被 Runtime 发现；
- Workflow 可以从真实 Intent 推进，而不依赖历史 Conversation；
- 至少一个真实 Execution Unit 被实际实现并使用 Current Evidence 验证；
- 如果存在多个 Units，它们由独立 Fresh Execution Context 执行；
- `converge` 基于整体当前状态判断，而不是重复 Unit Completion Claim；
- Human Intervention 主要发生在真实授权边界，而不是日常低风险实现细节；
- 没有为了形式完整性制造明显无价值 Artifact；
- 最终达到 `Ready to Integrate`，或形成一个有证据、可分类的真实 Blocker。

## Non-goals

本轮不做：

- 新建第九个核心 Skill；
- 预先建设 Installer / Registry / Marketplace；
- 预先建设 Controller / Worker Framework；
- 扩展 Activation / Behavior Eval corpus；
- 强制全部 8 个 Skills 出场；
- 强制 Technical Plan；
- 使用 `agentic-dev` Eval Runner 自身作为首个 Consumer Feature；
- 为验证需要凭空创造产品需求。

## Validation Record

执行真实 Work Item 后在本节追加最小证据摘要。

当前状态：**尚未选择真实 Consumer Work Item。**

这不是 Method Blocker；在真实待办出现前保持 Ready，不以模拟验证替代。
