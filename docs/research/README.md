---
id: research:index
type: research
status: active
---

# Research

`docs/research/` 保存具有独立长期技术价值的外部规范、工程证据与设计参考。Research 不是 Repository Authority，不参与 ordinary runtime Rule Discovery，也不记录当前 Gate / PR / Issue 状态。

## 使用边界

- 当前项目事实从 `AGENTS.md`、`docs/project/project-roadmap.md` 与 GitHub 当前状态恢复；
- 当前规范语义从 Method / Architecture / Rule / Skill 等真实 owner 读取；
- Research 只有在需要理解外部依据、机制差异或设计取舍时按需加载；
- Research 与 current owner 冲突时，current owner 优先；
- Research 中形成的新长期结论必须进入真实 owner 后才改变仓库行为。

V1～V3 的项目过程、实验流水和阶段状态不因曾经出现在 Research 引用中而恢复 current 语义。

## 当前资料

### Method / Skill

- `agent-skills-specification-analysis.md`
- `mattpocock-skills-analysis.md`
- `spec-kit-analysis.md`
- `superpowers-analysis.md`
- `andrej-karpathy-skills-analysis.md`

### Engineering / Technology / Platform

- `implementation-minimality-and-speculative-complexity-analysis.md`
- `surgical-change-and-diff-scope-control-analysis.md`
- `data-access-scope-boundedness-analysis.md`
- `vue3-typescript-profile-analysis.md`
- `github-stacked-pr-squash-topology.md`

这些材料为当前 `docs/rules/**`、Skill 或架构提供研究依据，但不拥有其 normative body。

### Rule Discovery / Knowledge Activation

- `knowledge-activation-and-code-intelligence-analysis.md`
- `knowledge-activation-evidence-appendix.md`
- `llm-wiki-rule-governance-fit-analysis.md`
- `rule-retrieval-design-reference.md`

它们只作为 V4 `docs/architecture/rule-discovery-architecture.md` 与后续 eval/tool 设计的研究依据；旧 Reviewed Discovery Map、Manifest、Catalog 或 V1～V3 owner 引用均视为研究发生时的历史上下文，不构成当前发现机制。

## 保留原则

只保留离开原任务后仍有独立技术价值的材料。纯阶段状态、一次性审计、里程碑 closure、临时分类表和项目过程应由 Git / Issue / PR 保存，而不是进入 Research archive。