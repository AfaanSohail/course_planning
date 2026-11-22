"""Minimal OpenAI-compatible chat client, including local Ollama.

Requests/responses are recorded without authorization headers. No mock provider
can be selected by the evaluation CLI. Errors remain errors, never fake answers.
"""
import os
from time import perf_counter
from urllib.parse import urlsplit
import requests


class LLMError(RuntimeError):
    pass


class LLMClient:
    def __init__(self, config):
        self.config = config

    def runtime_identity(self):
        """Freeze the actual local model digest/version across separate A/B days."""
        c = self.config
        if c.provider != "ollama":
            return {"provider": c.provider, "requested_model": c.model,
                    "model_digest_verified": False, "note": "Hosted identity also depends on provider response metadata."}
        origin = urlsplit(c.base_url)
        url = f"{origin.scheme}://{origin.netloc}"
        try:
            version_response = requests.get(url + "/api/version", timeout=10)
            tags_response = requests.get(url + "/api/tags", timeout=10)
            version_response.raise_for_status(); tags_response.raise_for_status()
            names = {c.model, c.model + ":latest"}
            model = next(m for m in tags_response.json()["models"] if m["name"] in names)
            return {"provider": "ollama", "runtime_version": version_response.json()["version"],
                    "requested_model": c.model, "name": model["name"], "digest": model["digest"],
                    "details": model.get("details", {}), "model_digest_verified": True}
        except (requests.RequestException, KeyError, ValueError, StopIteration):
            raise LLMError("Ollama identity unavailable: start the server and create the configured local model.") from None

    def complete(self, messages):
        c = self.config
        if not c.model or c.model == "SET_MODEL_NAME":
            raise LLMError("Set the real provider/model in config/local.json or COURSE_LLM_MODEL.")
        key = os.environ.get(c.api_key_env)
        if c.require_api_key and not key:
            raise LLMError(f"Set {c.api_key_env} in the environment, never in code/config.")
        parsed = urlsplit(c.base_url)
        if parsed.username or parsed.password or parsed.query:
            raise LLMError("Credentials/query strings are not permitted in base_url.")
        if parsed.scheme != "https" and parsed.hostname not in {"localhost", "127.0.0.1", "::1"}:
            raise LLMError("Use HTTPS for a remote provider.")
        payload = {"model": c.model, "messages": messages, "temperature": c.temperature,
                   "max_tokens": c.max_tokens, "stream": False}
        headers = {"Content-Type": "application/json"}
        if key:
            headers["Authorization"] = f"Bearer {key}"
        started = perf_counter()
        try:
            response = requests.post(c.base_url.rstrip("/") + "/chat/completions", json=payload,
                                     headers=headers, timeout=c.timeout_seconds)
        except requests.RequestException as error:
            raise LLMError(f"Provider connection failed ({type(error).__name__}).") from None
        if not response.ok:
            raise LLMError(f"Provider returned HTTP {response.status_code}; inspect provider/model/settings locally.")
        try:
            raw = response.json()
            answer = raw["choices"][0]["message"]["content"]
            finish = raw["choices"][0].get("finish_reason")
            if not isinstance(answer, str) or not answer.strip():
                raise ValueError("Empty answer")
        except (KeyError, IndexError, ValueError, TypeError):
            raise LLMError("Provider response was not a nonempty chat completion.") from None
        return {"answer": answer, "request": payload, "raw": raw,
                "runtime_ms": (perf_counter() - started) * 1000,
                "finish_reason": finish, "truncated": finish == "length"}
