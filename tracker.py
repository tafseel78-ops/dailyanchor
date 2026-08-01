#!/usr/bin/env python3
import json
import os
import sys
from datetime import date

DATA_FILE = os.path.expanduser("~/dailyanchor/habits.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"habits": [], "log": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_habit(name):
    data = load_data()
    if name in data["habits"]:
        print(f"'{name}' already exists.")
        return
    data["habits"].append(name)
    save_data(data)
    print(f"Added habit: {name}")

def mark_done(name):
    data = load_data()
    if name not in data["habits"]:
        print(f"No such habit: {name}. Add it first with: python tracker.py add \"{name}\"")
        return
    today = str(date.today())
    data["log"].setdefault(today, [])
    if name in data["log"][today]:
        print(f"Already marked '{name}' done today.")
        return
    data["log"][today].append(name)
    save_data(data)
    print(f"Marked done: {name} ({today})")

def list_habits():
    data = load_data()
    if not data["habits"]:
        print("No habits yet. Add one: python tracker.py add \"habit name\"")
        return
    today = str(date.today())
    done_today = data["log"].get(today, [])
    print(f"\nHabits for {today}:")
    for h in data["habits"]:
        mark = "[x]" if h in done_today else "[ ]"
        print(f"  {mark} {h}")
    print()

def main():
    if len(sys.argv) < 2:
        print("Usage: python tracker.py [add|done|list] \"habit name\"")
        return
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) > 2:
        add_habit(sys.argv[2])
    elif cmd == "done" and len(sys.argv) > 2:
        mark_done(sys.argv[2])
    elif cmd == "list":
        list_habits()
    else:
        print("Usage: python tracker.py [add|done|list] \"habit name\"")

if __name__ == "__main__":
    main()
