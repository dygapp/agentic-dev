# Issue #58 EU-31～EU-36 Verification / Readiness / Adoption 维护计划

**状态：** Final AI Review Pending

## Goal

基于 Issue #58 最新 Consumer Evidence，收敛 EU-31～EU-36 暴露的 Verification trigger topology、Readiness 回退重入与 Existing Consumer repository-facing convention 可发现性缺口，同时只把其余样本保留为正向验证或后续候选，避免把 Consumer-specific 实现提升为通用规则。

## Authority / Inputs

- `AGENTS.md`
- `docs/method/ai-development-method.md`
- `docs/architecture/technology-profile-contract.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/external-operation-guidelines.md`
- `docs/architecture/engineering-disciplines.md`
- `skills/readiness-check/SKILL.md`
- `skills/github-actions-verification/SKILL.md`
- Issue #58 最新 Consumer Feedback（EU-31～EU-36）
- Consumer PR #70 / #71 / #72 / #73 / #74
- 基线：`master@d9fad0da83dbdb61cac5eb9778b0258c6861eef1`

## Evidence Classification

### Immediate targeted maintenance

1. **Finding A — Verification risk / claim 与 workflow trigger topology 对账**
   - Severity：Medium
   - Scope：Usage Guide + existing `github-actions-verification` + targeted Behavior Eval
   - Verification Profile Contract：**No change**；现有 `Acceptance / change type → verification layer → Consumer mechanism → Current Evidence` 责任链已经足够，缺口位于 GitHub Actions 平台 operationalization 没有显式把 Claim / Risk 与实际 trigger topology 对账。
   - 不规定固定 `paths` / label / manual / reusable workflow adapter。

2. **Finding B — Readiness return-to-upstream 后重新进入 Slice / Gate**
   - Severity：Medium
   - Scope：Usage Guide + existing `readiness-check` + targeted Behavior Eval
   - 不修改 Core Method；现行 Stage Return 已存在，本次只补 downstream evidence invalidation / re-entry 语义。

3. **Finding F — Existing Consumer repository-facing conventions 可发现性**
   - Severity：Low / Usage clarification
   - Scope：Existing Consumer Adoption Guide
   - 只要求升级时显式审计并本地采纳、保留、覆盖或拒绝 repository-facing conventions；不要求 Consumer 继承 `agentic-dev` 自身 Git Commit、语言或分支规则。

### Positive validation / no immediate rule change

- **C — Stale Verification Contract**：现行规则再次得到 Consumer 验证；不新增规则。
- **E — Temporary mechanism vs Final Delivery Scope**：现行 Surgical Diff / External Operation 规则再次得到验证；不新增规则。

### Deferred candidate

- **D — Executable Architecture Boundary 三层证据**：接受为有价值的 Verification Pattern Candidate，但当前只有单一 Consumer 的单一架构边界样本。暂不升级为 Engineering Discipline、Method 或强制 Verification Profile 规则；后续出现跨技术栈重复证据时再评估。

## Scope

1. 保持 Verification Profile Contract 不变，在 Operating Guide / GitHub Actions capability 中将其既有 Evidence Responsibility operationalize 为 `Change / Authority Impact → Evidence Claim / Risk → Verification Layer → Trigger Topology` 对账；
2. 在 GitHub Actions capability 中要求检查真实 workflow trigger topology，避免无关高成本 Claim 重验，同时防止受影响 Claim 被 path/filter 等 adapter 漏掉；
3. 明确 docs / Authority-only 变更不能仅按扩展名机械跳过或机械执行 full integration，应由 Consumer claim/risk policy 决定；
4. 明确 Readiness 返回上游后，若 Specification / Technical Plan / Architecture basis 发生实质修订，旧 Candidate / Gate evidence 不得继续授权 Execute，必须基于 Current Authority 重新 Slice / Readiness；
5. Existing Consumer baseline upgrade 增加 repository-facing convention discoverability 审计；
6. 新增最小 Behavior Eval，并回归直接受影响场景；
7. 回写 Issue #58，Issue 继续保持 OPEN。

## Non-goals

- 不新增 Core Method Stage；
- 不修改 Core Method、Principles、Skill Contract 或 Verification Profile Contract；
- 不新增 Task-oriented Skill；
- 不新增 Engineering Discipline；
- 不把 Consumer 的 L0～L4、具体 Workflow 路径、Vue/Kotlin、CMS 数据结构或固定 Review Environment 规则复制为通用政策；
- 不规定所有 docs-only PR 都跳过 CI / Review；
- 不规定所有架构边界必须具有 source guard；
- 不让 Consumer 自动继承 `agentic-dev` 仓库自身 Git Commit / 中文摘要规则。

## Work Items

1. 复核 Verification Profile Contract 已有责任链并保持其不变；
2. 修订 Usage Guide 的 Verification、Readiness 与 Existing Consumer Adoption 边界；
3. 对齐 `github-actions-verification` 与 `readiness-check`；
4. 新增：
   - `B-GA-08`：claim/risk 与 workflow trigger topology 不一致时，不机械运行或跳过高成本验证；
   - `B-RC-07`：Readiness 返回上游并修订 WHAT/HOW 后，旧 Candidate / PASS 不得继续授权 Execute；
5. 回归直接相关既有场景：
   - `B-GA-04`：后继提交按 Evidence Claim 判断复用；
   - `B-GA-01`：异步 GitHub Actions 当前证据闭环；
   - `B-RC-06`：Identifier / Roadmap 顺序不能替代 Readiness；
   - `B-RC-01`：完整输入无阻塞时仍可 PASS；
6. 静态验证、Fresh Runtime、人工语义评分、最终 AI Review；
7. 回写 Eval、Project Roadmap、Plan 与 Issue #58。

## Runtime Evidence

Fresh Runtime 已完成：

```text
新场景：   2 / 2 PASS，14 / 14 assertions PASS
直接回归： 4 / 4 PASS，23 / 23 assertions PASS
合计：     6 / 6 PASS，37 / 37 assertions PASS
```

场景：

- `B-GA-08`：7 / 7 PASS；
- `B-RC-07`：7 / 7 PASS；
- `B-GA-04`：7 / 7 PASS；
- `B-GA-01`：6 / 6 PASS；
- `B-RC-06`：6 / 6 PASS；
- `B-RC-01`：4 / 4 PASS。

行为验证 Head：

`ade7a59c5bf3e0819e336beec1d223e174ec8bc2`

评估附件：`pr61-verification-readiness-adoption-eval-results.zip`

SHA-256：

`f40a91054bc03ce3be92002f2c9623d0b25ea1dbad367c5ed76a7c388aa55cab`

6 个场景均来自独立仓库外 `/tmp/agentic-dev-behavior-*` workspace；stderr 全部为空，JSONL 均有完整最终回答与 `turn.completed`。命令轨迹未读取 Eval 定义、assertions、历史结果、Consumer Repository 或工作区外上下文。进程退出码均为 `0`，但没有被当作语义 PASS 依据。

Runtime 后只修改 Eval 结果、Project Roadmap 与本协调 Plan，不再修改 Guide、Skill 或 Behavior 场景，因此该 Runtime Evidence 继续对应行为语义。

## Completion Criteria

- A / B / F 的通用缺口进入正确 Authority 层且无过度泛化；✅
- C / E 只作为正向证据记录，不重复造规则；✅
- D 明确保留为 Deferred Pattern Candidate；✅
- 新场景与必要回归全部通过 Fresh Runtime 和人工语义评分；✅
- Final AI Review Blocking / Medium Finding = `0 / 0`；**PENDING**
- PR 只推进到 Ready to Integrate；Merge 仍由 Human Authority 决定；**PENDING Final AI Review**
- Issue #58 保持 OPEN。✅
