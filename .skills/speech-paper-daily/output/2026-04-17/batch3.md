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

## [5] Graph Propagated Projection Unlearning: A Unified Framework for Vision and Audio Discriminative Models

**arXiv ID**: 2604.13127
**方向**: 语音大模型
**作者**: Shreyansh Pathak, Jyotishman Das
**机构**: Indian Institute of Technology Jodhpur
**发布日期**: 2026-04-13
**论文链接**: https://arxiv.org/abs/2604.13127
**PDF 链接**: https://arxiv.org/pdf/2604.13127.pdf
**代码链接**: 暂无
**Demo 链接**: 暂无

### 📌 简介
本文提出Graph-Propagated Projection Unlearning (GPPU)，一个跨视觉和音频模型的统一、可扩展类别级遗忘学习算法。通过基于图的传播识别特征空间中的类别特定方向，将表征投影到正交子空间并进行针对性微调，确保目标类别信息有效且不可逆地移除。该方法实现10-20倍加速，同时在多个数据集上保持高保留类别性能。

### 🔧 技术方案

**模型架构**：跨模态框架，支持ResNets、Vision Transformers、Audio Transformers (Wav2Vec2/HuBERT)

**核心创新**：
1. Graph-based Forget Direction：构建k-NN特征图（k=8），通过图传播平滑类内变异，提取forget direction g_c作为传播后特征的类别质心
2. Projection-Based Unlearning：将特征投影到forget direction正交子空间：h_proj = h - (h·g)g
3. Projection Loss + Retention Loss联合优化：L_proj惩罚投影到forget direction的幅度，L_retain保持保留类别性能

**训练策略**：
- 微调参数：仅微调最后几层（ViT: 1-2 transformer blocks, CNN: final conv block, Audio: 2-3 transformer layers）
- 超参数：λ_proj=1.0, λ_retain=0.5, lr=1e-5, epochs=3, weight decay=1e-2
- 大数据集：使用FAISS加速k-NN搜索

### 📊 实验结果
**数据集**：CIFAR-10/100、SVHN、Flowers102、STL-10、FashionMNIST、LibriSpeech-100h、SpeechCommands v2、VoxCeleb1
**主要指标**：
- Forget Accuracy接近随机猜测（≈1/C）
- Retain Accuracy保持高水平
- 计算效率：10-20倍加速 vs Fisher Forgetting/Gradient Ascent
- VoxCeleb1: Speaker 10005遗忘，保留类别性能稳定

**是否开源**：暂无代码

### ⭐ 评分：8/10
**理由**：创新性高（Graph propagation + Projection unlearning）、实验充分（跨模态验证）、效率显著（10-20倍加速）、实用价值高（隐私合规/模型自适应）

---

## [6] Few-Shot and Pseudo-Label Guided Speech Quality Evaluation with Large Language Models

**arXiv ID**: 2604.13528
**方向**: 语音大模型
**作者**: Ryandhimas E. Zezario, Dyah A. M. G. Wisnu, Szu-Wei Fu, Sabato Marco Siniscalchi, Hsin-Min Wang, Yu Tsao
**机构**: 多机构合作
**发布日期**: 2026-04-15
**论文链接**: https://arxiv.org/abs/2604.13535
**PDF 链接**: https://arxiv.org/pdf/2604.13528.pdf
**代码链接**: 暂无
**Demo 链接**: 暂无

### 📌 简介
本文提出GatherMOS，利用大型语言模型作为元评估器聚合多信号进行语音质量预测。GatherMOS结合轻量级声学描述符（RMS、ZCR、MFCC等）与DNSMOS/VQScore伪标签，使LLM推理异构输入并推断感知MOS分数。在VoiceBank-DEMAND数据集上，GatherMOS在有限标注数据条件下超越DNSMOS、VQScore和CNN-BLSTM/MOS-SSL学习模型。

### 🔧 技术方案

**模型架构**：基于GPT-5作为元评估器，输入结构化文本提示（声学特征 + 伪标签），输出连续MOS预测和辅助属性（噪声级别、削波、混响等）

**核心创新**：
1. Meta-Evaluator框架：LLM聚合轻量声学描述符和伪标签（DNSMOS/VQScore）
2. Zero-shot vs Few-shot对比：zero-shot稳定跨条件，few-shot在匹配条件时大幅提升
3. 特征增强：MFCC + spectrogram statistics进一步改善性能

**训练策略**：
- 输入特征：RMS、ZCR、clipping ratio、duration、MFCC（13维）、mel-spectrogram statistics
- Zero-shot：仅使用基本声学特征
- Few-shot：添加K个标注示例作为context
- 批量评估：minibatch=10，session reset避免cross-sample conditioning

### 📊 实验结果
**数据集**：VoiceBank-DEMAND (200 utterances, 10 listeners)
**主要指标**：
- GatherMOS-ZS: LCC 0.6439, SRCC 0.6014
- GatherMOS-ZS* (with MFCC/spectrogram): LCC 0.6495, SRCC 0.6069
- vs DNSMOS: LCC 0.6021, SRCC 0.5314
- vs VQScore: LCC 0.5753, SRCC 0.4476
- vs CNN-BLSTM (limited data): LCC 0.3192, SRCC 0.2971
- vs MOS-SSL (limited data): LCC 0.4888, SRCC 0.4732

**是否开源**：暂无代码

### ⭐ 评分：7/10
**理由**：创新性中等（LLM作为元评估器）、实验较充分（多条件对比）、实用价值中等（减少标注依赖）

---

*由Speech-paper-daily工具 🍀 自动生成 · 数据来源：arXiv*