# Day 57: Sensitive-Data Redaction

## Goal
Remove secrets and personal data before model processing.

## Build
Redact email addresses, bearer tokens, API keys, and common secret formats; record only redaction counts in normal logs.

## Test
Model input contains no test email or token, while the redaction count is recorded.

## Complete when
Less sensitive data leaves the local boundary.