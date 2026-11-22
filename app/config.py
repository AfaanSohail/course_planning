from dataclasses import dataclass
import json
import os
from pathlib import Path
from reasoning.kg import ROOT


@dataclass(frozen=True)
class Config:
    provider: str = "openai_compatible"
    base_url: str = "http://localhost:11434/v1"
    model: str = "SET_MODEL_NAME"
    api_key_env: str = "COURSE_LLM_API_KEY"
    require_api_key: bool = False
    temperature: float = 0.0
    max_tokens: int = 2048
    timeout_seconds: int = 180
    context_max_chars: int = 120000

    @classmethod
    def load(cls, path=None):
        values = json.loads(Path(path).read_text()) if path else {}
        if os.environ.get("COURSE_LLM_MODEL"):
            values["model"] = os.environ["COURSE_LLM_MODEL"]
        if os.environ.get("COURSE_LLM_BASE_URL"):
            values["base_url"] = os.environ["COURSE_LLM_BASE_URL"]
        return cls(**values)

    def public(self):
        from dataclasses import asdict
        return asdict(self)
