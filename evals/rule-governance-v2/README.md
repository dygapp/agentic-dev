# 规则治理 v2 研究评估

本目录用于评估“规则治理与知识激活 v1”之后是否需要进入规则治理 v2，以及候选运行时激活方案是否值得进一步实验。

这些文件属于 `evals/` 评估资产，**不是 Repository Authority**。本分支不得修改正式 Method、Guide、Skill、Roadmap 或 Consumer Authority；任何 v2 结论都必须经过独立评估、证据比较和人工决策后，才能进入新的有限里程碑。

## 目标

当前研究重点不是继续证明 `rule-index` 能否检索规则，而是判断：

1. 规则发现 / 激活是否真正进入了需求分析、规格说明、技术设计、代码生成、调试与验证等生成阶段；
2. 大型 Guide 是否仍造成上下文膨胀、无关规则污染或关键规则激活过晚；
3. Skill 是否适合作为主要运行时激活单元；
4. Guide 拆分 + metadata / catalog 是否值得采用；
5. 现有 Guide 中哪些规则应通过“迁移而非复制”归入现有 Skill；
6. Consumer 将 Method / Rule / Skill 本地固化后，如何在不持续依赖 `agentic-dev` 的情况下保留等价激活能力；
7. 是否存在足够收益支持 v2，还是应继续保持 v1。

## 资产

- `evaluation-prompt.md`：GPT-6 Astra 与 GPT-5.6 Sol 使用的同一份独立架构评估命题；
- `rubric.md`：人工对照维度，不包含预设推荐答案；
- `scenarios/`：生成阶段基线场景，用于观察当前 v1 下不同模型实际读取与推理行为；
- `../run_rule_governance_v2_research.py`：隔离 Codex runner；
- `evals/results/rule-governance-v2/`：本地结果目录，已由仓库 `.gitignore` 中 `/evals/results/` 规则排除。

## 评估阶段

### Phase 1 — 独立架构评估

同一份 `evaluation-prompt.md` 分别交给 GPT-6 Astra 和 GPT-5.6 Sol。两个模型互不知道对方结论，不得先读取另一模型结果。

运行前：

```bash
codex --version
python3 evals/run_rule_governance_v2_research.py --validate-only
```

GPT-6 Astra：

```bash
python3 evals/run_rule_governance_v2_research.py \
  --run \
  --case architecture \
  --model gpt-6-astra \
  --reasoning-effort high
```

GPT-5.6 Sol：

```bash
python3 evals/run_rule_governance_v2_research.py \
  --run \
  --case architecture \
  --model gpt-5.6-sol \
  --reasoning-effort high
```

为保证公平性，两个模型应使用同一仓库提交、同一 prompt 和同一 reasoning effort。runner 会使用独立 `codex exec --ephemeral --json`、`read-only` sandbox、`approval_policy="never"` 和禁用 web search 的运行环境。

### Phase 2 — 当前 v1 生成阶段基线

该阶段不是 v1/v2 A/B，因为本分支不实现任何 v2 候选。它只记录当前 v1 在真实生成职责上的基线行为，供后续判断是否值得建立 v2 A/B。

运行 GPT-6 Astra 全部基线场景：

```bash
python3 evals/run_rule_governance_v2_research.py \
  --run \
  --case scenarios \
  --model gpt-6-astra \
  --reasoning-effort high
```

运行 GPT-5.6 Sol：

```bash
python3 evals/run_rule_governance_v2_research.py \
  --run \
  --case scenarios \
  --model gpt-5.6-sol \
  --reasoning-effort high
```

也可以定向运行单个场景：

```bash
python3 evals/run_rule_governance_v2_research.py \
  --run \
  --scenario 01-technical-design \
  --model gpt-5.6-sol \
  --reasoning-effort high
```

### Phase 3 — 汇总

两个模型完成后：

```bash
python3 evals/run_rule_governance_v2_research.py --report
```

生成：

```text
evals/results/rule-governance-v2/summary.md
```

该报告只汇总运行事实与模型最终输出，不自动判定哪个模型正确，也不把模型投票当成架构证据。

## 结果边界

每次运行至少保存：

- 原始 `codex exec --json` JSONL；
- 去除 provider / turn 事实 trace 后的 stderr；
- 请求模型与 reasoning effort；
- provider model / turn reasoning effort 可观察事实；
- wall-clock；
- 最终 Agent 文本（能够从 JSONL 可靠提取时）；
- 对应 prompt / scenario 身份。

进程退出码不是语义 PASS。模型结论也不是 Repository Authority。

## 人工比较

使用 `rubric.md` 对两份架构评估与生成阶段基线进行比较，重点查看：

- v1 已解决 / 部分解决 / 未解决的边界是否有 Repository Evidence 支持；
- 是否能指出生成阶段的真实激活缺口，而不是只讨论验证；
- 是否区分 Runtime Activation 与 Eval Verification；
- 是否保持 Consumer-local 解耦原则；
- 是否避免第二套 Authority；
- 是否控制 Skill 膨胀、Guide/Skill 重复和 metadata/catalog 漂移；
- 是否给出可逆、有限、可实验验证的 v2 路线；
- `GO / NO-GO / KEEP V1` 是否有充分证据。

## 进入 v2 实施前的门槛

本分支只做研究。只有当独立模型评估、当前 v1 生成阶段基线和人工复核共同支持“存在真实且足够大的 Runtime Activation 缺口”，才考虑建立新的有限 v2 Milestone。

即使进入 v2，也应先冻结一个最小候选并做真正 v1/v2 隔离 A/B，再决定是否修改正式 Guide / Skill / Method。