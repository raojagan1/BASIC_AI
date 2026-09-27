from datetime import date
from pathlib import Path
import sys


def rename_files(folder: Path, prefix: str) -> int:
    if not folder.is_dir():
        print(f"Folder does not exist: {folder}")
        return 2

    files = sorted(path for path in folder.iterdir() if path.is_file())
    for number, file_path in enumerate(files, start=1):
        new_name = f"{prefix}-{number:03d}{file_path.suffix.lower()}"
        destination = folder / new_name
        if destination != file_path and destination.exists():
            print(f"Refusing to overwrite existing file: {destination}")
            return 1
        file_path.rename(destination)
        print(f"Renamed {file_path.name} -> {new_name}")

    print(f"Renamed {len(files)} file(s)")
    return 0


def main() -> int:
    folder = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.home() / "automation-lab" / "rename-inbox"
    prefix = sys.argv[2] if len(sys.argv) > 2 else date.today().isoformat()
    return rename_files(folder, prefix)


if __name__ == "__main__":
    raise SystemExit(main())
