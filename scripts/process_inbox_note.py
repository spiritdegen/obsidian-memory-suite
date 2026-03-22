#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

if len(sys.argv) < 2:
    print("usage: process_inbox_note.py <note-path>")
    raise SystemExit(1)

note = Path(sys.argv[1]).resolve()
base = Path.home() / "obsidian-memory-suite" / "scripts"

if not note.exists():
    print(f"note not found: {note}")
    raise SystemExit(1)

subprocess.run([str(base / "auto_tag_normalize.py"), str(note)], check=True)

route = subprocess.check_output(
    [str(base / "route_to_moc.py"), str(note)],
    text=True
).strip()

subprocess.run([str(base / "link_to_moc.py"), str(note), route], check=True)
subprocess.run([str(base / "link_to_neural_index.py"), str(note)], check=True)

print("processed:", note)
print("route:", route)
