# AGENTS.md

## 仓库职责

`agentic-dev` 用于定义通用的 AI Agent 驱动软件开发方法，并维护工程纪律、技术画像、验证画像、使用方生命周期、小型可组合 Skill 与运行时适配等可复用工程能力。

本文件只维护**稳定的仓库治理、权威边界与 Agent 工作约束**，不承担当前阶段、当前里程碑、候选路线、Issue / PR 状态、实验进展或下一工作项的状态记录。

当前项目状态的职责分工：

- `README.md`：面向人的简短当前状态与稳定入口；
- `docs/project/project-roadmap.md`：详细当前阶段、活动里程碑、候选与下一 Gate；
- `docs/project/*`：具体里程碑、项目治理与设计记录；
- Git / PR / Issue / Actions：精确外部状态与执行证据。

不得为了方便恢复上下文，把这些易变化状态重新复制回 `AGENTS.md`。

**方法定义高于 Skill 实现。** Skill 必须实现方法与架构已经允许的职责，不得通过修改 `SKILL.md` 暗中改变方法、架构或仓库权威。

## 权威顺序

发生冲突时按以下顺序处理：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/method/principles.md`
4. `docs/architecture/engineering-capability-architecture.md`
5. `docs/architecture/consumer-lifecycle.md`
6. `docs/architecture/skill-architecture.md`
7. `docs/architecture/skill-contracts.md`
8. `docs/decisions/method-decisions.md`
9. `docs/architecture/engineering-disciplines.md`
10. `docs/architecture/technology-profile-contract.md`
11. `docs/technology-profiles/*`
12. `docs/project/*`
13. `docs/guides/git-commit-guidelines.md`
14. `docs/research/*`
15. 任务与临时工作记录

`docs/project/*` 只定义 `agentic-dev` 仓库自身的项目级治理与运行状态，不得覆盖更高优先级的方法、架构、契约、工程纪律或技术画像权威，也不得被 Consumer 自动继承。

## 仓库事实与知识边界

GitHub Repository 是本仓库唯一的长期项目事实来源。

- Git 提交记录项目演进历史；
- 分支用于隔离实验、设计和实现；
- ZIP 只用于初始化、离线交换或临时备份，不作为持续开发上下文来源；
- 会话历史、其他项目、个人记忆和未固化推理不构成本项目权威；
- 外部项目和外部资料可以成为研究输入，但只有按当前权威层级显式固化后才能改变本项目长期规则；
- 其他仓库拥有自己的 Repository Authority；本仓库的项目状态、路线、提交约定和治理细节不得自动成为其他项目事实；
- 新的长期结论应进入其真实 semantic owner，例如 Method、Principle、Architecture、Contract、Engineering Discipline、Guide、Skill 或 `docs/project/*`，不能只停留在聊天或临时计划中。

复杂、多阶段或需要跨新上下文协调的工作遵循 `tasks/README.md`；简单工作不得为了形式完整性创建计划。

## 工作入口与上下文加载

新的 `agentic-dev` 工作上下文按以下顺序恢复：

1. 读取本文件，取得稳定 Repository Governance 与 Authority Boundary；
2. 读取 `README.md`，取得简短当前状态和稳定入口；
3. 读取 `docs/project/project-roadmap.md`，确认当前阶段、活动里程碑和下一 Gate；
4. 只在当前任务需要时读取对应项目记录、Issue、计划、Method、Architecture、Guide、Skill、Research 或历史证据；
5. 已关闭里程碑、历史评估和完整 Research 不作为普通 Fresh Context 默认输入。

方法生命周期、WHAT / WHY 与 HOW、阶段、执行单元、上下文适配、证据、人工升级等方法语义由 `docs/method/*` 及相应 Architecture / Skill Contract 单点定义；本文件不维护第二份方法摘要。

Consumer 使用 `agentic-dev` 时，从 `docs/guides/rule-activation-guide.md` 和 Consumer 自己的 Repository Authority 进入；面向人的初始化 / 采用 / baseline upgrade 说明见 `docs/guides/using-agentic-dev.md`。Consumer 初始化、首次采用、baseline upgrade、采用验证、ordinary runtime local-only 与 upstream re-entry 的规范生命周期由 `docs/architecture/consumer-lifecycle.md` 定义。

## 外部操作治理

具备 GitHub、仓库、Issue、PR、外部 API 或其他可改变外部状态的工具能力，不等于自动获得操作授权。

所有外部状态修改遵循最小闭环：

```text
读取当前状态
→ 判断权限与最小操作
→ 执行
→ 重新读取并验证
→ 只汇报已验证状态
```

跨仓库授权必须分别确认。合并、发布、部署、破坏性清理及其他高影响或不可逆操作继续受人工权威或仓库策略控制。

详细规则见 `docs/guides/external-operation-guidelines.md`。

## AI 复核

本节只约束 `agentic-dev` 仓库自身，不自动投射给 Consumer。

会实质改变 Method、Principle、Architecture、Contract、核心 Skill、Repository Authority、`docs/project/*` 或后续 Agent 行为的高影响变更，在进入最终人工复核或集成决策前必须完成与风险相称的 AI 复核。

只有不存在未解决的 Blocking / Medium Finding 时才能声明 AI 复核通过；AI 复核通过不等于人工批准，也不授予合并或其他集成权限。

完整规则见 `docs/project/ai-review-guidelines.md`。

## 中文表达

`agentic-dev` 面向人的仓库内容与协作输出默认使用自然中文；代码标识符、文件路径、命令、API / CLI 参数、Git 引用、Skill 调用名、外部正式名称、协议和必须精确匹配的固定值保持原样。

正式概念身份与详细表达规则统一见 `docs/guides/terminology-guidelines.md`；不得从历史聊天、其他项目或个人记忆恢复已被当前规则取代的表达方式。

## 研究与能力采用

`docs/research/*` 只保存研究依据和横向比较，不因外部项目、论文、工具或规范使用某种机制就自动改变本仓库 Method / Architecture / Skill。

外部证据进入长期能力前必须先完成当前仓库的证据分类与架构适配。Consumer 采用时只选择对自身持续工作有价值的可复用能力，并按 `docs/architecture/consumer-lifecycle.md` 的生命周期形成 Consumer-local current state；`agentic-dev` 自身项目规则和当前项目状态不自动继承。

同一 Runtime scope 中，同一个 discovery responsibility 只能有一个被声明为 current 的机制。被新机制取代的派生 index / catalog / retriever 必须退出 Current Runtime / Eval surface 或明确降为冻结历史证据；仍声明为 current 的派生机制必须保持 source-currentness 与语义映射真实有效，不允许保留“可执行但已陈旧”的中间状态。

研究入口见 `docs/research/README.md`，Consumer 使用说明见 `docs/guides/using-agentic-dev.md`，规范采用生命周期见 `docs/architecture/consumer-lifecycle.md`。

## Git 提交

所有提交遵循 `docs/guides/git-commit-guidelines.md`。提交格式、`scope`、摘要和分层提交规则只在该规范中维护。