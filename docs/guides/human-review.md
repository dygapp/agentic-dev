---
id: guide:human-review
type: guide
status: active
---

# 人工评审使用指南

本文帮助人和 AI 理解：在普通 Consumer 软件项目中，怎样使用 `human-review` Skill，把需求、功能规格、架构或技术方案整理成便于人工理解和判断的材料，并把人工确认产生的长期语义正确返回真实 Authority。

真正的执行契约由 installed `human-review` Skill 持有；Requirement、Specification、Architecture 和 Technical decisions 仍由 Consumer 自己的真实 owner 持有。本文只提供方法导航、评审材料组织原则和人类可读示例，不建立第二套执行或事实 Authority。

## 1. 人工评审解决什么问题

Human Review 不是新的通用开发阶段，也不是每层文档都必须经过一次审批。

它主要解决两件事：

1. 把当前真实 Authority 中已经存在的内容重新组织成人容易理解、比较和判断的评审材料；
2. 把人工评审产生的语义修正或新增长期决定，准确回写到真正拥有这些事实的 Requirement、Specification、Architecture 或 Technical owner。

因此人工评审的核心不是“多生成一份文档”，而是：

```text
Current Authority
→ Human-readable Review Draft
→ Human Review
→ Feedback classification
→ durable semantic change 写回真实 owner
→ 重新生成 Review Draft
```

Review Draft、图形和最终交付文件默认都不是新的事实来源。

## 2. 什么时候值得进入人工评审

可以把调用情况理解成三类。

### 必须评审

如果不经过人工判断，就不能安全确定真实产品意图、长期高影响结构或高风险技术责任，例如：

- 多个合理业务解释会改变 Scope、State、Permission、Data Semantics、Business Result、Compliance 或 Acceptance；
- 跨多个 Feature 的高成本难逆 Architecture decision；
- 安全、隐私、核心数据、共享契约、生产拓扑或不可逆迁移等高影响边界；
- 当前执行者没有足够 Authority 自行作出 durable decision。

### 建议评审

AI 已经可以形成完整候选，但集中人工审阅能显著降低误解、遗漏或返工风险，例如：

- Requirement Baseline 的 Capability-level Review；
- 新增或实质改变用户可见行为、主要流程、失败语义或 Acceptance；
- 跨模块、多角色、全生命周期场景，需要把多个 owner 的事实组合成端到端视图；
- 大型 Architecture / Technical Plan 已经形成，但值得在进入高成本实现前集中复核。

### 无需评审

普通局部、低风险、可逆，并且现有 Authority 已经能够唯一决定结果的工作，不因为 Human Review capability 存在就增加固定人工审批。

## 3. 默认先做 Markdown Review Draft

没有明确交付格式要求时，默认只生成 **结构化 Markdown 评审草稿**。

这份草稿按当前评审对象组织，不要求所有项目套同一个模板。通常只选择真正有助于判断的内容，例如：

- 评审目标与范围；
- 已确认事实；
- 当前方案或可观察行为；
- 角色与责任；
- 主要流程 / 生命周期；
- 关键规则与状态；
- 边界和失败行为；
- Acceptance / 判断依据；
- 相对当前基线的变化；
- 待确认事项；
- 已发现缺口或冲突。

不要为了“材料完整”机械生成空章节，也不要因为要给人看就重新解释或改写已有业务事实。

## 4. Review Draft 为什么不是 Authority

Review Draft 是一个临时投影。

例如不同 Requirement owners 分别记录了发起方、业务处理方和后续服务的职责，评审时可以把它们组合成一份完整流程：

```text
发起方提交
→ 业务处理方处理
→ 后续服务继续生命周期
```

如果所有环节都能由当前 Requirement owners 唯一恢复，这份流程只是为了帮助人理解，不需要再建立一套“业务模型 Authority”。

如果组合时暴露了真实缺口，例如谁负责触发下一步、某状态何时结束、失败后由谁处理、跨模块交接条件是什么，这些问题应返回真正的 Requirement owner 处理，而不是只在 Review Draft 或流程图里补一句说明。

## 5. 流程图、状态图和架构图什么时候生成

图形是按需辅助视图，不是必备产物。

只有明显提升人工理解或判断效率时才生成，例如：

- 多角色流程 → 泳道图；
- 状态转换复杂 → 状态图；
- 多模块责任关系 → 关系图或矩阵；
- 长期 Architecture boundary → 架构图；
- 决策和依赖较多 → 思维导图或矩阵。

这些视图应满足：

- 可以从 Current Authority / Review Draft 重新生成；
- 删除后不影响项目事实恢复；
- 图里出现的新语义必须返回真实 owner；
- 默认不建立需要长期双向同步的 BPMN / UML / Business Model 中间层。

只有客户合同、法规或其他外部 Authority 明确要求某种模型本身成为正式交付依据时，目标 Consumer 才需要单独决定其长期责任。

## 6. 人工反馈分成四类

评审反馈不要统一当成“改文档”。先判断它改变的到底是什么。

### 展示反馈

例如调整章节顺序、修改措辞、优化表格和图形布局、改变 HTML 展开方式。这类反馈只修改评审投影，不修改产品或架构 Authority。

### 语义修正

例如人工明确指出：

> “业务处理完成后仍允许发起方修改当前对象。”

如果当前 Requirement 写的是“不允许修改”，这不是 Review Draft 的文字问题，而是 Requirement fact 被人工修正。应更新真正的 Requirement owner。

### 新增长期决定

如果当前 Authority 从未定义某个长期规则，而人工明确决定：

> “所有适用业务单元统一采用这一失败处理规则。”

只要它会长期约束后续开发与 Acceptance，就必须进入适当的 Requirement / Specification / Architecture / Technical owner，而不是只停留在评审会议或聊天记录里。

### 未决问题

如果人工暂时没有答案，就保持 unresolved。不要为了“完成评审”给它补一个看似合理但没有 Authority 的结论。

## 7. 语义反馈必须真正回写 Authority

Human Review 的关键闭环是：

```text
人工反馈
→ 判断是否改变长期语义
→ 找到真实 semantic owner
→ 更新 owner
→ 重新读取 owner，确认变更真实存在
→ 重新生成或校准 Review Draft
```

不要采用以下做法：

- 只修改 Review Draft；
- 只在 DOCX / HTML 中修正；
- 在下游 Technical Plan 里静默覆盖上游 Requirement；
- 把人工确认长期留在聊天记录中；
- 仅记录“待回写”，却把评审状态标为完成。

如果当前执行者没有目标 Repository 的写入权限，可以记录明确的待回写动作并返回，但状态仍是：

> **待权威回写 / 评审未完成**

后续具备权限的执行者必须完成真实写入、重新读取并重新生成评审投影后，才能声明语义已经收敛。

## 8. HTML 和 DOCX 不是默认产物

默认：

```text
delivery_target = none
```

只有明确要求最终交付格式时，才生成 HTML、DOCX 或其他格式。

### HTML

适合交互式人工审核，例如章节导航、展开 / 收起、只看待确认项、有限筛选、临时流程 / 状态 / 架构视图以及差异、风险和决策项突出展示。

默认应是静态、轻量、容易归档和重新生成的评审视图，不需要为了展示再做一套后台系统。

### DOCX

适合正式需求确认、设计确认、客户交付、归档或签章。

格式优先级是：

1. 客户 / 合同 / 法规明确模板；
2. Consumer 已确认的本地文档规范；
3. 都没有时使用通用的中文正式办公文档默认配置。

正式 DOCX 通常应基于已经完成 Authority 回写并重新核验的收敛内容生成。内容尚未收敛时，如果人工明确要求先输出 DOCX，应清楚标识为“草案 / 待确认”。

## 9. 一次评审什么时候算完成

从人类使用角度，可以用以下问题快速判断：

- 我们已经知道本次到底评审什么吗？
- 需要人工判断的高价值问题都处理了吗，或者明确保持 unresolved 吗？
- 所有确认后的长期语义变化都真的进入了正确 Authority 吗？
- 回写后重新读取过 Authority 吗？
- Review Draft 已根据最新 Authority 重新生成或校准吗？
- 是否还有 durable fact 只存在于聊天、草稿、图形或待办列表里？
- 没有显式交付要求时，是否已经在 Markdown Review Draft 停止，而不是继续制造格式文件？

这些条件满足后，Human Review 才算完成。

Human Review 完成仍然不代表 PR 已通过独立变更复核，也不代表可以 merge、release、deploy 或执行其他高影响外部操作。

## 10. Human Review 与 `review-change` 不是一件事

两者都包含“Review”这个词，但责任不同。

### Human Review

服务对象是产品、业务、架构或工程责任人，帮助他们理解和确认 Consumer 软件项目中的需求、行为、架构与技术方案。

### `review-change`

服务对象是 Repository change，独立检查一个变更是否符合当前 Authority、范围、规则、Evidence 和 artifact lifecycle。

Human Review 通过不能替代 `review-change`；`review-change` 通过也不能代替客户、产品或架构责任人的人工确认。

## 11. 一个典型使用流程

例如一个项目完成了新的 Requirement Capability，希望人工整体确认：

```text
1. AI 从当前 Requirement Authority 生成 Markdown Review Draft
2. 按需要生成一个跨角色流程图
3. 人工提出：两处展示调整、一个业务规则修正、一个暂不决定的问题
4. AI 分类：展示调整 → projection；业务规则 → 回写 Requirement owner；暂不决定 → unresolved
5. 回写后重新读取 Requirement owner
6. 重新生成 Review Draft
7. 人工确认内容
8. 如果明确要求正式 Word 文档，再生成并验证 DOCX
```

这里真正长期保存的是更新后的 Requirement Authority；Review Draft、流程图和 DOCX 都是围绕 Authority 的人工视图或交付投影。

## 12. 和 Requirement / Specification / Architecture / Technical Plan 怎样配合

Human Review 是横向能力，不拥有这些阶段本身。

- **Requirement**：确认 Product / Domain facts、业务规则、生命周期、范围和 Acceptance intent；
- **Specification**：确认用户可见行为、主要流程、失败语义和可验证 Acceptance；
- **Architecture**：确认长期、跨 Feature、高成本难逆的结构和责任边界；
- **Technical Plan**：确认当前实现方案中的高风险迁移、共享接口、生产影响或超出当前授权的工程决定。

普通、局部、可逆的实现 HOW 不应因为 Human Review capability 存在而不断升级给人工。

## 13. 进一步阅读

执行与复核入口：

- `skills/human-review/SKILL.md` — Consumer 项目人工评审的 canonical 执行过程；
- `skills/review-change/SKILL.md` — Repository change 的独立变更复核；
- Consumer 自己的 Requirement / Specification / Architecture / Technical Authority — 人工反馈的真实长期回写位置。

人类导航：

- `docs/guides/establishing-requirement-baseline.md` — 新项目 Requirement Baseline 建立过程；
- `docs/guides/using-agentic-dev.md` — `agentic-dev` 能力体系总览。
