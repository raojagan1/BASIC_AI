# Day 49: Retry with Exponential Backoff

## Goal
Recover from temporary failures without retry storms.

## Build
Use delays such as `0.25`, `0.5`, and `1.0` seconds, a maximum attempt count, and an exception allowlist.

## Test
A fake service fails twice then succeeds; a permanent error is not retried.

## Complete when
Temporary outages recover and permanent failures stop clearly.