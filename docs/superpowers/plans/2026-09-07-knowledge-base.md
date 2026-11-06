# 语音论文知识库 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 从历史速递构建 `knowledge_base/`（按方向分 md + 索引），并配套 `knowledge-base` skill 供对话式检索与团队复用。

**Architecture:** `knowledge_base/build_kb.py` 用正则解析 `.skills/speech-paper-daily/output/*/*.md` 统一格式（已验证 250 篇全可解析），过滤 ≥7 分（估算 223 篇），按主方向归类到 6 个 md + other。`knowledge-base/SKILL.md` 描述检索方法。每日速递后追加调用。

**Tech Stack:** Python 3 stdlib（re/json/pathlib/glob），无第三方依赖。

**Spec:** `docs/superpowers/specs/2026-09-07-knowledge-base-design.md`

---

### Task 1: 创建知识库构建脚本 `build_kb.py`

**Files:**
- Create: `knowledge_base/build_kb.py`
- Test: `knowledge_base/test_build_kb.py`

- [ ] **Step 1: 写构建脚本核心逻辑**

```python
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
            dir_m = re.match(r"##\s*\[.*?\]\s*(.*)", entry.split("\n", 1)[0])
            direction = ""
            dm = re.search(r"方向[^\n:：]*[:：]\s*([^\n|]*)\s*\|?\s*\*\*", entry)
            if dm:
                direction = dm.group(1).strip()
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


def build(output_dir: Path, kb_dir: Path) -> dict:
    papers = parse_output_files(output_dir)
    selected = {k: v for k, v in papers.items() if v["score"] >= MIN_SCORE}
    buckets = {name: [] for name in MAIN_DIRS["语音大模型"]} | {
        name: [] for name in MAIN_DIRS["语音前端"]
    } | {"other_related.md": []}
    for e in selected.values():
        fname = pick_file(e["direction"], subtag(e["title"], e["direction"])).name
        buckets[fname].append(e)
    for fname, entries in buckets.items():
        ordered = sorted(entries, key=lambda x: (-x["score"], x["date"]))
        parts = [f"# {fname.replace('.md', '').replace('_', ' ').upper()}（按评分降序）", "", f"共 {len(ordered)} 篇", ""]
        parts.extend(e for en in ordered for e in [render_entry(en), "---"])
        (kb_dir / fname).write_text("\n".join(parts) + "\n", encoding="utf-8")
    index = {
        "generated_at": None,
        "total_papers": len(selected),
        "min_score": MIN_SCORE,
        "by_file": {k: len(v) for k, v in buckets.items()},
    }
    return index


def main():
    import datetime
    index = build(OUTPUT_DIR, KB_DIR)
    index["generated_at"] = datetime.date.today().isoformat()
    (KB_DIR / "_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(index, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 运行构建脚本验证输出**

Run: `cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher && python3 knowledge_base/build_kb.py`
Expected: 打印 index JSON，total_papers ≈ 223，且生成 7 个方向 md 文件

- [ ] **Step 3: 提交**

```bash
cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher
git add knowledge_base/
git commit -m "feat: add speech paper knowledge base builder"
```

---

### Task 2: 编写构建脚本单元测试

**Files:**
- Create: `knowledge_base/test_build_kb.py`

- [ ] **Step 1: 写测试**

```python
# -*- coding: utf-8 -*-
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from build_kb import build, parse_output_files, subtag, pick_file, MIN_SCORE

SAMPLE = """# 2026-09-01 语音论文速递

## 语音大模型

## [1] ExampleTTS: A Fast Text-to-Speech Model

**arXiv ID**：2609.00001 | **方向**：语音大模型

**作者**：A, B
**发布日期**：2026-09-01 | **论文**：https://arxiv.org/abs/2609.00001 | **PDF**：https://arxiv.org/pdf/2609.00001.pdf | **代码**：https://github.com/x/tts | **Demo**：暂无

### 📌 简介
本文提出ExampleTTS解决TTS速度问题，在LibriTTS上达到SOTA。

### 🔧 技术方案

**问题背景：** 现有TTS级联慢。

**模型架构：** Transformer。

**训练策略：** MSE。

### 📊 实验结果
**数据集**：LibriTTS
**主要指标**：
- WER：1.0
**是否开源**：开源

### ⭐ 评分：8/10
评分理由：good.

---

## [2] WeakModel

**arXiv ID**：2609.00002 | **方向**：语音前端

**作者**：C
**发布日期**：2026-09-01 | **论文**：https://arxiv.org/abs/2609.00002 | **PDF**：https://arxiv.org/pdf/2609.00002.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
弱方法。

### 🔧 技术方案

**问题背景：** x。

**模型架构：** y。

### 📊 实验结果
**数据集**：A
**主要指标**：
- m：1
**是否开源**：no

### ⭐ 评分：5/10
"""


def test_parse_output_files():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "2026-09-01" / "speech_paper_20260901.md"
        p.parent.mkdir(parents=True)
        p.write_text(SAMPLE, encoding="utf-8")
        papers = parse_output_files(Path(d))
        assert "2609.00001" in papers
        assert "2609.00002" in papers


def test_filter_score():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "2026-09-01" / "speech_paper_20260901.md"
        p.parent.mkdir(parents=True)
        p.write_text(SAMPLE, encoding="utf-8")
        papers = parse_output_files(Path(d))
        selected = {k: v for k, v in papers.items() if v["score"] >= MIN_SCORE}
        assert "2609.00001" in selected
        assert "2609.00002" not in selected


def test_subtag():
    assert subtag("ExampleTTS: A Fast Text-to-Speech Model", "语音大模型") == "TTS"
    assert subtag("Speech Enhancement via Denoising", "语音前端") == "Enhancement"
    assert subtag("Unknown Topic", "语音大模型") == "Other"


def test_pick_file():
    assert pick_file("语音大模型", "TTS").name == "tts_speech_synthesis.md"
    assert pick_file("语音前端", "Enhancement").name == "enhancement_frontend.md"
    assert pick_file("语音前端", "Separation").name == "separation_diarization.md"
    assert pick_file("语音大模型", "Other").name == "other_related.md"


def test_build_creates_files():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "2026-09-01" / "speech_paper_20260901.md"
        p.parent.mkdir(parents=True)
        p.write_text(SAMPLE, encoding="utf-8")
        out = Path(d)
        kb = Path(d) / "kb_out"
        kb.mkdir()
        index = build(out, kb)
        assert index["total_papers"] == 1
        tts_f = kb / "tts_speech_synthesis.md"
        assert tts_f.exists()
        content = tts_f.read_text(encoding="utf-8")
        assert "ExampleTTS" in content
        assert "https://github.com/x/tts" in content
```

- [ ] **Step 2: 运行测试**

Run: `cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher && python3 -m pytest knowledge_base/test_build_kb.py -v`
Expected: 5 个测试全部 PASS

- [ ] **Step 3: 提交**

```bash
cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher
git add knowledge_base/test_build_kb.py
git commit -m "test: add build_kb unit tests"
```

---

### Task 3: 创建知识库 README 与 `knowledge-base` skill

**Files:**
- Create: `knowledge_base/README.md`
- Create: `.skills/knowledge-base/SKILL.md`

- [ ] **Step 1: 写 `knowledge_base/README.md`**

```markdown
# 语音论文知识库

由 speech-paper-daily 每日速递自动构建，仅收录评分 ≥ 7 分的论文。

## 方向文件

| 文件 | 内容 |
|------|------|
| tts_speech_synthesis.md | TTS / 语音合成 / 配音 / 语音克隆 |
| asr_spoken_language.md | ASR / 识别 / 逆文本正则化 |
| speech_lm_codec.md | SpeechLM / Codec / Tokenizer / 声码器 |
| speech_lm_understanding.md | 音频语言模型理解 / 评测 / 安全 |
| enhancement_frontend.md | 增强 / 降噪 / 去混响 / 超分 |
| separation_diarization.md | 分离 / 说话人提取 / 日志 |
| other_related.md | 其他相关方向 |

## 构建与更新

- 一次性构建：`python3 knowledge_base/build_kb.py`
- 每日速递后自动追加（由 speech-paper-daily 流程调用）
- 全局索引：`knowledge_base/_index.json`
```

- [ ] **Step 2: 写 `.skills/knowledge-base/SKILL.md`**

```markdown
# Skill: knowledge-base

# 语音论文知识库检索

## 简介

本仓库内置语音论文知识库，收录 speech-paper-daily 每日速递中评分 ≥ 7 分的论文，按研究方向分文件组织。用户讨论算法方案时，使用本知识库检索并引用相关论文。

## 使用场景

用户提到算法方案、技术选型、指标对比、前沿方向时，主动检索知识库引用相关论文。

## 检索流程

1. 定位知识库目录 `knowledge_base/`（若在克隆仓库中运行）或让用户提供路径
2. 按讨论方向选择文件：
   - TTS/合成 → `tts_speech_synthesis.md`
   - ASR → `asr_spoken_language.md`
   - codec/tokenizer/SpeechLM → `speech_lm_codec.md`
   - 理解/评测/安全 → `speech_lm_understanding.md`
   - 增强/降噪/超分 → `enhancement_frontend.md`
   - 分离/说话人 → `separation_diarization.md`
3. 用 grep 在文件内按关键词筛选：
   ```bash
   grep -i -A 5 "可达|<关键词>" knowledge_base/<文件>.md
   ```
4. 按评分优先引用（条目本身按评分降序排列）
5. 引用时包含：一句话贡献、关键技术点、主要指标、代码链接

## 输出约束

- 引用中文表达，论文标题保留英文
- 至少给出 1-3 篇相关论文，按相关度/评分排序
- 若方向无匹配论文，明确说明知识库暂无覆盖
```

- [ ] **Step 3: 提交**

```bash
cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher
git add knowledge_base/README.md .skills/knowledge-base/SKILL.md
git commit -m "feat: add knowledge-base skill and README"
```

---

### Task 4: 集成每日自动追加（修改 speech-paper-daily skill）

**Files:**
- Modify: `.skills/speech-paper-daily/SKILL.md`
- Modify: `knowledge_base/build_kb.py`（新增追加模式）

- [ ] **Step 1: 在 `build_kb.py` 增加增量追加模式**

将 Task 1 的 `build()` 重命名为 `build()`（全量）并新增 `incremental_update()`。在 `main()` 前追加如下完整实现（替换 Task 1 中的 `build` 以支持缓存）：

```python
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
```

同时将 `main()` 改为全量+写索引：

```python
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
```

- [ ] **Step 2: 在 speech-paper-daily/SKILL.md 的 GitHub 同步步骤后追加知识库同步说明**

在 SKILL.md 中"第四步：同步到 GitHub"之后增加：

```markdown
### 第五步：同步语音论文知识库

生成速递后，更新知识库并随 GitHub 同步：

1. 运行 `python3 knowledge_base/build_kb.py`（每日增量模式会重建受影响方向文件）
2. 确认 `knowledge_base/_index.json` 已更新
3. 将 `knowledge_base/` 一并加入 git commit 与 push
```

- [ ] **Step 3: 手动验证（用今天 9/7 数据跑全量+增量）**

Run:
```bash
cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher
python3 knowledge_base/build_kb.py
python3 -m pytest knowledge_base/test_build_kb.py -v
```
Expected: 构建成功、测试通过、知识库已覆盖 9/7 的 22 篇

- [ ] **Step 4: 提交**

```bash
cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher
git add knowledge_base/ .skills/speech-paper-daily/SKILL.md
git commit -m "feat: sync knowledge base after daily digest"
```

---

### Task 5: 生成知识库并推送到 GitHub

- [ ] **Step 1: 删除旧缓存并全量重建**

Run:
```bash
cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher
rm -rf knowledge_base/.cache
python3 knowledge_base/build_kb.py
```
Expected: 生成 7 个方向 md（约 223 篇）+ `_index.json`

- [ ] **Step 2: 验证知识库内容**

Run:
```bash
cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher
grep -c "^## \[" knowledge_base/*.md
```
Expected: 各文件有合理论文数，总和 223

再抽查一篇：
```bash
grep -A 6 "ExampleTTS\|EntangleCodec" knowledge_base/speech_lm_codec.md | head -10
```

- [ ] **Step 3: 推送 GitHub**

```bash
cd /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher
git add knowledge_base/
git commit -m "feat: generate speech paper knowledge base (223 papers, score>=7)"
git push origin main
```

- [ ] **Step 4: 验证共享可拉取**

Run: `git log --oneline -3`
Expected: 最新提交为知识库生成提交，且远程已更新