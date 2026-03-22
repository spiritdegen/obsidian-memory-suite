#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import re

vault = Path.home() / "obsidian-memory-suite" / "vault-template"
files = [p for p in vault.rglob("*.md") if p.is_file()]

def detect_tier(days: int) -> str:
    if days <= 7:
        return "#hot"
    if days <= 30:
        return "#warm"
    return "#cold"

for path in files:
    if path.name in {"_capture-template.md", "tags.md"}:
        continue

    text = path.read_text(encoding="utf-8", errors="ignore")

    m = re.search(r"## Created\n- ([0-9T:\-]+)", text)
    if not m:
        continue

    created_raw = m.group(1).strip()
    try:
        created = datetime.fromisoformat(created_raw)
    except ValueError:
        continue

    days = (datetime.now() - created).days
    tier = detect_tier(days)

    lines = text.splitlines()

    if "## Tags" in text:
        start = lines.index("## Tags")
        end = start + 1
        while end < len(lines) and lines[end].startswith("- "):
            end += 1

        tags = [line[2:] for line in lines[start+1:end]]
        tags = [t for t in tags if t not in {"#hot", "#warm", "#cold"}]
        tags.append(tier)
        tags = sorted(set(tags))

        new_block = ["## Tags"] + [f"- {t}" for t in tags]
        lines[start:end] = new_block
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("done")
