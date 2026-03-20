import argparse
from pathlib import Path

from modules.generator import (
    generate_evidence,
    generate_questions,
    learn_human_logic,
)
from modules.evaluator import evaluate_questions
from loader import load_inputs
from saver import save_json, save_text
from modules.utils import filter_questions_by_decisions, filter_questions_by_score
from modules.validator import validate_questions
from modules.judger import judge_results_by_paper


def main() -> None:
    project_root = Path(__file__).resolve().parent
    bundle = load_inputs(project_root=project_root)

    learned_logic = learn_human_logic(
        human_questions_text=bundle["human_questions_text"],
        prompt_text=bundle["prompts"]["learn_logic"],
    )
    evidence_by_paper = {}
    generated_by_paper = {}
    validation_by_paper = {}
    validated_by_paper = {}
    evaluation_by_paper = {}
    final_by_paper = {}

    total_generated = 0
    total_validated = 0
    total_final = 0

    for paper in bundle["papers"]:
        evidence = generate_evidence(
            paper_text=paper["paper_text"],
            paper_id=paper["paper_id"],
            prompt_text=bundle["prompts"]["evidence_extract"],
        )
        generated_questions = generate_questions(
            paper_id=paper["paper_id"],
            learned_logic=learned_logic,
            evidence=evidence,
            prompt_text=bundle["prompts"]["generator"],
        )
        validation = validate_questions(
            question_set=generated_questions,
            evidence=evidence,
            prompt_text=bundle["prompts"]["validator"],
        )
        validated_questions = filter_questions_by_decisions(
            question_set=generated_questions,
            decisions=validation,
        )
        evaluation = evaluate_questions(
            question_set=validated_questions,
            prompt_text=bundle["prompts"]["evaluation"],
        )
        final_questions = filter_questions_by_score(
            question_set=validated_questions,
            evaluations=evaluation,
            min_total=38,
        )

        paper_id = paper["paper_id"]
        evidence_by_paper[paper_id] = evidence
        generated_by_paper[paper_id] = generated_questions
        validation_by_paper[paper_id] = validation
        validated_by_paper[paper_id] = validated_questions
        evaluation_by_paper[paper_id] = evaluation
        final_by_paper[paper_id] = final_questions

        total_generated += count_questions(generated_questions)
        total_validated += count_questions(validated_questions)
        total_final += count_questions(final_questions)

    output_dir = bundle["output_dir"]
    save_text(output_dir / "learned_logic.txt", learned_logic)
    save_json(output_dir / "evidence.json", evidence_by_paper)
    save_json(output_dir / "generated_questions.json", generated_by_paper)
    save_json(output_dir / "validation.json", validation_by_paper)
    save_json(output_dir / "validated_questions.json", validated_by_paper)
    save_json(output_dir / "evaluation.json", evaluation_by_paper)
    save_json(output_dir / "final_questions.json", final_by_paper)

    solver_prompt = (
        project_root / "prompts" / "solver_prompt.md"
    ).read_text(encoding="utf-8")
    sa_judge_prompt = (
        project_root / "prompts" / "short_answer_judge_prompt.md"
    ).read_text(encoding="utf-8")
    judger_results = judge_results_by_paper(
        final_questions_by_paper=final_by_paper,
        solver_prompt_text=solver_prompt,
        sa_judge_prompt_text=sa_judge_prompt,
    )
    save_json(output_dir / "judger_results.json", judger_results)

    print(
        {
            "paper_count": len(bundle["papers"]),
            "output_dir": str(output_dir),
            "generated_items": total_generated,
            "validated_items": total_validated,
            "final_items": total_final,
            "judged_papers": len(judger_results),
        }
    )


def count_questions(question_set: dict) -> int:
    return len(question_set.get("mcqs", [])) + len(question_set.get("short_answers", []))



if __name__ == "__main__":
    main()
