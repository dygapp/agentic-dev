---
id: guide:establishing-requirement-baseline
type: guide
status: active
---

# 建立项目 Requirement Baseline

本文面向人类说明：一个新项目如何从原始需求材料开始，逐步形成可被 AI 开发稳定消费的 Requirement Baseline。

规范过程由 `method:requirement-baseline-establishment` 持有；Requirement ownership 与推荐 `docs/requirements` 信息架构由 `architecture:requirement-authority` 持有。本文只提供可操作的 Human View，不建立第二套 Method / Architecture Authority。

## 1. 什么时候需要这套流程

适合：

- 新项目 / 新产品；
- 已有一批客户需求、招标文件、PRD、访谈材料，但还没有稳定需求基线；
- legacy rewrite / modernization，需要重新确认现行需求；
- 现有需求文档彼此冲突、重复、边界不清；
- 多个 Feature 不断因为同一批业务事实缺失而返工。

如果项目已经有稳定 Requirement Authority，普通 Feature 不需要重跑这套流程，直接进入当前项目采用的 Feature Development Method。

## 2. 不要从“列功能”开始

更可靠的开始方式是先恢复六类业务事实：

```text
业务对象
业务活动
业务规则
状态 / 生命周期
角色 / 职责
外部依赖 / 输入输出
```

尽量回答：

> 谁，在什么条件下，对什么业务对象做什么，受什么规则和状态约束，最终产生什么业务结果？

不要一开始从以下内容反推产品边界：

```text
页面
菜单
API
数据库表
代码模块
微服务
```

这些通常是后续设计结果，不是需求事实本身。

## 3. 推荐的 `docs/requirements` 起始结构

```text
docs/requirements/
├── README.md
├── index.md
├── overview/
├── business/
├── aspects/
├── non-functional/
└── analysis/
```

这是推荐结构，不是所有 Consumer 的强制物理路径。

### README

给人解释：

- 这套 Requirements 怎么组织；
- 各类目录 / owner 的职责；
- 怎样新增、修改、复核需求；
- 哪些内容是 Authority，哪些不是。

不要在 README 再维护完整需求清单。

### index

只回答：

> 当前某个 Requirement / Capability 的 Authority 在哪里？

可以记录名称、分类、owner locator 和必要关系，但不要复制业务规则正文。

### overview

通常包括：

- 项目 / 产品目标；
- In Scope / Out of Scope；
- 产品 / 系统责任边界；
- 主要 Actor；
- Capability Map；
- 项目级统一约束。

### business

项目的主要纵向 Requirement Capability owner。

### aspects

只放真正跨多个 Capability、具有独立业务 / Acceptance 意义、又无法合理归属单一 Capability 的 Requirement。

不要把 aspects 当“其他内容”目录。

### non-functional

放真正可验收的性能、安全、容量、可用性、合规等系统性质。

### analysis

临时工作区。source inventory、比较表、歧义清单、状态图、关系图、会话草稿等默认不是长期 Authority。

## 4. 如果客户已经提供了很详细的需求材料

不要为了“走流程”重新把所有内容问一遍。

正确过程是：

```text
读取原始材料
→ 判断来源与事实地位
→ 提取 Requirement Facts
→ 建立 Capability / Owner
→ 自动推导能唯一确定的结果
→ 只处理剩余真实歧义
→ Human Review
→ Requirement Baseline Ready
```

原始资料越完整，Human Question 应越少。

“Requirement Baseline Establishment”不等于“Requirement Interview”。

## 5. 会话式需求获取：默认使用 Delta Conversation

AI 内部可以做完整分析，但普通交互默认只向人工输出当前需要处理的增量。

不推荐：

```text
重复上轮所有已确认结论
+ 大段背景解释
+ 三个问题
+ 再次总结全部项目
```

推荐：

```text
当前需要确认 2 项：

1. 学院审核是否为必经步骤？
   影响：就业方案状态机和角色责任。
   A. 必经
   B. 学校可配置

2. 解约通过后当前就业信息如何处理？
   影响：当前状态与历史数据语义。
   A. 清空当前就业信息
   B. 保留当前信息并标记失效

可直接回复：1B，2A。
```

确认后下一轮只说明必要增量，例如：

```text
已更新：学院审核由学校配置；解约后清空当前就业信息。

当前没有新的 Blocking Ambiguity，继续整理本 Capability。
```

不要重新打印整份历史确认结果。

## 6. AI 提问前先执行 Question Gate

候选问题依次判断：

```text
现有 Authority 能回答？
    → 能：不问

已确认事实能唯一推导？
    → 能：推导，不问

已有 Project Requirement Default？
    → 有：应用，不问

属于 Design Item？
    → 是：推迟，不问

只是缺少 Evidence 支持额外机制？
    → 是：默认不新增机制

存在多个合理业务答案？
    → 否：采用最小合理结果

不同答案会实质改变业务行为 / 验收？
    → 否：不升级人工

不解决会阻塞 Requirement Baseline？
    → 否：记录 non-blocking open item

以上都满足
    → Ask Human
```

核心原则：

> “AI 不知道”不等于“人工必须回答”。

## 7. 能推导的，不要再逐项确认

例如已经明确：

> 学校审核通过形成最终学校确认结果；最终学校确认结果学生不可修改。

就不要继续问：

- 学生还能不能修改？
- 是否需要再次提交？
- 是否要新增“锁定”按钮？
- 是否要给每一种角色分别确认一次？

如果下游结果由已确认上游规则唯一决定，应直接记录推导结果。

这类重复提问是需求分析无法收敛的主要原因之一。

## 8. 没有 Evidence 时，不要穷举不存在的机制

不要这样完成需求确认：

```text
是否需要审核？
是否需要复核？
是否需要版本？
是否需要通知？
是否需要归档？
是否需要批量导入？
是否需要自动同步？
```

不存在的可能功能是无限集合，不可能通过人工逐个否定完成“完整需求”。

没有 Evidence 支持时，默认不新增额外业务机制，例如：

- 审核 / 审批 / 复核；
- 通知 / 催办；
- 整改闭环；
- 版本管理；
- 归档；
- 自动同步；
- 批量能力；
- 额外业务状态；
- 额外角色。

如果项目确实存在一类重复的常规行为，可以先让 Product Authority 确认一个 **Project Requirement Default**，然后后续 Capability 统一使用，不再逐项提问。

## 9. 先问上游因果问题

如果一个决定会唯一决定多个下游结果，只确认上游决定。

例如：

```text
学院审核是否存在？
```

可能直接决定：

```text
状态
角色权限
流转路径
不通过后的返回对象
部分操作入口
```

不要在上游决定尚未确认时同时把全部下游分支都生成人工问题。

## 10. 一个问题应该有多短

一个人工问题默认只包含：

```text
Decision
必要 Context
Impact
Options / expected answer
```

例如：

> **Q3 学院审核是否为必经？** 现有材料同时出现“学生→学院→学校”和“学生→学校”。这会改变状态机与学院角色责任。A. 必经；B. 学校可配置；C. 不存在学院审核。

不需要附上此前全部讨论、完整 Capability 文档或后续技术设计建议。

## 11. 什么时候停止向下追问

一个 Requirement Capability 已经能明确以下内容时，应认真判断是否已经达到 Requirement 深度：

- Goal / Scope / Out of Scope；
- 核心业务对象；
- Actor / Responsibility；
- 主要状态与转换；
- 关键业务规则；
- 数据范围 / 语义；
- 跨 Capability 输入输出；
- 主要失败结果；
- Acceptance。

如果继续追问开始集中在：

```text
字段
按钮
菜单
页面布局
API
数据库
缓存
事务
类 / 包
```

通常应该停止 Requirement 下钻，把问题留给 Specification / Technical Planning / Execute。

## 12. 用 Capability Review 代替逐条确认

完成一个 Requirement Capability 后，推荐给人工一个短 Review 摘要，而不是再次逐条问答：

```text
就业方案管理 — Review

范围：
学生填报 → 学院可选审核 → 学校审核。

AI 自动推导：
- 学校审核通过后学生不可修改当前方案。
- 未通过返回学生修改。
- 学院审核未启用时直接进入学校审核。

采用默认：
- 不新增省级审核。
- 不新增独立草稿状态。
- 不新增审核通知机制。

仍有 1 个真实歧义：
1. 学院审核是否按学校统一配置？

完整 Authority：
docs/requirements/business/employment-scheme.md
```

人工可以直接回复：

```text
整体通过。学院审核按学校配置。
```

然后 AI 把决定 promote 到 Requirement Authority，再继续下一个 Capability。

## 13. 人工在这个流程中的主要角色

人工不是逐字段 Requirement Generator。

更合适的角色是：

- Product / Domain Authority；
- 对真实业务歧义做裁决；
- 对 Capability 整体结果做 Review；
- 发现 AI 推导错误时纠偏；
- 对项目级 Default Policy 做确认；
- 对高风险 Requirement Baseline 变换进行独立语义 Review。

AI 负责：

- 提取事实；
- 建立 ownership；
- 自动推导；
- 应用已确认默认；
- 发现冲突 / 歧义；
- 组织 Requirement Authority；
- 控制问题下钻尺度；
- 只把真正需要 Authority 的决定交给人。

## 14. 完成 Requirement Baseline 后

完成条件不是“所有未来 Feature 都已经写完”。

更重要的是：

- 主要长期事实都有 owner；
- 主要业务边界明确；
- Requirement Authority Index 可以定位需求；
- 真实高影响歧义已关闭；
- Fresh Context Agent 不依赖历史聊天也可以理解主要 Capability；
- 仍未确定的问题已经正确分类为 external / design / non-blocking。

达到 `Requirement Baseline Ready` 后：

- 没有 systemic architecture blocker → 可以开始具体 Feature Development；
- 有跨多个 Feature 的长期 Architecture blocker → 进入 `method:architecture-clarification`；
- 后续普通 Feature 使用 `method:ai-development`，不重复整套项目需求建立流程。