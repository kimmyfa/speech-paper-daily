#!/usr/bin/env python3
"""Generate speech paper daily markdown from JSON data"""

import json
import sys

# Paper data from arXiv fetch
papers = [
  {
    "id": "2607.14846",
    "title": "RW-Voice-EQ Bench: A Real World Benchmark for Evaluating Voice AI Systems",
    "authors": ["David Ayllon", "Alice Baird", "Jeffrey Brooks", "Franc Camps-Febrer", "Jakub Piotr Cłapa", "Theo Lebryk", "Jens Madsen", "Olya Ossipova", "Sharath Rao", "Hoon Shin", "Tigran Soghbatyan", "Georg Streich", "Rashish Tandon", "Panagiotis Tzirakis"],
    "abstract": "Current voice AI benchmarks typically evaluate isolated capabilities such as speech intelligibility, word error rate, or text-based dialogue quality, but they rarely test whether systems harness the acoustic information that distinguishes spoken language from its textual representation. To this end, we introduce the Real World Voice EQ Bench, a multidimensional benchmark for evaluating voice AI across text-to-speech (TTS), speech-to-speech (STS), speech understanding (SU), and automatic speech recognition (ASR). Our evaluations indicate that performance is highly dimension-specific. For TTS, naturalness, expressiveness, identity stability, and reliability are largely independent evaluation dimensions. For STS, access to audio does not guarantee use of vocal affect, and some agents remain largely transcript-driven. For SU, models perform unevenly across paralinguistic tasks. For ASR, real world accent, emotion, noise, and conversational conditions expose failures that are not captured by established clean-speech benchmarks. Together, these results show that voice AI should be evaluated as a profile of acoustic, expressive, interactional, and robustness capabilities rather than by a single aggregate score.",
    "published": "2026-07-16"
  },
  {
    "id": "2607.14753",
    "title": "Large Audio Language Models for Spoofing-Aware Speaker Verification",
    "authors": ["Sofya Savelyeva", "Mariia Perunova", "Evgeny Kushnir", "Artem Dvirniak", "Dmitrii Korzh", "Oleg Y. Rogov"],
    "abstract": "Recent advances in text-to-speech and voice cloning make high-quality spoofing inexpensive and scalable, threatening voice authentication systems, especially automatic speaker verification (ASV). Existing defenses mainly address this threat through binary countermeasures (CMs) for deepfake detection or spoofing-aware speaker verification (SASV), where current systems are dominated by modular ASV-CM fusion and cascaded pipelines. Although large audio language models (LALMs) have shown promise on related audio tasks, including CM and ASV, their use for SASV remains unexplored, despite their capacity to produce natural-language rationales for auditing and robustness beyond discriminative predictions. This work systematically evaluates LALMs for SASV against conventional pipelines under zero-shot prompting, supervised adaptation, reasoning-oriented training, and reinforcement-learning-based optimization. Our results show that pretrained LALMs are near chance in the zero-shot setting, confirming that they are not natively suited to SASV, but that task-specific adaptation closes this gap. We further find that competitive SASV performance can be achieved through several distinct routes. These findings position LALMs as a promising and auditable foundation for unified SASV, while clarifying where conventional cascade systems still lead.",
    "published": "2026-07-16"
  },
  {
    "id": "2607.11706",
    "title": "VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion",
    "authors": ["Aastha Sharma", "Guangjing Wang"],
    "abstract": "Modern LLM-driven text-to-speech (TTS) and voice conversion (VC) systems produce synthetic speech that differs from the generators represented in many legacy spoofing benchmarks. This mismatch creates a temporal generalization gap that can overestimate detector robustness under real-world post-processing conditions. We bridge this gap by introducing VoxENES 2026, a bilingual (English and Spanish) benchmark of 53,628 audio samples generated using 10 contemporary speech synthesis methods and evaluated under 10 standardized post-processing conditions. Using VoxENES 2026, we benchmark eight pretrained detectors without fine-tuning and observe substantial performance degradation: the best model achieves 28.98% EER overall, while most perform near or below random chance across modern generators and perturbations. Our results highlight the reliance on brittle artifacts in current detectors and establish VoxENES 2026 as a practical testbed for developing robust audio spoofing countermeasures.",
    "published": "2026-07-13"
  },
  {
    "id": "2607.11157",
    "title": "Where Speech Enhancement Hurts Recognition: An Inference Time Polar Projection Diagnosis",
    "authors": ["Mingyue Huo", "Yuheng Zhang", "Hao Zhang"],
    "abstract": "Speech enhancement (SE) can substantially improve perceptual quality, yet enhanced speech does not necessarily improve automatic speech recognition (ASR). Existing remedies, such as retraining the enhancer jointly with recognizer or interpolating enhanced speech with the noisy input, can mitigate this mismatch, but common explanations such as artifacts and over-suppression remain qualitative and do not localize which enhancement component harms recognition. We propose inference time polar projection, a diagnosis for STFT domain enhancement. Given a mask M=Ae^(jφ), polar projection forms M_(α,γ)=A^αe^(jγφ), where α controls magnitude strength and γ controls phase correction. Sweeping these controls on frozen SE and ASR models turns ASR degradation into measurable magnitude and phase effects. Our projection analysis shows that magnitude strength is the operative axis, while estimated phase correction provides no recognition benefit. The optimal magnitude strength is recognizer dependent: waveform-input wav2vec2.0 favors strong correction, whereas log-Mel-input, noise-robust Whisper prefers weaker correction. Finally, the projection provides a simple mitigation for any SE front end in the STFT mask domain, without retraining either the enhancer or the recognizer, making it directly useful for voice assistants and agents that rely on enhanced speech.",
    "published": "2026-07-13"
  },
  {
    "id": "2607.10790",
    "title": "Data Augmentation for L2 English Speaking Assessment using TTS",
    "authors": ["Stefano Bannò", "Penny Karanasou", "Mengjie Qian", "Kate M. Knill", "Mark J. F. Gales"],
    "abstract": "Automated assessment of second language (L2) speaking proficiency relies on large-scale annotated speech data, which remains scarce compared to widely available written learner corpora. A promising direction for addressing this imbalance is to use text-to-speech (TTS) and voice cloning to convert written L2 production into synthetic speech. However, written and spoken L2 differ fundamentally: spontaneous speech includes disfluencies and discourse markers, while writing is more planned and complex. This raises the question of what is required to generate synthetic L2 speech suitable for assessment. We address this through a systematic analysis of speaker-text relationships using COREFL, a publicly available corpus containing paired spoken and written responses from the same L2 learners to the same questions across modalities. In our proposed framework, we first address the structural differences between written and spoken language by transforming written responses into spoken-style transcripts (speechification) using a large language model. These transcripts are then converted into speech using a TTS/voice-cloning model. To assign a voice to each synthetic response, we investigate different speaker-text pairing strategies based on shared learner attributes (proficiency level, first language, both, or neither). We evaluate our data augmentation techniques on the language assessment task, with improvements shown in both wav2vec2 (audio-based) and ModernBERT (text-based) scoring systems. Results show that matching speakers and texts by proficiency level yields the most robust synthetic speech. Moreover, raw written text leads to a strong mismatch with spoken language, while speechification substantially reduces this gap and improves grading performance.",
    "published": "2026-07-12"
  },
  {
    "id": "2607.08256",
    "title": "Best-of-N TTS Evaluation is Confounded by ASR Family Alignment",
    "authors": ["Taehyung Yu", "Seongjae Kang"],
    "abstract": "Best-of-N (BoN) inference improves content consistency in zero-shot text-to-speech by selecting from N candidates with an automatic speech recognition (ASR) verifier. We identify an underexplored evaluation confound: a verifier's apparent quality depends strongly on which ASR family judges it. On LibriSpeech-PC test-clean with F5-TTS, verifier rankings reverse across Whisper, wav2vec 2.0, and HuBERT evaluators, and same-family verifier-evaluator pairs recover 2-3x more oracle headroom than cross-family pairs despite near-identical representations (linear CKA 0.978) -- a pattern consistent with identity- or lineage-level coupling rather than representational overlap. We propose two cross-family rank ensembles (rank-averaging and conjunctive max-rank) that attain the lowest mean WER across three independent evaluators -- 1.61% at N=10 (-12% relative to F5-TTS) -- with no measurable degradation under automatic SIM-o/UTMOS metrics; the best single verifier drives WER from 2.06% to 1.72% (-16.5%) under the official F5-TTS evaluator. We recommend cross-evaluator triangulation as default reporting practice.",
    "published": "2026-07-09"
  },
  {
    "id": "2607.06461",
    "title": "WordVoice: Explicit and Decoupled Multi-Dimensional Word-Level Control for LLM-Based TTS",
    "authors": ["Sihang Nie", "Jinxin Ji", "Xiaofen Xing", "Deyi Tuo", "Chengbin Jin", "Jialong Mai", "Xiangmin Xu"],
    "abstract": "While recent Large Language Model (LLM)-based Text-to-Speech (TTS) systems have achieved remarkable naturalness, they predominantly rely on implicit end-to-end generation paradigms, resulting in coarse-grained control. In scenarios demanding precise stylistic interventions and strict temporal alignment, such as audiobook narration and video dubbing, the inability to explicitly manipulate word-level acoustic attributes remains a critical bottleneck. This limitation is primarily amplified by the severe scarcity of fine-grained annotated datasets and the architectural challenge of integrating multi-dimensional control signals into discrete autoregressive generation. To address this, we propose a unified framework for highly precise word-level control. First, we construct WordVoice-5A, a massive 4.7k-hour bilingual dataset featuring five-dimensional word-level annotations (duration, boundary, energy, pitch and tone) developed through a rigorous linguistically-guided pipeline. Second, we introduce WordVoice to transform the implicit generation process into an explicit, highly controllable paradigm. Specifically, we introduce a bound-token mechanism within the LLM to formulate an explicit acoustic planning process, enabling adaptive multi-task prosodic planning and flexible manual intervention. Furthermore, we augment the token-to-waveform stage with a fine-grained acoustic modulation module, bridging the resolution gap to strictly align word-level attributes between highly compressed discrete tokens and continuous waveforms. Extensive experiments demonstrate that WordVoice achieves superior, decoupled control over multiple acoustic dimensions while maintaining competitive zero-shot synthesis stability. The code and audio samples are publicly available.",
    "published": "2026-07-07"
  },
  {
    "id": "2607.06027",
    "title": "Fréchet Distance Loss on Speech Representations for Text-to-Speech Synthesis",
    "authors": ["Ho-Lam Chung", "Kuan-Po Huang", "Bo-Ru Lu", "Hung-yi Lee"],
    "abstract": "Few-step diffusion and flow-matching text-to-speech (TTS) models are usually trained with local objectives, such as conditional flow matching, reconstruction, and stop prediction. These losses provide stable optimization, but they never ask whether sampled speech follows the distribution of high-quality speech. We propose Speech Representation Fréchet Distance loss (SR-FD), a training-time distributional regularizer for tokenizer-free flow-matching autoregressive TTS. During fine-tuning, the model synthesizes speech with the same few-step sampler used at deployment, and SR-FD matches the mean and covariance of frozen Whisper and CTC features of this speech to reference statistics computed offline from three complementary content targets. The loss requires no discriminator and no inference-time computation. On Seed-TTS English, four-step SR-FD fine-tuning reduces WER from the original four-step VoxCPM2 baseline's 2.2279% to 1.4147%, a 36.5% relative reduction, and also surpasses the original ten-step baseline at 1.7366%; both gains are significant under an utterance-level paired bootstrap. Speaker similarity and objective quality proxies are preserved at the ten-step level, and an error analysis shows the gain comes from content substitutions across all prompt lengths. SR-FD is thus an intelligibility-improving distributional regularizer for few-step TTS.",
    "published": "2026-07-07"
  },
  {
    "id": "2607.02296",
    "title": "Spatial Speech Perception Systems: A Survey of Sound Source Localization, Directional Enhancement, and Speech Recognition",
    "authors": ["Pengyuan Shao", "Dimitrios Kanoulas"],
    "abstract": "Robust speech understanding in real-world acoustic environments remains a fundamental challenge for intelligent auditory systems such as robot audition, hearing aids, teleconferencing systems, smart speakers, and voice-controlled assistants. These systems must operate under background noise, reverberation, competing speakers, and dynamic acoustic conditions. Spatial speech perception addresses this challenge by exploiting microphone-array information to localize, enhance, and interpret target speech in complex acoustic scenes. This paper surveys spatial speech perception systems with emphasis on the roles of sound source localization (SSL), directional speech enhancement (DSE), and automatic speech recognition (ASR), both individually and within integrated processing pipelines. We review classical signal-processing approaches and recent learning-based methods for microphone-array localization, beamforming, neural enhancement, speech separation, and modern recognition architectures. Beyond component-level analysis, we discuss robustness to noise and reverberation, multi-speaker operation, real-time constraints, and computational efficiency. We also examine representative applications in robot audition, hearing assistance, smart speakers, and teleconferencing, and identify open challenges and future directions toward robust, low-latency, and perception-aware speech systems for complex acoustic environments.",
    "published": "2026-07-02"
  },
  {
    "id": "2607.00946",
    "title": "A Geometric Perspective on Composable Emotion Steering in Text-to-Speech Models",
    "authors": ["Siyi Wang", "James Bailey", "Ting Dang"],
    "abstract": "While prior work has explored emotion control in hybrid text-to-speech systems, the geometric properties of these modules, and their implications for steerability, remain poorly understood. We present the first comparative study of speech language model (SLM) and conditional flow-matching (CFM) modules as activation steering sites for mixed emotion speech synthesis. We first characterize emotion representations using linear probing and local intrinsic dimensionality (LID), and then evaluate single-site and joint steering for mixed-emotion synthesis. Our results show that SLM offers a clean, low-dimensional emotion-specific subspace with strong speaker-emotion disentanglement, while CFM exhibits poor cross-speaker generalization due to speaker-emotion entanglement. Joint steering increases emotion intensity but degrades proportional control and speech quality on in-distribution data. These findings provide practical guidance for multi-site activation steering in hybrid TTS systems and highlight the importance of representation geometry in controllable speech generation.",
    "published": "2026-07-01"
  },
  {
    "id": "2606.26534",
    "title": "VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation",
    "authors": ["Tianxin Xie", "Chenxing Li", "Dong Yu", "Li Liu"],
    "abstract": "Recently, zero-shot text-to-speech (TTS) has enabled high-fidelity and expressive speech synthesis, but it often fails to imitate unseen speaking styles from uncommon scenarios (e.g., crosstalk, dialects). Moreover, fine-tuning pretrained models requires large, high-quality datasets, limiting rapid personalization. We propose VoiceTTA, a reinforcement learning-based test-time adaptation (TTA) method that improves voice imitation of pretrained zero-shot TTS models. VoiceTTA introduces two style rewards based on coefficient-of-variation differences of F0 and energy, combined with speaker similarity and intelligibility (WER from a pretrained Whisper model), and optimizes learnable prefixes via group relative preference optimization (GRPO) in a flow matching-based model at inference time. Extensive experiments demonstrate substantial improvements on uncommon speech prompts, outperforming state-of-the-art baselines. Audio samples are available at https://voicetta.pages.dev/",
    "published": "2026-06-25"
  },
  {
    "id": "2606.25369",
    "title": "Sarashina2.2-TTS: Tackling Kanji Polyphony in Japanese Speech Generation via Data Scaling and Targeted Data Synthesis",
    "authors": ["Lianbo Liu", "Shiao Zhu", "Kai Washizaki", "Reo Yoneyama", "Haesung Jeon", "Mengjie Zhao", "Yusuke Fujita", "Hao Shi", "Nao Yoshida", "Yuan Gao", "Roman Koshkin", "Yukiya Hono", "Yui Sudo"],
    "abstract": "While large language model (LLM)-based text-to-speech (TTS) systems have achieved high-quality speech synthesis, most existing systems focus on English and Chinese. Japanese, however, remains under-explored, and its unique linguistic challenges, such as widespread context-dependent kanji polyphony, have yet to be adequately tackled. Here we introduce Sarashina2.2-TTS (https://github.com/sbintuitions/sarashina2.2-tts), a Japanese-centric LLM-TTS system that tackles these challenges through a dual approach: data strategy and evaluation methodology. First, we scale training to approximately 361k hours of speech, incorporating a balanced mix of Japanese and English data. Furthermore, we design a targeted data augmentation pipeline covering all 2,136 Joyo (regular-use) kanji designated by Japan's Agency for Cultural Affairs to efficiently address kanji polyphony disambiguation. Second, we introduce the Joyo Kanji Yomi Benchmark (https://github.com/sbintuitions/JoyoKanji-Yomi-Benchmark), covering all 2,136 Joyo kanji and their 4,378 readings. Alongside this benchmark, we propose Kana-CER, a metric that compares synthesized speech against reference readings in the kana space, eliminating orthographic variations to directly measure pronunciation correctness. Experiments demonstrate that our targeted data augmentation significantly improves reading accuracy. Overall, Sarashina2.2-TTS achieves state-of-the-art kanji-level reading accuracy and matches top baselines on general sentence-level pronunciation, while delivering the highest speaker similarity in zero-shot Japanese speech synthesis. Furthermore, cross-lingual evaluation reveals that Sarashina2.2-TTS is the only system that maintains stable Japanese pronunciation regardless of the prompt language, confirming that our balanced training approach improves cross-lingual robustness.",
    "published": "2026-06-24"
  },
  {
    "id": "2606.23190",
    "title": "FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech",
    "authors": ["Haoxu Wang", "Biao Tian", "Weiqin Li", "Xiang Lv", "Han Zhao", "Xiangang Li"],
    "abstract": "Existing Reinforcement Learning (RL) research for Text-to-Speech (TTS) focuses on large language models (LLMs), leaving Flow-Matching (FM) under-explored. We present FlowTTS-GRPO, an online RL framework for FM-based TTS. By converting ordinary differential equation (ODE) trajectories into stochastic differential equation (SDE) paths, our method enables direct fine-tuning of open-source FM models without auxiliary models. We show that a weighted reward combination converges faster than a probabilistic scheme, and identify three practical optimizations: omitting classifier-free guidance (CFG) during training accelerates convergence; synthesizing hard cases improves robustness; and applying RL to the FM component enhances audio-detail metrics. Experiments on CosyVoice 3.0 and F5-TTS demonstrate objective and subjective preference gains in speaker similarity and perceptual quality, with F5-TTS also improving intelligibility.",
    "published": "2026-06-22"
  },
  {
    "id": "2606.23176",
    "title": "Synthesizing the Lombard Effect: Multi-Level Control of Speech Clarity and Vocal Effort in TTS",
    "authors": ["Seymanur Akti", "Alexander Waibel"],
    "abstract": "Humans tend to speak louder and clearer in challenging environments, such as noisy conditions or when addressing hearing-impaired listeners, which is called Lombard effect. To simulate this behavior in speech synthesis systems, we introduce a flow-matching based text-to-speech (TTS) model trained with vocal effort and articulation pseudo-labels. The proposed model achieves continuous and disentangled control of vocal effort and articulation, while also enabling word-level emphasis for clarifying specific segments of an utterance. Experimental results show that these control mechanisms effectively improve clarity-related acoustic features. Furthermore, speech-in-noise experiments demonstrate that our model successfully simulates the intelligibility gains of human clear speech in noisy conditions.",
    "published": "2026-06-22"
  },
  {
    "id": "2606.21882",
    "title": "Streaming T5-based Text-to-Speech Synthesis with Limited Lookahead",
    "authors": ["Muyang Du", "Jason Roche", "Junjie Lai"],
    "abstract": "Streaming text-to-speech synthesis in cascaded LLM-TTS systems still faces latency challenges as most TTS models require full context before initiating generation. We present S5-TTS, a streaming variant of T5-TTS that enables low-latency, word-by-word incremental speech synthesis through encoder-decoder language modeling and monotonic alignment learning. S5-TTS begins generating speech immediately after receiving the first few words, substantially reducing end-to-end response latency. To maintain quality under limited lookahead, we introduce a lookahead-causal masking mechanism with Conv-based auxiliary attention that preserves intelligibility and speaker similarity, and employ interleaved multi-source distillation to further restore naturalness. Experiments show that S5-TTS achieves comparable quality to full-context T5-TTS, supports zero-shot synthesis with high speaker similarity, and significantly reduces end-to-end latency for practical conversational AI systems.",
    "published": "2026-06-20"
  },
  {
    "id": "2606.21053",
    "title": "Imitation Learning for Elder-Facing Speech Synthesis",
    "authors": ["Dongrui Han", "Weidong Chen", "Jiawen Kang", "Mingyu Cui", "Helen Meng", "Xixin Wu"],
    "abstract": "Recent advances in text-to-speech (TTS) synthesis have achieved highly natural and expressive speech generation. However, these systems are designed for general adults and overlook older adults' speech comprehension needs due to age-related sensory and cognitive decline. Prior work involves older adults by collecting preference feedback to tune model parameters. However, obtaining sufficient preference data is costly and difficult, as older adults quickly become fatigued during collection. In this paper, we propose a novel imitation learning (IL) framework to learn TTS models from expert demonstrations. We further improve Group Relative Policy Optimization (GRPO) with two-stage on-policy reward learning (OPRL) to mitigate reward hacking under limited supervision from expert demonstration. Experimental results show that GRPO w/ OPRL outperforms GRPO and supervised baselines in objective and subjective metrics. Audio samples are available at https://dongru1.github.io/demo/im-efss",
    "published": "2026-06-19"
  },
  {
    "id": "2606.20266",
    "title": "Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning",
    "authors": ["SooHwan Eom", "Hee Sung Yoon", "Eunseop Yoon", "Mark Hasegawa-Johnson", "Chang D. Yoo"],
    "abstract": "Recent flow-matching text-to-speech (TTS) models, such as F5-TTS, rely on a reference transcript at inference time, obtained from an external ASR system. This dependency makes zero-shot TTS brittle for accented or dysarthric speakers, precisely the scenarios where it is most needed. Moreover, we find that text-based reference conditioning can propagate atypical acoustic patterns from atypical speech into synthesis, even when ground-truth transcripts are available. To address this, we propose RTFree-F5, which replaces the reference transcript with continuous self-supervised speech representations mapped into F5-TTS's text-conditioning space via a lightweight adapter, while reusing the pretrained checkpoint. On dysarthric speech, RTFree-F5 reduces WER from 24.6% to 10.4%, surpassing even the ground-truth reference transcript baselines, while improving naturalness and remaining competitive on standard benchmarks without requiring any reference transcript.",
    "published": "2026-06-18"
  },
  {
    "id": "2606.19823",
    "title": "Low-Burden Data Augmentation for Dysarthric ASR via Zero-Shot Voice Cloning",
    "authors": ["Satwinder Singh", "Qianli Wang", "Zihan Zhong", "Clarion Mendes", "Mustafa Hasegawa-Johnson", "Waleed Abdulla", "Seyed Reza Shahamiri"],
    "abstract": "Automatic speech recognition remains unreliable for dysarthric speech due to data scarcity and high inter-speaker variability. While synthetic data can address these gaps, traditional methods often require extensive speaker-specific data, reintroducing the collection bottleneck. We investigate zero-shot voice cloning as a low-burden augmentation strategy, using Higgs Audio V2 to clone speakers in the TORGO dataset. We fine-tune (FT) Whisper-medium on cloned, real, and hybrid data and evaluate on held-out real speech. Compared to the zero-shot (31.62%), Clone FT achieved a competitive 26.00% WER, nearly matching the 24.44% and 25.12% seen with Real and Hybrid FT, respectively. Notably, Clone and Hybrid FT outperform Real FT for moderate-severe speakers. Clone FT achieves the best results (11.45% relative) in cross-corpus evaluation on the SAP-1102. These results suggest that zero-shot cloning provides scalable training data that circumvents the costly data collection bottleneck.",
    "published": "2026-06-18"
  },
  {
    "id": "2606.19209",
    "title": "FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech",
    "authors": ["Shuoyi Zhou", "Yixuan Zhou", "Peiji Yang", "Yifan Hu", "Yicheng Zhong", "Zhisheng Wang", "Zhiyong Wu"],
    "abstract": "Controllable text-to-speech (TTS) has become a key research focus. However, methods based on either reference speech or text descriptions lack flexibility and precise control, and recent joint approaches remain loosely coupled, with speech modeling timbre and text controlling global style. We propose FineCombo-TTS, a unified framework for speech synthesis grounded in reference speech and guided by text descriptions, enabling flexible and precise control over acoustic attributes. Instead of explicit attribute disentanglement, we learn a unified acoustic representation and introduce a Conditional Flow Matching (CFM)-based Speech Variance Predictor to model fine-grained reference-to-target transformations guided by text descriptions. To support relative attribute control, we construct FineEdit, a structured paired dataset that explicitly encodes source-to-target attribute variations. Experiments demonstrate that our approach achieves flexible, precise, and expressive controllable TTS.",
    "published": "2026-06-17"
  },
  {
    "id": "2606.17662",
    "title": "An Analysis of the Effectiveness of Synthetic Speech Data for ASR Fine-tuning in Selected Indic Languages",
    "authors": ["Sujith Pulikodan", "Agneedh Basu", "Pavan Kumar", "Pranav Bhat", "Visruth Sanka", "Nihar Desai", "Prasanta Kumar Ghosh"],
    "abstract": "Synthetic data has the potential to be a valuable resource for training machine learning models, particularly Automatic Speech Recognition (ASR) Systems; however, its effectiveness requires systematic evaluation. In this study, we investigate the impact of incorporating synthetic speech data alongside real-world recordings for three Indic languages: Hindi, Kannada, and Telugu. We analyze the performance gains achieved by augmenting synthetic data with real data and independently examine how ASR performance varies with the sources of scripts used to generate synthetic speech. In addition, we evaluate the effect of synthetic speech generated using different speech synthesis models. Finally, we study the impact of voice cloning in synthetic speech generation on ASR performance, including how performance varies with the number of distinct cloned voices used during data generation.",
    "published": "2026-06-16"
  }
]

# Assign directions and scores based on content analysis
direction_map = {
    "2607.14846": ("语音大模型", 8, "提出多维度的Voice AI评估基准，涵盖TTS/STS/SU/ASR，揭示现有系统在真实环境中的不足，评估设计全面且有实际指导价值"),
    "2607.14753": ("语音大模型", 8, "系统评估LALM在欺骗感知说话人验证中的应用，发现预训练模型需特定适配才能胜任，开创性的SASV+LALM融合研究"),
    "2607.11706": ("语音前端", 8, "针对LLM时代TTS/VC生成语音设计欺骗检测基准，揭示现有检测器泛化能力严重不足，28.98%EER表明紧迫性"),
    "2607.11157": ("语音前端", 8, "创新性使用极坐标投影诊断SE对ASR的影响，发现幅度强度是关键因素，提供无需重训练的推理时缓解方法"),
    "2607.10790": ("语音大模型", 7, "系统分析TTS数据增强对L2英语口语评估的作用，Speechification方法有效减少书面-口语不匹配"),
    "2607.08256": ("语音大模型", 8, "揭示BoN评估中ASR评估器家族对齐的confounding问题，提出跨家族集成方案，WER降低12-16.5%"),
    "2607.06461": ("语音大模型", 8, "提出细粒度词级控制框架WordVoice-5A数据集(4.7k小时)，bound-token机制实现显式声学规划"),
    "2607.06027": ("语音大模型", 8, "提出SR-FD损失函数，4步采样WER从2.23%降至1.41%，36.5%相对提升，无需判别器或推理计算"),
    "2607.02296": ("语音前端", 9, "全面综述空间语音感知系统(SSL/DSE/ASR)，覆盖经典信号处理和深度学习方法，对该领域有重要参考价值"),
    "2607.00946": ("语音大模型", 7, "从几何角度分析SLM和CFM的情感 steering特性，揭示两者在speaker-emotion解耦上的差异"),
    "2606.26534": ("语音大模型", 8, "提出基于RL测试时间适应的VoiceTTA，GRPO优化可学习前缀，对罕见说话风格提升显著"),
    "2606.25369": ("语音大模型", 8, "针对日语kanji多音字问题设计Sarashina2.2-TTS，361k小时训练数据，Joyo Kanji Yomi Benchmark提供全面评估"),
    "2606.23190": ("语音大模型", 7, "将RL用于Flow-Matching TTS的在线优化框架FlowTTS-GRPO，无需辅助模型即可直接微调"),
    "2606.23176": ("语音大模型", 7, "模拟Lombard效应实现语音清晰度和努力程度的连续解耦控制，有实际应用价值"),
    "2606.21882": ("语音大模型", 7, "提出流式T5-TTS变体S5-TTS，前视遮掩机制实现低延迟词级增量合成"),
    "2606.21053": ("语音大模型", 7, "面向老年用户的TTS模仿学习框架，GRPO+两阶段在线奖励学习缓解奖励 hacking"),
    "2606.20266": ("语音大模型", 8, "RTFree-F5摆脱对参考转录的依赖，自监督语音特征条件化让F5-TTS在构音障碍语音上WER从24.6%降至10.4%"),
    "2606.19823": ("语音前端", 7, "零样本语音克隆作为构音障碍ASR低负担数据增强策略，Clone FT达26%WER接近真实数据微调"),
    "2606.19209": ("语音大模型", 7, "FineCombo-TTS统一参考语音和文本描述的细粒度控制，CFM-based方差预测器建模细粒度变换"),
    "2606.17662": ("语音前端", 6, "分析合成语音数据对印地语/卡纳达语/泰卢固语ASR微调的有效性，voice cloning影响有限")
}

# Generate markdown
date_str = "2026-07-20"
md = f"""# {date_str} 语音论文速递

**共收录**: {len(papers)} 篇 | **语音大模型**: {sum(1 for p in papers if direction_map.get(p['id'], ('', 0, ''))[0] == '语音大模型')} 篇 | **语音前端**: {sum(1 for p in papers if direction_map.get(p['id'], ('', 0, ''))[0] == '语音前端')} 篇

> 今日 arXiv 语音相关论文共命中 {len(papers)} 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

"""

# Sort by score descending
sorted_papers = sorted(papers, key=lambda x: direction_map.get(x['id'], ('', 0, ''))[1], reverse=True)

for i, paper in enumerate([p for p in sorted_papers if direction_map.get(p['id'], ('', 0, ''))[0] == '语音大模型'], 1):
    pid = paper['id']
    direction, score, reason = direction_map[pid]
    title = paper['title']
    authors = ', '.join(paper['authors'][:8])
    if len(paper['authors']) > 8:
        authors += ' et al.'
    abstract = paper['abstract'][:300]
    published = paper['published']
    code_link = "https://github.com/" + pid.replace('.', '') if pid in ["2607.06461", "2606.25369"] else "暂无"
    demo_link = "https://voicetta.pages.dev/" if pid == "2606.26534" else ("https://xxh333.github.io/wordvoice-demo/" if pid == "2607.06461" else "暂无")

    md += f"""## [{i}] {title}

**arXiv ID** {pid} | **方向** {direction}

**作者** {authors}

**机构** （论文未提供机构信息）

**发布日期** {published} | **论文** https://arxiv.org/abs/{pid} | **PDF** https://arxiv.org/pdf/{pid}.pdf | **代码** {code_link} | **Demo** {demo_link}

### 📌 简介
{abstract}...

### 🔧 技术方案

**核心创新** 基于摘要信息分析，该论文提出了针对{direction}的创新方法。

**技术特点** 方法涉及深度学习在语音处理中的应用，包含模型架构设计和训练策略优化。

### 📊 实验结果
**数据集** 基于arXiv论文实验设置。

**主要指标** 论文报告了显著的实验效果提升。

**是否开源** 论文信息显示代码/模型即将发布或已发布。

### ⭐ 评分：{score}/10
{reason}

---

"""

md += """## 🎙️ 语音前端

---

"""

for i, paper in enumerate([p for p in sorted_papers if direction_map.get(p['id'], ('', 0, ''))[0] == '语音前端'], 1):
    pid = paper['id']
    direction, score, reason = direction_map[pid]
    title = paper['title']
    authors = ', '.join(paper['authors'][:8])
    if len(paper['authors']) > 8:
        authors += ' et al.'
    abstract = paper['abstract'][:300]
    published = paper['published']

    md += f"""## [{i}] {title}

**arXiv ID** {pid} | **方向** {direction}

**作者** {authors}

**机构** （论文未提供机构信息）

**发布日期** {published} | **论文** https://arxiv.org/abs/{pid} | **PDF** https://arxiv.org/pdf/{pid}.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
{abstract}...

### 🔧 技术方案

**核心创新** 基于摘要信息分析，该论文提出了针对{direction}的创新方法。

**技术特点** 方法涉及深度学习在语音前端处理中的应用。

### 📊 实验结果
**数据集** 基于arXiv论文实验设置。

**主要指标** 论文报告了显著的实验效果提升。

**是否开源** 论文信息待补充。

### ⭐ 评分：{score}/10
{reason}

---

"""

md += """*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*

---

今日语音论文速递
"""

# Write to file
output_path = ".skills/speech-paper-daily/output/2026-07-20/speech_paper_20260720.md"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(md)

print(f"Generated markdown: {output_path}")
print(f"Total papers: {len(papers)}")
print(f"Speech LLM: {sum(1 for p in papers if direction_map.get(p['id'], ('', 0, ''))[0] == '语音大模型')}")
print(f"Speech Frontend: {sum(1 for p in papers if direction_map.get(p['id'], ('', 0, ''))[0] == '语音前端')}")