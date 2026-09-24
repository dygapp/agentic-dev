# agentic-dev 项目章程

## 1. 使命

`agentic-dev` 的使命是为普通软件项目提供**低认知负担、可直接安装、可独立使用**的 AI 软件开发 Skills，并通过少量 Guides 帮助人和 AI 判断怎样开始、当前下一步做什么。

项目本身不是通用 AI Governance Framework，也不要求 Provider 与 Consumer 运行同构的治理运行时。

## 2. 目标用户与适用域

主要面向新建或持续演进的软件项目，以及希望采用标准 Agent Skills、同时保留自身项目事实、技术政策和授权边界的团队。

## 3. 核心产品边界

正式 Consumer runtime product 只有 `skills/**`。Guides 服务人和 AI 的按需导航，但不作为 ordinary task 固定运行时。

Consumer 始终拥有自己的 Product / Requirement / Architecture / current work / code / tests / authorization / local constraints。Provider governance、Project Knowledge、Research 和内部设计不会因为存在就自动传播到 Consumer。

## 4. 核心目标

- **G1 — 可安装且自包含的 Skills**：每个正式 Skill package 对其通用责任自包含，通过标准 Agent Skills 兼容方式安装，不在线回读 Provider 文档树。
- **G2 — 低成本方法导航**：人和 AI 可以通过 Guides 理解怎么开始、下一步做什么和 Skills 怎样组合，不需要先学习 Provider 内部治理模型。
- **G3 — Consumer ownership**：安装、升级和 Skill execution 不覆盖 Consumer 的项目事实、技术政策、权限和本地约束。
- **G4 — 有界上下文**：普通运行只加载当前责任需要的最小 Repository Authority、Skill、Consumer-local facts 与 Evidence。
- **G5 — 证据驱动且低维护成本**：新增长期抽象、治理层、验证基础设施或 Skill 必须有真实问题和当前 Evidence 支撑；维护成本必须与给 Consumer 带来的收益相称。

## 5. 核心项目需求

1. GitHub Repository 是长期事实来源，Fresh Context 可以从当前仓库恢复必要事实。
2. `skills/**` 是唯一正式 Consumer-facing runtime product。
3. Consumer 项目事实、集成权限与本地约束始终由 Consumer 自己拥有。
4. 普通 Skill execution 不依赖 Provider current state。
5. Guide、Skill references、Research 和历史 Evidence 按需加载。
6. merge、release、deploy、生产变更和破坏性外部操作不因 Skill 或工具能力自动获得授权。
7. 完成、PASS、READY 与高影响复核声明必须由能够区分该声明是否真实成立的当前 Evidence 支持。
8. 高影响 Authority、Skill contract、governance 或产品边界变化在最终集成前接受 Fresh / Independent Review。
9. Provider 自身采用少量直接治理文档，不维护通用 Method selector、Rule Engine、中央 Discovery 或第二套模型 grader。
10. 普通 Provider 修改不得要求批量 LLM 自测或多级 Gate；复杂验证只在声明本身确实需要时启用。

## 6. 非目标

`agentic-dev` 默认不成为 Product / Domain / 业务事实或特定技术栈的中央知识库，不建立通用 Method Runtime、Rule Engine、Rule Discovery、Capability Registry、Runtime Controller 或 custom package manager，也不让 Consumer 日常联网读取 Provider 最新状态。

项目不为了验证方法论本身长期维护大规模模型对模型评分系统，也不把真实 Consumer adoption 设为每次 Provider 重构的固定完成门槛。

## 7. 成功判据

- 新 Agent 能在有限输入下理解 Repository 并找到正确 Skill / Guide；
- Consumer 能安装、更新 Skills 且不丢失 local Authority；
- `agentic-dev` 自身普通修改可以用少量 deterministic tests 和必要 Review 收敛；
- 新复杂度只有在简单机制经真实 Evidence 证明不足后才进入；
- Provider 维护成本显著低于其为真实软件项目节省的返工与协调成本；
- 当前工作树表达最终有效模型，历史原因由 Git / Research 恢复，而不是通过兼容层继续运行。
