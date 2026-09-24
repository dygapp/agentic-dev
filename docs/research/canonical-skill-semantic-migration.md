---
id: research:canonical-skill-semantic-migration
type: research
status: active
distribution: source-only
---

# Canonical Skill 语义迁移核对

## 1. 目的

本文是产品边界重构 Gate P2 的非规范 Evidence，用于防止从旧 Release composition 模型迁移到 canonical `skills/**` 时静默丢失已经验证的软件开发责任。

它不成为新的 Consumer runtime owner。P2 完成后，Consumer-facing 通用执行语义只由对应 `skills/<name>/**` 持有；本文只记录迁移来源、去向与验证状态。

## 2. 旧模型事实

冻结 RC source：

`51db05801382b74ee01601f391305fcbbff98db3`

旧 Release Builder 的确定性构建验证显示：

1. 15 个 Source Skill 的 `SKILL.md` 原样复制进入安装包；
2. 28 个 `distribution: release-input` 的 Method / Architecture / Rule 根据每个 Skill 的 `agentic-dev-release-inputs` 被复制；
3. 复制结果位于 Skill-local `references/release-inputs/**`；
4. 每个 generated reference 基本保留原 Source owner 完整正文，只增加 source id / source SHA provenance；
5. 因而旧 Consumer runtime 的实际语义模型是：

```text
Source Skill
+ selected Method / Architecture / Rule full-body copies
→ generated Skill package
```

P2 不把这批 generated references 原样搬回 `skills/**`。这会把 semantic compilation 从“构建期复制”变成“源码期复制”，并不能消除旧模型。

## 3. 迁移原则

对每个旧 release input 只保留当前软件项目仍需要的**可执行投影**：

- 输入 / 前置；
- 处理步骤；
- 完成 / fail-closed 条件；
- Evidence 责任；
- 人工升级边界。

跨多个 Skill 的原则按各 Skill 自己的责任表达，不全文复制同一 Rule。Consumer-local Product / Requirement / System Architecture / technology policy / authorization 不进入通用 Skill。

当前 P2 candidate 已移除全部 `agentic-dev-*` composition metadata。下表中的“已投影”只表示语义已写入当前候选；最终行为是否成立仍由 P2 behavior eval、标准安装、Codex native discovery 与 no-Provider-doc negative control 验证。

## 4. 28 个旧 release input 的去向

| 旧 Source owner | P2 canonical projection | 当前处置 |
|---|---|---|
| `method:ai-development` | `clarify-intent`、`specify`、`technical-plan`、`slice-work`、`readiness-check`、`execute-unit`、`systematic-debug`、`converge` | 生命周期责任拆回各可执行 Skill；不保留 Consumer Method runtime |
| `method:architecture-clarification` | `clarify-architecture` | systemic driver、非 BDUF、Requirement return、Architecture owner / ADR、Ready 条件已投影 |
| `method:requirement-baseline-establishment` | `establish-requirement-baseline` | source-role、冲突 / 缺口、长期 owner、Baseline Ready 已投影 |
| `method:model-collaboration-adoption` | `activate-model-collaboration` | runtime probe、策略选择、local instance、fallback、enablement boundary 已投影 |
| `architecture:requirement-authority` | `establish-requirement-baseline`、`specify` | Human navigation / locator / fact owner / analysis workspace 的 single-owner 边界已投影 |
| `architecture:data-migration` | `technical-plan`、`execute-unit`、`converge` | source role、semantic preservation、identity / duplicate、replay / idempotency、exception / provenance 与 completion 已投影 |
| `architecture:human-review` | `human-review` | 默认 Markdown、派生视图、反馈分类 / 回写、completion、显式交付格式直接由 Skill 持有 |
| `architecture:model-collaboration` | `activate-model-collaboration` | Runtime Under Test、observability、single-writer、resource ownership、fallback、functional vs efficiency claim 已投影 |
| `rule:data-access-boundedness` | `technical-plan`、`execute-unit` | bounded / growing / unknown scope、禁止无界全量与静默截断已投影 |
| `rule:implementation-discipline` | `execute-unit`、`systematic-debug` | 最低必要复杂度、精准差异、禁止猜测性大改已投影 |
| `rule:async-operation-bounded-observation` | `external-operation`、`github-actions-verification` | request accepted ≠ completion、有界观察、终态 / blocker / observation limit 已投影 |
| `rule:cross-repository-authorization` | `external-operation` | 每仓独立授权、局部授权缺口只阻塞依赖动作已投影 |
| `rule:external-binary-content-validation` | `external-operation`、`execute-unit` | signature / media type / parseability 与转换后复验已投影 |
| `rule:human-intervention-necessity` | 15 个 Skill 的 escalation / decision boundary | 先查 Authority / tools / Evidence，只把不可替代决定、权限、受控环境或法定责任交给人工 |
| `rule:safe-external-write` | `external-operation`、`github-actions-verification` | 授权、最小操作、复用现有 identity、幂等 / retry、写后 reread 已投影 |
| `rule:shared-resource-concurrency-ownership` | `activate-model-collaboration`、`external-operation`、`github-actions-verification` | 真实共享资源 owner / lifecycle 与安全释放已投影 |
| `rule:temporary-evidence-to-persistent-input-promotion` | `external-operation`、`github-actions-verification`、`converge` | 临时 Evidence 默认不晋升；显式 Authority acceptance + integrity / provenance / current revalidation 已投影 |
| `rule:authoritative-artifact-lifecycle-review` | `clarify-architecture`、`establish-requirement-baseline`、`specify`、`technical-plan`、`review-change`、`converge` | owner replace / retire / archive 时同步 locator / navigation / verification / current-state wording |
| `rule:high-impact-ai-review-required` | 高影响 owner Skill → `review-change` | 高影响 Authority / core Skill / governance 变化进入 fresh independent review；PASS 不授予集成 |
| `rule:integration-state-closure-review` | `review-change`、`converge` | Roadmap / README / recovery entry 按拟集成后的长期状态复核，避免瞬时状态成为 Current truth |
| `rule:database-migration-completion-evidence` | `execute-unit`、`converge` | 可取得时要求 `Fresh Database → Full Migration Chain → Application Startup`；否则显式 Evidence gap |
| `rule:evidence-claim-reuse-across-commits` | `github-actions-verification`、`review-change`、`converge` | ancestor/current exact diff、claim mapping、受影响 claim 重验已投影 |
| `rule:evidence-type-must-match-claim` | verification / completion 相关 Skills | 完成声明必须由能区分该 claim 的当前证据支持；局部终态不扩大成整体完成 |
| `rule:human-review-baseline-isolation` | `human-review`、`github-actions-verification` | 保存自动 Evidence 后恢复可重复人工 baseline，禁止测试残留污染人工评审 |
| `rule:verification-contract-currentness` | `execute-unit`、`systematic-debug`、`readiness-check`、`review-change`、`github-actions-verification`、`converge` 等 | 测试 / Workflow 必须与 Current Authority 一致；区分 implementation / stale contract / runtime / external dependency |
| `rule:visual-evidence` | `execute-unit`、`github-actions-verification`、`human-review`、`review-change`、`converge` | visual-fidelity claim 不由功能测试单独证明；使用真实渲染 / reference / AI / human evidence |
| `rule:execution-context-runtime-boundary` | `activate-model-collaboration`、`review-change` | fresh / independent context 与目标 Runtime 是不同维度；仅 Runtime-specific claim 启动目标 Runtime |
| `rule:execution-continuity-and-stop-condition` | 15 个 Skill 的 completion / escalation / observation boundary | 子任务、测试、工具、commit、timeout 终态不等于整体责任终态；仍有授权内可关闭责任时继续 |

## 5. RC-only delta

冻结 RC 相比上一稳定 master 对 15 个 Skill 的主要变化不是 Skill body 重写，而是：

- 将 `rule:execution-continuity-and-stop-condition` 加入 15 个 Skill 的 release composition；
- 将 `rule:execution-context-runtime-boundary` 加入 `activate-model-collaboration` 与 `review-change`；
- `review-change` body 增加 fresh / isolated review step。

P2 已把这些语义直接写回 canonical Skill body，不继续依赖 composition metadata。

## 6. P2 验收结果

Gate P2 的 canonical Skill exact subject：

`4918846e411b9797fb705fa0b6695891f190a51e`

最终验收结果：

- 15/15 `skills/*/SKILL.md` 只保留标准 `name` / `description` front matter；
- 旧 `agentic-dev-release-*`、`release-inputs`、`references/release-inputs/**` 与 Provider docs runtime locator 扫描为 0；
- 冻结 RC 的 28 个唯一 release-input owner 全部进入本文件迁移矩阵，`missing=0`；
- 标准 Skills CLI 能从 canonical `skills/**` 发现并安装 15/15 Skill；
- disposable Consumer 安装结果不复制 Provider `docs/**`，也不覆盖 Consumer-owned `AGENTS.md` / project docs；
- Codex native `skills/list` 发现 15/15 repo-local Skill，全部 enabled，`errors=[]`；
- 每个 Skill 至少一个代表性 behavior scenario 已实际运行并完成 assertion-level semantic grading，最终为 15/15 PASS；
- 首轮 grading 暴露的 `clarify-architecture` Requirement 越界、`github-actions-verification` 跨提交语义 Evidence 复用不足、`readiness-check` Return To 不明确三个问题已在当前 exact subject 修复并重新运行 / 重新 grading 为 PASS；
- 旧 RC-only 的 execution continuity / stop condition 已投影进各 Skill 自身 completion / escalation / observation responsibility；Execution Context 与 Runtime Under Test 区分已进入 `activate-model-collaboration` 与 `review-change`，`review-change` 保留 fresh / isolated review；
- Fresh Independent Review 结果：`Blocking=0`、`Medium=0`。

代表性 behavior Evidence 中，12 个未受最终 remediation 影响的 Skill 复用 `48bc7d3555fc26ef1b7665b019ec810b633d243e` 的已评分结果；精确 `48bc7d3… → 4918846…` diff 只修改：

- `skills/clarify-architecture/SKILL.md`
- `skills/github-actions-verification/SKILL.md`
- `skills/readiness-check/SKILL.md`

这三个 Skill 已在 `4918846…` 上重新运行并重新评分。祖先 Evidence 不被描述为当前 Run，只按未受 diff 影响的具体 behavior claim 复用。

保留 1 个非阻塞 Low：

- `skills/README.md` 仍以旧 Provider Capability / Method / Rule 模型解释 Skill 来源和维护关系。该文件是 `source-only` Human View，不进入标准安装 payload、native Skill discovery 或 ordinary Consumer runtime，因此不阻塞 P2；在后续 Provider governance cutover 中统一改写。

因此 Gate P2：**PASS / CLOSED**。
