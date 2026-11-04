# 2026-11-03 语音论文速递

**共收录**: 22 篇 | **语音大模型**: 11 篇 | **语音前端**: 11 篇

> 目标日期 2026-11-03（北京时间）arXiv 语音相关论文共命中 22 篇。
> 以下是按评分排序的结果。

### 速递说明

本批次精选前 15 篇进行完整模板精读，按评分由高到低排序；其余 7 篇论文仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），未展开精读。

---

## [1] GSLM2: Multi-Stream Speech Representation Learning and Generative Spoken Language Modeling

**arXiv ID**：2611.01143 | **方向**：语音大模型

**作者**：Yosuke Higuchi, Tom Fizycki, Mahi Luthra, Charles-Éric Saint-James, Emmanuel Dupoux 等

**机构**：Meta Superintelligence Labs（含 Université Paris Dauphine-PSL、AMI Labs 等）

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.01143 | **PDF**：https://arxiv.org/pdf/2611.01143.pdf | **代码**：https://github.com/facebookresearch/gslm2 | **Demo**：暂无

### 📌 简介
GSLM2针对无文本口语语言模型（SLM）达到文本LM同等语言能力需多约四个数量级训练数据的瓶颈，指出两大根源：离散语音单元语言质量有限、单流单元难以兼顾音位细节与高层语义。方法上提出SpidR 2.0编码器，以师生自监督蒸馏加逐层可微分共享预测头在多个编码层学习稳定互补的单元空间；再以多流SLM联合建模六条层级单元流，含共享时序骨干、分流预测头与捕获流间依赖的生成式深度头。在6M小时、6.5B参数下达sWuggy 80.7、sBLIMP 72.9、tSC 90.5，将与文本LM的数据差距缩小两个数量级，并超越Moshi等语音文本系统。

### 🔧 技术方案

**问题背景：** 标准GSLM对SSL编码器单一层的表征做后验k-means量化，迫使一个序列同时承载细粒度音位区分与高层语义规律，构成表示瓶颈；而词级/音节级低采样单元又丢失细粒度区分，压缩本身无法决定该保留哪些信息。

**模型架构：** 两阶段流水线。SpidR 2.0：学生与教师各90M参数Transformer编码器，学生收掩码输入、教师由学生EMA更新；选定各层挂共享线性预测头映射到公共码空间，软码分配经argmax得离散单元。多流SLM：各流独立嵌入后平均，送入仅解码Transformer共享时序骨干（90M至6.5B五档）；分流头预测各流下一单元，生成式深度头按层间码率升序对六流元组自回归；下游接时长预测器与HiFi-GAN vocoder合成波形。

**核心创新：** (1) 逐层可微分标记化（DLM）：借鉴视觉在线tokenizer，师生表征映射进同一可学习码空间并由蒸馏直接优化，摒弃后验非可微k-means与独立在线码本，各层同时产出高质量单元。(2) ME-MAX熵正则：对教师分布最小化条件熵、最大化边际熵，保证帧级置信且码字充分利用，防码本崩溃且梯度不回传编码器。(3) 跨流去重与多流联合建模：任一相邻帧流元组变化即保留，以变化点并集缩短序列且保留全流动态，单流损失、转移级自蒸馏与生成损失协同监督骨干。

**训练策略：** 编码器在LibriSpeech 960h自监督预训练；SpidR 2.0中条件熵权重固定、边际熵权重训练20k步后衰减；SLM在Libri-Light嵌套子集（600h/6K/60Kh）及网络会话英语（至6Mh）训练，Text LM用Libriheavy对齐转录配BPE 4096词表；vocoder用LJ Speech 24h；生成评测按auto-BLEU重复统计校准温度后top-k采样。

### 📊 实验结果
**数据集**：LibriSpeech 960h；Libri-Light与会话英语至6Mh；VoxPopuli 6Kh/语言；LJ Speech 24h。

**主要指标**：
- sWuggy/sBLIMP/tSC（60Kh/1.2B）：79.3/71.8/84.5，较SpidR SLM（73.9/62.4/75.1）平均升约6分，Text LM为83.8/71.5/89.2
- 6.5B/6Mh会话域：80.7/72.9/90.5/63.2（sWuggy/sBLIMP/tSC/sSC），全超Moshi 7B（74.8/59.9/80.9/56.9）
- 数据效率：匹配Text LM所需的数据差距由约四个数量级缩至约两个
- LLMJ评测：60Kh下3.05超文本LM的2.87，4/5分连贯续写多33%
- 编码器：ABX 2.83（层10，SpidR 3.92）、MAP 69.58（层7），跨种子ABX标准差降10倍

**是否开源**：训练代码与模型checkpoint已开源 @ https://github.com/facebookresearch/gslm2

### ⭐ 评分：9/10
评分理由：从表示瓶颈根源出发，把多层互补离散单元引入textless GSLM并给出完整的逐层探针、消融与统计显著性分析，1.2B参数即超越7B Moshi、数据效率提升两个数量级，属该方向里程碑式进展，且代码权重全开源实用性强。不足在于未显式建模韵律等声学属性，多流训练计算开销增大，部分结论依赖合成基准与经ASR的 indirect 生成指标。

---

## [2] Learning Timeline-Preserving Speech-to-Speech Translation

**arXiv ID**：2611.00690 | **方向**：语音大模型

**作者**：Zhisheng Zheng, David Harwath

**机构**：The University of Texas at Austin

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.00690 | **PDF**：https://arxiv.org/pdf/2611.00690.pdf | **代码**：暂无（承诺发表后释出） | **Demo**：暂无

### 📌 简介
本文提出时间线保持（timeline-preserving）语音翻译任务：配音等场景仅对齐总时长不够，译文语音须在同一绝对时间轴上保留源话语终点与显著内部停顿。作者用源画布（source-canvas）管线构造642K条时长严格匹配的英中目标语音，训练自回归端到端模型TransDubber，采用四阶段课程学习加验证器引导强化学习。在4,353句测试集上，相对最强基线UniSS将时长误差2%内占比从25.6%提升到61.5%、停顿对齐F1从0.118提升到0.550，同时COMET保持0.788的竞争力质量。

### 🔧 技术方案

**问题背景：** 现有S2ST系统能保语义、说话人与风格，但不控制"何时说、何时停"；TransVIP等需在推理时显式注入帧级isochrony控制，级联或后处理拉伸只能对齐全局时长而无法恢复内部停顿位置；独立录制的平行语料天然不含源时间线监督。

**模型架构：** TransDubber由Qwen3-ASR-1.7B初始化，词表扩展6,561个s3tokenizer语音codec符号（25Hz帧率），按源语音自回归先输出带<pause>标记的英文ASR，再按文本:语音=5:10的固定交错调度生成中文文本与codec token，文本结束后继续生成语音直至EOS，由flow-matching解码器还原波形；推理无任何时序控制模块。

**核心创新：** (1) 源画布监督构建：Silero VAD抽取语音区段与≥0.5s内部停顿构成时间骨架，每段按4.8字/秒时长预算用Hy-MT2-30B-A3B受预算翻译，VoxCPM2以源说话人条件合成候选，经Rubber Band有界变速校正后回填源语音窗口、窗口外保留源底噪，使目标采样数与源完全相同，质控后得642K对、298K停顿跨度。(2) 渐进课程训练：停顿感知文本接地→自然语速语音预热→时间线保持SFT（停顿codec损失权重2.0），消融显示从Stage 2直接做RL几乎无时序收益。(3) 分量级RL信用分配：MetricX-QE质量、全局时长（±2%免罚、饱和-4）、停顿对齐（容忍collar的漏/多静音、中心偏移、端点超出+时长门控）三类奖励独立组内归一化，语义反馈只作用文本token、时序反馈只作用codec token，用带掩码的GSPO序列级优化，权重(0.2,1,1)。

**训练策略：** 8 GPU、AdamW、seed 42、BF16；Stage 2训练20,000步、Stage 3训练12,000步，全局batch 256句，weight decay 0.02；Stage 4仅100更新，28 prompts×16 rollouts共448条，GSPO非对称裁剪(0.2,0.28)、KL系数0.01、FP32策略权重。解码核采样p=0.85、温度0.85、最多896 token。

### 📊 实验结果
**数据集**：训练源为Emilia-EN+GigaSpeech，含642K时间线对齐对（单侧约1,369小时）与806K自然语速对；测试集4,353句英译汉（1,439句CoVoST2朗读+2,914句GigaSpeech自发语音，均长8.9s）。

**主要指标**：
- Dur@2%/5%/10%：61.5%/92.2%/98.7%，UniSS为25.6%/56.1%/83.3%
- 停顿对齐：F1@0.4为0.550（UniSS：0.118，其余基线≤0.080）、tIoU 0.322、SER 0.128、onMedAE 0.162s
- 翻译质量：COMET 0.788 vs UniSS 0.784；MetricX-QE 4.12 vs 5.65；SIM 0.464居首
- 人评（1-5分）：质量3.63、自然度3.47，优于UniSS的3.13/2.87，但低于Cascaded的3.97/3.93
- 关键消融：删除<pause>标记使F1跌至0.231；Stage 4 RL把Dur@2%从48.6%升至61.5%；级联基线全局拉伸后F1仍≤0.159

**是否开源**：承诺发表后释出代码、数据与权重，项目页提供音频样例

### ⭐ 评分：8/10
评分理由：将"何时沉默"上升为翻译目标本身，任务定义、tIoU/SER等时序指标与642K对齐语料具备开创性；四阶段能力习得表、标记干预与拉伸对照等分析充分，时序收益接近量级提升而质量不崩。不足在仅覆盖英中短句、监督目标依赖自动翻译合成管线（构造管线自身成功率仅47.5%），质量与自然度仍逊级联基线。

---

## [3] One Waveform, Two Stories: Benchmarking Speech-Acoustic Conflict in Audio-Language Models

**arXiv ID**：2611.00325 | **方向**：语音大模型

**作者**：Wenbin Wang, Yuheng Li, Koichiro Yoshino

**机构**：The University of Osaka、University of Wisconsin-Madison

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.00325 | **PDF**：https://arxiv.org/pdf/2611.00325.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
论文提出SAC-Bench，首个系统性评测同一音频内"言语声明与环境声学证据相互矛盾"时音频大模型（ALM）听词还是听声的基准。基于FSD50K的188个声学事件类构建616,031条唯一音频（2,069.9小时）、204万QA，覆盖语义、时间、空间三类共七个任务，配对相容/冲突条件及audio-only对照。对五个开源ALM评测显示：高音频单模态准确率与冲突下大幅退化并存，Event Identity冲突较相容低24.8-46.5个百分点，语音跟随率（SFR）最高80.8%；提示干预效果异质，部分模型恢复声学grounding，部分反而恶化。论文首次将声学能力、冲突鲁棒性与干预效应解耦评估。

### 🔧 技术方案

**问题背景：** ALM评测多在言语与环境声一致时进行，模型可靠语言捷径答对而无需真正感知声学事件，故相容条件下的成功无法区分忠实声学定位与文本偏置。已有冲突基准仅覆盖模态间冲突或词汇-韵律/场景级冲突，时间与空间定位基准又缺少矛盾言语声明，跨"何事/何时/何处"的音频内言语-声学冲突长期缺位。

**模型架构：** SAC-Bench为受控构建管线而非新模型：FSD50K录音去冗余标签并经PP/PNP过滤后，用GPT-4o生成声明文本、F5-TTS合成双说话人语音，按设定语音-事件RMS比（SER）与事件音中心对齐混合；空间任务以38个球面Voronoi区离散方位，独立指定环境声源、语义声明、语音物理声源三组几何，用SADIE II KEMAR HRIR与AmbiX一阶Ambisonics渲染binaural/FOA（含距离衰减与径向多普勒）。评测端对Qwen3-Omni-30B-A3B、Step-Audio-2-mini、Audio Flamingo Next、MOSS-Audio-8B、Spatial-Omni SO30B做零样本问答。

**核心创新：** (1) 首次将音频内言语-声学冲突形式化为统一评测设定，语义（Presence/Identity）、时间（State/Order）、空间（Location/球面运动/径向运动）七任务一体，QA规模（204万）远超DEAF、AHA-Bench等先前工作。(2) 三源独立匹配设计：语音物理轨迹与声明内容解耦，L1-L5空间条件交叉语义与几何冲突，四格匹配对照可分离两类干扰；Temporal Order把误导语音放在完整事件序列之后，排除同时掩蔽解释。(3) 指标体系解耦能力维度：audio-only对照测声学能力、相容-冲突gap测退化、SFR测错误方向、CTA测对冲突目标吸引力，并对中性/声学接地/冲突感知三种提示以准确率与SFR双标准评估。

**训练策略：** 不做模型训练，零样本推理：vLLM/Transformers后端、BF16、最多256 token、关采样，不可解析输出计错。合成配置：F5-TTS Base（NFE 32、CFG 2.5、seed 4242、44.1kHz/16bit、语音段RMS 0.055）；空间渲染为消声自由场，静源半径2.0m、径向0.5-2.0m、10ms轨迹采样、事件-语音间隙0.2s、空间SER固定0dB；dev/eval含393,010/223,021条，源录音与合成ID跨split不重叠。

### 📊 实验结果
**数据集**：SAC-Bench：616,031条唯一音频（2,069.9小时，源自16,340条FSD50K录音、188类）、2,043,836个QA（评测split 744,086）；空间子集含binaural与FOA渲染

**主要指标**：
- Event Identity（五选一准确率，Qwen3-Omni）：audio-only 84.6%、冲突下39.8%；五模型相容-冲突gap 24.8-46.5pp
- 语音跟随率SFR：Identity冲突47.0-80.8%（远超20%随机参考）；Temporal Order最高92.4%
- Temporal Order：Step-Audio-2-mini相容96.8%对比冲突7.5%，gap达89.3pp，误导语音出现在事件序列之后仍失效
- 空间（Spatial-Omni FOA）：Motion audio-only 50.5%、有语音约34%；单独反转声明降9.9pp、单独反转语音轨迹降20.1pp（95% CI均不含0）
- 提示干预：冲突感知使Qwen3-Omni Identity 39.8%→59.3%；但MOSS-Audio Presence SFR降而BAcc不变；Step-Audio-2-mini Temporal State反降23.4pp

**是否开源**：暂无（论文未给出代码或数据发布链接）

### ⭐ 评分：8/10
评分理由：选题精准，首次将音频内言语-声学冲突作为独立评测对象，三源匹配设计与能力解耦指标体系方法论严谨，配对bootstrap置信区间与匹配对照增强了分析可信度；"speech序列后仍失效""SFR下降但grounding未提升"等发现有诊断价值。不足在于空间评测仅覆盖Spatial-Omni一个模型，合成语音与消声渲染限制真实场景泛化，且未提供开源渠道影响可用性。

---

## [4] InteractionBench: Measuring Timing, Task Accuracy, Whisper and Volume, and Grounding in Real-Time Voice Systems

**arXiv ID**：2611.02430 | **方向**：语音大模型

**作者**：Richard Yucheng He, Chen Xu, Yihang Liu, Tairan Chen, Baodong Cao

**机构**：AveraLabs

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.02430 | **PDF**：https://arxiv.org/pdf/2611.02430.pdf | **代码**：https://github.com/avera-labs/InteractionBench | **Demo**：暂无

### 📌 简介
现有实时语音基准通常只测单一维度。本文提出InteractionBench，用同一套录制用户音频与同一评测链路，在七个系统上同时度量对话时序、口头任务准确、耳语与音量、22轮以上长对话的groundedness四个维度，每系统13个场景221题、共1519次评分运行。关键发现：级联系统口头任务最高（38/50）但时序偏弱；没有任何系统在要求窗口内纠正用户语法错误；仅Gemini Live在多数请求下耳语（8/10）；托管系统groundedness通过率67–88%，开源全双工模型仅14–35%；扣除约1.5秒网络延迟后GPT-Live时序分从86%降到56%。

### 🔧 技术方案

**问题背景：** 既有全双工基准各自聚焦轮换、指令跟随、副语言控制或记忆的一面，数据、协议与系统互不一致，同一系统的不同维度结果难以对比；托管API如GPT-Live的流式音频无时间戳且省略静音帧，任何时序测量都须先重建其时间线。

**模型架构：** 框架由stimuli、驱动、录制与评分四部分组成：用户语音以MiMo TTS（24kHz）合成后实时流给各系统专用driver，双轨音频录于同一时间线，用WebRTC VAD（aggressiveness 2、30ms帧）切段、Parakeet TDT 0.6B v3逐词转录。评分卡在系统运行前固定：由MiMo mimo-v2.5-pro读剧本对话抽取触发词与目标答案，再按规则策略确定期望floor动作与onset窗口。Groundedness含Gemini 2.5 Flash生成的10段22–24轮对话、11类52个探针。

**核心创新：** (1) 首个在同一live框架内同时打分交互机制、回答内容、语音输出与对话状态并覆盖同批系统的基准；为无时间戳的GPT-Live按driver记录的音频块到达时间重建客户端时间线，并从服务器自带时钟测得约1.47s网络延迟。(2) 规则式评分卡加声学耳语判定：floor动作与目标答案先于运行固定，耳语直接以音频信号判（HNR<6dB且voiced比例<0.4），规避LLM评审在非语言线索上与人类近乎零一致的问题。(3) Groundedness探针嵌入系统自己回复构建的历史中（非固定上下文），评审对每段对话判三次多数表决，输出0–100连贯分与失败标签，把"没回答"与"答错"分开统计。

**训练策略：** 基准论文不涉及模型训练；语义判定统一用Gemini 2.5 Flash评审，耳语与音量走纯声学规则；7个verdict人工纠正、5个探针剔除。运行于2026-08-17至08-31录制，每系统213–221次评分运行，附录对onset窗口、暂停规则与耳语阈值做敏感性重打分。

### 📊 实验结果
**数据集**：13场景×221题/系统（时序140、口头任务50、耳语/音量20、groundedness 52探针）；评测GPT-Live、GPT-Realtime、Gemini Live、Moshi、PersonaPlex、Freeze-Omni及级联共7系统、1519次运行。

**主要指标**：
- 口头任务：级联38/50（76%）最高，托管34–36/50，开源模型仅3–9/50；语法纠正实时打断全系统0/10
- 时序：GPT-Live客户端86%最高，按服务器时钟扣除约1.5s延迟后降为56%；Moshi最低41%；六个全双工系统时序与口头任务Spearman秩相关0.83
- 耳语/音量：仅Gemini Live 8/10，其余系统0–2/10；35次耳语请求中仅2次得到更轻声回复
- Groundedness：托管与级联67–88%（Gemini Live 88%），开源14–35%（Moshi 14%、coherence 16）

**是否开源**：代码已开源 @ https://github.com/avera-labs/InteractionBench；录音与评审输出公开于项目页

### ⭐ 评分：8/10
评分理由：罕见地把机制、内容、语音输出与长对话groundedness统一在同一实时评测链路，且工程透明，时间线重建、规则评分卡与阈值敏感性分析可直接复用，结论对实践有明确指向（实时语法纠正普遍缺失、托管系统时序被网络延迟美化）。不足是各场景仅10–30题、全合成无噪声语音，协议在系统间不完全一致，语义判定依赖与Gemini Live同族的评审。

---

## [5] Voice-Native LLMs Hear Frustration but Do Not Listen to It

**arXiv ID**：2611.02893 | **方向**：语音大模型

**作者**：Hanjun Luo, Yuhan Lu, Hanan Salam

**机构**：New York University Abu Dhabi

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.02893 | **PDF**：https://arxiv.org/pdf/2611.02893.pdf | **代码**：https://github.com/Astarojth/hear-not-listen | **Demo**：暂无

### 📌 简介
用户的挫折既写在词里也藏在语气里，端到端音频大模型（ALLM）本可两者皆闻，但现有评测把"输出没变"直接读作鲁棒，无法区分"听见了才稳住"与"根本没听见"。本文按Brunswik镜头模型把挫折传递拆为表达、感知、利用三链路，在353个任务上交叉挫折措辞与挫折音色构成within-item 2×2设计，用55个音色合成1412条音频发布VoxAffect。8个模型中7个的准确率不受音色影响；7个能检出73–100%的表演愤怒，但中性措辞下至多3.1%的clips被标注为frustrated，而人类听者达65.3%；开源模型编码器仍解码出音色（成对准确率0.67/0.69）但向答案位衰减。结论：模型听见了挫折音色却不倾听，音色不变性是无感知的不变性，措辞不变性才是真鲁棒。

### 🔧 技术方案

**问题背景：** VoiceBench等评测将扰动下准确率不变等同于鲁棒，VoxParadox等仅在任务外测情绪识别，均未验证被评模型是否感知了刺激，导致鲁棒性与非感知被混淆；且很少有工作在任务音频中独立操纵措辞与音色两通道。

**模型架构：** 本文为受控评估协议而非训练模型，含三模块。1）VoxAffect刺激：MMLU-Pro、GPQA-Diamond、IFEval、MATH-500各采样100项，DS-V4-Pro做口语化归一与挫折改写，Doubao TTS 2.0按"平静/强烈沮丧不耐烦"指令在固定说话人上合成BN/BV/AN/AV四条件clip。2）感知测量：音色探针令模型忽略内容只答neutral或frustrated，配RAVDESS强愤怒阳性对照与10人听觉盲测。3）机制分析：对Qwen2.5-Omni-7B与MiMo-Audio-7B-Instruct在音频编码器中层、LLM音频token聚合态、答案位末层隐状态训线性探针，交叉感知与利用两轴得四象限（真鲁棒/情绪漂移/无感知不变/无感知敏感）。

**核心创新：** (1) 感知接地的鲁棒性协议：以镜头模型三链路在同一批音频上分别测表达（双SER+人类听者做独立manipulation check）、感知与利用，首次把"没听见"与"听见不动"分开。(2) within-item 2×2交叉刺激：任务、答案、说话人恒定，DS-V4-Pro语义保全审计剔除47/400个丢失任务信息的改写，ECAPA-TDNN说话人余弦0.940，使措辞效应与音色效应完全可分离。(3) 长度平衡的隐状态探针：因234/353项BV更短，提出长度平衡成对准确率使纯长度线索回归0.5，并把18个声学特征与时长残差化，证明音色信息超出表层声学仍留在LLM态（0.66/0.59），到答案位衰减为0.61/0.54。

**训练策略：** 无模型训练；探针为标准化特征上的L2正则logistic回归，五折切分使同项两clip同fold。推理全部temperature 0；IFEval用官方checker，MATH-500精确匹配终答。对比均在item内配对、4家族宏平均、5000次bootstrap出95%CI，24个准确率对比做Holm校正；开源模型合计12 GPU小时（单张L20）。

### 📊 实验结果
**数据集**：VoxAffect（353项、1412 clips、55音色、16.7小时）；辅助RAVDESS（96怒+96中性）与50项听测摘录。

**主要指标**：
- 音色对准确率：8模型效应-2.6至+7.7pp，7模型CI含零；仅MiMo-2.6-Flash显著+7.7pp
- 音色感知：中性措辞下BV标注frustrated率0.0–3.1%；表演愤怒命中率7/8模型73–100%，假警报0/96
- 感知灵敏度差：声学0.5–3.4pp vs 词汇41–75pp；人类听者65.3%[61.1,69.5]对比模型摘录48–50%
- 隐状态探针：编码器中层0.671/0.693与18声学特征持平，答案位降至0.611/0.538
- 放大效应：受挫措辞下音色推高标注率随arousal分位上升，Q4−Q1达+13.6pp；措辞通道为真鲁棒

**是否开源**：代码、prompt与VoxAffect数据集已开源 @ https://github.com/Astarojth/hear-not-listen

### ⭐ 评分：8/10
评分理由：把"鲁棒性"从输出不变升级为可证伪的感知—利用四象限诊断，操纵检查、阳性对照与长度平衡指标设计严谨，结论对EmoOmni类"学会倾听"的训练与评测实践有直接纠偏价值。不足在于仅覆盖英语、轻度、合成、单轮任务的挫折，闭源模型无内部证据，且感知阈值依赖人类听者单一标定。

---

## [6] How Much Prosody Does Your ASR Encoder Already Know

**arXiv ID**：2611.02602 | **方向**：语音大模型

**作者**：Rini Sharon, Kadri Hacioglu, Andreas Stolcke

**机构**：Uniphore

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.02602 | **PDF**：https://arxiv.org/pdf/2611.02602.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
传统轮次结束（EoT）检测长期假设手工韵律特征（音高、能量、语速、停顿）能补充神经ASR编码器的表征。本文直接追问：流经流式Zipformer编码器后，韵律还剩多少价值？作者在编码器输入的log-mel特征、第一/第三/最终stack共四个深度上运行三项测试：韵律增量、逐特征可重建性、结合时间移位对照的逐特征检验。三项结论一致：韵律在原始音频上增益很大，但仅过一个编码器stack即基本坍塌；残值多为说话人身份捷径而非真实轮次时序；wav2vec2、Whisper与公开CASPER语料复现同一模式。对基于强编码器的检测器，独立韵律前端收益有限。

### 🔧 技术方案

**问题背景：** 对话系统需在数百毫秒内连续判定说话人是否说完；固定静音阈值会误触轮内停顿或响应迟缓，故二十年来检测器普遍将手工韵律与ASR编码器特征作为两路独立输入拼接。但编码器读的是韵律所计算的同一信号，可能早已内含这些信息，业界为此付出特征抽取、延迟与逐说话人调优的成本。

**模型架构：** 被测编码器为6-stack流式Zipformer ASR编码器，经单次非流式前向后hook读取四个深度：输入log-mel（fbank）、zip-early、zip-mid、zip-final。韵律侧为约41个帧级特征、五大族：pitch/F0（13个）、energy（4个）、timing/pause（8个）、voice quality（4个）、spectral（12个）。检测器固定为两个：L2正则逻辑回归（L-BFGS）与单隐层神经网络，同配置分别跑在编码器特征、编码器+韵律拼接特征上。

**核心创新：** (1) 把"韵律是否还有用"拆成三个互补测量：条件增量ΔAUC与ΔCE（bits/帧，MDL式信息论可读）、从编码器激活回读每个韵律特征的留出R²、逐特征独立检验，三者交叉验证避免单一指标误导。(2) 时间移位对照：在每条话语内将韵律序列随机循环移位、破坏其与轮末边界对齐而保留每说话人统计量与自相关，real减shifted后的残差被判定为说话人身份捷径而非轮次时序；另用"整句平均韵律"第二对照确认残差来源。(3) 双重防护设计：逻辑回归与神经检测器各自复跑全部测量排除"检测器太弱"解释；在两个开源编码器（含无标注自训练的wav2vec2）和公开CASPER语料上复刻，排除单模型/单数据/纯词汇化解释。

**训练策略：** 逻辑回归标准化各维、类别均衡子采样、L2系数speaker-grouped四折CV选出；神经检测器Platt scaling校准保证bits指标有效。数据为内部英语双人电话对话、说话人不相交三向划分；显著性用整说话人块bootstrap；标签采用边界collar。wav2vec2/Whisper需将电话带宽音频上采样后off-the-shelf使用。

### 📊 实验结果
**数据集**：内部英语双人电话对话评测集 + 公开CASPER二人对话语料；韵律库约41维5族特征

**主要指标**：
- 编码器单用AUC（logistic/neural）：fbank 0.685/0.686 → zip-early 0.874/0.884 → zip-mid 0.908/0.912 → zip-final 0.893/0.901，韵律增量ΔCE过首个stack后即坍塌
- 90%召回工作点误报率：fbank上韵律使FA从0.711降到0.598（11.3个百分点，CI[.084,.144]）；zip-final仅0.356→0.330，对照校正后真实时序部分几乎归零
- 韵律重建R²中位数（ridge/MLP）：fbank 0.33/0.40 → zip-early 0.53/0.51 → zip-final 0.20/0.09
- CASPER复刻：raw log-mel AUC 0.763且校正增量坍塌复现；wav2vec2-base 0.994/0.964，whisper-small 0.897/0.995，自监督无词标签模型上韵律同样冗余
- 基线对照：仅VAD/静音检测AUC很低；逐特征无一越过实用阈值

**是否开源**：暂无（未提供本研究代码或Demo）

### ⭐ 评分：8/10
评分理由：设计严谨的表征分析型工作，以时间移位对照分离说话人捷径、双检测器防容量偏差、公开语料与自监督编码器三重复刻，把"语音前端该不该继续做韵律"这一实践问题回答得干净可信，对全双工语音Agent的EoT模块有直接工程价值。局限是主实验依赖内部电话数据、单语言，collar评测不等同完整流式endpointer的延迟表现，且未开源代码。

---

## [7] SPATEX: Array-Flexible Multichannel-to-Multichannel Target Speech Extraction using Direction Clue

**arXiv ID**：2611.03119 | **方向**：语音前端

**作者**：Wen Wen, Changda Chen, Yu Xi, Haoyu Li, Qiang Zhou, Guanyu Chen, Xiaoyu Gu, Bohan Li, Shuai Wang, Kai Yu

**机构**：上海交通大学AI研究院X-LANCE实验室、早稻田大学、南京大学、思必驰科技

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.03119 | **PDF**：https://arxiv.org/pdf/2611.03119.pdf | **代码**：https://github.com/Wenanzhi/SPATEX | **Demo**：暂无

### 📌 简介
现有MIMO目标语音提取（多通道输入多通道输出）系统均假设固定麦克风配置，无法跨阵型部署，而阵型灵活的单输出方法又丢弃逐麦克风空间信息。本文提出SPATEX，首个阵型灵活的MIMO TSE框架：以麦克风坐标与目标DOA为条件，通过几何感知通道交换（TAC）与共享时间联合注意力重建各麦克风的混响目标语音像，并保持排列等变性。在2–10麦克风、匹配/失配阵型下最高达15.98 dB SI-SNRi；固定4麦阵列上IPD误差0.614 rad、ITD误差5.00 µs，extraction质量与空间保真度均优于固定阵基线，且对DOA线索误差鲁棒。

### 🔧 技术方案

**问题背景：** M2M-TSE、SoundCompass等MIMO TSE方法采用阵型专用架构，仅适配固定麦克风数量与几何；TAC类与FlexIO等阵型灵活方法只重建参考通道信号，无法保留目标声场的通道间关系，难以满足VR/AR等沉浸式音频的空间渲染需求。

**模型架构：** 共享编码器（256点Hann窗STFT、128点hop、64维特征）+提取模块+共享解码器。输入波形与麦克风坐标padding到C通道并用二值有效掩码屏蔽pad通道；有效麦克风统一标准差归一化。提取模块沿用DeFTAN-II频-时建模设计，共6个分离阶段，每阶段含DOA调制、逐麦频率建模、时间联合注意和几何条件化TAC；参数量4.57M。解码器估计各有效麦克风的复数STFT，经iSTFT与幅度重标定输出目标像。

**核心创新：** (1) 几何感知通道交换：TAC仅对有效麦克风做变换-平均-拼接聚合，几何嵌入由相对质心偏移、归一化偏移与阵列半径经共享MLP生成并跨所有TAC块复用，天然支持任意麦克风数/阵型并保持排列等变。(2) 通道不变联合注意力：替换DeFTAN-II的逐麦时间注意力，各频率点上麦克风查询/键来自重叠时间patch，softmax前的注意力logits跨有效麦共享得到公共注意力图，而value保持麦克风专属；消融显示其贡献SI-SNRi提升约2.92–3.63 dB。(3) 空间一致监督：PCM损失外叠加IPD与复干相性损失，在语音活动TF点及有效无序麦克风对上计算，显式约束重建信号间通道关系；目标方位以sin/cos循环编码经调制向量统一作用于各麦流。

**训练策略：** 基于LibriSpeech用pyroomacoustics镜像法仿真8 kHz混响混合，1目标+2干扰，RT60 0.15–0.7 s，不加背景噪声。Adam、batch 8、最多100 epoch，按验证SI-SNRi选模型；基线（USES-DOA、FlexIO-DOA等）均在对应数据上重训100 epoch。

### 📊 实验结果
**数据集**：LibriSpeech仿真（8 kHz）；Matched Geometry（ULA/平面栅格2.5–8 cm、2–10麦）与Unmatched Geometry（稀疏/随机阵5–25 cm、1 cm扰动）及固定4麦线阵。

**主要指标**：
- SI-SNRi：Matched 2–8麦14.23 dB；Unmatched 9–10麦15.98 dB（训练范围外外推）
- PESQ/STOI：3.41/0.891（Matched）、3.65/0.923（Unmatched 9–10麦）
- 空间保真（固定4麦）：IPD误差0.614 rad、ITD误差5.00 µs、Pres@5达90.4–97.0%
- 关键对比：四个条件中三个取最高参考通道SI-SNRi，较FlexIO-DOA最高+0.59 dB；固定阵上较SoundCompass（11.68 dB）提升1.22–1.54 dB

**是否开源**：代码与数据集已开源 @ https://github.com/Wenanzhi/SPATEX

### ⭐ 评分：8/10
评分理由：首次将阵型灵活性与MIMO多通道重建统一，排列等变TAC+通道不变联合注意+IPD/干相性空间监督的组合设计针对性强、消融充分。覆盖2–10麦、匹配/失配阵型、DOA扰动等多维评测，实验较扎实。局限为仅8 kHz仿真语音混合，缺少真实录音、非语音声源及与波束成形的实时性对比。

---

## [8] C3: Speech-Guided KV Retrieval for Long-Context SpeechLLM Inference

**arXiv ID**：2611.00333 | **方向**：语音大模型

**作者**：Dancheng Liu, Markus Müller, Rupak Vignesh Swaminathan, Jing Liu, Srikanth Ronanki, Aram Galstyan

**机构**：Amazon AGI（美国）；University at Buffalo（美国）

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.00333 | **PDF**：https://arxiv.org/pdf/2611.00333.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
SpeechLLM以远高于文本的时间分辨率编码音频，KV缓存成为长上下文推理的显存与解码瓶颈；现有KV检索方法主要面向文本设计，论文证明检索误差会自回归复合成"生成漂移"。为此提出C3（Cluster–Compete–Compete）：按KV头组织的免训练检索框架，融合层级键空间聚类、同KV组查询头的共享预算竞争与查询自适应的split–merge分辨率再分配。在4个SpeechLLM的长语音识别/翻译/摘要上，C3在匹配检索预算下32项设置中31项取得检索类方法最优：Qwen3-Omni上128-KV预算将LS-Long WER从ClusterKV的180.94%降至7.07%，256-KV预算下语音翻译chrF从25.91提升至55.79。

### 🔧 技术方案

**问题背景：** 长音频使KV缓存随时长急剧膨胀，而Quest、UNIQUE、ClusterKV等检索方法使用固定时间页、逐查询头独立选择或静态聚类，不符合音频注意力结构。论文推导（式5上界）表明检索扰动正比于被忽略的注意力质量，并随生成自回归复合，可造成转录与音频失去对齐、提前输出EOS。

**模型架构：** C3在每层每KV头上对音频keys做递归二分k-means构建键空间层级，节点以质心代表；解码初期激活一个"frontier"划分全部音频keys（大小固定、各节点深度可不同）。每步将frontier节点对共享该KV头的全部查询头取最大余弦相似度打分，按分数降序在检索预算B内收集胜出节点的原始KV，所有查询头对同一子集做精确注意力；打分仅涉及O(F)个质心而非全部N个键。

**核心创新：** (1) C1键空间层级聚类：实测ASR/翻译/摘要中分别有34%/29%/78%的top-k注意力质量落在主导时间带之外且局部碎片化，固定时间块会连带低相关KV，非连续键空间聚类让相似query响应的分散位置共享检索单元。(2) C2共享预算竞争：集中型查询头将约85%注意力质量放在音频上、弥散型仅约12%，均值池化会稀释强匹配，故对同组查询头取max形成单一排名、竞争一份共同KV预算。(3) C3自适应分辨率：利用音频注意力frontier的时间连续性（ASR峰值位置每步中位仅移动约4个音频帧），以EMA平滑各active节点相关度，每步执行配对split–merge——拆分高优先级节点、合并低优先级兄弟对——frontier总数不变而细粒度单元向当前相关区域集中。

**训练策略：** 完全免训练、不改架构与参数：k-means每次二分8轮迭代、随机种子0，query与质心L2归一化后以余弦打分；推理BF16、batch size 1、温度0贪心解码，默认每步2次配对split–merge，音频短时绕过检索。系统层用FlashInfer分页注意力核与Triton收集的frontier融合核，固定缓冲形状支持CUDA Graphs捕获重放。

### 📊 实验结果
**数据集**：LibriSpeech-Long（270条英文长录音）、MLS多语长音频ASR（荷/德/法/西约4分钟、658条）、LongSpeech（6语言各100条翻译共600条、摘要545条）、AudioMarathon/MMAU-Pro/MSP-Podcast、自建120条约13–16分钟"大海捞针"音频。

**主要指标**：
- LS-Long WER：Qwen3-Omni 128-KV预算7.07%，ClusterKV为180.94%（全注意力2.02%）；Qwen2.5-Omni 128-KV为40.48%对133.13%
- 语音翻译chrF：Qwen3-Omni 256-KV预算55.79对ClusterKV的25.91（提升约30分，全注意力74.75）；Gemma-4 42.29对21.28
- 汇总：48个模型-任务-预算组合中39个最佳或并列最佳；大海捞针在Qwen3-Omni上32个KV即达95%精确匹配、64KV无损恢复
- 效率：H200上512-KV预算约8K音频token后端到端延迟低于全注意力；冷区卸载使显存内音频状态由O(N)降至O(B+F)

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：动机分析扎实，生成漂移的形式化界定与音频注意力三属性对检索设计有真实指导价值；方法免训练即插即用，紧凑预算下WER下降173个百分点级、收益显著且跨4模型多任务一致，系统实现完整。不足在于各组件承自Quest/ClusterKV/层级索引等既有思路、属语音特化组合式创新，未释出代码，超32K token的扩展结果为分析性外推而非实测。

---

## [9] Local or Escalate? Post-Training Expert Routing for Real-Time Duplex Speech Models

**arXiv ID**：2611.01639 | **方向**：语音大模型

**作者**：Ruoyu He, Jisen Li, Anthony Ji, Changyi Yang, Zetian Li, Runduo Ma, Zhen Zhang, Zhongzhu Zhou

**机构**：UCLA、UIUC、UBC、CMU、Stanford、UW-Madison、UCSB、悉尼大学

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.01639 | **PDF**：https://arxiv.org/pdf/2611.01639.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工语音模型须在接管话轮一刻决定"快答还是等待更强推理"，现有特殊token方案把路由与话轮切换绑定、依赖时间标注双工训练。本文冻结MiniCPM-o 4.5（9B，仅语音输入输出），在原生听→说转换点的L22隐状态上拟合logistic失败读出，超阈值即转给gpt-5.5专家并由本地talker转述答案。内部240query准确率从42.1%升至69.2%（+27.1分），较always-escalate省31.5%平均服务器等待，优于matched random与零样本文本路由；配方迁移至VoiceChat-11B同样有效。

### 🔧 技术方案

**问题背景：** 简单问题要快答、难题要深思，而决策必须发生在应答起点。现有特殊token路由在生成策略内学习，耦合话轮切换与打断、需时间标注双工训练，操作点调整依赖重训。

**模型架构：** 本地为冻结MiniCPM-o 4.5（9B，Qwen3-8B基座），专家为接入web search的gpt-5.5。音频按1s块流入；生成调用首次返回listen-to-speak转换（answer onset）时，以"L22最新尾部状态+尾部均值+输入均值"拼接特征经线性读出打分失败风险，仅数十毫秒、无额外LM前向；高危轮经ASR全文转录→专家文答→talker转述，等待期仅播一次固定hold线；dialogue-act头只放行信息请求轮。

**核心创新：** (1) 能力仲裁与交互控制解耦于生成之外：读出仅用冻结模型原生起点状态，阈值是服务参数，不改checkpoint即可重调专家预算；训练目标凸、只用缓存特征与标签，无法扰动双工策略。(2) 层选择有机制支撑：文本输入LOPO下L22 last-token AUC 0.931、末层0.366，L28–35权重插值将末层衰退归因双工训练接管轮末行为；文本态探针可直读语音态（0.855）与未见真人录音（0.760）。(3) 端到端部署闭环：相比零样本GPT-5.4-mini文本路由，读出在commit点决策、无需网络，本地轮少等0.64s且失败预测AUC更高（0.783 vs 0.722）。

**训练策略：** 标签由gpt-5.4-mini judge判本地答案对错；5,228校准行、五折分层CV（seed 42），按语言取4,986核心行out-of-fold分位设三档阈值、评估期固定；logistic原始特征+L2正则，bf16单卡H100。

### 📊 实验结果
**数据集**：240query内部集（chat/事实/知识/数学/SimpleQA陷阱）加TriviaQA/WebQ/Llama Q./SD-QA语音QA四池，5,950会话

**主要指标**：
- 内部准确率42.1%→69.2%（aggressive，50%升级），超matched random 8.3分，恢复always-expert差距72.2%
- 外部四池宏平均59.4%→83.2%，超matched random 7.1分
- Mean TTFA 5.95s vs 升级全部8.68s（-31.5%），留存轮1.23s；专家成本$0.018/query
- 读出判别AUC 0.848，优于TF-IDF与零样本LLM路由（外部0.532/0.722）；specific-but-wrong型失败（70%）AUC 0.81
- VoiceChat-11B迁移43.8%→75.7%（random 67.0%）；13人盲测9胜4平3负，实时信息正确性3.67 vs 2.56

**是否开源**：称代码release含校准清单、阈值与脚本，未给URL，暂无

### ⭐ 评分：7/10
评分理由：线性探针读出本身并非首创，但论文让其在原生音频应答边界生效并用live serving、成本核算、机制分析与人评完整验证，文本态探针跨模态可读与末层衰退归因是有价值的表征发现，对matched random和LLM路由的优势清晰。局限是模型家族有限、专家绑定单一云端模型、TTFA不含端点检测与客户播放、人评仅13人，属实验充分的实质性增量工作。

---

## [10] Multilingual TASU: Extending Text-Only Alignment to Multilingual Speech Recognition via Simulated CTC Posteriors

**arXiv ID**：2611.00692 | **方向**：语音大模型

**作者**：Chenghao Wang, Yi Yang, Jing Peng, Yu Xi, Shuai Wang, Kai Yu

**机构**：上海交通大学X-LANCE实验室、思必驰科技、南京大学

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.00692 | **PDF**：https://arxiv.org/pdf/2611.00692.pdf | **代码**：暂无

### 📌 简介
多语言Speech LLM性能受限于成对语音-文本数据稀缺与语种分布失衡，已有TASU文本对齐只在英语验证。本文提出多语言TASU：以冻结OWSM-CTC的原生50,002路CTC后验空间作为八语种共享对齐接口接入Qwen2.5-1.5B-Instruct，在MLS八语种上系统比较真实音频后验、启发式CPS与学习式多语种模拟器三种监督源。结果显示：真实后验+LoRA将池化WER从10.08%降至8.21%且八语种全升；纯文本模拟器+LoRA达10.51%；CPS文本初始化仅用1/9成对语音适配一epoch即达9.19%，显著降低配对音频需求。

### 🔧 技术方案

**问题背景：** 主流Speech LLM对齐依赖连续特征投影与大规模成对语音，多语言数据严重不均衡，低资源语种难以训练专用对齐模块；TASU/TASU2虽证明文本对齐可行但仅限英语，跨语种音系干扰与稀疏性下的共享后验接口能否成立尚属未知。

**模型架构：** 冻结OWSM-CTC v4 1B作为后验提供者（50,002类），按blank阈值0.9做LSD压缩并合并同argmax相邻帧；投影器为单层仿射映射，直接在Top-10后验值-索引稀疏表示上计算，映射到Qwen2.5-1.5B-Instruct替换<speech>占位符；后验模拟器为6编码器+6解码器层Transformer，温度0.5生成后验。八语种共享同一投影器、LLM骨干与LoRA参数，无语种专属模块。

**核心创新：** (1) 首次将TASU扩展至单一共享的多语言Speech LLM，直接复用多语种CTC编码器原生5万维后验空间作跨语言对齐接口，推理时替换为真实音频后验，训练阶段完全免波形。(2) 受控比较启发式CPS、学习式模拟器与真实后验三种监督，在projector-only与LoRA下量化差距：学习模拟器远优于CPS（11.50% vs 20.55%），仅训投影器不足以利用真实后验（波兰语15.09%反升至23.55%），须适配LLM。(3) "文本先行预对齐+少量真实语音校准"课程协议：CPS初始化后用1/9 MLS配对语音适配一epoch得9.19%；并在随机初始化CTC头的Whisper-CTC前端复现，证明结论不绑定特定后验提供者。

**训练策略：** AdamW+700步warmup+余弦衰减，bfloat16+DeepSpeed ZeRO-2，16张Ascend NPU，最多3 epoch/55,000步；LoRA施加于Qwen注意力与FFN投影；高资源语种封顶19.6万句得约110万条平衡训练集。

### 📊 实验结果
**数据集**：MLS八语种（荷/英/法/德/意/波/葡/西），官方切分，WeNet口径池化WER

**主要指标**：
- TASU-Real-LoRA：池化WER 8.21%（vs 独立OWSM-CTC 10.08%，相对降18.6%）
- Projector-only：真实后验9.93% / 学习模拟器11.50% / 启发式CPS 20.55%
- 低配对语音：CPS init+1/9语音一epoch 9.19%，较随机初始化11.04%相对降16.8%
- 模拟器覆盖消融：剔除波兰教师后验致波兰WER 16.38→80.47，其余七语种仅10.79→10.61
- Whisper-CTC复现：基线25.91% → 纯音频TASU 17.62% → 两阶段课程14.67%

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：首次系统性地将文本驱动后验对齐扩展到多语言并给出三监督源的干净量化对比，"文本预对齐+1/9语音校准"协议对低资源语种失衡有直接实用价值，跨编码器复现增强可信度。不足在于方法主体沿用TASU/TASU2属组合式增量，模拟与真实后验分布失配仍未解决，模拟器语种覆盖脆弱性突出，代码未开源且限于MLS朗读语料。

---

## [11] Sequence-to-Sequence Refinement for EEND-VC Diarization with a Shared Encoder

**arXiv ID**：2611.02709 | **方向**：语音前端

**作者**：Ruoyu Wang, Jun Du, Weixin Zhu, Yannan Wang

**机构**：中国科学技术大学（合肥）、Ethereal Audio Lab

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.02709 | **PDF**：https://arxiv.org/pdf/2611.02709.pdf | **代码**：暂无（依赖NSD-MS2S开源库） | **Demo**：暂无

### 📌 简介
EEND-VC（如DiariZen）将局部分割与全局说话人聚类分离优化，导致局部活动检测准确但录音级说话人身份混淆（SC）依然存在。本文提出共享编码器S2S精修：不引入独立声学编码器，而是直接复用DiariZen的SSL（WavLM/剪枝w2v-BERT 2.0）表征，配合说话人条件化解码器与先验约束推理，对身份和重叠人数进行保守修正。在8个数据集（1209条录音）上，冻结特征精修将宏平均DER从12.95%降至12.40%（WavLM）、从12.35%降至12.08%（w2v-BERT 2.0），SC相对下降17.4%/14.6%，仅增加约15% RTF；进一步联合训练分割与精修头后宏DER降至11.90%。

### 🔧 技术方案

**问题背景：** EEND-VC中局部分割与全局说话人分配被分开优化，正确的局部活动和说话人数仍可能得到错误的录音级身份；已有后处理要么改动活动要么需另配独立声学编码器，造成重复编码开销。

**模型架构：** 剪枝后的WavLM或w2v-BERT 2.0（115.8M参数，剪枝率80.05%）作为共享SSL编码器，每窗口只前向一次；分割头与精修头各自学习独立层混合权重再投影。局部分支为256维投影+4层Conformer+power-set分类器；精修分支沿用NSD-MS2S的i-vector与记忆库注册机制（100维i-vector、两组128中心i/x记忆库），6层512维8头解码器，最终状态作说话人吸引子，独立sigmoid并行预测所有候选活动以支持重叠。

**核心创新：** (1) 共享编码器的S2S精修：用DiariZen的SSL表征替换NSD-MS2S的独立声学编码器，精修RTF增量仅0.0027（总RTF 0.0204–0.0207）；两头独立学习层混合，分割与身份修正使用不同SSL层组合而共同更新编码器。(2) 先验约束推理：以DiariZen聚类的全局二值先验提供非重叠注册片段与session i-vector，先保持人数修正身份、仅在概率强于阈值0.8/0.2时增删说话人，静音帧保持静音，保守防止活动被破坏。(3) 联合训练：oracle先验/档案下同时用BCE与power-set损失更新编码器及两头，剪枝后经蒸馏初始化，聚类在计算图外，兼顾检测误差与身份误差的分解优化。

**训练策略：** 8语料混合、16秒窗、40%难窗采样，H20 GPU；冻结模式按0.7/0.3采样DiariZen/oracle先验，AdamW batch 512，dev损失最低5-checkpoint平均；联合模式重初始化、有效batch 128、最多14轮patience 5。

### 📊 实验结果
**数据集**：RAMC、VoxConverse、AISHELL-4、DIHARD III、MSDWild、AMI、AliMeeting、NOTSOFAR-1共8域1209条录音；NIST md-eval零collar计入重叠，宏平均等权。

**主要指标**：
- 宏DER：WavLM 12.95%→12.40%；w2v-BERT 2.0 12.35%→12.08%；联合系统11.90%（最优）
- SC分量：冻结精修相对下降17.4%与14.6%；联合系统内2.99→2.57（相对13.9%）
- 高重叠NSF：18.50%→16.54%；四套会议数据全部改善，RAMC轻微退化
- RTF：0.0177→0.0204（+15.3%）；宏DER最大降1.05个百分点（vs DiariZen）

**是否开源**：暂无（仅复用NSD-MS2S开源组件）

### ⭐ 评分：7/10
评分理由：共享SSL编码器的S2S精修设计直击EEND-VC的SC痛点，误差分解分析清晰可信；8域评测、剪枝模型与RTF报告完整。创新属对NSD-MS2S与DiariZen的结构性组合优化而非全新范式，增益幅度中等（约0.3–1.05 DER点）且RAMC/DH3等场景出现回退，联合训练未隔离单一变量影响，实用价值高但理论突破有限。

---

## [12] ReplayFactor: Replay-Aware Dual-Attribute Learning for Practical Speech Deepfake Detection

**arXiv ID**：2611.02628 | **方向**：语音前端

**作者**：Miao He, Jiayi Zhou, Yu Zheng, Zhongjie Ba, Peng Cheng, Yuxi Zhou, Junjie Zhu, Changhao Zhang, Jian Liu

**机构**：浙江大学区块链与数据安全全国重点实验室；蚂蚁集团

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.02628 | **PDF**：https://arxiv.org/pdf/2611.02628.pdf | **代码**：数据集即将发布（模型代码未提供）

### 📌 简介
现有SSL深度伪造检测器对数字生成语音表现良好，但在物理回放攻击下性能显著退化，且回放感知的检测器设计与数据集多样性均不足。本文提出双属性框架ReplayFactor：将四类标签分解为源属性（人声vs合成）与回放属性（未回放vs重放），用CQCC声学先验经门控融合增强SSL回放证据，并以多任务学习和双空间监督对比学习促进跨条件一致性；同时构建约185k条中文多设备重放合成语音数据集ReplayFake-CN。在EchoFake开放集上，相对基线macro-F1从60.99%提升至76.44%，EER从11.86%降至3.05%。

### 🔧 技术方案

**问题背景：** 物理回放经播放设备、声学环境与录音通道引入失真，会改变甚至掩盖合成伪影，使检测器将重放合成语音误判为真实语音；现有工作主要依赖数据增强或回放仿真，ReplayDF合成方法覆盖有限、EchoFake仅含英语，中文与智能眼镜等设备重放数据缺位。

**模型架构：** 以预训练SSL编码器（MMS-300M）加AASIST时频图注意力后端提取共享表征，经两个属性专属编码器映射为源嵌入与回放嵌入；CQCC静态系数拼接一二阶差分后经LCNN编码为声学先验嵌入，通过样本级门控以残差方式融合进回放支路；分类头为四路主分类器加源/回放两个二值辅助分类器。

**核心创新：** (1) 双属性因式分解：把四类标签显式拆成源与回放两个正交属性，使模型在一个属性变化下学习另一属性，提升未见条件下泛化。(2) 回放感知门控特征融合：CQCC补充SSL难以捕获的高频细微差异与信道响应失真等低层回放线索，逐样本门控自适应调节。(3) 双空间监督对比学习：在源空间中让相同源标签样本跨回放状态聚合、在回放空间中让相同回放标签样本跨源类型聚合，与多任务交叉熵联合优化。

**训练策略：** 四类CE加辅助属性CE与两个对比损失加权；SSL全量微调，Adam带权重衰减，分支分设学习率；四类样本均入每mini-batch，按开发集macro-F1选checkpoint；ReplayFake-CN训练约400k样本混合。

### 📊 实验结果
**数据集**：EchoFake、ReplayDF、ReplayFake-CN（自建184,954条中文、232.5小时、1,921说话人、22个TTS模型，9扬声器×10录音设备共90组合）

**主要指标**：
- EchoFake open：EER 3.05%、macro-F1 76.44%（基线XLSR-Linear 11.86%/60.99%）
- EchoFake closed：EER 0.53%、macro-F1 97.93%，与最强基线持平
- ReplayDF跨数据集：两类F1 38.31%/40.32%，优于基线最高6.73%/25.94%
- ReplayFake-CN：未见合成模型96.95%、未见设备83.00%、联合未见73.75%；公开AntiDeepfake权重仅55.43%
- 消融：去声学先验EER劣化至8.11%，去SupCon macro-F1降至73.89%

**是否开源**：数据集将发布 @ huggingface.co/datasets/Ahola/ReplayFake-CN，模型代码暂无

### ⭐ 评分：7/10
评分理由：面向物理回放这一低成本现实威胁，双属性分解、门控声学先验与双空间对比组合设计清晰，开放集提升显著；自建ReplayFake-CN填补中文多设备重放数据空白。不足在组件多为已有技术组合、原创深度有限，跨语言/跨设备泛化仍差，关键超参披露不全。

---

## [13] GDBack: A Group-Delay Backdoor Attack on Speaker Identification via Analytic All-Pass Filtering

**arXiv ID**：2611.01721 | **方向**：语音前端

**作者**：Bicheng Xiong, Tao Li, Chenhui Cui, Zedong Xing, Qien Li, Weiping Wen, Rubing Huang, Tsong Yueh Chen

**机构**：湘潭大学、北京航空航天大学、北京大学、阿尔伯塔大学、澳门科技大学、斯威本科技大学

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.01721 | **PDF**：https://arxiv.org/pdf/2611.01721.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对说话人识别系统的数据投毒后门威胁，本文提出并验证：跨样本触发一致性可建立在共享变换层面而非共享绝对相位模板之上。GDBack是纯投毒式群延迟后门攻击，以N级级联二阶解析全通滤波器为触发器：同一变换理想保谱、叠加频变相位/群延迟贡献，输出相位仍依赖原始语音。在LibriSpeech与VoxCeleb1上以ECAPA-TDNN、x-vector、RawNet3为victims，单组参数（r=0.90, fc=4000Hz, N=10、5%投毒）六设置ASR均超94%（均值97.00%），良性准确率差距≤1.54pp，WER仅升0.25pp，并躲过Neural Cleanse检测。

### 🔧 技术方案

**问题背景：** PhaseBack向预选时频bin注入预定义相位、StealthPhase用参考语音相位替换最高150个频点，均以共享绝对相位模板实现跨样本一致性，但ASR随数据集与架构剧烈波动（最低分别65.34%与59.42%）；能否不强制统一输出相位而靠共享变换建立一致性尚无答案。

**模型架构：** 闭集all-to-one标签翻转投毒：攻击者以N节相同二阶全通节（极点半径r、中心频率fc、零点关于单位圆镜像，幅频响应恒为1）构建确定性相位变换，作用于随机抽取的训练语句并统一改标为攻击者目标说话人，受害者按正常流程训练；推理期对非目标语句施加同一变换即激活后门。触发器仅由(r, fc, N)=(0.90, 4000Hz, 10)三个解析参数决定，无需参考语音模板或模型梯度优化。

**核心创新：** (1) 变换级触发一致性：以"共享相位变换"取代"共享相位模板"，同批中毒样本叠加相同相位响应与N·τ(ω)群延迟，输出相位保持输入依赖，一致性迁移到变换层。(2) 解析全通隐藏触发：fc控制延迟结构频域位置、r控制集中度、N控制累积延迟强度，单位幅频响应保证Mel频谱与波形无可见异常。(3) 机制解耦：相位/幅度分离、逆全通补偿与参数扫描证明激活源于诱导相位变换——phase-only目标预测率99.80%、magnitude-only仅0.30%、逆补偿后0.10%；fc偏移500Hz即ASR降至1.5%。

**训练策略：** LibriSpeech与VoxCeleb1各取251说话人构建16kHz、3s片段闭集任务；默认投毒率5%；统一触发配置跨两数据集三模型；训练30轮、batch 32、双RTX 4090；基线含PhaseBack、StealthPhase、PaddingBack、PBSM等六种。

### 📊 实验结果
**数据集**：LibriSpeech与VoxCeleb1（各251说话人、16kHz、3s片段）；干扰测试用MUSAN语料。

**主要指标**：
- ASR：单配置均值97.00%（最低94.66%），6/6设置高于StealthPhase（均值76.09%）、5/6高于PhaseBack（均值90.58%）
- BA：与干净模型最大差1.54pp；UTMOS 4.0267、NISQA 4.0826居三种相位攻击之首
- Whisper WER 6.73%（+0.25pp）、STOI 0.9933
- 鲁棒性：0.8/1.2增益与80ms时移下ASR 99.6–99.8%；混响下82.0–96.2%；OTA空放ECAPA 96.50%、x-vector 99.00%、RawNet3 78.00%
- 防御：Neural Cleanse异常指数1.71低于阈值2未检出；干净数据微调50轮ASR几乎不降

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：将相位域触发一致性从"模式层"重构到"变换层"具备真实概念新意，解析参数化+相位分离/逆补偿的机制归因实验明显强于同类工作；双数据集、三架构、六基线加OTA与四类防御评估充分。局限在闭集换标投毒场景偏理想、RawNet3空放跌至78%、未触及clean-label，属扎实进阶而非突破。

---

## [14] Spatially-Guided Speaker Extraction Based on Relative Position Cues

**arXiv ID**：2611.01757 | **方向**：语音前端

**作者**：Aviad Eisenberg, Shlomo E. Chazan, Sharon Gannot

**机构**：Bar-Ilan University（以色列）、OriginAI（以色列）

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.01757 | **PDF**：https://arxiv.org/pdf/2611.01757.pdf | **代码**：暂无 | **Demo**：https://aviad3189.github.io/RPC-extraction/

### 📌 简介
针对多通道目标说话人提取（TSE）依赖注册语音或显式DOA先验、在混响与动态场景下不稳健的问题，本文提出RPC（相对位置线索）：用说话人之间的离散相对空间关系（左/右、近/远）编码目标身份，无需DOA/RTF估计与注册音频。该框架与骨干无关，分别集成进U-Net提取模型与SpatialNet。实验显示4麦SpatialNet-RPC达14.2dB SI-SDR（超过盲分离基线SpatialNet的13.2dB），U-Net-RPC较DOA条件版高0.7–1.2dB；仅用静态数据训练即可在移动说话人与扩散babble噪声下保持稳健（退化≤0.9dB）。

### 🔧 技术方案

**问题背景：** 现有TSE的条件信号要么需要目标干净语音（可能缺失或与环境失配），要么依赖精确DOA/RTF估计（混响、噪声、动态下不可靠）；区域/扇区式线索仍以麦克风阵列为参照、需要绝对角度，且无法区分同处一个预定义区域的两个说话人。

**模型架构：** 两说话人定义8条关系指令、三说话人定义9条（近/远×左/右组合），每条指令对应一个可学习查询表嵌入。U-Net骨干经FiLM将指令嵌入注入混合表征；SpatialNet骨干将指令嵌入在每个窄带块Self-Attention前与帧级特征拼接。输入输出均为STFT实虚部沿通道维拼接，目标为参考麦克风处的混响目标语音。

**核心创新：** (1) 关系式而非区域式条件："左/近"相对于干扰说话人定义，目标-干扰边界不固定、需网络从混合信号中推断，双方同在阵列一侧或同距离段仍可区分，且完全规避DOA估计。(2) 架构无关的指令注入机制：查表嵌入+FiLM/拼接两种写法即可改造现有分离/提取网络，SpatialNet提取版甚至反超其盲分离版，证明关系线索本身携带有效梯度信号。(3) 动态场景的局部注意力掩码：关系按帧瞬时成立，全局自注意力会聚合跨帧伪关联；限制每帧注意力窗口后，模型零运动数据训练即可泛化到移动说话人。

**训练策略：** SI-SDR损失（每说话人轮流作目标，对每混合3种空间变体取平均）；LibriSpeech+DNS仿真，SNR 5–20dB；RT 0.2–0.8s、4麦ULA 8cm（2麦取中间两麦）；8kHz，STFT帧长256；4秒片段、AdamW、lr 1e-4；按说话人数与阵列规模分别训练。

### 📊 实验结果
**数据集**：LibriSpeech+DNS仿真（2/4麦、三组空间间隔测试集）、Hadad IWAENC实测RIR（360ms RT）、20人环形babble、移动轨迹。

**主要指标**：
- 4麦两说话人SI-SDR：SpatialNet RPC 14.20 dB、U-Net RPC 11.02 dB（STOI最高0.911）
- 3说话人4麦：SpatialNet RPC 6.70 dB，超oracle MVDR（5.70 dB）
- 关键对比：SpatialNet提取版比其分离版+1.0 dB；U-Net RPC比DOA条件版+0.7–1.2 dB；4→2麦仅降0.2–0.5 dB而MVDR降约4 dB；扩散babble最大退化0.9 dB；目标选择正确率98.4–100%

**是否开源**：代码未开源，音频样例公开于Demo页面

### ⭐ 评分：7/10
评分理由：以说话人间相对位置替代DOA/注册的条件设计直觉、可解释且工程代价低，两种骨干一致验证通用性；实验覆盖阵列数、说话人数、实测房间、弥散噪声与动态源。不足：假设所有说话人全程同时激活且人数已知；同向小间隔场景性能下降明显；未与区域基线直接对比，代码未开源。

---

## [15] SPHERE: A Multi-Attribute No-Reference metric for Binaural Speech Quality And Spatial Fidelity

**arXiv ID**：2611.00402 | **方向**：语音前端

**作者**：Bala Manikya Prasad Puram, Chandan K A Reddy, Artem Dementyev

**机构**：Google LLC

**发布日期**：2026-11-03 | **论文**：https://arxiv.org/abs/2611.00402 | **PDF**：https://arxiv.org/pdf/2611.00402.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对双声道（binaural）语音在耳机、智能眼镜等穿戴设备上缺乏无参考多维质量度量的问题，论文提出SPHERE框架：定义覆盖核心音质、空间沉浸与干扰伪影的9项感知属性（MOS-SIG/BAK/OVRL、听力省力、响度舒适、声源定位、空间稳定性、干扰伪影、背景噪声行为），并配套ITU-T P.808众测协议与硬件预筛模板人工标注。作者构建约9000条10-20秒双声道真实标注数据，训练Mel/STFT/PhaseCoder空间特征融合的6种小模型（321k-353k参数）。实验显示平均Clip PCC达0.706、System PCC达0.770，显著超越单声道DNSMOS基线，验证了自动多维空间语音质量评估的可行性。

### 🔧 技术方案

**问题背景：** PESQ/POLQA/ViSQOL等传统指标仅单声道，无法感知声源定位与方位感；NISQA/DNSMOS/SESQA等无参考深度模型虽可预测多维音质但对空间退化"失明"；PEAQ/AMBIQUAL等多声道指标需全参考信号且不评估听力省力、语音失真、神经增强伪影等语音专属维度。

**模型架构：** 混合CNN-RNN回归多任务框架，输入10秒立体声。Non-Siamese分支：左右声道特征沿通道维堆叠，经5个2D-CNN卷积块、2层BiLSTM（128单元）与全局平均池化到256维，路由9个独立回归头，共321k参数。Siamese分支：左右各用权值共享的2D-CNN编码，融合层投影对齐后并入同一BiLSTM主干（约330k参数）。MEL+SF配置额外拼接预训练PhaseCoder的256维麦克风几何无关双耳相位嵌入，约353k参数。

**核心创新：** (1) 9维双耳主观评测模板：整合ITU-T P.835/P.800核心音质、P.810听力省力、P.830空间沉浸、P.811/Supp.29空间漂移与伪影，并设置低分根因交叉校验（Part 4），保证MOS标签可解释。(2) 双耳专用众测质控协议：硬件类别预筛（禁用外放）、左右耳相位抵消声学验证、音量校准、gold anchor与陷阱样本，5人/条以压缩SEM。(3) 对称归纳偏置：Siamese权值共享编码显式约束ITD/ILD物理对称性，在系统级基准化上大幅优于非共享结构；同时以自监督PhaseCoder嵌入注入几何无关空间先验。

**训练策略：** Adam、batch 128、TPU、等属性权重WMSE，每500步按验证PCC选checkpoint。两阶段增强（Apache Beam）：10秒窗2秒步长滑窗弱监督传播标签，叠加时移、增益、极性反转等感知不变变换；按干净基准文件名做说话人/会话级无泄漏80/20划分。最终训练集433,396条，验证集12,554条。

### 📊 实验结果
**数据集**：自建双声道众标库，约9000条10-20s真实耳机/HATS/外场录音，9属性×5人评分。

**主要指标**：
- 平均Clip PCC：0.706（Non-Siamese MEL+SF最佳）；SRCC 0.660、RMSE 0.726
- System PCC：0.770（Siamese MEL）vs Non-Siamese MEL 0.715；空间维度定位0.910、空间稳定0.867
- Quality Tier PCC：全部模型>0.99
- 单属性最优：MOS-BAK 0.807、MOS-OVRL 0.773、MOS-SIG 0.669
- 关键对比：DNSMOS仅OVRL 0.284/BAK 0.460/SIG 0.054，SPHERE领先约0.3-0.6 PCC且可预测全部9维

**是否开源**：暂无

### ⭐ 评分：6/10
评分理由：9维主观模板+严格硬件质控的众测协议与无泄漏切分规范具工程示范价值，Siamese系统级优于clip级的发现有实际指导意义。但模型仅0.35M参数、结果偏基线验证性质，PCC 0.7量级精度有限，空间属性预测明显弱于音质属性，数据与代码均未开源；属高质量增量工作。

---

## 📄 更多语音论文（紧凑列表）

> 以下 7 篇为当日语音相关论文，未进入精读队列，仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），按预估评分从高到低排列。

**Zero-Shot Voice Cloning for Synthetic Data Augmentation in Children's ASR**
- **arXiv ID**：2611.03050 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2611.03050（未精读，按摘要评分）

**ufakzeka-kulak: Building and Evaluating a 31.6M-Parameter Turkish Speech Recognizer from Scratch**
- **arXiv ID**：2611.03605 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2611.03605（未精读，按摘要评分）

**Microphone Geometry Aware Regional Target Speaker Extraction**
- **arXiv ID**：2611.00894 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2611.00894（未精读，按摘要评分）

**Continual Residual Memory for Gradient-Free Test-Time Adaptation in Speech Enhancement**
- **arXiv ID**：2611.01023 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2611.01023（未精读，按摘要评分）

**Pop Goes the Verifier: Phoneme-Targeted Data Poisoning of Voice Liveness Detection**
- **arXiv ID**：2611.01095 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2611.01095（未精读，按摘要评分）

**High Frequency Safeguard and Weighted Objective Scoring Bandwidth Extension**
- **arXiv ID**：2611.02235 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2611.02235（未精读，按摘要评分）

**Q-BWE: Quantum Chaos-Informed Speech Bandwidth Extension**
- **arXiv ID**：2611.02250 | **方向**：语音前端 | **评分**：5/10 | **链接**：https://arxiv.org/abs/2611.02250（未精读，按摘要评分）

*Subagents used for reading: 15* | Generated on 2026-11-03 语音论文批次, by Kimmy's research agent | Powered by VAgent SpeechAI Researcher
