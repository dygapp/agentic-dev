# Research 信息架构治理

## 目标

在不启动 WI-07 或其他新有限里程碑的前提下，治理 `docs/research/` 当前混合“长期技术研究”与“里程碑过程证据”的问题。

完成后，`docs/research/` 只保留两类材料：

1. 离开原实施阶段后仍具有独立技术参考价值的外部规范、开源工程、工程实践或技术研究；
2. 能明确解释、支撑当前 Repository Authority 的技术资料，并能指出对应 Authority。

阶段审计、基线冻结、readiness、prototype validation、A/B 执行结果、Consumer 验证报告等过程材料不继续作为当前 Research 文档；其历史由 Git / PR / Issue、`docs/project/*`、`evals/*` 和本计划承接。

## 基线与边界

- 基线：`master@1dcb2d6fed146d62b23e832da28f6148281cc72a`
- PR #90 已合并；当前路线状态为待人工决策。
- 本任务属于仓库信息架构维护，不创建新的活动有限里程碑。
- 不启动 WI-07、WI-06、WI-09、第四工程纪律或 Issue #71 候选实施。
- 不修改 Method / Architecture / Skill / Engineering Discipline / Technology Profile 的规范语义。

## 长期保留方向

### 方法 / Skill / 外部实践研究

- `agent-skills-specification-analysis.md`
- `mattpocock-skills-analysis.md`
- `spec-kit-analysis.md`
- `superpowers-analysis.md`
- `andrej-karpathy-skills-analysis.md`

### 与当前工程能力对应的技术研究

- `implementation-minimality-and-speculative-complexity-analysis.md`
- `surgical-change-and-diff-scope-control-analysis.md`
- `data-access-scope-boundedness-analysis.md`
- `vue3-typescript-profile-analysis.md`
- `github-stacked-pr-squash-topology.md`

### 知识激活 / 检索技术研究

- `knowledge-activation-and-code-intelligence-analysis.md`
- `knowledge-activation-evidence-appendix.md`
- `llm-wiki-rule-governance-fit-analysis.md`
- 新建 `rule-retrieval-design-reference.md`，承接原最小检索契约与原型选择中仍具长期价值的技术设计。

## 从当前 Research 移除的过程材料

- `activation-failure-classification.md`
- `cross-authority-duplication-audit.md`
- `external-operation-guidelines-activation-map.md`
- `minimal-rule-retrieval-contract.md`（由长期设计参考替代）
- `rule-activation-audit-baseline.md`
- `rule-activation-e1-consumer-validation.md`
- `rule-retrieval-ab-baseline-validation.md`
- `rule-retrieval-c3-evaluation-results.md`
- `rule-retrieval-c3-runtime-readiness.md`
- `rule-retrieval-prototype-selection.md`
- `rule-retrieval-prototype-validation.md`
- `rule-retrieval-targeted-evaluation-design.md`
- `using-agentic-dev-activation-map.md`

这些文件不迁移到 Research archive。Git 历史、PR #74～#89、Issue #73、`docs/project/rule-governance-knowledge-activation-v1.md` 与 `evals/rule-retrieval/*` 已能够承接过程和验证证据。

## 必要入口收敛

1. 重写 `docs/research/README.md`，明确准入标准、禁止项、Authority 对应关系和目录清单；
2. 更新 `AGENTS.md`，修正 PR #90 后仍残留的活动里程碑状态，并删除过程 Research 恢复清单；
3. 更新根 `README.md`，将当前状态明确为待人工决策，不再要求恢复已关闭 Issue #73 的过程上下文；
4. 更新 `docs/project/project-roadmap.md`，把规则治理 v1 的研究入口收敛为长期技术资料 + Project / Eval 证据；
5. 更新 `docs/project/rule-governance-knowledge-activation-v1.md`，保留里程碑事实，但不再把已删除过程 Research 作为当前文件入口；
6. 在已完成的 `tasks/plans/20260908/01-rule-governance-knowledge-activation.md` 增加治理说明，明确历史路径应通过 Git 历史恢复。

## 完成条件

- `docs/research/` 不再包含上述 13 份过程材料；
- `docs/research/README.md` 能直接说明每份保留资料的长期价值与 Authority 关系；
- `rule-retrieval-design-reference.md` 不依赖 B1/B2/C3 阶段状态即可独立阅读；
- 当前高权威入口不再引用已删除 Research 文件；
- `evals/rule-retrieval/*` 可执行资产不受影响；
- `AGENTS.md`、README、Roadmap 一致反映：规则治理 v1 已完成并集成，当前待人工决策，WI-07 未启动；
- 最终差异不包含临时 workflow；
- Final AI Review 未解决 Blocking / Medium = `0 / 0`。
