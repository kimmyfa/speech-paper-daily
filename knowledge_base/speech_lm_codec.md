# SPEECH LM CODEC（按评分降序）

共 16 篇

## [1 EntangleCodec: A Unified Discrete Audio Tokenizer via Semantic-Acoustic Entanglement](https://arxiv.org/abs/2606.02739)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：9/10 | **日期**：2026-06-01
- **一句话贡献**：现有音频分词器难以同时支撑理解与生成：重建导向codec声学保真但语义匮乏，语义导向分词器多采用语义/声学双流结构造成冗余与错位。EntangleCodec提出在量化前通过CLIP式对比学习，将音频与LLM生成的多维rich caption对齐，把语义-声学信息纠缠进单一共享表征流，并配Rectified Flow扩散解码器。重建UTMOS 3.96接近专用codec（Xcodec2 4.02）；
- **关键技术点**：** 音频语言模型需要既语义丰富又声学保真的离散token，但重建导向与语义导向两类tokenizer各执一端；后者多采用独立语义流+双编码器，需要后期融合，且监督多为ASR文本，丢失说话人、情感、韵律、声场与音乐结构等非文本语义。作者认为双流分离是冗余的根源，主张在单编码器内于量化前一次性纠缠语义与声学。
- **主要指标**：
- **代码**：https://github.com/luckyerr/EntangleCodec | **Demo**：暂无

---
## [2 LILAC: An Idempotent Neural Speech Codec](https://arxiv.org/abs/2608.05727)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：9/10 | **日期**：2026-08-06
- **一句话贡献**：现有神经音频编解码器不是幂等的——12 个基线系统在单次解码-重编码周期中平均至少重写 15% 的 token，多次循环后质量严重退化。LILAC 是首个在设计上保证幂等的全卷积 24kHz 语音编解码器（0.75 kbit/s, 9.375Hz），利用可逆分析变换（可逆 1×1 卷积 + 加性耦合块）和有限标量量化（FSQ）实现结构级幂等性保证。在 LibriSpeech 和 LibriTTS-
- **关键技术点**：** 神经编解码器作为 token 接口在语音生成管线中广泛使用，但重编码解码输出会导致 token 漂移：EnCodec 一次循环后仅 80.5% token 一致，Mimi 32.9%，FocalCodec 10.9%，DAC 1.7%。现有方法（Code Drift, ICASSP 2025）通过辅助损失缓解但无法消除。
- **主要指标**：
- **代码**：https://github.com/Rick-McCoy/lilac-codec | **Demo**：https://rick-mccoy.github.io/lilac-demo

---
## [5 Speaker-Normalized Semantic Speech Tokens via Iterative S2U-T2U Refinement](https://arxiv.org/abs/2608.16235)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：语义语音 token 应保留语言内容、抑制说话人与时长信息，但现有 S2U tokenizer 常继承这些声学因素。本文提出 ISTP（迭代语义 token 提纯）：通过迭代 S2U-T2U 交替训练，以 T2U 预测与文本一致性作为提纯信号，逐步将对齐导向文本可预测的 token 空间。中英文实验表明 S2U-T2U 一致性强鲁棒提升（WER 降 72.0%-86.7%，BLEU 增 58.88
- **关键技术点**：** 现有 S2U tokenizer（如 HuBERT 量化）保留说话人、韵律和时长信息，同内容不同说话人产出不同 token 身份或序列长度，给 T2U 建模和隐私带来困难。已有方法依赖声学扰动（R-Spin）、并行话语（PINT）或对齐约束，且 BT4ST/DUB 等 T2U 反向翻译仅生成伪数据、不改动 tokenizer 本身。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://arxiv.org/abs/2609.04102)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对Apple端上Dictation等常驻音频tokenizer与稀疏激活大模型共享DRAM预算的问题，本文提出在预量化潜空间做编码器蒸馏的压缩配方：学生编码器在平方误差目标下回归教师逐帧潜变量，仅加一层仿射层弥合宽度差，无需标签、无需微调即以2.8倍压缩在六组师生对中的五组保持相对WER损失≤1.9%，并比同容量独立训练的tokenizer相对改善3.9%。
- **关键技术点**：** 系统级Dictation的tokenizer（每80ms输出一个向量）常驻内存且与IFP剪枝的200亿参数稀疏模型共享DRAM预算，需至少2.8倍参数压缩且不损失识别精度。若在离散token或解码器输出上蒸馏，前者须穿过不可微argmin，后者让学生容量浪费在端上并不存在的解码器上，故目标选在量化与bridge之前、两种token接口共享的末层潜变量。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 EffVOC: Low-Delay Efficient Speech Waveform Reconstruction from Spectral Representations Without Phase](https://arxiv.org/abs/2609.04226)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-07-14
- **一句话贡献**：EffVOC 面向无相位谱表示的低延迟语音波形重建。现有方法中，Griffin-Lim 算法（GLA）算法延迟极高；RTISI 系列在 20 ms 延迟下质量骤降；DiffPhase、BAPEN 等神经网络方法依赖整句重建、延迟无限；BigVGAN、Vocos、MelFlow 等生成式声码器普遍存在 32 ms 以上延迟。EffVOC 在已有 20 ms 低延迟声码器基础上统一支持幅度谱与 Mel
- **关键技术点**：** GLA 及其快速变体需大量迭代、算法延迟极高；RTISI 虽延迟 20 ms，但缺少前视致重建精度严重下降。神经网络方法用生成式手段大幅提升质量，但依赖整句重建或延迟超 32 ms；MelFlow 用流匹配实现实时，仍为 32 ms 延迟。低延迟声码器目前仅支持 Mel 输入与宽带合成，幅度谱输入及更高带宽的适用性尚无定论。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [9 Rethinking Speech Codecs: From Compression to Autoregressive Generative Modeling](https://arxiv.org/abs/2609.04237)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-07-27
- **一句话贡献**：主流神经语音编解码器以压缩保真为目标训练，其离散 token 序列缺乏自回归建模所需的时序条件依赖，统计分布偏离自然语言的 Zipf 幂律，与 LLM 的下一个 token 预测范式严重错位，导致语音大模型续训效率低下。本文提出 ARDDS 编解码器训练框架：在 codec 训练中引入辅助自回归解码器，通过温度控制的软量化实现梯度回传，显式约束 token 序列的自回归可预测性；同时提出异构下采样
- **关键技术点**：** 现有语音编解码器以多尺度梅尔谱重建损失、LSGAN 判别损失等联合优化，仅关注率失真与感知质量，对 token 序列的时序结构没有任何约束。作者统计发现各代表 codec 的 token 频率-排名关系明显偏离文本 Zipf 幂律分布，token 缺乏可预测的条件依赖；且第一层语义 token 速率（如 XCodec 50 Hz）远高于对应文本，增加语音大模型续训练负担。这是"压缩目标"与"生成目标"的结构性错位。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation](https://arxiv.org/abs/2608.03021)

- **方向**：语音前端 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-08-05
- **一句话贡献**：神经音频编解码器是LLM音频生成的基础tokenizer。现有工作广泛使用语义先验增强语言可懂度，但显式声学先验的整合仍缺乏探索。MeloCodec提出"Tokenize-then-Fuse"范式，预训练独立的离散旋律分支锁定旋律结构（音高、节奏），再进行特征融合，解决直接融合导致的优化不稳定问题。两阶段训练策略防止码本坍塌。在歌唱声音表示上优于基线，提升音高一致性，支持可控音高操控，最小化音色退
- **关键技术点**：** 神经音频编解码器（如EnCodec、DAC、SoundStream）将音频编码为离散token，作为LLM音频生成（如TTS、音乐生成）的输入。现有工作主要引入语义先验（如HuBERT、WavLM特征）提升可懂度，但显式声学先验（如旋律、音高、节奏）的整合尚未被充分探索。直接融合声学先验可能导致优化不稳定（如码本坍塌、收敛困难），特别是对于歌唱这类对音高敏感的领域。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 Multi Codec Discrete Diffusion Model for Text Guided Speech Inpainting and Editing](https://arxiv.org/abs/2608.06424)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-08-05
- **一句话贡献**：语音修复（inpainting）和编辑（editing）需要在不完全重新合成整个语音的情况下重建或修改缺失/错误区域。离散扩散天然适合该任务，因为它能迭代精炼 mask token 同时联合条件于左右声学上下文。SIEDD 提出分层多码本离散扩散框架 HiCoDD，遵循 RVQ 粗到细生成顺序，将先前生成的 codebook 表示为干净承诺声学上下文，仅对当前精炼 codebook 应用扩散。在 
- **关键技术点**：** 语音编辑中，自回归编解码器语言模型按固定因果顺序生成，无法同时利用左右上下文，早期错误会传播。离散扩散可同时条件于双边上下文并反复精炼，但简单将所有 RVQ codebook 扁平化处理会忽略粗到细的层次依赖。
- **主要指标**：
- **代码**：https://github.com/iftachShoham/SIEDD | **Demo**：暂无

---
## [5 BiMTokenizer: Preserving Semantic-Acoustic Balance in Low-Bitrate Speech Tokenization via Bidirectional State-Space Modeling](https://arxiv.org/abs/2609.00562)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：语音编解码器面临声学保真与语义保真的冲突。近期方案普遍采用双塔架构解耦语义与声学建模，但结构开销巨大。本文回归单塔范式，提出BiMTokenizer——约1.1 kbps的低码率编解码器，采用双向状态空间骨干结合残差球面网格量化（RSLQ）。实验在干净与噪声环境下均取得最优声学重建与最低WER，参数量不足双塔基线一半，下游语音理解任务上展现强语义表征。代码与权重已开源。
- **关键技术点**：** 传统低码率编解码器难以兼顾声学重建与语义保真；双塔架构虽缓解冲突却带来参数冗余。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [10 CRAW: Codec Robust Audio Watermarking](https://arxiv.org/abs/2609.03107)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-02
- **一句话贡献**：语音克隆技术使合成语音日益以假乱真，现有后验式音频水印在神经编解码器与降噪器下几乎全部失效。本文提出CRAW，在TimbreWatermark基础上用四项互补组件解决鲁棒性与保真度矛盾：扩宽的失真层（含FACodec再合成）、Q-Former式注意力池化、PESQ梯度推理期感知掩蔽、以及Rep3纠错码。CRAW在FACodec/EnCodec/TiCodec上F1达0.982/0.987/0.82
- **关键技术点**：** O'Reilly与RAW-Bench证实现有后验式水印（WavMark、AudioSeal等）在低码率神经编解码器或降噪器下检测率塌缩趋近随机，因为"再合成"变换整体重建波形而水印信号幅度远低于语音主体；生成式水印虽构造鲁棒却无法对已存在音频水印。CRAW目标是在后验范式内同时获得对神经再合成攻击的鲁棒性与高感知保真度。
- **主要指标**：
- **代码**：https://github.com/DavidC1212/craw | **Demo**：https://davidc1212.github.io/craw-audio-samples/

---
## [13 PACodec: A Low-bitrate Neural Speech Codec with Parallel Additive Vector Quantization](https://arxiv.org/abs/2609.03363)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对RVQ顺序依赖导致码编解码器码率难以下降的问题，提出并行加性矢量量化（PAVQ）的低码率神经语音编解码器PACodec。PAVQ采用"全局—局部—全局"设计，多个独立VQ并行量化同一全局特征、结果相加聚合。PACodec仅用4个码本大小为128的VQ即实现1.4 kbps（16kHz）与4.2 kbps（48kHz）码率，在同等音质前提下较基线省流约30%，参数量仅6.7M为所有模型中最小。
- **关键技术点**：** 主流神经语音编解码器皆采用残差矢量量化（RVQ），VQ间顺序依赖、逐级细化使得进一步降低码率困难，且不利于语音解耦任务。HiFi-Codec的GRVQ按通道分组引入部分并行但仍有RVQ依赖，SQCodec的FSQ需超大码本。PACodec从量化结构入手，用并行加性聚合替代残差迭代。
- **主要指标**：
- **代码**：暂无 | **Demo**：https://anonymity225.github.io/PACodec/

---
## [2 Masked Autoregressive Speech Enhancement with Continuous Neural Audio Codec Representations](https://arxiv.org/abs/2609.03940)

- **方向**：语音前端 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对基于NAC的SE研究大多依赖离散token、且缺少对不同解码策略权衡的系统研究，本文提出掩码自回归语音增强（MARSE），在连续NAC编码器输出上把迭代解码建模为分块自回归概率过程。在相同Conformer、相同DAC与训练设置下比较因果/非因果随机/非因果oracle三种解码策略。MARSE性能与开销介于C-NAR与C-AR之间，可灵活权衡。
- **关键技术点**：** 基于token的SE因离散量化损失对音质与可懂度至关重要的声学细节；近期研究证明使用DAC量化前的连续表示为音质与可懂度带来显著提升。同时token类方法通常各自固定一种解码策略、实验设置各异，缺少对"解码策略"维度的公平对比。
- **主要指标**：
- **代码**：https://yotofujita.github.io/marse | **Demo**：https://yotofujita.github.io/marse

---
## [4 StreamWSR: Streamable and Lightweight Waveform-Domain Neural Speech Super-Resolution](https://arxiv.org/abs/2609.03381)

- **方向**：语音前端 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：提出StreamWSR，全因果、轻量化的波形域语音超分辨率模型。针对现有语音SR依赖声码器重构或显式相位预测、难以零前瞻流式推理的问题，采用紧凑帧级波形表征和因果长短期建模骨干，在波形域端到端预测高频分量。在VCTK-0.92数据集8/4/2kHz→16kHz三档设置下，以仅9.03M参数、2.12G FLOPs取得与代表性基线相当或更优的质量与可懂度，支持零前瞻流式推理。
- **关键技术点**：** 语音SR需低算法时延还原缺失高频分量。波形域方法计算代价高或时延大；mel类需外接声码器，STFT类相位缠绕难以建模，显式幅相预测结构复杂，均难在零前瞻约束下兼顾信息保留与端到端优化。
- **主要指标**：
- **代码**：暂无 | **Demo**：https://tian1507.github.io/StreamWSR/

---
## [3 KVAE: Family of Tokenizers for Multimodal Generative Models](https://arxiv.org/abs/2608.05798)

- **方向**：多模态tokenizer | **子方向**：Codec | **评分**：7/10 | **日期**：2026-08-06
- **一句话贡献**：LDM的生成质量高度依赖tokenizer的latent空间特性，但重建指标无法可靠预测下游生成性能。KVAE系列提出面向音频、图像和视频的统一tokenizer方案：KVAE-Audio是48kHz全频带连续音频tokenizer（50Hz latent, 64通道）；KVAE-3D提供4×16×16和4×8×8两种因果视频tokenizer；KVAE-2D为8×压缩的32通道图像tokeniz
- **关键技术点**：** 视觉tokenizer的latent空间特性（diffusability）直接影响扩散模型的训练动态和生成质量，但重建指标（PSNR等）与下游生成性能之间存在reconstruction-generation dilemma。现有开源tokenizer如Wan-2.2（48通道）×16×16）、HunyuanVideo-1.5（32通道×16×16）在压缩率和通道数选择上各有局限。
- **主要指标**：
- **代码**：https://github.com/kandinskylab/kvae | **Demo**：暂无

---
## [10 Language-Statistical Analysis of Neural Audio Codec Tokens Across Architectures, Corpora, and Noise Conditions](https://arxiv.org/abs/2608.31037)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：神经音频编解码器（NAC）将语音转为离散token序列，此前研究声称其服从类语言统计定律。本文对13个NAC（覆盖多码本残差量化RVQ、单码本VQ与非VQ三类架构）在三个语料库、干净/白噪声/真实DEMAND噪声三种条件下系统估计Zipf与Heaps参数、unigram熵、码本占用率及JSD。结果显示：语料身份对各指标解释力极低，声学条件与量化器元类别按指标差异主导，unigram熵与元类别关联最
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [11 When Does Predictor-Based RL Align with Human Perception? A Study of Subjective Rewards in Codec-Based Speech Language Models](https://arxiv.org/abs/2608.31035)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：本文系统研究了基于预测器的强化学习（RL）奖励在编解码器语音语言模型中对齐人类感知的条件。使用 GRPO 算法，以动漫风格、自然度、喜好度和唤醒度四个主观预测器作为奖励，并引入 CER 区域约束防止转录漂移。实验发现：各奖励主要优化自身指标，不可互换；Best-of-8 重排在感知上与 GRPO 相当，表明 GRPO 本质是将奖励选择行为摊销到策略中，而非统一优于重排。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
