---
id: project:roadmap
type: project
status: active
---

# 项目路线图

## 当前基线

`agentic-dev` 当前 baseline 聚焦 **AI Agent 从需求 / 架构澄清到代码、验证、收敛与 Ready to Integrate** 的可复用软件开发能力。

当前稳定基础包括：

- Requirement Baseline Establishment、条件式 Architecture Clarification 与 `method:ai-development`；
- V4 Rule Discovery、Capability Model v2、Project / Capability knowledge boundary 与 Consumer-local adoption / upgrade；
- Review Governance、Human Review、Project Terminology 与 Data Migration governance；
- GitHub / Chat runtime 的 Repository Authority、Rule Discovery、execution transport、deterministic verification 与 human-escalation closure；
- upstream 不维护具体语言 / framework 技术知识 Rule family；technology specialization 由 Consumer-local Authority 持有；
- Issue #164 已完成 R1～R4：核心边界、评估入口、Rule Discovery / Evidence contract、Bootstrap 成本与真实 Consumer applicability 均已完成收敛和独立验证。

稳定演进里程碑与历史原因由 `docs/project/project-evolution.md` 持有；精确 branch / Issue / PR / Actions / commit 状态始终从 GitHub 当前事实读取。

## 当前演进

Issue #164 — **核心边界收敛与验证可信度整改** 已完成 R1～R4 并进入稳定 baseline：

- R1 — Core Boundary Cleanup；
- R2A — Current-State & Eval Entry Reliability；
- R2B — Discovery / Evidence Contract Reliability；
- R3 — Bootstrap Cost Reduction；
- R4 — Independent & Consumer Applicability Validation。

本轮最终确认 AI Development 核心边界止于 `Ready to Integrate`，upstream 不维护具体技术知识 Rule family；验证入口、Rule Discovery / Evidence contract 与 exact-subject CI 已收敛；ordinary Agent 固定 Bootstrap 已减为 `AGENTS + Roadmap + Project Capability Profile` 后按 selector 读取 selected Method；真实 Consumer `dygapp/jilinjobs-cms` read-only applicability 结果为兼容，当前 upgrade 为 optional，且本轮未执行 Consumer mutation。

稳定演进原因与历史摘要见 Project Evolution；精确 PR / Review / Actions / commit Evidence 继续由 GitHub 历史持有。

## 当前门禁

**当前没有活动中的有界演进。**

新的演进只在 `Next Candidates` 中某个候选获得新的真实 Evidence 与明确 Planning / Execute Authority 后启动。

## 后续候选

Issue #164 之外的后续演进只由新的真实 Evidence 重新激活。当前候选主题压缩为：

- Review Governance / Human Review 的跨 Consumer 持续有效性；
- GitHub / execution transport / human escalation 的新平台证据；
- Requirement Baseline / Architecture Clarification 的更多真实 Consumer validation；
- C6 verification invariant 与 deterministic current-owner tooling 的跨案例 Evidence；
- Consumer feedback（包括 Issue #58）与未来 Method selection scaling。

这些候选不因出现在 Roadmap 中自动获得 Planning / Execute Authority，也不得为了“能力完整”预建新 Method、Skill、technology Rule family、中央 registry 或 post-integration operations lifecycle。

## 已知约束

- Architecture Clarification 的 Evidence maturity 仍低于 Requirement Baseline Establishment，应保持 conditional / anti-BDUF；
- C6 verification invariant 继续暂缓，直到出现足够跨案例 Evidence；
- reusable capability 存在不等于本 Repository 或 Consumer 已采用，local selector / runtime instance 仍决定实际启用状态；
- Project Capability Profile 必须保持 Repository-local、薄且稳定，不演变成 Rule / Skill inventory 或 runtime catalog；
- Human Guide、Research、Project Evolution 不进入 ordinary Agent 固定 Bootstrap；只有当前责任明确需要时才加载。

## 状态归属

- Repository live state：GitHub；
- 项目使命 / 核心要求：`project-charter.md`；
- Repository-local capability instance：`project-capability-profile.md`；
- 当前 evolution / gate / compact next candidates：本 Roadmap；
- 稳定历史里程碑：`project-evolution.md`；
- bounded unit 的完整 Gate / Review / Actions / commit Evidence：对应 GitHub Issue / PR / Actions。

Roadmap 不复制完整 Architecture、Capability body、历史实施日志或完整 Review Evidence。
