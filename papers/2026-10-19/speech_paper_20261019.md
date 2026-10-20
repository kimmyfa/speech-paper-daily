# 2026-10-19 语音论文速递

**共收录**: 17 篇 | **语音大模型**: 12 篇 | **语音前端**: 5 篇

> 目标日期 2026-10-19（北京时间）arXiv 语音相关论文共命中 17 篇。
> 以下是按评分排序的结果。

### 速递说明

本批次精选前 15 篇进行完整模板精读，按评分由高到低排序；其余 2 篇论文仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），未展开精读。

---

## Jarvis: Coordination Deserves a Brain of Its Own in Agentic Interactive Models

**arXiv ID**：arXiv:2610.23804 | **方向**：语音大模型

**作者**：Yuxiang Wang, Shengbo Cai, Zhixian Zhao, Yingda Shen, Zhizheng Wu 等（共10人）

**机构**：香港中文大学（深圳）、腾讯混元、Amphion Technology

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.23804 | **PDF**：https://arxiv.org/pdf/2610.23804.pdf | **代码**：暂无 | **Demo**：https://amphionteam.github.io/Jarvis-Demo/

### 📌 简介
全双工语音模型把复杂推理外包给后台慢脑，任务运行时用户可随时细化、取消或替换请求，计划与结果随之过期，而前台只跟对话、后台只知自身任务，无人同时看到两边。论文提出协调框架Jarvis，遵循"模型判断、代码执行"：类型化决策模型JEV把每轮话语对照活动任务台账选操作，运行时校验版本后才生效。同前后端的受控对比下，τ-Voice任务解决数从29/278升至192/278；FDB-v3上以开源9B前端达69% Pass@1，超GPT-Realtime的60%。

### 🔧 技术方案

**问题背景：** 快慢脑分工带来协调时序问题：前台听得到每句话却看不到任务版本，后台了解任务却不跟随对话，导致过期送达、错误绑定、幽灵执行、虚假交付等六类失败，与识别和推理质量无关。

**模型架构：** Jarvis-Audio架于Venus-Audio 9B：Native Gate在Thinker的q/v/o加rank-8 LoRA共6.2M参数，按1秒音频单元从原生控制token读LISTEN/DIRECT/DELEGATE三路策略；Qwen3-ASR-1.7B绑定真实转写；JEV对台账实时生成的选项返回类型化分布；worker为DeepSeek-V4-Flash异步工具循环；Delivery以生成epoch与播放回执判定交付。Jarvis-Omni改用Jev-Omni 12B（Gemma 4基座、256路决策头），增Evidence Timeline与带有效期的Belief State。

**核心创新：** (1) JEV从不自由生成文本，选项由运行时按台账生成并绑定如REFINE:T2:3的任务版本，执行前校验live版本，旧版本选择自动作废，低置信交worker走ANSWER兜底。(2) Gate只学"何时移交"：在264条中英合成场景语音上以GRPO做四阶段课程训练，留出集首次放行98.8%正确、中位延迟0.16秒。(3) Done≠delivered：音频块带epoch，完整播放回执才置DELIVERED，停播不取消任务；Omni为视觉claim设有效期，播放前与播放中复查，过期即丢弃或掐断。

**训练策略：** GRPO每前缀采样8动作、组内归一化奖励，clipped策略梯度加KL0.03，末阶段4111新前缀加1056回放训800步；电话信道为8kHz重采样加G.711与15/9dB噪声；Omni gate用49局录音1211条episodes训两轮各3000步。

### 📊 实验结果
**数据集**：τ-Voice 278个任务（航空/零售/电信）、FDB-v3（100条真实录音）、FDB-v2（200多轮任务）、ContextDialog（80问）、80脚本竞态集

**主要指标**：
- τ-Voice同前端同后端仅换harness：192/278 vs QAA 29/278，提升逾6倍
- FDB-v3 Pass@1：69.0%，高于GPT-Realtime（60.0%）与原生Venus-Audio（48.0%）；Tool F1 0.927、打断率7%全表最低
- τ-Voice公开榜macro：69.2%，超全部实时语音系统
- FDB-v2任务分（1-5）：3.36 vs QAA 2.57
- JEV一秒内过阈正确率91.0%，两个LLM控制器均为0%；竞态一致性240/240；ContextDialog均分4.41 vs QAA 1.45

**是否开源**：Jev-Omni权重已发布@ huggingface.co/akhilaaa3/Jev-Omni，代码暂无

### ⭐ 评分：9/10
评分理由：首次把快慢脑协调识别为独立问题，版本化台账、类型化决策与播放回执的机制设计原创；同前后端仅换harness的受控实验说服力极强，开源9B前端多基准超越闭源实时系统，视觉实例验证设计可迁移性。不足是JEV训练细节未公开、视觉队列绝对正确率偏低。

---

## ConvexLLM: Scaling Convex-Hull Speech Interfaces to General-Purpose Audio Intelligence

**arXiv ID**：arXiv:2610.23539 | **方向**：语音大模型

**作者**：Ming-Hao Hsu, Shujie Liu, Yuxuan Hu, Yuxiang Wang, Yingda Shen, Jinyu Li, Zhizheng Wu

**机构**：香港中文大学（深圳）数据科学学院、微软研究院（雷德蒙德）、微软亚洲研究院

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.23539 | **PDF**：https://arxiv.org/pdf/2610.23539.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
通用语音音频大模型通常以MLP/Q-Former把声学特征无约束映射到解码器输入空间，迫使文本预训练解码器重新学习解释该表征并损失语言能力。ConvexLlm用C-Gate接口把每个音频位置表示为冻结文本嵌入的连续凸组合：路由词表top-16行并以非负归一权重加权求和，输出恒在文本嵌入凸包内。模型由Whisper-large-v3编码器与Qwen3.5-9B解码器组成，经三阶段多任务训练加文本教师蒸馏，仅用不到0.27M小时适配数据，取得VoiceBench十一任务75.36（对比开源模型最高）、MMAU 62.50%；2B对照中C-Gate语音Overall 60.35优于MLP 58.80与Q-Former 54.19，书面语音差距仅2.86分。

### 🔧 技术方案

**问题背景：** MLP/Q-Former投影器输出可落在文本嵌入表凸包之外的无约束向量，解码器适配语音时需重学解释新输入分布，常退化推理与指令遵循等文本能力；LegoSLM等词表接口虽更贴近文本空间，但此前仅在ASR、情感识别等受控任务验证，未支撑覆盖语音交互、推理、识别与非语音音频理解的通用模型。

**模型架构：** 声学编码器Whisper-large-v3、时间平均池化（stride 4）后接入C-Gate，再接Qwen3.5-9B解码器（对照实验用2B）。C-Gate为对词表的单次注意力查表：查询投影（仿射+LayerNorm+dropout 0.1）以路由维度512产出每帧query，学习线性映射把冻结文本嵌入行投影为key，用可学习路由温度（初始1.0）打分取top-16，再经固定混合温度0.7的softmax得非负归一权重，加权求和冻结value嵌入；输出填入解码器音频位置与嵌入提示相邻，自回归生成文本。文本嵌入表与LM头全程冻结，2B三接口参数量约1.706M。

**核心创新：** (1) 凸包约束接口：音频表征恒为冻结文本嵌入的凸组合，训练全程给解码器稳定的文本参照；诊断显示C-Gate输入能量28.4%分布于文本嵌入前100主方向，远高于MLP的8.8%与Q-Former的4.9%，且表征范数从首个解码块起即与文本尺度（0.65）一致。(2) 双温度top-k凸路由：路由温度可学习但只影响选择次序，混合温度决定权重锐度，支持大小K是容量旋钮；K=1时需直通估计器且模型崩溃（WER 86.48/88.65、Overall 22.30），K≥4才可用；词表按2048行分块打分再归并top-k以省显存。(3) 文本教师蒸馏与文本回放：对有书面对应的音频样本，用冻结的原Qwen3.5-9B读文本、音频条件模型匹配其每个响应位置的next-token分布（蒸馏温度1.0），配合约15%文本回放与分阶段解冻在获得语音能力的同时保留语言能力。

**训练策略：** 三阶段：Stage1仅训接口（编码器与解码器冻结，有效batch 2048，5000-7000更新）、Stage2加训编码器（7000）、Stage3联合微调解码器块（9B在7500更新评估，batch 512）。损失为响应token教师强制交叉熵，9B Stage3对含文本对应音频改用KL蒸馏；Stage3第5000更新把转录采样比20%提至35%、ASR衍生指令10%提至15%。9B用16×H100、weight decay 0.01、最小学习率比0.1、warmup 200更新；2B对照Stage1/2/3为5000/7000/18000更新、Stage3余弦调度batch 256、8×H100、纯CE、dropout 0.1；输入截30秒，数据池57.2M音频标注+0.44M文本，适配音频上界0.271M小时。

### 📊 实验结果
**数据集**：VoiceBench十一子集（GPT-5.4判分1-5乘20折算）、MMAU Test-mini（1000题）、LibriSpeech test-clean/test-other；训练用MLS/GigaSpeech/LibriSpeech/Emilia/CommonVoice/FLEURS英文、WavCaps/Clotho/MusicCaps、合成口语指令推理与文本回放。

**主要指标**：
- VoiceBench Overall：75.36，高于MiniCPM-o 4.5的73.04、Kimi-Audio的70.26、MiMo-Audio的67.01
- 知识与推理：OBQA 90.33、MMSU 72.32、SpMMLU 73.42、BBH 80.40（BBH超次优MiMo-Audio 71.60达8.80分）
- MMAU平均：62.50%（声65.77/乐60.78/语音60.96），低于MiMo-Audio 76.63达14.13分
- LibriSpeech WER：2.39%/5.07%，优于MiMo-Audio 3.19%/6.40%但逊于Kimi-Audio 1.40%/2.59%
- 2B对照语音/文本Overall：C-Gate 60.35/63.20、MLP 58.80/62.72、Q-Former 54.19/61.63（Base文本60.55）；语音-书面差距C-Gate 2.86最小
- 支持大小消融：K=4总体58.99、K=16（默认）60.35、K=64达61.53但MMAU由59.40降至58.50

**是否开源**：正文与附录未给出代码或演示链接，暂无。

### ⭐ 评分：8/10
评分理由：把声学表征约束为冻结文本嵌入凸组合是接口架构层面的新颖路线，贡献不在刷分而在用文本主方向能量、表征范数尺度三类诊断解释模态差距机制，证据链完整；仅0.27M小时训练即夺VoiceBench综合第一，数据效率显著。局限为MMAU与ASR仍落后大数据模型、2B对照仅单模型单配置且未开源降低可复现性，整体属有实质贡献的高水准工作。

---

## Bridge, Distill, Refine: High-Fidelity One-Step Generation for Multi-Bandwidth Speech Extension

**arXiv ID**：arXiv:2610.22910 | **方向**：语音前端

**作者**：Zhiqi Ai, Xu Shen, Mou Wang, Yongjin Zhou, Shugong Xu

**机构**：上海大学、OPPO、西交利物浦大学、早稻田大学

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.22910 | **PDF**：https://arxiv.org/pdf/2610.22910.pdf | **代码**：暂无 | **Demo**：https://aizhiqi-work.github.io/bdr-bwe-demo/

### 📌 简介
本文针对生成式带宽扩展（BWE）模型多为固定带宽训练且依赖迭代采样、灵活性与效率不足的问题，提出三阶段框架BDR-BWE：先在压缩复数STFT域学习截止频率感知的条件流桥，再用渐进一致性蒸馏将多步传输压缩为一步生成器，最后以对抗精炼改善高频细节与谐波相干性。模型仅1.80M参数，推理只需1-2次网络评估，在VCTK全部评测带宽上取得SOTA的LSD（较最强基线FlowHigh相对降低7.9%-14.4%），并在EARS上展现强跨域泛化。

### 🔧 技术方案

**问题背景：** 现有神经BWE中，重建型模型（TFiLM、AP-BWE等）生成高频易过平滑，对抗模型需在单阶段权衡频谱保真与感知真实；扩散/流方法（NU-Wave2、FlowHigh）虽建模缺失频谱的不确定性但采样步数多，且多数系统绑定固定源-目标采样率对，难以应对实际中变化的输入截止频率。

**模型架构：** 三阶段共享同一紧凑复谱生成器：频谱编码器扩通道并压缩频率轴；主干为对称U-Net排布的5个TF-GridNet块（通道24/48/96/48/24），块内双向频/时建模+全带时间注意力，BiLSTM替换为80隐层双向GRU；流时刻t与截止频率fc以高斯Fourier嵌入注入每个块；解码器预测相对观测谱q_y的复残差，输出经反归一化、幂解压与iSTFT得48kHz波形，单次网络评估16.8 GMACs/秒音频。

**核心创新：** (1) 截止感知条件流桥：对谱做0.3次幂复数压缩并按平滑逐频RMS归一化，源噪声幅度a(f,f_c)在观测带取0.05、经smoothstep在缺失带升至1（过渡宽w=min(0.15f_c,3kHz)），仅对未观测频点保留完整生成不确定性；端点预测谱感应导出局部速度场(q̂₁−q_t)/max(1−t,0.02)做Euler积分。(2) 渐进一致性蒸馏：按16→8→4→2→1逐级减半NFE，学生以单次更新匹配冻结教师两次更新后的同起点状态，逐级用前级教师初始化，蒸馏阶段不引入任何对抗或感知目标，专注复现轨迹。(3) 少步生成器直接对抗精炼：MPD（周期{2,3,5,7,11}）+三分辨率多尺度子带CQT判别器hinge对抗，配合特征匹配、多尺度log-mel与截止mask高频log幅值损失，梯度穿过完整少步求解器回传，在固定NFE下恢复高频锐度与谐波相干性。

**训练策略：** Stage 1损失L_RI+2L_miss+0.05L_mel，AdamW峰值lr 5e-4、5k warmup、300k步；每个蒸馏阶段5k步、lr 1e-4；Stage 3微调20k步，生成器/判别器lr 2e-5/1e-4，对抗项前2k步渐入；EMA衰减0.999、FP32；训练取48kHz随机1秒段（1024点STFT、512 hop），退化用阶数2-10随机切比雪夫I型低通+降采样再升采样，输入采样率随机取{4,6,…,32}kHz。

### 📊 实验结果
**数据集**：VCTK（约44小时48kHz、108人，100训练/8评测）；EARS（8个未见说话者跨域评测）

**主要指标**：
- LSD（VCTK输入8/12/16/24kHz，NFE=1）：0.755/0.690/0.632/0.524（NFE=2再降至0.748/0.685/0.627/0.519）
- 关键对比：一步模型较FlowHigh的LSD相对降低7.9%/9.6%/11.6%/14.4%，FAD在3/4设置最优（如8kHz 0.135 vs FlowHigh 0.207），ViSQOL保持竞争水平并在24kHz输入最优（4.216）
- 极限4kHz→48kHz：LSD 0.831（FlowHigh 0.901），参数量1.80M vs 49.4M、GMACs 16.8 vs 25.5
- EARS跨域：4/8kHz输入LSD 1.060/0.940，FlowHigh为1.368/1.319
- 消融（8kHz→48kHz）：Stage1 16NFE LSD 0.926 →蒸馏1步0.935 →对抗精炼1步0.755，ViSQOL 2.957→3.284

**是否开源**：音频样例Demo公开（https://aizhiqi-work.github.io/bdr-bwe-demo/），代码暂无

### ⭐ 评分：8/10
评分理由：三阶段解分"轨迹精度、推理效率、感知质量"三个目标的思路清晰且各有消融支撑；截止感知噪声档是流桥构造上的实质创新，1.80M参数+1-2 NFE即全面刷新LSD，效率-质量权衡突出，EARS跨域结果增强可信度。不足在于缺主观MOS评测，对抗阶段超参敏感，且一步模型ViSQOL在部分设置略输FlowHigh；总体属有实质贡献、工程价值明确的顶会水准工作。

---

## VocalGrad: Evaluating Acoustic Perception in Audio Language Models

**arXiv ID**：2610.23745 | **方向**：语音大模型

**作者**：Koki Ryu, Hitomi Yanaka

**机构**：东京大学、理化学研究所（RIKEN）、东北大学

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.23745 | **PDF**：https://arxiv.org/pdf/2610.23745.pdf | **代码**：https://github.com/ynklab/vocalgrad | **Demo**：暂无

### 📌 简介
针对现有评测无法解耦大音频语言模型（LALM）声学感知与高层推理的问题，本文提出VocalGrad基准：对语速、音高、音量、失真、粗糙度、噪声、回声、清晰度、振动9类声学因子施加单一因子的时变增强，将任务形式化为"增大还是减小"的方向二分类，使评测基本独立于语义理解与推理。在21,600条语料上，5个SOTA LALM平均准确率仅49.6%–51.8%（近随机水平），而人类标注达94.4%。进一步通过分段线性探测与LoRA微调，识别出两类表征层面失败模式：信息保留但LM Head无法读出，以及信息随层深逐层衰减。

### 🔧 技术方案

**问题背景：** MMSU、MMAU、WoW-Bench、SALMon等现有基准的任务含跨片段比较、重排序、时间戳对齐等额外推理步骤，模型答错时无法定位瓶颈在感知编码还是下游语义整合；LISTEN、StressTest等研究虽证实词义与声学线索冲突时LALM不可靠，但未澄清其在处理管线中的失效位置。

**模型架构：** VocalGrad为基准与分析框架而非新模型。语料构建：从VCTK按性别/口音均衡选50说话人共100条源clip，能量端点检测后切为0.05秒分段施加单参数时变增强，相邻段0.005秒交叉淡化；方向×3强度档×4时间轨迹（jump、linear、quad_first_flat、quad_last_flat）组合，每clip生成24条，共21,600条、均长3.98秒，统一prompt模板提问。探测侧提取Mel、Pre-LLM音频token、Late-LLM末层三类表示，16段时间平均池化拼接后接单层线性分类器，并逐层抽取解码器输出预测位置表示，绘制分层可解码性曲线。

**核心创新：** (1) 感知隔离式任务设计：完整保留词汇内容、每次仅变化一个声学因子，类内增大/减小样本严格均衡，消除排序与时间戳等推理混淆，首次以统一格式同时评测说话人内在与环境诱发两类低层声学变化。(2) 三段式线性探测追踪全管线表示：沿Mel→Pre-LLM→Late-LLM→各层输出预测表示追溯时变方向信息，发现信息约在layer 5即完成聚合，volume/noise/roughness信息保留至深层但LM Head读出失败，pitch/speed等信息则随层深线性可解码性渐次丧失。(3) LoRA干预与正弦波消融验证：正弦波信号消融证明失败并非仅由语言干扰导致；仅微调LM Head即让保留类达88.2%–98.6%，全线性LoRA使9类接近满分，且单类微调诱发跨类表征方向余弦相似度显著变化。

**训练策略：** 每类增强含三档强度参数（pitch半音移调、volume增益、noise按语音RMS比例加高斯噪声、distortion自48kHz降采样、clarity低通截止等）。探测训练集用57名与测试无重叠VCTK说话人的500条clip、每类12,000样本，线性分类器以BCEWithLogitsLoss+AdamW训练。LoRA基于PEFT，单epoch（留10%验证、每类10,800训练样本），AdamW+16步梯度累积；推理主要bfloat16、贪心解码（MiMo-Audio temperature=0.3、top_p=0.95）。

### 📊 实验结果
**数据集**：VocalGrad（21,600条，VCTK英文语音，9类×3强度×4轨迹，均长3.98s）；探测训练集每类12,000样本；正弦波消融集4类各240条。

**主要指标**：
- 人类标注平均准确率：94.4%（distortion、echo达100%）
- 模型平均准确率：Kimi-Audio 51.8%、Gemini 3 Flash 50.2%、MiMo-Audio 50.3%、Step-Audio 2 mini 50.0%、Audio Flamingo 3 49.6%
- 关键对比：最优模型Kimi-Audio落后人类约42.6个百分点，二项置信区间与50%随机基线重叠
- 正弦波消融：MiMo-Audio noise 64.2%、Kimi-Audio volume 57.5%，无一类超过70%
- All-Linear LoRA后：speed 99.0%、pitch 98.7%、volume/roughness/noise 100.0%

**是否开源**：代码与数据集已开源 @ https://github.com/ynklab/vocalgrad ，数据集见 huggingface.co/datasets/ynklab/vocalgrad

### ⭐ 评分：8/10
评分理由：基准设计诊断力强，"单因子+方向二分类"干净地解耦感知与推理，人机差距、分层探测与LoRA干预多条证据链相互印证，揭示了纯文本评测不可见的表征层面失效。消融、prompt敏感性、few-shot、多源语料验证充分。不足在于只覆盖单因子受控变化，未涉及自然共变声学场景，属性词与感知的绑定混淆未完全排除，线性探测可能低估细粒度信息。

---

## PromptSep-Speaker: Generative Target Speaker Extraction via Multimodal Prompting and Semantic Alignment

**arXiv ID**：arXiv:2610.23066 | **方向**：语音前端

**作者**：Yutong Wen, Ke Chen, Prem Seetharaman, Haonan Chen, Oriol Nieto, Paris Smaragdis, Justin Salamon, Zeyu Jin

**机构**：Adobe Research, MIT

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.23066 | **PDF**：https://arxiv.org/pdf/2610.23066.pdf | **代码**：暂无 | **Demo**：https://yutongwen.github.io/PromptSep-Speaker/

### 📌 简介
现有目标说话人抽取（TSE）普遍依赖单一线索与掩码预测模型，前者既不易得又不够可判别，后者易产生伪影、泛化差。本文提出PromptSep-Speaker，一个基于潜空间扩散的生成式TSE模型，统一说话人时序ID、转录文本、注册音频、自由描述caption四种可互换线索，并引入辅助对齐损失，用冻结WavLM表征监督线索-混合信号交叉注意，在零额外标注下迫使模型真正利用语音线索定位目标。在四个域外评测集与380人听力测试上全面超越TSE与通用分离基线，转录线索SI-SDRi提升6.6-11.3dB，DNSMOS最高2.93，主观MOS多数项超4.0。

### 🔧 技术方案

**问题背景：** 多数TSE系统只用单模态内的一种线索：注册音频在音色相近或片段过短时易混淆，文本线索通常匹配"类"而非"具体人"；且以掩码预测模型为主，分离质量与跨声学条件泛化逊于生成式方法，评测还偏向全重叠混合，脱离对话中部分重叠交错的真实场景。

**模型架构：** 条件潜空间扩散框架：48kHz混合与注册音频由冻结DAC-VAE编码为latent，DiT（微调自PromptSep，约0.8B参数）生成目标latent并经VAE解码为分离波形；文本线索由Qwen3-VL-8B编码；混合经冻结WavLM Base+编码后，由2层双向Transformer对齐模块把序列级cue token转为帧级目标图，经MLP投影加到扩散latent上。

**核心创新：** (1) 首个在单一生成模型中统一四种可互换模态线索：caption与注册latent拼入扩散序列由DiT自注意力联合处理，转录与时序ID走对齐模块，用户按场景可得性任选线索，区别于以往仅支持单cue的系统。(2) 辅助对齐损失：对多头平均的cue-混合帧交叉注意图直接监督，spk ID损失以oracle目标RMS能量检测的活动帧强制tag质量、其余帧对准null token（null项权重β=0.5），transcript损失以强制对齐词帧区间为注意目标，总权重λ=0.2，无额外标注成本；去掉后SI-SDRi跌至-21.43dB、注意质量仅1%落在cue。(3) 帧查cue的对齐方向：以WavLM帧表征为query、cue token为键生成帧级目标图，使每帧判断"哪个词属于目标"；方向反转则SI-SDRi崩至-14.21dB。

**训练策略：** 从PromptSep权重微调，AdamW，学习率1e-4，v-prediction去噪目标，推理用DPM-Solver++(2M) SDE采样器+Karras schedule共24步。训练混合由授权内部语料（4.8M语音、1.1M音效、10K音乐、2K环境噪声）仿真合成：16s/48kHz单声道、2-3人，叠加混响与音效音乐，时间布局模板覆盖部分重叠、交替轮转、全重叠。

### 📊 实验结果
**数据集**：CapSpeech-Mix、Libri2Mix（16kHz clean+noisy均值）、LibriTTS-R-Mix、Internal内部英文集，四集与训练源严格不相交、全部域外

**主要指标**：
- 转录线索SI-SDRi：8.73/11.41/12.47dB（CapSp./LTTS-R/Int），DAE-TSE仅2.13/2.41/1.21，域外提升6.6-11.3dB；Libri2Mix域内6.15对11.13dB败于DAE-TSE
- 注册音频线索：SI-SDRi 11.79（LTTS-R）/13.30dB（Int），超SoloSpeech的6.59/8.47
- Caption线索：SI-SDRi 3.64/4.99dB，较最强SAM-Audio（-8.73/-12.80）提升≥12dB，F1 0.87对0.65
- 说话人ID线索（无基线）：较全转录SI-SDRi仅降0.41/0.81/1.10dB，F1持平0.93/0.94/0.95
- 主观听力（700题、380人、4515份）：21格中16格超4.0，注册线索说话人准确率4.52±0.10、内容一致性4.53±0.10

**是否开源**：仅发布demo页（https://yutongwen.github.io/PromptSep-Speaker/），论文未提供代码与权重

### ⭐ 评分：8/10
评分理由：首个统一四种可互换多模态线索的生成式TSE，辅助对齐损失经消融与注意可视化验证为决定性组件，评测覆盖四个域外集加主观听力，主客观结论一致，并关注更真实的交错部分重叠场景。不足：训练依赖授权内部数据且未开源代码权重，复现困难；24步扩散采样实时算力开销大；域内全重叠等信号级指标不敌掩码基线。

---

## MedSonor: Learning to Use Clinical Audio in Medical LLMs

**arXiv ID**：arXiv:2610.22405 | **方向**：语音大模型

**作者**：Geyang Yu, Junying Chen, Benyou Wang

**机构**：The Chinese University of Hong Kong, Shenzhen

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.22405 | **PDF**：https://arxiv.org/pdf/2610.22405.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对现有医疗音频监督止步于分类/识别、通用音频大模型缺乏医学知识与开放式回复反馈的问题，提出MedSonor——基于Qwen2.5-Omni-7B的音频条件医疗对话模型。作者构建收集医疗音频、合成口语对话、音频集成对话三源共18,657条多模态SFT数据，再经两阶段rubric引导的强化学习，并推出MedVoice-Dial与MedVoice-AID两个评测集。模型在七个医疗基准上全面领先开源音频语言基线，MedVoice-AID得分0.7900（基座仅0.3341），医生偏好评测排名第一，同时基本保持通用语音能力。

### 🔧 技术方案

**问题背景：** 临床音频携带文本无法保留的声学证据（罗音、心脏杂音、嗓音障碍等），但有效应答需将音频与当前请求和对话史结合。声源中心数据集缺乏"如何依据声音作答"的监督，纯文本合成的口语对话也教不会解读真实录音，且开放式医疗回复缺少任务级反馈信号。

**模型架构：** 主干为Qwen2.5-Omni-7B的Thinker–Talker架构，输入音频、对话历史与文本上下文，评测取Thinker文本输出。三条数据流：收集医疗音频7,569条（肺心音、咳嗽、口吃、情感/抑郁/疼痛语音、婴儿哭声、医学ASR等31个来源）；GPT合成多轮口语对话5,088条，覆盖25科室×15场景共375组合、采样5,000主题，句级TTS保持说话人对齐；音频集成对话6,000条，将真实音频片段按指定位置插入TTS合成的临床请求语音中。

**核心创新：** (1) 上下文化任务构造：按音频来源与临床类别分配科室并配对场景，用音频描述生成单轮请求与参考回复，使声学与临床请求显式绑定；消融显示去掉该监督后MedVoice-AID从0.7900跌至0.5957。(2) 顺序式rubric引导RL：先医疗对话RL、再音频集成RL，均以DAPO组内相对优势更新并对本阶段初始策略加KL约束。(3) 严重性封顶的本地逐项评审奖励：每个实例生成8–12条带符号原子准则（正权+1~+10/负权−1~−10），用LoRA微调两个Qwen3-4B-Instruct裁判分别判正例/历史与负例条目；奖励为正项加权覆盖率减负项及长度截断罚，检出major违规封顶为0、critical违规强制为负，防止高分掩盖危险性医疗错误。

**训练策略：** SFT冻结视觉编码器，训练语言模型与aligner，per-device batch 8、余弦学习率；两RL阶段样本6,927/4,546，batch 4、每prompt采样10个补全、非对称裁剪0.20/0.28、256 token补全预算、长度罚阈值取参考长度1.10/1.50倍；全程fused AdamW、BF16、梯度检查点、seed 42。裁判以GPT标注监督，验证准确率94.76%/89.90%。RL数据经基线奖励过滤（仅留0~0.9之间样本）。

### 📊 实验结果
**数据集**：自建MedVoice-Dial/MedVoice-AID；LiveMedBench、MMedFD-Lite、ACI-Bench、HealthDial、ThReadMed-QA改编评测；MS-SNSD babble加噪测试；LibriSpeech、AISHELL-1、VoiceBench等通用能力评测。

**主要指标**：
- MedVoice-AID：0.7900，较基座Qwen2.5-Omni-7B的0.3341提升0.4559，开源组第一
- MedVoice-Dial 0.5225、LiveMedBench 0.2843、MMedFD-Lite 5.780、ACI-Bench 0.2263、HealthDial 0.5022、ThReadMed-QA 0.3403：七基准均列开源模型首位
- 医生偏好：30例、720次判断，Bradley–Terry总分高于全部6个开源基线
- 噪声鲁棒：约14.0/4.4 dB SNR babble下得0.7480/0.7282，全部基线低于0.32
- 通用保持：AISHELL CER 2.93→1.73、IFEval 35.55→45.34%、LibriSpeech WER微降质量（2.26→2.78）

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：把"识别医疗声音"推进到"依据声学证据在上下文中作答"，三源数据与严重性封顶的rubric奖励设计针对性强，消融、加噪、医生与自动偏好实验证据链较完整，具备实质领域贡献。不足在于评测重度依赖GPT系裁判、医生评估仅30例且评审一致率59.6%偏低、数据仅英文，临床可信度有限；未开源制约复现与实用价值。

---

## Audio System One Model: Typed Probabilistic Perception of Emotion in Speech

**arXiv ID**：arXiv:2610.22401 | **方向**：语音大模型

**作者**：Jaime Bellver-Soler, Iván Martín-Fernández, Anmol Guragain, Luis Fernando D'Haro

**机构**：马德里理工大学（Universidad Politécnica de Madrid）THAU 语音技术与机器学习组、信息处理与电信中心

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.22401 | **PDF**：https://arxiv.org/pdf/2610.22401.pdf | **代码**：暂无（承诺接收后开源，已投 ICASSP） | **Demo**：暂无

### 📌 简介
语音应用常需对同一句话回答多个问题（听到什么情绪、唤醒度高不高、是否在沮丧），但分类器快且校准却锁死固定标签集，音频大模型（ALM）能接受任意文本提问却逐题生成、延迟高且概率不校准。本文提出 ASOM：一个"系统一"式语音模型，用冻结的 Whisper-large-v3 与 Qwen2.5-1.5B 双编码器加 6.2M 参数无类别参数的 reader，按听众投票分布训练，请求时书写 choice/score/yes-no 类型问题，一次前向即返回校准概率分布。MSP-Podcast 上 F1 达 0.383，超最佳零样本 ALM 0.072、超同数据 LoRA 微调 ALM 0.026，20 题仅 13.1ms（快 17–41 倍），21 个未见语料平均 macro-F1 0.433。

### 🔧 技术方案

**问题背景：** 部署中的情感系统往往提前固定问题或决策树。分类器新增情绪词、换标签集或加属性都要重训；ALM 虽接受自由提问，但每题需一次语言模型生成，隐式概率与听众投票严重失配——六个零样本 ALM 的 log loss 全部高于类先验。

**模型架构：** 请求为 JSON 类型化问题，每个选项写成"criterion"文本（问题+标签名+描述），由冻结 Qwen2.5-1.5B 编码并缓存（不依赖音频）；音频由冻结 Whisper-large-v3 编码，取 32 块中 8/16/24/32 四块学习 softmax 混合，64 个时间段的均值由 4 个学习 query 注意后经零初始化门控注入。可选 RoBERTa-large 编码 ASR 转写。reader 把两侧映射到 R^256 单位向量，s=τ·ĉᵀâ+b(ĉ)（τ=8 固定，b 为 criterion 线性偏置），按题 softmax；63 个 criterion 一次矩阵乘 0.6ms 完成。共 2.2B 参数，仅 6.2M reader 可训。

**核心创新：** (1) 标签即文本的开放打分：类别是 criterion 而非输出单元，同一权重可答改写/缩减/新标签集、7 级量表与性别；消融显示文本描述相比每类学习向量保 F1（0.382 对 0.379）并提升未见均值（0.433 对 0.417）。(2) 以听众投票分布为目标并用交叉拟合蒸馏去噪：votes 份额/评分直方图/yes 占比做 CE，另用 32 个辅助 reader 在 disjoint 折上产生 out-of-fold 集成软目标；去掉蒸馏 LL8 恶化 0.019，CLIP 对比损失替代 votes 则 LL8 +0.369、AUC 从 0.763 跌至 0.596。(3) 一答多问且与题数无关：criterion 独立于音频可预缓存，成本近似纯语音编码器，兼得分类器时延与开放问题接口。

**训练策略：** 仅用 3 个公开个体投票语料：MSP-Podcast 2.0 Train（169k 片段，含主/次情绪与 7 点 A/V/D）、CREMA-D（每片 6–12 听众）、意大利语 Emozionalmente（每片 5 人）；每片段构 4 类问题，一半训练步对问题与选项改写；结果取 3 seed 均值；编码器全程冻结。

### 📊 实验结果
**数据集**：MSP-Podcast 2.0 Dev-select（28,759 片段/553 说话人，统一对比子集 3,113）；迁移含 21 个未见语料（20,585 片段、13 语言）及开放情绪词测试。

**主要指标**：
- 8 类 macro-F1：ASOM 0.383，超 Qwen2.5-Omni-7B（0.311）0.072、超 LoRA 全量微调 Omni-3B（0.357）0.026；加转写 0.402
- 校准 LL8：1.507，低于类先验 1.863；六个零样本 ALM 均≥2.097
- 时延：20 题 13.1ms，ALM 为 230–545ms，快 17–41 倍
- 泛化：21 未见语料均值 0.433（最佳零样本 ALM 0.313）；A/V/D CCC 0.674/0.735/0.584
- 短板：训练外情绪词 F1 仅 0.018（AUC 0.721）；性别 0.873 低于 Omni-7B 0.927

**是否开源**：承诺接收后开源，当前暂无公开仓库。

### ⭐ 评分：7/10
评分理由：首次在语音上落地"System One"类型化提问接口，精度匹配同数据分类器、校准与时延碾压 ALM，对语音代理与呼叫中心分析部署价值直接；21 语料 13 语言、转写对照组与系统消融的实验规模非常扎实。扣分在于模型主体是双塔打分与投票损失的成熟组件组合、架构新颖性有限，且评测封闭于情绪属性，瓶颈仍是多人标注数据稀缺。

---

## DriftTTS: One-stage Single Step Text-to-Speech via Generative Drifting

**arXiv ID**：arXiv:2610.22960 | **方向**：语音大模型

**作者**：Jaehyun Ahn, Dohyun Kim, Heeseung Kim

**机构**：Department of AI, University of Seoul, 韩国首尔

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.22960 | **PDF**：https://arxiv.org/pdf/2610.22960.pdf | **代码**：暂无 | **Demo**：https://drifttts.github.io/

### 📌 简介
基于score matching与flow matching的TTS需多步迭代调用解码器，合成慢，而现有少步方案要么从多步teacher蒸馏、要么在预训练模型上再叠加训练阶段。本文提出DriftTTS，首次将generative drifting引入语音生成：把迭代采样从推理移到训练，解码器单次调用即把先验分布推前到mel频谱分布，全程无需预训练TTS。针对语音变长问题提出segment drifting，并以编码器对齐输出构造先验。在LJSpeech上以1 NFE取得WER 1.80、MOS 4.43±0.08、RTF 4.41e-3，质量媲美Matcha-TTS（10步）与RapFlow-TTS（2步）且快4.2倍。

### 🔧 技术方案

**问题背景：** Grad-TTS、Matcha-TTS等以10次以上NFE换取自然度，推理慢；IntMeanFlow与RapFlow-TTS虽能少步生成，但都依赖预训练TTS提供底层轨迹，带来多阶段训练复杂度与算力开销，"无预训练模型训练单步TTS"的问题此前无人探索。

**模型架构：** 基于Matcha-TTS改造：文本编码器＋时长预测器＋解码器。文本编码器token表示经MAS与目标mel单调对齐，按时长重复扩展为先验μ，解码器另接收噪声作为随机条件，直接一步预测目标mel片段而非速度场；因drifting不需要时间步，删除解码器的时间嵌入并减少参数。声码器用HiFi-GAN，mel配置遵循HiFi-GAN V1。漂移在自训练MAE特征空间计算：mel视作单通道图像，瓶颈结构编码器的对应层特征成对比较。

**核心创新：** (1) 首次将generative drifting用于TTS：基于mean shift理论构造漂移场——对数据分布的吸引减对生成样本的排斥（Laplace核带温度τ），以漂移后样本作stop-gradient目标做特征空间L2回归，将迭代采样移入训练，实现单步one-stage生成。(2) Segment drifting解决变长与条件生成：训练时从先验与目标各采固定80帧片段；将先验从标准正态重定义为带文本对齐的μ，因每个μ只有唯一正确目标，用batch内目标片段作正样本、生成片段作负样本并mask对角自交互，避免错误吸引信号。(3) 多温度多层漂移损失：在τ∈[0.02,0.05,0.2]与多个MAE层组合上对drift loss取平均而非求和，防止过多梯度传入文本编码器、稀释prior loss导致训练失败。

**训练策略：** LJSpeech（沿用Matcha-TTS划分）；4×NVIDIA A10训练2000 epochs；AdamW，lr 1e-4，weight decay 0.01，梯度裁剪5.0，推理用EMA（decay 0.999）。batch size关键，取每GPU最大64对文本-语音；文本编码器在整句训练，解码器在80帧（约0.93s）片段训练，MAS用SuperMAS在GPU运行；MAE用4×4掩码、50%概率预训练；总损失L=L_prior+L_duration+L_drift。

### 📊 实验结果
**数据集**：LJSpeech单说话人英文语料，500条评测语句

**主要指标**：
- WER（whisper-large-v3-turbo转写）：1.80，对比GT 1.92、Matcha-TTS@10NFE 1.93、RapFlow-TTS@2NFE 1.82
- MOS（5分制，MTurk，153人290份响应）：4.43±0.08，为全部合成系统最高（Matcha-TTS 4.38±0.08、RapFlow-TTS 4.42±0.08）
- RTF（单张A10、batch=1、不含声码器）：4.41×10⁻³，比Matcha-TTS十步快4.2×、比RapFlow-TTS两步快1.3×
- 消融：去掉MAE直接在mel空间segment drifting→能量发散，WER恶化至20.03、UTMOSv2仅0.517；改frame drifting→虚假收敛，UTMOSv2 2.137；多温度损失取最低WER 1.80（单温度2.00/1.90）

**是否开源**：代码暂无开源仓库，demo页面https://drifttts.github.io/提供合成语音样例

### ⭐ 评分：7/10
评分理由：把漂移范式首次落地语音生成，确立单步、one-stage、无预训练teacher的新路线，问题定位准确；消融系统揭示能量发散与虚假收敛两种失效模式，机制解释扎实、结论诚实。局限在于仅评测单说话人LJSpeech，RTF略慢于同为1 NFE的基线，且质量强依赖额外训练的MAE特征提取器，多说话人与零样本场景尚未验证。

---

## Flash RNN-T: Memory-Efficient Joint Network and Transducer Loss Computation

**arXiv ID**：arXiv:2610.23409 | **方向**：语音大模型

**作者**：Mahmoud Ashraf

**机构**：Tarteel AI

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.23409 | **PDF**：https://arxiv.org/pdf/2610.23409.pdf | **代码**：https://github.com/MahmoudAshraf97/flash-rnnt-paper | **Demo**：暂无

### 📌 简介
RNN-T仍是流式ASR的主流模型，但其非线性联合网络需在T(U+1)个对齐位置计算隐状态与全词表logits，这些中间张量随batch累积导致训练内存爆炸，长语音尤为突出。本文提出Flash RNN-T：专用GPU融合内核加可选分块检查点重计算，在保留全对齐空间与全词表（精确损失不变）的前提下，将联合中间内存从O(N(H+V))压至O(min(N,R)(H+V))。H100实测非分块版比最快基线吞吐高24-39%、内存省26-56%；分块版在长语音上可放入80GB而全部基线OOM。

### 🔧 技术方案

**问题背景：** 传统批式训练将整个batch的联合隐状态与logits全部保留供反传，内存随T×U×V×B增长。Li等的有效位打包与Braun等的逐句计算只消除填充位或缩短句间共存窗口，均未对单句内部的大中间张量设上界。

**模型架构：** 被优化对象为给定编码器与预测网络投射状态后的联合+损失计算（含词表投影与梯度回传）。非线性联合h=Dropout(φ(e_t+p_u))、z=Wh+b在每句产生T(U+1)个位置，而forward-backward递推仅需blank与目标token两类log概率。Flash将有效对齐位置紧打包为至多R个位置的分块tile（可跨句边界），逐tile前向后只留压缩转移log概率，反向时在autograd内逐tile重算并立即释放。

**核心创新：** (1) 分块激活检查点：tile级检查点限于O(min(N,R)(H+V))，投射状态e_t、p_u不入检查点直接复用，每tile保存种子复现dropout掩码，不改训练循环且保持整batch单次损失backward。(2) 专用融合内核：联合内核融合加法+激活+dropout，反向融合导数与沿编码器/目标轴的归约，一次读隐状态梯度即产出两侧梯度；归一化内核只输出blank/target log概率，反向直接向logit原缓冲覆写梯度。(3) 免索引打包映射：由打包边界识别句子并以整除/求余得格点坐标，省去逐位置索引存储。

**训练策略：** 系统级评估，仅测joint+loss前后向基准：B=128、联合隐维H=640、SentencePiece BPE词表V=1024（含blank）、80ms编码器步长、joint dropout 0.1；FP16输入与联合计算，参数/梯度/归一化/递推用FP32；tile上限R从25K到800K倍增扫描，损失与梯度对参考实现做正确性验证。

### 📊 实验结果
**数据集**：Granary英语子集选short/medium代表batch（有效对齐位置282,687/2,300,131），TED-LIUM 3长语音split选long（41,122,726位置、均值69.6s）

**主要指标**（H100 80GB，吞吐samples/s/峰值内存）：
- medium：非分块Flash比Apex吞吐高24-25%、内存省49-56%；分块Flash 2839/1.84GiB，较Apex retain内存降9倍、吞吐低16.3%
- long：分块Flash 163.6/4.26GiB，全部基线retain配置在80GB OOM而6档分块配置均可放入；较Apex release内存省4倍、吞吐低12.3%
- short：非分块Flash较Apex内存省60%/73%，吞吐仅低7.8%/6.6%
- 组件消融：专用归一化内核使分块吞吐升13-16%，专用联合内核再省17-33%内存；RTX 5090 32GB重复出相同frontier

**是否开源**：代码、benchmark脚本与结果已开源 @ https://github.com/MahmoudAshraf97/flash-rnnt-paper

### ⭐ 评分：7/10
评分理由：将打包、紧凑转移概率与激活检查点组合，以tile量级给联合中间内存设上界且保持精确损失，工程价值明确，"长语音可训"对实际RNN-T训练有直接意义；双GPU对比与组件消融较扎实。不足：只评估joint+loss而非端到端训练吞吐，单一模型配置，未与Pruned RNN-T等近似方案对比精度影响，分块重计算吞吐代价达24.5-29.6%。

---

## Interpreting SSL Representations for Spoof Detection: a WavLM Study

**arXiv ID**：arXiv:2610.23526 | **方向**：语音大模型

**作者**：Mohamed Mallat, Michele Panariello, Massimiliano Todisco, Nicholas Evans, Anthony Larcher

**机构**：EURECOM（法国索菲亚安蒂波利斯）| 曼恩大学（法国勒芒）

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.23526 | **PDF**：https://arxiv.org/pdf/2610.23526.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
以WavLM为代表的自监督前端已是反欺骗检测主力，但哪一层携带欺骗线索、编码了何种声学属性长期不透明。本文基于ASVspoof 5数据库提出三合一逐层可解释性框架：逐层线性探针与按攻击的EER评估、PWCCA将层表征与17个手工声学特征对齐、8191种层子集穷举搜索。结果显示L11单层探针EER最低（dev 3.33%、eval 6.07%）；jitter/shimmer/HNR等音质特征与深层相关性单调上升；最优5层子集（L7–9–10–11–12）eval EER 6.1%，优于全13层池化的8.08%；对抗攻击在所有层均失效，暴露假线索检测的根本局限。

### 🔧 技术方案

**问题背景：** 现代反欺骗系统普遍用SSL前端加复杂后端追求性能，但表征本身是黑箱：层选择随意、检测依赖何种声学线索不明，且已有研究指出CM会利用非语音时长等虚假线索，亟需把模型行为锚定到可解释声学属性上。

**模型架构：** 冻结的WavLM Base（L0–L12共13层，每层768维帧表征）作特征提取器；每层沿时间轴做mean+std池化拼成1536维话语向量。三条分析支线：(i) 每层独立训练线性分类器区分bona fide/spoof，并按32种攻击归入TTS/VC/ADV三族绘制逐攻击EER热力图；(ii) 层向量经PCA降维至50后与音质(3)、韵律(4)、频谱(6)、共振峰(4)共17个手工特征做PWCCA双向对称相关；(iii) 对全部8191种层组合穷举，拼接k×1536维向量训练线性探针；辅以L1/L6/L11的t-SNE可视化。

**核心创新：** (1) 攻击感知的层刻画：首次系统揭示层深与攻击族的强交互，A12单元选择攻击EER由早期层约80%降至深层约5%，而A22/A24/A28在深层反而EER超30%。(2) PWCCA声学锚定：将SVCCA/PWCCA类表征相似度工具首次用于欺骗检测，发现谱特征在L7达峰后衰减、音质特征随深度单调增强这一相反几何转变。(3) 紧凑层子集超全层池化：5层组合eval EER 6.1% 对 8.08%，且t-SNE显示深层由离散攻击簇转为连续马蹄形流形，支持按声学自然度梯度组织攻击。

**训练策略：** 线性分类器仅用train集拟合，按dev EER选模型，eval仅一次性报告。CCA分析只用train+dev，每攻击组随机采样至多5000条说话人均衡话语；t-SNE在多个随机种子与perplexity（20/30/50）下验证一致性。

### 📊 实验结果
**数据集**：ASVspoof 5 Track 1（train A01–A08、dev A09–A16、eval A17–A32，32种TTS/VC/对抗攻击，含编解码与多样化录音条件）

**主要指标**：
- 单层线性探针EER：L11最低，dev 3.33%、eval 6.07%；L12回升至eval 7.3%
- 最优5层子集L7–9–10–11–12：dev 2.06%、eval 6.1%，较全13层池化（dev 4.59%、eval 8.08%）绝对降低1.98个百分点
- PWCCA相关系数：谱质心L7达0.96、MFCC均值0.92；jitter由0.52升至0.89、shimmer 0.53→0.90、HNR 0.55→0.94；共振峰最弱仅0.70–0.78
- 关键对比：Malafide/Malacopula对抗攻击全流程EER>20%，且层趋势平坦或倒置

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：问题切口扎实——层探针、PWCCA相关与子集搜索三种互补证据闭环，音质特征与深层对齐、马蹄形流形等发现对SSL基反欺骗系统的层选择有直接工程价值。实验覆盖32种攻击、dev/eval双验证且对抗失效分析坦诚。局限在于仅WavLM Base一种架构、线性探针只触及线性可读信息、单语料外推性未证，亦无开源。

---

## Too Emotional to Be Fake? Intra-Utterance Emotion Shifts Expose Failure Modes in Speech Deepfake Detectors

**arXiv ID**：arXiv:2610.22832 | **方向**：语音前端

**作者**：Jingyi Chen, Surya Koppisetti

**机构**：Reality Defender

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.22832 | **PDF**：https://arxiv.org/pdf/2610.22832.pdf | **代码**：暂无 | **Demo**：https://emoshift.github.io/emoshift/

### 📌 简介
表达性TTS已能在一句话内切换情绪，但深度伪造检测器对段内情绪转换是否敏感无人系统评估：现有EmoFake、AffectDF等基准只把情绪当作话语级标签。本文提出EmoShift基准，含7,240条真实与9,720条四个表达性TTS生成的合成语音（共16,960条），以类别标签+VAD连续标注对比情绪稳定(AA)与情绪转换(AB)语音，并控制静态情绪身份及拼接、语言内容、时长等混淆。在七个检测器上发现：情绪转换的合成语音获更低 spoof 分数，在OMG-Emotion固定阈值下漏检率增加9.7–25.3个百分点；真实转换语音则使IEMOCAP误报率最多升24.4个百分点，揭示了检测器的新失效模式。

### 🔧 技术方案

**问题背景：** 现有深度伪造基准只关注真伪标签，情绪类基准将情绪视为话语级静态属性，无法判断检测器是否对段内情绪变化本身敏感；且检测器对AB与AA的分数差异可能只是起点/终点情绪、拼接伪影或内容差异所致，需要受控对比设计。

**模型架构：** 每条语音含两个情绪区段，AA两段同情绪、AB由情绪a变到b。构建分三档：ESD用同说话人同文本两段拼接成400对受控AA/AB（20种有序情绪转换×20对）；OMG-Emotion取连续未拼接独白片段220/220条；IEMOCAP与MSP-Podcast用归一化VAD向量欧氏距离选段（如IEMOCAP aa为0.00–0.13、ab为0.84–1.09）。伪造端用四个情绪TTS：IndexTTS2分区合成再拼接、TED-TTS单遍段级情绪控制、HybridEmo按自然语言情绪序列指令整句生成、基于CosyVoice 2的EmoTra-TTS以连续VAD轨迹单遍生成；均克隆源说话人音色。评测7个检测器：RawNet2、AASIST、XLS-R-SLS、XLS-R-Mamba、ProsDD、SLIM、Alethia，统一用ASVspoof 2019 LA训练权重，按各自原生窗口3.0–4.2s滑窗取窗均值得句级概率。

**核心创新：** (1) 首个段内情绪转换基准：在真实与合成本两类内部分别对比AA/AB，把"情绪变化"与"静态情绪身份"解耦，弥补EmoFake/AffectDF只有话语级情绪的盲区。(2) 部署导向评测协议：类内logit分数位移Δ、在AA上EER点标定阈值后固定应用于AB统计FNR/FPR变化（pp），配合1,000次说话人聚类bootstrap 95%CI，避免EER自适应阈值掩盖真实风险。(3) 多层混淆控制：ESD全转换平衡；OMG按同生成器起/始情绪稳定样本均值对照；拼接分析对比拼接(IndexTTS2)与非拼接(TED/Hybrid/EmoTra)生成及边界窗口局部分数；自然真实语音用OLS回归控制说话人固定效应、log时长与分区VAD后检验位移持续性。

**训练策略：** 五检测器用公开发布checkpoint；SLIM无可用LA权重，在ASVspoof 2019 LA上微调其WavLM-Large骨干5个epoch；Alethia取作者预训练checkpoint后同集微调。全部音频重采样16kHz单声道，logit截断极端概率；基准AA/AB平均时长差≤0.49s。

### 📊 实验结果
**数据集**：EmoShift（16,960条=7,240 bona fide+9,720 spoof；ESD/OMG/IEMOCAP/MSP-Podcast；16kHz）

**主要指标**：
- 基线：池化EER在ESD为13.0–43.2%（Alethia最优13.0%），IEMOCAP/MSP多数检测器EER超50%（SLIM在IEMOCAP达84.4%）
- OMG-Emotion合成AB语音logit位移：RawNet2 −3.25、XLS-R-SLS −2.64、XLS-R-Mamba −2.47、Alethia −2.03，固定阈值FNR增加9.7–25.3pp，7/7检测器显著
- ESD：XLS-R-SLS/Mamba的FNR分别+6.8/+4.3pp，而EER变化幅度小且不显著，说明EER漏报风险盲区
- IEMOCAP真实语音：AASIST +1.66、RawNet2 +1.54 logit位移，FPR增加18.6–24.4pp；XLS-R方向相反
- 唤醒度分析：RawNet2/AASIST对真实语音唤醒度上升一致正响应（斜率+0.55/+0.98每0.1归一化唤醒度，两数据集均显著）

**是否开源**：基准数据与demo音频发布于项目网站 https://emoshift.github.io/emoshift/，未提供独立代码仓库

### ⭐ 评分：7/10
评分理由：视角新颖，首次把段内情绪动力学确立为伪造检测的系统性失效维度，固定阈值+bootstrap+多重混淆控制的方法学严谨，对产业界检测器极具警示价值。不足：自然语料上多数检测器基线EER超50%（分数倒序），结论解释力受限；类别转换与VAD转换混用生成方式难以归因；只暴露问题未给出缓解算法，属高质量增量评测工作。

---

## X-MDD: LLM-Based Mispronunciation Detection and Diagnosis for Unseen Languages with Canonical References

**arXiv ID**：arXiv:2610.23079 | **方向**：语音大模型

**作者**：Xintong Wang, Junchuan Zhao, Ye Wang

**机构**：新加坡国立大学计算机学院

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.23079 | **PDF**：https://arxiv.org/pdf/2610.23079.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
MDD 系统扩展到新语言通常需为每个目标语言采集并标注学习者语音，标注代价高、语言覆盖受限。本文提出多语言 LLM 框架 X-MDD，基于 Qwen3-ASR-1.7B，以 TTS 克隆合成的标准语音频与标准音素序列作参考，自回归预测学习者实际发音音素，并用带 in-context 示例的 SFT 加检测 F1 与 PER 联合奖励的 GRPO 优化。仅在中文、英文上训练，模型在阿拉伯语 QuranMB.v2 上检测 F1 达 38.07，接近监督基线 44.14，同时在中/英文上分别取得 78.68 与 58.78 的 F1。

### 🔧 技术方案

**问题背景：** 现有 MDD 系统依赖目标语言标注学习者语音，跨语言扩展需重复采集标注；已有多语言工作仍要求目标语言在训练中出现。LLM 原生 MDD 中显式标准先验还会使预测偏向正确发音、压低召回，未解决 unseen 语言迁移问题。

**模型架构：** 主干为 Qwen3-ASR-1.7B，含音频 Transformer（AuT）、音频投影器与 LLM 解码器。三路输入：学习者语音、以学习者录音作音色克隆参考由 CosyVoice3-0.5B（阿拉伯语用 SILMA TTS）合成的标准语音、以及空格序列化后经 BPE 编码的标准音素。示例与查询经可学习边界 token 拼入单一 user 轮，解码器在 assistant 轮贪心生成实际音素，与标准音素对齐得到检测与诊断结果。

**核心创新：** (1) 首次将 MDD 扩展到训练未见语言：仅训练中/英，阿拉伯语零训练迁移，靠标准音素提供符号锚点、标准语音补充声学实现证据；消融显示无标准音素时 PER 高达 606%，标准语音须与音素联用才有效。(2) 面向 MDD 指标的 GRPO 后训练：奖励组合句级检测 F1 与 PER，KL 约束于冻结 SFT 参考，显著提升被标准先验压过的召回（中文 65.46→79.97、英文 45.92→56.10）。(3) 机制可解释分析：注意力在 19-28 层超 50% 集中于标准音素、浅层依赖标准语音；替换 20% 标准音素的干预证明冲突语音证据降低照抄倾向；logit lens 显示 GRPO 主要把 SFT 已高排名的实际音素顶出。

**训练策略：** 音频重采样 16kHz、128 维 log-Mel；冻结 AuT 输入端三层 Conv2D，AuT 前 1000 步冻结；AdamW 对 LLM/投影器与 AuT 分层设学习率，中英均匀混合 7000 步、有效 batch 48；SFT 演示数 0-4 均匀采样、GRPO 为 1-2，GRPO 在含错误标注句上跑 300 步按温度对组内奖励归一化求优势；推理时中文用同说话人支持集，英/阿用 WavLM x-vector KNN 检索，最多 128 条演示。

### 📊 实验结果
**数据集**：训练中文 AISHELL-3+MagicHub 川渝/新加坡+LATIC 共 68,774 句、英文 TIMIT+SpeechOcean762+L2-ARCTIC 共 13,997 句；测试中/英各 900 句；未见语言阿拉伯语用 QuranMB.v2 官方测试集 1,643 句、18 人，音素错误率 6.73%。

**主要指标**：
- 多语言 F1：中文 78.68、英文 58.78，均超 ATP-LLM（75.23）等单语基线；PER 中文 17.79、英文 12.87
- 相对单语训练 F1 提升：中文 +6.37、英文 +2.87 个百分点
- 阿拉伯语迁移：F1 38.07、PER 7.75、DER 40.33，与阿拉伯语监督基线 44.14 差 6.07pp
- GRPO 后中文 F1 79.34（较 Base +5.43pp）；演示数 0→128 使阿语 F1 35.22→38.07
- 层 28 实际音素占比：SFT 16.0% → GRPO 24.4%（+8.5pp）

**是否开源**：暂无（论文未给出代码/Demo 仓库，仅使用开源组件 Qwen3-ASR、CosyVoice3、SILMA TTS）

### ⭐ 评分：7/10
评分理由：首次系统定义并验证 unseen 语言 MDD 迁移问题，标准语音+音素双参考与 GRPO 召回恢复的设计针对性强，注意力、音素干预、logit lens 等分析扎实有洞见。不足是阿语仅一个语种、F1 落后监督基线 6pp，召回与诊断准确率仍偏低，单说话人测试口音限制结论稳健性，属有实质贡献的会议级工作。

---

## Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS

**arXiv ID**：arXiv:2610.23678 | **方向**：语音大模型

**作者**：Séverin Baroudi, Yanis Labrak, Petr Motlicek, Hervé Bredin, Ricard Marxer

**机构**：Univ Toulon/CNRS LIS（法国）、Mila – Quebec AI Institute、Idiap Research Institute、Brno University of Technology、pyannoteAI、CNRS ILLS Montréal

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.23678 | **PDF**：https://arxiv.org/pdf/2610.23678.pdf | **代码**：https://beyond-the-benchmark.github.io | **Demo**：https://beyond-the-benchmark.github.io（项目页含生成音频）

### 📌 简介
Qwen3-TTS宣称零样本语音克隆SOTA，但其技术报告未说明两种克隆接口如何选型、在朗读语音之外的域如何表现、以及如何失效。本文以朗读（LibriSpeech）、会议（AMI）、情感（IEMOCAP）、ATC无线电（ATCO2）四域，联合18项客观指标、LLM评审、AASIST反欺骗与2AFC听测四类证据，系统剖析Qwen3-TTS（ICL与X-Vector接口）对比Chatterbox、XTTS-v2、F5-TTS。结果显示X-Vector最易骗人（AMI骗人率35.6%），语料解释方差63%是系统的4倍，现成探测器将99%真实ATC语音误标为伪造，ATC域防护完全失效。

### 🔧 技术方案

**问题背景：** 现有TTS评测依赖干净朗读语音上的WER、说话人相似度与预测MOS，在系统逼近人类质量后趋于饱和，且从未考察Qwen3-TTS的双接口、跨域行为与失效模式，单一证据族无法回答"哪个接口、哪个域、怎么坏"。

**模型架构：** 纯外部评测研究。被测系统为Qwen3-TTS-12Hz-1.7B-Base（1.7B；ICL接口以参考音频+转写续写、X-Vector接口仅以说话人嵌入条件化）及Chatterbox（500M）、XTTS-v2（约518M）、F5-TTS v1 Base（336M），均用公开checkpoint不微调。评测栈四层：2AFC真人听测（骗人率=选合成端比例）、Gemini 3.5 Flash评审（双呈现顺序）、18项客观指标归入说话人/韵律/F0/可懂度四维并按r=1−(1−A)²双重映射成综合分S、AASIST（0.3M参数）原样部署检测。

**核心创新：** (1) 首个Qwen3-TTS双克隆接口对照评测：采用shifted配对（音频取第i+1句、文本取第i句）排除韵律复制，证明两接口互不统治——ICL音色更近（LS S_Spk 80.2 对 61.5）、X-Vector韵律更准（各语料高2.6–11.3分）且更稳。(2) 转写扰动失效实验：仅替换参考转写中间一词即令ICL幻觉率短语句语料涨一个量级（IEMOCAP 0.8%→21.2%），且96.6%的干扰词泄漏在合成句首个三分之一而非注入位置。(3) 时长信号幻觉检测器（d/词数>1s或d/参考时长>1.5，人工审计召回94.7%），并量化客观分、LLM评审与真人排序的系统性背离。

**训练策略：** 不训练模型，仅统一推理配置：Qwen3-TTS以bfloat16推理，temperature 0.9、top-k 50、top-p 1.0、重复惩罚1.05；基线保持库默认。指标在留出开发集上与人类标注Spearman ρ≥0.45筛选，18项保留13项后应用于其余系统语料。

### 📊 实验结果
**数据集**：LibriSpeech、AMI、IEMOCAP、ATCO2四个英语语料，各随机抽取1小时，覆盖朗读/远场会议/情感对话/窄带噪声无线电。

**主要指标**：
- AMI真人骗人率：Qwen3 X-Vec 35.6%、ICL 27.0%，基线最高仅Chatterbox 9.0%、XTTS-v2 6.0%、F5-TTS 1.0%
- 综合分S均值：X-Vec 34.3 对 ICL 33.4 对 Chatterbox 31.9 对 XTTS-v2 28.2 对 F5-TTS 21.1
- 方差分解：语料63% 对 系统15%；ATCO2可懂度分S_Int仅14.7（LibriSpeech为55.2）
- AASIST检测率对假警率：ICL/AMI 13%/17%未分离，仅ICL/LS 39%/19%可分；ATCO2真语音误报99%，全部系统不可用
- 关键对比：XTTS-v2在AMI上S=40.9排第一但骗人率仅6%，机器检测与主观感知排序相反

**是否开源**：代码与全部生成音频已公开 @ https://beyond-the-benchmark.github.io

### ⭐ 评分：7/10
评分理由：作为首个Qwen3-TTS系统外评，四类证据互证的设计扎实，接口选型规则（ICL适用转录可靠的干净长参考，X-Vector适用短/噪/无转写场景）与ATC反欺骗彻底失效的结论对实践者直接可用；不足在于听测仅3名标注员使骗人率置信区间偏宽、且属行为剖析而非方法创新，整体实验规模与可复现性仍支撑其参考价值。

---

## Not All Frames Are Equal: Difference-Aware Quantization for Ultra-Low-Bit ASR

**arXiv ID**：arXiv:2610.22395 | **方向**：语音前端

**作者**：Woori Jeon, Jungmin So

**机构**：Sogang University（西江大学），首尔，韩国

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.22395 | **PDF**：https://arxiv.org/pdf/2610.22395.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对GPTQ/AWQ等PTQ方法在ASR上2-3比特量化即严重退化、甚至产生幻觉循环的问题，本文指出根源是语音激活的时序冗余：稳态与零填充帧在Hessian中均摊权重，淹没了承载音位区分信息的过渡帧。作者提出DiffAQ——一种无需训练的GPTQ修改，用帧间激活差衡量声学变化速率，并据此加权Hessian重要性，把量化精度集中到音位关键帧。在LibriSpeech与FLEURS、三种Whisper尺寸上，2/3比特WER持续下降，2-bit收益最大：Whisper Medium test-other从17.53%（GPTQ）降至12.93%。

### 🔧 技术方案

**问题背景：** Whisper边缘部署受内存带宽限制，LLM上成功的GPTQ/AWQ直迁ASR在2-3比特严重失效，根源是模态差异：文本token信息密度均匀，而语音log-Mel特征25ms窗10ms步进造成60%帧重叠，且Whisper强制30秒上下文（3000帧），3秒语音含2700个填充帧，标准Hessian把量化容量耗在重建静音上。

**模型架构：** 不改模型，仅重写GPTQ校准流程：抽取编码器各层中间隐激活x_t（T×D矩阵），用帧级重要性权重w_t缩放每帧外积、累加加权Hessian，再交给原Cholesky求解。DiffAQ仅作用于编码器线性层；解码器生成离散token无时序冗余，沿用标准GPTQ。量化为非对称逐组（group size 64），目标W2A16/W3A16。

**核心创新：** (1) 帧间时序差分重要性度量：取d_t为帧间激活差L2范数，零填充帧差分为零被自然清除，重叠导致的稳态冗余帧权重极低，音位边界过渡帧获得最大Hessian权重，与RASTA滤波抑制慢变分量的思想一致。(2) 归一化带下限加权：将d_t按序列均值归一化后取w_t=α+(1−α)·d_t_bar，常数下限α=0.2防止Hessian奇异；平均帧w_t=1.0与标准GPTQ等价。(3) 免训练、零开销：仅新增逐元素减法与归一化，相对GPTQ的O(D³) Cholesky可忽略，校准时长几乎不变。

**训练策略：** 无任何训练与损失函数，纯PTQ校准：从LibriSpeech train-other-500随机抽128条utterance作校准集，10个随机校准种子取均值并报95%置信区间；α取{0,0.1,0.2,0.3}时WER几乎不敏感（LibriSpeech差<0.2%，FLEURS差<1%）。

### 📊 实验结果
**数据集**：LibriSpeech test-clean/test-other 与 FLEURS 英文子集（域外），模型Whisper base/small/medium（约74M/244M/769M参数）

**主要指标**：
- Whisper Medium 2-bit WER：clean 7.93%、other 12.93%、FLEURS 12.07%，较GPTQ（13.73/17.53/18.05）分别降5.80/4.60/5.98
- 3-bit：Medium test-other 6.08%优于GPTQ 6.21%；Small FLEURS 8.69%较GPTQ 11.37%降2.68个百分点
- 2-bit基线：RTN/AWQ大量>100%退化，AWQ仅选中1个通道组几乎等同RTN；FP16基线Medium clean/other为2.73/5.69%
- 内存收益：Medium 2-bit权重从约1.5GB（FP16）压至200MB以下

**是否开源**：暂无

### ⭐ 评分：6/10
评分理由：选题切中低比特ASR量化的真实痛点，方法极简、免训练、零额外开销，实验含10种子与置信区间、域外集与α敏感性分析，2-bit收益显著。局限同样明显：3-bit增益微小，Base级模型仍整体失败说明容量瓶颈无法靠校准突破，且仅评测Whisper编码器、未验证噪声瞬态场景。属增量但可即用的工程贡献。

---

## Advancing Sentence-Level Dysarthric Audio-Visual Speech Recognition via Test-Time Adaptation

**arXiv ID**：2610.23117 | **方向**：语音大模型

**作者**：Shiyao Wang, Hui Wang, Jiaming Zhou, Shiwan Zhao, Yong Qin

**机构**：南开大学交叉学科高等研究院

**发布日期**：2026-10-19 | **论文**：https://arxiv.org/abs/2610.23117 | **PDF**：https://arxiv.org/pdf/2610.23117.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对构音障碍音视频语音识别（DAVSR）停留在词级小词表、且对未见说话人依赖有监督微调两大瓶颈，本文将任务推进到句子级连续识别：一方面提出源语音搜索切分管线，把预切分句段与CDSD原始视频对齐，构建句子级语料；另一方面首次将基于序列级广义熵最小化（SGEM）的无监督测试时自适应（TTA）系统应用于AV-SUPERB与ViSpeR两个骨干。实验显示ViSpeR配TTA-10将说话人44的CER由146.5%降至99.6%、说话人06降41.4个百分点，配对t检验p<0.05。

### 🔧 技术方案

**问题背景：** 现有DAVSR多限于词级任务与小词表，难以支撑真实交流；且说话人适配高度依赖目标说话人有监督微调，在构音障碍年龄、病因、严重度异质性下对未见说话人泛化差。句子级资源稀缺，CDSD以原始未切分视频发布，须大量预处理。

**模型架构：** AV-SUPERB以LRS3预训练AV-HuBERT为上游（音视频特征提取前端+12层Transformer+交替LayerNorm），下游两层BiLSTM解码；ViSpeR解耦模态，Conv1dResNet提音频、Conv3dResNet提唇部视频，各接12层Conformer编码器，跨模态融合后经6层Transformer自回归解码器与CTC双分支输出。TTA在每个测试样本上以SGEM损失适配，完成后用缓存参数复位，避免跨样本偏差与灾难遗忘。

**核心创新：** (1) 源语音搜索切分：单调匹配保证时序一一对应防重复对齐，滑窗等长Fbank特征按最小欧氏距离定位候选段，失配样本重遍历至多3次并经4名标注者声学-文本-视觉一致确认，8位说话人中7位对齐可用率超97%（44号仅22.2%），将原始视频转为句子级语料。(2) 首次在多模态DAVSR系统验证无监督TTA：无需目标说话人标签，推理期仅在未标注测试流上以β阶广义熵最小化+低于阈值负采样联合优化，绕开说话人特异微调。(3) 适配范围消融揭示架构依赖规律：模块化的AV-SUPERB只动Feature前端最优；紧耦合端到端的ViSpeR则全参数开放最优。

**训练策略：** LOSO三设置：AS-1在Aligned CDSD子集训练、AS-2用CN-CVS零样本、AS-3将AS-2在CDSD上微调；训练损失10轮停滞即停，中文字表5536字。TTA用AdamW+余弦退火，迭代1/3/5/10次，温度T=2.5、阈值τ=0.4/C；四组超参：LayerNorm（η 2e-4→2e-5，β=1.5，λ_NS=1）、Feature（4e-5→2e-5）、Module-Specific（4e-6→2e-6，β=1.25，λ_NS=0.5）、All（4e-7→2e-7）。

### 📊 实验结果
**数据集**：Aligned CDSD句级子集（8人、约8小时、每人约1小时；原始视频单条最长744秒）；CN-CVS（News约1.3万条/28人/35小时，Speech约19.3万条/2500+人/273小时）。

**主要指标**：
- AV-SUPERB CER：说话人01 AS-1 88.4%→87.1%、AS-2 74.4%→71.0%、AS-3 75.0%→72.5%
- ViSpeR CER：说话人01 58.9%→47.1%（Δ11.8，TTA-10）、说话人06 139.3%→97.9%、说话人44 146.5%→99.6%（Δ46.9）
- 关键对比：相对未适配基线，TTA配对t检验均p<0.05；个别说话人在AS-1/AS-2出现最多0.9个百分点的轻微回退

**是否开源**：论文未附自身代码，作者声明分割脚本将开源；基线AV-SUPERB与ViSpeR代码分别在GitHub公开。

### ⭐ 评分：6/10
评分理由：首次将TTA引入句级DAVSR并同步补上句子级多模态语料管线，问题真实、数据工程扎实，架构依赖的适配范围规律有工程指导价值；但识别错误率仍处高位（最优47.1%），仅8位说话人规模偏小，缺少与LHUC等有监督适配及其他TTA方法的同框对比，逐样本迭代适配推理开销大，属有参考价值的增量探索。

---

## 📄 更多语音论文（紧凑列表）

> 以下 2 篇为当日语音相关论文，未进入精读队列，仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），按预估评分从高到低排列。

**JAVIS: Joint Audio-Visual Interaction and Streaming for Real-Time Conversational Agents**
- **arXiv ID**：arXiv:2610.22499 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.22499（未精读，按摘要评分）

**Rethinking Magnitude Compression in Spectral Losses for DDSP Parameter Estimation**
- **arXiv ID**：arXiv:2610.22962 | **方向**：语音前端 | **评分**：5/10 | **链接**：https://arxiv.org/abs/2610.22962（未精读，按摘要评分）

*Subagents used for reading: 15* | Generated on 2026-10-19 语音论文批次, by Kimmy's research agent | Powered by VAgent SpeechAI Researcher
