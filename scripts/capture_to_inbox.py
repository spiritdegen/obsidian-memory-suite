#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import sys
import re

BASE = Path.home() / "obsidian-memory-suite" / "vault-template"
INBOX = BASE / "inbox"
INBOX.mkdir(parents=True, exist_ok=True)

text = " ".join(sys.argv[1:]).strip()
if not text:
    print("usage: capture_to_inbox.py <text>")
    raise SystemExit(1)

ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
slug = re.sub(r"[^a-zA-Z0-9а-яА-Я_-]+", "-", text[:50]).strip("-").lower()
path = INBOX / f"{ts}--{slug}.md"

title = text[:80].strip()
if len(text) > 80:
    title += "..."

content = f"""# {title}

## Source
- chat

## Created
- {datetime.now().isoformat(timespec='seconds')}

## Status
- inbox

## Tags
- #inbox

## Content
{text}
"""

path.write_text(content, encoding="utf-8")
print(path)
