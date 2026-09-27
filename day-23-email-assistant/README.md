# Day 23: Email Assistant

## Project

Read an incoming email, classify its intent, and create a reply draft. The program never sends the email automatically.

Supported intents:

- billing
- technical
- general

## Run it

```bash
python3 email_assistant.py incoming-email.txt reply-draft.txt
cat reply-draft.txt
```

## Test

```bash
printf '%s\n' 'Hello, my invoice payment was charged twice.' > incoming-email.txt
python3 email_assistant.py incoming-email.txt reply-draft.txt

grep -q 'Intent: billing' reply-draft.txt
grep -q 'billing request' reply-draft.txt
grep -q 'Automation Support' reply-draft.txt
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

An email automation can separate intent detection from response creation. Human review remains in the workflow because the output is a draft, not an automatic send.
