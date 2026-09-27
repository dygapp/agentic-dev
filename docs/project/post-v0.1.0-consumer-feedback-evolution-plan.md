---
id: project:post-v0.1.0-consumer-feedback-evolution-plan
type: project
status: active
---

# v0.1.0 后 Consumer 反馈演进计划

## 1. 目的

把 `agentic-dev-v0.1.0` 之后仍有效的 Consumer 反馈收敛为**小粒度、顺序执行、逐项闭环**的演进事项，避免多个问题在同一上下文中一起分析，重新形成过长上下文和过度设计。

本文件只拥有演进事项、顺序、边界和统一闭环协议；Issue / Research 提供 Evidence，Skill / Guide / governance 继续拥有各自正式语义。

## 2. 基线与约束

本计划的发布起点：

- Release：`agentic-dev-v0.1.0`
- Integration commit：`ae8ee8032e34c046d619c719dad408edda2d2d8a`
- `skills/**` 是唯一正式 Consumer runtime product；
- Guides 只做按需 Bootstrap、方法理解和导航；
- Consumer 拥有项目事实、架构、current work、技术政策、授权和本地约束；
- 不恢复 Method selector、Rule Discovery、Capability Runtime、custom Release Builder、批量模型 grader 或多级 Gate。

旧 Issue 须在 `v0.1.0` 产品边界下重新解释，旧架构中的候选方案不自动进入当前设计。每个后续事项的执行基线则是开始该事项时最新已集成的 Repository Authority 与精确 HEAD；不得回退到发布起点而忽略此前已完成事项的变化。

## 3. 单项执行协议

一次只推进一个演进事项。当前事项收口前，不展开下一事项的详细分析或实现。

单项的详细 Evidence、方案草稿、交叉评审记录与实施过程默认由对应 GitHub Issue / PR / Git 历史承载；`docs/project/**` 只保留仍具有稳定消费者的长期 Project Authority、Roadmap、当前阶段级演进协议与必要 locator，不为每个演进事项保留一次性详细方案文档。

每个事项统一执行：

1. **证据重新分析**
   - 固定当前精确基线；
   - 读取该事项对应的 Issue / Consumer Evidence；
   - 读取当前真正受影响的 Skill / Guide / governance；
   - 区分：已被当前模型消除、仍存在、Consumer-local、未验证。
2. **必要外部研究**
   - 只研究 Repository / Consumer Evidence 无法回答的具体技术事实；
   - 无必要则显式跳过，不建立大而全研究阶段。
3. **方案收敛**
   - 明确真正的语义 owner、修改范围、Consumer-local 边界、非目标、验收条件与负向约束；
   - 先判断是否无需 Provider 修改，再判断 Guide / 现有 Skill 调整，最后才考虑新增长期能力。
4. **实施**
   - 只实现冻结范围；
   - 不为后续事项预埋 Framework、registry、metadata 或 orchestration。
5. **聚焦验证与必要复核**
   - deterministic test / bounded fixture 优先；
   - 只有当前声明需要时才使用真实 Consumer 或 Runtime Under Test；
   - 高影响 Authority / canonical Skill contract / governance 变化才进入 Fresh / Independent Review。
6. **收口**
   - 回写 Evidence 与最终 owner；
   - 更新本计划 / Roadmap / 对应 Issue；
   - 重新读取最新 baseline，再决定下一个事项是否仍成立。

Issue 中已有判断和候选方案只作为 Evidence。每个事项都必须优先问：

> 当前能力是否已经解决？是否只是 Guide / trigger / input contract 缺口？是否应留在 Consumer-local？是否真的存在稳定、跨 Consumer、可独立触发的新 procedure？

## 4. 后续演进事项

前置状态收口已经完成：Issue #172 已按 `v0.1.0` 当前产品模型明确 superseded / completed 并关闭；旧 Gate H / custom Release 路线不再是 Current responsibility。

### 演进事项 1 — Skill 与项目权威的适配边界

**来源**：Issue #58 最新 Design Authority feedback。

**问题**：重新判断 Agent 在使用现有 Skill 完成软件开发责任时，面对 Consumer 新增的合法 Current Authority，是否能够从当前 Repository 按需解析、消费、跨 Fresh Context 恢复、验证并把长期语义返回真实 owner；同时保持 Authority 与 Consumer-local Constraint 的语义边界。

**分析范围**：

- 当前 Skill 对项目权威的输入、使用和反馈回写边界；
- Guide 是否提供了足够的方法导航；
- Consumer-local Authority 是否已经足以解决问题；
- Agent / Skill / Guide / Authority / Constraint / Execution Unit 的主体与责任关系；
- Authority 在 planning / slicing / readiness / execution / debug / convergence / review 中的生命周期；
- 新的项目权威类型是否暴露真正的 Provider 通用缺口。

**非目标**：预设 Design 专用 Skill、通用 Authority registry，或把 Consumer 的 `DESIGN.md` 格式提升为 Provider 标准。

**完成 Evidence**：GitHub Issue #183 / PR #184。详细方案、实现前交叉评审、实施 Evidence 与最终 Fresh / Independent Review 由 GitHub 历史保存；长期稳定结论已回写真实 Architecture / Guide / Skill owner。

演进事项 1 已完成并集成。最终 exact candidate `9335ea22dea972e3b52fee160703d603708b583d` 的 Fresh / Independent Review 结果为 `Blocking=0`、`Medium=0`、`Low=0`、`FINAL REVIEW PASS`；随后通过 PR #184 集成，integration commit 为 `1cf3901d1096ca998a16923363c29f663bc8e1a2`。Focused validation 覆盖 deterministic repository contracts、Provider-unknown Authority bounded scenarios 与真实 Consumer `jilinjobs-cms` 的只读 applicability challenge；真实 Consumer adoption / runtime PASS 仍保持未验证。

### 演进事项 2 — 小规模变更的执行粒度

**来源**：Issue #179。

**完成 Evidence**：Issue #179 / PR #185；最终 candidate `0b346d478b2e49d591a0f2f429f82e9a671715b2` 通过 11/11 deterministic repository contracts 与 Fresh / Independent Review（`Blocking=0`、`Medium=0`、`Low=0`；[只读复核记录](https://github.com/dygapp/agentic-dev/pull/185#issuecomment-5855895673)）。CI Run #17 检出 PR merge ref `5904b00194669a64afdda7cba13cd40ff9f99854`，与 candidate 无文件差异并通过；随后集成于 `765ed1e48c4840402cfe13e8ce5c60cd342c020c`。

本事项把执行粒度与 branch / commit / CI / PR 集成政策分开：目标和验收可从当前 Consumer Authority 恢复、修改局部低风险可逆且无需独立执行生命周期时，Agent 可直接实施有界变更并按范围验证；正式 Execution Unit 留给需要独立恢复、协调依赖或独立验收的责任。`converge` 支持无正式 Unit 的完整变更判断。持续工作区中的未提交差异与本地验证是当前执行态证据，长期事实仍进入可恢复的 Repository / GitHub 状态；集成政策由 Consumer 自己决定。

没有新增 Direct Change / Work Batch artifact、Skill、WebCodex 专用 Method 或 GitHub transport Framework。真实 Consumer adoption / runtime PASS 尚未验证。

### 演进事项 3 — 多仓库项目的工作区与权威边界

**来源**：Issue #181。

**完成 Evidence**：Issue #181 / PR #186；最终 candidate `1f4e2b1a8b8f434265f5048b7f7d9e341c22b15f` 通过 12/12 deterministic repository contracts、嵌套 Git 隔离样例与 Fresh / Independent Review（`Blocking=0`、`Medium=0`、`Low=0`；[只读复核记录](https://github.com/dygapp/agentic-dev/pull/186#issuecomment-5856587052)）。CI Run #21 检出与 candidate 无文件差异的 PR merge ref `deaa137ed8abf40723b9a98c86f6c96e66603557` 并通过；PR #186 集成于 `b9ebbecf485192532071a4b25c1894ce18f327f6`。

本事项将 Project Repository + nested independent Component Repositories 确认为**推荐但非必选**的多仓库布局。项目级与组件级事实各有 Consumer-owned owner，跨仓 Fresh Context、Git 状态和授权逐仓恢复；父仓忽略组件目录不等于跟踪组件版本或免除 gitlink / 强制清理风险。跨仓集成、可重建候选或发布声明才需要明确项目与参与组件的精确身份 / SHA 组合，普通单仓变更不强制维护全量 baseline。长期方法导航在 [多仓库软件项目 Guide](../guides/multi-repository-projects.md)，没有新增 Skill、固定 `repositories.yaml` schema、bootstrap orchestrator 或 central registry。真实 Consumer adoption、跨宿主 instruction / Skill 发现及实际跨仓 CI 重建仍未验证。

### 演进事项 4 — 本地验证环境的资源生命周期

**来源**：Issue #180。

**问题**：持久本地 Runner 中，验证镜像、BuildKit cache 和临时 container / volume / network 怎样避免无界增长和跨项目误删。

排在演进事项 3 之后，避免提前假设 project / component identity。

重新分析先区分：

- 与 Docker 无关的通用 resource lifecycle invariant；
- Docker / BuildKit / GHCR / WSL specialization；
- 已由 `external-operation` / `github-actions-verification` 覆盖的责任；
- Consumer-local 实现政策。

当前不预设新增 Docker Skill。只有新的 Evidence 证明存在稳定、跨 Consumer 的 reusable procedure 时，才重新评估 Provider 能力。

## 5. 默认顺序

```text
演进事项 1 — Skill 与项目权威的适配边界
→ 演进事项 2 — 小规模变更的执行粒度
→ 演进事项 3 — 多仓库项目的工作区与权威边界
→ 演进事项 4 — 本地验证环境的资源生命周期
```

顺序只表达当前规划：

- 先处理 Skill 与项目权威的适配边界；
- 再收敛小规模变更的执行粒度；
- 再澄清多仓库项目的工作区与权威边界；
- 最后评估依赖项目 / 组件身份的本地验证资源治理。

每个事项收口后都可以基于新 Evidence 调整、拆分或删除后续事项。

## 6. 当前停止点

演进事项 3 已完成多仓库项目推荐布局与权威边界的方法导航，并通过 PR #186 集成到 `master`。完整实施与验证过程由 Issue #181、PR #186 和 Git 历史保存；真实 Consumer adoption、跨宿主 instruction / Skill 发现及实际跨仓 CI 重建仍不属于已验证事实。

集成后重新核验：Issue #180 仍开放。演进事项 3 明确了 project / component identity，但未提供跳过事项 4 或预设 Docker 实现方案的新证据。下一责任暂为**演进事项 4 — 本地验证环境的资源生命周期**；进入时从最新 Repository Authority 重新分析 Issue #180，先区分通用资源生命周期、Docker / WSL 专项与 Consumer-local policy，不因已推荐嵌套布局就预设缓存 schema 或新 Skill。
