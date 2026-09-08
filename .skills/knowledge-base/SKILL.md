# Skill: knowledge-base

# 语音论文知识库检索

## 简介

本项目内置语音论文知识库，收录 speech-paper-daily 每日速递中评分 ≥ 7 分的论文，按研究方向分文件组织。用户讨论算法方案时，使用本知识库检索并引用相关论文。

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
   - 其他/多主题或方向不明确 → 先查 `other_related.md`，再在全部 md 中搜索
3. 用 grep 在文件内按关键词筛选（扩展正则，多文件搜索）：
   ```bash
   grep -niE "关键词1|关键词2" knowledge_base/<文件>.md
   ```
   方向不明确时跨多个文件搜索；标题行（`## [`）命中通常是最强匹配。
4. 按评分优先引用（条目本身按评分降序排列）
5. 引用时包含：一句话贡献、关键技术点、主要指标、代码链接。仅当在全部 7 个 md 文件中都无匹配时才说明暂无覆盖。

## 输出约束

- 引用中文表达，论文标题保留英文
- 至少给出 1-3 篇相关论文，按相关度/评分排序
- 若方向无匹配论文，明确说明知识库暂无覆盖