# 规则治理与知识激活 v1 — 协调计划

## 目标

在不继续机械增加指南、技能、技术画像或运行时层的前提下，完成当前规则体系的激活审计、最小检索模型、历史场景专项评估、必要权威收敛和使用方新上下文验证，使 Agent 能在具体任务中以更小活动上下文可靠取得正确规则。

## 权威 / 输入

开始或恢复本计划时按当前 GitHub 状态重新核验，并读取：

1. `AGENTS.md`；
2. `docs/project/project-roadmap.md`；
3. Issue #73；
4. `docs/project/rule-governance-knowledge-activation-v1.md`；
5. `docs/research/knowledge-activation-and-code-intelligence-analysis.md`；
6. `docs/research/knowledge-activation-evidence-appendix.md`；
7. `docs/research/rule-activation-audit-baseline.md`；
8. `docs/research/using-agentic-dev-activation-map.md`；
9. `docs/research/external-operation-guidelines-activation-map.md`；
10. `docs/research/cross-authority-duplication-audit.md`；
11. `docs/research/activation-failure-classification.md`；
12. `docs/research/minimal-rule-retrieval-contract.md`；
13. `docs/research/rule-retrieval-prototype-selection.md`；
14. `docs/research/rule-retrieval-prototype-validation.md`；
15. `docs/research/rule-retrieval-targeted-evaluation-design.md`；
16. `docs/research/rule-retrieval-ab-baseline-validation.md`；
17. `docs/guides/using-agentic-dev.md`；
18. `docs/guides/external-operation-guidelines.md`；
19. 按当前工作需要读取 `skill-architecture.md`、`skill-contracts.md`、工程纪律、历史治理评估与使用方证据；
20. 开放 PR / Issue 和当前 `master`，确认没有晚于本计划的人工路线决定或集成事实。

本计划只负责协调，不复制上述长期权威的完整规则。

## 启动状态

人工决策日期：2026-09-08

启动基线：

`master@0895ca30f76c666f3a0d4d9c2f9af6f14cded5d6`

活动里程碑：

**规则治理与知识激活 v1**

跟踪入口：Issue #73

阶段执行分支 / PR 不作为长期恢复事实写死在本计划中；恢复时以 GitHub 当前开放 PR、分支和 `master` 为准。

当前门禁：

> **阶段 C — 检索 / 激活评估 / C3 — 隔离运行时与人工评分**

## 范围

本计划负责：

- 高影响指南规则激活单元审计；
- 常驻 / 任务 / 条件上下文分层候选；
- 规则重复 / 冲突 / 取代检查；
- 最小检索模型；
- 检索 / 激活定向评估；
- 必要权威 / 指南 / 激活指针收敛；
- 使用方新上下文验证；
- 最终 AI 复核与集成前状态闭环。

## 非目标

- 不实现 `code-review` 技能；
- 不启动 WI-06；
- 不启动 WI-07；
- 不启动 WI-09；
- 不新增第四工程纪律；
- 不强制采用 Obsidian；
- 不强制采用 CodeGraph；
- 不预先建立规则图数据库、MCP、Marketplace、Plugin Bundle；
- 不把大指南机械按文件大小拆分；
- 不把现有规则复制到多个技能 / 指南中；
- 不把本计划写成完整会话记录。

## 工作项与顺序

### A1 — 建立审计基线

- [x] 重新确认 `master`、开放 PR / Issue 与当前活动里程碑；
- [x] 确认 `using-agentic-dev.md`、`external-operation-guidelines.md` 当前精确 blob / commit 身份；
- [x] 枚举当前 AGENTS / README / 技能 / 指南 / 项目入口中与两份指南重复或交叉的高影响规则；
- [x] 冻结历史失效场景候选清单。

输出：`docs/research/rule-activation-audit-baseline.md`。

### A2 — `using-agentic-dev.md` 激活映射

- [x] 按语义而不是标题机械切分规则激活单元；
- [x] 对每个单元记录触发条件 / 消费者 / 强度 / 权威指针；
- [x] 标记常驻核心规则候选；
- [x] 标记只在新项目 / 既有使用方 / 新上下文 / 项目路线图 / 集成 / 验证等条件下需要的单元；
- [x] 标记重复 / 重叠 / 陈旧 / 已取代候选；
- [x] 关联已知使用方 / PR / 评估证据。

输出：`docs/research/using-agentic-dev-activation-map.md`。

### A3 — `external-operation-guidelines.md` 激活映射

- [x] 同 A2；
- [x] 特别区分普通写操作、跨仓库、人工介入、异步闭环、媒体资源、共享资源 / 租约、证据晋升、PR 拓扑等独立条件；
- [x] 检查是否存在“任何外部操作都要加载整份指南”的隐式入口。

输出：`docs/research/external-operation-guidelines-activation-map.md`。

### A4 — 跨权威重复审计

- [x] 比较 AGENTS / README / 指南 / 技能 / 项目规则；
- [x] 区分合理摘要 / 指针与实质重复权威；
- [x] 标记同义但不同强度的规则；
- [x] 标记可能导致冲突选择的规则；
- [x] 不在本步骤立即删除规则。

输出：`docs/research/cross-authority-duplication-audit.md`。

### A5 — 激活失效分类证据

对历史场景逐项分类：

- [x] 发现 / 激活失败；
- [x] 选择 / 冲突失败；
- [x] 指令密度问题；
- [x] 误导 / 陈旧上下文；
- [x] 真实规则缺口。

至少覆盖：

- [x] 项目路线图 / 里程碑集成后状态闭环；
- [x] 规划候选 / 执行单元身份边界；
- [x] 验证触发 / 就绪重新进入；
- [x] 外部异步操作闭环；
- [x] 使用方新上下文权威发现。

输出：`docs/research/activation-failure-classification.md`。

阶段 A 完成结论：六个历史场景中既存在纯激活失败，也存在当时真实的使用层 / 平台专项规则缺口；这些历史缺口已经由当前仓库权威关闭。当前下一问题应优先验证检索、激活、范围选择、陈旧上下文和重复噪声，而不是继续新增同义规则。

---

### B1 — 冻结最小检索契约

- [x] 定义最小输入：任务 / 风险 / 产物 / 阶段中哪些字段确有辨识力；
- [x] 定义最小输出：权威指针 + 激活规则 + 必需检查；
- [x] 定义回退：无索引 / 索引陈旧时回退仓库直接读取；
- [x] 定义重复 / 取代最小语义；
- [x] 避免建立无法由当前证据证明必要的复杂结构。

输出：`docs/research/minimal-rule-retrieval-contract.md`。

B1 结论：采用稀疏查询契约——`scope + responsibility` 为必需输入，`stage / subject / conditions` 按适用性补充；结果只返回可追溯源权威的短激活摘要、适用信息、必需检查和匹配解释。条目角色只区分 authority / pointer / consumer / evidence，跨条目关系只冻结 equivalent / scope-variant / superseded-by。索引缺失、来源陈旧、范围冲突或高影响授权不确定时直接回退当前仓库权威。当前没有证据要求全库统一增加文件头或采用特定索引技术。

### B2 — 原型选择

- [x] 选择可从仓库权威重建的最小实现；
- [x] 确认能精确回指来源 / 段落；
- [x] 确认能检测来源漂移；
- [x] 确认能支持 B3 与阶段 C 评估；
- [x] 确认不需要先引入新运行时层或第三方依赖。

输出：`docs/research/rule-retrieval-prototype-selection.md`。

B2 结论：选择 **JSON 派生规则索引 + Python 标准库薄查询器**。原型拟位于 `evals/rule-retrieval/rule-index.json` 与 `evals/query_rule_index.py`，首轮只覆盖阶段 A 已审计的高影响规则面。该选择复用仓库既有 JSON + Python 标准库评估模式，不建立全仓库规则数据库，不引入 YAML 解析依赖、图数据库、MCP、服务或统一文件头；真正长期实现仍由 B3 / C / D 证据决定。

### B3 — 原型验证

- [x] 对阶段 A 的规则单元建立最小索引；
- [x] 手工检查查询结果；
- [x] 确认删除索引不损失任何长期事实；
- [x] 确认同一规则没有复制成第二权威。

输出：`docs/research/rule-retrieval-prototype-validation.md`、`evals/rule-retrieval/rule-index.json`、`evals/query_rule_index.py`。

B3 结论：首轮派生索引包含 61 个条目 / 8 个唯一规范性来源；查询器支持 B1 稀疏维度、来源身份校验、未知维度显式回退和 `superseded-by` 算法边界，不使用固定 Top-K，也不把索引或 Research 提升为规则权威。当前只证明原型具备进入阶段 C 评估设计的基础能力，不证明按需检索已经优于粗粒度加载。

---

### C1 — 定向评估设计

- [x] 设计能验证正确召回必要规则的真实历史场景；
- [x] 设计能观察整份指南噪声与条件化激活差异的场景；
- [x] 设计条件未触发时不误激活的负向控制；
- [x] 设计来源陈旧时安全回退的控制；
- [x] 设计真实规则缺口不能被近似规则伪装的控制；
- [x] 冻结强 A 组文件级粗粒度基线与 B 组查询 / 回退边界；
- [x] 冻结隐藏断言、预期键 / 回退与 Agent 可见输入隔离；
- [x] 冻结人工语义评分与可取得成本指标。

输出：

- `docs/research/rule-retrieval-targeted-evaluation-design.md`
- `evals/rule-retrieval/targeted-evaluation-design.json`

C1 结论：冻结 6 个真实历史场景 + 3 个控制场景。A 组只加载当前职责真正相关的整份规范性文档，不人为弱化；B 组使用首轮派生索引，只有直接命中时才按源指针读取，stale / unknown / no-match 均安全回退当前仓库权威。C1 静态设计还发现“查询词均已建模但零命中时静默返回空集”的原型缺口，已通过 `no_indexed_rule_match` 最小修正关闭；没有新增规则、没有扩索引、没有修改 Guide / Skill，也没有执行真实 A/B。

### C2 — A/B 基线实现与静态校验

- [x] 实现可重复的 A / B 隔离 runner；
- [x] 实现 Consumer-local Authority 最小 fixture；
- [x] 实现无语义来源漂移 fixture；
- [x] 确保运行时不复制 `expected_behavior` / assertions / expected keys，也不暴露 A/B 分组或 `metric_focus`；
- [x] 固定结果 schema，区分进程退出、查询回退与人工语义评分；
- [x] 静态固定同一任务正文、runner、进程环境与外部权限边界，并明确实际模型 / reasoning effort 必须由 C3 运行证据证明一致；
- [x] 验证 9 个场景的 A 载荷和 B query 可以生成；
- [x] 真实执行 runner 静态验证命令，且未在本步骤提前形成 C3 的运行时效果结论。

输出：

- `docs/research/rule-retrieval-ab-baseline-validation.md`
- `evals/rule-retrieval/README.md`
- `evals/rule-retrieval/result-schema.json`
- `evals/run_rule_retrieval_ab.py`
- `evals/rule-retrieval/fixtures/consumer-local-authority/`

C2 结论：A/B 基线已经可重复装配。最终差异复核曾发现 stale-source 场景虽然触发 fallback，却仍可能把临时陈旧副本作为 fallback 上下文消费；该缺口已修正为 fallback 后重新从当前 Repository Authority 装配，并增加工作区与当前 Authority / fixture 的字节一致性静态断言。修正后的只读 GitHub Actions Run `34296395675` / Job `102293842203` 在 Head `96eb5f356383bfb54ec5bd99e76f48f74d7ec01c` 上实际执行 Python 编译检查和 `python3 evals/run_rule_retrieval_ab.py --validate-only` 并成功，9 个场景均通过静态装配校验，隐藏答案与 A/B 分组没有进入运行时输入，且明确未执行 Agent A/B。此前 Run `34291536760` 与 `34296037510` 仅保留为祖先验证 / 诊断证据，不作为最终 C2 PASS。临时 workflow 在取证后删除。当前仓库没有足以由 runner 自动证明实际模型 / 推理强度的统一配置契约，因此 C3 只有在两侧真实运行证据能证明模型与推理强度一致时，才允许把该配对纳入效果比较。

比较基线：

```text
A：当前职责相关整份规范性文档的文件级粗粒度加载
B：薄入口 + 任务 / 风险条件检索 + 安全回退
```

记录可取得指标：

- 规则召回或回退正确性；
- 上下文噪声 / 精确度；
- 输入上下文；
- 文件 / 工具读取；
- 语义断言；
- 误停 / 误升级 / 误执行；
- 是否发生权威混淆。

### C3 — 隔离运行时与人工评分

- [ ] 使用新上下文 / 隔离环境；
- [ ] 隐藏预期行为 / 断言；
- [ ] 进程退出码与语义通过分离；
- [ ] 证明参与比较的 A/B 配对实际模型与推理强度一致；
- [ ] 人工按断言评分；
- [ ] 对失败场景先判断激活 / 检索 / 规则缺口类型再修订。

阶段 C 完成条件：存在足够证据判断新激活模式是否优于当前粗粒度加载。

---

### D1 — 基于证据实施指南 / 权威收敛

只实施阶段 C 证明有价值的动作，例如：

- [ ] 缩减常驻内容；
- [ ] 增加段落级指针；
- [ ] 拆出真正独立激活单元；
- [ ] 合并重复规则；
- [ ] 删除陈旧 / 已取代规则；
- [ ] 修正技能激活指针；
- [ ] 固化最小规则元数据 / 派生索引；
- [ ] 定义规则删除 / 取代生命周期。

禁止无证据全量重构。

### D2 — 回归

- [ ] 原有治理评估不回退；
- [ ] 新检索评估继续通过；
- [ ] 新上下文不需要读取整个历史；
- [ ] 当前正式术语与中文规则不回退。

---

### E1 — 使用方新上下文验证

选择真实使用方，重新读取其仓库权威，验证：

- [ ] 使用方仓库权威始终优先；
- [ ] 能取得当前任务最小 `agentic-dev` 规则集；
- [ ] 不机械读取全部指南；
- [ ] 不把 `agentic-dev` 项目级规则带入使用方；
- [ ] 关键规则没有因缩减上下文丢失。

### E2 — 使用方 CodeGraph 可选 A/B

这不是本里程碑完成的强制依赖；如果当前使用方环境适合，可以并行收集：

- [ ] 传统 `Read` / `Grep` / `Find`；
- [ ] Local Codex + CodeGraph；

在代码入口发现、调用路径、影响范围、调试 / 复核上比较效率和正确性。

任何结果只作为使用方代码智能采用证据，不把 CodeGraph 直接固化为核心方法强依赖。

---

### F1 — 最终验证

- [ ] 静态文件 / 结构 / 链接检查；
- [ ] 必要定向评估；
- [ ] 历史直接回归；
- [ ] 使用方验证证据；
- [ ] 人工语义评分完成。

### F2 — 最终 AI 复核

- [ ] 重新读取当前目标基线 / PR / 差异；
- [ ] 检查权威一致性；
- [ ] 检查是否制造新超级指南 / 技能 / 索引权威；
- [ ] 检查是否发生未授权 WI-06 / WI-07 / WI-09 范围扩张；
- [ ] 未解决阻塞 / 中等级问题必须为 `0 / 0`。

### F3 — 集成状态闭环

- [ ] 项目路线图；
- [ ] AGENTS；
- [ ] README；
- [ ] 本里程碑项目记录；
- [ ] Issue #73；
- [ ] 本计划；

全部形成拟集成后的自洽状态，再进入人工集成决策。

## 后继计划门禁：WI-07 — 代码复核能力 v1

本计划完成不自动启动 WI-07。

只有规则治理与知识激活 v1 已完成并集成后，新的上下文才可以基于项目路线图决定是否正式启动代码复核能力 v1。

未来代码复核规划必须继承以下已冻结边界：

1. 独立高信噪比复核职责；
2. 非通用方法新阶段；
3. 非超级技能；
4. 与规划复核分离；
5. 默认检查规格符合性、真实缺陷 / 回归、数据 / 状态 / 生命周期、边界 / 依赖 / 副作用、复杂度、差异范围、验证证据；
6. 技术规则按风险激活，不创建按技术名称的复核技能；
7. CodeGraph 等代码智能只能是可选结构发现辅助；
8. 无 CodeGraph 时必须可回退；
9. WI-06 是否启动由代码复核 / 使用方评估暴露的真实技术知识缺口决定。

## 当前下一步

阶段 A 与阶段 B 已完成；阶段 C 的 C1、C2 已完成，当前进入：

> **阶段 C — 检索 / 激活评估 / C3 — 隔离运行时与人工评分**

C3 执行 C1 冻结的真实新上下文 A/B，必须保持隐藏断言、记录实际模型 / 推理强度证据并由人工逐项评分；在 C3 证据形成前，不修改 Guide / Skill，不宣称 B 优于 A，也不进入阶段 D。

后续新上下文不得从聊天记忆恢复本轮讨论，应从 GitHub 当前状态和本计划列出的权威 / 研究入口重新开始。