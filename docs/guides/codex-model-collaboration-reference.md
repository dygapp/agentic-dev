---
id: guide:codex-model-collaboration-reference
type: guide
status: active
---

# Codex 模型协作参考配置

本文件是**人和 AI 可按需读取的、非规范、平台专项参考实现**。真正的 Consumer execution contract 由 installed `activate-model-collaboration` Skill 持有；本文件不拥有新的 Gate、policy 或 Consumer runtime state。

参考核验日期：**2026-09-14**。

本 Reference 基于当日 OpenAI Codex Subagents / configuration 文档与历史 `experiment/codex-multi-model-collaboration` 经验整理。Codex custom-agent 格式、模型目录、reasoning effort、并发与观测能力都可能变化；Consumer 启用协作时必须通过 `activate-model-collaboration` 重新探测当前 Runtime，不能把本文件当作永久兼容配置。

## 1. 当前 Codex 能力形态

当前官方 Codex 支持 local custom subagents，并允许项目级 Agent profile 使用不同的模型配置与 developer instructions。项目级自定义 Agent 位于：

```text
.codex/agents/
```

每个自定义 Agent TOML 至少需要：

- `name`；
- `description`；
- `developer_instructions`。

还可以按当前 runtime 支持情况设置：

- `model`；
- `model_reasoning_effort`；
- `sandbox_mode`；
- 其他当前 Codex 支持的 Agent-specific config。

项目级 `[agents]` 配置可以控制 subagent 是否启用、并发线程、默认 subagent model / reasoning effort 以及 interrupt 行为。字段与合法值必须在 adoption 时按当前官方文档重新确认。

官方文档同时明确：subagent workflow 通常会比可比单 Agent 运行消耗更多总 token；更适合并行 read-heavy、探索、测试与独立 review，write-heavy 并行则需要额外谨慎处理冲突与协调成本。

## 2. 推荐项目结构

Consumer 可以把 Codex local instance 组织为：

```text
.codex/
├── config.toml
└── agents/
    ├── context_explorer.toml
    ├── implementation_worker.toml
    ├── quality_reviewer.toml
    └── critical_reviewer.toml
```

这些文件只是 Consumer-local implementation assets。是否需要四个角色、文件名如何命名、具体模型、effort 与并发数都由 Consumer 当前策略决定。

如果 Consumer 只需要 read-only exploration，可以只建立 `context_explorer`；如果不需要独立 critical review，不应为了模板完整创建空闲角色。

## 3. `.codex/config.toml` 参考骨架

```toml
[agents]
enabled = true

# 按当前 runtime 能力与 Consumer policy 设置，不从 upstream 模板机械复制：
# max_concurrent_threads_per_session = <consumer-selected-value>
# default_subagent_model = "<consumer-selected-model>"
# default_subagent_reasoning_effort = "<supported-effort>"
# interrupt_message = true
```

如果 Consumer 决定禁用 child collaboration，fallback 形态应可明确恢复，例如：

```toml
[agents]
enabled = false
```

实际 fallback 还必须考虑 Consumer 是否通过命令行覆盖、用户级配置或其他 runtime layer 改写项目配置；不能只凭文件内容推断最终 effective config。

## 4. Context Explorer

用途：只读搜索、Authority / code / Rule candidate / Evidence 定位、上下文整理，不做方案定稿或写入。

```toml
name = "context_explorer"
description = "只读探索与上下文准备，用于有界定位 Authority、代码、依赖、Consumer-local constraints 和验证入口。"

# 由 Consumer 将 low-cost capability 映射到当前真实可用模型：
# model = "<consumer-selected-low-cost-model>"
# model_reasoning_effort = "<supported-effort>"

sandbox_mode = "read-only"

developer_instructions = """
只处理 Primary Agent 明确分配的有界只读任务。
优先返回 canonical locator、当前观察事实、Evidence locator 与 unknown，不把自己的摘要提升为 Authority。
项目级约束必须从当前 Consumer 声明的 local-constraint 入口按需恢复，不枚举全量 policy corpus，也不在线读取 upstream Rule tree 代替本地入口。
不要修改文件，不执行外部写操作，不继续递归委派。
"""
```

## 5. Implementation Worker

用途：在目标、Authority、允许修改面和验证责任已经明确后，承担**唯一有界 writer**。

```toml
name = "implementation_worker"
description = "单一有界写入角色，在明确 Authority、scope 和 verification responsibility 后实施当前工作项。"

# model = "<consumer-selected-capable-model>"
# model_reasoning_effort = "<supported-effort>"

sandbox_mode = "workspace-write"

developer_instructions = """
只实施 Primary Agent 明确分配的一个有界工作项。
同一共享写入面保持 single-writer；不要与其他 writer 并行编辑共享路径。
发现产品意图、Architecture、Authority 或权限缺口时返回 Primary Agent，不静默扩张范围。
完成后执行与当前责任匹配的验证并报告事实、Evidence、unknown 和未执行检查。
不要自行 merge、release、deploy 或执行破坏性外部操作。
不要继续递归委派。
"""
```

如果 Consumer runtime 不能可靠隔离 workspace writer 或当前工作存在共享外部资源竞争，应保持该角色 disabled，而不是降低 single-writer 约束。

## 6. Quality Reviewer

用途：从实施者结论隔离出来，对最终 candidate、Authority、Evidence 与回归风险做独立复核。

```toml
name = "quality_reviewer"
description = "只读独立复核最终 candidate 的正确性、回归、验证证据和范围控制。"

# model = "<consumer-selected-capable-review-model>"
# model_reasoning_effort = "<supported-effort>"

sandbox_mode = "read-only"

developer_instructions = """
基于当前 canonical Authority、最终 candidate 和当前 Evidence 独立复核。
不要把实施者的 completion claim 当作事实前提。
优先报告 Blocking / Medium actionable findings，并区分事实、条件性风险和 unknown。
不要修改文件，不执行外部写操作，不继续递归委派。
"""
```

独立 review 是否是当前任务的必要 Gate，仍由 Repository Rule / Method / Authority 决定；本 profile 不把 reviewer 的存在变成所有任务的新强制步骤。

## 7. Critical Reviewer

用途：只在高返工成本、重大 Architecture、安全 / 隐私、不可逆数据操作、冲突 Evidence 或 deliberate second opinion 等条件成立时执行补充 challenge。

```toml
name = "critical_reviewer"
description = "高影响补充复核角色，只在明确 escalation 条件成立时进行独立 challenge。"

# model = "<consumer-selected-high-capability-model>"
# model_reasoning_effort = "<supported-effort>"

sandbox_mode = "read-only"

developer_instructions = """
仅在 Primary Agent 明确给出 escalation reason 时执行。
重新读取 canonical Authority、candidate 与 Evidence，不因模型等级提高结论权威。
检查关键假设、失败模式、回退能力、跨层一致性和未解决风险。
不要修改文件，不执行外部写操作，不继续递归委派。
"""
```

Consumer 不应为了“高影响任务”机械调用最高等级模型；先使用最低足够能力，只有当前 Evidence 支持升级时才执行 high-capability second opinion。

## 8. Primary Agent 的最小运行责任

Primary Agent 可以由当前用户会话 / Codex 主线程承担，不要求额外创建一个 `primary_agent.toml`。

它至少负责：

1. 恢复当前 Repository Authority 与 Method responsibility；
2. 通过 deterministic tooling 完成可以确定性完成的发现；
3. 决定是否需要 child Agent，以及每个 child 的有界目标；
4. 保留 Goal / Scope / Authority / external-operation authorization；
5. 收到 child 输出后重新读取关键 canonical source、最终 diff / state 与验证 Evidence；
6. 只根据当前可验证事实形成 completion claim；
7. 在 child runtime 失败时执行 single-agent fallback，而不是假装 delegation 成功。

## 9. 运行时探测与冒烟验证

采用时至少执行与当前平台匹配的检查，并记录**实际命令与 effective config evidence**。不要把这里的示例命令视为永久接口。

Smoke 必须证明：

- 项目级配置确实被加载；
- 至少一个 read-only child task 被真实创建；
- 能观察 child thread / child run / child terminal result；
- child 返回结果与 Primary 观察的 runtime event 一致；
- requested model / effort 与 observed runtime identity 分开记录；
- 如果实际模型身份不可观察，明确记录 `not observable`；
- child failure 能触发 fallback，Primary 不会仅凭最终文本把失败记录成成功。

历史实验已经证明：配置解析通过、主进程 exit code `0` 和主 Agent 自述“委派成功”三者都不能替代真实 child evidence。

## 10. 写入与复核定向验证

如果启用 `implementation_worker`：

- 验证同一共享写入面只存在一个 writer；
- 验证其他 explorer / reviewer 保持 read-only；
- 验证 writer 不自行获得 merge / release / deploy 权限；
- 验证 Primary 能在 child 完成后重新读取最终状态。

如果启用 `quality_reviewer` / `critical_reviewer`：

- reviewer input 不应把实施者完成结论作为既定事实；
- reviewer 应读取 canonical Authority 与 candidate；
- 复核通过不自动产生 Integration Authority。

## 11. 功能启用与效率验证

第一次 smoke 的目标是 **functional enablement**：证明 collaboration chain 可以安全运行。

不要仅凭 smoke 声称：

- token 更少；
- wall time 更短；
- 高能力模型一定减少；
- review 质量一定更高；
- 应成为默认策略。

如果 Consumer 要形成 efficiency / preferred-default claim，应另外进行可比单 Agent baseline，对同一目标至少观察：

- high-capability model token / context；
- Primary Agent context；
- total token；
- wall time；
- rework / correction rounds；
- completion quality / residual findings。

只有质量不低于 baseline 且至少一个实际优化目标获得当前 Evidence 支持，才适合把 collaboration 从“可用选项”提升为“推荐 / 默认策略”。

## 12. 维护规则

出现以下变化时，Consumer 应重新执行运行时探测或相关冒烟验证，而不是沿用历史通过结果：

- Codex CLI / Agent runtime 大版本变化；
- custom-agent TOML schema 变化；
- 模型发布、退役或 reasoning effort 支持变化；
- sandbox / permission / subagent threading 行为变化；
- Consumer 修改协作角色、并发、writer ownership 或 fallback；
- 以前不可观察的 actual runtime model / usage 变为可观察，或反之。

本 Reference 的价值是提供一个安全的起点和检查结构，而不是把 2026-09-14 的 Codex 配置永久冻结为 `agentic-dev` Authority。
