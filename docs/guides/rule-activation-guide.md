# 规则激活导航

本文是 `agentic-dev` 面向使用方的**低频采用 / 恢复导航 Guide**。它帮助人和 Agent 找到初始化、首次采用、基线升级、实验与 Consumer-local 普通运行的正确入口，但**不再维护 ordinary runtime 的手工职责 / 风险路由表**。

长期规范语义分别由当前 Repository Authority、使用方生命周期、资源模型、资源发现架构、Skill / Engineering Capability 与 Consumer 自己的仓库权威持有。

## 1. 先区分工作位置

### 1.1 在 `agentic-dev` 仓库自身工作

普通 Fresh Context 从本仓库：

`docs/discovery/README.md`

进入本地发现机制。

该入口只使用 `agentic-dev` 自身当前资源；本 Guide 不再作为本仓库 ordinary runtime 的 current discovery mechanism。

### 1.2 新 Consumer 初始化 / 首次采用

规范生命周期：

`docs/architecture/consumer-lifecycle.md`

面向人的说明、初始化示例与采用方式：

`docs/guides/using-agentic-dev.md`

Consumer 自己的 Repository Authority 始终决定项目事实、权限与本地化方式。

### 1.3 已有 Consumer 基线升级

先按：

`docs/architecture/consumer-lifecycle.md`

执行显式重新进入上游、逐项采用 / 保留 / 覆盖 / 拒绝 / 取代、采用验证和基线推进。

需要人类说明时再读取 `using-agentic-dev.md`。上游出现新提交本身不会自动改变 Consumer 普通运行。

### 1.4 已完成采用的 Consumer 普通运行

完成采用后，普通运行必须回到 **Consumer 自己的 Local Discovery Entry / Current Authority**。

长期发现语义以：

`docs/architecture/resource-discovery-architecture.md`

为上游规范；如何在 Consumer 中落地见：

`docs/guides/consumer-local-rule-activation.md`

这不意味着 Consumer 普通任务需要在线读取本仓库。本地化完成后，ordinary runtime 默认只依赖 Consumer-local current state。

## 2. 低频使用场景

本 Guide 只在以下场景作为导航入口有持续价值：

- 新 Consumer 初始化；
- 首次采用 `agentic-dev`；
- 显式 baseline upgrade；
- 需要理解上游 Method / Skill / Engineering Capability 如何投射到 Consumer；
- 明确的 `agentic-dev` Consumer 实验 / validation；
- 人工需要解释 adoption / localization / recovery 路径。

如果当前工作已经在某个 Consumer 的普通运行阶段，应优先使用该 Consumer 自己的本地入口，而不是回到本 Guide 重新做职责路由。

## 3. 本 Guide 不拥有的语义

本文不再维护第二份：

- Method Stage / Stage Return；
- Skill Use When / Procedure；
- 工程纪律触发规则；
- 验证 / 证据条件表；
- 外部操作条件表；
- 技术画像适用规则；
- primary responsibility / supporting context 路由表；
- stale / missing / ambiguity 算法；
- Manifest / Catalog schema；
- current-state 真值。

这些内容由当前真实 semantic owner 与 `docs/architecture/resource-discovery-architecture.md` 单点持有。

## 4. 安全边界

无论处于哪种使用场景，都保持：

1. Consumer Repository Authority 优先；
2. 普通运行默认只依赖 Consumer-local current state；
3. 未知条件不猜测；
4. 派生发现陈旧 / 缺失 / 歧义时回到本地当前权威；
5. fail-closed 不自动访问 upstream；
6. 完成 / 通过 / 可集成声明必须有匹配的 Current Evidence；
7. 使用方项目状态、Requirement、Architecture、Issue / PR / Actions 不从 `agentic-dev` 项目状态自动继承。

完整语义仍应从对应 current owner 读取；本 Guide 只负责把低频使用者带到正确入口。