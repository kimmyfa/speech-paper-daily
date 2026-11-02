# 2026-10-30 语音论文速递

**共收录**: 23 篇 | **语音大模型**: 15 篇 | **语音前端**: 8 篇

> 目标日期 2026-10-30（北京时间）arXiv 语音相关论文共命中 23 篇。
> 以下是按评分排序的结果。

### 速递说明

本批次精选前 15 篇进行完整模板精读，按评分由高到低排序；其余 8 篇论文仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），未展开精读。

---

## [1] Streaming Speech Recognition on a Microcontroller: a 65.7M-Parameter Transducer in 2 and 4 Bits on the ESP32-P4

**arXiv ID**：2610.38739 | **方向**：语音大模型

**作者**：Billal Boumedine

**机构**：阿尔及利亚科学技术大学（USTHB）计算机科学学院

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.38739 | **PDF**：https://arxiv.org/pdf/2610.38739.pdf | **代码**：https://github.com/BoumedineBillal/esp32-pie-asr | **Demo**：https://huggingface.co/BoumedineBillal/esp32-pie-asr-kroko-en

### 📌 简介
本文在无神经加速器的 ESP32-P4 微控制器（双 400MHz RISC-V 核、PIE SIMD、32MB PSRAM）上流式实时运行 65.7M 参数 Zipformer2 transducer（Kroko）。全程零训练：按逐矩阵敏感度将 290 个编码器矩阵存入 Hadamard 旋转分组的 2/4bit 格式，依次输出校正、GPTQ 舍入与组范数搜索，71MB int8 权重压至 26.65MB；激活 int16/动态 int8，手写 PIE 核与 PC 构建逐位一致。beam=4 时 LibriSpeech test-clean/-other WER 为 4.34%/10.26%（原模型 3.94%/9.17%），端到端 0.90s/1.28s 音频，超实时。

### 🔧 技术方案

**问题背景：** 现有 MCU 语音识别要么是 ESP-SR 式固定命令词表，要么超不过实时（Oído 13M Conformer-CTC 需 1.97 倍音频时长）；开放词汇流式转写所需数千万参数模型超出多数 MCU 内存与算力。

**模型架构：** Kroko 为 icefall Zipformer2 medium：65.7M 参数、650 BPE、无状态 decoder 加 joiner；编码器含卷积前端与 6 个 stack 共 16 层，帧率呈 U 型（50/25/12.5/6.25Hz），每层 3 个 FF、非线性注意力、共享权重的双 self-attention、双卷积与学习 bypass。流式每 1.28s 输入 128 帧 80 维 log-mel，出 32 帧@25Hz，每 stack 留 5.12s 左上下文，无前视。

**核心创新：** (1) 免训练 2/4bit 混合精度：按逐矩阵敏感度误差/字节比在 25MB 预算内向 4bit 升配（193 个 4bit、97 个 2bit），输出邻 stack4/5 全 4bit，参数近半的 stack3 仅 13.8% 4bit。(2) 顺序舍入：每矩阵用部分舍入模型的输入解阻尼最小二乘向原输出校正，搜索 10 候选组范数后在旋转基内 GPTQ 逐列舍入、经 Cholesky 分摊误差；校正必须逐矩阵，整层合并使误差 0.034 恶化到 0.33。(3) 整数化与逐位一致引擎：乘积输入按帧 2 的幂动态缩放至 int8（静态缩放 SNR 26.1dB 对 37.8dB），非线性用查找表；PC 构建以四则运算自建超越函数并关 FMA 融合，逐位复现芯片。

**训练策略：** 方法零训练，仅用 FLEURS 训练集 512 条（87 分钟）校准且不用转录，舍入约 25 分钟（RTX 4060）。16MB 尝试经训练：裁剪 stack3 FF 至 56.31M、12.4h 音频蒸馏输出，再 1480 步 QAT，止步 19.63MB/5.63%。

### 📊 实验结果
**数据集**：LibriSpeech clean（2620 条/53029 词）与 other（2939 条）、FLEURS 英文(US)（647 条/1.77h）、Common Voice 17.0（1000 条/1.65h）、140 条 TTS；Whisper 正则化。

**主要指标**：
- WER 4.34%/10.26%：LibriSpeech clean/other（beam 4，芯片管线；greedy 4.52%/10.89%）
- 落后 int8 发布模型 +0.40/+1.09/+2.26/+1.09 点（clean/other/FLEURS/CV）；模拟器证差距全在权重，整数算术零代价（float 4.53% 对芯片 4.52%）
- 速度：每 1.28s 音频端到端 0.90s（RT 0.70 含搜索），编码器 51.3s 优化至 620ms；词延迟中位 1.9–2.3s
- 消融：最近舍入 8.83%，+GPTQ 4.75%，+校正 4.68%，+范数搜索 4.50%；全 2bit 仍 13.40%
- 短语偏置：140 TTS 条 WER 19.5%→3.4%

**是否开源**：引擎/固件/评测脚本开源 @ https://github.com/BoumedineBillal/esp32-pie-asr（Apache-2.0），2/4bit 权重见 HuggingFace；转换代码未开源，Algorithm 1 可复现。

### ⭐ 评分：8/10
评分理由：系统级工程贡献扎实：免训练把 71MB 权重压到 26.65MB，首次在 MCU 上实现超实时流式开放词汇识别，逐位一致使指标可在全测试集验证，消融与失败清单诚实。精度代价 +0.4 点可接受，短语偏置实用。不足：单作者技术报告、仅英文、未测能耗与噪声，方法未在第二模型验证迁移性。

---

## [2] Discovering Interpretable Acoustic Features in Autoregressive Voice-Cloning TTS Models

**arXiv ID**：2610.40505 | **方向**：语音大模型

**作者**：Anuj Diwan, David Harwath, Eunsol Choi

**机构**：University of Texas at Austin, New York University

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.40505 | **PDF**：https://arxiv.org/pdf/2610.40505.pdf | **代码**：https://github.com/ajd12342/voice-cloning-interp（计划释出） | **Demo**：https://anonymous.4open.science/w/tts_interp_demo/

### 📌 简介
零样本语音克隆TTS能用几秒参考音频合成未见说话人声音，但其内部表征并利用了哪些声学属性尚不清楚。本文提出基于特征的机械可解释性框架：将Qwen3-TTS等自回归克隆模型残差流激活经TopK SAE、PCA、随机方向转换为话语级特征，用稀疏探测、生成时操控与定量自动可解释性三条管线评估。实验表明模型编码音高、能量、噪声、口音、情感等概念但仅部分可被少数特征稀疏预测，且强探测不一定转化为强操控；SAE在人类标注概念稀疏预测与新概念发现上最优，发现经自动验证的特征覆盖说话人簇、说话风格与录音条件。

### 🔧 技术方案

**问题背景：** 既有语音SAE可解释性工作聚焦编码器而非生成模型，既有TTS可解释性研究只考察非克隆模型中的预定义概念；SAE相对PCA等简单基线在语音克隆生成模型中是否更优、表征可预测性能否因果转化为生成控制，均缺乏系统回答。

**模型架构：** 主模型为Qwen3-TTS-12Hz-0.6B-Base：自回归骨干逐帧预测第一码本token，多层MTP模块预测其余码本token，无显式风格监督；扩展至Fish S1-mini/S2 Pro、Higgs TTS 2/3、CosyVoice2-0.5B。teacher-forced前向提取语音区残差流激活（Qwen3-TTS取早/中/后5层），经逐层TopK SAE（硬稀疏字典）、PCA主方向、与SAE等宽随机单位方向、untrained SAE转为句级特征（max-pool），再做top-特征L1逻辑回归探测与推理时残差流干预。

**核心创新：** (1) 跨特征集×跨模型的统一评测：按正负均值差排序特征、仅用top-特征训练稀疏探针并以相对常正类基线归一的nF1量度稀疏可恢复性，在6个模型上对比四类特征，纠正"SAE必然最优"的默认假设。(2) 无监督字典的生成时操控：以带符号top-特征方向之和、按激活标准差缩放注入指定层残差流，并沿预期生成长度线性衰减以避免均匀干预随时间累积漂移，用Target Change/Off-target change/配对WER、UTMOS量化因果效应与副作用。(3) 定量自动可解释性管线：Gemini Flash基于高激活vs对比音频生成自然语言标签，用Coherence（找异类）、Label Fit（held-out检测）、Label Stability（重标稳定性）三阈值联合验证，另以MTurk人工Label Fit独立校验。

**训练策略：** 主语料混合LibriTTS-R、MSP-Podcast、Emilia、VoxCeleb、VCTK、ESD、RAVDESS、EARS共8个数据集数千小时语音，按说话人ID八二分划分feature-fitting/analysis两split，杜绝说话人泄漏；SAE用Adam加线性warmup训练，含死特征辅助损失，decoder方向每步投影为单位范数，逐层按EV-死特征率曲线扫描字典宽度与topk，选定k=32；探针为sklearn liblinear的L正则逻辑回归，决策阈值在验证集F1上调优。

### 📊 实验结果
**数据集**：8源混合主语料（按说话人ID划分）；ParaSpeechCaps人工标注概念集（气声、英音、耳语等21个tag概念）；操控评测用源音频+LibriTTS-R test-clean目标转写；探测覆盖PENN音高、RMS、Brouhaha SNR、Praat抖动/谐噪比、emotion2vec、口音等提取器概念

**主要指标**：
- 稀疏探测：6模型上SAE对人类标注概念的top-特征nF1均高于PCA；而PCA与随机方向的全特征提取器概念可恢复性超过SAE，SAE仅在Qwen3-TTS稀疏提取器预测领先
- 层间趋势：提取器概念早层即可恢复、稀疏可恢复性后期最强；耳语概念在所有模型均强稀疏可恢复
- 操控：Qwen3-TTS与Fish中SAE Target Change与PCA及监督DiffMean相当，off-target小于PCA、WER/UTMOS代价低于PCA；随机方向探测相当却近零Target Change；探测与操控相关性弱（Spearman低）
- 自动解释：SAE在三项指标最高且验证特征最多，发现约百量级经自动验证的特征，覆盖旁白/播客等说话人簇、笑声耳语风格、背景音乐混响录音条件；人工Label Fit验证特征显著高于未验证者
- Higgs TTS3的SAE操控严重劣化语音，暴露跨架构不稳定

**是否开源**：代码将释出 @ https://github.com/ajd12342/voice-cloning-interp；演示与新特征浏览器 @ anonymous.4open.science

### ⭐ 评分：7/10
评分理由：首个面向零样本语音克隆TTS的横向可解释性系统研究，6模型对比给出"SAE利于稀疏探测与新概念发现、PCA利于密集探测与操控"等务实结论，定量自动可解释性加人工复核的设计明显优于纯定性解读。不足是自动验证依赖Gemini自身感知、部分结论偏英语、缺主观MOS，且Higgs TTS3上失败说明方法鲁棒性有限；整体属有实质贡献的扎实工作。

---

## [3] EmpDPO: Enabling Emphasis Control in TTS via Direct Preference Optimization

**arXiv ID**：2610.39427 | **方向**：语音大模型

**作者**：Haonan Chen, Yunyun Wang, Megan Wei, Zeyu Jin

**机构**：Adobe Research（美国）；Brown University（美国）

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.39427 | **PDF**：https://arxiv.org/pdf/2610.39427.pdf | **代码**：暂无 | **Demo**：https://chaonan99.github.io/empdpo-demo/

### 📌 简介
针对从未见过重音标注的预训练TTS模型如何事后获得词级重音控制的问题，本文提出EmpDPO：先用现成多语种重音检测器给真实语音打伪标签做SFT，再用同一检测器对SFT模型采样输出打分构造偏好对，以Diffusion-DPO强化重音跟随能力，全程无需人工标注或定制奖励模型。在210句×8音色、6语种的评测中，DPO将目标词重音增益从SFT的0.069提到0.136，超过最强公开系统Fish-S2（0.129），主观重音强度3.56/5居首且自然度3.47保持与基线持平，仅用5171对偏好数据与1万步训练即达成。

### 🔧 技术方案

**问题背景：** 词级重音传达文本无法表达的对比重心。现有方法或依赖昂贵的词级重音标注，或局限于音高/能量/时长等少数声学参数且语言依赖；线上RL类方法（GRPO）需定制奖励与在线采样，落地成本高。

**模型架构：** 基座为类DMOSpeech teacher的多语种零样本潜空间扩散TTS：文本经冻结T5编码、IPA音素经嵌入表编码，目标与参考音频共用冻结DAC编码为潜帧；流匹配模型预测速度场去噪，E积分采样后由DAC解码。重音标记用<emp></emp>同时包裹文本与音素路径。

**核心创新：** (1) 检测器闭环全自动标注：同一多语种重音检测器（7语种训练、零样本迁移）给SFT打伪标签（阈值0.35）并给DPO候选打分，免除人工标注与奖励模型。(2) 组合评分构造偏好对：对每输入生成K=5带标记候选与N=3无标记基线，按最小/平均重音增益与选择性（非目标词低于目标最低分的比例）加权0.6/0.4/0.3排序，取最高最低为chosen/rejected，防止整句变响的伪重音。(3) 强制replay锚定：纯Diffusion-DPO约2k步后去噪误差爆炸，加入λ=0.1的原始去噪损失；实证语料replay优于chosen replay。

**训练策略：** 预训练700k步、300k小时、21语种内部数据；SFT用258k条（711小时，45%带标记）；偏好对硬过滤CER≤0.20、NISQA≥2.0、SIM≥0.15、削波≤0.001、增益≥0.20（ja/zh为0.15），得5171对；DPO跑10k步，8卡、batch 32对+64条replay，AdamW，lr 2e-5，β=0.1。

### 📊 实验结果
**数据集**：内部300k小时21语种预训练语料；评测为德英西班牙非法中日6语种×35句、8参考音频（男女各4）、每输入3次采样；主观测试经Prolific招募母语者共364人次。

**主要指标**：
- 目标词重音增益：Ours-DPO 0.136±0.005 vs Ours-SFT 0.069±0.003、Fish-S2 0.129±0.005、WordVoice 0.074±0.008、Qwen3-TTS 0.017±0.003
- 主观重音强度：DPO 3.56±0.07，显著高于Base 2.73、SFT 3.15、Fish-S2 3.25；自然度3.47±0.08持平Base/SFT，而Fish-S2 2.90、WordVoice 3.13显著更低
- 质量保持：CER 0.008、SIM 0.49、UTMOS 3.55、NISQA 4.34，与plain输入相当；错误重读率Q3 32%
- 关键对比：较SFT重音增益+0.067，replay消融显示chosen replay会响5.7 dB且NISQA从4.4跌至3.7

**是否开源**：代码未开源（暂无），提供音频Demo页 https://chaonan99.github.io/empdpo-demo/

### ⭐ 评分：7/10
评分理由：把Diffusion-DPO用于事后加控制信号是干净实用的配方，检测器闭环免去人工标注与奖励设计，5千对1万步即超越Fish-S2等强基线，且用replay消融揭示了DPO漂移失稳这一可复用的工程经验；六语种客观+母语者主观评测较充分。不足在于基座、数据均为内部资源无法复现，未给出与SFT等算力对齐的完整消融，检测器同源评分也可能高估自身增益，总体属扎实的增量工作而非范式突破。

---

## [4] What Makes a Good Audio Prompt for Zero-Shot TTS? Learning Prompt Selection from Synthesis Outcomes

**arXiv ID**：2610.40372 | **方向**：语音大模型

**作者**：Arnon Turetzky, Yossi Adi

**机构**：The Hebrew University of Jerusalem

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.40372 | **PDF**：https://arxiv.org/pdf/2610.40372.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
零样本TTS需从说话人长录音中截取短prompt，但选哪段、怎么选缺乏量化依据。本文在1500余条YODAS YouTube录音（每条19个候选prompt）上用Qwen3-TTS 0.6B/1.7B、F5-TTS、Chatterbox四个模型合成数十万条输出，发现prompt选择实质且稳定地影响可懂度、自然度与说话人相似度，而常规按UTMOS/DNSMOS预测质量选优只恢复自然度收益、错过大部分可懂度收益；进一步以合成结局为标签训练1.4M参数音频打分网络，仅凭候选音频排序。在held-out录音上其选择使WER相对随机prompt降低32%（Qwen3-TTS）至43%（F5-TTS），超过预测质量规则且逼近需每候选合成大量句子的探测式选择。

### 🔧 技术方案

**问题背景：** 实践中prompt须由用户从长录音截取，选段直接决定克隆质量；常用做法是取非侵入式质量分最高的候选，但"听起来干净"不等于"模型说得清楚"，且同一预测器既选择又评判会高估规则收益，缺乏以真实合成结局度量的系统性研究。

**模型架构：** audio selector由冻结Whisper-base编码器（21M，末层特征聚合至40ms帧）加1.4M可训练头构成：线性投影到256维、正弦位置编码、两层4头Transformer、注意力池化；prompt向量拼接其与整段录音均值向量之差后送入512→256→6的GELU打分头，六头分别预测平均WER、录音内WER排名、失败率、UTMOS、DNSMOS、ECAPA相似度，按WER排名头选择，5个不同初始化的网络取平均分。对照基线含UTMOS/DNSMOS规则、21描述符线性ranker与probe selection（每候选12次合成）。

**核心创新：** (1) 首次以"合成结局"大规模定义并度量prompt选择问题：每个候选配5句目标文本×3种子共15条输出计算outcome，并用ICC证明相当比例的输出方差来自prompt而非种子，即好坏可学。(2) 揭示预测质量规则的盲区与自评偏差：UTMOS规则仅捕获probe selection自然度收益的41%，按held-out Audiobox裁判只捕获18%，对F5-TTS为零。(3) 提出从合成结局学习的轻量排序网络，推理端零合成即可选prompt，且加UTMOS头（w=0.25）无需重训即可在可懂度与自然度间按曲线权衡。

**训练策略：** ListNet（温度1）对每录音19个候选做listwise排序，亦可用pointwise回归（差异约0.1pp）；AdamW，学习率1e-4、权重衰减1e-2，batch 16条录音、10 epochs、bf16训练，782条训练录音（14.8k prompts）单GPU数分钟训完；标注约每输出一至2.5秒L40S GPU时间，每模型100–270 GPU小时；ECAPA余弦>0.5的同声录音从训练集剔除（944中去162），5折交叉验证同声同折。

### 📊 实验结果
**数据集**：YODAS英文YouTube录音（CC-BY，每条30s切19候选），train 782/dev 200/两个test各200条，另用LibriSpeech加噪对照；输出由Whisper large-v3、UTMOS22、DNSMOS P.835、Audiobox、ECAPA-TDNN评分。

**主要指标**：
- ΔWER：1.36pp（相对随机prompt降32%，Qwen3-TTS 0.6B held-out 400条），比UTMOS规则多0.54pp、与probe selection（1.35pp、228次合成/录音）持平；失败率Δ0.87pp
- ΔWER：F5-TTS相对降43%，超最强基线DNSMOS规则1.45pp；加UTMOS头保留1.33pp WER收益并在DNSMOS/Audiobox上与规则持平；72条录音听测未见自然度劣势
- 消融：换用prompt自身UTMOS作标签收益减半（0.63pp）、CLAP编码器仅0.42pp——收益来自结局监督而非表示
- 模型共识：说话人相似度的优劣prompt跨模型Spearman 0.68–0.88，WER仅0.08–0.64；跨模型迁移达目标模型probe收益的51%–85%

**是否开源**：论文声明"接收后释出代码"，当前暂无。

### ⭐ 评分：7/10
评分理由：以数十万条合成为四个开源模型建立"结局导向"的prompt选择度量，实验设计严谨（held-out裁判、同声泄漏清理、测试前冻结、换识别器/换字幕稳健性检验），洞察实用：质量规则选"干净"而非"可懂"，小选择器零合成即逼近探测式选择。局限在仅英文、听测仅7人、未评韵律表现力，方法偏增量。

---

## [5] SpeakerTurn: Target-Speaker Semantic Turn Detection in Multi-Speaker Environments

**arXiv ID**：2610.39828 | **方向**：语音大模型

**作者**：Nan Li, Hetao Shan, Jintao Liang, Jiahao Yan, Longbiao Wang, Tubin Huang, Min Xu

**机构**：天津师范大学；天津大学人工智能学院；上海深奇迹源智能终端有限公司

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.39828 | **PDF**：https://arxiv.org/pdf/2610.39828.pdf | **代码**：https://github.com/linan2/SpeakerTurn | **Demo**：暂无

### 📌 简介
多说话人环境下仅凭语义完整性无法判断助手何时应答：完整话语可能属于干扰说话人，而注册用户可能仍在说话、附和或请求等待。本文提出SpeakerTurn，在CocktailASR-1之上以LoRA联合生成目标转写与语义轮次状态，区分complete/incomplete/backchannel/wait/target-absent五态并单列interrupt/ignore打断任务。合成双语测试上五态macro F1达0.811、目标CER 4.20%，10组参考换扰打断对全部判对；结构化CoT降低CER却使轮次F1降至0.764，提示需联合评估归属、判别与转写。

### 🔧 技术方案

**问题背景：** 现有轮次检测（Easy Turn、Smart Turn）只看混合音频判完整，不注册、不分归属；个人VAD只给声学线索，不表达backchannel/wait等语义状态，全双工系统易被他人完整句误触发应答。

**模型架构：** 继承CocktailASR-1冻结的Data2Vec2编码器+投影与Qwen3 LM后端；仅在query/value投影上加LoRA（144张量、7,667,712参数，rank 16、缩放32、dropout 0.05）。注册与混合语音一并输入，自由生成<answer>转写</answer>+<decision>状态</decision>；CoT变体前置<think>块（存在性/语义线索/助手上下文），无分离网络与分类头。

**核心创新：** (1) 提出说话人条件化语义轮次推断：五状态+独立打断二态任务，同一介入随注册参考改变需不同决策，把归属与语义绑定于同一接口。(2) 转写-轮次联合监督：L=L_text+L_decision+0.2L_CoT+0.1L_EOS，使语义决策锚定目标内容，非目标介入用空转写。(3) 结构化Turn-CoT消融：以标签模板化中间监督检验其利弊，发现CoT改善转写却损害轮次判别，暴露语音LLM中间推理监督的权衡。

**训练策略：** Qwen3-8B+deepseek-flash生成双语文本计划，CosyVoice2-0.5B合成语句；注册参考取AISHELL-1/LibriSpeech的1–4s语句；场景含目标-only、双/三说话人重叠与加噪（SNR 5–20 dB）、16 kHz。训练池115,204条（观测前缀303.74 h）；各变体训练219,037步含54,759次ASR回放，AdamW、lr 1e-5、批大小1、梯度裁剪1；推理贪婪限384 token。

### 📊 实验结果
**数据集**：自建合成双语多说话人语料（原始测试410/验证430/补充5,540条件；目标转写子集每分区350条、中英各175）

**主要指标**：
- 五态轮次检测：macro F1 0.811、准确率83.33%（n=390）；四态F1 0.779、二态F1 0.804
- 目标转写：CER 4.20%（中1.01%、英WER 6.48%），CoT变体降至2.56%
- 打断任务：10/10参考换扰对全部判对（turn-only基线8/10）；40个target-absent条件全对且转写为空
- 关键对比：五态F1较冻结CocktailASR-1(0.197)提升0.614，四态远超Easy Turn(0.312)；CER较原生30.69%降26.49个百分点；无注册的Whisper large-v3等CER均超73%
- CoT代价：五态macro F1从0.811降至0.764，backchannel召回从52%跌至32%

**是否开源**：声明将发布代码与合成脚本 @ https://github.com/linan2/SpeakerTurn，Demo暂无。

### ⭐ 评分：7/10
评分理由：把说话人归属、语义轮次与目标转写统一到单LLM联合生成接口，LoRA适配轻量且协议设计清晰，多任务对照暴露了CoT负收益这一有诊断价值的发现。但评估完全依赖合成语音、生成器定义截断点与单一训练种子，backchannel标签存疑，真实录音、混响与流式延迟下的可用性未验证，过早判完错误仍集中，落地前需真实数据复现。

---

## [6] Do Audio LLMs HEAR Pain? Tracing Acoustic Evidence from Speech to Language Reasoning

**arXiv ID**：2610.38570 | **方向**：语音大模型

**作者**：Wenqi Li, Xiangjue Dong, Sulaiman Vesal

**机构**：Microsoft

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.38570 | **PDF**：https://arxiv.org/pdf/2610.38570.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
大型音频语言模型能否利用语音中非词义的声学信息尚不清楚。本文以疼痛为受控探针，基于TAME-Pain数据集（冷水升压诱导疼痛，同一说话人在疼痛下朗读词义中性的Harvard句子、并口头报告疼痛等级），提出HEAR四阶段诊断框架，从行为、编码、感知、使用四个环节追踪疼痛证据。在七个LALMs上，当疼痛只能从声音推断时所有模型接近随机（二分类平衡准确率约48-51%），疼痛被言明时则近上限（87.5-99.7%）；逐层探测显示浅层编码的疼痛信息与线索随深度衰减，把线索文本化回注提示可使成对预测提升最多32分。

### 🔧 技术方案

**问题背景：** 已有工作表明LALMs在副语言任务上高度依赖词汇内容，但失败原因不明：声学信息是缺失于模型、在内部丢失，还是存在却不参与推理？现有评测混淆两类证据，难以归因。

**模型架构：** 不训练新模型，构建HEAR四阶段框架。RQ1行为层：4设定（中性句、口报疼痛、同说话人成对、20-shot）×3输入模态的疼痛多选题，评测gpt-realtime系、Gemini系、Qwen2.5/3-Omni、Kimi-Audio共7个。RQ2编码层：在冻结的编码器/投影器/LM隐藏状态挂Linear、MLP、CRNN（两层1D卷积+2层BiGRU+注意力池化）探针逐层解码。RQ3感知层：用PSOLA、增益、搁架滤波构造夸张A/B对比。RQ4使用层：将eGeMAPSv02特征值以文本注入提示。

**核心创新：** (1) 词汇-声学对照设计：同一说话人同一疼痛条件下对比中性句与口报疼痛录音，无需编辑语音即可把行为差异归因于证据来源。(2) 逐层可解码性追踪：用说话人分组5折交叉验证训练探针，对帧级隐藏态池化后按特征组岭回归恢复R²，定量证明疼痛线索在编码器浅层最强、越深越弱，Kimi-Audio上趋势一致。(3) 感知-干预闭环：经人工校验（98.7%正确率）的对比感知测试按能否辨别线索划分模型，再以文本回注定位瓶颈：强模型能辨别大对比却不用于疼痛推理。

**训练策略：** 探针用类加权交叉熵、AdamW、batch size 8、梯度裁剪5.0、余弦调度含5% warmup、最多30轮、patience 7早停；层/头型由41个训练说话人分组5折交叉验证选定，10个测试说话人单次评估，标准化仅用训练集。数据剔除噪声后保留4,658条录音（51说话人）；openSMILE提取88维eGeMAPSv02，疼痛与特征均在说话人内中心化归一。

### 📊 实验结果
**数据集**：TAME-Pain（实验性急性疼痛，4,658条录音、51说话人、1-10自评疼痛分），LISTEN中性文本子集做泛化验证

**主要指标**：
- 中性Harvard句（仅音频）：7模型近随机，二分类平衡准确率48.1-50.5%、三类32.8-34.0%（随机基线50%/33.3%）
- 口报疼痛（仅音频）：二分类87.5-99.7%、三类81.0-99.5%，近上限
- 探测（Qwen2.5-Omni-7B）：CRNN编码器Block1二分类74.1%±1.6、三类45.0%，随深度衰减；88特征LightGBM基线65.7%
- 感知测试：人类98.7%；Gemini系与Qwen3-Omni多数线索72-100%，gpt-realtime系/Qwen2.5-Omni/Kimi近随机
- 线索文本注入：gemini-3.1-pro-preview成对二分类最高+32.2点（52.4→81.7）；LISTEN上Qwen3最高+7.79点

**是否开源**：暂无（数据受PhysioNet受限健康数据许可约束不重分发）

### ⭐ 评分：7/10
评分理由：受控的词汇-声学对照加上四阶段追踪，把LALM副语言失败定位为"早期编码存在、深层与输出不可及"的模态接口鸿沟，七个模型、说话人独立切分与双数据集验证使结论可信。局限是仅疼痛单一探针、样本较小且为急性实验疼痛，层级分析集中于Whisper初始化的两款开源模型，未给训练侧修复方案。对副语言评测与临床语音应用有直接参考价值。

---

## [7] The Importance of Speech Genre for End-of-Turn Detector Training

**arXiv ID**：2610.39742 | **方向**：语音大模型

**作者**：Rini Sharon, Kadri Hacioglu, Jeena Prakash, Andreas Stolcke

**机构**：Uniphore

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.39742 | **PDF**：https://arxiv.org/pdf/2610.39742.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
该研究聚焦语音对话系统轮次结束（EoT）检测中被最少关注的维度——训练数据语音体裁，首次将其作为唯一受控变量：用同一标注管线构建人类多轮对话（Conv-10K）与人机单轮（ST-10K）两个配对语料，分别训练同一1.8M参数流式ConvLSTM检测器并在四个测试集评测。对话训练模型F1达0.760–0.959，最高领先单轮训练+0.45，增益主要来自中途停顿的误报下降（CASPER上FA% 6.6%对44.7%）。该模型在全部测试集F1超过含8M SmartTurn v3在内的开源基线。

### 🔧 技术方案

**问题背景：** EoT研究长期沿特征、建模、模态三轴改进，训练数据构成这一轴最少被研究：多数工作只用单一语料，对话与单轮训练几乎无配对比较，增益无法归因于数据本身；判决粒度（帧级vs语句级）的影响也未被系统检验。

**模型架构：** 每10ms帧输入85维向量（80维log-Mel+归一化F0、F0差分、浊音/语音标志、累积静音时长）；33核/256通道Conv1D给出320ms前瞻，经LayerNorm+GELU进入2层单向LSTM（256隐单元、dropout 0.25），再经3层MLP+sigmoid输出逐帧EoT概率；共1.8M参数，隐状态跨chunk携带、可连续流式推理。

**核心创新：** (1) 匹配语料受控对比：单一可复现标注管线（VAD平滑、同通道<0.5s间隙合并、≤1.3s静音扩展、10ms帧标注）构建规模与标注规则完全一致的两个训练集，同架构同超参，使体裁成为唯一变量。(2) 两级粒度检验：帧级之外首次在语句级复现，设计静音匹配测试——完整/不完整样本统一保留150ms尾随静音，迫使判决依赖停顿前语音，跨Whisper-Tiny与wav2vec2两个冻结编码器验证。(3) 部署导向评测协议：单侧容差窗口（早于真值50ms内算对，更早一律误报），配合检测延迟δ、McNemar与bootstrap显著性检验。

**训练策略：** 二元交叉熵，正类权重w+=N_neg/N_pos=5.6；Adam，学习率3e-4，权重衰减1e-4，2轮线性warmup+余弦退火至零，梯度裁剪5.0，batch size 8（按长度排序）；最多30轮、验证F1早停patience 7；逐chunk携带隐状态以匹配流式推理。

### 📊 实验结果
**数据集**：Conv-10K/ST-10K各10k段（8kHz）；测试Int-5K（5k人工核验）、CASPER（2.5k对话）、ST-Complete（2.5k）、SLURP（2.5k命令）

**主要指标**：
- 帧级F1（对话vs单轮训练）：Int-5K .894/.444、CASPER .959/.694、ST-Complete .911/.738、SLURP .760/.558；差+0.17~+0.45（p<1e-70，共享τ=.7仍成立）；CASPER上FA% 6.6% vs 44.7%
- 语句级AUROC：对话训练高+0.21/+0.38（Int-5K/CASPER，Whisper-Tiny）、+0.37/+0.29（wav2vec2），SLURP持平
- 关键对比：本模型.894/.959/.911 vs 基线Silero .781/.734/.673、SmartTurn v3 .523/.390/.652（前三个测试集），参数少4.4倍

**是否开源**：暂无；内部语料私有，但CASPER/SmartTurn/冻结编码器公开，效应可公开复现。

### ⭐ 评分：7/10
评分理由：首次把训练体裁作为严格受控变量，隔离出EoT性能增益的数据来源，配对语料、静音匹配测试与显著性检验构成完整证据链；"只用单轮评测会掩盖对话训练收益"的结论对对话系统数据选择有直接实践纠偏价值。局限是英语电话单域、体裁与来源域仍有残余纠缠、内部数据不可复现，属增量但扎实的实证贡献。

---

## [8] Towards Multilingual End-of-Turn Detection using Frozen Speech Encoders

**arXiv ID**：2610.39755 | **方向**：语音大模型

**作者**：Rini Sharon, Kadri Hacioglu, Andreas Stolcke

**机构**：Uniphore

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.39755 | **PDF**：https://arxiv.org/pdf/2610.39755.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
语音对话系统的轮次结束（EoT）检测器通常需按语言重新训练标注并逐语调整判决阈值，扩展成本高。本文提出"冻结多语种编码器+单一小头"方案：固定Whisper-small编码器（768维/50Hz，读取第6层），仅训练一个L2逻辑回归探针，在CALLHOME五语种（英/西/德/中/日，74,646个样本）上研究零样本迁移、少样本适应与阈值复用。结果显示因果读取迁移缺口仅0.017 AUC，几小时目标语音即恢复至同语言上限0.004 AUC内，跨语言复用同一阈值仍维持3.5-6.5%虚警率，证明该组合是可部署的语言无关流式EoT基线。

### 🔧 技术方案

**问题背景：** 现有EoT/endpointing检测器逐语言构建：带标注轮次边界昂贵，生产系统还须按语言搜索重设阈值以满足虚警预算；此前跨语言研究均经ASR文本间接进行，声学信号本身的轮次转移能力从未被直接度量。

**模型架构：** 冻结Whisper-small编码器作特征提取器，768维/50Hz输出，读出层经源数据逐层扫描定为第6层；头部为标准化特征上的L2正则逻辑回归探针，容量五语种统一。两种读取模式：oracle整句双向作全上下文上限，causal以160ms分块流式、按音频前缀重算log-mel使特征逐位稳定，仅留10ms前瞻。触发器对帧分数EMA平滑（α=0.3），连续3帧超过阈值θ才发火。

**核心创新：** (1) 首次直接度量纯声学EoT的零样本跨语言迁移：冻结编码器+固定容量小头，语言为唯一变量，得5x5迁移矩阵；因果缺口0.017 AUC仅为oracle到causal下降（约0.07）的四分之一。(2) 部署导向的因果读取与固定工作点协议：消除卷积前端感受野与全局log-mel归一化两条未来信息泄漏路径，在线报告虚警率与延迟，并首次检验单一阈值跨语言是否保持。(3) 冻结与微调的系统对照：仅微调顶部两层虽使同语言因果AUC从0.888升至0.906，但因果迁移缺口扩大至0.023（CI互斥），证明冻结保留共享结构；冻结XLS-R-300m缺口同为0.009，结论不限于Whisper。

**训练策略：** 帧级标签以边界±collar W=10帧（200ms）为正、边界前超过G=W+5帧为负、后1.3秒不计分，类均衡训练；0.5s合并同类说话人片段，边界吸附Silero VAD（±0.4s）；按说话人不重叠50/25/25划分，L2强度仅在源语言调优，全语种同训练预算，置信区间用说话人块配对bootstrap。

### 📊 实验结果
**数据集**：CALLHOME无剧本两方电话会话660通（约99h原始音频，16kHz单声道），英/西/德/中/日五语种，规则生成74,646个标注样本（59.5h）。

**主要指标**：
- 零样本迁移缺口Δ：因果0.017 AUC（95%CI [0.016,0.019]），oracle 0.011；同语言因果对角均值0.888
- 少样本适应：中位数对15分钟恢复缺口25%、1小时一半，数小时后所有目标语言距自身上限<0.004 AUC（含最难的日语）
- 阈值复用：虚警率3.5-6.5%（目标预算5%），中位延迟-80ms、p95不晚于+80ms，与重调阈值相比中位延迟仅变0-20ms
- 关键对比：微调顶两层同语言+0.018 AUC但因果缺口恶化至0.023；仅位置基线0.47-0.59 AUC排除窗口位置捷径；XLS-R末层因果崩至0.670，第18层0.861恢复

**是否开源**：暂无。

### ⭐ 评分：7/10
评分理由：控制变量设计首次把"跨语言成本"与"因果化成本"定量拆分，统计严谨（说话人块配对bootstrap），含collar敏感性、非线性头、XLS-R复现等完整稳健性链；结论给出可直接落地的配方（单头+阈值复用+几小时适应）。不足在于仅限8kHz电话两方语音、五种语言与两个编码器，绝对性能约0.89 AUC，宽带噪声远场下的普适性待验证。

---

## [9] Who Called? V33DA: A Physically Verified Multimodal Benchmark for Vocal Attribution in Zebra Finch Groups

**arXiv ID**：2610.38109 | **方向**：语音前端

**作者**：Maris Basha, Yuhang Wang, Xiaoran Chen, Longbiao Cheng, Luca Yapura, Anja T. Zai, Mathieu Salzmann, Richard Hahnloser

**机构**：Institute of Neuroinformatics, University of Zurich and ETH Zurich；SDSC & CVLab, EPFL

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.38109 | **PDF**：https://arxiv.org/pdf/2610.38109.pdf | **代码**：https://github.com/marisbasha/v33da | **Demo**：暂无

### 📌 简介
群体场景中判断"哪只鸟在发声"是社交通信研究的入口，但现有资源要么只定位声源不给呼叫者身份，要么只识别孤立叫声的个体、不依赖3D候选几何，且均缺乏物理验证的真值。本文提出V33DA：基于BirdPark录制系统构建的多模态声学归属基准，含33,625个经体表加速度计振动信号物理验证的事件，同步提供5通道音频、三视角视频、标定3D位姿与逐鸟无线电遥测，并设计session-distinct、held-out实验、留一个个体（LOO）三种递进评测协议。24个基线显示：槽位索引模型SELDnet++在session达86.5%但LOO崩塌至0.0%，而保留显式空间推理的候选打分/定位优先方法可迁移至49.5–55.4%，验证通道参考上限91.3%，揭示身份捷径与可迁移空间归属的分离。

### 🔧 技术方案

**问题背景：** 声源归属的证据跨模态分布：声音到多个麦克风、候选动物在共享3D空间移动，而训练测试同鸟时高准确率可能只是"熟悉嗓音识别"而非可泛化的归属能力。现有基准标签或来自感知标注、或来自定位反推，存在循环监督风险。

**模型架构：** 录制端为5个标定麦克风（24,414 Hz）+三视角相机（47.68 fps）+4天线FM接收阵列，笼内3–4只斑胸草雀。标注管线：多通道WhisperSeg从体表解调信号提候选窗口；YOLOX-Pose每视角检测5关键点，OC-SORT跟踪，CIELAB背包色K-NN分派身份，DLT跨视角三角化3D位置，人工多模态复核。基线覆盖物理Reference（SRP/LoudestMic）、槽位头（SELDnet）、候选打分（SELDnet++、SpatialScorer、PairRank等）、定位优先（AudioANN/RadioANN/ACCDOA/EINV2/CST-former/BeamFusion）等24法。

**核心创新：** (1) 物理验证标签：叫声由发声时调制FM载波的胸廓振动信号锚定而非主观判断，39,329个复核候选经过滤后发布33,625个单呼叫者事件，避免"用定位定义标签再评定位"的循环。(2) 三协议拆分身份捷径：LOO留出一个鸟的全部正例，held-out实验完全无共享个体，使"熟鸟识别"与"陌生鸟空间归属"可分别度量。(3) 测试时模态干预：置零音频/打乱候选几何/置零无线电，直接检验各方法的实际证据来源。(4) V33DA++附带3,784个经验证的多人重叠事件与2秒上下文窗口，支持分离/VAD后续研究。

**训练策略：** 学习型基线统一多随机种子训练，报告种子均值±标准差；LOO先在折内平均种子再对10折求统计量；含早停与梯度裁剪；CST-former与Whisper candidate用SELDnet的60 epoch预算重跑以控制训练预算；验证通道对全部被测模型严格扣留。

### 📊 实验结果
**数据集**：V33DA（33,625验证事件；BP01/BP02/BP05=16,219/11,577/5,829；10只鸟；5声道24,414 Hz音频，均值150 ms；约74小时连续多模态录制提炼）

**主要指标**：
- Top-1归属（LOO）：EINV2 55.2%、ACCDOA 55.4%、SpatialScorer 49.5%、SRP物理基线53.5%，随机27.0%
- 槽位崩塌：SELDnet++ session 86.5% vs LOO 0.0%（AudioANN直接归属0.0%、经定位归属53.0%）
- 体表参考上限：session 99.2%、held-out BP01 91.9%、LOO 91.3%（候选条件定位误差3.3 cm）
- 3D定位误差：SpatialScorer LOO 19.7 cm，优于随机候选27.1 cm约7.4 cm
- 模态干预：置零音频降25–30点、打乱几何降27–33点、置零无线电<1点；近距<10 cm时ACCDOA从73.0%降至46.6%
- 无参考通道时k-means聚类仅NMI 0.61/ARI 0.58，凸显物理验证价值

**是否开源**：数据集CC BY 4.0 @ huggingface datasets songbirdini/v33da（含V33DA++），代码 @ https://github.com/marisbasha/v33da

### ⭐ 评分：7/10
评分理由：物理验证的群体叫声归属基准填补了"定位不给身份、识身份无场景几何"的空白，三协议拆分身份捷径的设计严谨，24基线加干预实验的shortcut-learning结论有普适参考价值。局限在单一安装环境、仅10只鸟且无线电被弱特征摘要稀释，跨设施泛化未验证；任务偏生态声学，对通用语音前端工程迁移有限。

---

## [10] AKDQ: Adaptive Key-Delta Quantization for Low-Bitrate RVQ-based Neural Speech Codecs

**arXiv ID**：2610.39885 | **方向**：语音前端

**作者**：Xiao-Hang Jiang, Yang Ai, Zhen-Hua Ling, Ji Wu

**机构**：中国科学技术大学语音及语言信息处理国家工程研究中心；清华大学电子工程系

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.39885 | **PDF**：https://arxiv.org/pdf/2610.39885.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
RVQ神经语音编解码器对每帧固定分配相同数量码本，而相邻语音帧高度相似，独立量化造成码率冗余，低码率下尤为昂贵。本文提出即插即用的自适应关键-增量量化AKDQ：K帧用全部VQ量化作为参考锚点，D帧仅对帧间残差用少量VQ量化，由bit-bank驱动的因果调度器在目标码率下决策K/D，不改动编解码骨干、无需额外可训练模块。在LibriTTS上，DAC上1.5kbps的重建质量接近基线RVQ 2.0kbps，节省25%码率；1.0kbps下MOS从3.21提升至3.83。

### 🔧 技术方案

**问题背景：** SoundStream/DAC等RVQ编解码器每帧均匀分配码本，未利用相邻帧潜变量强相关性；直接减少VQ数或以FSQ等紧凑量化降码率往往需改架构或扩容量；已有的VRVQ虽可按帧分配但需引入可学习重要性子网络。

**模型架构：** 在编码器潜变量序列与RVQ瓶颈间插入两个模块：bit-bank驱动的K/D调度器输出逐帧模式标志d_t，K/D帧量化器据此选路——K帧 ẑ_t=Q_cK(z_t)，D帧 ẑ_t=ẑ_{t-1}+Q_cD(z_t−ẑ_{t-1})，两条路径复用同一组码本。基于iRVQ，c_K=4、c_D=1、码本大小M=1024、帧率50Hz、每帧1比特标志位，可行码率范围约0.925~2.05kbps；在因果谱域codec（MDCTCodec-S）与非因果波形域codec（DAC）两类家族上验证。

**核心创新：** (1) 关键-增量帧级量化策略：将帧间残差这一信息量更低的内容用浅层VQ编码，K帧保留完整参考内容，把内容自适应分配内置于原RVQ瓶颈，不新增任何量化器参数，纯插件式微调即可接入。(2) bit-bank闭环速率控制器：每帧按β=B_target/f_r−b_flag−c_D·log₂M存bits，选K帧支取Δb=(c_K−c_D)log₂M，配合难度分数s_t与EMA自适应阈值，经四条优先级规则级联，全因果、零前视、流式可用且实际码率自适应收敛到目标。(3) 递归参考下的微调对齐：D帧量化条件于带累积误差的ẑ_{t-1}，从预训练4-VQ检查点在AKDQ前向路径下微调使码本适配失真参考分布，避免直接切换导致的漂移崩溃。

**训练策略：** LibriTTS train-clean-100+360训练、dev-clean验证、test-clean评测（16kHz）；AdamW，单张RTX 3090；RVQ基线训练400k步，AKDQ从2.0kbps检查点200k步处分叉再微调200k步保持总预算一致；L_max=3、α=0.1、b_flag=1，B_target取1.0和1.5kbps。

### 📊 实验结果
**数据集**：LibriTTS 16kHz（train-clean-100/360训练，test-clean评测）

**主要指标**：
- DAC@1.0kbps：MOS 3.830±0.370 vs RVQ 3.210±0.555，UTMOS 3.674 vs 3.395（+0.28），STOI 0.905、LSD 0.894、SIM 0.961均优于基线
- DAC@1.5kbps：MOS 4.220±0.210，逼近RVQ@2.0kbps的4.330，即省25%码率
- MDCTCodec-S@1.0kbps：MOS 3.060±0.325较RVQ的2.440提升0.62，ViSQOL 4.001
- 速率控制：实际码率1001.4/1498.7bps贴合目标；消融中不微调版UTMOS崩至1.557，去delta编码版各项指标低于完整AKDQ

**是否开源**：论文未提供代码链接，暂无

### ⭐ 评分：7/10
评分理由：借鉴视频编码I/P帧思想解决RVQ帧间冗余，bit-bank调度器无需训练、完全因果且码率控制准确，即插即用特性工程价值高。实验覆盖因果/非因果两个codec家族、含主观MOS与两组关键消融，论证充分。不足：仅16kHz单语料、MOS样本量小（10人×10句），1.5kbps处对VRVQ优势收窄，超参依赖手工设定且未开源，属扎实的增量式贡献。

---

## [11] DRC-TTS: A Dual-Resolution Codec-Based Architecture for Lexicon-Free Malay Speech Synthesis

**arXiv ID**：2610.38316 | **方向**：语音大模型

**作者**：Tianhui Su, Tien-Ping Tan

**机构**：马来西亚理科大学计算机科学学院（Universiti Sains Malaysia）

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.38316 | **PDF**：https://arxiv.org/pdf/2610.38316.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对马来语TTS依赖发音词典、且时长预测在12.5 Hz低帧率离散codec下"亚40毫秒字符被量化为零帧"导致漏读的问题，提出DRC-TTS双分辨率FastSpeech 2架构：字符表示先在50 Hz做长度调节，再经stride-4卷积降采样到12.5 Hz并行预测Mimi codec离散token，推理全程无需发音词典。在12.4小时Idayu语料上，CER从基线27.11%降至21.86%，MOS从4.12提升至4.30，MCD由11.60 dB降至10.70 dB。

### 🔧 技术方案

**问题背景：** 马来语属低资源语言，现有系统多用G2P词典映射音素，词典错误在借词上会级联；同时duration-based非自回归TTS需将字符时长量化为codec帧数，12.5 Hz帧长80 ms，语料中20.23%字符物理时长<40 ms会被四舍五入为零帧，长度调节器直接丢弃其表示，造成发音遗漏。

**模型架构：** 基于FastSpeech 2框架，含字符嵌入层、Transformer序列编码器、分层variance adaptor（时长/音高/能量预测器+50 Hz长度调节器）、stride-4一维卷积降采样层与离散token解码器（FFTransformer）；解码器输出32个线性投影头，对应Mimi codec（12.5 Hz、32路量化器）逐层并行预测token，外部codec decoder还原波形。音高用YIN计算（限幅50–500 Hz、取对数），能量为帧级RMS，均按12.5 Hz边界切片平均对齐。

**核心创新：** (1) 双分辨率解耦设计：长度调节在50 Hz上进行并强制每字符至少占1帧（20 ms），杜绝零帧截断；再经stride-4卷积降至12.5 Hz，短字符信息借卷积局部感受野融入降采样序列，在不增加codec帧数、保持低码率传输效率的前提下保留表征。(2) 全字符级lexicon-free管线：利用马来语字母-发音高度规则性，经文本清洗与领域归一化（如RM 10.50→sepuluh ringgit lima puluh sen）后用MFA对字符直接强制对齐，去除发音字典且保证文本-语音长度确定映射。(3) 辅助连续梅尔谱损失：解码器隐状态同时投影梅尔谱作为内部正则化，稳定训练初期的梯度收敛。

**训练策略：** Idayu语料（Mesolitica Malaysian-TTS单女声，12,421条、约12.4小时、745,436字符、24 kHz）按90/5/5划分；联合优化时长、音高、能量、离散token及梅尔辅助五项损失；AdamW+Noam warmup，batch size 4，训练150,000步，单张RTX 4090。

### 📊 实验结果
**数据集**：Idayu马来语单说话人语料（约12.4小时，24 kHz，5%未见测试集）

**主要指标**：
- CER：21.86% vs 基线27.11%（绝对降5.25pp；真实录音下限16.32%）
- MOS：4.30±0.15 vs 基线4.12±0.09（20名马来语母语者5分制；真实录音4.65±0.08）
- MCD：10.70 dB vs 11.60 dB；F0 RMSE：40.32 Hz vs 41.59 Hz；V/UV错误：2.01% vs 2.06%
- 零帧分析：20.23%字符时长<40 ms，改造后每字符至少获1帧20 ms

**是否开源**：暂无（论文未提供代码/Demo链接）

### ⭐ 评分：6/10
评分理由：论文精准定位duration-based NAR TTS与低帧率离散codec结合时的零帧截断这一真实痛点，量化了20.23%亚阈值字符占比，双分辨率方案侵入性小且CER/MOS/MCD改进方向一致。但属增量工程工作：仅单说话人12.4小时小语料、只对比一个自建12.5 Hz基线、缺严格消融与显著性检验（MOS置信区间宽），方法通用性有待更大规模多说话人验证。

---

## [12] How Architecture, Typology, and Adaptation Strategies Shape ASR for Low-Resource African Languages: A Controlled Empirical Study

**arXiv ID**：2610.39004 | **方向**：语音大模型

**作者**：Mercy Muchai, Kevin Chege, Nick Mumero Mwangi, Samuel Chege Maina, Felermino Ali, Elizabeth Ankrah, Ignatius Ezeani

**机构**：Microsoft Research Africa（内罗毕）、Lancaster University

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.39004 | **PDF**：https://arxiv.org/pdf/2610.39004.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对低资源非洲语言ASR中架构与微调策略难以选择的问题，本文在匹配的每语言数据预算下，系统对比三种异构预训练模型：Phi-4-multimodal-instruct（LLM多模态）、Whisper-large-v3-turbo（编码器-解码器）、MMS-1B-all（编码器+语言适配器），覆盖luo/kln/kik/mas/som五个低资源语言及中资源swa，评估数据充分性、单/多语微调、领域适配与adapter迁移。Phi-4在4/6语言取得最优CER；MMS约150h即饱和；领域微调使Phi-4相对CER降低最高83%却令MMS域外退化；代理适配器比从零训练CER优6-20%。

### 🔧 技术方案

**问题背景：** 低资源ASR无法只靠堆标注数据解决，实践者需决定选型、数据预算、联合/独立微调、未支持语言初始化及领域数据分配；既有研究常随语言数增加总数据量，混淆多语收益，缺乏固定每语言小时数的受控对比。

**模型架构：** Phi-4：5.6B LLM骨干+920M语音侧参数（音频编码器+投影器460M、speech LoRA 460M），仅支持8语言；Whisper-large-v3-turbo：809M编码器-解码器，99语言，微调时扩展语言token并重设embedding；MMS-1B-all：1.0B Wav2Vec2.0编码器，1162语言adapter路由，骨干冻结仅调adapter。音频统一16kHz。

**核心创新：** (1) 以5-450h累计节点的匹配预算缩放曲线量化数据充分性，用配对t检验与bootstrap置信区间判定饱和，排除多语总数据混杂。(2) 对MMS未覆盖的Maasai、Kalenjin，按谱系邻近选Samburu(saq)、Sabaot(spy)代理adapter迁移微调，与从零训练adapter对照。(3) 领域三联评估：200h通用域零样本跨域、加38.3h农业数据in-domain、私有域外农业集测泛化，并以200→238h增益<1pp分离域匹配与数据量效应。

**训练策略：** AdamW与官方默认超参：Whisper batch256、LR1e-5、wd0.01；Phi-4 batch96、LR1e-4、wd0.005；MMS batch128、LR1e-3、wd0.01。Phi-4仅解冻音频embedding/编码器/投影层；多语微调跨语言交替batch。DDP：MMS/Whisper用8×A100 40GB，Phi-4用4×A100 80GB。

### 📊 实验结果
**数据集**：ANV-KE（luo 513.2h、kln 386.7h、mas 235.5h、kik 967.8h、som 341.9h，11域）、Common Voice swa 280h、农业kik 38.3h及私有域外集，16kHz。

**主要指标**：
- CER@200h：Phi-4六种语言中4种最优（kik 0.21、kln 0.26，Whisper对应0.71/0.70），MMS次之
- 数据饱和：MMS 150→450h仅Δ-0.7pp（p=0.036）；Phi-4平均Δ-4.4pp不显著（p=0.126），swa反升+5pp
- 单/多语：单语赢12个语言-模型对中的10个（Whisper som例外0.35→0.23）
- 领域适配：Phi-4域内CER相对降最高83%，Whisper域外降70%；MMS域内0.33→0.21但域外0.32→0.56
- 代理adapter：比从零训练CER优6-20%、WER优3-9%
- 训练成本：Phi-4显存71.2GB、单语200h仅6h；Whisper 29.1GB/26h；MMS 26.6GB/15h

**是否开源**：论文声明释出训练配置以支持复现；代码与Demo暂无，数据集HF链接已公开。

### ⭐ 评分：6/10
评分理由：受控实证设计规范，匹配数据预算、显著性检验与域外泛化评估使"150h适配模型饱和、优先领域数据、代理adapter"等结论可直接指导非洲语言ASR工程。但每架构仅一个代表模型，架构效应与预训练语料、tokenizer混杂；类型学仅为六语言相关性观察；无新方法提出，属增量而有参考价值的工作。

---

## [13] ODAQ-Collection: Expanding the Open Dataset of Audio Quality with a Focus on Spatial Distortions

**arXiv ID**：2610.37959 | **方向**：语音前端

**作者**：Chih-Wei Wu, Matteo Torcoli, Mhd Modar Halimeh, Pablo M. Delgado, Sascha Dick, Christoph Thompson, Phillip A. Williams, Emanuël A. P. Habets

**机构**：Netflix；Amplifon S.p.A.；Starkey Hearing Technologies；Fraunhofer IIS；Ball State University

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.37959 | **PDF**：https://arxiv.org/pdf/2610.37959.pdf | **代码**：https://github.com/Fraunhofer-IIS/ODAQ | **Demo**：https://fraunhofer-iis.github.io/ODAQ/

### 📌 简介
音频质量客观指标研发依赖含人工主观分的公开数据集，但此类数据制作成本高、受版权限制，且 ODAQ 此前扩展以音色失真为主，空间失真仅覆盖 MS/LR 基础立体声条件，各子集日益碎片化。本文新增 18 条音乐厅实录高音质语音/音乐立体声素材（96 kHz/24 bit 录制、48 kHz/24 bit 导出），经 ICC、ILD 双耳线索失真与对话增强（DE）三类方法生成 148 对信号，并由 23/12 名受训听测者在实验室完成 MUSHRA 测试。全库聚合为 ODAQ-Collection：688 对音频、17 类处理方法、18,984 条原始评分，DE 条件分数覆盖 poor 至 excellent 全量程。

### 🔧 技术方案

**问题背景：** 现有音频质量数据集多私有或一次性、规模有限，众包数据信噪比差；ODAQ 已有子集缺少可控的空间失真条件，且子集分散导致难以整体评测与聚合客观指标。

**模型架构：** 失真生成与主观测试管线：素材经主阵列（直达声/扩散场比标定）录音混为立体声；ICC/ILD 类改造 Binaural Cue Coding 参数编码 codec（48 kHz，21 ms 窗、10.7 ms 重叠），将逐帧逐 ERB 频带边信息篡改后解码，参考取 BCC 无失真重建；DE 类以 PSM 掩码估计前景，按 y_DE=ŝ+α·v̂（α=16 dB）重组，参考为干净混叠 y。

**核心创新：** (1) ICC 失真由 Culling 等心理测量模型驱动，按 perceptual distance d（|d|=1 即 1 JND）经 sigmoid k(f)、g(f)（中心 600–700 Hz）反解 ICC_gen，对低频敏感区精准加密，实现按感知刻度可控的纯串扰失真。(2) ILD 失真通过量化级数控制（±24 dB 分 100/7/5 级），Q4 步长 0.48 dB 低于 0.5 dB JND，配合 Q1 0 dB 坍缩模式隔离单一互线索退化，不引入音色失真。(3) qmsPSM 对中/边掩码分离量化并注入 [-Δ,Δ] 均匀噪声模拟次优掩码估计，叠加 DeepFilterNet、Bandit-v2 真实系统输出，合成与真实退化共同张满 MUSHRA 刻度。

**处理与测试策略：** 全部条件按 ITU-R BS.1770 响度归一至 −23 LUFS；MUSHRA 含 3.5 kHz 低通锚、mono 锚与参考（binaural 14 trial×7 条件、DE 8 trial×9 条件）；听测前使用与测试不重叠素材完成 6 轮训练；声学处理房间、DT770 Pro 封闭耳机、声学校准听力正常，测试软件为 Netflix-Skunkworks/listening-test-app。

### 📊 实验结果
**数据集**：18 条音乐厅（RT60≈2.5 s）录音双声道素材，148 对（不含锚点 104）处理/未处理信号，平均 11.8 s，48 kHz/24 bit；主观数据 18,984 条原始评分。

**主要指标**：
- 集合总量：688 对（488 不含锚）、17 处理类别、43 唯一素材
- DE 各质量级均值 BAQ：覆盖 poor 至 excellent 全量程（95% t 置信区间）
- ICC/ILD 均值 BAQ：多落 good 区间；逐条下 ICC poor—excellent、ILD fair—excellent
- 关键锚点：mono 锚（空间像完全丢失）仅 fair 档，与文献一致——空间失真对整体 BAQ 存在下限效应

**是否开源**：数据 Zenodo（doi.org/10.5281/zenodo.23425817）、代码 github.com/Fraunhofer-IIS/ODAQ、基准页全开源。

### ⭐ 评分：6/10
评分理由：数据集建设型工作，填补 ODAQ 在可控双耳空间失真上的空白，基于 JND 心理测量模型的 ICC/ILD 注入设计专业严谨，实验室 MUSHRA 加受训听测者保证标签质量，统一 Collection 与聚合脚本对社区实用价值高。局限是单一录音场地、DE 仅 12 人、人群同质，且未给出新客观指标评测数值，创新为增量性质但基础扎实。

---

## [14] Beyond Utterance-Level Speaker Similarity: Perception-Aligned Segmental Evaluation of Accent in Speech Generation

**arXiv ID**：2610.37912 | **方向**：语音前端

**作者**：Jinzuomu Zhong, Alice Ross, Catherine Lai, Korin Richmond

**机构**：Centre for Speech Technology Research, University of Edinburgh

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.37912 | **PDF**：https://arxiv.org/pdf/2610.37912.pdf | **代码**：https://github.com/jzmzhong/segmental_accent_evaluation | **Demo**：https://jzmzhong.github.io/Segmental-Accent-Evaluation/results.html

### 📌 简介
零样本TTS语音克隆普遍用话语级相似度SMOS评估口音保真，但该分数无法指出感知到的口音差异发生在语音的哪些片段。本文提出分段评估协议：让目标口音区域母语听者在话语级说话人/口音SMOS之外，以subword为单位标注感知到的口音差异位置；基于自采苏格兰/澳洲4说话人录音与内容匹配的参考-合成对，评测F5-TTS、MaskGCT及发音器官VC系统SPARC共200对音频。结果显示说话人与口音评分高度耦合（ρ=0.71），而分段标注可给出与SMOS不同的系统排名；7种客观距离与subword标注相关性最高仅ρ=0.22。

### 🔧 技术方案

**问题背景：** 话语级SMOS掩盖口音差异的局部位置；CodecMOS-Accent评分主要来自美国听者，对目标口音社区代表性存疑；先前XAB测试的字符级标注未被深入分析，成对比较随系统数增加成本高昂。

**模型架构：** 三阶段评估管线：录音（两段英语语音学常用文本）→合成（DeepFilterNet降噪后以同说话人另一录音作voice prompt，经MaskGCT/F5-TTS生成，SPARC作口音保持锚点）→评估（Pyphen切分亚词并人工复核，听者分别打说话人/口音SMOS并标注3–7个口音线索subword）。客观侧计算7种距离：ECAPA-TDNN与WavLM-SV说话人嵌入、GenAID与Voxlect口音嵌入余弦距离，及PPG（JS散度）、F1–F3共振峰、F0经DTW对齐的距离；帧级距离取自池化前表征，经MFA与G2P两级口音无关对齐映射到subword，用Mean/Max/Midpoint聚合。

**核心创新：** (1) subword级口音线索标注协议：以近似音节的粗粒度单元替代字符级标注，无需语音学训练背景，将标注稀疏度约束在3–7段，将局部标注作为一等评估输出。(2) 内容匹配参考-候选对加目标区域母语听者：合成语音与文本同源真实录音配对，支持对应片段直接比较，SPARC锚定口音/说话人相似度上下限。(3) 帧级客观距离到subword的映射与相关分析框架：对齐前池化表征保留时间序列，比较三种聚合，量化现有表征与局部感知的差距。

**训练策略：** 无模型训练；测试约40分钟，每听者评50对（F5-TTS/MaskGCT各20、SPARC10），60人按标注段数<2或>8、两类评分>80%完全相同两准则剔除留47人，得4,700条SMOS与约48,600条二元标注，对200对与4,140个subword算SRCC。

### 📊 实验结果
**数据集**：自采苏格兰/澳洲各一男一女4个声音，47名同区域听者，200条内容匹配对、1,035个subword（分析4,140实例）

**主要指标**：
- S-ACC-SMOS与S-SPK-SMOS相关ρ=0.71，仅SPARC的40对子集内仍ρ=0.57
- S-ACC-Freq与口音SMOS相关ρ=0.48，与说话人SMOS仅0.27
- 话语级最优客观关联：Voxlect距离与S-ACC-Freq ρ=0.46
- subword级：所有指标聚合最高ρ=0.22（WavLM-SV与Voxlect，Max聚合）
- 一致性：Fleiss κ=0.184–0.234，Krippendorff α=0.187–0.240
- 排名分歧：澳洲女声SPARC口音SMOS最低（2.77）但标注率亦最低（15.92%），两套指标排序不一

**是否开源**：代码、数据、交互demo全部开源（GitHub与HuggingFace见上）

### ⭐ 评分：6/10
评分理由：将分段标注提升为评估一等公民并开放全套资源，对口音幻觉与自身声音克隆评测有实用价值，协议细节（锚点系统、剔除准则、三级对齐）扎实可复用。但属于方法与资源型增量工作，无新模型；仅4说话人200对样本、标注一致性中等，客观相关性结论受录音条件与增强影响未能隔离，核心结论偏负结果且规模有限。

---

## [15] Toward Complete Speaker Anonymization: a Streaming Cascaded System for Voice Privacy and PII Removal

**arXiv ID**：2610.39754 | **方向**：语音前端

**作者**：Stanisław Kacprzak, Thomas Thebaud, Najim Dehak

**机构**：Johns Hopkins University CLSP、AGH University of Krakow、AMIAD

**发布日期**：2026-10-30 | **论文**：https://arxiv.org/abs/2610.39754 | **PDF**：https://arxiv.org/pdf/2610.39754.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文针对现有语音匿名化系统多为离线、且未覆盖个人身份信息（PII）的缺口，提出ASR+NLP+TTS级联的近似流式语音隐私系统：Whisper turbo结合SileroVAD以自研分块逻辑做流式识别，微调NER/LLM检测剔除PII，VoxCPM 2.0以固定参考音色续克隆重建语音。在RTX PRO 6000上语句起始端到端延迟中位数717 ms，LibriSpeech WER 11.44%，对半知情攻击者EER最高47.66%，PII检测SLU F1达69%，效果可比SOTA离线级联系统，将语音隐私保护推进到流式场景。

### 🔧 技术方案

**问题背景：** VC类匿名化保效用、可流式但隐私弱；ASR+TTS级联隐私强但效用受损且几乎全为离线；已有PII遮蔽工作仅用beep音遮盖音频，说话人身份匿名与内容级PII移除的结合鲜有探索。

**模型架构：** 三级级联。ASR用Whisper turbo+SileroVAD：700 ms音频块起步，检出语音起始块后识别，若句尾残留静音不足100 ms则逐块扩展（上限1.3 s识别窗），可能被窗口截断的尾部词结转至下一块。NLP层比较Qwen2.5-1.5B/0.5B-Instruct、GLiNER Small v2.5、NVIDIA GLiNER-PII与spaCy en_core_web_trf，检测六类实体并移除。TTS用VoxCPM 2.0（Nano-vLLM-VoxCPM引擎）对ElevenLabs合成的固定参考音做续克隆，cfg=2.0、10推理步、温度0.9、单次生成上限10步（约1.6 s）。

**核心创新：** (1) 首次将说话人匿名化与PII移除合并进同一准流式级联系统，实现语音之外的内容可控保护，为全匿名流式系统确立基线。(2) 将非流式Whisper工程化为近实时ASR的分块算法：VAD判定识别块边界、1.3 s窗口封顶、截断词结转，兼顾短语级识别质量与延迟。(3) TTS流式续克隆稳态策略：以激进生成步数上限防幻觉与长静音，并在静音、连续两短语或累计10 s音频后重启续克隆模式，抑制误差累积。

**训练策略：** 各PII检测器均在SLURP训练集11514条转录上微调（10%作验证），按2-4词分块并带左侧上下文模拟流式，训练10 epoch、选验证F1最优epoch，Qwen模型用LoRA；评估时合并相邻同类实体，指标为micro Entity F1与SLU F1。延迟实验取LibriSpeech train-100的100条音频、WhisperX强制对齐，在RTX PRO 6000上测量。

### 📊 实验结果
**数据集**：LibriSpeech dev/test（效用）、IEMOCAP（情绪UAR）、SLURP（11514训练/headset质控后6281测试）、DialogPII英文2913条。

**主要指标**：
- 端到端延迟：ASR+TTS管道中位数711 ms（ASR 669 ms、TTFA 41 ms），计入NER后约717 ms；输出/输入时长比1.33
- 效用：匿名化后WER dev/test 11.11/11.44（原始1.80/1.84；离线级联T30仅4.78）；情绪UAR 29.37/29.22（原始69.08/71.06）；UTMOS 3.21±0.44
- 隐私：ECAPA-TDNN+WavLM半知情攻击者下EER 44.18~47.66%，高于B5基线（32.92~35.82），与离线级联T30/T8-4同档
- PII检测：流式模拟中GLiNER Small v2.5 Entity F1 61.22@6 ms、NVIDIA GLiNER 60.40@17 ms，超过Qwen 1.5B（56.27@46 ms）；spaCy SLU F1 69.01
- 消融：流式ASR自身WER 7.83%，金标文本经TTS合成WER 10.38%，分块识别为首要瓶颈

**是否开源**：系统代码暂无；仅引用第三方权重。

### ⭐ 评分：6/10
评分理由：把说话人匿名与PII移除统一到准流式级联、并给出延迟/效用/隐私三维完整测量，是实用的系统贡献；"轻量NER在流式场景优于小LLM"的实测结论有部署价值。但效用明显劣于离线级联（WER 11.44 vs 4.78），ASR错误使PII检测F1大幅下降，NLP延迟未纳入端到端演示，且未开源，属奠基性增量工作。

---

## 📄 更多语音论文（紧凑列表）

> 以下 8 篇为当日语音相关论文，未进入精读队列，仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），按预估评分从高到低排列。

**Universal Short-Time Fourier Transform: Data-Adaptive Window-Length Selection for Time-Frequency Analysis**
- **arXiv ID**：2610.37795 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.37795（未精读，按摘要评分）

**Improving the Dependency on Fine-Tuning Data in Transfer Learning for Speech Emotion Recognition**
- **arXiv ID**：2610.38050 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.38050（未精读，按摘要评分）

**MixCards: Evaluating Structured Descriptions of Multi-Source Sound Scenes**
- **arXiv ID**：2610.38276 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.38276（未精读，按摘要评分）

**SelectSep: Target-Selective Video Queries for Audio Source Separation**
- **arXiv ID**：2610.38624 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.38624（未精读，按摘要评分）

**Wav2Aug: A Drop-In Speech Augmentation Policy**
- **arXiv ID**：2610.38656 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.38656（未精读，按摘要评分）

**Efficient Agentic Audio-Visual Question Answering through Toolset Pruning and Modality Consolidation**
- **arXiv ID**：2610.38960 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.38960（未精读，按摘要评分）

**Reading-Level Verification of Kanji Words in Japanese Financial Speech Synthesis**
- **arXiv ID**：2610.39168 | **方向**：语音大模型 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.39168（未精读，按摘要评分）

**Bridging Neural Representations and Symbolic Semantics in Audio Classification**
- **arXiv ID**：2610.40414 | **方向**：语音大模型 | **评分**：5/10 | **链接**：https://arxiv.org/abs/2610.40414（未精读，按摘要评分）

*Subagents used for reading: 15* | Generated on 2026-10-30 语音论文批次, by Kimmy's research agent | Powered by VAgent SpeechAI Researcher
