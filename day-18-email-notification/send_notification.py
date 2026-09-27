from email.message import EmailMessage
from pathlib import Path
import sys


def create_notification(recipient: str, subject: str, body: str, output_path: Path) -> None:
    message = EmailMessage()
    message["From"] = "automation@localhost"
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(bytes(message))


def main() -> int:
    if len(sys.argv) != 5:
        print("Usage: send_notification.py RECIPIENT SUBJECT BODY OUTPUT_FILE")
        return 2

    recipient, subject, body, output_file = sys.argv[1:]
    create_notification(recipient, subject, body, Path(output_file))
    print(f"Notification created: {output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
