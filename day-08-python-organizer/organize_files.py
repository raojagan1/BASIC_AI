from pathlib import Path
import shutil
import sys

CATEGORIES = {
    ".pdf": "pdf",
    ".txt": "text",
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
}


def organize_files(source: Path, destination: Path) -> int:
    if not source.is_dir():
        print(f"Source directory does not exist: {source}")
        return 2

    moved_count = 0
    for file_path in sorted(source.iterdir()):
        if not file_path.is_file():
            continue

        category = CATEGORIES.get(file_path.suffix.lower(), "other")
        category_dir = destination / category
        category_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file_path), category_dir / file_path.name)
        print(f"Moved {file_path.name} -> {category}/")
        moved_count += 1

    print(f"Organized {moved_count} file(s)")
    return 0


def main() -> int:
    source = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.home() / "automation-lab" / "inbox"
    destination = Path(sys.argv[2]).expanduser() if len(sys.argv) > 2 else source.parent / "organized"
    return organize_files(source, destination)


if __name__ == "__main__":
    raise SystemExit(main())
