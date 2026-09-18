---
id: guide:rules-navigation
type: guide
status: active
---

# Rule 目录导航

本 README 只用于**人类导航**，不是 runtime Rule index。Rule Discovery 会明确跳过名为 `README.md` 的导航文件，但 repository lint 仍会校验本文件 Front Matter 与资源 ID。

运行时规则发现只读取各 Rule 自身 YAML Front Matter；本 README 不保存 phases / activities / technologies / artifacts / risks，不维护 Rule→token、keyword、priority 或 activation routing。

## Rule 粒度

当前 Rule 以**具体任务 / 责任级规范集合**为默认自然边界，不再把每条可独立表述的 policy 机械拆成一个文件。同一任务中通常共同发现、共同消费的相关 policy 优先聚合；只有独立 discovery 能减少无关加载或错误激活时才继续拆分。

文件大小与 Progressive Disclosure 的长期标准见 `docs/architecture/rule-architecture.md`。Agent Skills 的 `<5000 tokens / <500 lines` 只作为上限复核参照，不是 Rule 的目标大小或自动拆分阈值。

## Rule 分类

- `generation/` — 实现生成、变更范围与数据访问等通用生成约束；
- `operations/` — 外部可变状态、授权、写后验证、并发、人工升级必要性与证据持久化约束；
- `repository/` — Repository Authority、Git、表达、概念身份与 Review / Integration 约束；
- `verification/` — Evidence、验证、迁移完成声明与人工复核约束。

当前 upstream corpus 不维护具体语言 / 框架 / 组件库的通用技术知识 Rule family。Consumer 如有稳定、项目特定的技术 policy，仍可按自己的 Authority 建立 local technology Rules；目录只服务人类维护，不参与 runtime matching。

## 当前 Rule 清单

### generation

- [`data-access-boundedness.md`](generation/data-access-boundedness.md)
- [`implementation-discipline.md`](generation/implementation-discipline.md)

### operations

- [`async-operation-bounded-observation.md`](operations/async-operation-bounded-observation.md)
- [`cross-repository-authorization.md`](operations/cross-repository-authorization.md)
- [`external-binary-content-validation.md`](operations/external-binary-content-validation.md)
- [`human-intervention-necessity.md`](operations/human-intervention-necessity.md)
- [`safe-external-write.md`](operations/safe-external-write.md)
- [`shared-resource-concurrency-ownership.md`](operations/shared-resource-concurrency-ownership.md)
- [`temporary-evidence-to-persistent-input-promotion.md`](operations/temporary-evidence-to-persistent-input-promotion.md)

### repository

- [`authoritative-artifact-lifecycle-review.md`](repository/authoritative-artifact-lifecycle-review.md)
- [`git-commit-discipline.md`](repository/git-commit-discipline.md)
- [`high-impact-ai-review-required.md`](repository/high-impact-ai-review-required.md)
- [`human-facing-content-integrity.md`](repository/human-facing-content-integrity.md)
- [`integration-state-closure-review.md`](repository/integration-state-closure-review.md)


### verification

- [`database-migration-completion-evidence.md`](verification/database-migration-completion-evidence.md)
- [`evidence-claim-reuse-across-commits.md`](verification/evidence-claim-reuse-across-commits.md)
- [`evidence-type-must-match-claim.md`](verification/evidence-type-must-match-claim.md)
- [`human-review-baseline-isolation.md`](verification/human-review-baseline-isolation.md)
- [`verification-contract-currentness.md`](verification/verification-contract-currentness.md)
- [`visual-evidence.md`](verification/visual-evidence.md)

当前共 20 条 discoverable Rule。该数量不是目标 KPI；增减只按 `docs/architecture/rule-architecture.md` 的任务级语义边界、独立 discovery 价值和总加载成本判断。