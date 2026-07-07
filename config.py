from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
CHAT_COMPLETIONS_URL = "https://api.qingyuntop.top/v1/chat/completions"


PROMPT_FILES = {
    "learn_principle": "learn_principle_prompt.md",
    "get_evidence": "get_evidence_prompt.md",
    "generator": "generator_prompt.md",
    "validator": "validator_prompt.md",
    "evaluation": "evaluation_prompt.md",
    "evaluation_calibration": "evaluation_calibration_prompt.md",
}


DATA_PATHS = {
    "data_dir": PROJECT_ROOT / "data",
    "human_questions": PROJECT_ROOT / "data" / "human_questions.json",
    "output_dir": PROJECT_ROOT / "output",
    "prompts_dir": PROJECT_ROOT / "prompts",
}



STAGE_CONFIG = {
    "learn_principle": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "sk-tnANfHE6FAX4Jjwq6ROMHNVDpzdzDQXzm9Fog8mfFqyypM0c",
        "model_name": "claude-sonnet-4-6",
        "temperature": 0.8,
    },
    "get_evidence": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "sk-tnANfHE6FAX4Jjwq6ROMHNVDpzdzDQXzm9Fog8mfFqyypM0c",
        "model_name": "claude-sonnet-4-6",
        "temperature": 0.8,
    },
    "generator": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "sk-tnANfHE6FAX4Jjwq6ROMHNVDpzdzDQXzm9Fog8mfFqyypM0c",
        "model_name": "claude-sonnet-4-6",
        "temperature": 0.6,
    },
    "validator": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "sk-JQAQ6dDXG5YDnXePYMrb22qNhIdcHzdqBUbJk6mnnYLIpxjn",
        "model_name": "gpt-5.2",
        "temperature": 0.2,
    },
    "evaluation": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "sk-JQAQ6dDXG5YDnXePYMrb22qNhIdcHzdqBUbJk6mnnYLIpxjn",
        "model_name": "gpt-5.2",
        "temperature": 0.2,
    },
    "judger": {
        "provider": "openai",
        "base_url": "https://api.qingyuntop.top/v1/chat/completions",
        "api_key": "sk-JQAQ6dDXG5YDnXePYMrb22qNhIdcHzdqBUbJk6mnnYLIpxjn",
        "model_name": "gpt-4o",
        "temperature": 0.2,
    },
}
