# 2026-08-04 语音论文速递

**共收录**: 13 篇 | **TTS**: 4 篇 | **ASR**: 2 篇 | **安全**: 3 篇 | **增强**: 2 篇 | **其他**: 2 篇

> 今日 arXiv 语音相关论文共命中 13 篇。
> 以下是按评分排序的结果。

---

## 🤖 TTS

---

## [1] JoyAI-Talker: Full-Duplex Speech Interactive Large Model Built for Empathetic Voice Agents

**arXiv ID** 2608.01119 | **方向** TTS

**作者**：Yinhao Bai, Jinming Chen, et al.

**机构**：JD.com

**发布日期**：2026-08-04 | **论文** https://arxiv.org/abs/2608.01119 | **PDF** https://arxiv.org/pdf/2608.01119.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
JoyAI-Talker是京东推出的全双工语音对话系统，在保持强大基础模型能力的同时实现共情交互和语音代理智能。该系统采用模块化的Thinker-Talker架构，将认知规划、对话状态协调和语音生成解耦，并实现了统一的语音-文本联合训练流程以缓解常见的"认知退化"瓶颈，从而在将模型能力扩展到语音交互的同时保持其核心文本推理、STEM和逻辑能力。

### 🔧 技术方案

**模型架构**：Thinker-Talker模块化架构，Thinker负责推理和共情，Talker负责语音生成。

**核心创新**：1）统一语音-文本联合训练流程，从预训练中期开始融合；2）PAER（人格适应共情响应）框架，从音频中提取说话人属性（性别、年龄、情绪），结合CoT推理生成共情响应；3）Joy-Duplex基于状态的全双工交互框架。

**训练策略**：多阶段训练，包括预训练、联合训练和微调。

### 📊 实验结果
**数据集**：T2T基准、S2T基准、Full-Duplex-Bench v1.5、MATH

**主要指标**：
- T2T和S2T基准：达到竞争力性能
- MATH基准：94.62%
- Full-Duplex-Bench v2.5：响应率0.88，误触发率极低

**是否开源**：暂无

### ⭐ 评分：9/10
首个展示全双工语音交互能力的国产大模型，架构设计清晰，实验充分。解决了语音交互中的核心挑战——如何在保持推理能力的同时实现自然的全双工对话。

---

## [2] Experience-Calibrated Contrastive Decoding for Mitigating Hallucinations in LM-Based Text-to-Speech

**arXiv ID** 2608.00722 | **方向** TTS

**作者**：Chenlin Liu, Minghui Fang, Zhonghao Bi, Zekai Su, Rong Wang, Jiqing Han

**机构**：Harbin Institute of Technology, Zhejiang University

**发布日期**：2026-08-03 | **论文** https://arxiv.org/abs/2608.00722 | **PDF** https://arxiv.org/pdf/2608.00722.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
基于语言模型的文本转语音（LM-based TTS）容易受到语音幻觉的影响，即生成的语音偏离目标文本。现有缓解方法主要依赖架构改变或额外训练，而解码时控制仍缺乏探索。本文提出条件信息视角，区分来自文本的对齐信息和来自声学上下文及学习到的语音规律的经验信息。本文假设一类重要的幻觉始于所选token的对齐支持不足。通过使用有无文本条件的同一语音LM的预测，提出经验校准对比解码（ECCD），这是一种训练-free方法，可在保留有用经验信息的同时增强对齐支持。

### 🔧 技术方案

**模型架构**：基于LM的TTS系统，结合文本条件编码器。

**核心创新**：1）条件信息视角区分文本对齐信息和经验信息；2）ECCD在不解码时控制幻觉；3）经验兼容性系数（ECC）动态调整增强强度。

**训练策略**：训练-free方法，无需额外训练即可应用。

### 📊 实验结果
**数据集**：SeedTTS-Eval, CV3-Eval

**主要指标**：
- SeedTTS-Eval：四个模型WER/CER最多降低55.6%
- CV3-Eval：25个多语言设置中24个取得改进
- 主观评测：CMOS +0.644，同时保持说话人相似度

**是否开源**：暂无

### ⭐ 评分：9/10
首个TTS解码时的条件信息分析方法，无需训练即可缓解幻觉。方法创新性强，对LM-based TTS有重要实用价值。

---

## [3] Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS via Interactive Optimization of Individual Emotion Perception Spaces

**arXiv ID** 2608.00998 | **方向** TTS

**作者**：Wangzixi Zhou, Bagus Tris Atmaja, Sakriani Sakti

**机构**：Nara Institute of Science and Technology, Japan

**发布日期**：2026-08-03 | **论文** https://arxiv.org/abs/2608.00998 | **PDF** https://arxiv.org/pdf/2608.00998.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
对话AI的兴趣增加推动了对情感TTS的研究。大多数系统依赖离散情感标签，无法捕捉人类情感的细微差别。近期模型采用Russell的唤醒度-效价（A-V）维度表示，但情感感知因人而异，这可能导致建模情感与感知情感不匹配。本文提出个性化和文化自适应的情感TTS框架，通过交互遗传算法对个性化A-V感知空间进行交互优化。

### 🔧 技术方案

**模型架构**：交互式遗传算法（IGA）+ 情感控制器。

**核心创新**：1）将情感个性化定义为低维感知优化问题；2）交互遗传算法根据用户偏好反馈迭代优化A-V坐标；3）为每个听众获得个性化的Russell环效模型变体。

**训练策略**：用户交互反馈驱动的在线优化，无需修改骨干声学模型。

### 📊 实验结果
**数据集**：中日印尼三国用户评估

**主要指标**：
- MOS：3.37提升到3.75
- WER相对降低23.5%
- 个性化偏好率76%，文化适应偏好率64-70%

**是否开源**：暂无

### ⭐ 评分：8/10
INTERSPEECH 2026接收论文。首次系统研究情感感知的个性化和文化差异，对对话AI有重要方向指引意义。

---

## [4] SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zero-Shot Tasks

**arXiv ID** 2608.02023 | **方向** TTS

**作者**：Yu Zhang, Ruiqi Li, Changhao Pan, Ke Lei, Xiang Yin, Cheng Yang

**机构**：ByteDance, Zhejiang University

**发布日期**：2026-08-05 | **论文** https://arxiv.org/abs/2608.02023 | **PDF** https://arxiv.org/pdf/2608.02023.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音和音频生成在动画配音、音频剧、电影、广告、游戏、播客和短视频制作中经常需要。在这些场景中，创作者可能需要设计没有参考录音的语音、用自然语言控制说话人风格、支持环境和音效的声学场景，并重用设计的语音。因此，支持指令和零样本任务的多说话人语音和音频生成非常重要。

### 🔧 技术方案

**模型架构**：SwanTale多说话人表达语音生成模型，支持zero-shot和instruct两种任务。

**核心创新**：1）SwanData-Caption数据清洗和标注；2）SwanVAE支持高质量多音频模态生成；3）GRPO后训练和课程学习。

**训练策略**：统一多任务多模态建模，使用GRPO进行后训练。

### 📊 实验结果
**数据集**：内部数据集

**主要指标**：
- Zero-shot和instruct指标领先
- 两种任务上表达分数最佳
- 支持复杂指令生成涉及多说话人语音和音频

**是否开源**：项目页面将公开

### ⭐ 评分：8/10
字节在语音生成领域的最新工作，统一框架覆盖多种场景。数据工程和训练策略都有创新。

---

## 🎤 ASR

---

## [5] Normal-Anchored First-Order Model-Agnostic Meta-Learning based Whisper Fine-Tuning for Enhancing Fairness of Cleft Lip and Palate Speech Recognition

**arXiv ID** 2608.00186 | **方向** ASR

**作者**：Susmita Bhattacharjee, Jagabandhu Mishra, H.S. Shekhawat, Ravi Jasuja, S.R. Mahadeva Prasanna

**机构**：IIT Guwahati, University of Eastern Finland, Harvard Medical School, IIIT Dharwad

**发布日期**：2026-08-01 | **论文** https://arxiv.org/abs/2608.00186 | **PDF** https://arxiv.org/pdf/2608.00186.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
唇腭裂（CLP）语音的自动语音识别由于与典型语音相比在声学和发音上的变异性而具有挑战性。这导致ASR设备对CLP语音的识别能力下降。标准微调方法训练的模型难以泛化到其他CLP群体。本文提出Normal-Anchored First-Order Model-Agnostic Meta-Learning (NA-FOMAML)，通过一级双层元学习框架对Whisper进行CLP语音微调。

### 🔧 技术方案

**模型架构**：Whisper + NA-FOMAML元学习框架。

**核心创新**：1）正常语音锚定内层，内层使用正常语音作为支持集；2）外层加入病理语音；3）部分编码器微调策略探索。

**训练策略**：双层优化：内层使用正常语音，外层使用不同严重程度的CLP语音。

### 📊 实验结果
**数据集**：NMCPC, AIISH

**主要指标**：
- NMCPC配置WER：正常4.40%，轻度5.53%，中度16.14%，重度52.07%
- 音素级错误分析显示严重语音在摩擦音、破擦音、鼻音、流音、塞音和元音上错误率高

**是否开源**：暂无

### ⭐ 评分：8/10
针对病理语音识别的公平性问题提出创新性元学习方案。INTERSPEECH 2026发表，对医疗语音处理有重要价值。

---

## [6] Latent Softmax for Data-Efficient Phoneme-Based Multilingual ASR Across Tonal and Non-Tonal Languages

**arXiv ID** 2608.01281 | **方向** ASR

**作者**：Saierdaer Yusuyin, Nanling Jiang, Hao Huang, Zhijian Ou

**机构**：Xinjiang University, University of Science and Technology of China, Tsinghua University, TasiTech

**发布日期**：2026-08-03 | **论文** https://arxiv.org/abs/2608.01281 | **PDF** https://arxiv.org/pdf/2608.01281.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
基于音素的多语言自动语音识别（ASR）可以比语言特定的子词建模更直接地共享声学证据。当带调语言和非带调语言联合训练时，它们的监督粒度不匹配：带调语言标注带调元音，而非带调语言通常只提供基元音标签。标准softmax要么将两者视为不相关类别，削弱跨语言共享，要么合并声调，失去带调语言所需的区分度。

### 🔧 技术方案

**模型架构**：Latent Softmax + CTC兼容输出层。

**核心创新**：1）将带调元音建模为子类，基元音为母类；2）边缘化推断，仅观测到基元音母类标签时处理带调元音子类；3）辅音和CTC blank保持单独标签。

**训练策略**：多语言联合训练，优化子类-母类关系。

### 📊 实验结果
**数据集**：AISHELL-1, LibriSpeech

**主要指标**：
- S2P音素错误率相比标准Softmax多语言基线降低：
  - AISHELL-1: 8.4%
  - LibriSpeech test-clean: 17.5%
  - test-other: 12.6%

**是否开源**：代码将公开

### ⭐ 评分：8/10
针对声调语言的创新性多语言ASR方案，有效解决带调和非带调语言联合训练的粒度不匹配问题。

---

## 🛡️ 安全

---

## [7] Hidden-Domain Routing for All-Type Audio Deepfake Detection

**arXiv ID** 2608.00493 | **方向** 安全

**作者**：Yifan Gao, Yao Tian, Hongbin Suo, Haonan Lu

**机构**：OPPO AI Center, Beijing & Shenzhen

**发布日期**：2026-08-02 | **论文** https://arxiv.org/abs/2608.00493 | **PDF** https://arxiv.org/pdf/2608.00493.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音深度伪造检测（SDD）系统在传统基准上取得良好性能，但现有方法难以处理所有类型的音频deepfake。OPPO提出隐藏域路由方案，首先恢复隐藏音频类型，然后在该分支内解释检测器分数。

### 🔧 技术方案

**模型架构**：路由系统 + 分支检测器。

**核心创新**：1）AudioType-BEATs-6s Router从6秒窗口估计音频类型；2）分支检测器：Speech-XLSR（语音）、SoundMusic-EAT（声音/音乐）、Singing-EAT（歌唱）；3）分支局部分数解释使用各自决策阈值。

**训练策略**：多阶段训练，先训练路由，再训练各分支检测器。

### 📊 实验结果
**数据集**：AT-ADD Challenge

**主要指标**：
- AT-ADD Track2最终评估：96.10% Macro-F1（排名第一）
- 各类型Macro-F1：语音88.07%，声音98.18%，歌唱99.07%，音乐99.08%

**是否开源**：ACMMM 2026接收

### ⭐ 评分：9/10
业界领先的全类型音频deepfake检测方案，AT-ADD Challenge Track2冠军。架构设计创新，对实际应用有重要价值。

---

## [8] REIMU: Efficient Heterogeneous Hierarchical Reasoning for SSL-Based Speech Deepfake Detection

**arXiv ID** 2608.00857 | **方向** 安全

**作者**：Kwok-Ho Ng, Tingting Song, Bingwen Feng, Peiya Li

**机构**：西北工业大学

**发布日期**：2026-08-03 | **论文** https://arxiv.org/abs/2608.00857 | **PDF** https://arxiv.org/pdf/2608.00857.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
基于自监督学习（SSL）的语音深度伪造检测近期取得进展，但缺乏对层次推理架构的系统研究。本文比较单次前向、权重共享循环、同质层次推理模块（HRM）和异构HRM，验证不同架构对检测性能的影响。

### 🔧 技术方案

**模型架构**：异构层次推理模块。

**核心创新**：1）异构操作分配：高级模块使用MHSA，低级模块使用线性注意力（GDN2或Raven）；2）参数高效设计；3）系统比较不同推理架构。

**训练策略**：标准SSL预训练 + 下游任务微调。

### 📊 实验结果
**数据集**：ASVspoof 2019, ASVspoof 2021

**主要指标**：
- 异构配置在多个设置下达到竞争力性能
- 在19LA、21LA、21DF上EER表现优异
- 比匹配基线减少10.8%的下游参数

**是否开源**：暂无

### ⭐ 评分：7/10
系统比较不同层次推理架构对语音deepfake检测的影响，为后续研究提供有价值的设计指南。

---

## [9] Anomalous Sound Detection Meets Noise-Aware Self-Supervised Learning

**arXiv ID** 2608.00447 | **方向** 安全

**作者**：Takuya Fujimura, Gordon Wichern, Yoshiki Masuyama, et al.

**机构**：NTT Corporation

**发布日期**：2026-08-02 | **论文** https://arxiv.org/abs/2608.00447 | **PDF** https://arxiv.org/pdf/2608.00447.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
异常声音检测（ASD）旨在检测机器运行中的异常。DCASE挑战推动了该领域的发展，但实际应用中麦克风记录往往包含噪声。本文提出噪声感知自监督学习（NA-SSL），利用远场麦克风录音作为辅助信息提取近场麦克风的干净SSL表示。

### 🔧 技术方案

**模型架构**：NA-BEATs/NA-EAT/NA-Dasheng噪声感知SSL模型。

**核心创新**：1）模拟双通道录音：使用FSD50K（目标声音）+ WHAM!/DEMAND/QUT-NOISE（噪声）；2）噪声感知扩展三种基础SSL模型；3）远场-近场联合学习。

**训练策略**：预训练 + 领域自适应。

### 📊 实验结果
**数据集**：DCASE 2026 Challenge Task 2

**主要指标**：
- NA-BEATs官方评估得分：70.24%（排名第一）
- 第二名：65.46%
- 官方基线：59.80%

**是否开源**：DCASE 2026 Challenge Track 2冠军

### ⭐ 评分：9/10
首个将噪声感知SSL应用于异常声音检测的工作，获挑战赛冠军。对实际工业应用有重要价值。

---

## 🔊 增强

---

## [10] AnyBand: Unified Multi-Bandwidth Speech Extension

**arXiv ID** 2608.00572 | **方向** 增强

**作者**：Junchuan Zhao, Minh Duc Vu, Bowen Zhang, Ye Wang

**机构**：National University of Singapore

**发布日期**：2026-08-02 | **论文** https://arxiv.org/abs/2608.00572 | **PDF** https://arxiv.org/pdf/2608.00572.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
带宽扩展（BWE）旨在从窄带输入恢复丢失的高频信息。传统方法针对特定带宽设计，难以泛化。本文将统一多带宽扩展重新表述为上下文频谱填充问题，提出频率感知Diffusion Transformer。

### 🔧 技术方案

**模型架构**：频率感知Diffusion Transformer + 频率感知模块。

**核心创新**：1）统一多带宽扩展为上下文频谱填充；2）频率感知Diffusion Transformer建模跨频率交互和长距离时序依赖；3）Easy-to-Balanced cutoff课程；4）多视角对抗细化。

**训练策略**：课程学习，从高截止频率逐渐过渡到均匀采样。

### 📊 实验结果
**数据集**：VCTK, EARS

**主要指标**：
- 2kHz输入：LSD 1.248, NISQA 3.125, STOI 0.8214
- 8kHz输入：LSD 1.086, NISQA 4.014, STOI 0.9870
- 不规则带宽泛化性能优异

**是否开源**：暂无

### ⭐ 评分：8/10
创新性地将BWE统一为频谱填充任务，支持任意带宽输入。方法创新，实验充分。

---

## [11] DroneAudioNet: Noise Suppression for Drone Audition-based Search and Rescue

**arXiv ID** 2608.00875 | **方向** 增强

**作者**：Chitralekha Gupta, Soundarya Ramesh, Yifei Luo, Suranga Nanayakkara

**机构**：National University of Singapore

**发布日期**：2026-08-03 | **论文** https://arxiv.org/abs/2608.00875 | **PDF** https://arxiv.org/pdf/2608.00875.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
无人机搜救中，使用无人机麦克风捕捉人类语音是一个重要任务，但无人机螺旋桨噪声严重影响语音质量。传统语音增强方法在低信噪比下效果有限。本文将源分离模型重新表述为无人机噪声估计器，提出 DroneAudioNet。

### 🔧 技术方案

**模型架构**：噪声估计重构 + 可学习mask缩放 + 加性残差校正。

**核心创新**：1）噪声估计重构：将源分离模型重新表述为无人机噪声估计器；2）可学习mask缩放：允许mask幅度超过1；3）加性复数残差项。

**训练策略**：端到端训练，优化语音分类性能。

### 📊 实验结果
**数据集**：DREGON, 内部数据集

**主要指标**：
- 人类语音分类F1分数最大提升10.6%（-20到-10 dB SNR）
- 域外泛化：在DREGON数据集上有效

**是否开源**：暂无

### ⭐ 评分：8/10
针对无人机搜救场景的噪声抑制，对低SNR有独特优化。应用场景明确，方法有针对性。

---

## 🔬 其他

---

## [12] SoniSpeech: Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces

**arXiv ID** 2608.00803 | **方向** 其他

**作者**：Ruidong Zhang, Jiacheng Liu, François Guimbretière, Cheng Zhang

**机构**：Cornell University

**发布日期**：2026-08-03 | **论文** https://arxiv.org/abs/2608.00803 | **PDF** https://arxiv.org/pdf/2608.00803.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
无声语音接口允许用户在不影响他人的情况下与设备交互。当前无声语音研究因缺乏大规模数据而受限。本文提出SoniSpeech，首个大规模可穿戴无声语音接口三模态数据集，包含超声回波profile、有声音频和前视视频。

### 🔧 技术方案

**模型架构**：声学传感眼镜 + CTC ResNet-34基线。

**核心创新**：1）三模态数据集：超声回波profile + 有声音频 + 前视视频；2）FMCW chirp捕捉面部运动；3）SODA对话语料。

**训练策略**：纯无声训练和有声+无声联合训练对比。

### 📊 实验结果
**数据集**：SODA对话语料（5356个唯一词汇）

**主要指标**：
- 纯无声训练：WER 33.7%（首次基准）
- 有声+无声联合训练：WER 26.3%
- 训练数据规模效应：数据越多性能越好

**是否开源**：数据集将公开

### ⭐ 评分：9/10
首个大规模可穿戴无声语音接口数据集，推动该领域研究。数据工程价值高。

---

## [13] Beyond Prompt Adherence: Auditing Attribute-Level Voice Control in Speech Generation

**arXiv ID** 2608.00545 | **方向** 其他

**作者**：Xianhao Zhou, Jianghao Wu

**机构**：Intelligence团队

**发布日期**：2026-08-02 | **论文** https://arxiv.org/abs/2608.00545 | **PDF** https://arxiv.org/pdf/2608.00545.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音生成模型的属性控制是重要研究方向，但现有评估仅关注prompt遵循度，忽视属性级控制保真度。本文提出配对审计和属性级控制评估，系统评估语音生成中的属性控制。

### 🔧 技术方案

**模型架构**：配对审计框架 + VoDER-Cal候选选择器。

**核心创新**：1）配对审计：将条件化输出与中性基线配对比较；2）属性级控制评估：测量目标属性变化和非目标属性变化；3）三候选池策略。

**训练策略**：无需训练的候选选择器。

### 📊 实验结果
**数据集**：内部评估集

**主要指标**：
- CosyVoice3：deep响应率84.4%，但93.8%有非目标变化
- VoDER-Cal在保留目标响应方面优于基线选择
- 联合成功率从4.8%提升到约14%

**是否开源**：暂无

### ⭐ 评分：8/10
首个系统评估语音生成中属性控制保真度的研究，为后续控制方法提供评估基准。
