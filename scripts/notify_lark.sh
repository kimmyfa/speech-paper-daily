#!/bin/bash
# 飞书通知封装：使用「SSE小组」群内应用发送每日论文速递通知。
# 用法: notify_lark.sh YYYY-MM-DD [--force]
# 说明: 必须使用 ~/.lark-cli 配置（应用 cli_aae2b74130789bd3，已在群内），
#       禁止使用 vagent runtime-home 默认配置（cli_aac993d952a3dbed，不在群内，报 230002）。
set -euo pipefail

DATE="${1:-}"
[ -n "$DATE" ] || { echo "用法: notify_lark.sh YYYY-MM-DD"; exit 1; }

LARK_CLI="$HOME/.config/vagent/runtime-home/lark-cli/darwin-arm64/lark-cli"
LARK_CONFIG_DIR="$HOME/.lark-cli"
CHAT_ID="oc_6167c48a3ad5662413abab93b359d183"
SENTINEL="$HOME/.vagent-speech/log/.notified_$(echo "$DATE" | tr -d '-')"
FORCE="${2:-}"
FORCE_BOOL=0
[ "$FORCE" = "--force" ] && FORCE_BOOL=1

# 幂等：已通知过则跳过（除非 --force）
if [ -f "$SENTINEL" ] && [ "$FORCE_BOOL" -ne 1 ]; then
  echo "[notify_lark] $DATE 已通知过（$SENTINEL 存在），跳过"
  exit 0
fi

[ -x "$LARK_CLI" ] || { echo "[notify_lark] 错误: lark-cli 不存在 $LARK_CLI"; exit 1; }
[ -f "$LARK_CONFIG_DIR/config.json" ] || { echo "[notify_lark] 错误: 配置缺失 $LARK_CONFIG_DIR/config.json"; exit 1; }

MSG=$(printf '📚 语音论文速递（%s）%s🔗 GitHub链接：https://github.com/kimmyfa/speech-paper-daily/tree/main/papers/%s' "$DATE" $'\n' "$DATE")

# 先确认身份（避免发到错误应用）
APPID=$(LARKSUITE_CLI_CONFIG_DIR="$LARK_CONFIG_DIR" "$LARK_CLI" config show 2>/dev/null | grep '"appId"' | head -1 | sed -E 's/.*"appId"[^"]*"([^"]+)".*/\1/' || true)
echo "[notify_lark] 使用应用: ${APPID:-unknown}（应为 cli_aae2b74130789bd3）"

if LARKSUITE_CLI_CONFIG_DIR="$LARK_CONFIG_DIR" "$LARK_CLI" im +messages-send \
   --chat-id "$CHAT_ID" --msg-type text --text "$MSG" --as bot; then
  mkdir -p "$HOME/.vagent-speech/log"
  touch "$SENTINEL"
  echo "[notify_lark] 通知发送成功，哨兵已写入 $SENTINEL"
else
  echo "[notify_lark] 通知发送失败" >&2
  exit 1
fi