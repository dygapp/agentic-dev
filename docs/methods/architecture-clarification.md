---
id: method:architecture-clarification
type: method
status: active
---

# 架构澄清方法

## 1. 目标

本方法处理普通软件 Consumer 中那些**跨多个当前或预期 Feature 持续成立、长期、高返工成本或高成本难逆，并且不解决就会阻塞可靠 Specification / Technical Planning 的 architecture driver**。

它不是 Big Design Up Front，也不负责完成整个系统的技术设计。它只把必须提前解决的长期结构问题收敛到真实 Architecture owner，使后续 Feature 可以在稳定的 Architecture Context 上继续。

本 Method 不创造 Product Requirement。若架构分析暴露出业务多解、Requirement conflict、未定义 Product Boundary 或长期业务事实缺失，应返回真实 Requirement owner；如果问题是系统性 Requirement Baseline gap，则由 Repository-local Method selector 决定是否进入 `method:requirement-baseline-establishment`。

## 2. 进入条件

只有存在一个或多个 systemic architecture driver 时才进入。本 Method 的典型触发包括：

- 多个 Feature / Execution Unit 共同依赖的 shared capability / shared contract；
- core data / system structural boundary；
- security / integration / deployment topology；
- 高成本难逆的 structural decision；
- 已出现多个局部实现，显示 shared capability extraction 信号；
- 一个成熟 reference implementation 可以显著降低系统性探索成本；
- 当前 Requirement Baseline 已足够明确，但缺少长期 Architecture Context 导致多个 Feature 无法可靠 Specification / Planning。

以下内容不进入本 Method：

- 单 Feature 的普通实现选择；
- 低影响、易逆局部设计；
- 精确类 / 函数 / 文件组织；
- 当前 Execution Unit 的施工顺序；
- 普通 framework usage detail；
- 仅因为项目较大、技术复杂或文档较多而提前进行全量架构设计。

## 3. 与其他 Method 的关系

```text
Requirement Baseline Ready
        ↓
architecture blocker?
   ├─ no → AI Development
   └─ yes
        ↓
Architecture Clarification
        ↓
Architecture Context Ready
        ↓
AI Development
```

本 Method 是条件性 work kind，不是所有新项目的必经步骤。简单项目、成熟技术栈或已经存在足够 Architecture Context 的项目，可以在 `Requirement Baseline Ready` 后直接进入具体 Feature 的 `method:ai-development`。

Feature Technical Planning 与本 Method 共享同一个长期 Architecture owner：

- Feature-specific、局部、可逆 HOW 留在 Technical Planning；
- 跨多个 Feature、长期持续、必须提前解决的 structural driver 才提升到 Architecture Clarification；
- Feature Planning 中确认具有长期价值的 architecture fact，应更新同一长期 Architecture owner，而不是建立平行 Authority。

## 4. 生命周期

```text
Establish Architecture Drivers
→ Clarify Architecture
→ Architecture Convergence
→ Architecture Context Ready
```

正式阶段三个：

1. Establish Architecture Drivers；
2. Clarify Architecture；
3. Architecture Convergence。

### 4.1 Stable phase identities

- Establish Architecture Drivers → `establish-architecture-drivers`；
- Clarify Architecture → `clarify-architecture`；
- Architecture Convergence → `architecture-convergence`。

这些 token 只属于 `method:architecture-clarification`。

## 5. Establish Architecture Drivers

先证明当前问题真的属于项目级 Architecture responsibility，而不是 Requirement ambiguity 或 Feature-local HOW。

每个候选 driver 至少检查：

- 影响范围：是否跨多个当前或预期 Feature；
- 生命周期：是否会形成长期结构事实；
- 可逆性：错误选择的返工成本是否显著；
- 阻塞性：是否会阻止可靠 Specification / Technical Planning；
- ownership：最终应进入哪个现有或待建立 Architecture owner；
- Requirement boundary：是否仍包含尚未解决的 Product / Domain ambiguity。

不能满足这些条件的内容应返回正确责任层，而不是为了“架构完整”继续扩张。

退出条件：保留下来的 driver 都具有明确的项目级 Architecture 理由，且没有把未解决 Product Requirement 伪装成 Architecture decision。

## 6. Clarify Architecture

根据当前 Requirement Baseline、Repository facts、已有 Architecture Context、成熟 reference / engineering evidence，对保留的 driver 形成最小充分长期结构决定。

可能形成或更新：

- Architecture Context / constraints；
- architectural capability boundary；
- shared contract / shared abstraction boundary；
- core data / system structural boundary；
- security / integration / deployment topology；
- current durable Architecture State；
- ADR（仅当背景、主要替代关系与权衡具有长期历史价值时）。

### 6.1 Seed Architecture

项目早期可以基于已知系统类别、Requirement Baseline、明确 NFR、成熟工程经验和 reference implementation 形成最小 Seed Architecture。

目标是提前解决高杠杆结构问题，而不是一次性预测全部未来设计。

### 6.2 Evolutionary Architecture

实施过程中出现以下 Evidence 时，可以重新进入本 Method 或其中相应责任：

```text
local implementation evidence
→ repeated structural pain / shared pattern
→ architecture candidate
→ architecture clarification
→ promote to Architecture Authority
```

原则：

> Seed deliberately, evolve empirically.

### 6.3 Requirement 回流

如果 Architecture Clarification 发现：

- 多个合理业务解释；
- Requirement conflict；
- product / system responsibility boundary 未定义；
- data semantics 本质上仍是业务事实；
- acceptance intent 不明确；

则停止在 Architecture 层自行选择，返回真实 Requirement owner。Architecture 不通过“技术上更合理”来创造 Product Requirement。

退出条件：阻塞性的长期 architecture driver 已进入真实 Architecture owner；普通 Feature-specific HOW 没有被提前吸收。

## 7. Architecture Convergence

只有同时满足以下条件，才可以声明 `Architecture Context Ready`：

1. 当前阻塞多个 Feature 的 architecture driver 已被处理；
2. 每个长期 Architecture fact 有明确 owner；
3. Requirement / Architecture 边界清楚，没有用 Architecture decision 隐式替代 Product decision；
4. 普通、局部、易逆的 Feature HOW 未被过度提升；
5. shared capability / contract / topology 等长期结构关系足以被后续 Fresh Context Feature Agent 定位；
6. ADR 只记录真正需要历史理由的 decision，不把 ADR 变成全部 Architecture 文档；
7. remaining architecture item 已明确为 non-blocking 或属于后续 evolutionary evidence；
8. 高影响变更需要的独立 review 已完成。

真正存在 blocker 时保持 NOT READY。

## 8. Return contract

完成后只声明：

```text
Architecture Context Ready
```

它不等于：

```text
all architecture designed
Specification created
Technical Plan created
Execution Unit created
Execute / Integrate authority granted
```

后续具体 Feature / change 仍必须重新按 Consumer-local selector 进入 `method:ai-development` 或其他适用 Method。

## 9. Artifact lifecycle

默认 durable：

- Architecture Context / constraints；
- shared capability / contract boundary；
- current durable Architecture State；
- 条件性的 ADR。

默认 transitional / disposable：

- candidate matrix；
- option comparison；
- exploratory diagram；
- spike / benchmark result 的解释性草稿；
- review scratchpad。

只要某个派生表达可以从长期 Architecture Authority 唯一再生，就不应为了 AI 理解方便再建立平行长期模型。

## 10. Skill / Rule 边界

本 Method 当前不要求新的 `architecture-framing` Skill。只有未来真实 Consumer Evidence 证明某个 procedure 在多个 Repository 中稳定、可独立调用并能减少重复错误时，才评估 Skill admission。

同样不因为 Method 独立出来就批量新增 Architecture Rules。现有高影响 review、Authority lifecycle、verification 等横切 policy 继续按 Rule Discovery 条件性适用。

## 11. Evidence maturity

Architecture Clarification 当前 Evidence maturity 低于 Requirement Baseline Establishment。v1 只固化已经有稳定理由的 bounded、conditional、anti-BDUF contract。

后续应继续从真实 Consumer 的三类 Evidence 校正：

- 提前澄清成功避免返工的 positive case；
- 缺失长期 Architecture Context 导致局部重复决策 / 返工的 negative case；
- 只能从真实实施演进中发现的 Evolutionary Architecture case。

不得为了补足证据数量而构造大而全的 upfront architecture lifecycle。