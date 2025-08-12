
import os, json, glob, argparse
from ai.client import call_llm
from ai.prompts import ANALYZE_RUN_TEMPLATE

def load_artifacts(path: str) -> dict:
    data = {"failures": [], "results": []}
    for f in glob.glob(os.path.join(path, "*.json")):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                obj = json.load(fh)
            data["results"].append({"name": obj.get("name"), "status": obj.get("status")})
            if obj.get("status") == "failed":
                data["failures"].append(obj)
        except Exception:
            continue
    return data

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", default="ai_suggestions.md")
    args = ap.parse_args()

    artifacts = load_artifacts(args.input)
    prompt = ANALYZE_RUN_TEMPLATE.format(artifacts=json.dumps(artifacts, ensure_ascii=False)[:8000])
    resp = call_llm(prompt)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(resp if isinstance(resp, str) else str(resp))
    print(f"Wrote suggestions to {args.out}")

if __name__ == "__main__":
    main()
