---
id: architecture:rule-discovery
type: architecture
status: active
---

# 规则发现架构

## 1. 目标

Rule Discovery 只解决一个问题：在不把全量规则 metadata 或正文发送给模型的前提下，从当前任务可观察事实中筛出少量值得读取的 Rule locator。

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

Rule 的规范定义、Skill / Rule 边界、granularity 与 Consumer-local specialization 由 `docs/architecture/rule-architecture.md` 持有。本文件只拥有发现机制、渐进披露与 fail-closed contract。

规则 metadata 与规范正文必须同源、同文件维护。不得维护需要与 Rule 同步的 Reviewed Discovery Map、Activation Manifest、Runtime Catalog、rule-index 或其他中心路由表。

## 2. 发现资源边界

### 可发现 Rule

configured Rule root 下除保留导航文件外的 Markdown 都必须是合法 discoverable Rule。Rule 必须 `type: rule`、`status: active`，并满足本 Architecture 的 Front Matter contract；坏文件不能被静默跳过。

### 保留的人类 README

文件名**恰为 `README.md`** 的 Markdown 是 Rule root 内唯一允许退出 Rule scan 的 Human Navigation 资源：

- 不作为 Rule；
- 不进入 Rule Discovery candidate corpus；
- 不提供 Rule routing / activation metadata；
- 仍参加 repository Markdown lint，必须拥有合法 common Front Matter、唯一资源 id 与非空正文。

这个保留例外只服务 Human View，不提供通用 `discoverable: false` 逃逸机制。其他文件名的 `.md` 若位于 configured Rule root，仍必须按 Rule contract fail closed。

### Rule root 扫描完整性

configured Rule root 内的目录 symlink 属于当前不支持的布局。Scanner 可以选择不跟随 symlink，但一旦发现目录 symlink，必须明确 `fail-closed` 并报告该路径；不得把被跳过的子树当作“没有 Rule”，更不得返回 `status=ok` 的不完整 candidate corpus。

这个约束只用于保证当前 Rule corpus 扫描完整性，不建立额外 path registry，也不要求 Tool 把物理目录结构暴露给 ordinary Agent runtime。

## 3. Rule Front Matter

```yaml
---
id: rule:example-policy
type: rule
status: active
scope:
  phases: [example-phase]
  activities: [implementation]
  technologies: []
  artifacts: [code]
  risks: []
---
```

`scope` 只允许 `phases`、`activities`、`technologies`、`artifacts`、`risks` 五个维度。Rule metadata 中每个值都是 lowercase kebab-case string array；空数组表示该 Rule 在该维度不限制。

Front Matter 只回答“当前任务是否值得加载这个 Rule”。required checks、正文摘要、decision logic、exception list、推荐方案和 completion condition 正文必须留在 Markdown body。

任务级 Rule 可以在正文中持有同一责任下的多个相关 policy；metadata 不需要为每个内部 policy 建第二份条件表。Rule 文件粒度由 `rule-architecture.md` 负责。

示例中的 `example-phase` 只说明字段形状，不是全局 phase token。真实 `phases` value 必须来自当前 Method canonical owner 定义的稳定 phase identity。

## 4. 任务信号

调用方从当前 task responsibility 和当前仓库事实形成同构五维 signals。五个字段必须全部出现，但 task-side value 是三态：

```json
{
  "phases": ["example-phase"],
  "activities": ["implementation"],
  "technologies": [],
  "artifacts": ["code"],
  "risks": null
}
```

- 非空数组：当前事实已经能够安全规范化出的已知 token；
- `[]`：当前事实明确没有该维度的正向 signal；
- `null`：存在未知、缺失或无法安全规范化的事实，该维度不得用于排除候选。

`null` 与 `[]` 不可互换。把未知误写为 `[]` 会产生 false negative；把已知为空误写为 `null` 会无必要扩大候选。

每个非空 task-signal 数组最多 6 个 token。禁止通过大量同义词、近义阶段名、推测风险或候选 Rule 术语做碰撞式检索；超过上限必须 fail closed。

### 4.1 阶段身份

Rule Discovery Architecture **不拥有任何具体 Method 的 phase token 列表**。

如果当前 selected Method 定义了稳定 phase identity，调用方可以把当前 Method stage 映射到对应 token；如果没有定义，或者无法在不猜测的情况下确定当前 phase，则 `phases` 使用 `null`。

不同 Method 不自动共享 phase token。新增 Method-specific Rule 前，应先由该 Method canonical owner 定义稳定 phase identity；Rule Discovery 不从自然语言阶段名、目录名、旧 Method 或未命中 Rule metadata 反向发明 token。

### 4.2 其他维度规范化

`activities` 优先使用直接责任类别，例如 `implementation`、`verification`、`review`、`external-operation`、`design`。不得把同一责任扩写成多个近义活动。

`technologies`、`artifacts`、`risks` 只使用当前任务或 Repository 事实可以直接支持的稳定机器身份。具体语言 / 框架 token 由目标 Repository 的 code、dependency、configuration 与 local Rule corpus 决定；本 Architecture 不维护跨项目技术词表。跨项目较稳定的工件 / 平台身份可包括普通源代码 → `code`、数据库 schema migration → `database-migration`、GitHub Actions → `github-actions`、workflow run → `workflow-run`。

这些规范化约定只定义 task facts 如何变成机器 token，不记录任何 Rule→token 对应关系，也不替代每个 Rule 自己的 Front Matter。

如果某个维度存在相关事实，但无法在不猜测的情况下得到 canonical token，使用 `null`。不得读取未命中 Rule 的 Front Matter、文件名集合或正文来反向学习 token。

目录路径不构成 task signal，也不参与匹配。

## 5. 确定性匹配

对每个 discoverable Rule：

- Rule 某维度为空：该维度不限制；
- Task 某维度为 `null`：该维度未知，不用于排除该 Rule；
- Task 某维度为 `[]`：若 Rule 在该维度有限制，则排除；
- Rule 与 Task 在某个双方均有 token 的受限维度无交集：排除；
- 其余受限维度均通过：进入候选。

不使用 score、priority、embedding、模型置信度或目录分类做隐式路由。候选按 `id` 稳定排序。

`null` 的目的不是扩大普通上下文，而是防止 Agent 为了命中精确 metadata 而猜测 taxonomy；候选扩大后仍必须由正文语义确认收窄。

## 6. 输出与渐进式披露

成功输出只包含：

```json
{
  "status": "ok",
  "scanned": 100,
  "candidate_count": 2,
  "candidates": [
    {"id": "rule:implementation-discipline", "path": "docs/rules/generation/implementation-discipline.md"}
  ]
}
```

不得返回未命中 Rule、全量 metadata、正文摘要、score 或推荐方案。LLM 只读取候选路径的正文。

Rule Discovery 返回的 `candidates[]` 是 ordinary runtime 的唯一 Rule locator 来源。Agent 不得在 discovery 前后通过 `rg --files`、`find`、目录树、Human README、IDE 索引、脚本扫描或其他文件枚举，把未命中 Rule 的 locator / 文件名集合送入模型上下文。

工具内部可以扫描全部 Rule Front Matter；Human README 也可以为人展示 inventory，但这些信息不得作为 ordinary Agent runtime 的替代候选输入。

如果 `status=ok` 但候选为空，调用方不得读取或枚举未命中 Rule locator / metadata 来反向校准 signals。只有当前任务 / 仓库事实发生变化时才重新构造 signals；否则保留“当前没有已发现 Rule”或上游事实缺口。

渐进式披露的成本目标是：

```text
Tool side: O(N metadata scan/filter)
LLM side: O(k locators + k Rule bodies), k << N
```

这里 `k` 不应因为把一个任务所需的一组 policy 机械拆成多个 micro-rules 而无意义膨胀。只要仍能保持可靠适用性判断，任务级 Rule 聚合可以同时减少 locator 数、文件读取次数和 LLM 语义确认开销；具体 granularity 决策仍由 `rule-architecture.md` 定义。

## 7. 失败关闭

YAML 无法解析、schema 不完整、未知 Rule 顶层字段、scope 类型错误、非法 token、重复 Rule id、discoverable Rule 非 active、task signals 非法、单维 task tokens 超过上限、扫描不完整或重复扫描同一 Rule 时，Discovery 必须返回 `fail-closed`，不得跳过坏 Rule 后继续给出候选。

reserved `README.md` 不属于 discoverable Rule，但其 common resource metadata / body lint 失败仍会使 repository lint 失败。

## 8. 可删除缓存

实现可以使用缓存，但缓存必须由当前 Rule Front Matter 确定性重建：

- 不人工维护；
- 不拥有规范语义；
- 不作为普通 LLM prompt context；
- 删除后不影响从真实 Rule 文件恢复。

## 9. 使用方边界

Consumer ordinary runtime 使用 Consumer-local current Rules 与本地 Rule Discovery Tool。上游 `agentic-dev` 只作为显式 adoption / upgrade 来源；普通任务发现失败不能自动在线回到 upstream 补规则。

Consumer adoption 必须携带当前 task-signal 三态、bounded-token contract、locator-only progressive-disclosure contract 与 reserved Human README / lint 边界；否则同一组 Rule 在 Consumer 中可能出现系统性 false negative、metadata 反向探测或 human catalog 被误当 runtime index。

具体 Consumer 的 Rule root、Tool locator、Method phase identities 与其他 implementation pointers 属于该 Consumer 的 local Project / Repository capability instance，不属于本 Architecture。

## 10. 普通运行时集成

普通 Agent 运行时按当前 responsibility 重复执行以下闭环：

```text
current task / repository facts
→ bounded current task signals
→ discover
→ locator-only candidates
→ read candidate bodies
→ semantic applicability confirmation
→ continue current responsibility
```

### 10.1 责任转换检查点

Rule Discovery 不是一次会话级初始化动作，而是 direct responsibility 级运行时 checkpoint：

- 当前 direct responsibility 建立后，在执行该责任的首个有副作用动作前必须完成一次 task-level discovery；
- direct responsibility 发生切换，或 phase / activity / technology / artifact / risk 等关键事实实质变化时，旧 candidate set 不再作为新责任的充分依据，必须在下一次有副作用动作前重新构造 signals 并执行 discovery；
- 为恢复事实而进行的只读读取可以先于 discovery，但不得借只读阶段形成的旧 candidate set 跨责任继续写入、合并、发布、部署或执行其他有副作用操作；
- CI 中的 Rule Discovery lint、deterministic test 或固定 smoke scenario 只验证工具与 corpus，不携带当前 Agent 的实时 task signals，因此不能证明当前责任已经完成 task-level discovery，也不能替代 ordinary runtime invocation。

该 checkpoint 只规定“何时必须重新发现”；task signals、matching、locator-only 输出与最终语义适用性仍由本 Architecture 其他章节统一定义，不建立第二套路由语义。

运行边界：

1. task signals 必须来自当前可观察事实，不包含目标 Rule 名、期望答案或历史候选集；
2. unknown 使用 `null`，不得通过 synonym cloud 或未命中 Rule metadata 反向校准；
3. Rule Discovery 返回值是 ordinary runtime 获得 Rule locator 的唯一入口；不得枚举未命中 Rule 路径或完整 Rule tree；
4. tool candidate 只是“值得读取”，不是“已经适用”；LLM 必须读取正文后确认该 Rule 对当前工作真实成立；
5. 当前 direct responsibility 或 phase / activity / technology / artifact / risk facts 发生足以改变候选集合的变化时，在继续该责任的有副作用动作前重新执行 discovery；旧 candidate set 不跨职责永久有效；
6. Skill discovery 与 Rule discovery 分离：Agent Skills 负责选择独立执行能力，Rule Discovery 负责当前责任的条件性约束；Rule 不要求依附 Skill；
7. `fail-closed` 时不得把无候选、旧候选或全量 Rules 当替代结果；先修复 signals、metadata 或扫描完整性，再继续依赖 Rule Discovery；
8. ordinary runtime 的模型上下文只接收 Discovery 返回的 candidate locator 与最终读取的候选正文，不接收全量 locator、全量 metadata、Human README inventory、未命中 Rules 或工具内部扫描状态。

### 10.2 进程外执行契约

canonical Rule Discovery Tool 不要求与当前 Agent 位于同一 execution environment。Repository-local capability instance 可以同时声明 direct execution transport 与 out-of-process compute transport；transport 只负责执行同一个 Tool，不取得 Method、Rule、Authority 或后续动作授权。

当前 Agent 缺少 worktree、shell、Python 或其他直接执行能力，不能成为跳过 task-level discovery、复用旧 candidate set 或改由 Human Guide / memory 推断规则的理由。使用 out-of-process transport 时必须：

1. 绑定一个明确、可复核的 Repository baseline；
2. 取得并验证实际执行 baseline 与请求 baseline 一致；
3. 执行该实际 baseline 自己声明的 canonical Tool，而不是 transport 环境中的替代实现；
4. 保持本 Architecture 的 task-signal、fail-closed 与 locator-only result contract；
5. 产生可审计的 invocation、signals、requested / actual baseline、result 与执行终态 Evidence，使当前 Agent 能恢复结果并确认其对应 subject。

transport 启动或请求被接受不等于 discovery 成功。只有目标 subject 的执行到达可观察终态、baseline 一致且 result 满足本 Architecture，才形成可消费的 discovery Evidence。

当前 Agent 应按 Repository-local capability instance 使用适用的已声明自动化 transport。所有 declared transports 都不可用、无法验证 baseline 或无法恢复结果时，Rule Discovery 必须 fail closed；不得把人工本地执行当作未检查其他声明路径时的默认 fallback。

Repository-local capability profile / bootstrap 发布当前 Rule root 与 Tool locator；具体实现路径可以变化，但不得改变上述运行语义而不先修改本 Architecture。
