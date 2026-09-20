---
id: project:roadmap
type: project
status: active
distribution: source-only
---

# 项目路线图

## 当前基线

`agentic-dev` 当前稳定 baseline 聚焦 **AI Agent 从需求 / 架构澄清到代码、验证、收敛与 Ready to Integrate** 的可复用软件开发能力。

当前稳定基础包括：

- Requirement Baseline Establishment、条件式 Architecture Clarification 与 `method:ai-development`；
- V4 Rule Discovery、Capability Model v2、Project / Capability knowledge boundary 与 Consumer-local adoption / upgrade；
- Review Governance、Human Review、Project Terminology 与 Data Migration governance；
- GitHub / Chat runtime 的 Repository Authority、Rule Discovery、execution transport、deterministic verification 与 human-escalation closure；
- upstream 不维护具体语言 / framework 技术知识 Rule family；technology specialization 由 Consumer-local Authority 持有；
- Issue #164 已完成 R1～R4：核心边界、评估入口、Rule Discovery / Evidence contract、Bootstrap 成本与真实 Consumer applicability 均已完成收敛和独立验证。

上述 baseline 在 Issue #172 重构完成前继续是当前已集成运行事实；本轮新目标不通过 planning 文档提前改写现行 Capability semantics。

稳定演进里程碑与历史原因由 `docs/project/project-evolution.md` 持有；精确 branch / Issue / PR / Actions / commit 状态始终从 GitHub 当前事实读取。

## 当前演进

Issue #172 — **发布模型重构：从能力仓库直接投影转向 Skills 发布产物** 已获得明确 Planning / Execute Authority。

本轮目标不是简单调整 Consumer 目录，而是正式分离：

```text
agentic-dev Source / Authoring Model
→ deterministic Release Build
→ versioned Software Development Agent Skills
→ Consumer installation / runtime
```

冻结目标、Source / Distribution 边界、Runtime compatibility、Legacy Consumer coverage 与 Acceptance Criteria 由：

- `docs/project/distribution-rebuild-specification.md`

统一持有。

Issue #172 只承担实施协调、Gate 与 Evidence timeline，不作为第二份规范 owner。

本轮实施固定按以下 Gate 推进：

1. Gate A — Specification & Acceptance Freeze
2. Gate B — Repository-wide Asset / Distribution Evidence & Classification
3. Gate C — Source / Distribution Model Rebuild
4. Gate D — Skill Packaging & Release Build
5. Gate E — Automated Runtime Acceptance
6. Gate F — Legacy Consumer Capability Coverage Audit
7. Gate G — Final Specification Conformance Review & Release Candidate Freeze
8. Gate H — Real Consumer Migration & Validation

Gate A～G 在 `agentic-dev` 内连续推进。重构期间不把真实 Consumer mutation / 人工 Consumer validation 作为每个中间 Gate 的阻塞条件；完全自动化的 Consumer-like fixture / runtime acceptance 可以保留。真实 Consumer migration / validation 只在 Release Candidate Freeze 后进入。

## 当前门禁

**当前 Gate：Gate D — Skill Packaging & Release Build。**

Gate A 已冻结 `DR-AC-01`～`DR-AC-39`；Gate B 已完成 Distribution Evidence Review、全仓发布分类与 deterministic distribution audit。

Gate C 已完成 Source / Distribution Model Rebuild：

- Source / Authoring Model 与 Consumer Distribution / Runtime Model 已在 Current Architecture 中分离；
- Method / Architecture / Rule 继续作为 provider-side Source canonical owner，但不再默认投影成 Consumer 同名 runtime asset；
- Skill 明确成为首版主要 Distribution Unit，并允许通过 `references/`、`scripts/`、`assets/` 承载构建后的 supporting semantics；
- Consumer 首次安装 / 后续升级已改为 versioned Release install / update；
- Consumer 根 `AGENTS.md` 保持 Consumer-owned，repository-local 默认目标以 `.agents/README.md + .agents/skills/**` 为核心；
- 普通 Consumer runtime / update 保持 `upstream access = 0`，不把 upstream Rule tree / Rule Discovery / Source tree 恢复成默认依赖；
- Model Collaboration 等可选能力改为 installed Release 提供 capability 后再建立 local runtime instance。

Gate C 的完整 diff、Actions、Review 与 Integration Evidence 由 PR #175 / Issue #172 / GitHub Actions 持有，本 Roadmap 不复制流水账或精确 merge SHA。

Gate D 只负责：

- 设计首版 release skill set；
- 将必要 Source semantics 编译 / 包装进 Skill；
- 引入实际需要的 `references/`、`scripts/`、`assets/`；
- 建立 deterministic release builder；
- 生成 repository-local install artifact；
- 建立 release identity、provenance、integrity / checksum 与必要 migration metadata；
- 满足 `DR-AC-12`～`DR-AC-19`。

Gate D 不执行真实 Consumer migration / validation；后续 Gate 不因出现在本文中自动跳过当前门禁。

## 后续候选

当前除 Issue #172 之外的演进候选保持非活动状态：

- Review Governance / Human Review 的跨 Consumer 持续有效性；
- GitHub / execution transport / human escalation 的新平台证据；
- Requirement Baseline / Architecture Clarification 的更多真实 Consumer validation；
- C6 verification invariant 与 deterministic current-owner tooling 的跨案例 Evidence；
- Consumer feedback（包括 Issue #58）与未来 Method selection scaling；
- 独立 `code-review` Skill 是否成立；
- setup / install / upgrade orchestration 是否需要独立 Skill；
- Plugin 或其他 Distribution Target。

这些候选不得插入 Issue #172 的当前 Gate，除非当前 Acceptance Evidence 证明其已成为完成本轮重构的必要条件；若会改变冻结 Acceptance，必须先修改重构规范并完成独立复核。

## 已知约束

- Issue #172 重构期间，当前已集成 Method / Architecture / Rule / Skill semantics 仍是 Repository ordinary runtime Authority，直到对应 Gate 明确替换并集成；
- Source Model 与 Distribution Model 分离不等于把所有内部 Method / Architecture / Rule 机械删除或全部塞入单个 Skill；
- Consumer-local Product / Requirement / System Architecture / technology policy / authorization / current state 不得被通用 Release 吸收；
- Architecture Clarification 的 Evidence maturity 仍低于 Requirement Baseline Establishment，应保持 conditional / anti-BDUF；
- C6 verification invariant 继续暂缓，直到出现足够跨案例 Evidence；
- Human Guide、Research、Project Evolution 不进入 ordinary Agent 固定 Bootstrap；只有当前责任明确需要时才加载；
- 每个 Issue #172 实现 PR 必须显式声明 Covered Acceptance IDs、Not Covered IDs 与 Current Evidence；
- 实施不得以便利性静默缩减 `DR-AC-01`～`DR-AC-39`。

## 状态归属

- Repository live state：GitHub；
- 项目使命 / 核心要求：`project-charter.md`；
- Repository-local capability instance：`project-capability-profile.md`；
- Issue #172 冻结目标 / Acceptance：`distribution-rebuild-specification.md`；
- 当前 evolution / gate / compact next candidates：本 Roadmap；
- 稳定历史里程碑：`project-evolution.md`；
- bounded unit 的完整 Gate / Review / Actions / commit Evidence：对应 GitHub Issue / PR / Actions。

Roadmap 不复制完整重构规范、Architecture、Capability body、历史实施日志或完整 Review Evidence。
