# AI Automation Learning Guide

This guide teaches AI automation from the Linux program level and then connects it to software and hardware.

## Automation Structure

Most automation follows:

```text
Trigger -> Program logic -> Action
```

Example:

```text
New file appears -> Python reads it -> Move it to another folder
```

## 1. Linux Automation

### Example: automatic backup

Create a backup script:

```bash
#!/bin/bash

SOURCE="$HOME/Documents"
DEST="$HOME/backups/documents-$(date +%F).tar.gz"

mkdir -p "$HOME/backups"
tar -czf "$DEST" "$SOURCE"

echo "Backup created: $DEST"
```

Save it as:

```text
backup.sh
```

Make it executable:

```bash
chmod +x backup.sh
```

Run it:

```bash
./backup.sh
```

This automates a manual backup task.

### Schedule it with cron

Open the cron editor:

```bash
crontab -e
```

Run the backup every day at 8 PM:

```text
0 20 * * * /home/yourname/backup.sh
```

Linux will now run the program automatically.

## 2. Software Automation

### Example: monitor a folder with Python

```python
from pathlib import Path
import time

folder = Path.home() / "Downloads"

while True:
    for file in folder.iterdir():
        if file.is_file() and file.suffix == ".pdf":
            destination = Path.home() / "Documents" / file.name
            file.rename(destination)
            print(f"Moved {file.name}")

    time.sleep(10)
```

This program checks the Downloads folder every 10 seconds and moves PDF files to Documents.

### Add AI

AI can decide what to do with each file:

```text
New document
    -> AI reads the document
    -> AI identifies its category
    -> Python moves it to the correct folder
```

Possible categories:

- invoices
- resumes
- reports
- personal documents
- unknown files

## 3. Program-to-Program Automation

Linux programs can communicate through:

- command-line arguments
- files
- pipes
- environment variables
- APIs
- webhooks
- databases
- message queues

Example using a pipe:

```bash
cat server.log | grep "ERROR" > errors.txt
```

This means:

```text
Read the log -> Find errors -> Save them
```

Another example:

```bash
df -h | grep "/dev"
```

This checks disk usage and filters the result.

## 4. Hardware Automation

Linux can control hardware using:

- GPIO pins
- USB
- serial ports
- Bluetooth
- network protocols
- Arduino
- Raspberry Pi
- sensors and relays

Example hardware workflow:

```text
Temperature sensor detects heat
    -> Python reads the temperature
    -> If temperature is high
    -> Turn on a fan
```

Simplified Python logic:

```python
temperature = 32

if temperature > 30:
    print("Turn fan ON")
else:
    print("Turn fan OFF")
```

With real hardware, the `print()` statements would be replaced with GPIO commands.

## 5. Combined AI, Software, and Hardware Example

A smart greenhouse could work like this:

```text
Sensor measures soil moisture
    -> Linux program reads the sensor
    -> AI analyzes the plant condition
    -> Python turns on a water pump
    -> System records the result
```

Another example:

```text
Security camera detects movement
    -> AI checks whether a person is present
    -> Linux sends a notification
    -> Hardware alarm turns on
```

## Recommended Learning Order

1. Linux terminal commands
2. Bash scripting
3. Python basics
4. Files and folders
5. Cron and systemd
6. APIs and webhooks
7. AI APIs
8. Raspberry Pi or Arduino
9. Sensors and GPIO
10. Complete AI automation projects

## First Practical Exercise

Run these commands in Linux:

```bash
mkdir -p ~/automation-lab
cd ~/automation-lab
touch input.txt
echo "Automation is useful" > input.txt
cat input.txt
```

You have created a small automated-work environment.

Next, create a Bash program that checks whether `input.txt` exists:

```bash
if [ -f input.txt ]; then
    echo "The file exists"
else
    echo "The file does not exist"
fi
```

This is the foundation of automation:

> Check a condition, then perform an action.

## Daily Project and Test System

Complete one project every day. Do not move to the next day until the test passes.

### Daily workflow

1. Read the day's project.
2. Create a folder named `day-XX-project-name`.
3. Build and run the project.
4. Run the test command or manual test.
5. Record the result in `README.md`.

Use this result format:

```text
Date:
Project:
What I built:
Test result: PASS or FAIL
What I learned:
```

## 30-Day Project Plan

| Day | Project | Test |
| --- | --- | --- |
| 1 | Create an automation workspace with Bash | The workspace and `input.txt` exist |
| 2 | Write a Bash file-existence checker | It prints the correct result for an existing and missing file |
| 3 | Build a Bash backup script | A dated archive is created and can be listed with `tar -tzf` |
| 4 | Check disk usage with Bash | The script warns when a chosen limit is exceeded |
| 5 | Search Linux logs for errors | `errors.txt` contains only matching error lines |
| 6 | Schedule a script with cron | A timestamp file is updated at the scheduled time |
| 7 | Build a system information report | The report contains hostname, kernel, memory, and disk information |
| 8 | Create a Python file organizer | Test files are moved into the correct folders |
| 9 | Rename files using Python | Files receive the expected date or category names |
| 10 | Monitor a folder with Python | A new file is detected and logged |
| 11 | Read and write CSV data | The output CSV contains the expected rows and columns |
| 12 | Create a JSON task tracker | A task can be added, listed, and marked complete |
| 13 | Run a Linux command from Python | Python captures and prints the command's output |
| 14 | Build a seven-day review project | Days 1-13 are documented and all selected tests pass |
| 15 | Call a public API with Python | The program receives valid JSON and prints selected fields |
| 16 | Build a local HTTP server | A browser or `curl` receives the expected response |
| 17 | Create a webhook receiver | A test POST request is logged successfully |
| 18 | Send an email notification | A test event produces one notification |
| 19 | Add retry and error handling | A failed operation retries and records the failure |
| 20 | Build a scheduled API report | The report file contains fresh data after each run |
| 21 | Create an AI text classifier | Test inputs are assigned to the expected categories |
| 22 | Build an AI document summarizer | The summary includes the main facts from a test document |
| 23 | Create an AI email assistant | It produces a draft without sending it automatically |
| 24 | Add human approval to an AI workflow | No action happens until approval is recorded |
| 25 | Build an AI file sorter | Test documents are categorized and moved correctly |
| 26 | Read a sensor value or simulated sensor value | The value is logged with a timestamp |
| 27 | Control an LED or simulated device | The device changes state when the threshold is crossed |
| 28 | Build temperature alert automation | A high-temperature test creates an alert |
| 29 | Build a smart greenhouse simulation | Moisture input causes the correct pump decision |
| 30 | Complete project: AI automation pipeline | Trigger, processing, action, logging, and failure handling all pass |

## Automatic Daily Test Runner

Create a file named `run_daily_test.sh` inside your learning folder:

```bash
#!/bin/bash

set -e

PROJECT_DIR="$HOME/automation-lab"
TEST_LOG="$PROJECT_DIR/daily-test.log"

mkdir -p "$PROJECT_DIR"
printf '%s - Daily test started\n' "$(date '+%F %T')" >> "$TEST_LOG"

if [ -f "$PROJECT_DIR/input.txt" ]; then
    printf '%s - PASS: input.txt exists\n' "$(date '+%F %T')" >> "$TEST_LOG"
else
    printf '%s - FAIL: input.txt is missing\n' "$(date '+%F %T')" >> "$TEST_LOG"
    exit 1
fi

printf '%s - Daily test finished\n' "$(date '+%F %T')" >> "$TEST_LOG"
echo "PASS: daily test completed"
```

Make it executable and run it:

```bash
chmod +x run_daily_test.sh
./run_daily_test.sh
cat "$HOME/automation-lab/daily-test.log"
```

Run the test every day at 8 PM with cron:

```text
0 20 * * * /home/yourname/automation-lab/run_daily_test.sh
```

Replace `/home/yourname` with the result of:

```bash
echo "$HOME"
```

The test runner is a starting point. As each daily project becomes more advanced, replace its file check with that project's real test.

## Days 31-60: Production AI Automation Track

This second track turns the first 30 projects into reliable, secure, deployable systems. Complete one project each day and do not continue until its test passes.

| Day | Project | Test |
| --- | --- | --- |
| 31 | Create a Python virtual environment | A clean environment installs the project dependencies successfully |
| 32 | Add project configuration with environment variables | The program reads a non-secret setting and fails clearly when required configuration is missing |
| 33 | Build a SQLite event database | An event can be inserted, queried, and retrieved after restarting the program |
| 34 | Add database migrations | A fresh database reaches the current schema from an empty state |
| 35 | Build a REST API with input validation | Valid requests return the expected JSON and invalid requests return HTTP 400 |
| 36 | Add API authentication | Requests without a valid token are rejected and valid tokens are accepted |
| 37 | Add pagination and filtering | The API returns the requested page and never returns more than the page size |
| 38 | Add idempotent webhook processing | Replaying the same event does not create duplicate effects |
| 39 | Build a background job queue | A submitted job moves from queued to completed and stores its result |
| 40 | Complete backend checkpoint | API, database, authentication, webhook, and job tests pass together |
| 41 | Add structured JSON logging | Every important event contains a timestamp, level, event name, and request ID |
| 42 | Add health and readiness checks | Health reports process status and readiness reports dependency status separately |
| 43 | Add metrics collection | A test request increments a counter and exposes the expected metric |
| 44 | Build an audit trail | Every state-changing action records actor, action, target, and timestamp |
| 45 | Add configuration validation | Invalid production configuration fails before the service starts |
| 46 | Add unit tests for business rules | The test suite covers normal, boundary, and invalid inputs |
| 47 | Add integration tests | A test starts the service and verifies the API-to-database workflow |
| 48 | Add contract tests for an external API | A changed response shape is detected by a failing test |
| 49 | Add safe retry with backoff | A transient failure retries with increasing delays and a permanent failure stops |
| 50 | Complete reliability checkpoint | Logging, health, metrics, audit, unit, integration, and retry tests pass |
| 51 | Build a document retrieval index | A query returns the most relevant stored document |
| 52 | Add retrieval-augmented generation | The answer includes citations to the retrieved source documents |
| 53 | Add AI output schema validation | Malformed model output is rejected and a valid structured output is accepted |
| 54 | Add prompt versioning | Every generated result records the prompt version used |
| 55 | Add AI confidence and fallback | Low-confidence input routes to human review instead of an automatic action |
| 56 | Add prompt-injection protection | Instructions inside untrusted document text cannot override system rules |
| 57 | Add sensitive-data redaction | Email addresses and secret-like values are removed before model processing |
| 58 | Measure AI quality on a test set | The evaluation report contains accuracy, failures, and representative examples |
| 59 | Add human feedback capture | A reviewer can approve, reject, and comment on an AI result |
| 60 | Complete production portfolio project | One end-to-end system passes functional, security, reliability, and AI quality tests |

### Recommended capstone for Days 51-60

Build an **AI operations assistant**:

```text
Webhook or uploaded document
    -> validate and redact input
    -> retrieve relevant knowledge
    -> classify and summarize with structured output
    -> request human approval for risky actions
    -> execute an approved action
    -> store an audit record and metrics
```

### Day 60 completion standard

Your final project should include:

- a reproducible setup command
- a README with architecture and example requests
- automated unit and integration tests
- authentication and input validation
- structured logs and an audit trail
- a failure and retry policy
- human approval for consequential actions
- redaction of sensitive data
- a short AI evaluation report
