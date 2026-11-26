"""Language mix of ALL my repos (private included), storagebits and algotitanhq, written to gen/langs.json.

The daily Action only sees public repos (github.token), so this runs locally with `gh` auth:
    python3 gen/langs.py && git add gen/langs.json && git commit -m "Languages: refresh" && git push
Only language names and shares are written, never a repo name. gen.py uses this file when present.
"""
import json, os, subprocess
SKIP_LANGS = {"HTML", "CSS", "CMake", "Makefile", "Dockerfile", "Batchfile", "Procfile", "Jupyter Notebook"}  # same as gen.py


def gh(path):
    out = subprocess.run(["gh", "api", "--paginate", path], capture_output=True, text=True, check=True).stdout
    return json.loads(out.replace("]\n[", ",").replace("][", ","))


repos = {r["full_name"]: r for r in gh("/user/repos?affiliation=owner&per_page=100") + gh("/orgs/algotitanhq/repos?type=all&per_page=100")}
repos = [r for r in repos.values() if not r["fork"] and not r["archived"] and r["name"] != "storagebits"]
langs = {}
for r in repos:
    for k, v in gh(f"/repos/{r['full_name']}/languages").items():
        if k not in SKIP_LANGS: langs[k] = langs.get(k, 0) + v
total = sum(langs.values()) or 1
top = [[k, round(v / total, 4)] for k, v in sorted(langs.items(), key=lambda kv: -kv[1])[:6]]
path = os.path.join(os.path.dirname(__file__), "langs.json")
with open(path, "w") as f:
    json.dump({"repos": len(repos), "langs": top}, f, indent=1)
print(len(repos), "repos:", ", ".join(f"{k} {v * 100:.1f}%" for k, v in top))
