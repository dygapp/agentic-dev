---
id: project:methodology-product-boundary-implementation-plan
type: project
status: active
---

# 方法论产品边界重构实施计划

## 1. 前置与目标

本计划只在以下前置成立后生效：

- 产品边界 Specification 已在 exact SHA `6eae3cf192c9ae67eed7f9d3e0aa33ef14d2c338` 完成 Fresh Independent Semantic Review，`Blocking=0`、`Medium=0`；
- Repository-wide disposition 已由 `docs/research/methodology-product-boundary-asset-disposition.md` 给出；
- 原 Issue #172 Gate H 保持终止，不修改真实 Consumer。

实施目标不是“给旧 Capability / Release Framework 换名字”，而是完成以下最终状态：

```text
agentic-dev Provider
  AGENTS.md + docs/** + tests/evals/tools
        ↓ design / validate
  skills/**                     ← canonical Consumer runtime product
        ↓ standard install

Consumer
  AGENTS.md                     ← Consumer-owned
  project docs                  ← Consumer-owned
  local constraints             ← Consumer-owned
  installed skills              ← agentic-dev product
  thin exact-version Guide locator
```

整个实施遵守**语义先迁移、旧 owner 后删除**，不允许先删 Method / Rule / Architecture 再依靠模型记忆补回。

## 2. 总体实施策略

采用单一隔离 implementation worktree / candidate branch。

默认：

- 不在真实 Consumer 上边做边试；
- 不建立新旧两套长期兼容层；
- 不 force-move 旧 RC tag；
- 不继续扩展 custom Release Builder；
- 不为了保持旧 tests 全绿而保留已被新目标明确替代的架构；
- 每个阶段都在同一最终候选上累积，最终以 exact-head deterministic + runtime + independent review 验收；
- 若为了 clean-checkout tests 必须产生本地提交，最终远端候选保持可审计的最小 coherent history，不把实验性中间状态作为正式 baseline。

## 3. Gate P1 — 标准 Skills Distribution 可行性验证

### 3.1 目的

在大规模改写前先证明最关键外部前提：

> canonical `skills/**` 可以直接通过 GitHub Repository / 明确版本被标准 Agent Skills 兼容安装路径使用。

### 3.2 验证场景

在 disposable fixture 中验证：

1. 从 Repository 当前候选安装全部或指定 Skills；
2. 从明确 Git ref / tag 安装或通过等价最小标准 Git pinning 路径得到同一 Skill 内容；
3. Codex native discovery 能发现安装后的 Skills；
4. 单个 Skill 安装时不会依赖 Provider `docs/**`；
5. update / reinstall 不覆盖 Consumer-owned 文件；
6. 无法精确确定版本时 fail closed，不静默安装 `latest`。

### 3.3 决策边界

若标准 Skills 工具原生支持所需 exact-ref 行为，直接采用。

若只支持 Repository URL、不直接暴露 exact-tag UX，允许使用**最薄 Git ref pinning / source selection**解决版本确定性，但不得恢复：

- semantic Release Build；
- 自定义 ZIP；
- Provider docs 编译；
- 自定义包管理协议。

### 3.4 Gate

P1 未证明前，不删除 Release Builder，也不大规模重写 15 个 Skill。

覆盖：`PB-AC-03`、`05`、`19`、`20`、`21`。

## 4. Gate P2 — Canonical Skills 重构

### 4.1 以 15 个现有 Skill 为产品基线

不先新增新 Skill。逐个处理：

- `activate-model-collaboration`
- `clarify-architecture`
- `clarify-intent`
- `converge`
- `establish-requirement-baseline`
- `execute-unit`
- `external-operation`
- `github-actions-verification`
- `human-review`
- `readiness-check`
- `review-change`
- `slice-work`
- `specify`
- `systematic-debug`
- `technical-plan`

### 4.2 每个 Skill 的迁移步骤

对当前 `agentic-dev-release-inputs` 中每个 Method / Architecture / Rule：

1. 判断该语义是否真的是 Skill 通用执行所需；
2. 是：写入 Skill body 或 Skill-local `references/**`；
3. 否：不因为历史 release-input 关系继续携带；
4. 删除 distribution / release-target / release-inputs 编译 metadata；
5. 确认 Skill 离开 Provider docs 后仍自包含；
6. 对 behavior eval 做对应更新。

跨多个 Skill 的旧 Rule 语义不得机械全文复制。迁移时按每个 Skill 的责任把同一通用原则投影为该 Skill 自己可执行的输入、步骤、退出或升级条件；Provider 若仍需要一个通用设计原则，可以保留 Provider-local design / policy owner，但 Consumer Skill 不在线依赖它。对 evidence、human escalation、execution continuity 等跨 Skill invariant，用确定性 / behavior tests 检查一致性，而不是通过 Skill 外共享 runtime reference 建立新的隐藏依赖。

不得把所有旧文档全文复制为 references。只迁移执行该 Skill 所需的稳定知识。

### 4.3 RC-only 语义

从 `agentic-dev-v0.0.0-rc.1` 明确吸收：

- execution continuity / stop condition；
- Execution Context 与 Runtime Under Test 区分；
- `review-change` 的 fresh / isolated review 语义；
- bounded process cancellation / stale evidence cleanup；
- runtime / grader / source subject identity binding。

不 cherry-pick 整个 RC 分支。

### 4.4 Gate

每个 Skill 至少通过：

- schema / metadata；
- reference integrity；
- behavior eval；
- isolated copy / install；
- no-Provider-doc negative control。

覆盖：`PB-AC-03`～`05`、`19`、`23`、`25`、`29`。

## 5. Gate P3 — Guides / Bootstrap / Navigation

### 5.1 Guide 入口

重构：

- `using-agentic-dev.md`；
- `feature-development.md`；
- `establishing-requirement-baseline.md`；
- `human-review.md`；
- adoption / upgrade；
- Consumer-local constraints；
- 平台相关 Guides。

新增：

- `getting-started.md`；
- `bootstrap-new-project.md`；
- `choosing-next-step.md`。

### 5.2 New Project Bootstrap

建立 disposable greenfield fixture，输入只提供：

- 项目基本情况；
- `agentic-dev` Repository + 精确版本。

验证 AI 可以：

1. 从 Guide 找到入口；
2. 完成最小谈判式澄清；
3. 在不过度问答的情况下建立初始 Repository；
4. 生成薄 `AGENTS.md`；
5. 建立最小必要项目知识；
6. 安装 Skills；
7. 建立 exact-version Guide locator；
8. 回答下一步建议。

Bootstrap Guide 只在 Consumer runtime 尚不存在时拥有有界编排；完成后退出执行责任。

### 5.3 “下一步做什么”

至少建立三个不同状态 fixture：

- 新项目 Requirement Baseline 尚未成立；
- Requirement 足够但存在系统性 Architecture blocker；
- Requirement / Architecture 足够，可进入普通 Feature development。

AI 必须依据项目事实 + `choosing-next-step` Guide 得到不同下一责任，不能把 Guide 当固定状态机，也不能只凭模型通识规划。

覆盖：`PB-AC-06`～`14`。

## 6. Gate P4 — Consumer-local Constraints 最小方案

### 6.1 先验证三类约束

用 disposable Consumer fixture 分别建立：

1. Repository-wide stable policy；
2. path / module scoped policy；
3. activity / semantic scoped policy。

### 6.2 候选机制的优先顺序

按最简单到最复杂评估：

1. 根 `AGENTS.md` 中极少量稳定全局约束；
2. nested `AGENTS.md` / 宿主原生 scoped instructions；
3. Consumer-local `docs/rules/**` 或等价 policy docs + 一个薄 locator；
4. 只有前三者不能可靠覆盖真实场景时，才评估最小 metadata/filter 工具。

禁止直接复制当前五维 Rule Discovery。

如果 disposable fixture 暴露前三种机制的缺口，在进入第 4 种 metadata/filter 工具之前，必须先对至少一个真实软件 Consumer 的现有 local constraints 做**只读 applicability challenge**，确认缺口确实来自真实项目的 activity / semantic scoped policy，而不是 fixture 设计或宿主用法错误。只有真实 Consumer Evidence 仍证明简单机制不足，才允许设计最小 filter 工具；该只读检查不得提前执行 Consumer mutation。

### 6.3 验收

必须证明：

- 不把所有 rules 塞进根 `AGENTS.md`；
- 不要求普通任务加载完整 rule corpus；
- Codex local work 与 ChatGPT + WebCodex 至少各有可解释路径；
- Rule 属于 Consumer，不因 `agentic-dev` update 被覆盖；
- 明确判断当前任务没有适用的 Consumer-local constraint 时可以正常继续；只有已声明的约束入口无法解析、完整性未知或 applicability 无法可靠判断时才 fail closed；
- 方案复杂度与真实 Consumer 规模匹配。

P4 结束时才冻结第一版 Consumer-local constraints 约定。

覆盖：`PB-AC-15`～`18`、`22`。

## 7. S1 — Authority Freeze

P1～P4 已完成的成果与 Evidence 保留，不重新执行。本阶段只冻结极简终局和剩余收敛路径，不开始删除旧资产。

S1 必须完成：

- 修订本 Specification、Implementation Plan、Project Roadmap 与 Asset Disposition，使它们一致表达极简终局；
- 取消真实 Consumer adoption 作为本轮完成门槛；
- 冻结 Provider 最小治理边界：薄 `AGENTS.md` 直接指向少量 Git、语言 / 术语、文档 Authority、重大变更复核、Evidence 匹配等治理正文；
- 冻结 Consumer 产品边界：`skills/**` 是唯一正式 Consumer runtime product，Guides 只按需服务人和 AI，Consumer 自己拥有项目事实与约束；
- 冻结执行边界：WebCodex Runner 不得直接或间接调用 `codex-cli`；Fresh Context、Independent Review 和普通语义判断由 ChatGPT 承担；只有 Codex-specific Runtime Under Test 才拆成非 WebCodex 独立子任务并等待人工临时授权；
- 已保留的 Codex 场景在仍存在期间统一使用 600 秒单场景 timeout，但这些批量模型场景不再属于本轮默认完成路径；
- 不新增 Method / Rule Engine / Discovery / Runtime / Gate 类型。

S1 Authority 修订完成后执行一次 Fresh Independent Semantic Review。Review 只检查：极简目标是否一致、是否仍残留旧 P5～P9 强制路径、是否误删长期必要语义。`Blocking=0`、`Medium=0` 后进入 S2。

## 8. S2 — Subtractive Cutover

S2 以“迁移必要语义，再删除旧 owner”为唯一实施原则。

### 8.1 保留并直接化

- 15 个 canonical Skills；
- 按需 Guides；
- Consumer-local ownership / constraints 语义；
- 少量 Provider governance：Git、语言 / 术语、文档 Authority、重大变更复核、Evidence 匹配及确有必要的外部写授权原则；
- P1～P4、旧 Gate / RC 与 26 obligation 的历史 Evidence。

Provider `AGENTS.md` 直接指向这些少量治理正文，不再通过 Method selector、五维 Rule Discovery 或 Project Capability Profile 间接恢复它们。

### 8.2 简化

- Bootstrap：缩为 Repository Authority + 少量直接 governance locator；
- 验证：缩为少量 deterministic checks、隔离安装 / 运行冒烟和必要 negative control；
- 跨 Skill invariant：只保留能够静态或小型 fixture 验证的关键一致性，不维持批量模型自测体系；
- Codex-specific Runtime 验证：只在相关产品声明发生变化且确实必须观察 Codex runtime 时作为独立临时授权子任务执行。

### 8.3 删除

在对应长期语义已经迁移后删除：

- Method runtime / selector 与 `project-capability-profile.md`；
- 五维 Rule Discovery tool / workflow / metadata runtime；
- 旧统一 Capability / Source Distribution classification；
- custom Release Builder / installer / workflow；
- 被 Skills / Guides / Provider governance 直接替代的旧 Method / Architecture / Rule runtime owner；
- 只服务上述旧机制的 tests / evals；
- 默认批量 `codex-cli` runtime eval / grader orchestration，包括不再具有独立长期价值的 `authenticated_model_acceptance.py` 路径。

S2 不要求把历史 Research 和 Evidence 机械删除；它们只要不再进入 current runtime 就可以保留。

## 9. S3 — Minimal Validation & Closure

S3 只执行能够区分极简目标是否真实成立的最小验证。

### 9.1 Deterministic

至少验证：

- canonical Skill package 仍只有必要标准 metadata，内部引用可解析；
- Provider `AGENTS.md` 和 Guides 没有指向已删除的 Method selector、Rule Discovery、Release Builder / installer 或其他死入口；
- 普通 Provider 修改不再要求 Method / Rule Discovery、批量模型自测或多级 Gate；
- Consumer-owned `AGENTS.md` / docs / constraints 在安装或更新 fixture 中不被覆盖；
- 旧 26 Consumer obligations 已有静态 owner 映射且没有因删除旧基础设施出现归属空洞；
- RC-only 有价值语义已迁移或有明确历史处置。

### 9.2 隔离安装 / 运行冒烟

使用 disposable Consumer-like fixture 验证：

```text
canonical skills/**
→ standard-compatible install / copy
→ Consumer-owned files preserved
→ Skill package 可被目标宿主的标准机制识别 / 使用到本轮声明所需边界
```

默认不启动批量模型任务。已有 P1～P4 的 Codex-specific Evidence 只有在对应 Skill package exact subject / digest 未变化、且当前声明只依赖该未变化 subject 时才可继续支持该声明；不得仅因历史曾 PASS 就跨 subject 复用。若最终 candidate 改变了相关 subject，或新增必须重新观察的 Codex-specific claim，则另拆独立临时授权子任务，不允许 WebCodex Runner 启动 `codex-cli`。

### 9.3 Fresh Independent Review

对最终 exact candidate 执行一次 Fresh ChatGPT Independent Review，重点只检查：

- 是否真的比旧模型简单，而不是换名；
- `skills/**` 是否仍是唯一 Consumer runtime product；
- Provider governance 是否已经直接化且数量有界；
- 是否仍存在旧 Method selector / Rule Discovery / Release machinery 的活动路径；
- 26 obligations 与 RC-only 语义是否无 gap；
- 验证基础设施是否本身再次形成新的复杂运行时。

`Blocking=0`、`Medium=0` 后结束本轮基础设施重构。

## 10. Acceptance 映射

| Acceptance | 当前主要证据 / 收敛责任 |
|---|---|
| PB-AC-01～05 | P2 已有成果 + S2 Provider cutover |
| PB-AC-06～10 | P3 已有成果 + S2 Guide / Bootstrap 直接化 |
| PB-AC-11～14 | P3 已有成果 + S3 隔离 fixture / 静态检查 |
| PB-AC-15～18 | P4 已有成果 + S3 Consumer-owned constraint fixture |
| PB-AC-19～23 | P1 / P2 已有成果 + S3 最小 runtime / negative-control 验证 |
| PB-AC-24～27 | S1 disposition + S2 删除 + S3 dead-entry 检查 |
| PB-AC-28 | 原 Specification Review 已满足；S1 Authority 修订另做 Fresh Independent Review |
| PB-AC-29 | P2 已有迁移 Evidence + S2 / S3 RC-only 处置核对 |

真实 Consumer adoption 不再承担任何 PB-AC 的本轮完成证明责任。

## 11. 停止条件

S1 以后只允许以下问题阻塞收敛：

- 会导致极简产品边界自相矛盾；
- 使 canonical Skills 无法安装或无法承担已冻结责任；
- 会覆盖 / 破坏 Consumer-owned Authority；
- 删除后产生无法归属的现有必要软件开发责任；
- Fresh Independent Review 发现 `Blocking` / `Medium`。

其他优化、体验改进、额外平台验证和真实 Consumer adoption 反馈全部进入 backlog，不再自动扩大本轮重构。

## 12. 实施完成定义

只有同时满足以下条件才算本轮完成：

- canonical Consumer product 只剩直接可安装 `skills/**`；
- Guides 对人和 AI 都可按需使用；
- Consumer-local facts / constraints 继续由 Consumer 拥有；
- Provider `AGENTS.md` 足够薄，并直接指向少量必要治理正文；
- Provider ordinary work 不再依赖 Method selector、Project Capability Profile、五维 Rule Discovery、old Release Builder / installer、批量模型自测或多级 Gate；
- 15 Skills、26 legacy obligations 与 RC-only 有价值语义没有能力 / 归属缺口；
- 最小 deterministic checks 与隔离安装 / 运行冒烟通过；
- 最终 Fresh Independent Review 为 `Blocking=0`、`Medium=0`。

完成后声明为：**Provider 极简切换完成，可供采用**。不得声明真实 Consumer 已完成采用验证；未来 Consumer adoption 问题进入正常产品反馈，不自动重开基础设施重构。
