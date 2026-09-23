---
id: research:methodology-product-boundary-asset-disposition
type: research
status: active
distribution: source-only
---

# 方法论产品边界重构资产处置审计

## 1. 性质与审计基线

本文是 `project:methodology-product-boundary-specification` 通过独立语义复核后的 Repository-wide asset disposition Evidence，不是新的 Runtime Authority。

审计输入：

- 当前已集成基线：`master@87a6ff8e1ba29baf8154c605bf1fbfef14574c8d`；
- 已冻结产品边界规范：`6eae3cf192c9ae67eed7f9d3e0aa33ef14d2c338`；
- 旧发布模型冻结 RC：`agentic-dev-v0.0.0-rc.1@51db05801382b74ee01601f391305fcbbff98db3`；
- Gate F Legacy Consumer Coverage：26 项 obligation，`unclassified=0`、`gap=0`。

当前旧 Distribution Audit 统计为 166 个 Repository 文件、115 个显式 scoped asset；其中 `release-direct=16`、`release-input=29`、`source-only=70`。这些旧分类只作为审计输入，不构成新的产品边界。

本文使用三种目标 disposition：

- **retain**：职责在新模型中仍然成立，保留并只做必要收敛；
- **adapt**：原始需求仍有价值，但 owner、加载方式或实现需要迁移；
- **retire**：当前文件 / 机制不应继续作为 Current asset；必要语义先迁移，再从当前树退出。

任何 `retire` 都不表示删除 Git 历史。

## 2. 根入口与 Project Knowledge

| 资产 | 处置 | 目标 |
|---|---|---|
| `AGENTS.md` | adapt | 收敛为 Provider 自身薄 Repository Bootstrap；移除统一 Capability Runtime、Method selector、发布分类与复杂 Rule Discovery 的固定依赖 |
| `README.md` | adapt | 成为人类入口，直接解释 Guides + Skills + Consumer-local Authority 的产品模型 |
| `docs/project/project-charter.md` | adapt | 移除“Provider 必须 self-consume Consumer runtime”与旧 Distribution Build 使命；保留软件项目适用域、Consumer ownership、Evidence-driven evolution |
| `docs/project/project-capability-profile.md` | retire | 统一 Capability instance / Method selector / Release Build locator 不再是目标模型；仍有价值的 Provider runtime locator 回到薄 Bootstrap 或实际工具文档 |
| `docs/project/project-roadmap.md` | retain | 继续拥有当前 evolution / gate / next candidate 的紧凑状态 |
| `docs/project/project-evolution.md` | retain | 继续保存理解当前模型有价值的稳定历史，不进入普通运行时 |
| `docs/project/methodology-product-boundary-specification.md` | retain | 当前重构规范；完成最终 canonical convergence 后再退出 Current Authority |
| `docs/project/distribution-rebuild-specification.md` | retire | 仅作为 Issue #172 Gate A～G 历史规范 / Evidence locator |
| `docs/project/README.md` | adapt | Project Knowledge 人类导航；删除 Capability Profile 作为长期必备 instance 的表述 |

Repository support：

- `.gitignore`：retain；
- `LICENSE`：retain。

## 3. Architecture 资产

| 资产 | 处置 | 目标 |
|---|---|---|
| `docs/architecture/skill-architecture.md` | adapt | 保留为 Provider 设计 / 验证 canonical Skills 的产品工程规范；去除 release-direct / release-input composition 假设 |
| `docs/architecture/consumer-architecture.md` | adapt | 只保留 Consumer ownership、Bootstrap、installed Skills、Guide locator 与 local constraints 边界；不再定义自定义 Release runtime |
| `docs/architecture/project-knowledge-architecture.md` | adapt | 提炼 Consumer/Provider 项目知识边界到 Guide / Bootstrap；若剩余内容仅是统一 Capability ontology 的配套层则最终 retire |
| `docs/architecture/requirement-authority-architecture.md` | adapt | 必要语义进入 `establish-requirement-baseline` Skill references 与 Requirement Guide，随后退出 Consumer runtime type |
| `docs/architecture/human-review-architecture.md` | adapt | 必要语义进入 `human-review` Skill references 与 Guide，随后退出 Consumer runtime type |
| `docs/architecture/data-migration-architecture.md` | adapt | 可复用执行 / review 语义进入 `technical-plan`、`execute-unit`、`converge` references，随后退出 Consumer runtime type |
| `docs/architecture/model-collaboration-architecture.md` | adapt | 可复用语义进入 `activate-model-collaboration` Skill / reference 与可选平台 Guide，随后退出 Consumer runtime type |
| `docs/architecture/engineering-capability-architecture.md` | retire | 统一 Method / Architecture / Rule / Skill Capability ontology 不再是产品前提；保留的 single-ownership / progressive-disclosure 原则进入真正 owner |
| `docs/architecture/method-architecture.md` | retire | Consumer 不再需要 Method runtime / selector |
| `docs/architecture/rule-architecture.md` | retire | Consumer-local constraints 不再继承 upstream Rule type |
| `docs/architecture/rule-discovery-architecture.md` | retire | 当前五维通用 Rule Runtime 不再作为软件 Consumer 的默认基础设施 |
| `docs/architecture/release-architecture.md` | retire | 自定义 Source→Release transformation / ZIP / installer 模型退出 |
| `docs/architecture/README.md` | adapt | 仅导航仍保留的 Provider architecture / design docs，不再展示统一 Capability type 系统 |

原则：`adapt` 不表示旧 Architecture 文档必须永久存在。必要 Consumer 运行语义完成向 Skill / Guide 迁移后，若其只剩旧 runtime type 责任，应 retire，而不是为保留文件而保留概念。

## 4. Method 资产

以下 Method 的**软件开发知识保留，但 Method runtime type 退出 Consumer 产品模型**：

| 资产 | 处置 | 目标迁移 |
|---|---|---|
| `docs/methods/ai-development.md` | adapt → retire | 生命周期导航进入 `feature-development.md` / `using-agentic-dev.md`；可执行阶段责任由相关 Skills 自己持有 |
| `docs/methods/requirement-baseline-establishment.md` | adapt → retire | 进入 `establish-requirement-baseline` Skill + Guide |
| `docs/methods/architecture-clarification.md` | adapt → retire | 进入 `clarify-architecture` Skill + Guide |
| `docs/methods/model-collaboration-adoption.md` | adapt → retire | 进入 `activate-model-collaboration` Skill + Guide |
| `docs/methods/consumer-adoption.md` | adapt → retire | Existing Project Adoption Guide + 标准 Skills 安装路径 |
| `docs/methods/consumer-upgrade.md` | adapt → retire | Skills 标准更新 / 精确版本切换 Guide |
| `docs/methods/README.md` | retire | 不再维护 Method inventory |

这组处置直接落实“Method 可以作为 Provider 分析语言，但 Consumer 不需要先消费一套中间 Method 产物”的边界。迁移完成后如果某个 Method 文档仍对 Provider 研究有独立价值，应以普通内部设计 / research 身份重新评估，而不是恢复 Consumer runtime 身份。

## 5. Guides

### 5.1 保留并重构

| 资产 | 处置 | 目标 |
|---|---|---|
| `docs/guides/README.md` | adapt | 从 Human-only 改为 Human + AI 按需知识导航 |
| `docs/guides/using-agentic-dev.md` | adapt | 方法论总览；说明怎么开始、如何组合 Skills、如何判断下一类工作 |
| `docs/guides/establishing-requirement-baseline.md` | adapt | 人和 AI 的 Requirement Baseline 使用知识，不复制 Skill procedure |
| `docs/guides/feature-development.md` | adapt | 软件 Feature 生命周期导航，不再依赖 Method runtime selector |
| `docs/guides/human-review.md` | adapt | 人工评审使用知识，与 `human-review` Skill 分工 |
| `docs/guides/github-agent-workflow.md` | adapt | 平台工作模式 Guide；不升级成跨平台 Runtime 前提 |
| `docs/guides/multi-model-collaboration.md` | adapt | 可选方法知识；真正执行由 Skill 负责 |
| `docs/guides/codex-model-collaboration-reference.md` | retain | Codex 平台非规范参考 |
| `docs/guides/language-and-terminology.md` | adapt | 解释项目语言 / 概念约定；不作为 Consumer 强制语言 Rule |
| `docs/guides/adopting-agentic-dev.md` | adapt | 重写为 Existing Project 最小侵入 Adoption |
| `docs/guides/upgrading-agentic-dev.md` | adapt | 重写为标准 Skills 精确版本更新 |
| `docs/guides/rule-activation-guide.md` | adapt → retire | 与 Consumer-local constraints Guide 合并，删除旧五维 Rule Runtime 教程 |
| `docs/guides/consumer-local-rule-activation.md` | adapt | 重构为 Consumer-local constraints 组织 / 按需加载指南；若合并后由新文件接管则 retire |

### 5.2 新增必要入口

后续实施需要补齐：

- `docs/guides/getting-started.md`：最短人类 / AI 总入口；
- `docs/guides/bootstrap-new-project.md`：预 Consumer runtime 的有界 Bootstrap 编排；
- `docs/guides/choosing-next-step.md`：结合 Consumer current facts 判断下一责任；
- 可选的 ChatGPT + WebCodex Layer 0 Project Instructions 模板，作为 Guide 示例而非 runtime Authority。

## 6. Skills

15 个现有 Skill 全部 **retain + adapt**，因为 Gate F 已证明它们覆盖核心软件开发 obligation，且新模型把它们提升为 canonical Consumer product：

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

统一适配：

1. 删除 `agentic-dev-distribution`、`agentic-dev-release-target`、`agentic-dev-release-inputs` 等旧编译 / 发布元数据；
2. 将真正需要的 Method / Architecture / Rule 语义直接收敛到 `SKILL.md` 或 Skill-local `references/**`；
3. Skill root 本身必须可由标准 Agent Skills 工具直接识别 / 安装；
4. 单个 Skill 不依赖 Provider `docs/**` 才能完成其通用责任；
5. 不为了消除旧 Rule 文件把所有知识塞进 `SKILL.md`；长知识使用 Skill-local progressive-disclosure references。

`skills/README.md`：adapt，为人和维护者提供产品 inventory；Agent 仍使用原生 Skill discovery。

## 7. Rule 资产

### 7.1 明确保留为 Provider-local

| 资产 | 处置 |
|---|---|
| `docs/rules/repository/git-commit-discipline.md` | retain，Provider-local |
| `docs/rules/repository/human-facing-content-integrity.md` | retain，Provider-local |
| `docs/rules/repository/high-impact-ai-review-required.md` | adapt，保留为 Provider-local 高影响复核策略；不再作为 Consumer release input |

### 7.2 Consumer 语义迁入 Skills 后退出 release-input 身份

以下文件全部为 **adapt**：先把仍需的通用软件开发语义写入相应 canonical Skill / reference；随后不再保留为 Consumer distribution input。若没有独立 Provider-local 价值则 retire。

| Rule | 主要目标 Skill / owner |
|---|---|
| `generation/data-access-boundedness.md` | `technical-plan` / `execute-unit` |
| `generation/implementation-discipline.md` | `execute-unit` / `systematic-debug` |
| `operations/async-operation-bounded-observation.md` | `external-operation` / `github-actions-verification` |
| `operations/cross-repository-authorization.md` | `external-operation` |
| `operations/external-binary-content-validation.md` | `external-operation` / `execute-unit` |
| `operations/human-intervention-necessity.md` | 各 Skill 的 Escalation contract |
| `operations/safe-external-write.md` | `external-operation` |
| `operations/shared-resource-concurrency-ownership.md` | `external-operation` / `activate-model-collaboration` |
| `operations/temporary-evidence-to-persistent-input-promotion.md` | `external-operation` / `converge` |
| `repository/authoritative-artifact-lifecycle-review.md` | `review-change` / `converge` |
| `repository/integration-state-closure-review.md` | `review-change` / `converge` |
| `verification/database-migration-completion-evidence.md` | `execute-unit` / `converge` |
| `verification/evidence-claim-reuse-across-commits.md` | `review-change` / `github-actions-verification` / `converge` |
| `verification/evidence-type-must-match-claim.md` | 通用 Verification references；Provider 若仍需可另保留 local policy |
| `verification/human-review-baseline-isolation.md` | `human-review` |
| `verification/verification-contract-currentness.md` | `execute-unit` / `review-change` / `converge` |
| `verification/visual-evidence.md` | `human-review` / `review-change` / `execute-unit` |

RC-only 两条 Rule 见 §12，语义保留但不按旧 release-input 形式进入新模型。

跨多个 Skill 适用的 Rule 不通过“把旧 Rule 正文复制到每个 Skill”迁移。每个 Skill 只拥有与自身责任相关的可执行投影；跨 Skill 的一致性通过 Provider-side invariant / behavior tests 保证。不得为了避免复制而让已安装 Skill 重新依赖 Provider `docs/rules/**` 或新增 Skill 外共享 runtime namespace。

`docs/rules/README.md`：adapt 为 Provider-local rule 导航；不得继续充当通用 Consumer Rule inventory。

## 8. Rule Discovery / Capability Runtime

以下机制的历史问题意识保留，但当前实现退出长期目标：

| 资产 | 处置 |
|---|---|
| `tools/rule-discovery/rule_discovery.py` | retire，在 Consumer-local constraints 最小方案和 Provider Bootstrap 已替代后删除 |
| `.github/workflows/rule-discovery.yml` | retire |
| `tools/rule-discovery/tests/test_rule_discovery.py` | retire / 只迁移仍适用的通用 fail-closed test idea |
| `test_rule_discovery_cli.py` | retire |
| `test_v4_discovery_eval.py` | retire |
| `test_v4_scaling_eval.py` | retire |
| `test_capability_model.py` | retire |
| `test_method_corpus.py` | retire |
| `test_runtime_activation.py` | adapt，只保留新 Bootstrap / Skill activation 仍需场景 |
| `test_repository_bootstrap_closure.py` | adapt 为新薄 Bootstrap contract |
| `test_bootstrap_cost_reduction.py` | adapt，继续验证 bounded bootstrap / progressive disclosure |
| `test_human_intervention_necessity.py` | adapt 到 Skill Escalation contract |
| `test_human_navigation.py` | adapt 为 Guide Human + AI navigation contract |
| `test_human_review_capability.py` | adapt 到 `human-review` Skill / Guide |
| `test_review_governance.py` | adapt 到 `review-change` Skill / Provider policy |
| `test_eval_runner_integrity.py` | retain + adapt，作为 eval/runtime Evidence integrity |

Consumer-local constraints 的新机制必须先通过小型 fixture / real Consumer Evidence 选择，不把当前 Rule Discovery 代码直接改名保留。

## 9. Distribution / Release infrastructure

| 资产 | 处置 |
|---|---|
| `tools/distribution-audit/distribution_audit.py` | retire，完成本轮迁移检查后删除 |
| `tools/distribution-audit/tests/test_distribution_audit.py` | retire |
| `tools/distribution-audit/tests/test_legacy_consumer_coverage.py` | adapt；历史 26 obligation coverage 可转为新模型回归检查 |
| `tools/release-build/release_build.py` | retire |
| `tools/release-build/install_release.py` | retire |
| `tools/release-build/tests/test_release_build.py` | retire；仅迁移仍适用于标准 Skill install 的 provenance / idempotency / conflict 思想 |
| `.github/workflows/release-build.yml` | retire |
| `.github/workflows/runtime-acceptance.yml` | adapt，为直接从 canonical `skills/**` / 标准 installer 建立 fixture 后验证 |
| `tools/runtime-acceptance/runtime_acceptance.py` | adapt |
| `tools/runtime-acceptance/tests/test_runtime_acceptance.py` | adapt |
| `tools/runtime-acceptance/authenticated_model_acceptance.py` | retain + adapt |
| `tools/runtime-acceptance/tests/test_authenticated_model_acceptance.py` | retain；该文件当前只存在 RC-only delta，按 §12 引入新基线 |

原则：删除的是自定义 packaging / semantic compilation，不删除 exact-subject、integrity、negative-control、authenticated runtime 等验证思想。

## 10. Evals

### 10.1 保留并适配

- `evals/activation/core-first-pass.json`：adapt，为 canonical Skills / direct install activation；
- `evals/behavior/*.json` 15 个 Skill 行为 corpus：retain + adapt；
- `evals/fixtures/execute-unit-basic/**`：retain；
- `evals/fixtures/github-actions-observation/**`：retain；
- `evals/fixtures/legacy-consumer-coverage/gate-f.json`：retain 为历史 coverage Evidence，并派生新模型 regression；
- `evals/run_codex_evals.py`：adapt，去除自定义 Release Build 前提，保留 bounded process、Fresh Context、Evidence integrity；
- `evals/run_codex_grader.py`：retain + adapt；
- `evals/run_governance_evals.py`：adapt 为 Provider governance / Guide / Bootstrap 测试；
- `evals/CODEX.md`、`evals/README.md`：adapt；
- `evals/governance/chinese-human-facing-output.json`：retain；
- `evals/governance/formal-concept-semantic-safety.json`：adapt；
- `evals/governance/stacked-pr-integration-topology.json`：retain，若后续仍验证 GitHub integration safety。

### 10.2 退出旧 Runtime 模型

- `evals/discovery/v4-discriminating.json`：retire；
- `evals/discovery/v4-scaling.json`：retire；
- `evals/discovery/README.md`：retire；
- `evals/run_v4_scaling.py`：retire；
- `evals/governance/method-object-semantic-safety.json`：adapt 后若只验证旧 Method runtime identity 则 retire；
- `evals/bootstrap/r3-cost-baseline.json`：retain 为历史 baseline，可用于证明新 Bootstrap 没有再次膨胀。

## 11. Research

`docs/research/**` 默认 **retain**。它们不进入 ordinary runtime，保留历史研究成本很低，同时可以解释本轮为何改变方向。

特别保留：

- `distribution-model-evidence-review.md`；
- `legacy-consumer-capability-coverage-audit.md`；
- `mattpocock-skills-analysis.md`；
- `agent-skills-specification-analysis.md`；
- Rule retrieval / knowledge activation 系列研究。

`docs/research/README.md` 需要 adapt：明确旧 Capability / Distribution 研究可能是 historical evidence，不代表 Current target model。

## 12. 冻结 RC-only delta

冻结 RC source tag `51db05801382b74ee01601f391305fcbbff98db3` 相对 `master@87a6ff8e1ba29baf8154c605bf1fbfef14574c8d` 有 34 个 changed paths。逐项 disposition 如下。

### 12.1 retain / adapt

| RC-only path | disposition | 理由 |
|---|---|---|
| `docs/architecture/model-collaboration-architecture.md` | adapt | 保留 Execution Context ≠ Runtime Under Test 原则，迁入 collaboration Skill/reference |
| `docs/architecture/skill-architecture.md` | adapt | RC 中与 Skill 独立性 / validation 相关改进进入新 Skill Architecture |
| `docs/rules/operations/execution-continuity-and-stop-condition.md` | adapt | 语义保留，进入相关 Skills / Guide；不保留为 release-input Rule |
| `docs/rules/verification/execution-context-runtime-boundary.md` | adapt | 语义保留，进入 review / collaboration / runtime verification references |
| `evals/activation/core-first-pass.json` | adapt | 保留 RC 新场景意图，改为直接 Skill install |
| `evals/behavior/activate-model-collaboration.json` | adapt | 保留 Runtime Under Test 行为断言 |
| `evals/run_codex_evals.py` | adapt | 保留 bounded process、cancellation、stale evidence cleanup 等通用运行可靠性 |
| 15 个 `skills/*/SKILL.md` | retain + adapt | 保留 RC 引入的 continuity / isolation 等语义；删除 release-input composition metadata |
| `tools/rule-discovery/tests/test_bootstrap_cost_reduction.py` | adapt | 保留 Bootstrap 成本约束 |
| `tools/rule-discovery/tests/test_eval_runner_integrity.py` | retain + adapt | 保留 process cancellation、stale evidence、identity binding 等测试 |
| `tools/rule-discovery/tests/test_rule_discovery.py` | adapt | 只迁移与新局部约束方案仍成立的 fail-closed / bounded-context invariant |
| `tools/rule-discovery/tests/test_rule_discovery_cli.py` | adapt | 同上；旧 CLI contract 本身不保留 |
| `tools/runtime-acceptance/authenticated_model_acceptance.py` | retain + adapt | 保留 scenario / source / runtime / grader identity binding 与 evidence schema |
| `tools/runtime-acceptance/tests/test_authenticated_model_acceptance.py` | retain | 将 RC-only 新测试带入新基线并改为 canonical Skill runtime subject |

### 12.2 drop-with-reason

| RC-only path | disposition | 理由 |
|---|---|---|
| `docs/architecture/release-architecture.md` | drop-with-reason | RC 增量绑定旧 custom Release / Evidence finalization；新模型不继续该包装架构 |
| `docs/project/project-capability-profile.md` | drop-with-reason | RC 增量属于旧 Provider capability instance / Release runtime |
| `docs/project/project-roadmap.md` | drop-with-reason | RC Gate G/H 状态已被新 Roadmap 取代 |
| `docs/rules/README.md` | drop-with-reason | RC 增量主要服务新增 release-input Rule inventory；新模型重新整理 Provider-local rules |
| `tools/release-build/release_build.py` | drop-with-reason | 602 行新增主要服务 finalizer / evidence binding / custom archive；通用 provenance 思想另迁标准安装验证 |
| `tools/release-build/tests/test_release_build.py` | drop-with-reason | 709 行新增主要验证旧 finalizer / archive contract；仅抽取适用于标准 install 的通用 invariant，不保留旧测试面 |

以上分类覆盖 34 个 changed paths；15 个 Skill 以单组列出但每个 path 均为 retain + adapt，不存在未分类 RC-only 文件。

## 13. Legacy Consumer 26 obligation 对新模型的重新映射

Gate F 的 26 项不继续使用旧 `release-covered / release-composed` 术语，而改为检查新 owner：

- GF-03～GF-18 的可执行软件开发责任：由 canonical Skills 直接拥有；
- GF-01、GF-19～GF-22：继续 Consumer-local；
- GF-02：由 Bootstrap Guide + Consumer thin `AGENTS.md` + installed Skills 覆盖；
- GF-23：普通执行由 installed Skills + Consumer Authority 实现；方法论咨询才通过精确 Guide locator 按需访问；
- GF-24：由标准 Skills install / update Guide 覆盖；
- GF-25：由 executable Skills 自身 direct / alternate / fail-closed contract 覆盖；
- GF-26：由 Skill-local Evidence semantics + runtime/eval exact-subject checks 覆盖。

因此旧 coverage Evidence 继续作为“不能因减法重构丢失能力”的回归 oracle，而不要求保留旧文件类型或 Release Builder。

## 14. 资产处置结论

本次 disposition 没有发现必须继续保留以下机制才能覆盖现有软件开发责任的证据：

- Consumer Method runtime / selector；
- upstream Rule runtime；
- Project Capability Profile；
- Source distribution classification；
- Release semantic transformation；
- custom ZIP / installer；
- Provider / Consumer 同构 Capability Model。

需要保留的是它们曾解决的真实问题：bounded context、Consumer ownership、local constraints、Fresh Context、Evidence integrity、runtime-specific verification、human escalation 与 independent review。

下一步可以据此制定实施计划；实施计划必须先完成“语义迁移，再删除旧 owner”，避免减法过程中丢失 Gate F / RC 已验证责任。
