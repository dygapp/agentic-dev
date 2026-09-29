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

### 演进事项 4 — 自动化验证路径与本地 Docker 资源生命周期

**来源**：Issue #180。

**问题**：为 AI 开发提供两条相互对应、可独立选择的自动化验证向导：GitHub Actions 路径与无需 GitHub 的本地 Docker 路径。本地路径能够承担 Consumer 选定的 CI 验证，并在持久 Runner 中按真实组件输入复用当前有效镜像与数据库基线、清理被替代版本和临时资源、约束 BuildKit cache，兼顾下一轮局部验证速度与磁盘占用。

排在演进事项 3 之后，避免提前假设 project / component identity。

重新分析先区分：

- 现有 `github-agent-workflow` 平台导航、`github-actions-verification` 可执行契约与新增 Actions 验证 Guide 的职责；
- 本地 Docker 作为独立验证路径所需的目标身份、可重复入口、证据和失败处理，不把 Actions Run 当作前提；
- 与 Docker 无关的通用 resource lifecycle invariant；
- Docker / BuildKit / GHCR / WSL specialization；
- 已由 `external-operation` / `github-actions-verification` 覆盖的责任；
- Consumer-local 实现政策。

本事项优先以两份按需 Guide 承载对应路径，保持 `execute-unit` / `converge` 的通用验证责任与 `github-actions-verification` 的 Actions 专项责任，不预设新增 Docker Skill、Provider 编排器或 Consumer 固定命令格式。发布镜像与生产部署不进入本事项；只有新的 Evidence 证明现有 Guide / Skill / Consumer-local 机制不足且存在稳定跨 Consumer procedure 时，才重新评估 Provider 能力。

Provider 文档层的结果由 [GitHub Actions 自动化验证 Guide](../guides/github-actions-automated-verification.md)和[本地 Docker 自动化验证 Guide](../guides/docker-automated-verification.md)承载。Issue #180 中的固定命令接口、统一缓存 schema 与真实持久 Consumer Runner 实测仍是原始候选及未验证边界，不因 Guide 建立而被宣称完成；真实采纳和磁盘收益须由具体 Consumer 后续证据证明。

### 演进事项 5 — Git Commit 生命周期与集成历史收敛

**来源**：Issue #188；真实 Consumer `dygapp/jilinjobs-cms` 的 EU-68 与历史 EU 暴露出 Readiness、CI / 测试、debug / Review 修复等执行步骤被机械转换成永久 commit 的问题。

本事项将 commit boundary 与 Method / Gate / Evidence 生命周期解耦：实现、验证与同一逻辑目的内的修复默认属于 Working State；只有 exact-Head Evidence、durable handoff 或其他可恢复 subject 需要时才形成 Candidate Commit；进入集成前通过 History Convergence 清理仅代表过程状态的 WIP / Readiness / Gate / iterative-fix commits，同时保留真正独立、可理解、可验证和可回退的多个 logical commits。因此不建立 `1 EU = 1 commit` 规则。

多仓场景按 Repository 独立收敛：Project Repository 与每个 Component Repository 分别拥有 history、授权和 candidate，父仓不能统一改写被忽略组件仓；需要精确组合时逐仓记录最终 identity / SHA。Git submodule 的 `160000` gitlink 是显式版本绑定，组件 SHA 改写后父仓 gitlink 与相关 Evidence 必须同步更新。没有新增 Commit Skill、中央 orchestrator、固定 baseline schema 或 Gate Framework。

**完成 Evidence**：implementation candidate `e21f207ebdcfa7bccccbf02079e28eff1f986db4`；14 / 14 deterministic repository contracts PASS；Fresh / Independent Review `Blocking=0`、`Medium=0`；`v0.2.0 → v0.2.1` release smoke 保持 15 个 Skill、只替换 `execute-unit` / `converge`、Consumer-owned 文件不变。正式发布身份由 `agentic-dev-v0.2.1` immutable tag 持有。

## 5. 默认顺序

```text
演进事项 1 — Skill 与项目权威的适配边界
→ 演进事项 2 — 小规模变更的执行粒度
→ 演进事项 3 — 多仓库项目的工作区与权威边界
→ 演进事项 4 — 自动化验证路径与本地 Docker 资源生命周期
→ 演进事项 5 — Git Commit 生命周期与集成历史收敛
```

顺序只表达当前规划：

- 先处理 Skill 与项目权威的适配边界；
- 再收敛小规模变更的执行粒度；
- 再澄清多仓库项目的工作区与权威边界；
- 再评估依赖项目 / 组件身份的本地 Docker 验证与资源治理，并与 GitHub Actions 路径建立对应导航；
- 随后的真实 Consumer commit-history Evidence 再启动事项 5，不把它预设为事项 4 的派生步骤。

每个事项收口后都可以基于新 Evidence 调整、拆分或删除后续事项。

## 6. 当前停止点

演进事项 1～3 已按各自 Issue / PR / Git Evidence 集成。事项 4 基于 Issue #180 收敛为 GitHub Actions 与本地 Docker 两条按需验证 Guide。事项 5 基于 Issue #188 收敛 Working State、Candidate Commit 与 History Convergence，并同时覆盖单仓、嵌套独立仓与 submodule；本次 runtime delta 通过 `agentic-dev-v0.2.1` 发布。

当前不预设下一演进事项。真实 Consumer adoption、多轮 Docker 构建的磁盘占用与回收、不同宿主的运行差异，以及任何发布环境用途都不属于已验证的 Provider 成果；若后续 Evidence 显示新的稳定跨 Consumer 缺口，另行确认 owner、边界和验收，再决定是否进入新的演进事项。
