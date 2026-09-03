# Data Access Scope & Boundedness Control Research

**状态：** Research / Candidate / Architecture Fit Completed  
**研究日期：** 2026-09-03  
**性质：** 非规范性 Research；只有后续 Draft、Targeted Eval、AI Review 与 Integration 才能改变 Repository Authority。

## 1. 研究问题

本研究判断 Issue #33 已核验的 Data Access Scope / Boundedness / Lifecycle 证据是否足以形成新的通用工程能力，以及该能力应落在哪一层。

核心问题不是“要不要分页”，而是：

> 当 Agent 设计或修改集合 / 列表 / 快照的数据访问时，如何先确定真实消费作用域、集合增长性质与生命周期，再选择 filtering、window / pagination、ordering、representation 与 verification？

## 2. Consumer Evidence

主要入口：

- Issue #33 Final Summary：`https://github.com/dygapp/agentic-dev/issues/33#issuecomment-5527800060`
- 原始 Data Access Finding：`https://github.com/dygapp/agentic-dev/issues/33#issuecomment-5503850695`

最终核验确认以下真实实例成立：

1. **全站固定 Top-N → 客户端按栏目过滤会产生正确性截断。**
   - Consumer PR #39 将首页文章从全站固定窗口后客户端过滤改为按栏目查询；
   - 问题不是窗口大小“不够大”，而是查询集合没有先表达真实业务 scope。
2. **明确消费 scope 应进入服务端查询契约。**
   - Consumer PR #43 将 CmsList / Advertisement / Article Type 的明确消费 scope 下推到服务端；
   - 页面只需要某个业务集合时，不应把“全局列表 + 客户端筛选”当作默认接口形状。
3. **有界稳定站点结构可以使用完整快照。**
   - Consumer PR #44 对 Navigation / SiteConfig 保留完整快照；
   - 重点从“是否分页”转为“同一 Main App 生命周期是否重复装配”。
4. **持续增长的业务集合需要有界读取。**
   - Consumer PR #45 对 Admin Article 使用服务端过滤、分页与列表 Summary；
   - 最终集成 `698ad1d...` 的 main CI #413 成功。
5. **Presentation N 不等于 Retrieval Scope N。**
   - 页面最终显示少量条目不能证明数据源只应读取全局同样数量的条目；
   - 业务集合成员资格与最终展示数量是不同责任。

Issue #33 最终将该候选分类为：

> **Post-v1 Engineering Discipline / Implementation Guidance Research Candidate**

并明确它不是 Foundation v1 的 Blocking / Medium Finding。

## 3. 外部 Evidence

### 3.1 Google AIP — Collection Scope、Pagination 与 Filtering

来源：

- AIP-132 Standard methods: List — `https://google.aip.dev/132`
- AIP-158 Pagination — `https://google.aip.dev/158`
- AIP-160 Filtering — `https://google.aip.dev/160`
- AIP-157 Partial responses — `https://google.aip.dev/157`
- 访问日期：2026-09-03

关键事实：

- AIP-132 把 collection 的 `parent` 作为 List request 的一等字段，用于标识正在列举的资源集合；`page_size` / `page_token` 负责 pagination，`filter` / `order_by` 是独立的查询语义；
- AIP-158 指出 collection 可能任意大并持续增长，因此 collection API 应从一开始具备 pagination；
- AIP-160 把 filtering 定义为针对 collection 只返回用户感兴趣结果的查询能力，而不是客户端获得窗口后再补救式筛选；
- AIP-157 明确 List 可以使用 BASIC / partial representation，而 Get 可以选择 FULL，说明 list/detail representation 可以因消费责任不同而分层，而不是机械返回完全相同的数据形状。

支持的研究结论：

- Collection scope、filtering、pagination 和 representation 是不同职责；
- 页面条数或 page size 不应替代 collection membership / business scope；
- 对可能持续增长的 collection，应在 API 契约层考虑分页，而不是假设一次完整返回永远成立；
- 但 partial response / BASIC view 是条件能力，不意味着所有列表都必须建立独立 DTO 或投影。

### 3.2 Relay GraphQL Cursor Connections Specification — Filter Boundary Before Slice

来源：

- `https://relay.dev/graphql/connections.htm`
- 访问日期：2026-09-03

关键事实：

- Connection pagination 明确区分 cursor boundary 与 `first` / `last` slicing；
- 规范算法先 `ApplyCursorsToEdges`，再应用 `first`，再应用 `last`；
- page-to-page ordering 必须保持一致。

支持的研究结论：

- 当某个约束定义“哪些元素属于当前可分页集合”时，应先建立该集合边界，再进行 window / slice；
- pagination 需要稳定 ordering / continuation semantics；
- 但这不能被扩展成“所有业务 filter 永远必须在所有 limit 之前”的绝对规则：如果当前 Product Authority 明确定义的是全局 Top-N 后再派生展示，则全局窗口本身就是业务语义。

### 3.3 PostgreSQL Current Documentation — LIMIT 是结果集切片，不是业务 Scope

来源：

- PostgreSQL 18 / current `LIMIT and OFFSET`：`https://www.postgresql.org/docs/current/queries-limit.html`
- 访问日期：2026-09-03

关键事实：

- `LIMIT` / `OFFSET` 只取得“查询其余部分已经产生的 rows”的一部分；
- `LIMIT` 如果没有约束为唯一顺序的 `ORDER BY`，返回子集可能不可预测；
- 大 `OFFSET` 仍需要服务端计算被跳过的 rows，可能低效。

支持的研究结论：

- Windowing 不是集合成员资格的替代品；
- 需要分页 / Top-N 时必须同时检查 stable ordering；
- “已经有 LIMIT/OFFSET”不能单独证明数据访问策略正确或高效。

### 3.4 Kubernetes API — Large Collection、Chunking 与 Consistent Snapshot

来源：

- Kubernetes API Concepts：`https://kubernetes.io/docs/reference/using-api/api-concepts/`
- 访问日期：2026-09-03

关键事实：

- Kubernetes 明确指出大型 collection 全量返回可能产生很大的 server / client 成本；
- API 支持 `limit` + `continue` 把大型 collection 分块；
- continuation 可以维持相同 `resourceVersion`，从而形成跨 page 的 consistent snapshot；
- selector 与 limit 是不同的 collection restriction / chunking 机制。

支持的研究结论：

- collection size、growth、consistency 和 pagination 需要一起判断；
- pagination 不只是 UI 行为，也可能是服务端资源和一致性责任；
- 但该证据针对 large collections，不能反向证明所有小型稳定集合都必须分页。

## 4. 证据综合

Consumer Evidence 与外部 Evidence 在以下方向一致：

```text
Real Consumer / Business Scope
        ↓
Collection Membership
        ↓
Boundedness / Growth / Cardinality
        ↓
Freshness / Lifecycle / Consistency
        ↓
Filtering / Ordering
        ↓
Window / Pagination / Chunking
        ↓
List / Detail Representation
        ↓
Verification at Relevant Boundaries
```

这里的顺序表达**判断责任**，不是要求所有实现都必须经过一个固定 API pipeline。

## 5. Candidate Core Rule

候选核心规则：

> 设计或修改集合型数据访问时，应先确认当前消费者真正需要的数据作用域，以及集合是稳定有界、可能持续增长还是当前无法可靠界定；再根据 freshness、consistency 和应用生命周期选择过滤、排序、window / pagination、字段表示与复用方式。页面最终展示数量、现有 LIMIT/OFFSET 或客户端过滤不能替代业务作用域。若业务 scope 决定集合成员资格，应在 window / pagination 之前形成该 scope；只有当前权威明确把全局窗口 / ranking 本身定义为业务语义时才例外。规模稳定有界且语义上属于共享快照的数据可以完整读取并按当前生命周期复用，不应为了形式一致机械分页。

## 6. Candidate Judgment Model

实施前按需回答：

1. **Consumer Scope**：当前页面 / API / Job 真正消费哪个业务集合？是否存在 parent、tenant、栏目、状态、组织或其他明确 membership boundary？
2. **Boundedness**：集合是否有真实、可解释、长期稳定的上界？还是会随业务持续增长？
3. **Lifecycle / Freshness**：数据是 page-local、request-local、application snapshot，还是必须频繁刷新？同一生命周期是否重复获取同一稳定快照？
4. **Filter / Ordering Boundary**：当前 filter / sort 是业务 membership / ordering 语义，还是 presentation detail？window / pagination 前是否已经建立正确候选集合？
5. **Window Strategy**：是否需要 page / cursor / chunk / top-N？是否有 stable ordering / continuation 语义？
6. **Representation**：list 是否只需要 summary/basic fields？detail 是否需要 full representation？额外 projection 的复杂度是否由当前成本或契约支持？
7. **Verification Boundary**：测试数据是否真正超过 page / Top-N / scope 边界，并包含可能掩盖截断问题的 competing records？

## 7. 明确非规则

本 Candidate **不支持**：

- 所有接口必须分页；
- 所有列表必须 server-side pagination；
- 所有 filter 必须无条件在所有 limit 之前执行；
- 小型站点结构 / enum / config snapshot 禁止全量读取；
- 所有列表必须建立单独 Summary DTO；
- 为了避免重复请求必须创建全局 cache / registry；
- 固定某个 page size；
- 把性能优化当作没有规格 / 当前证据也必须实施的 Product Scope。

## 8. 与现有 Engineering Discipline 的边界

### Implementation Minimality

回答：

> 当前数据访问机制需要多少复杂度？

例如是否真的需要 cache、repository abstraction、cursor framework、额外 endpoint。

本 Candidate 回答：

> 当前消费者需要访问哪个集合，这个集合的增长 / 生命周期性质意味着怎样的数据边界？

二者可组合但不重复。

### Surgical Change

回答：

> 为修正当前数据访问问题，哪些实际 diff 属于当前逻辑变化？

本 Candidate 不决定 diff ownership，只决定正确的数据访问边界。

## 9. Architecture Fit Review

结论：**PASS — Engineering Discipline**。

理由：

1. 该判断跨 Vue、Spring、数据库、REST、GraphQL 和后台 Job 成立，不依赖单一技术栈，因此不是 Technology Profile；
2. 它影响 correctness、scalability、consistency 与 verification，不只是数据库性能技巧；
3. 它发生在实施阶段内部，不改变 Core Method lifecycle；
4. 它没有独立任务入口、稳定独立输出或单独调度价值，因此不满足 Task-oriented Skill 条件；
5. Verification 责任是该 Discipline 的一个组成部分，但不足以单独建立新的 Verification Profile；
6. `execute-unit` 可以以薄判断消费，不需要新的 Stage Return 或持久化 Artifact。

拟议正式名称：

> **Data Access Scope & Boundedness Control（数据访问作用域与有界性控制）**

架构形态：

> **Independent Engineering Discipline + thin `execute-unit` consumption**

当前没有证据要求修改 Core Method、Engineering Capability Architecture 或创建新 Skill。

## 10. Targeted Eval Design

建议新增：

- `B-EU-18`：global Top-N 后 client filter 的 scope truncation；
- `B-EU-19`：bounded stable site snapshot，拒绝机械 pagination；
- `B-EU-20`：unbounded operational collection 的 server filtering / pagination / summary；
- `B-EU-21`：presentation N 与 retrieval scope 分离；
- `B-EU-22`：Authority 明确 global ranking 时允许 window-first 语义；
- `B-EU-23`：验证数据必须越过 page / Top-N / competing-scope boundary；
- `B-EU-24`：pagination ordering / continuation stability；
- `B-EU-25`：bounded snapshot 仍需遵守 freshness / invalidation responsibility。

历史回归至少：

- `B-EU-01` — actual repository execution / evidence；
- `B-EU-06` — pagination acceptance evidence；
- `B-EU-09` — speculative complexity control；
- `B-EU-13` — diff scope control。

## 11. Research Conclusion

当前证据足以进入 Draft Engineering Discipline。

本 Research 不直接修改 Repository Authority；下一步应在同一有限里程碑内形成 Draft、Targeted Eval，并在 Fresh Runtime 通过后再决定 Integration。