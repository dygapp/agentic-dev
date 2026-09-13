---
id: research:github-stacked-pr-squash-topology
type: research
status: active
---

# GitHub Stacked PR + Squash Merge 集成拓扑研究

**证据日期：** 2026-09-07  
**性质：** 非规范性平台研究

## 1. 研究问题

普通依赖式 PR 链在 squash merge 后可能出现“审查 ancestry”与“最终集成 ancestry”分离；但 GitHub 原生 stacked pull requests 已有自己的 stack lifecycle，因此不能把历史手工链故障机械推广到所有 stack。

## 2. Consumer 历史证据

Issue #33 曾观察到：父层 squash merge 后，下游普通 branch 仍保留未 squash 的 ancestry，导致旧 PR changed files 明显扩大；重新规范化 Head 后才恢复窄职责 diff。

该证据支持的结论是：普通手工依赖 PR 链不能假设 squash merge 会自动把 child branch ancestry 改写成最终集成 ancestry。

## 3. GitHub 官方证据

研究时 GitHub 文档显示：

- 原生 stacked pull requests 处于 public preview；
- stack 是同仓库线性 PR 依赖链；
- 原生 stack 对 required reviews/checks、stack trunk、cascading rebase 和 bottom-up merge 有专门语义；
- squash merge 时每层形成独立 squashed commit，剩余上层可按 stack lifecycle rebase / retarget；
- 普通 PR 的 squash merge 仍可能导致继续使用同一 head branch 时后续 PR 再次包含已 squash 的提交；
- 修改 base、rebase 或更新 head 会改变 PR 当前比较状态，必须重新读取实际 diff/checks/evidence。

来源包括 GitHub 关于 stacked PR、merging stacked PR、pull request merges、changing base branch 和 keeping a PR in sync 的官方文档。

## 4. 模式边界

### GitHub 原生 stack

只有当前平台事实明确证明相关 PR 正由原生 stack lifecycle 管理时，才按当前 GitHub stack 语义判断。由于该能力在研究时仍为 public preview，具体 UI/CLI/API 行为不是长期 Method contract。

### 普通手工依赖 PR 链

如果只是通过 branch base 形成依赖而没有原生 stack 证据：

- 审查拓扑不自动等于最终集成拓扑；
- 父层集成后重新读取 trunk、child branch、PR base/head/diff；
- child 若仍携带已集成父层 ancestry，需要先建立可验证的当前集成拓扑；
- rebase/rebuild/force-update/PR replacement 后，旧 Head 的验证证据不得自动复用。

## 5. V4 边界

该研究不支持新增方法阶段、统一分支策略、强制使用 GitHub 原生 stack 或禁止普通 dependent PR。

V4 的 `external-operation` / `review-change` 流程以及写后重新读取、evidence currentness、integration closure Rules 已覆盖通用运行约束；本文件只在 GitHub stacked/squash 拓扑本身成为当前任务事实时提供平台研究依据，不参与 ordinary Rule Discovery。

## 6. 结论

在 squash merge 场景中，不能仅凭“这些 PR 曾以依赖链方式审查”推断审查拓扑会自动成为最终集成拓扑。必须先识别当前平台管理模式，再以当前 trunk/head/diff/checks 建立证据。