# 项目路线图（Project Roadmap）方法修订计划

**状态：** In Progress  
**日期：** 2026-08-24  
**分支：** `codex/project-roadmap-method`

## 目标

把项目路线图定义为一种**条件性长期项目级产物**：当项目跨越多个里程碑、阶段或 Fresh Context，且仅凭功能级与任务级产物无法可靠恢复整体路线和当前状态时，用它承载可发现的项目演进路线、当前核心目标和下一步工作。

同时补齐启动、恢复、更新和收敛检查规则，使后续 Agent 不依赖聊天记忆，也不必重新分析整个仓库才能恢复真实项目状态。

## 权威与证据

- `AGENTS.md`
- `docs/method/ai-development-method.md`
- `docs/method/principles.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `docs/guides/using-agentic-dev.md`
- `docs/project/project-roadmap.md`
- agentic-dev 与首个 Consumer 项目暴露的 Fresh Context 状态恢复问题

## 范围

1. 在 Method 与 Principles 中定义项目路线图的适用条件、边界和完整生命周期。
2. 在 Skill Architecture 中把条件性项目路线图纳入 Project Initialization / Bootstrap Capability，但不新增 Skill。
3. 在 `converge` Contract 与 Skill 中增加窄范围检查：已有且适用的项目路线图因本次工作跨越更新触发条件而失效时，阻止 `READY` 并路由到有权维护项目路线的职责层。
4. 在 Operating Guide 与 README 启动提示中增加薄入口，避免复制 Method 或强制固定模板。
5. 新增一个隔离 Runtime Behavior Eval，验证陈旧但适用的项目路线图能被识别为 Artifact Lifecycle Gap。
6. 记录方法决策，并在证据完成后更新本项目 Project Roadmap。

## 非目标

- 不把项目路线图设为所有 Consumer 的必需文件。
- 不强制所有仓库使用固定路径或固定模板。
- 不新增方法阶段、核心 Skill、非核心 Skill 或 Super-skill。
- 不扩展研究样本。
- 不在本 PR 中修改 Consumer Repository。
- 不把完整规则复制进启动提示词。
- 不让 `converge` 自行规划路线、创建 Roadmap 或发明下一步工作。

## 工作顺序

1. Method / Principles
2. Skill Architecture / Contract
3. Operating Guide / README
4. `converge` Skill
5. Behavior Eval / Eval 说明
6. Decision Record / 本项目 Roadmap
7. 中文规范、术语一致性与结构复核
8. Fresh Runtime Eval 与语义评分
9. PR 收敛

## 完成条件

- 适用触发条件明确，普通小型或一次性工作不会被机械要求创建 Roadmap。
- Producer、Trigger、Consumer、Persistence、Update、Supersede、Escalation 均有明确归属。
- 已有且适用的 Roadmap 在里程碑完成、取消或取代，当前阶段 / 核心目标变化，或已决定的下一步顺序变化后，不得保持陈旧并同时得到 `READY`。
- 与项目路线无关的局部功能不会被要求更新 Roadmap。
- `converge` 只识别和路由 Gap，不自行修改路线权威。
- 新增场景 `B-CG-07` 经过 Fresh Runtime 执行并完成语义评分。
- 修改文档通过中文规范、权威边界、交叉引用和状态一致性复核。
