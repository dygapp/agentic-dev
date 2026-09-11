# V3-07 — agentic-dev 自采用与发现机制切换

**跟踪：** Issue #113  
**启动基线：** `master@5ae0e144d30c6010fadf8e3beff3c12ce4b7a147`

## 目标

把已经集成的使用方生命周期、资源模型与资源发现架构投射到 `agentic-dev` 自身真实仓库状态，形成一个可持续维护的本地发现机制，并在验证通过后原子取代现行 v2 手工 discovery surface。

## 当前事实

当前仓库没有实际版本化的 Activation Manifest / Runtime Catalog 文件。普通 Fresh Context 的现行 discovery surface 主要由：

- `AGENTS.md`；
- `README.md` / `docs/project/project-roadmap.md`；
- `docs/guides/rule-activation-guide.md` 的手工职责 / 风险导航；
- `docs/guides/consumer-local-rule-activation.md` 的普通运行说明；
- `skills/README.md` 与各 `SKILL.md`；
- 工程纪律、技术画像、验证规则、外部操作规则等真实 owner；
- 若干 v2 project contracts 的兼容语义；

共同承担。

因此 V3-07 不创建空 Manifest / Catalog 来模拟历史设计。

## 当前裁决

### 1. Reviewed Discovery Map：需要

当前仓库已经长期维护职责 / 风险 → 来源的手工跨资源映射，同时存在：

- 9 个 Skill；
- 3 个跨技术栈工程纪律；
- 技术画像 inventory；
- 跨职责验证规则；
- 外部操作规则；
- 使用方生命周期、仓库本地治理与项目权威。

这证明跨资源语义正规化具有持续价值。继续把该映射留在 Guide 中会形成派生导航与长期 owner 重叠，因此建立一个小型、已复核、非规范性的 Reviewed Discovery Map。

### 2. Runtime View / Catalog：当前不需要

当前仓库规模和运行证据不足以证明需要第二个 compact 运行投影。直接读取小型 Reviewed Discovery Map 的成本可接受，因此：

- 不建立 Runtime Catalog；
- 不建立 generator；
- 不建立第二 current discovery mechanism。

后续只有出现可测量的上下文 / 运行成本问题时再评估。

## Candidate 产物

- `docs/discovery/README.md`：薄 Local Discovery Entry；
- `docs/discovery/reviewed-discovery-map.md`：当前 Reviewed Discovery Map；
- `docs/project/rule-governance-v3-v3-07-self-adoption.md`：自采用、验证、迁移与切换证据。

## 执行顺序

1. 恢复并记录当前 self-runtime surface；
2. 建立 candidate Local Discovery Entry；
3. 建立 candidate Reviewed Discovery Map 与 coverage anchors；
4. 在旧 v2 入口仍 current 的前提下完成 candidate 验证；
5. 裁决验证发现并修复；
6. 完成高影响 AI 复核；
7. 在同一拟集成变更中原子切换：
   - 新 Local Discovery Entry / Map 成为 current；
   - `rule-activation-guide.md` 降为人类说明 / compatibility pointer，不再维护手工路由表；
   - `consumer-local-rule-activation.md` 中被 V3-06 supersede 的普通运行规范正文降为说明 / 指针；
   - v2 metadata / routing project contracts 明确历史 / 兼容身份；
   - Bootstrap / README / Roadmap 指向新 current entry；
8. 再次验证切换后的 Fresh Context 与 current mechanism 唯一性；
9. 集成后关闭 Issue #113，V3-08 只成为下一 Planning Candidate。

## Candidate 验证场景

至少覆盖：

1. Fresh Context 恢复当前 Repository Authority / Current Work；
2. routing-only：只判断下一职责时不加载完整 Skill；
3. 核心职责执行：只加载一个主 Skill；
4. GitHub Actions 条件：平台 Skill 作为按需能力；
5. 工程纪律条件：命中必要 Discipline 但不夺取主职责；
6. Vue 3 + TypeScript 条件：按需发现技术画像；
7. completion / migration / visual / evidence-reuse 条件：发现对应验证规则；
8. 外部写操作 / 异步 / 共享资源条件：发现外部操作规则；
9. Stage Return：丢弃旧 discovery decision 后重新发现；
10. stale source / missing selector / coverage drift / ambiguity：失败关闭到本地当前权威；
11. no-match 但仍有治理事实：不能解释为“无规则”；
12. ordinary runtime 不读取 upstream 或历史聊天。

## 完成条件

- candidate 验证覆盖上述场景且不存在未解决阻塞 / 中等级问题；
- Reviewed Discovery Map 的 coverage / source binding / 维护生命周期明确；
- Runtime View 不建立的理由有当前证据支持；
- replacement 在单一拟集成变更中完成，不产生两个 current discovery mechanism；
- Post-cutover Fresh Context / routing / Skill loading / Stage Return / fail-closed 再验证通过；
- 未修改任何 Consumer Repository；
- 未提前进入 V3-08。