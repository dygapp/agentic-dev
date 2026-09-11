# V3-08 — Consumer 验证与持续有效性复核协调计划

**跟踪：** Issue #115  
**启动基线：** `master@2fe193035c629f6b8805fd473bd322f70fe6e172`  
**分支：** `docs/rule-governance-v3-v3-08-consumer-validation`

## 目标

在不干扰 `jilinjobs-cms` 当前 EU-54 Execute 生命周期的前提下，完成 V3-08 Gate A 验证设计，并把后续 Consumer 独立实验所需的 exact baseline、场景、Evidence Contract、写入边界和持续有效性路径固定下来。

## 当前事实

- V3-01～V3-07 已完成并集成；
- V3-07 集成提交：`2fe193035c629f6b8805fd473bd322f70fe6e172`；
- V3-08 Planning Authority：Issue #115；
- Primary Consumer：`dygapp/jilinjobs-cms`；
- Gate A 观察时 Consumer `main@989405a0006eafd52f361d391ebefe0d55c8014e`；
- Consumer current evaluated `agentic-dev` baseline：`d9fad0da83dbdb61cac5eb9778b0258c6861eef1`；
- V3-08 candidate baseline：`2fe193035c629f6b8805fd473bd322f70fe6e172`；
- exact upstream delta：34 commits ahead / 0 behind；
- Consumer 当前 active work：EU-54；Issue #60 已记录 Readiness PASS / Execute GRANTED；Draft PR #138 已存在；
- Consumer 静态 Current Work 仍保留 Planning 集成时的 PENDING 状态，构成真实 current-locator / Current Evidence 验证样本；
- Consumer 当前声明的 5 个 Fresh Context 默认入口文件约 90,984 bytes，尚不含 current work / product authority / GitHub evidence。

## Repository Boundary

### agentic-dev

允许：

- 读取 Consumer；
- 修改本仓库 V3-08 Planning / Evidence；
- 创建 V3-08 分支 / PR；
- 接收和分类 Consumer Evidence；
- 后续按证据修订 `agentic-dev`。

### jilinjobs-cms

当前会话只读。

禁止在本会话：

- 创建 Consumer branch / commit / PR；
- 修改 Consumer baseline / Method / discovery / product files；
- 触发 V3-08 Consumer runtime mutation；
- 合并 Consumer changes。

## Gate A 工作项

1. **恢复 Consumer 当前事实** — 完成
   - main / Authority / open Issue / PR；
   - current evaluated baseline；
   - Fresh Context / local method entry；
   - active EU-54 state。

2. **固定 pre-upgrade observation** — 完成
   - static Work PENDING vs GitHub PASS；
   - current-locator hypothesis；
   - ordinary upstream independence；
   - context-cost starting point。

3. **比较 exact upstream delta** — 完成
   - `d9fad0d... → 2fe1930...` = 34 ahead / 0 behind；
   - 明确 reusable 与 agentic-dev project-only 必须逐项分类。

4. **形成验证矩阵** — 完成候选
   - Track A pre-upgrade observation；
   - Track B baseline upgrade；
   - Track C post-adoption runtime / fail-closed；
   - Track D sustained-validity real evolution。

5. **形成 Evidence Contract** — 完成候选
   - exact repo/base/head；
   - evaluated baseline；
   - actual reads / primary / supporting；
   - currentness / coverage / fail-closed；
   - context cost；
   - finding classification。

6. **隔离 active Consumer work** — 完成候选
   - EU-54 closure 前只读；
   - baseline-upgrade branch 只能从 EU-54 closure 后届时 latest main 建立。

7. **确定 post-adoption real evolution** — 条件固定
   - 当前首选 Issue #137 Page Content Architecture；
   - 若届时真实路线改变，使用第一个真实后续工作并记录替代原因。

8. **风险 / AI 复核** — PENDING
   - 是否把 `docs/README.md` 过早指定为最终 Local Discovery Entry；
   - 是否把 Map 强假设误写成必选；
   - 是否让 V3-08 干扰 EU-54；
   - Evidence Contract 是否足以证明 sustained validity；
   - first-adoption coverage 是否需要独立 fixture；
   - context metric 是否诱导错误优化。

9. **Gate A closure** — PENDING
   - Blocking / Medium = 0；
   - Issue #115 记录 Gate A Evidence；
   - 形成 Consumer handoff；
   - 不启动 Consumer 写实验。

## Consumer runtime 后续顺序

```text
Gate A PASS
→ Consumer 独立会话重新恢复 latest main
→ 若 EU-54 未 closure：仅 Track A read-only
→ 若 EU-54 已 closure 且无 conflicting Execute work：
   建立 isolated baseline-upgrade experiment branch
→ Track B exact baseline upgrade / per-item adoption
→ adoption verification
→ Track C ordinary runtime / drift / fail-closed
→ Consumer 是否集成 baseline upgrade，由 Consumer Authority 决定
→ 若已成为 Consumer current：Track D 真实后续项目演进
→ Evidence 回流 Issue #115
→ agentic-dev classification / impact review
```

## 完成条件

本协调计划只在 V3-08 Gate A 设计收口时结束，不代表 V3-08 完成。

Gate A 完成条件：

- 验证对象、exact baselines、隔离方式、场景、成功 / 失败判据、Evidence Contract、context-cost 口径全部明确；
- Consumer current active work 不被打断；
- Consumer 写实验具有明确 start condition；
- first-adoption 不通过破坏成熟 Consumer 伪造；
- AI / 风险复核无未解决 Blocking / Medium；
- 未修改 Consumer Repository。

V3-08 最终 closure 仍必须满足 Issue #115 Gate B～D。