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

## 检索

- 按方向选择对应 md 文件后用关键词 grep 检索
- 条目按评分降序排列
- 完整检索指引见 `.skills/knowledge-base/SKILL.md`