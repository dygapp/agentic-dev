---
id: research:surgical-change
type: research
status: active
---

# 精准修改与差异范围控制研究

**研究日期：** 2026-09-02  
**性质：** 非规范性 Research

## 1. 研究问题

Surgical Change 不等于“diff 越小越好”。目标是在完成当前工作行为、验证和必要工程责任时，使最终变更仍是一个可解释、可复核、可验证的逻辑变化，同时排除与当前责任无关的 drive-by change。

## 2. 外部 Evidence

研究基线引用：

- Google Engineering Practices — Small CLs；
- Google Engineering Practices — What to Look For in a Code Review；
- Linux Kernel — Submitting Patches；
- Martin Fowler — Opportunistic Refactoring；
- Martin Fowler — Preparatory Refactoring Example。

这些来源共同支持：

- 合理 change 的基本单位是 self-contained / logical change，而不是固定行数或文件数；
- 与当前行为直接相关的测试属于同一逻辑变化，不应为追求“小 diff”被排除；
- 多文件变更可以完全属于同一责任链，少行变更也可能是无关范围膨胀；
- 小型机会式 / preparatory refactoring 在直接服务当前任务、具有行为保持证据且不形成 rabbit hole 时可以合理存在；
- 大型无关重构、格式化或机械清理应与当前功能 / bug fix 分离，以保持可复核性。

## 3. Diff reason chain

最终 diff 中每个变更区域至少应能解释为以下一类：

1. 当前行为 / Acceptance 的直接实现；
2. 当前 Verification responsibility 所需测试、fixture 或验证入口；
3. 为当前变化建立安全实现 seam 所必需的 behavior-preserving preparatory refactoring；
4. 当前修改直接造成的 import / orphan / rename reference 等必要清理；
5. Repository Rule、build 或 generator 明确要求的确定性伴随变化；
6. 当前长期 Authority 要求同步维护的契约、migration 或文档。

只能解释为“顺便更好”的变化，应从当前 diff 移除或形成独立工作。

## 4. 反向边界

精准修改不支持以下机械判断：

- 多文件修改 = 范围过大；
- 少行修改 = 范围正确；
- 用户没有逐字要求的结构调整一律禁止；
- 必要测试、migration、契约或生成物属于额外范围；
- 所有触达区域的既存坏味道都应顺便清理。

如果 preparatory refactoring 规模已经足以明显降低当前 change 的可复核性，应拆成独立前置 change / Execution Unit。

## 5. V4 当前落点

该能力是横切约束，不是独立任务流程。V4 当前规范 owner：

`docs/rules/generation/surgical-change.md`

本 Research 只保留工程证据、reason-chain 模型和边界，不再描述旧 Candidate / Engineering Discipline / milestone 状态。

## 6. 结论

精准修改的核心不是限制文件数，而是让最终变更的每个区域都能沿当前责任链解释，并保持整个 change 可理解、可验证、可安全复核。