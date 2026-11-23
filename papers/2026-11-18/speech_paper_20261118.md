# 2026-11-18 语音论文速递

**共收录**: 5 篇 | **语音大模型**: 1 篇 | **语音前端**: 4 篇

> 目标日期 2026-11-18（北京时间）arXiv 语音相关论文（cs.SD + eess.AS，New + Cross，已去重与方向过滤）共命中 5 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts

**arXiv ID**：arXiv:2611.22627 | **方向**：语音大模型

**作者**：Yunrui Cai, Dingdong Wang, Lingwei Meng, Xixin Wu, Zhiyong Wu, Helen Meng

**机构**：香港中文大学（SE实验室）、清华大学深圳国际研究生院

**发布日期**：2026-11-18 | **论文**：https://arxiv.org/abs/2611.22627 | **PDF**：https://arxiv.org/pdf/2611.22627.pdf | **代码**：https://github.com/caiyunrui/MT-GRPO | **Demo**：暂无

### 📌 简介
针对说话人数未知的多talker重叠语音，SpeechLLM纯SFT对齐在密集重叠下易出现爆发式幻觉与畸形说话人/时间戳标签。本文提出两阶段生成式框架：先以CoT增强的SFT让模型在转写前显式推断全局说话人数，再用GRPO结合多维约束感知奖励MCAR做受约束在线探索，直接优化置换不变准确率并施加分辨计数、时序与结构约束。在Libri3Mix与自建Dynamic-Mix（2+3人混合）上分别取得cpWER 14.52%/9.24%、WDER 1.95%/1.12%，GRPO相对SFT+CoT带来35%/54%的cpWER相对下降，Dynamic-Mix说话人数推理准确率从90.06%升至99.72%。

### 🔧 技术方案

**问题背景：** 传统级联管线（分离+ASR+聚类diarization）误差传播严重；SOT/PIT专用模型虽强但缺乏SpeechLLM的推理与泛化能力；直接把SOT类模型接进LLM的混合方案仍需外挂前端。纯SFT因teacher forcing从不针对自身畸形输出训练，且cpWER等目标是序列级不可导的，在说话人数变化的场景下产生连续幻觉、时间边界退化与CoT计数-实际生成段数不一致。

**模型架构：** 以Qwen2.5-Omni-7B为基座（音频编码器+模态投影器+LLM），输出统一结构化序列 Y=C（CoT计数前缀）⊕ 各说话人段[⟨spk_i⟩, t_s, t_e, W_i, ⟨/spk_i⟩]。LoRA普遍施加于音频编码器、投影器与LLM全部线性层，兼顾前端声学解耦与LLM语言/推理能力防灾难遗忘。

**核心创新：** (1) CoT增强SFT：训练目标前置说话人数估计，并用置换不变提示（段序随机打乱）迫使模型依赖声学而非序列偏置，先建立XML结构模板。(2) 多talker域首次引入GRPO：每查询采样独立rollout组、组内估计基线免价值模型，KL锚定冻结SFT参考策略，把范式从被动模仿转为对完整假设的受约束在线探索。(3) MCAR奖励引擎：五维正交约束——CoT计数稠密奖励、全排列搜索的PI-WER指数衰减语义奖励、0.2s容差的时间对齐奖励、针对连续插入/替代错误最大串长L_burst的爆发惩罚（强制声学接地丢失时闭合说话人标签）、结构时序逻辑惩罚（缺标签/时序倒置/CoT数与实际段数矛盾的灾难性惩罚），五项等权求和。

**训练策略：** SFT用精心构建的细粒度多talker数据训练5 epochs、全局batch 128；GRPO仅在从官方训练集严格采样的10,000条高重叠样本上做RL，学习率较SFT进一步衰减、KL系数β约束、裁剪参数ε限制更新幅度，语义奖励衰减因子γ、burst容差τ_b与惩罚系数λ_b按消融设定，rollout组内独立采样。评测指标为cpWER、WDER（词级说话人日志错误率）、TE与CoT-Acc。

### 📊 实验结果
**数据集**：Libri2Mix/Libri3Mix（LibriSpeech+WHAM!噪声，0dB信噪比混合），自建Dynamic-Mix（2+3说话人均匀采样打乱、测试时人数未知）

**主要指标**：
- Libri3Mix：cpWER 14.52%、WDER 1.95%、TE 0.10s（SFT+CoT为22.45%/4.03%/0.18s）
- Dynamic-Mix：cpWER 9.24%、WDER 1.12%、CoT-Acc 99.72%（零样本仅69.3%/18.52%/32.25%）
- 与SoTA对比：Libri2Mix cpWER 4.45%优于UME 6.4、Whisper-Sidecar 4.66；Libri3Mix 14.52%优于UME 15.9、TS-ASR-AD 14.81、SOP-LLM 16.5
- 消融：去掉计数奖励cpWER 9.24→18.02，去掉N!排列评估→16.56，去掉burst惩罚→11.84

**是否开源**：代码已开源 @ https://github.com/caiyunrui/MT-GRPO

### ⭐ 评分：8/10
评分理由：首个将GRPO系统引入多talker联合ASR+diarization并配套多维物理约束奖励的工作，"SFT建格式、RL治幻觉"动机清晰，消融定量证实每个奖励维度的贡献（burst惩罚与N!排列项尤为关键），Dynamic-Mix未知人数设定贴近真实会议场景且开源。局限：全部评测为LibriMix+WHAM!合成重叠，缺真实电话/会议集，基座限于7B单模型，SOP-LLM在Libri2Mix仍略优。实质性强、可复现，接近顶会水准。

---

## 语音前端

## [2] High-Fidelity Binarized Neural Vocoder

**arXiv ID**：arXiv:2611.22593 | **方向**：语音大模型

**作者**：Andong Li, Tong Lei, Xiaodong Li, Chengshi Zheng

**机构**：中国科学院声学研究所、中国科学院大学、腾讯混元多模态模型部

**发布日期**：2026-11-18 | **论文**：https://arxiv.org/abs/2611.22593 | **PDF**：https://arxiv.org/pdf/2611.22593.pdf | **代码**：https://github.com/Andong-Li-speech/BiVoC | **Demo**：暂无

### 📌 简介
本文提出首个面向1-bit权重/激活的二值化神经声码器BiVoC，解决现有高保真声码器全精度推理开销大、而直接二值化又导致频谱严重退化的矛盾。方法在其先前RNDVoC框架上，将逆问题建模、值域-零空间分解与细到粗非均匀子带引入1-bit设定，并设计二值卷积单元BCU与混合精度分配策略。LibriTTS上BiVoC仅1.08M参数、1.01G OPs即达PESQ 3.447、VISQOL 4.779，远超直接二值化的HiFiGAN+BNN（PESQ 1.246），在相近运算量下反超全精度Vocos与DegVoC；OOD AISHELL3主观MOS 4.00与HiFiGAN-V1（3.93）相当，证明BNN在音频生成中的可行性。

### 🔧 技术方案

**问题背景：** 端侧TTS与嵌入式声学设备要求声码器在严格延迟、功耗与内存预算下持续运行，而主流高保真声码器依赖全精度卷积。BNN理论上可带来32倍权重压缩与最高64倍卷积计算削减，但声码合成需精确的谐波连续性与相位结构，把HiFiGAN/Vocos的卷积层逐层替换为二值版本会出现严重的频谱塌落，故BNN此前从未被系统用于神经声码。

**模型架构：** 时频域框架，输入mel谱先经值域空间模块RSM转为线性谱；零空间模块估计残差幅度与相位，由层级子带编码HSEM（谱按"从细到粗"非均匀切为F个子带，子带内Norm+二值Conv1d独立编码后堆叠为C×F×T三维张量）、层级子带幅/相解码HSMM/HSPM（二值Conv1d+RPReLU，输出层保留全精度Conv1d产生连续对数幅度与相位）、以及以BCU为核心的二值卷积模块BCM；再由RNDM与iSTFT合成波形。总参数1.08M。

**核心创新：** (1) 将RND理论二值化重构：值域分量由伪逆闭式给出、网络只需学习零空间残差估计器，大幅缓解1-bit表示的信息瓶颈，消融证明去掉RND策略后质量显著下降。(2) 提出稳定残差特征流的BCU二值卷积单元与细到粗子带编解码：低频子带分辨率高以保护F0与谐波；且二值化后归一化层占比凸显，BN经对比被证明优于LN/DyT。(3) 混合精度设计：按head/body/tail逐段分析质量-复杂度敏感度，发现编码器头部保全精度仅微增计算即可显著提升质量，据此只把计算主导部分二值化、输出层必全精度。

**训练策略：** 训练集为LibriTTS train-clean-100/360与train-other-500全部音频，val-full验证；batch size 16，每条切64帧（16384样本）；AdamW（β1=0.8, β2=0.99），初始lr 2e-4，单张A100，生成器与判别器各训练1M步、混合精度训练。损失为重建+对抗：7分辨率（窗长32–2048、mel bins 5–320）多分辨率mel损失、RI谱MAE、对数幅度MSE、相位损失、一致性损失，叠加多尺度/多周期判别器对抗项。

### 📊 实验结果
**数据集**：LibriTTS（208条dev-clean/dev-other，24k训练条件）；OOD：EARS、AISHELL3（中文）、RFWave（900条含音乐音效）、MUSDB18（音乐）

**主要指标**：
- LibriTTS：BiVoC M-STFT 0.962、PESQ 3.447、MCD 3.222、VISQOL 4.779、WER 6.98%，1.08M参数、1.01G OPs/5s
- BNN对比：HiFiGAN+BNN PESQ 1.246 / Vocos+BNN PESQ 1.829，BiVoC分别高出+2.20与+1.62，WER低6~9个百分点
- 相近复杂度（≈1G OPs）：BiVoC PESQ 3.447、GOMPSNR 4.645，优于全精度Vocos 3.196/4.004与DegVoC 3.224/4.305
- 主观MOS：AISHELL3 4.00±0.08 vs HiFiGAN-V1 3.93，MUSDB18人声 3.61±0.09 vs HiFiGAN-V1 3.38（GT 4.32/4.22），AB偏好显著且与全精度旗舰仍有小差距

**是否开源**：代码与预训练权重已开源 @ https://github.com/Andong-Li-speech/BiVoC

### ⭐ 评分：8/10
评分理由：首批系统研究BNN声码器的工作，"闭式值域+二值零空间"的组合是聪明的信息保全思路，16张表的消融（替代梯度、归一化、子带划分、精度分配）扎实，评测覆盖域内/中文/音乐OOD与主观实验且开源。不足：绝对质量仍逊于BigVGAN、RNDVoC等全精度旗舰，常规CPU/GPU上无XNOR-Popcount加速时实测速度增益有限，"理论OP优势"需专用硬件兑现。整体达到TASLP水准的实质贡献。

---

## [3] Back to Mel: Learning to Bridge Fidelity and Perception in Generative Speech Enhancement

**arXiv ID**：arXiv:2611.22628 | **方向**：语音前端

**作者**：Andong Li, Kun Zhou, Xiaodong Li, Chengshi Zheng

**机构**：中国科学院声学研究所、中国科学院大学、Télécom Paris（LTCI）

**发布日期**：2026-11-18 | **论文**：https://arxiv.org/abs/2611.22628 | **PDF**：https://arxiv.org/pdf/2611.22628.pdf | **代码**：https://github.com/Andong-Li-speech/BAME | **Demo**：暂无

### 📌 简介
针对生成式语音增强中可学习latent牺牲声学保真、扩散采样多步低效的问题，本文重新审视Mel谱的两大互补先验——层级频率带结构与RND伪逆值域恢复+退化相位，提出流匹配框架BaME：以2.9%于DiT-331M参数的子带感知Transformer（SaT）做Mel增强，用融合退化相位的phase-aware声码器重建波形，并以质量引导双相位（QDV）与一步保真-感知对齐（OS-FPA）实现单步生成。DNS-Challenge、EARS、GSR、URGENT 2025上全面领先，DNS-2020无混响集PESQ 3.430、WER 1.607%，CPU RTF 0.85。

### 🔧 技术方案

**问题背景：** 生成式SE大量转向VAE/NAC等学习latent，但其为压缩/合成设计，丢失说话人特质与细粒度谱细节，SSL语义保真不保声学保真；Mel带通结构先验长期未被利用，传统Mel+声码器管线完全抛弃相位先验；多步FM采样推理慢，一步化方法又常在保真与感知间失衡。

**模型架构：** 两阶段"Mel增强+声码器"。增强侧SaT：SSEM把FM插值mel谱与退化mel按频轴均分N=25子带、各子带Conv1D编码，并用N个独立低秩LRConv1D把去噪微调WavLM末层语义特征投影到对应子带并联编码；P=6个双路块DPB（BiGRU跨子带+MHSA时序+FFN，AdaLN时间步调制，256通道4头）；CSDM"滤波-细化"双支解码估计增益G与残差R得log-Mel=log(exp(X̄)⊙G+R)。生成侧改造DegVoC：预测Mel经伪逆𝒜†恢复线性幅度，与退化相位Φ_Z构造复谱输入，细化后iSTFT出波形。

**核心创新：** (1) 把Mel视为"粗粒度T-F子带"：SaT利用mel滤波器层级频带组织做子带并行建模，以2.9%参数、66.6%计算量超越DiT-331M，且算子硬件友好。(2) 退化相位先验+QDV：声码器复谱以观测相位而非零相位初始化，训练质量预测器对退化/零相位两候选自适应择优（UDMOS打分），规避相位不可靠场景，开销仅声码器级。(3) OS-FPA一步生成：免蒸馏，预训练FM上60k步微调，联合保真域（幅度/mel/原始谱损失）与感知域（λ_perc=25质量损失）约束，zero/退化相位各半采样，NFE=1兼顾保真与感知。

**训练策略：** 清洁语音约600小时（LibriVox、AISHELL3、DiDi、EARS、VCTK、MLS及URGENT指定库，按UTMOS/DNSMOS取top25%并剔除评测重叠说话人）；噪声池DNS5/FMA/FSD50K/WHAM!+RIR混响。Mel：16kHz、窗/FFT 1280、hop 25%、100 bins（0–8kHz）。FM训练batch 8、lr 1e-4、AdamW（β=0.8/0.99，wd 0.01）、1M步、EMA 0.999；OS-FPA batch 4、lr 1e-5、60k步；损失权重{40,40,40,25}；单张A100-80G。

### 📊 实验结果
**数据集**：DNS-Challenge 2020（有/无混响）、EARS-WHAM_v2/Reverb_v2、GSR、URGENT 2025非盲集；对比23个判别式/生成式基线（BSRNN、CleanMel、FlowSE、SenSE、PASE、UniPASE、Metis、GenSE等）

**主要指标**：
- DNS-2020（无混响）：BaME PESQ 3.430、SpkSim 0.957、WER 1.607%、UTMOS 4.119；PESQ较最强基线BSRNN(3.347)+0.083
- EARS-WHAM_v2去噪：PESQ 2.673 vs CleanMel 2.531；EARS-Reverb_v2去混响：PESQ 2.807 vs 2.697、DiMOS 4.502
- URGENT-2025非盲（未见退化域）：PESQ 2.259、CER 12.584%、UTMOS 3.293，优于挑战赛前三名系统
- 效率：总参数332.4M（含WavLM+声码器）、45.5 GMACs/s、CPU RTF 0.85、GPU 40.78×实时；消融证实QDV与OS-FPA各提升对应指标

**是否开源**：代码与音频样例已开源 @ https://github.com/Andong-Li-speech/BAME

### ⭐ 评分：8/10
评分理由："回归Mel"的表征中心视角论证充分（RND+子带+相位先验三位一体），SaT以小博大对比DiT-331M有说服力，QDV/OS-FPA直接回应多步生成与保真-感知失衡两大痛点，四个异构基准+主观+效率评估全面且开源。不足：依赖质量预测器精度、总参数仍达332M（含SSL前端）、极端退化下相位可靠性边界未充分讨论。接近SoTA的扎实工作。

---

## [4] Insight into Parametric First-Order Ambisonics Upscaling in Time and Frequency Domains

**arXiv ID**：arXiv:2611.23089 | **方向**：语音前端

**作者**：Oded Levi, Boaz Rafaely

**机构**：本-古里安大学电气与计算机工程学院（以色列）

**发布日期**：2026-11-18 | **论文**：https://arxiv.org/abs/2611.23089 | **PDF**：https://arxiv.org/pdf/2611.23089.pdf | **代码**：暂无（arXiv未提供） | **Demo**：暂无（arXiv未提供）

### 📌 简介
一阶Ambisonics（FOA）双耳渲染存在定位退化、高频染色的局限，已有FOA→HOA上采样方法聚焦直达声却忽略早反射的空间价值。本文构建"选择性上采样早反射"的分析框架：以FOA双耳分量的能量为准则，从直达声+100ms内早反射候选集中挑出r条最强的反射用高阶（N=10）LSD精确渲染，其余保持FOA-MAgLS渲染，并在长期（LT）、短时（ST，32ms Hann窗）与时频（TF，STFT局部窗）三个域比较选择策略。WSJ0语音仿真表明TF域最优：r=30时全局SI-SDR 17.66 dB，较ST/LT（15.64/15.56 dB）高约2 dB，IACC误差降至0.009，且利用语音时频稀疏性在多说话人场景最稳健；10人MUSHRA听音进一步印证TF感知优势。

### 🔧 技术方案

**问题背景：** HOA录制需大口径球阵，消费场景不现实；Dirac/Compass等参数法每时刻仅假设少数主导方向成分，在密集混响与多说话人重叠下空间假设失效，且主要增强直达声而未利用承载空间感信息的早反射。深度学习Ambisonics上采样缺乏对"哪些反射值得上采样"以及"时间/频率/时频哪个域最适合做选择"的可解释洞察。

**模型架构：** 分析框架而非神经网络：声场由镜像源法（ISM）产生各反射平面波，经球谐分解得FOA（一阶4通道）与10阶HOA参考信号。双耳渲染=FOA基底（1阶MAgLS解码，抑制高频染色）+上采样增量（所选反射在N=10 LSD下的渲染与其FOA渲染之差），使被选反射的分量与HOA参考完全一致；能量准则对每条反射计算左右耳FOA双耳信号平方和E(i)，取最大化总能的子集Ψ（r可调）。

**核心创新：** (1) 首次把"早反射选择性上采样"形式化为集合选择问题，提出按r∈{0,1,3,10,30}调节精度-复杂度权衡的统一实验框架。(2) 三级选择域对比：LT用全信号全局能量（静态）；ST用32ms/步进16ms窗的局部时域能量（50%重叠）；TF在每个STFT bin的Δτ×Δν局部窗内计算能量并逐bin选子集，同时利用语音的W-离散正交时频稀疏性与人耳频带化空间感知机理。(3) 多目标验证体系：SI-SDR总体/直达声分解、清晰度过渡指数C50误差（对照1.1 dB JND）、IACC误差（2ms ITD窗内最大互相关），并用drr分档与1–4说话人扫描评估稳健性，最后以ITU-R BS.1534-3 MUSHRA闭环可听度。

**训练策略：** 本文为解析/仿真研究、无训练过程。实验配置：6个鞋盒房间（72–1800 m³，T60 0.3–0.8 s），每房间3个方位（30°/60°/75°）×10个几何间距距离共30场景，源数~U{1,4}，语音取WSJ0 3.4s干净片段，DRR范围-10~15 dB；HRTF经球谐变换至SH域，10阶渲染，ST窗32ms/Hann、TF窗按STFT局部区域设定。

### 📊 实验结果
**数据集**：ISM仿真的6房间×30声学场景+WSJ0语音；MUSHRA听音（10名听者，2个高DRR场景：单/双说话人）

**主要指标**：
- 全局SI-SDR@r=30：TF 17.66 dB > ST 15.64 dB > LT 15.56 dB；单调随r提升，验证早反射价值
- IACC误差：TF在r=30时0.009（较r=0的0.083下降一个数量级），单条反射（r=1）即显著改善双耳相干
- C50：误差保持在1.1 dB JND附近量级，TF与两种时域法均优于anchor
- 多说话人：源数增至4时ST因时间重叠退化，TF借助speech稀疏性保持目标直达声SI-SDR稳定
- 主观MUSHRA：方法主效应显著（F(1.29,11.59)=89.5, p<.001, ηp²=.91），TF得分最高；低DRR场景各法收敛、无 audible 差异

**是否开源**：暂无（arXiv未提供代码/Demo）

### ⭐ 评分：6/10
评分理由：为FOA上采样提供了难得的"机理性洞察"：问题定义干净、消融式域对比（LT/ST/TF）+客观指标+标准MUSHRA的验证链条完整，TF优于时域的解释（时频稀疏性）对后续盲上采样与神经方法设计有直接指导价值。局限：框架依赖ISM已知反射的oracle信息（实际中方向/延迟需估计），未与Dirac/Compass或学习式上采样直接对比，主观听测仅10人、2个高DRR场景，样本偏小；无开源代码。作为分析型论文质量扎实，实用转化尚需一步。

---

## [5] Personalized Causal Low-Bitrate Coded Speech Restoration with Speaker Embeddings

**arXiv ID**：arXiv:2611.22620 | **方向**：语音前端

**作者**：Eray Özgünay, Christian Rollwage, Kishan Gupta, Andreas Brendel, Xavier Domont, Mattes Ohlenbusch, Jan Rennies, Simon Doclo

**机构**：Fraunhofer IDMT（HSA）、Oldenburg大学、CEOTRONICS AG、Fraunhofer IIS

**发布日期**：2026-11-18 | **论文**：https://arxiv.org/abs/2611.22620 | **PDF**：https://arxiv.org/pdf/2611.22620.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文首次系统研究低码率编码语音恢复（CSR）的个性化问题：以因果低复杂度UBGAN为基线，将AMR-NB 4.75kbps编码的8kHz语音恢复为16kHz宽带语音，比较两种基于说话人embedding的路线——单模型embedding条件化与聚类多模型选择，并评测混合方案。VCTK实验（分seen/unseen说话人集）显示：聚类模型选择并不稳定优于非个性化基线，而embedding条件化在两类说话人集上均显著提升ViSQOL与WB-PESQ（seen集ViSQOL 2.80→2.92、WB-PESQ 2.36→2.47），仅增约9K参数；且最优个性化路径依赖底层CSR模型架构。

### 🔧 技术方案

**问题背景：** 电话网络仍大量使用AMR-NB等legacy低码率codec，带宽受限、听感差且易致疲劳；现有CSR/BWE不做说话人自适应，残留codec伪影与说话人个性细节。个性化在语音增强、TTS、神经编码中已证明有益，但从未被系统研究于CSR；此前仅有的个性化CSR基于非因果、高复杂度HiFi-GAN+，能否推广到因果低延迟模型未知。

**模型架构：** CSR基线为盲UBGAN变体：编码语音经PQMF分析（2带前端/4带合成后端），以编码信号80维mel谱为唯一条件，生成器为类U-Net轻结构（6级下/上采样、48通道、因果深度可分离卷积核7、TADE残差调制块），子带合成恢复16kHz波形且允许改写低带；判别器为4子多分辨率STFT集成（FFT 2048/1024/512/256）。个性化采用冻结ECAPA-TDNN提取192维单位范数embedding。

**核心创新：** (1) Embedding条件化：将192维说话人embedding经学习卷积映射并与mel条件特征沿时间广播相加后注入下采样块，其余不变；测试仅需一条短清洁enrollment语音、推理开销几乎为零（参数309K→318K）。(2) 聚类模型选择：对训练说话人embedding做k-means（C=4，簇含16/17/22/34人），每簇训练一个同构UBGAN；test-time按enrollment embedding最近质心（余弦距离）选模型，让每模型聚焦更窄的声学子任务。(3) 首次在同一因果基线上对照两法及hybrid（簇内再加embedding条件化），并与非因果HiFi-GAN+基线（1.06M参数、30.54 GMACs）交叉比较，揭示个性化最优方法与底层模型容量/因果性相关。

**训练策略：** VCTK共109人（剔除p315）、每人约400条16kHz录音（ffmpeg AMR-NB 4.75kbps编码）；89人训练（人均80%）、10人验证、10人held-out构成unseen集，训练者20%语句构成seen集。随机裁1秒段、batch 64；mel条件FFT 256/窗240/hop 160。损失为LSGAN对抗+特征匹配（权重10）+四分辨率STFT重建+波形MSE；生成器AdamW（lr 2e-4，β=0.8/0.99，wd 0.01，每epoch×0.99衰减）、判别器Adam（lr 1e-4）。

### 📊 实验结果
**数据集**：VCTK（109英语说话人，16kHz；输入为AMR-NB 4.75kbps编码8kHz信号）

**主要指标**：
- Seen：embedding条件化 ViSQOL 2.92±0.50、WB-PESQ 2.47±0.35，vs 基线2.80/2.36（Wilcoxon p<0.001）；LSD持平（0.98）
- Unseen：embedding条件化 ViSQOL 2.97±0.53 / WB-PESQ 2.34±0.35，均高于基线2.92/2.28（p<0.02）；LSD持平或略差（0.99 vs 0.98）
- 聚类选择：seen ViSQOL 2.85但WB-PESQ反降；unseen三指标全劣于基线；hybrid不优于单独embedding条件化
- 复杂度：UBGAN 309K参数/0.253 GMACs，远小于HiFi-GAN+（1.06M/30.54 GMACs），且WB-PESQ与ViSQOL反而更高

**是否开源**：暂无

### ⭐ 评分：5/10
评分理由：面向legacy电话codec+端侧实时CSR的真实痛点，实验设计规范（说话人级显著性检验、seen/unseen分离、双基线交叉对比），负结果（聚类选择与hybrid不稳定）有社区参考价值。但方法为embedding注入与簇路由的既有技巧组合，绝对增益小（WB-PESQ约+0.06~0.11）、仅单一codec与英文VCTK域，且未开源。属有参考价值的增量工作。

---

*Generated on 2026-11-23（补录执行日 2026-11-19）*
