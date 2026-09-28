---
id: guide:github-actions-automated-verification
type: guide
status: active
---

# 基于 GitHub Actions 的自动化验证

本文帮助使用 GitHub 的 Consumer 把 AI 开发中的构建、测试、集成与必要的浏览器验证组织为可观察的自动化路径。它与[本地 Docker 自动化验证](docker-automated-verification.md)是两种可独立选择的执行方式，不要求同时运行，也不把 GitHub Actions 设为所有项目的默认门槛。普通变更的目标、执行粒度与完成判断仍见[普通 Feature / change 指南](feature-development.md)；Actions 的可执行责任由已安装的 `github-actions-verification` Skill 持有。

## 1. 先决定这条路径证明什么

从 Consumer 当前 Authority 和变更范围列出需要证明的行为、质量属性与失败边界，再决定哪些检查由 GitHub Actions 运行。Workflow 只执行 Repository 自己拥有的构建与测试命令，不成为第二份 Requirement、Acceptance 或技术政策。

开发反馈可以只运行受影响的快速检查；最终完成声明所需的完整验证按 Consumer 政策执行。快速通过不能改称完整通过，也不因存在 Actions 就要求每次本地编辑都触发远端 Run。若项目选择本地 Docker 路径完成相应验证，则不必为保持形式对称而重复运行 Actions；但项目已经明确要求的 GitHub 检查仍须满足。

## 2. 建立可追溯的运行对象

将本次声明绑定到明确的 Repository、目标 commit / PR Head 以及实际 checkout。PR merge ref、PR Head 与目标分支 Head 是不同 subject；不能只凭触发事件名称推断运行了哪个版本。跨仓集成声明还需记录参与仓库的精确身份与版本组合，不能由一个仓库的 SHA 代表整个项目。

GitHub 的 `pull_request` 事件默认可以检出合并引用；若声明针对 PR Head 本身，须明确选择并核对实际 checkout。具体事件语义以 [GitHub 官方说明](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)为准。

Workflow 应使 Agent 能恢复触发、checkout、关键 job / step、终态、日志与必要报告。Run 已创建或某个步骤成功，只证明对应阶段发生；只有与当前 claim 匹配的检查达到终态且证据可恢复，才支持相应通过结论。失败、取消、超时或证据缺失要保留原状并定位原因，不能把重试请求当作修复完成。

## 3. 控制反馈成本而不降低验证责任

按实际影响范围安排快速反馈与完整验证。未变化组件的已验证构建产物可以复用，但要区分目标源码身份、产物输入身份与原始生产者；缓存命中只省去重复构建，不自动省略当前目标仍需运行的测试。GHCR、Actions cache 或预构建容器都是可选实现，不是本 Guide 对 Consumer 的依赖要求。

当输入变化使缓存失效时，重新构建并验证候选后再将其作为可复用产物。未知的 Registry、权限或网络错误不能伪装成正常缓存未命中。合理设置超时、取消和证据保留；共享评审环境、数据库或固定入口须有真实 owner 与释放验证，不能用 Run 取消推断资源已经释放。

## 4. 失败与收敛

失败后先恢复实际 job / step / log，区分实现缺陷、过期验证契约、运行环境和外部依赖，再使用 `systematic-debug` 或当前责任的等价诊断路径。修复产生新 commit 时，重新绑定目标并取得受影响声明所需的证据；旧 Head 的绿色 Run 只有经过精确差异与逐项 claim 影响分析才能复用，且仍是旧 Head 的 Run。

`execute-unit` 或有界直接变更负责当前实现与按范围验证，`converge` 负责最终 Authority、实现和证据是否一致。需要触发、观察或修改 Actions 等外部状态时按 `github-actions-verification` 与 `external-operation` 的适用责任执行；本 Guide 不复制它们的操作契约，也不授予 merge、release 或 deploy 权限。

## 5. 与本地 Docker 路径的关系

两条路径共用 Consumer 的目标、验收与证据要求，但运行位置、缓存和证据来源不同。GitHub Actions 的 Run / Job 是 GitHub 原生事实；本地 Docker 的日志与报告不是 Actions Run。选择或更换路径时，逐项核对原来由 Actions 证明的声明是否已有同等可辨别的当前证据，再按 Consumer 自己的集成政策调整检查要求；不能仅因本地命令退出码为零就宣布整条验证路径等价。

本 Guide 只适用于选择 GitHub Actions 的项目。非 GitHub 仓库可以直接使用[本地 Docker 自动化验证](docker-automated-verification.md)，不需要迁入 GitHub、建立虚拟 PR 或引入 GHCR。
