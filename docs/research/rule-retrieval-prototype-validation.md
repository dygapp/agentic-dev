# 最小规则检索原型验证

验证日期：2026-09-08

阶段：**规则治理与知识激活 v1 / 阶段 B / B3 — 原型验证**

文档性质：**研究验证证据**

执行基线：

`master@7d1190ce554dc273916c010747c3653929def50a`

B1 契约：

`docs/research/minimal-rule-retrieval-contract.md`

B2 选择：

`docs/research/rule-retrieval-prototype-selection.md`

原型：

- `evals/rule-retrieval/rule-index.json`
- `evals/query_rule_index.py`

本文只证明 B2 选择的最小派生原型已经具备进入阶段 C 评估设计的基础能力。它不是阶段 C 的 A/B 结果，不证明新的激活模式已经优于当前粗粒度加载，也不把原型提升为长期运行时或 Repository Authority。

## 1. 实际分支与文件身份

B3 实现分支：

`feat/rule-retrieval-prototype`

分支从 `master@7d1190ce554dc273916c010747c3653929def50a` 创建。

当前原型文件身份：

| 文件 | GitHub blob |
|---|---|
| `evals/rule-retrieval/rule-index.json` | `62685de3ae729aff6d71dda97a2e2c13fea7a34f` |
| `evals/query_rule_index.py` | `01ae951bdc0cfa6368c93638935191484abd60fa` |

实际 GitHub 分支文件已重新读取，查询器包含“先应用所有已知维度不匹配，再判断未知维度是否需要回退”的最终逻辑；这避免无关候选因为未提供另一个维度而错误触发 `fallback_required`。

## 2. 索引覆盖

首轮索引共 **61 个条目**：

- `UG-01`～`UG-27`：27 个 `using-agentic-dev.md` 激活单元；
- `EO-01`～`EO-28`：28 个 `external-operation-guidelines.md` 激活单元；
- `PTR-AGENTS-EXT`：1 个 `AGENTS.md` 外部操作薄指针；
- `CON-SLICE`、`CON-READINESS`、`CON-EXEC`、`CON-CONVERGE`、`CON-GHA`：5 个 Skill 职责消费项。

索引没有批量纳入：

- Research / PR / Issue 历史全文；
- 已完成项目记录流水；
- 全部工程纪律；
- 全部技术画像；
- 全部 Skill 正文；
- 普通未审计文档。

因此首轮原型仍保持为“阶段 A 已审计规则面 + 最小跨层关系样本”，不是全仓库规则数据库。

## 3. 当前规范性来源身份

索引当前涉及 **8 个唯一规范性来源**。B3 对照当前 GitHub 源文件重新核验身份：

| 来源 | 当前 blob | 结果 |
|---|---|---|
| `docs/guides/using-agentic-dev.md` | `b8ccf80a5e8c14560a7bfd77450045e55ccbfaf1` | 匹配 |
| `docs/guides/external-operation-guidelines.md` | `f22de650351b89563a70653d4fdb96d4f24e6be3` | 匹配 |
| `AGENTS.md` | `394281f72cbcc933253819849efbd72d206eb541` | 匹配 |
| `skills/slice-work/SKILL.md` | `ffebf73f0b1f9213fe1334b94d2a360b10678d63` | 匹配 |
| `skills/readiness-check/SKILL.md` | `6745eb0af71f6cf920479ecc5fe47db7bbd59e80` | 匹配 |
| `skills/execute-unit/SKILL.md` | `c71ddd23d20b3a14c9cb19a38f6e8d6cbedcf46e` | 匹配 |
| `skills/converge/SKILL.md` | `363d9b21744cb5a04d16102dd7243446d2d19b83` | 匹配 |
| `skills/github-actions-verification/SKILL.md` | `5040e60a8a2274d8fead8375aaf66311392769ce` | 匹配 |

这组检查证明当前索引没有在创建时就引用已经陈旧的来源。

## 4. 查询器静态能力检查

实际分支查询器已复核以下行为：

1. 只使用 Python 标准库；
2. 索引结构检查覆盖必需字段、允许角色、强度和关系类型；
3. 关系目标必须指向现有 `entry_key`；
4. 查询前先检查全部索引活动源的 Git blob 兼容内容身份；
5. 来源缺失或身份变化时返回 `fallback_required`，退出码为 `2`；
6. `scope` 与 `responsibilities` 为必需查询维度；
7. `stage / subject / conditions` 可以省略，但省略时不猜测；
8. 已知维度不匹配先排除候选，只有仍可能适用且缺少必要维度时才触发未知条件回退；
9. 不使用固定 Top-K；
10. `superseded-by` 只在索引明确存在该关系时排除旧条目，不根据时间戳推断；
11. `equivalent` / `scope-variant` 关系保留独立来源指针；
12. 查询器不修改源文档、索引、权限或外部状态。

## 5. 代表性查询检查

B3 使用与当前索引结构等价的隔离 Python 执行检查查询语义，并在写入分支后重新读取实际查询器确认实现逻辑一致。该检查不是 Agent 运行时 A/B，也不代替阶段 C 的隔离新上下文评估。

### 5.1 就绪检查 / 上游语义失效

输入维度：

```text
scope = consumer-project
responsibility = readiness
stage = readiness
subject = execution-unit
conditions = slice-or-readiness + upstream-semantics-invalid
```

结果集合：

- `UG-01`
- `UG-02`
- `UG-03`
- `UG-14`
- `UG-15`
- `CON-READINESS`

观察：核心不变量、切分 / 就绪边界、上游语义失效重入和对应 Skill 消费项均被召回，没有加载无关外部操作规则。

### 5.2 使用方新上下文恢复

输入维度：

```text
scope = consumer-project
responsibility = context-recovery
stage = recovery
subject = project-context
conditions = fresh-context-recovery
```

结果集合：

- `UG-01`
- `UG-02`
- `UG-03`
- `UG-25`

观察：只返回使用方权威、渐进式披露、证据不变量和新上下文恢复规则。

### 5.3 普通外部写操作

输入维度：

```text
scope = external-operation
responsibility = external-operation
subject = external-state
conditions = external-write
```

结果集合：

- `EO-07`
- `EO-09`

观察：低风险 / 高影响 / 异步 / GitHub 等未触发条件规则没有被机械加载；已知条件不匹配会在未知阶段判断前排除。

### 5.4 跨仓库操作

输入维度：

```text
scope = external-operation + cross-repository
responsibility = cross-repository-coordination
subject = repository-boundary
conditions = multi-repository-operation
```

结果集合：

- `EO-03`

观察：只有同时满足外部操作与跨仓库作用域时才激活该边界，普通单仓库操作不会误得跨仓库授权规则。

## 6. 回退检查

### 6.1 查询维度未知

对 readiness 场景省略 `conditions` 时：

- 核心不变量仍可确定；
- `UG-07`、`UG-14`、`UG-15`、`CON-READINESS` 等仍可能适用但缺少必要条件信息；
- 查询器返回 `fallback_required = true`；
- `fallback_reason = query_dimensions_unknown`；
- 退出码为 `2`；
- 不猜测条件，也不把不完整结果宣称为最小正确规则集。

### 6.2 来源陈旧

隔离检查中修改一个已索引源的内容但保持索引旧身份：

- 查询器在筛选前发现来源身份变化；
- 返回 `fallback_required = true`；
- `fallback_reason = indexed_source_stale_or_missing`；
- 明确报告陈旧来源；
- 退出码为 `2`；
- 不继续使用旧索引返回“完整”结果。

这验证了 B2 在集成前补强的关键边界：不能只检查最终已命中的源，否则新规则可能因旧索引未命中而被静默遗漏。

## 7. 取代关系算法边界

当前真实索引**没有为了测试而虚构 `superseded-by` 关系**。

B3 只对查询器算法做隔离合成检查：测试副本中临时建立一个 `superseded-by` 关系后，旧条目会被排除；该合成关系没有写入仓库。

这保持以下边界：

- 原型支持 B1 已冻结的最小关系语义；
- 只有现行权威明确支持真实取代关系时才可进入实际索引；
- 不使用文件时间、提交时间或索引顺序推断规则取代。

## 8. 可删除 / 可重建与第二权威检查

B3 当前原型满足：

1. 删除 `evals/rule-retrieval/rule-index.json` 不会删除任何规范性规则；
2. 删除 `evals/query_rule_index.py` 不会改变任何方法、指南、Skill 或项目权威；
3. 每个活动索引条目独立保存 `source.path + source.section + source.identity`；
4. `activation_summary` 和 `required_checks` 只作为派生消费信息，不能覆盖或扩张源权威；
5. 原型内部 `entry_key` 明确不是永久规则身份；
6. Research 解释映射依据，但查询器的活动规则仍必须回到当前规范性源验证；
7. 当前没有通过索引复制完整指南正文或 Skill 正文。

因此派生原型被删除后，阶段 A 映射和当前仓库权威仍足以重新建立新的原型；不会产生规则事实损失。

## 9. GitHub 自动化验证边界

当前仓库基线上没有可直接复用的 `.github/workflows` 路径用于本原型验证。本 B3 没有为了取得一个绿色状态额外创建 GitHub Actions 工作流。

因此本步骤不能报告“GitHub Actions 通过”。当前证据由：

- GitHub 实际分支文件复核；
- 当前源 blob 身份对照；
- 查询算法等价隔离执行；
- 手工查询结果检查；
- 后续 PR 差异 / AI 复核

共同组成。

真正的 Agent 新上下文隔离 A/B、语义断言和人工评分属于阶段 C，不在 B3 提前执行。

## 10. B3 结论

B3 的四项协调门禁已经具备证据：

- **对阶段 A 规则单元建立最小索引**：完成，61 个条目 / 8 个唯一规范性来源；
- **手工检查查询结果**：完成，代表性职责、范围、条件与回退场景可区分；
- **确认删除索引不损失长期事实**：完成，规范性事实仍全部位于当前 Repository Authority；
- **确认没有复制成第二权威**：完成，索引只保存短派生摘要、检查与源指针，不复制完整规则正文。

因此阶段 B 可以在本候选集成后结束，下一实际工作进入：

> **阶段 C — 检索 / 激活评估 / C1 — 定向评估设计**

该结论只说明最小检索原型已经可用于设计后续评估；是否真正改善规则召回、上下文噪声、输入成本或 Agent 行为正确性，必须由阶段 C 的 A/B 隔离运行与人工语义评分回答。
