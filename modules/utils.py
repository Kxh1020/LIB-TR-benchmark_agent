import json
import re
from typing import Any
from urllib import request

from config import STAGE_CONFIG


def stage_settings(stage_name: str) -> tuple[str, str, str, float]:
    """确定调用模型"""
    config = STAGE_CONFIG[stage_name]
    return (
        config["base_url"],
        config["api_key"],
        config["model_name"],
        float(config["temperature"]),
    )

def call_stage_llm(stage_name: str, prompt: str) -> str:
    """调用模型"""
    base_url, api_key, model_name, temperature = stage_settings(stage_name)

    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "stream": False,
    }

    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        base_url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with request.urlopen(req, timeout=180) as response:
        data = json.loads(response.read().decode("utf-8"))

    choices = data.get("choices", [])
    content = choices[0]["message"]["content"]
    return content.strip()

def extract_json(text: str) -> Any:
    """转换为json格式引用自webaggregator_eval"""
    raw = text.strip()

    if raw.startswith("```"):
        raw = raw[3:]
        if raw.startswith("json"):
            raw = raw[4:]
        if raw.endswith("```"):
            raw = raw[:-3]
        raw = raw.strip()

    try:
        return json.loads(raw, strict=False)
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(raw[start:end + 1], strict=False)
            except json.JSONDecodeError as e:
                place = e.pos
                raise ValueError(
                    f"Invalid JSON returned by model: {e}\n"
                    f"Raw output: {raw}\n"
                    f"Error near: '{raw[max(0, place - 4):place + 5]}'"
                ) from e
        raise ValueError(f"No valid JSON object found in model output:\n{raw}")

def filter_questions_by_decisions(question_set: dict, decisions: list[dict]) -> dict:
    """筛选验证过的问题"""
    accepted_qids = {
        item["qid"]
        for item in decisions
        if item.get("decision") == "ACCEPT"
    }

    return {
        "mcqs": [
            q for q in question_set.get("mcqs", [])
            if q.get("qid") in accepted_qids
        ],
        "short_answers": [
            q for q in question_set.get("short_answers", [])
            if q.get("qid") in accepted_qids
        ],
    }

def filter_questions_by_score(question_set: dict,evaluations: list[dict],min_total: int = 38,) -> dict:
    """筛选打分后的问题"""
    accepted_qids = set()

    for item in evaluations:
        scores = item.get("scores", {})
        total = scores.get("Total", 0)
        try:
            total = int(total)
        except (TypeError, ValueError):
            total = 0

        if total >= min_total:
            accepted_qids.add(item.get("qid", ""))

    return {
        "mcqs": [
            q for q in question_set.get("mcqs", [])
            if q.get("qid") in accepted_qids
        ],
        "short_answers": [
            q for q in question_set.get("short_answers", [])
            if q.get("qid") in accepted_qids
        ],
    }

def iter_question_items(question_set: dict) -> list[dict]:
    """把问题集里的问题拿出来"""
    return question_set.get("mcqs", []) + question_set.get("short_answers", [])

def normalize_decision_payload(payload: object) -> dict:
    """规范格式"""
    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict):
                payload = item
                break
    if not isinstance(payload, dict):
        return {"decision": "REJECT", "raw": payload}
    decision = str(payload.get("decision", payload.get("status", "REJECT"))).upper()
    if decision not in {"ACCEPT", "REVISE", "REJECT"}:
        decision = "REJECT"
    payload["decision"] = decision
    return payload

def calc_judger_metrics(results_by_paper: dict) -> dict:
    """统计正确率"""
    total_items = 0
    total_score = 0.0

    mcq_count = 0
    mcq_score = 0.0

    sa_count = 0
    sa_score = 0.0

    for items in results_by_paper.values():
        for item in items:
            score = item.get("score", 0)
            try:
                score = float(score)
            except (TypeError, ValueError):
                score = 0.0

            total_items += 1
            total_score += score

            question_type = str(item.get("question_type", "")).lower()

            if question_type == "mcq":
                mcq_count += 1
                mcq_score += score
            elif question_type == "short_answer":
                sa_count += 1
                sa_score += score

    return {
        "total_items": total_items,
        "average_score": (total_score / total_items) if total_items else 0.0,
        "mcq_count": mcq_count,
        "mcq_accuracy": (mcq_score / mcq_count) if mcq_count else 0.0,
        "sa_count": sa_count,
        "sa_average_score": (sa_score / sa_count) if sa_count else 0.0,
    }
