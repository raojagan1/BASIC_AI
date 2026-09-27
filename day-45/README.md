# Day 45: Configuration Validation

## Goal
Reject unsafe deployment settings before startup.

## Build
Validate required variables, allowed log levels, positive ports, and production secrets.

## Test
Run with each invalid setting and verify startup exits before serving traffic.

## Complete when
Bad configuration cannot silently reach production.