#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) < 2:
    print("usage: route_to_moc.py <note-path>")
    raise SystemExit(1)

path = Path(sys.argv[1])
if not path.exists():
    print(f"file not found: {path}")
    raise SystemExit(1)

text = path.read_text(encoding="utf-8").lower()

routes = [
    ("maps/moc-automation.md", ["#automation", "cron", "workflow", "pipeline", "автоматиза"]),
    ("maps/moc-infra.md", ["#infra", "server", "vpn", "proxy", "config", "infra"]),
    ("maps/moc-crypto.md", ["#crypto", "wallet", "testnet", "dex", "okx"]),
    ("maps/moc-bot.md", ["#bot", "openclaw", "telegram", "skill", "бот"]),
]

target = "maps/moc-triage.md"
for route, keys in routes:
    if any(k in text for k in keys):
        target = route
        break

print(target)
