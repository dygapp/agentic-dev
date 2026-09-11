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
- Consumer `docs/work/current/*` 仍保存 Planning 集成时的 PENDING / NOT GRANTED 状态，和 Issue #60 Current Evidence / PR #138 形成真实 current-state 冲突；这不是纯 locator 正常漂移；
- Consumer 当前声明的 5 个 Fresh Context 默认入口文件约 90,984 bytes，尚不含 current work / product authority / GitHub evidence；该数字是静态文件大小观察，不等同于 token 或每次实际读取量。

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
   - static Work PENDING / NOT GRANTED vs GitHub Current Evidence PASS / GRANTED；
   - 将其分类为 current-state/source-currentness conflict，而不是纯 current-locator；
   - ordinary upstream independence；
   - context-cost starting point。

3. **比较 exact upstream delta** — 完成
   - `d9fad0d... → 2fe1930...` = 34 ahead / 0 behind；
   - 明确 reusable 与 agentic-dev project-only 必须逐项分类。

4. **形成验证矩阵** — 完成候选
   - Track A pre-upgrade observation；
   - Track B baseline upgrade；
   - Track C post-adoption runtime / fail-closed；
   - Track D sustained-validity real evolution；
   - Track E first-adoption claim coverage。

5. **形成 Evidence Contract** — 完成候选
   - exact repo/base/head；
   - evaluated baseline；
   - current Authority inputs / conflicting current sources；
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

8. **首次采用覆盖策略** — 完成候选
   - 不破坏成熟 Existing Consumer 来伪造首次采用；
   - 优先逐 claim 评估历史 Evidence 是否可复用；
   - 无法证明时使用最小隔离 Consumer fixture；
   - Track E 在 V3-08 最终 closure 前必须关闭，不能长期 PENDING。

9. **风险 / AI 复核** — IN PROGRESS
   - `docs/README.md` 只是 Local Discovery Entry 强候选，不是预设物理答案；
   - Reviewed Discovery Map 只是强假设，必须由 Consumer local inventory 决定；
   - current-state conflict 必须 fail-closed / 对账，不建立“GitHub 永远高于 Work”通用规则；
   - V3-08 不得干扰 EU-54；
   - Evidence Contract 必须足以证明 sustained validity；
   - first-adoption coverage 必须有 claim-level reuse 或 fixture 闭环；
   - context metric 不得诱导为了 bytes/token 牺牲 correctness；
   - baseline upgrade finding 不得顺带吸收无边界 Consumer cleanup。

10. **Gate A closure** — PENDING
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
→ Track E 逐 claim Evidence reuse；不足则最小 fixture
→ Evidence 回流 Issue #115
→ agentic-dev classification / impact review
```

## 完成条件

本协调计划只在 V3-08 Gate A 设计收口时结束，不代表 V3-08 完成。

Gate A 完成条件：

- 验证对象、exact baselines、隔离方式、Tracks A～E、成功 / 失败判据、Evidence Contract、context-cost 口径全部明确；
- Current Work / GitHub Current Evidence 冲突进入显式 fail-closed / classification 场景；
- Consumer current active work 不被打断；
- Consumer 写实验具有明确 start condition；
- first-adoption 不通过破坏成熟 Consumer 伪造，并有 closure 前必须完成的 Evidence 路径；
- AI / 风险复核无未解决 Blocking / Medium；
- 未修改 Consumer Repository。

V3-08 最终 closure 仍必须满足 Issue #115 Gate B～D。