# DailyAnchor

A command-line habit and productivity tracker for Android, built with Python and Termux. Uses fixed daily time-anchors — currently structured around daily prayer times — to prompt small, consistent habit check-ins instead of relying on willpower alone.

## Why I built this
I struggled to stick to a routine, but I already have 5 fixed points in my day from prayer. Instead of building a schedule from scratch, I built a tool that hangs small habits onto time-anchors I already keep.

## Features (current)
- Add habits
- Mark habits done for the day
- View today's habit list with completion status
- Data persists locally in JSON, no external database

## Planned
- Prayer-time API integration with push notifications (Termux:API)
- Expense logging
- Weekly streak view

## Tech stack
Python 3 (standard library only), Termux (Android terminal)

## Usage
```
python tracker.py add "habit name"
python tracker.py list
python tracker.py done "habit name"
```

Built entirely on an Android phone using Termux — no laptop required.
