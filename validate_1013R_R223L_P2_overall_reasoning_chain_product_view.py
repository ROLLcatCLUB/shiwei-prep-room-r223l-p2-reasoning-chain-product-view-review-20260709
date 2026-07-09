#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223L_P2_overall_reasoning_chain_product.md",
    "R223L_P2_reasoning_chain_edges.json",
    "R223L_P2_gold_sample_traceability.md",
    "R223L_P2_deep_canvas_mock.html",
    "R223L_P2_report.md",
    "README_FOR_GPT_REVIEW.md",
]

DOC_REQUIRED = [
    "Source Evidence Layer",
    "Unit DNA Judgment",
    "Student Problem Reasoning",
    "Unit Total Reasoning Chain",
    "Four-stage Reasoning Chain",
    "Current Stage Deep Chain Example",
    "Component Invocation Logic",
    "R223M = BLOCKED",
    "FORMAL_UI = BLOCKED",
]

HTML_REQUIRED = [
    "1013R_R223L_P2_OVERALL_REASONING_CHAIN_PRODUCT_VIEW",
    "资料证据层",
    "大观念",
    "基本问题",
    "表现性任务",
    "单元 DNA 判断",
    "学生问题推理",
    "四阶段推理链",
    "智造·新朋友",
    "1+1 合作设计",
    "1+n 大变身",
    "组件调用逻辑",
    "评价证据",
    "data-formal-ui=\"false\"",
]

TRACE_REQUIRED = [
    "raw_original_docx_or_pptx_in_repo = false",
    "design_application_and_life_problem_solving",
    "Contamination Control",
    "Do not generalize stationery-specific stories",
]

FORBIDDEN_PHRASES = [
    "正式 UI 已放行",
    "formal UI approved",
    "R97B route implemented",
    "provider call enabled",
    "database write enabled",
    "R223M = PASS",
]


def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")


def main():
    checks = []
    failures = []

    def check(name, passed, detail=""):
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        if not passed:
            failures.append({"name": name, "detail": detail})

    for name in REQUIRED_FILES:
        path = ROOT / name
        check(f"required_file:{name}", path.exists(), str(path))
        if path.exists():
            check(f"non_empty:{name}", path.stat().st_size > 0, str(path.stat().st_size))

    doc = read_text("R223L_P2_overall_reasoning_chain_product.md")
    html = read_text("R223L_P2_deep_canvas_mock.html")
    trace = read_text("R223L_P2_gold_sample_traceability.md")
    report = read_text("R223L_P2_report.md")
    readme = read_text("README_FOR_GPT_REVIEW.md")

    for needle in DOC_REQUIRED:
        check(f"doc_contains:{needle}", needle in doc)

    for needle in HTML_REQUIRED:
        check(f"html_contains:{needle}", needle in html)

    for needle in TRACE_REQUIRED:
        check(f"trace_contains:{needle}", needle in trace)

    for text_name, text in [
        ("doc", doc),
        ("html", html),
        ("trace", trace),
        ("report", report),
        ("readme", readme),
    ]:
        for phrase in FORBIDDEN_PHRASES:
            check(f"forbidden_absent:{text_name}:{phrase}", phrase not in text)

    edges_path = ROOT / "R223L_P2_reasoning_chain_edges.json"
    try:
        edges_payload = json.loads(edges_path.read_text(encoding="utf-8"))
        check("edges_json_valid", True)
    except Exception as exc:
        edges_payload = {}
        check("edges_json_valid", False, repr(exc))

    edges = edges_payload.get("edges", [])
    check("edges_count_at_least_12", len(edges) >= 12, str(len(edges)))
    check("formal_ui_false", edges_payload.get("formal_ui") is False)
    check("stage_id_matches", edges_payload.get("stage_id") == "1013R_R223L_P2_OVERALL_REASONING_CHAIN_PRODUCT_VIEW")

    required_edge_pairs = [
        ("unit.big_idea", "unit.essential_question"),
        ("unit.essential_question", "unit.performance_task"),
        ("stage.making_new_friend", "activity.one_plus_one_design"),
        ("activity.one_plus_one_design", "activity.one_plus_n_transformation"),
        ("activity.one_plus_n_transformation", "assessment.evidence_chain"),
    ]
    edge_pairs = {(edge.get("from"), edge.get("to")) for edge in edges}
    for pair in required_edge_pairs:
        check(f"required_edge:{pair[0]}->{pair[1]}", pair in edge_pairs)

    for idx, edge in enumerate(edges):
        prefix = f"edge_{idx+1}"
        check(f"{prefix}:has_from", bool(edge.get("from")))
        check(f"{prefix}:has_to", bool(edge.get("to")))
        check(f"{prefix}:has_relationship", bool(edge.get("relationship")))
        check(f"{prefix}:has_evidence", bool(edge.get("evidence")))
        check(f"{prefix}:has_source_status", bool(edge.get("source_status")))

    screenshot = ROOT / "R223L_P2_screenshot.png"
    if screenshot.exists():
        check("screenshot_exists", True)
        check("screenshot_non_empty", screenshot.stat().st_size > 1000, str(screenshot.stat().st_size))
    else:
        check("screenshot_exists", False)

    smoke_json = ROOT / "R223L_P2_screenshot_smoke_result.json"
    if smoke_json.exists():
        try:
            smoke = json.loads(smoke_json.read_text(encoding="utf-8"))
            check("screenshot_smoke_json_valid", True)
            check("screenshot_no_horizontal_overflow", smoke.get("no_horizontal_overflow") is True)
            check("screenshot_key_sections_present", smoke.get("key_sections_present") is True)
        except Exception as exc:
            check("screenshot_smoke_json_valid", False, repr(exc))

    result = {
        "passed": not failures,
        "check_count": len(checks),
        "failed": len(failures),
        "failures": failures,
        "checks": checks,
    }

    result_path = ROOT / "validate_1013R_R223L_P2_overall_reasoning_chain_product_view_result.json"
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"passed": result["passed"], "check_count": result["check_count"], "failed": result["failed"]}, ensure_ascii=False))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

