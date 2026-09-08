# 2026-09-08 语音论文速递

**共收录**: 20 篇 | **语音大模型**: 17 篇 | **语音前端**: 3 篇

> 目标日期 2026-09-08（北京时间）arXiv 语音相关论文共命中 20 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue

**arXiv ID**：2609.04250 | **方向**：语音大模型

**作者**：Chengqian Ma、Wei Tao、Haoyu Zhang、Yiwen Guo

**机构**：北京大学、LIGHTSPEED、香港中文大学（深圳）、独立研究者

**发布日期**：2026-08-28 | **论文**：https://arxiv.org/abs/2609.04250 | **PDF**：https://arxiv.org/pdf/2609.04250.pdf | **代码**：GitHub 与 Hugging Face（论文注明 Code and data available） | **Demo**：https://step-out.github.io/Motion-Omni-Page/

### 📌 简介
口语对话模型（SDM）只能产出语音而不能产出伴随动作，语音驱动动作模型则无法规划对话应答，常规级联方案需在音频完成后再做一次完整动作推理，且动作目标无法反向更新语音与对话参数。本文提出 Motion-Omni，首个原生端到端输出面部表情与手、上体、下体全身动作的口语对话框架，动作直接从产出语音的 Speech Generator 隐状态生成。以 Qwen2.5-7B-Instruct 为骨干的 Motion-Omni-Q7 在参考无关运动指标上以 2% 以内差距贴近同音频教师级联，响应速度快 5.4 倍（RTF=0.78、快于实时），口语 WER 低至 2.62%（Omni-modal 系统中最低）。

### 🔧 技术方案

**问题背景：** 级联方案存在两大结构性代价：动作模型在音频生成完成后要执行第二次独立推理；运动目标永远无法更新语音或对话参数。近年口语运动模型也未完全解决该问题。核心挑战有三：语音与动作处于异构帧率（12.5 Hz 语音单元 vs 30 Hz 动作）、共享参数时两条损失互相干扰，且没有大规模一致嗓音的运动监督与公开评测基准。

**模型架构：** 框架含四组件。Speech Encoder 为冻结的 Whisper-large-v3 编码器（隐维度 1280），Speech Projector 每 5 帧拼接一次并过两层 MLP 降采样 5 倍后注入 LLM。LLM 骨干为 Qwen2.5-7B-Instruct。Speech Generator 从 Qwen2.5-0.5B-Instruct 初始化，自回归输出 GLM-4-Voice 12.5 Hz 离散语音单元（16,384 词表），经 Token-as-Query Gated Fusion（TQGF）按 head-wise sigmoid 门掩码查询 LLM 隐状态。Motion Generator 含四个并列 per-part 解码器（face/hand/upper/lower），每个用 2 层 TQGF（K/V 来自 Speech Generator 末层隐状态）加 6 层带周期 30 帧周期旋转位置编码的自注意力（30 Hz），query 为语音单元嵌入线性插值至 30 Hz 的序列，最终以部件专属 MLP 头在 256 码条目上输出 logits。总参数约 8.3B。推理时语音单元经 CosyVoice flow-matching 解码器转 mel，再经 HiFi-GAN 风格声码器合成 22.05 kHz 波形；动作码由冻结的 LOM VQ-VAE 解码为 SMPL-X/FLAME 参数。

**核心创新：** (1) 双输入门控条件接口（K/V 取自生成语音的隐状态、query 为插值到运动率的语音 token 嵌入）将运动变成 SDM 原生输出，终端推理去掉独立 audio-to-motion 阶段；消融显示联合共适配（motion loss 反向更新 LLM 与 Speech Generator）是必需的。(2) 四阶段渐进训练课程（ASR→TTS→TTSM→四任务联合混合），TTSM 阶段按质量分位 12.5%/25%/50%/100% 递进热身；阶段间 FGD 从 0.3974 稳定降至 0.3040。(3) 模型无关的伪标注流水线：LOM 教师标注每段响应波形，产出 422,856 对（1,402 小时）监督；并发布 SwDA-500 与统一渲染、参考感知自动指标、人工 A/B 与延迟测量的评估协议。

**训练策略：** 总损失为 LLM 下一 token 交叉熵加语音单元 label-smoothing CE 加四部件按特征维度加权的运动 CE（权重 face:hand:upper:lower=106:180:78:61）。各阶段合计 436 万样本/12144.6 小时训练语料。44 张 GPU、DeepSpeed ZeRO-2、BF16、梯度检查点、有效 batch 128。峰值学习率：Stage1/2 用 cosine（SP 1e-3、SG 1e-4）；Stage3 恒定加 warmup（SG 1e-5、MG 2e-4）；Stage4 热启（LLM 2e-7、SP 1e-6、SG 5e-7、MG 2e-6）。总训练成本约 960 GPU-hours。

### 📊 实验结果
**数据集**：Seed-TTS-Eval（1,088 样本）、VoiceBench（九子集）、SwDA-500；训练语料 InstructS2S-200K、Ex-Instruct 等

**主要指标**：
- WER：Motion-Omni-Q7 2.62%，Omni-modal LLM 中最低（Qwen2.5-Omni 2.72、Ex-Omni 2.67）
- VoiceBench Overall：47.63（LLaMA-Omni 41.12、Ex-Omni 43.57、Moshi 29.51）
- SwDA-500：Diversity 13.67、BC 7.59、LSE-C 7.011、教师参考 FGD 3.03；八项指标七项第一或第二
- 延迟：Tresp 4.32 s、RTF 0.78，比级联（23.35 s、4.39）快 5.4 倍
- 人类 A/B：对 MO-audio+EMAGE 胜率差 +25（45 胜/10 平/20 负）
- UTMOSv2 3.77；课程 FGD 0.3974→0.3040

**是否开源**：开源。代码发布于 GitHub、数据发布于 Hugging Face，项目页 https://step-out.github.io/Motion-Omni-Page/

### ⭐ 评分：9/10
评分理由：首个将面部与全身动作作为口语对话模型原生输出并让运动目标反向适配 LLM 与语音生成器的端到端工作，四阶段课程与消融充分验证了联合共适配的必要性，评估协议与开源数据代码俱佳。扣分点在于运动质量受教师伪标签上限约束、仅支持英文、为离线响应生成器，且人工评估规模有限。

---

## [2] The Trade-off Was in the Labels: Causal Supervision for Turn-Aware Streaming ASR

**arXiv ID**：2609.04225 | **方向**：语音大模型

**作者**：Bojie Li, Noah Shi

**机构**：Pine AI, University of Washington

**发布日期**：2026-07-12 | **论文**：https://arxiv.org/abs/2609.04225 | **PDF**：https://arxiv.org/pdf/2609.04225.pdf | **代码**：https://github.com/19PINE-AI/turn-aware-asr | **Demo**：https://01.me/research/turn-aware-asr

### 📌 简介
语音智能体的核心难题是判断用户何时说完话：VAD 加静音超时（业界默认方案）无法区分话内停顿与话间停顿，任何单一超时阈值都无法同时应对"读电话号码""one-word 命令""长问题"三类话轮。本文提出首个开源的 turn-aware 流式 ASR 完整训练配方：在 Qwen3-ASR-0.6B 上接一个 LoRA 适配器，用约两万条合成样本、单卡数小时训练，使一个 checkpoint 同时具备增量转写、语义端点检测、听写保持和上下文偏置能力。在部署匹配的 replay 基准上达到 0.969 边界召回、0.39 秒中位延迟、每分钟 0.3 次误触发，所有静音超时设置与现有开源 turn-aware 系统均达不到该工作点。

### 🔧 技术方案

**问题背景：** 现有端点检测路线（VAD+静音超时、下游分类器、或与识别器联合训练）都只间接获取"语义完整度"这一本应收音机副产品，且各开源/商用系统均未披露训练方法与标注规程。核心发现在于：用离线语料训练流式决策会系统性违反因果性——离线 clip 被强制对齐切成"说话即结束"，标签依赖决策点之后的音频（未来信息），作者称之为 clairvoyant 标签，会造成训练振荡和虚假的"召回-精度 Pareto 前沿"。

**模型架构：** 基座为 Qwen3-ASR-0.6B，在注意力 q/k/v/o 投影及两个新标记 token 的 embedding/head 行上加 LoRA（α=2r，r16/r32）。每个 0.5 秒 chunk 做一次 committed-prefix 增量解码，将未用的两个词表行声明为 <EAGER_END_SPEECH> 和 <END_SPEECH> 标记，模型在转写流中直接输出 fire。解码端另设能量门、confirm horizon h、force-flush 三个外部旋钮。

**核心创新：** (1) 因果监督原则：提出"每个流式决策标签必须可由决策点之前的输入计算"的因果性原则，当且仅当"已说词语义完整"且"观察到至少 0.3 秒静音"时输出双 fire 标记。(2) 成对构造训练数据：八种 schema（约 1.2 万端点样本），minimal-pair 迫使模型依赖可观测静音而非完整性，pause-pair 教会"沉默中语义判断"，silence-heavy 等 schema 杜绝噪声下幻觉 fire。(3) 反事实双子构造修复上下文轴泄漏：增加 1/3"上下文与音频冲突、目标跟随音频"的反事实样本，把入侵率从 40% 压到 0.8% 而保持 +28.9pp 实体召回增益。

**训练策略：** AdamW，批量 8，学习率 2e-4 经 100 步 warmup 后余弦衰减到 1e-5，权重衰减 0.01，约 1.2 万步；统一模型混入 20% 纯转写 replay 样本纠正离线 WER 回归；Muon 优化器因 LoRA 因子矩形度过低而劣于 AdamW。合成数据来自 LibriSpeech 与 AMI 各约各半，统一池约 20k。

### 📊 实验结果
**数据集**：AMI、LibriSpeech、Free Spoken Digit Dataset、Earnings-22

**主要指标**：
- 端点（25 段 dev）：0.969 边界召回、P50 0.39 秒、P95 0.70 秒、0.3 次 false fire/分钟；fresh 50 段 0.924/0.42 秒/0.2 次
- 统一模型（100 段 held-out）：0.982 边界召回、1.30 次 false fire/分钟
- 超时族对比：无任一超时设置可达该工作点，匹配其召回需 3 倍延迟和约 5 倍误报
- 听写探针：提前 fire 由 4.96 次/号降至 0.16 次，数字准确率 0.998
- 上下文偏置：实体召回 +28.9pp；入侵率 40%→0.8%
- 离线 WER：基座 2.79%/5.14%，端点 LoRA 3.93%/7.87%，统一模型恢复至 3.49%/6.90%

**是否开源**：开源。代码、标签规范构建器、replay 基准、探针均发布于 github.com/19PINE-AI/turn-aware-asr

### ⭐ 评分：9/10
评分理由：首次给出 turn-aware 流式 ASR 的完整开放训练配方与部署匹配基准，填补了商用系统与开源模型均不披露训练细节的空白；"clairvoyant 标签"概念精准普适，八种监督组合的开发记录、单变量干预诊断和合成隔离实验构成严谨证据链。限制：仅单说话人单声道英文、证据集中于 AMI、checkpoint 为研究原型。

---

## [3] GhostWord: A Fine-Grained Backdoor Attack on Automatic Speech Recognition

**arXiv ID**：2609.04260 | **方向**：语音大模型

**作者**：Mojtaba Nafez, Mobina Poulaei, Kiarash Kiani Feriz, Aref Mousavi, Mohammad Ebrahim Mahdavi, Mohammad Mosayebi, Mohammad Hossein Rohban

**机构**：EPFL（洛桑联邦理工学院）、谢里夫理工大学、伊斯法罕大学

**发布日期**：2026-09-02 | **论文**：https://arxiv.org/abs/2609.04260 | **PDF**：https://arxiv.org/pdf/2609.04260.pdf | **代码**：https://github.com/rohban-lab/GhostWord | **Demo**：暂无

### 📌 简介
现有 ASR 后门攻击普遍采用短语级投毒范式：固定声学触发加固定恶意目标句、整句转录被替换，导致数据集中出现大量完全相同转录、触发常挂在非语音区，可被 VAD 裁剪、转录去重等简单预处理轻易清除。本文提出 GhostWord，一种词级、时间定位的 ASR 后门攻击：以码本将约 400 ms 声学触发与目标单词绑定，投毒时用强制对齐定位所选源词的时间区间，仅将该词替换为目标词，实现精确语义翻转与可组合的句子级操控，规避多对一转录伪迹。在 Common Voice 英文/立陶宛语及 Whisper-Small/Medium、MMS、SpeechT5 四个骨干上平均攻击成功率达 89.3%；对比下 BadNet/Blended 可被预处理防御彻底清除，而优化类防御（ABL/ANP/SAU/I-BAU）可将攻击率降至 29.1%，但干净词错率由 21.5% 升至 45.0%，暴露鲁棒性-精度权衡。

### 🔧 技术方案

**问题背景：** 现有 ASR 后门均为短语级投毒，产生两类结构性伪迹：大量重复的固定转录（可被频率统计或转录过滤识别）、触发附于非语音区（可被 Silero 等 VAD 直接裁剪）。作者指出 ASR 词表远超 1 万类且输出为变长序列，后门抑制（梯度上升式 unlearning）会把概率质量按 softmax 梯度重新分配给与目标 token 高对齐的"runner-up"簇，结构性地损害干净识别，且词表越大、几何拥挤越严重。

**模型架构：** 核心是码本式投毒管线。每个码本条目绑定一个固定约 400 ms 声学触发与目标词。投毒流程：按比例 α 采样训练子集，随机选源词，用 MMS（CTC 目标）强制对齐得到其时间区间，在区间内软叠加触发（保证注入段 SNR≥22 dB），转录仅把源词替换为目标词。触发由四类噪声（高斯、拉普拉斯、带限高斯、粉噪）随机选取后固定，经 300–3400 Hz 中频带通与方差归一化（16 kHz）。默认 4 个码本、10% 投毒率；多码本可复合实现多词句子级操纵。

**核心创新：** (1) 词级时间定位范式：用强制对齐把触发精确嵌入源词发音区间，仅翻转单个词，避免短语级攻击的重复转录与 VAD 可除伪迹，转录词频仍符 Zipf 分布无可检测突刺。(2) 码本式多触发-多目标绑定：一个触发绑定一个目标词、跨说话人无关，支持同一片段多码本组合操控，且目标词碰撞检测保证成功率无虚假通胀。(3) 系统适配 ABL、ANP、SAU、I-BAU 四种优化类防御到 ASR，并给出高词表下防御必然损害干净精度的几何学论证，验证对 Neural Cleanse、STRIP 等自适应防御的抵抗能力。

**训练策略：** 干净微调 10 轮，lr 1e-5，10% 线性 warmup 后线性衰减；Whisper-Small batch16，Whisper-Medium lr 5e-6，MMS-1B lr 5e-5（立陶宛 1e-4），SpeechT5 lr 1e-4。英文用 CV23 训练集 1%（11429 句约 18.2 小时），立陶宛语用 CV24 全量（9008 句约 12.9 小时）。

### 📊 实验结果
**数据集**：Common Voice v23（英文）、v24（立陶宛语）

**主要指标**：
- 无防御下 GhostWord 平均攻击成功率：89.3%（跨 2 语言 4 模型）
- BadNet/Blended 无防御 97.4%，经转录去重后降为 0.0%
- GhostWord 对转录去重/VAD 免疫：攻击率仍约 83–93.5%
- 最优防御 ANP/i-BAU/SAU 下降至 29.1%，但干净 WER 由 21.5% 升至 45.0%（i-BAU 降攻击至 3.6% 时 WER 达 50.2%）
- 投毒率 1% 时仍达 65.9%；码本扩至 10 个时 68.9%
- 跨域迁移：Whisper v3 Turbo 85.3%；MP3 16kbps 压缩后 61.1%
- 人因实验：触发定位正确率 42.4%（随机 33%），94.7% 判定词清晰/可懂

**是否开源**：开源（https://github.com/rohban-lab/GhostWord ，CC BY 4.0）

### ⭐ 评分：9/10
评分理由：第一次将 ASR 后门从句级整体替换推进到词级时间定位，码本绑定与强制对齐设计工程完备，系统适配四种优化类防御并给出高词表下鲁棒性-精度权衡的几何直觉论证，跨模型跨语言实验与消融非常扎实，且开源并附人因评测。扣分点在于理论分析停留在单步梯度非正式层面，防御侧缺乏同时保护干净精度的可行方案。

---

## [4] VocalCoachBench: Benchmarking Audio-Language Models on Expert Feedback for Singing

**arXiv ID**：2609.04241 | **方向**：语音大模型

**作者**：Hayeon Bang, Hounsu Kim, Wonil Kim, Juhan Nam

**机构**：KAIST（韩国科学技术院）

**发布日期**：2026-08-06 | **论文**：https://arxiv.org/abs/2609.04241 | **PDF**：https://arxiv.org/pdf/2609.04241.pdf | **代码**：暂无具体 URL（标注数据、提示词与评估代码将公开释放） | **Demo**：暂无

### 📌 简介
当前音频语言模型评测集中于描述、识别与问答，缺乏对"面向专家的分析式反馈"能力的检验。本文提出 VocalCoachBench，首个面向演唱声乐教练式反馈的专家标注评测基准：含 515 条演唱录音，由 18 位职业声乐教师产出 1052 份反馈与 12051 条原子教练断言。基准将确定性结构化任务（三元组排序、Top-3 问题标签、分段问题分类）与基于原子断言的开放式诊断/纠正评测分离。实测 12 个最新音频语言模型：三元组两两比较可达 74.5%（Qwen3.5-Omni Plus，随机基线 50.0%），但细粒度 Top-3 问题识别 F1@3 全部低于标签先验多数基线 62.4%，严格诊断命中率全部低于 7%，揭示模型"能宽泛描述却不能精准定位问题"的能力断层。

### 🔧 技术方案

**问题背景：** 现有歌唱自动评估聚焦打分、排序等感知质量判断，基准数据多为小型、平台私有，音乐表演反馈资源面向钢琴/器乐且不将诊断与纠正的有效性本身作为评测目标。关键难点在于声乐教练反馈天然开放——同一演唱不同教练会给出不同主次问题与纠正策略，单一标量分无法刻画。两轮预实验证实标量评分格式失败：4 位专家对齐评分标准后整体 Krippendorff's α 仅约 0.323，分歧源于刻度"阈值校准"，故最终移除标量评分。

**模型架构：** 本文构建评测基准并评估 12 个现成音频语言模型：开源主协议为 R1-AQA、Qwen2.5-Omni、Qwen3-Omni、Fun-Audio-Chat、MiMo-Audio、Kimi-Audio；短格式模型 Audio Flamingo 3、Music Flamingo；闭源 API 为 GPT-Audio 1.5、Gemini 3 Flash Preview、Qwen3.5-Omni Flash/Plus。评测包含结构化套件（三元组两两比较、七类问题标签 Top-3 预测、262 条共识片段单类分类）与开放套件（LLM judge 将模型自由文本与专家原子断言逐条比对，威胁标签 strict/coarse/miss/contradict 与 valid/weak/invalid）。

**核心创新：** (1) 双子集共构设计：同歌子集（Amazing Grace，按自动音高准确率分层 1:2:1 采样）控制旋律与难度；多歌子集（9 个公开歌唱集）提供多样化场景，每人最多 4 条防偏差。(2) 以"可评估的教练动作"取代打分的标注协议：按 feedback block 组织并标注七个细粒度问题类别，全部反馈经确定性解码拆分为带 target 链接的原子 claim，单作者审计零遗漏零幻觉。(3) 双层评测掌握专家分歧：可约束判断做确定性评估，开放文本按原子 claim 覆盖与矛盾评估，并给出 judge 与人的一致性验证。

**训练策略：** 不训练任何模型，全部评估为推理。推理尽可能 temperature=0 确定性解码；标注人员 18 名、时薪约 20 美元、全程约 7 天；252 个共识片段（IoU≥0.3 且共享标签）支撑片段评测。

### 📊 实验结果
**数据集**：DAMP-S-AG（同歌）、PopBuTFy、N20EMv2、LM-SSD、NUS-48E、MedleyDB、MedleyVox、MRSSing、URSing、GTSinger（多歌），共 515 条录音

**主要指标**：
- 三元组两两比较：Qwen3.5-Omni Plus 74.5% 最佳，开源最佳 Qwen2.5-Omni 68.7%，Fun-Audio-Chat 49.3% 低于随机 50.0%
- 细粒度 Top-3 F1@3：所有模型均未超过多数基线 62.4%
- 严格诊断命中率：全部低于 7%（最高 6.9%）；宽泛命中率 17.1%–63.2%
- 纠正有效性：Qwen3.5-Omni Plus 98.4%，而 Qwen2.5-Omni 仅 31.7%
- 预实验：标量评分专家间 Krippendorff's α 约 0.323

**是否开源**：标注数据、元数据、提示词与评估代码声明公开释放；部分源数据集不允许重分发原始音频。

### ⭐ 评分：8/10
评分理由：这是首个系统化评测"面向声乐的专家诊断+纠正式反馈"的公开基准，18 名专家、12051 条原子断言的标注规模与质量控制扎实，双层评测设计与 judge 一致性验证具有方法论价值，实验清晰暴露"宽泛可答、精准失灵"的能力差距。扣分：仅英语单语与单一同歌手曲，开放指标依赖专家 claim 参考，未报告统计显著性检验，代码无显式链接。

---

## [5] ProLombard: Structured Multi-Scale Modeling for Normal-to-Lombard Speech Conversion

**arXiv ID**：2609.04828 | **方向**：语音大模型

**作者**：Hongyang Chen, Xinmeng Xu, Youqiang Zheng, Xingyu Liu, Yuhong Yang, Zhongyuan Wang, Weiping Tu, Song Lin

**机构**：武汉大学国家多媒体软件工程技术研究中心；Song Lin 来自 OPPO 移动通信

**发布日期**：2026-09-04 | **论文**：https://arxiv.org/abs/2609.04828 | **PDF**：https://arxiv.org/pdf/2609.04828.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
常规语音到 Lombard 语音转换（N2L）旨在噪声环境下提升语音可懂度，但现有方法仅在语句级或帧级建模 Lombard 效应，忽略了其层级结构及其与说话人身份、音素级内容纠缠的本质，导致说话人表征中 Lombard 泄漏、内容特征分离不彻底。本文提出 ProLombard，一种结构化多尺度 N2L 框架，在语句级、音素级和帧级三个时间尺度上显式建模 Lombard 效应：设计对齐说话人编码器（ASE）通过跨风格嵌入对齐抑制 Lombard 泄漏；提出音素感知的 Lombard-内容解耦与注入机制；设计 VQ-median 模块，结合矢量量化分割与中位帧聚合得到可靠的音素级表征。在 EMALG（中文）与 Lombard Grid（英文）上，LMUSHRA 达 72.40（基线最高 69.37）、QMUSHRA 达 82.01（基线最高 74.25）、F0RMSE 降至 50.48、可懂度 WRR 达 41.31，全面优于各基线。

### 🔧 技术方案

**问题背景：** 现有解耦式 N2L 方法（如 PGD-N2L、LombardTokenizer）面临两大瓶颈。其一为 Lombard-说话人纠缠：预训练说话人确认模型以身份判别为目标而非去除风格变化，导致 Lombard 信息残留在说话人嵌入中（Lombard 泄漏）；对抗式或互信息式解耦缺少显式跨风格对齐监督，在说话人稀缺的低资源场景下难以兼顾身份保持与解耦。其二为 Lombard-内容纠缠：Lombard 效应随音素变化（共振峰位移、元音时长延长），帧级解耦无法覆盖；现有音素级方法多用外部模型分割后做简单池化，分割边界不可靠且会损伤内容保真。

**模型架构：** 整体基于 PGD-N2L 骨干（内容编码器、后验编码器、归一化流、HiFi-GAN 解码器、判别器），按三层尺度组织。语句级：Lombard 编码器为可学习查找表，将离散噪声级（L55/L80）映射为 Lombard 嵌入；ASE 用预训练 ECAPA-TDNN 抽取输入语音嵌入，经线性 Lombard 移除模块抑制变化后与平行正常语音参考嵌入对齐。音素级：VQ-median 模块含 VQ 分割（码本大小 200）、中位帧聚合、可学习上采样与时长预测器。De-Lomb/En-Lomb 块构成互补解耦-注入对，分别在音素级与帧级工作：De-Lomb 经 GRL 对抗训练使参数预测器无法从内容特征预测 F0、响度、alpha ratio 等 Lombard 参数。

**核心创新：** (1) 对齐说话人编码器（ASE）：引入跨风格对齐损失 L_spk，用平行正常语音嵌入监督 Lombard 嵌入，首次将说话人编码目标与风格不变建模对齐。(2) 音素感知 Lombard-内容解耦与注入：将 De-Lomb/En-Lomb 块扩展至音素级，以 VQ 段内帧级参数均值构造音素级训练目标，联合帧级形成层级解耦。(3) VQ-median 模块：以 VQ 码本游程做端到端可学习分割，用中位帧聚合替代池化/质心以保留内容保真，配合可学习上采样与时长预测器。

**训练策略：** 总损失 L_total = L_hier + L_PGD + L_dur + 5×L_spk + L_VQ；L_PGD 含 KL、重建、对抗与特征匹配损失；重建损失在 Mel L1 基础上新增幅度谱谱能量距离损失。训练 450k 步，单块 NVIDIA 4090，batch size 64，最大段长 128 帧；扰动采用 NANSY 系数；推理统一将正常语音转换为最高噪声级 L80。

### 📊 实验结果
**数据集**：EMALG（中文，10200 句、34 说话人）；Lombard Grid（英文，5400 句、54 说话人）；基线为 CycleGAN、StarGAN、PGD-N2L、DurFlex-Lomb；主观评测 20 名听者

**主要指标**：
- LMUSHRA（EMALG）：ProLombard 72.40±1.90，优于 CycleGAN 69.37、PGD-N2L 61.41（真实 Lombard 93.31）
- QMUSHRA：82.01±1.59，优于 PGD-N2L 74.25、StarGAN 69.94
- F0RMSE 50.48（CN）/53.28（EN）均最优；αRME 1.06（CN）/2.58（EN）均最优
- WRR（ASR 可懂度）：41.31（CN 最优）；EER 8.88（CN）；UTMOS 3.36（CN）/4.07（EN）
- 效率：42.84 G FLOPs、32.79 M 参数，较 PGD-N2L 仅增 1.8 M 参数
- 消融：VQ+Median 组合 WRR 41.31 显著优于 VQ+Pooling 的 20.24；删除音素级 De-Lomb/En-Lomb 均致指标回退

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：对 Lombard 效应的层级性洞察深刻，首次将音素-帧-语句三尺度结构与显式解耦目标引入 N2L，ASE 跨风格对齐直接解决 SV 模型目标不匹配问题，中英文双语五类指标改进一致且开销极小。扣分：未开源与无 Demo，优化器/学习率等超参缺失，部分英文指标未达最优。

---

## [6] KanAdapter: A Kolmogorov-Arnold Network-based Plug-and-Play Module for Efficient Fine-tuning of Foundation Speech Models

**arXiv ID**：2609.05281 | **方向**：语音大模型

**作者**：Phuong Tuan Dat, Phuong Khai Minh, Tran Huy Dat

**机构**：新加坡国立大学（NUS）、A*STAR 高级智能与计算研究所

**发布日期**：2026-09-04 | **论文**：https://arxiv.org/abs/2609.05281 | **PDF**：https://arxiv.org/pdf/2609.05281.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全文微调自监督（SSL）语音大模型计算开销巨大，而现有参数高效微调（PEFT）方法主要依赖 MLP 适配器，其固定激活函数在紧凑参数预算下表征能力受限。本文提出 KanAdapter，一种基于 Group-Rational KAN（GR-KAN）的即插即用适配器框架，采用并行瓶颈设计，在冻结的 Transformer 编码器旁插入可训练 GR-KAN 分支，并从预训练 MLP 层迁移权重实现稳定初始化。在说话人验证、语音情感识别与深度伪造检测三个任务上，KanAdapter 相对全量微调最高减少 97.5% 可训练参数（SV 仅 9M 参数），性能仍紧逼全量微调（Vox1-O EER 0.52% 对比 0.49%），并在相近参数预算下全面优于 AdaptFormer 与 LoRA；在持续学习场景中相比全量微调在 LA19 上 EER 下降 83.6%。

### 🔧 技术方案

**问题背景：** 现有 PEFT 方法应用到语音 SSL 模型时建模能力受限：LoRA 本质是无非线性激活的线性低秩分解，难以刻画伪造痕迹、情感分布等复杂语音特征；AdaptFormer 的 MLP 瓶颈使用固定激活，表达力不足。针对语音 SSL 的 PEFT 研究仍少见，将 KAN 类可学习激活模块用作适配器此前尚属空白。

**模型架构：** 骨干完全冻结，SV 与 SER 采用 WavLM-Large，DFD 采用 XLSR-300M。每个 Transformer 层保留原始冻结 MLP 分支，并行插入 KanAdapter 分支：输入经 LN 与下投影 W_down（d→128），中间用 GR-KAN 层替代 MLP/ReLU，再经上投影 W_up，输出由可学习标量 s 缩放后与冻结 MLP 输出残差融合。GR-KAN 以可学习 Padé 有理函数（Safe Padé Activation Unit，单次求值仅 21 FLOPs）替代 B 样条基函数；分组参数共享，组内共享有理系数而每条边保留独立标量权重，总参数量仅比标准 MLP 多常数开销。

**核心创新：** (1) 首次将 KAN 模块（GR-KAN）引入语音基础模型 PEFT，构建"下投影+GR-KAN+上投影"并行适配器，用可学习有理激活提升非线性表征能力，结构上类似 LoRA 却具备非线性中间变换。(2) 权重迁移初始化：下投影权重取自骨干预训练 MLP 层、上投影置零，保证初始输出为零、保持原模型行为。(3) 验证并归因 GR-KAN 局部有理激活的抗灾难性遗忘特性，持续学习下显著超越全量微调与 MLP 适配器（LA19 EER 相对下降 83.6%）。

**训练策略：** 仅更新 W_down、W_up、GR-KAN 有理系数与缩放因子 s；统一 dhat=128，s=0.1。SV 在 VoxCeleb2 训练，SER 在 MSP-Podcast，DFD 在 ASVspoof2019 LA，沿用公开框架默认配置。消融显示 dhat=128 最优。

### 📊 实验结果
**数据集**：VoxCeleb2/VoxCeleb1（说话人验证）、MSP-Podcast（SER）、ASVspoof2019/2021/5、In-The-Wild（深度伪造检测）

**主要指标**：
- 说话人验证（9M 可训练，削减 97.5%）：Vox1-O 0.52%，全量微调（364M）0.49%，AdaptFormer（8M）1.44%，LoRA（4M）2.25%
- SER（16M，削减 95.2%）：Test F1-Macro 0.3290，保留全量 99% 性能；AdaptFormer 0.2310、LoRA 0.1822
- 深度伪造检测（17M，削减 94.7%）：LA19 0.34%、LA21 1.32%、DF21 5.93%、LA5 18.40%
- 持续学习（ASVspoof2019→ASVspoof5）：LA19 0.86% 四项全最优，较全量下降 83.6%
- 跨骨干泛化：WavLM-Large/UniSpeech-SAT/mHuBERT-147 参数削减 91–95%

**是否开源**：暂无（基于 WeSpeaker、XLSR-Conformer、MSP-Podcast Challenge 三个公开框架实现）

### ⭐ 评分：8/10
评分理由：首次将 KAN/GR-KAN 用作语音基础模型的即插即用适配器，动机清晰、设计简洁且可迁移，实验覆盖三任务、四评估框架与持续学习场景，证据较充分。扣分点在于未开源代码、持续学习仅两阶段、未覆盖 ASR 等序列生成任务，且缺乏对 GR-KAN 优势的机制级分析。

---

## [7] EffVOC: Low-Delay Efficient Speech Waveform Reconstruction from Spectral Representations Without Phase

**arXiv ID**：2609.04226 | **方向**：语音大模型

**作者**：Shi Renzheng, Simon Welker, Timo Gerkmann, Tim Fingscheidt

**机构**：布伦瑞克工业大学（TU Braunschweig）、汉堡大学（Universität Hamburg）

**发布日期**：2026-07-14 | **论文**：https://arxiv.org/abs/2609.04226 | **PDF**：https://arxiv.org/pdf/2609.04226.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
EffVOC 面向无相位谱表示的低延迟语音波形重建。现有方法中，Griffin-Lim 算法（GLA）算法延迟极高；RTISI 系列在 20 ms 延迟下质量骤降；DiffPhase、BAPEN 等神经网络方法依赖整句重建、延迟无限；BigVGAN、Vocos、MelFlow 等生成式声码器普遍存在 32 ms 以上延迟。EffVOC 在已有 20 ms 低延迟声码器基础上统一支持幅度谱与 Mel 系数两种输入，可合成宽带（16 kHz）与全带（48 kHz）语音。VCTK 实验表明：F=32 宽带模型取得 MOS 4.17/4.15，距真实语音 4.20 仅 0.05 分；全带最小 Mel 模型（6.57 M 参数）MOS 4.11，全面超越 MelFlow 等基线。

### 🔧 技术方案

**问题背景：** GLA 及其快速变体需大量迭代、算法延迟极高；RTISI 虽延迟 20 ms，但缺少前视致重建精度严重下降。神经网络方法用生成式手段大幅提升质量，但依赖整句重建或延迟超 32 ms；MelFlow 用流匹配实现实时，仍为 32 ms 延迟。低延迟声码器目前仅支持 Mel 输入与宽带合成，幅度谱输入及更高带宽的适用性尚无定论。

**模型架构：** EffVOC 保留原低延迟模型的高效上采样转置卷积结构与循环层：2 个卷积层、2 个 LSTM 层、4 个转置卷积层（每层后接一个 ResBlock），全部因果卷积并做权重归一化。特征提取采用周期 Hann 窗，窗长 20 ms、帧移 5 ms（75% 重叠）；宽带 DFT 512 点、全带 1024 点，幅度谱取 K/2+1 个非冗余频点，Mel 滤波数为 80。以通道数 F（∈{64,32,16,8}，参数 0.47 M–27.19 M）控制尺寸。

**核心创新：** (1) 首次在单一重建模型中统一比较幅度谱与 Mel 两种谱表示，同一框架可配置宽带或全带输出。(2) 以低至 20 ms 算法延迟实现接近真实语音的主观质量，75% 高重叠带来更强时频冗余，缓解稀疏频率点映射到 80 维 Mel 通道的重建难度。(3) 系统研究 F 因子缩放与 stride 深度对质量、参数量、GFLOPS 及实时因子的影响，最小模型仅 0.47 M 参数、0.584 RTF。

**训练策略：** 生成器与判别器联合对抗训练，超参遵循 BigVGAN 官方实现，初始学习率 1e-4、批量 32、总步数 1M。数据为 VCTK，训练集约 35.8 小时/93 人；主观评测按 ITU-T P.808 众包进行。

### 📊 实验结果
**数据集**：VCTK（宽带 16 kHz / 全带 48 kHz），基线含 GLA、RTISI、DiffPhase、BAPEN、MelFlow

**主要指标**：
- MOS：F=64 幅度谱 4.17、F=32 Mel 4.15，对比 MelFlow 3.95、GLA 3.95、RTISI-DM 2.76，真实语音 4.20
- PESQ-WB：F=64 幅度谱 4.31（优于 BAPEN 4.26）；POLQA 4.45；LPS 0.976；ESTOI 0.94
- RTF：F=64 幅度谱 0.652，优于 MelFlow 5 迭代 0.719
- 全带：F=32 幅度谱 MOS 4.14、最小 Mel 模型（6.57 M）MOS 4.11，均超 MelFlow 3.89/3.85
- 复杂度：F=32 幅度谱仅 9.73 GFLOPS，比 MelFlow 25 迭代（7050 GFLOPS）低两个数量级

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：在 20 ms 算法延迟约束下首次统一验证幅度谱与 Mel 两种输入表示在宽带/全带下的重建表现，主观 MOS 逼近真实语音并全面超越同延迟基线，F 与 stride 的系统消融给出清晰复杂度-质量关系，工程价值突出。扣分：架构为对既有低延迟声码器的适配改进，缺少本质性方法创新，未开源代码与 Demo。

---

## [8] Robust Speech Emotion Recognition under Tone-Word Conflict: A Benchmark and Framework

**arXiv ID**：2609.04236 | **方向**：语音大模型

**作者**：Xiaojiang Peng, Dawei Huang, Yongjie Lv, Ruijie Xiong, Chunxiang Jin, Bin Li, Xiaohui Wang, Zitong Yu

**机构**：深圳技术大学、蚂蚁集团、创维数字技术、小派科技、大湾区大学

**发布日期**：2026-07-27 | **论文**：https://arxiv.org/abs/2609.04236 | **PDF**：https://arxiv.org/pdf/2609.04236.pdf | **代码**：https://github.com/24DavidHuang/FAS | **Demo**：暂无

### 📌 简介
现有语音情感识别（SER）系统默认音调与词义一致，但现实交互中普遍存在"声调-词义冲突"（反讽、冷怒等），主流方法在此场景下性能崩溃。针对这一问题，论文构建了首个高密度冲突基准 TWIN-SER（378 条多语言样本，经 LLM 场景生成与 TTS 合成），并提出 DAS（解耦声学-语义融合）框架：通过 MingTok-Audio 声学 tokenizer 与 Whisper 语义编码器双路径解耦、基于能量得分的高信息嵌入选择、轻量 Q-Former 跨注意力自适应融合。实验表明，DAS 在 TWIN-SER 上达 59.38% WA、55.08% WF1，超越最强基线 Whisper（47.26%）12 个百分点以上，且在 MELD、RAVESS、ESD 及零样本数据集上均保持竞争力。

### 🔧 技术方案

**问题背景：** 论文指出现有方法存在三类结构缺陷：一是语音-文本联合预训练模型（Whisper、CLAP）存在语义偏置，模型被字面含义"污染"；二是 SSL 编码器（HuBERT、wav2vec2、WavLM）产出声学与语义纠缠表征，冲突难以消解；三是大语音语言模型（Qwen2-Audio、Qwen2.5-Omni）的编码器优先语义而削弱韵律情感线索。同时社区缺乏控制变量式的高密度冲突评测基准。

**模型架构：** DAS 由三个模块构成。（1）异构特征提取：声学路径用 MingTok-Audio tokenizer 提取 64 维表征，语义路径用 Whisper-large 编码器提取 1280 维特征，分别以窗口大小 5 的平均池化 patchify 压缩。（2）显著 patch 选择：以 token 的 ℓ2 范数能量分数做 saliency 打分，非均匀 top-k 选择，默认声学 k_aco=8、语义 k_sem=16，投影对齐到 d=512。（3）Q-Former 融合：n=2 个可学习查询向量经跨注意力、残差、LayerNorm、MLP 交替融合，MLP 头输出 7 类情感概率。全模型仅 3.45M 参数。

**核心创新：** (1) 首创将神经音频 tokenizer（MingTok-Audio）作为 SER 声学情感表示专用通路，与语义编码器显式解耦，克服主流编码器表征纠缠。(2) 提出非均匀能量 top-k patch 选择，仅保留情感高激活片段，抑制冲突场景下相互干扰的冗余信息。(3) 引入 Q-Former 式查询融合，以可学习查询动态分配声学/语义权重，支撑零样本泛化。

**训练策略：** 采用 6 数据集（MER2024、IEMOCAP、CMU-MOSEI、MELD、RAVDESS、ESD）合计 66 小时以上训练语料。AdamW，学习率 2×10⁻⁴，余弦衰减，权重衰减 1×10⁻⁴，dropout 0.4，全局 batch 2048，训练 100 轮，16kHz 采样，8 张 A6000，损失为交叉熵。

### 📊 实验结果
**数据集**：MER2024、IEMOCAP、CMU-MOSEI、MELD、RAVDESS、ESD（训练）；TWIN-SER（冲突基准）；Emo-Emilia、EmoDB（零样本）

**主要指标**：
- TWIN-SER：DAS WA 59.38 / WF1 55.08，最强基线 Whisper 47.26 / 44.97，HuBERT 32.90、Qwen2.5-Omni 34.66
- 退化证据：HuBERT 在 ESD 上 80.1%、TWIN-SER 上跌至 32.9%；Qwen2.5-Omni 从 RAVDESS 75.35% 跌至 34.66%
- ESD：87.27/86.72；RAVDESS：76.61/76.19；MELD：51.89/48.42（F1 最优）
- 消融：能量 top-k（59.38）优于随机 55.47 与全注意力 55.99；Q-Former（59.38）优于 Concat 53.65 与 Gated 53.12
- 查询数 Nq=8 时 TWIN-SER 达 60.5%；零样本 Emo-Emilia 51.14、EmoDB 68.10

**是否开源**：开源，代码与数据集位于 https://github.com/24DavidHuang/FAS

### ⭐ 评分：8/10
评分理由：首次系统性定义并评测音调-词义冲突场景，TWIN-SER 基准流水线严谨可控，DAS 解耦-选择-融合设计简洁有效，冲突场景相对基线提升显著且消融充分。瑕疵：基准仅 378 条样本两种语言，fear 与 disgust 类无方法可识别；DAS 在标准与零样本集上低于专用模型，且仅基于预提取特征。

---

## [9] Rethinking Speech Codecs: From Compression to Autoregressive Generative Modeling

**arXiv ID**：2609.04237 | **方向**：语音大模型

**作者**：Yazheng Yang, Yao Qiu, Hui Su, Qi Liu

**机构**：香港大学、美团

**发布日期**：2026-07-27 | **论文**：https://arxiv.org/abs/2609.04237 | **PDF**：https://arxiv.org/pdf/2609.04237.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
主流神经语音编解码器以压缩保真为目标训练，其离散 token 序列缺乏自回归建模所需的时序条件依赖，统计分布偏离自然语言的 Zipf 幂律，与 LLM 的下一个 token 预测范式严重错位，导致语音大模型续训效率低下。本文提出 ARDDS 编解码器训练框架：在 codec 训练中引入辅助自回归解码器，通过温度控制的软量化实现梯度回传，显式约束 token 序列的自回归可预测性；同时提出异构下采样策略，将第一层（语义层）token 率降至 6.25 Hz、声学层保持 12.5 Hz，使语音 token 在时间粒度上对齐文本。基于该框架继续训练 LLaMA-3 8B 语音大模型，StoryCloze 准确率达 70.1（+6.4），AISHELL-I 字错误率降至 2.5（-2.7），SeedTTS 词错误率降至 2.3（-2.4），且可推广到 SpeechTokenizer、BigCodec、XCodec-2 等多种 codec。

### 🔧 技术方案

**问题背景：** 现有语音编解码器以多尺度梅尔谱重建损失、LSGAN 判别损失等联合优化，仅关注率失真与感知质量，对 token 序列的时序结构没有任何约束。作者统计发现各代表 codec 的 token 频率-排名关系明显偏离文本 Zipf 幂律分布，token 缺乏可预测的条件依赖；且第一层语义 token 速率（如 XCodec 50 Hz）远高于对应文本，增加语音大模型续训练负担。这是"压缩目标"与"生成目标"的结构性错位。

**模型架构：** 框架保持原 codec 编码器、量化器、解码器结构不变，整体损失为 L = L_ori + λ·L_AR。新增轻量自回归解码器 A_ψ（6 层、隐藏维度 2048、16 头），与编码器和量化模块联合训练。对每个编码器输出特征计算温度软分配概率 p_t(i)=exp(-‖x_t-c_i‖²/τ)/Σ_j exp(-‖x_t-c_j‖²/τ)，以软概率喂给 A_ψ 实现梯度经量化模块回传。异构下采样对第一量化层做平均池化，语义层 token 率由 50 Hz 降至 6.25 Hz，声学层保持 12.5 Hz。

**核心创新：** (1) 首次将自回归正则化嵌入 codec 训练目标：以交叉熵最大化 P(y_{t+1}|y_{≤t})，把"下一个 token 可预测性"作为归纳偏置引入量化学习，重塑 token 分布使其逼近 Zipf 形态。(2) 温度软离散赋值作为可导桥梁：τ 取 0.01 时近似 one-hot，保证梯度流经量化器进入编码器。(3) 异构下采样策略：语义层与声学层不同帧率（6.25 vs 12.5 Hz），使语义 token 速率接近文本，附录证明 6.25 Hz 是稳定训练下界（3 Hz 时 commit loss 严重发散）。

**训练策略：** 正则项权重 λ=1，温度 τ=0.01。Codec 统一用 LibriSpeech + Common Voice 23 中文子集训练。下游 SpeechLM 以 LLaMA-3 8B 为骨干，任务动态采样比 interleaved:ASR:TTS=90:1:1，约 40 万小时中文语音语料，32 张 A100，初始学习率 1e-4。

### 📊 实验结果
**数据集**：LibriSpeech、Common Voice 23；StoryCloze、AISHELL-I、SeedTTS（下游）；约 400k 小时中文语音语料

**主要指标**：
- XCodec:ARDDS 下游：StoryCloze 70.1%（+6.4）、AISHELL-I CER 2.5%（-2.7）、SeedTTS WER 2.3%（-2.4）
- 编解码器内在质量：重建 WER 4.13、SPKSIM 0.88、UTMOS 4.30、PESQ-nb 3.53，与基线相当
- 消融：w/o AR 为 67.0/74.2/4.2/3.5，w/o DDS 为 67.1/74.7/3.8/3.4，均显著低于完整模型
- 泛化：SpeechTokenizer、BigCodec、XCodec-2 均提升且重建质量不降；token 分布更趋 Zipf 幂律

**是否开源**：暂无（实验基于开源 XCodec 实现，未提供 ARDDS 实施代码）

### ⭐ 评分：8/10
评分理由：首次从自回归生成视角重设计 codec 训练目标，软量化梯度回传工程简洁可行，异构下采样动机清晰；实验覆盖推理、ASR、TTS 多任务并通过多种 codec 验证通用性，Zipf 分布分析增强可解释性。扣分：精细消融仅基于 XCodec，验证集中于单一语言与单一骨干，未提供开源代码。

---

## [10] TurnFSM for Full-Duplex Dialogue System: Internalizing State-Machine Logic for Streaming Semantic Voice Activity Detection and Utterance-Level Rejection

**arXiv ID**：2609.04240 | **方向**：语音大模型

**作者**：Zhiwei Lin, Tianjiao Du, Qiaochu Huang, Zihan Zhang, Naijun Zheng, Longshuai Xiao, Yunfei Lu, Jun Chen, Zhiyong Wu

**机构**：未在文中明确标注

**发布日期**：2026-08-05 | **论文**：https://arxiv.org/abs/2609.04240 | **PDF**：https://arxiv.org/pdf/2609.04240.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工语音助手需在持续播放语音的同时监听用户输入，实时处理打断、流式分工和无效输入拒绝。现有端到端方案会让模型在下游推理能力上退化，级联流水线则引入额外推理开销和手工状态机控制逻辑。本文提出 TurnFSM，一种基于 LLM 的流式控制状态预测框架，将级联管线的外部决策逻辑内化为显式有限状态转移（Start、Silence、Listen、Submit、Accept、Reject 六态），并设计一阶状态转移机制（FOSTM）实现训练-推理一致的紧凑单遍预测。实验表明：流式语义 VAD 成功率 82.41%、拒绝误报率 3.35%，优于双头基线并接近单任务专用模型，在 EasyTurn 话语级测试集上准确率 91.00%。

### 🔧 技术方案

**问题背景：** 现有全双工系统分两类：端到端统一建模（如 Moshi、GLM-4-Voice）接口简洁、天然处理重叠，但语音域适配会损害预训练文本推理与工具调用能力；工业级联管线（声学 VAD、语义 VAD、话语级拒绝逐级串联）稳健但引入额外开销、级间误差传播和手工状态机。折中方案是在共享流式骨干上加双预测头，但两任务决策准则异构，平行标签会在共享表征上产生梯度冲突。TurnFSM 的出发点即消除这种多任务耦合。

**模型架构：** 三模块组成：流式音频编码器为两层 VGG 风格卷积前端加 6 层 Conformer，输出 25 Hz 声学帧；音频适配器为轻量 MLP 做 2 倍下采样，映射进 LLM 空间（音频 token 率 12.5 Hz）；LLM 骨干采用 Qwen2.5-7B-Instruct。音频编码器初始化自内部预训练流式 ASR 模型并冻结为声学骨干。训练分两阶段：第一阶段冻结编码器与 LLM，仅训练适配器做跨模态对齐（ASR）；第二阶段解冻适配器与 LLM，优化状态预测目标。

**核心创新：** (1) 显式有限状态转移框架：定义 6 个离散状态 token 内化级联决策逻辑，将提交与拒绝放入不同决策阶段，规避共享表征的多任务干扰。(2) 一阶状态转移机制（FOSTM）：训练时对交错音频-状态序列施加修改的因果掩码，使状态 S_t 只能关注声学前缀与前一状态，并通过位置绑定保持声学时序。(3) 紧凑推理范式：推理时用 (A_0,...,A_t,S_(t-1)) 直接预测 S_t，无需逐步生成中间状态，兼容流式与话语级两种场景。

**训练策略：** 对齐阶段用 AISHELL-1/2、WenetSpeech 共 11200 小时语料做 ASR 对齐，16 张昇腾 910b NPU、lr 6e-5、batch 256、2 轮；状态预测阶段用内部语义 VAD 数据集（7 万训练/800 测试，194 小时）和内部拒绝检测数据集（70 万训练/3 千测试，2000 小时），64 张昇腾 910b NPU、lr 2e-5、batch 64、4 轮。

### 📊 实验结果
**数据集**：内部流式语义 VAD 与拒绝检测评测集；开源 EasyTurn 话语级测试集

**主要指标**：
- 流式语义 VAD 成功率：TurnFSM 82.41%，优于双头基线（80.29%），显著高于 TEN（58.75%）、Smart Turn（68%）、Easy Turn（69.5%）
- 拒绝误报率（FAR）：3.35%，与 Rejection-only 3.31% 相当；误拒率（FRR）16.04% 低于双头 18.38%
- 成功延迟：80.9 ms，低于双头 119 ms；整体延迟 222.7 ms
- EasyTurn 话语级准确率：91.00%，优于 TEN 87.99%、Smart Turn 74.67%，仍低于 Easy Turn 97.00%
- 消融：去掉 FOSTM 后成功率降为 81.97%、延迟升至 111.35 ms；去掉跨模态对齐后早切率升至 15.83%

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：将级联全双工管线的手工状态机逻辑提炼为 LLM 内化的显式状态转移，用一阶依赖配合掩码与位置绑定优雅解决训练-推理一致性和状态 token 累积问题，工程可落地，指标接近单任务专用模型且优于双头基线。扣分：内部数据集与 ASR 预训练细节缺失、未开源复现门槛高，属系统化工程改进而非范式突破。

---

## [11] Training-Free Speech-Centric Omni Understanding with Frozen VLMs

**arXiv ID**：2609.04242 | **方向**：语音大模型

**作者**：Ankan Deria, Hanoona Rasheed, Xilin He, Fahad Shahbaz Khan, Salman Khan

**机构**：穆罕默德·本·扎耶德人工智能大学（MBZUAI）

**发布日期**：2026-08-07 | **论文**：https://arxiv.org/abs/2609.04242 | **PDF**：https://arxiv.org/pdf/2609.04242.pdf | **代码**：https://github.com/mbzuai-oryx/OmniEvalKit | **Demo**：https://mbzuai-oryx.github.io/OmniEvalKit

### 📌 简介
原生 Omni 模型需引入专用音频编码器并依赖大规模音视频文本联合训练，音频通路与特定 VLM 骨干强耦合，成本高且脆弱，并可能削弱其既有视觉、推理与领域能力。本文提出 TFO（Training-Free Omni），一个即插即用的免训练框架：仅用 Whisper 将音频转为经过置信度过滤、带时间戳的转写文本，经 VLM 原有语言接口注入，视觉通路完全不变。在 56 个基准、21 种语言、四个模型家族五档规模的严格同规格对比中：TFO 在视听理解上与原生态 Omni 相当（Qwen2.5 系列平均 +3.0/+2.2），多语言语音理解提升最大达 +18.4 分，并更完整地保留图像/视频理解、编程、数学、医学问答与视觉定位能力；主要短板是非语音声学推理（MMAR-Bench 上普遍下滑 1.5 至 9.5 分）。

### 🔧 技术方案

**问题背景：** 原生 Omni 模型通过为 VLM 附加音频编码器并做大规模多模态对齐获得语音能力，但存在三点根本困难：一是每次 VLM 骨干升级都要重做音频通路适配；二是音频信号须与语音内容和视觉事件精确对齐，文献表明原生训练的视听模型仍会忽略相关音频、凭视觉臆测声音；三是修改并联合训练骨干会削弱既有能力。现有评估缺乏与原生训练严格对照的免训练基线，无法回答"音频通路是否对每类任务都必需"。

**模型架构：** TFO 将所有音频证据压缩为语言级上下文：y=Lθ(Ev(V), P(CA,Q))，视觉编码器与语言骨干完全冻结。音频路由实例化为 Whisper-large-v3-turbo（单声道 16kHz、温度 0），将音频分解为{文本、语种、起止时间、置信度}分段，按阈值 τ=0.65 过滤不可靠段；若全部低于阈值则省略音频上下文。融合阶段构造提示 P=[system]⊕[V]⊕[CA]⊕[Q]，长音频用 30 秒分块、3 秒重叠处理。可选语音输出由 CosyVoice3 转语音，不参与评测。

**核心创新：** (1) 音频到语言路由范式：用置信度过滤加时间戳的 Whisper 转写替代 VLM 侧可学习音频通路，语音理解能力随 ASR 前端随换随用。(2) 构建原生 Omni、其原始 VLM 骨干与免训练版本的五组同家族同规模配对对照，分离"语音路由能否恢复 Omni 能力""冻结骨干是否保留原能力""何处仍需丰富声学表征"三个问题。(3) 消融验证逐段时间戳对时序视听推理的定向增益（移除后 AVUT-Gemini、AVMeme-Full、Daily-Omni 各降 2.3/1.7/1.4 分），并系统检验 SenseVoice、MELLOW、AudioFlamingo2、BEATs、CLAP 等辅助声学模型。

**训练策略：** TFO 全程零训练、零微调。评测协议贪心解码、温度 0；在 AMD Instinct MI210 上完成；长答案用 LLM 判分，多选与翻译类采用精确匹配、ROUGE-L 或 BLEU-1；自研 OmniEvalKit 统一评测工具链。

### 📊 实验结果
**数据集**：56 个基准：10 个视听 Omni（UnoBench、WorldSense、AV-Odyssey、Video-Holmes、AVMeme、AVUT、Daily-Omni、AVHBench）、14 个图像/视频、9 个纯音频（CoVoST2、FLEURS、MMAR-Bench、VoiceBench 等）、8 个编码数学、12 个医学问答、4 个定位基准；21 种语言

**主要指标**：
- 视听理解：Qwen2.5-3B 43.2→46.2（+3.0）、7B 45.8→48.0（+2.2），WorldSense 最高 +14.5
- 多语言转写：五档 +7.9/+13.5/+18.4/+11.1/+6.8，MiniCPM4.5 达 64.0
- 纯音频理解：全五档提升，VILA 档 50.3→63.8（+13.5）；MMAR-Bench 全线滑 1.5~9.5
- 图像/视频理解全保留甚至提升；视觉定位 PixMo-Count 全五档提升（VILA +15.5）
- 时延：AVMeme 上由原生 0.7~2.4 秒增至 1.3~3.1 秒

**是否开源**：评估工具链 OmniEvalKit 开源（github.com/mbzuai-oryx/OmniEvalKit）；TFO 属开箱即用组合

### ⭐ 评分：8/10
评分理由：以严格的同规格配对对照实证回答"是否每个新 VLM 都需要原生 Omni 训练"，56 基准 21 语言、四族五档规模的评测体系与开源工具链工程价值高，消融厘清 Whisper、时间戳与辅助声学模型的贡献边界。扣分：框架技术含量有限（核心即 ASR 转写接入提示词），对非语音声学任务失败分析属定性层面，评测中编码题用 LLM 判定而非官方 pass@1。

---

## [12] Brain2Speech-Net: Intelligible, Real-Time Brain-to-Speech Synthesis Without Text Decoding

**arXiv ID**：2609.04455 | **方向**：语音大模型

**作者**：Shreeram Suresh Chandra, Zexin Cai, Yu Tsao, Simon King, Berrak Sisman

**机构**：约翰霍普金斯大学、中央研究院、爱丁堡大学

**发布日期**：2026-09-03 | **论文**：https://arxiv.org/abs/2609.04455 | **PDF**：https://arxiv.org/pdf/2609.04455.pdf | **代码**：https://b2s-lang.github.io/ | **Demo**：暂无

### 📌 简介
针对瘫痪或 ALS 患者失去语音能力的问题，speech BCI 需从皮层神经信号直接合成语音。现有级联式"脑→文本→语音"系统推理延迟高（RTF 大于 1.6）且错误逐级累积；直接预测离散语音单元的方法在脑内数据不足 6 小时时缺乏语言结构先验，产出不可懂语音。本文提出 Brain2Speech-Net，首个在有限数据下保持可懂且超实时的单阶段神经-语音框架：以可微音素瓶颈（帧级音素后验）保留语言结构而不显式解码文本，轻量可微 deep-HMM 将该瓶颈对齐到预训练 VITS 文本编码器的上下文化音素表征。在脑神经假体数据集上，闭集 PER 0.109、WER 0.068、MCD 4.632，实时因子 0.504（快于实时），开集 MOS 3.34，远超 DSU 基线（PER 0.758）并逼近级联系统（PER 0.078）。

### 🔧 技术方案

**问题背景：** 级联范式先解码文本再由独立 TTS 合成，强 LM 先验可能覆盖神经证据而非修正之，多级处理既抬高延迟又使后端继承且无法恢复前端错误。speech BCI 脑内数据极度稀缺，纯端到端大词表训练困难；而直接声学单元方法在小样本下因缺显式语言结构而不可懂。

**模型架构：** 单阶段三模块。脑内容编码器为 5 层 GRU（窗口核宽 32、步长 2），输入 256 运动皮层通道阈值跨越计数与 spike 频带功率，输出帧级音素表征（d_bc=41），Phase 1 用 CTC 损失预训练。脑帧编码器（线性层加 3 个残差 MLP 块，d_f=256）将音素表征映射为 HMM 观测序列。deep-HMM 为左到右无跳转模型，状态对应 CPR 序列中音素段位置加自吸收 EOS 态，转移概率由两隐层 MLP 预测，发射得分为负欧氏距离。前后向后验 gamma 加权池化后由 4 层 Transformer 与残差细化 MLP 回归 CPR 段向量。

**核心创新：** (1) 可微音素瓶颈：以帧级音素后验分布充当神经与语音间的结构化、带不确定性的语言表征，保留音素内容又剔除声学与韵律可变性，规避显式文本生成。(2) 轻量可微 deep-HMM 段对齐：用神经网络参数化发射与转移的逐段单调 HMM 学习神经帧与 CPR 段对齐，无需帧级对齐监督，借预训练 VITS 编码器条件先验实现极低数据训练。(3) 两阶段训练加单程推理：推理时以 k-means 初始化的发射原型表替代真实 CPR 并预测段数 N，实现"神经→CPR→波形"一次前向的实时合成。

**训练策略：** 总损失为 CPR 段回归 MSE、段数交叉熵与辅助 CTC 之和（λ_CTC=0.1）。数据为 Willett 等 2023 年脑神经假体数据集（单名 ALS 患者、四枚微电极阵列），训练目标由单说话人 VITS 合成伪语音，共 8800 训练句/880 测试句、5.71 小时。Adam，batch 32，峰值学习率 1e-3（内容编码器微调 1e-5）。

### 📊 实验结果
**数据集**：Willett 等（2023）脑神经假体数据；闭集 880 句、开集官方测试集 880 句

**主要指标**：
- 闭集 PER：0.109，DSU 基线 0.758，NTS-Cascade 0.078（+LLM 重排 0.069）
- 闭集 WER 0.068、MCD 4.632，优于 DSU（1.011/6.004）
- 开集 PER/WER：0.373/0.472，显著优于 DSU（0.785/1.054），低于级联（0.209/0.229）
- RTF：0.504（闭）/0.532（开），级联 1.664 至 1.962
- MOS：3.34（20 名英语听者、开集）

**是否开源**：开源。提供代码与预训练模型，https://b2s-lang.github.io/

### ⭐ 评分：8/10
评分理由：可微音素瓶颈加深度 HMM 段对齐的组合在脑内数据极稀缺条件下首次实现可懂且快于实时的单阶段脑到语音合成，与级联及 DSU 基线的多指标对比附听感实验，证据较充分且开源。不足：训练与评估目标均为 VITS 合成伪语音，开集泛化与级联差距明显，仅单一被试，且缺少核心模块消融实验。

---

## [13] Tracing Audio Grounding and Answer Selection in Audio LLMs

**arXiv ID**：2609.04637 | **方向**：语音大模型

**作者**：Hyebin Cho, Suho Yoo, Jihoo Jung, Joon Son Chung

**机构**：KAIST（韩国科学技术院）

**发布日期**：2026-09-04 | **论文**：https://arxiv.org/abs/2609.04637 | **PDF**：https://arxiv.org/pdf/2609.04637.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
音频大语言模型（Audio LLM）常依赖文本线索或语言先验答题而非真实听音，即便音频信息极度缺乏时仍能保持较高 AudioQA 准确率。现有应对方法用"无法仅凭文本作答"的数据训练，精度确有提升，但模型内部发生了什么改变仍不清晰。本文对 Qwen2-Audio 与 Qwen2.5-Omni 两个模型、在零样本（ZS）与 LoRA 微调（FT）状态下开展机制可解释性分析，回答"训练如何增强音频证据使用"。三大发现：(1) 替换输入为静音或无关音频后 FT 模型精度下降远大于 ZS 模型；(2) 音频信息在早-中层塑造选项表征，而训练主要强化中间至后期选项表征对最终答案的贡献；(3) 训练学到的 LoRA 更新集中于特定层带。消融表明仅训练 8–15 层的 Qwen2-Audio 可逼近全层训练性能。

### 🔧 技术方案

**问题背景：** 现有评测关注预测是否真正由声学证据支撑（幻觉、模态冲突、证据缺失），但已有研究指出模型可在几乎无声学证据时保持高 AudioQA 性能，说明基准精度与实际听音之间存鸿沟。机制层面工作虽已探究音频信息在模型中的表示与传播位置，却未说明训练如何改变音频信息最终驱动答案选择的过程。

**模型架构：** 任务为多项选择 AudioQA。研究对象为 Qwen2-Audio 与 Qwen2.5-Omni，比较原始指令微调检查点（ZS）与 LoRA 适配检查点（FT）。训练数据为 AudioMCQ-StrongAC-GeminiCoT（答案需依赖音频才能作答，共 19,480 样本），丢弃思维链标注。LoRA 秩 r=16、α=32、dropout 0.05，应用于音频编码器与 LM 目标模块，输入音频截断至 30 秒。评估 ADQA-Bench、MMAU-test-mini、MMAR、MMSU 均不参与训练。

**核心创新：** (1) 提出行为级"声学证据敏感度"指标 Saudio=Aorig−(Asil+Amis)/2，以全零静音与随机错配音频两种扰动衡量模型对有效声学证据的依赖。(2) 将注意力敲除扩展到音频-选项-答案三段连接，用标签重归一化后的正确选项概率变化 Δp 捕捉置信度层面的干预效应。(3) 提出 LoRA 层带归因协议：既做"功能必要性"消融又做"适配充分性"训练，揭示了禁用带与孤立训练带作用不一致的现象。

**训练策略：** 训练样本仅含 4 个选项，推理时限制生成到合法选项标签；行为扰动采用固定随机种子构造错配 pair；注意力敲除验证 k∈{1,3,5,9,13} 趋势一致；精度差值统计基于 10,000 次配对 bootstrap 给出 95% 置信区间。

### 📊 实验结果
**数据集**：ADQA-Bench、MMAR、MMAU-test-mini、MMSU；训练 AudioMCQ-StrongAC-GeminiCoT

**主要指标**：
- Qwen2-Audio ADQA：ZS 36.9%→FT 51.1%，ΔSaudio +9.3；MMAR 41.2%→52.5%，ΔSaudio +6.9
- Qwen2.5-Omni ADQA：41.9%→54.4%，ΔSaudio +4.5；MMAR 53.7%→65.7%
- 两模型在 MMAU 上均负迁移（ΔA −1.1 与 −13.5），作为对照
- 注意力敲除：Audio→Options 在早-中层（Qwen2-Audio 8–12 层、Qwen2.5-Omni 10–16 层）影响最强；Options→Answer 训练后后期层显著降低正确概率
- LoRA 层带：仅训练 8–15 层 Qwen2-Audio 的 ADQA 51.13%、MMAR 52.81%、MMSU 59.72%，逼近全层 r=16（均值 54.82 对 55.26）

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：首次以统一框架刻画训练如何改变音频 LLM 中"声学信息整合"与"最终答案选择"两个阶段，将行为敏感度、注意力敲除与 LoRA 层带归因三类证据互相印证，尤其 LoRA 单带训练达到 92% 以上全层性能的结果对高效适配有实际启示。扣分：训练细节（优化器、学习率）缺失，机制结论主要基于两个 Qwen 系列模型。

---

**其他收录（简列）**：

- [Enhancing Neural Speech Coding with Semantic and Visual Cues](https://arxiv.org/abs/2609.05076) | arXiv:2609.05076 | **方向**：语音大模型 | ⭐ 7/10
- [Auditing Bias and Safety in Voice AI Customer Care](https://arxiv.org/abs/2609.04206) | arXiv:2609.04206 | **方向**：语音大模型 | ⭐ 7/10
- [GEPARD - Generative, Prosody-aware, Autoregressive text-to-speech model for Realtime Dialogue](https://arxiv.org/abs/2609.04222) | arXiv:2609.04222 | **方向**：语音大模型 | ⭐ 7/10
- [Automatic Speech Recognition for Multilingual Oral History Research](https://arxiv.org/abs/2609.04232) | arXiv:2609.04232 | **方向**：语音大模型 | ⭐ 6/10

---

## 语音前端

## [1] Grounded Decoding for Autoregressive Speech Enhancement via Adaptive Code-Space Grounding and Local LLM Refinement

**arXiv ID**：2609.04245 | **方向**：语音前端

**作者**：Hao Shi, Yuan Gao, Zhaoheng Ni, Junyi Peng, Gongping Huang, Yu Tsao, Xugang Lu

**机构**：京都大学、Meta、布尔诺理工大学、武汉大学、台湾中研院、日本 NICT

**发布日期**：2026-08-21 | **论文**：https://arxiv.org/abs/2609.04245 | **PDF**：https://arxiv.org/pdf/2609.04245.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
LLM 自回归语音增强（SE）能借助干净语音先验生成自然语音，但易产生输入不支持的内容幻觉；确定性增强更忠实保留观测证据，却常残留噪声或局部失真。本文提出证据锚定的生成式 SE 框架：以 Whisper 引导的 DPRNN 确定性增强器输出作为观测耦合证据，与带噪观测混合后经 FSQ 分词得到离散证据序列用于条件生成，并设计 Code-Space Grounding（CSG）按 FSQ 空间中的汉明距离惩罚解码候选；提出 SNR-CSG 将锚定强度随声学难度自适应；再以 GNR-LLM 在锚点局部 FSQ 邻域内做一次教师强迫的 LLM 排序细化。在后测试集上，GNR-LLM（K=50,R=3）将 WER 从 UD 的 9.3% 降至 8.5%，全程无新增可训练参数。

### 🔧 技术方案

**问题背景：** 确定性 SE 在 DNN 输出层保留语言内容但残留噪声与局部失真；LLM 类生成式 SE 利用长程上下文恢复重度退化区域，但强先验可能覆盖模糊声学证据造成幻觉。已有低幻觉生成式 SE 主要改进送入生成器的信息，并不显式约束解码过程本身。本文核心出发点是把确定性输出当作不完美但观测耦合的证据而非最终结果或伪干净目标。

**模型架构：** 前端为 Whisper 引导的 DPRNN 确定性增强器：Conv1D 编码器（64 通道，核 16，步长 8），6 个 DPRNN 块（双向 LSTM 隐层 128），每块以 1×1 卷积门控残差注入冻结 Whisper-large-v3 特征，损失为负 SI-SDR；增强波形以 ρ=0.6 与带噪观测混合，经 CosyVoice 3 分词器（25Hz，3^8 个 FSQ token）得到离散证据序列。生成器采用 Qwen2.5-0.5B-Instruct：Whisper 特征按 5 帧堆叠经两层投影(6400→2048→896)映射进 LLM 嵌入空间，与证据 token 拼接为条件序列；全参数微调，词表扩至 158,625 项。

**核心创新：** (1) Code-Space Grounding（CSG）：定义证据距离 Δ 为候选与相邻证据 token 的最小 FSQ 分量汉明距离，解码得分改写为 log p_t(v)−λΔ，连续惩罚观测不支持的大幅偏离。(2) SNR-CSG 自适应锚定：以残差 SNR 为代理，经 Theil–Sen 校准后映射为 9 档冻结强度 Λ=(2.0,…,0)，SNR 越低锚定越强。(3) GNR-LLM 局部细化：在完整锚序列上做一次教师强迫前向，将 Top-K 候选与锚点周围汉明球取交集选最高概率 token，仅增加约 2.5% 解码开销。

**训练策略：** 由 LibriSpeech 960h 语音与 DNS 2020 噪声以 SNR 在 [−5,20]dB 均匀采样混成 281,224 对训练对；自回归交叉熵目标，最多训练 3 轮加早停；训练用 4s 片段、batch size 4；分词器、CosyVoice 3 流匹配与声码器全程冻结。

### 📊 实验结果
**数据集**：LibriSpeech dev-clean/test-clean 合成域内集；control-SNR 配对集；DNS Challenge no_reverb 跨语料测试集

**主要指标**：
- 测试集 WER：UD 9.3% → CSG 8.5% → SNR-CSG 8.5% → GNR-LLM(50,3) 8.5%
- 确定性基线 E2-WhspDPRNN：WER 6.5%、STOI 0.937、PESQ 2.522、SI-SDR 17.30 dB
- 受控 SNR：−5dB 时 GNR-LLM WER 23.9%、UTMOS 从 2.993 回升至 3.299
- DNS no-reverb：SNR-CSG 8.4% WER 优于 CSG（8.6%）与 UD（9.2%）
- 尾部鲁棒性：WER>0.5 句子比例由 UD 3.3% 降至 GNR-LLM 2.5%

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：将确定性输出重新定位为"观测耦合证据"，并依据 FSQ 因子化空间的局域几何设计解码期惩罚项，角度新颖且全程零附加参数，工程友好。实验设计全面（域内、受控 SNR、跨语料 DNS、尾部鲁棒性），并细致分析自适应锚定机制。扣分：生成式基线规模较小（0.5B 级）、幻觉问题未在真实录音场景验证，GNR-LLM 在最恶劣子集上劣于固定 CSG。

---

## [2] Discriminative Flow Matching: Beyond Time-Conditioning in Generative Restoration via Flow-State Representations

**arXiv ID**：2609.04525 | **方向**：语音前端

**作者**：Shrishti Saha Shetu, Emanuël A. P. Habets, Andreas Brendel

**机构**：International Audio Laboratories Erlangen（FAU 与 Fraunhofer IIS 联合机构）

**发布日期**：2026-09-03 | **论文**：https://arxiv.org/abs/2609.04525 | **PDF**：https://arxiv.org/pdf/2609.04525.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
条件流匹配（CFM）以显式时间坐标 t 同时驱动插值路径与速度网络的条件化，但恢复任务中源与目标分布统计相关（目标信号内嵌于含噪输入），同一 t 可能对应不同的退化程度与传输进度，时间条件存在固有歧义。本文提出判别式流状态假设并据此提出判别式流匹配（DFM）：用冻结判别式增强模型编码器提取的判别式流状态表征（DFSR）替代显式时间 t 条件化速度网络，并实现样本自适应推理。在 Interspeech 2020 DNS Challenge 上，DFM 取得 19.63 dB SI-SDR 与 2.96 PESQ，一致超越 FlowSE（18.99/2.86）、ARF（19.04/2.82）、CFM+DL（19.47/2.87）等基线；自适应推理在平均 NFE 降至 2.98（计算减 40.4%）时 SI-SDR 反升至 20.12 dB。

### 🔧 技术方案

**问题背景：** CFM 的目标向量场随时间变化，故需用 t 条件化速度网络。标准 OT-CFM 中源与目标统计独立，流状态 S(p_t)=W_2(p_t,p_1) 满足线性关系，t 是传输进度的可靠代理。但恢复任务初值 x_0=αx_1+βν，命题 2 证明存在不同的 (α,β,t) 组合产生相同边际分布，即同一状态可在不同 t 达成，全局插值坐标无法无歧义描述传输进度；近期工作（如 ARF）直接移除时间条件化，又丢失按进度自适应调节速度的机制。

**模型架构：** DFM 沿用 FlowSE 训练框架与 NCSN++ 主干（约 63.2M 参数）。判别式概率路径 x_ζ=(1-ζ)x_0+ζx_1+σ_ζ ε。DSFR z=ε_φ(x_ζ) 由冻结判别式恢复模型（默认 DCCRN）编码器提取，经线性层投影至 256 维，FIR 滤波下采样后以加法条件注入每个残差块，总模型 65.8M 参数。推理采用欧拉法，每步按当前估计实时更新 z，速度网络完全由 DFSR 驱动。

**核心创新：** (1) 理论上定义流状态描述传输进度，严格证明时间坐标歧义（命题 2）、流状态上界（命题 3）、流状态近似误差受判别模型训练损失约束（命题 4）和互信息保持性（命题 5），为判别式条件化提供系统理论支撑。(2) 提出判别式流状态假设与 DFM 框架，t-SNE 显示 DFSR 能高精度预测中间态 SNR（Pearson 0.968），潜空间与信号域轨迹严格单调（Spearman ρ=−1.000）。(3) 基于流状态的样本级自适应推理：预测器联合输出所需 NFE 与非均匀积分步长，NFE=2.98 时 SI-SDR 达 20.12 dB。

**训练策略：** DNS Challenge 约 1000 小时训练集（SNR −10~30 dB，50% 混响），Adam、lr=1e-4、batch 8、EMA 0.999，高斯噪声系数 σ=0.487，单块 A100 训练 80 万步，5 次独立运行取均值；损失为速度匹配。另验证数据预测目标、不同判别主干（DCCRN/ULCNet/TaylorSENet/GCRN）与图像去噪（MNIST/Fashion-MNIST）。

### 📊 实验结果
**数据集**：Interspeech 2020 DNS Challenge（合成非混响 150 条、DNS Real 300 条、混响测试集）；MNIST、Fashion-MNIST

**主要指标**：
- SI-SDR：DFM 19.63 dB，优于 FlowSE 18.99、ARF 19.04、CFM+DL 19.47、BBED 19.10、SGMSE+ 16.86
- PESQ：DFM 2.96，优于 FlowSE 2.86、ARF 2.82、CFM+DL 2.87
- 真实录音 P.808 MOS：3.75（SIG 3.43、BAK 4.03、OVRL 3.14），超 SGMSE+ 3.64
- 自适应推理：平均 2.98 NFE、SI-SDR 20.12 dB，计算量减 40.4%
- 去混响：DFM −27.19 dB/2.44，优于 CFM −27.64/2.35；SI-SDR 对所有基线 p<0.001

**是否开源**：暂无（依赖 FlowSE、SNR-Aligned DiffSE、DCCRN 等第三方实现）

### ⭐ 评分：8/10
评分理由：首次以严格的命题体系论证恢复任务中时间条件的歧义性及判别式表征作为传输状态描述的合理性，理论推导完整且与实证互相印证，是该方向少有的深度工作。DNS 合成与真实场景下相对三类 CFM 变体均取得一致且统计显著的增益，自适应推理具备工程价值。扣分：代码未开源，去混响增益微弱，对判别模型性能依赖性缺乏敏感性分析。

---

**其他收录（简列）**：

- [What Selects, What Reconstructs: Repairing Exemplar-Based Complex-Spectrum Separation](https://arxiv.org/abs/2609.04756) | arXiv:2609.04756 | **方向**：语音前端 | ⭐ 8/10

---

*Generated on 2026-09-08*
