# Tasks

Tasks 只承担工作协调职责，不构成 Method、Architecture 或 Skill Contract 权威。

## 项目状态入口

项目演进路线、当前阶段、已完成里程碑、当前核心目标和下一步工作统一维护在：

`docs/project/project-roadmap.md`

Tasks 不重复维护这些易变化的项目状态；这里只定义工作协调规则。

## Plan 使用规则

复杂、多步骤、跨 Fresh Context、需要恢复现场或需要显式阶段协调的工作，可以创建临时 Plan：

```text
tasks/plans/YYYYMMDD/NN-name.md
```

其中：

- `YYYYMMDD` 使用创建日期；
- `NN` 是当日目录内的两位顺序号；
- 文件名使用简短、稳定的英文 kebab-case 描述工作目标。

简单、单 Context、可以直接安全完成的工作不创建 Plan。不得为了形式完整性把每次聊天、每个文件修改或每一步操作都转换成 Task。

Plan 只保存完成当前工作的必要协调信息，例如：

- Goal；
- Authority / Inputs；
- Scope / Non-goals；
- Work Items / Order；
- Blockers；
- Completion Criteria；
- 必要的 Evidence Reference。

不要在 Plan 中复制已有 Method、Architecture、Contract 或长期 Project Knowledge，也不要保存完整 Conversation Reasoning。

## 知识边界与生命周期

- Conversation History、其他会话和其他项目的工作习惯不能直接成为当前 Task 的项目事实；
- Task 中产生新的长期结论时，必须回写到对应权威 Artifact；
- Task 与 Plan 可以记录临时协调状态，但不能通过任务文本修改 Method 或 Skill Contract；
- 已存在权威文档时，只保留引用，不在 Task 中复制一份长期规则；
- 临时 Runtime 输出、Eval 结果和 Workspace 按仓库现有忽略规则处理，不因为出现过就自动升级为长期 Artifact。

## 与 Execution Unit 的关系

`Execution Unit` 是 Method 中的逻辑执行单位，Tasks / Plans 只是可能的承载或协调方式之一。

一个 Plan 可以协调一个或多个 Work Item，也可以引用 Execution Units，但不得改变 Execution Unit 的 Method Contract。是否需要持久化 Task，取决于协调价值，而不是方法阶段是否存在。

## 阶段回写

如果 Task 产生新的 Method Decision，应先更新对应 Method / Decision 文档；如果实现暴露 Skill Contract 问题，应先修改并提交 Contract，再继续 Skill Implementation。

当前项目的详细 Authority 与知识边界以根目录 `AGENTS.md` 为准。
