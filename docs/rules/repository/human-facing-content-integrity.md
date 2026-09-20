---
id: rule:human-facing-content-integrity
type: rule
status: active
distribution: source-only
scope:
  phases: []
  activities: [documentation, communication, review, implementation]
  technologies: []
  artifacts: [human-facing-content, machine-identifier, authority]
  risks: []
---

# 面向人的内容完整性

编写或修改文档、Issue、PR、Review、状态说明及其他人类可读内容时，同时保持自然中文表达、精确标识与稳定状态值，以及正式概念身份。

## 默认使用自然中文

`agentic-dev` 的面向人内容默认使用自然、完整、连续的中文。动作、判断、因果和结论应以中文表达，不为了显得专业、方便检索或制造“术语感”机械保留普通英文，也不把中英文并列作为默认模板。

当前用户明确要求使用其他语言时，以该次明确要求为准。Consumer 的主导语言由 Consumer 自己的 Repository Authority 决定。

## 精确标识、稳定状态值和外部正式名称保持原样

Skill 调用名、文件名与路径、Branch、Commit SHA、Issue / PR 编号、代码标识符、配置键、数据库字段、API / CLI、命令与参数、协议值、真实日志和错误信息必须保持可精确匹配的原始形式。

作为跨文档、Gate、验证或复核结果使用的简短稳定状态值，例如 `PASS`、`FAIL`、`READY`、`BLOCKED`、`PENDING`、`HOLD`，可以保持原样；不为了“纯中文”制造同一状态的第二套表示。状态值周围的原因、判断和结论仍使用自然中文。

外部产品、框架、协议、标准、规范和官方项目名称在翻译会损害识别或对照能力时保留正式名称。

保留这些对象原样只适用于对象本身；周围的说明、判断和结论仍使用自然中文。

## 正式概念身份和稳定中文表达不得被语言重写改变

中文化、术语整理或表达优化只能改变面向人的表达，不得把具有不同职责或生命周期的 Method stage、gate、artifact、Skill、Rule、Architecture 等正式对象合并，也不得改变其正式身份。

当前 canonical owner 已经形成稳定中文表达时，后续面向人内容应沿用，不自行制造同义中文、不恢复已经退出当前模型的历史迁移别名。只有在自然语言可能对应多个正式对象时，才用对象类型或精确标识消除歧义；身份已经明确后，不重复双语注释。

正式概念拥有英文 identity，不等于普通中文叙述默认保留英文名称。当前句子只需表达概念含义、类型或状态而不需要逐字识别正式 identity 时，应使用自然中文或当前稳定中文表达。例如写“稳定基线”“当前方法”“规则发现已完成”“人工指南”，而不是把 `baseline`、`Method`、`Rule Discovery`、`Human Guide` 当作默认术语嵌入中文句子。只有确实需要消歧、引用精确 id / 调用名、路径或外部官方名称时才保留对应原文。

当前高风险的表达区分包括：

- 技术规划阶段不等于技术计划产物；
- 执行阶段不等于 `execute-unit` Skill；
- 整体收敛阶段不等于 `converge` Skill；
- 就绪门禁不等于 `readiness-check` Skill；
- 仓库权威不等于人工权威。

这些区分只约束语言表达和身份消歧，不重新定义对象语义；正式概念的职责、生命周期和 canonical identity 仍由各自 canonical owner 持有。不得为了建立“统一术语表”在 Guide、README 或其他解释层维护第二套概念定义。

## 面向人的结构优先中文

标题、表格标题与列名、列表中的动作说明、流程图节点以及其他面向人的结构性标签默认使用中文。只有结构项本身就是机器标识、稳定状态值、外部正式名称或必须精确对照的正式身份时才保留原样。

## Agent 协作输出同样适用

Agent 面向用户展示的分析、进度更新、规划、风险、阻塞、验证结果和复核结论遵守同一语言规则。输入材料、工具输出、历史 PR 或旧文档大量使用英文，不构成切换叙述语言的理由。

必须引用英文原文时，将引用与 Agent 自己的中文判断分开，不让引用语言扩散为整段叙述语言。
