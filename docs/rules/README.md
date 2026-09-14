---
id: guide:rules-navigation
type: guide
status: active
---

# Rules 目录导航

本 README 只用于**人类导航**，不是 runtime Rule index。Rule Discovery 会明确跳过名为 `README.md` 的导航文件，但 repository lint 仍会校验本文件 Front Matter 与资源 ID。

运行时规则发现只读取各 Rule 自身 YAML Front Matter；本 README 不保存 phases / activities / technologies / artifacts / risks，不维护 Rule→token、keyword、priority 或 activation routing。

## Rule 分类

- `generation/` — 实现生成、变更范围与数据访问等通用生成约束；
- `operations/` — 外部可变状态、授权、写后验证、并发与证据持久化约束；
- `repository/` — Repository Authority、Git、表达、概念身份与 Review / Integration 约束；
- `technology/` — 技术 / 框架特定约束，目前主要为 TypeScript / Vue；
- `verification/` — Evidence、验证、迁移完成声明与人工复核约束。

## 当前 Rule inventory

### generation

- [`data-access-boundedness.md`](generation/data-access-boundedness.md)
- [`implementation-minimality.md`](generation/implementation-minimality.md)
- [`surgical-change.md`](generation/surgical-change.md)

### operations

- [`async-operation-bounded-observation.md`](operations/async-operation-bounded-observation.md)
- [`cross-repository-authorization.md`](operations/cross-repository-authorization.md)
- [`external-binary-content-validation.md`](operations/external-binary-content-validation.md)
- [`external-operation-authorization-boundary.md`](operations/external-operation-authorization-boundary.md)
- [`minimal-external-change.md`](operations/minimal-external-change.md)
- [`post-write-state-verification.md`](operations/post-write-state-verification.md)
- [`shared-resource-concurrency-ownership.md`](operations/shared-resource-concurrency-ownership.md)
- [`temporary-evidence-to-persistent-input-promotion.md`](operations/temporary-evidence-to-persistent-input-promotion.md)

### repository

- [`authoritative-artifact-lifecycle-review.md`](repository/authoritative-artifact-lifecycle-review.md)
- [`exact-machine-identifiers.md`](repository/exact-machine-identifiers.md)
- [`formal-concept-identity-safety.md`](repository/formal-concept-identity-safety.md)
- [`git-authority-layer-ordering.md`](repository/git-authority-layer-ordering.md)
- [`git-breaking-change-marker.md`](repository/git-breaking-change-marker.md)
- [`git-commit-format-and-language.md`](repository/git-commit-format-and-language.md)
- [`git-commit-single-purpose.md`](repository/git-commit-single-purpose.md)
- [`high-impact-ai-review-required.md`](repository/high-impact-ai-review-required.md)
- [`human-facing-chinese-default.md`](repository/human-facing-chinese-default.md)
- [`integration-state-closure-review.md`](repository/integration-state-closure-review.md)

### technology

- [`avoid-any-as-default.md`](technology/avoid-any-as-default.md)
- [`official-vue-tsconfig-starting-point.md`](technology/official-vue-tsconfig-starting-point.md)
- [`preserve-type-inference.md`](technology/preserve-type-inference.md)
- [`strict-default-for-new-or-authorized-projects.md`](technology/strict-default-for-new-or-authorized-projects.md)
- [`vue-async-watcher-cleanup.md`](technology/vue-async-watcher-cleanup.md)
- [`vue-build-vs-typecheck.md`](technology/vue-build-vs-typecheck.md)
- [`vue-composable-reactivity-return-shape.md`](technology/vue-composable-reactivity-return-shape.md)
- [`vue-computed-purity.md`](technology/vue-computed-purity.md)
- [`vue-define-model-default.md`](technology/vue-define-model-default.md)
- [`vue-props-emits-declaration-mode.md`](technology/vue-props-emits-declaration-mode.md)
- [`vue-props-one-way-input.md`](technology/vue-props-one-way-input.md)
- [`vue-reactive-generic-boundary.md`](technology/vue-reactive-generic-boundary.md)
- [`vue-risk-based-browser-visual-verification.md`](technology/vue-risk-based-browser-visual-verification.md)
- [`vue-script-setup-default.md`](technology/vue-script-setup-default.md)
- [`vue-template-ref-dom-timing.md`](technology/vue-template-ref-dom-timing.md)
- [`vue-template-ref-nullability.md`](technology/vue-template-ref-nullability.md)
- [`vue-use-template-ref-default.md`](technology/vue-use-template-ref-default.md)
- [`vue-watcher-dependency-tracking.md`](technology/vue-watcher-dependency-tracking.md)

### verification

- [`database-migration-completion-evidence.md`](verification/database-migration-completion-evidence.md)
- [`evidence-claim-reuse-across-commits.md`](verification/evidence-claim-reuse-across-commits.md)
- [`evidence-type-must-match-claim.md`](verification/evidence-type-must-match-claim.md)
- [`human-review-baseline-isolation.md`](verification/human-review-baseline-isolation.md)
- [`verification-contract-currentness.md`](verification/verification-contract-currentness.md)
- [`visual-evidence.md`](verification/visual-evidence.md)

当前共 45 条 discoverable Rule。Rule 是否拆分 / 合并以 `docs/architecture/rule-architecture.md` 的独立发现、独立适用和独立演进标准判断，不按文件长度机械处理。