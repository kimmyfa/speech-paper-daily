# 2026-11-24 语音论文速递

**共收录**: 21 篇 | **语音大模型**: 20 篇 | **语音前端**: 1 篇

> 目标日期 2026-11-24（北京时间）arXiv 语音相关论文共命中 21 篇。
> 按规则超过 15 篇，以下详载评分最高的 15 篇，其余 6 篇仅列标题、ID、评分与链接。

---

## 语音大模型

## [1] BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language Models

**arXiv ID**：arXiv:2611.30723 | **方向**：语音大模型

**作者**：Yixian Lu, Lijun Wang, Shogo Okada

**机构**：日本北陆先端科学技术大学院大学（JAIST）

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.30723 | **PDF**：https://arxiv.org/pdf/2611.30723.pdf | **代码**：暂无 | **Demo**：https://seekmind-lab.github.io/bisat-demo

### 📌 简介
面向语音大模型的低比特率单流tokenizer需同时保留声学与语义信息，现有统一方案在单一特征空间内容易互相干扰，且依赖冻结语义教师的固定对齐目标。本文提出BiSAT：声学支（mel重建）与语义支（CTC）各配独立编码器、码本与解码器，通过共享索引量化按两支联合距离选码，实现无须教师的双向对齐，输出25Hz、375bps单码流。基于其构建BiSAT-TTS（0.5B自回归LM+条件流匹配解码器），仅用12.2万小时数据即在Seed-TTS test-en达WER 1.21%、失败率0.016%，全面优于100万小时训练的CosyVoice 3（1.55%、0.063%）。

### 🔧 技术方案

**问题背景：** 语义增强tokenizer丢弃声学细节、声学导向tokenizer保留过多不利于语言建模的变异；统一tokenizer要么融合表征导致目标干扰，要么以冻结SSL编码器为教师使语义目标静态化；对抗波形重建还会解耦重建质量与码内结构。

**模型架构：** 双编码器各为17层Conformer（512维、8头），由NeMo英文SSL模型初始化；共享索引向量量化器（SVQ）用两个K×512配对码本（K=32768/65536），每帧按加权联合欧氏距离选一个共享索引；训练期声学解码器为9层ConvNeXt V2上采样至100Hz回归mel，语义解码器为9层Conformer+CTC头。TTS端以MiniCPM4-0.5B初始化的AR LM预测码流，22层DiT流匹配解码器以25Hz码上采样到50Hz，条件含prompt mel与CAM++说话人嵌入，接CosyVoice 3预训练因果HiFT声码器。

**核心创新：** (1) 共享索引量化：单一离散码流由两支联合距离决定，声学与语义在分离连续空间学习并以离散瓶颈耦合，配合球面k-means初始化、EMA与死码替换实现100%/99.8%码本利用率。(2) 双向对齐：共享索引同时依赖两编码器，任一支的梯度更新都会改变另一支的量化分配，无须固定语义教师即可联合优化；诊断显示过度失真与方向信息不平衡随训练收敛。(3) tokenization与波形重建解耦：tokenizer仅受mel回归+CTC塑造、去除对抗训练，波形交由prompt条件化流匹配解码器，验证"可及的码结构而非重建质量"才是AR建模收益来源。

**训练策略：** 数据122k小时11语言（Emilia、LibriTTS-R、AISHELL-3等）。Tokenizer两阶段：分肢无VQ各100k步，插入SVQ后联合200k步；损失权重λa=1、λs=0.7、λint=0.3、β=0.5，AdamW、lr 10⁻⁴/7.5×10⁻⁵、BF16。LM全参微调400k步（峰值10⁻⁴余弦衰减），top-k=25、温度0.8-0.9；流匹配解码器1M步、Euler J=10、CFG 0.7，支持chunk-causal流式。

### 📊 实验结果
**数据集**：LibriSpeech-PC test-clean、Common Voice 27（重建）；Seed-TTS test-en/test-zh（零样本TTS）；SUPERB风格冻结码探针

**主要指标**：
- 重建（BiSAT-32k，375bps）：LibriSpeech-PC WER 2.15%、SIM 0.976，优于CosyVoice 3（2.26%/0.969）与X-Codec2（2.27%，800bps）
- 冻结码理解：EN ASR WER 37.71%（CosyVoice 3为74.17%）、SID 40.4%、ASV EER 1.92%、LID 95.5%
- 零样本TTS：Seed-TTS test-en最低WER 1.21%、test-zh CER 1.27%、失败率0.016%-0.031%（基线0.039%-0.756%）、SIM-o 0.950接近CosyVoice 3（0.951）

**是否开源**：仅音频Demo页，代码暂无

### ⭐ 评分：8/10
评分理由：将图像领域TokenFlow的共享索引思想首次系统化引入语音统一tokenization，双向对齐机制有真实方法论增量，并用过度失真、方向信息不平衡等三类诊断支撑机理分析，罕见地扎实。122k小时以约1/8数据在零样本TTS错误率与失败率上全面反超CosyVoice 3。不足在缺全组件消融、编码器基于英文SSL初始化限制多语上界且未开源代码。

## [2] Tenlai-TTS 2.0: Continuous-Representation LLM-Based TTS System with End-to-End Training

**arXiv ID**：arXiv:2611.29226 | **方向**：语音大模型

**作者**：Changfeng Gao, Yong Ren, Jun Yuan, Zhengkun Tian, Ye Bai, Zhao You, Shidong Shang

**机构**：腾讯元宝（Tencent Yuanbao）、Tencent Ethereal Audio Lab

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.29226 | **PDF**：https://arxiv.org/pdf/2611.29226.pdf | **代码**：暂无 | **Demo**：https://tenlai-tts.github.io/Tenlai-TTS-2.0/

### 📌 简介
连续表征可规避离散词元TTS的量化信息损失，但现有方法先单独学习隐空间再在LLM训练前冻结，难以兼顾高保真重建与自回归可预测性。腾讯元宝提出Tenlai-TTS 2.0：能量归一化加固定方差噪声的容量控制高斯瓶颈，将编码器、LLM+AR-DiT头、流匹配解码器与多任务识别模型端到端联合训练，并以可微重建/识别反馈优化隐变量预测，再经DiffusionNFT强化学习。最终模型在Seed-TTS-eval达test-zh CER 0.77%、test-en WER 1.08%，为对比系统最低英文WER与最高中文相似度。

### 🔧 技术方案

**问题背景：** 主流配方先用VAE学表征并在LLM训练前冻结，LLM无法影响表征的语义-声学平衡，回归/扩散损失不区分解码后改变字词或说话人与几乎无感的预测误差，且误差在长序列生成中累积。

**模型架构：** 语音编码器把24kHz音频映射为25Hz、D=384连续隐变量，经μ=z/RMS能量归一化叠加固定σ高斯噪声成瓶颈；LLM由Qwen3-1.7B-Base初始化，每3帧隐变量合并为一个输入嵌入（约8.3Hz运行），小型AR-DiT头以条件流匹配生成下一隐补丁并配EOS头；CosyVoice3风格FM解码器（ODE+CFG+说话人嵌入）生成mel，HiFT声码器合成；多头RM基于Conformer共享主干，CTC ASR与CAM++说话人两头预训练、SFT扩展情感/性别/语速等。总损失L_CE+L_DiT+L_FM(z)+L_RM(z)+λ[L_FM(ẑ)+L_RM(ẑ)]。

**核心创新：** (1) 容量可控连续瓶颈：隐维度化为单位功率加性高斯信道，信息率上限闭式C=(D/2)·log2(1+1/σ²)——σ=0.5即11.1kbps，约Qwen3-TTS RVQ（2.2kbps）5倍、CosyVoice3单码簿（0.2-0.38kbps）的30-56倍，信息预算由单一超参设定。(2) 端到端表征学习：编码器同时接收生成、重建、识别三路梯度，表征在容量内由三任务共同塑形，从机制缓解连续AR生成误差累积。(3) 反馈式优化与RL：由FM恒等式ẑ=x_t+(1−t)v̂得可微一步预测，在其上评估L_FM(ẑ)+L_RM(ẑ)把"解码后可听代价"回传生成器（连续表征免除STE），再以DiffusionNFT无似然优化做句级奖励强化。

**训练策略：** 两阶段E2E：阶段1联合训练编码器/RM/FM/LLM+AR-DiT；阶段2冻结RM加入反馈损失；目标说话人SFT先适配FM/RM再微调LLM/AR-DiT；RL在阶段2 checkpoint做1000步DiffusionNFT。数据160万小时中英文（含六类方言）+5万小时困难样本，统一24kHz。

### 📊 实验结果
**数据集**：Seed-TTS-eval（zh/en/hard；Paraformer/Whisper-large-v3评CER/WER，整句余弦SIM）；CV3-Eval 198句测声学细节跟随

**主要指标**：
- test-zh：CER 0.77%、SIM 0.811；test-en：WER 1.08%、SIM 0.766（18系统最低WER、最高中文SIM）；test-hard CER 6.29%
- 反馈阶段消融：zh CER 0.82%→0.74%、en WER 1.32%→1.27%、hard 8.32%→7.08%；RL再降en WER 15.0%、hard CER 11.2%
- 容量消融：σ=0.2（22.6kbps）重建/识别更好但合成变差（zh CER 0.92%），验证容量须兼顾可预测性
- 细粒度跟随：zh语速r=0.760、en音量r=0.927、CV3音高/音量r=0.961/0.948居首

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：把离散token端到端方案系统迁移到连续表征，"可计算容量上限+经FM/RM的可微反馈+DiffusionNFT"构成对预测-重建矛盾最成体系的机制性解法，容量扫描与逐阶段消融论证扎实，结果在Seed-TTS-eval多指标同级最优，实用价值高。不足是未公开部分优化细节、代码不开源，方法偏范式延续非突破。

## [3] SpeechSplice: Pronunciation Control in Encoder-Decoder LLM-based TTS by Replacing Encoder Hidden States

**arXiv ID**：arXiv:2611.30927 | **方向**：语音大模型

**作者**：Kiyoshi Kurihara, Jumpei Ukita, Yusuke Iwasawa, Yutaka Matsuo

**机构**：Matsuo Institute, Inc.、东京大学

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.30927 | **PDF**：https://arxiv.org/pdf/2611.30927.pdf | **代码**：https://github.com/Kuri-san-jp/speechsplice | **Demo**：https://kuri-san-jp.github.io/speechsplice/

### 📌 简介
LLM-TTS把文本前端并入端到端序列模型，失去了G2P词典逐条修正发音的接口，常读错专有名词、同形异音词与数字。本文提出免训练的SpeechSplice：用同一冻结编码器分别编码原句与目标读音句，把实体token段的编码器隐状态直接拼回原序列，零权重改动即可推理时局部纠音。在10个系统、17个模型-语言条件上母语听者判定目标读音达98.6%-100.0%，MOS与原始合成无显著差异；并发现仅当解码器经交叉注意力读取被替换张量时干预才有效。

### 🔧 技术方案

**问题背景：** VALL-E、CosyVoice2等单序列LLM-TTS取消了可编辑的G2P接口；已有补救（参考音频纠音、语音编辑、LoRA微调、权重编辑）或需目标词录音与优化，或离线进行且被报告引发音质退化乃至语音崩塌。

**模型架构：** 主系统T5Gemma-TTS-2b-2b（5.31B，XCodec2作tokenizer与声码器）。对含实体e的句子x及目标读音改写句x'，用同一冻结文本编码器得H_src、H_tgt；按字符偏移定位实体token跨度，在解码器交叉注意力读取的最终编码器输出处拼接H~=(h^src前缀,h^tgt实体块,h^src后缀)，并重建注意力掩码与位置索引。

**核心创新：** (1) 首个在编码器-解码器LLM-TTS文本编码器输出上做G2P-free词发音注入的方法，全部权重冻结、零训练，与微调/权重编辑的离线范式形成对比。(2) 跨架构系统对比给出适用边界：要求生成器在被替换张量处通过交叉注意力读取文本，17个条件下两组架构的干预有效率区间完全不重叠；另一前提是分词器给源/目标词形不同token ID。(3) 交叉注意力掩码消去实验定位传输路径：屏蔽实体列后三语言指标归零，证明实体状态沿该路径传入语音。

**训练策略：** 完全不训练，10个系统均用公开冻结checkpoint，纯推理时干预；BL与INJ同文本、同音源提示、同种子；T5Gemma时长估计固定取原句长度使两版等长。

### 📊 实验结果
**数据集**：英日中各300对实体替换句基准、双实体句集、160项日语语境读音基准；音源LibriTTS test-clean、JSUT、Databaker

**主要指标**：
- 听者选择注入版达目标读音：EN 99.4%、JA 98.6%、ZH 100.0%；日语基准45处基线误读全部纠正
- MOS：三语言均与基线无显著差异（p=0.45/0.74/0.96）
- 关键对比：英语96.33% vs VoiceCraft 90.00%（+6.33）、EdiTTS 86.00%（+10.33）；decoder-only架构有效率仅2.67%-27.00% vs 编码器-解码器41.67%-65.33%

**是否开源**：代码、基准与听测材料已开源 @ https://github.com/Kuri-san-jp/speechsplice

### ⭐ 评分：8/10
评分理由：方法极简但把激活干预从语言模型迁移到TTS发音控制的思路清晰，最大贡献是给出"交叉注意力决定干预是否可达输出"这一带因果消融证据的机制性结论；三种母语听者成对比较、MOS、消去实验与四套自动指标构成严紧验证。局限是decoder-only上需经验性选择替换深度、未评音高重音与长文本。

## [4] Granary-v2: Scalable Multilingual Speech Data Curation for Predictable and Controllable Model Outputs

**arXiv ID**：arXiv:2611.28248 | **方向**：语音大模型

**作者**：Nithin Rao Koluguri, Meline Mkrtchyan, Nune Tadevosyan, Aaftab V 等（NVIDIA，前三位同等贡献）

**机构**：NVIDIA

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.28248 | **PDF**：https://arxiv.org/pdf/2611.28248.pdf | **代码**：https://github.com/NVIDIA-NeMo/Curator | **Demo**：https://huggingface.co/datasets/nvidia/Granary-v2

### 📌 简介
面向指令可控的语音-语言模型，现有语料每条录音通常只有一份转录，模型无法从单条音频学会输出多种有效形态。Granary-v2基于NeMo Curator构建元数据、ASR标注、文本生成三条可复用管线，以"忠实口语转录"为公共源派生对齐的多目标，语言从25种扩到48种，处理约84.36万小时音频，译入英语约14.28万小时。质量过滤实验显示同预算下英语Transformer-TDT九基准平均WER从4.91%降至4.67%。

### 🔧 技术方案

**问题背景：** 听写、语言学分析、语码转换、翻译等场景对同一录音输出约定不同，单一转录无法教会模型"按指令选择输出形态"，需要把音频与多个对齐目标及指令关联的可复现数据基础。

**模型架构：** 三管线串联可独立选择。元数据管线：Nemotron-3-Diarization说话人分离+Silero VAD（0.5–40s切分）+PANNs声学事件+VoxLingua107语言识别。ASR管线按语言路由7组主/备模型（Qwen3-Omni/Parakeet v3/Whisper等）做伪标注或人工标签改进。文本管线以Gemma/Qwen级LLM生成实体恢复、标点、TN/ITN、去赘语、字幕、SpeechQA与翻译，末段确定性打包指令-目标对。

**核心创新：** (1) 以单一"忠实口语转录"为公共源派生对齐的多种目标形态，同一段音频连到多个指令-标签对，天然支持提示可控多任务训练。(2) 语言相关ASR主/备路由加幻觉/一致性质量规则与可恢复处理清单，使84万小时级批处理可断点续跑。(3) 质量过滤与可扩展性系统评估：给出各阶段实测吞吐，并用同预算双臂训练量化"少而精"标签收益。

**训练策略：** 验证实验用Transformer-TDT（编码器630.9M，32层、隐维1280、10×RoPE、8×下采样），16kHz/128维log-mel，BF16、AdamW、峰值lr 5e-4、余弦15000步预热、300k步；英语高质量子集162845.95小时（占46.91%）vs全量347178.9小时。

### 📊 实验结果
**数据集**：843579小时48语言唯一ASR音频、约2.134亿条语句；公开子集463062小时（HuggingFace发布清单）

**主要指标**：
- 平均WER：高质量标签4.67% vs 全量4.91%；AMI-Cleaned 7.84% vs 8.72%
- 吞吐：元数据23音频小时/GPU小时、ASR标注281、质量过滤10400小时/CPU节点小时
- 下游：Nemotron 3.5 Transcribe 7语4.62% WER、FLEURS 37语9.29%均值、英译外26.54 BLEU

**是否开源**：管线与训练配方开源（NeMo Curator/NeMo Speech），标签与指令子集发于HuggingFace nvidia/Granary-v2（音频需自备）

### ⭐ 评分：8/10
评分理由：数据基础设施类工作，48语言、84万小时与多目标对齐打包的体系化程度和工程可复现性非常扎实，同预算双臂训练给出可量化的标签过滤收益且被Nemotron 3.5下游使用。局限是指令家族未逐一消融、质量实验仅单一英语架构，提升幅度偏小（0.24点），最大数据源不公开，受许可制约。

## [5] Voice Agents: From Auditory Intelligence to Auditory Agency

**arXiv ID**：arXiv:2611.29465 | **方向**：语音大模型

**作者**：Kele Xu, Qisheng Xu, Xinwang Liu, Huaimin Wang

**机构**：国防科技大学

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.29465 | **PDF**：https://arxiv.org/pdf/2611.29465.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
语音智能体正把流式语音、持久记忆、推理与工具执行整合进同一运行时，语音因此具备改变数字或物理状态的后果性，组件指标已无法刻画系统实际行为。本综述提出听觉智能与听觉Agency两个概念及统一框架：承诺边界刻画可修正语音证据转化为持久状态或可执行请求的位置，能动性闭环沿观察、验证、恢复补偿与结果沟通追踪授权动作。对744篇文献的梳理给出一致结论：整合进展快于端到端观测，代表性具身基准现实条件下pass@1仅26%至38%。

### 🔧 技术方案

**问题背景：** 现有评估以单能力口径进行，而增量语义理解会在话轮未完成时提前触发推理与工具准备，造成过早承诺、越权执行与虚假成功报告；社区缺少区分"听得准"与"做对了"、并把评测证据对齐到agency声明的系统级框架。

**模型架构：** 综述以语音证据到后果的路径为主线，以承诺边界与能动性闭环为锚点，提出横跨模态处理、交互管理、推理控制、应用与后果的四层功能架构；按级联、语音-语言模型、原生长双工、分层、工具增强、具身六类范式比较状态与决策权归属，梳理并行codec流（Moshi）与语音-动作共享160ms时钟的DuplexSLA等机制。

**核心创新：** (1) 承诺边界：将声学/语义端点检测与承诺决策分离，投机推理的中间状态必须保持可撤回，使过早动作可识别、可追溯。(2) 能动性闭环：把执行→观察→验证→恢复补偿→沟通分解为可区分环节，指出模型自身的成功播报不是独立观察。(3) 六类证据端点评测框架（信号、语义、交互、任务、后果、人的结局），要求结论不超出实际观测端点，并把四个未解决接口问题转化为带指标的实验议程。

**训练策略：** 综述无训练；744篇引文按接口归类，引用数值保留原始实验口径，禁止跨表统一排名，冻结截止后的工作单独讨论。

### 📊 实验结果
**数据集**：无训练集；综述覆盖Full-Duplex-Bench v2/v3、IHBench、3万条噪声语音请求speech-to-function集、278项grounded服务任务、AgentDojo、LongMemEval等

**主要指标**：
- DuplexSLA：900确定性工具案例85.56%@0.648s（级联91.33%@2.77s）
- Full-Duplex-Bench v3：最优实时模型工具选择pass@1仅0.600、抢话率96%、任务延时6.89s
- grounded服务基准：音频原生系统clean条件pass@1 31%–51%，realistic条件26%–38%
- 关键结论：各证据线一致显示整合进展快于端到端观测，后果性验证是普遍缺口

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：作为综述有真正的概念原创性，承诺边界与能动性闭环给语音智能体提供了区分能力与因果效用的统一语言，端点纪律批评切中评测口径泛滥的要害，覆盖至2026年最新工作且四个开放问题均转化为可执行实验。不足是无原创实验复测、商用证据仅赖厂商文档、拒绝跨系统汇总削弱实用基准价值。

## [6] Synthetic Twins: Closing the Gap Between TTS Test Sets and Real Recordings in Turkish ASR Evaluation

**arXiv ID**：arXiv:2611.30694 | **方向**：语音大模型

**作者**：Nur Yağmur Tuncer, Mustafa Sertaç Türkel, Fatma Nur Korkmaz, Ahmet Tuğrul Bayrak

**机构**：Ata Technology Platforms（伊斯坦布尔）

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.30694 | **PDF**：https://arxiv.org/pdf/2611.30694.pdf | **代码**：https://huggingface.co/datasets/yagmurtuncer/turkasr-bench-twins | **Demo**：暂无

### 📌 简介
现成TTS引擎合成的ASR测试集信息价值很低，但既有研究只证明差距存在、未分解来源。本文为507条土耳其语Common Voice录音构建"合成孪生"阶梯R0-R4，逐级叠加说话人音高、克隆、真实录音通道与语速四个因子，并用预测驱动推断把保真度折算为等效真实录音条数。跨三引擎与6/19识别器面板，说话人克隆显著提升句级难度一致性（Spearman ρ .41→.55），最佳孪生体价值相当于70至122条真实录音（现成音色仅约9条），结论在VoxForge复现。

### 🔧 技术方案

**问题背景：** 已有工作确认合成语音与真实语音存在评测鸿沟——合成品触发21%至34%不存在的失败，但既没有分解缺口成因，也没有回答"合成测试集到底抵多少条真实录音"这一实操问题。

**模型架构：** 评测协议而非训练模型。孪生阶梯R0内置音色→R1音高匹配音色→R2同说话人另一录音零样本克隆→R3叠加真实通道（1/3倍频程谱均衡+背景噪声+响度匹配+64kbps MP3往返）→R4按真实语速重合成；识别端19个开源ASR（Whisper全尺寸、wav2vec2/XLS-R、MMS、Qwen3-ASR、SeamlessM4T），主分析6面板。

**核心创新：** (1) "价值"单一量化标尺：定义合成集S等效于n条随机真实录音的WER估计误差期望，把排序、绝对误差、句级难度、校准四个层面保真度统一到可比数字。(2) 因子分解：通道与语速只修正误差水平偏差，说话人克隆才改善句级排序一致性，二者不可加——克隆已继承参考句通道特征，再叠通道反而使合成语音比真人更难。(3) 双语料双面板稳健性设计：VoxForge复现（ρ .31→.50、价值8→52），种子间孪生ρ=.69证明残差缺口74%–80%已触及零样本TTS自身变异上限。

**训练策略：** 无模型训练。四级通过阈值预登记：排序τ≥.80、|Δ|≤2点系统占比≥80%、句级ρ≥.60且假报警≤20%、校准MAE≤3点；2000次句子级配对重采样CI、Holm-Bonferroni校正。

### 📊 实验结果
**数据集**：Common Voice 17土耳其语（507句实验集）；VoxForge土耳其朗读（507句、165 session）

**主要指标**：
- 句级难度一致性ρ：Chatterbox .41→.55、VoxCPM2 .50→.62（克隆vs现成音色）
- 合成集价值：最佳孪生122条（6识别器）/70条（19识别器）vs现成音色9-10条；真实录音上限251/309条
- 误差水平：通道使|Δ|从5.8点缩小到1.9点
- MUSAN+RIR通用加噪可把价值从4升到31-39，但句级一致性反降

**是否开源**：合成测试集与孪生音频已在HuggingFace公开

### ⭐ 评分：8/10
评分理由：把"TTS能否替代真实测试集"从二元判断推进为可量化的信息价值工程问题，value指标与阶梯分解设计干净，阈值预登记、多重校正与可靠性上限分析使统计结论可信，末尾实操配方可被工业评测直接采纳。扣分在范围受限：仅朗读式土耳其语、无端到端优化方案、19识别器面板CI仍宽、语速因子受XTTS速度控制伪影混淆。

## [7] S2SCORE: A Textless Unified Evaluation Metric for Speech-to-Speech Translation Systems

**arXiv ID**：arXiv:2611.29557 | **方向**：语音大模型

**作者**：Lalaram Arya, Mrinmoy Bhattacharjee, S. R. Mahadeva Prasanna

**机构**：IIT Dharwad、IIT Jammu

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.29557 | **PDF**：https://arxiv.org/pdf/2611.29557.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
S2ST评测长期依赖ASR转写文本指标，只覆盖语义充分度，说话人相似度与自然度需另用工具拼成分裂流水线。本文提出无文本统一评测框架S2SCORE：SONAR、WavLM-SV与log-Mel三路特征经共享MLP送入三个任务头，以xCOMET-XXL、UTMOSv2等教师分数弱监督，再用人工总评校准聚合权重合成单一总分。在5个X-en语对上，无参考变体语义分与人工一致性ρ=0.631超BLASER 2.0-QE的0.606；总分ρ=0.714。

### 🔧 技术方案

**问题背景：** 端到端S2ST去掉中间文本，BLEU/COMET类指标须先ASR转写，引入转录误差且丢弃声学信息；已有语音域指标仍只针对语义单一维度，无法给出整体质量分。

**模型架构：** 三分支：多语SONAR嵌入按BLASER 2.0方式构造交互特征（语义）；log-Mel谱展平16384维（自然度）；WavLM-SV嵌入（说话人）。三路投影到4096维，经硬参数共享S-MLP（FC 2048→1024）路由到各头：语义/自然度回归头各对教师MSE，说话人头128维余弦相似度以1正5负InfoNCE（τ=0.07）训练；总分为归一化三分量加权和。

**核心创新：** (1) 首个无文本条件下同时建模语义、说话人相似度、自然度并输出人工校准总分的统一S2ST评测框架。(2) 蒸馏式弱监督：标签全由成熟指标自动生成，仅聚合权重与测试用少量人工评分（2500条、5标注员、Krippendorff α=0.79），绕开大规模人工标注。(3) 硬参数共享多任务使三维度互益（消融平均ρ 0.775→0.791），QE变体稳定优于REF，说明源语音+译文已携带绝大部分质量信息。

**训练策略：** SONAR与WavLM-SV冻结；AdamW、lr 5e-4、batch 64、250 epochs；损失权重λT=1.0/λN=0.5/λS=0.1。数据CVSS（fr/de/es/zh–en）+BhasaAnuvaad（hi–en）约47.8k句57.1小时，译文由Whisper large-v3+XTTS v2、SeamlessM4T v2、DS2ST-LM生成，每句配6个目标音色构造匹配/不匹配对。

### 📊 实验结果
**数据集**：CVSS+BhasaAnuvaad构造的5语对S2ST数据（ASR-BLEU 15.16–26.57）

**主要指标**：
- 语义 vs 人工：S2SCORE-T-QE ρ=0.631 vs BLASER 2.0-QE 0.606（p<0.05）
- 说话人相似度 vs 人工ρ=0.862；自然度 vs 人工ρ=0.879
- 统一总分 vs 人工总评：QE ρ=0.714；聚合权重α_T=0.47/α_S=0.28/α_N=0.25
- 关键对比：较最强基线+0.025；学习权重比等权平均+0.043；分数标准差0.228–0.237远高于BLASER 2.0（0.119–0.144），区分度更强

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：立意务实，直指S2ST评测碎片化痛点，是首个三维一体无文本总分指标；以人工、独立指标、训练信号三重参照缓解循环验证嫌疑，附多任务/聚合消融与显著性检验。不足是语义维度ρ≈0.63仍偏低、教师蒸馏有天花板、语对限X–en且未开源。

## [8] SWIFT: A Handcrafted, Arithmetic-Minimal FPGA Engine for Real-Time Audio Deepfake Detection

**arXiv ID**：arXiv:2611.29315 | **方向**：语音大模型

**作者**：Chirantan Banerjee, Soumita Chatterjee, Bhargab B. Bhattacharya, Hafizur Rahaman

**机构**：印度工程科学技术学院Shibpur分校（IIEST Shibpur）

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.29315 | **PDF**：https://arxiv.org/pdf/2611.29315.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有深伪检测器依赖高功耗神经网络，难以部署到呼叫中心/IoT/移动取证等边缘硬件。SWIFT是无神经网络检测器：在工作合成伪影集中的高频噪声域设计整数前端与两级校准堆叠分类器。软件参考模型在8个基准上最高准确率99.86%、EER低至0.03%；定点前端加线性分类器映射到PYNQ-Z2 FPGA后单帧延迟7.85微秒（127.4k帧/秒）、功耗1.734W、LUT占用11.22%，验证边缘整数深伪检测可行性。

### 🔧 技术方案

**问题背景：** GAN判别器调优的检测器在扩散/codec LM上泛化差，主流方法依赖大型预训练编码器；边缘SoC缺乏运行这些模型或浮点单元的算力与功耗预算，已有硬件加速停留在数据中心图像/视频量化CNN。

**模型架构：** 音频16kHz、40ms窗/20ms hop量化Q15；一阶整数高通残差（整数Haar提升predict）抑制共振暴露高频噪声底；整数LeGall 5/3提升DWT分解，非对称交织LH/HL/HH经BinDCT26压缩成104维DWT倒谱，连同Mahalanobis（10）、Poincaré相空间（24）、相位抖动（10）、局部关系异常（10）、token周期通量（8）、F0 jitter/shimmer（8）、对谱差（10）、调制谱比（8）共192维。两级堆叠：Level-0为11个并行成员（方差阈值→PCA→类平衡LightGBM 3-fold Platt校准），Level-1用L1逻辑回归融合。FPGA的PL仅跑整数残差+DWT+BinDCT+26维定点线性分类器。

**核心创新：** (1) 噪声域整数高通残差+提升DWT替代语义特征：合成器上采样棋盘/相位失配在高频细节带成结构化spike，一阶差分零乘法器即可隔离。(2) 神经网无关的9族DSP描述子融合，L1自动砍冗余成员，把单LightGBM 88.62%拉到99.78%。(3) 首个手工无NN音频深伪检测器的位精确FPGA映射，整条路径纯整数加/移位/MAC。

**训练策略：** 泄漏可控嵌套CV（外层分层5折、内层随机搜索），全部阈值/PCA/Platt/融合系数仅训练折内拟合；clip级切分避免帧泄漏；LightGBM类平衡、extra-trees随机切分。

### 📊 实验结果
**数据集**：WaveFake、LibriTTS、Audeter、MLAAD、CodecFake、ShiftySpeech、ASVspoof、SONAR（约77万样本）

**主要指标**：
- Accuracy：MLAAD 99.86%、ShiftySpeech 99.78%；EER LibriTTS 0.03%
- 对照：MLP 92.96%、单LightGBM 88.62%；SSL法91–93%（XLS-R+CL 93.42%）
- FPGA（PYNQ-Z2，50MHz）：7.85μs/帧、1.734W、5968 LUT（11.22%）、19.09% DSP；部署线性分类器98.45% acc、0.42% EER

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：把整数高通残差与提升DWT做成可位精确部署的边缘深伪前端，给出手工检测器首个嵌入式FPGA落地，工程贡献扎实、指标亮眼。不足在于训练/测试共享生成器仅测seen-generator、部署分类器只在单一基准验证、端到端DMA/PS延迟未报，鲁棒性与未见生成器、特征消融缺失。

## [9] CAST: A Deployed Speech-to-Text Cascade for Closed Captioning of Entertainment Television

**arXiv ID**：arXiv:2611.31055 | **方向**：语音大模型

**作者**：Aditya Mishra, Thanish Bolla, Bidisha Sharma, Balaji Pitchaikannu, Surbhi Sinha, Anup Kotalwar

**机构**：Warner Brothers Discovery

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.31055 | **PDF**：https://arxiv.org/pdf/2611.31055.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
长篇娱乐电视节目音乐音效密集、口音与串音复杂，冻结Whisper加单次VAD既漏低能量人声造成删除、又给近静音段诱发幻觉。CAST以完全不微调的Whisper large-v3为核心，串联Demucs人声分离、逐级放宽带语义+声学双门控的层级VAD与残差准入、便宜到昂贵的语言识别级联、歌词分流和重复修复。在100个共60.46小时内部资产上WER从6.99%降至5.36%，字幕编辑率从254.2降至221.9分钟/小时，删除率相对下降33.79%。

### 🔧 技术方案

**问题背景：** 娱乐字幕从混录母带出发，ASR漏词与幻觉被下游对齐不可逆放大；既有工作多只评识别器，几乎不公开商用STT组件的路由决策与失败模式。

**模型架构：** 级联依次为人声分离、层级VAD与残差准入、语言识别、歌词分类路由、转录、重复修复、合并对齐。pyannote分段在配置层ℓ把节点切为语音与残差，语音子段终端，残差在更深更宽松配置复检；终端残差串行经时长门、Gemini语义门与250ms Silero语音门后裁剪到单一最长burst。

**核心创新：** (1) 召回优先层级VAD+残差准入：严格层拒掉的区段逐级重检，终端残差须语义与声学两道独立门同过，在"漏检弱语音致删除"与"放行近静音致幻觉"间取折中。(2) 便宜到昂贵升级：语言识别先由Whisper-base以0.8概率解决约93.5%段，模糊输入再升MMS-LID、最后升Gemini，算力只花在模糊输入且失败非对称。(3) 回原音频而非改文本的重复修复：重复候选先按温度0-1回退重解整窗，仍循环则按1秒栅格搜分裂点重解两半，失败保留原文绝不删词。

**训练策略：** 无训练/微调，纯推理级联工程。16kHz单声道，Whisper large-v3 temperature 0，段间隔≤200ms时取前条最后80词作初始提示，歌词段由Gemini 2.5 Pro转录；单张L4约9-12GB显存，平均27.4分钟/音频小时。

### 📊 实验结果
**数据集**：内部100英语节目资产（60.46小时、569651参考词）；公开CORAAL、Earnings-22、Rev16

**主要指标**：
- WER：6.99%→5.36%（相对-23.31% vs WhisperX）；SubER 14.72%→11.18%
- 删除每千词：28.79→19.06；编辑率254.2→221.9分钟/小时（Wilcoxon p=5.8e-11）
- 公开集仅小幅改善：CORAAL 21.52→21.30、Earnings-22 14.04→13.46

**是否开源**：内部系统，暂无

### ⭐ 评分：7/10
评分理由：作为真正进入生产的娱乐字幕STT组件，论文把层级VAD、残差语义门与可逆重复修复组织成召回优先级联，并用内部加三公开集加人工编辑时长研究给出统计显著结果，工程参照价值高。不足是全部模块为现成模型组装、缺逐模块消融无法归因删除下降，内部数据不可复现。

## [10] Which Layer to Trust? Layer Selection in Frozen Speech Encoders for Singing-Voice Deepfake Detection under Signal Corruption

**arXiv ID**：arXiv:2611.29871 | **方向**：语音大模型

**作者**：Benjamin Hurt, Yefei Yang（共同第一）

**机构**：University of California, Santa Barbara

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.29871 | **PDF**：https://arxiv.org/pdf/2611.29871.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
冻结自监督语音编码器在歌声深伪检测中的层选择通常只靠开发集和干净音频，无法验证对污染与未见攻击是否泛化。本文在CtrSVDD上对冻结XEUS（19层）/XLS-R（24层）逐层与learned mix训练MHFA头，加噪/混响/编码10条件×4/2种子：干净音频L9-L12优于最后层1.99-5.5pp，mix不超最佳；开发集选层损失2.32-4.13pp EER；噪声/编码下最佳层仍在中间，混响使XEUS上层追平、XLS-R向浅层移动。结论：开发集+干净音频不可靠选层。

### 🔧 技术方案

**问题背景：** 层或层加权和常由开发集干净音频挑选，但开发集与训练攻击重叠、测试为未见攻击A09-A14，部署还要扛噪声/混响/编码，两因素很少被同时评估；歌声检测器不易由语音直接迁移。

**模型架构：** 冻结编码器XEUS（19层E-Branchformer，masked prediction+去噪去混响预训练）与XLS-R 300M；读出头统一为线性投影→LN→MHFA（K=64、H=8）→LN→线性分类；learned mix对所有层softmax加权；XEUS另试SSL–CQCC交叉注意力融合。仅训头/融合/mix，clip截补至64,600样本。

**核心创新：** (1) 同encoder同seed的配对读出实验：一次前向过各层头、同一data order，差值仅来自读出层，按seed配对差与"几个seed同号"做统计。(2) 失真系统纳入层比较：MUSAN噪声（0-20dB SNR）、325个真实RIR、MP3/Opus编解码，揭示"去混响预训练让XEUS混响下上层追平、无反向先验的XLS-R最佳层反而压浅"的不对称现象。(3) 显式检验开发集选层泛化：歌手分层bootstrap、dev-EER近乎平且ρ仅0.29/0.36，量化"dev无法在L3-L12间区分层"。

**训练策略：** 每seed训20单头+1 mix头；AdamW lr 1e-4、cosine、max 20 epochs、batch 24、每头独立早停；训练全程干净，污染只加在test前；XEUS 4 seeds跑10条件、XLS-R 2 seeds跑关键条件。

### 📊 实验结果
**数据集**：CtrSVDD（16kHz；train/dev/test=84,404/43,625/92,769 clips；main假样本A09-A13、A14商用合成）

**主要指标**：
- 干净main EER：XEUS最佳L10 7.50%，L19高1.99pp（4/4同向）；mix 8.84%劣于最佳单读
- dev选层损失：XEUS高2.32pp、XLS-R高4.13pp（ρ=0.36）
- 噪声/编码：最佳层28/30 per-seed落在L9-L12；混响：XEUS L10-L19齐平（差-0.18pp）、XLS-R浅层优（末层距最佳5.0-5.4pp）
- 域外A14：XEUS L8最优且噪声下优于L10 2.2-3.5pp全同向

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：把"dev选层"这一被普遍接受却缺验证的环节放进干净/失真×两架构×多seed的配对测量，给出dev几乎不能排序中间层、混响下两种编码器行为相反、域外攻击偏爱不同层三条可复用事实，对评测协议有直接指导价值。局限是仅1数据集2编码器1种头配方、XLS-R只有2 seed、缺可复现代码。

## [11] CANDOR: A Multilingual Provenance-Documented Corpus for Dysarthric Speech Research

**arXiv ID**：arXiv:2611.28930 | **方向**：语音大模型

**作者**：Bernard Muller, LaVonne Roberts, Leo Kaiya, Antonio Ortiz Barrañón

**机构**：The Scott-Morgan Foundation、SMF Labs、Tecnológico de Monterrey

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.28930 | **PDF**：https://arxiv.org/pdf/2611.28930.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
构音障碍ASR研究受制于语料小、几乎全英语、单病因与许可碎片化。CANDOR汇编61个语料库、17种语言、五类病因，注册2,057名构音障碍说话人与19,538名健康对照，共4,469.7小时（含1,178.8小时障碍语音；732名障碍说话人分布14种非英语，194人说Qwen3-ASR完全不支持的6种语言）。以"可审计注册表"公开构成、许可与来源链，给出七语言ASR基线：held-out合成CER 4.68%–38.55%，唯一干净的中文真实语音CER达33.73%，相差约7倍，合成增强在真实集无可测增益（+0.11点，p=0.884）。

### 🔧 技术方案

**问题背景：** 领域标杆TORGO仅8名障碍说话人，综述发现每个非英语语言恰由唯一语料库支撑；跨语言结论建立在两三种语言上，病因效应与语料库效应相互混淆。

**模型架构：** 注册表加协调流水线（非模型）：每条记录归一化语言、病因、诱因、严重度量表、许可字段；音频统一16kHz/16bit。派生制品含7个kNN声纹转换池、8个severity-matched XTTS合成池、5个对照合成池；基线用Qwen3-ASR-1.7B逐语言微调；严重度模型为HuBERT-base三阶段对比嵌入。

**核心创新：** (1) 治理与语料一体化的"注册表即资源"：31个含障碍语音的语料库中19个禁再分发（覆盖86.2%障碍说话人），改三层访问模型（公开注册表/受限语料向托管方申请/受条款继承的派生制品），使不可共享数据仍可审计引用。(2) 证伪式评测："合成增益即构音障碍能力"不成立——中文合成CER 4.72%对真实33.73%，ep2增强在真实集p=0.884无增益；主动披露评测harness静默丢弃8种语言真实音频的缺陷及修复。(3) 不强行统一不可比信息：声明15个语料库严重度标签不构成跨库映射，提供免标注音位d′代理与按病因分训的severity嵌入。

**训练策略：** 六套模型各训2 epoch（真实+kNN派生池/真实+severity合成池），初始化自1,027,832 utterance多语预训练checkpoint；XTTS适配器仅用SAP/TORGO/LibriSpeech；说话人重采样2000次bootstrap；severity测试集speaker-disjoint（CP 49,755/PD 36,325/ALS 25,217句）。

### 📊 实验结果
**数据集**：61语料库/17语言/4,469.7小时；评测面held-out XTTS合成与real_only子集

**主要指标**：
- 开放许可占比仅语料库29.0%、小时8.2%，量化了再分发瓶颈
- 中文真实CER 33.73%（7人，CI[16.83,59.61]）vs同checkpoint合成4.72%——约7倍差
- 合成增强不迁移：真实+0.11（p=0.884）而匈牙利合成面-15.8点
- severity嵌入held-out macro-F1：CP 0.829、ALS 0.788、PD 0.715，较混合病因模型提升22.6%–40.0%

**是否开源**：不发布音频与模型；计划CC-BY-4.0公开注册表与评测规范

### ⭐ 评分：7/10
评分理由：广度（194名说六种现有ASR不含语言的构音障碍说话人）与把许可链、再分发条款等治理细节系统公开的做法有真实公共品价值；以近乎苛刻的坦率拆穿自家基线在资源类文章中极罕见。扣分在基准支撑力薄弱：可用真实语音估计仅中文7人、无受控增强实验、严重度映射明确不成立。

## [12] Ultrasound Watermark: Real-time Acoustic Watermarking against Voice Scams on Smartphones

**arXiv ID**：arXiv:2611.30106 | **方向**：语音大模型

**作者**：Renzhi Hao, Shirui Cao, Yizhu Wen, Rishav Gupta, Dharani Nadendla, Mehran Kafai, Hanqing Guo, Dong Li

**机构**：Bloomberg L.P.、UMass Amherst、Indiana University、UMBC、Amazon

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.30106 | **PDF**：https://arxiv.org/pdf/2611.30106.pdf | **代码**：暂无 | **Demo**：https://ultrasoundwatermark.github.io

### 📌 简介
针对TTS/VC声纹克隆诈骗中现有防御离线、遇电话编解码退化、易被自适应攻击绕过的问题，本文提出超声水印：主叫手机用自带扬声器持续发射20kHz六载波超声、麦克风采集口面部运动回波，将相位/幅度运动特征与语音经FiLM融合生成动态水印，被叫端同步生成器-检测器校验跨模态一致性。在22人、8机型、2.5小时同步语料上六类欺骗平均AUC 0.95、端到端延迟<200ms、PESQ 3.99。

### 🔧 技术方案

**问题背景：** 深伪检测靠声学伪影且怕编解码；数字水印多离线、不校验实时性；活体检测只证"有人"无法绑定身份；四类方法均无法满足通话中实时、无需额外硬件、可防自适应攻击的来电验证。

**模型架构：** 超声支路：FIR带通分离六载波、I/Q解调取相位与幅度差分抑制静态信道，12通道特征图经多分支时序网络投影出对齐潜变量h_u；语音支路48k→16k重采样经strided残差卷积得h_a；FiLM调制z=(1+γ)·h_a+β后转置卷积解码水印，x_w=x_a+α·w。检测器为Encodec式编码上采样+1×1头出帧级概率，窗口均值聚合。

**核心创新：** (1) 用超声回波的相位多普勒与幅度变化作为"因果绑定"活体线索——物理上不可仅凭重放或合成语音复制，区别于纯音频水印。(2) 对抗对齐训练：NLL+对比对齐铰链+感知损失联合优化生成器-检测器对，强制学习语音-超声同步性。(3) 流式化与真实部署：滑动窗口、RMS 0.05静音门控、播放延迟补偿t_D=t_b+t_i+t_c，跨iOS/Android原生部署（NCNN/CoreML）。

**训练策略：** RTX 5090、Adam（β=0.5/0.9）、lr 5e-4自适应、EMA 0.99、batch 16 FP32、700k步；损失权重λloc=10、λalign=10、λloud=10、λmsspec=2、λmel/λsisnr=1；2s@48k片段80/10/10；TTS攻击用WaveNet/Tacotron2/FastSpeech，VC用VAE/GAN/扩散。

### 📊 实验结果
**数据集**：自建22 speaker、8机型、4环境、>2000句（>1700真实、150 TTS、150 VC）、>2.5小时同步语音-超声语料

**主要指标**：
- 六类欺骗平均AUC 0.95 / FPR 0.12；训练TTS/TNR 0.93/0.99
- 同步超声replay/synthesis AUC 0.84/0.88（最难场景）；部分合成r=0.5/0.1 ASR 0.26/0.30
- VoIP：G.711 TPR 0.98、Opus-96k 0.97、Opus-48k掉至0.08
- 感知与实时：PESQ 3.99、STOI 0.922、SI-SNR 25.6dB；生成器15-24ms、检测器<8ms、端到端<200ms

**是否开源**：承诺录用后开源，Demo已上线

### ⭐ 评分：7/10
评分理由：首个用手机超声回波把语音绑定口面部生理运动做实时来电活体+身份验证，思路独特且已跨iOS/Android真机部署、延迟达标。但同步超声回放/合成场景下防护退化至0.84-0.88、白盒大扰动接近失效，样本仅22人，低码率Opus不鲁棒，落地需配合会话nonce与编解码策略。

## [13] Characterizing Frozen SSL Encoders and Backends for Cross-Domain Speech Deepfake Detection

**arXiv ID**：arXiv:2611.29865 | **方向**：语音大模型

**作者**：Benjamin Hurt, Oscar O'Donnell, Yefei Yang, Anjani Sethi, Priyanka Durai

**机构**：UC Santa Barbara、Columbia University

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.29865 | **PDF**：https://arxiv.org/pdf/2611.29865.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
主流深伪检测配方在小型欺骗语料上全量微调SSL编码器，域内优异但跨域显著退化。本文将已发表的跨注意力融合配方冻结编码器，交叉两个冻结编码器（XEUS、XLSR-53）与两个后端（MHFA、AASIST）做2×2因子设计，五基准、三种子统一评测。MHFA后端下冻结XEUS较XLSR-53在LA21/DF21/ASV5相对降错58–77%；冻结XEUS+MHFA仅更新0.39M参数即在ASV5取得EER 16.67%、min-DCF 0.48，显著优于更新316M参数的全量微调基线（27.81%、0.77）。

### 🔧 技术方案

**问题背景：** 全量微调把通用编码器适配到单一语料窄统计特性，过拟合已知攻击，在未见攻击、编解码与真实录音下迁移差，In-the-Wild错误率可恶化一个数量级。

**模型架构：** 双流融合：冻结SSL（XEUS 577M或XLSR-53 315M，1024维）为SSL流；60维CQCC（96 bins/octave常数Q谱20阶倒谱加一、二阶差分）为谱流；两流线性投影至D=128，以SSL为Q、CQCC为K/V单头交叉注意力，后端MHFA（H=8、K=64）或AASIST接LayerNorm+Linear二分类。仅训投影/融合/后端/头：MHFA头390k、AASIST头332k参数。

**核心创新：** (1) 冻结因子化刻画范式：固定发表版融合配方、编码器×后端2×2交叉，五基准三种子同管线，把"哪个表征能跨域迁移、需要多少可训练参数"变成可复现控制实验。(2) 揭示编码器-后端交互效应：MHFA适配强编码器（XEUS全部域外集更优），AASIST从弱编码器中"抢救"信号并把XLSR-53的in-domain标准差从16.68压到4.66，证明"最优后端"不可跨编码器迁移。(3) 容量受控诊断：加入等参数WavLM Large+MHFA单元证实315M规模冻结特征不必劣，排除参数量解释，并用三种子全量微调对照量化"冻结约800倍参数"的交换率。

**训练策略：** 仅ASVspoof 2019 LA训练、无增强；16kHz、预加重0.97、定长64,600样本；种子{42,1234,2025}，EER均值±标准差加类分层bootstrap 95%CI；微调基线XLSR-53全解冻~316M+AASIST按dev EER选checkpoint。

### 📊 实验结果
**数据集**：训练LA19；评测LA19、ASVspoof2021 LA/DF、In-the-Wild、ASVspoof 5

**主要指标**：
- XEUS+MHFA EER：LA21 10.93%、DF21 7.97%、ITW 34.04%、ASV5 16.67%（mDCF 0.48）
- 关键对比：冻结XEUS+MHFA以0.39M可训参数较316M微调基线在ASV5降11.14pp，但DF21/ITW落后；XLSR-53三域相对降错58–77%
- 匹配聚合消融中XEUS在全部10组对比均更低

**是否开源**：暂无

### ⭐ 评分：6/10
评分理由：以实验纪律见长的刻画型工作：统一管线、三种子±标准差、匹配聚合与容量受控诊断加对预训练数据重叠的坦率限定，方法学诚实度高于同类，"后端排名依赖编码器"的交互结论有实用价值。但无新模块、不追求SOTA且在ITW上全面落后，结论限定于单一配方内，属有参考价值的增量研究。

## [14] Spoof Localization as Boundary Regression

**arXiv ID**：arXiv:2611.29085 | **方向**：语音大模型

**作者**：Yixuan Xiao, Xin Wang, Yassine El Kheir, Feidi Kallel, Arnab Das, Tim Polzehl, Sebastian Möller, Ngoc Thang Vu

**机构**：斯图加特大学、日本国立信息学研究所（NII）、DFKI、柏林工业大学

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.29085 | **PDF**：https://arxiv.org/pdf/2611.29085.pdf | **代码**：https://github.com/XIAOYixuan/boundary_detection/ | **Demo**：暂无

### 📌 简介
针对部分伪造定位中帧级模型受固定20毫秒分辨率束缚（标签量化误差、边界精度受限、评测随分辨率漂移），本文将伪造定位重构为边界回归：借鉴TriDet相对边界建模的单阶段反欺骗模型，以精确参考区间监督，输出连续时间戳的（起始、结束、分）三元组。PartialSpoof上最低点式EER 4.92%、边界误差约9毫秒、区间命中率95%；零样本迁移LlamaPartialSpoof较基线降5.79至12.23个百分点；核验发现PartialEdit发布标签结束时间严重错位（仅37%文件对齐）并发布校正版。

### 🔧 技术方案

**问题背景：** SSL前端帧间隔固定20毫秒，而篡改词段起止时刻非20毫秒整数倍，导致参考标签必须量化、预测精度被分辨率钳制、点式EER横向不可比。

**模型架构：** 前端约300M参数XLS-R（冻结卷积特征提取器、微调Transformer层）输出1024维20ms帧序列；两级核宽3一维卷积投影256通道+步长2最大池化构建20-640ms六层特征金字塔，每层接TriDet式SGP块；每instant生成提案经Soft-NMS保留100个；另设话语级门控头（六层拼接+attentive statistics pooling+两层MLP，阈值0.2）。

**核心创新：** (1) 单阶段相对边界回归替代帧分类：起止距离由分数场softmax期望建模叠加邻居偏移，残差头0.5·tanh限幅半步长，边界可落帧网格任意位置；Huber损失（尺度20ms）与IoU损失互补，训练全程使用未量化精确区间。(2) 多粒度中心采样正样本分配加IoU加权focal损失；辅助帧级头在输入处截断梯度，保证量化标签不污染回归主干。(3) 给出范围式EER在平稳遍历假设下的贝叶斯决策风险解释，并以VCTK源互相关（阈值0.99）系统核查PartialEdit标签、发布realigned校正版。

**训练策略：** AdamW，XLS-R lr 1e-5、其余1e-4、wd 0.05，5轮预热+30轮余弦，batch 8条完整话语，耐心3早停，fp16 autocast，单张48GB A6000；总损失L_cls+0.05·L_hub+L_IoU+L_utt+L_fr；超参仅在PartialSpoof dev定一次；每模型3种子取均值。

### 📊 实验结果
**数据集**：PartialSpoof、LlamaPartialSpoof、PartialEdit E1（含realigned子集），源VCTK

**主要指标**：
- PartialSpoof点式EER 4.92%（max fusion，较最强基线BAM 5.20%降0.28pp）；范围式EER 5.34%（MRM复现16.07%，降10.73pp）
- 边界精度：回归MAE起/止8.7/9.3毫秒、Matched 94.5%；帧级头14.2/17.9毫秒、78.9%
- LlamaPartialSpoof零样本26.10%（基线MRM 32.76%/CFPRF 35.01%，降5.79–12.23pp）；微调后partial 1.71%、both 2.78%
- PartialEdit realigned：帧头点式EER 0.41%（原标签版7.23%）

**是否开源**：代码已开源，校正数据集发布于HuggingFace DeepFense/partialedit-corrected

### ⭐ 评分：6/10
评分理由：把部分伪造定位从帧分类改造为精确区间回归的公式直击20ms量化痛点，8-9毫秒级边界MAE是帧级模型给不出的证据，发现并修复PartialEdit标签错位有实在社区价值。不足是绝对增益有限（点式EER仅-0.28pp）、零样本迁移仍>24%、对比方法覆盖偏少，方法启发大于性能突破。

---

## 语音前端

## [15] From Spatial Perception to Speech Recovery: Binaural Semantic Adaptation for Spatially Grounded Multi-Talker Transcription

**arXiv ID**：arXiv:2611.29012 | **方向**：语音前端

**作者**：Wenxuan He, Shan Liang

**机构**：arXiv未提供

**发布日期**：2026-11-24 | **论文**：https://arxiv.org/abs/2611.29012 | **PDF**：https://arxiv.org/pdf/2611.29012.pdf | **代码**：暂无（声明将发布） | **Demo**：暂无

### 📌 简介
现有双耳音频大模型能定位声源却难完整转写重叠语音并正确方位归因。本文构建BiCP-Bench基准（1152条同步onset+384条错时onset、16kHz双耳混合），发现基座MiDashengLM-Spatial的空间感知与语音恢复断层：四选一识别69.27%而自由转录成功率仅26.91%，联合转写归因成功为0；切换参考耳使转录偏向翻转，证明单耳语义编码丢失双耳互补信息。据此提出BiSA：冻结主干仅增230万参数（0.027%），同步联合转写归因成功率从0%升至57.81%，后说话人WER从109.47%降至29.58%。

### 🔧 技术方案

**问题背景：** 空间音频LLM在声源定位与空间问答表现良好，但无法在重叠语音中恢复每位说话人的完整话语并正确空间归因；现有方法把空间感知等同于语义恢复能力，忽视语义通路对双耳互补信息利用不足的根本瓶颈。

**模型架构：** 基座MiDashengLM-Spatial（语义编码器+空间分支+音频投影器+冻结LLM，隐层d=1280）。BiSA将固定左耳输入改为左右耳分别送入共享权重语义编码器加共享LoRA；在第4/8/…/32层后插入跨耳差分模块：Δ=H_L−H_R经rank-8独立down/up投影产生残差更新（up零初始化）；语义特征与原始空间特征P0拼接经冻结投影器入LLM，每耳序列前置可学习耳身份向量，共2,300,928可训参数。

**核心创新：** (1) BiCP-Bench三级能力体系（候选识别/位置条件转录/联合转写+空间归因），首次量化空间感知与开放语音恢复的差距，并以参考耳切换与双耳vs重复单耳对照证明双耳语义信息互补。(2) 跨耳差分交互：在语义编码内部显式建模两耳隐层差异作残差更新，与同参数量同来自交互基线相比多46.3个百分点增益，证明收益来自差分建模而非参数容量。(3) 参数高效两阶段训练：阶段1用位置条件+联合转录监督学双耳语义恢复；阶段2冻结其余、仅用480条校准7168个耳身份参数，兼顾转录能力与空间响应一致性。

**训练策略：** 自回归交叉熵、按record内query数归一；阶段1用4000条由LibriSpeech+ARI HRIR构造的双耳录音（同步/错时/单说话人混合）；阶段2在480条上仅更新身份向量并加四方向分类与候选选择监督；训练与测试在耳型和语音材料上严格隔离。

### 📊 实验结果
**数据集**：BiCP-Bench（LibriSpeech test-clean+FLEURS英文，ARI HRIR与Surrey BRIR渲染16kHz双声道）；外部Clarity CEC1（750条）、STAR-Bench、MMAU-Pro

**主要指标**：
- 联合转写正确归因成功率（同步）：57.81% vs 原始0%
- 后说话人WER（错时）：29.58% vs 109.47%；错选早期说话人响应170/384→14/384
- 位置条件转录WER：18.12% vs 65.96%；CEC1目标说话人WER 39.60% vs 59.33%
- MMAU-Pro空间题+9.54pt至64.92%，STAR-Bench基本保持（69.06% vs 70.25%）

**是否开源**：代码与基准声明将公开发布，当前暂无

### ⭐ 评分：7/10
评分理由：诊断实验设计干净，方法以0.027%参数在归因联合转写上从0%做到近58%，消融用参数量对齐基线隔离差分交互贡献，且有外部数据集泛化验证。不足是仅单一基座验证、错时增益部分依赖顺序线索、基准由仿真混合构成且与训练共享LibriSpeech语料来源，代码未释出影响复现。

---

## 其余论文（评分较低，仅列要点信息）

- **[16] Training speech deepfake detectors against worst-case filters: Gains, Costs and Limits** | arXiv:2611.28718 | 评分：6/10 | https://arxiv.org/abs/2611.28718
- **[17] Scoring L2 Pronunciation Without Synthesis: Counterfactual Velocity Contrast in Frozen Flow-Matching TTS** | arXiv:2611.29985 | 评分：6/10 | https://arxiv.org/abs/2611.29985
- **[18] Preserving Prosody in Speaker Anonymization** | arXiv:2611.28290 | 评分：6/10 | https://arxiv.org/abs/2611.28290
- **[19] Restorable Multilingual Voice Anonymization via Audio Watermarking** | arXiv:2611.28863 | 评分：6/10 | https://arxiv.org/abs/2611.28863
- **[20] PAWP-TTS: Phoneme-Aware Weight Programming for Compact Bilingual English-Nepali Speech Synthesis** | arXiv:2611.29455 | 评分：6/10 | https://arxiv.org/abs/2611.29455
- **[21] What Do Sound Event Embeddings Reveal? Auditing Speaker Leakage in Audio Representations** | arXiv:2611.31043 | 评分：5/10 | https://arxiv.org/abs/2611.31043

---

*Generated on 2026-11-26*
