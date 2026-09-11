# 数据模型说明（Data Schema）

每首歌一个 JSON 文件，位于 `data/`，文件名用 `id` 字段（连字符小写）。

## 字段定义

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `id` | string | ✓ | 唯一标识，如 `caro-mio-ben`，同时是文件名 |
| `number` | int | ✓ | 在《26 Italian Songs and Arias》中的序号（1–26） |
| `title.it` | string | ✓ | 意大利语标题 |
| `title.zh` | string | ✓ | 中文译名 |
| `composer.name` | string | ✓ | 作曲家 |
| `composer.life` | string |  | 生卒年 |
| `source` | string | ✓ | 出处说明（仅指歌词来源，公有领域） |
| `voice` | string | ✓ | 音域版本（Medium Low / Medium High） |
| `meter` / `tempo` | string |  | 拍号与速度标记（以乐谱为准） |
| `structure` | string | ✓ | 曲式结构，如 `A-B-A'（da capo）` |
| `intro` | string | ✓ | 原创背景简介（中文，不含书内英文原文） |
| `lyrics[]` | array | ✓ | 歌词，见下 |
| `variants[]` | array |  | 同曲异文版本（如男/女声应答词），结构同 lyrics 的简版 |
| `diction_notes[]` | array |  | 整曲发音要点（原创，逐条） |
| `practice_tips[]` | array |  | 练习建议 |

## `lyrics[]` 结构

按乐句分行，每行：

| 字段 | 类型 | 说明 |
|---|---|---|
| `section` | string | 所属段，如 `A1` / `B` / `B'` / `A2` |
| `it` | string | 该行意大利语原文（公有领域文本） |
| `zh` | string | 该行整句中文直译（原创翻译） |
| `words[]` | array | 逐字拆解 |
| `notes` | string | 该行特有发音要点（原创） |

### `words[]` 结构

| 字段 | 类型 | 说明 |
|---|---|---|
| `it` | string | 单词 |
| `ipa` | string | 标准 IPA 注音（原创标注） |
| `zh` | string | 该词中文词义 |

## 发音标注规范

- IPA 采用**标准国际音标**（含重音符号 `ˈ`、长音 `ː`、双辅音延长如 `ʃʃ`）。
- 按美声（bel canto）演唱习惯标注，不按日常口语弱化标注。
- 开口/闭口元音（`ɛ` vs `e`、`ɔ` vs `o`）严格区分——这是意大利语咬字的生命线。

## 版权边界（重要）

- **歌词原文**：17–18 世纪公有领域文本，可自由使用。
- **IPA 注音、中文直译、发音要点**：本项目原创内容。
- **不包含**：Paton 版书籍的英文翻译、乐谱排版、伴奏编配等受版权保护内容。
