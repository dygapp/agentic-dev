---
id: guide:consumer-local-constraints
type: guide
status: active
distribution: source-only
---

# Consumer-local Constraints

普通软件项目在开发过程中会沉淀自己的技术规则、数据迁移约束、安全政策、验证要求、外部操作边界和模块级约定。

这些内容属于 Consumer，不属于 `agentic-dev` 通用 Skills。

P4 已验证第一版最小约定：

```text
repository-wide stable policy
→ root AGENTS.md

path / module scoped policy
→ nested AGENTS.md / host-native scoped instructions

activity / semantic scoped policy
→ Consumer-local policy docs + thin locator

only if real evidence proves these insufficient
→ consider minimal metadata / filter
```

当前没有 Evidence 要求普通 Consumer 复制 `agentic-dev` 的五维 Rule Discovery、Rule metadata schema 或 discovery tool。

## 1. 为什么不能全部写进根 AGENTS.md

如果所有约束都进入根 `AGENTS.md`：

- Bootstrap 会持续膨胀；
- 与当前任务无关的规则长期占用上下文；
- path / module / activity scoped policy 很难维护；
- 一个局部规则变化会影响所有任务的启动输入。

因此根 `AGENTS.md` 只保存：

- 极少量真正 repository-wide、稳定、几乎每次都必须知道的 policy；
- 指向其他 Consumer-local constraints 的稳定 locator；
- fail-closed / no-match 的最小恢复语义。

不要把完整 policy corpus、Skill procedure 或项目当前工作流水账塞进去。

## 2. Repository-wide stable policy

适合根 `AGENTS.md` 的例子：

- Repository Authority 原则；
- 明确的安全红线；
- 全仓统一的 merge / release / deploy 授权边界；
- Consumer-local constraint locator；
- “工具可用不等于已授权”这类全仓稳定政策。

判断标准：

> 如果一条 policy 几乎所有任务都必须知道，而且长期稳定，才值得占用根 Bootstrap。

P4 disposable fixture 已验证 Codex 能直接从 root `AGENTS.md` 应用这类 policy，不需要额外 discovery tool。

## 3. Path / module scoped policy

只对某个目录、模块或技术区域生效时，优先使用自然路径作用域：

- nested `AGENTS.md`；
- 或目标宿主提供的原生 scoped instructions。

例如：

```text
frontend/
  AGENTS.md
  TicketList.vue
```

`frontend/AGENTS.md` 可以保存：

- Vue / TypeScript authoring style；
- 模块内测试要求；
- 该目录专属的依赖 / 样式 / 代码组织约定。

P4 fixture 已验证 Codex 在 `frontend/**` 任务中能够同时恢复 root policy 与 nested policy，不需要中央 Rule Registry / Rule Discovery。

如果某个平台不支持 nested instruction 自动加载，也可以让 root `AGENTS.md` 声明：

> 对目标路径，读取最近的 Consumer-local scoped policy。

重点是**路径天然决定 applicability**，不需要额外 metadata 匹配。

## 4. Activity / semantic scoped policy

有些约束不与文件路径一一对应，例如：

- 外部写操作；
- GitHub / remote API write；
- 业务数据迁移；
- 历史数据导入；
- 生产环境验证；
- 特定高风险活动。

这类约束使用：

```text
thin locator
→ current responsibility
→ one matching Consumer-local policy
```

一种简单形态：

```text
docs/constraints/
  README.md
  external-operation.md
  business-data-migration.md
```

其中 `README.md` 只做薄 locator，例如：

```text
外部写 / GitHub 写 / shared remote state
→ external-operation.md

业务数据迁移 / 历史数据导入 / 批量数据修复
→ business-data-migration.md

其他任务
→ no additional activity-specific policy
```

这个 locator 不应变成第二个规则引擎：

- 不需要五维 signals；
- 不需要给每条 policy 维护复杂 metadata；
- 不需要中央 Registry / Catalog；
- 不需要模型先看到完整 policy corpus；
- 不需要从 upstream 同步 Rule tree。

P4 已验证 Codex 可以只读取 locator + 当前匹配 policy，而不读取无关 policy。

## 5. Progressive Disclosure

普通任务的约束恢复顺序是：

```text
root AGENTS.md
→ path-scoped instructions（如果目标路径有）
→ activity locator（只有责任需要时）
→ one matching local policy
```

不应该是：

```text
root AGENTS.md
→ enumerate all policies
→ load all metadata
→ load all rule bodies
```

P4 external-write fixture 实际只读取：

- root `AGENTS.md`
- activity locator
- `external-operation.md`

没有读取不相关的 business-data-migration policy。

## 6. No-match 与 fail-closed

必须区分两个状态。

### Verified no-match

locator 明确覆盖当前责任空间，并可靠判断：

> 当前任务没有额外 activity / semantic scoped policy。

此时：

**正常继续。**

例如普通 README 拼写修订既不属于外部写，也不属于业务数据迁移，locator 可以明确返回 no-match。

### Broken / uncertain applicability

Repository 已声明存在 constraint locator，但：

- locator 缺失；
- locator 无法解析；
- locator 指向不存在的 policy；
- applicability 无法可靠判断；
- 内容完整性未知。

此时：

**fail closed。**

不得：

- 根据文件名猜哪个 policy 大概适用；
- 全量枚举 policy corpus 兜底；
- 在线读取 upstream Rule corpus；
- 使用模型记忆补出本地项目政策。

最小恢复条件是修复 Consumer-local locator / policy，使 applicability 再次可以可靠判断。

P4 broken-locator fixture 已验证该行为。

## 7. Skill 与 Consumer-local constraint 的边界

通用 Skill 回答：

> “这类软件开发工作通常怎样安全完成？”

Consumer-local constraint 回答：

> “在这个具体项目里，做这件事还必须遵守什么？”

例如：

- `execute-unit` 可以要求遵守当前 Consumer-local constraints；
- `external-operation` 可以提供通用安全写模式；
- Consumer 自己决定 Vue lint、KingbaseES migration、生产部署审批、内部网络、安全扫描等项目政策。

不要把 Consumer policy 复制进 upstream Skill。

也不要为了通用 Skill 复用而让普通运行时在线读取 Provider `docs/rules/**`。

## 8. Ownership 与升级

Consumer-local constraint 必须：

- 正文由 Consumer Repository 自己拥有；
- locator 由 Consumer 自己拥有；
- `agentic-dev` Skill install / update 不自动覆盖；
- ordinary runtime 不需要在线访问 upstream；
- 不把本地 Product / Requirement fact 塞进通用 Skill；
- 不因为 policy 数量增加就默认全量加载。

P4 fixture 在安装全部 15 个 canonical Skills 前后，对 5 个 Consumer-local constraint 文件做 hash 对比：

**全部保持不变。**

因此 Skills install 与 Consumer-local constraints ownership 可以自然解耦。

## 9. Codex local 与 ChatGPT + WebCodex

### Codex local

P4 已验证：

- root `AGENTS.md`：repository-wide stable policy；
- nested `frontend/AGENTS.md`：path-scoped policy；
- thin locator + local policy：activity / semantic scoped policy；
- verified no-match：正常继续；
- broken locator：fail closed。

### ChatGPT + WebCodex

同一个 disposable Consumer fixture 被注册为独立 WebCodex Project 后：

- WebCodex 自动恢复 root `AGENTS.md`；
- frontend 任务只需 root `AGENTS.md` + `frontend/AGENTS.md`；
- external-write 任务只需 root `AGENTS.md` + locator + `external-operation.md`；
- 不读取 Provider docs；
- 不需要中央 Rule Discovery。

因此两种执行面可以共享同一个 Consumer-owned 约束模型，只是 instruction 自动加载能力不同。

## 10. 什么时候才增加 metadata / filter

当前 v1 不引入 metadata/filter。

只有未来真实 Consumer Evidence 同时证明：

1. root + nested scope + thin locator 无法可靠表达真实 activity / semantic applicability；
2. 问题不是 fixture 设计错误；
3. 问题不是宿主原生 scoped instructions 用法错误；
4. 简单 locator 已经出现不可接受的 context / maintenance / correctness 问题；

才允许评估**最小** metadata / filter。

即使触发，也不得直接复制：

- 当前五维 Rule metadata；
- 当前 Rule Discovery Tool；
- 中央 Rule Registry / Catalog；
- 固定 task-signals schema。

复杂度必须由真实 Consumer 规模和失败证据证明。

## 11. 当前明确不做什么

P4 v1 不要求普通 Consumer：

- 建立 `.agents/rules/**`；
- 安装 Provider Rule corpus；
- 安装 Provider Rule Discovery Tool；
- 维护 Project Capability Profile；
- 维护五维 task signals；
- 运行中央 policy registry；
- 每个任务扫描全部 policy；
- 在本地入口损坏时访问 upstream 猜规则。

## 12. v1 总结

第一版 Consumer-local constraints 约定是：

```text
root AGENTS.md
  = 极少量全仓稳定 policy + locator

nested AGENTS.md / host-native scoped instructions
  = path / module scoped policy

Consumer-local policy docs + thin locator
  = activity / semantic scoped policy

verified no-match
  = continue

broken / uncertain locator
  = fail closed

agentic-dev Skills
  = 通用执行能力，不拥有 Consumer policy
```

当前 P4 Evidence 没有发现需要进入真实 Consumer applicability challenge 的简单机制缺口，因此没有触发真实 Consumer 只读检查，也没有进入 metadata/filter 设计。
