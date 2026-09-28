---
id: guide:git-commit-conventions
type: guide
status: active
---

# Git Commit 方法与常用约定

本文帮助普通软件 Consumer 在没有更具体方法入口时组织有界、可复核的 Git commit，并为希望采用 `<type>(<scope>): <summary>` 的项目提供可裁剪基线。它不是 Consumer 的提交 Authority，也不要求所有项目采用同一种格式；当前 Repository 已有的 commit policy、自动化配置和 Human Authority 始终优先。

## 1. 先恢复当前项目规则

提交前先确认：

- 当前操作的 Git Repository、top-level、branch、HEAD 与 working tree；
- 根或 scoped `AGENTS.md` 中的提交、验证和授权约束；
- Consumer-local commit guideline、commit template、hook、lint 或 release 配置；
- 当前变更真正允许提交、推送和集成到什么边界。

没有本地格式规范时，可以把本文的常见格式作为候选，但不能因为安装了 Skills 或读过本 Guide，就把候选自动提升为 Consumer policy。需要形成长期统一约定时，由 Consumer 把采用后的规则写入自己的 Current owner。

## 2. 一个 commit 表达一个主要逻辑目的

提交边界按可解释的逻辑目的划分，而不是机械按文件数、技术层或工具步骤切分。为完成同一目的必须同步变化的 Authority、实现、测试、迁移和必要文档可以进入同一 commit；无关修正、独立重构和顺手清理应拆开。

一个候选 commit 应能回答：

- 它完成或推进了什么单一目的？
- 每个 staged change 为什么属于这个目的？
- 移除其中任一变化后，目标、正确性或验证是否会不完整？
- 是否混入了可以独立理解、验证或回退的另一项变化？

commit 不要求与一次编辑、一次测试、一个 Execution Unit、一个 Issue 或一个 PR 一一对应。小型有界变更可以形成一个 commit；较大责任可以有多个可解释 commit，最终仍由 Consumer 的集成政策决定。

## 3. 提交闭环

按以下顺序形成提交：

1. 读取当前 Repository Authority 和本地 commit policy，确认提交权限与目标仓库。
2. 检查 branch、HEAD、staged、unstaged、untracked 和并发变化；多仓项目逐仓确认，不能用父仓干净状态替代组件仓检查。
3. 选定本次 commit 的单一逻辑目的，只暂存属于该目的的文件或 hunk，不用无边界 `add`、清理或历史改写掩盖未归属变化。
4. 检查 staged diff、文件状态和必要生成物，确认没有 secret、调试产物、临时日志、无关格式化或其他 owner 的修改。
5. 运行与本次声明匹配的验证，并确认实际验证输入与准备提交的 subject 一致。若 unstaged 内容影响了构建或测试，不能把该结果直接描述为候选 commit 的证据。
6. 按当前项目格式编写 message；需要 body、footer、Issue 关联或 breaking 标记时遵守本地 policy。
7. 创建 commit 后重新读取 HEAD、commit diff 和 working tree，确认实际提交内容、message 与预期一致。
8. push、创建 PR、merge、release 和历史改写是后续独立操作；commit 成功不自动授予这些权限。

未提交 diff 和本地验证可以是当前执行态证据；需要跨上下文长期恢复的结论，应进入 Consumer 认可的 Repository / GitHub 状态。commit 本身也不证明构建、测试或 Review 已通过。

## 4. 可选的 message 基线

希望采用紧凑、机器和人都容易识别的格式时，可以从以下形态开始：

```text
<type>(<scope>): <summary>
```

`scope` 可选：

```text
<type>: <summary>
```

这只是可采用的基线，不等于完整采用任何外部提交标准。大小写、语言、长度、body / footer、breaking marker 和 Issue 关联方式均由 Consumer 自己确定。

### 常用 type

| type | 适用边界 |
|---|---|
| `feat` | 增加或扩展对用户、调用方或运营可观察的能力 |
| `fix` | 修复已存在的错误行为、回归或缺陷 |
| `docs` | 只改变文档、示例或说明，不改变运行行为 |
| `refactor` | 调整实现结构，预期不改变外部行为，也不以修复缺陷为主要目的 |
| `test` | 新增或调整测试、fixture 或测试基础设施，主要实现行为不变 |
| `perf` | 以性能改善为主要目的，并保持声明的行为 contract |
| `build` | 修改构建系统、依赖解析、打包或产物生成 |
| `ci` | 修改 CI workflow、自动化验证或相关运行配置 |
| `chore` | 必要维护工作，且没有更准确的 type；不应成为含糊变化的默认收纳箱 |
| `revert` | 明确撤销一个或一组既有提交，并保留可恢复的撤销对象 |

项目不需要为了“完整”启用全部 type，也可以基于真实发布、changelog 或工程需要增删。type 的定义一旦成为项目政策，应保持稳定；不要让同类变化在 `fix`、`chore`、`refactor` 之间随意漂移。

### scope 选择

scope 表示当前项目中稳定、可识别的主要影响范围，通常来自：

- 产品域或业务能力，例如 `auth`、`billing`；
- 应用或运行面，例如 `api`、`web`、`worker`；
- 稳定 package、模块或组件名；
- 工程责任面，例如 `db`、`ci`、`deps`。

这些名称只是示例，不是中央 scope 清单。选择 scope 时：

- 使用 Consumer 已有词汇和稳定边界；
- 优先一个最能解释主要目的的 scope；
- 跨多个范围且没有可靠主范围时省略 scope，而不是写 `misc`、`all` 或临时组合；
- 不使用文件名、人员名、临时 branch、Issue 编号或会快速失效的组织结构充当长期 scope；
- monorepo 可以采用稳定 workspace / package 名，但必须与项目实际发布和维护边界一致。

### summary、body 与 breaking change

summary 应准确说明主要动作，避免“update files”“misc fixes”等无法恢复目的的文字。使用何种语言、是否使用祈使句、是否加句号，由 Consumer 的语言政策决定。

当标题不足以解释原因、迁移方式、风险或验证边界时，在 body 中补充必要上下文；不要把完整实施日志复制进 message。

只有公开 contract、持久数据、调用方式或兼容承诺确实发生不兼容变化时才使用 breaking 标记，并说明受影响对象和迁移方式。普通内部整理、文件移动或大 diff 不等于 breaking change。

## 5. Consumer 怎样持有这套政策

载体与复杂度匹配：

- 只有几条稳定的全仓规则时，可直接放在根 `AGENTS.md`；
- type、scope、breaking、示例和例外较多时，使用 Consumer-local guideline，例如 `docs/constraints/git-commits.md`，并由根入口或 constraint locator 指向它；
- path / package 有额外要求时，使用 nested `AGENTS.md` 或宿主原生 scoped instructions；
- commitlint、hook、release 配置等机器规则可以拥有可执行格式和值域，guideline 解释选择语义并指向真实配置。

不要在 `AGENTS.md`、guideline、commit template 和 lint 配置中分别维护会漂移的 type / scope 清单。确定一个 Current owner，其他位置只做 locator、解释或可再生投影。

## 6. 最小采用方式

Consumer 可以从以下最小政策开始：

```md
## Git Commit

- 一次提交只表达一个主要逻辑目的，不混入无关变化。
- 提交信息使用 `<type>(<scope>): <summary>`；scope 不明确时省略。
- type 使用当前项目已采用的稳定集合；scope 使用当前项目真实模块或领域名。
- 提交前检查 staged diff 并运行与当前声明匹配的验证。
- commit 不自动授权 push、PR、merge、release 或历史改写。
```

只有真实协作、发布或自动化需求证明必要时，再扩展 type、scope、body / footer 或机器校验。项目没有一致性需求时，不必为了采用本 Guide 创建独立 guideline 或新增工具。
