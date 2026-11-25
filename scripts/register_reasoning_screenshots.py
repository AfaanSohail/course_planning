"""Register actual Day 5 PNG captures after the user saves them.

No images are generated here. Existing entries from teammates are preserved.
"""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CAPTIONS = {
    "chain": "Actual Day 5 prerequisite-chain execution for CS421, showing the input, graph hash, path validation and a stored-edge excerpt. Full paths are in reasoning/outputs/day5/chain.json.",
    "eligibility": "Actual Day 5 eligibility execution for synthetic S003 and CS421 in Fall 2026, showing met and unmet AND/OR conditions. Full evidence is in reasoning/outputs/day5/eligibility.json.",
    "unlock": "Actual Day 5 hypothetical reverse-unlock execution for synthetic S002 completing CS225, with concurrent-plan credit disabled to match the what-if protocol. Full assumptions and blockers are in reasoning/outputs/day5/unlock.json.",
    "degree": "Actual Day 5 recorded degree-progress execution for synthetic S003, showing count/credit shortfalls and graph evidence. This is not a certified graduation audit. Full groups are in reasoning/outputs/day5/degree.json.",
}


def main():
    entries = []
    for case, caption in CAPTIONS.items():
        path = Path("report/screenshots") / f"afaan_day5_{case}.png"
        actual = ROOT / path
        if not actual.exists():
            raise SystemExit(f"Capture the real terminal output and save {path} first. Manifest unchanged.")
        with Image.open(actual) as image:
            if image.format != "PNG":
                raise SystemExit(f"{path} must be an actual PNG image. Manifest unchanged.")
            image.verify()
        if not (ROOT / f"reasoning/outputs/day5/{case}.json").exists():
            raise SystemExit(f"Missing saved reasoning output for {case}; run reasoning.examples first.")
        entries.append({"path": path.as_posix(), "caption": caption, "iteration": 2})
    manifest = ROOT / "report/screenshots/manifest.json"
    existing = json.loads(manifest.read_text()) if manifest.exists() else []
    if not isinstance(existing, list):
        raise SystemExit("Expected a list in the shared screenshot manifest; inspect before modifying it.")
    replaced = {entry["path"] for entry in entries}
    combined = [entry for entry in existing if entry["path"] not in replaced] + entries
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps(combined, indent=2, ensure_ascii=False) + "\n")
    print("Registered four existing PNG captures and preserved other manifest entries.")
    print("Review each image and caption before committing; image validation does not prove authenticity.")


if __name__ == "__main__":
    main()
