# C3 隔离运行时与公平性证据 Readiness

记录日期：2026-09-09

阶段：**规则治理与知识激活 v1 / 阶段 C / C3 — 隔离运行时与人工评分**

文档性质：**Research / Evaluation Evidence，不是 Repository Authority**

集成起点：

`master@d06c87489677c8307e4c0e3be305bbaab5fb2cfd`

## 1. 问题

C1 已冻结：只有 A / B 两侧使用同一实际模型与推理强度，配对才可以进入效果比较。

C2 故意没有把请求参数或本地配置冒充为实际运行事实，因此 `model` / `reasoning_effort` 保持空值。这一边界在进入真实 C3 前必须解决，否则即使 18 个 Codex 进程全部退出 0，也不能证明 A/B 公平性。

本步骤只解决：

> **如何在不破坏 `--ephemeral --json` 隔离边界的前提下，为每个真实 turn 取得足够的模型 / 推理强度事实，并在事实缺失或冲突时 fail-closed。**

本步骤不执行真实 A/B，不做人工评分，也不形成“B 优于 A”的结论。

## 2. 当前 Codex 事实

### 2.1 `exec --json` 尚未直接暴露 provider model

OpenAI Codex Issue #39406（2026-08-19 创建，当前仍 Open）明确请求：在 `codex exec --ephemeral --json` 的 `turn.completed` JSONL 中暴露 provider 返回的模型 ID。该 Issue 同时明确区分：

- 请求模型；
- 本地配置 / alias / resolved model；
- provider response metadata 中真正返回的模型标识。

因此 C3 不能仅记录 `--model` 或客户端启动 / turn 配置并称为实际服务模型。

来源：

- https://github.com/openai/codex/issues/39406

### 2.2 Codex SSE 层已经能够观察 provider `response.model`

Codex 当前 `codex-api` SSE 解析实现会对收到的 SSE data 执行 trace，并从事件中提取 `response_model()`；当服务端模型变化时还会生成 `ResponseEvent::ServerModel`。

公开复现已经使用：

```text
RUST_LOG=codex_api::sse::responses=trace
```

在 `codex exec` 的 `response.created` / `response.completed` SSE event 中直接观察 `response.model`，并实际发现“请求模型与 provider 返回模型不同”的情况。这证明请求值不能替代 provider 事实，同时也提供了当前可用的取证面。

来源：

- https://github.com/openai/codex/blob/main/codex-rs/codex-api/src/sse/responses.rs
- https://github.com/openai/codex/issues/11971
- https://github.com/openai/codex/issues/10953

### 2.3 reasoning effort 可从 turn span 取得

OpenAI Codex Issue #21990 记录：Codex per-turn structured span 可以包含：

- `thread_id`；
- `model`；
- `codex.turn.reasoning_effort`。

该 Issue 将日志解析明确描述为当前可用 workaround，同时请求未来提供正式结构化 session info API。

来源：

- https://github.com/openai/codex/issues/21990

### 2.4 `codex exec` 默认日志级别不足

Codex 当前安装文档说明：

- Codex 遵循 `RUST_LOG`；
- 显式 `log_dir` 可以开启单次运行的 plaintext log；
- 非交互 `codex exec` 默认 `RUST_LOG=error`。

因此只设置 `log_dir` 不足以把 turn-level / SSE trace 当作必然可观察事实。C3 必须只对当前隔离子进程显式开启最小必要日志：

```text
RUST_LOG=error,codex_core=info,codex_api::sse::responses=trace
```

来源：

- https://github.com/openai/codex/blob/main/docs/install.md

## 3. C3 运行时证据适配

新增：

`evals/run_rule_retrieval_c3.py`

该 runner 不取代 C2 装配器，而是复用 C1/C2 已冻结的设计、索引、A/B 工作区和静态校验。

真实 C3 每个场景必须连续执行 A、B 两侧；不提供可用于正式评分的单侧 `--variant` 入口。

### 3.1 固定请求与工具边界

A/B 使用同一：

- `--model` 请求值；
- `model_reasoning_effort` 请求值；
- `--sandbox read-only`；
- `approval_policy="never"`；
- `web_search="disabled"`；
- 场景任务正文；
- Codex 可执行文件与父进程环境结构。

临时工作目录和 log 目录名称不包含 A / B 分组。

### 3.2 分层记录模型事实

结果区分：

- `requested_model`：请求值；
- `client_turn_model`：主 turn span 的客户端解析模型，只作诊断；
- `model`：SSE `response.model`，作为本次 provider 返回模型标识；
- `requested_reasoning_effort`：请求值；
- `reasoning_effort`：同一主 turn span 的解析值。

provider `response.model` 仍只是服务端返回的标识，不是密码学权重证明；但它满足当前阶段“不用请求 / alias / 本地配置冒充实际服务模型”的证据要求。

### 3.3 fail-closed

每个隔离 run：

- provider model 唯一且 reasoning effort 唯一：`runtime_facts_status=observed`；
- 任一事实出现多个不同值：`ambiguous`；
- provider model 或 reasoning effort 缺失：`unavailable`。

每个 A/B pair：

- 两侧均 `observed` 且 `(provider model, reasoning effort)` 完全相同：`comparable`；
- 任一侧不可观察：`insufficient`；
- 两侧实际事实不同：`mismatch`。

只有 `comparable` 可以进入效果比较。

## 4. 证据最小化

完整 SSE / turn trace 只存在于当前临时子进程的 stderr / isolated `log_dir`。

持久化到本地评估结果中的运行事实文件只保存：

- thread ID；
- trace 来源类别；
- provider model 值集合；
- client turn model 值集合；
- reasoning effort 值集合；
- 解析状态。

不把完整 trace 作为长期仓库输入，也不把当前 Codex 日志格式提升为 Method / Guide / Skill 契约。

## 5. Readiness 与后续门禁

本步骤完成的条件：

1. C3 runner 与结果 schema 可以静态校验；
2. provider / client model 区分、缺失、多值和路由不一致场景具有机器级 parser 回归；
3. 一次只读 GitHub Actions 静态验证实际执行 `py_compile` 与 `--validate-only`；
4. 最终 AI Review 未解决 Blocking / Medium 为 `0 / 0`；
5. 集成后仍停在 C3，不把 Readiness 等同于真实 A/B 完成。

集成后的下一实际步骤仍是：

> 在具备真实 Codex 认证的运行环境中执行冻结 9 个场景的 A/B；仅对 `comparable` pair 进行人工隐藏断言评分和效果比较。

若当前 Codex 版本 / 认证环境无法取得 provider model 或 reasoning effort，应记录 `insufficient` 并停止效果比较，而不是降低 C1 公平性要求。

若未来 Codex 正式在 `exec --json` 或 session API 暴露 provider model / reasoning effort，应优先迁移到正式接口，删除当前 trace 适配层，而不是让 workaround 长期固化。
