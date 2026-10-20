# ISCSLP 2026 视听多模态语音分离/增强 精读报告

**来源**：https://iscslp.org/2026/accepted-papers（共 115 篇录用论文）| **执行日期**：2026-10-15

**筛选结果**：命中 **4 篇**，全部来自 Challenge: Real-World Audio-Visual Speech Enhancement（AVSE）特殊赛道，方向均为**语音前端**。

**筛选方法与排除说明**：
1. 按"视听/多模态线索（AVSE 赛道 + audio-visual/lip/visual/face/multimodal）× 分离/增强类任务（separation/enhancement/extraction/denoising）"交叉关键词在标题+摘要全量比对，115 篇中命中 4 篇；
2. 主赛道另有 10 余篇纯音频的语音增强/分离/目标说话人提取论文（如 Scale This Not That、Diffusion SE、TFGridNet 变体 CSGA-TIGER、AlphaFlowTSE 等），因**不含视觉模态**未纳入；含 visual/audio-visual 关键词的论文（deepfake 定位、多模态情感分析等）经逐篇摘要核验与"分离/增强"任务无关，予以排除；
3. 挑战赛官方总览论文（arXiv 2608.23759v3）与两篇系统论文全文（arXiv 2608.14812、2608.09288）均已下载精读，其余两篇依据录用摘要 + 总览论文 §3.3 系统描述交叉核实（已确认 4 论文与排行榜队伍的对应关系：SUSTechAILab、DAVE=依加鹤、AITD=安克创新、audioman=腾讯 CF-AVSS）。

**挑战赛背景（总览论文，供理解精读对象）**：ISCSLP 2026 Real-World AVSE Challenge 首次把"自然混录双说话人音频（无干净参考）+ 可控视觉退化（低清/遮挡/冻帧/音视频失同步/黑屏/3 米远场）"作为受控评测变量。Track 1（真实混合场景）16 队、Track 2（视觉退化）12 队参赛；7 指标（SI-SDR/PESQ/STOI 仅 remix 场景计，UTMOS/DNSMOS-OVRL/CER/SPK-SIM 两场景均计）取平均名次定 OVRL。官方基线 AV-ConvTasNet（VisualVoice 式时域模型）完全不迁移（SI-SDR≈1.1~1.3 dB、CER≈1.0）；三大结论：自然录音显著难于同人 remix（最优系统 CER 9.0%→14.7%）、领先系统把视频主要用作**说话人归属**而非信号重建、无参考质量指标（UTMOS/DNSMOS）与保真/CER/音色类指标排名系统性分歧（存在"刷分"空间）。4 篇精读论文恰为排行榜第 1（并列）、1、4、5 名系统。

---

## [1] A Two-Stage Audio-Visual Speech Enhancement System with Blind Speech Separation and Cross-Modal Speaker Selection

**arXiv ID**：暂无（系统描述见挑战赛总览 arXiv:2608.23759） | **方向**：语音前端（视听多模态语音增强/分离，ISCSLP 2026 AVSE Challenge Track1&2 双冠）

**作者**：chunliang wang*, guochang zhang, rui zhu, runqiang han, jianqiang wei

**机构**：Anker Innovations（安克创新）

**发布日期**：ISCSLP 2026 录用 | **论文**：https://iscslp.org/2026/accepted-papers（ID 172） | **PDF**：暂无 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
面向真实环境视听语音增强（AVSE）中视觉线索不可靠、视听融合模型易被退化视频拖垮的问题，安克团队提出"盲分离 + 跨模态选者"两阶段解耦系统：第一阶段用纯音频双路 Transformer 将混合语音分解为匿名双路流，第二阶段由 AVSelector（基于预训练 auto-AVSR 编码器 + 新设计的跨模态融合与匹配头）计算每路分离流与每位目标说话人唇部视频的双向匹配分，经二分图匹配确定目标输出。该系统在 AVSE Challenge Track 1（真实混合）与 Track 2（视觉退化）双双夺魁，SI-SDR 12.72/12.26 dB，也是两赛道 SI-SDR、PESQ、STOI、SPK-SIM 四项指标的第一名（PESQ 达 3.00、STOI 0.85）。

### 🔧 技术方案
**问题背景：** 主流 AVSE 把视觉特征直接融合进分离网络做信号重建，在低清、遮挡、失同步等真实退化视频下，错误的视觉条件会直接污染分离过程，性能剧烈下降；总览论文将其概括为"视频该不该进重建"这一核心争论。

**模型架构：** 分离级为 STFT 域双路 Transformer（dual-path，盲分离，输出两路匿名流，无视觉条件）；选者级为 AVSelector：复用自动视听语音识别（auto-AVSR）的音视频预训练编码器（部分微调），新增跨模态融合模块与匹配头，对"分离流×唇部视频"逐对打分，二分图匹配（匈牙利式一对一指派）决定目标通道与说话人顺序；视觉增强数据贯穿选者训练。

**核心创新：** (1) 视频完全退出信号重建路径，视觉只负责"归属决策"——把低带宽、可判定的身份关联问题交给跨模态模型，把高带宽的重建问题留给纯音频专家模型，从结构上免疫视频退化。(2) 用 auto-AVSR 的大规模伪标签视听预训练权重替代从零训练 AV-CLIP：唇动语义表征质量高且省资源，融合模块+匹配头把音视频同步特征进一步蒸馏成"同一说话人"判别器。(3) 二分图匹配替代简单的逐流打分排序：在双方言者同时可见、两路流都含残差干扰时，指派式匹配保证全局一致的说话人—流对应，Track 2 视频损坏时主要风险退化为"选错人"而非"分离崩坏"。

**训练策略：** 分离模型先在纯音频语料上以 PIT SI-SNR 预训练，再依次引入感知导向损失（UTMOS、PESQ、WavLM 特征损失）微调，最后用 Track 1 开发集（含真实录音 remix）域适应；AVSelector 用带视觉增强（退化模拟）训练保住匹配鲁棒性。赛道未提供训练集，全部依赖公开数据+官方开发集。

### 📊 实验结果
**数据集**：AVSE Challenge 官方评测集（说话人互斥的 dev/test；test：Track1 mix 2472 + remix 1785，Track2 mix 2820 + remix 2121，另含 3m 远场）

**主要指标**（官方总览表 III）：
- Track 1 remix：SI-SDR 12.716 dB、PESQ 3.000、STOI 0.852、CER 9.2%、SPK-SIM 0.794（四项第一）
- Track 2 remix：SI-SDR 12.255 dB、PESQ 2.939、STOI 0.844、CER 11.4%、SPK-SIM 0.785
- 关键对比：Track1 视觉退化到 Track2 仅掉 0.46 dB SI-SDR；基线 AV-ConvTasNet 12.72−1.14≈+11.6 dB；与并列第一的 CF-AVSS 相比 OVRL 2.86 打平，Track2 以 2.43 对 2.86 拉开差距

**是否开源**：挑战赛基线、评测器与榜单公开（real-world-avse.github.io）；本系统代码未开源。

### ⭐ 评分：8/10
评分理由：Track1/Track2 双冠，是"视频只做归属、不进重建"路线的最强实证，二分图匹配与 auto-AVSR 选者设计针对性强；从 Track1 到 Track2 指标几乎不掉，验证了解耦架构对视觉退化的结构性免疫。扣分在于系统论文贡献偏工程整合（分离主干与选者均借现成组件），且未开源；另外其 CER（14.7%→18.3% mix）高于 CF-AVSS，说明盲分离残差对下游 ASR 仍有实质伤害。

---

## [2] CF-AVSS: A Coarse-to-Fine Audio-Visual Speech Separation Framework with Target-Speaker Refinement and Post-Fusion for Real-World AVSE Challenge

**arXiv ID**：暂无（系统描述见挑战赛总览 arXiv:2608.23759） | **方向**：语音前端（视听多模态语音分离，Track1 并列冠军）

**作者**：Gang Yang*, Zhongshu Hou, Longjie Luo, Yuepeng Li, Fan Zhou

**机构**：腾讯（Tencent）；电子科技大学（UESTC）

**发布**：ISCSLP 2026 录用 | **论文**：https://iscslp.org/2026/acc//epted-papers（ID 174） | **PDF**：暂无 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
由腾讯与电子科大组成的"audioman"队提出粗到细两阶段视听分离框架 CF-AVSS：粗级把渐进式 SPAV-TFGridNet 扩展为**双同步视频流**条件，对双说话人混合物做"视觉排序"的粗估计——按说话人逐个抑制竞争语音、同时刻意保留目标混响与双方共享的背景噪声；细级用 TFGridNet 精炼网以"原始混合+两路粗估计"为输入重建目标、修复粗级刻意保留的残留；粗/细输出再经开发集标定的线性 post-fusion 混合。该系统是唯一进入前二的全视听融合方案，Track 1 与安克系统并列第一，Track 2 第二，并以双赛道最低 CER（12.31%/14.79%，mix 场景 9.0%/11.2%）证明视觉条件对下游识别的增益。

### 🔧 技术方案
**问题背景：** 传统 AVSE（以唇动为唯一条件提取单目标）无法处理"两路干净输出都要评"的分离赛制：混合物中双方说话人都有视频，若按单一目标抽取则非目标流直接崩溃；此外视觉特征若进入重建路径会随视频退化放大误差。

**模型架构：** 粗级：SIR（speech-to-interference ratio）渐进式视听 TF-GridNet（spatial-visual conditioning），融合 AV-HuBERT 视听表征作为双说话人条件头，依次抑制第一位、第二位干扰说话人，输出两路"视觉排序"的粗流，仅去竞争语音、保留混响与公共噪声；细级：标准 TF-GridNet，输入=[混合, 两路粗估计]，以完全重建为损失精炼目标流；融合级：粗/细两版输出的线性加权（权重在 dev 标定），兼顾 SI-SDR 保真与预测质量类指标。

**核心创新：** (1) "SIR 渐进 + 双视频排序"把增强任务改写成对两个可见说话人各自抽取、且顺序由视频指派，天然消解 PIT 排列模糊，也让每个输出流有明确的目标参考。(2) "先抑制、后精炼"的分层损失设计：粗级只负责去掉竞争说话人（避免过抑制目标混响/噪声导致 PESQ/UTMOS 受损），细级基于混合重新恢复信号完整性，配合过抑制惩罚、可微 PESQ 与对抗损失实现感知—保真双目标。(3) post-fusion 线性混合是对"精炼换波形保真"这一已知权衡的工程回应：粗流 SI-SDR 高、细流感知质量高，dev 标定权重让七个指标同时不吃亏。

**训练策略：** 训练数据 = VoxCeleb2 + MISP 2023 模拟混录（RIR 卷积 + 噪声叠加），Track 2 额外做视觉退化增强与**模态丢弃**（modality dropout）训练以模拟视频缺失/损坏；使用 AV-HuBERT 预训练视听编码器；赛制无官方训练集。

### 📊 实验结果
**数据集**：同挑战赛官方 test 集（mix 无参考、remix 有参考）

**主要指标**（总览论文 Table III）：
- Track 1：remix SI-SDR 10.699 dB、PESQ 2.933、STOI 0.841；CER mix 14.7% / remix 9.0%（全场最低）；SPK-SIM 0.771/0.734；OVRL 2.86（并列第一）
- Track 2：remix SI-SDR 10.223 dB、PESQ 2.888、STOI 0.830；CER mix 17.5% / remix 11.2%（最低）；OVRL 2.86（第二）
- 关键对比：比安克纯音频路线低约 2 dB SI-SDR，但两赛道 CER 各低约 4~5 个百分点；相对基线 SI-SDR +9.6 dB、mix CER 从 106% 降至 14.7%；视觉退化 Track1→Track 2 仅 −0.48 dB

**是否开源**：系统未开源；挑战赛基线/评测器/榜单公开。

### ⭐ 评分：8/10
评分理由："粗级只去竞争、细级负责重建"的职责切分非常聪明，双视频排序消解排列模糊的设计比纯后匹配方案更贴分离赛制本质；Track2 模态丢弃增强使其全融合路线未因视频退化崩盘，双赛道最低 CER 是下游价值最硬的证据。扣分：SI-SDR/SPK-SIM 落后于解耦路线，说明视觉进重建的脆弱性被总览结论再次验证；post-fusion 权重偏 dev 标定、有轻微 metric-gaming 色彩；未开源。

---

## [3] DAVE: A Decoupled Audio-Visual Enhancement Framework for Real-World Speech Separation

**arXiv ID**：2608.09288（v1，2026-08-10） | **方向**：语音前端（视听多模态语音增强/分离，Track1 第 4）

**作者**：Wei Zhou; Wanyi Ning*; Yinshang Guo; Qianxiao Fang; Haitao Qian; Yingpeng Li

**机构**：依加鹤智能（Yijiahe AI）；天津大学；南京大学

**发布日期**：2026-08-10 | **论文**：https://arxiv.org/abs/2608.09288 | **PDF**：https://arxiv.org/pdf/2608.09288 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
依加鹤队（Yijiahe Robot）提出 DAVE：解耦视听增强框架，把视觉彻底降级为"低带宽决策通道"，纯音频负责重建。为对抗真实声学域数据稀缺，他们从 AliMeeting/MISP/AISHELL-4 真实会议语料经组合式声学增广构造了 219,411 条混合的 DAVE-Corpus（消融显示合成—真实域 gap 1.31→0.45），并用 PIT SI-SDR + 可微 CER/SPK/STOI/PESQ/UTMOS 多目标渐进优化训练扩充 3 倍的轻量 TIGER-M 分离主干；视觉侧用声纹+双唇同步判别器+唇关键点运动四票加权融合做说话人归属；再叠加"认证选择性增强链"（场景路由分类器把 remix 与真实混录分流，GAN 去噪与响度归一只作用于无参考分区，保证有参考指标结构性不退化）。最终 Track1 第 4（OVRL 4.00），mix 场景 UTMOS 2.65/DNS-OVRL 2.23 全场最高。

### 🔧 技术方案
**问题背景：** 两大痛点并存——融合式 AVSE 对退化视觉输入脆弱；模拟混合训练数据与真实录音存在声学域差。论文用 TIGER 探针模型定量展示纯加法混合在合成域越训越好、真实域反而退化（SI-SDR gap 从 1.31 扩到 3.56），把矛头指向数据而非模型。

**模型架构：** 三段式：(a) 音频分离主干 TIGER-M（时频域高效分离网），encoder 通道 256→512、特征通道 128→256、重复块 8→12，参数 0.82M→2.56M，输出两路匿名流；(b) 视觉归属模块——WeSpeaker-ResNet34(CN-Celeb) 声纹相似度为主锚 + StableSyncNet 口型匹配分 + SyncNet（按 Perfect Match 对比范式微调）同步分 + FAN 唇关键点运动能量，四证据归一化加权，一次通过完成归属；(c) 认证选择性增强链——轻量声学场景分类器区分 remix/真实混录，对真实分支做 MossFormerGAN 式分层去噪 + ITU-R BS.1770 响度归一（6× 增益、峰值保护），remix 分支原样直通。

**核心创新**：(1) DAVE-Corpus 的三源构造协议：组合式会议语料增广（SNR>25dB、2–15s、静音比<35% 筛段，4431 段；说话人嵌入 cos>0.5 拒绝配对；4–8s 随机截复；相对增益 0~6dB 模拟距离差；50% 经 pyroomacoustics 混响 RT60 0.2–0.4s；MUSAN 12–30dB 加噪；冻结合成 ASR 参考文本）——把"评测协议"本身作为训练分布锚点（协议 remix 8000 条）并用 EchoSet 11,413 条回放防灾难遗忘。(2) 指标对齐的可微多目标：冻结 Fun-ASR-Nano 做跨可微 log-mel 前端的 CER 损失、冻结 WeSpeaker 嵌入做音色保真损失，使训练损失与官方评测模型同族，"只惩罚会被指标的退化"。(3) "认证不降级"的后处理链：场景路由 + 分区增强在构造上保证参考类指标零风险，是面向挑战赛排名机制的防御式设计，思路可迁移到任何"无参考指标易被激进降噪刷高"的场景。

**训练策略**：8×A800 DDP，每卡 batch=2×3s 段；Adam 峰值 LR（warm-up 1000 步）+ ReduceLROnPlateau(patience=3)；每 4000 步在 dev 149 held-out 会话上以 PIT SI-SDR 选 checkpoint；渐进多目标按 SI-SDR→+CER→+SPK→+感知损失分阶段接入（消融见 Table II：CER 21.9→19.3→17.1%，UTMOS 1.999→2.77→2.81，OVRL 1.624→2.12，SPK 0.663→0.726）。

### 📊 实验结果
**数据集**：AVSE Challenge test；TIGER 探针域差分析（合成 vs 真实）

**主要指标**：
- Track 1：remix SI-SDR 10.232 dB、PESQ 2.717、STOI 0.817；mix：UTMOS 2.652、DNS-OVRL 2.225（两赛道 mix 感知质量最高）、CER 18.9%、SPK 0.696；OVRL rank 4.00
- Track 2：remix SI-SDR 8.933 dB（−1.3 dB 退化，解耦队伍中最大）、CER mix 23.4%；OVRL 4.14
- 关键对比：比基线 SI-SDR +9.0 / +7.6 dB；域差 gap 分析显示 DAVE-Corpus 训练使合成—真实 SI-SDR gap 从 1.31(加法混合)/3.56(加法微调) 收敛至 0.45

**是否开源**：论文未放代码；挑战赛基线/评测器公开。

### ⭐ 评分：7/10
评分理由：DAVE-Corpus 的数据域差分析与三源构造协议是全文最有价值的部分，可复现、可迁移；可微多目标 + 认证后处理体现对评测体系的深刻理解。扣分：Track2 掉 1.3 dB 与 mix CER 偏高说明归属链在视觉退化下仍先于重建出错；场景路由+选择性 GAN 增强本质是防刷分机制，科学分量有限；SI-SDR 与前三有差距，21.9→17.1% 的 CER 改善主要归功于 ASR 族损失与官方 CER 模型同源（评测对齐红利）。

---

## [4] Separate First, Then Associate: A Two-Stage Approach for Real-World Audio-Visual Speech Enhancement

**arXiv ID**：2608.14812（v1，2026-08-14） | **方向**：语音前端（视听多模态语音增强/分离，Track1 第 5 / Track2 第 5）

**作者**：Tongtao Ling*; Zhong-Qiu Wang

**机构**：南方科技大学（SUSTech, Shenzhen）

**发布日期**：2026-08-14 | **论文**：https://arxiv.org/abs/2608.14812 | **PDF**：https://arxiv.org/pdf/2608.14812 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
南科大团队（SUSTechAILab）把 AVSE 拆解为"先分离后关联"：TF-GridNet 纯音频做双说话人分离（PIT SI-SNR，Libri2Mix 预训练 + 官方开发集 remix 微调），再用自训**帧级** AV-CLIP（冻结 WavLM-Large + 冻结 3D-ResNet18，中间可训练投影与 Transformer 时序编码器，LRS3 上 InfoNCE 帧级对比学习）计算每路分离流与目标唇视频的逐帧余弦相似度均值，两说话人仅两种指派枚举后选高分排列作为目标输出。Track 1 remix SI-SDR 10.42 dB（基线 1.14 dB，+9.3 dB）、CER 13.24%、SPK-SIM 0.737；Track 2 同样大幅超基线（SI-SDR 9.54 dB）。追加 dynamic mixing 实验发现合成混合"提升音色保留但牺牲信号指标"的权衡。

### 🔧 技术方案
**问题背景：** 视听紧耦合模型在真实退化视频下不可靠，且大音频分离数据与稀缺视听数据难以联合训练；解耦可分别用大规模纯音频语料预训练分离器、用视听语料单独训练关联器。此前"分离+说话人验证选择"（SpeakerBeam/IVS+识别等）与脑电辅助增强的分离后选择范式表明该路线可行，但未迁移到 AVSE 与跨模态对比匹配。

**模型架构：** (a) 分离器：TF-GridNet（TAAB 结构，N=8/B=256/H=512/C=4 超参照原文），STFT 40ms 窗/10ms hop/平方根 Hann，2 路输出，SI-SNR+PIT；(b) 帧级 AV-CLIP：WavLM 50fps 音频帧嵌入经线性投影降至与 25fps 视频帧时间对齐（相邻两帧取平均），3D-ResNet18 逐帧视觉编码后接 2 层可训练 Transformer 捕获唇动时序，InfoNCE 双向（视听→频/音→视）帧级对齐，温度可学习；(c) 跨模态关联：对 2×2 音频—视频对归一化嵌入取逐帧余弦相似均值，两种一一对应中取总分高者完成排列消歧——无需注册语句、无需显式说话人模型。

**核心创新：** (1) 段级 AV-CLIP（Synchformer 式）改为**帧级对比**，使表征直接编码唇动—声学的细粒度时间对应，匹配分即同步度，把关联问题变成无需阈值的两排列枚举打分。(2) 只训练投影层+小 Transformer（约 2M 参数）、冻结 WavLM/3D-ResNet18 主干——数据高效的 AV-CLIP 配方，适配 LRS 规模的视听语料。(3) "纯音频分离 + 视听仅归属 + 无身份模板"是三解耦方案中最轻量的实例，同时提供域适应策略（Libri2Mix→官方 dev remix 微调）与 dynamic mixing 消融：再合成混合能提 SPK/CER 但伤 SI-SDR/感知指标，实证"再模拟也补不齐真实域差"。

**训练策略**：TF-GridNet 最长 150 epochs，Adam，batch 8，初始 LR 1e-3、两 epoch 验证不改进即减半；AV-CLIP 在 LRS 上 AdamW，LR 1e-4、前 10% epoch 线性 warm-up + cosine 退火，冻结双主干仅训投影层与 2 层 Transformer（hidden 256、FFN 512，约 2M 可训练参数）；分离器与 AV-CLIP 均在官方 dev remix 上域微调（注：HTML 版截断了 AV-CLIP 的 batch size 与完整 epoch 数，以 PDF 原文为准）。

### 📊 实验结果
**数据集**：Libri2Mix（预训练）+ AVSE dev（微调/验证）+ 官方 test

**主要指标**：
- Track 1：remix SI-SDR 10.42 dB、PESQ 2.65、STOI 0.823、CER 16.4%、SPK-SIM 0.737；mix 端 UTMOS 1.998、DNS-OVRL 1.770；OVRL 5.43
- Track 2：remix SI-SDR 9.54 dB、PESQ 2.55、CER 21.1%（mix）；OVRL 5.29
- 关键对比：两赛道全面超基线（SI-SDR +9.3/+8.2 dB，CER 相对下降 70%+）；与榜首 12.7 dB 差约 2.0~2.3 dB，差距主要源于 TF-GridNet 未经感知级多目标训练；dynamic mixing 使 Track2 both SPK 0.726→0.778？（原文表值截断，趋势为提音色降保真）

**是否开源**：暂无；基线依赖开源 TF-GridNet/WavLM/LRS3 生态。

### ⭐ 评分：6/10
评分理由：问题定义干净、方法组合简单正交（现成分离器+帧级对比匹配），解耦优势与域适应价值论证充分，dynamic mixing 消融诚实展示了合成再混合的局限；但相对安克/CF-AVSS/SUSA 技术差异化弱、AV-CLIP 与归属环节缺少对更差视觉条件（失同步/黑屏率）的专门增强，Track1/2 均排第五，实验与写作也略显仓促（若干超参数在版本中缺失/歧义）。工程参考价值高于学术新意。

---

## 横向对比与趋势总结

| 排序依据 OVRL | 队伍/论文 | 技术路线 | 视频用途 | SI-SDR(T1/T2) | 关键长板 | 评分 |
|---|---|---|---|---|---|---|
| 1(并列)/1 | 安克 172 | 纯音频分离 + AVSelector | 归属（不进重建） | 12.72/12.26 | 保真四项指标第一 | 8 |
| 1(并列)/2 | 腾讯 174 | SPAV-TFGridNet 粗→细全融合 | 条件重建+排序 | 10.70/10.22 | 双赛道最低 CER | 8 |
| 4/4 | 依加鹤 167 | 纯音频 TIGER-M + 多证据归属 + 认证后处理 | 归属 | 10.23/8.93 | mix 感知质量最高/数据贡献 | 7 |
| 5/5 | 南科大 159 | TF-GridNet + 帧级 AV-CLIP | 归属 | 10.42/9.54 | 最轻量解耦模板 | 6 |

**四点观察**：(1) "视频只做归属"已成 2026 年真实 AVSE 的主流赢家策略——解耦派前三独占两席，唯一坚持视觉全融合的 CF-AVSS 以最低 CER 保住并列第一，说明视觉对重建仍有下游价值；(2) 赛制驱动"指标工程"盛行：可微 PESQ/UTMOS/CER/SPK 全家桶几乎是前三标配，同时暴露 UTMOS/DNSMOS 与保真指标的系统性分歧（总览论文 §4.3），对评测生态是重要预警；(3) 域差是第一瓶颈：Libri2Mix 系（159）远弱于会议语料模拟系（167）与挑战赛数据微调系（172），再合成混合（dynamic mixing）证明补不齐真实域差；(4) Track2 几乎不分胜负（头部两队 SI-SDR 掉幅<0.5 dB），视觉退化的真正考题只剩"归属正确性"，未来 3+ 说话人、相似嗓音条件才会重新拷问全融合路线（总览结论一致）。

*Generated on 2026-10-15 by vagent；信息源：ISCSLP 2026 录用列表 + arXiv 2608.23759v3 / 2608.09288v1 / 2608.14812v1 全文精读。*
