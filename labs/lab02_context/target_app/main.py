from __future__ import annotations

import argparse

from sort_rules import sort_tasks
from storage import load_tasks, save_tasks


def cmd_list() -> int:
    tasks = sort_tasks(load_tasks())
    if not tasks:
        print("(empty)")
        return 0
    for task in tasks:
        status = "x" if task["done"] else " "
        print(f'{task["id"]:>3} [{status}] (p{task["priority"]}) {task["title"]}  {task["created_at"]}')
    return 0


def cmd_add(title: str, priority: int) -> int:
    tasks = load_tasks()
    next_id = (max((t["id"] for t in tasks), default=0)) + 1
    # Keep the schema fixed per constraints.
    from datetime import datetime, timezone

    tasks.append(
        {
            "id": next_id,
            "title": title,
            "priority": priority,
            "created_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "done": False,
        }
    )
    save_tasks(tasks)
    print(f"added #{next_id}")
    return 0


def cmd_done(task_id: int) -> int:
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"done #{task_id}")
            return 0
    print(f"not found: {task_id}")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list")

    add = sub.add_parser("add")
    add.add_argument("title")
    add.add_argument("--priority", type=int, choices=[1, 2, 3], default=2)

    done = sub.add_parser("done")
    done.add_argument("id", type=int)

    args = parser.parse_args()
    if args.cmd == "list":
        return cmd_list()
    if args.cmd == "add":
        return cmd_add(args.title, args.priority)
    if args.cmd == "done":
        return cmd_done(args.id)
    raise SystemExit("unknown command")


if __name__ == "__main__":
    raise SystemExit(main())

