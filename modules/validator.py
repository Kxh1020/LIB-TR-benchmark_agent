import json

from modules.utils import (
    call_stage_llm,
    extract_json,
    iter_question_items,
    normalize_decision_payload,
)


def validate_questions(question_set: dict, evidence: dict, prompt_text: str) -> list[dict]:
    """调用模型进行验证"""
    decisions = []
    for item in iter_question_items(question_set):
        payload = (
            "VALIDATOR_TASK\n"
            f"{prompt_text}\n\n"
            f"QUESTION_JSON:\n{json.dumps(item)}\n\n"
            f"EVIDENCE_JSON:\n{json.dumps(evidence)}"
        )
        parsed = normalize_decision_payload(
            extract_json(call_stage_llm("validator", payload))
        )
        parsed["qid"] = item.get("qid", "")
        decisions.append(parsed)
    return decisions
