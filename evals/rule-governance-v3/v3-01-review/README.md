# V3-01 独立复核执行说明

本目录只用于对 PR #100 的 V3-01 知识与能力所有权模型候选做一次 Fresh Context、只读、定向一致性复核。

正式候选提交固定为：

`8504d1b2fcb5a834de75279f4ec7dfc81af70119`

评估分支：

`eval/rule-governance-v3-v3-01-review`

本目录中的 prompt / schema / runner 都是评估资产，不属于 PR #100，也不构成 v3 Authority。

## 运行

在原仓库更新远程引用：

```bash
cd ~/ai-projects/agentic-dev
git fetch origin
```

推荐使用独立 detached worktree：

```bash
EVAL_HEAD="$(git rev-parse origin/eval/rule-governance-v3-v3-01-review)"
git worktree add --detach ../agentic-dev-v3-01-review "$EVAL_HEAD"
cd ../agentic-dev-v3-01-review
```

确认当前 Head：

```bash
git status --short
git rev-parse HEAD
git rev-parse origin/eval/rule-governance-v3-v3-01-review
```

然后执行：

```bash
bash evals/rule-governance-v3/v3-01-review/run-gpt6-v3-01-review.sh
```

runner 使用：

- model：`gpt-6-astra`
- reasoning effort：`high`
- sandbox：`read-only`
- exact candidate：`8504d1b2fcb5a834de75279f4ec7dfc81af70119`

这里使用 `high` 而不是 `xhigh`，因为本次不是重新进行完整架构设计，而是针对已经过 GPT-6 治理评审与定向复评的 V3-01 候选做有限一致性验证，以降低不必要的额度消耗。

## 结果

结果目录：

`evals/results/rule-governance-v3-v3-01-review/<timestamp>/`

期望 Gate 输出：

```text
[PASS] GPT-6 V3-01 independent review completed
[PASS] verdict: PASS
[PASS] ready for V3-02 audit: true
[PASS] findings: Blocking=0 Medium=0 Low=<n>
```

`Low` 不自动阻止 V3-01 Gate，但仍需回到正式 PR 逐项判断是否值得修改。

如需上传最新结果，可直接打包：

```bash
tar -czf /tmp/v3-01-review.tar.gz "$(ls -dt evals/results/rule-governance-v3-v3-01-review/*/ | head -1)"
```

然后上传 `/tmp/v3-01-review.tar.gz`。
