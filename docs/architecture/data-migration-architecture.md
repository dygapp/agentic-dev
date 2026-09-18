---
id: architecture:data-migration
type: architecture
status: active
---

# 数据迁移治理架构

## 1. 目标

本 Architecture 定义普通软件 Consumer 中 legacy / historical / business data migration 的可复用语义边界、source role、ownership、异常治理与完成不变量。

它解决的是：

> 当旧系统、历史文件、外部数据或其他既有数据来源需要进入当前系统时，哪些语义必须由 Current Authority 决定，哪些信息只是 source evidence，怎样避免静默改写 / 丢弃历史事实，以及什么证据才足以声明迁移完成。

本 Architecture 不等同于数据库 schema migration，也不规定 ETL 工具、数据库、文件格式、目录、fingerprint 算法或具体 migration application 结构。

具体 Feature / change 的工作生命周期继续由 `method:ai-development` 持有；本 Architecture 只提供 migration-specific semantic contract。

## 2. 责任链

Data Migration 的通用责任链是：

```text
Current Requirement / Domain Authority
        ↓ durable business semantics / constraints
Current Feature Specification
        ↓ migration goal / scope / observable acceptance
Legacy / Historical / External Source Evidence
        ↓ acquisition / extraction
Migration Mapping / Canonical Input（按需）
        ↓ controlled transform / import
Current Target State
        ↓ reconciliation / observable use / acceptance evidence
Migration Evidence
```

这条链中的每一层职责不同：

- Requirement / Domain Authority 持有跨 Feature 持续成立的业务对象、历史语义、retired behavior boundary、长期兼容义务与不可越界约束；
- Current Feature Specification 持有本次 migration change 的 Goal、In Scope / Out of Scope、Observable Behavior 与 Acceptance，并引用而不是复制长期 Requirement / Domain facts；
- Source Evidence 提供历史事实、原始值和 provenance，但不自动成为 Current Requirement；
- Mapping / Canonical Input 只负责受控转换、稳定重放或核验所需的 migration representation，不获得 Product / Requirement Authority；
- Target State 是当前系统可消费的数据状态，不等于旧系统的完整复制；
- Migration Evidence 证明本次迁移是否满足当前 Specification / Acceptance，不反向创造业务规则。

## 3. 当前权威拥有迁移语义

Data Migration 必须区分**长期业务语义**与**当前 change contract**。

### 3.1 Requirement / Domain 责任

Current Requirement / Domain Authority 持有会跨多个 Feature 持续成立的：

- business object / identity / lifecycle semantics；
- 必须保留的 historical semantics；
- 允许 / 禁止的 merge、normalization、repair 或 exclusion boundary（当其具有长期业务含义时）；
- retired behavior 是否允许进入 Current system；
- 其他长期 Product / Domain constraint。

### 3.2 Feature Specification 责任

当前 migration change 的 Specification 持有：

- migration goal；
- in-scope / out-of-scope source、time range 与 business range；
- 本次 change 的 observable behavior；
- 本次迁移的 Acceptance Criteria；
- 对长期 Requirement / Domain facts 的具体适用关系。

如果某个 scope、source mapping 或 acceptance fact 被证明会跨多个后续 Feature 持续成立，则应按目标 Repository Authority promote 到真正长期 owner；不能因为 migration 一次需要就默认把全部 Feature-local fact 提升成 Requirement / Domain baseline。

Migration implementation 不得仅因为：

- 旧系统存在某字段或记录；
- 新系统存在同名字段、表、Capability；
- 技术上可以转换；
- 某条历史数据“看起来应该这样解释”；

就反向发明 Current Requirement 或绕过当前 Specification。

如果 migration analysis 暴露新的长期业务决定，应回到真实 Requirement / Domain owner；如果只影响当前 change 的 Scope / Observable Behavior / Acceptance，则更新当前 Specification，而不是永久留在脚本、mapping table、Issue 或 migration report 中。

## 4. 来源角色与出处

Legacy database、历史文件、旧接口、旧代码、旧字典和外部数据可以是 migration source evidence，但它们的存在不等于当前业务事实。

至少区分：

```text
Current Requirement / Domain Authority
Current Feature Specification
Legacy / Historical Evidence
External Source Evidence
Migration Analysis / Mapping
Canonical Migration Input（optional）
Current Target State
Migration Evidence
```

Source provenance 应足以回答：

- 这条数据来自哪里；
- 哪个时间 / 版本 / source role；
- 是否经过转换、合并或排除；
- 当前异常或冲突应回到哪个输入解释。

具体 provenance schema、字段、文件格式和存储方式由 Consumer-local design 决定。

## 5. 规范化前保持语义

历史或遗留数据进入 Current system 时，默认先保护真实语义，再决定是否归一化。

未经 Current Authority 明确允许，不得静默：

- 把 historical state 改写成 Current state；
- 用 Current dictionary 覆盖无法等价解释的 legacy code；
- 把同一主体的多条合法历史记录合并成一条；
- 重新编号导致原始 identity / provenance 丢失；
- 为缺失字段补造业务事实；
- 将历史流程存在过解释成 Current system 仍应支持该流程。

能够 deterministic 且保持业务含义的格式转换、编码转换、规范化可以由 design / implementation 处理；会改变业务含义的 mapping 必须有 Current Authority 支撑。

## 6. 不静默修复，也不静默丢弃

无法解释、无法映射、无法关联、重复、冲突、无效代码、资源缺失或其他异常必须获得显式 disposition。

允许的 disposition 包括：

- **safe deterministic transform**：转换不会改变业务语义；
- **preserve source / raw value**：原值或 source representation 继续保留；
- **explicit exception / conflict record**：进入可追踪异常集合；
- **Human / Requirement decision**：需要业务事实判断时升级；
- **explicitly authorized exclusion**：当前 Authority 明确允许排除且保留理由 / 范围。

不得为了让迁移“通过”而：

- 静默丢弃记录；
- 主观修复业务含义；
- 用默认值掩盖 Material Ambiguity；
- 因关联失败直接删除可识别历史事实；
- 把未处理异常从完成证据中隐藏。

## 7. 身份与重复项语义

Data Migration 必须建立足以支持导入、核验和必要重放的 source / target identity 关系。

Consumer 可以根据风险使用：

- legacy stable id；
- natural key；
- composite business identity；
- fingerprint / checksum；
- explicit source + local id；
- 其他可证明稳定的 identity strategy。

本 Architecture 不规定统一算法。

Duplicate 也不是纯技术概念：

- 同一人员可以有多条合法历史业务记录；
- 字段相同不必然代表同一业务事实；
- 来源冲突不等于某一来源可自动丢弃；
- merge / dedupe / source priority 必须由 source semantics、Current Requirement / Specification 或明确 technical contract 支持。

## 8. 数据获取与稳定导入分离

从 Legacy / External Source 取得数据是 **acquisition responsibility**；把已经确定 source role 与 mapping 的数据写入 Current system 是 **import responsibility**。

项目需要可复现、可审计、可重复迁移或脱离旧系统运行时，可以建立 bounded canonical migration input：

```text
Legacy / External Source
→ Acquisition
→ Canonical Migration Input
→ Stable Import
→ Current Target State
```

Canonical Migration Input 是 migration artifact，不是第二套 Requirement / Domain Authority，也不是所有 Consumer 必须建立的固定文件层。

如果项目不需要独立 canonical input，也必须保持 source role、mapping 与 acceptance 可解释；不能因为直接从 source import 就把旧系统变成长期 Runtime dependency。

## 9. 重放与幂等边界

Migration 是否允许重跑、resume、partial retry 或 one-shot，必须显式决定。

### 可重放迁移

至少明确：

- stable identity；
- already-imported behavior；
- conflict behavior；
- update / overwrite / skip semantics；
- side-effect boundary；
- exception retry boundary。

### 一次性迁移

至少明确：

- 哪些副作用不可重复；
- partial failure 如何恢复；
- 如何判断哪些数据已写入；
- reconciliation 如何定位缺失 / 重复 / 半完成状态；
- rollback 或 forward-fix 责任。

不得在未声明时默认“脚本天然幂等”或“失败后重新跑一次即可”。

## 10. 对账与完成

Migration completion 不是“脚本返回 0”或“目标表已有数据”。

应根据当前风险，从以下维度选择足以支撑 claim 的证据：

- source / scope coverage；
- before / after quantity reconciliation，且按有业务意义的维度核对；
- representative semantic checks；
- source / provenance traceability；
- identity / duplicate / conflict disposition；
- unresolved exception inventory；
- resource / attachment integrity（若适用）；
- target-side query / behavior / observable use；
- retired behavior 未被意外恢复；
- Legacy Source 未成为未声明的长期 Runtime dependency。

验证粒度由风险与 Acceptance 决定，不要求所有 migration 使用相同统计报表或 reconciliation 模板。

数据库 schema / initialization 的完成证据仍由相应 Rule / Technical contract 持有；schema migration PASS 不能单独证明 business data migration complete。

## 11. 人工决策边界

Agent 可以自主处理：

- 不改变业务语义的 deterministic transform；
- 已由 Current Authority 唯一决定的 mapping；
- 可逆、局部且不改变 Acceptance 的实现 HOW。

以下情况应按 Consumer 当前 Authority 升级：

- 多个合理 mapping 会形成不同业务事实；
- merge / dedupe / source priority 会不可逆丢失信息；
- repair / exclusion 会改变 Current Requirement、当前 Specification 或 Acceptance；
- 历史事实与 Current Domain interpretation 冲突；
- 异常处置需要决定“哪一个来源才代表真实业务事实”；
- 迁移会恢复、覆盖或改变用户可观察业务行为。

跨 Feature 的长期业务决定写回 Requirement / Domain owner；只影响本次 change 的 Goal / Scope / Observable Behavior / Acceptance 写回当前 Specification；技术执行选择留在 Technical Plan / implementation；尚未解决的 source anomaly 保持 exception，不用默认实现掩盖。

## 12. 与 AI Development 的组合

Data Migration Governance 不增加新的通用 Method stage。

涉及 legacy / historical / business data migration 的具体 change 继续使用：

```text
Specification
→ Technical Planning（通常需要）
→ Slice & Ready
→ Execute
→ Converge
```

其中：

- Specification 明确本次 migration 对长期 Requirement / Domain facts 的适用范围、Observable Behavior 与 Acceptance；
- Technical Planning 应加载本 Architecture，决定 source / target、mapping、identity、replay、exception、reconciliation 与 rollout HOW；
- Execute 按 Execution Unit 和适用 Rules 实施；
- Converge 必须验证 migration Evidence 与当前 Authority / Acceptance 一致，而不是只验证脚本执行成功。

如果 migration 暴露跨多个 Feature 持续成立的长期 Architecture driver，应回写真实 Architecture owner；如果暴露长期 Requirement / Domain 事实缺口，应回到真实 Requirement owner；如果只暴露当前 change 的 Scope / Observable / Acceptance 缺口，则回到当前 Specification。

## 13. 与其他能力的边界

### Requirement Authority

`architecture:requirement-authority` 决定长期 Requirement / Domain facts 如何唯一归属和被 Fresh Context 发现；本 Architecture 不复制 Product / Domain 事实，只约束 migration 如何消费并保护这些事实。

### Human Review

`architecture:human-review` / `skill:human-review` 可以帮助人工理解高风险 mapping、exception、merge 或 exclusion decision；Review Draft 仍是非 Authority，决定必须写回真实 owner。

### Review Change

`skill:review-change` 可以对 high-impact semantic migration 执行 Authority-chain semantic review；它审查 repository change，不拥有 migration semantics。

### 数据库迁移验证

schema / initialization migration 与 legacy / historical business data migration 是不同责任。数据库 migration Rule 可以独立验证 Fresh Database / migration chain / startup，不自动覆盖本 Architecture 的 source semantics、exception 或 reconciliation。

## 14. 产物生命周期

典型 migration artifact 包括：

- source inventory；
- field / state mapping；
- canonical migration input；
- transform code / script；
- exception / conflict inventory；
- reconciliation result；
- migration report；
- verification evidence。

这些 artifact 是否长期保存取决于它是否仍承担可恢复、可审计、重放或验收责任。

原则：

- durable semantic decision 进入真实 Requirement / Domain / Architecture / Specification / Technical owner；
- canonical input 只在重放 / provenance / audit 有长期价值时保留；
- 临时 mapping scratchpad、一次性分析表和执行流水账完成使命后退出 Current consumption；
- Git / Issue / PR 保留历史，不通过第二套 Markdown Authority 复制执行过程。

## 15. 不变量

Consumer 采用本 Architecture 后，应保持以下不变量：

1. Source evidence 不自动升级为 Current Requirement 或 Feature Specification；
2. 会改变业务含义的 mapping 必须有 Current Authority；
3. Feature-local migration scope / observable acceptance 不因一次 migration 自动提升为长期 Requirement；
4. 无法解释 / 映射 / 关联的数据不得静默 repair 或 discard；
5. duplicate / merge / source priority 必须基于真实 semantics；
6. acquisition 与 stable import 可以分离，Legacy Source 不因迁移而自动成为长期 Runtime dependency；
7. replay / idempotency / one-shot boundary 必须显式；
8. Completion 必须包含与 Acceptance 匹配的 reconciliation / observable evidence；
9. historical data migration 不自动恢复 retired workflow 或把 historical state 解释成 Current state；
10. schema migration completion evidence 不替代 business data migration evidence；
11. migration artifact 不形成第二套 Product / Requirement / Specification Authority。
