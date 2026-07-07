#!/usr/bin/env python3
"""Export markdown prompts into a Python prompt registry module."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def _to_key(filename: str) -> str:
    # get_evidence_prompt.md -> get_evidence
    return filename.replace("_prompt.md", "").replace(".md", "")


def export_prompts(md_dir: Path, out_py: Path, out_meta: Path | None = None) -> None:
    if not md_dir.exists():
        raise FileNotFoundError(f"Prompt directory not found: {md_dir}")

    prompt_files = sorted(md_dir.glob("*.md"))
    prompts: dict[str, str] = {}
    sources: dict[str, str] = {}

    for p in prompt_files:
        key = _to_key(p.name)
        prompts[key] = p.read_text(encoding="utf-8").rstrip() + "\n"
        sources[key] = str(p)

    lines: list[str] = []
    lines.append('"""Auto-generated prompt registry from markdown files."""')
    lines.append("")
    lines.append("PROMPTS = {")
    for key in sorted(prompts):
        lines.append(f"    {key!r}: '''")
        lines.extend(prompts[key].splitlines())
        lines.append("''',")
    lines.append("}")
    lines.append("")
    lines.append("")
    lines.append("def get_prompt(name: str) -> str:")
    lines.append('    if name not in PROMPTS:')
    lines.append('        available = ", ".join(sorted(PROMPTS))')
    lines.append('        raise KeyError(f"Unknown prompt: {name}. Available: {available}")')
    lines.append("    return PROMPTS[name]")
    lines.append("")
    lines.append("")
    lines.append("def list_prompts() -> list[str]:")
    lines.append("    return sorted(PROMPTS)")
    lines.append("")

    out_py.parent.mkdir(parents=True, exist_ok=True)
    out_py.write_text("\n".join(lines), encoding="utf-8")

    if out_meta is not None:
        out_meta.parent.mkdir(parents=True, exist_ok=True)
        out_meta.write_text(
            json.dumps(
                {
                    "source_dir": str(md_dir),
                    "count": len(prompts),
                    "prompt_files": [p.name for p in prompt_files],
                    "sources": sources,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--md-dir",
        default="/Users/k/Desktop/Benchmark-agent_副本/project/prompts",
        help="Directory containing markdown prompt files.",
    )
    parser.add_argument(
        "--out-py",
        default="/Users/k/Desktop/Benchmark-agent_副本/project/prompts_py/prompts.py",
        help="Output Python module path.",
    )
    parser.add_argument(
        "--out-meta",
        default="/Users/k/Desktop/Benchmark-agent_副本/project/prompts_py/prompts_meta.json",
        help="Output metadata json path.",
    )
    args = parser.parse_args()

    export_prompts(
        md_dir=Path(args.md_dir),
        out_py=Path(args.out_py),
        out_meta=Path(args.out_meta),
    )


if __name__ == "__main__":
    main()
