---
id: guide:language-and-terminology
type: guide
status: active
---

# 语言与术语指南

本文帮助人工理解和维护 `agentic-dev` 的中文表达、原始标识和正式概念身份。它是 **Human View**，不是第二套语言 Authority。

规范性 owner：

- 通用面向人内容：`rule:human-facing-content-integrity`；
- Git Commit 格式与摘要语言：`rule:git-commit-discipline`；
- Method、Architecture、Skill、Rule 等正式对象的职责与身份：各自 canonical owner。

本文可以在语言复查、术语整理、文档重写等责任中由 Agent 按需参考，但不进入 ordinary Agent runtime 的固定 Bootstrap。

## 1. 判断一个英文内容是否应该保留

按以下顺序判断：

1. **必须精确匹配的机器对象**：保留原样；
2. **外部正式名称**：翻译会降低识别、检索或规范对照能力时保留原样；
3. **正式概念身份锚点**：确有消歧需要时，在首次必要位置保留正式英文身份或精确 id；
4. **普通叙述**：使用自然中文。

英文不是默认的“更精确表达”。精确性来自真实 Authority、上下文和必要的原始标识。

## 2. 自然中文是默认值

推荐：

```text
执行单元完成后必须取得当前证据，再进入整体收敛。
```

不推荐：

```text
Execution Unit 完成后必须取得 Current Evidence，再进入 Converge。
```

如果必须保留精确 Skill 名称，可以写：

```text
`readiness-check` 未通过，需要回到工作切分重新形成候选执行单元。
```

不要把周围的动作和判断一起切换成英文。

## 3. 不把中英文并列当作标准模板

以下形式不应成为默认写法：

```text
中文概念（English Term）
English Term（中文解释）
```

只有在以下情况下才需要补充英文身份：

- 不保留会造成真实对象歧义；
- 正在定义该正式概念本身；
- 需要与外部标准、协议或原始资料精确对照；
- 当前任务明确要求双语材料。

身份已经明确后，后续继续使用自然中文或精确 id，不重复括号注释。

## 4. 必须或适合保持原样的内容

通常保持原样：

- Skill 调用名，例如 `clarify-intent`、`execute-unit`；
- Rule / Method / Architecture 等精确资源 id；
- 文件名、路径、Branch、Commit SHA、Issue / PR 编号；
- 代码标识符、配置键、数据库字段、枚举值；
- API、CLI、命令和参数；
- GitHub Actions 的事件名、字段名和表达式；
- 错误信息、日志、命令输出；
- 必须与外部系统逐字匹配的固定值；
- GitHub、Codex、Vue 3、TypeScript 等外部产品或技术正式名称；
- 外部协议、标准、规范和项目的正式名称。

是否保留的核心问题不是“这个词是不是英文”，而是“翻译后是否会丢失精确身份或外部对照能力”。

## 5. 正式概念与自然语言表达

正式概念的 semantic owner 决定它是什么；语言指南只决定怎样向人表达。

例如：

- 方法阶段和同名 Skill 不能因为中文名称相近而合并；
- Gate、artifact、Method stage、Skill 调用名属于不同对象时，应显式写出对象类型；
- 一个普通中文词不能因为与正式概念同名就自动升级为正式对象；
- 如果 canonical owner 已定义稳定中文名称，应优先沿用；
- 如果 owner 只定义精确 id 或英文身份，而当前上下文确有身份识别需要，可以保留该身份，不另建中央术语映射表。

本 Guide 不维护全仓“中文名称 ↔ 英文名称”总表，以避免与各 canonical owner 漂移。

## 6. 面向人的状态怎样表达

如果状态只是给人阅读：

- PASS → 通过；
- FAIL → 失败；
- READY → 已就绪；
- BLOCKED → 受阻；
- PENDING → 待处理；
- HOLD → 暂缓。

如果它是实际机器值、日志内容、协议字段、测试输出或历史正式 verdict，则保留原值。例如：

```text
工作流 conclusion 为 `success`。
该历史 Gate 的正式 verdict 为 `PASS`。
```

不要为了“看起来像工程状态”把普通中文状态重新写成大写英文。

## 7. 标题、表格、列表和流程图

普通结构性标题优先中文：

推荐：

```text
## 人工介入边界
## 主要责任
## 退出条件
```

不推荐：

```text
## Human escalation
## Primary responsibility
## Exit Conditions
```

表格列名、列表中的动作和流程图节点同样遵守该原则。节点本身是 Skill 名、命令、文件或外部正式名称时保留原样。

## 8. Agent 会话与协作输出

Agent 面向用户的以下内容默认使用中文：

- 分析和判断；
- 进度更新；
- 规划候选；
- 风险和阻塞；
- 验证结果；
- Review 结论；
- 需要人工决定的事项。

输入材料或工具输出使用英文时，先理解其含义，再用中文说明；必须逐字引用的部分与自己的判断分开。

## 9. Issue、PR、Review 与 Commit

当前仓库的 Issue、PR、Review 和状态说明默认使用中文叙述；精确路径、SHA、Rule / Skill id、workflow 名称等保持原样。

Git Commit 另受 `rule:git-commit-discipline` 约束。固定的 `type(scope)` 是协议结构，摘要使用自然中文。

## 10. 既有内容怎样收敛

语言复查不是机械全局翻译。遇到英文时先分类：

- 普通叙述 → 中文化；
- 机器标识 → 保留；
- 外部正式名称 → 按识别需要保留；
- 正式概念身份 → 先确认 canonical owner，再决定表达；
- 历史 Evidence 中的正式 verdict / 原始输出 → 保留历史值；
- 已关闭历史材料 → 只有仍影响当前理解或会制造语义冲突时才修订。

如果语言问题同时暴露真实语义冲突，应回到对应 Authority 解决，不能用翻译代替语义决策。

## 11. 复核清单

复核一段面向人的内容时，至少检查：

1. 去掉必须保留的精确标识后，中文是否已经能完整表达结论？
2. 每个保留的英文对象是否确实承担机器身份、外部正式名称或必要的概念身份？
3. 普通动作、判断、因果和状态是否仍被英文短语替代？
4. 标题、表格、列表和流程节点是否可以直接用中文表达？
5. 人工状态是否误写成了非必要的大写英文值？
6. 中文化是否错误合并了不同 Method stage、Gate、artifact、Skill、Rule 或 Architecture？
7. 是否因为历史文档、工具输出或输入资料的语风而扩散英文？
8. 人工是否能够连续阅读，而不需要频繁在两种语言之间切换？

只要英文没有承担精确身份、正式名称或必要对照作用，就优先使用自然中文。
