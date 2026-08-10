# 2026-07-24 语音论文速递

**共收录**: 8 篇 | **语音大模型**: 3 篇 | **语音前端**: 5 篇

> 今日 arXiv 语音相关论文共命中 8 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

## [1] Harness TTS: Towards Context-Aware Expressive Speech Synthesis with Harness Layer

**arXiv ID** 2607.17900 | **方向** 语音大模型

**作者** Shengfan Shen, Di Wu, Xingchen Song, Dinghao Zhou, Pengyu Cheng, Sixiang Lyu, Jian Luan, Shuai Wang

**机构** 湖南大学，南京大学，小米

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.17900 | **PDF** https://arxiv.org/pdf/2607.17900.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Harness TTS提出了一种轻量级的控制层来包装TTS引擎，实现上下文感知的 expressive 语音合成。该方法将风格控制重新表述为封闭集提示工具路由：离线构建风格化提示工具注册表，在线使用LLM planner根据优先级感知观察模式选择适当工具。

### 🔧 技术方案
**模型架构** 基于LLM的planner作为决策核心，使用Qwen3-4B作为路由决策器，配合CosyVoice3和VoxCPM2作为TTS executor。

**核心创新** 提出Harness层架构，将表达控制从TTS引擎外部化。注册表包含两类工具：axis-based工具（速度、音量、情感三轴）和scenario-preset工具（常见语音助手场景）。设计五层观察结构：系统默认、用户画像、场景、隐含意图、显式指令，按优先级策略解决冲突。

**训练策略** 路由任务评估使用Gemini-2.5-Pro作为teacher model，Qwen3系列作为student planner。合成任务比较Harness与Instruct两种控制条件。

### 📊 实验结果
**数据集** 42工具注册表，210样本/子集（explicit/implicit/conflict）

**主要指标**
- 路由任务：Qwen3-4B+CoT在explicit子集达到74.3% T-Exact@1
- 合成任务：Harness在CosyVoice3上比Instruct提高23.1-35.6个百分点win rate
- UTMOSv2提升0.11-0.38
- P95 First-ID延迟41.2ms，满足实时交互

**是否开源** 部分开源

### ⭐ 评分：8/10
创新性地提出Harness层架构解决语音助手表达控制问题，实验充分，在多个子任务上取得显著提升。工程性强，适合实际部署。

---

## [2] Staged Depth-Pruning Distillation of a Flow-Matching Text-to-Speech Teacher: A Compact Hindi Speech Synthesizer

**arXiv ID** 2607.18662 | **方向** 语音大模型

**作者** Sivateja Trikutam

**机构** Independent Researcher

**发布日期** 2026-07-19 | **论文** https://arxiv.org/abs/2607.18662 | **PDF** https://arxiv.org/pdf/2607.18662.pdf | **代码** 暂无 | **Demo** https://huggingface.co/spaces/5ivatej/hindi-tts-190M

### 📌 简介
本文提出一种实用的深度剪枝蒸馏配方，从大型flow-matching TTS teacher（IndicF5，337M参数）蒸馏出小型Hindi TTS模型。在严重数据预算（约17.6小时）约束下，通过逐阶段深度剪枝（22→16→12→8→6 blocks）实现。

### 🔧 技术方案
**模型架构** Teacher为flow-matching DiT（dim=1024, depth=22, heads=16），学生保留宽度不变仅剪枝深度。使用Vocos声码器。

**核心创新** 深度仅warm-start：保持teacher的宽度、text dimension、attention heads不变，保留均匀分布的transformer blocks子集。测量teacher的剪枝容忍度，发现-27% blocks仍near-functional，但-50%后崩溃。

**训练策略** 条件flow-matching目标，lr=5e-5，500步warmup，动态batch 24000 mel frames，Euler ODE solver，EMA权重。每个阶段使用ASR WER门控检查。

### 📊 实验结果
**数据集** ~17.6小时teacher生成的24kHz音频（9999 utterances）

**主要指标**
- 190M参数学生在unseen句子达到WER 0.00
- FLEURS 50句benchmark：UTMOS 3.65 vs teacher 3.79（96%保留）
- SI-SDR提升，RTF 3.13（MPS）
- 102M参数出现明显capacity cliff

**是否开源** 模型开源：https://huggingface.co/5ivatej/hindi-tts-190M

### ⭐ 评分：7.5/10
创新性地将知识蒸馏与结构化剪枝结合，在低资源场景下实现高效TTS。实验详尽，但数据预算限制可能影响泛化性。

---

## [3] CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis with Nonlinear Chaotic Losses

**arXiv ID** 2607.18629 | **方向** 语音大模型

**作者** Sajid Fardin Dipto, Tarikul Islam Tamiti, David Vergano, Luke Baja-Ricketts, Anomadarshi Barua

**机构** 暂无

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18629 | **PDF** https://arxiv.org/pdf/2607.18629.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
CS-ETS首次将混沌理论引入EMG-to-Speech合成，提出基于Samba的encoder结合两个混沌启发损失函数：Lyapunov Exponent Regularization（LER）和Multi-Scale Detrended Fluctuation Analysis（MSDFA）。

### 🔧 技术方案
**模型架构** 修改版Samba架构（Mamba-SWA-MLP），Convolutional Feature Extraction (CFE) block，4层encoder，HiFi-GAN vocoder。

**核心创新**
- LER：基于Lyapunov指数捕获非线性波动和初始条件敏感性
- MSDFA：利用去趋势波动分析量化分形-like长时间相关
- Post-Vocoder Alignment：解决vocoder生成音频与目标的时间对齐问题

**训练策略** AdamW，lr=1e-3，weight decay=1e-7，80 epochs，FP32，2xRTX 4090

### 📊 实验结果
**数据集** Gaddy数据集（19小时EMG数据）

**主要指标**
- 参数减少40.79%（32M vs 54.1M）
- FLOPs减少13.33%
- LSD: 1.07 vs 2.25 baseline（2.1x提升）
- STOI: 0.61 vs 0.13（4.7x提升）
- SI-SDR: -33.41 vs -41.96（1.25x提升）
- MOS: 4.21 vs 3.98

**是否开源** 部分代码

### ⭐ 评分：7.5/10
创新性地将混沌理论引入语音合成，提出新颖的损失函数。实验全面，在多个指标上取得显著提升。工程性强。

---

## 🎙️ 语音前端

## [4] Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution

**arXiv ID** 2607.18658 | **方向** 语音前端

**作者** Zhenglong Liu, Wangyou Zhang, Chenda Li, Yanmin Qian

**机构** 上海交通大学 Auditory Cognition and Computational Acoustics Lab

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18658 | **PDF** https://arxiv.org/pdf/2607.18658.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
提出Geometry-Aware Dynamic Convolution（Geo-DConv）框架，使固定阵列语音增强模型能够适应任意麦克风阵列几何结构。该方法显式利用麦克风坐标信息。

### 🔧 技术方案
**模型架构** Geo-DConv = Geometry-Aware Dynamic Kernel Generation + Topology-Aware Coordinate Transformer (TACT)。TACT使用Fourier位置编码和Transformer Encoder建模全局阵列拓扑。

**核心创新**
- 动态卷积权重由基础核的线性组合生成，组合系数由麦克风坐标决定
- TACT模块保证置换等变性：输入通道排列变化时输出稳定
- 显式利用阵列几何先验，而非仅依赖通用时频特征

**训练策略** RealMAN数据集训练，随机4-mic阵列，评估在多种阵列拓扑

### 📊 实验结果
**数据集** RealMAN（83.7小时多通道语音），CHiME-4跨数据集评估

**主要指标**
- Geometry-Invariant设置：SpatialNet-Geo-DConv达到SI-SDR 4.22dB，OVRL 2.68
- 跨阵列泛化：1/2/5 mic配置均显著优于baseline
- CHiME-4无微调：OVRL从1.42提升到2.64-2.73

**是否开源** 暂未提及

### ⭐ 评分：8/10
创新性地将阵列几何信息引入语音增强，提出有效的动态卷积方法。实验充分，在多个阵列配置和跨数据集上验证有效性。获Interspeech 2026接收。

---

## [5] End-to-End Markov State Sequence Learning for Auditory Attention Decoding

**arXiv ID** 2607.18614 | **方向** 语音前端

**作者** Yushan Yashengjiang, Jie Zhang, Miao Sun, Huadong Liang, Xin Li, Zhen-Hua Ling

**机构** 中国科学技术大学，广州海事大学，科大讯飞

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18614 | **PDF** https://arxiv.org/pdf/2607.18614.pdf | **代码** https://github.com/YusanX/AAD-CRF | **Demo** 暂无

### 📌 简介
提出端到端Markov状态序列学习框架用于听觉注意力解码（AAD）。使用CRF联合优化窗口级神经发射与状态转移，而非将AAD作为独立短窗口分类器。

### 🔧 技术方案
**模型架构** ESCNet：EEG-Speech Correlation Network，保留时间对齐特征，将两个Pearson相关的差异直接转换为状态logits。CRF作为两层注意力状态模型。

**核心创新**
- 将AAD重新表述为注意力状态序列估计
- CRF训练将序列级监督传播到发射网络
- ESCNet使用参数-free的PCC评分，无需额外分类头

**训练策略** 两阶段：CE warm-up + 联合CRF训练。基线切换率q=1e-3初始化后可学习

### 📊 实验结果
**数据集** AVGC（动态注意力切换），KUL和USTC（静态AAD）

**主要指标**
- AVGC 1s窗口：CRF-Causal 86.5%，CRF-NC 92.4%
- KUL：因果解码提升5.6%
- USTC：因果解码提升2.0%
- 四种发射骨架（ESCNet/AADNet/LSTM/Attn-GRU）均验证CRF训练优势

**是否开源** 代码开源：https://github.com/YusanX/AAD-CRF

### ⭐ 评分：8/10
创新性地将CRF引入AAD任务，提出ESCNet骨架。实验详尽，在多个数据集和窗口长度上验证方法有效性。代码开源。

---

## [6] Addressing Limited Data in Auditory Attention Decoding with Diffusion Generative Models

**arXiv ID** 2607.18345 | **方向** 语音前端

**作者** David Rannaleet, Victor Gunnarsson, Bo Bernhardsson, Martin A. Skoglund, Emina Alickovic

**机构** 暂无

**发布日期** 2026-07-22 | **论文** https://arxiv.org/abs/2607.18345 | **PDF** https://arxiv.org/pdf/2607.18345.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
研究使用扩散概率模型（DPM）生成合成语音诱发EEG数据，以解决助听器AAD中训练数据稀缺问题。DPM学习数据的潜在复杂结构，可生成适合数据增强的真实样本。

### 🔧 技术方案
**模型架构** 使用扩散概率模型学习 speech-evoked EEG 数据分布

**核心创新** 使用DPM生成合成EEG数据进行数据增强，解决短时间窗口（≤1s）下真实EEG数据稀缺问题

**训练策略** 在locus-of-attention（LoA）分类任务上评估合成数据增强效果

### 📊 实验结果
**数据集** 语音诱发EEG数据

**主要指标**
- DPM可生成真实感的EEG信号
- 加入合成数据显著提升AAD性能（p<0.05）
- 有效缓解短窗口AAD的训练数据限制

**是否开源** 暂未提及

### ⭐ 评分：6.5/10
创新思路使用生成模型解决数据稀缺问题，实验显示统计显著提升。但需更多细节验证。

---

## [7] Summary of DCASE 2026 Task 5: Audio-Dependent Question Answering

**arXiv ID** 2607.18718 | **方向** 语音前端

**作者** Haolin He, Renhe Sun, Zheqi Dai等（28位作者）

**机构** 多机构联合

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18718 | **PDF** https://arxiv.org/pdf/2607.18718.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
DCASE 2026 Task 5引入Audio-Dependent Question Answering（ADQA），测试大型音频语言模型是否真正从音频而非文本先验作答。提出Audio-Dependency Filtering（ADF）管道移除可从文本解决的题目。

### 🔧 技术方案
**ADF管道** 四阶段过滤：Hard-ADF（静音探测）、Soft-ADF（perplexity过滤）、LLM常识过滤、人工验证。保留3000题形成ADQA-Bench评估集。

**数据集** 训练：AudioMCQ-StrongAC-GeminiCoT；开发：1607题；评估：3000题

**主流技术** MOSS-Audio-8B-Thinking backbone（13/36提交），LoRA微调，GRPO/DPO强化学习，prompt工程，投票集成

### 📊 实验结果
**主要指标**
- 最佳系统：Lim_CAU（MOSS+Qwen3-Omni ensemble）达58.33%
- 轻量级冠军：57.30%（8B模型）
- 开发到评估准确率平均下降11.91pp
- 全部系统均错过同一233题

**是否开源** 数据集和部分基线开源

### ⭐ 评分：7/10
首届ADQA挑战系统总结，提供音频依赖性基准新视角。技术趋势分析详尽，对音频语言模型发展有参考价值。

---

## [8] What the Waveform Knows: Transparent-first Speech and Audio Intelligence with Caption Studio

**arXiv ID** 2607.18704 | **方向** 语音前端

**作者** Cheng Siong Chin, Jianhua Zhang, Mohan Venkateshkumar

**机构** Newcastle University Singapore, 青岛理工大学, Amrita Vishwa Vidyapeetham

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18704 | **PDF** https://arxiv.org/pdf/2607.18704.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Caption Studio是一个透明优先的语音和音频智能平台，通过自动转录、说话人 diarization、语音分析、信号级音频分析和字幕生成，将 spoken audio/video 转换为结构化可搜索内容。

### 🔧 技术方案
**系统架构** 三层架构：转录diarization核心（Whisper + pyannote）、音频智能层（波形/频谱/pitch/语速/静音/填充词/情感）、集成层（多格式导出/webhook/对话查询）。

**核心创新** 透明优先框架：每个报告指标明确标识为"measured"、"derived"或"unavailable"，提高可追溯性和可靠性。

**技术细节** Whisper ASR，pyannote diarization（可选），librosa信号分析，VADER情感，FastAPI后端，WebSocket实时仪表板

### 📊 实验结果
**数据集** 自有评估

**主要指标**
- 提供WER和DER基准评测方法
- 信号分析支持7种可视化：波形/频谱/mel/MFCC/pitch/RMS/VAD
- 支持SRT/WebVTT/CSV/JSON导出

**是否开源** 论文CC BY 4.0

### ⭐ 评分：6.5/10
系统性强，整合多个语音处理组件。透明优先理念有价值，但创新性相对有限，更偏工程系统。

---

## 📋 其他论文（快速浏览）

### 语音大模型
无

### 语音前端
无

---

*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*
