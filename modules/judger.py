import json

from modules.utils import call_stage_llm, extract_json


def build_solver_item(item: dict) -> dict:
    """将完整题目对象裁剪"""
    return {
        "qid": item.get("qid", ""),
        "type": item.get("type", ""),
        "solver_view": item.get("solver_view", {}),
    }


def solve_question(item: dict, prompt_text: str) -> dict:
    """调用模型进行作答"""
    solver_item = build_solver_item(item)

    payload = (
        "SOLVER_TASK\n"
        f"{prompt_text}\n\n"
        f"QUESTION_JSON:\n{json.dumps(solver_item)}"
    )
    return extract_json(call_stage_llm("judger", payload))

def judge_mcq(item: dict, prediction_payload: dict) -> dict:
    """判断mcq正确率"""
    predicted = prediction_payload.get("prediction", [])
    gold = item.get("ground_truth", {}).get("correct_options", [])

    predicted_set = set(predicted if isinstance(predicted, list) else [predicted])
    gold_set = set(gold if isinstance(gold, list) else [gold])

    score = 1 if predicted_set == gold_set else 0

    return {
        "qid": item.get("qid", ""),
        "question_type": "mcq",
        "prediction": predicted,
        "gold_answer": gold,
        "score": score,
    }

def judge_short_answer(item: dict, prediction_payload: dict, prompt_text: str) -> dict:
    """判断sa正确率"""
    prediction = prediction_payload.get("prediction", "")
    gold_answer = item.get("ground_truth", {}).get("gold_answer", "")

    payload = (
        "SHORT_ANSWER_JUDGE_TASK\n"
        f"{prompt_text}\n\n"
        f"QUESTION_JSON:\n{json.dumps(item)}\n\n"
        f"PREDICTION:\n{prediction}\n\n"
        f"GOLD_ANSWER:\n{gold_answer}"
    )

    result = extract_json(call_stage_llm("judger", payload))

    return {
        "qid": item.get("qid", ""),
        "question_type": "short_answer",
        "prediction": prediction,
        "gold_answer": gold_answer,
        "score": result.get("score", 0),
        "reason": result.get("reason", ""),
    }

def judge_results_by_paper(final_questions_by_paper: dict, solver_prompt_text: str,sa_judge_prompt_text: str) -> dict:
    """把多篇论文的最终题集逐篇交给 judge_question_set(...) 处理。"""
    results_by_paper = {}

    for paper_id, question_set in final_questions_by_paper.items():
        results_by_paper[paper_id] = judge_question_set(
            question_set=question_set,
            solver_prompt=solver_prompt_text,
            sa_judge_prompt=sa_judge_prompt_text,
        )

    return results_by_paper



def judge_question_set(question_set: dict, solver_prompt: str, sa_judge_prompt: str) -> list[dict]:
    """对一篇论文的最终题集逐题作答并评分。"""
    results = []

    for item in question_set.get("mcqs", []):
        prediction_payload = solve_question(item, solver_prompt)
        results.append(judge_mcq(item, prediction_payload))

    for item in question_set.get("short_answers", []):
        prediction_payload = solve_question(item, solver_prompt)
        results.append(judge_short_answer(item, prediction_payload, sa_judge_prompt))

    return results
