# 2026-10-26 语音论文速递

**共收录**: 16 篇 | **语音大模型**: 9 篇 | **语音前端**: 7 篇

> 目标日期 2026-10-26（北京时间）arXiv 语音相关论文共命中 16 篇。
> 以下是按评分排序的结果。

### 速递说明

本批次精选前 15 篇进行完整模板精读，按评分由高到低排序；其余 1 篇论文仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），未展开精读。

---

## [1] CoupleFlow: Null-Calibrated Auditory Attention Decoding With Time-Locked Brain-Speech Coupling and Flow-Matching Likelihood Ratios

**arXiv ID**：2610.32950 | **方向**：语音前端

**作者**：Ali Alavi, Donald S. Williamson

**机构**：Department of Computer Science and Engineering, The Ohio State University

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32950 | **PDF**：https://arxiv.org/pdf/2610.32950.pdf | **代码**：https://github.com/saliAlavi/coupleflow | **Demo**：https://salialavi.github.io/coupleflow/

### 📌 简介
听觉注意解码（AAD）要从秒级 EEG 判断听者聚焦哪一路语音，近期直接分类器报 1 s 近完美精度。本文证明其源于试次泄漏、眼动与响度捷径，跨内容即崩至随机。提出 CoupleFlow：决策仅经神经与声学嵌入的时间耦合，脑信号无时间信息时落于随机（null 校准），并以条件流匹配头构造 PMI 似然比判决、证明其贝叶斯最优。9 个 EEG/MEG 数据集内容不相交折下 5 s 于 7/8 集最优（KU Leuven 72.7%，较最强基线 +6.8 分），所有 null 保持随机，并导出单参数预测窗长—精度关系的证据积累定律。

### 🔧 技术方案

**问题背景：** 重建法需数十秒才可靠；直接分类器借试次内划分虚高至 95%+，跨试次跌回随机；各家预处理不一，NJU 集甚至未与音频时间锁定。

**模型架构：** EEG 映射 64 通道@64 Hz，经 rank-2 听者修正、64→8 虚拟传感卷积与 5 层膨胀编码器（仅取声后 lag 窗）得神经嵌入；每候选以包络、onset、8/28 子带、glimpsed/masked 通道（54 维）经共享权因果卷积得声学嵌入；两路仅在时间中心化耦合分数相交，流匹配头另供 PMI 判决。全模型约 13–15 万参数，判决路径仅 2.6 万+256/听者。

**核心创新：** (1) Null 校准耦合分数：嵌入时间中心化后取逐维 Pearson 相关的可学习加权和，恒定 EEG 使所有候选得 0 分（Prop.1），构造上排除响度/音色/试次身份等捷径，另配四重防捷径损失。(2) 流匹配 PMI 判决：classifier-free 条件流同学 p(x|EEG) 与 p(x)，带脑/不带脑残差差近似 PMI，先验相消、无"典型语音"偏置，仅依赖注意流时贝叶斯最优。(3) 无泄漏基准与积累定律：按包络互相关恢复内容组构建不相交折，配跨试次/循环 null 与声前 lag 控制；Prop.3 精度—窗长公式单参数拟合全部 14 条曲线。

**训练策略：** 损失=CE(平滑 0.1)+InfoNCE(1)+null hinge(0.5)+VICReg(0.1)+音频对抗(0.3)+flow(0.3)+side(0.3)+包络读出(0.2)，统一设定；AdamW lr 3e-4、wd 1e-5；单听者 batch≤32 窗、5 s 裁剪、≤100 epoch 早停；按验证 contribution（精度−null）选模，lag(0/125 ms) 为唯一逐数据集超参；1×A100/折。

### 📊 实验结果
**数据集**：9 个公开集经统一管线（0.5–32 Hz、64@64 Hz、28 带 gammatone 包络）：六个四语言双说话人集（KU Leuven/DTU/Fuglsang'20 含 22 听损/ESAA 中文/KUL-255ch/Broderick）、单说话人 SparrKULee/MEG-MASC、室内 6 选 4 MAESTRO；排除未锁时 NJU 与不可切分 AV-GC。

**主要指标**：
- 5 s 内容不相交折：KU Leuven 72.7%(+6.8)、DTU 76.2、Fuglsang'20 79.6、ESAA 77.9、KUL-255ch 69.4、SparrKULee 92.2(+8.9)、MEG-MASC 99.0%，7/8 最优；Broderick 63.6 持平线性
- LOSO 未见听者高出 pooled linear 2.0–8.3 分；MAESTRO(随机 25%) 因果对齐 71.2%/试次、LOSO 56.9%（null 24.8–25.3%），超 MERIT 与官方基准
- 流 PMI 规则 69.8–97.1% 比条件似然高 5–25 分，仅音频先验 47.0–50.9% 近随机
- 积累定律 MAE 0.2–1.8 分，EEG 达 95% 需 7–170 s、MEG ρ=1.02
- 泄漏对照：试次内划分虚高 16.7–31.5 分；DARNet/DBPNet/ListenNet 不相交折跌至 40–62%

**是否开源**：代码与 checkpoint 已开源 @ https://github.com/saliAlavi/coupleflow。

### ⭐ 评分：9/10
评分理由：直击 AAD 评测的系统性泄漏，null 校准为"只能读脑"提供构造性保证，其统一协议构成最严格基准并推翻 1 s 95% 旧结论；PMI 规则与积累定律兼具理论深度与窗长—SNR 实用价值。扣分因 EEG 性能距 5 s 实用目标仍远，部分对比依赖并行发布的 MAESTRO/MERIT。

---

## [2] Pseudo-Labels as Rewards, Not Targets: Group-Relative Policy Optimization for Semi-Supervised ASR

**arXiv ID**：2610.32572 | **方向**：语音大模型

**作者**：Shashi Kumar, Yanis Labrak, Sergio Burdisso, Esaú Villatoro-Tello, Petr Motlicek, Kadri Hacioglu, Andreas Stolcke

**机构**：Idiap研究所（瑞士）、EPFL（瑞士）、布尔诺理工大学（捷克）、Uniphore（美国）

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32572 | **PDF**：https://arxiv.org/pdf/2610.32572.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
ASR在仅有未转录音频的域上适配时，传统伪标签自训练把教师转录当作SFT目标，学生几乎原样复刻教师错误。本文将同一伪标签改用为GRPO的WER奖励参考而非最大似然目标，借on-policy采样天然过滤标签噪声。银行域中GRPO相对SFT取得29.3%–56.2%的WER相对下降：Tiny标签下14.06% vs 32.11%，甚至优于Large-V3标签SFT的17.21%；GRPO仅复制27%的教师错误而SFT近100%。优势在4种Whisper规模、4个教师家族、3个会话域、4种语言上均成立。

### 🔧 技术方案

**问题背景：** 跨域ASR严重退化而目标域音频常无转录，自训练伪标签的交叉熵对每个token无条件最大化似然，教师错误变成监督目标并被深度网络记忆放大；已有工作（迭代伪标签、slimIPL、Kaizen、数据筛选）均只改标签不改目标函数，学生仍被迫复现教师输出。

**模型架构：** 学生为speech-LLM：冻结WavLM-Large编码器→可训练投影层（两层线性+ReLU，声学序列5倍下采样）→冻结Llama-3.2-1B-Instruct（LoRA r=16、α=32），仅训练投影层与LoRA，LibriSpeech 960h预调；教师用Whisper Tiny/Small/Medium/Large-V3及Qwen3-ASR-1.7B、Phi-4 Multimodal、Audio Flamingo 3生成伪标签。

**核心创新：** (1) 首次将伪标签从训练目标降级为奖励参考：对每条语音采样G=4个rollout，r=1−WER(rollout, PL)，组内标准化优势+裁剪代理目标+KL约束（β=0.04），标签集不动、只换目标函数，此前GRPO-for-ASR均需真值参考。(2) 给出on-policy噪声过滤机制：梯度仅作用于学生自采样序列，教师错词在rollout中仅以低概率p出现，全组一致的错误惩罚被组均值μ_r抵消，错误梯度质量从O(1)降至O(p)。(3) 发现并解释"SFT→GRPO反常有害"：SFT把错词放进策略支集（rollout命中率从10–30%升至>95%），组内奖励标准差从0.06–0.09塌缩至约0.01，摧毁GRPO校正所需的方差信号；仅当学生无法产出目标文字体系时SFT初始化才必要。

**训练策略：** AdamW+BF16，batch size 16，5 epochs，100 warmup步，梯度裁剪1.0；SFT学习率1e-4、GRPO 2e-5；GRPO超参G=4、温度0.8、rollout至多128新token、β=0.04、ε=0.2；单张H100 80GB；测试时贪心解码（beam=1）、256 token上限。

### 📊 实验结果
**数据集**：DefinedAI英语客服对话（银行训练约54h/测试6.55h；医疗11.51h/1.11h；保险27.60h/3.24h）、Common Voice 26印地/希伯来/越南/塞尔维亚语（各<6h训练）；Whisper伪标签WER从Tiny 26.42到Large-V3 14.61构成质量梯度

**主要指标**：
- 银行域WER：Large-V3标签下GRPO 12.17% vs SFT 17.21%；Tiny标签下14.06% vs 32.11%
- Tiny标签GRPO比Large-V3标签SFT优3.15点，换目标收益大于换教师
- 敏感度：伪标签WER每升1点，SFT学生WER平均升1.31点，GRPO仅升0.16点
- 教师错误复刻：SFT近100%，直接GRPO在11+错误分箱降至27%；插入错误15.17→1.87
- 跨教师：Qwen3 ASR标签GRPO 11.35 vs SFT 13.83；三其余家族GRPO均胜2.5–3.1点
- 金标签对照：SFT 10.27略优于GRPO 10.78，证实优势专属于噪声参考场景；医疗18.72→14.64、保险19.59→15.70

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：首次在无真值参考的半监督场景下系统研究GRPO，"伪标签当奖励不当目标"的重定位简洁有力，且用rollout重叠率与奖励方差塌缩两个诊断把机制讲透，SFT→GRPO反转的发现有直接实操价值。验证覆盖4教师规模×4家族、3域、4语言，充分性强。局限是学生配置单一、数据规模小、绝对性能仍逊金标准上界，且尚未结合迭代伪标签；属扎实的高完成度工作，接近顶会水准。

---

## [3] Why Full-Duplex Speech Models Collapse in Long Conversations

**arXiv ID**：2610.32349 | **方向**：语音大模型

**作者**：Yeonju Kim, Bella Godiva, Se Jin Park, Yong Man Ro

**机构**：韩国科学技术院（KAIST）Integrated Vision and Language Lab；庆熙大学

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32349 | **PDF**：https://arxiv.org/pdf/2610.32349.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工语音模型即使聆听也按帧（12.5Hz）每帧生成一个token，数分钟内即耗尽上下文，而现有基准只测单轮或少数轮的轮换、打断能力，长时程稳定性从未被检验。本文提出FD-LHB双赛道基准（CANDOR 40条超长对话受控重放至60分钟、与Gemini语音伙伴闭环交互至20分钟），评测5个全双工模型，发现所有模型均陷入重复、沉默、乱语。机制上诊断出初始化锚点驱逐与自强化重复两种成因，并用免训练的IAP+DRP干预，使Moshi乱语率100%降至0%、重复65%降至0%，PersonaPlex重复90%降至2.5%，且RTF 0.75实时可运行。

### 🔧 技术方案

**问题背景：** 全双工系统逐帧持续生成音频与文本token，静音与高频backchannel迅速填满上下文，且自身输出会反哺后续生成；现有Full-Duplex-Bench、FD-Bench等仅评估单轮或少轮的轮换、打断、重叠能力，增长式上下文与滑窗缓存两种设计能否稳定运行几十分钟从未被系统研究。

**模型架构：** 不引入新模型，而是构建"评测-诊断-干预"框架。FD-LHB-CANDOR从CANDOR语料裁剪后截取最长的40条对话（55.5至92.6分钟），取语音时长更多的说话人通道作固定16kHz单声道输入；FD-LHB-LLM用Gemini-2.5-Flash生成文本、facebook/mms-tts-eng VITS合成16kHz语音作自适应伙伴，围绕10个日常话题闭环对话。被测模型为Moshi、PersonaPlex（滑窗3000帧@12.5Hz，约4分钟首次填满窗口）与Raon-SpeechChat、BayLing-Duplex、Lychee-FD（增长上下文，约5、17.5、10.9分钟到达上限）。

**核心创新：** (1) FD-LHB以onset时刻刻画三种失效：重复为32词窗口内Seq-Rep-4≥0.30且连续两窗，沉默为1分钟bin少于3词且连续两bin，乱语由Gemini判分并结合预测熵，经8人盲听校验（与人类多数一致36/40、κ=0.80、精确率1.00），按Kaplan-Meier右删失估计无失效生存曲线。(2) 机制诊断：沉默/乱语的onset随窗口长度近似正比推迟，仅保留第1个KV条目即消除全部乱语，被钉锚点注意力占比从32%升至60%以上、充当注意力sink，重排位置索引无影响而缓存历史决定熵（新起0.05对长跑后4.2 nats），证明训练chunk从空cache带锚点开始、推理滑窗驱逐锚点造成训练-推理失配；插入上下文中不存在的词purple使复用率随插入次数升至28.4%，证明近期输出自强化重复。(3) 免训练干预：IAP永久钉住第1个KV条目，滑窗仅驱逐锚点之后的最旧条目、每步只把锚点位置+1并对存储的无RoPE键重施RoPE，开销O(1)；DRP仅改文本logits，对最近词表token按CTRL式惩罚并排除PAD/EPAD，再统一加offset保持词总概率不变以免加剧沉默，配合静默超30秒且用户安静时10秒内线性下调PAD logit的兜底。

**训练策略：** 无任何训练或微调，纯推理时干预；实验在NVIDIA RTX A6000上以bfloat16运行，Baseline与Ours使用完全相同的prompt、采样设置与输入，每条件40次运行（主实验seed 42，诊断实验seed 42-46）；IAP仅保留单锚点，DRP惩罚强度按Moshi与PersonaPlex分别调参，重复阈值0.20/0.30/0.40、窗口16/32/64词、单窗与双窗规则的敏感性分析均不改变基线与IAP+DRP的差距。

### 📊 实验结果
**数据集**：CANDOR 40条最长自然会话（裁剪后时长55.5至92.6分钟、每条最多评60分钟，16kHz单声道）+ 每模型40场20分钟闭环LLM交互（10个日常话题）

**主要指标**：
- CANDOR基线（重复/沉默/乱语发生率，40次/系统）：Moshi 65%/100%/100%，PersonaPlex 90%/85%/100%；加IAP+DRP后降至0%/7.5%/0%与2.5%/47.5%/0%
- 闭环交互赛道：基线乱语达97.5%-100%、长期沉默70%-87.5%，IAP+DRP将各项失效压至不超过10%
- 响应质量：两个滑窗基线约10分钟内Coherence/Context跌至1分最低，IAP+DRP全程60分钟稳定
- 增长上下文模型：Raon-SpeechChat约5分钟即达上下文上限，BayLing-Duplex 17.5分钟内重复/沉默/乱语55%/100%/90%，Lychee-FD 10.9分钟内重复/乱语37.5%/30%
- 关键对比：RTF 0.75（快于实时）vs StreamingLLM式基线1.03（跟不上实时）；McNemar六项对比全部显著；音频侧Whisper复核文本重复在音频中precision 1.00

**是否开源**：论文承诺发表时发布IAP+DRP实现、FD-LHB-LLM伙伴与指标代码及CANDOR对话ID清单，当前未公开（CANDOR音频需走研究申请通道）

### ⭐ 评分：8/10
评分理由：首个在几十分钟尺度系统评测全双工语音模型的基准，填补了长时程稳定性空白；诊断不止于现象描述，窗口扫参、单条目保留因果实验、注意力占比与词语插入构成完整因果链，说服力强；IAP+DRP免训练、零显存增量、可并入现有推理栈，工程价值突出。不足是验证限于英语与两个滑窗模型，PersonaPlex沉默率仍达47.5%，乱语依赖LLM裁判（召回0.83）略有低估，方法偏补丁而非根治。

---

## [4] NECTAR: Automatic Negative Clue Estimation via Centroid-Space Mapping for Target Speaker Extraction

**arXiv ID**：2610.32133 | **方向**：语音前端

**作者**：Hyungjun Yoo, Yongjoon Lee, Jung-Woo Choi

**机构**：韩国科学技术院（KAIST）电气工程学院、AI Systems 系

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32133 | **PDF**：https://arxiv.org/pdf/2610.32133.pdf | **代码**：https://github.com/Hyungjun-Yoo811/NECTAR | **Demo**：暂无

### 📌 简介
目标说话人提取（TSE）通常仅以目标注册语音作正线索条件化提取器；已知干扰者注册语音可作负线索抑制干扰，但推理时无法获得该语音。本文发现说话人嵌入在质心空间中满足"混合质心近似位于两组说话人质心中点"（c_mix≈½(c_s1+c_s2)），据此提出NECTAR：用质心空间映射器（CSM）仅凭一条混合与一条注册语音还原质心表示，由2ĉ_mix−ĉ_s1自动推出干扰者质心作负线索，与目标嵌入拼接送入BSRNN。在Libri2Mix上SI-SDRi达16.18 dB、提取准确率97.1%，超过全部对比系统，且几乎无额外计算开销。

### 🔧 技术方案

**问题背景：** 现有嵌入式TSE几乎只对目标说话人条件化，缺少"抑制谁"的显式负向信号；干扰者注册作负线索虽有效但推理时不可得。中点关系也不成立于单句嵌入（2e_mix−e_s1崩溃至2.36 dB），仅在质心级成立。

**模型架构：** 冻结预训练CAM++作说话人编码器（D=192）出帧级特征，BSRNN作提取主干；输入16 kHz、3 s，STFT用32 ms Hann窗、8 ms帧移。CSM由核3深度卷积、单层512维8头MHSA与注意力统计池化（ASP）构成，注册与混合支路共享参数；正线索P为目标注册嵌入，负线索N=2ĉ_mix−ĉ_s1，拼接成384维条件向量。

**核心创新：** (1) 实证质心中点关系：N=100质心下CAM++与ECAPA-TDNN余弦相似度均在α=0.5最大、MSE在β=0.5最小，偏差随N增大单调饱和、N=1时不可靠。(2) CSM把单段特征映射回质心空间：监督目标为说话人质心或c_s1+c_s2≈2c_mix，ℓ2平方误差损失，使干扰者质心偏差从N=1恢复到接近N=100参考，训练仅约1小时。(3) 免干扰注册的条件化：提取器训练用真实干扰注册嵌入作负线索、推理换成CSM估计质心，二者分开训练避免适配估计误差，隔离验证负线索增益。

**训练策略：** 提取器在LibriSpeech train-clean-100动态混音（SIR~U[−5,5] dB，注册取同人不同句），负SI-SDR损失，Adam、lr 1e-3指数衰减、batch 16、150 epochs；CSM用train-clean-100+Libri2Mix train-100，AdamW、lr 4e-5、batch 128、50 epochs；oracle质心由全部语句构建，混合质心参考同说话人对100条混合平均；含噪实验用mix_both训练集，单张B200。

### 📊 实验结果
**数据集**：Libri2Mix mix_clean/mix_both（16 kHz双人混合）、VCTK-2Mix（域外，剔除p280/p315）

**主要指标**：
- Libri2Mix mix_clean：SI-SDRi 16.18 dB、Acc. 97.1%、PESQ 2.89、ESTOI 0.88
- 关键对比：较最强基线Multi-Level BSRNN（15.91 dB）高0.27 dB，较仅目标嵌入基线（14.81 dB）高1.37 dB，优于混合嵌入线索（15.34 dB）
- 线索消融：单句嵌入近似2.36 dB、oracle质心近似16.62 dB、oracle干扰质心17.44 dB
- 域外VCTK-2Mix（未微调）：12.90→14.67 dB、Acc 92.0%→94.8%；含噪mix_both：11.38→12.02 dB、PESQ 1.85→1.90

**是否开源**：代码已开源 @ https://github.com/Hyungjun-Yoo811/NECTAR

### ⭐ 评分：8/10
评分理由：把负线索从依赖干扰者注册变为由混合与目标注册几何推导，洞察新鲜、开销可忽略，2.36 dB崩溃与16.62/17.44 dB oracle对照构成清晰因果证据，域外与含噪泛化扎实。不足在于中点关系仅有经验验证而无理论刻画，CSM与提取器非端到端联合训练，相对最强基线绝对增益0.27 dB偏小，且只覆盖双人语音混合、未验证非语音干扰。

---

## [5] Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes

**arXiv ID**：2610.32749 | **方向**：语音前端

**作者**：Wendi Sang, Kai Li, Yifan Li, Jianqiang Huang, Xiaolin Hu

**机构**：青海大学；清华大学计算机系/人工智能研究所/BNRist/IDG麦戈文脑科学研究院；CIBR

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32749 | **PDF**：https://arxiv.org/pdf/2610.32749.pdf | **代码**：https://cslikai.cn/Falcon/ | **Demo**：https://cslikai.cn/Falcon/

### 📌 简介
针对因果流式视听目标说话人提取（AVTSE）"基准失真+模型过重"的双重困境，论文发布RealSSA基准（RealSSA-Sim模拟套件+RealSSA-Real实拍评测集，支持1–5近场、10–15远场动态干扰，混响/环境/突发噪声联合变化），并提出轻量因果模型Falcon：单次编码-解码前向完成多尺度时频分离，配合编码器空间说话人对比损失抑制近场泄漏。Falcon在四个模拟基准上取得SOTA（RealSSA-Sim SI-SNRi 7.7 dB、VoxCeleb2-2Mix 10.5 dB），相比因果AV-TFGridNet参数量减少91.9%、计算量降20.2倍、GPU推理延迟降11.1倍。

### 🔧 技术方案

**问题背景：** 现有AVTSE基准把说话人数固定在2、按控制SNR混合，忽略真实场景的近/远场几何、混响与突发噪声，且缺独立实拍评测集；因果高性能架构的参数量与每帧计算量超边缘实时预算，轻量方法则靠反复调用小分离器补容量；SI-SNR损失不显式把估计推离近场干扰者，泄漏随近场说话人数增加而恶化。

**模型架构：** 视觉侧复用CTCNet的FRCNN骨干（唇语预训练、全程冻结）与SwiftNet VideoBlock（因果LSTM聚合后上采样至音频帧率），音频侧STFT实部/虚部/幅度三通道经2D卷积编码；核心为不对称U-Net分离器：4级编码器以步深向卷积同时减半时频分辨率，瓶颈与每个解码器级各置一个TFRB（频率双向LSTM→时间单向LSTM→块因果二维自注意力），GCI门控模块把全局上下文注入各skip，解码由粗到细恢复；掩码生成器做复数乘法掩蔽，经解码器与iSTFT重建目标语音，总参数仅0.5M。

**核心创新：** (1) 单趟多尺度分离器：把频率轴、时间轴、联合时频建模分配给不同分辨率的解码器级，一次编码-解码遍历即覆盖4个TF尺度，替代SwiftNet式多轮迭代复用；3级深度是视觉3帧缓冲lookahead预算下因果流式允许的上限。(2) 编码器空间说话人对比损失：复用分离器STFT编码器同时产生查询与参照（带同一房间响应的干净目标为正中、各近场干扰者为负，参照路径stop-gradient），池化头按频率平均、自适应时间池化，softmax温度聚焦最难负样本并线性退火；推理时整条分支丢弃、零成本，可移植到任何音频编码器AVTSE骨干。(3) RealSSA基准：四种场景将1–5近场/10–15远场干扰说话人数、几何、混响、WHAM!连续噪声与Hive语义化突发事件联合采样，gpuRIR镜像源仿真，另配8个真实环境iPhone实拍纯评测集。

**训练策略：** 总目标为SI-SNR重建损失加固定权重λ的对比损失；AdamW，验证损失平台期后学习率减半、超patience早停；RTX 3090训练；音频切2s片段@16kHz，视频25fps、96×96灰度口唇ROI；STFT Hann窗、3通道输入；视觉FRCNN冻结，对比温度线性退火；各基线在同一划分与优化协议下重训。

### 📊 实验结果
**数据集**：RealSSA-Sim（4场景、16kHz、三分割）与RealSSA-Real（8环境实拍、仅评测）；公开基准LRS2-2Mix、LRS3-2Mix、VoxCeleb2-2Mix（官方划分）

**主要指标**：
- RealSSA-Sim：SI-SNRi 7.7 dB / SDRi 8.2 dB，较AV-TFGridNet（7.6）高0.1 dB、较Swift-Net-12（7.3）高0.4 dB
- LRS3-2Mix：SI-SNRi 16.4 / SDRi 16.7 dB（超AV-Mossformer2）；VoxCeleb2-2Mix：10.5/11.8 dB，较Swift-Net-12提升1.1 dB
- RealSSA-Real：DNSMOS 3.276、NISQA 3.615、WER 32.74%（次优）、目标说话人相似度42.23%（最高）
- RealSSA-Sim WER 25.47%为所有提取系统最低（对照AV-TFGridNet 27.31%、ground truth 11.83%）
- 效率：0.5M参数/10.6G MACs/GPU延迟51.3ms，较AV-TFGridNet参数-91.9%、计算-20.2×、GPU延迟-11.1×；显存364.7MB全局最低
- 消融：对比损失使Falcon/Swift-Net-12/Dolphin分别+0.4/+0.2/+0.3 dB；分离器1→3级SI-SNRi +0.6 dB

**是否开源**：代码与Demo发布于项目页 https://cslikai.cn/Falcon/ ，声明将随数据集发布生成脚本与完整元数据

### ⭐ 评分：8/10
评分理由：同时补齐真实场景基准与边缘可部署因果模型两个空档，对比损失在3种骨干零推理成本增益、迁移性强，是干净实惠的贡献；0.5M参数在四基准达SOTA并保持十余倍效率优势，实用价值突出。不足：公开两说话人基准领先幅度偏小（0.1–1.1 dB），RealSSA-Real规模仅够揭示跨架构趋势，对比损失依赖仿真中带标注的近场干净语音且多通道阵列暂未使用。

---

## [6] DRAMA-Eval: A Benchmark for Context-Aware, Multi-Turn, Multi-Speaker Speech Generation

**arXiv ID**：2610.31796 | **方向**：语音大模型

**作者**：Jingbin Hu, Zihang Yang, Xiaoge Peng, Haoyu Zhang 等，Liumeng Xue, Lei Xie

**机构**：西北工业大学ASLP@NPU、深圳皮美科技、南京大学ASLP@NJU、玉兔智能

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.31796 | **PDF**：https://arxiv.org/pdf/2610.31796.pdf | **代码**：https://github.com/ASLP-lab/DRAMA-Eval | **Demo**：https://ASLP-lab.github.io/DRAMA-Eval-Demo

### 📌 简介
语音生成正转向上下文感知、多轮、多说话人合成，但现有基准将指令跟随、对话生成与音视频模型音频分支的评估彼此割裂，无法联合度量场景级能力。本文提出DRAMA-Eval：以结构化脚本（场景上下文+角色设定+轮级指令）为条件，提供客观、局部、全局三层统一评测，并用LALM裁判对照真实音频做AB偏好判分，以平局调整胜率计分。发布1038例、12.5小时中英双语人工质检测试集。评测12个开源/商业系统显示：最强SeedAudio局部B3达64.2、全局C1-C3为67.4/73.2/75.7，而Qwen3-TTS B3高至60.6但C2仅28.2，暴露长程说话人一致性与隐式指令跟随短板。

### 🔧 技术方案

**问题背景：** 指令可控模型面向孤立句，多轮对话模型仅以裸转录+说话人ID为条件，音视频模型音频分支评估停留在音质、可懂度等表面属性；上下文建模、指令执行与多说话人长程一致性从未被联合考察。

**模型架构：** DRAMA-Eval为基准框架而非生成模型，含三模块：(1)任务定义：给定结构化脚本（场景上下文、角色描述、各轮说话人/文本/局部指令）与可选参考音频，输出整场场景音频；(2)数据管线：真实播客/影视音频经Gemini 2.5 Pro段级表达标注、DeepSeek-v4.1-Flash改写为三层脚本、人工质检；(3)评测体系：客观层A1文本忠实度（Qwen3-0.6B-ASR算CER/WER）、A2轮间一致性（声纹嵌入，沿用Seed-TTS-Eval），局部层B1-B3与全局层C1-C3共六维由Gemini 3.8 Flash裁判。

**核心创新：** (1)首个以完整场景为评估单元、统一四层能力的协议：候选与同场景真实音频匿名AB对比，胜率=（胜+0.5×平局）/总数，50即与真人持平。(2)真实素材驱动：局部指令直接源自段级真实表演标注，脚本覆盖情绪递进/对比/复杂情绪等场景，指令与可验收的真实演绎挂钩。(3)四类推理协议：对话TTS、语音设计、语音控制、上下文感知多Speaker各自按接口生成，交叉分析可精确归因"音色保持≠表现力、局部可控≠场景连贯"。

**训练策略：** 本文不训练生成模型，评测协议即核心：每对音频正反AB双序各判一次、两轮均被偏好才计胜以消位置偏置，三次独立评估取均值；测试集1038例（中537/英501）、7530轮，平均案例43.36秒、7.25轮，1-4说话人、2-20轮，多说话人占65.6%。

### 📊 实验结果
**数据集**：1038例、12.50小时中英真实场景音频，Normal/Escalation/Contrast/Rich Emotions四类528/149/162/199例

**主要指标**：
- 客观：SeedAudio中文CER 2.58%、FireRedTTS3英文WER 3.97%最优；MOSS-TTSD一致性0.78但中文B3仅35.9，音色保持≠表现力
- 局部：SeedAudio中英B1 62.2/56.5、B3 64.2/57.0最高，StepAudio 3 Gen中文B2 58.3最优
- 全局：SeedAudio中文C1/C2/C3 67.4/73.2/75.7；Qwen3-TTS B3达60.6而C2/C3仅28.2/27.7，句级成功≠场景连贯
- 裁判与人类共识一致率65.91%-81.58%；加全局上下文后SeedAudio中文C3由64.4升至75.7、英文由45.9升至55.7

**是否开源**：代码开源 @ https://github.com/ASLP-lab/DRAMA-Eval，数据集与结果见HuggingFace（含Demo页）

### ⭐ 评分：8/10
评分理由：直面剧本化语音生成评测的真实空白，对真实音频的AB胜率协议设计干净，四类推理协议的交叉分析定位出长程一致性与隐式指令跟随两大系统性短板，并有人工一致性验证；数据代码全量开放，复现门槛低。局限在仅中英双语、裁判依赖闭源LALM、情绪与说话人分布失衡、跨类别条件不同削弱可比性。创新性高、实验充分，可直接用作工业级对话TTS回归基准。

---

## [7] X-Dubbing: Speech-to-Speech Translation under Temporal and Visual Constraints

**arXiv ID**：2610.32042 | **方向**：语音大模型

**作者**：Jeongsoo Choi, Ji-Hoon Kim, Junseok Ahn, Joon Son Chung

**机构**：KAIST, Chung-Ang University

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32042 | **PDF**：https://arxiv.org/pdf/2610.32042.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
X-Dubbing针对配音译文难以自然贴合源视频时间与口型约束的问题，将其建模为时间感知S2TT与视频感知TTS的协同任务：Dubbing Translator（Qwen2.5-Omni-3B）基于VAD时序预算生成含<pause>标记的字幕，Voice Actor（X-Voice流匹配DiT）在暂停与视觉条件下合成同步语音，并以合成语音作端到端反馈对翻译器做DPO，无需配对配音数据。mTEDx法→英取得ASR-BLEU 42.34、Pause IoU 0.551、LSE-C 2.58、人评音视对应MOS 4.01/5，超越全部基线。

### 🔧 技术方案

**问题背景：** 视觉盲的定时翻译器局部对齐差、语速失配，视频感知TTS用无约束译文硬凑时长则扭曲语速；端到端S2ST不建模视觉约束，且配对配音语料稀缺无法微调适配。

**模型架构：** 双模块共享语言无关时序预算。Translator经Qwen2.5-Omni-3B音频塔编码源语音，读取VAD时序预算，输出插入<pause>的字幕；Voice Actor基于X-Voice（flow-matching DiT），字幕驱动、源语音作音色参考，输出长度锁定源时长的mel谱。暂停二值帧与SyncNet视觉帧嵌入重采样至mel帧率后，经FiLM在DiT输入与各block逐帧调制，文本侧注入<pause>嵌入。

**核心创新：** (1) 等时归一化投影INP：按语言音节率归一估计目标句预期时长D̂t=Ds·(Nt·r̄t)/(Ns·r̄s)，据此伸缩源时序预算并在最近词边界插入<pause>，从普通平行语料构造定时监督，绕开配对配音数据。(2) 暂停+视觉双重帧条件：训练用目标语音VAD序列、推理改源语音传递暂停结构，条件dropout 0.5缓解单语训练-跨语推理失配。(3) 端到端反馈DPO：G个候选由冻结Voice Actor以N随机种子渲染，按音节率、COMET-Kiwi、LSE-C/LSE-D平均、暂停数一致四标准Pareto支配构造偏好对，使翻译器学会选择易配音译文。

**训练策略：** Translator SFT用mTEDx法→英11,092条/14.9h；Voice Actor用LRS3英语音视频95,474条/约200h，法语参考音色由X-Voice合成增强；各模型LoRA rank=8、alpha=32，Translator音频投影与Actor条件模块全参训练；DPO用7,752对且仅更新LoRA与投影；学习率与轮数未披露。

### 📊 实验结果
**数据集**：mTEDx法→英测试集（固定源视频，片段2-10s）

**主要指标**：
- ASR-BLEU 42.34、chrF++ 64.06，较最强基线SeamlessExpressive高3.90/3.79
- SpkSim 0.497（较Hibiki 0.358提升0.139）；UTMOS 3.748接近最优Hibiki 3.864
- 时序对齐：SyllRate ρ=0.617、Pause IoU=0.551、SLC@0.2=97.1%、SLC@0.4=100.0%
- 唇同步：LSE-C 2.58、LSE-D 11.30，最优基线Hibiki为1.48、12.62
- 人评MOS（15评委×12片段）：音视对应4.01±0.12、自然度3.99±0.13，显著高于Cascaded的3.13/3.54
- 消融：去INP致SyllRate ρ降0.079；去帧级FiLM致Pause IoU 0.563→0.386、LSE-C 2.56→1.91

**是否开源**：正文未提供代码或Demo仓库链接，暂未开源

### ⭐ 评分：8/10
评分理由：首次将翻译定时约束与合成视听约束在同一时序预算下显式耦合，INP与语音反馈DPO摆脱了配对配音数据依赖，范式新颖可复用；客观指标、人评与双侧消融充分，唇同步和时序大幅领先主流基线。不足是仅验证法→英单人独白，训练超参披露不全，UTMOS未全面占优。

---

## [8] Concentrated Causal Influence, Distributed Diagnostic Information: Cognitive Impairment Decisions in Large Audio-Language Models

**arXiv ID**：2610.32061 | **方向**：语音大模型

**作者**：Xiutian Zhao, Luqi Sun, Björn Schuller, Berrak Sisman

**机构**：Center for Language and Speech Processing (CLSP), Johns Hopkins University；GLAM, Imperial College London

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32061 | **PDF**：https://arxiv.org/pdf/2610.32061.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
大型音频语言模型（LALM）可从语音评估认知障碍（CI），但其答案既不揭示哪些内部组件控制决策，也不揭示表征中诊断信息的分布。本文提出CI对比神经元（CICN）：在解码器MLP中选取模型自信正确分类的健康（NC）与受损（CI）录音间正激活频率差异最大的前0.5%神经元，并在8个开源LALM、Pitt与PROCESS-2两语料上对尺寸/层级匹配随机掩码和活动匹配对照做消融因果检验。5个合格模型中3个出现类定向大幅预测偏移：Kimi-Audio AT-chat NC掩码消融翻转88%基线正确NC样本（随机掩码16%）。CICN监督读出AUC达0.92–0.97，高于模型直接回答的0.67–0.84，但随机/全神经元读出相当，揭示因果控制集中而诊断信息广泛分布。

### 🔧 技术方案

**问题背景：** CI检测的可解释性研究停留在输入层（特征重要性、注意力、SHAP），只能说明预测与哪些输入相关，无法指出产生决策的内部计算；尚无工作在直接处理语音的模型内对CI决策做因果神经元定位，也未检验该控制是否跨语音与文字通道共享。

**模型架构：** 8个开源LALM（Qwen2.5-Omni-7B、Qwen3-Omni-30B、Kimi-Audio、MiniCPM-o-4.5、Gemma-4-12B、Audio-Flamingo-Next、Voxtral-Small-24B、MOSS-Audio-8B），统一16kHz单声道输入；Cookie Theft图片描述经固定二选一提示，由首步选项字母logits重归一化取argmax判NC/CI，双选项顺序运行以抵消位置偏好；设仅文字T、仅语音A、联合AT、带标注联合AT-chat四条件；钩取门控MLP逐层激活，MoE将每专家单元视为神经元（Qwen3-Omni共471.9万神经元），掩码取全局排名前0.5%。

**核心创新：** (1) 首个LALM CI决策的因果神经元级分析：以ConAct对比激活边际选择CICN，对每个掩码用20组尺寸/层级匹配随机掩码与逐层激活统计匹配集双重零假设检验，双共主指标做交并检验并以BH-FDR控多重性。(2) 证明控制跨通道、跨语料可迁移：语音识别掩码零重选也显著支配仅文字决策（9/9迁移过检），Pitt四个主掩码中3个在远程收集的PROCESS-2保持特异、并泛化至留出MCI诊断。(3) 将干预分解为决策偏置偏移与诊断判别变化：单一加性offset解释61–91%的逐项log-odds均方变化、排序基本保持；再以岭读出证明诊断信息在CICN之外广域可恢复，二者构成分离。

**训练策略：** 零样本确定性推理，不训练任何模型：贪心解码、首步logits先于处理器读取、A100单卡批量1、固定种子并验证二次运行logits逐位一致；识别池要求双顺序正确且margin达阈，每类16–86条均衡抽取；读出为类均衡岭回归，预算8–2048单元对比层匹配随机神经元。

### 📊 实验结果
**数据集**：DementiaBank Pitt Cookie Theft（识别297条：152 NC/145 CI；评估107条）；PROCESS-2 99条评估+136条留出MCI

**主要指标**：
- 消融显著性：24掩码7个双指标过检（q<0.05），四个主掩码逐项log-odds偏移约±0.16–0.26，2000次录音bootstrap中4/4主掩码100%超出全部随机掩码
- 翻转率：Kimi-Audio AT-chat NC掩码翻转88%基线正确NC样本，随机掩码均值16%
- 偏置vs判别：79–100%录音按预测方向移动（随机37–60%），offset份额61–91%，消融前后log-odds Spearman相关0.89–0.98
- 迁移：T条件9/9过检；PROCESS-2四主掩码3个过检
- 读出AUC：CICN 0.92–0.97，模型直接回答0.67–0.84，TF-IDF词汇基线0.91；8单元时top-CICN较层匹配随机+0.118 AUC
- 关键对比：因果控制仅见于5合格模型中的3个

**是否开源**：代码与Demo未发布；所用模型checkpoint均在Hugging Face公开，语料需DementiaBank/PROCESS授权

### ⭐ 评分：8/10
评分理由：首次对LALM诊断决策做严格因果神经元定位，匹配双重零假设、IUT+BH-FDR与bootstrap稳健性检验设计扎实，"集中控制/分布式信息"的分离结论对临床语音模型审计具方法论价值。不足在于可控效应仅见于5个合格模型中的3个，干预限于解码器MLP，数据仅英文Cookie Theft且未开源代码，工程可复用性有限。

---

## [9] SURE-Tagger: Structured Speech Representations for Compositional Evaluation and Targeted Data Selection

**arXiv ID**：2610.32198 | **方向**：语音大模型

**作者**：Jing Peng, Huifei Wang, Weihan Chen, Shuo Gao, Bicheng Zhang, Junhao Du, Hanqi Li, Chaolei Liu, Wen Wen, Tao Liu, Xu Li, Yu Xi, Shuai Wang, Kai Yu

**机构**：上海交通大学 X-LANCE 实验室、AISpeech（思必驰）、深圳大学、南京大学等

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32198 | **PDF**：https://arxiv.org/pdf/2610.32198.pdf | **代码**：暂无（承诺录用后开源） | **Demo**：暂无

### 📌 简介
针对自由文本语音标注属性覆盖不一致、"遗漏"无法区分缺失/忽视/不确定的问题，提出SURE-Tagger：按L1词内容、L2说话人、L3时间结构、L4副语言、L5声景五层，为每条录音构造"显式属性值+证据不足null+补充描述"的半结构化表示，由LLM整合专家感知模型观测生成。配套Tag-Bench（650条真实+500条智能体合成场景，29轴评测）。SURE-Tagger在25/29（真实）、24/29（合成）维度最高，综合77.28%（基线60.93/58.20）；1小时微调预算下按条件误差选数据，使Qwen3-ASR-1.7B整体错误率相对下降14.3%。

### 🔧 技术方案

**问题背景：** 自由caption在录音间属性覆盖与措辞不一，省略属性不可解释为确认缺失，难以用作一致的样本级属性记录；数据集级聚合分数亦会掩盖多条件并发下的模型短板，跨数据集联合条件评估与定向改进缺乏共同表示。

**模型架构：** 免训练流水线。感知层由FireRedLID（语种）、按语种分流的中英MOSS-Diarize/其他DiariZen（说话人分离）、FireRedAED（声学事件）与ASR输出带来源的属性观测；经ASR文本做语言一致性复核；最后DeepSeek-V4-Pro单次调用在schema约束下产出五层显式属性＋描述层D。

**核心创新：** (1) 半结构化表示：显式属性区分"确认值（含确认缺席）"与null"证据不足"，保留开放式补充描述，使跨数据集联合条件查询语义明确；去null后仍居首。(2) 证据接地构造：专家观测不被直接当作schema答案，而由LLM按字段定义与约束调和冲突、不确定时弃权；语种轴因该整合从88.90%升至98.62%。(3) 表示驱动的闭环下游：属性谓词合取构造跨库子集；用23维混合类型属性向量做k-medoids聚类得6个冻结声况簇，簇级误差估计对10,000条候选池加权采样，固定1小时预算内实现诊断→选数→微调闭环。

**训练策略：** SURE-Tagger本身免训练；下游用约1小时选定音频微调Qwen3-ASR-1.7B，候选池与1,000条评测集（500英/400中/100泰）不相交，Pool与Eval两种引导策略各跑3个采样种子，按语言以Open-Bench协议计WER/CER。

### 📊 实验结果
**数据集**：Tag-Bench＝650条AMI/FLEURS/LibriSpeech/DESED/FSD50K真实录音＋500条合成场景（11交互模式×3语速×3档SNR×2音乐×2混响基准构型）；诊断/选数用10库各100条与10,000条候选池。

**主要指标**：
- Tag-Bench综合：真实76.28%（Omni-Flash 62.79、Captioner 51.23）、合成78.88%、综合77.28%；结构化19轴综合83.19%
- 弃权拆解：SURE显式null率仅5.6%，Captioner达78.3%；null计零时Captioner崩至12.83%，SURE仅小降，非弃权刷分
- 人类偏好：200条层级判定159票选SURE（79.5%，L2层95%）；重合成试听偏好59.1%对Captioner 27.3%
- 条件化ASR：Qwen3-ASR-1.7B在C03长干净语音5.12% vs C01短低噪21.53%；短语音47.6% WER叠加高非语音比后升至83.8%
- 聚类解释力：标签簇η²=0.348 vs 随机0.005
- 关键对比：SURE选数将总体错误率由5.50%降14.3%相对，同预算下caption引导与随机采样反升错误

**是否开源**：暂无即刻可下载地址；论文承诺录用后开源代码、提示词、评测脚本与派生标注。

### ⭐ 评分：8/10
评分理由：以"显式属性＋null弃权＋补充描述"直击caption式标注不可比与不可联合查询的真痛点，基准合成可控场景并经二次评审、人类偏好与弃权拆解多重验证；首次贯通富标注→跨库组合评估→1小时预算定向选数闭环，实用价值明确。不足在于描述层优势有限、尾部小簇不稳定、依赖多个外部模型致复现成本高，且代码与基准尚未落地公开。

---

## [10] Uni-Stream: A Unified Streaming Speech Language Model for Speech Synthesis and Recognition

**arXiv ID**：2610.32187 | **方向**：语音大模型

**作者**：Xuan Shi, Chang Zeng, Tiantian Feng, Ye Zhang, Jun Liu, Shih-Heng Wang, Lie Lu, Shrikanth Narayanan

**机构**：南加州大学（通讯）、日本国立情报学研究所、麻省理工学院、Dolby Laboratories

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32187 | **PDF**：https://arxiv.org/pdf/2610.32187.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出Uni-Stream，首个在单一共享权重decoder-only主干上同时支持流式语音识别与流式语音合成的语音大模型。方法基于VibeVoice-1.5B家族，采用词级时间对齐的语音-文本交错序列与两阶段训练（任务专属流式适应+合成锚定/识别蒸馏联合训练），并构建约4万小时带词级时间戳的Emilia-EN标注管线。最终ASR WER为3.63%/10.74%（LibriSpeech clean/other），TTS WER 3.20%、SIM 0.714，与专用流式模型相当，词发射延迟仅0.66秒、首包延迟129毫秒。

### 🔧 技术方案

**问题背景：** 已有统一语音模型多为离线，流式系统则按任务分开训练；仅Speech-T以transducer做到双向流式但局限于单说话人。此前无单一decoder-only主干能同时流式运行ASR与TTS且不牺牲任务性能。

**模型架构：** 1.5B参数VibeVoice-TTS decoder-only主干，复用其声学+语义tokenizer（24kHz→7.5 latent帧/秒），输出双头：文本头（ASR自回归转写）与diffusion头（TTS预测下一语音latent）。序列以任务token开头接交错块：ASR每步4帧、前瞻3帧；TTS时间对齐每步2词、前瞻2词，语音块边界由词尾时间戳决定、推理时预测。

**核心创新：** (1) 选定时间对齐交错：每段在所属词读完处给局部停止监督，避免固定比例格式仅句级停止信号导致的跑续多读（39条WER>50%的固定比例输出中29条为续读），Stage I TTS WER 3.54%比7.67%。(2) 两阶段训练与双教师蒸馏：Stage I将TTS/ASR分别适应为流式教师并冻结；Stage II从TTS教师初始化联合训练，在SFT损失上叠加合成锚定（扩散速度MSE+两token KL停止蒸馏）保住TTS，ASR教师next-token KL蒸馏加速识别学习。(3) 数据管线：三ASR假设ROVER投票修订转录、三强制对齐器误差倒数加权合并词边界（TIMIT平均误差24.4ms），保留40k小时并承诺发布标注。

**训练策略：** Stage I于10k小时微调（TTS 80k步、ASR 20k步）；Stage II共300k步，TTS用40k小时Emilia、ASR用38k小时混合语料并按语音时长平衡；AdamW lr 1e-5 cosine衰减、tokenizer冻结；prompt同人3-10秒、文本/音色drop 0.2/0.1；推理10扩散步、CFG 3.0/4.0。

### 📊 实验结果
**数据集**：LibriSpeech test-clean/other与Seed-TTS-Eval English（1088条）；训练为Emilia-EN、GigaSpeech XL、LibriSpeech train-960。

**主要指标**：
- ASR：WER 3.63%（clean）/10.74%（other），词发射延迟0.66s、RTF 0.17（较原VibeVoice-ASR-Streaming延迟1.68s大幅下降）
- TTS：WER 3.20%、SIM 0.714、UTMOS 3.994，首包延迟129ms、RTF 0.64
- 关键对比：与专用模型配对bootstrap差异不显著（ASR WER +0.13pt、TTS WER -0.33pt）；TTS教师较仅SFT在300k步将TTS WER从4.35%降至3.20%；仍逊于Kyutai DSM-TTS（WER 1.58%）等大数据专用系统

**是否开源**：暂无（仅承诺发布Emilia-EN投票转录及词级时间戳，模型与训练代码未开源）

### ⭐ 评分：7/10
评分理由：填补"单一decoder-only主干+双向流式ASR/TTS"空白，时间对齐交错与停止监督分析具方法论启发，双教师消融配配对置信区间论证严谨，4万小时词级时间戳释出有社区价值。局限在依托VibeVoice既有能力、仅英语验证，绝对性能不及大数据专用系统，属扎实的工程整合与实证贡献而非范式突破。

---

## [11] DIAL-S2ST: Learning Latency Control for Simultaneous Speech-to-Speech Translation

**arXiv ID**：2610.32214 | **方向**：语音大模型

**作者**：Jeongsoo Choi, Junseok Ahn, Joon Son Chung

**机构**：KAIST

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32214 | **PDF**：https://arxiv.org/pdf/2610.32214.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
Hibiki等多流式同传语音到语音翻译（SimulS2ST）模型把"何时说"与"说什么"耦合进并行token流，推理时无可独立调节的读写策略，直接偏置logits会显著损伤质量。本文提出DIAL-S2ST后训练方法：以冻结预训练模型加源音频超前（lookahead）作教师，对LoRA学生做在线自蒸馏学得更早释出，并将LoRA缩放系数与lookahead绑定，实现单适配器推理时连续延迟控制。仅用约10小时法语源语音、500步训练，在CVSS Fr→En上LAAL 2.16s时达34.4 ASR-BLEU，质量-延迟权衡明显优于StreamSpeech、Seamless及logit偏置基线。

### 🔧 技术方案

**问题背景：** SimulS2ST需持续权衡"多听源语音"与"早出译文"，质量-延迟平衡应在推理时可调。StreamSpeech的chunk大小与Seamless的发射阈值是显式控制机制，但Hibiki等多流模型把发射时机由训练期学到的token流行为决定，训练后无独立读写策略；仅偏置PAD/BOS logits会致质量骤降。

**模型架构：** 基于Hibiki式decoder-only多流框架：因果Mimi codec将源/目标语音编码为12.5 Hz帧率并行token流；Temporal Transformer每帧预测目标文本token W_t，其输出与W_t共同条件Depth Transformer自回归生成各codebook目标语音（声学码本延后2帧）；文本流按词级对齐用PAD填充。冻结基座权重，仅向Temporal Transformer全部线性层注入rank-16 LoRA（约16M可训练参数），更新量按α缩放。

**核心创新：** (1) Lookahead在线自蒸馏：冻结模型以多看k秒源语音为教师，学生仅用源数据采文本+语音轨迹并在自身前缀上匹配教师的文本forward KL；教师已提前释出学生仍在等待的词，从而无需配对译文或奖励即获得"更早发射"的监督信号。(2) 大文本KL掩码与语音锚定：对超过阈值c=10 nats的文本KL置零保留可靠监督；同时将学生语音分布向无lookahead教师按codebook蒸馏（语义项全权重、声学项λ=0.02），防止文本移位破坏音色与流畅度。(3) 单适配器连续延迟控制：训练采样k~U[0, 2s]并配α=k/k_max绑定缩放系数与lookahead深度，推理仅调α即可平滑改变发射时机，α=0精确恢复原预训练模型。

**训练策略：** 总损失ℓ_t=1[d≤c]·d^txt+d^(1)+λΣ_{q≥2}d^(q)；FLEURS域外约10小时法语语音，500步、每步16 rollout，AdamW、lr 5×10^-5线性warm-up；三随机种子适配器经model soup平均。reverse KL替代forward KL会崩溃为静默。

### 📊 实验结果
**数据集**：CVSS Fr→En测试集（源自CoVoST 2/Common Voice）；后训练用约10小时FLEURS法语语音，另对照域内CVSS训练子集

**主要指标**：
- ASR-BLEU：34.4（α=0.5操作点），LAAL 2.16s、End Offset 1.73s
- 音色/自然度：Speaker Sim 0.391、UTMOS 3.41
- 关键对比（LAAL 1.8/2.3/2.8s对齐延迟的ASR-BLEU）：Ours 32.5/34.8/35.6 vs 移位rollout自训练SFT 32.0/33.2/34.3、off-policy蒸馏 31.1/34.6/35.5，最低延迟点高1.4 BLEU
- 组件消融：去文本KL掩码降至33.1；去speech KL BLEU 32.7且音色相似跌至0.337、UTMOS 3.33
- 对比基线：StreamSpeech与Seamless同等延迟下质量明显低于DIAL-S2ST；Hibiki PAD logit偏置降延迟但质量骤降

**是否开源**：暂无（论文未提供代码或模型发布链接）

### ⭐ 评分：7/10
评分理由：首次在无显式读写策略的多流SimulS2ST上把推理时可调延迟学进单一LoRA缩放系数，lookahead自蒸馏+KL掩码设计优雅，且仅需10小时无配对源音频、500步即超过SFT与在线偏置方案，实用性强。消融覆盖on/off-policy、各损失项与域内外数据，比较充分。不足是仅Fr→En单语对、延迟随语句波动且α-延迟关系纯经验、无人工评估，泛化性待验证。

---

## [12] MG-REPA: Multi-Granularity Representation Alignment for Generative Target Speaker Extraction

**arXiv ID**：2610.32161 | **方向**：语音前端

**作者**：Dohwan Kim, Jung-Woo Choi

**机构**：韩国科学技术院（KAIST）电气工程学院与AI系统系

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32161 | **PDF**：https://arxiv.org/pdf/2610.32161.pdf | **代码**：https://github.com/rlaehghks5/MG-REPA | **Demo**：暂无

### 📌 简介
生成式目标说话人提取（TSE）感知质量高，但MeanFlow-TSE等一步模型仍需约2000 epochs才收敛；现有语音域REPA仅在帧级或话语级单一粒度对齐。本文提出MG-REPA：在DiT中间层并联双分支，帧级用时间归一化（TN）后的WavLM特征对齐、话语级用CAM++说话人嵌入对齐。Libri2Mix上用3.0×/2.1×更少的epoch达到基线OVRL/PESQ水平，750 epochs即在侵入式指标追平2000 epochs基线（PESQ 3.29、SI-SDR 18.88 dB），非侵入式指标全面超出。

### 🔧 技术方案

**问题背景：** 判别式TSE保真但易生伪影、泛化差；扩散/流式TSE将推理压至一步却训练收敛极慢。已有语音REPA（A-DMA、ImmersiveTTS、AG-REPA）即便多教师仍仅单一粒度对齐，另一粒度无监督。

**模型架构：** 底座为AD-FlowTSE/MeanFlow-TSE共享的uDiT速度估计器（8编码+1bottleneck+8解码块，16头、hidden 1024），输入STFT频谱（窗510/hop128），token即STFT帧。两分支接于bottleneck（l=9）：帧级MLP adapter+平均池化降采样至教师帧率，与WavLM Large第24层特征逐帧余弦对齐；话语级GLU门控adapter+均值池化+线性投影，与CAM++说话人嵌入余弦对齐。损失L=L_gen+0.5·L_frame+0.5·L_utt。

**核心创新：** (1) 帧级教师管音素内容、话语级管全局音色，双分支各配独立adapter，监督互补而非重复，区别于AG-REPA等单粒度方案。(2) 对帧级教师目标做通道级时间归一化TN，借鉴VC中instance-norm去说话人思想剥离全局统计量，消融显示加TN后多数指标再升。(3) 对齐损失不依赖先验/端点/回归目标，可挂接FM、α-Flow等任意生成目标；推理时adapter与教师全部丢弃，开销与原骨干相同。

**训练策略：** Libri2Mix train-100+train-360合训，6秒16kHz段（3秒enrollment+3秒混合）；AdamW（wd 0.01，lr 1e-4余弦退火，Tmax=50、下限1e-5），5 warm-up epochs，梯度裁剪0.5，batch 256，16bit混合精度+DDP；主实验750e，消融150e。

### 📊 实验结果
**数据集**：Libri2Mix（分Clean/Noisy测试集，16 kHz）

**主要指标**：
- Clean 750e：PESQ 3.29、SI-SDR 18.88 dB、ESTOI 0.93，均超2000e的MeanFlow-TSE（3.26/18.80/0.93）
- Noisy 750e：PESQ 2.22、OVRL 3.20、DNSMOS 3.60，OVRL/DNSMOS较基线+0.03/+0.05，仅SI-SDR 12.38落后0.47 dB
- 收敛加速：同等重训基线下，OVRL于250 epochs即达其750 epochs水平（3.0×加速），PESQ于350 epochs达标（2.1×）
- 消融150e：无对齐PESQ 1.74→MG-REPA+TN 1.99，SI-SDR 10.34→11.60 dB，确认双粒度+TN最优

**是否开源**：代码已开源 @ https://github.com/rlaehghks5/MG-REPA

### ⭐ 评分：7/10
评分理由：把REPA引入生成式TSE的切入点准确——TSE恰需内容与说话人两类互补监督，TN解耦与粒度消融使机理主张证据充分，3×收敛加速对反复训模的TSE研究有直接实用价值。不足在于终态质量增益较小（+0.03量级）、仅Libri2Mix单数据集验证、尚未实测其它backbone以证明通用性，投稿形态为短文，实验广度有提升空间。

---

## [13] Noisy Target Training Meets Drifting for Weakly-Supervised Speech Enhancement

**arXiv ID**：2610.32870 | **方向**：语音前端

**作者**：Yoshiki Masuyama, Dominik Klement, Christoph Boeddeker, Julius Richter, Kohei Saijo, Gordon Wichern, Takahiro Edo, Jonathan Le Roux

**机构**：Mitsubishi Electric Research Laboratories（MERL）、捷克布尔诺理工大学 Speech@FIT、三菱电机

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32870 | **PDF**：https://arxiv.org/pdf/2610.32870.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对弱监督语音增强中 NyTT 因训练目标含噪而残留噪声的问题，本文引入基于无配对干净语音的 Sinkhorn drifting 损失，在语音质量评估（SQA）模型 UrgentMOS 的潜空间中把增强分布推向干净分布，同时保留 NyTT 的波形级保真监督。在 VoiceBank-DEMAND 上，方法在不损失 SI-SDR（18.58 dB）的前提下将 PESQ/DNSMOS/UTMOS 从 2.63/3.53/3.81 提升至 2.69/3.59/3.93；在 CHiME-3 真实录音上 DNSMOS 由 3.42 升至 3.59、UTMOS 由 2.60 升至 2.82。

### 🔧 技术方案

**问题背景：** 标准监督训练（CTT）依赖人工加噪合成配对数据，与真实录音存在声学域不匹配；NyTT 用观测含噪信号本身作目标从而可用真实数据，但其最优解理论上必然残留噪声，mean-teacher 等变体（NyTT+）也仍未显式促使增强语音分布匹配干净语音分布。

**模型架构：** 增强模型为卷积 DPRNN（约 1.5M 参数）：3 层 Conv2D 编码器、2 个时频 DPRNN 块、CBAM 注意力块和 3 层 ConvTrans2D 解码器，输入复数 STFT 的实部/虚部/幅值（510 点 DFT、128 帧移），输出复数时频掩码。漂移场在冻结的 UrgentMOS 话语级嵌入（维度 768）中由吸引项（拉向干净特征）与排斥项（推离当前增强分布）构成。

**核心创新：** (1) 首次将 drifting 模型接入 NyTT，总目标为 NyTT+（EMA 教师伪目标+负 SNR）加 λ=0.5 加权的无配对 Sinkhorn 漂移损失，波形级保真与分布级匹配互补，干净语音独立于含噪观测采样，完整保留弱监督属性。(2) 用 Sinkhorn 散度诱导的漂移场替代 mean-shift：mini-batch 经验测度上以二次代价做熵正则最优传输，Sinkhorn 迭代 10 次得到全局平衡传输权重，理论上保证零漂移等价于两分布精确匹配。(3) 改用 SQA 模型潜空间而非 SSL 帧级特征做分布匹配：无配对条件下按音素对齐不合理，而 SQA 嵌入距离直接对应感知自然度，隐式提升质量分且保留干净语音多样性。

**训练策略：** VBDM 28 说话人训练集上以 AdamW 训练至多 200 epochs，lr warmup 1000 步至 1e-3，2 秒切块，batch 32；额外噪声取自 DEMAND 与 CHiME-3，重标定使相对观测 SNR 服从 U(-5,5) dB；EMA 衰减 0.8^(1/Q)；漂移场按 τ∈{0.1,0.5,2.0} 平均。CHiME-3 以仅负 SNR 预训练的 CTT 模型初始化微调至多 100 epochs，无配对干净语音用 EARS 数据集。

### 📊 实验结果
**数据集**：VoiceBank-DEMAND（28 说话人子集、16 kHz）；CHiME-3 真实五通道录音（取第 5 通道，Whisper Large v2 计 WER）。

**主要指标**：
- VBDM：NyTT+ w/ UP-Drift SI-SDR 18.58 dB、PESQ 2.69、DNSMOS 3.59、UTMOS 3.93
- 对比 NyTT+ 基线：PESQ +0.06、DNSMOS +0.06、UTMOS +0.12，SI-SDR 持平
- 对比无配对 DriftSE：SI-SDR 由 6.60 dB 恢复至 18.58 dB，DNSMOS 基本保持（3.61→3.59）
- CHiME-3：WER 9.115%（NyTT+ 为 9.281%）、Squim SI-SDR* 10.16（+0.77）、DNSMOS +0.17、UTMOS +0.22（配对 t 检验 p<1e-10）
- 消融：no-Sinkhorn UTMOS 3.82、no-SQA 3.83，均明显低于完整组合 3.93

**是否开源**：暂无（正文未提供代码链接）

### ⭐ 评分：7/10
评分理由：将 NyTT 与 Sinkhorn drifting 两个既有范式以加权损失低成本融合，针对性修复了无配对漂移严重牺牲 SI-SDR/WER 的缺陷，SQA 潜空间选择有消融支撑，想法清晰有效。实验覆盖合成与真实域、附 95% 置信区间与显著性检验，证据扎实。不足在于对强基线 NyTT+ 的可感知增益幅度不大，真实录音上 WER 仍劣于未处理噪声信号，UrgentMOS 自身偏好未讨论，且未开源。属有实质贡献的增量工作。

---

## [14] SEMAC: Spherical Energy Matching Ambisonics Codec for Efficient Higher-Order Ambisonics Compression

**arXiv ID**：2610.32981 | **方向**：语音前端

**作者**：Christoph Hold, Jan Buethe, Jean-Marc Valin, Jan Skoglund, Toni Hirvonen, Nils Peters

**机构**：Meta Reality Labs Research | Google | Samsung Research America | Trinity College Dublin

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32981 | **PDF**：https://arxiv.org/pdf/2610.32981.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
高阶Ambisonics（HOA）声道数C=(N+1)²随球谐阶数二次增长，Opus CMF2/3须编码全部声道导致低码率传输不可行。SEMAC提出"方向能量匹配"：编码端用球面滤波器组（36波束×21频带、50帧/s）提取全阶方向能量包络作边信息，用CELT仅编码4–16个降维传输声道；解码端扩回全阶并按波束逐带重缩放，强制匹配编码端观测的输入能量分布。五阶MUSHRA听测（512/768 kbit/s）表明SEMAC以16/36传输声道即优于等参配置的全阶Opus CMF3，且在同等传输声道数下优于阶数截断基线。

### 🔧 技术方案

**问题背景：** Opus CMF2/3虽优化声道编码组织，但均码全部C路波形，总码率随阶数二次增长；现有参数化HOA编码器（DAC、COMPASS、IVAS等）质量依赖声源方位/数量等场景参数估计，信号自适应变换（PCA/SVD）又须传输基矩阵边信息，均有各自的鲁棒性或开销短板。

**模型架构：** 编码器：MDCT域SH系数经分析矩阵A（D×C，由临界采样球面上的max-r_E波束成形器加模态权重构成，综合伪逆B=A†）分解为D=36个方向波束；对每波束每CELT频带提取带能量作方向能量包络；投影矩阵T将信号降至C_tp<C个传输声道交CELT编码；传输重建由固定U完成，A/B/T/U均无矩阵边信息。解码器：CELT解码→扩回36维→用A在全方向分辨率下再分析并逐带归一化→按解码包络与解码实测包络之比重缩放各波束→B逆变换回SH域，实现能量引导的全阶上混。

**核心创新：** (1) 将CELT"包络-形状分离"原理从频域推广到方向域：每频带独立维护全阶方向能量包络，不做显式DOA或源数估计，对稀疏、密集、混响场景均鲁棒。(2) 解码端能量匹配：降维传输张成低秩子空间必然引入方向误差，解码后重施加输入包络，恢复全阶方向能量分布，而CMF3只能逐声道恢复能量。(3) 码率结构自包含：包络编码复用CELT能量编码框架（帧间/带间对数能量预测+6 dB格栅熵编码+细比特精化），细比特数随每传输声道可用码率自适应；CELT码率分配由编解码端相同导出，无需分配边信息。

**训练策略：** 属传统信号处理编解码器，无模型训练。实现fork自Opus v1.6.1，48 kHz采样、20 ms帧；推导用N3D正交球谐规范，实现输入输出转SN3D（AmbiX）；五阶配置C=D=36、B=21带、50帧/s；低码率模式自动降低包络精度防止边信息挤占波形码率，C_tp∈{4,9,16}与包络精度、聚合码率共同决定工作点。

### 📊 实验结果
**数据集**：MUSHRA听测素材：48 kHz五阶Ambisonics（36声道）7条预筛选关键条目，覆盖稀疏、密集与混响场景；每条目512/768 kbit/s各一次；输出经MagLS+KU100 HRTF双耳渲染。

**主要指标**：
- MUSHRA评分（11名有效听者）：SEMAC 16/36传输声道在两个码率下均达"Excellent"区间，中位数高于36声道全阶CMF3且评分散布更紧
- 等传输声道对比：SEMAC-BEAM9（C_tp=9）显著高于同为9传输声道的CMF3-SH2阶数截断基线
- 码率敏感性：C_tp=4/9时512与768 kbit/s评分相近，质量上限由传输声道数而非码率决定
- 包络开销：五阶方向包络量化可消耗超过100 kbit/s

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：把CELT包络/形状分离思想简洁地推广到方向域，思路清晰且无需任何矩阵边信息，工程上可直接嵌入Opus生态；对照实验专门隔离"包络恢复"与"降传输"两个因素，结论（少声道+包络优于全声道低精度）对HOA标准化有实际参考价值，作者为Opus核心开发者。不足在于主观实验规模偏小（11人、7条目）、缺客观指标，且未涉及SHD传输、白化及更优码率划分等设计空间。

---

## [15] CounselPlex: A Stressor-Aware Full-Duplex Counseling Model

**arXiv ID**：2610.32702 | **方向**：语音大模型

**作者**：Yeonju Kim, Bella Godiva, Yong Man Ro

**机构**：Integrated Vision and Language Lab, KAIST（韩国科学技术院）

**发布日期**：2026-10-26 | **论文**：https://arxiv.org/abs/2610.32702 | **PDF**：https://arxiv.org/pdf/2610.32702.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工语音模型（FD-SLM）虽能边听边说，但在心理咨询中常只回应最新话语、遗忘来访者已披露的核心压力源，本文称之为"Stressor Blindness"。CounselPlex 基于 PersonaPlex/Moshi 8.4B 骨干，在来访者静默 0.5 秒后生成 1–7 词压力状态的 think trace，并在新一轮说话确认时强制注入 agent 文本流的 PAD 位；另提出 RoPE 位置偏移增强（RPSA）稳定长上下文。合成语音评测集上其五维咨询质量全面超越域内微调基线，代价是全双工延迟增加约 1 秒。

### 🔧 技术方案

**问题背景：** 情绪支持对话研究多为纯文本严格轮换，FD-SLM 的角色条件只规定"如何行事"而非"要保留哪些用户信息"，压力源披露数轮后即失联；级联方案虽可挂外部模块但延迟不可比。

**模型架构：** PersonaPlex（基于 Moshi）双路音频-文本并行流，约 8.4B 参数，Mimi codec 12.5 fps、每帧 8 码本，2048 帧上下文。文本流含思维压力轨迹、<PAD>/<EPAD> 静音标记。数据流：来访者轮次结束→静默检测决定是否更新压力状态→Silero VAD v5 确认新轮开始→将活动状态强注入 PAD 位。

**核心创新：** (1) 压力状态"生成—注入"两阶段解耦：静默时更新、监听时仅注入不再生成，状态持续有效直至下次更新，把治疗性长期上下文显式写入文本流，无需外部记忆模块。(2) RPSA：长对话裁剪段起点超过 750 帧（约 60 s）时以 0.7 概率随机偏移整段 RoPE 绝对位置，保持相对次序，纠正训练中低位置索引采样过密导致的高位置欠训练。(3) 文本损失按 think/pad/speech 三组分别加权：PAD 远多于其他组且 think 稀疏，think 权重设低于 speech 以防过度生成；系统注入窗口不参与文本损失，仅监督 agent 音频流。

**训练策略：** 将 ESConv+ESCoT 用 CosyVoice3 合成 24 kHz 双固定音色语音语料（3,009 对话/158.3 小时，train/val/test=2,107/367/535）；GPT-4.1 按时间序标注核心压力源。8-bit AdamW+DeepSpeed ZeRO-2、bfloat16、batch 16、4 epochs、4×RTX A6000，约 45 GPU 时；每轮后加入随机间隔静默做停顿增强，单次训练运行。

### 📊 实验结果
**数据集**：自建 ESConv+ESCoT 合成语音语料（158.3 h/24 kHz）；ESConv 194 对话 2,286 轮、ESCoT 341 对话 3,992 轮测试；Full-Duplex-Bench 全双工行为集

**主要指标**：
- 咨询质量 Avg5（GPT-4.1 五维 1–5，沉默计 1）：ESCoT 2.813 vs PersonaPlex† 2.644（+0.169）；ESConv 2.481 vs 2.143（+0.338）
- 跨评委验证：Gemini-2.5-Flash 复现同排序（2.926 vs 2.691）；双评委响应级 Pearson 相关约 0.8
- 全双工行为：静默抢话 TOR 0.066（Synthetic）/0.213（Candor），流畅轮换 TOR 0.992 但延迟 0.988 s；打断响应 3.071/延迟 1.056 s（zero-shot PersonaPlex 为 4.210/0.400 s）
- 消融（combined Avg5）：完整 2.692，去注入 2.329，去 RPSA 2.201，域内微调基线 2.461
- 人评偏好：CounselPlex 非平局胜率 61.2%（52:33）
- 复用轮压力口头化率 36.2%，接近 GT 45.9%（基线约 28%）

**是否开源**：论文声明语料、代码与权重暂不发布，无法端到端复现

### ⭐ 评分：6/10
评分理由：首次命名并显式建模"压力源失明"，生成/注入解耦与 RPSA 简洁有效；消融、跨评委、响应率归一与配对检验使实验论证较扎实。但语音全部由双固定音色合成、评分依赖 GPT 系评委（兼标注与打分）、单训练种子、无backchannel且延迟上升，未开源进一步限制实用价值。

---

## 📄 更多语音论文（紧凑列表）

> 以下 1 篇为当日语音相关论文，未进入精读队列，仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），按预估评分从高到低排列。

**ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge**
- **arXiv ID**：2610.32202 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.32202（未精读，按摘要评分）

*Subagents used for reading: 15* | Generated on 2026-10-26 语音论文批次, by Kimmy's research agent | Powered by VAgent SpeechAI Researcher
