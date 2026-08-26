# 2026-08-25 语音论文速递

**共收录**: 14 篇 | **语音大模型**: 10 篇 | **语音前端**: 4 篇

> 目标日期 2026-08-25（北京时间）arXiv 语音相关论文共命中 14 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] DiaScriber: A Speech LLM for Joint Diarization and Transcription in Multi-Speaker Scenarios

**arXiv ID**：2608.22796 | **方向**：语音大模型

**作者**：Bingshen Mu, Xian Shi, Xiong Wang, Zhifang Guo, Ting He, Xize Cheng, Yu Xi, Jin Xu, Lei Xie

**机构**：西北工业大学计算机学院语音与音频信号处理实验室（ASLP@NPU）

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.22796 | **PDF**：https://arxiv.org/pdf/2608.22796 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
多说话人场景下"谁在何时说了什么"（MSASR）仍受快速话轮切换、重叠语音与场景多样性的困扰。本文提出 DiaScriber，基于预训练 Qwen3.5-Omni 的端到端多说话人分离与转写模型，通过验证精修、仿真与多模态标注三条数据流水线构建大规模训练语料，并采用持续预训练（CPT）、有监督微调（SFT）与强化学习（RL）三阶段训练策略。在 AliMeeting、AISHELL-4、AMI 等公开集与8个内部测试集上，DiaScriber 平均 DER 5.4%、cpWER 11.8%、tcpWER 12.6%，大幅优于 VibeVoice-ASR（26.1/28.9/39.1）与 MOSS-Transcribe-Diarize（18.6/23.3/30.4），并在未见场景中展现出出色泛化能力。

### 🔧 技术方案

**问题背景：** 传统级联式 MSASR 将说话人分离、切分与 ASR 各自独立优化，无法建模说话人身份、时间戳与内容的相互依赖，且上游错误逐级传播，在重叠语音与频繁说话人切换时误差累积严重，还需复杂后处理与启发式规则合并各模块输出。半级联方法（如 DM-ASR）仍依赖前置模块结果，无法克服误差传播。现有端到端方法中，SoulX-Transcriber 仅支持不超过10分钟的输入，VibeVoice-ASR 与 MOSS-Transcribe-Diarize 可处理超一小时语音但在复杂多样场景下稳定性不足。

**模型架构：** DiaScriber 由语音编码器（AuT）、线性投影层与 LLM 后端组成。AuT 基于 Qwen3-ASR 4000万小时语音-文本对训练，参数量600M，Fbank 特征经4个 Conv2D 块下采样16倍后经自注意力得到 6.25Hz 低帧率语音嵌入以支持长时输入，训练中采用1s-8s 的 flash attention 窗口；LLM 后端为 23B 参数 MoE 架构（2.6B 激活参数）。输出序列格式为 <soc><sos><start_time>转写文本<end_time><spkid><eos>...<eoc>，以特殊 token 编码话轮起止、时间戳与说话人 ID。

**核心创新：** (1) 验证与精修流水线：用 Qwen3-ASR-Flash 抽取段首段中段尾并计算 WER 与边界连续错误率（BCER）检验时间戳质量，通过说话人相似度检验身份标注，对低质时间戳仅重写段边界转写、对低质身份标注按段重聚类修复。(2) 仿真流水线：合成-拼接用 Qwen3-TTS 参考语音克隆扩展多目标说话人话语后随机排序与间隔拼接成长语音并加噪加混响；裁剪-平移通过平移相邻说话人片段制造两说话人乃至三说话人以上重叠语音。(3) 多模态标注流水线：对真实视频组合 VAD、pyannote 说话人分离与多 ASR ROVER 融合得到初步标注，结合人脸轨迹聚类与 SyncNet 视听一致性校正说话人身份，再由 Gemini-3.1-pro-preview 生成结构化标注，覆盖访谈、影视等场景。

**训练策略：** 三阶段训练：(1) CPT 阶段用85000小时多场景语料以 teacher forcing 负对数似然损失适配 MSASR 任务与输出格式；(2) SFT 阶段用约4600小时精选数据强化格式稳定性；(3) RL 阶段采用组序列策略优化（GSPO），以 DER、cpWER、tcpWER 三者加权组合构建复合奖励，用1000条未见多说话人长语音训练。

### 📊 实验结果
**数据集**：AliMeeting、AISHELL-4、MagicData-RAMC、AMI、MLCSLM-EN，以及8个内部测试集（5个为 OOD 场景）

**主要指标**：
- AliMeeting：DER 3.6%，cpWER 12.0%，tcpWER 12.4%（MOSS 为 4.1/16.2/16.3）
- AMI：DER 5.5%，cpWER 10.3%，tcpWER 10.8%（MOSS 24.0/17.7/20.4）
- 全部测试集平均：DER 5.4%，cpWER 11.8%，tcpWER 12.6%（VibeVoice 26.1/28.9/39.1）
- OOD 内部重叠对话集：DER 1.3%，cpWER 2.2%，tcpWER 2.3%
- 阶段消融：CPT 8.2/18.1/19.3 → SFT 5.5/14.4/14.8 → RL 4.8/13.8/14.4

**是否开源**：暂未开源（未提供代码、模型与数据链接）

### ⭐ 评分：8/10
评分理由：构建了验证精修、仿真、多模态标注三条系统化数据流水线，并首次在 Qwen3.5-Omni 上以 CPT+SFT+RL 三阶段训练端到端 MSASR，工程价值高且数据方案可复用。实验覆盖5个公开集与8个内部集（含OOD场景），并做了训练阶段与奖励消融，充分性较好。扣分点在于代码与模型未开源、内部测试集不可公开访问，部分指标（AISHELL-4、MagicData）低于 MOSS 表明优势并非全面。

---

## [2] Unsupervised Speech Recognition at the Syllable Level

**arXiv ID**：2608.22907 | **方向**：语音大模型

**作者**：Liming Wang, Kai-Wei Chang, Kunio Kashino, David Harwath, Mark Hasegawa-Johnson, James R. Glass

**机构**：MIT CSAIL、NTT、德克萨斯大学奥斯汀分校、伊利诺伊大学厄巴纳-香槟分校

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.22907 | **PDF**：https://arxiv.org/pdf/2608.22907 | **代码**：https://github.com/cactuswiththoughts/SylCipher | **Demo**：暂无

### 📌 简介
本文提出 SylCipher，首个基于掩码语言建模的音节级无监督语音识别（UASR）系统，无需G2P与对抗训练。在 LibriSpeech 干净子集上，SylCipher 较无G2P基线 wav2vec-U（35.6%/43.3%）实现最高 40% 的字符错误率（CER）相对下降（达成 21.8%/35.9%，自训练后 17.5%/33.3%）；在 Mandarin AISHELL-3 上取得 12.2% 的 Phone Error Rate（PER），而 GAN 基线无法收敛；在多语言 LibriSpeech 与低资源粤语、台语上也一致超越音素级方案。实验贯穿匹配/非匹配分布、跨语言与极低资源场景，均验证音节单位的优越性。

### 🔧 技术方案

**问题背景：** 现有主流 UASR 均在音素级建模，依赖 G2P 将文本转音素，而许多语言书写系统缺失关键音信息或缺乏发音词典；在强协同发音语言（如 Mandarin）中音素边界难以检测。GAN 式对抗训练（wav2vec-U）存在训练不稳定、容易发散问题。词级方案虽免 G2P，但稀有词词汇量近乎无限，且长程上下文使分词机制不稳定。音节数量有限、与语音文本天然对齐，是更优的对齐单位。

**模型架构：** SylCipher 为共享编码器的 encoder-only 语言模型。语音侧经"语音音节器"（Sylber 初始化的边界检测器 + clamp 稀疏软池化 + 可微 K-means 向量量化器）转为音节级离散单元；文本侧用 Pyphen+ 无 G2P 音节化（top-2048 音节）。两端通过线性 pre-net 映射到同一 768 维空间，送入 2 层 Transformer 共享编码器（768 维、12 头），再经线性 softmax post-net 输出。

**核心创新：** (1) 信息约束掩码语言建模：用 wMLM（泊松 span 掩码，均值 3.5、掩码预算<30%）最小化语音与文本单模态分布的 KL 散度，辅以浅层共享编码器、Gumbel-Softmax 乘积量化器与随机 mix-up 限制表征容量，防止模态漂移。(2) 联合端到端（JE2E）音节边界精调：软池化可微，使边界检测器随文本分布匹配信号更新，并以软音节数约束抑制过/欠切分。(3) 分阶段 PUSM 训练：wMLM 饱和后加入位置单/双元组分布匹配进行显式对齐，三段迭代式训练保障稳定。

**训练策略：** 总损失 L=λ1·L_wMLM+λ2·L_JE2E+λ3·L_PUSM。Adam 优化器，lr 2e-4，多项式衰减、150 步预热；英语用 HuBERT-Large（LibriLight 60k 小时），其余语言用 XEUS；自训练阶段用 wav2vec2.0 学生模型 + CTC + 单向 Bi-LSTM，lr 1e-4。

### 📊 实验结果
**数据集**：LibriSpeech（460h）、SpokenCOCO（742h）、AISHELL-3（85h）、多语言 LibriSpeech（德/荷/法）、MDCC（粤语）、SuiSiann（台语）

**主要指标**：
- LibriSpeech CER：SylCipher 21.8%/35.9%，自训练后 17.5%/33.3%，较 wav2vec-U 相对降低 40%/17%
- AISHELL-3 PER：12.2%（GAN 基线 wav2vec-U 为 74.9 且不稳定）
- MLS CER：德 32.3、荷 35.6、法 41.7，较单语无G2P基线相对提升 25-50%
- 低资源语言 PER：粤语 35.0、台语 35.5（自训练后 23.5/26.5），显著优于 wav2vec-U（75.7/69.0）
- 与音节级 GAN 对比：SylCipher SER 25.5，GAN 达 115.7-126.5

**是否开源**：开源，https://github.com/cactuswiththoughts/SylCipher

### ⭐ 评分：8/10
评分理由：首次将 UASR 系统化地推进到音节级，以信息受限的 MLM 框架统一边界检测、量化与跨模态对齐，创新性突出且给出了理论保证与完整消融；实验覆盖匹配/非匹配、多语言、半监督与极低资源多场景，多个结果显著优于现有方法。扣分点在于各语言仍依赖人工/规则音节化方案，非语言通用，且共享编码器规模较小。整体为顶会水准的实质贡献。

---

## [3] WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs

**arXiv ID**：2608.22704 | **方向**：语音大模型

**作者**：Yiming Yao, Chenyang Lyu, Xuanfan Ni, Longyue Wang, Weihua Luo, Yazheng Yang, Jinsong Su

**机构**：阿里巴巴集团、厦门大学信息学院、厦门大学闽台非物质文化遗产数字化保护与智能处理文旅部重点实验室

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.22704 | **PDF**：https://arxiv.org/pdf/2608.22704 | **代码**：https://github.com/XMUDeepLIT/WnW | **Demo**：暂无

### 📌 简介
长音频输入的语音LLM其推理瓶颈由模型参数转移到KV缓存（10分钟音频即占7500-15000个KV位置）。现有prefill-only压缩方法在长音频上失效：prefill注意力集中于音频开头（attention-sink），而decode注意力分布均匀。本文提出WnW，通过离线校准将KV头分类为anchor/tidal/fixed三类，解码期以anchor头注意力作为重要性观测信号，将tidal头的音频KV按chunk从CPU按需召回，实现可恢复的KV管理。在两个3B骨干（Voxtral-mini-3b与Qwen2.5-Omni-3B）的LibriSpeech-Long上，仅保留20%音频token于GPU时距Full Cache约1.6 WER以内，而此时prefill-only基线彻底无法终止生成。

### 🔧 技术方案

**问题背景：** 现有H2O、SnapKV、Ada-KV、AudioKV等方法均在prefill阶段利用提示注意力一次性打分并固定保留集，其核心假设"prefill注意力能预测decode期注意力"在长音频上不成立。论文实测prefill注意力呈attention-sink分布（前10%位置占47.9%质量），而decode累积注意力近乎均匀（前10%仅9.8%）；240个KV头逐头Jaccard（K=100）在0.006-0.641间。一旦prefill期将位置永久丢弃、无恢复通道，压缩方法就结构性受损。

**模型架构：** 主骨干为Voxtral-mini-3b-2507（L=30、Hq=32、Hkv=8、GQA组g=4、12.5音频token/秒）和Qwen2.5-Omni-3B（L=36、Hq=16、Hkv=2、g=8、25 token/秒），另在Voxtral-Small-24B上验证扩展性，全部使用bf16权重与贪心解码。

**核心创新：** (1) 三类KV头离线校准（anchor/tidal/fixed）：以语音接地比（VS，top注意力落在词对齐时间窗内的比例）与梯度敏感度（HS）之积VS×HS排序，top5为anchor头全量保留充当解码期观测器，其余voice头为tidal头（GPU部分+CPU可召回副本），剩下为fixed头（仅静态保留prefill top-k）。(2) 偏置校准式预算分配：retention_i=min(s̃_i·λ,1)，仅作用于音频KV，λ控制GPU驻留比例。(3) 解码期chunk交换召回：音频位置划分为4秒（步长2秒）重叠chunk，每步聚合5个anchor Q头的softmax注意力为逐位置分数，top-k（k=3）chunk自CPU召回，连续3步未命中者释放GPU但保留CPU副本。

**训练策略：** 该方法不训练模型，仅需离线校准：用50条LibriSpeech-Long dev-clean样本计算各头VS与HS分数，λ在标定集上调节以匹配目标GPU保留率（0.2/0.4/0.6/0.8），指标为截断WER与sacreBLEU。

### 📊 实验结果
**数据集**：LibriSpeech-Long（test-clean 270条/test-other 207条）、LongSpeech（asr-fr、en2fr）、PriMock57（57条门诊对话）

**主要指标**：
- Voxtral-mini-3b，r_GPU=20%：WER 6.23/8.87（Full Cache 6.79/8.86）
- Qwen2.5-Omni-3B，r_GPU=20%：WER 15.31/18.42（Full Cache 13.87/16.80）
- 同预算基线（r_GPU=20%）：Ada-KV 199.24、AudioKV 192.58（均不终止）、ArkVale 11.74
- 泛化性：asr-fr WER 22.68（Full 20.42）、en2fr BLEU 38.21、PriMock57 WER 24.23
- 24B扩展：WnW 11.29/16.63，ArkVale 15.60/22.20

**是否开源**：代码与实验脚本将发布至 https://github.com/XMUDeepLIT/WnW（截至发布尚未放出）

### ⭐ 评分：8/10
评分理由：首次系统量化语音LLM长音频上prefill-decode注意力错配问题，证据扎实；anchor/tidal/fixed三类头离线校准与解码期CPU召回机制兼具理论动机与工程实用性，在0.2保留率下仍优于可召回基线ArkVale近5.5 WER。实验覆盖双语种/跨任务/跨领域与24B扩展，消融充分。扣分点在于AudioKV实现细节差异可能影响公平对比，且模型/数据仅提供计划。

---

## [4] MetaSICL: Globalizing Auditory LLMs for Underserved Speakers and Languages via Meta Speech In-Context Learning

**arXiv ID**：2601.18904 | **方向**：语音大模型

**作者**：Haolong Zheng, Siyin Wang, Zengrui Jin, Mark Hasegawa-Johnson

**机构**：伊利诺伊大学厄巴纳-香槟分校（UIUC）、清华大学

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2601.18904 | **PDF**：https://arxiv.org/pdf/2601.18904 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
听觉大语言模型多在高资源英语成人数据上训练，对儿童语音、语音翻译方向及文化性音频理解等低资源场景表现差，直接微调在分布偏移下易过拟合甚至退化。作者提出MetaSICL后训练配方，仅用充沛的高资源ASR+ST数据以上下文学习（ICL）格式构建episode，教会模型"如何使用演示"做测试时适配。在两个backbone（MiMo-Audio与Qwen2.5-Omni）上，MetaSICL相比vanilla SICL与零样本在儿童ASR、音频理解/推理、多语ASR和语音翻译上全面提升；在低资源语言ASR上，以MetaSICL为warmup的域内SICL GRPO使Swahili CER从52.9降至25.6，全部优于直接微调。

### 🔧 技术方案

**问题背景：** 全球化生成式AI要求听觉LLM适配低资源用户、语言、方言与年龄组，但现有模型被成人英语等高资源数据主导。多数目标社区在训练数据中覆盖不足，而收集标注充分的域内语料成本高、难以代表真实测试分布，直接监督微调会过拟合到数据集特有伪影。文本领域MetaICL等已证明元训练可增强ICL能力，但该范式是否适用于听觉LLM仍属空白。

**模型架构：** 采用Qwen2.5-Omni与MiMo-Audio两个开放听觉LLM backbone，在语言backbone中插入轻量LoRA适配器（rank 88、alpha=32），其余参数冻结，属参数高效后训练。

**核心创新：** (1) 元语音上下文学习（MetaSICL）训练配方：每步采样一个query实例并从演示池检索k个演示拼接成prompt，训练目标为最大化P(y_query|x1,y1,…,xk,yk,x_query)，学习依赖演示生成query输出的能力。(2) 仅用高资源离域数据激活ICL能力：后训练仅用CommonVoice英语子集与CoVoST2多语子集，演示经TICL文本嵌入KNN检索，未见目标域却跨域、跨语言、跨任务改善。(3) MetaSICL→域内SICL GRPO的warmup范式：当可收集少量域内数据时，以其作为GRPO初始化，比直接从基座跑SICL GRPO更稳定。

**训练策略：** 采用ICL格式episode的交叉熵损失。训练任务组成经消融确认为ASR++ST默认配方：纯ASR虽ASR最优但使ST崩塌，++SQA（加语音问答）AU/AR最优但轻微损害ASR/ST。推理时few-shot演示数k=3。

### 📊 实验结果
**数据集**：MyST、RSR（儿童ASR）、MMAU/MMAR（音频理解与推理）、FLEURS（五种类型学多样低资源语言ASR）

**主要指标**：
- 儿童ASR WER（Qwen2.5-Omni）：MyST 22.72→17.03（MetaSICL）；RSR 27.86→21.95
- 音频理解准确率：MMAU 65.80%→71.10%，MMAR 49.20%→54.40%
- 语音翻译 BLEU：en→ja 33.53→35.72，ja→en 16.24→18.15
- 低资源语言ASR CER（FLEURS 3-shot）：Swahili 47.7→25.6，平均73.4→60.4，优于直接SFT

**是否开源**：暂未开源（未提供代码/模型/数据链接，伦理声明仅承诺发布时排除可识别参与者信息）

### ⭐ 评分：8/10
评分理由：首次将元ICL后训练系统性地应用于听觉LLM全过程（高资源元训练+推理时演示适配+域内RL warmup），落在低资源全球化的现实痛点上，且用双backbone、held-out语言与五种类型学多样语言验证泛化性。扣分点在于未公开训练超参数细节与代码链接，影响可复现性；方法更多是对MetaICL/SMILE在多模态大模型上的迁移深化。

---

## [5] MRMAD: A Multi-Round Multi-Audio Benchmark for Evaluating Acoustic Degradation Perception in Large Audio-Language Models

**arXiv ID**：2608.22236 | **方向**：语音大模型

**作者**：Yize Li, Ningyuan Yang, Sile Yin, Sindhuja Thogarrati, Sung-En Chang, Andrew C. Singer, Xue Lin, Chuan-Che Huang, Shuo Zhang

**机构**：Northeastern University, Bose Corporation, Stony Brook University

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.22236 | **PDF**：https://arxiv.org/pdf/2608.22236 | **代码**：https://github.com/Bose/MRMAD | **Demo**：暂无

### 📌 简介
MRMAD 是首个面向大音频语言模型（LALM）的多轮多音频声学退化感知评测基准，覆盖语音、音乐、声音三类域与九种常见退化类型，基于 8400 道多选题构建退化类型识别（DTI）、严重度比较（DSC）与排序（DSR）三大任务。针对现有基准过度聚焦语义理解而忽视低层音质判断的缺陷，采用"每轮一个音频对应一段提示"的多轮对话形式评测跨轮次比较与推理能力。对 18 个代表性LALM的系统评测显示：Gemini 3.1 Pro 最优（DTI 86.22%、DSC 90.81%），最佳开源模型 Qwen3-Omni-Thinking 在 DTI 仅达 36.58%，揭示了当前模型"能听内容、不会辨退化"的显著短板。该论文已被 EMNLP 2026 接收。

### 🔧 技术方案

**问题背景：** 现有基准（AIR-Bench、AudioBench、MMAU等）主要评测语义理解、事件识别与高层推理；QualiSpeech 虽接近低层感知但仅限语音且为单音频。真实音频常受背景噪声、混响、编码压缩等退化影响，判断退化是评估音质与决定恢复/增强的前提。多音频比较若拼接为单输入会引入时序定位这一混淆因素，故采用多轮多音频会话格式：每轮提供一段音频与对应文本提示，通过对话上下文完成比较。

**模型架构：** 核心结构为三任务：DTI 两轮（首轮干净参考、次轮strong级退化音频，干扰项从感知组外采样）；DSC 两轮（audible 与 strong 两版本对比）；DSR 三轮（audible/medium/strong 三版本排序，含正确、相邻交换、较易干扰共四个选项）。数据源含 VCTK/LJSpeech/HiFi-TTS/LibriSpeech（语音5400条）、URMP/MUSDB18-HQ/FMA-small（音乐4800条）、FSD50K/TAU Urban 2019（声音4200条），全部单声道16kHz。

**核心创新：** (1) 首个多轮多音频低层音质感知基准：以轮次对话整合跨音频证据，规避拼接输入的时序定位混淆。(2) 控制化数据构建：按域定制退化覆盖（语音9类、音乐8类、声音7类），三档严重度调节，感知分组干扰项采样与平衡配额保证可区分性。(3) 诊断式失败分析框架：通过替换/删除参考音频、单轮对照、音频token余弦相似度三类受控实验定位失败模式。

**训练策略：** 本工作为评测基准，不涉及模型训练。平均音频长度9.1秒、平均问题长度73.8词，问题采用多套模板随机采样并强制仅输出字母选项，降低提示偏见。

### 📊 实验结果
**数据集**：MRMAD（8400题），对照 AIR-Bench、QualiSpeech、MMAU 等

**主要指标**：
- DTI：Gemini 3.1 Pro 86.22%；最佳开源 Qwen3-Omni-Thinking 36.58%，其余开源普遍贴近25%随机基线
- DSC：Gemini 3.1 Pro 90.81%；Qwen3-Omni-Thinking 60.70%
- DSR：Gemini 3.1 Pro 64.25%；最佳开源 Qwen2.5-Omni 33.58%
- 失败诊断：多数模型在参考音频被替换/删除时性能几乎不降；SALMONN 音频token对退化近乎不变

**是否开源**：已开源（代码与数据集 https://github.com/Bose/MRMAD）

### ⭐ 评分：8/10
评分理由：首次系统化开辟 LALM 低层退化感知这一被忽视的评测维度，任务与数据设计严谨（多轮多音频格式、感知分组干扰项、跨域多层退化控制），对不同失败模式给出诊断级分析，实验充分。扣分点在于其定位仅为评测基准、未提出改进方案，且缺乏人类专家性能对照。

---

## [6] Reasoning-Oriented Post-Training and Inference-Time LoRA Rescaling for Audio-Dependent Question Answering

**arXiv ID**：2608.23092 | **方向**：语音大模型

**作者**：Weiteng Hu, Yin Cao, Jun Yang

**机构**：中国科学院声学研究所、中国科学院大学

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.23092 | **PDF**：https://arxiv.org/pdf/2608.23092 | **代码**：https://github.com/WeitengHu/DCASE2026-Task5 | **Demo**：暂无

### 📌 简介
针对 DCASE 2026 Task 5 ADQA 任务，本文提出结构化思维链（Structured CoT）后训练框架与推理时 LoRA 缩放机制，并在 Qwen2.5-Omni 与 MOSS-Audio-8B-Thinking 两个骨干上系统分析适配行为。Qwen 系统经 SFT+GRPO/GDPO 后 top-1 从基线 54.39% 提升至 58.93%，推理时将 LoRA 缩放因子降至 γ=2 进一步达到 61.05%；MOSS 零样本达 67.70% 但 SFT 反而降至 60.36%，降低缩放可部分恢复。最终挑战赛排名第三、10B 以下轻量组件第二名。

### 🔧 技术方案

**问题背景：** 现有听觉问答基准存在语言先验泄露，模型替换音频为静音仍能答对部分题，无法证明真正基于音频推理。ADQA 通过 Audio-Dependency Filtering 筛选强音频依赖样本解决该问题，但答案级奖励不监督中间推理是否扎根于声学证据，可能产生未落地或退化的推理轨迹；且任务特定后训练并非对所有模型有益。

**模型架构：** 基于 Qwen2.5-Omni-7B 构建 Qwen-CoT 与 Qwen-Structured-CoT 两条流水线；基于 MOSS-Audio-8B-Thinking 构建零样本与 LoRA-SFT 系统。LoRA 施加于音频编码器、多模态投影层与语言模型全部线性层，rank r=8，训练时 α=32（γ=4）。

**核心创新：** (1) 结构化 CoT 框架：将输出分解为 question_analysis、question_type、audio_evidence、reasoning 及最终答案四字段，显式监督中间推理。(2) 门控双阶段 RL：采用 GDPO 按组归一化多奖励，question analysis 相似度仅在题型正确时生效，audio evidence、reasoning 与长度正则均以答案正确为门控条件，避免错误推理轨迹获得虚假高分。(3) 推理时 LoRA 缩放：固定训练好的低秩矩阵仅改变 γ=α/r，无需再训练即调整适配器强度。

**训练策略：** 数据为官方 AudioMCQ-StrongAC-GeminiCoT 训练集（19,480 条）。Qwen：SFT 1 epoch、lr 1e-4；RL 1 epoch、lr 1e-5、KL β=0.001、generations 8。MOSS：SFT 1 epoch、lr 1e-4。全部在 4×RTX 4090、bfloat16 下训练，后处理统一精确/包含匹配映射选项并加多数投票。

### 📊 实验结果
**数据集**：DCASE 2026 Task 5 development set

**主要指标**：
- Qwen-CoT：基线 55.38% → SFT 56.50% → GRPO 58.93%，γ=2 时 61.05%
- Qwen-Structured-CoT：基线 54.39% → SFT 57.93% → GDPO 58.93%，γ=4 最优
- MOSS-Thinking-Full：零样本 66.02% → SFT 58.18%，γ=0.5 时 67.02%
- MOSS-Thinking-Label：零样本 67.70% → SFT 60.36%
- 系统总体第三名，10B 以下轻量组件第二名

**是否开源**：代码已开源（https://github.com/WeitengHu/DCASE2026-Task5），模型与数据未公开

### ⭐ 评分：8/10
评分理由：结构化 CoT+门控 GDPO 多奖励设计针对 ADQA 声学证据扎根问题有明确技术贡献，推理时 LoRA 缩放验证了适配器强度与模型能力权衡的假设，实验跨两个骨干、含逐阶段消融与完整缩放曲线，分析扎实。扣分点在于本质是挑战赛系统报告，规模较小，且缩放机制是复用 SALMONN 观察而非全新设计。

---

## [7] sanoTTS: The Smallest Real-Time Neural TTS on a General-Purpose Microcontroller

**arXiv ID**：2608.21378 | **方向**：语音大模型

**作者**：Ashish Thapa

**机构**：Ampixa Labs

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.21378 | **PDF**：https://arxiv.org/pdf/2608.21378 | **代码**：https://github.com/Ampixa/saanotts | **Demo**：暂无

### 📌 简介
针对 Piper/VITS 这类约 15M 参数的优质神经 TTS 面向 Linux 级设备、无法在通用单片机（MCU）上实时合成的问题，本文提出 sanoTTS，一个从 VITS 条件 VAE 教师蒸馏出的确定性学生堆栈，无需神经加速器即可在通用 MCU 上运行到 22.05kHz PCM。部署图仅 567,008 参数，两个 int8 blob 共 679,832 字节；在 ESP32-S3 上 1.02 秒生成 4.54 秒语音（0.22x实时），在无 FPU 的 ESP32-C3 上离线 5.72x实时。代价是质量下降：嵌入式堆栈 SCOREQ 2.54、UTMOS 2.80，其 Kristin 教师为 4.68/4.42；改用 Amy 教师的质量级 Pareto 点（1,454,284 参数）可达 SCOREQ 4.13、UTMOS 4.10。

### 🔧 技术方案

**问题背景：** 面向 MCU 时参数量只回答了一半问题：模型还须在未见文本上保持可用质量，并在设备算力/内存内完成合成。已有工作边界不统一：TinyTTS 使用 NPU；TinyVocos 仅测声码器而非完整 TTS；SlimTTS 报告了 562k 参流水线但未在物理 MCU 上执行。作者主张知识蒸馏比单纯剪枝更能迁移教师行为，并对完整神经路径在实体 MCU 上计时。

**模型架构：** 40 维 c-line 部署图由三部分串联：时长学生（36,164 参数，宽度32、三个 kernel-5 残差块）、声学学生（199,536 参数，宽度48，直接预测解码契约c）、帧域逆STFT解码器（331,308 参数，宽度76、五个 kernel-7 块，预测 1024 点 iSTFT（hop 256）的 513 个幅度bin 与 1026 个相位坐标）。训练期另有一个 14,952 参数的 z→c 编码器收缩 192 通道教师潜变量，部署时不参与。

**核心创新：** (1) 教师一致的确定性蒸馏：冻结教师做无噪声确定性推理，从文本先验取对齐标签、固定样本z与波形，学生不构成第二个VAE。(2) 多分量蒸馏损失：时长损失由 Huber0.25 加对数总和平方时长守恒项；潜空间接口损失组合 L1/L2/通道归一化L1/一阶差分L1/统计匹配；波形损失为 L1+多分辨率STFT+LSGAN对抗+特征匹配，联合蒸馏以 λc 锚定接口，打包权重 (0.1,0.5,0.025,0.25,0.5)。(3) 音素级失效恢复：用对齐时长按音素类测 2-8kHz 频谱平坦度定位齿擦音缺陷，引入仅对/s,sh,z,zh/加回乘性高斯噪声的推理期修正。(4) MCU 工程优化：int8 逐输出通道量化、手写PIE矩阵向量核、双核列切分与周期重叠相加，把 4.54 秒语音计算从 6.685s 压到 1.021s。

**训练策略：** 训练数据为教师标注文本行，由 512 行扩至 14,343 行（窄集 12 句模板句曾使 SCOREQ 虚高 1.35）。时长尺度英语 s_v=1.08、越南语/印尼语 1.16；部署激活词表 157 项；论文记录精确种子与训练 flags，所有 blob 提供校验和。

### 📊 实验结果
**数据集**：LJSpeech（验证集24句构成 diverse24 未见文本评估集）

**主要指标**：
- 参数量：嵌入式 567,008；质量级 1,454,284 / 1,834,380
- ESP32-S3：最终 0.22x 实时，峰值 arena 约 289KB，全程约 45 MMAC/秒音频
- ESP32-C3（无FPU）：整数流水线后 5.72x 实时（离线）
- 质量（diverse24）：嵌入式 SCOREQ 2.54 / UTMOS 2.80；Amy Pareto 4.13/4.10；Kristin 教师 4.68/4.42
- 对比 TinyTTS（1.22M）：3.94/3.65/3.62；解码器容量缺口（1.49）大于声学缺口（0.98）

**是否开源**：开源。代码、模型清单、精确二进制 fixtures、可移植 C 运行时与评价工具见 https://github.com/Ampixa/saanotts

### ⭐ 评分：8/10
评分理由：创新点扎实——从 VITS 条件 VAE 可复现推导确定性学生、显式40维潜接口与多分量蒸馏损失组合，并量化容量与表征的贡献；实验充分，含教师复现、受控容量研究、窄测试集膨胀审计与音素级频谱探针。在无 NPU 的实体 MCU 上给出迄今最小的实时完整 TTS 部署测量，实用价值高。扣分点：嵌入式质量差距仍大（SCOREQ 2.54 vs 4.68）、仅 ESP32-S3 为唯一实测实时目标、缺 MOS 与能耗测量。

---

## [8] Mitigating Speaker Leakage in Cascaded Multi-talker ASR with Diarization-based Transcript Correction

**arXiv ID**：2608.22196 | **方向**：语音大模型

**作者**：Hermann Nkouanga, Minwei Luo, Maggie Wigness, Suresh Singh

**机构**：Portland State University, US Army Research Laboratory

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.22196 | **PDF**：https://arxiv.org/pdf/2608.22196 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
级联多说话人ASR（MT-ASR）性能受限于分离阶段的说话人泄漏问题，现有修正方法以词法重标注为主，在高泄漏场景下存在内在歧义。本文提出基于剪枝的全新修正范式：利用预训练说话人分离（Diarization）模型作为多模态验证器，对满足时间包含、词法交叉验证与时间对齐三段一致共识的转录词进行剪枝。在 Libri2Mix、LibriSpeechMix 与 AMI 语料上，该算法在所有测试条件下一致降低 cpWER，在高泄漏子集上相对基线最多降低 29.26%。该文已获 INTERSPEECH 2026 接收。

### 🔧 技术方案

**问题背景：** 级联MT-ASR采取"先分离、后识别"的模块化管线，依赖基础模型但性能上限由分离质量决定。分离不完美必然在分离流中残留干扰说话人语音，即"泄漏"，导致最终说话人归属错误。现有后处理主导范式是词法重标注：早期LSEC依赖文本、易过度修正；LLM方案引入延迟与幻觉风险；混合方案融合词法与声学信号但仍属重标注。作者指出高泄漏场景下重标注本身具有歧义，转而在信号层验证并删除泄漏。

**模型架构：** 分离采用 Mossformer2 与 Sepformer（speechbrain预训练），识别采用 Universal-2（可输出词级时间戳），验证器为 pyannote.audio 3.1。联合实验框架为 MossFormer2 编码器经24次FLA自注意力与Gated FF交替迭代产生512维帧级特征，分出 Diarization 头（2层Transformer）输出逐帧说话人概率。

**核心创新：** (1) 三段一致共识剪枝：词元仅当同时满足声学包含（词落入泄漏窗口）、词法交叉验证（该词存在于并行转写）、时间对齐（区间重叠）三个条件才判定为泄漏并删除。(2) 自适应过滤：用 Ratcliff/Obershelp 相似度 σ，仅在 σ 超过阈值 γ（取0.40）时才跳过修正，避免误删。(3) 联合分离-Diarization预防架构与分阶段微调：总损失 L=L_SI-SNR+λ_diar·L_diarization（λ_diar=20.0），先冻结分离主干10轮稳定 Diar 头再整体解冻微调5轮。

**训练策略：** 联合框架仅用 Libri2Mix both-train 子集微调 Diarization 头；消融比较仅文本、仅声学与完整三模态贡献，证明声学窗口是泄漏检测主驱动力，词法与时间对齐作为安全门防止过度修正。

### 📊 实验结果
**数据集**：Libri2Mix、LibriSpeechMix（2spk）、AMI 会议语料（SDM与IHM，659段双说话人）

**主要指标**：
- Mossformer+修正（整体）：3.53→3.44，9.31→9.17，5.13→4.64，35.50→32.67，23.96→22.26
- 高泄漏子集（相对降幅）：Mossformer 在 LSM 上 48.58→34.51（-28.96%）、AMI-IHM 上 65.58→46.39（-29.26%）
- 联合架构域迁移敏感：LSM 上+18.91%、AMI-IHM 上+20.78% 退化
- 消融：仅文本模态全面劣于基线（过度修正），仅声学降幅显著，完整三模态最优

**是否开源**：暂未开源（仅引用第三方 speechbrain 预训练模型）

### ⭐ 评分：7/10
评分理由：首次系统提出以剪枝替代重标注的说话人泄漏修正范式，三段共识机制设计合理且消融充分验证各模态作用，高泄漏子集上29%的相对降幅说明精度高。扣分点在于联合架构探索失败未形成有效信号级方案，缺少与LLM重标注SOTA方法的直接对比，且未开源降低可复现性。

---

## [9] Multi-Task Learning for Non-Canonical Phoneme Recognition via Articulatory Feature Decomposition

**arXiv ID**：2608.22273 | **方向**：语音大模型

**作者**：Sophia Riaz, Haoze Zheng, Amos Roche, Miyu Zhang, Anamika Ragu, Salvatore Penachio, Kaustav Mukherjee, Aneesh Jonelagadda

**机构**：Kaliber AI（美国）

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.22273 | **PDF**：https://arxiv.org/pdf/2608.22273 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对病理/非标准语音中系统性的发音偏差与临床标注数据稀缺，本文将音素识别从"原子类别分类"重构为发音特征维度（manner/place/voicing/height 等）的多任务预测，提出基于 WavLM 的分层多任务（HMTL）架构，通过 cross-attention 融合发音特征表示后经 BiLSTM 与 CTC 输出音素序列。结合 Momentum Pseudo-Labeling 半监督与两阶段分段解冻训练，在 L2-ARCTIC 代理数据集上把音素错误率（PER）从最强基线 14.46% 降至 13.47%，并系统减少清浊、元音高度等结构化混淆（voicing 错误 -10.1%、height -5.65%），且优于外部多视图基线 MV_multi-MT_seq（14.13%）。

### 🔧 技术方案

**问题背景：** 病理/非标准语音（如运动言语障碍、儿童言语失用）音素识别 PER 高达 42%-69%。现有模型在健康语音上训练，会把非标准发音"自动纠正"为最近的规范音素；且把音素当作原子标签无法刻画"部分特征保留、部分偏离"的系统性错误结构。病理语音标注稀缺且标注者间一致性差，故用 L2-ARCTIC 口音语音作为病理发音的代理。

**模型架构：** 以 WavLM-base-plus（预训练9.4万小时）为编码器，对全部 transformer 隐层做两组可学习加权求和。三支发音专家头：type 头做辅/元音二分类门控，consonant 头与 vowel 头提取特征级表示。phoneme query 对专家令牌内存矩阵做 cross-attention，残差融合后经 BiLSTM 捕获时序依赖，最后 CTC 解码（39音素+blank）。隐藏维 384、dropout 0.35。

**核心创新：** (1) 发音特征维度分解：通过 IPA 中间映射从 ARPAbet 导出 type/place/manner/voicing/height/backness/roundedness 七类逐帧辅助标签，辅/元音特征按相关帧互相掩码。(2) 分层多任务+专家内存 cross-attention：phoneme 表示作为 query 每帧动态加权专家令牌，残差融合保留原始音素编码；辅助任务权重由 MGDA（Frank-Wolfe）求解帕累托最优梯度组合。(3) MPL 半监督+级联分段解冻：EMA 教师对干净语音产生软伪标签，先冻结骨干训练15轮再解冻顶部6层联合微调15轮，配重放机制缓解灾难性遗忘。

**训练策略：** 波形级增强含相位扰动（模拟痉挛性构音障碍不稳定性）、VTLP、pitch shift、时长拉伸与加性噪声；AdamW、梯度裁剪0.35、Optuna TPE调参。L2-ARCTIC 24说话人（6种母语背景），18人训练/6人测试。

### 📊 实验结果
**数据集**：L2-ARCTIC（24位非母语英语说话人，作为病理语音代理）

**主要指标**：
- PER：HMTL+CA+Aug+MPL 13.47%，最强基线 WavLM+Aug+MPL 14.46%，外部 MV_multi-MT_seq 14.13%
- 错误结构：voicing 错误 -10.1%、height -5.65%、backness -5.83%、roundedness -4.73%
- 消融：去掉任一发音头 PER 上升 +0.08~+0.44
- 引入 cross-attention 后 MPL 大幅减少删除错误（-9.7%）

**是否开源**：暂未开源

### ⭐ 评分：7/10
评分理由：创新性地将音素识别解构为发音特征维度预测，专家内存 cross-attention 融合与 MGDA 加权技术路线完整，错误模式沿发音特征维度的分析具语言学可解释性。局限在于仅用 L2 口音作为病理代理，未在真实病理数据集验证；特征为离散单标签，无法刻画连续发音动力学。

---

## [10] AudioNoisePrints: Model-free audio watermarking using spatial correlation in flow matching TTS

**arXiv ID**：2608.22186 | **方向**：语音大模型

**作者**：Timothy Tin-Long, Jian Zhu, Aidan Pine, Mengzhe Geng

**机构**：加拿大国家研究委员会（National Research Council Canada）、不列颠哥伦比亚大学

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.22186 | **PDF**：https://arxiv.org/pdf/2608.22186 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对flow matching/扩散TTS水印的"事后"嵌入需额外算力、损伤音质且易遭覆盖攻击，"模型内"水印需重训生成模型的问题，本文提出 AudioNoisePrints，首次将图像领域 NoisePrints 思想迁移到语音合成：利用 FM/扩散模型中初始高斯噪声与生成输出间显著的余弦相关性，生成时仅替换初始噪声即完成"模型无关"打标，零推理开销、不重训TTS、不损音质。在 F5-TTS 与 MatchaTTS 上，其朴素余弦方案与受训检测器在 AAC 压缩下分别取得 0.987 与 0.9947 准确率（AudioSeal 为 1.0），而在裁剪、变速等强增强下显著优于 AudioSeal——后者在仅1%音速变化时即完全失效，本文顶部精度仍达 97-98%。

### 🔧 技术方案

**问题背景：** 扩散/FM模型虽推动了高保真语音合成，但生成内容缺乏可靠溯源水印。post-hoc 水印（如 AudioSeal）带来额外计算与延迟，且存在"音质-鲁棒性"根本权衡，并易受覆盖攻击；in-model 水印需重训整个生成模型，训练昂贵且可能降低生成质量。图像领域已证明潜在扩散模型中生成图像与初始噪声存在显著空间相关（NoisePrints），但尚无工作将其应用于语音合成模型。

**模型架构：** AudioNoisePrints 不改动任何生成模型，仅以预定义特殊噪声 x̂_init 替换生成时的初始高斯噪声，检测在音频/Mel谱域进行；为对抗裁剪，将 x̂_init 按固定长度100帧在 Mel 空间中周期性重复直至覆盖全程。外部检测器为 4 层 Conv2D ResNet 二分类。TTS 侧使用 F5-TTS v1_Base（DiT结构FM模型，配 Vocos 声码器）与 MatchaTTS，并额外验证 DiffWave 扩散声码器。

**核心创新：** (1) 训练免费、即插即用：不重训TTS、生成与推理零额外计算，不改变音频内容，规避"音质-鲁棒性"权衡并免于覆盖攻击。(2) 经验p值判定替代固定阈值：比较目标音频与原始噪声的余弦相似度与500个随机噪声的相似度分布计算经验p值，消融显示余弦与点积有效、L1/L2失效。(3) 轻量外部检测器：以BCE二分类判断是否由指定噪声生成，训练引入 MP3、AAC 等压缩增强，在裁剪、变速等强攻击下维持检测精度。

**训练策略：** 检测器以BCE损失训练二分类；训练数据来自 LibriTTS 与 LJSpeech，规模远小于 AudioSeal 的 VoxPopuli（4.5K小时）；全程采用 Euler ODE 求解器，p值估计使用 N=500 个随机噪声。

### 📊 实验结果
**数据集**：LibriTTS、LJSpeech、VCTK（Matcha-TTS权重）、VoxPopuli（AudioSeal基线训练数据）

**主要指标**：
- F5-TTS，AAC压缩准确率：CosSim 0.987、检测器 0.9947、AudioSeal 1.0
- 强增强（裁剪、变速）：AudioNoisePrints 显著胜出，AudioSeal 在1%音速变化即完全失效
- 距离函数消融：余弦 0.988 > 点积 0.986 >> L2 0.497 ≈ L1 0.497
- MatchaTTS 与 DiffWave 各生成500条，原始噪声p值全部为0.0，证实空间相关性普遍存在

**是否开源**：暂未开源

### ⭐ 评分：7/10
评分理由：首次将 NoisePrints 空间相关水印系统性迁移至 flow matching/扩散语音合成，训练免费、零生成开销且不损音质，设计简洁并直接规避"音质-鲁棒性"权衡。实验覆盖 F5-TTS、MatchaTTS 与 DiffWave 三种架构，以远小于 AudioSeal 的数据量在强增强下超越基线。局限在于对回声等特定增强弱于 AudioSeal，攻击类型有限，且未公开代码。

---

## 语音前端

## [1] FlowSep 2: Self-Supervised Flow Matching for Language-Queried Audio Source Separation

**arXiv ID**：2608.22111 | **方向**：语音前端

**作者**：Yi Yuan, Xubo Liu, Haohe Liu, Xiyuan Kang, Mark D. Plumbley, Wenwu Wang

**机构**：英国萨里大学、Meta 超级智能实验室、伦敦国王学院

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.22111 | **PDF**：https://arxiv.org/pdf/2608.22111 | **代码**：暂无 | **Demo**：https://audio-agi.github.io/Flowsep2-demo/

### 📌 简介
现有 LASS 方法多为判别式掩码估计模型，在声音高度重叠的复杂声学场景下会过抑制目标源或分离不完整。本文提出 FlowSep2，将整流流匹配（Rectified Flow Matching）与扩散 Transformer（DiT）结合，在 Stable-Audio VAE 潜在空间中从高斯噪声直接生成目标源表征，条件为混合音频潜在表示与 FLAN-T5 文本嵌入，并引入 Self-Flow 自监督表征对齐。在多个 LASS benchmark 上，FlowSep2-M 将 AudioCaps 的 FAD 从 FlowSep 的 2.86 降至 0.88、VGGSound 从 2.06 降至 1.32，CLAPA 分别提升至 80.5 与 78.5，全面优于 LASS-Net、AudioSep、SAM-Audio 等基线。扩展至 24 层 FlowSep2-L 后 FAD 进一步降至 0.84。

### 🔧 技术方案

**问题背景：** 判别式 LASS（LASS-Net、AudioSep）从混合频谱估计时频掩码，重叠事件下掩码易产生过抑制或选择性不足，造成谱空洞与不完整分离；PIT/MixIT 等通用分离依赖类别选择模块、扩展性差；SAM-Audio 用生成式框架但依赖大规模私有数据，无法复现与系统分析。

**模型架构：** 文本编码器采用预训练 FLAN-T5（输出 50x1024 嵌入）；音频编码器用 Stable-Audio 波形 VAE（压缩比约320，10秒音频得到 512x128 潜在图）；生成骨干为 DiT 流模块，设 S/M/L 三种规模（深度 12/16/24 层，M 约558M参数），混合潜在与中间潜在沿通道维拼接后输入；VAE 解码器将潜在图重建为波形。推理时用 ODE 求解器从 λ=0 积分到 λ=1。

**核心创新：** (1) 生成式 RFM 分离范式：插值路径 zλ=(1-(1-σ)λ)z0+λz1，损失 L_RFM=E||μ- v||²，在潜在空间直接"生成"目标源而非估计掩码，规避掩码伪影。(2) Self-Flow 自监督流表征对齐：EMA 教师-学生框架，每个潜在token采样两个流时间 λa/λb 构成学生多时步视图，教师接收统一视图 λc=max(λa,λb)，对教师深层与学生浅层中间特征施加余弦相似度损失。(3) 语义表征强化策略对比：与 RAE 和 REPA 相比，Self-Flow 收敛更快（约1-1.5M步即达强性能）且质量均衡。

**训练策略：** 训练集扩至 5,650 小时/2,033,564 段（VGGSound 510h、AudioCaps 140h、AudioSetCaps 3900h、WavCaps 1100h），统一 mono 16kHz；单卡 A100-80GB 训练 400 万步，batch size 8，AdamW，lr 5x10⁻⁵，前10,000步线性预热。

### 📊 实验结果
**数据集**：VGGSound、AudioCaps、ESC-50、MUSDB18、DCASE 2024 Task 9（Synth 3000 / Real 100）

**主要指标**：
- FAD（越小越好）：FlowSep2-L 在 AudioCaps 0.84、VGGSound 1.28、DCASE-Synth 0.71（FlowSep AC 2.86→0.88）
- CLAP Score：AudioCaps 44.9、DCASE-Real 51.0、VGGSound 42.0，所有数据集均为最高
- CLAPA：AudioCaps 80.5（FlowSep 76.7）、VGGSound 78.5（69.2）
- 主观指标：AudioCaps SAJ 2.96、OVL 4.09
- 消融：DiT 优于 UNet、RFM 优于 DDPM、模型扩容持续增益

**是否开源**：暂未开源（仅有公开 Demo 页面）

### ⭐ 评分：8/10
评分理由：首次将 RFM+DiT 与自监督表征对齐（Self-Flow）系统性引入 LASS，构建了可扩展的生成式分离范式，创新性突出；实验覆盖 6 个 benchmark 及主客观双套指标体系，并有 4 组消融深入分析设计取舍。扣分点在于模型与代码未开源限制可复现性，且评测依赖 FAD/CLAP 等软对齐指标而非传统分离度量。属实质贡献、实验完备的工作，接近顶会水准。

---

## [2] AT-ADD: A Benchmark and Challenge for Robust and All-Type Audio Deepfake Detection

**arXiv ID**：2608.23437 | **方向**：语音前端

**作者**：Yuankun Xie, Haonan Cheng, Jiayi Zhou, Xiaoxuan Guo, Tao Wang, Changhao Zhang, Jian Liu, Weiqiang Wang, Ruibo Fu, Xiaopeng Wang, Hengyan Huang, Xiaoying Huang, Long Ye, Guangtao Zhai

**机构**：中国传媒大学、蚂蚁集团、中国科学院自动化研究所、北京理工大学、上海交通大学

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.23437 | **PDF**：https://arxiv.org/pdf/2608.23437 | **代码**：https://github.com/xieyuankun/AT-ADD-Baseline | **Demo**：https://at-add.com

### 📌 简介
本文提出 AT-ADD 基准与 ACM Multimedia 2026 大挑战，针对现有 ADD 检测以语音为中心、忽略真实信道变化与多类型音频的问题，构建两大任务：Track1 为覆盖47个生成模型、11,299说话人、96种语言及噪声/混响/重放/压缩等扰动的鲁棒语音深伪检测；Track2 为语音、环境声、歌声、音乐四类音频在测试时类型未知条件下的全类型检测。官方最强基线 FT-XLSR-AASIST 在 Track1/Track2 评测集上仅达 76.73%/79.47% Macro-F1，而冠军系统分别达 90.71% 与 96.10%。结果表明大规模自监督表示、条件感知增强、多片段推理及结构化融合是泛化关键，但 BigVGAN 与重放语音等少数生成条件仍是未解难题。

### 🔧 技术方案

**问题背景：** 现有 ADD 基准（ASVspoof、ADD、SVDD等）以语音为中心且多在受控条件下评估，对压缩、噪声、混响、重放等真实信道变化鲁棒性差；对 ALLM 合成与 neural codec 等新范式及非语音音频类型泛化不足。AT-ADD 以渐进式双赛道弥合理想研究与真实多媒体取证之间的差距，全程采用闭合设置，仅允许使用官方 train/dev 数据。

**模型架构：** 提供六类可复现基线：Spec-ResNet（47.41%/53.83%）、AASIST（60.39%/62.21%）、FT-XLSR-AASIST（全微调W2V2-XLSR-300m+AASIST，76.73%/79.47%）、WPT-XLSR-AASIST（73.35%/66.68%）及 Qwen2.5-Omni-3B/7B 的 ALLM 基线。冠军方案为 W2V-BERT2.0-AASIST 集成（LoRA 适配器+AM-Softmax 大间隔微调），T2 采用 BEATs 类型路由器配合语音/通用专家路由集成。

**核心创新：** (1) 大规模多类型数据构建：Track1 共245,655条，约20%真实/23%伪造样本施加音量缩放(0.2-0.9)、变速(0.5-2.5)、8kHz重采样扰动，评测含27个不可见生成器；Track2 共467,223条、68类生成模型，评测引入 AVQA、FMA 等OOD真实子集。(2) 双层均衡评估协议：Track2 先算类型内 Macro-F1 再对四类取均值，暴露"平均高分掩盖类型短板"（唱歌96.30%对声音仅66.82%）。(3) 样本级诊断分析：对 Top5 系统做逐生成器/逐语种/自举重采样分析，量化错误互补性与榜单统计稳定性，并给出 oracle 上界（T2 Top3 达98.40%）。

**训练策略：** 基线采用0.5固定决策阈值；增强体系覆盖 RawBoost、MUSAN 噪声、RIR 混响、codec 重编码、量化、变速、重放模拟与片段拼接；比赛允许最多5个子系统的融合；身份隔离与生成器、源、任务标注随数据发布。

### 📊 实验结果
**数据集**：AT-ADD Track1（245,655条/47生成器）与 Track2（467,223条/68生成模型/四类音频）

**主要指标**：
- Macro-F1（Track1 Eval）：官方基线 FT-XLSR-AASIST 76.73%，冠军 WaveShield 90.71%
- Macro-F1（Track2 Eval）：FT-XLSR-AASIST 79.47%（声音66.82%/唱歌96.30%），冠军 starfire 96.10%
- 最难生成器 BigVGAN 平均假样本召回：Track1 为72.84%，Track2 语音仅58.33%
- 语种稳健性：Top5 语言级 Macro-F1 自低资源81.66%升高资源86.83%

**是否开源**：已开源。数据集（Hugging Face）、官方基线代码（https://github.com/xieyuankun/AT-ADD-Baseline）、ALLM基线，官方主页 at-add.com

### ⭐ 评分：8/10
评分理由：构建了迄今最大、覆盖四类音频与68种生成模型的全类型 ADD 基准，数据构建规范（身份隔离、OOD真实子集、标注完备）与双层均衡评估协议设计严谨，实用价值高。对 Top5 系统的生成器级、语种级与自举统计稳定性分析超出一般 benchmark 论文深度。扣分在于方法贡献主要源自参赛系统分析，自身未提出新检测算法。

---

## [3] Separating Voice from Age in COPD Screening

**arXiv ID**：2608.21599 | **方向**：语音前端

**作者**：George P. Kafentzis, Nikoletta Arvaniti

**机构**：希腊克里特大学计算机科学系

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.21599 | **PDF**：https://arxiv.org/pdf/2608.21599 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文针对 COPD 语音筛查结果可被"年龄混淆"琐碎解释的问题，重新评估公开的 COPDVD 持续元音语料（1246条录音、68名参与者），首次在严格的参与者级年龄匹配队列上验证语音是否携带超越年龄的疾病信息。作者发现常规合并评估在年龄严重失衡（SMD=0.726）下无法区分语音病理与年龄信号，遂提出以"混淆变量自身的判别力"（原始年龄 AUC 0.510、性别0.479，均为随机水平）为已核验对照的匹配评估协议。结果显示：年龄匹配队列上不含年龄的声学模型保留 ROC-AUC 0.717、AP 0.747，而含年龄的模型降至0.531-0.679；14个经典嗓音质量扰动指标（PTRB）达 AP 0.755，媲美55维组合表征。结论是存在非年龄声学信号，但无法排除录音条件混淆。

### 🔧 技术方案

**问题背景：** COPD 强年龄相关且发声随年龄衰老变化，病例组普遍比对照组年老时，模型可能学到的是年龄或其声学代理而非疾病。仅"剔除年龄变量"的训练并不充分：特征与年龄相关时，灵活学习器可从相关声学特征中重构年龄驱动决策边界。作者审计数据发现：按参与者计对照组比 COPD 组年轻7.7岁、SMD=0.726，而按录音加权则方向反转——源论文声称的年龄匹配基于录音而非参与者统计。

**模型架构：** 主模型为 CatBoost 梯度提升树（性别作为原生类别特征），另以固定超参的直方图梯度提升（HistGB）和 L2 正则逻辑回归做独立复现。共12个嵌套特征配置（维度1至107），用于隔离年龄、性别、症状问卷、MFCC时序差分等各块的贡献；PTRB 为14个先验临床选取的经典扰动/嗓音质量指标。

**核心创新：** (1) 参与者级评估协议：分层分组5折外CV、反向录音数加权、logit域平均聚合每位参与者单分数、仅在参与者上 bootstrap，杜绝跨折录音泄漏。(2) 年龄匹配评估+已核验对照：每次按2年卡尺一对一抽出约24对，并报告原始年龄与性别的 AUC 作为阳性对照；证明拟合年龄模型因交叉拟合伪影不能作对照。(3) 混淆协变量排除建议：含年龄训练的模型匹配后 AUC 跌幅（-0.108）远大于不含年龄者（-0.008），且跌幅随声学信息增加单调缩小，主张训练时即排除混淆协变量。

**训练策略：** CatBoost 网格 4x3x4x4=192 组合（迭代300-1000、深度2-6、学习率0.001-0.10、L2正则1-10），一标准误差规则选择；录音反向权重仅用于训练目标；置信区间用2000次参与者 bootstrap。

### 📊 实验结果
**数据集**：COPDVD（1246条持续元音/a/录音，68名瑞典参与者，30 COPD/38对照），去重后67人940条

**主要指标**：
- 匹配队列 ROC-AUC：AC（不含年龄）0.717 [0.552,0.859]；含年龄配置 0.531-0.679
- 匹配队列 AP：AC 0.747 [0.581,0.892]；PTRB 0.755 为最高下界
- 对照判别力：原始年龄 0.510、性别 0.479，均在机会水平；SMD 从0.726降至0.026
- 复现：三学习器年龄致死方向分离一致（+0.082/+0.147/+0.066）

**是否开源**：暂未开源

### ⭐ 评分：8/10
评分理由：论文切入横断面语音筛查长期被忽视的方法学盲区——混淆变量本身作对照、参与者级年龄匹配评估均为领域首创设计，SMD 反转这一审计发现极具警示价值；实验充分性突出：12配置消融、三学习器复现、配对 bootstrap 齐全，并坦率交代自身局限。弱点在于样本极小、点估计区间过宽，临床实用性有限，且未公开代码。

---

## [4] LipsAM: Lipschitz-continuous Neural Networks for Convergent Plug-and-Play Audio Signal Recovery

**arXiv ID**：2608.23038 | **方向**：语音前端

**作者**：Kazuki Matsumoto, Ren Uchida, Natsuki Yoshino, Kohei Yatabe

**机构**：东京农工大学（Tokyo University of Agriculture and Technology）

**发布日期**：2026-08-25 | **论文**：https://arxiv.org/abs/2608.23038 | **PDF**：https://arxiv.org/pdf/2608.23038 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
传统语音 DNN 将复数 STFT 的幅度与相位分开处理，由于 sign 函数在零点不连续，此类网络即使幅度部分 Lipschitz 连续，整体也必然不连续，无法纳入现有 Lipschitz 理论框架。本文推导了幅度修正器（AM）满足 Lipschitz 连续性的充要条件（定义 LipsAM），并给出 LipsAM-E、LipsAM-M（时频掩蔽）两类可证连续的架构及 Lipschitz 常数紧凑上界。在此基础上提出 CoReM-LipsAM 与 PnP-ADMM 去混响算法，理论上保证收敛（定理17）。在语音去混响实验中，CoReM-LipsAM 将迭代残差降至约 10⁻¹² 量级表明收敛成立，但 SI-SNR 低于无理论保证的 ReM-AM 基线。

### 🔧 技术方案

**问题背景：** 现有 Lipschitz 网络构造（谱归一化、正则化、结构法）均针对实值图像网络；而语音常用的复数谱网络通过幅度映射加 sign(z) 分离处理幅度相位，sign(z) 在 z=0 处不连续，导致即使幅度映射本身 Lipschitz 连续，整体映射仍非 Lipschitz。这阻碍了基于 Lipschitz 条件的 PnP 收敛保证在语音中的应用。

**模型架构：** LipsAM-E 为 (min(ℰ(|z|),|z|))+sign(z)，加入逐元素 min 层强制"零保持"；LipsAM-M 为 G(max(ℳ(|z|),a|z|+b))z，通过 max 操作强制掩蔽映射线性增长。可学习映射采用预缩放 L=sigmoid(s_L) 加 5 层一维正交卷积（核3、通道128）与 LeakyReLU(0.1) 构成，保证 Lip≤L。

**核心创新：** (1) 定理证明 AM 整体 Lipschitz 连续当且仅当其满足 LipsAM 定义（Lipschitz + 零保持），为架构设计提供可验证判据。(2) Lipschitz 常数求值框架：将架构统一为双变量函数的一般形式，定理证明最紧全域上界在输入维数 N=2 时取得，将 N 维雅可比最大化等价降为仅7参数的优化问题；LipsAM-E 还解析导出 √(L²+1) 与 L+1 的闭合界。(3) CoReM-LipsAM 取 D=Id-(C/B)·LipsAM 构造残差映射并以 C/B 缩放使 Lipschitz 常数<1，在 Parseval 紧框架 STFT 与 γ 强凸数据项下给出 PnP-ADMM 收敛到唯一不动点的充分条件。

**训练策略：** 以 LibriTTS-R train-clean-100 干净语音加高斯噪声做去噪训练（SNR 10-30 dB，步长2 dB）；时域 MSE 损失、Adam lr=0.001、batch=32、训练10 epoch；掩蔽型用三次样条构造可微代理以兼容自动微分；最优模型学得的 L 分别为 0.48（E型）与 0.14（M型）。

### 📊 实验结果
**数据集**：LibriTTS-R（train-clean-100），语音去混响任务

**主要指标**：
- SI-SNR（1200次迭代后）：无约束 ReM-AM 最高，CoReM-LipsAM 因 Lipschitz 约束性能下降，但仍优于软阈值基线
- 收敛残差 Δx[k]：ReM-AM 不下降（不收敛），CoReM-LipsAM 降至约 10⁻¹²
- Lipschitz 界验证：N=2 时数值估计达到上界

**是否开源**：暂未开源

### ⭐ 评分：7/10
评分理由：理论贡献扎实，给出 LipsAM 充要条件、掩蔽型充分条件、N=2 降维求常数框架及 PnP 收敛定理共10余个带完整证明的结论，填补了语音幅度/相位分离网络 Lipschitz 理论的空白。但实验仅在单一去混响任务验证，且为满足理论约束性能低于无约束基线，未报告绝对 SI-SNR 数值，代码未开源。整体属具有实质理论价值、实验支撑尚可的工作。

---

*Generated on 2026-08-25*