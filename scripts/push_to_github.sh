#!/bin/bash
# 兼容旧入口：参数透传给 sync_to_github.py
# 用法: push_to_github.sh YYYY-MM-DD [--no-push] [--dry-run]
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec python3 "$REPO/.skills/speech-paper-daily/scripts/sync_to_github.py" "$@"