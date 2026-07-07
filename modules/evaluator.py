import json

from modules.utils import (
    call_stage_llm,
    extract_json,
    iter_question_items,
    normalize_decision_payload,
)


def calibrate_evaluator(human_questions_text: str, prompt_text: str) -> dict:
    """Run calibration stage and return anchor json."""
    payload = (
        "EVALUATION_CALIBRATION_TASK\n"
        f"{prompt_text}\n\n"
        f"HUMAN_QUESTIONS_JSON:\n{human_questions_text}"
    )
    return extract_json(call_stage_llm("evaluation", payload))


def evaluate_questions(
    question_set: dict,
    prompt_text: str,
    calibration_anchors: dict | None = None,
) -> list[dict]:
    """调用模型进行评分并输出"""
    decisions = []
    anchors_json = json.dumps(calibration_anchors, ensure_ascii=False) if calibration_anchors else "{}"

    for item in iter_question_items(question_set):
        payload = (
            "EVALUATION_TASK\n"
            f"{prompt_text}\n\n"
            f"CALIBRATION_ANCHORS_JSON:\n{anchors_json}\n\n"
            f"QUESTION_JSON:\n{json.dumps(item)}"
        )

        parsed = normalize_decision_payload(
            extract_json(call_stage_llm("evaluation", payload))
        )
        parsed["qid"] = item.get("qid", "")
        decisions.append(parsed)

    return decisions
