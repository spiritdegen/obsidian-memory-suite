#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) < 3:
    print("usage: link_to_moc.py <note-path> <moc-path>")
    raise SystemExit(1)

note_path = Path(sys.argv[1]).resolve()
moc_rel = sys.argv[2]

vault = Path.home() / "obsidian-memory-suite" / "vault-template"
moc_path = vault / moc_rel

if not note_path.exists():
    print(f"note not found: {note_path}")
    raise SystemExit(1)

if not moc_path.exists():
    print(f"moc not found: {moc_path}")
    raise SystemExit(1)

note_rel = note_path.relative_to(vault)
wikilink = f"[[{note_rel.as_posix().removesuffix('.md')}]]"

text = moc_path.read_text(encoding="utf-8")

if wikilink not in text:
    if not text.endswith("\n"):
        text += "\n"
    text += f"\n- {wikilink}\n"
    moc_path.write_text(text, encoding="utf-8")

print(moc_path)
print(wikilink)
