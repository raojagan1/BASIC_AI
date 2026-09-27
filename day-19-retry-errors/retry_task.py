from collections.abc import Callable
import sys
import time


def run_with_retries(
    operation: Callable[[], str],
    attempts: int = 3,
    delay_seconds: float = 1.0,
) -> tuple[bool, list[str]]:
    if attempts < 1 or delay_seconds < 0:
        raise ValueError("attempts must be positive and delay cannot be negative")

    errors: list[str] = []
    for attempt in range(1, attempts + 1):
        try:
            result = operation()
            return True, [f"Attempt {attempt}: success ({result})"]
        except Exception as error:
            message = f"Attempt {attempt}: {error}"
            errors.append(message)
            if attempt < attempts:
                time.sleep(delay_seconds)
    return False, errors


def simulated_operation(failures_before_success: int) -> Callable[[], str]:
    state = {"attempts": 0}

    def operation() -> str:
        state["attempts"] += 1
        if state["attempts"] <= failures_before_success:
            raise RuntimeError("temporary service failure")
        return "operation completed"

    return operation


def main() -> int:
    failures_before_success = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    success, messages = run_with_retries(
        simulated_operation(failures_before_success),
        attempts=3,
        delay_seconds=0,
    )
    print("\n".join(messages))
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
