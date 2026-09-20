---
id: rule:safe-external-write
type: rule
status: active
distribution: release-input
release-target: software-development
scope:
  phases: []
  activities: [external-operation]
  technologies: []
  artifacts: []
  risks: []
---

# 安全外部写操作

任何会改变 Repository、Issue / PR、Workflow、部署、远程服务或其他外部可变状态的写操作，都按同一安全责任链执行。

## 先确认授权

工具能力、认证成功或 API 可写不等于已经获得操作授权。写入前必须从当前 Repository / Human Authority 确认目标、范围和允许的动作。

合并、发布、部署、破坏性清理以及其他仓库策略明确保留给人工或高影响审批的操作，不得因为技术上可执行而自动执行。

## 只做最小必要变更

一次外部变化保持单一主要目的，只执行达到当前目标所需的最小变更；不顺带修改无关对象，不为了形式完整扩大范围，也不基于未经重新读取验证的旧状态继续操作。

存在等价方案时，优先选择更可逆、影响面更小且容易重新验证的路径。

## 创建前检查可复用对象

准备创建具有持续身份或后续生命周期的远程对象时，先在当前目标范围内重新读取并检查是否已经存在语义相同、可以继续推进的对象，例如同一 bounded change 的 Issue、PR、branch、deployment / environment ownership 或其他有身份的远程资源。

如果已有对象能够承担当前目标，优先更新、复用或继续该对象；只有当前 Authority、对象状态或语义边界确实要求新的独立对象时才创建新的对象。不得因为重试、工具返回不明确、会话切换或未先查询 current state 而机械重复创建。

对可能被重试的写入，尽量使用平台已有的对象 identity、expected current state、幂等语义或等价防重机制；无法确认前一次写入结果时，先重新读取目标系统，而不是直接再次执行 create。

## 写后重新读取真实状态

外部写 API 返回成功只证明操作被接受或执行，不证明目标状态已经成立。写操作后必须重新读取对应事实来源，确认文件、Issue、PR、分支、Workflow、部署或其他目标对象的实际当前状态。

验证失败时重新分析，不得继续基于预期状态执行后续操作。