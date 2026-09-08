#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 speech-paper-daily 输出构建语音论文知识库。"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / ".skills" / "speech-paper-daily" / "output"
KB_DIR = Path(__file__).resolve().parent
MIN_SCORE = 7.0

# 子方向标签：arXiv标题关键词 -> 子方向
SUBTAG_RULES = [
    (re.compile(r"\b(TTS|Text-to-?Speech|speech synthesis|dubbing|voice cloning|voice conversion)\b", re.I), "TTS"),
    (re.compile(r"\b(ASR|speech recognition|transcription|inverse text normalization|endpoint)\b", re.I), "ASR"),
    (re.compile(r"\b(codec|tokenizer|vector quantiz|vocoder|speech unit)\b", re.I), "Codec"),
    (re.compile(r"\b(Speech Language Model|SLM|audio language model|Audio LM|LLM|large audio)\b", re.I), "SpeechLM"),
    (re.compile(r"\b(speech enhancement|noise suppression|denois|dereverberat|super-resolution|band.?width extension)\b", re.I), "Enhancement"),
    (re.compile(r"\b(separation|source separation|speaker extraction|target speaker|diariz)\b", re.I), "Separation"),
    (re.compile(r"\b(voiceprint|speaker verification|speaker recognition|speaker identification|emotion|deepfake|spoof|watermark)\b", re.I), "Speaker/Verification"),
]

# 主方向文件映射
MAIN_DIRS = {
    "语音大模型": {
        "tts_speech_synthesis.md": "TTS",
        "asr_spoken_language.md": "ASR",
        "speech_lm_codec.md": "Codec",
        "speech_lm_understanding.md": "SpeechLM",
    },
    "语音前端": {
        "enhancement_frontend.md": "Enhancement",
        "separation_diarization.md": "Separation",
    },
}


def parse_output_files(output_dir: Path):
    """解析所有速递 md，返回 {arxiv_id: entry}，已去重且优先高评分。"""
    papers = {}
    for f in sorted(output_dir.glob("*/*.md")):
        content = f.read_text(encoding="utf-8", errors="ignore")
        for entry in re.split(r"\n## \[", content)[1:]:
            entry = "## [" + entry
            m = re.search(r"arXiv ID[^\n:：]*[:：]\s*([0-9]{4}\.[0-9]{4,5})", entry)
            if not m:
                continue
            aid = m.group(1)
            title = entry.split("\n", 1)[0].replace("## [", "").replace("]", "", 1).strip()
            score_m = re.search(r"评分[^\d]*([0-9]+(\.[0-9]+)?)/10", entry)
            score = float(score_m.group(1)) if score_m else 0.0
            dm = re.search(r"方向[^\n:：]*[:：]\s*([^\n|]*)\s*\|?\s*\*\*", entry)
            direction = dm.group(1).strip() if dm else ""
            date_m = re.search(r"发布日期[^\n:：]*[:：]\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", entry)
            code_m = re.search(r"\*\*代码\*\*：([^\n|]*)", entry)
            demo_m = re.search(r"\*\*Demo\*\*：([^\n|]*)", entry)
            intro_m = re.search(r"### 📌 简介\n+\s*(.+?)\n\n###", entry, re.DOTALL)
            tech_m = re.search(r"问题背景：\s*(.+?)(?=\n\n\*\*模型架构|\n\n\*\*核心创新)", entry, re.DOTALL)
            exp_m = re.search(r"### 📊 实验结果\n+\s*数据集[^\n:：]*[:：]\s*([^\n]+)", entry, re.DOTALL)

            new_entry = {
                "id": aid,
                "title": title,
                "score": score,
                "direction": direction.split("/")[0].strip(),
                "date": date_m.group(1) if date_m else "",
                "code": code_m.group(1).strip() if code_m else "暂无",
                "demo": demo_m.group(1).strip() if demo_m else "暂无",
                "contribution": re.sub(r"\s+", " ", intro_m.group(1)).strip()[:200] if intro_m else "",
                "tech_points": re.sub(r"\s+", " ", tech_m.group(1)).strip()[:300] if tech_m else "",
                "metrics": re.sub(r"\s+", " ", exp_m.group(1)).strip()[:150] if exp_m else "",
            }
            if aid not in papers or score >= papers[aid]["score"]:
                papers[aid] = new_entry
    return papers


def subtag(title: str, direction: str) -> str:
    """按标题关键词推断子方向标签。"""
    if direction in ("语音大模型", "语音前端"):
        for pat, tag in SUBTAG_RULES:
            if pat.search(title):
                return tag
    return "Other"


def pick_file(direction: str, tag: str) -> Path:
    """选择目标方向文件。"""
    for main, files in MAIN_DIRS.items():
        if direction == main:
            for fname, f_tag in files.items():
                if f_tag == tag:
                    return Path(__file__).parent / fname
    return Path(__file__).parent / "other_related.md"


def render_entry(e: dict) -> str:
    code = e["code"]
    if code.strip().lower() in ("暂无", "", "none"):
        code = "暂无"
    lines = [
        f"## [{e['title']}](https://arxiv.org/abs/{e['id']})",
        "",
        f"- **方向**：{e['direction']} | **子方向**：{subtag(e['title'], e['direction'])} | **评分**：{e['score']:.0f}/10 | **日期**：{e['date']}",
        f"- **一句话贡献**：{e['contribution']}",
        f"- **关键技术点**：{e['tech_points']}",
        f"- **主要指标**：{e['metrics']}",
        f"- **代码**：{code} | **Demo**：{e['demo']}",
        "",
    ]
    return "\n".join(lines)


ALL_FILES = [*MAIN_DIRS["语音大模型"], *MAIN_DIRS["语音前端"], "other_related.md"]
BUCKETS = {name: [] for name in ALL_FILES}


def incremental_update(papers: dict):
    """基于 .cache/<fname>.json 增量重写受影响方向文件。

    首次运行 .cache 不存在时为全量构建。每次运行后刷新对应缓存，
    使后续增量只需合并新论文即可，丢弃的条目（评分低于阈值不再出现）自然移除。
    """
    cache_dir = KB_DIR / ".cache"
    cache_dir.mkdir(exist_ok=True)
    new_papers = {k: v for k, v in papers.items() if v["score"] >= MIN_SCORE}
    for fname in ALL_FILES:
        cf = cache_dir / f"{fname}.json"
        cached = {}
        if cf.exists():
            cached = json.loads(cf.read_text(encoding="utf-8"))
        merged = dict(cached)
        for k, v in new_papers.items():
            if pick_file(v["direction"], subtag(v["title"], v["direction"])).name == fname:
                merged[k] = v
        ordered = sorted(merged.values(), key=lambda x: (-x["score"], x["date"]))
        parts = [f"# {fname.replace('.md', '').replace('_', ' ').upper()}（按评分降序）", "", f"共 {len(ordered)} 篇", ""]
        parts.extend(e for en in ordered for e in [render_entry(en), "---"])
        (KB_DIR / fname).write_text("\n".join(parts) + "\n", encoding="utf-8")
        cf.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    import datetime
    papers = parse_output_files(OUTPUT_DIR)
    incremental_update(papers)
    selected = {k: v for k, v in papers.items() if v["score"] >= MIN_SCORE}
    index = {
        "generated_at": datetime.date.today().isoformat(),
        "total_papers": len(selected),
        "min_score": MIN_SCORE,
        "by_file": {f: 0 for f in ALL_FILES},
    }
    for e in selected.values():
        fname = pick_file(e["direction"], subtag(e["title"], e["direction"])).name
        index["by_file"][fname] += 1
    (KB_DIR / "_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(index, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()