from collections import Counter
from pathlib import Path
import re
import sys

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "in", "is", "it", "of", "on", "or", "that", "the", "this", "to",
    "with", "will",
}


def summarize(text: str, sentence_count: int = 2) -> str:
    sentences = [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text.strip()) if sentence.strip()]
    if len(sentences) <= sentence_count:
        return " ".join(sentences)

    words_by_sentence = [
        [word for word in re.findall(r"[a-z]+", sentence.lower()) if word not in STOP_WORDS]
        for sentence in sentences
    ]
    frequencies = Counter(word for words in words_by_sentence for word in words)
    scores = [sum(frequencies[word] for word in words) for words in words_by_sentence]
    selected_indexes = sorted(
        sorted(range(len(sentences)), key=lambda index: scores[index], reverse=True)[:sentence_count]
    )
    return " ".join(sentences[index] for index in selected_indexes)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: summarize_document.py INPUT_FILE OUTPUT_FILE")
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    if not input_path.is_file():
        print(f"Input document does not exist: {input_path}")
        return 2

    text = input_path.read_text(encoding="utf-8")
    summary = summarize(text)
    output_path.write_text(summary + "\n", encoding="utf-8")
    print(f"Summary created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
