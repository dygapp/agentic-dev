---
id: eval:governance
type: eval-guide
status: active
---

# 项目治理定向评估

本目录保存 `agentic-dev` 仓库自身治理语义的隔离回归语料。治理评估不创建新的 Method / Skill / Rule owner；只有映射到当前 Authority 的场景才作为 current regression asset。

## 当前语料

### `chinese-human-facing-output.json`

验证面向人的内容规则：

- 普通动作、判断、因果和结论默认使用自然中文；
- 精确机器标识、外部正式名称与稳定状态值可以保持原样；
- `PASS`、`PENDING`、`BLOCKED` 等状态值不为了“纯中文”建立第二套翻译状态；
- 旧会话、旧交接材料或英文密集输入不能覆盖当前 Repository Authority。

当前规范 owner：`rule:human-facing-content-integrity`。

### `formal-concept-semantic-safety.json`

验证语言收敛不会合并当前能力模型中的不同正式对象，重点覆盖仓库权威 / 人工权威、Method / Skill / Rule / Guide，以及中文表达、精确 identity 与 canonical owner 的边界。

当前规范来源是 Repository Authority、当前 Capability / Skill Architecture 与 `rule:human-facing-content-integrity`。

### `method-object-semantic-safety.json`

验证当前 AI Development Method 中容易发生词面碰撞的对象仍保持身份区分：

- 技术规划阶段 / 技术计划产物；
- 整体收敛阶段 / `converge`；
- 就绪门禁 / `readiness-check`；
- 执行阶段 / `execute-unit`。

这些场景读取 current Method / Skill owners，不再引用已经删除的旧 terminology Guide、Skill Contracts 聚合文件或退出当前架构的 Technology Profile / Verification Profile。

### `stacked-pr-integration-topology.json`

GitHub squash / stacked / dependent PR 的平台拓扑研究仍可作为专项回归依据；场景不得推导统一分支策略或把平台 preview 细节提升为 Method contract。

## 运行边界

每个场景必须：

- 独立 Fresh Runtime；
- 只复制场景声明的 current context；
- 不暴露 `expected_behavior` / `assertions` / 历史结果；
- 不因为治理语料存在就虚构 Skill；
- 进程退出码不作为语义 `PASS`；
- 需要语义判断时逐项人工评分。

```bash
python3 evals/run_governance_evals.py
```

Skill、Rule、Method 或 Bootstrap contract 发生实质变化后，受影响场景必须重新取得 current evidence；历史 `PASS` 不自动证明当前行为。
