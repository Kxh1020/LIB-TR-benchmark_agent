from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
CHAT_COMPLETIONS_URL = "https://api.qingyuntop.top/v1/chat/completions"


PROMPT_FILES = {
    "learn_logic": "learn_logic_prompt.md",
    "evidence_extract": "evidence_extract_prompt.md",
    "generator": "generator_prompt.md",
    "validator": "validator_prompt.md",
    "evaluation": "evaluation_prompt.md",
    "evaluation_calibration": "evaluation_calibration_prompt.md",
}


DATA_PATHS = {
    "data_dir": PROJECT_ROOT / "data",
    "human_questions": PROJECT_ROOT / "data" / "human_questions.txt",
    "output_dir": PROJECT_ROOT / "output",
    "prompts_dir": PROJECT_ROOT / "prompts",
}


"""敏感apikey"""
STAGE_CONFIG = {
    "learn_logic": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "YOUR_API_KEY",
        "model_name": "gpt-5.2",
        "temperature": 0.2,
    },
    "evidence_extract": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "YOUR_API_KEY",
        "model_name": "gpt-5.2",
        "temperature": 0.2,
    },
    "generator": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "YOUR_API_KEY",
        "model_name": "gpt-5.2",
        "temperature": 0.6,
    },
    "validator": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "YOUR_API_KEY",
        "model_name": "gpt-5.2",
        "temperature": 0.2,
    },
    "evaluation": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "YOUR_API_KEY",
        "model_name": "gpt-5.2",
        "temperature": 0.2,
    },
    "judger": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "YOUR_API_KEY",
        "model_name": "gpt-5.2",
        "temperature": 0.2,
    },
}
