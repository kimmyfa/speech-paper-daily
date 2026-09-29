# 2026-09-28 语音论文速递

**共收录**: 25 篇 | **语音大模型**: 18 篇 | **语音前端**: 7 篇

> 目标日期 2026-09-28（北京时间，周一批次）arXiv 语音相关论文共命中 25 篇。
> 以下是按评分排序的结果（前 15 篇完整精读，其余仅列标题、arXiv ID、评分与链接）。

---

## 语音大模型

## [1] Acoustic-to-Text KV Compression for Full-Duplex Speech Models

arXiv ID：2609.31224 | 方向：语音大模型
作者：Yejin Lee, Seungbeom Kim, Yongha Lee, Kyuhong Shim
机构：成均馆大学（Sungkyunkwan University，韩国）
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.31224 | PDF https://arxiv.org/pdf/2609.31224.pdf | 代码：暂无 | Demo：暂无

### 📌 简介
全双工语音大模型在持续监听中不断累积声学KV状态，长时间交互内存开销巨大。本文提出声学到文本的KV压缩：利用"监听空闲时间"（约900ms）引入转录旁路通道，将语音转为紧凑文本记忆，缓存超预算时驱逐旧声学状态而保留转录与近期声学窗口。在MiniCPM-o 4.5上实现：10分钟LongSpeech会话峰值流式KV缓存降低64.6%，转录、时序问答与摘要均优于原生流式，且保持实时性与打断、轮转等全双工行为，无需独立ASR模型。

### 🔧 技术方案
**问题背景：** 全双工语音模型边听边说，语音表示占用的序列位置远多于文本（声学约17位置/秒 vs 转录约3位置/秒），KV缓存随交互持续膨胀；仅在输入结束后压缩无法降低处理过程中的峰值内存。
**模型架构：** 基于MiniCPM-o 4.5的1秒双工单元（约10个音频token+listen/speak决策）。新增<|asr_start|>/<|asr_end|>特殊token，在每个单元原生决策后插入转录段，保留在LM上下文但不进入语音解码器。推理时模型自预测是否开启旁路，贪心解码至多64个token；缓存超过预算B=4K时，驱逐保留窗口（最近5个单元）之外最旧单元的声学/结构KV，保留转录token与系统前缀，位置ID不因驱逐重编以避免RoPE重编码。
**核心创新：** (1)转录旁路通道利用监听空闲时间增量生成文本记忆；(2)LoRA秩16（α=32，仅加43.7M参数、占LM 0.53%）训练旁路，交叉熵监督转录+词级强制对齐（发射延迟δ=0.5s）；(3)以冻结原模型为teacher，在原生预测位置做token级前向KL蒸馏，并针对决策类型与轮次边界设计组平衡辅助损失，防止转录适配破坏原生听说行为；训练损失为四项之和。
**训练策略：** 仅用LibriSpeech train-clean 460小时中的132K短语句，3轮、学习率1e-4、批大小16；无需长音频或全双工交互数据。

### 📊 实验结果
**数据集**：LongSpeech（每任务100个10分钟英文会话）、Full-Duplex-Bench v1.0（727样本）、LibriSpeech test-clean
主要指标：
- ASR WER：12.9（原生流式96.9，StreamingLLM式截断109.5；外部Whisper-large-v3级联9.35但多1.55B参数）
- 时序QA准确率：42.0%（原生30.0%，StreamingLLM 4.0%）
- 摘要R-1：49.0（原生27.3）
- 峰值流式KV：4.02K vs 无驱逐同模型11.35K，降64.6%；监听态缓存12.3K→4.0K
- 实时性：4K预算下每单元均值461ms、p99 675ms，10039单元零超时（H100，批1）；词发射延迟1.01s vs 原生提示转录9.5s
- 全双工行为：轮转TOR 0.706、打断TOR 0.940，与原模型（0.664/0.975）相当；去掉蒸馏则几乎接管所有停顿（TOR 1.0），凸显行为蒸馏必要
- 预算消融：floor全驱逐WER升至19.7且4.07%超时，确认4K为合理工作点
**是否开源**：论文未给出代码链接，暂无

### ⭐ 评分：8/10
首次将"边听边转录+在线文本记忆驱逐声学KV"结合进全双工模型，工程动机明确、消融充分：仅0.53%参数的小适配即换来64.6%峰值内存下降，同时以蒸馏保行为的设计洞察（不当适配会摧毁轮换策略）极具价值。扣分在于仅单模型验证、转录WER不及外部大ASR级联、长程推理仅达Cascade水平且未公开代码。
## [2] Training-Free Contextual ASR via SpeechLLM-Based Error-Aware Selective Retrieval

arXiv ID：2609.30694 | 方向：语音大模型
作者：Natsuo Yamashita、Ai Nemoto、Ryosuke Koichi、Masaaki Yamamoto
机构：日立制作所研究所（Hitachi, Ltd. R&D Group, Japan）；日立高级系统株式会社（Hitachi Advanced Systems Corporation, Japan）
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.30694 | PDF https://arxiv.org/pdf/2609.30694.pdf
代码：暂无
Demo：暂无

### 📌 简介
本文提出一种免训练（training-free）的领域上下文ASR框架：让预训练语音大模型（Qwen3-Omni-30B）在解码第一遍识别假说的同时，定位“疑似含领域词识别错误”的短片段，以这些片段为硬门控触发对外部术语词典的音似检索（ANE），再由同一模型以一遍假说加检索术语为条件做第二遍上下文重识别。整条流水线无任何任务专用训练，在医疗、空管、金融三域将词典查询量削减92.6%并提升检索R@10与排序质量，同步改善第二遍WER与B-WER，为领域专有/低频词识别提供了低成本落地路径。

### 🔧 技术方案
**问题背景：** ASR对领域专有词与低频词识别困难。直接注入大型术语词典会引入大量无关偏置项并导致过偏置；检索式contextual biasing可缓解，但若对每个识别词都查询词典，则查库次数剧增且候选命中不准。已有方法多依赖单独训练的检索/排序/对齐模块，且选取准则未显式瞄准“既领域相关又很可能识别错误”的区域。
**模型架构：** 三段式流水线，全部由同一预训练Qwen3-Omni-30B-A3B-Instruct完成、不更新参数。第一段单次推理联合产出一遍假说h并定位领域词错误片段（限2词内、剔除纯数字）；第二段将各片段作为独立查询，用ANE相似度r(q,v)=1/(1+‖g(q)−g(v)‖2)对词典项打分并按max聚合排序取top-K，若无片段则跳过检索与二遍；第三段以一遍假说与检索项为条件对同一语音重识别。
**核心创新：** (1) ASR与错误定位联合推理：利用自回归性在假说之后输出错误片段，配合4条音文ICL示例覆盖无错/领域词替换/误听为常用词串/音似替换四类情形，使定位能条件于模型自身生成文本；(2) 片段作字典检索硬门控：只以片段查询而非全假说，把每句片段数从13.37降到0.99（削减92.6%）；(3) 全免训练闭环：检索采用公开的预训练ANE embedder-64，二遍重识别复用同一SpeechLLM，无需额外模块开发。
**训练策略：** 无任何任务专用训练或微调，纯prompt方案：4条ICL示例取自训练集且与评测 disjoint，领域引导p_dom仅改写出目标域、术语类别与选取准则；同任务格式跨域共用。

### 📊 实验结果
**数据集**：United-MedSyn（医疗，7906句、域词比11.65%）、ATCOSIM（空管，1901句、9.00%）、Contextual Earnings-22（金融，772句、5.04%）；词典由参考转写按百万词频过滤低通用度项构建。
**主要指标**
- 定位（MedSyn）：Error Precision 51.9%、Error Recall 76.1%、Domain Recall 86.0%，0.99片段/句，对比全1-gram（13.37片段、精度8.1%）与NE抽取（29.5%、Domain 81.7%）、置信片段（召回50.6%、Domain 65.3%）
- 检索：R@10 61.8%、MRR@10 47.9%、查询削减92.6%
- 二遍ASR（top-10）：WER 7.30→5.67、B-WER 41.43→28.05、U-WER 2.80→2.72
- 跨域：ATCOSIM WER 14.81→12.88、B-WER 46.40→30.65；Earnings WER 17.97→17.45、B-WER 50.93→45.66
- 消融：仅音频Domain Recall 22.8%、仅ASR 66.4%、音+文84.4%；Joint zero-shot已达Error Recall 75.6%/Domain 85.9%，ICL主要提升精度（46.7→51.9）；联合定位不损伤一遍WER；top-10优于top-50，低排候选引入噪声
**是否开源**：论文公开；所用组件均公开（Qwen3-Omni、ANE embedder-64与三数据集），本文未发布专属代码/Demo。

### ⭐ 评分：7/10
理由：片段作硬门控检索的想法干净、工程性强，全免训练即可部署，三跨域一致改善且消融充分。扣分：本质是SpeechLLM+ICL+ANE的组合创新，新颖度中等；仅英文三行业评测；两遍推理的时延与成本未量化讨论；未与训练充分的检索/排序模块正面对比。
## [3] A Comprehensive Study of Content Representations for Speech Synthesis

arXiv ID：2609.30975 | 方向：语音大模型
作者：Diego Torres、Axel Roebel、Nicolas Obin
机构：STMS Lab, IRCAM, CNRS, Sorbonne Université（法国巴黎）
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.30975 | PDF https://arxiv.org/pdf/2609.30975.pdf | 代码：暂无 | Demo：https://content-demo.diegotg2000.workers.dev/

### 📌 简介

本文提出一个无参考的生成式统一评测框架，系统比较 SSL 特征、k-means/RVQ 令牌、监督令牌、后验图谱与神经音频编码器等语音内容表示。生成模型仅以表示为条件且不含说话人信息，生成音频在内容、说话人身份、韵律三轴上量化评估。结果揭示两种机制：接近完整重建音频的表示，与有效剥离说话人身份的表示。关键发现是解耦并非仅靠监督实现，而是训练目标与信息容量交互作用的结果。

### 🔧 技术方案

**问题背景：** 语音内容表示广泛用于语音转换、语音翻译与多模态大模型，但以往基准将声学令牌与内容令牌混排，且缺乏在统一生成框架下直接度量各表示保留何种属性的方法。

**模型架构或实验设计：** 在 LibriTTS 上训练约 67M 参数的流匹配声学子模型（Vocoder），输入表示统一上采样至 100 Hz，ConvNeXt+U-Net 生成 100 维梅尔谱，经自训 Vocos 合成波形。评测表示涵盖 HuBERT/WavLM 第 6 层、k-means、VQ-VAE、VQ-ASR、PPG、Soft units、ContentVec、SpeechTokenizer 第一级，均工作于 50 Hz。生成模型绝不接触说话人 ID 或参考音频，任何说话人信息只能经由表示泄漏。指标含 dWER（Parakeet ASR）、 VoicePrivacy EER（ECAPA-TDNN 说话人验证）、性别探针准确率、F0 音高相关系数与音域误差（PENN），并以 UTMOS 监控音质。

**核心创新：** (1) 提出容量约束与训练目标共同决定解耦的机制性假说；(2) 通过对比连续与离散、监督与无监督的同容量变体，隔离量化与监督各自贡献；(3) 提供内容、身份、韵律三轴统一可比较的信息空间。

**训练策略或评测协议：** AdamW 学习率 1e-4、批大小 32、800k 迭代、单张 RTX 4070；推理用中点求解器 10 步、CFG guidance w=2.0、固定随机种子，并做了解码器容量（3 倍参数）与 guidance 稳健性验证。

### 📊 实验结果

**数据集**：LibriTTS（train.clean.100/360 训练，test.clean 评测，24 kHz）

- EER 接近随机：VQ-ASR 256 码达 46.6%、PPG argmax 43.0%，性别准确率回落至 ~53% 基线；HuBERT 连续特征仅 1.3% 保持高保真重建
- dWER：VQ-ASR 2.7% vs ContentVec 0.6%；量化容量减至 8 维后 EER 由 8.6% 升至 46.6%
- 码本规模影响：k-means 64→1024 码 EER 由 36.0%→32.4%，未跨机制；SpeechTokenizer 一级介于两机制之间
- guidance 提升可令解耦表示 UTMOS 反超原始重合成

**是否开源**：Demo 音频公开，代码未见正式开源仓库。

### ⭐ 评分：7/10

评测协议设计干净，去掉了说话人通道混淆，得出「监督须配瓶颈」「压缩与内容解耦」「码本规模次要」三条对语音令牌选定具直接指导意义的结论，消融充分。扣分点：生成质量受解码器限制只能给信息量下界，缺少主观听感评估，且为 IRCAM 单实验室中等规模工作。
## [4] CLEAR: Online Speech Content Leakage Estimation through Cross-ASR Disagreement

arXiv ID：2609.30415 | 方向：语音大模型
作者：Bhawana Chhaglani、Tanvi Kandepuneni（共同一作）、Jeremy Gummeson、Prashant Shenoy
机构：麻省大学阿默斯特分校（UMass Amherst）
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.30415 | PDF https://arxiv.org/pdf/2609.30415.pdf | 代码：暂无 | Demo：暂无

### 📌 简介
信号级语音隐私机制（如Kirigami语音抑制、低通滤波）在抑制语言内容的同时保留可用于活动识别的声学信息，但其实际泄露程度随话语与讲话者剧烈波动，如固定阈值0.5下敌方PER在0.45至1.0间变化。WER/PER等指标依赖真值转写，无法在部署时在线计算。CLEAR提出无参考的运行时泄露估计：当内容仍可恢复时，多个独立训练的异构ASR输出高度一致，内容被破坏则分歧增大，故用ASR两两分歧的均值作为泄露代理。在Common Voice上其与真值泄露Spearman相关达0.8，使隐私从离线固定配置变为可在线监测、向用户告警并动态调节的运行时属性。

### 🔧 技术方案
**问题背景：** 语音隐私变换的保护强度是输入相关的，离线聚合选参无法反映当前音频的残余可恢复性，而现有评估均需参考转写，部署场景不可得。
**方法：** 将隐私变换后的音频x'送入6个架构迥异的ASR（Wav2Vec2-base-960h、Whisper-small、Citrinet-1024、SpeechBrain CRDNN-RNNLM、Emformer-RNNT、Parakeet-TDT-0.6B），归一化假设文本后计算两两序列相似度，分歧定义为1减相似度并取全部组合的均值即为CLEAR分数，另统计空假设率；被两个以上ASR共同恢复的词标记为潜在泄露词。
**核心创新：** (1)首次将异构ASR间分歧作为无参考的内容可恢复性信号；(2)泄露词定位实现可解释隐私告警；(3)形成"估计-反馈-调节"闭环，支撑自适应隐私控制。
**细节：** 在Kirigami阈值0.3至0.9共13个操作点与低通滤波300/500/700Hz上验证；评测时留出最强敌方HuBERT-large（激进变换下平均PER最低0.936）计算真值PER；用保序回归把CLEAR校准为PER估计，按话语分组5折交叉验证。

### 📊 实验结果
**数据集**：Mozilla Common Voice抽取100条约2秒语音
主要指标
- 跨1300个话语-配置对Spearman相关ρ=0.80，操作点均值级ρ=0.98，话语内中位ρ=0.82
- PER校准MAE：保序回归0.162，优于线性0.172与均值基线0.316；判别PER≥0.7准确率82%
- 泄露词识别：阈值0.7时恢复42/74真值词（43.2%），共同词中61.3%确为泄露词
- 对比单ASR置信度：Wav2Vec2置信度与PER相关仅ρ=-0.626
- 延迟-精度：3个ASR组合ρ=0.807、RTF=0.15（2秒片段0.295s，T4 GPU），第4个ASR仅提升0.003
**是否开源**：论文暂未提供代码仓库链接

### ⭐ 评分：7/10
视角新颖，把ASR集成一致性巧妙转化为无参考隐私度量，直击信号级隐私机制"离线选参、在线失明"的真实痛点；评测设计严谨（留出敌方、分组交叉验证、系统消融与延迟权衡），结论可信度较高。不足：数据集仅100条英文语音、规模小，泄露绝对值的校准依赖离线敌方ASR，未实现端到端自适应隐私闭环实验，且对中文等多语言与更强LLM-based ASR敌手的泛化性未验证。作为运行时隐私感知系统方向的重要奠基工作，值得跟进。
## [5] Learning Natural Conversational Behavior in Tandem Speech-to-Speech Models with Randomized Guidance

arXiv ID：2609.30773 | 方向：语音大模型
作者：Manato Yaguchi、Yotaro Kubo、Hikaru Asano、So Kuroki
机构：Sakana AI（东京，日本）、东京大学（东京，日本）
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.30773 | PDF https://arxiv.org/pdf/2609.30773.pdf
代码：暂无 | Demo：暂无

### 📌 简介

串联式语音到语音（tandem S2S）架构如 KAME 用异步 LLM 后端在用户说话期间向前端持续推送候选回复作为引导流，从而兼得全双工交互的低延迟与文本 LLM 的知识能力。但监督微调需要中间引导轨迹，而真实对话录音只包含最终回复，KAME 原本要逐条样本调用模拟器 LLM 生成逐渐收敛到目标回复的引导序列，成为规模化使用真实语音的数据准备瓶颈。本文提出随机中间引导：训练时末位更新用目标回复文本作有效引导，其余更新位随机采样其他对话的回复作潜在无关引导，倒逼前端甄别后端信息。基于此在 3.8k 小时真实双人对话上训练 KAME，回复质量媲美各种引导构造基线，轮次衔接与音频自然度显著优于合成数据版本。

### 🔧 技术方案

**问题背景：** 级联 ASR-LLM-TTS 延迟破坏对话流畅性，Moshi 等全双工模型知识推理有限；KAME 让异步文本 LLM 以 2 Hz（每 0.5 秒）基于用户部分输入向全双工语音前端推送候选回复组成引导流（原文称"oracle"流）。训练时普通对话数据缺少该中间引导，原方案需对每条训练对话逐例 LLM 模拟生成收敛到目标回复 y 的引导轨迹，无法扩展到大规模真实语料。

**模型架构：** 前端为预训练 Moshi 全双工 S2S 模型，推理后端为 GPT-4.1，按用户转录前缀每 0.5 秒推送预计算引导并附加 6 帧（0.48 秒）固定模拟延迟；本方法仅重造训练期引导流构造方式，推理接口完全不变。

**核心创新：** (1) 随机中间引导：每个回复段末位更新保留目标转录 y 作信息性引导，其余更新位从按 token 序列去重、长度限定为 y 的 0.5 至 2 倍且剔除当前对话回复的池中超均匀无放回采样，可视作负采样，使前端学会只利用有用引导；(2) 全自动化真实对话数据流水线：基于 PodcastIndex，经 Silero VAD、pyannote diarization-3.1 分离、Sidon 语音增强、DNSMOS P.835（OVRL≥3.0）过滤、faster-whisper large-v3-turbo 转写并对齐 token 级时间戳、语言概率≥0.85、平均对数概率≥-0.4，筛出恰含两位说话人的分段按时序背靠背拼接，得 3.8k 小时英文双人对话（约为 1.36k 小时合成语料的 2.8 倍）；(3) 与 LLM-generated、MiniLM 相似度检索、Target-only 三种引导构造策略的系统对比与消融。

**训练策略：** 同一 Moshi checkpoint 全参数微调 1 epoch，全局 batch size 32，temporal 与 depth transformer 学习率分别 2e-6 与 4e-6；真实数据模型取 3000 更新 checkpoint。

### 📊 实验结果

**数据集**：spoken MT-Bench 子集（30 题、每题 2 轮）测回复质量，MTR-DuplexBench 衍生平滑轮次/打断/停顿三任务（200 段十轮对话×3 种子）测会话行为，Gemini 3.1 Pro 作音频评委测自然度。
- 合成数据 MT-Bench：Randomized 6.09±0.05，Similarity 6.14±0.05，LLM-generated（KAME）5.54±0.03，Target-only 5.12±0.03
- 真实数据模型 MT-Bench：5.04±0.21，对比合成 KAME 5.54、Moshi 1.96±0.01
- 平滑轮次成功率：50.88%（真实）对比 40.62%（合成 KAME）、36.75%（Moshi）；打断：17.77% 对比 19.28%、23.93%；停顿：81.08% 对比 80.20%、74.62%
- 音频评委自然度：4.79±0.32（真实）对比 4.05±0.14（合成 KAME）、5.29±0.22（Moshi）

**是否开源**：论文未给出代码与 Demo 链接，暂无开源。

### ⭐ 评分：7/10

把"随机无关引导"视为负采样的洞察直击串联式训练数据无法规模化的核心痛点，方法极简且免逐例 LLM 模拟；3.8k 小时真实对话实验清晰验证了在保住对 Moshi 约 3 分 MT-Bench 优势的同时，自然度从 4.05 提到 4.79、平滑轮次从 40.62% 提到 50.88% 的可控权衡。不足：评价仅 30 题 MT-Bench 子集，统计显著性有限；自然度仍不及 Moshi，打断处理未改善且缺乏显式停止响应训练目标；无代码/Demo 开源，创新偏增量式工程。
## [6] Who Says What: Symbolic Trimodal Binding Mechanisms in Audio-Visual LLMs

arXiv ID：2609.31193 | 方向：语音大模型
作者：Jihoo Jung、Youngjoon Jang、Joon Son Chung
机构：KAIST（韩国科学技术院）、牛津大学 VGG 视觉几何组
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.31193 | PDF https://arxiv.org/pdf/2609.31193.pdf | 代码：暂无 | Demo：暂无

### 📌 简介

本文系统研究音视频大模型（AVLLM）在多说话人对话视频中如何完成"文本-语音-视觉"三模态符号绑定。作者发现模型涌现出模态特异的符号ID机制：听觉属性被编码为记录说话时序的时间ID，视觉属性被编码为记录画面位置的空间ID，绑定经锚点ID提取、目标ID选择、特征检索三阶段完成。借助表征相似性分析（RSA）与因果中介分析（CMA），作者定位绑定失败主要发生在目标ID选择阶段，即音-画对齐的根本缺陷，并提出基于现成主动说话人检测（ASD）的红框提示方法，免训练即在对话基准上提分，配合少于300步LoRA微调进一步泛化到通用AV基准，为"who says what"难题提供了机制解释与可落地的修复路径。

### 🔧 技术方案

**问题背景：** video-SALMONN2+（7B）、Qwen2.5-Omni（3B/7B）、MiniCPM-o-4.5（9B）等AVLLM在单镜头多说话人视频（画面每帧同时出现多个候选人）中频繁把话语归属到错误人脸。LLM/VLM的一模态与双模态绑定已被证实使用内容无关的符号ID，但AVLLM的三模态绑定机制与失败位置仍是黑箱。

**方法：** 作者构造4只动物说话人分布在四象限、各说一个随机国家名的玩具数据集，定义AAVR（声音锚点检索视觉目标）与VAAR（视觉锚点检索语音内容）两个双向绑定任务。先用上下文priming诱导正确绑定，对每层注意力输出做RSA，与时间ID、空间ID、语义内容三个假设空间算皮尔逊相关（800样本汇总）；再用CMA交换时间ID、空间ID或注入新颖语义做跨运行patching，以CM分数检验因果性（960样本）；最后在unprimed设定下通过primed-unprimed表征差距与头部级CAI因果干预定位瓶颈，并用现成ASD模型在每帧给主动说话人叠加红框做视觉提示，辅以400条人声合成视频、LoRA rank16、单卡A6000、不足300步的微调（ASD-FT）。

**核心创新：** 1）首次揭示AVLLM采用模态特异符号ID的三模态绑定——声音映射时间ID、画面映射空间ID，并在抽象符号空间完成跨模态链接；2）提出并双重验证"锚点ID提取—目标ID选择—特征检索"三阶段机制，各阶段对应明确层区间（锚点提取在中后层、目标选择在后层、特征检索在最深层）；3）精准诊断失败瓶颈为目标ID选择即音-画对齐缺陷，据此给出训练免费的ASD红框提示及轻量微调方案。

**协议：** 机制可解释性研究（RSA+CMA+因果干预）与7个基准的ASD/ASD-FT消融评测协议。

### 📊 实验结果

**数据集**：机制分析用玩具四说话人视频及SocialOmni真实2000条双说话人clip；评测含AVSpeaker、DailyOmni、SocialOmni、DiaDemBench四个对话中心基准和OmniBench、DAVE、WorldSense三个通用基准。

主要指标：
- Qwen2.5-Omni(7B) AVSpeaker准确率：44.86% → 45.59%（+ASD）→ 48.79%（+ASD-FT）
- Qwen2.5-Omni(7B) DailyOmni准确率：64.33% → 64.66% → 71.09%
- Qwen2.5-Omni(7B) SocialOmni准确率：38.95% → 41.90% → 44.25%（对话中心平均提升9.7%）
- MiniCPM-o-4.5(9B) DiaDemBench ASR：7.4 → 10.8 → 30.9（REF：6.3 → 9.7 → 24.8）
- video-SALMONN2+(7B) AVSpeaker：44.74% → 44.65% → 49.10%；OmniBench：37.04% → 44.92%、三微调增益7.9%
- Qwen2.5-Omni ASD免训练在SocialOmni即+2.95个百分点

**是否开源**：正文与附录均未给出代码/Demo仓库链接，玩具数据、400条微调语料与评测脚本暂未见公开释放，承诺程度不明。

### ⭐ 评分：7/10

理由：机制层面贡献扎实——RSA与CMA双证据链首次把LLM/VLM符号绑定结论扩展到AVLLM三模态，并把"who says what"失败归因到音-画对齐阶段，头部级干预显著恢复准确率，诊断-修复逻辑闭环完整；ASD红框提示零成本、三模型七基准一致收益，微调不足300步即可泛化到通用基准，工程价值高。扣分点：机制验证主要依赖受控玩具数据（4说话人、动物合成视频），真实场景相关性被相关系数量级衰减削弱；免训练ASD在video-SALMONN2+与Qwen的DiaDemBench/通用基准上无收益甚至轻微下降，修复手段对模型能力敏感；方法本身（外接ASD+画框）创新性中等，且未开源复现资产。
## [7] Training-Free Pronunciation Transcription via Text-Constrained Acoustic Rescoring

arXiv ID：2609.30924 | 方向：语音大模型；作者：Hikaru Asano、Yotaro Kubo、So Kuroki；机构：东京大学、Sakana AI；发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.30924 | PDF https://arxiv.org/pdf/2609.30924.pdf | 代码：暂无 | Demo：暂无

### 📌 简介

发音转写（由语音与文本恢复实际读音）是规模化构建TTS训练数据的关键环节。纯G2P只用文本、纯S2P只用音频，信息均有缺失，而联合语音-文本的ST2P模型又依赖昂贵的发音标注。本文提出免训练ST2P流水线：文本侧用词典、形态分析与G2P生成受限候选读音，音频侧用冻结预训练S2P模型对整句NLL重打分，经从左到右贪心搜索、双评分器级联与带裕度检查选出最优读音组合。日语三语料CER降至0.04–0.17%，超越已训练ST2P与商用多模态大模型，贪心搜索比beam快3–3.5倍，并在西班牙语、法语、英语上验证泛化。

### 🔧 技术方案

**问题背景：** 日语同形异读现象突出（如"明日"有asu/ashita/myōnichi），TTS数据标注需低成本低错，ST2P训练却要求（音频、文本、发音）三元组，标注成本远高于普通转写。

**方法：** 将转录w经形态分析切成N个span，每个span由词典/G2P/规则给出候选读音集，并取文本最可能的默认读音；完整读音序列送入冻结S2P模型算整句负对数似然S(y,x)=−log p(z(y)|x)，最小化J=S+P。为避免候选空间指数增长，采用从左到右贪心搜索：每个span只访问一次，已定span固定、后续span取默认。主评分器为320M参数wav2vec2.0假名CTC模型，二级为810M自回归kana-whisper，融合分L1+λL2（λ=1）；级联策略仅在第一趟改动过默认读音时用融合分重搜，kana-whisper侧对多拼写最多求和16个teacher-forced似然并缓存cross-attention。最后做裕度检查：从左到右重访被改动span，若相对默认读音的收益不足每符号τ=0.6（τ按长度ℓj=max(1,|r̃j|,|rj0|)缩放）则回退；仅孤立词分析得到的候选加0.03·m·n_ctc罚。

**核心创新：** (1)词汇约束候选+冻结声学模型纯推理侧融合，零训练、零三元组标注；(2)整句NLL联合打分而非逐span判决，保留上下文声学证据；(3)贪心+级联+裕度检查在精度与RTF间取得帕累托改进。

**协议：** 日语在JVS-dev、JSUT、JVS-par各取512条共同语句评归一化假名CER，转录分别用参考文本与Whisper large-v3输出；λ、τ及拼写上限在JSUT/JVS-par各1000条校正集标定后迁移至JVS-dev。

### 📊 实验结果

**数据集**：JVS-dev/JSUT/JVS-par（日语），DIMEx100/Rhapsodie/Buckeye（西/法/英）

- 参考文本CER：级联0.15/0.17/0.04%，纯文本基线0.85/1.40/0.60%，提升约4–20倍
- ASR文本CER：0.64/0.65/1.58%
- 对比训练型ST2P：Furigana Whisper加词表约束为0.21/–/0.15%，本方法更优且无需训练
- 对比商用：Gemini 3.5 Flash为0.50/0.59/0.84%；开源MLLM差，Qwen3-Omni 8.13%、Phi-4-multimodal 61.48%
- 效率：贪心比beam（B=5）快3–3.5倍且CER相当；级联比kana-whisper直接解码快2倍（H100）
- 消融：去裕度/去级联CER升≤0.022/0.016点；换无关或静音音频CER暴涨至12.4–16.2%，证明声学证据必要；距贪心oracle仅0.042–0.107点，回收87–96%增益
- 多语言PFER：西2.38、法4.11、英13.21（最佳配置），超4个开源MLLM，距顶级Gemini差≤0.4点

**是否开源**：论文开源（CC BY 4.0），代码与Demo暂无；所用S2P/G2P资源均为公开模型与词表。

### ⭐ 评分：7/10

理由：工程价值突出，免训练方案在日语注音上全面超越已训练ST2P与商用多模态大模型，且RTF低、消融扎实（oracle差距分析说服力强）；贪心近似的局部性假设被beam实验反向验证。弱点是方法学新意有限，本质是词表约束+CTC/AR联合重打分的成熟范式系统化组合；评测以日语为中心，跨语言仅PFER小幅领先、英语结果预初性，收益强依赖词表与评分器匹配。对TTS数据生产实用性强，理论贡献中等。
## [8] I-Parakeet: Integer-Only Conformer ASR on Mobile NPU
arXiv ID：2609.30846 | 方向：语音大模型
作者：Taichi Nishimura
机构：Sony Interactive Entertainment（日本东京）
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.30846 | PDF https://arxiv.org/pdf/2609.30846.pdf
代码：暂无 | Demo：暂无
### 📌 简介
本文提出I-Parakeet，将NVIDIA 0.6亿级参数（0.6B）的Parakeet-CTC Conformer语音识别模型改造为完全整数推理实现，首个在消费级手机NPU上运行且无任何浮点算子与CPU回退的现代Conformer ASR。以往量化模型在归一化、softmax、Swish等数值敏感处仍需反量化回FP16/FP32，无法吃满整数加速器。作者重新推导相对位置自注意力的整数形式，用minimax方法逼近Swish，并按层激活域分析做INT8/INT16混合量化。在Nothing Phone (3a)上取得4.97% WER、实时率RTF 0.048，较CPU基线快7.5倍，证明大型Conformer无需浮点推理。
### 🔧 技术方案
**问题背景：** Parakeet-CTC-0.6B含24层Conformer块，FP32权重超2.4GB，边缘设备内存/时延/功耗难以承载；INT8权重虽可压到600MB，但既有量化方案在LayerNorm、softmax、Swish与相对位置注意力处回退浮点，手机NPU（仅整数算力）无法端到端承接。
**方法：** 全网络采用均匀对称量化，激活每张量一个尺度、权重每通道一个尺度，以LibriSpeech dev-other校准；矩阵乘INT32累加后经离线定点乘子m（2^16移位）重量化，BatchNorm折入深度卷积，LayerNorm与softmax沿用I-BERT整数核。
**核心创新：** (1)整数相对位置自注意力：内容分支与位置分支标定尺度不同（Sc与Sp）无法直接相加，将双分支尺度转换、相加与1/√dk缩放融合为单次重量化，相对移位仅搬运数值，故对整数张量直接施加以静态索引图实现，位置投影作INT8常量离线存储；(2)minimax整数Swish：不再最小二乘拟合tanh，而是直接最小化Swish输出最大误差，求得a*=-0.1240、c*=2.4632（最大误差0.039，对比L2拟合tanh的0.073）；(3)逐层激活域分析：BatchNorm各通道缩放系数max/median比值达4个数量级（10759），故其输出单独用INT16网格；pre-encoder激活max/p99.9达11-21倍重尾，采用99.9百分位截断校准，编码器仍用min-max。
**量化与部署细节：** 基于Qualcomm QNN SDK（QAIRT 2.47），NPU要求静态形状，按3-35秒输入长度编译多档计算图并按 utterance 选最小图，静音填充致帧数+23%且已计入RTF；除BatchNorm输出为INT16外其余全部INT8。
### 📊 实验结果
**数据集**：LibriSpeech（test-clean/test-other）、Common Voice（test），校准集dev-other，真机为Nothing Phone (3a)（骁龙7s Gen 3）。
主要指标
- WER（真机test-other）：4.97%，较FP32的3.76%仅损失1.21点；仿真版5.32%
- WER（test-clean/Common Voice）：2.61%/14.70%，优于I-BERT配方7.41%/19.05%与Naive INT8的6.38%/16.54%
- RTF：0.048，较CPU FP16 parakeet.cpp（0.36）快7.5倍，峰值内存612MiB，省60%
- 消融：全用p99.9反劣化至8.03%，Hybrid缩放5.32%；per-channel INT16不可部署（5.29%），per-tensor INT8为5.91%
- 对照：高通stock工具链FP16与INT8 PTQ真机均WER 100%失败
**是否开源**：代码暂未公开，模型基于NVIDIA开源checkpoint Parakeet-CTC-0.6B。
### ⭐ 评分：7/10
理由：工程完成度高，是首个在真实手机NPU上端到端跑通0.6B Conformer的纯整数方案，整数注意力融合与minimax Swish推导干净，逐层域分析加消融把每个设计选择的WER贡献量化清楚，stock工具链100%失败的对照极具说服力。不足在于单篇作者、仅验证英文LibriSpeech/CV两集与单一高通NPU，真机WER损失1.21点且0.6B模型精度天花板受限，无开源代码，亦未对比更大模型或流式场景，属扎实的系统性增量工作而非范式创新。
## [9] Inference-Time Target Speaker Unlearning in LLM-Based Automatic Speech Recognition

arXiv ID：2609.30439 | 方向：语音大模型
作者：Bo Su、Yueru Yan、Thai Le
机构：Indiana University, Bloomington, USA
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.30439 | PDF https://arxiv.org/pdf/2609.30439.pdf
代码：暂无 | Demo：暂无

### 📌 简介

本文首次提出面向多说话人会议转写的"目标说话人遗忘"任务（TSU-ASR）：给定会议音频与若干选择退出（opt-out）说话人的短语音注册样本，要求系统在转写时剔除这些人的言语内容，同时保留其他说话人的转写精度，并继续通过说话人日志标注"谁在何时说话"。针对现有平台无法让参会者在不离场的前提下动态排除AI转写的需求，作者提出轻量即插即用的注册条件门控模块（ECG），挂载到冻结的双流语音LLM（TagSpeech）上，仅需训练ECG本身，推理时可对从未见过的新退出说话人免重训地动态生效。在AMI英文与AliMeeting中文会议数据上，退出词/字转写正确率显著下降而保留说话人误差基本不变。

### 🔧 技术方案

**问题背景：** 在线会议的AI转写需尊重部分参会者的隐私退出意愿。传统方案均有缺陷：录制后按说话人过滤是事后补救且在语音重叠时会误删他人内容；部署前重新训练成本高且不适应推理期间动态出现的退出请求。与目标说话人ASR（只转写选定者）相反，TSU-ASR要转写除退出名单外的所有人，同时保留其发声时间戳以区分"被省略的语音"与"沉默"。

**方法：** 基座为TagSpeech——两个Zipformer编码器分别提取语义（内容）流与声纹（说话人）流，经投影器送入Qwen2.5-7B生成含说话人标签与时间戳的XML格式文本，全部参数冻结。ECG模块利用与声纹编码器同空间的帧级特征与各退出者注册嵌入（短语音特征平均归一化），经两层MLP输出[0,1]连续匹配分数，多目标时取最大值，再用该分数逐帧乘性抑制语义流，声纹流保持不变以维持日志能力。训练仅优化ECG：以0.5概率随机选录制内说话人为目标并从参考文本中删除其话语（保留标签与时间），另含未见说话人负样本；损失为α·CE+β·BCE（α=β=1.0）。

**核心创新：** (1) 首次定义推理时端到端多说话人目标遗忘ASR任务，兼顾内容清除与日志完整性及重叠语音下双目标的竞争关系；(2) ECG通过门控抑制内容流而保留说话人流，实现对未见退出者零重训的即插即用；(3) 连续分数门控可反向传播，训练轻量、易于迁移到其他语音LLM。

**协议/细节：** 0.5–80秒语音段，AMI-SDM得2607段、AliMeeting远场首通道4373段；测试集约10%时长（AMI 16人、AliMeeting 60人，训练测试说话人零重叠），每次随机取25%说话人退出、重复10次平均，每个退出者用5条3–8秒孤立语音段注册。

### 📊 实验结果

**数据集**：AMI（英文）、AliMeeting（中文）
主要指标：
- CLR-all（AMI，越低越好）：72.3%→48.2%
- CLR-all（AliMeeting）：73.6%→27.3%
- CLR-rare 降幅：AMI 25.4%、AliMeeting 42.7%
- 保留侧 cpWER（AMI）：48.9→50.1（+1.2）；cpCER（AliMeeting）：49.1→51.4（+2.3）
- Forget-only 段 CLR-all：AMI 86.0→48.1、AliMeeting 89.0→16.9
- Mixed-overlap 保留侧仍有退化：AMI cpWER 62.7→65.6、AliMeeting cpCER 56.9→65.5
- 局限：AliMeeting Mixed-nonoverlap 组保留误差大幅上升（cpCER 18.6→45.7），重叠抑制与清除不彻底（信息仍泄漏至冻结LLM），且无与既有遗忘/抑制基线的定量对比。

**是否开源**：论文未提供代码仓库链接，暂无开源承诺。

### ⭐ 评分：6/10

理由：任务定义是真实且有价值的新颖贡献（隐私退出+日志完整性+重叠约束），ECG设计简洁、冻结主干仅训门控，训练/推理均轻量并对未见说话人泛化，英中双语会议数据验证较全面，实用意义明确（视频会议场景）。但效果仍是部分抑制远非"遗忘"——英文CLR仅降到48%，混合重叠段保留侧误差上升明显，中文非重叠混合组近乎失效；缺少与activation redirect、embedding-corruption等推理时遗忘方法的直接对比，亦未开源，可复现性与结论强度打折扣。整体是扎实的任务开创性工作（first step定位清楚），方法深度有限，故给6分。
## [10] Tracing and Relearning Detection Evidence in Text-to-Speech Systems

arXiv ID：2609.30983 | 方向：语音大模型
作者：Eunji Shin、Kyudan Jung、Jihwan Kim、Minwoo Lee、Jaegul Choo
机构：梨花女子大学、KAIST AI
发布日期：2026-09-28
论文 https://arxiv.org/abs/2609.30983 | PDF https://arxiv.org/pdf/2609.30983.pdf
代码：暂无
Demo：暂无

### 📌 简介
F5-TTS 声学模型加大模型声码器两阶段 TTS 中，深度伪造检测证据究竟来自哪一级，此前无人归因。本文用固定声码器的受控重合成把检测证据主要归到声学生成级，并发现对抗微调声学模型（目标不含检测器）会抬高固定检测器 EER、削弱证据；但仅用微调输出适配检测器后，EER 从 19.42% 降至个位数，还能迁移到未见过的基模型输出，说明证据并未消失，只是检测器没学到，为"生成-检测博弈须持续再训练"提供直接实证。

### 🔧 技术方案
**问题背景：** 现有基准混合声学模型、声码器、语料与信道因素，低 EER 无法定位证据来源；已知真实 mel 经声码器重建本身可分，故需隔离 TTS 各级贡献。
**方法：** 对同一源语音构造五条件差分归因：纯重采样 R、真实 mel+BigVGAN 重建 V、基 F5-TTS 合成 T、对 T 做 RMS 增益匹配 TG、微调后 FT。微调 337.1M DiT 全部参数，冻结 BigVGAN 但保持可微使波形域判别器梯度回传；判别器为 5 个多周期（2,3,5,7,11）加 3 个多分辨率（FFT 2048/1024/512）组合，采用 HiFi-GAN 最小二乘对抗损失与特征匹配，权重 1:2，无 mel 重建损失，真实样本用真实 mel 的重建，评估检测器完全不在目标中；再以 XLS-R SLS 公开权重继续训练 2000 步（批 14、3 种子），FT 配对其提示源真语音作配对训练。
**核心创新：** (1) 固定声码器配对重合成首次定量将检测证据归到声学生成级，并显示 V 级分离强度依赖声码器（BigVGAN EER 38.00% vs Vocos 12.00%）；(2) 无检测器反馈的声学模型对抗微调在 3 个检测器上全向抬高 EER 且质量不降；(3) 仅见 FT 假样本的适配检测器同时改善 T 检测。
**协议：** LibriSpeech train-clean-100 微调 1800 步（4×A100，批 8，32 步 Euler 采样），选质量不劣于基线的最后检查点，检测器 EER 不参与选择。

### 📊 实验结果
**数据集**：LibriSpeech（800 句 test-clean/40 人）、VCTK（1354 段/68 人）、VoxPopuli（800 句）、ASVspoof 2019/2021 与 In-the-Wild。
主要指标
- 基线固定 SLS EER：T 15.46%（LibriSpeech）/3.45%（VCTK），FT 19.42%/4.09%，AASIST-L 对 FT 达 47.67% 近随机
- EER 提升幅度 0.64–18.92 个百分点，全部超生成种子波动；RMS 增益匹配仅解释 52%（SLS）/30%（Mamba）差距
- 检测器适配后 FT EER：LibriSpeech 适配降至 1.71%，VCTK 适配降至 7.46%，且未见过的 T 同步降至 1.42%/5.92%
- 传统基准：DF 1.90% 保持，LA 8.35%（LS 适配）/3.35%（VC 适配），In-the-Wild 10.66%/9.53%（原 7.46%）
- 质量不变：UTMOS 3.35–3.45、WER 0.68–2.95%、说话人相似度约 0.72–0.76
**是否开源**：代码与微调模型未发布，论文页无链接，标注"暂无"。

### ⭐ 评分：6/10
归因实验设计干净（五条件差分+增益对照+多检测器/前端交叉验证），结论对深度伪造检测社区有直接政策价值：EER 升高不等于不可检，再适配可恢复甚至更好。局限是仅一个声学模型、一个声码器、一种检测架构，适配集仅 20 说话人约 2600 条，传统基准性能有回涨，外推性受限，属方法学上严谨但覆盖面窄的诊断型增量工作。
## [11] Symbiotic Architecture for Post-Hoc Audio Extension of Frozen Language Models

arXiv ID：2609.30784
方向：语音大模型
作者：Yotaro Kubo、Qi Sun、Yujin Tang
机构：Sakana AI（东京，日本）
发布日期：2026-09-28
论文：https://arxiv.org/abs/2609.30784
PDF：https://arxiv.org/pdf/2609.30784.pdf
代码：暂无
Demo：暂无

### 📌 简介

传统音频语言模型采用一体化架构，将音频嵌入直接送入骨干大模型做预填充，存在两大缺陷：预填充开销随模型规模线性增长，且音频指令微调引发灾难性遗忘。本文提出共生架构，通过注入器模块把音频条件化向量逐层直接写入冻结大模型的KV缓存，使纯文本LLM在不更新任何权重的情况下转化为音频语言模型。音频注入成本仅由注入器宽度决定，与骨干规模解耦。实验显示该外挂式设计在ASR、音频问答与声学场景分类上大幅超越仅调输入的SLM基线，逼近LoRA微调参考模型，同时文本基准成绩完整保留，长音频鲁棒性显著。

### 🔧 技术方案

**问题背景**：一体化ALM中音频嵌入须由骨干LLM自身转换为KV缓存，预填充成本与Llama级大模型宽度成正比；有监督音频微调导致灾难性遗忘，需复杂多任务数据配比才能缓解，推理与训练成本俱增。

**模型架构**：整体由语音编码器、注入器与冻结LLM三部分组成。编码器采用预训练WavLM-Large，注入器层数与骨干一致，内部为基于Conformer中LConv模块的堆叠CNN（深度可分离卷积核长15、通道维2048，归一化改用RMSNorm以稳定小批量训练）。适配器块以步长8的最大池化降采样，再用两个仿射变换映射为各层键值向量。注入器参数551M，音频预填充激活参数由一体化方案的1108M降至551M，总参数1303M，骨干选用Qwen3-0.6B。

**核心创新**：(1) KV缓存直写机制：将音频适应问题重构为逐层生成输入相关的键值缓存，绕开骨干计算，注入成本慢于全骨干预填充增长；(2) KV尺度匹配：用Qwen3对应层RMSNorm参数初始化键尺度、以少量校准句统计值向量标准差初始化值尺度，并加每头缩放因子，保证注入向量获得足够注意力分数，避免早期梯度消失；(3) 噪声RoPE训练：对位置编码引入随机偏移（τ均匀取自0至256）与随机时间缩放（κ取自0.75至1.5），在不微调骨干的前提下修复RoPE对未见序列长度的过拟合。

**训练策略**：骨干LLM完全冻结，仅训练注入器，编码器加LoRA（r=64、α=64）。训练数据共约1302小时：LibriSpeech 960小时（混合权重90%）做ASR，CompA-R 159小时、Clotho-AQA与DCASE2025 Task5各7.4小时做音频问答、CochlScene 169小时做场景分类（各2.5%）。LibriSpeech按40%概率做1.1x/0.9x变速扰动，超过25秒语句剔除。AdamW训练8万步，batch size 64，余弦调度峰5e-4、谷5e-6，2000步预热，以dev-other WER选模。

### 📊 实验结果

**数据集**：LibriSpeech、Clotho-AQA、CochlScene、WikiText-2、HellaSwag、GSM8K

主要指标：
- LibriSpeech WER（dev-clean/dev-other/test-clean/test-other）：Symbiotic 1.91/3.73/2.07/3.91，优于Encoder-only的2.22/4.07/2.33/4.25，接近Monolithic的2.16/3.68/2.26/4.01
- Clotho-AQA错误率：Symbiotic 47.1 vs Encoder-only 62.6 vs Monolithic 45.4
- CochlScene错误率：Symbiotic 41.7 vs Encoder-only 52.9 vs Monolithic 32.7（CNN注入器是差距来源）
- 预填充速度（H100，batch 4）：Symbiotic 157.1秒 vs Monolithic 199.8秒，快约21%
- 文本任务保留：冻结LLM的GSM8K为57.8，音频微调后暴跌至2.0，HellaSwag从47.3降至38.2；Symbiotic按构造与冻结版完全一致
- 消融：长语料WER从架构原始的120.68降至加噪声RoPE后10.49，再加KV尺度匹配降至4.70

**是否开源**：论文未提供代码与模型链接，暂无开源承诺。

### ⭐ 评分：6/10

动机明确且工程价值高：KV直写+冻结骨干一次性解决预填充可扩展性与灾难性遗忘，噪声RoPE与尺度匹配两项消融扎实，长音频WER改善10倍极具说服力，且可复用现有LLM推理基建。扣分点：仅在0.6B紧凑骨干上验证，规模化优势未经大模型证实；非语音音频任务明显落后微调基线；单语英文实验、无开源；架构思想与LLaMA-Adapter重叠度较高。属于思路干净、落地潜力大的实用型增量创新。

---

## 语音前端

## [12] Adapting Personalized Speech Enhancement for Low-Latency Audio-Visual Target-Speaker Extraction

**arXiv ID**：2609.30631 | **方向**：语音前端  
**作者**：Rayhan Rashed、Senja Filipi、Ross Cutler  
**机构**：Microsoft、University of Michigan  
**发布日期**：2026-09-28 | **论文** https://arxiv.org/abs/2609.30631 | **PDF** https://arxiv.org/pdf/2609.30631.pdf  
**代码**：暂无  
**Demo**：暂无

### 📌 简介
本文提出 AV-PVQE，反向的思路是从个性化语音增强模型 PVQE 出发适配到在线音视频目标说话人提取（TSE）。PVQE 虽输出音质高，但在双人混合中有 46% 的概率错误恢复竞争说话人（目标混淆）。作者在 PVQE 的说话人条件输入上引入 AV-HuBERT 唇动特征并与注册向量以门控残差融合，联合微调视觉网络与重建网络，将目标混淆降至 1.6%，且无未来帧、算法延迟仅 20 ms。在 LRS3、VoxCeleb2 合成混合与 AMI、MCoRec、MTM 真实会议上的客观指标与个性化 P.835 听音测试均显著优于从零训练的视听提取器 AVASE。

### 🔧 技术方案
**问题背景：** 现有在线视听 TSE 模型多从零训练、只在合成双人混合上评估，监听音质与真实会议行为缺乏验证；而个性化语音增强模型音质好却在混合中频繁选错目标说话人。

**模型架构：** 以预训练 PVQE（DeepVQE 个性化版，含 STFT、卷积编码、条件 GRU、子像素解码与复数掩码）为声学主干，冻结其注册编码器输出 176 维向量；新增 AV-HuBERT 卷积视觉编码器提取 88x88、25 fps 唇部裁剪特征，经两层 256 维 ReLU 投影到 176 维。总参数 12.79M，仅 0.40M 为新增。

**核心创新：** (1) 门控注册残差融合：用累积均值视觉 cues 与注册向量的 sigmoid 门控残差 r(e) 组合成条件向量 c_t=b_t+g_t⊙r(e)，W2/a2 零初始化保证训练起点等价纯视觉条件注册编码器全程冻结；(2) 在线因果化改造：整段 cues 聚合换成 running mean，解码器时域卷积重映射为仅用当前及过去帧、新过去抽头零初始化，跨 chunk 携带音频状态，视觉只看当前帧加前 4 帧，实现零未来帧、20 ms 算法延迟（符合 ICASSP 2023 DNS 限制）；(3) 分阶段联合微调：先训视觉条件，再加注册残差，最后视觉路径+融合层+声学网络整体微调，负 SI-SNRi 为损失，Adam， lr 1e-3，末级 30 epoch、batch 16，按安静目标验证集选第 29 epoch。

**训练策略：** 用 LRS3 与 VoxCeleb2 各生成 40000 对两说话人混合（TIR -10~10 dB），测试各 3000 对固定混合，说话人与训练集不重叠。

### 📊 实验结果
**数据集**：LRS3、VoxCeleb2（合成双人混合），AMI、MCoRec、MTM Teams 会议（未再微调直接泛化测试）。  
主要指标：
- SI-SNRi：LRS3 上 AV-PVQE 9.03 dB（AVASE 8.72，PVQE -2.31）；MTM 上 9.64 dB（AVASE 3.06，+6.58 dB）
- 目标选择率 Picked：LRS3 98.38%，各响度水平均 ≥97%；4 人会议组 75.00% vs AVASE 56.82%
- 词准确率 WAcc：AMI 68.27%（AVASE 50.14），MTM 67.65%（AVASE 49.56）
- 个性化 P.835 OVRL：AMI 2.68 vs AVASE 2.11（+0.57），MCoRec 1.85 vs 1.22（+0.63），与 PVQE 差异不显著（-0.06/+0.17）
- 保护/抑制测试：目标独讲时长时过抑制事件 7 次（PVQE 142）；目标静默静止视频下抑制竞争 32.83 dB（AVASE 2.25）

**是否开源**：论文与代码均未公开释出，仅基线 AVASE 使用其发布 checkpoint。

### ⭐ 评分：8/10
理由：视角新颖——不从零建 TSE 而是反向适配高质量增强模型，直击目标混淆与会话音质的实际工程痛点；20 ms 零 lookahead、已验证严格因果流式，可直接落地视频会议；评测覆盖合成+三个真实会议语料，含听音实验、保护/拒绝测试，且泛化到多于微调人数的 3-4 人场景，方法论扎实。扣分在于未报告设备端计算耗时与端到端延迟，未消融视听/增强的各自贡献（作者自认 future work），模型与数据不开源，且仅在双人混合上微调。
## [13] Dialogue-Based Streaming Audio-Visual Target Speaker Extraction with Predictive Dialogue Information

arXiv ID：2609.30774 | 方向：语音前端
作者：Shuhan Zhang、Wenxuan Wu、李海洲（Haizhou Li，通讯作者）
机构：深圳 loop 区研究院；香港中文大学（深圳）人工智能学院；香港中文大学
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.30774 | PDF https://arxiv.org/pdf/2609.30774.pdf
代码：暂无
Demo：https://jjjjiaozi.github.io/TS-VAP/

### 📌 简介
面向面对面实时对话场景，系统需在自然停顿、轮换与 backchannel 中持续追踪目标说话人，同时抑制对话伙伴与无关第三方插话。本文构建了首个基于完整双人类对话并叠加独立第三方干扰的在线流式音视频目标说话人提取（AV-TSE）基准，保留真实轮换结构而非模拟拼接。并提出基于语音大模型的目标说话人语音活动预测模块 TS-VAP，从重叠混合的语义、声学与面部线索中预测目标与对话伙伴的未来活动，作为预测性上下文引导低延迟流式分离器，与历史、同步上下文融合，显著改善轮次边界处的提取鲁棒性。

### 🔧 技术方案
**问题背景：** 现有 AV-TSE 多在完全重叠或人工模拟稀疏重叠混合上评测，缺乏真实对话的轮换结构；流式模型不可见未来帧，目标在轮次边界沉默处歧义最大。传统语音活动投影（VAP）仅在干净单通道训练，靠停顿与韵律预测，未利用决定轮换的语言知识（提问预示回答、句满即交接）。

**模型架构：** 将 speech-LLM Mini-Omni2（Qwen2-0.5B 骨干）改造为 TS-VAP：Whisper 编码混合音频、CLIP 编码目标人脸，Qwen 输出视觉条件化音频表征并与 CLIP 特征融合，轻量因果头输出 25Hz、256 维预测序列，每帧对目标与伙伴未来 2s 联合活动做 2^8=256 状态分类。分离端对比三类上下文：历史（GRU 自注册）、同步（ASD 特征）、预测（近 2s TS-VAP 特征池化为 ≤10 token，经 4 头交叉注意力查询）。

**核心创新：** (1) 首个保留自然轮换的在线 AV-TSE 真实对话基准 IEMOCAP-Dialog3Mix（3000 测试混合）及 RealTalk 跨库集；(2) 首个从鸡尾酒混合直接预测对话双方未来活动的目标条件化 LLM-VAP；(3) 系统比较历史/同步/预测上下文互补性，并以 pVAD 头监督替代手工场景损失加权。

**训练策略：** TS-VAP 用 IEMOCAP 10s 窗口预测后 2s：先冻结 Mini-Omni2 训任务层（lr 3e-4、≤6 epoch），再联合 rank-8 LoRA（lr 3e-5、≤8 epoch）后冻结。分离器先在 Vox2Mix（-10~10dB 混合）预训练，Adam lr 1e-4、batch 32、双遍训练 ≤100 epoch（patience 10）；推理 2s 窗、600ms 跳步，pVAD 阈值 0.4、衰减 0.05。

### 📊 实验结果
**数据集**：Vox2Mix 预训练；IEMOCAP-Dialog3Mix（训练 23522/验证 8120/测试 3000）；RealTalk-Dialog3Mix（1000 混合）零样本迁移。
主要指标：
- 平均 TP SI-SNR（USEV）：无上下文 9.04dB，+TS-VAP 9.56dB（+5.8%），三上下文融合 10.03dB（+10.9%）
- LLM-VAP vs 声学 VAP（USEV）：9.56 vs 9.41dB，AV-SepFormer 9.59dB（+5.7%）、TDSE 7.78dB（+4.6%）
- 目标静音正确抑制率 CSR（第三方干扰）：79.73%→85.13%；伙伴干扰 83.96%→87.74%
- RealTalk 零样本：TDSE 3.35→5.48dB，USEV 全上下文 8.03dB
**是否开源**：提供项目主页与 demo，代码尚未发布（论文声称将释出基准与模型）。

### ⭐ 评分：7/10
问题设定新颖，真实轮换混合基准填补在线 AV-TSE 评测空白；用 speech-LLM 把对话级轮换知识注入预测 VAP 的思路有洞察力，TS-VAP 在三个骨干上一致增益、跨库零样本仍有效，并以声学 VAP 做对照，实验设计扎实。不足：绝对增益约 1dB 偏温和；LLM 仅作预测条件而非语义驱动分离；干扰仍靠脚本语料叠加，生态效度有限；延迟指标未详报。属扎实的增量式贡献，基准与预测引导范式具长期价值。
## [14] Asymmetric Classifier-Free Guidance for Target-Speaker ASR
arXiv ID：2609.30476 | 方向：语音前端
作者：Yiwen Guan、Jacob Whitehill
机构：美国伍斯特理工学院（WPI）
发布日期：2026-09-28 | 论文 https://arxiv.org/abs/2609.30476 | PDF https://arxiv.org/pdf/2609.30476.pdf | 代码：暂无 | Demo：暂无

### 📌 简介
目标说话人语音识别（TS-ASR）需在重叠与噪声不断变化的混音中转写指定说话人，训练期学到的说话人条件强度在域偏移后会失配。本文首次将无分类器引导（CFG）用于TS-ASR的推理时校准：基于Whisper，条件分支学习目标说话人转写，无条件分支学习串行化多人转写（SOT），解码时以单一引导系数w调节两分支logit差值。冻结骨干后，先在目标域开发集网格搜索全局系数，再训练轻量预测器做句级调节。Libri2Mix与受控域偏移实验显示，相对条件基线最高降低相对WER 21.8%。

### 🔧 技术方案
**问题背景：** TS-ASR依赖注册语音注入的目标条件，但测试域重叠比例或信噪比改变时条件强度不再最优，已有方法均在训练期建模，本文提出推理时对引导强度再校准的自适应范式。
**模型架构：** 以Whisper-small为共享骨干，在编码器第3/6/9层后插入零初始化交叉注意力适配器，混音表征作query、注册表征作key/value；编码器末层接CTC头，条件分支与丢弃注册的无条件分支共享全部参数。
**核心创新：** (1)非对称CFG训练：条件分支用混合CTC/注意力损失（α=0.5）拟合目标转写，无条件分支以概率pu=0.1改用带说话人切换标记的SOT与PIT训练多人转写，单模型兼顾TS-ASR与多说话人识别。(2)逐步解码组合两分支logit：softmax(ℓu+w(ℓc−ℓu))，w=1退化为普通条件解码，w>1放大目标偏好。(3)推理时自适应：开发集上以0.2~3.0、步长0.2网格选全局系数wg；两层256单元MLP预测器从编码器特征预测WER变化量与收益概率，双阈值触发在{wg−δ, wg, wg+δ}中选句级系数。
**训练策略：** ASR骨干训练60 epoch，单张L40S，批大小8，AdamW，骨干lr 1e-5、新增参数lr 1e-4；预测器训练10 epoch、lr 1e-3，85%/15%划分训练与验证选阈值，全程不更新ASR模型。

### 📊 实验结果
**数据集**：Libri2Mix-clean（train-clean-100训练，3秒随机裁剪注册语音）；LSM受控域偏移：开发5406/测试5240句，重叠比30%/50%/70%，OV50下加WHAM!噪声（SNR=10/0 dB）。指标为语料级TS-WER与cpWER。
主要指标
- Libri2Mix TS-WER：非对称CFG 17.59%±1.96%（最优run 15.66%，对比条件基线18.04%、对称CFG 17.61%）
- OV30：41.28%→w=1为36.22%→全局标定34.78%→句级自适应34.18%（相对同模型普通解码降5.6%，相对条件基线最高21.8%）
- OV50/0dB：87.77%→74.16%→71.28%（自适应70.50%）
- 多人cpWER：23.51%（SOT-only 14.10%，pu=0.3时21.97%）
- Oracle分析：OV50句级最优系数可达21.60%，噪声增强后收益句比例从17.2%升至38.4%，显示句级选择仍有大余量
**是否开源**：暂无（论文未给出代码仓库链接）。

### ⭐ 评分：6/10
首次将CFG引入TS-ASR推理时校准，非对称训练让共享Whisper同时具备目标与多人识别能力，且冻结骨干即可适配新域，思路优雅；全局标定+句级预测+oracle三重分析论证充分。不足：仅Libri2Mix单语料、Whisper-small单骨干，WER绝对收益约2%，多人cpWER明显弱于SOT-only基线，未验证真实会议与远场场景，实用性有待扩大规模检验。
## [15] Room Impulse Response Embeddings for Speech Enhancement in Noisy and Reverberant Environments

arXiv ID：2609.31041 | 方向：语音前端
作者：Adrian Meise, Reinhold Haeb-Umbach
机构：德国帕德博恩大学（Paderborn University）
发布日期：2026-09-28
论文 https://arxiv.org/abs/2609.31041
PDF https://arxiv.org/pdf/2609.31041.pdf
代码：暂无（沿用 sp-uhh/rir-encoder 预训练权重，投稿 ICASSP 2027）
Demo：暂无

### 📌 简介

本文提出一种自监督方法，从单通道含噪混响语音中学习对噪声鲁棒的房间脉冲响应（RIR）表征。核心是课程式三阶段训练：先在纯混响数据、再在含噪混响数据上做对比学习，最后用教师-学生框架让学生从含噪输入复现教师从干净混响得到的嵌入。作者用轻量线性探针估计 T60 和 DRR 来衡量表征质量，并将嵌入通过 FiLM 注入判别式深度滤波增强模型，在混响与含噪混响两种条件下，STOI、CD、SRMR、DNSMOS 及下游 WER 均获得一致提升。

### 🔧 技术方案

**问题背景：** 去混响可改善主观听感与 ASR。已有研究证明显式或隐式利用 RIR、CTF、T60 等空间传播侧信息能提升去混响性能，但自监督空间表征大多要求高信噪比输入，对噪声鲁棒性差；传统做法先降噪再抽嵌入，因降噪系统对混响不透明，会引入伪影污染嵌入空间。本文目标是直接从低 SNR 含噪混响语音原生学习仅反映房间信息、忽略源信号与噪声的鲁棒嵌入。

**模型架构：** RIR 编码器采用 Conformer，以混响语音的对数幅度谱为输入，10 层、256 隐藏单元、4 注意力头，经两层 MLP 头输出 256 维 L2 归一化嵌入；从 Khanagha 等预训练检查点热启动。下游增强基于实时深度滤波 DeepFilterNet3 及其二步去混响变体，在解码器每个 Block 后插入 FiLM 层，以小 MLP 做逐特征缩放与平移来条件化滤波系数估计。

**核心创新：** (1) 首次面向含噪条件设计课程式原生噪声鲁棒 RIR 对比学习，绕开"先降噪后表征"的混响不透明缺陷；(2) 提出含噪配对策略 p=0.7，正样本对（同一 RIR）倾向于用不同噪声、负样本对（不同 RIR）倾向于用相同噪声，迫使模型忽略噪声差异；(3) 教师-学生嵌入对齐，用冻结教师从纯混响得到的嵌入作为学生从含噪混响输出的 MSE 目标，并保留对比损失做模型选择，把干净嵌入空间结构迁移给学生。

**训练策略：** 第一阶段沿用 InfoNCE 与负样本余弦相似度加权损失在 EARS-Reverb 上微调；第二阶段加入 WHAM! 噪声（SNR −2.5 至 17.5 dB）构造 EARS-WHAMR 继续对比训练；第三阶段额外引入 CHiME-3、SINS、SMS-WSJ 噪声扩大多样性的同时做师生训练。

### 📊 实验结果

**数据集**：训练用 EARS 约 100h 干净语音、EARS-Reverb v2、EARS-WHAM v2，噪声源 WHAM! 约 80h、CHiME-3、SINS、SMS-WSJ；测试集为未见过的真实 BUT-ReverbDB 测量 RIR 与 DEMAND 噪声（SNR 0 至 20 dB）。ASR 用 NeMo 轻量 QuartzNet 18.9M（弱）与 Conformer 1.1B（强）双模型。

**主要指标**（表征能力，线性探针 MAE 越低越好/ρ 越高越好）：
- T60（含噪混响，s）：CNN 0.31、Stage1 仅 0.25 且退化，Stage3 学生 0.23/0.68
- DRR（含噪混响，dB）：CNN 5.26/0.21，Stage3 学生 2.56/0.51，比 Stage2 优 1 dB 以上，接近纯混响水平

增强结果：混响条件下 Two-step+FiLM 取得 STOI 0.74、CD 3.55、SRMR 8.39、强 ASR WER 11.13；含噪混响下 Two-step+FiLM 为 STOI 0.64、CD 4.28、SRMR 8.20、强 ASR WER 从输入 41.32 降至 35.15，提升幅度更大。弱 ASR 深度滤波后 WER 反而略高于输入，但 FiLM 条件化可部分挽回。

**是否开源**：代码与权重未随本文公开，仅引用基线 rir-encoder 仓库；暂未提供 Demo。

### ⭐ 评分：6/10

理由：选题精准切中空间 SSL 表征抗噪这一开放问题，三阶段课程学习加噪声感知配对与师生对齐的设计简洁有效，并用线性探针、t-SNE 轮廓系数、判别式 DeepFilterNet/FiLM 双重证据验证嵌入确实编码了 T60/DRR；实验覆盖未见房间与噪声、强弱两类 ASR，结论"各类指标一致提升"可信。但整体相对已发表工作 [12] 属增量改进，绝对收益偏小，弱 ASR 上增强结果 WER 仍劣于含噪输入，评估集中于仿真退化数据，缺少真实端到端系统验证。

---

## 其余论文（仅列标题、arXiv ID、评分与链接）

### [16] Subject-Invariant Cross-Modal Decoding of Perceived Speech from Brain Recordings
- **arXiv ID**：2609.30832 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题摘要评分）
- 说者不变的感知语音跨模态脑解码，朝向无声语音接口
- **论文**：https://arxiv.org/abs/2609.30832 | **PDF**：https://arxiv.org/pdf/2609.30832.pdf | **代码**：暂无 | **Demo**：暂无

### [17] AcoustiClaim: A Numeric Claim Benchmark with Instrument Ground Truth
- **arXiv ID**：2609.30483 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题摘要评分）
- 带仪器真值的数值型音频声明基准，度量语音理解中的数字事实性
- **论文**：https://arxiv.org/abs/2609.30483 | **PDF**：https://arxiv.org/pdf/2609.30483.pdf | **代码**：暂无 | **Demo**：暂无

### [18] Why Alzheimer's Speech Screening Fails to Generalize
- **arXiv ID**：2609.31293 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题摘要评分）
- 剖析阿尔茨海默语音筛查的跨语料部署鸿沟与泛化失败归因
- **论文**：https://arxiv.org/abs/2609.31293 | **PDF**：https://arxiv.org/pdf/2609.31293.pdf | **代码**：暂无 | **Demo**：暂无

### [19] RePlay: Retrieval-Based Voice Playback for Multi-Turn Spoken Dialogue
- **arXiv ID**：2609.31588 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题摘要评分）
- 多轮口语对话以检索真实语音回放维持音色与内容一致
- **论文**：https://arxiv.org/abs/2609.31588 | **PDF**：https://arxiv.org/pdf/2609.31588.pdf | **代码**：暂无 | **Demo**：暂无

### [20] SAID: Semantic Acoustic Imaging Detector for Sound Event Localization and Detection
- **arXiv ID**：2609.31492 | **方向**：语音前端 | **评分**：6/10（未精读，按标题摘要评分）
- 语义声学成像引导声事件定位与检测
- **论文**：https://arxiv.org/abs/2609.31492 | **PDF**：https://arxiv.org/pdf/2609.31492.pdf | **代码**：暂无 | **Demo**：暂无

### [21] BAT-CLIP: Trimodal Alignment of Brain, Audio and Text
- **arXiv ID**：2609.31180 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题摘要评分）
- 脑-音频-文本三模态 CLIP 式对齐
- **论文**：https://arxiv.org/abs/2609.31180 | **PDF**：https://arxiv.org/pdf/2609.31180.pdf | **代码**：暂无 | **Demo**：暂无

### [22] BreathGRU: Semi-Supervised Bidirectional GRU for Speech and Breath Sounds
- **arXiv ID**：2609.31165 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题摘要评分）
- 半监督双向 GRU 联动检测语音与呼吸声事件
- **论文**：https://arxiv.org/abs/2609.31165 | **PDF**：https://arxiv.org/pdf/2609.31165.pdf | **代码**：暂无 | **Demo**：暂无

### [23] TinyAudio: Compact and Efficient Text-to-Audio Generation for Low-Resource Deployment
- **arXiv ID**：2609.31525 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题摘要评分）
- 面向低资源端部署的紧凑高效文本转音频生成
- **论文**：https://arxiv.org/abs/2609.31525 | **PDF**：https://arxiv.org/pdf/2609.31525.pdf | **代码**：暂无 | **Demo**：暂无

### [24] AFA-Net: Differential Attention for Auditory Attention Detection
- **arXiv ID**：2609.31402 | **方向**：语音前端 | **评分**：5/10（未精读，按标题摘要评分）
- EEG 听觉注意力检测引入差分注意力
- **论文**：https://arxiv.org/abs/2609.31402 | **PDF**：https://arxiv.org/pdf/2609.31402.pdf | **代码**：暂无 | **Demo**：暂无

### [25] Coupled Meta-Adaptive Filtering for Active Noise Control Under Time-Varying Acoustic Paths
- **arXiv ID**：2609.30945 | **方向**：语音前端 | **评分**：5/10（未精读，按标题摘要评分）
- 时变声路下方控主动噪声的耦合元自适应滤波
- **论文**：https://arxiv.org/abs/2609.30945 | **PDF**：https://arxiv.org/pdf/2609.30945.pdf | **代码**：暂无 | **Demo**：暂无

---

*Generated on 2026-09-28*
