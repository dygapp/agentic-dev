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

S1 起统一使用三种极简 disposition：

- **Keep**：长期职责仍然成立，继续作为 Current asset；
- **Simplify**：保留真实需求，但压缩 owner、加载方式或实现，不能继续维持旧运行时复杂度；
- **Delete after semantic migration**：当前文件 / 机制退出 Current path；必要长期语义先迁移，再删除工作树中的旧 owner。

历史表格中的 `retain / adapt / retire` 仍可作为旧审计记录理解，但 S2 实施决策以 Keep / Simplify / Delete after semantic migration 为准。任何 Delete 都不表示删除 Git 历史。

## 2. 根入口与 Project Knowledge

| 资产 | 处置 | 目标 |
|---|---|---|
| `AGENTS.md` | adapt | 收敛为 Provider 自身薄 Repository Bootstrap；移除统一 Capability Runtime、Method selector、发布分类与复杂 Rule Discovery 的固定依赖 |
| `README.md` | adapt | 成为人类入口，直接解释 Guides + Skills + Consumer-local Authority 的产品模型 |
| `docs/project/project-charter.md` | adapt | 移除“Provider 必须 self-consume Consumer runtime”与旧 Distribution Build 使命；保留软件项目适用域、Consumer ownership、Evidence-driven evolution |
| `docs/project/project-capability-profile.md` | retire | 统一 Capability instance / Method selector / Release Build locator 不再是目标模型；仍有价值的 Provider runtime locator 回到薄 Bootstrap 或实际工具文档 |
| `docs/project/project-roadmap.md` | Keep | 继续拥有当前 evolution / stage / next candidate 的紧凑状态 |
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
| `docs/guides/rule-activation-guide.md` | retired in P4 | 已由 `consumer-local-constraints.md` 的 v1 最小约定接管；不再保留旧五维 Rule Runtime 教程 |
| `docs/guides/consumer-local-rule-activation.md` | retired in P4 | Consumer-local constraints ownership / progressive disclosure 已由 `consumer-local-constraints.md` 接管 |

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

## 7. Provider Governance / Rule 资产

S2 不保留“少量规则 + 通用发现引擎”的折中形态。需要长期约束 Provider 的语义直接进入少量 governance owner，由薄 `AGENTS.md` 明确指向，不再依赖 Rule metadata、五维 signal 或候选发现。

### 7.1 Keep / Simplify 为直接治理正文

| 当前资产 / 语义 | S1 disposition | S2 目标 |
|---|---|---|
| `docs/rules/repository/git-commit-discipline.md` | Simplify | 迁入直接 Git governance owner，例如 `docs/governance/git-conventions.md` |
| `docs/rules/repository/human-facing-content-integrity.md` | Simplify | 迁入语言 / 术语 governance owner，例如 `docs/governance/language-and-writing.md` |
| `docs/rules/repository/high-impact-ai-review-required.md` | Simplify | 与 Evidence 匹配合并到重大变更复核 owner |
| `docs/rules/verification/evidence-type-must-match-claim.md` | Simplify | 与重大变更复核共同形成最小 verification governance |
| authoritative artifact / documentation lifecycle 相关长期语义 | Simplify | 进入文档 Authority governance owner |
| Provider 外部写授权的必要原则 | Simplify | 保留在薄 `AGENTS.md`、直接 governance 或 `external-operation` Skill 中，不保留通用 Rule Discovery |

这些治理正文只约束 Provider 自身；不因为它们存在就恢复 Consumer Rule Runtime。

### 7.2 Consumer 通用执行语义

旧 release-input Rules 中已经被 P2 投影进 canonical Skills 的通用执行语义，以 Skills 为长期 owner。S2 不再为了保存旧 Rule 文件而保留第二份正文。

仍未迁出的个别长期语义必须先进入对应 Skill / Skill-local reference 或上述 Provider governance；确认新 owner 后，原 Rule 文件归入 Delete after semantic migration。

`docs/rules/README.md` 不再作为长期 runtime inventory；若 Provider governance 已直接化，则随旧 Rule tree 一并退出或仅保留必要的人类迁移说明。

## 8. Rule Discovery / Capability Runtime

| 资产 | S1 disposition | S2 处理 |
|---|---|---|
| `tools/rule-discovery/rule_discovery.py` | Delete after semantic migration | Provider governance 直接化后删除 |
| `.github/workflows/rule-discovery.yml` | Delete after semantic migration | 不再保留 task-level Rule Discovery transport |
| Rule metadata / 五维 signal contract | Delete after semantic migration | 不建立替代 Rule Engine |
| `tools/rule-discovery/tests/test_rule_discovery.py` | Delete after semantic migration | 只把仍有价值的 fail-closed 思想投影到最小 deterministic tests |
| `test_rule_discovery_cli.py` / `test_v4_discovery_eval.py` / `test_v4_scaling_eval.py` | Delete after semantic migration | 旧 CLI / scaling contract 不再验证 |
| `test_capability_model.py` / `test_method_corpus.py` | Delete after semantic migration | 旧 Capability / Method runtime 退出 |
| `test_repository_bootstrap_closure.py` | Simplify | 改为薄 `AGENTS.md` + 直接 governance locator 静态检查 |
| `test_bootstrap_cost_reduction.py` | Simplify / Keep | 保留 bounded bootstrap / progressive disclosure 的低成本静态约束 |
| human navigation / review 相关 tests | Simplify | 只保留能静态验证 Guide / Skill / governance 边界的最小检查 |
| `test_eval_runner_integrity.py` | Delete after semantic migration | 迁出 WebCodex→`codex-cli` 禁止边界和仍必要的最小 process invariant 后删除批量 Eval runner 测试面 |

Consumer-local constraints 已由 P4 证明简单机制足够；本轮不再要求真实 Consumer applicability challenge，也不把当前 Rule Discovery 代码改名保留。

## 9. Distribution / Release infrastructure

| 资产 | S1 disposition | S2 处理 |
|---|---|---|
| `tools/distribution-audit/distribution_audit.py` 及旧 classification tests | Delete after semantic migration | 完成一次最终静态迁移核对后删除 |
| `tools/distribution-audit/tests/test_legacy_consumer_coverage.py` | Simplify | 转为 26 obligation 静态 owner 映射检查 |
| `tools/release-build/release_build.py` | Delete after semantic migration | custom packaging / semantic compilation 退出 |
| `tools/release-build/install_release.py` | Delete after semantic migration | 普通安装回到标准 Skills 兼容路径 |
| `tools/release-build/tests/test_release_build.py` | Delete after semantic migration | 只迁出 Consumer-owned 文件不覆盖、必要 provenance / idempotency invariant |
| `.github/workflows/release-build.yml` | Delete after semantic migration | 不再构建 custom archive |
| `.github/workflows/runtime-acceptance.yml` | Simplify | 若保留，只执行 canonical Skills 的 deterministic / isolated smoke，不安装或调用 `codex-cli` |
| `tools/runtime-acceptance/runtime_acceptance.py` | Simplify | 缩成 isolated Consumer fixture、Skill copy / install integrity、Consumer-owned 文件保护与必要 negative control |
| `tools/runtime-acceptance/tests/test_runtime_acceptance.py` | Simplify / Keep | 只覆盖上述最小 runtime smoke |
| `tools/runtime-acceptance/authenticated_model_acceptance.py` | Delete after semantic migration | exact-subject / Evidence 绑定中仍必要的静态思想迁出后删除；不再作为默认验收 orchestrator |
| `tools/runtime-acceptance/tests/test_authenticated_model_acceptance.py` | Delete after semantic migration | 不再维护 14+14 批量模型验收面 |

保留的是 exact-subject、Consumer ownership、integrity、negative control 和 isolated smoke 等问题意识，而不是旧 Release Finalizer、authenticated batch model runtime 或独立 grader 基础设施。

Codex-specific Runtime Under Test 如未来确有必要，由非 WebCodex 独立子任务临时授权执行；它不是 S3 默认完成路径。

## 10. Evals

S3 不保留批量模型自测作为 Provider 日常验证基础设施。

### 10.1 Keep / Simplify

- `evals/fixtures/legacy-consumer-coverage/gate-f.json`：Keep，作为 26 obligation 历史回归 oracle，仅做静态 owner 映射；
- `evals/bootstrap/r3-cost-baseline.json`：Keep 为历史 Bootstrap 成本基线；
- S3 所需的 disposable install / Consumer-owned file fixture：Simplify，只保留一个能够区分安装、覆盖保护和最小 runtime 边界的 fixture；
- `evals/README.md`：若仍有必要则 Simplify 为最小验证说明，否则删除。

### 10.2 Delete after semantic migration

以下资产不再属于 Current validation path：

- `evals/activation/core-first-pass.json`；
- `evals/behavior/*.json` 批量 Skill 模型行为 corpus；
- `evals/run_codex_evals.py`；
- `evals/run_codex_grader.py`；
- `evals/run_governance_evals.py`；
- `evals/run_v4_scaling.py` 与 `evals/discovery/**`；
- 只为模型语义评分存在的 `evals/governance/*.json`；
- `evals/CODEX.md` 中只服务批量运行器的部分。

删除前只迁移仍有长期价值的内容：WebCodex 不得调用 `codex-cli` 的执行边界、必要的 timeout / fail-closed 经验、Consumer-owned 文件保护、少量跨 Skill deterministic invariant。语义判断与 Fresh Review 回到 ChatGPT，不再通过第二套模型 grader 模拟独立性。

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

本节保留 PB-AC-29 已冻结审计时的 `retain / adapt / drop-with-reason` 历史语义；S1 当前实施动作以前文 Keep / Simplify / Delete after semantic migration 为准。历史 `adapt` 可以在长期语义迁出后对应当前的 Delete after semantic migration，两者不构成双重 Current Authority。

### 12.1 retain / adapt

| RC-only path | disposition | 理由 |
|---|---|---|
| `docs/architecture/model-collaboration-architecture.md` | adapt | 保留 Execution Context ≠ Runtime Under Test 原则，迁入 collaboration Skill/reference |
| `docs/architecture/skill-architecture.md` | adapt | RC 中与 Skill 独立性 / validation 相关改进进入新 Skill Architecture |
| `docs/rules/operations/execution-continuity-and-stop-condition.md` | adapt | 语义保留，进入相关 Skills / Guide；不保留为 release-input Rule |
| `docs/rules/verification/execution-context-runtime-boundary.md` | adapt | 语义保留，进入 review / collaboration / runtime verification references |
| `evals/activation/core-first-pass.json` | Delete after semantic migration | Skill activation 的必要静态责任进入 S3 最小检查；不保留批量模型场景 |
| `evals/behavior/activate-model-collaboration.json` | Delete after semantic migration | Execution Context ≠ Runtime Under Test 语义已迁入 Skill / governance；真实 Codex Runtime 仅按需独立验证 |
| `evals/run_codex_evals.py` | Delete after semantic migration | 只迁出仍必要的 timeout / fail-closed 与 WebCodex 禁止调用 Codex CLI 语义 |
| 15 个 `skills/*/SKILL.md` | retain + adapt | 保留 RC 引入的 continuity / isolation 等语义；删除 release-input composition metadata |
| `tools/rule-discovery/tests/test_bootstrap_cost_reduction.py` | adapt | 保留 Bootstrap 成本约束 |
| `tools/rule-discovery/tests/test_eval_runner_integrity.py` | Delete after semantic migration | 最小 invariant 迁到 S3 deterministic tests 后删除旧 Eval runner 测试面 |
| `tools/rule-discovery/tests/test_rule_discovery.py` | adapt | 只迁移与新局部约束方案仍成立的 fail-closed / bounded-context invariant |
| `tools/rule-discovery/tests/test_rule_discovery_cli.py` | adapt | 同上；旧 CLI contract 本身不保留 |
| `tools/runtime-acceptance/authenticated_model_acceptance.py` | Delete after semantic migration | 不再由 Provider orchestrator 批量调用 codex-cli；只迁出必要 exact-subject / Evidence 绑定思想 |
| `tools/runtime-acceptance/tests/test_authenticated_model_acceptance.py` | Delete after semantic migration | 不保留批量 authenticated model acceptance 测试面 |

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
- GF-26：由 Skill-local Evidence semantics + S3 最小 exact-subject deterministic / isolated smoke 覆盖。

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

S1 起按 Keep / Simplify / Delete after semantic migration 执行。S2 必须先迁移长期语义再删除旧 owner；S3 只保留最小 deterministic / isolated smoke 与 Fresh Independent Review。真实 Consumer adoption 不再是完成门槛，未来采用反馈进入正常产品反馈，不自动重开基础设施重构。
