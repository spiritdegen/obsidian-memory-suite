#!/usr/bin/env python3
from pathlib import Path
import re
import sys

if len(sys.argv) < 2:
    print("usage: auto_tag_normalize.py <note-path>")
    raise SystemExit(1)

path = Path(sys.argv[1])
if not path.exists():
    print(f"file not found: {path}")
    raise SystemExit(1)

text = path.read_text(encoding="utf-8")

lower = text.lower()
tags = []

rules = {
    "#bot": ["openclaw", "telegram", "bot", "skill"],
    "#automation": ["cron", "workflow", "pipeline", "automation"],
    "#infra": ["server", "vpn", "proxy", "config", "infra"],
    "#crypto": ["wallet", "testnet", "crypto", "dex", "okx"],
    "#memory": ["memory", "obsidian", "moc", "zettelkasten"],
}

for tag, keywords in rules.items():
    if any(word in lower for word in keywords):
        tags.append(tag)

tags.append("#inbox")
tags = sorted(set(tags))

text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

if "## Tags" in text:
    text = re.sub(
        r"## Tags\n(?:- .*\n)*",
        "## Tags\n" + "\n".join(f"- {t}" for t in tags) + "\n",
        text,
        flags=re.MULTILINE,
    )
else:
    text += "\n## Tags\n" + "\n".join(f"- {t}" for t in tags) + "\n"

path.write_text(text, encoding="utf-8")
print(path)
print("tags:", ", ".join(tags))
