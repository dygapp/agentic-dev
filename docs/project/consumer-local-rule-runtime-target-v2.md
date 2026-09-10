# Consumer-local 规则运行目标模型 v2

## 状态

**Phase A / A1 结果 — Consumer-local Runtime Target Baseline**

上层里程碑：Issue #92 / `docs/project/rule-governance-knowledge-activation-v2.md`

本文属于 `agentic-dev` 的项目级设计与验收 Authority，用于约束规则治理与知识激活 v2 的后续设计；它不覆盖核心方法、架构或 Skill 契约，也不会被 Consumer 自动继承。

## 1. 目标

本目标模型回答的不是“`agentic-dev` 应该如何保存规则”，而是：

> 一个已经采用 `agentic-dev` 能力的真实 Consumer，在普通 Fresh Context 中不重新读取 upstream 的前提下，必须具备什么本地能力，才能可靠发现当前适用规则、确定职责、按需进入 Skill，并始终服从 Consumer Repository Authority？

后续 metadata、Catalog、Guide decomposition、Skill ownership 与 baseline projection 的设计都必须能够落到这个目标模型；如果某个 upstream 方案无法低成本投射为 Consumer-local 长期能力，即使它在 `agentic-dev` 内部实验表现良好，也不能视为 v2 完成方案。

## 2. 现实 Consumer 基线观察

以 `dygapp/jilinjobs-cms` 当前 `main` 作为只读现实样本，可以观察到：

1. `AGENTS.md` 已明确 Repository Authority、Knowledge Boundary、精确 `agentic-dev` baseline、Consumer-local 方法入口和 baseline upgrade 流程；
2. `docs/project/development-method.md` 已明确 ordinary development 不需要每次重新读取 `agentic-dev`，并把已采用的方法规则本地固化；
3. `docs/README.md` 已作为 Documentation Authority Map，区分 Current / Partially Current / Superseded / Historical Evidence 与 Fresh Context 默认读取边界；
4. `README.md` 与 Project Roadmap 已能恢复当前 Planning / Execute Gate、长期架构边界与下一自然 Gate；
5. baseline upgrade 已经实际采用“只吸收 Consumer 需要且具有持续约束价值的规则，不继承 `agentic-dev` 自身 Project Rule”的模式。

因此 Consumer-local-first 并不要求重建现有 Consumer 文档体系。真实缺口主要是：

- 当前 Fresh Context 仍主要依靠读取多个较大的本地 Authority / Method / Roadmap 文档后，由 Agent 自己在正文中寻找当前适用规则；
- 已采纳 reusable rule、Consumer-native governance rule、Domain / Architecture / Verification Authority 虽然都在本地，但缺少一个统一、薄、可按任务过滤的发现层；
- 当前 baseline provenance 已经存在，但没有统一参与普通 Runtime 的本地规则发现；
- 如果继续通过向 `AGENTS.md`、Development Method 或 Roadmap 增加正文规则来提高可发现性，会重新放大 Fresh Context 输入并增加重复维护风险。

v2 因此应在现有 Consumer Authority **之上**建立最小发现能力，而不是替换或复制其 Authority。

## 3. Consumer-local Runtime 的五类对象

A1 不冻结物理目录或 schema 字段，但后续设计必须能表达以下五类不同对象。

### 3.1 Consumer Bootstrap / Repository Authority

职责：

- 建立 Consumer Repository Authority 优先级；
- 给出本地规则发现入口；
- 定义最少的跨任务不变量；
- 明确普通工作是否允许访问 upstream。

它必须很薄。不能把全部方法、所有 Skill、全部架构规则或当前执行历史继续塞入 Bootstrap。

### 3.2 Consumer-native Authority

由 Consumer 自己拥有的项目事实与规则，例如：

- Repository governance；
- Requirement / Specification；
- Domain / Architecture / ADR；
- Verification / Integration policy；
- Project Roadmap / current gate；
- project-specific technology / configuration rules；
- 当前 Work / Evidence。

这些内容不来自 `agentic-dev`，也不能因为进入统一发现机制而被降级为 reusable capability 的附属数据。

### 3.3 Adopted reusable rule / module

来源于 `agentic-dev` 或其他被 Consumer 显式接受的可复用规则，但已经经过 Consumer adoption：

```text
upstream candidate
→ compare against current Consumer Authority
→ adopt / retain-or-override / reject-not-applicable
→ persist locally when durable
```

一旦需要约束普通后续工作，就必须具有 Consumer-local 可发现载体。普通 Runtime 不通过远程读取 upstream 才知道这条规则。

本地载体可以保留 upstream provenance，但 provenance 不提升为 Consumer Authority，也不意味着 future upstream commit 自动覆盖当前本地规则。

### 3.4 Reusable Skill / execution capability

Skill 表示稳定职责的执行过程。

Consumer 可以按精确 baseline 采用、安装、复制或以其他可本地解析的方式暴露所需 Skill；v2 不在 A1 阶段规定固定分发机制。

运行时只有在真正进入对应职责执行时才需要加载完整 Skill。仅进行职责识别、Stage Return 或发现判断时，不要求机械读取 Skill 正文。

Consumer-specific rule 可以选择、限制或覆盖 Skill 对项目事实的推测；Skill 不成为 Consumer 项目事实 Authority。

### 3.5 Local discovery metadata / catalog

职责只包括：

- 帮助 Agent 判断“当前任务应继续读取哪些本地对象”；
- 表达足够的 scope / responsibility / condition / risk / consumer / source relation；
- 支持 primary responsibility 与 supporting context 的区分；
- 指向本地 semantic owner / Skill / Authority；
- 帮助检测 stale / missing / ambiguous activation。

它不得：

- 复制完整规范性规则正文；
- 自己成为更高优先级 Authority；
- 因 metadata 命中就绕过 Consumer Authority；
- 要求把所有仓库文件统一 metadata 化。

## 4. 最小成功运行路径

普通 Consumer Fresh Context 的目标路径为：

```text
Fresh Consumer Task
        ↓
Thin Consumer Bootstrap
        ↓
Consumer-local Discovery Entry
        ↓
根据 task / responsibility / conditions / risk
选择最小本地 metadata records / rule modules
        ↓
读取对应 Consumer-local semantic owner
        ↓
确定 primary responsibility / supporting context / current Authority
        ↓
如果只需 routing / Stage Return
        └─ 直接返回相应职责

如果真正进入稳定职责执行
        ↓
加载本地可用的对应 Skill
        ↓
读取当前任务真正需要的 Consumer Requirement / Architecture / Code / Evidence
        ↓
Execute / Verify / Stage Return
```

### 4.1 ordinary runtime 中不出现 upstream

正常路径中不得包含：

```text
→ 打开 dygapp/agentic-dev
→ 重新搜索 upstream Guide / Skill / Roadmap
→ 再决定本 Consumer 怎么工作
```

upstream 只在以下情况重新进入：

- 明确执行 baseline adoption / upgrade；
- Consumer-local Authority 明确声明当前必要方法 / Skill 缺失；
- 当前工作本身是 `agentic-dev` 实验 / 验证；
- Consumer Authority 明确要求重新解析 upstream。

### 4.2 Runtime 不假定固定文档体系

Consumer 可以拥有与 `jilinjobs-cms` 不同的目录和 Authority 组织方式。

因此正式能力只能要求：

- 本地 Authority 可识别；
- 本地发现入口可识别；
- semantic owner 可追溯；
- adopted capability provenance 可追溯；
- stale / conflict 可检测；

不得要求所有 Consumer 复制 `agentic-dev/docs/**` 或 `jilinjobs-cms/docs/**` 的物理目录。

## 5. Authority 与发现优先级

统一发现路径不等于统一 Authority 等级。

任何 activation 结果都必须先服从 Consumer 自己声明的 Repository Authority Hierarchy。

目标解析顺序为：

```text
Consumer Repository Authority
        ↓
Consumer-native current Authority
        ↓
Consumer-local adopted reusable rule / capability
        ↓
generic reusable default
```

这里只表达覆盖关系，不要求实现为一个全局数值 priority。

必须保留以下语义：

- Consumer Requirement / Specification 不会因为 reusable Skill 或 metadata 命中而被改写；
- Consumer Architecture / ADR 可以约束 reusable technical default；
- Consumer-local override 必须可发现；
- upstream 更新不能自动使本地 override 失效；
- metadata 只能帮助定位冲突，不能自行裁决超出当前 Authority 的事实。

## 6. Consumer-native 与 adopted reusable rule 的同路发现

v2 最终需要解决的不只是“找到 `technical-plan` Skill”。

同一个任务可能同时需要：

```text
Consumer-native Repository Rule
+ Consumer Architecture Rule
+ adopted reusable Engineering Rule
+ current Execution Authority
```

因此本地发现机制必须允许这些不同来源进入同一个候选选择过程，但保持来源身份。

示例目标行为：

```text
任务：修改共享数据 contract

local discovery
→ Consumer Architecture Authority      [project-native]
→ Consumer verification rule           [project-native]
→ technical-planning rule module       [adopted reusable]
→ technical-plan Skill                 [adopted reusable capability]
```

Agent 最终判断必须由这些来源的 Authority 关系共同约束，而不是由“哪个 metadata 匹配更多关键词”决定。

## 7. Baseline adoption / projection 目标

v2 后续必须定义一个可审计的 projection 生命周期，但 A1 只冻结它必须满足的语义。

### 7.1 输入

- 当前 Consumer Authority；
- 当前 Consumer 已记录的 exact upstream baseline；
- 候选新 upstream baseline；
- baseline 间 reusable Method / Guide / Skill / Contract 变化；
- Consumer 已存在的 local override / rejection / project-specific rules。

### 7.2 对每项候选变化分类

至少能表达：

- **adopt**：Consumer 需要该能力并形成 / 更新本地可发现资产；
- **retain / override**：Consumer 已有更具体规则，保留本地 Authority，同时记录与 upstream 的关系；
- **reject / not applicable**：当前 Consumer 不采用，不把无关规则带入 Runtime；
- **remove / supersede**：已采用本地资产因新的显式决定被取代时，必须清理旧激活关系，避免新旧同时有效。

### 7.3 输出

完成 adoption 后，普通 Runtime 所需内容必须全部可以从 Consumer Repository 或 Consumer 明确管理的本地 capability installation 中取得。

保留 upstream 信息的目的主要是：

- provenance；
- future baseline comparison；
- upgrade audit；
- 判断 local override / adopted copy 是否需要重新评估。

它不是普通 Runtime 的网络依赖。

## 8. Fail-closed 目标

当 discovery 不能安全给出最小正确集合时，回退对象必须仍然是 **Consumer 当前 Repository Authority**，而不是自动跳到 upstream。

至少覆盖：

### 8.1 Metadata / pointer stale

如果本地 discovery metadata 指向的 semantic owner 已变化、缺失或无法验证当前身份：

```text
停止信任该派生记录
→ 读取 Consumer-local Current Authority / Authority Map
→ 恢复或重建本地发现信息
```

### 8.2 Ambiguous responsibility

多个 responsibility 均可能适用时：

- 允许读取少量 supporting modules；
- 必须区分 primary responsibility；
- 不得把所有匹配项全部激活来规避判断；
- 无法安全区分时回到 Consumer-local Authority，而不是用关键词得分直接继续高影响操作。

### 8.3 Authority conflict

如果 Consumer-native rule 与 adopted reusable rule 表面冲突：

- 先按 Consumer Repository Authority 判断是否为合法 override；
- 如果无法确认本地规则身份、版本或适用范围，停止相关动作并恢复 Consumer Current Authority；
- 不自动在线查询新 upstream 来“覆盖”本地冲突。

### 8.4 High-impact boundary

产品意图、重大架构、安全 / 隐私、高影响难逆或授权边界不明确时，继续沿现行 Human Escalation 规则处理。Discovery 机制不能把高 metadata 置信度当作新的授权来源。

## 9. A1 可观察成功条件

后续实现或 Consumer 验证至少必须能够观察到：

1. Fresh Context 仅从 Consumer Repository 启动；
2. ordinary runtime 不读取 upstream；
3. Agent 能找到 Consumer-local discovery entry；
4. 对明确职责任务能选择最小适用 rule / module；
5. 对歧义任务能区分 primary 与 supporting responsibility；
6. Consumer-specific override 能覆盖更通用 adopted default；
7. Consumer-native Domain / Architecture / Verification Rule 可以被发现；
8. 只做 routing 时不机械加载 Skill；真正执行职责时能找到并加载所需 Skill；
9. stale / missing / conflict / ambiguity 能 fail-closed 到 Consumer 当前 Authority；
10. baseline upgrade 后 adopted / retained / overridden / rejected 结果在新的 Fresh Context 中仍可发现；
11. upstream 新提交不会自动改变 Consumer 普通 Runtime 行为；
12. 删除或重建纯 discovery metadata 不损失任何 Consumer 规范性事实。

## 10. 明确失败状态

出现以下任一结果，均表示后续方案不满足 A1 目标：

- Consumer 必须每次跨仓读取 `agentic-dev` 才能正确工作；
- 为实现发现而复制完整 upstream Method / Guide 树；
- Metadata / Catalog 成为规则正文的第二份维护位置；
- Consumer-native rule 无法与 adopted reusable rule 一起被发现；
- reusable Skill 或 upstream default 可以覆盖 Consumer Requirement / Architecture Authority；
- 所有任务默认加载全部 Skill 或全部 Guide module；
- stale metadata 仍被继续用于高影响判断；
- baseline upgrade 自动覆盖本地 override；
- 为了支持 discovery 要求 Consumer 重构为固定目录模板；
- 实验 token 指标改善，但真实 Consumer Fresh Context 仍不能独立恢复和正确执行。

## 11. A1 不冻结的设计

A1 故意不决定：

- metadata 最终字段名；
- JSON / YAML / Markdown Front Matter / generated catalog 的具体格式；
- Catalog 是否持久化或由本地 Authority 动态生成；
- Guide module 是否必须物理拆文件；
- Skill 使用复制、安装、vendor、plugin 还是其他分发方式；
- 是否需要自动生成器；
- 是否需要 Runtime Rule Index；
- metadata 是否覆盖所有可发现对象。

这些决定必须等待 Rule Ownership、A2 验收矩阵与 Consumer-local 生命周期需求进一步收敛。

## 12. A1 结论

当前真实 Consumer 已证明 **local Authority persistence 与 baseline adoption 基础可行**；v2 需要补的是一个低成本、非 Authority、可 fail-closed 的 Consumer-local discovery / activation layer。

后续设计应围绕以下目标链路继续：

```text
Thin Consumer Bootstrap
→ Local Discovery
→ Local Rule / Authority Selection
→ Responsibility / Stage Routing
→ Skill only when executing
→ Consumer Current Evidence
```

而不是：

```text
Consumer Task
→ reopen upstream agentic-dev
→ load broad Method / Guide stack
→ infer local rules again
```

A1 到此形成目标基线。下一步进入 A2：把上述目标转换为可独立判定的 Consumer-local 验收场景矩阵，再用该矩阵约束 Rule Ownership 与 metadata schema 设计。
