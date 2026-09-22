---
name: activate-model-collaboration
description: Establishes and validates a Consumer-local model/agent collaboration instance after the installed Release already provides the collaboration capability. Use to detect actual runtime capabilities, choose a bounded strategy, configure local mapping, validate delegation and fallback, and enable only the verified scope.
metadata:
  agentic-dev-id: "skill:activate-model-collaboration"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
  agentic-dev-release-inputs: "method:model-collaboration-adoption;architecture:model-collaboration;rule:human-intervention-necessity;rule:shared-resource-concurrency-ownership;rule:evidence-type-must-match-claim;rule:execution-context-runtime-boundary;rule:execution-continuity-and-stop-condition;rule:verification-contract-currentness"
---

# activate-model-collaboration

## 目的

在当前 installed Release 已经提供 Model Collaboration capability 的前提下，建立、验证并按证据启用 Consumer-local collaboration instance；不通过在线读取 upstream Source 补能力。

## 输入

- Current installed release；
- Consumer Repository Authority；
- 实际 Runtime / provider 能力；
- 当前 collaboration config / policy；
- 当前运行环境提供的 packaged references 与 Consumer-local policy。

## 流程

1. 确认当前 installed release 已包含本 Skill 及其 references；若缺失，返回 Consumer Release 安装 / 升级责任。
2. 读取 Model Collaboration Architecture / activation Method 与相关 verification / concurrency references。
3. 先区分 Primary execution context 与 Runtime Under Test，再只对当前 capability claim 不可替代的真实 Runtime 探测 child agent / thread、model / effort、权限隔离、并发、observability 与结果恢复能力；不把静态配置当作 runtime fact，也不为了“多模型”本身扩大额外模型执行范围。
4. 选择 `disabled`、有界 basic、reviewed 或 Consumer 自定义策略；具体模型映射只属于 local config。
5. 建立或更新 local collaboration instance，保持明确 Primary Agent、bounded delegation、single-writer、独立 review 与 single-agent fallback。
6. 对准备启用的每条 role path 做真实 delegation / authority / writer / evidence / fallback 验证。
7. 只启用已验证范围；失败或不可观察路径保持 disabled / fallback，不把 requested configuration 冒充 observed runtime。
8. 记录 local instance、当前 Evidence、observability limitation 与 fallback，不改变 installed release identity。

## 输出

- Consumer-local collaboration instance；
- Runtime capability matrix；
- Enabled / conditional / disabled status；
- Current validation evidence；
- Fallback path / blocker。

## 退出条件

当前启用范围与可观察 Evidence 一致，single-agent fallback 可执行，ordinary runtime 不依赖 upstream Source Repository。

## 升级

如果所需 capability 不在 installed Release、需要改变通用 collaboration semantics，或出现 Repository Authority / 高影响权限冲突，返回 Release Upgrade / upstream evolution 或人工 Authority。本 Skill 不授予 merge、release、deploy 或破坏性外部操作权限。
