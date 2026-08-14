# 2026-08-07 语音论文速递

**共收录**: 2 篇 | **语音大模型**: 1 篇 | **语音前端**: 1 篇

> 今日 arXiv 语音相关论文共命中 2 篇（另有2篇与0806重复，已跳过）。

---

## 语音大模型

---

## [1] Pixel-TTS: Image based Text Rendering for Robust Text-to-Speech

**arXiv ID**：2606.14750 | **方向**：TTS

**作者**：Adarsh Arigala, Arjun Gangwar, Srinivasan Umesh, Yova Kementchedjhieva

**机构**：IIT Madras, MBZUAI

**发布日期**：2026-08-06 (v2) | **论文**：https://arxiv.org/abs/2606.14750 | **PDF**：https://arxiv.org/pdf/2606.14750.pdf | **代码**：即将发布 | **Demo**：暂无

### 📌 简介
传统TTS系统依赖离散Unicode字符嵌入，每个字符独立处理，导致跨语言适配时需扩展嵌入矩阵且在未见字符上泛化能力差。Pixel-TTS提出首个基于视觉文本渲染的端到端语音合成框架：将文本渲染为16×16灰度图像，经2D卷积层投影为像素级嵌入，利用视觉相似性使结构相似字符（如A-À、e-é）产生相近嵌入。在LibriSpeech-PC上WER 2.28%（对比Text-TTS 2.53%），MOS 4.63（对比4.25），零样本德语零样本WER 66.48%（对比71.49%），在Unicode/l33tspeak噪声下鲁棒性显著优于传统方法。

### 🔧 技术方案

**问题背景：** 传统TTS将每个字符映射为独立one-hot嵌入向量，Unicode编码不同的视觉相似字符（如A和À）被完全独立处理。跨语言适配时需扩展嵌入矩阵，未见字符无法处理。此外，Unicode同形攻击和l33tspeak噪声下传统方法性能急剧下降。

**模型架构：** 基于ADMA架构（F5-TTS的扩展，159M参数，18层Transformer，12注意力头，hidden size 768）。文本渲染：每个字符渲染为16×16灰度patch（白patch作为填充token），按宽度方向堆叠为单张图像X∈R^{H×W}。像素到嵌入投影：单层Conv2D（in=1, out=512, kernel=16×16, stride=16），将每个patch映射为512维嵌入向量。4个ConvNeXtV2 block处理文本嵌入（维度512）。与ADMA共享整体架构和训练流程，沿用CFM损失+CTC文本对齐损失（λ=0.1）+HuBERT语音对齐损失（λ=1.0）。

**核心创新：** (1) 首次将像素级文本表示引入对齐自由的flow-matching TTS框架，替代传统字符嵌入，无需嵌入矩阵扩展即可处理任意Unicode字符。(2) 视觉相似性驱动表示学习：t-SNE可视化显示Pixel-TTS将视觉相似字符（c/C, m/M, o/O等）在嵌入空间中紧密聚类，而Text-TTS中字符嵌入分散无规律。(3) 跨语言共享视觉表示：多语言训练中，Pixel-TTS对带变音符号的拉丁字符对（A-À, e-é等）平均余弦相似度0.989（Text-TTS仅-0.002），证明其捕获了共享视觉结构。

**训练策略：** 基于LibriTTS（585小时，24kHz）训练。AdamW优化器，lr=7.5e-5，20k warmup，线性衰减。batch size 0.758小时音频。8×A100 GPU。Vocos声码器（LibriTTS上300k步预训练）。mel谱：1024窗长，256帧移，100 mel bins。

### 📊 实验结果
**数据集**：LibriSpeech-PC (in-domain), SEED-TTS-EN / LJSpeech (out-of-domain), L2-ARCTIC (非母语), Common Voice DE/FR/NL (零样本)

**主要指标**：
- 300k步后LibriSpeech-PC: WER 2.28%, CER 0.81%, UTMOS 4.01, SIM 0.58（对比Text-TTS: 2.53%/1.16%/4.06/0.59）
- MOS: Pixel-TTS 4.63±0.11 vs Text-TTS 4.25±0.14
- SEED-TTS-EN: WER 2.19% vs 2.36%
- LJSpeech: WER 5.13% vs 5.69%
- L2-ARCTIC非母语英语: WER 3.87% vs 5.35%（相对降低27.7%）
- 零样本德语: WER 66.48% vs 71.49%（相对降低7.0%）
- 10小时德语微调: Pixel-TTS 70k步达WER 16.67%（Text-TTS 150k步仍为17.22%）
- Unicode噪声（p=1.0）: WER 34.88% vs 119.55%
- l33tspeak噪声（p=1.0）: WER 77.18% vs 101.15%
- 多语言训练（英+德+法+荷）: 英语WER 1.94% vs 2.35%，德语7.44% vs 9.74%，法语12.14% vs 14.26%，荷兰语3.82% vs 4.68%

**是否开源**：代码和模型即将发布

### ⭐ 评分：8/10
评分理由：将像素级文本表示成功引入TTS领域，在跨语言泛化、低资源适配、非母语语音和对抗噪声四种挑战性场景下均取得一致且显著的改进。实验设计全面（9个评测场景），分析深入（t-SNE可视化、余弦相似度量化）。但零样本跨语言WER仍较高（66%+），且相对于ADMA基线，视觉编码带来的计算开销未报告。

---

## 语音前端

---

## [2] AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks

**arXiv ID**：2608.05507 | **方向**：语音深度伪造检测

**作者**：Aurosweta Mahapatra, Xiutian Zhao, Shreeram Suresh Chandra, Zihan Zhang, Zongyang Du, Ismail Rasim Ulgen, Kong Aik Lee, Nicholas Andrews, Carlos Busso, Berrak Sisman

**机构**：Johns Hopkins University, Hong Kong Polytechnic University, Carnegie Mellon University

**发布日期**：2026-08-06 | **论文**：https://arxiv.org/abs/2608.05507 | **PDF**：https://arxiv.org/pdf/2608.05507.pdf | **代码**：https://affectdf33-data.github.io/AffectDF-Data/ | **Demo**：暂无

### 📌 简介
现有语音深度伪造检测（SDD）系统在ASVspoof等传统基准上表现强劲，但情感表达和LALM攻击的覆盖极为有限。AffectDF是目前最全面的情感语音深度伪造基准，包含约260小时语音，21种欺骗攻击（TTS/VC/EVC/LALM-EVC四种范式），覆盖5种情感状态（中性/高兴/愤怒/悲伤/惊讶），同时包含表演性和自发性情感语音。评测发现：ASVspoof2019训练的模型在AffectDF上EER高达59.71%（接近随机），甚至大规模情感训练也不能一致提升跨域鲁棒性，多个系统在情感条件下接近随机性能。

### 🔧 技术方案

**问题背景：** 现有ASVspoof基准主要关注中性语音，情感欺骗数据集（EmoFake 7种VC攻击，EmoSpoof-TTS 3种TTS攻击）规模小、攻击多样性不足且缺乏LALM攻击。情感语音在基频、能量、语速、shimmer等方面引入巨大变异性，可能掩盖或改变SDD系统依赖的伪造痕迹。

**数据集构建：** 基于ESD（表演性情感语音，4个说话人）和MSP-Podcast（自发性情感语音，4个说话人）两个语料库。21种攻击：LALM-EVC（Qwen2.5-Omni, Kimi-Audio, MiniCPM-o 4.5，含steered版本）、TTS（CosyVoice/2/3, Qwen3-TTS, StyleTTS2, F5-TTS）、VC（GenVC, ConsistencyVC, TriAAN-VC, DDDMVC）、EVC（GenVC-EVC, Vevo2-EVC）。训练/开发/测试集说话人disjoint，攻击系统disjoint。训练集5种攻击（86,999样本），开发集2种攻击（23,330样本），测试集14种攻击（175,468样本，8个说话人）。

**核心创新：** (1) 规模和覆盖度全面超越现有情感欺骗基准：260小时+21种攻击+5种情感+表演/自发双模式。(2) 首次系统评估LALM-based SDD（Qwen-2.5-Omni, Qwen-3.0-Omni, Voxtral），包含inference-only prompting和supervised fine-tuning两种设置。(3) 揭示SDD系统根本性局限：情感变异性导致SDD系统无法学习广义的欺骗相关表示，训练数据扩展（从ASVspoof2019到AffectDF）不能一致提升跨域鲁棒性，且通常以牺牲常规基准性能为代价。

**评估协议：** 6个评估维度：情感角色、跨域泛化、情感攻击鲁棒性、情感状态间差异、表演vs自发、攻击家族间差异。基准模型：RawNet2, AASIST, XLSR-SLS, XLSR-Mamba, ProSDD（传统+SSL），Qwen-2.5-Omni, Qwen-3.0-Omni, Voxtral（LALM）。EER为主要指标。

### 📊 实验结果
**数据集**：ASVspoof2019/2021/5, EmoFake, EmoSpoof-TTS, AffectDF

**主要指标**：
- ASVspoof2019训练→AffectDF测试: RawNet2 59.71%, AASIST 56.40%, XLSR-SLS 44.91%, XLSR-Mamba 29.78%, ProSDD 31.04%
- ASVspoof5训练→AffectDF测试: ProSDD最优12.49%（AASIST 18.00%, RawNet2 33.02%）
- AffectDF训练→ASVspoof2019测试: RawNet2 43.02%（严重退化），AASIST 44.52%
- 情感间差异：愤怒/悲伤通常EER最低，中性/高兴/惊讶最高（但模式因模型和训练数据而异）
- 表演vs自发（GenVC/StyleTTS2/F5-TTS）：自发语音EER普遍低于表演语音
- LALM-SDD: Voxtral (ASVspoof2019微调) AffectDF EER 26.15%，Qwen-2.5-Omni inference-only 45.29%
- 攻击家族间差异：TTS攻击最易检测，LALM-EVC攻击最难

**是否开源**：AffectDF数据集完全公开

### ⭐ 评分：9/10
评分理由：在情感语音深度伪造检测领域建立了迄今为止最全面的基准，21种攻击×5种情感×2种语音模式的系统性覆盖大幅超越现有数据集。实验设计严谨，6个维度的系统评估揭示了SDD领域的关键瓶颈：情感变异性破坏广义泛化。最令人警醒的发现是情感训练不能一致提升鲁棒性，且通常以常规性能为代价，表明当前SDD架构存在根本性局限。对语音安全领域有重要推动价值。

---

*Generated on 2026-08-14*