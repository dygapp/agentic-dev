---
id: eval-guide:governance
type: eval-guide
status: active
---

# 项目治理定向评估

本目录保存 `agentic-dev` 仓库自身治理语义的隔离回归语料。治理评估不创建新的 Method / Skill / Rule owner；只有映射到当前 Authority 的场景才可作为 V4 regression asset。

## 当前语料与 V4 迁移状态

### `chinese-human-facing-output.json`

目标仍有效：验证自然中文默认，同时保留代码标识、路径、命令、API/CLI 参数、Git 引用与外部正式名称。V4 current owner：

- `rule:human-facing-chinese-default`；
- `rule:exact-machine-identifiers`。

V4-06 前需把 `context_paths` 从旧 terminology Guide 切到 current Rules。

### `formal-concept-semantic-safety.json`

“保持正式概念身份、不因中文化合并不同对象类型”的风险仍有效。V4 current owner：

- `rule:formal-concept-identity-safety`；
- 当前 Method / Architecture / Skill definitions。

旧 Technology Profile / Verification Profile 等已退出 current architecture 的对象不能继续作为 V4 current concept expectation；场景需要按 V4 实际资源模型重写。

### `method-object-semantic-safety.json`

Technical Planning / Technical Plan、Converge / `converge`、Readiness Gate / `readiness-check`、Execute / `execute-unit` 的对象类型区分仍有效，但必须读取 V4 current Method / Skill architecture，而不是已删除的 Skill Contract 聚合文档。

### `stacked-pr-integration-topology.json`

GitHub squash / stacked / dependent PR 的平台拓扑研究仍可作为专项回归依据；V4 通用 owner 是 external-operation / review-change + currentness / integration closure Rules。该场景不得推导统一分支策略或把平台 preview 细节提升为 Method contract。

## 运行边界

每个场景必须：

- 独立 Fresh Runtime；
- 只复制场景声明的 current context；
- 不暴露 `expected_behavior` / `assertions` / 历史结果；
- 不因为治理语料存在就虚构 Skill；
- 进程退出码不作为语义 PASS；
- 需要语义判断时逐项人工评分。

```bash
python3 evals/run_governance_evals.py
```

V4-06 必须先完成语料与 `context_paths` migration，再重新取得 current evidence；历史 PASS 不能替代该步骤。