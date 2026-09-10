# Consumer-local Runtime Routing 接口 v2

## 状态

**Phase D 结果 — Discovery → Routing → Skill Interface**

上层输入：

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`
- `docs/project/rule-ownership-decomposition-audit-v2.md`
- `docs/project/consumer-local-activation-metadata-contract-v2.md`
- `docs/architecture/skill-contracts.md`
- `docs/architecture/engineering-capability-architecture.md` §9～§11

本文冻结 v2 的**逻辑 Runtime Routing Contract**。它不创建新的 Method Stage、Stage Router Skill、Rule Super Skill 或固定运行时 Controller，也不规定必须使用 JSON、Python、MCP、Plugin 或某一种 Agent 产品。

## 1. 目标

一个普通 Consumer Fresh Context 应能只依赖 Consumer-local 资产完成：

```text
Task
→ Current Consumer Authority
→ Candidate Discovery
→ Primary Responsibility + Supporting Constraints
→ Routing-only Stop 或按需 Skill Load
→ Execute / Verify
→ 必要时 Stage Return 并重新解析
```

关键目标不是“尽可能多命中规则”，而是：

> 在不遗漏当前必需 Authority / Rule / Skill 的前提下，得到一个明确 primary responsibility、最小 supporting set 和可解释的 Stage Action。

## 2. Runtime 输入

Phase D 不要求固定对象格式，但每次 routing 至少只能使用当前可观察事实。

### 2.1 必需输入

- 当前 Consumer Repository Authority / Bootstrap；
- 当前用户目标或当前工作目标；
- 当前 Consumer-local Discovery Entry；
- 当前任务可观察状态，例如当前阶段、当前 Work、当前 Evidence、Observed Problem；
- 当前本地可读取的 Activation Manifest / Catalog 或等价发现元数据。

### 2.2 条件输入

只有当前任务实际需要时才读取：

- Requirement / Specification；
- Technical Plan；
- Domain / Architecture / ADR；
- Verification / Integration Policy；
- Current Execution Unit / Readiness Evidence；
- Code / Tests / Runtime Evidence；
- adopted reusable Rule Module / Engineering Discipline；
- platform-specific Skill。

### 2.3 不允许作为 ordinary runtime 事实输入

- 未被 Consumer 固化的历史聊天；
- 个人记忆；
- 其他项目规则；
- upstream `agentic-dev` 当前最新状态；
- rejected / superseded discovery record；
- stale metadata 的摘要或旧 pointer。

## 3. Task Signals

Runtime 先提取**事实信号**，再做 responsibility 解析；不根据关键词直接决定 Skill。

最小信号族：

### 3.1 Goal signal

当前实际要求解决什么：澄清、规格、规划、切分、就绪、执行、缺陷调查、收敛、验证平台问题、外部操作等。

### 3.2 Authority signal

当前任务依赖的 Consumer-native Authority 是否存在、current、可解析且互不冲突。

### 3.3 Lifecycle signal

当前工作已经位于哪个职责 / 阶段，是否存在仍有效的 Readiness / Execute Authority，以及新的证据是否改变了它的基础。

### 3.4 Problem signal

出现的是：

- expected behavior 已定义下的 unexpected implementation/runtime failure；
- 还是 Product Intent / Specification / Architecture / Authorization 本身不完整、冲突或失效。

前者才可能进入 `systematic-debug`；后者应返回拥有该 Authority 的职责。

### 3.5 Condition / risk signal

只记录当前已由事实满足、且会改变规则集合的条件，例如：

- baseline upgrade；
- visual fidelity；
- database migration；
- shared external resource；
- external side effect；
- major architecture；
- irreversible / security / privacy / authority conflict。

未知条件不能为了提高命中率而猜测。

## 4. Candidate Discovery

Discovery 根据当前事实信号从 Consumer-local Manifest / Catalog 取得候选 record。

### 4.1 Candidate 集合包含

按需包含：

- Consumer-native Authority locator；
- routing rule；
- conditional constraint module；
- current responsibility owner；
- execution Skill / platform Skill locator。

### 4.2 Candidate 集合不等于激活集合

Catalog 命中只表示“值得继续判断”，不能直接等价为：

- 该规则已经适用；
- 该 Skill 必须加载；
- 该 Authority 可以被 reusable default 覆盖；
- 当前阶段可以继续执行。

Candidate 仍需经过 Source Currentness、Applicability 与 Consumer Authority 检查。

### 4.3 不使用固定 Top-K

最小集合不是固定条数。所有当前必需 record 都必须保留；无关 record 必须排除。

## 5. Primary Responsibility 解析

一次 routing decision 只允许有一个**当前 primary responsibility**。

### 5.1 解析原则

按以下语义判断，不使用全局数值 priority：

1. **Consumer Authority first**：Consumer-specific current Authority 决定项目事实和约束；
2. **Authority gap owns the return**：如果当前工作暴露上游 Product / Specification / Architecture / Authorization 基础缺口，拥有该缺口的职责成为新的 primary responsibility；
3. **Current requested responsibility**：如果前置基础仍有效，当前明确要求执行的稳定职责成为 primary；
4. **Unexpected failure is not automatically debugging**：只有 expected behavior 已明确且问题属于实现 / runtime 非预期失败时，`systematic-debug` 才成为 primary；
5. **Supporting signal 不夺取 primary**：验证、平台、外部操作、工程纪律等只要不改变当前职责所有权，就保持 supporting role。

### 5.2 典型 Stage Return

```text
Execute 发现 Product Intent 不明确
→ clarify-intent / specify

Execute / Readiness 发现跨 Unit Durable HOW 或 Architecture basis 失效
→ technical-plan

Readiness 发现 Unit shape / acceptance ownership 不完整
→ slice-work

Systematic Debug 发现 expected behavior 未定义 / 冲突
→ clarify-intent / specify

Converge 发现长期 Architecture / ADR 缺口
→ technical-plan
```

这些关系来自现有 Method / Skill Contract；Phase D 只定义 Runtime 如何重新发现 owner，不建立第二份 Method 语义。

## 6. Supporting Context

Supporting Context 是**当前 primary responsibility 正确完成所需、但不拥有当前职责转换**的最小约束集合。

可能包括：

- Consumer Architecture / Domain Authority；
- Verification policy；
- applicable Engineering Discipline；
- external-operation constraint；
- platform-specific capability；
- current Work / Evidence；
- reusable default 被 Consumer-specific rule 覆盖后的背景关系。

### 6.1 Supporting set 的准入

一个 record 只有满足以下条件才进入 supporting set：

- trigger / condition 已由当前事实满足；
- 它会改变当前职责的正确执行或完成声明；
- 它没有被更具体 Consumer Authority supersede / override；
- source currentness 可验证。

“可能有用”不构成准入理由。

## 7. Routing-only 与 Skill Execution

### 7.1 Routing-only

如果当前目标只是：

- 判断下一职责；
- 判断 Stage Return；
- 判断当前 Execute / Readiness 是否仍有效；
- 解释为什么需要某职责；

并且 metadata / routing module + Current Authority 已足够，则：

```text
resolve primary responsibility
→ 返回 responsibility + reason + required source pointers
→ stop
```

不得仅因为发现了 Skill locator 就加载完整 Skill。

### 7.2 真正执行职责

如果当前任务明确要求继续执行 primary responsibility，则：

1. 验证对应 Skill 已在 Consumer-local capability set 中 current / available；
2. 加载**当前 primary responsibility 的完整 Skill**；
3. 只加载当前 Skill 需要的 Consumer Authority 与 supporting constraints；
4. 按 Skill Contract 执行；
5. 遇到 Stage Return signal 时停止当前职责并重新进入 routing。

### 7.3 多 Skill 边界

普通职责不批量加载所有 Skill。

允许额外加载 platform-specific Skill 或其他被当前 primary Skill 明确允许的 supporting capability，但必须满足：

- 当前条件真实命中；
- 它承担的是可分离 supporting responsibility；
- 不改变 primary responsibility；
- 不接管完整生命周期；
- Consumer Repository Authority 允许。

例如：`execute-unit` 可以在 GitHub Actions completion evidence 真正需要专项处理时按需消费 `github-actions-verification`，但不会因此把所有 GitHub 工作自动变成平台 Skill 主导。

## 8. Stage Return 与旧状态失效

### 8.1 每次 Stage Return 都重新 routing

Stage Return 发生后：

```text
停止当前 responsibility
→ 丢弃当前 routing decision 作为继续授权
→ 重新读取受影响 Consumer Current Authority
→ 重新运行 discovery / routing
```

不得把第一次 routing 集合当成整个会话永久上下文。

### 8.2 Readiness 何时失效

不是所有返回都会让历史 Readiness 失效。

如果以下基础发生实质变化，则旧 Candidate Unit / Readiness 只对应旧语义基础：

- Product Intent；
- Specification WHAT / WHY；
- durable Technical Plan；
- Architecture / ADR；
- Execution Unit scope / acceptance ownership。

此时必须按真实影响重新进入 `slice-work` / `readiness-check`。

如果 `systematic-debug` 只修复实现缺陷，且没有改变上述基础，则可以在取得相应 Regression Evidence 后恢复原执行路径；不机械重做全部上游阶段。

## 9. Activation Decision

Runtime routing 的最小逻辑输出称为 **Activation Decision**。它是当前一次决策结果，不是长期 Authority，也不要求持久化。

至少能表达：

- `primary_responsibility`；
- `mode`：`routing-only` 或 `execute`；
- `stage_action`：`continue` / `return` / `fail-closed` / `escalate`；
- `primary_source`；
- `supporting_sources`；
- `skill_to_load`（仅 execute 且需要时）；
- `reason`；
- `invalidated_prior_state`（如旧 Readiness / routing 已失效）。

这些是逻辑字段，不要求所有 Runtime 使用同一 JSON schema。

## 10. Fail-closed

出现以下任一情况，不继续依赖当前 discovery result：

- Manifest / Catalog stale；
- source missing / selector 无法解析；
- current Authority identity 不明确；
- no-match 但当前仍存在治理 / 风险判断；
- 多个 primary candidate 无法可靠区分；
- Consumer override / supersede 关系无法确认；
- high-impact / irreversible / security / privacy / authorization boundary 不清；
- 需要的 Skill 本地不存在或版本身份不可确认。

回退路径：

```text
停止当前 derived discovery
→ 回到 Consumer-local Current Authority / Authority Map
→ 按当前问题扩大本地读取
→ 重新解析 responsibility
→ 必要时升级人工
```

ordinary runtime 的 fail-closed 不自动访问 upstream。

## 11. Runtime Adapter 边界

Runtime Adapter 可以：

- 读取 / 验证 Manifest / Catalog；
- 检查 source identity；
- 按显式 metadata 做确定性候选过滤；
- 暴露选定的 Consumer-local source / Skill；
- 记录可观察 discovery trace；
- 在 stale / missing 时返回 fail-closed signal。

Runtime Adapter 不可以：

- 私下定义 Method Stage；
- 在代码中维护另一套“migration → technical-plan”等隐藏职责语义；
- 覆盖 Consumer Repository Authority；
- 自动拉取 upstream 最新规则并改变 ordinary runtime；
- 为了方便 routing 缓存第二份 Requirement / Architecture / Rule 正文；
- 变成接管完整开发生命周期的 Controller。

职责语义必须来自当前 Consumer-local semantic owner / adopted capability；Adapter 只负责交付、发现和加载。

## 12. 与 Phase A 验收矩阵的映射

| 场景 | Phase D 接口保证 |
|---|---|
| CL-01 | 单一 primary responsibility + 最小 supporting set；execute 时才加载 Skill |
| CL-02 | Authority gap 可夺取 primary；Stage Return 后重新 routing；HOW / Architecture 变化使旧 Readiness 失效 |
| CL-03 | Consumer Authority first；override 不用数值 priority 解决 |
| CL-04 | Candidate Discovery 同时支持 Consumer-native Authority locator |
| CL-05 | `mode = routing-only` 时不加载完整 Skill |
| CL-06 | `mode = execute` 时只加载 primary Skill + 必要 supporting capability |
| CL-07 | source currentness 失败直接 fail-closed |
| CL-08 | no-match / ambiguity 不猜测、不自动访问 upstream |
| CL-09 | Phase D 消费本地 adoption 结果；具体 projection 由 Phase E 定义 |
| CL-10 | ordinary runtime 只读本地 current state，upstream 演进不参与 routing |
| CL-11 | superseded / disabled record 不进入 candidate current set |
| CL-12 | Catalog 删除后可从 Manifest / current owner 重建；不改变 semantic owner |

## 13. Phase D 完成结论

Phase D 接口不需要新的 Skill 或 Runtime Service。

当前最小模型是：

```text
Current Consumer Authority
+ Consumer-local Manifest / Catalog
        ↓
Fact-based Candidate Discovery
        ↓
One Primary Responsibility
+ Minimal Supporting Constraints
        ↓
routing-only stop
或
load current primary Skill
        ↓
Execute / Verify
        ↓
Stage Return → re-route
```

下一阶段应解决的已经不是“怎么选责任”，而是：

> upstream baseline 中的可复用 rule / module / Skill 如何经过 adopt / retain-or-override / reject，低成本、可审计地投射成上述 Consumer-local current assets？

这属于 Phase E — Baseline Adoption / Consumer-local Projection。