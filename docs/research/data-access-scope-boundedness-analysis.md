---
id: research:data-access-scope-boundedness
type: research
status: active
---

# 数据访问范围与有界控制研究

**研究日期：** 2026-09-03  
**性质：** 非规范性 Research

## 1. 研究问题

集合 / 列表 / 快照的数据访问不应从“要不要分页”开始，而应先判断真实 Consumer Scope、集合成员资格、增长性质和生命周期，再选择 filtering、ordering、window / pagination、representation 与 verification。

## 2. Consumer 证据

Issue #33 的实际案例支持以下结论：

- 全站固定 Top-N 后客户端按业务 scope 过滤可能产生正确性截断；
- 明确的 parent / 栏目 / tenant / 状态等消费 scope 应进入查询集合定义，而不是在取得全局窗口后补救式过滤；
- 稳定、有界、共享的站点结构可以使用完整快照，不应机械分页；
- 持续增长的业务集合需要有界读取与稳定 continuation 语义；
- Presentation N 不等于 Retrieval Scope N。

## 3. 外部证据

研究基线引用：

- Google AIP-132 / 158 / 160 / 157；
- Relay GraphQL Cursor Connections Specification；
- PostgreSQL `LIMIT / OFFSET` current documentation；
- Kubernetes API Concepts。

共同支持的边界：

- collection membership、filtering、pagination/window 与 representation 是不同责任；
- windowing 不能替代业务集合成员资格；
- pagination / Top-N 需要稳定 ordering / continuation；
- large / growing collection 与稳定 bounded snapshot 应使用不同策略；
- list/detail representation 可以因消费责任不同而分层，但不要求机械建立额外 DTO / projection。

## 4. 判断模型

设计或修改集合数据访问时按需判断：

1. Consumer Scope：当前真正消费哪个集合？
2. Boundedness：是否有真实、长期稳定上界？
3. Lifecycle / Freshness：数据属于 request、page、application snapshot 还是持续刷新集合？
4. Filter / Ordering Boundary：哪些条件决定集合成员资格，哪些只是 presentation？
5. Window Strategy：是否需要 page / cursor / chunk / top-N，是否有稳定 continuation？
6. Representation：list 与 detail 是否需要不同数据形状？
7. Verification Boundary：测试数据是否越过 page / Top-N / competing-scope 边界？

## 5. 明确非规则

本研究不支持以下绝对化结论：

- 所有接口必须分页；
- 所有 filter 都必须无条件先于所有 limit；
- 小型站点结构禁止完整读取；
- 所有列表都必须建立 Summary DTO；
- 为减少重复读取必须创建全局 cache / registry；
- 固定统一 page size。

## 6. V4 当前落点

该能力没有独立任务入口和稳定独立输出，不满足 Skill 判据。V4 已把规范语义收敛到：

`docs/rules/generation/data-access-boundedness.md`

本 Research 只保留证据来源、判断模型和非规则边界，不再描述旧 Engineering Discipline / Candidate / milestone 状态。

## 7. 结论

正确的数据访问设计顺序是先确定业务集合及其增长 / 生命周期性质，再决定 filtering、ordering、window / pagination、representation 与 verification。V4 Rule 是当前规范 owner；本文件只提供研究依据。