# 工程术语语义安全与现行文档全量收敛 v1

## 1. 目标

本里程碑解决两个相互关联的问题：

1. 中文表达收敛不能改变正式工程概念的身份、对象类型、方法职责、架构层级、契约或机器标识；
2. 当前仓库中仍会被 Agent、开发者、评估运行器或项目恢复流程主动读取的人类可读材料，需要按现行中文表达规则完成一次全量扫描和分类收敛。

本里程碑不新增方法阶段、工程能力层、工程纪律、技术画像或 Skill。

跟踪入口：Issue #64。

启动基线：

`master@5dc5b7135d59b43d624cf5a8407dae6d6b04a514`

工作分支：

`governance/terminology-semantic-safety-v1`

PR：#67。

## 2. 阶段 A：正式概念语义安全

阶段 A 已完成。

建立的核心保护规则：

- 正式工程概念使用唯一首选中文名称；
- 首选中文名称与正式英文身份的映射统一由术语规范维护；
- 正式职责仍由对应方法 / 架构 / 契约定义权威决定，术语映射不重新定义职责；
- 方法阶段、产物、门禁、能力层和 Skill 调用名即使语义相邻，也不得因中文化合并；
- 代码、命令、配置键、Git / GitHub 原生字段、版本、SHA、评估编号和外部正式名称保持原样。

阶段 A 运行时证据：

```text
G-LANG-01：5 / 5 断言通过
G-TERM-01：5 / 5 断言通过
G-TERM-02：5 / 5 断言通过
合计：     15 / 15 断言通过
```

三个场景进程退出码均为 `0`，标准错误为空，JSONL 均包含 `turn.completed`；未发现越出声明隔离上下文的读取。

运行附件 SHA-256：

`616c54d8146a205a8c96bc52f9c429f5a90ddebb801c43ecbcdb145dd1544b47`

阶段 A 静态跨层复核 Review `5125728184` 未解决阻塞 / 中等级问题为 `0 / 0`。

`G-TERM-02` 有一次仅用于定位文本的 shell 命令因反引号引用产生非阻塞 `command not found` 输出；没有影响最终回答、进程状态、隔离边界或语义评分，作为低等级评估执行观察保留。

## 3. 阶段 B：全量扫描分类

阶段 B 已完成仓库内容扫描与必要修订。扫描范围按当前分支实际目录树建立，不以关键词命中替代文件枚举。

处理分类统一为：

1. **现行定义 / 治理权威**：逐文件检查；存在冲突名称、普通英文叙述或陈旧当前状态时修订；
2. **当前能力实现 / 操作指南**：逐文件检查；保留精确互操作标识，清理无必要英文叙述；
3. **Skill 双用途契约实现**：保留 front matter、契约结构字段和精确调用名；只有正式身份或职责冲突才修改；
4. **评估语料 / 运行说明**：检查是否仍对应当前定义状态；历史结果不为了语言外观改写；
5. **历史研究 / 旧计划 / 收尾材料**：纳入扫描，检查是否会竞争当前权威；默认不机械重写历史证据；
6. **法律与机器文件**：不为了语言统一修改。

## 4. 根目录扫描

| 文件 | 分类 | 处理结果 |
|---|---|---|
| `AGENTS.md` | 最高项目权威 | 已检查并建立正式概念身份保护、当前里程碑边界；阶段 B 完成状态在最终候选中同步 |
| `README.md` | 当前入口 | 已检查并同步语言治理、当前里程碑和恢复入口 |
| `LICENSE` | 法律文本 | 已扫描存在性；不修改外部许可原文 |
| `.gitignore` | 机器 / 仓库配置 | 不属于人类叙述收敛对象 |

## 5. `docs/` 扫描

### 5.1 方法

- `docs/method/ai-development-method.md` — 已实质收敛普通英文叙述，保持方法阶段、技术计划等对象边界；
- `docs/method/principles.md` — 已实质收敛，保持原则语义等价。

### 5.2 架构与契约

- `docs/architecture/engineering-capability-architecture.md` — 已实质收敛；统一“技术画像 / 验证画像 / 任务型技能 / 运行时适配器”；
- `docs/architecture/engineering-disciplines.md` — 已实质收敛；三项正式纪律首次定义保留英文身份锚点，正文使用中文首选名称；
- `docs/architecture/first-batch-skill-design.md` — 已实质收敛；Skill 调用名和契约结构保持原样；
- `docs/architecture/skill-architecture.md` — 已实质收敛普通英文叙述；
- `docs/architecture/skill-contracts.md` — 已逐节扫描；作为 Skill 正式契约身份源，保留 `Purpose`、`Use When`、`Inputs`、`Exit Conditions` 等契约结构和精确输入 / 输出身份，不做表面全文翻译；未发现技术画像等冲突中文别名重新定义；
- `docs/architecture/technology-profile-contract.md` — 已实质收敛；移除“技术配置档 / 验证配置档”等现行冲突名称。

### 5.3 方法决策

- `docs/decisions/method-decisions.md` — 已实质收敛；保留 `D-xxx`、ADR、精确 Skill 名和历史取代关系。

### 5.4 使用指南

- `docs/guides/external-operation-guidelines.md` — 已逐节扫描；正文已以中文为主体，GitHub、API、字段和命令等原样保留，无需额外大规模改写；
- `docs/guides/git-commit-guidelines.md` — 已逐节扫描；`type(scope)`、`BREAKING CHANGE` 和 Skill 调用名属于提交协议 / 精确身份，当前语言规则已清楚，无需修改；
- `docs/guides/terminology-guidelines.md` — 已建立正式概念身份映射和唯一首选中文名称；
- `docs/guides/using-agentic-dev.md` — 已逐节扫描并保持自然中文；外部正式名、Skill 调用名、路径和命令继续原样保留。

### 5.5 项目治理与里程碑

当前目录实际文件：

- `docs/project/ai-review-guidelines.md`
- `docs/project/chinese-interaction-context-cleanup-v1.md`
- `docs/project/engineering-capability-foundation-v1-closure.md`
- `docs/project/engineering-capability-foundation-v1.md`
- `docs/project/engineering-discipline-expansion-v1-closure.md`
- `docs/project/engineering-discipline-expansion-v1.md`
- `docs/project/engineering-discipline-scope.md`
- `docs/project/project-roadmap.md`
- `docs/project/repository-baseline.md`
- `docs/project/terminology-semantic-safety-v1.md`

处理结果：

- AI 复核规则已增加翻译导致对象类型合并、层级漂移和契约语义变化的检查；
- 项目路线图、README、AGENTS 和本轮计划作为当前状态入口同步维护；
- `repository-baseline.md` 已收敛普通英文叙述；
- “中文交互与上下文清理 v1”文档中 PR #63 的旧“等待集成”状态已按 GitHub 当前事实修正为已合并，合并提交 `5dc5b7135d59b43d624cf5a8407dae6d6b04a514`；
- 工程能力基础、工程纪律扩展及范围文档属于已完成里程碑 / 范围历史，已检查其不会竞争当前路线，不为了语言外观整体重写。

### 5.6 技术画像

- `docs/technology-profiles/README.md` — 已实质收敛；
- `docs/technology-profiles/vue3-typescript.md` — 已实质收敛；Vue / TypeScript API、版本、SHA、`TC/ED/CG/KM/VP` 编号和 `C-VTS-xx` 等保持原样。

### 5.7 研究材料

当前 `docs/research/` 文件：

- `README.md`
- `agent-skills-specification-analysis.md`
- `andrej-karpathy-skills-analysis.md`
- `data-access-scope-boundedness-analysis.md`
- `implementation-minimality-and-speculative-complexity-analysis.md`
- `mattpocock-skills-analysis.md`
- `spec-kit-analysis.md`
- `superpowers-analysis.md`
- `surgical-change-and-diff-scope-control-analysis.md`
- `vue3-typescript-profile-analysis.md`

以上均按历史研究 / 证据材料扫描。它们保留来源原名、历史术语和当时研究表达，不作为当前中文术语定义权威；未发现需要为了避免竞争当前权威而整体重写的阻塞问题。

## 6. `skills/` 扫描

当前技能入口：

- `skills/README.md`
- `skills/clarify-intent/SKILL.md`
- `skills/specify/SKILL.md`
- `skills/technical-plan/SKILL.md`
- `skills/slice-work/SKILL.md`
- `skills/readiness-check/SKILL.md`
- `skills/execute-unit/SKILL.md`
- `skills/systematic-debug/SKILL.md`
- `skills/converge/SKILL.md`
- `skills/github-actions-verification/SKILL.md`

`skills/README.md` 已实质收敛。

9 个 `SKILL.md` 已逐一检查。它们同时承担 Agent 契约实现和打包 / 发现职责，因此：

- `name` / `description` front matter 保留；
- `Purpose`、`Use When`、`Do Not Use When`、`Inputs`、`Authority Sources`、`Procedure`、`Outputs`、`Exit Conditions`、`Escalation Conditions`、`Context Rules`、`Allowed Sub-skills / Disciplines` 等契约结构保留；
- `clarify-intent`、`execute-unit`、`converge` 等精确调用名保留；
- 不为了表面中文化修改已经有运行时证据支持的行为契约；
- 未发现它们把“技术配置档 / 验证配置档 / 运行时适配层”等旧中文迁移别名重新定义为当前能力层。

`github-actions-verification` 的当前运行参考文件也纳入逐文件扫描：

- `references/branch-pr-verification-path.md` — 已收敛普通英文叙述；
- `references/containerized-e2e.md` — 已收敛普通英文叙述；
- `references/diagnostics-and-runtime-cost.md` — 已收敛普通英文叙述；
- `references/evidence-observability.md` — 已收敛普通英文叙述。

GitHub Actions 原生字段、YAML 键、事件名、Run / Job / Step / Artifact、SHA、容器与工具名称按精确对象保持原样。

## 7. `evals/` 扫描

### 7.1 当前运行说明

- `evals/CODEX.md` — 已逐节扫描；当前已以中文说明隔离、运行和评分边界，命令 / 字段 / 场景编号保持原样；
- `evals/capability/README.md` — 已实质收敛普通英文叙述；
- `evals/governance/README.md` — 已更新为阶段 B 最终语义回归边界。

`evals/README.md` 主要承担历次运行时评估的历史证据索引，包含大量当时的英文场景标签与运行术语。它已纳入扫描，但不为了语言外观整体改写历史结果；当前新评估和人工汇报继续遵守现行中文规则。

### 7.2 评估语料

激活语料：

- `evals/activation/core-first-pass.json`

行为语料：

- `evals/behavior/clarify-intent.json`
- `evals/behavior/converge.json`
- `evals/behavior/execute-unit.json`
- `evals/behavior/github-actions-verification.json`
- `evals/behavior/readiness-check.json`
- `evals/behavior/slice-work.json`
- `evals/behavior/specify.json`
- `evals/behavior/systematic-debug.json`
- `evals/behavior/technical-plan.json`

工程能力语料：

- `evals/capability/vue3-typescript-profile.json`

项目治理语料：

- `evals/governance/chinese-human-facing-output.json`
- `evals/governance/formal-concept-semantic-safety.json`
- `evals/governance/method-object-semantic-safety.json`

这些 JSON 是评估输入 / 评分材料，不作为面向人的语言示范。历史语料不机械翻译；只有当当前定义状态改变导致题面或期望行为陈旧时才修订。

阶段 B 已发现并修正 `G-TERM-01` 的陈旧假设：最终场景不再声称现行定义权威仍包含旧别名，而是把旧别名作为历史 / 迁移输入，验证它们不能重新覆盖当前正式身份。

## 8. `tasks/` 扫描

`tasks/README.md` 已实质收敛，继续规定临时协调而非长期权威。

历史计划已按目录树纳入扫描：

### 2026-08-17

- `01-establish-github-as-project-source-of-truth.md`
- `02-implement-readiness-check-skill.md`
- `03-implement-slice-work-skill.md`
- `04-implement-clarify-intent-skill.md`
- `05-implement-specify-skill.md`
- `06-implement-technical-plan-skill.md`
- `07-implement-systematic-debug-skill.md`
- `08-implement-execute-unit-skill.md`
- `09-implement-converge-skill.md`

### 2026-08-18

- `01-review-first-batch-skills-and-define-skill-engineering-closure.md`
- `02-converge-project-governance-and-reuse-boundaries.md`
- `03-first-real-repository-validation.md`

### 2026-08-20

- `01-artifact-lifecycle-closure-method-revision.md`
- `01-github-actions-verification.md`
- `02-artifact-lifecycle-operationalization-recovery.md`

### 2026-08-24

- `01-acceptance-verification-closure.md`
- `02-project-roadmap-method.md`

### 2026-08-26

- `01-existing-consumer-governance-evidence.md`

### 2026-08-28

- `01-verification-evidence-boundaries.md`
- `02-review-evidence-impact.md`

### 2026-08-31

- `01-shared-resource-concurrency.md`

### 2026-09-01

- `01-engineering-capability-expansion.md`
- `01-implementation-judgment-evidence.md`

### 2026-09-02

- `01-technology-profile-contract.md`
- `02-vue-typescript-profile.md`
- `03-foundation-v1-consumer-adoption-handoff.md`

### 2026-09-03

- `01-foundation-v1-closure.md`
- `02-data-access-discipline.md`

### 2026-09-04

- `01-issue-58-external-lifecycle.md`

### 2026-09-05

- `01-issue-58-planning-candidate-boundary.md`

### 2026-09-06

- `01-issue-58-verification-readiness-adoption.md`
- `02-chinese-interaction-context-cleanup.md`
- `03-terminology-semantic-safety-and-doc-scan.md`

这些计划属于历史 / 临时协调材料。它们可以保留当时使用的英文标签、阶段描述和旧术语，只要不被当作当前权威恢复；本轮不对其做无语义价值的批量重写。

## 9. 阶段 B 语义安全结论

本轮修订遵循以下边界：

- 没有新增或删除方法阶段；
- 没有改变执行单元、就绪门禁、整体收敛、人工升级或集成边界；
- 没有把技术规划阶段与技术计划产物合并；
- 没有把方法阶段 / 门禁与 Skill 调用名合并；
- 没有把技术画像、验证画像、任务型技能或运行时适配器改变成新的能力层；
- 没有新增 Skill，也没有修改 9 个 `SKILL.md` 的行为契约；
- 历史证据中的旧表达没有被提升为当前正式名称；
- PR #63 等已发生 GitHub 事实按当前仓库状态修正，不把历史候选状态继续当作现行事实。

因此阶段 B 的仓库内容扫描与必要修订已经完成，但**本里程碑尚未完成**。

## 10. 最终门禁

阶段 B 修改了阶段 A 运行时评估所读取的定义和项目状态上下文，因此阶段 A 的 `15 / 15` 只证明阶段 A 当时的语义门禁，不直接替代最终候选回归。

最终候选必须重新运行：

```bash
python3 evals/run_governance_evals.py --scenario G-LANG-01
python3 evals/run_governance_evals.py --scenario G-TERM-01
python3 evals/run_governance_evals.py --scenario G-TERM-02
```

要求：

- 三个场景均在独立隔离运行环境执行；
- 进程轨迹无评分语料或历史结果污染；
- 每个场景人工语义评分 `5 / 5`；
- 合计 `15 / 15`；
- 随后对 PR #67 最终提交执行 AI 复核；
- 未解决阻塞 / 中等级问题必须为 `0 / 0`。

只有这些最终门禁通过，PR #67 才可以进入人工集成决策；本里程碑不授予自动合并权限。
