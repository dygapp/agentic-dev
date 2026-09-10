# Metadata 歧义实验执行手册

本实验只验证 Guide decomposition + metadata discovery 在职责边界模糊时的选择鲁棒性，不重新运行 v1 baseline，也不修改正式 Method / Guide / Skill。

## 1. 固定分支

```bash
cd /home/dyg/ai-projects/agentic-dev
git fetch origin
git switch eval/rule-governance-v2-metadata-ambiguity
git pull --ff-only
git status
git rev-parse HEAD
```

运行模型前应保持 clean working tree，并记录当前 Head。

## 2. 静态检查

```bash
python3 evals/run_rule_governance_v2_metadata_ambiguity.py --validate-only
```

若失败，不运行模型。

## 3. 第一阶段：GPT-5.6

先只运行 GPT-5.6：

```bash
python3 evals/run_rule_governance_v2_metadata_ambiguity.py \
  --run \
  --model gpt-5.6-sol \
  --reasoning-effort high
```

结果目录：

```text
evals/results/rule-governance-v2/gpt-5.6-sol/06-metadata-ambiguity/
```

runner 默认拒绝覆盖已存在结果。普通执行不要使用 `--force`。

完成后：

```bash
python3 evals/summarize_rule_governance_v2_metadata_ambiguity.py \
  --model gpt-5.6-sol

cat evals/results/rule-governance-v2/metadata-ambiguity-summary.md
```

人工先按 `metadata-ambiguity-design.md` 复核。若 GPT-5.6 出现 primary responsibility 错误、继续 Execute、错误进入 systematic-debug、错误复用 stale Readiness 或明显过激活，则先停止，不支付 GPT-6 成本。

## 4. 第二阶段：GPT-6

只有 GPT-5.6 结果值得继续时再运行：

```bash
python3 evals/run_rule_governance_v2_metadata_ambiguity.py \
  --run \
  --model gpt-6-astra \
  --reasoning-effort high
```

随后生成双模型汇总：

```bash
python3 evals/summarize_rule_governance_v2_metadata_ambiguity.py \
  --model gpt-5.6-sol \
  --model gpt-6-astra
```

## 5. 打包结果

```bash
cd /home/dyg/ai-projects/agentic-dev
zip -r rule-governance-v2-metadata-ambiguity-results.zip \
  evals/results/rule-governance-v2
```

上传 `rule-governance-v2-metadata-ambiguity-results.zip` 进行人工语义复核。

## 6. 人工判定重点

不把进程成功或 token 降低视为语义 PASS。优先检查：

- `technical-plan` 是否成为 primary responsibility；
- `execution-context` / `slice-readiness` 是否只作为 supporting context；
- 当前 Unit 是否停止继续 Execute；
- 是否正确排除 systematic-debug；
- 历史 Readiness PASS 是否被判定为不能跨上游基础变化继续授权；
- 是否要求上游技术 / 架构基础解决后重新核对 Unit Set 并重新 readiness；
- 是否在 Consumer 事实不足时拒绝发明具体 contract 设计；
- metadata module 是否存在明显关键词式过激活；
- 是否无理由回退完整 Guide / Method / Contract。

双模型都通过后，本轮 Runtime Eval 停止，进入 Rule Governance v2 有限 Planning。