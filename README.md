# Italian Diction Studio · 意大利语歌曲咬字训练

> 面向美声初学者的意大利古咏叹调咬字工具 — 逐字 IPA · 中文直译 · 发音要点 · 示范音频
> A diction toolkit for bel canto beginners — word-by-word IPA · translations · diction notes · demo audio

[中文](#中文) | [English](#english)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Progress](https://img.shields.io/badge/曲目进度-3%2F26-orange)

---

## 中文

### 这是什么

这个项目是为**刚开始学习美声唱法的初学者**准备的，尤其是正在学习**意大利古咏叹调**的学生。

初学者遇到的最大障碍往往不是嗓音，而是**发音**——特别是以中文为主要语言的亚洲学生，面对意大利语的开闭口元音、双辅音、大舌颤音这些规则，常常"认得词、唱不对"。这个项目针对每一首经典意大利古咏叹调，把咬字问题逐字拆解清楚：

- **标准 IPA 逐字注音**——区分开闭口元音（ɛ/e、ɔ/o）、双辅音时值（ss/tts/ɲɲ/ʎʎ）、重音
- **原创中文翻译**——逐字词义 + 整句直译（古语缩略词如 cor / fedel / ognor 都有解释）
- **美声发音要点**——每行要点 + 整曲要点 + 练习建议，按演唱规范编写
- **示范音频**——男声朗读，可跟读对照
- **歌剧场景版本**——男 / 女声应答词对照

### 怎么用

1. 打开网页界面，选择你要练习的曲目
2. 逐句对照 IPA 注音和词义，跟着示范音频朗读
3. 进阶用法：录下自己的演唱音频，发送给 AI Agent，让它基于本项目数据逐字对照你的发音——它会告诉你**哪里需要调整**，比如哪个元音开闭口错了、哪个双辅音时值不够

### 曲目来源

曲目构成采用被众多学习者视为"声乐圣经"的 **John Glenn Paton** 编订《26 Italian Songs and Arias》（Alfred 出版）——美声学习中传唱度最高的意大利古咏叹调选集。所有歌词均为 17–18 世纪公有领域文本。

### 项目状态

- 个人独立开发，目前收录 **3 / 26** 首：Caro mio ben · Sebben, crudele · Nel cor più non mi sento
- 可能存在 bug 或不完善之处，**欢迎在 Issues 留言**反馈，我会陆续完善
- 计划逐步加入更多曲目、更多发音泛读素材

### 快速开始

```bash
# 直接双击 web/index.html 即可使用（无需服务器）
# 或本地起服务：
cd web && python3 -m http.server 8000
# 浏览器打开 http://localhost:8000
```

### 目录结构

```
italian-diction-studio/
├── data/            # 歌曲数据（JSON，字段规范见 data/README.md）
├── web/             # 网页界面（自包含，可整目录部署）
├── audio/           # 示范音频源文件
├── scripts/         # 构建脚本（数据更新后重新打包）
├── LICENSE          # MIT
└── README.md
```

### 数据更新流程

1. 在 `data/` 新建 `<id>.json`（格式见 `data/README.md`）
2. 可选：在 `audio/` 放入 `<id>-demo.wav`
3. 运行 `python3 scripts/build_data_js.py` 重新打包 web/
4. 提交改动

### 部署到 GitHub Pages

`web/` 目录自包含（数据内嵌 + 音频副本）：Settings → Pages → Deploy from a branch → `main` / `/web` → Save。

### 版权与合规

- **歌词原文**：17–18 世纪公有领域文本
- **IPA 注音、中文翻译、发音要点、示范音频**：本项目原创，[MIT](LICENSE) 协议
- **不含**任何出版社书籍的英文翻译、乐谱排版或伴奏编配内容；仅参考 Paton 编订版的曲目构成

### 反馈

有问题或建议，直接在 GitHub Issues 留言即可，每条我都会看。

---

## English

### What is this?

A diction toolkit for **beginners of bel canto singing**, especially students working on **classic Italian arias**.

For most beginners the biggest obstacle is not the voice but **pronunciation**—particularly for Asian students whose main language is Chinese. The open/closed vowels, doubled consonants, and rolled "r" of Italian are notoriously easy to get wrong. This project breaks pronunciation down word by word for each classic Italian aria:

- **Standard IPA, word by word** — open vs. closed vowels (ɛ/e, ɔ/o), doubled-consonant length (ss/tts/ɲɲ/ʎʎ), stress
- **Original Chinese translations** — word-by-word meaning + full-line literal translation (archaic contractions such as cor / fedel / ognor explained)
- **Bel canto diction notes** — per-line notes, whole-song notes, and practice tips written in singing convention
- **Demonstration audio** — male voice reading, for shadowing practice
- **Opera scene versions** — male / female answer-text comparison

### How to use

1. Open the web interface and pick the aria you are practicing
2. Follow the IPA and translation line by line; shadow the demonstration audio
3. Advanced: record your own singing and send the audio to an AI agent. Using the data in this project, it will compare your pronunciation word by word and tell you **exactly what to adjust**—an open vowel where a closed one is needed, a doubled consonant held too short, and so on

### Repertoire

The repertoire follows **John Glenn Paton**'s *26 Italian Songs and Arias* (Alfred)—widely regarded as the "vocal Bible" of Italian aria study. All lyrics are public-domain texts from the 17th–18th centuries.

### Project status

- Independently developed; currently **3 / 26** songs: Caro mio ben · Sebben, crudele · Nel cor più non mi sento
- May contain bugs or rough edges—**feedback via Issues is very welcome**
- Plan: gradually add more songs and more pronunciation/shadowing materials

### Quick start

```bash
# Just open web/index.html in your browser (no server needed)
# or:
cd web && python3 -m http.server 8000
# then visit http://localhost:8000
```

### Structure

```
italian-diction-studio/
├── data/            # Song data (JSON; schema in data/README.md)
├── web/             # Web interface (self-contained, deployable as-is)
├── audio/           # Demo audio sources
├── scripts/         # Build script (repackage after data changes)
├── LICENSE          # MIT
└── README.md
```

### Data workflow

1. Add `<id>.json` under `data/` (schema: `data/README.md`)
2. Optional: put `<id>-demo.wav` under `audio/`
3. Run `python3 scripts/build_data_js.py` to repackage web/
4. Commit

### Deploy to GitHub Pages

`web/` is self-contained: Settings → Pages → Deploy from a branch → `main` / `/web` → Save.

### License & compliance

- **Lyrics**: public-domain texts from the 17th–18th centuries
- **IPA transcription, Chinese translations, diction notes, demo audio**: original work by this project, [MIT](LICENSE)
- **No** copyrighted content from any published edition (English translations, engraving, or accompaniments) is included; only the repertoire selection of Paton's edition is referenced

### Feedback

Issues and suggestions are very welcome—every one will be read.
