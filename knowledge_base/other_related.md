# OTHER RELATED（按评分降序）

共 41 篇

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
## [TamilEOT: A Dataset and Model for Semantic End-of-Turn Detection in Tamil Telephone Speech](https://arxiv.org/abs/2609.05631)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-04
- **一句话贡献**：语音代理必须在每个停顿处裁决用户是否说完，无语言模型时只能退化为固定静默超时。本文发布 TamilEOT 数据集（从 116 段真实泰米尔电话通话切出 18,485 条标注 turn 边界）及两个 audio-only 检测器（自 Smart Turn v3 微调，8.7MB 与 21MB）。在来自 30 通未见电话的 4,168 条 held-out 上，精度由零样本 70.30% 升至 83.
- **关键技术点**：语义端轮（EOT）检测是语用层面判断，单纯静默时长是表面近似；现有开源语义 EOT 检测器均以英语等大语种为主，南印度语言完全空白。作者以实验揭示规则标签与模型任务不等价：规则在正类命中 95.9% 但负类仅 44.4%（低于随机），因规则回答的是"是否存在长静默"而模型需回答"用户话语是否完成"。
- **主要指标**：- 精度：70.30%（零样本）→83.71%（8.7MB）→86.13%（21MB） - ROC-AUC：0.751→0.921 - 延迟：<150ms 单线程笔记本 CPU
- **代码**：开源（数据、权重、代码公开） | **Demo**：暂无

---
## [MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation](https://arxiv.org/abs/2608.03021)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-05
- **一句话贡献**：神经音频编解码器是LLM音频生成的基础tokenizer。现有工作广泛使用语义先验增强语言可懂度，但显式声学先验的整合仍缺乏探索。MeloCodec提出"Tokenize-then-Fuse"范式，预训练独立的离散旋律分支锁定旋律结构（音高、节奏），再进行特征融合，解决直接融合导致的优化不稳定问题。两阶段训练策略防止码本坍塌。在歌唱声音表示上优于基线，提升音高一致性，支持可控音高操控，最小化音色退
- **关键技术点**：神经音频编解码器（如EnCodec、DAC、SoundStream）将音频编码为离散token，作为LLM音频生成（如TTS、音乐生成）的输入。现有工作主要引入语义先验（如HuBERT、WavLM特征）提升可懂度，但显式声学先验（如旋律、音高、节奏）的整合尚未被充分探索。直接融合声学先验可能导致优化不稳定（如码本坍塌、收敛困难），特别是对于歌唱这类对音高敏感的领域。
- **主要指标**：- 重建质量：MeloCodec显著优于基线（EnCodec、DAC），特别是在高音区域 - 音高一致性：PCC（Pearson相关系数）提说明显高于基线 - 可控音高操控：在编码空间中进行音高偏移后，解码器能保持音色一致性 - 音色退化最小化：在MOS评估中，音色自然度接近原始录音 - 消融实验验
- **代码**：暂无 | **Demo**：暂无

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

- **方向**：语音前端；**作者**：Goksenin Yuksel、Marcel van Gerven、Kiki van der Heijden；**机构**：拉德堡德大学Donders研究所；哥伦比亚大学Zuckerman研究所；**发布日期**：2026-09-22 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-22
- **一句话贡献**：一阶 ambisonics（FOA）信号具有严格的O(3)旋转反射对称性，但现有声事件定位与检测（SELD）方法要么靠旋转增广近似学习该对称性，要么使用计算昂贵的SO(3)等变网络，无法处理同类重叠声源且未利用反射对称。本文提出EquiSELD，首个对完整O(3)群精确等变的SELD注意力网络：将每个时频token处理为"O(3)不变标量+等变声强向量"双流，经Multi-ACCDOA读出不变活动
- **关键技术点**：
- **主要指标**：- TAU2021 ℰS：0.40（最强基线SELDNet+ 0.47、CGNet-STS 0.51，差-0.11） - STARSS23 ℰS：0.56（SELDNet+ 0.60、CGNet-STS 0.72，差-0.04/-0.16） - TAU2021：LE 16.4°、F20° 49.8%
- **代码**：https://github.com/labhamlet/equiSELD | **Demo**：暂无

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
- **关键技术点**：
- **主要指标**：
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
