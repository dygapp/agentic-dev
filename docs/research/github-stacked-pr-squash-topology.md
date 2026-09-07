# GitHub Stacked PR + Squash Merge 集成拓扑研究

## 研究目的

为 Issue #69“Squash Merge 下 Stacked PR 集成拓扑安全 v1”提供当前平台证据，判断 Issue #33 中历史 Consumer 故障应如何映射到 GitHub 当前能力。

本文属于研究材料，不直接定义方法、架构、技能契约或使用方仓库策略。

## 证据日期

2026-09-07。

## 既有 Consumer 证据

Issue #33 已独立核验以下历史事实：

- `dygapp/jilinjobs-cms` 曾使用普通依赖式 PR 链进行分层审查；
- 父层通过 squash merge 集成后，下游 branch 仍保留未 squash 的审查 ancestry；
- 原 PR #38 最终显示 48 个 changed files，而规范化后的替代 PR #39 只包含 2 个职责文件；
- 原 PR #37 最终显示 58 个 changed files且未合并，而规范化后的替代 PR #40 只包含 13 个职责文件；
- Head 规范化后重新取得当前证据；
- 该风险被独立分类为 `Low / Future Improvement Candidate`，不支持禁止 stacked PR，也不支持修改核心方法、技能契约或新增 Skill。

该证据证明普通手工依赖 PR 链在 squash merge 后可能出现审查 ancestry 与最终集成 ancestry 分离，但不证明 GitHub 当前所有 stacked PR 模式都具有同一故障路径。

## GitHub 当前官方证据

### 1. 原生 stacked pull requests 已成为平台能力

来源：

- https://docs.github.com/en/pull-requests/get-started/about-stacked-prs
- https://docs.github.com/en/pull-requests/reference/stacked-pull-requests

当前文档明确：

- stacked pull requests 处于 **public preview**，行为可能继续变化；
- 一个 stack 是同仓库内的 PR 依赖链，底层 PR 指向 trunk，其余 PR 逐层指向下层 branch；
- GitHub CLI、GitHub website、GitHub Mobile 与程序化 API 均可识别 stack；
- 原生 stack 的 required reviews、required checks、CODEOWNERS 与 GitHub Actions 以 stack trunk 为统一基准评估，而不是只按每层直接 base branch 处理；
- stack 必须保持层间线性历史。

### 2. 原生 stack 对 squash merge 有专门语义

来源：

- https://docs.github.com/en/pull-requests/reference/stacked-pull-requests
- https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-stacked-pull-requests

当前文档明确：

- 原生 stack 支持 merge commit、squash、rebase 三种 merge method；
- 使用 squash 时，每个 PR 层形成一个独立的 squashed commit；
- stack 从 bottom 向上集成，可以一次合并从最低未合并层开始的连续一组 PR；
- 底层或连续下层完成集成后，剩余上层 PR 会自动 rebase / retarget 到 stack trunk，使下一层成为新的底层；
- 如果 stack 因 trunk 前进或下层变化失去线性历史，GitHub 要求 cascading rebase，可通过 `gh stack rebase` / `gh stack push` 或网站上的 `Rebase stack` 恢复。

因此，Issue #33 中“父 PR squash 后 child 仍需人工规范化并可能产生旧 PR 快照”的故障路径，**不能直接视为 GitHub 当前原生 stack 的标准行为**。

### 3. 普通 PR 的 squash merge 仍可能保留旧 branch ancestry

来源：

- https://docs.github.com/en/pull-requests/reference/pull-request-merges

GitHub 对普通 PR 的 squash merge 会把 PR 中的提交合并成 base branch 上的一个新提交；官方文档同时明确指出，如果继续在同一 head branch 上工作，后续 PR 可能重新包含已经被 squash 到 base branch 的提交。

这个平台事实与 Issue #33 的历史 Consumer 现象方向一致：当依赖 PR 链**没有被 GitHub 原生 stack 生命周期接管**时，不能假设 squash merge 会自动把 child branch 的 Git ancestry 改写成最终集成 ancestry。

### 4. 普通 PR 的 base / head 变化会影响审查快照

来源：

- https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/changing-the-base-branch-of-a-pull-request
- https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch

当前文档明确：

- PR 比较的是 head branch 与 base branch；
- 修改 base branch 可能使部分 commits 从 timeline 消失，也可能让已有 review comments 变为 outdated；
- 更新 PR branch 可以通过 merge base 或 rebase 到最新 base；
- branch 更新是新的仓库状态，不能沿用旧 Head 的验证声明。

最后一点“不能沿用旧 Head 的验证声明”由 `agentic-dev` 当前证据规则提供，不是 GitHub 文档直接定义。

## 模式分类

### 模式 A — GitHub 原生 stack

识别条件：GitHub 将相关 PR 识别为同一 stack，存在 stack metadata / stack map / stack merge requirements，或使用 `gh stack` / 对应平台操作管理其生命周期。

安全含义：

- 优先遵循 GitHub 当前 stack merge / rebase 语义；
- 不需要把 Issue #33 的人工 branch normalization 路径机械复制到原生 stack；
- 进入集成决策前仍必须读取实际 stack / PR 状态、Head、diff、checks 与当前证据；
- 因功能仍处于 public preview，不能把具体 UI、CLI 子命令或自动重写行为提升为长期不变的方法契约。

### 模式 B — 普通手工依赖 PR 链

识别条件：PR 只是通过 branch base 形成依赖关系，但没有当前证据证明平台把它们作为原生 stack 管理。

安全含义：

- 审查拓扑只表示审查依赖，不自动等于最终集成拓扑；
- 父层 squash merge 后，应重新读取 trunk、child branch、PR base / Head / diff；
- 如果 child 仍携带已集成父层 ancestry，应先规范化 / rebase / rebuild 到实际集成基线，再决定是否继续使用原 PR；
- branch rewrite、rebase、rebuild、force-update 或 PR 替换后，旧 Head 的当前证据不得自动复用；
- 如果 GitHub PR 快照无法可靠证明当前 Head 与职责 diff，应停止该 PR 的集成并创建或使用可验证的干净载体，而不是对语义不明的旧快照继续合并。

## 架构适配判断

当前证据支持的最小长期落点是：

- `docs/guides/external-operation-guidelines.md` 的 GitHub / 外部状态验证指导；
- 必要时由项目级评估验证该指导。

当前证据**不支持**：

- 修改核心方法；
- 修改技能契约；
- 新增 Skill；
- 规定统一分支策略；
- 规定所有使用方必须使用 GitHub 原生 stack；
- 禁止普通 stacked / dependent PR。

## 研究结论

Issue #33 的历史风险仍成立，但它现在必须被更精确地表述为：

> 在 squash merge 场景中，Agent 不能仅凭“这些 PR 曾以依赖链方式审查”推断审查拓扑会自动成为最终集成拓扑。必须先判断当前依赖链是否由 GitHub 原生 stack 生命周期管理；原生 stack 按当前平台 stack 语义验证和集成，普通手工依赖 PR 链则必须在每次父层集成或 Head 变化后重新建立可验证的集成拓扑与当前证据。

这是一条平台 / 外部操作安全边界，而不是新的方法阶段或仓库级分支策略。
