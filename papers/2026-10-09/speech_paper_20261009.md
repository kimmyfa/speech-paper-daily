# 2026-10-09 语音论文速递

**共收录**: 23 篇 | **语音大模型**: 14 篇 | **语音前端**: 9 篇

> 目标日期 2026-10-09（北京时间）arXiv 语音相关论文共命中 23 篇。
> 以下是按评分排序的结果。

---

## [1] 语音大模型

## [2] 1. MiDashengLM-Spatial: Unifying General Audio Understanding and Spatial Awareness

**arXiv ID**：2610.11156 | **方向**：语音大模型

**作者**：Jinbo Hu, Hang Su, Lichun Fan, Heinrich Dinkel, Jian Luan, Cong Zou, Heng Qu 等

**机构**：小米集团（Xiaomi Inc., China）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11156 | **PDF**：https://arxiv.org/pdf/2610.11156.pdf | **代码**：https://github.com/xiaomi-research/midashenglm-spatial | **Demo**：暂无

### 📌 简介
主流LALM基于单声道训练、丢失声道间空间线索，专用空间音频大模型又牺牲通用理解能力。本文提出首个开源端到端统一音频大模型MiDashengLM-Spatial（7B），在MiDashengLM上以层级语义-空间条件（HSSC）单向双分支编码器接入Spatial-Dasheng，并构建约1.3万小时双耳合成数据管线。其STAR-Bench SR子集准确率70.3%（最强基线Gemini-3.6-Flash仅47.0%）、MMAU-Pro空间子集55.4%，单声道基准与8B级SOTA相当。

### 🔧 技术方案

**问题背景：** 主流LALM处理多通道音频时折叠声道维度（如跨通道平均），丢失空间感知所需线索；现有空间大模型（BAT/OWL等）需大量架构改造并在空间数据上微调，损害通用音频理解能力，且闭集标签限制了对复杂空间场景的开放描述。

**模型架构：** 7B LLM加双分支音频编码器。语义分支为未改动的32层Dasheng语义编码器处理单声道音频；空间分支为12层Spatial-Dasheng，基于MAE预训练的帧级ViT，前置轻量CNN将多通道特征融合为单通道，采用multi-ACCDOA输出（N条轨道，每帧输出活动耦合DOA向量与距离），实现重叠声源帧级检测、定位与运动跟踪。HSSC将语义分支每8层中间表示经MLP适配器单向注入空间分支每3层（共4处），末端融合为统一音频token E_Audio=E_Sem+Adapter(E_Spa)送入LLM。

**核心创新：** (1) HSSC层级语义-空间条件：语义中间表示逐层注入空间分支对应深度，为重叠声源建立语义-空间关联；单向设计保持语义分支前向结构不变，消融显示优于双向连接方案。 (2) Spatial-Dasheng空间编码器：在MAE预训练编码器上引入多通道CNN融合与multi-ACCDOA帧级输出，并以排列不变训练（PIT：ACCDOA用MSE、距离用MAPE）解决轨道错位，实现重叠声源帧级检测与DOA/距离估计。 (3) 可扩展空间数据合成管线：镜像源法预计算数千房间RIR并叠加HRTF渲染含静态/移动声源（最多3个重叠）的双耳场景，LLM合成场景级空间描述，元数据确定性构造多选空间QA，共100万片段、600万QA、约1.3万小时。

**训练策略：** 三阶段课程：Stage I在合成SELD数据上预训练Spatial-Dasheng（帧级活动+DOA+距离，不建模声源类别，PIT损失）；Stage II用其初始化空间编码器并在空间音频-文本对（事件级+场景级）上微调；Stage III在单声道+双耳全量数据上整体微调并侧重空间QA。学习率/优化器/轮数/batch等超参数未单独披露，沿用MiDashengLM；音频统一16kHz、限60秒，双通道64-bin log-mel（512点Hann窗、hop 160）。

### 📊 实验结果

**数据集**：SELD：EasyCom、MRSSound、STARSS23立体声版（真实录音）及合成双耳测试集；空间理解：MMAU-Pro空间子集、STAR-Bench SR子集（真实录音）；通用音频覆盖MMAU、MuChoMusic、MusicQA、LibriSpeech、AISHELL-2、GigaSpeech2、MusicCaps等；训练源音频来自ACAVCaps、AudioCaps、LibriSpeech等。

**主要指标**：
- STAR-Bench（SR）空间准确率：70.3%（最强基线Gemini-3.6-Flash 47.0%，+23.3个点）
- MMAU-Pro空间子集准确率：55.4%（Gemini 48.3%，提升7.1；单声道开源大模型26.8%-43.1%）
- STAR-Bench通道交换ACR：72.6%（随机11.1%，其他LALM 0-17%）
- EasyCom SELD F45°/1：31.6（PSELDNets 26.1，+5.5）；MRSSound F45°/1：26.4（+10.5）
- 空间QA（纯多通道训练）：总体准确率OV1为80.6%、OV2为66.9%（随机28.8%），三轴位置精确匹配F分数44.7%升至50.8%
- 通用音频：MuChoMusic 76.7、MusicCaps FENSE 60.0、LibriSpeech test-clean WER 1.8%，与8B级SOTA相当

**是否开源**：代码与模型权重已开源 @ https://github.com/xiaomi-research/midashenglm-spatial （HuggingFace: mispeech/midashenglm-spatial）

### ⭐ 评分：8/10
评分理由：首个开源端到端统一"通用理解+空间感知"音频大模型，单向HSSC设计精巧、消融充分，1.3万小时合成数据管线可复现、实用价值高。空间基准大幅超越最强基线，通道交换实验严谨验证双耳线索依赖，SELD的sim-to-real泛化亦有实证。扣分项：细粒度空间能力偏弱（运动轨迹精确匹配低于20%、OV2空间计数39.5%），超参数披露不足。

## [3] 2. DiffuPlex: Accelerating Full-Duplex Spoken Dialog Models via Rolling Masked Diffusion

**arXiv ID**：2610.12214 | **方向**：语音大模型

**作者**：Heeseung Kim

**机构**：首尔大学人工智能系（韩国首尔）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.12214 | **PDF**：https://arxiv.org/pdf/2610.12214.pdf | **代码**：暂无（拟评审后开放） | **Demo**：https://diffuplex.github.io/

### 📌 简介
全双工语音对话模型（Moshi、PersonaPlex等）每80ms交互帧都需调用一次时间骨干网络，逐帧自回归推理成为部署瓶颈。本文提出DiffuPlex滚动掩码扩散框架：每次骨干"wake"用流专属MASK token一次性预测多个未来用户/助手帧，仅消费高置信前缀，若用户实际输入偏离预测则只修订未播放的未来部分。基于personaplex-rl-seamless骨干，Listen与Speak两种推理策略平均每次wake推进1.91/2.23帧，实现1.46×/1.59×部署墙钟加速与1.61×/1.80×核心语言模型加速，所有骨干调用均在80ms内完成；人评显示Listen的语音自然度（NMOS 3.92）与对话质量（DMOS 4.08）基本无损。

### 🔧 技术方案

**问题背景：** 现有全双工语音模型采用单流序列化或并行用户/助手双流，每80ms交互帧都要前向一次时间骨干（Moshi、PersonaPlex均如此）；细粒度利于响应打断与附和，但逐帧顺序计算使累计GPU开销极高。而双人对话中95.3%时间为单说话人，未来帧本可联合预测，但全双工场景验证助手草稿所需的用户语音尚未到达，使投机解码难以直接迁移。

**模型架构：** 骨干为personaplex-rl-seamless（PersonaPlex的强化学习后训练版，Moshi式架构，12.5Hz即80ms/帧，17流布局：1条助手文本流+用户/助手各8个Mimi音素代码本，其中cb0为语义码、cb1-7为声学码），由时间骨干建模交互序列、深度Transformer帧内自回归解码音频代码本。DiffuPlex冻结骨干，仅训练流专属MASK嵌入与未来门控LoRA（rank 128，门控g(h)=1[h≥2]，深度Transformer同步施加同门控）。数据流：每次backbone wake将不可用的未来流按角色与原生延迟阶梯式替换为MASK，联合预测W=16个未来位置（h=1保持原自回归路径，h≥2走学习得到的扩散路径），输出助手草稿与用户预测；草稿高置信前缀按原80ms速率播放，用户预测存储备查，新到达用户帧触发校验与修订，实现"预测-消费-修订"滚动循环。

**核心创新：** (1) 掩码未来预测与蒸馏训练：用变长块（L_blk从{1..W}均匀采样）clean-context拼接构造训练序列，以冻结自回归模型为teacher，对文本token与PAD/EPAD/词法三态分布及Q个音频流加权KL蒸馏对齐掩码学生路径；与投机解码用小模型draft、PredGen等将计算前移但序列仍逐帧自回归不同，此处骨干自身在单次前向中并行预测多个未来交互帧。(2) 滚动草稿生成（Rolling Draft Generation）：按策略允许的状态集合与置信度C_h=softmax(z_h)的y_h≥τconf(=0.80)保留最长连续前缀，Listen仅限PAD静音态且最小保留长度m=6，Speak允许全部状态m=2；h=1恒保留保证每次wake至少推进一帧，保留前缀播放期间不再唤醒骨干，仅存储对应用户预测。(3) 用户感知草稿修订（User-Aware Draft Revision）：以-log q_h(x_h)+log P_h(A_h(y_h))-log P_h(y_h)≥τrev(=-0.5)触发修订，该判据近似保留/修订假设的后验赔率检验；触发时丢弃全部未播放未来并从更新后的交互上下文重新唤醒骨干，已播放助手内容与已收用户帧完整保留，避免重播已输出音频。

**训练策略：** 数据为Seamless Interaction面对面双人语料（原始4000+h、4000+说话人），双声道联合处理保持原始停顿/重叠/打断时序；24kHz重采样、Qwen3-ASR-1.7B转写、Qwen3-ForcedAligner-0.6B词级对齐、Silero VAD、Mimi编码为12.5Hz×8代码本；实际训练16,832窗口（来自8,480个session，约702h对话音频）。损失为掩码蒸馏KL（文本token KL+三态文本KL+音频流加权KL）。AdamW，学习率1e-4，权重衰减0.1，梯度裁剪1.0，OneCycle调度（15% warmup+余弦衰减），bfloat16+梯度检查点，单卡batch 4×2梯度累积×4块RTX A6000（等效batch 32），共526步，W=16，LoRA rank 128。

### 📊 实验结果

**数据集**：Full-Duplex-Bench v1.0（停顿/附和/轮替/打断四类）与v1.5（重叠、干扰语音）；VoiceBench、OpenAudioBench（通用语音能力，s→t与s→s口径）；固定60片段运行时子集（单卡RTX A6000，每类15条）。

**主要指标**：
- 骨干调用效率：Listen/Speak每次wake推进1.91/2.23帧（AR为1.00）
- 部署墙钟加速：1.455×/1.590×；端到端GPU加速1.458×/1.593×
- Core LM累计耗时：656.8s降至408.4s/365.5s，加速1.608×/1.797×
- 实时性：wake帧p99延迟61.34ms/61.41ms，超80ms窗口的帧占比0%
- 人评：Listen NMOS 3.92±0.11、DMOS 4.08±0.13（基线3.93±0.12/4.09±0.14）；Speak DMOS 4.07±0.13但NMOS降至3.54±0.12
- 通用能力：VoiceBench s→t 31.93（Listen）/31.20（Speak）对基线31.95；OpenAudioBench s→s 33.53/32.12对34.03
- 关键对比：相比最强基线personaplex-rl-seamless，Listen在Core LM 1.608×加速下各交互指标与基线无显著差异（Holm校正）；免训练延迟执行PAD基线（R=6）墙钟达2.05×但附和频率从0.163跌至0.048、轮替延迟由0.124s增至0.423s，劣于DiffuPlex

**是否开源**：代码暂未开源（宣布评审后发布实现与评测脚本），Demo页可用 @ https://diffuplex.github.io/

### ⭐ 评分：8/10
评分理由：将滚动掩码扩散与置信修订机制迁移至全双工语音对话，思路新颖且机制自洽，系统性解决了逐帧骨干调用瓶颈。实验非常充分，覆盖全双工两个版本基准、通用能力、人评、运行时测量及大量消融与配对统计检验。加速幅度约1.6倍属务实改进，且Speak策略语音自然度下降、方法绑定特定骨干未跨架构验证，故未达突破性顶会水准，为高完成度的实质贡献。

## [4] 3. Edit Who Speaks, Control How They Speak: Global Timbre Editing and Local Instruction Control for TTS

**arXiv ID**：2610.11437 | **方向**：语音大模型

**作者**：Junchuan Zhao, Chenglin Xu, Wei Zeng, Haoyang Li, Yiwen Guo, Ye Wang

**机构**：新加坡国立大学（NUS）、LIGHTSPEED、南洋理工大学（NTU）、独立研究员

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11437 | **PDF**：https://arxiv.org/pdf/2610.11437.pdf | **代码**：暂无 | **Demo**：https://danny-nus.github.io/EDICT-demopage/

### 📌 简介
本文针对TTS中"全局音色编辑+局部表达控制"的双重瓶颈：现有接口只能克隆参考声音或用文本描述新声音，无法直接编辑给定参考音色并用其合成；整句级指令也无法对应到不同文本片段。提出EDICT框架：第一阶段训练1.7B音色编辑器，按九维属性相对编辑指令在codec空间生成经编辑的参考音色；第二阶段在冻结TTS骨干的段落边界重建KV缓存实现局部指令控制并抑制控制泄漏。在自建TimbreEdit-Bench与IntraTTS-Bench上，EDICT取得最高目标相似度SIM-T 0.793/0.648与类别编辑准确率91.7%，Stage II的SegAcc达82.3%、过渡质量82.0%，分别较TED-TTS高约8pp与4pp。

### 🔧 技术方案

**问题背景：** 现有声音指定接口分为声音克隆（声学参考）与声音设计（文本描述）两类，均无法直接修改给定参考音色并用编辑后的新声音合成新文本；多数指令式TTS对整句使用单一prompt，TED-TTS等仅用注意力掩码而不刷新声学历史，旧KV状态把前段条件带入后续片段造成控制泄漏，保留全部历史又会削弱新指令、丢弃又失去连续性所需的上下文。

**模型架构：** 整体为可训练音色编辑器与冻结自回归TTS骨干的两级级联。Stage I：Qwen3-14B在推理时把全局编辑请求解析为九维属性操作（感知性别、年龄印象为类别型，音高区、亮度、声厚、共鸣焦点、粗糙度、气息感、鼻音为三档有序，未提及属性置为<keep>）并序列化为z_edit；编辑器（自Qwen3-TTS-12Hz-1.7B-Base初始化，含codec预测器，全参数训练）以(源参考codec序列, z_edit, 编辑参考文本)为条件生成codec域编辑参考。Stage II：编辑参考全句固定为共享声音锚点，冻结骨干（Qwen3-TTS-VD为主、CosyVoice 2为第二骨干）逐段生成；每个非终<EOS>边界丢弃旧KV缓存，用"新指令+新文本+编辑参考+声学输入前S=4与最近K=5位置"重新prefill，保留声学状态的KV在新条件下前向重算，段内缓存正常增长，各段汇入单一codec流解码为一条波形。

**核心创新：** (1) 参考锚定的相对音色编辑：不做绝对目标声音指定，而是相对源声音的逐属性操作（如<brightness_up_1>），由LLM把自由描述映射为结构化操作，<keep>显式保持未编辑属性，输出可复用的codec声音锚点，支持任意新文本与演绎条件的零样本合成，区别于声音克隆（需目标声音样本）与经典语音转换（仅同文本内容）。 (2) 奖励加权DPO后训练（wDPO）：不用人工偏好对，而以生成候选与配对目标声音的WavLM说话人嵌入余弦相似度为奖励，正样本奖励差作偏好对权重，并叠加辅助SFT交叉熵（λ=0.01）稳定对齐目标音色；候选离线采样M=16个且偏好对冻结，避免在线采样开销。 (3) 段边界KV缓存重建：每次指令切换以"新指令+编辑参考+初始S位置+最近K位置"重新prefill并在更新条件下重算保留声学KV，初始上下文保声音身份、最近上下文保续接自然，是有界历史机制；不同于TED-TTS纯掩码（旧缓存仍携带前段条件），消除控制泄漏并支持多次切换，且无需骨干额外训练，可泛化到任意自回归TTS。

**训练策略：** 编辑器全参数微调：SFT在1M编辑对上训练50 epochs，AdamW，lr 4e-6，有效batch 1024，weight decay 0.1，余弦衰减+10%预热；损失为全部codebook上的teacher-forced交叉熵，残差codebook损失权重0.3，条件dropout 0.1。数据由5,800个九维音色profile（留200个、训练对两侧均排除）经Qwen3-TTS-VD合成中英中性演绎配对语音，编辑操作源自source-target profile差异，覆盖单属性/组合编辑、同异文本、跨语言；再经一轮wDPO：20K训练条件各采样M=16候选，lr恒1e-6，每更新8条件，β=0.1，λ_SFT=0.01。

### 📊 实验结果

**数据集**：1M合成中英编辑对（训练）；TimbreEdit-Bench：1,955对源-目标、9编辑类别、3名标注员筛选、中英双语；IntraTTS-Bench：997条2-3片段多指令请求、中英双语；另有ESD真人录音参考集与500条MED-TTS。

**主要指标**：
- 音色编辑SIM-T（TimbreEdit-Bench，描述式指令）：EDICT-Stage I 0.793（WavLM）/0.648（ERes2Net），指令条件系统中最优
- 编辑Δ（目标-源相似度差）：+0.195/+0.207，为唯一输出比源更靠近目标的指令条件系统（Qwen3-TTS-VD为-0.156/-0.279）
- 类别属性编辑准确率：91.7%（描述式）/89.3%（结构化）；Up/Down方向准确率77.9%/70.8%
- 句内指令控制（IntraTTS-Bench，Qwen3-TTS-VD）：EDICT-Stage II SegAcc 82.30%、EmoAcc 83.60%、Trans 82.00%、SIM-I 0.915
- 联合控制（EDICT全流程）：SIM-T 0.788/0.609最高、SIM-I 0.917、UTMOS 3.795、DNSMOS 3.921最高
- 关键对比：相对最强局部控制基线TED-TTS，Stage II的SegAcc提升+8.05pp（Qwen3-TTS-VD）与+2.46pp（CosyVoice 2），Trans提升+3.97pp与+12.26pp
- 代价：WER/CER较Joint设定升高（英文WER 3.8→5.1、中文CER 1.3→1.8），说话一致性保持（SIM-I 0.915 vs 0.922）

**是否开源**：代码未开源，仅提供参考音频demo页。

### ⭐ 评分：8/10
评分理由：问题定义新颖，首次统一全局参考音色编辑与局部分段指令控制，KV缓存重建设计巧妙，免骨干训练且验证于两个骨干，消融确认初始/最近上下文互补作用；自建双基准加客观指标、Gemini评审与19名听感主观三重评测，实验充分。不足在于训练数据与基准均为合成语音，真实泛化仅在ESD上有限验证，内容保真有可见代价（英文WER 3.8→5.1），且代码未开源。整体是扎实实用的方法论贡献。

## [5] 4. Listen-to-Reason: Listen with Experts, Retrieve over a Graph, Reason with LLMs

**arXiv ID**：2610.10749 | **方向**：语音大模型

**作者**：Pooneh Mousavi, Mirco Ravanelli, Cem Subakan

**机构**：Concordia University; Mila – Quebec AI Institute（Subakan 另属 Laval University）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.10749 | **PDF**：https://arxiv.org/pdf/2610.10749.pdf | **代码**：https://poonehmousavi.github.io/listen-to-reason/ | **Demo**：https://poonehmousavi.github.io/listen-to-reason/

### 📌 简介
LALM通过多阶段训练耦合音频编码器与LLM，更换领域或LLM需重训，且答案无法追溯到所听内容。本文提出Listen-to-Reason（L2R）：四级多模态知识树（39属性/363类/668叶）加冻结专家编码器上的小路由头，把音频块映射为可命名树节点，与ASR转写拼成文本上下文，由冻结纯文本LLM作答，任意图灵能替换reader，新域只需训练一个小头。7B reader在SAKURA达80.1%超越所有对比LALM（最佳73.3%），MMAU/MMAR仅落后6.8/12.0分，且仅训练7.7M参数（约为Omni-7B的1/1400）；新域每类5条样本即超过QLoRA微调13–26分。

### 🔧 技术方案

**问题背景：** LALM将音频编码器输出以连续嵌入接入LLM并多阶段训练，编码器与LLM深度耦合：换更强LLM或新编码器、适配新领域都要重新微调，且可能遗忘旧能力；其CoT是决策后由同一网络生成的事后叙述，不忠实于决策，答案无法追溯到模型实际听到的证据。

**模型架构：** 管线分四步。Listen：构建树状多模态知识树——地域（语音/音乐/环境声）→属性（性别、情绪、乐器等39个）→闭集类（363）→开放词表叶（668，如"engine knocking"），由4,054条19来源片段经专家分类器+Qwen3-Omni-30B按严格模板混合标注建成。Retrieve：每个短块由适配该属性的冻结编码器（CLAP管声音音乐、emotion2vec管情绪等）提取嵌入，经共享1–3层MLP小体（宽256）+每属性一个头打分；类得分取该类节点与其叶的log-sum-exp，叶置信才输出否则回退到类（如engine knocking→engine），region gate决定块激活哪些地域。Reason：整片节点按属性去重分组成可读文本（如speech gender: female; sound animal: dog (Bark)），拼接Whisper-large-v3转写与带时间的事件列表，冻结文本LLM仅凭该上下文作答。Adapt：新域作为新属性挂入树，用一个冻结编码器+小头承接。

**核心创新：** (1) 可解释性源于设计：音频只以树节点+转写文本进入LLM，答案的解释即其输入，错答可定位到单个节点并修正而不触碰reader；干预实验证明节点是因果的——SAKURA单跳将路由节点换成干扰节点使78.3%正确答翻错，注入金节点修复90.9%错答（动物/情绪/性别达93.8–99.8%），与LALM的不可追溯CoT本质不同。(2) 统一分层词表+蒸馏路由头：用单一层级词汇覆盖语音、音乐与环境声（非SAR-LM拼接多抽取器标签空间），小头从仅训练期的教师模型（如VGGSound软标签）蒸馏，推理时同一套头无planning地服务所有片段。(3) 感知与推理文本化解耦：任何LLM可零训练当reader（实测0.5B–72B共26个，72B/32B在MMAU-Pro超AF3）；新域=新头（0.17M–0.34M）在冻结编码器上几分钟训完，双域添加后原任务掉点≤0.6，无灾难性遗忘，而LALM需QLoRA重调。

**训练策略：** 仅训7.7M可训参数（各路由头小体），约1,400×少于Qwen2.5-Omni-7B；损失为属性掩码下的类交叉熵/BCE（单选softmax、多选二元）加父类内叶交叉熵，叶学习不移动类间概率；叶需≥5条样本（情绪/性别≥3）才成节点，稀有叶回归父类节点。AdamW，学习率3e-4–1e-3，批64，60–80 epoch；数据共约0.2M标注片段（AudioSet、FSD50K、ESC-50、MusicCaps、IRMAS、FLEURS等），数量级小于LALM语料（Omni-7B仅二阶段用300B音频token）。

### 📊 实验结果

**数据集**：MMAU test-mini（1,000题）、MMAR（1,000题）、SAKURA（4,000题）、MMAU-Pro单音频多选子集（4,133题）；新域：BirdSet鸟类48种（938题）、BEANS海洋哺乳31种（678题），均为四选一只选，随机25%。

**主要指标**：
- SAKURA：7B reader 80.1%，超全部LALM（Omni-7B 73.3%、Qwen3-Omni-30B 73.0%、AF3 68.2%）
- MMAU：68.3%（Omni-7B 75.1%，差6.8分）；72B reader提至70.5%，Phi-4达71.7%
- MMAR：51.6%（Omni-7B 63.6%，差12.0分）；MMAU-Pro 45.7%（vs 57.4%）
- 因果与判官：节点置换破坏78.3%正确答、金节点注入修复90.9%错答；3个音频LLM判官在97–99%的1,200条留样上给L2R节点高于对照组
- 新域5条/种：鸟类79.6%、海洋76.2%应为65.2%，对比QLoRA 54.1%/52.2%（13–26分领先；QLoRA训40.4M参数，多120–240×）
- 关键对比：训练参数7.7M vs LALM数亿至数十亿，约为Omni-7B的1/1400、音频数据少数量级；推理单MMAU题5.3 TMACs/0.57s，高于Omni-7B的2.7/0.12（Whisper占约半）

**是否开源**：代码已开源 @ https://poonehmousavi.github.io/listen-to-reason/（含checkpoint、示例与树交互查看器）

### ⭐ 评分：8/10
评分理由：以可读知识树作文本瓶颈解耦感知与推理，思路原创且动机扎实；节点因果干预与判官评估为音频领域少见的定量可解释性证据，26个reader扩展与两个新域的few-shot实验充分可信。但MMAU/MMAR仍落后LALM 6–12分，暴露树词汇在细粒度声学推理上的信息损耗，且推理开销明显高于同规模稠密LALM，故给8分。

## [6] 5. EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams

**arXiv ID**：2610.12248 | **方向**：语音大模型

**作者**：Heeseung Kim

**机构**：首尔大学AI系

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.12248 | **PDF**：https://arxiv.org/pdf/2610.12248.pdf | **代码**：暂无 | **Demo**：https://egocentricvoice.github.io/

### 📌 简介
可穿戴AR助手需从连续第一人称视听流中自主决定何时开口，但现有omni-modal模型均为被动对话，主动视频助手只能输出文本。本文提出EgoVoice：用源分离与语音重合成将HoloAssist真实教练指导录音转成91.7小时干净训练数据，微调MiniCPM-o 4.5学习"倾听或开口"的秒级决策，再以DPO精化干预时机。170个测试会话上，闭源API开场F1仅0.02-0.03，EgoVoice-SFT/DPO达0.274/0.324，end-vs-action间隔+1.57s/+1.75s，显著优于zero-shot基座（F1=0.113，间隔-4.69s），接近人类教练水平。

### 🔧 技术方案

**问题背景：** 真实物理任务中用户常忙碌或无法察觉何时需要帮助，而现有语音助手是反应式的，依赖显式提问或VAD触发；主动视频助手（如ProAssist）只产出文本。尚无工作将"何时说话+说什么"统一到单一模型中从连续第一人称视听流训练。

**模型架构：** 基于MiniCPM-o 4.5（9B，流式全双工omni-modal LLM）。每个1秒chunk编码一帧第一人称视频与1秒音频（背景音+用户语音），预测Listen或Speak；Speak chunk上LLM自回归生成BPE文本，0.3B语音token解码器产出S3 token，流式flow-matching解码器转为波形。教练语音仅作为输出目标；以每次干预为中心构造60秒训练窗口，共13,676个。

**核心创新：** (1) 解决"文本指令→语音播放"时间错配问题的真实语音数据管线：从1,673个HoloAssist会话出发，SAM-Audio以语音区间为提示分离出背景通道，Silero VAD校验无语音残留；转录用gpt-5.4-mini归一（删除9.0%无关话语），IndexTTS2按会话重合成（2,498训练/340评测参考说话人），Qwen3-ASR验证ASR精确匹配，最终得1,249训练+170测试会话。(2) 两阶段训练：SFT损失为L_LM+0.1·L_S3，并在LLM隐状态处切断语音损失梯度（消融显示不切断F1略高但评分下降）；DPO每窗口采10个候选，F1最高者为正例、F1最低三者中随机取负例（F1差≥0.10）构成5,335对，用长度归一DPO精化时机。(3) 四维评估协议：非对称开场窗口（提前2.5s/延后1.5s）配Hungarian匹配算Prec/Rec/F1；end-vs-action间隔度量"用户行动前是否说完"（行动链接子集942/2,067语句）；余弦相似度度量内容相关；LLM评审按正确性/及时性/效率/总体四轴1-5打分，并分text-llm与text-asr双通道评估意图与实际听感。

**训练策略：** SFT：LoRA（r=32，α=64）同时施加于LLM骨干与语音解码器，视觉/音频编码器冻结，5 epochs，学习率2e-4，batch size 32。DPO：仅LLM骨干加LoRA，长度归一DPO，β=0.1，学习率5e-6，batch size 16，1 epoch，S3语音token不参与DPO似然。

### 📊 实验结果

**数据集**：HoloAssist（1,673会话/124.8小时第一人称任务指导录音，清洗后91.7小时训练、12.9小时测试；60秒窗口、1秒chunk粒度）

**主要指标**：
- 开场时机F1：EgoVoice-SFT 0.274，EgoVoice-DPO 0.324（zero-shot MiniCPM-o 4.5仅0.113；Gemini Live 0.022、gpt-realtime 0.030、gpt-realtime-2 0.024）
- 内容相关余弦相似度：SFT 0.684，DPO 0.649（zero-shot 0.519，ProAssist 0.594）
- 语句结束vs行动间隔（均值/中位数，正值=用户行动前说完）：SFT +1.57s/+1.52s，DPO +1.75s/+1.62s，zero-shot -4.69s/-0.40s，人类教练+1.69s/+1.38s
- LLM评审总体分（1-5）：SFT 2.23，DPO 2.18，zero-shot 1.41，ProAssist 2.06
- 人类偏好胜率：SFT对zero-shot 45.6%（p=0.01），DPO对zero-shot 45.3%（p=0.02），DPO对SFT 36.1%对33.3%不显著（p=0.60）
- 关键对比：SFT较zero-shot基座F1提升0.161（p<10⁻¹²），超文本基线ProAssist 0.079（p<10⁻⁴）；DPO较SFT再提升0.050（p=0.0007）；干预顺序Kendall's τb DPO 0.868 vs zero-shot 0.749

**是否开源**：暂无（项目页：https://egocentricvoice.github.io/）

### ⭐ 评分：8/10
评分理由：选题新颖重要，首次将第一人称"何时说+说什么"统一进单一omni-modal语音模型，数据处理管线与四维评估协议扎实、工程严谨。含闭源/API、开源文本与全双工基线、消融、显著性检验与真人评估，实验充分。召回率0.285与人类差距明显、数据局限于组装类任务，但贡献实质，属优秀工作。

## [7] 6. DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration

**arXiv ID**：2610.11299 | **方向**：语音大模型

**作者**：Yingda Shen, Yuxiang Wang, Kunyu Feng, Qinke Ni, Jiaqi Li, Minghao Hsu, Junan Zhang, Dekun Chen, Yutong Bian, Zhizheng Wu

**机构**：香港中文大学（深圳）；Amphion Technology Co., Ltd.

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11299 | **PDF**：https://arxiv.org/pdf/2610.11299.pdf | **代码**：https://amphionteam.github.io/DuplexAgent-RSI-Demo/ | **Demo**：https://amphionteam.github.io/DuplexAgent-RSI-Demo/

### 📌 简介
全双工对话模型推理与工具执行能力弱，顺序编码代理缺乏直播对话的实时性；现有异步委托协作的任务更新、取消、替换与结果交付决策耦合在系统特定启发式里，难以从痕迹中定位与修复。本文提出DuplexAgent全双工协作系统，将协作流程显式化为六个可编辑harness模块，并给出Duplex-Harness-RSI闭环：委托池推理LLM任Exam Planner、编码代理任Harness Editor，依据交互痕迹与修复档案迭代修订模块。在Qwen-Realtime上MMSU由64.8升至82.7、FDB-v3 Pass@1由39.0升至49.0，固定核心协作分较初始harness提升37.7分。

### 🔧 技术方案

**问题背景：** 领域正收敛到"全双工模型守活频道、推理/编码代理异步承接任务"的协作范式，但用户修改请求时如何更新、取消或替换进行中的任务、结果何时开口交付并无定论。现有系统用手写耦合启发式实现交接、确认与交付控制，同一失败反复出现时痕迹无法明确指向委托、解释、执行还是交付环节，有界修复难以隔离、评估与迁移。

**模型架构：** 系统分解为S=(F,B,H)：F为全双工交互模型（VoiceChat-11B或Qwen-Realtime），B为委托池（DeepSeek-v4-flash推理、Codex编码），H为协作harness含六个模块：Policy决定应答路由（直答/委托/任务控制）、Intake解析请求及其关联的在途任务、Hold在工作挂起期间维持确认与进度播报、Worker选择代理并定义结果契约、Deliver控制结果返回的说话窗口与成败呈现、Memory维护对话与后台共享的上下文（组装、保留、压缩、复位恢复）。底层由会话引擎任务台账（accept/run/complete/deliver/cancel/replace六态，迟到的返回不能复活过期任务）与模型适配器支撑，使harness决策与传输细节解耦。RSI闭环组件：Observer记录痕迹（语音活动、转写、模块决策、代理返回、交付事件）；Diagnoser给出(cause,module,pattern)失败签名，按固定优先级映射到感知/路由/解释/连续性/执行/交付/上下文家族；Exam Planner依据归因失败与修复档案在19种请求类型×22种交互模式上调整下轮考试采样并保留固定核心；Harness Editor在隔离工作区仅修订诊断指名的模块的声明可编辑面（指令、schema、结果契约、覆盖规则），给出可检验假设；评估器校验六条协作不变量，候选须过配对开发门（胜>负）与不相交保护门（胜≥负）才保留，接受与拒绝的经验写入修复档案供下轮使用，交互模型权重全程不动。

**核心创新：** (1) 协作harness的六模块可编辑分解：将协调决策变成输入、决策、可观测效果明确的模块并声明可编辑面，任何失败都能归因到有限模块并被独立检验；与Qwen-Audio-Agent、Realtime-Venus、Gander等系统以自然语言描述或任务标题做交接、决策相互耦合不可分的关键区别在于"任务身份+说话时机+上下文共享"被显式建模。 (2) Duplex-Harness-RSI递归改进闭环：复用服务用户的委托池改进系统自身，推理LLM作Exam Planner从归因失败与修复档案设计自适应测试，编码代理作Harness Editor产生修复假设，以固定核心配对胜负与保护集独立裁决保留与否；相比一次性/顺序编辑多了每轮诊断与档案经验，采样权移动有界、保护集对编辑器隐藏、禁止插入情景特定答案。 (3) 可复用全双工协作模拟器：请求类型与交互模式解耦，确定性composer把回合排上实时时间线并定义期望任务转换与说话窗口，内容先切分开发/保护/封存(60/20/20)防泄漏，再经Qwen3-TTS渲染与噪声信道增强生成带时间戳的测试对话，可产出模块级失败归因。

**训练策略：** 系统类工作，不训练任何交互模型权重。闭环按交互模型各跑10轮独立campaign：固定核心占比40%，每轮新变体预算30，每轮最多3个候选、每候选最多2次修正；Exam Planner对请求类型/模式/输入条件的采样权移动有界且设请求覆盖下限。外部评测按实时时钟流式输入，OBQA/MMSU、BFCL-v3、FDB-v3、FDB-v1各自独立评分；协作分Q为固定核心上剔除感知失败后的成功率。

### 📊 实验结果

**数据集**：VoiceBench（OBQA、MMSU）、BFCL-v3（五单轮子集）、FDB-v3、FDB-v1；自建模拟器测试对话（19请求类型×22交互模式，60/20/20切分）

**主要指标**：
- MMSU：80.5（VoiceChat）/82.7（Qwen-Realtime），对比独立交互模型36.1/64.8
- OBQA：80.6/92.1，对比独立54.2/86.3
- BFCL-v3均值：75.8/90.8，对比独立53.5/82.0（Qwen-Audio-Agent 24.9/80.8）
- FDB-v3 Pass@1：47.0/49.0，对比独立16.0/39.0（Qwen-Audio-Agent 5.0/30.0）
- FDB-v1打断TOR：0.965（VoiceChat）/0.970（Qwen-Realtime），不低于所附模型1.000/0.890
- Harness消融（VoiceChat固定核心）：初始54.6→一次性编辑57.4→顺序编辑61.9→RSI 85.3；Qwen-Realtime初始47.1→第8保留版84.8
- 关键对比：RSI r10较初始harness提升30.7分、较顺序编辑提升23.4分；漏委托由30.3%降至1.3%，额外交付由3.9%略升至6.6%

**是否开源**：代码已开源 @ https://amphionteam.github.io/DuplexAgent-RSI-Demo/（项目页同址）

### ⭐ 评分：8/10
评分理由：将全双工协作显式化为六模块可编辑harness、并复用委托池做递归自改进，思路新颖且闭环完整可复现。实验充分：双交互模型×四组外部基准，加一次性/顺序/RSI消融与模块级修复证据，数据扎实。不足是改进止于harness层、触不到模型自身感知与时机，模拟器评测偏自建。对真实语音代理落地实用价值高。

## [8] 7. SAVU-BENCH: A Real-World Benchmark for Spatial Audio-Visual Understanding

**arXiv ID**：2610.10624 | **方向**：语音大模型

**作者**：Yu Chen, Ruihang Liu, Yangguang Xu, Xinyue Jiang, Mohammed Bennamoun, Farid Boussaid, Xinyuan Qian, Qiuhong Ke

**机构**：University of Western Australia、University of Science and Technology Beijing、Monash University

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.10624 | **PDF**：https://arxiv.org/pdf/2610.10624.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有空间音频-视觉基准多依赖仿真场景且孤立评估单项空间能力，缺乏对失败机制的诊断。作者提出SAVU-Bench：基于6个真实数据来源、覆盖"感知-对齐-推理"三级能力与7项任务（1066条问答，平均片段6.12秒）的实景空间音频-视觉理解基准，并设计场景链接诊断集SAVU-Diag（611条/81场景），将推理题分解为前置接地与对齐子任务。评测12个模型显示：视觉接地最高95.4%，音频接地仅55.6%，空间推理最高45.8%（chance 42.2%）。免训练基线SAVU-EA将音频接地提升30.7个百分点。

### 🔧 技术方案

**问题背景：** 当前AV-LLM能识别"有什么"，但难以定位视觉实体与声源并解析其跨模态空间关系。现有基准存在三局限：一、重度依赖仿真环境，无法反映真实录音复杂度；二、孤立评估单项空间技能，难以在同一场景系统考察感知、对齐、推理的协同；三、任务级准确率缺乏诊断性，无法区分推理错误源于定位失败还是关系组合失败。

**模型架构：** 基准将7任务按难度升序组织为三级：感知层含Audio/Visual Grounding，各细分粗定位、相对位置、空间动态（含水平与深度运动）三类；对齐层含语义对齐（可听事件是否匹配可见对象）、空间对齐（声源轨迹与其视觉 counterpart 运动是否一致，负样本保持类别级语义兼容只改变空间关系）、A2V/V2A联合匹配（候选为匹配项+语义负例+空间负例）；推理层含相对方向（以视觉参考定位画面外声源）、空间排序（原地旋转遭遇声源方向序列）、自我中心推理（换算到由场景实体定义方位与朝向的虚拟观察者视角）。推理实例围绕双模态互补线索构造：静默视觉锚点+画面内发声源+画外声源，以画面内源为共同参照连接视觉与听觉空间布局。数据源自MRSAudio、STARSS23、YT360、D-SAV360、MULTIVOX、QoEVAVE六个真实来源；全景录像切分出有限视场视图，FOA音频按ViSAGe约定水平重居中并与视觉参考系对齐；GPT-5.4仅生成候选草稿，人工核验修正，推理题链由标注者确认后生成；三位领域专家独立作答、至少两位正确方可保留。SAVU-Diag将每道推理题的前置事实转写为同场景、同时间窗、同参考系的独立诊断任务，把推理错误分解为接地对错×对齐对错的2×2模式。

**核心创新：** (1) 真实场景统一的三维能力评测框架：首次在同一无仿真实景设定中贯通感知、对齐、推理，并以全部选项循环置换消除选项位置偏差、按AA_circ计准确率。(2) SAVU-Diag场景链接诊断：将推理题与同场景前置接地/对齐任务绑定，可区分"空间证据获取失败"与"证据组合失败"两类错误，揭示相似推理准确率背后截然不同的前置错误模式。(3) SAVU-EA免训练证据增强基线：以SELD与VLM提取显式空间线索注入输入，作为干预实验量化感知瓶颈与残存推理差距的价值。

**训练策略：** 基准评测协议为多选判定，每题在选项全循环置换下评测；Spatial-Omni保留四通道FOA输入其专用空间编码器，其余模型走单声道downmix，人工评测用HRTF渲染双耳音频，模型与人同场景同题可比。SAVU-EA为免训练推理策略：OpenVocabularySELD从FOA音频提取声事件及空间轨迹，Qwen3.5-Omni-Plus从静默视频提取可见对象、位置与运动，将预测空间线索连同原始输入、提问一并提供给Gemini-3.6-Flash；感知任务仅注入对应模态的线索。

### 📊 实验结果

**数据集**：SAVU-Bench（1066条问答、7任务、平均片段时长6.12秒、平均题长15.41词，真实FOA一阶Ambisonics音频+有限视场视频）；SAVU-Diag（611条诊断问答、81场景、平均每场景7.54条）。

**主要指标**：
- 视觉vs音频接地：最高Visual Grounding 95.4%（DOTS-3）对最高Audio Grounding 55.6%（Spatial-Omni），差距约40个百分点
- 联合匹配：最佳A2V 35.6%、V2A 42.8%，相对33.3%随机基线仅提升约2-10个百分点
- 空间推理：最佳45.8%（Gemini-2.5-Pro、SO-7B），仅高于42.2%随机水平3.6个百分点；30题人评子集上人类达85.0%，与最佳模型差距38.3个百分点
- SAVU-Diag：OmniVideo-7B的推理错误61.4%为纯接地失败；Spatial-Omni仅17.9%纯接地失败，46.2%为双前置失败，且前置全对时仍存在推理错误
- SAVU-EA：Audio Grounding +30.7点、Joint A2V +19.1、V2A +21.7、Spatial Reasoning +14；oracle前置事实下推理从49.38%升至77.78%（+28.4）

**是否开源**：暂无（作者声明被接收后计划公开基准、评测代码与构建脚本）

### ⭐ 评分：8/10
评分理由：真实场景三级七任务体系与SAVU-Diag场景链接诊断设计新颖，填补现有仿真/孤立基准空白；12模型评测、人评子集、oracle与捷径消融实验齐备，数据管线含专家三重校验，结论扎实。SAVU-EA干预有效量化感知瓶颈与组合差距。不足是诊断集规模偏小（81场景/611条），代码数据尚未开源，且QA生成依赖GPT草稿的人工质量控制难以完全排除偏差。

## [9] 8. SmoothConv and DuplexConv: Complementary Mandarin Multi-Party Conversational Speech Corpora for Speech Interaction

**arXiv ID**：2610.11150 | **方向**：语音大模型

**作者**：Chengyou Wang, Mingchen Shao, Chunjiang He, Zeyu Zhu, Jierui Guo, Bingshen Mu, Zikai Liu, Hanke Xie, Yuhang Dai, Zhou Zhu, Lei Xie

**机构**：ASLP@NPU、Soul AI Lab、QualiaLabs（arXiv未提供逐作者机构对应）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11150 | **PDF**：https://arxiv.org/pdf/2610.11150.pdf | **代码**：https://github.com/qualialabsAI/SmoothConv-DuplexConv | **Demo**：暂无

### 📌 简介
语音交互系统需建模轮次交替、重叠语音等会话行为，但现有多方普通话语料缺乏参与者级同步音轨与细粒度交互标注。本文发布SmoothConv与DuplexConv两个互补语料库，共2100小时普通话多人群会话，覆盖辅导与社交聊天场景，每人提供同步音轨及轮次状态、副语言、说话人属性细粒度标注；SmoothConv（100小时）经人工多轮核验，DuplexConv（2000小时）由自动标注流水线构建。在SmoothConv基准上评测语音分离、多说话人ASR与轮次检测三任务，基于对话数据适配后MSASR的cpWER由27.04%降至16.87%，轮次检测incomplete召回达74.66%。

### 🔧 技术方案

**问题背景：** LALM驱动的交互式语音系统需理解轮次交接、响应时机等会话行为，而Switchboard/Fisher仅限英文双人电话，CHiME-5/AMI/AliMeeting/AISHELL-4或缺乏同步参与者级音轨、或缺少交互行为细粒度标注，公开普通话多人群资源不足以支撑真实多人交互建模。

**模型架构：** 数据来源为真实线上交互（Tutoring与Social Chat双场景，知情同意并匿名化），非脚本式录制，保留自然抢话、重叠与长程交互上下文。标注体系含三维细粒度标注：轮次状态（complete/incomplete/backchannel/wait四态）、副语言（12类预定义情绪加哭闹/咳嗽/清嗓/打喷嚏/叹气等非言语发声事件）、说话人属性（性别与儿童/青少年/成人/中年/老年五档年龄）。双库互补：SmoothConv 100小时/2503片段，每段4名标注员标注加3名资深复核，供可靠分析与评测；DuplexConv 2000小时/93709片段，平均片段76.8s（8-618s），自动构建供大规模训练。

**核心创新：** (1) 人工核验小规模与自动标注大规模的双轨设计：SmoothConv提供可靠监督用于评测，DuplexConv提供可扩展训练数据；自动流水线在随机抽样20小时子集上人工核验通过率82.4%，轮次状态标签与专家标注一致率达91%。 (2) LLM驱动的两阶段自动标注：逐通道VAD加多ASR（FunASR、FireRedASR、Qwen3-ASR等）ROVER融合转写，Pyannote说话人日志加Qwen3-ForcedAligner边界精化，3D-Speaker全局聚类；轮次状态由Qwen3-32B从文本预测候选、Qwen3-Omni结合声学复核，incomplete/backchannel以韵律线索重要者优先采用音频判定。 (3) 任务导向的SmoothConv基准：分离/MSASR共享评测集9.48小时/255片段、严格说话人不重叠划分、平均重叠率3.33%；轮次检测集覆盖四态并按自然比例采样，wait态稀疏处用DeepSeek V3加IndexTTS2合成1000条且人工核验，仅用于评测。

**训练策略：** 分离任务以SPMamba训练，各配置480小时（模拟混音WSJ0-2mix/WHAM!/WHAMR!/Libri2Mix、DuplexConv参与者轨派生混音及混合）；MSASR在SoulX-Transcriber骨干上用LoRA微调（1 epoch、lr 1e-5、warmup 0.05、rank 8、α=32），DER配0.25s collar；轮次检测训练FastTurn（EasyTurn、DC、DC+SC三配置）。全程训练/测试严格分离，无共享会话或说话人，SmoothConv作训练集时剔除对应评测样本防泄漏。

### 📊 实验结果

**数据集**：SmoothConv（100h/2503片段，2-4人，人工核验）；DuplexConv（2000h/93709片段，自动标注）；SmoothConv Benchmark（分离/MSASR评测集9.48h/255片段、重叠3.33%；轮次检测集22432条/约12.9h，含1000条合成wait样本）

**主要指标**：
- 语音分离（SPMamba）：DuplexConv对话混音训练在SmoothConv集SI-SDRi 17.26dB/CER 32.15%，显著优于纯模拟混音（13.55dB/81.24%）；混合配置OOD上AISHELL-4 CER 36.04%、AliMeeting CER 45.48%
- MSASR（SoulX-Transcriber+LoRA）：SmoothConv-Bench上DER/cpWER/tcpWER由基线40.89%/27.04%/27.95%降至DC+SC的12.73%/16.87%/17.62%；AliMeeting-Near cpWER 11.65%→7.43%，AMI-SDM DER 16.15%→14.57%
- 轮次检测（FastTurn召回%）：SmoothConv-Bench上DC+SC四态89.20/74.66/94.15/91.30，incomplete与backchannel优于纯DC（72.85/93.78）与EasyTurn（73.03/92.57）
- 关键对比：与Switchboard/Fisher/AMI/AliMeeting/AISHELL-4等相比，仅本语料同时覆盖多轨、轮次、副语言、说话人属性四维度（Table 1），且DuplexConv 2000小时规模远超AISHELL-4（120h）/AliMeeting（118h）等普通话多方语料

**是否开源**：数据、基准及相关资源已开源 @ https://github.com/qualialabsAI/SmoothConv-DuplexConv

### ⭐ 评分：8/10
评分理由：人工核验与自动扩缩容的双轨设计对语音交互资源极具创新性，2100小时四维细粒度标注填补公开普通话资源空白，LLM两阶段轮次标注91%一致率可信；实验覆盖分离、MSASR、轮次检测三任务，MSASR提升幅度实质；不足在于wait态依赖合成样本、远场跨域性能退化，且模型侧仅为LoRA适配未做全量训练验证。

## [10] 9. SteerablePlex: Can We Steer Full-Duplex Models?

**arXiv ID**：2610.12201 | **方向**：语音大模型

**作者**：Haolong Zheng, Maike Züfle, Dominik Macháček, Peter Polák, Xulin Fan, Xavier Sumba, Siyin Wang, Ondřej Klejch, Mark Hasegawa-Johnson

**机构**：University of Illinois Urbana-Champaign, Karlsruhe Institute of Technology, Charles University, Imperial College London, Tsinghua University, University of Edinburgh

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.12201 | **PDF**：https://arxiv.org/pdf/2610.12201.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工语音模型作为用户模拟器时会随对话历史增长偏离预设场景，导致评估失真。本文提出SimIF-Bench基准，量化考官模型的主题遵循、自然度、目标完成与顺序约束，发现GPT-Realtime及开源模型在多阶段顺序完成上均不可靠。进而提出SteerablePlex：以特殊token分隔的在线指令注入接口加GDPO多奖励强化学习配方，使全双工模型在对话中实时遵循文本指令并保持轮替能力。配合异步后端LLM导演，in-domain版在SimIF-Bench的目标完成与精确顺序上双双超过GPT-Realtime，轮替能力10项指标中6项优于基座模型。

### 🔧 技术方案

**问题背景：** 全双工模型边听边说、无明确干预边界，现有系统仅靠系统提示词控制，而提示词遵循度随对话历史增长发生漂移；严格时延预算又限制模型规模与长程规划能力，"能否在运行时控制全双工模型"成为开放问题。

**模型架构：** Actor-Director双角色系统。Actor构建于PersonaPlex的三条同步流（用户音频、模型音频、模型文本，其中模型文本作为音频token的时间对齐语义前缀），将特殊起止token分隔的指令token拼接进模型文本流，注入步内两路音频填充静音token且对话时间冻结。Director为异步文本LLM（Qwen3.8-27B），输入来自Parakeet-TDT-0.6B-v2流式ASR与内部模型文本的上下文，每2秒更新目标状态并输出send/wait/none三态动作，仅在必要时注入指令。

**核心创新：** (1) 在线指令注入接口：复用现有tokenizer将祈使句指令嵌入模型文本流，借助预训练模型对文本流的语义理解降低学习成本，无需学习新控制模态；区别于KAME持续由后端模型驱动前端，此处仅在需要时干预，保留基座原生轮替策略。(2) GDPO多奖励训练配方：将GRPO扩展到多奖励场景，对每个奖励维度在组内独立归一化为z=(r−μ)/σ，未定义或无差异维度置零，加权求和后再组内归一化得优势值，避免高方差奖励分量主导梯度。(3) 六维奖励设计：目标完成（0/0.5/1分档）与自然度（0/1，惩罚自问自答、替对方发言）抑制"直接喊出目标内容"与"抢话制造机会"两类捷径，再加重叠、接管、响应延迟、backchannel F1四个VAD轮替奖励防止霸占话轮，KL项锚定adapter-off的PersonaPlex策略防止漂移。

**训练策略：** 数据分两部分：Fisher语料派生9,417条回合级指令RL样本（合计130.8小时rollout）；按Behavior-SD流水线从Full-Duplex-Bench v2的200个场景合成2,000段重叠语音对话（84.1小时立体声，其中200段留出）。LoRA适配器训练（temporal/depth秩128/32，缩放2.0）；GDPO组大小G=8，音频/文本采样温度0.8/0.7、top-k 250/25；学习率1e-5，任务无关训练自0.05起自适应β朝KL目标0.3调整，in-domain训练固定β=0.01；VAD处理合并小于0.3秒间隔、丢弃短于0.1秒片段，backchannel不超过1秒且须覆盖对方语音至少50%。

### 📊 实验结果

**数据集**：SimIF-Bench（复用Full-Duplex-Bench v2的200个分阶段场景，PersonaPlex固定为受试者，通话120秒，LLM判分三遍取多数/中位数）；轮替能力评测用Full-Duplex-Bench。

**主要指标**：
- SimIF-Bench 200场景：SteerablePlex(in-domain)在目标完成与精确顺序两项上均超过最强基线GPT-Realtime（论文正文未给出表中具体数值，见Figure 2），在20个留出场景上优势保持
- 轮替能力（Table 1，对比基座PersonaPlex）：停顿处理Syn. 0.642→0.394、backchannel TOR 0.418→0.218、平滑轮替TOR 0.983→1.000、打断TOR 0.935→1.000、打断评分4.684→4.790
- 关键对比：对基座10项轮替指标中6项提升（如打断评分+0.106），backchannel分布与基座接近；持续驱动的KAME各backchannel与打断指标明显退化，验证显式轮替奖励防止交互策略被破坏

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：首个系统性回答"全双工模型可否运行时受控"的工作，指令注入接口、Actor-Director协同与GDPO多奖励配方组合具备明确新颖性，对用户模拟器场景实用价值高。实验覆盖200场景、对比GPT-Realtime/KAME/Raon等多组基线并双基准验证；但SimIF-Bench主结果仅以图呈现、正文缺具体数值与消融，故定为实质贡献。

## [11] 10. Selective Listening: Mechanism-Guided Control of Audio Influence in Large Audio-Language Models

**arXiv ID**：2610.11196 | **方向**：语音大模型

**作者**：Yulin Sun, Kele Xu, Yong Dou

**机构**：国防科技大学计算机学院；复杂关键软件环境全国重点实验室

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11196 | **PDF**：https://arxiv.org/pdf/2610.11196.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对LALM在纯文本推理任务中受任务无关音频干扰、且聚合准确率会因修复与损害相消掩盖单样本决策漂移的问题，论文提出配对漂移分析（Influence Rate/Answer Flip）与机制引导的指令条件音频通路门控ICAP-Gate：离线定位各模型干预敏感的晚期音频通路，推理时按指令是否显式需求音频将其输出乘以模型特定衰减系数λ（0.10-0.25）或保持原样，每查询仅一次生成。在4个LALM、ARC与MMLU、环境声与自然语音干扰共16个全量设置上，IR与Answer Flip均低于无门控；ASR的WER与无门控完全一致。

### 🔧 技术方案

**问题背景：**LALM中模态可用不等于任务相关：环境声或无关语音可改变文本推理决策，而净准确率把正确→错误与错误→正确的转移相消，掩盖个体漂移；既有缓解（提示、多采样Self-Consistency）作用于输入层或输出层，无法定位并控制模型内部影响音频的因果通路。

**模型架构：**免训练方法，部署于Qwen2.5-Omni-7B/3B、Phi-4-MM（5.6B）、Voxtral-Mini-3B四个现成LALM。ICAP-Gate作用于机制定位出的晚期音频通路模块并对模块输出施加门控：z̃_ℓm = g(I)·z_ℓm，其中Qwen-7B/3B取audio_tower.layers.25（归一化深度0.81，26/32层）、Phi-4-MM取audio_embed.encoder.encoders.23（1.00，24/24）、Voxtral取audio_tower.layers.30（0.97，31/32）；门控g(I)∈{1, λm}，λm为离线校准的模型特定衰减系数（Qwen 0.25、Phi 0.10、Voxtral 0.25）。

**核心创新：** (1) 配对漂移度量：将准确率差拆解为方向性转移，定义IR=（干净对→错+干净错→对）/N与Answer Flip（含错答互换），揭示聚合Acc几乎不变时个体决策大量移动的隐藏失败模式。 (2) 机制引导通路定位：以通路缩放、模块级消融（z̃ℓ=α·zℓ, 0≤α≤1）及NetC2W/NetAnswer配对转移与金标答案logit margin分析，在Qwen2.5-Omni因果定位干预敏感晚期音频通路，并在三类异构架构中复现同类控制点，区别于仅凭激活幅度的解释。 (3) 指令条件门控：仅解析任务指令中的显式音频需求指示r(I)∈{0,1}（不做问题正文词法匹配），需求时保持通路开放（g=1）否则衰减（g=λm），单次生成、免clean参考路径、免辅助相关性模型，实现"抑制无关影响+保留ASR能力"。

**训练策略：**推理期方法，无参数更新、无训练损失；(ℓm, λm)由离线pathway scaling干预校准得到，在线仅需一次指令路由决策与一次临时通路缩放；Qwen用确定性解码，Voxtral用nucleus T=0.2、p=0.95、max_new_tokens=1024，clean/无门控/ICAP三条件共用同一解码配置；ASR侧效果每模型用400条LibriSpeech dev-clean语料评测。

### 📊 实验结果

**数据集**：ARC-Challenge全量1,172题、MMLU测试集14,042题；FSD为FSD50K真实环境声配对，SIB为LibriSpeech dev-clean随机配对的5秒16kHz单声道自然语音（2,694条唯一语音、40/97章节覆盖）；ASR侧效果用每模型400条dev-clean语音。

**主要指标**：
- IR（无门控→ICAP）：16个全量设置点估计全部下降，如Qwen2.5-Omni-7B MMLU-SIB 13.65%→11.19%（降2.46pp），Voxtral-Mini-3B MMLU-SIB 28.41%→25.88%（降2.53pp），Phi-4-MM MMLU-SIB无门控最高达30.00%
- Answer Flip：7B MMLU-SIB 18.89%→15.58%（降3.31pp），3B MMLU-SIB 25.17%→20.65%（降4.52pp），NetC2W与NetAnswer恢复最多+303/+635
- ASR WER（%）：ICAP与无门控完全一致（17.74/60.82/2.45/16.72），固定抑制升高16.28-123.76pp（Qwen-7B升至98.60）
- 路由审计：240个硬案例中指令级路由0/40误报（全文匹配40/40误报），显式音频请求40/40正确开路
- 关键对比：vs缓解提示，4个设置IR/Flip均更低，MMLU-SIB分别低8.87/11.76pp（配对95%CI不含零）；vs 8样本Self-Consistency，SCS漂移略低（最多-2.99pp）但延迟为无门控7.03-9.22倍，ICAP仅0.89-1.06倍

**是否开源**：暂无（仅提供匿名补充代码存档）

### ⭐ 评分：7/10
评分理由：提出"模态可用≠模态影响"的机制引导任务条件控制范式，概念新颖且闭环完整；配对漂移度量直击聚合指标盲区，4模型×16全量设置加ASR保持、路由审计与配对bootstrap统计，证据充分、可复现性文档详尽。不足在于可控通路限于单一模块、部分模型（Phi-4-MM ARC）收益有限；SIB仅随机5秒片段，语义相似/多说话人等更真实干扰留待未来；漂移控制弱于多采样Self-Consistency；代码未公开。

## [12] 11. Beyond Speech Captions: Speech-Rewarded Style Planning for Conversational Text-to-Speech

**arXiv ID**：2610.11461 | **方向**：语音大模型

**作者**：Shiao Zhu, Lianbo Liu, Sizhen Lyu, Yuzhe Wang, Sheng Li, Takahiro Shinozaki

**机构**：Institute of Science Tokyo, Independent Researcher（Tokyo, Japan）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11461 | **PDF**：https://arxiv.org/pdf/2610.11461.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
会话式TTS依赖自然语言风格描述衔接LLM推理与可控合成，但描述式伪标签监督与下游声学控制有效性脱节。本文提出SRSP框架，以冻结CosyVoice3 TTS对目标语音token的teacher-forced似然作为奖励，用GRPO训练Qwen3.5-9B风格规划器，无需目标风格caption。在ISCSLP 2026 CoT-TTS英文子集上，SRSP五项下游声学指标全面优于Base LLM与目标音频辅助captioning基线：S2S达0.3632，MCD-DTW降至5.9569（test_in），Gemini盲测在语境恰当性与参考一致性上全胜。

### 🔧 技术方案

**问题背景：** 现有工作（如Chain-Talker）以语音captioner（StyleCap/SECap/AlignCap）的描述文本作为伪标签训练风格规划器，但目标声学细节被压缩进文字而丢失；更关键的是预测目标描述与为特定合成器生成有效指令是两个不同目标，准确描述未必诱导最接近目标的声学实现。作者实证表明CLAPScore等语音-文本对齐分数与下游声学相似度近乎零相关，按T2S选指令与随机无异。

**模型架构：** 整体为"风格规划器+冻结下游TTS"管线。规划器基座为Qwen3.5-9B（LoRA微调），输入文本对话历史H与响应文本y，输出单句英文风格指令z；z与y、同说话人prompt音频p共同条件冻结的Fun-CosyVoice3-0.5B（自回归LLM+声码器）合成语音。推理时仅需(H,y)，目标语音token s仅在训练期用于构造奖励，不进入规划器输入。

**核心创新：** (1) 提出语音token似然奖励：对每个候选指令zi，冻结TTS的自回归LLM在目标语音token序列上计算teacher-forced平均交叉熵，取负值为奖励Ri=−LTTS(zi)−Pi，使规划器直接优化合成器实际声学输出而非描述一致性；同组候选共享(y,s)，相对损失差直接度量各指令对同一目标的差异化控制效果。 (2) 以GRPO完成免caption规划器训练：每样本采G=8条指令，组内奖励标准化得优势值，配合clip目标与对参考策略的KL约束更新策略，无需任何目标风格描述标注。 (3) 给出描述对齐弱代理的候选级证据：8条候选指令的句内Spearman相关显示T2S与S2S/情感相似度/MCD近零相关；AF-Next基线T2S全最高但五项下游指标全垫底，反证合成感知反馈的必要性。

**训练策略：** Qwen3.5-9B在全线性层做rank-16 LoRA（α=32，dropout 0.02）；GRPO训练1个epoch，G=8，学习率2×10⁻⁶，clip η=0.2，KL权重β=0.075，TRL 1.3.0默认token级重要性采样加DAPO式损失归一化；采样温度训练1.3、测试0.7。辅助惩罚：指令短于6词罚5、6-11词罚0.5，重复二元/三元组按0.01罚（每worker滚动2048条历史）。每实例随机采0-3条CosyVoice风格示例作in-context演示（组内共享），推理采2条。数据规模：277.60小时英文训练语料。

### 📊 实验结果

**数据集**：ISCSLP 2026 CoT-TTS语料英文子集（总池299.75小时，筛选条件：时长3-15s、活跃语音比≥0.70、响度≥-40dBFS、转写≤300字符、参考相似度≥0.65、自然度≥3.0、噪声分≥3.5）；训练277.60小时；dev_in/test_in按整场景留出、dev_out/test_out按整部电影留出，各2750句（约5小时）。

**主要指标**：
- S2S(ParaCLAP-C)：SRSP 0.3632/0.3627，Base LLM 0.3166/0.3220，AF-Next 0.2874/0.2982（test_in/test_out）
- S2S(CLSP)：SRSP 0.8329/0.8296，Base LLM 0.8150/0.8146
- 情感相似度(emotion2vec)：SRSP 0.6417/0.6269，Base LLM 0.6124/0.5927
- MCD-DTW：SRSP 5.9569/6.1637，Base LLM 6.3395/6.5072
- Gemini盲测胜率：SRSP对Base LLM语境恰当54.19%/53.67%、参考一致60.91%/57.75%
- 关键对比：较Base LLM，S2S(ParaCLAP-C)提升+0.0466/+0.0407、情感相似度+0.0293/+0.0342、MCD降低0.38/0.34；且全面优于可直接使用真实目标音频的特权captioning基线AF-Next与Qwen3-Omni；40项下游对比中38项Wilcoxon+Holm检验显著（p<.05）

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：以冻结TTS的目标语音token似然作GRPO奖励、免caption训练风格规划器的思路清晰且有新颖性，辅以T2S弱相关的候选级实证，动机扎实；实验覆盖双分区、五项声学指标与LLM表达力盲评，统计检验充分。但方法绑定CosyVoice3单一后端、奖励计算与合成同源，缺乏人类听感验证，且未开源代码，相关似然奖励与GRPO已有先例，故为实质贡献而非突破性工作。

---

## [13] 语音前端

## [14] 12. SepGen: Multi-Stem Audio-Video Separation and Generation in a Single Model

**arXiv ID**：2610.11361 | **方向**：语音前端

**作者**：Aviad Dahan, Rajaei Khatib, Yonatan Bitton, Idan Szpektor, Lior Wolf, Raja Giryes

**机构**：特拉维夫大学、Google

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11361 | **PDF**：https://arxiv.org/pdf/2610.11361.pdf | **代码**：https://sepgen.github.io/ | **Demo**：https://sepgen.github.io/

### 📌 简介
现有联合音视频生成器只输出一条混合声轨，声源无法被单独编辑或在新视角下空间化重渲染。SepGen将预训练LTX-2.5 22B音视频生成器扩展为多stem模型，一次采样同时输出视频、混合轨与每个声源一条波形，同一套权重通过噪声水平切换生成/分离双模式。在Veo基准分离上Judge 4.36、J-swap 2.61、语音自台词WER 0.05（去除台词后仍0.50领先全部基线）；129个带参考stem场景上包络相关0.82、LSD 6.39dB全面第一。

### 🔧 技术方案

**问题背景：** 现有联合音视频生成器（LTX-2、Ovi、Veo 3.1 Lite）只输出整场景一条audio-mix，声源不可移动、删除或单独重渲染，4D场景换视角重渲染时没有任何可交给空间音频渲染器的逐源波形。语言查询分离器（AudioSep、FlowSep、SAM Audio）逐条caption独立处理，同一类别两个说话人时可能两次返回同一个人。

**模型架构：** 在冻结的LTX-2.5 22B双流flow-matching Transformer上，把每条stem的VAE latent沿token轴拼在audio-mix后面构成za=[zs1|zs2|zm]，各通道保持预训练时序位置、共享旋转位置编码实现时间对齐。stem token可自注意力、互注意、注意audio-mix与视频，但只注意自己的caption（块对角路由）；audio-mix只注意自己与场景caption，视频与mix均不注意任何stem，信息单向从场景流向stem。audio-mix是"保护通道"：其token上的LoRA增量被门控置零（g_j=1[j∉J_m]），配合注意力掩码Λ，实验验证开关适配器后mix与视频逐层bit级一致。

**核心创新：** (1) 多stem单模型输出：stem作为音频流附加通道与mix联合去噪，各stem跟随自己caption并共享场景时间轴，单次采样输出视频+mix+逐源波形；保护通道与单向信息流保证预训练输出不被扰动，消融显示独立两遍生成会崩溃（Judge 4.07→2.43、WER 0.09→1.05）。 (2) 噪声水平选模式：去噪基座中分离保持观察mix零噪声、生成则与stem共同去噪；推理σk≤σg=0.97后stem改注意当前步mix的干净估计ẑ0,m（Estimated Separation），Stage2按30%干净/其余σm=min(σm′,σs)覆盖两种噪声态，单checkpoint双模式且互不退化。 (3) 跨stem注意力引导CSAG：在caption交叉注意力内以兄弟caption为负支路施加归一化注意力引导NAG（λ=2、τ=2.5、α=0.5），抑制两stem内容互相泄漏，比单纯块对角路由更有效。

**训练策略：** 冻结LTX-2.5 22B基座（int8量化），只训练音频流LoRA（rank 128、480模块、327M参数）。数据为4843条双声源样本（CelebV-HQ 1658、URMP 1437、自生成749、VGGSound×MUSIC-21跨视频合成999），语义/位置/简短三级caption每步随机抽取；损失为flow-matching速度MSE，仅supervise stem token。Stage1分离12000步（σm=0），Stage2续训3000步生成；AdamW、batch size 1、学习率1e-4线性衰减、bfloat16、单卡A6000，片段113帧@25fps、768×512。

### 📊 实验结果

**数据集**：生成基准194条双源prompt（134音效+60双人对话，4.5s）；Veo基准149个Veo 3.1 Lite渲染场景（104音效+45语音，48kHz立体声，取前5.7s评分）；LTX-2.3基准64条（5s）；SAM-Audio-bench 172条真实录音（乐器55音效48说话人，10s窗口）；参考stem评估129个留出场景（258条stem）

**主要指标**：
- 语音分离（Veo）：SepGen自台词WER 0.05（含台词）/0.50（去台词）vs AudioSep 0.93/1.03、FlowSep 0.98/0.99；说话人余弦0.61/0.53 vs 基线0.89–0.96（越低越 distinct）
- 音效分离（Veo）：Judge 4.36 / J-swap 2.61 / C-swap 0.23 vs AudioSep 3.46/1.60/0.16、SAM large 3.14/0.50/0.04
- 真实录音（SAM-Audio-bench）：Judge 3.70 / J-swap 1.52 vs SAM large-tv 3.12/0.78、AudioSep 2.81/0.82
- 联合生成（joint run）：Judge 3.82 / J-swap 2.07 / WER 0.07 / 说话人余弦0.66全第一；self-separation二次分离Judge 4.21、J-swap 2.29
- 波形级（129参考场景）：包络相关0.82 / LSD 6.39dB vs AudioSep 0.76/11.0dB、SAM large 0.39/18.9dB
- 用户研究：分离偏好0.58 vs SAM Audio 0.25（真实录音0.64 vs 0.20）；生成0.63 vs AudioSep 0.28（语音0.87 vs 0.10）
- 关键对比：语音上SepGen自台词WER比最强级联基线AudioSep低0.88（0.05 vs 0.93，含引用台词）；去掉台词后0.50 vs 1.03领先保持（90条中仅4-5条stem变静音）；专用语音分离器SepFormer仅在去台词设定下接近

**是否开源**：代码、checkpoints与数据集已开源 @ https://sepgen.github.io/

### ⭐ 评分：8/10
评分理由：首个把预训练联合音视频生成器改造为多stem生成/分离双模式框架，噪声水平切模式、保护通道与CSAG设计精巧且消融充分；四类基准加用户研究、显著性检验与波形级验证，全面胜过级联与专用语音分离器并完全开源。局限是固定2个stem且未端到端验证4D空间渲染，故给8分。

## [15] 13. SEER: Source-Conditioned Emotion Enhancement via Retrieval for Cochlear-Implant Speech

**arXiv ID**：2610.11131 | **方向**：语音前端

**作者**：Hsing-Hang Chou, Yun-Shao Lin, Ching-Chin Sung, Chi-Chun Lee

**机构**：国立清华大学电机工程学系；中研院资讯创新研究中心（台湾）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11131 | **PDF**：https://arxiv.org/pdf/2610.11131.pdf | **代码**：https://github.com/HenryChou36/SEER | **Demo**：https://github.com/HenryChou36/SEER

### 📌 简介
CI语音丢失F0等情感线索，听者情感识别显著退化，而现有CI情感增强依赖正常/强情感平行录音与强度标签。本文提出SEER，一个源条件检索框架：以Maestro-EVC参考条件情感语音转换为基座，用CI-aware奖励学习效用评分器，为每个源语音挑选同情感参考使CI处理后仍可识别，并以LinUCB式不确定性探索避免穷举配对评估，无需平行录音与强度标签。RAVDESS/ESD上N8源macro-F1分别提升7.30/11.66分，16人听测各条件均显著提升，且可懂度损失小于固定参考法。

### 🔧 技术方案

**问题背景：**电听觉无法有效传递F0线索，CI-vocoder语音的情感识别准确率下降，CI用户易给出Neutral判断，SER模型在CI模拟下同样退化。以往JD-NMF增强需同一说话人、同一句子的正常/强情感平行录音及显式强度标注，难以迁移到通用类别情感语料，且穷举源—参考转换评估代价随语料规模快速增长。

**模型架构：**先构建参考池：仅当预训练Emotion2Vec+ Large对录音的原始版与CI模拟版均判对目标情感时才入库（RAVDESS 281条/ESD 6630条）。源侧用Transformer时序编码器聚合Maestro-EVC情感编码器输出为h_x∈R128并接辅助情感分类器；参考侧由2064维描述子（情感嵌入均值/标准差、平滑mel能量帧与平均归一F0的统计量、清音帧比例、时长）投影为h_r∈R128；评分器对[|h_x−h_r|; h_x⊙h_r]输出预测效用û，其中64维中间表示z_θ复用于探索；推理仅选正分参考否则保留源。探索借鉴Neural-LinUCB浅层探索：z_θ归一化后加偏置得ψ_θ∈R65，维护单位岭矩阵V（α=1，历史至多16384个唯一配对），按取a=û+α√(ψ⊤V⁻¹ψ)最高的每源前4个参考做转换，与原始基线一并评估生成奖励目标。

**核心创新：** (1) CI-aware源相对效用奖励：用Emotion2Vec+对转换输出与源在CI前后评分，定义u(x,r)=c(x̃_r)−c(x)+0.1·[q(x̃_r)−q(x)]，指示项c给出+1修复/−1损伤信号，q再叠加CI后置信度，把"CI处理后是否仍可识别"直接编码为监督信号。 (2) 源条件效用检索器：联合学习源/参考隐空间与成对评分器，从少量采样转换结果推断"哪个参考对哪个源有益"，回避O(N×M)穷举转换评估，使通用类别情感语料可直接用作参考库。 (3) 不确定性引导参考探索：LinUCB式获取函数在采样时平衡预测与不确定性，避免贪心查询固化早期偏置，最终检索仅用预测效用保证在线可用。

**训练策略：**RAVDESS/ESD均限定Angry/Happy/Sad；每数据集单独训练Maestro-EVC骨干（目标情感+Neutral+Surprise）；以22通道CI24式PSHC激励器的N8为优化目标（N4/N16仅测试），按验证N8 macro-F1选检查点。奖励权重τ=0.1，探索系数α=1，每源评估前4参考，岭矩阵V每16次更新重建，损失L=MSE(û,u)+CE(p_x,e_x)。

### 📊 实验结果

**数据集**：RAVDESS（24位演员，384/96/96按演员不重叠划分，参考池281条）；ESD英文（10位说话人，9000/600/900，参考池6630条）；CI模拟用22通道CI24 PSHC激励器（N4/N8/N16）。

**主要指标**：
- 源macro-F1：RAVDESS N8 78.26→85.56（+7.30）、N16 80.33→95.82（+15.48，显著）、N4 80.35→80.13（不显著）；ESD N4/N8/N16为58.71→68.23、57.09→68.75（+11.66）、70.46→82.06，三条件均显著
- WER（Whisper large-v3-turbo）：SEER较固定参考在所有条件下WER更低（RAVDESS N8 2.43%→1.39%、ESD N8 14.19%→10.00%），减少强制统一参考的可懂度代价
- 16人听测：主观macro-F1在N4/N8/N16为68.37/70.14/67.39，较Source（46.42/52.66/58.71）提升21.94/17.48/8.68分，Holm校正后均显著，超JD-NMF 1.68–7.17分
- 关键对比：客观上超JD-NMF达8.96–22.98分（全部6个数据—CI组合）；N8下Angry识别31.3%→82.0%、Neutral 42.2%→5.5%，但Happy/Angry与Sad/Neutral边界仍难分离

**是否开源**：代码与demo已开源 @ https://github.com/HenryChou36/SEER

### ⭐ 评分：8/10
评分理由：问题定位清晰，把参考选择形式化为源条件检索加分臂决策新颖，CI-aware奖励与LinUCB探索结合方法学扎实；客观+16人听测+三级激励条件与显著性检验齐备且开源。扣分在于仅三情感两数据集、客观评估依赖Emotion2Vec+而非真实CI听者，且RAVDESS N4客观增益不显著，泛化性待进一步验证。

## [16] 14. Disentangling Linguistic and Paralinguistic Information with Routed Sparse Autoencoders

**arXiv ID**：2610.10865 | **方向**：语音前端

**作者**：Beimnet Bekele Guta, Xiaoyu Yang, Guangzhi Sun, Philip C. Woodland

**机构**：剑桥大学工程研究所（Department of Engineering, University of Cambridge, UK）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.10865 | **PDF**：https://arxiv.org/pdf/2610.10865.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
自监督语音编码器把音素内容、说话人身份、情感、韵律等语言与副语言因子混在同一纠缠表征空间，难以对单个因子做选择性解读与修改。本文在冻结编码器之上构建TopK稀疏自编码器，用互补可学习路由掩码把稀疏码划分为语言/副语言双路由，配合路由特定任务监督与跨因子对抗。在SPEAR XLarge与WavLM Large上，独立探针显示语言路由强保留音素（PER 8.94%）、副语言路由高保留说话人（SID 99.8%）且跨因子可恢复性显著受抑，MSP-Podcast上模式保持，路由交换实现双分离。

### 🔧 技术方案

**问题背景：**自监督语音编码器同一激活同时携带音素、说话人、韵律、情感等信息，选择性移除或修改单一因子困难；已有稀疏自编码器仅分析自动发现特征，并不保证单元对应预选因子，难以施加显式解纠缠目标。

**模型架构：**冻结SSL编码器（逐层无参LayerNorm后均匀平均）输出帧级表征，经TopK SAE（K=5120，k=256）投影为过完备稀疏码，含L2重构与AuxK（预算64、权重1/32，用非活跃单元预测残差防死单元）。互补可学习掩码m_L+m_P=1将稀疏码划分为z_L与z_P（z_t=z_L+z_P），提供三种路由：学习路由（直通硬Gumbel-Softmax加L_routing决择损失）、固定路由（预定成员与独立预算k_L/k_P=240/16）、配额冻结（4000步学分配后按平均活跃度定配额转各路由独立TopK）。监督：z_L由PR-CTC监督，z_P由SID/情感（加权）分类与逐帧log-F0及能量MSE监督。对抗：音素对抗作用于z_P，说话人/情感/韵律对抗作用于z_L，经GRL梯度反转（-γ）实现互抑。

**核心创新：** (1) 将路由稀疏自编码器引入语音解纠缠，以互补掩码将SAE潜空间组织为语言/副语言路由，在保持重构的同时实现因子级选择读写，并给出固定与配额冻结两种变体权衡重构与选择性。 (2) 路由特定任务监督使每条路由与目标因子直接对齐，弥补"稀疏性本身无法恢复预选因子分解"的缺口。 (3) 跨因子对抗叠加独立后验探针与受控路由交换验证，证明路由是功能性而非仅统计性双分离，消融显示两类对抗互补抑制。

**训练策略：**编码器全程冻结，仅训SAE、掩码与任务头；数据为LibriSpeech train-clean-100（74音素词表，CMU词表加G2P回退）；K=5120、k=256、AuxK预算64权重1/32；固定路由K_L/K_P=4096/1024、k_L/k_P=240/16；训练12000步（WavLM配额冻结16000步）；损失=λ_recon·L_recon+λ_AuxK·L_AuxK+L_task+L_adv（学习路由另加L_routing）。

### 📊 实验结果

**数据集**：LibriSpeech（train-clean-100训练，dev-clean验证，test-clean测试）；MSP-Podcast（51,017句、700说话人、41,067/4,975/4,975划分，封闭SID随机水平0.143%）

**主要指标**：
- 语言路由保留（LibriSpeech）：z_L PER 8.94%（SPEAR配额冻结）/9.40%（WavLM配额冻结），z_L SID仅0.6%/14.8%
- 副语言路由保留：z_P SID 99.8%（两编码器），z_P PER升至80.26%（SPEAR）/80.84%（WavLM）
- 消融抑制：去掉对抗后z_L SID 6.2%→99.8%（固定），说明对抗是跨因子抑制关键
- 路由交换（250对，SPEAR）：PP交换自留音素99.57%且转移捐赠人说话人98.00%；LL交换替换为捐赠人音素94.26%且自留说话人96.00%
- MSP-Podcast跨语料迁移（不重训）：固定路由z_L/z_P PER 43.92/99.72%、SID 12.82/82.71%
- 关键对比：SPEAR/WavLM跨编码器一致——固定路由更抑制z_L副语言，配额冻结更抑制z_P语言且重构更均衡

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：路由掩码+路由监督+跨因子对抗组合优雅，独立探针与路由交换干预的评估设计严谨；因子选择性分离在两编码器、两语料、两路由变体上一致，说服力强。不足：监督任务限于PR/SID/情感/韵律，重构MSE明显上升（0.066→0.179），且缺下游端到端任务验证。

## [17] 15. Cross-Lingual Speaker Verification with Self-Supervised Pre-Trained Models

**arXiv ID**：2610.11099 | **方向**：语音前端

**作者**：Jinghan Peng, Yu Zheng, Weiqiang Wang, Jian Liu

**机构**：蚂蚁集团机器智能部（上海，Ant Group）

**发布日期**：2026-10-09 | **论文**：https://arxiv.org/abs/2610.11099 | **PDF**：https://arxiv.org/pdf/2610.11099.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
说话人验证在跨语言、语言失配场景下，因说话人身份与语言相关声学线索纠缠而性能显著退化。本文采用w2v-BERT 2.0自监督预训练模型（PTM）作为前端特征提取器，经逐层Adapter投影与多尺度特征聚合并经ASPPooling输出256维说话人嵌入，配套三阶段训练范式与QMF分数校准及多系统融合。团队T02在TidyVoice2026基准上取得tv26_eval-A EER 2.21%、tv26_eval-U EER 2.99%，在全未见语言集上较ReDimNet基线优约0.6个百分点，验证了PTM前端的跨语言泛化优势。

### 🔧 技术方案

**问题背景：** 当注册与验证发生在不同语言时，说话人身份被语言相关声学特性混淆，交叉语言SV精度明显下降。已有PTM基SV工作多在VoxCeleb等同域基准上验证PTM前端有效性，尚缺面向全跨语言、含未见语言评测场景下对PTM选型、特征聚合与训练策略的系统性研究。

**模型架构：** 输入log-Mel特征送入w2v-BERT 2.0（580M参数、143种语言）SSL骨干，抽取全部层隐表示；每层经独立两层MLP Adapter投影至统一256维；多尺度聚合模块考察平均、层加权、通道加权、通道拼接、时间拼接、层次交叉注意力六种融合方式，最终采用通道拼接（无新增参数且EER最优）；帧级特征经ASPPooling得到固定维utterance表示，再投影为256维说话人嵌入，以AAM-Softmax损失训练。对照与融合用轻量ReDimNet-B5（9.2M）/B6（15M），输出192维嵌入、SF2-C损失，最终对各系统QMF校准后分数取均值融合。

**核心创新：** (1) 构建PTM跨语言SV管线：以w2v-BERT 2.0多语言无标注预训练知识学习语言无关说话人表征，解耦说话人身份与语言特定特征，实证其在完全未见语言测试集上显著优于同数据训练的传统ReDimNet前端。 (2) 系统消融多尺度特征聚合：对比六种层融合机制，通道拼接以最简结构取得最低EER（2.09%对平均融合2.21%），层次交叉注意力minDCF最优（0.648），给出低开销工程选型依据。 (3) 提出三阶段渐进训练范式：冻结骨干训练下游、全参数微调、目标域LM-FT大边距精调逐级验证，并叠加分数级融合，在评测集上取得团队提交系统中最好成绩。

**训练策略：** PTM对比：w2v-BERT 2.0显著优于Whisper-Large-v3（3.15%）、XLS-R-300M/1B/2B（2.94%/3.10%/3.10%）、MMS-300M/1B（3.27%/3.46%），dev EER为2.09%。数据：TidyVoiceX_Train（3666人/40语言）+VoxCeleb2（5994人）+VoxBlink2（111284人）+CN-Celeb1&2（2793人）+WenetSpeech过滤集（35285人）+3D-Speaker（10000人）。阶段：①冻结骨干60epoch、2s片段、batch 16384、margin 0→0.2（epoch20-30）、LR 0.1→5e-5；②解冻PTM 20epoch、margin 0.2、LR 1e-4→1e-6；③仅在TidyVoiceX_Train上LM-FT 6epoch、6s片段、margin 0.5、batch 512。AdamW（weight decay 2e-5）；增强概率：混响0.3、音乐0.1（SNR 5-15dB）、噪声0.1（0-15dB）、babble 0.1（10-30dB），无变速。

### 📊 实验结果

**数据集**：训练集为TidyVoiceX_Train（3666说话人、40语言）及VoxCeleb2、VoxBlink2、CN-Celeb1&2、WenetSpeech、3D-Speaker等多语语料；TidyVoiceX_Dev（808人、1200万trials）用于开发与阈值校准；评测TidyVoiceX2，tv26_eval-A为部分语言失配，tv26_eval-U为注册与测试均为38种训练/开发中完全未见语言。

**主要指标**：
- tv26_eval-A（部分语言失配）：融合系统EER 2.21%，minDCF 0.1797
- tv26_eval-U（全未见语言）：融合系统EER 2.99%，minDCF 0.2045
- 单系统：w2v-BERT2.0+QMF 2.73%/2.84%；ReDimNet-B6+QMF 2.52%/3.43%
- PTM消融（dev）：w2v-BERT2.0 2.09%，较XLS-R/MMS/Whisper系列优0.85-1.37个百分点
- 关键对比：eval-U上PTM系统较ReDimNet-B6低0.59个百分点，未见语言泛化更强；融合系统较最佳单系统优0.31/0.44个百分点（A/U集）

**是否开源**：暂无（论文未提供代码链接）

### ⭐ 评分：7/10
评分理由：方法本身组合PTM前端、Adapter投影、多尺度聚合与三阶段训练等成熟组件，无突破性创新；但实验体系完整，PTM选型、聚合方式、训练阶段消融充分，且在新型跨语言基准TidyVoice2026上实证w2v-BERT 2.0优于传统前端，EER 2.21%/2.99%有实用参考价值，属扎实增量工作。

---

## [18] 其他论文（未进入前 15，仅列标题）

16. **Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners** | 语音大模型 | arXiv: 2610.10868 | 评分：7/10 | https://arxiv.org/abs/2610.10868

17. **Local Prototype Reconstruction for Text-Compatible Speech-to-LLM Bridge Pretraining** | 语音大模型 | arXiv: 2610.11159 | 评分：7/10 | https://arxiv.org/abs/2610.11159

18. **Towards Automated Clinical Behavioral Coding with Large Language Models: A Case study Using BOSCC recordings of Children** | 语音大模型 | arXiv: 2610.11106 | 评分：6/10 | https://arxiv.org/abs/2610.11106

19. **Monaural Continuous-Radius Regional Speech Extraction with Cross-Radius Consistency Learning** | 语音前端 | arXiv: 2610.11507 | 评分：7/10 | https://arxiv.org/abs/2610.11507

20. **Toward accurate speaker inventories for online speaker diarization** | 语音前端 | arXiv: 2610.11278 | 评分：7/10 | https://arxiv.org/abs/2610.11278

21. **Using the enrollment gallery as evidence: affine-invariant score calibration for target speaker tagging** | 语音前端 | arXiv: 2610.11272 | 评分：7/10 | https://arxiv.org/abs/2610.11272

22. **Detection-Guided Adaptive Purification with Diffusion Models for Robust Audio Deepfake Detection** | 语音前端 | arXiv: 2610.10752 | 评分：7/10 | https://arxiv.org/abs/2610.10752

23. **Self-Supervised Speech Representations for Cross-Speaker Dysarthria Detection During Awake Craniotomy** | 语音前端 | arXiv: 2610.11825 | 评分：7/10 | https://arxiv.org/abs/2610.11825

---

*Generated on 2026-10-09*
