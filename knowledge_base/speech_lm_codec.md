# SPEECH LM CODEC（按评分降序）

共 18 篇

## [EntangleCodec: A Unified Discrete Audio Tokenizer via Semantic-Acoustic Entanglement](https://arxiv.org/abs/2606.02739)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：9/10 | **日期**：2026-06-01
- **一句话贡献**：现有音频分词器难以同时支撑理解与生成：重建导向codec声学保真但语义匮乏，语义导向分词器多采用语义/声学双流结构造成冗余与错位。EntangleCodec提出在量化前通过CLIP式对比学习，将音频与LLM生成的多维rich caption对齐，把语义-声学信息纠缠进单一共享表征流，并配Rectified Flow扩散解码器。重建UTMOS 3.96接近专用codec（Xcodec2 4.02）；
- **关键技术点**：音频语言模型需要既语义丰富又声学保真的离散token，但重建导向与语义导向两类tokenizer各执一端；后者多采用独立语义流+双编码器，需要后期融合，且监督多为ASR文本，丢失说话人、情感、韵律、声场与音乐结构等非文本语义。作者认为双流分离是冗余的根源，主张在单编码器内于量化前一次性纠缠语义与声学。
- **主要指标**：- 重建：Speech UTMOS 3.96（次佳Xcodec2 4.02）、LibriTTS UTMOS 3.94 - 理解（同Qwen3-0.6B）：MMAU-mini 34.2(+1.5)、MMAU 35.1(+2.5)、MMAR 34.3(+7.4) - 缩放：8B得56.2/52.6/42
- **代码**：https://github.com/luckyerr/EntangleCodec | **Demo**：暂无

---
## [LILAC: An Idempotent Neural Speech Codec](https://arxiv.org/abs/2608.05727)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：9/10 | **日期**：2026-08-06
- **一句话贡献**：现有神经音频编解码器不是幂等的——12 个基线系统在单次解码-重编码周期中平均至少重写 15% 的 token，多次循环后质量严重退化。LILAC 是首个在设计上保证幂等的全卷积 24kHz 语音编解码器（0.75 kbit/s, 9.375Hz），利用可逆分析变换（可逆 1×1 卷积 + 加性耦合块）和有限标量量化（FSQ）实现结构级幂等性保证。在 LibriSpeech 和 LibriTTS-
- **关键技术点**：神经编解码器作为 token 接口在语音生成管线中广泛使用，但重编码解码输出会导致 token 漂移：EnCodec 一次循环后仅 80.5% token 一致，Mimi 32.9%，FocalCodec 10.9%，DAC 1.7%。现有方法（Code Drift, ICASSP 2025）通过辅助损失缓解但无法消除。
- **主要指标**：- LibriSpeech: UTMOS 4.14, dWER 0.101, PESQ 2.60, STOI 0.935, SI-SNR +2.2 dB - LibriTTS-R: UTMOS 4.24, dWER 0.086, PESQ 2.60, STOI 0.944, SI-SNR +6.0 
- **代码**：https://github.com/Rick-McCoy/lilac-codec | **Demo**：https://rick-mccoy.github.io/lilac-demo

---
## [Speaker-Normalized Semantic Speech Tokens via Iterative S2U-T2U Refinement](https://arxiv.org/abs/2608.16235)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：语义语音 token 应保留语言内容、抑制说话人与时长信息，但现有 S2U tokenizer 常继承这些声学因素。本文提出 ISTP（迭代语义 token 提纯）：通过迭代 S2U-T2U 交替训练，以 T2U 预测与文本一致性作为提纯信号，逐步将对齐导向文本可预测的 token 空间。中英文实验表明 S2U-T2U 一致性强鲁棒提升（WER 降 72.0%-86.7%，BLEU 增 58.88
- **关键技术点**：现有 S2U tokenizer（如 HuBERT 量化）保留说话人、韵律和时长信息，同内容不同说话人产出不同 token 身份或序列长度，给 T2U 建模和隐私带来困难。已有方法依赖声学扰动（R-Spin）、并行话语（PINT）或对齐约束，且 BT4ST/DUB 等 T2U 反向翻译仅生成伪数据、不改动 tokenizer 本身。
- **主要指标**：- S2U-T2U 对齐：T0→T4 WER 相对降 72.0%-86.7%，BLEU 增 58.88-73.39 - TTS 英文 WER：Iter0 1.80 / Iter4 1.97，SIM 0.63→0.71；对比 CosyVoice3 2.02/0.72、MaskGCT 2.62/0.71
- **代码**：暂无 | **Demo**：暂无

---
## [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://arxiv.org/abs/2609.04102)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对Apple端上Dictation等常驻音频tokenizer与稀疏激活大模型共享DRAM预算的问题，本文提出在预量化潜空间做编码器蒸馏的压缩配方：学生编码器在平方误差目标下回归教师逐帧潜变量，仅加一层仿射层弥合宽度差，无需标签、无需微调即以2.8倍压缩在六组师生对中的五组保持相对WER损失≤1.9%，并比同容量独立训练的tokenizer相对改善3.9%。
- **关键技术点**：系统级Dictation的tokenizer（每80ms输出一个向量）常驻内存且与IFP剪枝的200亿参数稀疏模型共享DRAM预算，需至少2.8倍参数压缩且不损失识别精度。若在离散token或解码器输出上蒸馏，前者须穿过不可微argmin，后者让学生容量浪费在端上并不存在的解码器上，故目标选在量化与bridge之前、两种token接口共享的末层潜变量。
- **主要指标**：- Stage-0三对师生：WER +0.4%/+1.9%/+0.8% - 同容量独立训练基线12.36、蒸馏学生11.90 → 相对改善3.9% - Stage-1：J1 +1.5%、J2 -5.3%（全部反超教师）、J3 +7.7%（最大退化） - 消融：教师质量是学生WER最强预测因子；两种接
- **代码**：暂无 | **Demo**：暂无

---
## [EffVOC: Low-Delay Efficient Speech Waveform Reconstruction from Spectral Representations Without Phase](https://arxiv.org/abs/2609.04226)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-07-14
- **一句话贡献**：EffVOC 面向无相位谱表示的低延迟语音波形重建。现有方法中，Griffin-Lim 算法（GLA）算法延迟极高；RTISI 系列在 20 ms 延迟下质量骤降；DiffPhase、BAPEN 等神经网络方法依赖整句重建、延迟无限；BigVGAN、Vocos、MelFlow 等生成式声码器普遍存在 32 ms 以上延迟。EffVOC 在已有 20 ms 低延迟声码器基础上统一支持幅度谱与 Mel
- **关键技术点**：GLA 及其快速变体需大量迭代、算法延迟极高；RTISI 虽延迟 20 ms，但缺少前视致重建精度严重下降。神经网络方法用生成式手段大幅提升质量，但依赖整句重建或延迟超 32 ms；MelFlow 用流匹配实现实时，仍为 32 ms 延迟。低延迟声码器目前仅支持 Mel 输入与宽带合成，幅度谱输入及更高带宽的适用性尚无定论。
- **主要指标**：- MOS：F=64 幅度谱 4.17、F=32 Mel 4.15，对比 MelFlow 3.95、GLA 3.95、RTISI-DM 2.76，真实语音 4.20 - PESQ-WB：F=64 幅度谱 4.31（优于 BAPEN 4.26）；POLQA 4.45；LPS 0.976；ESTOI 0
- **代码**：暂无 | **Demo**：暂无

---
## [Rethinking Speech Codecs: From Compression to Autoregressive Generative Modeling](https://arxiv.org/abs/2609.04237)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-07-27
- **一句话贡献**：主流神经语音编解码器以压缩保真为目标训练，其离散 token 序列缺乏自回归建模所需的时序条件依赖，统计分布偏离自然语言的 Zipf 幂律，与 LLM 的下一个 token 预测范式严重错位，导致语音大模型续训效率低下。本文提出 ARDDS 编解码器训练框架：在 codec 训练中引入辅助自回归解码器，通过温度控制的软量化实现梯度回传，显式约束 token 序列的自回归可预测性；同时提出异构下采样
- **关键技术点**：现有语音编解码器以多尺度梅尔谱重建损失、LSGAN 判别损失等联合优化，仅关注率失真与感知质量，对 token 序列的时序结构没有任何约束。作者统计发现各代表 codec 的 token 频率-排名关系明显偏离文本 Zipf 幂律分布，token 缺乏可预测的条件依赖；且第一层语义 token 速率（如 XCodec 50 Hz）远高于对应文本，增加语音大模型续训练负担。这是"压缩目标"与"生成目标"的结构性错位。
- **主要指标**：- XCodec:ARDDS 下游：StoryCloze 70.1%（+6.4）、AISHELL-I CER 2.5%（-2.7）、SeedTTS WER 2.3%（-2.4） - 编解码器内在质量：重建 WER 4.13、SPKSIM 0.88、UTMOS 4.30、PESQ-nb 3.53，与基
- **代码**：暂无 | **Demo**：暂无

---
## [Multi Codec Discrete Diffusion Model for Text Guided Speech Inpainting and Editing](https://arxiv.org/abs/2608.06424)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-08-05
- **一句话贡献**：语音修复（inpainting）和编辑（editing）需要在不完全重新合成整个语音的情况下重建或修改缺失/错误区域。离散扩散天然适合该任务，因为它能迭代精炼 mask token 同时联合条件于左右声学上下文。SIEDD 提出分层多码本离散扩散框架 HiCoDD，遵循 RVQ 粗到细生成顺序，将先前生成的 codebook 表示为干净承诺声学上下文，仅对当前精炼 codebook 应用扩散。在 
- **关键技术点**：语音编辑中，自回归编解码器语言模型按固定因果顺序生成，无法同时利用左右上下文，早期错误会传播。离散扩散可同时条件于双边上下文并反复精炼，但简单将所有 RVQ codebook 扁平化处理会忽略粗到细的层次依赖。
- **主要指标**：- 语音编辑：WER 0.121（最佳），SIM 0.98（最佳），MCD 270.0（最佳），F0 Dist. 8.57，Energy Dist. 0.005 - 对比 VoiceCraft（WER 0.124, SIM 0.97, MCD 392.25）和 SSR-Speech（WER 0.14
- **代码**：https://github.com/iftachShoham/SIEDD | **Demo**：暂无

---
## [BiMTokenizer: Preserving Semantic-Acoustic Balance in Low-Bitrate Speech Tokenization via Bidirectional State-Space Modeling](https://arxiv.org/abs/2609.00562)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：语音编解码器面临声学保真与语义保真的冲突。近期方案普遍采用双塔架构解耦语义与声学建模，但结构开销巨大。本文回归单塔范式，提出BiMTokenizer——约1.1 kbps的低码率编解码器，采用双向状态空间骨干结合残差球面网格量化（RSLQ）。实验在干净与噪声环境下均取得最优声学重建与最低WER，参数量不足双塔基线一半，下游语音理解任务上展现强语义表征。代码与权重已开源。
- **关键技术点**：传统低码率编解码器难以兼顾声学重建与语义保真；双塔架构虽缓解冲突却带来参数冗余。
- **主要指标**：- 码率：约1.1 kbps - WER：低码率基线中最低 - 参数量：不足双塔基线一半
- **代码**：暂无 | **Demo**：暂无

---
## [CRAW: Codec Robust Audio Watermarking](https://arxiv.org/abs/2609.03107)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-02
- **一句话贡献**：语音克隆技术使合成语音日益以假乱真，现有后验式音频水印在神经编解码器与降噪器下几乎全部失效。本文提出CRAW，在TimbreWatermark基础上用四项互补组件解决鲁棒性与保真度矛盾：扩宽的失真层（含FACodec再合成）、Q-Former式注意力池化、PESQ梯度推理期感知掩蔽、以及Rep3纠错码。CRAW在FACodec/EnCodec/TiCodec上F1达0.982/0.987/0.82
- **关键技术点**：O'Reilly与RAW-Bench证实现有后验式水印（WavMark、AudioSeal等）在低码率神经编解码器或降噪器下检测率塌缩趋近随机，因为"再合成"变换整体重建波形而水印信号幅度远低于语音主体；生成式水印虽构造鲁棒却无法对已存在音频水印。CRAW目标是在后验范式内同时获得对神经再合成攻击的鲁棒性与高感知保真度。
- **主要指标**：- FACodec：CRAW 0.982 vs 最强基线AWARE 0.149 - EnCodec 6kbps（未见）：0.987 vs AWARE 0.252 - TiCodec（未见）：0.826 vs AWARE 0.075 - 降噪0dB（未见）：CRAW 0.944/0.956 - 保真度
- **代码**：https://github.com/DavidC1212/craw | **Demo**：https://davidc1212.github.io/craw-audio-samples/

---
## [PACodec: A Low-bitrate Neural Speech Codec with Parallel Additive Vector Quantization](https://arxiv.org/abs/2609.03363)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对RVQ顺序依赖导致码编解码器码率难以下降的问题，提出并行加性矢量量化（PAVQ）的低码率神经语音编解码器PACodec。PAVQ采用"全局—局部—全局"设计，多个独立VQ并行量化同一全局特征、结果相加聚合。PACodec仅用4个码本大小为128的VQ即实现1.4 kbps（16kHz）与4.2 kbps（48kHz）码率，在同等音质前提下较基线省流约30%，参数量仅6.7M为所有模型中最小。
- **关键技术点**：主流神经语音编解码器皆采用残差矢量量化（RVQ），VQ间顺序依赖、逐级细化使得进一步降低码率困难，且不利于语音解耦任务。HiFi-Codec的GRVQ按通道分组引入部分并行但仍有RVQ依赖，SQCodec的FSQ需超大码本。PACodec从量化结构入手，用并行加性聚合替代残差迭代。
- **主要指标**：- 1.4kbps：LSD 0.89、STOI 0.93、UTMOS 3.80、DNSMOS 3.26 - 4.2kbps：LSD 0.78、UTMOS 3.93、DNSMOS 3.17 - 同音质省流约30%（600bps/1.8kbps） - 消融：删VQ1→WER/CER升高（内容）；删VQ4
- **代码**：暂无 | **Demo**：https://anonymity225.github.io/PACodec/

---
## [Masked Autoregressive Speech Enhancement with Continuous Neural Audio Codec Representations](https://arxiv.org/abs/2609.03940)

- **方向**：语音前端 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对基于NAC的SE研究大多依赖离散token、且缺少对不同解码策略权衡的系统研究，本文提出掩码自回归语音增强（MARSE），在连续NAC编码器输出上把迭代解码建模为分块自回归概率过程。在相同Conformer、相同DAC与训练设置下比较因果/非因果随机/非因果oracle三种解码策略。MARSE性能与开销介于C-NAR与C-AR之间，可灵活权衡。
- **关键技术点**：基于token的SE因离散量化损失对音质与可懂度至关重要的声学细节；近期研究证明使用DAC量化前的连续表示为音质与可懂度带来显著提升。同时token类方法通常各自固定一种解码策略、实验设置各异，缺少对"解码策略"维度的公平对比。
- **主要指标**：- Libri1Mix（N=10）：MARSE-causal SIG 3.62/dWER 12.68/GFLOPs 1912 - 基线：C-AR 3.64/20.89/3856；C-NAR 3.60/12.84/1235 - 域外LibriDEMAND：MARSE-causal 3.54/3.11/
- **代码**：https://yotofujita.github.io/marse | **Demo**：https://yotofujita.github.io/marse

---
## [StreamWSR: Streamable and Lightweight Waveform-Domain Neural Speech Super-Resolution](https://arxiv.org/abs/2609.03381)

- **方向**：语音前端 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：提出StreamWSR，全因果、轻量化的波形域语音超分辨率模型。针对现有语音SR依赖声码器重构或显式相位预测、难以零前瞻流式推理的问题，采用紧凑帧级波形表征和因果长短期建模骨干，在波形域端到端预测高频分量。在VCTK-0.92数据集8/4/2kHz→16kHz三档设置下，以仅9.03M参数、2.12G FLOPs取得与代表性基线相当或更优的质量与可懂度，支持零前瞻流式推理。
- **关键技术点**：语音SR需低算法时延还原缺失高频分量。波形域方法计算代价高或时延大；mel类需外接声码器，STFT类相位缠绕难以建模，显式幅相预测结构复杂，均难在零前瞻约束下兼顾信息保留与端到端优化。
- **主要指标**：- 8kHz：LSD 0.73/ViSQOL 4.68；4kHz：0.92/4.27（优于TRAMBA）；2kHz：1.03/3.81 - 复杂度：9.03M参数、2.12G FLOPs（约为UDM+ 189G的1%） - 消融：频谱判别器换波形域后2kHz ViSQOL降至3.78
- **代码**：暂无 | **Demo**：https://tian1507.github.io/StreamWSR/

---
## [Clean Accuracy Does Not Guarantee Provenance Robustness: A Prospective Codec-Stress Evaluation of Audio Attribution](https://arxiv.org/abs/2609.07981)

- **方向**：语音前端 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-07
- **一句话贡献**：音频溯源归属（判断合成话语由哪个系统产生）在干净 benchmark 上报告接近满分，但分析师实际拿到的音频通常经过转码，性能大幅衰减。本文提出前瞻注册式测量协议：在训练任何归属模型前用保真元数据固定分析区域，评估单阶段 codec 转码后的 closed-set 归属。实验显示 WavLM-Base+ 在 support 内损失 53.5 与 70.3 点 Macro-F1，W2V2-BERT 
- **关键技术点**：音频溯源归属检测在实际取证中面对的音频几乎都经过转码传输，而现有评测多在无扰动干净信号上进行，导致近满分精度与真实性能脱节；衰减同时强依赖被测表征类型与 codec 条件，需要一个在训练前就固定评估范畴、避免选择偏差的协议。
- **主要指标**：- support 内损失：WavLM-Base+ 53.5 [43.5,63.6] 与 70.3 [63.0,77.5] Macro-F1；W2V2-BERT 2.0 61.0 [56.8,65.1] 与 49.8 [41.6,57.9] - 单一 support 网格内 WavLM 损失范围 -
- **代码**：暂无 | **Demo**：暂无

---
## [StreamAlign: Streaming Text-Aligned Speech Tokenization](https://arxiv.org/abs/2609.09719)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-09
- **一句话贡献**：StreamAlign 提出流式文本对齐语音分词框架：通过字符级 RNN-T 对齐与词级 ASR 引导的在线声学-文本对齐，配合 LLM 子词级聚合解决 ASR-LLM 词表不匹配；并引入前瞻性词边界分类器，将延迟从 560ms 降至 270ms。在 LibriSpeech 上取得最低 WER（4.41）与最高 UTMOS（4.23），其 SLM 在 speech continuation 上人类
- **关键技术点**：现有 text-aligned 分词（TASTE、TASLA）依赖离线 ASR，需完整话语才能分词，无法流式实时处理（延迟约 410ms+300ms）；且 ASR 与 LLM 子词词表不匹配，需在词级复制特征到各子词 token，丢失细粒度声学与副语言信息。
- **主要指标**：- WER：StreamAlign 4.41（SpeechTokenizer 4.63、WavTokenizer 4.95、Mimi 4.82、TASTE 8.38） - UTMOS 4.23（最高）；SECS 0.588；单元率仅 2.97Hz，延迟 270ms - SLM 总体一致率 70.6；
- **代码**：暂无 | **Demo**：https://ishlove77.github.io/StreamAlign/

---
## [UniStream: Multi-Expert Residual Vector Quantization for 48 kHz Causal Streaming Audio Coding](https://arxiv.org/abs/2609.09866)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-09
- **一句话贡献**：本文提出 UniStream，面向语音、音乐与环境声音的全因果 48kHz 流式神经音频编解码器。核心是 ME-RVQ（多专家残差矢量量化）：将每层单一共享码本替换为 4 个专家码本，由确定性 Top-K 路由器仅基于已解码量化状态路由，无需传输专家 ID，仅增加 5.5M 参数即扩展量化容量。配合训练期专属的 OT-CFM 流匹配正则（推理期完全移除），支持 12 kbps（Top-1）与 22
- **关键技术点**：现有 RVQ 类编解码器每层共享单一码本，难以用同一表示空间建模语音、音乐、环境声音的异构声学结构；现有 MoE 方案要么把专家放在量化瓶颈之外，要么需在码流中额外传输路由信息增加开销、阻碍流式部署；FlowMAC/FlowDec 等流式解码器需迭代推理，难以实时。
- **主要指标**：- PESQ/UTMOS/STOI（12k）：2.81 / 3.34 / 0.826；22.5k Top-2 为 3.41 / 3.87 / 0.864 - 语音 Mel-D：T1 8.21（vs EnCodec 13.07）；环境 Mel-D 10.16（vs 13.18） - ViSQOL（T2
- **代码**：暂无 | **Demo**：暂无

---
## [KVAE: Family of Tokenizers for Multimodal Generative Models](https://arxiv.org/abs/2608.05798)

- **方向**：多模态tokenizer | **子方向**：Codec | **评分**：7/10 | **日期**：2026-08-06
- **一句话贡献**：LDM的生成质量高度依赖tokenizer的latent空间特性，但重建指标无法可靠预测下游生成性能。KVAE系列提出面向音频、图像和视频的统一tokenizer方案：KVAE-Audio是48kHz全频带连续音频tokenizer（50Hz latent, 64通道）；KVAE-3D提供4×16×16和4×8×8两种因果视频tokenizer；KVAE-2D为8×压缩的32通道图像tokeniz
- **关键技术点**：视觉tokenizer的latent空间特性（diffusability）直接影响扩散模型的训练动态和生成质量，但重建指标（PSNR等）与下游生成性能之间存在reconstruction-generation dilemma。现有开源tokenizer如Wan-2.2（48通道）×16×16）、HunyuanVideo-1.5（32通道×16×16）在压缩率和通道数选择上各有局限。
- **主要指标**：- KVAE-4×8×8 (16ch): PSNR 36.0, SSIM 0.92, LPIPS 0.047 (对比HunyuanVideo-1.0 34.3/0.90/0.047, Wan-2.1 34.3/0.89/0.044) - KVAE-4×16×16 (64ch): PSNR 35.2,
- **代码**：https://github.com/kandinskylab/kvae | **Demo**：暂无

---
## [Language-Statistical Analysis of Neural Audio Codec Tokens Across Architectures, Corpora, and Noise Conditions](https://arxiv.org/abs/2608.31037)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：神经音频编解码器（NAC）将语音转为离散token序列，此前研究声称其服从类语言统计定律。本文对13个NAC（覆盖多码本残差量化RVQ、单码本VQ与非VQ三类架构）在三个语料库、干净/白噪声/真实DEMAND噪声三种条件下系统估计Zipf与Heaps参数、unigram熵、码本占用率及JSD。结果显示：语料身份对各指标解释力极低，声学条件与量化器元类别按指标差异主导，unigram熵与元类别关联最
- **关键技术点**：
- **主要指标**：- unigram熵：与量化器元类别关联最强的指标 - 码本占用率：单码本VQ噪声下出现占用与分布形状迁移 - clean-to-noise JSD：与mel倒谱失真相关，DEMAND噪声下关联最清晰
- **代码**：暂无 | **Demo**：暂无

---
## [When Does Predictor-Based RL Align with Human Perception? A Study of Subjective Rewards in Codec-Based Speech Language Models](https://arxiv.org/abs/2608.31035)

- **方向**：语音大模型 | **子方向**：Codec | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：本文系统研究了基于预测器的强化学习（RL）奖励在编解码器语音语言模型中对齐人类感知的条件。使用 GRPO 算法，以动漫风格、自然度、喜好度和唤醒度四个主观预测器作为奖励，并引入 CER 区域约束防止转录漂移。实验发现：各奖励主要优化自身指标，不可互换；Best-of-8 重排在感知上与 GRPO 相当，表明 GRPO 本质是将奖励选择行为摊销到策略中，而非统一优于重排。
- **关键技术点**：
- **主要指标**：- 单奖励实验：各奖励主要提升自身指标，主观预测器不可互换 - 奖励差距分析：符号化奖励差距显著预测听者选择 - Best-of-8 重排结果：在感知上不劣于 GRPO
- **代码**：暂无 | **Demo**：暂无

---
