# 2026-07-22 语音论文速递

**共收录**: 13 篇 | **语音大模型**: 5 篇 | **语音前端**: 8 篇

> 今日 arXiv 语音相关论文共命中 13 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

### [1] Harness TTS: Towards Context-Aware Expressive Speech Synthesis with Harness Layer

**arXiv ID** 2607.17900 | **方向** 语音大模型 / TTS

**作者** Shengfan Shen, Di Wu, Xingchen Song, Dinghao Zhou, Pengyu Cheng, Sixiang Lyu, Jian Luan, Shuai Wang

**机构** 南京大学，小米公司，WeNet开源社区

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.17900 | **PDF** https://arxiv.org/pdf/2607.17900.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出Harness TTS，一个轻量级的控制层，用于语音助手的情感合成。该方法将风格控制重新表述为封闭集提示工具路由问题，通过LLM planner选择合适的表达提示符，然后由TTS执行器合成语音。实验表明Harness TTS在路由和合成任务上均优于基线方法。

### 🔧 技术方案

**模型架构** Harness TTS由离线工具注册库、在线LLM planner和TTS执行器组成。工具注册库包含轴向工具和场景预设工具，每个工具绑定音频和结构化元数据。Planner使用Qwen3-4B根据优先级感知观察模式选择合适工具，执行器使用CosyVoice3或VoxCPM2合成语音。

**核心创新** 提出Harness层概念，将表达决策外部化而非修改底层TTS引擎。设计优先级策略解决冲突（显式指令>隐式意图>场景>用户画像>系统默认）。采用封闭集提示工具路由代替开放域连续参数空间。

**训练策略** 路由任务评估：构建42个工具的评估集，包含显式、隐式和冲突三个子集。使用Gemini-2.5-Pro生成测试用例，Qwen3系列作为planner。合成任务使用CosyVoice3和VoxCPM2作为后端。

### 📊 实验结果
**数据集** 路由任务：210样本/子集×3子集；合成任务：27风格指令标签×5 utterances=135测试用例

**主要指标** 路由任务：Qwen3-4B+CoT达到显式子集74.3%、隐式子集43.0%、冲突子集64.6%的Top-1准确率。合成任务：Harness相比Instruction-only在CosyVoice3上提升23.1-35.6个百分点instruction-following win rate，在VoxCPM2上提升13.8-20.0个百分点，UTMOSv2提升0.11-0.38。Planner延迟：Qwen3-4B首个工具推荐延迟P95为41.2ms。

**是否开源** 部分开源（代码未发布，但模型和工具注册库结构已描述）

### ⭐ 评分：8/10
创新性强，提出Harness层概念解决语音助手表达控制问题，实验充分，在路由和合成任务上都展示了显著改进。工程价值高，适合实际部署。

---

### [2] Staged Depth-Pruning Distillation of a Flow-Matching Text-to-Speech Teacher: A Compact Hindi Speech Synthesizer

**arXiv ID** 2607.18662 | **方向** 语音大模型 / TTS

**作者** Sivateja Trikutam

**机构** 个人

**发布日期** 2026-07-19 | **论文** https://arxiv.org/abs/2607.18662 | **PDF** https://arxiv.org/pdf/2607.18662.pdf | **代码** https://huggingface.co/5ivatej/hindi-tts-190M | **Demo** https://huggingface.co/spaces/5ivatej/hindi-tts-190M

### 📌 简介
本文提出一种实用的紧凑印地语TTS模型构建方法，通过从大模型（IndicF5，337M参数）蒸馏得到小模型。采用深度剪枝的渐进式蒸馏策略，在17.6小时的数据预算下训练出190M参数的模型，可在6GB笔记本GPU上实时运行。

### 🔧 技术方案

**模型架构** 使用IndicF5作为teacher（337M参数的DiT流匹配模型），通过深度剪枝得到student。保持teacher的宽度、文本维度、注意力头不变，只减少transformer块数量。

**核心创新** 深度only warm-start：非块张量一一复制。测量剪枝容忍度：teacher在-27%块时仍接近原有功能，-50%后崩溃。渐进式蒸馏阶梯：22→16→12→8→6块，每步微调后用ASR WER门控。记录两个train/inference parity失败（mel filterbank和rotary embedding库版本）。

**训练策略** 数据：约17.6小时teacher生成的24kHz音频（9999句）。训练：lr=5e-5，500步warmup，动态batch 24000 mel帧，Euler ODE solver，EMA权重。

### 📊 实验结果
**数据集** 17.6小时teacher生成的印地语音频，FLEURS hi_in测试集50句

**主要指标** 249M模型在未见句子达到WER 0.00，190M模型WER 0.00-0.06，131M模型WER 0.06-0.12。独立基准：190M学生保留教师96%自然度（UTMOS 3.65 vs 3.79）和说话人相似度（0.750 vs 0.784），参数量56%，合成速度1.8倍。

**是否开源** 已开源：https://huggingface.co/5ivatej/hindi-tts-190M

### ⭐ 评分：8/10
实用的模型压缩方法，实验充分，在有限数据预算下训练出高质量小模型。工程价值高，已开源可复现。

---

### [3] CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis with Nonlinear Chaotic Losses

**arXiv ID** 2607.18629 | **方向** 语音大模型 / EMG转语音

**作者** Sajid Fardin Dipto, Tarikul Islam Tamiti, David Vergano, Luke Baja-Ricketts, Anomadarshi Barua

**机构** 需确认

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18629 | **PDF** https://arxiv.org/pdf/2607.18629.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出CS-ETS，首个将混沌理论融入EMG转语音的架构。使用Samba-based编码器和两个混沌启发的损失函数（LER和MSDFA），在参数减少40.79%的情况下，性能超过之前最佳方法。

### 🔧 技术方案

**模型架构** 修改的Samba架构（去除第一个MLP子层），使用CFE块提取特征。Mamba-SWA-MLP编码器4层，输出80维mel spectrogram。使用HiFi-GAN vocoder。

**核心创新** 混沌理论损失：Lyapunov指数正则化（LER）捕捉非线性波动和初始条件敏感性；多尺度去趋势波动分析（MSDFA）量化分形-like长程时间相关性。后置Vocoder对齐（PVA）：首次在ETS中实现帧级指标计算。

**训练策略** 80 epochs，batch size 32，AdamW lr=1e-3，weight decay=1e-7，梯度裁剪norm 0.5。2×RTX 4090 GPU。

### 📊 实验结果
**数据集** Gaddy数据集（19小时面部EMG数据）

**主要指标** LSD降低2.1倍（1.07 vs 2.25），STOI提升4.7倍（0.61 vs 0.13），SI-SDR提升1.25倍（-33.41 vs -41.96）。参数减少40.79%（32M vs 54.1M），FLOPs减少13.33%。MOS：CS-ETS 4.21 vs 基线3.98。

**是否开源** 部分开源

### ⭐ 评分：7/10
创新性强，首次将混沌理论引入EMG转语音，方法新颖。参数大幅减少但性能提升，实验较充分。

---

### [4] Summary of DCASE 2026 Task 5: Audio-Dependent Question Answering

**arXiv ID** 2607.18718 | **方向** 语音大模型 / 音频问答

**作者** Haolin He, Renhe Sun, Zheqi Dai等（14个团队36个提交）

**机构** 多机构

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18718 | **PDF** https://arxiv.org/pdf/2607.18718.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
DCASE 2026 Task 5引入音频依赖问答（ADQA），测试大型音频语言模型是否真正从音频而非文本先验回答问题。通过音频依赖过滤（ADF）管道构建3000项评估集。14个团队提交36个系统，冠军达到58.33%准确率。

### 🔧 技术方案

**模型架构** 使用多种LALM作为backbone：MOSS-Audio-8B-Thinking（13个提交），Qwen3-Omni-30B（5个提交）等。技术：LoRA微调、SFT、GRPO、GDPO、prompt工程、投票集成。

**核心创新** ADF管道：四阶段过滤（Hard-ADF静默探测、Soft-ADF困惑度过滤、LLM常识检查、人工验证）移除可从文本解决的问题。获胜系统Lim_CAU：MOSS+Qwen3-Omni集成 + GDPO-based LoRA + 声学tagger + choice-permutation集成。

**训练策略** 训练集：AudioMCQ-StrongAC-GeminiCoT（约571k项）。评估集：3000项通过ADF的音频问答。

### 📊 实验结果
**数据集** 3000项ADQA-Bench评估集

**主要指标** 冠军系统：Lim_CAU_4达到58.33%（总体）和57.30%（<10B轻量级）。最佳基线Qwen3-Omni-30B在开发集62.48%。开发到评估准确率平均下降11.91pp。常见技术：MOSS-Audio-8B-Thinking backbone（13/36提交），LoRA（9队），CoT提示（9队），GRPO（5队）。

**是否开源** 部分开源

### ⭐ 评分：7/10
任务设置有意义，推动音频问答从音频而非文本回答。技术方案多样，实验规模大。评分基于任务贡献而非单一方法创新。

---

### [5] Fretiq: Browser-Native Electric Guitar String Classification via Engineered Spectral Features and Held-Out Free-Play Evaluation

**arXiv ID** 2607.18303 | **方向** 语音大模型 / 音频分类

**作者** Aadi Garg

**机构** 需确认

**发布日期** 2026-07-18 | **论文** https://arxiv.org/abs/2607.18303 | **PDF** https://arxiv.org/pdf/2607.18303.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Fretiq是一个浏览器原生的电吉他弦分类系统，使用26维特征表示（频带能量、频谱统计、13维MFCC），在322215个平衡帧上达到97.1%验证准确率。引入比较训练方法，并进行103000帧的自由演奏评估。

### 🔧 技术方案

**模型架构** 26维特征：频带能量、频谱统计、13维MFCC。Python和TypeScript特征提取管道保证训练推理一致性。

**核心创新** 比较训练：相邻开放弦和五品弦对交替录制。消融实验：MFCC是主要准确率驱动（92.2%→97.1%）。

**训练策略** 322215个平衡帧，97.1% shuffled frame-level验证准确率。103000帧自由演奏评估：87.8%准确率。

### 📊 实验结果
**数据集** 322215训练帧，103000评估帧

**主要指标** 验证准确率97.1%，自由演奏准确率87.8%，D3到A2混淆降低44%。

**是否开源** 部分开源

### ⭐ 评分：6/10
工程性工作，浏览器端实现有创新，数据集规模较大但方向相对小众。

---

## 🎙️ 语音前端

### [1] Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution

**arXiv ID** 2607.18658 | **方向** 语音前端 / 语音增强

**作者** Zhenglong Liu, Wangyou Zhang, Chenda Li, Yanmin Qian

**机构** 上海交通大学 Auditory Cognition and Computational Acoustics Lab，VUI Labs

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18658 | **PDF** https://arxiv.org/pdf/2607.18658.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出几何感知动态卷积（Geo-DConv）框架，用于实现阵列不变语音增强。该方法显式利用麦克风坐标将标准固定阵列SE模型转换为鲁棒的阵列不变系统。实验在RealMAN真实录制多通道语音数据集上进行。

### 🔧 技术方案

**模型架构** Geo-DConv层处理任意数量麦克风输入。TACT模块使用Fourier位置编码和Transformer编码器建模全局阵列拓扑。动态卷积权重由基础核线性组合生成。

**核心创新** 几何感知动态卷积：显式利用阵列几何信息。TACT模块：排列等变性和稳定性。固定阵列模型到阵列不变系统的通用适配器。

**训练策略** RealMAN数据集（83.7小时多通道语音），重采样8kHz，256点窗128帧移。SpatialNet-Geo-DConv和TF-GridNet-Geo-DConv两种backbone。

### 📊 实验结果
**数据集** RealMAN（真实录制多通道语音数据集），CHiME-4

**主要指标** SpatialNet-Geo-DConv：SI-SDR 4.22dB，PESQ 2.48，OVRL 2.68。TF-GridNet-Geo-DConv：SI-SDR 3.90dB，PESQ 2.59，OVRL 2.77。CHiME-4跨数据集泛化：OVRL从1.42提升到2.64/2.73。

**是否开源** 暂无

### ⭐ 评分：8/10
解决阵列不变SE的重要问题，方法创新性强（几何感知动态卷积），实验充分，在真实数据集上验证，效果显著。已中Interspeech 2026。

---

### [2] End-to-End Markov State Sequence Learning for Auditory Attention Decoding

**arXiv ID** 2607.18614 | **方向** 语音前端 / 听觉注意解码

**作者** Yushan Yashengjiang, Jie Zhang, Miao Sun, Huadong Liang, Xin Li, Zhen-Hua Ling

**机构** 中国科学技术大学，广州海事大学，科大讯飞

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18614 | **PDF** https://arxiv.org/pdf/2607.18614.pdf | **代码** https://github.com/YusanX/AAD-CRF | **Demo** 暂无

### 📌 简介
本文提出端到端Markov状态序列学习框架用于听觉注意解码（AAD）。将任意AAD backbone的logits视为Markov发射，在两状态注意先验下训练窗口级神经发射。提出ESCNet保留时间对齐特征并转换为状态logits。

### 🔧 技术方案

**模型架构** ESCNet：EEG-语音相关网络，保留时间轴。2D空间卷积+1D时间卷积提取特征。Pearson相关系数计算，两候选分数差转换为反对称状态logits。CRF联合优化交叉熵和CRF目标。

**核心创新** 端到端CRF训练：将时间连续性纳入表征学习而非仅后处理平滑。ESCNet：时间保持的EEG-语音相关backbone。联合优化转换率和发射网络。

**训练策略** 数据集：AVGC（动态注意切换），KUL和USTC（静态AAD）。窗口长度：1s/2s/4s。训练：CE warm-up + 联合CRF训练。

### 📊 实验结果
**数据集** AVGC（1313参与者），KUL（16参与者），USTC（18参与者）

**主要指标** AVGC动态AAD：CRF-Causal 86.5%，CRF-NC 92.4%（1s窗口）。静态KUL/USTC：因果解码相比post-hoc HMM基线提升5.6%/2.0%。

**是否开源** 已开源：https://github.com/YusanX/AAD-CRF

### ⭐ 评分：8/10
方法创新性强，将AAD表述为注意力状态序列估计，实验规模大（多数据集多参与者），开源可复现。

---

### [3] Addressing Limited Data in Auditory Attention Decoding with Diffusion Generative Models

**arXiv ID** 2607.18345 | **方向** 语音前端 / 听觉注意解码

**作者** David Rannaleet, Victor Gunnarsson, Bo Bernhardsson, Martin A. Skoglund, Emina Alickovic

**机构** 需确认

**发布日期** 2026-07-18 | **论文** https://arxiv.org/abs/2607.18345 | **PDF** https://arxiv.org/pdf/2607.18345.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
研究扩散概率模型（DPM）用于生成合成语音诱发EEG数据，以解决助听器AAD中训练数据有限的问题。DPM学习复杂数据结构，可生成用于数据增强的真实样本。

### 🔧 技术方案

**模型架构** 使用扩散概率模型生成合成语音诱发EEG数据。

**核心创新** 探索DPM用于AAD中的数据增强。评估合成EEG数据对locus-of-attention（LoA）分类任务的影响。

**训练策略** 合成数据增强训练。

### 📊 实验结果
**数据集** 语音诱发EEG数据

**主要指标** DPM可生成真实EEG信号，合成数据显著提升AAD性能（p<0.05）。

**是否开源** 暂无

### ⭐ 评分：6/10
数据增强思路，但实验结果和具体方法描述较少。

---

### [4] StemFX: Learning Mixing Style Representations via Autoregressive FX Chain Prediction on Source-Separated Stems

**arXiv ID** 2607.15634 | **方向** 语音前端 / 音频混音

**作者** Yuan-Chiao Cheng, Jui-Te Wu, Brian Chen, Yen-Tung Yeh, Yu-Hua Chen, Yi-Hsuan Yang

**机构** 需确认

**发布日期** 2026-07-19 | **论文** https://arxiv.org/abs/2607.15634 | **PDF** https://arxiv.org/pdf/2607.15634.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
StemFX通过自回归预测源分离stem上的FX链来学习混音风格表示。Transformer解码器自回归预测tokenized FX链，band-split multi-band CNN encoder with FiLM conditioning捕获每stem频谱结构。

### 🔧 技术方案

**模型架构** Transformer解码器自回归预测FX链。Band-split multi-band CNN encoder with FiLM conditioning。使用MultiAFx工具包增强（85个音频效果，7个Python库）。

**核心创新** 端到端可变长度FX链预测。从约105K歌曲提取伪stem训练。

**训练策略** 约105K歌曲伪stem + MultiAFx增强。

### 📊 实验结果
**数据集** 约105K歌曲

**主要指标** 混音风格检索和配对风格迁移均优于基线。推理速度比迭代优化快4000倍+。

**是否开源** 暂无

### ⭐ 评分：7/10
创新性强，方法系统完整，在大规模数据上验证，已中ISMIR 2026。

---

### [5] GigaSpeechBench: A Real-World Multilingual Speech-to-Text Benchmark

**arXiv ID** 2606.28884 | **方向** 语音前端 / ASR

**作者** Yujie Tu, Yifan Yang等（大量作者）

**机构** 多机构

**发布日期** 2026-06-?? | **论文** https://arxiv.org/abs/2606.28884 | **PDF** https://arxiv.org/pdf/2606.28884.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
GigaSpeechBench是一个综合的多语言多维度野生ASR&AST基准，包含680小时人工标注语音。覆盖12种低资源中东和东南亚语言、6种中文方言、6种英语口音、12个垂直领域术语、老年人和儿童语音。

### 🔧 技术方案

**模型架构** 基准构建：5个模块覆盖多语言、多方言、多口音、多领域、年龄变体。

**核心创新** 多维度挑战评估：领域术语、年龄变体、口音、低资源语言。提供11种语言的人工标注中英文翻译支持AST评估。

**训练策略** 680小时人工标注。

### 📊 实验结果
**数据集** 680小时，12低资源语言+6中文方言+6英语口音+12垂直领域+老幼语音

**主要指标** 现有顶级模型和商业API在此基准上性能显著下降，暴露关键评估盲点。

**是否开源** 暂无

### ⭐ 评分：7/10
基准构建工作有价值，推动ASR在真实场景的鲁棒性评估。

---

### [6] Acoustic Simulation Framework for Multi-channel Replay Speech Detection

**arXiv ID** 2509.14789 | **方向** 语音前端 / 回放语音检测

**作者** Michael Neri, Tuomas Virtanen

**机构** 需确认

**发布日期** 2025-09-?? | **论文** https://arxiv.org/abs/2509.14789 | **PDF** https://arxiv.pdf/2509.14789.pdf | **代码** https://github.com/michaelneri/synthetic-ReMASC | **Demo** 暂无

### 📌 简介
提出多通道回放语音检测的声学模拟框架。使用公开资源模拟多通道回放语音配置。训练M-ALRAD并评估在ReMASC真实录制语料库上的泛化。

### 🔧 技术方案

**模型架构** M-ALRAD扩展：相邻麦克风对的通道间相位差特征。

**核心创新** 声学模拟框架：模拟多通道回放语音配置。空间信息利用。

**训练策略** 合成数据集训练，真实数据评估。

### 📊 实验结果
**数据集** 合成ReMASC，ReMASC真实录制

**主要指标** 框架可生成多样化声学条件的合成数据。合成数据集已发布。

**是否开源** 已开源：https://github.com/michaelneri/synthetic-ReMASC

### ⭐ 评分：6/10
工程性工作，数据模拟框架有价值，已中IEEE MMSP 2026。

---

### [7] What does the model actually see? Evaluation protocols and input availability in data-driven prediction of room acoustic parameters

**arXiv ID** 2607.15243 | **方向** 语音前端 / 房间声学

**作者** Akın Oktav

**机构** 需确认

**发布日期** 2026-07-?? | **论文** https://arxiv.org/abs/2607.15243 | **PDF** https://arxiv.pdf/2607.15243.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文揭示机器学习模型预测ISO 3382-1房间声学参数的准确性往往由评估协议而非模型本身决定。通过264座会议厅和180座音乐厅的实测，分析协议对结果的影响。

### 🔧 技术方案

**模型架构** 评估协议消融：验证 splits（row-based vs position-grouped），输入特征（measured-at-test vs geometry-only）。

**核心创新** 揭示评估协议对结果的显著影响。区分位置指纹vs可迁移声学信息。

**训练策略** 多条件测量campaign。

### 📊 实验结果
**数据集** 264座会议厅，180座音乐厅

**主要指标** Row-based splits + measured-at-test输入：R² 0.81。Position-grouped + geometry-only：R² 0.09-0.57。部署一致协议下，模型在测点条件插值上R² 0.80-0.88。

**是否开源** 暂无

### ⭐ 评分：7/10
重要的方法论贡献，揭示评估协议问题，对后续研究有指导意义。

---

### [8] A Situational Speech Synthesizer for Yoruba: System Design, Phonological Rule Architecture, and Orthographic Extensions for Contour

**arXiv ID** 2607.18317 | **方向** 语音前端 / TTS

**作者** Kola Tubosun, Adedayo Oluokun, Hafiz Adewuyi, Dadepo Aderemi

**机构** 需确认

**发布日期** 2026-07-18 | **论文** https://arxiv.org/abs/2607.18317 | **PDF** https://arxiv.pdf/2607.18317.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
TTSYoruba是约鲁巴语的规则拼接音素合成系统。系统接受带声调标记的约鲁巴语文本输出音频，应用手写音韵规则系统到651个双音素单元库。

### 🔧 技术方案

**模型架构** 规则拼接双音素合成。651个双音素单元，5种声调变体。

**核心创新** 完整声调文件选择逻辑。三向鼻音消歧（oral /n/, 鼻化元音, 音节鼻音）。从平调输入派生升调和降调。

**训练策略** 50人监听study，MOS评估。

### 📊 实验结果
**数据集** 651双音素单元

**主要指标** MOS结果见Section 6。

**是否开源** 部分开源（系统部署在YorubaName.com）

### ⭐ 评分：6/10
低资源语言TTS有价值，但方法相对传统。

---

## 📋 其他论文（快速浏览）

### 语音大模型
## [1] Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio
**arXiv ID**: 2607.18666 | **评分**: 6/10
**链接**: https://arxiv.org/abs/2607.18666

## [2] Teleportation Game: Quantum Teleportation in Multi-Agent Systems for Interactive Music
**arXiv ID**: 2607.19212 | **评分**: 4/10
**链接**: https://arxiv.org/abs/2607.19212

## [3] Memo2496: Expert-Annotated Dataset and Dual-view Adaptive Framework for Music Emotion Recognition
**arXiv ID**: 2512.13998 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2512.13998

### 语音前端
## [1] Auto-AEG: Scalable Data Construction for Open-Vocabulary Audio Event Grounding
**arXiv ID**: 2607.04383 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.04383

## [2] Towards a reproducible cross-venue method for quantifying crowd noise in stadiums
**arXiv ID**: 2607.18922 | **评分**: 4/10
**链接**: https://arxiv.org/abs/2607.18922

## [3] Caption Studio: Transparent-first Speech and Audio Intelligence
**arXiv ID**: 2607.18704 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.18704

---

*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*
