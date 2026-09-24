---
id: project:methodology-product-boundary-implementation-plan
type: project
status: active
distribution: source-only
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

## 7. Gate P5 — Runtime / Eval 基础设施切换

### 7.1 Runtime Acceptance

重构当前 Runtime Acceptance：

```text
canonical skills/**
→ standard-compatible install/copy into isolated Consumer
→ native discovery
→ activation / behavior
→ negative controls
→ evidence collection
```

不再：

```text
docs Method / Rule / Architecture
→ release_build.py
→ generated ZIP
→ install_release.py
```

### 7.2 保留的验证能力

- exact subject identity；
- Codex native Skill discovery；
- authenticated representative behavior；
- independent grader；
- process timeout / cancellation；
- stale evidence cleanup；
- Evidence kind / schema；
- source / scenario / runtime / grader binding；
- Provider Source / docs unreadable / unavailable negative controls；
- Skill resource integrity；
- progressive disclosure。

### 7.3 ChatGPT + WebCodex

验证第 0 层 Project Instructions 只负责：

```text
定位 Repository
→ WebCodex
→ AGENTS.md
```

进入 Repository 后由 Layer 1～4 接管。不得要求 ChatGPT Project Instructions 复制方法论正文。

P5 执行期间额外冻结以下执行边界：WebCodex Runner 只承担 Repository / deterministic runtime 工作，不得启动 `codex-cli`；Fresh Context、independent review 与普通 semantic grading 由 ChatGPT 完成。只有 Codex-specific Runtime Under Test 声明必须使用 `codex-cli` 时，才拆成独立子任务并等待人工在单独会话显式临时授权。仓库自带 Codex 执行入口在 WebCodex 环境必须 fail closed。单个 Codex Runtime / grader 场景 timeout 统一为 600 秒。

覆盖：`PB-AC-20`～`23`。

## 8. Gate P6 — Provider Governance Cutover 与减法清理

P1～P5 全部通过后才执行 Provider 自身 cutover。

### 8.1 更新真正 Current Owners

调整：

- `project-charter.md`；
- `AGENTS.md`；
- 根 `README.md`；
- `project-roadmap.md`；
- `skill-architecture.md`；
- 必要 Consumer / Project Knowledge 说明。

目标：

- Provider 不再声明必须 self-consume Consumer runtime；
- Fresh Context 不固定加载 Project Capability Profile；
- 不执行 Method selector；
- 不执行旧五维 Rule Discovery；
- Guides 从 Human-only 改为 Human + AI on-demand；
- `skills/**` 是唯一 Consumer runtime product。

### 8.2 Provider 自身 Rules

Provider 只保留有独立本仓治理价值的少量规则。第一轮优先：

- human-facing content；
- Git commit discipline；
- external write / authorization 中仍需的最小原则；
- high-impact independent review；
- 必要 Evidence integrity。

通过薄 Bootstrap / 少量明确 trigger 使用，不为这几条规则重建通用 Rule Engine。

### 8.3 删除已替代资产

只有对应语义已迁移且新验证已通过后，删除：

- Project Capability Profile；
- Method runtime / selector；
- 统一 Capability Architecture；
- upstream Rule distribution model；
- Rule Discovery tool / workflow / obsolete tests；
- distribution metadata / audit tool；
- Release Builder / custom installer / workflow；
- 被 Skill / Guide 正式替代的 Method / Architecture 文档；
- 旧 Discovery evals。

旧 Specification / disposition / implementation plan 在最终 canonical convergence 前继续作为本轮 Evidence；完成后按各自生命周期退出 Current Authority。

覆盖：`PB-AC-01`～`05`、`24`、`27`。

## 9. Gate P7 — 全仓最终验证与独立复核

在最终 exact candidate 上执行：

### 9.1 Deterministic

- Markdown / Skill schema；
- dead locator / broken reference；
- no old distribution metadata；
- no active Release Builder / installer locator；
- Guide / Skill link consistency；
- new Bootstrap fixtures；
- Consumer-local constraints fixtures；
- full eval suite；
- runtime acceptance。

### 9.2 Negative controls

至少包括：

- Provider `docs/**` 对安装后的 Skill runtime 不可读；
- Guide exact ref 不可用时 methodology navigation 不回退 latest；
- Consumer local policy 与 Skill 默认冲突时 local Authority 优先；
- 删除 optional Layer 0 后 Codex local work 仍能从 `AGENTS.md` 启动；
- ChatGPT Project Instructions 不包含项目 current facts；
- install/update 不覆盖 Consumer-owned `AGENTS.md` / docs；
- retired Method / Rule / Release locator 不再参与 ordinary runtime。
- Provider Fresh Context 在没有旧 Rule Discovery Tool 的情况下，仍能通过薄 `AGENTS.md` + 少量明确 Provider-local trigger 恢复本仓关键治理约束；

### 9.3 Fresh Independent Review

独立复核：

- 目标模型是否真正变简单，而不是概念换名；
- 旧 26 Consumer obligations 是否仍无 gap；
- RC-only delta 是否全部处置；
- Guides 是否既能给 AI 使用又没有恢复常驻大上下文；
- Skills 是否真正 canonical / self-contained；
- Consumer-local constraints 是否没有偷偷重建 Rule Runtime。

Blocking / Medium 必须为 0 才进入真实 Consumer。

## 10. Gate P8 — 真实 Consumer 最小 Adoption

目标仍使用 `dygapp/jilinjobs-cms`，但这是**新模型的 adoption validation**，不是旧 Gate H 延续。

默认动作严格最小：

1. 恢复 Consumer 当前 Authority；
2. 安装 canonical Skills；
3. 对 Consumer-owned `AGENTS.md` 做 bounded Bootstrap integration；
4. 建立 exact-version Guide locator；
5. 保留现有 Product / Requirement / Architecture / technology policy / local rules；
6. 验证 Codex 与 ChatGPT + WebCodex；
7. 验证 representative software-development behavior；
8. 验证普通开发不依赖 Provider docs。

Consumer 当前历史 AI governance 清理只有在与新入口形成真实冲突时才做必要部分；更广泛的文档 / Rule / Authority remediation 作为独立可选工作，不再绑在 Adoption 上。

覆盖：`PB-AC-13`～`18`、`21`～`26`。

## 11. Gate P9 — 最终收敛

真实 Consumer validation 通过后：

1. 把仍有价值的稳定结论写回 canonical owner；
2. Roadmap 切换到完成后的稳定 baseline；
3. 本 Specification、asset disposition 与 implementation plan 退出 Current Authority；
4. 历史由 Git / Issue / PR / Actions 与 Research Evidence 保留；
5. 不保留“新模型迁移中”兼容入口。

## 12. Acceptance 映射

| Acceptance | 主要 Gate |
|---|---|
| PB-AC-01～05 | P2、P6 |
| PB-AC-06～10 | P3 |
| PB-AC-11～14 | P3、P8 |
| PB-AC-15～18 | P4、P8 |
| PB-AC-19～23 | P1、P2、P5、P7 |
| PB-AC-24～27 | P6、P7、P9 |
| PB-AC-28 | 已由 Specification Fresh Independent Review 满足 |
| PB-AC-29 | P2、P5、P6、P7 |

## 13. 停止与回退条件

只在以下情况停止自动推进：

- P1 证明标准 Skills distribution 无法满足必要能力，需要改变产品边界；
- P4 的真实约束场景证明轻量方案不足，且需要新增复杂机制；
- 新项目 Bootstrap 出现需要人工决定的重大产品边界；
- 当前 Repository Authority / 权限形成不可关闭 blocker；
- Independent Review 发现需要修改冻结 Specification 的 Blocking / Medium finding。

普通文件组织、reference 拆分、fixture 结构和测试实现属于可逆实现决定，不作为人工中断点。

## 14. 实施完成定义

只有同时满足以下条件才算本轮完成：

- canonical Consumer product 只剩直接可安装 `skills/**`；
- Guides 对人和 AI 都可按需使用；
- New Project Bootstrap / Existing Project Adoption 均有真实可执行路径；
- “下一步做什么”能够依据 Consumer facts + Guide 工作；
- Consumer-local constraints 有最小、已验证方案；
- `AGENTS.md` 保持薄；
- Provider 不再依赖统一 Capability Runtime 自我治理；
- old Release Builder / distribution classification / Method selector / upstream Rule Runtime 退出 current path；
- 15 Skills 与 26 legacy obligations 没有能力缺口；
- RC-only 有价值语义全部迁移；
- deterministic / runtime / Fresh Context / independent review 全部通过；
- 真实 Consumer 最小 adoption validation 通过。
