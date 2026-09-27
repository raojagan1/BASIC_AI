# Day 48: External API Contract Test

## Goal
Detect incompatible provider responses.

## Build
Store an expected response schema and validate live or fixture responses against it.

## Test
A fixture missing a required field must fail the contract test.

## Complete when
External API changes become visible test failures.