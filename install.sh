#!/usr/bin/env bash
set -e

BASE="${1:-$HOME/obsidian-memory-suite-deploy}"
SRC="$HOME/obsidian-memory-suite"

echo "== Installing obsidian-memory-suite =="
echo "Source: $SRC"
echo "Target: $BASE"

mkdir -p "$BASE"
mkdir -p "$BASE/vault"
mkdir -p "$BASE/scripts"
mkdir -p "$BASE/skills"
mkdir -p "$BASE/plugin"

cp -r "$SRC/vault-template/." "$BASE/vault/"
cp -r "$SRC/scripts/." "$BASE/scripts/"
cp -r "$SRC/skills/." "$BASE/skills/"
cp -r "$SRC/plugin/." "$BASE/plugin/"
cp "$SRC/README.md" "$BASE/README.md"

chmod +x "$BASE"/scripts/*.py || true
chmod +x "$BASE"/scripts/*.sh || true

echo
echo "== Done =="
echo "Vault:   $BASE/vault"
echo "Scripts: $BASE/scripts"
echo "Skills:  $BASE/skills"
echo
echo "== Quick checks =="
echo "$BASE/scripts/context_hygiene.py"
echo "$BASE/scripts/weekly_graph_audit.py"
echo "$BASE/scripts/weekly_runner.py"
