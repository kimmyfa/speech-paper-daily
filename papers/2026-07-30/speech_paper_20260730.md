# 2026-07-30 语音论文速递

**共收录**: 8 篇 | **语音大模型**: 2 篇 | **语音安全**: 3 篇 | **语音前端/TTS**: 3 篇

> 今日 arXiv 语音相关论文共命中 8 篇。
> 以下是按评分排序的结果。

---

## 语音安全

## [1] ThinkOmni: A Reasoning-Driven Omni-Modal LLM Framework for Audio Forgery Detection and Localization

**arXiv ID**：2607.26553 | **方向**：语音伪造检测与定位

**作者**：Yuxiong Xu, Kaiqing Lin, Bin Li, Haodong Li, Sheng Li

**机构**：Guangdong Provincial Key Laboratory of Intelligent Information Processing, Shenzhen Key Laboratory of Media Security, Shenzhen University; Afirstsoft Technology Group Co., Ltd.

**发布日期**：2026-07-29 | **论文**：https://arxiv.org/abs/2607.26553 | **PDF**：https://arxiv.org/pdf/2607.26553.pdf | **代码**：https://beyond0814.github.io/ThinkOmni/ | **Demo**：暂无

### 📌 简介
ThinkOmni是一个推理驱动的全模态大语言模型框架，可同时执行显式取证推理、伪造检测和时序篡改定位。为了支持显式推理监督，作者构建了FACoT（Forensic-Aware Chain-of-Thought）数据集，包含10万样本带有结构化取证证据和推理标注。实验表明ThinkOmni在检测和定位任务上都实现了强大的跨数据集泛化能力。

### 🔧 技术方案

**模型架构：** 基于Qwen2.5-Omni构建，包含语义编码器、声学编码器和视觉编码器。核心组件包括语义-声学取证增强器（SAFE），通过跨注意力机制捕获细粒度取证线索。

**核心创新：** (1) Forensic-Aware Modality-Incremental Learning (FMIL)：渐进式对齐语义、声学和光谱-视觉表示与LLM主干。(2) Forensic-Consistent Multi-task Loss (FCML)：结合加权交叉熵与自适应定位损失，协调推理生成、伪造检测和时序定位。(3) FACoT数据集：首个大规模带结构化推理标注的部分深度伪造音频数据集。

**训练策略：** 三阶段渐进训练：语义取证适应→声学取证增强→多模态取证细化。仅更新适配器和部分编码器参数，冻结LLM主干。

### 📊 实验结果
**数据集**：ASVspoof 2019 LA、HAD、LAV-DF、SINE、LlamaPartialSpoof、ArEnAV、AV-Deepfake1M++

**主要指标**：
- 跨数据集检测：平均ACC 93.70%，F1 93.72%
- 跨数据集定位：ADD 2023上F1 80.74%，Speech-Forensics上F1 85.15%
- 显著优于SSL基线（W2V2-AASIST）和ALLM基线（ALLM4ADD）

**是否开源**：代码已开源

### ⭐ 评分：9/10
创新性强，首次将Chain-of-Thought推理引入音频伪造检测。FACoT数据集构建方法值得借鉴，跨数据集泛化性能优异。实验充分，在多个基准上取得SOTA。工程价值高。

---

## [2] Audio-Anchored Fusion of Multi-Ratio DiT Reconstruction Residuals for Cross-Domain Audio Deepfake Detection

**arXiv ID**：2607.26472 | **方向**：语音deepfake检测

**作者**：Haotian Mo, Jie Liu, Siqi Shen, Songzhu Mei, Xinhai Chen, Xiangyang Wang, Yigui Feng, Shuai Li, Gencheng Liu, Keqi Yang, Qinglin Wang

**机构**：Nanjing University; Nankai University; Zhejiang University, China

**发布日期**：2026-07-29 | **论文**：https://arxiv.org/abs/2607.26472 | **PDF**：https://arxiv.org/pdf/2607.26472.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出跨域音频deepfake检测框架，使用仅在真实语音上训练的Diffusion Transformer (DiT)作为冻结重建探测仪。在0.5、0.75、0.9三种掩码比下进行重建，产生显式的多比残差图。提出音频锚定融合机制，将冻结WavLM听觉表示直接传入融合和，仅用残差作为标量门控加性校正。在ASVspoof 5和真实环境ITW数据集上验证了跨域泛化能力。

### 🔧 技术方案

**模型架构：** 条件流匹配DiT（基于F5-TTS）作为重建探测仪，冻结WavLM-Large作为听觉编码器，多比残差编码器（修改的ResNet-18）。

**核心创新：** (1) 多比DiT重建残差：使用三种掩码比（0.5/0.75/0.9）生成残差图，保留局部失配位置和频率区域信息。(2) 音频锚定加性融合：听觉分支直接进入融合和，残差仅作为加性校正，避免竞争性融合中残差权重增加时压制听觉分支的问题。(3) 样本级标量门控控制残差校正幅度。

**训练策略：** 两阶段解耦训练：DiT探测仪在真实语音上预训练后冻结，检测器使用ASVspoof 5训练集微调。

### 📊 实验结果
**数据集**：ASVspoof 5 Eval、ITW Full

**主要指标**：
- ASVspoof 5 Eval：EER 6.54%，min-DCF 0.1846
- ITW Full：EER 13.84%，min-DCF 0.3692
- 三种子平均：Eval EER 6.89%，ITW EER 15.33%
- 辅助监督损害动态竞争融合：ITW从18.40%恶化到25.30%

**是否开源**：暂无

### ⭐ 评分：8/10
创新性较强，跨域泛化设计合理，实验详尽。音频锚定融合的消融实验验证了假设。跨域性能提升明显。代码开源可进一步提升影响力。

---

## [3] Prosody-driven Jailbreaks in Audio LLMs: A Controlled Study and Mechanistic Analysis

**arXiv ID**：2607.26541 | **方向**：语音LLM安全

**作者**：Jiachen Qian, Junyu Li

**机构**：City University of Hong Kong

**发布日期**：2026-07-29 | **论文**：https://arxiv.org/abs/2607.26541 | **PDF**：https://arxiv.org/pdf/2607.26541.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文研究韵律驱动的语音LLM越狱攻击，固定文本内容仅改变语音韵律来触发有害响应。提出PJ-Break黑盒评估协议和AdvAudio-Prosody基准（600样本），使用6种韵律预设（Panic/Anger/Commanding/Fast/Whisper/Neutral）。实验表明情感韵律音频（44/95）远高于情感文本（11/95），证明韵律是语音LLM安全评估的一等公民。

### 🔧 技术方案

**攻击框架：** PJ-Break固定有害转录本，使用TTS生成6种韵律变体（唤醒度、权威性、语速）。每个预设可能协同改变多个声学属性。

**数据集：** AdvAudio-Prosody包含100个种子指令×6种韵律条件=600样本。韵律预设通过声学特征验证（F0均值/方差、RMS强度、语速）。

**分析手段：** 潜在空间探测、激活修补、拒绝方向分析等可解释性方法。

### 📊 实验结果
**数据集**：AdvAudio-Prosody（600样本），Qwen2-Audio-7B-Instruct

**主要指标**：
- Qwen2-Audio上：Panic 38/95，Anger 35/95，Fast 32/95，均远超Neutral 4/95
- 六条件池化：44/95（46.3%），超过StyleBreak（27/95）
- 消融：情感音频 alone（44/95）远超情感文本 alone（11/95）
- 同语音池（不含Commanding）：40/95

**是否开源**：暂无

### ⭐ 评分：8/10
首次系统研究韵律越狱攻击，贡献方法论。控制变量实验设计严谨，结论有说服力。揭示了语音LLM的新攻击面。创新性强，对语音安全有重要启示。

---

## 语音大模型

## [4] Voice Memory for Agentic Speech Recognition

**arXiv ID**：2607.26410 | **方向**：语音识别

**作者**：Chao-Han Huck Yang, Zih-Ching Chen, Piotr Zelasko, Zhehuai Chen, Jagadeesh Balam, Boris Ginsburg

**机构**：NVIDIA

**发布日期**：2026-07-29 | **论文**：https://arxiv.org/abs/2607.26410 | **PDF**：https://arxiv.org/pdf/2607.26410.pdf | **代码**：https://huggingface.co/huckiyang/voice-memory | **Demo**：https://huckiyang.github.io/voice-memory/

### 📌 简介
Voice Memory提出一种推理时仅需语音识别的智能语音识别方案：冻结的corrector读取每个领域的memory.md文件，每帧决定是修改假设还是保持1-best。异步地，score-gated优化器通过有限编辑修订memory。核心发现是约束发现"克制"是关键技能：无约束生成误差校正（GER）过度修正（金融新闻上64%的编辑破坏了正确token），Voice Memory将此降至35%。

### 🔧 技术方案

**核心创新：** (1) listener-thinker架构：listener是同步解码和决策路径，thinker是异步改进memory的后台路径，两角色仅通过memory耦合。(2) 可验证奖励vs oracle：决策策略通过验证门控优化，而非传统的WER指标。(3) 可移植性：memory可在不同corrector家族间迁移。

**训练策略：** 无需权重更新，仅通过前向传播优化memory文件。使用Semantic-gated记忆优化，使用语义相似度作为训练信号优于WER。

### 📊 实验结果
**数据集**：HyPoradise（10领域）、CHiME-4、NOIZEUS

**主要指标**：
- HyPoradise加权WER：8.36%→7.52%（使用memory），7.47%（加3个in-context样本）
- 航空指令：8.40%→3.40%
- CHiME-4远场：12.69%→10.46%
- 无领域回归任何数据集到1-best基线以下
- memory可跨corrector迁移

**是否开源**：已开源：https://huggingface.co/huckiyang/voice-memory

### ⭐ 评分：9/10
创新性强，首次将"记忆"概念引入ASR。无需训练的核心突破对部署有重要意义。实验充分，在多个基准验证。代码和模型已开源。实用性突出。

---

## [5] Qwen-Audio-3.0-Gen-Preview Technical Report

**arXiv ID**：2607.27011 | **方向**：音频大模型

**作者**：Junyu Dai, Xiaoyue Duan, Xinyue Fan, Yihan Feng, Xiangang Li, Yunjia Li, Lejun Min, Yufei Shi, Xingchen Song, Yiran Wang, Cheng Wen, Menglin Wu, Bajian Xiang, Huaicheng Zhang, Han Zhao, Ruichen Zheng

**机构**：Alibaba DAMO Academy, China

**发布日期**：2026-07-29 | **论文**：https://arxiv.org/abs/2607.27011 | **PDF**：https://arxiv.org/pdf/2607.27011.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
Qwen-Audio-3.0-Gen-Preview是一个统一非自回归框架，使用Diffusion Transformer (DiT)和共享变分自编码器（VAE）生成完整混合波形。提示增强将自由形式请求转换为结构化时序记录，两阶段数据课程和语义条件视图训练模型跨领域使用条件。在Seed-TTS-Eval上实现高说话人相似度，多speaker基准上跨轮一致性高于Seed-Audio-1.0。

### 🔧 技术方案

**模型架构：** DiT + 共享连续VAE（48kHz立体声压缩到25Hz潜序列）+ 提示增强模块。

**核心创新：** (1) 共享VAE压缩48kHz立体声波形，单一表示处理语音、音乐、音效及其混合。(2) 提示增强：将自由形式请求转换为结构化时序记录。(3) 两阶段数据课程训练。

**训练策略：** 两阶段：语义条件视图训练→跨领域条件使用。

### 📊 实验结果
**数据集**：Seed-TTS-Eval、AudioCaps、SongBench

**主要指标**：
- Seed-TTS-Eval说话人相似度：主要优势在三个子集上
- 多speaker基准：跨轮一致性高于Seed-Audio-1.0（中英）
- AudioCaps：大型音频语言模型评估和AudioBox上优势明显
- 时间定位：比Seed-Audio-1.0更强
- SongBench：使用约10%音乐数据，保持接近并在三个组件领先

**是否开源**：暂无

### ⭐ 评分：8/10
音频LLM的重要进展，统一生成框架设计新颖。跨模态能力突出，工程量大。消融实验可更详尽。期待正式版本。

---

## 语音前端/TTS

## [6] Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens

**arXiv ID**：2607.26350 | **方向**：自监督学习、语音表示

**作者**：Daigo Takizawa, Tomohiko Nakamura, Samuele Cornell, William Chen, Satoru Fukayama, Shinji Watanabe

**机构**：National Institute of Advanced Industrial Science and Technology (AIST), Japan; Carnegie Mellon University, USA

**发布日期**：2026-07-28 | **论文**：https://arxiv.org/abs/2607.26350 | **PDF**：https://arxiv.org/pdf/2607.26350.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文系统分析基于神经音频codec（NAC）token的自监督学习（SSL）中的语言敏感性。实验表明：下游性能对NAC训练语言不敏感，但强烈依赖于SSL预训练语言。这一发现表明单个NAC可以跨语言重用，而SSL预训练语言与目标语言对齐至关重要。

### 🔧 技术方案

**实验设计：** 分离NAC和SSL预训练阶段的语言敏感性分析。RQ1：NAC训练语言对重建语音的下游性能影响。RQ2：SSL预训练语言对codec-based SSL性能影响。RQ3：固定SSL预训练语言后，NAC训练语言的影响。

**模型：** 使用HuBERT框架训练codec-based SSL，使用DAC作为NAC。

**评估任务：** ASR（WER/CER）和SER（情感识别），语言：英语、日语、中语。

### 📊 实验结果
**数据集**：
- NAC训练：EN+/JP/ZH/All条件
- SSL预训练：LibriSpeech/日文广播/中文语音
- 下游：LL-10h、LTVS-100h、WS-100h、AS1等

**主要指标**：
- RQ1：DAC训练语言对重建语音下游性能影响有限，CoV < 3.38%
- RQ2：SSL预训练语言敏感性强，CoV达42.99%
- RQ3：固定SSL预训练语言后，NAC训练语言影响有限，CoV < 3.90%
- 结论：NAC可跨语言重用，SSL预训练语言需与目标语言对齐

**是否开源**：暂无

### ⭐ 评分：8/10
系统性的语言敏感性分析，实验设计严谨。首次量化NAC vs SSL的语言敏感性贡献。结论对实践有重要指导意义。创新性强，填补领域空白。

---

## [7] Zero-Shot Face-to-Speech Synthesis via Latent Space Adaptation of a Style-Diffusion TTS Model

**arXiv ID**：2607.26742 | **方向**：TTS、语音合成

**作者**：Carlos Muñoz-Romero, Jose A. Gonzalez-Lopez

**机构**：Universitat Oberta de Catalunya (UOC), Spain; Monoceros Labs, Spain; University of Granada, Spain

**发布日期**：2026-07-29 | **论文**：https://arxiv.org/abs/2607.26742 | **PDF**：https://arxiv.org/pdf/2607.26742.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
Face-to-Speech (F2S)框架从静态面部图像预测语音。轻量级Face Adapter配合face encoder上层的soft-tuning，将face recognition特征对齐到冻结StyleTTS 2模型的style空间。在LRS3数据集上评估，未见身份语音自然度高（UTMOS 3.7-4.0），face-to-voice检索持续高于随机，零样本跨语言迁移到西班牙语也产生流畅语音。

### 🔧 技术方案

**模型架构：** InceptionResnetV1 (VGGFace2预训练) + Face Adapter MLP (512→1024→1024→128) + 冻结StyleTTS 2声学教师。

**核心创新：** (1) Freeze-Align策略：冻结StyleTTS 2作为教师，训练Face Adapter和对face encoder上层进行soft-tuning。(2) 混合对比损失：InfoNCE + RKD + 方差正则 + 人口统计辅助头。(3) 推理时特征解耦： timbre与prosody分离，暴露可调的身份-自然度权衡。

**训练策略：** 平衡采样器（每speaker 4样本），200 epochs，lr 2e-3，cosine annealing。

### 📊 实验结果
**数据集**：LRS3（英语）、内部西班牙语语料库

**主要指标**：
- Face→voice检索：Top-1 9.3%（2.2×随机），Top-5 35.1%
- SECS（embedding级）：0.40-0.42
- UTMOS（英语）：3.7-4.0 vs 真实语音3.61
- 零样本西班牙语：UTMOS 2.7-2.9，face-to-style映射与语言无关

**是否开源**：暂无

### ⭐ 评分：8/10
有趣的跨模态映射任务，创新性较强。零样本跨语言能力有价值。消融实验验证各损失组件贡献。推理时控制机制是亮点。

---

## [8] Unfolded Recursive Expectation-Maximization Neural Network for Speaker Tracking

**arXiv ID**：2607.26575 | **方向**：说话人跟踪

**作者**：Rina Veler, Sharon Gannot

**机构**：Bar Ilan University, Israel

**发布日期**：2026-07-29 | **论文**：https://arxiv.org/abs/2607.26575 | **PDF**：https://arxiv.org/pdf/2607.26575.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
提出深度展开的递归EM（REM）网络用于在轻度混响环境中鲁棒跟踪单个移动说话人。与依赖固定步长衰减 schedules的传统REM算法不同，架构通过将迭代过程展开为可微分层来学习自适应更新策略。引入Step Size Network，利用Feature-wise Linear Modulation (FiLM)和Positional Encoding (PE)根据时序上下文和收敛状态动态调整递归权重。

### 🔧 技术方案

**模型架构：** 编码器-解码器结构 + FiLM/PE驱动的Step Size Network。编码器将候选空间位置映射到初始PRP向量，解码器将精化PRP估计映射回空间坐标。

**核心创新：** (1) 深度展开CREM：将递归EM步骤嵌入编码器-解码器结构。(2) FiLM+PE动态步长学习：根据当前收敛状态和时序上下文学习自适应步长γ_t，而非使用固定衰减schedule。(3) 加权损失：时间加权复合损失，处理REM初始收敛期。

**训练策略：** 梯度裁剪（1.5）、权重衰减（1e-4）、方差clamp（50）、Adam优化器（lr 1e-3）。

### 📊 实验结果
**数据集**：WSJ语料库模拟（混响室，8麦克风对，T60=0-0.3s）

**主要指标**：
- 无混响（T60=0）：RMSE 0.25m vs CREM基线0.28-1.44m
- 混响（T60=0.3s）：RMSE 0.55m vs CREM基线0.74-0.86m
- learned γ_t在无混响时收敛到~0.25，在混响时降低到0.02-0.1

**是否开源**：暂无

### ⭐ 评分：7/10
算法展开+自适应步长的有趣应用。消融验证了learned step size的有效性。在动态场景下优于传统REM。混响条件下性能仍有提升空间。

---

*Generated on 2026-07-30*
