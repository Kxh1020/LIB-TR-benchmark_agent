from pathlib import Path

from pdfminer.high_level import extract_text

from config import DATA_PATHS, PROMPT_FILES


def load_pdf_text(file_path: Path) -> str:
    """解析PDF文件"""
    return extract_text(str(file_path)).strip()


def load_text(file_path: Path) -> str:
    """读取文本文件内容"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def load_prompts(project_root: Path) -> dict:
    """读取prompts内容"""
    prompts_dir = (
        DATA_PATHS["prompts_dir"]
        if project_root == DATA_PATHS["prompts_dir"].parent
        else project_root / "prompts"
    )
    return {
        name: load_text(prompts_dir / filename)
        for name, filename in PROMPT_FILES.items()
    }


def load_papers(project_root: Path) -> list[dict]:
    """读取data目录下全部PDF论文内容"""
    data_dir = (
        DATA_PATHS["data_dir"]
        if project_root == DATA_PATHS["data_dir"].parent
        else project_root / "data"
    )
    paper_paths = sorted(data_dir.glob("*.pdf"))

    return [
        {
            "paper_id": paper_path.stem,
            "paper_text": load_pdf_text(paper_path),
            "paper_path": paper_path,
        }
        for paper_path in paper_paths
    ]


def load_human_questions(project_root: Path) -> dict:
    """读取人类问题集内容"""
    human_questions_path = (
        DATA_PATHS["human_questions"]
        if project_root == DATA_PATHS["human_questions"].parent.parent
        else project_root / "data" / "human_questions.txt"
    )
    return {
        "human_questions_text": load_text(human_questions_path),
    }


def load_inputs(project_root: Path) -> dict:
    """读取全部文件"""
    return {
        "papers": load_papers(project_root),
        **load_human_questions(project_root),
        "prompts": load_prompts(project_root),
        "output_dir": (
            DATA_PATHS["output_dir"]
            if project_root == DATA_PATHS["output_dir"].parent
            else project_root / "output"
        ),
    }
