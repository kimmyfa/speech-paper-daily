# 2026-08-11 语音论文速递

**共收录**: 5 篇 | **语音大模型**: 4 篇 | **语音前端**: 1 篇

> 今日 arXiv 语音相关论文共命中 5 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] SemBridge: Semantic Token Anchoring for Continuous-Latent Autoregressive Speech Generation

**arXiv ID** 2608.07462 | **方向** 语音大模型

**作者**：Hanke Xie, Haopeng Lin, Jiale Qian, Dake Guo, Yuepeng Jiang, Zhichao Wang, Wenxiao Cao, Jingbin Hu, Guobin Ma, Wenhao Li, Huakang Chen, Chengyou Wang, Ming Tao, Zhonghua Fu, Lei Xie, Xinsheng Wang

**机构**：西北工业大学音频语音与语言处理研究组 (ASLP Lab)、Soul AI Lab

**发布日期**：2026-08-07 | **论文** https://arxiv.org/abs/2608.07462 | **PDF** https://arxiv.org/pdf/2608.07462.pdf | **代码** https://github.com/ASLP-lab/SemBridge | **Demo** https://tiamojames.github.io/SemBridge_demo/

### 📌 简介
连续潜向量自回归语音生成已成为高保真语音合成的有前景方向，能够避免离散token的量化损失并保留更丰富的声学信息。然而，连续声学目标不像离散语义token那样提供显式的token级预测目标，导致自回归语言模型必须通过声学预测间接获取语言结构，这可能损害生成语音的内容保真度。SemBridge是一个训练阶段的语义token锚定框架，使用离散语义token直接监督自回归LM状态，并采用语义对齐声学VAE在相同语义参考下组织连续目标空间。语义监督仅用于训练阶段，推理时完全保持连续生成。在零样本TTS和分数条件歌声合成任务上，SemBridge持续降低WER/CER同时保持竞争力的说话人相似度和感知质量。

### 🔧 技术方案

**模型架构**：两阶段框架。Stage I训练SA-VAE进行波形重建同时对齐连续声学patch与冻结语义tokenizer的embedding；Stage II训练连续潜向量自回归生成器，包含因果LM、局部扩散变换器LocDiT和语义预测头。语义tokenizer使用GLM-4-Voice，在12.5Hz运行，词汇量16384。

**核心创新**：提出语义token锚定机制——使用离散语义token标签直接监督选定自回归LM状态的训练，同时保持连续潜向量patch作为唯一生成和递归变量。引入语义对齐声学VAE (SA-VAE)将连续声学目标空间与语义tokenizer的token级embedding对齐，建立共享语义参考。

**训练策略**：SA-VAE在25K小时音频上训练（20K小时语音+5K小时歌声）；SemBridge在100K小时双语文本到语音语料库上训练300K步。使用AdamW优化器，bf16精度，学习率1e-4。

### 📊 实验结果
**数据集**：Seed-TTS-Eval、CV3-EVAL零样本TTS评估；GMO-SVS歌声合成评估。

**主要指标**：
- 中文CER: 0.95% (最佳)，SIM: 0.758
- 英文WER: 1.81% (最佳)，SIM: 0.699
- 中文困难集CER: 9.79%，SIM: 0.717
- 歌声合成：中文CER 8.32%，SIM 0.906；英文WER 14.77%，SIM 0.926

**是否开源**：已开源

### 评分：9/10
SemBridge在零样本TTS上实现了领先的内容准确率，首次证明离散语义token监督对连续语音生成的有效性。消融实验证实了语义对齐和状态锚定的互补增益。这是一个有前景的研究方向，为连续语音生成中的语言结构建模提供了新思路。

---

## [2] LILAC: An Idempotent Neural Speech Codec

**arXiv ID** 2608.05727 | **方向** 语音大模型

**作者**：June Young Yi, Dongwook Lee, Jiheum Yeom, Sungroh Yoon

**机构**：首尔大学 (Seoul National University)

**发布日期**：2026-08-06 | **论文** https://arxiv.org/abs/2608.05727 | **PDF** https://arxiv.org/pdf/2608.05727.pdf | **代码** https://github.com/Rick-McCoy/lilac-codec | **Demo** https://rick-mccoy.github.io/lilac-demo

### 📌 简介
神经音频编解码器在语音生成和编辑中广泛应用，但现有神经音频编解码器不是幂等的：测试的十二个基线系统中，每种配置在单次解码-重编码周期内平均至少重写15%的token。这对将神经音频编解码器用作token接口的流水线构成问题，因为重编码解码输出可能发生。LILAC是首个在设计上保证幂等的全卷积24kHz语音编解码器，位率0.75 kbit/s，帧率9.375 Hz。LILAC在保持竞争力的质量同时实现幂等性，在LibriSpeech和LibriTTS-R上分别达到UTMOS 4.14和4.24，与SOTA亚1 kbit/s神经音频编解码器相当。

### 🔧 技术方案

**模型架构**：全卷积架构，使用可逆分析变换作为核心骨干。可逆变换由可逆1×1卷积和加性耦合块组成，使用有限标量量化(FSQ)对坐标进行量化，帧率9.375 Hz，每帧80比特，位率0.75 kbit/s。编码器和解码器共享分析变换权重。

**核心创新**：首次提出并实现结构上保证的编解码幂等性。通过可逆分析变换、有选择地丢弃信息、然后仅从传输的量化坐标重建丢弃信息来保证幂等性。数学证明表明，无论权重如何，编解码器都是幂等的。

**训练策略**：在HiFiTTS-2数据集（31700小时）上训练。使用多分辨率mel损失、STFT损失、对抗铰链损失和特征匹配损失。隐藏维度256，深度4，总共58.5M参数。

### 📊 实验结果
**数据集**：LibriSpeech test-clean、LibriTTS-R test、VCTK、HiFiTTS-2 test

**主要指标**：
- LibriSpeech: UTMOS 4.14, dWER 0.101, STOI 0.935, SI-SNR +2.2
- LibriTTS-R: UTMOS 4.24, dWER 0.086, STOI 0.944, SI-SNR +6.0
- 幂等性：100% token一致（所有测试样本）

**是否开源**：已开源

### 评分：9/10
LILAC是首个在设计上保证编解码幂等性的神经语音编解码器，解决了语音生成流水线中的关键问题。实验表明经过任意次数重编码周期后仍能保持自然度、可懂度和音频质量。这是一个重要的技术创新，对下游任务稳定性有重要意义。

---

## [3] Multi Codec Discrete Diffusion Model for Text Guided Speech Inpainting and Editing

**arXiv ID** 2608.06424 | **方向** 语音大模型

**作者**：Iftach Shoham, Tali Dror, Oren Gal, Haim Permuter, Gilad Katz, Eliya Nachmani

**机构**：Ben-Gurion University of the Negev、University of Haifa（以色列）

**发布日期**：2026-08-05 | **论文** https://arxiv.org/abs/2608.06424 | **PDF** https://arxiv.org/pdf/2608.06424.pdf | **代码** https://github.com/iftachShoham/SIEDD | **Demo** 暂无

### 📌 简介
语音 recordings经常包含缺失、损坏或错误的区域，需要在不完全重新合成整个语音的情况下进行重建或修改。语音修复恢复缺失片段，而语音编辑根据编辑后的转录本替换 spoken 内容。两者都要求生成的语音表达预期内容，同时与周围说话人身份、韵律、时间和录制条件保持一致。离散扩散特别适合这些任务，因为它可以迭代细化masked token，同时联合条件于左右声学上下文。SIEDD是一个基于分层codec token的文本引导语音修复和编辑的离散扩散框架。其核心架构HiCoDD遵循RVQ生成顺序，将先前生成的codebook表示为干净的承诺声学上下文，仅对当前细化codebook应用扩散。

### 🔧 技术方案

**模型架构**：分层多码本离散扩散框架HiCoDD。使用Diffusion Transformer (DiT)作为score网络，包含承诺上下文编码器和解噪解码器。采用XPhoneBERT编码器进行音素级条件化。

**核心创新**：1) 层次感知的codec扩散——在每个CB内联合细化时间位置，同时按固有粗到细顺序生成CB；2) 对比引导用于文本条件修复和编辑——在log-score空间中组合条件和非条件具体分数，负分支局部化到编辑span。

**训练策略**：在LibriTTS和GigaSpeech数据集上训练。使用DWDSE (Diffusion Weighted Denoising Score Entropy) 目标函数。

### 📊 实验结果
**数据集**：RealEdit benchmark

**主要指标**：
- 语音编辑: WER 0.121 (最佳), SIM 0.98 (最佳), MCD 270.0
- 语音修复: 单一gap和多重gap设置均优于自回归基线

**是否开源**：已开源

### 评分：8/10
SIEDD在RealEdit基准上实现了最佳整体语音编辑性能，在所有语音修复设置中优于评估的自回归基线。明确建模codec层次结构显著改善了上下文保留的语音重建和编辑。首次将离散扩散应用于分层RVQ token取得成功。

---

## [4] Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement

**arXiv ID** 2608.07423 | **方向** 语音前端

**作者**：Xulin Fan, Juan Azcarreta, Ashutosh Pandey, Jesus Alvarez, Ke Tan, Jacob Donley, Ritwik Giri, Buye Xu

**机构**：University of Illinois Urbana-Champaign、Meta Reality Labs Research

**发布日期**：2026-08-07 | **论文** https://arxiv.org/abs/2608.07423 | **PDF** https://arxiv.org/pdf/2608.07423.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
低延迟、低计算量的语音增强对可穿戴设备的实时通信至关重要，但严格的计算约束显著限制了设备端性能。之前提出的知识增强通过利用更强大的服务器端模型来提高边缘模型性能，但语音增强的性能提升有限。提出一个协作框架，包含三种技术：1) 延迟服务器输出作为额外输入；2) 层-wise特征增强，传输中间服务器表示以指导边缘推理；3) 协作多通道Wiener滤波，融合服务器和边缘模型估计的加权协方差矩阵以改进波束形成。实验表明所提框架显著优于仅边缘基线，计算开销极小。

### 🔧 技术方案

**模型架构**：服务器-边缘协作系统。服务器端模型是因果SpatialNet；边缘端模型基于TinyGRU，包含空间卷积模块和三个SplitGRU层。

**核心创新**：1) 延迟输入级联——服务器增强音频作为辅助参考；2) 层-wise特征增强——通过FiLM将中间服务器表示注入边缘模型；3) 协作MCWF——融合服务器和边缘的协方差矩阵。

**训练策略**：服务器端SpatialNet预训练100轮后冻结。边缘TinyGRU训练100轮，使用Adam优化器，学习率1e-3，梯度裁剪0.03。训练目标为SNR损失。

### 📊 实验结果
**数据集**：DNS-Challenge数据集模拟，包含8通道圆形麦克风阵列

**主要指标**：
- 标准条件: SI-SDR 5.74 dB (+3.77 vs 基线), PESQ 2.33, STOI 85.48%
- 困难条件: SI-SDR 2.33 dB (+3.49 vs 基线), STOI 73.73%
- 边缘额外参数量: 1.5%，额外计算量: 2.4%

**是否开源**：暂无

### 评分：8/10
该工作提出了一个实用的云边协作语音增强框架，在极小额外开销下显著提升边缘设备性能。实验验证了三种技术（延迟输出、层-wise特征、协作MCWF）的互补增益，为可穿戴设备上的实时语音增强提供了可行方案。

---

## [5] LSEAD: A Privacy-Preserving LLM-Based Speech Analysis Framework for Early Alzheimer's Disease Screening

**arXiv ID** 2608.07378 | **方向** 语音大模型

**作者**：Xin Wang, Yingchao Huang, Yuhan Su, Shanshan Yao, Wei Peng

**机构**：待确认（从摘要提取）

**发布日期**：2026-08-07 | **论文** https://arxiv.org/abs/2608.07378 | **PDF** https://arxiv.org/pdf/2608.07378.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
阿尔茨海默病(AD)的早期诊断对于实现可能减缓疾病进展和改善患者结果的及时干预至关重要。对非侵入性和具有成本效益的AD检测方法的需求日益增长，特别是在具有不同患者群体和录音条件的真实临床环境中。基于语音的筛查使用无需专业设备的自然语音采集来解决这些需求。大型语言模型的最新进展通过提供丰富的语言表示和强泛化能力改进了语音分析。提出LSEAD，一个使用预训练开源LLM的基于语音的AD检测框架。语音录音自动转录，文本embedding使用本地部署的LLM提取，应用主成分分析(PCA)降维后进行分类。

### 🔧 技术方案

**模型架构**：基于LLM的语音分析框架。使用自动语音识别进行转录，本地部署的LLM提取文本embedding，PCA降维，分类头进行AD风险评估。

**核心创新**：隐私保护的AD筛查——仅依赖语音转录和本地部署模型，支持无需外部数据交换的隐私保护AD风险评估。

**训练策略**：在ADReSS20和ADReSSo2021基准数据集上评估。

### 📊 实验结果
**数据集**：ADReSS20、ADReSSo2021

**主要指标**：
- 与现有方法相比，分类准确率提升高达5%
- 早期阶段检测性能优异

**是否开源**：暂无

### 评分：7/10
LSEAD提供了一个实用的、安全的、可扩展的早期AD筛查方法。使用LLM-based embedding跨数据集泛化良好，隐私保护特性使其适合临床应用。这是一个有意义的医学语音应用方向。

---

今日语音论文速递
