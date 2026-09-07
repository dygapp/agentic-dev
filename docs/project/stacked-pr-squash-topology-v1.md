# Squash Merge 下 Stacked PR 集成拓扑安全 v1

## 状态

**当前：实施中**

当前门禁：

**运行时前 AI 复核 / 隔离运行时评估待执行**

跟踪入口：Issue #69。

启动基线：

`master@d1119e77a6fd83caa9e65334636d7aab6abdb06e`

实施分支：

`docs/stacked-pr-squash-topology-v1`

## 里程碑决策

2026-09-07，人工权威显式选择 Issue #33 中已独立核验的“stacked PR + squash merge 的审查拓扑 / 集成拓扑”候选作为下一有限里程碑。

长期阶段保持“工程能力扩展与方法演进”。本里程碑不自动启动 WI-06、WI-07、WI-09、第四工程纪律或其他候选。

## 目标

在 GitHub + squash merge + 依赖式 PR 场景中，建立足够薄、可验证的集成拓扑安全指导，使 Agent：

1. 不把临时审查拓扑自动等同于最终集成拓扑；
2. 能先识别当前依赖链是否由 GitHub 原生 stacked pull requests 生命周期管理；
3. 对普通手工依赖 PR 链，在父层集成、Head / base / diff 改变后重新建立可验证的集成拓扑；
4. 对平台原生 stack，按当前平台 stack 生命周期工作，同时重新读取真实 stack / PR 状态而不只相信自动化提示；
5. 把检查、工作流、评审和其他当前证据绑定到真实 Head / diff / 集成基线。

## 证据重新核验

Issue #33 的历史 Consumer 证据已经重新读取，原独立分类仍成立：

- 风险真实存在于当时的普通手工依赖 PR 链；
- 原 PR #38 显示 48 个 changed files，干净替代 PR #39 只保留 2 个职责文件；
- 原 PR #37 显示 58 个 changed files且未集成，干净替代 PR #40 只保留 13 个职责文件；
- child normalization 后重新取得当前证据；
- 最终分类为 `Low / Future Improvement Candidate`；
- 该证据不支持禁止 stacked PR、不支持修改核心方法 / 技能契约，也不支持新增 Skill。

## 当前平台研究结果

2026-09-07 重新核验 GitHub 当前官方文档后，确认 GitHub 已提供原生 stacked pull requests，当前仍处于 public preview。

当前官方行为显示：

- 原生 stack 对 trunk、层级、merge requirements 和 checks 有平台级识别；
- squash merge 可以按每层生成独立 squash commit；
- 从底层连续集成后，剩余上层可以由平台自动 rebase / retarget 到 trunk；
- stack 失去线性历史时存在级联 rebase 机制；
- public preview 的具体 UI、CLI、API 与自动化行为仍可能变化。

因此历史 Consumer 风险不能写成“所有 GitHub stacked PR 在 squash 后都必须人工 rebuild”的永久规律。

研究记录：

`docs/research/github-stacked-pr-squash-topology.md`

## 架构适配结论

当前证据支持的最小长期落点为：

`docs/guides/external-operation-guidelines.md`

原因：

- 问题核心是外部 GitHub 状态、PR 快照、Head / diff 和证据身份的验证；
- 核心方法已经要求当前权威、实现和当前证据对齐，无需修改方法阶段或生命周期；
- 技能契约没有缺口；
- 不需要新的 Skill；
- 具体 stack 能力属于平台行为，不能提升为跨平台永久契约。

## 当前实施

已完成：

- Issue #69 建立并冻结目标、范围、非目标与完成定义；
- 建立实施分支与协调计划；
- 完成 GitHub 当前 stack / squash merge 平台研究；
- 在外部操作指南中增加“依赖 PR 的审查拓扑与集成拓扑”薄规则；
- 新增 `G-PR-TOPO-01`、`G-PR-TOPO-02`、`G-PR-TOPO-03` 三个治理定向评估场景，共 15 条语义断言；
- 治理评估运行入口已加载新语料；
- 完成定向语料静态 JSON 解析与分支差异范围检查；
- 建立 Draft PR #70 作为后续运行时证据与最终复核载体。

待完成：

- 隔离运行时评估；
- 人工逐项语义评分；
- 最终项目状态回写；
- 最终 AI 复核；
- 达到“已具备进入集成决策的条件”并将 PR 转为正式复核状态。

## 定向评估门禁

评估文件：

`evals/governance/stacked-pr-integration-topology.json`

覆盖：

- `G-PR-TOPO-01`：普通手工依赖 PR 链 + 父层 squash merge；
- `G-PR-TOPO-02`：GitHub 原生 stack + 平台级联 rebase / retarget；
- `G-PR-TOPO-03`：stack 身份、PR 快照或 Head 不明确。

运行时必须使用仓库现有隔离治理评估运行器取得真实输出，再由人工逐条评分。进程退出码 `0` 不能单独视为通过。

## 非目标

- 不禁止 stacked PR；
- 不强制 GitHub 原生 stack；
- 不规定统一分支策略或合并策略；
- 不修改核心方法；
- 不修改技能契约；
- 不新增 Skill；
- 不把 GitHub public preview 细节提升为永久契约；
- 不启动其他候选里程碑。

## 完成定义

以 Issue #69 冻结的完成定义为准。只有在定向运行时评估和人工评分完成、最终 AI 复核未解决阻塞 / 中等级问题为 `0 / 0`、路线图 / Issue / PR 状态一致后，才可以报告本里程碑“已具备进入集成决策的条件”。
