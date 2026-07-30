# 2026-07-29 语音论文速递

**共收录**: 10 篇 | **语音大模型**: 3 篇 | **语音前端**: 5 篇 | **医学语音**: 1 篇 | **其他**: 1 篇

> 今日 arXiv 语音相关论文共命中 10 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

## [1] From Semantics to Readout: Mechanistic Understanding of Audio Tokens after Fine-Tuning for Temporal Audio Grounding

**arXiv ID** 2607.25355 | **方向** 语音大模型

**作者：** Yujian Ma, Jinqiu Sang, Ruizhe Li, Jiaao Yu, Ang Li

**机构：** 上海交通大学

**发布日期：** 2026-07-28 | **论文** https://arxiv.org/abs/2607.25355 | **PDF** https://arxiv.org/pdf/2607.25355.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
大语言音频模型（LALM）通过原生音频token将声学证据传递给语言解码器，但这些token的内部角色仍未被深入理解。本文使用时间音频定位作为诊断设置，通过四种互补分析来研究语言模型微调如何影响原生音频token的层级语义、解码器可访问性和时间输出对齐：查询条件token语义、校准token readout、时间窗口探测和生成时残差擦除。语义分析表明，基础模型在微调前已包含查询事件的潜在证据，微调前后与查询事件最强对齐的音频token出现在相似的时间位置。微调后，音频token中的事件信息对解码器更加可访问，尤其是在早期和中间层。跨检查点控制显示这种改进主要来自解码器适应。

### 🔧 技术方案

**模型架构：** 基于Qwen2.5-Omni和Qwen2-Audio-7B-Instruct，使用LoRA微调。分析框架包括：查询条件token语义分析、校准token readout、时间窗口探测和生成时残差擦除。

**核心创新：** 提出语义到readout账户：基础模型已包含潜在事件证据，微调主要改善解码器对现有证据的读取能力，而非创建新证据。跨检查点控制显示增益主要来自解码器适应，而非token语义的改变。

**训练策略：** 在AudioGrounding-QA数据集上训练，使用LoRA适配器仅应用于语言模型transformer块，音频塔和投影仪保持冻结。

### 📊 实验结果
**数据集** AudioGrounding-QA（9542/1052/992 QA实例）

**主要指标** Qwen2.5-Omni微调后：mIoU从0.3707提升到0.6817，F1从0.4416提升到0.7626，R@0.7从0.2349提升到0.5817。Qwen2-Audio也呈现类似的解码器可读性和预测对齐改进。

**是否开源** 暂无

### ⭐ 评分：8/10
这是首次系统分析LALM中音频token内部机制的工作，为理解语音大模型的工作原理提供了重要贡献。实验设计严谨，四种分析方法相互印证，结论有价值。创新性高，实验充分。

---

## [2] Text-Prompted CLAP: Learning Query-Conditioned Audio Representations via Contrastive Learning

**arXiv ID** 2607.25085 | **方向** 音频理解

**作者：** Mohan Li, Rama Doddipatla, Philip C. Woodland

**机构：** University of Cambridge, Amazon

**发布日期：** 2026-07-27 | **论文** https://arxiv.org/abs/2607.25085 | **PDF** https://arxiv.org/pdf/2607.25085.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
对比语言-音频预训练（CLAP）在共享嵌入空间中学习对齐的文本和音频表示。然而，每个模态的独立编码限制了其在复杂音频理解和检索任务中建模跨模态语义的能力。本文提出Text-Prompted CLAP（TP-CLAP），这是一个参数高效的CLAP扩展，引入基于跨注意力的融合模块将文本提示融入音频特征。TP-CLAP使用音频多选题（audio-MCQ）框架进行训练，通过对比学习学习将查询条件音频表示与正确答案的文本嵌入对齐。实验表明，TP-CLAP在音频问答任务上与更大的音频LLM相比具有竞争力，同时在音频-文本检索和零样本分类基准上改进了基础CLAP模型。学习到的表示进一步微调用于属性聚焦的音频到音频检索，表明TP-CLAP在音乐检索任务中始终优于标准CLAP基线。

### 🔧 技术方案

**模型架构：** 基于CLAP backbone，使用CED-Base音频编码器和bert-base-uncased文本编码器。融合模块包含L=2个跨注意力块。

**核心创新：** 提出跨注意力融合模块，使音频表示能够根据文本查询进行动态调整。引入音频-MCQ监督框架，学习查询条件表示而不需要多模态LLM。

**训练策略：** 在AudioCaps-v2、Clotho、WavCaps等数据集上预训练，然后在AudioMCQ上训练。使用两阶段训练：先冻结CLAP编码器仅训练融合模块，然后联合微调所有参数。

### 📊 实验结果
**数据集** AudioCaps、Clotho、MMAU、MMAR、NSynth、MagnaTagATune

**主要指标** 音频问答：TP-CLAP在MMAU上达到71.47%准确率（sound）和55.99%（music），优于CLAP+AudioMCQ的64.56%和52.99%。音乐检索任务也持续优于CLAP基线。

**是否开源** 暂无

### ⭐ 评分：7/10
参数高效的方法，在多个任务上取得竞争性性能。创新性较好，实验充分，适用于资源受限场景。参数高效是该工作的主要亮点。

---

## [3] Unlocking Spatial Grounding in Large Audio-Visual Retrieval models

**arXiv ID** 2607.24786 | **方向** 音频视觉定位

**作者：** Hugo Malard, Michel Olvera, Sanjeel Parekh, Gaël Richard, Slim Essid, Stéphane Lathuilière

**机构：** LTCI, Télécom Paris, Institut Polytechnique de Paris; Meta Reality Labs Research; NVIDIA France; Inria Grenoble Alpes

**发布日期：** 2026-07-22 | **论文** https://arxiv.org/abs/2607.24786 | **PDF** https://arxiv.org/pdf/2607.24786.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
弱监督为音频视觉声源定位设置了一个实用的制度，因为大规模获取密集空间注释成本很高。然而，该任务仍然具有挑战性，因为模型必须在没有像素级监督的情况下从时间对齐的音频视觉数据中定位声源。最近的大规模音频视觉检索模型以前所未有的规模训练，编码了丰富的多模态结构。研究表明，尽管这些模型的潜在表示针对全局对齐进行了优化，但仍然能够实现细粒度空间定位。虽然检索backbone的上层由于全局池化逐渐丢失空间细节，但中间视觉token保留了高度结构化的空间信息。为此，本文引入LAIP框架，采用轻量级的音频信息空间池化（AiSP）来替换标准的全局聚合模块。通过使用帧对齐的音频查询中间视觉token，LAIP恢复了否则会被冻结检索流程丢弃的局部空间信息。该方法在AVSBench和AVATAR上实现了最先进的性能，在后者上几乎将之前的结果翻倍。

### 🔧 技术方案

**模型架构：** 基于PE-AV检索 backbone，添加音频信息空间池化（AiSP）模块。采用三层分级设计，逐步将空间token池化为音频条件token。

**核心创新：** 提出Audio-informed Spatial Pooling (AiSP)，使用音频查询中间视觉token。多分辨率正则化确保注意力图空间一致性。可学习null token处理不相关情况。

**训练策略：** 使用SigLIP风格对比目标，仅训练新增的AiSP模块和视频编码器适配器。训练10个epoch，lr=1e-4。

### 📊 实验结果
**数据集** AVATAR、AVSBench、ADE-SP

**主要指标** AVATAR：CIoU达到27.63%（single-sound）、27.35%（mixed-sound）、23.69%（multi-entity），相比TAVLO提升约10个百分点。AVSBench S4：F-score达到65.18%。

**是否开源** 暂无

### ⭐ 评分：8/10
创新性强，首次证明检索模型可解锁定位能力。实验充分，在多个基准上取得SOTA性能。工程价值高，为检索和定位任务的统一提供了新思路。

---

## 🎙️ 语音前端

## [4] faster-enhancer.c: A Dependency-Free int8 Runtime for Streaming Speech Enhancement on Commodity CPUs

**arXiv ID** 2607.25350 | **方向** 语音增强

**作者：** Gyeongmin Kim

**机构：** 暂无

**发布日期：** 2026-07-28 | **论文** https://arxiv.org/abs/2607.25350 | **PDF** https://arxiv.org/pdf/2607.25350.pdf | **代码** https://github.com/kdrkdrkdr/faster-enhancer.c | **Demo** 暂无

### 📌 简介
这是一篇关于在CPU上运行流式语音增强器成本的实现和测量研究。我们将48kHz的FastEnhancer-Medium移植到faster-enhancer.c，这是一个C运行时，在初始化时选择六个int8 GEMM层，保持架构和权重不变。一个Apple M2核心达到0.069实时因子，而同一台机器上的fp32 ONNX Runtime图为0.230，实现3.3倍加速。Galaxy S23+（骁龙8 Gen 2）达到0.096。加速来自于围绕一个固定模型专门化运行时的每一层。激活范围按帧重新计算，因此不需要校准集；k=3卷积使用Winograd F(2,3)；跨级状态为fp16；GRU和反量化尾声部融合；启动后不分配任何东西。在824个VoiceBank-DEMAND话语上，引擎与fp32的差距控制在-0.006 PESQ和-0.08 dB SNR以内。速度本身并不能决定部署成本。增强器只要麦克风打开就占用一小部分核心，因此其实时因子是一个占空比。基准测试竞速通过文件；音频回调不是。按6.67ms截止时间节奏运行每帧花费4.2倍，节省49%的能量，最便宜的核心放置仍会错过96%的截止日期。

### 🔧 技术方案

**模型架构** FastEnhancer-Medium 48kHz，6层int8 GEMM tiers，Winograd F(2,3)卷积，fp16跨级状态。

**核心创新** 无需校准集的per-frame激活范围重计算；Winograd卷积加速；GRU和反量化融合；启动后零内存分配。6层SIMD tiers：ARM NEON、DOTPROD、I8MM、x86 AVX2、AVX-VNNI、AVX-512 VNNI。

**训练策略** 训练-free int8移植，保持模型架构和权重不变。

### 📊 实验结果
**数据集** VoiceBank-DEMAND（824 utterances）

**主要指标** Apple M2: RTF 0.069 vs fp32 ONNX 0.230 (3.3x加速)；Galaxy S23+: RTF 0.096。量化损失：PESQ -0.006，SNR -0.08dB。节拍pacing节省49%能量。

**是否开源** 已开源：https://github.com/kdrkdrkdr/faster-enhancer.c

### ⭐ 评分：9/10
工程突破性工作，实用价值极高。首次实现商品CPU上实时48kHz增强，质量损失可忽略。创新性强，代码已开源。解决了端侧语音增强的核心工程问题。

---

## [5] VAD to the Bone: Ultra-Tiny Speech Activity Detection for Edge Deployment

**arXiv ID** 2607.25870 | **方向** VAD

**作者：** Stephen Bauer, Sheila Seidel, Shanza Iftikhar, Scott Veidenheimer, Gorkem Ulkar

**机构：** Analog Devices, Inc.; University of California, Los Angeles (UCLA)

**发布日期：** 2026-07-28 | **论文** https://arxiv.org/abs/2607.25870 | **PDF** https://arxiv.org/pdf/2607.25870.pdf | **代码** https://huggingface.co/spaces/kiloVAD-demo/kiloVAD | **Demo** https://huggingface.co/spaces/kiloVAD-demo/kiloVAD

### 📌 简介
语音活动检测（VAD）在始终在线系统中在严格的内存、延迟和计算约束下触发下游语音处理。最近的紧凑模型报告了强大的准确性，但依赖于未被广泛支持的组件：可学习滤波器组、循环层或非因果后处理。我们提出kiloVAD，设计用于使用标准Mel特征、仅CNN层和可调上下文/频谱参数进行嵌入式推理。我们引入per-layer结构化剪枝与自蒸馏，以及基于角度的量化感知训练（QAT），其性能优于标准QAT 1-4%。在因果条件下逐帧评估，kiloVAD在AVA-Speech上以2.1k参数和200ms上下文达到0.850 AUC，为因果、部署就绪的VAD建立了新的最先进水平。

### 🔧 技术方案

**模型架构** CNN-only架构，使用标准Mel频谱图特征。包含适配器层、深度可分离卷积块、残差块、膨胀块、全局平均池化和二分类器。

**核心创新** Per-layer结构化剪枝+自蒸馏；Angle-based自蒸馏QAT，优于标准QAT 1-4%。无GRU、无可学习滤波器库、无非因果后处理。

**训练策略** 在LibriSpeech train-clean-100上训练，使用三种噪声条件。Per-layer剪枝通过Optuna多目标搜索优化。

### 📊 实验结果
**数据集** AVA-Speech

**主要指标** 2.1k参数pruned模型：AVA-Speech AUC 0.850，F1 0.783。INT8量化后保持0.851 AUC（无损失）。200ms输入延迟。已被INTERSPEECH 2026接收。

**是否开源** 已开源：https://huggingface.co/spaces/kiloVAD-demo/kiloVAD

### ⭐ 评分：9/10
突破性工作，参数极少（2.1k）且满足所有部署要求。创新性高，实验充分，开源且有demo。首个满足所有四个部署要求（前端兼容、可移植、低延迟、因果评估）的模型。

---

## [6] Towards Operational Conversational Intelligence: A Speech Intelligence Framework

**arXiv ID** 2607.24958 | **方向** ASR/对话智能

**作者：** Chaitanya Vishnoi, Shudhant Khurana, Abhilash Timmapur, Somya Rai, Saket Mohanty

**机构：** Indian Institute of Technology Kanpur; EXL

**发布日期：** 2026-07-27 | **论文** https://arxiv.org/abs/2607.24958 | **PDF** https://arxiv.org/pdf/2607.24958.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
执法记录仪（BWC）音频具有独特的挑战，包括高环境噪声、可变录音条件和多个重叠说话人，这使得自动转录和说话人标记具有挑战性。我们提出了一个双路径对话智能框架，对原始BWC音频进行预处理，将处理管道分为diarization分支和ASR分支，并融合它们的输出。diarization分支使用降噪前端（DeepFilterNet）、语音活动检测（VAD）和NVIDIA的多尺度说话人diarization解码器（MSDD）及TitaNet嵌入。转录分支使用响度归一化和WhisperX（Large-v3）及强制对齐和概率引导语音分割。最后，通过将每个识别的单词分配给时间重叠最大的说话人片段来执行词级说话人归因。我们在被被 curation的执法记录仪数据集上评估了提出的框架，该数据集由公开可用的美国和英国警察执法记录仪录音构建。实验结果表明，任务特定声学条件和概率引导语音分割改善了在具有挑战性的执法记录仪录音条件下的说话人diarization、转录和词级说话人归因。提出的模块化架构为未来支持说话人的对话智能系统提供了可扩展的基础。

### 🔧 技术方案

**模型架构** 双路径架构：diarization路径使用DeepFilterNet+Pyannote VAD+NVIDIA MSDD+TitaNet；ASR路径使用loudness normalization+WhisperX。

**核心创新** 提出"增强陷阱"概念：神经增强对diarization有益但损害ASR。概率引导VAD后处理，使用Pyannote语音概率进行分段。基于最大时间重叠的说话人归因融合。

**训练策略** 使用公开的BWC风格数据集评估（8个录音，31分钟，41个说话人）。各组件使用预训练模型。

### 📊 实验结果
**数据集** 自建BWC数据集（8个录音，31分钟）

**主要指标** 报告了VAD、diarization、ASR和说话人归因的组件级评估结果，验证了任务特定声学条件和概率引导分割的有效性。

**是否开源** 框架组件均为公开模型，但整体pipeline未开源

### ⭐ 评分：7/10
针对实际应用场景的实用系统，创新性地解决增强陷阱问题。实验基于真实数据，但数据集规模有限。为执法记录仪音频处理提供了有价值的解决方案。

---

## [7] Multi-Phonation Graph Learning with Self-Supervised Speech Embeddings for ALS Detection and Progression Prediction

**arXiv ID** 2607.25284 | **方向** 医学语音/ALS检测

**作者：** Behrad TaghiBeyglou, Fatemeh Bagheri, Ervin Sejdic

**机构：** University of Toronto; North York General Hospital

**发布日期：** 2026-07-28 | **论文** https://arxiv.org/abs/2607.25284 | **PDF** https://arxiv.org/pdf/2607.25284.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
肌萎缩侧索硬化症（ALS）逐渐损害言语运动控制，使声学分析成为严重程度和进展估计的有前途的生物标志物。我们提出了一个subject-level图框架，将多个发声录音聚合为一个独特的k近邻图，该图由2秒片段的预训练SSL嵌入构建。我们在SAND数据集任务上比较了四种SSL前端（wav2vec 2.0、HuBERT、data2vec-audio和UniSpeech-SAT）和五种图神经网络（GCN、residual GCN、GAT、GraphSAGE和GIN）（339名参与者：205名ALS，134名对照）：5类构音障碍严重程度和4类ALSFRS-R进展预测。在官方验证集上，最佳配置（HuBERT+GIN）在任务1上达到0.73的macro-F1，在任务2上达到0.69，优于SAND验证基线（0.61和0.58）。这些结果凸显了将GNN与预训练跨语言语音表示结合用于低资源ALS检测和进展监测的潜力。

### 🔧 技术方案

**模型架构** Subject-level图框架：使用SSL嵌入（wav2vec 2.0、HuBERT、data2vec-audio、UniSpeech-SAT）提取2秒片段特征，构建kNN图，使用GNN（GCN、ResGCN、GAT、GraphSAGE、GIN）进行图分类。

**核心创新** 提出subject-level图公式，将多个录音建模为统一表示。系统评估4种SSL前端的5种GNN架构。HuBERT+GIN组合表现最佳。

**训练策略** 在SAND数据集训练（339 participants: 205 ALS, 134 control）。10折交叉验证选择超参数。已被Interspeech2026接收。

### 📊 实验结果
**数据集** SAND Challenge数据集

**主要指标** HuBERT+GIN：Task 1（5类严重程度）mF1=0.73，Task 2（4类ALSFRS-R进展预测）mF1=0.69。相比SAND验证基线（0.61和0.58）显著提升。

**是否开源** 暂无

### ⭐ 评分：8/10
创新地将图学习应用于ALS检测，实验系统充分，在两个任务上均超越基线。方法新颖，有临床应用价值。为医学语音分析提供了新思路。

---

## 🔬 其他语音技术

## [8] Extracting Voice Styles from Frozen TTS Models via Gradient-Based Inverse Optimization

**arXiv ID** 2607.25351 | **方向** TTS/声纹

**作者：** Gyeongmin Kim

**机构：** 暂无

**发布日期：** 2026-07-28 | **论文** https://arxiv.org/abs/2607.25351 | **PDF** https://arxiv.org/pdf/2607.25351.pdf | **代码** https://github.com/kdrkdrkdr/supertonic.embed | **Demo** 暂无

### 📌 简介
一些文本到语音系统发布合成模型和预设风格向量，但不发布将音频转换为此类向量的参考编码器。该模型仍然接受风格向量；拥有自己声音的用户无法生成一个。我们通过梯度下降直接求解该输入，反向发布管道：每个权重保持冻结，仅优化风格向量，针对一个录音的时间池化WavLM统计量。因为目标丢弃了时间轴，合成的文本可能与录音不同，所以不需要转录和对齐。在两个语料库的154个说话人中，ECAPA-TDNN相似度从0.132提升到0.403，ResNet从0.099提升到0.401，每个说话人都有提升；在其等错误点的验证器接受53%的恢复声音作为目标，而它们开始的预设只有1%。

### 🔧 技术方案

**模型架构** 基于SupertonicTTS 2，风格向量s∈R^(50×256)，共12800参数。

**核心创新** 无需参考编码器，通过优化风格向量匹配目标语音的WavLM层4统计量。内容无关目标函数使用时间池化的mean和std。停止阈值0.30通过预设合成内容差异校准。

**训练策略** 冻结所有TTS和WavLM权重，仅优化风格向量。5个英语提示轮换，Adam优化器，lr=2e-4。

### 📊 实验结果
**数据集** VCTK（110 speakers）、Common Voice Seed-TTS Eval（44 speakers）

**主要指标** ECAPA相似度从0.132提升到0.413，ResNet从0.099提升到0.401。每个说话人都有提升。验证器在EER点接受53%的提取声音 vs 预设的1%。

**是否开源** 已开源：https://github.com/kdrkdrkdr/supertonic.embed

### ⭐ 评分：8/10
创新性问题解决方法，实验规模大（154说话人），开源且有明确应用价值。对TTS模型安全性有启示。无需参考编码器即可提取声音风格。

---

## [9] Device Invariance using Domain Adaptation on Acoustic Scene Classification

**arXiv ID** 2607.25887 | **方向** 声学场景分类

**作者：** Abhishek Dileep, Shubham Sharma, Padmanabhan Rajan

**机构：** 暂无

**发布日期：** 2026-07-28 | **论文** https://arxiv.org/abs/2607.25887 | **PDF** https://arxiv.org/pdf/2607.25887.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文探讨了在使用卷积神经网络（CNN）基于和Transformer基于特征表示进行声学场景分类时，领域适应技术的有效性。两种著名的领域适应技术，即域对抗神经网络（DANN）和条件域对抗网络（CDAN）在各种领域偏移下进行了评估。我们的研究表明，DANN对两种特征提取器都能相当一致地提供有效的领域适应。另一方面，CDAN仅对基于CNN的特征提取器提供有效的领域适应。该研究提供了关于领域适应方法可能需要根据底层特征表示进行定制的见解。在DCASE 2020数据集上针对多个设备的实验评估支持了这些观察。

### 🔧 技术方案

**特征提取器** PaSST (Transformer)、DcaseNet (CNN)、Custom CNN三种特征提取器。

**领域适应方法** DANN（域对抗神经网络）和CDAN（条件域对抗网络）。

**核心创新** 发现DANN在所有特征提取器上提供一致有效的领域适应；CDAN仅在CNN特征提取器上有效，对Transformer（PaSST）失效。原因可能与ViT的动态特征和分类器伪标签相关。

**训练策略** 在DCASE 2020 Task 1A数据集上评估，以设备A为源，其他设备为目标。

### 📊 实验结果
**数据集** DCASE 2020 Task 1A（设备A为源，其他设备为目标）

**主要指标** PaSST：源准确率0.845，域移后0.61-0.65，DANN提升至0.65-0.74。DcaseNet：DANN提升10.9%，CDAN提升11.5%。Custom CNN：CDAN提升11.8%。

**是否开源** 暂无

### ⭐ 评分：6/10
实验充分，揭示了领域适应方法与特征提取器类型的重要关系。创新性中等但有实践指导价值。为领域适应在不同特征提取器上的应用提供了重要见解。

---

## [10] Time-Frequency Consistency Learning for Robust Speech Deepfake Detection

**arXiv ID** 2607.17761 | **方向** 语音深度伪造检测

**作者：** Jun Xue, Zhuolin Yi, Yanzhen Ren, Yihuan Huang, Jiayu Xiong, Yi Chai, Guanxiang Feng, Jiajun Liu, Tong Zhang

**机构：** 武汉大学；同济大学

**发布日期：** 2026-07-20 | **论文** https://arxiv.org/abs/2607.17761 | **PDF** https://arxiv.org/pdf/2607.17761.pdf | **代码** https://github.com/JunXue-tech/TFCL | **Demo** 暂无

### 📌 简介
最近，语音深度伪造检测（SDD）取得了显著进展。然而，其鲁棒性评估仍然主要局限于受控加法噪声场景，缺乏对现实部署中声学前段（AFE）处理管道引入的复杂失真的系统研究。在这项工作中，我们模拟了一个统一的AFE管道，包括声学回声消除、噪声抑制、自动增益控制和语音活动检测（VAD），并对当前最先进的模型进行了全面评估。结果表明，AFE引入的非线性和时频耦合失真显著降低了检测性能。为了解决这个问题，我们提出了时频一致性学习（TFCL）框架，旨在学习在AFE处理前后保持稳定的伪造不变表示。我们观察到AFE不仅引入时间不对齐（例如VAD导致的片段级偏移），还削弱或扭曲了关键的频域线索。为此，TFCL采用注意力驱动的软对齐机制来捕获跨时间依赖性，以及频域结构一致性约束来强制特征不变性。因此，该模型能够在时间扰动和频谱失真下保持稳定表示。广泛实验结果表明，该方法有效缓解了AFE处理导致的性能下降，显著提高了SDD在现实场景中的鲁棒性。代码已开源。

### 🔧 技术方案

**模型架构** 基于AASIST后端分类器，结合时频一致性学习模块。

**核心创新** 时域：注意力驱动的软对齐机制捕获跨时间依赖；频域：频域结构一致性约束保持特征不变。AFE处理包括AEC、NS、AGC、VAD级联。

**训练策略** 使用ASVspoof2019 LA数据集，结合模拟AFE处理进行训练。已被ACM MM 2026接收。

### 📊 实验结果
**数据集** ASVspoof2019 LA

**主要指标** 在完整AFE pipeline下：EER 9.78%，AUC 96.40%，显著优于所有基线方法。干净条件下：EER 0.55%，AUC 99.96%。在各种AFE条件下一致提升。

**是否开源** 已开源：https://github.com/JunXue-tech/TFCL

### ⭐ 评分：8/10
创新性地将AFE处理引入SDD鲁棒性评估，提出有效解决方案。实验系统充分，在真实场景有重要应用价值。为语音深度伪造检测的实际部署提供了重要参考。

---

## 本期总结

本期论文涵盖：

- **语音大模型机制理解**：首次系统分析LALM音频token内部机制
- **语音理解**：Text-Prompted CLAP参数高效方法
- **音频视觉定位**：LAIP框架从检索模型解锁定位能力
- **语音增强**：faster-enhancer.c商品CPU实时增强
- **超小型VAD**：kiloVAD仅2.1k参数满足所有部署要求
- **执法对话智能**：双路径框架处理BWC音频
- **医学语音**：ALS检测与进展预测的图学习方法
- **TTS声纹提取**：梯度优化从冻结模型提取声音风格
- **声学场景分类**：领域适应与特征提取器关系研究
- **语音深度伪造检测**：TFCL框架提升AFE鲁棒性

**推荐关注**：faster-enhancer.c端侧增强、kiloVAD超小型VAD、TFCL鲁棒性检测、音频token机制分析

---

*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*
