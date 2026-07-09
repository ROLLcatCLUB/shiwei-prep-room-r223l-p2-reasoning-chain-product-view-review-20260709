# R223L-P2 Gold Sample Traceability

```text
stage_id=1013R_R223L_P2_OVERALL_REASONING_CHAIN_PRODUCT_VIEW
status=gold_sample_traceability_only
sample=我为文具代言
formal_ui=blocked
R223M=blocked
```

## 1. Traceability Boundary

This file records what the P2 reasoning-chain product may say about the
gold sample, and what it must not pretend to know.

```text
raw_original_docx_or_pptx_in_repo = false
source_basis = R221A reference audit + R221B contracts + R221C fixture
teacher_review_notes = used only where marked reconstructed_from_teacher_review
```

R223L-P2 is therefore not a new sample extraction pass. It is a teacher-facing
product view that makes prior evidence and prior reconstruction inspectable.

## 2. Source Evidence Ledger

| Claim | Status | Evidence Source | Use In P2 |
| --- | --- | --- | --- |
| Unit theme is 我为文具代言 | confirmed_reference_sample | R221A reference audit | Title and sample scope |
| Subject is 美术 | confirmed_reference_sample | R221A reference audit | Unit DNA |
| Stage/grade is 第一学段/一年级 | confirmed_reference_sample | R221A reference audit | Learner problem reasoning |
| Big idea is about traditional craft, curiosity, imagination, design improvement, and improving learning life | confirmed_from_R221A | R221A unit reasoning chain | Unit total chain |
| Essential question asks how to understand stationery comprehensively and feel its importance | confirmed_from_R221A | R221A unit reasoning chain | Big idea to inquiry edge |
| Performance task includes 一年级购买文具建议书 and 文具课堂使用指南 | confirmed_from_R221A | R221A/R221C fixture | Inquiry to public evidence edge |
| Four phases are 初探、再探、智造、结交 | confirmed_from_R221A | R221A unit reasoning chain | Stage chain |
| Initial phase includes blind-box style observation, learning sheet, and helper exchange | confirmed_from_R221A_dictionary | R221A field inventory | Initial stage deep evidence |
| Re-exploration includes 圆珠笔、太空笔、毛笔工艺、中国智造 value line | reconstructed_from_teacher_review | Teacher review notes and P1 calibration line | Cultural/technology chain |
| Third phase 智造 includes structure observation, 1+1 design, 1+n transformation, and 文具交朋友 | reconstructed_from_teacher_review | Teacher review notes | Current deep chain |
| Final phase includes online exchange, debate, suggestion book, use guide | reconstructed_from_teacher_review | Teacher review notes | Public output chain |
| Components should solve visible student problems, not appear as tool buttons | system_reasoning_product | R222D-P1 component hardening + R223H/I/J/K guard line | Component invocation logic |

## 3. Unit DNA Trace

The sample should be classified as:

```text
primary_archetype = design_application_and_life_problem_solving
secondary_archetypes =
  - observation_expression
  - craft_technology_culture_understanding
  - performance_task_public_expression
not_primary =
  - pure_object_drawing
  - generic_handcraft
  - generic_object_introduction
```

Reason:

```text
The unit does not stop at naming or drawing stationery.
It asks students to observe stationery, understand its use and value,
explore stories of making and technology, redesign or improve stationery,
and finally produce public-facing recommendations or guides.
```

## 4. Learner Problem Trace

| Learner Problem | Evidence Status | Teaching Response | Product View Requirement |
| --- | --- | --- | --- |
| Observation is scattered | reconstructed_from_stage_and_grade | Use touch, compare, circle, describe | Show why observation components appear |
| Attention is short | inferred_from_grade_with_R221A_support | Use game entry and short action loops | Show short, concrete classroom moves |
| Handwork is limited | inferred_from_grade_with_R221A_support | Use low-threshold materials and 1+1 scaffold | Show scaffold before open creation |
| Expression needs sentence support | reconstructed_from_learning_sheet_and_public_task | Use sentence frames, helper exchange, guide output | Show teacher language and evidence |
| Curiosity is strong | inferred_from_stage_and_sample_story_line | Use blind box, stories, craft/technology discovery | Show why cultural/technology line exists |

## 5. Stage Trace

| Stage | Teaching Responsibility | Prior Evidence | P2 Display Role |
| --- | --- | --- | --- |
| 初探 | Open curiosity and observable description | R221A stage chain and field inventory | Shows why the unit starts with touch, description, and helper exchange |
| 再探 | Move from object use to craft, technology, and cultural value | Teacher review + R221E-P1 calibration | Shows why stories are not decorative material |
| 智造 | Convert understanding into design improvement and making | Teacher review + reconstructed stage responsibility | Used as current deep-chain canvas |
| 结交 | Turn learning into public recommendation, use guide, debate, and migration | R221A/C performance task evidence | Shows why final output is evaluable evidence |

## 6. Component Trace

| Component | Student Problem It Solves | Why Here | Alternative | Evidence Output |
| --- | --- | --- | --- | --- |
| 比一比 / compare_two_images | Students judge by like/dislike instead of visual grounds | When comparing ordinary vs improved stationery or material effects | 圈一圈 if the task is finding local details | Comparison note or annotated contrast |
| 圈一圈 / circle_and_annotate | Students cannot point to the visual basis of a claim | When observing structure, line, shape, texture, or problem point | 说一说 if evidence is already visible | Annotated image or keyword note |
| 技法菜单 / technique_menu | Students have ideas but do not know how to realize them | During 1+n transformation and low-threshold design | Teacher demo if safety or tool use is high-risk | Chosen technique and reason |
| 学习单记录 / worksheet_record | Students forget process evidence | During trial, design, debate, or recommendation preparation | Photo submission for work process evidence | Worksheet row, checklist, or selected evidence |
| 材料盲盒 / material_mystery_box | Students know material names but not tactile/effect differences | Initial exploration or before material choice | Material gallery when touch is unavailable | Material effect note |

## 7. Contamination Control

```text
Do not generalize stationery-specific stories to every art lesson.
Do not turn the gold sample into a universal component list.
Do not treat reconstructed stage lines as raw confirmed source text.
Do not show complete reasoning as default final UI.
Do not authorize R97B, frontend, backend, runtime, prompt, model, db, or formal apply.
```

## 8. P2 Review Question

The reviewer should not ask whether the page is visually final. The reviewer
should ask:

```text
Can a teacher see why this unit, this stage, this activity, this component,
and this evidence chain exist?
```

