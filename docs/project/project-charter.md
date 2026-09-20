---
id: project:charter
type: project
status: active
distribution: source-only
---

# 项目章程

## 1. 项目使命

`agentic-dev` 的使命是形成一套**可由 AI Agent 实际执行、可由真实软件项目选择性采用、并能在 Consumer-local 环境持续演进**的软件开发能力体系。

当前核心开发责任覆盖从需求分析、条件性架构澄清，到具体 Feature / change 的 Specification、Technical Planning、工作切分、代码实现、验证与收敛，并在 `Ready to Integrate` 边界结束。merge、release、deployment、production operations、incident response 与 service retirement 默认由 Consumer-local Authority 和实际技术架构承担；只有未来真实跨 Consumer Evidence 证明存在稳定 reusable capability 时，才单独评估 admission。

项目不追求把所有开发知识集中进一个超大 Prompt、超级 Skill 或中央运行控制器，而是把长期语义放到正确 owner，并通过可恢复的 Repository Authority、Method、Skill、Rule、Architecture 与渐进式发现机制支撑 Fresh Context 工作。

## 2. 要解决的核心问题

AI Agent 驱动开发长期面临几个相互关联的问题：

- 新上下文不能依赖旧聊天、个人记忆或隐藏推理恢复项目事实；
- 规则与工程知识增多后，全量加载会造成上下文膨胀和无关约束干扰；
- 稳定执行 Procedure、条件性 policy、复杂工作生命周期和长期结构容易混成重复 Authority；
- 上游方法仓库如果持续参与 Consumer ordinary runtime，会破坏 Consumer 自身 Authority 与长期可维护性；
- 人类需要完整可理解的说明，而 Agent 又需要更薄、更确定的运行入口；
- 演进结论如果只存在于会话或阶段文档中，会导致“讨论很多、current owner 很少”。

`agentic-dev` 通过 capability ownership、Consumer-local adoption、渐进式披露、Evidence-driven evolution 等机制解决这些问题。

## 3. 目标使用方

主要使用方包括：

- 使用 AI Agent 进行需求、设计、开发、验证和仓库维护的软件项目；
- 希望把稳定开发方法、执行能力和工程规则固化进 Repository Authority 的团队；
- 已存在并持续演进、需要显式 baseline adoption / upgrade 而不是日常依赖上游的 Consumer Repository。

项目自身也是其能力的 self-consumer，用于验证 Fresh Context、Rule Discovery、Skill / Rule / Method 边界和 Repository governance。

## 4. 核心目标

### G1 — 可从 Repository 恢复的开发

项目事实、长期方法和执行约束必须能够从当前 Repository / GitHub Authority 恢复，而不是依赖此前会话。

### G2 — 具备本地归属的可复用能力

可复用 Method / Architecture / Skill / Rule 可以被 Consumer adopt / adapt，但 adoption 完成后必须拥有 Consumer-local canonical owner。

### G3 — 有界的 Agent 上下文

普通运行只加载当前责任需要的最小 Authority、Method、Skill、Rule 和代码 / Evidence；规则总量增长不能要求模型线性读取全量规则元数据或正文。

### G4 — 清晰的语义归属

复杂过程、结构边界、执行 Procedure、条件性 policy、人类解释、项目自身状态分别由适合的 owner 持有，不通过兼容或目录习惯维持重复 Authority。

### G5 — 人与 Agent 均可用

Agent 与人类可以通过不同入口使用同一套 canonical knowledge；Human View 可以完整解释，但不得成为第二套 runtime Authority。

### G6 — 证据驱动演进

新 Method、Skill、Rule 或更复杂发现机制必须由真实项目 / Consumer Evidence 证明长期价值，而不是为了理论完整性预建。

## 5. 核心项目需求

以下是 `agentic-dev` 自身必须长期满足的项目级结果要求；具体实现由 Architecture / Method / Skill / Rule 持有。

1. **Repository Authority**：GitHub Repository 是长期项目事实来源；Fresh Context 可以从当前仓库恢复必要事实。
2. **Consumer ownership**：Consumer 项目事实、产品 Authority、集成权限与 local adaptation 始终由 Consumer 自身拥有。
3. **Local ordinary runtime**：完成 adoption / upgrade 后，Consumer ordinary runtime 不依赖在线读取 `agentic-dev` current state。
4. **Progressive disclosure**：普通 Agent 不默认加载完整 Rule / Skill / Research / Project history。
5. **Fail-closed discovery**：发现输入、metadata、扫描完整性或 Authority 不可靠时，不通过猜测、旧缓存或全量加载制造“成功”。
6. **Single semantic ownership**：同一规范语义只存在一个 canonical owner；允许多视窗解释，不允许多 Authority。
7. **Local specialization**：不同 Consumer 可以保留自己的规则、术语、审批、技术默认值和仓库 policy。
8. **Explicit irreversible authority**：merge、release、deploy、生产变更和破坏性远程操作服从目标仓库 / 人工 Authority，不因 Skill 或工具能力自动获得授权。
9. **Current Evidence**：完成声明、验证与高影响复核必须由与当前 claim / current head 匹配的 Evidence 支持。
10. **Minimal durable project knowledge**：长期 Project 文档只保存无法由现有 capability owner 或 GitHub native state合理承担的项目知识，不恢复阶段文档膨胀。

## 6. 非目标

`agentic-dev` 不以以下目标为默认方向：

- 成为产品需求、领域模型或业务事实的中央仓库；
- 成为 Vue、TypeScript、Spring、组件库、数据库产品或其他具体技术栈的通用知识库；技术事实优先由当前 Consumer 的 code / dependency / configuration、版本匹配资料和工具验证承担，稳定项目选择由 Consumer-local Authority 持有；
- 为了形式上的“全生命周期”预建 release、deployment、production operations、incident response 或 service retirement Method / Skill；
- 让 Consumer 日常联网读取 upstream 最新状态；
- 建立需要人工同步的中央 Rule Map / Runtime Catalog；
- 用一个 Super Skill / Runtime Controller 接管完整开发生命周期；
- 为所有项目强制同一目录、同一 policy、同一技术栈或同一审批流程；
- 为未来可能需求预建向量数据库、图数据库、MCP Rule Server 或大型 Rule Engine；
- 用大量 Project 阶段文档替代 Issue / PR / Git / Actions 的原生追溯能力。

## 7. 成功判据

项目长期成功应能由真实使用证明：

- Fresh Context 可以在有限输入下恢复正确当前责任；
- Consumer 能选择性采用能力并长期保持 local Authority；
- Rule / Skill / Method 数量增长时普通上下文仍保持有界；
- 项目演进不会持续产生重复 owner 或人工同步索引；
- Human View 足够完整可理解，Agent View 足够薄且可执行；
- Consumer 反馈能够回流为 Evidence，但不会自动污染 upstream canonical semantics；
- 当前工作树表达最终有效模型，实施过程由 GitHub 历史可追溯。

## 8. 与 Capability Architecture 的关系

本 Charter 只拥有 `agentic-dev` 自身的使命、目标、非目标和项目级结果要求。

具体“如何满足这些要求”由 `docs/architecture/**`、`docs/methods/**`、`skills/**`、`docs/rules/**` 和工具实现分别持有；本文件不得复制其详细 contract。