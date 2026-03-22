#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import subprocess
import sys

text = " ".join(sys.argv[1:]).strip()
if not text:
    print("usage: daily_capture.py <text>")
    raise SystemExit(1)

vault = Path.home() / "obsidian-memory-suite" / "vault-template"
scripts = Path.home() / "obsidian-memory-suite" / "scripts"
daily_dir = vault / "knowledge" / "memory" / "daily"
daily_dir.mkdir(parents=True, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
daily_path = daily_dir / f"{today}.md"

if not daily_path.exists():
    content = f"""# {today}

## Context
- 

## Decisions
- 

## Links
- [[knowledge/graph/neural-index]]
- [[knowledge/memory/daily/index]]

## Notes
- 
"""
    daily_path.write_text(content, encoding="utf-8")

doc = daily_path.read_text(encoding="utf-8")
marker = "## Notes\n"
entry = f"- {text}\n"

if marker in doc and entry not in doc:
    doc = doc.replace(marker, marker + entry, 1)
    daily_path.write_text(doc, encoding="utf-8")

subprocess.run([str(scripts / "link_daily_index.py"), str(daily_path)], check=True)
subprocess.run([str(scripts / "link_to_neural_index.py"), str(daily_path)], check=True)

print(daily_path)
