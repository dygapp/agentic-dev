---
id: guide:multi-repository-projects
type: guide
status: active
---

# 多仓库软件项目

本文帮助人和 AI 组织同一个软件项目中的多个独立 Git Repository。它只提供布局选择、权威边界和工作导航；具体项目事实、仓库身份、权限与集成政策由 Consumer 自己拥有，执行时仍使用当前责任适用的 installed Skills。

## 1. 何时采用嵌套独立仓库

当项目级 Requirement、Architecture、current work 或集成决定需要稳定的共同 owner，而多个组件又需要独立的 Git 历史、验证和集成周期时，推荐考虑以 Project Repository 为工作区根目录、在其下放置独立 Component Repositories：

```text
project/                    # Project Repository / Workspace Root
├── .git/
├── .gitignore
├── AGENTS.md
├── docs/                   # Consumer 自己选择的项目级 Authority / current work
├── .agents/skills/         # 如需项目级 installed Skills
├── backend/                # 独立 Git Repository
│   ├── .git/
│   └── AGENTS.md
└── public-web/             # 独立 Git Repository
    ├── .git/
    └── AGENTS.md
```

这是**推荐但非必选**布局，不是 Skill 安装、普通软件开发或多仓项目的前置条件。已有项目可以保留非 Git 工作区加并列仓库，或在确实需要父仓提交天然固定组件 gitlink 时选择 Git submodule。目录嵌套只方便共同工作区与项目级入口，不把多个 Git Repository 合并为一个 Authority 或权限域。

## 2. 长期事实由谁拥有

| 责任 | 通常的 owner |
|---|---|
| 跨组件的项目目标、Requirement、系统级 Architecture、共同 current work 与集成结论 | Project Repository 中 Consumer 指定的 Current Authority / state owner |
| 组件实现、组件局部 Architecture / policy、代码、测试、仓库 CI 与 Git 生命周期 | 对应 Component Repository |
| 组件路径、仓库身份、角色及必要的恢复入口 | Consumer 项目级拓扑说明；可以先是简短的人可读 locator |
| 当前 checkout、未提交差异、本地验证与运行中的服务 | 当前工作区执行态，不自动成为长期项目事实 |

项目级事实不因物理位置自动覆盖组件仓的本地执行政策；组件仓也不能单方面改写共同产品或跨组件 contract。两侧内容冲突或 owner 不明且影响当前结论时，先返回对应 Consumer owner 澄清，不按“父目录优先”或“更近文件优先”猜测语义权威。

Project Repository 的根 `AGENTS.md` 保持薄入口，指出项目级事实、组件拓扑和约束从何恢复。每个 Component Repository 自己的 `AGENTS.md` 指向该仓本地事实、installed Skills 与约束。宿主是否自动加载父级 instructions 或发现项目根 Skills 取决于实际 Runtime；切换仓库时要核验，不能把路径嵌套当作自动继承。凭证、secret、cache 和 session 不因工作区共享而进入版本化项目事实。

## 3. 跨仓 Fresh Context 与执行

从项目级任务进入组件仓时，先从项目 Current Authority 确认受影响的组件和共同目标，再逐仓核对实际路径、Git top-level、仓库身份、branch / HEAD / working tree、`AGENTS.md`、当前适用 Authority、local constraints、installed Skills 与权限。只加载当前责任需要的仓库；组件缺失、身份或 remote 不符、locator 损坏时，只阻断受影响的执行或完成声明，不以同名目录代替目标仓库。

跨仓工作按实际责任切分，不规定一个 Repository 必须对应一个 Execution Unit，也不因为跨仓就自动建立 Unit。局部、低风险、可逆且不需要独立生命周期的变更仍可直接实施；需要独立恢复、依赖协调或独立验收时使用现有 `slice-work`、`readiness-check`、`execute-unit`。项目级 Specification 或 Work 记录共同目标与依赖，组件仓保存本地实现和验证证据；`readiness-check` 在正式 Unit 执行前核对受影响仓库身份及逐仓实施、验证边界，最终用 `converge` 检查跨组件接缝。项目仓忽略的组件目录不会出现在根仓普通 Git 状态中；项目级完成判断和独立变更复核须按已知拓扑分别核对工作区内组件仓的 Git 状态，不能把根仓干净或根仓 PR diff 当作所有代码已提交的证据。每仓的 commit、PR、CI、merge 仍由其自己的 Authority 决定，某仓授权不传递给另一仓。

## 4. 何时记录精确组合

Project Repository 的提交不会记录被忽略的独立组件仓当前 SHA。因此，跨仓集成验证、可重建候选或发布声明需要明确其实际 subject：项目仓身份与 SHA、参与组件仓的身份与 SHA、验证所用配置，以及证据位置。未提交差异可以作为当前执行态证据；若声明要求日后按精确版本重建，就应先形成可恢复的提交或明确保留未完成的重建缺口，不能把工作区快照误称为 durable baseline。

各组件分别集成后，重新读取最终 HEAD 并核对组合；候选组合的验证不自动证明不同的最终组合通过。Project CI 或 Fresh Review 只有按所声明的仓库身份与精确版本重建、并取得与 claim 匹配的证据，才能支持跨仓 PASS。普通单仓修改不必每次生成全量项目 baseline。

拓扑和精确组合需要可恢复，但这不要求普通项目默认建立 `repositories.yaml`、固定 baseline schema 或 bootstrap orchestrator。只有重复的自动 checkout、CI 或环境重建确实需要机器消费时，才由 Consumer 选择最小格式并验证身份、完整性与漂移。

## 5. Commit 生命周期与历史收敛

跨仓工作不建立一个“项目级全局 commit”。Project Repository 和每个独立 Component Repository 都按各自 Current Authority 决定 commit policy，并分别经历 Working State → Candidate Commit → Durable Integration History。Execution Unit、Readiness、测试轮次、debug / Review 修复轮次本身不定义 commit 边界；具体提交按各仓真正的逻辑目的形成。

需要 exact-Head Evidence 时，各仓只在自身需要 durable subject 的边界形成 candidate。尚未共享且本仓允许历史整理时，同一逻辑目的的后续修复可以在该仓收敛进 candidate；不得从 Project Repository 对被忽略的组件仓执行统一 squash / rebase / amend，也不得把项目仓的授权外推给组件仓。一个跨仓 change 可以最终对应项目仓一个文档 / 集成逻辑 commit、若干组件仓各自的实现 commit，也可以只有部分仓发生 commit；数量由实际责任决定，不由仓库数量机械决定。

若 Consumer 选择 Git submodule，父仓 `160000` gitlink 本身就是显式版本绑定。组件仓 History Convergence 改变最终 SHA 后，父仓必须更新 gitlink 并重新判断依赖该组合的 Evidence；不能保留指向旧 candidate 的 gitlink，也不能因为父仓能够提交 gitlink 就推导出其拥有改写组件仓历史的权限。

如果完成声明依赖精确跨仓组合，History Convergence 后重新读取每个参与仓的最终 identity / SHA，再验证该组合。任一仓的 amend、rebase、squash 或其他 SHA 改写都会使旧组合中该成员失效；旧 CI / Review / Runtime Evidence 只有在当前 Evidence reuse policy 能证明差异不影响 claim 时才可复用。普通局部单仓变更不因此维护全项目 baseline。

## 6. 嵌套布局的 Git 安全

Project Repository 应以锚定路径在自己的 `.gitignore` 中忽略组件目录，例如 `/backend/`、`/public-web/`；这些路径由 Consumer 实际拓扑决定。建立或迁移时检查父仓索引没有组件文件或 `160000` gitlink。忽略规则不会移除已经跟踪的内容，也不能阻止显式强制暂存。

每次 Git 写操作先确认目标仓库的真实 top-level 与当前状态；不要从项目根目录对所有组件做无边界的 `add`、`clean`、reset 或其他批量变更。特别是强制清理可以触及被忽略的嵌套仓库；清理必须按明确 owner、精确目标和可恢复性另行授权。缺少组件目录、错误 remote、意外 gitlink 或当前工作区有未归属修改时，先停下受影响操作并恢复事实。

## 7. 采用与验证边界

已有项目不因采用本 Guide 自动搬迁仓库或重组 Authority。若选择嵌套布局，先确认共同项目事实确需独立 Project Repository，再建立最薄拓扑入口、各仓 Bootstrap 与忽略边界；之后用当前 Runtime 验证根与组件的 instruction / Skill 发现、仓库身份、组件缺失和错误 identity 的处理，以及跨仓候选和最终组合能否重建。

本 Guide 不提供通用跨仓 Runner、中央 registry、固定 Release / Gate 流程，也不替 Consumer 决定组件拆分、权限、CI 或迁移策略。实际 Runtime 与 Consumer adoption 的通过结论只能由对应当前证据支持。
