# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import build_kb
from build_kb import (
    parse_output_files,
    subtag,
    pick_file,
    render_entry,
    incremental_update,
    MIN_SCORE,
)

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
- UTMOS：4.0

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


def _make_sample_tree(tmp_path):
    src = tmp_path / "out" / "2026-09-01"
    src.mkdir(parents=True)
    (src / "speech_paper_20260901.md").write_text(SAMPLE, encoding="utf-8")
    return tmp_path / "out"


def test_parse_output_files(tmp_path):
    out = _make_sample_tree(tmp_path)
    papers = parse_output_files(out)
    assert "2609.00001" in papers
    assert "2609.00002" in papers
    assert papers["2609.00001"]["title"] == "ExampleTTS: A Fast Text-to-Speech Model"
    assert papers["2609.00001"]["metrics"].strip().endswith("UTMOS：4.0")
    assert papers["2609.00001"]["metrics"] != ""


def test_filter_score(tmp_path):
    out = _make_sample_tree(tmp_path)
    papers = parse_output_files(out)
    selected = {k: v for k, v in papers.items() if v["score"] >= MIN_SCORE}
    assert list(selected.keys()) == ["2609.00001"]
    assert papers["2609.00002"]["score"] == 5.0


def test_subtag():
    assert subtag("ExampleTTS: A Fast Text-to-Speech Model", "语音大模型") == "TTS"
    assert subtag("Speech Enhancement via Denoising", "语音前端") == "Enhancement"
    assert subtag("Unknown Topic", "语音大模型") == "Other"
    assert subtag("Deepfake Audio Detection", "语音大模型") == "Speaker/Verification"


def test_pick_file():
    assert pick_file("语音大模型", "TTS").name == "tts_speech_synthesis.md"
    assert pick_file("语音大模型", "ASR").name == "asr_spoken_language.md"
    assert pick_file("语音大模型", "Codec").name == "speech_lm_codec.md"
    assert pick_file("语音大模型", "SpeechLM").name == "speech_lm_understanding.md"
    assert pick_file("语音前端", "Enhancement").name == "enhancement_frontend.md"
    assert pick_file("语音前端", "Separation").name == "separation_diarization.md"
    assert pick_file("语音大模型", "Other").name == "other_related.md"


def test_pick_file_cross_direction_fallback():
    assert pick_file("语音大模型", "Enhancement").name == "enhancement_frontend.md"
    assert pick_file("语音前端", "SpeechLM").name == "speech_lm_understanding.md"


def test_render_entry():
    e = {
        "id": "2609.00001",
        "title": "ExampleTTS",
        "score": 8.0,
        "direction": "语音大模型",
        "date": "2026-09-01",
        "code": "https://github.com/x/tts",
        "demo": "暂无",
        "contribution": "sample contribution",
        "tech_points": "sample tech points",
        "metrics": "WER 1.0",
    }
    out = render_entry(e)
    assert "https://arxiv.org/abs/2609.00001" in out
    assert "ExampleTTS" in out
    assert "**代码**：https://github.com/x/tts" in out


def test_incremental_update_creates_files(monkeypatch, tmp_path):
    kb_out = tmp_path / "kb"
    kb_out.mkdir()
    _make_sample_tree(tmp_path)
    monkeypatch.setattr(build_kb, "KB_DIR", kb_out)
    papers = build_kb.parse_output_files(tmp_path / "out")
    build_kb.incremental_update(papers)
    tts_f = kb_out / "tts_speech_synthesis.md"
    assert tts_f.exists()
    content = tts_f.read_text(encoding="utf-8")
    assert "ExampleTTS" in content
    assert "https://github.com/x/tts" in content
    for fname in build_kb.ALL_FILES:
        assert (kb_out / fname).exists()
    assert not (kb_out / "asr_spoken_language.md").read_text(encoding="utf-8").count(
        "## ["
    )