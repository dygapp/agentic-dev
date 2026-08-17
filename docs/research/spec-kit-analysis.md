# 研究总结 — github/spec-kit

**研究日期：** 2026-08-17  
**性质：** 非规范性研究输入

## 1. 项目定位

上游仓库：

https://github.com/github/spec-kit

Spec Kit 是一个更明确的 Spec-driven Development 工具体系，具有比 `mattpocock/skills` 更完整的 Lifecycle 和 Artifact Model。

## 2. 主要观察

### 2.1 Lifecycle / Artifact Model 更完整

Spec Kit 对 Specification、Plan、Tasks、Analysis 和 Implementation 之间的关系定义更加明确，因此非常适合作为“生命周期完整性”的对照样本。

### 2.2 WHAT / WHY 与 HOW 分离更清晰

Specification 更强调产品意图和必须实现的行为，Technical Design 交给 Planning。

这一点被当前方法直接吸收：

```text
Specification = WHAT / WHY
Technical Plan = HOW
```

### 2.3 Technical Planning 有独立语义价值

本方法吸收 Technical Plan 的语义角色，但不把它变成所有 Feature 的强制产物。

### 2.4 Cross-artifact Consistency 很有价值

实施前应该检查：

- Ambiguity
- Missing Coverage
- Duplication
- Contradiction
- Orphan Work
- Dependency / Ordering
- Governance Conflict

这直接形成了本方法的 **Readiness Gate**。

### 2.5 Convergence 与 Code Review 不同

Feature 最终是否与 Specification 一致，是比 Local Diff Review 更高一层的问题。

这形成了独立的 `converge` 职责。

## 3. 本方法吸收的内容

- WHAT / WHY 与 HOW 分离
- Optional Durable Technical Plan
- Structured Readiness Analysis
- Requirement-to-execution Coverage
- Cross-artifact Consistency
- Feature-wide Convergence

## 4. 未直接照搬的内容

- 每个 Feature 强制产生完整 Artifact 套餐；
- 固定 Slash-command Lifecycle；
- 每个 Task 强制带精确 File Paths；
- 上游特定 Template / CLI Structure。

当前方法强调：

> 流程和产物应与工作复杂度成比例。

## 5. 参考

- https://github.com/github/spec-kit
- https://github.com/github/spec-kit/blob/main/README.md
