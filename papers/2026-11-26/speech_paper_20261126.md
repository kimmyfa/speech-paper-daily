# 2026-11-26 语音论文速递

**共收录**: 11 篇 | **语音大模型**: 10 篇 | **语音前端**: 1 篇

> 目标日期 2026-11-26（北京时间）arXiv 语音相关论文共命中 11 篇（已剔除纯音乐节拍跟踪/音乐相似度/音乐推荐等 3 篇与全部替换投稿）。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] TigerTTS: Draft-Guided Multi-Frame Parallel Speech-Token Language Model for Fast and Robust Text-to-Speech

**arXiv ID**：arXiv:2611.34241 | **方向**：语音大模型

**作者**：Dewei Kong

**机构**：Wiz Holdings Pte. Ltd.

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.34241 | **PDF**：https://arxiv.org/pdf/2611.34241.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对自回归语音token语言模型TTS延迟随序列增长、缺显式对齐致丢字重复、离散codebook限制保真度三大瓶颈，提出TigerTTS：轻量NAR模型显式对齐全句draft，0.15B紧凑AR LLM逐帧精修，每步并行预测3帧×4组共12 token。RTX 4090上CUDA-Graph解码RTF 0.05（约20倍实时），比VoxCPM2快5倍、CosyVoice 2快16倍；SEED上CER/WER最低1.09/1.67，LibriSpeech test-clean上WER/NMOS/相似度2.22/4.36/0.820。

### 🔧 技术方案

**问题背景：** NAR声学模型快但L1/L2回归只恢复条件均值致过平滑；token LM建模好一对多映射却逐token慢，长句、罕见词、数字串因无对齐而丢词、重复、提前停或跑过末尾。需同时拿到速度与对齐鲁棒性。

**模型架构：** 四模块共354.6M：文本经情绪/韵律tagger与G2P；Stage A draft生成器28.8M（4层双向Transformer+Conformer卷积分支+膨胀1/2/4/4时长预测）输出G×K token与mel draft；Stage B LLM 145.7M（6层，H=1280、10头×128、SwiGLU、r_kv=640）以10帧prefix+phoneme+R=3帧步骤输入；FSQ无码本tokenizer（HuBERT→4并行组×512类，20ms约1800bps）；Stage C mel decoder 139.8M、Stage D Vocos 40.3M+192维ECAPA。

**核心创新：** (1) 帧对齐draft引导：draft与LLM目标逐帧同坐标、仅输入注入一次，论文证明训推一致无exposure bias；draft固定对齐与长度作为内容先验，从源头消除丢词、循环与runaway。(2) 多帧并行无损界：R=3×G=4每步12 token、序列缩短3倍；并行独立假设的建模误差恰等于条件全相关T_C∈[0,ΣH(y_i|C)]，draft把各条件熵压向0使并行近无损，且无speculative decoding的accept/reject分支。(3) 部署导向骨干：位置信息只留输入embedding使MLA权重吸收精确、KV cache压4×；draft/speaker线性项预算后整步捕获进单一CUDA Graph，Gumbel-max等效multinomial采样graph-safe。

**训练策略：** 先CTC+单调attention对齐器标时长；decoder学重建后同一量化器tokenize全数据；draft以log域MSE时长+L1 mel+token交叉熵训练（token权重4k→100k步线性升）；LLM对缓存draft teacher forcing并短finetune适配Fast mode。AdamW（β=0.9/0.95、wd 0.1、clipping 1.0）、lr 2×10⁻⁴、warmup 2000、cosine至10%、batch 16；推理T=1.0、top-k 5。

### 📊 实验结果
**数据集**：SEED test-zh/en/hard、LibriSpeech test-clean；RTF同卡RTX 4090单流自测

**主要指标**：
- SEED：test-zh CER 1.09（CosyVoice2 1.45）、test-en WER 1.67（2.57）
- LibriSpeech test-clean：WER 2.22、N-MOS 4.36、SIM 0.820（CosyVoice2为2.47/3.96/0.745）
- RTF 0.05：VoxCPM2的1/5、CosyVoice2的1/16
- FSQ码本利用率100%，token可懂度较CosyVoice2 FSQ低36-43% ASR错误率
- 关键对比：单一0.15B backbone即优于2B VoxCPM2与0.5B CosyVoice2

**是否开源**：文中称数值随代码发布但未给链接，暂无

### ⭐ 评分：8/10
评分理由：把draft引导、多帧并行、MLA吸收与CUDA Graph做成有理论支撑（帧对齐注入、条件全相关无损界）的整体部署系统，比拼贴式加速TTS更有依据；单卡RTF 0.05且质量全面优于CosyVoice2，工程价值突出。扣分在单作者、训练数据规模未披露、消融偏简、未附代码/Demo。

## [2] InstructTTS-OPD: On-Policy Distillation for Multi-Objective Instruction-Following TTS

**arXiv ID**：arXiv:2611.33937 | **方向**：语音大模型

**作者**：Haitao Li, Tian Tan, Yuguang Yang, Guanrou Yang, Wenhao Guan, Chenglin Li, Shan Yang, Xie Chen

**机构**：浙江大学、上海交通大学、厦门大学、腾讯混元

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.33937 | **PDF**：https://arxiv.org/pdf/2611.33937.pdf | **代码**：暂无 | **Demo**：https://cucl-2.github.io/InstructTTS-OPD

### 📌 简介
指令TTS需同时满足指令遵循（IF）、发音可懂（CER）、自然度（MOS），单一标量奖励GRPO联合优化时目标竞争产生跷跷板。本文将图像生成的在线蒸馏OPD迁入语音：各轴先训三个单目标GRPO teacher，再在学生自身SDE rollout上按速度场匹配融合；奖励逐轴选型（Qwen-Omni蒸馏代理替代Gemini judge r=0.95、WER去方言数据、DNSMOS替代有语言偏差的UTMOS），并提出conflict-aware逐帧投影。zh_DSD上IF 77.0→81.1、CER 2.34→2.25、DNSMOS 3.25→3.28三轴同升。

### 🔧 技术方案

**问题背景：** 标量化合并三目标丢弃方向信息，两轴分歧时贡献抵消、更新漂向最易改进目标；重加权只移动平衡点不消除张力，缺在连续速度场上表达折衷的融合机制。

**模型架构：** 基于DiTAR（约0.7B）：Qwen 0.5B自回归LM每步输出条件向量c，193M local flow-matching DiT解码器把噪声转为当前帧audio latent，48M aggregation encoder压回单向量闭合循环，frozen声码器出波形。RL与蒸馏在流匹配轨迹上做：10步ODE取连续3步窗口化为SDE产生on-policy rollout；student与teacher共享高斯转移核，单步KL闭式≈两均值平方距离，蒸馏信号可微零方差。

**核心创新：** (1) 多目标on-policy速度域融合：三teacher不经标量合并、直接在速度场融合（stop-gradient）；按数据域把rollout路由到IF或WER teacher，MOS teacher作guardrail施加于全部rollout（λ=0.3），使IF与可懂落在不同样本上同步提升。(2) 逐轴奖励实证：IF用蒸馏Qwen2.5-Omni-7B代Gemini（Pearson r=0.95）；WER数据必须去方言否则模型改说普通话骗ASR致IF跌至10%；质量用DNSMOS（偏差≤2.8%）替代UTMOS（英文偏高0.72分逼出洋腔）。(3) 冲突感知速度融合：约15步后质量与主方向中位余弦转负，故内积为负时从质量方向dU投影掉与主目标dP相反分量，使质量仅做正交修饰。

**训练策略：** 自同一监督DiTAR base出发，30000条指令+30000条可懂utterance 1:1；GRPO每prompt G=32、KL β=0.01；OPD 16 rollouts、lr 2×10⁻⁶、Adam(0.9,0.95)、4节点×8 GPU共350步；IF奖励三票多数判，WER奖励r=1−min(CER,1)。

### 📊 实验结果
**数据集**：InstructTTSEval zh_DSD（1000条主评测）+六个子集全量；held-out Qwen3-ASR CER与UTMOS

**主要指标**：
- IF（Gemini判）：81.1，较标量GRPO 77.0提升4.1pp，逼近IF teacher上限82.1
- CER 2.25（标量GRPO 2.34）、DNSMOS 3.28（2.81→显著超base）、归一化Avg 0.82 vs 0.75
- 盲听偏好：after-RL较base净胜6.7pp；去conflict-aware后Avg跌至0.80
- 关键对比：三目标同时优于标量GRPO，无跷跷板

**是否开源**：Demo已上线，训练代码暂无

### ⭐ 评分：7/10
评分理由：把Flow-OPD速度域在线蒸馏完整迁移到Instruct-TTS三目标后训练，conflict-aware逐帧投影直击标量GRPO跷跷板痛点，机制新颖、奖励选型分析细致、证据链（主表+held-out+盲听+sweep+routing消融）较完整。局限是backbone为私有DiTAR、仅350步1万样本规模、方言与英文验证偏弱、未开源代码，属强增量。

## [3] UMAI: UM Aware Inference with a Frozen Qwen3-ASR

**arXiv ID**：arXiv:2611.34256 | **方向**：语音大模型

**作者**：Gyeongmin Kim

**机构**：汉阳大学（韩国首尔）

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.34256 | **PDF**：https://arxiv.org/pdf/2611.34256.pdf | **代码**：https://github.com/kdrkdrkdr/umai | **Demo**：暂无

### 📌 简介
逐字转写需保留语气词，但Qwen3-ASR-1.7B在AMI eval上语气词F1仅12.2，微调恢复又会改变其余输出。本文提出UMAI：仅用冻结模型一次贪心解码记录的内部状态（28层解码器输出、注意力对齐、帧级后验），经两级带OAS收缩的五类LDA与保序回归校准，在词间隙插入[uh]/[um]，全程无梯度训练。AMI eval语气词F1升至82.6，Nyra从37.2升至96.5，额外耗时仅14%，识别词零改动。

### 🔧 技术方案

**问题背景：** 临床言语评估、不流利分析与TTS数据管线依赖逐字转写，主流识别器大量丢弃语气词；微调/提示/偏置解码会连带改变措辞、标点与数字格式，且已有不流利检测器基于文本或外部特征，无法定位音频中的语气词区间。

**模型架构：** 冻结Qwen3-ASR-1.7B（24层音频编码器+28层解码器）单次贪心解码；在每个输出词起始步g与g+1记录全部28层状态，词间/句尾"gap"为决策单元；EM混合448个注意力头为单一对齐头（0.91权重集中于L21-H15），以累积注意力构造gap音频窗；五类（静音/词/语气词/截断/重复）帧后验由25个特征源各一级LDA再接二级LDA；末层状态过输出层得uh/um拼写概率差定形式；保序回归给插入概率P>τ。

**核心创新：** (1) 梯度无关闭式读出：OAS收缩协方差LDA闭式解，两级线性可折叠为单一矩阵，整个读出不改一字、仅5.7MB文件与识别器解耦分发。(2) 识别器自身注意力充当时间定位器：不依赖外部强制对齐，用EM选出的对齐头注意力构造gap窗并池化后验。(3) 五类gap标注给异常解码状态提供竞争解释，LLM审读校正4129个标签（复现一致性κ=0.974）。

**训练策略：** 全部统计量在AMI训练会议66900条语句上闭式估计；取全部154138个非O gap加抽样的O gap按会议分五折stacking；τ=0.75在Nyra选定；无学习率/轮数/优化器。

### 📊 实验结果
**数据集**：AMI eval（16场会议、7490句、3067参考语气词，说话人隔离）；Nyra Verbatim（4957句、3072语气词）

**主要指标**：
- AMI eval语气词F1：12.2→82.6（τ=0.75），召回6.6%→74.0%、精确率保持93.3%
- Nyra F1：37.2→96.5（阈值在此选定，作者自注偏乐观）
- Exact F1（含uh/um形式正确）：AMI 80.0、Nyra 94.9
- 开销：RTF 0.139→0.158（+14%）、显存+0.11GiB；关键对比：零训练较冻结原生输出提升70.4/59.3点

**是否开源**：代码与5.7MB读出文件已开源 @ https://github.com/kdrkdrkdr/umai

### ⭐ 评分：7/10
评分理由：把探测探针改造成不改一字识别词的语气词插入工具，全程闭式解、成本可控、消融与错误分析诚实（明确Nyra乐观偏差与未归因差距）。局限是仅英语uh/um、单一识别器验证，方法组件（LDA+等渗回归）本身传统。扎实的小而美工作。

## [4] A Head-Level Investigative Study of Self-Supervised Backbones for Synthetic Speech Detection

**arXiv ID**：arXiv:2611.34426 | **方向**：语音大模型

**作者**：Mohamed Mallat, Michele Panariello, Massimiliano Todisco, Anthony Larcher, Nicholas Evans

**机构**：EURECOM（法国）、勒芒大学LIUM（法国）

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.34426 | **PDF**：https://arxiv.org/pdf/2611.34426.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
SSL骨干深伪检测研究长期止步于层级探针，层内12个注意力头谁在计算伪声判决无人知。本文首次在ASVspoof 5上对冻结WavLM-base与WavLM/Wav2Vec2做头级因果分析：逐头消融发现判决集中在少数检测头、另有头主动干扰，直接置零干扰头无需重训即相对降EER 13%（5.66→4.92）与22%（6.85→5.31）；并找到免探针注意力熵签名——伪声注意力更聚焦，144维熵值逻辑回归即达5.95% EER逼近全表征探针5.4%。

### 🔧 技术方案

**问题背景：** 层级探针确认证据集中在SSL中间层，但层一直被视为不可分割原子；模型对未见攻击泛化失效被怀疑与部分头有关，此前无人在反欺骗场景做头级考察。

**模型架构：** 冻结WavLM/Wav2Vec2-base（12层×12头，d_h=64）。先逐层训均值池化线性探针选最优层（L7/L5）；头消融＝把W_O对应列块置零的因果探针，按EER变化分检测头/干扰头/冗余头并做top-k充分性测试；统计全部144头每句注意力平均熵（4s音频T=199帧）构成免探针签名；再对每头64维修置输出训二/八分类探针。

**核心创新：** (1) 分析粒度从层降到头并定义为因果探针：以移除后误差变化定角色，给出检测/干扰/冗余划分，为泛化失效提供机理解释。(2) "少即是多"免费午餐：干扰头零成本直接删除即得13%/22%相对EER下降，增益集中于最难A11-A13攻击，eval未见攻击上角色更显著。(3) 独立于探针的注意力熵签名：伪声熵差最大0.15/0.20比特、每层熵差峰值恰在最优探针层且与探针EER强负相关（ρ=-0.87/-0.76），144维熵即可近似全表征性能，可用于免训练选层。

**训练策略：** 探针仅训A01-A08、分析用dev未见攻击A09-A16；说话人均衡2000真+5200假4s样本；头排序在随机子样本确定后于两个不相交子样本报EER；Wilcoxon+144头Bonferroni校正（p<3.5×10⁻⁴，显著138/132头）。

### 📊 实验结果
**数据集**：ASVspoof 5（16kHz，TTS/VC/对抗攻击）

**主要指标**：
- 剔除干扰头（无重训）：WavLM EER 5.66%→4.92%、Wav2Vec2 6.85%→5.31%
- 熵签名：WavLM train→dev 5.95%（LOAO均值2.98）、Wav2Vec2 9.69%
- 单头独立检测最优仅11.3%（全层5.4%）；攻击身份全头可解码76-82%（随机12.5%）——"头之不同在做不在知"
- 关键对比：熵签名落后最强全表征探针仅0.55pp

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：填补SSL反欺骗头级因果分析空白，"删干扰头免费增益"与"免探针熵签名"兼具机理洞见与即用工价值，防选择泄漏协议+显著性校正+eval复验体现严谨。局限是单一英文语料、base级骨干、观测性分析而非机理建模、绝对增益适中。

## [5] Psychophysics of Duration Perception in Multimodal Large Language Models

**arXiv ID**：arXiv:2611.33176 | **方向**：语音大模型

**作者**：Auss Abbood, Zihao Fu, Nigel Collier

**机构**：University of Cambridge Language Technology Lab、CUHK

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.33176 | **PDF**：https://arxiv.org/pdf/2611.33176.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
多模态模型音频侧时长感知极限缺乏量化。本文把Warren(1991)经典旋律时伸缩心理物理实验移植到21个MLLM：将英语耳熟能详儿歌渲染为正弦波旋律，40-3600ms/note共14档探测旋律"丧失整体性"的识别阈值，对照人类中位识别窗（160-1280ms）。零样本全部模型筛查失败；带标注上下文范例后仅7个通过且多在人类窗口内达峰，但峰值随范例语速右移、旋律标题诱发偏差（中性编号后峰值从约50%升至60%+），仅Gemini 3.1 Pro在3600ms/note仍约80%。

### 🔧 技术方案

**问题背景：** LLM时间感知研究集中在文本模态；音频基准只测远高于人类阈值的粗粒度物理量，音乐基准做固定音集类别判断，均未以变化音符时值测量"时长依赖的时间分组崩溃点"，缺少与人类基线可比的心理物理阈值。

**模型架构：** 评测探针而非新模型。旋律刺激正弦波渲染（44.1kHz、5ms斜坡、20ms音符间隔、onset-to-onset计时），流程仿人类实验分训练（320ms/note）—筛查（第3-4音进入循环防首音识别）—14档时值缩放（每旋律28 trial）；输入分text+audio交错与TTS合成两格式；识别包络用Bernoulli链接+三次B样条+模型/旋律随机截距GLMM拟合；被测21模型含Gemini 3.1 Pro、GPT Audio、Qwen3.5/3 Omni、Voxtral、Audio Flamingo等。

**核心创新：** (1) 首次把"时长感知极限"操作化为格式塔时间分组崩溃点，直接与人类四分位窗（113/2560ms）对照，区别于符号化时长估计。(2) 上下文语速消融：范例时值113-640ms变化识别峰随之移动、113ms范例下几乎全错——表观"感知边界"是提示属性而非内在知觉常数。(3) 标题偏差与记谱消融：中性编码消除Twinkle假阳性过预测（0.36-0.60→正常）、性能提升；附科学音高记谱使平均峰值略高于50%升至约60%，但长时值多数模型仍衰退。

**训练策略：** 无训练，纯黑盒API评测；温度默认0；阈12/16机会校正计分；GLMM 4链NUTS、1000+1000采样、PSIS-LOO选样条自由度。

### 📊 实验结果
**数据集**：Warren 8首+扩展11首共21首儿歌旋律；YouTube四个24小时窗口做曝光代理分析

**主要指标**：
- 零样本筛查最高仅38%（Qwen3.5 Omni Plus），21模型全失败；上下文筛查7模型通过（text+audio）vs 4个（audio-only）
- 时值组GLMM峰值约50%、落在人类中位窗内；<160ms全员崩解（疑因160ms音频分词块）
- Gemini 3.1 Pro：3600ms/note仍约80%，唯一"类音乐家"保持型
- 中性编码后峰值60%+；扩展旋律集复现形态

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：把经典心理物理范式严谨移植到MLLM评测是真实方法论增量，"识别窗口是提示的属性"结论对时间感知评估有警示价值，GLMM+PSIS-LOO统计处理超多数评测文章。局限是放弃人类交互范式、正弦波刺激+黑盒API无法区分转录策略与真实知觉，未提出改进手段，偏诊断性。

## [6] Line-Level Singer Diarization in Multi-Member Pop Songs: A Benchmark, Lead-Vocal Isolation, and Song-Level Decoding

**arXiv ID**：arXiv:2611.33247 | **方向**：语音大模型

**作者**：Allen Ng

**机构**：nagiflow LLC（东京）

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.33247 | **PDF**：https://arxiv.org/pdf/2611.33247.pdf | **代码**：https://huggingface.co/datasets/nagiflow/colorcoded-sd | **Demo**：https://huggingface.co/datasets/nagiflow/colorcoded-sd

### 📌 简介
粉丝为多成员流行团逐行标注主唱/伴唱，但语音diarization无法迁移：商用服务在5人团平均只认出1.35个说话人、43首中33首塌成单簇。本文定义逐行歌手分离任务，发布ColorCoded-SD基准（K-pop 43首、1740行、3-8人/首、人类一致性89.1%），并提出"主唱隔离+歌唱自适应嵌入+免训练歌级解码"管线，B3-F1较标准管线在ColorCoded-SD提升+0.058（0.641→0.699）、未见歌手IdolSongsJp提升+0.066（0.800→0.867）。

### 🔧 技术方案

**问题背景：** 语音diarization假设声纹差异大；偶像团音色刻意趋同、共享制作与音域、乐句间多和声，任务实质是"线已对齐、声纹难分"的分组问题，需重设输入、嵌入与解码三层。

**模型架构：** HT-Demucs人声分离+Mel-RoFormer karaoke主唱轨为前端；每行裁0.1s切3s窗、静音门限为歌曲均幅1/4；ECAPA2或SpeechBrain ResNet编码192维；曲内减Song均值并L2归一化去共享制作分量；cosine平均链接AHC聚已知K簇，短/静音行取最近邻。

**核心创新：** (1) 输入端主唱隔离为最大单一收益因子（同线+0.04~0.06）：karaoke判和声的行回退Demucs轨（0.699 vs 0.661），证明"去他人"价值高于分离更全。(2) 歌唱自适应嵌入："同曲异人做难负例+冻结语音模型锚项"微调，15.4M ResNet-ft在lead输入追平27.1M ECAPA2（0.665 vs 0.661）且CPU成本仅1/8；干净音轨下两嵌入差异消失。(3) 两个免训练歌级解码：利用"同歌手连续成行占57.2%"先验的sticky Viterbi，与基于discography跨曲匈牙利链接同一成员原型的交替重解码，合用再+0.028。

**训练策略：** 训练集2277首/1765歌手/约125h；监督对比学习温度0.1、batch含3曲3s窗+同歌手跨曲窗；BatchNorm冻结，随机增益与±6dB EQ增强；AdamW，ResNet-ft lr 5e-4/1000步只训3-4层，ECAPA2-ft 500步只训1D部分；IdolSongsJp全程零调参。

### 📊 实验结果
**数据集**：ColorCoded-SD（43首K-pop、1740行、30歌手）；IdolSongsJp（14首309行、18未见歌手仅评估）

**主要指标**：
- ColorCoded-SD：B3-F1 0.699、Acc 72.4%（标准管线0.641/66.3%，p=0.012）
- IdolSongsJp未见歌手：0.867 vs 0.800（p=0.040），最优组合0.875
- ElevenLabs Scribe v2商用仅0.386 B3-F1（平均1.35 speaker），错误集中在短行
- 嵌入EER ResNet 30.7→26.5%；距人类一致性89.1%已闭合约1/4差距

**是否开源**：基准/工具已发布CC BY-NC 4.0（2026-12-24起，不含音频歌词）

### ⭐ 评分：7/10
评分理由：首次系统化定义逐行歌手diarization并给出带人一致性度量的真实基准，配对bootstrap做输入/编码器/解码三因素误差分解，"主唱隔离主导、嵌入在干净输入下不重要、解码器收益需组合"结论清晰，负面结果坦诚。不足是仅43首单域K-pop、需已知说话人数、方法偏现有组件组合。

## [7] An offset-drift Kalman filter for continuous emotion recognition and annotation from sparse human reviews

**arXiv ID**：arXiv:2611.34857 | **方向**：语音大模型

**作者**：Jie Dong, Mahdi Zareei

**机构**：Tecnológico de Monterrey（墨西哥）

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.34857 | **PDF**：https://arxiv.org/pdf/2611.34857.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
连续情感识别（CER）预测常成片偏离人工评分，而连续标注需评审实时打分成本高昂。本文提出偏移-漂移卡尔曼滤波器ODKF：把预测误差建模为"每段常数偏移+慢速AR(1)漂移"，以被评审窗口的误差为观测，在线估计状态并直接校正全部未评审窗口，预测器不动。MSP-Conversation上48组配对比较全胜四种简单校正；评审20%窗口后唤醒度逐段CCC从0.47升至0.58、效价从0.33升至0.52。

### 🔧 技术方案

**问题背景：** 预测误差在时间上高度相关（可长时间停在评分均值一侧），理论上次评审应惠及邻域；现有动力学模型建的是情绪本身而非预测误差，自适应/拒识/主动学习要么不用测试时人工输入、要么只决定交接窗口，均未把稀疏评审用于校正未评审窗口。

**模型架构：** 校正层为2维线性高斯状态空间：x_k=(a_p,b_k)，F=diag(1,φ)、h=(1,1)，每段重置先验diag(τ²,q)。MSP轨迹10Hz、切4s窗；考虑评审3s反应滞后，窗口j仅前1s误差可观测，观测为前1s平均误差加方差ρ噪声；只更新评审点、未评审窗口外推，y̅=f_t+h'x̂_{k|k-1}直接加到冻结预测器。被校正预测器为双约束neural ODE（CD约束速率+值域约束+二ODE建模评审离散度），输入为冻结WavLM-Large全25层均值。

**核心创新：** (1) 首次把人工评审重构为"预测误差贝叶斯跟踪"：偏移项永衰减不、漂移按φ^|i-j|加权历史评审，使每次评审按"误差多持久"分配合适credit——Offset-only/EWMA/CM都不具备该双重机制。(2) 参数可解释免训练：τ²/φ/q在开发集以L-BFGS最大化误差序列联合高斯似然拟合；实测偏移占总误差方差43-49%、漂移时间尺度10.5/20.6s，Offset-only即拿到ODKF增益的78-91%、漂移补其余。(3) 同一状态估计支撑三用途：在线校正、按预测平方误差提示人工优先接管偏移最大的段、及"评审预算均匀间隔优于随机"的排期设计。

**训练策略：** 无梯度：5折开发集交叉拟合、测试集单次拟合；预测器三种子42/123/456；预算5%/10%/20%，随机排期10次抽样均值。

### 📊 实验结果
**数据集**：MSP-Conversation v2.0（68.3h播客、279对话799段、10Hz唤醒/效价、每段6-8名评审），说话人无关484/147/168段

**主要指标**：
- 未评审窗口校正损失：唤醒度ODKF −10.60×10⁻⁴ vs Offset-only −9.33、EWMA −9.12；效价−32.64 vs −25.55；48/48配对比较显著
- CCC（20%均匀评审）：唤醒0.470→0.584（pooled 0.627→0.808）、效价0.327→0.522（0.638→0.857）
- 排期：20%均匀比随机低损失0.87/2.87；5%预算下简单校正反而劣于不校正
- 离线平滑、反应间隙放宽、评审组重采样后均保持一致（量级缩小仍显著）

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由："评审即误差观测"视角新颖、切中CER标注成本痛点，预测器不动即插即用，统计设计罕见严谨（有限总体校正、聚类bootstrap、敏感性分析）。局限是单语料单预测器、未与测试时自适应基线对比、漂移贡献仅一成、无代码。扎实增量。

## [8] Evaluating Cine and Tagged MRI-to-Speech Synthesis with Complementary Metrics and MRI-Free Controls

**arXiv ID**：arXiv:2611.33786 | **方向**：语音大模型

**作者**：Karlo Vrancic, Fangxu Xing, Jiachen Zhuo, Maureen Stone, Jerry L. Prince, Jonghye Woo

**机构**：Mass General Brigham/Harvard医学、University of Maryland、Johns Hopkins

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.33786 | **PDF**：https://arxiv.org/pdf/2611.33786.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
舌运动MRI转语音合成过去用Corr2D绝对值夸耀影像贡献，但从不对照"不用MRI也能得到多少"。本文在同一骨干固定下构造两个仅用训练集录音的MRI-free阴性对照——静态平均谱基线与时间对齐队列模板，44人留一人交叉：从未见过MRI的模板Corr2D达0.745/0.664，静态基线占其87-89%；八次确认族对比中七次所有训练配置显著低于模板，CEPSTRAL/ESTOI全败。核心结论：绝对Corr2D无法证明模型从MRI恢复声学，只能读对模板之差。

### 🔧 技术方案

**问题背景：** 受试只念"a souk""a geese"两句节拍器脚本，队列模板即可命中大部分共有结构；被用的0.665-0.820 Corr2D来自被试内共享框架，混入了表征、语料与静态谱偏置三个非影像成分而无校准。

**模型架构：** 逐帧ViT（2层4头）8×8 patch→128维token、位置编码用像素网格拉普拉斯前8非平凡特征+符号不变MLP；token池化后线性重采样、dilated 1D卷积出64通道log-mel（22.05kHz、FFT1024、hop256）。四个输入条件仅换/堆通道（cine/单双朝向tagged/三通道融合，另有晚融合）。对照：静态基线=训练谱沿时平均 broadcast；队列模板=warp后训练mean per utterance重采样到目标长。

**核心创新：** (1) 双阴性对照可复用方法：静态基线量化表征自带供给，队列模板量化共享语料供给，差值才是影像的边际贡献，任何研究都能从自身训练录音计算。(2) 稳健性消融：时间注意力、可学习patch编码、z-score目标重参数化，12次训练均值全部低于模板——结论不依赖特定骨干配置。(3) 目标渲染敏感性：同一批录音三种渲染下MRI-free模板Corr2D跨0.34-0.75，比已发表影像值区间宽2.5倍——绝对分数跨研究根本不可比。

**训练策略：** 每折重训同种子模型、MSE（+z-score变体）40 epoch；Wilcoxon受试者内配对、Mann-Whitney患者vs健康；8项模板对比确认族Holm校正。

### 📊 实验结果
**数据集**：Siemens 3T同步cine+双朝向tagged MRI+音频（44人：26健康+18舌切除术后，两句朗读）

**主要指标**：
- 模板Corr2D 0.7445(a souk)/0.6638(a geese)全表最优；静态基线0.6631/0.5743（87-89%）
- 训练配置cine 0.7393与模板打平（p=0.36），换硬件重训即显著落后（p=0.021）；a geese四配置0.586-0.626全落后（p<0.001）
- ESTOI：模板0.1466/0.1632高于全部配置（0.1172等）
- 压缩检验：28次预测与模板相关0.94＞与自身目标0.67，模型输出"更像模板不像真录音"

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：贡献在评测方法学，把"高Corr2D=影像还原声学"拆解为表征/共享语料/个体三成分并用严格配对检验立住；MRI-free对照可一键复用于MRI转语音、无声语音合成等同类任务，附四步报告清单实用。局限：单站两句脚本、单骨干、未在已发表方法渲染下复现对照、模型本身弱于既有方法不能排除更强模型越线。对社区是高价值警示论文。

## [9] Modality-Shift Contrastive Decoding for Temporally Grounded Audio-Visual Understanding

**arXiv ID**：arXiv:2611.34162 | **方向**：语音大模型

**作者**：Minyeong Jeong, Yeonju Kim, Yong Man Ro

**机构**：KAIST（Integrated Vision Language Lab）

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.34162 | **PDF**：https://arxiv.org/pdf/2611.34162.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
AV-LLM虽显式建模时间结构，但本文在DAVE上平移音轨做受控探测发现：改变后新对齐事件仅22.7-29.4%被选中，模型仍以34.3-38.0%偏向原对齐事件——对齐没被真正使用。提出免训练解码MSCD：30秒窗内循环半段对调平移已编码音频/视频特征，用（原始−音移−移视+双移）四元组对数差代数消去单模态重排干扰、放大跨模态对齐。OmniVinci/video-SALMONN 2+上DAVE +5.5/+3.0、Daily-Omni +2.2/+2.8个百分点。

### 🔧 技术方案

**问题背景：** AV-LLM用时间分组/交错token/时间嵌入表示时间结构，但"能表示"≠"会用"；现有免训练解码（AVCD/MAD/CAD等）都针对幻觉抑制，无解码期强化音视时间对齐的方法。

**模型架构：** 骨干为时间交错输入[V1,A1,…,VK,AK]（OmniVinci 9B、video-SALMONN 2+ 7B均Qwen2.5系）。MSCD：视频切w=30s不重叠窗，窗内音频按特征向量/视频按时间块做循环半段对调；每解码步4次前向（原始/音移/视移/双移），媒体编码仅算一次；Δz=½(z−z_A−z_V+z_AV)后α加权进原logit。

**核心创新：** (1) 声源-事件移位探测量化AV-LLM时序不敏感（±4/8/16s平移下原对齐事件选择率不降反高），为解码干预提供行为动机。(2) 四条件logit分解：单模态移位差=对齐贡献a+模态内部乱序贡献o，以同样保对齐的双移位估o_A+o_V，代数恰好消去乱序项只留跨模态对齐——区别于单路扰动的传统对比解码。(3) 循环半窗扰动设计（平移量w/2与视频长无关、保半段内次序与全部特征），消融优于位置偏移与随机置换。

**训练策略：** 完全免训练，仅解码干预；窗长30s与强度α（三基准无权重均分选优：OmniVinci 5.0、v-SALMONN 2+ 1.5），移位分别施加于OmniVinci时间嵌入前与v-SALMONN解码输入处。

### 📊 实验结果
**数据集**：DAVE同步（2022题）、Daily-Omni（1197题）、AVUT对齐子集（1120题）

**主要指标**：
- DAVE：44.3→49.8%（+5.5）/42.5→45.5%（+3.0）；Daily-Omni 61.2→63.3/61.6→64.4（+2.2/+2.8）；AVUT +1.2/+0.6
- 唯一在2骨干×3基准均正增益的解码法（AVCD/MAD/CAD多数持平或负）
- ±16s移位"新对齐正确"选择率29.4%→35.6%，首次反超原事件；≥8s错选最高降8.3pp

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：以受控探测暴露AV-LLM时间利用不足的问题新颖，四分支对数差代数消元优雅、消融完整并给出行为级证据链。局限是增益幅度小、每骨干需搜α、解码计算约4倍、仅评选择题首步解码，泛化到开放生成未知。对AV-LLM推理优化参考价值高。

## [10] Investigation of generalization to unseen audio generation models in audio-text semantic-alignment score prediction

**arXiv ID**：arXiv:2611.34626 | **方向**：语音大模型

**作者**：Yuki Okamoto, Noriyuki Tonami, Takao Kawamura, Keisuke Imoto, Ryotaro Nagase, Riki Takizawa, Minoru Kishi, Shinnosuke Takamichi

**机构**：东京大学、NEC、京都大学、立命馆大学、京都产业大学、庆应义塾大学

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.34626 | **PDF**：https://arxiv.org/pdf/2611.34626.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
音频-文本语义对齐分数预测模型只在训练内已见TTA模型音频上评测过，跨生成器泛化无人量化。本文把XACLE Challenge 2026数据集的8个TTA模型分为A/B互斥两组做跨组训练测试，并将DANN梯度反转层（GRL）接入BYOL-A+RoBERTa基线。实验证明：冻结预训练编码器可约0.94准确率识别来源生成模型（指纹确实存在），基线未见组SRCC从0.339崩至0.144；GRL(All)仅小幅回到0.161/0.241，且抑制效果不稳定——坦率呈报近似负结果。

### 🔧 技术方案

**问题背景：** CLAPScore、RELATE式监督打分与XACLE官方基线全部只在"训练集出现过的生成模型"合成音频上验证；TTA模型加速迭代，评测器若捷径学习某生成器声学指纹，换新模型即刻失真，此风险此前无人量化。

**模型架构：** 基线为XACLE 2026官方：BYOL-A音频编码器V∈R^(F×T)+RoBERTa文本编码o沿时复制拼接Z，单层BiLSTM+两层线性输出分数ŷ。对抗分支为2层MLP生成模型分类器，GRL（前向恒等、反向梯度反号按α缩放）接于音频编码器或Score Predictor全链路两处位置。

**核心创新：** (1) 首次系统量化对齐打分模型跨未TTA生成器的泛化：8模型分两组，跨组训练/测试，SRCC/KTAU/LCC/MSE四指标。(2) 生成模型指纹探针：BYOL-A/CLAP冻结表征+MLP训8类来源识别器达0.928/0.942高精度，把"为什么泛化差"落实为可测泄漏。(3) 把语音MOS已验证的GRL对抗训练平移到音频-文本对齐任务并对比注入位置，同时诚实报告仅SetB方向识别率降至0.835、部分设置反升。

**训练策略：** 打分模型Adam lr 2×10⁻⁵、batch 12、20轮按验证SRCC选模，L=L_mse+0.5L_con+0.1L_adv（前5轮1.0、α=1.0）；每组2000/1000/1000对（大模型下采样），探针各自训4类。

### 📊 实验结果
**数据集**：XACLE Challenge 2026（8个TTA模型，A组AudioLDM/Tango2/AudioGen/Stable Audio；B组AudioLDM2/Tango/Make-an-Audio2/TangoFlux，11分制主观对齐标注）

**主要指标**：
- 未见组SRCC：A→B基线0.144，Ours 0.161（+0.017）；B→A基线0.210→0.241（+0.031）
- 组内SRCC稳定0.39-0.41；GRL对识别精度抑制不稳定（SetB降至0.835但SetA升至0.951）
- 关键结论：泛化退化主要源于生成器指纹未被GRL抑制，改善极小——负结果为主

**是否开源**：暂无

### ⭐ 评分：5/10
评分理由：选题切中TTA评测可信性，是首个量化该泛化的工作，指纹探针+坦率负结果有社区价值。但方法仅平移已知DANN/GRL，跨组提升+0.02~0.03难言实用，单配置无显著性检验、8模型仅分两组，未定位指纹所在频段/模块。增量性强的分析型短文。

---

## 语音前端

## [11] Learning Temporal Stabilization for Double-Talk-Robust Delay Estimation in Acoustic Echo Cancellation

**arXiv ID**：arXiv:2611.33689 | **方向**：语音前端

**作者**：Lu Ma, Yongliang Wang, Zhewen Su

**机构**：京东（JD.com, Inc.）

**发布日期**：2026-11-26 | **论文**：https://arxiv.org/abs/2611.33689 | **PDF**：https://arxiv.org/pdf/2611.33689.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
AEC自适应滤波器须先补偿远端参考与麦克风的体时延才收敛，GCC-PHAT在短分析窗持续双讲下产生与真峰同样尖锐的伪峰，灾难性时延跳变且经典中值滤波/置信门控都难压制。本文保留GCC-PHAT为完全不可训练backbone，仅在时延-滞后相关图上叠加13.2K参数因果2D CNN稳定器，利用"真实时延呈持续脊线、双讲伪峰为瞬时尖峰"时序先验甄别。对比调优经典估计器与WebRTC AEC3匹配滤波器，MAE与粗差率降3-5倍（跳变场景3.9ms vs 20.5ms），下游漏回率与ERLE恢复显著改善。

### 🔧 技术方案

**问题背景：** 作者压力测试表明学习型TDE在干扰/低SNR/强混响/喇叭非线性/噪声参考下不如GCC-PHAT，全学习前端MAE高达100-200ms——替换前端路线失败；真正脆弱点仅在算法时延受限下的短窗持续双讲，中值滤波只消一半损伤（21.5→11.7ms），峰锐度门控几乎无效，遗留问题本质是峰的时序可信度判别。

**模型架构：** 流式GCC-PHAT（100ms窗/1024样点hop/因果左填充）输出(B,T,τ+1)相关图→滞后轴×4平均池化（0.25ms/bin，τ_max=80ms）→逐帧峰值归一→DelayCombiner2D（因果time×lag CNN，1→16→16→16→1通道、滞后核11/9/7/5、时间核3、FrameGroupNorm保证严格因果）→滞后softmax+抛物线亚bin插值。13.2K参数全在组合器，backbone零参数。

**核心创新：** (1) 固定backbone只学稳定化：受可学习前端会破坏宽带相位相干的教训，把参数严格限制在相关图之后、仅补经典方法无法表达的时序可靠性判别，与"替换GCC"路线构成方法论区别。(2) 二维时序归纳偏置：网络学持续脊线与瞬时尖峰之分；训练注入时延跳变使持续新脊线触发快速重锁定、瞬时伪峰被抑制，消除恢复-稳定权衡；消融2D 4.7ms vs 1D逐帧14.0ms、可靠性头可省。(3) 免重训粗到细扩展：慢速长窗全局搜索（至1s、带滞回流更新）估体时延并预移参考，同一0-80ms残差CNN微调，稳定覆盖100-400ms设备/网络时延。

**训练策略：** 全合成回声路径+真实语音训练，时延0-80ms，注入持续双讲/跳变/音乐与歌唱干扰；交叉熵+smooth-L1损失、权重EMA、ReduceLROnPlateau。

### 📊 实验结果
**数据集**：合成held-out split（恒定/跳变两协议）+AEC-Challenge真实路径（Route 1A n=64精确GT、1B n=64 SER 0dB伪GT）

**主要指标**：
- 恒延+持续双讲：MAE 2.0ms（经典GCC-HT 10.1/AEC3-mf 9.8ms）、粗差2.7%（vs 17.3%/15.3%）
- 频繁跳变：3.9ms vs AEC3-mf 20.5ms（约5倍）；真实1A/1B：4.1/5.3ms vs 12.2/14.7ms；100-400ms粗到细3.1-4.6ms
- 下游忠实AEC3式测试：时变ERLE 3.43dB（oracle 4.27、GCC-HT 2.20/AEC3-mf 1.94）、漏回率52.9%（vs 64.5%/70.1%）、7.5窗恢复最优

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：定位精准、工程务实——先证经典backbone近最优，再把13.2K参数严格限制在唯一失效模式，消融与机制验证闭环，含真实AEC-Challenge路径与下游ERLE增益3-5倍可信。扣分：下游为自研合成测试床非真实WebRTC产物，受益场景（短窗时变双讲）较窄，100-400ms扩展依赖体时延近似恒定。对车载/免提AEC有直接落地参考价值。

---

*Generated on 2026-11-27*
