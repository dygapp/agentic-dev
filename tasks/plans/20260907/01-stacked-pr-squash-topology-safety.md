# Stacked PR 集成拓扑安全 v1 计划

## 状态

**最终 AI 复核待执行**

启动基线：

`master@d1119e77a6fd83caa9e65334636d7aab6abdb06e`

跟踪入口：Issue #69。

实施载体：Draft PR #70。

## 目标

在不改变核心方法、技能契约或仓库合并策略的前提下，针对 GitHub + squash merge 下的依赖式 PR 建立最小、可验证的集成拓扑安全指导，并区分 GitHub 原生 stacked pull requests 与普通手工依赖 PR 链。

## 权威与输入

- `AGENTS.md`
- `docs/project/project-roadmap.md`
- `docs/guides/external-operation-guidelines.md`
- `docs/method/ai-development-method.md` 中当前证据与收敛语义
- Issue #33 中已独立核验的 stacked PR + squash merge 历史证据
- Issue #69 的里程碑决策
- GitHub 当前官方 stacked pull requests / pull request merge 文档

## 范围

1. 重新核验历史 Consumer 证据；
2. 研究当前 GitHub 原生 stack 的 merge、rebase、CI 与 squash 语义；
3. 固化原生 stack 与普通依赖 PR 链的模式边界；
4. 在外部操作 / GitHub Integration 指导中增加薄规则；
5. 增加定向评估，覆盖普通依赖链、原生 stack、Head 变化与证据失效；
6. 完成静态检查、可执行评估准备、AI 复核、路线图 / Issue / PR 回写。

## 非目标

- 不禁止 stacked PR；
- 不要求所有仓库使用 GitHub 原生 stack；
- 不修改核心方法、技能契约或新增 Skill；
- 不规定统一分支策略或合并策略；
- 不启动 WI-06、WI-07、WI-09、第四工程纪律或其他候选。

## 工作顺序

1. **证据重新核验**：核验 Issue #33 既有证据与当前仓库已有外部操作 / 当前证据边界；
2. **平台语义研究**：记录 GitHub 当前 public preview 原生 stacked PR 行为与稳定性限制；
3. **架构适配**：确定长期规则只落在平台 / 外部操作指导层；
4. **薄指导**：形成规则，明确两种依赖 PR 模式及各自进入集成决策前的检查；
5. **定向评估**：新增场景与断言，并加入治理评估运行入口；
6. **验证**：执行可在当前环境完成的静态检查；运行时模型评估必须使用隔离运行取得当前证据，不以本会话模拟替代；
7. **AI 复核 / 收敛**：最终差异复核，未解决阻塞 / 中等级问题必须为 `0 / 0`；
8. **已具备进入集成决策的条件**：PR 转为正式复核状态并等待人工集成决策。

## 当前进展

步骤 1～6 已完成：

- 完成历史证据、当前平台语义和架构适配核验；
- 完成薄指导、治理定向评估和静态检查；
- 运行时前 AI 复核 PR #70 Review `5128856306` 未解决阻塞 / 中等级问题为 `0 / 0`；
- 首轮三个隔离场景均 `returncode=0`、stderr 为空、未发现污染，人工语义评分为 `14 / 15`；
- `G-PR-TOPO-01` 与 `G-PR-TOPO-03` 均为 `5 / 5`；
- `G-PR-TOPO-02` 唯一缺口经长期规则激活修订后，第二次重跑仍为 `4 / 5`，随后仅调整场景提问覆盖，未降低 `expected_behavior` 或断言；
- 运行时评估行为 Head `267b0928b745eac990594b43986048a25b8470a9` 上第三次 `G-PR-TOPO-02` 重跑为 `5 / 5`；其后仅发生 README、Roadmap、里程碑记录与计划等状态回写，不涉及治理评估声明的四个运行时上下文文件，因此既有运行时证据仍适用于行为候选；
- 最终有效治理语义评分为：

```text
G-PR-TOPO-01: 5 / 5
G-PR-TOPO-02: 5 / 5
G-PR-TOPO-03: 5 / 5
合计:          15 / 15
```

有效运行均使用隔离 `codex exec --ephemeral --json`，进程退出码为 `0`、stderr 为空；运行轨迹仅读取场景声明的仓库内相对路径，没有读取评分语料、历史 `evals/results/*` 或隔离工作目录外上下文。

当前只剩步骤 7～8：完成最终项目状态回写、最终 AI 复核；若未解决阻塞 / 中等级问题为 `0 / 0`，则进入“已具备进入集成决策的条件”并将 PR 转为正式复核状态。

## 完成条件

以 Issue #69 的完成定义为准。本计划只协调实施，不复制长期规则。
