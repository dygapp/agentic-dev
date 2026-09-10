# 规则治理与知识激活 v3 — GPT-6 独立评审

## 1. 性质与边界

本目录只服务 `agentic-dev` v3 候选方案的临时独立评审。

它不：

- 修改 `master` 的正式 Roadmap / Method / Architecture / Guide / Skill；
- 创建正式 v3 Milestone；
- 把 GPT-6 输出自动提升为 Repository Authority；
- 自动实施任何评审建议；
- 自动创建 PR / Issue / Merge。

Frozen base：

`agentic-dev@3c31ae96683c4a653f001402b889b40e87df976b`

评估分支：

`eval/rule-governance-v3-gpt6-review`

评估输入只允许该 base 与本目录新增的 review assets。

## 2. 文件

- `v3-candidate-review-package.md`：v3 Candidate Design；
- `gpt6-review-prompt.md`：独立评审提示；
- `review-output-schema.json`：结构化输出契约；
- `run-gpt6-review.sh`：只读 Fresh Context 执行与结果完整性检查。

生成结果进入：

`evals/results/rule-governance-v3-gpt6-review/<UTC timestamp>/`

该目录已由根 `.gitignore` 排除，不进入评估分支提交。

## 3. 运行前提

本评估目标模型固定为：

- model：`gpt-6-astra`
- reasoning effort：`xhigh`

创建本评估时，OpenAI 当前说明要求 GPT-6 Astra 使用 Codex CLI `0.153.0` 或更高版本；模型访问仍可能受账号 / rollout 影响。

脚本不会自动降级到其他模型。如果 `gpt-6-astra` 当前不可用，应停止并回传运行错误，不要用 GPT-5.x 替代后仍把结果记为 GPT-6 Review。

本机还需要：

- `git`
- `codex`
- `jq`
- GNU/BSD `sort` 支持 `-V`

## 4. 推荐：独立 worktree 执行

不要切换当前正在使用的 `agentic-dev` 工作目录。

在原仓库执行：

```bash
cd /home/dyg/ai-projects/agentic-dev
git fetch origin

EVAL_HEAD="$(git rev-parse origin/eval/rule-governance-v3-gpt6-review)"

git worktree add --detach \
  ../agentic-dev-v3-gpt6-review \
  "$EVAL_HEAD"

cd ../agentic-dev-v3-gpt6-review
```

确认：

```bash
git status --short
git rev-parse HEAD
git rev-parse origin/eval/rule-governance-v3-gpt6-review
codex --version
```

要求：

- `git status --short` 为空；
- 当前 `HEAD` 与远程 eval branch 精确一致；
- Codex CLI >= `0.153.0`。

## 5. 执行评审

只运行：

```bash
bash evals/rule-governance-v3/run-gpt6-review.sh
```

脚本会自动：

1. 检查当前 HEAD 精确等于远程 eval branch；
2. 检查 eval branch 相对 frozen base 只修改 `evals/rule-governance-v3/`；
3. 检查工作区干净；
4. 检查 Codex CLI 版本；
5. 以 `read-only` sandbox 启动新的 `codex exec`；
6. 显式请求 `gpt-6-astra` + `xhigh`；
7. 使用 `review-output-schema.json` 约束最终回答；
8. 保存完整 JSONL events、stderr、最终 JSON 与运行元数据；
9. 验证存在 `turn.completed`，且不存在 `turn.failed`；
10. 验证 PASS / REVISE 与 Blocking / Medium 数量没有自相矛盾；
11. 再次确认运行没有改变 Git HEAD 或 tracked working tree。

不要把进程退出码本身当作评审 PASS。

## 6. 等价手工命令

如果需要定位脚本问题，可以在同一隔离 worktree 中手工执行：

```bash
mkdir -p evals/results/rule-governance-v3-gpt6-review/manual

codex exec \
  --cd "$PWD" \
  --sandbox read-only \
  --json \
  --model gpt-6-astra \
  --config 'model_reasoning_effort="xhigh"' \
  --output-schema evals/rule-governance-v3/review-output-schema.json \
  --output-last-message evals/results/rule-governance-v3-gpt6-review/manual/review-result.json \
  - < evals/rule-governance-v3/gpt6-review-prompt.md \
  2> >(tee evals/results/rule-governance-v3-gpt6-review/manual/stderr.log >&2) \
  | tee evals/results/rule-governance-v3-gpt6-review/manual/events.jsonl
```

手工命令只用于诊断；正式回传优先使用脚本生成的 timestamped run。

## 7. 运行后检查

脚本结尾应显示：

```text
[PASS] GPT-6 review run completed
[PASS] verdict: <PASS|REVISE|REJECT>
[PASS] findings: Blocking=<n> Medium=<n> Low=<n>
```

然后查看：

```bash
LATEST="$(find evals/results/rule-governance-v3-gpt6-review \
  -mindepth 1 -maxdepth 1 -type d | sort | tail -n1)"

echo "$LATEST"
cat "$LATEST/run-metadata.json"
jq . "$LATEST/review-result.json"
cat "$LATEST/runtime-selection.txt" || true
```

如果 `runtime-selection.txt` 为空，不直接判失败；保留 `stderr.log`，回传后结合 Codex 当前输出格式判断。模型请求值已经记录在 `run-metadata.json` 中，但“请求了某模型”与“运行时确实使用该模型”仍应尽量通过 runtime output 交叉核验。

## 8. 回传结果

建议把完整 timestamped run 打包，而不是只复制模型最终回答：

```bash
LATEST="$(find evals/results/rule-governance-v3-gpt6-review \
  -mindepth 1 -maxdepth 1 -type d | sort | tail -n1)"

ARCHIVE="/tmp/rule-governance-v3-gpt6-review-$(basename "$LATEST").tar.gz"
tar -czf "$ARCHIVE" -C "$(dirname "$LATEST")" "$(basename "$LATEST")"
echo "$ARCHIVE"
```

回传 archive 应至少包含：

- `review-result.json`
- `events.jsonl`
- `stderr.log`
- `run-metadata.json`
- `runtime-selection.txt`（如果 Runtime header 可取得）

## 9. 回传后的处理规则

GPT-6 Review 返回后，`agentic-dev` 再进行人工 / 当前模型二次裁决：

```text
GPT-6 finding
→ 验证其 Repository evidence
→ 分类 Blocking / Medium / Low 是否成立
→ 只吸收成立的最小修正
→ 再决定是否正式建立 v3 Milestone
```

禁止：

- 因 GPT-6 提出建议就自动扩大 v3；
- 把 optional alternative 直接变成 Architecture；
- 未验证 evidence 就修改正式 Method / Skill；
- 在评估分支直接实施 v3；
- 因评审 PASS 就跳过正式 Milestone / Authority / Integration Gate。

## 10. 清理

结果已回传并确认不再需要本地 worktree 后，可在原仓库执行：

```bash
cd /home/dyg/ai-projects/agentic-dev
git worktree remove ../agentic-dev-v3-gpt6-review
```

远程 eval branch 是否删除由后续人工决定；本评估脚本不自动删除任何分支。
