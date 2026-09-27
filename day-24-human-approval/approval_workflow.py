import argparse
import json
from pathlib import Path


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"action": None, "approved": False, "executed": False}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(path: Path, state: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def create_action(path: Path, action: str) -> None:
    save_state(path, {"action": action, "approved": False, "executed": False})
    print("Action proposed. Approval is required.")


def approve_action(path: Path) -> int:
    state = load_state(path)
    if not state.get("action"):
        print("No action is waiting for approval")
        return 1
    state["approved"] = True
    save_state(path, state)
    print("Action approved")
    return 0


def execute_action(path: Path, output_path: Path) -> int:
    state = load_state(path)
    if not state.get("approved"):
        print("Blocked: action has not been approved")
        return 1
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"Executed approved action: {state['action']}\n", encoding="utf-8")
    state["executed"] = True
    save_state(path, state)
    print(f"Action executed: {output_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Require approval before executing an action")
    parser.add_argument("--state", type=Path, default=Path("approval-state.json"))
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("action")
    subparsers.add_parser("approve")
    execute_parser = subparsers.add_parser("execute")
    execute_parser.add_argument("output", type=Path)

    args = parser.parse_args()
    if args.command == "create":
        create_action(args.state, args.action)
        return 0
    if args.command == "approve":
        return approve_action(args.state)
    return execute_action(args.state, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
