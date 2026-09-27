import argparse
import json
from pathlib import Path


def load_tasks(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as task_file:
        return json.load(task_file)


def save_tasks(path: Path, tasks: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as task_file:
        json.dump(tasks, task_file, indent=2)
        task_file.write("\n")


def add_task(path: Path, title: str) -> None:
    tasks = load_tasks(path)
    next_id = max((int(task["id"]) for task in tasks), default=0) + 1
    tasks.append({"id": next_id, "title": title, "completed": False})
    save_tasks(path, tasks)
    print(f"Added task {next_id}: {title}")


def list_tasks(path: Path) -> None:
    tasks = load_tasks(path)
    if not tasks:
        print("No tasks")
        return
    for task in tasks:
        status = "done" if task["completed"] else "open"
        print(f"[{status}] {task['id']}: {task['title']}")


def complete_task(path: Path, task_id: int) -> int:
    tasks = load_tasks(path)
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(path, tasks)
            print(f"Completed task {task_id}")
            return 0
    print(f"Task not found: {task_id}")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Manage tasks in a JSON file")
    parser.add_argument("--file", type=Path, default=Path("tasks.json"))
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    subparsers.add_parser("list")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)

    args = parser.parse_args()
    if args.command == "add":
        add_task(args.file, args.title)
        return 0
    if args.command == "list":
        list_tasks(args.file)
        return 0
    return complete_task(args.file, args.id)


if __name__ == "__main__":
    raise SystemExit(main())
