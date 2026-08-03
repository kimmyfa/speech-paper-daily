# 2026-08-01 语音论文速递

**共收录**: 6 篇 | **语音大模型**: 6 篇 | **语音前端**: 0 篇

> 今日 arXiv 语音相关论文共命中 66 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] Teffic-Audio: Tell Fact from Fiction

**arXiv ID** 2607.28351v1 | **方向** 语音大模型

**作者：** Wan Lin, Li Wang, Jindong Wang, Kunyu Feng, Zhizheng Wu

**机构：** arXiv未提供机构信息

**发布日期：** 2026-07-30 | **论文** https://arxiv.org/abs/2607.28351v1 | **PDF** https://arxiv.org/pdf/2607.28351v1.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
Speech deepfake detection has expanded in scope with increasingly heterogeneous spoofing mechanisms, including speech synthesis, voice conversion, vocoder reconstruction, and neural-codec resynthesis. The resulting spoofing artifacts can be further shaped by variability in source speech, recording environments, and transmission channels. This variability makes robust generalization across heterogeneous conditions a central requirement for practical detection systems. This report presents Teffic-Audio, a general speech deepfake detection system designed for comprehensive evaluation environment. Teffic-Audio adopts a straightforward detector architecture consisting of a Conformer-based speech encoder, multi-head attentive statistics pooling, and a binary classifier. Rather than relying on additional architectural complexity, the system improves generalization through its training recipe, which integrates multi-source data, attack- and source-balanced sampling, and diverse audio augmentation. Trained only with open-source data, Teffic-Audio achieves a pooled EER of 1.454% on the 14 test sets of Speech-DF-Arena, outperforming all currently public systems on the leaderboard. It also obtains the lowest EER on five individual test sets and shows a favorable performance-complexity trade-off compared with larger leading systems. Overall, Teffic-Audio provides a strong and practical reference system for general speech deepfake detection.

### 技术方案
基于摘要信息：本文提出针对语音/音频任务的方法，具体技术细节需参考原文。

### 实验结果
基于摘要信息：本文在相关数据集上进行了实验验证，具体指标需参考原文。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [2] RIPPLE: Generating Multi-Channel Phase, Not Recovering It

**arXiv ID** 2607.27775v1 | **方向** 语音大模型

**作者：** Jaehyuk Lee, Yeajin Lee, Dayeon Shin, Donghun Lee

**机构：** arXiv未提供机构信息

**发布日期：** 2026-07-30 | **论文** https://arxiv.org/abs/2607.27775v1 | **PDF** https://arxiv.org/pdf/2607.27775v1.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
Generative models synthesize magnitude spectra with high fidelity, while phase is delegated to a recovery module---Griffin--Lim, a vocoder, or a latent decoder---applied independently to each channel. For multi-channel waveforms this delegation is costly: the physical content of spatial audio and three-component seismograms lives in the phase relationships between channels, precisely what channel-independent recovery cannot produce. The cost is also invisible, since the magnitude-based metrics common to both fields barely move when inter-channel phase coherence collapses---so a pipeline can discard the physical information in its output while still scoring well. We argue that phase should be generated, not recovered, and present RIPPLE (Rectified Inter-channel Phase with Prior-based LEarning), which reinterprets Griffin--Lim as a phase **prior** rather than a final estimator: initialized from the source phase, this prior carries the inter-channel structure to be preserved, and a rectified flow refines it toward the target under an explicit inter-channel phase loss. Tested on first-order ambisonics environment transfer and seismic cross-station translation---two physically unrelated domains---RIPPLE outperforms recovery-based pipelines on the coherence metrics that downstream analyses consume. The seismic case is decisive: across architecturally distinct generators, per-channel recovery leaves S-wave polarization error near the $57.3^\circ$ random expectation, whereas learned phase reduces it to $33.8^\circ$.

### 技术方案
基于摘要信息：本文提出针对语音/音频任务的方法，具体技术细节需参考原文。

### 实验结果
基于摘要信息：本文在相关数据集上进行了实验验证，具体指标需参考原文。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [3] Cocktail-Talker: Multi-Speaker Dialog Modeling in Noisy Social Environments with Turn Action GRPO

**arXiv ID** 2607.27756v1 | **方向** 语音大模型

**作者：** Xilin Jiang, Riki Shimizu, Sukru Samet Dindar, Junkai Wu, Zhongweiyang Xu, Nima Mesgarani

**机构：** arXiv未提供机构信息

**发布日期：** 2026-07-30 | **论文** https://arxiv.org/abs/2607.27756v1 | **PDF** https://arxiv.org/pdf/2607.27756v1.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
Spoken dialog systems are typically designed for clean, dyadic interactions in which a single user and an assistant take turns speaking. Real-world social conversations, however, are often more ambiguous: multiple speakers may participate in the same conversation amid irrelevant speech and background noise. Each utterance may be directed to the assistant, addressed to another speaker, or completely irrelevant. In such settings, the assistant must decide not only what to say, but also whether to speak at all. In this paper, we introduce Cocktail-Talker, a speech LLM framework for multi-speaker spoken dialog modeling in noisy social environments. We model the assistant's behavior with three action tokens: &lt;|respond|&gt;, &lt;|listen|&gt;, and &lt;|ignore|&gt;, placed before a response or silence. Cocktail-Talker is trained via supervised finetuning and reinforcement learning to generate the appropriate action token and, only in &lt;|respond|&gt; mode, a speech response. To prepare the training data, we develop Cocktail-DialogGen, an LLM-based data pipeline that simulates realistic multi-speaker dialogs with speaker roles across diverse social settings. Together, these components take a step toward spoken dialog systems that interact more naturally and selectively in complex social environments.

### 技术方案
基于摘要信息：本文提出针对语音/音频任务的方法，具体技术细节需参考原文。

### 实验结果
基于摘要信息：本文在相关数据集上进行了实验验证，具体指标需参考原文。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [4] WeSep: A Modular and Cue-Composable Framework for Target Speaker Extraction

**arXiv ID** 2607.27436v1 | **方向** 语音大模型

**作者：** Ke Zhang, Xiaoyang Yu, Haoyu Li, Shuai Wang, Shuhan Zhang, Haizhou Li

**机构：** arXiv未提供机构信息

**发布日期：** 2026-07-29 | **论文** https://arxiv.org/abs/2607.27436v1 | **PDF** https://arxiv.org/pdf/2607.27436v1.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
The study of Target Speaker Extraction (TSE) aims to isolate a desired speaker from overlapping speech mixture given auxiliary cues. Existing systems are typically designed for specific cue types, limiting flexibility when cue availability varies across scenarios. We present WeSep, a unified framework that reformulates TSE as a heterogeneous cue-conditioned learning problem. In WeSep, cue modules and separator backbones are decoupled through standardized interfaces, enabling configurable cue injection and flexible integration of diverse modalities. The design enables systematic study of cue structure, intra- and cross-modal interaction, and dynamic cue availability within a shared optimization framework, facilitating adaptation to real-world conditions. Experiments across enrollment, spatial, visual, and textual cues reveal modality-dependent characteristics and demonstrate stable optimization under heterogeneous cue availability. The toolkit will be publicly available.

### 技术方案
基于摘要信息：本文提出针对语音/音频任务的方法，具体技术细节需参考原文。

### 实验结果
基于摘要信息：本文在相关数据集上进行了实验验证，具体指标需参考原文。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [5] MMAC: A Massive Multi-dimensional Benchmark for Audio Captioning

**arXiv ID** 2607.27109v2 | **方向** 语音大模型

**作者：** Weijie Wu, Junbo Li, Lin Li, Jun Fang, Qingyang Hong

**机构：** arXiv未提供机构信息

**发布日期：** 2026-07-29 | **论文** https://arxiv.org/abs/2607.27109v2 | **PDF** https://arxiv.org/pdf/2607.27109v2.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
With the development of audio large language models (AudioLLMs), audio captioning needs to move from brief descriptions toward open-ended and fine-grained free-form descriptions. Existing evaluations often focus on generation quality or task performance, making it difficult to diagnose information coverage and description reliability. We propose MMAC, a \textbf{M}assive \textbf{M}ulti-dimensional benchmark for \textbf{A}udio \textbf{C}aptioning. MMAC contains 5,638 audio clips from more than 20 data sources, covering 6 capability categories and 15 evaluation dimensions. Given a model-generated caption, MMAC checks whether it mentions relevant information in the target dimension and whether the mentioned content is consistent with the reference label. We evaluate representative open-source and proprietary AudioLLMs. Results show clear differences across evaluation dimensions, information coverage, and description reliability. We will release the MMAC benchmark and evaluation code.

### 技术方案
基于摘要信息：本文提出针对语音/音频任务的方法，具体技术细节需参考原文。

### 实验结果
基于摘要信息：本文在相关数据集上进行了实验验证，具体指标需参考原文。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

## [6] Qwen-Audio-3.0-Gen-Preview Technical Report

**arXiv ID** 2607.27011v2 | **方向** 语音大模型

**作者：** Junyu Dai, Xiaoyue Duan, Xinyue Fan, Yihan Feng, Jingbei Li, Xiangang Li, Yunjia Li, Lejun Min

**机构：** arXiv未提供机构信息

**发布日期：** 2026-07-29 | **论文** https://arxiv.org/abs/2607.27011v2 | **PDF** https://arxiv.org/pdf/2607.27011v2.pdf | **代码** 暂无 | **Demo** 暂无

### 简介
Existing single-domain and multi-task audio systems remain limited in directly organizing heterogeneous audio components, ambience, and multiple roles into long-form temporal scenes. We present Qwen-Audio-3.0-Gen-Preview, a unified non-autoregressive framework that uses a Diffusion Transformer (DiT) and a shared variational autoencoder (VAE) to generate the complete mixed waveform. Prompt enhancement converts free-form requests into structured temporal records that are rendered as textual conditions, while a two-stage data curriculum and semantic conditional views train the proposed model to use these conditions across standalone and mixed-scene audio. A shared continuous VAE compresses 48kHz stereo waveforms into 25Hz latent sequences and incorporates semantic supervision, providing one representation for heterogeneous audio. On the public reference-conditioned benchmark, speaker similarity is the proposed model's clearest strength across all three subsets. Across the multi-speaker and rich-timeline benchmarks, its clearest comparative strengths are cross-turn consistency in both languages and temporal localization, respectively. On AudioCaps, its advantages are concentrated in evaluations using large audio-language models and AudioBox. These results demonstrate the potential of unified generation for temporally structured audio without task-specific branches.

### 技术方案
基于摘要信息：本文提出针对语音/音频任务的方法，具体技术细节需参考原文。

### 实验结果
基于摘要信息：本文在相关数据集上进行了实验验证，具体指标需参考原文。

### 评分：7/10
基于标题和摘要的初步评估，有一定学术价值。

---

今日语音论文速递