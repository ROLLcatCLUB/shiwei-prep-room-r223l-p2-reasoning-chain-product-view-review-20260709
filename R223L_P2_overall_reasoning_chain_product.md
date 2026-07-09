# R223L-P2 Overall Reasoning Chain Product View

```text
stage_id=1013R_R223L_P2_OVERALL_REASONING_CHAIN_PRODUCT_VIEW
status=reasoning_chain_product_view_only
R223L_P1 = VISUAL_DENSITY_IMPROVED
R223L_P1 = REASONING_CHAIN_NOT_VISIBLE
R223M = BLOCKED
FORMAL_UI = BLOCKED
R97B / UI / runtime / prompt / model / db = UNTOUCHED
```

## 0. Why This Stage Exists

The previous review over-focused on page density, carrier slots, and visual
folding. Those are necessary, but they do not answer the central teacher
question:

```text
Why was this lesson designed this way?
```

R223L-P2 therefore outputs the teaching reasoning chain product that the system
should place in front of the teacher before any formal UI work.

This is not hidden model reasoning. It is teacher-auditable teaching design
reasoning.

## 1. Source Evidence Layer

```text
sample = 我为文具代言
subject = 美术
stage = 第一学段
grade = 一年级
textbook_anchor = 苏少版一年级上册第六单元《学习小帮手》
raw_sample_files_available_in_repo = false
evidence_basis = R221A reference audit + R221C static fixture
```

Confirmed or recorded anchors:

```text
大观念：
体验传统工艺，带着好奇心和想象力设计改进文具从而改善学习生活。

基本问题：
怎样全方面了解文具，并感受它的重要性？

表现性任务：
我为文具代言，形成《一年级购买文具建议书》《文具课堂使用指南》。

四阶段：
初探、再探、智造、结交。
```

Boundary:

```text
The original docx/pptx files are not present in this repository.
Confirmed values come from prior scan and dictionary evidence.
Stage responsibilities and some local chains remain reconstructed.
```

## 2. Unit DNA Judgment

The sample is not:

```text
ordinary still-life drawing of stationery
ordinary paper craft
generic classroom object introduction
```

The sample is:

```text
design_application
+ life_problem_solving
+ observation_expression
+ material_technique_inquiry
+ cultural_technology_understanding
```

Core judgment:

```text
文具不是被观察的静物。
文具是学生学习生活中的真实问题对象。

学生不是只要画出文具。
学生要经历：
认识文具 -> 探究文具 -> 改进文具 -> 评价使用文具。
```

## 3. Student Problem Reasoning

Based on first-grade learner constraints recorded in R221A/R221C, the system
should infer these student problems:

```text
学生问题 1：看文具容易停留在“我知道这个是什么”。
学生问题 2：描述文具时容易只说名称，不会说外形、材质、功能。
学生问题 3：设计改进时容易天马行空，缺少结构和用途依据。
学生问题 4：做作品时容易只装饰，不考虑使用便捷性。
学生问题 5：评价时容易只说“好看”，不能说出是否适合使用。
```

Therefore the unit must build a learning chain:

```text
感知 -> 描述 -> 解释 -> 改进 -> 表达 -> 建议
```

## 4. Unit Total Reasoning Chain

```text
大观念
设计可以改善学习生活，传统工艺和现代智造都体现人的智慧。

↓

基本问题
学生怎样全面了解文具，并感受它的重要性？

↓

表现性任务
形成《一年级购买文具建议书》和《文具课堂使用指南》。

↓

反推学习过程
1. 认识文具：外形、材质、功能、用途。
2. 探究文具：结构、工艺、技术和文化。
3. 改进文具：根据使用问题提出设计改进。
4. 表达文具：评价、推荐、说明如何合理使用。

↓

四阶段学习责任
初探：认识与描述文具。
再探：技术 / 工艺 / 文化理解。
智造：材料技法改进文具。
结交：评价、辩论、形成建议。
```

## 5. Four-stage Reasoning Chain

### 5.1 初探：笔中奥秘

Responsibility:

```text
让学生从“知道文具名称”走向“能观察、描述、介绍文具”。
```

Activity chain:

```text
发现小帮手
-> 盲盒猜猜猜
-> 小帮手介绍会 / 我为文具代言
-> 文具大变身
```

Reasoning edges:

```text
学生不会细看文具 -> 用课前学习单引导观察
学生只会说名称 -> 用盲盒触摸迫使其描述外形与触感
学生不会表达文具价值 -> 用代言情境介绍特点和用途
学生对结构没有创造性理解 -> 用拼搭变身感受外形和结构可组合
```

Components:

```text
material_mystery_box
guess_from_clue
say_what_you_see
endorsement_talk
creative_combination
learning_sheet_record
```

Evidence:

```text
课前文具观察单
盲盒描述记录
文具代言表达
文具拼搭照片
外形 / 材质 / 用途描述
```

### 5.2 再探：笔中奥秘

Responsibility:

```text
让学生从“文具是学习用品”走向“文具有技术、工艺、文化和设计智慧”。
```

Activity chain:

```text
文具知多少：剪影猜名称
-> 圆珠笔的故事：小小辩论会
-> 太空中的笔：小小分享会
-> 走访造笔厂：小小手艺人
-> 智造交流会：选一选、说一说、画一画
```

Reasoning edges:

```text
学生已经认识文具 -> 增加剪影难度，检查视觉特征是否内化
学生觉得文具普通 -> 用圆珠笔故事打开技术问题
学生不知道设计与国家科技有关 -> 用中国制造 / 中国智造建立价值理解
学生不知道传统工艺和文具有关 -> 用毛笔工厂和造笔师傅建立文化理解
学生有了价值理解 -> 回到喜欢的文具，提出改进想法并画草图
```

Components:

```text
silhouette_guess
mini_debate
story_video_prompt
learning_sheet_record
design_reason_talk
idea_sketch_card
```

Evidence:

```text
剪影识别与理由
圆珠笔故事观后表达
太空笔分享
毛笔工艺学习单
文具优点 / 缺点 / 改进想法
改进小草图
```

### 5.3 智造：新朋友

Responsibility:

```text
把前两阶段的观察、故事、工艺和设计意识转化为文具改进作品。
```

Activity chain:

```text
忆一忆：毛笔的诞生
-> 探一探：关键结构
-> 设计会：像设计师一样思考
-> 试一试：1+1 合作小设计
-> 创一创：1+n 文具大变身
-> 笔友汇
-> 赠笔礼
```

Reasoning edges:

```text
学生已了解文具故事 -> 回忆毛笔工艺，唤醒“文具不是普通物品”
学生容易只装饰表面 -> 先探究关键结构和小巧思
学生设计能力弱 -> 用 1+1 合作小设计降低难度
学生需要扩展材料 -> 从粘土模拟过渡到 1+n 多材料技法
学生评价语言弱 -> 用笔友汇、关键词评价和赠笔礼完成表达与评价
```

Components:

```text
circle_and_annotate
design_detail_spotlight
material_choice_board
technique_menu
one_plus_n_expansion
gallery_walk
keyword_feedback
photo_submit
```

Evidence:

```text
关键结构观察记录
1+1 合作小设计照片
改进小草图
1+n 新朋友作品
材料技法选择理由
笔友汇评价记录
赠笔表达
```

### 5.4 结交：新朋友

Responsibility:

```text
让学生从“我做了一个文具作品”走向“我能评价文具、合理使用文具、向别人提出建议”。
```

Activity chain:

```text
线上交流会
-> 学习小帮手：有没有一种可能
-> 小型辩论会
-> 成果展示会
-> 购买文具建议书
-> 文具课堂使用指南
-> 初识中高年级文具
```

Reasoning edges:

```text
学生完成作品 -> 在线上交流会欣赏和点赞
学生容易只追求功能越多越好 -> 用“有没有一种可能”制造冲突
学生需要价值判断 -> 辩论文具是否越多越好、越贵越好
学生需要迁移到生活 -> 形成购买文具建议书和课堂使用指南
```

Components:

```text
gallery_walk
peer_vote_wall
mini_debate
two_stars_one_wish
guide_generation
recommendation_card
```

Evidence:

```text
线上点赞 / 评价记录
辩论观点
购买文具建议
课堂使用指南
成果展示表达
```

## 6. Current Stage Deep Chain Example

Selected example:

```text
stage = 第三阶段 智造·新朋友
lesson_responsibility = 把观察、故事、工艺和设计意识转化为文具改进作品
core_question = 如何用身边的材料创意改造好朋友？
performance_task_link = 为购买文具建议书和课堂使用指南提供作品经验和改进理由
```

Generation logic:

```text
前置证据：
学生已经认识文具外形、材质、功能；
学生已经听过圆珠笔、太空笔、毛笔工艺故事；
学生已经有初步改进想法和小草图。

↓

所以本课不能再重复“文具是什么”。

↓

本课重点：
从“我知道文具”转到“我能改进文具”。

↓

但一年级学生设计能力弱。

↓

所以用：
忆一忆 / 探一探 / 找小巧思
帮助学生看到文具结构和设计细节。

↓

学生有想法但难以实现。

↓

所以用：
1+1 合作小设计
先用铅笔 + 粘土模拟改进。

↓

学生容易停留在单一材料。

↓

所以用：
1+n 文具大变身
引入线形材料、纸材、形状材料和技法菜单。

↓

学生评价语言弱。

↓

所以用：
笔友汇 + 关键词评价 + 赠笔礼
完成展示、表达、接纳建议。
```

## 7. Component Invocation Logic

| Component | Student Problem | Why Here | Alternative | Evidence |
| --- | --- | --- | --- | --- |
| `circle_and_annotate` / 圈一圈 | 学生只看外表，不知道结构为什么这样设计。 | 用圈画把“关键结构”显性化。 | 教师直接讲结构，但学生参与弱。 | 关键结构观察记录。 |
| `design_detail_spotlight` / 设计细节聚焦 | 学生看不到文具中的小巧思。 | 聚焦握笔器、笔夹、橡皮笔等可改进细节。 | 大图讲解。 | 学生说出小巧思。 |
| `material_choice_board` / 材料选择板 | 学生选择材料随意。 | 把材料特性和改进目的对应起来。 | 教师指定材料。 | 材料选择理由。 |
| `technique_menu` / 技法菜单 | 学生不会从想法转到做法。 | 给 1-2 种低门槛技法。 | 完全自由制作。 | 技法使用痕迹。 |
| `photo_submit` / 拍照提交 | 过程作品容易丢失。 | 保存 1+1 小设计和 1+n 作品证据。 | 课后收作品。 | 过程照片。 |
| `keyword_feedback` / 关键词评价 | 学生评价只说好看。 | 提供结构、功能、材料、使用四类评价词。 | 自由点评。 | 笔友汇评价记录。 |

## 8. Output Shape Required Later

The workbench should not show a flat card. It should show three levels:

```text
Level 1: Unit total chain
大观念 -> 基本问题 -> 表现性任务 -> 四阶段责任

Level 2: Current stage responsibility
承接 -> 本阶段责任 -> 输出证据

Level 3: Current activity expansion
为什么存在 -> 教师怎么说 -> 学生怎么做 -> 素材支架 -> 组件调用 -> 评价证据
```

This is the reasoning-chain product that should be reviewed before any
teacher-facing UI implementation.
