# LIB-TR Benchmark Agent

This project is a lightweight benchmark generation pipeline for engineering reasoning tasks in lithium-ion battery thermal runaway research.

It takes:
- research papers in PDF format
- a human-written question collection

and runs the following pipeline:
- learn human question design logic
- extract evidence from each paper
- generate candidate questions
- validate admissibility
- evaluate question quality
- filter final questions
- let a solver answer the final questions and judge the results

## Project Structure

```text
project/
├── main.py
├── config.py
├── loader.py
├── saver.py
├── data/
├── output/
├── prompts/
└── modules/
    ├── generator.py
    ├── validator.py
    ├── evaluator.py
    ├── judger.py
    └── utils.py
```

## Input

The pipeline expects:
- all PDF papers under `data/`
- one human question file at `data/human_questions.txt`
- prompt files under `prompts/`

`loader.py` scans all `.pdf` files in `data/` and loads them as papers.

## Main Pipeline

`main.py` runs the full workflow:

1. Load papers, human questions, and prompts
2. Learn human question design logic
3. For each paper:
   - extract evidence
   - generate questions
   - validate questions
   - filter accepted questions
   - evaluate question quality
   - filter questions by score
4. Save final benchmark artifacts
5. Run the judger on final questions

## Output

The pipeline writes the following files to `output/`:

- `learned_logic.txt`
- `evidence.json`
- `generated_questions.json`
- `validation.json`
- `validated_questions.json`
- `evaluation.json`
- `final_questions.json`
- `judger_results.json`

Most JSON outputs are grouped by `paper_id`.

## How to Run

From the project root:

```bash
python main.py
```

## Judger

The judger performs two tasks:

- MCQ: calls the solver and compares predicted options with the gold answer using exact match
- Short answer: calls the solver, then uses an LLM judge to compare the prediction with the gold answer and assign a score between `0` and `1`

Related prompt files:
- `prompts/solver_prompt.md`
- `prompts/short_answer_judge_prompt.md`

## Notes

- Model settings are currently defined in `config.py`
- The current implementation is designed for simple experimentation and debugging, not for production deployment
