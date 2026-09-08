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
| `evals/rule-retrieval/rule-index.json` | `e2ed5605d0a6496fc7f37b77ef5bbf9cc65e94dd` |
| `evals/query_rule_index.py` | `361285de931b9341d73f645d0b3cd170eaf7b785` |

最终查询器包含两个集成前修正：

1. 先应用所有已经明确提供的维度排除不适用条目，再判断仍可能适用的条目是否缺少必要维度；
2. `scope / responsibility / stage / subject / conditions` 中出现首轮索引未建模值时直接返回 `fallback_required`，不能把未知范围伪装成“当前没有规则”。

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

索引当前涉及 **8 个唯一规范性来源**。最终候选重新对照当前分支源文件身份：

| 来源 | 当前 blob | 结果 |
|---|---|---|
| `docs/guides/using-agentic-dev.md` | `b8ccf80a5e8c14560a7bfd77450045e55ccbfaf1` | 匹配 |
| `docs/guides/external-operation-guidelines.md` | `f22de650351b89563a70653d4fdb96d4f24e6be3` | 匹配 |
| `AGENTS.md` | `3e34d542922d7b22768d108d1d6a70416427a2c5` | 匹配 |
| `skills/slice-work/SKILL.md` | `ffebf73f0b1f9213fe1334b94d2a360b10678d63` | 匹配 |
| `skills/readiness-check/SKILL.md` | `6745eb0af71f6cf920479ecc5fe47db7bbd59e80` | 匹配 |
| `skills/execute-unit/SKILL.md` | `c71ddd23d20b3a14c9cb19a38f6e8d6cbedcf46e` | 匹配 |
| `skills/converge/SKILL.md` | `363d9b21744cb5a04d16102dd7243446d2d19b83` | 匹配 |
| `skills/github-actions-verification/SKILL.md` | `5040e60a8a2274d8fead8375aaf66311392769ce` | 匹配 |

在项目状态入口推进到阶段 C 后，`AGENTS.md` 的文件 blob 发生变化；索引中的 `PTR-AGENTS-EXT` 已同步刷新到新 blob。最终候选因此不会因为自身状态回写而在查询开始时立即判定为陈旧。

## 4. 查询器最终静态能力检查

最终分支查询器已重新读取并复核以下行为：

1. 只使用 Python 标准库；
2. 索引结构检查覆盖必需字段、允许角色、强度和关系类型；
3. 非对象条目、非法 `entry_key` 和非法关系不会进入后续假设路径；
4. 关系目标必须指向现有 `entry_key`；
5. 查询前先检查全部索引活动源的 Git blob 兼容内容身份；
6. 来源缺失或身份变化时返回 `fallback_required`，退出码为 `2`；
7. `scope` 与 `responsibilities` 为必需查询维度；
8. `stage / subject / conditions` 可以省略，但省略时不猜测；
9. 任一已提供查询值不在首轮索引词表时返回 `query_values_not_modeled` 回退；
10. 已知维度不匹配先排除候选，只有仍可能适用且缺少必要维度时才触发 `query_dimensions_unknown` 回退；
11. 不使用固定 Top-K；
12. `superseded-by` 只在索引明确存在该关系时排除旧条目，不根据时间戳推断；
13. `equivalent / scope-variant` 关系不消除独立来源指针；
14. 查询器不修改源文档、索引、权限或外部状态，也不访问网络、模型或数据库。

## 5. 代表性查询语义检查

B3 初版使用与索引结构等价的隔离 Python 执行检查了主要过滤语义，并在写入分支后重新读取实际查询器确认对应实现。最终收口新增的“未知查询值回退”和来源身份刷新是在该初版执行之后完成，因此本节不会把早期运行结果冒充为最终 Head 的完整运行时证据。

阶段 C 必须使用最终集成基线重新执行真正的新上下文 / 隔离 A/B。

### 5.1 就绪检查 / 上游语义失效

输入维度：

```text
scope = consumer-project
responsibility = readiness
stage = readiness
subject = execution-unit
conditions = slice-or-readiness + upstream-semantics-invalid
```

预期并经初版等价执行检查的结果集合：

- `UG-01`
- `UG-02`
- `UG-03`
- `UG-14`
- `UG-15`
- `CON-READINESS`

该集合覆盖核心不变量、切分 / 就绪边界、上游语义失效重新进入和对应 Skill 消费项，不需要加载外部操作规则。

### 5.2 使用方新上下文恢复

输入维度：

```text
scope = consumer-project
responsibility = context-recovery
stage = recovery
subject = project-context
conditions = fresh-context-recovery
```

预期并经初版等价执行检查的结果集合：

- `UG-01`
- `UG-02`
- `UG-03`
- `UG-25`

### 5.3 普通外部写操作

输入维度：

```text
scope = external-operation
responsibility = external-operation
subject = external-state
conditions = external-write
```

预期并经初版等价执行检查的结果集合：

- `EO-07`
- `EO-09`

低风险、高影响、异步、GitHub 等其他条件规则不应被机械加载。

### 5.4 跨仓库操作

输入维度：

```text
scope = external-operation + cross-repository
responsibility = cross-repository-coordination
subject = repository-boundary
conditions = multi-repository-operation
```

预期并经初版等价执行检查的结果集合：

- `EO-03`

## 6. 回退边界

### 6.1 必要查询维度未提供

对 readiness 场景省略 `conditions` 时，仍可能适用的条件规则不能安全判定。查询器应：

- 返回 `fallback_required = true`；
- 使用 `fallback_reason = query_dimensions_unknown`；
- 指出仍缺少判定维度的候选；
- 不把部分结果宣称为最小正确规则集。

### 6.2 查询值未建模

最终查询器新增保守边界：如果输入包含当前首轮索引没有建模的作用域、职责、阶段、目标对象或条件值，则：

- 返回 `fallback_required = true`；
- 使用 `fallback_reason = query_values_not_modeled`；
- 返回具体 `unknown_query_values`；
- 不以零命中或部分命中推断“当前没有适用规则”。

这对应 B1 的范围不确定回退要求，也明确承认首轮 61 项原型不是全仓库规则数据库。

### 6.3 来源陈旧

查询器在筛选前校验首轮原型全部活动规范性来源：

- 任一源缺失或 blob 身份变化，返回 `fallback_required = true`；
- `fallback_reason = indexed_source_stale_or_missing`；
- 明确报告陈旧来源；
- 不继续使用旧索引声称完整召回。

该边界避免“旧索引没有命中新规则，因此也没有机会检查新规则所在来源”的静默漏召回。

## 7. 取代关系算法边界

当前真实索引**没有为了测试而虚构 `superseded-by` 关系**。

B3 初版只对算法做过隔离合成检查：测试副本临时建立 `superseded-by` 关系后旧条目被排除；该合成关系没有写入仓库。

最终实现仍保持：

- 只有现行权威明确支持真实取代关系时才可进入实际索引；
- 不使用文件时间、提交时间或索引顺序推断规则取代；
- 关系只是派生导航 / 过滤信息，不建立新的规范性优先级。

## 8. 可删除 / 可重建与第二权威检查

B3 当前原型满足：

1. 删除 `evals/rule-retrieval/rule-index.json` 不会删除任何规范性规则；
2. 删除 `evals/query_rule_index.py` 不会改变任何方法、指南、Skill 或项目权威；
3. 每个活动索引条目独立保存 `source.path + source.section + source.identity`；
4. `activation_summary` 和 `required_checks` 只作为派生消费信息，不能覆盖或扩张源权威；
5. 原型内部 `entry_key` 明确不是永久规则身份；
6. Research 解释映射依据，但查询器的活动规则仍必须回到当前规范性源验证；
7. 当前没有通过索引复制完整指南正文或 Skill 正文；
8. 当前没有为了原型给全库统一增加文件头。

因此派生原型被删除后，阶段 A 映射和当前仓库权威仍足以重新建立新的原型，不会产生规则事实损失。

## 9. 自动化验证边界

当前仓库在该分支上不存在 `.github/workflows`，没有可直接复用的 GitHub Actions 验证入口。B3 没有为了取得绿色状态临时增加工作流。

因此不能报告“最终 B3 Head 的 GitHub Actions / 运行时验证通过”。当前 B3 证据由：

- GitHub 实际分支文件与最终差异复核；
- 8 个当前源 blob 身份对照；
- 初版查询算法的等价隔离执行；
- 最终实现的静态逻辑复核；
- 代表性查询与回退语义检查；
- 后续 PR Final AI Review

共同组成。

这一区分是有意保留的：真正需要比较 Agent 行为、规则召回、噪声、文件读取和上下文成本的运行时证据属于阶段 C，而不是通过 B3 自证原型来替代。

## 10. B3 结论

B3 的四项协调门禁已经具备证据：

- **对阶段 A 规则单元建立最小索引**：完成，61 个条目 / 8 个唯一规范性来源；
- **手工检查查询结果**：完成，代表性职责、范围、条件与回退场景可区分；
- **确认删除索引不损失长期事实**：完成，规范性事实仍全部位于当前 Repository Authority；
- **确认没有复制成第二权威**：完成，索引只保存短派生摘要、检查与源指针，不复制完整规则正文。

因此阶段 B 可以在本候选集成后结束，下一实际工作进入：

> **阶段 C — 检索 / 激活评估 / C1 — 定向评估设计**

该结论只说明最小检索原型已经可用于设计后续评估；是否真正改善规则召回、上下文噪声、输入成本或 Agent 行为正确性，必须由阶段 C 的 A/B 隔离运行与人工语义评分回答。
