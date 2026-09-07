# Stacked PR 集成拓扑安全 v1 计划

## 状态

`ACTIVE — Evidence Revalidation / Platform Semantics Research`

启动基线：

`master@d1119e77a6fd83caa9e65334636d7aab6abdb06e`

跟踪入口：Issue #69。

## 目标

在不改变 Core Method、Skill Contract 或仓库 merge strategy 的前提下，针对 GitHub + squash merge 下的依赖式 PR 建立最小、可验证的集成拓扑安全指导，并区分 GitHub 原生 stacked pull requests 与普通手工依赖 PR 链。

## 权威与输入

- `AGENTS.md`
- `docs/project/project-roadmap.md`
- `docs/guides/external-operation-guidelines.md`
- `docs/method/ai-development-method.md` 中当前证据与收敛语义
- Issue #33 中已独立核验的 stacked PR + squash merge 历史证据
- Issue #69 的 Milestone Decision
- GitHub 当前官方 stacked pull requests / pull request merge 文档

## 范围

1. 重新核验历史 Consumer 证据；
2. 研究当前 GitHub 原生 stack 的 merge、rebase、CI 与 squash 语义；
3. 固化原生 stack 与普通依赖 PR 链的模式边界；
4. 在 External Operation / GitHub Integration 指导中增加薄规则；
5. 增加定向评估，覆盖普通依赖链、原生 stack、Head 变化与证据失效；
6. 完成静态检查、可执行评估准备、AI 复核、Roadmap / Issue / PR 回写。

## 非目标

- 不禁止 stacked PR；
- 不要求所有仓库使用 GitHub 原生 stack；
- 不修改 Core Method、Skill Contract 或新增 Skill；
- 不规定统一分支策略或 merge strategy；
- 不启动 WI-06、WI-07、WI-09、第四工程纪律或其他候选。

## 工作顺序

1. `Evidence Revalidation`：核验 Issue #33 既有证据与当前仓库已有 External Operation / Current Evidence 边界；
2. `Platform Semantics Research`：记录 GitHub 当前 public preview 原生 stacked PR 行为与稳定性限制；
3. `Architecture Fit`：确定长期规则只落在平台 / 外部操作指导层；
4. `Guidance`：形成薄规则，明确两种依赖 PR 模式及各自 Ready to Integrate 前检查；
5. `Targeted Eval`：新增场景与断言，并加入治理评估运行入口；
6. `Verification`：执行可在当前环境完成的静态检查；运行时模型评估必须使用隔离运行取得当前证据，不以本会话模拟替代；
7. `AI Review / Converge`：最终差异复核，未解决 Blocking / Medium 必须为 `0 / 0`；
8. `Ready to Integrate`：形成 PR 并等待人工集成决策。

## 完成条件

以 Issue #69 的完成定义为准。本计划只协调实施，不复制长期规则。
