# 语音论文速递 2026-08-05

## 📌 本期亮点

- **MeloCodec**：利用旋律先验的高保真歌唱声音表示学习，提出 Tokenize-then-Fuse 范式
- **DAIEN-TTS**：环境感知零样本 TTS，解耦语音、环境噪声和混响
- **GROW**：流匹配 TTS 的on-policy强化学习方法，WER 从 2.016 降至 1.558

---

## 🔧 语音合成 (TTS)

### 1. MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation

📝 **作者**：Yizhong Geng, Wenxin Fu, Kecan Mao 等  
🏫 **机构**：待补充  
📰 **arXiv**：2608.03021

**核心方法**：
- **Tokenize-then-Fuse 范式**：预训练独立的离散旋律分支来锁定结构，再进行特征融合，解决直接融合导致的优化不稳定问题
- **两阶段训练策略**：防止码本坍塌，确保稳定收敛
- **旋律先验整合**：将关键的旋律信息（音高、节奏）融入音频编码器

**实验结果**：
- 在歌唱声音表示上优于基线
- 提升音高一致性，支持可控的音高操控
- 最小化音色退化

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：首个将旋律先验显式整合到神经音频编码器的工作，对 LLM 音频生成有重要意义

---

### 2. GROW: Group-Relative Advantage-Weighted On-Policy RL of Autoregressive-Diffusion TTS

📝 **作者**：Guanrou Yang, Tian Tan, Qian Chen 等（上海交通大学）  
🏫 **机构**：上海交通大学  
📰 **arXiv**：2608.03215

**核心方法**：
- **群组相对优势加权**：对每个 prompt 采样一组 on-policy  utterances，在组内标准化可懂度和说话人相似度奖励
- **Wasserstein-2 速度惩罚**：将更新后的模型锚定到冻结的预训练参考模型
- **群组均值奖励基线**：将奖励加权转化为优势加权
- **零均值符号优势**：保留有效的组内信用分配

**实验结果**：
- LibriSpeech 和 Seed-TTS EN/ZH 上评估
- 平均 WER：从 2.016 降至 1.558
- 说话人相似度：从 0.676 提升至 0.715
- 保持 UTMOS 不变
- 10-NFE 训练rollout，训练速度比 32-NFE DiTAR-GRPO 快 2.9 倍

**⭐ 评分**：⭐⭐⭐⭐⭐  
**推荐理由**：创新性地将强化学习直接应用于流匹配目标，解决 ODE 采样难题，显著提升 TTS 质量

---

### 3. DAIEN-TTS: Real-world Environment-aware Zero-shot TTS via Disentangled Audio Infilling

📝 **作者**：Ye-Xin Lu, Xin Wang, Yang Ai 等（中国科学技术大学、NII）  
🏫 **机构**：中国科学技术大学、NII 日本  
📰 **arXiv**：2608.03011

**核心方法**：
- **语音-环境分离模块**：将环境语音分解为语音、噪声和混响分量
- **流匹配 F5-TTS 为基础**： Diffusion Transformer 进行环境感知生成
- **三重 Classifier-free Guidance**：细粒度控制语音、噪声和混响
- **信噪比适配策略**：将合成语音与环境 prompt 对齐

**实验结果**：
- 模拟和真实测试集上均表现优异
- 高自然度、强说话人相似度
- 忠实的噪声和混响重现
- 超越以往环境感知 TTS 系统的可控性

**⭐ 评分**：⭐⭐⭐⭐⭐  
**推荐理由**：首次实现真实环境下的零样本 TTS，解决环境信息剥离/纠缠问题

---

### 4. dots.tts.edit: Precisely Controlled Speech Editing with a Continuous Autoregressive Model

📝 **作者**：Hankun Wang, Bohan Li, Shi Lian 等（上海交通大学、思邻科技）  
🏫 **机构**：上海交通大学、思邻科技  
📰 **arXiv**：2608.02673

**核心方法**：
- **结构化编辑指令**：基于转录本的 XML 风格标签，明确指定操作类型并定位到转录本片段
- **语义时间线**：避免显式时间戳对齐，提供可检查的组合编辑契约
- **四类编辑控制**：词汇内容、情感表达、语调和语速、时间节奏
- **doteBench 评估套件**：双语评估，衡量指令遵循、局部保留和音频质量

**实验结果**：
- 五个编辑类别上领先的指令遵循和局部保留
- 音频质量与现有开源系统相当
- Seed-TTS-Eval 上与基础模型零样本 TTS 识别错误率和说话人相似度几乎无差异

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：创新的精确语音编辑接口，推动语音内容创作效率

---

## 📊 语音识别 / 音频理解

### 5. Efficient Audio Enhancement with a Differentiable Psychoacoustic Loss

📝 **作者**：Wallace Abreu, Bernardo V. Miranda, Luiz W. P. Biscainho  
🏫 **机构**：待补充  
📰 **arXiv**：2608.02918

**核心方法**：
- **AEROMamba_P**：将 AERO 超分辨率架构中的 attention 和 LSTM 替换为 Mamba 状态空间模型
- **可微分心理声学损失**：基于 PAQM (Perceptual Audio Quality Measure) 设计的感知损失
- **AEROMamba_PS**：针对 MP3 32kbps 压缩音频的增强版本

**实验结果**：
- 训练时 GPU 内存减少 2-4 倍
- 推理速度提升 14 倍，仅使用 1/5 GPU 内存
- 钢琴数据集和 MUSDB18 从 11.025kHz 上采样到 44.1kHz，感知质量比 AERO 提升 15%
- MP3 恢复质量提升 52%

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：状态空间模型在音频增强中的应用，效率提升显著

---

### 6. Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning

📝 **作者**：Fangxu Yu, Tao Feng, Dehai Min 等  
🏫 **机构**：待补充  
📰 **arXiv**：2608.02831  
🔗 **项目主页**：https://audiorubrics.github.io

**核心方法**：
- **AudioRubrics**：自我进化的音频锚定评分奖励框架
- **样本级评分标准合成**：从原始波形生成每样本评分规则
- **条件重采样和重加权**：基于模型自身 rollouts 动态调整评分标准
- **连续学习信号**：持续针对当前策略弱点

**实验结果**：
- 三个音频推理基准显著优于开源和训练基线
- 收益随评分生成器和判断器能力提升而扩展
- 收敛到稳定的推理长度，避免退化崩溃和无界增长
- 音频感知提升证明声学证据锚定的有效性

**⭐ 评分**：⭐⭐⭐⭐⭐  
**推荐理由**：创新性地将 RL 评分规则与音频证据结合，推动音频推理能力

---

## 📡 其他语音相关

### 7. DDSynth-RL: Audio Synthesizer Inversion via Discrete Diffusion with RL

📝 **arXiv**：2608.03032

**核心方法**：离散扩散模型结合强化学习进行音频合成器反转

**⭐ 评分**：⭐⭐⭐

---

### 8. Language-Specialized Multi-Teacher On-Policy Distillation for Multilingual LLM-based ASR

📝 **arXiv**：2608.03610

**核心方法**：多语言 LLM-ASR 的多教师策略蒸馏

**⭐ 评分**：⭐⭐⭐

---

### 9. Speaker Verification Under Real Classroom Conditions

📝 **arXiv**：2608.03623

**核心方法**：真实教室环境下的说话人验证

**⭐ 评分**：⭐⭐⭐

---

## 📊 统计数据

- **今日语音相关论文**：约 40+ 篇
- **精读推荐**：9 篇
- **语音合成 (TTS)**：4 篇
- **语音识别/增强**：5 篇

---

*今日语音论文速递*
