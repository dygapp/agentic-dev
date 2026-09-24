---
id: guide:multi-model-collaboration
type: guide
status: active
distribution: source-only
---

# 多模型协作使用指南

多 Agent / 多模型协作是可选能力，不是 `agentic-dev` 的默认运行前提。

它适合把只读探索、主推理、实现、独立复核或高影响 second opinion 做有界分工；如果单 Agent 已经能稳定完成当前责任，不要为了“多模型”本身增加配置和协调复杂度。

真正的 Consumer execution contract 由 installed `activate-model-collaboration` Skill 持有；本文只提供方法导航和平台理解。

## 1. 什么时候值得启用

可能有价值的情况：

- 大量只读搜索 / Evidence 收集占据主模型上下文；
- 实施与独立 review 可以清晰隔离；
- 某些高影响问题只在有未决冲突时需要更高能力 second opinion；
- 希望把高能力模型预算集中到真正需要推理的工作；
- 多个有界责任可以安全并发。

不适合：

- 当前任务很小；
- delegation 成本高于收益；
- Runtime 无法观察真实 child execution；
- 多写入者会争用共享状态；
- 用户只是为了“用上多模型”而没有实际瓶颈。

## 2. 推荐责任模型

```text
Deterministic tools
  ↓
Explorer / context worker
  ↓
Primary reasoning / implementation worker
  ↓
Independent reviewer（按需）
  ↓
High-capability second opinion（只有触发条件成立时）
```

Primary Agent 仍保留：

- Goal；
- Consumer Authority；
- delegation boundary；
- shared-resource ownership；
- completion claim；
- fallback responsibility。

子 Agent 返回的是观察、Evidence 或有界工作结果，不自动成为最终 Authority。

## 3. 先安装 Skill，再建立本地实例

Existing Consumer 不需要采用 Provider 的 Model Collaboration Method / Architecture。

只需要：

1. 当前 Repository 已安装 `activate-model-collaboration`；
2. 当前 Runtime 能力可探测；
3. Consumer 自己决定本地是否启用以及配置放在哪里；
4. 对真实 delegation、observability、single-writer 和 fallback 做验证。

普通运行不能因为本地配置缺口在线读取 Provider Source 临时补齐 runtime semantics。

## 4. Consumer 中应该保存什么

典型 Consumer 可以保存：

```text
AGENTS.md / project docs
→ 是否启用、稳定 locator、权限边界

platform-local config
→ 例如 .codex/config.toml / agent profiles

Consumer-local constraints
→ shared-resource、权限、安全、成本等项目政策

verification evidence
→ 当前 Runtime 实际观察结果
```

不需要建立 `Project Capability Profile`、Model Collaboration Method instance 或 upstream Rule mirror。

## 5. Runtime capability 必须实测

不要只看：

- 配置文件可以 parse；
- 某个 model 名称写得进去；
- 主 Agent 自述“已委派”；
- CLI exit 0。

真正启用前至少确认当前平台实际支持什么：

- child agent / thread；
- model / effort 选择；
- sandbox / permission；
- write concurrency；
- observability；
- child terminal result；
- interruption / timeout / recovery；
- fallback。

requested configuration 与 observed runtime 是两回事。

不可观察时明确标记 unknown，不把配置意图冒充事实。

## 6. Execution Context 与 Runtime Under Test

Fresh Context、独立 review 与目标 Runtime 不是一回事。

例如：

- 只是需要 fresh semantic review → 新隔离上下文即可；
- 需要证明 Codex native subagent / model / permission 行为 → 才启动真实 Codex Runtime Under Test；
- 只是 deterministic repository check → 用当前 Repository Runtime 即可。

不要为了“独立”自动启动额外 provider 或模型。

## 7. Single writer 与共享资源

如果多个 Agent 并发：

- 明确哪个 Agent 可以写；
- 共享 branch / worktree / database / environment 只有一个明确 owner；
- child worker 默认只在分配范围内行动；
- 需要交接 ownership 时显式完成 acquire / handoff / release；
- 不清理其他 worker 仍在使用的资源。

只读并行通常比多写入者并行更安全。

## 8. Independent reviewer

独立 reviewer 应：

- 从 exact subject 重新恢复 Consumer Authority；
- 不继承作者意图和旧 PASS；
- 只读取复核所需最小 Evidence；
- 输出具体 findings 或有界 PASS。

独立性来自 fresh / isolated reasoning boundary，不来自“必须换另一个厂商 / 模型”。

如果 review claim 本身依赖 Runtime-specific behavior，再单独启动对应 Runtime Under Test。

## 9. Fallback 必须真实可用

任何启用策略都需要 single-agent fallback。

例如：

```text
collaboration enabled
→ child delegation fails / times out / becomes unobservable
→ primary recovers bounded evidence
→ disable affected path
→ continue safely in single-agent mode when current responsibility still allows
```

如果失败会让 completion claim 无法验证，则保持 blocker，不冒充成功。

## 10. 成本和效率怎么判断

不要预设“多 Agent 总 token 一定下降”。

应分别观察：

- 高能力模型 token；
- Primary context size；
- total token；
- wall time；
- coordination cost；
- retry / rework；
- residual findings；
- 与 single-agent baseline 的质量差异。

区分两个 claim：

- **functional enablement**：协作链路安全可用并可 fallback；
- **efficiency / preferred default**：只有可比较 baseline 支持时才能声称更省、更快或更适合作为默认策略。

## 11. Codex 参考

Codex 平台具体的 subagent / model / config 能力会变化。

带核验日期的参考见：

- [codex-model-collaboration-reference.md](codex-model-collaboration-reference.md)

它只提供平台参考，不是永久兼容契约。真正启用时仍由 `activate-model-collaboration` 对当前 Runtime 重新探测。

## 12. 最小启用检查表

启用前至少确认：

- installed `activate-model-collaboration` Skill 可发现；
- Consumer Authority 已恢复；
- 当前 Runtime capabilities 已实测；
- strategy 与角色边界已选定；
- single-writer / resource owner 已明确；
- observability 足够支撑 claim；
- independent review path 真实可用（如果采用）；
- fallback 已验证；
- ordinary runtime 不依赖 Provider docs。

这些条件不能成立时，保持 disabled / bounded single-agent mode。
