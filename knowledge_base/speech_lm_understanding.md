# SPEECH LM UNDERSTANDING（按评分降序）

共 80 篇

## [VoxPrivacy: A Benchmark for Evaluating Interactional Privacy of Speech Language Models](https://arxiv.org/abs/2601.19956)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-01-27
- **一句话贡献**：SLM正从个人设备走向共享智能家居等多人环境，却缺乏区分说话人并管理信息流的"交互式隐私"能力。本文提出首个交互式隐私评测基准VoxPrivacy：7107条32.86小时中英双语数据、三层递进任务（遵守保密指令→以声音为钥匙的条件放行→主动推断敏感信息）。评测9个SLM发现开源模型在条件隐私任务上接近随机（约50%），微调Kimi-Audio后Tier2英文F1升至82.65（Gemini-2.
- **关键技术点**：现有SLM基准只测"说了什么"不测"谁在说"；隐私基准只针对密码等全局敏感信息，忽略"本不敏感但在特定语境下变敏感"的信息。作者将交互式隐私定义为共享环境中阻止A用户信息泄露给B用户，并论证逐轮声纹验证或硬性历史隔离均不可行。
- **主要指标**：- Tier2英文F1：微调模型82.65（Gemini-2.5-pro 76.39）；开源模型（Qwen2.5-Omni 44.63等）≈随机 - Tier3英文F1：微调模型77.83，开源模型全部≈50% - Tier1英文Accuracy：微调88.11（LLM上界97.33） - 对抗攻击
- **代码**：官方发布 | **Demo**：https://interactionalprivacy.github.io/

---
## [ParaBridge: Bridging Paralinguistic Perception and Dialogue Behavior in Speech Language Models](https://arxiv.org/abs/2606.10581)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-06-09
- **一句话贡献**：针对SLM"能感知副语言线索却不据此调整开放对话行为"的感知-行为鸿沟（如Qwen3-Omni在VoxSafeBench儿童语音任务SAR仅6.1%），本文提出ParaBridge，基于on-policy自蒸馏的后训练方法：同一模型在scaffold加持下充当稠密逐token教师，向无scaffold学生分布蒸馏。仅1000条数据即可使无scaffold SAR从14.64%升至40.33%（超过
- **关键技术点**：现有SLM在MMSU副语言感知任务上可达52.8%，说明模型已具备线索识别能力，但普通请求中几乎不据此调整回复。推理时前置副语言提示scaffold可显著激发潜在能力（SAR 14.6%→29.0%），但此类scaffold在多轮长上下文、指令竞争下易失效；SFT需人工标注且有偏移风险，RFT只保留单条被选轨迹存在暴露偏差，GRPO仅提供稀疏标量奖励。
- **主要指标**：- VoxSafeBench SAR（无scaffold）：14.64%→40.33%（+25.69），超过scaffolded基线29.02% - EchoMind平均分：3.27→3.92（+0.65），C_SpeechRel +0.82 - 通用能力保持：MMAU-Pro 62.96(-0.2
- **代码**：暂无（承诺随上游许可发布LoRA适配器） | **Demo**：暂无

---
## [JoyAI-Talker: Full-Duplex Speech Interactive Large Model for Empathetic Voice Agents](https://arxiv.org/abs/2608.01119)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：京东提出JoyAI-Talker，一个全双工语音对话系统，采用模块化Thinker-Talker架构将认知规划、对话状态协调和语音生成解耦。通过统一的语音-文本联合训练流程缓解"认知退化"问题，在MATH基准上达到94.62%的推理准确率，同时在全双工交互中实现0.88的响应率和极低误触发率。PAER框架从音频中提取说话人属性（性别、年龄、情绪）并结合CoT推理生成共情响应。
- **关键技术点**：现有语音对话系统将语音交互作为独立模块附加在LLM后，导致模型在扩展到语音模态时出现"认知退化"——核心文本推理、STEM和逻辑能力显著下降。全双工交互中的打断、插话等复杂对话管理尚未得到系统解决。
- **主要指标**：- MATH基准: 94.62%（保持接近纯文本模型的推理能力） - Full-Duplex-Bench v2.5: 响应率0.88，误触发率极低 - T2T和S2T基准：达到竞争力性能 - 共情对话评估：PAER框架显著提升响应相关性和自然度
- **代码**：暂无 | **Demo**：暂无

---
## [Hidden-Domain Routing for All-Type Audio Deepfake Detection](https://arxiv.org/abs/2608.00493)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：语音深度伪造检测（SDD）系统在传统基准上表现良好，但现有方法难以处理所有类型的音频deepfake（语音、环境声音、歌唱、音乐）。OPPO提出隐藏域路由方案，首先用AudioType-BEATs-6s路由器从6秒窗口估计音频类型，然后路由到对应的分支检测器：Speech-XLSR（语音）、SoundMusic-EAT（声音/音乐）、Singing-EAT（歌唱）。在AT-ADD Challeng
- **关键技术点**：全类型音频deepfake检测需要在推理时音频类型未知的条件下，对语音、环境声音、歌唱、音乐四种类型的音频做出真假判断。不同类型音频的特征分布差异巨大，单一检测器难以同时处理。在AT-ADD Challenge Track2中，隐藏域设置（hidden-domain condition）要求系统在无类型标签的条件下进行检测。
- **主要指标**：- 总体Macro-F1: 96.10%（排名第一） - 各类型Macro-F1: 语音88.07%，声音98.18%，歌唱99.07%，音乐99.08% - 第二名: 未公布具体数值但显著低于本方案
- **代码**：暂无 | **Demo**：暂无

---
## [AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks](https://arxiv.org/abs/2608.05507)

- **方向**：语音深度伪造检测 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-08-06
- **一句话贡献**：现有语音深度伪造检测（SDD）系统在ASVspoof等传统基准上表现强劲，但情感表达和LALM攻击的覆盖极为有限。AffectDF是目前最全面的情感语音深度伪造基准，包含约260小时语音，21种欺骗攻击（TTS/VC/EVC/LALM-EVC四种范式），覆盖5种情感状态（中性/高兴/愤怒/悲伤/惊讶），同时包含表演性和自发性情感语音。评测发现：ASVspoof2019训练的模型在AffectDF上
- **关键技术点**：现有ASVspoof基准主要关注中性语音，情感欺骗数据集（EmoFake 7种VC攻击，EmoSpoof-TTS 3种TTS攻击）规模小、攻击多样性不足且缺乏LALM攻击。情感语音在基频、能量、语速、shimmer等方面引入巨大变异性，可能掩盖或改变SDD系统依赖的伪造痕迹。 **数据集构建：** 基于ESD（表演性情感语音，4个说话人）和MSP-Podcast（自发性情感语音，4个说话人）两个语料库。21种攻击：LALM-EVC（Qwen2.5-Omni, Kimi-Audio, MiniCPM-o 4.5，含steered版本）、TTS（CosyVoice/2/3, Qwen3-TTS, 
- **主要指标**：- ASVspoof2019训练→AffectDF测试: RawNet2 59.71%, AASIST 56.40%, XLSR-SLS 44.91%, XLSR-Mamba 29.78%, ProSDD 31.04% - ASVspoof5训练→AffectDF测试: ProSDD最优12.49%
- **代码**：https://affectdf33-data.github.io/AffectDF-Data/ | **Demo**：暂无

---
## [Listen, Reason, and Segment: Aligning LALMs with Editorial Judgment for Media Chapterization](https://arxiv.org/abs/2608.16539)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-08-18
- **一句话贡献**：音频章节化（把连续音频流切分为主题连贯章节）依赖主观编辑判断而非客观声学事件，现有 ASR+LLM 流水线仅适用于纯语音场景，且无纯音频端到端方案与评测基准。本文提出 AudioChaps 后训练框架，以 Audio-Flamingo-3-Think-8B 为骨干，通过 CoT-SFT 冷启动加 GRPO 校准将模型边界决策对齐 YouTube 创作者标注。在 AudioChaps-Eval 上平
- **关键技术点**：LALM 在标准 benchmark 上进步很快，却难以落地媒体工作流。章节边界本质是创作者主观编辑判断，而非可客观检测的声学事件；现有研究仅限视频域（VidChapters-7M）或转写级联（Whisper-Large-V3+Qwen3-235B 测试仅 48.0 F1），在音乐、游戏、动态媒体上显著退化，且缺乏有监督的推理数据。
- **主要指标**：- 片段级平均 F1：AudioChaps-R1 77.8 vs AF3-Think-8B 零样本 28.6 vs Step-Audio-R1-32B 59.3 - 分类别 F1：DM 73.4/G 75.5/M 84.6/SS 77.8，类别跨度由骨干的 43.9 收窄至 11.2 - 消融：直接
- **代码**：https://github.com/ta012/AudioChaps（录用后开源） | **Demo**：暂无

---
## [INSPIRE: A Benchmark for Instruction-Aware Speech Retrieval](https://arxiv.org/abs/2608.16203)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-08-18
- **一句话贡献**：语音检索现有系统依赖固定相似度匹配，无法适应多样用户意图。台大李宏毅组提出首个指令感知语音检索基准 INSPIRE，让自然语言指令动态指定语义内容、说话人身份、说话风格、环境声及多属性组合的匹配准则，并统一评测四种检索范式。结果发现无现有方法能稳健覆盖全部意图：级联流程在语义检索上最优（DailyTalk R@10=62.0），自监督语音模型更擅超音段属性（VCTK R@10=17.5），多属性综
- **关键技术点**：传统语音检索以固定声学/语义相似度或级联 ASR 检索定义相关性，一条查询只能对应一个目标；而真实场景中同一段语音在不同指令下应检索不同文档，现有方法无法按指令动态调节内容、说话人、风格、环境声等异构线索的权重，指令感知检索在文本/图像领域已有积累但在语音域尚属空白。
- **主要指标**：- DailyTalk（语义延续）R@10：Qwen3-Embedding 最高 62.00，优于 E5-Mistral 55.50、Qwen3-Omni 51.50、CLAP 0.00 - VCTK（说话人）R@10：WavLM-Large 17.50、HuBERT-Large 11.88，明显优
- **代码**：https://github.com/lca0503/INSPIRE | **Demo**：暂无

---
## [SpeechSense: A Paralinguistic-Focused Dataset for Fine-Grained Speech Sentiment Analysis](https://arxiv.org/abs/2608.17931)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-08-19
- **一句话贡献**：现有语音情感分析存在两大局限：文本中心pipeline经ASR转写后丢弃韵律、语调等副语言线索，且标签粒度停留于基本情绪类别，难以刻画社交场景所需的人际立场。本文提出SpeechSense数据集，定义8类可主要由韵律线索识别的人际立场标签体系，通过语义-韵律解耦文本设计+角色扮演TTS合成+人工双阶段验证构造高质量数据。实验显示，具备声学访问的多模态LLM（Qwen2.5-Omni-7B 宏F1达
- **关键技术点**：现有方法的局限有二。其一，文本中心pipeline将语音经ASR转成文本后再做文本情感分析，不可避免丢弃韵律、语调、停顿、重音、语速等副语言线索，且ASR转写错误会传播恶化下游情感性能，例如"We can't wait another decade"全靠声学表达区分"热情支持"与"不耐烦"。其二，标签粒度失配：IEMOCAP、RAVDESS、CREMA-D等主流数据集仅标注happy/sad等基本情绪；Ekman和Plutchik的离散情绪框架面向内部情感状态而非面向交谈对象的人际立场，口语场景尚无标准化标注体系。
- **主要指标**：- 零样本全部接近随机（宏F1仅1.31%–6.63%），说明预训练模型本身不具备细粒度立场表征 - 监督微调最佳音频模型 Qwen2.5-Omni-7B：准确率56.95%、宏F1 56.76%；Omni-3B：54.86%/53.38% - 最佳文本模型 Qwen2.5-Omni-7B：26.7
- **代码**：https://github.com/Sher13cked/SpeechSense | **Demo**：暂无

---
## [Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio Learners](https://arxiv.org/abs/2608.19863)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-08-20
- **一句话贡献**：本文提出 NAPE（Next-Audio-Patch-Embedding prediction），将大语言模型中"预测下一个元素"的自回归范式引入自监督音频表示学习：把一个因果 Transformer 训练为，仅凭之前谱图模块的嵌入去预测下一个 patch 的连续嵌入。设计刻意极简，只用因果掩码加 stop-gradient 作为全部训练信号，彻底摆脱了重建解码器、声学 tokenizer、tea
- **关键技术点**：
- **主要指标**：NAPE-L raster 达到 AS-2M 50.2 mAP、AS-20K 40.5、ESC-50 96.0%、KS1 97.9%、KS2 98.8%、ER 68.0%；NAPE-L diagonal（96.2%/98.2%/98.9%/68.8%）在除 AS-2M 外的任务上略优。与最强基线 S
- **代码**：https://github.com/umbertocappellazzo/nape | **Demo**：暂无

---
## [Explainability by Design: Structured Kolmogorov-Arnold Networks over Probabilistic Attributes for Speech Deepfake Source Tracing](https://arxiv.org/abs/2608.20213)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：9/10 | **日期**：2026-08-20
- **一句话贡献**：现代语音合成技术可生成高度逼真的伪造语音，因此深度伪造语音溯源（识别伪造语句背后的具体生成器）对取证、内容溯源与平台问责日益重要。本文在作者此前"透明概率属性"工作（将语句表示为合成器子组件的概率分布）的基础上做了两项关键扩展：一是用多任务学习（MTL）联合训练概率属性提取器，二是引入结构化 Kolmogorov-Arnold 网络（SKM）作攻击分类器。SKM 的拓扑显式遵循 ASVspoof 
- **关键技术点**：
- **主要指标**：最优配置 ST_RB_SSL-AASIST_ff（全微调 SSL-AASIST 骨干）在属性提取上 BAcc 99.59%–99.92%、EER 0.07%–0.16%，17 类攻击分类 BAcc 99.64%、EER 0.11%（最好）；AASIST 骨干下从零训练与全微调攻击分类为 99.53%
- **代码**：https://github.com/HoangHPham/KAN-Probabilistic-Deepfake-Attribution | **Demo**：暂无

---
## [Do SpeechLMs Hear Their Own Opinions? Diagnosing and Mitigating Previous-Belief Contamination in Streaming Emotion Understanding](https://arxiv.org/abs/2608.20769)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-08-24
- **一句话贡献**：流式语音情感理解普遍将模型上一时刻的预测作为历史上下文注入当前推理，本文通过反事实干预证明这种"历史信念"会污染当前音频的感知：固定音频、仅更换注入的上一个情感标签，CREMA-D-Stream 上准确率从 72.50% 跌至 30.42%，65.69% 的预测发生翻转，且效应强标签不对称（先验拉动率 4.76%~98.20%），作者称之为前人信念污染（PBC）。为此提出 EmoUpdate，一个
- **关键技术点**：现有流式情感系统将上一次预测当作历史文本直接写入感知提示，模型会"听见自己的观点"：错误状态递归回注并随时间放大，不同于普通识别误差或外部上下文偏见。单一粘性参数或提示词无法修复——10 个地面提示中 7 个明确要求忽略上一标签，错误先验拉动率仍不低于 59.7%，且随先验盲准确率上升而上升（Pearson r=0.81）。历史并非只是"权重大小"问题，而是参与了当前观测本身的形式化。
- **主要指标**：- EmoUpdate 在 8/8 个组合上取得最佳 S-BAcc 与 step accuracy、7/8 最佳 step macro-F1、6/8 最佳 final accuracy；DHC 直接历史条件化最高损失 49 分 step accuracy - HumDial-En：Qwen2-Aud
- **代码**：暂无（论文声明将发布完整复现工件与SHA-256审计日志，正文未附公开仓库链接） | **Demo**：暂无

---
## [TAG-Bench: Benchmarking Temporal Audio Grounding in Large Audio Language Models](https://arxiv.org/abs/2609.01542)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-09-01
- **一句话贡献**：大音频语言模型（LALM）能描述听到什么，但其精确定位"所查内容何时发生"的能力缺乏系统评估。本文提出 TAG-Bench，专门评估时间音频定位的基准：模型需返回与自然语言查询匹配的所有时间区间。TAG-Bench 包含 1,750 条人工核验的查询-录音对，覆盖 149.5 小时音频，8 个子集、时长跨度 7 秒到 20 分钟，其中 22.1% 查询含多个正确区间。21 个系统中最佳模型仅达 3
- **关键技术点**：现有 LALM 基准多聚焦内容理解和语音识别，对"何时发生"的时间定位评估零散不成体系。
- **主要指标**：- 最佳系统 mIoU：31.2 - IoU≥0.7 时最高 Recall：21.5% - 低于 5 mIoU 的系统数：9/21
- **代码**：暂无 | **Demo**：暂无

---
## [Auditory Illusion Benchmark for Large Audio Language Models](https://arxiv.org/abs/2609.02277)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-09-02
- **一句话贡献**：该论文提出AIB，首个面向大型音频语言模型（LALM）的听觉错觉基准，覆盖音乐、声音、语音三领域的十种代表性错觉，共14829个刺激（10385个错觉+4444个匹配对照）。方法将错觉感知判断重构为二元/三元选择题，并配以受控人类听感研究（20名绝对音高听者）实现人与模型的直接对比。结果显示多数LALM在低层物理型错觉上保持信号忠实，部分模型（Audio Flamingo 3、Gemini 3.1
- **关键技术点**：现有音频基准（SUPERB、AudioBench、MMAU等）聚焦转录、分类、推理等含客观真值任务，无法评估模型是否复现人类的主观错误知觉；视觉领域已有错觉基准，听觉领域尚属空白，LALM是否能像人类一样受错觉影响完全未知。
- **主要指标**：- 平均ISI最优：Audio Flamingo 3（8B）0.455（人类参照1.0） - 物理+知识型最高ISI：Audio Flamingo 3（8B）0.505；最高HLA：Gemini 3.1 Pro 0.707 - 模型分三态：易感型（MuLLaMa、Audio Flamingo 3）、
- **代码**：https://github.com/gillosae/aib | **Demo**：暂无

---
## [SonicCaps: Large-Scale Diverse and Fine-Grained Captioning for Improved Audio-Retrieval](https://arxiv.org/abs/2609.02343)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-09-02
- **一句话贡献**：现有音频-语言数据集普遍存在语义多样性低、描述缺乏声学细节、单对单映射无法反映听觉感知歧义等问题。本文提出大规模音频标题数据集 SonicCaps，含约70万音频片段与约1500万条标题，由多模态大语言模型 Qwen3-Omni 以音频和文本为条件联合生成，并针对每个音频生成约24条多粒度标题。消融实验表明，标题多样性的提升显著优于质量提升，能使 CLAP 模型在检索与零样本分类上一致获益，并提升
- **关键技术点**：音频感知天生具有一对多的语义歧义，而现有数据集通常每段音频只有一两条标题；LLM 生成的标题重复单调、缺乏细粒度声学细节，手工标注又难以规模化且存在主观偏差。
- **主要指标**：- AudioCaps-Val T2A R@5：Ours(8) 78.9 / SonicCLAP_AR 79.5（LAION-CLAP 64.7） - AudioCaps-Val A2T-any R@5：SonicCLAP_AR 71.3（LAION-CLAP 49.7） - Commercial-
- **代码**：暂无 | **Demo**：暂无

---
## [Summary of the ChinaVoices Challenge 2026: Data, Tasks, Baseline, and Methods](https://arxiv.org/abs/2609.03471)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：9/10 | **日期**：2026-09-03
- **一句话贡献**：为填补中文方言语音缺乏统一公开评测平台的空白，本文介绍与NCMMSC 2026联合举办的ChinaVoices Challenge 2026：覆盖16个方言类别，定义多方言识别与多方言ASR双任务，提供约320小时、说话人不相交的三类评测音频。基于Qwen3-ASR-1.7B的统一基线达到53.62% ACC与18.10% CER；最佳参赛系统分别冲到83.19% ACC与11.08% CER，且
- **关键技术点**：标准普通话ASR已趋成熟，但真实语音方言众多，方言类别判定与内容转写仍是难点。既有研究使用各方言语料但清单、训练资源与评测集各不相同，缺乏公开可复现、可公平比较的统一平台，同时需评测"识别方言"与"准确转写"两种相关但不同的能力。 **任务与数据：** 16个方言标签，数据约320小时（每方言约20小时），分参考集、开放评测集、隐藏评测集，三集严格说话人不相交，真值转写全部人工生成并质检。识别用macro ACC，ASR用macro CER；每任务设受限与开放双赛道。基线基于Qwen3-ASR-1.7B，LoRA只更新语言模型，把"方言标签+转写"统一为条件生成任务，开放集达到53.62% A
- **主要指标**：- 识别macro ACC：scy919 83.19%＞Optima 78.47%＞zenava.ai 73.42%（基线53.62%） - ASR macro CER：TeleASR 11.08%＜Mlslabs 11.22%＜Kyoto-Tsinghua 11.75%（基线18.10%） - 方
- **代码**：https://github.com/ASLP-lab/ChinaVoices-Challenge | **Demo**：https://aslp-lab.github.io/ChinaVoices-Challenge/

---
## [DAMOS: Learning Distortion-Aware Speech Quality Assessment through Explicit Distortion Localization](https://arxiv.org/abs/2608.21176)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-24
- **一句话贡献**：针对现有语音质量评估（SQA）模型仅以句级 MOS 作为监督、缺乏对感知关键失真位置的显式建模这一局限，本文首次将显式失真定位作为辅助知识引入 MOS 预测。作者构建了首个带帧级失真标注的部分失真语音数据集（15,000 条、覆盖五类 23 种失真），并训练 BAM 定位模型输出帧级失真掩码；在此基础上提出 DAMOS 框架，通过 DSLA、DistortionFiLM 与 LQR 三个模块渐进地
- **关键技术点**：现有 SQA 模型依赖句级 MOS 粗粒度监督，既无法指示失真正发生在哪些时域区域，也难以刻画"整体质量往往由少数显著失真区主导"这一感知特征；对于 TTS/VC 等合成语音，发音错误、局部语音塌陷、声码器伪影等短时局部失真会不成比例地拉低听感。作者指出当前 SQA 缺的不是更复杂的网络结构，而是描述"失真在哪"的辅助知识，但公开数据集无帧级标注，且定位信息如何融入预测管道尚待探索。
- **主要指标**：- BVCC 句级：SRCC 0.885、LCC 0.884、MSE 0.191；系统级：SRCC 0.931、LCC 0.931、MSE 0.100 - 对比 UTMOS（SRCC 0.878/SRCCsys 0.930）、SSL-MOS（0.870）、NISQA（0.784） - In-doma
- **代码**：暂无 | **Demo**：暂无

---
## [ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection](https://arxiv.org/abs/2609.03620)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对真实场景"真伪线索共存"（时间切换、声源重叠或混合）这一传统整段二分类难以处理的问题，提出ToolDF——以音频大语言模型为编排器、经监督工具调用轨迹训练的"工具集成推理"框架。框架自适应分析声学场景、按需调用Demucs分离与人声/背景域专用检测器并聚合证据输出可解释判决。在混合真实性基准上，ToolDF复合类型检测C-Avg达81.89，较最强单体基线XLSR-AASIST提升3.72个点
- **关键技术点**：现有ADD普遍假设单域、整段二分类（ASVspoof、CtrSVDD、EnvSDD各自独立）。但真实操控音频可为"混合真实性"：一段剪辑内可同时含真语音到合成歌唱的切换、叠在真实背景乐上的伪元素等。域专属检测器遇到域外声源失效，整段分类器易漏检局部操控，固定先分离再检测的流水线对无需分离的输入引入伪影，直接ALLM做分类器则是黑箱。
- **主要指标**：- C-Avg（复合）：ToolDF 81.89，超最强单体XLSR-AASIST 78.17（+3.72） - 固定流水线C-Avg 67.50，ToolDF +14.39 - Oracle上界C-Avg 82.85，与ToolDF仅差0.96 - 定位（DCASE事件级宏F1）：Speech 9
- **代码**：https://github.com/rlataewoo/tooldf | **Demo**：暂无

---
## [Robust Speech Emotion Recognition under Tone-Word Conflict: A Benchmark and Framework](https://arxiv.org/abs/2609.04236)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-07-27
- **一句话贡献**：现有语音情感识别（SER）系统默认音调与词义一致，但现实交互中普遍存在"声调-词义冲突"（反讽、冷怒等），主流方法在此场景下性能崩溃。针对这一问题，论文构建了首个高密度冲突基准 TWIN-SER（378 条多语言样本，经 LLM 场景生成与 TTS 合成），并提出 DAS（解耦声学-语义融合）框架：通过 MingTok-Audio 声学 tokenizer 与 Whisper 语义编码器双路径解耦
- **关键技术点**：论文指出现有方法存在三类结构缺陷：一是语音-文本联合预训练模型（Whisper、CLAP）存在语义偏置，模型被字面含义"污染"；二是 SSL 编码器（HuBERT、wav2vec2、WavLM）产出声学与语义纠缠表征，冲突难以消解；三是大语音语言模型（Qwen2-Audio、Qwen2.5-Omni）的编码器优先语义而削弱韵律情感线索。同时社区缺乏控制变量式的高密度冲突评测基准。
- **主要指标**：- TWIN-SER：DAS WA 59.38 / WF1 55.08，最强基线 Whisper 47.26 / 44.97，HuBERT 32.90、Qwen2.5-Omni 34.66 - 退化证据：HuBERT 在 ESD 上 80.1%、TWIN-SER 上跌至 32.9%；Qwen2.5-
- **代码**：https://github.com/24DavidHuang/FAS | **Demo**：暂无

---
## [Cloned Voices, Real Consequences: Evaluating Bias in Political Deepfake Detection for Electoral Integrity in Brazil](https://arxiv.org/abs/2607.28770)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-07-30
- **一句话贡献**：生成式AI使制作假音频更容易，在选举期间放大政治虚假信息。本文引入ParlaSpoof-BR，一个基于巴西众议院官方录音构建的葡萄牙语政治语音deepfake数据集，包含40名说话人（性别和地区平衡）、2,000个真实样本，通过5种TTS、5种语音转换和部分操控（音频infilling）扩展至134,400个文件（11,200真实/123,200伪造）。评估发现：AASIST和AASIST-L在P
- **关键技术点**：
- **主要指标**：- 总体EER：AASIST 50.98%, AASIST-L 53.70%, DF-Arena-1B 32.30% - TTS检测（DF-Arena-1B）：平均EER 39.3%，Qwen3-TTS最差（EER 58.0%, 召回31.2%） - VC检测（DF-Arena-1B）：平均EER 
- **代码**：https://huggingface.co/datasets/freds0/ParlaSpoof-BR | **Demo**：https://ermisai.github.io/parlaspoof-br-demo

---
## [Beyond Residual Connections: Manifold-Constrained Hyper-Connections for Robust Speaker Representation](https://arxiv.org/abs/2608.05549)

- **方向**：说话人识别 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-06
- **一句话贡献**：标准残差连接的恒等映射将信息流限制在单一路径，导致深层网络中特征冗余。mHC（Manifold-Constrained Hyper-Connections）将残差路径重写为多流演化，通过Sinkhorn-Knopp迭代将可学习混合矩阵投影到双随机流形上，保证能量守恒（信号强度和特征均值保持）。在ECAPA-TDNN、ResNet-34、Res2Net、E-Res2Net四种骨干网络上，mHC一致提
- **关键技术点**：标准残差连接的逐通道相加（y=x+f(x)）缺乏跨通道信息交换机制，随着网络加深产生高度相关特征。Hyper-Connections (HC) 通过多流并行和可学习混合矩阵促进信息交换，但失去恒等映射性质导致信号爆炸/衰减。mHC在保留HC多流交互优势的同时，通过双随机流形约束恢复恒等映射的稳定性。
- **主要指标**：- mHC-ECAPA-L (20.76M): VoxCeleb1-O EER 0.77%（相对降低11.5%），Vox-E 0.94%（-16.1%），Vox-H 1.88%（-11.3%） - mHC-ECAPA-S (6.19M): Vox-O EER 0.98%（-3.9%），Vox-E 1
- **代码**：暂无 | **Demo**：暂无

---
## [VocalCoachBench: Benchmarking Audio-Language Models on Expert Feedback for Singing](https://arxiv.org/abs/2609.04241)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-06
- **一句话贡献**：当前音频语言模型评测集中于描述、识别与问答，缺乏对"面向专家的分析式反馈"能力的检验。本文提出 VocalCoachBench，首个面向演唱声乐教练式反馈的专家标注评测基准：含 515 条演唱录音，由 18 位职业声乐教师产出 1052 份反馈与 12051 条原子教练断言。基准将确定性结构化任务（三元组排序、Top-3 问题标签、分段问题分类）与基于原子断言的开放式诊断/纠正评测分离。实测 12
- **关键技术点**：现有歌唱自动评估聚焦打分、排序等感知质量判断，基准数据多为小型、平台私有，音乐表演反馈资源面向钢琴/器乐且不将诊断与纠正的有效性本身作为评测目标。关键难点在于声乐教练反馈天然开放——同一演唱不同教练会给出不同主次问题与纠正策略，单一标量分无法刻画。两轮预实验证实标量评分格式失败：4 位专家对齐评分标准后整体 Krippendorff's α 仅约 0.323，分歧源于刻度"阈值校准"，故最终移除标量评分。
- **主要指标**：- 三元组两两比较：Qwen3.5-Omni Plus 74.5% 最佳，开源最佳 Qwen2.5-Omni 68.7%，Fun-Audio-Chat 49.3% 低于随机 50.0% - 细粒度 Top-3 F1@3：所有模型均未超过多数基线 62.4% - 严格诊断命中率：全部低于 7%（最高 
- **代码**：暂无具体 URL（标注数据、提示词与评估代码将公开释放） | **Demo**：暂无

---
## [Training-Free Speech-Centric Omni Understanding with Frozen VLMs](https://arxiv.org/abs/2609.04242)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-07
- **一句话贡献**：原生 Omni 模型需引入专用音频编码器并依赖大规模音视频文本联合训练，音频通路与特定 VLM 骨干强耦合，成本高且脆弱，并可能削弱其既有视觉、推理与领域能力。本文提出 TFO（Training-Free Omni），一个即插即用的免训练框架：仅用 Whisper 将音频转为经过置信度过滤、带时间戳的转写文本，经 VLM 原有语言接口注入，视觉通路完全不变。在 56 个基准、21 种语言、四个模型
- **关键技术点**：原生 Omni 模型通过为 VLM 附加音频编码器并做大规模多模态对齐获得语音能力，但存在三点根本困难：一是每次 VLM 骨干升级都要重做音频通路适配；二是音频信号须与语音内容和视觉事件精确对齐，文献表明原生训练的视听模型仍会忽略相关音频、凭视觉臆测声音；三是修改并联合训练骨干会削弱既有能力。现有评估缺乏与原生训练严格对照的免训练基线，无法回答"音频通路是否对每类任务都必需"。
- **主要指标**：- 视听理解：Qwen2.5-3B 43.2→46.2（+3.0）、7B 45.8→48.0（+2.2），WorldSense 最高 +14.5 - 多语言转写：五档 +7.9/+13.5/+18.4/+11.1/+6.8，MiniCPM4.5 达 64.0 - 纯音频理解：全五档提升，VILA 档
- **代码**：https://github.com/mbzuai-oryx/OmniEvalKit | **Demo**：https://mbzuai-oryx.github.io/OmniEvalKit

---
## [RAG-Audio: Retrieval-Augmented Generation for Faithful Brain-to-Audio Reconstruction](https://arxiv.org/abs/2608.09331)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-10
- **一句话贡献**：脑到音频重建受限于"先验主导"问题：当预训练生成器以弱神经信号为条件时，会产生逼真但刺激不准确的音频。RAG-Audio 将 fMRI 解码为语义音频 embedding，检索匹配的真实音频样本，从该样本初始化冻结生成器的采样轨迹，同时保留解码 embedding 作为条件。在 Brain2Music 上，10 路刺激识别从 0.14-0.18（直接生成，接近随机 0.10）提升到 0.40-0.
- **关键技术点**：脑到音频重建中，fMRI 信号空间分辨率有限（~2mm），时间分辨率低（~1s），导致条件信号弱。预训练生成器倾向于产生"先验主导"的输出——逼真但与刺激无关。现有方法难以区分 generator 先验和神经信号驱动的重建。
- **主要指标**：- 10 路刺激识别：0.14-0.18 → 0.40-0.43（直接生成→RAG-Audio） - FAD：13.49 → 1.25（AudioLDM） - 与最近邻检索接近（检索 0.46-0.49），但保持生成性
- **代码**：暂无 | **Demo**：暂无

---
## [From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs](https://arxiv.org/abs/2608.09158)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-10
- **一句话贡献**：大型音频语言模型（LALM）已展示理解多样音频输入的能力，包括人类听不见的低频信号。该工作提出间歇性低频锁定（ILL）攻击方法，使用通用波形模板在黑盒设置中评估此风险。ILL 使用句子注意力尺度估计确定活跃区间，频率混淆转移从语料谱变化构建连续相位低频波形。提出分布重查询守卫（DRG）检测低频分布偏移并条件性请求第二次录音进行语义恢复。在 6 个 LALM 和多个音频理解任务上，ILL 降低准确率
- **关键技术点**：LALM 处理人类可听频段（20Hz-20kHz）和不可听低频（<20Hz）信号，但低频输入对 LALM 安全性的实际影响尚未被探索。
- **主要指标**：- ILL 攻击：准确率降低高达 67 个百分点 - 人类可听度评分：1.33（干净音频 1.17，5 分制），接近不可感知 - DRG 防御：平均攻击准确率从 28.5% 提升到 46.1%
- **代码**：暂无 | **Demo**：暂无

---
## [The GENEA Challenge 2026: Large-Scale Disentangled Evaluation of Speech-Driven Gesture Generation](https://arxiv.org/abs/2608.10839)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-11
- **一句话贡献**：GENEA Challenge 2026 是第四届语音驱动手势生成挑战赛，在 Seamless Interaction 对话数据集上对 5 个参赛系统进行大规模人类评估。采用解构评估方法分别评估动作质量和语音对齐，消除两者混淆效应，并引入新的语义手势生成任务和文本失配评估方法。在四个大规模用户研究中收集了 869 名测试者的 23000+ 投票。关键发现：数据集中过滤片段在动作质量上远超所有参赛系
- **关键技术点**：语音驱动手势生成评估中，动作质量和语音对齐通常相互混淆——高质量动作可能因与语音不匹配而评分低，反之亦然。现有方法未有效分离这两个维度。
- **主要指标**：- 动作质量：数据集过滤片段 68-95% 配对胜率（所有参赛系统中最高） - 语音对齐：Mocap 基准 62%，最佳提交 32%，其余仅略高于 0%（输入无关系统预期） - 对话互动：Mocap 基准 65% 适当性，无提交显著高于随机水平 - 语义手势：数据集匹配转录识别率 79%，最佳系统仅
- **代码**：暂无 | **Demo**：暂无

---
## [Never Stop Speaking: a Denial-of-Service Attack on End-to-End Speech Language Models](https://arxiv.org/abs/2608.10405)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-11
- **一句话贡献**：现有文本 DoS 攻击主要针对纯文本 LLM，端到端语音 LLM 的 DoS 漏洞尚未被探索。该工作提出基于扰动的 DoS 攻击，优化不可感知的声学扰动以影响 E2E 语音 LLM 的自回归生成过程，在保持原始输入长度的同时抑制 EOS 生成、鼓励延长解码。使用 VAD 仅在有声区域注入扰动。在三个开源 E2E 语音 LLM 上实现了稳定攻击成功率，显著增加生成长度和 GPU 资源消耗，揭示了现代
- **关键技术点**：文本 LLM 的 DoS 攻击通过 prompt 工程（对抗后缀、语义诱导）实现，但无法直接迁移到连续语音输入。现有语音模型安全研究主要关注 ASR/TTS 系统，未涉及 E2E 语音 LLM 的 DoS 脆弱性。
- **主要指标**：- 稳定攻击成功率（ASR） - 显著增加生成长度和 GPU 资源消耗 - 扰动隐蔽性高（VAD 策略）
- **代码**：暂无 | **Demo**：暂无

---
## [VoxSumm: A Multilingual Corpus of Long-Form Spoken News for Joint Summarization and Translation](https://arxiv.org/abs/2608.10359)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-11
- **一句话贡献**：长文档摘要研究仍以文本为中心，多语言语音研究主要优先翻译而非压缩。VoxSumm 正式定义联合语音摘要与翻译（JSumT）任务——从源语言长口语文档直接生成目标语言简洁忠实摘要。构建首个多语言跨语言基准，包含 10045 个 BBC 文章-摘要对，覆盖 24 种语言，约 703 小时语音数据。评估代表性语音语言模型，Gemini3.1-Pro 表现最佳，英语摘要普遍优于非英语目标语言生成，先翻译整
- **关键技术点**：多语言语音研究主要关注翻译（保留源内容），长文档摘要研究主要关注文本。两者结合——从语音直接生成跨语言摘要——尚未被正式定义和基准化。
- **主要指标**：- Gemini3.1-Pro 表现最佳 - 英语摘要质量优于非英语目标语言 - 先翻译后摘要策略加剧指令遵循失败
- **代码**：暂无 | **Demo**：暂无

---
## [AT-ADD: All-Type Audio Deepfake Detection Challenge Summary](https://arxiv.org/abs/2608.14249)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-17
- **一句话贡献**：本文是ACM Multimedia 2026 AT-ADD大挑战赛的总结报告，针对音频深度伪造检测领域两大核心问题：一是在真实声学与信道变化下的鲁棒语音深度伪造检测（Track 1），二是跨语音、环境音、歌声和音乐四种类型的全类型音频深度伪造检测（Track 2）。挑战赛采用封闭设置，参赛者仅可使用组织者提供的训练/开发数据、信号级数据增强和可追溯的通用预训练模型。Track 1评估集包含26种未
- **关键技术点**：现有ADD研究在ASVspoof和ADD挑战系列中取得显著进展，但实际部署面临两大关键瓶颈：一是真实声学环境和信道条件下的鲁棒性不足，现有基准测试中的真实语音多来自受控环境，而实际场景中录音设备、声学环境、语言种类等因素存在巨大变化；二是面对异构音频类型（语音、环境音、歌声、音乐）时的泛化能力有限，生成式AI已能合成各种类型的高保真音频，而现有检测器大多仅针对单一语音类型设计。
- **主要指标**：- Track 1冠军WaveShield（w2vBERT2.0-AASIST）：Macro-F1 90.71% - Track 1亚军Fosafer（ssl_gfcc_multiscale_ensemble）：Macro-F1 86.67% - Track 1季军sonomsl：Macro-F1 
- **代码**：暂无 | **Demo**：暂无

---
## [Trajectory Dynamics in Self-Supervised Learning Latent Space for Audio Deepfake Detection](https://arxiv.org/abs/2608.13817)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-17
- **一句话贡献**：现有语音深度伪造检测方法大多依赖SSL特征提取器加全局池化，丢弃了时序顺序信息，在跨语料库泛化时性能急剧下降。本文提出利用人类语音生理约束在SSL潜空间中产生的结构化轨迹动态进行检测：训练一个因果LSTM下一帧预测器（Stage 1），仅在ASVspoof 2019的真实语音上学习轨迹动态，以预测误差作为异常分数；可选Stage 2将冻结的LSTM隐状态均值池化后训练一个有监督MLP分类器。在AS
- **关键技术点**：现有SSL检测方法（如AntiDeepfake、SLIM、QAMO、BreathNet）大多对帧级嵌入做全局平均池化或注意力加权汇总，完全丢弃时序顺序。少量利用时序结构的工作（FGFM、TRACE、BreathNet）要么针对局部拼接伪影，要么需要伪造监督信号，均未建模整段语音的全局生理合理性轨迹。
- **主要指标**：
- **代码**：https://doi.org/10.5281/zenodo.21879214 | **Demo**：暂无

---
## [ARENA: Automated Red-Teaming for Large Audio Language Models](https://arxiv.org/abs/2608.15578)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：针对文本侧安全而音频侧藏有害意图的"音频接地"攻击，本文提出 ARENA 闭环红队框架：用独立 2000 条文本-音频规格训练控制器，MD-Judge 提供训练奖励与自适应搜索反馈，仅由非自适应的 Llama Guard 3 独立裁决最终结果。在 520 条 AdvBench 目标上，ARENA 在 Audio Flamingo 3、Qwen2-Audio、MiMo-Audio、GPT-Audio
- **关键技术点**：现有 LLM/多模态红队聚焦文本或视觉，LALM 的音频通道使无恶意的文本查询结合语音/环境音后可能诱导有害行为，且静态音频越狱集（AJailBench、JALMBench）无法自适应不同目标模型；失败响应中的识别失败、拒绝、事件复述等结构信号未被利用。
- **主要指标**：- FDR：AF3 87.9% | Qwen2-Audio 71.5% | MiMo-Audio 68.1% | GPT-Audio 75.4%（PSR：100.0/96.3/100.0/98.5%） - 基线对比：AJailBench FDR 仅 31.2/10.8/25.3/24.6% - 转移
- **代码**：https://github.com/Leanwithming/ARENA | **Demo**：暂无

---
## [ACE-Cap: Active Evidence Acquisition via Agentic Co-Evolution for Long-Paragraph Fine-Grained Audio Captioning](https://arxiv.org/abs/2608.16162)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：长段落细粒度音频字幕生成要求模型覆盖多样化声学事实，但现有字幕器均为被动一次性生成器，遗漏细节后无法自查、定向查询音频或自适应决定何时证据充分。本文将任务重构为主动证据采（Active Evidence Acquisition）问题，提出 ACE-Cap：由 Captioner 生成初始描述，文本-only 的 Composer 多轮提问、由音频条件化的 Instruct 回答，证据累积后 Com
- **关键技术点**：现有一键式字幕生成模型在粗粒度或短句生成上表现良好，但面对长段落细粒度字幕时一旦遗漏细节便无法补救；扩大模型与数据规模无法获得主动信息获取机制。同时多轮交互训练存在两大难题：异构动作（提问/停止/合成）的跨回合信用分配（相邻差分法受回合顺序与分数饱和影响、给予早问以首动者优势）；多智能体共同优化时的目标移动导致训练不稳定。
- **主要指标**：- MMAU：73.0（超最强开源 5.1pp、超 Gemini 2.5 Pro 3.0） - MMAR：64.1（超最强开源 8.8pp、与 Gemini 2.5 Pro 持平） - MMSU：70.4（超最强开源 2.2pp） - Omni-Cloze：64.4%（全方法最优，超 Qwen3-O
- **代码**：暂无 | **Demo**：暂无

---
## [How Fragile Is Your Watermark? Training-Free Structural Removal of Neural Audio Watermarks](https://arxiv.org/abs/2608.16566)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：论文提出"先诊断后移除"的免训练框架：从少量干净/含水印配对信号计算四个廉价结构探针，估计水印嵌入域并据此选择单一匹配攻击，取代固定失真集的盲目扫描。在 10 种水印方案上，幅度域方案 WavMark、SilentCipher、audiowmark 被单次匹配攻击在近乎透明质量（PESQ≥3.6）下擦除载荷，AudioSeal 检测标志被移除；潜在域方案 VoiceMark、WMCodec、Ali
- **关键技术点**：现有鲁棒性评估（AudioMarkBench、RAW-Bench、SoK）对全部方案盲目施加同一固定失真集，仅报告聚合准确率/检测率，掩盖了攻击者真正关心的两个问题：水印嵌入在哪里、哪种扰动移除代价最低。已有移除方式要么是经典估计/减法、谐波攻击，需训练跨域去除网络。
- **主要指标**：- WavMark：模板减法后 bit-acc 降至 5.9%，PESQ 4.17，fragility 0.87 - SilentCipher：RMS 自适应减法后 10.3%，PESQ 3.84，fragility 0.84 - audiowmark：48.4%，PESQ 4.22，fragili
- **代码**：https://github.com/i-618/audio-watermark-fragility | **Demo**：暂无

---
## [Navigating Speech Enhancement for Real-Time MRI: A Systematic Assessment of Signal Quality, Source Preservation, and Downstream Tasks](https://arxiv.org/abs/2608.16125)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：实时 MRI（rtMRI）同步录音被扫描仪梯度噪声严重污染，通用语音增强能否真正改善信号可用性此前缺乏系统验证。本文对 Denoiser、PASE、RE-USE 三个离架增强系统在五个 rtMRI 语料库上展开跨信号质量、源保真与下游任务的多端点评测。核心结论是增强效果与端点强相关：RE-USE 在 15 组对比中 11 组降低 WER，Denoiser 却在 13 组升高 WER；配对加噪探针中
- **关键技术点**：rtMRI 语音受 MRI 梯度噪声（周期性强宽带瞬变叠加谐波）污染，即使经定制光纤麦克风、自适应对消与 DSP 处理仍有残留，严重影响 ASR、说话人建模、情绪识别与发音学研究。现有评测聚焦常规含噪语音，未验证跨语料库（0.55T/1.5T 场强、不同麦克风）时增强是否保留测量相关属性；且学习型 MOS 预测器对域外数据的效度未经检验。
- **主要指标**：- WER（RE-USE）：15 组 DSP 对比 11 组下降，均值 ΔWER=-1.28 点；LSS Raw 上 Qwen3 6.29→4.90% - WER（Denoiser）：13/15 组升高（Δ+3.04 点），LSS Raw Qwen3 6.29→10.02% - STOI/ESTOI
- **代码**：暂无 | **Demo**：https://rmridemo.huangchengchou.com

---
## [Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges](https://arxiv.org/abs/2608.17605)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：本综述系统覆盖多轮对话AI从文本向多模态交互的演进，横跨纯文本对话、AudioLLM/语音原生系统、多模态/全模态系统与工具增强智能体四类体系，以session级持续交互（而非单轮响应）为分析单元，沿数据集与基准、建模范式、训练策略、评测设置与跨领域挑战组织文献（初筛约4K篇，经PRISMA-ScR筛选精读200篇）。核心发现：多模态感知/说话/行动能力进步快于跨轮连贯交互能力，持久记忆、跨轮gr
- **关键技术点**：真实对话中用户会澄清目标、修订请求、打断答复、切换话题、引入新证据，并要求系统保留上下文。现有前沿模型即使信息在上下文窗口内也常利用不足，任务分散在多轮时性能退化（Lost in Multi-turn、MultiChallenge），且此类失败只在session级显现、轮级评测会漏检；语音/多模态/工具设置下错误还会跨轮传播（ASR错误、视觉grounding衰减、工具外部状态）。
- **主要指标**：- 核心发现：多模态感知/说话/行动能力强，但持久记忆、跨轮grounding、全双工、鲁棒评测与跨文化对齐不足；长horizon与多session对话资源稀缺 - 评测现状：LLM-as-judge与混合打分为主导（53个基准中多采用J/M），但session级指标、人类校验与可复现性仍欠开发；口
- **代码**：https://github.com/faiza-sfa/multiturn-conversational-ai-survey | **Demo**：暂无

---
## [Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models](https://arxiv.org/abs/2608.17102)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：多模态基础模型（MFM）识别语音与面部情绪时，是依赖共享的情感功能单元还是模态特异通路，此前尚无定论。本文以语音情感识别（SER）和面部表情识别（FER）为互补探针，在 Gemma-4-12B-it、MiniCPM-o-4.5、Qwen2.5-Omni-7B 中利用对比激活边际（ConAct）定位稀疏解码器情感敏感神经元（ESN）。结果显示：去激活 ESN 选择性损害对应情绪（Gemma FER 
- **关键技术点**：心理学与情感计算长期争论情感感知源于跨模态共享类别还是模态特异线索。本文以语音和面部情绪识别作为测试床，首次在激活层面对齐 MFM 内部情感表征：识别 ESN、分析结构对齐并因果验证，判定情感处理是否收敛于共享的解码器组件（基于 Introduction）。
- **主要指标**：- 去激活视觉 ESN（V-ESN 于 FER）：Gemma-4-12B-it -25.80（Gap -28.33）、MiniCPM-o-4.5 -10.33（-11.16）、Qwen2.5-Omni-7B -10.40（-10.65）；随机掩码仅 -0.28~-1.07 - steering 增强
- **代码**：暂无 | **Demo**：暂无

---
## [The Last Mile of Deepfake Speech Detection: An Industry-Academia Experience Report](https://arxiv.org/abs/2608.17585)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：本文是捷克内政部 SECTECH 项目（VB02000060）资助、Phonexia 与布尔诺理工大学合作三年、面向捷克警方交付深度伪造语音检测器的产业-学术经验报告。核心问题：公开 benchmark 宣称 sub-1% 错误率，但现实部署在"最后一公里"失效。三大 barrier：公开语料不可商用授权（数据灰色地带）、真实输入是长录音/codec 退化/部分合成而非 4 秒干净片段、LLR 2
- **关键技术点**：现有合成语音检测 benchmark（ASVspoof 系列、in-the-wild 语料）宣称 in-domain 亚 1% 错误率，但 Müller 等报道跨域 EER 退化达 1000%，社区共识是深度伪造检测本质为 OOD 泛化问题。本文不提出新模型，而是从引擎内部视角记录生产化过程，指出 in-domain 精度无法证明部署就绪。
- **主要指标**：- 现有 benchmark：in-domain sub-1% EER，但跨域退化高达 1000%（引述他人结果） - 现实部署：telephony 场景假警率约 5%→70%，AMR-NB 与 G.711 下 EER 分别约 16% 与 25% - 内部 seen/unseen 分量验证：v2（a
- **代码**：暂无 | **Demo**：暂无

---
## [Represented but Ignored: A Causal Account of Prosodic Underuse in Audio-Language Models](https://arxiv.org/abs/2608.19211)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-20
- **一句话贡献**：人类语音的韵律承载着超越词汇内容的语言与情感信息，理想的音频语言模型（audio-LLM）应能理解"怎么说"而不只是"说了什么"，但现有基准只评测最终答案，无法定位模型韵律失败的根源。本文提出一个分阶段的探针阶梯（probe ladder），把韵律失败划分为三大机制：F1 感知失败（语音通路未保留韵律对比）、F2 解释失败（内部表征了错误的韵律类别）、F3 使用不足（内部表征正确但未充分表达在答案
- **关键技术点**：
- **主要指标**：音频通路探针在三个 Whisper 塔模型（Qwen、AF3、DeSTA）的 projector 处，CREMA-D/ESD 上 WA 达 0.79–0.92（相对随机基线提升 +0.28~+0.35），VESUS 达 0.69–0.72，IViE Q/stmt 达 0.71–0.81，纯 F1 在
- **代码**：暂无 | **Demo**：暂无

---
## [Tracking the Trend in How Speech Synthesizers Deceive People](https://arxiv.org/abs/2608.19959)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-20
- **一句话贡献**：早期研究普遍报告人对深度伪造语音有 70–80% 的检出率，但这些结论大多基于 2019 年左右的旧一代合成器。本文针对 2019、2022、2024 三个不同发布时期的合成工具（RTVC、YourTTS、ElevenLabs）开展受控实证比较：82 名 IT 从业者在明确被告知"存在深度伪造"的条件下，对全合成（full spoof）与局部替换（partial spoof）语音做逐句真实性判断，
- **关键技术点**：
- **主要指标**：全伪造方面，RTVC 与 YourTTS 的人类 F1 与 All OK 均约 0.90（逐句准确率 0.96–0.97），而 ElevenLabs 的 All OK 仅 28%、Over 50 Percent 仅 33%（接近 31% 的随机基线）、F1 为 0.48、逐句准确率 0.43（低于 
- **代码**：暂无 | **Demo**：暂无

---
## [Grounded Decoding for Autoregressive Speech Enhancement via Adaptive Code-Space Grounding and Local LLM Refinement](https://arxiv.org/abs/2609.04245)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-21
- **一句话贡献**：LLM 自回归语音增强（SE）能借助干净语音先验生成自然语音，但易产生输入不支持的内容幻觉；确定性增强更忠实保留观测证据，却常残留噪声或局部失真。本文提出证据锚定的生成式 SE 框架：以 Whisper 引导的 DPRNN 确定性增强器输出作为观测耦合证据，与带噪观测混合后经 FSQ 分词得到离散证据序列用于条件生成，并设计 Code-Space Grounding（CSG）按 FSQ 空间中的汉
- **关键技术点**：确定性 SE 在 DNN 输出层保留语言内容但残留噪声与局部失真；LLM 类生成式 SE 利用长程上下文恢复重度退化区域，但强先验可能覆盖模糊声学证据造成幻觉。已有低幻觉生成式 SE 主要改进送入生成器的信息，并不显式约束解码过程本身。本文核心出发点是把确定性输出当作不完美但观测耦合的证据而非最终结果或伪干净目标。
- **主要指标**：- 测试集 WER：UD 9.3% → CSG 8.5% → SNR-CSG 8.5% → GNR-LLM(50,3) 8.5% - 确定性基线 E2-WhspDPRNN：WER 6.5%、STOI 0.937、PESQ 2.522、SI-SDR 17.30 dB - 受控 SNR：−5dB 时 G
- **代码**：暂无 | **Demo**：暂无

---
## [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：长音频输入的语音LLM其推理瓶颈由模型参数转移到KV缓存（10分钟音频即占7500-15000个KV位置）。现有prefill-only压缩方法在长音频上失效：prefill注意力集中于音频开头（attention-sink），而decode注意力分布均匀。本文提出WnW，通过离线校准将KV头分类为anchor/tidal/fixed三类，解码期以anchor头注意力作为重要性观测信号，将tida
- **关键技术点**：现有H2O、SnapKV、Ada-KV、AudioKV等方法均在prefill阶段利用提示注意力一次性打分并固定保留集，其核心假设"prefill注意力能预测decode期注意力"在长音频上不成立。论文实测prefill注意力呈attention-sink分布（前10%位置占47.9%质量），而decode累积注意力近乎均匀（前10%仅9.8%）；240个KV头逐头Jaccard（K=100）在0.006-0.641间。一旦prefill期将位置永久丢弃、无恢复通道，压缩方法就结构性受损。
- **主要指标**：- Voxtral-mini-3b，r_GPU=20%：WER 6.23/8.87（Full Cache 6.79/8.86） - Qwen2.5-Omni-3B，r_GPU=20%：WER 15.31/18.42（Full Cache 13.87/16.80） - 同预算基线（r_GPU=20%）
- **代码**：https://github.com/XMUDeepLIT/WnW | **Demo**：暂无

---
## [MetaSICL: Globalizing Auditory LLMs for Underserved Speakers and Languages via Meta Speech In-Context Learning](https://arxiv.org/abs/2601.18904)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：听觉大语言模型多在高资源英语成人数据上训练，对儿童语音、语音翻译方向及文化性音频理解等低资源场景表现差，直接微调在分布偏移下易过拟合甚至退化。作者提出MetaSICL后训练配方，仅用充沛的高资源ASR+ST数据以上下文学习（ICL）格式构建episode，教会模型"如何使用演示"做测试时适配。在两个backbone（MiMo-Audio与Qwen2.5-Omni）上，MetaSICL相比vanil
- **关键技术点**：全球化生成式AI要求听觉LLM适配低资源用户、语言、方言与年龄组，但现有模型被成人英语等高资源数据主导。多数目标社区在训练数据中覆盖不足，而收集标注充分的域内语料成本高、难以代表真实测试分布，直接监督微调会过拟合到数据集特有伪影。文本领域MetaICL等已证明元训练可增强ICL能力，但该范式是否适用于听觉LLM仍属空白。
- **主要指标**：- 儿童ASR WER（Qwen2.5-Omni）：MyST 22.72→17.03（MetaSICL）；RSR 27.86→21.95 - 音频理解准确率：MMAU 65.80%→71.10%，MMAR 49.20%→54.40% - 语音翻译 BLEU：en→ja 33.53→35.72，ja→
- **代码**：暂无 | **Demo**：暂无

---
## [MRMAD: A Multi-Round Multi-Audio Benchmark for Evaluating Acoustic Degradation Perception in Large Audio-Language Models](https://arxiv.org/abs/2608.22236)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：MRMAD 是首个面向大音频语言模型（LALM）的多轮多音频声学退化感知评测基准，覆盖语音、音乐、声音三类域与九种常见退化类型，基于 8400 道多选题构建退化类型识别（DTI）、严重度比较（DSC）与排序（DSR）三大任务。针对现有基准过度聚焦语义理解而忽视低层音质判断的缺陷，采用"每轮一个音频对应一段提示"的多轮对话形式评测跨轮次比较与推理能力。对 18 个代表性LALM的系统评测显示：Gem
- **关键技术点**：现有基准（AIR-Bench、AudioBench、MMAU等）主要评测语义理解、事件识别与高层推理；QualiSpeech 虽接近低层感知但仅限语音且为单音频。真实音频常受背景噪声、混响、编码压缩等退化影响，判断退化是评估音质与决定恢复/增强的前提。多音频比较若拼接为单输入会引入时序定位这一混淆因素，故采用多轮多音频会话格式：每轮提供一段音频与对应文本提示，通过对话上下文完成比较。
- **主要指标**：- DTI：Gemini 3.1 Pro 86.22%；最佳开源 Qwen3-Omni-Thinking 36.58%，其余开源普遍贴近25%随机基线 - DSC：Gemini 3.1 Pro 90.81%；Qwen3-Omni-Thinking 60.70% - DSR：Gemini 3.1 Pr
- **代码**：https://github.com/Bose/MRMAD | **Demo**：暂无

---
## [Reasoning-Oriented Post-Training and Inference-Time LoRA Rescaling for Audio-Dependent Question Answering](https://arxiv.org/abs/2608.23092)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：针对 DCASE 2026 Task 5 ADQA 任务，本文提出结构化思维链（Structured CoT）后训练框架与推理时 LoRA 缩放机制，并在 Qwen2.5-Omni 与 MOSS-Audio-8B-Thinking 两个骨干上系统分析适配行为。Qwen 系统经 SFT+GRPO/GDPO 后 top-1 从基线 54.39% 提升至 58.93%，推理时将 LoRA 缩放因子降至 
- **关键技术点**：现有听觉问答基准存在语言先验泄露，模型替换音频为静音仍能答对部分题，无法证明真正基于音频推理。ADQA 通过 Audio-Dependency Filtering 筛选强音频依赖样本解决该问题，但答案级奖励不监督中间推理是否扎根于声学证据，可能产生未落地或退化的推理轨迹；且任务特定后训练并非对所有模型有益。
- **主要指标**：- Qwen-CoT：基线 55.38% → SFT 56.50% → GRPO 58.93%，γ=2 时 61.05% - Qwen-Structured-CoT：基线 54.39% → SFT 57.93% → GDPO 58.93%，γ=4 最优 - MOSS-Thinking-Full：零样
- **代码**：https://github.com/WeitengHu/DCASE2026-Task5 | **Demo**：暂无

---
## [AT-ADD: A Benchmark and Challenge for Robust and All-Type Audio Deepfake Detection](https://arxiv.org/abs/2608.23437)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：本文提出 AT-ADD 基准与 ACM Multimedia 2026 大挑战，针对现有 ADD 检测以语音为中心、忽略真实信道变化与多类型音频的问题，构建两大任务：Track1 为覆盖47个生成模型、11,299说话人、96种语言及噪声/混响/重放/压缩等扰动的鲁棒语音深伪检测；Track2 为语音、环境声、歌声、音乐四类音频在测试时类型未知条件下的全类型检测。官方最强基线 FT-XLSR-AA
- **关键技术点**：现有 ADD 基准（ASVspoof、ADD、SVDD等）以语音为中心且多在受控条件下评估，对压缩、噪声、混响、重放等真实信道变化鲁棒性差；对 ALLM 合成与 neural codec 等新范式及非语音音频类型泛化不足。AT-ADD 以渐进式双赛道弥合理想研究与真实多媒体取证之间的差距，全程采用闭合设置，仅允许使用官方 train/dev 数据。
- **主要指标**：- Macro-F1（Track1 Eval）：官方基线 FT-XLSR-AASIST 76.73%，冠军 WaveShield 90.71% - Macro-F1（Track2 Eval）：FT-XLSR-AASIST 79.47%（声音66.82%/唱歌96.30%），冠军 starfire 9
- **代码**：https://github.com/xieyuankun/AT-ADD-Baseline | **Demo**：https://at-add.com

---
## [SpeechGym: An Audio-Native Gym for Training Voice Agents via Reinforcement Learning](https://arxiv.org/abs/2608.26432)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-26
- **一句话贡献**：语音智能体必须完全通过语音调用工具、遵守领域策略并把多轮对话驱动到可验证的终态，但主流范式仍在文本中训练、在边缘拼接语音。现有方案要么在专有语音API外级联TTS/ASR（梯度不可回传、按次计费使在线RL不可行），要么停留在纯文本。论文提出SpeechGym，一个音频原生智能体环境：两个全模态模型用原生音频对话——冻结的用户模型扮演来电者，可训练的Thinker-Talker智能体在结构化工具调用
- **关键技术点**：语音智能体必须用语音完成文本智能体的一切动作，而主流做法在文本中训练策略、在边缘附加语音，假定文本能力能穿过音频回路而存活。τ-Voice将τ²-bench包进语音循环并报告了陡峭的文本到语音性能落差，却无法弥合：梯度无法穿过封闭API，且延迟与价格排除了在线RL所需的rollout规模（单epoch API成本超200美元，7轮超1400美元，千epoch接近20万美元）。全模态模型在架构上消解了级联，但只在无工具、无对话对象的单轮任务上做过RL。作者指出失败本质是感知缺陷而非推理缺陷：智能体选对了工具与参数槽，却把从波形中误听的数值填进去，该错误级联为调用失败、重复重试与步数预算浪费；另一
- **主要指标**：- 语音与纯文本差距诊断：槽值误听率语音32%对文本2%（16倍）；级联工具调用错误率42%。 - 训练配方有效性：携带梯度的rollout组比例从仅outcome GRPO的16%提升到加入逐轮过程奖励后的99.6%。 - 训练吞吐与成本：vLLM全模态rollout服务使单训练epoch加速5.
- **代码**：暂无 | **Demo**：暂无

---
## [TEMPO: Temporally-grounded Multi-task Post-training for Large Audio-Language Models](https://arxiv.org/abs/2608.29999)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-30
- **一句话贡献**：现有大音频语言模型（LALM）以片段级方式理解音频，无法为识别的事件、说话人或声音标注精确时间，严重限制其在多说话人字幕、密集音频描述等下游任务中的应用。本文提出 TEMPO，首个统一处理语音、声音与音乐三类时间戳任务的模型，其核心是三项创新的SFT阶段：原子时间戳token（0.0–60.0秒、0.1秒分辨率）、注入正弦壁钟编码的时间感知投影器，以及距离感知高斯损失，并采用合成到真实的课程式训练
- **关键技术点**：时间戳预测是LALM的关键短板，源自三大技术障碍：其一，BPE分词会将"12.3"拆成多token，破坏时间的数值序关系；其二，音频编码器产生的帧特征经投影器接入LLM时仅含相对位置编码，缺少绝对壁钟信息；其三，标准交叉熵对偏离0.1秒与偏离10秒的预测惩罚相同，与tIoU等评测指标严重不匹配。
- **主要指标**：- 多说话人ASR：WER 43.5%，平均IoU 65.8% - 说话人分离：说话人标注F1 56.3% - 对比基线：整体超越Audio Flamingo Next、Qwen3-Omni - 消融结论：SFT贡献主要性能提升，GRPO提供一致但温和的增量
- **代码**：https://github.com/kaousheik-26/tempo | **Demo**：暂无

---
## [Closing the Verification Loop: Self-Check Captioning for Long-Paragraph Detailed Audio Captioning](https://arxiv.org/abs/2608.30713)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-31
- **一句话贡献**：本文针对长段落、细粒度且与转写文本逐字对齐的详细音频字幕生成（long-paragraph detailed audio captioning）这一任务。现有视听多模态大语言模型因数据匮乏与生成模式失效两大结构性问题而失败，后者的证据是正确音频与打乱音频多选问答准确率存在44.8~46.4个百分点差距。作者提出自检字幕生成框架（SCC），将基于音频接地问答作为各生命周期阶段的验证原语，产出包含50
- **关键技术点**：长段落详细音频字幕生成要求对细粒度音频内容进行密集且忠实于转写的描述。现有视听大模型在该任务上失败源于两大结构性原因：一是数据贫困，公开语料无法同时提供长音频、段落级字幕与逐字转写保真度；二是生成模式失效，模型在"听错音频也能答对"的表现下产生幻觉式字幕。
- **主要指标**：- 正确音频 vs 打乱音频 MCQ准确率差距：44.8~46.4个百分点 - 平均字幕长度：491.5词 - 语料规模：50,222条视听片段 - 开源captioner对比：达到SOTA水平 - 闭源专有基线对比：竞争力相当
- **代码**：暂无 | **Demo**：暂无

---
## [Textual Acoustic Grounding for Generalizable LLM-Based Deepfake Voice Detection](https://arxiv.org/abs/2608.30622)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-31
- **一句话贡献**：针对深度伪造语音检测在未见域上泛化性能差的问题，本文提出一种基于文本化声学接地（Textual Acoustic Grounding）的ALLM检测框架。通过将Qwen LLM（0.5B-7B）与多种音频编码器结合，发现冻结LLM相比微调LLM在域外泛化上更具优势。进一步引入跨模态提示策略，将openSMILE提取的专家知识驱动声学特征以结构化文本令牌形式注入LLM，显式弥合模态鸿沟。在域外ITW
- **关键技术点**：现有ALLM将音频编码器输出的连续嵌入直接送入LLM，但连续音频嵌入携带的细粒度声学伪影细节与LLM的离散语义空间之间存在模态鸿沟，导致LLM难以有效利用声学线索进行真伪判别。此外，直接微调LLM会使其在训练域上过拟合，损害域外泛化能力。
- **主要指标**：- Macro-F1（域外ITW）：0.703，对比基线ALLM（0.541），绝对提升+16.2% - Macro-F1（域外MLAAD）：0.837，对比基线ALLM（0.603），绝对提升+23.4% - EER（域内ASVspoof 2019 LA）：0.84% - 冻结LLM（Qwen-1
- **代码**：https://huggingface.co/01Yassine/AudioLLM-Deepfake-Detection | **Demo**：暂无

---
## [Perceptible or Not? Diagnosing Passive Fingerprints for Speech Deepfake Attribution](https://arxiv.org/abs/2609.00765)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：被动指纹可用于深度伪造语音溯源，但其持久性、可复现性与内容无关性尚未被验证。本文提出可感知-不可感知被动指纹诊断协议（PIPDP），通过残差能量、可复现性、显著性分析等多证据验证，结合感知透明扰动与提示驱动情绪变化两类干预剖析两类指纹。在10个语音生成器与3个溯源检测器上，不可感知指纹能提供持久溯源线索；感知透明扰动使HiggsAudioV3上溯源准确率最高下降48.2%。
- **关键技术点**：深度伪造归因依赖生成器遗留的被动指纹，但指纹跨模型更新、跨内容的稳定性从未被系统验证。
- **主要指标**：- 感知透明扰动下HiggsAudioV3溯源准确率下降48.2% - CosyVoice2 + w2v-bert-MLP跨情绪波动仅约1.0%
- **代码**：暂无 | **Demo**：暂无

---
## [Heard but Not Heeded: Paralinguistic Information Encoding and Loss in Audio-Language Models](https://arxiv.org/abs/2609.00727)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：音频大模型能否真正捕捉"怎么说"而非仅"说什么"仍无定论。本文对Whisper-large-v2、Qwen2-Audio-7B、Qwen2.5-Omni-7B、Chroma-4B四个模型，在Expresso数据集受控说话风格下进行机制级分析。结合CKA、留一说话人线性探测、开放式音调预测与内容-韵律泄漏指标，追踪风格信息从编码器到输出的流动。结果所有模型在编码器后1/3层强烈编码说话风格，但在到达
- **关键技术点**：韵律、情绪等副语言信息对真实语音理解至关重要，但现有音频语言模型是否真正利用这些信息缺乏机制级证据。
- **主要指标**：- 所有模型在编码器后1/3层强编码说话风格 - 输出前风格信息一致衰减 - 泄漏指标区分内容驱动与声学驱动模型
- **代码**：暂无 | **Demo**：暂无

---
## [VoxReason: Listener-Free Evaluation of Source-Grounded Speech Planning Before Synthesis](https://arxiv.org/abs/2609.03203)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-09-02
- **一句话贡献**：表达性语音系统在合成前就决定情感、音高、能量、语速等，但这段隐藏的"说话计划"一旦编码进波形就难以审计，模型可能"听起来对但理由错了"。VoxReason把该决策升级为第一类可验证预测：输出带源引用的说话计划，由确定性验证器检查引用合法性、槽位一致性与反事实局部性。在1440条RAVDESS样本上，去掉源记录使7B模型引用必需分下降0.488；定位SFT+CF修复把计划槽准确率/反事实一致性从0.
- **关键技术点**：现有上下文感知TTS评估都只对最终波形或自由文本解释打分，很少暴露"哪条源记录授权了哪个交付字段"这一上游决策。作者主张把评分前移到合成之前，以受控干预检测源使用而非风格。
- **主要指标**：- 源通道消融：引用必需grounded分+0.488 - 7B SFT：证据F1 1.000、计划槽0.876±0.018、引用必需分0.944±0.008 - source-key不相交验证：乐观情感先验0.958槽准确率；定位SFT+CF达证据F1 1.000、槽0.919、反事实一致性1.0
- **代码**：https://github.com/MENGZHEGENG/voxreason | **Demo**：暂无

---
## [Is Semantics Enough for Speech Mean Opinion Score Prediction?](https://arxiv.org/abs/2609.03283)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：本文系统回答"语义表征是否足以支撑语音MOS预测"。对SSL模型、纯声学NAC、统一NAC三类表征进行首次大规模对比，在冻结编码器与全微调两种协议下于BVCC及两个OOD数据集上评测。"语义+声学"协同表征（尤其Xcodec-wavlm）在域内达最高上限（微调SRCC 0.882），而纯SSL在跨语言场景泛化更优（BC2019上wavlm_base零样本SRCC 0.674）。结论：语义不足够，需
- **关键技术点**：现有SOTA MOS预测器几乎都以SSL（Wav2Vec 2.0、HuBERT、WavLM）为特征骨干，其掩码预测预训练目标天然鼓励抽象高层语义、舍弃噪声与波形失真等声学细节，给自然度MOS预测施加表征上限。既往工作未在冻结编码器下探测表征固有信息含量，也未系统对比语义与声学两大范式。
- **主要指标**：- BVCC微调：Xcodec-wavlm最优SRCC 0.882（wavlm_base 0.875） - BVCC冻结：wavlm_base SRCC 0.863超纯语义SSL与纯声学NAC - SOMOS：统一NAC全胜（微调SpeechTokenizer SRCC 0.440） - BC201
- **代码**：暂无 | **Demo**：暂无

---
## [Tracing Audio Grounding and Answer Selection in Audio LLMs](https://arxiv.org/abs/2609.04637)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-09-04
- **一句话贡献**：音频大语言模型（Audio LLM）常依赖文本线索或语言先验答题而非真实听音，即便音频信息极度缺乏时仍能保持较高 AudioQA 准确率。现有应对方法用"无法仅凭文本作答"的数据训练，精度确有提升，但模型内部发生了什么改变仍不清晰。本文对 Qwen2-Audio 与 Qwen2.5-Omni 两个模型、在零样本（ZS）与 LoRA 微调（FT）状态下开展机制可解释性分析，回答"训练如何增强音频证据
- **关键技术点**：现有评测关注预测是否真正由声学证据支撑（幻觉、模态冲突、证据缺失），但已有研究指出模型可在几乎无声学证据时保持高 AudioQA 性能，说明基准精度与实际听音之间存鸿沟。机制层面工作虽已探究音频信息在模型中的表示与传播位置，却未说明训练如何改变音频信息最终驱动答案选择的过程。
- **主要指标**：- Qwen2-Audio ADQA：ZS 36.9%→FT 51.1%，ΔSaudio +9.3；MMAR 41.2%→52.5%，ΔSaudio +6.9 - Qwen2.5-Omni ADQA：41.9%→54.4%，ΔSaudio +4.5；MMAR 53.7%→65.7% - 两模型在 M
- **代码**：暂无 | **Demo**：暂无

---
## [Cleaner Speech, Weaker Generalization: Revisiting Pitt-Derived Benchmarks for Alzheimer's Disease Detection](https://arxiv.org/abs/2609.00276)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：基于语音的阿尔茨海默病（AD）检测日益依赖Pitt语料库的增强版本。本文系统重访预处理与数据整理对AD检测的副作用：增强数据集上域内性能提升但跨域稳健性下降；训练/测试匹配增强只能缓解无法消除退化。LALM同样敏感，增强数据诱发更强的类别不平衡与预测偏移。结论提示"更干净"的语音数据集对真实世界AD检测未必更可靠。
- **关键技术点**：AD语音检测常把语音增强、样本筛选等当作有利预处理，但这些转换可能在域内制造虚高成绩。
- **主要指标**：- 域内性能：增强数据集普遍提升 - 跨域/跨数据集：增强数据训练显著降低稳健性 - 匹配增强：可缓解但不能消除退化
- **代码**：暂无 | **Demo**：暂无

---
## [Does EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding](https://arxiv.org/abs/2607.27268)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-07-29
- **一句话贡献**：EEG基础模型（LaBraM在~2,500小时EEG上预训练，EEGMamba在~16,000小时上预训练）在运动imagery、癫痫检测、睡眠分期等任务上显著超越CNN基线，但其向语音解码的迁移效果尚未被系统验证。本文首次对EEG基础模型与卷积基线在语音解码任务上进行系统基准测试，覆盖overt、covert和imagined speech三种模式。在UGR-MINDVOICE数据集上，16K参
- **关键技术点**：EEG基础模型在运动imagery、癫痫检测等任务上表现优异，但语音解码涉及腹侧感觉运动皮层和颞上回的皮层动态，与基础模型预训练语料（静息态、运动imagery、临床事件）主导的范式有本质差异。现有研究仅在EEGMamba中将BCI Competition 2020 Track 3作为6个下游任务之一进行了评估，缺乏针对语音解码的受控比较。
- **主要指标**：- UGR-MINDVOICE语音模式（3类）：EEGNet 61.3% Acc / 0.607 W-F1，LaBraM 57.3% / 0.562，EEGMamba 56.6% / 0.553 - 语义类别（6类）：EEGNet 19.9% / 0.186，EEGMamba 19.3% / 0.1
- **代码**：暂无 | **Demo**：暂无

---
## [REIMU: Efficient Heterogeneous Hierarchical Reasoning for SSL-Based Speech Deepfake Detection](https://arxiv.org/abs/2608.00857)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-04
- **一句话贡献**：基于自监督学习（SSL）的语音深度伪造检测中，下游骨干网络通常通过单次前向处理SSL表示。本文系统研究循环层次推理对检测性能的影响，比较单次前向、权重共享循环、同质HRM和异构HRM四种架构。异构HRM在高层次模块使用MHSA（多头自注意力），低层次模块使用线性注意力（GDN2），在保持竞争力的同时减少10.8%的下游参数。代码开源。
- **关键技术点**：SSL模型（如WavLM、HuBERT）在语音deepfake检测中取得进展，但下游骨干网络的设计选择缺乏系统研究。单次前向（single forward pass）能否充分利用SSL表示的多层次信息？循环和层次推理是否带来提升？这些问题尚未被系统回答。
- **主要指标**：- 异构配置在多个设置下达到竞争力性能 - EER（等错误率）在19LA、21LA、21DF上表现优异 - 比匹配基线减少10.8%的下游参数 - 与单次前向基线相比，异构HRM在多个设置上取得改进
- **代码**：暂无 | **Demo**：暂无

---
## [LSEAD: A Privacy-Preserving LLM-Based Speech Analysis Framework for Early Alzheimer's Disease Screening](https://arxiv.org/abs/2608.07378)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-07
- **一句话贡献**：阿尔茨海默病（AD）早期诊断对及时干预至关重要。基于语音的筛查使用自然语音采集，无需专业设备。LSEAD 提出使用本地部署的开源 LLM（Zephyr-7B-β）提取语音转录文本 embedding，经 PCA 降维后使用逻辑回归分类。在 ADReSS20 和 ADReSSo2021 基准上，LLM embedding 跨数据集泛化良好，分类准确率提升高达 5%（达到 90.0%），尤其对早期阶段
- **关键技术点**：传统 AD 诊断依赖 MRI/PET 等资源密集型方法。基于语音的检测面临隐私挑战——商用 LLM（如 GPT-4）需要云端处理，不符合 HIPAA 合规要求。现有方法使用手工特征或浅层模型，泛化能力有限。
- **主要指标**：- 测试准确率：LR 90.0%, F1 89.7%, 精确率 91.2%, 召回率 88.1% - 对比：Mortensen et al. 84.9%, Bang et al. 83.1%, Agbavor et al. 80.3% - 早期检测：正确分类 AD 的 MMSE 均值 19.4±7.
- **代码**：https://github.com/kelci2017/AD_Text_LLMs | **Demo**：暂无

---
## [MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection](https://arxiv.org/abs/2608.09593)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：语音合成和音频生成的最新进展使得高保真声学伪造低成本且难以归因，实现了语音和背景音频可被独立操纵的现实攻击场景。但现有研究要么关注视觉操纵，要么孤立处理语音检测，或将语音和非语音音频混为一谈。MADBench 是首个将语音和环境音频视为不同声学组件的基准，支持组件感知的音频深度伪造检测评估。实验揭示：环境音频操纵比合成语音更容易被通用编码器检测；现有预训练检测器对两种声学组件均失败；操纵环境音频不
- **关键技术点**：真实攻击场景中，攻击者可独立操纵视频中的语音轨道和背景音频，但现有检测基准将语音和背景音频视为单一标签，忽视了两者不同的伪造特征和检测难度。
- **主要指标**：- 环境音频操纵比合成语音更容易被检测 - 现有预训练检测器在两种声学组件上均失败 - 操纵环境音频不对称地降低语音检测性能
- **代码**：暂无 | **Demo**：暂无

---
## [AudioMap: Cloze-and-Choice Reinforcement Learning for Time-Aware Dense Audio Captioning](https://arxiv.org/abs/2608.09559)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：时间感知密集音频描述（TDAC）旨在生成具有精确时间边界的多个细粒度音频属性。现有方法主要依赖监督微调，性能次优。AudioMap 提出基于填空-选择强化学习（RL）的 TDAC 框架，引入证据充分性奖励（ESR）的不对称分层评分机制以提高细粒度准确性和描述丰富性，以及事件条件时间奖励（ECTR）通过时间 IoU 将时间戳绑定到事件语义。构建首个时间感知细粒度音频描述数据集 AudioMapCap
- **关键技术点**：TDAC 需要同时生成细粒度多属性描述和精确时间边界，现有监督微调方法难以优化两个目标。现有奖励函数过于粗糙，无法细粒度监督多事件、多属性、多关系描述；自由格式 caption 的时间监督困难。
- **主要指标**：- 开源模型中 SOTA - 与闭源模型竞争或更优
- **代码**：https://github.com/ryysayhi/AudioMap | **Demo**：暂无

---
## [DuplexWorld: Can Voice Agents Help You Get Through the Day?](https://arxiv.org/abs/2608.10716)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-11
- **一句话贡献**：语音到语音（S2S）语音代理越来越多地集成到企业中用于客户服务和日常陪伴。DuplexWorld 引入六个世界（银行、保险、旅行、医疗保健、物流和路径规划），共 156 个场景和 350+ 小时对话，全面评估语音代理的代理能力、对话能力和语音自然度。评估显示即使最佳语音代理在三方面仍有巨大提升空间：Pass@1 仅 0.490，轮次切换 0.653，DNSMOS 3.378。
- **关键技术点**：现有语音代理基准主要测试代理工具调用能力，未充分覆盖日常活动的对话多样性，也未测试代理在数据库操作之外的多步骤任务协助能力。
- **主要指标**：- 最佳代理：Pass@1 0.490，轮次切换 0.653，DNSMOS 3.378 - 各世界和对话类型性能差异显著 - 路径规划场景中探索-利用权衡分析揭示代理失效模式
- **代码**：暂无 | **Demo**：暂无

---
## [DINO-A: Adapting Self-Distillation Vision Transformers to General Audio Representation Learning](https://arxiv.org/abs/2608.10659)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-11
- **一句话贡献**：DINO-A 将视觉自蒸馏方法 DINO 适配到通用音频表示学习。保留 DINO 的多裁剪、EMA 教师和高维投影，仅将输入模态和增强替换为 log-mel 频谱图和 BYOL-A v2 增强块。在 FSD50K 上预训练三种骨干（ViT 8×8, ViT 16×16, 卷积编码器），在 ESC-50、Speech Commands v2、UrbanSound8K 和 GTZAN 上用线性探测评估
- **关键技术点**：DINO 已成为视觉自监督学习的标准方法，但之前没有工作将标准 DINO 以 BYOL-A 将 BYOL 带到音频的方式系统性地适配到通用音频分类。
- **主要指标**：- ViT-S/8 在所有任务上优于 ViT-S/16 - 卷积网络在语音任务上优于 ViT，ViT 在环境和音乐上领先 - DINO-A vs BYOL-A v2：平均差距 11.96 个百分点 - 主要原因：高维投影空间在 FSD50K 规模下导致过拟合
- **代码**：暂无 | **Demo**：暂无

---
## [In Defense of Using Worst-case Privacy Disclosure as Privacy Evaluation Metric of Voice Anonymization](https://arxiv.org/abs/2608.10318)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-11
- **一句话贡献**：语音匿名化社区主要使用 EER 评估语音身份保护性能，但 EER 最优系统在 LLR 空间中可能无法正确评估信息泄漏。该论文为 privacy-ZEBRA 框架（最坏情况隐私泄露评估）进行辩护，基于 Shannon 完美保密概念解释 EER 的局限性，展示基于排名的指标如何等价于完美保密原则。在模拟数据和 VoicePrivacy Challenge 数据上展示结果，为语音匿名化评估提供理论指导。
- **关键技术点**：语音匿名化主要使用 EER（等错误率）评估隐私保护，但 EER 衡量的是平均性能，可能掩盖单个说话人的信息泄露。privacy-ZEBRA 框架提出最坏情况评估，但其理论基础和与其他指标的关系尚未被充分解释。
- **主要指标**：- EER 最优系统在 LLR 空间可能无法正确评估信息泄漏 - 基于排名的指标等价于完美保密原则 - LLR 估计方法对评估结果有显著影响
- **代码**：https://github.com/nii-yamagishilab/paper-archive-spsc2026-privacy-llr | **Demo**：暂无

---
## [Infant Audio Understanding via Whisper + LoRA](https://arxiv.org/abs/2608.11587)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-12
- **一句话贡献**：本文提出基于Whisper encoder + LoRA微调的方法，用于婴儿中心音频理解任务（如婴儿哭声检测、情感状态分类等）。创新性地设计了因子化说话人token机制，将共享层级token与家族特定偏移结合，实现跨家族的婴儿音频理解。采用多层级音频标记和序列级平滑损失函数来提升模型性能。
- **关键技术点**：婴儿音频理解面临数据稀缺和跨个体泛化两大挑战：婴儿音频数据收集困难且标注成本高，不同婴儿的发声特征差异巨大，导致模型在未见过的婴儿上性能显著下降。
- **主要指标**：待论文全文确认具体数值
- **代码**：暂无 | **Demo**：暂无

---
## [CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model](https://arxiv.org/abs/2608.13101)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-13
- **一句话贡献**：自动口语评估（ASA）需要同时评估语音表达（怎么说）和内容（说什么），现有语音 LLM 方法依赖大规模多模态骨干网络，计算开销大且缺乏对声学/内容信息贡献的分离分析。CASA 提出双分支架构，将 Whisper-medium 编码器（声学分支，LoRA 适配）与 Qwen3.5-2B（内容分支）结合，在 Speak & Improve Corpus 2025 上以 3.13B 总参数量（约 NTN
- **关键技术点**：口语评估中语音表达（流利度、发音）和内容（词汇、语法、主题发展）是多源交互的证据，现有方法要么使用大参数语音 LLM 但计算开销大且缺乏可解释性，要么依赖多 grader 组合和手工特征增加系统复杂度。现有实现均未开源，限制了可重复性和进一步研究。
- **主要指标**：- RMSE 0.358（SOTA 对比：NTNU 0.360，Perezoso 0.364） - PCC 0.829，%≤0.5 达 84.7%，%≤1.0 达 98.7% - 总参数 3.13B（NTNU 约 6.24B 的一半） - 10 次重复运行平均 RMSE 0.363 [95% CI:
- **代码**：https://github.com/aalto-speech/casa | **Demo**：暂无

---
## [Measuring Fairness in Large Audio Language Models via Semantic-Aware Bias Estimation](https://arxiv.org/abs/2608.13624)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-17
- **一句话贡献**：大音频语言模型（LALM）在语音识别和音频问答等任务中广泛应用，但其跨人口子组的公平性评估面临语义混杂和说话人特性相关的混淆因素挑战。现有方法未考虑不同子组间语音内容的语义难度差异，导致虚假公平性结论。本文提出一种语义感知混合效应回归框架，将参考文本的句子级语义嵌入作为协变量，说话人身份作为随机效应，从而在公平性评估中显式控制语义和说话人混杂。在模拟实验中，传统方法将性别间分数比错误估计为1.12
- **关键技术点**：LALM在语音输入场景下，不同人口子组（如性别）的语音内容在语义复杂度上可能存在系统性差异。例如，某一性别群体的语音可能包含更多语义密集或难度更高的内容。此外，同一说话人的多个话语之间存在相关性。如果这些因素在公平性评估中不加控制，会导致模型偏差被高估或误判。现有方法（如Liu et al., ICASSP 2022）针对传统ASR系统提出了基于混合效应的统计框架，但依赖外部语义表示（如fastText、BERT），且未覆盖LALM场景。本文首次针对LALM场景提出语义感知公平性评估框架。
- **主要指标**：- 模拟数据（性别分数比）：Vanilla估计1.124（假阳性）-> 语义感知Embed-AGG 1.003（正确阴性） - LibriSpeech Test-Clean（WER性别比）：Vanilla 0.719（显著）-> 语义感知Embed-AGG 0.802（不显著） - LibriSpe
- **代码**：暂无 | **Demo**：暂无

---
## [EXAM$^2$: Extending Audio Understanding in Multilingual and Multimodal Analysis](https://arxiv.org/abs/2608.23758)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：本文提出多语言多模态音频理解基准 EXAM²，系统评估现有音频语言模型在多语言、多模态理解上的表现，发现模型存在明显的多语言跨模态理解差距。作者进一步构建微调的 Gemma3n-EXAM² 模型，其性能较基线显著提升，为多语言音频理解研究提供了新的评测工具与改进方向。核心价值在于填补了现有基准对非英语语言与多模态结合场景覆盖不足的空白。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [GRGA: Graph-based Retrieval-Generation Agent for Long-form Audio Meeting Understanding](https://arxiv.org/abs/2608.24048)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：针对长音频会议理解任务中问答数据集稀缺、现有语音模型声学信息丢失与长期记忆能力差的问题，本文构建了 LongAudioQA 数据集，并提出基于图的检索-生成智能体（GRGA）。GRGA 利用智能体规划实现检索与答案生成，将语义信息组织为图结构以缓解长期记忆与信息丢失问题。该工作已被 ACL Findings 2026 接收，为长会议场景下的语音理解提供了新的数据资源与建模范式。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [AudioSpan: Spanning the Duration and Depth of Audio Comprehension](https://arxiv.org/abs/2608.26431)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：现有音频理解基准大多在数秒级短片段上评测，得分快速饱和；近期长音频类基准虽把时长拉长，评测方式却仍沿用短音频的抽取式问答，未触及认知深度。本文提出AudioSpan：将音频时长从10分钟跨度到2小时以上，配套3,240道题，划分为知觉、理解、推理三个认知层级。题目由两条路径生成——Native QA从音频真实内容取材，每道题同时给出四选一选择题和按详细评分表打分的开放题；Anchor QA则向音频
- **关键技术点**：现有基准（秒级剪辑QA）上分数饱和、模型趋同，说明短片段测试已丧失区分度；近期长改工作虽在时长上突破，评测仍按"把长音频当短音频"的抽取式问答处理，既没有覆盖跨数小时的完整内容流，也没有触及深于事实检索的认知层次。同时LALM正走向多模态（语音、声音、音乐全覆盖），训练目标与评测方式脱节。AudioSpan同时扩展"时长"与"认知深度"两个轴：时长轴检验长上下文能力，深度轴检验从简单感知到复杂推理的认知全过程。
- **主要指标**：- 评测广度：12个大音频语言模型参与基准评测，覆盖不同架构与参数量。 - 核心发现：模型的首要瓶颈在推理之前——从冗长且高冗余的长音频中提炼少量关键相关事实最困难，即"困难发生在前置的检索/提炼环节"。 - 难度随时长增长：音频越长模型表现越差，时长维度对分数有系统性影响，不再像短片段基准那样饱和
- **代码**：https://huggingface.co/datasets/holvan/AudioSpan | **Demo**：暂无

---
## [A Training-Free Proactive Defense Against Partial Speech Manipulation via Self-Embedding Steganography](https://arxiv.org/abs/2608.25285)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：部分（局部）语音被替换、拼接式的深度伪造难以被整段检测器捕获。本文提出一种无需训练的主动防御方法，将自嵌入策略与现有音频隐写术结合，在待保护语音中内嵌自身摘要，解码器据此修复被操纵区域从而实现操纵检测。该方法无需重新训练模型、数据效率高，可与被动检测互补。已被 Interspeech 2026 接收。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [SURE-Challenge: Evaluating Speech Evidence Before Speech-LLM Generation](https://arxiv.org/abs/2608.27783)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：现有语音大模型评测均为回答后打分，但部署时操作系统需在生成前决定一段波形是否值得送入模型。本文定义SURE-Challenge，将"语音证据准入"作为独立评测环节：前端在模型推理前判断输入是否包含足以支撑回答的语音证据，否则拒绝调用。基准基于LibriSpeech构建转写与首词问答两类受支持样本，配合静音、彩色噪声、合成音调与源歧义混叠四类不支持样本，采用源不相交划分。采用Qwen2-Audio做
- **关键技术点**：论文指出语音大模型评测的盲区：答案评分发生在生成之后，但对不支持输入（纯背景声、音乐、合成音、未指明来源的人声）生成流畅答案本身就不安全。操作决策是语音证据过滤——给定音频与提示，前端决定准入或弃权，仅在准入后调用大模型。作者强调识别性不等于来源可支持性：说话人无法与提示匹配的清晰语音同样应被拒绝，这是现有工具（VAD、ASR置信度、AudioSet标签器）无法解决的。
- **主要指标**：- 裸Qwen2-Audio不支持拒绝率仅0.074（15/204），固定规则提升至0.961（196/204），受支持准确率0.930不变，下游调用减41%。 - 六骨干上主规则重放均达SURE R.=0.961，受支持准确率0.919-0.970。 - 前端对照：Silero 0.735、AST
- **代码**：https://github.com/MENGZHEGENG/sure-challenge | **Demo**：暂无

---
## [When Text Misleads: Inconsistent-Aware Reasoning for Audio-Grounded Dialogue](https://arxiv.org/abs/2608.27176)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：本文针对语音对话理解中的隐藏失败模式——模型仅凭转写文本即可作答，并未真正把预测建立在语音声学证据上（模态塌缩）。作者将文本与声学线索相矛盾的场景形式化为跨模态不一致，并据此构建受控评测基准ContraTalk，包含501道多选题，覆盖互动行为、情绪状态、对话行为、社会立场和会话意图五个话语维度，其中333道冲突题与168道一致题。同时提出代理式推理框架Audio Twin，将语音转写对齐的声学线
- **关键技术点**：当前多模态评测普遍允许模态捷径：在VQA和对话情绪识别中已有"语言先验主导"的共识，近期语音语言模型研究也常出现仅凭词汇或数据集先验即获高分的现象。当基准可仅由单模态求解时，另一模态在功能上可被忽略，导致模态塌缩。现有基准大多评估模态"协同/互补"情形，几乎没有把"解决显式跨模态冲突"作为推理前提，因此作者将跨模态不一致定义为一条独立且未充分探索的评测轴。仅靠隐式多模态融合不够，模型需自行判定转写推理是否充分、定位相关声学证据并在文本与语音分歧时比较竞争解释。
- **主要指标**：- 冲突题准确率：文本LLM为33.0%-47.7%；直接Audio-LLM为33.6%-46.8%；Audio Twin推理为43.2%-50.5%（Sonnet 4.5+AT最佳50.5%）。 - 冲突题误导率：文本LLM达34.5%-45.0%；Audio-LLM仍有29.7%-39.9%；A
- **代码**：暂无 | **Demo**：暂无

---
## [Direct or Mediated? Task-Dependent Audio Information Routing in Large Audio Language Models](https://arxiv.org/abs/2608.27026)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：论文针对大型音频语言模型通常在单一连贯音频段上评估、在非熟悉输入配置下行为未知的问题，设计了将两段音频在波形层面拼接为单输入（中间不插入静音或边界标记）的受控设置。在Audio-Flamingo-Next、MiMo-Audio、Step-Audio-R1、Qwen3-Omni四个LALM上发现一致的任务依赖健壮性差距：ASR相对稳定（WER仅上升0.10-1.30个百分点），而AQA显著退化（拼接
- **关键技术点**：现有LALM（如Qwen3-Omni、Audio-Flamingo-Next）在基准测评中表现优异，但已有工作表明模型在输入偏离熟悉分布时存在音频接地不足与幻觉。多数研究仅在行为层面构建基准刻画失败，缺乏对内部机制的剖析。ASR只需恢复语言内容，AQA还需识别证据、保持属性并按问题检索，两者信息需求存在本质差异，但同一解码器内部是否采用不同路由机制此前未知。作者以受控双段拼接暴露这一差异，再用因果干预与表达性分析追踪机制。
- **主要指标**：- 拼接ASR仅小幅退化：跨四个模型WER上升0.10-1.30个百分点且均低于4.5%，如Audio-Flamingo-Next的WER 1.68%->1.86%。 - AQA单段对照为85.17%-98.00%，拼接后Audio-Flamingo-Next降至35.33%-54.33%，MiMo
- **代码**：暂无 | **Demo**：暂无

---
## [Mapping Written Words to Spoken Words in a Different Language Using Only Visual Grounding](https://arxiv.org/abs/2608.26925)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：针对低资源语言连语音采集都很困难的现状，本文研究如何仅凭视觉grounding（图像配印地语口语描述）将英文书面关键词映射到印地语语音中对应的词段，全程无需目标语言转录、无需训练任何神经网络。方法把无监督词发现与视觉监督结合：用现成的图像描述系统自动生成英文caption作为弱文本监督，据此把话语划分为正/负两类，再基于HuBERT自监督表征进行对齐，并通过interval piling聚合、减去
- **关键技术点**：世界上绝大多数语言缺乏文本资源和书写系统，难以构建传统语音技术。项目Vaani正通过让说话人描述图像来采集语音，但此类视觉grounding数据缺乏语音-文字对应关系。此前工作用单一图像tagger为注意力式音频-关键词神经网络提供弱监督，关键词种类固定且限定在单个tagger的输出域，分段也不精确。本文希望动态构建与语料相关的词表，仅利用无监督词发现思路，把印地语口语词段与英文书面词建立跨语言映射，支撑语言记录与保护。
- **主要指标**：- 跨语言视觉grounding主结果：CFA正负例 定位49.9% / spotting 63.0%；CFA仅正例 23.6% / 47.7%；DFA正负例 34.2% / 56.8%。 - 对照基线：注意力CNN（Olaleye等）定位10.4% / spotting 18.8%，CFA正负例相
- **代码**：https://github.com/gabitza-tech/vgs-cl-vocab | **Demo**：暂无

---
## [Auditing Generative Audio Calls for Known-Task Audio-LLM Evaluation](https://arxiv.org/abs/2608.27817)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：针对"波形输入是否优于ASR文本"这一常见音频LLM评测方式，论文指出它混淆了两个因素：模型是否获得声学证据，以及结论是否依赖于调用生成式音频模型。为此论文提出受控的"生成式调用决策测试"：对每个样本，策略在保留文本标签、使用本地编码器（CLAP/AST/WavLM）证据、调用生成模型（Qwen2-Audio/Qwen2.5-Omni/MOSS-Audio）三者间做路由，关键消融在固定选择器与开发
- **关键技术点**：常见评测将音频LLM输出与纯文本预测对比，只能证明波形含有效证据，却无法回答"是否必须以生成式音频模型才能利用该证据"。部署端在闭集任务中面临三选一路由：保留文本侧标签、用本地编码器打分发（成本与隐私支出低）、把波形送给托管生成模型（增加成本并暴露语音数据）。已有基准（SUPERB、Dynamic-SUPERB、VoiceBench等）主要测模型能力，本文反其道而行：固定已知任务，用文本侧与编码器控制问清"生成调用是否仍能改变决策"。
- **主要指标**：- VocalSound上文本基线0.296，Qwen2.5-Omni 0.883、Qwen2-Audio 0.838、MOSS-Audio 0.808、零样本CLAP 0.762。 - 零生成调用的受监督编码器控制已逼近上限：WavLM-base+ 0.854、CLAP嵌入探针0.850、联合CL
- **代码**：暂无 | **Demo**：暂无

---
## [A Shaky Voice Is Not Always a Dodge: Benchmarking Textual and Vocal Evasion Detection in Earnings Calls](https://arxiv.org/abs/2608.28040)

- **方向**：语音大模型 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：现有财报电话会中的"答非所问"检测仅依赖转写文本，把规避行为当作单一维度现象。本文认为口语交流中的规避本质上是多维度的：高管"说什么"与"怎么说"携带相互独立且互补的信息（两类标签弱相关，32.1%的样本出现跨模态不一致）。为此构造了首个带独立文本+语音双重标签的基准DualEvasion，含60场电话会、505个Q&A问答对，分别标注文本规避（直接/规避）与声学置信度（自信/不自信）。实验表明：
- **关键技术点**：现有研究（SubjECTive-QA、EvasionBench等）均将规避检测建模为纯文本分类任务，忽略了语音通道。作者用填充停顿、犹豫、语调等韵律线索将"怎么说"操作化为说话人置信度，指出关键难点是说话人依赖性：同一声学表现对不同高管意义不同，必须做说话人感知评估。此前的语音前端研究为音频级建模提供了基础，但尚无工作把文本规避与声学置信度联合建模。
- **主要指标**：- 文本规避宏F1：GPT-5达87.4（accuracy 89.5），已接近人类水平。 - 语音置信度宏F1：最佳模型GPT-Audio仅58.5（不自信F1 38.2），Audio-Flamingo-3 51.7/30.8、Qwen2-Audio 28.0/36.2。 - 不自信类F1整体仅30
- **代码**：暂无 | **Demo**：暂无

---
## [Beyond Speech: Dual-Domain SSL Fusion for Unified All-Type Audio Deepfake Detection](https://arxiv.org/abs/2608.29021)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：7/10 | **日期**：2026-08-29
- **一句话贡献**：本文针对输入音频类型未知（语音、环境音、歌声、音乐四类）的统一全类型音频深度伪造检测问题，提出双域SSL融合框架。以EAT-large与wav2vec 2.0 XLS-R-300M为互补前端，通过逐层加权融合与token级拼接消除帧级对齐需求，经多头注意力统计池化聚合、二分类MLP头判别，并在其上叠加保守语音精炼。在AT-ADD Track 2评测集上核心双域模型达94.44% Macro-F1，
- **关键技术点**：现有音频深度伪造检测主要集中于语音，依赖音素、说话人等语音专属线索，而当前生成模型可产出音乐、歌声与环境音，待测类别未知且只需二分类输出。不同域伪影形式差异大，现有类型相关方案难以泛化。
- **主要指标**：- 核心双域模型Macro-F1：94.44% - 加入语音精炼后Macro-F1：95.58% - 挑战赛排名：第二名
- **代码**：暂无 | **Demo**：暂无

---
## [Perceptually Better, Semantically Worse: Measuring Speech Enhancement Impact on LLM-Based Voice Systems](https://arxiv.org/abs/2608.30348)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：语音增强（SE）常作为语音AI流水线的预处理模块，其隐含假设是提升音频质量可改善下游任务表现。本文提出输出发散率（ODR），量化SE处理相对于干净语音改变LLM意图分类结果的频率，并在2,974条SLURP音频、五种条件及Whisper large-v3与wav2vec2-large串联系统上验证。结果显示所有条件下ODR均显著大于零（p<0.001），MetricGAN+虽改善PESQ却使ODR
- **关键技术点**：
- **主要指标**：- ODR：未增强加噪0.135，MetricGAN+增强0.318，未处理回声0.836 - PESQ与ODR相关性：ρ=-0.467（中等负相关） - 跨架构复现：Whisper large-v3和wav2vec2-large下表现一致
- **代码**：暂无 | **Demo**：暂无

---
## [SISER: Speaker-Invariant Speech Emotion Recognition with Entropy-Based Adversarial Training](https://arxiv.org/abs/2609.02941)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：针对SER中标注数据稀缺与说话人差异两大痛点，提出SISER框架，将wav2vec 2.0作为特征编码器、ECAPA-TDNN作为说话人判别器，融入基于熵最大化的对抗训练。在IEMOCAP说话人独立10折交叉验证下取得测试集UA 60.63%（WA 58.53%），相比复现基线（51.15%）提升9.48%，超越无对抗的wav2vec 2.0系统（56.46%）。
- **关键技术点**：语音中音素、说话人特性与情感状态在声学层面深度交织，SER模型在说话人独立设置下易学到说话人特有相关关系导致泛化退化。先验工作将熵最大化用于对抗解耦，但其CNN+GRU编码器与浅层FC判别器未能利用强预训练表示，弱判别器无法对残留说话人维度施压。
- **主要指标**：- SISER测试UA/WA：60.63%/58.53% - 无增强复现基线UA 51.15%；wav2vec 2.0无对抗UA 56.46% - 消融：FC→ECAPA在wav2vec 2.0上+6.49%（56.24→62.73）
- **代码**：https://github.com/slp-lab-research/siser.git | **Demo**：暂无

---
## [A Unified Uncertainty-Aware Back-End for Speaker Verification: Scoring, Normalization, and Calibration](https://arxiv.org/abs/2609.01221)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：7/10 | **日期**：2026-09-01
- **一句话贡献**：说话人验证（SV）后端通常组合相似度打分、分数归一化与校准，但说话人嵌入置信度随时长、噪声、信道而变化。现有不确定性感知方法多只改进编码器，不确定度未贯穿归一化与校准。本文将每条语音表示为"后验均值+协方差"，提出统一不确定性感知后端：UIA-cosine打分、UAS-Norm与UQMF校准。ECAPA-TDNN与ResNet上EER一致下降。
- **关键技术点**：SV传统后端假设每条试听可靠性相同；短语音、噪声使某些嵌入天然不可靠。
- **主要指标**：- EER：两架构下均一致下降 - 目标-非目标分离度：均改善
- **代码**：暂无 | **Demo**：暂无

---
## [Removing Speech, Keeping Activities: A Privacy Firewall for Acoustic Sensing in Assisted Living](https://arxiv.org/abs/2609.02376)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-09-02
- **一句话贡献**：为解决辅助生活环境中声学感知系统采集日常活动声时泄露居民言语内容的隐私问题，本文提出"隐私防火墙"流水线：卷积 U-Net 编解码器在 log-mel 频谱域去除语音分量、保留环境活动声，全程仅用合成数据训练；下游活动识别采用 VGGish+SVM 迁移学习。在 ESC-50 和 SINS 上所有语音电平下残言语音均降为 0% VAD 可检测（Silero），ESC-50 40% 语音电平下精确率
- **关键技术点**：声学感知能非侵入监测老人日常活动，但居民与护理人员最担忧系统录制私人对话。ADAPTIVE 养老院部署中采用 VAD 触发静音捕获，遇广播语音频繁误触发导致大量活动信号丢失；且真实部署数据标注昂贵、收集窗口短，需契合实际工业部署约束（ADAPTIVE 项目经验启发）。
- **主要指标**：- ESC-50 40% 语音电平去去除后精确率/召回率：85%/85%（无语音基线 84%/83%，语音污染时 81%/75%） - VAD 可检测语音：ESC-50 100% 语音电平由 67.5% 降至 0%；SINS 各电平均为 0% - 现成模型对比（ESC-50 100% 语音，残余 V
- **代码**：暂无 | **Demo**：暂无

---
