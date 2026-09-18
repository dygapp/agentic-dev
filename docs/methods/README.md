---
id: guide:methods-navigation
type: guide
status: active
---

# Method 目录导航

本 README 是 Human View。通用 Method selection contract 由 `docs/architecture/method-architecture.md` 定义；`agentic-dev` 当前 `work kind → Method locator` 实例由 `docs/project/project-capability-profile.md` 持有。Agent 不依赖本目录索引进行 Method routing。

## 当前 Method 人类清单

- [`requirement-baseline-establishment.md`](requirement-baseline-establishment.md) — 当普通软件 Consumer 尚无可靠 Requirement Baseline，或现有基线碎片化、冲突、需要重建时，从 Raw Project Inputs 建立 / 重建长期 Requirement Authority，并以 `Requirement Baseline Ready` 收敛；
- [`architecture-clarification.md`](architecture-clarification.md) — 当多个当前或预期 Feature 共同依赖一个长期、高成本难逆、会阻塞可靠 Specification / Planning 的 systemic architecture driver 时，条件性澄清并更新长期 Architecture owner；
- [`ai-development.md`](ai-development.md) — 当本地 Requirement / Architecture Context 已足够稳定时，用于普通 Feature / change 的 Clarify Intent → Specification → Technical Planning? → Slice & Ready → Execute → Converge 生命周期；
- [`consumer-adoption.md`](consumer-adoption.md) — Consumer 首次显式采用 `agentic-dev` reusable capability；
- [`consumer-upgrade.md`](consumer-upgrade.md) — Existing Consumer 显式评估 / 升级 upstream capability baseline；
- [`model-collaboration-adoption.md`](model-collaboration-adoption.md) — Repository 在相关 collaboration semantics 已进入 local Authority 后，建立 / 首次启用 Model Collaboration runtime instance。

本清单只方便人理解当前 Repository 的 Method corpus，不拥有 `work kind → Method` selector；当前 selector instance 只由各 Repository 自己的 Project Capability Profile 或等价 Authority 持有。

`method:requirement-baseline-establishment`、`method:architecture-clarification` 与 `method:ai-development` 是三个不同 work kind：

```text
Raw Project Inputs
→ Requirement Baseline Establishment
→ Requirement Baseline Ready
→ Architecture Clarification?（仅存在 systemic architecture blocker 时）
→ AI Development（具体 Feature / change）
```

新项目通常需要先建立 Requirement Baseline，但 Architecture Clarification 不是所有项目的必经步骤；已有稳定 Requirement / Architecture Context 的普通 Feature 也不重复执行项目建立流程。

这些 reusable Method 存在于本仓库 corpus，**不等于** `agentic-dev` 自身已经把它们注册到 local selector；Consumer adoption / upgrade 后应由 Consumer 自己判断 work kind、adopt / adapt / reject，并建立 local mapping。

当前不再保留负责串联 Requirement 与 Architecture 的项目澄清 super-method。长期语义由真实 owner 分别承担：Requirement Baseline、Architecture Clarification、AI Development 各自拥有自己的阶段 / Gate / return contract；能力边界在 Architecture，执行能力在 Skill，条件性约束在 Rule。

Method 是可扩展的一等 capability 类型。未来只有真实 Evidence 证明存在稳定的复杂工作生命周期时才增加新 Method；Method 不只用于普通产品开发，也可以描述 requirement baseline establishment、architecture clarification、adoption / upgrade、capability establishment 等具有独立 work kind、阶段转换、Gate 与完成语义的复杂过程。