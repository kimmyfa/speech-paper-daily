#!/bin/bash
# GitHub 推送封装：校验 remote token 有效、屏蔽 workflow 文件提交、简化推送。
# 用法: push_to_github.sh YYYY-MM-DD [commit_message]
set -euo pipefail

REPO="/Users/kimmy/Desktop/Vagent_app/SpeechAIResercher"
DATE="${1:-}"
[ -n "$DATE" ] || { echo "用法: push_to_github.sh YYYY-MM-DD [commit_message]"; exit 1; }
MSG="${2:-Daily Speech Papers Update - $DATE}"

cd "$REPO"

# 1. 校验 remote 与 token 有效性（避免 401/权限问题无法定位）
#    只允许 origin 内置 token，绝不使用 fetch_papers.py 中已失效的死 token
REMOTE_URL=$(git config --get remote.origin.url || true)
if [[ "$REMOTE_URL" != https://*@github.com/* ]]; then
  echo "[push] 警告: origin 不是带 token 的 https URL: $REMOTE_URL"
fi
if git ls-remote --exit-code origin HEAD >/dev/null 2>&1; then
  echo "[push] remote 校验通过"
else
  echo "[push] 错误: git ls-remote 失败，token 可能失效或网络异常" >&2
  exit 1
fi

# 2. 禁止提交 workflow 文件（当前 PAT 无 workflow scope，提交会整体拒推）
if git status --porcelain | grep -qE '\.git workflows/|\.github/workflows/'; then
  echo "[push] 检测到 .github/workflows 或 .github/workflows 变更，已停止（PAT 无 workflow 权限）" >&2
  exit 1
fi

git config user.name >/dev/null 2>&1 || git config user.name "Speech Paper Daily Bot"
git config user.email >/dev/null 2>&1 || git config user.email "speech-paper-daily@bot.local"

# 3. 只添加论文与知识库目录
git add "papers/$DATE/" knowledge_base/ 2>/dev/null || true

if git diff --cached --quiet; then
  echo "[push] 无新变更，跳过提交与推送"
  exit 0
fi

git commit -m "$MSG"
if git push origin main; then
  echo "[push] 推送成功"
else
  echo "[push] 推送失败" >&2
  exit 1
fi