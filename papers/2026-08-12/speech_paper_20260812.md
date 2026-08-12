# 2026-08-12 语音论文速递

**共收录**: 10 篇 | **语音大模型**: 10 篇 | **语音前端**: 0 篇

> 今日 arXiv 语音相关论文共命中 10 篇。
> 以下是按评分排序的结果。

---

##  语音大模型

---

## [1] Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions

**arXiv ID** 2608.09930 | **方向** 语音大模型

**作者：** Oluwanifemi Bamgbose, Simon Rosen, Jash Shah, Lindsay Devon Brin, Hoang H Nguyen, Anke Koelzer, Rachel Hansen, Tara Bogavelli

**机构：** Carnegie Mellon University, University of Oxford

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09930 | **PDF** https://arxiv.org/pdf/2608.09930.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Automated Text-to-Speech (TTS) evaluation methods (Mean Opinion Score (MOS) predictors and Audio Large Language Models (Audio-LLM) judges) are expected to reflect human perception, yet it is unclear how well they capture the distinct aspects of speech that listeners actually perceive. We deconstruct "naturalness" into a linguistically grounded annotation schema spanning 10 distinct perceptual dime

###  技术方案
本文提出对自动TTS评估器（MOS预测器和Audio-LLM评判器）进行多维度评估。将「自然度」解构为10个语言学感知维度，构建了包含860句标注语料的基准测试。MOS预测器侧重声学信号质量，Audio-LLM评判器表现出选择性、依赖提示词的检测能力，但不能泛化到所有维度。

###  实验结果
对4个MOS预测器和4个Audio-LLM评判器进行了基准测试，数据集、标注模式和评估代码已公开发布。

**是否开源：** 暂无。

###  评分：8/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [2] MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection

**arXiv ID** 2608.09593 | **方向** 语音大模型

**作者：** Yanqiu Li, Yang Xiao, Jisheng Bai, Bin Chen, Hong Jia, Ting Dang

**机构：** The University of Melbourne, Xi'an University of Posts and Telecommunications

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09593 | **PDF** https://arxiv.org/pdf/2608.09593.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Recent advances in speech synthesis and audio generation have made high-fidelity acoustic forgery low-cost and difficult to attribute, enabling a realistic attack scenario in which speech and background audio are independently manipulated over otherwise authentic video. Yet existing research either focuses on visual manipulation, addresses speech detection in isolation, or conflates speech and non

###  技术方案
MADBench：用于模态感知音频深度伪造检测的基准测试。评估评估器在音频-视觉多模态场景下的深度伪造检测能力。

###  实验结果
建立了多模态音频深度伪造检测基准，覆盖多种场景。

**是否开源：** 暂无。

###  评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [3] SonicWeave: Chunk-Routed Mixture-of-Experts for Unified Audio Scene Generation

**arXiv ID** 2608.09571 | **方向** 语音大模型

**作者：** Yunrui Cai, Xu Li, Yucheng Zhou, Jinchao Li, Dingdong Wang, Dongchao Yang, Xixin Wu, Chen Zhang

**机构：** Kling Team, Kuaishou Technology; The Chinese University of Hong Kong

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09571 | **PDF** https://arxiv.org/pdf/2608.09571.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Text-conditioned general audio generation is moving beyond isolated speech, music, and sound-effect synthesis toward a single model that can compose them into controllable, coherent audio scenes. This unified setting is particularly challenging: heterogeneous components impose conflicting structural requirements on a shared backbone, while a complex mixed scene may contain locally distinct or over

###  技术方案
SonicWeave：基于分块路由MoE（Mixture-of-Experts）的统一音频场景生成框架。将音频场景分解为分块处理，通过专家混合机制实现多样化音频生成。

###  实验结果
在多种音频场景生成任务上验证了方法的有效性。

**是否开源：** 暂无。

###  评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [4] AudioMap: Cloze-and-Choice Reinforcement Learning for Time-Aware Dense Audio Captioning

**arXiv ID** 2608.09559 | **方向** 语音大模型

**作者：** Yan Rong, Fengji Ma, Xu Li, Jinting Wang, Chen Zhang, Li Liu

**机构：** The Hong Kong University of Science and Technology (Guangzhou); Kling Team, Kuaishou Technology

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09559 | **PDF** https://arxiv.org/pdf/2608.09559.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Time-aware dense audio captioning (TDAC) aims to generate multiple fine-grained attributes (dense) of the audio with precise time boundaries (time-aware). Existing methods struggle to achieve these two goals and mainly rely on supervised fine-tuning, yielding sub-optimal performance. While reinforcement learning (RL) shows promise, applying it to TDAC faces two main challenges: (1) existing reward

###  技术方案
AudioMap：基于填空-选择强化学习的时间感知密集音频描述方法。提出同时考虑时序和语义的时间感知密集音频captioning任务。

###  实验结果
在音频描述任务上验证了时间感知能力。

**是否开源：** 暂无。

###  评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [5] Dynamic Clustering for Cross-Segment Permutation Alignment in Long Speech Separation

**arXiv ID** 2608.09451 | **方向** 语音大模型

**作者：** Yuzhu Wang, Archontis Politis, Konstantinos Drossos, Tuomas Virtanen

**机构：** Signal Processing Research Centre, Tampere University; Nokia Technologies, Espoo

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09451 | **PDF** https://arxiv.org/pdf/2608.09451.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Long speech separation typically employs a segment-separation-stitch paradigm where recordings are divided into short segments, processed independently, and stitched together. Its challenge lies in predicting cross-segment permutations. This paper proposes a training-free dynamic clustering approach for cross-segment permutation alignment using speaker embedding reference pools. The method predict

###  技术方案
动态聚类用于长语音分离中的跨段排列对齐。在长语音分离任务中，动态调整聚类以处理说话人排列问题，提高分离质量。

###  实验结果
在长语音分离数据集上验证了方法的有效性。

**是否开源：** 暂无。

###  评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [6] Neural Array-Generic Direction-of-Arrival Estimation Exploiting Array Transfer Functions

**arXiv ID** 2608.09425 | **方向** 语音大模型

**作者：** Mikko Heikkinen, Archontis Politis, Konstantinos Drossos, Tuomas Virtanen

**机构：** Tampere University

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09425 | **PDF** https://arxiv.org/pdf/2608.09425.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Direction-of-arrival (DoA) estimation is a key component of multichannel audio processing, yet many deep learning approaches remain tied to the microphone arrays used during training and generalize poorly to unseen devices. This paper proposes an array-generic neural DoA estimation framework using measured or simulated complex directional array transfer functions (ATFs) matched to real-world multi

###  技术方案
利用阵列传递函数的神经阵列通用方向到达估计（DOA）方法。提出不依赖特定麦克风阵列配置的通用DOA估计方法。

###  实验结果
在多种阵列配置上验证了方法的泛化能力。

**是否开源：** 暂无。

###  评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [7] RAG-Audio: Retrieval-Augmented Generation for Faithful Brain-to-Audio Reconstruction

**arXiv ID** 2608.09331 | **方向** 语音大模型

**作者：** Ambuj Mehrish, Sebastiano Vascon

**机构：** Ca' Foscari University of Venice; National University of Singapore

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09331 | **PDF** https://arxiv.org/pdf/2608.09331.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Brain-to-audio reconstruction is limited by \emph{prior domination}: when a pretrained generator is conditioned on a weak neural signal, it produces realistic but stimulus-inaccurate audio. We introduce RAG-Audio, which decodes fMRI into a semantic audio embedding, retrieves a matching real-audio exemplar, and initializes the frozen generator's sampling trajectory from that exemplar while retainin

###  技术方案
RAG-Audio：用于脑电-音频重建的检索增强生成框架。通过检索相关脑电信号来增强音频重建的保真度。

###  实验结果
在脑电-音频重建任务上验证了保真度提升。

**是否开源：** 暂无。

###  评分：8/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [8] DAVE: A Decoupled Audio-Visual Enhancement Framework for Real-World Speech Separation

**arXiv ID** 2608.09288 | **方向** 语音大模型

**作者：** Wei Zhou, Wanyi Ning, Yinshang Guo, Qianxiao Fang, Haitao Qian, Yingpeng Li

**机构：** Tianjin University; Nanjing University

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09288 | **PDF** https://arxiv.org/pdf/2608.09288.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Audio-visual speech enhancement under real-world conditions remains challenging due to unreliable visual inputs and the lack of large-scale training data with realistic acoustic conditions. Existing approaches usually fuse visual features directly into the separation network, making them vulnerable to degraded visual signals. In this paper, we present DAVE, a decoupled audio-visual enhancement fra

###  技术方案
DAVE：用于真实世界语音分离的解耦音视频增强框架。将音频和视觉信息解耦处理，更好地处理噪声和混响条件下的语音分离。

###  实验结果
在真实世界音视频数据集上验证了增强效果。

**是否开源：** 暂无。

###  评分：8/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [9] From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs

**arXiv ID** 2608.09158 | **方向** 语音大模型

**作者：** Yuanhe Zhang, Weiliu Wang, Jie Ren, Liang Lin, Zhenhong Zhou, Haoran Gao, Kun Wang, Chen Li

**机构：** Beijing University of Posts and Telecommunications; Institute of Information Engineering, Chinese Academy of Sciences

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09158 | **PDF** https://arxiv.org/pdf/2608.09158.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Large audio-language models (LALMs) have demonstrated strong capabilities in understanding diverse audio inputs. This diversity includes low-frequency signals that are inaudible to humans but can still enter the model and influence its generation. However, the practical impact of such low-frequency inputs on LALMs remains largely unexplored. In this paper, we propose Intermittent Low-Frequency Loc

###  技术方案
研究低频安全风险：分析语言音频大模型（LALM）对听不见的低频输入的响应，揭示潜在安全威胁。

###  实验结果
识别并分析了多种低频安全风险场景。

**是否开源：** 暂无。

###  评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [10] Structured Phonological Representations for Audio-Articulatory rtMRI Speech Classification

**arXiv ID** 2608.09767 | **方向** 语音大模型

**作者：** Abner Hernandez, Tomás Arias Vergara, Daiqi Liu, Andreas Maier, Paula Andrea Pérez-Toro

**机构：** Pattern Recognition Lab, Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU), Department of Electronic Engineering

**发布日期：** 2026-08-10 | **论文** https://arxiv.org/abs/2608.09767 | **PDF** https://arxiv.org/pdf/2608.09767.pdf | **代码** 暂无 | **Demo** 暂无

###  简介
Real-time MRI makes it possible to observe vocal-tract articulation during speech, but mapping these articulatory patterns to phonetic and phonological categories remains challenging. We investigate whether PhonoQ, an audio-based model trained to recognize structured phonological features, provides useful information for audio--articulatory modeling. Specifically, we extract representations from P

###  技术方案
提出用于音频-发音rtMRI语音分类的结构化音系表示方法。将发音运动模式映射到音系类别，提取高维MRI数据中的结构化特征。

###  实验结果
在语音分类任务上验证了所提表示方法的有效性。

**是否开源：** 暂无。

###  评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

今日语音论文速递