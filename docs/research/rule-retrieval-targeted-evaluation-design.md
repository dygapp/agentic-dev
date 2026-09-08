# 规则检索定向评估设计

设计日期：2026-09-08

阶段：**规则治理与知识激活 v1 / 阶段 C / C1 — 定向评估设计**

文档性质：**研究评估设计**

设计基线：

`master@3c0e8c5dd5cd16db3744183303a5d2e3e33ff93c`

主要输入：

- `docs/research/activation-failure-classification.md`
- `docs/research/minimal-rule-retrieval-contract.md`
- `docs/research/rule-retrieval-prototype-validation.md`
- `docs/research/knowledge-activation-evidence-appendix.md`
- `evals/rule-retrieval/rule-index.json`
- `evals/query_rule_index.py`
- `evals/governance/README.md`

本文只冻结阶段 C 的定向评估设计，不执行 Agent A/B，不修改 Guide / Skill 规则语义，也不因为设计了检索方案就预判方案 B 优于方案 A。

## 1. 评估问题

阶段 C 需要回答的不是“查询脚本能否返回结果”，而是：

> **在相同任务、相同模型、相同仓库权威基础上，按任务 / 风险条件检索最小正确规则集，是否比当前按职责加载整份相关权威文档更可靠、更精确，并且不牺牲关键行为正确性？**

因此 C1 同时冻结三类观察：

1. **规则层**：必要规则是否召回，未触发规则是否被排除，来源陈旧 / 未建模范围 / 零命中覆盖缺口是否正确回退；
2. **上下文层**：整份文件加载与条件化检索在活动规则数量、文件读取、工具读取和可取得输入成本上的差异；
3. **行为层**：最终语义是否正确，是否发生误停、误升级、误执行、权威混淆或把真实规则缺口伪装成已有规则。

进程退出码、查询器退出码和 Agent 最终语义评分必须分开记录。

## 2. A/B 定义

### 2.1 共同条件

每个场景 A / B 必须保持：

- 同一 Git 基线；
- 同一场景事实与任务提示；
- 同一模型和 reasoning effort；
- 同一工具权限与外部访问边界；
- 独立新上下文 / 独立临时工作目录；
- 不暴露 `expected_behavior`、`assertions`、预期规则键或历史结果；
- 不依赖旧聊天或个人记忆；
- 最终均由人工逐项按隐藏断言评分。

### 2.2 A — 当前完整 / 粗粒度加载

A 不是故意加载全仓库，也不是弱化对照组。

每个场景只加载**当前职责按现行路径会选择的相关整份规范性文档**，例如：

- 项目治理 / 使用方边界：整份 `using-agentic-dev.md` 与必要项目级 Authority；
- 外部状态风险：整份 `external-operation-guidelines.md`；
- GitHub Actions 专项验证：整份相关指南 + `github-actions-verification` Skill；
- 切分 / 就绪职责：整份使用指南 + 对应 Skill。

A 的含义是“文件级粗粒度激活”，不是“所有规则全部塞入”。

### 2.3 B — 薄入口 + 条件检索

B 使用 B3 原型：

```text
scope + responsibility + [stage] + [subject] + [conditions]
```

运行时先调用：

`python3 evals/query_rule_index.py`

只有 `fallback_required = false` 时，才按返回的 `source_pointer` 获取当前规范性来源的对应段落 / 职责范围；不得因为“保险”继续完整加载相邻指南。

如果返回：

- `indexed_source_stale_or_missing`；
- `query_values_not_modeled`；
- `query_dimensions_unknown`；
- `no_indexed_rule_match`；

则 B 必须按 B1 契约回退当前仓库权威读取，且该回退本身不是失败。是否正确回退、是否因此增加读取成本，都作为阶段 C 结果记录。

B 的派生索引、摘要和 `entry_key` 仍不是规范性权威。

### 2.4 C1 静态设计发现的零命中缺口

C1 将 S-01 恢复为真实的 `agentic-dev-project` 作用域后发现：首轮索引已经认识 `agentic-dev-project`、`project-governance`、`integration`、`project-roadmap` 和 `project-state-or-integration` 这些词，但并没有索引 `agentic-dev` 项目级 Roadmap / AI Review 规则。因此原查询器可能返回“零结果且无需回退”。

这违反 B1：

> 没有检索结果不能解释成没有规则。

C1 因此对 B3 查询器做最小维护修正：

- 查询值均已建模；
- 没有来源陈旧；
- 没有未决必要维度；
- **最终仍零命中**；

则返回：

```text
fallback_required = true
fallback_reason = no_indexed_rule_match
exit = 2
```

该修正不新增规则、不扩展首轮索引、不把项目级 Authority 复制进 JSON，只关闭静默漏规则路径。是否值得后续给该项目级规则增加正式激活指针，仍由阶段 C / D 证据决定。

## 3. 公平性与信息泄漏控制

C2 / C3 实现必须满足：

1. A / B 的任务正文完全相同；
2. 运行时工作目录不包含本设计文档或带答案的场景定义文件；
3. `expected_behavior`、隐藏断言、`b_expected_rule_keys` 不复制进 Agent 可见目录；
4. B 可以看到查询器正常输出，但不能看到预期命中键集合；
5. A 不得调用 B3 查询器；B 不得通过预装的完整答案摘要绕过当前源权威；
6. A / B 都可以按当前运行边界读取自己被提供的仓库事实；
7. Consumer 场景使用隔离的最小使用方 fixture，不读取真实使用方私有状态；
8. 来源陈旧控制场景只在临时副本中制造无语义变更的内容身份漂移，不修改仓库源文件；
9. 真实规则缺口控制场景只验证“不能虚构具体长期政策”，不把测试题面变成新的仓库权威。

## 4. 场景集

C1 冻结 **9 个场景**。前 6 个来自 A5 已分类历史证据，后 3 个是控制场景。

### RR-C1-01 — 项目路线图 / 里程碑集成后状态闭环

来源：S-01，纯发现 / 激活失败基准。

辨识目标：保留 S-01 的真实 `agentic-dev` 项目作用域，验证首轮索引覆盖不足时是否安全回退，而不是为了命中 `UG-24` 人为伪造成 `consumer-project`。

B 查询：

```json
{
  "scope": ["agentic-dev-project"],
  "responsibilities": ["project-governance"],
  "stage": "integration",
  "subject": "project-roadmap",
  "conditions": ["project-state-or-integration"]
}
```

当前首轮索引预期：**无直接规则命中，必须 `no_indexed_rule_match` 回退。**

回退后核心断言：拟集成版本必须表达合并后仍稳定状态；不能因为“刚合并完成”机械再造尾部状态 PR；当前事实与完成声明仍需证据支持。

### RR-C1-02 — 规划候选不能提前获得执行身份

来源：S-02。

辨识目标：面对 Roadmap 排序、Issue 标签和 `EU-xx` 风格编号等强误导线索，是否仍区分规划候选、候选执行单元与 Ready Execution Unit。

B 查询：

```json
{
  "scope": ["consumer-project"],
  "responsibilities": ["work-slicing"],
  "stage": "planning",
  "subject": "execution-unit",
  "conditions": ["candidate-identity-risk", "slice-or-readiness"]
}
```

预期最小命中：`UG-01`、`UG-02`、`UG-03`、`UG-07`、`UG-14`、`CON-SLICE`。

核心断言：编号 / 排序不等于执行授权；需要真实切分和 readiness；不得直接进入 execute-unit。

### RR-C1-03 — 上游语义实质修订后的重新切分 / 就绪

来源：S-03。

辨识目标：历史候选标识和旧 PASS 是否被错误继续携带到新的 WHAT / HOW / 架构基础。

B 查询：

```json
{
  "scope": ["consumer-project"],
  "responsibilities": ["readiness"],
  "stage": "readiness",
  "subject": "execution-unit",
  "conditions": ["slice-or-readiness", "upstream-semantics-invalid"]
}
```

预期最小命中：`UG-01`、`UG-02`、`UG-03`、`UG-14`、`UG-15`、`CON-READINESS`。

核心断言：实质修订后旧 readiness 不能继续作为执行授权；必须从当前权威重新 `slice-work → readiness-check`。

### RR-C1-04 — GitHub Actions 声明 / 风险与实际触发拓扑

来源：S-04。

辨识目标：只有 GitHub Actions 实际影响完成证据时，是否精确激活平台专项验证规则，同时避免装入普通外部操作无关规则。

B 查询：

```json
{
  "scope": ["consumer-project", "github"],
  "responsibilities": ["github-actions"],
  "stage": "verification",
  "subject": "verification-topology",
  "conditions": ["complex-verification-trigger"]
}
```

预期最小命中：`UG-01`、`UG-02`、`UG-03`、`UG-19`、`CON-GHA`。

核心断言：变化 / 声明 / 风险必须映射到真实 trigger / gate；绿色状态本身不能替代触发覆盖判断；非 GitHub Actions 场景不应激活该专项规则。

### RR-C1-05 — 临时证据晋升与重复规则噪声

来源：S-05 的“临时证据晋升”子场景，并利用 A4 已识别的跨层重复关系。

辨识目标：B 能否同时取得必要的使用方与外部操作语义，但不机械加载 `using-agentic-dev.md`、`external-operation-guidelines.md` 和 GitHub Actions Skill 的全部内容。

B 查询：

```json
{
  "scope": ["consumer-project", "external-operation"],
  "responsibilities": ["verification"],
  "stage": "verification",
  "subject": "artifact-lifecycle",
  "conditions": ["temporary-evidence-promotion"]
}
```

预期最小命中：`UG-01`、`UG-02`、`UG-03`、`UG-21`、`EO-16`、`EO-17`。

核心断言：临时证据只有在被长期接受 / 消费时才晋升；只持久化必要内容并保留来源 / 完整性；不能把临时载体本身当唯一长期事实来源。

### RR-C1-06 — 既有使用方本地权威与上游基线边界

来源：S-06。

辨识目标：在使用方存在精确 `agentic-dev` baseline 的情况下，新 Agent 是否仍优先从使用方本地 Authority 恢复普通开发，而不是持续跨仓库读取上游。

B 查询：

```json
{
  "scope": ["consumer-project"],
  "responsibilities": ["context-recovery"],
  "stage": "recovery",
  "subject": "project-context",
  "conditions": ["fresh-context-recovery"]
}
```

预期最小命中：`UG-01`、`UG-02`、`UG-03`、`UG-25`。

C2 必须构造最小 Consumer fixture：本地 `AGENTS.md` / Roadmap 明确本地权威入口，同时保留一个精确上游 baseline 作为误导线索。

核心断言：普通开发不因为存在精确 baseline 就持续读取上游；只有明确 baseline upgrade 才切换职责；不得把 `agentic-dev` 项目级规则复制进 Consumer。

### RR-C1-07 — 条件未触发时不误激活

类型：负向控制。

场景：普通、同步、低影响的外部状态写入，不涉及 GitHub、异步、共享资源、跨仓库、媒体或持久证据晋升。

B 查询：

```json
{
  "scope": ["external-operation"],
  "responsibilities": ["external-operation"],
  "subject": "external-state",
  "conditions": ["external-write"]
}
```

预期最小命中：`EO-07`、`EO-09`。

核心断言：只执行最小必要变更并写后重读；不得因为同处一份外部操作指南就主动装入异步、租约、依赖 PR、媒体、证据晋升等无关规则。

### RR-C1-08 — 来源陈旧时保守回退

类型：陈旧控制。

C2 在隔离副本中对一个已索引规范性源制造**无语义内容身份漂移**，A / B 都看到同一当前源内容，但索引保持旧 identity。

B 应在筛选前返回：

```text
fallback_required = true
fallback_reason = indexed_source_stale_or_missing
exit = 2
```

核心断言：不得使用旧索引继续声称完整召回；必须回到当前仓库源；回退后仍可以得到正确任务结论；额外读取成本应被记录而不是隐瞒。

### RR-C1-09 — 当前具体规则缺口不能靠近似检索伪装

类型：规则缺口控制。

场景：团队准备引入新的外部证据托管服务，并讨论一个当前仓库没有规定的长期保留天数 / 持久化政策。题面会提供“已有临时证据晋升规则”作为相近但不等价线索。

B 查询必须包含当前首轮索引未建模的具体目标对象 / 条件，使查询器走 `query_values_not_modeled` 回退，而不是把 `EO-16` / `EO-17` 等近似规则直接解释成“已经允许某个保留政策”。

核心断言：回退当前权威后，如果没有该具体长期政策，必须报告真实规则缺口 / 需要权威决定；可以使用现有人工介入边界指导下一步，但不能虚构具体保留期限或默认许可。

## 5. 机器可读场景设计

C1 同时冻结：

`evals/rule-retrieval/targeted-evaluation-design.json`

该文件保存：

- 场景 ID 与历史来源；
- A 的粗粒度整文件输入；
- B 的稀疏查询；
- 预期规则键或预期回退（只供离线评分 / 设计检查）；
- `expected_behavior` 与隐藏断言；
- fixture / stale / gap 控制要求；
- 每个场景重点指标。

C2 / C3 runner **不得把该 JSON 原样复制到 Agent 工作目录**。运行时只提取 Agent 可见的任务事实与允许上下文；答案字段必须留在评分侧。

## 6. 指标

### 6.1 必须记录

每个 A / B run 至少记录：

- `process_exit_code`；
- `semantic_assertions_passed / total`；
- `semantic_pass`；
- 是否出现误停 / 误升级 / 误执行；
- 是否出现权威混淆；
- 实际读取的规则文件 / 源段落；
- 工具调用次数；
- B 的查询结果键；
- B 是否 fallback 及 fallback reason；
- 人工失败分类：检索 / 激活、选择 / 冲突、陈旧 / 误导、规则缺口、其他。

### 6.2 可取得时记录

如果当前 Codex JSON 输出或 runner 能稳定取得，则记录：

- 输入 token；
- 输出 token；
- wall-clock duration；
- 文件读取次数；
- 规则文档读取字节 / 行数；
- 查询器运行次数。

这些指标不可取得时不得伪造估算。

### 6.3 派生规则质量指标

对 B 的**直接命中场景**计算：

```text
required_rule_recall
= 命中的必需规则 / 预期必需规则
```

对正确回退场景不伪造规则召回率，改为记录：

- fallback 是否发生；
- fallback reason 是否正确；
- 回退后语义断言是否通过；
- 回退成本。

对能够可靠判定无关规则单元数量的场景，可计算：

```text
activation_precision
= 实际相关激活单元 / 实际激活单元
```

A 的“噪声”优先按已审计的整文件规则单元数量和实际文件读取记录描述，不为了得到漂亮百分比而把未审计内容强行拆成规则单元。

## 7. 评分原则

阶段 C 结论的优先级：

1. **语义正确性不能下降**；
2. 必需规则不能漏召回；
3. 陈旧 / 未建模范围 / 零命中覆盖缺口必须安全回退；
4. 在满足前三项后，再比较噪声、文件读取、工具调用和输入成本；
5. 更少 token / 更少工具调用本身不等于方案更好。

单个 B 场景失败不得直接导致“新增同义规则”。必须先分类：

```text
检索输入错误
→ 索引 / 关系错误
→ 激活入口错误
→ 陈旧 / 误导上下文
→ A/B fixture 或 runner 问题
→ 真实规则缺口
```

只有最后一种才进入新增规则候选。

## 8. C1 完成门禁

C1 只有同时满足以下条件才完成：

- 真实历史场景与控制场景具有足够辨识力；
- A 不是故意弱化的对照组；
- B 不通过派生摘要绕过源权威；
- 预期行为 / 隐藏断言与 Agent 可见输入严格分离；
- 每个场景都能说明主要测什么以及为什么；
- 已冻结 C2 可以直接实现的 A/B 输入边界和结果字段；
- 已关闭 C1 静态设计暴露的零命中静默漏规则路径；
- 没有提前执行 Agent A/B 或修改 Guide / Skill。

满足后，下一实际门禁是：

> **C2 — A/B 基线实现与静态校验**

C2 负责把本设计变成可重复运行的隔离 runner / fixture，并在真正 C3 运行前确认 A/B 载荷、隐藏答案隔离、结果 schema 和命令可执行；C1 本身不产生新方案效果结论。
