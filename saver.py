import json
from pathlib import Path
from typing import Any


def save_text(path: Path, text: str) -> None:
    """保存text"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text or "", encoding="utf-8")


def save_json(path: Path, payload: Any) -> None:
    """保存json"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )
