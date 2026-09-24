---
id: guide:consumer-local-constraints
type: guide
status: active
distribution: source-only
---

# Consumer-local Constraints

普通软件项目在开发过程中会沉淀自己的技术规则、数据迁移约束、安全政策、验证要求、外部操作边界和模块级约定。

这些内容属于 Consumer，不属于 `agentic-dev` 通用 Skills。

本 Guide 只冻结**职责边界**。具体最小发现机制由产品边界重构 P4 通过 disposable fixture 和真实 Consumer applicability challenge 验证后再确定；当前不预设需要复制 `agentic-dev` 的 Rule Discovery。

## 1. 为什么不能全部写进根 AGENTS.md

如果所有约束都进入根 `AGENTS.md`：

- Bootstrap 会持续膨胀；
- 与当前任务无关的规则长期占用上下文；
- path / module / activity scoped policy 很难维护；
- 一个局部规则变化会影响所有任务的启动输入。

因此根 `AGENTS.md` 只适合极少量真正 repository-wide、稳定、每次都必须知道的约束，以及指向其他本地约束的稳定 locator。

## 2. 三类常见约束

### Repository-wide stable policy

几乎所有工作都适用，例如：

- 事实来源 / Authority 原则；
- 明确的安全红线；
- 全仓统一的提交 / 合并权限边界。

这类内容可以少量进入根 `AGENTS.md`。

### Path / module scoped policy

只对某个目录、模块或技术区生效，例如：

- 前端模块的 Vue / TypeScript 约定；
- 某个数据库模块的 migration 约定；
- 某个部署目录的基础设施规则。

优先利用 nested `AGENTS.md` 或宿主原生 scoped instructions 等自然作用域机制。

### Activity / semantic scoped policy

与文件路径不完全重合，只在某类责任发生时适用，例如：

- 外部写操作；
- 业务数据迁移；
- 高影响人工评审；
- 生产环境验证。

这类约束可能需要 Consumer-local policy docs + 薄 locator。只有真实项目证明简单机制不足时，才考虑最小 metadata / filter。

## 3. Ownership

Consumer-local constraint 必须满足：

- 正文由 Consumer Repository 自己拥有；
- `agentic-dev` update 不自动覆盖；
- 不需要在线访问 upstream 才能知道本地项目规则；
- 不把本地 Product / Requirement fact 塞进通用 Skill；
- 不因为规则数量增加就默认全量加载。

## 4. Skill 怎样与本地约束配合

通用 Skill 负责：

> “这类软件开发工作通常怎样安全完成？”

Consumer-local constraint 负责：

> “在这个具体项目里，做这件事还必须遵守什么？”

例如 `execute-unit` 可以要求遵守当前 Consumer-local constraints，但它不会内置某个 Consumer 的 Vue lint、KingbaseES migration、生产部署审批等本地政策。

## 5. Fail-closed 的边界

“没有适用本地约束”和“约束系统损坏”不是一回事。

- 已经可靠判断当前任务没有额外 local constraint → 正常继续；
- Repository 声明存在 constraint locator，但 locator 无法解析、内容完整性未知或 applicability 无法可靠判断 → fail closed，先修复本地入口；
- 不得因为本地入口损坏就在线读取 upstream Rule corpus 猜答案。

## 6. 当前明确不做什么

在 P4 Evidence 形成前，不把以下机制作为所有 Consumer 的默认要求：

- 五维 Rule metadata；
- 中央 Rule Registry / Catalog；
- `agentic-dev` 当前 Rule Discovery Tool；
- 每次任务固定 signals schema；
- 从 upstream 同步 Rule corpus。

后续只在简单方案经真实 Evidence 证明不足时增加复杂度。
