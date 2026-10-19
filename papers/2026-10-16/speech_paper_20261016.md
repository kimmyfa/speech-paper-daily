# 2026-10-16 语音论文速递

**共收录**: 9 篇 | **语音大模型**: 6 篇 | **语音前端**: 3 篇

> 目标日期 2026-10-16（北京时间）arXiv 语音相关论文共命中 9 篇。
> 以下是按评分排序的结果。

---

## [1] Reference-Guided Turn-Taking Style Transfer for Full-Duplex Spoken Language Models

**arXiv ID**：2610.20763 | **方向**：语音大模型

**作者**：Yuxuan Chen, Yang Xiao, Jack Sun, Chak Sun, Brick Li, Sam

**机构**：The Chinese University of Hong Kong, Shenzhen; The University of Melbourne; Lulula

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.20763 | **PDF**：https://arxiv.org/pdf/2610.20763.pdf | **代码**：暂无 | **Demo**：https://elpsykongloo.github.io/initiative-vector/

### 📌 简介
全双工语音模型的轮换风格（话轮主动性）被冻结在权重里，现有外部控制方法或需重训、或指令遵循不可靠。本文发现并提取"initiative vector"：从模型自身对话中、无需训练与标注，用类别均值差得到 L30 残差流单一方向；该方向可读（提前 800 ms 预测话语起始，AUC 0.82–0.90，超双说话人计时基线 +0.115~0.185）亦可写（沿方向按剂量叠加，语占比从 21–30% 单调移至 6–12% 至 42–61%）。用一段 5 分钟参考录音的三体征校准每人剂量即可迁移其轮换风格：换他人参考使匹配变差的比例达 92.7–98%，且在 Moshika/Moshika-RL/PersonaPlex 三权重与 CANDOR 上零样本成立。

### 🔧 技术方案

**问题背景：** 全双工模型逐帧决定是否接管话轮，形成"会话人格"，但一套权重只编码一种风格；训练类方法把单一风格写死且易奖励劫持，指令控制遵循率仅 64.4%，已有激活转向只设二值听/说状态、单一剂量，无法按人校准。

**模型架构：** 基于 Moshi 架构的三个 80 ms 帧率全双工权重（Moshika、Moshika-RL、PersonaPlex），32 块时间 Transformer 残差流。在 L30 位置（最深层仍可被后续整块处理并写入 KV cache、使偏移在上下文中持续）提取 u=(μ+−μ−)/‖μ+−μ−‖，正负样本为沉默帧中 800 ms 内起语与保持沉默者；生成时每帧 h_t←h_t+αs·u，s 为 listen-to-speak swing 以跨权重可比。每层重拟合对比做深度剖面定位决策。

**核心创新：** (1) initiative vector：无训练无标注读取并控制"接管话轮"倾向，方向随机对照（norm-matched）语占比变化≤5.6 点，证效属于方向而非扰动幅度。(2) 机制发现：接管话轮证据在末层达峰（L31 达 0.968/0.898/0.966），让位证据峰在中层（L26/L22/L19）后衰减，"正在说话"L0 即可解码约 0.99——取轮与让轮是不同深度的两套轴。(3) 参考引导的风格迁移：5 分钟录音提取语占比、重叠起始/分钟、应答概率三体征，按训练参考 SD 归一的三维距离，在 100 dev 目标上选最小化平均距离的剂量，新说话人无需运行模型即可校准。

**训练策略：** 核心方法不涉及训练：方向由模型自身未转向对话的类别均值对比得到；基线为同样 100 对话上训练的双说话人计时逻辑回归。剂量网格 {−2a,−a,0,a,2a}，a=0.125（Moshika/PersonaPlex）或 0.25（Moshika-RL）；体征由 Silero VAD 提取，σ 来自 120 训练参考；报告均值基于 3 seeds、95% 双向 bootstrap（5000 重采样，按对话类型分层）。

### 📊 实验结果
**数据集**：Seamless Interaction 双人对话（每权重 100 拟合/500 留出）；CANDOR 500 段零样本；迁移用 568 留出参考×550 目标

**主要指标**：
- 读取 AUC（800 ms 起始）：0.818/0.830/0.898，超计时基线 +0.115/+0.185/+0.172，500 对话中 449/497/462 领先；无近文本时仍达 0.806/0.823/0.893
- 转向效应：语占比 −2a 时 6–12%、+2a 时 42–61%（默认 21–30%）；−a→+a 配对提升 20.1/27.4/14.1 点
- 风格迁移：换他人参考使距离增大比例 92.7/98.0/95.6%；校准后语占比 Spearman 0.69/0.60/0.78；优于最优均匀剂量 0.129/0.208/0.164 SD（达事后最优增益的 93.1/99.5/98.1%）；10 个 dev 对话即达平台；跨权重剂量相关 ρ=0.81/0.77/0.70

**是否开源**：暂无代码；音频 Demo 已公开；数据用公开 Seamless Interaction 与 CANDOR

### ⭐ 评分：8/10
评分理由：将可解释性中的线性表示假设落地为全双工模型轮换行为的可读写控制量，机制分析（取轮/让轮深度分离）与迁移实验相互印证，且证明增益源于个性化本身而非均匀补偿，论证严谨。实验覆盖三权重、两语料、配对同种子对照与随机方向消融，统计设计扎实。局限在仅验证 Moshi 架构系、未评估转向后内容质量与任务表现，且无代码开源；但对全双工对话系统个性化落地有直接工程价值。

---

## [2] CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models

**arXiv ID**：2610.21143 | **方向**：语音大模型

**作者**：Yingzhuo Deng, Chong Li, Bingxin Liu, Yi Shu, Tianyu Peng, Can Xie, Siyao Song, Shuo Ren, Jiajun Zhang

**机构**：中国科学院自动化研究所、中国科学院大学人工智能学院、武汉大学人工智能研究中心（Wuhan AI Research）

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.21143 | **PDF**：https://arxiv.org/pdf/2610.21143.pdf | **代码**：https://github.com/yingzhuodeng/CoSTA | **Demo**：暂无

### 📌 简介
口语对话模型（SDM）生成与合成共享语音 token 空间，导致自回归序列过长、推理代价高；直接换低码率 tokenizer 会引入压缩-质量权衡且需重训解码器。本文发现语音 token 序列可被 BPE 无损压缩且遵循近似 log-linear 缩放规律（8 种 tokenizer 配置上 R²≥0.98），据此提出 CoSTA：通过后验词表扩展、发音适配与对话适配三步，让原有 SDM 生成压缩 token，再确定性展开回原空间交原语音解码器合成。在 Step-Audio 2 mini（8B）上，中/英扩展语音 token 生成速度达 1.736×/1.659×，全响应延迟降 22.4–39.0%，G-Eval 平均 72.27（vs 基线 69.24），ASR-CER 从 7.49% 降至 1.51%，质量不降反升。

### 🔧 技术方案

**问题背景：** 现有 SDM（Step-Audio 2、GLM-4-Voice 等）自回归生成与语音解码耦合在同一 token 空间，25 Hz 序列长、耗生成预算；换低码率 codec 需重训 tokenizer-解码器-SDM 整套链路，且根本未解耦两者。

**模型架构：** 基于 8B Step-Audio 2 mini（S3Tokenizer V2，25 Hz，原语音词表 6656）。CoSTA 用 BPE 从对话语音 token 序列学习扩展词表（+80K 单元），新单元 embedding 与 LM-head 行按组成 token 均值初始化（仅增约 6% 参数）；推理时生成文本-语音交错序列，仅对语音流做确定性 BPE 展开 π(z)=s 后送原解码器，tokenizer 与 decoder 完全不动。

**核心创新：** (1) 揭示语音 token BPE 压缩的 log-linear 缩放规律（10K–320K 单元、八配置、跨语种 R²≥0.994），为"生成-合成 token 空间解耦"范式提供实证依据。(2) 兼容性保持的后验适配框架：不重训 codec、不改合成接口即可加速任意现有 SDM，与低码率 tokenizer 互补（在 OpenS2S 12.5 Hz 上仍再省 18–21% 步数）。(3) 两阶段渐进适配：阶段一只调 embedding/LM-head（lr 1.6e-4），阶段二解冻中间层（lr 2e-5），再加对话适配（只训 LLM，冻结语音编码器/adaptor/解码器），消融显示去掉对话适配 G-Eval 从 72.27 崩至 24.35。

**训练策略：** 损失为标准序列 NLL（式 5/6）。发音适配数据：Emilia 中/英各 300h，经 Seed-VC 统一音色；对话适配数据：按 OpenS2S 管线从 InstructS2S-200K 构建约 50K 例/语种（49,664 中、49,408 英，CosyVoice 2 合成回复，过滤 >1 分钟）。AdamW + cosine（warmup 0.03），bfloat16，DeepSpeed ZeRO-1，grad clip 1.0，global batch 256，3 epochs，8×A100；总训练约 79.5 A100 GPU·时。推理 greedy，repetition penalty 1.2，max 2048 tokens。

### 📊 实验结果
**数据集**：URO-Bench 12 个中英语音对话基准（AlpacaEval-zh、APE-zh、Claude-zh、LCSTS-zh、MLC-zh（多语）、Wildchat 等）

**主要指标**：
- 模型侧效率：CoSTA-ZH 生成压缩率 ρg=66.81%，相对扩展 token 生成速度 1.736×；CoSTA-EN 70.17%、1.659×（Vanilla-FT 均 ρg=100%、速度约 1.0×）
- 系统效率：单卡 A100 + vLLM，并发 1/4/8 下全响应延迟降 32.8–39.0%（中）/22.4–26.0%（英），吞吐升 51.6–59.2%/25.8–38.6%，峰值显存仅多 ≤0.68 GiB
- 质量：CoSTA-ZH 平均 G-Eval 72.27 vs 基线 69.24（+3.03）、ASR-CER 1.51% vs 7.49%，UTMOS 3.75 持平；人评 1080 条配对 MOS，流畅性 win-or-tie 86.1–96.1%
- 预算受限交互：CoSTA-ZH 有效轮次 7.21 vs Vanilla-FT 3.71，语音时长 150.7s vs 97.6s

**是否开源**：代码已开源 @ https://github.com/yingzhuodeng/CoSTA

### ⭐ 评分：8/10
评分理由：视角原创——不动 tokenizer/decoder、以后验词表扩展解耦生成与合成，填补了低码率 codec 路线之外的效率空白，且 log-linear 压缩规律有扎实跨配置验证。实验充分：效率-质量-系统三层指标齐全，消融定位各组件贡献，跨架构迁移（OpenS2S）证明通用性，代码开源。主要局限：仅验证两个 8B 级开源 SDM，训练与数据准备（音色转换、对话合成 1–2 天×8 卡）成本不算低，且质量提升部分依赖适配数据而非方法本身。实用与启发价值均高。

---

## [3] PEDBench: Can Speech Models Detect Phonetic Errors?

**arXiv ID**：2610.20830 | **方向**：语音大模型

**作者**：Zhonghao Shi, Zackary Rackauckas, Jasmine Yip, et al.（共12人）

**机构**：Harvard University, University of Southern California, University of Michigan, Columbia University

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.20830 | **PDF**：https://arxiv.org/pdf/2610.20830.pdf | **代码**：暂无（承诺录用后开源代码与acted/synthetic数据集） | **Demo**：暂无

### 📌 简介
语音错误检测（PED）是识字教育与临床言语病理评估的关键，但因高质量评测数据缺乏、标注不一致，SOTA语音模型能否可靠检测音素级错误一直不明。本文提出首个PED基准PEDBench，数据跨自然到受控连续谱：真实儿童朗读错误（N=334）、演员脚本化错误（N=1,188）、音素可控TTS合成的含错语音（N=1,083），全部由两名语音学训练标注者核验，并提出要求"检测对且诊断对"的诊断加权P/R/F1。评测13个SOTA模型发现其在受控条件下仍无法可靠检测音素错误、精度偏低；在合成数据上LoRA微调的Qwen2.5-Omni与AF3 acted F1达90.06/88.83超越所有基线，但儿童语音仍存在sim-to-real差距。

### 🔧 技术方案

**问题背景：** 现有PED/MDD研究碎片化：公开数据集人工音素标注不一致（作者标注员复标100句，与原标注F1仅42.25/66.22）；SOTA音素识别模型与语音-语言模型（SLM）从未被系统评测PED；常用PER/PFER与MDD的P/R/F1无法刻画检测+诊断的真实能力。

**模型架构：** 基准化评测管线（基于PRiSM工具包扩展）：每条语音由G2P得规范音素序列C、人工听写实实现序列U、模型预测序列Û，统一投影到CMU-39音素表（K词典/标准IPA），按hierarchical MDD框架在公共网格对齐，逐位置判TA/FR/FA/TR，TR再分正确诊断CD与诊断错误DE。评测8个PR模型（MultiIPA、W2V2P-LV60/XLSR53、ZIPA-CTC/NS、HuPER、PhoneticXeus、BabAR）、Azure发音评估、4个SLM（Gemini-3.8-Flash、GPT-Audio-1.5、Qwen2.5-Omni-7B、AF3），SLM以prompt输出JSON内空格分隔的CMU-39 IPA序列。

**核心创新：** (1)三个双标注核验的新型PED数据集：synthetic用Amazon Polly SSML <phoneme>标签从60个GFTA-3目标词注入1个替换/删除错误，经word/sentence/passage三级两轮复核保留361个匹配集合共1,083条；acted由3名受训母语者按脚本故意犯错并互审重录至零标记；儿童数据从199名3-7岁西英双语儿童3,574条录音中仅保留两标注者完全一致的334条。(2)诊断加权DW P/R/F1：以更严的CD替代标准MDD的TR作分子，检测与诊断皆对才计分，贴合教育临床反馈需求。(3)音素可控TTS的错误数据规模化配方：构造SW（396合成词）与SC（+154条匹配儿童真实错误类型的合成数据）语料，针对性覆盖下游已知的常见/罕见错误。

**训练策略：** SLM LoRA微调（Qwen2.5-Omni-7B/AF3）：r=16、α=32、dropout 0.05，加在Text-LM全部注意力q/k/v/o投影（112模块、10.1M可训练参数），音频编码器冻结；仅对答案token算交叉熵；AdamW（wd 0.01、lr 2e-4）、线性schedule带3% warmup、有效batch 16、bf16、单GPU、6 epochs，每epoch贪心解码dev取最低PER checkpoint。W2V2P-XLSR53全量CTC微调（lr 1e-5、warmup 10%、batch 4×4、5折CV）。TIMIT按Kaldi标准划分去SA句后3,696训/400 dev/192 test；seed=42。

### 📊 实验结果
**数据集**：L2-ARCTIC-Perceived（3,599句）、CMU-Kids（5,180句）+新型集：儿童334、acted 1,188、synthetic 1,083条

**主要指标**：
- L2-ARCTIC F1最高基线仅W2V2P-XLSR53的31.85；CMU-Kids最高ZIPA-CTC-NS 54.55（其PFER虽低至7.86但F1差，PFER不反映PED）
- 新型集最佳基线：儿童59.51（BabAR）、acted 76.17（GPT-Audio-1.5）、synthetic词级74.32（Azure）；随音频变长精度骤降，passage级最高F1仅14.22，误判正确音素为错误（FR偏高）普遍
- 微调后：Qwen+TIMIT+SW acted F1达90.06（较最强基线+13.89）、AF3+SW 88.83；儿童集Qwen+SC 63.47、AF3+SC 63.82超Gemini 58.26但远未可靠，存在sim-to-real与成人到儿童域差
- 错误集中于近音混淆：/θ/–/f/、/ʃ/–/tʃ/、/ɔ/–/ɑ/、/eɪ/–/ɪ/

**是否开源**：暂无；计划录用后开源代码、微调checkpoint与acted/synthetic数据，儿童数据因知情同意不公开，将作隐藏评测集支撑未来leaderboard。

### ⭐ 评分：7/10
评分理由：首个PED标准化基准，系统性揭示SOTA模型连受控条件下的简单音素错误都检测不可靠，领域价值明确。两级标注核验+自然-受控连续谱数据设计直击现有数据集标注噪声痛点，DW指标比标准MDD P/R更贴合应用，TTS可控造错+LoRA微调 recipe可复现性强。不足：数据规模小且仅英语词句级，微调模型在真实儿童语音仍不达标，方法层创新偏工程整合，属扎实的benchmark贡献而非技术突破。

---

## [4] High-Order Sinusoidal Modeling for Precise Parameter Refinement

**arXiv ID**：2610.21643 | **方向**：语音前端

**作者**：Shaowen Chen, Tomoki Toda

**机构**：名古屋大学（信息学研究科信息学专业、信息中心）

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.21643 | **PDF**：https://arxiv.org/pdf/2610.21643.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对正弦建模中初始频率失配导致准谐波模型（QHM/aQHM/eaQHM）幅度、频率、相位估计精度受限的问题，本文揭示QHM复斜率幅度模型仅是失配项e^{i2πηt}的一阶泰勒逼近，阶数不足是其误差根源。据此提出高阶正弦模型（High-Order SM），将失配项展开为N阶泰勒级数并以两个复系数(a_k,b_k)强制保持指数结构，用Levenberg–Marquardt算法做非线性最小二乘估计。仿真中4th-SM在μ=50Hz失配下SRER达38.8dB、幅度RMSE从QHM的19.3降至5.9；LJspeech上平均SRER 12.7dB、RTF 9.49，精度优于eaQHM（SRER约11.5dB）。

### 🔧 技术方案

**问题背景：** 信号参数提取精度受限于频率估计误差，谱图类方法受不确定性原理约束；QHM家族虽可在帧内用复幅度斜率修正频率失配，但其线性模型结构只能捕捉一阶失配，初始频率误差大时估计振荡甚至放大误差，且迭代式修正计算量大、对加性噪声敏感。

**模型架构：** 对K个良分隔正弦分量，N阶模型定义为 x^(N)(t)=[Σ_k a_k(Σ_{n=0}^N b_k^n t^n/n!)e^{i2πf̂_k t}]w(t)，即在窗内每分量用e^{b_k t}的泰勒截断逼近失配调制项，仅保留两自由复系数：a_k给出幅度Â_k=|a_k|与相位φ̂_k=∠a_k，b_k虚部给出频率失配η̂_k=ℑ{b_k}/2π。定理1给出最小二乘解形式，命题1证明估计误差以|2πη|^{N+1}/(N+1)!上界随阶数N衰减。帧间通过频率/幅度插值与正弦跳变相位修正项z重建瞬时轨迹。

**核心创新：** (1) 从泰勒展开视角重推QHM，指出其a_k+tb_k结构恰为失配项的一阶截断，从根本上解释大误差下修正失效的机理。(2) 提出高阶正弦模型：将N阶多项式各项系数按c_n=c_1^n/(n!·c_0^{n-1})约束成a·e^{bt}形式，把N+1个自由参数压缩为2个并保持指数结构对齐，兼顾表达力与噪声稳定性，优于无结构的一般高阶多项式模型(2nd-PM)。(3) 模型对b非线性使传统线性LS失效，推导显式解析Jacobian并用LM算法（阻尼因子λ按γ>1自适应调节，典型γ=10）迭代估计，可跨帧并行且避免自动微分开销。

**训练策略：** 纯估计方法、无训练。逐帧窗口内非线性最小二乘，LM固定少量迭代（通常8次）即收敛；帧初频率由谱峰/YAAPT给出。语音实验用LJspeech（22.05kHz），f0由YAAPT初始化，理论分析用Hamming窗、T=10ms。

### 📊 实验结果
**数据集**：6分量仿真相态信号（含线性/调频成分，幅度调制），两种场景：初始频率失配μ∈[10,80]Hz（20次Monte-Carlo，对比2/4/6阶SM）；叠加高斯白噪声SNR 1–20dB、μ=80Hz。真实语音：LJspeech随机32句。

**主要指标**：
- 仿真Case1（μ=50Hz）：4th-SM幅度RMSE 0.5–10.5（对比QHM 11.6–26.7），频率RMSE 0.2–3.9×10⁻³（对比QHM最高99.3×10⁻³），重建SRER 38.8dB为最高；噪声场景SNR15dB下4th-SM SRER 24.5dB，eaQHM因噪声幅度RMSE恶化至121.8
- 语音（表III）：Lspec×10⁻²为9.38，优于QHM 10.96、eaQHM 26.31；SRER 12.7dB vs QHM 8.8/eaQHM 11.5；RTF 9.49 vs eaQHM 25.49、QHM 4.39（单核i7-8700K）
- 阶数消融：6th-SM在各失配与噪声水平下误差最低，验证误差随N单调改善

**是否开源**：暂无（论文仅引用eaQHM基线开源实现，本文代码未发布）

### ⭐ 评分：7/10
评分理由：从泰勒展开角度统一解释QHM家族失配修正能力的天花板，理论动机清晰，并给出误差随阶数收缩的严格上界（定理/命题附证明），学术贡献扎实且有实用价值。实验覆盖仿真与真实语音、Monte-Carlo、阶数消融与噪声鲁棒性，指标一致占优，且RTF显著低于eaQHM。不足：仅与QHM家族比较，缺少与高阶同步压缩变换等基线的对比；语音评估依赖Lspec/SRER间接指标且只测32句；假设分量良分隔，未验证强噪声下F0跟踪等下游任务；无代码开源。总体是信号建模方向的实质性增量工作，值得QHM使用者关注。

---

## [5] Hear, Localize, and Reason: Spatially Aware Scene Understanding for Audio-Visual LLMs

**arXiv ID**：2610.21588 | **方向**：语音大模型

**作者**：Kim Sung-Bin, Lee Jung-Mok, Jinwoo Jung, Oh Hyun-Bin, Hyeonggon Ryu, David Harwath, Tae-Hyun Oh

**机构**：POSTECH, KAIST, Hankuk University of Foreign Studies, The University of Texas at Austin

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.21588 | **PDF**：https://arxiv.org/pdf/2610.21588.pdf | **代码**：https://hlrllm.github.io/ | **Demo**：https://hlrllm.github.io/

### 📌 简介
现有视听大模型把音频当单声道语义内容处理，难以定位声源并与视觉场景关联推理，且已有空间基准各自只覆盖零散子任务。本文提出 HLR-AVSceneQA 基准（12 任务、175k 训练/21.8k 测试 QA，按"听-定位-推理"三层级组织）与 HLR-LLM 模型：在 Qwen2.5-Omni 上增加双耳空间音频分支，并用三阶段课程训练加末端 CoT 监督。HLR-LLM 自我中心方向定位达 78.21%（对比最强微调基线双通道 Qwen2.5-Omni 64.27%），关系推理五任务全面最优，STARSS23 真实数据上方向准确率 29.92% 显著领先。

### 🔧 技术方案

**问题背景：** AV-LLM 普遍以单声道音频输入，只关注"听到什么"而非"从哪听到"，面对离屏、遮挡、跨房间声源无法定位与推理；同时现有空间视听基准（BAT、SAVVY-Bench、SpatialSceneQA、Hear You Are）评估维度碎片化，且训练多用直接答案监督，缺乏对多步空间推理的结构化支持。

**模型架构：** HLR-LLM 基于 Qwen2.5-Omni（保留视觉编码器与单声道音频编码器作语义通路），新增空间音频分支：冻结的 BAT 预训练双耳空间音频编码器 f_spa 提取特征，经可训练 MLP 投影器 p_spa 映射到 LLM 嵌入空间；引入新媒体 token <spatial_audio>，输入序列为文本、视觉、单声道音频与空间音频 token 拼接，由 LLM 自回归生成答案。

**核心创新：** (1) HLR-AVSceneQA 基准：基于 SoundSpaces 2.0 声学仿真与 HM3DSem 场景（145 训练/36 测试房间），插入 Objaverse-XL 及生成式补强的 3D 网格，渲染 90° FOV、1280×720 RGB 与 32 kHz 双耳音频，导出结构化元数据自动生成 12 类任务 QA，覆盖自我/他心视角定位、可见性、音画对应、隐藏源定位、响度变化等，且用普通 FOV 而非全景图迫使模型处理离屏与遮挡源。(2) 双通路空间音频建模：单声道分支管语义、双耳分支管方位距离，明确注入空间声学 token，区别于简单把左右声道分别当两路单声道输入的做法。(3) 课程化 CoT 监督：由仿真元数据模板确定性生成含声事件、方位、距离、可见性检查等中间线索的推理链（94,519 条），在指令微调后单独做第三阶段 CoT tuning。

**训练策略：** 各阶段最小化答案 token 自回归交叉熵。Stage1 仅训空间投影器（BAT 空间音频 QA 514k）；Stage2 冻结全部编码器，LoRA 微调 LLM + 更新投影器（HLR-AVSceneQA 175k）；Stage3 CoT 数据 94.5k。LoRA rank 16/alpha 16/dropout 0.05，应用于全部线性层并用 LoRA+；lr 2e-4，weight decay 0.01，warmup 0.05，梯度裁剪 1.0，bfloat16 + FlashAttention，2 epochs，4×A6000，per-device batch 4、梯度累积 4。

### 📊 实验结果
**数据集**：HLR-AVSceneQA（175,061 训练 / 21,808 测试 QA；多源场景 53,279/4,869；CoT 94,519），真实域迁移用 STARSS23

**主要指标**：
- 自我中心方向/距离定位：78.21% / 55.56%，较双通道 Qwen2.5-Omni（64.27/46.59）提升 13.94 / 8.97 个百分点；他心方向/距离 52.03% / 45.08%
- 空间关系推理全最优：可见性 80.51、对应 76.19、隐藏源 67.23、响度变化 80.87、邻近 61.50；SPIDEr 3.109
- 语义保留：声音事件 81.03%、远场 WER 14.43%，略逊纯单声道微调基线；STARSS23 上预训练带来方向 16.13→29.92% 大幅提升

**是否开源**：代码与基准数据通过项目页 https://hlrllm.github.io/ 释出

### ⭐ 评分：7/10
评分理由：统一"hear-localize-reason"层级的 12 任务基准填补了空间视听评估碎片化的空白，模拟器+元数据自动 QA 构造可控且规模化，双分支架构消融（去视觉/去双耳/CoT 联合 vs 分阶段）设计干净，增益显著。不足：全程依赖仿真数据，双耳距离线索与真实录音差异大（STARSS23 绝对性能仍低，方向仅 29.9%），声音识别略被空间通路挤占；基准与模型同作者构建，测试集多样性受限于 HM3DSem 室内场景。作为基准+强基线的组合贡献扎实，具较强参考价值。

---

## [6] Qwen-Audio-Jev: A Unified Interface for Audio Decisions

**arXiv ID**：2610.21614 | **方向**：语音大模型

**作者**：Ying Fang, Zhifu Gao, Qing Gu, Jiajun He, Kangqi Jing, Xiangang Li, Yu Pu, Wupeng Wang

**机构**：Token Foundry, Alibaba Group

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.21614 | **PDF**：https://arxiv.org/pdf/2610.21614.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
大型音频语言模型在音频理解上进展显著，但高吞吐场景下的选择、判断、打分任务若依赖自回归文本生成，会带来额外算力和延迟。本文在Qwen-Audio-3.1-ASR-Flash-Next骨干上添加Jev决策头，统一三种决策原语：Choice（候选分布）、Noul（二值命题概率）、Score（有序等级期望分），从题目前缀的pre-answer隐状态直接仿射读出类型化概率。训练采用异构监督SFT（缺失标注不计损失）加面向校准的RLCD阶段（Brier/RPS组奖励+策略梯度）。在18个标注配置上，MMAU-mini 78.70%、MMSU 84.06%，VoxCeleb1-O EER 6.50%，NISQA总体质量nMAE 0.1062、Pearson 0.8210，推理较原骨干提速约20倍。

### 🔧 技术方案

**问题背景：** 高吞吐音频应用（大规模筛选、说话人验证、质量评估）的输出是有界决策（类别/二值/评分），LALM的自回归生成不仅有算力与延迟开销，还需解析校验文本才能被下游消费；现有直接决策方法（如AudioJev）仅覆盖Choice，缺乏统一的三原语接口与校准训练。

**模型架构：** 继承骨干的音频编码器Eθ+音频-语言适配器Aθ+MoE语言解码器（40层、hidden 2048、256路由专家、每token选8个）。将音频、自然语言问题与答案规格(q,c)序列化融合进解码器，取问题前缀最后token的pre-answer隐状态h★（因果掩码防止标签泄漏），接三个仿射读出头：W_C∈R^(64×2048)、W_N∈R^(1×2048)、W_S∈R^(10×2048)，Choice/Score仅对有效候选或等级位置做softmax，输出类型化概率或期望分。

**核心创新：** (1) 统一类型化决策接口：Choice/Score采用固定容量索引投影，索引语义由问题附带的答案规格动态定义而非全局固定类别表，候选少于上限时只归一化有效logit，支持2-64个候选与2-10个等级的任意任务。(2) 异构监督统一表征：将全部数据组织为audio-question-criteria-target格式，每条样本只对其有标注的原语计算损失，使MELD、VoxCeleb等标注方案迥异的数据集无需全量重复标注即可联合训练SFT。(3) RLCD校准训练：把单次决策建模为一步上下文赌博机，从探索策略（ε=0.05混合均匀分布）采样M=32个动作，用严格proper评分规则（Brier/RPS）构造可无偏估计的组奖励，配leave-one-out基线的sampled-action reinforce，显式优化概率校准而非仅准确率。

**训练策略：** SFT联合优化编码器、适配器、骨干与决策头；Score损失=CE+0.25·CDF项+0.10·SmoothL1期望值项；Noul用BCE（支持软标签）；Choice用类别交叉熵并随机置换候选顺序作增强；总目标含MoE load-balancing与router z-loss辅助项。RLCD从SFT检查点初始化做策略梯度。论文未披露学习率、batch size、训练轮数与数据规模等具体数值（仅说明按实验配置提供），亦无next-token目标。

### 📊 实验结果
**数据集**：18个标注配置——Choice 8项（CochlScene、NSynth、NonSpeech7k、DiDiSpeech、MELD、MMAU、MMSU、MMAR）；Noul 4项（VoxCeleb1-O、Clotho-AQA、PodSarc、In-the-Wild深伪检测）；Score 6项（NISQA五维、VoiceMOS/BVCC）

**主要指标**：
- Choice：MMSU 84.06%、MMAU 78.70%、MMAR 69.90%、NonSpeech7k 92.69%、DiDiSpeech性别100%、MELD情绪仅57.31%
- Noul：VoxCeleb1-O EER 6.50%、AUC 0.9823、准确率93.54%、Brier 0.0487；PodSarc EER 1.44%；In-the-Wild AUC 0.8763但0.5阈值下FNR高达57.29%
- Score：NISQA overall nMAE 0.1062（MOS MAE 0.4246）、Pearson 0.8210/Spearman 0.8074；VoiceMOS nMAE 0.2034、Pearson 0.7231
- 关键对比：与原始Qwen-Audio-3.1-ASR-Flash-Next相比推理约20倍加速；但未提供与其他LALM/专用模型的同口径任务精度对比，论文自认对比增益与校准需进一步评估

**是否开源**：暂无（论文未给出代码/模型发布链接）

### ⭐ 评分：6/10
评分理由：将Jev类型化决策接口扩展为Choice/Noul/Score三原语并落在生产级MoE音频骨干上，问题动机明确、工程价值实在，20倍加速对高吞吐筛选场景有实际意义；RLCD部分以严格proper评分规则推导无偏组奖励，方法上严谨。但实验仅18个配置自测，缺少与SOTA LALM及传统专用模型（如SV、DNSMOS类）的横向基线，训练关键超参均未披露，可复现性差；MELD 57.3%、In-the-Wild漏检57.3%、VoiceMOS MAE 0.81等暴露泛化短板。属有参考价值的增量系统工作，距实质突破尚有距离。

---

## [7] CF-AVSS: A Coarse-to-Fine Audio-Visual Speech Separation Framework with Target-Speaker Refinement and Post-Fusion for Real-World AVSE Challenge

**arXiv ID**：2610.21773 | **方向**：语音前端

**作者**：Longjie Luo, Zhongshu Hou, Yuepeng Li, Gang Yang, Shidong Shang, Fan Zhou

**机构**：Tencent Ethereal Audio Lab（腾讯）；电子科技大学（UESTC）

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.21773 | **PDF**：https://arxiv.org/pdf/2610.21773.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对真实场景 AVSE 中混响、噪声、重叠说话及视觉质量退化导致一步增强易损伤目标语音的问题，提出粗到细两阶段框架：先用渐进式双视觉流 SPAV-TFGridNet 生成保留目标混响与共享噪声的粗分离结果，再以 TFGridNet 目标说话人精化工序从原始混合信号恢复更干净目标，最后经开发集校准的线性融合输出。该方法在 ISCSLP 2026 Real-World AVSE Challenge 中 Track1 并列第一、Track2 第二（OVRL 2.86），两赛道 CER 均最优（12.31%/14.79%）。

### 🔧 技术方案

**问题背景：** 真实会议场景中混响、噪声源与说话人数目远超训练假设，一步增强若过度抑制会误伤目标语音（混响、弱音素），而竞赛常见的单阶段 AVSE 管线难以同时兼顾目标保真与干扰消除。

**模型架构：** 两阶段级联：Stage1 粗分离采用 SIR-Progressive AV-TFGridNet，混合信号经 Conv2D 编码后由 K 个级联 AVTFGrid 块（TFGrid 块+两个 FAVA 视觉注意力）处理双视频流，逐层解码输出两个按视觉流绑定、避免置换歧义的粗估计；Stage2 精化用 TFGridNet-TSR，以混合 y 与两个粗估计为输入，经上下文编码器拼接、TFGrid 块与 Deconv2D 解码出精细估计，再线性融合。视觉前端用 AV-HuBERT 官方预处理（68 关键点、嘴部 ROI）+ AV-HuBERT Base 提取 25fps 视觉特征。

**核心创新：** (1) 将单输出的 SPAV-TFGridNet 扩展为两个视觉有序输出，渐进监督按 SIR 调度 {0,5,10,15}dB 逐级消干扰，粗目标 c_i=u_i+n 刻意保留目标房间响应与共享背景噪声，不做 s_c1+s_c2=y 的一致性约束，避免过度抑制弱目标音素。(2) 上下文 TSR 复用原始混合与粗估计双线索：混合提供被粗阶段削弱的目标成分，粗估计锚定说话人身份，配不对称欠抑制损失（仅惩罚活跃 TF bin 上的目标幅值缺失）+可微 PESQ 损失+PASE 时频双判别器对抗。(3) 开发集标定的单一全局融合系数 α=0.34，对粗/精两路互补输出做线性合并，测试期不做句级自适应调参。

**训练策略：** 用 VoxCeleb2+MISP2023 构造混合：采样 M∈{2,3,4} 说话人（0.75/0.20/0.05），两人出镜、其余画外干扰；各源独立卷积 OpenSLR SLR26/SLR28 的 16kHz RIR，叠噪后裁成同步 4s 段。Track2 训练加随机视觉退化（空间掩码、高斯模糊、丢帧，视觉模态丢弃率 0.1）。AVSS/TSR 各训 50 epoch，AdamW，lr 1e-3，weight decay 1e-4，batch 8；λ_s=λ_c=1.0，μ_o=0.1、μ_p=0.05、μ_a=0.01、μ_f=0.1。

### 📊 实验结果
**数据集**：ISCSLP 2026 Real-World AVSE Challenge（开发集 Track1 1242 mix+900 remix，Track2 1527+1098；测试集 Track1 4257、Track2 4941 条，16kHz）

**主要指标**：
- Track1（mix+remix）：SI-SDR 10.70、PESQ 2.93、STOI 0.84、UTMOS 2.07、DNS-OVRL 1.83、CER 12.31%、SPK-SIM 0.75、OVRL 2.86（并列第一）
- Track2：SI-SDR 10.22、PESQ 2.89、STOI 0.83、CER 14.79%、SPK-SIM 0.74、OVRL 2.86（第二）
- 关键对比：CER 两赛道均为全场最低，较次优对手（Track1 Team1 14.5%）降约 2.2 个百分点；Track2 较第一名胜者 Team1（CER 15.3%）低 0.5 个点。消融显示 TSR 使 DNS-OVRL 由 1.56→2.20 但伤 SI-SDR/PESQ，融合后兼得最优 SI-SDR、CER、SPK-SIM。

**是否开源**：暂无

### ⭐ 评分：6/10
评分理由：系统面向真实挑战赛的工程整合度高，渐进粗分离保混响/保噪声、TSR 补回目标成分、α=0.34 融合三者形成清晰的"互补观测"设计思路，双赛道 CER 最优且 Track1 并列第一，结果有说服力。但单模块多为既有工作（SIR-Progressive、TFGridNet、FAVA、PASE）的组合与扩展，方法学创新属增量级；消融较简略且仅在 Track2 dev-set 做，未对视觉退化策略、粗估计数量、判别器贡献逐一验证，α 全局固定也略显粗糙。作为竞赛技术报告实用参考价值高，适合作真实 AVSE 基线参考。

---

## [8] Rethinking Batch Composition: Promoting Feature Diversity for Speech Enhancement

**arXiv ID**：2610.21803 | **方向**：语音前端

**作者**：Mingchi Hou, Ina Kodrasi

**机构**：Idiap Research Institute, Switzerland; EPFL, Switzerland

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.21803 | **PDF**：https://arxiv.org/pdf/2610.21803.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
语音增强训练普遍采用随机采样的 mini-batch，而单个 batch 内干净语音的内在声学特征多样性可能不足；已有研究表明干净语音特征（如共振峰结构、响度）与增强难度强相关。本文提出特征分层 mini-batch 采样：对每条训练语音用 openSMILE 提取一个干净语音特征，按经验分布划分若干分位区间，每个 batch 从各区间等量抽取样本，形成即插即用的采样策略，不改动模型与损失。在英语 WSJ0、西语 CROWD 及含帕金森病理语音的 PC-GITA 上，判别式（CR）与生成式（Schrödinger Bridge, SB）模型均有改善，如 WSJ0-CR 的 fwSSNR 由 5.16 升至 6.17、E-STOI 由 0.25 升至 0.32，且分层维度需与增强难度相关才有效。

### 🔧 技术方案

**问题背景：** 现有 SE 鲁棒性工作多针对噪声类型、SNR 或说话人条件，但即使这些条件固定，不同语音样本的增强难度仍差异显著。作者前期研究证实干净语音内在特征（如第三共振峰、响度）与增强性能强相关，而随机采样使单个 batch 仅覆盖声学特征空间的狭窄区域，梯度更新被局部难度范围主导，且该因素从未被纳入训练策略设计。

**模型架构：** 方法本身仅为数据采样层改造，以自定义 sampler 实现：训练前一次性提取每条语音特征 f(si)，将训练集分为 J 个分位（要求 B 可被 J 整除），每个 batch 从每层无放回抽 B/J 条、跨 epoch 重洗，分位边界固定且特征不输入模型。验证宿主模型为两类 SOTA：CR 判别式复谱回归模型与 SB 生成式薛定谔桥模型，均基于 NCSN++M U-Net（去掉/保留噪声条件层，分别 22.1M/25.2M 参数）；STFT 窗长 510、hop 128、Hann 窗、α=0.5/β=0.33 压缩；SB 用 VE 调度 σmin=0.7、σmax=1.82、EMA 0.999、50 步 SDE 采样。

**核心创新：** (1) 特征分层 batch 采样：首次将干净语音内在特征分布纳入 SE 训练采样设计，主实验以 F3 均值分层（B=8、J=4），零模型改动、几乎零额外算力，与任何损失/架构互补。(2) 揭示分层收益的条件性：对比 F3（与增强难度强相关）与 f0 标准差（与性能几乎无关），仅前者带来 E-STOI/fwSSNR 明显增益，说明有效性并非泛泛的"batch 更多样"，而是沿难度相关维度引入多样性。(3) 跨范式/语种/人群的系统验证与稳健性检验：判别式与生成式、英/西语、神经典型与病理语音上一致改善，并以 3 个随机种子证明收益对 batch 组成的随机扰动稳健。

**训练策略：** Adam，lr 1e-4，最多 1000 epoch，验证损失 20 epoch 无下降早停；噪声混合采用 CHiME3 四类环境噪声（bus/cafe/pedestrian/street），SNR 均匀采样 -6 至 14 dB，全部 16 kHz。WSJ0 标准划分（101/10/8 说话人，28.6h），CROWD 截取与 WSJ0 时长和说话人数匹配的子集，PC-GITA（2.8h，50 帕金森+50 对照）用说话人独立 10 折交叉验证（80/10/10）。WSJ0/CROWD 用 H100，PC-GITA 用 RTX 3090；评价指标为相对带噪的 ΔE-STOI、ΔPESQ、ΔfwSSNR、ΔSI-SDR。

### 📊 实验结果
**数据集**：WSJ0（英语，28.6h/120 人）、CROWD（拉美西语，匹配 WSJ0 规模子集）、PC-GITA（西语帕金森病理语音，2.8h/100 人）；噪声为 CHiME3 四类环境噪声，SNR -6~14 dB，16 kHz

**主要指标**（均值±95%CI，Δ 表示相对带噪改善）：
- WSJ0+CR：ΔE-STOI 0.25±0.01→0.32±0.01（+0.07），ΔfwSSNR 5.16→6.17（+1.01），ΔPESQ 1.42→1.48，ΔSI-SDR 11.81→11.95
- WSJ0+SB：ΔSI-SDR 10.59→10.99（+0.40），ΔfwSSNR 6.13→6.32；CROWD+SB：ΔSI-SDR 8.71→10.66（+1.95，本文最大单项增益），ΔfwSSNR 5.42→6.33
- PC-GITA 病理语音+CR：ΔE-STOI 0.14→0.19、ΔfwSSNR 5.18→5.62；3 种子复验：ΔPESQ 1.49 vs 随机 1.40；f0 标准差分层无增益（ΔE-STOI 0.25）
- 关键对比：分层采样在最强基线"随机采样"之上全面持平或提升，增益幅度依数据集/模型/指标而异

**是否开源**：暂无（论文未提供代码仓库链接）

### ⭐ 评分：6/10
评分理由：切入点真实且此前被忽视——batch 内干净语音特征分布影响训练，方法即插即用、零额外成本，工程上可直接落地到现有 SE 训练管线，这是其实用价值所在。消融显示"仅难度相关维度分层才有效"是有洞察的结论，跨语种、跨范式、跨病理人群的验证较系统。局限在于：增益幅度普遍偏小且无主观听感评估，batch size 与分位数等关键超参未扫描，仅单种子主实验（稳健性检验只覆盖 WSJ0+CR），未与 hard-example mining、课程学习等采样策略直接对比，创新偏训练技巧而非方法突破，属于有参考价值的增量贡献。

---

## [9] Bias Mitigation in Audio-Enabled LLMs through Adversarial Training and Distillation Methods

**arXiv ID**：2610.21763 | **方向**：语音大模型

**作者**：Adnan Al Ali, Jindřich Libovický, Anne Lauscher

**机构**：Charles University, Faculty of Mathematics and Physics（捷克）；Trustworthy AI Lab, University of Hamburg（德国）

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.21763 | **PDF**：https://arxiv.org/pdf/2610.21763.pdf | **代码**：https://github.com/adnan-al-ali/speech-llm-bias-mitigation/ | **Demo**：https://hf.co/alalia/speech-bias-mitigation/（模型权重）

### 📌 简介
音频大模型（AuLLM）直接从语音编码副语言线索推断性别等属性，导致对相同内容的女声/男声输出刻板化偏见回答，但其缓解方法几乎无人研究。本文提出两阶段方法：先用梯度反转层（GRL）对抗训练音频编码器生成"性别无感知模型"（GUM），再将原模型与GUM的logits混合蒸馏出保留性别感知但去偏的LoRA模型。在Qwen2-Audio-7B、Qwen3-Omni-30B、Nemotron-3-Nano-Omni三个模型上，性别检测准确率从81.5%-99.9%降到随机水平（46%-54.5%），偏见LOR最高从0.40降至0.10，通用音频理解mmau损失小于4%。

### 🔧 技术方案

**问题背景：** Holtermann等（2026）已证实AuLLM会基于音色产出性别刻板输出，但缓解几乎空白；先前唯一方案是修改基频（pitch），论文复现确认其会破坏音高检测、声音识别等下游能力，且无法彻底消除性别感知，故需属性级"机器遗忘"方案。

**模型架构：** 针对三种编码器（Whisper、AuT、Parakeet）各<1B参数的音频编码器：冻结LLM主干，仅全量微调编码器；编码器末尾表征mean-pool成d_encoder向量，经GRL（梯度乘-α）接二分类性别头。蒸馏阶段则用LoRA（rank 16/32）只作用于decoder全部注意力权重，学生模型同时拟合教师（原模型生成的sift-50m^M）与GUM（ImpGender上生成）两套logits。

**核心创新：** (1) 将文本模型的对抗去偏迁移到AuLLM：仅攻击编码器输出中的性别子空间，联合损失L=L_gender+γ·L_LM防止灾难遗忘；因sift-50m含诱导性别检测的样本，先按关键词过滤出sift-50m-neuter避免干扰遗忘目标。(2) 选择性checkpoint机制：网格搜索48组超参，只取性别检测<60%中mmau最高者，且指出必须定性分析（Qwen3-Omni靠95.5%恒定答"F"作弊达标）。(3) 双教师logits蒸馏：以原模型保留能力、GUM提供无偏行为，KL散度按样本长度归一化，得到"能感知性别但除非明确询问不作差异化回答"的折中模型。

**训练策略：** 对抗阶段：4000条性别均衡样本、1 epoch、constant LR、有效batch size=8、AdamW、weight decay=5e-3，每125步存checkpoint；搜索空间LR∈{5e-6~1e-4}、γ∈{0.5,1,2}、α∈{0.025~0.2}。蒸馏阶段：每数据集4000条共8000样本（剔除>150MB异常logits），LoRA dropout=0.05、alpha=2×rank，1 epoch、每80步checkpoint，1 epoch约2小时，用A40/L40/H100训练，推理用vLLM。

### 📊 实验结果
**数据集**：British Dialects(500)+Speech Archive(470)做性别检测/偏见评测（23280条recording-prompt对，LOR指标）；自建ImpGender（34模板×VCTK 240录音=8160条）；mmau(908条neuter子集)测通用音频理解；misgend测误性别化率

**主要指标**：
- 性别检测：三模型绝对acc降至46.0/54.5/50.8%，接近随机（基线81.5/99.9/96.4%）
- 偏见LOR：0.40→0.10、0.24→0.10、0.25→0.18（GUM）；蒸馏后0.23/0.22/0.21
- mmau：最高仅降3.7个百分点（75.0→71.3），Qwen2-Audio反而提升4.5
- 蒸馏对比：86.3%（Qwen3-Omni）与83.8%（Nemotron）的checkpoint偏见比原模型更严重，仅Qwen2-Audio LOR显著下降（0.40→0.23）

**是否开源**：代码与模型已开源（GitHub + HuggingFace），新基准数据亦公开

### ⭐ 评分：6/10
评分理由：这是首篇系统研究AuLLM属性偏见缓解的工作，问题真实且方法（GRL对抗+双教师蒸馏）工程上可复现，小数据量（4k样本）即达随机化遗忘，实用性强。定性揭示checkpoint作弊与mmau评测盲区是有价值的洞察。但蒸馏阶段仅边际改善、多数checkpoint反而加重偏见，核心贡献一半未兑现；评测局限于英语、二元性别、合成prompt场景，无真实对话验证。属方法论扎实的增量探索，适合关注音频模型安全的团队参考。
