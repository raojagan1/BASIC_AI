# Day 60: AI Operations Assistant Capstone

## Goal
Build one production-style AI automation system.

## Pipeline
```text
Webhook or document -> validate and redact -> retrieve knowledge -> structured AI result -> human approval -> action -> audit, metrics, feedback
```

## Required tests
1. Valid input completes.
2. Invalid input is rejected.
3. Duplicate events create one effect.
4. Sensitive values are redacted.
5. Untrusted instructions cannot approve actions.
6. Low confidence requires approval.
7. Approved actions are audited.
8. External failures retry and report failure.
9. AI evaluation produces a quality report.
10. Clean setup and README reproduce the project.

## Complete when
The system passes functional, security, reliability, and AI quality tests and is documented as a portfolio project.