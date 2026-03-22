---
name: moc-router
description: Маршрутизирует заметки и контекст в правильные Map of Content: decisions, triage, bot, automation, infra, crypto.
---

# MOC Router

## Цель
Не складывать заметки хаотично, а сразу связывать их с правильным кластером.

## Домены
- bot
- automation
- infra
- crypto

## Правила маршрутизации
- решение -> moc-decisions
- неясная новая тема -> moc-triage
- OpenClaw / Telegram / skills -> moc-bot
- пайплайны / cron / workflow -> moc-automation
- сервер / VPN / конфиги -> moc-infra
- кошельки / тестнеты / роли -> moc-crypto

## Ограничения
- не создавать новые MOC без необходимости
- не дублировать заметку в несколько MOC без причины
