# 首次真实 Repository 验证

## 状态

Ready for Execution。

## Goal

验证 `agentic-dev` 作为一个可被独立消费的方法与 Skills Repository，是否能够在完全独立的 Fresh Context 中支撑一个真实 Greenfield Consumer Project 从初始化到 `Ready to Integrate` 的完整开发闭环。

本轮重点验证：

- Operating Guide 是否足以指导新的 Agent 开始工作；
- Project Authority 与 Consumer Repository 自治边界是否清晰；
- Skills 是否能够被正确发现、选择和组合；
- Method 是否能够降低上下文负担并支持持续演进。

本轮不是在 `agentic-dev` 当前会话中开发 Consumer，也不是继续扩展 Eval Framework。

## Experiment Isolation

实验必须在独立 Consumer Context 中进行。

实验 Context 不得继承：

- 当前 `agentic-dev` 开发会话；
- 其他项目聊天历史；
- 未固化的个人记忆；
- 实验设计者口头补充的隐含流程。

Consumer Context 只获得：

1. 指定版本的 `agentic-dev` Repository；
2. Consumer 项目的真实需求来源；
3. Consumer Repository；
4. 当前 Runtime 可观察能力。

如果使用 ChatGPT Project，应优先使用独立 Project 边界；如果使用 Codex，则应使用新的 Session / Context。

## Consumer Project Selection

首个 Consumer 应满足：

- 真实业务目标，而非为验证临时创造；
- 规模可控；
- 可以从最小项目骨架开始逐步演进；
- 不依赖先对大型 Legacy Repository 完成完整 Spec Reconstruction。

当前候选 Consumer：

**jilinjobs 信息发布网站核心重构验证。**

首轮范围：

包含：

- 栏目管理；
- 菜单 / 导航组织；
- 信息发布核心能力；
- 首页；
- 二级页面；
- 内容详情页面。

不包含：

- 外部内容嵌入；
- 用户与权限管理；
- 中心党建二级网站；
- 评论；
- 复杂统计；
- 多站点扩展。

## Operating Guide Validation

Consumer 启动时不提供固定项目模板。

Agent 应首先读取：

```text
agentic-dev/docs/guides/using-agentic-dev.md
```

然后根据真实项目需要建立最小启动骨架。

验证重点：

- 是否可以从最小 Repository Authority 开始；
- 是否会过度创建目录和 Artifact；
- 是否能随着需求逐步形成 Project Rules；
- 是否能自然选择所需 Skills。

项目初始化不预设需要 Bootstrap Skill。

如果实践中反复出现稳定、跨项目的初始化 Procedure，再作为候选能力分析。

## Development Flow

Consumer Agent 根据 Operating Guide 自主推进：

```text
Project Initialization
        ↓
clarify-intent?
        ↓
specify
        ↓
technical-plan? (conditional)
        ↓
slice-work
        ↓
readiness-check
        ↓
execute-unit
        ↓
converge
        ↓
Ready to Integrate
```

不要求所有 Skill 都出现。

不要求所有阶段都产生文件。

不为了验证覆盖率创建无价值 Artifact。

## Experiment Feedback Channel

实验反馈优先通过 `agentic-dev` GitHub Issue 回流。

Issue 作为：

- Evidence Channel；
- 跨 Repository / Context 的跟踪入口；
- 后续分析输入。

Issue 不作为：

- Consumer 项目知识库；
- Method Authority；
- Contract Authority。

建议一个 Consumer Experiment 对应一个 Tracking Issue。

反馈内容只记录：

- 实际观察到的问题；
- Evidence Reference；
- 使用阶段 / Skill；
- Human Intervention；
- Candidate Classification。

不提交：

- 完整 Conversation；
- 完整 Reasoning；
- Consumer Repository 已存在的大量文档副本。

## Evidence Classification

实验结束后，Evidence 回到新的 `agentic-dev` Context 分析。

分类：

- Runtime / Distribution Gap；
- Skill Implementation Gap；
- Contract Gap；
- Method Gap；
- Operating Guide Gap；
- Project-specific Issue。

只有真实证据支持时，才修改对应 Artifact。

## Success Criteria

首轮成功标准：

- 一个新的 Agent 可以仅依靠 `agentic-dev` Repository 和 Consumer 输入开始工作；
- Operating Guide 足以指导项目启动；
- Consumer 可以建立最小必要 Project Authority；
- 至少一个真实 Execution Unit 完成并验证；
- 多 Unit 工作可以使用 Fresh Execution Context 推进；
- Converge 可以基于整体 Evidence 判断 Ready to Integrate；
- 实验产生的发现可以通过 Issue 回流并分类。

## Non-goals

本轮不做：

- 新增第九个核心 Skill；
- 创建固定项目模板体系；
- 创建 Bootstrap Framework；
- 创建 Installer / Registry / Marketplace；
- 创建 Controller / Worker Framework；
- 扩展 Eval Corpus；
- 在当前 `agentic-dev` Repository 内模拟 Consumer 开发。

## Validation Record

执行真实 Consumer Experiment 后追加最小证据摘要。
