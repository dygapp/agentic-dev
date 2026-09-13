---
id: architecture:rule-discovery
type: architecture
status: active
---

# 规则发现架构

## 1. 目标

V4 的规则发现只解决一个问题：在不把全量规则 metadata 或正文发送给模型的前提下，从当前任务可观察事实中筛出少量值得读取的 Rule locator。

```text
当前任务 / 仓库事实
→ 提取少量 task signals
→ Rule Discovery Tool
→ 只扫描 Rule 自身 YAML Front Matter
→ 确定性候选初筛
→ 返回少量 {id, path}
→ LLM 读取候选正文
→ LLM 做最终语义适用性确认
```

规则 metadata 与规范正文必须同源、同文件维护。不得维护需要与 Rule 同步的 Reviewed Discovery Map、Activation Manifest、Runtime Catalog、rule-index 或其他中心路由表。

## 2. 资源边界

### Skill

Skill 拥有稳定独立执行闭环：Trigger / Purpose、Inputs、Procedure、Outputs、Exit Conditions、Escalation。Skill 的选择继续使用 Agent Skills 原生发现机制，不进入 Rule Discovery Tool。

### Rule

Rule 是执行工作时必须遵守的条件、约束、默认值、不变量或完成声明要求，但本身不是完整任务流程。一个独立发现单元对应一个最小 Rule Markdown 文件。

### Guide

Guide 只承担面向人的初始化、采用、升级、低频说明和导航。普通 Agent runtime 的生成、验证、外部操作、仓库治理约束不得以 Guide 作为规范 owner。

## 3. Rule Front Matter

```yaml
---
id: rule:implementation-minimality
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: []
  artifacts: [code]
  risks: []
---
```

`scope` 只允许 `phases`、`activities`、`technologies`、`artifacts`、`risks` 五个维度。Rule metadata 中每个值都是 lowercase kebab-case string array；空数组表示该 Rule 在该维度不限制。

Front Matter 只回答“当前任务是否值得加载这个 Rule”。required checks、正文摘要、decision logic、exception list、推荐方案和 completion condition 正文必须留在 Markdown body。

## 4. Task Signals

调用方从当前任务和当前仓库事实形成同构的五个维度。五个字段必须全部出现，但 task-side value 是三态：

```json
{
  "phases": ["execute"],
  "activities": ["implementation"],
  "technologies": ["vue3", "typescript"],
  "artifacts": ["code", "vue-sfc"],
  "risks": null
}
```

- 非空数组：当前事实已经能够安全规范化出的已知 token；
- `[]`：当前事实明确没有该维度的正向 signal；
- `null`：存在未知、缺失或无法安全规范化的事实，该维度不得用于排除候选。

`null` 与 `[]` 不可互换。把未知误写为 `[]` 会产生 false negative；把已知为空误写为 `null` 会无必要扩大候选。

每个非空 task-signal 数组最多 6 个 token。禁止通过大量同义词、近义阶段名、推测风险或候选 Rule 术语做碰撞式检索；超过上限必须 fail closed。

### 4.1 稳定规范化

`phases` 使用 Method 的稳定阶段身份：

- `clarify-intent`
- `specification`
- `technical-planning`
- `slice-ready`
- `execute`
- `converge`

`activities` 优先使用直接责任类别，例如 `implementation`、`verification`、`review`、`external-operation`、`design`。不得把同一责任扩写成多个近义活动。

`technologies`、`artifacts`、`risks` 只使用当前任务或仓库事实可以直接支持的稳定机器身份。常见规范化例子包括：Vue 3.x → `vue3`、TypeScript → `typescript`、`.vue` SFC → `vue-sfc`、普通源代码 → `code`、数据库 schema migration → `database-migration`、GitHub Actions → `github-actions`、workflow run → `workflow-run`。

这些规范化约定只定义 task facts 如何变成机器 token，不记录任何 Rule→token 对应关系，也不替代每个 Rule 自己的 Front Matter。

如果某个维度存在相关事实，但无法在不猜测的情况下得到 canonical token，使用 `null`。不得读取未命中 Rule 的 Front Matter、文件名集合或正文来反向学习 token。

目录路径不构成 task signal，也不参与匹配。

## 5. 确定性匹配

对每个 `type: rule`、`status: active` 的 Rule：

- Rule 某维度为空：该维度不限制；
- Task 某维度为 `null`：该维度未知，不用于排除该 Rule；
- Task 某维度为 `[]`：若 Rule 在该维度有限制，则排除；
- Rule 与 Task 在某个双方均有 token 的受限维度无交集：排除；
- 其余受限维度均通过：进入候选。

不使用 score、priority、embedding、模型置信度或目录分类做隐式路由。候选按 `id` 稳定排序。

`null` 的目的不是扩大普通上下文，而是防止 Agent 为了命中精确 metadata 而猜测 taxonomy；候选扩大后仍必须由正文语义确认收窄。V4-07 必须继续验证这种保守未知语义不会破坏 `k << N` 的规模目标。

## 6. 输出与渐进式披露

成功输出只包含：

```json
{
  "status": "ok",
  "scanned": 100,
  "candidate_count": 2,
  "candidates": [
    {"id": "rule:implementation-minimality", "path": "docs/rules/generation/implementation-minimality.md"}
  ]
}
```

不得返回未命中 Rule、全量 metadata、正文摘要、score 或推荐方案。LLM 只读取候选路径的正文。

因此允许 Tool CPU / I/O 随 N 增长，但 ordinary runtime 的 LLM discovery context 只能随候选数 k 增长。

如果 `status=ok` 但候选为空，调用方不得读取未命中 Rule metadata 反向校准 signals。只有当前任务 / 仓库事实发生变化时才重新构造 signals；否则保留“当前没有已发现 Rule”或上游事实缺口。

## 7. Fail-closed

YAML 无法解析、schema 不完整、未知 Rule 顶层字段、scope 类型错误、非法 token、重复 Rule id、discoverable Rule 非 active、task signals 非法、单维 task tokens 超过上限、扫描不完整或重复扫描同一 Rule 时，Discovery 必须返回 `fail-closed`，不得跳过坏文件后继续给出候选。

## 8. 可删除缓存

实现可以使用缓存，但缓存必须由当前 Rule Front Matter 确定性重建：

- 不人工维护；
- 不拥有规范语义；
- 不作为普通 LLM prompt context；
- 删除后不影响从真实 Rule 文件恢复。

## 9. Consumer 边界

Consumer ordinary runtime 使用 Consumer-local current Rules 与本地 Rule Discovery Tool。上游 `agentic-dev` 只作为显式 adoption / upgrade 来源；普通任务发现失败不能自动在线回到 upstream 补规则。

Consumer adoption 必须携带当前 task-signal 三态与 bounded-token contract；否则同一组 Rule 在 Consumer 中可能出现系统性 false negative 或 metadata 反向探测。

## 10. Ordinary Runtime Integration

普通 Agent 运行时按当前责任重复执行以下最小闭环：

```text
current task / repository facts
→ bounded current task signals
→ discover
→ locator-only candidates
→ read candidate bodies
→ semantic applicability confirmation
→ current Skill / responsibility
```

运行边界：

1. task signals 必须来自当前可观察事实，不包含目标 Rule 名、期望答案或历史候选集；
2. unknown 使用 `null`，不得通过 synonym cloud 或未命中 Rule metadata 反向校准；
3. tool candidate 只是“值得读取”，不是“已经适用”；LLM 必须读取正文后确认该 Rule 对当前工作真实成立；
4. 当前 phase、activity、technology、artifact 或 risk facts 发生足以改变候选集合的变化时，重新执行 discovery；旧 candidate set 不跨职责永久有效；
5. Skill discovery 与 Rule discovery 分离：Agent Skills 负责选择独立执行能力，Rule Discovery 负责给该职责补充条件约束；
6. `fail-closed` 时不得把无候选、旧候选或全量 Rules 当替代结果；先修复 signals、metadata 或扫描完整性，再继续依赖 Rule Discovery；
7. ordinary runtime 的模型上下文只接收 locator 与最终读取的候选正文，不接收全量 metadata、未命中 Rules 或工具内部扫描状态。

稳定 CLI 入口与最小规范化约定由根 `AGENTS.md` 声明；具体实现可以重构，但不得改变上述运行语义而不先修改本 Architecture。