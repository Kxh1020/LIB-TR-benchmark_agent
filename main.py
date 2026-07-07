from pathlib import Path

from modules.generator import (
    generate_evidence,
    generate_questions,
    learn_human_principle,
)
from modules.evaluator import calibrate_evaluator, evaluate_questions
from loader import load_inputs
from saver import save_json, save_text
from modules.utils import filter_questions_by_decisions, filter_questions_by_score
from modules.validator import validate_questions
from modules.judger import judge_results_by_paper


def build_sequential_paper_bundles(
    papers: list[dict],
    bundle_size: int = 3,
) -> list[dict]:
    """按顺序把相邻论文捆绑成 bundle。"""
    bundles = []

    for index in range(0, len(papers), bundle_size):
        bundle_papers = papers[index:index + bundle_size]
        if not bundle_papers:
            continue

        paper_ids = [paper["paper_id"] for paper in bundle_papers]
        bundle_id = "__".join(paper_ids)
        bundles.append(
            {
                "bundle_id": bundle_id,
                "paper_ids": paper_ids,
                "papers": bundle_papers,
            }
        )

    return bundles


def build_evidence_bundle(bundle: dict, evidence_by_paper: dict) -> dict:
    """把多篇论文的 evidence 合成一个生成/验证用 bundle。"""
    evidence_bundles = []

    for paper_id in bundle["paper_ids"]:
        paper_evidence = evidence_by_paper.get(paper_id, {})
        claims = []

        for index, claim in enumerate(paper_evidence.get("claims", []), start=1):
            claims.append(
                {
                    "claim_id": f"{paper_id}:C{index:03d}",
                    **claim,
                }
            )

        evidence_bundles.append(
            {
                "paper_id": paper_id,
                "claims": claims,
            }
        )

    return {
        "bundle_id": bundle["bundle_id"],
        "paper_ids": bundle["paper_ids"],
        "evidence_bundles": evidence_bundles,
    }


def main() -> None:
    project_root = Path(__file__).resolve().parent
    bundle = load_inputs(project_root=project_root)

    learned_logic = learn_human_principle(
        human_questions_text=bundle["human_questions_text"],
        prompt_text=bundle["prompts"]["learn_principle"],
    )
    calibration_anchors = calibrate_evaluator(
        human_questions_text=bundle["human_questions_text"],
        prompt_text=bundle["prompts"]["evaluation_calibration"],
    )
    evidence_by_paper = {}

    for paper in bundle["papers"]:
        evidence = generate_evidence(
            paper_text=paper["paper_text"],
            paper_id=paper["paper_id"],
            prompt_text=bundle["prompts"]["get_evidence"],
        )
        evidence_by_paper[paper["paper_id"]] = evidence

    paper_bundles = build_sequential_paper_bundles(bundle["papers"])
    evidence_by_bundle = {
        paper_bundle["bundle_id"]: build_evidence_bundle(
            paper_bundle,
            evidence_by_paper,
        )
        for paper_bundle in paper_bundles
    }
    generated_by_bundle = {}
    validation_by_bundle = {}
    validated_by_bundle = {}
    evaluation_by_bundle = {}
    final_by_bundle = {}

    total_generated = 0
    total_validated = 0
    total_final = 0

    for paper_bundle in paper_bundles:
        bundle_id = paper_bundle["bundle_id"]
        evidence_bundle = evidence_by_bundle[bundle_id]

        generated_questions = generate_questions(
            source_id=bundle_id,
            learned_logic=learned_logic,
            evidence=evidence_bundle,
            prompt_text=bundle["prompts"]["generator"],
        )
        validation = validate_questions(
            question_set=generated_questions,
            evidence=evidence_bundle,
            prompt_text=bundle["prompts"]["validator"],
        )
        validated_questions = filter_questions_by_decisions(
            question_set=generated_questions,
            decisions=validation,
        )
        evaluation = evaluate_questions(
            question_set=validated_questions,
            prompt_text=bundle["prompts"]["evaluation"],
            calibration_anchors=calibration_anchors,
        )
        final_questions = filter_questions_by_score(
            question_set=validated_questions,
            evaluations=evaluation,
            min_total=38,
        )

        generated_by_bundle[bundle_id] = generated_questions
        validation_by_bundle[bundle_id] = validation
        validated_by_bundle[bundle_id] = validated_questions
        evaluation_by_bundle[bundle_id] = evaluation
        final_by_bundle[bundle_id] = final_questions

        total_generated += count_questions(generated_questions)
        total_validated += count_questions(validated_questions)
        total_final += count_questions(final_questions)

    output_dir = bundle["output_dir"]
    learn_principle_dir = output_dir / "learn_principle"
    calibration_dir = output_dir / "evaluation_calibration"
    get_evidence_dir = output_dir / "get_evidence"
    generator_dir = output_dir / "generator"
    validator_dir = output_dir / "validator"
    evaluation_dir = output_dir / "evaluation"
    judger_dir = output_dir / "judger"

    save_text(learn_principle_dir / "learned_principle.txt", learned_logic)
    save_json(calibration_dir / "calibration_anchors.json", calibration_anchors)
    save_json(get_evidence_dir / "evidence_by_paper.json", evidence_by_paper)
    save_json(get_evidence_dir / "evidence_by_bundle.json", evidence_by_bundle)
    save_json(generator_dir / "generated_questions.json", generated_by_bundle)
    save_json(validator_dir / "validation.json", validation_by_bundle)
    save_json(validator_dir / "validated_questions.json", validated_by_bundle)
    save_json(evaluation_dir / "evaluation.json", evaluation_by_bundle)
    save_json(evaluation_dir / "final_questions.json", final_by_bundle)

    solver_prompt = (
        project_root / "prompts" / "solver_prompt.md"
    ).read_text(encoding="utf-8")
    sa_judge_prompt = (
        project_root / "prompts" / "short_answer_judge_prompt.md"
    ).read_text(encoding="utf-8")
    judger_results = judge_results_by_paper(
        final_questions_by_paper=final_by_bundle,
        solver_prompt_text=solver_prompt,
        sa_judge_prompt_text=sa_judge_prompt,
    )
    save_json(judger_dir / "judger_results.json", judger_results)

    print(
        {
            "paper_count": len(bundle["papers"]),
            "bundle_count": len(paper_bundles),
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
