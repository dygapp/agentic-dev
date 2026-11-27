---
name: activate-model-collaboration
description: Establishes and validates a Consumer-local model/agent collaboration instance using the installed Skill package. Use to detect actual runtime capabilities, choose a bounded strategy, configure local mapping, validate delegation and fallback, and enable only the verified scope.
---

# activate-model-collaboration

## 目的

在当前 Repository 已安装本 Skill 的前提下，建立、验证并按证据启用 Consumer-local collaboration instance；普通运行只依赖已安装 Skill 与 Consumer-local Authority，不在线读取 upstream Source 补能力。

## 输入

- 当前已安装 Skill package 与版本 / provenance；
- Consumer Repository Authority；
- 实际 Runtime / provider 能力；
- 当前 collaboration config / policy；
- Consumer-local constraints。

## 流程

1. 确认本 Skill 已安装且当前版本 / provenance 可恢复；缺失时返回安装或显式版本更新责任，不读取 upstream Source 临时补齐。
2. 区分当前 Primary execution context 与 Runtime Under Test。ordinary reasoning、仓库操作、deterministic verification 或 fresh review 能在当前执行面完成时，不为了“多模型”本身启动额外 Runtime；只有 claim 明确依赖 provider / runtime-specific behavior 时才探测真实目标 Runtime。
3. 对真实 Runtime 探测 child agent / thread、model / effort、权限隔离、并发、observability 与结果恢复能力；requested config、输出风格或 Agent 自述都不能替代 runtime fact，不可观察时明确记为 unknown。
4. 选择 `disabled`、有界 basic、reviewed 或 Consumer 自定义策略；具体模型映射、并发数与 provider 配置只属于 local instance。
5. 建立或更新 local collaboration instance，保持明确 Primary Agent、bounded delegation、single-writer、shared-resource owner / lifecycle、独立 review 与可验证 single-agent fallback。
6. 对准备启用的每条 role path 做真实 delegation / authority / writer / evidence / fallback 验证；child run 的启动或单次成功不等于整个 activation responsibility 完成。
7. 只启用已验证范围；失败、超时或不可观察路径保持 disabled / fallback，并继续处理当前责任内可自动关闭的剩余诊断，直到满足退出条件或出现真实 blocker。
8. 区分 functional enablement 与 efficiency / preferred-default claim：链路可用只能证明功能启用；若要声称更省成本、更快或应成为默认策略，必须与可比较的 single-agent baseline 建立当前 Evidence。
9. 记录 local instance、当前 Evidence、observability limitation、资源 ownership 与 fallback；不改变 Consumer 的产品 / Requirement / 集成授权。

## 输出

- Consumer-local collaboration instance；
- Runtime capability matrix；
- Enabled / conditional / disabled status；
- Current validation evidence；
- Fallback path / blocker。

## 退出条件

当前启用范围与可观察 Evidence 一致，single-agent fallback 可执行，ordinary runtime 不依赖 upstream Source Repository。

## 升级

如果本 Skill 未安装、需要改变通用 collaboration semantics，或出现 Repository Authority / 高影响权限冲突，返回显式版本更新、upstream evolution 或人工 Authority。请求人工前先检查当前已授权工具、Evidence 与等价自动路径，只升级不可替代的人类责任。本 Skill 不授予 merge、release、deploy 或破坏性外部操作权限。
