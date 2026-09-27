# Day 55: Confidence and Human Fallback

## Goal
Route uncertain decisions to review.

## Build
Set a confidence threshold. High confidence may continue; low confidence creates a review task.

## Test
`0.95` continues; `0.45` enters review and executes no action.

## Complete when
Uncertainty is a controlled workflow state.