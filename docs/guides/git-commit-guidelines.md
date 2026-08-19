# Git Commit 提交规范

**状态：** Baseline v0.1  
**性质：** 规范性文档

## 1. 目标

本规范用于统一 `agentic-dev` 仓库的 Git Commit Message，确保提交历史能够：

- 清晰表达每次变更的主要目的；
- 支持 Human 与 Agent 在 Fresh Context 中快速理解仓库演进；
- 区分 Method、Skill Contract 与 Skill Implementation 的变化；
- 避免一个提交混合多个不同层级的目的；
- 为后续 Release、Review 和问题追溯提供稳定语义。

## 2. 基本格式

统一采用：

```text
<type>(<scope>): <中文摘要>
```

其中：

- `type` 使用小写英文；
- `scope` 使用小写英文；
- 摘要使用中文；
- 摘要应直接说明本次提交的主要动作和对象；
- 默认不在摘要末尾添加句号。

示例：

```text
docs(method): 建立 AI 开发方法基线
feat(skills): 实现 clarify-intent Skill
fix(skills): 修正 execute-unit 验证退出条件
refactor(skills): 简化上下文加载逻辑
test(skills): 增加 specify Skill 契约验证
chore(repo): 调整仓库基础配置
```

## 3. Type

第一版统一使用以下类型。

| Type | 用途 |
|---|---|
| `docs` | 方法、规范、架构、契约、研究记录等文档变更 |
| `feat` | 新增可实际使用的 Skill、Capability 或运行能力 |
| `fix` | 修复 Skill、脚本、配置或方法实现中的错误 |
| `refactor` | 重构实现或结构，但不改变既定外部语义 |
| `test` | 新增或调整验证用例、Skill 测试、契约测试 |
| `chore` | 仓库维护、配置、目录整理等非功能性变更 |

只有出现明确需要时，再增加新的 Type。

不要为了“看起来更完整”预先引入大量暂时用不到的 Conventional Commit 类型。

## 4. Scope

Scope 表示稳定的责任域，不表示具体文件名、文件路径、目录名称或单个 Artifact 类型。

同一次逻辑变更即使同时修改 README、Guide 或其他不同位置的文件，也应根据**变更目的所属的稳定责任域**选择 Scope，而不是跟随被修改文件的位置命名 Scope。

当前推荐：

| Scope | 用途 |
|---|---|
| `method` | AI 开发方法、顶层原则、阶段定义 |
| `contracts` | Skill Contract 与职责边界 |
| `skills` | Skill 实现及其直接相关内容 |
| `usage` | `agentic-dev` 使用方式、Operating Guide、Consumer 启动与协作指导 |
| `research` | 外部项目研究、对照分析 |
| `governance` | Repository Rules、Authority、治理规则 |
| `tasks` | Task 管理与工作协调规则 |
| `repo` | 仓库结构、配置、基础维护 |

示例：

```text
docs(method): 明确 Technical Planning 按需触发规则
docs(contracts): 完善 readiness-check 输入输出契约
docs(usage): 明确 Consumer 需求权威采纳边界
docs(research): 补充 Superpowers 执行模型分析
docs(governance): 增加 Git Commit 提交规范
feat(skills): 实现 specify Skill
chore(repo): 调整目录结构
```

如果现有 Scope 已能准确表达责任域，不要为单个文件、目录或一次性概念新增 Scope。

## 5. 摘要规则

摘要应：

- 使用中文；
- 以明确动作开头；
- 说明主要修改对象；
- 避免泛化描述；
- 保持简短但具有独立可读性。

推荐动词：

```text
建立
新增
补充
明确
调整
更新
修正
统一
重构
移除
简化
完善
```

推荐：

```text
docs(method): 明确 Fresh Context 的逻辑定义
docs(contracts): 调整 execute-unit 的验证退出条件
feat(skills): 实现 systematic-debug Skill
```

不推荐：

```text
docs(method): 更新文档
docs: 修改内容
feat: 增加功能
chore: 一些调整
```

## 6. 单一变更目的

一次 Commit 应只表达一个主要目的。

可以包含为完成该目的所必需的多个文件修改，但这些修改必须属于同一个逻辑变更。

例如，以下内容可以放在一个 Commit 中：

```text
docs(governance): 建立 Git Commit 提交规范
```

同时修改：

- `docs/guides/git-commit-guidelines.md`
- `AGENTS.md`
- `README.md`

因为它们共同完成“建立提交规范”这一单一目的。

以下内容原则上应拆分：

```text
docs(contracts): 调整 execute-unit 契约
feat(skills): 实现 execute-unit Skill
```

原因是前者改变权威契约，后者实现该契约。

## 7. Method / Contract / Implementation 分层提交

仓库采用以下权威关系：

```text
Method
  ↓
Skill Architecture
  ↓
Skill Contract
  ↓
Skill Implementation
```

Git Commit 应尽量保持同样的演进顺序。

如果 Skill 实现暴露出方法或契约问题，应：

1. 先修改对应 Method / Architecture / Contract；
2. 单独提交权威层变更；
3. 再修改 Skill Implementation；
4. 再单独提交实现变更。

示例：

```text
docs(contracts): 调整 execute-unit 的验证退出条件
```

随后：

```text
refactor(skills): 对齐 execute-unit 新验证契约
```

禁止只修改 `SKILL.md`，使 Skill Implementation 在事实上改变方法或契约语义。

## 8. Commit 前检查

提交前至少检查：

- 本次提交是否只有一个主要目的；
- `type` 是否准确；
- `scope` 是否属于稳定责任域；
- 中文摘要是否能独立说明变更；
- 是否把 Method / Contract Change 与 Skill Implementation Change 混在一起；
- 是否包含无关临时文件、生成物或调试内容；
- 当前工作是否已达到适合提交的稳定状态。

如果仓库存在对应 Build / Test / Validation Command，应在提交前按当前变更风险执行必要验证。

“准备提交”本身不构成完成证据；验证仍应遵守仓库的 Evidence Before Claims 原则。

## 9. Commit Body

普通提交默认不要求 Body。

只有在摘要无法清楚表达以下信息时才增加 Body：

- 为什么必须这样修改；
- 重要 Trade-off；
- 非显而易见的兼容性影响；
- 后续必须注意的迁移事项。

Body 应解释 **why** 和重要约束，不要简单重复 diff。

示例：

```text
docs(contracts): 调整 readiness-check 的职责边界

将 Artifact 修正从 readiness-check 中移除，使其保持只读检查职责。
实际修正由对应 Workflow Skill 或 Human 决定，避免 Checker 静默改写权威产物。
```

## 10. Breaking Change

当前仓库主要处于方法与 Skill 建设阶段。

如果未来对已经公开稳定的 Skill Contract、CLI Interface 或其他对外能力产生 Breaking Change，应采用 Conventional Commits 的显式 Breaking Change 表达方式，例如：

```text
feat(skills)!: 调整 execute-unit 输入契约
```

必要时在 Body 中增加：

```text
BREAKING CHANGE: ...
```

在第一版 Skill 稳定发布之前，不应滥用 Breaking Change 标记来描述普通设计迭代。

## 11. Merge / Release

本规范只定义 Commit Message。

以下事项由独立 Repository Policy 或 Human Authority 决定：

- Merge Strategy；
- Pull Request Title；
- Squash Policy；
- Tag；
- Release Version；
- Push；
- Deploy。

通用 Skill 不得仅依据本规范自行执行这些共享状态变更。

## 12. 当前基线的推荐初始提交

如果使用当前 Baseline 初始化新仓库，推荐：

```text
docs(method): 建立 AI 开发方法基线
```

如果仓库初始化动作本身需要独立记录，也可以使用：

```text
chore(repo): 初始化 agentic-dev 仓库
```

方法文档本身仍建议作为独立的 `docs(method)` 提交语义。
