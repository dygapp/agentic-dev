# 规则治理与知识激活 v3 — GPT-6 独立评审

## 1. 性质与边界

本目录只服务 `agentic-dev` v3 的临时**治理 / 规划独立评审**。

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

评估输入只允许该 base 与本目录新增 / 更新的 review assets。

## 2. 当前评审目标

本轮**不再先评审具体 Manifest / Front Matter / Index 实现**。

评审顺序改为：

```text
Root Cause
→ Knowledge / Capability Ownership
→ Guide / Skill / Repository Standard boundary
→ Consumer lifecycle
→ V3-01～V3-08 analysis sequence
→ ADR gate
→ v1 / v2 preservation
→ 只有前述成立后，再评 metadata / discovery 是否被正确延后
```

核心候选判断见：

- `v3-governance-convergence-summary.md`：当前已经收敛的治理判断、未决边界和非目标；
- `v3-analysis-plan.md`：V3-01～V3-08 分阶段分析计划；
- `v3-candidate-review-package.md`：供独立 reviewer 挑战的候选模型；
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

脚本不会自动降级到其他模型。如果 `gpt-6-astra` 当前不可用，应停止并回传运行错误，不要用其他模型替代后仍把结果记为 GPT-6 Review。

本机需要：

- `git`
- `codex`
- `jq`
- `sort -V`

脚本还会检查 Codex CLI 版本是否不低于评估脚本当前要求。

## 4. 推荐：独立 detached worktree 执行

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
- 不要求本地 checkout 为命名分支，detached HEAD 是推荐模式。

## 5. 执行评审

只运行：

```bash
bash evals/rule-governance-v3/run-gpt6-review.sh
```

脚本会自动：

1. 检查 `origin/eval/rule-governance-v3-gpt6-review` 存在；
2. 检查当前 HEAD 精确等于远程 eval Head；
3. 检查 eval Head 继承 frozen base；
4. 检查相对 frozen base 只修改 `evals/rule-governance-v3/`；
5. 检查工作区干净；
6. 检查 Codex CLI 版本；
7. 以 `read-only` sandbox 启动新的 `codex exec`；
8. 显式请求 `gpt-6-astra` + `xhigh`；
9. 使用 `review-output-schema.json` 约束最终回答；
10. 保存完整 JSONL events、stderr、最终 JSON 与运行元数据；
11. 验证存在 `turn.completed`，且不存在 `turn.failed`；
12. 验证 PASS / REVISE 与 Blocking / Medium 数量没有自相矛盾；
13. 再次确认运行没有改变 Git HEAD 或 tracked / unignored working tree。

不要把进程退出码本身当作评审 PASS。

## 6. GPT-6 本轮应读什么

评审 prompt 已要求至少读取：

- 当前 `AGENTS.md` / README / Roadmap；
- Method / Principle / Skill Architecture / Skill Contracts；
- v1 / v2 Rule Governance 结果；
- 当前主要 Guide；
- Skill inventory 与代表性 `SKILL.md`；
- 本目录三份 v3 candidate / governance / planning 文档。

评审重点不是按文件名贴标签，而是判断实际 semantic owner。

## 7. 本轮明确不要求 GPT-6 决定

本轮不要求最终决定：

- Guide 最终拆成几个文件；
- 新增哪些 Skill；
- Repository Standard 最终目录；
- Front Matter 完整 schema；
- Resource Index 是否一定存在；
- Index 使用 YAML 还是 JSON；
- source identity 最终机制；
- Manifest / Catalog 的最终迁移方式；
- 最终 ADR 清单。

如果 GPT-6 把这些未决项当成本轮必须冻结的设计，应在评审结果中视为 over-design / scope drift，而不是自动采纳。

## 8. 等价手工命令

如果只为定位脚本问题，可以在同一隔离 worktree 中手工执行：

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

## 9. 运行后检查

脚本结尾应显示：

```text
[PASS] GPT-6 governance review run completed
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

`runtime-selection.txt` 为空不直接判失败；保留 `stderr.log`，回传后结合当前 Codex 输出格式交叉判断。

## 10. 回传结果

建议把完整 timestamped run 打包：

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
- `runtime-selection.txt`（若可取得）

## 11. 回传后的处理规则

GPT-6 Review 返回后：

```text
GPT-6 finding
→ 验证 Repository evidence
→ 当前模型二次裁决 Blocking / Medium / Low
→ 只吸收成立的最小治理 / planning 修正
→ 必要时重验
→ 再决定是否正式建立 v3 Milestone
```

禁止：

- 因 GPT-6 建议就自动扩大 v3；
- 把 optional implementation 直接升级成 Architecture；
- 未完成 V3-01 / V3-02 就实现 Index / generator；
- 未满足 Skill admission 就新增 Skill；
- 因评审 PASS 直接实施或合并；
- 在当前 eval branch 修改 Consumer Repository。

## 12. ADR 边界

当前不创建 ADR。

只有 V3-01 / V3-04 / V3-06 等专项分析形成具有长期架构后果、存在真实替代方案且需要保留选择理由的决定后，才按当前 Method / ADR 生命周期判断是否创建。

## 13. 清理

结果回传并确认不再需要本地 worktree 后：

```bash
cd /home/dyg/ai-projects/agentic-dev
git worktree remove ../agentic-dev-v3-gpt6-review
```

远程 eval branch 是否删除由后续人工决定；脚本不自动执行破坏性清理。
