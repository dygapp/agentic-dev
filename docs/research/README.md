# Research

`docs/research/` 保存**长期可复用的技术研究资料**。本目录不是项目状态日志、里程碑执行日志或第二套 Repository Authority。

**Research 文档不是规范性权威。** 外部项目、官方资料或研究结论只有在进入相应 Method / Architecture / Guide / Engineering Discipline / Technology Profile / Skill 等当前权威后，才能改变本仓库长期行为。

## 1. 准入标准

一份材料只有满足至少一项条件，才应长期保留在本目录：

1. **独立技术价值**：离开原任务或里程碑后，仍可作为外部规范、成熟开源工程、工程实践、工具 / 平台机制或技术设计的独立参考；
2. **Authority 对应价值**：能够解释某个当前 Repository Authority 为什么这样设计，并能明确指出对应的 Authority；
3. **长期设计价值**：记录一个仍然适用、可独立复用的技术模型或设计边界，而不是某次实施的阶段状态。

日期、版本与外部证据可以保留，用于说明研究成立时的观察范围；它们不能被解释成当前项目状态。

## 2. 不进入 Research 的内容

以下材料默认不长期保留在 `docs/research/`：

- 里程碑阶段推进、当前 Gate、readiness 或恢复现场；
- 为一次实施冻结的审计基线、激活映射、重复审计或阶段分类表；
- 原型选择过程、原型验证报告、运行准备报告；
- A/B 执行过程、人工评分过程或一次 Consumer 阶段验收报告；
- 与当前 Roadmap / Issue / PR 重复维护的项目状态；
- 仅为了证明“某一步已经做过”而存在的文档。

这些信息分别由以下载体承担：

- `docs/project/*`：项目里程碑、长期项目决策与收尾记录；
- `tasks/plans/*`：复杂工作的临时协调与恢复；
- `evals/*`：可执行评估定义、fixture、机器可读结果与长期回归资产；
- Git / PR / Issue：精确历史、审查、运行与集成事实。

无需为了保留历史在 Research 下建立 archive；Git 历史已经保存被移除文件的完整版本。

## 3. 当前资料目录

### 3.1 方法与 Skill 外部研究

| 文档 | 长期价值 | 当前对应 Authority |
|---|---|---|
| `mattpocock-skills-analysis.md` | Small / Composable Skills、上下文控制、纵向切片等早期方法对照 | `docs/method/ai-development-method.md`、`docs/architecture/skill-architecture.md` |
| `spec-kit-analysis.md` | WHAT / WHY 与 HOW、规格 / 计划 / 任务边界、就绪思想 | `docs/method/ai-development-method.md` |
| `superpowers-analysis.md` | 执行编排、证据先于完成、调试与隔离执行的外部对照 | `docs/method/ai-development-method.md`、`docs/architecture/skill-architecture.md` |
| `agent-skills-specification-analysis.md` | Agent Skills 规范、包装与互操作边界 | `docs/architecture/skill-architecture.md`、`docs/architecture/skill-contracts.md` |
| `andrej-karpathy-skills-analysis.md` | 最小实现、推测性复杂度、精准修改、包装实践 | `docs/architecture/engineering-disciplines.md`、`docs/architecture/skill-contracts.md` |

### 3.2 工程纪律、平台与技术画像研究

| 文档 | 长期价值 | 当前对应 Authority |
|---|---|---|
| `implementation-minimality-and-speculative-complexity-analysis.md` | 实现最小化与推测性复杂度的外部 / 工程证据 | `docs/architecture/engineering-disciplines.md` |
| `surgical-change-and-diff-scope-control-analysis.md` | 精准修改与差异范围控制 | `docs/architecture/engineering-disciplines.md` |
| `data-access-scope-boundedness-analysis.md` | 数据访问作用域、有界性、生命周期与分页 / 窗口判断 | `docs/architecture/engineering-disciplines.md` |
| `vue3-typescript-profile-analysis.md` | Vue 3 + TypeScript 官方资料、规则候选与专项验证依据 | `docs/technology-profiles/vue3-typescript.md`、`docs/architecture/technology-profile-contract.md` |
| `github-stacked-pr-squash-topology.md` | GitHub stacked PR / squash merge 的平台语义与拓扑风险 | `docs/guides/external-operation-guidelines.md` |

### 3.3 知识激活与检索研究

| 文档 | 长期价值 | 当前对应 Authority |
|---|---|---|
| `knowledge-activation-and-code-intelligence-analysis.md` | 规则激活、知识发现、CodeGraph / Obsidian 边界、代码智能与后继能力分层 | `docs/guides/rule-activation-guide.md`、`docs/architecture/engineering-capability-architecture.md`、`docs/architecture/skill-architecture.md` |
| `knowledge-activation-evidence-appendix.md` | 上述研究所依赖的外部实现证据、数值与仓库反例 | `docs/guides/rule-activation-guide.md`；仅作为技术证据伴随文档 |
| `llm-wiki-rule-governance-fit-analysis.md` | LLM Wiki 思路与当前规则治理的适配 / 不适配边界 | `docs/guides/rule-activation-guide.md` |
| `rule-retrieval-design-reference.md` | 稀疏规则查询、源指针、fail-closed、派生索引与最小正确规则集设计 | `docs/guides/rule-activation-guide.md`；实现映射到 `evals/rule-retrieval/*` |

## 4. 使用规则

- 当前项目事实先读 `AGENTS.md` 与 `docs/project/project-roadmap.md`，不要从 Research 恢复项目状态；
- 当前任务规则先读相应 Repository Authority，Research 只在需要理解设计依据、外部机制或技术取舍时按需读取；
- Research 与当前 Authority 冲突时，以 Authority 为准；
- 外部资料发生变化时，可以更新 Research，但不会自动改变 Authority；
- 如果 Research 中形成新的长期规则，必须另行进入相应 Authority 并完成对应验证，不能让 Research 自行升格。
