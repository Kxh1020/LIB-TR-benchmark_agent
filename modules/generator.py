import json
from modules.utils import call_stage_llm, extract_json

def learn_human_principle(human_questions_text: str, prompt_text: str) -> str:
    """调用模型进行人类问题集学习"""
    payload = (
        "LEARN_LOGIC_TASK\n"
        f"{prompt_text}\n\n"
        "HUMAN_QUESTIONS:\n"
        f"{human_questions_text}"
    )
    return call_stage_llm("learn_principle", payload).strip()

def generate_evidence(paper_text: str, paper_id: str, prompt_text: str) -> dict:
    """调用模型进行证据提取"""
    payload = (
        "EVIDENCE_EXTRACT_TASK\n"
        f"{prompt_text}\n\n"
        f"PAPER_ID: {paper_id}\n"
        "PAPER_TEXT:\n"
        f"{paper_text}"
    )
    return extract_json(call_stage_llm("get_evidence", payload))

def generate_questions(source_id: str, learned_logic: str, evidence: dict,prompt_text: str,) -> dict:
    """调用模型进行问题生成"""
    payload = (
        "GENERATOR_TASK\n"
        f"{prompt_text}\n\n"
        f"SOURCE_BUNDLE_ID: {source_id}\n"
        "LEARNED_LOGIC:\n"
        f"{learned_logic}\n\n"
        "EVIDENCE_JSON:\n"
        + json.dumps(evidence)
    )
    return extract_json(call_stage_llm("generator", payload))
