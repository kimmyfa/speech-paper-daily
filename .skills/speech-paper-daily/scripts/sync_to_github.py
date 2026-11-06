#!/usr/bin/env python3
"""把某一批次的速递与知识库提交到 GitHub。

用法：
    python3 .skills/speech-paper-daily/scripts/sync_to_github.py 2026-11-03
    python3 .skills/speech-paper-daily/scripts/sync_to_github.py 2026-11-03 --no-push
    python3 .skills/speech-paper-daily/scripts/sync_to_github.py 2026-11-03 --dry-run

退出码：0 = 已推送或无需推送；1 = 失败（调用方可据此判断）。
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def run(args, check=True):
    proc = subprocess.run(args, cwd=REPO, capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} 失败：\n{redact(proc.stderr or proc.stdout)}")
    return proc


def redact(text):
    return re.sub(r"(https?://)[^@\s/]+@", r"\1***@", text or "")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help="arXiv 批次日期，格式 YYYY-MM-DD")
    parser.add_argument("--no-push", action="store_true", help="只提交，不推送（本地验证用）")
    parser.add_argument("--dry-run", action="store_true", help="只检查将要提交什么，不做任何写操作")
    args = parser.parse_args(argv)

    if not DATE_RE.match(args.date):
        print(f"[sync] 日期格式错误: {args.date}（必须是 YYYY-MM-DD）", file=sys.stderr)
        return 1

    papers_dir = REPO / "papers" / args.date
    if not papers_dir.is_dir():
        print(f"[sync] 目录不存在: {papers_dir}", file=sys.stderr)
        return 1

    md_files = sorted(papers_dir.glob("*.md"))
    if not md_files:
        print(f"[sync] {papers_dir} 下没有 .md 文件", file=sys.stderr)
        return 1

    kb_dir = REPO / "knowledge_base"
    add_targets = [f"papers/{args.date}/"]
    if kb_dir.is_dir():
        add_targets.append("knowledge_base/")
    else:
        print("[sync] 警告: knowledge_base/ 不存在，本次只提交 papers/", file=sys.stderr)

    staged_before = run(["git", "diff", "--cached", "--name-only"]).stdout.strip()
    if staged_before:
        print("[sync] 错误: 暂存区已有其他改动，为避免误提交请先处理：", file=sys.stderr)
        print(staged_before, file=sys.stderr)
        return 1

    if args.dry_run:
        preview = run(["git", "add", "--dry-run", "--"] + add_targets).stdout.strip()
        if not preview:
            print(f"[sync] {args.date} 无变更需要提交")
        else:
            print("[sync] --dry-run，以下文件将被提交：")
            print(preview)
        return 0

    run(["git", "add", "--"] + add_targets)

    staged = run(["git", "diff", "--cached", "--name-only"]).stdout.strip()
    if staged:
        msg = f"Daily Speech Papers Update - {args.date}"
        run(["git", "commit", "-m", msg])
        print(f"[sync] 已提交: {msg}")
    else:
        print(f"[sync] {args.date} 无新增改动")

    if args.no_push:
        print("[sync] --no-push，跳过推送")
        return 0

    local_sha = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    remote = run(["git", "ls-remote", "origin", "refs/heads/main"]).stdout.strip()
    remote_sha = remote.split()[0] if remote else ""
    if local_sha == remote_sha:
        print(f"[sync] 已与远端一致，无需推送: {local_sha[:7]}")
        return 0

    run(["git", "pull", "--rebase", "--autostash", "origin", "main"])
    run(["git", "push", "origin", "main"])

    local_sha = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    remote = run(["git", "ls-remote", "origin", "refs/heads/main"]).stdout.strip()
    remote_sha = remote.split()[0] if remote else ""
    if local_sha != remote_sha:
        print(f"[sync] 推送后校验失败: local={local_sha} remote={remote_sha}", file=sys.stderr)
        return 1

    print(f"[sync] 同步成功: {args.date} @ {local_sha[:7]}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as exc:
        print(f"[sync] {exc}", file=sys.stderr)
        sys.exit(1)