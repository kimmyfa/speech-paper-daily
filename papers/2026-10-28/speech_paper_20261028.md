# 2026-10-28 语音论文速递

**共收录**: 15 篇 | **语音大模型**: 7 篇 | **语音前端**: 8 篇

> 目标日期 2026-10-28（北京时间）arXiv 语音相关论文共命中 15 篇。
> 以下是按评分排序的结果。

---

## [1] TAC2: Timestamped Audio Captioning as composable functions

**arXiv ID**：2610.36568 | **方向**：语音大模型

**作者**：Swapnil Bhosale, Prem Seetharaman, Ke Chen, Haonan Chen, Justin Salamon, Zeyu Jin

**机构**：University of Surrey（英国）、Adobe Research（美国）

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36568 | **PDF**：https://arxiv.org/pdf/2610.36568.pdf | **代码**：暂无 | **Demo**：https://swapb94.github.io/tac2-audio-describer/

### 📌 简介
针对大型音频语言模型自由文本输出缺乏时间grounding与可查询性的问题，提出TAC2：以时间注册IoU匹配融合captioner、说话人分离、声音事件检测三个弱监督teacher，在200万条in-the-wild音频上构建带说话人归属的时间戳声学时间线，用Instruction-Input-Output（IIO）可组合函数格式训练，再由小样本LoRA专家引出重音、情绪等副语言属性并蒸馏为TAC2-S。接冻结文本LLM后MMSU达81.9、感知77.8超Gemini-3.7 Flash（68.7）；作为文生音配对监督，事件定位误差1.54s，实现事件时序、说话人属性、词级强调的零样本控制。

### 🔧 技术方案

**问题背景：** 声学表征需锚定物理时间且可查询；LALM自由描述易时间幻觉，前作TAC一次性事件级描述难表达说话人轮次/重叠事件，无法融入转写等先验。

**模型架构：** 两阶段，骨干为冻结Qwen3-Omni-30B captioner+rank-512仅注意力LoRA。阶段1把时间轴上SED/diarization/captioner三teacher输出逐类一对一IoU对齐融合，形成事件/属性/边界/说话人/转写多粒度schema并拆为IIO任务；阶段2按属性LoRA专家热加载成TAC2-E级联重标注，Qwen3-Next-80B改写后再附加LoRA蒸馏出TAC2-S。

**核心创新：** (1) IIO可组合函数接口：任务即f(音频、指令、可选输入)；comprehensive空输入一次解码全时间线，链式调用以前序输出/外部转写做teacher-forcing条件，扩展只需加任务。(2) 时间注册IoU多视图弱监督：属性设权威teacher、事件类设时间owner，对齐最大化总IoU，音效0.2/语音0门槛配中点回退，程序化构造目标。(3) 潜在能力引出：探测显示副语言属性在骨干内高度可线性解码（AUC 0.89–0.99）而生成可及性差，<1万样本LoRA即把潜表征暴露为标签，并修正情绪、口音塌缩。

**训练策略：** 约200万条≤30s授权clip，IIO完成交叉熵、按说话人数加权采样，AdamW 1万步/lr 1.6e-3/warmup 1千步余弦衰减；任务权重comprehensive 1.0/caption・stress・emotion 0.5/画像・声学0.3；专家金标<1万条：重音A560E、情绪IEMOCAP/RAVDESS/MELD、画像silver+Common Voice、声学CREPE/RMS；TAC2-S同配置续训2000步。

### 📊 实验结果
**数据集**：MMSU/MMAR/MMAU/MSU-Bench/LongAudioSpan；生成集300条六口音/1471事件

**主要指标**：
- MMSU 81.9（感知77.8/推理86.4），感知超TAC +14.0、超Gemini-3.7 Flash +9.1，近TAC2-E 82.9
- MSU-Bench 82.2（T1 79.2/T2 86.6）超Gemini-3.7 Flash +5.8；MMAR 68.0/MMAU 75.6
- 时间定位：PE 1.54s/FLAM 2.14s（无戳2.93/3.16s；PicoAudio2带戳2.47/3.16s）
- TAC2-S-as-judge：性别0.99/年龄0.84/情绪0.77/WER 0.14；主观3.95/4.52超Seed Audio（Gemini-3-Pro）
- 多遍vs单遍81.9→81.3，音高/音域/口音+12.9/+12.0/+9.7；Buckeye onset 49ms；LongAudioSpan 79.0超音频模型

**是否开源**：代码未发布，demo见项目页；骨干/金标/基准公开，语料专有、给融合复现方法

### ⭐ 评分：8/10
评分理由：把时间戳描述重构为可组合函数接口，监督构造与推理范式均有实质创新，基于探测的潜在能力引出大幅降低副语言标注成本；MMSU、MSU-Bench感知增益扎实，理解生成双向验证充分。不足是骨干依赖既有captioner、生成器与语料未公开、情绪生成准确率仅0.59，复现受限；总体达顶会水准。

---

## [2] S3-S2ST: Semantically Supervised Streaming Speech-to-Speech Translation

**arXiv ID**：2610.36777 | **方向**：语音大模型

**作者**：Yuxiang Zhao, Zhiyun Fan, Yu Pu, Yanjie An, Yushen Chen, Wenrui Liang, Baiji Liu 等14人

**机构**：上海交通大学X-LANCE实验室、上海创智学院、阿里巴巴Token Foundry

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36777 | **PDF**：https://arxiv.org/pdf/2610.36777.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对流式语音到语音翻译（S2ST）"何时该commit译文"的决策难题，本文提出S3-S2ST：将句级平行语音对改造为"语义单元+640ms栅格"的增量监督数据，在Thinker–Talker架构上同时学习翻译内容与发射时机；READ/WRITE门控阈值可在推理时调节质量–延迟权衡，配合播放缓冲自适应阈值无需重训。4B稠密模型离线FLEURS达COMET 0.904与Qwen3-Omni（30B/3B）相当；流式9-pair上COMET 0.965超最强流式基线Hy-SimulMT（0.954）；RealSI上以几乎不增的首包延迟换来质量提升。

### 🔧 技术方案

**问题背景：** 流式S2ST必须决定等待多少源语音再翻译：过早会误译，而已播出的语音无法像文本那样被静默修正；句级平行语料只给最终译文，缺失"哪个源前缀支持哪个目标片段"的监督。SimulS2ST-Omni等靠改变输入chunk时长获得延迟档位，把决策频率与输入粒度耦合在一起。

**模型架构：** 4B稠密Thinker–Talker。Thinker为Qwen3.5-4B，编码器由SenseVoice初始化：640ms块含16个编码状态、经块因果adaptor压至8个位置，仅第一层允许160ms前瞻，保留31抽头FSMN卷积的居中抽头对齐；MLP门控读最终归一化Thinker状态输出WRITE概率；Talker由CosyVoice初始化，条件为Thinker第4–32共8层的通道级可学习加权融合（w_ℓ∈R^2560）再过投影，生成12.5Hz codec token，冻结的流匹配（流式FM8/离线FM15）与声码器渲染波形。

**核心创新：** (1) 语义监督的流式化：用Qwen3.7-Max按"前缀支持"约束切分对齐语义单元（禁止译文引入源信号晚于当前边界的信息），强制对齐将两端点量化到640ms栅格，构造READ/WRITE轨迹，使无时序标注的句级数据可直接监督commit时机。(2) 解耦的延迟控制：固定τ或播放自适应τ_t=0.1+0.89·sqrt(min(b_t/1s,1))，缓冲有可播音频时抬高阈值以等待更多上下文，空缓冲仍为0.1保住首次响应；不改权重、不改输入粒度即得不同权衡点。(3) 8层隐状态融合条件化：让语音生成同时利用不同深度的语义与声学表征，优于仅用末层。

**训练策略：** 三阶段：流式S2TT（encoder/adaptor/Thinker LoRA rank32训练10k步，lr 2e-5/1e-5，有效batch 128，序列长8192；再冻结编码器训练Thinker+门控10k步，约17k小时轨迹）→离线S2ST（约300k小时，15k步，batch 64）→流式S2ST（Talker子阶段5k步+E2E联合4k步）；损失L=L_text+L_codec+0.1·L_gate；训练对由Qwen3-Max翻译+CosyVoice3.5合成构建，流式混合约13k小时（双向各6.5k）。

### 📊 实验结果
**数据集**：FLEURS英汉测试集（汉译英945+英译汉646条）；内部9-pair集（每方向996条，未公开）；RealSI同传基准；训练语料约3M小时S2TT、300k小时离线、13k小时流式。

**主要指标**：
- 流式FLEURS（τ=0.5）：COMET 0.828、BLEU 29.83、ASR-COMET 0.769、SIM 0.606、UTMOS 3.75
- 流式9-pair：COMET 0.965、BLEU 60.51、ASR-COMET 0.933、WER 1.54
- 离线FLEURS：BLEU 34.52、COMET 0.904、WER 2.00，与Qwen3-Omni（30B/3B）相当
- 关键对比：9-pair COMET较Hy-SimulMT（1.6s）高+0.011、BLEU高+8.29且仅用4B稠密参数；MLP门控较8块固定调度COMET +0.014；自适应阈值较τ=0.1 ASR-COMET +0.014而StartOffset仅+70ms

**是否开源**：代码暂未发布，论文承诺将释出模型及训练、推理、数据构建pipeline；9-pair评测集不公开。

### ⭐ 评分：8/10
评分理由：以LLM语义切分+强制对齐把句级配对数据转化为commit监督，直击流式S2ST缺时序标注的核心痛点；阈值与播放自适应实现了免重训的延迟调节，比变chunk时长方案更解耦；基线涵盖Hy-SimulMT、SimulS2ST-Omni、X-Translator且消融链条完整，工程价值高。不足是仅评测英汉方向、依赖大量内部数据难以复现，9-pair上SIM逊于两个基线。属实质贡献明确、实验充分的顶会水准工作。

---

## [3] EmbeddingGemma 2: Unified and Efficient Multimodal Representations

**arXiv ID**：2610.37364 | **方向**：语音大模型

**作者**：Henrique Schechter Vera, Sahil Dua, Jovan Andonov, Sara Smoot, Sebastian Russo, 等（EmbeddingGemma Team）

**机构**：Google

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.37364 | **PDF**：https://arxiv.org/pdf/2610.37364.pdf | **代码**：https://ai.google.dev/gemma/docs/embeddinggemma | **Demo**：暂无

### 📌 简介
Google发布744M参数开源多模态嵌入模型EmbeddingGemma 2，解决文本嵌入模型处理音视频需ASR/描述器等外挂、而MLLM系多模态嵌入模型动辄数十亿参数难以端侧部署的问题。模型以271M双向Transformer为骨干，配167M ViT视觉编码器与305M Conformer音频编码器，将文本、图像、音频、视频及任意交错混合输入统一映射到768维空间，经"蒸馏→对比"渐进课程训练。MTEB(Code) 78.68、MMEB-v2 59.01、MAEB 49.87、MSEB检索69.54，跨模态树立新帕累托前沿，常超2-12倍于己的模型。

### 🔧 技术方案

**问题背景：** CLIP/SigLIP类双塔模型无法原生处理混合模态输入；由MLLM改造的嵌入模型规模偏大，不适合低时延、高吞吐与端侧隐私场景；ASR级联文本嵌入的管线丢失非语言声与环境声等副语言信号。

**模型架构：** 总参744M：271M双向注意力骨干（由Gemma 4解码器改装，去除因果掩码）+167M ViT（patch16）+305M音频编码器（2层下采样卷积+12层Conformer，USM架构，全程冻结）。模态编码器输出soft tokens与文本token交错拼接：音频按40ms块mel滤波器组输入、每秒25个token；图像限280视觉token，视频1fps采样、每帧140 token并可交错音轨带MM:SS时间戳。骨干输出mean pooling后经线性投影+L2归一化得768维嵌入，MRL支持截断至512/256/128维。

**核心创新：** (1) 简化版逐层嵌入PLE：取消专用查找表，仅用主嵌入表与模态编码器输出经每层线性投影、GELU门控调制后回注残差，省参数反提性能，MMEB-v2总体55.46对55.07，因非文本模态得以共享同一token嵌入空间。(2) 模态-目标双课程：文本预微调（300B token，几乎纯蒸馏）→多模态预微调（2T token，embedding-matching蒸馏自Gemini Embedding 2）→多模态微调（600B token，用含同塔负例的NCE对比损失、GOR正则、MRL与Plackett–Luce列表损失完全替换蒸馏），使模型脱离教师空间；微调末对早/晚checkpoint做权重平均合并。(3) 资源弹性设计：合并后新增QAT尾段，提供int4 Q4_0/Q4_C检查点，Pixel 11 Pro峰值内存191/447/567MB；推理时视觉token预算70–1120可调。

**训练策略：** 课程采样见上；预微调阶段用更大batch与更大学习率扩充批内负例，微调转小学习率与高质量任务数据；对比损失弃用硬度加权以避免放大噪声正例。

### 📊 实验结果
**数据集**：MTEB（162任务、250+语言）、MMEB-v2（78任务）、MIEB(lite)、MAEB（30任务，语音/音乐/环境声/生物声学/情感）、MSEB(Retrieval)（26语种语音检索，MRR@10），训练共约2.9T token。

**主要指标**：
- MTEB(Code) 78.68，超全部sub-4B模型；MTEB(多语) 61.36、较EG1 +0.21
- MMEB-v2 59.01（仅用439M参数），比986M的jina-embed-v5-omni-nano高15.4；MIEB(lite) 60.17，较sub-1B最强+7.9
- MAEB 49.87，A2A检索53.6、音频分类52.9为sub-1B第一；128维仍超所有sub-1B模型
- MSEB 69.54，比自身ASR级联57.59高11.95、比EG1-ASR高18.59；教师Gemini Embedding 2为73.99
- 关键消融：冻结视觉编码器使MMEB-v2掉4.09分；去掉微调对比阶段仅52.28；int4量化MTEB多语仅降0.40

**是否开源**：已开源bfloat16与int4量化权重（Gemma许可），模型页 https://ai.google.dev/gemma/docs/embeddinggemma；训练代码未发布。

### ⭐ 评分：8/10
评分理由：全模态统一评测的帕累托前沿扎实，PLE简化、课程式蒸馏-对比切换与原生音频vs ASR消融对语音社区尤具参考价值，端侧内存数字可复核。不足在音频编码器直接复用Gemma 4且冻结、MAEB均值距教师仍差约3.5分，副语言零样本能力弱（性别聚类0.40），内部训练数据不可复现；属高工程水准的系统性贡献而非方法突破。

---

## [4] AudioRSI: Recursively Self-Improving Audio Reasoners

**arXiv ID**：2610.36578 | **方向**：语音大模型

**作者**：Jiajun Fan, Roger Ren, Jingyuan Li, Rahul Pandey, Prashanth Gurunath Shivakumar, Ankur Gandhe, Yile Gu, Ge Liu, Ivan Bulyko

**机构**：UIUC（伊利诺伊大学厄巴纳-香槟分校）

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36578 | **PDF**：https://arxiv.org/pdf/2610.36578.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有音频大模型RL的奖励全部来自模型外部：只看最终答案的结果校验、需人工调权的过程分、或训练全程冻结的LLM裁判，导致"学生进步、监督者不变"。本文提出AudioRSI：单一模型同时充当Actor（以`<think>…<answer>…`格式生成推理路径）与Critic（对组内候选路径两两比较输出胜/平/负，折算过程级奖励），并每200步将Critic同步替换为当前Actor，形成递归自我改进；Critic与Actor听同一段录音，可拒斥引用不存在声学证据的推理。在四个与AVQA训练分布不相交的OOD基准上：MMAU test-mini达76.10%，MMSU以62.52%排名第一，MMAU-Pro最难Multi-Audio项37.9%领先全部受测系统，MMAR 64.0%领跑7B开源梯队。

### 🔧 技术方案

**问题背景：** 结果导向奖励让"蒙对"与"严谨声学分析"得分相同，二元信号无法区分到达答案的路径；人工过程奖励需多项调权；外部LLM裁判标准固定，OOD精度在训练后半程停滞。核心问题是：监督者能否也学习，且随策略一起变强。

**模型架构：** 基座为Qwen2.5-Omni-7B，在AVQA上用GRPO微调。Critic是Actor权重的一份副本，critic模式输入音频、问题、选项与两条匿名化推理路径输出三元判断，映射为胜1.0/平0.5/负0.0；总奖励=结果校验+格式合规+自批评（λ均为1.0），优势用组均值基线、省略组内标准差归一化。每T步做带守卫同步：仅当Actor在当前训练mini-batch上结果精度不低于现任Critic才交接critic角色。

**核心创新：** (1) 模型自评过程奖励：候选与组内在线采样的参考路径两两比较，胜场频率即奖励，把过程监督从手写规则或外部裁判移入策略内部；音频是关键优势——能听的Critic可核对每条声学主张，纯文本Critic只能检查表层合理性。(2) 周期性critic同步构成递归步：周期内Critic冻结保证奖励平稳（规避行为分布漂移问题），周期末由改进后的Actor接任，使奖励标准随策略上升；消融显示同步过密不稳定、过疏退回冻结。(3) 全程自足训练：无外部裁判、无手工过程分、无需单独训练奖励模型，参考路径默认同组在线抽样，离线固定参考反而更差。

**训练策略：** 仅用AVQA音轨（视觉帧丢弃）；GRPO超参对齐Ke-Omni-R：组大小G=8、lr 1e-5、KL系数0.01、batch 8、最多6400步、同步周期默认200；无CoT SFT数据、无任务定制提示；8×NVIDIA H200训练3–4天；批评pass相对actor rollout有额外开销（未报告受控wall-clock对比）。

### 📊 实验结果
**数据集**：训练AVQA（仅音轨）；评测四个OOD基准：MMAU test-mini（1,000题）、MMSU（5,000样本）、MMAU-Pro（5,305样本）、MMAR（1,000样本）

**主要指标**：
- MMAU test-mini：76.10%（Sound 82.58/Music 69.16/Speech 76.58），较同协议Ke-Omni-R 74.60%高1.5pp，超Audio Flamingo 3（73.30）与Gemini 2.5 Pro（71.60）
- MMSU：Overall 62.52%第一（Reasoning 80.54、Perception 45.62），仅险胜AF3/Ke-Omni-R 0.22/0.44pp
- MMAU-Pro：Multi-Audio 37.9%领先所有系统（Gemini 2.5 Flash 21.2垫底），Avg 55.9%为开源最强
- MMAR：64.0%，无外部奖励模型方法中7B开源第一，Music 56.8%全表最高
- 行为分析：Premise & Deduction出现率94.4%（Ke-Omni-R 62.7%、基座53.3%）；外部GPT-4o Audio裁判胜率81.2%/74.7%
- 消融：去自批评-1.5pp；冻结外部裁判约-1.0pp；T=200近最优

**是否开源**：未见官方代码与Demo，暂无

### ⭐ 评分：7/10
评分理由：首次把过程级奖励移入策略内部并利用音频"可核对性"实现递归自我改进，范式干净、动机与消融互相咬合，四个OOD基准+训练动态+外部裁判交叉验证证据链较完整。局限是单一骨干、单一语料、单种子，多数领先在零点几pp量级，自我偏好偏差未彻底排除，训练期批评开销未量化且代码未开源。作为"监督者也能学习"的可行性验证有实质贡献，推广性有待后续检验。

---

## [5] Tap2Listen: Instant Target Switching for Streaming Audio-Visual Speaker Extraction

**arXiv ID**：2610.36643 | **方向**：语音前端

**作者**：Hansol Park, Minkyung Song, Zinu Kim, Yujun Lee, Hoseong Ahn, Hyunjin Choi, Kyuhong Shim

**机构**：Sungkyunkwan University

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36643 | **PDF**：https://arxiv.org/pdf/2610.36643.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
流式音视频目标说话人提取（AV-TSE）现有系统在整个片段内固定目标说话人，而对话场景需要频繁且即时地切换目标，点击不同人脸应立刻只输出对应说话人。本文提出Tap2Listen：目标无关的因果音频编码器仅处理混合音频并维护共享缓存，选定人脸的视觉线索只条件化解码器，一次切换仅需0.12 ms缓存重投影即立即生效。在LRS3-2mix上SI-SNRi由基线8.85提升至9.68 dB，切换至已知人脸后首帧即满质量输出（基线需约1秒恢复），并在单颗移动CPU核心上实时运行。

### 🔧 技术方案

**问题背景：** 现有流式AV-TSE系统中音频与视觉信息在全链路深度耦合，且递归、自回归或说话人跟踪状态会累积目标相关记忆，切换目标后旧说话人信息残留、需等待状态衰减，无法实现即时切换；交互式目标切换此前几乎未被研究和评测。

**模型架构：** 整体8.06 M可训练参数。编码器将16 ms窗、8 ms跳的STFT帧投影到256维，接6个pre-RMSNorm局部因果自注意力块（128帧窗口），维护目标无关的共享时间缓存；冻结视觉前端提供条件：因果BlazeNet64输出25 Hz唇动特征（每脸4 s滚动缓冲）、face embedder输出身份ID向量。解码器是唯一目标依赖组件：缓存音频表征与所选脸唇特征拼接形成注意力记忆k,v=W[ȧ;lip]（M=500帧即4 s），身份嵌入仅加性进入查询；查询经K=4个交叉注意力+FFN块，共享掩码头在每块输出复数比例掩码，iSTFT重叠相加重建波形；解码器无输出自注意与自回归反馈。

**核心创新：** (1) 按目标相关性分离计算：编码器只处理混合语音，缓存在切换间保持有效，切换仅需对缓存窗口重算记忆投影（0.12 ms）并替换身份项，无需重跑音频编码器，从根本上消除状态恢复期。(2) 视觉信号双通道解耦：时变唇动特征进入交叉注意力记忆引导音视频时间对应，固定身份嵌入仅进查询，使切换代价最小化且回到曾见过的脸与任意切换开销相同。(3) 组件化损失：解码器侧深监督提取损失Σw_k·clamp(−SI-SDR,−30 dB)，权重(0.1,0.2,0.3,0.4)偏重后块；编码器侧纯混合信号自监督预测5帧后Δlog|X|的线性头损失，无需目标标签。

**训练策略：** ClearerVoice版LRS3-2mix协议，40k/5k/3k训练/验证/测试行，功率匹配干扰声按±10 dB SIR混合，训练时干扰者与SNR每步重采样；单张RTX 3080训150 epoch（28 GPU时），bf16，batch 16，AdamW余弦调度1e-3→1e-5，EMA 0.999并按EMA权重报告结果。

### 📊 实验结果
**数据集**：LRS3-2mix（ClearerVoice协议3,000条固定测试混合；切换评测重构AV-SkiM注意力转移协议）

**主要指标**：
- SI-SNRi：9.68 dB，超AV-SkiM基线8.85 dB（+0.83 dB，参数量同为8.1 M）
- SNRi / PESQi / STOIi：10.05 dB / 0.71 / 0.20，基线9.16 dB / 0.52 / 0.19
- 切换恢复：切至已知脸首个200 ms窗口即领先2.59 dB、无恢复期，基线约1 s才追平；新脸切换后首1 s领先8.08 dB，80 ms处峰值差11.9 dB
- 端侧时延：S22大核ONNX fp32单线程，8 ms帧处理3.2 ms（预算40%），触发切换总时延8.5 ms p95；算法时延16 ms，高于基线约1 ms

**是否开源**：暂无（全文未提供代码仓库或Demo链接）

### ⭐ 评分：7/10
评分理由：将交互式目标切换确立为流式AV-TSE需显式设计与评测的系统属性，问题定义新颖；架构解耦干净，切换后输出与从头条件化等价且首帧无恢复期，移动端单核实时验证充分，固定目标质量还同步提升0.83 dB。不足是对比基线仅AV-SkiM一个、数据集单一，算法时延劣于基线，且未开源代码，复现与横向比较受限，属有实质贡献的高质量工作。

---

## [6] From Voiceprints to User Entities: Online Speaker-Memory Construction for Multi-User Spoken Agents

**arXiv ID**：2610.36713 | **方向**：语音前端

**作者**：Yucong Zhang, Cancan Li, Bo Xiao, Ke Zeng, Ming Li

**机构**：美团、香港中文大学（深圳）、武汉大学

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36713 | **PDF**：https://arxiv.org/pdf/2610.36713.pdf | **代码**：https://anonymous.4open.science/r/EvoSpeakerMem-4AF1 | **Demo**：https://anonymous-user428.github.io/evo-speaker-mem-demo

### 📌 简介
多用户语音智能体须在访问用户记忆前先辨认说话人，而现有记忆基准均默认历史已正确归属。本文提出"声纹只是身份的观察而非身份本身"，形式化在线说话人-记忆构建问题，给出免训练的EvoSpeakerMem语音支持层：按时间序create/link路由、选择性更新声学状态、按身份分区读写文本记忆，并构建LoCoMo-ID语音记忆基准。SMIIP-TV上固定模板真探针拒识率约一年从29.8%升至55.6%；LoCoMo-ID上身份门控QA较固定表征在干净/条件偏移下分别提升3.86与11.62个百分点且无错误授权。

### 🔧 技术方案

**问题背景：** 同一说话人录音随环境、设备与状态漂移，固定注册声纹无法长期充当身份键；归属错误进入记忆写路径后果持久——错误新建碎片化一人历史，错误链接污染用户画像，且现有Audio LLM缺少持久说话人状态。

**模型架构：** EvoSpeakerMem由ECAPA-TDNN编码器、说话人实体注册表与可替换文本记忆后端（LightMem+Qdrant，bge-small-en-v1.5嵌入）构成。每实体维护声学embedding中心、观测计数与分区原子事实：最高余弦分低于合并阈值θ=0.489（VoiceDesign合成声纹库标定的EER工作点）即新建实体，否则链接该实体并写入其记忆分区；查询时做读侧声纹匹配并限定分区检索。

**核心创新：** (1) 将说话人归属纳入记忆写入/读取路径，形式化在线speaker-memory construction，以因果first-seen绑定协议评测，杜绝未来信息重标实体。(2) 分配与中心更新解耦：链接后仅当相似度超过更严阈值τ=0.58才更新中心而路由固定0.489，阻断错误链接自增强污染并降低碎片化；与Fixed/Update/All-exemplar KNN对比揭示碎片化-污染权衡。(3) 构建LoCoMo-ID：改写1371条问题为第一人称敏感查询，Qwen3-TTS合成17646条历史与5958条查询语音，叠加模拟录音条件偏移与同名冲突事实四说话人交错压力测试。

**训练策略：** 完全免训练，阈值均为推理期标定：合并/查询0.489（EER点）、门控更新0.58（扫参使错误授权115次归零）；转写、抽取、作答与judge用本地Qwen3-Omni-30B-A3B-Instruct，LLMLingua-2预压缩率0.6；合成经UTMOS与ECAPA相似度双QC，不合格最多重采样4次。

### 📊 实验结果
**数据集**：LoCoMo-ID（10段历史5882轮、1986条QA，30干净+30偏移合集）；SMIIP-TV（373人90天重复录音）；MSU-Bench。

**主要指标**：
- B3F1（ECAPA-only、偏移条件）：Fixed 74.18→Gated 92.73、KNN 96.62（%）
- SMIIP-TV固定模板真探针拒识：29.8%→55.6%（0–1天→约1年），EER 9.7→14.0%
- 身份门控QA（4113条敏感查询）：干净71.41→75.27（+3.86pp）、偏移60.15→71.77（+11.62pp），Gated错误授权0次vs KNN 116次
- 四说话人压力测试：full QA 67.83→73.60、B3F1 97.77（Fixed→Gated）
- MSU-Bench外挂工具：SR 96.61/SV 79.35，超最强端到端Audio LLM Gemini-3-Flash（69/75）

**是否开源**：anonymous.4open.science仓库EvoSpeakerMem（匿名），数据集已发布至HuggingFace，交互Demo在线。

### ⭐ 评分：7/10
评分理由：将说话人归属纳入记忆构建的问题形式化新颖，分配与更新解耦的免训练门控简洁有效；同时报告聚类质量、授权安全与端到端QA并诚实揭示碎片化-污染权衡，可信度高。局限是全合成语音、模拟条件偏移且依赖ECAPA分数域标定，但基准与协议对多用户语音智能体研究有实质参考价值。

---

## [7] The Content Leash: Mitigating Degenerate Solutions in Invertible Speaker Anonymization

**arXiv ID**：2610.36768 | **方向**：语音前端

**作者**：Nirjon Mobarak Talukder, Rafid Ahmed, Mohammad Ishrak Abedin, Abu Raihan Mostofa Kamal

**机构**：Islamic University of Technology, Dhaka, Bangladesh

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36768 | **PDF**：https://arxiv.org/pdf/2610.36768.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对基于条件可逆网络（cINN）的可恢复说话人匿名化方法Rano做论文指导式复现，发现退化解：发表目标不约束匿名化输出内容，优化器可借严重语音降质降低triplet损失、制造"高EER+完全不可懂"（41.6% EER但WER 117.6%）的假隐私。作者提出三项修改：anchor与range损失约束输出谱、ECAPA蒸馏mel域验证器泛化到未见验证模型、含测量底限与seeds的评测协议。最终在38个未见说话人上达ECAPA EER 26.31±0.25%、WER 11.75%、密钥还原说话人相似度94.90%。

### 🔧 技术方案

**问题背景：** 在Rano类cINN匿名化中，consistency损失只作用于以真实说话人嵌入为条件的另一前向，triplet损失只看匿名化谱Xa的说话人嵌入，没有任何项惩罚Xa内容改变，目标可被语音降质"作弊"；且对轻量验证器训练的匿名化器骗不过独立强验证模型。

**模型架构：** 匿名化器为12个条件耦合块的cINN（26.5M参数），在80-band log-mel（22.05kHz、hop 256、窗1024）上运行；秘密密钥k~N(0,I)经8块耦合的ACG生成伪说话人条件c，前向Xa=f(X;c)，逆用同一密钥精确还原（往返MSE约1e-6）；波形由微调30k步的HiFi-GAN合成。

**核心创新：** (1) 内容约束损失：anchor损失MSE(Xa,X)把输出拉回原谱，与triplet形成权重可调的隐私-效用平衡；range损失对原话语动态范围包络做hinge，仅惩罚越界值；另加log|det J|²正则（λ=0.01）保证逆过程数值稳定。(2) ECAPA蒸馏验证器：独立ECAPA仅18.35% EER仍可识别，将冻结ECAPA-TDNN以逐样本余弦对齐+批量成对相似度矩阵匹配蒸馏进256维mel域TDNN V_mel，并重训ACG。(3) 严格评测协议：每项指标配干净音频底限、附训练全程未见的异族ResNet held-out验证器、伪密钥种子化并报3 seeds均值±方差、仅用与所有训练语料无交集的说话人测试。

**训练策略：** 蒸馏30k步（AdamW、lr 1e-3、batch 64）、ACG 80k步；匿名化器52k步（λ_anchor=0.2、λ_2=5）后warm-start 12k步（λ_anchor=1.0、λ_range=1.0、margin m=0.3），取第二阶段8k步checkpoint；数据VCTK+LibriTTS train-clean-100按话语85/15切分；单卡RTX 6000 Ada。

### 📊 实验结果
**数据集**：训练VCTK+LibriTTS train-clean-100；评测LibriTTS test-clean 38个未见说话人303条（2417 genuine/89392 impostor对），ignorant攻击者设定。

**主要指标**：
- ECAPA-TDNN EER 26.31±0.25%（干净底限2.83%）；held-out ResNet 27.86%（底限2.08%）
- WER 11.75%（底限2.48%，Whisper large-v3），McAdams基线8.44% EER/WER 3.61%
- 匹配消融：加两损失后WER从117.58%降至8.29%、mel MSE从6.551降至1.338；蒸馏验证器在同设置下EER从18.35%升到39.58%（+21.2点）
- 还原Sim_spk 94.90%，等于vocoder往返底限（Rano 87.75%）；错误密钥还原相似度约4%且随密钥距离保持平坦（Rano为4.66%→12.78%，存在可搜索梯度）

**是否开源**：正文未提供代码仓库或Demo链接（亦指出Rano无官方实现），暂无。

### ⭐ 评分：7/10
评分理由：以严格匹配消融揭示了可逆匿名化公开训练目标的内容约束盲区，anchor/range损失与ECAPA蒸馏验证器改动小但动机与证据扎实，密钥距离平坦响应具安全价值，评测协议有示范意义。不足在于绝对隐私水平不及原方法报告、WER相对底限代价偏大、单语料单攻击者、无代码发布，整体属扎实增量贡献而非突破。

---

## [8] Developing a Speech Language Model for Basque

**arXiv ID**：2610.36911 | **方向**：语音大模型

**作者**：Andoni Sudupe, Inma Hernáez Rioja, Ander Arriandiaga, Christoforos Souganidis, Ibon Saratxaga, Eva Navas

**机构**：HiTZ Basque Center for Language Technology / Aholab，巴斯克大学（UPV/EHU）

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36911 | **PDF**：https://arxiv.org/pdf/2610.36911.pdf | **代码**：暂无（声明将开放GitHub与HuggingFace） | **Demo**：暂无

### 📌 简介
为解决少数民族语言缺失端到端语音大模型、级联ASR+LLM+TTS管线带来语义损失、误差累积与高延迟的问题，本文提出首个开放的巴斯克语语音大模型：基于LLaMA-Omni模块化架构，以巴斯克语指令版Latxa-3.1-8B-Instruct为骨干；针对语音指令数据稀缺，用Latxa-3.1-70B翻译VoiceAssistant-400K并经VITS多音色TTS合成音频，构建约45万组口语指令对。评测显示内容质量3.86/5、输出语音WER 9.94%、UTMOS 3.07、流式延迟370ms，可懂度与内容质量接近英文LLaMA-Omni。

### 🔧 技术方案

**问题背景：** 开源SLM（LLaMA-Omni、Spirit LM等）几乎只覆盖英中双语，语音模态使少数民族语言劣势加剧；巴斯克语不存在（音频输入、文本输出、离散单元输出）三元组指令数据，无法负担大规模多模态预训练，级联管线又无法满足低延迟对话需求。

**模型架构：** 遵循LLaMA-Omni模块化设计。输入侧由巴斯克适配的Whisper-large-v3-eu编码语音，语音适配器先降采样、再经两层ReLU FFN映射到LLM嵌入维度后注入Latxa-3.1-8B的prompt；输出侧取LLM生成文本前的隐状态，绕过中间文本并行解码：语音解码器上采样后用非自回归Transformer预测离散语音单元——单元取自微调后mHuBERT-147第9隐层并经K-Means（1000质心）聚类，最后由ECAPA-TDNN说话人嵌入条件化的多说话人Unit HiFi-GAN声码器合成波形；推理按块大小Ω=40分块流式合成。

**核心创新：** (1) 首个开放的巴斯克语端到端SLM：LLaMA-Omni架构恰基于LLaMA-3.1-8B，与巴斯克指令版Latxa骨干完全兼容，仅训练适配器与解码器即可把文本语言能力迁移到语音模态，免去多模态预训练，极低算力落地。(2) LLM翻译+TTS合成的指令数据管线：用严格rubric提示Latxa-3.1-70B翻译英文语料消除MT直译错误；问题用14个性别均衡合成音色，答案固定用声码器目标说话人，且SLM与声码器共用同一HuBERT编码器与K-Means模型避免离散单元错配。(3) 两阶段冻结式训练：Stage1冻结语音编码器、仅训适配器与LLM学习语音理解与口语化回复；Stage2冻结除NAR解码器外全部模块，以CTC损失对离散单元做变长对齐，无需显式文本-语音对齐。

**训练策略：** HuBERT在600小时composite-eu上ASR微调，100 epochs、batch 64、1×H100约400小时；声码器用Maider/Antton各16小时训1000 epochs、约10小时；SLM两阶段各3 epochs，沿用LLaMA-Omni推荐超参，4×A100-80G总耗时不足100小时。

### 📊 实验结果
**数据集**：合成巴斯克语语音指令集（约45万问答对，问题音频约550小时、答案音频超3300小时）；测试集为4,419条与训练不相交的合成指令（同分布）

**主要指标**：
- 内容质量 LLM-as-a-Judge（Latxa-70B评分）：3.86/5，接近英文LLaMA-Omni的3.99，超Qwen2-Audio 3.47与SALMONN 3.44
- 输出语音可懂度：WER 9.94%、CER 1.62%（HiTZ Conformer ASR口径），优于LLaMA-Omni英文10.82%
- 语音质量：UTMOS 3.07，落后LLaMA-Omni 3.92约0.85分
- 模块指标：HuBERT离散编码器ASR WER 4.90%；声码器MCD Antton 4.8dB、Maider 5.1dB
- 流式首包延迟：370ms（A100、Ω=40），与LLaMA-Omni 346ms相近，较级联管线5587ms降低约5.2秒

**是否开源**：声明全部材料开放——模型/数据上HuggingFace、代码上GitHub（正文未附直接链接），TTS语料有Zenodo链接

### ⭐ 评分：7/10
评分理由：作为首个少数民族语言开放端到端SLM，其"模块化迁移+全合成数据+两阶段CTC训练"配方完整可复现、训练成本低，多项指标对齐英文LLaMA-Omni，对同类低资源语言具直接推广价值。不足在于评测全部基于同分布合成语音，judge与骨干同属Latxa家族存在自我偏好风险，缺少真人语音与人工评估，且UTMOS差距明显，实验严谨性限制了结论强度。

---

## [9] StreamSE: Neural Audio Codec-based Streaming Speech Enhancement for On-device Inference

**arXiv ID**：2610.37024 | **方向**：语音前端

**作者**：Hyunjin Choi, Zinu Kim, Junwon Moon, Jeongyun Chae, Seungbeom Kim, Kyuhong Shim

**机构**：Sungkyunkwan University（成均馆大学，韩国）

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.37024 | **PDF**：https://arxiv.org/pdf/2610.37024.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
生成式语音增强感知质量高，但非因果结构与迭代采样使其难以流式端侧部署。本文提出StreamSE：一个在冻结神经音频编解码器潜空间上运行的20M参数流式增强模型，因果Transformer逐帧从带噪潜变量直接回归干净连续潜变量，并以自身历史帧的量化预测作条件反馈，每帧单次前向即可增强、无需采样与look-ahead；另将RVQ截断至8个粗层级，每帧token减半且提升混响鲁棒性。在DNS Challenge 2020测试集上，作为唯一流式生成模型取得7/9项DNSMOS最优，完整int8流水线在智能手机单CPU核心上实时运行。

### 🔧 技术方案

**问题背景：** 端侧场景（电话/助听器/语音助手）要求因果性与单帧80ms内算力，而现有生成式方法或整句非因果（SELM）或需迭代采样（扩散类），高感知质量难在流式端侧实现。

**模型架构：** 全因果流水线=冻结codec MOSS-Audio-Tokenizer-Nano（约22M、12.5Hz帧率、潜维768、16级RVQ）+StreamSE（约20M可训）：6层8头decoder-only因果Transformer（隐维512、RoPE）；输入拼接带噪潜变量与上一帧回喂潜变量，回归增强潜变量后由codec解码重建波形。

**核心创新：** (1) 连续潜变量回归取代逐级离散token分类：离散生成须逐级分类、开销随级数线性增长，本方法每帧一次回归连续潜变量、重建交给codec，免采样免look-ahead。(2) 自预测回喂的自回归条件：训练对c_quant做teacher forcing，推理回喂自身h_quant保持时序一致，首次将连续预测与零look-ahead因果流式结合。(3) RVQ粗级截断：利用quantizer dropout仅留k=8，每帧token减半，佐证细级携带残余混响假设。

**训练策略：** L=L_emb+0.2·L_wav+0.5·L_mel：潜空间对c_embed做L1回归；辅助损失以codec往返c̄为参照剔除重建误差、STE透传。在线合成：LibriTTS-R clean-100/360+VoiceBank-DEMAND混WHAM!/DEMAND噪声（SNR −5~20dB）、0.5概率加openSLR26/28 RIR且以干信号为目标，段长125帧、20 epoch、batch 48、AdamW、LR升温至6e-4后退火、dropout 0.2。

### 📊 实验结果
**数据集**：DNS Challenge 2020测试集（有混响/无混响/真实录音三类，48kHz），无参考DNSMOS P.835（SIG/BAK/OVL）；基线数值引自SELM论文

**主要指标**：
- StreamSE（ℓ=0，fp32）：有混响SIG/BAK/OVL 3.417/3.990/3.086，无混响3.617/4.124/3.361，真实录音3.399/3.830/3.016
- 关键对比：9项指标类别组合中7项全场最优（含两个合成类全部6项，均超最强离线基线），ℓ=0有混响OVL较SELM 2.695提升0.391
- 截断消融：k=8较k=16有混响OVL +0.048（2.973→3.086），无混响SIM −0.024（0.818→0.779）
- 端侧int8：Galaxy S22单大核p95帧耗61.04ms（占80ms预算76%、无超帧），编码器/StreamSE/解码器27.72/5.46/27.86ms，codec占延迟91%；量化后OVL仅降0.06~0.1

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：连续潜变量回归与全因果流式、端侧逐帧实测的组合务实稀缺，让生成式增强在匹配离线感知质量的同时跑进手机单核实时预算，截断消融与延迟拆解证据扎实。不足在于仅在DNS2020老基准以客观DNSMOS评估、基线数值转引而非复测、缺主观听测，且截断的相似度与混响鲁棒性权衡未完全解决，属扎实工程贡献而非方法突破。

---

## [10] Beyond Answer Changes: Matched Same-Class Controls for Local Audio Evidence

**arXiv ID**：2610.37605 | **方向**：语音大模型

**作者**：Yunuo Wang, Maoyuan Chen, Yuanjin Huang, Xing Liu

**机构**：香港科技大学（广州）、武汉大学、新加坡国立大学、Northeastern University（多伦多）

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.37605 | **PDF**：https://arxiv.org/pdf/2610.37605.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
音频-语言模型（ALM）在被查询声事件发生局部编辑后改变答案，可能源于对事件类别的响应、对波形被改写的敏感，或两者混合，现有干预评测无法区分。本文提出匹配的同类别替换控制协议：异类替换与同类替换共享同一时间区间、电平估计、供体拟合与交叉淡入淡出，仅前者改变查询类别而后者保持正确答案不变。在600个合成声景、3个模型（Qwen2.5-Omni-7B/3B、Fun-Audio-Chat-8B）上，异类替换比同类替换多引发49.7至60.9个百分点的答案变化，同类准确率与原准确率差距不超过5.2个百分点，声景加权选择准确率达73.7%至81.9%。

### 🔧 技术方案

**问题背景：** ALM答案是否真正由局部声学证据支撑是可信度评测核心。现有噪声/区域掩蔽、注意力引导掩蔽、反事实声音植入等方法把"改变目标类别"与"局部重写波形"混为同一复合处理，答案变化无法归因。

**模型架构：** 本文为评测协议而非新模型。用Scaper将FSD-MIX-SED单标签前景与TUT城市声学场景2018背景混成10秒16kHz声景（名义事件-背景比+10dB），33个查询类别，二选一问答在两种选项顺序下各测一次。围绕原音频设六种干预：异类替换、同类替换、干扰移除、无事件背景窗重写、全片段静音、sham自替换（编辑路径相同，浮点舍入仅在约16万样本中改动至多1个LSB）；渲染后校验背景噪声底差中位数低于1dB、边界差分在原音频3倍以内。

**核心创新：** (1) 匹配同类替换对照：同类臂在同一区间插入同类别另一条录音，正确答案不变，分离出对"局部重写"的纯响应，与异类臂配对作差即在相同编辑程序下类别变化的净效应；配合nuisance、背景窗、静音、sham构成完整对照设计。(2) 答案变化的精确分解：对固定选项-类别映射的二元问答给出恒等式Δ=G_ind+2Cov(C_o,C_d)+2Cov(C_o,C_s)，以独立性参考值定位观测差距。(3) 方向性选择准确率：在原始与同类均答对的合格试验上检验改变后的答案是否恰好指向插入类别，按声景等权聚合，把"认出新类别"与"答案漂移"区分开。

**训练策略：** 纯推理评测，无训练。协议设准入条件：三个模型原始准确率均高于0.75且静音条件改变超过20%答案；置信区间采用配对声景bootstrap，保持选项顺序与全部干预条件成组重采样。

### 📊 实验结果
**数据集**：600个Scaper合成声景（FSD-MIX-SED/FSD50K前景+TUT ASE2018背景，10s/16kHz，33类，458条背景录音），每模型每条件1,200次试验。

**主要指标**：
- 异类替换答案变化率：73.17%/70.25%/65.33%（Qwen2.5-Omni-7B/3B、Fun-Audio-Chat-8B）
- 同类重写答案变化率：12.25%/12.50%/15.67%；配对差距Δ=60.92[57.25,64.58]/57.75/49.67[45.33,53.92]个百分点
- 同类准确率0.859/0.841/0.795，较原始差距在5.2pp内；声景加权选择准确率0.819/0.801/0.737
- 对照：sham低于1.0%，背景窗低于1.6%，干扰移除5.5–7.5%
- 关键对比：log-mel编辑距离匹配子集（472次试验）差距仍为0.617/0.530且95% CI不含零；33个类别逐类差距全部为正

**是否开源**：论文未声明代码或数据发布，暂无

### ⭐ 评分：7/10
评分理由：同类型匹配替换巧妙地把类别响应从复合编辑处理中解耦，配合精确协方差分解、四类对照与编辑距离匹配子集，归因逻辑严谨，跨两架构家族33类结果一致。局限在合成声景、单一信噪比、33类，选择准确率依赖模型自身合格子集，生态效度有限；属方法扎实的增量评测贡献而非模型突破。

---

## [11] Partially Edited Audio: Generation, Defense, and Open Problems

**arXiv ID**：2610.37640 | **方向**：语音大模型

**作者**：Lin Zhang, You Zhang, Nicholas Evans, Xin Wang, David Harwath, Abhinav Dhall, Bowen Shi, Chengzhe Sun, Siwei Lyu, Sanjeev Khudanpur

**机构**：Independent Researcher、Télécom Paris、EURECOM、NII、UT Austin、Monash、SUNY Buffalo、JHU

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.37640 | **PDF**：https://arxiv.org/pdf/2610.37640.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文为ICASSP 2027特殊session撰写的部分编辑音频（partially edited audio）综述，首次从生成与防御双视角统一梳理该范式。文章沿"部分/完整"与"编辑/生成"两维下定义，归纳共存性、局部性、双重意图三特征，论证"fake/有害"是取决于披露、同意与信任假设的应用性判断而非编辑操作固有属性。综述按编辑目标-方法-评估组织生成侧，按检测-定位-deepfake分离-可解释性组织防御侧，指出现存防御仅集中于语音语言内容的时序编辑，并提出协同开发、主动水印溯源、真实场景、域泛化等开放问题。

### 🔧 技术方案

**问题背景：** 生成式音频模型已从整段合成走向对真实录音的局部选择性编辑（词/短语替换、插入、删除，及情绪、韵律、背景音修改），但生成与安全社区研究彼此割裂：无统一框架连接编辑效用与取证责任，且"何为fake"的判定标准长期含糊。

**模型架构（综述框架）：** 生成taxonomy分三层：编辑目标（语言内容、韵律/说话风格、副语言/情绪、声学环境、音乐与通用声音、跨模态同步）；编辑方法（DSP剪辑/复制移动→Voicebox式先合成后拼接→VoiceCraft等自回归codec语言模型masked区间插值与非自回归diffusion/flow-matching在频谱或latent空间填补→指令条件单模型）；生成评估须兼顾编辑区与未编辑区。防御taxonomy分四层：utterance级检测（whether）、segment级时序定位（when/where）、deepfake diarization（判别各编辑段由何种生成过程产生）、可解释性分析。

**核心创新：** (1) 给出部分编辑音频的正式定义与"accountability"判定框架：codec编辑会整段重编码，未编辑段是否应被标记取决于应用需验证的属性，据此规范训练标注与评估协议。(2) 首次打通生成-防御双侧taxonomy，指出编辑拼接边界伪影正是检测器依赖的线索、防御分析可反馈改进编辑质量，并论证GAN式对抗类比不成立——合法编辑追求utility而非逃避检测。(3) 系统梳理RealEdit、MMAE、PartialSpoof、HAD、LlamaPartialSpoof、WeDefense、DeepFense等资源，凝练协同开发、主动保护、真实场景、泛化、跨模态五大开放问题方向。

**训练策略：** 本文为综述、无自有模型训练；其提炼的防御训练规律为：训练数据比网络结构更关键——仅用全生成样本训练的检测器在部分编辑音频上显著退化，直接用含短fake嵌入段的编辑数据训练可同时泛化到两种设定。

### 📊 实验结果
**数据集**：综述覆盖PartialSpoof（英语）、HAD（普通话）、ADD系列、LlamaPartialSpoof、LENS-DF、AV-Deepfake1m系列；生成侧benchmark为RealEdit与MMAE。

**主要指标**：
- 转录正确性：WER（口径不足——转写达标仍可能引入说话人/韵律/声学不一致）
- 自然度：UTMOS等自动MOS预测
- 说话人一致性：WavLM等SV嵌入相似度，比较编辑区与未编辑区
- 关键对比（定性）：检测器主要依赖拼接边界伪影，context-aware神经编辑消除边界后此类性能显著退化

**是否开源**：本文无代码；所综述WeDefense、DeepFense为开源工具链，ICASSP 2027音频编辑challenge提供公开评测（https://audio-editing-challenge.github.io/）。

### ⭐ 评分：7/10
评分理由：多机构资深团队执笔，概念框架（fake的应用依赖判定、utility-consistency-accountability三元可信编辑准则）具有引领性，是首篇贯通生成与防御两侧的音频编辑综述，开放问题清单对细分领域路线图价值高。不足在于纯综述、无新方法，也未给出各方法/数据集的量化性能对照表，实证深度有限；实用价值取决于后续benchmark落地。

---

## [12] ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling

**arXiv ID**：2610.36126 | **方向**：语音前端

**作者**：Kehinde Elelu, Joshua E Siegel, Mohammadali Saffary, Tashfain Ahmed, Simeon Babatunde, Ebuka Okpala

**机构**：Michigan State University, Clemson University

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36126 | **PDF**：https://arxiv.org/pdf/2610.36126.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
TTS/VC质量评估依赖准确的MOS预测，但现有预测器大多只输出点估计、缺乏可靠的量化不确定性，限制了模型选择与实际部署的安全性。本文提出ConformalMOS：冻结预训练音频编码器作骨干，用高斯平滑标签的序数预测头给出MOS点估计，再经split conformal后验校准输出具有有限样本覆盖保证的预测区间。在BVCC上，M2D2骨干配合α=0.05取得系统级MSE 0.080（较FUSE-MOS降低7.0%）、LCC 0.953，且经验覆盖与名义目标紧密对齐，为可靠性感知的语音质量评估提供了理论有保证的方案。

### 🔧 技术方案

**问题背景：** 人评MOS本身具有主观性、听者偏差与声学条件波动，SOTA系统句级相关性也只是中等；UTMOS、FUSE-MOS等主要输出点估计，少数概率式方法虽建模不确定性，但均无法保证预测区间以受控概率覆盖真实MOS，在分布外语音上容易过度自信、不可信。

**模型架构：** 冻结上游编码器（M2D2或Wav2Vec2）抽取帧级嵌入Z∈R^{T×D}，经时序均值池化得固定维向量，输入轻量两层MLP预测头，输出[1,5]上K个等宽序数bin的类概率，按bin中心期望求和得标量MOS估计；推理后再由split conformal校准阶段基于校准集残差的单一标量半宽生成区间并裁剪至[1,5]。

**核心创新：** (1) 首次将无分布假设的split conformal预测引入MOS回归：取校准集绝对残差的(1−α)分位数为半宽q̂，在可交换性下保证P(Y∈I(X))≥1−α，与启发式不确定性有本质区别，后验完成且推理只需加减q̂，开销极小。(2) 序数感知标签：将one-hot换成对bin中心的高斯平滑软目标，以KL散度加辅助ℓ1损失训练，编码相邻分数的部分正确性，使目标与SRCC等排序型指标对齐。(3) 骨干无关的可靠性分析：同一框架对比M2D2与Wav2Vec2，证明基础预测器质量直接决定conformal校准的覆盖与区间锐度，为部署选型提供依据。

**训练策略：** BVCC按VoiceMOS标准划分：训练4,477条、校准497条（10%）、验证1,066条、测试1,066条；SGD（lr 1e-4、动量0.9、wd 1e-4），训练batch 32/验证测试batch 8，最长1000 epochs、早停patience 20，冻结骨干仅训练预测头，单张RTX A5000约2小时/run。

### 📊 实验结果
**数据集**：BVCC，7,106条英语合成语音样本，来自187个TTS/VC系统，多人评分标注

**主要指标**：
- 系统级（M2D2，α=0.05）：MSE 0.080、LCC 0.953、SRCC 0.943、KTAU 0.805（均为表内最优）
- 句级（M2D2，α=0.05）：MSE 0.228、LCC 0.878、SRCC 0.876、KTAU 0.698
- 关键对比：系统级MSE较FUSE-MOS（0.086）降0.006（7.0%）、较UTMOS（0.090）优势更明显；UTMOS句级MSE 0.165仍更好
- 校准：M2D2各α（0.01/0.05/0.1/0.2）下经验覆盖紧贴名义1−α、校准误差低；wav2vec在α=0.01覆盖不足且区间更宽（系统级MSE升至0.153）

**是否开源**：暂无（论文未提供代码链接）

### ⭐ 评分：6/10
评分理由：将conformal预测的形式化覆盖保证引入MOS估计，填补了不确定性感知评估"无统计保证"的空档，思路干净、即插即用且开销小，对TTS/VC部署的模型选择有实际价值。但方法上主要是现有技术的组合，属增量式创新；评测仅限域内BVCC，句级精度不及UTMOS，覆盖/校准误差/区间宽度等关键校准指标只有定性展示而缺乏数值表，实验说服力有限。

---

## [13] Physiology-Informed Audio Quality and Listening Effort Estimation

**arXiv ID**：2610.36865 | **方向**：语音前端

**作者**：Niall McGuire, Dimitra Emmanouilidou

**机构**：University of Strathclyde（英国格拉斯哥）；Microsoft Research（美国雷德蒙德）

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36865 | **PDF**：https://arxiv.org/pdf/2610.36865.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
传统MOS主观评测慢、贵且只能在播放后收集，现有ML预测方法又只输出人群平均分，丢失个体感知差异；已有生理研究依赖实验室级设备。本文对30名听者同步记录32通道实验室EEG与消费级可穿戴设备（Muse Athena的4通道EEG+fNIRS、Pupil Labs Neon眼动），从生理信号解码音频质量与聆听努力。结果表明可穿戴/光学信号可显著解码质量（AQ-2二分类LOSO平衡准确率0.60–0.65，AQ-5与语料MOS相关r达0.36–0.38），且校正到个体后可追踪其努力评分（眼动r=0.37），指向同时以感知质量和处理努力调优音频系统的可能。

### 🔧 技术方案

**问题背景：** MOS依赖大面板、播放后收集且无法支持自动化自适应评测；参考/无参考客观指标仍预测单一人群均值。既有生理-质量研究全部基于高通道湿电极实验室设备，消费级干电极设备能否解码质量、质量与努力能否同时解码均未知。

**模型架构：** 非深度模型，而是"多模态生理特征+传统分类/回归解码器"管线：四类流（LabEEG 32ch@256Hz、Muse EEG 4ch@256Hz、fNIRS 4对光源@64Hz、眼动200Hz）经LSL同步；EEG提取各通道delta至gamma带功率、谱熵、峰频与OAS收缩协方差；fNIRS提取幅值、斜率、AUC、达峰时间；眼动提取瞳孔直径幅度/斜率/达峰与注视速度、离散度、路径长度。任务四组：AQ-2/AQ-5（干净vs退化二分类、回归5点语料MOS）与EF-2/EF-5（低/高努力、回归5点努力评分）。

**核心创新：** (1) 首次在相同听者上同时对比实验室级与消费级传感：Muse EEG+fNIRS与Pupil Labs Neon眼动均显著解码质量（AQ-2 LOSO 0.60–0.65，Holm校正p<.001），而32通道实验室EEG未超机会（0.51），凸显干电极可穿戴设备的实用性。(2) 质量与努力联合处理：区分LOSO（未见听者）与within-subject（个体校正）两种外层验证，揭示努力仅在个体校正后可解码、跨听者不泛化。(3) 监督标签对比分析：以客观MOS训练全面优于主观评分训练（pooled r从约0.17升至0.41–0.43），但证明这是对组均值的"收缩"而非去噪——个体内排序恶化（rank r从约0.79跌至0.12–0.33），划出生理解码的适用边界。

**训练策略：** 二分类最小化BCE、回归最小化MSE；每个外层训练折内以3折听者分组交叉验证从SVM、elastic-net、XGBoost、MLP、CatBoost选模型与超参（回归加PLS），外层测试折不参与选择；信号经2秒刺激前基线校正；显著性用听者级bootstrap 5万次并在任务内做Holm校正。

### 📊 实验结果
**数据集**：自行采集，30名听者，144条约10±2s音频（102条语音取自NISQA退化语料、42条音乐取自ODAQ），覆盖编解码/加性噪声/混响/丢包四类退化。

**主要指标**：
- 行为验证：主观质量评分与语料MOS相关r=0.75，努力评分与质量负相关r=−0.57
- AQ-2平衡准确率（机会0.5，Full/LOSO）：Muse EEG 0.64±.12、fNIRS 0.60±.09、Eye 0.65±.17、Lab EEG 0.51±.09
- AQ-5皮尔逊r（Full/LOSO）：Muse EEG 0.38±.14、fNIRS 0.36±.11；WS升至0.41–0.43
- EF-5仅个体内显著：Eye WS r=0.37±.03（RMSE 0.89）；LOSO下仅fNIRS在EF-2达显著（0.52±.04）
- 语音vs音乐（AQ-2）：0.69–0.83对比0.38–0.62，质量信号主要由语音承载

**是否开源**：论文正文未给出代码/数据仓库或Demo链接，暂无

### ⭐ 评分：6/10
评分理由：一项诚实的可行性研究：同听者四设备同步对比、质量+努力双任务线，并主动暴露客观标签训练的收缩效应与跨听者不泛化，结论克制。创新在实验与验证设计而非建模（均传统ML+手工特征）。短板是效应幅度适中（最高r≈0.43）、模态对比受队列与trial数不平衡混淆、未做leave-one-clip-out排除刺激记忆，距离替代DNSMOS类客观指标仍有差距。

---

## [14] Perceptual Differences and Preferences in Speech Enhancement

**arXiv ID**：2610.36892 | **方向**：语音前端

**作者**：Simon Dahl Jepsen, Jesper Rindom Jensen

**机构**：Audio Analysis Lab, Dept. of Electronic Systems, Aalborg University（丹麦奥尔堡大学）

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36892 | **PDF**：https://arxiv.org/pdf/2610.36892.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有语音增强（SE）评估依赖有/无参考客观指标和类别制主观测试，均只测质量与可懂度，无法回答"监听者是否感知到差异、是否形成系统性偏好"。本文将可分辨性（discriminability）与偏好（preference）引入SE评估作为互补维度：借鉴感官科学的ISO 4120三角判别测试与带"无偏好"项的A/B/N成对偏好测试，对MP-SENet、MambAttention、MeanFlowSE、StoRM四个系统及其与干净语音的配对，开展92人众测。结果显示总体判别正确率约0.70（显著高于1/3随机率），判别率与决策度在系统对与语句间大幅波动；客观指标与之相关性参差，PESQ与判别相关性仅0.05。

### 🔧 技术方案

**问题背景：** 高性能SE系统在基准上的得分差日益缩小，而得分分离不等于可感知差异，更不等于监听者偏好；URGENT挑战赛已暴露客观与主观评估的不一致。评分制范式无法直接量化"能否分辨"与"偏好哪方"。

**模型架构：** 不训练网络，核心是成对比较统计框架：逐语句计算指标差Δm与绝对差D。(1)三角测试：同语句三样本（两同一异、6种排列随机），听者找出"不同者"，响应建模为Bernoulli/Binomial，用单侧精确二项检验对照1/3随机率，判别率经含机会渐近线的心理测量函数P=1/3+(2/3)σ(α+βD)最大似然拟合；(2)偏好测试：A/B/N三选，定义决策度(N_A+N_B)/总数与带符号偏好方向Ŝ，用2σ(α+βΔm)−1双向logistic建模。

**核心创新：** (1) 将感官科学ISO 4120三角判别测试引入SE评估：直接回答"两个增强输出是否可被听出差别"，并把1/3随机率作为显式机会下界嵌入心理测量模型。(2) 带"无偏好"选项的A/B/N配对范式：区别于ISO 5495的强制A/B，把"感知相似"与"真正分歧"分开，量化决策度与偏好方向两个维度。(3) 语句级成对分析：首次系统考察客观指标差与可分辨性/偏好的SRCC关联，揭示语料级均值会掩盖个体信号上的重要感知差异。

**训练策略：** 无模型训练。四个被评系统均用VoiceBank+DEMAND训练的官方公开checkpoint；DNS2020测试集45条语句截断至4秒并响度归一化；不完全配对设计组成10个系统对，每语句评3对；每位被试在判别与偏好两BLOCK各完成30次试验，92名无听力障碍被试通过耳机筛查，参数由最大似然估计，95%CI用语句bootstrap。

### 📊 实验结果
**数据集**：VoiceBank+DEMAND（各系统训练集）；DNS2020测试集45条语句（4秒截断、响度归一化）

**主要指标**：
- 总体三角判别正确率：0.70（1775/2541，显著高于1/3随机率）
- 系统对平均判别率：StoRM vs干净最高0.83，MambAttention vs MeanFlow最低0.56；语句级跨0.34–1.0大幅波动
- 决策度：总体68%表示偏好；MeanFlow vs干净0.84最高，MeanFlow vs StoRM 0.51最低
- 指标差与判别的SRCC：SQUIM-STOI 0.62、ScoreQ 0.59；PESQ仅0.05、SI-SDR 0.17、DNSMOS-OVRL 0.29
- 偏好方向：MP/MF/Sto相对MambAttention与干净参考均处劣势，MambAttention与干净语音平均获得同等偏好

**是否开源**：承诺公开web听测框架与实验材料（"Code published upon acceptance"），当前未给出仓库链接；被测四系统各自开源。

### ⭐ 评分：6/10
评分理由：视角新颖，把感官科学的三角测试与A/B/N偏好范式引入SE评估，直击"得分差≠可感知差≠偏好差"的盲区，PESQ对判别近零相关等发现对基准选型有直接参考价值。但规模较小（45语句、92人），众听测的设备与注意力噪声未受控，不完全配对设计削弱系统对间可比性。属方法学探索与方向性结论而非可落地新指标，为稳健的增量贡献。

---

## [15] A Lightweight Dual-Branch Visual Front-End for Efficient Audio-Visual Target Speaker Extraction

**arXiv ID**：2610.36834 | **方向**：语音前端

**作者**：Zhan Jin, Peijun Yang, Juan Liu, Ming Li

**机构**：武汉大学、香港中文大学（深圳）

**发布日期**：2026-10-28 | **论文**：https://arxiv.org/abs/2610.36834 | **PDF**：https://arxiv.org/pdf/2610.36834.pdf | **代码**：暂无 | **Demo**：https://anonymous.4open.science/r/Lightweight-Visual-Frontend-E46E

### 📌 简介
针对AVTSE系统中卷积视觉前端计算占比随分离主干轻量化而失衡的问题（ResNet18级88×88 ROI编码达8.0 GMACs，与IIANet主干17.1 GMACs同量级），本文提出双分支视觉前端：用32×32紧凑唇部ROI经轻量ResNet式卷积建模局部发音细节，用84点面部landmark坐标经V-TCN建模全局几何运动，以极低开销融合后接入IIANet与SpatialNet。在LRS3-2mix统一精简训练协议下，视觉编码计算从8.0降至0.3 GMACs（降幅超90%），性能与轻量基线BlazeNet64持平（SI-SNRi 17.1 dB、PESQ 2.80），与ResNet18相比仅差约0.4 dB。

### 🔧 技术方案

**问题背景：** 现有AVTSE视觉前端普遍采用ResNet18类对88×88面部ROI稠密卷积的范式，当分离主干日趋轻量化时，视觉端计算占比不断上升，成为低功耗部署瓶颈；已有轻量方案仍停留在图像卷积内部压缩，未改变表征策略本身。

**模型架构：** 双分支各输出64通道特征。唇分支以唇部轮廓landmark均值为中心从96×96嘴部patch裁出局部窗、训练random crop至32×32，经Conv3D+BN+ReLU短时空建模，后接2D残差块堆叠、空间池化与时序投影；landmark分支输入SADRNet的84点二维坐标（标准68点外加鼻-上唇与口角-下颌各8点），z-score归一化后V-TCN块建模时序动态。融合：IIANet中两路concat经单层1D卷积投影回64维；SpatialNet中两路对齐至129维频率维后与复数谱沿新增视觉维concat，主干结构均不改动。

**核心创新：** (1) 注意力可视化引导的表征分配策略：插入MHSA探针发现内唇响应高度集中而外围稀疏，据此将局部外观交给小ROI卷积、外围几何运动交给低维landmark坐标，从输入表征侧削减稠密卷积量级。(2) 84点扩展landmark模板与双分支互补设计：消融显示全方案在IIANet（tol=3档）达16.0 dB，显著优于ROI-only的14.9 dB与lmk84-only的15.3 dB。(3) 骨干无关的即插即用融合：在跨模态注意力（IIANet）与TF域条件注入（SpatialNet）两类主干上仅以0.3-0.5 GMACs融合开销完成替换。

**训练策略：** 损失为SI-SDR主项加λ·‖αŝ−s‖₁尺度辅助项；Adam，lr 0.001，停滞减半并早停；8×V100，batch 3；增强为随机32×32裁剪与水平翻转（landmark同步镜像），LRS3-2mix（CTCNet协议）50000/5000/3000划分，tolerance/early-stop两种缩减调度（5/15与3/10）下同组方法条件完全一致。

### 📊 实验结果
**数据集**：LRS3-2mix（CTCNet协议：2秒双人16 kHz、SIR −5至5 dB，25 FPS 224×224人脸视频）

**主要指标**：
- IIANet（tol=5/ES=15）：本方法SI-SNRi 17.1 dB、PESQ 2.80、视觉编码0.3 GMACs；BlazeNet64为17.0/2.80/2.4；ResNet18为17.5/2.90/8.0（骨干均17.1）
- IIANet（tol=3/ES=10）：本方法16.0/2.59 vs ResNet18 16.2/2.64、BlazeNet64 16.0/2.58
- SpatialNet（tol=3/ES=10）：本方法15.5/2.81/0.5 vs BlazeNet64 15.5/2.77/2.9、ResNet18 15.6/2.79/8.0
- 消融（IIANet，tol=3）：ROI-only 14.9、lmk84-only 15.3、lmk68-only 15.2、全方案16.0 dB
- 口径说明：GMACs为模块级视觉编码量，不含人脸检测与landmark估计（SADRNet单帧10.4 GMACs，视为已有预处理）

**是否开源**：仅提供匿名Demo音频页，代码未见正式开源。

### ⭐ 评分：5/10
评分理由：贡献在于系统化验证了"小ROI图像+扩展landmark"这一表征层权衡，统一缩减协议、固定对照与消融设计严谨，结论清醒不夸大，对低功耗AVTSE部署有直接参考价值。但方法本质是既有组件的组合与ROI收缩，创新增量有限；仅单数据集、无多seed、无端到端延迟实测，且把landmark估计排除在计算口径外削弱了"轻量"主张的完整性，与BlazeNet64的差距也未拉开。属有参考价值的扎实增量工作。

*Subagents used for reading: 15* | Generated on 2026-10-28 语音论文批次, by Kimmy's research agent | Powered by VAgent SpeechAI Researcher
