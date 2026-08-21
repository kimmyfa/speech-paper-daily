# 2026-08-20 语音论文速递

**共收录**: 6 篇 | **语音大模型**: 4 篇 | **语音前端**: 2 篇

> 今日 arXiv 语音相关论文共命中 6 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio Learners

**arXiv ID**：2608.19863 | **方向**：语音大模型 / 自监督音频表示学习

**作者**：Umberto Cappellazzo, Xubo Liu, Stavros Petridis, Maja Pantic

**机构**：Imperial College London（帝国理工学院）; University of Surrey（萨里大学）

**发布日期**：2026-08-20 | **论文**：https://arxiv.org/abs/2608.19863 | **PDF**：https://arxiv.org/pdf/2608.19863.pdf | **代码**：https://github.com/umbertocappellazzo/nape | **Demo**：暂无

### 📌 简介
本文提出 NAPE（Next-Audio-Patch-Embedding prediction），将大语言模型中"预测下一个元素"的自回归范式引入自监督音频表示学习：把一个因果 Transformer 训练为，仅凭之前谱图模块的嵌入去预测下一个 patch 的连续嵌入。设计刻意极简，只用因果掩码加 stop-gradient 作为全部训练信号，彻底摆脱了重建解码器、声学 tokenizer、teacher-student 结构和辅助正则损失。作者主张音频比静态图像更适合该范式，因为音频沿时间轴天然有序，下一个片段预测同时契合声学事件的涌现方式与语言模型的序列式学习。在六个音频与语音基准上，NAPE 在多个任务达到或追平 SOTA，且在三档模型规模上表现出稳定一致的缩放规律。

### 🔧 技术方案

**问题背景**：主流音频 SSL 方法要么走掩码谱图重建（如 Audio-MAE），要么走 EMA 师生蒸馏（如 EAT、ASiT、SSLAM、BEATs），前置配方日趋复杂：需要重建解码器把隐表示映射回 mel、需单独训练声学 tokenizer 提供离散目标、需 EMA 更新目标编码器和额外正则损失来稳定训练。与此同时，视觉与语言领域已证明"从上下文直接预测下一元素"的简单自回归目标即可学到数据分布，但这一思路在音频 SSL 中尚属空白，而音频恰恰是最适合因果预测的模态。

**模型架构**：输入先经过 128 维 mel、25ms 窗、10ms hop 计算 log-mel 谱图，切成不重叠的 16x16 patch（10 秒片段共 504 个），由默认 Conv2d patch embedding 层投影得到嵌入序列。2D patch 网格须先按一种扫描顺序线性化成一维序列，作者对比了 raster、time-major、zigzag、diagonal 四种顺序；因果 Transformer 编码器（ViT 结构、pre-norm、RoPE 沿时间与频率轴独立施加、LayerScale、QK 归一化）在因果掩码下处理序列，轻量预测头 g 在每步预测下一个 patch 的嵌入。下游微调时移除因果掩码改为双向注意力，在均值池化的 token 上接线性分类头。

**核心创新**：其一是任务形式——在连续嵌入空间做类 next-token 预测而非离散词表，目标仅为共享 patch embedding 层产生的嵌入，通过负余弦相似度衡量并配合 stop-gradient，整条目标无需任何重建或辅助损失。其二是三项防坍缩机制的协同：因果掩码阻止预测时窥视目标、预测位移（位置 t 预测 t+1 而非自身）杜绝复制输入、目标分支 stop-gradient 防止两侧同时回传梯度导致表示坍缩，消融显示任去其一即训练发散或性能骤降。其三是面向音频特有的扫描顺序设计，它决定每一步可用的因果上下文与结构归纳偏置。附录还系统对比了 patchifier（Conv2d/Convstem/Speechstem）、预测目标（patch embedding/raw mel/首层编码器输出）、相似度函数（余弦/交叉熵/L1/L2）等设计轴。

**训练策略**：在无标签 AudioSet 上预训练（unbalanced 1,964,222 条 + balanced 20,961 条，与主流工作一致），Small/Base/Large 三档规模分别为约 19M/85M/303M 参数，Small 与 Large 训练 25 轮、Base 30 轮。AdamW，lr 5e-3 带余弦退火、weight decay 0.05、batch 256（Large 为 128）、10% warmup，在 NVIDIA L40s 上用 HF Trainer 与 DDP 训练。微调使用层式学习率衰减，AudioSet 用二分类交叉熵、单标签任务用软目标交叉熵，配 SpecAugment、Mixup、CutMix、DropPath、时间翻转、加噪与标签平滑等增强，AudioSet 微调还叠加 EMA；线性探测则冻结编码器只用最佳中间层特征。

### 📊 实验结果
**数据集**：AudioSet-2M（AS-2M，mAP）、AudioSet-20K（AS-20K，mAP）、ESC-50（五折交叉验证准确率）、Speech Commands V1/V2（KS1/KS2，top-1）、IEMOCAP（ER，四类情感五折交叉验证）。

**主要指标**：NAPE-L raster 达到 AS-2M 50.2 mAP、AS-20K 40.5、ESC-50 96.0%、KS1 97.9%、KS2 98.8%、ER 68.0%；NAPE-L diagonal（96.2%/98.2%/98.9%/68.8%）在除 AS-2M 外的任务上略优。与最强基线 SSLAM（88M 参数，50.2/40.9/96.2/98.8/98.1）相比，NAPE-L raster 在 AS-2M 上打平、AS-20K（40.5 vs 40.9）与 ESC-50（96.0 vs 96.2）接近，且不依赖师生结构、混合物监督与重建解码器。NAPE 在 5 个基准上超过 A-JEPA（86M，48.6/38.4/96.3），并超过 BEATsiter3、ASiT、EAT、SPEAR（Large，49.7/39.3）等；IEMOCAP 上 NAPE-L 68.0% 比此前最强（BEATsiter3 64.5%）高出 3.5 个点。缩放方面 NAPE 在所有规模超过 Audio-MAE（Small 档 AS-2M +2.6、AS-20K +4.1 mAP）且 Base 到 Large 的增益更持久。线性探测随规模单调上升（AS-2M 23.2→25.0→27.1、AS-20K 18.9→19.7→20.4、ESC-50 79.8→81.7→83.5），最佳探测层位于网络中部（S/B/L 分别第 2/6/11 层），但绝对数值明显低于微调，符合预测式目标与线性可分性不对齐的预期。

**是否开源**：代码已开源（GitHub 仓库 https://github.com/umbertocappellazzo/nape），并提供项目主页；论文未明确说明是否发布预训练权重/checkpoint。

### ⭐ 评分：9/10
评分理由：NAPE 首次把自回归 next-embedding 预测干净利落地落地到音频领域，配方极简却能与 SSLAM 等最复杂模型打平并大幅刷新 IEMOCAP，思路清晰、说服力强；围绕扫描顺序、预测头、训练目标等做了系统消融，并给出缩放、线性探测与注意力可视化三层证据，完整度高。扣分点：预训练仅在 AudioSet 单一数据源上完成，AS-20K 与 ESC-50 仍未超过 SSLAM，线性探测表现偏弱，作者对两档规模模型间差距的量化也较简略。

---

## [2] Towards Quantifying Benchmark Optimization in ASR Models

**arXiv ID**：2608.19936 | **方向**：语音大模型 / ASR评测分析

**作者**：Theo Lebryk（通讯作者）、David Ayllon、Alice Baird、Jakub Piotr Cłapa、Jens Madsen、Panagiotis Tzirakis

**机构**：Hume AI Research（Hume AI 研究团队）

**发布日期**：2026-08-20 | **论文**：https://arxiv.org/abs/2608.19936 | **PDF**：https://arxiv.org/pdf/2608.19936.pdf | **代码**：https://github.com/HumeAI/asr-benchmark-optimization | **Demo**：暂无

### 📌 简介
公开评测基准（如 VoxPopuli、LibriSpeech）是衡量 ASR 模型能力的重要标准，但由于其公开性，模型可能针对基准进行"benchmark optimization"（benchmaxxing）——依赖基准特有的声学线索提升报告指标，而非真实通用转录能力。论文提出一套可复用的量化方法论，聚焦于"音频欠决定参考转写"的情形，设计了参考不一致（reference disagreement）、掩码数字恢复（masked-number recovery）、拼写切换（orthographic switching）三类行为探针，并配合合成语音克隆、激活修补、低秩线性操控等机制性手段，验证高 WER 优异成绩的模型会系统性复现基准参考片段。结果证明最前沿的开源模型确实在基准上"报喜"，其行为可通过输入拼接或单层激活操控双向翻转。该工作为 ASR 评测的测量可靠性提供了重要警示。

### 🔧 技术方案

**问题背景**：公开基准上的低 WER 常被误读为通用泛化能力，但以往研究主要把"基准与现实差距"当作覆盖率问题（缺什么就补什么基准）。作者指出还存在测量问题：当基准参考转写本身有错、音频被掩码、或存在语音与语义等价的两种拼写时，忠实于音频的转写器应降低错误参考的低概率，而"刷榜"模型会基于基准声学捷径匹配参考，导致基准分数虚高。语音 LLM 还能全局注意力整个音频编码，拥有更多自由度去学习基准特有策略，使该问题成为高维模态特有的风险。

**模型架构**：评估覆盖 11 个主流开源 ASR 模型，横跨两大类架构：编码器-解码器注意力/转导模型（Whisper-Large-v3、Cohere-Transcribe、Parakeet-TDT-0.6B-v2、Moonshine-Streaming）和语音大模型（Canary-Qwen-2.5B、Granite-Speech-4.1-2B、Higgs-Audio-v3-8B、Kimi-Audio-7B、Phi-4-Multimodal、Qwen3-ASR-0.6B、Voxtral-Mini-3B）。方法上提出"音频提升量"（audio lift）指标，即用参考片段在有声/静音（waveform 归零）条件下教师强制对数似然差除以字符数归一化，分离语言模型先验与端到端模型中音频的真实贡献。三类行为探针均标记参考渲染 r 与音频真实渲染 a 的对抗位置，以 accept-ref 为读出口；拼写探针另以 switch rate（两类条件 accept-ref 的较小值）排除固定拼写偏好干扰。

**核心创新**：其一，参考不一致探针采用"共识模型面板"大规模挖掘基准参考错误——以音素错误率筛选 Kimi-Audio、Qwen3-ASR、Voxtral、Moonshine 为面板，统一标注后取全体一致标记的编辑为参考错误（VoxPopuli 测试集 745 条语音共 1113 处编辑），与人工标注子集验证有 93% 重合，可扩展至无人标注数据集。其二，机制定位：通过加噪/加混响扰动、测试集说话人 TTS 克隆、同域新鲜说话人（ep-fresh、libri-fresh）、通用音色对照，刻画触发条件的"狭窄性"；再用截断、拼接 donor 音频的差分差分、激活修补（区分错误写在编码器表征还是解码器策略）、以及 dif-in-means 线性转向与低秩分析定位覆盖发生位置。其三，用 courtesy 省略案例（VoxPopuli 参考系统性漏掉"thank you, Mr. President"）做任务切换与注意力掩码验证，证明忠实表征其实可用却被解码策略忽略。

**训练策略**：本文不改任何训练流程，采用纯推理时的度量与操控协议，但结论与训练数据规模相关联——高 accept-ref 模型（Phi-4、Cohere、Granite、Canary）公开展示训练数据通常不足 1 百万小时，而低 accept-ref 的 Qwen3 采用约 4 千万小时弱监督数据，提示数据规模与基准优化倾向负相关。合成语音由 Qwen3-TTS 按基准说话人、新鲜说话人及通用预设音色生成；线性转向方向由 22 对 ep-fresh courtesy 拼接对学习，作用于单个编码器层并验证 k=1 低秩结构可恢复 65–80% 全方向效应。

### 📊 实验结果
**数据集**：VoxPopuli（英语，含 HF 版测试集 40% 说话人混入训练集的泄露背景）、LibriSpeech（clean/other）、私有真实对话集 DaiKon（held-out 控制）、以及 2026 年 6 月按 VoxPopuli 采集流程重新爬取的同域新鲜议会语音 ep-fresh 与 LibriVox 新鲜朗读人 libri-fresh（均晚于全部模型训练截点）。

**主要指标**：参考不一致探针中，VoxPopuli WER 最优的 6 个模型（5.4–5.8%）恰是 accept-ref 最高者（0.18–0.30），而 WER ≥6.5% 的模型全部 ≤0.10，指标与"刷榜"行为高度正相关。掩码数字恢复上，公开基准的 masked accept-ref 高于 held-out（LibriSpeech 顶部模型约 0.40），测试集朗读人克隆显著高于新鲜朗读人克隆。拼写切换中 6/11 模型显著超 0.50 的 honorific 基准线，8/11 模型超 archaic spacing 的 0.50，说明模型能区分数据集乃至数据子群体。机制侧：拼接 8 秒 VoxPopuli donor 可在 ep-fresh 克隆上回升 accept-ref（Phi-4 +0.10、Canary +0.09、Higgs/Cohere +0.07、Parakeet +0.04），而会话上下文拼接或截断使行为坍塌至地面；对 Cohere、Parakeet、Canary（及部分 Granite）学习到线性方向后，加入方向使通用音频 accept-ref 从近 0（0.01–0.02）升至 0.04–0.11，投影消融则使 Cohere、Canary、Parakeet 的 accept-ref 下降 82–92%；激活修补显示插入类编辑错误存在于编码器表征，删除/替换类则更多被解码策略覆盖，证明行为是端到端学得的而非纯文案污染。泄露说话人与未泄露说话人探针无显著差异（0.22 vs 0.26），排除简单数据泄露解释。

**是否开源**：开源（代码仓库 github.com/HumeAI/asr-benchmark-optimization 已随论文发布，包含探针与机制实验脚本；模型均为既有开源模型）。

### ⭐ 评分：9/10
评分理由：以罕见的严谨度把"benchmaxxing"从推测变成可测量、可操控的科学现象：三类触达行为层面的探针 + 四层机制定位（扰动、克隆、截断、拼接、patching、steering）形成完整证据链，并首次证明该行为可被单层线性转向双向翻转，低秩分析（k=1 恢复 65–80% 效应）更揭示了紧凑表征结构。实验设计周严，含多种 held-out 与归一化对照组（per-character 音频提升量）排除先验与泄露混淆，结论对评测社区有即用价值。扣 1 分：参考错误标注依赖模型共识面板、人类验证仅 93% 且集中于格式性编辑，部分结论在 4 个可转向模型上的样本量较小，训练机制（如何产生该行为）仍属推测。

---

## [3] Represented but Ignored: A Causal Account of Prosodic Underuse in Audio-Language Models

**arXiv ID**：2608.19211 | **方向**：语音大模型 / 音频语言模型韵律理解

**作者**：Linkai Peng；Baorian Nuchged

**机构**：University of Connecticut（康涅狄格大学）；The University of Texas at Austin（德州大学奥斯汀分校）

**发布日期**：2026-08-20 | **论文**：https://arxiv.org/abs/2608.19211 | **PDF**：https://arxiv.org/pdf/2608.19211.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
人类语音的韵律承载着超越词汇内容的语言与情感信息，理想的音频语言模型（audio-LLM）应能理解"怎么说"而不只是"说了什么"，但现有基准只评测最终答案，无法定位模型韵律失败的根源。本文提出一个分阶段的探针阶梯（probe ladder），把韵律失败划分为三大机制：F1 感知失败（语音通路未保留韵律对比）、F2 解释失败（内部表征了错误的韵律类别）、F3 使用不足（内部表征正确但未充分表达在答案中）。在四个纯理解型 audio-LLM 上，模型的语音通路和深层表征通常保留了韵律信息，但行为输出只部分利用该信息，F3 是占主导的失败模式。作者进一步用隐状态干预证明该潜在信号具有因果可控性，并把可恢复信号定位到稀疏特征子空间，结论是这类失败的瓶颈不在于"听不到韵律"，而在于"没有用上已经听懂的韵律"。

### 🔧 技术方案

**问题背景**：Dynamic-SUPERB、AIR-Bench、SD-Eval 等基准均以最终答案为唯一指标，一个模型把问句判成陈述句既可能源于音频通路丢失信息、也可能源于内部误解或表征未被使用，这些机制性不同的失败在传统评测中被混为一谈。作者指出韵律承载两类信息：语言性/语调信息（intonational，如问句与陈述句）与副语言/情感信息（paralinguistic，如情绪类别），需要用分层诊断而非端到端精确率来定位故障。

**模型架构**：研究覆盖四个纯理解型 audio-LLM：Qwen2.5-Omni-7B（Whisper 风格音频塔+28 层 LM）、Audio-Flamingo-3（Whisper 塔+28 层 LM）、DeSTA2.5-Audio（冻结 Whisper-large-v3 编码器+Q-Former 适配器+32 层 Llama-3.1-8B）、Phi-4-multimodal-instruct（conformer 音频塔+32 层 LM）。诊断梯子分为三级：在冻结音频塔上逐层训练线性探针并对照随机初始化基线判断 F1；在 LLM 最后一位置（answer-position）残差流上做逐层 logit-lens 读出，选 AUC 峰值层 L*，并用预测性 V-information 量化状态携带的可被线性探针利用的信息量；行为侧用三条件阶梯（仅文本无韵律提示基线、文本+显式韵律提示参考、真实音频条件）计算 shift 与 % recovery，判断 F2/F3。

**核心创新**：提出 F1/F2/F3 分阶段失败分类法与 probe ladder 框架，并用"能力鸿沟"（内部信号可解码但行为表达不足）作为 F3 的诊断签名；在 L* 层做两类单点因果干预，方向注入（向 answer-position 状态叠加类均值方向 d=μ+−μ−）与激活替换/激活修补（用匹配的反类样本在 L* 的状态替换目标样本状态），证明该信号改变会系统性改变答案 token 分布而非仅外部可读；进一步在每个架构 L* 层训练 TopK 稀疏自编码器（SAE），结合 AtP* 归因选出覆盖 95% 绝对归因的最小特征集 S0.95，仅对其中坐标做加法 clamp 即可驱动模型转向目标韵律类；最后将高归因特征与 F0 斜率、时长、RMS 能量等声学描述符做相关分析，验证稀疏特征编码了可解释的声学结构。

**训练策略**：本工作为分析型研究，不训练主模型，只在 L* 激活上训练 expansion-8、k=64 的 TopK SAE（池为 LibriSpeech、IViE、JL-Corpus、CREMA-D、ESD-English、RAVDESS、VESUS 多语料混合，RAVDESS 与 LibriSpeech 仅作池扩充，各语料按说话人×文本组留出 30%，零死特征、R² 0.94–0.98，留出 VESUS 重建 R²≈0.83–0.88）。诊断数据用匹配内容对比（同说话人、词汇近似、韵律标签相反）：IViE 问句/陈述句（430 条）、CREMA-D 四类情绪（4348 条）、VESUS 四类情绪（10073 条），ESD-English 作为补充，JL-Corpus 仅用于编码器校准，训练重叠的模型×语料格（如 DeSTA×CREMA-D）被遮蔽。提示协议采用强制二选一/多选与直接问答混合，每条样本在 N=5–7 个改写提示下投票，正面类用 recall、情绪类用宏平均 recall 打分。

### 📊 实验结果
**数据集**：IViE（语调 Q/stmt）、CREMA-D、VESUS（情绪，VESUS 为留出集）、ESD-English（补充）、JL-Corpus（校准）。

**主要指标**：音频通路探针在三个 Whisper 塔模型（Qwen、AF3、DeSTA）的 projector 处，CREMA-D/ESD 上 WA 达 0.79–0.92（相对随机基线提升 +0.28~+0.35），VESUS 达 0.69–0.72，IViE Q/stmt 达 0.71–0.81，纯 F1 在多数格被排除；Phi-4 的 conformer 中段情绪峰值 WA≈0.84，但传入 LLM 的表示中 VESUS 仅 ≤0.52（真 F1 弱点）。内部读出在 11 个干净格中 8 个取得 L* 高 AUC 0.81–1.00，情绪格 V-information 达 1.49–1.75 bits（上限约 2.0），但 IViE 格 AUC 0.81–0.83 而 V-information 仅 0.23–0.41 bits（线性可分信息弱）。行为恢复率：IViE 上 Qwen/Phi-4/AF3 仅恢复基线到参考区间的 30–36%，DeSTA 为 0%；CREMA-D 上 AF3 达 92%，VESUS 上最好的模型仍留下 40–60% 未利用。方向注入的 18 个干净格斜率全部为正且置信区间不含零；VESUS 激活修补 16 个迁移符号全部符合预测（AF3/DeSTA |Δ| 3.3–5.2，Phi-4 ≤0.6）；Qwen×CREMA-D neutral/angry 格 recall 由 α=0 时 0.366 升至 α=2 时 1.000，18 格中 15 格在扫描范围内饱和。稀疏干预在 18 格中 17 格恢复目标类（唯一例外 Phi-4×VESUS neutral/angry），S0.95 仅含 33–102 个特征（不超过字典 0.5%）；声学相关上 CREMA-D 情绪格 Qwen/AF3 的 top 特征与 RMS 能量 |r|=0.51–0.73，IViE 语调格与 F0 斜率 |r|≈0.3（较弱但聚类清晰）。

**是否开源**：未开源，摘要仅声明"code will be released"，模型为公开模型（Qwen2.5-Omni、Phi-4-MM、Audio-Flamingo-3、DeSTA2.5-Audio），数据集均为公开语料。

### ⭐ 评分：8/10
评分理由：本文首次把机制可解释性工具（logit-lens、方向注入、激活修补、SAE+AtP*）系统移植到 audio-LLM 的韵律失败定位上，F1/F2/F3 分类法与三条件行为阶梯设计严谨，匹配内容语料控制了词法混淆，因果证据链完整（探针→调解读→干预→稀疏定位→声学解释）。扣分原因：模型覆盖窄（仅 4 个纯理解型密集 Transformer，未涉 MoE 与语音到语音模型）；F3 只在 7/11 格占主导而非普适；IViE 语调格的 V-information 很低，客观性存疑；干预具有方向性偏向而非选择性恢复正确类；代码未发布；声学相关为描述性分析且未做多重比较校正。

---

## [4] A Speech Corpus for Mizo Automatic Speech Recognition: Whisper and SraVaani 1.0 Fine-Tuning with Morphology-Aware Evaluation

**arXiv ID**：2608.19361 | **方向**：语音大模型 / 低资源语言ASR

**作者**：Priyankoo Sarmah、Sanasam Ranbir Singh、Lalhmingmawia

**机构**：Center for Linguistic Science and Technology, Indian Institute of Technology Guwahati, India（IIT Guwahati 语言科学与技术中心）

**发布日期**：2026-08-20 | **论文**：https://arxiv.org/abs/2608.19361 | **PDF**：https://arxiv.org/pdf/2608.19361.pdf | **代码**：暂无 | **Demo**：https://clst.iitg.ac.in/tts/mizo-as/

### 📌 简介
本文构建了首个大规模公开发布的 Mizo 语（印缅语系、印度东北部低资源语言）语音语料库，共 17.62 小时、8274 句来自 200 位说话人的朗读语音，内容涵盖报纸新闻与法院判决书翻译文本。作者将三个 Whisper 多语言模型（small/medium/large-v3）与 SraVaani 1.0 印度多语言模型在该语料上进行了说话人独立（speaker-independent）的微调与评测。由于 Mizo 正字法在形态边界（空格切分）上存在书写变体，论文提出了一种形态感知的 Mizo WER（MA-WER）评测指标，能更公允地反映识别质量。实验表明 Whisper-large-v3 微调后取得最低常规 WER 18.08%，而 SraVaani 1.0 经 Mizo 数据适配后 WER 由零样本的 58.27% 大幅降至 29.45%。

### 🔧 技术方案

**问题背景**：Mizo 是印度米佐拉姆邦及缅甸、孟加拉部分地区的低资源印缅语系语言，长期缺乏公开语音数据与连续语音识别系统。此前工作仅覆盖孤立词/数字识别，或基于 Wav2vec 2.0 与 XLS-R 微调（WER 约 11–17%）；而 Whisper 的 99 语言集不含 Mizo，SraVaani 1.0 虽原生支持 Mizo 但零样本性能未知，因此需要探索大规模多语言预训练对未见语言的适配能力。

**模型架构**：实验框架分为模型适配、基于验证集 WER 的模型选择、留出测试集评估与语言特异性错误分析四阶段。Whisper 系列为编码器-解码器 Transformer，本文使用 Whisper-small（244M）、Whisper-medium（769M）与 Whisper-large-v3（1550M，128 mel bins）三档容量版本；SraVaani 1.0 为基于 FastConformer 编码器加混合 RNNT/CTC 解码头的多语言 Indic 模型。训练环境为 RTX PRO 4500 Blackwell GPU（32GB），Whisper 用 Hugging Face Transformers 实现，SraVaani 用 NVIDIA NeMo 实现。

**核心创新**：一方面系统验证了 Whisper 对完全未见语言（Mizo）的适配可行性，并对比了模型容量与原生语言支持的差异；另一方面提出形态感知 Mizo WER，该指标将参考与假设按空白切分后允许最多四个相邻 token 拼合比较，仅当拼接字符序列完全一致即视为正确（如 "a ni" 与 "ani" 等价），从而剔除因形态边界空格变体导致的过度惩罚。同时采用两阶段 SraVaani 适配策略：冻结预训练 Conformer 编码器，仅微调解码器与 joint 层。

**训练策略**：语料经 8kHz 降采样至 16kHz、格式统一为 wav、人工校验后划分训练/验证/测试集（184/11/5 位说话人，7656/426/192 句，16.18/1.02/0.42 小时），三集说话人严格不重叠。Whisper 三个模型统一采用 Adafactor、学习率 5×10⁻⁶、有效 batch 16、训练 20 epoch，按最佳验证 WER 选 checkpoint；SraVaani 用 AdamW、LR 1×10⁻⁴、weight decay 1×10⁻³、梯度累积有效 batch 16，训练至 25 epoch 后选取第 18 epoch 的 checkpoint。

### 📊 实验结果
**数据集**：自建 Mizo 语音语料库（IITG-Mizospeech-220726-V2），17.62 小时、8274 句，已部分上传至 AI-Kosh 平台，另与 Bawitlung 等人 2025 年工作报告的 Wav2vec/XLS-R 结果做间接对比。

**主要指标**：留出测试集上 Whisper-small/medium/large-v3 微调模型的 CER 分别为 4.83%/4.02%/3.26%，WER 为 24.00%/21.69%/18.08%，MA-WER 为 11.49%/8.87%/7.22%；SraVaani 1.0 零样本 CER/WER/MA-WER 为 17.71%/58.27%/36.27%，Mizo 微调后降至 6.90%/29.45%/17.93%。结果表明性能随 Whisper 容量一致提升（medium 较 small 减 22%、large-v3 较 medium 减约 19%），且所有系统 MA-WER 显著低于常规 WER，说明大量表面错误源于形态边界空格差异。错误分析显示 SraVaani 零样本大量输出 Meitei-mayek 脚本（21 句外文脚本），微调后消失；命名实体、喉塞音 /h/、数字转写及码混合英文错误在各模型上均随微调或容量增大而减少。

**是否开源**：语料库部分开源（验证集与测试集全集及训练集 5845 句已在 AI-Kosh 的 ANRF Open License 下公开，其余训练数据即将上传）；模型仅可按研究用途申请共享，代码未提供。

### ⭐ 评分：8/10
评分理由：该工作为建设性强的低资源 ASR 资源贡献，首次公开 Mizo 连续语音语料库并系统对比 Whisper 与 SraVaani 两大多语言模型体系，实验设计严谨（说话人独立划分、验证选取、留存测试）。形态感知 MA-WER 指标切中 Mizo 形态边界书写变体的要害，对印缅语系罗马字正字法评测具有方法论价值，错误分析细致。扣分点在于语料规模有限（17.6 小时）、测试集较小（0.42 小时，5 位说话人）可能影响统计稳定性，且模型未直接开源、代码未公布，可复现性受限。

---

## 🎙️ 语音前端

---

## [5] Explainability by Design: Structured Kolmogorov-Arnold Networks over Probabilistic Attributes for Speech Deepfake Source Tracing

**arXiv ID**：2608.20213 | **方向**：语音前端 / 深度伪造语音溯源

**作者**：Hoang H. Pham, Manasi Chhibber, Tomi H. Kinnunen

**机构**：School of Computing, University of Eastern Finland（东芬兰大学计算机学院，约恩苏）

**发布日期**：2026-08-20 | **论文**：https://arxiv.org/abs/2608.20213 | **PDF**：https://arxiv.org/pdf/2608.20213.pdf | **代码**：https://github.com/HoangHPham/KAN-Probabilistic-Deepfake-Attribution | **Demo**：暂无

### 📌 简介
现代语音合成技术可生成高度逼真的伪造语音，因此深度伪造语音溯源（识别伪造语句背后的具体生成器）对取证、内容溯源与平台问责日益重要。本文在作者此前"透明概率属性"工作（将语句表示为合成器子组件的概率分布）的基础上做了两项关键扩展：一是用多任务学习（MTL）联合训练概率属性提取器，二是引入结构化 Kolmogorov-Arnold 网络（SKM）作攻击分类器。SKM 的拓扑显式遵循 ASVspoof 2019 LA 元数据中的属性—攻击关系，实现"架构即解释"，并利用 KAN 2.0 内置特征重要性机制替代 SHAP 这类事后解释器。在 ASVspoof2019-attr-17 协议上，系统在属性提取与 17 类攻击分类两个任务上均取得 99% 以上平衡准确率，兼具高精度与结构级可解释性。

### 🔧 技术方案

**问题背景**：语音深度伪造溯源需从二分类检测（真人/伪造）扩展为识别具体生成模型（如 TTS 或 VC 系统的子组件）。现有方案要么是端到端黑盒模型难以解释，要么采用两阶段设计——先独立训练一批概率属性 MLP 提取器，再用决策树或逻辑回归做后端分类、事后用 SHAP 算特征重要性——管线割裂、稳定性差、解释开销高，且难以保证解释忠实反映模型真实逻辑。

**模型架构**：整体为端到端三模块流水线。第一是 MTL 模块：共享前端采用 AASIST 或 SSL-AASIST（基于 wav2vec 2.0 XLS-R 0.3B 预训练）并移除二分类层，输出共享语句表征；在共享表征上挂 7 个属性分支，每个分支由 Houlsby 适配器（LayerNorm + 瓶颈下/上投影 + GELU + dropout + 残差）加一个线性头部（softmax 输出属性值概率）组成，7 个属性分别对应 3/6/6/9/5/10/11 个取值，共 50 个属性值；所有分支概率后验拼接成 50 维概率属性嵌入。第二是 SKM：一个单隐层浅 KAN，含 50×17 个可学习单变量激活函数（5 个网格区间、2 次 B 样条、SiLU 残差），其连边根据 ASVspoof 2019 LA 生成层次元数据手工配置，只保留对每个攻击合法的属性值—攻击边，将先验结构直接嵌入网络拓扑。第三是内置可解释性机制：按 KAN 2.0 的做法，以节点/边上激活的标准差量化变异性，并从输出层向后逐层累加传播，得到每个属性值的全局与局部重要性分数。

**核心创新**：其一，将割裂的两阶段管线统一为端到端联合训练，属性提取与攻击分类共享优化目标，替代原本独立训练的 MLP 属性银行和黑盒后端。其二，把攻击的属性依赖关系显式编码进 KAN 拓扑，实现结构性内在可解释；消融实验表明移除该结构（全连接 KAN）性能几乎持平（AASIST_ff 下 99.65% vs 99.61%），证明结构约束不牺牲精度。其三，用 KAN 内置特征重要性替代 SHAP 等事后解释器，并系统验证其一致性（与 SHAP 排名比对）与稳定性（跨 batch 规模），同时可视化单隐层激活函数的形状，揭示"激活越平滑、重要性越高"的规律。

**训练策略**：使用 ASVspoof2019-attr-17 协议（仅伪造语音、17 个攻击源，A16/A19 并入 A04/A06，闭集设定）。预处理采用基于短时能量与过零率的静音裁剪，叠加 RawBoost 增强，并把多种增广以概率化方式组合（8 种组合各 12%，4% 样本不增广）。骨干训练分三种策略：从零训练、全微调（骨干在 attr-2 检测任务预训练后整体微调）、部分微调（冻结骨干）。总损失为各属性交叉熵之和加上攻击分类交叉熵。测试集评估采用平均各类别召回的平衡准确率（BAcc）与一对更多类 EER。

### 📊 实验结果
**数据集**：ASVspoof 2019 LA（ASVspoof2019-attr-17 闭集协议）

**主要指标**：最优配置 ST_RB_SSL-AASIST_ff（全微调 SSL-AASIST 骨干）在属性提取上 BAcc 99.59%–99.92%、EER 0.07%–0.16%，17 类攻击分类 BAcc 99.64%、EER 0.11%（最好）；AASIST 骨干下从零训练与全微调攻击分类为 99.53%/99.61% BAcc、EER 0.12%/0.11%；部分微调显著退化（AASIST_pf 81.96%/3.64%，SSL-AASIST_pf 61.71%/9.86%）。相比两阶段基线（AASIST 特征 + 逻辑回归，属性提取最好 91.59% BAcc，攻击分类 84.37% BAcc/3.35% EER）大幅领先。可解释性验证上，KAN 内置重要性与 SHAP 在模型级 Spearman 相关达 0.72，多数类别正相关（A18 为唯一负相关 −0.71，A01/A06/A09/A13/A17 低于 0.5）；重要性排名跨 batch 规模稳定（batch 为 8–256 时与全局相关性 0.88–0.92，单样本 batch 降至 0.56）；全局上"text (inputs)"是最重要属性。

**是否开源**：开源（贡献者声明代码库公开，用于透明性与可复现）

### ⭐ 评分：9/10
评分理由：方法在精度上表现突出，属性提取与 17 类攻击溯源均超 99% BAcc、EER 低至 0.11%，并大幅超越先前两阶段基线；核心思想"以结构换取解释"技术路线清晰，KAN 拓扑嵌入属性—攻击先验既保内在可解释又不损精度，且对内置重要性与 SHAP 的一致性、跨 batch 稳定性做了严谨定量验证，还公开了代码。扣分点在于仅采用单一且较老的 ASVspoof 2019 LA 数据集、过度依赖生成器元数据致跨数据集泛化受限（作者自述局限），部分微调退化明显且个别类别解释与 SHAP 不一致，实验覆盖有待在 ASVspoof 2021/5 等新协议上进一步检验。

---

## [6] Tracking the Trend in How Speech Synthesizers Deceive People

**arXiv ID**：2608.19959 | **方向**：语音前端 / 深度伪造语音检测

**作者**：Milan Šalko、Anton Firc、Kamil Malinka、Vojtěch Staněk、Martin Perešini、Filip Pleško、Jakub Reš

**机构**：Security@FIT，布尔诺理工大学（Brno University of Technology）信息技术学院，捷克

**发布日期**：2026-08-20 | **论文**：https://arxiv.org/abs/2608.19959 | **PDF**：https://arxiv.org/pdf/2608.19959.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
早期研究普遍报告人对深度伪造语音有 70–80% 的检出率，但这些结论大多基于 2019 年左右的旧一代合成器。本文针对 2019、2022、2024 三个不同发布时期的合成工具（RTVC、YourTTS、ElevenLabs）开展受控实证比较：82 名 IT 从业者在明确被告知"存在深度伪造"的条件下，对全合成（full spoof）与局部替换（partial spoof）语音做逐句真实性判断，并将人类表现与六个预训练自动检测器在同一批材料上进行对照。结果显示，ElevenLabs 全合成语音的人类 F1 由旧工具的约 0.90 骤跌至 0.48，而局部伪造（仅替换一句）在严格指标下准确率不足 10%，被替换的合成句有 77% 被判为真实语音；人类与自动检测器以互补的方式失效。作者由此呼吁采用程序化核验、溯源、水印以及片段级检测等分层防御。

### 🔧 技术方案

**问题背景**：深度伪造语音在讹诈、虚假信息与语音钓鱼中威胁日益增大，但人类听觉防御的有效性随合成技术的迭代快速变化。以往研究几乎只覆盖全合成语音、且多依赖"提示存在伪造"的情境，几乎无人研究"部分伪造"这一更贴近现实的攻击形态（一条真实录音中仅替换一个句子即可改变整段话语的含义），也缺乏在同一材料上人类与自动检测器的直接对照。

**模型架构**：三位被评测的合成器代表三个技术代际——RTVC（2019）基于 Tacotron2+WaveRNN，只需 10 秒目标语音即可克隆；YourTTS（2022）是基于 VITS 的多语言零样本模型；ElevenLabs（2024）为唯一商用系统，采用先进神经网络生成自然韵律与情感变化。三者均以零样本方式、用 3 分钟源语音生成克隆音频。自动检测器基线共六个，采用通用反欺骗范式：预训练前端特征（XLS-R 300M 与 WavLM Base+）接反欺骗后端（AASIST 图注意网络与 MHFA 多头部分解注意池化），其中两个在 ASVspoof 2019 LA 上训练、（各）四个在 ASVspoof 5 上训练，输出真实语音概率并在固定阈值 t=0.5 处二值化。

**核心创新**：研究设计上的创新在于控制变量——实验素材来自 9 位知名娱乐圈公众人物（4 男 5 女，刻意避开政客）的公开 YouTube 访谈，每位说话人构成一个测试组，包含 1 条真实录音、3 条全伪造与 3 条局部伪造（每段 4 个句子，仅随机替换其中 1 句，替换文本由 ChatGPT-4 按原转写生成以模拟信息操纵）。每个测试组开头播放说话人真实参考视频，作答采取逐句三级判断（真实/合成/不确定），不确定回答被剔除。评测采用三种严格度不同的指标（最严的 All OK 要求四句全对、F1、宽松的 Over 50 Percent），并结合信号检测理论（灵敏度 d′ 与判据 c）、Krippendorff 一致性系数与按被试者聚类自助的统计检验。

**训练策略**：本研究不对合成器或检测器做任何训练，全部使用预训练权重直接推理；检测器仅做前馈打分，未针对本材料微调。数据侧确定性因素包括音量归一化与背景噪声抑制，保证局部伪造句与周围真实语音听感一致。统计检验采用 Wilcoxon 符号秩对配对被试者的全伪造与局部伪造检出率做比较。

### 📊 实验结果
**数据集**：自制问卷数据集——9 位名人 × 每套 7 段录音（每段 4 句），共 63 段、252 个句级片段，82 名 IT 从业者（男性 70、女性 11），平均完成 8.6 套、耗时约 35 分钟；不确定回答剔除后共 17,233 条有效句级判断。自动检测器在同一材料上评估。

**主要指标**：全伪造方面，RTVC 与 YourTTS 的人类 F1 与 All OK 均约 0.90（逐句准确率 0.96–0.97），而 ElevenLabs 的 All OK 仅 28%、Over 50 Percent 仅 33%（接近 31% 的随机基线）、F1 为 0.48、逐句准确率 0.43（低于 0.5 随机水平）。局部伪造方面，mixElevenLabs 的 F1 降至 0.29、All OK 低于 10%（9%），合成句仅 22.65% 被正确识别（即 77% 被判为真实），而真实句正确率仍达 88.59%；ElevenLabs 的伪造句检测率由全伪造的 0.43 跌至局部伪造的 0.23（n=73，p≈6×10⁻⁸）。人类对真实语音出现 17.5% 误报（d′：RTVC 2.75、YourTTS 2.88、ElevenLabs 0.73）。人机对照方面，检测器在 RTVC/YourTTS 全伪造上 F1 达 0.96/1.00，但在 ElevenLabs 全伪造上崩至 0.09（低于人类 0.48）；在 mixElevenLabs 上检测器 F1 0.40 高于人类 0.29，但其 All OK 为 0.00（人类 0.09）。句级一致性 Krippendorff α 总体 0.631。

**是否开源**：未开源，调查音频数据集因包含可识别公众人物的伪造语音不公开，可在合理请求下提供；代码与 Demo 均暂无。

### ⭐ 评分：8/10
评分理由：研究填补了"人类对局部伪造（partial spoofing）感知"这一重要空白，并首次在相同材料上对人类与自动检测器做直接对照，揭示了二者互补失效的新事实；统计方法严谨（信号检测论、Wilcoxon 配对检验、聚类自助置信区间），伦理与局限性讨论完整。扣分点在于每个代际仅一个工具、无法支撑"趋势"结论，被试集中于 IT 从业者且缺少未提示对照组，检测器仅用固定阈值、测试规模偏小，且未开源代码与数据、可复现性有限。

---

*由Speech-paper-daily工具 自动生成 · 数据来源：arXiv*