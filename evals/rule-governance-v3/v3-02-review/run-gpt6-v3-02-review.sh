#!/usr/bin/env bash
set -euo pipefail

CANDIDATE_HEAD="e7e952850d99d59ef75767ec5cff5b5b22262a89"
EXPECTED_REMOTE_REF="origin/eval/rule-governance-v3-v3-02-review"
MODEL="gpt-6-astra"
EFFORT="high"
MIN_CODEX_VERSION="0.153.0"

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

ASSET_DIR="$ROOT/evals/rule-governance-v3/v3-02-review"
PROMPT="$ASSET_DIR/gpt6-v3-02-review-prompt.md"
SCHEMA="$ASSET_DIR/v3-02-review-output-schema.json"
RESULT_ROOT="$ROOT/evals/results/rule-governance-v3-v3-02-review"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"
OUT="$RESULT_ROOT/$RUN_ID"

fail() {
  echo "[FAIL] $*" >&2
  exit 1
}

command -v git >/dev/null 2>&1 || fail "git not found"
command -v codex >/dev/null 2>&1 || fail "codex not found"
command -v jq >/dev/null 2>&1 || fail "jq not found"
command -v sort >/dev/null 2>&1 || fail "sort not found"
command -v sha256sum >/dev/null 2>&1 || fail "sha256sum not found"

git rev-parse --verify "$EXPECTED_REMOTE_REF" >/dev/null 2>&1 || \
  fail "missing remote eval ref '$EXPECTED_REMOTE_REF'; run git fetch origin first"

git cat-file -e "$CANDIDATE_HEAD^{commit}" 2>/dev/null || \
  fail "candidate head $CANDIDATE_HEAD is not available locally"

HEAD_BEFORE="$(git rev-parse HEAD)"
EXPECTED_HEAD="$(git rev-parse "$EXPECTED_REMOTE_REF")"
CURRENT_BRANCH="$(git branch --show-current)"
CHECKOUT_MODE="named-branch"
[[ -n "$CURRENT_BRANCH" ]] || CHECKOUT_MODE="detached"

[[ "$HEAD_BEFORE" == "$EXPECTED_HEAD" ]] || \
  fail "current HEAD $HEAD_BEFORE does not equal remote eval HEAD $EXPECTED_HEAD"

git merge-base --is-ancestor "$CANDIDATE_HEAD" HEAD || \
  fail "eval HEAD is not descended from candidate $CANDIDATE_HEAD"

UNEXPECTED_FILES="$(git diff --name-only "$CANDIDATE_HEAD"...HEAD | grep -v '^evals/rule-governance-v3/v3-02-review/' || true)"
[[ -z "$UNEXPECTED_FILES" ]] || {
  echo "$UNEXPECTED_FILES" >&2
  fail "eval ref contains changes outside the V3-02 review asset directory"
}

[[ -z "$(git status --porcelain --untracked-files=normal)" ]] || \
  fail "working tree is not clean before review"

[[ -f "$PROMPT" ]] || fail "missing prompt: $PROMPT"
[[ -f "$SCHEMA" ]] || fail "missing schema: $SCHEMA"

jq -e . "$SCHEMA" >/dev/null || fail "review output schema is not valid JSON"
jq -e 'all(.. | objects | select(has("const")); has("type"))' "$SCHEMA" >/dev/null || \
  fail "every schema node using const must also declare type"

CODEX_VERSION_RAW="$(codex --version)"
CODEX_VERSION="$(printf '%s\n' "$CODEX_VERSION_RAW" | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+' | head -n1 || true)"
[[ -n "$CODEX_VERSION" ]] || fail "cannot parse Codex version from: $CODEX_VERSION_RAW"

LOWEST="$(printf '%s\n%s\n' "$MIN_CODEX_VERSION" "$CODEX_VERSION" | sort -V | head -n1)"
[[ "$LOWEST" == "$MIN_CODEX_VERSION" ]] || \
  fail "GPT-6 Astra requires Codex CLI >= $MIN_CODEX_VERSION; current: $CODEX_VERSION"

PROMPT_SHA256="$(sha256sum "$PROMPT" | awk '{print $1}')"
SCHEMA_SHA256="$(sha256sum "$SCHEMA" | awk '{print $1}')"

mkdir -p "$OUT"
EVENTS="$OUT/events.jsonl"
STDERR_LOG="$OUT/stderr.log"
FINAL="$OUT/review-result.json"
META="$OUT/run-metadata.json"

STATUS_BEFORE="$(git status --porcelain --untracked-files=normal)"

jq -n \
  --arg repository "dygapp/agentic-dev" \
  --arg candidate_head "$CANDIDATE_HEAD" \
  --arg eval_ref "$EXPECTED_REMOTE_REF" \
  --arg eval_head "$HEAD_BEFORE" \
  --arg checkout_mode "$CHECKOUT_MODE" \
  --arg local_branch "$CURRENT_BRANCH" \
  --arg codex_version "$CODEX_VERSION" \
  --arg model_requested "$MODEL" \
  --arg reasoning_effort_requested "$EFFORT" \
  --arg prompt_sha256 "$PROMPT_SHA256" \
  --arg schema_sha256 "$SCHEMA_SHA256" \
  --arg started_at_utc "$RUN_ID" \
  '{
    repository: $repository,
    candidate_head: $candidate_head,
    eval_ref: $eval_ref,
    eval_head: $eval_head,
    checkout_mode: $checkout_mode,
    local_branch: $local_branch,
    codex_version: $codex_version,
    model_requested: $model_requested,
    reasoning_effort_requested: $reasoning_effort_requested,
    prompt_sha256: $prompt_sha256,
    schema_sha256: $schema_sha256,
    started_at_utc: $started_at_utc,
    runtime_model_identity_independently_verified: false
  }' > "$META"

echo "[INFO] repository:       dygapp/agentic-dev"
echo "[INFO] candidate:        $CANDIDATE_HEAD"
echo "[INFO] eval ref:         $EXPECTED_REMOTE_REF"
echo "[INFO] eval head:        $HEAD_BEFORE"
echo "[INFO] checkout:         $CHECKOUT_MODE${CURRENT_BRANCH:+ ($CURRENT_BRANCH)}"
echo "[INFO] codex:            $CODEX_VERSION_RAW"
echo "[INFO] requested model:  $MODEL"
echo "[INFO] requested effort: $EFFORT"
echo "[INFO] prompt sha256:    $PROMPT_SHA256"
echo "[INFO] schema sha256:    $SCHEMA_SHA256"
echo "[INFO] output:           $OUT"

set +e
codex exec \
  --cd "$ROOT" \
  --sandbox read-only \
  --json \
  --model "$MODEL" \
  --config "model_reasoning_effort=\"$EFFORT\"" \
  --output-schema "$SCHEMA" \
  --output-last-message "$FINAL" \
  - < "$PROMPT" \
  2> >(tee "$STDERR_LOG" >&2) | tee "$EVENTS"
PIPE_STATUSES=("${PIPESTATUS[@]}")
CODEX_EXIT="${PIPE_STATUSES[0]:-1}"
TEE_EXIT="${PIPE_STATUSES[1]:-1}"
set -e

[[ "$CODEX_EXIT" -eq 0 ]] || fail "codex exec failed with exit $CODEX_EXIT"
[[ "$TEE_EXIT" -eq 0 ]] || fail "tee failed with exit $TEE_EXIT"
[[ -s "$EVENTS" ]] || fail "events.jsonl is empty"
[[ -s "$FINAL" ]] || fail "review-result.json is empty"

jq -e . "$FINAL" >/dev/null || fail "final response is not valid JSON"
jq -e 'select(.type == "turn.completed")' "$EVENTS" >/dev/null || \
  fail "JSONL contains no turn.completed event"
if jq -e 'select(.type == "turn.failed")' "$EVENTS" >/dev/null; then
  fail "JSONL contains turn.failed"
fi

jq -e --arg expected "$CANDIDATE_HEAD" \
  '.review_target.repository == "dygapp/agentic-dev" and .review_target.candidate_head == $expected and .review_target.candidate_pr == 102' \
  "$FINAL" >/dev/null || fail "review result did not preserve exact candidate identity"

BLOCKING="$(jq '[.findings[] | select(.severity == "Blocking")] | length' "$FINAL")"
MEDIUM="$(jq '[.findings[] | select(.severity == "Medium")] | length' "$FINAL")"
LOW="$(jq '[.findings[] | select(.severity == "Low")] | length' "$FINAL")"

jq -e \
  --argjson blocking "$BLOCKING" \
  --argjson medium "$MEDIUM" \
  --argjson low "$LOW" \
  '.gate_assessment.blocking_count == $blocking and
   .gate_assessment.medium_count == $medium and
   .gate_assessment.low_count == $low' \
  "$FINAL" >/dev/null || fail "reported finding counts do not match findings array"

jq -e '
  .verdict as $v |
  ([.findings[] | select(.severity == "Blocking" or .severity == "Medium")] | length) as $major |
  if $v == "PASS" then
    ($major == 0 and .gate_assessment.v3_02_gate_ready == true and .gate_assessment.pr_ready_for_human_integration == true)
  elif $v == "REVISE" then
    ($major > 0 and .gate_assessment.v3_02_gate_ready == false and .gate_assessment.pr_ready_for_human_integration == false)
  elif $v == "REJECT" then
    (.gate_assessment.v3_02_gate_ready == false and .gate_assessment.pr_ready_for_human_integration == false)
  else false
  end
' "$FINAL" >/dev/null || fail "verdict/gate is inconsistent with Blocking/Medium findings"

HEAD_AFTER="$(git rev-parse HEAD)"
STATUS_AFTER="$(git status --porcelain --untracked-files=normal)"
[[ "$HEAD_AFTER" == "$HEAD_BEFORE" ]] || fail "repository HEAD changed during read-only review"
[[ "$STATUS_AFTER" == "$STATUS_BEFORE" ]] || fail "tracked/unignored working tree changed during read-only review"

# Codex JSONL currently does not provide an independently verifiable runtime-model identity.
# Keep any stderr selection lines only as diagnostics; authoritative metadata above records requested model/effort.
grep -E '^(model|reasoning effort):' "$STDERR_LOG" > "$OUT/runtime-selection-diagnostic.txt" || true
jq '. + {completed: true}' "$META" > "$META.tmp"
mv "$META.tmp" "$META"

echo
printf '[PASS] V3-02 independent review execution completed\n'
printf '[PASS] verdict: %s\n' "$(jq -r '.verdict' "$FINAL")"
printf '[PASS] V3-02 gate ready: %s\n' "$(jq -r '.gate_assessment.v3_02_gate_ready' "$FINAL")"
printf '[PASS] PR ready for human integration: %s\n' "$(jq -r '.gate_assessment.pr_ready_for_human_integration' "$FINAL")"
printf '[PASS] findings: Blocking=%s Medium=%s Low=%s\n' "$BLOCKING" "$MEDIUM" "$LOW"
printf '[PASS] result directory: %s\n' "$OUT"
