from pathlib import Path
import re
import sys

KEYWORDS = {
    "billing": {"bill", "billing", "invoice", "payment", "charge", "refund"},
    "technical": {"error", "bug", "crash", "login", "password", "server", "broken"},
    "support": {"help", "question", "support", "how", "problem", "request"},
}


def classify(text: str) -> tuple[str, int]:
    words = set(re.findall(r"[a-z]+", text.lower()))
    scores = {
        category: len(words & keywords)
        for category, keywords in KEYWORDS.items()
    }
    category, score = max(scores.items(), key=lambda item: item[1])
    if score == 0:
        return "other", 0
    return category, score


def main() -> int:
    if len(sys.argv) == 2 and Path(sys.argv[1]).is_file():
        text = Path(sys.argv[1]).read_text(encoding="utf-8")
    elif len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        print("Usage: classify_text.py TEXT_OR_FILE")
        return 2

    category, score = classify(text)
    print(f"category={category}")
    print(f"matched_keywords={score}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
