---
id: eval:governance
type: eval-guide
status: active
---

# 项目治理定向评估

本目录保存 `agentic-dev` 仓库自身治理语义的隔离回归语料。治理评估不创建新的 Method / Skill / Rule / Architecture owner；只有映射到当前 Authority 的场景才可作为 current regression asset。

## 当前语料

### `chinese-human-facing-output.json`

验证自然中文默认，同时保留代码标识、路径、命令、API/CLI 参数、Git 引用与外部正式名称。current owner：

- `rule:human-facing-chinese-default`；
- `rule:exact-machine-identifiers`。

### `formal-concept-semantic-safety.json`

验证正式概念身份不能因中文化而合并不同对象类型。current owner：

- `rule:formal-concept-identity-safety`；
- 当前 Method / Architecture / Skill definitions。

### `method-object-semantic-safety.json`

验证 Technical Planning / Technical Plan、Converge / `converge`、Readiness Gate / `readiness-check`、Execute / `execute-unit` 等对象类型区分。

### `stacked-pr-integration-topology.json`

验证 GitHub squash / stacked / dependent PR 的当前状态恢复、Head / diff / checks currentness 与平台 preview 边界；不得推导统一分支策略或把平台 preview 细节提升为 Method contract。

### `github-agent-runtime-routing.json`

验证 `architecture:github-agent-runtime` 的关键行为回归：

- GitHub-native responsibility 默认进入 C；
- 已有适用 local runtime 时默认 A；
- Human Forced B 覆盖默认 A，但不覆盖 Repository governance；
- Forced B unavailable 时 fail closed，不静默降级；
- generic container 不等于 Cloud Repository Runtime；
- Consumer broken runtime locator 时不从 memory / upstream Guide 补定义；
- 跨 Repository responsibility 重新 Bootstrap。

该语料只提供隔离语义回归，不替代 Issue #160 Frozen Acceptance Contract 要求的真实 Local / Cloud / Remote / Consumer runtime evidence。

## 运行边界

每个场景必须：

- 独立 Fresh Runtime；
- 只复制场景声明的 current context；
- 不暴露 `expected_behavior` / `assertions` / 历史结果；
- 不让 Human Guide成为普通 runtime context，除非场景本身明确评估 Guide；
- 不因为治理语料存在就虚构 Skill、runtime 或 permission；
- 进程退出码不作为语义 PASS；
- 需要语义判断时逐项人工评分。

```bash
python3 evals/run_governance_evals.py
```

历史 PASS 不能自动支撑已发生语义变化的新 claim；current owner、context paths 或 expected behavior变化后必须重新取得对应 current evidence。
