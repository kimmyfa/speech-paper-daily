# 2026-07-21 语音论文速递

**共收录**: 5 篇 | **语音大模型**: 1 篇 | **语音前端**: 4 篇

> 今日 arXiv 语音相关论文共命中 5 篇。
> 以下是按评分排序的结果。

---

## 🎙️ 语音前端

### 1. CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis with Nonlinear Chaotic Losses

**arXiv ID** 2607.18629 | **方向** 语音合成

**作者** Sajid Fardin Dipto, Tarikul Islam Tamiti, David Vergano, Luke Baja-Ricketts, Anomadarshi Barua

**机构** （论文未提供机构信息）

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18629 | **PDF** https://arxiv.org/pdf/2607.18629.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出CS-ETS，一种基于混沌激发的EMG-to-Speech (ETS) 合成架构。该方法结合Samba编码器和两种新型混沌损失函数：Lyapunov指数正则化(LER)和多尺度去趋势波动分析(MSDFA)。LER用于捕捉非线性波动和初始条件敏感性，MSDFA利用去趋势波动分析量化分形-like的长程时间混沌相关性。

### 🔧 技术方案

**模型架构** CS-ETS采用Samba-based编码器架构，包含EMG信号处理主干和语音合成解码器。整体参数量32M，相比之前54.1M模型减少40.79%。

**核心创新** 提出两种混沌损失函数：Lyapunov指数正则化(LER)通过计算Lyapunov指数捕捉系统对初始条件的敏感性；多尺度去趋势波动分析(MSDFA)量化分形-like的长程时间相关性。此外引入Post-Vocoder Alignment方法解决声学模型与声码器对齐问题。

**训练策略** 训练使用多尺度损失组合，包括Lyapunov指数正则化损失、MSDFA损失和传统重建损失。模型在EMG-speech配对数据上端到端训练。

### 📊 实验结果

**数据集** EMG-speech数据集

**主要指标** 相比之前最佳模型：LSD降低2.1倍，STOI提升4.7倍，SI-SDR提升1.25倍。参数量减少40.79% (32M vs 54.1M)，计算量减少13.33%。

**是否开源** 代码暂未开源

### ⭐ 评分：8/10
创新性地将混沌理论引入EMG-to-Speech合成，使用Lyapunov指数和分形分析捕捉非线性语音特征。实验结果显著提升且模型更轻量，有望推动可穿戴设备语音合成应用。

---

### 2. Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution

**arXiv ID** 2607.18658 | **方向** 语音增强

**作者** Zhenglong Liu, Wangyou Zhang, Chenda Li, Yanmin Qian

**机构** （论文未提供机构信息）

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18658 | **PDF** https://arxiv.org/pdf/2607.18658.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
多通道语音增强(SE)系统相比单通道方法性能更优，但受限于固定麦克风阵列配置，限制了其在具有不同阵列几何形状的设备上的实际部署。现有的阵列无关SE方法虽能处理可变麦克风数量和排列，但未能充分利用可用的显式阵列几何先验信息。

### 🔧 技术方案

**模型架构** 提出Geometry-Aware Dynamic Convolution (Geo-DConv)框架，包含两个核心模块：Geo-DConv动态卷积模块和Topology-Aware Coordinate Transformer (TACT)模块。

**核心创新** 显式利用麦克风坐标信息，将标准固定阵列SE模型转换为鲁棒的阵列无关系统。通过Fourier位置编码将相对坐标变换为编码表示，TACT模块生成动态变换矩阵，通过矩阵乘法动态调整固定维度卷积核权重以适应目标阵列配置。

**训练策略** 整体框架包含编码器-解码器结构，使用复数域特征表示。训练采用语音增强标准损失函数，结合几何感知适配模块的辅助损失。

### 📊 实验结果

**数据集** RealMAN多通道语音数据集（真实录制）

**主要指标** 实验表明，所提架构使两种广泛使用的固定阵列模型能够适应阵列无关设置，在不同阵列拓扑上实现一致的性能提升。

**是否开源** 代码暂未开源

### ⭐ 评分：7/10
针对实际部署中阵列几何多样性挑战，提出几何感知的动态卷积方法，有较强实用价值。实验在真实数据集上验证了有效性。

---

### 3. What the Waveform Knows: Transparent-first Speech and Audio Intelligence with Caption Studio

**arXiv ID** 2607.18704 | **方向** 语音/音频智能

**作者** Cheng Siong Chin, Jianhua Zhang, Mohan Venkateshkumar

**机构** （论文未提供机构信息）

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18704 | **PDF** https://arxiv.org/pdf/2607.18704.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Caption Studio是一个透明度优先的语音和音频智能平台，通过自动转录、说话人分离、语音分析、信号级音频分析和字幕生成，将口语音频和视频转换为结构化、可搜索内容。系统基于FastAPI后端和实时仪表板构建，采用三层架构设计。

### 🔧 技术方案

**模型架构** 三层架构设计：(i) 转录和分离核心基于Whisper-class自动语音识别和pyannote说话人分离；(ii) 音频智能层提取声学和语言特征，包括波形、频谱图、pitch、语速、静音、填充词频率和情感；(iii) 集成层支持数据导出和工作流集成。

**核心创新** 透明度优先框架是主要贡献，每个报告的指标都被明确标识为测量、派生或不可用，从而提高语音分析的可追踪性、可解释性和可靠性。

**训练策略** 系统集成了多个预训练模型组件，包括Whisper ASR模型、pyannote diarization模型和音频分析模型。

### 📊 实验结果

**数据集** 基准测试基于多个公开数据集

**主要指标** 系统在转录、说话人分离、音频分析等任务上进行了基准测试，展示了各模块的性能表现。

**是否开源** 代码暂未开源

### ⭐ 评分：6/10
作为系统论文，Caption Studio提供了完整的语音/音频智能解决方案。透明度优先的理念有价值，但创新性一般，更偏工程实现。

---

### 4. Summary of DCASE 2026 Task 5: Audio-Dependent Question Answering

**arXiv ID** 2607.18718 | **方向** 音频问答

**作者** Haolin He, Renhe Sun, Zheqi Dai, Xingjian Du, Chunyat Wu, Zining Liang, Zhengxi Liu, Jiahe Lei, Runbang Wang, Jiayi Zhou, Mingru Yang, Xiquan Li, Yun Chen, Xie Chen, Zhiyao Duan, Weiqiang Wang, Mark D. Plumbley, Jian Liu, Qiuqiang Kong

**机构** （论文未提供机构信息）

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18718 | **PDF** https://arxiv.org/pdf/2607.18718.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
DCASE 2026 Task 5引入Audio-Dependent Question Answering (ADQA)，测试大型音频语言模型是否真正从音频而非文本先验中回答问题。Audio-Dependency Filtering (ADF)管道结合静音音频探测、每选项困惑度、LLM常识检查和人工审查，以移除可仅从文本解决的题目。

### 🔧 技术方案

**模型架构** 任务分为两个track：参数上限100B和10B以下。参赛系统主要使用MOSS-Audio-8B-Thinking backbone (13/36提交)，结合Low-Rank Adaptation (LoRA)微调。

**核心创新** ADF管道设计：静音音频探测排除纯文本可解题目；per-option困惑度筛选；LLM常识检查进一步过滤；人工审查确保质量。3000道通过筛选的题目形成ADQA-Bench评估集。

**训练策略** 参赛队伍使用音频语言模型的指令微调，结合LoRA参数高效微调方法。

### 📊 实验结果

**数据集** ADQA-Bench评估集（3000题），涵盖音乐、语音和环境音频

**主要指标** 中端大学团队MOSS-Audio-8B-Thinking + Qwen3-Omni-30B组合达到最高总体准确率58.33%；MOSS-only配置在sub-10B轨道领先达57.30%。30个可比较提交从开发集到隐藏评估集平均下降11.91个百分点。

**是否开源** 评估代码和数据集预计开源

### ⭐ 评分：7/10
DCASE挑战赛总结论文，提出了Audio-QA新任务，设计了系统性的音频依赖过滤方法。任务设计有价值，揭示了当前音频语言模型的问题。

---

## 🤖 语音大模型

### 5. Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio

**arXiv ID** 2607.18666 | **方向** 音频嵌入/语音大模型

**作者** Abdul Basit Tonmoy, Kazi Fardinul Hoque, Md. Shahrier Islam Arham, Arman Luthra

**机构** （论文未提供机构信息）

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.18666 | **PDF** https://arxiv.org/pdf/2607.18666.pdf | **代码** https://github.com/Eximius-Labs/fusion-embedding | **Demo** https://huggingface.co/EximiusLabs/fusion-embedding-1-2b-preview

### 📌 简介
单一嵌入空间覆盖文本、图像、视频和音频，使一个索引能够服务用户可以提出的任何查询。基于视觉语言主干的嵌入模型在文本/图像/视频检索基准上领先，但完全缺乏音频；而音频-文本检索由专业系统主导，不支持其他模态。Fusion Embedding系列将音频添加到冻结的视觉语言嵌入基础中。

### 🔧 技术方案

**模型架构** 两代架构：Fusion Embedding 1训练仅16.4M参数的连接器连接冻结音频塔和冻结基础；Fusion Embedding 2增加模态门控深度适配器(44.2M参数)，该分支在文本、图像或视频输入时不执行，其输出与发布的基础位对位相同。

**核心创新** 冻结基础参数从不被更新，利用基础已绑定文本、图像、视频的特性，仅通过将音频与文本对齐就使音频-图像检索涌现，无需成对音频-视觉训练数据。设计了控制变量实验探索设计空间。

**训练策略** 在大规模音频-文本对数据上训练连接器/适配器，使用对比学习目标。训练在数小时内单GPU完成。

### 📊 实验结果

**数据集** 音频-文本检索基准

**主要指标** 两代模型均在音频-文本检索任务上达到领先性能，且因基础已绑定多模态，音频-图像检索自然涌现。训练效率高，单GPU数小时完成。

**是否开源** 代码、模型权重和评估框架均已开源：https://github.com/Eximius-Labs/fusion-embedding

### ⭐ 评分：8/10
创新性地提出冻结基础的多模态嵌入学习方法，利用预训练模型的特性实现音频模态的高效添加。设计空间探索详实，实验充分，具有较高实用价值。

---

## 📋 其他论文（快速浏览）

当日无其他语音相关论文。

---

*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*
