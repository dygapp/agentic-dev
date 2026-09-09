# Guide + Metadata G-min 执行手册

本轮只运行 `01-technical-design` 的 G-min C 组。A 组与 E-min B 组全部复用既有结果，不重跑。

## 1. 更新实验分支

```bash
cd /home/dyg/ai-projects/agentic-dev
git fetch origin
git switch eval/rule-governance-v2-guide-metadata
git pull --ff-only
git status
git rev-parse HEAD
```

工作区应保持 clean。

## 2. 保留既有 A / E-min 结果

本地应继续存在：

```text
evals/results/rule-governance-v2/<model>/01-technical-design/
evals/results/rule-governance-v2/<model>/01-technical-design-emin/
```

不要删除或重跑这些目录。

## 3. 静态检查

```bash
python3 evals/run_rule_governance_v2_guide_metadata.py --validate-only
```

只有输出 `rule-governance-v2 Guide + Metadata assets: OK` 后才进入真实运行。

## 4. 先跑 GPT-5.6

```bash
python3 evals/run_rule_governance_v2_guide_metadata.py \
  --run \
  --model gpt-5.6-sol \
  --reasoning-effort high
```

结果目录：

```text
evals/results/rule-governance-v2/gpt-5.6-sol/01-technical-design-guide-metadata/
```

runner 默认拒绝覆盖已存在结果，避免重复消耗额度。正常情况下不要加 `--force`。

## 5. 三组比较

```bash
python3 evals/compare_rule_governance_v2_guide_metadata.py \
  --model gpt-5.6-sol
```

查看：

```bash
cat evals/results/rule-governance-v2/guide-metadata-comparison.md
```

重点检查：

- C 相对 A 的 Repository output 是否下降至少 40%；
- C 与 E-min 的主指标收益差；
- C 是否自行选中 `technical-planning` 模块；
- 是否继续读取完整大型 Guide / Method / Contract；
- 是否发生 fail-closed；
- 最终输出是否保持 10 条技术规划语义。

## 6. GPT-5.6 通过后再考虑 GPT-6

如果 GPT-5.6 出现重大语义回归，或主指标未达到 40%，先停止，不消耗 GPT-6。

如果 GPT-5.6 通过，再运行：

```bash
python3 evals/run_rule_governance_v2_guide_metadata.py \
  --run \
  --model gpt-6-astra \
  --reasoning-effort high
```

然后生成双模型对比：

```bash
python3 evals/compare_rule_governance_v2_guide_metadata.py \
  --model gpt-5.6-sol \
  --model gpt-6-astra
```

## 7. 打包

```bash
zip -r rule-governance-v2-guide-metadata-results.zip \
  evals/results/rule-governance-v2
```

上传 ZIP 后进行人工语义评分和最终 A / E-min / G-min 解释。

## 8. 判定边界

`SUPPORTS G-min` 需要：

- 关键语义无重大回归；
- runtime facts 可比较；
- 相对 A 的 Repository output 至少下降 40%；
- Agent 没有从 prompt 得到预解析 responsibility；
- 能通过 metadata 自行找到技术规划模块与必要后续来源。

如果 G-min 明显弱于 E-min 但仍优于 A，优先解释为“metadata 适合作为 Skill-first 的补充发现层”，而不是直接否定 metadata。
