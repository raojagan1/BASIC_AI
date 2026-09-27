from pathlib import Path
import argparse
import time


def scan_folder(folder: Path, known_files: set[Path]) -> set[Path]:
    current_files = {path for path in folder.iterdir() if path.is_file()}
    for new_file in sorted(current_files - known_files):
        print(f"New file detected: {new_file.name}")
    return current_files


def main() -> int:
    parser = argparse.ArgumentParser(description="Monitor a folder for new files")
    parser.add_argument("folder", type=Path)
    parser.add_argument("--interval", type=float, default=2.0)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()

    folder = args.folder.expanduser()
    if not folder.is_dir():
        print(f"Folder does not exist: {folder}")
        return 2
    if args.interval <= 0:
        print("Interval must be greater than zero")
        return 2

    known_files: set[Path] = set()
    if args.once:
        scan_folder(folder, known_files)
        return 0

    print(f"Monitoring {folder}. Press Ctrl+C to stop.")
    try:
        while True:
            known_files = scan_folder(folder, known_files)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
