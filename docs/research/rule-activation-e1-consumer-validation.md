# E1 使用方新上下文验证

## 1. 目的

本文记录“规则治理与知识激活 v1”阶段 E / E1 的真实使用方验证证据。

验证目标不是证明 `agentic-dev` 的全部规则都应被使用方加载，而是验证 D1 形成的薄启动入口能否在真实 Consumer 的新上下文中：

- 先恢复 Consumer Repository Authority；
- 只激活当前任务真正需要的最小 `agentic-dev` 规则集；
- 保持 Consumer-local Method 与精确 baseline 优先；
- 不把 `agentic-dev` 自身项目规则带入 Consumer；
- 不因上下文缩减漏掉当前任务的高影响规则；
- 在未知、冲突或 Consumer-specific 语义上回退当前 Consumer Authority，而不是由上游方法猜测项目事实。

本文属于 Research / Evaluation Evidence，不是新的 Repository Authority。

## 2. 验证对象与基线

### agentic-dev

验证基线：

`master@7ba9f246380193733ede774634f40715a3f6bd97`

该提交已集成 PR #88，包含：

- 薄 `README` Bootstrap；
- `docs/guides/rule-activation-guide.md`；
- 阶段 D / D1～D2 收敛结果；
- E1 恢复入口。

### Consumer

Repository：

`dygapp/jilinjobs-cms`

Integrated baseline：

`main@982a214d65f8ebfa461a6488b89709c2be1a3863`

当前真实执行对象：

- PR #117 — `EU-50: run bounded Main source probe`
- Head：`547ac9453fd4ca6b85949810f3991d02f172e02f`
- Current Unit：EU-50 — Main Source Discovery & Article Snapshot Promotion
- PR state：Draft / Open

Consumer 当前固化的 `agentic-dev` Validation Baseline 仍为：

`master@d9fad0da83dbdb61cac5eb9778b0258c6861eef1`

E1 是 `agentic-dev` 自身的明确验证，不构成 Consumer baseline upgrade；最新 `agentic-dev` master 只作为本次验证输入，不覆盖 Consumer 已固化规则。

## 3. 隔离方式

本次采用逻辑 Fresh Context 隔离：

- Consumer 项目事实只从当前 GitHub Repository、PR / Actions 与直接 Authority 恢复；
- 不使用历史聊天、其他 Consumer 会话或个人记忆补充 Consumer 事实；
- 即使当前运行环境可见其他上下文，也不把它们作为 Requirement、Scope、Execute Authority 或当前状态来源；
- `agentic-dev` 项目 Roadmap、Issue、PR、Research 只用于协调本次 E1，不进入 Consumer 项目事实集。

这符合 `using-agentic-dev.md` §7 / §8.1 对逻辑新上下文和实验隔离的定义。

## 4. Consumer Authority 恢复

按 Consumer 自身 Documentation Authority Map 实际读取：

1. `AGENTS.md`；
2. `README.md`；
3. `docs/README.md`；
4. `docs/project/project-roadmap.md`；
5. `docs/project/development-method.md`；
6. Open PR #117；
7. PR Head 上的 `docs/work/current/eu50-main-source-discovery-promotion.md`；
8. 当前 PR Head 关联 GitHub Actions 与 Artifact 状态。

恢复结果：

- Consumer 当前唯一 Ready / Active Execution Unit 是 EU-50；
- EU-51 仍为 Candidate / BLOCKED，不具有 Execute Authority；
- EU-50 当前只允许 Article source discovery / bounded collection / classification / accepted snapshot promotion，不允许 Runtime import；
- source resource missing 只有明确 HTTP `404 / 410` 才能成立；其他异常必须显式分类，不能静默修复或丢弃；
- Page / List 当前属于 Site Package follow-up，不得进入 Main Historical Migration promotion；
- PR #117 当前仍保持 Draft，人类分类或阻塞事实存在时不能通过推断强行收口。

这些全部来自 Consumer Authority / Current Evidence，没有由 `agentic-dev` 推导产品规则。

## 5. 薄导航实际激活结果

先读取：

`docs/guides/rule-activation-guide.md`

根据当前 `scope + responsibility`，实际只需要继续激活以下 `agentic-dev` 来源。

### 5.1 Current Unit / Fresh Execution Context

来源：

- `skills/execute-unit/SKILL.md`
- `using-agentic-dev.md` §5.5 / §5.7

命中的关键规则：

- 一次只执行一个 Ready Execution Unit；
- 只加载当前 Unit 所需最小 Authority / Specification / Technical / Verification Context；
- Current Unit 不覆盖更高层 Consumer Authority；
- 当前证据必须匹配当前完成声明；
- 不自动进入下一个 Unit。

对 EU-50 的实际作用：确认 EU-51 不能因“下一步已经明确”而被提前执行，也不能把 EU-50 的 source collection 扩大成 Runtime import。

### 5.2 异步外部操作

来源：

- `docs/guides/external-operation-guidelines.md` §5.1
- `skills/github-actions-verification/SKILL.md` §11

命中的关键规则：

- Workflow 触发只表示执行请求进入中间态；
- `queued / pending / in_progress` 不等于完成；
- 当前运行环境仍可观察时，应继续读取终态、Jobs / Logs / Artifacts；
- 失败应先取得诊断证据，再决定修复 / 重试 / 升级；
- 只有真实人工权威、权限、安全、架构或高影响决定才构成人工停止条件。

PR #117 当前 Head `547ac945...` 的 PR-triggered `EU-50 Main Source Discovery` 和 `EU-50 Main Import Eligibility` 均已取得 terminal `success`，说明该规则可以直接落到真实 Consumer Actions 状态，而不依赖历史运行印象。

### 5.3 Evidence Claim / Trigger Topology

来源：

- `skills/github-actions-verification/SKILL.md` §4 / §4.1

命中的关键规则：

- Workflow 成功不能机械扩大为 Unit 完成；
- Evidence Claim 必须与实际 trigger / gate 对齐；
- 高成本 external-source collection 可以与 ordinary offline PR validation 分层；
- `workflow_dispatch`、`paths` 等只是 Consumer adapter，不是通用 Method 强制规则。

这与 PR #117 已明确的当前结构一致：ordinary stable CI 不依赖 Legacy Source，可访问外部源的 collection / retry 使用显式边界；EU-50 Completion 仍由 Current Work 的 10 项 Verification Strategy 和 Article promotion Gate 决定。

### 5.4 Ephemeral Evidence → Accepted Durable Input

来源：

- `docs/guides/external-operation-guidelines.md` §5.3
- `skills/github-actions-verification/SKILL.md` §10 / §10.1

当前真实证据：

`EU-50 Main Import Eligibility` Run `34323764969` 在 PR Head `547ac945...` 上产生 Artifact：

`eu50-main-article-eligibility-547ac9453fd4ca6b85949810f3991d02f172e02f`

Artifact facts：

- Artifact ID：`10092917399`
- digest：`sha256:fac36c148f54550f310b955cef73eacba7ed32de948fc819dda904263672fae5`
- `expired = false`
- expires at：`2026-09-16T07:26:20Z`

命中的关键规则：

- Artifact upload / existence 只能证明临时执行证据存在；
- Artifact 不因 Run PASS 自动成为 Consumer Authority 或长期运行输入；
- 被后续稳定迁移消费前，必须由 Consumer Authority 接受并晋升到 Consumer-owned 持久来源；
- 应保留 Run / Head / Artifact / digest 等 provenance / integrity；
- Promotion 改变目标 Head / input / Evidence Claim 后，需要对最终状态重新取得 Current Evidence。

这与 PR #117 自身“artifacts remain Evidence Candidates；destructive triage / accepted-snapshot promotion only after evidence closure”的边界一致。

## 6. 没有加载的内容

Consumer 执行上下文不需要机械读取：

- `agentic-dev/AGENTS.md`；
- `agentic-dev` Project Roadmap / 当前 Milestone 状态；
- 完整 `using-agentic-dev.md`；
- 完整 `external-operation-guidelines.md`；
- 全部 Skill；
- `evals/` 规则检索索引 / C1～C3 历史评估；
- LLM Wiki Research；
- CodeGraph Research / Runtime；
- WI-06 / WI-07 / WI-09 候选。

本次协调者为判断 E1 是否完成而读取的 `agentic-dev` Project Authority 不属于 Consumer Active Context，不能反向算作 Consumer 必需规则集。

## 7. Fail-closed / Consumer Override 检查

### 7.1 Consumer baseline 不被自动升级

Consumer 明确记录 Validation Baseline `d9fad0da...`，并规定普通开发优先 Consumer-local Method。

因此：

- 最新 `agentic-dev@7ba9f246...` 不能自动替换 Consumer baseline；
- E1 只验证最新薄导航是否能正确工作；
- 如果未来决定 baseline upgrade，仍必须走 Consumer 自己的显式 upgrade closure。

结果：**PASS**。

### 7.2 Product-specific source error 不由通用规则猜测

`SOURCE_RESOURCE_MISSING`、Article / Page / List ownership、retry budget、accepted Article arithmetic 等都是 Consumer-specific Authority。

薄导航没有尝试定义这些事实；遇到 source classification / migration ownership 时，实际判断回到 Consumer Requirement / Current Work / PR Evidence。

结果：**PASS**。

### 7.3 Main 与 PR 工作状态的层次没有混淆

Integrated `main` 仍记录 EU-50 Fresh Context Execute-baseline recovery；Open PR #117 与其 Head Current Work 则记录 Execute ACTIVE。

Consumer Documentation Authority Map 明确要求 Fresh Context 同时读取 Open PR / Actions / Current Evidence，因此没有把 `main` 的稳定长期状态误当成“PR 尚未开始”，也没有把未集成 PR 状态反写成 integrated Authority。

结果：**PASS**。

## 8. E1 判定

| 验证项 | 结果 | 证据摘要 |
|---|---|---|
| 使用方仓库权威始终优先 | PASS | Consumer baseline / local Method / EU-50 产品边界均保持优先 |
| 取得当前任务最小 `agentic-dev` 规则集 | PASS | 薄导航定位 execute-unit、异步外部操作、Actions evidence、Evidence Promotion |
| 不机械读取全部指南 | PASS | 只按风险读取现行来源的小节 / 当前 Skill；不加载完整规则栈 |
| 不把 `agentic-dev` 项目级规则带入使用方 | PASS | agentic-dev Roadmap / WI / Milestone 未成为 Consumer 事实 |
| 关键规则没有因缩减上下文丢失 | PASS | 单 Unit、EU-51 禁止自动进入、异步终态、Artifact Promotion、Consumer Override 全部命中 |
| fail-closed / override | PASS | Consumer-specific source error / ownership 全部回到 Consumer Authority |

E1 结论：**PASS**。

## 9. E2 判断

E2 — Consumer CodeGraph A/B 是可选项，不是本里程碑完成条件。

本次 E1 的主要风险是 Repository Authority / Method Activation / External Evidence，而不是源码入口发现；没有当前证据表明必须引入 CodeGraph 才能判断 E1。因此 E2 本轮记为：

**NOT RUN / OPTIONAL / NOT BLOCKING**。

不得把未执行 E2 解释成 CodeGraph 不具价值，也不得因此把 CodeGraph 升级为核心依赖。

## 10. 结论与后续

本轮真实 Consumer 证据支持 D1 的核心路线：

```text
Consumer Authority
→ 薄规则导航
→ 当前职责 / 风险
→ 最小现行 Guide / Skill
→ Consumer Current Evidence
→ fail-closed 回 Consumer Authority
```

当前没有证据支持：

- 删除 Consumer / Guide 中的源规则正文；
- 引入新的长期检索 Runtime；
- 引入 BM25 / vector / graph / MCP；
- 自动 baseline upgrade；
- 把 Evidence Candidate 自动晋升为 Authority；
- 启动 WI-07。

E1 完成后可以进入阶段 F 最终验证 / AI Review / 状态闭环。

## 11. F1 派生索引陈旧发现与修复

E1 后进入 F1 时，首次 `evals/run_rule_retrieval_ab.py --validate-only` 没有通过，而是按设计报告：

`rule-index 当前来源陈旧：AGENTS.md (source_identity_changed)`

该结果不是规则召回回归，而是 D1/D2 PR #88 后续项目状态闭环修改了 `AGENTS.md` 的整文件 blob identity，B3 派生索引仍保存旧 identity。进一步对比确认：索引唯一指向的 `AGENTS.md`“外部操作治理”段落在 PR #88 前后语义与正文均未改变。

处理方式：

- 保留 fail-closed 陈旧检测，不降级或绕过；
- 先完成项目状态证据措辞修正，再按最终 `AGENTS.md` blob 重建派生 `rule-index.json` source identity；
- 不修改 entry_key、scope、responsibility、condition、activation_summary 或 required_checks；
- 修正阶段 D 记录中“治理评估输入完全未变化”的过度表述；
- 重新执行 F1 静态检索回归。

第二次临时修复运行曾因“先刷新 identity、后修改 `AGENTS.md`”的顺序错误再次触发同一 fail-closed；最终修复改为以所有长期文本修正后的最终 blob 重建 identity。该过程反向证明陈旧源保护能够持续阻止旧派生索引被静默继续使用。
