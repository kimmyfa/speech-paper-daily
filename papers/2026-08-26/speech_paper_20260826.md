# 2026-08-26 语音论文速递

**共收录**: 12 篇 | **语音大模型**: 6 篇 | **语音前端**: 6 篇

> 目标日期 2026-08-26 arXiv 语音相关论文共命中 12 篇（补录）。
> 数据来源 arxivdaily 镜像，基于页面 AI 总结与 comments 精炼，按评分排序。

---

## 语音大模型

## [1] EXAM$^2$: Extending Audio Understanding in Multilingual and Multimodal Analysis

**arXiv ID**：2608.23758 | **方向**：语音大模型

**作者**：Jiawen Wang, Xiaoxue Gao, Zi Haur Pang, Nancy F. Chen

**机构**：暂无公开机构信息

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.23758 | **PDF**：https://arxiv.org/pdf/2608.23758 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出多语言多模态音频理解基准 EXAM²，系统评估现有音频语言模型在多语言、多模态理解上的表现，发现模型存在明显的多语言跨模态理解差距。作者进一步构建微调的 Gemma3n-EXAM² 模型，其性能较基线显著提升，为多语言音频理解研究提供了新的评测工具与改进方向。核心价值在于填补了现有基准对非英语语言与多模态结合场景覆盖不足的空白。

### 📊 实验结果
**数据集与关键信息**：构建 EXAM² 多语言多模态音频理解基准；微调的 Gemma3n-EXAM² 相比基线模型性能显著提升，具体数值详见页面 AI 总结（comments：8 pages, 2 figures）。

### ⭐ 评分：7/10
创新性较突出，是面向多语言跨模态音频理解的首批评测基准之一，具有较高的评测与社区价值；但仅基于 AI 总结与 comments 判断，缺少公开代码与详细指标披露。

---

## [2] GRGA: Graph-based Retrieval-Generation Agent for Long-form Audio Meeting Understanding

**arXiv ID**：2608.24048 | **方向**：语音大模型

**作者**：Quanwei Tang, Dong Zhang, Shoushan Li, Guodong Zhou

**机构**：江苏省语言计算重点实验室

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.24048 | **PDF**：https://arxiv.org/pdf/2608.24048 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对长音频会议理解任务中问答数据集稀缺、现有语音模型声学信息丢失与长期记忆能力差的问题，本文构建了 LongAudioQA 数据集，并提出基于图的检索-生成智能体（GRGA）。GRGA 利用智能体规划实现检索与答案生成，将语义信息组织为图结构以缓解长期记忆与信息丢失问题。该工作已被 ACL Findings 2026 接收，为长会议场景下的语音理解提供了新的数据资源与建模范式。

### 📊 实验结果
**数据集与关键信息**：构建 LongAudioQA 长音频会议问答数据集；GRGA 模型通过图结构检索-生成智能体提升长音频会议问答性能，具体指标详见页面 AI 总结（ACL Findings 2026 Accepted）。

### ⭐ 评分：7/10
面向长音频会议 QA 这一实用痛点，数据集与图检索智能体方案配套、场景价值明确；但依赖 AI 总结信息，缺乏可复现的代码链接与量化对比细节。

---

## [3] EmoTra-TTS: Smooth Intra-Utterance Emotion Transitions for Speech Synthesis

**arXiv ID**：2608.23791 | **方向**：语音大模型

**作者**：Tianchi Liu, Zeyang Song, Tianrui Wang, Zhipeng Li, Chenglin Xu, Yiwen Guo

**机构**：暂无公开机构信息

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.23791 | **PDF**：https://arxiv.org/pdf/2608.23791 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有情感 TTS 系统往往忽视情感的时间演化特性，无法生成句内平滑情感转换。EmoTra-TTS 采用多遍流混合管道、双阶段 VAD 条件以及方向-幅度解耦注入三大设计，实现流畅的句内情感转换。实验表明其性能优于 SOTA 基线与商业系统，已被 EMNLP 2026 主会接收。

### 📊 实验结果
**数据集与关键信息**：在情感 TTS 数据集上较 SOTA 基线与商业系统取得更优性能，具体指标数值详见页面 AI 总结（Accepted to EMNLP 2026 Main Conference）。

### ⭐ 评分：7/10
切入句内情感动态转换这一未充分解决的情感 TTS 难题，双阶段 VAD 条件与方向-幅度解耦注入设计有技术亮点且被顶会接收；惜未披露代码与具体指标数值，打分依据主要为 AI 总结。

---

## [4] Preference Optimization for Non-Verbal Vocalization Synthesis

**arXiv ID**：2608.24163 | **方向**：语音大模型

**作者**：Haoyang Li, Chenglin Xu, Junchuan Zhao, Yuang Cao, Liumeng Xue, Yiwen Guo, Eng Siong Chng

**机构**：暂无公开机构信息

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.24163 | **PDF**：https://arxiv.org/pdf/2608.24163 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文针对支持非言语发声（情感发声、拟声等）的 TTS 系统研究偏好优化（DPO）设计，提出专门的 NV-CER 指标以评估非言语发声合成质量。作者在 Emilia-NV 等数据集上系统验证了标准 DPO 设置在非言语发声合成中的有效性，为相关后训练提供了实用见解。

### 📊 实验结果
**数据集与关键信息**：在 Emilia-NV 等数据集上验证标准 DPO 设置的有效性并给出 NV-CER 指标；具体数值详见页面 AI 总结。

### ⭐ 评分：6/10
聚焦非言语发声合成后训练这一细分方向并贡献专用评估指标，实用价值不错；但方法整体为对 DPO 的适配性研究，创新幅度有限，且无代码与完整实验细节披露。

---

## [5] Speech-to-SOAP: End-to-End Summarization of Medical Dialogues (KIT@BeTraC 2026)

**arXiv ID**：2608.24327 | **方向**：语音大模型

**作者**：Enes Yavuz Ugan, Fabian Retkowski, Yuka Ko, Thai-Binh Nguyen, Maike Züfle, Jan Niehues, Alexander Waibel

**机构**：Karlsruhe Institute of Technology（卡尔斯鲁厄理工学院）；Carnegie Mellon University（卡内基梅隆大学）

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.24327 | **PDF**：https://arxiv.org/pdf/2608.24327 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文为 KIT 团队参加 BeTraC 2026 挑战赛轻量级赛道提出的医学对话摘要方案，面向语音输入直接生成 SOAP（主观/客观/评估/计划）结构化摘要。通过可扩展的数据增强流水线适配语音基础模型，实现端到端语音到 SOAP 摘要生成，以减轻医护人员病历记录负担。

### 📊 实验结果
**数据集与关键信息**：构建可扩展数据增强流水线并适配语音基础模型完成端到端语音转 SOAP；为挑战赛系统描述论文（3 pages, BeTraC 2026），具体指标详见页面 AI 总结。

### ⭐ 评分：5/10
医学语音摘要应用价值明确且团队背景扎实，但属 3 页挑战赛系统描述，方法以工程适配为主，缺少独立技术贡献与充分实验支撑。

---

## [6] CoSTALA: Compositional Spatio-Temporal Audio-Language Alignment via Multi-Grain Hierarchical Contrastive Learning

**arXiv ID**：2608.24374 | **方向**：语音大模型

**作者**：Peiwei Ren, Jinbo Hu, Fang Kang, Shan Liang, Yin Cao

**机构**：西交利物浦大学；小米公司 MiLM Plus；奥卢大学；中国科学院声学研究所

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.24374 | **PDF**：https://arxiv.org/pdf/2608.24374 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
传统音频语言模型（ALM）难以处理包含多个事件的多事件音频序列。CoSTALA 通过多粒度层次对比学习构建新型训练范式，以组合式时空建模实现对多事件音频序列的理解，为时空音频理解提供了新框架。

### 📊 实验结果
**数据集与关键信息**：提出多粒度层次对比学习训练范式用于组合式时空音频-语言对齐；具体评测数据集与指标详见页面 AI 总结。

### ⭐ 评分：6/10
面向多事件音频序列的对齐难题提出多粒度层次对比方案，想法有新颖性；但仅基于 AI 总结未见量化实验结果，方法与数据集细节不足，暂定中间分。

---

## 语音前端

## [1] REDnet: Recursive Encoder and Decoder for Speech Separation under Unknown Number of Speakers and Variable Number of Microphones

**arXiv ID**：2608.24659 | **方向**：语音前端

**作者**：Fulin Wu, Zhong-Qiu Wang

**机构**：暂无公开机构信息

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.24659 | **PDF**：https://arxiv.org/pdf/2608.24659 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
实际麦克风阵列场景中说话人数量与麦克风数量往往事先未知。REDnet 采用递归编码器和解码器结构，摆脱了对固定说话人数与固定通道数的依赖，同时解决"说话人数量未知"与"麦克风数量可变"两大问题，在多个公开数据集上实现领先性能。

### 📊 实验结果
**数据集与关键信息**：在多个公开语音分离数据集上取得领先性能，较现有固定参数模型更鲁棒；具体 SI-SNR/PESQ 等指标详见页面 AI 总结（in submission）。

### ⭐ 评分：7/10
同时攻克未知说话人数与可变通道数两个实际痛点，递归编码-解码设计思路清晰、实用价值高；缺陷是缺少项目页面与开源信息，仍处于投稿中，指标细节待补。

---

## [2] Visually-Guided Spatial Audio Generation for 360° In-the-Wild Speech Scenes

**arXiv ID**：2608.24579 | **方向**：语音前端

**作者**：Qingyu Luo, Peng Zhang, Wenwu Wang, Philip J. B. Jackson

**机构**：暂无公开机构信息

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.24579 | **PDF**：https://arxiv.org/pdf/2608.24579 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
面向野外 360° 语音场景中空间音频采集设备受限、质量有限的问题，本文提出视觉引导的第一阶声场（FOA）语音空间化方法，并构建 YT-SPEECH 数据集。采用 Localizer-Renderer 框架，从视觉信息估计声源方向并重建定向 FOA 信号，实用地提升了音频相关性能。该工作已被 INTERSPEECH 2026 接收。

### 📊 实验结果
**数据集与关键信息**：构建 YT-SPEECH 野外数据集；Localizer-Renderer 框架实现视觉引导 FOA 重建并提升音频相关指标（Accepted at INTERSPEECH 2026）。

### ⭐ 评分：7/10
将视觉信息用于野外空间音频重建，数据集与任务设定贴合真实场景，被顶级语音会议接收；但具体空间音频指标细节依赖 AI 总结，代码未开源。

---

## [3] Array-Agnostic Ambisonics Encoding via Diffusion Posterior Sampling

**arXiv ID**：2608.24558 | **方向**：语音前端

**作者**：Amit Milstein, Nir Shlezinger, Boaz Rafaely

**机构**：暂无公开机构信息

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.24558 | **PDF**：https://arxiv.org/pdf/2608.24558 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有 Ambisonics 编码方案受固定麦克风阵列布局限制。本文提出生成式框架 ADEPS（Array-agnostic Diffusion Encoding via Posterior Sampling），将物理采集模型嵌入扩散后验采样推理过程，从而补偿阵列失真并实现对任意麦克风阵列的零样本编码，性能优于传统基线。

### 📊 实验结果
**数据集与关键信息**：对任意阵列实现零样本 Ambisonics 编码并补偿阵列失真，性能优于传统基线；具体指标详见页面 AI 总结。

### ⭐ 评分：7/10
将扩散后验采样与阵列物理模型结合，实现阵列无关的空间声场编码，方法创新性与工程实用性兼备；评分基于 AI 总结，缺乏数据集与量化对比细节。

---

## [4] Investigating Voiced and Unvoiced Regions of Speech for Audio Deepfake Detection

**arXiv ID**：2608.24639 | **方向**：语音前端

**作者**：Ganesh Sivaraman, Hemlata Tak, Elie Khoury

**机构**：暂无公开机构信息

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.24639 | **PDF**：https://arxiv.org/pdf/2608.24639 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文探讨语音浊音与清音区域对音频深度伪造检测（ADD）的作用，基于图注意力的 AASIST 系统分别对两类区域单独训练。研究发现清音区域检测效果更优，而融合浊音区域后可进一步提升性能，在 MLAAD 数据集上取得 5.82% 的等错误率（EER）。该工作已被 IEEE ICASSP 2025 接收。

### 📊 实验结果
**数据集与关键信息**：MLAAD 数据集上取得 5.82% EER；清音区域检测效果优于浊音区域，融合两者进一步提升性能（Accepted in IEEE ICASSP 2025）。

### ⭐ 评分：6/10
对 ADD 中浊/清音区域的信息量进行系统研究，实验发现对后续特征设计有参考价值；但本质是对 AASIST 的实证分析，方法创新有限。

---

## [5] On the Robustness of Audio Deepfake Detection under Audio Watermarking

**arXiv ID**：2608.24159 | **方向**：语音前端

**作者**：Zi Qian Yong, Ajinkya Kulkarni, Julia Lau, Hwa Hui Tew, Shu Min Leong, Raphael Phan, Sébastien Marcel

**机构**：莫纳什大学马来西亚校区信息技术学院；瑞士 Idiap 研究所

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.24159 | **PDF**：https://arxiv.org/pdf/2608.24159 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
音频内容认证常同时涉及深度伪造检测（ADD）与音频水印，两者并存时的相互作用尚不清晰。本研究采用 WavMark 水印评估框架探究水印对 ADD 系统的影响，发现水印会大幅降低部分数据集上的 ADD 检测性能，系统性揭示了 ADD 系统的鲁棒性漏洞，为多技术叠加下的既有音频内容生态监管提供了重要实证依据。

### 📊 实验结果
**数据集与关键信息**：使用 WavMark 评估框架；发现音频水印在部分数据集上大幅降低 ADD 性能，揭示鲁棒性漏洞；具体降幅指标详见页面 AI 总结。

### ⭐ 评分：6/10
首次系统评估水印-深伪检测组合下的耦合效应，研究视角新颖、安全意义明确；属评测性质工作，未提出缓解方案，量化细节依赖 AI 总结。

---

## [6] The ISCSLP 2026 Real-World Audio-Visual Speech Enhancement Challenge

**arXiv ID**：2608.23759 | **方向**：语音前端

**作者**：Challenge Organizers

**机构**：暂无公开机构信息

**发布日期**：2026-08-26 | **论文**：https://arxiv.org/abs/2608.23759 | **PDF**：https://arxiv.org/pdf/2608.23759 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文介绍 ISCSLP 2026 真实场景视听语音增强（AVSE）挑战赛——首个面向真实世界场景的 AVSE 挑战。赛事设置真实混合、合成重混等赛道，公布基线结果与相关资源，旨在评估视听语音增强技术在自然场景（而非理想化实验室条件）下的实际性能，推动领域评测向真实场景落地。

### 📊 实验结果
**数据集与关键信息**：发布首个真实世界 AVSE 挑战，含真实混合与合成重混赛道及基线结果；具体指标详见页面 AI 总结（The First Real-World Audio-Visual Speech Enhancement Challenge）。

### ⭐ 评分：5/10
作为挑战赛说明文档，缺失的主要是"方法贡献"，但首倡真实场景 AVSE 评测对领域门槛提升有积极价值；主要成绩在数据集与评测协议构建上。

---

*Generated on 2026-08-28 (补录)*