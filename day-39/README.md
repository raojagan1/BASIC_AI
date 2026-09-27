# Day 39: Background Job Queue

## Goal
Move slow work out of the HTTP request.

## Build
Create a jobs table with `queued`, `running`, `completed`, and `failed` states. Add a submit route and worker.

## Test
Submit one job, run the worker, and verify it reaches `completed` with a result.

## Complete when
The request stays responsive while work runs asynchronously.