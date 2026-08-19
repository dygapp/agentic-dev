# 术语表达规范

本文规定 `agentic-dev` 中文主导文档中英文术语的呈现方式，目标是在保留方法与技术术语精确性的同时，降低人工复核（Human Review）的阅读负担。

本文属于项目级文档治理，不重新定义方法（Method）、架构（Architecture）、契约（Contract）或 Skill 的语义。术语含义发生冲突时，仍以对应仓库权威（Repository Authority）为准。

## 1. 适用范围

本规范适用于 `agentic-dev` 中面向人阅读的：

- `AGENTS.md`、`README.md`；
- Method / Architecture / Contract / Decision 文档；
- 使用指南（Operating Guide）与其他 Guide；
- Research、Plan 及其他说明性 Markdown；
- PR、Issue 等需要长期阅读的项目说明。

代码标识符、文件名、路径、命令、API 参数和外部系统固定值不受自然语言翻译要求约束。

Consumer 项目使用什么主导自然语言，由 `docs/guides/using-agentic-dev.md` 中的语言选择规则和 Consumer Repository Authority 决定；本文只规定 `agentic-dev` 自身及采用本规则的项目如何呈现术语。

## 2. 核心原则

### 2.1 中文主述，英文用于精确锚定

当前仓库的人类可读文档以中文作为主要叙述语言。

优先写成自然中文句子，只在以下情况下保留英文：

- 英文是稳定的方法术语或技术术语；
- 英文需要与 Skill、Contract、文件、外部规范或生态概念精确对应；
- 中文翻译不稳定、容易失真或反而增加理解成本；
- 英文本身就是固定名称、状态或标识符。

不要为了显得“技术化”而在中文句子中堆叠可直接用中文表达的英文词汇。

### 2.2 首次解释，不重复注释

当一个英文概念值得保留，且存在自然、稳定的中文表达时，在文档中的首次重要出现位置优先采用：

```text
中文表述（English Term）
```

例如：

```text
执行单元（Execution Unit）应能够独立验证。
当前证据（Current Evidence）必须支持完成声明。
事实来源（Source of Truth）应在修改后重新读取。
```

后续出现默认使用更自然的中文或已明确的英文简称，不要求每次重复中英对照。

### 2.3 英文是固定名称时，可用英文主词并补中文解释

当英文名称本身需要保持稳定，或者直接翻译会削弱与代码、Skill、状态值或方法定义的对应关系时，可以采用：

```text
English Term（中文解释）
```

例如：

```text
Fresh Context（与未持久化历史推理隔离的新上下文）
Ready to Integrate（已具备进入集成决策的条件）
Skill Contract（Skill 的职责与输入输出契约）
```

括号中的中文用于帮助理解，不应被当作新的正式 Method 定义。

### 2.4 固定标识符保持原样

以下内容默认保持原生形式，不强制翻译：

- Skill 名称，如 `clarify-intent`、`execute-unit`；
- 文件名和路径；
- Branch、Commit、PR、Issue 标识；
- API、CLI、命令和参数；
- 代码标识符；
- 外部规范、产品和协议的正式名称；
- 必须精确匹配的状态值或枚举值；
- 错误信息与需要原样引用的输出。

## 3. 三种表达方式的选择

根据术语性质选择最自然的方式，不要求整个仓库机械使用单一格式。

| 场景 | 推荐方式 | 示例 |
|---|---|---|
| 中文已有自然稳定表达，英文需要精确对应 | 中文（英文） | 执行单元（Execution Unit） |
| 英文本身是固定名称，中文只是辅助理解 | 英文（中文解释） | Fresh Context（隔离的新上下文） |
| 固定标识符或无需翻译的通用名称 | 直接保留英文 | `execute-unit`、GitHub、API |
| 普通叙述概念，不需要英文锚定 | 直接中文 | 验证失败后重新分析 |

选择标准依次是：

1. 是否容易被人正确理解；
2. 是否保持与 Repository Authority 的精确对应；
3. 是否避免重复和视觉噪声；
4. 是否有利于 Fresh Agent 在跨文档工作时识别同一概念。

## 4. 轻量术语表的使用

当一组核心术语在多个文档中高频出现，且容易因为翻译差异造成理解偏差时，可以维护轻量术语表。

术语表用于统一**表达方式**，不承担重新定义概念语义的职责。

推荐记录：

- 稳定英文术语；
- 推荐中文主述或中文解释；
- 必须保留英文的场景；
- 对应语义权威文档的引用。

不应：

- 为每个英文词建立条目；
- 把通用技术名词全部翻译；
- 在术语表中复制 Method / Contract 的完整定义；
- 为了词汇表完整性创造仓库从未实际使用的术语。

只有实际出现跨文档歧义或重复解释成本时，再增加正式术语条目。

## 5. 写作示例

不推荐：

```text
Agent 在 Fresh Context 中 execute 一个 Execution Unit，并生成 Verification Evidence，然后进入 Converge。
```

推荐：

```text
Agent 在 Fresh Context 中执行一个执行单元（Execution Unit），形成验证证据（Verification Evidence）后，再进入 `converge` 对应的整体收敛工作。
```

不推荐：

```text
执行单元（Execution Unit）完成后，执行单元（Execution Unit）必须提供当前证据（Current Evidence），当前证据（Current Evidence）再进入收敛（Converge）。
```

推荐：

```text
执行单元（Execution Unit）完成后必须提供当前证据（Current Evidence），再进入整体收敛。
```

核心目标是减少不必要的语言切换，而不是消灭英文术语。

## 6. 标题、表格与列表

标题应优先使用中文表达主题；只有英文名称本身是正式对象时才保留英文。

推荐：

```text
## 人工介入边界
## Fresh Context 使用规则
## Skill Contract 对齐检查
```

不推荐为了双语对称把所有标题写成：

```text
## Human Intervention Boundary（人工介入边界）
```

除非英文名称本身需要作为跨文档检索锚点。

表格和列表同样遵循“中文主述、必要时保留英文锚点”，不要让双语重复显著增加扫描成本。

## 7. 既有文档的收敛方式

本规范首次引入时，对高频入口和直接治理文档做一次首轮统一收敛：

- `AGENTS.md`；
- `README.md`；
- `docs/guides/` 下全部文档。

首轮收敛只调整术语呈现、标题和说明性措辞，不借机改变 Method、Contract、Skill 或其他既有治理语义。

完成首轮收敛后：

- 新增文档应直接遵守本规范；
- 其他既有文档在实际修改时，在当前修改范围内顺带收敛明显的中英文混用；
- 不要求为了术语形式统一立即重写 Method、Architecture、Contract、Research、Skills 等全部旧内容；
- 不创建只有语言替换、没有实际阅读价值的大规模 diff；
- 如果发现术语背后存在真实语义不一致，应单独按对应 Method / Contract / Governance 流程处理，而不是用翻译调整掩盖。

原则：

> 高频入口先统一，其他旧内容按触达逐步收敛。

## 8. 与其他规则的关系

- `docs/guides/using-agentic-dev.md` 决定 Consumer 在缺少显式规则时如何选择项目主导语言；
- 本文决定中文主导文档中英文术语如何呈现；
- `docs/guides/external-operation-guidelines.md` 约束 PR、Issue、Review Comment 等外部协作内容的工作语言一致性；
- Method / Architecture / Contract 文档仍决定术语的正式语义；
- Skill、代码和固定标识符保持其原生名称。

如果表达可读性与语义精确性发生冲突，优先保证语义不失真，再通过括号解释、上下文说明或权威引用改善可读性。
