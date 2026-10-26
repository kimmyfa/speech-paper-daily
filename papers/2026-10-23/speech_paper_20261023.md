# 2026-10-23 语音论文速递

**共收录**: 13 篇 | **语音大模型**: 10 篇 | **语音前端**: 3 篇

> 目标日期 2026-10-23（北京时间）arXiv 语音相关论文共命中 13 篇。
> 以下是按评分排序的结果。

---

## [1] HeyGen Voice: Scene-Aware Voice Cloning for Talking Videos

**arXiv ID**：2610.30470 | **方向**：语音大模型

**作者**：Pavel Andreev, Andrei Gusev, Adithya Narayan, Yi Ren 等18人

**机构**：HeyGen Research

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.30470 | **PDF**：https://arxiv.org/pdf/2610.30470.pdf | **代码**：暂无 | **Demo**：https://heygen.com/heygen-voice

### 📌 简介
现有声音克隆把参考录音的话筒、房间与说话方式当作音色本身，生成语音与画面场景脱节。本文提出面向talking video的场景感知克隆模型HeyGen Voice：参考录音只保留音色/口音/节奏，目标图像加caption决定"怎么说、在哪说"。模型为多模态自回归transformer+flow-matching解码器，输出44.1kHz，经五阶段课程训练。其控制声音榜 Elo 1201 排第一，用户盲测对 ElevenLabs v4、Cartesia 获62.2%/54.1%偏好，自评数字人视频高10-30分。

### 🔧 技术方案

**问题背景：** 常规TTS数据中参考与目标同条录音，参考已解释全部声学信息，模型无动机看图像，而真实同人异景配对稀缺；已有方法只做对一半：描述引导TTS无图像，人脸/图像条件合成留不住特定说话人，音视频联合生成无法指定声音；图像+caption还欠定声学，长文本分块会漂移音色与房间。

**模型架构：** 单序列因果多模态自回归transformer：条件前缀以冻结编码器+注意力池化把各模态压成少量固定token：视觉-语言编码器嵌目标图像；文本分别嵌speaker caption（delivery）与background caption（环境/混响/演变）；音频编码器抽参考音色/口音/节奏token；另加锚点一致性嵌入、局部声学滑窗与音高动态/SNR/背景均匀度等标量控制。脚本后自回归预测mel-VQ离散声学码（交叉熵）；重放序列取隐状态条件化DiT流匹配模型、以参考音频为条件解码44.1kHz，解码器无图像输入。

**核心创新：** (1) 跨场景条件化配两种克隆策略：voice-clone以声纹设计输出为锚、为画面场景重新设计delivery与声学；full-clone以处理后参考为锚、延续原录音话筒与房间、保真最高，保真-场景折衷由用户切换。(2) 消除捷径的五阶段课程：TTS预训练→对参考做通道/时序扰动的模拟跨场景适配（身份只用人声、场景用整条录音）→真实跨源同人异景对SFT→以说话人相似度+CER/WER易懂性为奖励的GRPO→低秩表现力adapter两阶段DPO（judge→人类偏好）。(3) 长文本一致性：跨chunk复用锚点一致性嵌入固定音色与场景，滑窗上下文保证衔接；adapter以W+αBA修改投影、α可调且不破坏基座。

**训练策略：** HELIOS调度5000+跨云GPU、数据引擎20万+并发任务；八阶段音频管线：人声分离、语种/diarization/ASR词级对齐、质量过滤、说话人聚类、双流caption、跨场景对挖掘、审计、视频/近重复/说话人三层划分train-test；teacher-forcing交叉熵+条件dropout，扰动贯穿SFT、GRPO不加扰动；CFG+DMD蒸馏后RTF约0.1，参数量/超参未披露。

### 📊 实验结果
**数据集**：331例英文同人异景基准（TalkVid+CelebV-HQ，155簇）；修正后MiniMax十语言集（每语言100×2人）；Podonos 245例5语种42,875评分；43人视频自评+50场景。

**主要指标**：
- ImageBind：voice-clone音频-音频0.637、音频-图像0.282全场最高
- ECAPA相似度：voice-clone对目标0.590（Cartesia 0.582/ElevenLabs 0.556），full-clone对参考0.757（Cartesia 0.745）
- 十语言agreement-only CER宏平均0.015%（ElevenLabs 0.013%同带、Cartesia 0.079%）
- 聆听narrator choice胜率61.5%/77.9%/68.1%对ElevenLabs/Cartesia/Inworld，清晰度78.4%/86.6%/63.5%
- 生产盲投62.2%（8332票）与54.1%（7286票）、三方41.7%对chance 33.3%；arena Elo 1201第一
- 视频自评76.1 vs ElevenLabs 59.2/Seedance 45.7（配对差+9.5~+30.3）；50场景背景声贴合69.7%

**是否开源**：模型与代码未开源，正文无GitHub链接；Demo https://heygen.com/heygen-voice 。

### ⭐ 评分：8/10
评分理由：把"谁在说"与"怎么/在哪说"解耦为双克隆策略，任务定义新且直击talking video痛点；参考扰动消除捷径的课程及GRPO+两段DPO合理，评测从自建基准、五语种聆听、生产投票到第三方arena与视频研究层层递进、统计校正严谨。不足是闭源、超参未披露、基准caption由真实目标录音导出而非纯图像推断，复现受限。

---

## [2] Spark-Audio 1.0 Technical Report

**arXiv ID**：2610.31292 | **方向**：语音大模型

**作者**：iFlytek Spark Audio Team（通讯作者 Shifu Xiong）

**机构**：科大讯飞（iFlytek）

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.31292 | **PDF**：https://arxiv.org/pdf/2610.31292.pdf | **代码**：暂无 | **Demo**：https://iflytekresearch.iflytek.com/experience/spark-audio

### 📌 简介
传统ASR只优化逐字转写，丢弃了情感、性别年龄、韵律与环境声等副语言信息，且语音基础模型长期依赖受限的海外算力栈。科大讯飞发布Spark-Audio 1.0：由0.65B稠密音频编码器与30B-A3B MoE LLM耦合的语音基础模型，基于1300万小时音频与大规模文本训练，支持99语言/202方言语音识别、语音翻译、音频感知理解及语音/文本对话，全程在华为昇腾910B与海光BW1000国产芯片上训练。仅用约Qwen3.5-Omni-Flash十分之一的数据，即在其上取得FLEURS中文CER 1.88%对2.90%、VoiceBench 90.35对87.80的优势，但指令遵循与复杂音频推理仍有差距。

### 🔧 技术方案

**问题背景：** 现有ASR面向单一转写目标，难以统一声学感知与语言推理；同时竞争性语音基础模型被认为需要不断堆叠数据与参数，且训练依赖海外软硬件生态，国产算力上端到端训练可行、少量数据能否支撑实用场景均属未验证问题。

**模型架构：** 音频编码器采用Whisper large-v3编码器架构（0.65B稠密参数），流式/非流式共享同一套参数；输出表征经MLP+CNN时间下采样适配器映射进30B-A3B MoE语言主干。ASR、翻译、理解、对话统一为条件文本生成，prompt指定语言、方言与输出格式。

**核心创新：** (1) 表征增强BEST-RQ：将随机投影量化器的输入由低层声学特征换成约150万小时多语ASR监督训练的冻结教师末层归一化上下文表征，构造语义感知离散目标，不引入可训练tokenizer或表征匹配网络即注入多语语义先验，使预测目标更紧凑、任务更具区分度并加速收敛。(2) 分级课程与双轨迹on-policy蒸馏：编码器经BEST-RQ→130万小时监督ASR→性别/年龄/情感/声事件等五任务文本目标三阶段；音频LLM经适配器对齐→全参数联合→32K长上下文扩展；后训练由冻结纯文本教师对学生音频/文本双轨迹rollout按转写评估，在教师top-k支撑集上计算局部反向KL并等权联合，抑制认知退化。(3) 国产全链路训练与长上下文工程：昇腾910B/海光BW1000覆盖编码器预训练至后训练；Stage III用EP8专家并行+CP4上下文并行+ZeRO-2，超长音频分块独立编码后按时间序在embedding级拼接。

**训练策略：** 预训练三阶段可训练范围为适配器→全参→全参，全局批大小67M/66M/152M token、最大序列4K/4K/32K；统一BF16+AdamW，weight decay 0.01、梯度裁剪1、label smoothing 0.05，损失按有效目标token数归一。SFT用ChatML高质量多任务数据训1 epoch、余弦衰减；OPD用数万条语音-文本配对输入训3 epoch（采用第2 epoch检查点），采样含nucleus与重复惩罚设置。

### 📊 实验结果
**数据集**：FLEURS（99语言）、AISHELL6-Whisper、WenetSpeech、SpeechIO、KeSpeech、LibriSpeech、speechocean762、TED、AIR-Bench、MMSU、MMAR、VoiceBench、MMLU-Pro/CMMLU/C-Eval/IFEval/IFBench/MATH-500/GSM8K/HumanEval，及内部202方言库与高噪/低音量语音测试集

**主要指标**：
- FLEURS-zh CER 1.88%、FLEURS-en WER 2.25%，较最优对照错误率相对降低35.2%/16.7%（Flash为2.90/3.70）
- FLEURS 14/20/64语言平均WER/CER 2.81/6.30/31.89%，前两组最优，64语组逊于Gemini 3.1 Pro的20.09%
- 内部202方言CER 14.29%，较最优基线19.79相对降27.8%；低音量中文CER 17.17对23.62，高噪37.76对38.66
- S2TT：内部中→英44.76 BLEU、英→中51.40，超最优基线7.41/7.97分；FLEURS 28.40/44.54低于Omni-Plus
- VoiceBench 90.35（Flash 87.80），MMSU 73.96%；MMAR 57.90%落后全部对比系统
- GSM8K 97.35、HumanEval 92.07高于Flash，IFEval 82.19低于85.20
- 编码器对照：同配Qwen3-4B下FLEURS 37语言宏平均错误率26.24%，较Whisper large-v3（45.65%）降19.41、较AuT两阶段（38.46%）降12.22个百分点

**是否开源**：暂无（论文未提供代码或权重仓库链接，仅提供在线体验Demo）

### ⭐ 评分：8/10
评分理由：语义感知BEST-RQ目标与双轨迹OPD具备实质方法创新，编码器消融与统一底座对照实验支撑充分；仅十分之一数据即达SOTA级识别与对话表现，并首次在国产算力完成端到端训练，工程与产业价值突出。扣分在于复杂音频推理（MMAR）、长尾小语种与指令遵循明显落后更大模型，且未开源限制复现。

---

## [3] EmoFI-TTS: Face-Conditioned Expressive Voice Synthesis with Intensity Modulation

**arXiv ID**：2610.30477 | **方向**：语音大模型

**作者**：Yejin Jeon, Luel Hagos Beyene, Marie Maltais, Hyounghun Kim, David Ifeoluwa Adelani

**机构**：Mila–Québec AI Institute、McGill University、NM-AIST（名古屋工业学院）、AIMS Research and Innovation Center、POSTECH、Canada CIFAR AI Chair

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.30477 | **PDF**：https://arxiv.org/pdf/2610.30477.pdf | **代码**：https://github.com/luelhagos/Emofi | **Demo**：暂无

### 📌 简介
表达性TTS在精细的强度控制上仍很困难。本文提出EmoFI-TTS面部条件跨模态框架：单张人脸决定情绪类别与强度，参考音频决定音色，文本控制内容；模态表征融合后条件化预训练TTS主干，并用强度细化模块修正mel频谱，强度嵌入插值可实现连续控制。在speaker-disjoint MEAD上客观/主观强度准确率均值达64.4%/75.2%，高于用真值标签的EmoSpeech（39.1%），且WER仅6.9%、自然性好（UTMOS 3.14）。

### 🔧 技术方案

**问题背景：** 现有表达性TTS依赖手工情绪标签或目标情绪参考音频，交互式场景难以满足；此前face-to-speech研究多把人脸当作音色代理，普遍不建模细粒度情绪强度，同属happy的轻度与狂喜被映射到同样声学实现，表现力与视觉线索失配。

**模型架构：** 主干为LibriTTS预训练的多说话人FastSpeech2；人脸分支用ImageNet预训练ResNet-50把单帧脸编成768维情感嵌入（与emotion2vec音频情绪表征对齐并挂情绪/强度辅助分类头后冻结），音频分支用ECAPA-TDNN+LEACE概念消除提取192维音色嵌入；两分支拼接投影为128维风格向量，经仿射调制条件化音素编码器与mel解码器。

**核心创新：** (1) 首个显式建模面部情绪强度的face-conditioned情感TTS：推理时类别与3档强度均由人脸预测，无需情绪标注，单条参考即可把情感迁移到未见说话人。(2) 跨说话人配对训练解离情感与音色：超一半训练样本换成仅情绪/强度标签一致的他人人脸，切断借人脸身份重建音色的捷径。(3) 强度门控细化模块R：膨胀卷积栈预测零初始化残差修正mel，档1（平静）整体跳过以免过度增能，监督含多尺度LSGAN、谱方差匹配、内容ℓ1锚与冻结wav2vec2特征匹配；强度嵌入线性插值支持t∈[1,3]连续控制且无需额外训练。

**训练策略：** 风格分支在MEAD上训练30k步（batch size 16）后冻结，R单独训练15k步；损失为主干mel/音高/能量/时长/对抗项加0.1倍情绪与强度交叉熵；全部在单卡NVIDIA GH200完成。

### 📊 实验结果
**数据集**：MEAD平行视听语料，剔除disgust/contempt及2名强度覆盖失衡说话人后共18,270条，22.05kHz音频+单帧人脸，Whisper-large转录校正（141句canonical），按说话人不相交约8:1:1划分

**主要指标**：
- 客观强度准确率：64.4%（L1 76.4/L2 42.8/L3 74.1），主观75.2%（82.2/69.5/73.9）
- 可懂度与自然度：WER 6.9%、UTMOS 3.14、MOS 3.25±0.26（95% CI）、说话人忠实度4.13
- 关键对比：较真值条件EmoSpeech客观强度+25.3pp（39.1%）、WER低2.4pp、UTMOS高0.26；FaceTTS改造后WER 16.3%/UTMOS 2.46；oracle强度67.2%仅差2.8pp；消融去R降7.7pp（56.7%），跨说话人配对使L3升8.2pp（65.9%→74.1%）

**是否开源**：代码已开源 @ https://github.com/luelhagos/Emofi

### ⭐ 评分：7/10
评分理由：首次把面部情绪强度显式引入face-conditioned TTS，问题定位新颖，跨说话人解耦与门控残差细化设计干净并有完整消融支撑；仅用单张人脸即逼近oracle标签条件。不足在于只在MEAD单语料验证，基线为相邻任务改造而缺少更强的面部情绪竞争方法，中性档生成仍有过增强风险，整体属扎实的增量贡献。

---

## [4] HC-AINet: An Auditory-Inspired Network with Harmonic Compensation for Low-Complexity Speech Enhancement

**arXiv ID**：2610.30818 | **方向**：语音前端

**作者**：Nan Li, Xiaoxiong Wu, Huawei Liu, Ziping Zhao

**机构**：天津师范大学计算机与信息工程学院，中国

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.30818 | **PDF**：https://arxiv.org/pdf/2610.30818.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对低算力听觉子带方法增益过于平滑、难以区分谐波峰与带间噪声的问题，提出HC-AINet：三角ERB滤波器组将特征压缩至32/64带，轻量网络预测全局增益、谐波增益与融合权重；由带噪谱导出的谐波位置图把谐波贡献限制在原始频率栅格的选定频点上补偿，再以最小相位线索条件化紧凑相位估计器重建波形。64带模型仅约0.27M参数、1.08 G MAC/s，在VoiceBank-DEMAND取得PESQ 3.20、STOI 0.95，真实录音DNSMOS 3.81。

### 🔧 技术方案

**问题背景：** 资源受限设备上增强质量与模型规模难兼顾；RNNoise/PercepNet等听觉子带方法以非均匀分辨率省算力，但增益频率分辨率随之受限——一个ERB带内谐波与带间噪声共存，共享增益无法独立调节窄带结构，oracle 32带ERB增益重建仍留残差，且直接复用带噪相位使相位误差无从解决。

**模型架构：** STFT为512点FFT / 512窗 / 200跳（16 kHz下32/12.5 ms），三角ERB组把线性频bin压缩至32/64带送入增益网络AINet：编码器由逐点+深度可分离倒残差单元（32通道×4，跨步下采样降频维）构成；4个TFP模块串联时序Conformer（带掩码防未来帧）与PFG模块（3路并行深度卷积、频域平均池化softmax加权，模块间串行、分支并行）；转置卷积解码后输出4头（全局/谐波增益与两个融合权重，各独立可学习sigmoid，不约束和为1）；增益广播扩展回原始栅格融合后，连同带噪相位与最小相位线索输入紧凑卷积网络回归二维坐标合成相位，ISTFT重建。总参数0.27M。

**核心创新：** (1) 把增益预测分辨率与增益施加选择性解耦：学习只在紧凑ERB域进行，但预测增益在保留的原始线性频谱上逐bin扩展应用，噪声高分辨率幅度作为补偿载体，区别于在ERB域之后直接重建的方法。(2) 位置条件化谐波分支：带噪对数幅度投影到固定谐波积分模板、取最优候选做时间聚合并经查表生成二值位置图，无需pYIN或嗓音门控；谐波增益仅作用命中频点，与全局包络分支加权和成等效增益，实现带内选择性，属现有能量再分配而非生成缺失谐波。(3) 幅度条件化相位重建：对补偿对数幅度做谱分解（实倒谱+最小相位提升器）得到确定性最小相位线索，与带噪相位一起引导紧凑网络预测相位坐标，配合复谱、波形与IP/GD/IAF损失联合监督。

**训练策略：** 多任务联合损失：全局/谐波/补偿幅度MSE类损失、复谱与波形损失、包装相位距离与IP/GD/IAF一致性损失，再加MetricGAN式判别器目标（仅训练期使用）；谐波监督使用与前向相同的带噪位置图，避免硬选择反传；11,572对16 kHz训练语音随机裁剪至32,000点、batch 2、幂律压缩、AdamW、学习率逐epoch×0.99、PyTorch单seed 1234。

### 📊 实验结果
**数据集**：VoiceBank-DEMAND（训练28人、测试824条，未见说话人噪声、SNR 2.5–17.5 dB）；DNS Challenge带参考集与2020真实录音测试集。

**主要指标**：
- VoiceBank-DEMAND（64带）：PESQ 3.20、CSIG 4.27、CBAK 3.65、COVL 3.74、STOI 0.95，0.27M参数
- 对比自家HC-APNet-64 PESQ 2.86→3.20（+0.34，参数0.22→0.27M）；PESQ为表中最高，高于GTCRN 2.84（0.05M）、CMGAN-mag 3.04（0.40M）、DeepFilterNet 2.81（1.78M）
- 消融：去掉谐波补偿PESQ均值2.80→2.69，复用带噪相位2.76；32→64带MAC/s 0.66→1.08
- DNS参考集（64带）：WB-PESQ 3.22、NB-PESQ 3.72、STOI 97.21%、SI-SDR 18.88 dB；仅为HGCN+（5.29M）5%参数，WB/NB-PESQ +0.03/+0.07
- 真实录音DNSMOS 3.81，比PercepNet 3.51高0.30

**是否开源**：暂无（正文未给出GitHub/HuggingFace/Demo链接）。

### ⭐ 评分：7/10
评分理由：以噪声域谐波位置图在原始栅格做带内选择性补偿，切中听觉子带方法的代表性短板；表征—骨干—补偿—重建四条消融链完整，0.27M参数达PESQ 3.20的性价比突出并经DNS/真实录音互补验证。不足是相对作者前作HC-APNet属增量改进，单seed、无听测与延迟实测，流式实现仅设计未验证，鲁棒性证据偏弱。

---

## [5] When Do Self-Supervised Representations Help Speech Restoration?

**arXiv ID**：2610.30869 | **方向**：语音前端

**作者**：Yongjoon Lee, Younghoo Kwon, Jung-Woo Choi

**机构**：韩国科学技术院（KAIST）电气工程学院、AI系统系（大田，韩国）

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.30869 | **PDF**：https://arxiv.org/pdf/2610.30869.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文追问"SSL特征清洗是否总利于语音恢复"，通过t-SNE与Spearman相关分析发现感知相关性坍缩现象：轻度退化为SSL特征距离与感知质量强相关，一旦超过临界退化严重度，相关性崩溃，最小化SSL损失不再带来质量提升。据此提出Early Restoration Injection（ERI），将恢复主干中间层的部分恢复特征经轻量条件网络注入SSL，缓解坍缩。在VoiceFixer测试集上ERI取得PESQ 2.82、ESTOI 0.71、LPS 0.92三项最优，UTMOS 3.86次优，RTF仅0.020。

### 🔧 技术方案

**问题背景：** 主流SSL特征清洗方法默认"clean-degraded的SSL特征距离越小、恢复质量越好"，该假设从未被检验；在强噪声、窄带、削波、丢包等严重退化下，清洗目标与感知恢复目标实际失配，SSL损失梯度失效。

**模型架构：** 恢复主干为SEMamba++（编码器+4层时频瓶颈+解码器，输出幅度相位谱），SSL为WavLM（卷积特征提取器+24层Transformer）。从SEMamba++第2层取瓶颈潜特征(T,F,D)，reshape后线性映射到WavLM通道维C，经LayerNorm+LeakyReLU与自适应平均池化对齐时间维，与特征提取器输出拼接为(T',2C)再投影回C完成条件注入；WavLM以LoRA(r=16,α=32)微调清洗特征，第24层清洗结果经AdaLN融合模块注回主干第3层，注入与融合前均设stop-gradient；总参数340M、可训练24.5M。

**核心创新：** (1) 首次系统揭示感知相关性坍缩：在WavLM/HuBERT/SPEAR/Wav2Vec2四个large SSL与VQScore/SCOREQ/DNSMOS代理及免模型LSD上，以m=100、1000次bootstrap计算SSL余弦距离与感知分的Spearman相关，显示相关性在Extreme级严重度崩溃，排除单一指标与采样噪声假象。(2) 提出ERI：直接复用主干中间特征作为SSL的"已恢复证据"，取得相当于前置预恢复模型的效果却无需额外模型开销。(3) 极简融合归因：默认拼接注入(24M)对比AdaLN注入(32M)无显著增益，证明收益来自注入特征本身而非容量增大。

**训练策略：** 损失为SEMamba++的LSGAN生成器损失加上第24层特征L2归一化MSE的SSL清洗损失（L_total=L_G+L_SSL），端到端联合优化。数据为VCTK-0.92（剔除p280/p315）与LibriTTS-R train-clean-100/360共约300小时语音，16kHz；噪声取WHAM!与DNS Challenge，RIR取Arni与DNS；按概率随机叠加噪声（SNR -5~20dB）、带限（截止2-7kHz）、削波、混响。段长48000样本（3s），STFT窗400/跳160；AdamW（β1=0.8,β2=0.99），学习率1e-4、指数衰减γ=0.99，batch 8；两阶段训练：先训SEMamba++，再加300k步训完整ERI。

### 📊 实验结果
**数据集**：VoiceFixer官方测试集（覆盖噪声、混响、带限、削波，16kHz）；内部消融用自建模拟退化测试集。

**主要指标**：
- PESQ：2.82（全场最优，较SEMamba++的2.76提升0.06，较最强回归基线TF-GridNet的2.47提升0.35）
- ESTOI：0.71（最优，vs 0.68）；LPS：0.92（最优）
- OVRL：3.10；UTMOS：3.86（仅次于SIDON的3.97）；RTF从0.015升至0.020（单卡RTX 4090）
- 匹配参数量消融：有/无ERI的SCOREQ 3.97/3.93、PESQ 2.50/2.42；换HuBERT同样有效（PESQ 2.41/2.33），Stage1仅300k步欠收敛时仍增益

**是否开源**：暂无（正文与致谢未提供代码/Demo链接）

### ⭐ 评分：7/10
评分理由：以"质疑假设—分析现象—给出解法"的完整闭环切入SSL语音恢复领域，感知相关性坍缩的验证跨4种SSL、4种质量代理并含bootstrap与LSD交叉检验，扎实可信；ERI实现极简，消融将增益归因于注入特征本身而非容量，方法学规范。不足是绝对提升幅度偏小、VoiceFixer基准缺主观听测、未开源限制复现与落地，整体属顶会水准的增量但有启发性工作。

---

## [6] Text-Only LLM Correctors Break Correct Transcripts: A Repair-Damage Analysis of Audio Grounding in ASR Error Correction

**arXiv ID**：2610.30385 | **方向**：语音大模型

**作者**：Vasiliy Kudryavtsev, Kirill Borodin, Nikita Vasiliev, Mikhail Gorodnichev, Grach Mkrtchian

**机构**：BitmanagerAI（迪拜）| MTUCI（莫斯科）| lab260（埃里温）

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.30385 | **PDF**：https://arxiv.org/pdf/2610.30385.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
LLM 对 ASR 结果的纠错长期以聚合 WER 评判，掩盖了它修复哪些词、破坏哪些本已正确的转录。本文把 WER 变化在词级精确分解为修复、损坏与插入三个分量，在"自我修正（音频 LLM 的草稿）/跨系统（独立 ASR 输出）"与"带音频接地/纯文本"上设计五格对照，以 Gemini 2.5 Flash 在俄英三个语料评测。纯文本自我修正破坏 13–32% 本已正确的输入，带音频仅 1–3%；接地在两种设定下均降低损坏而修复符号相反；医疗语料上插入分量抵消净收益；开源权重 Voxtral 不复现该文模式。

### 🔧 技术方案

**问题背景：** 零样本单假设 LLM 纠错大多抬高 WER，ClozeGER 等证明给正确器音频有益，但聚合错误率把"修好词"与"改坏词"两股反向力量混在一起，缺少词级记账来回答音频改变了正确器的什么行为。

**模型架构：** 不提出新模型，而是诊断框架 ŷ=g(a,h)，音频与假设均可扣留。五格单元：B（仅音频无假设，对照）、C/A（以模型自身草稿为输入的纯文本/带音频格，自我修正档）、T/F（以独立 ASR 输出为输入的同两格，跨系统档），每格只对供给其输入的系统计分。俄语识别器 GigaAM、英语 Whisper large-v3-turbo；主正确器 Gemini 2.5 Flash。参考与输入/输出分别对齐标记词对错，导出恒等式 ΔWER=rep/W−dam/W+(ιh−ιŷ)/W，按句与聚合均成立；另定义 break-rate（零错输入被改坏占比）与 fix-rate。

**核心创新：** (1) 词级修复/损坏/插入分解是记账恒等式而非模型，对任一固定对齐精确成立；采用 deletion-first 回溯，换 insertion-first 各率变动不超过 0.02pt，远小于论文最小效应。(2) 2×2+1 因子配对对照以"带音频−纯文本"差界定音频作用，并诚实分析 prompt 混杂：纯文本 prompt 更严格，故损坏结论偏保守、跨系统修复增益仅是音频贡献的上界。(3) 用 break-rate 揭示聚合 WER 掩盖的静默破坏，提出并检验"接地使过度纠正者克制、使纠正不足者增加修复"的非对称解读。

**训练策略：** 零训练：全部调用 temperature=0、每句一次，经同一 API（2026 年 3–8 月）完成；评分前经 NFKC、小写、ё→е 折叠、去标点且无 ITN；区间为 20,000 次配对句级百分位 bootstrap；比较子集 n=2,260/270/284。

### 📊 实验结果
**数据集**：俄 TTS 合成语料 3,000 句（n=2,260）、RuLibriSpeech 300 句（n=270）、Eka 英语医疗听写 300 句（n=284），Voxtral 子集 467/96/96

**主要指标**：
- 输入 WER（%，TTS/RuLibri/医疗）：ASR 3.95/7.29/16.06，draft 2.39/10.04/17.65
- 自我修正 break-rate：纯文本格 31.9/16.3/12.8% 对比带音频格 2.6/1.0/2.3%
- A−C 分量差：dam 降 0.88–2.83pt，rep 同降 0.15–0.74pt（区间均排除零）
- F−T 净增益：+1.48/+1.18/+1.57pt；rep +0.09/+0.95/+1.25pt（医疗修复 2.06%→3.31%，相对 +61%）
- 医疗插入：ins 分量 −1.08pt 抵消 rep−dam 的 +0.98pt，净 ΔWER 反为 −0.09pt
- 术语召回 DTR：纯文本自我修正 69.0%→66.1%，带音频保持 69.3%
- Voxtral 不复现：六对比带音频 rep 均更高（+0.24~+4.64pt）

**是否开源**：暂无

### ⭐ 评分：6/10
评分理由：贡献在方法论与诚实性：词级记账干净精确，break-rate 首次量化纯文本纠错静默改写正确转录的规模，"修复符号跨设定反转"给出可操作建议——音频调用优先花给独立识别器的输出。但两个自然语料仅约 300 句、不少区间跨零；完整因子设计只有一个商用模型，两臂 prompt 不同无法完全隔离音频，也未与训练式正确器对比。诊断型参考价值高，突破性中等。

---

## [7] Synthetic-to-Real Code-Switched ASR: A Spontaneous Nepali-English Podcast Benchmark

**arXiv ID**：2610.30860 | **方向**：语音大模型

**作者**：Firoj Paudel

**机构**：Wiseyak Inc.

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.30860 | **PDF**：https://arxiv.org/pdf/2610.30860.pdf | **代码**：https://github.com/Firoj-Wise/nepali-english-codeswitch-asr | **Demo**：暂无

### 📌 简介
针对尼泊尔语-英语代码切换ASR中的文字混淆（天城文/拉丁文乱混）与语言切换点错误率偏高问题，本文发布13,044条/15.45小时经双语标注审计的自发播客基准，并提出两阶段合成到真实适配框架：先在0.95小时双引擎TTS合成码混音频上对1.22B IndicTranscribeFlex（冻结FastConformer编码器、仅调24层解码器）做SFT，再用MER+SCR联合奖励做序列级GRPO。全流程将真实测试MER从23.40%降至21.49%、切换点错误率从35.89%降至28.70%（-7.19pp），英语词错误率无显著变化，基准与代码开源。

### 🔧 技术方案

**问题背景：** 真实码切口语采集与标注昂贵；token级脚本门控头在自回归边界施加过刚性约束、反损转写保真；序列级GRPO此前仅在decoder-only音频LLM上验证，其在编码器-解码器架构与自发会话语音中的效果不明。

**模型架构：** 基座IndicTranscribeFlex（Canary-1B-v2，1.22B参数）：FastConformer编码器32个Conformer块（d_model=1024）+24层自回归Transformer解码器、7,152词表；适配时编码器全冻，仅微调解码器+投影头，可训练410.46M参数（33.60%）。

**核心创新：** (1) 双引擎合成语料：Gemini生成尼-英码混句子并5-gram防泄漏检查，OmniVoice扩散TTS（2尼泊尔语男声）+Gemini TTS（4音色）合成517条/0.95h，经电话带滤波、噪声增强与whisper回环过滤，SFT即完成对真实自发语音的主要跨域迁移。(2) 序列级GRPO：每条采样G=8 rollout、组归一化优势、PPO裁剪ε=0.2、KL系数β=0，奖励R=(1−MER)+0.5(1−SCR)，在SFT收敛模型上取得虽小但统计显著的精调。(3) 否定性消融：token级门控使dev MER从18.92%升至19.14%；脚本奖励与纯MER奖励完全同效，因SFT收敛后合成rollout组内脚本方差近零。

**训练策略：** SFT交叉熵、AdamW、lr=1e-5、batch 8、1000步；GRPO自SFT检查点初始化、lr=1e-6、500步、每批32次rollout、最佳checkpoint在step 50；FP16单卡RTX 4090。语料经两名双语标注逐条审计：剔233条乐音与161条机翻泄漏、修819条时间戳重叠，500条双审字符一致98.4%。

### 📊 实验结果
**数据集**：尼英播客基准13,044条/15.45h（测10,214条/52人，dev 2,830条/20人互斥，切换点29,033）；0.95h合成训练；单语：BHASAANUVAD/LibriSpeech

**主要指标**：
- MER：23.40→21.52→21.49%（基线/SFT/GRPO），−1.90pp，95%CI [-2.37,-1.42]
- SPER：35.89→28.70%（总−7.19pp，SFT−7.12/GRPO−0.07，聚类p=0.022）
- SCR_en：6.70→6.36%（GRPO较SFT −0.09pp，p≤0.001）
- 单语：尼泊尔语MER 20.80→18.42%；英语WER 3.33→3.38%（p>0.05）
- 门控对照（dev）：MER 18.92→19.14%、SCR_en 5.35→5.75%劣于SFT

**是否开源**：代码 github.com/Firoj-Wise/nepali-english-codeswitch-asr；数据HF SamaFiroz/nepali-english-codeswitch-podcasts

### ⭐ 评分：6/10
评分理由：贡献重心在严格审计的基准与诚实实证而非方法突破：MER/SCR/SPER解耦指标加配对bootstrap与聚类检验可信度高，0.95h合成数据即实现SPER −7.12pp迁移极具工程价值；坦承脚本奖励零增益、GRPO仅−0.07pp是少见的负面结果分析。但合成数据极小、缺乏多seed与Whisper等外部基线，GRPO收益难与额外梯度步区分，语言对单一，通用性有限。

---

## [8] Lip-Focused Audio-Visual Consistency Detects Speech Content Manipulation beyond Coarse Synchronization

**arXiv ID**：2610.30872 | **方向**：语音前端

**作者**：Jian Zong, Chenghan Lin, Meng Liu, Zhao Xu, Junyu Wang, Siyuan Zhang, Peiyuan Jiang, Longbiao Wang, Jianwu Dang

**机构**：天津大学；中国科学院深圳先进技术研究院

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.30872 | **PDF**：https://arxiv.org/pdf/2610.30872.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
语音内容篡改通过替换音轨并用Wav2Lip类retalking模型重生成口型来规避纹理伪影与粗粒度唇同步检测。本文提出SyncSpeech基准（真实、异源/同源音频拼接cheapfake、Wav2Lip重绘共5个分布内场景，外加Video-Retalking两个未知生成器场景）与唇部聚焦检测器C-MIND：在帧级对齐声学动觉与口部运动表征，用点积与绝对差显式建模一致性，不依赖转写、ASR特征或参考真视频。预训练SyncLip-C在SyncSpeech上达95.813%场景平均准确率、AUC 0.9943，FakeAVCeleb未见说话者子集278/280正确，但对未见Video-Retalking攻击降至82.775%，表明该咬合一致性信号有效但生成器敏感。

### 🔧 技术方案

**问题背景：** retalking系统显式优化音视频同步，使SyncNet类粗唇同步线索被"修复"而失效；合成伪影线索依赖特定生成器，身份校验需注册或声称身份。全脸特征混入姿态、纹理、表情会稀释发音信号，句级池化则掩盖短时不一致，因此需要在身份信息受控后仍可观测的帧级音频-唇动兼容性。

**模型架构：** 双分支编码器：视觉分支以3D卷积前端+残差图像编码器+时序卷积编码96×96灰度口部区域（25fps）；音频分支用扩展时延神经网络（TDNN）编码16kHz、80维log-mel（25ms窗/10ms hop）的帧级声学动态。可学习音频投影Pa与视觉插值UT把两分支映射到共享T×d空间逐帧对齐；SyncLip-C每帧构造交互向量ct=[at;vt;at⊙vt;|at−vt|]，经自适应统计池化ASP后由MLP输出篡改logit。对照变体含句级融合（A类）、帧级拼接（B类）与整脸输入（SyncFace类）；编码器初始化为独立训练的音视频唇动说话人验证模型。

**核心创新：** (1) SyncSpeech操控矩阵将"内容替换"与"身份不匹配"解耦：同源/异源说话者替换×音频拼接×Wav2Lip重绘×未见生成器Video-Retalking共7场景；同源样本音频身份一致且retalking已修复粗同步，使咬合一致性成为唯一可观测量，并配性别平衡配对、0.8–1.2变速对齐等控制。(2) 唇聚焦的帧级显式跨模态交互：点积表征坐标级一致、绝对差表征分歧，避免句级池化抹平短时不一致；消融显示同解码器的整脸SyncFace-C仅56.000%准确率/0.5297 AUC，而SyncLip-C达94.313%/0.9872，证明信息主要由口部区域承载。(3) 说话人验证预训练迁移：以AM-Softmax、29帧88×88口部片段训练的音视频说话人验证模型初始化双分支（维度不匹配的log-mel输入投影重新初始化），无需伪造样本外的语义监督，准确率由94.313%升至95.813%，且检测全程不用转写或真值参考。

**训练策略：** 二进制交叉熵损失；2秒clip；AdamW，新增投影/交互/分类层lr=1e-4，骨干解冻消融时用3e-5；余弦退火+10%预热、weight decay=1e-4、全局batch 32、最多30 epoch；主配置冻结预训练骨干。SyncSpeech训练集20,000真+20,000伪，FakeAVCeleb训练8,255真+8,268伪。以验证集AUC选checkpoint，验证集平衡准确率定阈值后固定测试。

### 📊 实验结果
**数据集**：SyncSpeech（自建，源自LRS3，真实野外说话视频；测试320真+1280伪，seen/unseen说话者各半）；Video-Retalking未见生成器测试627条；FakeAVCeleb未见说话者子集70真+210伪

**主要指标**：
- SyncSpeech场景平均准确率：95.813%，AUC 0.9943（预训练SyncLip-C，Wilson 95%CI 94.72–96.69%）
- 说话者泛化：seen 97.250% / unseen 94.375%（unseen AUC 0.9918）；同源cheapfake 95.938%、同源Wav2Lip 93.438%
- 消融：SyncFace-A句级整脸31.688%/0.5075 → SyncLip-B帧级92.375% → SyncLip-C 94.313% → 预训练95.813%
- 关键对比：SyncSpeech+Video-Retalking合均C-MIND 92.960% vs 复现SyncNet 66.150%（+26.81点）；FakeAVCeleb子集278/280（99.286%）
- 未见生成器场景：82.775%（519/627，CI 79.62–85.53%），仅略高于SyncNet 80.223%；10名人类观察者平均67.750%，Wav2Lip攻击仅35–37%

**是否开源**：暂无

### ⭐ 评分：6/10
评分理由：假设界定诚实、消融链条完整，"唇聚焦+帧级交互"对粗同步失效场景的鉴别价值证据充分，SyncSpeech的同源/异源×拼接/重绘矩阵是有用的法证控制设计。但外部验证薄弱：未见生成器精度大跌至82.8%、仅单个未测生成器，无压缩/噪声等退化压力测试，缺少与最新自监督音视频检测器的同协议对比，且代码未开源，实用复现受限。

---

## [9] Muting Tokens: Exploring Token Sparsification for Efficient Audio Transformers

**arXiv ID**：2610.31235 | **方向**：语音大模型

**作者**：Shreya Sajid, Fabrizio Julian Piva, Hiram Rayo Torres Rodriguez, Elif Ceren Gok Yildirim, Murat Onur Yildirim, Joaquin Vanschoren

**机构**：Eindhoven University of Technology；NXP Semiconductors

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.31235 | **PDF**：https://arxiv.org/pdf/2610.31235.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文针对音频Transformer自注意力随谱图token数二次增长导致推理开销高、且音频域token稀疏化研究仅限单方法/单模型/单数据集的问题，在AST模型上首次系统对比剪枝与合并类稀疏化方法，覆盖三个数据集、三种模型规模及后训练与微调两种设定，并提出基于谱平坦度（SF）与低频能量（LFE）的频率感知token重要性估计新策略。实验显示SF在90%保留率下AS-20K mAP达0.3576、超过未稀疏基线0.3572；25%保留率下LFE在SPC达93.49%准确率，较Top-K的88.73%高4.76个百分点。

### 🔧 技术方案

**问题背景：** 谱图输入使token数随音频时长线性增长、注意力开销二次膨胀，长音频部署代价高。已有音频稀疏化研究或仅评估Top-K/Intensity两种方法、单一ViT-Base与微调设定，或仅将ToMe用在天然稀疏的MAE框架上，缺乏跨方法、跨模型规模、跨后训练/微调场景的统一基准。

**模型架构：** 骨干为ImageNet预训练的AST（Audio Spectrogram Transformer）Base/Small/Tiny三档，16×16 patch、重叠6。稀疏化模块插入每个Transformer块attention与MLP分支之间，按三个等距点分四段施加，保留率r∈{0.90, 0.70, 0.50, 0.25}。评测剪枝类（Top-K、EViT、Intensity、LFE、SF）与合并类（ToMe）方法。

**核心创新：** (1) 提出谱平坦度引导的token剪枝：对每个token embedding沿embedding维做FFT，以谱几何均值/算术均值比作平坦度分数，利用"低平坦度对应谐波化、信息更丰富"的先验，与CLS注意力分数融合排序选top-K，免调参、不改权重，跨数据集与模型规模稳定领先；纯注意力基线无法感知token内部结构化程度，该频率线索补足此盲区。(2) 将视觉LFC思想适配为音频低频能量LFE：在patch投影后的token表示上加高斯低通滤波计算低频能量，并与头加权注意力TopK-Wt融合，优先保留低频结构丰富且被关注的token。(3) 改进Intensity剪枝为两级策略：log-Mel patch能量仅作高/低强度粗分阈值过滤，高亮组内再由CLS注意力排序、不足从低强度组回填，修正了纯强度法在低保留率下的次优表现。

**训练策略：** 沿用AST原始微调配方：AS-20K与ESC50微调25 epoch，SPC训练30 epoch；启用稀疏化时关闭SpecAugment等掩码增强以避免冗余；稀疏化微调从ImageNet权重起、仅用AST-B，后训练稀疏化在已微调模型推理时直接施加；结果报3次运行平均，对比实验重复5-6次；FLOPs用DeepSpeed profiler按batch=1测量（AST-B基线261.43 GFLOPs）。

### 📊 实验结果
**数据集**：Speech Commands V2（105,829条1秒语音、35类）、ESC50（2,000条5秒环境声、50类、5折交叉验证）、AudioSet-20K（10秒YouTube音频、527类，训练~22k/评测~20k）

**主要指标**：
- AST-B基线：SPC 97.67% Acc、ESC50 89.42% Acc、AS-20K 0.3572 mAP
- SF（90%保留率）：SPC 97.68%、ESC50 89.20%、AS-20K 0.3576 mAP，多设定唯一超基线
- LFE（25%保留率）：SPC 93.49% Acc，较Top-K（88.73%）提升4.76个百分点
- 计算量：50%保留率下AST-B AS-20K FLOPs由261.43降至124.85 GFLOPs（降52.3%）
- 控制实验：Intensity剪枝在>2秒音频段上持续优于Top-K；稀疏化微调下各方法25%保留率仍接近基线、方法间差距明显缩小

**是否开源**：暂无

### ⭐ 评分：6/10
评分理由：本文建立了音频token稀疏化的首个统一基准，将谱平坦度等经典声学先验引入token打分，思路简洁有效，输入时长的受控实验有实际指导价值。但性能增益整体偏小（mAP差距约0.003级），效率仅以FLOPs代理、缺实测延迟/吞吐，且未开源代码，属扎实的增量性实证工作，适合边缘音频部署者参考选型。

---

## [10] A corpus-only AUC diagnostic for pooled speech-based depression detection

**arXiv ID**：2610.31247 | **方向**：语音大模型

**作者**：Cezary Polak, Milosz Dudek, Daria Hemmerling

**机构**：SoftServe（波兰克拉科夫）、AGH University of Krakow

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.31247 | **PDF**：https://arxiv.org/pdf/2610.31247.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
将多个临床语音语料库合并评估语音抑郁检测时，各库阳性率不同会使"语料库身份"本身成为可预测标签的捷径。本文推导出一个仅用语料库身份与经验患病率的oracle预测器AUC闭式解，可直接从语料构成计算，无需音频。在3种语言5个抑郁语料库（590名说话人）上，corpus-only AUC达0.697，且六种声学/自监督表征能以97.5–99.8%准确率识别语料库身份；库内标签置换与患病率均等化实验表明，pooled与LOCO评估差距随诊断值同序增大、并在均等化后显著缩小，提示池化评估会因语料库特异基率而高估临床判别力，应联合报告语料感知诊断。

### 🔧 技术方案

**问题背景：** 单个临床语音语料库太小，模型比较常依赖多库合并；但即使说话人不重叠的交叉验证下，各fold仍共享语料库特异的采集条件、语言、诱导任务与标签分布，模型可利用源信息走捷径。此前工作只定性报告跨库性能退化与DAIC-WOZ面试官捷径，缺少能直接计算的量化诊断。

**模型架构：** 框架含三部分：(1)闭式corpus-only AUC：给定各库规模n_k与患病率p_k，oracle按p_k打分，对正负样本对加权求和（同分计0.5）；(2)语料库识别探针：L2正则化多项逻辑回归从冻结表征预测库身份；(3)双协议对照：同一冻结表征+逻辑回归头，pooled 5折CV与留一库out（LOCO）对比。表征为eGeMAPS（88维）与WavLM-Base/Base+、HuBERT、XLS-R、mHuBERT-147，SSL编码器全部冻结。

**核心创新：** (1) 推导出仅依赖语料构成的闭合AUC诊断，量化"库身份+患病率"单独可提供的判别度；作者明确其非模型AUC上界、不应直接相减，而是池化评估的警告信号。(2) 库内标签置换：保留各库规模与患病率、破坏库内语音-标签关联；三个嵌套配置（AUC 0.567/0.621/0.697）的残余pooled−LOCO差距+0.003/+0.023/+0.060，与诊断值单调同序，证明基率通道对模型可及。(3) 患病率干预与控制：子采样至公共患病率0.19使诊断值降为0.501，eGeMAPS/WavLM-Base差距由+0.113/+0.206变为-0.032/+0.023，而样本量匹配对照仅变-0.011/+0.003，确证差距源于患病率异质性而非样本量。

**训练策略：** 音频重采样16kHz单声道、RMS归一化-23dBFS；超30秒切30秒窗，帧级隐状态先窗内平均再跨窗平均；eGeMAPS v02由openSMILE提话语级泛函；同subject多clip平均为subject级向量；DAIC-WOZ仅保留受试者声道。下游为L2逻辑回归，标准化仅在训练fold拟合；pooled用全局类别平衡权重，LOCO按库等质量加权。平均30种fold划分；置换审计用200次库内置换。

### 📊 实验结果
**数据集**：5个抑郁语音语料库、3语言（EN/ZH/IT），590说话人/150阳性（总患病率25%）：DAIC-WOZ（141，29%）、EATD（162，19%）、MPDD-Elderly（87，13%）、MPDD-Young（88，11%）、Androids-Read（112，52%）。

**主要指标**：
- corpus-only AUC：0.697，仅由语料构成计算，不用任何语音信号
- 库身份识别精度：97.5–99.8%（六种表征），多数基线27.5%；剔除最大库EATD后仍99.5–100%
- pooled vs LOCO AUC差距：XLS-R最大+0.291（0.725对0.434），WavLM-Base+ 0.209，eGeMAPS +0.154，六种表征pooled全部高于LOCO
- 患病率均等化后差距：eGeMAPS +0.113→-0.032，WavLM-Base +0.206→+0.023；样本量匹配对照仅变化-0.011/+0.003
- 关键对比：置换后残余差距随配置嵌套(+0.003→+0.023→+0.060)与诊断值同序增长

**是否开源**：论文正文未提供代码或数据链接，暂无

### ⭐ 评分：6/10
评分理由：切入角度新颖且实用，闭式诊断极易落地，置换+均等化+样本量对照的机制归因设计干净，对抑郁检测及一切池化临床评估有直接方法论价值。不足在于独立语料配置仅3个、无法拟合剂量-响应关系，语言与库身份部分混叠，只测冻结表征+线性头，结论适用范围有限，且未提供可复用代码，属于有参考价值的方法学增量工作。

---

## [11] Query-Conditioned Liquid Temporal Grounding for Long-Form Audio

**arXiv ID**：2610.31252 | **方向**：语音大模型

**作者**：Yuelan Cheng, Yonggang Zhu, Yongqiang Chen, Peiwei Chang, Yingyi Chen, Wenwu Wang

**机构**：University of Surrey（CVSSP）、中国农业大学、北京邮电大学

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.31252 | **PDF**：https://arxiv.org/pdf/2610.31252.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对长音频时间定位（TAG）中目标片段仅占录音极小部分、查询含多重语义约束导致时间搜索空间巨大的难题，本文提出查询条件化液态时间定位框架：先用FiLM把查询语义注入音频时序表征，再由闭式连续时间网络（CfC）建模长程依赖并生成多候选区间，冻结的大音频语言模型按Yes/No兼容性选出最优候选，最后轻量精修边界。在LAT-Bench英文TAG子集上，Qwen3-Omni主干最高达44.13% mIoU、46.95% R@0.5，较QA-SFT基线提升4.93个百分点，且仅单张A100即可完成训练。

### 🔧 技术方案

**问题背景：** 现有音频语言模型的时间定位性能随录音时长显著退化：目标事件周围常存在声学或语义相似内容，查询又同时约束说话人、事件、属性与时序关系，直接回归单一区间或滑动窗口枚举难以在巨大搜索空间中兼顾效率与精度。

**模型架构：** 以冻结的MOSS-Audio-8B-Instruct或Qwen3-Omni-30B-A3B-Instruct为主干；音频表征投影池化为T帧序列H，查询编码器给出token级Q与池化q；FiLM调制后送入CfC单元（时间步Δt=D/(T-1)绑定物理时长），经LN+Dropout得状态序列Z；并行分支用token级与全局相似度加权得逐帧匹配信号p^m；F=LN([H̃;Z;p^m])拼接后由start/end/relevance三个轻量头输出分布。候选提取无训练参数；Qwen3-Omni分支另加精修器：候选边界外扩±5s窗口，冻结音频编码器语义特征与mel谱Conv1D声学特征经FiLM融合，预测带sigmoid门控的边界残差（δ_max=5s）。

**核心创新：** (1) 把FiLM条件注入置于CfC之前，使液态网络连续时间、输入自适应的动力学直接依赖查询条件化表征，查询语义影响长程时间信息传播而非仅下游打分；消融显示FiLM仅在耦合CfC时生效（Qwen上mIoU由38.37%升至42.72%，单独FiLM反而降至33.85%）。(2) 可训练模块只学习边界、相关性、匹配三类时间证据，候选生成完全参数化且保留多假设，语义判别交由冻结LALM的Yes/No双softmax完成，分工明确且免主干微调。(3) 局部门控残差精修只微调已选候选，训练时剔除修正量超5s的样本，避免越界梯度污染。

**训练策略：** 主干全程冻结，仅优化定位模块。总损失为边界soft-target、focal式类平衡BCE相关性、hard-negative匹配、一维GIoU、end边界hard-negative五项加权和，权重取(0.3,1.0,0.5,0.5,0.3)；精修器用SmoothL1+1-IoU。AdamW、学习率1e-4、3轮、1024时间bins、9:1训练/验证划分，单张NVIDIA A100完成全部实验。

### 📊 实验结果
**数据集**：LAT Chronicle英文TAG子集共3,737条query–segment对用于训练，LAT-Bench英文TAG子集（录音最长30分钟）评测，指标为mIoU与R@0.3/0.5/0.7。

**主要指标**：
- mIoU：Qwen3-Omni（Union候选池+精修）44.13%，MOSS-Audio 38.52%
- R@0.5：Qwen3-Omni 46.95%，MOSS-Audio 40.61%；R@0.3最高65.26%
- 关键对比：Qwen3-Omni mIoU较QA-SFT基线39.20%提升4.93个百分点，较Direct 15.80%提升28.33个百分点，但低于LAT-Audio主模型的50.00%
- 消融与上限：GRU替换CfC后mIoU跌至31.29%（Qwen）/32.00%（MOSS）；候选池oracle mIoU达55.20%，Top-1与oracle差距表明LALM选择仍是主要瓶颈

**是否开源**：正文未给出代码/Demo链接，暂无

### ⭐ 评分：6/10
评分理由：将FiLM+液态CfC时间建模与冻结LALM候选选择相结合，对长音频TAG是有实质价值的增量贡献，双主干结果一致、FiLM/CfC/GRU消融设计较严谨，单卡免微调的训练成本低、工程可复现性好。局限在于仅在LAT-Bench英文子集评测，绝对性能未超越LAT-Audio专用模型，且选择瓶颈未解决、代码未开源，通用性与影响力受限。

---

## [12] Measuring the Verifier's Floor: How Much Apparent Rare-Word Text-to-Speech Error Is ASR Error?

**arXiv ID**：2610.31470 | **方向**：语音大模型

**作者**：Kirill Borodin, Vasilii Kudryavtsev, Nikita Vasiliev, Grach Mkrtchian

**机构**：BitmanagerAI（迪拜）；lab260（埃里温）

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.31470 | **PDF**：https://arxiv.org/pdf/2610.31470.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
TTS 通常用 ASR round-trip WER 评估，但该指标同时计入识别器自身错误，且错误集中在恰是 TTS 报错高发区的稀有词上。本文在 LibriSpeech 和 FLEURS 的真人原始录音与合成语音上运行三族识别器（Whisper large-v3-turbo、wav2vec 2.0 large、OWSM v3.1），系统比较标准 round-trip、单识别层掩蔽、三识别层仲裁三种 TTS 错误估计。结果显示评估识别层在人类语音上漏掉 32.9%（LS）—66.7%（FLEURS）的极稀有词；仲裁使表观 TTS 错误降 2.8—3.2 倍（极稀有词由 10.1/13.4% 降至 3.4/4.7%），但极稀有词仍最难；单识别层掩蔽是有偏的修正，剩余错误约一半疑似拼写变体，需听力测试确认。

### 🔧 技术方案

**问题背景：** ASR round-trip 同时测量两个系统：若识别器连人说某个词都转写不出，该词上的"错误"几乎不能说明 TTS 的问题。先前工作称稀有词是 TTS "真正的极限而非采样问题"，但未在真值音频上测过其假阳性下限（floor），本工作正是量化这一验证器下限。

**模型架构：** 纯测量框架，无新模型。每句测试文本有真人原声与 N 条合成版本，由识别器 C（评估者，OWSM v3.1）和 A/B（Whisper large-v3-turbo、wav2vec 2.0 large，仅用于复核）转写。文本用 Whisper 英语规范化器对齐；参考词完全匹配、或仅空格差异（≤3词）记为"听到"；忽略插入，统计的是词漏检率而非 WER。频率用 wordfreq 的 Zipf 刻度，极稀有 z<2.5、常见 z≥4.5。

**核心创新：** (1) 首次在真人录音上直接测验证器假阳性下界并按词频分层：C 漏掉常见词仅 1.5% 而极稀有词达 32.9%，三族一致漏掉 21.6%（FLEURS 41.7%）极稀有词根本不可评判。(2) 提出三识别层仲裁判定 err(w)=[hA∨hB∨hC]∧¬[sA∨sB∨sC]，即词被判定需至少一族在人类语音听到、且无族在任一合成版本听到；对 best-of-N 保留候选也给出保守比较。(3) 用 A/B 作反向裁判证明单识别层掩蔽有偏：它删掉的恰是 TTS 真错最多的词（3.9%—6.0% vs 保留词 0.2%—0.3%），且其保留错误约一半被仲裁推翻。

**训练策略：** 不涉及模型训练。F5-TTS 以随机种子生成 N=8（FLEURS 为 4）条克隆 test-clean 五说话人语音；Kokoro-82M 确定性输出，N=4 用四个音色。统计用句级百分位 bootstrap（4000 重采样）给 95% CI，零错误格用 Clopper-Pearson 上限；趋势为句级 Pearson 相关，明确标注为探索性。

### 📊 实验结果
**数据集**：LibriSpeech test/dev 500 句（15—30 词，均值 20.8，稀有词占比 0—41%）；FLEURS en_us 前 200 条录音（161 句，12—30 词）

**主要指标**：
- 人类语音 ASR 漏词率（极稀有 vs 常见）：C 层 32.9% vs 1.5%（LS）、66.7% vs 3.2%（FLEURS）
- 仲裁后表观 TTS 错误（any-of-N，判定词）：F5-TTS 0.63%→0.22%、Kokoro 0.72%→0.22%，标准/仲裁比 2.8 [2.1,4.1] 与 3.2 [2.4,4.8]，FLEURS 为 3.3
- 极稀有词仲裁错误：F5-TTS 3.4% [1.4,5.4]、Kokoro 4.7% [2.5,7.2]（标准掩蔽下为 10.1%/13.4%）
- 掩蔽偏差：C 漏词的 TTS 错误率 3.9%/4.9%/6.0% vs C 听到词的 0.2%/0.3%；53%/64%/56% 的保留错误被推翻
- 仅计真实发音偏差后极稀有词错误 1.7%/1.7%/5.7%：稀有词仍是最难

**是否开源**：结论承诺将释出代码、句子清单与全部转录，当前未提供仓库地址

### ⭐ 评分：6/10
评分理由：直击 TTS 评估中 ASR 假阳性混淆这一真实痛点，实验设计干净（句级 bootstrap、双向偏差检验、best-of-N 保守口径），四条实践建议即刻可用。局限也明确：仅 23+23+18 个仲裁错误、区间宽、趋势为探索性且未跑听力测试，B/C 在 LibriSpeech 上训练带来域偏置。作为增量但方法论扎实的评估研究，对做 TTS round-trip 的团队有直接参考价值。

---

## [13] AGF-Net: A Robust Multimodal Emotion Recognition Model for Asynchronous Audio-Visual Signals Based on Predictive Dynamic Fusion with Negative Learning

**arXiv ID**：2610.30651 | **方向**：语音大模型

**作者**：Chuan-Han Li, Yun-Chien Cheng

**机构**：阳明交通大学机械工程学系、台湾大学电机工程学系

**发布日期**：2026-10-23 | **论文**：https://arxiv.org/abs/2610.30651 | **PDF**：https://arxiv.org/pdf/2610.30651.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对多模态情绪识别依赖人工标注话语边界、真实连续音视频流中模态失衡与音画异步的问题，本文提出整合自动话语分割（Silero VAD+自适应端点+语义保持）与Audio-Guided Fusion、Predictive Dynamic Fusion、Multimodal Negative Learning三策略的AGF-Net框架。在IEMOCAP上，干净条件达64.92%准确率/65.47% F1，噪声λ=5与λ=10下分别为62.13%/63.08%和58.19%/59.41%，中度噪声F1居对比方法首位。

### 🔧 技术方案

**问题背景：** 现有方法多以手工切分话语为输入，而实际系统只获得连续流，自动切分带来边界漂移、片段时长失当与说话人泄漏；叠加模态失衡、音画异步与固定权重融合无法适应可靠性变化，稳定性受损。

**模型架构：** 音频重采样16 kHz经wav2vec 2.0提特征；视觉经YuNet检测与五点landmarks对齐、裁剪224×224后由ResNet18编码。AGF（音频引导滞后感知）将每个音频事件映射为最相关视觉帧的高斯参数(μ,σ)，高斯掩码作偏置注入缩放点积注意力，实现内容相似性与时间先验联合约束；再以Hybrid Fusion融合特征级与音/视/融合三分支决策输出。决策端由PDF按分支可靠性动态加权，训练端由MNL稳定弱分支决策空间。

**核心创新：** (1) 自动话语分割将切分建模为语音状态跟踪：VAD概率经EWMA平滑+滞回阈值+按长度自适应端点+partial-ASR语义保持，摆脱人工边界并缓解停顿致过度切分，端点延迟约564 ms。(2) AGF把音画异步表述为高斯先验约束的交叉模态密度估计，滞后预测器联合学习目标帧位置μ与不确定度σ，偏置注意力抑制背景干扰且可解释，区别于纯内容匹配对齐。(3) PDF/MNL协同缓解模态失衡：PDF以真值类概率作置信代理，mono/holo-confidence合成Co-Belief经相对校准非对称降权高不确定分支；MNL在warm-up后以强模态引导弱模态抑制非目标类，推理零开销。

**训练策略：** 损失为三分支交叉熵+可靠性MSE，权重1.0/0.2/1.0；AdamW，100轮+早停，batch size 8，分层学习率（预测头1e-4、音视频分支1e-5）；按Actor-ID被试独立划分；噪声按RMS注入音频高斯白噪声、按λ/255注入图像高斯噪声，每次仅扰动单一模态。

### 📊 实验结果
**数据集**：IEMOCAP（约12小时双人互动音视频，10名演员5个session，取angry/happy/neutral/sad四类），5折评估

**主要指标**：
- 干净(λ=0)：准确率64.92%、F1 65.47%，较最强Social-MAE(66.72%/67.89%)低1.80/2.42个百分点
- 中度噪声(λ=5)：准确率62.13%、F1 63.08%，F1领先Social-MAE/AVF-MAE/VAVL各0.52/4.15/7.89个百分点
- 高强度噪声(λ=10)：准确率58.19%、F1 59.41%，F1仅落后最佳0.20个百分点
- 分割性能：IoU>0.5下F1由置信端点0.4372、自适应端点0.4532升至加语义保持0.4608，平均延迟564.0 ms
- 消融：AGF使准确率/Macro F1升0.91/1.26个百分点；MNL以30轮warm-up最优（57.17±5.15%/56.79±5.51%）；PDF在λ=5/10使Macro F1提升2.13/1.99个百分点

**是否开源**：暂无

### ⭐ 评分：5/10
评分理由：面向真实连续流的分割+融合系统完整，消融层层递进且单模态噪声评估贴近部署；但PDF、MNL、锚定融合等均复用已有工作，原创以整合为主，模块参数量缺失，LOSO约57%与最终64.92%两套口径可比性存疑，且仅验证单一数据集，属增量型集成研究。

*Subagents used for reading: 13* | Generated on 2026-10-23 语音论文批次, by Kimmy's research agent | Powered by VAgent SpeechAI Researcher
