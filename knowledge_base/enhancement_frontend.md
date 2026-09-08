# ENHANCEMENT FRONTEND（按评分降序）

共 25 篇

## [13 Prototype-Rectified Iterative Self-supervised Manifold Denoising under Severe Acoustic Shift](https://arxiv.org/abs/2608.15037)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：9/10 | **日期**：2026-08-18
- **一句话贡献**：音频-文本基础模型（ATM，如 CLAP）在严重声学噪声下性能骤降，现有 TTA 方法或依赖梯度而放大噪声，或需特权噪声标注。论文提出 PRISM（原型修正迭代自监督流形去噪），一个训练无关、源无关、噪声提示无关的 transductive TTA 框架：基于 Affine Noise Hypothesis 将严重噪声视为潜空间低秩仿射变形，以冻结文本原型为几何锚，用 OPCA、CCVD、逐类平移
- **关键技术点**：** 三类现有方法均不匹配恶劣声学环境：静态几何对齐（协方差白化、线性探测）将噪声视为刚性整体平移，无法应对每个环境独特的旋转/平移/低秩变形；梯度 TTA（TENT 等）在 <0dB 多音噪声下产生确认偏差，把高置信伪标签反馈回循环等于在噪声底上训练；提示优化（TPT、ContextDA）需推理时不可得的噪声类型特权标注且迭代反传与实时流不兼容。
- **主要指标**：
- **代码**：https://github.com/Ashish-1108/PRISM | **Demo**：暂无

---
## [11 AnyBand: Unified Multi-Bandwidth Speech Extension](https://arxiv.org/abs/2608.00572)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-08-04
- **一句话贡献**：带宽扩展（BWE）旨在从窄带输入恢复缺失的高频信息。传统方法针对特定带宽设计，当输入带宽变化时需要重新训练。AnyBand将统一多带宽扩展重新表述为上下文频谱填充问题，使用频率感知Diffusion Transformer（DiT）将观测到的低频段作为频率域prompt，条件化生成高频段。在VCTK数据集上，2kHz输入：LSD 1.248, NISQA 3.125, STOI 0.8214；8k
- **关键技术点**：** 实际场景中语音信号的带宽可能因采集设备、传输条件等而变化（如2kHz、4kHz、8kHz），传统BWE方法需要为每个带宽训练专门的模型。理想方案应该用一个统一模型处理任意输入带宽，同时支持规则和不规则（如缺失中频段）的频谱填充。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [12 DroneAudioNet: Noise Suppression for Drone Audition-based Search and Rescue](https://arxiv.org/abs/2608.00875)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-08-04
- **一句话贡献**：无人机搜救中，螺旋桨噪声在混合信号中占主导地位，信噪比低至-10 dB以下，传统语音增强方法效果有限。本文提出DroneAudioNet，将源分离模型重新表述为无人机噪声估计器，引入可学习mask缩放（允许mask幅度>1）和加性复数残差校正项。在公开无人机听觉数据集上，人类语音分类F1分数最大提升10.6%（-20到-10 dB SNR），在域外DREGON数据集上验证了泛化能力。
- **关键技术点**：** 无人机麦克风在搜救任务中捕捉人类语音时，螺旋桨噪声通常比语音信号高10-20 dB，形成极低SNR的混合信号。传统语音增强方法（如频谱减法、Wiener滤波）和通用源分离模型（如Conv-TasNet）在接近平衡的混合信号上设计，在无人机噪声主导场景下性能严重退化。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement](https://arxiv.org/abs/2608.07423)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-08-07
- **一句话贡献**：低延迟、低计算量的语音增强对可穿戴设备至关重要，但严格计算约束严重限制设备端性能。该工作提出云边协作框架，包含三种技术：(1) 延迟服务器输出作为额外输入，(2) 层特征增强（FiLM 调制）传输中间服务器表示指导边缘推理，(3) 协作多通道 Wiener 滤波（MCWF）融合服务器和边缘估计的加权协方差矩阵。在 DNS-Challenge 模拟数据上，完整框架相比仅边缘基线在标准条件下 SI-S
- **关键技术点**：** 可穿戴设备实时通信需要低延迟语音增强，但边缘模型容量受限。知识增强（Knowledge Boosting）已被提出，但语音增强性能提升有限，因为非平稳噪声的快速谱变化在通信延迟存在时难以处理。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 HybridSB-MoE: Dual-Domain Schrödinger Bridges with Scene-Adaptive Expert Routing for Speech Enhancement](https://arxiv.org/abs/2608.12715)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-08-13
- **一句话贡献**：生成式语音增强面临三个结构性差距：谱域模型捕获谐波结构但破坏相位，时域模型保持相位但丢失谐波，薛定谔桥（SB）缩短噪声到干净语音的传输路径但推理步数与训练松散关联。HybridSB-MoE 提出双域框架，包含三个核心贡献：(1) 非对称不确定性融合——谱域路径通过专家分歧捕获认知不确定性，时域桥路径通过随机动力学建模偶然不确定性；(2) 异构 MoE——top-k=2 路由跨越五种不同架构原型，架
- **关键技术点**：** 语音增强面临三个关键挑战：(1) 单域承诺——现有方法在时域或频域操作，牺牲了另一域的互补归纳偏置；(2) 均匀处理异质噪声——单一网络同时处理平稳家电嗡鸣、谐波引擎噪声和非平稳人群噪声，这三类噪声需要结构不同的处理策略；(3) 松散控制的采样成本——生成式 SE 通常需要多次迭代细化步，训练目标与推理预算之间缺乏形式化联系。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [14 A Novel Binaural Cue Preservation Loss for DNN-Based Binaural Speech Enhancement](https://arxiv.org/abs/2608.16299)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：面向助听器 DNN 双耳语音增强，本文提出两种新颖双耳线索保持损失以缓解降噪引入的通道间关系畸变：双耳重建误差损失（L_BRE）直接惩罚时频掩蔽对左右谱关系的破坏，联合双耳线索损失（L_BC）将 ILD 与 IPD 在复单位圆上联合建模以规避相位缠绕。与 SOTA 的 L_ILD+10·L_IPD 基线 cue loss 相比，两种损失均保持接近仅降噪模型的 SI-SDR 与 MBSTOI，同时降
- **关键技术点**：** 现有 DNN 双耳语音增强普遍以独立的 ILD 误差与 IPD 误差加权项作为空间保持目标。其缺陷有三：直接相位相减在 ±π 边界受相位缠绕干扰；误差均基于增强输出，无法隔离 T-F 掩蔽本身引入的通道间畸变；显式 cue 损失通常以牺牲降噪性能为代价。且评估缺乏统一标准。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 SlimDiffuSE: Towards Efficient Diffusion-Based Speech Enhancement using Slimmable Networks](https://arxiv.org/abs/2608.21188)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-08-24
- **一句话贡献**：扩散生成模型虽在语音增强上达到先进水平，但因需在大量反向扩散步中反复评估庞大模型而计算开销巨大。本文提出 SlimDiffuSE，将可瘦身网络（slimmable network）引入扩散增强：用利用率因子 u 控制每步激活的网络宽度，多宽度联合训练，并按步动态调度容量。实验证实早期时步需高容量、后期低容量即可，随后用贪心搜索求出最优宽度调度，在 DNS 测试集上相比高复杂度基线削减 87.5% 
- **关键技术点**：** 判别式 DNN 方法在中高 SNR 表现良好，但在低 SNR 下性能骤降；生成式方法可重建被噪声完全掩蔽的内容。基于 SDE/DDPM 的扩散增强（如 SGMSE+）性能领先，然而 PC 采样需要 N 步、每步评估体量巨大的分数网络，总计算量 C_total=2N·FLOPs(Sθ)，与去噪任务的实际难度无关，难以部署到实时或资源受限设备。已有的剪枝需维护多套网络，早退仅改深度而缺乏宽度维度的灵活调度。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 μNet: Ultra-Low-Memory and Low-Complexity Speech Enhancement for Embedded Digital Signal Processors](https://arxiv.org/abs/2608.21155)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-08-24
- **一句话贡献**：针对嵌入式DSP上语音增强对内存、计算量、延迟与整型运算支持的严苛约束，本文提出超低内存低复杂度端到端模型 μNet。该模型仅需 90 KB 静态内存与 28 MMACs，支持低至 4 ms 的算法延迟，可实现完整 int8 量化。在 DNS Challenge 数据集上，μNet_MSE 取得 4.03 BAK(MOS)、PESQ 1.90 与 13.24 dB SI-SDR，MUSHRA 主观
- **关键技术点**：** 主流DNN语音增强模型计算复杂度和内存占用大，且普遍工作于 10–40 ms 高延迟区间，难以满足助听器、透明模式耳穿戴设备及直播对话增强对超低延迟的硬性需求；这些场景依赖 Cadence HiFi 4/5 等资源受限消费级 DSP，通常只允许整数运算。现有低延迟方案（非对称窗、可学习变换、未来帧预测等）尚未同时统一解决延迟、内存与 int8 定点运算的联合优化。
- **主要指标**：
- **代码**：暂无 | **Demo**：https://sshetu-iis.github.io/uNet/ulm/

---
## [4 Ouroboros: Self-Referential Backdoor Attacks on Speech Enhancement via Clean Audio Triggers](https://arxiv.org/abs/2608.30329)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-08-31
- **一句话贡献**：本文首次系统研究语音增强模型的后门攻击。现有后门方法仅面向分类任务且依赖推理阶段主动注入触发器，与语音增强模块的被动处理特性矛盾。作者提出 CleanTrigger 机制，将训练集中的纯净目标语音作为天然触发器，构建自指式攻击框架 Ouroboros，仅需训练数据投毒、无需推理期干预。在 VB-DEMAND 与 WSJ0-CHiME3 上对 MP-SENet、SEMamba、CMGAN、FlowS
- **关键技术点**：** 语音增强常作为实时语音服务的被动预处理模块部署，攻击者无法在推理期可控修改用户音频流，因此传统依赖主动注入人工触发器（超声波、加性噪声、特定片段）的后门威胁模型不成立；现有音频后门研究又局限于关键词唤醒、说话人识别等分类任务。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [9 U-PAST: A Phase-Aware Audio Spectrogram Transformer-U-Net for Single-Channel Speech Enhancement](https://arxiv.org/abs/2609.00431)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：CNN在语音增强中只能通过逐层卷积间接捕获长程时频依赖。本文提出U-PAST，一种混合Transformer-U-Net结构，在复数谱图域通过自注意力显式建模依赖。它将复数STFT切分为token，送入多层Transformer编码器，再用U-Net式解码器重建增强复数谱图。在DNS Challenge、VoiceBank-DEMAND、LibriMix上以1.17M~2.40M参数评测4种变体，
- **关键技术点**：** 传统CNN/时域增强模型依赖局部感受野，长程时频依赖难以直接建模，失配场景泛化受限。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 Test-time adaptation for speech enhancement with an autoregressive speech prior](https://arxiv.org/abs/2609.03622)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：监督语音增强在训练/测试条件失配时性能显著退化。本文提出单句测试时自适应（TTA）方法：在NAC隐空间训练自回归干净语音先验，对单个无标注带噪语句，仅通过最小化增强语音分布与该先验的KL散度来微调预训练增强模型，全程无需干净标签或源域数据。在DNS Challenge V5与TIMIT-DEMAND等失配数据集上DNSMOS OVRL分别提升+0.18与+0.15。
- **关键技术点**：** 监督SE模型在噪声类型、混响等与训练分布失配时明显退化。现有方案各有局限：监督微调与UDA需带标签源数据；TTT约束原始训练流程；RemixIT依赖伪标签；掩码熵极化仅适用时频掩膜类SE。本文目标是对预训练SE模型仅用目标域单条无标注语音完成源自由自适应，且不修改训练流程。
- **主要指标**：
- **代码**：https://sofienekammoun.github.io/TAAP-SE/ | **Demo**：https://sofienekammoun.github.io/TAAP-SE/

---
## [2 Discriminative Flow Matching: Beyond Time-Conditioning in Generative Restoration via Flow-State Representations](https://arxiv.org/abs/2609.04525)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：条件流匹配（CFM）以显式时间坐标 t 同时驱动插值路径与速度网络的条件化，但恢复任务中源与目标分布统计相关（目标信号内嵌于含噪输入），同一 t 可能对应不同的退化程度与传输进度，时间条件存在固有歧义。本文提出判别式流状态假设并据此提出判别式流匹配（DFM）：用冻结判别式增强模型编码器提取的判别式流状态表征（DFSR）替代显式时间 t 条件化速度网络，并实现样本自适应推理。在 Interspeec
- **关键技术点**：** CFM 的目标向量场随时间变化，故需用 t 条件化速度网络。标准 OT-CFM 中源与目标统计独立，流状态 S(p_t)=W_2(p_t,p_1) 满足线性关系，t 是传输进度的可靠代理。但恢复任务初值 x_0=αx_1+βν，命题 2 证明存在不同的 (α,β,t) 组合产生相同边际分布，即同一状态可在不同 t 达成，全局插值坐标无法无歧义描述传输进度；近期工作（如 ARF）直接移除时间条件化，又丢失按进度自适应调节速度的机制。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [16 Separate First, Then Associate: A Two-Stage Approach for Real-World Audio-Visual Speech Enhancement](https://arxiv.org/abs/2608.14812)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：
- **一句话贡献**：
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [8 Training DeepFilterNet with Accurate Room Acoustic Simulations Improves Single-Channel Speech Enhancement](https://arxiv.org/abs/2608.20971)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-08-24
- **一句话贡献**：论文系统研究合成房间冲激响应（RIR）数据集真实度对单通道语音增强模型DeepFilterNet3训练效果的影响，对比基于镜像源法（ISM）的DNS4标准RIR数据集与采用混合波动/几何声学仿真生成的Treble高保真数据集。在保持模型与训练流程不变的前提下，全部8种训练配置下高保真数据集均带来稳定但温和的客观指标提升，并在未见实测RIR环境上将ASR词错误率（WER）从0.1663降至0.127
- **关键技术点**：** 消费与嵌入式设备普遍采用单麦克风采集，缺乏空间信息使增强极具挑战。主流深度增强方法依赖改进源法（ISM）生成RIR做数据扩充，但ISM基于镜面反射假设，无法刻画衍射、干涉、房间模态等波动现象，且DNS4数据集使用单一均匀吸声系数近似整个房间，低频与中频建模误差显著。Gusó等曾为DeepFilterNet3隔离研究频变吸收与声源指向性等单因素，本文则从实用数据集生成视角对比完整流水线的整体真实度。
- **主要指标**：
- **代码**：https://github.com/TrebleTechnologies/iwaenc2026milo | **Demo**：暂无

---
## [5 StrixAE: An Intelligent Agent for Audio Enhancement under Complex Distortion Coupling in Real-World Scenarios](https://arxiv.org/abs/2609.03414)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：StrixAE面向真实世界中噪声、混响、干扰说话人等多失真耦合与个性化增强并存的难题，提出以MLLM（Audio-Reasoner）为控制器、编排多个开源专家增强模型作为工具的音频增强智能体范式。采用"CoT监督微调+音频感知强化学习（APRL）"两阶段训练。在真实盲测集上全面超越TF-GridNet等开源方法，多数指标优于部分闭源方案。
- **关键技术点**：** 现有音频增强要么单任务方法、要么全一模型，二者均无法同时应对真实场景未知组合的复合失真与按人定制需求；标注含混合失真的配对数据稀缺，且缺乏统一基准评测泛化性。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 Model-Agnostic Meta-Learning Initialization for Distributed Multichannel Active Noise Control](https://arxiv.org/abs/2607.29117)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-07-31
- **一句话贡献**：分布式多通道主动噪声控制（DMCANC）是大面积降噪的可扩展框架，但现有方法依赖零或随机初始化，导致自适应滤波器收敛缓慢，限制了节点间协作效率。本文提出基于模型无关元学习（MAML）的初始化策略，通过聚合不同节点和声学环境的异构声学特征（主通道和次通道脉冲响应），学习可泛化的初始控制滤波器系数。在6节点DMCANC系统上验证，使用宽带噪声（100-2000Hz多种范围）进行MAML训练。结果表明该
- **关键技术点**：** DMCANC系统中多个节点独立运行本地单通道ANC控制器并通过间歇通信交换信息实现全局控制。现有DMCANC实现依赖零或随机初始化，在时变噪声和大规模系统中收敛缓慢。自适应滤波器初始化对ANC系统收敛行为至关重要，但DMCANC领域此前未系统研究。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 Neural Array-Generic Direction-of-Arrival Estimation Exploiting Array Transfer Functions](https://arxiv.org/abs/2608.09425)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：DOA 估计是多通道音频处理的关键组件，但许多深度学习方法与训练时使用的麦克风阵列绑定，对未见设备泛化差。该工作提出阵列通用神经 DOA 估计框架，使用测量或模拟的复值方向阵列传递函数（ATF）匹配真实多麦克风设备。使用独立卷积编码器处理多通道频谱图和 ATF 元数据，通过交叉注意力融合表示，使用多源笛卡尔向量输出预测源方向。在混响和扩散噪声下的模拟 2D 和 3D 定位任务中，方法泛化到未见阵列
- **关键技术点**：** 现有神经 DOA 方法通常针对特定阵列配置训练，当部署到不同阵列（如不同麦克风数量、几何形状）时性能严重下降，需要重新训练。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [8 DAVE: A Decoupled Audio-Visual Enhancement Framework for Real-World Speech Separation](https://arxiv.org/abs/2608.09288)

- **方向**：语音大模型（语音前端） | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：真实世界条件下音视频语音增强因不可靠的视觉输入和缺乏大规模真实声学条件训练数据而具有挑战性。现有方法通常将视觉特征直接融合到分离网络中，使其对退化视觉信号脆弱。DAVE 提出解耦音视频增强框架：构建 DAVE-Corpus（219,411 个混合样本，从公共会议语料库通过组合声学增强生成），引入渐进多目标优化策略联合改善语音分离、可懂度、说话人身份保持和感知质量，发展认证选择性增强链（仅对无参考分
- **关键技术点**：** 真实世界中视觉输入可能被遮挡、模糊或低光，现有方法将视觉特征直接融合到分离网络，使系统在视觉退化时性能严重下降。同时缺乏大规模真实声学条件的训练数据。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [9 RT-SEMamba: Real-Time Speech Enhancement with Progressive Knowledge Distillation](https://arxiv.org/abs/2608.12099)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-08-12
- **一句话贡献**：RT-SEMamba提出基于因果Mamba的实时语音增强模型，并采用渐进式知识蒸馏策略将8层教师模型压缩为1层学生模型。因果时频Mamba块在保持Mamba状态空间模型高效序列建模能力的同时，引入因果约束实现实时流式处理。在Voicebank-DEMAND上，8层教师PESQ达3.32，蒸馏后的1层学生PESQ 3.18（优于朴素1层模型的3.06），推理速度提升2.75倍。
- **关键技术点**：** 状态空间模型（如Mamba）在语音增强中展现出潜力，但非因果Mamba无法用于实时场景。同时，Mamba模型的计算开销与层数成正比，如何在保持增强质量的同时大幅降低推理延迟，是实现实时部署的关键。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [10 Rethinking LM-Based Generative Speech Enhancement](https://arxiv.org/abs/2608.12082)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-08-12
- **一句话贡献**：本文提出统一比较框架，系统评估了6种基于语言模型（LM）的生成式语音增强范式，包括离散域（D/CAR, D/CNAR）和连续域（DDiff, CFM）方法。研究发现连续域方法整体优于离散域方法，其中CNAR（条件非自回归）在离散域中表现最佳。辅助损失微调显著提升DNSMOS、NISQA、PESQ和POLQA指标。在URGENT 2025数据上完成实验。
- **关键技术点**：** 基于语言模型的生成式语音增强方法近年来涌现出多种范式，但缺乏统一的比较框架。不同方法在离散域vs连续域、自回归vs非自回归、扩散vs流匹配等维度上的优劣缺乏系统性分析。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [9 A Regularized Block Diagonal RLS Algorithm for Acoustic Echo Cancellation](https://arxiv.org/abs/2608.20693)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-08-24
- **一句话贡献**：针对经典RLS算法计算复杂度高达O(N²)、且长滤波器下数值不稳定而难以在资源受限设备上实时部署的问题，本文提出正则化分块对角RLS算法（RBD-RLS）。该算法将N阶自相关矩阵近似为M个L×L分块对角结构（N=ML），把大规模矩阵递归更新分解为互相独立可并行的子块运算，复杂度降至O(NL)；同时对每个子块施加Tikhonov正则化以保证初始阶段数值稳定。在N=512、最优配置（λ=0.9999,
- **关键技术点**：** AEC需用自适应滤波实时估计回声路径h(n)。NLMS等LMS族复杂度仅O(N)，但输入强相关（如语音）时收敛慢；RLS利用输入二阶统计量，收敛最优，但每步更新P(n)含O(N²)矩阵运算，滤波器阶数N通常为512~2048，且P(n)递归中减法易在有限精度下破坏正定性，导致增益向量发散。FRLS虽将复杂度降至O(N)，但数值不稳定；RLS-DCD数值稳健，却仍隐含O(N²)的数据拷贝开销，通用处理器上延迟不可接受。上述矛盾促使作者寻求兼顾收敛、复杂度与数值稳定性的折中方案。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 Array-Agnostic Ambisonics Encoding via Diffusion Posterior Sampling](https://arxiv.org/abs/2608.24558)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：现有 Ambisonics 编码方案受固定麦克风阵列布局限制。本文提出生成式框架 ADEPS（Array-agnostic Diffusion Encoding via Posterior Sampling），将物理采集模型嵌入扩散后验采样推理过程，从而补偿阵列失真并实现对任意麦克风阵列的零样本编码，性能优于传统基线。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 GAN-based Joint Dereverberation and Directional Filtering](https://arxiv.org/abs/2608.26403)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：神经方向滤波（NDF）可在紧凑阵列上按期望指向性模式重建虚拟指向性麦克风（VDM）信号，但强混响会破坏空间线索，而一阶心形的方向性指数仅约4.8 dB、难以抑制混响能量。本文提出NDDF，将去混响与方向滤波统一为单一学习问题，直接从阵列输入重建去混响VDM信号，并用判别式与GAN两种范式实现。实验表明NDDF全面超越级联基线（一阶目标、RT60=0.2s时PESQ 4.34 vs 3.08，fwS
- **关键技术点**：** NDF通过学习理想指向性麦克风的输入输出行为，可在小孔径阵列上获得高指向、频率无关的响应，但高指向对应窄主瓣，而X-Y立体声等录音格式要求固定的一阶心形（DI仅约4.8 dB），在强混响下无法抑制反射能量，重建的VDM混响严重、空间线索被掩盖。级联"去混响前端+NDF"流水线逐级独立优化，各级最优未必导致整体最优，因而需要统一公式同时处理去混响与方向滤波。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 Low-Power End-to-End Cochlear Implant Speech Denoising with Spiking Neural Networks](https://arxiv.org/abs/2608.28493)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：人工耳蜗（CI）可帮助重度至极重度听障人群恢复听觉，但用户在噪声环境下仍难以理解语音。现有基于深度神经网络（DNN）的增强方案虽有效，却因能耗过高不适合低功耗CI处理器。本文提出一种受Deep ACE架构启发的脉冲神经网络（SNN），以单一网络端到端同时完成语音增强与CI编码两项任务。实验表明，该模型在声码化短时客观可懂度（VSTOI）和信噪比改善量（SNRi）上与Deep ACE持平，同时能耗降
- **关键技术点**：** CI处理链需在受限功耗与体积的硬件上将麦克风信号实时转为电刺激脉冲，噪声环境下倾听尤为困难。Deep ACE等深度方案用DNN联合增强与编码，效果显著但乘法密集、功耗高，难以嵌入电池供电的CI处理器。SNN采用事件驱动的二值脉冲通信，能耗极低且天然适配神经形态硬件，但如何在不损失CI编码性能的前提下实现低功耗增强尚待解决。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [11 ABSE-NET: A Lightweight Neural Model for Active Binaural Speech Enhancement in Open-Fit Hearing Aids](https://arxiv.org/abs/2609.00966)

- **方向**：语音前端 | **子方向**：Enhancement | **评分**：7/10 | **日期**：2026-09-01
- **一句话贡献**：开放式助听器因佩戴舒适广受关注，但开放设计造成耳道声学泄漏，使现有双耳语音增强（BSE）性能下降。本文提出ABSE-NET，将主动噪声控制（ANC）与BSE结合的主动框架，级联双耳MVDR与轻量级神经网络（LNN），同时增强目标语音并抑制声学泄漏，且部署时无需耳内麦克风。
- **关键技术点**：** 开耳式助听器因耳道开放造成声学泄漏，传统BSE无法处理。早期方案需额外耳内麦克风。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
