#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict

vault = Path.home() / "obsidian-memory-suite" / "vault-template"
files = [p for p in vault.rglob("*.md") if p.is_file()]
report = []

EXCLUDE_NO_TAGS = {
    "MEMORY.md",
    "HEARTBEAT.md",
    "GPT.md",
    "tags.md",
    "index.md",
    "neural-index.md",
    "_capture-template.md",
}

EXCLUDE_MERGE_NAMES = {
    "index",
    "tags",
    "memory",
    "heartbeat",
    "gpt",
    "neural-index",
}

# notes without tags
for path in files:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.name in EXCLUDE_NO_TAGS:
        continue
    if "## Tags" not in text:
        report.append(f"[NO_TAGS] {path.relative_to(vault)}")

# duplicate titles
titles = defaultdict(list)
for path in files:
    if path.name == "_capture-template.md":
        continue
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    title = next((line.strip() for line in lines if line.startswith("# ")), None)
    if title:
        titles[title].append(path.relative_to(vault))

for title, paths in titles.items():
    if len(paths) > 1:
        joined = ", ".join(str(p) for p in paths)
        report.append(f"[DUPLICATE_TITLE] {title} -> {joined}")

# simple orphan check
all_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in files)
for path in files:
    if path.name == "_capture-template.md":
        continue
    rel = path.relative_to(vault).as_posix().removesuffix(".md")
    if rel.startswith("inbox/") or rel.startswith("knowledge/memory/daily/"):
        wikilink = f"[[{rel}]]"
        count = all_text.count(wikilink)
        if count <= 1:
            report.append(f"[ORPHAN?] {rel}")

if not report:
    print("OK: no issues found")
else:
    print("\n".join(report))
