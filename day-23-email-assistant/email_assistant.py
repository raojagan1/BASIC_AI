from pathlib import Path
import re
import sys

INTENT_KEYWORDS = {
    "billing": {"bill", "billing", "invoice", "payment", "charge", "refund"},
    "technical": {"error", "bug", "crash", "login", "password", "server", "broken"},
}


def detect_intent(message: str) -> str:
    words = set(re.findall(r"[a-z]+", message.lower()))
    scores = {
        intent: len(words & keywords)
        for intent, keywords in INTENT_KEYWORDS.items()
    }
    intent, score = max(scores.items(), key=lambda item: item[1])
    return intent if score else "general"


def create_draft(message: str) -> str:
    intent = detect_intent(message)
    responses = {
        "billing": (
            "Thank you for contacting us about your billing request. "
            "We will review the invoice and payment details and follow up with you."
        ),
        "technical": (
            "Thank you for reporting this technical issue. "
            "We will investigate the error and follow up with troubleshooting steps."
        ),
        "general": (
            "Thank you for your message. "
            "We have received your request and will follow up shortly."
        ),
    }
    return (
        f"Intent: {intent}\n\n"
        "Draft reply:\n"
        "Hello,\n\n"
        f"{responses[intent]}\n\n"
        "Regards,\nAutomation Support\n"
    )


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: email_assistant.py INCOMING_EMAIL OUTPUT_DRAFT")
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    if not input_path.is_file():
        print(f"Incoming email does not exist: {input_path}")
        return 2

    draft = create_draft(input_path.read_text(encoding="utf-8"))
    output_path.write_text(draft, encoding="utf-8")
    print(f"Draft created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
