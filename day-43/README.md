# Day 43: Metrics

## Goal
Measure automation behavior.

## Build
Track `requests_total`, `request_errors_total`, and `jobs_completed_total`; expose `/metrics`.

## Test
Call an endpoint twice and verify its counter increases by two.

## Complete when
A metric report can show usage and failures.