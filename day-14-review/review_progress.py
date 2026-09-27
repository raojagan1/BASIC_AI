from pathlib import Path


def review_days(project_root: Path, first_day: int, last_day: int) -> int:
    missing: list[str] = []
    completed = 0
    report_lines = ["AI Automation Learning Review", ""]

    for day in range(first_day, last_day + 1):
        folders = sorted(project_root.glob(f"day-{day:02d}-*"))
        if len(folders) != 1:
            missing.append(f"Day {day}: project folder not found")
            report_lines.append(f"Day {day:02d}: MISSING")
            continue

        project_folder = folders[0]
        readme = project_folder / "README.md"
        if not readme.is_file():
            missing.append(f"Day {day}: README.md not found")
            report_lines.append(f"Day {day:02d}: MISSING README")
            continue

        completed += 1
        report_lines.append(f"Day {day:02d}: COMPLETE ({project_folder.name})")

    report_lines.extend(["", f"Completed: {completed}/{last_day - first_day + 1}"])
    if missing:
        report_lines.append("Missing work:")
        report_lines.extend(missing)
    else:
        report_lines.append("All review projects are documented.")

    report_path = project_root / "day-14-review" / "review-report.txt"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print("\n".join(report_lines))
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(review_days(Path(__file__).resolve().parent.parent, 1, 13))
