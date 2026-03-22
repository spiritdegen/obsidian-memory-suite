#!/usr/bin/env bash
set -e

BASE="$HOME/obsidian-memory-suite"
VAULT="$BASE/vault-template"

echo "== Vault path =="
echo "$VAULT"
echo

echo "== Created / changed files =="
find "$BASE" -maxdepth 6 -type f | sort
echo

echo "== Verification commands =="
echo "~/obsidian-memory-suite/scripts/capture_to_inbox.py \"Тестовая заметка\""
echo "~/obsidian-memory-suite/scripts/process_inbox_note.py <path-to-note>"
echo "~/obsidian-memory-suite/scripts/daily_capture.py \"Запись в daily\""
echo "~/obsidian-memory-suite/scripts/context_hygiene.py"
echo "~/obsidian-memory-suite/scripts/weekly_graph_audit.py"
echo "~/obsidian-memory-suite/scripts/weekly_runner.py"
