from pathlib import Path
import json
import re
import subprocess


def replace_section(path, start, end, body):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    pattern = re.escape(start) + r".*?(?=" + re.escape(end) + r")"
    new = start + "\n\n" + body.rstrip() + "\n\n"
    out, count = re.subn(pattern, new, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{path}: expected one section {start!r}, got {count}")
    p.write_text(out, encoding="utf-8")


agents_body = """当前长期阶段是：

> **工程能力扩展与方法演进**

最近完成并已集成的有限里程碑是：

> **规则治理与知识激活 v1**

该里程碑已通过 PR #89 集成；Issue #73 已按完成关闭。精确里程碑历史、验证结果与集成事实由 Project Roadmap、项目记录、Git / PR / Issue 和 `evals/` 保存。

当前路线状态是：

> **待人工决策**

当前没有活动有限里程碑。WI-07 — 代码复核能力 v1 是优先后继候选，但尚未启动；WI-06、WI-09、第四工程纪律和 Issue #71 候选实施同样未启动。候选优先级不能替代新的人工里程碑决策。

`docs/research/` 只保留离开原实施阶段后仍具有独立技术参考价值的资料，或能够明确解释 / 支撑当前 Repository Authority 的技术资料。阶段审计、冻结基线、readiness、原型验证、A/B 执行报告和使用方阶段验收等过程证据不作为常驻 Research；需要追溯时从 `docs/project/*`、`tasks/plans/*`、`evals/*`、Git、PR 或 Issue 取得。

当前项目状态与恢复顺序以 `docs/project/project-roadmap.md` 为准。只有当前任务确实需要时，再按渐进式披露读取：

- `docs/guides/rule-activation-guide.md`；
- `docs/project/rule-governance-knowledge-activation-v1.md`（已完成里程碑记录）；
- `docs/research/README.md`；
- `docs/research/knowledge-activation-and-code-intelligence-analysis.md`；
- `docs/research/knowledge-activation-evidence-appendix.md`；
- `docs/research/llm-wiki-rule-governance-fit-analysis.md`；
- `docs/research/rule-retrieval-design-reference.md`。

Issue #58 继续作为长期使用方经验反馈入口；Issue #71 继续作为独立高风险规划复核 / 模型路由相关研究输入，不与未来代码复核自动合并。

工程能力的分层、证据进入方式和能力生命周期统一记录在 `docs/architecture/engineering-capability-architecture.md`。不得因为当前处于待人工决策状态，就机械增加技能、超级技能、技术画像或流程层级。"""
replace_section("AGENTS.md", "## 当前阶段", "## 核心规则", agents_body)

readme_body = """- **基线版本：** v0.1
- **长期阶段：** 工程能力扩展与方法演进
- **最近完成并已集成的有限里程碑：** 规则治理与知识激活 v1
- **当前路线状态：** 待人工决策
- **下一有限里程碑：** 尚未选择

当前没有活动有限里程碑。WI-07 — 代码复核能力 v1 仍是优先后继候选，但未启动；其他候选也不会因当前维护工作自动进入实施。

当前路线、已完成里程碑、候选库与 Fresh Context 恢复顺序只在以下入口维护详细状态：

`docs/project/project-roadmap.md`

Issue #73、PR #89 以及规则治理 v1 的阶段计划属于已完成里程碑的历史证据，不再是普通 Fresh Context 的当前工作入口。需要研究技术依据时，从 `docs/research/README.md` 选择与当前 Authority 或技术问题直接相关的材料，而不是恢复已关闭里程碑的完整过程文档。"""
replace_section("README.md", "## 当前状态", "## 仓库事实与权威", readme_body)

research_readme = """# Research

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

| 文档 | 长期价值 | 当前对应关系 |
|---|---|---|
| `mattpocock-skills-analysis.md` | Small / Composable Skills、上下文控制、纵向切片等早期方法对照 | `docs/method/*`、`docs/architecture/skill-architecture.md` |
| `spec-kit-analysis.md` | WHAT / WHY 与 HOW、规格 / 计划 / 任务边界、就绪思想 | `docs/method/ai-development-method.md` |
| `superpowers-analysis.md` | 执行编排、证据先于完成、调试与隔离执行的外部对照 | Method 与现有核心 Skills |
| `agent-skills-specification-analysis.md` | Agent Skills 规范、包装与互操作边界 | `docs/architecture/skill-architecture.md`、`skill-contracts.md` |
| `andrej-karpathy-skills-analysis.md` | 最小实现、推测性复杂度、精准修改、包装实践 | `docs/architecture/engineering-disciplines.md` 与 Skill Packaging 边界 |

### 3.2 工程纪律、平台与技术画像研究

| 文档 | 长期价值 | 当前对应关系 |
|---|---|---|
| `implementation-minimality-and-speculative-complexity-analysis.md` | 实现最小化与推测性复杂度的外部 / 工程证据 | `docs/architecture/engineering-disciplines.md` |
| `surgical-change-and-diff-scope-control-analysis.md` | 精准修改与差异范围控制 | `docs/architecture/engineering-disciplines.md` |
| `data-access-scope-boundedness-analysis.md` | 数据访问作用域、有界性、生命周期与分页 / 窗口判断 | `docs/architecture/engineering-disciplines.md` |
| `vue3-typescript-profile-analysis.md` | Vue 3 + TypeScript 官方资料、规则候选与专项验证依据 | `docs/technology-profiles/vue3-typescript.md`、Technology Profile Contract |
| `github-stacked-pr-squash-topology.md` | GitHub stacked PR / squash merge 的平台语义与拓扑风险 | `docs/guides/external-operation-guidelines.md` |

### 3.3 知识激活与检索研究

| 文档 | 长期价值 | 当前对应关系 |
|---|---|---|
| `knowledge-activation-and-code-intelligence-analysis.md` | 规则激活、知识发现、CodeGraph / Obsidian 边界、代码智能与后继能力分层 | `docs/guides/rule-activation-guide.md`、Engineering Capability / Skill Architecture |
| `knowledge-activation-evidence-appendix.md` | 上述研究所依赖的外部实现证据、数值与仓库反例 | 同上；仅作为技术证据伴随文档 |
| `llm-wiki-rule-governance-fit-analysis.md` | LLM Wiki 思路与当前规则治理的适配 / 不适配边界 | `docs/guides/rule-activation-guide.md` |
| `rule-retrieval-design-reference.md` | 稀疏规则查询、源指针、fail-closed、派生索引与最小正确规则集设计 | `docs/guides/rule-activation-guide.md`；实现映射到 `evals/rule-retrieval/*` |

## 4. 使用规则

- 当前项目事实先读 `AGENTS.md` 与 `docs/project/project-roadmap.md`，不要从 Research 恢复项目状态；
- 当前任务规则先读相应 Repository Authority，Research 只在需要理解设计依据、外部机制或技术取舍时按需读取；
- Research 与当前 Authority 冲突时，以 Authority 为准；
- 外部资料发生变化时，可以更新 Research，但不会自动改变 Authority；
- 如果 Research 中形成新的长期规则，必须另行进入相应 Authority 并完成对应验证，不能让 Research 自行升格。
"""
Path("docs/research/README.md").write_text(research_readme, encoding="utf-8")

retrieval_ref = """# 规则检索设计参考

本文记录 `agentic-dev` 已验证过的**规则发现 / 激活技术设计**。它用于解释当前规则激活导航和 `evals/rule-retrieval/*` 原型背后的设计边界，不是 Repository Authority，也不定义当前项目状态。

当前规范性激活入口：`docs/guides/rule-activation-guide.md`。

当前可执行评估实现：

- `evals/rule-retrieval/rule-index.json`
- `evals/query_rule_index.py`
- `evals/run_rule_retrieval_ab.py`
- `evals/rule-retrieval/README.md`

历史里程碑与验证事实：`docs/project/rule-governance-knowledge-activation-v1.md`、Git / PR #74～#89 / Issue #73。

## 1. 设计目标

规则检索层只解决一个问题：**根据当前任务职责和已知风险，找到足以正确执行当前任务、又不引入大量无关上下文的最小规则入口。**

它必须可回到当前规范性来源、不复制第二份规则权威、保留项目 / 仓库作用域、来源陈旧或判断不可靠时安全回退、查询和选择过程可解释，并且派生数据可删除、可重建。

## 2. 稀疏查询模型

最小查询使用两个必需语义维度：

```text
作用域 + 当前职责
```

只有规则集合会因此改变时，才增加：

```text
+ 当前阶段
+ 目标对象
+ 风险 / 状态条件
```

这些维度是逻辑输入，不要求用户填写固定表单。未知条件不得为了“命中更多规则”而猜测。

## 3. 作用域必须保真

跨仓库工作至少需要区分当前项目事实由哪个仓库权威主导、当前职责正在读取或改变哪个仓库 / 外部对象，以及其他仓库究竟是只读方法来源、使用方事实来源还是具有明确写入授权。

这可以避免把 `agentic-dev` 自身项目规则误带入 Consumer，也避免把对一个仓库的授权扩张为跨仓库授权。

## 4. 一个查询只描述一个当前职责

职责从执行切换到验证、从验证切换到集成复核，或从普通开发进入显式 baseline upgrade 时，应重新解析规则入口。第一次得到的规则集不能被当成整个会话永久上下文。

## 5. 最小正确规则集

“最小”不是固定条数、最低令牌数或最少文件数，而是：**没有遗漏任何当前必需规则，同时不装入当前职责不需要的规则。** 因此不能使用固定 Top-K 代替完整召回当前适用的必需规则。

通常应纳入当前作用域和职责成立的核心不变量、触发条件已经由事实满足的条件必需规则，以及当前职责独立执行需要的最小 Skill / 平台专项守卫。默认排除触发条件未满足的条件规则、其他项目作用域规则、纯历史证据、已被当前 Authority 取代的旧规则，以及当前职责无关的相邻指南段落。

## 6. 最小输出

每个活动结果至少应能表达：

- `source_pointer`：仓库路径、可定位章节 / 独立职责载体，以及用于陈旧检测的来源身份；
- `activation_summary`：明显短于源规则的“为什么当前任务需要它、它约束什么”；
- `applicability`：匹配的作用域、职责和已满足条件；
- `required_checks`：当前执行 / 验证必须检查的最小事项；
- 选择解释：为什么命中这些规则，以及哪些条件导致其他规则未激活或触发回退。

摘要不能脱离源指针成为长期权威。

## 7. 条目角色与关系

当前评估实现只需要三类条目角色：`authority`、`pointer`、`consumer`。评估证据本身留在 `evals/`、Project / PR / Issue，不作为当前规则索引条目角色。

当前最小关系是 `equivalent`、`scope-variant`、`superseded-by`。关系只帮助选择和解释，不能改变 Repository Authority 顺序。

## 8. Fail-closed

出现规范性来源缺失、来源 identity 已变化、源指针无法精确解析、必需查询维度 / 值未知、查询无命中但仍存在治理风险、作用域冲突，或高影响授权 / 架构 / 安全 / 隐私 / 不可逆边界无法可靠判断时，不应继续用派生摘要声称规则召回完整。

回退路径：

```text
停止依赖当前派生检索结果
→ 读取当前 Repository Authority
→ 按当前职责读取完整相关 Guide / Skill
→ 重新判断
```

“不命中”不能被解释为“没有规则”。

## 9. 当前派生实现为何保持简单

当前评估原型使用 `JSON 派生规则索引 + Python 标准库薄查询器`。JSON 足以表达稀疏条件、源身份和最小关系，Python 标准库足以完成确定性过滤、来源校验和机器可读输出；无需数据库、第三方检索包、MCP 服务或全仓库统一 Front Matter。

原型可以整体删除 / 重建，不损失任何规范性事实。这只是当前已经证明足够的评估载体，不构成未来必须永久使用 JSON / Python 的架构承诺。

## 10. 当前实现映射

| 技术职责 | 当前实现 |
|---|---|
| 派生规则条目与源 identity | `evals/rule-retrieval/rule-index.json` |
| 查询、过滤、来源陈旧检查 | `evals/query_rule_index.py` |
| A/B 工作区与静态回归 | `evals/run_rule_retrieval_ab.py` |
| 可执行说明 / fixture / 结果结构 | `evals/rule-retrieval/README.md` 及同目录资产 |

这些实现属于 Evaluation Asset，不属于 Authority。

## 11. 已取得的验证信号

历史隔离 A/B 中，9 / 9 pair 可比较；按需检索组的直接命中场景召回冻结的 29 / 29 必需规则，3 / 3 安全回退 reason 正确，按需检索组行为语义 9 / 9 PASS，完整相关文档组为 8 / 9。直接命中场景观察到的命令输出字节约下降 48.6%，wall-clock 约下降 49.8%；fallback 成本更高，但 stale / unknown / no-match 的安全回退均正确，因此不能为了成本删除 fail-closed。

机器可读评分结果保存在 `evals/rule-retrieval/c3-human-scoring.json`。这些结果证明当前设计值得作为长期技术参考，但不证明所有仓库、模型或任务都能获得相同比例收益。

## 12. 维护边界

派生索引保存规范性源 identity。任一活动来源变化时，旧索引必须先视为陈旧；只有核对相关源规则语义后，才能按当前源重新生成 identity。

不得通过关闭来源校验、继续使用旧摘要、把派生索引提升为事实来源，或只因为新 blob 看起来是状态修改就自动信任旧索引来“修复”陈旧。

如果未来出现新检索技术，只要仍满足“当前 Authority 单点定义、派生层可重建、陈旧可检测、失败时安全回退”，就可以替换当前评估载体，而不需要改变本设计的核心边界。
"""
Path("docs/research/rule-retrieval-design-reference.md").write_text(retrieval_ref, encoding="utf-8")

p = Path("docs/research/knowledge-activation-evidence-appendix.md")
text = p.read_text(encoding="utf-8")
old = """# 知识激活关键证据附录

研究日期：2026-09-08

研究性质：**研究证据附录**

本文是 `knowledge-activation-and-code-intelligence-analysis.md` 的证据附录，专门保存后续新上下文最容易遗漏的数值、具体反例、外部项目实测和当前架构身份。本文不是规范性权威，不单独改变方法、指南、技能、工程纪律或技术画像。
"""
new = """# 知识激活关键证据附录

研究日期：2026-09-08

研究性质：**长期技术证据伴随资料**

本文是 `knowledge-activation-and-code-intelligence-analysis.md` 的技术证据附录，保存该研究所依赖的数值、具体仓库反例、外部项目实测和架构身份边界。它用于解释 `docs/guides/rule-activation-guide.md` 及相关工程能力设计为什么采用薄入口、按需激活、派生索引与 fail-closed 等边界。

本文不是规范性权威，也不是项目状态 / Fresh Context 恢复入口；当前项目状态以 `AGENTS.md` 与 Project Roadmap 为准，当前规则以相应 Repository Authority 为准。
"""
if old not in text:
    raise SystemExit("evidence appendix intro not found")
p.write_text(text.replace(old, new, 1), encoding="utf-8")

p = Path("docs/project/project-roadmap.md")
text = p.read_text(encoding="utf-8")
start = "当前没有新的里程碑实施门禁。规则治理与知识激活 v1 已完成并集成，路线已经进入下一有限里程碑人工决策；WI-07 仍只是优先候选，不自动启动。完整研究和实施边界分别位于："
i = text.find(start)
if i < 0:
    raise SystemExit("roadmap top research list start not found")
ls = i + len(start)
le_marker = "\n\nWI-06、WI-07、WI-09、第四工程纪律和 Issue #71"
le = text.find(le_marker, ls)
if le < 0:
    raise SystemExit("roadmap top research list end not found")
durable = """

- `docs/research/knowledge-activation-and-code-intelligence-analysis.md`
- `docs/research/knowledge-activation-evidence-appendix.md`
- `docs/research/llm-wiki-rule-governance-fit-analysis.md`
- `docs/research/rule-retrieval-design-reference.md`
- `docs/project/rule-governance-knowledge-activation-v1.md`
- `evals/rule-retrieval/README.md`
- `tasks/plans/20260908/01-rule-governance-knowledge-activation.md`"""
text = text[:ls] + durable + text[le:]
bs = text.find("研究记录：\n\n- `docs/research/knowledge-activation-and-code-intelligence-analysis.md`")
be_marker = "\n\n协调计划：\n\n`tasks/plans/20260908/01-rule-governance-knowledge-activation.md`"
be = text.find(be_marker, bs)
if bs < 0 or be < 0:
    raise SystemExit("roadmap section 4.8 research block missing")
replacement = """研究 / 技术依据：

- `docs/research/knowledge-activation-and-code-intelligence-analysis.md`
- `docs/research/knowledge-activation-evidence-appendix.md`
- `docs/research/llm-wiki-rule-governance-fit-analysis.md`
- `docs/research/rule-retrieval-design-reference.md`
- `evals/rule-retrieval/README.md`

阶段审计、激活映射、原型验证、A/B 运行结果与 E1 Consumer 验证等过程 Research 已在 2026-09-09 的 Research 信息架构维护中从当前树移除；历史仍由 Git、PR #74～#89、Issue #73、本节项目记录与 `evals/` 保存。该维护不构成新的有限里程碑，也不启动 WI-07。"""
text = text[:bs] + replacement + text[be:]
p.write_text(text, encoding="utf-8")

p = Path("docs/project/rule-governance-knowledge-activation-v1.md")
text = p.read_text(encoding="utf-8")
text = text.replace("**有限里程碑实施与验证已收敛；精确集成事实由 GitHub 原生状态记录**", "**已完成并集成**", 1)
anchor = "`master@0895ca30f76c666f3a0d4d9c2f9af6f14cded5d6`\n"
if anchor not in text:
    raise SystemExit("project record baseline anchor missing")
text = text.replace(anchor, anchor + "\n集成结果：PR #89 已通过 squash merge 集成；Issue #73 已按完成关闭。\n", 1)
s = text.find("### 4.1 仓库内证据")
e = text.find("### 4.2 外部研究", s)
if s < 0 or e < 0:
    raise SystemExit("project record section 4.1 missing")
sec41 = """### 4.1 仓库内与长期技术输入

当前树长期保留的主要技术输入：

- `AGENTS.md`；
- `docs/guides/rule-activation-guide.md`；
- `docs/guides/using-agentic-dev.md`；
- `docs/guides/external-operation-guidelines.md`；
- `docs/architecture/skill-architecture.md`；
- `docs/architecture/skill-contracts.md`；
- `docs/research/knowledge-activation-and-code-intelligence-analysis.md`；
- `docs/research/knowledge-activation-evidence-appendix.md`；
- `docs/research/llm-wiki-rule-governance-fit-analysis.md`；
- `docs/research/rule-retrieval-design-reference.md`；
- `evals/rule-retrieval/*`。

阶段 A～E 的审计、基线冻结、原型选择 / 验证和运行结果 Markdown 属于里程碑过程证据；2026-09-09 起不再作为当前 Research 文档。精确历史由 Git、PR #74～#89、Issue #73、本项目记录和 `evals/` 承接。

"""
text = text[:s] + sec41 + text[e:]
pat = r"阶段 A 研究入口：\n\n(?:- `docs/research/[^\n]+`\n)+\n"
repl = "阶段 A 的五份审计 / 激活映射过程文档已在 2026-09-09 Research 信息架构维护中从当前树移除。需要复核阶段 A 原始材料时，从 PR #75～#79、Issue #73 或 Git 历史恢复；长期技术结论已由当前 Guide、Project Record 与规则检索设计参考承接。\n\n"
text, n = re.subn(pat, repl, text, count=1)
if n != 1:
    raise SystemExit(f"stage A list replacement count={n}")
repls = [
    ("B1 研究基线：\n\n`docs/research/minimal-rule-retrieval-contract.md`", "B1 的长期技术设计已收敛到：\n\n`docs/research/rule-retrieval-design-reference.md`"),
    ("B2 研究决策：\n\n`docs/research/rule-retrieval-prototype-selection.md`", "B2 的实现选择依据已收敛到 `docs/research/rule-retrieval-design-reference.md`；精确历史由 PR #81 / Git 保存。"),
    ("B3 验证证据：\n\n`docs/research/rule-retrieval-prototype-validation.md`", "B3 的当前可执行证据位于 `evals/rule-retrieval/` 与 `evals/query_rule_index.py`；精确实现 / 验证历史由 PR #82 / Git 保存。"),
    ("- `docs/research/rule-retrieval-targeted-evaluation-design.md`\n- `evals/rule-retrieval/targeted-evaluation-design.json`", "- `evals/rule-retrieval/targeted-evaluation-design.json`"),
    ("- `docs/research/rule-retrieval-ab-baseline-validation.md`\n- `evals/rule-retrieval/README.md`", "- `evals/rule-retrieval/README.md`"),
    ("- 证据入口：`docs/research/rule-retrieval-c3-evaluation-results.md` 与 `evals/rule-retrieval/c3-human-scoring.json`。", "- 机器可读人工评分保存在 `evals/rule-retrieval/c3-human-scoring.json`；精确运行 / PR 历史由 GitHub 原生记录。"),
    ("- E1 六项检查全部 PASS，详细证据见 `docs/research/rule-activation-e1-consumer-validation.md`。", "- E1 六项检查全部 PASS；精确 Consumer 验证与 Actions / Artifact 证据由 PR #89、Issue #73 和 GitHub 原生历史保存。"),
    ("F3 稳定项目状态在当前候选中完成收敛。F2 最终 AI 复核与人工集成决策必须针对最终 PR Head / diff 执行并记录在 PR / Issue；本文不预写尚未发生的复核或集成结果。", "F2 最终 AI 复核已完成，F3 稳定项目状态已收敛；最终集成通过 PR #89 完成，Issue #73 已关闭。"),
    ("当前没有新的里程碑实施门禁。A～E 与 F1 / F3 已完成；下一有限里程碑尚未选择，只有本里程碑完成集成后才重新进入人工路线决策。WI-07 仍只是优先候选，不自动启动。", "本里程碑已完成并集成，不再承担当前工作入口职责。当前路线为待人工决策；WI-07 仍只是优先候选，不自动启动。"),
]
for old, new in repls:
    if old not in text:
        raise SystemExit(f"project record replacement missing: {old[:70]}")
    text = text.replace(old, new, 1)
marker = "新上下文开始时应重新读取当前 GitHub 状态、`AGENTS.md`、项目路线图、Issue #73、本文件、`docs/research/rule-retrieval-targeted-evaluation-design.md`、`docs/research/rule-retrieval-ab-baseline-validation.md`、`docs/research/rule-retrieval-c3-evaluation-results.md` 和协调计划，然后从 D1 继续。"
pos = text.find(marker)
if pos < 0:
    raise SystemExit("project record stale recovery marker missing")
text = text[:pos] + """本文件现在是已完成里程碑的历史项目记录，不再承担 Fresh Context 当前工作入口。普通新上下文应读取 `AGENTS.md` 与 Project Roadmap；只有需要调查规则治理 v1 的历史设计或证据时，才按需读取本文件、长期 Research、`evals/rule-retrieval/*`，或通过 Git / PR #74～#89 / Issue #73 恢复已移除的过程材料。

不得因为历史文档曾记录 D1 / C3 / E1 等阶段，就把这些阶段重新解释为当前 Gate。
"""
p.write_text(text, encoding="utf-8")

p = Path("tasks/plans/20260908/01-rule-governance-knowledge-activation.md")
text = p.read_text(encoding="utf-8")
note = "> **2026-09-09 Research 信息架构治理说明**：本计划是已完成里程碑的过程协调记录。下文引用的阶段审计、激活映射、原型验证、A/B 运行和 E1 Consumer 验证等 `docs/research/*` 过程文件，已从当前 Research 树移除；如需历史复核，请通过 Git 历史、PR #74～#89、Issue #73 恢复原文件。当前长期技术入口为 `knowledge-activation-and-code-intelligence-analysis.md`、`knowledge-activation-evidence-appendix.md`、`llm-wiki-rule-governance-fit-analysis.md` 与 `rule-retrieval-design-reference.md`。本说明不重新激活该计划，也不启动 WI-07。\n\n"
if "2026-09-09 Research 信息架构治理说明" not in text:
    lines = text.splitlines(keepends=True)
    if not lines or not lines[0].startswith("# "):
        raise SystemExit("old plan title missing")
    text = lines[0] + "\n" + note + "".join(lines[1:])
    p.write_text(text, encoding="utf-8")

remove = [
    "activation-failure-classification.md",
    "cross-authority-duplication-audit.md",
    "external-operation-guidelines-activation-map.md",
    "minimal-rule-retrieval-contract.md",
    "rule-activation-audit-baseline.md",
    "rule-activation-e1-consumer-validation.md",
    "rule-retrieval-ab-baseline-validation.md",
    "rule-retrieval-c3-evaluation-results.md",
    "rule-retrieval-c3-runtime-readiness.md",
    "rule-retrieval-prototype-selection.md",
    "rule-retrieval-prototype-validation.md",
    "rule-retrieval-targeted-evaluation-design.md",
    "using-agentic-dev-activation-map.md",
]
for name in remove:
    path = Path("docs/research") / name
    if not path.exists():
        raise SystemExit(f"missing remove candidate: {path}")
    path.unlink()

new_identity = subprocess.check_output(["git", "hash-object", "AGENTS.md"], text=True).strip()
p = Path("evals/rule-retrieval/rule-index.json")
raw = p.read_text(encoding="utf-8")
data = json.loads(raw)
entries = [e for e in data["entries"] if e.get("entry_key") == "PTR-AGENTS-EXT"]
if len(entries) != 1 or entries[0]["source"]["path"] != "AGENTS.md":
    raise SystemExit("PTR-AGENTS-EXT invariant failed")
old_identity = entries[0]["source"]["identity"]
key_pos = raw.find('"entry_key":"PTR-AGENTS-EXT"')
line_start = raw.rfind("\n", 0, key_pos) + 1
line_end = raw.find("\n", key_pos)
if key_pos < 0:
    raise SystemExit("compact PTR-AGENTS-EXT entry missing")
if line_end < 0:
    line_end = len(raw)
line = raw[line_start:line_end]
token = f'"identity":"{old_identity}"'
if line.count(token) != 1:
    raise SystemExit("PTR-AGENTS-EXT identity token not unique")
newline = line.replace(token, f'"identity":"{new_identity}"', 1)
p.write_text(raw[:line_start] + newline + raw[line_end:], encoding="utf-8")
print("PTR-AGENTS-EXT identity:", old_identity, "->", new_identity)
