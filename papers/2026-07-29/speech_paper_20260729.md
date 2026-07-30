# 2026-07-29 语音论文速递

**共收录**: 10 篇 | **语音大模型**: 3 篇 | **语音前端**: 3 篇 | **医学语音**: 1 篇 | **其他**: 3 篇

> 今日 arXiv 语音相关论文共命中 10 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

### [1] From Semantics to Readout: Mechanistic Understanding of Audio Tokens after Fine-Tuning for Temporal Audio Grounding

**arXiv ID**：2607.25355 | **方向**：语音大模型

**作者**：Yujian Ma, Jinqiu Sang, Ruizhe Li, Jiaao Yu, Ang Li

**机构**：上海交通大学

**发布日期**：2026-07-28 | **论文**：https://arxiv.org/abs/2607.25355 | **PDF**：https://arxiv.org/pdf/2607.25355.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文对大语言音频模型（LALM）中的音频token进行机制分析，研究微调如何影响音频token的语义表示和解码器可读性。以时间音频定位为诊断设置，通过四种互补分析方法揭示微调前后音频token状态的变化。

### 🔧 技术方案
**模型架构**：基于Qwen2.5-Omni和Qwen2-Audio-7B-Instruct，使用LoRA微调。分析框架包括：查询条件token语义、校准token readout、时间窗口探测和生成时残差擦除。

**核心创新**：提出语义到readout账户：基础模型已包含潜在事件证据，微调主要改善解码器对现有证据的读取能力，而非创建新证据。跨检查点控制显示增益主要来自解码器适应。

**训练策略**：在AudioGrounding-QA数据集上训练，使用LoRA适配器仅应用于语言模型transformer块，音频塔和投影仪保持冻结。

### 📊 实验结果
**数据集**：AudioGrounding-QA（9542/1052/992 QA实例）

**主要指标**：Qwen2.5-Omni微调后：mIoU从0.3707提升到0.6817，F1从0.4416提升到0.7626，R@0.7从0.2349提升到0.5817。

**是否开源**：代码未开源

**评分**：8/10
创新性高，首次系统分析LALM音频token内部机制，实验充分，结论有价值。对理解语音大模型工作原理有重要贡献。

---

### [2] Text-Prompted CLAP: Learning Query-Conditioned Audio Representations via Contrastive Learning

**arXiv ID**：2607.25085 | **方向**：音频理解

**作者**：Mohan Li, Rama Doddipatla, Philip C. Woodland

**机构**：University of Cambridge, Amazon

**发布日期**：2026-07-27 | **论文**：https://arxiv.org/abs/2607.25085 | **PDF**：https://arxiv.org/pdf/2607.25085.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出Text-Prompted CLAP (TP-CLAP)，通过跨注意力融合模块将文本提示融入音频特征，学习查询条件音频表示。使用音频多选题框架进行对比学习，在音频问答、检索和零样本分类任务上取得竞争力性能。

### 🔧 技术方案
**模型架构**：基于CLAP backbone，使用CED-Base音频编码器和bert-base-uncased文本编码器。融合模块包含L=2个跨注意力块。

**核心创新**：提出跨注意力融合模块，使音频表示能够根据文本查询进行动态调整。引入音频-MCQ监督框架，学习查询条件表示而不需要多模态LLM。

**训练策略**：在AudioCaps-v2、Clotho、WavCaps等数据集上预训练，然后在AudioMCQ上训练。使用两阶段训练：先冻结CLAP编码器仅训练融合模块，然后联合微调所有参数。

### 📊 实验结果
**数据集**：AudioCaps、Clotho、MMAU、MMAR、NSynth、MagnaTagATune

**主要指标**：音频问答：TP-CLAP在MMAU上达到71.47%准确率（sound）和55.99%（music），优于CLAP+AudioMCQ的64.56%和52.99%。

**是否开源**：代码未开源

**评分**：7/10
参数高效的方法，在多个任务上取得竞争性性能。创新性较好，实验充分，适用于资源受限场景。

---

### [3] Unlocking Spatial Grounding in Large Audio-Visual Retrieval models

**arXiv ID**：2607.24786 | **方向**：音频视觉定位

**作者**：Hugo Malard, Michel Olvera, Sanjeel Parekh, Gaël Richard, Slim Essid, Stéphane Lathuilière

**机构**：LTCI, Télécom Paris, Institut Polytechnique de Paris; Meta Reality Labs Research; NVIDIA France; Inria Grenoble Alpes

**发布日期**：2026-07-22 | **论文**：https://arxiv.org/abs/2607.24786 | **PDF**：https://arxiv.org/pdf/2607.24786.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出LAIP框架，证明大规模音频视觉检索模型可以适配为有效的声源定位器，无需密集空间监督。核心观点是中间层视觉token保留了结构化空间信息，通过音频信息空间池化（AiSP）模块可恢复定位能力。

### 🔧 技术方案
**模型架构**：基于PE-AV检索 backbone，添加音频信息空间池化（AiSP）模块。采用三层分级设计，逐步将空间token池化为音频条件token。

**核心创新**：提出Audio-informed Spatial Pooling (AiSP)，使用音频查询中间视觉token。多分辨率正则化确保注意力图空间一致性。可学习null token处理不相关情况。

**训练策略**：使用SigLIP风格对比目标，仅训练新增的AiSP模块和视频编码器适配器。训练10个epoch，lr=1e-4。

### 📊 实验结果
**数据集**：AVATAR、AVSBench、ADE-SP

**主要指标**：AVATAR：CIoU达到27.63%（single-sound）、27.35%（mixed-sound）、23.69%（multi-entity），相比TAVLO提升约10个百分点。AVSBench S4：F-score达到65.18%。

**是否开源**：代码未开源

**评分**：8/10
创新性强，首次证明检索模型可解锁定位能力。实验充分，在多个基准上取得SOTA性能。工程价值高。

---

## 🎙️ 语音前端

### [4] faster-enhancer.c: A Dependency-Free int8 Runtime for Streaming Speech Enhancement on Commodity CPUs

**arXiv ID**：2607.25350 | **方向**：语音增强

**作者**：Gyeongmin Kim

**机构**：暂无

**发布日期**：2026-07-28 | **论文**：https://arxiv.org/abs/2607.25350 | **PDF**：https://arxiv.org/pdf/2607.25350.pdf | **代码**：https://github.com/kdrkdrkdr/faster-enhancer.c | **Demo**：暂无

### 📌 简介
本文是语音增强模型FastEnhancer-Medium的int8推理runtime实现。研究在商品CPU上运行流式语音增强的成本，实现在Apple M2上达到0.069实时因子（3.3x加速），Galaxy S23+达到0.096。量化后质量损失极小（PESQ -0.006，SNR -0.08dB）。

### 🔧 技术方案
**模型架构**：FastEnhancer-Medium 48kHz，6层int8 GEMM tiers，Winograd F(2,3)卷积，fp16跨级状态。

**核心创新**：无需校准集的per-frame激活范围重计算；Winograd卷积加速；GRU和反量化融合；启动后零内存分配。6层SIMD tiers：ARM NEON、DOTPROD、I8MM、x86 AVX2、AVX-VNNI、AVX-512 VNNI。

**训练策略**：训练-free int8移植，保持模型架构和权重不变。

### 📊 实验结果
**数据集**：VoiceBank-DEMAND（824 utterances）

**主要指标**：Apple M2: RTF 0.069 vs fp32 ONNX 0.230 (3.3x加速)；Galaxy S23+: RTF 0.096。量化损失：PESQ -0.006，SNR -0.08dB。节拍 pacing 节省49%能量。

**是否开源**：已开源：https://github.com/kdrkdrkdr/faster-enhancer.c

**评分**：9/10
工程突破性工作，实用价值极高。首次实现商品CPU上实时48kHz增强，质量损失可忽略。创新性强，代码已开源。

---

### [5] VAD to the Bone: Ultra-Tiny Speech Activity Detection for Edge Deployment

**arXiv ID**：2607.25870 | **方向**：VAD

**作者**：Stephen Bauer, Sheila Seidel, Shanza Iftikhar, Scott Veidenheimer, Gorkem Ulkar

**机构**：Analog Devices, Inc.; University of California, Los Angeles (UCLA)

**发布日期**：2026-07-28 | **论文**：https://arxiv.org/abs/2607.25870 | **PDF**：https://arxiv.org/pdf/2607.25870.pdf | **代码**：https://huggingface.co/spaces/kiloVAD-demo/kiloVAD | **Demo**：https://huggingface.co/spaces/kiloVAD-demo/kiloVAD

### 📌 简介
本文提出kiloVAD，一个面向边缘部署的超小型VAD模型。参数仅2.1k，在200ms输入上下文下达到0.850 AUC，是首个满足所有四个部署要求（前端兼容、可移植、低延迟、因果评估）的模型。

### 🔧 技术方案
**模型架构**：CNN-only架构，使用标准Mel频谱图特征。包含适配器层、深度可分离卷积块、残差块、膨胀块、全局平均池化和二分类器。

**核心创新**：Per-layer结构化剪枝+自蒸馏；Angle-based自蒸馏QAT，优于标准QAT 1-4%。无GRU、无可学习滤波器库、无非因果后处理。

**训练策略**：在LibriSpeech train-clean-100上训练，使用三种噪声条件。Per-layer剪枝通过Optuna多目标搜索优化。

### 📊 实验结果
**数据集**：AVA-Speech

**主要指标**：2.1k参数 pruned模型：AVA-Speech AUC 0.850，F1 0.783。INT8量化后保持0.851 AUC（无损失）。200ms输入延迟。

**是否开源**：已开源：https://huggingface.co/spaces/kiloVAD-demo/kiloVAD

**评分**：9/10
突破性工作，参数极少（2.1k）且满足所有部署要求。创新性高，实验充分，开源且有demo。

---

### [6] Towards Operational Conversational Intelligence: A Speech Intelligence Framework

**arXiv ID**：2607.24958 | **方向**：ASR/对话智能

**作者**：Chaitanya Vishnoi, Shudhant Khurana, Abhilash Timmapur, Somya Rai, Saket Mohanty

**机构**：Indian Institute of Technology Kanpur; EXL

**发布日期**：2026-07-27 | **论文**：https://arxiv.org/abs/2607.24958 | **PDF**：https://arxiv.org/pdf/2607.24958.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出用于执法记录仪（BWC）音频的双路径对话智能框架，解决高环境噪声、多说话人重叠等挑战。框架整合语音活动检测、说话人 diarization、自动语音识别和说话人归因。

### 🔧 技术方案
**模型架构**：双路径架构：diarization路径使用DeepFilterNet+Pyannote VAD+NVIDIA MSDD+TitaNet；ASR路径使用loudness normalization+WhisperX。

**核心创新**：提出"增强陷阱"概念：神经增强对diarization有益但损害ASR。概率引导VAD后处理，使用Pyannote语音概率进行分段。基于最大时间重叠的说话人归因融合。

**训练策略**：使用公开的BWC风格数据集评估（8个录音，31分钟，41个说话人）。各组件使用预训练模型。

### 📊 实验结果
**数据集**：自建BWC数据集（8个录音，31分钟）

**主要指标**：报告了VAD、diarization、ASR和说话人归因的组件级评估结果，验证了任务特定声学条件和概率引导分割的有效性。

**是否开源**：框架组件均为公开模型，但整体pipeline未开源

**评分**：7/10
针对实际应用场景的实用系统，创新性地解决增强陷阱问题。实验基于真实数据，但数据集规模有限。

---

## 🏥 医学语音

### [7] Multi-Phonation Graph Learning with Self-Supervised Speech Embeddings for ALS Detection and Progression Prediction

**arXiv ID**：2607.25284 | **方向**：医学语音/ALS检测

**作者**：Behrad TaghiBeyglou, Fatemeh Bagheri, Ervin Sejdic

**机构**：University of Toronto; North York General Hospital

**发布日期**：2026-07-28 | **论文**：https://arxiv.org/abs/2607.25284 | **PDF**：https://arxiv.org/pdf/2607.25284.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出使用自监督学习（SSL）嵌入和图神经网络（GNN）进行ALS（肌萎缩侧索硬化症）检测和进展预测。将受试者的多个发声录音聚合为k近邻图，在SAND数据集上取得优异性能。

### 🔧 技术方案
**模型架构**：Subject-level图框架：使用SSL嵌入（wav2vec 2.0、HuBERT、data2vec-audio、UniSpeech-SAT）提取2秒片段特征，构建kNN图，使用GNN（GCN、ResGCN、GAT、GraphSAGE、GIN）进行图分类。

**核心创新**：提出subject-level图公式，将多个录音建模为统一表示。系统评估4种SSL前端的5种GNN架构。HuBERT+GIN组合表现最佳。

**训练策略**：在SAND数据集训练（339 participants: 205 ALS, 134 control）。10折交叉验证选择超参数。

### 📊 实验结果
**数据集**：SAND Challenge数据集

**主要指标**：HuBERT+GIN：Task 1（5类严重程度）mF1=0.73，Task 2（4类ALSFRS-R进展预测）mF1=0.69。相比SAND验证基线（0.61和0.58）显著提升。

**是否开源**：代码未开源

**评分**：8/10
创新地将图学习应用于ALS检测，实验系统充分，在两个任务上均超越基线。方法新颖，有临床应用价值。

---

## 🔬 其他语音技术

### [8] Extracting Voice Styles from Frozen TTS Models via Gradient-Based Inverse Optimization

**arXiv ID**：2607.25351 | **方向**：TTS/声纹

**作者**：Gyeongmin Kim

**机构**：暂无

**发布日期**：2026-07-28 | **论文**：https://arxiv.org/abs/2607.25351 | **PDF**：https://arxiv.org/pdf/2607.25351.pdf | **代码**：https://github.com/kdrkdrkdr/supertonic.embed | **Demo**：暂无

### 📌 简介
针对TTS系统只发布合成模型和预设风格向量但不发布参考编码器的问题，本文提出通过梯度下降直接优化风格向量，从冻结的TTS模型中提取语音风格。使用WavLM统计作为目标，无需转录和对齐。

### 🔧 技术方案
**模型架构**：基于SupertonicTTS 2，风格向量s∈R^(50×256)，共12800参数。

**核心创新**：无需参考编码器，通过优化风格向量匹配目标语音的WavLM层4统计量。内容无关目标函数使用时间池化的mean和std。停止阈值0.30通过预设合成内容差异校准。

**训练策略**：冻结所有TTS和WavLM权重，仅优化风格向量。5个英语提示轮换，Adam优化器，lr=2e-4。

### 📊 实验结果
**数据集**：VCTK（110 speakers）、Common Voice Seed-TTS Eval（44 speakers）

**主要指标**：ECAPA相似度从0.132提升到0.413，ResNet从0.099提升到0.401。每个说话人都有提升。验证器在EER点接受53%的提取声音 vs 预设的1%。

**是否开源**：已开源：https://github.com/kdrkdrkdr/supertonic.embed

**评分**：8/10
创新性问题解决方法，实验规模大（154说话人），开源且有明确应用价值。对TTS模型安全性有启示。

---

### [9] Device Invariance using Domain Adaptation on Acoustic Scene Classification

**arXiv ID**：2607.25887 | **方向**：声学场景分类

**作者**：Abhishek Dileep, Shubham Sharma, Padmanabhan Rajan

**机构**：暂无

**发布日期**：2026-07-28 | **论文**：https://arxiv.org/abs/2607.25887 | **PDF**：https://arxiv.org/pdf/2607.25887.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文探索领域适应方法在声学场景分类（ASC）中处理设备不匹配问题的有效性。对比DANN和CDAN两种方法在CNN和Transformer特征提取器上的表现。

### 🔧 技术方案
**特征提取器** PaSST (Transformer)、DcaseNet (CNN)、Custom CNN三种特征提取器。

**领域适应方法** DANN（域对抗神经网络）和CDAN（条件域对抗网络）。

**核心创新**：发现DANN在所有特征提取器上提供一致有效的领域适应；CDAN仅在CNN特征提取器上有效，对Transformer（PaSST）失效。原因可能与ViT的动态特征和分类器伪标签相关。

### 📊 实验结果
**数据集**：DCASE 2020 Task 1A（设备A为源，其他设备为目标）

**主要指标**：PaSST：源准确率0.845，域移后0.61-0.65，DANN提升至0.65-0.74。DcaseNet：DANN提升10.9%，CDAN提升11.5%。Custom CNN：CDAN提升11.8%。

**是否开源**：代码未开源

**评分**：6/10
实验充分，揭示了领域适应方法与特征提取器类型的重要关系。创新性中等但有实践指导价值。

---

### [10] Time-Frequency Consistency Learning for Robust Speech Deepfake Detection

**arXiv ID**：2607.17761 | **方向**：语音深度伪造检测

**作者**：Jun Xue, Zhuolin Yi, Yanzhen Ren, Yihuan Huang, Jiayu Xiong, Yi Chai, Guanxiang Feng, Jiajun Liu, Tong Zhang

**机构**：武汉大学；同济大学

**发布日期**：2026-07-20 | **论文**：https://arxiv.org/abs/2607.17761 | **PDF**：https://arxiv.org/pdf/2607.17761.pdf | **代码**：https://github.com/JunXue-tech/TFCL | **Demo**：暂无

### 📌 简介
本文针对语音深度伪造检测（SDD）在现实声学前端（AFE）处理下的鲁棒性问题。提出时频一致性学习（TFCL）框架，学习在AFE处理前后保持稳定的伪造表示。

### 🔧 技术方案
**模型架构**：基于AASIST后端分类器，结合时频一致性学习模块。

**核心创新**：时域：注意力驱动的软对齐机制捕获跨时间依赖；频域：频域结构一致性约束保持特征不变。AFE处理包括AEC、NS、AGC、VAD级联。

**训练策略**：使用ASVspoof2019 LA数据集，结合模拟AFE处理进行训练。

### 📊 实验结果
**数据集**：ASVspoof2019 LA

**主要指标**：在完整AFE pipeline下：EER 9.78%，AUC 96.40%，显著优于所有基线方法。干净条件下：EER 0.55%，AUC 99.96%。在各种AFE条件下一致提升。

**是否开源**：已开源：https://github.com/JunXue-tech/TFCL

**评分**：8/10
创新性地将AFE处理引入SDD鲁棒性评估，提出有效解决方案。实验系统充分，在真实场景有重要应用价值。

---

## 📋 其他论文（快速浏览）

### 语音大模型
无

### 语音前端
无

---

*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*
