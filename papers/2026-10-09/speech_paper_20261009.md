# 2026-10-09 语音论文速递

**共收录**: 25 篇 | **语音大模型**: 19 篇 | **语音前端**: 6 篇

> 目标日期 2026-10-09（北京时间）arXiv 语音相关论文共命中 25 篇。
> 以下是按评分排序的结果。

### 速递说明

本批次精选前 15 篇进行完整模板精读，按评分由高到低排序；其余 10 篇论文仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），未展开精读。

---

## Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners

**arXiv ID**：arXiv:2610.10868 | **方向**：语音大模型

**作者**：Xilin Jiang, Shun Zhang, Tejas Jayashankar, Yinghao Aaron Li, Osama Hanna

**机构**：Columbia University、Meta Superintelligence Labs

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.10868 | **PDF**：https://arxiv.org/pdf/2610.10868.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出基于Qwen2.5-Omni 7B的对话语音审美模型CVAM，给定上文语境与真实或合成应答语音，输出四段证据化描述与九个类别标签（性别、音高、语速、情绪、delivery）。针对情绪/delivery等主观维度缺乏确定真值的问题，团队对CANDOR衍生3k条应答采集每条约10份人工投票，先以30k条Gemini 3.1 Pro合成标注SFT，再用GRPO对齐人类投票分布。最终感知字段平均macro-F1达50.1%，超过Gemini 3.1 Pro（44.2%）与各开源语音LLM，并高于单个标注者对其余人的平均一致性（43.5%）。

### 🔧 技术方案

**问题背景：** 现有语音质量度量与LLM评判（AudioJudge、WavReward、SpeechJudge等）多为孤立话语级判断，忽视情绪、delivery等属性依赖对话上文；同时人类感知主观不一致，单点标签无法刻画群体分布，合成标注还会继承LLM标注者的失准。

**模型架构：** CVAM以Qwen2.5-Omni 7B为骨干，输入3–30秒语境语音与应答语音，禁用talker头、仅用thinker输出JSON（四描述+九标签）。客观标签由工具测定：Praat取F0（均值阈值[100,150,200,250] Hz、标准差[2,3,4,5]半音）、faster-whisper-large-v3转写加NeMo强制对齐得音素速率[7,9,11,13]/s。

**核心创新：** (1) 真实与合成同标准评测数据：CANDOR每条真实应答经Qwen3-TTS扩展voice-clone与voice-design版本使数据三倍，voice-design由Qwen3-Omni按统一采样的情绪/唤醒度/温暖度/自信度标签生成prompts，补足罕见情感覆盖。(2) 两阶段后训练：先在30k合成标注上SFT建立输出格式与描述能力，再在1.5k人类投票数据上RL，兼避纯合成失准与纯人类数据饥饿。(3) 留一法分布奖励：G=16 rollouts，感知奖励为φ=-∂D(p,q)/∂q(c)，即以人类对该标签的支持度对比其余rollout（排除自身、λ=1拉普拉斯平滑）的频率，奖励稀有标签、抑制过产标签；对比Frac/TVD/前向KL/反向KL四类奖励。

**训练策略：** 两阶段均LoRA（rank 32、α=64）调thinker全部线性层，冻结音频编码器与aligner；各训1 epoch，cosine调度+5% warmup，bfloat16；SFT lr=1e-4（2×8 A100），GRPO lr=1e-5（4×8 A100），rollout温度1.0，对冻结SFT策略KL系数β=0.04；性别+四客观标签用accuracy reward占5/9，四感知字段占4/9；框架为ms-swift+vLLM加速rollout。

### 📊 实验结果
**数据集**：CANDOR英语自然对话语料，10k+0.5k训练与0.5k测试turn（×3版本=30k合成标注样本；1.5k+1.5k条人工标注，平均9.7/9.8票，测试集14,664条judgment/字段）

**主要指标**：
- 感知平均macro-F1：50.1%（SFT_synth+GRPO前向KL），Gemini 3.1 Pro为44.2%、单人对其余43.5%、Qwen2.5-Omni基座31.1%
- 感知平均accuracy：77.8%（Frac奖励，最高acc）对Gemini 60.2%
- 分字段F1（KL模型 vs Gemini）：Emotion 40.5 vs 37.9、Arousal 59.3 vs 46.3、Warmth 51.9 vs 44.4、Confidence 48.6 vs 48.4
- 客观字段（不注入工具测量）：性别Acc 99.0、音高均值73.1、语速71.2
- 关键对比：比最强基线Gemini 3.1 Pro提升约5.9pp macro-F1，且超出人类单体一致性水平

**是否开源**：暂无（论文未给出代码或Demo链接）

### ⭐ 评分：8/10
评分理由：将语音审美描述纳入对话语境并以人类群体投票分布为对齐目标，留一法分布奖励推导严谨，且用Frac与KL奖励实证了 Majority精度与稀有类覆盖的权衡，方法论贡献清晰。实验含多基线、奖励消融、真实/克隆/设计版本分解与混淆矩阵分析，"超单人一致性"的结论尤有说服力。局限在于仅英语CANDOR单一语料、测试规模1.5k、模型数据未开源，落地复用成本较高。

---

## DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration

**arXiv ID**：arXiv:2610.11299 | **方向**：语音大模型

**作者**：Yingda Shen, Yuxiang Wang, Kunyu Feng, Qinke Ni, Jiaqi Li, Minghao Hsu, Junan Zhang, Dekun Chen, Yutong Bian, Zhizheng Wu

**机构**：The Chinese University of Hong Kong, Shenzhen；Amphion Technology Co., Ltd

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11299 | **PDF**：https://arxiv.org/pdf/2610.11299.pdf | **代码**：https://amphionteam.github.io/DuplexAgent-RSI-Demo/ | **Demo**：https://amphionteam.github.io/DuplexAgent-RSI-Demo/

### 📌 简介
全双工语音智能体常把交互模型与长时任务的协调耦合进启发式harness，故障难归因、修复难验证。本文提出DuplexAgent：全双工模型驻守实时通道，推理LLM与编码智能体委托池处理复杂任务，harness拆为Policy/Intake/Hold/Worker/Deliver/Memory六个可编辑模块；并提出Duplex-Harness-RSI闭环，由模拟器生成定时测试与失败轨迹，同一池兼任Exam Planner与Harness Editor修订模块。VoiceChat上十轮RSI把固定核心协作分从54.6升至85.3，BFCL均分75.8，超越同接口委托基线。

### 🔧 技术方案

**问题背景：** 全双工模型能持续听说但推理与工具能力有限，编码智能体可长程执行却顾不了实时通道；Qwen-Audio-Agent、Realtime-Venus等方案把接受、更新、取消、交付决策耦合进系统特定启发式，故障难归因到环节，有界修复难隔离、评估与迁移。

**模型架构：** 系统S=(F,B,H)：F为全双工交互模型（VoiceChat-11B或Qwen-Realtime），B为推理LLM+编码智能体委托池，H为六模块harness——Policy决定回答/委托/任务控制路由，Intake解析请求并关联活跃任务，Hold维护回执与进度，Worker选择delegate与结果契约，Deliver控制返回时机，Memory共享对话与后台上下文；辅以任务账本session engine与模型adapter。

**核心创新：** (1) 六模块把故障归因到有界可编辑面，Diagnoser从trace输出失败签名(cause,module,pattern)，区分任务未更新与旧结果误交付，修复变为可检验假设。(2) 同一池兼任改进角色：Exam Planner按归因与repair archive在19种请求类型×22种交互模式上加权重排考试（固定核心40%、每轮30新变体），Harness Editor每轮出3个候选、至多2次细化。(3) 可验证保留：配对wins/losses依次过development/protection两道gate并检查六条协作不变量，被拒候选存档防重复犯错。

**训练策略：** 全程不更新模型权重；DeepSeek-v4-flash生成测试内容，Qwen3-TTS合成多风格语音并加噪声与信道增广，composer在实时时间轴注入轮次与延迟/失败，按60/20/20切分dev/protection/sealed三集，VoiceChat与Qwen-Realtime各跑独立战役。

### 📊 实验结果
**数据集**：VoiceBench（OBQA、MMSU），BFCL-v3（5个单轮子集），FDB-v3（不流畅语音工具调用），FDB-v1（pause/turn/interrupt），均为百分比口径。

**主要指标**：
- BFCL-v3均分：90.8%（Qwen-Realtime）、75.8%（VoiceChat），vs 独立模型82.0/53.5、Qwen-Audio-Agent 80.8/24.9
- FDB-v3 Pass@1：49.0%（Qwen-Realtime）、47.0%（VoiceChat），比Qwen-Audio-Agent高19.0与42.0个百分点
- OBQA/MMSU：92.1%/82.7%（Qwen-Realtime）、80.6%/80.5%（VoiceChat）
- 中断TOR：0.97（Qwen-Realtime）、0.965（VoiceChat）
- harness消融：VoiceChat固定核心Q从54.6到85.3，高于顺序编辑23.4分、one-shot编辑27.9分；Qwen-Realtime从g0 47.1到g8 84.8

**是否开源**：项目主页与代码入口均为 https://amphionteam.github.io/DuplexAgent-RSI-Demo/ ，论文称实验采用已发布实现的默认配置。

### ⭐ 评分：8/10
评分理由：将全双工协作从模型能力问题重构为harness工程问题，模块化解耦加证据驱动的递归修复是系统性创新，双交互模型上外部基准、消融与逐模块归因证据链完整，对语音智能体落地价值高。不足是改进依赖强外部LLM与编码代理，模拟器自建Q指标与外部基准不可直接比较，且synthetic pause TOR出现回退，属有实质贡献的系统型工作。

---

## DiffuPlex: Accelerating Full-Duplex Spoken Dialog Models via Rolling Masked Diffusion

**arXiv ID**：arXiv:2610.12214 | **方向**：语音大模型

**作者**：Heeseung Kim

**机构**：Department of Artificial Intelligence, University of Seoul（韩国首尔）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.12214 | **PDF**：https://arxiv.org/pdf/2610.12214.pdf | **代码**：暂无 | **Demo**：https://diffuplex.github.io/

### 📌 简介
细粒度全双工语音对话模型（Moshi、PersonaPlex 系列）每 80ms 交互帧都必须执行一次时间骨干自回归前向，计算量随对话时长线性增长。本文提出 DiffuPlex 滚动掩码扩散框架：每次"骨干唤醒"用可学习 MASK token 并行预测未来最多 W=16 帧的用户与助手流，仅消费高置信前缀并按原帧率播放；当真实用户输入偏离预测时，保留已播放内容、只修订未播出未来。在 Full-Duplex-Bench v1.0 上 Listen/Speak 两策略平均每唤醒推进 1.91/2.23 帧，取得 1.46x/1.59x 部署路径墙钟加速与 1.61x/1.80x Core LM 加速，唤醒帧 p99 延迟全部低于 80ms；Listen 基本保持音质与对话质量（NMOS 3.92 对基线 3.93）。

### 🔧 技术方案

**问题背景：** 现有端到端全双工模型以 12.5Hz（每帧 80ms）逐帧自回归推进骨干，即使实测 95.3% 活跃对话时间仅单方在说话；粗粒度 chunk 序列化方法虽省电计算，但牺牲对打断、重叠、backchannel 的即时反应能力。

**模型架构：** 基于 personaplex-rl-seamless 骨干（Mimi 8 码本×双流 17 路输入流、12.5Hz、80ms 交互网格）。每次唤醒按各流原生延迟的"阶梯式"规则将尚不可用的未来输入替换为流专属可学习 MASK，一次前向同时预测 W=16 个未来位置的用户与助手流，depth transformer 仍在帧内对码本保持自回归。训练采用 block diffusion 的 clean-context 布局：干净序列与按均匀采样块长 1..W 平铺的掩码副本拼接。骨干完全冻结，仅训练 MASK 嵌入与未来门控 LoRA（rank 128、scale 2.0、门控 g(h)=1[h>=2]，同时作用于时间骨干与 depth transformer），h=1 保持原始自回归路径。

**核心创新：** (1) 全双工场景的联合掩码未来预测：区别于文本投机解码和 VocalNet-MDM 等语音块扩散（更远输出可由已有输入推出），全双工对话的助手未来依赖尚未到达的用户语音，DiffuPlex 将用户流与助手流在同一未来区间联合预测，使用户预测可稍后充当草稿一致性校验依据。(2) 滚动草稿生成与双保留策略：按置信度 C_h=softmax(z_h) 前缀保留，阈值 τ_conf=0.80，h=1 恒保留保证每唤醒至少推进一帧；Listen 仅在预测助手状态保持 PAD（持续聆听）时消费未来（最短保留 m=6），Speak 放宽至 EPAD/词元状态（m=2），形成"保守省时"与"激进省时"的两档推理策略。(3) 用户感知草稿修订：唤醒时存下用户分布 q_h，实际用户语义 token 到达后无需再唤醒即可校验，按近似后验几率分数 -log q_h(x_h)+log P_h(A_h(y_h))-log P_h(y_h) >= τ_rev=-0.5 触发修订；已播出助手音频全部保留，仅丢弃未播出未来从最新交互状态重新唤醒预测，保证交互连续性与实时节拍。

**训练策略：** 以冻结 AR 骨干在干净序列上的分布为教师，对掩码学生做 KL 蒸馏，覆盖助手文本、PAD/EPAD/lexical 三态分组分布（与文本 KL 等权以保对话动态）、音频码本（说话人语义 cb0 权重 1，cb1–7 权重 0.02）。数据为 Seamless Interaction 面对面双通道对话，重采样 24kHz、Qwen3-ASR-1.7B 转写、ForcedAligner-0.6B 词级对齐、Silero VAD 与串扰/单边/低语音密度过滤后保留 42,413 会话共 2,728.5h（双声道角色互换得 84,183 例）。窗口上限 2,048 时间位（约 163.8s）；AdamW，lr 1e-4、wd 0.1、梯度裁剪 1.0、OneCycle 15% 预热+bfloat16+梯度检查点，每卡 batch 4、梯度累积 2、4 张 RTX A6000（有效 batch 32），训练 526 步、消耗 16,832 窗口约 702h 音频，取第 526 步检查点。

### 📊 实验结果
**数据集**：Full-Duplex-Bench v1.0/v1.5、VoiceBench、OpenAudioBench；60-clip 固定运行时子集（单张 NVIDIA RTX A6000 测速）

**主要指标**：
- 每唤醒平均推进帧数 c：1.91（Listen）/ 2.23（Speak），自回归基线为 1.00
- 部署路径墙钟加速：1.455x（Listen）/ 1.590x（Speak）；Core LM 加速：1.608x / 1.797x，对 RL-Seamless 基线净省 248s/291s
- 唤醒帧墙钟 p99：61.34ms / 61.41ms，超 80ms 帧占比 0%
- 人评 NMOS：3.92±0.11（Listen，基线 3.93±0.12，仅差 0.01）；Speak 3.54±0.12（降 0.39）；DMOS：4.08±0.13 对 4.09±0.14
- VoiceBench s→t：31.93（Listen）对骨干 31.95，通用语音能力基本无损
- 关键对比：免训练 deferred 基线 R=6 时 PAD 达 2.05x 墙钟加速但 backchannel 频率从 0.163 跌至 0.048、轮换延迟从 0.124s 恶化至 0.423s，DiffuPlex 以约 1.5x 换取交互行为近乎保持

**是否开源**：代码与权重暂未开源（工件表仅列外部依赖），匿名演示页 https://diffuplex.github.io/ 提供音频样例与定性 Demo

### ⭐ 评分：8/10
评分理由：把掩码扩散的并行预测迁移到"验证所需的用户未来尚未到达"这一全双工特有约束，用户-助手联合预测加深存草稿修订规则是真正针对该场景的设计创新；基准、人评、运行时三线验证完备，80ms 实时性论证扎实且 ablation 充分。不足在：1.5x 级绝对加速幅度有限，Speak 策略的 NMOS 明显退化暴露省时与音质权衡未解决，且无代码开源复现门槛较高，单作者工作。整体属系统向的实质性贡献，对全双工语音推理效率研究有直接参考价值。

---

## Edit Who Speaks, Control How They Speak: Global Timbre Editing and Local Instruction Control for TTS

**arXiv ID**：2610.11437 | **方向**：语音大模型

**作者**：Junchuan Zhao, Chenglin Xu, Wei Zeng, Haoyang Li, Yiwen Guo, Ye Wang

**机构**：新加坡国立大学、LIGHTSPEED、南洋理工大学、独立研究者

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11437 | **PDF**：https://arxiv.org/pdf/2610.11437.pdf | **代码**：暂无 | **Demo**：https://danny-nus.github.io/EDICT-demopage/

### 📌 简介
指令式TTS的语音克隆与声音设计两类接口都无法对给定参考音色做"相对编辑"，且句级指令对内部各文本段的语气措辞欠规定。EDICT以两级级联统一全局音色编辑与局部指令控制：可训练的音色编辑器在codec token空间生成编辑后参考，作为全句共享的语音锚点；冻结的TTS主干逐段生成并在指令边界重建KV缓存刷新条件。在自建TimbreEdit-Bench与IntraTTS-Bench上，目标相似度WavLM SIM-T达0.819、段级指令准确率82.30%，分别超最强基线0.118与8.05个百分点。

### 🔧 技术方案

**问题背景：** 现有可控TTS要么声学克隆、要么文本造声，缺少以参考为基准"改指定属性、保留未提及属性"的编辑接口；句内分段控制上，TED-TTS的掩蔽不刷新声学历史，缓存KV携带前段条件导致控制泄漏，全部保留会削弱新指令、全部丢弃又失去自然衔接。

**模型架构：** 两级级联。可训练编辑器从Qwen3-TTS-12Hz-1.7B-Base初始化并全参微调，输入源参考codec序列、序列化编辑操作与编辑参考文本，输出编辑后codec参考；冻结主干采用Qwen3-TTS-VD并以CosyVoice 2为第二主干，该参考在N个(文本,指令)对间保持不变，逐段生成拼为一条连续codec流再解码波形。推理时Qwen3-14B先把自然请求解析为9类属性操作：性别、年龄、音高域、明亮度、嗓音重量、共鸣焦点、粗糙度、气声、鼻音。

**核心创新：** (1) 操作化音色编辑：未提及属性记为<keep>，等级变化编成<brightness_up_1/2>等有序操作按固定顺序序列化，编辑器在codec空间产出可复用的编辑参考，使"改声"直接嵌入TTS流水线驱动新文本合成，区别于VoxEditor等仅输出编辑语音的语音编辑。(2) 段边界KV缓存重建：非末尾<EOS>触发以新指令与新文本、共享编辑参考及头部S=4、尾部K=5声学token组装fresh prefill，对声学上下文因果前向重算KV，刷新指令条件同时保留有界上下文，主干零额外训练。(3) 双语双基准解耦评测：TimbreEdit-Bench分别考核请求的编辑操作与未提及属性保持，IntraTTS-Bench联合考核局部依从、说话人一致与转换质量。

**训练策略：** 由5800个九属性音色profile经Qwen3-14B描述、Qwen3-TTS-VD合成中英语音构建1M有向编辑对，200个profile留出且不用于任一侧。SFT 50轮teacher-forced交叉熵（残差码本损失权重0.3、条件dropout 0.1），AdamW，lr 4e-6，有效batch 1024，weight decay 0.1，余弦衰减加10%预热；随后一轮wDPO：20K条件各采M=16候选，以WavLM说话人嵌入与目标的余弦相似定偏好对与权重，β=0.1、辅助SFT系数0.01，恒定lr 1e-6。

### 📊 实验结果
**数据集**：TimbreEdit-Bench（1955条源-目标编辑对、九类编辑、中英双语）、IntraTTS-Bench（997条含2-3段的句内投递指令请求）

**主要指标**：
- SIM-T（WavLM）：结构化/描叙式编辑下EDICT-Stage I为0.819/0.793，Qwen3-TTS-VD为0.701/0.676，Δ（目标减源）转正+0.199
- Category Acc：89.3%/91.7%，对比CosyVoice 2的57.7%/69.0%
- SegAcc/EmoAcc/Trans（Qwen3-TTS-VD主干）：82.30%/83.60%/82.00%，较TED-TTS提升+8.05/+9.58/+3.97pt；CosyVoice 2上Trans较Joint提升+12.26pt
- 联合控制：WavLM SIM-T 0.788、Trans 83.45%、UTMOS 3.795、SIM-I 0.917
- 主观评测：19人五点制，指令条件下Edit-MOS/S-MOS与Instr-MOS/Trans-MOS均最高，代价是CER由1.1%小幅升至1.8%

**是否开源**：代码暂未开源，音频演示见 https://danny-nus.github.io/EDICT-demopage/

### ⭐ 评分：7/10
评分理由：首个把参考相对音色编辑与句内分段指令控制统一进同一TTS流水线的框架，KV缓存重建免训练且在两个主干上验证有效，客观、主观与消融较完备。不足在于训练数据与基准全由Qwen3-TTS-VD自合成、偏好奖励又取自带评测的WavLM嵌入，存在循环偏置风险；属性保持仍落后Qwen3-TTS-VD，内容准确率有小幅退化，且代码未开放，复现受限。

---

## Monaural Continuous-Radius Regional Speech Extraction with Cross-Radius Consistency Learning

**arXiv ID**：arXiv:2610.11507 | **方向**：语音前端

**作者**：Biao Dong, Jie Chen, Jianwei Fang, Wei Xiao, Jiqing Han, Yongjun He

**机构**：哈尔滨工业大学计算学部、中国联合网络通信（北京）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11507 | **PDF**：https://arxiv.org/pdf/2610.11507.pdf | **代码**：https://dongb001.github.io/CRadius-RSE/ | **Demo**：https://dongb001.github.io/CRadius-RSE/

### 📌 简介
本文研究单通道条件下的连续半径区域语音抽取：以麦克风为圆心、查询半径为边界，保留半径内全部说话人语音并抑制半径外语音。现有单通道距离方法只能做固定阈值（DSS）或本地距离窗（QD-TSE）抽取，难以用单一模型对0到4米内任意半径做连续累积区域控制。作者将查询半径编码为连续标量并经FiLM注入TF-GridNet式时频网络，提出跨半径一致性学习（CRC），利用目标说话人集合的嵌套不变性稳定相邻半径预测。在dEchorate实测RIR上取得SI-SDR 29.25 dB、SI-SDRi 4.40 dB、衰减62.01 dB、RCE 0.46%，全面优于基线。

### 🔧 技术方案

**问题背景：** 传统目标说话人抽取依赖声纹注册，目标未知或动态变化时灵活性差；基于声源-麦克风距离的单通道方法DSS仅支持近/远固定阈值切换，QD-TSE只抽取局部距离窗内说话人，均无法直接建模以麦克风为中心的累积区域；已有区域抽取方案多依赖麦克风阵列，连续半径的单通道区域抽取此前欠探索。

**模型架构：** 采用轻量TF-GridNet骨架：对混合信号做STFT（FFT 192、hop 128），取幅度归一化的实部、虚部与对数幅度拼接并投影为C×T×F特征，堆叠6个TF块，每块沿频率轴和时间轴各做一次LN加BiLSTM加线性投影的残差建模，末端解码复数谱经iSTFT重建波形。查询半径在[0, Rmax=4]m归一化后经三层MLP编码器映射为特征表示，通过5个FiLM模块仅在相邻TF块之间注入特征仿射调制，推理时只需用户指定物理半径、无需估计声源距离。模型规模约0.66M参数（特征维度32、BiLSTM隐层64）。

**核心创新：** (1) 连续半径条件化抽取：把查询半径作为连续标量注入网络，单模型对训练范围内任意半径一次前向即得累积区域目标y_r对半径内说话人求和，空区域以全零为监督，区别于DSS的多模型固定阈值与QD-TSE需多次前向的区间求和。(2) 跨半径一致性学习CRC：利用半径间目标集合的嵌套关系S(r1)⊆S(r2)，对同一混合均匀采样Q=4个半径，仅对未跨越说话人边界的相邻半径对施加按公共目标RMS归一化的波形L1一致性损失，并以tau=1e-4剔除近静音对，避免过度平滑且显著抑制相邻半径输出的抖动。(3) 区域自适应损失：目标非空时用对数域归一化MSE重建损失，空目标时用alpha=100加权的预测幅值均值惩罚迫使输出静音，总损失为区域抽取损失加0.1倍一致性损失，使同一模型同时学全、部分与空三种区域状态。

**训练策略：** 用gpuRIR仿真1000间房间生成RIR（长宽[2,12]m、高[2,5]m、RT60在[0.1,1.0]s、声源距离[0.3,5.0]m），语音取自AISHELL-1、AISHELL-2、THCHS-30、VCTK，DNS噪声按0.5概率在SNR[0,15]dB叠加，16kHz采样、4.5s片段、训练为双人混合。Adam优化器，初始学习率6e-4，warmup 2000步，ReduceLROnPlateau调度，batch size为1，最多50轮，结果取3个随机种子平均。

### 📊 实验结果
**数据集**：测试为dEchorate实测RIR（检验真实房间泛化），训练/验证为gpuRIR仿真1000房间混合中文/英文语音（16kHz）；查询半径1/2/3/4m。

**主要指标**：
- 全目标SI-SDR：29.25 dB（DSS为22.03 dB、QD-TSE加区间求和为25.99 dB，分别提升7.22/3.26 dB）
- 部分目标SI-SDRi：4.40 dB（基线0.39/1.12 dB，提升4.01/3.28 dB）
- 空目标衰减：62.01 dB（基线56.12/54.10 dB，提升5.89/7.91 dB）
- 跨半径一致性误差RCE：0.46%（消融：离散编码1.04%，连续编码0.85%，连续加CRC 0.46%）
- 挑战条件：三人干净26.17 dB（RCE 1.12%）、2人5dB噪声RCE 3.17%、3人10dB SI-SDRi 3.10 dB仍可用

**是否开源**：论文声明Demo样本与代码发布于项目页 https://dongb001.github.io/CRadius-RSE/，正文未给出独立GitHub仓库直链。

### ⭐ 评分：7/10
评分理由：把单通道距离抽取从固定阈值与局部窗推进到连续半径累积区域查询，任务定义清晰且贴合可听设备、移动录音的实际需求；CRC利用目标集合嵌套这一物理不变量设计一致性约束，直觉良好，消融充分证明连续编码与CRC各自独立有效。0.66M模型单次前向即完成任意半径查询，效率优势明确。不足在于实验以两人、最长4.5s仿真混合为主，缺少主观听评，噪声下RCE退化至5倍左右，且一致性对的构造依赖训练期声源距离真值。

---

## SteerablePlex: Can We Steer Full-Duplex Models?

**arXiv ID**：arXiv:2610.12201 | **方向**：语音大模型

**作者**：Haolong Zheng, Maike Züfle, Dominik Macháček, Peter Polák, Xulin Fan, Xavier Sumba, Siyin Wang, Ondřej Klejch, Mark Hasegawa-Johnson

**机构**：University of Illinois Urbana-Champaign, Karlsruhe Institute of Technology, Charles University, Imperial College London, Tsinghua University, University of Edinburgh

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.12201 | **PDF**：https://arxiv.org/pdf/2610.12201.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工语音模型虽能边听边说，但随会话历史增长越来越难控制，作为用户模拟器会偏离既定场景、污染评测结论。本文提出 SimIF-Bench，量化考察模拟器的主题遵循、自然度、目标完成与目标顺序；并在 PersonaPlex 上设计特殊符指令注入接口与 GDPO 多奖励 RL 配方，训练出可在对话中接受运行时文本指令的 SteerablePlex，再连接异步 LLM 导演组成 Actor-Director 系统。200 个场景上，in-domain 变体在多目标完成与精确顺序上超过 GPT-Realtime，且在全双工轮次指标 10 项中有 6 项优于基座，证明全双工前端可被后端模型可靠转向。

### 🔧 技术方案

**问题背景：** 全双工模型持续生成、无明确的行为调整边界，仅靠系统提示的遵循度随对话变长而漂移；低延迟预算又限制模型规模与长程计划能力。Full-Duplex-Bench v2 用 GPT-Realtime 当考官，但考官不遵循脚本会削弱评估有效性，现有开源全双工模型在此类约束下差距更大。

**模型架构：** 基座 PersonaPlex 含用户音频、模型音频、模型文本三条同步流。指令由原有 tokenizer 编码后，以起止特殊符拼接进模型文本流，插入期间两路音频流填充静音符且会话时间不推进；异步文本 LLM 导演（Qwen3-27B）基于 Parakeet-TDT-0.6B-v2 流式 ASR 与模型文本流每 2s 更新目标状态，生成候选指令并给出 send/wait/none 动作，构成 Actor-Director 双层系统。

**核心创新：** (1) 运行时指令融合接口：复用预训练模型对文本流的语义理解，把带分隔符的文本段当作指令而非新控制模态；观察到基座零样本已能遵循短祈使句指令，为直接 RL 提供初始能力。(2) GDPO 训练配方：对目标完成、自然度、轮换等多维异质奖励在组内逐维 z 归一化后再加权合成并二次归一化，避免高方差奖励分量主导 GRPO 优势项，同时以 KL 项锚定 adapter-off 基座防止对话能力漂移。(3) 防作弊奖励设计：用规则化 VAD 事件定义重叠惩罚、抢话惩罚、应答延迟惩罚与 backchannel F1 四项轮换奖励，堵住"直接喊出目标内容"和"压着对方说话刷完成度"两类捷径。

**训练策略：** Fisher 语料经 Qwen3-32B 逐轮生成祈使指令，得 9,417 条 RL 样本、130.8 小时 rollout；按 Behavior-SD 管线从 200 个 FDB-v2 场景合成 2,000 条四目标重叠语音对话（84.1 小时立体声，200 条留出）。rollout 用 30s 双方录音上下文、插入指令后采样 20s 模型窗口、对方流原样回放。LoRA 秩 128/32、scale 2.0，lr 1e-5，G=8，音频/文本采样温度 0.8/0.7、top-k 250/25；task-independent 版 β 从 0.05 自适应至 KL 目标 0.3，in-domain 版固定 β=0.01。Silero VAD 阈值 0.5。

### 📊 实验结果
**数据集**：SimIF-Bench（200 个 Full-Duplex-Bench v2 分阶段场景，单通上限 120s，LLM 裁判三遍多数表决）与 Full-Duplex-Bench 轮换能力集

**主要指标**：
- 平滑轮换 TOR：1.000（PersonaPlex 为 0.983）
- 打断响应 TOR：1.000（PersonaPlex 为 0.935）
- 打断质量评分：4.790/5（PersonaPlex 为 4.684）
- 停顿误启动率：0.394（PersonaPlex 为 0.642，越低越好）
- 关键对比：相对 PersonaPlex 10 项指标提升 6 项；in-domain 变体在 200 场景的目标完成与四目标精确顺序均超 GPT-Realtime，且在未参与训练的 20 个场景上保持优势；KAME 持续转向则明显损害 backchannel 表现

**是否开源**：正文未给出代码或模型发布链接，暂无

### ⭐ 评分：7/10
评分理由：首次把"模拟器指令遵循"确立为可量化评测维度并给出 SimIF-Bench，填补了全双工可控性评测空白；特殊符注入 + GDPO 的配方工程细节扎实、六路奖励设计针对性强，实验同时验证了控制能力与轮次能力不互相牺牲。不足是 SimIF-Bench 主结果以图呈现、缺精确数值表，裁判依赖单一 LLM，且多指令长程协调仍不稳定，开源缺失也限制复现。

---

## Local Prototype Reconstruction for Text-Compatible Speech-to-LLM Bridge Pretraining

**arXiv ID**：arXiv:2610.11159 | **方向**：语音大模型

**作者**：Xinnian Zhao, Chia-Hua Wu, Pu Wang, Hugo Van Hamme

**机构**：KU Leuven电子工程系（ESAT）；中央研究院信息学研究所

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11159 | **PDF**：https://arxiv.org/pdf/2610.11159.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
语音转LLM系统中桥接冻结语音编码器与冻结LLM的轻量模块决定了接口几何，而NWP与句级对比预训练只优化全局语义对齐，未约束桥接token与LLM词嵌入流形的局部兼容性。本文提出固定、无头、无时间戳的接口兼容性诊断，并引入LPR（局部原型重构）：仅训练期要求每个转写对齐的桥接token能由冻结LLM输入嵌入的K个局部原型邻域凸组合重构。在CoVoST2多语种ASR/ST上，LPR将平均WER从7.75%降至7.22%、ST BLEU从39.09升至41.11，低资源增益最大，且诊断指标与下游迁移显著相关。

### 🔧 技术方案

**问题背景：** 当语音编码器与LLM同时冻结时，可训练桥接层定义speech-to-LLM接口几何，其是否可复用取决于预训练目标。NWP只优化语音条件下的生成；句级对比损失作用于池化话语表征，虽使全局检索接近满分（utterance R@1约0.999），token级余弦兼容性仍很低（0.06），词法兼容性欠约束且此前无法度量。

**模型架构：** 冻结Whisper-large-v3编码器接冻结Llama-3-8B-Instruct；桥接为窗口级Q-Former（2层Transformer，隐维4096、8头、窗口10，约177M可训练参数），骨干为句级InfoNCE对比损失（可学习温度、多LLM层平均）。LPR在其上增加：bias-free投影Wq/Wk把4096维降至512维计算转写条件软对齐得s_u；从预构建的高频token原型库检索以金标签E(y_u)为中心的K个冻结LLM嵌入近邻，softmax加权凸组合得重构r_u。

**核心创新：** (1) 提出固定、独立于训练头的诊断（话语R@1、MRE、金标签R@1/MRR、原型熵、对齐熵），可统一施加于NWP/对比/LPR检查点，证明全局检索饱和后仍无法区分桥接质量，而MRE可预测迁移。(2) LPR作为连续局部流形正则器：以余弦重构损失检验token是否落在词法流形邻域而非整个词表附近，保留语音连续性、不绑定离散tokenizer；K=1时退化为对金标签token的硬锚定，两种约束互补。(3) 纯训练期介入：转写、对齐头与原型检索仅在预训练使用，部署只保留编码器-桥接-LLM路径，推理行为与对比基线完全一致。

**训练策略：** 五语言联合预训练单一多语桥接（CoVoST2约431h），ASR/ST从同一起点分别微调；预训练最多6轮、batch 32、单张H100 80GB；微调自回归上限8万步、早停patience 3；AdamW峰值学习率3e-5、warmup 0.03；评测beam=3。LPR超参：d_a=512、K=16、tau_a=tau_p=0.1、lambda_a=lambda_r=0.5，lambda置零即回退对比基线。

### 📊 实验结果
**数据集**：CoVoST2（源自CommonVoice），De/Fr/Es/It/Pt转En五语种，训练约431h、dev 83h、test 88h，另有10%低资源子集约43h

**主要指标**：
- 全资源ASR平均WER：LPR(full) 7.22%，对比7.56%、NWP 7.67%、无预训练7.75%，相对无预训练降6.8%
- 全资源ST平均BLEU：LPR(full) 41.11，较对比基线+0.75、较无预训练+2.02
- 低资源适配：WER从10.28%降至9.08%；BLEU从35.24升至39.49（对比仅36.55，NWP跌至32.68）
- 诊断关联：LPR(full) MRE 0.645对比1.835；MRE与下游增益相关系数全资源r=-0.51(ASR)/-0.69(ST)，低资源r=-0.90/-0.88（n=25）

**是否开源**：暂无（论文正文未提供代码或Demo链接）

### ⭐ 评分：7/10
评分理由：将局部词法流形兼容性确立为可量化、可预测迁移的接口属性，诊断独立于LPR训练目标且能排序未优化该信号的NWP/对比检查点，方法学扎实；LPR零推理开销、即插即用，低资源与ST收益最明显。不足：整体增益幅度较小，仅单一基准与单一8B LLM组合，相关性分析样本少（n=25），且未开源复现。属增量但有清晰洞见的贡献。

---

## Selective Listening: Mechanism-Guided Control of Audio Influence in Large Audio-Language Models

**arXiv ID**：arXiv:2610.11196 | **方向**：语音大模型

**作者**：Yulin Sun, Kele Xu, Yong Dou

**机构**：College of Computer Science and Technology, National University of Defense Technology；State Key Laboratory of Complex & Critical Software Environment

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11196 | **PDF**：https://arxiv.org/pdf/2610.11196.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文研究大型音频语言模型（LALM）中任务无关音频改变文本推理决策的问题，指出聚合准确率会掩盖音频"修复"与"破坏"相互抵消的成对漂移。通过 clean/干扰成对评估与通路缩放干预，定位出对决策具有可操作影响的晚期音频通路作为控制点，提出 ICAP-Gate：按任务指令调制通路输出，明确音频需求时 g=1，否则乘模型特定衰减 λ_m。在 4 个 LALM、2 个推理基准、2 类干扰的 16 项全量评测中 IR 与 Flip 点估计均低于无门控；固定抑制导致 ASR WER 剧增，ICAP-Gate 则保持与无门控一致，并以单次生成获得接近 8 样本 Self-Consistency 的稳定性。

### 🔧 技术方案

**问题背景：** 无关音频可改变文本推理决策而聚合准确率几乎不变（cw/wc 转移相互抵消）；已有缓解仅作用于输入（prompting）或输出聚合（Self-Consistency），未触及内部机制，且 8 样本解码带来 7–9 倍延迟，模型内部缺少"何时让音频参与计算"的可干预接口。

**模型架构：** 免训练的推理时框架。对深度 ℓ_m 处的晚期音频通路模块输出 z，施加 ẑ=g(I)·z：任务指令含明确音频需求时 g=1，否则 g=λ_m。控制点按架构离线校准：Qwen2.5-Omni-7B/3B 为 audio_tower.layers.25（相对深度 0.81=26/32，λ=0.25），Phi-4-MM 为 audio_embed.encoder.encoders.23（24/24，λ=0.10），Voxtral-Mini-3B 为 audio_tower.layers.30（0.97=31/32，λ=0.25）。线上推理仅需一次指令路由决策与一次临时通路缩放，每查询单次生成。

**核心创新：** (1) 成对漂移度量框架：定义 Influence Rate、Answer Flip、NetC2W、NetAnswer，并给出与聚合准确率 ΔAcc 的精确抵消关系，暴露"个体预测大量变动而总分稳定"的隐藏失效模式。(2) 机制性因果定位：以通路缩放干预（0≤α≤1）证明晚期通路携带可操作影响——C2W 样本与稳定样本在晚期位点激活 RMS 相近但 clean gold-answer margin 差异显著，说明控制点由决策相关性而非激活幅度决定，且同类可操作位点在三种异构音频架构中重复出现。(3) 选择性模态影响控制原则：模态可得不等于模态影响计算，指令条件化门控对显式音频请求保留通路，无需 clean 参考路径或辅助相关性模型，规则透明可审计。

**训练策略：** 方法免训练、无损失函数：(ℓ_m,λ_m) 由离线干预分析校准得到。干扰构造：FSD 为每题配对一条 FSD50K 真实环境声；SIB 用 LibriSpeech dev-clean 语音独立配对（MMLU 共 14,042 对、2,694 条源语音、40 说话人、平均复用 5.212 次）；三条推理路径共享文本、配对音频与模型解码配置，bfloat16 推理，统计用 20,000 次配对 bootstrap（seed 0）的 95% CI 确认。

### 📊 实验结果
**数据集**：ARC-Challenge 与 MMLU 全量测试集（推理）；FSD50K 环境声与 LibriSpeech dev-clean 自然语音（干扰）；每模型 400 条 dev-clean 语音（ASR 副作用）

**主要指标**：
- Influence Rate：Qwen2.5-Omni-7B MMLU-FSD 为 11.80%→9.16%，Answer Flip 16.06%→12.60%，而 Accuracy 67.58%→67.55% 几乎不变
- 16 项全量评测 IR/Flip 点估计均低于无门控，ΔIR 最大 4.01pt（Qwen-3B ARC-FSD：11.77%→7.76%）
- 对比 mitigation prompting：MMLU-SIB 上 IR 低 8.87pt、Flip 低 11.76pt（配对 95% CI 不含零）；8 样本 Self-Consistency 漂移略优（ARC-SIB ΔIR −2.99pt）但 ICAP-Gate 延迟仅 0.894–1.057× 无门控，SC 为 7.03–9.22×
- ASR WER：固定抑制剧增（Qwen-7B 17.74%→98.60%、Voxtral 16.72%→61.05%）；ICAP-Gate 与无门控完全一致（17.74/60.82/2.45/16.72%）
- 路由审计（n=240）：显式音频请求 40/40 保留，问题文本难负样本 0/40 误触发（整句匹配则 40/40 误判）

**是否开源**：论文与 HTML 全文未提供代码/Demo 链接，暂无开源

### ⭐ 评分：7/10
评分理由：首次将无关音频鲁棒性转化为"机制定位+条件门控"的模型内干预，从成对漂移度量、因果定位到门控验证的证据链完整，覆盖 4 模型、2 类干扰与全量数据的显著性检验也较扎实，单次生成即接近 SC 稳定性且零 ASR 损失，工程价值明确。不足：漂移降幅多为 2–4 个百分点，Phi-4-MM 上收益尤小；门控依赖指令显式线索，隐式音频需求的泛化存疑；因果定位主要在 Qwen 完成，代码未开源。

---

## Toward Accurate Speaker Inventories for Online Speaker Diarization

**arXiv ID**：2610.11278 | **方向**：语音前端

**作者**：Youngki Kwon, Hee-Soo Heo, Minjae Lee, Bong-Jin Lee

**机构**：NAVER Cloud Corporation, South Korea

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11278 | **PDF**：https://arxiv.org/pdf/2610.11278.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
在线说话人分离系统实时维护一份可被应用直接读取的说话人清单，现有方法要么预先固定清单容量（超出者被合并），要么仅凭距离无界增长清单（噪声与话轮边界造成分裂），而这两种失败都无法从DER看出：VoxSRC-23上固定容量系统少报44-46%说话人，DER最低的无界追踪器多报63%。本文在DC-OST嵌入追踪器上只改动注册触发机制：候选说话人池要求新说话人积攒K个相互兼容的嵌入后才注册，提交门控标签分配在候选未决时挂起输出、不确认不露出。九个数据集上宏平均说话人数错误从225%降至21%，宏DER从17.59%降至15.95%，全部输出平均仅增加0.109秒延迟。

### 🔧 技术方案

**问题背景：** 在线系统各自以attractor、speaker cache、speaker-tracing buffer等名义维护说话人清单，增长规则预先固定且标签一旦发出不可撤销：固定容量在真实人数超过上限时把说话人合并，无界注册则让每一个足够远的嵌入都成为新说话人，单次观测即可播种幽灵说话人。DER按说话人所占时长加权，对人数及其增减方向完全沉默，掩盖了清单层面的系统性错误。

**模型架构：** 流式管线由FireRedVAD检测器（0.6M参数因果DFSMN，零前视）检测语音，ReDimNet2检查点b6-vb2+vox2_v0-lm.pt在1.5秒窗上每0.5秒产生一个嵌入，基础延迟0.5秒。追踪器维护三部分组成：已提交质心注册表、按候选分开的说话人池、按步序释放的挂起队列；路由沿用DC-OST自适应阈值τ_t=min(τ_base+λN_t, τ_max)。

**核心创新：** (1)证据门控注册：将单一共享缓冲改为彼此隔离的候选池，新嵌入与各候选成员两两余弦距离取中位数，在τ_pool=0.45内并入最近候选，否则新建候选；候选积满K=5个成员才以归一化均值质心注册，单元素候选静默超过30秒即丢弃，同时消除了交替未知说话人的合并与单点外点引发的分裂。(2)提交门控标签分配：未决输出以（回退标签，候选临时身份）双重身份入队，候选注册即以临时身份释放，等待超过延迟预算L_prov=2.0秒才以回退最近已注册说话人释放，无任何说话人先于确认出现在输出中，前视只花在8.6%的输出上。(3)计数错误评测轴：提出|e|=Σ|N_sys−N_ref|/ΣN_ref（双向均计），把清单准确性与DER并列为第一级指标，并给出队头阻塞等延迟构成分析。

**训练策略：** 方法为免训练的推理决策规则；K=5、τ_pool=0.45、L_prov=2.0s在DIHARD III与VoxConverse开发集上按DER与|e|折中调定，T_e=30s未调（0.45/0.005/0.8沿用DC-OST超参），无任何评测集参与调参；前端完全复用公开预训练权重（ReDimNet2训练于VoxBlink2+VoxCeleb2，均不在九个评测集内）。

### 📊 实验结果
**数据集**：九个公开数据集共1,907条录音（DIHARD I-III、VoxConverse、VoxSRC 2021-2023、AMI、AliMeeting，单条1-28人，合计1,473,619个输出）；与现有系统对比用VoxSRC-23与DIHARD III评测集。

**主要指标**：
- 宏说话人数错误（统一0.15s collar）：基线规则225.0%降至全系统20.7%；宏DER 17.59%降至15.95%（SC 5.95%至4.31%）
- VoxSRC-23：DER 6.76%、|e| 16.0%，对比系统两轴同时最低（基线规则DER 7.40%但人数超报63.1%；Sortformer/LS-EEND人数缺报46.2%/43.7%）
- 关键对比：DIHARD III上DER 24.31%落后Streaming Sortformer 4.6%p（19.76%）、S2SND-M 7.2%p（17.12%），|e| 23.2%落后LS-EEND 8.7%p
- 延迟：平均全体输出额外0.109 s，被挂起的8.6%平均1.27 s，最大4.16 s（总延迟0.50 s+δ）
- 消融：池使SC在DIHARD III降3.55%p、AMI降2.47%p；延迟使Vox系SC再降1.17-1.53%p；唯一例外AliMeeting因重叠混入嵌入DER持平（34.60→34.76%）但|e|从440%降至13%

**是否开源**：论文正文未提供本方法代码链接，暂无；其前端与对比系统均基于公开实现（FireRedVAD、ReDimNet2、DIART、Streaming Sortformer、LS-EEND）。

### ⭐ 评分：7/10
评分理由：把DER长期掩盖的说话人计数问题显式化并提出可复核的|e|指标，问题定义有原创性与实用价值；两道门不改管线、纯决策规则即可部署，延迟记账精确到输出的8.6%与1.27秒，工程可信。九数据集双轴对照与敏感性分析充分。不足是相对DC-OST仅增量改动、DER绝对收益有限，高重叠会议场景仍是明显短板，且未发布代码影响复现。

---

## SAVU-BENCH: A Real-World Benchmark for Spatial Audio-Visual Understanding

**arXiv ID**：arXiv:2610.10624 | **方向**：语音大模型

**作者**：Yu Chen, Ruihang Liu, Yangguang Xu, Xinyue Jiang, Mohammed Bennamoun, Farid Boussaid, Xinyuan Qian, Qiuhong Ke

**机构**：西澳大利亚大学、北京科技大学、蒙纳士大学

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.10624 | **PDF**：https://arxiv.org/pdf/2610.10624.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出完全基于真实录制的空间视听理解基准SAVU-Bench，解决现有评测偏仿真场景、能力孤立且缺乏失败机理诊断的问题。基准由六个真实空间视听数据源经四阶段human-LLM标注管线构建，含1,066道多选题，覆盖感知、对齐、推理三层级七类任务；SAVU-Diag将推理题分解为同场景的前置grounding/alignment子任务（611题、81场景）。12个AV-LLM评测显示音频空间定位是核心瓶颈：Audio Grounding最高仅55.6，最佳空间推理45.8只超随机基线3.6个百分点，人类达85.0；训练免调的SAVU-EA注入显式空间线索可将Audio Grounding提升30.7个百分点，但推理差距仍在。

### 🔧 技术方案

**问题背景：** 现有空间视听基准大量依赖仿真环境、只孤立评测定位或匹配单项能力，任务级准确率无法区分推理错误源于感知、跨模态对齐还是关系组合，难以衡量真实录制条件下的泛化水平。

**模型架构：** 本文是评测体系而非新模型。视觉侧从全景录制提取受限FoV视图，FOA一阶球声音频按ViSAGe方式对齐到视觉参考系；任务体系分三层七任务：Perception（Audio/Visual Grounding，含粗定位、相对位置、空间动态）、Alignment（语义对齐、空间对齐、A2V/V2A联合匹配，候选集含语义负例与保持类别兼容的空间负例）、Reasoning（相对方向、空间顺序、自我中心转换推理）。每个推理实例围绕静默视觉锚点、画面内声源与画面外声源构造双模态互补线索。

**核心创新：** (1) 真实场景系统化基准：1,066题横跨MRSAudio、STARSS23、YT360、D-SAV360、MULTIVOX、QoEVAVE六源，平均片段6.12秒，统一评测感知-对齐-推理能力梯度。(2) 场景联动诊断SAVU-Diag：将推理题的前置事实与跨模态对应转成共享同一录音、时间窗与参考系的独立子任务，分离证据获取失败与关系组合失败两类模式。(3) 训练免调证据增强基线SAVU-EA：用OpenVocabularySELD从FOA提取声事件与空间轨迹、Qwen3.5-Omni-Plus提取视觉对象与运动，作为显式空间线索注入Gemini-3.6-Flash，构成知觉瓶颈的干预实验。

**构建与评测策略（论文无模型训练）：** 四阶段管线：场景筛选与结构化（BEATs声事件标签、Grounded SAM 2视觉目标与轨迹、缺空间标注时用OpenVocabularySELD估计方向）、GPT-5.4生成题目候选、人工标注并手工构造推理链、三位领域专家独立作答仅保留至少两人答对的题目；选项循环排列计算平均准确率AA去除位置敏感；除保留4通道FOA的Spatial-Omni外模型均输入单声道downmix，人类经HRTF听双耳音频，人类评测每任务随机抽30题。

### 📊 实验结果
**数据集**：SAVU-Bench（1,066题、7任务）与SAVU-Diag（611诊断题、81场景、平均每场景7.54题），来自六个真实录制源。

**主要指标**：
- Audio Grounding：最佳Spatial-Omni SO-7B为55.6（随机50.0），人类89.33
- Visual Grounding：DOTS-3-Note-Preview达95.4
- Joint A2V与Joint V2A：最佳35.6与42.8，A2V仅超随机33.3约2.3个百分点
- Spatial Reasoning：Gemini-2.5-Pro与SO-7B并列最高45.8，超随机基线42.2仅3.6个百分点，人类85.00
- SAVU-Diag诊断：OmniVideo-7B仅有61.4%推理错误属grounding-only；SO-7B为grounding-only 17.9%、alignment-only 23.1%、双失败46.2%
- SAVU-EA增益：Audio Grounding +30.7、Joint A2V +19.1、Joint V2A +21.7、Spatial Reasoning +14个百分点

**是否开源**：暂未开源，论文声明接收后计划公开基准、评测代码与构建脚本

### ⭐ 评分：7/10
评分理由：以真实录制数据统一三层能力评测，并用场景联动诊断定量分离此前混淆的两类推理失败模式，12个模型对比加人类基线充分；评测协议（循环排列、随机基线计算）严谨。局限在于纯基准工作、SAVU-EA依赖外部SELD与视觉模型的正确性存在级联误差，且未给出消除推理差距的端到端方案；千题规模适中，对空间音频大模型研究方向指引价值高。

---

## EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams

**arXiv ID**：arXiv:2610.12248 | **方向**：语音大模型

**作者**：Heeseung Kim

**机构**：Department of AI, University of Seoul

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.12248 | **PDF**：https://arxiv.org/pdf/2610.12248.pdf | **代码**：暂无 | **Demo**：https://egocentricvoice.github.io/

### 📌 简介
面向可穿戴AR场景中的持续第一视角视频/音频流，本文提出 proactive egocentric spoken assistance：助手需自主决定何时开口、说什么，而现有语音系统多为反应式，主动视频助手仅输出文本。作者从HoloAssist真实导师录音出发，经音频分离与语音重合成构建流式语音监督数据，在MiniCPM-o 4.5上做SFT并用DPO优化干预时机。EgoVoice-DPO将onset F1提升至0.324（零样本骨干0.113、ProAssist 0.195），end-vs-action +1.75s接近人类导师+1.69s，并在人工偏好对比中显著胜出基线。

### 🔧 技术方案

**问题背景：** 语音交互系统依赖VAD/轮次触发，用户在体力任务中几乎不说话则模型极少介入；文本主动助手的指令时间戳与语音播放时长错位，且无法涵盖真实环境声。尚无单一模型联合学习连续egocentric流上的干预时机与语音内容。

**模型架构：** 以9B流式全双工Omni模型MiniCPM-o 4.5为骨干，每1秒chunk输入1帧视频与混合音频（背景声+用户语音），输出Listen或Speak决策；Speak后经LLM生成BPE文本，0.3B语音token解码器转为S3 speech token，再由流式flow-matching解码器合成波形。系统prompt含任务名与逐步recipe。

**核心创新：** (1) 语音数据工程管线：SAM-Audio以语音区间为prompt分离去除变调人声、仅保留背景残差并用Silero VAD校验；GPT-5-mini规范文本并剔除9.0%无关 remarks，IndexTTS2以MLS每会话参考音色分别重合成用户/导师语音，多候选中仅保留Qwen3-ASR转写完全一致且时长不超原文者，使干预时刻与真实行为天然对齐。(2) 逐秒chunk的Listen/Speak流式监督：每条导师话语构造中心对齐的60秒窗口（带时间抖动），每epoch 13,676窗口，文本与语音token联合监督；(3) 以指标为奖励的时机偏好优化：同上下文采样N=10候选，按onset F1择优（最小差0.10）构造5,335对，采用length-normalized DPO直接校准"何时说话"。

**训练策略：** LoRA r=32/α=64/dropout 0.05，冻结视觉与音频编码器；SFT损失L_LM+0.1·L_S3并做主干-解码头梯度detach，lr 2e-4、batch 32、5 epochs（2,140步）；DPO仅调LLM、语音解码器冻结，β=0.1、lr 5e-6、batch 16、1 epoch（334步）；cosine+5% warmup、weight decay 0.01、梯度裁剪1.0、bf16+FlashAttention-2。

### 📊 实验结果
**数据集**：HoloAssist加工版（原1,673会话124.8h→1,249训练91.7h/170评测12.9h），主报text-asr通道

**主要指标**：
- Onset F1：DPO 0.324、SFT 0.274（ProAssist 0.195、零样本MiniCPM-o 0.113、Gemini Live 0.022）
- Content cosine：SFT 0.684（ProAssist 0.594，+0.090）
- end-vs-action：DPO +1.75s/SFT +1.57s，人类导师+1.69s；ASR/TTS级联为-0.44s
- LLM Judge Overall：SFT 2.23、DPO 2.18 vs 零样本1.41
- 人工偏好：SFT胜45.6%/负31.3%（p=0.01），DPO胜45.3%/负33.0%（p=0.02）
- 关键对比：相对零样本骨干，SFT的F1提升+0.161（p<1e-12）

**是否开源**：项目页提供数据音频样本与对比demo；作者声明将以CDLAv2兼容方式释放数据集、代码与模型，预印本阶段代码仓库暂无。

### ⭐ 评分：7/10
评分理由：首次把"何时说+说什么"合并为可训练的持续第一视角语音助手任务，数据管线严谨、评测协议（双通道+end-vs-action分解+显著性检验）完整，SFT/DPO互补分析与消融充分。局限在于单一装配域、recall仅0.285、录制式评测非交互式，骨干复读/语言切换伪影残留，且正式发布尚未落地代码，实用价值有待开源验证。

---

## Detection-Guided Adaptive Purification with Diffusion Models for Robust Audio Deepfake Detection

**arXiv ID**：arXiv:2610.10752 | **方向**：语音大模型

**作者**：Muhammed Salih Kayhan, Qiben Yan

**机构**：Michigan State University

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.10752 | **PDF**：https://arxiv.org/pdf/2610.10752.pdf | **代码**：https://github.com/msalih98/DGAP | **Demo**：暂无

### 📌 简介
音频深伪检测器易被微量对抗扰动欺骗为真人语音。本文提出 DGAP，一种不修改、不重训检测器的扩散净化防御：低噪声级轻度净化使对抗样本的 bonafide 分数偏移远大于良性样本，以该分数差为无参考对抗标志，仅对被标记输入施加强净化，其余原样通过。在 ASVspoof 2019 LA 上对 AASIST、RawGAT-ST、Res-TSSDNet 与 PGD l_inf/l_2、C&W 评测，综合目标 y 为 5.61/5.18/21.65%，优于最强扩散基线 DiffPure 的 12.56/11.26/29.69%，EER_clean 几乎无损，防御感知攻击下仍最优。

### 🔧 技术方案

**问题背景：** 对抗训练依赖攻击感知重训，加噪类防御引入额外失真；现有扩散净化（DiffPure、AudioPure、WavePurifier）对所有输入固定同一强度，过强抹除微弱合成伪影，过弱残留扰动，难以兼顾去扰动、保伪影与保良性。

**模型架构：** probe、gate、purify 三段流水线。净化骨干为微调后的 OpenAI guided-diffusion（Dhariwal 256x256 权重，VP-SDE 线性调度，N=1000）：波形经 512 点/hop 128/Hann 窗 STFT 取幅度谱，dB 归一后切方形窗口独立净化，保留相位 iSTFT 重建后送入冻结检测器。

**核心创新：** (1) 检测器引导的逐输入强度自适应：以 t_g 级探针净化后的 bonafide 分数差为对抗指标，无需干净参考、攻击类型与预算知识。(2) 统计门控：阈值取良性校准集分数差的均值加 gamma 倍标准差，仅超标输入进入强 t_p 净化；并由前向加噪下对抗与干净表示差异随 alpha_bar 单调收缩论证轻探针可放大两类响应差。(3) t_g 与 t_p 解耦，(t_g,t_p,gamma) 在开发集按 y=EER_clean+lambda·EER_adv 搜索，每检测器一套攻击无关配置。

**训练策略：** 净化器在 LA 训练集提取的 55,001 个频谱窗口上微调，窗口兼取 bonafide 与 spoof 两类；16 kHz，dB 偏移 -20、归一 [-120,25] 至 [0,1]；网格 t=20-300 共 15 级、gamma 0.5-3.0（步长 0.01）、lambda=1；攻击 PGD l_inf eps=0.005、l_2 eps=1.0（迭代 10-100），C&W k=10、c=1.0、200 步；正文未披露优化器与学习率。

### 📊 实验结果
**数据集**：ASVspoof 2019 LA（16 kHz；train/dev/eval 25,380/24,844/71,237 条；测试 600 条 spoof 配等量 bonafide）

**主要指标**：
- 综合 y（%）：5.61/5.18/21.65，DiffPure 12.56/11.26/29.69，无防御 53.78/23.99/50.85
- EER_clean（%）：1.83/1.67/2.83，接近无防御 1.17/1.25/2.17
- EER_adv（%）：PGD l_inf 4.25/4.33/19.37；C&W 2.08/1.61/21.40（无防御 46.5/20.7/38.5）
- 消融（%）：AASIST 同 t_p 下由均匀净化 24.40 降为有门控 9.30
- 自适应 BPDA+EOT：RawGAT-ST y=14.17 仍最优，仅 33.3/34.2% 对抗被门控
- 耗时：良性约 8-15 s，对抗约 31-52 s（RTX A6000）

**是否开源**：代码已开源 @ https://github.com/msalih98/DGAP

### ⭐ 评分：7/10
评分理由：以检测器自身响应驱动净化强度，无需参考与重训即可插拔，思路新颖并有单调性论证；3 检测器 x 3 攻击 x 9 基线加防御感知攻击，评测充分、指标全面领先。局限是 1000 步扩散令单条耗时达秒级至数十秒，离实时部署较远，且仅在 ASVspoof 2019 验证，跨数据集泛化与效率待补。

---

## Disentangling Linguistic and Paralinguistic Information with Routed Sparse Autoencoders

**arXiv ID**：arXiv:2610.10865 | **方向**：语音大模型

**作者**：Beimnet Bekele Guta, Xiaoyu Yang, Guangzhi Sun, Philip C. Woodland

**机构**：University of Cambridge, Department of Engineering

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.10865 | **PDF**：https://arxiv.org/pdf/2610.10865.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
自监督语音编码器（WavLM/SPEAR）在同一表征空间中混合语言与副语言信息，难以对单一因子做选择性读取或移除。本文在冻结编码器上叠加TopK稀疏自编码器，通过单元级路由、路由内任务监督与跨因子对抗训练，将稀疏码划分为语言与副语言两条路由。独立探针显示：SPEAR固定路由下语言路由音素错误率PER为10.02%而说话人识别准确率仅6.2%，副语言路由SID达99.8%而PER升至99.60%；在LibriSpeech习得的路由组织可迁移至MSP-Podcast，路由交换实验实现99.57%的音素保留与98.00%的供体说话人转移，证明路由具备功能级双重分离。

### 🔧 技术方案

**问题背景：** SSL语音表征中音素、说话人、情感、韵律纠缠于同一激活，扰动不变性、信息瓶颈与对抗训练等方法只能整体地削弱某一因子；已有语音/音频SAE研究侧重分析自发发现的特征，稀疏性本身并不保证学到的单元对应事先选定的因子分解。

**模型架构：** 冻结语音编码器输出帧级D维表征x_t（SPEAR XLarge与WavLM Large，逐层无参数LayerNorm后均匀跨层平均）；线性SAE投影到K>D过完备字典并取TopK后解码重建。激活单元经互补掩码（m_L[u]+m_P[u]=1）分为语言路由z_L与副语言路由z_P，分别接入PR（CTC）任务头与SID/情感/韵律任务头，反方向由各对抗头经梯度反转层作用。

**核心创新：** (1) 首次把SAE从特征解释工具转为有监督因子分离工具：单元级路由掩码将TopK单元划入两条路由，掩码互补保证z_t=z_L+z_P、整体稀疏码仍可完整重建编码器表征。(2) 可学习路由用直通Gumbel-Softmax硬分配加路由熵惩罚促使决断性分配，并提出固定路由与在第4000步冻结分配、按均激活率转为各路线额（quota-freeze）的两种组织策略。(3) 跨因子对抗：phone对抗作用于z_P、speaker/emotion/prosody对抗作用于z_L，配合任务监督同时实现目标因子保留与跨因子抑制，消融证明二者互补。

**训练策略：** 总目标为λ_recon·L_recon + λ_AuxK·L_AuxK + L_task + L_adv（可学习路由期加路由熵项），AuxK以64预算、权重1/32复活死单元。字典宽K=5120、激活预算k=256；固定路由用连续K_L/K_P=4096/1024与激活预算k_L/k_P=240/16；quota-freeze在step 4000由20个采样batch的均激活率设定冻结后预算；SPEAR重建/固定模型训12000步，WavLM 12000步、quota-freeze 16000步；论文未披露学习率、优化器与batch size。

### 📊 实验结果
**数据集**：LibriSpeech train-clean-100（251说话人闭合集SID，74符号音素表，PR用dev-clean/test-clean）；MSP-Podcast 51,017子集（700说话人，41,067/4,975/4,975划分，SID随机水平0.143%）

**主要指标**：
- 语言路由（SPEAR固定）：PER 10.02%、SID准确率6.2%；副语言路由：SID 99.8%、PER 99.60%
- quota-freeze语言路由：PER 8.94%、SID 0.6%（对比仅重建SAE的SID 99.6%，跨因子抑制幅度约99个百分点）
- 零重训跨库迁移：固定路由z_L/z_P PER 43.92%/99.72%、SID 12.82%/82.71%，路由组织在MSP-Podcast保持
- 路由交换：P-swap后音素保留99.57%、供体说话人匹配98.00%；L-swap后受体说话人保留96.00%、供体音素保留99.10%
- 对比最强基线Eta-WavLM：其h_η PER仅7.25%但SID仍有95.41%，选择性抑制远弱于路由SAE

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：把SAE引入语音解耦并配齐"路由+任务监督+双向对抗"的归纳偏置，在两个冻结编码器、两个语料、独立探针与受控路由交换下均得到一致的双重分离证据，实验设计严谨可信。不足是语言路由PER较仅重建基线劣化约3-4个百分点、训练超参披露不全、情感/韵律仅单库验证，且未开源限制了可复现性与即插即用价值。

---

## How Much Audio Is Left In An Embedding? An Inversion Audit Of Audio Encoders

**arXiv ID**：arXiv:2610.12250 | **方向**：语音大模型

**作者**：Marios Glytsos, Brian McFee

**机构**：Music and Audio Research Laboratory, New York University

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.12250 | **PDF**：https://arxiv.org/pdf/2610.12250.pdf | **代码**：https://mariosgly.github.io/research/audio-embedding-inversion/ | **Demo**：https://mariosgly.github.io/research/audio-embedding-inversion/

### 📌 简介
预训练编码器常被复用于未知下游任务，甚至作为音频替代品在隐私与版权场景分发，其嵌入残留多少源信息缺乏标准度量。本文提出统一逆转向审计：以同一Stable Audio Open潜空间扩散解码器为探针，分别用VGGish、CLAP、ConvNeXt、EnCodec四族冻结表征微调配对源重建，在Million Song Dataset音乐上评测。EnCodec在同一探针下配对源检索R@1达0.894（其原生解码器为1.000），VGGish仅0.004；同编码器内更细粒度接口一致提升可恢复性，表明面向任务的压缩嵌入仍保留可测量的源特异性与高层音乐内容。

### 🔧 技术方案

**问题背景：** 以嵌入替代音频分发时，下游可用性无法揭示保留了多少源细节；逐编码器自适应攻击使跨家族比较混淆，且难以分离嵌入信息缺失与探针能力限制。

**模型架构：** 探针初始化自Stable Audio Open 2.0：固定VAE将5秒44.1kHz立体声压为64通道潜变量（降采样比2048），去噪主干为24层/宽1536/24头扩散Transformer，交叉注意力读取768维token。原T5接口替换为各冻结表征经线性层投影至768维：VGGish 128x(6-7)、CLAP 512x1或512x5、ConvNeXt 768或5376x(16-17)、EnCodec z_q 128x750；除接口外其余条件完全一致。

**核心创新：** (1) 统一生成式探针：所有条件共享同一预训练扩散先验、按接口分别微调，以标准化审计替代最坏情况攻击，使可重建性跨家族可比；新投影近零初始化，缓解条件接口替换的训练扰动。(2) 时间局部注意力先验：交叉注意力分数加按头可学的时间差分桶偏置，并以|t-s|<=0.2硬掩码使潜变量对齐时间对应区段，亦助益EnCodec等稠密接口的算力受限微调。(3) 接口级消融与双指标校准：同编码器构造CLAP 5s/1s、ConvNeXt池化/展平变体以隔离时频压缩本身的影响；MR-STFT距离与SAO-VAE余弦相似度并用，后者以200k随机源-源对校准，分离波形误差与解码器表征局限。

**训练策略：** v-prediction潜空间扩散损失；因目标是重建配对源，条件dropout为0、guidance权重w=1；推理用150步确定性DDIM（eta=0）。MSD按artist不相交划分为219,810/26,190/26,367条、覆盖15个流派；先用Demucs去人声以匹配SAO器乐先验域。4 GPU、单卡batch size 32，每个接口微调约36小时。

### 📊 实验结果
**数据集**：Million Song Dataset（含Tagtraum流派标注）5秒44.1kHz立体声器乐片段，测试26,367条。

**主要指标**：
- MR-STFT距离（越低越好）：EnCodec 0.13、CLAP 1s 0.19、VGGish 0.21，原生EnCodec 0.10为参照
- SAO-VAE余弦相似度：EnCodec 0.47，ConvNeXt展平 0.24，VGGish 0.15，原生EnCodec 0.89
- 配对源检索R@1/R@10（在26,367个测试片段中）：EnCodec 0.894/0.913，ConvNeXt展平0.352/0.539（池化0.094/0.201），CLAP 1s 0.024/0.091（5s 0.006/0.034），VGGish 0.004/0.021
- MusicNN标签重合度：EnCodec 0.847，VGGish 0.733
- 关键对比：EnCodec较VGGish的R@1高0.890；同编码器ConvNeXt展平较池化提升R@1约0.258

**是否开源**：代码与试听样例经上述项目页面发布，论文未提供独立GitHub仓库。

### ⭐ 评分：6/10
评分理由：将逆转重构为受控的跨家族可重建性审计，接口消融与双指标校准的方法学干净，对嵌入代音频流通的隐私版权风险有直接警示价值。局限在仅覆盖音乐域与单一数据集，绝对重建保真度有限，只能给出保留信息下界而非泄漏量，且结论受生成先验域限制。属增量但扎实、可复用的审计工作。

---

## Controlled Acquisition and Abstention in Three-Channel Score Conflicts

**arXiv ID**：arXiv:2610.10808 | **方向**：语音大模型

**作者**：Mengzhe Geng

**机构**：National Research Council Canada

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.10808 | **PDF**：https://arxiv.org/pdf/2610.10808.pdf | **代码**：https://github.com/MENGZHEGENG/audio-video-text-conflicts | **Demo**：暂无

### 📌 简介
当音频、视频、文本通道冲突时，仅凭准确率无法回答"是否值得获取第三个信源、何时应弃权"。本文构建受控三符号分数基准：策略先观察两路分数，可付费0.10请求第三路，也可付费0.20弃权，且弃权仅对指定 ambiguity 机制判对。在部分留出分片上，固定阈值策略以83个随机种子达到0.789±0.006定向决策准确率与0.481±0.014效用，优于三分数 majority 基线（0.626/0.252）；但该优势强依赖奖励口径与信息预算，学习式查询选择器整体不敌简单阈值与不确定性排序。

### 🔧 技术方案

**问题背景：** 现有融合模型始终输出标签，隐藏了缺失源是否值得获取、观测能否支撑安全答案两个决策；冲突基准与可信度融合聚焦回答生成，缺少对获取+弃权的显式成本化评测。

**模型架构：** ConflictBench 生成器由潜二值事件产生三通道分数 x_m=(2y-1)s+ε（s=1，σ=0.22），叠加 invert/swap/dropout/mixed/burst/ambiguity 机制。基线含 Majority/Median/Weighted、MLP（6→32→16→3）、Gated 与学习式获取打分器（4→24→12→1，特权全分数目标）；时序用宽度96、深度4的 fusion/gated 网络处理 [3,T] 轨迹。阈值策略：两符号冲突或任一分量幅值<τ=0.35 即请求第三源；获取后仅当≥2个分数幅值≥τ且同号才回答，否则弃权。

**核心创新：** (1) 把获取与终局动作解耦的匹配控制：τ>0 时 always-query 与阈值策略逐样本终局一致，效用差恰为省下的请求费 0.10×(1-0.6344)=0.03656。(2) 机制特异奖励：弃权只对 ambiguity 判对、对 mixed 照常收费，并用 mixed-reward 与弃权全错变体证明效用排序是奖励掩码下的适应结果。(3) 匹配预算选择器实验：统一 sum-rule 终止，比较 train-only ridge 价值选择器（α=1，7维特征）、pair 不确定性、匹配随机与不可部署 oracle，在 10%–63.7% 预算下量化请求前选择价值。

**训练策略：** Adam 训练90轮、batch size 256、学习率0.0015、梯度裁剪范数5；分类用交叉熵、查询打分器用二元交叉熵；6000条训练样本，打分器阈值在校准分片上从{0.1,…,0.9}按效用选定；时序模型 AdamW、800优化步；主研究83种子、10000次配对bootstrap。

### 📊 实验结果
**数据集**：合成三分数生成器（6000训练/4000评测；时序含207个设置-种子运行）；媒体诊断含 CMU-MOSEI 描述符、1244段演员留出 CREMA-D、AMI 244例。

**主要指标**：
- 定向决策准确率（部分留出）：阈值 0.789±0.006、学习式获取 0.746±0.010、多数表决 0.626±0.008
- 效用：阈值 0.481±0.014 对比多数表决 0.252±0.016（差 +0.230 [0.226, 0.233]）；弃权全错口径下 majority 反超（0.252 对比 -0.064）
- 机制分解：作答时条件准确率 0.918±0.005，新 ambiguity 弃权率 0.992，mixed 效用 -0.839
- 匹配预算：价值选择器 10% 预算 +0.0138、25% +0.0041，50%/63.7% 为 -0.0795/-0.1493，全预算段不及 pair 不确定性
- CREMA-D 八帧融合减音频 +5.87%（wav2vec 2.0+ViT）与 -2.49%，演员置信区间均含零

**是否开源**：代码已开源 @ https://github.com/MENGZHEGENG/audio-video-text-conflicts（MIT）。

### ⭐ 评分：6/10
评分理由：方法学严谨，匹配控制的效用差恒等式、多种子配对bootstrap与诚实的负结果报告是诊断式评测的好示范；但核心增益强绑定特定奖励口径，学习策略全预算段不敌固定阈值与不确定性基线，媒体实验置信区间含零，对语音系统缺乏可直接部署的收获，价值主要在评测协议设计层面。

---

## 📄 更多语音论文（紧凑列表）

> 以下 10 篇为当日语音相关论文，未进入精读队列，仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），按预估评分从高到低排列。

**SmoothConv and DuplexConv: Complementary Mandarin Multi-Party Conversational Speech Corpora for Speech Interaction**
- **arXiv ID**：arXiv:2610.11150 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.11150（未精读，按摘要评分）

**Listen-to-Reason: Listen with Experts, Retrieve over a Graph, Reason with LLMs**
- **arXiv ID**：arXiv:2610.10749 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.10749（未精读，按摘要评分）

**SEER: Source-Conditioned Emotion Enhancement via Retrieval for Cochlear-Implant Speech**
- **arXiv ID**：arXiv:2610.11131 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.11131（未精读，按摘要评分）

**Using the enrollment gallery as evidence: affine-invariant score calibration for target speaker tagging**
- **arXiv ID**：arXiv:2610.11272 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.11272（未精读，按摘要评分）

**MiDashengLM-Spatial: Unifying General Audio Understanding and Spatial Awareness**
- **arXiv ID**：arXiv:2610.11156 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.11156（未精读，按摘要评分）

**Beyond Speech Captions: Speech-Rewarded Style Planning for Conversational Text-to-Speech**
- **arXiv ID**：arXiv:2610.11461 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.11461（未精读，按摘要评分）

**Cross-Lingual Speaker Verification with Self-Supervised Pre-Trained Models**
- **arXiv ID**：arXiv:2610.11099 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.11099（未精读，按摘要评分）

**Self-Supervised Speech Representations for Cross-Speaker Dysarthria Detection During Awake Craniotomy**
- **arXiv ID**：arXiv:2610.11825 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.11825（未精读，按摘要评分）

**Towards Automated Clinical Behavioral Coding with Large Language Models: A Case study Using BOSCC recordings of Children**
- **arXiv ID**：arXiv:2610.11106 | **方向**：语音大模型 | **评分**：5/10 | **链接**：https://arxiv.org/abs/2610.11106（未精读，按摘要评分）

**Open-Vocabulary Audio-Visual Event Localization via Complex-Valued Fusion**
- **arXiv ID**：arXiv:2610.11846 | **方向**：语音前端 | **评分**：5/10 | **链接**：https://arxiv.org/abs/2610.11846（未精读，按摘要评分）

*Subagents used for reading: 15* | Generated on 2026-10-09 语音论文批次, by Kimmy's research agent | Powered by VAgent SpeechAI Researcher
