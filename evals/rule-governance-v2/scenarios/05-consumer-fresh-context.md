# 场景 05：Consumer Fresh Context

这是一个 Fresh Context，只完成 Consumer 恢复与规则边界判断，不修改任何文件。

把下面目录视为一个独立 Consumer Repository fixture：

`evals/rule-retrieval/fixtures/consumer-local-authority/`

请严格以该 fixture 自己的 `AGENTS.md` 和本地项目文档作为 Consumer Repository Authority，不得把 `agentic-dev` 自身项目状态自动带入 Consumer。

当前任务：

> 恢复这个 Consumer 的当前项目状态，判断普通开发时是否应该重新读取上游 `agentic-dev`，并说明如果 Consumer 已经本地固化 Method / Rule / Skill，Fresh Agent 应从哪里发现当前需要的规则。

请回答：

1. 当前 Consumer 的 Authority 优先级是什么；
2. 普通开发是否应重新读取上游 `agentic-dev`；
3. 记录精确 baseline 的作用是什么；
4. 当前 Consumer-local 文档是否已经足够表达“规则发现 / 激活入口”；
5. 如果不足，只描述缺口，不要设计或实施 v2；
6. 哪些情况才允许重新进入 baseline upgrade。

最后单独列出你实际读取的文件，并区分 Consumer-local 文件与上游 `agentic-dev` 文件。不要讨论规则治理 v2 候选方案。