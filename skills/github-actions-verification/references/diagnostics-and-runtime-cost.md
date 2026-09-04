# Diagnostics 与 Runtime 成本控制

## 目的

当 GitHub Actions 的失败日志不足、环境准备异常耗时、Run 被新提交淘汰或不同 Run 争用共享外部资源时，本参考说明如何让 CI 产生足够诊断证据，同时控制无价值等待、重复成本和资源竞争。

## 显式 Timeout

不要把平台默认最大时长当作正常失败边界。

根据正常基线设置：

- Job-level timeout；
- 高成本环境准备 Step timeout；
- service startup / health-check timeout；
- browser / E2E timeout。

Timeout 的目标是区分“正常慢”与“当前 Runtime 已失去继续等待价值”，不是为了机械追求更短。

## 取消过期 Run 与匹配共享资源并发

当同一 PR/ref 出现新提交时，如果旧 Run 已不能证明最新状态，应使用当前 Repository Policy 允许的 concurrency / cancellation 机制终止过期工作。

常见 GitHub Actions Pattern：

```yaml
concurrency:
  group: <stable-pr-or-ref-key>
  cancel-in-progress: true
```

具体 key 由 Consumer Workflow 决定，不在 Skill 中固定。

稳定 PR / ref key 解决的是“同一逻辑工作的新 Run 淘汰旧 Run”。如果不同 ref 会取得同一个固定域名、代理名、端口、部署槽位、评审环境或临时数据库，该 key 仍可能比真实冲突域更窄。

此时应以共享资源标识或环境槽位建立排他边界，例如：

```yaml
concurrency:
  group: review-environment-<stable-resource-key>
  cancel-in-progress: <true-or-false-by-consumer-policy>
```

要求：

- 每个可能使用同一资源的 trigger / ref 采用同一资源 key；
- 资源不同的运行可以使用不同 key，避免无必要的 Repository 全局串行；
- 长生命周期单实例环境显式记录当前 owner、用途、目标 Head、lease 开始 / 续期 / 到期 / 释放和 stale 判定；不能只从 Run 是否仍为 `in_progress` 推断 Human session 仍然有效；
- PR 自动 Verification 通常只保留完成自动检查和外部地址验证所需的短生命周期；manual Human Review 可以拥有更长且可观察的 lease，但具体时长与续期信号由 Consumer Repository Policy 决定；
- 保护有效 Human lease 与让最新 Head 取得环境是不同目标。只有当前策略判定新 Run supersede 旧工作，且释放闭环可靠时才启用 `cancel-in-progress`；否则有界排队或升级真实优先级冲突，不默认采用 `latest-head-wins`；
- key 只协调 GitHub Run，不能单独证明外部资源已经释放；
- Run 被取消或进程退出后，按正常释放基线进行有界观察；若资源残留，只在 owner、lease / activity、环境和授权明确时执行有界重试、释放或接管；
- 一次性 unlock / recovery Workflow 应使用最小权限、记录目标资源和旧 owner，使用后删除或禁用；它不能成为绕过正常 ownership policy 的长期后门；
- 取得资源后重新读取 owner / status，并验证对外地址或目标服务实际可用且对应当前 Run / Head。

如果资源 owner 不明确，或处理需要清理生产 / 其他 owner 的资源，应停止该项操作并升级，而不是通过扩大 destructive cleanup 绕过竞争。

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

## Artifact 的临时证据与持久输入边界

不要因为 Artifact 已通过 Human Review，就让长期 Importer、Review Environment 或 Runtime 永久依赖该 Actions 对象。先判断角色：

| 角色 | 适合的载体与生命周期 |
|---|---|
| 单次运行证明 / transport / diagnostics / review snapshot | 当前 Run Artifact；允许受 retention / expiry 约束，但要保留 Run、Head、名称 / ID 和 digest 等 Evidence Reference |
| 已被适当 Authority 接受、后续稳定消费的输入 | Consumer 可长期发现和维护的 versioned source / Authority；不以临时 Artifact 作为唯一来源 |

Promotion 的平台实现可以是将已接受内容无损复制、解包或重组到 Consumer 选择的持久载体，但必须：

1. 在复制前后核对 digest、manifest、数量或当前声明需要的完整性属性；
2. 记录 source Run / Head / Artifact、接受责任和 Promotion 目标；
3. 让后续 Workflow 显式读取持久输入，避免隐式回退到即将过期的 Artifact；
4. 对 Promotion 后的最终 Head 重跑受影响的 Importer、fresh environment、Review Runtime 或其他 Completion Verification；
5. 不版本化无持续价值的完整日志、临时诊断或 debug reasoning；
6. 受敏感数据、许可、体积或保留政策限制时，不机械写入 Git，按 Repository Policy 选择对象存储、制品库或其他持久载体。

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
