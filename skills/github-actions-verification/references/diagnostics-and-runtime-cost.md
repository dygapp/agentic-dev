# Diagnostics 与 Runtime 成本控制

## 目的

当 GitHub Actions 的失败日志不足、环境准备异常耗时或 Run 被新提交淘汰时，本参考说明如何让 CI 产生足够诊断证据，同时控制无价值等待和重复成本。

## 显式 Timeout

不要把平台默认最大时长当作正常失败边界。

根据正常基线设置：

- Job-level timeout；
- 高成本环境准备 Step timeout；
- service startup / health-check timeout；
- browser / E2E timeout。

Timeout 的目标是区分“正常慢”与“当前 Runtime 已失去继续等待价值”，不是为了机械追求更短。

## 取消过期 Run

当同一 PR/ref 出现新提交时，如果旧 Run 已不能证明最新状态，应使用当前 Repository Policy 允许的 concurrency / cancellation 机制终止过期工作。

常见 GitHub Actions Pattern：

```yaml
concurrency:
  group: <stable-pr-or-ref-key>
  cancel-in-progress: true
```

具体 key 由 Consumer Workflow 决定，不在 Skill 中固定。

## 失败诊断 Artifact

如果 Agent 无法稳定读取完整 Job Log，或远程 Runtime 的关键状态不在默认日志中，应优先让 Workflow 生成可下载的最小诊断 Artifact。

容器化 Runtime 常见诊断包括：

```text
container/service list
container inspect
container logs
health-check result
network / port state
application startup logs
```

浏览器验证常见诊断包括：

```text
trace
screenshot
video when useful
test report
console / network evidence
```

后端或数据库验证可以按需保留：

```text
application logs
migration status
schema / health evidence
failing test report
```

## 诊断流程

推荐：

```text
Observed Failure
→ inspect available Jobs / Steps / Logs
→ evidence insufficient?
   → add minimal diagnostics
   → run again
   → download / read artifact
→ systematic-debug
→ minimal root-cause fix
→ new current verification
```

不要使用：

```text
Step name looks suspicious
→ guess root cause
→ random patch
```

## Runtime Observation 与 Completion

Human 提供的 UI 截图、可见日志、持续时间或人工取消记录，可以证明当前 Runtime 发生异常，也可以支持：

- abort；
- reroute；
- diagnostic enhancement；
- verification strategy adjustment。

但被卡住、取消或失败的 Run 不能作为 Completion PASS。

## 环境准备成本

如果某一步稳定环境准备在每次 CI 中重复支付且成本明显高于业务验证本身，依次评估：

1. 是否可以提前到独立 Build Job；
2. 是否可以传递 Artifact；
3. 是否有官方 / Vendor-maintained 预构建 Runtime；
4. 是否可以使用 service container；
5. 是否可以使用安全且可追溯的缓存；
6. 是否值得维护 Consumer 自有薄镜像。

优化目标是缩短反馈路径，不是牺牲 Completion Verification 覆盖。

## 诊断信息的持久化边界

只有具有跨 Run 或跨 Execution Unit 持续价值的验证 HOW 才进入 Consumer 的长期 Verification Strategy / Workflow。

一次性失败日志、临时调查笔记和完整 debug reasoning 不因为出现过就自动升级为长期 Artifact。
