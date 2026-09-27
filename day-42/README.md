# Day 42: Health and Readiness

## Goal
Separate process health from dependency readiness.

## Build
Add `/health` for process status and `/ready` for database/API dependency status.

## Test
When a dependency is unavailable, `/health` remains 200 while `/ready` returns 503 with the failed dependency.

## Complete when
Deployment systems know whether to restart or remove an instance from traffic.