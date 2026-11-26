"""Paired A/B experiment: same question/model/settings; separate stateless calls.

Expected answers are used only by scorers, never passed to either LLM call.
An existing run is immutable; use a new run ID to repeat the experiment.
"""
import argparse
import hashlib
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from app.config import Config
from app.service import Advisor
from app.llm import LLMError
from reasoning.kg import ROOT, save_json


def execute(run_id, config, conditions="AB"):
    import re
    if not re.fullmatch(r"[A-Za-z0-9_-]+", run_id):
        raise ValueError("Run ID must contain only letters, numbers, _ and -")
    folder = ROOT / "evaluation/results" / run_id
    folder.mkdir(parents=True, exist_ok=True)
    source = ROOT / "evaluation/cqs.json"
    if not source.exists():
        raise SystemExit("Run python -m evaluation.prepare first.")
    cases = json.loads(source.read_text())
    # No baseline retrieval or completion cache; KG is only used in condition B.
    advisor = Advisor(config)
    if any(c["expected_graph_sha256"] != advisor.reasoner.kg.sha256 for c in cases):
        raise SystemExit("Expected answers belong to a different graph; prepare them again.")
    prompt_hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT / "prompts").glob("*.txt")}
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, stderr=subprocess.DEVNULL, text=True).strip()
    except subprocess.CalledProcessError:
        commit = "PENDING: not a Git checkout"
    try:
        model_identity = advisor.client.runtime_identity()
    except LLMError as error:
        raise SystemExit(str(error))
    identity = {"config": config.public(), "graph_sha256": advisor.reasoner.kg.sha256,
                "cqs_sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "prompt_hashes": prompt_hashes,
                "model_identity": model_identity}
    identity["source_sha256"] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                for folder in ("app", "reasoning", "evaluation")
                                for p in sorted((ROOT / folder).glob("*.py"))}
    manifest_path = folder / "manifest.json"
    if manifest_path.exists():
        old = json.loads(manifest_path.read_text())
        if any(old.get(k) != value for k, value in identity.items()):
            raise SystemExit("Run config/data/prompts changed. Use a new --run-id.")
    else:
        save_json(manifest_path, dict(identity, started_utc=datetime.now(timezone.utc).isoformat(),
                                     python=platform.python_version(), platform=platform.platform(), commit=commit))
    snapshot = folder / "cqs.snapshot.json"
    if not snapshot.exists():
        snapshot.write_bytes(source.read_bytes())
    for i, case in enumerate(cases):
        # Alternate order to reduce systematic time/order effects.
        order = "AB" if i % 2 == 0 else "BA"
        for condition in order:
            if condition not in conditions:
                continue
            path = folder / f"{case['id']}_{condition}.json"
            if path.exists():
                print(f"Preserving {path.name}", flush=True)
                continue
            print(f"Calling {case['id']} condition {condition}", flush=True)
            try:
                output = advisor.answer(case["question"], mode="baseline" if condition == "A" else "grounded")
            except LLMError as error:
                save_json(folder / f"{case['id']}_{condition}.error.json", {"error": str(error), "condition": condition,
                          "cq": case["id"], "time_utc": datetime.now(timezone.utc).isoformat()})
                raise SystemExit(f"Stopped without fabricating an answer: {error}")
            save_json(path, dict(output, cq=case["id"], condition=condition,
                                recorded_utc=datetime.now(timezone.utc).isoformat()))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--conditions", choices=["A", "B", "AB"], default="AB")
    a = p.parse_args()
    execute(a.run_id, Config.load(a.config), a.conditions)
