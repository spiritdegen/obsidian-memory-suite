#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) < 2:
    print("usage: link_daily_index.py <daily-note-path>")
    raise SystemExit(1)

note_path = Path(sys.argv[1]).resolve()
vault = Path.home() / "obsidian-memory-suite" / "vault-template"
index_path = vault / "knowledge/memory/daily/index.md"

note_rel = note_path.relative_to(vault)
wikilink = f"[[{note_rel.as_posix().removesuffix('.md')}]]"

text = index_path.read_text(encoding="utf-8")
if wikilink not in text:
    if not text.endswith("\n"):
        text += "\n"
    text += f"\n- {wikilink}\n"
    index_path.write_text(text, encoding="utf-8")

print(index_path)
print(wikilink)
