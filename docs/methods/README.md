---
id: guide:methods-navigation
type: guide
status: active
---

# Methods 目录导航

本 README 是 Human View。通用 Method selection contract 由 `docs/architecture/method-architecture.md` 定义；`agentic-dev` 当前 `work kind → Method locator` 实例由 `docs/project/project-capability-profile.md` 持有。Agent 不依赖本目录索引进行 Method routing。

## 当前 Method Human Inventory

- [`ai-development.md`](ai-development.md) — 当本地 Requirement / Architecture Context 已足够稳定时，用于普通 Feature / change 的 Clarify Intent → Specification → Technical Planning? → Slice & Ready → Execute → Converge 生命周期；
- [`software-project-clarification.md`](software-project-clarification.md) — 当普通软件 Consumer 中多个 Feature 共同依赖的长期 Requirement / Architecture Context 缺失、冲突或需要重建时，用于项目级或重大范围的前置澄清；
- [`consumer-adoption.md`](consumer-adoption.md) — Consumer 首次显式采用 `agentic-dev` reusable capability；
- [`consumer-upgrade.md`](consumer-upgrade.md) — Existing Consumer 显式评估并升级 upstream capability baseline；
- [`model-collaboration-adoption.md`](model-collaboration-adoption.md) — Repository 在相关 collaboration semantics 已进入 local Authority 后，建立并首次启用 Model Collaboration runtime instance。

本清单只方便人理解当前 Repository 的 Method corpus，不拥有 `work kind → Method` selector；当前 selector instance 只由各 Repository 自己的 Project Capability Profile 或等价 Authority 持有。

特别地，`software-project-clarification` 是面向普通软件 Consumer 的 reusable Method。它存在于本仓库 Method corpus，**不等于** `agentic-dev` 自身已经把该 Method 注册到 local selector；Consumer adoption / upgrade 后应由 Consumer 自己判断是否采用并建立 local mapping。

当前不再保留独立 `principles.md` 复合文档。原有长期语义由真实 owner 分别承担：AI Development 的阶段 / Gate / phase identity / artifact lifecycle 在 `ai-development.md`，能力边界在 Architecture，执行能力在 Skill，条件性约束在 Rule。

Method 是可扩展的一等 capability 类型。未来只有真实 Evidence 证明存在稳定的复杂工作生命周期时才增加新 Method；Method 不只用于普通产品开发，也可以描述 project clarification、adoption / upgrade、capability establishment 等具有独立 work kind、阶段转换、Gate 与完成语义的复杂过程。