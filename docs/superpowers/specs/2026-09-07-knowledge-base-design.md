# 语音论文知识库（Speech Paper Knowledge Base）设计文档

- 日期：2026-09-07
- 状态：已获用户批准
- 仓库：`/Users/kimmy/Desktop/Vagent_app/SpeechAIResercher`

## 1. 背景与目标

speech-paper-daily skill 每日精读 arXiv 语音论文并输出速递（已累积约 250 篇）。用户希望在与我交流算法方案时，这些论文能被自动检索引用，形成可复用、可共享给团队的语音论文知识库。

**核心场景**：用户讨论算法方案时，agent 自动检索相关论文并引用其贡献、技术点、指标、代码链接作为参考。

## 2. 需求确认（已与用户逐项确认）

| 维度 | 决策 |
|------|------|
| 核心使用方式 | 对话时自动引用 |
| 检索机制 | 结构化索引 + 关键词检索 |
| 数据范围 | 仅收录评分 ≥ 7 分的论文 |
| 存储形态 | 仓库内目录 + 结构化条目 |
| 条目详细度 | 精简结构化，每条约 0.3-0.5KB |
| 更新机制 | 每日速递后自动同步追加 |
| 组织结构 | 按研究方向分文件 |
| 历史入库 | 规则解析脚本一次性批量入库 |
| 团队共享 | 仅 GitHub 仓库 + 配套 skill |

## 3. 目录结构与文件格式

### 3.1 目录结构

```
knowledge_base/
├── README.md                    # 说明与检索指引
├── build_kb.py                  # 一次性历史构建脚本（规则解析）
├── _index.json                  # 全局索引元数据（方向数/论文数/构建时间）
├── tts_speech_synthesis.md      # 语音大模型-TTS
├── asr_spoken_language.md       # 语音大模型-ASR
├── speech_lm_codec.md           # 语音大模型-SpeechLM/Codec/Token
├── speech_lm_understanding.md   # 语音大模型-理解/评测/安全
├── enhancement_frontend.md      # 语音前端-增强/降噪/去混响
├── separation_diarization.md    # 语音前端-分离/说话人
└── other_related.md             # 其他相关（SR/评估/工程等）
```

配套 skill：`.skills/knowledge-base/SKILL.md`，供任何 vagent 用户加载以使用知识库。

### 3.2 条目格式（每条 0.3-0.5KB）

```
## [标题](arXiv ID)

- **方向**：语音大模型/语音前端 | **子方向**：TTS | **评分**：8/10 | **日期**：2026-09-07
- **一句话贡献**：xxx
- **关键技术点**：(1) xxx。(2) xxx。(3) xxx。
- **关键指标**：xxx（数值）；xxx（数值）
- **代码**：URL或暂无
```

按评分降序排列（同分按日期新-旧）。

### 3.3 方向分类规则

- 构建脚本按标题关键词推定子方向标签（TTS/ASR/enhancement/separation/codec/speechLM 等）
- 归类到 6 个主方向文件；无法命中归入 `other_related.md`
- 方向字段以速递原文为准（速递中已有"语音大模型/语音前端"分类）

## 4. 构建与更新机制

### 4.1 一次性历史构建

`build_kb.py`：
- 读取 `.skills/speech-paper-daily/output/*/*.md` 全部历史速递
- 用正则按统一格式解析：标题、arXiv ID、方向、评分、简介、技术方案、实验结果、开源链接
- 过滤评分 ≥ 7 分
- 按方向分组写入各 md 文件（去重：arXiv ID 唯一，最新日期优先）
- 生成 `_index.json` 元数据

输入格式依赖（已验证）：速递文件含 `## [N] 标题`、`**arXiv ID**：xxx | **方向**：xxx`、`### 📌 简介`、`### 🔧 技术方案`、`### 📊 实验结果`、`### ⭐ 评分：X/10`、`**代码**：xxx` 等统一字段。

### 4.2 每日自动追加

在 speech-paper-daily skill 生成速递后，追加一步：
- 解析当天速递的新论文（≥7 分）→ 追加/更新对应方向文件
- 更新 `_index.json`
- 随速递一并 git commit + push

### 4.3 幂等与去重

- arXiv ID 为唯一键，重复出现时覆盖为最新版本
- 追加前检查是否已存在

## 5. 对话时使用方式（agent 行为约定）

1. 用户讨论算法方案时，若方向可判定，先定位对应方向 md 文件
2. 用关键词 grep 筛选匹配论文
3. 引用匹配条目的：一句话贡献、关键技术点、关键指标、代码链接
4. 无匹配方向时，扫描 `_index.json` + 多方向文件

## 6. 团队共享

- GitHub 仓库为主载体（已具备 push 流程）
- 配套 `.skills/knowledge-base/SKILL.md`：描述知识库路径、检索方法、引用格式
- 团队成员部署：`git clone https://github.com/kimmyfa/speech-paper-daily.git`，将 `.skills/knowledge-base/` 复制到自己工作区，即可获得与用户相同的对话式检索能力
- 不开通飞书渠道（用户已确认暂不需要）

## 7. 验证方式

- 构建后：各方向文件论文总数 = 历史速递中 ≥7 分且去重后论文数
- 抽检 3-5 篇：字段完整、方向归类正确、评分正确
- grep 可检索性测试：对已知方向/关键词能定位到论文

## 8. 明确不做（YAGNI）

- 不做向量数据库/语义检索
- 不做飞书云文档/群推送
- 不做 Web 前端/HTML 页面
- 不追溯 2026-07 之前无简介格式的旧速递（或仅记录元数据）