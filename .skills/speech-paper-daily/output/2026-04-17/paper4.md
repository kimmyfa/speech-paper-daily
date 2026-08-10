## 🤖 语音大模型

## [4] Towards Fine-grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt

**arXiv ID**: 2604.13715
**方向**: 语音大模型
**作者**: Yanfeng Shi, Pengfei Cai, Jun Liu, Qing Gu, Nan Jiang, Lirong Dai, Ian McLoughlin, Yan Song
**机构**: University of Science and Technology of China, Singapore Institute of Technology
**发布日期**: 2026-04-15
**论文链接**: https://arxiv.org/abs/2604.13715
**PDF 链接**: https://arxiv.org/pdf/2604.13715.pdf
**代码链接**: 暂无
**Demo 链接**: 暂无

### 📌 简介
本文提出TimePro-RL框架，增强大型音频语言模型(LALMs)的细粒度时间感知能力。通过Audio-Side Time Prompt将时间戳编码为嵌入并穿插在音频特征序列中作为时间坐标，随后引入强化学习后训练直接优化时间对齐性能。该方法在Audio Grounding、Sound Event Detection、Dense Audio Captioning等任务上取得显著提升。

### 🔧 技术方案

**模型架构**：基于Qwen2-Audio/Qwen2.5-Omni，扩展tokenizer添加750个Timestamp Tokens（0-30s，stride=0.04s），Timestamp Embedding采用语义先验初始化（对应数字字符串的subword embeddings平均）

**核心创新**：
1. Audio-Side Time Prompt (ASTP)：将时间戳嵌入穿插在音频特征序列中，提供显式时间坐标提示
2. 语义初始化策略：Timestamp Embedding初始化为对应数字字符串的subword embeddings平均，利用预训练知识
3. 自适应时间奖励机制：结合Event-based F1 (r_main)和mIoU/METEOR (r_aux)，根据方差阈值动态调整奖励

**训练策略**：
- SFT: 3 epochs, lr=1e-5, LoRA (r=8, α=32)
- RL: GRPO, 1 epoch, lr=1e-6, group size=4, subset=10,200 samples
- 基于Eb-F1的自适应时间奖励，方差阈值ϵ=1e-6

### 📊 实验结果
**数据集**：FTAR (Audio Grounding)、DESED (Sound Event Detection)、FTAR (Dense Audio Captioning)
**主要指标**：
- Audio Grounding: R@0.5 80.1%, R@0.7 66.3%, R@0.9 39.8%, mIoU 74.4%
- Sound Event Detection: Eb-F1 57.6%
- Dense Audio Captioning: METEOR 33.9%, Eb-F1 40.7%

**是否开源**：暂无代码

### ⭐ 评分：8/10
**理由**：创新性高（Audio-Side Time Prompt + RL后训练）、实验充分（多任务验证）、结果显著（高精度时间定位显著提升）

---
