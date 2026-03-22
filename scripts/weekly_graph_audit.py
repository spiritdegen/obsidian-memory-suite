#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import re

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

texts = {}
for path in files:
    texts[path] = path.read_text(encoding="utf-8", errors="ignore")

all_text = "\n".join(texts.values())

# duplicate titles
titles = defaultdict(list)
for path, text in texts.items():
    if path.name == "_capture-template.md":
        continue
    for line in text.splitlines():
        if line.startswith("# "):
            titles[line.strip()].append(path.relative_to(vault))
            break

for title, paths in titles.items():
    if len(paths) > 1:
        joined = ", ".join(str(p) for p in paths)
        report.append(f"[DUPLICATE_TITLE] {title} -> {joined}")

# notes without tags
for path, text in texts.items():
    if path.name in EXCLUDE_NO_TAGS:
        continue
    if "## Tags" not in text:
        report.append(f"[NO_TAGS] {path.relative_to(vault)}")

# orphan inbox/daily notes
for path in files:
    if path.name == "_capture-template.md":
        continue
    rel = path.relative_to(vault).as_posix().removesuffix(".md")
    if rel.startswith("inbox/") or rel.startswith("knowledge/memory/daily/"):
        wikilink = f"[[{rel}]]"
        count = all_text.count(wikilink)
        if count <= 1:
            report.append(f"[ORPHAN?] {rel}")

# stale links
existing = {p.relative_to(vault).as_posix().removesuffix(".md") for p in files}
link_re = re.compile(r"\[\[([^\]]+)\]\]")
for path, text in texts.items():
    for match in link_re.findall(text):
        target = match.split("|")[0].strip()
        if target and target not in existing:
            report.append(f"[STALE_LINK] {path.relative_to(vault)} -> [[{target}]]")

# simple merge candidates
names = defaultdict(list)
for path in files:
    if path.stem.lower() in EXCLUDE_MERGE_NAMES:
        continue
    names[path.stem.lower()].append(path.relative_to(vault))
for name, paths in names.items():
    if len(paths) > 1:
        joined = ", ".join(str(p) for p in paths)
        report.append(f"[MERGE_CANDIDATE?] {name} -> {joined}")

if not report:
    print("OK: no issues found")
else:
    print("\n".join(report))
