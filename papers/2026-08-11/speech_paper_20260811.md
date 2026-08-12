# 2026-08-11 语音论文速递

**共收录**: 8 篇 | **语音大模型**: 8 篇 | **语音前端**: 0 篇

> 今日 arXiv 语音相关论文共命中 8 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

---

## [1] X2-Turn: Frame-Synchronous Dual-Head Modeling for Joint Streaming ASR and Turn State Prediction

**arXiv ID** 2608.10878 | **方向** 语音大模型

**作者：** Kaiqi Fu, Rime Wen, Altman Lin, Shawn Qin, Roy Gan, Hao Wang, Qian Wang

**机构：** Shanghai Jiao Tong University (x2robot.com)

**发布日期：** 2026-08-11 | **论文** https://arxiv.org/abs/2608.10878 | **PDF** https://arxiv.org/pdf/2608.10878.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
Accurate and responsive turn-taking is essential for spoken dialogue systems. We present X2-Turn, a frame-synchronous turn state prediction method via delayed-stream modeling, building on the pretrained Voxtral Realtime model.

### 技术方案
提出X2-Turn方法，在预训练Voxtral Realtime模型上引入帧同步turn状态头，与ASR头并行运行，在帧级别联合预测ASR token和细粒度turn状态。

### 实验结果
在双语中英Easy-Turn测试集上验证了方法的有效性，实现了准确的turn-taking检测同时保持低延迟。

**是否开源：** 暂无。

### 评分：8/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [2] The GENEA Challenge 2026: A Large-Scale Disentangled Evaluation of Speech-Driven Gesture Generation

**arXiv ID** 2608.10839 | **方向** 语音大模型

**作者：** Rajmund Nagy, Silvia Arellano García, Hendric Voss, Mihail Tsakov, Taras Kucherenko, Youngwoo Yoon, Gustav Eje Henter

**机构：** KTH Royal Institute of Technology, Bielefeld University, Independent researcher, National Library of Sweden, ETRI, Motorica AB

**发布日期：** 2026-08-11 | **论文** https://arxiv.org/abs/2608.10839 | **PDF** https://arxiv.org/pdf/2608.10839.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
The GENEA Challenge 2026 presents large-scale human evaluation on five speech-driven gesture-generation systems trained on the Seamless Interaction dataset.

### 技术方案
提出解构评估方法，分别评估手势质量和与语音的对齐性，消除了两者之间的混淆效应。引入了新的语义手势生成任务和评估方法。

### 实验结果
运行了四个大规模用户研究，收集了869名测试者的23000多票。

**是否开源：** 暂无。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [3] Whisper-Aware LLM: Self-Supervised Uncertainty Learning for Robust Whispered Speech Recognition

**arXiv ID** 2608.10836 | **方向** 语音大模型

**作者：** Gaopeng Xu, Zhenyu Wang, Zheng Xue, Yinfeng Xia, Haitao Yao

**机构：** Qwen Business Unit of Alibaba, China

**发布日期：** 2026-08-11 | **论文** https://arxiv.org/abs/2608.10836 | **PDF** https://arxiv.org/pdf/2608.10836.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
The signal ambiguity of whispered speech drives ASR systems toward two opposing failure modes. This paper introduces the Whisper-Aware LLM that teaches an Audio-LLM to perceive and react to this uncertainty.

### 技术方案
提出Whisper-Aware LLM框架，通过自监督任务学习量化声学信号的物理缺陷，引入置信度融合解码机制(Confidence-Fused Decoding)为LLM解码器提供高级指令和帧级注意力调制。

### 实验结果
在AISHELL6-Whisper上实现了17%的相对CER降低，幻觉率从25%以上降至4.5%。

**是否开源：** 暂无。

### 评分：9/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [4] DuplexWorld: Can voice agents help you get through government services?

**arXiv ID** 2608.10716 | **方向** 语音大模型

**作者：** Aryan Vijay Bhosale, Harshit Rajgarhia, Akhil Pothanapalli, Asif Shaik, Abhishek Mukherji, Dinesh Manocha

**机构：** Centific Global Solutions Inc.; University of Maryland

**发布日期：** 2026-08-11 | **论文** https://arxiv.org/abs/2608.10716 | **PDF** https://arxiv.org/pdf/2608.10716.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
Speech-to-speech voice agents are increasingly being incorporated into enterprise. DuplexWorld introduces six worlds where voice agents are especially useful: banking, insurance, travel, healthcare and logistics.

### 技术方案
提出DuplexWorld基准测试，包含六个领域（银行、保险、旅行、医疗保健和物流）的156个场景，覆盖350+小时对话。

### 实验结果
对语音代理进行了全面评估，测试对话和分析能力。

**是否开源：** 暂无。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [5] DINO-A: Adapting Self-Distillation Vision Transformers to General Audio Representation Learning

**arXiv ID** 2608.10659 | **方向** 语音大模型

**作者：** Tomasz Radzikowski, Mateusz Modrzejewski, Przemyslaw Rokita

**机构：** Warsaw University of Technology, Poland

**发布日期：** 2026-08-11 | **论文** https://arxiv.org/abs/2608.10659 | **PDF** https://arxiv.org/pdf/2608.10659.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
We present DINO-A, an adaptation of self-distillation from vision to general audio representation learning.

### 技术方案
将DINO从视觉领域适配到音频领域，保留多crop、EMA教师和高维投影，仅将输入模态和增强替换为log-mel频谱图和BYOL-A v2增强块。

### 实验结果
在FSD50K上预训练，在ESC-50、Speech Commands v2、UrbanSound8K和GTZAN上用线性探测评估。视觉Transformer在环境和音乐上领先，卷积网络在语音上领先。

**是否开源：** 暂无。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [6] Never Stop Speaking: a Denial-of-Service Attack on End-to-End Speech Language Models

**arXiv ID** 2608.10405 | **方向** 语音大模型

**作者：** Shuozhe Cheng, Kunlan Xiang, Mingxuan Li, Ji Zhang, Dongxiao Liu, Wenbo Jiang

**机构：** Anonymous

**发布日期：** 2026-08-11 | **论文** https://arxiv.org/abs/2608.10405 | **PDF** https://arxiv.org/pdf/2608.10405.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
We propose the first perturbation-based DoS attack targeting E2E speech LLMs that optimizes imperceptible acoustic perturbations to influence the model's autoregressive generation process.

### 技术方案
提出基于扰动的DoS攻击，公式化组合优化目标：抑制EOS生成、鼓励延长解码、保持语义一致性。使用VAD仅在有声区域注入扰动。

### 实验结果
在三个开源E2E语音LLM上进行了广泛实验。

**是否开源：** 暂无。

### 评分：8/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [7] VoxSumm: A Multilingual Corpus of Long-Form Spoken News for Joint Summarization and Translation

**arXiv ID** 2608.10359 | **方向** 语音大模型

**作者：** Yejin Jeon, Marie Maltais, Virginia Ceccatelli, Min Ma, David Ifeoluwa Adelani

**机构：** Mila - Quebec AI Institute; McGill University; Google DeepMind; Canada CIFAR AI Chair

**发布日期：** 2026-08-11 | **论文** https://arxiv.org/abs/2608.10359 | **PDF** https://arxiv.org/pdf/2608.10359.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
We address the methodological gap by formalizing joint speech summarization and translation (JSumT): the generation of a succinct, faithful target-language summary directly from a long spoken document.

### 技术方案
提出JSumT任务，从长口语文档直接生成目标语言的简洁忠实摘要。构建了VOXSUMM多语言基准，包含10045个BBC文章-摘要对，涵盖24种语言，约703小时语音数据。

### 实验结果
对代表性语音语言模型进行了评估，Gemini3.1-Pro表现最佳，英语摘要普遍优于非英语目标语言生成。

**是否开源：** 暂无。

### 评分：8/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [8] In Defense of Using Worst-case Privacy Disclosure as Privacy Evaluation Metric of Voice Anonymization

**arXiv ID** 2608.10318 | **方向** 语音大模型

**作者：** Xin Wang, Xiaoxiao Miao

**机构：** National Institute of Informatics, Japan; Duke Kunshan University, China

**发布日期：** 2026-08-11 | **论文** https://arxiv.org/abs/2608.10318 | **PDF** https://arxiv.org/pdf/2608.10318.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
This paper positions itself as a defense of the privacy-ZEBRA framework for voice anonymization evaluation.

### 技术方案
为privacy-ZEBRA框架进行辩护，解释了EER最佳系统如何在LLR空间中无法正确评估信息泄漏，展示了基于排名的指标如何等同于完美保密原则。

### 实验结果
在模拟数据和VoicePrivacy Challenge数据上展示了研究结果。

**是否开源：** 暂无。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

今日语音论文速递