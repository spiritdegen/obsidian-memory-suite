#!/usr/bin/env bash
set -euo pipefail

TEXT="$*"
if [ -z "$TEXT" ]; then
  echo "usage: obsidian_capture.sh <text>"
  exit 1
fi

BASE="$HOME/obsidian-memory-suite/scripts"

NOTE_PATH="$("$BASE/capture_to_inbox.py" "$TEXT" | tail -n 1)"
"$BASE/process_inbox_note.py" "$NOTE_PATH"

echo
echo "saved: $NOTE_PATH"
