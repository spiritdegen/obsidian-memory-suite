#!/usr/bin/env python3
from pathlib import Path
import subprocess

base = Path.home() / "obsidian-memory-suite" / "scripts"

steps = [
    "tiers.py",
    "context_hygiene.py",
    "weekly_graph_audit.py",
]

for step in steps:
    print(f"==> {step}")
    subprocess.run([str(base / step)], check=True)
    print()
