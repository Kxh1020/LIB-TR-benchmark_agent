import json
from modules.utils import call_stage_llm, extract_json

def learn_human_logic(human_questions_text: str, prompt_text: str) -> str:
    """调用模型进行人类问题集学习"""
    payload = (
        "LEARN_LOGIC_TASK\n"
        f"{prompt_text}\n\n"
        "HUMAN_QUESTIONS:\n"
        f"{human_questions_text}"
    )
    return call_stage_llm("learn_logic", payload).strip()

def generate_evidence(paper_text: str, paper_id: str, prompt_text: str) -> dict:
    """调用模型进行证据提取"""
    payload = (
        "EVIDENCE_EXTRACT_TASK\n"
        f"{prompt_text}\n\n"
        f"PAPER_ID: {paper_id}\n"
        "PAPER_TEXT:\n"
        f"{paper_text}"
    )
    return extract_json(call_stage_llm("evidence_extract", payload))

def generate_questions(paper_id: str, learned_logic: str, evidence: dict,prompt_text: str,) -> dict:
    """调用模型进行问题生成"""
    payload = (
        "GENERATOR_TASK\n"
        f"{prompt_text}\n\n"
        f"PAPER_ID: {paper_id}\n"
        "LEARNED_LOGIC:\n"
        f"{learned_logic}\n\n"
        "EVIDENCE_JSON:\n"
        + json.dumps(evidence)
    )
    return extract_json(call_stage_llm("generator", payload))
