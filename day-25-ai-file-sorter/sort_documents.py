from pathlib import Path
import shutil
import sys

CATEGORY_KEYWORDS = {
    "invoices": {"invoice", "payment", "amount", "total", "due"},
    "resumes": {"resume", "experience", "skills", "education", "employment"},
    "reports": {"report", "summary", "analysis", "findings", "results"},
}


def classify_document(text: str) -> str:
    words = set(text.lower().split())
    scores = {
        category: len(words & keywords)
        for category, keywords in CATEGORY_KEYWORDS.items()
    }
    category, score = max(scores.items(), key=lambda item: item[1])
    return category if score else "unknown"


def sort_documents(source: Path, destination: Path) -> int:
    if not source.is_dir():
        print(f"Source directory does not exist: {source}")
        return 2

    for document in sorted(source.iterdir()):
        if not document.is_file():
            continue
        try:
            category = classify_document(document.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            category = "unknown"
        category_dir = destination / category
        category_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(document), category_dir / document.name)
        print(f"Sorted {document.name} -> {category}/")
    return 0


if __name__ == "__main__":
    source = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.home() / "automation-lab" / "documents"
    destination = Path(sys.argv[2]).expanduser() if len(sys.argv) > 2 else source.parent / "sorted-documents"
    raise SystemExit(sort_documents(source, destination))
