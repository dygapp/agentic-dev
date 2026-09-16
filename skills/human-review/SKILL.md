---
name: human-review
description: 为 Consumer 软件项目准备结构化人工评审材料，分类人工反馈，并把确认后的长期语义返回正确的需求、功能规格、架构或技术方案所有者；默认只生成结构化 Markdown 评审草稿，除非调用方明确要求最终交付格式。
metadata:
  agentic-dev-id: "skill:human-review"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
---

# 人工评审

## Purpose

把当前需求、功能规格、架构或技术方案整理成便于人工理解和判断的结构化评审材料，并把人工确认产生的语义变化准确返回真实所有者。

本 Skill 只面向 Consumer 软件项目，不用于 `agentic-dev` 自身的方法论演进、Issue / PR 决策或能力设计过程。

## Trigger

满足以下任一情况时可以调用：

- 当前 Method / Skill 将事项判断为必须人工评审；
- 当前 Method / Skill 将事项判断为建议人工评审；
- 用户、客户、产品、架构或工程责任人明确要求人工评审材料；
- 需要通过跨模块流程、生命周期、角色关系等综合视角发现当前 Authority 是否存在缺口。

普通局部、低风险、可逆且现有 Authority 已能唯一决定结果的工作，不因为本 Skill 存在而自动进入人工评审。

## Inputs

- 当前评审目标与范围；
- 直接相关的 Requirement / Specification / Architecture / Technical owner；
- 必要的上下游关系；
- 当前未决歧义、冲突、临时默认或待决事项；
- Consumer 的语言与术语规范；
- 当前写入授权；
- 可选的交付目标，默认 `delivery_target = none`。

不得为了生成“完整评审材料”默认读取全量项目文档、archive 或无关实现。

## Procedure

1. **确认评审责任**
   - 确认当前对象属于 Consumer 软件项目；
   - 明确评审目标、范围和受众；
   - 判断当前状态是必须评审、建议评审还是仅因人工明确请求而评审；
   - 不自行扩大产品、架构或技术责任。

2. **读取最小权威上下文**
   - 读取当前评审目标直接需要的真实 owner；
   - 只补充能够改变当前判断的上游 / 下游 Authority；
   - 区分 Current Authority、历史证据、临时分析和未决材料。

3. **生成结构化 Markdown 评审草稿**
   - 默认只输出结构化 Markdown；
   - 按当前内容选择必要部分，不强制固定模板；
   - 优先表达评审目标、已确认事实、当前方案、角色责任、主要流程 / 生命周期、规则与状态、边界 / 失败行为、验收、差异、待确认项和已发现缺口；
   - 不为了形式完整制造不存在的章节或额外业务机制。

4. **按需形成临时辅助视图**
   - 只有明显提升理解或判断效率时，才建议或生成流程图、泳道图、状态图、思维导图、关系图、矩阵、架构图或时序图等临时视图；
   - 视图必须能够从当前 Markdown / Authority 重新生成；
   - 不建立持久 BPMN、UML 或业务模型中间层；
   - 图形中发现的新语义问题返回真实 owner。

5. **执行人工评审并分类反馈**
   - 展示反馈：只修改评审投影；
   - 语义修正：回写原真实 owner；
   - 新增长期决定：提升到适当 Requirement / Specification / Architecture / Technical owner；
   - 未决问题：保持 unresolved，不伪装成已确认事实；
   - 一条反馈同时包含展示和语义变化时拆分处理。

6. **回写长期语义**
   - 有写入授权时，更新真实 owner；
   - 没有写入授权时，输出明确的 Required Authority Action，不声称已经完成回写；
   - 不在下游文件中静默覆盖上游 Requirement / Architecture；
   - 不让人工决定长期停留在聊天、评审草稿或图形中。

7. **重新生成并核对评审草稿**
   - 以更新后的 Current Authority 重新生成或校准草稿；
   - 确认没有 durable fact 只存在于草稿、图形或会话；
   - 确认临时投影没有成为第二套 Current Authority。

8. **处理交付目标**
   - `delivery_target = none` 时，到语义收敛为止并停止；
   - 调用方明确要求 `html`、`docx` 或其他格式时，保留已确认内容作为后续交付投影输入；
   - 本 Skill 不通过渲染过程重新解释业务、架构或技术语义；
   - 具体最终格式能力由目标 Repository 已采用的交付机制处理。

## Outputs

默认输出：

- 结构化 Markdown 评审草稿；
- 已发现的缺口、冲突、待确认事项；
- 人工反馈分类结果；
- 已完成的 Authority 回写，或缺少授权时的 Required Authority Action；
- 必要的临时辅助视图或视图建议；
- 若显式要求最终格式，已确认内容与交付目标的后续处理边界。

## Exit Conditions

同时满足以下条件时可以退出：

- 评审范围明确；
- 需要人工判断的高价值问题已处理或明确保持 unresolved；
- 已确认语义变化已回写真正 owner，或已明确列出尚未授权的 Authority Action；
- 评审草稿与最终 Current Authority 一致；
- 不存在只保存在草稿、图形或会话中的长期事实；
- 没有显式交付要求时已经停止在结构化 Markdown 评审草稿；
- 本次评审没有被错误解释为 merge、release、deploy 或独立 change review 授权。

## Escalation

以下情况返回真实责任层或人工权威，不由本 Skill 自行决定：

- Requirement / Product ambiguity 或 Authority conflict；
- 高影响、高成本难逆架构决定超出当前授权；
- 安全、隐私、生产或不可逆数据风险；
- semantic owner 无法唯一确定；
- 外部合同、法规或组织流程要求特殊正式交付物成为权威依据；
- 当前请求实际是独立仓库变更复核，应使用 `review-change` 而不是本 Skill。

人工评审通过不等于仓库变更复核通过，也不授予集成或外部操作权限。
