# 场景 03：代码生成前的执行推理

这是一个 Fresh Context，只完成执行前分析与拟修改说明，不实际修改任何文件。

把下面目录视为当前唯一执行单元的最小 Consumer fixture：

`evals/fixtures/execute-unit-basic/`

请读取该 fixture 中的 `AGENTS.md`、`unit.md` 和现有代码 / 测试，并按当前 `agentic-dev` 方法判断：

1. 当前是否具备执行条件；
2. 当前唯一执行单元要求实现什么；
3. 应加载哪些 Skill / Rule / Authority；
4. 给出最小代码修改方案；
5. 给出必须执行的验证；
6. 哪些情况会要求 Stage Return，而不是继续编码；
7. 不得因为这是代码生成任务就扩展到其他 Execution Unit 或 Feature-wide converge。

如果当前 fixture 已经实现目标，也必须基于当前证据说明，不得为了产生代码而制造修改。

最后单独列出你实际读取的 Repository 文件。不要讨论规则治理 v2 候选方案。