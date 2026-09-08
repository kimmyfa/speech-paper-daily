# OTHER RELATED（按评分降序）

共 15 篇

## [10 Anomalous Sound Detection Meets Noise-Aware Self-Supervised Learning](https://arxiv.org/abs/2608.00447)

- **方向**：语音前端 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：异常声音检测（ASD）在工业设备监控中至关重要，但实际工厂环境中的背景噪声严重干扰检测性能。本文提出噪声感知自监督学习（NA-SSL），利用双麦克风录音设置（近场麦克风靠近目标机器，远场麦克风捕捉噪声），训练NA-SSL模型从含噪信号中提取干净表示。使用FSD50K（目标声音）+ WHAM!/DEMAND/QUT-NOISE（噪声）模拟双通道录音。在DCASE 2026 Challenge Tas
- **关键技术点**：** 工业ASD需要在工厂环境中检测机器异常声音，但严重背景噪声导致标准ASD方法性能大幅下降。DCASE 2026 Challenge Task 2首次引入噪声感知ASD（NA-ASD）任务，提供双麦克风录音：近场（靠近机器，目标信号主导）和远场（远离机器，噪声主导）。挑战在于如何利用远场噪声信息辅助近场信号的干净表示学习。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [13 SoniSpeech: Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces](https://arxiv.org/abs/2608.00803)

- **方向**：语音前端 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：无声语音接口（SSI）允许用户在不发出声音的情况下与设备交互，但受限于小词汇量数据集。本文提出SoniSpeech，首个大规模开放词汇可穿戴无声语音接口三模态数据集，包含34小时、18000个话语，三个同步模态：超声回波profile（通过声学传感眼镜捕获面部运动）、有声音频和前视视频。语料来自SODA对话数据集，包含5356个唯一词汇和完整音素覆盖。CTC ResNet-34基线在纯无声模式下W
- **关键技术点**：** 无声语音接口允许用户在安静环境下（如图书馆、会议室）或隐私敏感场景下与设备交互。现有研究受限于小词汇量（通常<100词）和封闭词汇集，缺乏大规模开放词汇的基准数据集。可穿戴硬件如面部电极（EMG）虽然精度高但佩戴不便。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 DNN-Based Frequency-Dependent Estimation of Speech, Music, and Noise Power in Acoustic Mixtures for Hearing-Aid Scene Analysis](https://arxiv.org/abs/2608.17482)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：当前助听器场景分析依赖多个独立估计器（场景分类、VAD、SNR 估计），计算开销大且未利用任务间依赖。本文提出统一可解释的场景表示：用低复杂度因果 CRNN 将混合谱分解为语音/音乐/噪声三类时-频相关相对功率比例，再与混合功率相乘恢复各类功率谱。开发集总体对数误差 1.40 dB、PCC 0.891；未见数据集为 1.71 dB、0.875。下游 VAD 经简单阈值化即可达到与 SOTA Sil
- **关键技术点**：** SOTA 场景分析通常由多个独立估计器组成（场景分类、VAD、SNR 估计、源定位/方向分析），输出控制压缩、降噪与程序自动切换。该模块化设计有两方面缺陷：一是计算低效，而深度学习算法进入助听器后台算力更趋紧张；二是独立估计器无法利用相关任务间的依赖，且多从同一混合声提取重叠信息（如 VAD 与 SNR 估计）。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 A Factorial Ablation of a Speech-to-SFT Pipeline: Differential Effects on Data Quality and Downstream Transfer](https://arxiv.org/abs/2608.20394)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-24
- **一句话贡献**：语音转SFT数据流水线在工业界广泛应用，但各阶段的边际价值此前从未被公开逐阶段验证。本文针对韩国医学与金融会议录音驱动的三段式流水线（Phase 0转录精炼、Phase 1 QA生成、Phase 2质量精炼）设计2x2因子消融，四种条件各生成约2600条QA，微调5大厂商9个（2.4B-70B）LLM，并以4个跨厂商LLM评判员、6位盲评领域专家及KMMLU/KMMLU-Pro/MMLU三个基准评
- **关键技术点**：** 现有语音转SFT工作（COSMIC、SIFT-50M、LiveCC、PodGPT等）或面向通用能力或采用持续预训练而非文本LLM SFT，均未对精炼环节做逐阶段消融，各阶段边际价值对实践者未知；且当数据源为语音时有转录噪声、命名实体对齐、语篇结构缺失等文档源不存在的前端挑战。
- **主要指标**：
- **代码**：https://github.com/flitto/speech-to-sft-ablation-paper | **Demo**：暂无

---
## [7 Sensing Bone-Conducted Speech with Earbuds](https://arxiv.org/abs/2609.02165)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-02
- **一句话贡献**：针对无线入耳式耳机在噪声环境下自身语音（OV）采集困难的问题，本文系统分析了佩戴者语音诱发的耳机壳振动（骨导语音）的频谱与空间特性。基于 Anker P3i 与 A20i 两款耳机、17 名受试者的实测数据，发现该振动呈显著低通特性：400 Hz 以上以约 -93 dB/decade 滚降，100-400 Hz 为高功率频段（平均约 530 µg）。空间分析表明耳机主要沿耳道口进出方向振动，且个体
- **关键技术点**：** 骨导语音可提升 TWS 在噪声下的自语音采集，但耳机壳振动的带宽与空间特性缺乏系统测量，致使加速度计轴数选择、安装方向以及单轴/三轴方案缺乏设计依据，现有多项研究用法不一、未达共识。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 Beyond .WAV: Design and Software Verification of VocalCap, a Traceable Browser-Based Audio Capture System for Vocal Biomarker Research](https://arxiv.org/abs/2609.03320)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：远程语音采集往往只交付一个音频文件，缺少"信号如何被捕获、传输、处理与验收"的证据。VocalCap为受试者自助式语音采集设计机构可控浏览器系统，每个录音同时保留浏览器原生对象、客户端无损Float32 WAV与服务端规范单声道PCM16 WAV，并关联完整性与转换溯源证据。软件验证证实40ms连续性边界在8/16/44.1/48kHz正确生效，活动声道选择RMS偏差超低频低于0.001dB。
- **关键技术点**：** 语音生物标志物研究要求把采集技术验证与下游推断分开，远程自助采集时无受训人员在场，权限处理、编码与持久化均不可见。同类系统各覆盖部分环节，但没有一个把双工件配对、逐字节校验、版本化规范化等整合为单一验收契约。SPIRA项目（6000+语音捐献者）的空白录音问题直接催生本设计。 **系统设计：** Flask服务端+移动优先Web前端，协议通用任务执行器（麦克风测试、持续元音、标准句、计数、自发语音5任务）。同一MediaStream并行馈入MediaRecorder（原生对象N）与AudioWorklet（Float32 WAV无损L）双路径。采集记录含完整清单M（SHA-256）、采集
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 KanAdapter: A Kolmogorov-Arnold Network-based Plug-and-Play Module for Efficient Fine-tuning of Foundation Speech Models](https://arxiv.org/abs/2609.05281)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-04
- **一句话贡献**：全文微调自监督（SSL）语音大模型计算开销巨大，而现有参数高效微调（PEFT）方法主要依赖 MLP 适配器，其固定激活函数在紧凑参数预算下表征能力受限。本文提出 KanAdapter，一种基于 Group-Rational KAN（GR-KAN）的即插即用适配器框架，采用并行瓶颈设计，在冻结的 Transformer 编码器旁插入可训练 GR-KAN 分支，并从预训练 MLP 层迁移权重实现稳定初
- **关键技术点**：** 现有 PEFT 方法应用到语音 SSL 模型时建模能力受限：LoRA 本质是无非线性激活的线性低秩分解，难以刻画伪造痕迹、情感分布等复杂语音特征；AdaptFormer 的 MLP 瓶颈使用固定激活，表达力不足。针对语音 SSL 的 PEFT 研究仍少见，将 KAN 类可学习激活模块用作适配器此前尚属空白。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 Explicit and Stable Pseudospectral Time-Domain Method for Föppl-von Kármán Equations](https://arxiv.org/abs/2608.06139)

- **方向**：声学模拟 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-06
- **一句话贡献**：模态合成是乐器动力学模拟的常用技术，但Föppl-von Kármán板方程的非线性项导致模态域中四阶张量计算代价极高（O(N_x^4)）。本文提出伪谱时域方法：在空域网格上计算乘积项（O(N_x^2 log N_x)），在模态域中精确计算空间导数，通过离散正弦/余弦变换施简支边界条件，并利用标量辅助变量技术实现显式稳定时间积分。数值实验在44.1kHz采样率下验证了能量守恒到机器精度，且漂移调控
- **关键技术点**：** Föppl-von Kármán板方程的非线性耦合由四阶张量描述，纯模态方法需要评估O(M_x^4)个耦合项，在GPU上才能实现实时。现有数值方法（Kirby & Yosibash）使用隐式迭代方案，计算效率低。
- **主要指标**：
- **代码**：https://github.com/victorzheleznov/fa2026 | **Demo**：https://victorzheleznov.github.io/fa2026

---
## [10 Structured Phonological Representations for Audio-Articulatory rtMRI Speech Classification](https://arxiv.org/abs/2608.09767)

- **方向**：语音大模型（语音前端） | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：实时 MRI 可以观察语音中的声道发音，但将这些发音模式映射到音系类别仍具挑战性。该工作研究 PhonoQ（一个训练识别结构音系特征的音频模型）是否为音频-发音建模提供有用信息。从 PhonoQ 的 Conformer 模块提取表示（其训练受方式、位置、发声、元音特征监督），使用发音轮廓与同步音频特征结合，对比 WavLM-large 和 HuBERT-large 基线。在未见语音和未见说话人设置
- **关键技术点**：** rtMRI 提供了高时间分辨率（~80fps）的声道发音观测，但发音数据维度高、标注困难，映射到音系类别需要有效的特征表示。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [9 Multi-Task Learning for Non-Canonical Phoneme Recognition via Articulatory Feature Decomposition](https://arxiv.org/abs/2608.22273)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-25
- **一句话贡献**：针对病理/非标准语音中系统性的发音偏差与临床标注数据稀缺，本文将音素识别从"原子类别分类"重构为发音特征维度（manner/place/voicing/height 等）的多任务预测，提出基于 WavLM 的分层多任务（HMTL）架构，通过 cross-attention 融合发音特征表示后经 BiLSTM 与 CTC 输出音素序列。结合 Momentum Pseudo-Labeling 半监督与
- **关键技术点**：** 病理/非标准语音（如运动言语障碍、儿童言语失用）音素识别 PER 高达 42%-69%。现有模型在健康语音上训练，会把非标准发音"自动纠正"为最近的规范音素；且把音素当作原子标签无法刻画"部分特征保留、部分偏离"的系统性错误结构。病理语音标注稀缺且标注者间一致性差，故用 L2-ARCTIC 口音语音作为病理发音的代理。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 LipsAM: Lipschitz-continuous Neural Networks for Convergent Plug-and-Play Audio Signal Recovery](https://arxiv.org/abs/2608.23038)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-25
- **一句话贡献**：传统语音 DNN 将复数 STFT 的幅度与相位分开处理，由于 sign 函数在零点不连续，此类网络即使幅度部分 Lipschitz 连续，整体也必然不连续，无法纳入现有 Lipschitz 理论框架。本文推导了幅度修正器（AM）满足 Lipschitz 连续性的充要条件（定义 LipsAM），并给出 LipsAM-E、LipsAM-M（时频掩蔽）两类可证连续的架构及 Lipschitz 常数紧凑
- **关键技术点**：** 现有 Lipschitz 网络构造（谱归一化、正则化、结构法）均针对实值图像网络；而语音常用的复数谱网络通过幅度映射加 sign(z) 分离处理幅度相位，sign(z) 在 z=0 处不连续，导致即使幅度映射本身 Lipschitz 连续，整体映射仍非 Lipschitz。这阻碍了基于 Lipschitz 条件的 PnP 收敛保证在语音中的应用。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction](https://arxiv.org/abs/2608.26005)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：面向实时语音交互中语音大模型（SLM）缺乏记忆的痛点，本文提出 VoiceMem"双脑流式记忆"架构，将短时工作记忆与长期记忆结合，构建了完整的记忆感知 SLM 训练、评估与部署流水线。实验显示其在记忆准确性、情感个性化与实时性上均有显著优势，为实时语音交互提供了实用的记忆基础。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 Multirate State Space Models for End-to-End Processing of Pulse Density Modulated Speech Signals](https://arxiv.org/abs/2608.28472)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：针对低功耗常开边缘设备上的SSM语音处理依赖PCM、且PDM转PCM需低通滤波与抽取带来高昂硬件开销的问题，本文提出一种仅用16kHz PCM训练、即可天然泛化到任意采样率PDM数据的端到端语音处理架构。其核心是使用FouT/LegT初始化的SSM编码层，利用其连续时间参数化特性把PCM与PDM输入映射为调制方式与采样率无关的SSM系数表示，并借助连续时间记忆窗在不做抗混叠的情况下对系数序列进行大
- **关键技术点**：** PDM MEMS麦克风兼具噪声鲁棒、低成本与可变采样率（多档位）省电优点，但现有算法都要求先做PDM转PCM（级联滤波+抽取），给资源受限硬件带来开销。已有两条绕开路径均不理想：一是用CNN把滤波与抽取融合为一个输入模块，二是端到端直接喂PDM进DNN。二者共同缺陷是必须在高达2MHz级别的PDM采样率下训练，序列过长导致训练耗时且内存占用大；同时只在单一采样率上训练，无法泛化到其他OSR。其可行性依据在于：PCM与PDM在PCM奈奎斯特频率（8kHz）以下共享完全相同频谱内容。
- **主要指标**：
- **代码**：https://github.com/NECOTIS/ssm-speech-processing.git | **Demo**：暂无

---
## [2 Exploring the Design Space of Representation Learning for Audio Transformations](https://arxiv.org/abs/2608.28127)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：现有神经音频表示学习主要面向内容类任务（如检索、分类），其表征在处理类任务上能力有限；且处理感知表征究竟应编码"与源内容解耦的处理本身"还是"保留内容的处理后音频"，学界缺乏共识。本文提出统一框架，以处理一致性、描述对齐、前向预测等变三类目标在受控设置下穷举组合对比，系统揭示各目标的相对优势与交互效应；框架同时产出变换嵌入与处理后音频嵌入，二者职责互补——距离度量型任务偏好前者，探针型任务偏好后者
- **关键技术点**：** 既要回答"处理感知表征应捕获什么"这一表征设计问题，又要解决"模型、数据、评测各异导致无法归因行为差异"的对比公平性问题。现有方法各自隐式承诺单一表征范式，缺乏在统一条件下的系统比较。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [8 VAANI Noise Event Dataset: A curated spontaneous speech dataset annotated with timestamps for noise events](https://arxiv.org/abs/2609.02474)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-02
- **一句话贡献**：现有音效语料要么面向通用音频标记，要么面向纯净语音分离，缺少叠加在自发性真实语音上、带时间戳的强噪声标注。VAANI Noise Event Dataset 基于 Project VAANI 在印度自发性语音现场录音，为背景噪声事件添加精确起止时间戳，构成七类语义分类法（动物、交通、婴儿/儿童、音乐、信号/报警、家电、非言语人声）。数据集含 72,756 段语音（122.17 小时、38,541 
- **关键技术点**：** 真实印度场景中语音与车辆、动物、婴儿等非平稳背景噪声共存，噪声起止与语音的重叠关系直接决定识别误差与增强质量。现有语料要么合成混合（WHAM!、DESED 合成子集）、仅帧/片段级弱标签（AVA-Speech、FSD50K、AudioSet）、或无噪声标注（CHiME-6）；iNoise 与 Kathbath-Noisy 虽面向印度，却分别缺少语音与噪声事件标注。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
