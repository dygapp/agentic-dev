# 中文交互与上下文清理计划

**状态：** 等待运行时验证

## 目标

按 Issue #62 与 `docs/project/chinese-interaction-context-cleanup-v1.md` 推进下一有限里程碑，建立严格中文默认规则、清理高影响示范语料、补充中文输出行为评估，并把账户级记忆清理保留为人工验收步骤。

## 权威与输入

- `AGENTS.md`
- `docs/project/project-roadmap.md`
- `docs/project/chinese-interaction-context-cleanup-v1.md`
- `docs/guides/terminology-guidelines.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/external-operation-guidelines.md`
- `docs/project/ai-review-guidelines.md`
- `evals/README.md`
- Issue #62
- 启动基线：`master@9818b3209a80bba22c6fbec2af740f49a17fa2d4`

## 范围

1. 更新路线图，记录当前有限里程碑已经由人工启动；
2. 收紧 `AGENTS.md` 与术语表达规范；
3. 清理 README、使用指南、外部协作指南、AI 复核规则中直接影响默认语言行为的规则与示例；
4. 增加中文输出稳定性行为评估；
5. 执行静态检查、独立运行时评估、人工语义评分与最终 AI 复核；
6. 将结果回写到本计划、路线图、Issue #62 和 PR。

## 非目标

- 不新增或修改核心方法阶段；
- 不新增工程纪律、技术画像、任务型 Skill 或运行时适配器；
- 不重写全部历史研究、历史证据、已关闭计划或 Git 历史；
- 不由仓库工具删除 ChatGPT 账户级记忆；
- 不自动合并 PR。

## 工作项

1. 建立里程碑与跟踪 Issue；
2. 更新路线图当前状态；
3. 修订严格中文表达规则；
4. 收敛高影响入口；
5. 新增行为评估及评分标准；
6. 完成静态检查；
7. 完成独立运行时评估与人工语义评分；
8. 完成最终 AI 复核；
9. 回写证据并推进到人工集成决策。

## 当前证据

- `master` 启动基线在本轮执行期间未漂移；
- PR #63 保持 Draft、未合并；
- 全量差异复核已经发现并修复两类语义回归：使用指南误删既有方法细节、`AGENTS.md` 漏掉主动外部研究与使用方证据边界；
- 后续复核未再发现新的阻塞 / 中等级方法语义问题；
- `evals/run_governance_evals.py` 已通过 Python 语法编译检查；
- `evals/governance/chinese-human-facing-output.json` 定义 6 个唯一场景，并为每个场景提供人工语义断言；
- 当前 ChatGPT 执行环境不存在 `codex` 可执行文件；容器也无法直接访问 GitHub 克隆仓库，因此本会话没有取得真实 `codex exec --ephemeral --json` 运行结果；
- 运行时评估、基于运行结果的人工语义评分和最终 AI 复核仍待完成，不能宣称通过。

## 完成条件

- 路线图与 Issue #62 一致；
- 高影响入口不再推荐稳定中文概念机械附带英文；
- 会话汇报、Issue / PR、人工复核等输出被明确纳入严格中文治理；
- 行为评估能区分“语义正确但中英文混写”和“自然中文且保留必要原始标识”；
- 新场景及必要回归通过独立运行时评估和人工语义评分；
- 最终 AI 复核未解决的阻塞 / 中等级问题为 `0 / 0`；
- 账户级记忆清理步骤已明确交付；
- PR 保持未合并，等待人工权威决定。