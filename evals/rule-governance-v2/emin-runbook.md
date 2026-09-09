# 规则治理 v2 E-min 执行手册

本手册只用于临时评估分支 `eval/rule-governance-v2-research`。

考虑到 GPT-6 / GPT-5.6 High reasoning 的 Codex 限额成本，本轮采用**单模型先行 + 明确停止门禁**，避免再次一次性跑完整矩阵。

## 1. 更新本地评估分支

```bash
cd /home/dyg/ai-projects/agentic-dev

git fetch origin
git switch eval/rule-governance-v2-research
git pull --ff-only

git status
git rev-parse HEAD
```

运行前应保持工作区干净。`evals/results/` 已被 `.gitignore` 排除，现有 Pilot 结果可以继续留在本地。

## 2. 确认 A 组 Pilot 仍在

至少应存在：

```bash
test -f evals/results/rule-governance-v2/gpt-5.6-sol/01-technical-design/metadata.json
test -f evals/results/rule-governance-v2/gpt-5.6-sol/01-technical-design/run.jsonl
test -f evals/results/rule-governance-v2/gpt-5.6-sol/01-technical-design/final.md

test -f evals/results/rule-governance-v2/gpt-6-astra/01-technical-design/metadata.json
test -f evals/results/rule-governance-v2/gpt-6-astra/01-technical-design/run.jsonl
test -f evals/results/rule-governance-v2/gpt-6-astra/01-technical-design/final.md
```

如果某个 `test` 返回非 0，不要重跑 A；先恢复此前打包的 Pilot 结果到原目录。

## 3. 静态检查 E-min 资产

```bash
python3 evals/run_rule_governance_v2_emin.py --validate-only
```

预期包含：

```text
rule-governance-v2 E-min assets: OK
```

如果这里失败，不运行模型。

## 4. 第一门：只跑 GPT-5.6 Sol B 组

先运行成本相对较低的一侧：

```bash
python3 evals/run_rule_governance_v2_emin.py \
  --run \
  --model gpt-5.6-sol \
  --reasoning-effort high
```

默认结果目录：

```text
evals/results/rule-governance-v2/gpt-5.6-sol/01-technical-design-emin/
```

runner 默认拒绝覆盖已有 B 组结果，避免误操作重复消耗额度。正常情况下**不要使用 `--force`**。

## 5. 立即比较 GPT-5.6 A/B

```bash
python3 evals/compare_rule_governance_v2_emin.py \
  --model gpt-5.6-sol
```

查看：

```bash
cat evals/results/rule-governance-v2/emin-comparison.md
```

并人工对照：

```bash
less evals/results/rule-governance-v2/gpt-5.6-sol/01-technical-design/final.md
less evals/results/rule-governance-v2/gpt-5.6-sol/01-technical-design-emin/final.md
```

按 `emin-design.md` 第 5 节的 10 条语义检查逐项判断。

### GPT-5.6 停止门禁

出现任一情况，**停止，不运行 GPT-6 B 组**：

1. B 出现重大语义回归；
2. `runtime_comparable = false` 且无法简单归因于可修复的 Eval 事实采集问题；
3. `repository_command_output_bytes` 相对 A 下降不足 40%；
4. B 为完成任务仍无明确 fail-closed 原因地机械读取大量完整 Method / Guide / Contract；
5. B 的正确结果依赖评估激活 envelope 直接提供了规则正文，而不是现有 Skill / Authority。

这时已有证据足以说明当前 E-min 不值得继续消耗第二个模型额度，应先复核实验设计或回到其他候选方案。

## 6. 第二门：只有 GPT-5.6 通过后再跑 GPT-6 Astra

```bash
python3 evals/run_rule_governance_v2_emin.py \
  --run \
  --model gpt-6-astra \
  --reasoning-effort high
```

然后运行完整比较：

```bash
python3 evals/compare_rule_governance_v2_emin.py
```

查看：

```bash
cat evals/results/rule-governance-v2/emin-comparison.md
```

人工同时比较：

```bash
less evals/results/rule-governance-v2/gpt-6-astra/01-technical-design/final.md
less evals/results/rule-governance-v2/gpt-6-astra/01-technical-design-emin/final.md
```

## 7. 结果打包

不需要重新运行 architecture，也不需要重跑 A 组。

完整两模型 B 组完成后，或第一门提前停止时，都可以打包当前结果：

```bash
cd /home/dyg/ai-projects/agentic-dev

zip -r rule-governance-v2-emin-results.zip \
  evals/results/rule-governance-v2
```

上传 ZIP 进行人工语义评分与最终 E-min 判断。

## 8. 本轮禁止事项

- 不重跑 architecture；
- 不重跑 `01-technical-design` A 组；
- 不运行 02～05 其他 v1 场景；
- 不使用 `--force`，除非已经明确决定丢弃一次失败的本地 B 运行；
- 不因为单模型 token 下降就修改正式 Skill / Guide；
- 不在本轮实现 Runtime Index、metadata、Catalog 或 Consumer-local；
- 不把 E-min 结果直接解释为“规则治理 v2 可以实施”。
