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

# 子方向标签：arXiv标题关键词 -> 子方向（按顺序优先匹配）
SUBTAG_RULES = [
    # 合成 / 克隆 / 说话人转换
    (re.compile(r"\b(TTS|Text-to-?Speech|text-to-?voice|speech synthes|dubbing|voice cloning|voice conversion|speech conversion)\b", re.I), "TTS"),
    # 语音/音频生成与编辑
    (re.compile(r"\b(speech|voice|audio) (generation|editing|design|designer|synthesis)\b|\b(TTS|dubbing|duplex|dialogue) (synthesis|generation)\b|\b(audio.?visual|avatar|scene|singing|voice.?singing) (generation|synthesis)\b|\b(synthetic|spoken) (speech|dialogue|dialog|voice)\b", re.I), "TTS"),
    # ASR / VAD / 端点检测 / 关键词
    (re.compile(r"\b(ASR|speech recognition|transcription|inverse text normalization|endpoint|voice activity|VAD|turn.?aware|turn.?based|turn.?taking|turn action|keyword spot\w*)\b", re.I), "ASR"),
    # Codec / Tokenizer / 声码器
    (re.compile(r"\b(codec\w*|tokeniz\w*|speech.?token\w*|audio.?encoder\w*|speech cod\w*|vector quantiz\w*|vocoder\w*|speech.?unit\w*|waveform\w*)\b", re.I), "Codec"),
    # 语音大模型相关术语
    (re.compile(r"(\bSpeech Language Model\w*|\bLarge Language Model\w*|\bslm\b|\bLLMs?\b|\bLALMs?\b|\bAudio LM\b|\baudio lms?\b|\blarge audio\b|audio.?language|audio.?understand|audio.?comprehension|audio.?grounded|audio.?representation|audio.?learn)", re.I), "SpeechLM"),
    # 理解 / 评测 / 安全 / 说话人身份之外的大模型主题
    (re.compile(r"\b(caption\w*|benchmark\w*|challenge\w*|retrieval|reasoning|ground(ed|ing|s)?|paralinguistic|sentiment|privacy|safety|voice agent\w*|speech agent\w*|duplex|conversational|summar\w*|assessment|understanding)\b", re.I), "SpeechLM"),
    # MOS / 音质评估
    (re.compile(r"\b(MOS|mean opinion|quality assessment|listening test|speech quality)\b", re.I), "SpeechLM"),
    # 前端增强 / 降噪 / 波束 / 空间处理
    (re.compile(r"\b(speech enhancement|audio enhancement|noise suppression|noise control|noise cancellation|active noise|acoustic echo|echo cancel|super-?resolution)\b|\bband.?width|\bdereverberat|\bdenois|\benhanc|\brestorat|\bbeamform|\bdirection.?of.?arrival|\bambisonic", re.I), "Enhancement"),
    # 分离 / 说话人提取
    (re.compile(r"\bseparat|\bspeaker extraction|\btarget speaker|\btarget sound|\bdiariz", re.I), "Separation"),
    # 说话人识别 / 认证 / 伪造检测
    (re.compile(r"\bvoiceprint|\bspeaker verif|\bspeaker recogni|\bspeaker identif|\bspeaker represent|\bemotion|\bdeepfake|\bspoof|\bwatermark|\bmanipulat|\bdeceiv|\bevasion|\bimpersonat|\banti-spoof", re.I), "Speaker/Verification"),
    # Whisper 类模型归入 ASR
    (re.compile(r"\bwhisper", re.I), "ASR"),
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
            title_line = entry.split("\n", 1)[0]
            tm = re.match(r"^##\s*\[\d+\]\s*(.+)$", title_line)
            title = tm.group(1).strip() if tm else title_line.replace("## [", "").replace("]", "", 1).strip()
            score_m = re.search(r"评分[^\d]*([0-9]+(\.[0-9]+)?)/10", entry)
            score = float(score_m.group(1)) if score_m else 0.0
            dm = re.search(r"方向[^\n:：]*[:：]\s*([^\n|]*)\s*\|?\s*\*\*", entry)
            direction = dm.group(1).strip() if dm else ""
            date_m = re.search(r"发布日期[^\n:：]*[:：]\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", entry)
            code_m = re.search(r"\*\*代码\*\*：([^\n|]*)", entry)
            demo_m = re.search(r"\*\*Demo\*\*：([^\n|]*)", entry)
            intro_m = re.search(r"### 📌 简介\n+\s*(.+?)\n\n###", entry, re.DOTALL)
            tech_m = re.search(r"\*\*问题背景：\*\*\s*(.+?)(?=\n\n\*\*模型架构|\n\n\*\*核心创新)", entry, re.DOTALL)
            exp_m = re.search(r"\*\*主要指标\*\*\s*[:：]\s*(.*?)(?=\n\*\*是否开源|\Z)", entry, re.DOTALL)

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


# 需要路径映射的跨主方向子标签集合
UNDERSTANDING_TAGS = ("SpeechLM", "Speaker/Verification")


def normalize_direction(direction: str, title: str = "") -> str:
    """把编辑侧方向标签归一化为 语音大模型 / 语音前端。"""
    d = direction or ""
    if "语音大模型" in d:
        return "语音大模型"
    if "语音前端" in d:
        return "语音前端"
    if title and re.search(r"\b(separat|speaker extraction|target speaker|enhanc|denois|dereverberat|diariz|band.?width)\b", title, re.I):
        return "语音前端"
    return "语音大模型"


def subtag(title: str, direction: str) -> str:
    """按标题关键词推断子方向标签。"""
    # direction retained for API compatibility; classification is title-driven
    for pat, tag in SUBTAG_RULES:
        if pat.search(title):
            return tag
    return "Other"


def pick_file(direction: str, tag: str, title: str = "") -> Path:
    """选择目标方向文件。"""
    main = normalize_direction(direction, title)
    for fname, f_tag in MAIN_DIRS[main].items():
        if f_tag == tag:
            return Path(__file__).parent / fname
    for other in (m for m in MAIN_DIRS if m != main):
        for fname, f_tag in MAIN_DIRS[other].items():
            if f_tag == tag:
                return Path(__file__).parent / fname
    if tag in UNDERSTANDING_TAGS:
        return Path(__file__).parent / "speech_lm_understanding.md"
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


def incremental_update(papers: dict):
    """基于全量语料重写各方向文件。

    解析输出会返回完整语料，因此每次构建都以 new_papers 为准重排各文件，
    缓存文件仅作为历史记录保留（不再作为合并依据），
    评分低于阈值的条目自然移除。
    """
    cache_dir = KB_DIR / ".cache"
    cache_dir.mkdir(exist_ok=True)
    new_papers = {k: v for k, v in papers.items() if v["score"] >= MIN_SCORE}
    for fname in ALL_FILES:
        merged = {
            k: v
            for k, v in new_papers.items()
            if pick_file(v["direction"], subtag(v["title"], v["direction"]), v["title"]).name == fname
        }
        ordered = sorted(merged.values(), key=lambda x: (-x["score"], x["date"]))
        parts = [f"# {fname.replace('.md', '').replace('_', ' ').upper()}（按评分降序）", "", f"共 {len(ordered)} 篇", ""]
        parts.extend(e for en in ordered for e in [render_entry(en), "---"])
        (KB_DIR / fname).write_text("\n".join(parts) + "\n", encoding="utf-8")
        cf = cache_dir / f"{fname}.json"
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
        fname = pick_file(e["direction"], subtag(e["title"], e["direction"]), e["title"]).name
        index["by_file"][fname] += 1
    (KB_DIR / "_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(index, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()