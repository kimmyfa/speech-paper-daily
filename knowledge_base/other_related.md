# OTHER RELATED（按评分降序）

共 123 篇

## [Autoregressive Guidance of Deep Spatially Selective Filters using Bayesian Tracking for Efficient Extraction of Moving Speakers](https://arxiv.org/abs/2603.23723)

- **方向**：语音前端 | **子方向**：Other | **评分**：9/10 | **日期**：2026-03-24
- **一句话贡献**：针对移动说话人的弱引导目标说话人提取（TSE），作者在因果逐帧处理框架下将上一步增强信号自回归（AR）地融入轻量级贝叶斯跟踪器，提出两种策略：MISO-AR 将增强单通道信号作为额外观测量加入贝叶斯滤波，MIMO-AR 将深度空间选择性滤波器（SSF）扩展为多通道输出并用增强多通道估计替换带噪观测。结合基于社会力模型生成的新型合成数据集与真实录音，在计算开销几乎不变的前提下显著提升 DoA 跟踪精
- **关键技术点**：深度空间选择性滤波器（SSF）对方向已知的静止说话人可实时高质量增强；但连续 DoA 信息通常不可得，移动说话人场景需依赖仅初始方位（弱引导）+跟踪算法。现有神经跟踪器精度高但计算量大，轻量统计算法（KF/PF 的 Concat 串联式）在难声学条件下精度不足。
- **主要指标**：- ACC(10°)/MAE：MISO-AR PF 87.6%/6.47°（最优）；MIMO-AR WKF 86.4%/6.65°；Concat WKF 33.2%/32.67° - PESQ/ESTOI：Oracle 2.14/81.6%；MISO-AR PF 2.04/80.4% - MISO-
- **代码**：https://github.com/sp-uhh/autoregressive-spatial-filters | **Demo**：https://sp-uhh.github.io/autoregressive-spatial-filters/

---
## [Anomalous Sound Detection Meets Noise-Aware Self-Supervised Learning](https://arxiv.org/abs/2608.00447)

- **方向**：语音前端 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：异常声音检测（ASD）在工业设备监控中至关重要，但实际工厂环境中的背景噪声严重干扰检测性能。本文提出噪声感知自监督学习（NA-SSL），利用双麦克风录音设置（近场麦克风靠近目标机器，远场麦克风捕捉噪声），训练NA-SSL模型从含噪信号中提取干净表示。使用FSD50K（目标声音）+ WHAM!/DEMAND/QUT-NOISE（噪声）模拟双通道录音。在DCASE 2026 Challenge Tas
- **关键技术点**：工业ASD需要在工厂环境中检测机器异常声音，但严重背景噪声导致标准ASD方法性能大幅下降。DCASE 2026 Challenge Task 2首次引入噪声感知ASD（NA-ASD）任务，提供双麦克风录音：近场（靠近机器，目标信号主导）和远场（远离机器，噪声主导）。挑战在于如何利用远场噪声信息辅助近场信号的干净表示学习。
- **主要指标**：- NA-BEATs官方评估得分: 70.24%（排名第一） - 第二名: 65.46% - 官方基线: 59.80% - NA-EAT和NA-Dasheng也显著优于基线
- **代码**：暂无 | **Demo**：暂无

---
## [SoniSpeech: Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces](https://arxiv.org/abs/2608.00803)

- **方向**：语音前端 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：无声语音接口（SSI）允许用户在不发出声音的情况下与设备交互，但受限于小词汇量数据集。本文提出SoniSpeech，首个大规模开放词汇可穿戴无声语音接口三模态数据集，包含34小时、18000个话语，三个同步模态：超声回波profile（通过声学传感眼镜捕获面部运动）、有声音频和前视视频。语料来自SODA对话数据集，包含5356个唯一词汇和完整音素覆盖。CTC ResNet-34基线在纯无声模式下W
- **关键技术点**：无声语音接口允许用户在安静环境下（如图书馆、会议室）或隐私敏感场景下与设备交互。现有研究受限于小词汇量（通常<100词）和封闭词汇集，缺乏大规模开放词汇的基准数据集。可穿戴硬件如面部电极（EMG）虽然精度高但佩戴不便。
- **主要指标**：- 纯无声训练：WER 33.7%（首次开放词汇SSI基准） - 有声+无声联合训练：WER 26.3%（相对改善22%） - 训练数据规模效应：数据量从25%到100%增加，WER持续下降，说明数据规模仍有扩展空间 - 模态比较：超声回波>视频>音频（无声模式下）
- **代码**：暂无 | **Demo**：暂无

---
## [Language Orthogonalization of Self-Supervised Speech Representations for Cross-lingual Parkinson's Detection](https://arxiv.org/abs/2609.09499)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-09-08
- **一句话贡献**：自监督语音模型（S3M）表示中混杂的语种信息会扰乱跨语种帕金森病（PD）检测：当目标语言仅有健康对照（HC）语音时，分类器会学会区分语种而非病理，导致高特异/低敏感。本文提出语种正交化（LO）——仅用HC语音拟合S3M特征对外部VoxLingua107语种嵌入的闭式岭回归残差化。实验表明，在5个S3M骨干、3种语音任务、3种目标语言上，该方法将F1均值从0.52/0.67提升至0.87，并实现敏感
- **关键技术点**：大多数语音化PD检测系统仅限单语种/单语料评估，而跨语种检测需区分可迁移的病理信号与语种特有变化。S3M同时编码强大的语种结构；当训练集只含源语种患者与目标语种HC时，分类器将目标语种与HC关联，导致目标语种患者被漏检（高特异、低敏感）。已有基线 Language Shift（LS）仅将各语种HC质心对齐为常向量，不改变组内协方差，无法去除质心之外的语种依赖结构。
- **主要指标**：- 敏感度0.90工作点F1均值（5骨干×3任务×3目标语种×5折）：Raw 0.52 → LS 0.67 → LO 0.87（+0.35）；分任务：Vowel 0.53/0.65/0.89、DDK 0.59/0.68/0.90、Read 0.43/0.69/0.81 - 语种可解码性三语分类mac
- **代码**：https://github.com/MINUKIMS/language-orthogonalization | **Demo**：暂无

---
## [Jarvis: Coordination Deserves a Brain of Its Own in Agentic Interactive Models](https://arxiv.org/abs/2610.23804)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-10-19
- **一句话贡献**：全双工语音模型把复杂推理外包给后台慢脑，任务运行时用户可随时细化、取消或替换请求，计划与结果随之过期，而前台只跟对话、后台只知自身任务，无人同时看到两边。论文提出协调框架Jarvis，遵循"模型判断、代码执行"：类型化决策模型JEV把每轮话语对照活动任务台账选操作，运行时校验版本后才生效。同前后端的受控对比下，τ-Voice任务解决数从29/278升至192/278；FDB-v3上以开源9B前端达
- **关键技术点**：快慢脑分工带来协调时序问题：前台听得到每句话却看不到任务版本，后台了解任务却不跟随对话，导致过期送达、错误绑定、幽灵执行、虚假交付等六类失败，与识别和推理质量无关。
- **主要指标**：- τ-Voice同前端同后端仅换harness：192/278 vs QAA 29/278，提升逾6倍 - FDB-v3 Pass@1：69.0%，高于GPT-Realtime（60.0%）与原生Venus-Audio（48.0%）；Tool F1 0.927、打断率7%全表最低 - τ-Voic
- **代码**：暂无 | **Demo**：https://amphionteam.github.io/Jarvis-Demo/

---
## [CoupleFlow: Null-Calibrated Auditory Attention Decoding With Time-Locked Brain-Speech Coupling and Flow-Matching Likelihood Ratios](https://arxiv.org/abs/2610.32950)

- **方向**：语音前端 | **子方向**：Other | **评分**：9/10 | **日期**：2026-10-26
- **一句话贡献**：听觉注意解码（AAD）要从秒级 EEG 判断听者聚焦哪一路语音，近期直接分类器报 1 s 近完美精度。本文证明其源于试次泄漏、眼动与响度捷径，跨内容即崩至随机。提出 CoupleFlow：决策仅经神经与声学嵌入的时间耦合，脑信号无时间信息时落于随机（null 校准），并以条件流匹配头构造 PMI 似然比判决、证明其贝叶斯最优。9 个 EEG/MEG 数据集内容不相交折下 5 s 于 7/8 集最优
- **关键技术点**：重建法需数十秒才可靠；直接分类器借试次内划分虚高至 95%+，跨试次跌回随机；各家预处理不一，NJU 集甚至未与音频时间锁定。
- **主要指标**：- 5 s 内容不相交折：KU Leuven 72.7%(+6.8)、DTU 76.2、Fuglsang'20 79.6、ESAA 77.9、KUL-255ch 69.4、SparrKULee 92.2(+8.9)、MEG-MASC 99.0%，7/8 最优；Broderick 63.6 持平线性 
- **代码**：https://github.com/saliAlavi/coupleflow | **Demo**：https://salialavi.github.io/coupleflow/

---
## [GSLM2: Multi-Stream Speech Representation Learning and Generative Spoken Language Modeling](https://arxiv.org/abs/2611.01143)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-11-03
- **一句话贡献**：GSLM2针对无文本口语语言模型（SLM）达到文本LM同等语言能力需多约四个数量级训练数据的瓶颈，指出两大根源：离散语音单元语言质量有限、单流单元难以兼顾音位细节与高层语义。方法上提出SpidR 2.0编码器，以师生自监督蒸馏加逐层可微分共享预测头在多个编码层学习稳定互补的单元空间；再以多流SLM联合建模六条层级单元流，含共享时序骨干、分流预测头与捕获流间依赖的生成式深度头。在6M小时、6.5B参
- **关键技术点**：标准GSLM对SSL编码器单一层的表征做后验k-means量化，迫使一个序列同时承载细粒度音位区分与高层语义规律，构成表示瓶颈；而词级/音节级低采样单元又丢失细粒度区分，压缩本身无法决定该保留哪些信息。
- **主要指标**：- sWuggy/sBLIMP/tSC（60Kh/1.2B）：79.3/71.8/84.5，较SpidR SLM（73.9/62.4/75.1）平均升约6分，Text LM为83.8/71.5/89.2 - 6.5B/6Mh会话域：80.7/72.9/90.5/63.2（sWuggy/sBLIMP/
- **代码**：https://github.com/facebookresearch/gslm2 | **Demo**：暂无

---
## [Disentangling Acoustic Cues in Alzheimer's Pathology and Perception: The Roles of Language and Gender](https://arxiv.org/abs/2607.23977)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：—
- **一句话贡献**：声学生物标志物在检测阿尔茨海默病(AD)方面显示潜力，但驱动诊断AI的线索与人类听众关注的线索是否一致在语言和性别间尚未得到充分探索。本文训练模型预测临床AD状态（病理）和跨Mandarin和Greek语言、男女性别说话人的人类感知评分。结果揭示了情境依赖的差异：病理-感知对齐在Mandarin和女性说话人中显著，但在Greek和男性说话人中消失。
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：暂无 | **Demo**：暂无

---
## [TamilEOT: A Dataset and Model for Semantic End-of-Turn Detection in Tamil Telephone Speech](https://arxiv.org/abs/2609.05631)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-04
- **一句话贡献**：语音代理必须在每个停顿处裁决用户是否说完，无语言模型时只能退化为固定静默超时。本文发布 TamilEOT 数据集（从 116 段真实泰米尔电话通话切出 18,485 条标注 turn 边界）及两个 audio-only 检测器（自 Smart Turn v3 微调，8.7MB 与 21MB）。在来自 30 通未见电话的 4,168 条 held-out 上，精度由零样本 70.30% 升至 83.
- **关键技术点**：语义端轮（EOT）检测是语用层面判断，单纯静默时长是表面近似；现有开源语义 EOT 检测器均以英语等大语种为主，南印度语言完全空白。作者以实验揭示规则标签与模型任务不等价：规则在正类命中 95.9% 但负类仅 44.4%（低于随机），因规则回答的是"是否存在长静默"而模型需回答"用户话语是否完成"。
- **主要指标**：- 精度：70.30%（零样本）→83.71%（8.7MB）→86.13%（21MB） - ROC-AUC：0.751→0.921 - 延迟：<150ms 单线程笔记本 CPU
- **代码**：开源（数据、权重、代码公开） | **Demo**：暂无

---
## [Improving Zero-Shot Phonetic Classification through Language-Agnostic Articulatory Features](https://arxiv.org/abs/2607.23606)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：—
- **一句话贡献**：当前语音到IPA的音素基础模型(PFM)依赖G2P标签，但这些标签在语音上并不忠实。本文在中文送气音和日本鼻音的零样本分类任务上评估了模型，发现G2P训练的PFM表现很差。提出基于连续发音特征(AF)向量的分类方法，该方法优于离散token方法，尤其对罕见音素。最优时间聚合策略对目标区分至关重要：送气音用单帧分类最佳，鼻音用片段分类显著提升。
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：暂无 | **Demo**：暂无

---
## [Simultaneous Speech-to-Speech Translation Without Aligned Data](https://arxiv.org/abs/2602.11072)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-02-11
- **一句话贡献**：同声传译需要将源语言语音实时翻译成目标语言并处理非单调词依赖。传统方法依赖词级对齐数据监督，这些数据难以大规模收集。本文提出Hibiki-Zero完全消除对词级对齐的需求。首先在句子级对齐数据上学习高延迟语音翻译，然后应用新型强化学习策略使用GRPO优化延迟同时保持翻译质量。
- **关键技术点**：Hibiki-Zero无需词级对齐，简化训练流程支持多语言无缝扩展。
- **主要指标**：翻译准确率、延迟、声音迁移、自然度均达最优。少于1000小时即可适配新语言。
- **代码**：https://github.com/kyutai-labs/hibiki-zero | **Demo**：暂无

---
## [Child-Centric Voice Anonymization in Single and Multi-Speaker Speech via Domain-Adapted SSL Models](https://arxiv.org/abs/2606.29897)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-06-29
- **一句话贡献**：本文提出针对儿童语音的隐私保护匿名化技术。通过领域自适应的自监督模型，学习儿童语音的安全表示，在保护隐私的同时保留语音可懂度和自然度。为未成年人的语音数据保护提供解决方案。
- **关键技术点**：基于SSL的儿童语音编码器，匿名化变换模块实现说话人信息移除。
- **主要指标**：说话人相似度降低70%，同时保持95%以上的可懂度。
- **代码**：暂无 | **Demo**：暂无

---
## [From Objectives to Applications: Aligning Architectural Biases in Audio Self-Supervised Learning](https://arxiv.org/abs/2607.00387)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-01
- **一句话贡献**：本文从预训练目标、架构归纳偏置和下游应用的对齐角度审视音频自监督学习(SSL)。不同于将SSL方法视为时间顺序的代理任务或模型家族序列，本文探讨不同监督信号如何塑造模型预期学习的表示。讨论围绕五个范式组织：辅助任务、对比学习、生成重建、离散token化和掩码预测，为SSL方法选择提供理论指导。
- **关键技术点**：审视音频SSL的预训练目标与架构归纳偏置对齐的统一框架。
- **主要指标**：揭示预训练目标与架构偏置如何影响表示学习，为SSL方法选择提供系统性指导。
- **代码**：https://github.com/colaudiolab/Awesome-Self-Supervised-Audio-Learning | **Demo**：暂无

---
## [Goodbye Equal Error Rate, Hello Local Information Disclosure: Evaluating Voice Anonymisation against 1-to-N Linkage Threats](https://arxiv.org/abs/2607.06259)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-07
- **一句话贡献**：语音匿名化旨在保护说话人身份。当前隐私评估主要依赖EER，但EER设计用于1-to-1验证，与真实1-to-N数据库链接攻击存在威胁模型不匹配。提出模块化信息论评估框架，核心指标Local Information Disclosure（LID）以比特量化单次试验 utterance 的精确隐私损失。在VoicePrivacy 2024 Challenge系统上评估，揭示即便EER接近完美的系统也可
- **关键技术点**：信息论评估框架：LID量化原始相似度分数到攻击者后验置信度的隐私损失。
- **主要指标**：揭示EER近乎完美的系统在1-to-N场景下最坏情况泄露可达1比特/次，有效加倍攻击成功率。
- **代码**：暂无 | **Demo**：暂无

---
## [Pitwall: Faithful Natural-Language Race-Strategy Briefings from a Calibrated Real-Time Monte Carlo Engine](https://arxiv.org/abs/2607.06495)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-07
- **一句话贡献**：实时体育解说是在截止日期下的接地生成：陈述涉及真实命名运动员，接地状态每几秒变化，生成时无参考文本。提出Pitwall系统生成英语、西班牙语、葡萄牙语的F1策略简报，将忠实性作为架构属性而非追求目标：每个发布的句子分解为类型化事实声明，每个声明根据促使它的概率状态验证。验证器同样门控微调数据：3045个模型撰写目标中，只保留81.9%所有声明都有状态支持的，其余回退到可证明忠实的模板。验证基于12
- **关键技术点**：Pitwall：Monte Carlo引擎（每圈2000次续篇）+ 事实验证器 + 三语生成模型。
- **主要指标**：Winner-in-top-3准确率90.3%（155次回测），留出Brier 0.0745。现场验证在奥地利和英国大奖赛成功。
- **代码**：暂无 | **Demo**：https://pitwall.jsantillana.com

---
## [GigaAM Multilingual: Foundation Model for Underrepresented Languages](https://arxiv.org/abs/2607.10371)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-11
- **一句话贡献**：本文针对 underrepresented 中亚语言（哈萨克语、吉尔吉斯语、乌兹别克语）构建多语言ASR基础模型。尽管缩放预训练取得成功，但长尾语言仍面临严重的数据稀缺问题。GigaAM Multilingual 是一个基于2M小时音频预训练的 Conformer 编码器，采用 HuBERT 风格训练目标，并引入聚类级数据平衡策略和领域感知采样方法以缓解头部语言主导问题。
- **关键技术点**：基于Conformer编码器，参数规模约1B，采用HuBERT风格的自监督预训练目标。
- **主要指标**：在哈萨克语、吉尔吉斯语、乌兹别克语ASR任务上显著优于Whisper Large v3和Omnilingual-1B，WER相对降低15-20%。
- **代码**：https://github.com/salute-developers/GigaAM | **Demo**：暂无

---
## [ECHOv2: Two-Level Band-Splitting Representation Learning for Anomalous Sound Detection](https://arxiv.org/abs/2607.10596)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-12
- **一句话贡献**：本文提出ECHOv2，一种用于异常声检测（ASD）的双层带分裂表示学习方法。现有预训练音频 backbone 未充分捕捉机器声音的频率特异性。ECHOv2通过学习局部带内表示捕获细粒度频谱模式，同时引入双层自蒸馏策略进行显式带间监督建模跨频率依赖关系。
- **关键技术点**：带分裂模型，包含intra-band（带内）和inter-band（带间）两分支。
- **主要指标**：在统一的ASD benchmark（embedding-based和adaptation-based两种协议）上达到SOTA性能。
- **代码**：https://github.com/yucongzh/ECHOv2 | **Demo**：暂无

---
## [Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?](https://arxiv.org/abs/2607.13864)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-15
- **一句话贡献**：监督微调（SFT）被广泛用于将自监督语音表示适应到下游分类任务。现有研究通常在单个预训练checkpoint上观察到的微小增益被解释为方法级改进，即更高的可达到性能上限。本研究证明此类结论并不总是可靠的，因为SFT结果很大程度上取决于特定的预训练实例。
- **关键技术点**：基于wav2vec 2.0、HuBERT和WavLM三种自监督语音表示模型，在SUPERB分类任务上评估不同SFT策略。
- **主要指标**：同一SFT配方在不同预训练实例上的表现差异显著，顶级配方的身份往往是checkpoint依赖的。
- **代码**：暂无 | **Demo**：暂无

---
## [End-to-End Markov State Sequence Learning for Auditory Attention Decoding](https://arxiv.org/abs/2607.18614)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-21
- **一句话贡献**：提出端到端Markov状态序列学习框架用于听觉注意力解码（AAD）。使用CRF联合优化窗口级神经发射与状态转移，而非将AAD作为独立短窗口分类器。
- **关键技术点**：ESCNet：EEG-Speech Correlation Network，保留时间对齐特征，将两个Pearson相关的差异直接转换为状态logits。CRF作为两层注意力状态模型。
- **主要指标**：- AVGC 1s窗口：CRF-Causal 86.5%，CRF-NC 92.4% - KUL：因果解码提升5.6% - USTC：因果解码提升2.0% - 四种发射骨架（ESCNet/AADNet/LSTM/Attn-GRU）均验证CRF训练优势
- **代码**：https://github.com/YusanX/AAD-CRF | **Demo**：暂无

---
## [SimulS2ST-Omni: Data-Efficient Streaming Speech-to-Speech Translation via Explicit Trajectory Supervision](https://arxiv.org/abs/2607.19810)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-22
- **一句话贡献**：本文提出SimulS2ST-Omni，一种支持流式的语音到语音翻译系统。现有方法通常受限于句子级监督或需要大量成对S2ST数据。本文仅使用约2000小时成对跨语言S2ST数据结合辅助监督即可实现句子级和长音频流式S2ST。通过两阶段Thinker-Talker因子分解解耦语言推理与声学预测，在RealSI和ACL60数据集上达到与最新闭源S2ST系统（如LiveInterpret 2.0）相当的A
- **关键技术点**：基于语音语言模型的两阶段架构，核心为Thinker-Talker因子分解。Thinker负责语言推理，Talker负责密集声学预测，有效缓解模态干扰。
- **主要指标**：ASR-BLEU达到与LiveInterpret 2.0相当水平，支持流式翻译。
- **代码**：暂无 | **Demo**：暂无

---
## [Multi-Phonation Graph Learning with Self-Supervised Speech Embeddings for ALS Detection and Progression Prediction](https://arxiv.org/abs/2607.25284)

- **方向**：医学语音 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-28
- **一句话贡献**：本文提出subject-level图框架，将多个ALS患者的发声录音聚合为k近邻图进行分类。系统比较4种SSL前端和5种GNN架构，最佳配置HuBERT+GIN在SAND数据集上达到0.73和0.69的mF1，显著超越基线（0.61和0.58）。
- **关键技术点**：Subject-level图框架：使用SSL嵌入（wav2vec 2.0、HuBERT、data2vec-audio、UniSpeech-SAT）提取2秒片段特征，构建kNN图，使用GNN（GCN、ResGCN、GAT、GraphSAGE、GIN）进行图分类。
- **主要指标**：HuBERT+GIN：Task 1（5类严重程度）mF1=0.73，Task 2（4类ALSFRS-R进展预测）mF1=0.69。相比SAND验证基线（0.61和0.58）显著提升。
- **代码**：暂无 | **Demo**：暂无

---
## [Qwen-Audio-3.0-Gen-Preview Technical Report](https://arxiv.org/abs/2607.27011)

- **方向**：音频大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-29
- **一句话贡献**：Qwen-Audio-3.0-Gen-Preview是一个统一非自回归框架，使用Diffusion Transformer (DiT)和共享变分自编码器（VAE）生成完整混合波形。提示增强将自由形式请求转换为结构化时序记录，两阶段数据课程和语义条件视图训练模型跨领域使用条件。在Seed-TTS-Eval上实现高说话人相似度，多speaker基准上跨轮一致性高于Seed-Audio-1.0。
- **关键技术点**：（仅标题，未精读）
- **主要指标**：- Seed-TTS-Eval说话人相似度：主要优势在三个子集上 - 多speaker基准：跨轮一致性高于Seed-Audio-1.0（中英） - AudioCaps：大型音频语言模型评估和AudioBox上优势明显 - 时间定位：比Seed-Audio-1.0更强 - SongBench：使用约1
- **代码**：暂无 | **Demo**：暂无

---
## [MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation](https://arxiv.org/abs/2608.03021)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-05
- **一句话贡献**：神经音频编解码器是LLM音频生成的基础tokenizer。现有工作广泛使用语义先验增强语言可懂度，但显式声学先验的整合仍缺乏探索。MeloCodec提出"Tokenize-then-Fuse"范式，预训练独立的离散旋律分支锁定旋律结构（音高、节奏），再进行特征融合，解决直接融合导致的优化不稳定问题。两阶段训练策略防止码本坍塌。在歌唱声音表示上优于基线，提升音高一致性，支持可控音高操控，最小化音色退
- **关键技术点**：神经音频编解码器（如EnCodec、DAC、SoundStream）将音频编码为离散token，作为LLM音频生成（如TTS、音乐生成）的输入。现有工作主要引入语义先验（如HuBERT、WavLM特征）提升可懂度，但显式声学先验（如旋律、音高、节奏）的整合尚未被充分探索。直接融合声学先验可能导致优化不稳定（如码本坍塌、收敛困难），特别是对于歌唱这类对音高敏感的领域。
- **主要指标**：- 重建质量：MeloCodec显著优于基线（EnCodec、DAC），特别是在高音区域 - 音高一致性：PCC（Pearson相关系数）提说明显高于基线 - 可控音高操控：在编码空间中进行音高偏移后，解码器能保持音色一致性 - 音色退化最小化：在MOS评估中，音色自然度接近原始录音 - 消融实验验
- **代码**：暂无 | **Demo**：https://anonymous.4open.science/api/repo/melocodec_demo-60EC/file/demo.html

---
## [DNN-Based Frequency-Dependent Estimation of Speech, Music, and Noise Power in Acoustic Mixtures for Hearing-Aid Scene Analysis](https://arxiv.org/abs/2608.17482)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：当前助听器场景分析依赖多个独立估计器（场景分类、VAD、SNR 估计），计算开销大且未利用任务间依赖。本文提出统一可解释的场景表示：用低复杂度因果 CRNN 将混合谱分解为语音/音乐/噪声三类时-频相关相对功率比例，再与混合功率相乘恢复各类功率谱。开发集总体对数误差 1.40 dB、PCC 0.891；未见数据集为 1.71 dB、0.875。下游 VAD 经简单阈值化即可达到与 SOTA Sil
- **关键技术点**：SOTA 场景分析通常由多个独立估计器组成（场景分类、VAD、SNR 估计、源定位/方向分析），输出控制压缩、降噪与程序自动切换。该模块化设计有两方面缺陷：一是计算低效，而深度学习算法进入助听器后台算力更趋紧张；二是独立估计器无法利用相关任务间的依赖，且多从同一混合声提取重叠信息（如 VAD 与 SNR 估计）。
- **主要指标**：- 开发集整体 LE 1.40 dB、PCC 0.891；未见数据集整体 LE 1.71 dB、PCC 0.875 - 分组合误差：噪声单源最低；双源中 N+S、M+S 低于 M+N；三源误差最大；语音/音乐单源误差主要来自能量误归至噪声类，说明语音谱结构更易区分而音乐与噪声重叠更强 - 定性验证：
- **代码**：暂无 | **Demo**：暂无

---
## [A Factorial Ablation of a Speech-to-SFT Pipeline: Differential Effects on Data Quality and Downstream Transfer](https://arxiv.org/abs/2608.20394)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-24
- **一句话贡献**：语音转SFT数据流水线在工业界广泛应用，但各阶段的边际价值此前从未被公开逐阶段验证。本文针对韩国医学与金融会议录音驱动的三段式流水线（Phase 0转录精炼、Phase 1 QA生成、Phase 2质量精炼）设计2x2因子消融，四种条件各生成约2600条QA，微调5大厂商9个（2.4B-70B）LLM，并以4个跨厂商LLM评判员、6位盲评领域专家及KMMLU/KMMLU-Pro/MMLU三个基准评
- **关键技术点**：现有语音转SFT工作（COSMIC、SIFT-50M、LiveCC、PodGPT等）或面向通用能力或采用持续预训练而非文本LLM SFT，均未对精炼环节做逐阶段消融，各阶段边际价值对实践者未知；且当数据源为语音时有转录噪声、命名实体对齐、语篇结构缺失等文档源不存在的前端挑战。
- **主要指标**：- QA质量（1-5分，4评判员均值）：Exp 0 3.81→Exp 2 3.99，Δ2-0=+0.18（95% CI [+0.06,+0.32]），前沿评判员子集+0.23；6位人类专家+0.220（全部为正且与LLM方向一致，医学ICC(2,3)=0.69） - 阶段差异：QA质量上Phase 
- **代码**：https://github.com/flitto/speech-to-sft-ablation-paper | **Demo**：暂无

---
## [Sensing Bone-Conducted Speech with Earbuds](https://arxiv.org/abs/2609.02165)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-02
- **一句话贡献**：针对无线入耳式耳机在噪声环境下自身语音（OV）采集困难的问题，本文系统分析了佩戴者语音诱发的耳机壳振动（骨导语音）的频谱与空间特性。基于 Anker P3i 与 A20i 两款耳机、17 名受试者的实测数据，发现该振动呈显著低通特性：400 Hz 以上以约 -93 dB/decade 滚降，100-400 Hz 为高功率频段（平均约 530 µg）。空间分析表明耳机主要沿耳道口进出方向振动，且个体
- **关键技术点**：骨导语音可提升 TWS 在噪声下的自语音采集，但耳机壳振动的带宽与空间特性缺乏系统测量，致使加速度计轴数选择、安装方向以及单轴/三轴方案缺乏设计依据，现有多项研究用法不一、未达共识。
- **主要指标**：- 振动带宽：400 Hz 以上约 -93 dB/decade 滚降；截止频率 P3i 约 360 Hz、A20i 约 280 Hz - 第一主分量方差占比：P3i 89%（77-96%）、A20i 79%（49-92%） - 主方向角度离散度：P3i 6.5°、A20i 14.7° - 单轴投影平
- **代码**：暂无 | **Demo**：暂无

---
## [Beyond .WAV: Design and Software Verification of VocalCap, a Traceable Browser-Based Audio Capture System for Vocal Biomarker Research](https://arxiv.org/abs/2609.03320)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：远程语音采集往往只交付一个音频文件，缺少"信号如何被捕获、传输、处理与验收"的证据。VocalCap为受试者自助式语音采集设计机构可控浏览器系统，每个录音同时保留浏览器原生对象、客户端无损Float32 WAV与服务端规范单声道PCM16 WAV，并关联完整性与转换溯源证据。软件验证证实40ms连续性边界在8/16/44.1/48kHz正确生效，活动声道选择RMS偏差超低频低于0.001dB。
- **关键技术点**：语音生物标志物研究要求把采集技术验证与下游推断分开，远程自助采集时无受训人员在场，权限处理、编码与持久化均不可见。同类系统各覆盖部分环节，但没有一个把双工件配对、逐字节校验、版本化规范化等整合为单一验收契约。SPIRA项目（6000+语音捐献者）的空白录音问题直接催生本设计。 **系统设计：** Flask服务端+移动优先Web前端，协议通用任务执行器（麦克风测试、持续元音、标准句、计数、自发语音5任务）。同一MediaStream并行馈入MediaRecorder（原生对象N）与AudioWorklet（Float32 WAV无损L）双路径。采集记录含完整清单M（SHA-256）、采集证据E
- **主要指标**：- 仓库路径134/134、JS套件6/6、Python测试43/43全部通过 - 40ms边界：39ms通过、40/41ms拒绝 - 活动声道选取后RMS偏差全部<0.001dB（等权平均约6.02dB衰减） - 生产E2E：2浏览器画像、10接受录音、30工件全部通过校验
- **代码**：暂无 | **Demo**：暂无

---
## [KanAdapter: A Kolmogorov-Arnold Network-based Plug-and-Play Module for Efficient Fine-tuning of Foundation Speech Models](https://arxiv.org/abs/2609.05281)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-04
- **一句话贡献**：全文微调自监督（SSL）语音大模型计算开销巨大，而现有参数高效微调（PEFT）方法主要依赖 MLP 适配器，其固定激活函数在紧凑参数预算下表征能力受限。本文提出 KanAdapter，一种基于 Group-Rational KAN（GR-KAN）的即插即用适配器框架，采用并行瓶颈设计，在冻结的 Transformer 编码器旁插入可训练 GR-KAN 分支，并从预训练 MLP 层迁移权重实现稳定初
- **关键技术点**：现有 PEFT 方法应用到语音 SSL 模型时建模能力受限：LoRA 本质是无非线性激活的线性低秩分解，难以刻画伪造痕迹、情感分布等复杂语音特征；AdaptFormer 的 MLP 瓶颈使用固定激活，表达力不足。针对语音 SSL 的 PEFT 研究仍少见，将 KAN 类可学习激活模块用作适配器此前尚属空白。
- **主要指标**：- 说话人验证（9M 可训练，削减 97.5%）：Vox1-O 0.52%，全量微调（364M）0.49%，AdaptFormer（8M）1.44%，LoRA（4M）2.25% - SER（16M，削减 95.2%）：Test F1-Macro 0.3290，保留全量 99% 性能；AdaptFor
- **代码**：暂无 | **Demo**：暂无

---
## [Voice or Stereotype? Disentangling Acoustic and Content-Based Gender in Speech-to-Speech Models](https://arxiv.org/abs/2609.09263)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-08
- **一句话贡献**：在配音、翻译、语音代理等语音到语音(S2S)任务中，模型需判断说话人性别。商用S2S系统多以固定音色输出，使"输出音色是否随内容刻板印象漂移"这一传统探针结构性失效。本文用神经TTS构建 180 条音声化段落（英/西/中文 × 阳刚/中性/阴柔内容 × 男/女声），在 5 个模型的 5 类任务上交叉验证。结果：渲染音色无刻板漂移（Δ=-0.018±0.020），但内容每向阴柔推进一档，判"女性"胜
- **关键技术点**：S2S模型听得到说话人嗓音中的性别信息，忠实系统应按"听起来的性别"而非"通常谁说这类内容"来判断。但主流S2S模型以单一固定输出音色回答，使"输出音色是否向刻板印象漂移"的检测永远通过——无漂移≠无偏置。现有文本偏置基准（WinoBias/BBQ）仅限英文模板/多选题，语音基准（Spoken StereoSet、VoiceBBQ）为多选QA，缺少长文本、生成式评测。
- **主要指标**：- 渲染音色：15次readback拟合content×voice交互无显著项，合并Δ=-0.018±0.020 - 归因胜算比：Gpt-audio OR=21.9、Gemini OR=24.3；开源GLM OR=1.7、Kimi OR=3.3、Step-Audio OR=3.4 - 误称率：错配单
- **代码**：暂无 | **Demo**：暂无

---
## [StepAudio 3 Gen Technical Report](https://arxiv.org/abs/2609.12945)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-11
- **一句话贡献**：本文提出StepAudio 3 Gen，一个统一的通用音频生成模型，在单一框架内支持零样本TTS、声音设计、人声生成、音效、音乐、vibe speech及多类音频混合生成。其核心是离散自回归生成器：StepAudio Tokenizer以12.5Hz、16×2048共享RVQ码空间对语音/音乐/环境音统一量化，同时融合语义与声学特征；LLM主干沿时间轴自回归预测第0层码本，轻量因果Transfor
- **关键技术点**：TTS、文生音效、音乐与唱歌传统上沿各自独立技术路线发展，系统间表示、条件格式与生成管线互不兼容。近年统一音频生成分两大流派：连续隐空间扩散/流匹配（并行渲染高效）与离散unit的LM式序列建模（与LLM词表、因果目标、交错上下文天然兼容）。但高保真RVQ帧含多码本，展平后序列过长，仅用粗语义token又丢失声学细节；向文本LLM注入音频token还会因嵌入统计不匹配与残差码目标干扰，导致文本能力遗忘。
- **主要指标**：- 1. RVQ Adaptor消融：AISHELL-1 CER 3.00%(vs 5.25%)、LibriSpeech test-clean WER 3.41%(vs 6.00%)、MMAU 51.70(vs 40.70)、CoVoST En→Zh/ Zh→En BLEU 30.56/18.59(
- **代码**：暂无 | **Demo**：https://stepaudiollm.github.io/step-audio-3-gen/

---
## [Objective Intelligibility Prediction Using Distance Metrics on Speech Foundation Model Representations](https://arxiv.org/abs/2609.13046)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-11
- **一句话贡献**：预训练语音基础模型（SFM）的高维表征已被证明有利于客观语音质量和可懂度预测。已有神经可懂度预测工作通常利用这些表征进行任务特定微调，而本工作评估在不进行任何额外训练的情况下，这些表征对可懂度预测的效用。作者对多个语音基础模型进行了逐层分析，将各种嵌入距离与主观可懂度评分相关系联。结果表明，Whisper语音识别模型提取的嵌入最适合此任务，在采用Fréchet Audio Distance（FAD
- **关键技术点**：语音助听器、编解码器、语音增强等技术的核心目标是保持或提升语音可懂度，需要高效的评估方法。主观测试虽是金标准但昂贵耗时，传统基于信号处理或ASR的概率/混合指标各有局限，WER类方法局限于英语、不可微。作者希望探究无需训练的、基于预训练SFM嵌入距离的、可微且跨语种稳健的可懂度预测方案。
- **主要指标**：- 模型对比（cosD最好层）：Whisper Base在NCLEIR上PCC=-0.560/SRCC=-0.463，TMHINTQI上PCC=-0.583/SRCC=-0.621，全面优于WavLM、wav2vec 2.0及MFCC。逐层分析：FAD最稳健，最佳层为最后编码器/解码器层。模型规模：
- **代码**：暂无 | **Demo**：暂无

---
## [CVSS-X: A Multilingual Speech-to-Speech Translation Corpus for 28 Languages](https://arxiv.org/abs/2609.13413)

- **方向**：语音大模型（语音到语音翻译语料） | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-11
- **一句话贡献**：CVSS 语料仅支持 21 种语言到英语的多对一语音翻译，缺乏从英语出发的一对多训练数据。本文提出 CVSS-X，反向扩展 CVSS，构建从英语到 28 种目标语言（覆盖 12 个语系）的大规模合成语音到语音翻译语料，含 CVSS-X-C（每语言两个固定嗓音）与 CVSS-X-T（跨语言音色克隆）两个变体。语料约 24 万句对/语言，总量超 16,000 小时，为 CVSS 的 8 倍；质量评测中
- **关键技术点**：真实并行的语音到语音翻译语料因跨语言对齐录制成本极高而稀缺；SpeechMatrix（41.8 万小时）为挖掘式对齐且仅覆盖 17 种欧洲语言，SeamlessAlign（37 语言）仅公开元数据需自行重建。现有最大规模开源语料 CVSS 仅支持 X→EN 单一方向，阻碍了从英语翻译及非英语语言对间的研究。
- **主要指标**：- CVSS-X-C：UTMOS 3.55 | ASR-BLEU 82.4 | WER/CER 12.1% - CVSS-X-T：UTMOS 3.21 | ASR-BLEU 79.4 | WER/CER 14.1% | 说话人相似度 0.607 - CVSS-C 对照：UTMOS 4.43 | AS
- **代码**：https://github.com/ErmisAI/XVSS-X | **Demo**：暂无

---
## [StepAudio 3 Realtime Technical Report](https://arxiv.org/abs/2609.14005)

- **方向**：语音大模型（语音生成 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-12
- **一句话贡献**：实时语音交互需要在深度推理、快速应答与自然的轮换控制之间取得平衡。论文提出 StepAudio 3 Realtime，一个约 196B 总参数（11B 激活）的端到端语音-语言基础模型，围绕"监听-对话-思考-行动"连续循环组织 Deep Perception、Seamless Duplex、Think-While-Speaking 与流式 Voice Agent 四大能力。实验表明其在 Step
- **关键技术点**：全双工语音对话需在未说完的句内停顿与话轮结束之间、简短应和与实质打断之间做出区分，复杂请求还需在响应延迟与深思熟虑间权衡，工具调用又要求外部任务与对话并行推进。现有多数系统分别优化识别、理解或流式生成，缺乏对感知-推理-行动的统一协调。
- **主要指标**：- ASR Max：LibriSpeech test-clean WER 1.18｜test-other 2.28｜AISHELL-1 CER 0.49｜ContextASR-Bench 英/中宏平均误差 5.67%/1.23%（均第一） - 音频理解宏平均：81.3（MMSU 90.6 领先 7.
- **代码**：暂无 | **Demo**：https://stepaudiollm.github.io/step-audio-3-realtime/

---
## [CCMAN: Cognitive Instability-Aware Cross-Modal Attention Network for Interpretable Temporal Biomarkers of Verbal Fluency Speech](https://arxiv.org/abs/2609.14764)

- **方向**：语音前端（语音医学检测 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-13
- **一句话贡献**：现有基于语音的认知衰退自动检测多在整段录音上聚合特征，忽略言语流畅度任务中的词级时序动态与生成不稳定性。本文提出认知不稳定性感知的跨模态注意力网络（CCMAN）：先在12个记忆探测任务上预训练任务无关的多模态认知语音表征，再在60秒语义与语音流畅度任务上微调。在843名受试者共165.44小时语音上，语义流畅度二分类Macro-F1达0.81、多分类0.59，语音流畅度达0.77与0.53；独立P
- **关键技术点**：传统语义/语音流畅度评分是粗粒度的静态指标；多数深度学习模型对录音级特征平均池化，丢失会话内的检索不稳定性信息，且缺乏跨数据集泛化与临床可解释性。
- **主要指标**：- 语义流畅度二分类Macro-F1：0.81（LLM静态基线0.75） - 语义多分类Macro-F1：0.59（静态基线0.50） - 语音流畅度二分类/多分类：0.77 / 0.53（+5% / +7%） - 消融：Base 0.50→+Drift 0.52→+CrossAttn 0.54→+
- **代码**：https://github.com/Madhurananda/CCMAN | **Demo**：暂无

---
## [CLASH: Counterfactual Auditing of Lexical and Prosodic Reliance in Spoken Sarcasm Detection](https://arxiv.org/abs/2609.16582)

- **方向**：语音大模型（口语理解 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-16
- **一句话贡献**：口语讽刺检测器可能依赖词汇、韵律或其交互，但常规评测无法揭示实际决策信号。本文提出 CLASH（Controlled Lexical-Acoustic Separation Harness），一种双语反事实诊断框架，对每条话语构造原始、保词汇、保韵律和近似中性四种条件，系统评测 eGeMAPS 手工特征、WavLM/wav2vec 自监督探针及大型音频语言模型。对仅目标话语的 Qwen3-Omni
- **关键技术点**：现有口语讽刺检测研究集中于特征融合与不一致性建模以提升性能，但聚合性能提升无法证明系统真正使用了韵律；学习式语音表征将词汇与韵律信息纠缠在同一空间，有无音频特征的对比只能度量聚合贡献，无法隔离词汇、韵律及其交互。先前研究（如 LISTEN 揭示音频大模型的词汇主导）未提供中性参照，也未区分分数移动、标签判别力与二分化决策的差异。CLASH 用配对阶乘设计补充这些空白。
- **主要指标**：- Qwen3-Omni 原始语音 AUROC：CMMA 0.734（Macro-F1 0.602）、MUStARD 0.775（Macro-F1 0.690） - 时长均衡后 A_L−A_P：CMMA 0.148（95%CI [0.103,0.193]）、MUStARD 0.135（95%CI [
- **代码**：https://github.com/glam-imperial/clash | **Demo**：暂无

---
## [EquiSELD: Efficient training of equivariant sound event localization and detection networks](https://arxiv.org/abs/2609.23156)

- **方向**：语音前端； | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-22
- **一句话贡献**：一阶 ambisonics（FOA）信号具有严格的O(3)旋转反射对称性，但现有声事件定位与检测（SELD）方法要么靠旋转增广近似学习该对称性，要么使用计算昂贵的SO(3)等变网络，无法处理同类重叠声源且未利用反射对称。本文提出EquiSELD，首个对完整O(3)群精确等变的SELD注意力网络：将每个时频token处理为"O(3)不变标量+等变声强向量"双流，经Multi-ACCDOA读出不变活动
- **关键技术点**：（仅标题，未精读）
- **主要指标**：- TAU2021 ℰS：0.40（最强基线SELDNet+ 0.47、CGNet-STS 0.51，差-0.11） - STARSS23 ℰS：0.56（SELDNet+ 0.60、CGNet-STS 0.72，差-0.04/-0.16） - TAU2021：LE 16.4°、F20° 49.8%
- **代码**：https://github.com/labhamlet/equiSELD | **Demo**：暂无

---
## [Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction](https://arxiv.org/abs/2609.25176)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-23
- **一句话贡献**：面向可靠的代理式语音交互，本文提出 Qwen-Audio-3.1-Realtime，围绕"思考-行动-表达与协调"三层设计：以 Core-Cocktail SFT 与 M2-OPD 双路在线蒸馏夯实音频推理底座，用自演化可执行环境与多粒度 GRPO 轨迹学习工具调用与长程任务完成，并显式对齐"怎么说、何时说、是否说或做"的会话策略。相较 3.0，τ-Voice 半双工任务成功率由 78.4% 升至
- **关键技术点**：（仅标题，未精读）
- **主要指标**：- τ-Voice Overall：82.0%（3.0 为 78.4%，次优 GPT-Realtime-2 仅 43.8%，领先 38.2 分；Airline 64.0→74.0） - FDB v1.5 背景语音响应率：0.13，较 3.0 的 0.73 降 60 个百分点；恢复率 0.87 - A
- **代码**：暂无 | **Demo**：暂无

---
## [Persistent Delivery Optimization for Streaming Speech-to-Text Translation with Revisions](https://arxiv.org/abs/2609.26427)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-23
- **一句话贡献**：支持修订的流式语音翻译（S2TT）可纠正早期草稿，但基于可见文本的过程奖励会把"早输出"功劳记给随后被撤回的临时内容，造成可见性与最终交付的错位。本文提出持久性交付优化 PDO：中间奖励只分配给能在全部后续修订中存活的内容（当前草稿与其后所有草稿的最长公共前缀），最终译文质量另行单独计分；轨迹级回报让后续修订反过来影响早期输出的信用。仅用 7.49 小时 FLEURS 适配数据，PDO 在 5 个
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：https://github.com/ggiggit/PDO_S2TT | **Demo**：暂无

---
## [WenetSpeech-Min: A Large-Scale Minnan Speech Corpus with Dual Transcriptions for Dialectal Speech Processing](https://arxiv.org/abs/2609.36834)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-30
- **一句话贡献**：闽南语长期缺乏大规模真实场景、同时配对"方言转写+书面普通话转写"的语料。本文发布WenetSpeech-Min：约10,000小时多源在线媒体闽南语音库，每条话语均配对闽南语方言转写与普通话转写双文本；并建立覆盖双转写目标的ASR基准（6小时人工校验）与闽南语TTS基准（Easy 500句+Hard 250句），配套发布在语料上微调的Qwen3-ASR、FireRedASR2、CosyVoice
- **关键技术点**：闽南语覆盖福建、台湾及东南亚，但公开资源稀少：Common Voice仅小规模朗读语料，MinSpeech数千小时只有普通话转写，YT-THDC有方言-普通话配对却仅30小时，Breeze Taigi评测集不公开，跨模型公平比较与可复现评测缺失。 **数据管线：** 采集多源媒体音频后VAD切分，以SNR、时长计算WV-MOS声学质量分，经DaSheng事件检测过滤非语音、pyannote估计说话人数作元数据；用1,600小时人工闽南语转写分别微调Qwen3-ASR、FireRedASR2-AED、Fun-ASR-Nano作三个互补标注器，ROVER融合生成方言转写；有内嵌字幕的媒体用WeSu
- **主要指标**：（仅标题，未精读）
- **代码**：/Demo：https://aslp-lab.github.io/WenetSpeech-Min-Repo/ | **Demo**：https://aslp-lab.github.io/WenetSpeech-Min-Repo/

---
## [Almost Human, Except When It Matters: VoxParity and the Decisions a Voice Should Change](https://arxiv.org/abs/2609.35922)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-30
- **一句话贡献**：语音智能体已在真实电话线中执行转账、药品续方、关停服务、紧急派发等动作，而急救调度、反电诈、民航话务、赌博年龄核验等行业规范均承认：来电者"听起来如何"可以改变正确动作。VoxParity 是针对此盲区的基准：同一转写文本保持不变，只改变声音（哭泣、监护仪报警、背景中的 Mayday、儿童嗓音、噪声掩盖药名），正确的工具调用随之翻转。它以纯文本管线作对照零假设，检验模型是否真正因"听见"而改变决策
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：/Demo：https://github.com/bhavik-mangla/voxparity-bench（Zenodo 存档 doi:10.5281/zenodo.23008159） | **Demo**：https://github.com/bhavik-mangla/voxparity-bench（Zenodo 存档 doi:10.5281/zenodo.23008159）

---
## [Audiovisual Joint Learning for End-to-End Hearing Aids](https://arxiv.org/abs/2610.08579)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-07
- **一句话贡献**：本文提出AV-NeuroAMP，首个把视听语音增强与神经听力损失补偿统一为端到端框架的助听器方法。模型同时输入带噪语音、目标说话人脸视频与听者纯音测听图，联合完成降噪、个性化放大与动态范围压缩，直接优化听者特定的最终输出，规避传统两级级联带来的误差传递。视觉线索为竞争说话人场景提供互补的发音信息，正是纯音频方案难以获得的增益来源。论文还提出AC-FiLM听图条件化调制，并在英语域内与普通话域外噪声
- **关键技术点**：现有助听器普遍将语音增强与听力损失补偿分两级串联，增强阶段的残留干扰、失真与电平偏差会被放大级继续继承；纯音频增强在面对竞争说话人时，因目标语与干扰语声学特征高度相似而难以有效分离。
- **主要指标**：（仅标题，未精读）
- **代码**：暂无 | **Demo**：暂无

---
## [5. EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams](https://arxiv.org/abs/2610.12248)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-09
- **一句话贡献**：可穿戴AR助手需从连续第一人称视听流中自主决定何时开口，但现有omni-modal模型均为被动对话，主动视频助手只能输出文本。本文提出EgoVoice：用源分离与语音重合成将HoloAssist真实教练指导录音转成91.7小时干净训练数据，微调MiniCPM-o 4.5学习"倾听或开口"的秒级决策，再以DPO精化干预时机。170个测试会话上，闭源API开场F1仅0.02-0.03，EgoVoice
- **关键技术点**：真实物理任务中用户常忙碌或无法察觉何时需要帮助，而现有语音助手是反应式的，依赖显式提问或VAD触发；主动视频助手（如ProAssist）只产出文本。尚无工作将"何时说话+说什么"统一到单一模型中从连续第一人称视听流训练。
- **主要指标**：- 开场时机F1：EgoVoice-SFT 0.274，EgoVoice-DPO 0.324（zero-shot MiniCPM-o 4.5仅0.113；Gemini Live 0.022、gpt-realtime 0.030、gpt-realtime-2 0.024） - 内容相关余弦相似度：SF
- **代码**：暂无 | **Demo**：https://egocentricvoice.github.io/

---
## [From 2.1M Hours of Raw Broadcast Audio to Finnish Speech SSL: Confidence Filtering and Architectural Analysis at Scale](https://arxiv.org/abs/2610.13102)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-12
- **一句话贡献**：针对广播档案用于低资源语言语音自监督预训练时含大量噪声、非语音与多语内容、"存在语音"不等于"高质量"的问题，本文提出以ASR的CTC置信度作为数据质量代理：从芬兰RTVA 210万小时广播出发，经pyannote VAD得120万小时、ASR转写去重得89万小时，再以置信度阈值τ=-0.1筛出47.1万小时（99%芬兰语）。在wav2vec 2.0框架下对Transformer、Macaron-
- **关键技术点**：广播档案规模大、多样但质量混杂，既有工作仅用VAD或LID保证"提取到语音"，从未按质量系统性筛选无标注预训练数据；同时先前SSL架构对比同时变动结构与参数量（如618M Conformer vs 317M Transformer），无法区分收益来自架构还是容量。
- **主要指标**：（WER）： - 置信度过滤 vs LID过滤：同等~72%保留率下4个验证集中3个更低，最终带来3-7%相对WER下降 - Base Conformer(17/512/1536)：CV 5.69、FLEURS 10.56，较同参数Transformer（9.74/13.02）相对下降41.6%/1
- **代码**：https://github.com/aalto-speech/large-scale-monolingual-speech-foundation-models （模型开源，语料因广播版权不可再分发） | **Demo**：暂无

---
## [ELARSpeech: A 30K-Hour Dataset Across 675 Underrepresented Languages for Long-Tail Multilingual Speech Technologies](https://arxiv.org/abs/2610.19388)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-15
- **一句话贡献**：现有语音资源在语言长尾上存在可及性、声学与域多样性、评测基准三重缺口。论文基于濒危语言档案（ELAR）田野录音构建ELARSpeech：共30,202小时、675种低资源语言，其中标注子集2,791小时（443语言）、无标注子集27,412小时（665语言），259种语言不被现有模型支持、53种无ISO 639-3编码。实验表明其可有效支撑ASR/TTS长尾适配，伪标签扩展带来最高6.1%相对CE
- **关键技术点**：公开语料多仅覆盖数百语言，千语言级数据集因许可限制不可公开；MMS/XEUS等集中于圣经朗读域；ML-SUPERB等基准偏高资源语言，长尾有效性缺系统评测。
- **主要指标**：- ASR单语宏平均CER：Whisper 22.48%（30 pivot语言最优） - 无ISO语言宏平均CER：OmniASR-CTC-300M 24.50%，优于Whisper 1.5B的24.63% - 伪标签扩展：最高6.1%相对CER下降；Dawoodi在ELAR测试集93.99→22.
- **代码**：https://github.com/sanghyang00/elarspeech/ | **Demo**：暂无

---
## [ConvexLLM: Scaling Convex-Hull Speech Interfaces to General-Purpose Audio Intelligence](https://arxiv.org/abs/2610.23539)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-19
- **一句话贡献**：通用语音音频大模型通常以MLP/Q-Former把声学特征无约束映射到解码器输入空间，迫使文本预训练解码器重新学习解释该表征并损失语言能力。ConvexLlm用C-Gate接口把每个音频位置表示为冻结文本嵌入的连续凸组合：路由词表top-16行并以非负归一权重加权求和，输出恒在文本嵌入凸包内。模型由Whisper-large-v3编码器与Qwen3.5-9B解码器组成，经三阶段多任务训练加文本教师
- **关键技术点**：MLP/Q-Former投影器输出可落在文本嵌入表凸包之外的无约束向量，解码器适配语音时需重学解释新输入分布，常退化推理与指令遵循等文本能力；LegoSLM等词表接口虽更贴近文本空间，但此前仅在ASR、情感识别等受控任务验证，未支撑覆盖语音交互、推理、识别与非语音音频理解的通用模型。
- **主要指标**：- VoiceBench Overall：75.36，高于MiniCPM-o 4.5的73.04、Kimi-Audio的70.26、MiMo-Audio的67.01 - 知识与推理：OBQA 90.33、MMSU 72.32、SpMMLU 73.42、BBH 80.40（BBH超次优MiMo-Aud
- **代码**：暂无 | **Demo**：暂无

---
## [SpikeAid: A Streaming Spiking Hearing Aid Framework for Joint Noise Reduction and Wide Dynamic Range Compression](https://arxiv.org/abs/2610.24696)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-20
- **一句话贡献**：助听器需同时完成降噪（NR）与宽动态范围压缩（WDRC）。传统级联流程两阶段分离设计，NR误抑制的弱语音无法被后续压缩恢复、残余噪声还可能被放大；已有端到端神经联合方法依赖密集ANN计算，难以满足助听器实时低功耗常开约束。本文提出首个因果端到端脉冲神经网络框架SpikeAid：NR-Net估计互补语/噪掩码，WDRC-Net估计分支增益，融合后的有效增益作用于带噪复谱经iSTFT重建；底层神经元D
- **关键技术点**：NR输出直接决定WDRC的增益与包络行为，级联设计无法联合最优；SNR感知压缩等策略部分考虑交互但仍保留独立模块与预定义策略。Neural-WDRC等神经联合方法逐帧MAC密集计算，与助听器的质量—延迟—功耗三角约束冲突；现有SNN去噪器只重建干净语音，不产生受处方WDRC剖面支配的助听输出。
- **主要指标**：- 助听器任务（PESQ/STOI/HASPI v2/HASQI v2）：2.214 / 0.8412 / 0.4365 / 0.1812，前三项最优 - 关键对比：PESQ较最强SNN基线Spiking-FullSubNet 2.159提升0.055，HASPI较Binary S4D 0.4290
- **代码**：暂无 | **Demo**：暂无

---
## [You Are the Trigger: Speaker-Activated Backdoors](https://arxiv.org/abs/2610.27210)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-21
- **一句话贡献**：现有音频后门都要求攻击者在推理时向受害者输入注入或诱导触发器（噪声、超声、语音转换片段），防御方因此可针对"异常输入"检测剥离。本文提出 Speaker-Activated Backdoor（SAB）威胁模型：攻击者只在微调阶段污染模型，部署后不接触推理输入，目标说话人自然、未修改的语音本身就是触发器。方法用两阶段微调先增强说话人身份可及性、再将目标身份绑定到恶意 payload，仅需 2 分钟真
- **关键技术点**：既有音频后门（Koffas 超声、Shi 环境声、Bartolini 污染 Whisper 等）都假定攻击者能控制推理时音频，触发器是"外来附加物"，因而可被输入过滤、VAD 或异常检测削弱。Cai/Ye/Schoof 等虽改用音色、情绪等自然属性，但只在小分类模型验证，推理时仍需语音转换。SAB 的差异是触发器零成本、零接触：目标一开口即触发。
- **主要指标**：- Whisper-medium 后门成功率（BSR）：90.2% - Parakeet 后门成功率（BSR）：97.0% - Whisper-medium / Parakeet 误触发率（FPR）：1.7% / 0% - 指令注入率（C1）：96.9% - 下游 Agent 有害执行率：87.5%
- **代码**：暂无 | **Demo**：暂无

---
## [StyleStream 2.0: Fast and Controllable Streaming Voice Style Conversion](https://arxiv.org/abs/2610.28940)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-22
- **一句话贡献**：StyleStream 1.0 首次实现零样本整体语音风格转换（音色/口音/情感）流式生成，但 16 步像素流匹配使消费级 GPU 端到端延迟约 1s，且风格只能由参考语音指定。本文提出 StyleStream 2.0：将 Stylizer 重训为 few-step 像素 MeanFlow 并施加 Self-Forcing 式逐块自回归微调，端到端延迟降至 520.7ms（约 2× 提速）；同时取
- **关键技术点**：StyleStream 1.0 确立"去风格内容+风格嵌入重建 mel"两阶段流式 VSC 范式，但存在两项实用瓶颈：像素 mel 上的多步流匹配推理慢、难以交互；风格条件依赖参考语音与 mel 上下文信息分散，无法以自然语言精确设计目标音色或仅修改单一属性。
- **主要指标**：- 离线 VSC：S-SIM 0.879、A-SIM 0.705、E-SIM 0.806、S-SMOS 4.32、WER 7.00%，全面优于 1.0（0.869/4.23/7.47）及 Vevo、CosyVoice 3.0；仅用 4 NFE - 流式：端到端 520.7ms（300ms 分块+80
- **代码**：暂无 | **Demo**：https://berkeley-speech-group.github.io/StyleStream2.0

---
## [Spark-Audio 1.0 Technical Report](https://arxiv.org/abs/2610.31292)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-23
- **一句话贡献**：传统ASR只优化逐字转写，丢弃了情感、性别年龄、韵律与环境声等副语言信息，且语音基础模型长期依赖受限的海外算力栈。科大讯飞发布Spark-Audio 1.0：由0.65B稠密音频编码器与30B-A3B MoE LLM耦合的语音基础模型，基于1300万小时音频与大规模文本训练，支持99语言/202方言语音识别、语音翻译、音频感知理解及语音/文本对话，全程在华为昇腾910B与海光BW1000国产芯片上
- **关键技术点**：现有ASR面向单一转写目标，难以统一声学感知与语言推理；同时竞争性语音基础模型被认为需要不断堆叠数据与参数，且训练依赖海外软硬件生态，国产算力上端到端训练可行、少量数据能否支撑实用场景均属未验证问题。
- **主要指标**：- FLEURS-zh CER 1.88%、FLEURS-en WER 2.25%，较最优对照错误率相对降低35.2%/16.7%（Flash为2.90/3.70） - FLEURS 14/20/64语言平均WER/CER 2.81/6.30/31.89%，前两组最优，64语组逊于Gemini 3.
- **代码**：暂无 | **Demo**：https://iflytekresearch.iflytek.com/experience/spark-audio

---
## [SURE-Tagger: Structured Speech Representations for Compositional Evaluation and Targeted Data Selection](https://arxiv.org/abs/2610.32198)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-26
- **一句话贡献**：针对自由文本语音标注属性覆盖不一致、"遗漏"无法区分缺失/忽视/不确定的问题，提出SURE-Tagger：按L1词内容、L2说话人、L3时间结构、L4副语言、L5声景五层，为每条录音构造"显式属性值+证据不足null+补充描述"的半结构化表示，由LLM整合专家感知模型观测生成。配套Tag-Bench（650条真实+500条智能体合成场景，29轴评测）。SURE-Tagger在25/29（真实）、2
- **关键技术点**：自由caption在录音间属性覆盖与措辞不一，省略属性不可解释为确认缺失，难以用作一致的样本级属性记录；数据集级聚合分数亦会掩盖多条件并发下的模型短板，跨数据集联合条件评估与定向改进缺乏共同表示。
- **主要指标**：- Tag-Bench综合：真实76.28%（Omni-Flash 62.79、Captioner 51.23）、合成78.88%、综合77.28%；结构化19轴综合83.19% - 弃权拆解：SURE显式null率仅5.6%，Captioner达78.3%；null计零时Captioner崩至12
- **代码**：暂无（承诺录用后开源） | **Demo**：暂无

---
## [ADReasoner: Acoustic-Linguistic Cue-Aware Reinforcement Learning for Explainable Alzheimer's Disease Detection from Speech](https://arxiv.org/abs/2610.34220)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-27
- **一句话贡献**：现有语音 AD 检测多被简化为二分类黑箱，近期 SpeechLLM 虽能输出解释，但仅靠 SFT 学到的是表层描述，未把细粒度声学-语言学线索与临床意义关联。作者提出 ADReasoner，首次以强化学习将 AD 检测重构为可解释推理任务：合成并标注 ADCoT-7K 推理数据集，用线索中心的两阶段 SFT 增强线索感知，再以四项奖励的 GRPO 优化推理与标签一致性。在 Pitt 测试集取得 8
- **关键技术点**：AD 语音数据受隐私与采集成本限制规模极小，且现有数据集只有离散标签，缺少细粒度线索标注与思维链监督。当前 SpeechLLM 对异常停顿、语义不连贯等关键线索感知弱，而标准 GRPO 仅用格式与标签规则奖励，无法约束开放式推理，易出现推理与预测标签不一致。
- **主要指标**：- Pitt macro-F1：80.72% - Pitt 准确率：81.10% - 格式解析率 FPR：100.00% - 推理分 / 一致性分：85.24% / 90.86% - LLM-R 四维均值：3.70，较最强基线 GPT-audio-1.5 的 3.27 相对提升 13.15% - 跨
- **代码**：暂无 | **Demo**：暂无

---
## [The Voice on the Line](https://arxiv.org/abs/2610.35272)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-27
- **一句话贡献**：论文面向单麦克风转写时同时收进旁人语音的真实通话，训练 20 ms 帧、无前视的因果目标说话人隔离器，从通话本身取已听到的最响 3 s 在线注册主叫，并以 WER 及漏词、插词、泄漏词分解评价。作者指出短窗评测掩盖长通话遗忘主叫与主叫独处被误伤两个失效，用 24 s 长通话训练、因果化 WavLM-Large 和从更长通话切窗训练解决。发布版在 60 s AMI 窗口将 WER 从 23.66% 
- **关键技术点**：噪声抑制保留所有人声，无法直接转写；目标说话人提取依赖注册片段，真实通话却没有干净音频。既有评测只用不超过 4 s 的背景语音，看不到他人独白后主叫回归的遗忘与主叫独处的过抑制。
- **主要指标**：- 开发集平均 WER：发布版 10.49%，无 WavLM 的 M 模型 11.44%，开源最强隔离器 11.91% - AMI 60 s 窗口 WER：16.13%，基线 23.66% - 基线自有 AMI 窗口：10.19% 对 11.71% - Krisp WER：5.74%，基线 5.63
- **代码**：https://huggingface.co/collections/Scicom-intl/voice-isolator | **Demo**：暂无

---
## [S3-S2ST: Semantically Supervised Streaming Speech-to-Speech Translation](https://arxiv.org/abs/2610.36777)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-28
- **一句话贡献**：针对流式语音到语音翻译（S2ST）"何时该commit译文"的决策难题，本文提出S3-S2ST：将句级平行语音对改造为"语义单元+640ms栅格"的增量监督数据，在Thinker–Talker架构上同时学习翻译内容与发射时机；READ/WRITE门控阈值可在推理时调节质量–延迟权衡，配合播放缓冲自适应阈值无需重训。4B稠密模型离线FLEURS达COMET 0.904与Qwen3-Omni（30B/
- **关键技术点**：流式S2ST必须决定等待多少源语音再翻译：过早会误译，而已播出的语音无法像文本那样被静默修正；句级平行语料只给最终译文，缺失"哪个源前缀支持哪个目标片段"的监督。SimulS2ST-Omni等靠改变输入chunk时长获得延迟档位，把决策频率与输入粒度耦合在一起。
- **主要指标**：- 流式FLEURS（τ=0.5）：COMET 0.828、BLEU 29.83、ASR-COMET 0.769、SIM 0.606、UTMOS 3.75 - 流式9-pair：COMET 0.965、BLEU 60.51、ASR-COMET 0.933、WER 1.54 - 离线FLEURS：BL
- **代码**：暂无 | **Demo**：暂无

---
## [EmbeddingGemma 2: Unified and Efficient Multimodal Representations](https://arxiv.org/abs/2610.37364)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-10-28
- **一句话贡献**：Google发布744M参数开源多模态嵌入模型EmbeddingGemma 2，解决文本嵌入模型处理音视频需ASR/描述器等外挂、而MLLM系多模态嵌入模型动辄数十亿参数难以端侧部署的问题。模型以271M双向Transformer为骨干，配167M ViT视觉编码器与305M Conformer音频编码器，将文本、图像、音频、视频及任意交错混合输入统一映射到768维空间，经"蒸馏→对比"渐进课程训
- **关键技术点**：CLIP/SigLIP类双塔模型无法原生处理混合模态输入；由MLLM改造的嵌入模型规模偏大，不适合低时延、高吞吐与端侧隐私场景；ASR级联文本嵌入的管线丢失非语言声与环境声等副语言信号。
- **主要指标**：- MTEB(Code) 78.68，超全部sub-4B模型；MTEB(多语) 61.36、较EG1 +0.21 - MMEB-v2 59.01（仅用439M参数），比986M的jina-embed-v5-omni-nano高15.4；MIEB(lite) 60.17，较sub-1B最强+7.9 -
- **代码**：https://ai.google.dev/gemma/docs/embeddinggemma | **Demo**：暂无

---
## [Learning Timeline-Preserving Speech-to-Speech Translation](https://arxiv.org/abs/2611.00690)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-11-03
- **一句话贡献**：本文提出时间线保持（timeline-preserving）语音翻译任务：配音等场景仅对齐总时长不够，译文语音须在同一绝对时间轴上保留源话语终点与显著内部停顿。作者用源画布（source-canvas）管线构造642K条时长严格匹配的英中目标语音，训练自回归端到端模型TransDubber，采用四阶段课程学习加验证器引导强化学习。在4,353句测试集上，相对最强基线UniSS将时长误差2%内占比从
- **关键技术点**：现有S2ST系统能保语义、说话人与风格，但不控制"何时说、何时停"；TransVIP等需在推理时显式注入帧级isochrony控制，级联或后处理拉伸只能对齐全局时长而无法恢复内部停顿位置；独立录制的平行语料天然不含源时间线监督。
- **主要指标**：- Dur@2%/5%/10%：61.5%/92.2%/98.7%，UniSS为25.6%/56.1%/83.3% - 停顿对齐：F1@0.4为0.550（UniSS：0.118，其余基线≤0.080）、tIoU 0.322、SER 0.128、onMedAE 0.162s - 翻译质量：COMET
- **代码**：暂无（承诺发表后释出） | **Demo**：暂无

---
## [SPATEX: Array-Flexible Multichannel-to-Multichannel Target Speech Extraction using Direction Clue](https://arxiv.org/abs/2611.03119)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-11-03
- **一句话贡献**：现有MIMO目标语音提取（多通道输入多通道输出）系统均假设固定麦克风配置，无法跨阵型部署，而阵型灵活的单输出方法又丢弃逐麦克风空间信息。本文提出SPATEX，首个阵型灵活的MIMO TSE框架：以麦克风坐标与目标DOA为条件，通过几何感知通道交换（TAC）与共享时间联合注意力重建各麦克风的混响目标语音像，并保持排列等变性。在2–10麦克风、匹配/失配阵型下最高达15.98 dB SI-SNRi；固
- **关键技术点**：M2M-TSE、SoundCompass等MIMO TSE方法采用阵型专用架构，仅适配固定麦克风数量与几何；TAC类与FlexIO等阵型灵活方法只重建参考通道信号，无法保留目标声场的通道间关系，难以满足VR/AR等沉浸式音频的空间渲染需求。
- **主要指标**：- SI-SNRi：Matched 2–8麦14.23 dB；Unmatched 9–10麦15.98 dB（训练范围外外推） - PESQ/STOI：3.41/0.891（Matched）、3.65/0.923（Unmatched 9–10麦） - 空间保真（固定4麦）：IPD误差0.614 ra
- **代码**：https://github.com/Wenanzhi/SPATEX | **Demo**：暂无

---
## [Speech Entrainment in Multi-Party Conversations with a Digital Agent](https://arxiv.org/abs/2607.22939)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：—
- **一句话贡献**：已有广泛观察表明参与对话的个人倾向于调整说话风格以匹配对方。但之前大多数工作集中在人类之间的双人交互。本文研究一种新设置：人类群体和数字代理之间的多方交互。研究发现个体在局部上与其他人entrain，但全局entrainment以及与代理的entrainment有限且依赖于队列。
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：暂无 | **Demo**：暂无

---
## [Monaural Continuous-Radius Regional Speech Extraction with Cross-Radius Consistency Learning](https://arxiv.org/abs/2610.11507)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：—
- **一句话贡献**：（仅标题，未精读）
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：暂无 | **Demo**：暂无

---
## [Self-Supervised Speech Representations for Cross-Speaker Dysarthria Detection During Awake Craniotomy](https://arxiv.org/abs/2610.11825)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：—
- **一句话贡献**：（仅标题，未精读）
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：暂无 | **Demo**：暂无

---
## [Adaptive Perturbation Selection for Contrastive Audio Decoding](https://arxiv.org/abs/2607.00247)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-06-30
- **一句话贡献**：大音频语言模型(LALMs)常通过语言先验覆盖声学证据产生幻觉。虽然对比解码(CD)提供无需训练的缓解方法，但现有方法依赖mask或noise等粗粒度扰动，结构化音频转换未被探索。本文通过评估多样化针对性音频扰动库并自适应为每个任务和样本选择最优negative branch来探索这一设计空间。首先改进先前VCD等方法，然后提出自适应扰动选择策略。
- **关键技术点**：对比音频解码框架，包含扰动库和自适应选择器。
- **主要指标**：在多种音频语言模型任务上减少语言先验覆盖声学证据的问题，提升生成质量。
- **代码**：暂无 | **Demo**：暂无

---
## [ProPS: Prompted Profile Synthesis for Natural Language-Conditioned Speaker Embedding Distributions](https://arxiv.org/abs/2607.05276)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-06
- **一句话贡献**：说话人嵌入(x-vector)广泛应用于表示说话人身份和相关属性，但现有嵌入提取器是描述性的而非生成性的：它们将观测语音片段映射到x-vector，再用于下游应用。ProPS提出提示画像合成框架，可根据自然语言提示(如"三十多岁男性操印度口音")生成说话人嵌入分布。ProPS将人类撰写的画像描述转换为句子嵌入，使用在大规模数据集上训练的混合密度网络预测x-vector空间中的高斯混合模型。模型通过
- **关键技术点**：ProPS包含三个核心组件：(1)提示编码器：将自然语言画像描述转换为句子嵌入；(2)混合密度网络(MDN)：基于提示嵌入预测x-vector空间中的GMM参数(均值、方差、混合系数)；(3)x-vector提取器：用于评估的预训练说话人嵌入模型。
- **主要指标**：负对数似然(NLL)评估分布质量，属性分类准确率评估生成x-vector的属性保留度。实验证明ProPS能生成保留年龄、性别、口音、韵律特征的x-vector。 **应用场景** TTS(文本到语音)、VC(声音转换)的可控说话人画像合成。 ### ⭐ 评分：7/10 ProPS将生成式AI方法引入
- **代码**：暂无 | **Demo**：暂无

---
## [TriA Pipeline: A Large-Scale Automatic Audio Annotation Pipeline For Audio Classification In Specific Scenarios](https://arxiv.org/abs/2607.06179)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-07
- **一句话贡献**：大多数场景（如家庭环境）缺乏标注数据。提出TriA Pipeline，自动将各种场景音频转换为带音频事件标注的高质量训练数据。构建了TriA数据集，涵盖431个音频类、超过2130小时。划分先验知识引导的TriA_GK子集进行家庭音频分类任务对比实验。手动标注数据结合TriA_GK相比仅用手动标注数据，平均相对提升准确率3.97%，Macro-F1 3.35%。
- **关键技术点**：TriA Pipeline：自动音频标注流程，将原始音频转换为带标注的训练数据。
- **主要指标**：TriA_GK带来平均3.97%准确率相对提升，3.35% Macro-F1相对提升。
- **代码**：https://github.com/huanxian/TriA | **Demo**：暂无

---
## [Determinantal point process sampling for bioacoustic active learning](https://arxiv.org/abs/2607.06063)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-07
- **一句话贡献**：生态声学监测产生大量音频数据，主动学习可减少标注工作量同时高效训练可靠生物多样性分类器。提出CARE-DPP，一种批主动学习获取方法，结合类别平衡的预测不确定性与嵌入空间新颖性，DPP目标选择高质量非冗余获取批次。不确定性-新颖性平衡随标注预算退火：早期强调几何覆盖，后期越来越多利用分类器不确定性。评估在BirdSet HSN、POW、UHH和ATBFL上，Macro mAP的AULC达0.50 
- **关键技术点**：CARE-DPP：类别平衡不确定性 + 嵌入空间新颖性 + DPP批次选择。
- **主要指标**：Macro mAP的AULC达0.50 vs CoreSet基线0.46。
- **代码**：暂无 | **Demo**：暂无

---
## [Few-Shot Class-Incremental Audio Classification Using Pseudo-Incrementally Trained Embedding Learner and Continually Updated Stochastic Classifier](https://arxiv.org/abs/2607.05953)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-07
- **一句话贡献**：少样本类别增量音频分类（FCAC）需要逐步识别增量类（少标签样本）同时记忆基类。模型需兼具高稳定性（记忆基类）和强可塑性（适应增量类）。设计解耦为两个独立模块：嵌入学习器（残差卷积网络骨干）和随机分类器（每类由均值和方差向量组成的分布）。基会话训练后，嵌入学习器不再更新以记忆基类知识，通过伪增量训练策略保持增量类表示能力；随机分类器在每个增量会话更新以适应新类。在FSC-89、NSynth-100
- **关键技术点**：嵌入学习器（冻结）+ 随机分类器（持续更新）。伪增量训练策略保持嵌入学习器的表示能力。
- **主要指标**：准确率超越比较方法，计算复杂度低于大多数比较方法。
- **代码**：https://github.com/vinceasvp/PITEL-CUSC | **Demo**：暂无

---
## [InfluMatch: Frontier-Quality KOL Search at 4B-Model Cost](https://arxiv.org/abs/2607.05968)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-07
- **一句话贡献**：KOL（关键意见领袖）匹配当前依赖关键词搜索（丢失语义）或提示前沿LLM处理每个候选（准确但慢且贵）。提出InfluMatch，低成本三阶段级联——检索→重排→推理——完全基于小规模开源模型：密集检索返回50候选，4B逐点评分重排器对每个候选打分取前10，4B推理器按 rubric 评估短名单。端到端在11-query、50-KOL标签集上达94.1% P@5，匹配前沿模型Kimi-K2.6（91
- **关键技术点**：三阶段级联：密集检索 + 4B逐点重排 + 4B推理评分。
- **主要指标**：94.1% P@5匹配Kimi-K2.6（91.8%），约35倍更少输出token，约20秒/A100。
- **代码**：暂无 | **Demo**：暂无

---
## [When Does Tool Use Increase the Expressive Power of Finite-Precision Recurrent Models?](https://arxiv.org/abs/2607.06155)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-07
- **一句话贡献**：现代序列模型作为代理部署时将token生成与外部工具调用交错。本文给出工具访问何时增加计算表达性的精确架构级描述。将任何固定有限精度循环序列模型（包括B位内部状态的有限精度SSM）建模为通过有限命令/观察接口与oracle交互的确定性有限状态控制器。结果形成尖锐二分法：有限状态工具本质上不增加表达能力；单个最小无限状态工具（图灵机磁带）使系统图灵完备；一阶层有限精度选择性仿射SSM控制器（含二元o
- **关键技术点**：有限精度循环序列模型 + 工具oracle接口。
- **主要指标**：揭示EQ_n需要2^n状态但带工具的单常规模控制器可模拟，指数级分离。
- **代码**：暂无 | **Demo**：暂无

---
## [Local Multimodal Music Alignment from Global Supervision](https://arxiv.org/abs/2607.10023)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-10
- **一句话贡献**：理解音乐需要理解数据模态之间的局部对应关系，例如表演音频中的时间如何映射到乐谱图像中的位置。然而，获取这类局部对应的监督信号很困难——实践中通常只有更粗粒度的全局监督（如配对的音频和图像片段）。本文提出FuSiLi（Fused Sinkhorn-Localized Similarity），一种用于多模态对比学习的相似度分数，通过基于Sinkhorn的软对齐直接在局部图像块和音频帧特征上操作。
- **关键技术点**：微调预训练的CLIP图像编码器和CLAP音频编码器。使用ViT图像编码器和LAION-CLAP HTSAT音频编码器。
- **主要指标**：在局部对齐任务上，FuSiLi达到30% top-1准确率，相比全局基线的16%几乎翻倍。点&检索任务上，I2A方向提升超过10倍（13.91% vs 1.33%）。全局检索保持竞争力（PDMX上MRR约0.83-0.86）。
- **代码**：https://github.com/irmakbky/fusili | **Demo**：https://irmakbky.github.io/fusili/

---
## [Hybrid Continual Learning for Low-Resource Australian Aboriginal Language Identification](https://arxiv.org/abs/2607.11946)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-11
- **一句话贡献**：本文针对濒危澳大利亚原住民语言（AAL）的语言识别问题提出混合持续学习方法。极端数据稀缺限制模型性能，从高资源语言迁移学习存在灾难性遗忘问题。提出两种混合持续学习方法：Replay Augmented Elastic Weight Consolidation和Constraint Guided Knowledge Distillation。
- **关键技术点**：基于预训练语音模型（如wav2vec2）的语言识别系统。
- **主要指标**：提出的方法优于简单微调和现有CL基线，在多AAL适应和高资源语言保持两方面同时提升。
- **代码**：https://github.com/PraviMyl/AAL | **Demo**：暂无

---
## [Qwen-Audio-VAE Technical Report](https://arxiv.org/abs/2607.11738)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-13
- **一句话贡献**：Qwen-Audio-VAE是一套低比特率、快速编码的连续音频自编码器，专为可扩展的通用音频生成设计。核心原则是音频VAE不仅要以高保真度重建多样化音频，还要产生足够紧凑的潜在表示以支持大规模文本到音频训练。模型结合因果编码器-解码器、窗口Transformer块和多判别器训练，在重建质量和压缩率之间取得良好平衡。
- **关键技术点**：因果编码器-解码器结合窗口Transformer块，多判别器训练。训练于500万小时多域音频。
- **主要指标**：跨不同音频域泛化良好，编码32分钟音频仅需541ms，实现高效率。
- **代码**：暂无 | **Demo**：暂无

---
## [Synchronized Three-Dimensional Vocal-Tract Motion for Speech Synchronization via Joint-Embedding Predictive Architecture Alignment](https://arxiv.org/abs/2607.11772)

- **方向**：语音前端（语音合成） | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-13
- **一句话贡献**：现代神经语音系统可以生成可理解的波形，但通常隐藏了产生声音的物理语音产生状态。相反，生物力学声带模型暴露了发音结构、接触行为、气流路由和几何约束，但直接物理波形合成不如现代神经声码器鲁棒。本文提出一种JEPA风格表示和RL/CEM轨迹选择循环，将发音动作与声学载体和物理可信度约束对齐。评估包含12个3D录制覆盖24个最小对刺激。在24词集上，载体获得良好ASR结果（8.33% WER，4.17% 
- **关键技术点**：JEPA风格表示学习结合生物力学声带模型，时频对齐发音动作与声学载体。
- **主要指标**：ASR WER 8.33%，CER 4.17%，显示良好的可理解性。UTMOS 3.174，平均JEPA分数0.864， timbre-guard分数0.947。发音动作与声学载体的同步精度验证。
- **代码**：暂无 | **Demo**：暂无

---
## [Semantic Sampling via Learnable Observation Front Ends](https://arxiv.org/abs/2607.11260)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-13
- **一句话贡献**：采样决定了重建系统可用信息的形式。传统低速率采样直接从原始波形形成有限维观测，采样规则主要由带宽、稀疏性或固定信号级结构指导。然而，对于语音等声学信号，重建相关信息通常通过内容相关的谱时结构而非仅通过波形样本表达。本研究提出通过可学习观测前端的语义采样。
- **关键技术点**：（仅标题，未精读）
- **主要指标**：在相同观测预算下，语义采样前端提供比固定低速率采样和基于预定低速率波形的神经恢复方法更信息丰富的观测。波形保真度、谱一致性和感知质量的改善表明可学习前端在相同观测预算下保留了更多有用信息。
- **代码**：暂无 | **Demo**：暂无

---
## [Self-supervised Speech Comparison for L2 Phone, Rhythm, and Intonation Scoring](https://arxiv.org/abs/2607.13721)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-15
- **一句话贡献**：L2语音评估传统上专注于音素评估，留下韵律和语调等超音段特征的评分未被探索。此外，评估方法通常需要带标签的L2语音数据进行训练，使它们难以应用于低资源环境。本研究探索DTW过WavLM自监督表示是否可提供无需文本的框架来评估英语和日语L2语音的音素准确度、韵律和语调。
- **关键技术点**：（仅标题，未精读）
- **主要指标**：音素评分超过人类一致性，韵律评分接近人类水平，语调评分在某些任务上仍较温和。
- **代码**：暂无 | **Demo**：暂无

---
## [SceneBind: Binding What and Where Across Vision, Audio and Language](https://arxiv.org/abs/2607.15265)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-16
- **一句话贡献**：现有全模态编码器在实例级语义方面表现出色，但通常缺乏显式的空间结构。SceneBind通过将每个场景表示为结合全局语义嵌入与对象中心语义-空间槽的语义-空间实体来解决这一差距。该表示显式捕捉对象级语义、空间属性和不确定性。
- **关键技术点**：语义-空间实体表示，结合全局语义嵌入与对象中心语义-空间槽。
- **主要指标**：实现最先进的场景和空间检索，同时支持强零样本迁移到下游任务如音频-视觉定位。
- **代码**：暂无 | **Demo**：https://scenebind.github.io/

---
## [Layer-Wise Decision Fusion for Fake Audio Detection Using XLS-R](https://arxiv.org/abs/2607.20023)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-22
- **一句话贡献**：近期伪造音频检测方法利用大型语音模型获取稳健语音表示。这些模型通常非常深，提供多层表示。然而，现有工作通常仅依赖单层表示或特征融合提取 utterance 级表示进行决策，存在信息利用不足和特征崩溃风险。本文提出新型层-wise决策融合方法，在每层决策后进行融合，在In-the-Wild数据集上实现最佳跨数据集性能（EER 6.90%）。
- **关键技术点**：基于XLS-R的深度模型，多层表示决策融合。
- **主要指标**：EER 6.90%，跨数据集性能最佳。
- **代码**：暂无 | **Demo**：暂无

---
## [Music-JEPA: Learning a World Model of Sound from Action](https://arxiv.org/abs/2607.22000)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-24
- **一句话贡献**：联合嵌入预测架构（JEPA）已成为通过预测潜在表示来学习世界模型的新范式。本文提出Music-JEPA，将音乐建模为动作条件系统：音频作为状态，钢琴卷作为乐器动作。给定当前音频状态和动作，模型预测未来音频状态，模拟人类通过交互学习音乐声音的方式。
- **关键技术点**：使用Vision Transformer (ViT) backbone编码状态和动作表示。状态编码器使用12层Transformer，动作编码器使用8层。状态和动作预测器均为6层Transformer。模型参数量约19M。
- **主要指标**：在beat tracking任务上，Music-JEPA的F1为0.6208（70ms容差）和0.6599（100ms容差），优于AO-JEPA和MERT。在composer identification上，Top-3准确率70.45%，Top-5准确率87.34%。在key recognition
- **代码**：即将发布 | **Demo**：https://zzwaang.github.io/music-jepa-demo/

---
## [CODA: Cascaded Online Discontinuity-Aware Alignment for Real-Time Image-Based Score Following](https://arxiv.org/abs/2607.21899)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-24
- **一句话贡献**：实时乐谱跟踪从乐谱图像仍然具有挑战性，因为模型必须在严格延迟约束下处理流式音频同时解决高度重复的视觉模式。本文提出CODA，据我们所知是第一个解决这两个缺口的实时乐谱跟踪系统。CODA明确利用乐谱的级联结构：首先选择活动系统，然后选择活动系统内的活动小节，最后选择所选小节内的活动音符。
- **关键技术点**：因果Mamba音频编码器+共享CNN视觉主干+三个级联阶段（系统选择，小节选择、音符定位）+带学习时间先验的Beam Search。
- **主要指标**：在Setting I上，CODA在≤0.10s阈值下达0.914，而CYOLO-SB为0.837。小节准确率从0.890提升至0.975。在Setting II上，达0.743 vs 0.630。跳转恢复上，重复子集1s系统恢复率0.78，随机子集0.64。
- **代码**：https://github.com/ValleyC/CODA | **Demo**：暂无

---
## [Unfolded Recursive Expectation-Maximization Neural Network for Speaker Tracking](https://arxiv.org/abs/2607.26575)

- **方向**：说话人跟踪 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-29
- **一句话贡献**：提出深度展开的递归EM（REM）网络用于在轻度混响环境中鲁棒跟踪单个移动说话人。与依赖固定步长衰减 schedules的传统REM算法不同，架构通过将迭代过程展开为可微分层来学习自适应更新策略。引入Step Size Network，利用Feature-wise Linear Modulation (FiLM)和Positional Encoding (PE)根据时序上下文和收敛状态动态调整递归权
- **关键技术点**：（仅标题，未精读）
- **主要指标**：- 无混响（T60=0）：RMSE 0.25m vs CREM基线0.28-1.44m - 混响（T60=0.3s）：RMSE 0.55m vs CREM基线0.74-0.86m - learned γ_t在无混响时收敛到~0.25，在混响时降低到0.02-0.1
- **代码**：暂无 | **Demo**：暂无

---
## [Explicit and Stable Pseudospectral Time-Domain Method for Föppl-von Kármán Equations](https://arxiv.org/abs/2608.06139)

- **方向**：声学模拟 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-06
- **一句话贡献**：模态合成是乐器动力学模拟的常用技术，但Föppl-von Kármán板方程的非线性项导致模态域中四阶张量计算代价极高（O(N_x^4)）。本文提出伪谱时域方法：在空域网格上计算乘积项（O(N_x^2 log N_x)），在模态域中精确计算空间导数，通过离散正弦/余弦变换施简支边界条件，并利用标量辅助变量技术实现显式稳定时间积分。数值实验在44.1kHz采样率下验证了能量守恒到机器精度，且漂移调控
- **关键技术点**：Föppl-von Kármán板方程的非线性耦合由四阶张量描述，纯模态方法需要评估O(M_x^4)个耦合项，在GPU上才能实现实时。现有数值方法（Kirby & Yosibash）使用隐式迭代方案，计算效率低。
- **主要指标**：- 能量误差：保持在机器精度2.2×10⁻¹⁶量级，无长期漂移 - 漂移调控：SAV+控制项将相对漂移从~10⁻³降至~10⁻⁵（两个数量级） - 大板（ϰ=8）：1027个模态，首次激励模式下能量精确守恒 - 小板（ϰ=60）：127个模态，不同激励幅度下呈现从线性→pitch glide→宽带噪
- **代码**：https://github.com/victorzheleznov/fa2026 | **Demo**：https://victorzheleznov.github.io/fa2026

---
## [Structured Phonological Representations for Audio-Articulatory rtMRI Speech Classification](https://arxiv.org/abs/2608.09767)

- **方向**：语音大模型（语音前端） | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：实时 MRI 可以观察语音中的声道发音，但将这些发音模式映射到音系类别仍具挑战性。该工作研究 PhonoQ（一个训练识别结构音系特征的音频模型）是否为音频-发音建模提供有用信息。从 PhonoQ 的 Conformer 模块提取表示（其训练受方式、位置、发声、元音特征监督），使用发音轮廓与同步音频特征结合，对比 WavLM-large 和 HuBERT-large 基线。在未见语音和未见说话人设置
- **关键技术点**：rtMRI 提供了高时间分辨率（~80fps）的声道发音观测，但发音数据维度高、标注困难，映射到音系类别需要有效的特征表示。
- **主要指标**：- PhonoQ 特征改善音系目标 macro-F1（方式、位置、发声、元音高度、前后位置） - 改善 39 音素细粒度分类 - 仅轮廓推理：音频教师监督比仅轮廓训练有适度增益 - 后验分析：可解释的舌拍 /t/、/t/-/r/ 后缩、鼻音同化模式
- **代码**：暂无 | **Demo**：暂无

---
## [Multi-Task Learning for Non-Canonical Phoneme Recognition via Articulatory Feature Decomposition](https://arxiv.org/abs/2608.22273)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-25
- **一句话贡献**：针对病理/非标准语音中系统性的发音偏差与临床标注数据稀缺，本文将音素识别从"原子类别分类"重构为发音特征维度（manner/place/voicing/height 等）的多任务预测，提出基于 WavLM 的分层多任务（HMTL）架构，通过 cross-attention 融合发音特征表示后经 BiLSTM 与 CTC 输出音素序列。结合 Momentum Pseudo-Labeling 半监督与
- **关键技术点**：病理/非标准语音（如运动言语障碍、儿童言语失用）音素识别 PER 高达 42%-69%。现有模型在健康语音上训练，会把非标准发音"自动纠正"为最近的规范音素；且把音素当作原子标签无法刻画"部分特征保留、部分偏离"的系统性错误结构。病理语音标注稀缺且标注者间一致性差，故用 L2-ARCTIC 口音语音作为病理发音的代理。
- **主要指标**：- PER：HMTL+CA+Aug+MPL 13.47%，最强基线 WavLM+Aug+MPL 14.46%，外部 MV_multi-MT_seq 14.13% - 错误结构：voicing 错误 -10.1%、height -5.65%、backness -5.83%、roundedness -4
- **代码**：暂无 | **Demo**：暂无

---
## [LipsAM: Lipschitz-continuous Neural Networks for Convergent Plug-and-Play Audio Signal Recovery](https://arxiv.org/abs/2608.23038)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-25
- **一句话贡献**：传统语音 DNN 将复数 STFT 的幅度与相位分开处理，由于 sign 函数在零点不连续，此类网络即使幅度部分 Lipschitz 连续，整体也必然不连续，无法纳入现有 Lipschitz 理论框架。本文推导了幅度修正器（AM）满足 Lipschitz 连续性的充要条件（定义 LipsAM），并给出 LipsAM-E、LipsAM-M（时频掩蔽）两类可证连续的架构及 Lipschitz 常数紧凑
- **关键技术点**：现有 Lipschitz 网络构造（谱归一化、正则化、结构法）均针对实值图像网络；而语音常用的复数谱网络通过幅度映射加 sign(z) 分离处理幅度相位，sign(z) 在 z=0 处不连续，导致即使幅度映射本身 Lipschitz 连续，整体映射仍非 Lipschitz。这阻碍了基于 Lipschitz 条件的 PnP 收敛保证在语音中的应用。
- **主要指标**：- SI-SNR（1200次迭代后）：无约束 ReM-AM 最高，CoReM-LipsAM 因 Lipschitz 约束性能下降，但仍优于软阈值基线 - 收敛残差 Δx[k]：ReM-AM 不下降（不收敛），CoReM-LipsAM 降至约 10⁻¹² - Lipschitz 界验证：N=2 时数值
- **代码**：暂无 | **Demo**：暂无

---
## [VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction](https://arxiv.org/abs/2608.26005)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：面向实时语音交互中语音大模型（SLM）缺乏记忆的痛点，本文提出 VoiceMem"双脑流式记忆"架构，将短时工作记忆与长期记忆结合，构建了完整的记忆感知 SLM 训练、评估与部署流水线。实验显示其在记忆准确性、情感个性化与实时性上均有显著优势，为实时语音交互提供了实用的记忆基础。
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：暂无 | **Demo**：暂无

---
## [Multirate State Space Models for End-to-End Processing of Pulse Density Modulated Speech Signals](https://arxiv.org/abs/2608.28472)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：针对低功耗常开边缘设备上的SSM语音处理依赖PCM、且PDM转PCM需低通滤波与抽取带来高昂硬件开销的问题，本文提出一种仅用16kHz PCM训练、即可天然泛化到任意采样率PDM数据的端到端语音处理架构。其核心是使用FouT/LegT初始化的SSM编码层，利用其连续时间参数化特性把PCM与PDM输入映射为调制方式与采样率无关的SSM系数表示，并借助连续时间记忆窗在不做抗混叠的情况下对系数序列进行大
- **关键技术点**：PDM MEMS麦克风兼具噪声鲁棒、低成本与可变采样率（多档位）省电优点，但现有算法都要求先做PDM转PCM（级联滤波+抽取），给资源受限硬件带来开销。已有两条绕开路径均不理想：一是用CNN把滤波与抽取融合为一个输入模块，二是端到端直接喂PDM进DNN。二者共同缺陷是必须在高达2MHz级别的PDM采样率下训练，序列过长导致训练耗时且内存占用大；同时只在单一采样率上训练，无法泛化到其他OSR。其可行性依据在于：PCM与PDM在PCM奈奎斯特频率（8kHz）以下共享完全相同频谱内容。
- **主要指标**：- KWS最优：LegT（H=128, theta=8ms）在2MHz PDM测试集上准确率93.72%，优于最佳FouT（H=512, theta=32ms）的93.44%。 - KWS抽取：2MHz PDM下输出速率降至31.25Hz（抽取65,536倍），所有抽取因子下准确率下降<10%。 -
- **代码**：https://github.com/NECOTIS/ssm-speech-processing.git | **Demo**：暂无

---
## [Exploring the Design Space of Representation Learning for Audio Transformations](https://arxiv.org/abs/2608.28127)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：现有神经音频表示学习主要面向内容类任务（如检索、分类），其表征在处理类任务上能力有限；且处理感知表征究竟应编码"与源内容解耦的处理本身"还是"保留内容的处理后音频"，学界缺乏共识。本文提出统一框架，以处理一致性、描述对齐、前向预测等变三类目标在受控设置下穷举组合对比，系统揭示各目标的相对优势与交互效应；框架同时产出变换嵌入与处理后音频嵌入，二者职责互补——距离度量型任务偏好前者，探针型任务偏好后者
- **关键技术点**：既要回答"处理感知表征应捕获什么"这一表征设计问题，又要解决"模型、数据、评测各异导致无法归因行为差异"的对比公平性问题。现有方法各自隐式承诺单一表征范式，缺乏在统一条件下的系统比较。
- **主要指标**：- 检索任务：全局最优配置由变换嵌入取得 - 探针评测：处理后音频嵌入更优 - 风格迁移：完整方案相对既有基线取得一致收益 - 消融对比：三类目标全部启用优于任意子集组合
- **代码**：暂无 | **Demo**：暂无

---
## [VAANI Noise Event Dataset: A curated spontaneous speech dataset annotated with timestamps for noise events](https://arxiv.org/abs/2609.02474)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-02
- **一句话贡献**：现有音效语料要么面向通用音频标记，要么面向纯净语音分离，缺少叠加在自发性真实语音上、带时间戳的强噪声标注。VAANI Noise Event Dataset 基于 Project VAANI 在印度自发性语音现场录音，为背景噪声事件添加精确起止时间戳，构成七类语义分类法（动物、交通、婴儿/儿童、音乐、信号/报警、家电、非言语人声）。数据集含 72,756 段语音（122.17 小时、38,541 
- **关键技术点**：真实印度场景中语音与车辆、动物、婴儿等非平稳背景噪声共存，噪声起止与语音的重叠关系直接决定识别误差与增强质量。现有语料要么合成混合（WHAM!、DESED 合成子集）、仅帧/片段级弱标签（AVA-Speech、FSD50K、AudioSet）、或无噪声标注（CHiME-6）；iNoise 与 Kathbath-Noisy 虽面向印度，却分别缺少语音与噪声事件标注。
- **主要指标**：- 总规模：72,756 段 / 122.17 小时 / 38,541 位说话人 - 覆盖率：58 门语言、30 个邦、162 个地区（Hindi 占 83.9 小时为主） - 噪声事件：106,892 个时间戳事件，72,746 段含事件标注 - 质量层级：verified 11,111 段/21
- **代码**：暂无 | **Demo**：暂无

---
## [X-Pred MeanFlow for Streaming Token-to-Mel Speech Decoding](https://arxiv.org/abs/2609.12728)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-11
- **一句话贡献**：近期基于离散token的语音生成进展凸显了在流式与对话场景中高效token转波形合成的重要性。流匹配声学解码器能实现高质量的token转mel生成，但其迭代采样需要多次神经函数评估（NFE），限制了低延迟语音合成。MeanFlow通过建模时间区间内的平均速度来减少采样预算，但在极少步数下保持高音质仍具挑战。为此本文提出X-Pred MeanFlow，一种少步流式token转mel解码器，用mel空
- **关键技术点**：LLM式TTS逐步转向在离散语音表示上进行序列建模，token转声学解码直接决定感知质量、每包计算量与流式能力。条件流匹配能高质量生成但迭代采样开销大（多次NFE），在流式合成中每包须在固定播放间隔内完成，而MeanFlow虽能用平均速度减少采样步数，但极少数步下高保真token转mel生成仍难；同时全局自注意力导致流式成本随句长增长。
- **主要指标**：- 评估用100句未见说话人句子，指标UTMOS/WER/SIM（SEED-TTS官方工具）。少步质量（CFG=0）：Small X-Pred 2-NFE UTMOS 3.189/SIM 0.661/WER 6.89%，3-NFE 3.310/0.670/6.28%，10-NFE 3.464/0.6
- **代码**：暂无 | **Demo**：https://renxiaming.github.io/xpred-meanflow-stream-demo/

---
## [Building a Production Greek-English Speech Recognizer](https://arxiv.org/abs/2609.13498)

- **方向**：语音大模型（ASR） | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-11
- **一句话贡献**：本文报告为希腊语与英语混合语音构建商业级双语ASR系统Sophea的多月工程实践。系统需同时通过九项生产门禁：四个希腊语和三英语WER上限、95%语种识别下限、非语音零幻觉。在23次训练迭代后发现关键负结果：希腊噪音门禁需约1500步密集噪音暴露，而英语LID门禁最多容忍250步，两区间相差约6倍且永不重叠，单一模型无法全部通过。最终交付模型家族加路由服务层与解码端修复，集成系统Sophea AS
- **关键技术点**：希腊语音频多来自电话线、嘈杂会议室而非录音棚，且单句内希腊英混合切换，数据稀缺。固定容量双语模型面临"多语言诅咒"，其竞争本质是声学邻域而非语言数据量：加835小时纯净英语保护无济于事，而577小时噪声重叠会议英语即保住指标。
- **主要指标**：- 希腊语脏环境WER：K1单模型25.88（首次单served模型破≤26门禁） - 希腊码转换WER：三模型投票23.84 vs 单模型59.74 - 重叠语音WER：53.35降到37.87（相对降29%） - K1七清洗集平均WER：4.35；LibriSpeech test-clean 1
- **代码**：暂无 | **Demo**：https://huggingface.co/spaces/KIEFERSA/sophea-asr-k1-docs

---
## [FRAUDSkill: Structured Frozen-Weight Skill Optimization for Audio Anti-Fraud Detection](https://arxiv.org/abs/2609.18766)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-17
- **一句话贡献**：面向电话反诈的音频大模型部署须遵循"服务场景识别→欺诈判定→条件欺诈类型分类"的三级闭集决策协议，现有微调与提示方法把任务规则烧进权重或手工提示，难以随欺诈模式与标签政策演进。本文提出 FRAUDSkill：完全冻结 Qwen2-Audio-7B-Instruct，仅优化外部技能程序、路由策略与决策规则，并配合闭集标签投影、路由规范化与验证集拟合的多路选择器。在 TeleAntiFraud 上 M
- **关键技术点**：反欺诈是闭集链式决策：场景、欺诈、类型三路由互相条件依赖，上游非法输出会传导污染整条决策链。微调将标签约束隐式编码进权重、政策一变即需重训；提示法灵活但无法保证输出合法与跨路由一致。
- **主要指标**：- Macro-F1：73.50%（加权 F1：79.40%，Acc：78.72%，联合准确率：58.87%，非法输出率：1.94%） - 关键对比：较共享冻结基线 41.54% 提升 +31.96pp；优于 SkillOpt（37.67%）与 EvoSkill（39.07%），高于 SFT 参考 
- **代码**：https://anonymous.4open.science/r/FRAUDSKILL-114514 | **Demo**：暂无

---
## [Multi-Teacher Distillation for Cross-Domain Streaming Electrolaryngeal Speech Encoding](https://arxiv.org/abs/2609.18686)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-17
- **一句话贡献**：针对自监督语音表征在电喉（EL）病理域 zero-shot 性能差、EL 微调又会灾难性遗忘健康域、且基础模型过大无法端侧实时的问题，提出三阶段渐进式多教师蒸馏框架训练轻量流式内容编码器：先由冻结 mHuBERT 教师给出健康域离散音素聚类目标，再引入 EL 微调 ASR 教师的连续瓶颈特征回归，最后用 Whisper 引导的 DTW 路径做跨域对齐。最优 Mel-Conformer（21.9M）
- **关键技术点**：全喉切除患者依赖电喉发声，信号机械单调且常被设备噪声淹没。SSL 基础模型在海量健康语音上预训练，zero-shot 迁移到 EL 严重域失配；EL 微调又损害健康域表征，且 300M+ 参数非因果架构无法低延迟流式部署。
- **主要指标**：- EL WER：21.2%、EL CER：8.3%；HE WER：17.2%、CER：3.9% - 关键对比：较最强 zero-shot SSL 基线 WavLM-large（EL WER 39.3%）绝对降 18.1 点、约 46% 相对改善；距 EL 教师直接 CTC 解码（16.6%）仍受因
- **代码**：暂无 | **Demo**：暂无

---
## [Beyond EER: Multi-Dimensional Evaluation of Information Leakage in Speaker De-Identification](https://arxiv.org/abs/2609.18673)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-17
- **一句话贡献**：说话人去标识化（SDID）系统的隐私评估通常退化为单一指标——说话人验证 EER，忽略了软生物特征推断、嵌入级重识别与模板结构相似等关键泄露通道。本文提出五维整体评估框架：EER、软生物特征泄露分数（SBLS）、CMC 检索重识别、CCA/Procrustes 嵌入子空间对齐、WER 与语义相似度。在 IARPA ARTS 的 5 个 SDID 系统、约 347 万验证试次上证明各指标捕获独立的泄
- **关键技术点**：现有 SDID 评估以说话人验证 EER 为中心（VoicePrivacy 范式），但 EER 只度量一对一比对抵抗性，无法反映攻击者从匿名语音恢复性别、年龄、口音，或在嵌入库中检索原始说话人、从匿名表示线性预测原始表示的能力，威胁不可链接性与不可逆性；且隐私必须与可用性联合量化。
- **主要指标**：- oaoa EER：PHORTRESS 49.79% 最优，SHADOW 45.40%，VOXLET 仅 27.75% - SBLS（性别+年龄）：PHORTRESS 0.920 > 基线 0.877 > VOXLET 0.728 > RASP 0.617 > SHADOW 0.593（原始语音 
- **代码**：暂无 | **Demo**：暂无

---
## [PersianVox: A Prosody-Aware Approach for Speech Dataset Generation from In-the-Wild Data](https://arxiv.org/abs/2609.19324)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-18
- **一句话贡献**：针对低资源语言缺少大规模高保真语音数据、现成 in-the-wild 流水线用单模型 ASR 加静音 VAD 切分导致转写错误与韵律截断的问题，提出全自动数据生成流水线 PersianVox。核心是韵律感知切分（声学轮次检测+目标时长动态合并）与无真值的 dual-ASR 一致性过滤。最终从 6180 小时原始音频产出 2408.67 小时、625192 句、3248 说话人的当前最大开源波斯语数
- **关键技术点**：零样本 TTS 受限于数据规模与质量：对齐法需逐字稿难扩展，Emilia/AutoPrep 类流水线依赖强 ASR 且用静音阈值切分，产生大量句中截断短句、破坏长程韵律；DNSMOS 在波斯语上泛化差不可靠。
- **主要指标**：- TTS 合成 WER：2.1；CER：0.3；说话人 SECS：79.8 - 合成 MOS（SCOREQ）：4.27（参考真值 4.31） - SQA 相关性 PLCC/SRCC：SCOREQ 0.6658/0.6271，较最强基线 DNSMOS（0.5590/0.5182）提升约 0.107 
- **代码**：https://huggingface.co/datasets/saeedzou/persianvox | **Demo**：https://saeedzou.github.io/persianvox-demo

---
## [Model-Agnostic and Language-Agnostic Voice Pipeline Improvement for the Agriculture Domain](https://arxiv.org/abs/2609.20504)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-18
- **一句话贡献**：针对小农户田间录音（廉价手机、农机噪声、旁帮说话人、密集成语农业词）下通用 ASR 转写差、且错误集中在改变语义的核心词的问题，提出包裹零改动 ASR 的五模块流水线：信号特征门控的 DeepFilterNet3 增强、说话人分离与目标人选择、可替换 ASR、加权农词词典规则修复、质量门控。在 Hindi/Telugu/Odia 人工标注语料上，完整流水线对三个云端 ASR 降低相对 WER 16
- **关键技术点**：通用 ASR 在低信噪比、多说话人、语言混合的田间音频上严重劣化，且 WER 对内容词与功能词一视同仁，无法暴露作物/农药/剂量类词错误改变提问的危险；微调 ASR 与端到端多模态路线分别受限于标注不可靠、成本与可测性。
- **主要指标**：- 全语料相对 WER 降幅：Gemini −22.8%（0.439→0.339）、Sarvam −19.3%、Azure −16%、端侧 IndicConformer −4.9% - 多说话人相对降幅：云端 −32%～−42%、端侧约 −16% - 分离 DER：微调 segmenter 0.21
- **代码**：https://github.com/aakashdg/agri-voice-pipeline | **Demo**：https://huggingface.co/spaces/DigiGreen/farmerchat-voice-pipeline-demo

---
## [A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound](https://arxiv.org/abs/2609.20595)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-18
- **一句话贡献**：人类听觉计算模型通常只针对单一通路阶段或范式，难以跨神经时间尺度整合发现。本文提出人脑听觉电生理"基础模型"：完全因果的编码器—解码器网络，将双耳原始声波形端到端映射为高采样率连续 EEG，在 92 名被试、约 250 小时数据（纯音、语音、音乐）上训练。固定权重、零微调下，模型重现了 pABR 的刺激率/频率效应、自然语音皮层下与皮层 TRF 以及双耳交互成分（BIC 潜伏期 6.40 ms）；
- **关键技术点**：传统手工听觉模型只覆盖单阶段单时间尺度，难以扩展至多神经发生器；已有数据驱动模型要么只瞄准单一通路环节、依赖动物侵入式记录，要么建模行为而非脑响应。
- **主要指标**：- pABR 模型—人类总均值 Pearson 相关：0.604–0.944（500 Hz–8 kHz） - 皮层下/皮层语音 TRF 相关：0.39–0.93；率—幅曲线相关 ≥0.961 - 预测 BIC 潜伏期 6.40 ms（文献规范 5.58–6.90 ms 内）；幅值超规范但 Crawf
- **代码**：暂无 | **Demo**：暂无

---
## [Online Algorithms for Independent Low-Rank Matrix Analysis and Rank-Constrained Spatial Covariance Matrix Estimation Based on Maximum Weighted Likelihood Estimation](https://arxiv.org/abs/2609.21180)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-18
- **一句话贡献**：扩散噪声下的实时多通道目标语音提取问题：此前块批式B-RCSCME假设批内空间特性平稳，说话人移动时性能骤降。本文将最大加权似然估计（MWLE）引入NSR-ILRMA与RCSCME，推导逐帧在线更新算法，并配套稳定化与加速技巧。仿真实验（JVS语音+DEMAND噪声+镜像法混响，T60约346毫秒）与东京大学实测录音中，所提O-RCSCME在全部六种噪声条件下SDR/SIR改善均优于O-IVA、O
- **关键技术点**：离线最先进的RCSCME类方法（ILRMA/NSR-ILRMA前端加秩约束空间协方差估计后端）在扩散噪声下提取精度最高，但整流程难以在STFT移位长度内完成；已有块批实现B-RCSCME依赖批内空间平稳假设，且RCSCME初始化含 Moore-Penrose 伪逆等高开销矩阵运算，无法跟踪目标说话人移动。
- **主要指标**：- 平稳仿真：O-RCSCME六种噪声下SDR/SIR全面领先四个基线；与潜在离线上界Potential差距小于1分贝SDR - 在线NSR-ILRMA单评：比块批B-NSR-ILRMA后期SDR改善高约2分贝 - 消融：Online-Online组合最优；在线RCSCME比块批版每帧最大处理时间少
- **代码**：暂无 | **Demo**：暂无

---
## [All I Hear is Noise: Investigating Clever Hans Effects in Clinical Speech Datasets](https://arxiv.org/abs/2609.21080)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-21
- **一句话贡献**：既有发现在 Pitt 语料上仅用静默段即达到 Alzheimer 检测近 100% 准确率，引发对临床语音数据集捷径学习的担忧。本文对五个主流健康语音语料（DAIC-WoZ 抑郁、TORGO 构音障碍、Neurovoz 与 MDVR-KCL 帕金森、UCLASS 口吃）系统审计：对比仅首秒音频、VAD 非语音静默段、全音频在 eGeMAPS、Compare16、wav2vec 2.0 三种表征及原
- **关键技术点**：临床语音语料采集条件异质（麦克风、环境、预处理流程不一），诊断标签可能与非临床因素产生虚假相关，模型借此捷径即可获得高分；除 Pitt 外该现象是否跨语料普遍存在尚不清楚。
- **主要指标**：- TORGO：全音频 F1 0.72-0.87，静默段 0.82-0.90，去噪首秒 0.91（文献基线 0.98） - UCLASS：全音频 0.76-0.85，静默段最高 0.89，场地推断 F1 0.89 - DAIC-WoZ：首秒/全音频/静默三种条件几乎无差（0.66-0.75） - 仅
- **代码**：暂无 | **Demo**：暂无

---
## [I'll Keep an Ear Out: Teaching AudioLLMs Proactive Audio Assistance](https://arxiv.org/abs/2609.21183)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-21
- **一句话贡献**：现有AudioLLM只能被动应答查询，无法持续监听并在恰当时机主动提醒。本文提出"主动音频辅助"新任务，面向听障用户可穿戴场景，设计模型无关的ISM范式：在LLM解码词表中嵌入特殊token实现四状态主动决策。基于Qwen2-Audio-7B训练后，ESC-50上打断F1达99.6%、去重召回100%；零样本迁移Epic-Sounds取得最高打断F1 67.5，流式平均延迟3.5秒。
- **关键技术点**：传统声音感知系统按固定类别持续报警，不含用户意图与交互历史，导致同一持续事件反复提示造成"通知疲劳"。主动辅助要求模型仅凭一条watch-out意图，对流式音频逐步因果判断何时打断、何时静默，且须满足实时延迟约束。
- **主要指标**：- ESC-50：打断F1 99.6%、打断精确率99.4%、S2去重召回100%、R_I1 99.8%；reactive分类准确率94.7%，与PANN持平、逼近AST 95.7%；零样本基线S2召回仅0.2%（肯定偏置）、reactive SFT的S2仅10.1% - Epic-Sounds零样
- **代码**：暂无 | **Demo**：暂无

---
## [Reusing Latent Speech Representations for Query-Conditioned Topic Localization in Transcripts](https://arxiv.org/abs/2609.21844)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-21
- **一句话贡献**：针对语音长转录输入下游 NLP 系统低效且含大量无关上下文的问题，本文研究"查询条件化主题定位"：给定主题标题作查询，预测转录中最佳对应句子跨度。方法将冻结的 Whisper large-v3 顶层编码器状态按句子对齐区间池化为句级声学表示，与文本句嵌入门控融合后输入 VSLNet 与 QMSum-Pointer 两类定位头。Euronews 上 VSLNet 的 EM 从 45.26 升至 69
- **关键技术点**：长转录直接输入检索、问答与摘要管线时注意力开销随长度二次增长且易"丢失中间信息"，而固定窗口切分与查询无关的主题分段均无法对齐用户信息需求。现有跨度定位以文本/视觉为主，弃用了停顿、韵律、说话人与场景切换等可标示主题边界的声学线索，而这些线索天然存在于语音链路必经的 ASR 编码器内部状态中。
- **主要指标**：- EM 与 R@1（IoU≥0.7/0.5/0.3）：VSLNet 在 Euronews 上 T+A 达 EM 69.11、R@1@0.5 79.66，YTSeg 达 EM 20.56、R@1@0.5 48.63，双数据集双定位头均最优。 - 与文本-only 基线差值：Euronews EM +
- **代码**：https://github.com/steffrs/speech-topic-localization | **Demo**：暂无

---
## [Per-Aetiology Contrastive Severity Embeddings with Phonological Pseudo-Labelling for Multilingual Dysarthric Speech](https://arxiv.org/abs/2609.21789)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-21
- **一句话贡献**：多病因构音障碍严重度系统常把所有病因混入单一标签空间，本文首次在架构、配方、评测全对齐条件下检验该"混合假设"：同一 HuBERT-base 骨干与三阶段对比训练，分别训练 CP、PD、ALS 病因专属模型与混合基线，并用免训练音系 d-prime 伪标签扩充少数严重度类。说话人不相交、泄漏过滤的留出测试上，分病因模型全面胜出：CP macro F1 0.829 对 0.676（相对 +22.6%
- **关键技术点**：CP、PD、ALS 的临床量表数值语义不可互换，音系退化模式亦不同：PD 少动型晚期才丢辅音对比，CP 痉挛型早期即崩解 stridency 与发音方式对比。SpICE 等大模型隐含假设严重度是跨病因单一可学习构念，从未受控验证。
- **主要指标**：- CP：macro F1 0.829（准确率 88.5%）对混合 0.676，差 +0.153（+22.6%） - PD：0.715 对 0.511（+40.0%）；ALS：0.788 对 0.596（+32.3%），mild/moderate/severe 逐类同升 - 伪标签消融：CP 纯临床
- **代码**：暂无（录用后开源） | **Demo**：暂无

---
## [Partial Accent-Control Editing in Frozen Speech Representations for Accent Conversion](https://arxiv.org/abs/2609.22031)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-21
- **一句话贡献**：口音转换系统多依赖训练生成器，转换强度在推理时不可控。本文提出 PACE：一种免生成器训练的口音转换框架，在冻结 WavLM 第6层1024维表征上做局部编辑——先用非平衡最优传输估计目标口音参考并沿口音预测子空间加性更新源特征，再在目标口音参考库上 top-k 检索并按权重 γ 受控融合。在 L2-ARCTIC 5000 对跨口音协议下，默认工作点口音分类器准确率 39.0%（DART 28.2
- **关键技术点**：口音转换需在保留语言内容与说话人属性的同时使语音贴近目标口音。现有方法以训练好的生成模型为主，口音修改强度由模型或条件输入固化，推理时无法调节，难以量化"口音强度—源保持"的折中。
- **主要指标**：- 默认 PACE：WER 16.0%、CER 8.3%、STOI 0.802、SECS 0.583、准确率 39.0% - γ 从 0.3 到 0.7：准确率 10.6%→39.0%，WER 12.9%→16.0%，SECS 0.770→0.583 - 关键对比：较最强基线 DART 准确率 +1
- **代码**：暂无 | **Demo**：暂无

---
## [Qwen-Audio-Agent Technical Report](https://arxiv.org/abs/2609.25195)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-23
- **一句话贡献**：全双工语音Agent需在任务执行期间保持对话连贯：用户常在搜索进行中修改请求、在交易过程中补充约束，打断语音不应隐式取消任务，任务完成也需等待合适时机交付结果。本文提出Qwen-Audio-Agent，一个前台-后台异步协调运行时（harness）：Frontend Agent维持全双工对话，经spawn_thinking委托Backend Agent在独立上下文执行多步任务，Orchestrat
- **关键技术点**：（仅标题，未精读）
- **主要指标**：- 任务成功率：91.04%（混合执行），较全委托80.60%高10.44pp、较直接调用72.39%高18.65pp，并超最强基线文本后端直连90.30%达0.74pp - 工具F1：0.962（音频方案最高，文本基线0.963） - 参数准确率：95.2%，全配置最高 - 回复质量：97.8（仅
- **代码**：https://github.com/QwenAudio/qwen-audio-agent | **Demo**：暂无

---
## [Spoken Language Models that Think Aloud](https://arxiv.org/abs/2609.26488)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-23
- **一句话贡献**：思维链推理显著提升了语言模型能力，但语音模型若沿用串行"先想后说"范式，复杂问题会产生十余秒无masked静默，破坏实时对话节奏。本文在Thinker-Talker架构下提出异步想-说双stream框架：主推理stream在后台进行文本演绎，轻量think-aloud stream根据用户输入与演化的推理状态生成短句进度反馈，运行时由动态平衡策略协调两stream，检测到静默则增补语音、答案就绪则
- **关键技术点**：现有推理型语音模型先生成完整文本推理链再合成语音，推理耗时完全暴露为用户可听静默（实测12.82秒），导致系统显得无响应、话轮断裂；而通用填充语只能掩盖开头一小段，且不提供任务相关信息，难以覆盖长推理区间。
- **主要指标**：- 无masked静默时长Lsil：串行CoT基线12.82s → 完整模型0.36s（40 tok/s），缩减约97% - 表达计算开销Loh：无动态平衡策略时19.92s → 完整模型4.34s - Spoken-MQA准确率：本模型91.6（单步）/83.6（多步），平均87.6 vs 串行C
- **代码**：暂无 ｜ Demo：暂无 | **Demo**：暂无

---
## [Beyond Short Segments : Expanding Speaker Embeddings with Vector Archives](https://arxiv.org/abs/2609.25007)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-23
- **一句话贡献**：针对 SOTA 说话人验证（SV）系统在短语音上性能急剧退化的问题，本文提出 VAM-ECAPA。其核心是 TVAMSP 模块：将信息稀缺的短语音帧级特征映射到一组可学习的"向量档案"（Vector Archive，长语音特征空间的规范化原型库），无需额外推理输入即可恢复缺失的说话人判别信息。在 VoxCeleb1 的 1 秒测试段上，EER 由基线 18.437% 降至 8.334%，相对错误率
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：https://github.com/slp-lab-research/vam_ecapa | **Demo**：暂无

---
## [Narrowband Voice Communication Using Streaming Neural Compression](https://arxiv.org/abs/2609.25379)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-23
- **一句话贡献**：TinyCall 是马里兰大学提出的面向边缘设备的轻量流式神经语音编解码器，码率低至 2.3 kbps，目标在 ESP32 级 MCU 与树莓派上实时运行，服务应急信标、穿戴设备等带宽受限场景。其以 RFSQ 残差有限标量量化替代 RVQ，消除码本最近邻搜索，把量化开销降到实时预算内；以伪前瞻解码与解码器输入缓存将因果训练的 iSTFT 声码器转换为严格流式推理，仅引入一帧 20 ms 算法延迟。
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：暂无 | **Demo**：暂无

---
## [Perception-Inspired Bayesian Causal Fusion for Audiovisual Source Localization](https://arxiv.org/abs/2609.36441)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-30
- **一句话贡献**：多模态融合只有在模态共享同一因果来源时才有益；声源被遮挡或位于视野外时，视觉通道与目标条件独立，盲目融合只会污染估计。本文将"是否融合"的决策建模为贝叶斯因果推断，借鉴人类多感知最优观察者模型（Körding 等），在冻结的音频与视觉模型之上实现即插即用的因果门控层，用于声事件定位与检测（SELD）。模型先对可见候选物体推断共因后验，再按该后验对精度加权融合进行门控。实验显示无条件融合使方向误差翻
- **关键技术点**：（仅标题，未精读）
- **主要指标**：（仅标题，未精读）
- **代码**：未开源（依赖公开的 DCASE2025 SELD 基线 checkpoints、DCASE2024 ngcc-seld 模型与 Grounding DINO） | **Demo**：无

---
## [Voice Anonymization Made Simple: Training-Free Anonymization with Projected Classifier-Free Guidance](https://arxiv.org/abs/2610.08276)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-07
- **一句话贡献**：针对语音匿名化普遍依赖专门训练的问题，本文提出基于预训练流匹配语音转换系统 Seed-VC v2 的两阶段免训练匿名化方法。第一阶段在条件构造时用随机说话人上下文重新生成源内容 token，削弱表征中残留的源说话人信息；第二阶段在语音生成时用源语音估计与原说话人对应的生成方向，通过投射式无分类器引导（Projected CFG）抑制 token 引导中与源音色对齐的分量，同时保留内容引导。全程仅修
- **关键技术点**：：语音匿名化需在隐藏说话人身份的同时保留语言内容与情感。现有方法（共振峰等信号处理、ASR+TTS 重合成、解耦表征合成、扩散/流匹配匿名化如 DiffAnon、F3-VA）大多需要匿名化专项训练或额外可学习模块，更换基座模型即需重训。核心问题：能否仅改变预训练流匹配 VC 模型的推理过程使其变成匿名化器？ **方法**：Stage 1（条件构造）：源窄带 token 提供语言序列，改以随机采样目标的窄带/宽带 token 作 AR 上下文与前缀，重新生成宽带 token 条件 mu_AR；为保持 prompt 对齐，token 提示 mu_prm、Mel 声学提示 p 与 CAM++ 风格嵌
- **主要指标**：（仅标题，未精读）
- **代码**：https://github.com/xs125-stack/voice_anon_simple | **Demo**：暂无

---
## [PEDBench: Can Speech Models Detect Phonetic Errors?](https://arxiv.org/abs/2610.20830)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-14
- **一句话贡献**：语音错误检测（PED）是识字教育与临床言语病理评估的关键，但因高质量评测数据缺乏、标注不一致，SOTA语音模型能否可靠检测音素级错误一直不明。本文提出首个PED基准PEDBench，数据跨自然到受控连续谱：真实儿童朗读错误（N=334）、演员脚本化错误（N=1,188）、音素可控TTS合成的含错语音（N=1,083），全部由两名语音学训练标注者核验，并提出要求"检测对且诊断对"的诊断加权P/R/F
- **关键技术点**：现有PED/MDD研究碎片化：公开数据集人工音素标注不一致（作者标注员复标100句，与原标注F1仅42.25/66.22）；SOTA音素识别模型与语音-语言模型（SLM）从未被系统评测PED；常用PER/PFER与MDD的P/R/F1无法刻画检测+诊断的真实能力。
- **主要指标**：- L2-ARCTIC F1最高基线仅W2V2P-XLSR53的31.85；CMU-Kids最高ZIPA-CTC-NS 54.55（其PFER虽低至7.86但F1差，PFER不反映PED） - 新型集最佳基线：儿童59.51（BabAR）、acted 76.17（GPT-Audio-1.5）、syn
- **代码**：暂无（承诺录用后开源代码与acted/synthetic数据集） | **Demo**：暂无

---
## [ACR-Net: Mitigating Semantic Dominance via Contrastive Acoustic-Semantic Decoupling](https://arxiv.org/abs/2610.20114)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-15
- **一句话贡献**：针对语音情绪识别与语音LLM在语调与文本语义冲突时盲目信任文本的"语义主导"现象，本文用EmotiVoice对抗合成配对冲突语音构建ASPIRE基准，并提出SOP与LDD两指标量化文本过自信与潜层纠缠。ACR-Net以冻结Whisper双流加LoRA为骨干，经跨模态注意力定位冲突后，用对比解耦损失将矛盾表征投影至正交潜空间。结果显示现有模型在极性冲突下近乎失效（ACC低于45%、SOP高于0.5）
- **关键技术点**：多模态SER与Audio LLM在音义一致语料反复训练后形成僵化语义先验，文本token的低方差语义捷径压制细微声学线索，标准情感集筛除不一致样本更甚。已有缓解手段仅做融合层重加权、移动决策边界，无法恢复已塌缩的声学表征。
- **主要指标**：- ASPIRE总体ACC：76.5%，较MCR（48.5%）绝对提升28.0个百分点，高于Tensor Fusion（43.8%）与朴素拼接（41.2%） - SOP：0.128（MCR为0.628、朴素拼接0.824） - LDD：0.864（MCR为0.242），四类冲突下均超0.812 - 
- **代码**：https://github.com/zmkshakespar/ACR-Net | **Demo**：暂无

---
## [High-Order Sinusoidal Modeling for Precise Parameter Refinement](https://arxiv.org/abs/2610.21643)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-15
- **一句话贡献**：针对正弦建模中初始频率失配导致准谐波模型（QHM/aQHM/eaQHM）幅度、频率、相位估计精度受限的问题，本文揭示QHM复斜率幅度模型仅是失配项e^{i2πηt}的一阶泰勒逼近，阶数不足是其误差根源。据此提出高阶正弦模型（High-Order SM），将失配项展开为N阶泰勒级数并以两个复系数(a_k,b_k)强制保持指数结构，用Levenberg–Marquardt算法做非线性最小二乘估计。仿真
- **关键技术点**：信号参数提取精度受限于频率估计误差，谱图类方法受不确定性原理约束；QHM家族虽可在帧内用复幅度斜率修正频率失配，但其线性模型结构只能捕捉一阶失配，初始频率误差大时估计振荡甚至放大误差，且迭代式修正计算量大、对加性噪声敏感。
- **主要指标**：- 仿真Case1（μ=50Hz）：4th-SM幅度RMSE 0.5–10.5（对比QHM 11.6–26.7），频率RMSE 0.2–3.9×10⁻³（对比QHM最高99.3×10⁻³），重建SRER 38.8dB为最高；噪声场景SNR15dB下4th-SM SRER 24.5dB，eaQHM因噪
- **代码**：暂无 | **Demo**：暂无

---
## [Flash RNN-T: Memory-Efficient Joint Network and Transducer Loss Computation](https://arxiv.org/abs/2610.23409)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-19
- **一句话贡献**：RNN-T仍是流式ASR的主流模型，但其非线性联合网络需在T(U+1)个对齐位置计算隐状态与全词表logits，这些中间张量随batch累积导致训练内存爆炸，长语音尤为突出。本文提出Flash RNN-T：专用GPU融合内核加可选分块检查点重计算，在保留全对齐空间与全词表（精确损失不变）的前提下，将联合中间内存从O(N(H+V))压至O(min(N,R)(H+V))。H100实测非分块版比最快基线
- **关键技术点**：传统批式训练将整个batch的联合隐状态与logits全部保留供反传，内存随T×U×V×B增长。Li等的有效位打包与Braun等的逐句计算只消除填充位或缩短句间共存窗口，均未对单句内部的大中间张量设上界。
- **主要指标**：（H100 80GB，吞吐samples/s/峰值内存）： - medium：非分块Flash比Apex吞吐高24-25%、内存省49-56%；分块Flash 2839/1.84GiB，较Apex retain内存降9倍、吞吐低16.3% - long：分块Flash 163.6/4.26GiB，全
- **代码**：https://github.com/MahmoudAshraf97/flash-rnnt-paper | **Demo**：暂无

---
## [PhonoBridge: Error-Aware Phoneme-Mediated EMG-to-Text Reconstruction](https://arxiv.org/abs/2610.27678)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-21
- **一句话贡献**：针对表面肌电（EMG）静默语音转文本中配对 EMG–文本数据稀缺、解码器难以纠正前端识别错误的痛点，作者提出 PhonoBridge 两阶段框架：先用通道感知前端把 8 通道 EMG 解码为音素序列，再用 Qwen3-8B 后端把音素还原为文本。为保证后端见过真实前端噪声，作者提出错误画像引导增广（EPGA），从留出集的前端预测中统计替换/删除/插入模式并注入 LibriSpeech 转写音素序列
- **关键技术点**：现有 EMG-to-text 多采用 CTC 前端加外挂语言模型/WFST 的模块化结构（Gaddy & Klein、Gowda & Miller），重建阶段的语言能力受限于 n-gram 或小模型。直接端到端 EMG-to-text 或直接用 LLM 处理 EMG 特征（EMG-LLM）则受制于配对数据规模与跨模态对齐难度，泛化到开放词表时 WER 甚至超过 100%。
- **主要指标**：- 端到端 WER：24.77% - 端到端 CER：14.58% - 前端 PER：13.65%（cWER 35.53%） - 相对最强基线：较 Gaddy & Klein 的 28.27% 下降 3.50 个百分点（约 12.4% 相对降低），较 EMG2Vec 的 29.45% 下降 4.68
- **代码**：暂无 | **Demo**：暂无

---
## [ShlokaDhara: A Multi-Speaker Sanskrit Speech Corpus for Learning Meter-Aware Prosody in Text-to-Recitation](https://arxiv.org/abs/2610.26929)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-21
- **一句话贡献**：梵语诗歌朗诵受 Chandas（诗律）约束，音节按 Laghu（轻）与 Guru（重）构成严格时长模板，但现有语料多面向 ASR 或对话合成，缺乏格律保真度。作者构建 ShlokaDhara：43.24 小时、19 位说话人、覆盖 20 余种 Chandas 的多说话人朗诵语料，并提出 Text-to-Recite 任务与音节级评测。微调 7 类 TTS 后，XTTS-v2 取得最高 UTMOS 
- **关键技术点**：现有梵语语料如 Vāksañcayaḥ、IndicVoices 以识别或对话为目标，韵律被当作随机声学特征；面向格律的 Vāgdhenu 仅 5.3 小时单说话人，难支撑零样本多音色朗诵。相同 Chanda 可由不同旋律演唱，亟需解耦“不变格律结构”与“可变旋律实现”的数据。
- **主要指标**：- XTTS-v2 seen UTMOS：4.01（次优 EnGenTTS 3.87） - XTTS-v2 unseen UTMOS：3.24（次优 Voxtral 3.12） - XTTS-v2 seen CMOS：-0.0386；unseen CMOS：-0.0502 - 16 位专家 5 级评
- **代码**：暂无（作者称将公开数据集与源码） | **Demo**：https://shlokadhara.vercel.app/

---
## [MuseFlow-TSE: Music-Aware Target Speech Extraction via Cross-Source Band-Splitting and Data-to-Data Flow Matching](https://arxiv.org/abs/2610.29119)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-22
- **一句话贡献**：现有目标语音抽取（TSE）几乎只在无音乐混合上验证，面对宽带、强谐波、与语音高度重叠的背景音乐时判别式方法受掩码上限约束、生成式方法又易幻觉身份漂移且步数多。本文提出 MuseFlow-TSE，按"判别式删除+生成式插入"分两阶段：Stage-1 音乐感知的跨源分频抽取器联合估计目标/干扰人/音乐/噪声，Stage-2 以判别估计为锚点、对干扰轨做负条件、按难度自适应跑 1–4 步数据到数据流匹配
- **关键技术点**：真实场景含背景音乐、歌唱、噪声与混响，而 TSE 研究几乎全在无音乐混合上评测，zero-shot 含音乐评测明显退化；纯判别只能删干扰无法补目标细节，纯生成从噪声采样慢且易把被删的伴奏或歌唱幻听回来造成身份漂移。
- **主要指标**：- Config-D SI-SDRi 13.2→13.0 dB / PESQ 2.71 / SIM 0.89 / WER 12.0% / MusicLeak 2.9% - Config-DG SI-SDRi 13.2 dB / PESQ 2.88 / SIM 0.90 / NFE 1.6 - 关键对
- **代码**：暂无 | **Demo**：暂无

---
## [Where Does Timbre Hide? Localizing Speaker Information in Speech Signals](https://arxiv.org/abs/2610.29150)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-22
- **一句话贡献**：音色相似性是 VC、克隆 TTS 与零样本语音模型的核心评测目标，但生成语音"不像目标说话人"往往源于说话人信息分离不彻底。本文以说话人身份为可测代理，在中英日三路/歌唱数据上系统探测频带、相位/幅度、WORLD 源/滤波、清浊音、SSL 层与 EnCodec/HuBERT token，并配 45 人听音测试。结果：感知音色集中于 1–8 kHz 幅度谱与声道包络（Same <8kHz 评分 4.
- **关键技术点**：音色难以直接规模化测量；经典子频带研究早于高采样率语料、神经 codec 与 SSL 探针，机器可分辨性与人类感知相似度长期混为一谈，导致 VC/TTS 不清楚该在何处注入说话人条件。
- **主要指标**：- 听音（45 人，1–5 分）：Same <8 kHz 4.45±0.35 vs 仅 >8 kHz 1.24±0.29，低/中频配对差 +2.57（p=1.7e-38） - mel-MLP 说话人分类：VCTK 1–4 kHz 92.1%、4–8 kHz 89.3%、20–24 kHz 50.1%
- **代码**：暂无 | **Demo**：暂无

---
## [XingChen-UniFE: A Unified Generative Speech Front-End via Complementary Acoustic-Semantic Modeling](https://arxiv.org/abs/2610.29164)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-22
- **一句话贡献**：针对噪声、混响、削波、丢包、带限与干扰说话人等复杂退化下GSR与TSE各用独立模型、架构割裂且部署成本高的问题，本文提出统一LALM模型XingChen-UniFE，将两类任务建模为条件式离散token生成：冻结WavLM语义分支与复谱可学习声学分支经双向交叉注意力显式融合，连同任务token与注册语音条件化从零训练的自回归主干，生成交错延迟排列的codec token。Libri2Mix去噪PE
- **关键技术点**：判别式GSR依赖任务专属架构、难统一异构恢复任务，严重退化需同时建模声学、语言与说话人特征；LALM所用SSL特征未针对波形重建优化，PASE/L3-SE等声学表征仍源自SSL、缺频相建模，融合仅加法/拼接。
- **主要指标**：- Denoise：PESQ 2.137、STOI 90.56、SBS .916、LPS .930，全指标最佳（超次优UniTok 2.100） - TSE：PESQ 2.093、SBS .888；TSE&Denoise：PESQ 1.703、SBS .852、LPS .714 - GSR平均LPS
- **代码**：暂无 | **Demo**：暂无

---
## [DIAL-S2ST: Learning Latency Control for Simultaneous Speech-to-Speech Translation](https://arxiv.org/abs/2610.32214)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-26
- **一句话贡献**：Hibiki等多流式同传语音到语音翻译（SimulS2ST）模型把"何时说"与"说什么"耦合进并行token流，推理时无可独立调节的读写策略，直接偏置logits会显著损伤质量。本文提出DIAL-S2ST后训练方法：以冻结预训练模型加源音频超前（lookahead）作教师，对LoRA学生做在线自蒸馏学得更早释出，并将LoRA缩放系数与lookahead绑定，实现单适配器推理时连续延迟控制。仅用约1
- **关键技术点**：SimulS2ST需持续权衡"多听源语音"与"早出译文"，质量-延迟平衡应在推理时可调。StreamSpeech的chunk大小与Seamless的发射阈值是显式控制机制，但Hibiki等多流模型把发射时机由训练期学到的token流行为决定，训练后无独立读写策略；仅偏置PAD/BOS logits会致质量骤降。
- **主要指标**：- ASR-BLEU：34.4（α=0.5操作点），LAAL 2.16s、End Offset 1.73s - 音色/自然度：Speaker Sim 0.391、UTMOS 3.41 - 关键对比（LAAL 1.8/2.3/2.8s对齐延迟的ASR-BLEU）：Ours 32.5/34.8/35.6
- **代码**：暂无 | **Demo**：暂无

---
## [A Robust, Explainable, and Efficient Deep Metric for Speech and General Audio Quality](https://arxiv.org/abs/2610.35810)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-27
- **一句话贡献**：针对现有客观音频质量指标的两难困境：传统 PEAQ 类模型可解释但泛化差，基于音频基础模型的深度指标泛化好却是黑箱且算力昂贵。本文提出 SAQM，将 ITU-R BS.1387 PEAQ 的 1199 维感知前驱特征与 ConvNeXt 一维卷积网络结合，用对比回归学习质量流形。为绕开人工标注稀缺，设计两条伪标签预训练路线，共约 5000 小时数据训练。模型仅 0.039 GMACs、20M 参数
- **关键技术点**：PEAQ/PESQ 等规则型指标依赖手工感知特征，对加性噪声、混响、带宽扩展等现代失真可靠性下降；SCOREQ、DeePAQ 等深度指标虽在特定数据集领先，但依赖昂贵的音频基础模型，在语音或音乐单一域外泛化受限，且无法说明哪里坏了、坏在何种失真。
- **主要指标**：- NISQA-VAL 皮尔逊/斯皮尔曼：0.84 / 0.81（强基线 0.92 仍领先） - SiSEC08：0.90 / 0.84，SASSEC 0.87 / 0.80，SAOC 0.88 / 0.73 - ODAQ：0.77 / 0.82；IGORC96：0.89 / 0.78；USAC3：
- **代码**：暂无 | **Demo**：暂无

---
## [AudioRSI: Recursively Self-Improving Audio Reasoners](https://arxiv.org/abs/2610.36578)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-28
- **一句话贡献**：现有音频大模型RL的奖励全部来自模型外部：只看最终答案的结果校验、需人工调权的过程分、或训练全程冻结的LLM裁判，导致"学生进步、监督者不变"。本文提出AudioRSI：单一模型同时充当Actor（以`<think>…<answer>…`格式生成推理路径）与Critic（对组内候选路径两两比较输出胜/平/负，折算过程级奖励），并每200步将Critic同步替换为当前Actor，形成递归自我改进；C
- **关键技术点**：结果导向奖励让"蒙对"与"严谨声学分析"得分相同，二元信号无法区分到达答案的路径；人工过程奖励需多项调权；外部LLM裁判标准固定，OOD精度在训练后半程停滞。核心问题是：监督者能否也学习，且随策略一起变强。
- **主要指标**：- MMAU test-mini：76.10%（Sound 82.58/Music 69.16/Speech 76.58），较同协议Ke-Omni-R 74.60%高1.5pp，超Audio Flamingo 3（73.30）与Gemini 2.5 Pro（71.60） - MMSU：Overall
- **代码**：暂无 | **Demo**：暂无

---
## [The Content Leash: Mitigating Degenerate Solutions in Invertible Speaker Anonymization](https://arxiv.org/abs/2610.36768)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-28
- **一句话贡献**：针对基于条件可逆网络（cINN）的可恢复说话人匿名化方法Rano做论文指导式复现，发现退化解：发表目标不约束匿名化输出内容，优化器可借严重语音降质降低triplet损失、制造"高EER+完全不可懂"（41.6% EER但WER 117.6%）的假隐私。作者提出三项修改：anchor与range损失约束输出谱、ECAPA蒸馏mel域验证器泛化到未见验证模型、含测量底限与seeds的评测协议。最终在3
- **关键技术点**：在Rano类cINN匿名化中，consistency损失只作用于以真实说话人嵌入为条件的另一前向，triplet损失只看匿名化谱Xa的说话人嵌入，没有任何项惩罚Xa内容改变，目标可被语音降质"作弊"；且对轻量验证器训练的匿名化器骗不过独立强验证模型。
- **主要指标**：- ECAPA-TDNN EER 26.31±0.25%（干净底限2.83%）；held-out ResNet 27.86%（底限2.08%） - WER 11.75%（底限2.48%，Whisper large-v3），McAdams基线8.44% EER/WER 3.61% - 匹配消融：加两损
- **代码**：暂无 | **Demo**：暂无

---
## [Beyond Answer Changes: Matched Same-Class Controls for Local Audio Evidence](https://arxiv.org/abs/2610.37605)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-28
- **一句话贡献**：音频-语言模型（ALM）在被查询声事件发生局部编辑后改变答案，可能源于对事件类别的响应、对波形被改写的敏感，或两者混合，现有干预评测无法区分。本文提出匹配的同类别替换控制协议：异类替换与同类替换共享同一时间区间、电平估计、供体拟合与交叉淡入淡出，仅前者改变查询类别而后者保持正确答案不变。在600个合成声景、3个模型（Qwen2.5-Omni-7B/3B、Fun-Audio-Chat-8B）上，异类
- **关键技术点**：ALM答案是否真正由局部声学证据支撑是可信度评测核心。现有噪声/区域掩蔽、注意力引导掩蔽、反事实声音植入等方法把"改变目标类别"与"局部重写波形"混为同一复合处理，答案变化无法归因。
- **主要指标**：- 异类替换答案变化率：73.17%/70.25%/65.33%（Qwen2.5-Omni-7B/3B、Fun-Audio-Chat-8B） - 同类重写答案变化率：12.25%/12.50%/15.67%；配对差距Δ=60.92[57.25,64.58]/57.75/49.67[45.33,53.
- **代码**：暂无 | **Demo**：暂无

---
## [Partially Edited Audio: Generation, Defense, and Open Problems](https://arxiv.org/abs/2610.37640)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-28
- **一句话贡献**：本文为ICASSP 2027特殊session撰写的部分编辑音频（partially edited audio）综述，首次从生成与防御双视角统一梳理该范式。文章沿"部分/完整"与"编辑/生成"两维下定义，归纳共存性、局部性、双重意图三特征，论证"fake/有害"是取决于披露、同意与信任假设的应用性判断而非编辑操作固有属性。综述按编辑目标-方法-评估组织生成侧，按检测-定位-deepfake分离-可
- **关键技术点**：生成式音频模型已从整段合成走向对真实录音的局部选择性编辑（词/短语替换、插入、删除，及情绪、韵律、背景音修改），但生成与安全社区研究彼此割裂：无统一框架连接编辑效用与取证责任，且"何为fake"的判定标准长期含糊。
- **主要指标**：- 转录正确性：WER（口径不足——转写达标仍可能引入说话人/韵律/声学不一致） - 自然度：UTMOS等自动MOS预测 - 说话人一致性：WavLM等SV嵌入相似度，比较编辑区与未编辑区 - 关键对比（定性）：检测器主要依赖拼接边界伪影，context-aware神经编辑消除边界后此类性能显著退化
- **代码**：暂无 | **Demo**：暂无

---
## [SpeakerTurn: Target-Speaker Semantic Turn Detection in Multi-Speaker Environments](https://arxiv.org/abs/2610.39828)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-30
- **一句话贡献**：多说话人环境下仅凭语义完整性无法判断助手何时应答：完整话语可能属于干扰说话人，而注册用户可能仍在说话、附和或请求等待。本文提出SpeakerTurn，在CocktailASR-1之上以LoRA联合生成目标转写与语义轮次状态，区分complete/incomplete/backchannel/wait/target-absent五态并单列interrupt/ignore打断任务。合成双语测试上五态m
- **关键技术点**：现有轮次检测（Easy Turn、Smart Turn）只看混合音频判完整，不注册、不分归属；个人VAD只给声学线索，不表达backchannel/wait等语义状态，全双工系统易被他人完整句误触发应答。
- **主要指标**：- 五态轮次检测：macro F1 0.811、准确率83.33%（n=390）；四态F1 0.779、二态F1 0.804 - 目标转写：CER 4.20%（中1.01%、英WER 6.48%），CoT变体降至2.56% - 打断任务：10/10参考换扰对全部判对（turn-only基线8/10）
- **代码**：https://github.com/linan2/SpeakerTurn | **Demo**：暂无

---
## [The Importance of Speech Genre for End-of-Turn Detector Training](https://arxiv.org/abs/2610.39742)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-30
- **一句话贡献**：该研究聚焦语音对话系统轮次结束（EoT）检测中被最少关注的维度——训练数据语音体裁，首次将其作为唯一受控变量：用同一标注管线构建人类多轮对话（Conv-10K）与人机单轮（ST-10K）两个配对语料，分别训练同一1.8M参数流式ConvLSTM检测器并在四个测试集评测。对话训练模型F1达0.760–0.959，最高领先单轮训练+0.45，增益主要来自中途停顿的误报下降（CASPER上FA% 6.6
- **关键技术点**：EoT研究长期沿特征、建模、模态三轴改进，训练数据构成这一轴最少被研究：多数工作只用单一语料，对话与单轮训练几乎无配对比较，增益无法归因于数据本身；判决粒度（帧级vs语句级）的影响也未被系统检验。
- **主要指标**：- 帧级F1（对话vs单轮训练）：Int-5K .894/.444、CASPER .959/.694、ST-Complete .911/.738、SLURP .760/.558；差+0.17~+0.45（p<1e-70，共享τ=.7仍成立）；CASPER上FA% 6.6% vs 44.7% - 语句
- **代码**：暂无 | **Demo**：暂无

---
## [Towards Multilingual End-of-Turn Detection using Frozen Speech Encoders](https://arxiv.org/abs/2610.39755)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-10-30
- **一句话贡献**：语音对话系统的轮次结束（EoT）检测器通常需按语言重新训练标注并逐语调整判决阈值，扩展成本高。本文提出"冻结多语种编码器+单一小头"方案：固定Whisper-small编码器（768维/50Hz，读取第6层），仅训练一个L2逻辑回归探针，在CALLHOME五语种（英/西/德/中/日，74,646个样本）上研究零样本迁移、少样本适应与阈值复用。结果显示因果读取迁移缺口仅0.017 AUC，几小时目标
- **关键技术点**：现有EoT/endpointing检测器逐语言构建：带标注轮次边界昂贵，生产系统还须按语言搜索重设阈值以满足虚警预算；此前跨语言研究均经ASR文本间接进行，声学信号本身的轮次转移能力从未被直接度量。
- **主要指标**：- 零样本迁移缺口Δ：因果0.017 AUC（95%CI [0.016,0.019]），oracle 0.011；同语言因果对角均值0.888 - 少样本适应：中位数对15分钟恢复缺口25%、1小时一半，数小时后所有目标语言距自身上限<0.004 AUC（含最难的日语） - 阈值复用：虚警率3.5-
- **代码**：暂无 | **Demo**：暂无

---
