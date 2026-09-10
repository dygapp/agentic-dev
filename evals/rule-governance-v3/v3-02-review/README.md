# V3-02 定向独立复核

本目录用于对 PR #102 的 V3-02 ownership audit 做修订后的隔离定向复核。

正式候选：

```text
e7e952850d99d59ef75767ec5cff5b5b22262a89
```

上一轮针对 `5f4423000e3f459285e97087740db6f7eea2f4a3` 的独立复核发现 1 个 Medium：`consumer-local-rule-activation.md` §13 的现行采用验收要求被整体归为 Evidence，缺少明确当前 owner。该 finding 已按 Repository Evidence 接受并做最小候选修订。

本轮只定向验证：

- adoption acceptance 的 current owner 是否已经明确；
- V3-03 / V3-06 / V3-08 的责任分层是否避免第二 owner；
- v2 compatibility boundary 是否保持。

评估资产不是候选正确性证据。正式正文必须通过 `git show <candidate>:<path>` 从精确候选读取。

## 执行

先同步远端：

```bash
git fetch origin
```

推荐使用 detached worktree：

```bash
EVAL_HEAD="$(git rev-parse origin/eval/rule-governance-v3-v3-02-review)"
git worktree add --detach ../agentic-dev-v3-02-review "$EVAL_HEAD"
cd ../agentic-dev-v3-02-review
bash evals/rule-governance-v3/v3-02-review/run-gpt6-v3-02-review.sh
```

如果旧 worktree 已存在，可在其中执行：

```bash
git fetch origin
git checkout --detach origin/eval/rule-governance-v3-v3-02-review
bash evals/rule-governance-v3/v3-02-review/run-gpt6-v3-02-review.sh
```

Runner 请求 `gpt-6-astra` / `high`，要求 Codex CLI >= `0.153.0`，并以 read-only sandbox 执行。Codex JSONL 当前不独立证明真实 runtime model identity，因此运行元数据只记录 requested model / effort；stderr 选择信息仅作为诊断。

结果写入：

```text
evals/results/rule-governance-v3-v3-02-review/<UTC_TIMESTAMP>/
```

至少包含：

- `review-result.json`
- `run-metadata.json`
- `events.jsonl`
- `stderr.log`
- `runtime-selection-diagnostic.txt`（如存在）

## Gate

只有定向复核 `Blocking=0 && Medium=0`，且 Repository Evidence 裁决没有新阻塞项时，V3-02 才可以进入人工集成决策。

即使 PASS，也不授权自动合并 PR #102、关闭 Issue #101 或启动 V3-03。
