from pathlib import Path
import subprocess

COMMANDS = {
    "kernel": ["uname", "-sr"],
    "current_directory": ["pwd"],
    "disk_usage": ["df", "-h", "/"],
}


def run_command(command: list[str]) -> str:
    result = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def create_report(output_path: Path) -> int:
    try:
        sections = [
            f"Kernel:\n{run_command(COMMANDS['kernel'])}",
            f"Current directory:\n{run_command(COMMANDS['current_directory'])}",
            f"Disk usage:\n{run_command(COMMANDS['disk_usage'])}",
        ]
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        print(f"Command failed: {error}")
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"Report created: {output_path}")
    return 0


if __name__ == "__main__":
    import sys

    report_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("command-report.txt")
    raise SystemExit(create_report(report_path))
