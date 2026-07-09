# R223L-P2 Report

```text
stage_id=1013R_R223L_P2_OVERALL_REASONING_CHAIN_PRODUCT_VIEW
status=READY_FOR_REASONING_CHAIN_PRODUCT_REVIEW
R223L_P1 = VISUAL_DENSITY_IMPROVED
R223L_P1 = REASONING_CHAIN_NOT_VISIBLE
R223M = BLOCKED
FORMAL_UI = BLOCKED
R97B / UI / runtime / prompt / model / db = UNTOUCHED
```

## What Changed

R223L-P2 stops treating the next review as a page-density problem. It creates
a teacher-auditable teaching reasoning chain product for the gold sample
`我为文具代言`.

The core output is:

```text
source evidence
→ unit DNA
→ learner problem reasoning
→ big idea / essential question / performance task
→ four-stage responsibility chain
→ current stage deep chain
→ activity reason
→ component invocation
→ assessment evidence
```

## Main Deliverables

| File | Role |
| --- | --- |
| `R223L_P2_overall_reasoning_chain_product.md` | Main teacher-readable reasoning chain product |
| `R223L_P2_reasoning_chain_edges.json` | Structured edge list for later validation and reuse |
| `R223L_P2_gold_sample_traceability.md` | Evidence status and contamination boundary |
| `R223L_P2_deep_canvas_mock.html` | Static visual mock of the reasoning product view |
| `R223L_P2_screenshot.png` | Screenshot smoke evidence |
| `validate_1013R_R223L_P2_overall_reasoning_chain_product_view.py` | Local validator |

## Review Standard

This stage should be reviewed by asking:

```text
Can a teacher see why this unit is generated this way?
Can a teacher see how big idea leads to activities?
Can a teacher see why each activity exists?
Can a teacher see why each component is invoked?
Can a teacher see what evidence will prove learning?
```

The reviewer should not approve this stage merely because the HTML looks
clean or the validator passes.

## Boundary

Allowed:

```text
static reasoning product document
structured reasoning edges
static visual mock
screenshot smoke
validator
review package
```

Blocked:

```text
formal UI
R97B route/component/CSS modification
frontend/backend implementation
runtime/provider/model/prompt/database
lesson body writeback
real classroom component execution
formal apply
R223M
```

## Decision Options

```text
PASS_GOLD_SAMPLE_DEEP_CANVAS_MOCK
HOLD_FOR_DEEP_CANVAS_REDESIGN
STOP_FORMAL_UI_NOT_READY
```

Recommended next step only if this review passes:

```text
R223M_TEACHER_REVIEW_OF_GOLD_SAMPLE_MOCK
```

