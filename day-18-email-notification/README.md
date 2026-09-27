# Day 18: Email Notification Automation

## Project

Create an email notification automatically when an event occurs. This exercise writes an `.eml` file for review instead of sending mail to a real address.

## Run it

```bash
python3 send_notification.py \
  learner@example.com \
  "Automation test" \
  "The daily automation test passed." \
  "$HOME/automation-lab/notifications/test.eml"
```

Open the resulting `.eml` file with an email client or inspect it with:

```bash
cat "$HOME/automation-lab/notifications/test.eml"
```

## Test

The generated message must contain the recipient, subject, and body:

```bash
python3 send_notification.py \
  learner@example.com \
  "Automation test" \
  "The daily automation test passed." \
  "$HOME/automation-lab/notifications/test.eml"
message="$HOME/automation-lab/notifications/test.eml"
grep -q 'To: learner@example.com' "$message"
grep -q 'Subject: Automation test' "$message"
grep -q 'The daily automation test passed.' "$message"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Python's `email` module creates a correctly formatted email message. Saving a preview first is a safe way to test notification automation before configuring a real SMTP service.
