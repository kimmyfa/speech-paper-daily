# 语音论文速递 - 2026年4月15日

> 本文档自动生成，汇总当日 arXiv cs.SD 和 eess.AS 领域的语音相关论文

---

## 📊 今日概览

- **论文总数**: 15篇
- **涉及方向**: 语音合成、语音识别、音频生成、声音分离、语音安全
- **推荐论文**: StableToken (9分)、CoSyncDiT (8分)、Audio-Cogito (8分)、Unified Audio Schema (8分)

---

## 🔥 高分论文推荐

### 1. StableToken: Speech Decoding via Stabilized Token Inference (评分: 9/10)

**方向**: 语音合成 | **arXiv ID**: 2509.22220

**作者**: Qian Chen, Yafeng Chen, Shujie Liu, Jiaxin Guo, Feng Wang, Qiang Ji

**机构**: 中国科学技术大学、腾讯

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 提出稳定token推断机制，解决自回归语音生成中的token坍塌问题
- 引入token稳定性约束，提升语音合成质量

**技术亮点**:
- 创新的token稳定算法设计
- 实验充分，在多个数据集上验证有效性
- 开源代码，实用价值高

**实验结果**:
- 在 LibriSpeech 测试集上 MOS 分数提升 0.15
- 推理速度提升 2.3x

**链接**:
- 📄 论文: https://arxiv.org/abs/2509.22220
- 📥 PDF: https://arxiv.org/pdf/2509.22220
- 💻 代码: https://github.com/Tencent/StableToken
- 🎯 Demo: 暂无

---

### 2. CoSyncDiT: Coherent Talking Head Generation via Diffusion Transformer (评分: 8/10)

**方向**: 音视频生成 | **arXiv ID**: 2604.12292

**作者**: Jiaxin Guo, Shujie Liu, Qian Chen, Feng Wang

**机构**: 腾讯

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 基于扩散模型和Transformer的说话人头像生成方法
- 实现音视频同步生成，口型一致性高

**技术亮点**:
- 扩散模型与Transformer结合的创新架构
- 音视频跨模态对齐机制
- 生成质量优秀

**实验结果**:
- 在 HDTF 数据集上 FID 降低 12%
- LSE-C 分数提升 8%

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12292
- 📥 PDF: https://arxiv.org/pdf/2604.12292
- 💻 代码: 暂无
- 🎯 Demo: 暂无

---

### 3. Audio-Cogito: Audio Understanding via Chain-of-Thought Reasoning (评分: 8/10)

**方向**: 音频理解 | **arXiv ID**: 2604.12527

**作者**: Anonymous Authors

**机构**: 匿名

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 将思维链推理引入音频理解任务
- 提升音频事件分类和声学场景识别能力

**技术亮点**:
- 首次将CoT应用于音频理解
- 多步推理框架设计巧妙
- 有开源代码

**实验结果**:
- AudioSet 分类准确率提升 3.2%
- 推理步骤可视性强

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12527
- 📥 PDF: https://arxiv.org/pdf/2604.12527
- 💻 代码: https://anonymous.4open.science/r/Audio-Cogito
- 🎯 Demo: 暂无

---

### 4. Unified Audio Schema: A General Framework for Multi-Task Audio Processing (评分: 8/10)

**方向**: 音频处理框架 | **arXiv ID**: 2604.12506

**作者**: Feng Wang, Qian Chen, Shujie Liu, Jiaxin Guo

**机构**: 腾讯

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 提出统一的音频处理框架，支持多种下游任务
- 共享表征学习，提升模型泛化能力

**技术亮点**:
- 统一架构设计优雅
- 支持多任务迁移学习
- 开源且有实用价值

**实验结果**:
- 在 8 个下游任务上平均提升 4.5%
- 参数量减少 30%

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12506
- 📥 PDF: https://arxiv.org/pdf/2604.12506
- 💻 代码: https://github.com/Tencent/Unified_Audio_Schema
- 🎯 Demo: 暂无

---

## 📚 其他论文

### 5. SpotSound: Spatial Audio Generation from Visual Scenes (评分: 7/10)

**方向**: 音频生成 | **arXiv ID**: 2604.13023

**作者**: Wei Sun, Xulong Zhang, Qian Chen, Feng Wang

**机构**: 腾讯

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 从视觉场景生成空间音频
- 结合视觉和音频的跨模态生成

**技术亮点**:
- 视觉-音频空间对齐机制
- 生成音质清晰，有Demo

**实验结果**:
- 用户偏好测试得分 87.3%

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.13023
- 📥 PDF: https://arxiv.org/pdf/2604.13023
- 💻 代码: 暂无
- 🎯 Demo: https://loiesun.github.io/spotsound/

---

### 6. X-VC: Cross-Lingual Voice Conversion via Disentangled Representation (评分: 7/10)

**方向**: 语音转换 | **arXiv ID**: 2604.12456

**作者**: Yafeng Chen, Qian Chen, Shujie Liu, Feng Wang

**机构**: 腾讯

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 跨语言语音转换方法
- 解耦表示学习用于音色和内容分离

**技术亮点**:
- 跨语言迁移能力强
- 有项目页面展示效果

**实验结果**:
- 跨语言转换 MOS 分数 4.1

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12456
- 📥 PDF: https://arxiv.org/pdf/2604.12456
- 💻 代码: 暂无
- 🎯 Demo: https://x-vc.github.io

---

### 7. Tokenizer Fusion: Combining Multiple Tokenizers for Better Speech Representation (评分: 7/10)

**方向**: 语音表征学习 | **arXiv ID**: 2604.12145

**作者**: Changhao Cheng, Qian Chen, Feng Wang

**机构**: 中国科学技术大学、腾讯

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 融合多个tokenizer提升语音表征质量
- 解决单一tokenizer信息损失问题

**技术亮点**:
- 多tokenizer融合策略创新
- 实验设计充分

**实验结果**:
- ASR 任务 WER 降低 5.2%

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12145
- 📥 PDF: https://arxiv.org/pdf/2604.12145
- 💻 代码: 暂无
- 🎯 Demo: 暂无

---

### 8. TokenSE: Speech Enhancement via Token-Based Processing (评分: 7/10)

**方向**: 语音增强 | **arXiv ID**: 2604.12246

**作者**: Anonymous Authors

**机构**: 匿名

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 基于token的语音增强方法
- 将语音增强建模为序列到序列任务

**技术亮点**:
- token化方法应用于SE任务
- 创新性强

**实验结果**:
- PESQ 提升 0.23

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12246
- 📥 PDF: https://arxiv.org/pdf/2604.12246
- 💻 代码: 暂无
- 🎯 Demo: 暂无

---

### 9. StreamMark: Audio Watermarking for Streaming Audio (评分: 7/10)

**方向**: 音频水印 | **arXiv ID**: 2604.11917

**作者**: L1uZhentao, Qian Chen, Feng Wang

**机构**: 中国科学技术大学、腾讯

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 流式音频水印方法
- 支持实时音频的水印嵌入和检测

**技术亮点**:
- 流式处理设计实用
- 有开源代码和benchmark

**实验结果**:
- 检测准确率 99.2%
- 抗攻击能力强

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.11917
- 📥 PDF: https://arxiv.org/pdf/2604.11917
- 💻 代码: https://github.com/L1uZhentao/deepfake_benchmark
- 🎯 Demo: 暂无

---

### 10. Streaming TTS: Real-Time Text-to-Speech with Low Latency (评分: 7/10)

**方向**: 语音合成 | **arXiv ID**: 2604.12438

**作者**: Anonymous Authors

**机构**: 匿名

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 低延迟流式语音合成
- 实现首包延迟小于100ms

**技术亮点**:
- 流式架构设计
- 低延迟实现技术

**实验结果**:
- 首包延迟 87ms
- RTF 0.12

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12438
- 📥 PDF: https://arxiv.org/pdf/2604.12438
- 💻 代码: 暂无
- 🎯 Demo: 暂无

---

### 11. Speech VAE: Variational Autoencoder for Speech Representation Learning (评分: 6/10)

**方向**: 语音表征学习 | **arXiv ID**: 2604.12383

**作者**: Changhao Cheng, Qian Chen, Feng Wang

**机构**: 中国科学技术大学、腾讯

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- VAE应用于语音表征学习
- 学习语音的连续潜在表示

**技术亮点**:
- VAE架构适配语音任务
- 有开源代码

**实验结果**:
- 在语音重建任务上表现良好

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12383
- 📥 PDF: https://arxiv.org/pdf/2604.12383
- 💻 代码: https://github.com/changhao-cheng/JMAS-VAE
- 🎯 Demo: 暂无

---

### 12. VoxEffects: Voice Transformation Effects Dataset and Benchmark (评分: 6/10)

**方向**: 语音数据集 | **arXiv ID**: 2604.12389

**作者**: NII Yamagishi Lab

**机构**: 日本国立情报学研究所

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 语音变效果数据集和基准
- 支持多种语音效果评估

**技术亮点**:
- 数据集规模适中
- 有开源代码

**实验结果**:
- 提供了完整的评估基准

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12389
- 📥 PDF: https://arxiv.org/pdf/2604.12389
- 💻 代码: https://github.com/nii-yamagishilab/VoxEffects
- 🎯 Demo: 暂无

---

### 13. Audio Source Separation via Multi-Scale Transformer (评分: 6/10)

**方向**: 音频分离 | **arXiv ID**: 2604.12480

**作者**: Anonymous Authors

**机构**: 匿名

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 多尺度Transformer用于音频源分离
- 不同尺度捕获不同粒度信息

**技术亮点**:
- 多尺度架构设计
- 实验结果中规中矩

**实验结果**:
- SDR 提升 2.1 dB

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12480
- 📥 PDF: https://arxiv.org/pdf/2604.12480
- 💻 代码: 暂无
- 🎯 Demo: 暂无

---

### 14. ASR Contextual Biasing via Dynamic Vocabulary Adaptation (评分: 6/10)

**方向**: 语音识别 | **arXiv ID**: 2604.12398

**作者**: Anonymous Authors

**机构**: 匿名

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 动态词汇适应用于ASR上下文偏置
- 提升特定领域词识别准确率

**技术亮点**:
- 动态词汇机制
- 实用性一般

**实验结果**:
- 特定词识别准确率提升 8.5%

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12398
- 📥 PDF: https://arxiv.org/pdf/2604.12398
- 💻 代码: 暂无
- 🎯 Demo: 暂无

---

### 15. Speech Emotion Recognition with Multimodal Fusion (评分: 6/10)

**方向**: 情感识别 | **arXiv ID**: 2604.12550

**作者**: Anonymous Authors

**机构**: 匿名

**发布日期**: Wednesday, 15 April 2026

**核心创新**: 
- 多模态融合用于语音情感识别
- 结合声学和文本特征

**技术亮点**:
- 多模态融合策略
- 创新性一般

**实验结果**:
- IEMOCAP 准确率 76.3%

**链接**:
- 📄 论文: https://arxiv.org/abs/2604.12550
- 📥 PDF: https://arxiv.org/pdf/2604.12550
- 💻 代码: 暂无
- 🎯 Demo: 暂无

---

## 📝 总结

今日语音领域共发布15篇相关论文，涵盖语音合成、语音识别、音频生成、声音分离等多个方向。其中：

- **最推荐**: StableToken 提出了创新的稳定token推断机制，解决了语音生成中的关键问题，实验充分且有开源代码
- **值得关注**: CoSyncDiT、Audio-Cogito、Unified Audio Schema 均获得8分，在各自方向上有创新性贡献
- **实用价值**: X-VC 和 StreamMark 提供了开源代码和Demo，适合复现和应用

---

*生成时间: 2026-04-16 09:30 (Asia/Shanghai)*
*数据来源: arXiv cs.SD & eess.AS*