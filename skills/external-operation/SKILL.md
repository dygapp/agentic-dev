---
name: external-operation
description: Safely performs authorized changes to external or shared state such as GitHub objects, CI runs, remote APIs, review environments, or other mutable services. Use when a task requires an external write or asynchronous external state transition; do not use for read-only inspection or purely local edits.
---

# External Operation

## 目的

对已授权的外部可变状态完成“读取真实状态 → 最小操作 → 重新读取验证 → 汇报”的闭环，不把工具调用成功误报为目标状态完成。

## 输入

- 目标外部对象与期望状态；
- 当前 Repository / Human Authority；
- 可用工具与认证边界；
- 当前外部状态；
- Consumer-local constraints。

## 流程

1. 重新读取目标外部对象的当前事实、Consumer-local constraints 与授权边界。跨多个 Repository 时逐仓确认读、写、Issue / PR、Workflow、merge / release 等权限；某一仓库的认证或写能力不自动授予另一个仓库。
2. 选择满足目标的最小必要、优先可逆操作，不顺带修改无关状态。创建具有持续 identity 的对象前先检查是否已有可复用对象；对可能重试的写入优先使用既有 identity、expected state 或幂等语义，前次结果不明时先重新读取而不是再次 create。
3. 若操作涉及固定域名、端口、部署槽位、临时数据库、单例服务、受限账号等共享资源，先确认真实 resource owner / lifecycle；取得、续期、释放、接管和清理后都重新验证归属，不清理生产资源、有效人工复核资源或其他 owner 的状态。
4. 若外部输入是二进制 / 媒体内容，在版本化或交给运行时消费前验证真实签名 / 类型与必要可解析属性；转换后重新验证。
5. 执行已授权写操作，并重新读取事实来源验证目标状态，而不是只检查写 API 的成功响应。
6. 对异步操作执行有界观察：请求被接受不等于完成；使用合理轮询间隔持续恢复必要 Evidence，直到终态、真实 blocker 或观察上限。失败或超时后重新计算仍可自动完成的诊断 / 修复责任，不因一次子操作终止而静默停止。
7. Workflow artifact、远程任务输出或临时快照默认只承担一次运行的 Evidence / 传输职责；只有当前 Authority 显式接受且后续确需稳定消费时才能晋升为持久输入，晋升后验证完整性、provenance 与持久位置并重新取得受影响 Current Evidence。
8. 只汇报当前证据能够支持的结果；未验证状态明确保留为未验证。

## 可执行路径合同

- `direct-path`：优先使用当前 Runtime 已授权、且能够在操作后重新读取目标真实状态的 connector / API / external tool；工具存在本身不授予权限。
- `automated-alternate`：direct path 不可用时，只能使用 Consumer Repository 已声明、已授权且同样能够恢复当前 Evidence 的自动化路径，例如仓库 workflow、受控 API transport 或等价 external tool；不得临时回 upstream 补工具。
- `evidence-recovery`：保存或恢复目标对象 identity、必要 run / job / step / log / artifact 等当前证据，并以重新读取后的真实状态支持 completion claim。
- `fail-closed`：不存在授权执行路径、缺少 credential / capability、无法恢复目标 identity，或不能重新读取足以支持声明的当前证据时，停止并保留为 blocker / 未验证状态，不报告成功；不得为了绕过本地能力缺口临时在线读取 upstream 方法论源码。

## 输出

- 已执行操作；
- 验证后的当前外部状态；
- 必要诊断 / 当前证据；
- 未验证边界或真实 blocker；
- 需要人工权威时的最小 escalation。

## 退出条件

目标状态已由重新读取的当前证据确认；或已识别无法在当前授权 / 能力内解决的真实 blocker；或异步观察达到既定有界上限并准确保留未验证状态。

## 升级

- 授权无法从当前 Authority 判断；
- merge / release / deploy / destructive remote operation 等被仓库策略保留给人工；
- 高影响或难逆共享状态变化存在多个实质不同方案；
- 当前环境缺少完成或验证操作所需 credentials / capability。

请求人工执行、提供输入或充当系统中转前，先检查当前 connector / API / Git / GitHub / container / Python / browser / Actions 与已存在 Evidence 是否能在不绕过 Authority 的情况下完成；只有不可替代的人类决定、凭证 / 权限、受控环境或法规职责才升级，并明确需要返回的最小 Evidence / decision。工具可用本身不授予任何外部写权限。