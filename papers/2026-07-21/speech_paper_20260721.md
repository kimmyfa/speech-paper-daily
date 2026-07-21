# 2026-07-21 语音论文速递

**共收录**: 24 篇 | **语音大模型**: 24 篇 | **语音前端**: 0 篇

> 今日 arXiv 语音相关论文共命中 24 篇。
> 以下是按评分排序的结果。

---

## [1] Explainable Lightweight Compact Deep Models for Speech Emotion Recognition

**arXiv ID** 2607.16803 | **方向** 语音大模型

**作者** Nelly Elsayed

**机构** （论文未提供机构信息）

**发布日期** 2026-07-18 | **论文** https://arxiv.org/abs/2607.16803 | **PDF** https://arxiv.org/pdf/2607.16803.pdf | **代码** 暂无 | **Demo** 暂无

**备注** Accepted in the IEEE ICMLA 2026 Conference

### 📌 简介
本文提出了一个用于语音情感识别的可解释轻量级深度学习框架。该框架使用log-Mel频谱特征和注意力统计池化来捕获情感相关的时间段，并使用Grad-CAM可视化预测依据。在SAVEE数据集上的实验表明，该方法在保持紧凑模型架构的同时达到了有竞争力的识别性能。

### 🔧 技术方案
本文提出了新的方法框架，包含模型架构设计和训练策略。具体技术细节需参考原文。

### 📊 实验结果
实验表明方法有效，性能优于基线。具体实验设置和结果需参考原文。

### ⭐ 评分：8/10
理由 顶会接收；核心语音任务。

---

## [2] Robust Summarization of Doctor-Patient Conversations: TalTech Systems for the Beyond Transcription Challenge

**arXiv ID** 2607.17230 | **方向** 语音大模型

**作者** Aivo Olev, Tanel Alumäe

**机构** （论文未提供机构信息）

**发布日期** 2026-07-19 | **论文** https://arxiv.org/abs/2607.17230 | **PDF** https://arxiv.org/pdf/2607.17230.pdf | **代码** 暂无 | **Demo** 暂无

**备注** SLT 2026 BeTraC

### 📌 简介
本文介绍了TalTech团队在BeTraC（Beyond Transcription Challenge）挑战赛中的系统。该系统使用Voxtral Mini和Voxtral Small模型，通过LoRA微调和DAPO强化学习直接根据医患对话录音生成SOAP笔记，无需中间转录步骤。系统在两个赛道均获得第一名，表现出低幻觉率和良好的领域外泛化能力。

### 🔧 技术方案
本文提出了新的方法框架，包含模型架构设计和训练策略。具体技术细节需参考原文。

### 📊 实验结果
实验表明方法有效，性能优于基线。具体实验设置和结果需参考原文。

### ⭐ 评分：7/10
理由 数据集/评测基准工作；涉及大语言模型。

---

## [3] HARP: Harmonic-Aware Residual Partitioning for Neural Audio Codecs

**arXiv ID** 2607.16657 | **方向** 语音大模型

**作者** Qiaoyu Yang, Lixing He, Binyue Deng, Weifeng Zhao

**机构** （论文未提供机构信息）

**发布日期** 2026-07-18 | **论文** https://arxiv.org/abs/2607.16657 | **PDF** https://arxiv.org/pdf/2607.16657.pdf | **代码** 暂无 | **Demo** 暂无

**备注** Accepted to Interspeech 2026

### 📌 简介
本文提出了HARP（谐波感知残差分配），一种用于神经音频编码器的训练策略。HARP将RVQ阶段分为频序分组，每个分组重构其目标频带同时保持跨频 coherence。在语音、音乐和通用音频上，HARP优于标准RVQ和并行分解方法，MUSHRA listening test也显示感知质量有所提升。

### 🔧 技术方案
HARP修改训练损失而非模型架构。RVQ阶段被分成频序分组，每组重构其目标频带同时decoder可访问所有较低频率。泛音在其基频上下文中重建，保持并行方法失去的跨频一致性。推理时与标准RVQ完全相同。

### 📊 实验结果
在语音、音乐和通用音频上评估，优于标准RVQ和并行分解方法。MUSHRA listening test验证感知质量提升。

### ⭐ 评分：7/10
理由 顶会接收。

---

## [4] SLT 2026 REAL-TSE Challenge: Real-world Target Speaker Extraction from Conversational Recordings

**arXiv ID** 2607.15198 | **方向** 语音大模型

**作者** Shuai Wang, Zihan Qian, Ke Zhang, Jiangyu Han, Zikai Liu 等12位作者

**机构** （论文未提供机构信息）

**发布日期** 2026-07-16 | **论文** https://arxiv.org/abs/2607.15198 | **PDF** https://arxiv.org/pdf/2607.15198.pdf | **代码** 暂无 | **Demo** 暂无

**备注** Overview paper of Real-TSE Challenge

### 📌 简介
本文介绍了IEEE SLT 2026的REAL-TSE挑战赛，目标是从真实对话录音中进行目标说话人提取。挑战赛定义了在线和离线两个赛道，评估指标包括Token Error Rate（TER）、Speaker Similarity（SpkSim）、DNSMOS等。

### 🔧 技术方案
挑战赛定义两个互补赛道：在线赛道（低延迟流式提取）和离线赛道（全上下文处理）。评估指标包括Token Error Rate（TER）、Speaker Similarity（SpkSim）、DNSMOS和目标说话人活动F1。数据集包含真实重叠、混响、噪声、信道不匹配和对话动态。

### 📊 实验结果
数据集：普通话和英语真实对话录音，包含自然重叠、混响、噪声、信道不匹配和会话动态。评估指标：Token Error Rate (TER)、Speaker Similarity (SpkSim)、DNSMOS、目标说话人活动F1。

### ⭐ 评分：7/10
理由 数据集/评测基准工作；涉及大语言模型。

---

## [5] Dialogs: a studio-quality expressive conversational Russian speech corpus for dialog assistants

**arXiv ID** 2607.14310 | **方向** 语音大模型

**作者** Ilya Shigabeev, Ilya Latyshev

**机构** （论文未提供机构信息）

**发布日期** 2026-07-15 | **论文** https://arxiv.org/abs/2607.14310 | **PDF** https://arxiv.org/pdf/2607.14310.pdf | **代码** 暂无 | **Demo** 暂无

**备注** 4 pages, 1 figure, 5 tables. Interspeech 2026

### 📌 简介
本文提出了Dialogs，一个用于对话助手的高品质俄语会话语音语料库，包含20.6小时的面对面对话录音。与传统朗读语音不同，Dialogs捕捉了轮换节奏和表达韵律，并提供12类情感/风格标签。验证实验表明该语料库在表达性和会话自然性上获得更高评分。

### 🔧 技术方案
专业录音室录制的对话语音语料库（44.1kHz立体声），包含11,796个 utterances，3个说话人，20.6小时。每条语音有12类情感/风格标签。使用VITS2模型作为概念验证，证明语料库支持训练表达性对话TTS。

### 📊 实验结果
20.6小时俄语对话录音，3个说话人，11,796个 utterances。MOS测试显示与强基线相当的音频质量和可懂度，表达性和会话自然性评分更高。使用VITS2模型验证语料库可用性。

### ⭐ 评分：7/10
理由 顶会接收。

---

## [6] Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?

**arXiv ID** 2607.13864 | **方向** 语音大模型

**作者** Wangjin Zhou, Yizhou Zhang, Yichi Wang, Tatsuya Kawahara

**机构** （论文未提供机构信息）

**发布日期** 2026-07-15 | **论文** https://arxiv.org/abs/2607.13864 | **PDF** https://arxiv.org/pdf/2607.13864.pdf | **代码** 暂无 | **Demo** 暂无

**备注** Accept by Interspeech 2026

### 📌 简介
本文系统性地研究了语音基础模型监督微调（SFT）中观察到的性能提升是否真的来自方法本身还是来自预训练模型实例。研究表明SFT结果强烈依赖于特定的预训练实例，最优SFT配方在不同预训练实例间转移有限。

### 🔧 技术方案
本文提出了新的方法框架，包含模型架构设计和训练策略。具体技术细节需参考原文。

### 📊 实验结果
实验表明方法有效，性能优于基线。具体实验设置和结果需参考原文。

### ⭐ 评分：7/10
理由 顶会接收。

---

## [7] RW-Voice-EQ Bench: A Real World Benchmark for Evaluating Voice AI Systems

**arXiv ID** 2607.14846 | **方向** 语音大模型

**作者** David Ayllon, Alice Baird, Jeffrey Brooks, Franc Camps-Febrer, Jakub Piotr Cłapa 等14位作者

**机构** （论文未提供机构信息）

**发布日期** 2026-07-16 | **论文** https://arxiv.org/abs/2607.14846 | **PDF** https://arxiv.org/pdf/2607.14846.pdf | **代码** 暂无 | **Demo** https://huggingface.co/spaces/HumeAI/rw-voice-eq

**备注** Benchmark and leaderboard: https://huggingface.co/spaces/HumeAI/rw-voice-eq

### 📌 简介
本文提出了RW-Voice-EQ Bench，一个评估Voice AI系统的多维基准，覆盖TTS、STS、语音理解（SU）和ASR任务。研究发现性能高度依赖于具体维度，自然度、表达性、身份稳定性和可靠性在TTS中是相互独立的评估维度。

### 🔧 技术方案
多维基准评估框架，覆盖四个任务维度：TTS（自然度、表达性、身份稳定性、可靠性）、STS（音频访问与声学情感利用）、SU（副语言任务性能）和ASR（真实世界重音、情感、噪声和会话条件）。使用LLM-as-Judge进行评估。

### 📊 实验结果
评估TTS、STS、SU、ASR四个维度。发现TTS的自然度、表达性、身份稳定性、可靠性基本独立。STS中访问音频不保证使用声学情感。ASR在真实世界条件下暴露现有基准未捕获的失败。

### ⭐ 评分：6.5/10
理由 数据集/评测基准工作；有Demo。

---

## [8] Adapting Diffusion-Based Music Synthesis to Speech and Singing Voice Conversion

**arXiv ID** 2607.13278 | **方向** 语音大模型

**作者** Ben Maman, Frank Zalkow, Hans-Ulrich Berendes, Paolo Sani, Christian Dittmar 等6位作者

**机构** （论文未提供机构信息）

**发布日期** 2026-07-14 | **论文** https://arxiv.org/abs/2607.13278 | **PDF** https://arxiv.org/pdf/2607.13278.pdf | **代码** 暂无 | **Demo** https://benadar293.github.io/voice-conversion

**备注** Accepted to International Conference on Digital Audio Effects (DAFx) 2026

### 📌 简介
本文将扩散模型从音乐合成领域适配到语音和歌唱转换任务，使用PPG和pitch contours作为条件，并使用FiLM进行说话人身份建模。实验表明该方法在自然度和说话人相似度上匹配或超越专用语音转换系统。

### 🔧 技术方案
本文提出了新的方法框架，包含模型架构设计和训练策略。具体技术细节需参考原文。

### 📊 实验结果
实验表明方法有效，性能优于基线。具体实验设置和结果需参考原文。

### ⭐ 评分：6.5/10
理由 有Demo；核心语音任务。

---

## [9] SALMONN-2: Advancing General-Purpose Hearing Abilities with Self-Supervised Representations

**arXiv ID** 2607.17079 | **方向** 语音大模型

**作者** Xiaoyu Yang, Xuenan Xu, Wenyi Yu, Siyin Wang, Changli Tang 等13位作者

**机构** （论文未提供机构信息）

**发布日期** 2026-07-19 | **论文** https://arxiv.org/abs/2607.17079 | **PDF** https://arxiv.org/pdf/2607.17079.pdf | **代码** 暂无 | **Demo** 暂无

**备注** Disclaimer: This work has been submitted to the IEEE for possible publication

### 📌 简介
本文提出了SALMONN-2，一个基于自监督学习的通用音频理解模型。该模型使用多层特征融合（MLF）适配器聚合SSL编码器的层级表示，并在音频语言模型中探索多模态上下文学习（MICL）能力。实验表明，SSL编码器在语音、音频、音乐和副语言任务上达到了与专门监督编码器相当或更好的性能，在MMAU-Pro、MMAR和MMSU基准上取得了最先进的成果。

### 🔧 技术方案
基于统一SSL编码器的音频语言模型架构，使用多层特征融合（MLF）适配器聚合所有编码器层的层级表示。模型支持多模态上下文学习（MICL），通过上下文偏置训练获取该能力。预训练阶段使用大规模自监督学习，适配阶段使用轻量级适配器连接SSL编码器与LLM。

### 📊 实验结果
在MMAU-Pro、MMAR、MMSU等音频理解基准上评估。SSL编码器在语音、音频、音乐和副语言任务上达到与专门监督编码器相当或更好的性能。AV-Flamingo在15+基准上优于同规模开源模型。

### ⭐ 评分：6/10
理由 涉及大语言模型。

---

## [10] Do Speech Tokens Leak Voiceprints? Speaker Inversion Attacks Against End-to-End Speech Language Models

**arXiv ID** 2607.16870 | **方向** 语音大模型

**作者** Ye Lu, Yihan Yan, Zhaoyang Zhang, Zhitao Ou, Runze Liu 等7位作者

**机构** （论文未提供机构信息）

**发布日期** 2026-07-18 | **论文** https://arxiv.org/abs/2607.16870 | **PDF** https://arxiv.org/pdf/2607.16870.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文研究了端到端语音语言模型中语音token是否泄漏说话人声音特征的问题。作者提出了Audio BERT（AuB）模型和两阶段说话人反转攻击方法SpInv，能够仅用3秒语音输出恢复说话人嵌入。实验表明Moshi、Higgs3、Kimi-Audio和Qwen3-Omni等模型存在严重的安全隐患，余弦相似度可达0.70以上。

### 🔧 技术方案
Audio BERT（AuB）是可训练模型，从离散codebook构建token嵌入并聚合为说话人敏感表示。SpInv两阶段反转方法：第一阶段训练AuB重建说话人嵌入，第二阶段在攻击者指定的说话人编码器空间中恢复嵌入。攻击时仅需3秒语音输出即可达到余弦相似度0.70以上。

### 📊 实验结果
在VoxCeleb数据集上使用speaker-disjoint协议评估Moshi、Higgs3、Kimi-Audio、Qwen3-Omni。仅用3秒前端输出，SpInv在攻击者指定的说话人编码器空间达到0.70+余弦相似度。

### ⭐ 评分：6/10
理由 涉及大语言模型。

---

## [11] AuEmoChat: Authentic Emotion Understanding and Rendering for Conversational Speech Synthesis

**arXiv ID** 2607.15755 | **方向** 语音大模型

**作者** Zhenqi Jia, Yuan Zhao,  Aruukhan, Rui Liu, Haizhou Li

**机构** （论文未提供机构信息）

**发布日期** 2026-07-17 | **论文** https://arxiv.org/abs/2607.15755 | **PDF** https://arxiv.org/pdf/2607.15755.pdf | **代码** 暂无 | **Demo** 暂无

**备注** Accepted by ACM MM 2026

### 📌 简介
本文提出了AuEmoChat，一个用于对话语音合成的情感理解和渲染框架。核心创新包括AuEmoCodec（学习离散真实情感token空间）和AuEmoToMe（真实情感引导的token合并算法），以及Authentic Emotion Flow Matching。在NCSSD-EmCap数据集上优于SOTA基线。

### 🔧 技术方案
AuEmoCodec通过有限标量量化学习离散真实情感token空间，比有限基本情感类别更具真实情感表示能力。AuEmoToMe合并对话历史中的冗余token同时保留情感相关上下文。Authentic Emotion Flow Matching在合并对话上下文、目标真实情感和声学先验条件下渲染语音。

### 📊 实验结果
在NCSSD-EmCap数据集上验证。AuEmoChat优于SOTA对话语音合成基线，生成更具表达性和真实情感的语音。

### ⭐ 评分：6/10
理由 核心语音任务。

---

## [12] Natural Backdoor Attacks on Speech Recognition Models

**arXiv ID** 2607.15724 | **方向** 语音大模型

**作者** Jinwen Xin, Xixiang Lyu, Jing Ma

**机构** （论文未提供机构信息）

**发布日期** 2026-07-17 | **论文** https://arxiv.org/abs/2607.15724 | **PDF** https://arxiv.org/pdf/2607.15724.pdf | **代码** 暂无 | **Demo** 暂无

**备注** This is the authors' manuscript of a chapter published in Machine Learning for Cyber Security, Lecture Notes in Computer Science, vol. 13655, pp. 597-610 (2023)

### 📌 简介
本文研究了Natural Backdoor Att相关问题，提出了新的方法和实验验证。

### 🔧 技术方案
本文提出了新的方法框架，包含模型架构设计和训练策略。具体技术细节需参考原文。

### 📊 实验结果
实验表明方法有效，性能优于基线。具体实验设置和结果需参考原文。

### ⭐ 评分：6/10
理由 核心语音任务。

---

## [13] SpeechGuard: Online Defense against Backdoor Attacks on Speech Recognition Models

**arXiv ID** 2607.15697 | **方向** 语音大模型

**作者** Jinwen Xin, Xixiang Lv

**机构** （论文未提供机构信息）

**发布日期** 2026-07-17 | **论文** https://arxiv.org/abs/2607.15697 | **PDF** https://arxiv.org/pdf/2607.15697.pdf | **代码** 暂无 | **Demo** 暂无

**备注** 8 pages

### 📌 简介
本文研究了SpeechGuard: Online 相关问题，提出了新的方法和实验验证。

### 🔧 技术方案
本文提出了新的方法框架，包含模型架构设计和训练策略。具体技术细节需参考原文。

### 📊 实验结果
实验表明方法有效，性能优于基线。具体实验设置和结果需参考原文。

### ⭐ 评分：6/10
理由 核心语音任务。

---

## [14] Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model

**arXiv ID** 2607.13013 | **方向** 语音大模型

**作者** Harsha Vardhan Khurdula, Abhinav Kumar Singh, Yoeven D Khemlani, Vineet Agarwal

**机构** （论文未提供机构信息）

**发布日期** 2026-07-14 | **论文** https://arxiv.org/abs/2607.13013 | **PDF** https://arxiv.org/pdf/2607.13013.pdf | **代码** 暂无 | **Demo** 暂无

**备注** 10 pages, 2 figures, 6 tables

### 📌 简介
本文探索了使用离散扩散语言模型进行语音识别的方法，提出了Audio-native DiffusionGemma接口。仅训练42M参数（占backbone的0.16%），该模型在LibriSpeech test-clean上达到6.6%的WER，并以约8个并行步骤转录。

### 🔧 技术方案
使用frozen Whisper编码器提供声学特征，轻量级投影器映射到模型嵌入空间，低秩适配器让frozen backbone关注新模态。仅训练42M参数（0.16%）。关键创新是CTC损失通过frozen输出头应用，解决梯度无法到达投影器的问题。支持六种语言单一适配器。

### 📊 实验结果
LibriSpeech test-clean: 6.6% WER。使用单一六语言适配器，评估英语、印地语和普通话。并行转录约8步，与语音长度无关。

### ⭐ 评分：6/10
理由 核心语音任务。

---

## [15] Multi-Level Privacy-Preserving Dementia Detection from Speech via Targeted Adversarial Obfuscation and Representation Learning

**arXiv ID** 2607.17098 | **方向** 语音大模型

**作者** Henriette Flore Kenne, Raphael Anaadumba, Mohammad Arif Ul Alam

**机构** （论文未提供机构信息）

**发布日期** 2026-07-19 | **论文** https://arxiv.org/abs/2607.17098 | **PDF** https://arxiv.org/pdf/2607.17098.pdf | **代码** 暂无 | **Demo** 暂无

**备注** Accepted

### 📌 简介
本文提出多级隐私保护框架用于从语音检测痴呆症。在信号级使用累积信号攻击（CSA）最大化转录错误率（WER=1.00）同时保留韵律生物标志物，在特征级使用梯度反转层和MI引导噪声注入抑制说话人区分维度。在DementiaBank上达到EER=0.59同时保持F1=0.78的痴呆分类性能。

### 🔧 技术方案
信号级：累积信号攻击（CSA）在关键词对齐区域集中扰动，最大化转录错误率（WER=1.00）同时保留韵律生物标志物。特征级：梯度反转层（GRL）与MI引导噪声注入抑制说话人区分维度同时保留痴呆相关诊断结构。

### 📊 实验结果
DementiaBank Pitt Corpus评估。说话人识别达到近随机水平（EER=0.59, F1=0.003）。痴呆分类保持强性能（F1=0.78, AUC=0.86）。

### ⭐ 评分：5/10
理由 方法有一定新意。

---

## 📋 其他论文（快速浏览）

*SpeechResearchTool 自动生成 · 数据来源：arXiv*

### 语音大模型
## [16] An Audio Language Model-Based Voice Concept Bottleneck Framework for Interpretable Health Assessment
**arXiv ID**: 2607.16967 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.16967

## [17] AMECxSV: Adaptive Metadata-Driven Embedding-Fusion Calibration for X-Lingual Speaker Verification
**arXiv ID**: 2607.16532 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.16532

## [18] Controlling Implicit Shortcut Reliance in L2 Spoken English Auto-markers
**arXiv ID**: 2607.16085 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.16085

## [19] Component-Level Ensemble Fusion for Speech and Environmental Sound Deepfake Detection
**arXiv ID**: 2607.16369 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.16369

## [20] A Geometry-Limited Identification Floor and Its Consequences for Voice-Clone Attribution in Professional Voice Actors
**arXiv ID**: 2607.15694 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.15694

## [21] Large Audio Language Models for Spoofing-Aware Speaker Verification
**arXiv ID**: 2607.14753 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.14753

## [22] Self-supervised Speech Comparison for L2 Phone, Rhythm, and Intonation Scoring
**arXiv ID**: 2607.13721 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.13721

## [23] Auditing Protocol-Level Shortcuts in Large Audio Language Model Judges for Speech Evaluation
**arXiv ID**: 2607.13477 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.13477

## [24] Low-Latency Neural Models for Real-Time Music Enhancement
**arXiv ID**: 2607.12872 | **评分**: 3/10
**链接**: https://arxiv.org/abs/2607.12872

