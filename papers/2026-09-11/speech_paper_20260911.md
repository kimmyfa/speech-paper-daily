# 2026-09-11 语音论文速递

**共收录**: 32 篇 | **语音大模型**: 25 篇 | **语音前端**: 7 篇

> 目标日期 2026-09-11（北京时间）arXiv 语音相关论文共命中 32 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] Language Orthogonalization of Self-Supervised Speech Representations for Cross-lingual Parkinson's Detection

**arXiv ID**：2609.09499 | **方向**：语音大模型

**作者**：Minu Kim, Eunjung Yeo, Kwanghee Choi, June-Woo Kim

**机构**：美国南加州大学（University of Southern California）；美国德州大学奥斯汀分校（University of Texas at Austin）；韩国圆光大学（Wonkwang University）

**发布日期**：2026-09-08 | **论文**：https://arxiv.org/abs/2609.09499 | **PDF**：https://arxiv.org/pdf/2609.09499.pdf | **代码**：https://github.com/MINUKIMS/language-orthogonalization | **Demo**：暂无

### 📌 简介
自监督语音模型（S3M）表示中混杂的语种信息会扰乱跨语种帕金森病（PD）检测：当目标语言仅有健康对照（HC）语音时，分类器会学会区分语种而非病理，导致高特异/低敏感。本文提出语种正交化（LO）——仅用HC语音拟合S3M特征对外部VoxLingua107语种嵌入的闭式岭回归残差化。实验表明，在5个S3M骨干、3种语音任务、3种目标语言上，该方法将F1均值从0.52/0.67提升至0.87，并实现敏感度阈值跨语种迁移。

### 🔧 技术方案

**问题背景：** 大多数语音化PD检测系统仅限单语种/单语料评估，而跨语种检测需区分可迁移的病理信号与语种特有变化。S3M同时编码强大的语种结构；当训练集只含源语种患者与目标语种HC时，分类器将目标语种与HC关联，导致目标语种患者被漏检（高特异、低敏感）。已有基线 Language Shift（LS）仅将各语种HC质心对齐为常向量，不改变组内协方差，无法去除质心之外的语种依赖结构。

**模型架构：** 三级流水线：①冻结S3M逐句提取表征——5个24层1024维Transformer-Large骨干（wav2vec2-Large-LV60、XLS-R-300M、MMS-300M、WavLM-Large、HuBERT-Large），对25个表示（卷积输出+24层）做mean+std池化并逐层ℓ2归一化后跨层平均，得到2048维句级嵌入，再按说话人与任务平均；②外部语种模型VoxLingua107 ECAPA-TDNN（14M参数，107语种）提取256维说话人级LID向量g_i；③对齐层：LO在HC子集上拟合岭映射 W* = X_HᵀG_H(G_HᵀG_H + αI)⁻¹，输出残差 x'_i = x_i − W*g_i。

**核心创新：** (1) 提出语种正交化（LO），HC-only闭式岭回归残差化，无需目标语种患者语音即可去除语种可预测成分；(2) 与逐语言平移的LS不同，LO逐说话人减去随LID嵌入变化的语言分量，可去除高于分布均值的语种依赖变异；(3) 通过语种探测证明残差显著降低语种可解码性（LC），残余PC、HC紧密聚集而PD发散。

**训练策略：** 联合5折交叉验证（语种×组别分层、说话人不重叠）；训练集含全部源语种说话人及目标语种其余HC折，评估为留出HC折+全部目标语种PD（目标病理训练时完全不可见）。下游用类别平衡逻辑回归，仅用训练集统计量标准化。岭系数α为主超参，越小的α去除越多语种可预测成分。

### 📊 实验结果
**数据集**：OneVoice-MSD-2026（统一协议协调的3个PD语音库）：GermanPD（n=176）、CzechPD（n=100）、西班牙语e-PC-GITA（n=140）；任务为持续元音、DDK（/pa-ta-ka/）、朗读。

**主要指标**：
- 敏感度0.90工作点F1均值（5骨干×3任务×3目标语种×5折）：Raw 0.52 → LS 0.67 → LO 0.87（+0.35）；分任务：Vowel 0.53/0.65/0.89、DDK 0.59/0.68/0.90、Read 0.43/0.69/0.81
- 语种可解码性三语分类macro-F1（随机0.33）：HC Raw 0.99 / LS 0.76 / LO 0.47；PD Raw 0.98 / LS 0.94 / LO 0.62
- 残差几何：PD说话人中位数距离为HC的7.5–10.8倍；阈值在敏感度0.70–0.90区间跨语种迁移近似一致

**是否开源**：代码开源（GitHub）；数据集OneVoice-MSD-2026可获取，VoxLingua107、S3M骨干均为公开预训练模型。

### ⭐ 评分：9/10
方法极简且理论闭环——闭式解、仅HC拟合、无需目标语种数据，工程可复现性极高。5骨干×3任务×3语言的系统性消融及阈值迁移、筛查场景验证充分，分析部分对LS数学局限的证明与语种可解码性量化严谨支持了机制解释。扣一分在于目标语言均为印欧语系，语系多样性覆盖不足；LO对语言的"正交化"仍残留部分语种信息（PD侧0.62），且α选择缺乏无标签策略。整体为一篇高质量、实用导向的方法论工作。

---

## [2] Candor-LR: A Dyadic Conversational Dataset for Audio-Visual Speech Recognition

**arXiv ID**：2609.10394 | **方向**：语音大模型

**作者**：Rishabh Jain, Aristeidis Papadopoulos, Zhaofeng Lin, Naomi Harte

**机构**：Sigmedia Group, School of Engineering, Trinity College Dublin, Ireland（研究资助 Research Ireland Grant 22/FFP-A/11059）

**发布日期**：2026-09-11 | **论文**：https://arxiv.org/abs/2609.10394 | **PDF**：https://arxiv.org/pdf/2609.10394.pdf | **代码**：https://github.com/rishabhjain16/lipreading-data-guide/tree/main/Candor | **Demo**：暂无

### 📌 简介
本文构建了 Candor-LR，一个基于 1656 场自然双人视频会议的 AVSR 对话基准，提供 713.5/10.1/60.1 小时训练/验证/测试数据。作者设计定制清洗流水线，用 Speechmatics 词级时间戳驱动分割、人脸对齐与质量过滤。实验表明脚本式数据训练模型在真实对话上性能骤降，视觉信息与域内数据显著提升鲁棒性，并开源处理流水线。

### 🔧 技术方案

**问题背景：** 现有 AVSR 基准（LRS2/LRS3）基于脚本化、排练式广播语音，无重叠语音、无打断、声学环境单一，高分不保证真实对话鲁棒性；低 WER 常来自数据集模式与语言建模而非真实视觉表征。WildVSR、LRS-VoxMM 等虽趋于真实，但缺乏对话规模。

**模型架构：** 本文不提出新模型，核心是数据流水线。CANDOR 会话约 26–30 分钟，含双说话人独立音视频轨与 channel_map.json。（1）用 Speechmatics 词级转录（毫秒级时间戳、置信度）替代无词级对齐的 AWS 转录；（2）按 channel_map 将音频声道 0/1 映射到左右说话人视频；（3）句法分割：在标点或 >0.5s 的词语间隙处切分短语，得到 0.8–5.0s、均值 3.6s 片段；（4）RetinaFace（阈值 0.8）逐帧检测，68 关键点中裁剪唇区 48–68，缩放至 96×96、25fps（30fps 降采样），并用 3 帧滑动平均抑制抖动；（5）从独立说话人音轨提取音频（避免串扰），转单声道、16kHz、WAV，音视频同时间戳保证帧级同步。

**核心创新：** (1) 首个大规模自然双人对话 AVSR 基准，测试集 58,718 片段（60.1h）远超 LRS3 的 1,321 片段；(2) 说话人感知切分：701 名仅出现一次的说话人（约 164.9h）全部划入测试集，保证测试说话人完全未见；(3) 展示视觉模态增益随数据真实度与噪声增加而放大的对比实验范式。

**训练策略：** 文本经去标点、统一小写、去填充词（uh/um/mhm）归一化；三重过滤（时长<800ms、词数<2、纯填充词）后切分。用于基准的多数据集训练为 LRS3:433h、LRS2+LRS3:657h、Candor-LR:713h、三者合计 1370h；噪声实验采用贴心语噪声，SNR -10~+10dB，训练时 25% 概率混合噪声增强。

### 📊 实验结果
**数据集**：Candor-LR（训练/验证/测试=713.5/10.1/60.1h，共 787,670 片段，1,554 名说话人；人口统计更均衡，训练集 25–35 岁占 46%，训练 47% 女性）

**主要指标**：
- 零样本：AV-HuBERT 在 LRS3 AO 1.95/AV 1.47，Candor-LR AO 24.32/AV 22.76；Llama-AVSR Candor-LR AO 16.92、AV 16.92；Auto-AVSR-L Candor-LR AV 16.69
- 干净域内：LRS3 训练 AO 2.99→Candor-LR 26.63；Candor-LR 训练 AO 14.81、AV 10.50（Δ+4.31）；三者联合训练 Candor-LR AV 9.83（Δ+6.54），LRS2 AV 2.54、LRS3 AV 1.42
- 噪声（推理注入 10dB）：LRS3 AO 8.39 vs Candor-LR 34.60；0dB 时 Candor-LR AO 99.33 vs AV 50.63（差 48.7%）

**是否开源**：数据处理流水线及切分 ID 已开源（GitHub lipreading-data-guide）；原始数据需向 CANDOR 作者申请许可。

### ⭐ 评分：9/10
以 783.7 小时真实双人对话填补 AVSR 亟待解决的"脚本化过拟合"空白，流水线细节完整（阈值、尺寸、fps 均有据可查），实验设计严谨，从零样本、跨域到噪声鲁棒性层层递进，且严谨采用说话人不相交的测试划分。评分扣一分为原始数据未直接分发且转写依赖商业 API Speechmatics，复现成本较高。

---

## [3] Voice or Stereotype? Disentangling Acoustic and Content-Based Gender in Speech-to-Speech Models

**arXiv ID**：2609.09263 | **方向**：语音大模型

**作者**：Xiaoqun Liu, Tanu Mitra, Harshit Rajgarhia, Abhishek Mukherji

**机构**：Centific Research, University of Washington

**发布日期**：2026-09-08 | **论文**：https://arxiv.org/abs/2609.09263 | **PDF**：https://arxiv.org/pdf/2609.09263.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
在配音、翻译、语音代理等语音到语音(S2S)任务中，模型需判断说话人性别。商用S2S系统多以固定音色输出，使"输出音色是否随内容刻板印象漂移"这一传统探针结构性失效。本文用神经TTS构建 180 条音声化段落（英/西/中文 × 阳刚/中性/阴柔内容 × 男/女声），在 5 个模型的 5 类任务上交叉验证。结果：渲染音色无刻板漂移（Δ=-0.018±0.020），但内容每向阴柔推进一档，判"女性"胜算提高 1.7~24 倍，错配单元误称率 83~100%。

### 🔧 技术方案

**问题背景：** S2S模型听得到说话人嗓音中的性别信息，忠实系统应按"听起来的性别"而非"通常谁说这类内容"来判断。但主流S2S模型以单一固定输出音色回答，使"输出音色是否向刻板印象漂移"的检测永远通过——无漂移≠无偏置。现有文本偏置基准（WinoBias/BBQ）仅限英文模板/多选题，语音基准（Spoken StereoSet、VoiceBBQ）为多选QA，缺少长文本、生成式评测。

**模型架构：** 非训练类评测框架，核心为两级流水线：(1) 输入构建——用神经TTS（性别稳定音色）将LLM生成并筛选的段落合成为输入音频；(2) 评测目标——5个S2S模型：闭源GPT-4o-audio、Gemini 2.5 native-audio，开源GLM-4-Voice-9B、Step-Audio-2-mini、Kimi-Audio-7B。设计为3语言×3内容刻板×2音色性别=180条段落，含readback/paraphrase/summarize/translate/describe五类任务。性别度量：输出音色用复合阴柔指数Δ_comp（F0、F1-F3共振峰、两个wav2vec2分类器logit边际的z分数等权平均）。

**核心创新：** (1) 有效性诊断——指出"漂移检测"在固定音色系统上结构性失效（空结果源于通道无变化空间），纠正审计方法论盲区。(2) 双问题协议——同一全因子交叉设计同时回答语音渲染漂移与性别归因，以不变性而非准确率为准则评分。(3) 跨5模型×3语言的分类证据——闭源模型偏置最重（OR 6~14倍于开源），并证明非单一语言或任务特例。

**训练策略：** 无训练。数据构建：从WinoBias/BBQ取职业/活动主题作种子；LLM各语种写第一人称、说话人匿名篇段（构造性排除性别代词）；LLM评委面板打分刻板强度，每(语言,极)保留强度最高的10篇；三语评员人工核验。提示词全为语言本族语，无英文中转。

### 📊 实验结果
**数据集**：自建Voiced Passages评测集（180条段落，3语种）；评测GPT-4o-audio、Gemini 2.5 native-audio、GLM-4-Voice-9B、Step-Audio-2-mini、Kimi-Audio-7B

**主要指标**：
- 渲染音色：15次readback拟合content×voice交互无显著项，合并Δ=-0.018±0.020
- 归因胜算比：Gpt-audio OR=21.9、Gemini OR=24.3；开源GLM OR=1.7、Kimi OR=3.3、Step-Audio OR=3.4
- 误称率：错配单元83%～100%（合并90%），一致/中性单元仅2%~3%；闭源es/zh单语OR 9.9~42.8

**是否开源**：未提及代码/数据开源；受测三个开源模型权重可复现。

### ⭐ 评分：8/10
本文的"有效性诊断"切中要害——论证固定音色下漂移检测的结构性失效，为S2S公平审计提供教科书级方法论修正，创新性突出。实验设计严谨：TTS作测量仪器+H0载体门控认证输入、全因子三语交叉、不变性评分，覆盖5个代表性模型的5类生成任务。数据公开不足与每格10样本削弱可复现性与跨语言结论强度；二元性别框架限制了覆盖率。

---

## [4] Beyond Accuracy: ARIA-Rubrics for Evaluating Audio Reasoning in Large Audio Language Models

**arXiv ID**：2609.09681 | **方向**：语音大模型

**作者**：Yupei Li, Qiyang Sun, Mohamed Mady, Chenxi Wang, Zhengwei Gong, Berrak Sisman, Björn Schuller

**机构**：Imperial College London；Technische Universität München；Mohamed bin Zayed University of AI；上海交通大学；Johns Hopkins University

**发布日期**：2026-09-09 | **论文**：https://arxiv.org/abs/2609.09681 | **PDF**：https://arxiv.org/pdf/2609.09681.pdf | **代码**：https://github.com/glam-imperial/allm_assessment | **Demo**：暂无

### 📌 简介
针对LALM音频推理评估仅看准确率而无法区分"真推理"与"猜对/模式匹配"的问题，本文提出ARIA-Rubrics：以四步结构化CoT提示（Perception/Analysis/Reasoning/Answer）外化推理过程，用六个互补指标（CLAP声学接地、句嵌入跨步连贯、LLM内容充实度、条件困惑度因果性、RoBERTa-NLI推理进展、AudioSet词表声学词密度）融合成ARIA总分。在MMAR与MMAU-mini两个1000题基准上评测9个LALM，识别出Reasoning/Scaffolding/Decoration三类推理模式，与人工评价Spearman ρ=0.671。

### 🔧 技术方案

**问题背景：** 现有LALM推理基准（MMAR、MMAU等）仅以准确率评估，高分可能来自猜测或统计模式利用，无法反映推理过程忠实度；MMAR-Rubrics依赖专有模型与人工金CoT、CAFE是黑盒LLM-as-judge、OCRA纯依赖人工，均不可扩展或不透明。音频特有挑战——感知幻觉（捏造/误识别声音实体）与跨模态对齐——使纯文本指标无法直接迁移。

**模型架构：** 不构建新模型，而是评估框架。构件：(1) 四步结构化CoT提示模板（Perception/Analysis/Reasoning/Answer），其结构源自ALR/CoTA数据集的CoT认知流，验证相比自由提示精度差异<3%；(2) 六个互补指标M1-M6。

**核心创新：** (1) M1声学接地=1/|E|Σ CLAP_sim(e_i,a)，用CLAP检测感知幻觉，平均而非累加防"堆实体刷分"；(2) M4推理步因果性：用Qwen2.5-1.5B条件困惑度计算逐步加入Analysis/Reasoning后对答案的信息增益，sigmoid归一化衡量每步是否推进答案；(3) 指标互锁防作弊：M1-M6相互约束，ARIA取六指标无权重均值∈[0,1]，据得分剖面划分Reasoning/Scaffolding/Decoration三类模式。

**训练策略：** 无训练。M3用Qwen2.5-1.5B-Instruct配few-shot打分内容充实度；M2用all-mpnet-base-v2句嵌入算相邻步余弦相似度；M5用Roberta-large-mnli蕴含得分；M6用417词AudioSet本体+word2vec。答案提取用"精确匹配→子串匹配→字母映射"三阶段流程。

### 📊 实验结果
**数据集**：MMAR与MMAU-mini（各1000道多选题、无样本重叠）；评估9个LALM

**主要指标**：
- ARIA总分（MMAR）：GPT-4o-audio 0.5796（Acc 67.6%）、Gemini 2.5 Flash 0.5689、Qwen2.5-Omni 0.5449
- ARIA总分（MMAU-mini）：Gemini 2.5 Flash 0.5819、GPT-4o-audio 0.5801、AudSemThinker 0.4865
- ARIA与人评Spearman ρ=0.671（p=0.006），优于单指标最高M1（ρ=0.563）；ANOVA中模型身份解释91.9-96.4%方差

**是否开源**：代码开源（GitHub: glam-imperial/allm_assessment，CC BY 4.0）

### ⭐ 评分：8/10
首次提出面向音频推理的免人工标注、透明自动化过程评估框架，六个指标覆盖感知接地到结论一致性全链路且设计互锁防作弊，思路新颖、系统性强；实验较充分，9模型×2基准、CoT扰动三元模式验证、45位标注者人工验证，尤其ρ=0.671显著高于单指标颇具说服力。扣分点：M3-M5轻量打分器能力有限，M6词密度与人类判断弱相关（ρ=0.070），仅两个闭源模型及90实例人工规模偏小。

---

## [5] Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS

**arXiv ID**：2609.10022 | **方向**：语音大模型

**作者**：Georgios Syllas, Efthymios Georgiou, Kosmas Kritsis, Alexandros Potamianos

**机构**：雅典Athena研究中心语言与语音处理研究所；伯尔尼大学数字医学系；雅典国立理工大学

**发布日期**：2026-09-09 | **论文**：https://arxiv.org/abs/2609.10022 | **PDF**：https://arxiv.org/pdf/2609.10022.pdf | **代码**：https://gsyllas.github.io/greek-stable-tts/ | **Demo**：暂无

### 📌 简介
针对现代希腊语缺乏干净高质量单说话人TTS数据的问题，提出基于WhisperX对齐过滤的数据清洗流水线，并在Parler-TTS（880M）上先全量微调（500M解码器，50 epoch）再做说话人专属LoRA（25M参数量，3.5h单说话人数据、2 epoch）。发现LLM生成风格提示导致说话人漂移，改用确定性提示（五分组箱标签拼接）后，最佳配置取得WER 10.7%、MOS-I 4.00、MOS-C 4.24，接近真人水平。

### 🔧 技术方案

**问题背景：** 现代希腊语公开语料要么干净单说话人数据极少（CSS10仅约4h），要么多说话人且含转写及声学噪声（Common Voice约32h/412人，清洗后15.5h）；其丰富屈折形态与词重音系统对韵律建模要求高，碎片化多说话人微调会得到"说话人平均化"的不稳定音色，VITS基线质量不足无法正式评估。

**模型架构：** 采用Parler-TTS（880M）：冻结Flan-T5文本编码器经cross-attention处理风格描述，Transformer解码器自回归预测DAC残差矢量量化（RVQ）9个码本层token（delay-pattern交织），DAC解码器重建波形。

**核心创新：** (1) 半自动数据清洗流水线：源选择→WhisperX强制对齐切分（1.5–10s）→置信度/SNR/人工校队过滤，产出已验证3.5h单说话人语料；(2) 确定性提示：将语速、基频、SNR、C50等标量属性离散化为5个分位箱标签固定拼接，推理用中位数箱标准提示，消除LLM随机措辞导致的音色漂移；(3) 两阶段适应：全量微调后接说话人专属LoRA（r=16, α=32, dropout 0.05）锚定身份且保留跨语言音素先验。

**训练策略：** 两阶段均用AdamW（lr=1×10⁻⁴）。全量微调50 epoch（A100 40GB，约20h），LoRA 2 epoch（T4 16GB，约2h），按留出10%验证集最小loss选最优checkpoint。曾探索Seed-VC音色转换扩充，因伪影降质而弃用。

### 📊 实验结果
**数据集**：CSS10（4h，女声）、Common Voice希腊语（15.5h/174人）、有声书Audiobook-1（3.5h男声，LoRA专用）；测试用50句Common Voice与20句有声书留出集

**主要指标**：
- Det.+LoRA WER：10.7%（ASR底线7.8%）；CER 3.7%（LLM+LoRA WER 21.1%）
- MOS-I：Det.+LoRA 4.00（真人4.36）；MOS-C：Det.+LoRA 4.24 vs LLM+LoRA 3.56（真人4.30）
- SIM-S：约0.60（偏低，故改用模型内一致性MOS-C评估）

**是否开源**：代码、模型权重与数据处理脚本已发布；原始有声书来自私有许可无法再分发。

### ⭐ 评分：8/10
问题定位准确，以简洁有效的数据清洗+确定性提示+说话人LoRA组合在极低资源下逼近人类水平，实验设计严谨（双主观任务拆分、Friedman/Wilcoxon Holm校正、专家/非专家子组分析）；诚实报告了SIM-S仅0.6、MCD未改善与统计不显著等局限。扣分在于限于单一语言、单一男声、平实朗读风格，结论通用性有限。

---

## [6] Orukeet: Multilingual ASR with Frozen Gabor Kernels

**arXiv ID**：2609.10054 | **方向**：语音大模型

**作者**：Nathan Roll, Irene Yi, Büşra Marşan, Vianney Grenez, Gabriel Stein, Momcilo Mrkaic, Pavle Padjin, Vladimir Zeljkovic, Calbert Graham

**机构**：Oruk AI；斯坦福大学；剑桥大学；OpenWhispr；Hoid

**发布日期**：2026-09-09 | **论文**：https://arxiv.org/abs/2609.10054 | **PDF**：https://arxiv.org/pdf/2609.10054.pdf | **代码**：https://github.com/Oruk-AI/orukeet | **Demo**：https://huggingface.co/oruk/orukeet

### 📌 简介
Orukeet 以 NVIDIA Parakeet TDT 0.6B v3 为基座，用全局拟合的最优 12,288 个 Gabor 函数替换其编码器中一半的时间深度卷积核并冻结，其余参数在多语种/多口音数据上继续训练。在 25 语言 20,146 条 FLEURS 上 pooled WER 由 11.01% 降至 9.85%（相对降幅 10.6%），25 种语言中 23 种更优，且在 LibriSpeech、口音与领域共 74 个测试分片中 61 个胜出。冻结核以普通卷积权重重物化，不改变架构与推理算子。

### 🔧 技术方案

**问题背景：** 端到端 ASR 模型中蕴含大量冗余参数，能否在不改变架构、不加任何推理开销的前提下提升多语种识别？现有可学习前端（LEAF、SincNet）把解析滤波器放在模型最前端，本文思考将确定性信号处理结构嵌入编码器内部，替代已学习的时间滤波器，验证"冻结的解析结构"是否能在适配后带来增益。

**模型架构：** 起点为 NVIDIA Parakeet TDT 0.6B v3（25 语种识别器），其 FastConformer 编码器含 24 层，每层 1,024 个 9 抽头时间深度卷积核，由 token-and-duration transducer（TDT）输出文本。对每个核拟合 Gabor 函数 g_i(t)=A_i·exp[-(t-μ_i)²/2σ_i²]·cos(2πf_i(t-μ_i)+φ_i)，基于归一化残差全局排序，取最优 12,288 个（占 24,576 的一半）替换并全程冻结。材料化模型 627M 标量参数，推理仍用普通深度卷积，与 Parakeet 完全一致。

**核心创新：** (1) 首次在已训练 ASR 编码器内部用解析 Gabor 核替换并冻结已学习的时间滤波器，且同时降低 WER；(2) 全局排序式替换：不动架构、不加算子、无额外推理开销，融合核以普通卷积权重存储；(3) 确定性、可审计的替换流程：float64 拟合、多轮精修、独立校验逐字节一致。

**训练策略：** 恢复阶段用 transducer 损失、教师匹配及 token/duration 蒸馏训练剩余网络；适配阶段 4,035 步 AdamW，lr 1e-6→1e-7（β=(0.9,0.98)，权重衰减 0.001，梯度裁剪 1.0）；最后在 LibriSpeech test-other 上跑 3 遍共 168 步，3% warmup、cosine 衰减 5e-6→5e-7。单卡 A100 40GB、BF16，禁用 dropout/增强。

### 📊 实验结果
**数据集**：FLEURS（25 语言 test）、LibriSpeech test-clean/test-other；口音领域集 EuroSpeech、GigaSpeechBench、Monsoon、Golos、NST、VoxPopuli、Lesbos（47 分片 12,006 条）

**主要指标**：
- FLEURS pooled WER（20,146 条）：11.01% → 9.85%（相对 -10.6%）；language macro WER 11.07% → 9.96%
- LibriSpeech test-clean WER 1.53% → 1.46%；test-other 3.14% → 2.86%
- 口音/领域 pooled WER（47 分片）：16.72% → 15.25%；74 个分片中 61 个更低

**是否开源**：完全开源。代码 MIT（GitHub），权重与拟合函数 CC BY-SA 4.0（HuggingFace），评测记录 CC BY 4.0。

### ⭐ 评分：8/10
方法简洁新颖——不动架构、零推理开销，仅靠冻结一半时间卷积核为 Gabor 函数就带来一致且可复现的 WER 收益，在 74 个分片中 61 个占优，跨语言、口音与领域均有泛化。评估协议严谨（相同解码配置、独立审计、逐字节校验）。扣分点：改进幅度有限（FLEURS pooled 相对 -10.6%），少数语言退化但缺少消融解释；未给出训练数据量与总耗时。

---

## [7] StreamAlign: Streaming Text-Aligned Speech Tokenization

**arXiv ID**：2609.09719 | **方向**：语音大模型

**作者**：Kang-wook Kim, Jinyoung Park, Jinsoo Kim, Sehun Lee, Sang Hoon Woo, Gunhee Kim（前两位共同一作）

**机构**：首尔大学（SNU）、加州大学伯克利分校、KRAFTON、佐治亚理工学院

**发布日期**：2026-09-09 | **论文**：https://arxiv.org/abs/2609.09719 | **PDF**：https://arxiv.org/pdf/2609.09719.pdf | **代码**：暂无 | **Demo**：https://ishlove77.github.io/StreamAlign/

### 📌 简介
StreamAlign 提出流式文本对齐语音分词框架：通过字符级 RNN-T 对齐与词级 ASR 引导的在线声学-文本对齐，配合 LLM 子词级聚合解决 ASR-LLM 词表不匹配；并引入前瞻性词边界分类器，将延迟从 560ms 降至 270ms。在 LibriSpeech 上取得最低 WER（4.41）与最高 UTMOS（4.23），其 SLM 在 speech continuation 上人类评分 4.00，超越次优 3.47。

### 🔧 技术方案

**问题背景：** 现有 text-aligned 分词（TASTE、TASLA）依赖离线 ASR，需完整话语才能分词，无法流式实时处理（延迟约 410ms+300ms）；且 ASR 与 LLM 子词词表不匹配，需在词级复制特征到各子词 token，丢失细粒度声学与副语言信息。

**模型架构：** 采用流式 Conformer 编码器（CNN+12 层 Transformer、8 头、512 维隐藏、chunk 160ms、1.28s 历史），输出语义特征（末层）与声学特征（前 6 层）。冻结词级流式 ASR 提供假设，拆分为字符序列作为 RNN-T 目标，Viterbi 解码得到帧-字符对齐；LLM tokenizer 将转写切为子词，每个子词的声学帧块经 2 层 Transformer 聚合器嵌入并通过 RVQ（R=32，每层 512 码、256 维）离散化。重建采用两阶段解码：6 层 Transformer 单元预测器预测 CosyVoice3 的 S³ 帧级单元，由预训练流式声码器合成。附加 MLP 词边界分类器基于 RNN-T joint-network 状态二分类。

**核心创新：** (1) 词引导字符对齐：兼顾词级 ASR 识别精度与字符粒度，桥接 ASR-LLM 词表鸿沟，相对词级聚合降 20% WER；(2) 前瞻词边界分类器：chunk 边界处预判补全状态并行 flush，延迟从 560ms 降至 270ms（精度 99.5%/召回 97.1%）；(3) 训练推理全程流式，端到端 tokenizer+SLM RTF 0.350，低于实时线。

**训练策略：** 两阶段训练。对齐阶段用 RNN-T 损失训练编码器+对齐器 160K 步（AdamW，lr 8e-4，wd 1e-2）；重建阶段冻结编码器，以 commit loss + L_REC 训练聚合器/RVQ/单元预测器（210K+96K 步+lr 1e-4，再微调 2 epoch）。数据：LibriTTS（约585h/2456说话人）+ Emilia 英语子集（约46K小时），DNS 噪声增强。StreamAlign-SLM 基于 Llama-3.2-1B、RVQ R=16、延迟预测（子词 m 步、声学码+时长 m+2 步）、LoRA r=64/α=128 训练 200K 步。

### 📊 实验结果
**数据集**：LibriSpeech test-clean（重建）、SALMon+spoken StoryCloze（似然分类）、LibriTTS 3s 续说、多流自发言语 1732 段

**主要指标**：
- WER：StreamAlign 4.41（SpeechTokenizer 4.63、WavTokenizer 4.95、Mimi 4.82、TASTE 8.38）
- UTMOS 4.23（最高）；SECS 0.588；单元率仅 2.97Hz，延迟 270ms
- SLM 总体一致率 70.6；续说人类评分 4.00 vs TASLM 3.47 vs GPT-4o 2.26

**是否开源**：附项目主页，未提供代码/模型仓库。

### ⭐ 评分：8/10
首次系统地解决 text-aligned 分词的流式化问题，方法巧妙（词引导字符对齐+前瞻边界分类），消融全面且自洽。重建质量在众多基线中领先且单元率最低，SLM 下游验证充分。扣分点：仅英文朗读语料、SLM 规模较小（Llama-3.2-1B+LoRA）、未开源实现，且并发工作 TASTE-Streaming 未纳入比较。

---

## [8] Source-Adaptive Data Curation for Bilingual NVV-Aware ASR

**arXiv ID**：2609.09929 | **方向**：语音大模型

**作者**：Yuang Cao, Qirui Zhan, Jingbin Hu, Ziyu Zhang, Yunxiang Chen, Houdun Liu, Shuo Feng, Bengu Wu, Lei Xie, Liumeng Xue

**机构**：西北工业大学 ASLP@NPU；深圳皮莓科技；愚图智能；南京大学

**发布日期**：2026-09-11 | **论文**：https://arxiv.org/abs/2609.09929 | **PDF**：https://arxiv.org/pdf/2609.09929.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出中英双语 NVV-aware ASR 系统，参赛 ISCSLP 2026 NVVSpeech Challenge Track 1（16 类非语言发声事件在线内标注与转写）。基于 Whisper-medium（769M）通过 checkpoint 兼容词表重映射实现词元与 NVV 标签统一自回归解码，并用"源自适应数据治理"策略（公开语料增广+多模态大模型过滤+影视媒体 NVV 挖掘）构建训练数据。官方评测下 FinalScore 由 33.32 提升至 53.61（+20.29）。

### 🔧 技术方案

**问题背景：** 笑声、叹息、呼吸、咳嗽等非语言发声（NVV）携带情感与交互信息，传统 ASR 常丢弃或归为通用符号；NVV-aware ASR 需在单一转录中同时给出词元内容、NVV 类别及转录相对位置，中英双语下难度进一步加大。现有公开语料声学多样性有限、标注质量不一。

**模型架构：** 采用 Whisper-medium（769M）全参数微调，词元与 16 类 NVV 标签共享解码输出空间、单条自回归序列联合生成。NVV 标签通过重映射 16 个未用 BPE 条目表示，删除对应 merge rules 使标签成为独立原子 token，保持词表规模与模型维度不变，直接复用预训练权重；保留多语言转录 prompt、禁用时间戳预测。

**核心创新：** (1) 检查点兼容的 NVV 词表重映射，无需扩容词表即可生成内联 NVV 标签；(2) 源自适应数据治理：公开语料经标签归一、分层噪声/速度增广与 Gemini 2.5 Pro 多模态 LLM 接受/拒绝过滤，影视媒体经预处理（MossFormer2-SE-48K 增强、Silero-VAD、Doubao ASR 2.0 分段）后由 LLM 生成式标注 NVV；(3) 互补数据聚合，混合无标签 ASR 数据作为纯语音负例抑制虚警。

**训练策略：** 自回归交叉熵损失；AdamW + 余弦调度，LR=1e-5、500 步 warm-up、有效批大小 352、bfloat16 + DeepSpeed ZeRO-2，8×RTX 4090。增广比例 40%/40%/20%，SNR∈[20,35]dB、速度因子∈[0.9,1.1]。总训练集 1178.8 小时（401,599 句；NVV 数据 1000h，512,968 个 NVV 事件，513/h）。

### 📊 实验结果
**数据集**：NVVSpeech Challenge Track 1（ISCSLP 2026）官方测试集 1,946 句（985 中 / 961 英）

**主要指标**：
- FinalScore：33.32 → 53.61（+20.29）；中文 34.05 → 55.45；英文 32.59 → 51.76
- 中文 F1_micro 0.3325 → 0.5666；mNTD 0.6602 → 0.4443
- 单类：英/中分别提升 14/16、15/16 类；EN burp 0.161→0.742、EN sigh 0.019→0.498
- 消融：Raw 33.32 → 增广 37.56(+4.24) → LLM 过滤 39.27(+1.71)；Movie 单独 46.34；最终 53.61

**是否开源**：未提及开源。

### ⭐ 评分：8/10
数据治理思路系统完整且消融严谨，各组件增益量化清晰（增广+4.24、过滤+1.71、影视数据+7.27），20.29 分提升显著；NVV 词条重映射不扩词表技巧颇具工程价值。扣分点：英文词元 WER 明显退化（25.58%→34.98%）暴露双语权衡未解决，依赖 Gemini 2.5 Pro 过滤/标注导致可复现性有限，数据与代码未开源。

---

## [9] NVV-Locator: From Transcript Tags to Acoustic Boundaries for Fine-Grained Nonverbal Vocalization Grounding

**arXiv ID**：2609.09940 | **方向**：语音大模型

**作者**：Yuang Cao, Bingshen Mu, Zhennan Lin, Guojian Li, Haoyue Zhan, Jie Liu, Chuan Xie, Qiang Zhang, Liumeng Xue, Lei Xie

**机构**：西北工业大学 ASLP@NPU；上海灵光咋现科技；南京大学

**发布日期**：2026-09-11 | **论文**：https://arxiv.org/abs/2609.09940 | **PDF**：https://arxiv.org/pdf/2609.09940.pdf | **代码**：暂无 | **Demo**：https://nvv-locator.github.io/Demo-Page/

### 📌 简介
针对非语言发声（NVV）仅以转录本文本标签表示、缺乏波形时间边界细粒度监督的问题，本文统一26类NVV分类体系，构建"双LLM校验＋转写引导强制对齐＋能量边界精修＋解耦增广"四阶段自动标注流水线，产出551.42小时带时间戳训练数据，并构建667句/1094事件的基准NVV-TimeBench。提出基于Qwen3-ASR-0.6B的非自回归槽填充模型NVV-Locator，并行预测词时间戳、NVV类别与声学起止边界，Micro/Macro F1 达 71.0%/70.2%。

### 🔧 技术方案

**问题背景：** NVV 承载情感与交互信息。现有工作或仅做片段/句级事件分类，或将其表示为转录本中的离散标签与相对位置，不保留波形起止与时长；MFA/Kaldi 等强制对齐依赖发音词典难以覆盖 OOV 的 NVV，WhisperX/NeMo 等神经对齐器主要面向词语音且对非词事件退化；时间戳监督数据稀缺、人工边界标注昂贵是核心瓶颈。

**模型架构：** NVV-Locator 基于 Qwen3-ASR-0.6B。将时间戳任务重构为转录对齐序列上的结构化槽填充：在每个转写单元后插入五槽模板⟨词起始、词结束、NVV类别、NVV起始、NVV结束⟩。时间离散化 B=750 个 bin、分辨率 40ms，覆盖 30s 音频；词表扩充 778 个任务 token。解码器单次前向并行预测所有槽位，对时间 bin 后验做 soft expectation 解码获得亚 bin 精度连续时间戳。

**核心创新：** (1) 提出 26 类统一 NVV 分类体系，按"声学归一化"合并物理事件、"功能抽象"合并词化感叹音，新增 Scream/Roar/Burp 三类；(2) 四阶段自动数据构建流水线：Qwen3-Omni 首诊＋Gemini-2.5 终判双 LLM 校验、LLM-ForcedAligner 转写引导粗窗口（τ=0.15·maxE 阈值精修）、类平衡噪声/变速解耦增广及"混合-孤立-去除"三视图数据；(3) 轻量非自回归槽填充模型，规避自回归时间戳的时序不一致。

**训练策略：** 冻结音频编码器，仅微调解码器与预测层。总损失 L=L_text_time+L_nv_type+L_event_time（均为有效位置均值交叉熵），L_event_time 仅在 NVV 存在槽位计算，per-term 归一化防止稠密词时间监督压过稀疏事件目标。验证集采用类别感知匈牙利匹配（τ_val=0.3）以事件级 Macro F1 与边界 MAE 选点。

### 📊 实验结果
**数据集**：NVV-TimeBench（667句、1094事件、约112.6分钟、覆盖全部26类）；跨语料泛化验证于 WESR-Bench

**主要指标**：
- NVV-Locator Micro F1 71.0%（最佳基线 Gemini-2.5-Pro 仅 45.8%，+25.2pp）；Macro F1 70.2%
- Macro mIoU 80.4%；Macro mMAE 59.6ms（基线 92.6ms）
- 消融：去双 LLM 校验 Macro F1 55.1；去能量精修 mMAE 劣化至 133.6；去解耦增广 66.4
- 跨语料 zero-shot：WESR-Bench Micro F1 70.2%、Macro F1 45.7%（对原系统 37.7–38.0%）

**是否开源**：代码未提供；已提供 Demo 页面。

### ⭐ 评分：8/10
选题切中 NVV"标签粒度过粗、缺乏声学边界监督"真实痛点，四阶段自动数据流水线兼具可扩展性与工程可复现价值，消融证明各阶段均有明确增益。非自回归槽填充将词级与事件级时间对齐统一到单一参考系，是简洁有效的建模选择，55ms 级边界误差已具备实用潜力。扣分点：与 Llama-FA 等词对齐方法对比不充分、训练超参与数据规模披露有限、代码未开源。

---

## [10] SpeechAnnotator: A Context-Aware Multi-Agent Framework and Benchmark for Multidimensional Speech Annotation

**arXiv ID**：2609.09947 | **方向**：语音大模型

**作者**：Qirui Zhan, Shuiyuan Wang, Jingbin Hu, Haoyu Zhang, Xiaming Ren, Jinrui Liang, Chaoren Yu, Bengu Wu, Yunxiang Chen, Houdun Liu, Su Feng, Liumeng Xue, Lei Xie

**机构**：西北工业大学、鱼图智能、深圳品美科技、南京大学

**发布日期**：2026-09-09 | **论文**：https://arxiv.org/abs/2609.09947 | **PDF**：https://arxiv.org/pdf/2609.09947.pdf | **代码**：https://github.com/ASLP-lab/SpeechAnnotator | **Demo**：https://zhanqirui.github.io/SpeechAnnotator-demo-page/

### 📌 简介
SpeechAnnotator 提出全开源、本地可部署的多智能体语音标注框架：前端模块完成分段与转写，三个专家智能体经共享状态协作，实现说话人特质、韵律、情感、副语言与声学场景等多维字段标注与受限复查；发布含 8.87 小时人工标注的 SA-Bench 基准与分离词法、闭集、开放语义评估的 SA-Eval，以低词错误率与 81.27% 属性均值逼近商业多模态系统。

### 🔧 技术方案

**问题背景：** 可控语音生成需要描述"谁在说、如何说、何场景、何语境"的细粒度段级标注。现有流程依赖人工修正、付费托管多模态 API 或固定处理链，存在标注成本高、外部服务依赖、跨阶段错误难纠正等局限；MD 评测资源按任务碎片化，缺乏统一 schema 下联合评估时间线、闭集属性与开放语义的基准。

**模型架构：** 十二阶段流水线，全部构建于开源模型。前端：FullSubNet 语音增强→MOSS-Transcribe-Diarize 估计说话人均匀段、说话人 ID 与初始转写→Qwen3-Omni 精化转写。先验提取器：DataSpeech 估计音高/能量/响度/语速，Emotion2vec 情感表征，SED 声音事件检测，按段键挂载到共享状态。Planning Agent 将本地音频证据、说话人历史、邻段语境转化为轻量"字段契约"；Labeling Agent（Qwen3-Omni）按契约做多模态预测；Review Agent（Qwen3.6-27B）运行受限复查循环，仅对证据不充分或跨段不一致字段发起定向重标注。

**核心创新：** (1) 字段级契约驱动证据路由的 Planning/Labeling/Review 三智能体协作协议，全面开源可本地部署；(2) 有界复查循环实现证据与语境感知的字段级修复，不触发全流水线重算；(3) SA-Bench（9 种音频格式、15 属性 6 大证据类目）+ SA-Eval 三分量评估（CER/cpCER/tcpCER、闭集规范化精确匹配、隐状态均值池化+裁剪余弦的开集语义评分）。

**训练策略：** 全流程零参数训练，SA-Bench 仅作 held-out 测试集。标注采用"5 标注者+2 检查员"协议。Open-Eval 对参考与预测文本取冻结 Qwen3.6-27B 最后一层隐状态、attn-mask 加权均值池化并 L2 归一化，余弦相似度截断至 [0,1]。

### 📊 实验结果
**数据集**：SA-Bench（8.87 小时中文主导、9 种源格式：现场解说 1.46h、知识讲座 1.16h、卡通 1.16h、新闻播报 1.10h 等）

**主要指标**：
- 时间线：CER 12.42%（最优）；tcpCER 33.69%（比最佳商业基线低 19.92 点）
- 属性宏平均：SpeechAnnotator 81.27%（第二），Gemini 2.5 Pro 81.73%（第一），Seed2.0 Lite 79.40%
- 15 字段中 7 项第一；最弱字段：环境 55.04%、情感 62.85%
- 消融：去 Context 79.79、去 Priors 80.07、去 Loop 80.42

**是否开源**：代码与 SA-Bench 数据将开源（GitHub 已发布），在线 Demo 可用。

### ⭐ 评分：8/10
问题定位精准，将语音标注从单任务流程升级为共享状态下的多智能体协作范式，受限复查循环概念清晰可审计；SA-Bench 覆盖 9 种中文格式与 15 维统一 schema，填补多维联合评估空白；全开源本地部署相对商业 API 有实际工程价值。但基准规模偏小（8.87 小时）、仅中文单语，属性宏平均仍落后商业 Gemini 2.5 Pro。

---

## [11] UniStream: Multi-Expert Residual Vector Quantization for 48 kHz Causal Streaming Audio Coding

**arXiv ID**：2609.09866 | **方向**：语音大模型

**作者**：Mingyu Zhao, Zhiyong Wu

**机构**：清华大学深圳国际研究生院

**发布日期**：2026-09-09 | **论文**：https://arxiv.org/abs/2609.09866 | **PDF**：https://arxiv.org/pdf/2609.09866.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出 UniStream，面向语音、音乐与环境声音的全因果 48kHz 流式神经音频编解码器。核心是 ME-RVQ（多专家残差矢量量化）：将每层单一共享码本替换为 4 个专家码本，由确定性 Top-K 路由器仅基于已解码量化状态路由，无需传输专家 ID，仅增加 5.5M 参数即扩展量化容量。配合训练期专属的 OT-CFM 流匹配正则（推理期完全移除），支持 12 kbps（Top-1）与 22.5 kbps（Top-2）两种模式，12 kbps 下语音 Mel-D 较 EnCodec 由 13.07 降至 8.21。

### 🔧 技术方案

**问题背景：** 现有 RVQ 类编解码器每层共享单一码本，难以用同一表示空间建模语音、音乐、环境声音的异构声学结构；现有 MoE 方案要么把专家放在量化瓶颈之外，要么需在码流中额外传输路由信息增加开销、阻碍流式部署；FlowMAC/FlowDec 等流式解码器需迭代推理，难以实时。

**模型架构：** 由因果卷积编码器 E、ME-RVQ 量化器 Q、因果卷积解码器 D 与训练期专属 OT-CFM 模块 F 组成。SEANet 风格对称因果 CNN，4 个步长 [2,4,5,8] 卷积块，降采样 320 倍（150 Hz 帧率）。ME-RVQ 共 L=8 层：Q0 为共享码本（1024 项），Q1–Q7 每层 E=4 个 1024 项专家码本；路由器 g=Softmax(GELU(ẑ̃W1)W2)（H=128）输出帧级软权重，Top-K 选取、权重归一化后对各专家量化结果加权求和，STE 反传，EMA 更新码本（衰减 0.99，利用率 87.3%）。

**核心创新：** (1) ME-RVQ 通过仅依赖已解码累积重构的确定性路由，使解码端可复现专家选择而无需传输专家 ID，消除信令开销（已在 A100 与 Xeon 8358 验证位精确一致）；(2) 仅训练期 OT-CFM 正则（5k 步后激活），不引入推理开销即提供额外学习信号；(3) 单一模型支持 12 kbps Top-1 与 22.5 kbps Top-2 双工作模式，全因果实时（GPU RTF 0.144）。

**训练策略：** 损失为 mel（λ=45）、STFT（1）、ℓ1（0.1）、对抗（1，10k 步后激活）、特征匹配（2）、量化（commitment + bal 0.01 + z-loss 0.001）与 FM（1）之和，MPD/MSD 判别器。数据 LibriSpeech/MTG-Jamendo/FSD50K 按 0.5/0.3/0.2 采样，48kHz、-23 LUFS，8×A100、batch 128、1s 片段训练 200k 步，Adam lr 3e-4、1k warmup、余弦衰减。

### 📊 实验结果
**数据集**：LibriSpeech test-clean（200 句）、MTG-Jamendo test（100 段）、FSD50K eval（94 段）；基线含 Opus、EnCodec（12/24k）、DAC、SNAC、Mimi

**主要指标**：
- PESQ/UTMOS/STOI（12k）：2.81 / 3.34 / 0.826；22.5k Top-2 为 3.41 / 3.87 / 0.864
- 语音 Mel-D：T1 8.21（vs EnCodec 13.07）；环境 Mel-D 10.16（vs 13.18）
- ViSQOL（T2）：语音音频模式 4.42、音乐 4.06、环境 3.96、语音模式 4.67；DNSMOS SIG 3.55 / BAK 3.89 / OVR 3.20
- 效率：训练 75.6M 参数、推理 47.9M；A100 RTF 0.144

**是否开源**：未开源。

### ⭐ 评分：8/10
ME-RVQ 消除专家 ID 传输、确定性路由降低流式部署成本思路新颖且有工程价值，双码率模式表现均具竞争力，OT-CFM 训练期正则零推理开销设计务实。全频带 ViSQOL、VGGish-FAD、DNSMOS 多维评估补足窄带指标局限。扣分点：未开源、缺乏主观听测，音乐域 FAD 与 STOI 表现偏弱。

---

## [12] AVSRBench: A Multi-Condition AVSR Benchmark

**arXiv ID**：2609.10366 | **方向**：语音大模型

**作者**：Rishabh Jain, Naomi Harte

**机构**：Sigmedia Group, School of Engineering, Trinity College Dublin（都柏林圣三一大学）

**发布日期**：2026-09-09 | **论文**：https://arxiv.org/abs/2609.10366 | **PDF**：https://arxiv.org/pdf/2609.10366.pdf | **代码**：https://github.com/rishabhjain16/lipreading-data-guide | **Demo**：暂无

### 📌 简介
本文针对 AVSR 在 LRS3 上 WER 低于 1% 却难以区分真实泛化与域适配的问题，系统评测了 Auto-AVSR、AV-HuBERT Large 和 Llama-AVSR 三种架构在六个数据集（LRS2/LRS3/GRID/LombardGrid/TCD-TIMIT/RoomReader-AV）上的视觉、音频与音视频识别性能。发现视觉理解在广播域外急剧退化，听觉-视觉融合仅对 Lombard 语音有效，极端侧脸视角主要依赖音频兜底，说话人发音清晰度的影响远大于相机角度。

### 🔧 技术方案

**问题背景：** 主流 AVSR 研究几乎全在 LRS2/LRS3 广播语料上评估，其测试集不足 1 小时；各模型评估代码与数据集紧耦合。作者追问：广播域上的低 WER 究竟代表真实泛化还是仅域内适配。已有研究表明鸡尾酒会场景 WER 可从 7% 飙升至 69%+，野外基准相对 LRS3 平均暴增约 30 绝对值，Zoom 视频会议下 Auto-AVSR AV 也从 <1% 升至 33%+。

**模型架构：** 评测三种架构（官方预训练权重、官方解码设置）：(1) Auto-AVSR——ResNet-18 视觉前端+Conformer+CTC/attention 混合解码器，3,448h 监督训练（另有 1,759h 版本）；(2) AV-HuBERT Large——VoxCeleb2+LRS3 上的掩码多模态聚类预训练，LRS3 微调；(3) Llama-AVSR——AV-HuBERT 视觉特征+Whisper 声学特征+LoRA 微调 Llama3.1-8B。评测 VO/AO/AV 三种设置的 WER。

**核心创新：** (1) 发布统一多数据集预处理工具包，将 GRID/LombardGrid/TCD-TIMIT/RoomReader 一键转换为 AV-HuBERT 与 Auto-AVSR 直接兼容格式；(2) 引入 RoomReader-AV 作为自发多轮会议语音基准，按 2 秒阈值划分 Easy(3,572句/4.9h) 与 Hard(6,752句/1.6h) 子集；(3) 首次对三种架构在六数据集上做系统性多条件横向评测，覆盖非正面相机角度、发音清晰度、Lombard 语音与视频会议四大变量。

**训练策略：** 不训练新模型；Fix checkpoint 与解码设置。预处理统一为 RetinaFace+68 关键点提取 96×96 口部 ROI、音频 16kHz、去标点小写。

### 📊 实验结果
**数据集**：LRS2、LRS3、GRID、LombardGrid、TCD-TIMIT、RoomReader-AV（六数据集覆盖广播、固定文法、Lombard、专业唇语者、自发会议语音）

**主要指标**：
- LRS3 AV WER：Llama-AVSR 0.79% < Auto-AVSR 0.90% < AV-HuBERT 1.47%
- GRID VO WER：Auto-AVSR 66.53%；融合恶化 Auto-AVSR Δ(AO-AV)=-8.90%
- LombardGrid：唯一 AV 优于 AO 的域外场景，Auto-AVSR AO 14.02%→AV 11.73%
- 90°侧脸 VO WER：Auto-AVSR 64.88%→92.50%；AV 仅小幅波动（11.59%→11.87%）靠音频兜底
- RoomReader-AV：VO 全面崩溃（Auto-AVSR 110.07%、Llama-AVSR 311.48% 幻觉）；Llama-AVSR AV 128.54%

**是否开源**：代码开源（lipreading-data-guide 工具包），RoomReader-AV 数据及管线公开。

### ⭐ 评分：8/10
选题精准，直面 AVSR"广播域内饱和"的伪收敛问题，以统一工具包和六数据集横向评测揭示视觉泛化失败、融合机制盲信视觉特征、LLM 解码器域外幻觉等重要局限，数值支撑扎实。发布的标准工具包与 RoomReader-AV 基准可复用性高。扣分点：无新模型或训练方法贡献，评测限于三模型预训练 checkpoint，对融合机制为何偏好音频缺乏机理剖析。

---

## 语音前端

## [13] Autoregressive Guidance of Deep Spatially Selective Filters using Bayesian Tracking for Efficient Extraction of Moving Speakers

**arXiv ID**：2603.23723 | **方向**：语音前端

**作者**：Jakob Kienegger, Timo Gerkmann

**机构**：德国汉堡大学（University of Hamburg）信号处理组

**发布日期**：2026-03-24（v1） | **论文**：https://arxiv.org/abs/2603.23723 | **PDF**：https://arxiv.org/pdf/2603.23723.pdf | **代码**：https://github.com/sp-uhh/autoregressive-spatial-filters | **Demo**：https://sp-uhh.github.io/autoregressive-spatial-filters/

### 📌 简介
针对移动说话人的弱引导目标说话人提取（TSE），作者在因果逐帧处理框架下将上一步增强信号自回归（AR）地融入轻量级贝叶斯跟踪器，提出两种策略：MISO-AR 将增强单通道信号作为额外观测量加入贝叶斯滤波，MIMO-AR 将深度空间选择性滤波器（SSF）扩展为多通道输出并用增强多通道估计替换带噪观测。结合基于社会力模型生成的新型合成数据集与真实录音，在计算开销几乎不变的前提下显著提升 DoA 跟踪精度与会话增强质量。

### 🔧 技术方案

**问题背景：** 深度空间选择性滤波器（SSF）对方向已知的静止说话人可实时高质量增强；但连续 DoA 信息通常不可得，移动说话人场景需依赖仅初始方位（弱引导）+跟踪算法。现有神经跟踪器精度高但计算量大，轻量统计算法（KF/PF 的 Concat 串联式）在难声学条件下精度不足。

**模型架构：** SSF 采用 SpatialNet 的逐帧因果版（窄带 Mamba 块 + 引导机制），约 1.74M 参数、18.8 GMACs/s；MIMO 扩展仅增加约 500 参数、约 800 kMACs/s/kHz。跟踪器为 Wrapped KF（线性高斯、白噪声加速度模型）与 Bootstrap PF（N=50 粒子、Watson 似然 16 或复高斯似然 23）。MISO-AR 中 KF 用 |S_tk|² 加权聚合窄带 DoA，PF 引入条件于 S_t 的似然并经 EMA 递归估计噪声协方差；MIMO-AR 估计全直射路径信号并替换观测。

**核心创新：** (1) 将增强语音 AR 反馈融入 KF 与 PF 贝叶斯滤波公式（预测替代跟踪），无需改动 SSF；(2) 提出 MIMO 空间滤波扩展，对 M 通道输出联合损失保证空间线索保留（IPD 损失）；(3) 提出基于社会力模型的移动说话人轨迹合成数据集并开源。

**训练策略：** 多阶段训练。预训练：强引导（oracle DoA）、Adam、lr=1e-3（指数衰减 0.955）、50 epoch，联合时频域 L1 损失（α=10）；微调：以贝叶斯跟踪估计引导、lr=1e-4、20 epoch，采用伪 AR（开环）训练模拟闭环推理。

### 📊 实验结果
**数据集**：合成数据集（LibriSpeech+Libri2Mix 两说话人、gpuRIR 仿真、T60 0.2–0.5s、3 麦环形阵直径 10cm）+ 实验室实拍（T60 200/350/800ms）

**主要指标**：
- ACC(10°)/MAE：MISO-AR PF 87.6%/6.47°（最优）；MIMO-AR WKF 86.4%/6.65°；Concat WKF 33.2%/32.67°
- PESQ/ESTOI：Oracle 2.14/81.6%；MISO-AR PF 2.04/80.4%
- MISO-AR PF 以 2.5 MMACs/s 全面优于 SELDnet（70 MMACs/s），仅为 CNN/LSTM（830 MMACs/s）的 1/300
- 跨轨迹泛化：在 LOCATA 任务4轨迹上获 0.3 PESQ 增益

**是否开源**：开源（代码+数据集生成脚本+项目页）。

### ⭐ 评分：9/10
自回归贝叶斯跟踪与深度空间滤波结合的思路新颖，理论上与任意 SSF 兼容，无需增加神经网络参数量即实现近乎神经跟踪器的精度；MISO/MIMO 两种 AR 方案的消融与计算量对比清晰，社会力模型数据集补足了轨迹真实性空白。主要不足是仅含两说话人、方位角一维 DoA 设定，且未与更多端到端方法对比。

---

## [14] Zero-Shot Temporal Localisation of Audio Deepfakes in Multi-Speaker Conversations

**arXiv ID**：2609.10051 | **方向**：语音前端

**作者**：Soumyadeep Roy

**机构**：印度加尔各答圣泽维尔学院数据科学研究生部；研究实习于 TCG CREST 前沿智能研究所

**发布日期**：2026-09-09 | **论文**：https://arxiv.org/abs/2609.10051 | **PDF**：https://arxiv.org/pdf/2609.10051.pdf | **代码**：https://github.com/sami42200/tdlmc-audio-deepfake-localization | **Demo**：暂无

### 📌 简介
针对"外科手术式注入"语音克隆欺诈，将多说话人对话中音频深度伪造的时间定位形式化为 TDLMC，证明混合内容文件上 utterance 级 EER/min-DCF 不适定，提出 t-IoU/TDR/TFAR/SBD/MS-DCF 等时间指标，并设计免训练的 5 阶段流水线包裹冻结检测器、以迟滞 FSM 解码器输出连贯伪造区间。在 ASVspoof 5 构建的 180 段对话上主骨干达到 t-IoU 0.90、TDR 0.95，逼近监督式定位器。

### 🔧 技术方案

**问题背景：** 语音克隆欺诈常仅替换真实通话中一句关键句，utterance 级检测器每片段只输出单一二值标签，无法定位注入片段；现有 PartialSpoof、W-TDL、LENS-DF 等定位工作均需帧级标注训练，尚无对冻结检测器免训练、无时间监督地在多说话人对话上输出位置的工作。混合内容下 naive 应用 utterance 级 EER 近随机（≈44%）。

**模型架构：** 五阶段免训练流水线包裹冻结骨干：(1–4) 16 kHz、60 s 波形用 W=2.0 s 窗口、H=1.0 s 步进滑窗得 K=59 个窗口，逐窗打分后 overlap-add 映射到 10 fps 时间轴；(5) 中值滤波（k=21）+ 高斯平滑（σ=1）后由两态迟滞 FSM 解码——p(t)≥θ_H=0.55 进入 FAKE，p(t)<θ_L=0.35 回到 REAL，死区抑制抖动；后处理丢弃 <2.0s 区间、合并 <1.5s 间隔。解码常数仅在留存校准集上以 J=t-IoU−½·TFAR 寻优。

**核心创新：** (1) 形式化定义 TDLMC 任务并证明混合内容下 utterance 级 EER/min-DCF 不适定，提出时间级指标体系；(2) 设计无需重训练的 5 阶段零样本定位流水线，对冻结检测器即插即用；(3) 用迟滞 FSM 与校准驱动常数选择抑制边界抖动，并系统诊断残差误警源于骨干域差距而非解码器；(4) 提供可复用的四模式×七种编解码器构建协议与首个 TDLMC 基线。

**训练策略：** 流水线零训练；构建 60 s 对话：四说话人语句归一化到 U[12,18] s、−23 LUFS、50ms 交叉淡化拼接，随机打七种编解码器。

### 📊 实验结果
**数据集**：ASVspoof 5 @dev + AMI 会议语料（真实多说话人对话验证）

**主要指标**：
- 主骨干 DF Arena 1B：t-IoU 0.904、TDR 0.949、TFAR 0.284、SBD 3.527s、MS-DCF 0.258、frame-EER 0.042
- 真音误警：RRRR 上 TFAR 0.0、含真音三模式均值 0.053；AMI real-only 0.017
- 监督定位器对比：t-IoU 0.909 vs 零样本最高 0.871，差距≈0.04；零样本 MS-DCF 0.220 更优
- 真实 AMI 注入 F5-TTS（≈3s）：TDR 仅 0.093，35/40 段完全漏检

**是否开源**：已开源（构建清单、逐对话分数与评测代码于 GitHub）。

### ⭐ 评分：8/10
首次为多说话人对话场景提出可复用的 TDLMC 评测协议与零样本基线，目标定位清晰且指标设计严谨；假警归因实验与真实语料 AMI 验证显著增强结论可信度。不足：测试集为人工拼接而非实时对话，边界位移约 3.5s 及真实数据注入 F5-TTS 段近全 miss 暴露骨干域差距，实际取证能力有限。

---

## [15] Over-Tightening-Aware Pseudo-Labeling for Tight-Boundary Speaker Diarization

**arXiv ID**：2609.09965 | **方向**：语音前端

**作者**：Shota Horiguchi, Takanori Ashihara, Marc Delcroix, Naohiro Tawara, Alexis Plaquet

**机构**：NTT, Inc.（日本）

**发布日期**：2026-09-09 | **论文**：https://arxiv.org/abs/2609.09965 | **PDF**：https://arxiv.org/pdf/2609.09965.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对 ASR 语料松标注导致 EEND 说话人分离模型输出边界过松、而基于因果–反因果一致性的伪标签收紧会过度收紧并引发漏检传播到下游任务的问题，论文细致分析过度收紧成因并提出三项改进：(i) 聚焦消除"停顿填充"、保留松标注起止边界的收紧；(ii) 为单向模型引入 1s burn-in 上下文缓解序列开端冷启动漏检；(iii) 将最终非因果模型纳入并行协同训练并以其实验集性能早停。DER 与理想紧标注上线差距在 AMI 缩小约 40%、AliMeeting 约 60%。

### 🔧 技术方案

**问题背景：** EEND 模型混合不同语料训练时，ASR 语料的松标注会使模型学出松散边界。前人工作基于因果/反因果模型输出平均生成紧伪标签，但伪标签源于预测、协同训练中会被过度收紧导致漏检增加。论文量化：填充停顿平均 0.336s/0.267s，而起止边界偏移均 <0.1s，说明松度主要来自停顿填充而非边界 padding。

**模型架构：** 基于 EEND-vector clustering 框架：局部说话人分离用 ReDimNet-B2 多说话人嵌入抽取器 + 单/双向 LSTM backend，powerset 分类（每块 S=4 说话人、每帧 M=2 共说），10s 窗/1s 位移滑窗；全局经 ResNet34+VoxCeleb 嵌入与 VBx 聚类聚合。因果/反因果变体通过因果卷积核、因果注意力掩码与单向 LSTM 实现。

**核心创新：** (1) 停顿填充聚焦收紧：伪标签生成时始终保留松标注起止边界，仅消除段内停顿填充；(2) Burn-in 阶段：因果模型额外输入其前 1s、反因果模型额外输入其后 1s 上下文，burn-in 区输出不参与损失、推理丢弃；(3) 非因果模型感知协同训练：最终非因果模型以松标签预训练后与因果/反因果模型并行迭代、共用同一批伪标签，并以其实验集性能早停。

**训练策略：** 逐帧交叉熵（speaker permutation 对齐后）；SC 说话人计数法修正混淆。Adam，Step1/3 用 1k 步线性 warmup 至 lr=0.001 再每 6k 步 ×0.8 指数衰减，Step2 协同训练 lr 固定 0.0001。训练混合集 352.3h（AMI-MHM 80.7h、AMI-SDM 79.7h、AliMeeting 111.4h、MSDWild 64.1h、VoxConverse 18.3h）。

### 📊 实验结果
**数据集**：AMI-MHM、AMI-SDM、AliMeeting（松标注）、MSDWild、VoxConverse（紧标注）；测试用无 collar DER，以 forced-alignment 紧标签为参考

**主要指标**：
- DER（%）C2 紧基线：AMI-MHM 14.03 / AMI-SDM 17.05 / AliMeeting 19.79
- DER（%）C4 原方法：AMI-MHM 18.28 / AMI-SDM 21.56 / AliMeeting 22.90（漏检 11.20）
- DER（%）P3 完整方案：AMI-MHM 16.40 / AMI-SDM 19.63 / AliMeeting 21.38；与上线差距缩小约 40%/60%
- 多说话人 ASR（AMI，GSS+Whisper large-v3）：tcpWER C4 26.46% → P3 24.79%（接近 C2 24.65%）

**是否开源**：未提供代码仓库；紧标签依赖公开工具 diar-forced-alignment。

### ⭐ 评分：8/10
对过度收紧成因做了扎实量化分析（停顿 vs 边界、位置级 DER），三个改进相互正交、动机清晰且实现简单；在 DER 与多通道/单通道两套 ASR 流水线上均一致提升并逼近紧标注上线。扣分点：三项改进逐项增益有限（非因果感知协同训练提升尤其小幅），验证仍需紧标签，且未开源代码复现成本较高。

---

### 其余论文速览（命中但未进入前 15 详读）

语音大模型：
- EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents | **arXiv ID**：2605.13841 | **评分**：8/10 | https://arxiv.org/abs/2605.13841
- DuplexJail: Safety Alignment Breaks Under Spoken Interruption in Full-Duplex Models | **arXiv ID**：2609.09420 | **评分**：8/10 | https://arxiv.org/abs/2609.09420
- Unifying Score and Performance for Fine-Grained Music Understanding in Audio-Language Models | **arXiv ID**：2609.10351 | **评分**：8/10 | https://arxiv.org/abs/2609.10351
- Robust Rank Aggregation for Multimodal Speech-Based Alzheimer's Disease Detection | **arXiv ID**：2609.09948 | **评分**：8/10 | https://arxiv.org/abs/2609.09948
- Pushing the Boundaries of Streaming Multi-Speaker ASR: A Systematic Study of Architectural Trade-offs | **arXiv ID**：2609.10265 | **评分**：7.5/10 | https://arxiv.org/abs/2609.10265
- Arti-JEPA: Adapting Video World Model to Real-Time MRI of the Vocal Tract for Speech-Production Analysis | **arXiv ID**：2609.09757 | **评分**：7/10 | https://arxiv.org/abs/2609.09757
- NOPE-HYPE: A Structured Simulation Workflow for Robust Speech-to-Text Across Diverse Acoustic Environments | **arXiv ID**：2609.10058 | **评分**：7/10 | https://arxiv.org/abs/2609.10058
- Do speech foundation models really learn words? | **arXiv ID**：2609.10434 | **评分**：7/10 | https://arxiv.org/abs/2609.10434
- Omni Interaction Agent Technical Report | **arXiv ID**：2609.08977 | **评分**：7/10 | https://arxiv.org/abs/2609.08977
- SphereVAE: Hyperspherical Latent Autoencoders for Robust Autoregressive Speech Representation Modeling | **arXiv ID**：2609.09903 | **评分**：7/10 | https://arxiv.org/abs/2609.09903
- Phoneme-Aware Pronunciation Representations for L2-English L1-Background Accent Identification | **arXiv ID**：2609.10466 | **评分**：7/10 | https://arxiv.org/abs/2609.10466
- V2TATC: Joint Voice-Trajectory Embedding and Dataset for Air Traffic Controller Situational Awareness | **arXiv ID**：2608.28981 | **评分**：7/10 | https://arxiv.org/abs/2608.28981
- SCNet: Enhancing GAN-based Speech Generation with Subband Condition Network and Magnitude-aware Reconstruction | **arXiv ID**：2609.10025 | **评分**：6/10 | https://arxiv.org/abs/2609.10025

语音前端：
- Audio Deepfake Detection Using Temporal Coherence Analysis | **arXiv ID**：2609.09489 | **评分**：7/10 | https://arxiv.org/abs/2609.09489
- Who Are They to Each Other? Multi-Agent Reasoning for Speaker Relationship Inference | **arXiv ID**：2609.09628 | **评分**：7/10 | https://arxiv.org/abs/2609.09628
- Teacher-Free Self-Distilled Consistency Trajectory Learning for Fast Speech Enhancement | **arXiv ID**：2609.10392 | **评分**：7/10 | https://arxiv.org/abs/2609.10392
- Vocal Music under Phoneme-Conditional Analysis | **arXiv ID**：2608.30823 | **评分**：6/10 | https://arxiv.org/abs/2608.30823

---

*Generated on 2026-09-11*