#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

vault = Path.home() / "obsidian-memory-suite" / "vault-template"
daily_dir = vault / "knowledge" / "memory" / "daily"
daily_dir.mkdir(parents=True, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
path = daily_dir / f"{today}.md"

if not path.exists():
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
    path.write_text(content, encoding="utf-8")

print(path)
