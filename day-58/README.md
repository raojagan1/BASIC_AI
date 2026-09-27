# Day 58: AI Quality Evaluation

## Goal
Measure AI behavior on a fixed test set.

## Build
Create `evaluation.jsonl` with input, expected category, and safety behavior. Write an evaluator for total, correct, accuracy, and failures.

```bash
python3 evaluate.py evaluation.jsonl
```

## Test
The report contains accuracy and representative failure examples.

## Complete when
AI improvements are measured instead of guessed.