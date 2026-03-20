import json

from modules.utils import (
    call_stage_llm,
    extract_json,
    filter_questions_by_decisions,
    iter_question_items,
    normalize_decision_payload,
)


def evaluate_questions(question_set: dict, prompt_text: str) -> list[dict]:
    """调用模型进行评分并输出"""
    decisions = []

    for item in iter_question_items(question_set):
        payload = (
            "EVALUATION_TASK\n"
            f"{prompt_text}\n\n"
            f"QUESTION_JSON:\n{json.dumps(item)}"
        )

        parsed = normalize_decision_payload(
            extract_json(call_stage_llm("evaluation", payload))
        )
        parsed["qid"] = item.get("qid", "")
        decisions.append(parsed)

    return decisions
