#!/bin/bash
# 删除本批次精读派生的子代理会话（仅限本会话 task 工具返回的 task_id）
# 护栏：只删除 parent_id 非空（即派生子会话）、且属本项目的 ses_ 会话；执行会话与人工对话（parent 为空）不受任何影响
# 用法: prune_sessions.sh ses_xxx [ses_yyy ...]
DB="$HOME/.config/vagent/runtime-home/.vagent/data/vagent.db"
IDS=()
for a in "$@"; do
  [[ "$a" == ses_* ]] && IDS+=("'$a'")
done
if [ ${#IDS[@]} -eq 0 ]; then
  echo "[prune_sessions] 无有效会话ID，跳过"
  exit 0
fi
LIST=$(printf "%s," "${IDS[@]}")
LIST=${LIST%,}
DEL=$(sqlite3 "$DB" "SELECT count(*) FROM session WHERE directory LIKE '%SpeechAIResercher%' AND parent_id IS NOT NULL AND id IN ($LIST);")
sqlite3 "$DB" "PRAGMA foreign_keys=ON; DELETE FROM session WHERE directory LIKE '%SpeechAIResercher%' AND parent_id IS NOT NULL AND id IN ($LIST);"
echo "[prune_sessions] 请求 ${#IDS[@]} 个ID，实际清理子代理会话 $DEL 个（非派生子会话一律拒绝）"
